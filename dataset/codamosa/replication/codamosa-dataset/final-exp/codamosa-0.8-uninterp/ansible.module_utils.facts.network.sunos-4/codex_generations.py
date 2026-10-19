

# Generated at 2022-06-13 01:48:28.214570
# Unit test for method parse_interface_line of class SunOSNetwork
def test_SunOSNetwork_parse_interface_line():
    # create a mock module
    import ansible.module_utils.facts.network.sunos as sunos
    sunos.AnsibleModule = DummyAnsibleModule()
    # create a mock config file for ifconfig command
    import tempfile
    tmpfile = tempfile.NamedTemporaryFile(mode='w', delete=False)
    ifconfig_file = tmpfile.name
    tmpfile.write("lo0: flags=2001000849<UP,LOOPBACK,RUNNING,MULTICAST,IPv4,VIRTUAL> mtu 8232 index 1\n")
    tmpfile.write("    inet 127.0.0.1 netmask ff000000\n")
    tmpfile.write("    inet6 ::1/128\n")

# Generated at 2022-06-13 01:48:30.808051
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    assert issubclass(SunOSNetworkCollector, NetworkCollector)
    assert SunOSNetworkCollector._platform == 'SunOS'
    assert SunOSNetworkCollector._fact_class == SunOSNetwork

# Generated at 2022-06-13 01:48:33.070202
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    mod = SunOSNetworkCollector()
    assert mod._fact_class._platform is 'SunOS'
    assert mod._fact_class.platform is 'SunOS'


# Generated at 2022-06-13 01:48:34.814419
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    assert SunOSNetworkCollector.platform == 'SunOS'
    assert SunOSNetworkCollector._fact_class is SunOSNetwork


# Generated at 2022-06-13 01:48:37.607564
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    """Unit test for constructor of class SunOSNetworkCollector"""
    SunOSNetworkCollector()

# Generated at 2022-06-13 01:48:40.164534
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    network_collector_object = SunOSNetworkCollector()
    assert network_collector_object.__class__.__name__ == "SunOSNetworkCollector"

# Generated at 2022-06-13 01:48:41.181910
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    SunOSNetworkCollector()

# Generated at 2022-06-13 01:48:44.747549
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    collected_facts = SunOSNetworkCollector.collect()
    contained_fact = 'ansible_net_interfaces'
    assert contained_fact in collected_facts

# Generated at 2022-06-13 01:48:47.890703
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    network_collector = SunOSNetworkCollector(None)
    network_collector.module = None
    network_collector.get_interfaces_info(None)

# Generated at 2022-06-13 01:48:51.981011
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    """Test SunOSNetworkCollector"""

    testobj = SunOSNetworkCollector(None, None, None, None, None)
    assert testobj._fact_class is SunOSNetwork
    assert testobj._platform == "SunOS"
    assert isinstance(testobj._fact_class, NetworkCollector) is True


# Generated at 2022-06-13 01:49:08.443802
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    in_interfaces, in_ips = sunos_network.get_interfaces_info('/sbin/ifconfig')
    assert 'lo0' in in_interfaces
    assert 'net0' in in_interfaces
    assert 'ipv4' in in_interfaces['lo0']
    assert 'ipv6' in in_interfaces['lo0']
    assert 'ipv4' in in_interfaces['net0']
    assert 'ipv6' in in_interfaces['net0']
    assert 'mtu' in in_interfaces['lo0']['ipv4'][0]
    assert 'flags' in in_interfaces['lo0']['ipv4'][0]
    assert 'mtu' in in_interfaces['lo0']['ipv6'][0]

# Generated at 2022-06-13 01:49:18.932762
# Unit test for method parse_interface_line of class SunOSNetwork
def test_SunOSNetwork_parse_interface_line():
    module = MagicMock()
    facts = SunOSNetwork(module)
    interfaces = {}
    current_if = {}
    new_current_if = facts.parse_interface_line(["lo0:", "flags=", "UP,", "LOOPBACK,", "RUNNING,", "MULTICAST,"],
                                                current_if, interfaces)
    interfaces['lo0'] = new_current_if
    current_if = new_current_if
    new_current_if = facts.parse_interface_line(["lo0:", "IPv6,", "flags=", "UP,", "LOOPBACK,", "RUNNING,", "MULTICAST,"],
                                                current_if, interfaces)

# Generated at 2022-06-13 01:49:25.822615
# Unit test for method get_interfaces_info of class SunOSNetwork

# Generated at 2022-06-13 01:49:30.209127
# Unit test for method get_interfaces_info of class SunOSNetwork

