

# Generated at 2022-06-13 01:48:24.784473
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    '''get_interfaces_info(ifconfig_path)'''
    from ansible.module_utils.facts.network.sunos import SunOSNetwork

    ifconfig_path = '/sbin/ifconfig'
    ip_path = '/usr/bin/ip'
    module = AnsibleModuleMock()


# Generated at 2022-06-13 01:48:25.807026
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    obj = SunOSNetworkCollector()
    assert obj.platform == 'SunOS'


# Generated at 2022-06-13 01:48:27.249484
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    """ Test whether SunOSNetworkCollector can be initialized """

    sunos_collector = SunOSNetworkCollector()
    assert sunos_collector is not None


# Generated at 2022-06-13 01:48:29.657967
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    collector = SunOSNetworkCollector()
    assert collector.platform == 'SunOS'


# Generated at 2022-06-13 01:48:31.567213
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    net_collector = SunOSNetworkCollector()
    assert isinstance(net_collector._fact_class, SunOSNetwork)


# Generated at 2022-06-13 01:48:32.746712
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    collector = SunOSNetworkCollector()
    assert collector._platform == 'SunOS'

# Generated at 2022-06-13 01:48:43.388606
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    module = AnsibleModule(argument_spec=dict())
    ifconfig_path = module.get_bin_path('ifconfig')
    obj = SunOSNetwork(module)
    interfaces, ips = obj.get_interfaces_info(ifconfig_path)

# Generated at 2022-06-13 01:48:50.215873
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():

    # Get a SunOSNetwork object
    sunos_network = SunOSNetwork()

    # Path to custom test file with ifconfig -a output
    ifconfig_path = os.path.join(os.getcwd(), 'tests/unittests/fixtures/SunOS_ifconfig_a.txt')

    # Run test method with custom test file
    interfaces, ips = sunos_network.get_interfaces_info(ifconfig_path)

    # Test that the correct interfaces have been found
    assert len(interfaces) == 4
    assert 'lo0' in interfaces
    assert 'lo1' in interfaces
    assert 'net0' in interfaces
    assert 'net1' in interfaces

    # Test that the IPv4 and IPv6 facts are properly nested
    assert len(interfaces['lo1']['ipv4']) == 1


# Generated at 2022-06-13 01:48:58.439333
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    """
    Test method get_interfaces_info for class SunOSNetwork.
    """
    #
    #  Test data:
    #
    #  Sample of "ifconfig -a" output on Solaris 11.1:
    #
    #  lo0: flags=2001000849<UP,LOOPBACK,RUNNING,MULTICAST,IPv4,VIRTUAL> mtu 8232 index 2
    #          inet 127.0.0.1 netmask ff000000
    #          inet6 ::1/128
    #          ether 8:0:20:36:4c:4e
    #          options=80003<RXCSUM,TXCSUM,LINKSTATE>
    #  vnic0: flags=201000843<UP,BROADCAST,RUNNING,MULTICAST,IP

# Generated at 2022-06-13 01:49:09.559185
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    module = AnsibleModule(argument_spec={})
    ifconfig_path = module.get_bin_path('ifconfig')

    # Make an instance of SunOSNetwork
    my_sunos_net = SunOSNetwork(module)

    # Get interfaces information
    interfaces, ips = my_sunos_net.get_interfaces_info(ifconfig_path)

    # Check that the interfaces exist
    assert interfaces is not None

    # Check that the ip facts exist
    assert ips is not None

    # Check that each interface has an ipv6 and ipv4 fact
    # (Dict/List)
    for iface in interfaces:
        assert 'ipv4' in interfaces[iface]
        assert 'ipv6' in interfaces[iface]

    # Check that each ipv4/ipv6 interface fact is a list

# Generated at 2022-06-13 01:49:17.195155
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    obj = SunOSNetworkCollector()
    assert obj.platform == 'SunOS'
    assert obj.fact_class == SunOSNetwork
    assert obj.fact_class().platform == 'SunOS'


# Generated at 2022-06-13 01:49:24.575121
# Unit test for method get_interfaces_info of class SunOSNetwork

# Generated at 2022-06-13 01:49:26.682305
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():

    c = SunOSNetworkCollector()
    assert c._fact_class == SunOSNetwork
    assert c._platform == 'SunOS'

# Generated at 2022-06-13 01:49:36.047948
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    """ Test get_interfaces_info of class SunOSNetwork """
    mock_module = MockModule({'ANSIBLE_MODULE_ARGS': dict(gather_subset='!all,!min')})
    mock_module.params['gather_network_resources'] = ['interfaces']
    network = SunOSNetwork(mock_module)
    ifconfig_path = network.get_bin_path('ifconfig')
    network.get_interfaces_info(ifconfig_path)

