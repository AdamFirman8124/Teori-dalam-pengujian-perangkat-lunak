

# Generated at 2022-06-13 01:28:19.415483
# Unit test for method parse_media_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_media_line():
    test_iface = {'device': 'lo0', 'ipv4': [], 'ipv6': [], 'type': 'unknown', 'flags': []}
    test_ips = dict(
        all_ipv4_addresses=[],
        all_ipv6_addresses=[],
    )
    test_words = ['media:', 'Ethernet', 'autoselect', '(1000baseT <full-duplex>)']
    network = GenericBsdIfconfigNetwork()
    network.parse_media_line(test_words, test_iface, test_ips)

# Generated at 2022-06-13 01:28:23.033230
# Unit test for method get_interfaces_info of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_interfaces_info():
    module = Mock()
    module.run_command.return_value = 1, '', ''
    obj = GenericBsdIfconfigNetwork(module)
    interfaces, ips = obj.get_interfaces_info('/sbin/ifconfig', ifconfig_options='-a')
    assert interfaces == {}
    assert ips == {'all_ipv4_addresses': [], 'all_ipv6_addresses': []}


# Generated at 2022-06-13 01:28:30.317845
# Unit test for method parse_media_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_media_line():
    options = ['media:', 'Ethernet', '10Gbase-T', '<full-duplex>', '<txpause>']
    current_if = {}
    ips = {}
    GenericBsdIfconfigNetwork().parse_media_line(options,current_if,ips)
    expected = {'full-duplex': True,
                'media': 'Ethernet',
                'media_options': 'full-duplex,txpause',
                'media_select': '10Gbase-T',
                'media_type': 'full-duplex,txpause',
                'txpause': True}
    assert current_if == expected


# Generated at 2022-06-13 01:28:40.850819
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_default_interfaces():
    output_v4 = '''
     interface: en0
   destination: default
        gateway: 17.111.12.13
      interface: en0
         flags: <UP,GATEWAY,DONE,STATIC,PRCLONING>
 recvpipe  sendpipe  ssthresh  rtt,msec    rttvar  hopcount      mtu     expire
       0         0         0         0         0         0      1500         0
'''


# Generated at 2022-06-13 01:28:52.882642
# Unit test for method parse_inet_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet_line():
    gb = GenericBsdIfconfigNetwork()

    # with netmask 255.255.255.255
    words = "inet 127.0.0.1  netmask 0xffffffff".split()
    current_if = {'device': 'lo0', 'mtu': '16384', 'metric': '1', 'flags': ['UP', 'LOOPBACK', 'RUNNING', 'MULTICAST'],
                  'macaddress': 'unknown', 'type': 'loopback', 'ipv4': [], 'ipv6': []}
    ips = dict(
        all_ipv4_addresses=[],
        all_ipv6_addresses=[],
    )
    gb.parse_inet_line(words, current_if, ips)

# Generated at 2022-06-13 01:29:00.837995
# Unit test for method parse_inet6_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet6_line():
    from ansible.module_utils.facts import cache
    from ansible.module_utils.facts.network.generic_bsd import ifconfig
    from ansible.module_utils.facts.network.generic_bsd import network
    ifconfig = ifconfig.GenericBsdIfconfigNetwork()
    network = network.GenericBsdIfconfigNetwork()
    words = 'fe80::1%lo0 prefixlen 64 scopeid 0x2'.split()
    current_if = {'ipv6': [], 'device': 'lo0'}
    ips = dict(
        all_ipv4_addresses=[],
        all_ipv6_addresses=[],
    )
    ifconfig.parse_inet6_line(words, current_if, ips)

# Generated at 2022-06-13 01:29:12.399916
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )

    network_facts = GenericBsdIfconfigNetwork(module).populate()
    assert network_facts['default_ipv4']['interface'] == 'lo0'
    assert network_facts['default_ipv4']['gateway'] == '127.0.0.1'
    assert network_facts['default_ipv4']['type'] == 'loopback'
    assert network_facts['default_ipv4']['address'] == '127.0.0.1'

    assert network_facts['default_ipv6']['interface'] == 'lo0'
    assert network_facts['default_ipv6']['gateway'] == '::1'

# Generated at 2022-06-13 01:29:23.621977
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_default_interfaces():

    ifconfig_path = 'ifconfig_path'
    route_path = 'route_path'
    test_module = AnsibleModule(argument_spec=dict())


