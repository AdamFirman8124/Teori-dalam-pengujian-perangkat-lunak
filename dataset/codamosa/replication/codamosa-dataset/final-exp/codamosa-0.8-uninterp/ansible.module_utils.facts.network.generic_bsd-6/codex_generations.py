

# Generated at 2022-06-13 01:27:58.290533
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_default_interfaces():
    fake_module = type('', (object,), {'run_command': _run_command})
    network = GenericBsdIfconfigNetwork(fake_module)

    default_ipv4, default_ipv6 = network.get_default_interfaces('/fake/route')

    assert default_ipv4['interface'] == 'en0'
    assert default_ipv4['gateway'] == '192.0.2.1'
    assert default_ipv4['address'] == '192.0.2.2'
    assert default_ipv6['interface'] == 'en0'
    assert default_ipv6['gateway'] == '2001:db8::1'


# Generated at 2022-06-13 01:28:08.963266
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():
    module = AnsibleModule({})
    network = GenericBsdIfconfigNetwork(module)


# Generated at 2022-06-13 01:28:19.230018
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():
    # Unit test for method populate of class GenericBsdIfconfigNetwork
    # Todo : add checks for other attributes of the returned object
    # Todo : add a test for the case that bin/ifconfig does not exist
    # Todo : add a test for the case that bin/route does not exist
    # Todo : add a test for the case that bin/ifconfig returns non json data
    # Todo : add a test for the case that bin/route returns non json data
    from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork
    from ansible.module_utils.facts.network.base import NetworkCollector
    generic_bsd_ifconfig_network = GenericBsdIfconfigNetwork()
    network_collector = NetworkCollector()
    network_collector._module = Mock()
    network_

# Generated at 2022-06-13 01:28:30.357222
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_default_interfaces():

    class FakeModule(object):
        def __init__(self):
            self.run_command_args = []
            self.run_command_rc = 0
            self.run_command_out = []
            self.run_command_err = []

        def get_bin_path(self, arg):
            return arg

        def run_command(self, args):
            self.run_command_args.append(args)
            rc = self.run_command_rc[args[0]]
            out = self.run_command_out[args[0]]
            err = self.run_command_err[args[0]]
            return rc, out, err

    fake_module = FakeModule()

    # set up a fake route output
    fake_module.run_command_rc['route'] = 0
    fake_module.run

# Generated at 2022-06-13 01:28:32.917764
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():
    facts = GenericBsdIfconfigNetwork().populate()
    assert 'interfaces' in facts
    assert 'all_ipv4_addresses' in facts
    assert 'all_ipv6_addresses' in facts


# Generated at 2022-06-13 01:28:38.912791
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():
    # Create a mock module
    module = AnsibleModule(
        argument_spec = dict(
            gather_subset = dict(type='list', required=False),
        ),
        supports_check_mode=True
    )
    # Set values for test
    ifconfig_path = module.get_bin_path('ifconfig')
    route_path = module.get_bin_path('route')

    if ifconfig_path is None:
        return

    if route_path is None:
        return

    # Create an instance of the GenericBsdIfconfigNetwork class
    facter_network = GenericBsdIfconfigNetwork(module)

    # get_default_interfaces()
    default_ipv4, default_ipv6 = facter_network.get_default_interfaces(route_path)

    # Populate facts
   

# Generated at 2022-06-13 01:28:49.441729
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():

    # Set up a mock module
    module = AnsibleModule(argument_spec={'gather_subset': {'choices': ['all', 'min'], 'required': True, 'type': 'list'}})

    # Set up a mock task
    task = mock.Mock()

    # Set up a mock shared object
    mock_ansible_module = mock.Mock()
    mock_ansible_module.params = module.params

    # Instantiate the class under test
    netinfogroup = GenericBsdIfconfigNetwork()

    # Invoke the populate method
    netinfogroup.populate(mock_ansible_module)

# Generated at 2022-06-13 01:28:58.807527
# Unit test for method detect_type_media of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_detect_type_media():
    network = GenericBsdIfconfigNetwork()

