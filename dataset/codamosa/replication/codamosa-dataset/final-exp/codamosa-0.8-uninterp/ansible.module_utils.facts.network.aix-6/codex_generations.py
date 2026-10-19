

# Generated at 2022-06-13 01:16:59.308750
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    # testing AIXNetwork.get_interfaces_info() method
    # this test is compatible with the network/generic_bsd/test_bsd.py test_bsd.test_bsd_get_interfaces_info()
    interfaces = {}
    current_if = {}
    ips = dict(
        all_ipv4_addresses=[],
        all_ipv6_addresses=[],
    )


# Generated at 2022-06-13 01:17:09.372913
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():

    testobj = AIXNetwork()

    # case 1
    route_path_1 = '/bin/netstat'
    expected_result1 = dict(v4={}, v6={})
    expected_result1['v4']['gateway'] = '10.10.10.1'
    expected_result1['v4']['interface'] = 'en0'
    expected_result1['v6']['gateway'] = 'ffff::1'
    expected_result1['v6']['interface'] = 'en0'

    testobj.module = AnsibleModuleMock()

# Generated at 2022-06-13 01:17:10.434587
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    assert AIXNetworkCollector._platform == 'AIX'


# Generated at 2022-06-13 01:17:23.237119
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    def mock_run_command(self, command, check_rc=True):
        if command == ['/sbin/netstat', '-nr']:
            return (0, 'default 172.31.1.1 UG 0 5 ent0\ndefault 172.31.1.1 UG 0 5 ent0\ndefault fe80::1%ent0 UG 0 5 ent0\n', '')
        else:
            raise Exception('Unknown command: %s' % command)


# Generated at 2022-06-13 01:17:26.223878
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    """
    Test whether AIX Network Collector class can be initialized
    """

    AIXNetworkCollector()

# Unit test of function AIXNetworkCollector.collect()

# Generated at 2022-06-13 01:17:32.753747
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    ans_module = MockAnsibleModule()
    net = AIXNetwork(ans_module)

    for device, routes in AIX_ROUTES.items():
        interfaces = AIX_INTERFACES[device]
        v4_result, v6_result = net.get_default_interfaces(routes)
        assert v4_result == interfaces['v4']
        assert v6_result == interfaces['v6']



# Generated at 2022-06-13 01:17:35.832653
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    platform_name = 'AIX'
    fact_class = AIXNetwork
    fact_collector = AIXNetworkCollector()

    assert fact_collector._platform == platform_name
    assert fact_collector._fact_class == fact_class

# Generated at 2022-06-13 01:17:42.893274
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():

    import pdb
    #pdb.set_trace()

    class NetworkModuleMock:
        def __init__(self):
            self.params = {}
            self.exit_json = None
            self.run_command_paths = {'ifconfig': 'ifconfig.mock', 'netstat': 'netstat.mock', 'uname': 'uname.mock'}
            self.run_command_calls = []

        def get_bin_path(self, name, opt_dirs=[]):
            return self.run_command_paths[name]

        def run_command(self, args, check_rc=True):
            with open(args[0], 'r') as f:
                contents = f.read()
            self.run_command_calls.append((args, contents))
            return

# Generated at 2022-06-13 01:17:54.822238
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    module = ansible_module_mock()
    net = AIXNetwork(module)
    ifconfig_path = net.module.get_bin_path('ifconfig')

# Generated at 2022-06-13 01:17:56.932276
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    # Constructor of class
    obj = AIXNetworkCollector()
    assert obj
    assert isinstance(obj, AIXNetworkCollector)


# Generated at 2022-06-13 01:18:11.444425
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    assert AIXNetworkCollector._platform == 'AIX'
    assert AIXNetworkCollector._fact_class == AIXNetwork
    assert AIXNetworkCollector.platform == 'AIX'


# Generated at 2022-06-13 01:18:12.612317
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    assert AIXNetworkCollector(dict(module=dict()))._platform == 'AIX'

# Generated at 2022-06-13 01:18:19.740311
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():

    class module:
        def __init__(self, path=None):
            self.path = path

        def get_bin_path(self, name=None, opt_dirs=None):
            if name == 'netstat':
                # return path to netstat
                return '/bin/netstat'
            else:
                return None

        def run_command(self, cmd=None, check_rc=True):
            # return the output of the command
            cmd = ' '.join(cmd)

# Generated at 2022-06-13 01:18:29.056917
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    """
    Unit test for method get_interfaces_info of class AIXNetwork
    """
    from ansible.module_utils.facts.network import NetworkCollector


