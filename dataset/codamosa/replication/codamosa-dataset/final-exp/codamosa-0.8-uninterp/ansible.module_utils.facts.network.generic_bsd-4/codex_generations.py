

# Generated at 2022-06-13 01:27:57.940650
# Unit test for method parse_media_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_media_line():

    # Testing of parse_media_line from class GenericBsdIfconfigNetwork
    # Test Case 1 - test with input values
    if1 = GenericBsdIfconfigNetwork()
    current_if = {}
    words = ['media:', 'Ethernet', 'autoselect', '(none)']
    if1.parse_media_line(words, current_if, {})
    assert current_if == {'media': 'Ethernet', 'media_select': 'autoselect', 'media_type': '(none)'}

    # Test Case 2 - test with input values
    if1 = GenericBsdIfconfigNetwork()
    current_if = {}
    words = ['media:', 'Ethernet', 'autoselect', '(none)', 'status:', 'inactive']

# Generated at 2022-06-13 01:28:07.200339
# Unit test for method get_options of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_options():
    r = GenericBsdIfconfigNetwork()
    options = r.get_options('name nospace')
    assert options == []
    options = r.get_options('name <none>')
    assert options == []
    options = r.get_options('name <>')
    assert options == []
    options = r.get_options('name <a,b>')
    assert options == ['a','b']
    options = r.get_options('name <a,b> more')
    assert options == ['a','b']
    options = r.get_options('name <a,b,c,d> more')
    assert options == ['a','b','c','d']


# Generated at 2022-06-13 01:28:12.293449
# Unit test for method parse_media_line of class GenericBsdIfconfigNetwork

# Generated at 2022-06-13 01:28:18.022118
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():
    module_name = 'Network'

    test_module = AnsibleModule(argument_spec=dict(
        gather_subset=dict(default=['!all'], type='list'),
        fact_path=dict(default=None, type='path')))

    mock_ansible_module = Mock(name='ansible_module')
    mock_ansible_module.params = {}
    mock_ansible_module.run_command.return_value = (
        0,
        'ether 8:0:27:8e:ba:f1  media: Ethernet autoselect (1000baseT <full-duplex>)',
        '')

    mock_get_bin_path = MagicMock(name='get_bin_path')
    mock_get_bin_path.return_value = '/sbin/ifconfig'

    mock_

# Generated at 2022-06-13 01:28:24.797517
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():
    host_vars = {
        'ansible_hostname': 'hostname1',
        'ansible_ssh_host': '0.0.0.0',
        'ansible_ssh_pass': 'passwd123',
        'ansible_become_pass': 'passwd123',
        'ansible_connection': 'ssh',
        'ansible_python_interpreter': 'python'
    }

    module = FakeAnsibleModule(
        argument_spec=dict(),
        host_vars=host_vars
    )
    
    bsd_network = GenericBsdIfconfigNetwork(module)

# Generated at 2022-06-13 01:28:32.421006
# Unit test for method get_options of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_options():
    network = GenericBsdIfconfigNetwork()
    option_string = 'flags=<UP,LOOPBACK,RUNNING>'
    assert network.get_options(option_string) == ['UP', 'LOOPBACK', 'RUNNING']

    option_string = 'flags=<UP,LOOPBACK,,>'
    assert network.get_options(option_string) == ['UP', 'LOOPBACK', '']

    option_string = 'options=<LOOPBACK>'
    assert network.get_options(option_string) == ['LOOPBACK']

    option_string = 'LOOPBACK'
    assert network.get_options(option_string) == []


# Generated at 2022-06-13 01:28:35.622511
# Unit test for method get_options of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_options():
    assert GenericBsdIfconfigNetwork().get_options('foo<UP,LOOPBACK,RUNNING,MULTICAST>') == ['UP', 'LOOPBACK', 'RUNNING', 'MULTICAST']



