

# Generated at 2022-06-13 01:48:27.056448
# Unit test for method get_interfaces_info of class SunOSNetwork

# Generated at 2022-06-13 01:48:30.383453
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    network = SunOSNetworkCollector('sol', 'test_module')

    assert network._fact_class is not None
    assert network._platform == 'SunOS'
    assert isinstance(network._fact_class(), SunOSNetwork)

# Generated at 2022-06-13 01:48:40.946778
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():

    class ModuleMock(object):
        def __init__(self):
            self.run_command_exit_status = 0
            self.run_command_calls = []
            self.run_command_results = []

        def run_command(self, args):
            self.run_command_calls.append(args)
            rc, out, err = self.run_command_results.pop(0)
            return rc, out, err

    mod = ModuleMock()
    net = SunOSNetwork(module=mod)

# Generated at 2022-06-13 01:48:51.555719
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    module = NetworkCollector()
    interfaces, ips = module.get_interfaces_info('/sbin/ifconfig')
    assert 'lo0' in interfaces
    assert 'en0' in interfaces
    assert 'en0' in ips['all_ipv4_addresses']
    assert '192.168.2.3' in ips['all_ipv4_addresses']
    assert '192.168.2.3' in interfaces['en0']['ipv4'][0]['address']
    assert 'fe80::5054:ff:fe0d:c4b4' in interfaces['en0']['ipv6'][0]['address']


# Generated at 2022-06-13 01:49:00.168838
# Unit test for method parse_interface_line of class SunOSNetwork
def test_SunOSNetwork_parse_interface_line():
    # Input data
    line = "lo0: "
    words = line.split()

    # Expected output
    current_if = {'device': 'lo0', 'ipv4': [], 'ipv6': [], 'type': 'unknown'}
    interfaces = {'lo0': current_if}

    ifconfig = SunOSNetwork(None)
    output = ifconfig.parse_interface_line(words, current_if, interfaces)

    assert current_if == {'device': 'lo0', 'ipv4': [], 'ipv6': [], 'type': 'unknown'}
    assert interfaces == {'lo0': {'device': 'lo0', 'ipv4': [], 'ipv6': [], 'type': 'unknown'}}

# Generated at 2022-06-13 01:49:03.229076
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    assert SunOSNetworkCollector._platform == 'SunOS'
    assert SunOSNetworkCollector._fact_class == SunOSNetwork



# Generated at 2022-06-13 01:49:04.171391
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    assert SunOSNetworkCollector.platform == 'SunOS'


# Generated at 2022-06-13 01:49:12.284113
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    module = AnsibleModule(argument_spec={})

# Generated at 2022-06-13 01:49:13.909036
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    collector = SunOSNetworkCollector()
    assert collector.platform == 'SunOS'

# Generated at 2022-06-13 01:49:17.618173
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    """
    This function tests SunOSNetwork with "ifconfig -a" output.

    It is expected to test:
     - IPv4 and IPv6 facts for the same interface are in separate dicts
     - 'macaddress' is parsed
     - 'media' is parsed
     - 'status' is parsed
     - 'lladdr' is parsed

    This is a best effort approach. Commands may not be installed on the system.
    """
    module = type('Module', (object,), {'run_command': run_command})
    SunOSNetwork = type('SunOSNetwork', (object,), {'module': module, 'ipv': 'ipv4'})

    network = SunOSNetwork()
    interfaces, ips = network.get_interfaces_info('ifconfig')

# Generated at 2022-06-13 01:49:24.487849
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    SunOSNetworkCollector()

# Generated at 2022-06-13 01:49:34.136492
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    module = MockModule()
    ifconfig_path = '/sbin/ifconfig'
    network_class = SunOSNetwork(module)

# Generated at 2022-06-13 01:49:35.294118
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    assert SunOSNetworkCollector()

# Generated at 2022-06-13 01:49:46.601045
# Unit test for method parse_interface_line of class SunOSNetwork
def test_SunOSNetwork_parse_interface_line():
    module = type('', (), {})()  # Module class with empty name and namespace
    module.run_command = lambda *args, **kwargs: (0, '', '')
    interfaces = {}
    current_if = {}
    net = SunOSNetwork(module)
    words = ['lo0:', 'flags=2001000849', 'mtu', '8232', 'index', '1']
    current_if = net.parse_interface_line(words, current_if, interfaces)
    assert current_if['device'] == 'lo0'
    assert current_if['type'] == 'unknown'
    assert current_if['ipv4'][0]['mtu'] == '8232'

