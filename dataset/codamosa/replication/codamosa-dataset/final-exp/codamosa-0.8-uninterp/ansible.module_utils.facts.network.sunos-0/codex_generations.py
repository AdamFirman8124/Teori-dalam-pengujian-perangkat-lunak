

# Generated at 2022-06-13 01:48:20.281675
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    assert SunOSNetworkCollector()._fact_class == SunOSNetwork

# Generated at 2022-06-13 01:48:21.828624
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    collector = SunOSNetworkCollector()
    assert collector._fact_class is SunOSNetwork
    assert collector._platform == 'SunOS'

# Generated at 2022-06-13 01:48:23.124487
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    SunOSNetworkCollector()

# Generated at 2022-06-13 01:48:28.885201
# Unit test for method get_interfaces_info of class SunOSNetwork

# Generated at 2022-06-13 01:48:39.015520
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    from ansible.module_utils.facts.network.sunos import Interfaces
    interfaces = Interfaces()
    assert len(interfaces) == 2
    assert 'bge0:1' in interfaces
    assert 'lo0' in interfaces

    # Common
    assert interfaces.get('bge0:1').get('device') == 'bge0:1'
    assert interfaces.get('bge0:1').get('active') == False
    assert interfaces.get('bge0:1').get('type') == 'ether'
    assert interfaces.get('bge0:1').get('macaddress') == '00:14:4f:15:91:fa'

# Generated at 2022-06-13 01:48:47.588484
# Unit test for method parse_interface_line of class SunOSNetwork
def test_SunOSNetwork_parse_interface_line():
    current_if = {}
    interfaces = {}
    words = ['lo0:', 'flags=2001000849<UP,LOOPBACK,RUNNING,MULTICAST,IPv4,VIRTUAL>', 'mtu', '8232']
    current_if = SunOSNetwork().parse_interface_line(words, current_if, interfaces)
    assert 'device' in current_if
    assert current_if['device'] == 'lo0'
    assert 'ipv4' in current_if
    assert 'ipv6' in current_if
    assert 'type' in current_if
    assert len(current_if['ipv4']) == 1
    ipv4_dict = current_if['ipv4'][0]
    assert 'flags' in ipv4_dict

# Generated at 2022-06-13 01:48:57.105812
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    module = AnsibleModule(argument_spec={})
    ifconfig_path = get_file_content('get_interfaces_info', 'SunOS', 'ifconfig')
    fact = SunOSNetwork(module)
    interfaces, ips = fact.get_interfaces_info(ifconfig_path)
    assert interfaces == get_file_json_content('get_interfaces_info_interfaces', 'SunOS', 'interfaces')
    assert ips == get_file_json_content('get_interfaces_info_ips', 'SunOS', 'ips')

if __name__ == '__main__':
    # Unit test
    argument_spec = dict(
        gather_subset=dict(default=['!all'], type='list'),
        gather_network_resources=dict(type='list'),
    )
    module = Ans

# Generated at 2022-06-13 01:48:58.439621
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    collector = SunOSNetworkCollector()
    assert collector.facts['network']

# Generated at 2022-06-13 01:49:09.569768
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    ifconfig_path = '/sbin/ifconfig'


# Generated at 2022-06-13 01:49:20.159138
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():

    test_sunos_network = SunOSNetwork(dict(module=None), dict(params=dict(gather_subset=['all'])))

    test_sunos_network.module.run_command = lambda cmd: (0, sunos_get_interfaces_info_output_1, '')


# Generated at 2022-06-13 01:49:26.625559
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    module = FakeModule()
    SunOSNetworkCollector(module)
    assert module.SunOS_HAS_NETWORK_FACTS


# Generated at 2022-06-13 01:49:36.009040
# Unit test for method get_interfaces_info of class SunOSNetwork

# Generated at 2022-06-13 01:49:47.135124
# Unit test for method parse_interface_line of class SunOSNetwork
def test_SunOSNetwork_parse_interface_line():

    class Test_SunOSNetwork(object):

        def __init__(self):
            self.ansible_facts = {}
            self.ansible_facts['ansible_interfaces'] = []
            self.ansible_facts['ansible_all_ipv4_addresses'] = []
            self.ansible_facts['ansible_all_ipv6_addresses'] = []
            self.ansible_facts['ansible_local4'] = []
            self.ansible_facts['ansible_local6'] = []

    # Construct test output: interface lines for IPv4 and IPv6 both
    # followed by extra lines with facts to be ignored.
    #
    # The test output is taken from Solaris 10 U7 (x86), ifconfig -a.
    # The IPv6 information is manufactured and may not be accurate.

    test

