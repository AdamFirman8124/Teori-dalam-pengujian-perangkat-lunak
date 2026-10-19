

# Generated at 2022-06-13 01:27:44.990877
# Unit test for method parse_inet_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet_line():
    from ansible.module_utils.network.common.network.module_utils.network.common.utils import set_module_args
    # create a test module
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )
    # Set args
    set_module_args(dict(gather_subset=['!all','!min']))
    # Instantiate the module
    module.params['gather_network_resources'] = 'no'
    network_module = NetworkModule(module, run_intentionally_missed=False)
    network_module.generic_bsd_ifconfig_network = GenericBsdIfconfigNetwork(module)
    # Execute the module

# Generated at 2022-06-13 01:27:55.265682
# Unit test for method parse_ether_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_ether_line():
    # tests to make sure that parse_ether_line properly sets the
    # current_if['type'] and current_if['macaddress']
    # values of the passed in dictionary

    # Test that data is properly set when all data is present
    current_if = {}
    words = ['bge0:', 'flags=8843<UP,BROADCAST,RUNNING,SIMPLEX,MULTICAST>',
             'metric 0', 'mtu 1500', 'ether xx:xx:xx:xx:xx:xx']
    module = MockModule()
    generic_bsd_ifconfig_network = GenericBsdIfconfigNetwork(module)

    generic_bsd_ifconfig_network.parse_ether_line(words, current_if, ips)

    assert current_if['type'] == 'ether'

# Generated at 2022-06-13 01:28:07.844966
# Unit test for method get_options of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_options():
    # Even though this is a static function, we need an instance to get
    # at the function (in Python 2).
    obj = GenericBsdIfconfigNetwork({}, {})
    s = "options=3<RXCSUM,TXCSUM,VLAN_MTU>"
    assert obj.get_options(s) == ['RXCSUM', 'TXCSUM', 'VLAN_MTU']
    s = "options=3"
    assert obj.get_options(s) == []
    s = "options=3<>"
    assert obj.get_options(s) == []
    s = "options=<>"
    assert obj.get_options(s) == []
    s = "options=<RXCSUM,TXCSUM,VLAN_MTU>"

# Generated at 2022-06-13 01:28:18.651793
# Unit test for method get_interfaces_info of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_interfaces_info():
    ifc = GenericBsdIfconfigNetwork(module=None)


# Generated at 2022-06-13 01:28:25.498302
# Unit test for method parse_interface_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_interface_line():
    # GenericBsdIfconfigNetwork is not a direct subclass of GenericIfconfigNetwork.
    # GenericBsdIfconfigNetwork is a subclass of GenericBsdNetwork, which is a subclass of GenericIfconfigNetwork.
    # The call to parse_interface_line method is in the GenericBsdNetwork class. This is not a known good
    # route to test the method. Will create a class that inherits from GenericIfconfigNetwork with a dummy
    # module, then register the class.
    class BsdNetwork(GenericIfconfigNetwork):
        def __init__(self, module):
            super(BsdNetwork, self).__init__(module)

    module = AnsibleModule({})
    BsdNetwork.register(module)

    # Interface name

# Generated at 2022-06-13 01:28:34.337318
# Unit test for method parse_media_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_media_line():
    interface = {'device': 'bge0'}
    ips = dict(
        all_ipv4_addresses=[],
        all_ipv6_addresses=[],
    )
    # create the object
    class_obj = GenericBsdIfconfigNetwork()
    words = []
    current_if = {}
    # test 1
    words = ['media:', 'Ethernet', 'autoselect', '(1000baseT)']
    current_if = interface
    current_if['type'] = 'unknown'
    current_if['media'] = 'unknown'
    current_if['media_select'] = 'unknown'
    current_if['media_type'] = 'unknown'
    current_if['media_options'] = []
    class_obj.parse_media_line(words, current_if, ips)

# Generated at 2022-06-13 01:28:36.035320
# Unit test for method get_options of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_options():
    module = AnsibleModule(argument_spec={})
    test = GenericBsdIfconfigNetwork(module)

    assert test.get_options('options=<NONE>') == ['NONE']



