

# Generated at 2022-06-13 01:28:10.660122
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():
    hostname = 'Hostname'
    module = setup_ansible_module(None, None, {"ansible_facts": {'ansible_hostname': hostname}})
    generic_bsd_ifconfig_network = GenericBsdIfconfigNetwork(module)
    ansible_facts_from_cmd = generic_bsd_ifconfig_network.populate()

    assert ansible_facts_from_cmd is not None
    assert ansible_facts_from_cmd['default_ipv4'] is not None
    assert ansible_facts_from_cmd['default_ipv6'] is not None
    assert ansible_facts_from_cmd['all_ipv4_addresses'] is not None
    assert ansible_facts_from_cmd['all_ipv6_addresses'] is not None
    assert ansible_facts_from

# Generated at 2022-06-13 01:28:20.302910
# Unit test for method get_interfaces_info of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_interfaces_info():
    test_module, test_class = import_module_get_cls('ansible.modules.network.freebsd', 'GenericBsdIfconfigNetwork')
    network = GenericBsdIfconfigNetwork(test_module)

# Generated at 2022-06-13 01:28:27.644836
# Unit test for method parse_media_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_media_line():
    params = dict(ifconfig_out='media: Ethernet autoselect (1000baseT <full-duplex>)',
                  ifconfig_path='ifconfig',
                  module=MagicMock(),
                  run_command=MagicMock())
    current_if = dict()
    ips = dict()

    gen_ifconfig_net = GenericBsdIfconfigNetwork(ansible_module=params['module'])
    gen_ifconfig_net.run_command = params['run_command']
    gen_ifconfig_net.parse_media_line(params['ifconfig_out'].split(),
                                      current_if=current_if,
                                      ips=ips)

    assert 'media' in current_if
    assert current_if['media'] == 'Ethernet'
    assert 'media_select' in current_if

# Generated at 2022-06-13 01:28:38.761621
# Unit test for method detect_type_media of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_detect_type_media():
    network = GenericBsdIfconfigNetwork()
    interfaces = {}
    assert network.detect_type_media(interfaces) == {}


# Generated at 2022-06-13 01:28:51.775030
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork

# Generated at 2022-06-13 01:29:00.160332
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():
    # Get the class that we want to exercise
    module_class = GenericBsdIfconfigNetwork()

    # set up the results of module.get_bin_path()
    module_class.module.get_bin_path = answers.get_bin_path

    # set up the results of module_class.run_command()
    module_class.module.run_command = answers.run_command

    # Assert that the results are as we expect

# Generated at 2022-06-13 01:29:11.820463
# Unit test for method parse_inet_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet_line():

    ipv4_addr = '192.0.2.1'
    ipv4_netmask = '255.255.0.0'
    netmask_length = 16
    netmask_bin = (1 << 32) - (1 << 32 >> netmask_length)
    ipv4_netmask_hex = socket.inet_ntoa(struct.pack('!L', netmask_bin))


# Generated at 2022-06-13 01:29:18.257427
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_default_interfaces():
    module = NetworkModule({'ANSIBLE_MODULE_ARGS': {}}, '.')
    network = GenericBsdIfconfigNetwork(module)
    default_interfaces = {
        'v4': {'interface': 'en0', 'gateway': '10.0.0.1'},
        'v6': {},
    }

    actual = network.get_default_interfaces('route')

    assert default_interfaces == actual


# Generated at 2022-06-13 01:29:28.735496
# Unit test for method parse_interface_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_interface_line():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(argument_spec={})
    collection = GenericBsdIfconfigNetwork(module)
    result = collection.parse_interface_line(['em0:', 'flags=8843<UP,BROADCAST,RUNNING,SIMPLEX,MULTICAST>', 'mtu', '1500', 'lladdr', '00:01:02:03:04:05', 'index', '10', 'priority:', '0', 'media:', 'Ethernet', 'autoselect', '(1000baseT', '<full-duplex>)', 'status:', 'active'])

