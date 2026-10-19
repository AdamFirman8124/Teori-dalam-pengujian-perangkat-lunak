

# Generated at 2022-06-13 01:27:45.077216
# Unit test for method parse_media_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_media_line():
    intf = GenericBsdIfconfigNetwork()
    current_if = {}

    # Test 1
    words = ["media:", "Ethernet", "autoselect", "(1000baseT)", "status:", "active"]
    intf.parse_media_line(words, current_if, ips)
    assert current_if == {'media': 'Ethernet', 'media_select': 'autoselect', 'media_options': ['1000baseT']}

    # Reset
    current_if["media_options"] = []

    # Test 2
    words = ['media:', 'autoselect', '(100baseTX)', 'status:', 'active', 'lladdr', '00:00:00:00:00:00']
    intf.parse_media_line(words, current_if, ips)
    assert current_

# Generated at 2022-06-13 01:27:55.343707
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():
    network_facts = GenericBsdIfconfigNetwork()
    defaults = {'interface':'eth0', 'address': '127.0.0.1'}

# Generated at 2022-06-13 01:28:07.881748
# Unit test for method parse_media_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_media_line():
    """ Tests for method parse_media_line of class GenericBsdIfconfigNetwork """
    # Test where all parameters are passed
    module = AnsibleModule(argument_spec=dict())

    words = ['media:', 'Ethernet', 'autoselect', '(1000baseT)', 'status:', 'active']

    current_if = dict()
    ips = dict(all_ipv4_addresses=[], all_ipv6_addresses=[])

    GenericBsdIfconfigNetwork(module).parse_media_line(words, current_if, ips)

    assert 'media' in current_if
    assert 'media_select' in current_if
    assert 'media_type' in current_if
    assert 'media_options' in current_if

    assert current_if['media'] == 'Ethernet'
    assert current

# Generated at 2022-06-13 01:28:18.692118
# Unit test for method parse_inet_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet_line():
    # prepare for testing class for ansible
    #
    # define test data
    module = {
        'run_command': (0, '', ''),
        'get_bin_path': lambda *args, **kwargs: None
    }
    custom_args = {}
    custom_facts = {}
    network = GenericBsdIfconfigNetwork(module, custom_args, custom_facts)

# Generated at 2022-06-13 01:28:25.498468
# Unit test for method parse_inet6_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet6_line():
    module=sys.modules['ansible.module_utils.network.common.network'].NetworkModule
    network_module=network.NetworkModule(module)
    network_module.get_bin_path=mock_get_bin_path
    # test case 1
    line = "inet6 fe80::250:56ff:fe89:eba3%wlan0 prefixlen 64 scopeid 0x2"
    words = line.split()
    current_if = {'ipv6': [] }
    ips = dict(all_ipv6_addresses=[])
    network.GenericBsdIfconfigNetwork.parse_inet6_line(network.GenericBsdIfconfigNetwork(), words, current_if, ips)
    if len(current_if['ipv6']) != 1:
        raise Exception('Expected one address')


# Generated at 2022-06-13 01:28:34.336476
# Unit test for method populate of class GenericBsdIfconfigNetwork

# Generated at 2022-06-13 01:28:36.580308
# Unit test for method detect_type_media of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_detect_type_media():
    obj_GenericBsdIfconfigNetwork = GenericBsdIfconfigNetwork()
    interfaces = {'em0': {'type': 'unknown'}, 'em1': {'type': 'unknown'}}

    obj_GenericBsdIfconfigNetwork.detect_type_media(interfaces)

# Generated at 2022-06-13 01:28:49.388719
# Unit test for method parse_media_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_media_line():
    ansible_module = AnsibleModule(argument_spec=dict())
    ansible_module.get_bin_path = MagicMock(return_value='/sbin/ifconfig')
    network = GenericBsdIfconfigNetwork(ansible_module)
    current_if = {}
    ips = {}

    words = [
        'media:',
        'Ethernet',
        'autoselect',
        '(100baseTX <full-duplex>)',
        'status:',
        'active'
    ]

    # test populated media options
    network.parse_media_line(words, current_if, ips)

    assert current_if['media'] == 'Ethernet'
    assert current_if['media_select'] == 'autoselect'