# Generated at 2022-06-13 01:28:48.573227
# Unit test for method parse_inet6_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet6_line():
    # Arrange
    words = ['inet6', 'fe80::9c07:5bff:feea:f5b5', 'prefixlen', '64', 'scopeid', '0x2', 'inet6', 'fe80::fc54:ff:fe35:d4d0', 'prefixlen', '64', 'scopeid', '0x1', 'inet6', '::1', 'prefixlen', '128', 'inet6', 'fe80::1%lo0', 'prefixlen', '64', 'scopeid', '0x3', 'inet6', 'fe80::c32b:6aff:fef9:d6ef', 'prefixlen', '64', 'scopeid', '0x4']
    current_if = {}

# Generated at 2022-06-13 01:28:57.862773
# Unit test for method parse_inet6_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet6_line():
    module = AnsibleModule({})
    platform = GenericBsdIfconfigNetwork(module)
    current_if = {'device': 'something', 'ipv4': [], 'ipv6': []}
    ips = dict(all_ipv4_addresses=[], all_ipv6_addresses=[])
    words = 'inet6 fe80::6099:c3ff:fe1d:f2b3%vlan2 prefixlen 64 scopeid 0x5'.split()
    platform.parse_inet6_line(words, current_if, ips)
    assert current_if['ipv6'][0]['address'] == 'fe80::6099:c3ff:fe1d:f2b3%vlan2'


# Generated at 2022-06-13 01:29:07.513087
# Unit test for method parse_media_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_media_line():
    # Create object
    n = GenericBsdIfconfigNetwork()
    current_if = {}
    ips = dict(
        all_ipv4_addresses=[],
        all_ipv6_addresses=[],
    )
    words = ['media:',
             'Ethernet',
             'autoselect',
             '(1000baseT<full-duplex>)'
             ]
    n.parse_media_line(words, current_if, ips)
    assert current_if['media'] == 'Ethernet'
    assert current_if['media_select'] == 'autoselect'
    assert current_if['media_type'] == '(1000baseT<full-duplex>)'

# Generated at 2022-06-13 01:29:23.540659
# Unit test for method parse_ether_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_ether_line():
    ne = GenericBsdIfconfigNetwork()
    current_if = {}
    current_if['device'] = None
    current_if['macaddress'] = None
    current_if['ether'] = None
    ips = {}
    words = ['ether','52:54:00:ab:2a:9f']
    ne.parse_ether_line(words,current_if,ips)
    assert current_if['device'] == None
    assert current_if['macaddress'] == '52:54:00:ab:2a:9f'
    assert current_if['ether'] == None
    assert ips == {}
    assert words == ['ether','52:54:00:ab:2a:9f']



# Generated at 2022-06-13 01:29:32.100849
# Unit test for method get_interfaces_info of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_interfaces_info():
    gbin = GenericBsdIfconfigNetwork()
    # DragonFly BSD.

# Generated at 2022-06-13 01:29:36.912644
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_default_interfaces():
    options = globals()
    options.update({
        'bin_path': {
            'route': '/sbin/route'
        },
        'run_command': {
            'route': [
                1,
                str('default 192.168.122.1 UGS 0 4 em1'),
                str('default fe80::a00:27ff:fe86:c3bc%em1 UGS 0 4 em1')
            ]
        },
    })
    test_instance = GenericBsdIfconfigNetwork(Options(**options))

    # Test IPv4 gateway
    assert test_instance.get_default_interfaces(options['bin_path']['route'])[0] == {'interface': 'em1', 'gateway': '192.168.122.1'}

    # Test IPv6 gateway
    assert test_instance

# Generated at 2022-06-13 01:29:48.998433
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():
    # Test with command output from DragonFly 3.0
    module = FakeModule()
    result = GenericBsdIfconfigNetwork().populate({'ansible_facts': {}, 'ansible_module': module})
    assert result['default_ipv4']['interface'] == 'em0'
    assert result['default_ipv4']['address'] == '192.168.1.1'
    assert result['default_ipv4']['gateway'] == '192.168.1.255'
    assert 'gateway' not in result['default_ipv6']
    assert result['default_ipv6']['interface'] == 'em0'
    assert result['default_ipv6']['address'] == 'fe80::5efe:192.168.1.1%em0'