# Generated at 2022-06-13 01:29:35.340508
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():
    platform = 'Generic_BSD_Ifconfig'
    module = AnsibleModule(argument_spec=dict())
    network = GenericBsdIfconfigNetwork(module)

    # Test empty target interface
    dest_interface = dict()
    src_interface = dict()
    src_interface['interface'] = 'int1'
    src_interface['ipv4'] = [dict(address='127.0.0.1', netmask='255.0.0.0')]
    src_interface['ipv6'] = [dict(address='::1', netmask='ffff:ffff::')]
    src_interface['a'] = 'avalue'

    network.merge_default_interface(dest_interface, dict(int1=src_interface), 'ipv4')
    assert dest_interface == dict()

    dest_interface = dict()
   

# Generated at 2022-06-13 01:29:51.954892
# Unit test for method parse_media_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_media_line():
    n = GenericBsdIfconfigNetwork()
    words = ['media:', 'Ethernet', 'autoselect', '(100baseTX)', 'status:', 'active', 'lladdr', 'xx:xx:xx:xx:xx:xx', 'nd6']
    current_if = {}
    ips = {}
    n.parse_media_line(words, current_if, ips)
    assert current_if['media'] == 'Ethernet'
    assert current_if['media_select'] == 'autoselect'
    assert current_if['media_type'] == '100baseTX'
    assert current_if['media_options'] == ['status:', 'active', 'lladdr', 'xx:xx:xx:xx:xx:xx', 'nd6']


# Generated at 2022-06-13 01:30:02.783976
# Unit test for method detect_type_media of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_detect_type_media():
    gen = GenericBsdIfconfigNetwork({"bin_path": "/usr/bin"})

# Generated at 2022-06-13 01:30:04.998485
# Unit test for method detect_type_media of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_detect_type_media():
    network = GenericBsdIfconfigNetwork()
    iface = {'media': 'ether'}
    result = network.detect_type_media(iface)
    assert result == {'media': 'ether', 'type': 'ether'}


# Generated at 2022-06-13 01:30:16.956941
# Unit test for method parse_media_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_media_line():
    # Test
    module = generic

    # Mock
    class Tmp(object):
        pass

    tmp_module = Tmp()


    tmp_module.MODULE_COMPLEX_ARGS = dict()
    tmp_module.MODULE_COMPLEX_ARGS['use_defaults'] = False
    tmp_module.MODULE_COMPLEX_ARGS['gather_subset'] = list()
    tmp_module.MODULE_COMPLEX_ARGS['gather_network_resources'] = list()

    # Create class instance
    network = GenericBsdIfconfigNetwork(tmp_module)

    # Make test data
    words = ['media:', 'Ethernet', 'autoselect', '(1000baseT)', 'status:', 'active']

# Generated at 2022-06-13 01:30:26.073820
# Unit test for method get_interfaces_info of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_interfaces_info():
    # Initialization
    module = AnsibleModule(argument_spec={})
    platform = 'Generic_BSD_Ifconfig'
    ifconfig_path = module.get_bin_path('ifconfig')

    network = GenericBsdIfconfigNetwork(module)
    # Test for FreeBSD
    interfaces, ips = network.get_interfaces_info(ifconfig_path)
    assert interfaces[platform].get('device') == 'lo0'
    # Test for NetBSD
    interfaces, ips = network.get_interfaces_info(ifconfig_path, '-e')
    assert interfaces[platform].get('device') == 'lo0'
    # Test for OpenBSD
    interfaces, ips = network.get_interfaces_info(ifconfig_path, '-A')
    assert interfaces[platform].get('device') == 'lo0'

# Generated at 2022-06-13 01:30:34.488337
# Unit test for method get_interfaces_info of class GenericBsdIfconfigNetwork

