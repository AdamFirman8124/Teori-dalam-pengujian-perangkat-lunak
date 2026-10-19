

# Generated at 2022-06-13 01:27:55.067420
# Unit test for method get_interfaces_info of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_interfaces_info():
    platform = 'GenericBsdIfconfigNetwork'
    module = get_platform_subclass(AnsibleModule, platform)()
    ifconfig_path = module.get_bin_path('ifconfig')
    args = dict(ifconfig_path=ifconfig_path)
    network = GenericBsdIfconfigNetwork(module)
    interfaces, ips = network.get_interfaces_info(module.params['ifconfig_path'], ifconfig_options="-a")
    assert interfaces['lo0']['device'] == 'lo0'
    assert interfaces['lo0']['ipv4'][0]['address'] == '127.0.0.1'
    assert interfaces['lo0']['ipv4'][0]['broadcast'] == '127.255.255.255'

# Generated at 2022-06-13 01:28:07.793189
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():
    defaults = dict(
        interface='em0',
        gateway='10.0.0.1',
    )

    interfaces = dict(
        em0=dict(
            device='em0',
            ipv4=[dict(
                address='10.0.0.2',
                netmask='255.255.255.0',
                broadcast='10.0.0.255',
                network='10.0.0.0',
            )],
            ipv6=[dict(
                address='1000::1',
                prefix='64',
                scope='0x5',
            )],
        ),
    )

    gn = GenericBsdIfconfigNetwork()

    gn.merge_default_interface(defaults, interfaces, ip_type='ipv4')


# Generated at 2022-06-13 01:28:18.609877
# Unit test for method get_options of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_options():
    '''Unit test for method get_options of class GenericBsdIfconfigNetwork'''

    gbi = GenericBsdIfconfigNetwork()

    assert gbi.get_options('<LOOPBACK,UP,LOWER_UP>') == ['LOOPBACK', 'UP', 'LOWER_UP']
    assert gbi.get_options('') == []
    assert gbi.get_options('foo') == []
    assert gbi.get_options('<>') == []
    assert gbi.get_options('<LOOPBACK,UP>') == ['LOOPBACK', 'UP']
    assert gbi.get_options('<LOOPBACK,UP,LOWER_UP> metric 1') == ['LOOPBACK', 'UP', 'LOWER_UP']

# Generated at 2022-06-13 01:28:25.136432
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_default_interfaces():
    '''Test function GenericBsdIfconfigNetwork_get_default_interfaces of class GenericBsdIfconfigNetwork'''
    obj = GenericBsdIfconfigNetwork()
    # Test case 1
    # Test the validity of the return value of function get_default_interfaces
    #
    # We don't know what the return value will be, so we just make sure
    # it is a tuple.
    assert isinstance(obj.get_default_interfaces(None), tuple)


# Generated at 2022-06-13 01:28:25.667544
# Unit test for method detect_type_media of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_detect_type_media():

    pass

# Generated at 2022-06-13 01:28:32.737543
# Unit test for method parse_ether_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_ether_line():
    module = get_module_mock()
    generic_network = GenericBsdIfconfigNetwork(module)

    words = ['ether', '00:12:34:56:78:9a']
    current_if = {}
    ips = {}
    generic_network.parse_ether_line(words, current_if, ips)
    assert 'macaddress' in current_if
    assert 'type' in current_if
    assert current_if['macaddress'] == '00:12:34:56:78:9a'
    assert current_if['type'] == 'ether'


# Generated at 2022-06-13 01:28:33.551534
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():
    pass



# Generated at 2022-06-13 01:28:42.613382
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_default_interfaces():
    import platform
    from ansible.module_utils._text import to_bytes
    if platform.system() == 'Darwin':
        route_path = '/sbin/route'
    else:
        route_path = '/sbin/route'
    ifconfig = GenericBsdIfconfigNetwork()
    assert ifconfig is not None

    default_ipv4, default_ipv6 = ifconfig.get_default_interfaces(route_path)
    assert 'interface' in default_ipv4
    #assert 'interface' in default_ipv6



# Generated at 2022-06-13 01:28:54.332313
# Unit test for method get_interfaces_info of class GenericBsdIfconfigNetwork

# Generated at 2022-06-13 01:29:06.401368
# Unit test for method parse_inet_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet_line():
    module = AnsibleModule(argument_spec={})
    net = GenericBsdIfconfigNetwork(module)

    current_if = {'device': 'lo0'}
    ips = dict(
        all_ipv4_addresses=[],
        all_ipv6_addresses=[],
    )

    # Test IPv4 info parsing
    words = ['lo0', 'inet', '127.0.0.1', 'netmask', '0xff000000']
    net.parse_inet_line(words, current_if, ips)
    assert current_if['ipv4'][0]['address'] == '127.0.0.1'
    assert current_if['ipv4'][0]['netmask'] == '255.0.0.0'