# Generated at 2022-06-13 01:29:58.441541
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():
    gather_subset = ["all"]
    filters = ["lo0"]
    data = GenericFactCollector('module', 'local_tmp', gather_subset, filters).collect()
    network_facts = data['ansible_facts']['ansible_network_resources']
    assert network_facts['interfaces'] == ['lo0']
    for key in ['broadcast', 'netmask', 'network']:
        assert key in network_facts['lo0']['ipv4'][0]
        assert key in network_facts['lo0']['ipv6'][0]



# Generated at 2022-06-13 01:30:07.655548
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():
  # mock out the module class
  module = MagicMock()
  module.run_command.return_value = 0, "", ""
  module.get_bin_path.return_value = "/bin/ifconfig"

  platform = "Generic_BSD_Ifconfig"

  network = Network(module)
  network.populate()

  assert network.facts['default_ipv4'] == {'broadcast': 'ff:ff:ff:ff:ff:ff', 'gateway': '0.0.0.0', 'interface': 'lo0'}
  assert network.facts['default_ipv6'] == {}
  assert network.facts['interfaces'] == ['lo0']

# Generated at 2022-06-13 01:30:13.205189
# Unit test for method detect_type_media of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_detect_type_media():
    """Test for method detect_type_media of class GenericBsdIfconfigNetwork."""
    c = GenericBsdIfconfigNetwork()
    current_if = {'device': 'lo0', 'ipv4': [], 'ipv6': [], 'type': 'unknown'}
    interfaces = {'lo0': current_if}
    assert(c.detect_type_media(interfaces) == interfaces)

# Generated at 2022-06-13 01:30:23.304491
# Unit test for method parse_media_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_media_line():
    mac_words = [
        'media:',
        'Ethernet',
        'autoselect',
        '(1000baseT)'
    ]
    expected = {
        'media' : 'Ethernet',
        'media_select' : 'autoselect',
        'media_type' : '1000baseT'
    }
    network_facts = GenericBsdIfconfigNetwork()
    network_facts.parse_media_line(mac_words, {})
    assert mac_words[0] == 'media:'
    for i in 1,2,3:
        assert mac_words[i] == expected[mac_words[i]]

    freebsd_words = [
        'media:',
        'Ethernet',
        'autoselect',
        '(1000baseT<full-duplex>)'
    ]

# Generated at 2022-06-13 01:30:31.115006
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_default_interfaces():

    def check_answer(in_answer, expected_answer):
        assert expected_answer['interface'] == in_answer['interface']
        assert expected_answer['gateway'] == in_answer['gateway']

    #
    # First test (Invalid argument)
    #
    test_input = """
    gateway: localhost
    """
    test_answer = GenericBsdIfconfigNetwork.get_default_interfaces(test_input)
    test_expected_answer= {}
    check_answer(test_answer[1], test_expected_answer)

    #
    # Second test (Normal)
    #
    test_input = """
    gateway: default
    interface: localhost
    """

    test_expected_answer['interface'] = 'localhost'
    test_expected_answer['gateway'] = 'default'
    test_answer

# Generated at 2022-06-13 01:30:42.096835
# Unit test for method parse_inet_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet_line():
    from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork
    from collections import defaultdict
    c = GenericBsdIfconfigNetwork('eth0')
    o = defaultdict(list)
    p = ['inet', '127.0.0.1', 'netmask', '0xff000000']
    c.parse_inet_line(p, None, o)
    assert o['all_ipv4_addresses'] == ['127.0.0.1']
    p = ['inet', '10.0.0.1', 'netmask', '0xff000000']
    c.parse_inet_line(p, None, o)
    assert o['all_ipv4_addresses'] == ['127.0.0.1', '10.0.0.1']

# Generated at 2022-06-13 01:30:59.879972
# Unit test for method parse_inet_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet_line():
    m = GenericBsdIfconfigNetwork()
    current_if = dict()
    ips = dict()

    # test ipv4 address
    m.parse_inet_line(['inet', '127.0.0.1', 'netmask', '0xff000000'], current_if, ips)
    assert current_if['ipv4'][0]['address'] == '127.0.0.1'
    assert current_if['ipv4'][0]['netmask'] == '255.0.0.0'
    assert current_if['ipv4'][0]['network'] == '127.0.0.0'
    assert current_if['ipv4'][0]['broadcast'] == '127.255.255.255'

    # test ipv4 with alias
    m.parse_inet_