# Generated at 2022-06-13 01:30:43.214123
# Unit test for method parse_inet_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet_line():
    import sys
    import pytest
    import socket

    socket.gethostname = lambda: 'test'
    out = 'inet 10.0.0.1 netmask 0xfffffe00 broadcast 10.0.0.255'
    words = out.split()

    net_cls = GenericBsdIfconfigNetwork()
    current_if = {'device': 'lo0', 'ipv4': [], 'ipv6': [], 'type': 'unknown'}
    ips = dict(
        all_ipv4_addresses=[],
        all_ipv6_addresses=[],
    )
    net_cls.parse_inet_line(words, current_if, ips)

    assert len(current_if['ipv4']) == 1

# Generated at 2022-06-13 01:30:53.721225
# Unit test for method detect_type_media of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_detect_type_media():
    obj = GenericBsdIfconfigNetwork({})

# Generated at 2022-06-13 01:31:02.099922
# Unit test for method get_interfaces_info of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_interfaces_info():
    parser = GenericBsdIfconfigNetwork()

    interfaces = parser.get_interfaces_info('/usr/bin/ifconfig')
    assert len(interfaces[0]) == 2
    assert len(interfaces[1]) == 2
    assert len(interfaces[1]['all_ipv4_addresses']) == 2
    assert len(interfaces[1]['all_ipv6_addresses']) == 2
    for iface in interfaces[0]:
        assert len(interfaces[0][iface][0]['flags']) == 3
        assert interfaces[0][iface][0]['type'] == interfaces[0][iface][0]['type']
        assert len(interfaces[0][iface][0]['ipv4']) == 1

# Generated at 2022-06-13 01:31:04.815812
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():
    # TODO: test method execute of class GenericBsdIfconfigNetwork
    raise NotImplementedError()
# Method of class GenericBsdIfconfigNetwork

# Generated at 2022-06-13 01:31:26.489010
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_default_interfaces():

    class EmptyObject:
        """ Empty object that can be used to get a struct like object """
        def __init__(self, **entries):
            self.__dict__.update(entries)

    hostvars = EmptyObject()

    # Create a simple ifconfig output to test get_default_interfaces
    ifconfig_path = './ifconfig'
    route_path = './route'

# Generated at 2022-06-13 01:31:32.728946
# Unit test for method parse_inet_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet_line():
    hostn = "example"
    network = GenericBsdIfconfigNetwork()
    current_if = {}
    ips = dict(all_ipv4_addresses=[])
    words=['inet','127.0.0.1','netmask','0xff000000']
    network.parse_inet_line(words, current_if, ips)
    assert(current_if == {'ipv4': [{'address': '127.0.0.1',
       'netmask': '255.255.255.255',
       'network': '127.0.0.1',
       'broadcast': '127.0.0.1'}], 'device': 'inet'})
    words=['inet','127.0.0.1']
    network.parse_inet_line(words, current_if, ips)


# Generated at 2022-06-13 01:31:42.620946
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():
    from ansible_collections.notmintest.not_a_real_collection.plugins.module_utils.network.common.utils import dict_merge

    # Create an instance of the class we want to test
    network_info = GenericBsdIfconfigNetwork()

    # Mock the module this class depends on
    module = MagicMock()
    setattr(module, 'get_bin_path', MagicMock(return_value=True))
    setattr(module, 'run_command', MagicMock(return_value=True))

    # Assign the module mock.
    network_info.module = module

    # Test the populate method
    network_info.populate()



# Generated at 2022-06-13 01:31:53.879983
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )

    # We need to change the module path to get to the right test data
    module.params['ansible_facts_dir'] = os.path.dirname(__file__)
    network = GenericBsdIfconfigNetwork()

    result = network.populate()
    assert 'all_ipv4_addresses' in result
    assert 'all_ipv6_addresses' in result
    assert 'default_ipv4' in result
    assert 'default_ipv6' in result
    assert 'interfaces' in result

    for interface in result['interfaces']:
        assert interface in result.keys()
        assert 'ipv4' in result[interface].keys()

# Generated at 2022-06-13 01:32:00.697035
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():
    args = dict(
        collected_facts=dict()
    )

