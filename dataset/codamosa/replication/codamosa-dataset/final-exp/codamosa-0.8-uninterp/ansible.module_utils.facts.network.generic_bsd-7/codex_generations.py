

# Generated at 2022-06-13 01:27:51.626620
# Unit test for method parse_ether_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_ether_line():
    module = GenericBsdIfconfigNetwork()

    current_if = {'device': 'eth0'}
    words = ['ether', '00:16:3e:3c:2d:f1']

    module.parse_ether_line(words, current_if, {})
    assert current_if['device'] == 'eth0'
    assert current_if['macaddress'] == '00:16:3e:3c:2d:f1'
    assert current_if['type'] == 'ether'



# Generated at 2022-06-13 01:27:59.336420
# Unit test for method parse_interface_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_interface_line():
    print('GenericBsdIfconfigNetwork.test_parse_interface_line()')
    module = AnsibleModule(argument_spec=dict(
        use_ipv6=dict(type='bool', default=True),
    ))
    network_module = GenericBsdIfconfigNetwork(module)
    words = ['em0:', 'flags=8843<UP,BROADCAST,RUNNING,SIMPLEX,MULTICAST>', 'mtu', '1500', 'metric', '0']
    current_if = network_module.parse_interface_line(words)
    assert current_if['device'] == 'em0'
    assert current_if['flags'] == ['UP', 'BROADCAST', 'RUNNING', 'SIMPLEX', 'MULTICAST']
    assert current_if['mtu'] == '1500'


# Generated at 2022-06-13 01:28:10.085072
# Unit test for method parse_media_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_media_line():
    class MockModule:
        def get_bin_path(self, arg, opt_dirs=None):
            return '/sbin/ifconfig'
        def run_command(self):
            return 1, '', ''
    test_dict = dict()
    test_dict['device'] = 'em0'
    test_dict['type'] = 'unknown'
    test_dict['ipv4'] = []
    test_dict['ipv6'] = []
    test_dict['flags'] = ''
    test_dict['macaddress'] = 'unknown'
    test_dict['mtu'] = ''
    current_if = test_dict
    ips = dict(
        all_ipv4_addresses=[],
        all_ipv6_addresses=[],
    )


# Generated at 2022-06-13 01:28:14.918718
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():
    module = AnsibleModule(argument_spec=dict())
    iface = GenericBsdIfconfigNetwork(module)
    facts = iface.populate()
    assert facts['default_ipv4']['interface'] == 'lo0'
    assert facts['interfaces'] == ['lo0']


# Generated at 2022-06-13 01:28:22.562709
# Unit test for method parse_ether_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_ether_line():
    class Facts(object):
        def __init__(self,
                     module=None,
                     platform='Linux',
                     bin_dir='/bin'):
            self.module = module
            self.platform = platform
            self.bin_dir = bin_dir

    class TestModule(object):
        def __init__(self):
            self.exit_args = None
            self.exit_kwargs = None
            self.params = None

        def fail_json(self, *args, **kwargs):
            self.exit_args = args
            self.exit_kwargs = kwargs

        def get_bin_path(self, module, required=False, opt_dirs=[]):
            return module

    facts = Facts(TestModule())
    network = GenericBsdIfconfigNetwork(facts)

# Generated at 2022-06-13 01:28:24.943587
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():

    ## Need to figure out how to unit test this class
    module = AnsibleModule(argument_spec={})
    iface = GenericBsdIfconfigNetwork(module)

    result = iface.populate()
    assert result is not None


# Generated at 2022-06-13 01:28:33.761263
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():
    instance = GenericBsdIfconfigNetwork()

    default_ipv4 = {"interface": "lo0"}
    default_ipv6 = {"interface": "lo0"}

    interfaces = {
        "lo0": {
            "ipv4": [{"address": "127.0.0.1", "broadcast": "127.255.255.255", "netmask": "255.0.0.0", "network": "127.0.0.0"}],
            "ipv6": [{"address": "fe80::1%lo0", "prefix": "64", "scope": "link"}],
        }
    }

    instance.merge_default_interface(default_ipv4, interfaces, 'ipv4')
    instance.merge_default_interface(default_ipv6, interfaces, 'ipv6')