# Generated at 2022-06-13 01:29:32.164814
# Unit test for method get_options of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_options():
    obj = GenericBsdIfconfigNetwork()
    assert obj.get_options('foo') == []
    assert obj.get_options('foo<>') == []
    assert obj.get_options('foo<Bar>') == []
    assert obj.get_options('<>') == []
    assert obj.get_options('<Bar>') == []
    assert obj.get_options('<Bar,>') == []
    assert obj.get_options('<Bar,Baz>') == ['Bar', 'Baz']
    assert obj.get_options('<Bar,Baz,Zot>') == ['Bar', 'Baz', 'Zot']
    assert obj.get_options('<Bar,Baz,Zot,>') == ['Bar', 'Baz', 'Zot']
    assert obj.get_options('<,>')

# Generated at 2022-06-13 01:29:44.360054
# Unit test for method parse_media_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_media_line():
    module = AnsibleModule({})
    module.run_command = MagicMock(return_value=(0, '', ''))

    g = GenericBsdIfconfigNetwork({'module': module})

    current_if = {}
    words = ['media:', 'Ethernet', 'autoselect', '(1000baseT)', 'status:', 'active']
    g.parse_media_line(words, current_if, {})
    assert 'media' in current_if
    assert current_if['media'] == 'Ethernet'
    assert 'media_select' in current_if
    assert current_if['media_select'] == 'autoselect'
    assert 'media_type' in current_if
    assert current_if['media_type'] == '(1000baseT)'



# Generated at 2022-06-13 01:29:57.544695
# Unit test for method parse_media_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_media_line():
    network_info_module = GenericBsdIfconfigNetwork()
    result = network_info_module.parse_media_line(['media:', 'Ethernet', '10Gbase-LR'])
    assert result == None

# Generated at 2022-06-13 01:30:06.956246
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():

    from ansible.module_utils.network.common.utils import wrap_var

    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True)

    def get_bin_path(name, required=True):
        try:
            for p in os.environ['PATH'].split(':'):
                if os.path.exists(p + '/' + name):
                    return p + '/' + name
        except Exception:
            pass
        if required:
            module.fail_json(msg='%s not found in PATH or specified: %s' % (name, os.environ['PATH']))

    def run_command(args):
        p = Popen(args, stdin=PIPE, stdout=PIPE, stderr=PIPE)
        p.std

# Generated at 2022-06-13 01:30:17.401984
# Unit test for method parse_inet_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet_line():

    # Fail
    result = {'cmd': 'ifconfig -a',
           'stdout': 'inet 127.0.0.1 netmask 0xff000000',
           'stdout_lines': ['inet 127.0.0.1 netmask 0xff000000'],
           'warnings': []}
    current_if = {'device': 'lo0',
                  'ipv4': [],
                  'ipv6': [],
                  'type': 'unknown'}
    ips = dict(
        all_ipv4_addresses=[],
        all_ipv6_addresses=[],
    )

    # Act
    test_network = GenericBsdIfconfigNetwork()
    test_network.parse_inet_line(result['stdout_lines'][0].split(), current_if, ips)

    # Assert


# Generated at 2022-06-13 01:30:21.793650
# Unit test for method get_options of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_options():
    network = GenericBsdIfconfigNetwork()
    assert network.get_options('lo0: flags=8049<UP,LOOPBACK,RUNNING,MULTICAST> mtu 33184') == [
        'UP', 'LOOPBACK', 'RUNNING', 'MULTICAST'
    ]



# Generated at 2022-06-13 01:30:30.036850
# Unit test for method get_options of class GenericBsdIfconfigNetwork

# Generated at 2022-06-13 01:30:37.393555
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_default_interfaces():

    class mock_ansible_module(object):

        class mocked_run_command(object):

            def __init__(self, returncode, output, err=None):
                self.rc = returncode
                self.returncode = returncode
                self.out = output
                self.output = output
                self.err = err

            def __call__(self, *args, **kwargs):
                return self.rc, self.out, self.err

        def __init__(self):
            self.run_command = mock_ansible_module.mocked_run_command(0, "")

    # unit test 1
    ifconfig_path = '/sbin/ifconfig'
    route_path = '/sbin/route'
    genericsource = GenericBsdIfconfigNetwork(mock_ansible_module())
    test