# Generated at 2022-06-13 01:29:29.099627
# Unit test for method get_options of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_options():
    # create an instance of the GenericBsdIfconfigNetwork class with default args
    n = GenericBsdIfconfigNetwork()
    option_string = "inet6 fe80::5ebe:caff:feba:c5e5%lo0 prefixlen 64 scopeid 0x3"
    options = n.get_options(option_string)
    assert options == ['inet6', 'fe80::5ebe:caff:feba:c5e5%lo0', 'prefixlen', '64', 'scopeid', '0x3']
    option_string = "lo0: flags=8049<UP,LOOPBACK,RUNNING,MULTICAST> metric 0 mtu 16384"
    options = n.get_options(option_string)

# Generated at 2022-06-13 01:29:33.704126
# Unit test for method get_options of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_options():
    option_string = 'options=<foo,bar,baz>'
    option_csv = 'foo,bar,baz'
    option_list = option_csv.split(',')
    assert GenericBsdIfconfigNetwork.get_options(option_string) == option_list


# Generated at 2022-06-13 01:29:41.235576
# Unit test for method get_options of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_options():
    generic_bsd_testobj = GenericBsdIfconfigNetwork(None, None)
    value = generic_bsd_testobj.get_options('LOOPBACK,RUNNING,MULTICAST>')
    assert value == ['LOOPBACK', 'RUNNING', 'MULTICAST']
    value = generic_bsd_testobj.get_options('LOOPBACK,>')
    assert value == ['LOOPBACK']



# Generated at 2022-06-13 01:29:45.989903
# Unit test for method parse_ether_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_ether_line():
    ifconfig_outputs = """
en0: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
    ether 00:23:32:45:65:4e
    media: autoselect (100baseTX <full-duplex>)
    status: active
"""
    network = GenericBsdIfconfigNetwork()
    current_if = {}
    ips = {}
    for line in ifconfig_outputs.splitlines():
        if line:
            words = line.split()
            if words[0].startswith('ether'):
                network.parse_ether_line(words, current_if, ips)
                assert current_if == {'macaddress': '00:23:32:45:65:4e', 'type': 'ether'}


# Generated at 2022-06-13 01:29:53.946205
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_default_interfaces():
    generic = GenericBsdIfconfigNetwork()

    # The following is output of 'route -n get default' on FreeBSD 12.0
    #     route to: default
    #     destination: default
    #     mask: default
    #     interface: fxp0
    #     flags: <UP,GATEWAY,DONE,STATIC,PRCLONING>
    #     recvpipe  sendpipe  ssthresh  rtt,msec    mtu    weight    expire
    #           0         0         0         0      0         0         0

# Generated at 2022-06-13 01:29:54.632371
# Unit test for method get_interfaces_info of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_interfaces_info():
    pass


# Generated at 2022-06-13 01:29:59.846554
# Unit test for method get_options of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_options():
    generic = GenericBsdIfconfigNetwork()
    assert generic.get_options("") == []
    assert generic.get_options("<>") == []
    assert generic.get_options("<a>") == ['a']
    assert generic.get_options("<a,b>") == ['a', 'b']
    assert generic.get_options("<a,b,>") == ['a', 'b']
    assert generic.get_options("<a,b,c>") == ['a', 'b', 'c']
    assert generic.get_options("<a, b, c>") == ['a', 'b', 'c']
    assert generic.get_options("<a,b,c>extra") == ['a', 'b', 'c']



# Generated at 2022-06-13 01:30:01.620542
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():
    module = AnsibleModule(argument_spec={})
    network = GenericBsdIfconfigNetwork(module)
    collected_facts = None
    network.populate(collected_facts)
    assert network.platform == 'Generic_BSD_Ifconfig'


# Generated at 2022-06-13 01:30:02.209888
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():
    assert True

# Generated at 2022-06-13 01:30:07.686134
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():
    generic_bsd_ifconfig_network = GenericBsdIfconfigNetwork()
    generic_bsd_ifconfig_network.module = Parameters()
    generic_bsd_ifconfig_network.module.run_command = run_command_mock
    """ :type : Parameters """
    generic_bsd_ifconfig_network.module.get_bin_path = lambda x: x
    result = generic_bsd_ifconfig_network.populate(collected_facts={})
    assert result is not None
    assert 'interfaces' in result
    assert 'default_ipv4' in result
    assert 'default_ipv6' in result
    assert 'all_ipv4_addresses' in result
    assert 'all_ipv6_addresses' in result
    assert 'lo0' in result
    assert 'en1'