# Generated at 2022-06-13 01:28:47.985231
# Unit test for method parse_inet6_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet6_line():
    iface = GenericBsdIfconfigNetwork()
    line = "inet6 fe80::250:56ff:fe92:66c8%bge0 prefixlen 64 scopeid 0x3"
    words = line.split()
    current_if = {'ipv6': []}
    ips = dict(all_ipv6_addresses=[])
    iface.parse_inet6_line(words, current_if, ips)
    assert current_if == {
        'ipv6': [
            {'address': 'fe80::250:56ff:fe92:66c8', 'prefix': '64', 'scope': '0x3'}
        ]
    }
    assert ips == {'all_ipv6_addresses': ['fe80::250:56ff:fe92:66c8']}



# Generated at 2022-06-13 01:28:58.045510
# Unit test for method parse_media_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_media_line():
    from ansible_collections.ansible.netcommon.tests.unit.compat.mock import Mock
    from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.network import NetworkBase
    from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.module_utils.network import NetworkModule
    module = Mock(name='module',
                  spec=NetworkModule,
                  run_command=Mock(return_value=0),
                  check_mode=False)

    base_iface = {
        'device': 'lo0',
        'ipv4': [],
        'ipv6': [],
        'type': 'unknown',
        'mtu': '33184',
        'macaddress': 'unknown',
        'flags': [],
    }

# Generated at 2022-06-13 01:29:08.876120
# Unit test for method parse_inet6_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet6_line():
    data_in = ['inet6', 'fe80::5054:ff:fe5b:d8ba%lo0', 'prefixlen', '64', 'scopeid', '0x3']
    data_exp = {'address': 'fe80::5054:ff:fe5b:d8ba', 'prefix': '64', 'scope': '0x3'}
    data_act = {'address': '', 'prefix': '', 'scope': ''}
    module = mock.MagicMock()
    platform = 'Generic_BSD_Ifconfig'
    obj = GenericBsdIfconfigNetwork(module)
    obj.parse_inet6_line(data_in, {}, {})
    actual = obj.parse_inet6_line(data_in, {}, {})
    assert data_exp == actual

# Generated at 2022-06-13 01:29:28.148132
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():
    module = AnsibleModule(
        argument_spec=dict()
    )
    set_module_args(module, dict(
        _ansible_check_mode=False,
        _ansible_diff=False,
        _ansible_keep_remote_files=False,
    ))
    module.check_mode = False
    result = GenericBsdIfconfigNetwork(module).populate()
    assert isinstance(result, dict)
    assert 'interfaces' in result
    assert 'all_ipv4_addresses' in result
    assert 'all_ipv6_addresses' in result
    assert 'default_ipv4' in result
    assert 'default_ipv6' in result
    assert 'all_ipv4_addresses' in result
    assert 'all_ipv6_addresses' in result



# Generated at 2022-06-13 01:29:40.426999
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():
    # This is a generated test to see if the method populate generates the correct data
    # The method currently fails...
    fake = FakedGenericBsdIfconfigNetworkClass()
    fact_data = "ifconfig"

# Generated at 2022-06-13 01:29:50.721385
# Unit test for method parse_inet6_line of class GenericBsdIfconfigNetwork

# Generated at 2022-06-13 01:30:01.518388
# Unit test for method parse_inet6_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet6_line():
    module = AnsibleModule(argument_spec={})
    # noinspection PyProtectedMember
    network = GenericBsdIfconfigNetwork(module)

    # Test line with scope, prefixlen
    test_line = ['inet6', 'fe80::1%lo0', 'prefixlen', '64', 'scopeid', '0x4']
    iface = dict()
    result = dict()
    network._parse_inet6_line(test_line, iface, result)
    assert iface['ipv6'][0]['address'] == 'fe80::1%lo0'
    assert iface['ipv6'][0]['prefix'] == '64'
    assert iface['ipv6'][0]['scope'] == '0x4'

    # Test line with prefixlen, scope
    iface = dict()