# Generated at 2022-06-13 01:30:47.729954
# Unit test for method parse_inet6_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet6_line():
    module_mock = MagicMock()
    network = GenericBsdIfconfigNetwork(module_mock)

    current_if = {}
    ips = {'all_ipv6_addresses': []}

    words = ['inet6', 'fe80::1146:4bff:fe8a:e4f/64', 'prefixlen', '64', 'scopeid', '0x2']
    network.parse_inet6_line(words, current_if, ips)
    assert ips['all_ipv6_addresses'] == ['fe80::1146:4bff:fe8a:e4f']

# Generated at 2022-06-13 01:30:58.318781
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():
    facts = GenericBsdIfconfigNetwork()

    # Needed for function get_default_interfaces
    facts.module = Mock()
    facts.module.run_command.return_value = (0, "default via 192.168.1.1 dev eth0", "")
    # Needed for function get_interfaces_info
    # FreeBSD 10.2-RELEASE

# Generated at 2022-06-13 01:31:04.834582
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():
    # Allocate a GenericBsdIfconfigNetwork object
    myGenericBsdIfconfigNetwork = GenericBsdIfconfigNetwork()
    assert myGenericBsdIfconfigNetwork is not None
    # Set up test defaults
    myDefaults = dict(interface = 'abc',
                      something = 'else')
    # Set up test interfaces

# Generated at 2022-06-13 01:31:07.978792
# Unit test for method get_options of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_options():
    bsd = GenericBsdIfconfigNetwork()
    opts = bsd.get_options('LOOPBACK,UP,LOWER_UP')
    assert len(opts) == 3

# Generated at 2022-06-13 01:31:52.560431
# Unit test for method get_options of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_options():
    network = GenericBsdIfconfigNetwork(None)
    assert_equals(network.get_options('<UP,LOOPBACK>'), ['UP','LOOPBACK'])
    assert_equals(network.get_options('<LOOPBACK>'), ['LOOPBACK'])
    assert_equals(network.get_options('<>'), [])
    assert_equals(network.get_options('<RUNNING>'), ['RUNNING'])
    assert_equals(network.get_options('<HELLO,GOODBYE>'), ['HELLO','GOODBYE'])
    assert_equals(network.get_options('HELLO,GOODBYE>'), [])
    assert_equals(network.get_options('<HELLO,GOODBYE'), [])

# Generated at 2022-06-13 01:31:58.336877
# Unit test for method get_interfaces_info of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_interfaces_info():
    platform_mock = Mock()
    platform_mock.system.return_value = 'FreeBSD'
    m_open = mock_open(read_data='fake data')
    with patch("ansible.module_utils.facts.network.interfaces.open", m_open, create=True):
        plugin = GenericBsdIfconfigNetwork(platform_mock)
        plugin.get_interfaces_info('/sbin/ifconfig', '-a')
    #assert plugin.run_command.call_count == 1


# Generated at 2022-06-13 01:32:09.888153
# Unit test for method parse_inet_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet_line():
    module = GenericBsdIfconfigNetwork()

# Generated at 2022-06-13 01:32:18.720042
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():
    # Test empty dict
    gbin = GenericBsdIfconfigNetwork()
    defaults = {'interface': 'eth0'}
    interfaces = {}
    ip_type = 'ipv4'
    gbin.merge_default_interface(defaults, interfaces, ip_type)
    assert 'interface' not in defaults
    # Test empty dict
    defaults = {'interface': 'eth0'}

# Generated at 2022-06-13 01:32:31.016399
# Unit test for method detect_type_media of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_detect_type_media():
    """
    Test if detect_type_media() return the interface type ether
    """
    network = GenericBsdIfconfigNetwork()
    interfaces = dict(
        em0={'device': 'em0', 'ipv4': [], 'ipv6': [], 'type': 'unknown', 'flags': [], 'mtu': True, 'media': 'Ethernet autoselect (1000baseT <full-duplex>)', 'media_select': 'auto'},
        em1={'device': 'em1', 'ipv4': [], 'ipv6': [], 'type': 'loopback', 'flags': ['LOOPBACK'], 'mtu': True, 'media': 'Ethernet autoselect (1000baseT <full-duplex>)', 'media_select': 'auto'})
    interfaces_out = network.detect_

# Generated at 2022-06-13 01:32:37.675863
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():
    def run_module():
        module_args = dict(
        )