# Generated at 2022-06-13 01:31:11.777909
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():
    defaults = dict(interface='lo0')
    interfaces = dict(
        lo0=dict(
            ipv4=list(),
            ipv6=list(),
            device='lo0'
        ),
        eth0=dict(
            ipv4=list(),
            ipv6=list(),
            device='eth0'
        )
    )
    ifconfig_platform = GenericBsdIfconfigNetwork()
    ifconfig_platform._merge_default_interface(defaults, interfaces, 'ipv4')

    ipv4 = dict(
        interface='lo0',
        device='lo0'
    )
    assert defaults == ipv4, defaults

    defaults = dict(interface='lo0')

# Generated at 2022-06-13 01:31:22.362896
# Unit test for method get_interfaces_info of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_interfaces_info():
    module = AnsibleModule(argument_spec=get_default_argspec())

    ifconfig_path = module.get_bin_path('ifconfig')

    platform = GenericBsdIfconfigNetwork(module)

    interfaces, ips = platform.get_interfaces_info(ifconfig_path)

    assert 'lo0' in interfaces
    assert 'ether' in interfaces['lo0']['type']
    assert 'lo0' in interfaces
    assert 'inet' in interfaces['lo0']['ipv4'][0]
    assert 'netmask' in interfaces['lo0']['ipv4'][0]
    assert 'network' in interfaces['lo0']['ipv4'][0]
    assert 'ether' in interfaces['lo0']

# Generated at 2022-06-13 01:31:28.317317
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():
    class CiscoIosNetworkModuleMock(object):
        def __init__(self):
            self.mock_run_command_return_value = 'default_output'
            self.run_command_call_history = []

        def get_bin_path(self, executable, opt_dirs=None, required=False):
            return 'thing'


# Generated at 2022-06-13 01:31:35.708247
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_default_interfaces():
    # Setup
    generic_bsd_ifconfig_network = GenericBsdIfconfigNetwork()

    # Test 1
    result = generic_bsd_ifconfig_network.get_default_interfaces(route_path)

    # Test 2
    generic_bsd_ifconfig_network.get_default_interfaces(route_path)

    assert result['v4']['interface'] == 'lo0'
    assert result['v4']['address'] == '127.0.0.1'
    assert result['v4']['gateway'] == '127.0.0.1'


# Generated at 2022-06-13 01:31:45.724905
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():
    network = GenericBsdIfconfigNetwork()
    network.module = dummy()
    network.module.run_command = run_command


# Generated at 2022-06-13 01:31:55.904609
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():
        m = AnsibleModule()
        n = GenericBsdIfconfigNetwork(m)

        defaults = dict(interface='lo0', ipv4=[])
        interfaces = dict(lo0=dict(ipv4=[], ipv6=[], device='lo0'))
        n.merge_default_interface(defaults, interfaces, 'ipv4')
        assert defaults == dict(interface='lo0', ipv4=[], device='lo0')

        defaults = dict(default_ipv4=dict(interface='lo0', ipv4=[], device='lo0'))
        interfaces = dict(lo0=dict(ipv4=[], ipv6=[], device='lo0'))
        n.merge_default_interface(defaults['default_ipv4'], interfaces, 'ipv4')

# Generated at 2022-06-13 01:32:07.449921
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():
    GENBsdIfNw = GenericBsdIfconfigNetwork()
    defaults = {
        'interface':'bridge0',
        'address':'10.110.40.33',
        'macaddress':'0a:60:78:ab:ca:d5'
    }


# Generated at 2022-06-13 01:32:16.853589
# Unit test for method parse_inet_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet_line():
    ifconfig_path = '/sbin/ifconfig'
    ifconfig_options = '-a'
    current_if = {'device': 'en0', 'ipv4': [], 'ipv6': [], 'type': 'unknown'}
    ips = dict(
        all_ipv4_addresses=[],
        all_ipv6_addresses=[],
    )

    # case 1 example output with cidr style ip address (eg, 127.0.0.1/24)
    # in inet line used in netbsd ifconfig -e output after 7.1
    words = ['inet', '192.168.100.11/24', 'netmask', '0xffffff00', 'broadcast', '192.168.100.255']
    gbn = GenericBsdIfconfigNetwork(None)
   

