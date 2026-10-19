

# Generated at 2022-06-13 01:16:59.373058
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    module = AnsibleModule(argument_spec={})
    module.params['gather_subset'] = ['network']
    module.params['gather_timeout'] = 0
    module.params['gather_network_resources'] = [
        'interfaces',
        'default_gateway_ipv4',
        'default_gateway_ipv6',
    ]

    net = AIXNetwork(module)
    routes_path = '/etc/defaultrouter'
    (v4_interface, v6_interface) = net.get_default_interfaces(routes_path)

    v4_route = v4_interface['gateway']
    v6_route = v6_interface['gateway']

    v4_interface = v4_interface['interface']
    v6_interface = v6_interface['interface']

# Generated at 2022-06-13 01:17:00.959312
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    assert repr(AIXNetworkCollector)

# Generated at 2022-06-13 01:17:10.187806
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    module = NetworkCollector()
    ifconfig_path = module.get_bin_path('ifconfig')
    route_path = module.get_bin_path('route')
    net = AIXNetwork(module=module, ifconfig_path=ifconfig_path, route_path=route_path)

    #
    # test case 1
    #

# Generated at 2022-06-13 01:17:16.161213
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    facts = dict()
    collector = AIXNetworkCollector(module=None, facts=facts)
    assert collector._facts is facts
    assert collector._platform == 'AIX'
    assert collector._fact_class.__name__ == 'AIXNetwork'


# Generated at 2022-06-13 01:17:25.633631
# Unit test for method get_interfaces_info of class AIXNetwork

# Generated at 2022-06-13 01:17:33.946167
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    module = AnsibleModuleMock()
    if_class = AIXNetwork(module)

    gateway_v4, gateway_v6 = if_class.get_default_interfaces('/sbin/route')

    assert_equals(gateway_v4['gateway'], '9.0.0.1')
    assert_equals(gateway_v4['interface'], 'en0')
    assert_equals(gateway_v6['gateway'], '::')
    assert_equals(gateway_v6['interface'], 'lo0')


# Generated at 2022-06-13 01:17:41.682719
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():

    MODULE_UTILS_PATH = None
    IFACE_PATH = '../../library/module_utils/facts/network/bsd/ifconfig.py'
    AIX_PATH = '../../library/module_utils/facts/network/aix/ifconfig.py'
    cmd = {'run_command': {}}
    module = type('fake_module', (object,), {
        'get_bin_path': lambda x: '/sbin/ifconfig',
        'run_command': lambda x, check_rc=True: cmd['run_command'][x],
    })
    fact_class = AIXNetwork(module)
    interfaces_info = None
    try:
        interfaces_info = fact_class.get_interfaces_info('/sbin/ifconfig', '-a')
    except:
        pass
   

# Generated at 2022-06-13 01:17:53.699965
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    '''
    This function tests the get_interfaces_info function of class AIXNetwork
    The test uses the output of the command 'ifconfig -a' on an AIX system
    which has been stored in the file module_utils/facts/network/ifconfig-a
    '''
    with open('module_utils/facts/network/ifconfig-a') as f:
        ifconfig_output = f.read()
    ifconfig_path = '/usr/sbin/ifconfig'
    ifconfig_options = '-a'
    interfaces = {}
    current_if = {}
    ips = dict(
        all_ipv4_addresses=[],
        all_ipv6_addresses=[],
    )

    AIX_network = AIXNetwork(None)


# Generated at 2022-06-13 01:17:56.257366
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    m = AIXNetworkCollector()
    assert m.platform == 'AIX'
    assert m._fact_class.platform == 'AIX'
    assert m.get_default_interfaces('netstat') == (None, None)

# Generated at 2022-06-13 01:17:57.998349
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    assert AIXNetwork().get_default_interfaces('route -an') == ('lo0', {})

# Generated at 2022-06-13 01:18:18.271840
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    net = AIXNetwork()

    net.module = type('DummyClass', (object,), dict(run_command=lambda s, l: (0, 'default 192.168.1.1 UG     0 0 en0\ndefault 2001:1111:2222:3333::1 UG    0 0 en1', '')))
    assert net.get_default_interfaces('A') == (dict(gateway='192.168.1.1', interface='en0'), dict(gateway='2001:1111:2222:3333::1', interface='en1'))

    net.module = type('DummyClass', (object,), dict(run_command=lambda s, l: (0, '', '')))

# Generated at 2022-06-13 01:18:21.563810
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    obj = AIXNetworkCollector()
    assert obj._fact_class == AIXNetwork
    assert obj._platform == 'AIX'



