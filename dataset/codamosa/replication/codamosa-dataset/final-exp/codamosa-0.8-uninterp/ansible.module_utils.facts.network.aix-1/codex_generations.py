

# Generated at 2022-06-13 01:16:59.921808
# Unit test for method get_interfaces_info of class AIXNetwork

# Generated at 2022-06-13 01:17:09.905166
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    test_AIXNet = AIXNetwork()
    # the following ifconfig output is a simulated output for this test
    test_AIXNet.get_interfaces_info('ifconfig', ifconfig_options='-a')
    assert test_AIXNet.interfaces['lo0']['ipv4'] == [{'address': '127.0.0.1', 'broadcast': '127.0.255.255'}]
    assert test_AIXNet.interfaces['lo0']['ipv6'] == [{'address': '::1', 'prefix': '128'}]
    assert test_AIXNet.interfaces['en0']['ipv4'] == []
    assert test_AIXNet.interfaces['en0']['ipv6'] == []
    assert test_AIXNet.interfaces

# Generated at 2022-06-13 01:17:18.965951
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    test_object = AIXNetwork()
    real_results = test_object.get_default_interfaces('/etc/ansible')
    expected_results = {'gateway': '10.1.1.1', 'interface': 'en0'}, {'gateway': 'fe80::38d0:fe6b:b7a9:6ce1%en0', 'interface': 'en0'}
    assert real_results == expected_results

# Generated at 2022-06-13 01:17:26.477578
# Unit test for method get_interfaces_info of class AIXNetwork

# Generated at 2022-06-13 01:17:32.235311
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    """
    This function tests the constructor of class AIXNetworkCollector.
    It uses constructor of class AIXNetworkCollector to create an object of class AIXNetworkCollector.
    Then it checks if the object created is true or false.
    """
    aix_net = AIXNetworkCollector()
    assert isinstance(aix_net, AIXNetworkCollector)

# Generated at 2022-06-13 01:17:35.711258
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    module = AnsibleModule(argument_spec={})
    current = AIXNetwork()
    result = current.get_default_interfaces(module)
    module.exit_json(ansible_facts={'ansible_net_default_interface': result})



# Generated at 2022-06-13 01:17:43.536245
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():

    class TestAIXNetwork(AIXNetwork):

        def run_module(self):

            interfaces, ips = self.get_interfaces_info(ifconfig_path='/sbin/ifconfig')

            assert interfaces['lo0']['description'] == 'Loopback, Type:Software'
            assert interfaces['lo0']['macaddress'] == '00:00:00:00:00:00'
            assert interfaces['lo0']['ifa_index'] == '1'
            assert interfaces['lo0']['ipv4'][0]['address'] == '127.0.0.1'
            assert interfaces['lo0']['ipv4'][0]['netmask'] == '255.0.0.0'

# Generated at 2022-06-13 01:17:48.827066
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    import os

    my_class = AIXNetwork()
    if os.path.exists('/usr/sbin/ifconfig'):
        my_class.get_interfaces_info('/usr/sbin/ifconfig')



# Generated at 2022-06-13 01:17:58.307528
# Unit test for method get_interfaces_info of class AIXNetwork

# Generated at 2022-06-13 01:18:04.224326
# Unit test for method get_interfaces_info of class AIXNetwork

# Generated at 2022-06-13 01:18:23.208432
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    module = AnsibleModule(argument_spec={})
    network_collector = AIXNetworkCollector(module=module)
    assert network_collector.__class__.__name__ == 'AIXNetworkCollector'
    assert network_collector.platform == 'AIX'
    assert network_collector.fact_class.__name__ == 'AIXNetwork'


# Generated at 2022-06-13 01:18:32.879811
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    from ansible_collections.ansible.community.tests.unit.compat import unittest
    from ansible_collections.ansible.community.tests.unit.compat.mock import patch
    from ansible.module_utils.facts.network.base import NetworkCollector
    from ansible.module_utils.facts.network.aix import AIXNetwork
    from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork
    import sys

    # override sys.platform to aix
    sys.platform = 'aix'

    class TestAIXNetworkCollector(unittest.TestCase):

        def setUp(self):
            self.collector = AIXNetworkCollector()


# Generated at 2022-06-13 01:18:42.383938
# Unit test for method get_default_interfaces of class AIXNetwork