# Generated at 2022-06-13 01:32:08.943244
# Unit test for method detect_type_media of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_detect_type_media():
    """get_interfaces_info"""

    # [('IF_NAME', 'IF_TYPE'),
    #  ... ]
    testcases = [
        (['xl0', 'ether'],),
    ]
    for testcase in testcases:
        interfaces = {}
        current_if = {'device': testcase[0][0],
                      'media': testcase[0][1]}
        interfaces[current_if['device']] = current_if
        host = GenericBsdIfconfigNetwork()
        host.detect_type_media(interfaces)
        assert interfaces[current_if['device']]['type'] == testcase[0][1]


# Generated at 2022-06-13 01:32:18.065432
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():
    G = GenericBsdIfconfigNetwork()
    ifconfig_path = G.module.get_bin_path('ifconfig')

    cmd = [ifconfig_path, '-a']
    rc, out, err = G.module.run_command(cmd)
    #G.module.fail_json(msg=out)

    interfaces, ips = G.get_interfaces_info(ifconfig_path)
    interfaces = G.detect_type_media(interfaces)

    default_ipv4, default_ipv6 = G.get_default_interfaces(route_path)
    G.merge_default_interface(default_ipv4, interfaces, 'ipv4')
    G.merge_default_interface(default_ipv6, interfaces, 'ipv6')
    network_facts = dict()
   

# Generated at 2022-06-13 01:32:19.803488
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_default_interfaces():
    module = AnsibleModule(argument_spec=dict())
    obj = GenericBsdIfconfigNetwork(module)
    obj.get_default_interfaces('/sbin/route')



# Generated at 2022-06-13 01:32:31.850946
# Unit test for method get_interfaces_info of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_interfaces_info():
    from ansible.module_utils.facts import Collector
    from ansible.module_utils.facts.network.generic_bsd import ifconfig

    class ReturnCode:
        SUCCESS = 0
        ERROR = 1

    class FakeModule:
        def run_command(command, check_rc=True):
            if 'ifconfig' in command:
                if command[1] == '-a':
                    return ReturnCode.SUCCESS, '\n'.join(BSD_IFCONFIG), ''
                elif command[1] == '-l':
                    return ReturnCode.SUCCESS, '\n'.join(BSD_NETWORK_INTERFACES), ''
                else:
                    return ReturnCode.ERROR, '', 'FAIL'
            else:
                return ReturnCode.ERROR, '', 'FAIL'


# Generated at 2022-06-13 01:32:38.607056
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():
    # Arrange
    defaults = {'interface':'en1', 'address':'192.168.0.1'}
    interfaces = {'en0':{'ipv4':[{'address': '192.168.1.1'}, {'address': '192.168.1.2'}], 'ipv6':[]}, 'en1':{'ipv4':[{'address': '192.168.0.1'}, {'address': '192.168.0.2'}], 'ipv6':[]}}

    # Act
    GenericBsdIfconfigNetwork().merge_default_interface(defaults, interfaces, 'ipv4')

    # Assert
    assert defaults['interface'] == 'en1'
    assert 'ipv4' not in defaults
    assert len(defaults) == 3

#

# Generated at 2022-06-13 01:32:53.728587
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():
    default = dict(interface = "a" , a = "a", b = "b", ipv4 = [], ipv6 = [])
    interfaces = dict(a = {'device': 'a', 'ipv4': [{'address': '10.0.0.1', 'broadcast': '192.168.0.1', 'netmask': '255.0.0.0'}], 'ipv6': [{'address': '2001:db8::1'}]})
    network = GenericBsdIfconfigNetwork(dict())
    network.merge_default_interface(default, interfaces, 'ipv4')
    assert default['device'] == 'a'
    assert len(default['ipv4']) == 1
    assert default['ipv4'][0]['address'] == '10.0.0.1'