# Generated at 2022-06-13 01:18:39.856828
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    module = AnsibleModule(
        argument_spec=dict(
            gather_subset=dict(type='list', default=['!all']),
            gather_network_resources=dict(type='list', choices=['all', '!all'], default=['all'])
        ),
        supports_check_mode=True)

    net = AIXNetwork(module)
    # Create an instance of AIXNetwork with mocked route_path
    net.route_path = os.path.join(os.path.dirname(__file__),
                                  'unit/ansible_collections/ansible/community/plugins/module_utils/facts/network/files/route')

    # Expected results
    expected = net.default_gateways()
    # Use get_default_interfaces to compare results

# Generated at 2022-06-13 01:18:42.603037
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    fc = AIXNetwork(dict())
    assert len(fc.get_interfaces_info('/usr/sbin/ifconfig')[0]) > 0


# Generated at 2022-06-13 01:18:53.323350
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    # set up test class instance
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True)
    testclass = AIXNetwork(module=module, warnings=[])
    # simulate success of 'which ifconfig' command
    # testclass.module.get_bin_path = lambda _: '/usr/sbin/ifconfig'

    # set up call parameters
    ifconfig_path='/usr/sbin/ifconfig'
    ifconfig_options='-a'

    # simulate ifconfig output

# Generated at 2022-06-13 01:19:01.204792
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():

    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )

    network = AIXNetwork(module)

    rc, out, err = module.run_command([network.route_path, '-n'])

    lines = out.splitlines()
    for line in lines:
        words = line.split()
        if len(words) > 1 and words[0] == 'default':
            if '.' in words[1]:
                gateway_ipv4 = words[1]
                interface_ipv4 = words[5]
            elif ':' in words[1]:
                gateway_ipv6 = words[1]
                interface_ipv6 = words[5]

    interfaces = network.get_default_interfaces(network.route_path)


# Generated at 2022-06-13 01:19:08.259077
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    """
    Constructor test: Check return value of constructor.
    """
    os_platform = 'AIX'
    os_version = '7.1'
    ansible_module = None

    network_collector = AIXNetworkCollector(os_platform, os_version, ansible_module)

    assert network_collector._facts_class.platform is 'AIX', 'Value of attribute _fact_class.platform is not \'AIX\''
    assert network_collector._platform is 'AIX', 'Value of attribute _platform is not \'AIX\''

# Generated at 2022-06-13 01:19:15.759736
# Unit test for method get_interfaces_info of class AIXNetwork

# Generated at 2022-06-13 01:19:48.675976
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    fact_list = [
        'ansible_all_ipv4_addresses',
        'ansible_all_ipv6_addresses',
        'ansible_default_ipv4',
        'ansible_default_ipv6',
        'ansible_interface_ip',
        'ansible_interfaces',
        'ansible_machine',
        'ansible_os_family',
        'ansible_pkg_mgr',
        'ansible_user_dir',
        'ansible_userspace_bits'
    ]
    nc = AIXNetworkCollector(fact_list)
    assert nc is not None
    assert nc.fact_class is not None
    assert nc.platform == 'AIX'
    assert nc.fact_class.platform == 'AIX'

# Generated at 2022-06-13 01:19:57.193700
# Unit test for method get_interfaces_info of class AIXNetwork

# Generated at 2022-06-13 01:20:08.255861
# Unit test for method get_interfaces_info of class AIXNetwork

# Generated at 2022-06-13 01:20:10.832281
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    net_collector = AIXNetworkCollector()

    assert(net_collector._platform == 'AIX')
    assert(net_collector._fact_class == AIXNetwork)


# Generated at 2022-06-13 01:20:17.867894
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    """
    This is the test for method get_default_interfaces of class AIXNetwork.
    """
    my_AIXNetwork = AIXNetwork()
    result = my_AIXNetwork.get_default_interfaces('/sbin/route')
    print(result)
    # TODO: write test for
    #       result[0] = {'interface': 'en5'}
    #       result[1] = {'gateway': 'fe80::f00', 'interface': 'en5'}
    return


# Generated at 2022-06-13 01:20:24.595351
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    from types import ModuleType
    class MockModule(ModuleType):
        def run_command(self, args):
            if args == ['netstat', '-nr']:
                return 0, '''\
Kernel IP routing table
Destination Gateway Flags Refs Use If Exp Groups
default 10.0.0.254 UG 0 3 en2
default 10.0.0.254 UG 0 0 en1
default ::1 UG 0 0 lo0
default 2001:db8::a UG 0 0 en2
''', ''
            if args == ['netstat', '-nr']:
                return 1, '', ''
            raise Exception('Unexpected call to run_command')

        def get_bin_path(self, app, required=False):
            if app == 'netstat':
                return '/opt/freeware/bin/netstat'


# Generated at 2022-06-13 01:20:27.955902
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    from ansible.module_utils.facts.network.aix import AIXNetworkCollector
    network_collector = AIXNetworkCollector()