# Generated at 2022-06-13 01:30:06.839542
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():
    # Tests for GenericBsdIfconfigNetwork.merge_default_interface

    # Ensures that the method works as expected when the default interface
    # is in the interfaces dictionary.
    def_if = 'eth0'
    interfaces = {def_if: {'ipv4': [{'address': '10.0.0.1', 'broadcast': '10.0.0.255', 'netmask': '255.0.0.0', 'network': '10.0.0.0'}], 'ipv6': [], 'type': 'unknown', 'mtu': '1500', 'device': 'eth0', 'flags': ['BROADCAST', 'MULTICAST']}}
    defaults = {'gateway': '10.0.0.1', 'interface': def_if}

    def_copy = defaults.copy()
   

# Generated at 2022-06-13 01:30:09.419558
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_default_interfaces():
    assert GenericBsdIfconfigNetwork.get_default_interfaces('/route', "/dev/null") == ({}, {})



# Generated at 2022-06-13 01:30:19.926668
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():
    defaults = dict(
        interface='lo0',
        address='127.0.0.1'
    )
    ifinfo = dict(
        lo0=dict(
            ipv4=[
                dict(
                    address='127.0.1.1',
                    netmask='255.255.255.0',
                    broadcast='NONE'
                ),
                dict(
                    address='127.0.0.1',
                    netmask='255.255.255.0',
                    broadcast='NONE'
                )
            ]
        )
    )

    interfaces = dict()
    interfaces['lo0'] = ifinfo['lo0']
    ip_type = 'ipv4'

    result = GenericBsdIfconfigNetwork.merge_default_interface(defaults, interfaces, ip_type)
    assert result is None



# Generated at 2022-06-13 01:30:28.682689
# Unit test for method parse_media_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_media_line():
    from ansible_collections.community.network.tests.unit.compat.mock import MagicMock
    from ansible_collections.community.network.tests.unit.compat.mock import patch
    from ansible_collections.community.network.plugins.modules import network_faqs

    class TestGenericBsdIfconfigNetwork(GenericBsdIfconfigNetwork):
        ''' Ansible subclass module for testing parse_media_line method '''

        def __init__(self, module):
            super(TestGenericBsdIfconfigNetwork, self).__init__(module)

        def parse_media_line(self, words, current_if, ips):
            ''' override the parse_media_line method '''
            # we can not test the second argument, so we use two mock objects
            current_if = MagicMock()


# Generated at 2022-06-13 01:30:34.914784
# Unit test for method get_options of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_options():
    # Create an instance of class GenericBsdIfconfigNetwork
    foo = GenericBsdIfconfigNetwork()

    # Test case 1
    assert foo.get_options('foo <bar,baz>') == ['bar', 'baz']

    # Test case 2
    assert foo.get_options('foo <>') == []

    # Test case 3
    assert foo.get_options('foo') == []

    # Test case 4
    assert foo.get_options('foo <bar') == []

    # Test case 5
    assert foo.get_options('foo bar>') == []


# Generated at 2022-06-13 01:30:46.549842
# Unit test for method get_interfaces_info of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_interfaces_info():
    module = AnsibleModule({})

    network = GenericBsdIfconfigNetwork(module)

    # FreeBSD netif.c does not add the -a flag if not specified
    val = network.get_interfaces_info('/sbin/ifconfig', '-a')
    assert val

    # DragonflyBSD netif.c does not add the -a flag if not specified
    val = network.get_interfaces_info('/sbin/ifconfig', '-a')
    assert val

    # NetBSD netif.c does not add the -a flag if not specified
    val = network.get_interfaces_info('/sbin/ifconfig', '-a')
    assert val

    # OpenBSD netif.c does not add the -a flag if not specified

# Generated at 2022-06-13 01:31:12.087214
# Unit test for method detect_type_media of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_detect_type_media():
    network_module = GenericBsdIfconfigNetwork()

    interfaces = {'eth0': {'device': 'eth0', 'ipv4': [], 'ipv6': [], 'type': 'unknown',
                           'flags': ['BROADCAST', 'SIMPLEX', 'RUNNING', 'MULTICAST', 'LINK0'],
                           'macaddress': 'unknown', 'metric': '0', 'mtu': '1500'},
                  'lo': {'device': 'lo', 'ipv4': [], 'ipv6': [], 'type': 'loopback',
                         'flags': ['LOOPBACK', 'RUNNING', 'MULTICAST'],
                         'macaddress': 'unknown', 'metric': '0', 'mtu': '33184'}}

    new_interfaces = network_module.det