# Generated at 2022-06-13 01:18:53.060134
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    module = AnsibleModule(argument_spec=dict())
    mock_run_command = MagicMock(return_value=(0, '''default 172.17.0.1 UG 0 1500 en0
172.17.0.0/16 172.17.0.1 UG 0 1500 en0
172.17.0.1 0:1e:34:e6:8b:57 UH 0 1500 lo0
default 10.128.128.1 UG 0 1500 en1
10.128.128.0/24 10.128.128.1 UG 0 1500 en1
10.128.128.1 1:3e:34:e6:8b:1a UH 0 1500 lo0''', ''))
    with patch.object(AIXNetwork, 'run_command', mock_run_command):
        aix = AIXNetwork

# Generated at 2022-06-13 01:19:04.161286
# Unit test for method get_interfaces_info of class AIXNetwork

# Generated at 2022-06-13 01:19:12.953222
# Unit test for method get_interfaces_info of class AIXNetwork

# Generated at 2022-06-13 01:19:19.843141
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    import unittest
    import sys
    from mock import MagicMock

    class TestNetwork(unittest.TestCase):
        @classmethod
        def setUpClass(cls):
            cls.aix_net = AIXNetworkCollector(MagicMock(), MagicMock())
            cls.aix_net.get_interfaces_info = MagicMock()

# Generated at 2022-06-13 01:19:25.455560
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():

    class MockModule():
        def get_bin_path(self, path):
            return path

        def run_command(self, command):
            if command[0] == 'netstat':
                return (0, '''Kernel IP routing table
Destination Gateway     Flags Refs Use If Exp    TStype     addressable locked
default   192.168.1.1   UG        0 0   0        ether      yes         no
default   ::ffff:192.1 UGc        0 0   0        ipv6       yes         no
''', '')
            else:
                return (127, '', '')

    class MockAIXNetwork():
        def __init__(self, module):
            self.module = module

    mod=MockModule()
    aixnet=MockAIXNetwork(mod)


# Generated at 2022-06-13 01:19:35.234762
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True)
    net = AIXNetwork(module)

    command = module.get_bin_path('netstat')
    if command is None:
        return dict(msg='Omitting tests: netstat not found')

    net.route6_path = command
    net.route_path = command
    net.ifconfig_path = command

    # Define the output for command netstat -nr
    # 1st line: default gateway for IPv4
    # 2nd line: default gateway for IPv6
    # 3rd line: default gateway for IPv6 with different interface name

# Generated at 2022-06-13 01:19:42.024947
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    """
    Unit test for method get_interfaces_info of class AIXNetwork
    """

    # Setup a dummy module for testing
    class DummyModule(object):
        def __init__(self):
            self._module = self
            self._debug = False
            self._verbosity = 0
            self.params = {}
            self.exit_json = None
            self.fail_json = None

        def run_command(self, cmd_args):
            # return 0 to avoid skipping stats
            return 0, '', ''

        def get_bin_path(self, cmd_name):
            return None

    def create_out(out_list):
        dummy_out = ''
        interface_lines = dict()
        link_lines = dict()
        addr_lines = dict()

        # hostname fake

# Generated at 2022-06-13 01:20:09.353725
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    module = AnsibleModule({})

    # Create the instance of AIXNetwork and test the get_interfaces_info method
    aix_network = AIXNetwork({}, module)
    interfaces, ips = aix_network.get_interfaces_info(aix_network.module.get_bin_path('ifconfig'))
    pprint.pprint(interfaces)
    pprint.pprint(ips)

# Generated at 2022-06-13 01:20:11.546090
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    '''Test constructor of class AIXNetworkCollector
    '''
    aix_net_collector_ins = AIXNetworkCollector()
    assert aix_net_collector_ins

# Generated at 2022-06-13 01:20:20.027960
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    out = '''default 192.168.0.1 UG 1 622 en1
default 192.0.2.2 UGDR
default fe80::xxx:xxx:xxx:xxx%en1 UG 1 622 en1
default dead:beef:: UGDR
'''

    sn = AIXNetwork()
    (interface_v4, interface_v6) = sn.get_default_interfaces('route')

    assert interface_v4['gateway'] == '192.168.0.1'
    assert interface_v4['interface'] == 'en1'
    assert interface_v6['gateway'] == 'dead:beef::'
    assert interface_v6['interface'] == None

# Generated at 2022-06-13 01:20:20.940408
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    AIXNetworkCollector()