# Generated at 2022-06-13 01:18:24.307434
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    network_collector = AIXNetworkCollector()
    assert network_collector._fact_class == AIXNetwork
    assert network_collector._platform == 'AIX'

# Generated at 2022-06-13 01:18:27.494857
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    module = NetworkCollector()
    aix = AIXNetwork(module)
    v4, v6 = aix.get_default_interfaces('route_path')
    assert v4['interface'] == 'en0'
    assert v6['interface'] == 'en0'

# Generated at 2022-06-13 01:18:30.452462
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    aix_network_collector = AIXNetworkCollector()
    assert aix_network_collector is not None


# Generated at 2022-06-13 01:18:32.462178
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    """
    Constructor of class AIXNetworkCollector can be called without arguments
    """
    AIXNetworkCollector()

# Generated at 2022-06-13 01:18:42.113918
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork
    from ansible.module_utils.facts.network.aix import AIXNetwork

    my_AIXNetwork = AIXNetwork()

    # ifconfig command output for AIX
    ifconfig = 'lo0: flags=0x8049 mtu 8232\n'\
               'options=3<RXCSUM,TXCSUM>\n'\
               'inet 127.0.0.1 netmask 0xff000000\n'\
               'nd6 options=21<PERFORMNUD,AUTO_LINKLOCAL>\n'\
               'en0: flags=0x8802b mtu 1500 index 2\n'\
               'ether d8:0d:17:c6:f9:26\n'

# Generated at 2022-06-13 01:18:45.960306
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    from ansible.module_utils.facts.network.aix import AIXNetworkCollector
    network_collector = AIXNetworkCollector()
    assert network_collector._fact_class == AIXNetwork
    assert network_collector._platform == 'AIX'


# Generated at 2022-06-13 01:18:49.106495
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    collector = AIXNetworkCollector()
    assert collector.platform == 'AIX'
    assert collector._fact_class.platform == 'AIX'


# Generated at 2022-06-13 01:18:58.322966
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    module = AnsibleModule(argument_spec=dict())
    nw = AIXNetwork(module=module)
    netstat_path = nw.module.get_bin_path('netstat')

    if netstat_path:
        nw.module.run_command = lambda x, y, z: (1, '', '')
        assert nw.get_default_interfaces(netstat_path) == (dict(), dict())

        out = '''
        default            10.0.0.2          UG        0        0        0 en0
        default            fe80::%en1       UG        0        0        0 en1
        default            default           UG        0        0        0 en1
        '''
        nw.module.run_command = lambda x, y, z: (0, out, '')


# Generated at 2022-06-13 01:19:30.881440
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    module = AnsibleModule(argument_spec={})
    module.run_command = MagicMock(return_value=(0, '', ''))

    ifconfig_path = module.get_bin_path('ifconfig')
    if not ifconfig_path:
        raise Exception('ifconfig path could not be found')

    _network_collector = AIXNetworkCollector(module)
    _network_collector.get_interfaces_info(ifconfig_path, '-a')
    _network_collector.get_interfaces_info(ifconfig_path, 'lo0')

# Generated at 2022-06-13 01:19:33.013090
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    module = AnsibleModule(argument_spec=dict())
    collector = AIXNetworkCollector(module=module)

    assert isinstance(collector, NetworkCollector)
    assert isinstance(collector, AIXNetworkCollector)
    assert collector._platform == 'AIX'
    assert collector._fact_class == AIXNetwork


# Generated at 2022-06-13 01:19:34.603098
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    aixnet = AIXNetwork()
    assert aixnet.get_default_interfaces('route') is not None

# Generated at 2022-06-13 01:19:36.328350
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    # create test object
    fact_collector=AIXNetworkCollector()
    assert fact_collector._platform == 'AIX'

# Generated at 2022-06-13 01:19:37.983253
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    assert AIXNetworkCollector._platform == 'AIX'
    assert AIXNetworkCollector._fact_class == AIXNetwork


# Generated at 2022-06-13 01:19:48.293678
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    obj = AIXNetwork(dict(module=None, params=None))

    ifconfig_path = obj.module.get_bin_path('ifconfig')
    rc, out, err = obj.module.run_command([ifconfig_path, '-a'])
    interfaces, ips = obj.get_interfaces_info(ifconfig_path)
    print(interfaces)
    print(ips)

    ifconfig_path = obj.module.get_bin_path('ifconfig')
    rc, out, err = obj.module.run_command([ifconfig_path, '-a'])
    interfaces, ips = obj.get_interfaces_info(ifconfig_path, '-a')
    print(interfaces)
    print(ips)