# Generated at 2022-06-13 01:31:22.808526
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_default_interfaces():
    from ansible.module_utils.network.common.utils import load_platform_subclass

    platform_class = load_platform_subclass(GenericBsdIfconfigNetwork)
    network_module = platform_class()
    network_module.module.fail_json = lambda *args, **kwargs: None

# Generated at 2022-06-13 01:31:28.904157
# Unit test for method parse_media_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_media_line():
    class ModuleStub(object):
        pass

    module = ModuleStub()
    loader = collections.namedtuple('Loader', ['path', 'name'])
    module.loader = loader(path='/usr/local/bin', name='bsd')

    class ModuleUtilsStub(object):
        def get_bin_path(self, name):
            if name in ('route', 'ifconfig'):
                return '/sbin/' + name
            else:
                return None

    module.module_utils = ModuleUtilsStub()

    class AnsibleModuleStub(object):
        def __init__(self, *args, **kwargs):
            self.params = kwargs

        def run_command(self, args):
            return 0, '', ''


# Generated at 2022-06-13 01:31:38.328121
# Unit test for method parse_media_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_media_line():
    """
    Test parse_media_line()
    """
    n = GenericBsdIfconfigNetwork()
    test_words = ["media:", "Ethernet", "10Gbase-T", "(10Gbase-T/IEEE", "802.3an)"]

    # call the function
    n.parse_media_line(test_words, None, None)

    assert test_words[1] == "Ethernet"
    assert test_words[2] == "10Gbase-T"
    assert test_words[3] == "(10Gbase-T/IEEE"
    assert test_words[4] == "802.3an)"



# Generated at 2022-06-13 01:31:43.984059
# Unit test for method get_interfaces_info of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_interfaces_info():
    module = AnsibleModule(argument_spec={})

    # test with linux interface data file
    test_data = read_fixture_file(['generic_bsd_ifconfig', 'example1_ifconfig.txt'])
    network = GenericBsdIfconfigNetwork(module)
    interfaces, ips = network.get_interfaces_info(ifconfig_path='/bin/echo', ifconfig_options='-a')

# Generated at 2022-06-13 01:31:55.199682
# Unit test for method populate of class GenericBsdIfconfigNetwork

# Generated at 2022-06-13 01:32:06.817629
# Unit test for method parse_inet6_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet6_line():
    current_if = {'ipv6': []}
    ips = dict(
        all_ipv6_addresses=[],
    )
    my_test = GenericBsdIfconfigNetwork()
    # test for address and prefix
    line = "fe80::a00:27ff:fe07:7bae%e1000g0 prefixlen 64 scopeid 0x6"
    tokens = re.split("\s+", line)
    my_test.parse_inet6_line(tokens, current_if, ips)
    assert current_if['ipv6'][0]['address'] == 'fe80::a00:27ff:fe07:7bae%e1000g0'
    assert current_if['ipv6'][0]['prefix'] == '64'
    assert 'scope' not in current_

# Generated at 2022-06-13 01:32:16.105446
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_default_interfaces():
        test_GenericBsdIfconfigNetwork = GenericBsdIfconfigNetwork()
        route_path = "route"
        test_GenericBsdIfconfigNetwork.module.run_command = MagicMock(return_value=(0,"", ""))
        assert test_GenericBsdIfconfigNetwork.get_default_interfaces(route_path) == ({},{})
        test_GenericBsdIfconfigNetwork.module.run_command = MagicMock(return_value=(0,"interface: en0\n\rgateway: 10.0.2.2\n\r", ""))
        assert test_GenericBsdIfconfigNetwork.get_default_interfaces(route_path) == ({'interface': 'en0', 'gateway': '10.0.2.2'},{})