# Generated at 2022-06-13 01:32:46.574881
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():
    # setup test data
    class Module(object):
        def get_bin_path(self, arg):
            return '/bin/' + arg
        def run_command(self, arg):
            return (0, '', '')
    module = Module()
    network = GenericBsdIfconfigNetwork(module)
    network.get_default_interfaces = MagicMock(return_value=('foo', 'bar'))
    network.get_interfaces_info = MagicMock(return_value=({'device': 'foo'}, {'all_ipv4_addresses': ['foo'], 'all_ipv6_addresses': ['bar']}))


# Generated at 2022-06-13 01:32:48.568154
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():
    obj = GenericBsdIfconfigNetwork()
    # TODO implement unit test
    raise Exception('not implemented')


# Generated at 2022-06-13 01:32:55.288135
# Unit test for method parse_inet_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet_line():
    def test_parse_inet_line(words, current_if, ips, expected):
        class mock_GenericBsdIfconfigNetwork():
            def __init__(self):
                self.current_if = current_if
                self.ips = ips
            def parse_inet_line(self, words, current_if, ips):
                self.current_if = current_if
                self.ips = ips
        ifconfig = mock_GenericBsdIfconfigNetwork()
        ifconfig.parse_inet_line(words, current_if, ips)
        assert ifconfig.current_if == expected[0]
        assert ifconfig.ips == expected[1]

    ips = {
        'all_ipv4_addresses': []
    }

# Generated at 2022-06-13 01:33:02.569326
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():
    interface_name = 'interface'
    interface = {interface_name: {'ipv4': [{'address': '10.0.0.3', 'broadcast': '10.0.0.255', 'netmask': '255.255.255.0', 'network': '10.0.0.0'}],
                                  'ipv6': [],
                                  'macaddress': '08:00:27:07:38:3c',
                                  'mtu': '1500',
                                  'type': 'ether'}}
    default = {'address': '10.0.0.3', 'gateway': '10.0.0.1', 'interface': 'interface'}

# Generated at 2022-06-13 01:33:29.599688
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():
    module = AnsibleModule({})

# Generated at 2022-06-13 01:33:40.013769
# Unit test for method parse_inet_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet_line():
    # Tests if the IPv4 address with a netmask prefix is correctly parsed.
    net_module = AnsibleModule(argument_spec={}, supports_check_mode=True)
    net_module.params = {'ansible_check_mode': True}
    net = GenericBsdIfconfigNetwork(net_module)
    interface_info = {'device': 'lo0',
                      'ipv4': [],
                      'ipv6': [],
                      'type': 'unknown',
                      'flags': ['UP', 'LOOPBACK', 'RUNNING'],
                      'macaddress': 'unknown',
                      'metric': '8',
                      'mtu': '33184',
                      }
    test_ipv4_prefix = '127.0.0.1/24'

# Generated at 2022-06-13 01:33:50.153040
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():

    class mock_iface():
        def __init__(self, *args, **kwargs):
            self.device = args[0]
            self.ipv4 = []
            self.ipv6 = []

    interfaces = {
        'lo0': mock_iface('lo0'),
        'em0': mock_iface('em0'),
    }

    # test empty default
    defaults = {}
    GenericBsdIfconfigNetwork.merge_default_interface(defaults, interfaces, 'ipv4')
    assert defaults == {}

    # test invalid default
    defaults = {'interface': 'em0'}
    GenericBsdIfconfigNetwork.merge_default_interface(defaults, interfaces, 'ipv4')
    assert defaults == {'interface': 'em0'}

    # test valid default

# Generated at 2022-06-13 01:33:56.714465
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():
    # Setup test data
    defaults = dict(interface='lo0')
    interfaces = dict(lo0=dict(device='lo0', ipv4=[dict(address='127.0.0.1')]))

    # Verify method output
    generic_bsd_ifconfig_network = GenericBsdIfconfigNetwork()
    generic_bsd_ifconfig_network.merge_default_interface(defaults, interfaces, 'ipv4')
    assert defaults == dict(interface='lo0', device='lo0', ipv4=[dict(address='127.0.0.1')], address='127.0.0.1', netmask='255.0.0.0')


# Generated at 2022-06-13 01:34:07.149169
# Unit test for method parse_inet_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet_line():
    test_module = AnsibleModule({})
    test_class = GenericBsdIfconfigNetwork(test_module)

    # Test with a cidr style ip address in the inet line
    current_if = dict(ipv4=[], ipv6=[])
    ips = dict(
        all_ipv4_addresses=[],
        all_ipv6_addresses=[],
    )
    words = ['lo0:', 'flags=8049<UP,LOOPBACK,RUNNING,MULTICAST>', 'metric', '1', 'mtu', '33184',
             'inet', '127.0.0.1/24', 'netmask', '0xff000000']

    # Tested ip address information

