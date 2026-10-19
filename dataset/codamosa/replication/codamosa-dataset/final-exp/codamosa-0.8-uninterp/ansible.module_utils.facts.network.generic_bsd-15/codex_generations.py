

# Generated at 2022-06-13 01:27:54.464565
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():
    # make a mock module
    module = MagicMock()

# Generated at 2022-06-13 01:28:07.748710
# Unit test for method get_interfaces_info of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_interfaces_info():
    gbifcn = GenericBsdIfconfigNetwork()
    ips = {'all_ipv4_addresses': [], 'all_ipv6_addresses': []}

# Generated at 2022-06-13 01:28:18.565664
# Unit test for method detect_type_media of class GenericBsdIfconfigNetwork

# Generated at 2022-06-13 01:28:30.317517
# Unit test for method get_interfaces_info of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_interfaces_info():
    _print_header('Testing GenericBsdIfconfigNetwork.get_interfaces_info')
    module = AnsibleModule(argument_spec={})
    module.params["rc"] = 0

# Generated at 2022-06-13 01:28:40.727971
# Unit test for method get_interfaces_info of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_interfaces_info():
    network = GenericBsdIfconfigNetwork()

    # Test ifconfig_lo_output
    ifconfig_lo_output = """
lo0: flags=8049<UP,LOOPBACK,RUNNING,MULTICAST> metric 0 mtu 16384
    options=1203<RXCSUM,TXCSUM,TXSTATUS,SW_TIMESTAMP>
    inet 127.0.0.1 netmask 0xff000000
    inet6 ::1 prefixlen 128
    inet6 fe80::1%lo0 prefixlen 64 scopeid 0x1
    nd6 options=201<PERFORMNUD,DAD>
    groups: lo
    status: active
"""
    interfaces, ips = network.get_interfaces_info('/sbin/ifconfig', '-a')

# Generated at 2022-06-13 01:28:52.791144
# Unit test for method parse_inet6_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet6_line():
    ifconfig_output = (
        'lo0: flags=8049<UP,LOOPBACK,RUNNING,MULTICAST> metric 0 mtu 33128\n'
        '        options=600003<RXCSUM,TXCSUM,RXCSUM_IPV6,TXCSUM_IPV6>\n'
        '        inet6 fe80::1%lo0 prefixlen 64 scopeid 0x3\n'
        '        inet6 ::1 prefixlen 128\n'
        '        inet 127.0.0.1 netmask 0xff000000\n'
        'gif0: flags=8010<POINTOPOINT,MULTICAST> metric 0 mtu 1280\n'
        'stf0: flags=0<> metric 0 mtu 1280\n'
        )
    network_

# Generated at 2022-06-13 01:29:00.783827
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():
    module = MockModule()
    n = GenericBsdIfconfigNetwork(module=module)

    def run_command(cmd, *args, **kwargs):
        output = ''

# Generated at 2022-06-13 01:29:07.511569
# Unit test for method parse_media_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_media_line():
    network_platform_module = GenericBsdIfconfigNetwork()
    iface = {}
    words = ['media:', 'Ethernet', 'autoselect', '(1000baseT)', 'status:', 'active']
    network_platform_module.parse_media_line(words, iface, None)
    assert iface == {'media': 'Ethernet', 'media_select': 'autoselect', 'media_type': '1000baseT', 'media_options': []}

# Generated at 2022-06-13 01:29:16.995524
# Unit test for method parse_interface_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_interface_line():
    bsd_ifconfig = GenericBsdIfconfigNetwork()


# Generated at 2022-06-13 01:29:25.077077
# Unit test for method get_options of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_options():
    ansible = AnsibleModule()
    m = GenericBsdIfconfigNetwork(ansible)

    assert m.get_options('foo<bar,baz,bleh>') == ['bar', 'baz', 'bleh']
    assert m.get_options('foo<bar>') == ['bar']
    assert m.get_options('foo<bar,baz,bleh') == []
    assert m.get_options('foo>') == []
    assert m.get_options('') == []
    assert m.get_options(None) == []