# Generated at 2022-06-13 01:28:43.373236
# Unit test for method parse_ether_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_ether_line():
    network_module = GenericBsdIfconfigNetwork()
    iface_data = {}
    iface_data['device'] = 'rl0'

    line = 'ether 00:a0:cc:2b:1c:fc'
    words = line.split()
    network_module.parse_ether_line(words, iface_data, {})
    assert iface_data['device'] == 'rl0'
    assert iface_data['macaddress'] == '00:a0:cc:2b:1c:fc'
    assert iface_data['type'] == 'ether'

# Generated at 2022-06-13 01:28:53.519721
# Unit test for method parse_media_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_media_line():
    platform = 'Generic_BSD_Ifconfig'
    media_current_if = {}
    media_words = ['media:', 'IEEE', '802.11', 'autoselect', '(autoselect)', 'status:', 'active']
    GenericBsdIfconfigNetwork.parse_media_line(platform, media_words, media_current_if, None)
    assert media_current_if['media'] == 'IEEE 802.11'
    assert media_current_if['media_select'] == 'autoselect'
    assert media_current_if['media_type'] == 'autoselect'
    assert media_current_if['media_options'] == ['active']

# Generated at 2022-06-13 01:29:01.193875
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_default_interfaces():
    from ansible.module_utils.net_tools.net_facts.linux.network_generic_bsd_ifconfig import GenericBsdIfconfigNetwork
    from mock import MagicMock

# Generated at 2022-06-13 01:29:40.537215
# Unit test for method parse_interface_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_interface_line():
    # Test when the interface is loopback
    gb = GenericBsdIfconfigNetwork()
    words = ["lo0:", "flags=8049<UP,LOOPBACK,RUNNING,MULTICAST>", "metric", "0", "mtu", "33184"]
    cif = gb.parse_interface_line(words)
    assert 'loopback' == cif['type']
    assert 'lo0' == cif['device']
    assert '33184' == cif['mtu']
    assert 'unknown' == cif['macaddress']
    assert 'UP,LOOPBACK,RUNNING,MULTICAST' == ",".join(cif['flags'])
    # Test when the interface is ether

# Generated at 2022-06-13 01:29:50.798321
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():
    module = AnsibleModule({})
    module.fail_json = Mock(return_value=module.exit_json)
    module.run_command = Mock(return_value=(0, '', ''))
    module.get_bin_path = Mock(return_value='/sbin/ifconfig')

    # no interface
    defaults = {
        'interface': '',
        'ipv4': {},
        'ipv6': {},
        'type': 'loopback'
    }

# Generated at 2022-06-13 01:29:52.818589
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():
    # TODO: Write unit test for GenericBsdIfconfigNetwork.populate
    pass


# Generated at 2022-06-13 01:30:03.549726
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork

# Generated at 2022-06-13 01:30:08.992361
# Unit test for method parse_ether_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_ether_line():
    ifconfig_out = """
lo0: flags=8049<UP,LOOPBACK,RUNNING,MULTICAST> mtu 16384
	options=3<RXCSUM,TXCSUM>
	inet 127.0.0.1 netmask 0xff000000
	inet6 ::1 prefixlen 128
	inet6 fe80::1%lo0 prefixlen 64 scopeid 0x1
	nd6 options=1<PERFORMNUD>
utun0: flags=8051<UP,POINTOPOINT,RUNNING,MULTICAST> mtu 1380
	inet 10.2.2.6 --> 10.2.2.6 netmask 0xffffff00
"""
    ifconfig_obj = GenericBsdIfconfigNetwork()
    current_if = {}
    ips = {}
    ifconfig_obj.parse

# Generated at 2022-06-13 01:30:18.943634
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )

    defaults = dict(
        gateway="192.168.1.1",
        address="192.168.1.11",
    )
    interface = "em0"

# Generated at 2022-06-13 01:30:27.149245
# Unit test for method get_interfaces_info of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_interfaces_info():
    network_fixture = GenericBsdIfconfigNetwork()

# Generated at 2022-06-13 01:30:27.698929
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():
    pass

# Generated at 2022-06-13 01:30:35.903656
# Unit test for method get_interfaces_info of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_interfaces_info():
    # create a mock module
    from ansible_collections.ansible.community.tests.unit.compat import unittest
    from ansible_collections.ansible.community.tests.unit.compat.mock import patch, MagicMock

    def side_effect_function(module):
        return module.params['output']

    def side_effect_function2(module):
        return module.params['path']

    module = MagicMock()