# Generated at 2022-06-13 01:49:50.189196
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    network_collector = SunOSNetworkCollector()
    assert network_collector._fact_class == SunOSNetwork
    assert network_collector._platform == 'SunOS'

# Generated at 2022-06-13 01:50:02.032415
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    # Create SunOSNetwork object
    sn = SunOSNetwork()

    # Create test data

# Generated at 2022-06-13 01:50:04.144655
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    sc = SunOSNetworkCollector(None)
    assert sc.platform == 'SunOS'
    assert sc.fact_class._platform == 'SunOS'


# Generated at 2022-06-13 01:50:05.682972
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    obj = SunOSNetworkCollector()
    assert obj._fact_class == SunOSNetwork
    assert obj._platform == 'SunOS'

# Generated at 2022-06-13 01:50:16.465673
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():

    # Unit tests require the following imports
    import os.path
    import sys
    import unittest

    class AnsibleModulesTest(unittest.TestCase):

        #def setUp(self):
        #    print('setUp')

        #def tearDown(self):
        #    print('tearDown')

        #def test_name(self):
        #    print('test_name')

        def test_SunOSNetwork(self):

            class Module:
                def __init__(self):
                    self.run_command = self.run_command_fn
                    self.fail_json = self.fail_json_fn

                def fail_json_fn(self, **kwargs):
                    print('AnsibleModule.fail_json:', kwargs)
                    sys.exit(1)


# Generated at 2022-06-13 01:50:26.555132
# Unit test for method parse_interface_line of class SunOSNetwork
def test_SunOSNetwork_parse_interface_line():
    net = SunOSNetwork()
    net.interfaces = {}
    net.ips = {}
    current_if = {}
    words = ['lo0:', 'flags=1000849', 'mtu', '8232']
    current_if = net.parse_interface_line(words, current_if, net.interfaces)
    assert current_if['device'] == 'lo0'
    assert current_if['ipv4'][0]['mtu'] == '8232'
    assert current_if['ipv4'][0]['flags'] == 'LOOPBACK,RUNNING,MULTICAST,IPv4'
    assert current_if['macaddress'] == 'unknown'
    assert current_if['type'] == 'loopback'
    assert current_if['ipv6'] == []

# Generated at 2022-06-13 01:50:38.167520
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    from ansible_collections.community.network.tests.unit.compat.mock import patch, MagicMock
    from ansible_collections.community.network.plugins.module_utils.facts.facts.network.sunos import SunOSNetwork

    mock_module = MagicMock()
    mock_module.run_command = MagicMock(return_value=(0, open('test/unit/ansible_collections/community/network/tests/unit/compat/ifconfig_a_sunos.txt').read(), ''))
    mock_module.params = {'gather_subset': ['!all', '!min']}

    ifcs = SunOSNetwork(mock_module)

    # convert to lists and sort because the order of the interfaces is random
    interfaces_list = list(ifcs.interfaces.items())
    ip

# Generated at 2022-06-13 01:50:54.147574
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    test_module = type('test_module', (object,), dict(
        run_command=lambda x, check_rc=True: (0, '', ''),
        params={},
    ))
    test_intf = test_module()
    test_intf.module = test_module()
    test_intf.module.run_command = lambda x, check_rc=True: (0, '', '')

    ifconfig_path = '/sbin/ifconfig'

# Generated at 2022-06-13 01:51:02.517700
# Unit test for method parse_interface_line of class SunOSNetwork
def test_SunOSNetwork_parse_interface_line():
    from ansible.module_utils.facts.network.sunos import SunOSNetwork
    sunos = SunOSNetwork(None)
    iface = None
    current_if = {'device': 'lo0', 'ipv4': [], 'ipv6': [], 'type': 'unknown'}
    interfaces = {}
    words = ['lo0:', 'flags=10048', 'mtu', '8232', 'index', '8']
    result = sunos.parse_interface_line(words, current_if, interfaces)
    assert current_if['device'] == 'lo0'
    assert current_if['type'] == 'loopback'
    assert current_if['ipv4'][0]['flags'] == '10048'
    assert current_if['ipv4'][0]['mtu'] == '8232'