# Generated at 2022-06-13 01:29:46.090162
# Unit test for method parse_inet_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet_line():
    check = GenericBsdIfconfigNetwork()
    current_if = {}
    ips = dict(
        all_ipv4_addresses=[],
    )

    # ip address with cidr mask, netmask_length is 24, netmask is 255.255.255.0 (/24)
    words = 'inet 10.0.0.1/24'.split()
    check.parse_inet_line(words, current_if, ips)
    assert current_if['ipv4'][0]['netmask'] == '255.255.255.0'
    assert current_if['ipv4'][0]['network'] == '10.0.0.0'
    assert current_if['ipv4'][0]['broadcast'] == '10.0.0.255'

    # ip address with hex netmask

# Generated at 2022-06-13 01:29:54.033355
# Unit test for method parse_media_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_media_line():
    """ Test parse_media_line of class GenericBsdIfconfigNetwork """

    # Initialize the test environment
    variables = dict()
    module = AnsibleModule(argument_spec=variables)
    network = GenericBsdIfconfigNetwork(module)

    # Test parse_media_line with ifconfig output containing media line with 2 words
    words = ['media:', 'Ethernet', '10Gbase-CR', '10Gbase-CR']
    expected_value = dict()
    expected_value['media'] = words[1]
    expected_value['media_select'] = words[2]
    expected_value['media_type'] = words[3][1:]
    current_if = dict()
    ips = dict()
    network.parse_media_line(words, current_if, ips)

# Generated at 2022-06-13 01:30:04.420004
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():
    network_module = NetworkModule(argument_spec={}, check_invalid_arguments=False)
    if not HAS_SUBPROCESS:
        pytest.skip("missing required subprocess module")
    if not HAS_STRUCT:
        pytest.skip("missing required struct module")
    if not HAS_SOCKET:
        pytest.skip("missing required socket module")
    if not HAS_FCNTL:
        pytest.skip("missing required fcntl module")
    # not testing the module on a system without the route command
    if not network_module.get_bin_path('route'):
        pytest.skip("route command not found")
    if not network_module.get_bin_path('ifconfig'):
        pytest.skip("ifconfig command not found")
    facts = {}
    network_module

# Generated at 2022-06-13 01:30:16.415675
# Unit test for method parse_inet_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet_line():
    test_parsed_data_dict = {'broadcast': '255.255.255.255',
                             'address': '0.0.0.0',
                             'netmask': '0.0.0.0',
                             'network': '0.0.0.0'}

    test_line_dict = {'no_broadcast': ['inet', '0.0.0.0', 'netmask', '0.0.0.0'],
                      'no_netmask': ['inet', '0.0.0.0', 'broadcast', '255.255.255.255'],
                      'with_netmask': ['inet', '0.0.0.0', 'netmask', '0.0.0.0', 'broadcast', '255.255.255.255']}

# Generated at 2022-06-13 01:30:26.434859
# Unit test for method parse_inet6_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet6_line():
    iface = GenericBsdIfconfigNetwork()
    result1 = [{'address': '::1', 'prefix': '128', 'scope': '0x1'}]
    result2 = [{'address': 'fe80::1%lo0', 'prefix': '64', 'scope': '0x1'}]
    result3 = [{'address': 'fe80::11:22ff:fe33:4455%lo0', 'prefix': '64', 'scope': '0x1'}]
    result4 = [{'address': 'fe80::2f3a:6dff:fe1b:a7ac%lo0', 'prefix': '64', 'scope': '0x1'}]

# Generated at 2022-06-13 01:30:31.463437
# Unit test for method get_interfaces_info of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_interfaces_info():
    obj = GenericBsdIfconfigNetwork()
    ifconfig_path = '/sbin/ifconfig'
    ifconfig_options='-a'
    expected = "interfaces, ips = obj.get_interfaces_info(ifconfig_path, ifconfig_options='-a')"
    actual = "interfaces, ips = obj.get_interfaces_info(ifconfig_path, ifconfig_options)"
    assert str(expected) == str(actual)



# Generated at 2022-06-13 01:30:42.730954
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_default_interfaces():
    # valid_interfaces = [
    #         ['eth0', '192.168.0.1', '192.168.0.7'],
    #         ['eth1', '10.0.0.1', '10.0.0.7']
    # ]
    # invalid_interfaces = [
    #         'lo',
    #         'eth2',
    #         'eth3'
    # ]

    network = GenericBsdIfconfigNetwork()
    # TODO: How do we mock out module.run_command()?

    # # For each test case
    # for valid_interface in valid_interfaces:
    #     device, ip, gateway = valid_interface
    #     # For each address
    #     for address in [ip, gateway]:
    #         # When we call get_interfaces method
   