# Generated at 2022-06-13 01:32:24.085902
# Unit test for method parse_inet_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet_line():
    iface = GenericBsdIfconfigNetwork()
    words = ['lo0',
             'inet',
             '127.0.0.1',
             'netmask',
             '0xff000000']
    current_if = {'device': 'lo0', 'ipv4': [], 'ipv6': [], 'type': 'unknown'}
    ips = dict(
        all_ipv4_addresses=[],
        all_ipv6_addresses=[],
    )
    iface.parse_inet_line(words, current_if, ips)
    assert len(current_if['ipv4']) == 1
    assert current_if['ipv4'][0]['address'] == '127.0.0.1'

# Generated at 2022-06-13 01:32:30.599189
# Unit test for method parse_inet_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet_line():
    """Testing parse_inet_line"""
    # Test input word list

# Generated at 2022-06-13 01:33:11.858981
# Unit test for method parse_inet6_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet6_line():
    # Setup variables used in tests
    module_class = 'network'
    module_name = 'ansible.modules.network.%s' % module_class
    module_path = os.path.join(FUTURE_DIR, '%s.py' % module_class)
    module_args = dict()
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_text

    network_module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    module = GenericBsdIfconfigNetwork(network_module)
    test_object = GenericBsdIfconfigNetwork.parse_inet6_line


# Generated at 2022-06-13 01:33:23.444313
# Unit test for method populate of class GenericBsdIfconfigNetwork

# Generated at 2022-06-13 01:33:35.411944
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_default_interfaces():
    content_route_n_get_default = '''
    default
        gateway 192.168.1.1
    default
        gateway 192.168.1.1
        if address 192.168.1.1
        local addr 192.168.1.1
    '''
    content_route_n_get_inet6_default = '''
    default
        gateway fe80::21e:52ff:fe74:c88f
    '''
    module = MockModule()
    module.run_command = Mock(return_value=(0, content_route_n_get_default, ''))
    network = GenericBsdIfconfigNetwork(module)
    interface_v4, interface_v6 = network.get_default_interfaces('route')
    assert interface_v4['gateway'] == '192.168.1.1'

# Generated at 2022-06-13 01:33:41.523886
# Unit test for method get_interfaces_info of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_interfaces_info():
    module = AnsibleModule(argument_spec={})

    ifconfig_path = module.get_bin_path('ifconfig')
    ifconfig_options = module.params['options']

    obj = GenericBsdIfconfigNetwork(module)
    interfaces, ips = obj.get_interfaces_info(ifconfig_path, ifconfig_options=ifconfig_options)
    assert type(interfaces) is dict
    assert type(ips) is dict
    for interface in interfaces:
        assert type(interfaces[interface]) is dict
    for key in ips:
        assert type(ips[key]) is list



# Generated at 2022-06-13 01:33:50.503313
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_default_interfaces():
    # test cases:
    #  * OpenBSD route show default6
    #  * FreeBSD route get default
    #  * MacOSX/FreeBSD route get -inet6 default
    #  * NetBSD route get default
    #  * NetBSD route get -inet6 default

    def test(module_mock, module_args, result):
        def ifconfig_path_side_effect(arg):
            if arg == 'route':
                return '/sbin/route'
        module_mock.get_bin_path.side_effect = ifconfig_path_side_effect
        module_mock.run_command.return_value = (0, module_args, '')
        platform = GenericBsdIfconfigNetwork()
        assert platform.get_default_interfaces('/sbin/route') == result


# Generated at 2022-06-13 01:33:57.853529
# Unit test for method parse_inet6_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet6_line():
    '''
    Unit test for method parse_inet6_line of class GenericBsdIfconfigNetwork
    '''
    module = AnsibleModule(argument_spec={})
    module = mock.MagicMock(name='AnsibleModule')
    module._socket_path = 'test'
    module.run_command.return_value = 3
    module.get_bin_path.return_value = 'test'

    gbi = GenericBsdIfconfigNetwork(module)
    address = {'address': '2001:db8:1::1/64'}
    current_if = {'ipv6': []}
    ips = {'all_ipv6_addresses': []}