# Generated at 2022-06-13 01:33:01.509009
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_default_interfaces():
    args = {}
    args['route_path'] = '/bin/route_test'

    MockedModule = MagicMock()
    MockedModule.run_command.return_value = ('0', 'interface: en0\ngateway: 192.168.0.1', "")
    real_import = __import__
    def mock_import(name, *args):
        if name == 'ansible.module_utils.basic':
            return MockedModule
        return real_import(name, *args)
    # Override '__import__' builtin
    builtins.__import__ = mock_import

    ifconfig_obj = GenericBsdIfconfigNetwork(MockedModule)
    default_ipv4, default_ipv6 = ifconfig_obj.get_default_interfaces('/bin/route_test')

# Generated at 2022-06-13 01:33:12.105264
# Unit test for method detect_type_media of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_detect_type_media():
    test = GenericBsdIfconfigNetwork()
    test_interfaces = {'lo0': {'ipv4': [], 'ipv6': [], 'type': 'unknown', 'device': 'lo0', 'macaddress': 'unknown', 'flags': ['LOOPBACK', 'RUNNING', 'MULTICAST']}}
    result = test._detect_type_media(test_interfaces)
    assert result == {'lo0': {'ipv4': [], 'ipv6': [], 'type': 'loopback', 'device': 'lo0', 'macaddress': 'unknown', 'flags': ['LOOPBACK', 'RUNNING', 'MULTICAST']}}

# Generated at 2022-06-13 01:33:23.768829
# Unit test for method get_interfaces_info of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_interfaces_info():
    """
    Test get_interfaces_info
    """
    from pprint import pprint

    from ansible_collections.notstdlib.moveitallout.tests.unit.compat.mock import patch
    from ansible_collections.notstdlib.moveitallout.plugins.modules import network_cli

    with patch.object(network_cli, 'NetworkModule') as patched_nm:
        inst = patched_nm.return_value
        ifconfig_path = '/sbin/ifconfig'
        inst.get_bin_path.return_value = ifconfig_path
        # Construct network_module instance
        inst.get_bin_path.return_value = ifconfig_path
        nm = inst.NetworkModule
        nm.__init__ = lambda self, *args, **kwargs: None
        nm.module = nm

# Generated at 2022-06-13 01:33:26.133939
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():
    GenericBsdIfconfigNetwork.merge_default_interface(
        {'interface': 'lo0'},
        {'lo0': {'foo': 'bar', 'ipv4': [{'address': '127.0.0.1'}]}},
        'ipv4'
    )



# Generated at 2022-06-13 01:33:37.438610
# Unit test for method parse_inet_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet_line():
    ns = GenericBsdIfconfigNetwork()

    # No Netmask
    words = [
        'em0',
    ]
    current_if = {'ipv4': []}
    ips = dict(
        all_ipv4_addresses=[],
    )
    # Should not fail
    ns.parse_inet_line(words, current_if, ips)

    # CIDR-Style netmask
    words = [
        'em0:',
        '192.168.0.2/24',
        '0x0',
        '0xc0a80001',
        'netmask',
        '0xffffff00',
        'broadcast',
        '0xc0a800ff',
    ]
    current_if = {'ipv4': []}

# Generated at 2022-06-13 01:33:44.460656
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_default_interfaces():
    """
    Test case to verify the output of get_default_interfaces on a sys with both an IPv4 and IPv6 network assets
    """
    dut_mock = MagicMock()

# Generated at 2022-06-13 01:33:51.932909
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():
    # Initialize
    net_info = {}
    net_info['interfaces_list'] = ['lo0', 're0', 're1', 're2', 're3', 'bridge0', 'tap0', 'epair0b', 'epair0a']