# Generated at 2022-06-13 01:30:44.157346
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():
    # Initialization
    module = MockModule()
    network_module = NetworkModule(module)
    generic_bsd_ifconfig_network = GenericBsdIfconfigNetwork(module)
    defaults = {'interface': 'em0'}
    interfaces = {'em0': {'ipv4': []}, 'em1': {'ipv4': []}}
    ip_type = 'ipv4'

    # Test case 1: exceptions
    try:
        generic_bsd_ifconfig_network.merge_default_interface(defaults, interfaces, ip_type)
    except Exception as e:
        assert False, "Failed: Should not raise exception."

    # Test case 2: standard case #1
    defaults = {'interface': 'em0'}

# Generated at 2022-06-13 01:31:08.226370
# Unit test for method populate of class GenericBsdIfconfigNetwork

# Generated at 2022-06-13 01:31:14.221764
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_default_interfaces():
    network = GenericBsdIfconfigNetwork()
    default_ipv4 = {
        'gateway': '192.168.0.1',
        'interface': 'eth0',
        'address': '192.168.0.2'
    }
    default_ipv6 = {
        'interface': 'eth0'
    }

    assert network.get_default_interfaces( 'route') == (default_ipv4, default_ipv6)



# Generated at 2022-06-13 01:31:24.617572
# Unit test for method get_interfaces_info of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_interfaces_info():
        fake_ioctl = {}
        module_ioctl = {}

# Generated at 2022-06-13 01:31:28.496341
# Unit test for method get_options of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_options():
    GBI = GenericBsdIfconfigNetwork()
    option_string = '<UP,BROADCAST,LOOPBACK,RUNNING,MULTICAST>'
    options = ['UP', 'BROADCAST', 'LOOPBACK', 'RUNNING', 'MULTICAST']
    if GBI.get_options(option_string) != options:
        raise AssertionError()
# end of test_GenericBsdIfconfigNetwork_get_options


# Generated at 2022-06-13 01:31:40.191605
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():
    ifconfig = GenericBsdIfconfigNetwork()
    defaults = {'interface':'en0', 'gateway':'192.168.0.1'}
    interfaces = {'en0': {'device':'en0', 'ipv4': [
                        {'address':'192.168.0.2', 'netmask':'0xffffff00', 'broadcast':'192.168.0.255'},
                        {'address':'172.16.10.2', 'netmask':'0xffffff00', 'broadcast':'172.16.10.255'}
                        ],
                    'ipv6': [], 'type':'loopback', 'macaddress':'01:23:45:67:89:ab'}}
    ip_type = 'ipv4'
    ifconfig.merge_default_interface

# Generated at 2022-06-13 01:31:44.504478
# Unit test for method get_options of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_options():
    network = GenericBsdIfconfigNetwork()
    string = 'flags=<UP,BROADCAST,RUNNING,PROMISC,MULTICAST>'
    option_list = ['UP','BROADCAST','RUNNING','PROMISC','MULTICAST']
    assert network.get_options(string) == option_list

# Generated at 2022-06-13 01:31:55.568622
# Unit test for method detect_type_media of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_detect_type_media():
    # genericBSDIfconfigNetwork => class object
    generic_bsd_ifconfig_network = GenericBsdIfconfigNetwork()
    # interfaces => local variable

# Generated at 2022-06-13 01:32:00.915217
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():
    module = unittest.mock.MagicMock()
    obj = GenericBsdIfconfigNetwork(module)
    ifacelist = {}
    default_ipv4 = {}
    default_ipv6 = {}
    ipv4_address1 = {'address': '192.168.1.1', 'netmask': '255.255.255.0',
                     'network': '192.168.1.0'}
    ipv4_address2 = {'address': '192.168.1.2', 'netmask': '255.255.255.0',
                     'network': '192.168.1.0'}
    ipv6_address1 = {'address': '::1', 'prefix': '128',
                     'scope': 'host'}

# Generated at 2022-06-13 01:32:08.819213
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():
    # Test merge_default_interface
    class TestGenericBsdIfconfigNetwork(GenericBsdIfconfigNetwork):
        pass
    tbd = TestGenericBsdIfconfigNetwork()
    defaults = {'interface': 'ix0'}
    interfaces = {'ix0': {'ipv6': [{'address': '2001:db8::1', 'prefix': '64'}]}}
    tbd.merge_default_interface(defaults, interfaces, 'ipv6')
    assert defaults == {'interface': 'ix0', 'ipv6': [{'address': '2001:db8::1', 'prefix': '64'}]}


# Generated at 2022-06-13 01:32:17.968076
# Unit test for method get_interfaces_info of class GenericBsdIfconfigNetwork