# Generated at 2022-06-13 01:34:07.576816
# Unit test for method parse_interface_line of class GenericBsdIfconfigNetwork

# Generated at 2022-06-13 01:34:17.229703
# Unit test for method get_options of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_options():
    # setup test object
    c = GenericBsdIfconfigNetwork()
    # test
    # no options
    assert c.get_options('stuff') == []
    # one option
    assert c.get_options('<UP>') == ['UP']
    # multiple options
    assert c.get_options('<UP,MULTICAST,RUNNING>') == ['UP', 'MULTICAST', 'RUNNING']
    # option with spaces
    assert c.get_options('<UP,MULTICAST,RUNNING,some stuff>') == ['UP', 'MULTICAST', 'RUNNING', 'some stuff']


# Generated at 2022-06-13 01:34:24.113202
# Unit test for method get_options of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_options():
    network_module = NetworkModule(argument_spec=dict())
    ifconfig_path = network_module.get_bin_path('ifconfig')
    if not ifconfig_path:
        skip_msg = "ifconfig not found in PATH"
        raise SkipTest(skip_msg)
    gbni = GenericBsdIfconfigNetwork(network_module)
    options_string = "options=<foo,bar,baz,quux>"
    option_list = gbni.get_options(options_string)
    assert option_list == ['foo', 'bar', 'baz', 'quux']


# Generated at 2022-06-13 01:34:34.893333
# Unit test for method parse_inet6_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet6_line():
    network = GenericBsdIfconfigNetwork()

    words = ["inet6", "1000:0000:0000:0000:0000:0000:0000:0100", "prefixlen", "64", "scopeid", "0x0"]
    iface = {
        "device": "test0",
        "ipv4": [],
        "ipv6": [],
        "type": "unknown",
        "flags": [],
        "macaddress": "unknown",
        "mtu": "1500"
    }

    ips = {
        "all_ipv4_addresses": [],
        "all_ipv6_addresses": []
    }

    network.parse_inet6_line(words, iface, ips)

# Generated at 2022-06-13 01:34:56.137499
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_default_interfaces():
    
    # Mock class for route_path argument of GenericBsdIfconfigNetwork.get_default_interfaces
    # Acts like a file handle, but returns the mock_route_output when read
    class mock_route_file_handle(object):
        def __init__(self, mock_route_output, module=None):
            self.mock_route_output = mock_route_output

        # Read function
        def read(self):
            return self.mock_route_output
        
        # Write function
        def write(self, stuff):
            pass

        # Close function
        def close(self):
            pass

    # Mock return value for module.run_command
    class mock_module_run_command(object):
        def __init__(self, rc, out, err):
            self.rc = rc
            self

# Generated at 2022-06-13 01:35:05.959158
# Unit test for method parse_media_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_media_line():
    module = MagicMock()
    cmd = 'ifconfig -e'
    rc = 0

# Generated at 2022-06-13 01:35:15.147703
# Unit test for method get_interfaces_info of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_interfaces_info():
    # read sample data file
    with open('../lib/ansible/module_utils/network/common/test/unit/data/bsd_ifconfig_data') as f:
        testdata = f.read()

    # build fake module class for unit testing
    class FakeModule:
        def __init__(self):
            self.name = 'test_module'
        def get_bin_path(self, name, opt_dirs=[]):
            return '/sbin/'+name
        def run_command(self, args):
            return (0, testdata, "")

    module = FakeModule()

    # check parameters of the returned result
    network_module = GenericBsdIfconfigNetwork(module)
    result = network_module.get_interfaces_info('ifconfig', '-a')
    # test for the presence