# Generated at 2022-06-13 01:30:29.620323
# Unit test for method parse_inet6_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet6_line():
    """Test GenericBsdIfconfigNetwork.parse_inet6_line"""
    # noinspection PyUnusedLocal
    def do_test(input, expected_current_if, expected_ips):
        """
        Function to call parser and check the result
        :param input: input line to parse
        :param current_if: a dictionary to check against
        :param ips: a dictionary to check against
        """
        current_if = {}
        ips = {}
        my_obj = BasicNetworkGenericBSDIfconfig()
        words = input.split()
        my_obj.parse_inet6_line(words=words, current_if=current_if, ips=ips)
        assert current_if == expected_current_if
        assert ips == expected_ips

    # Test for valid input

# Generated at 2022-06-13 01:30:39.469749
# Unit test for method get_options of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_options():
    def get_options(option_string):
        start = option_string.find('<') + 1
        end = option_string.rfind('>')
        if (start > 0) and (end > 0) and (end > start + 1):
            option_csv = option_string[start:end]
            return option_csv.split(',')
        else:
            return []

    assert get_options('flags=<UP,BROADCAST,RUNNING,SMART>') == ['UP', 'BROADCAST', 'RUNNING', 'SMART']
    assert get_options('options=<SMART>') == ['SMART']


# Generated at 2022-06-13 01:30:49.057276
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_default_interfaces():
    args = ['pci0:0', 'link#1', 'UC', '1234', '0x0', 'pci0', '10.0.0.1', '00:11:22:33:44:55', 'UHLWIi', '11', '99', '0']
    route_path = 'route'
    module = AnsibleModule(argument_spec={})
    module.run_command = MagicMock(return_value=(0, route_path + ' -n get %s\n' % ' '.join(args), ''))
    network = GenericBsdIfconfigNetwork(module)

    interface = network.get_default_interfaces(route_path)


# Generated at 2022-06-13 01:30:59.345322
# Unit test for method get_interfaces_info of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_interfaces_info():
    import json
    ifconfig_path = "/sbin/ifconfig"

    module = BSDIfconfigNetworkModule()
    module.get_bin_path = mock.MagicMock(return_value=ifconfig_path)
    module.run_command = mock.MagicMock(
        return_value=(0, (GENERIC_BSD_IFCONFIG_OUTPUT + GENERIC_BSD_IFCONFIG_OUTPUT6), ''))

    platform = 'Generic_BSD_Ifconfig'
    network = GenericBsdIfconfigNetwork(module, platform=platform)
    interfaces, ips = network.get_interfaces_info(ifconfig_path)

    assert len(ips) > 0
    assert len(interfaces) > 0
    assert len(ips['all_ipv4_addresses']) > 0
   

# Generated at 2022-06-13 01:31:07.353709
# Unit test for method parse_ether_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_ether_line():
    iface = {}
    line = "ether aa:bb:cc:dd:ee:ff"
    words = line.split()
    assert len(words) > 1
    network_test = GenericBsdIfconfigNetwork()
    network_test.parse_ether_line(words, iface, {})
    assert iface['macaddress'] == "aa:bb:cc:dd:ee:ff"
    assert iface['type'] == 'ether'


# Generated at 2022-06-13 01:31:16.261226
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():
    # Setup inventory data
    module = AnsibleModuleMock()
    module.run_command = MagicMock(return_value=(0, '', ''))
    module.get_bin_path = MagicMock(return_value='/var/bin/ifconfig')

    # Instantiate Network subclass and test method populate
    network = GenericBsdIfconfigNetwork(module)
    network.detect_type_media = MagicMock()
    network.get_interfaces_info = MagicMock()
    network.get_default_interfaces = MagicMock()
    network.merge_default_interface = MagicMock()
    network.populate()
    # It needs to call these methods
    network.get_interfaces_info.assert_called_once()
    network.get_default_interfaces.assert_called_once()
   

# Generated at 2022-06-13 01:31:25.667847
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():
    results = {'ansible_facts': {'all_ipv4_addresses': ['127.0.0.1', '192.168.59.106', '10.0.2.15'], 'all_ipv6_addresses': [], 'default_ipv4': {'address': '192.168.59.106', 'broadcast': '192.168.59.255', 'gateway': '192.168.59.2', 'interface': 'eth0', 'metric': '100', 'mtu': '1500', 'netmask': '255.255.255.0', 'network': '192.168.59.0', 'type': 'ether'}, 'default_ipv6': {}, 'interfaces': ['eth0', 'lo0']}}
    p = GenericBsdIfconfigNetwork()