# Generated at 2022-06-13 01:51:12.883692
# Unit test for method parse_interface_line of class SunOSNetwork
def test_SunOSNetwork_parse_interface_line():
    interfaces = {}
    current_if = {}
    words = ['lo0:', 'flags=2001000849', 'mtu', '8232']
    current_if = SunOSNetwork.parse_interface_line(None, words, current_if, interfaces)
    assert current_if['device'] == 'lo0'
    assert len(current_if['ipv4']) == 1
    assert len(current_if['ipv6']) == 0
    assert current_if['ipv4'][0]['flags'] == 'IPv4 IPv6 LOOPBACK up'
    assert current_if['ipv4'][0]['mtu'] == '8232'

# Generated at 2022-06-13 01:51:14.742043
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    assert SunOSNetworkCollector.platform == 'SunOS'
    assert SunOSNetworkCollector._fact_class == SunOSNetwork

# Generated at 2022-06-13 01:51:26.244074
# Unit test for method parse_interface_line of class SunOSNetwork
def test_SunOSNetwork_parse_interface_line():
    # Create instance of SunOSNetwork
    network = SunOSNetwork()

    # Create a regular interface
    current_if = {}
    interfaces = {}
    words = ['bge0:', 'flags=2100843<UP,BROADCAST,RUNNING,MULTICAST,IPv4,NOFAILOVER>', 'mtu', '1500']
    current_if = network.parse_interface_line(words, current_if, interfaces)

    # Check that current_if is the new interface
    assert current_if['device'] == 'bge0'
    assert current_if['ipv4'] == [{'flags': '2100843<UP,BROADCAST,RUNNING,MULTICAST,IPv4,NOFAILOVER>', 'mtu': '1500'}]

# Generated at 2022-06-13 01:51:38.210134
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():

    module = type('module', (object,), {})()
    module.run_command = type('run_command', (object,), {})()
    module.run_command.return_value = 0, '', ''

    # Test data from ifconfig -a on Solaris 11.4
    test_data = '''lo0: flags=2001000849<UP,LOOPBACK,RUNNING,MULTICAST,IPv4,VIRTUAL> mtu 8232 index 1
    inet 127.0.0.1 netmask ff000000 groupname loghost
    nd6 options=23<PERFORMNUD,ACCEPT_RTADV,AUTO_LINKLOCAL>
    ether 8:0:20:6b:f6:98
'''

# Generated at 2022-06-13 01:51:40.746375
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    """
    Test SunOSNetworkCollector class constructor
    """
    SunOSNetColl = SunOSNetworkCollector()
    assert SunOSNetColl._fact_class is not None

# Generated at 2022-06-13 01:51:49.615906
# Unit test for method parse_interface_line of class SunOSNetwork
def test_SunOSNetwork_parse_interface_line():
    module = FakeAnsibleModule()
    # test with two interfaces, the first one with ipv4 info (first line), the second with ipv6 info (second line)
    line = 'lo0: flags=2001000849<UP,LOOPBACK,RUNNING,MULTICAST,IPv4,VIRTUAL> mtu 8232 index 1'
    words = line.split()
    current_if = {'device': words[0][0:-1], 'ipv4': [], 'ipv6': [], 'type': 'unknown'}
    interfaces = {}

    s = SunOSNetwork(module)
    s.parse_interface_line(words, current_if, interfaces)

# Generated at 2022-06-13 01:51:59.752587
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    from ansible.module_utils.facts.network.sunos import SunOSNetwork as sunos_network
    from ansible.module_utils.facts.network.sunos import SunOSNetworkCollector as sunos_network_collector
    from ansible.module_utils.facts.test_utils import AnsibleExitJson, AnsibleFailJson, ModuleTestCase
    import doctest
    import sys

    class MyModule(object):
        def __init__(self):
            self.params = {}
            self.exit_json = AnsibleExitJson()
            self.fail_json = AnsibleFailJson()
            self.is_sunos = True


# Generated at 2022-06-13 01:52:08.658401
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    import ast
    import json

    from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork
    from ansible.module_utils.facts.network.sunos import SunOSNetwork

    # Only run this test if 'ifconfig' binary is present on the system
    # otherwise skip it.
    if GenericBsdIfconfigNetwork.is_ifconfig_installed():
        test_data_root = os.path.join(os.path.dirname(__file__), 'unit/data')
        expected = open(os.path.join(test_data_root, 'SunOSNetwork_get_interfaces_info.json'))
        expected_data = json.load(expected)
        bsd_network = SunOSNetwork()