# Generated at 2022-06-13 01:29:09.868474
# Unit test for method parse_inet6_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet6_line():
    interface_fixture_1 = dict()
    ips_fixture_1 = dict()
    GenericBsdIfconfigNetwork().parse_inet6_line(["inet6", "fe80::1%lo0", "prefixlen", "64", "scopeid", "0x2"], interface_fixture_1, ips_fixture_1)
    assert interface_fixture_1 == dict()
    assert ips_fixture_1 == dict(
        all_ipv6_addresses=['fe80::1%lo0'],
    )
    interface_fixture_2 = dict()
    ips_fixture_2 = dict()

# Generated at 2022-06-13 01:29:18.372754
# Unit test for method get_interfaces_info of class GenericBsdIfconfigNetwork

# Generated at 2022-06-13 01:29:46.412460
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_default_interfaces():
    from collections import namedtuple
    module = namedtuple('module', ['run_command', 'fail_json'])
    module.run_command = lambda *args, **kwargs: (0, '', '')
    platform = GenericBsdIfconfigNetwork(module)

    # Test with FreeBSD
    platform.run_command = lambda *args, **kwargs: (
        0, 'default 192.168.1.1 UGS 0 100000 em0', '')
    default_ipv4, default_ipv6 = platform.get_default_interfaces('/sbin/route')
    assert 'interface' in default_ipv4
    assert 'gateway' in default_ipv4
    assert default_ipv4['interface'] == 'em0'

# Generated at 2022-06-13 01:29:56.518169
# Unit test for method get_interfaces_info of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_interfaces_info():
    test_module = AnsibleModule(argument_spec=dict())

    # Use the test data below to mimic the ifconfig output.
    def test_get_bin_path(name):
        return None

    # Entire test class is module_scope but only create_instance is
    # accessed in the method that we are testing below.
    def create_instance(cls):
        return GenericBsdIfconfigNetwork()

    from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork

    # The example data is from a FreeBSD 10.3 system

# Generated at 2022-06-13 01:30:06.328398
# Unit test for method detect_type_media of class GenericBsdIfconfigNetwork

# Generated at 2022-06-13 01:30:13.001413
# Unit test for method parse_inet_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet_line():
    test_obj = GenericBsdIfconfigNetwork({}, None)
    test_line = 'inet 10.20.30.40 netmask 0xffffff00 broadcast 10.20.30.255'
    test_words = test_line.split()
    test_interface = {'device': 'lo0', 'ipv4': [], 'ipv6': [], 'type': 'unknown'}
    test_ips = dict(
        all_ipv4_addresses=[],
        all_ipv6_addresses=[],
    )
    test_obj.parse_inet_line(test_words, test_interface, test_ips)
    assert test_interface['ipv4'][0]['address'] == '10.20.30.40'

# Generated at 2022-06-13 01:30:23.136706
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_default_interfaces():
    cls = GenericBsdIfconfigNetwork
    ifconfig_path = 'tests/unit/modules/network/ifconfig'
    mocker = Mocker()
    module = mocker.mock()
    plugin_get_bin_path = mocker.replace('ansible.module_utils.basic.AnsibleModule.get_bin_path')
    mock_module_run_command = mocker.replace('ansible.module_utils.basic.AnsibleModule.run_command')
    plugin_get_bin_path(module, 'route')
    mock_module_run_command(['route', '-n', 'get', 'default'])
    mocker.result(True)
    mocker.result(b"""default: gateway 192.168.0.1""")
    mocker.count(0, None)
    plugin_

# Generated at 2022-06-13 01:30:26.073583
# Unit test for method parse_inet_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet_line():
    G = GenericBsdIfconfigNetwork(dict(module=AnsibleModule()))

    # Test for IPV4
    words = ['lo0', 'inet', '127.0.0.1', 'netmask', '0xff000000']
    current_if = d

# Generated at 2022-06-13 01:30:35.055627
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_default_interfaces():
    ifconfig_path = '/sbin/ifconfig'
    # route_path = './fixtures/GenericBsdIfconfigNetwork_route_listing'
    route_path = '/sbin/route'
    cmd_results = {route_path: dict(stdout='default\nadd via 192.168.1.254\nadd default 192.168.1.254\n', stderr='')}
    module_args = {}
    generic_bsd_network = GenericBsdIfconfigNetwork(module_args, cmd_results)
    result = dict()
    result = generic_bsd_network.get_default_interfaces(route_path)
    # I am not sure if this is the best way to print, but it does work.
    for key in result:
        print(key, result[key])


# Unit test