# Generated at 2022-06-13 01:19:56.853016
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    """
    This is a test method for testing the method
    get_default_interfaces of class AIXNetwork.

    The test method does not actually require AIX.
    It just pretends to be on AIX.
    It uses an object of the class AIXNetwork
    and runs the method get_default_interfaces.

    :return:
    """
    from ansible.module_utils.facts.network.base import NetworkCollector
    from ansible.module_utils.facts.network.aix import AIXNetwork

    class MockNetworkCollector(NetworkCollector):
        _platform = 'AIX'

        def get_netstat_path(self):
            return './test/aix/netstat'

    class MockAIXNetwork(AIXNetwork):

        def __init__(self, module):
            self.module = module

# Generated at 2022-06-13 01:20:07.816405
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    from ansible_collections.community.network.tests.unit.compat.mock import (
        patch, Mock, MagicMock
    )

    module = MagicMock()
    module.run_command = Mock(return_value=(0, 'fakeout', 'fakeerr'))

    get_bin_path_mock = Mock(return_value='/usr/sbin/ifconfig')
    m_module = manager.module_utils.facts.network.generic_bsd.module
    with patch.object(m_module, 'get_bin_path', get_bin_path_mock):
        result = AIXNetwork.get_interfaces_info(module, "/bin/foo", "-a")

    assert result[0]['lo0']['flags'] == ['UP', 'LOOPBACK', 'RUNNING']
   

# Generated at 2022-06-13 01:20:12.469712
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    module = AnsibleModule(argument_spec=dict())
    collector_aix = AIXNetworkCollector(module=module)
    network = AIXNetwork(module=module)

    assert network.get_default_interfaces("route_path") is not None
    assert collector_aix.get_device_default_gateways("route_path") is not None

# Generated at 2022-06-13 01:20:17.156048
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    net_mod = AIXNetwork()
    module = _ansible_mock('aix')
    net_mod.module = module
    net_mod.module.exit_json = _ansible_exit_json
    net_mod.module.fail_json = _ansible_fail_json

    assert net_mod.get_default_interfaces('route') is not None


# Generated at 2022-06-13 01:20:49.274881
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    """Return dictionary of interface information and all ip addresses"""

    class TestModule(object):
        def __init__(self):
            self.run_command_calls = 0
            self.run_command_call_results = []

        def get_bin_path(self, name, opt_dirs=[]):
            return name

        def run_command(self, commands, check_rc=True):
            self.run_command_calls += 1
            return self.run_command_call_results.pop(0)

    # create test object
    test_obj = AIXNetwork()
    test_obj.module = TestModule()

    # create test data

# Generated at 2022-06-13 01:20:59.524998
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    file_path = os.path.join(os.path.dirname(__file__), 'fixtures', 'AIX_netstat_nr')
    with open(file_path, 'r') as f:
        output = f.read()
    module = Mock()
    module.run_command.return_value = 0, output, ''
    module.get_bin_path.return_value = os.getcwd()
    net = AIXNetwork()
    net.module = module
    result = net.get_default_interfaces('/usr/sbin/route')
    assert result == ({'gateway': '192.0.2.1', 'interface': 'en0'},
                      {'gateway': '2001:db8::1', 'interface': 'en0'})


# Generated at 2022-06-13 01:21:04.672640
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():

    test_module = AnsibleModule(
        argument_spec=dict(
            route_path=dict(default='/usr/sbin/route'),
        ),
        supports_check_mode=False
    )

    test_obj = AIXNetwork(test_module)
    test_result = test_obj.get_default_interfaces(test_module.params['route_path'])

    test_module.exit_json(ansible_facts=dict(network=test_result))


# Generated at 2022-06-13 01:21:05.837086
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    assert AIXNetworkCollector.platform == 'AIX'


# Generated at 2022-06-13 01:21:07.970371
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    """
    Constructor test of AIXNetworkCollector
    """
    assert AIXNetworkCollector._platform == 'AIX'
    assert AIXNetworkCollector._fact_class == AIXNetwork



# Generated at 2022-06-13 01:21:08.970246
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    AIXNetwork.get_default_interfaces('route_path')

# Generated at 2022-06-13 01:21:11.023613
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    facts = AIXNetwork()
    default_interface = facts.get_default_interfaces('/bin/route')
    assert 'gateway' in default_interface
    assert 'interface' in default_interface
    assert 'v6' not in default_interface