# Generated at 2022-06-13 01:20:32.463305
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    class AIXNetwork_test():
        module = None
        platform = 'AIX'

    # when no route is defined
    AIXNetwork_test.module = class_mock('AIXNetwork_test.module',
                                        **{'run_command.return_value': (None, None, None)})
    aix_if = AIXNetwork_test()
    (v4_dict, v6_dict) = aix_if.get_default_interfaces('')
    assert v4_dict == {}
    assert v6_dict == {}

    # when a route is defined

# Generated at 2022-06-13 01:20:39.291059
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    net = AIXNetwork({'route': '/usr/bin/netstat'})
    default_v4, default_v6 = net.get_default_interfaces('/usr/bin/netstat')
    assert default_v4 == {'gateway': '192.168.0.1', 'interface': 'en0'}
    assert default_v6 == {'gateway': 'fe80::5054:ff:fe00:0%lo0', 'interface': 'lo0'}

# Generated at 2022-06-13 01:20:42.353961
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    module = type('AnsibleModule', (object,), {'run_command': run_command})()
    net = AIXNetwork(module)

    net.get_default_interfaces('/etc/path_to_routes')


# Generated at 2022-06-13 01:20:44.873948
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    assert issubclass(AIXNetworkCollector, NetworkCollector)
    c = AIXNetworkCollector()
    assert c._fact_class == AIXNetwork
    assert c._platform == 'AIX'

# Generated at 2022-06-13 01:20:48.702493
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    module = AnsibleModule(argument_spec={})
    network_collector = AIXNetworkCollector(module)
    network_module = network_collector._fact_class('/bin/ifconfig', module)
    if 'netstat' in module.get_bin_path('netstat'):
        v4, v6 = network_module.get_default_interfaces('/bin/netstat')
        assert v4.keys() or v6.keys()

# Generated at 2022-06-13 01:20:55.708362
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts.network.aix import AIXNetwork
    module = MagicMock()
    module.run_command = Mock(return_value=(0, to_bytes(''), to_bytes('')))
    module.get_bin_path = Mock(return_value='/usr/bin')
    net = AIXNetwork(module)
    net.get_default_interfaces('/usr/bin/netstat')

# Generated at 2022-06-13 01:21:47.273413
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    """
    Test function
    """


# Generated at 2022-06-13 01:21:54.757520
# Unit test for method get_interfaces_info of class AIXNetwork

# Generated at 2022-06-13 01:22:06.317271
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    # Mock module argument spec
    mock_module = type('AnsibleModule', (object,), dict(argument_spec={}))()

    # Mock facts module
    mock_facts = type('Facts', (object,), dict(module=mock_module))()

    # Mock module
    mock_module.run_command = MagicMock(return_value=(0, "default 0.0.0.0 UG 0 0 0 en0", ""))

    # Get class
    aix_network = AIXNetwork()

    # Test
    result = aix_network.get_default_interfaces(mock_facts)
    assert result == ({'interface': 'en0', 'gateway': '0.0.0.0'}, {})

    # Test empty result

# Generated at 2022-06-13 01:22:13.163402
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork
    from ansible.module_utils.facts.network.aix import AIXNetwork
    import os

    # set up fake module with dummy arguments
    class FakeModule(object):
        def __init__(self, ifconfig_path):
            self.params = {}
            self.params['path'] = {'ifconfig': ifconfig_path}

        def get_bin_path(self, binary_name):
            return self.params['path'].get(binary_name, None)

        def run_command(self, cmd):
            return 0, cmd[0], []

    class_ifconfig = GenericBsdIfconfigNetwork(FakeModule('/sbin/ifconfig'))

    # test empty route output

# Generated at 2022-06-13 01:22:13.967928
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    assert issubclass(AIXNetworkCollector, NetworkCollector)


# Generated at 2022-06-13 01:22:18.833862
# Unit test for method get_interfaces_info of class AIXNetwork

# Generated at 2022-06-13 01:22:21.137370
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    """
    This function returns the AIXNetworkCollector object for
    platform "AIX"
    """
    return AIXNetworkCollector()

# Generated at 2022-06-13 01:22:22.887492
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    m = AIXNetworkCollector()
    print(m)