# Generated at 2022-06-13 01:30:46.669506
# Unit test for method parse_inet_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet_line():
    """GenericBsdIfconfigNetwork:Unit test for method parse_inet_line"""
    module = unittest.mock.MagicMock()
    module.run_command = MagicMock(return_value=(0, "", ""))
    module.get_bin_path = MagicMock(return_value="/sbin/ifconfig")
    inst = GenericBsdIfconfigNetwork(module)

    current_if = dict()
    ips = dict()
    words = list()
    words.append('inet')
    words.append('127.0.0.1')
    words.append('netmask')
    words.append('0xff000000')
    words.append('broadcast')
    words.append('127.0.0.1')
    inst.parse_inet_line(words, current_if, ips)
   

# Generated at 2022-06-13 01:30:50.411318
# Unit test for method get_interfaces_info of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_interfaces_info():
    bcni = GenericBsdIfconfigNetwork()

    # Create a GenericBsdIfconfigNetwork instance
    assert isinstance(bcni, GenericBsdIfconfigNetwork)



# Generated at 2022-06-13 01:31:00.105187
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_default_interfaces():
    G = GenericBsdIfconfigNetwork

# Generated at 2022-06-13 01:31:10.513832
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():
    pass
    # TODO: implement this unit test.


# Generated at 2022-06-13 01:31:15.215201
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_default_interfaces():
    module = AnsibleModule(argument_spec=dict())
    gbin = GenericBsdIfconfigNetwork(module)
    ipv4_default, ipv6_default = gbin.get_default_interfaces()
    assert 'interface' in ipv4_default, 'Got %s' % ipv4_default
    assert 'interface' in ipv6_default, 'Got %s' % ipv6_default

# Generated at 2022-06-13 01:31:24.895700
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():
    from test_utils import AnsibleExitJson, AnsibleFailJson
    from ansible.module_utils.basic import AnsibleModule

    class TestAnsibleModule(AnsibleModule):
        """ Test AnsibleModule """
        def __init__(self, *args, **kwargs):
            super(TestAnsibleModule, self).__init__(*args, **kwargs)
            self._module = None
            self._id = None
            self._name = None
            self._ifaces = None

        @property
        def id(self):
            return self._id

        @id.setter
        def id(self, value):
            self._id = value

        @property
        def name(self):
            return self._name

        @name.setter
        def name(self, value):
            self._name

# Generated at 2022-06-13 01:31:30.906361
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_default_interfaces():
    module = AnsibleModule(argument_spec=dict())
    processor = GenericBsdIfconfigNetwork(module)

# Generated at 2022-06-13 01:31:33.763145
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():
    assert GenericBsdIfconfigNetwork.merge_default_interface(
        'default_ipv4',
        'interfaces',
        'ip_type'
    ) is None


# Generated at 2022-06-13 01:31:42.654004
# Unit test for method get_options of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_options():
    network_obj = GenericBsdIfconfigNetwork()
    assert network_obj.get_options("") == []
    assert network_obj.get_options("something something") == []
    assert network_obj.get_options("<>") == []
    assert network_obj.get_options("<a,b>") == ["a","b"]
    assert network_obj.get_options("<a,b,c>") == ["a","b","c"]
    assert network_obj.get_options("DELAY <a,b,c>") == ["a","b","c"]
    assert network_obj.get_options("DELAY <a,b,c") == []
    assert network_obj.get_options("DELAY a,b,c>") == []

# Generated at 2022-06-13 01:31:53.879804
# Unit test for method get_options of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_options():
    invalid_inputs = [
        [
            dict(option_string=''),
            dict(option_string='<>'),
            dict(option_string='<OPT1,OPT2>'),
            dict(option_string='OPT1,OPT2>')
        ]
    ]
    for inputs in invalid_inputs:
        for test in inputs:
            obj = GenericBsdIfconfigNetwork()
            actual_output = obj.get_options(test['option_string'])
            assert [] == actual_output

    valid_inputs = [
        dict(option_string='<OPT1,OPT2>', expected_output=['OPT1', 'OPT2'])
    ]
    for test in valid_inputs:
        obj = GenericBsdIfconfigNetwork()
        actual_output = obj

# Generated at 2022-06-13 01:31:56.940659
# Unit test for method get_options of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_options():
    ifn = GenericBsdIfconfigNetwork()
    assert ifn.get_options('<UP,LOOPBACK,RUNNING,MULTICAST>') == ['UP', 'LOOPBACK', 'RUNNING', 'MULTICAST']
    assert ifn.get_options('<UP,LOOPBACK,RUNNING,MULTICAST') == []
    assert ifn.get_options('<>') == []