# Generated at 2022-06-13 01:52:23.467586
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    nc = SunOSNetworkCollector()
    assert nc.platform == 'SunOS'
    assert nc._get_interfaces_info == nc.get_interfaces_info
    assert nc._get_interfaces_info_command == nc.get_interfaces_info_command
    assert nc._fact_class == SunOSNetwork
    assert nc.get_interfaces_info() == nc.collect()

# Unit tests for 'get_interfaces_info' and 'get_interfaces_info_command'
# and all methods they call

# Generated at 2022-06-13 01:52:34.568277
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    # test data
    ifconfig_path = '../ansible/module_utils/facts/network/generic_bsd/ifconfig'

# Generated at 2022-06-13 01:52:44.167764
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    from ansible.module_utils.facts.network.sunos import SunOSNetwork

    collector = SunOSNetwork(dict(), dict())

    # Example file with mixed IPv4 and IPv6 interfaces
    with open('testsuite/ansible_module_facts/network/sunos_ifconfig_a.txt') as sunos_ifconfig_a_file:
        out = sunos_ifconfig_a_file.read()

    interfaces, ips = collector.get_interfaces_info('')

    assert interfaces['lo0']['type'] == 'loopback'
    assert interfaces['lo0']['ipv4'][0]['mtu'] == '8232'
    assert interfaces['lo0']['ipv4'][0]['flags'] == 'UP,LOOPBACK,RUNNING'

# Generated at 2022-06-13 01:52:48.576437
# Unit test for method parse_interface_line of class SunOSNetwork
def test_SunOSNetwork_parse_interface_line():
    # Sample data copied from ifconfig -a on Solaris 11.1
    test_line = "lo0: "
    test_words = test_line.split()
    interfaces = {}
    current_if = {}
    net_obj = SunOSNetwork()
    current_if = net_obj.parse_interface_line(test_words, current_if, interfaces)
    assert current_if == {'device': 'lo0:', 'ipv4': [{'mtu': '', 'flags': []}], 'ipv6': [], 'type': 'unknown'}

    # Sample data copied from ifconfig -a on Solaris 11.1
    test_line = "lan0: flags=201000842<UP,BROADCAST,RUNNING,MULTICAST,IPv4,CoS> mtu 1500 index 2"


# Generated at 2022-06-13 01:52:56.289324
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    module = type('Module', (object,), {})()
    module.run_command = lambda args: (0,
        """lo0: flags=1000849<UP,LOOPBACK,RUNNING,MULTICAST,IPv4> mtu 8232 index 1
        inet 127.0.0.1 netmask ff000000 ipadm_args PRIVATE
        lo0: flags=2000849<UP,LOOPBACK,RUNNING,MULTICAST,IPv6> mtu 8252 index 1
        inet6 ::1/128 ipadm_args PRIVATE
        options=8000<IP6BIL>
        nd6 options=1<PERFORMNUD>
        options=8<VLAN_MTU>""",'')

    SunOSNetwork = SunOSNetworkCollector._fact_class()
   

# Generated at 2022-06-13 01:53:09.017932
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    ifconfig_path = '../ansible/module_utils/facts/network/files/sample_outputs/solaris_ifconfig_a'

# Generated at 2022-06-13 01:53:11.468106
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    obj = SunOSNetworkCollector()
    assert isinstance(obj, SunOSNetworkCollector)

# Generated at 2022-06-13 01:53:20.899034
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    fact_class = SunOSNetworkCollector
    assert fact_class._platform == 'SunOS'
    assert fact_class._fact_class == SunOSNetwork
    # Inherited properties
    assert fact_class.platform is None
    assert fact_class._device_fact_class is None
    assert fact_class._device_parser is None
    assert fact_class.DEFAULT_IFACE is None
    assert fact_class.GLOBAL_PARSERS == {
        'kernel': 'parse_kernel_version',
        'all_ipv4_addresses': 'parse_all_ipv4_addresses',
        'all_ipv6_addresses': 'parse_all_ipv6_addresses',
    }

# Generated at 2022-06-13 01:53:23.088065
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    obj_unit_test = SunOSNetworkCollector()
    assert obj_unit_test

# Generated at 2022-06-13 01:53:24.976875
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    assert SunOSNetworkCollector._platform == 'SunOS'
    assert SunOSNetworkCollector._fact_class.platform == 'SunOS'