# Generated at 2022-06-13 01:32:24.778652
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork

# Generated at 2022-06-13 01:32:41.338001
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_default_interfaces():
    # test for method get_default_interfaces(route_path)
    # of class GenericBsdIfconfigNetwork
    module = AnsibleModule(
        argument_spec=dict(
            route_path=dict(type='str', required=False)
        ),
    )

    # Make sure we have a module to test
    assert module

    network = GenericBsdIfconfigNetwork(module)

    route_path = {'v4': 'route -n get default',
                  'v6': 'route -n get -inet6 default'}

    # IPv4
    # FreeBSD

# Generated at 2022-06-13 01:32:49.722727
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():
    _system_info = dict(
        distro=dict(
            id='FreeBSD',
            version_id='7.4',
        ),
        network=dict(
            default_ipv4=dict(
                interface='lo0',
            ),
        ),
    )
    _module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True,
    )
    _module._system_info = _system_info
    _mock_network = MagicMock(GenericBsdIfconfigNetwork)
    getattr(_mock_network, '_system_info', _module._system_info)

    # Case 1: no values in defaults dict
    defaults = {}

# Generated at 2022-06-13 01:32:59.416780
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():
    module = AnsibleModule(argument_spec={})
    pci_test_class = GenericBsdIfconfigNetwork()
    interfaces = dict({'eth0':
                       {'ipv4': [{'address':'192.168.1.1', 'netmask': '255.255.255.0', 'broadcast': '192.168.1.1'}],
                        'ipv6': [{'address':'fe80::5efe:192.168.1.1', 'prefix': '64', 'scope': 'link'}],
                        'macaddress': '00:01:02:03:04:05',
                        'metric': '0',
                        'mtu': '9000',
                       }})
    defaults = dict({'interface':'eth0', 'address':'192.168.1.1'})
    pci

# Generated at 2022-06-13 01:33:11.859285
# Unit test for method get_interfaces_info of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_interfaces_info():
    module = AnsibleModule(argument_spec={})
    module.params['gather_subset'] = 'all'


# Generated at 2022-06-13 01:33:23.445475
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():
    defaults = {
        'interface': 'lo0',
        'address': '127.0.0.1',
    }
    interfaces = {
        'lo0': {
            'ipv4': [
                {'address': '127.0.0.1', 'netmask': '255.0.0.0', 'broadcast': '127.255.255.255', 'network': '127.0.0.0'},
                {'address': '127.1.1.1', 'netmask': '255.0.0.0', 'broadcast': '127.255.255.255', 'network': '127.0.0.0'},
            ],
        },
    }


# Generated at 2022-06-13 01:33:26.635215
# Unit test for method parse_media_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_media_line():
    message = "Test parse_media_line of class GenericBsdIfconfigNetwork"

    # Setup a mock module and network module class
    module_mock = MagicMock()

    network_facts = GenericBsdIfconfigNetwork(module_mock)

    # Test method
    # Method is only used to set media and is not used, return True
    assert True == network_facts.parse_media_line(["media:"])



# Generated at 2022-06-13 01:33:37.887495
# Unit test for method parse_media_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_media_line():
    bsd_network = GenericBsdIfconfigNetwork()
    words = ['media:', 'Ethernet', 'autoselect', '(100baseTX <full-duplex>)', 'status:' ,'active']
    current_if = {}
    ips = {}

    bsd_network.parse_media_line(words, current_if, ips)

    assert current_if.get('media') == 'Ethernet'
    assert current_if.get('media_select') == 'autoselect'
    assert current_if.get('media_type') == 'full-duplex'
    assert current_if.get('media_options') == ['100baseTX']
    assert current_if.get('status') == 'active'
# Test class for method parse_options_line of class GenericBsdIfconfigNetwork

# Generated at 2022-06-13 01:33:44.819071
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_default_interfaces():
    class MockModule(object):
        def __init__(self):
            self.run_command_calls = []

        def run_command(self, command, check_rc=True):
            self.run_command_calls.append(command)
            if command[:4] == ['/sbin/route', '-n', 'get', 'default']:
                return 0, 'interface: en5\ngateway: 192.168.0.254', ''
            elif command[:5] == ['/sbin/route', '-n', 'get', '-inet6', 'default']:
                return 0, 'interface: en5\ngateway: ::1', ''
            else:
                assert command == []