# Generated at 2022-06-13 01:33:58.792901
# Unit test for method parse_inet6_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet6_line():

    # test data
    n = GenericBsdIfconfigNetwork()
    words = ['inet6', 'fe80::1%lo0', 'prefixlen', '64', 'scopeid', '0x4']
    current_if = {
        'device': 'lo0',
        'ipv4': [{
            'address': '127.0.0.1',
            'broadcast': '255.0.0.0',
            'netmask': '255.0.0.0',
            'network': '127.0.0.0'
        }],
        'ipv6': [],
        'type': 'unknown',
        'mtu': '33184',
        'flags': ['UP', 'LOOPBACK', 'RUNNING', 'MULTICAST']
    }

# Generated at 2022-06-13 01:34:08.065861
# Unit test for method detect_type_media of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_detect_type_media():
    #  Correctly detect ether media as ether type.
    interfaces = {'lo0': {'media': 'Ethernet 10Gb/s'}}
    check = {'lo0': {'media': 'Ethernet 10Gb/s', 'type': 'ether'}}
    _module = MagicMock()
    _class = GenericBsdIfconfigNetwork(_module)
    assert _class.detect_type_media(interfaces) == check

    # Correctly detect ether media as ether type.
    interfaces = {'lo0': {'media': 'Ethernet'}}
    check = {'lo0': {'media': 'Ethernet', 'type': 'ether'}}
    _module = MagicMock()
    _class = GenericBsdIfconfigNetwork(_module)

# Generated at 2022-06-13 01:34:25.048192
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_default_interfaces():
    # Set up mock of module.run_command
    mock_module = Mock()

    # Set mock return values for 'run_command' transformation
    mock_module.run_command.side_effect = lambda args, **kwargs: (test_defaults[tuple(args)], '', '')

    class_under_test = GenericBsdIfconfigNetwork(mock_module)
    result_v4, result_v6 = class_under_test.get_default_interfaces('/path/to/route')

    assert result_v4 == test_defaults_results['v4']
    assert result_v6 == test_defaults_results['v6']


# Generated at 2022-06-13 01:34:36.470388
# Unit test for method parse_media_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_media_line():
    
    network_facts = GenericBsdIfconfigNetwork()
    
    # Test parse_media_line
    # Input set 1:
    #    Words: [
    #        "media:", "Ethernet", "autoselect"
    #    ]
    #  Expected Result:
    #    empty
    words = [
        "media:", "Ethernet", "autoselect"
    ]  

    expected_current_if = {}
    expected_ips = {}
    expected_current_if['media'] = "Ethernet"
    expected_current_if['media_select'] = "autoselect"
    expected_ips['all_ipv4_addresses'] = []
    

# Generated at 2022-06-13 01:34:43.081208
# Unit test for method parse_interface_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_interface_line():
    # test string
    test_str = "lo0: flags=8049<UP,LOOPBACK,RUNNING,MULTICAST> metric 0 mtu 16384\n"
    # parse it
    interface_line = GenericBsdIfconfigNetwork().parse_interface_line(test_str.split())
    # test result
    assert "lo0" == interface_line['device']
    assert "16384" == interface_line['mtu']
    assert ["UP", "LOOPBACK", "RUNNING", "MULTICAST"] == interface_line['flags']


# Generated at 2022-06-13 01:34:52.640591
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_default_interfaces():
    myNet = GenericBsdIfconfigNetwork()
    myNet.module = AnsibleModule(argument_spec={}, supports_check_mode=True)
    myNet.module.socket = SocketMockup()
    myNet.module.socket.add_command({'command': ['/sbin/route', '-n', 'get', 'default'], 'rc': 0, 'stdout': """route to: default
destination: default
  route to: default
destination: default
mask: default
  gateway: default
  interface: default
"""})

# Generated at 2022-06-13 01:35:03.185952
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():
    ifconfig_path = '/sbin/ifconfig'
    route_path = '/sbin/route'
    if not os.path.exists(ifconfig_path):
        return

    module = MockModule()
    module.run_command = Mock(return_value=(0, ifconfig_out, ''))
    module.get_bin_path = Mock(side_effect=lambda arg: arg)

    network_facts = GenericBsdIfconfigNetwork.populate()

    assert network_facts['default_ipv4']['interface'] == 'en1'
    assert network_facts['default_ipv4']['address'] == '192.168.0.49'
    assert network_facts['default_ipv4']['netmask'] == '255.255.255.0'