# Generated at 2022-06-13 01:31:31.612275
# Unit test for method parse_inet_line of class GenericBsdIfconfigNetwork

# Generated at 2022-06-13 01:31:42.875207
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():
    default_if = dict(interface='lo0',
                      gateway='127.0.0.1')

# Generated at 2022-06-13 01:31:53.981723
# Unit test for method parse_ether_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_ether_line():
    generic_bsd_ifconfig_network = GenericBsdIfconfigNetwork()
    words = ['ether', 'b8:27:eb:9b:00:e6']
    current_if = {'device': 'device_name', 'ipv4': [], 'ipv6': [], 'type': 'unknown'}
    ips = dict(
        all_ipv4_addresses=[],
        all_ipv6_addresses=[],
    )
    # Act:
    generic_bsd_ifconfig_network.parse_ether_line(words, current_if, ips)

    # Assert:

# Generated at 2022-06-13 01:32:41.513268
# Unit test for method get_interfaces_info of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_interfaces_info():
    ifconfig_interfaces_info = {}

# Generated at 2022-06-13 01:32:49.904398
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():
    net = GenericBsdIfconfigNetwork()

    defaults = { 'interface':'lo0' }
    interfaces = {
        'lo0': {
            'ipv4': [
                { 'address':'127.0.0.1', 'netmask':'255.0.0.0' },
                { 'address':'127.0.0.1', 'netmask':'255.0.0.0' },
                { 'address':'127.0.0.1', 'netmask':'255.0.0.0' }
            ],
            'type': 'loopback', 'device': 'lo0', 'ipv6': []
        }
    }

    net.merge_default_interface(defaults, interfaces, 'ipv4')
    assert defaults['address'] == '127.0.0.1'

# Generated at 2022-06-13 01:32:59.596551
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():
    ifconf = GenericBsdIfconfigNetwork(MockModule(), None)

# Generated at 2022-06-13 01:33:03.704689
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():
    # TODO: Fix this test
    # Module import
    # import sys
    # sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + '/../..'))
    # from lib.modules.network.generic_bsd_ifconfig import GenericBsdIfconfigNetwork
    # from lib.module_utils.facts.network.base import NetworkCollector
    # from lib.module_utils.facts.network.generic_bsd import GenericBsd
    pass


# Generated at 2022-06-13 01:33:13.402299
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_default_interfaces():

    results = dict(
        v4='lo0',
        v6='lo0',
    )

    # Test FreeBSD
    route = unittest.mock.Mock()
    route.side_effect = [
        (0, "default 192.168.1.1 UGS 0 8192 em0\nproto rtnetlink scope link default dev em0\n", ""),
        (0, "default fe80:10:20:30:ffff:ffff:ffff:fffe UG 0 0 lo0\nproto rtnetlink scope link default dev lo0 weight 1\n", ""),
    ]

    facts = GenericBsdIfconfigNetwork(dict(module=unittest.mock.Mock(run_command=route))).get_default_interfaces()

# Generated at 2022-06-13 01:33:15.869526
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_default_interfaces():
    assert GenericBsdIfconfigNetwork.get_default_interfaces(None, '/sbin/route') == ({'interface': 'bge0', 'gateway': '10.10.10.1'}, {'interface': 'lo0', 'gateway': '::1'})


# Generated at 2022-06-13 01:33:27.561233
# Unit test for method get_interfaces_info of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_interfaces_info():
    from ansible_collections.ansible.community.tests.unit.compat import unittest
    from ansible_collections.ansible.community.plugins.modules.network.facts import GenericBsdIfconfigNetwork

    class TestGenericBsdIfconfigNetwork(unittest.TestCase):
        """
        Unit test class for the GenericBsdIfconfigNetwork module
        """
        def setUp(self):
            """
            Setup a test dictionary for the GenericBsdIfconfigNetwork class
            """

# Generated at 2022-06-13 01:33:38.318116
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_default_interfaces():
    module = AnsibleModule(argument_spec=dict())
    ifconfig = GenericBsdIfconfigNetwork(module=module)
    ifconfig_path = module.get_bin_path('ifconfig')
    if ifconfig_path is None:
        module.fail_json(msg='ifconfig not found in path')

    route_path = module.get_bin_path('route')
    if route_path is None:
        module.fail_json(msg='route not found in path')

    default_ipv4, default_ipv6 = ifconfig.get_default_interfaces(route_path)

    module.exit_json(
        default_ipv4=default_ipv4,
        default_ipv6=default_ipv6,
    )