# Generated at 2022-06-13 01:30:53.493974
# Unit test for method detect_type_media of class GenericBsdIfconfigNetwork

# Generated at 2022-06-13 01:30:59.463178
# Unit test for method parse_media_line of class GenericBsdIfconfigNetwork

# Generated at 2022-06-13 01:31:07.059597
# Unit test for method detect_type_media of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_detect_type_media():
    network = GenericBsdIfconfigNetwork()


# Generated at 2022-06-13 01:31:26.047222
# Unit test for method parse_inet_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet_line():
    '''Test of parsing the inet info from ifconfig output'''

    class MockModule(object):
        '''Mocks the module object that is passed by Ansible'''
        def __init__(self, *args, **kwargs):
            self.params = kwargs
            self.return_values = []

        def run_command(self, cmd):
            return (0, self.params['output'], '')

    class C(GenericBsdIfconfigNetwork):
        '''Mocks the GenericBsdIfconfigNetwork class'''
        def __init__(self, *args, **kwargs):
            self.module = MockModule(*args, **kwargs)


# Generated at 2022-06-13 01:31:31.921254
# Unit test for method parse_media_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_media_line():
    """GenericBsdIfconfigNetwork: Test parsing media line from ifconfig"""

    # Setup
    module = None
    facts = {}
    ansible_host = None
    connection = Connection(ansible_host, module, facts)
    network = GenericBsdIfconfigNetwork(connection)
    current_if = {}
    ips = {}
    line = "media: Ethernet autoselect (100baseTX <full-duplex>)"
    words = line.split()

    # Execute
    network.parse_media_line(words, current_if, ips)

    # Verify
    assert current_if == {
        'media': 'Ethernet',
        'media_select': 'autoselect',
        'media_type': '100baseTX',
        'media_options': ['full-duplex']
    }


# Generated at 2022-06-13 01:31:43.112692
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_default_interfaces():
    ifconfig_route = "127.0.0.1 link#2 UH   1   0     lo0\n" \
                     "192.168.100.1   link#4  UH  8    en0\n" \
                     "fe80:1::1%lo0 link#2  UH  1     lo0"
    module = Mock(return_value=ifconfig_route)


# Generated at 2022-06-13 01:31:54.193303
# Unit test for method parse_inet_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet_line():
    mock_ifconfig_path = 'ifconfig'
    mock_ifconfig_options = '-a'
    mock_words = [
        "lo0:",
        "inet",
        "127.0.0.1",
        "netmask",
        "0xffffff00",
        "inet6",
        "fe80::1%lo0",
        "prefixlen",
        "64",
        "scopeid",
        "%lo0"
    ]
    mock_current_if = {
        "device": "lo0",
        "ipv4": [],
        "ipv6": [],
        "type": "unknown",
        "flags": [],
        "macaddress": "unknown",
        "mtu": "33184"
    }

# Generated at 2022-06-13 01:32:05.497696
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():
    # Create instance of the class under test
    network = GenericBsdIfconfigNetwork()
    
    # Create mock interfaces map
    interfaces = {
        'lo0' : {
            'device' : 'lo0',
            'flags' : ['LOOPBACK'],
            'ipv4': [{'address': '127.0.0.1', 'netmask': '255.0.0.0', 'broadcast': '0.0.0.0'}],
            'ipv6': [{'address': '::1'}],
            'macaddress': 'unknown',
            'metric': '1',
            'mtu': '33184',
            'type': 'loopback'
        }
    }
    
    # Create mock default ipv4 interface map

# Generated at 2022-06-13 01:32:09.728337
# Unit test for method get_interfaces_info of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_interfaces_info():
    generic_bsd_ifconfig_network = GenericBsdIfconfigNetwork()
    assert generic_bsd_ifconfig_network.get_interfaces_info(None) == ({}, {'all_ipv4_addresses': [], 'all_ipv6_addresses': []})