# Generated at 2022-06-13 01:32:50.723862
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():
    network = GenericBsdIfconfigNetwork(module=object)
    result = network.populate()
    assert result != None


# Generated at 2022-06-13 01:33:00.144494
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():
    """Test populate."""

# Generated at 2022-06-13 01:33:11.943583
# Unit test for method detect_type_media of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_detect_type_media():
    import copy
    import test_utils

    # Initialize test variables
    module_args = dict(
        config_file=dict(default=None, required=False),
        cache_timeout=dict(default=None, type='int', required=False),
    )
    platform_mock = ['Generic_BSD_Ifconfig', 'Linux']
    platform_facts = dict(
        system='Linux',
        python_version='2.7.5',
        python_executable='/usr/bin/python',
        python_version_short='2.7',
        python_version_nano='2.7.5',
        python_version_tuple=(2, 7, 5, 'final', 0),
    )
    test_utils.system_mock = copy.deepcopy(platform_mock)
    test_utils.system

# Generated at 2022-06-13 01:33:14.636884
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():
    print("test_GenericBsdIfconfigNetwork_populate()")
    module = AnsibleModule(argument_spec=dict())
    
    module.run_co

# Generated at 2022-06-13 01:33:26.532880
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():
    args = dict(
        config_file=dict(
            default='/dev/null', type='path', required=False),
        gather_subset=[],
        filter=dict(default=None, required=False, type='str')
    )
    ansible_options = dict(
        connection='local',
    )
    module = FakeAnsibleModule(**ansible_options)
    mgr = GenericBsdIfconfigNetwork(module)

    code, output = mgr.populate()

    assert code == 0
    assert len(output) > 3
    assert 'interfaces' in output
    assert 'default_ipv4' in output
    assert 'default_ipv6' in output
    assert 'all_ipv4_addresses' in output
    assert 'all_ipv6_addresses' in output




# Generated at 2022-06-13 01:33:35.041038
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():
    # Arrange
    class_populate = None
    module_populate = None

    def Mock_module_populate(self):
        module_populate = True
        return 123
    module_populate = Mock_module_populate
    GenericBsdIfconfigNetwork.populate = module_populate

    class_populate = GenericBsdIfconfigNetwork()
    class_populate.module = Mock()

    # Act
    result = class_populate.populate()

    # Assert
    assert(result == 123)

# Generated at 2022-06-13 01:33:46.688042
# Unit test for method get_options of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_options():

    my_network = GenericBsdIfconfigNetwork()

    assert my_network.get_options('UP,LOOPBACK,RUNNING') == ['UP', 'LOOPBACK', 'RUNNING']
    assert my_network.get_options('UP,LOOPBACK') == ['UP', 'LOOPBACK']
    assert my_network.get_options('UP') == ['UP']
    assert my_network.get_options('UP,RUNNING') == ['UP', 'RUNNING']
    assert my_network.get_options('UP,RUNNING,') == ['UP', 'RUNNING']
    assert my_network.get_options('UP,,RUNNING') == ['UP', 'RUNNING']
    assert my_network.get_options('UP,,,RUNNING') == ['UP', 'RUNNING']

# Generated at 2022-06-13 01:33:55.371626
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():
    import platform
    from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.network import Network
    from ansible_collections.ansible.netcommon.tests.unit.compat.mock import Mock
    from ansible_collections.ansible.netcommon.tests.unit.compat.mock import patch
    from ansible_collections.ansible.netcommon.tests.unit.utils.network_mock import mock_get_bin_path
    from ansible_collections.ansible.netcommon.tests.unit.utils.network_mock import mock_get_file_content
    from ansible_collections.ansible.netcommon.tests.unit.utils.network_mock import mock_run_commands

# Generated at 2022-06-13 01:34:06.488655
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():
    # Setup
    my_host = Host(name='host.example.com', groups=['my_host_group'], variables={})
    my_host.set_variable('ansible_user', 'root')

    dc_module = DummyModule()

    dc_module.params.update(dict(
        gather_network_resources=['interfaces'],
    ))

    # Act
    GenericBsdIfconfigNetwork(module=dc_module).populate(my_host.fact_cache)

    # Assert
    assert 'interfaces' in my_host.fact_cache
    assert len(my_host.fact_cache.get('interfaces')) > 0

# Main
if __name__ == '__main__':
    print(json.dumps(test_GenericBsdIfconfigNetwork_populate()))

# Generated at 2022-06-13 01:34:17.965929
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():
    module = ansible_module_create()