# Generated at 2022-06-13 01:33:48.937663
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():
    GenericBsdIfconfigNetwork._module = AnsibleModuleMock()
    GenericBsdIfconfigNetwork._platform = 'Generic_BSD_Ifconfig'

    GenericBsdIfconfigNetwork._module.run_command = MagicMock(return_value=(0, 'a string', ''))
    assert GenericBsdIfconfigNetwork.populate() == {'all_ipv4_addresses': [], 'all_ipv6_addresses': [], 'interfaces': []}

    run_command = MagicMock(return_value=('', '', ''))
    GenericBsdIfconfigNetwork._module.run_command = run_command

    GenericBsdIfconfigNetwork._module.get_bin_path = MagicMock(return_value=None)
    assert GenericBsdIfconfigNetwork.populate() == {}

    # get_bin_path

# Generated at 2022-06-13 01:33:54.080746
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():
    root = GenericBsdIfconfigNetwork(
        module=AnsibleModule(
            argument_spec=dict()
        )
    )

    defaults = {
        'interface': 'lo0',
        'address': '127.0.0.1',
    }


# Generated at 2022-06-13 01:34:32.358143
# Unit test for method get_interfaces_info of class GenericBsdIfconfigNetwork

# Generated at 2022-06-13 01:34:42.449199
# Unit test for method populate of class GenericBsdIfconfigNetwork

# Generated at 2022-06-13 01:34:52.171968
# Unit test for method parse_media_line of class GenericBsdIfconfigNetwork

# Generated at 2022-06-13 01:35:02.716980
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():
    nm = GenericBsdIfconfigNetwork()
    nm.module = MagicMock()

# Generated at 2022-06-13 01:35:09.826389
# Unit test for method parse_media_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_media_line():
    network = GenericBsdIfconfigNetwork()
    # Test for no words
    current_if = {}
    ips = {}
    words = []
    network.parse_media_line(words, current_if, ips)
    assert 'media' not in current_if.keys()

    # Test for one word
    current_if = {}
    ips = {}
    words = ['media:']
    network.parse_media_line(words, current_if, ips)
    assert current_if['media'] == ''

    # Test for two words
    current_if = {}
    ips = {}
    words = ['media:', '1000baseT']
    network.parse_media_line(words, current_if, ips)
    assert current_if['media'] == '1000baseT'

    # Test for three

# Generated at 2022-06-13 01:35:14.998557
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():
    network = GenericBsdIfconfigNetwork()
    defaults = {'interface': 'em1'}
    # Test case with invalid interface name
    network.merge_default_interface(defaults, {}, 'ipv4')
    assert(defaults == {'interface': 'em1'})

    interfaces = {'em1': {'ipv4': [{'address': '192.168.1.1'}, {'address': '192.168.1.2'}]}}
    network.merge_default_interface(defaults, interfaces, 'ipv4')
    assert(defaults == {'interface': 'em1', 'ipv4': [{'address': '192.168.1.1'}, {'address': '192.168.1.2'}]})


# Generated at 2022-06-13 01:35:20.725728
# Unit test for method detect_type_media of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_detect_type_media():
    c = GenericBsdIfconfigNetwork()

# Generated at 2022-06-13 01:35:29.981367
# Unit test for method parse_inet_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet_line():
    from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork

# Generated at 2022-06-13 01:35:35.709880
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():
    GenericBsdIfconfigNetwork.get_interfaces_info = lambda s, p: ([], [], [])
    GenericBsdIfconfigNetwork.get_default_interfaces = lambda s, p: ([], [])

    module = AnsibleModule(
        argument_spec=dict(
            gather_subset=dict(default=['!all', '!min'], type='list')
        ),
        supports_check_mode=True
    )

    network = GenericBsdIfconfigNetwork()

    network.module = module

    result = network.populate()

    assert result == {}

# Generated at 2022-06-13 01:35:44.948052
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_default_interfaces():
    network_info = GenericBsdIfconfigNetwork()
    with open(os.path.join(os.path.dirname(__file__), 'route_output.txt'), 'r') as f:
        output = f.read()

    with mock.patch('os.path.exists') as mock_path_exists:
        with mock.patch('os.access') as mock_access:
            with mock.patch('ansible_collections.ansible.netcommon.plugins.module_utils.network.common.run_commands') as mock_run_commands:
                mock_path_exists.return_value = True
                mock_access.return_value = True
                mock_run_commands.return_value = [0, output, '']