# Generated at 2022-06-13 01:49:31.183591
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    SunOSNetworkCollector()

# Generated at 2022-06-13 01:49:39.092959
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    module = type('', (), {})()
    network_module = SunOSNetwork(module)
    ifconfig_path = '/usr/sbin/ifconfig'

# Generated at 2022-06-13 01:49:48.764078
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    iface = SunOSNetwork()
    ifaces, ips = iface.get_interfaces_info("dummy_path")

    assert len(ifaces) == 4
    assert 'lo0' in ifaces
    assert 'ce0' in ifaces
    assert 'lo0' in ifaces
    assert 'lo0' in ifaces

    assert ifaces['lo0']['type'] == 'loopback'
    assert ifaces['lo0']['ipv4'][0]['mtu'] == '16436'
    assert ifaces['lo0']['ipv4'][0]['flags'] == ['UP', 'RUNNING', 'MULTICAST', 'IPv4']
    assert ifaces['lo0']['ipv6'][0]['mtu'] == '16384'
    assert ifaces

# Generated at 2022-06-13 01:49:50.627011
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    # Instantiate SunOSNetworkCollector
    device_network_information = SunOSNetworkCollector(module=None, commands={})
    assert isinstance(device_network_information, SunOSNetworkCollector)


# Generated at 2022-06-13 01:49:55.504384
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    """
    This is the unit test for method 'get_interfaces_info' of class SunOSNetwork
    Expectations were getting from running command 'ifconfig -a' on a Solaris 11.3 system.
    """

# Generated at 2022-06-13 01:50:05.995018
# Unit test for method parse_interface_line of class SunOSNetwork
def test_SunOSNetwork_parse_interface_line():
    # Create an instance of the sunos network module
    module = AnsibleModule(argument_spec=dict())
    network = SunOSNetwork(module)

    # Current network interface under test
    current_if = {}

    # Known network interfaces
    interfaces = {}

    # Define interfaces to be tested
    interfaces['lo0'] = {}
    interfaces['lo0']['ipv4'] = []
    interfaces['lo0']['ipv6'] = []
    interfaces['lo0']['type'] = 'unknown'

    # Define lines to be tested
    line1 = 'lo0: flags=1000849<UP,LOOPBACK,RUNNING,MULTICAST,IPv4> mtu 8232 index 1'   # IPv4

# Generated at 2022-06-13 01:50:22.459328
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    from ansible.module_utils.facts.network.generic_bsd import \
        GenericBsdIfconfigNetwork

    result = GenericBsdIfconfigNetwork.test_get_interfaces_info()

    assert result.get('lo0') is not None
    assert result.get('net0') is not None


if __name__ == '__main__':

    import doctest
    doctest.testmod()

# Generated at 2022-06-13 01:50:33.441644
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():

    ifconfig_path = '/sbin/ifconfig'

    ###########################################################################
    # Test a typical 'ifconfig -a' output on Solaris 10.
    ###########################################################################


# Generated at 2022-06-13 01:50:34.940774
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    assert SunOSNetworkCollector is not None

# Generated at 2022-06-13 01:50:37.721599
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    '''
    SunOSNetwork.get_interfaces_info unit test.

    TODO: Write unit test for SunOSNetwork.get_interfaces_info.
    '''
    pass

# Generated at 2022-06-13 01:50:49.074437
# Unit test for method get_interfaces_info of class SunOSNetwork

# Generated at 2022-06-13 01:50:51.246449
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    obj = SunOSNetworkCollector()
    assert obj._fact_class.platform == 'SunOS'

# Generated at 2022-06-13 01:51:00.901388
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    """
    Unit test method get_interfaces_info of class SunOSNetwork
    """
    # Check if the platform is SunOS. This test should only run on a SunOS platform.
    assert SunOSNetwork.platform == "SunOS"

    # Create a SunOSNetwork object (SunOSNetwork is an extension of GenericBsdIfconfigNetwork).
    sunos_network = SunOSNetwork()

    # Define a sample output from the command 'ifconfig -a' on a Solaris 10 platform.

# Generated at 2022-06-13 01:51:13.066420
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    v1 = re.compile(r'(^\s*[0-9]*\s[a-zA-Z0-9_]*)(.*)')
    v2 = re.compile(r'(^\s*[a-zA-Z0-9]+)(.*)')

    device = ''
    interfaces = {}
    ips = dict(
        all_ipv4_addresses=[],
        all_ipv6_addresses=[],
    )