# Generated at 2022-06-13 01:35:05.949685
# Unit test for method get_interfaces_info of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_interfaces_info():
    interfaces, ips = GenericBsdIfconfigNetwork.get_interfaces_info(None, 'tests/data/sample_ifconfig_hr_emx/ifconfig-plain.txt')
    assert('lo0' in interfaces)


# Generated at 2022-06-13 01:35:15.146511
# Unit test for method get_interfaces_info of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_interfaces_info():

    module = AnsibleModule({})
    platform = 'Generic_BSD_Ifconfig'
    network = GenericBsdIfconfigNetwork(module)

    # NetBSD ifconfig
    interfaces, ips = network.get_interfaces_info('ifconfig')

    assert isinstance(interfaces, dict)
    for name, info in interfaces.items():
        assert isinstance(name, str)
        assert isinstance(info, dict)
        assert 'device' in info
        assert isinstance(info['device'], str)
        assert 'ipv4' in info
        assert isinstance(info['ipv4'], list)
        for ip in info['ipv4']:
            assert isinstance(ip, dict)
            assert 'address' in ip
            assert isinstance(ip['address'], str)
            assert 'netmask' in ip

# Generated at 2022-06-13 01:35:26.036133
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_default_interfaces():
    # setup test
    import tests.unittest_util
    testobj = tests.unittest_util.AnsibleTestObject(GenericBsdIfconfigNetwork())

    # set up for 4.4-RELEASE-p2
    testobj.module.run_command.return_value = (0, """add net default: gateway 10.0.2.2
add host ::1: gateway lo0
add host ::ffff:0.0.0.0: gateway lo0
add host 127.0.0.1: gateway lo0
add net ::ffff:0.0.0.0: gateway ::1
add net fe80::: gateway link#3
add net ff02::: gateway ::1
add net ff02::1: gateway ::1
""", None)

    # run the code to test
    testobj.network.get_default_

# Generated at 2022-06-13 01:35:33.098064
# Unit test for method parse_inet_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet_line():
    def test_parse_inet_line(line, expected):
        words = line.split()
        current_if = {}
        ips = dict(all_ipv4_addresses=[])
        network_facts = GenericBsdIfconfigNetwork()
        network_facts.parse_inet_line(words, current_if, ips)
        assert current_if['ipv4'] == expected

    # base case
    current_if = {'device': 'lo0', 'ipv4': [], 'ipv6': [], 'type': 'unknown'}
    ips = dict(all_ipv4_addresses=[])

# Generated at 2022-06-13 01:35:39.500803
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_default_interfaces():

    route_output = {
        'v4': """
        default via 192.168.122.1 dev eth0  proto static
        """,
        'v6': """
        default via fe80::5054:ff:fe75:c42b dev eth0  proto static
        """,
    }

    route_path = 'route'

    network_module = GenericBsdIfconfigNetwork()

    network_module.get_bin_path = MagicMock(return_value=route_path)

    network_module.run_command = MagicMock(side_effect=lambda args, **kwargs: (0, route_output[args[-1]], ''))

    interface = network_module.get_default_interfaces(route_path)


# Generated at 2022-06-13 01:36:22.977648
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_default_interfaces():
    """Test method get_default_interfaces of class GenericBsdIfconfigNetwork"""
    testobj = GenericBsdIfconfigNetwork(dict())
    sample_output_route_v4 = '''
default: default: gateway: 192.168.1.254 local addr: 192.168.1.104 refcnt: 1 usecnt: 1 type: netif expire: 0 flags: local'''
    sample_output_route_v6 = '''
default: default: gateway: fe80::1%lo0 local addr: fe80::25ee:d6ff:fef9:e6e9%lo0 refcnt: 1 usecnt: 1 type: netif expire: 0 flags: local'''