# Generated at 2022-06-13 01:53:49.686842
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    hostname = NetworkCollector().get_hostname()
    interfaces = SunOSNetwork().get_interfaces_info('/sbin/ifconfig')[0]

    # Spot checks to ensure each interface has some expected data
    assert 'lo0' in interfaces
    assert 'en0' in interfaces
    assert 'en1' in interfaces
    assert 'bge0' in interfaces
    assert 'bge1' in interfaces
    assert 'bge0' in interfaces
    assert 'vlan2' in interfaces
    assert 'vlan3' in interfaces
    assert 'ip.tun0' in interfaces
    assert 'ip.tun1' in interfaces
    assert 'ip.tun2' in interfaces
    assert 'ip.tun3' in interfaces
    assert 'lo0' in interfaces
    assert 'net0' in interfaces

# Generated at 2022-06-13 01:53:58.934109
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    platform_facts = dict(
        distribution=dict(
            name='SunOS',
        ),
        system=dict(
            sunos_major='5',
            sunos_minor='10',
        ),
    )
    nc = SunOSNetworkCollector(module=None, facts=platform_facts)
    assert nc.facts_class._platform == 'SunOS'
    platform_facts = dict(
        distribution=dict(
            name='Illumos',
        ),
        system=dict(
            sunos_major='5',
            sunos_minor='11',
        ),
    )
    nc = SunOSNetworkCollector(module=None, facts=platform_facts)
    assert nc.facts_class._platform == 'SunOS'

# Generated at 2022-06-13 01:54:02.768884
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    network_collector = SunOSNetworkCollector()
    assert network_collector.platform == 'SunOS'
    assert network_collector._platform == 'SunOS'
    assert network_collector._fact_class == SunOSNetwork
    assert network_collector._fact_class._platform == 'SunOS'

# Generated at 2022-06-13 01:54:13.382937
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    module = type('', (), {})()

# Generated at 2022-06-13 01:54:22.104284
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    """
    This unit test checks if the parsing of the output from 'ifconfig -a'
    into the dictionary 'interfaces' is correct.
    """

    # Output from 'ifconfig -a' on Solaris 11.4

# Generated at 2022-06-13 01:54:23.468842
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    network_collector = SunOSNetworkCollector()
    assert network_collector._fact_class == SunOSNetwork

# Generated at 2022-06-13 01:54:35.170745
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():

    class TestModule(object):
        def __init__(self):
            self.run_command_called = False

        def run_command(self, cmd):
            self.run_command_called = True
            cmd_string = ' '.join(cmd)
            assert cmd_string.endswith('/sbin/ifconfig -a')
            return 0, SUNOS_IFCONFIG_A_OUTPUT, []

    test_ifconfig_path = '/sbin/ifconfig'
    test_module = TestModule()
    test_SunOSNetwork = SunOSNetwork(test_module)
    test_SunOSNetwork.get_interfaces_info(test_ifconfig_path)
    assert test_module.run_command_called
    # Method 'get_interfaces_info' contains the following assertions:
    #       assert '

# Generated at 2022-06-13 01:54:37.389613
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    mod = NetworkCollector._create_module()
    assert isinstance(SunOSNetworkCollector(mod)._fact_class(mod), SunOSNetwork)

# Generated at 2022-06-13 01:54:48.523696
# Unit test for method get_interfaces_info of class SunOSNetwork

# Generated at 2022-06-13 01:54:51.331906
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    sunos_network_collector = NetworkCollector()
    assert isinstance(sunos_network_collector, NetworkCollector)

# Generated at 2022-06-13 01:55:34.774735
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    from ansible.module_utils.facts.network.sunos.sunos import SunOSNetworkCollector
    from ansible.module_utils.facts.network.sunos.sunos import SunOSNetwork
    SunOSNetwork.platform = 'SunOS'
    module = MockModule()
    sn = SunOSNetworkCollector(module)
    iface = sn._get_interface_points()
    assert(iface.platform == 'SunOS')
    interface_path = sn.default_file_path
    iface_facts, ips = iface.get_interfaces_info(interface_path)
    assert iface_facts is not None
    assert len(iface_facts.keys()) == 8
    assert iface_facts['lo0']['type'] == 'loopback'