# Generated at 2022-06-13 01:51:24.826276
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    """
    Run simple tests for SunOSNetwork class methods
    """

    from tempfile import NamedTemporaryFile

    # when looking for 'options=', 'nd6', 'ether', ..., 'inet6' below,
    # we only want the one line and not the first match that happens to be
    # in the comment at the top of the file.


# Generated at 2022-06-13 01:51:31.419126
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    test_run = SunOSNetwork({})
    ifconfig_path = '/sbin/ifconfig'

# Generated at 2022-06-13 01:51:58.773775
# Unit test for method get_interfaces_info of class SunOSNetwork

# Generated at 2022-06-13 01:52:07.439621
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    fake_module = type('obj', (object,), {
        'run_command': lambda *args, **kwargs: (0, '', '')
    })

    n = SunOSNetwork(fake_module)
    interfaces, ips = n.get_interfaces_info('/sbin/ifconfig')

# Generated at 2022-06-13 01:52:17.127884
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    """
    This test uses a static 'ifconfig -a' output from a Solaris server
    to test the get_interfaces_info method of the SunOSNetwork class.
    """
    test_module = AnsibleModule(argument_spec={}, supports_check_mode=True)
    test_iface_file = os.path.join(os.path.dirname(__file__), 'SunOS', 'ifconfig.out')
    ifaces, ips = SunOSNetwork(test_module).get_interfaces_info(test_iface_file)
    for iface in ifaces:
        print("{}: {}".format(iface, ifaces[iface]))
    print("")
    print("ips: {}".format(ips))


# Generated at 2022-06-13 01:52:19.347447
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    collect = SunOSNetworkCollector()
    assert collect.platform == 'SunOS'
    assert collect.fact_class.platform == 'SunOS'

# Generated at 2022-06-13 01:52:28.624074
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():

    # Set up mock module
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True)

    module.run_command = MagicMock(return_value=(0, '', ''))

    # Set up parser object and populate it with output from "ifconfig -a"
    parser = SunOSNetwork()
    parser.module = module
    with open('tests/utils/fixtures/facts/network/sunos/ifconfig.txt') as f:
        ifconfig_output = f.read()
    module.run_command.return_value = (0, ifconfig_output, '')
    (interfaces, ipv4_addresses, ipv6_addresses) = parser.get_interfaces_info('/sbin/ifconfig')

    # assert the number of interfaces is correct
    assert len

# Generated at 2022-06-13 01:52:30.684145
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    assert SunOSNetworkCollector() is not None


# Generated at 2022-06-13 01:52:32.974552
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    assert SunOSNetworkCollector._platform == 'SunOS'
    assert SunOSNetworkCollector._fact_class == SunOSNetwork


# Generated at 2022-06-13 01:52:41.053209
# Unit test for method get_interfaces_info of class SunOSNetwork

# Generated at 2022-06-13 01:52:42.378971
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    obj = SunOSNetworkCollector()
    assert isinstance(obj, SunOSNetworkCollector)
    assert isinstance(obj._fact_class, SunOSNetwork)
    assert obj._platform == 'SunOS'

# Generated at 2022-06-13 01:52:43.411682
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    SunOSNetworkCollector()

# Generated at 2022-06-13 01:53:20.642601
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    assert SunOSNetworkCollector._platform == "SunOS"
    assert SunOSNetworkCollector._fact_class == SunOSNetwork

# Constructor for class SunOSNetwork

# Generated at 2022-06-13 01:53:23.213926
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    assert SunOSNetworkCollector._platform == 'SunOS'
    assert SunOSNetworkCollector._fact_class == SunOSNetwork

# Generated at 2022-06-13 01:53:33.841077
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    """
    Test get_interfaces_info of class SunOSNetwork
    """

    # Sample ifconfig -a output.

# Generated at 2022-06-13 01:53:40.655117
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    ''' Unit test for method get_interfaces_info of class SunOSNetwork '''
    from ansible_collections.notstdlib.moveitallout.plugins.module_utils.facts.network.sunos.sunos_network import SunOSNetwork
    from ansible.module_utils import basic
    network_collector = SunOSNetwork()
    network_collector.get_interfaces_info('test_ifconfig')



# Generated at 2022-06-13 01:53:48.695851
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    test_class = SunOSNetwork()
    # Unfortunately there seems to be no way to test
    # get_interfaces_info() method as it calls
    # module.run_command which we cannot stub
    # (run_command method is called in module.__init__()).
    # Can run test separately with
    # ansible -m setup -a 'gather_subset=!all' $(uname -n)
    # and check the output in ansible_local
    # and ansible_local.interfaces
    assert test_class.get_interfaces_info("/sbin/ifconfig")[0]['lo0']['ipv4']