# Generated at 2022-06-13 01:28:58.773895
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_default_interfaces():

    class MockModule(object):
        # We don't want to use real command paths so
        # we mock the get_bin_path method

        @staticmethod
        def get_bin_path(cmd):
            return '/path/to/{}'.format(cmd)


# Generated at 2022-06-13 01:29:09.812611
# Unit test for method detect_type_media of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_detect_type_media():
    module_argument_spec = dict(
        config=dict(),
        check_invalid_interface=dict(type='bool', default=False)
    )

    module = NetworkModule(argument_spec=module_argument_spec,
                           supports_check_mode=True)

    generic_bsd_ifconfig_network = GenericBsdIfconfigNetwork(module)

    # Set up test data

# Generated at 2022-06-13 01:29:32.602408
# Unit test for method parse_inet6_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet6_line():
    """generic_bsd_ifconfig.py
    Unit test for method parse_inet6_line of class GenericBsdIfconfigNetwork
    """

    # Setup - create instance
    GNW = GenericBsdIfconfigNetwork()

    # Test: no input line (expect no output)
    words = None
    current_if = {
        'device': 'eth0',
        'ipv4': [],
        'ipv6': [],
        'type': 'unknown'
    }
    ips = dict(
        all_ipv4_addresses=[],
        all_ipv6_addresses=[],
    )
    result = GNW.parse_inet6_line(words, current_if, ips)
    assert result is None

# Generated at 2022-06-13 01:29:45.137686
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():
    def_if = dict()
    def_if['interface'] = 'eth1'
    def_if['gateway'] = '172.16.102.222'
    def_if['address'] = '172.16.102.57'
    ifaces = dict()
    ifaces['eth1'] = dict()
    ifaces['eth1']['ipv4'] = [{'address': '172.16.102.57', 'netmask': '255.255.254.0', 'broadcast': '172.16.102.255', 'network': '172.16.102.0'}]

    obj = GenericBsdIfconfigNetwork()
    obj.merge_default_interface(def_if, ifaces, 'ipv4')
    assert('interface' in def_if)

# Generated at 2022-06-13 01:29:53.446038
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork

# Generated at 2022-06-13 01:30:03.995819
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_default_interfaces():
    def return_value(test_data):
        return ([test_data['return_rc'], test_data['return_out'], ''])


# Generated at 2022-06-13 01:30:05.877002
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():
    """Test case for method GenericBsdIfconfigNetwork.populate"""
    GenericBsdIfconfigNetwork().populate()

# Generated at 2022-06-13 01:30:17.138216
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes

    hostname = socket.gethostname()
    class module(object):
        def __init__(self):
            self.fail_json = basic.fail_json
            self.connection = 'local'
            self.shell = None
            self.run_command = mock.MagicMock(return_value=(0, b'128.2.193.84\n', b''))
            self.get_bin_path = mock.MagicMock(return_value='/sbin/ifconfig')
            self.params = {
                'gather_subset': 'all',
            }
        def get_shell_type(self):
            return 'sh'

    facts = module()

# Generated at 2022-06-13 01:30:26.177413
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():
    print("Test case running...")
    defaults = {
        "interface": "en0",
        "lladdr": "00:11:22:33:44:55",
        "type": "ether"
    }
    interfaces = {
        "en0": {
            "macaddress": "00:11:22:33:44:55",
            "type": "ether",
            "lladdr": "00:11:22:33:44:55",
            "device": "en0"
        },
        "en1": {
            "macaddress": "00:11:22:33:44:56",
            "type": "ether",
            "lladdr": "00:11:22:33:44:56",
            "device": "en1"
        }
    }

# Generated at 2022-06-13 01:30:34.388636
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():
    out_ifinfo = {'device': 'eth0', 'ipv4': [{'address': '10.1.1.1'}], 
                  'ipv6': [{'address': '2010::1'}], 'type': 'ether'}
    out_defaults = {'interface': 'eth0', 'address': '10.1.1.1'}

    module = AnsibleModule(argument_spec={})
    obj = GenericBsdIfconfigNetwork(module)

    obj.merge_default_interface(out_defaults, out_ifinfo, 'ipv4')

    assert '10.1.1.1' == out_defaults['address']
    assert 'eth0' == out_defaults['interface']