# Generated at 2022-06-13 01:49:51.204129
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    # test_SunOSNetworkCollector:
    module = NetworkCollector._create_module('SunOS')
    collector = SunOSNetworkCollector(module)
    # Default value for network facts
    network_facts = dict(
        interfaces=dict(),
        default_ipv4=dict(),
        default_ipv6=dict(),
        all_ipv4_addresses=list(),
        all_ipv6_addresses=list(),
    )
    # Check that collector.get_network_facts() returns a dictionary of expected keys.
    assert collector.get_network_facts() == network_facts

# Generated at 2022-06-13 01:50:03.113210
# Unit test for method parse_interface_line of class SunOSNetwork
def test_SunOSNetwork_parse_interface_line():
    # Create a SunOSNetwork object and give it the test data
    t = SunOSNetwork({})
    interfaces = {}
    current_if = {}

# Generated at 2022-06-13 01:50:07.649719
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    # Given
    results = dict(failed=False, changed=False, skipped=False, succeeded=False)
    module_mock = MagicMock(return_value=MagicMock(**results))
    facts = dict(FACTS={})
    # When
    net = SunOSNetworkCollector(module_mock, facts)
    # Then
    assert net is not None
    assert net._facts is not None
    assert net._module is not None
    assert net._platform is not None


# Generated at 2022-06-13 01:50:12.789441
# Unit test for method get_interfaces_info of class SunOSNetwork

# Generated at 2022-06-13 01:50:17.504417
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    module = ansible.module_utils.basic.AnsibleModule(argument_spec=dict())
    collector = SunOSNetworkCollector(module=module)
    out = collector.get_interfaces_info("/usr/bin/ifconfig")
    assert out is not None

# Generated at 2022-06-13 01:50:18.895752
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    assert issubclass(SunOSNetworkCollector, NetworkCollector)


# Generated at 2022-06-13 01:50:33.289224
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    obj = SunOSNetworkCollector(None, None, list(), dict())
    assert obj._platform == 'SunOS'
    assert obj._fact_class is SunOSNetwork


# Generated at 2022-06-13 01:50:44.747756
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():

    # Interface mac address
    mac_address = "1c:4b:d6:d4:6f:65"
    mac_address_invalid = "00:00:00:00:00:00"

    # Interface with ipv4 link local address
    i1 = "lo0: flags=2002000849<UP,LOOPBACK,RUNNING,MULTICAST,IPv4,VIRTUAL> mtu 8232 index 1\n" \
         "        inet 127.0.0.1 netmask ff000000\n"

    # Interface with ipv6 link local address

# Generated at 2022-06-13 01:50:45.805858
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    SunOSNetworkCollector()

# Generated at 2022-06-13 01:50:47.959524
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    assert SunOSNetworkCollector._platform == 'SunOS'
    assert SunOSNetworkCollector._fact_class == SunOSNetwork

# Generated at 2022-06-13 01:50:49.818209
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    network = SunOSNetworkCollector()
    assert network.platform == 'SunOS'

# Generated at 2022-06-13 01:50:59.918305
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    """
    Test that the correct interface data is collected for Solaris
    """
    ifconfig_path = 'tests/unit/module_utils/facts/network/generic_bsd/ifconfig/Solaris.txt'
    with open(ifconfig_path, 'r') as test_output:
        testing = test_output.read()

    test_network = SunOSNetwork()
    test_interfaces, test_ips = test_network.get_interfaces_info(ifconfig_path)

# Generated at 2022-06-13 01:51:01.587876
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    obj = SunOSNetworkCollector()
    obj.get_all_network_interfaces()

# Generated at 2022-06-13 01:51:06.230230
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    facts = SunOSNetworkCollector()
    assert isinstance(facts, SunOSNetworkCollector)
    assert isinstance(facts._fact_class, SunOSNetwork)
    assert facts._platform == 'SunOS'

# Generated at 2022-06-13 01:51:15.688740
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    fake_module = FakeModule()
    interfaces, ips = SunOSNetwork(fake_module).get_interfaces_info('')
    assert interfaces['lo0']['ipv4'][0]['address'] == '127.0.0.1'
    assert interfaces['lo0']['ipv4'][0]['netmask'] == '255.0.0.0'
    assert interfaces['lo0']['ipv6'][0]['address'] == '::1'
    assert interfaces['lo0']['ipv6'][0]['prefix'] == '128'
    assert interfaces['lo0']['mtu'] == '8232'
    assert interfaces['lo0']['type'] == 'loopback'

# Generated at 2022-06-13 01:51:22.193626
# Unit test for method parse_interface_line of class SunOSNetwork
def test_SunOSNetwork_parse_interface_line():
    iface = {}
    ifaces = {}
    words = ['e1000g1:', 'flags=201000843', 'mtu', '1500']

    iface = SunOSNetwork().parse_interface_line(words, iface, ifaces)
    assert iface == {'device': 'e1000g1', 'ipv4': [{'flags': 'flags=201000843', 'mtu': '1500'}], 'ipv6': [], 'type': 'unknown'}

    ifaces = {'e1000g1': {'device': 'e1000g1', 'ipv4': [{'flags': 'flags=201000843', 'mtu': '1500'}], 'ipv6': [], 'type': 'unknown'}}