# Generated at 2022-06-13 01:32:18.632212
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():
    from ansible_collections.notstdlib.moveitallout.plugins.module_utils.network.common.utils import dict_merge
    from ansible_collections.notstdlib.moveitallout.plugins.module_utils.network.common.facts.network import NetworkCollector
    from ansible_collections.notstdlib.moveitallout.plugins.module_utils.network.common.facts.network import Network
    from ansible_collections.notstdlib.moveitallout.plugins.module_utils.network.common.facts.network import Interface
    from ansible_collections.notstdlib.moveitallout.plugins.module_utils.network.common.facts.network import IPv4

# Generated at 2022-06-13 01:32:30.899682
# Unit test for method parse_inet_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet_line():
    gb = GenericBsdIfconfigNetwork()
    # test a octet style ip address
    inet_string = "  inet 192.168.0.1 netmask 0xffffff00 broadcast 192.168.0.255"
    inet_words = inet_string.split()
    current_if = {'device': 'en0'}
    ips = dict()
    ips['all_ipv4_addresses'] = []
    gb.parse_inet_line(inet_words, current_if, ips)
    assert inet_words[1] == '192.168.0.1'
    assert current_if['ipv4'][0]['address'] == '192.168.0.1'
    assert len(current_if['ipv4']) == 1

# Generated at 2022-06-13 01:32:35.902529
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_default_interfaces():
    module = AnsibleModule(argument_spec={})
    network = GenericBsdIfconfigNetwork(module)
    defaults = network.get_default_interfaces(route_path=os.path.dirname(__file__) + "/files/route")
    assert defaults == ({'address': '192.168.0.12',
                         'gateway': '192.168.0.1',
                         'interface': 'en0'},
                        {'address': 'fe80::1%en0',
                         'gateway': 'fe80::1%en0',
                         'interface': 'en0'})


# Generated at 2022-06-13 01:32:43.091525
# Unit test for method get_interfaces_info of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_interfaces_info():
    module = Mock()
    gbi = GenericBsdIfconfigNetwork(module)
    assert module == gbi.module, 'Expected module ref to be set'
    # test case: no options set
    (interfaces, ips) = gbi.get_interfaces_info('/sbin/ifconfig')
    assert (interfaces,ips) == ({},{})
    # test case: loopback interface, no ipv6

# Generated at 2022-06-13 01:33:11.768456
# Unit test for method parse_media_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_media_line():
    module = AnsibleModule(argument_spec={})

    mock_parse_media_line = GenericBsdIfconfigNetwork()

    # test 1st option
    words = ['media:', 'Ethernet', '10Gbase-SR', 'media_type', '<full-duplex>']
    current_if = {
        'device': 'lo0',
        'ipv4': [],
        'ipv6': [],
        'type': 'unknown',
        'flags': [],
        'macaddress': 'unknown',
        'mtu': 33184,
        'metric': '',
        'options': [],
        'media': '',
        'media_select': '',
        'media_type': '',
        'media_options': [],
        'status': ''
    }

# Generated at 2022-06-13 01:33:16.434804
# Unit test for method get_interfaces_info of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_interfaces_info():
    module = AnsibleModule(
        argument_spec=dict()
    )

    module.run_command = MagicMock(return_value=(0, '', ''))
    module.get_bin_path = MagicMock(return_value=('/sbin/ifconfig', '/sbin/route'))
    module._socket = MagicMock()
    module.check_mode = False
    module.socket.has_ipv6 = MagicMock(return_value=True)

    obj = GenericBsdIfconfigNetwork(module)
    obj.populate()



# Generated at 2022-06-13 01:33:25.302284
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():
    defaults = {'interface': 'lo1'}
    ifinfo = {'lo1': {'ipv4': [{'address': '127.0.0.1'}]},'lo0': {'ipv4': [{'address': '127.0.0.2'}]}}
    ip_type = 'ipv4'
    expected_ipinfo = [{'address': '127.0.0.1'}]
    assert GenericBsdIfconfigNetwork.merge_default_interface(defaults, ifinfo, ip_type) == expected_ipinfo