# Generated at 2022-06-13 01:30:40.141348
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():
    # Simple smoke tests
    g = GenericBsdIfconfigNetwork()
    assert g.merge_default_interface({'interface': 'lo0'},
                                     {'lo0': {'ipv4': [], 'ipv6': []}},
                                     'ipv4') == None
    assert g.merge_default_interface({'interface': 'lo0', 'address': '127.0.0.1'},
                                     {'lo0': {'ipv4': [], 'ipv6': []}},
                                     'ipv4') == None

# Generated at 2022-06-13 01:30:49.387173
# Unit test for method parse_inet_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet_line():
    # test with one alias address
    line = [
        'lo0:',
        'flags=8049<UP,LOOPBACK,RUNNING,MULTICAST>',
        'mtu 33184',
        'inet 127.0.0.1',
        'netmask 0xff000000',
        'inet alias 127.1.1.1',
        'netmask 0xff000000'
    ]
    words = ' '.join(line).split()
    #print(words)
    network = GenericBsdIfconfigNetwork()
    current_if = {}
    ips = {}
    ips['all_ipv4_addresses'] = []
    #print(ips)
    network.parse_inet_line(words, current_if, ips)
    #print(current_if)
    #print(ips)


# Generated at 2022-06-13 01:31:39.188892
# Unit test for method parse_inet_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet_line():

    class MockModule:
        def __init__(self):
            pass

        def run_command(self, command):
            return 0, output, pylib_err.Popen.stderr

    class MockedNetwork(GenericBsdIfconfigNetwork):
        def __init__(self):
            self.module = MockModule()

    network = MockedNetwork()

    # test a single line
    # inet 127.0.0.1 netmask 0xffffff00 broadcast 127.255.255.255
    current_if = {'device': 'lo0', 'ipv4': [], 'ipv6': [], 'type': 'unknown'}
    ips = dict(
        all_ipv4_addresses=[],
        all_ipv6_addresses=[],
    )


# Generated at 2022-06-13 01:31:41.954318
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():
    GenericBsdIfconfigNetwork.merge_default_interface({"interface": "lo1"}, {"lo1": {"ipv4": [{"address": "0.0.0.0"}]}}, "ipv4")


# Generated at 2022-06-13 01:31:53.186370
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():
    module = AnsibleModule({})
    platform = 'Generic_BSD_Ifconfig'
    network_obj = GenericBsdIfconfigNetwork(module)
    net_facts = dict()
    net_facts['interfaces'] = 'bge0,bge1'
    net_facts['bge0'] = dict(
        ipv4=[dict(address='127.0.0.1', netmask='32', broadcast='127.0.0.1')],
        ipv6=[dict(address='::1', prefix='128')],
        device='bge0',
        type='ether',
        macaddress='02:01:02:03:04:05',
        mtu='1500',
        metric='0',
        flags=['BROADCAST', 'RUNNING', 'MULTICAST']
    )
    net_facts

# Generated at 2022-06-13 01:31:58.871496
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():
    net = GenericBsdIfconfigNetwork()

    interfaces = {}
    interface = {'device': 'lo0', 'mtu': '33184', 'macaddress': 'unknown'}

    interface['ipv4'] = [{'address': '127.0.0.1', 'netmask': '255.0.0.0'}]
    interface['ipv6'] = [{'address': 'fe80::1%lo0', 'prefix': '64'}]

    interfaces['lo0'] = interface

    defaults = {'interface': 'lo0', 'address': '127.0.0.1'}

    net.merge_default_interface(defaults, interfaces, 'ipv4')

    assert defaults['mtu'] == '33184'
    assert defaults['address'] == '127.0.0.1'
   

# Generated at 2022-06-13 01:32:06.799128
# Unit test for method parse_inet6_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet6_line():
    module = NetworkModule(argument_spec=dict())
    network = GenericBsdIfconfigNetwork(module)

    current_if = {'ipv6': []}
    ips = dict(all_ipv6_addresses=[])

    input = ['inet6', '::1', 'prefixlen', '128', 'alias']
    expected_ipv6_addresses = [':1']
    network.parse_inet6_line(input, current_if, ips)
    assert current_if['ipv6'] == [{'address': ':1'}]
    assert ips['all_ipv6_addresses'] == expected_ipv6_addresses