# Generated at 2022-06-13 01:21:20.264005
# Unit test for method get_interfaces_info of class AIXNetwork

# Generated at 2022-06-13 01:21:28.477407
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():

    # create "faked" module object
    class FakedModule():
        def __init__(self):
            self.a = 5

        def get_bin_path(self, name):
            return '/usr/sbin/' + name


# Generated at 2022-06-13 01:21:34.300780
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():

    from ansible.module_utils.facts.network.base import NetworkCollector
    from ansible.module_utils.facts.network.aix import AIXNetwork

    from ansible.module_utils.facts.network.tests.unit.compat.mock import MagicMock, patch

    # Set up class AIXNetwork and test method get_default_interfaces()


# Generated at 2022-06-13 01:22:31.609784
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    '''
    Unit test for method get_interfaces_info of class AIXNetwork
    '''


# Generated at 2022-06-13 01:22:38.517810
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():

    import ansible.utils.ansible_runner
    from ansible.module_utils.facts import UnitTestModule

    runner = ansible.utils.ansible_runner.AnsibleRunner(
        module_name='ansible.module_utils.facts.network.aix.AIXNetwork',
        module_args=dict(
        ),
    )

    # --- Test with good data ---

    # Load mock data
    runner.load_module_data()

    # check under normal conditions
    assert_method = runner.module_result['assert_method']
    assert_result = runner.module_result['assert_result']
    assert_module = UnitTestModule(runner.module_result['module_name'])
    assert_module.fail_json = UnitTestModule.fail_json

# Generated at 2022-06-13 01:22:47.930819
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    test_module = MockModule({})
    test_netstat_path = "/usr/bin/netstat"
    test_netstat_output = """
test_netstat_output
default 192.168.0.1 UGHD 192.168.1.1 
default fe80::5efe:192.168.21.150%en0 UGHD en0 
default fe80::5efe:192.168.1.1%en0 UGHD en0 
"""
    test_AIXNetwork_instance = AIXNetwork(test_module)
    test_AIXNetwork_instance.module.run_command = Mock(return_value=(0, test_netstat_output, test_netstat_output)) 
    test_interface = test_AIXNetwork_instance.get_default_interfaces(test_netstat_path)


# Generated at 2022-06-13 01:22:54.524964
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    import platform
    module = platform.system().lower()
    instance = AIXNetwork()

    # create an empty module to feed it to the method
    import ansible.module_utils.common.removed
    m = ansible.module_utils.common.removed.RemovedModule()
    m.params = {}
    instance.module = m
    instance.module.run_command = run_command_mock

    ifconfig_path = '/usr/sbin/ifconfig'
    ifconfig_options = '-a'

    # expected result

# Generated at 2022-06-13 01:22:56.519165
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    """
    Constructor of AIXNetworkCollector can be instantiated without arguments
    """
    try:
        AIXNetworkCollector()
    except Exception as e:
        assert False, "Construction of AIXNetworkCollector failed with " + str(e)

# Generated at 2022-06-13 01:22:57.134377
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    assert AIXNetworkCollector().platform == 'AIX'

# Generated at 2022-06-13 01:23:01.965515
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    network = AIXNetwork()
    # test with real ifconfig output, so no need to mock the module
    interfaces_info, ips_dict = network.get_interfaces_info('/usr/sbin/ifconfig', ifconfig_options='')

    assert interfaces_info['lo0']['device'] == 'lo0'
    assert interfaces_info['lo0']['flags'] == ['UP', 'RUNNING', 'LOOPBACK', 'MULTICAST']
    assert interfaces_info['lo0']['ipv4'] == []
    assert interfaces_info['lo0']['ipv6'] == []
    assert interfaces_info['lo0']['macaddress'] == 'unknown'
    assert interfaces_info['lo0']['mtu'] == '65536'

# Generated at 2022-06-13 01:23:09.781585
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():

    test_module = AnsibleModule(argument_spec={})
    ifconfig_path = test_module.get_bin_path('ifconfig')
    netstat_path = test_module.get_bin_path('netstat')
    assert ifconfig_path
    assert netstat_path

    network_collector = AIXNetworkCollector(test_module)
    aix_network = network_collector._fact_class(test_module)
    default_interfaces = aix_network.get_default_interfaces('/test/route/path')

    assert default_interfaces['v4']['gateway'] == '172.16.2.1'
    assert default_interfaces['v4']['interface'] == 'vlan3094'