# Generated at 2022-06-13 01:35:25.341004
# Unit test for method parse_media_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_media_line():
    iface = {'device': 'enp0s3', 'type': 'unknown', 'media': '1000baseTX', 'media_select': 'autoselect', 'media_type': '<full-duplex>', 'media_options': None}
    line = ['media:', '1000baseTX', 'autoselect', '<full-duplex>']
    networkfact = GenericBsdIfconfigNetwork()
    networkfact.parse_media_line(line, iface, None)
    assert iface == {'device': 'enp0s3', 'type': 'unknown', 'media': '1000baseTX', 'media_select': 'autoselect', 'media_type': '<full-duplex>', 'media_options': None}


# Generated at 2022-06-13 01:35:32.160514
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_default_interfaces():
    gbin = GenericBsdIfconfigNetwork()
    gbin.module = mock.MagicMock()
    gbin.module.run_command.return_value = 0, 'default 172.16.1.1: gateway 192.168.1.1', ''
    gbin.module.get_bin_path.return_value = '/sbin/route'
    assert gbin.get_default_interfaces('/sbin/route') == ({'interface': '172.16.1.1', 'gateway': '192.168.1.1'}, {})
    gbin.module.run_command.assert_called_with(['/sbin/route', '-n', 'get', '/sbin/route'])


# Generated at 2022-06-13 01:35:42.251931
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():
    expected_result = {'interface': 'lo0', 'device': 'lo0', 'ipv4': [{'netmask': 'ffffffff', 'address': '127.0.0.1', 'broadcast': '127.255.255.255', 'network': '127.0.0.0'}], 'ipv6': [{'prefix': '128', 'address': '::1'}, {'prefix': '16', 'scope': '10', 'address': 'fe80::1%lo0'}], 'macaddress': '00:00:00:00:00:00', 'flags': ['UP', 'LOOPBACK', 'RUNNING'], 'type': 'loopback', 'mtu': '65536'}
    network = GenericBsdIfconfigNetwork()

# Generated at 2022-06-13 01:35:50.268216
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():
    ifconfig_network = GenericBsdIfconfigNetwork({})
    interfaces = {
        'lo0': {'ipv4': [{'address': '10.0.0.1'}]},
    }
    interface = {}
    ifconfig_network.merge_default_interface(interface, interfaces, 'ipv4')
    assert interface == {}
    interface = {'interface': 'lo0'}
    ifconfig_network.merge_default_interface(interface, interfaces, 'ipv4')
    assert interface == {'interface': 'lo0', 'ipv4': [{'address': '10.0.0.1'}]}
    interface = {'interface': 'lo0', 'address': '10.0.0.2'}

# Generated at 2022-06-13 01:35:56.332207
# Unit test for method get_interfaces_info of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_interfaces_info():
    """unit test for method get_interfaces_info"""

    test_module = Mock(spec_set=dict(
        run_command=Mock(return_value=[0, '', '']),
        get_bin_path=Mock(return_value='/sbin/ifconfig')
    ))
    test_generic_bsd_ifconfig_network = GenericBsdIfconfigNetwork(test_module)


# Generated at 2022-06-13 01:36:06.210279
# Unit test for method parse_inet6_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet6_line():
    obj = GenericBsdIfconfigNetwork()
    #invalid input
    iface = dict()
    line = list()
    ips = dict()
    obj.parse_inet6_line(line, iface, ips)
    assert iface == dict()
    assert ips == dict()
    #valid input
    iface = dict()
    line = list()
    line.append('inet6')
    line.append('fe80::5e5:5ff:fe5d:8ed0%em0')
    line.append('prefixlen')
    line.append('64')
    line.append('scopeid')
    line.append('0x2')
    ips = dict()
    obj.parse_inet6_line(line, iface, ips)

# Generated at 2022-06-13 01:36:13.622773
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():
    platform = 'GenericBsdIfconfig'

    test_module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )

    test_network = Network(test_module)

    test_default_ipv4 = dict(
        interface='en0',
        address='192.168.1.1',
    )

    test_default_ipv6 = dict(
        interface='en0',
        address='fe80::967e:51ff:fe97:f241',
    )