# Generated at 2022-06-13 01:32:16.451701
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_default_interfaces():
    # Setup
    generic_bsd_ifconfig_network = GenericBsdIfconfigNetwork(None)
    route_path = '/sbin/route'
    command_mock = MagicMock()
    generic_bsd_ifconfig_network.module.run_command = command_mock
    command_mock.side_effect = [[0, """
default via 192.0.2.1 metric 100
""", ''], [0, """
default via 2001:db8::1
""", '']]

    # Exercise
    defaults = generic_bsd_ifconfig_network.get_default_interfaces(route_path)

    # Verify

# Generated at 2022-06-13 01:32:24.417488
# Unit test for method parse_inet_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet_line():
    m_module = MagicMock(name='module')
    instance = GenericBsdIfconfigNetwork(m_module)
    words_1 = ['0.0.0.0', 'broadcast', '0.0.0.0']
    current_if = {'device': 'test_device'}
    ips = {'all_ipv4_addresses':[]}
    instance.parse_inet_line(words_1, current_if, ips)
    # assert_equal(current_if['ipv4'][0]['address'], '0.0.0.0')
    words_2 = ['192.168.0.1', 'netmask', '0xffffff00']
    instance.parse_inet_line(words_2, current_if, ips)
    # assert_equal(current_if

# Generated at 2022-06-13 01:32:30.849264
# Unit test for method parse_inet_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet_line():
    def create_current_if():
        return {'device': 'lo0', 'ipv4': [], 'ipv6': [], 'type': 'unknown'}
    out = "lo0: flags=8049<UP,LOOPBACK,RUNNING,MULTICAST> mtu 33184\n" \
          "    inet 127.0.0.1 netmask 0xff000000\n" \
          "    inet6 ::1 prefixlen 128\n"
    network_module = GenericBsdIfconfigNetwork()
    current_if = create_current_if()
    ips = dict(all_ipv4_addresses=[], all_ipv6_addresses=[])
    for line in out.splitlines():
        words = line.split()
        if words[0] == 'inet':
            network_module

# Generated at 2022-06-13 01:32:37.503884
# Unit test for method parse_inet_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet_line():
    gbin = GenericBsdIfconfigNetwork()

    ipv4_address = '127.0.0.1'
    ipv4_netmask = '255.0.0.0'
    ipv4_broadcast = '127.0.255.255'
    ipv4_network = '127.0.0.0'

    word_list = [
        "lo0:",
        "inet", '127.0.0.1', "netmask", "0xff000000", "groupname", "localname", "media:", "Ethernet", "autoselect", "status:", "active",
    ]
    iface = {}
    ips = {}
    gbin.parse_inet_line(word_list, iface, ips)
    assert iface['ipv4'][0]['address']

# Generated at 2022-06-13 01:32:46.376447
# Unit test for method detect_type_media of class GenericBsdIfconfigNetwork

# Generated at 2022-06-13 01:33:18.480445
# Unit test for method get_options of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_options():
    module = Mock()
    gen = GenericBsdIfconfigNetwork(module)
    assert gen.get_options("") == []

# Generated at 2022-06-13 01:33:28.704349
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_default_interfaces():
    module_mock = Mock()
    module_mock.get_bin_path.return_value = "/bin/route"
    network_object = GenericBsdIfconfigNetwork(module_mock)
    out = "   route to: default\n destination: default\n       mask: default\n    gateway: 192.168.1.1"
    module_mock.run_command.return_value = (0, out, '')
    ipv4_dict, ipv6_dict = network_object.get_default_interfaces("/bin/route")
    assert ipv4_dict['interface'] == '192.168.1.1'

# Generated at 2022-06-13 01:33:37.061087
# Unit test for method get_interfaces_info of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_interfaces_info():
    lines = ["em0: flags=8843<UP,BROADCAST,RUNNING,SIMPLEX,MULTICAST> metric 0 mtu 1500"]
    ifcfg = GenericBsdIfconfigNetwork()
    current_if = ifcfg.parse_interface_line(lines[0].split())
    assert current_if['device'] == "em0"
    assert current_if['type'] == "unknown"
    assert len(current_if['flags']) == 5
    assert current_if['mtu'] == "1500"