# Generated at 2022-06-13 01:23:13.936639
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    module = AnsibleModule(argument_spec=dict(gather_subset=dict(default=['all'], type='list')))
    collector = AIXNetworkCollector(module)
    assert isinstance(collector, AIXNetworkCollector)
    assert isinstance(collector.module, AnsibleModule)

# Generated at 2022-06-13 01:23:21.179931
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    module = AnsibleModule(
        argument_spec = dict(),
        supports_check_mode = True
    )
    ifc = AIXNetwork(module)

    netstat_output = """
default       192.0.2.2       UG        1     0        en0
default      2001:db8::1      UG        1     0      en0
"""

    netstat_path = '/usr/bin/netstat'

    def mock_execute_command(cmd, module_check_mode=False, check=None, executable=None,
                             run_as_root=False, shell=None):
        return 0, netstat_output, ''

    module.run_command = mock_execute_command

    v4, v6 = ifc.get_default_interfaces(netstat_path)

# Generated at 2022-06-13 01:25:06.819770
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    from ansible.module_utils.facts.network.aix import AIXNetwork
    import sys
    import StringIO

    class AnsibleModuleFake(object):
        def __init__(self, params):
            self.params = params

        def get_bin_path(self, arg):
            if arg == 'ifconfig':
                return '/usr/sbin/ifconfig'


# Generated at 2022-06-13 01:25:15.392980
# Unit test for method get_interfaces_info of class AIXNetwork

# Generated at 2022-06-13 01:25:21.774528
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    module = AnsibleModule(
        argument_spec=dict(
            gather_subset=dict(default=['!all', '!min'], type='list')
        ),
        supports_check_mode=True)

    module.run_command = mock.Mock(return_value=(0, 'output', ''))
    set_module_args(dict(gather_subset=['!all', '!min']))
    result = AIXNetwork()._get_interfaces_info(module)
    assert (result['defaults']['gateway'] == '172.22.0.1')
    assert (result['defaults']['gateway_v6'] == 'fe80::21e:c0ff:fe05:741/64')

# Generated at 2022-06-13 01:25:24.948013
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    route_path = ''
    an = AIXNetwork()
    an.module = AnsibleModule(argument_spec={})
    an.get_default_interfaces(route_path)



# Generated at 2022-06-13 01:25:25.868809
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    assert issubclass(AIXNetworkCollector, NetworkCollector)



# Generated at 2022-06-13 01:25:32.241683
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    net = AIXNetwork()
    net.module = MockNetworkModule()
    
    net.module.run_command = Mock()
    net.module.run_command.return_value = [0, 'default 10.10.10.2 UGS 0 0 en0', '']
    
    (v4, v6) = net.get_default_interfaces('/sbin/route -n')
    
    assert v4['gateway'] == '10.10.10.2'
    assert v4['interface'] == 'en0'
    assert v6 is None


# Generated at 2022-06-13 01:25:35.518620
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    net_gather = AIXNetworkCollector()
    assert net_gather.platform == 'AIX'
    assert net_gather._platform == 'AIX'
    assert isinstance(net_gather._fact_class, AIXNetwork)

# Generated at 2022-06-13 01:25:42.048124
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():

    class TestModule(object):
        def __init__(self, input_text, rc, module_path, uname_path):
            self.input_text = input_text
            self.rc = rc
            self.bin_path = module_path
            self.uname_path = uname_path

        def get_bin_path(self, module_name, required=False):
            if module_name == 'ifconfig':
                return self.bin_path
            elif module_name == 'uname':
                return self.uname_path

        def run_command(self, args):
            return self.rc, self.input_text, None


# Generated at 2022-06-13 01:25:46.997497
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    from ansible.module_utils import facts
    from ansible.module_utils.facts.collector import BaseFactCollector

    # test constructor
    fact_collector = AIXNetworkCollector(facts.Facts(BaseFactCollector))
    assert fact_collector.platform == 'AIX'
    assert fact_collector.fact_class.platform == 'AIX'

# Generated at 2022-06-13 01:25:53.644595
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():

    import ansible.module_utils.facts.network.net_tools as tools
    import ansible.module_utils.facts.network.aix as aix

    net = aix.AIXNetwork(tools.ANSIBullshit())
    route_path = '/usr/bin/route'

    result_v4 = dict(gateway='10.1.1.1', interface='en2')
    result_v6 = dict(gateway='fe80::5afe:59ff:fe83:ffff', interface='en2')
    assert net.get_default_interfaces(route_path) == (result_v4, result_v6)