# Generated at 2022-06-13 01:32:08.733942
# Unit test for method get_interfaces_info of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_interfaces_info():
    # Case 1: FreeBSD 9.0-RELEASE
    ifconfig_path = [os.path.dirname(__file__), '..', 'ifconfig_outputs', 'FreeBSD', '9.0-RELEASE']
    ifconfigCommand = [os.path.join('/', *ifconfig_path)]
    commandResult = dict(rc=0, out=None, err=None)
    cmd = os.path.join('/', *ifconfigCommand)
    rc, out, err = commandResult['rc'], commandResult['out'], commandResult['err']
    if not os.path.exists(cmd):
        import epdb; epdb.st()
    with open(cmd) as f:
        commandResult['out'] = str.format("{0}", f.read())

# Generated at 2022-06-13 01:32:17.907145
# Unit test for method parse_inet_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet_line():
    module = AnsibleModule(argument_spec=dict())
    nm = GenericBsdIfconfigNetwork(module)

    words = ['em0', 'flags=8843<UP,BROADCAST,RUNNING,SIMPLEX,MULTICAST>', 'metric', '0', 'mtu', '1500', 'inet', '192.168.1.1', 'netmask', '0xffffff00', 'broadcast', '192.168.1.255', 'ether', 'aa:bb:cc:dd:ee:ff']
    iface = nm.parse_interface_line(words)

# Generated at 2022-06-13 01:32:26.869852
# Unit test for method get_interfaces_info of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_interfaces_info():
    pass


# Generated at 2022-06-13 01:32:36.666657
# Unit test for method get_interfaces_info of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_interfaces_info():
    from ansible_collections.notstdlib.moveitallout.tests.unit.compat import unittest
    from ansible_collections.notstdlib.moveitallout.tests.unit.compat.mock import patch
    from ansible.module_utils.facts import Network
    from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork

    mock_module = type('module', (object,), {})()
    mock_module.run_command = lambda *_, **__: (0, "", "")
    mock_module.get_bin_path = lambda _: '/sbin/ifconfig'
    ifconfig_path = mock_module.get_bin_path('ifconfig')
    mock_module.boolean = True


# Generated at 2022-06-13 01:32:45.319333
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():
    module = AnsibleModule(argument_spec={})
    module.exit_json = exit_json
    module.fail_json = fail_json
    network = GenericBsdIfconfigNetwork(module)

    # TODO: find better way to test?

    if platform.system() != 'FreeBSD':
        module.fail_json(msg='GenericBSD tests can only run on freebsd')

    result = network.populate()

    if len(result['interfaces']) == 0:
        module.fail_json(msg='No interfaces found)')

    if 'default_ipv4' not in result:
        module.fail_json(msg='No default_ipv4 interface found')

    if 'default_ipv6' not in result:
        module.fail_json(msg='No default_ipv6 interface found')


# Generated at 2022-06-13 01:32:51.995712
# Unit test for method detect_type_media of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_detect_type_media():

    # Test 1:
    # Setup
    interfaces = {'en0': {'device': 'en0', 'ipv4': [], 'ipv6': [], 'type': 'unknown', 'flags': ['UP'], 'macaddress': 'unknown', 'metric': '0', 'mtu': '1500'},
                  'lo0': {'device': 'lo0', 'ipv4': [], 'ipv6': [], 'type': 'loopback', 'flags': ['UP'], 'macaddress': 'unknown', 'metric': '0', 'mtu': '33184'}}
    # Exercise
    interfaces = GenericBsdIfconfigNetwork.detect_type_media(interfaces)
    # Verify

# Generated at 2022-06-13 01:33:00.589969
# Unit test for method parse_interface_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_interface_line():
    parser = GenericBsdIfconfigNetwork()

    network_facts = {}
    current_if = {}

    # Test the data which contains the metric and mtu
    words = "bge0: flags=8843<UP,BROADCAST,RUNNING,SIMPLEX,MULTICAST> metric 0 mtu 1500".split()
    current_if = parser.parse_interface_line(words)
    assert current_if['device'] == 'bge0'
    assert current_if['flags'] == ['UP', 'BROADCAST', 'RUNNING', 'SIMPLEX', 'MULTICAST']
    assert current_if['metric'] == '0'
    assert current_if['mtu'] == '1500'
    assert current_if['type'] == 'unknown'

    # Test the data which does not contain the metric
    words