# Generated at 2022-06-13 01:51:51.321134
# Unit test for method parse_interface_line of class SunOSNetwork
def test_SunOSNetwork_parse_interface_line():
    current_if = {}
    interfaces = {}
    words = ['net0:', 'flags=2004841<UP,LOOPBACK,RUNNING,MULTICAST,IPv4>', 'mtu=8232']
    result = SunOSNetwork().parse_interface_line(words, current_if, interfaces)
    assert result['device'] == 'net0'
    assert result['macaddress'] == 'unknown'
    assert result['type'] == 'loopback'
    assert result['ipv4'][0]['flags'] == ['UP', 'LOOPBACK', 'RUNNING', 'MULTICAST', 'IPv4']
    assert result['ipv4'][0]['mtu'] == '8232'
    assert result['ipv6'] == []

# Generated at 2022-06-13 01:52:00.982318
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    from ansible.module_utils.facts.network.sunos.facts import SunOSNetwork


# Generated at 2022-06-13 01:52:10.306109
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    module = type('', (), {
        'run_command': SunOSNetwork.run_command,
        '_load_params': lambda self: None,
    })
    instance = SunOSNetwork(module)

# Generated at 2022-06-13 01:52:12.809014
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    obj = SunOSNetworkCollector()
    assert obj.platform == 'SunOS'
    assert obj.fact_class is SunOSNetwork
    assert obj.config == {}


# Generated at 2022-06-13 01:52:14.034007
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    # TODO: create a fake 'ifconfig -a' output
    return

# Generated at 2022-06-13 01:52:22.704729
# Unit test for method parse_interface_line of class SunOSNetwork
def test_SunOSNetwork_parse_interface_line():
    """Unit testing for 'parse_interface_line()' method"""
    # Test SunOS interface parsing
    module = type('', (), {})()
    module.run_command = lambda args: (0, '', '')
    module.params = {}
    sn = SunOSNetwork(module)
    interfaces = {}
    current_if = {}
    # Test 1a: parse valid IPv4 line
    words = ['e1000g0:', 'flags=1000843<UP,BROADCAST,RUNNING,MULTICAST,IPv4>', 'mtu=1500']
    current_if = sn.parse_interface_line(words, current_if, interfaces)
    assert current_if['device'] == 'e1000g0'
    assert 'mtu' in current_if['ipv4'][0]

# Generated at 2022-06-13 01:52:25.725215
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    facts = {}
    SunOSNetworkCollector(facts, None).populate()
    assert 'SunOS' == facts['ansible_net_platform']

# Generated at 2022-06-13 01:52:28.414710
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    from ansible.module_utils.facts.network.sunos import SunOSNetworkCollector
    obj = SunOSNetworkCollector()
    assert obj.platform == 'SunOS'

# Generated at 2022-06-13 01:52:38.416580
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    module = AnsibleModuleMock()
    ifconfig_path = os.path.join(os.path.dirname(__file__), "fixtures", "ifconfig_SunOS")
    with open(ifconfig_path, 'r') as f:
        ifconfig_out = f.read()
    module.run_command.return_value = (0, ifconfig_out, '')
    sunos_net = SunOSNetwork(module)
    interfaces, ips = sunos_net.get_interfaces_info(ifconfig_path)
    assert len(interfaces) == 2
    assert len(ips) == 2
    assert 'ipv4' in interfaces['lo0']
    assert 'ipv6' in interfaces['lo0']
    assert 'ipv4' in interfaces['net0']
    assert 'ipv6'

# Generated at 2022-06-13 01:52:48.919305
# Unit test for method get_interfaces_info of class SunOSNetwork

# Generated at 2022-06-13 01:53:34.525526
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    obj = SunOSNetworkCollector()
    assert obj._fact_class is SunOSNetwork


# Generated at 2022-06-13 01:53:36.288658
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    fact_class = SunOSNetworkCollector()
    assert fact_class._platform == 'SunOS'


# Generated at 2022-06-13 01:53:39.032085
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    # Module instantiation does not have side effects.
    # Just verify that it does not throw an exception.
    SunOSNetworkCollector()

# Generated at 2022-06-13 01:53:48.615299
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    datadir = os.path.join(os.path.dirname(__file__), '../../../fixtures/network/')
    facts_module, output, _warnings = Facts(
        dict(
            gather_subset='!all',
            gather_network_resources=['interfaces'],
            gather_network_resources_facts=True
        ),
        [],
        datadir=datadir
    ).get_facts()

    expected_output = json.loads(open(datadir + 'SunOS-ifconfig_a.json').read())

    assert output['ansible_network_resources']['interfaces'] == expected_output['ansible_network_resources']['interfaces']