# Generated at 2022-06-13 01:33:36.848416
# Unit test for method parse_inet6_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet6_line():
    # ------------------------------------------------------------------- #
    # Unit test setup
    # ------------------------------------------------------------------- #
    # Mock module class
    class MockAnsibleModule():
        def __init__(self):
            self.params = {}
        def get_bin_path(self, executable):
            return '/path/to/bin'
        def run_command(self, command):
            return 0, '', ''
        def fail_json(self, *args, **kwargs):
            raise Exception(str(args))

    # Mock parser class
    class MockGenericBsdIfconfigNetwork(GenericBsdIfconfigNetwork):
        def __init__(self, module):
            pass

    module = MockAnsibleModule()
    module.params = {'gather_subset': ['!all']}

# Generated at 2022-06-13 01:33:46.985848
# Unit test for method parse_inet6_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet6_line():
    p=GenericBsdIfconfigNetwork()
    # ne, prefixlen 64  scopeid 0x20<link>
    # fe80::224:dfff:fe98:3f3b%vlan0 prefixlen 64 scopeid 0x2 
    # test address and prefix
    words = "fe80::224:dfff:fe98:3f3b/64".split()
    ipv6_address={}
    p.parse_inet6_line(words, {}, {'all_ipv6_addresses':[]})
    assert(ipv6_address['address'] == 'fe80::224:dfff:fe98:3f3b')
    assert(ipv6_address['prefix'] == '64')
    
    

# Generated at 2022-06-13 01:33:55.412572
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():
    module = AnsibleModule(
        argument_spec={},
        supports_check_mode=True
    )
    try:
        from ansible_collections.notstdlib.moveitallout.tests.unit.compat import unittest
        from ansible_collections.notstdlib.moveitallout.tests.unit.compat.mock import create_autospec, patch
        from ansible_collections.notstdlib.moveitallout.plugins.module_utils import basic
        from ansible_collections.notstdlib.moveitallout.plugins.module_utils.network.common.utils import dict_merge

        has_import_error = False
    except ImportError:
        has_import_error = True
        unittest = None

    # If the above import failed, try to load the python3 Comp

# Generated at 2022-06-13 01:34:01.289658
# Unit test for method get_options of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_options():
    net = GenericBsdIfconfigNetwork()

    assert net.get_options('<UP,BROADCAST,RUNNING>') == ['UP', 'BROADCAST', 'RUNNING']
    assert net.get_options('<>') == []
    assert net.get_options('') == []
    assert net.get_options('FOOBAR') == []


# Generated at 2022-06-13 01:34:09.724498
# Unit test for method parse_inet6_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet6_line():
    module = AnsibleModule(argument_spec={})
    module.run_command = MagicMock(return_value=(0, '', ''))
    # this is the real thing
    generic_bsd_ifconfig_network = GenericBsdIfconfigNetwork(module)

    words = ['inet6', 'fe80::1%lo0', 'prefixlen', '64', 'scopeid', '0x1']
    current_if = {'ipv6': []}
    ips = dict(
        all_ipv6_addresses=[],
    )
    generic_bsd_ifconfig_network.parse_inet6_line(words, current_if, ips)

# Generated at 2022-06-13 01:34:16.127212
# Unit test for method parse_media_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_media_line():
    module = AnsibleModule(
        argument_spec = dict(
            interfaces = dict(type='any'),
        ),
        supports_check_mode=False,
    )

    module.run_command = MagicMock(return_value=(0, 'output', ''))
    set_module_args(dict(
        interfaces=dict(
            type='any',
        ),
    ))

    # The code to be tested
    from ansible_collections.community.general.plugins.modules.remote_management.network import GenericBsdIfconfigNetwork
    network = GenericBsdIfconfigNetwork(module)
    network.detect_type_media = MagicMock()
    network.get_default_interfaces = MagicMock()

# Generated at 2022-06-13 01:34:25.084452
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_default_interfaces():
    print("Test method get_default_interfaces of class GenericBsdIfconfigNetwork")
    # Setup
    test_module = AnsibleModule(argument_spec={})
    test_network = GenericBsdIfconfigNetwork(module=test_module)
    test_route_path = '/usr/sbin/route'

# Generated at 2022-06-13 01:34:50.386743
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_default_interfaces():
    pytest.debug_func()
    ipv4default_test_1 = "route -n get default"
    ipv6default_test_1 = "route -n get -inet6 default"