# Generated at 2022-06-13 01:49:47.174215
# Unit test for method parse_interface_line of class SunOSNetwork
def test_SunOSNetwork_parse_interface_line():
    iface = {'device': 'net0', 'ipv4': [], 'ipv6': [], 'type': 'unknown'}
    sut = {'device': 'net0', 'ipv4': [{'mtu': 1500, 'flags': ['IPv4', 'BROADCAST', 'RUNNING', 'MULTICAST']}], 'ipv6': [], 'type': 'unknown'}
    words = ['net0:', 'flags=843<UP,BROADCAST,RUNNING,MULTICAST>', 'mtu', '1500']
    test = SunOSNetwork()
    test.parse_interface_line(words, iface, {})
    assert sut == iface


# Generated at 2022-06-13 01:49:49.904306
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    collector = SunOSNetworkCollector()
    assert collector.platform == 'SunOS'
    assert collector.fact_class == SunOSNetwork

# Generated at 2022-06-13 01:50:01.740303
# Unit test for method get_interfaces_info of class SunOSNetwork

# Generated at 2022-06-13 01:50:02.360821
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    from .. import SunOSNetworkCollector


# Generated at 2022-06-13 01:50:09.127599
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    from ansible.module_utils.facts.network.sunos import SunOSNetwork

    network = SunOSNetwork()
    network.module = AnsibleModule(argument_spec=dict())

    output = ''
    output += '\n'   # keepalive0
    output += 'lo0: flags=2001000849<UP,LOOPBACK,RUNNING,MULTICAST,IPv4,VIRTUAL> mtu 8232 index 1\n'
    output += '        inet 127.0.0.1 netmask ff000000 \n'
    output += '        inet6 ::1/128 \n'
    output += '        ether 8:0:20:a7:86:10 \n'
    output += '        nd6 options=21<PERFORMNUD,AUTO_LINKLOCAL>\n'


# Generated at 2022-06-13 01:50:10.313861
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    assert SunOSNetworkCollector._fact_class == SunOSNetwork
    assert SunOSNetworkCollector._platform == 'SunOS'


# Generated at 2022-06-13 01:50:19.244432
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    obj = SunOSNetworkCollector()
    assert obj._fact_class.platform == 'SunOS'
    assert obj._platform == 'SunOS'
    assert obj.platforms == ['SunOS']

# Generated at 2022-06-13 01:50:29.130473
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():

    class MySunOSNetwork(SunOSNetwork):
        def __init__(self, module):
            self.module = module

    net1 = MySunOSNetwork(module=None)
    interfaces, ips = net1.get_interfaces_info('ifconfig')
    assert len(interfaces) == 3
    assert interfaces['net0']['ipv4'][0]['netmask'] == '255.255.255.0'
    assert interfaces['net0']['ipv4'][0]['inet'][0]['address'] == '172.16.218.178'
    assert interfaces['net0']['ipv4'][0]['inet'][0]['netmask'] == '255.255.255.0'

# Generated at 2022-06-13 01:50:31.849593
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    collector = SunOSNetworkCollector()
    assert collector.platform == 'SunOS'

# Generated at 2022-06-13 01:50:34.056420
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    collector = SunOSNetworkCollector
    assert collector._fact_class == SunOSNetwork
    assert collector._platform == 'SunOS'

# Generated at 2022-06-13 01:50:45.478299
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():

    # Create a test class instance
    test_class = SunOSNetwork()

    # Create a dictionary from the output of the 'ifconfig -a' command ('out' variable)
    test_dict = {}
    for line in out.splitlines():
        if '=' in line:
            key, value = line[0:-1].split('=', 1)
            test_dict[key] = value

    # Run the method get_interfaces_info of class SunOSNetwork given the command's output
    # as input.
    interfaces, ips = test_class.get_interfaces_info(test_dict)

    # Check that the returned interfaces dictionary has the expected content
    assert interfaces['net0']['device'] == 'net0'

# Generated at 2022-06-13 01:50:46.651702
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    assert SunOSNetworkCollector is not None

# Generated at 2022-06-13 01:50:57.956681
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    '''
    unit test for method get_interfaces_info of class SunOSNetwork
    '''
    ifconfig_path = '/sbin/ifconfig'

# Generated at 2022-06-13 01:51:10.351453
# Unit test for method get_interfaces_info of class SunOSNetwork