# Generated at 2022-06-13 01:33:47.785080
# Unit test for method get_interfaces_info of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_interfaces_info():

    # Mocking out the run_command method so that I can control the output for testing
    import io
    import os
    import sys

    class FakeModule(object):
        def __init__(self, **kwargs):
            self.params = kwargs

        def fail_json(self, *args, **kwargs):
            self.exit_args = args
            self.exit_kwargs = kwargs
            sys.exit(1)

        def exit_json(self, *args, **kwargs):
            self.exit_args = args
            self.exit_kwargs = kwargs
            sys.exit(0)

        def run_command(self, command):
            self.command = command

    test_module = FakeModule()

    # Example output from FreeBSD 11.1-RELEASE-p1
    #
   

# Generated at 2022-06-13 01:33:55.845775
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():
    defaults = {'interface': 'lo0', 'address': '127.0.0.1', 'foo': 'bar'}
    interfaces = {'lo0': { 'ipv4': [{'address': '127.0.0.1', 'netmask': '255.0.0.0', 'network': '127.0.0.0'}], 'foo': 'baz'}, 'eth0': {'ipv4': [{'address': '192.0.2.1', 'netmask': '255.255.255.0'}]}}

    o = GenericBsdIfconfigNetwork()
    o.merge_default_interface(defaults, interfaces, 'ipv4')
    assert defaults['foo'] == 'baz'
    assert 'address' in defaults
    assert 'netmask' in defaults

# Generated at 2022-06-13 01:34:02.664418
# Unit test for method parse_inet_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet_line():
    from ansible_collections.os.bsd.tests.unit.compat.mock import MagicMock

    mock_module = MagicMock()
    mock_module.run_command = MagicMock(return_value=(0, '', ''))
    from ansible_collections.os.bsd.plugins.module_utils.network.bsd.GenericBsdIfconfigNetwork import Generic_BSD_Ifconfig
    obj = Generic_BSD_Ifconfig(mock_module)

    # NetBSD
    current_if = {'device': 'lo0', 'ipv4': [], 'ipv6': [], 'type': 'unknown'}
    ips = dict(
        all_ipv4_addresses=[],
        all_ipv6_addresses=[],
    )

# Generated at 2022-06-13 01:34:10.701200
# Unit test for method get_interfaces_info of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_interfaces_info():
    module = MockModule()

# Generated at 2022-06-13 01:34:21.195634
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():
    # Setup the object
    module = AnsibleModule({})
    object = GenericBsdIfconfigNetwork(module)
    
    # Test Case 1
    defaults = {}

# Generated at 2022-06-13 01:34:30.296268
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():
    # Test populate checks for existence of ifconfig path
    with mock.patch.object(NetworkService, 'get_bin_path', return_value=None):
        network = GenericBsdIfconfigNetwork()
        network.populate()

    # Test populate checks for existence of route path
    with mock.patch.object(NetworkService, 'get_bin_path', return_value='/sbin/route'):
        with mock.patch.object(GenericBsdIfconfigNetwork, 'get_default_interfaces'):
            with mock.patch.object(GenericBsdIfconfigNetwork, 'get_interfaces_info'):
                network = GenericBsdIfconfigNetwork()
                network.populate()

    # Test populate calls get_default_interfaces, get_interfaces_info and returns network_facts

# Generated at 2022-06-13 01:34:35.214094
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_default_interfaces():

    module = AnsibleModule(argument_spec=dict())

    # setup some mocks...

# Generated at 2022-06-13 01:35:31.988278
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_default_interfaces():
    # Dummy function for globals
    module = ''
    test_class = GenericBsdIfconfigNetwork(module)

    # Test 1
    output = "default via 192.0.2.1 on em0\n"
    f = open('test/unit/ansible_collections/ansible/community/plugins/modules/network/config/get_default_interfaces.txt', 'w')
    f.write(output)
    f.close()

    test_class._executable_exists = Mock(return_value=True)
    test_class.get_bin_path = Mock(return_value='test/unit/ansible_collections/ansible/community/plugins/modules/network/config/get_default_interfaces.txt')

    actual_return = test_class.get_default_interfaces('route')
   