# Generated at 2022-06-13 01:53:57.506461
# Unit test for method get_interfaces_info of class SunOSNetwork

# Generated at 2022-06-13 01:54:03.600576
# Unit test for method get_interfaces_info of class SunOSNetwork

# Generated at 2022-06-13 01:54:08.589837
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    obj = SunOSNetworkCollector()
    assert obj.platform == 'SunOS'
    assert obj._fact_class == SunOSNetwork
    assert obj.interface_list == []
    assert obj.interfaces == {}
    assert obj.all_ipv4_addresses == []
    assert obj.all_ipv6_addresses == []


# Generated at 2022-06-13 01:54:09.340382
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    assert SunOSNetworkCollector._platform == 'SunOS'

# Generated at 2022-06-13 01:54:10.981322
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    c = SunOSNetworkCollector()
    assert c.platform == "SunOS"


# Generated at 2022-06-13 01:55:32.624516
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    c = SunOSNetworkCollector(None, None, None)
    assert isinstance(c._fact_class(), SunOSNetwork)
    assert c._platform == 'SunOS'

# Generated at 2022-06-13 01:55:34.393407
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    NetworkCollector.collect(SunOSNetworkCollector, 'test_SunOSNetworkCollector', {})



# Generated at 2022-06-13 01:55:38.431744
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    """
    Test SunOSNetworkCollector.
    """

    def get_bin_path(mod, mod_name, bin_name):
        """
        Test get_bin_path().
        """

        return 'bin'

    # Mock module
    class MockModule:
        """
        MockModule
        """

        def __init__(self, params):
            """
            MockModule
            """

            self.params = params

        def run_command(self, args):
            """
            Mock run_command.
            """


# Generated at 2022-06-13 01:55:47.077628
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():

    # Set up class instance to be tested.
    network_collector = SunOSNetwork('module', 'path')
    network_collector.module.run_command = lambda *args: ('', '', '')

    # Test with a default interface name.
    ansible_facts = dict()
    ansible_facts['ansible_' + network_collector.prefix] = dict()
    ansible_facts['ansible_' + network_collector.prefix]['interfaces'] = dict()
    ansible_facts['ansible_' + network_collector.prefix]['interfaces']['lo0'] = dict()
    ansible_facts['ansible_' + network_collector.prefix]['interfaces']['lo0']['device'] = 'lo0'

# Generated at 2022-06-13 01:55:51.984639
# Unit test for method get_interfaces_info of class SunOSNetwork

# Generated at 2022-06-13 01:55:59.479535
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    module_dict = dict(
        ansible_facts=dict(
            ansible_interfaces=[],
            ansible_all_ipv4_addresses=[],
            ansible_all_ipv6_addresses=[]))
    module_dict['ansible_facts']['ansible_system'] = 'SunOS'

    # Test for 'ifconfig -a' output with IPv4 and IPv6 addresses on a single interface.
    # Test for output from 'ifconfig -a' with IPv6 LL address, global scope address and no scope address.
    module_dict['ansible_facts']['ansible_network_resources'] = {'interfaces': {}, 'ips': {}}

# Generated at 2022-06-13 01:56:01.864328
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    _fact_class = SunOSNetwork
    _platform = 'SunOS'
    sunos_nc = SunOSNetworkCollector(_fact_class, _platform)

    assert(sunos_nc.fact_class == sunos_nc._fact_class)
    assert(sunos_nc.platform == sunos_nc._platform)

# Generated at 2022-06-13 01:56:08.202966
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    from ansible.module_utils.facts.network.generic_bsd import GenericBsdNetwork
    from ansible.module_utils.facts.network.generic_bsd import NetworkParams
    from ansible.module_utils.facts.network.generic_bsd import NetworkConfig
    from ansible.module_utils.facts.network.generic_bsd import Options

    # Only one octet of MAC address is used.

# Generated at 2022-06-13 01:56:11.449162
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    assert SunOSNetworkCollector._platform == 'SunOS'
    assert SunOSNetworkCollector._fact_class == SunOSNetwork


# Generated at 2022-06-13 01:56:23.341897
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    from ansible.module_utils.facts.network.sunos import SunOSNetwork
    from ansible.module_utils.facts.network.tests.test_ifconfig import content_ifconfig_a as content_ifconfig_a_SunOS

    sunos_network = SunOSNetwork({})

    interfaces, ips = sunos_network.get_interfaces_info('/sbin/ifconfig')