# Generated at 2022-06-13 01:20:31.306161
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    """Unit test for constructor of class AIXNetworkCollector"""

    collector = AIXNetworkCollector()
    assert collector is not None
    assert isinstance(collector, NetworkCollector)
    assert isinstance(collector._fact_class, AIXNetwork)

# Generated at 2022-06-13 01:20:41.623170
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():

    from ansible.module_utils.facts.network.generic_bsd import NetworkModule
    from ansible.module_utils.facts.network.aix import AIXNetwork
    from ansible.module_utils.facts.network.posix import get_file_content
    import tempfile
    import os

    class NetworkModuleTest(NetworkModule):
        def __init__(self):
            self.tmpdir = tempfile.mkdtemp(prefix='ansible_unittests.')
            self.filename = os.path.join(self.tmpdir, 'netstat')
            with open(self.filename, 'w') as f:
                f.write(get_file_content('unit/network/files/netstat.out'))

        def get_bin_path(self, cmd, required=False):
            return self.filename

   

# Generated at 2022-06-13 01:20:48.955824
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    import os
    from ansible.module_utils._text import to_bytes

    # Constructor of class AIXNetworkCollector must set default values of 
    # following instance variables.
    mod = 'ansible.module_utils.facts.network.aix.AIXNetworkCollector'
    mod = __import__(mod, fromlist=[''])
    cls = getattr(mod, 'AIXNetworkCollector')

    # Default value of _fact_class
    fact_class = cls._fact_class
    assert fact_class == 'ansible.module_utils.facts.network.aix.AIXNetwork'

    # Default value of _platform
    platform = cls._platform
    assert platform == 'AIX'

    # Default value of _ignore_interface_list
    ignore_interface_list = cls.ignore_interface

# Generated at 2022-06-13 01:21:35.701457
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    test_module = NetworkCollector()
    aixnetwork = AIXNetwork(test_module)
    aixnetwork.get_default_interfaces('')



# Generated at 2022-06-13 01:21:42.512976
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )
    network_collector = AIXNetworkCollector(module=module)
    assert network_collector.platform == 'AIX'
    assert network_collector.fact_class.platform == 'AIX'
    assert network_collector.config == {}
    assert type(network_collector.facts) == dict
    assert type(network_collector.facts['all_ipv4_addresses']) == list
    assert type(network_collector.facts['interfaces']) == dict
    assert type(network_collector.facts['default_ipv4']) == dict


# Generated at 2022-06-13 01:21:48.108139
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    from ansible.module_utils.facts.aix.network.aix import AIXNetwork
    net = AIXNetwork()
    net.module = MockModule()
    ret = net.get_default_interfaces("/path/to/route")
    assert ret[0]['interface'] == 'en6'
    assert ret[0]['gateway'] == '172.16.0.1'
    assert ret[1]['interface'] == 'en6'
    assert ret[1]['gateway'] == '2001:db8:a:1::1'


# Generated at 2022-06-13 01:21:55.530978
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    netfacts = AIXNetwork()
    netfacts.module = FakeModule()
    netfacts.module.run_command = run_command_mock

    test_data = dict(
        test_data_1 = (
            dict(route_path='route'),
            dict(v4=dict(gateway='192.168.1.1', interface='en0'), v6=dict(gateway='2001:0db8:85a3:08d3:1319:8a2e:0370:7334', interface='en1'))
        ),

        test_data_2 = (
            dict(route_path='route'),
            dict(v4=dict(gateway='192.168.1.1', interface='en0'), v6=dict())
        ),
    )


# Generated at 2022-06-13 01:21:57.214700
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    collector = AIXNetworkCollector()
    assert collector is not None

# Generated at 2022-06-13 01:21:59.377128
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    instance = AIXNetworkCollector()
    assert instance._platform == 'AIX'
    assert instance._fact_class.platform == 'AIX'


# Generated at 2022-06-13 01:22:10.162430
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    module = AnsibleModule(argument_spec=dict())

    # Test basic case with IPv4 and IPv6
    route_path = "/path/to/route"
    netstat_path = "/path/to/netstat"
    module.get_bin_path = MagicMock(return_value=route_path)
    module.run_command = MagicMock(return_value=(0, "default x.y.z.1 UGS 0 0 enx001256f0b5a2 eth0\ndefault ::ffff:0:0 UGS 0 0 enx001256f0b5a2 eth0", ""))

    n = AIXNetwork(module)
    v4, v6 = n.get_default_interfaces(route_path)

    assert v4['interface'] == "eth0"