# Generated at 2022-06-13 01:34:18.666378
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():
    # Mock out superclass methods
    class MockGenericBsdIfconfigNetwork(GenericBsdIfconfigNetwork):
        def get_default_interfaces(self):
            return {}, {}

        def get_interfaces_info(self):
            interfaces = {}
            interfaces['en0'] = {
                'ipv4': [{
                    'address': '10.0.0.1',
                    'netmask': '255.255.255.0'
                }]
            }
            interfaces['en1'] = {
                'ipv4': [{
                    'address': '10.0.0.2',
                    'netmask': '255.255.255.0'
                }]
            }


# Generated at 2022-06-13 01:34:26.860050
# Unit test for method get_interfaces_info of class GenericBsdIfconfigNetwork

# Generated at 2022-06-13 01:34:34.441403
# Unit test for method parse_inet6_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet6_line():
    # testing with a valid line
    line = 'inet6 fe80::d83e:e9ff:fe01:8a01%br0 prefixlen 64 scopeid 0x3'
    words = line.split()
    current_if = {'device': 'br0', 'ipv4': [], 'ipv6': []}
    ips = dict(
        all_ipv4_addresses=[],
        all_ipv6_addresses=[],
    )
    a = GenericBsdIfconfigNetwork()
    a.parse_inet6_line(words, current_if, ips)

    assert 'fe80::d83e:e9ff:fe01:8a01' in ips.get('all_ipv6_addresses')

# Generated at 2022-06-13 01:34:37.816553
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():
    c = GenericBsdIfconfigNetwork()

    # TODO: write unit tests



#
# BSD netstat network plugin
#

# Generated at 2022-06-13 01:34:45.535027
# Unit test for method parse_inet_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet_line():
    candidate = GenericBsdIfconfigNetwork({})

    current_if = dict(device='lo0', ipv4=[], ipv6=[], type='unknown')
    current_if['flags'] = candidate.get_options('UP,LOOPBACK,RUNNING,MULTICAST')
    current_if['macaddress'] = 'unknown'    # will be overwritten later
    current_if['metric'] = '0'
    current_if['mtu'] = '33184'

    ips = dict(
        all_ipv4_addresses=[],
        all_ipv6_addresses=[],
    )

    # Test aliases
    test_line = 'inet alias 127.1.1.1 netmask 0xff000000'
    words = test_line.split()

# Generated at 2022-06-13 01:35:10.895368
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():
    net = GenericBsdIfconfigNetwork()
    # first sanity check for net.module set
    assert net.module, 'module attr not set in GenericBsdIfconfigNetwork'
    mock_params = {'run_command': MagicMock(), 'get_bin_path': MagicMock()}
    mockmodule = MagicMock(**mock_params)
    mockmodule.get_bin_path.return_value = '/sbin/ifconfig'
    net.module = mockmodule
    net.populate()
    mockmodule.run_command.assert_any_call(['/sbin/ifconfig', '-a'])
test_GenericBsdIfconfigNetwork_populate()

# Generated at 2022-06-13 01:35:17.009331
# Unit test for method parse_inet6_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet6_line():
    test = GenericBsdIfconfigNetwork()

    words = 'fe80::1%lo0 prefixlen 64 scopeid 0x3'.split()
    current_if = {'device': 'lo0', 'macaddress': 'unknown', 'type': 'loopback'}
    ips = dict(
        all_ipv4_addresses=[],
        all_ipv6_addresses=[],
    )

    test.parse_inet6_line(words, current_if, ips)

    assert ips['all_ipv6_addresses'] == ['fe80::1%lo0']



# Generated at 2022-06-13 01:35:26.568710
# Unit test for method get_interfaces_info of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_interfaces_info():
    module = AnsibleModule(argument_spec={})
    network = GenericBsdIfconfigNetwork(module)

    # Config for get_interfaces_info()

# Generated at 2022-06-13 01:35:33.412932
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():
    ifconfig = GenericBsdIfconfigNetwork(None)
    defaults = {'interface': 'lo0', 'address': '0.0.0.0'}
    interfaces = {'lo0': {'ipv4': [{'address': '0.0.0.0'}], 'ipv6': [{'address': '::1'}]}}
    ifconfig.merge_default_interface(defaults, interfaces, 'ipv4')
    assert defaults['address'] == '0.0.0.0'
    ifconfig.merge_default_interface(defaults, interfaces, 'ipv6')
    assert defaults['address'] == '0.0.0.0'
    defaults = {'interface': 'lo0', 'address': '::1'}