# Generated at 2022-06-13 01:53:50.336739
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    network = SunOSNetworkCollector()
    assert network.platform == 'SunOS'
    assert network.fact_class == SunOSNetwork

# Generated at 2022-06-13 01:53:54.151526
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    """Test SunOSNetworkCollector constructor"""
    assert SunOSNetworkCollector._platform == 'SunOS'
    assert SunOSNetworkCollector._fact_class == SunOSNetwork
    c = SunOSNetworkCollector()
    assert c._platform == 'SunOS'
    assert c._fact_class == SunOSNetwork

# Generated at 2022-06-13 01:53:55.819044
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    obj = SunOSNetworkCollector()

if __name__ == '__main__':
    test_SunOSNetworkCollector()

# Generated at 2022-06-13 01:54:05.224820
# Unit test for constructor of class SunOSNetworkCollector

# Generated at 2022-06-13 01:54:09.868465
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    """
    This is to test the constructor of class SunOSNetworkCollector.
    """
    object_SunOSNetworkCollector = SunOSNetworkCollector()
    assert object_SunOSNetworkCollector._fact_class == SunOSNetwork
    assert object_SunOSNetworkCollector._platform == 'SunOS'

# Generated at 2022-06-13 01:54:14.378345
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    assert hasattr(SunOSNetworkCollector, '_platform')
    assert hasattr(SunOSNetworkCollector, '_fact_class')
    assert SunOSNetworkCollector._platform == 'SunOS'
    assert SunOSNetworkCollector._fact_class == SunOSNetwork


# Generated at 2022-06-13 01:55:50.957534
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    module = type('test_module', (object, ), dict(params=dict(gather_subset=[])))
    net = SunOSNetworkCollector(module)
    assert net is not None


# Generated at 2022-06-13 01:55:59.695369
# Unit test for method get_interfaces_info of class SunOSNetwork

# Generated at 2022-06-13 01:56:03.828637
# Unit test for method parse_interface_line of class SunOSNetwork
def test_SunOSNetwork_parse_interface_line():
    iface = {'device': 'lo0', 'ipv4': [], 'ipv6': [], 'type': 'unknown'}
    line = 'lo0: flags=2001000849 mtu 8232 index 3'
    expected_result = {'device': 'lo0', 'ipv4':[{'flags': ['UP', 'LOOPBACK', 'RUNNING', 'MULTICAST'], 'mtu': '8232'}], 'ipv6': [], 'type': 'loopback'}
    result = SunOSNetwork().parse_interface_line(line.split(), iface, {})
    assert expected_result == result

# Generated at 2022-06-13 01:56:04.650254
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    assert SunOSNetworkCollector


# Generated at 2022-06-13 01:56:06.769948
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    obj = SunOSNetworkCollector()
    assert hasattr(obj, 'platform')
    assert hasattr(obj, '_fact_class')


# Generated at 2022-06-13 01:56:09.916595
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    o = SunOSNetworkCollector()
    assert o.__class__.__name__ == 'SunOSNetworkCollector'

# Generated at 2022-06-13 01:56:12.198428
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    c = SunOSNetworkCollector()
    assert c.platform == 'SunOS'
    assert c.fact_class == SunOSNetwork

# Generated at 2022-06-13 01:56:23.851926
# Unit test for method parse_interface_line of class SunOSNetwork
def test_SunOSNetwork_parse_interface_line():
    interfaces = {}
    current_if = {}
    words = ['xge0:', '<BROADCAST,MULTICAST,UP,LOWER_UP>', 'mtu', '9000', 'ip', '172.16.73.125', 'netmask', 'ffffff00', 'broadcast', '172.16.73.255']
    current_if = SunOSNetwork.parse_interface_line(None, words, current_if, interfaces)
    assert current_if['device'] == 'xge0'
    assert current_if['ipv4'][0]['flags'] == ['BROADCAST', 'MULTICAST', 'UP', 'LOWER_UP']
    assert current_if['ipv4'][0]['mtu'] == '9000'

    # SunOS displays single digit octets in MAC addresses e.

# Generated at 2022-06-13 01:56:25.935937
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    obj = SunOSNetworkCollector()
    assert obj
    assert obj._fact_class == SunOSNetwork
    assert obj._platform == 'SunOS'

# Generated at 2022-06-13 01:56:30.972382
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    m_module = MagicMock()
    m_module.get_bin_path.return_value = '/sbin/ifconfig'
    m_facts = SunOSNetworkCollector(m_module).collect()
    assert m_facts['default_ipv4']['gateway'] == '10.0.0.1'
    assert m_facts['interfaces']['lo0']['macaddress'] == '00:00:00:00:00:00'