# Generated at 2022-06-13 01:35:37.533998
# Unit test for method parse_inet_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet_line():
    """ Test method parse_inet_line of class GenericBsdIfconfigNetwork """
    from ansible.module_utils.facts.network.generic_bsd_ifconfig import GenericBsdIfconfigNetwork as test_ifconfig
    #  lo0: flags=8049<UP,LOOPBACK,RUNNING,MULTICAST> mtu 33184
    #         inet 127.0.0.1 netmask 0xff000000
    line = ["lo0:", "inet", "127.0.0.1", "netmask", "0xff000000"]
    current_if = {'device': line[0][0:-1], 'ipv4': [], 'ipv6': [], 'type': 'unknown'}
    ips = {'all_ipv4_addresses': [], 'all_ipv6_addresses': []}

# Generated at 2022-06-13 01:35:46.797186
# Unit test for method get_interfaces_info of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_interfaces_info():
    """ test get_interfaces_info method of GenericBsdIfconfigNetwork """
    module = AnsibleModule(argument_spec={})
    obj = GenericBsdIfconfigNetwork(module)
    result = obj.get_interfaces_info(ifconfig_path='/sbin/ifconfig')

# Generated at 2022-06-13 01:35:47.480678
# Unit test for method get_interfaces_info of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_interfaces_info():
    pass


# Generated at 2022-06-13 01:35:48.567372
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_default_interfaces():

    platform = FakeGenericBsdIfconfigNetwork({})
    platform.get_default_interfaces('fake')



# Generated at 2022-06-13 01:35:53.978431
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork

# Generated at 2022-06-13 01:36:02.442552
# Unit test for method detect_type_media of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_detect_type_media():
    from ansible.module_utils.network.common.network import GenericBsdIfconfigNetwork
    network_api = GenericBsdIfconfigNetwork('fake_module')
    interfaces = {}
    interfaces = network_api.detect_type_media(interfaces)
    assert {} == interfaces
    interfaces = {'en0':{'media': 'Ethernet'}}
    interfaces = network_api.detect_type_media(interfaces)
    assert {'en0': {'media': 'Ethernet', 'type': 'ether'}} == interfaces
    interfaces = {'en0':{'media': 'Ethernet autoselect'}}
    interfaces = network_api.detect_type_media(interfaces)
    assert {'en0': {'media': 'Ethernet autoselect', 'type': 'ether'}} == interfaces

# Generated at 2022-06-13 01:36:10.650139
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():
    class ModuleFake:
        def __init__(self):
            self.run_command_result = ''
            self.run_command_rc = 0
            self.run_command_output = []

        def get_bin_path(self, binary):
            return "/fake/bin/" + binary

        def run_command(self, args, check_rc=True, close_fds=True, executable=None, data=None, binary_data=True):
            self.run_command_args = args
            output = self.run_command_output.pop(0)
            return self.run_command_rc, output, self.run_command_result
    module = ModuleFake()

# Generated at 2022-06-13 01:36:14.300604
# Unit test for method get_interfaces_info of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_interfaces_info():
    from ansible.module_utils.basic import AnsibleModule
    import platform
    if not platform.system() in ['FreeBSD', 'MacOS', 'DragonFly']:
        return
    mod = AnsibleModule(argument_spec=dict(mock_ifconfig_output=dict(required=True, type='str')))
    platform = GenericBsdIfconfigNetwork(mod)
    interfaces, ips = platform.get_interfaces_info('/sbin/ifconfig')
    assert interfaces
    assert ips

# Generated at 2022-06-13 01:36:21.509471
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():
    '''Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork'''

    defaults = {'interface': 'eth0'}
    interfaces = {'eth0': {'device': 'eth0', 'macaddress': '00:aa:bb:cc:dd:ee', 'type': 'ether'}}
    generic_bsd_ifconfig = GenericBsdIfconfigNetwork()
    generic_bsd_ifconfig.merge_default_interface(defaults, interfaces, 'ipv4')

    assert defaults == {'interface': 'eth0', 'device': 'eth0', 'macaddress': '00:aa:bb:cc:dd:ee', 'type': 'ether'}