# Generated at 2022-06-13 01:35:38.932358
# Unit test for method parse_inet_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet_line():
    # create an instance of class GenericBsdIfconfigNetwork
    network_facts_module = network_module.GenericBsdIfconfigNetwork()


# Generated at 2022-06-13 01:35:47.397107
# Unit test for method detect_type_media of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_detect_type_media():
    ins = GenericBsdIfconfigNetwork(None, None)
    mac_address = '01:23:45:67:89:ab'

# Generated at 2022-06-13 01:35:53.824887
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():
    for platform in TEST_VARS:
        for distro in TEST_VARS[platform]:
            for test_set in [
                {}, # gather_subset=None
                {'options': {'gather_subset': []}},
                {'options': {'gather_subset': ['!all']}},
                {'options': {'gather_subset': ['!fake']}},
                {'options': {'gather_subset': ['network']}},
                {'options': {'gather_subset': ['min']}},
                {'options': {'gather_subset': ['!config']}},
            ]:
                test_ansible = TestAnsibleModule(platform, distro)

# Generated at 2022-06-13 01:36:02.250351
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():
    default_ipv4 = {'interface': 'lo0', 'address': '127.0.0.1'}
    interfaces = {
        'lo0': {
            'device': 'lo0',
            'ipv4': [
                {
                    'address': '127.0.0.1',
                    'netmask': '0xff000000',
                    'network': '127.0.0.1',
                    'broadcast': '127.255.255.255'
                }
            ]
        }
    }
    platform = 'Generic_BSD_Ifconfig'
    network = GenericBsdIfconfigNetwork()
    network.module = AnsibleNetworkModuleMock
    network.module.run_command = MagicMock(return_value=(0, '', ''))
    network.module.get_bin_path = MagicM

# Generated at 2022-06-13 01:36:10.594821
# Unit test for method get_interfaces_info of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_interfaces_info():
    obj = GenericBsdIfconfigNetwork()
    # Test the ifconfig output from MacOS
    ifconfig_output = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'ifconfig_macos.txt'), 'r').read()
    rc, interfaces, ips = obj.get_interfaces_info(ifconfig_output)
    assert isinstance(interfaces, dict)

    assert len(interfaces) == 8
    # Test the ifconfig output from FreeBSD
    ifconfig_output = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'ifconfig_freebsd.txt'), 'r').read()
    rc, interfaces, ips = obj.get_interfaces_info(ifconfig_output)

# Generated at 2022-06-13 01:36:18.920346
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():
    m = GenericBsdIfconfigNetwork()
    f = FactCollector()

    # BSD Ifconfig output for FreeBSD

# Generated at 2022-06-13 01:36:51.618803
# Unit test for method get_interfaces_info of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_interfaces_info():
    module = AnsibleModule(
        argument_spec = dict(),
        supports_check_mode = True
    )
    bsdnetwork = GenericBsdIfconfigNetwork(module)


# Generated at 2022-06-13 01:37:00.947976
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_default_interfaces():
    network_instance = GenericBsdIfconfigNetwork()
    
    # List with first value as 'route', second value as '-n', third value as 'get', fourth value as 'default'
    value0 = ['/sbin/route', '-n', 'get', 'default']
    value1 = 'RTNETLINK answers: Invalid argument'
    
    # Test list with first value as 'route', second value as '-n', third value as 'get', fourth value as 'default'
    # Test empty string for value1 test for second value in tuple
    @patch.object(GenericBsdIfconfigNetwork, 'run_command')
    def test_get_default_interfaces_value_1(self, mock_run_command):
        mock_run_command.return_value = (0, value0, '')

# Generated at 2022-06-13 01:37:08.670045
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_default_interfaces():
    """Test function get_default_interfaces of class GenericBsdIfconfigNetwork"""
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )

    if not HAS_PARAMIKO:
        module.fail_json(msg='paramiko is required but does not appear to be installed, use `pip` or your package '
                             'manager to install it')

    if not HAS_NETIFCONFIG:
        module.fail_json(msg='netifaces is required but does not appear to be installed, use `pip` or your package '
                             'manager to install it')