# Generated at 2022-06-13 01:33:49.991671
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():
    defaults = dict(
        interface='eth0'
    )
    interface = dict(
        interface='eth0',
    )
    interfaces = dict(
        eth0=interface
    )
    class_obj = GenericBsdIfconfigNetwork()
    result = class_obj.merge_default_interface(defaults, interfaces, 'ipv6')
    expected = None
    assert result == expected


# Generated at 2022-06-13 01:33:57.493244
# Unit test for method parse_inet_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet_line():
    module = AnsibleModule(argument_spec={})
    network = GenericBsdIfconfigNetwork(module)
    iface = {}
    ips = {
        'all_ipv4_addresses': [],
        'all_ipv6_addresses': [],
    }
    test_in = '192.168.0.1 netmask 0xffffff00 broadcast 192.168.0.255'
    network.parse_inet_line(test_in.split(), iface, ips)
    assert iface['ipv4'][0]['address'] == '192.168.0.1'
    assert iface['ipv4'][0]['netmask'] == '255.255.255.0'

# Generated at 2022-06-13 01:34:24.599817
# Unit test for method get_interfaces_info of class GenericBsdIfconfigNetwork

# Generated at 2022-06-13 01:34:28.572388
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True)

    n = GenericBsdIfconfigNetwork(module)

    facts = n.populate()

    assert facts['interfaces'] == ['lo0', 're0', 'vlan100']



# Generated at 2022-06-13 01:34:40.397735
# Unit test for method parse_inet6_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet6_line():
    test_network = GenericBsdIfconfigNetwork({})
    test_current_if = dict(ipv4=[], ipv6=[], type='unknown')
    test_ips = dict(
        all_ipv4_addresses=[],
        all_ipv6_addresses=[],
    )
    test_words = ['inet6', 'fc00:dead:beef::1/64', 'prefixlen', '64', 'noprefixroute', 'alias']
    test_network.parse_inet6_line(test_words, test_current_if, test_ips)
    assert test_ips['all_ipv6_addresses'] == ['fc00:dead:beef::1']
    assert len(test_current_if['ipv6']) == 1

# Generated at 2022-06-13 01:34:50.916288
# Unit test for method parse_inet_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet_line():
    import sys

# Generated at 2022-06-13 01:34:55.238583
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():
    default_ipv4 = dict(interface='foo', address='192.168.0.1')
    interfaces = dict(foo=dict(ipv4=[dict(address='192.168.0.1'), dict(address='192.168.0.2')], ipv6=[], other='bar'))
    network = GenericBsdIfconfigNetwork()
    network.merge_default_interface(default_ipv4, interfaces, 'ipv4')
    assert default_ipv4 == dict(address='192.168.0.1', interface='foo', ipv4=[dict(address='192.168.0.1'), dict(address='192.168.0.2')], other='bar')


# Generated at 2022-06-13 01:35:05.661501
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():
    # Setup
    default_interface = {'gateway': '192.168.20.1', 'interface': 'vmx0'}

# Generated at 2022-06-13 01:35:14.955279
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():
    class Options:
        def __init__(self):
            self.connection = 'local'
            self.module_path = os.path.dirname(os.path.realpath(__file__))
            return
    options = Options()
    module = NetworkModule(argument_spec={},
                           supports_check_mode=True)
    module.params = {}
    setattr(module, 'get_bin_path', mock.MagicMock(side_effect=lambda x: os.path.dirname(os.path.realpath(__file__))))
    setattr(module, 'run_command', mock.MagicMock(side_effect=lambda x: (0, True, '')))
    network = GenericBsdIfconfigNetwork(module)

    # test interface not in interfaces
    defaults = {'interface': 'em0'}


# Generated at 2022-06-13 01:35:20.678074
# Unit test for method get_interfaces_info of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_interfaces_info():
    m = AnsibleModule(argument_spec={})
    f = GenericBsdIfconfigNetwork(m)

    interfaces = {}
    current_if = {}
    ips = dict(
        all_ipv4_addresses=[],
        all_ipv6_addresses=[],
    )
    # on NetBSD, the ifconfig output looks like this