# Generated at 2022-06-13 01:36:30.609115
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():
    # arrange
    fake_module = FakeModule()
    fake_module.run_command = run_command_mock
    fake_module.get_bin_path = get_bin_path_mock
    fake_module.get_bin_path.side_effect = get_bin_path_side_effect
    fake_module.run_command.side_effect = run_command_side_effect
    fake_module.check_mode = False

    # act
    result = GenericBsdIfconfigNetwork(fake_module).populate()

    # assert

# Generated at 2022-06-13 01:36:33.196238
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():
    import pprint
    tmp = GenericBsdIfconfigNetwork()
    pprint.pprint(tmp.populate())

if __name__ == '__main__':
    test_GenericBsdIfconfigNetwork_populate()

# Generated at 2022-06-13 01:36:42.357629
# Unit test for method parse_inet_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet_line():
    gb = GenericBsdIfconfigNetwork()

    # test with valid input
    words = [
        "lo0:",
        "flags=8049<UP,LOOPBACK,RUNNING,MULTICAST>",
        "mtu", "33184",
        "inet", "127.0.0.1" ,"netmask", "0xff000000",
        "inet6", "::1", "prefixlen", "128",
        "inet6", "fe80::1%lo0", "prefixlen", "64",
        "scopeid", "0x1"
    ]
    current_if = gb.parse_interface_line(words[:4])
    assert current_if['device'] == 'lo0'

# Generated at 2022-06-13 01:36:46.824014
# Unit test for method get_interfaces_info of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_interfaces_info():
    module = AnsibleModule(argument_spec=dict())
    ifconfig_path = module.get_bin_path('ifconfig')
    ifconfig_options='-a'
    obj = GenericBsdIfconfigNetwork(module)
    interfaces, ips = obj.get_interfaces_info(ifconfig_path, ifconfig_options)
    return True


# Generated at 2022-06-13 01:36:53.148435
# Unit test for method parse_inet_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet_line():
    module = imp.new_module('test_module')
    c = GenericBsdIfconfigNetwork(module)
    current_if = {'device': 'test_device', 'ipv4': [], 'ipv6': [], 'type': 'unknown'}
    ps = c.parse_inet_line
    ips = dict(
        all_ipv4_addresses=[],
        all_ipv6_addresses=[],
    )
    assert c.get_options('<none>') == []

    out = ps(['inet', '127.0.0.1', 'netmask', '0xff000000'], current_if, ips)
    assert len(current_if['ipv4']) == 1
    assert len(ips['all_ipv4_addresses']) == 0


# Generated at 2022-06-13 01:37:01.507872
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_default_interfaces():
    import re
    ifconfig_path = module.get_bin_path('ifconfig')
    route_path = module.get_bin_path('route')
    network = GenericBsdIfconfigNetwork({}, ifconfig_path, route_path)
    result = network.get_default_interfaces(route_path)
    if result[0] == {}:
        print('not IPv4 default interface found!')
    else:
        print('IPv4 default interface: %s' % result[0]['interface'])
    if result[1] == {}:
        print('no IPv6 default interface found!')
    else:
        print('IPv6 default interface: %s' % result[1]['interface'])


# Generated at 2022-06-13 01:37:09.178072
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():
    for test_case in [('bsd_ifconfig_1.txt', 'bsd_route_1.txt')]:
        test_module = GenericBsdIfconfigNetwork(dict(module=AnsibleModuleMock(test_case)), platform='test')
        network_facts = test_module.populate()


# Generated at 2022-06-13 01:37:16.625349
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.network.common.utils import load_platform_subclass

    module = AnsibleModule(
        argument_spec=dict()
    )

    network = load_platform_subclass(GenericBsdIfconfigNetwork, module)()
    network.get_interfaces_info = lambda *args, **kwargs: ({}, {})
    network.get_default_interfaces = lambda *args, **kwargs: ({}, {})

    assert network.populate() == {}