# Generated at 2022-06-13 01:51:22.729691
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    facts = SunOSNetworkCollector().collect()
    assert facts['network']['interfaces']['em2']['active'] == False
    assert facts['network']['interfaces']['em2']['device'] == "em2"
    assert facts['network']['interfaces']['em2']['macaddress'] == "00:11:22:33:44:55"
    assert facts['network']['interfaces']['em2']['mtu'] == 1500
    assert facts['network']['interfaces']['em2']['type'] == "ether"

# Generated at 2022-06-13 01:51:24.915768
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    facts = SunOSNetworkCollector(None, None, None, None, None, None)
    assert facts._fact_class._platform == 'SunOS'

# Generated at 2022-06-13 01:51:44.793853
# Unit test for method parse_interface_line of class SunOSNetwork
def test_SunOSNetwork_parse_interface_line():
    # define input variables
    words = 'lo0:8 flags=2001000849<UP,LOOPBACK,RUNNING,MULTICAST,IPv4,VIRTUAL> mtu 8232 index 1'
    words = words.split()

    interfaces = {}
    current_if = {}

    # define expected output
    expected_current_if = {'device': 'lo0', 'ipv4': [{'flags': '2001000849<UP,LOOPBACK,RUNNING,MULTICAST,IPv4,VIRTUAL>', 'mtu': '8232'}], 'type': 'loopback', 'ipv6': [], 'macaddress': 'unknown'}

    # instantiate the SunOSNetwork class
    sunosnetwork = SunOSNetwork()

    # call the parse_interface_line method
    current

# Generated at 2022-06-13 01:51:54.214276
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    # Test interface parsing.
    collector = SunOSNetworkCollector()

# Generated at 2022-06-13 01:51:56.259596
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    assert SunOSNetworkCollector._platform == 'SunOS'
    assert SunOSNetworkCollector._fact_class == SunOSNetwork

# Generated at 2022-06-13 01:52:05.134773
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    """get_interfaces_info() returns a tuple of two dictionaries, the first contains all interfaces info, the second
    contains info about all IP addresses.
    """
    module = FakeAnsibleModule()

# Generated at 2022-06-13 01:52:14.864780
# Unit test for method get_interfaces_info of class SunOSNetwork

# Generated at 2022-06-13 01:52:23.152162
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    def mock_execute(module, command):
        return 0, test_out, ''
    test_collector = SunOSNetworkCollector()

# Generated at 2022-06-13 01:52:25.558186
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    obj = SunOSNetworkCollector()
    assert obj._fact_class == SunOSNetwork


# Generated at 2022-06-13 01:52:27.790413
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    assert SunOSNetworkCollector._platform == 'SunOS'
    assert SunOSNetworkCollector._fact_class == SunOSNetwork



# Generated at 2022-06-13 01:52:31.046025
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    # Ensure only SunOSNetworkCollector is loaded when run on Solaris/illumos.
    # Explicitly setting platform to SunOS also works.
    SunOSNetworkCollector()

# Generated at 2022-06-13 01:52:32.974807
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    sunos_test = SunOSNetworkCollector()
    assert sunos_test._fact_class.platform == 'SunOS'

# Generated at 2022-06-13 01:52:53.403819
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    """Test SunOSNetworkCollector constructor"""
    from ansible.module_utils.facts.network.sunos.SunOSNetworkCollector import SunOSNetworkCollector
    SunOSNetworkCollector()

# Generated at 2022-06-13 01:52:58.327430
# Unit test for method parse_interface_line of class SunOSNetwork
def test_SunOSNetwork_parse_interface_line():
    current_if = {}
    interfaces = {}
    words = ['lo0:', 'flags=2001000849<UP,LOOPBACK,RUNNING,MULTICAST,IPv4,VIRTUAL>', 'mtu', '8232']
    current_if = SunOSNetwork.parse_interface_line(None, words, current_if, interfaces)
    assert(current_if['type'] == 'loopback')
    assert(current_if['ipv4'][0]['mtu'] == '8232')
    assert(current_if['ipv6'] == [])

# Generated at 2022-06-13 01:53:02.127313
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    network_collector = SunOSNetworkCollector()
    assert network_collector
    assert network_collector.platform == 'SunOS'
    assert network_collector.fact_class == SunOSNetwork

# Generated at 2022-06-13 01:53:15.317426
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    from ansible.module_utils.facts.network.sunos import SunOSNetwork

    sunos_mod = SunOSNetwork({})
    ifconfig_path = 'tests/unit/module_utils/facts/network/ifconfig_output/SunOS_ifconfig_a_wireless_ipv6'
    interfaces, ips = sunos_mod.get_interfaces_info(ifconfig_path)