# Generated at 2022-06-13 01:35:29.947451
# Unit test for method parse_inet6_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet6_line():
    module = MagicMock()
    current_if = {}
    ips = {}

    network = GenericBsdIfconfigNetwork(module)

    # test 0: regular ipv6 address
    words = ['inet6', 'fc76:a0dd:7444:5566:00aa:9999:aaaa:bbbb', 'prefixlen', '64', 'scopeid', '0x3']
    network.parse_inet6_line(words, current_if, ips)

    assert len(ips['all_ipv6_addresses']) == 1
    assert ips['all_ipv6_addresses'][0] == 'fc76:a0dd:7444:5566:00aa:9999:aaaa:bbbb'


# Generated at 2022-06-13 01:35:37.132379
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_default_interfaces():
    fake_module = FauxModule()
    network = GenericBsdIfconfigNetwork(fake_module)

    # Try without a route command
    fake_module.run_command = FauxAnsibleModule.run_command
    fake_module.get_bin_path = lambda x: None
    (default_ipv4, default_ipv6) = network.get_default_interfaces('route')
    assert (default_ipv4 == {})
    assert (default_ipv6 == {})

    # Fake route command output

# Generated at 2022-06-13 01:36:10.592918
# Unit test for method get_interfaces_info of class GenericBsdIfconfigNetwork

# Generated at 2022-06-13 01:36:18.921389
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():
    network = GenericBsdIfconfigNetwork()
    defaults = {
        'interface': 'lo0',
        'address': '::1'
    }
    interfaces = {
        'lo0': {
            'ipv4': [
                {
                    'address': '127.0.0.1',
                    'netmask': '255.0.0.0',
                    'broadcast': '127.255.255.255',
                    'network': '127.0.0.0'
                }
            ],
            'ipv6': [
                {
                    'address': '::1',
                    'prefix': '128',
                    'scope': 'host'
                }
            ]
        }
    }
    network.merge_default_interface(defaults, interfaces, 'ipv6')

# Generated at 2022-06-13 01:36:23.947251
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():
    from ansible.module_utils.network.common.utils import dict_merge
    from ansible.module_utils.network.bsd.ifconfig import GenericBsdIfconfigNetwork

    # TODO: Extend this to not require side_effects in the fixtures.
    # This is here *only* because the module *actually* calls out to
    # the system.
    class TestModule(object):
        def __init__(self):
            self.params = dict()
            self.params['gather_subset'] = ['!all', '!min']

        def run_command(self, cmd, check_rc=True):
            if len(cmd) == 1:
                cmd = ' '.join(cmd)

# Generated at 2022-06-13 01:36:32.442099
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():
    module = AnsibleModule(argument_spec={})
    # build sample output for ifconfig
    out_media_status = ''

# Generated at 2022-06-13 01:36:41.399824
# Unit test for method get_interfaces_info of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_interfaces_info():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(
        argument_spec = dict(),
        supports_check_mode = True
    )

    # fake ifconfig output

# Generated at 2022-06-13 01:36:49.746367
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():
    module = AnsibleModule(argument_spec={})
    module.run_command = MagicMock(return_value=(0, 'success', ''))
    module.get_bin_path = MagicMock(return_value='/bin/path')

    network = GenericBsdIfconfigNetwork(module)

    network.get_interfaces_info = MagicMock(return_value=(
        {},
        {
            'all_ipv4_addresses': ['1.1.1.1', '1.1.1.2'],
            'all_ipv6_addresses': ['1:1:1::1', '1:1:2::1']
        }
    ))


# Generated at 2022-06-13 01:36:57.340809
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():
    inst = GenericBsdIfconfigNetwork()
    inst.module.get_bin_path = Mock(return_value='/bin/ifconfig')
    inst.module.run_command = Mock(return_value=(0, '', ''))
    assert inst.populate() == {'default_ipv4': {}, 'default_ipv6': {}, 'interfaces': [], 'all_ipv4_addresses': [], 'all_ipv6_addresses': []}


# Generated at 2022-06-13 01:37:00.081489
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():
    print('TODO: write unit test for method merge_default_interface of class GenericBsdIfconfigNetwork')

# Generated at 2022-06-13 01:37:07.602476
# Unit test for method parse_inet_line of class GenericBsdIfconfigNetwork