# Generated at 2022-06-13 01:22:26.012275
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    assert AIXNetwork().get_default_interfaces('/usr/sbin/route') == ({}, {}), \
        "AIXNetwork().get_default_interfaces('/usr/sbin/route') failed"

# Generated at 2022-06-13 01:22:34.577633
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():

    def get_mock_module(command_string, output):
        def mock_module_run_command(self, command, check_rc=True):
            if command == command_string:
                return 0, output, ''
        class MockModule(object):
            run_command = mock_module_run_command
            get_bin_path = lambda self, name: '/sbin/%s' % name
        return MockModule()

    test_interface_name = 'eth0'
    test_mac_address = '00:11:22:33:44:55'
    test_ipv4_address = '192.168.1.1'
    test_ipv6_address = 'dead::beef'
    test_ipv6_addr_global = 'dead:beef::1'


# Generated at 2022-06-13 01:24:07.072285
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    network_collector = AIXNetworkCollector()
    assert(network_collector._platform == 'AIX')
    assert(network_collector._fact_class == AIXNetwork)


# Generated at 2022-06-13 01:24:12.516423
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    module = object()

# Generated at 2022-06-13 01:24:22.451290
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    testnetif = AIXNetwork()
    testnetif._module = MagicMock()
    testnetif._module.run_command = MagicMock(return_value=(0, 'default 192.168.1.1 UG 0 0 en0\n'
                                                      'default 192.168.1.0 U 0 0 en0\n'
                                                      'default 2002:c0a8:1:0::0:1 UGHL 0 0 en0\n'
                                                      'default 2002:c0a8:1::0:0:1 UGHWISC 0 0 en0\n', ''))
    testnetif._module.get_bin_path = MagicMock(return_value='/sbin/netstat')


# Generated at 2022-06-13 01:24:23.308101
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    network = AIXNetworkCollector()


# Generated at 2022-06-13 01:24:32.176231
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    """
    Test method AIXNetwork.get_interfaces_info using the following scenario:
        - one system having an ipv4 and ipv6 link-local address on 'en1', an
          ipv4 address on 'en2', and a ipv4 alias address on 'en2:1'
    """
    # interface names and ipv4 addresses are used as keys in the returned interface
    # dictionaries, so make sure these terms are defined for the test case
    key_intf_device = 'device'
    key_intf_ipv4_addr = 'ipv4_address'
    key_intf_ipv6_addr = 'ipv6_address'
    key_addrs_ipv4_all = 'all_ipv4_addresses'

# Generated at 2022-06-13 01:24:41.413006
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    """Unit test for method get_default_interfaces of class AIXNetwork"""

    class MockModule:

        def run_command(self, command):
            """Mock function"""

            routes = dict(
                default=[
                    'default               172.17.0.1      UG        0        0 en0',
                    'default               fe80::a00:27ff:feb0:c39d%en0 UGc       0        0 en0',
                ],
            )

            # route = dict(
            #     v4={
            #         'gateway': '172.17.0.1',
            #         'interface': 'en0',
            #     },
            #     v6={
            #         'gateway': 'fe80::a00:27ff:feb0:c39d%en0',
           

# Generated at 2022-06-13 01:24:48.811259
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():

    # These are the inputs to the method
    route_path = "not_empty"

    return_values = []

    # Following are the return values from the above method
    gw1, gw2 = "192.168.1.1", "2001:DB8::1"
    iface1, iface2 = "en0", "en1"
    # following are the results of the test
    netstat_path = class_under_test_path = "/bin/netstat"
    uname_path = "/usr/bin/uname"
    uname_out = "0 "
    rc = [0, 0, 0, 0, 0, 0, 1]

# Generated at 2022-06-13 01:24:55.087117
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    AIXNetwork = AIXNetwork()

    # This is a list of lines of the 'ifconfig -a' output on AIX.
    # The output was adapted to these lines, since the real output would be too big
    # The output was generated on AIX 7.1 TL3 SP6
    # 'en0' is the only one interface with a MAC address

# Generated at 2022-06-13 01:25:03.339082
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():

    def get_AIXNetwork():
        return AIXNetwork({'path': {'uname': '/usr/bin/uname'}})

    # Sample input and expected output

# Generated at 2022-06-13 01:25:05.821465
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    result = AIXNetworkCollector()
    assert result.platform == 'AIX'
    assert result.fact_class.platform == 'AIX'
    assert isinstance(result.fact_class, GenericBsdIfconfigNetwork)