# Generated at 2022-06-13 01:53:20.281787
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    sunos_facts = SunOSNetworkCollector().collect()[0]
    assert sunos_facts.__class__.__name__ == 'SunOSNetwork', \
        'sunos_facts.__class__.__name__ == {0!r}, should be {1!r}'.format(
            sunos_facts.__class__.__name__, 'SunOSNetwork'
        )


if __name__ == '__main__':
    # Unit test
    test_SunOSNetworkCollector()

# Generated at 2022-06-13 01:53:20.977103
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    SunOSNetworkCollector()

# Generated at 2022-06-13 01:53:24.722719
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    facts = SunOSNetworkCollector()
    assert isinstance(facts, NetworkCollector)
    assert isinstance(facts, SunOSNetworkCollector)
    assert facts.platform == 'SunOS'
    assert facts.fact_class == SunOSNetwork

# Generated at 2022-06-13 01:53:35.036668
# Unit test for method parse_interface_line of class SunOSNetwork
def test_SunOSNetwork_parse_interface_line():
    current_if = {'device': 'non-existent', 'ipv4': [], 'ipv6': [], 'type': 'unknown'}
    interfaces = {}
    current_if = SunOSNetwork.parse_interface_line(None, ['e1000g0', 'Index:0:UP:IPV6'], current_if, interfaces)
    assert current_if['ipv4'] == []
    assert current_if['ipv6'] == [{'flags': ['UP', 'IPV6'], 'mtu': 'Index:0'}]
    assert current_if['device'] == 'e1000g0'
    assert interfaces['e1000g0'] == current_if

# Generated at 2022-06-13 01:53:38.482387
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    sunos_network_collector = SunOSNetworkCollector()
    assert sunos_network_collector._fact_class == SunOSNetwork
    assert sunos_network_collector._platform == 'SunOS'

# Generated at 2022-06-13 01:53:49.140127
# Unit test for method parse_interface_line of class SunOSNetwork
def test_SunOSNetwork_parse_interface_line():
    module = MockModule()
    sunos_network = SunOSNetwork(module)
    current_if = {}
    interfaces = {}

    words = ['e1000g0', 'flags=201000843', 'mtu', '1500', 'index', '6']
    current_if = sunos_network.parse_interface_line(words, current_if, interfaces)
    assert current_if['device'] == 'e1000g0'
    assert current_if['flags'] == ['2', '1000843']
    assert current_if['mtu'] == '1500'

    words = ['e1000g0:1', 'flags=201000843', 'mtu', '1500', 'index', '6']
    current_if = sunos_network.parse_interface_line(words, current_if, interfaces)
    assert current_if

# Generated at 2022-06-13 01:54:33.151800
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    assert SunOSNetworkCollector._platform == 'SunOS'
    assert SunOSNetworkCollector._fact_class == SunOSNetwork

# Generated at 2022-06-13 01:54:37.193364
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    """
    This will test the constructor of SunOSNetworkCollector
    """

    sunos_collector = SunOSNetworkCollector()
    assert sunos_collector != None, "The test failed because SunOSNetworkCollector failed to instantiate."


# Generated at 2022-06-13 01:54:48.353855
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    net = SunOSNetwork()
    net.module = FakeAnsibleModule()
    net._interfaces_info = net.get_interfaces_info('/sbin/ifconfig')
    assert len(net._interfaces_info) > 0, "no interfaces found"
    for i in net._interfaces_info:
        if not i.startswith('lo'):
            assert 'ipv4' in net._interfaces_info[i], 'ipv4 not found: %s' % i
            assert 'ipv6' in net._interfaces_info[i], 'ipv6 not found: %s' % i

# Generated at 2022-06-13 01:54:54.139249
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    module = NetworkCollector._create_module(platform='SunOS')
    network_collector = SunOSNetworkCollector(module)
    assert network_collector._platform == 'SunOS'
    assert network_collector._fact_class == SunOSNetwork

if __name__ == '__main__':
    test_SunOSNetworkCollector()

# Generated at 2022-06-13 01:54:57.983606
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    module = AnsibleModuleMock()
    collector = SunOSNetworkCollector(module)
    assert collector._platform == 'SunOS'
    assert collector.get_device() == 'en0'


# Generated at 2022-06-13 01:54:59.409422
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    facts = SunOSNetworkCollector()
    result = isinstance(facts, NetworkCollector)
    assert result is True


# Generated at 2022-06-13 01:55:04.746356
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    o = SunOSNetworkCollector()
    assert o.get_interfaces_info({}) == ([],[])
    assert o.platform == 'SunOS'
    assert o._fact_class._platform == 'SunOS'
    assert o._fact_class.platform == 'SunOS'
    assert o._fact_class.get_interfaces_info.__doc__.startswith('Get interfaces')