# Generated at 2022-06-13 01:22:17.514669
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    module = NetworkCollector()
    platform = 'AIX'
    path = '/sbin'
    options = None
    module.warnings = []

    m = module.get_network_module(platform)
    m.module = module
    m.path = path
    m.options = options

    # Mock run_command method
    m.module.run_command = mock_run_command

    # Mock get_bin_path method
    mock_path = ['/sbin/netstat']
    m.module.get_bin_path = lambda x: mock_path.pop()

    # Mock get_default_interfaces method
    route_path = '/sbin/route'
    default_interfaces = m.get_default_interfaces(route_path)

# Generated at 2022-06-13 01:22:28.151564
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    """
    Test the get_default_interfaces method of the AIXNetwork class.
    In fact, we use class AIXNetworkCollector, but it is only used to call the method get_default_interfaces
    """

    # Assert that no gateway is found if netstat returns no gateway
    net_collector=AIXNetworkCollector()
    assert "interface" not in net_collector.get_default_interfaces("")

    # Assert that a v4 gateway is found if netstat returns an ipv4 gateway
    net_collector.module.run_command = lambda arguments, ignore_rc=False, check_rc=True: (
        0,
        "Dummy output of netstat that contains default gateway 10.0.0.1 on en0",
        ""
    )
    v4_default_interface = net_collector

# Generated at 2022-06-13 01:22:36.254083
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    class FakeModule():
        def __init__(self):
            self.run_command = classmethod(_run_command)
            self.is_executable = classmethod(_is_executable)
            self.get_bin_path = classmethod(_get_bin_path)

    class FakeModule():
        def __init__(self, params):
            self.params = params

    # test data

# Generated at 2022-06-13 01:24:12.030580
# Unit test for method get_interfaces_info of class AIXNetwork

# Generated at 2022-06-13 01:24:16.122550
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    module = MockModule()
    network = AIXNetwork(module=module)
    rc = 0
    out = '''Kernel IP routing table
Destination        Gateway            Flags  #Ent  Use  Mtu  Interface
default            10.0.2.2          UG     200     0     4   ent0
'''

    module.run_command = Mock(
        return_value=(rc, out, '')
    )
    ipv4, ipv6 = network.get_default_interfaces('')
    assert ipv4 == {"gateway": "10.0.2.2", "interface": "ent0"}
    assert ipv6 == {}



# Generated at 2022-06-13 01:24:26.333704
# Unit test for method get_interfaces_info of class AIXNetwork

# Generated at 2022-06-13 01:24:33.373522
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    interface = dict(v4={}, v6={})
    # Parameters to mock the run_command method
    run_command_args = [
        'bin/netstat',
        '-nr'
    ]

# Generated at 2022-06-13 01:24:35.744165
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    """
    Constructor of NetworkCollector shall set _platform to 'AIX'
    """
    collector = AIXNetworkCollector()
    assert collector._platform == 'AIX'

# Generated at 2022-06-13 01:24:43.793086
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    test_module = AnsibleModule(
        argument_spec=dict(
            gather_subset=dict(default=['!all'], type='list'),
        ),
        supports_check_mode=True
    )

    network_collector = AIXNetworkCollector(test_module)
    network = network_collector.collect()[0]

    assert 'default_ipv4' in network
    assert 'default_ipv6' in network

    assert 'interface' in network['default_ipv4']
    assert 'interface' in network['default_ipv6']

    assert 'gateway' in network['default_ipv4']
    assert 'gateway' in network['default_ipv6']


# Generated at 2022-06-13 01:24:46.047013
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    network_backend = AIXNetworkCollector()
    assert network_backend.__class__.__name__ == 'AIXNetworkCollector'
    assert network_backend._fact_class.__name__ == 'AIXNetwork'

# Generated at 2022-06-13 01:24:50.370013
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    module = AnsibleModule(argument_spec=dict())
    module.run_command = MagicMock(return_value=(0, '', ''))
    network_collector = AIXNetwork()
    network_collector.module = module
    result = network_collector.get_default_interfaces('/etc/route')
    assert result == ({'gateway': '169.254.0.0', 'interface': 'lo0'}, {'gateway': 'fe80::%en1', 'interface': 'en1'})



# Generated at 2022-06-13 01:24:53.436030
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    obj = AIXNetworkCollector()
    assert obj._fact_class.__name__ == 'AIXNetwork'
    assert obj._platform == 'AIX'

# Generated at 2022-06-13 01:24:59.151426
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    mod_args = dict(
        gather_timeout=10,
        gather_subset=['!all', '!min'],
        command_timeout=10
    )
    nc = AIXNetworkCollector(
        module=dict(),
        params=mod_args
    )
    assert nc.FACT_SUBSET == [
        'default_ipv4', 'default_ipv6',
        'interfaces', 'all_ipv4_addresses', 'all_ipv6_addresses'
    ]