# Generated at 2022-06-13 01:55:45.651558
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    # This function returns a dictionary with the keys
    # interfaces, localhost, and ips.
    # interfaces is a dictionary containing interface information keyed by the
    # interface name.
    # localhost is a dictionary containing localhost information.
    # ips is a dictionary containing ip address details for interfaces.
    # The values for interfaces and localhost are dictionaries.
    # The values for ips are lists of dictionaries.
    ng = SunOSNetwork()
    interfaces, localhost, ips = ng.get_interfaces_info(ng.ifconfig_path)
    assert interfaces['lo0']['device'] == 'lo0'
    assert interfaces['lo0']['type'] == 'loopback'
    assert interfaces['lo0']['macaddress'] == '00:00:00:00:00:00'

# Generated at 2022-06-13 01:55:56.799869
# Unit test for method get_interfaces_info of class SunOSNetwork

# Generated at 2022-06-13 01:55:59.868362
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    module = AnsibleModule(argument_spec={})
    collector = SunOSNetworkCollector(module=module)
    facts = collector.collect()
    assert 'ansible_all_ipv4_addresses' in facts

# Generated at 2022-06-13 01:56:06.803911
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    '''Unit test for method get_interfaces_info of class SunOSNetwork'''


# Generated at 2022-06-13 01:56:11.971467
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    from ansible.module_utils.facts.network.sunos import SunOSFacts
    sn = SunOSFacts()
    interfaces_info, ips = sn.get_interfaces_info()
    assert len(interfaces_info.keys()) == 4, "invalid number of interfaces"

# Generated at 2022-06-13 01:56:23.701586
# Unit test for method parse_interface_line of class SunOSNetwork
def test_SunOSNetwork_parse_interface_line():
    ifconfig_net = SunOSNetwork()
    test_line = ['bge0:', 'flags=...', 'mtu', '1500']
    current_if = {}
    interfaces = {}
    current_if = ifconfig_net.parse_interface_line(test_line, current_if, interfaces)
    assert(current_if['device'] == 'bge0')
    assert('ipv4' in current_if)
    assert('ipv6' not in current_if)
    assert(len(current_if['ipv4']) == 1)
    test_line = ['bge1:', 'flags=...', 'mtu', '1500']
    current_if = ifconfig_net.parse_interface_line(test_line, current_if, interfaces)

# Generated at 2022-06-13 01:56:32.139810
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    """Test SunOSNetworkCollector constructor"""
    # Test with no args, no params
    fc = SunOSNetworkCollector()
    # pylint: disable-msg=no-member
    assert fc.platform == "SunOS"
    assert fc.default_file == '/sbin/ifconfig'
    # Test with args, no params
    fc = SunOSNetworkCollector(module=5)
    # pylint: disable-msg=no-member
    assert fc.module == 5
    assert fc.platform == "SunOS"
    assert fc.default_file == '/sbin/ifconfig'
    # Test with args, and params
    fc = SunOSNetworkCollector(module=5, file='/bin/foo')
    # pylint: disable-msg=no-member
    assert f

# Generated at 2022-06-13 01:56:40.529808
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    module = AnsibleModule(argument_spec={
        'gather_subset': dict(default=['all'], type='list')
    })

    ifconfig_path = module.get_bin_path('ifconfig', True)

    fake_net_obj = SunOSNetwork(module)
    netobj = SunOSNetwork(module)

    # mock the function run_command() so that it returns a predetermined string
    mock_run_command = MagicMock(return_value=(0, str(fake_net_obj.get_interfaces_info(ifconfig_path)), ''))
    with patch('ansible.module_utils.facts.network.sunos.run_command', mock_run_command):
        interfaces, ips = netobj.get_interfaces_info(ifconfig_path)
    # test that run_command was called as

# Generated at 2022-06-13 01:56:48.271107
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    from ansible.module_utils import basic
    from ansible.module_utils.facts import collector

    module = basic.AnsibleModule(
        argument_spec = dict(),
        supports_check_mode = False,
    )

    module.run_command = lambda *args, **kwargs: (0, output_ifconfig, "")
    collector.collector.fetch(['network'], module=module)
    facts = module.exit_json['ansible_facts']
    interfaces = facts['ansible_net_interfaces']
    ips = facts['ansible_all_ipv4_addresses'] + facts['ansible_all_ipv6_addresses']

    assert 'lo0' in interfaces
    assert 'lo0' in ips

# Generated at 2022-06-13 01:58:09.433716
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    collector = SunOSNetworkCollector()
    assert collector.platform == 'SunOS'
    assert collector.fact_class.platform == 'SunOS'