# Generated at 2022-06-13 01:33:12.024529
# Unit test for method parse_inet6_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet6_line():
    _network = GenericBsdIfconfigNetwork()
    _current_if = {}

    ### Test for 2 cases:
    ###  a) valid prefix length
    ###  b) invalid prefix length

    _words = ['inet6', 'fe80:1:2:3::4', 'prefixlen', '64', 'scopeid', '0x5']
    _network.parse_inet6_line(_words, _current_if, {'all_ipv6_addresses': []})
    assert _current_if == {'device': '', 'ipv4': [], 'ipv6': [{'address': 'fe80:1:2:3::4', 'prefix': '64', 'scope': '0x5'}], 'type': 'unknown', 'macaddress': 'unknown'}


# Generated at 2022-06-13 01:33:23.649764
# Unit test for method parse_inet6_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet6_line():
    module = AnsibleModule(argument_spec={})
    facts = GenericBsdIfconfigNetwork(module)
    current_if = {}
    ips = {'all_ipv6_addresses': []}
    # Format of output from ifconfig command on NetBSD
    words = ['inet6', 'fe80::20c:29ff:fe3f:4d4c', 'prefixlen', '64', 'scopeid', '0x2', 'inet6', 'fe80::20c:29ff:fe3f:4d4d', 'prefixlen', '64', 'scopeid', '0x2']
    facts.parse_inet6_line(words, current_if, ips)

# Generated at 2022-06-13 01:33:35.547496
# Unit test for method parse_inet_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet_line():
    '''
    Test parsing of ipv4 addresses
    '''
    input_data = [
        "127.0.0.1/24",
        "127.0.0.1",
        "127.0.0.1 netmask 0xff000000",
        "127.0.1.1 alias 127.0.0.1",
        "127.0.1.1 netmask 0xff000000 alias 127.0.0.1",
        "127.0.1.1 netmask 0xff000000 broadcast 127.255.255.255",
    ]


# Generated at 2022-06-13 01:33:41.634524
# Unit test for method detect_type_media of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_detect_type_media():
    import pytest
    import ansible.module_utils.network.bsd

    assert(hasattr(GenericBsdIfconfigNetwork, 'detect_type_media'))

    assert(callable(GenericBsdIfconfigNetwork.detect_type_media))

    assert(isinstance(GenericBsdIfconfigNetwork.detect_type_media, Callable))



# Generated at 2022-06-13 01:33:50.503790
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():
    from ansible.module_utils.network.freebsd.facts.network.generic_bsd_ifconfig import GenericBsdIfconfigNetwork

    module = AnsibleModule(argument_spec={})

    # Test Interface options
    # Test Option flags
    assert 'UP' in GenericBsdIfconfigNetwork.get_options('<LOOPBACK,UP,LOWER_UP>')
    assert 'LOOPBACK' in GenericBsdIfconfigNetwork.get_options('<LOOPBACK,UP,LOWER_UP>')
    assert 'LOWER_UP' in GenericBsdIfconfigNetwork.get_options('<LOOPBACK,UP,LOWER_UP>')
    assert 'UP' not in GenericBsdIfconfigNetwork.get_options('<LOOPBACK,LOWER_UP>')
    # Test Max length

# Generated at 2022-06-13 01:34:25.478760
# Unit test for method detect_type_media of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_detect_type_media():
    f_module = FakeModule()
    f_module.params = {}
    interfaces = {}
    interfaces['eth0'] = {}
    interfaces['eth0']['media'] = 'Ethernet'
    interfaces['eth0']['type'] = 'unknown'
    interfaces['lo0'] = {}
    interfaces['lo0']['media'] = 'Local Loopback'
    interfaces['lo0']['type'] = 'loopback'
    interfaces['wlan0'] = {}
    interfaces['wlan0']['media'] = 'Ethernet'
    interfaces['wlan0']['type'] = 'unknown'
    gbn = GenericBsdIfconfigNetwork(f_module)
    result = gbn.detect_type_media(interfaces)