# Generated at 2022-06-13 01:55:09.479404
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    c = SunOSNetwork({})
    interfaces, ips = c.get_interfaces_info('/usr/sbin/ifconfig')
    assert len(interfaces) == 3
    assert 'lo0' in interfaces
    assert 'lo1' in interfaces
    assert 'lan0' in interfaces
    assert len(ips['all_ipv4_addresses']) == 2
    assert len(ips['all_ipv6_addresses']) == 5

# Generated at 2022-06-13 01:55:13.514613
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    #
    # This can't run as a unit test because it doesn't have access to
    # the module util globals.
    #
    collector = SunOSNetworkCollector()
    assert collector.fact_class == SunOSNetwork
    assert collector.fact_class.platform == 'SunOS'

# Generated at 2022-06-13 01:55:15.467011
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    x = SunOSNetworkCollector()
    assert x._fact_class._platform == 'SunOS'


# Generated at 2022-06-13 01:56:30.158172
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    nm = SunOSNetworkCollector()
    assert nm._platform == 'SunOS'
    assert nm._fact_class == SunOSNetwork

# Generated at 2022-06-13 01:56:38.630208
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    from ansible.module_utils.facts.network.sunos.sunos import SunOSNetwork
    from ansible.module_utils.facts.network import NetworkCollector  # needed for __file__
    from ansible.module_utils.facts.network.generic_bsd import GENERIC_BSD_IFCONFIG_SAMPLE

    ifconfig_path = "ifconfig"
    sunos_network = SunOSNetwork(ifconfig_path)

    interfaces, ips = sunos_network.get_interfaces_info(ifconfig_path)


# Generated at 2022-06-13 01:56:47.035436
# Unit test for method get_interfaces_info of class SunOSNetwork

# Generated at 2022-06-13 01:56:48.841282
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    obj = SunOSNetworkCollector()
    assert obj._fact_class is not None
    assert obj._platform is not None

# Generated at 2022-06-13 01:56:58.549837
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    from unittest import TestCase
    from ..freebsd import TEST_FREEBSD_IFACES
    from ansible.module_utils.facts.network.generic_bsd import TEST_GENERIC_BSD_IFACES_EXTRA_FIELDS

    # Test data from pytest_collector_ansible_module_utils test fixture
    # in: ../../UnitTests/collection/ansible_module_utils/
    # This test data is generated on a FreeBSD server.
    # Solaris 'ifconfig -a' output differs enough that I don't want to try and
    # maintain an ifconfig -a output for a Solaris server, so I used the FreeBSD output.
    # This test data is a hybrid of FreeBSD and Solaris ifconfig -a output.
    # I've used the FreeBSD 'ifconfig -a' output as a template,

# Generated at 2022-06-13 01:57:07.834284
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    from ansible.module_utils.facts.network.sunos import SunOSNetwork
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils import basic
    import os
    import sys

    testfile = os.path.join(os.path.dirname(__file__), 'get_interfaces_info_ipv6.txt')
    ifc_path = 'ifconfig'
    with open(testfile, 'rb') as f:
        ifconfig_output = to_bytes(f.read())

    module = basic.AnsibleModule(argument_spec={})
    module.run_command = lambda cmd, check_rc=None: (0, ifconfig_output, None)
    obj = SunOSNetwork(module)

# Generated at 2022-06-13 01:57:09.700844
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    """
    Tests the constructor of class SunOSNetworkCollector
    """
    SunOSNetworkCollector()

# Generated at 2022-06-13 01:57:17.276846
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    """
    Run this function with:

    python -m ansible.module_utils.facts.network.sunos.SunOSNetwork
    """
    from ansible.module_utils.facts import ansible_facts
    from ansible.module_utils.facts.network.sunos import SunOSNetwork
    import json
    import tempfile
    import ntpath
    import platform
    import sys

    # Build a test 'ifconfig -a' output which has one of everything, and run
    # it through the class.
    if platform.system() != 'SunOS':
        print('Unit test can only be run on a SunOS host')
        sys.exit(1)


# Generated at 2022-06-13 01:57:20.550112
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    test_fact = SunOSNetwork(None)
    ifconfig_path = '/sbin/ifconfig'
    interfaces, ips = test_fact.get_interfaces_info(ifconfig_path)
    assert len(interfaces) == 3
    assert len(ips['all_ipv4_addresses']) == 7
    assert len(ips['all_ipv6_addresses']) == 3



# Generated at 2022-06-13 01:57:28.060080
# Unit test for method get_interfaces_info of class SunOSNetwork