# Generated at 2022-06-13 01:34:56.179266
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_default_interfaces():
    class TestModule:
        def __init__(self, rc = 0, stdout = "", stderr = ""):
            self.run_command_rc = rc
            self.run_command_stdout = stdout
            self.run_command_stderr = stderr
        def run_command(self, command_args, check_rc=True):
            return self.run_command_rc, self.run_command_stdout, self.run_command_stderr
    #
    # Test case 1:
    # - output from route shows different defaults for IPv4 and IPv6
    #
    module = TestModule()

# Generated at 2022-06-13 01:35:02.832718
# Unit test for method parse_inet_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet_line():
    generic_bsd_ifconfig_network = GenericBsdIfconfigNetwork()

    # Test case 1
    current_if = {'ipv4' : list()}
    ips = {'all_ipv4_addresses' : list()}
    words = ['inet', '192.168.0.1', 'netmask', '255.255.255.0', 'broadcast', '192.168.0.255']
    generic_bsd_ifconfig_network.parse_inet_line(words, current_if, ips)
    assert current_if == {'ipv4': [{'netmask': '255.255.255.0', 'broadcast': '192.168.0.255', 'address': '192.168.0.1', 'network': '192.168.0.0'}]}

# Generated at 2022-06-13 01:35:12.312823
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():
    test_module = NetworkModule(argument_spec={},
                                supports_check_mode=True)

    def route_side_effect(*args, **kwargs):
        return 0, '', ''


# Generated at 2022-06-13 01:35:19.048138
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():
    interfaces = dict(
        lo0=dict(flags=['LOOPBACK']),
        bge0=dict(flags=['BROADCAST', 'SMART'], ipv4=[dict(address='192.168.4.4')]),
    )
    network = GenericBsdIfconfigNetwork()
    network.merge_default_interface(dict(interface='lo0'), interfaces, 'ipv4')
    assert (interfaces['lo0']['flags'] == ['LOOPBACK'])

    network.merge_default_interface(dict(interface='bge0', address='192.168.4.4'), interfaces, 'ipv4')
    assert (interfaces['bge0']['flags'] == ['BROADCAST', 'SMART'])



# Generated at 2022-06-13 01:35:28.545461
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():
    parser = GenericBsdIfconfigNetwork()
    # test darwin
    module = MagicMock(name='module')

# Generated at 2022-06-13 01:35:35.968435
# Unit test for method get_interfaces_info of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_interfaces_info():
    ifconfig_path = '/sbin/ifconfig'
    module = AnsibleModule(argument_spec={})
    network = GenericBsdIfconfigNetwork(module)
    ifconfig_options='-a'
    interfaces, ips = network.get_interfaces_info(ifconfig_path, ifconfig_options)

# Generated at 2022-06-13 01:35:40.620126
# Unit test for method detect_type_media of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_detect_type_media():
    my_obj = GenericBsdIfconfigNetwork()
    my_obj.interfaces_d = {'en0':{'media':'Ether', 'type':'unknown'}}
    my_obj.detect_type_media(my_obj.interfaces_d)
    assert my_obj.interfaces_d['en0']['type'] == 'ether'


# Generated at 2022-06-13 01:35:46.725716
# Unit test for method parse_media_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_media_line():
    network = GenericBsdIfconfigNetwork()
    iface = {}
    ips = {}
    words = 'media: Ethernet autoselect (1000baseT full-duplex)'.split(' ')
    network.parse_media_line(words, iface, ips)
    assert iface['media'] == 'Ethernet'
    assert iface['media_select'] == 'autoselect'
    assert iface['media_type'] == '(1000baseT'
    assert iface['media_options'] == 'full-duplex)'



# Generated at 2022-06-13 01:35:53.262537
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():
    net = GenericBsdIfconfigNetwork()

    defaults = {}
    net.merge_default_interface(defaults, {}, 'ipv4')
    assert defaults == {}, defaults

    defaults = {'interface': 'foo'}
    net.merge_default_interface(defaults, {}, 'ipv4')
    assert defaults == {'interface': 'foo'}, defaults

    defaults = {'interface': 'foo'}
    net.merge_default_interface(defaults, {'foo': {'bar': 'baz'}}, 'ipv4')
    assert defaults == {'interface': 'foo', 'bar': 'baz'}, defaults

    defaults = {'interface': 'foo'}