# Generated at 2022-06-13 01:34:33.501793
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():
    testmod_GenericBsdIfconfigNetwork = FakeModule()
    testobj = GenericBsdIfconfigNetwork(testmod_GenericBsdIfconfigNetwork)

    # ------- Test Invalid Paths -------
    invalid_route_path = None
    invalid_ifconfig_path = None

    # ------- Test Invalid Paths -------
    testmod_GenericBsdIfconfigNetwork.run_command = FakeRunCommand(
        stdout=None,
        stderr=None,
        rc=0
    )

    network_facts = testobj.populate(collected_facts=None)
    assert network_facts == {}

    # ------- Test no IPv6 -------

# Generated at 2022-06-13 01:34:43.415028
# Unit test for method parse_inet6_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet6_line():

    g = GenericBsdIfconfigNetwork()

    # test normal inet6 line
    current_if = {}
    ips = dict(
        all_ipv6_addresses=[],
    )
    g.parse_inet6_line(['inet6', 'fe80::9e2f:dfff:fe7b:8c0f%lo0', 'prefixlen', '64', 'scopeid', '0x1'],
                    current_if, ips)
    assert len(ips['all_ipv6_addresses']) == 1, len(ips['all_ipv6_addresses'])
    assert ips['all_ipv6_addresses'][0] == 'fe80::9e2f:dfff:fe7b:8c0f'

    # test old style inet6 netbsd

# Generated at 2022-06-13 01:34:52.912640
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():
    import ast
    import platform
    import re
    import os
    import tempfile

    #
    # ifconfig -a
    #

# Generated at 2022-06-13 01:35:03.471725
# Unit test for method detect_type_media of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_detect_type_media():
    # This is a stub that you can use to test your function
    # assert func(args) == 'foo'
    printer("Testing: GenericBsdIfconfigNetwork_detect_type_media")
    obj = GenericBsdIfconfigNetwork()

# Generated at 2022-06-13 01:35:12.573278
# Unit test for method get_interfaces_info of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_interfaces_info():
    module = AnsibleModule(
        argument_spec={},
        supports_check_mode=True,
    )

    module.exit_json = Mock()


# Generated at 2022-06-13 01:35:19.664322
# Unit test for method parse_interface_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_interface_line():
    result = GenericBsdIfconfigNetwork.parse_interface_line(None, ['eth0: flags=8843<UP,BROADCAST,RUNNING,SIMPLEX,MULTICAST> metric 0 mtu 1500', 'options=9<RXCSUM,VLAN_MTU>', 'ether 00:01:02:03:04:05', 'inet6 fe80::201:2ff:fe03:405%eth0 prefixlen 64 scopeid 0x1', 'inet 10.0.0.1 netmask 0xffffff00 broadcast 10.0.0.255', 'nd6 options=21<PERFORMNUD,AUTO_LINKLOCAL>', 'media: Ethernet autoselect (1000baseT <full-duplex>)', 'status: active'])

# Generated at 2022-06-13 01:35:29.094994
# Unit test for method parse_inet_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet_line():
    GenericBsdIfconfigNetwork.parse_inet_line(['inet', '127.0.0.1', 'netmask', '0xff000000', 'mtu', '16436'], {}, None)
    GenericBsdIfconfigNetwork.parse_inet_line(['inet', '127.0.1.1', 'netmask', '0xff000000', 'mtu', '16436'], {}, None)
    GenericBsdIfconfigNetwork.parse_inet_line(['inet', '10.0.0.1', 'netmask', '0xffffff00', 'mtu', '16436'], {}, None)
    GenericBsdIfconfigNetwork.parse_inet_line(['inet', '10.0.0.2', 'netmask', '0xffffff00', 'mtu', '16436'], {}, None)

# Generated at 2022-06-13 01:35:36.430525
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():
    # Mock data
    ifconfig_data = load_fixture('ifconfig')
    route_data = load_fixture('route')
    # Mock module
    module = AnsibleModule(argument_spec=dict())
    # Mock module functions
    module.get_bin_path = Mock(side_effect=['/sbin/ifconfig', '/sbin/route'])
    module.run_command = Mock(side_effect=[(0,ifconfig_data,''),(0,route_data,'')])
    # Unit test
    network = BSDIfconfigNetwork(module)
    result = network.populate()
    # Assert test data

# Generated at 2022-06-13 01:35:45.658224
# Unit test for method parse_inet_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet_line():
    test_class = GenericBsdIfconfigNetwork()