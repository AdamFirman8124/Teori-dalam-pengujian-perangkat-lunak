

# Generated at 2022-06-13 01:17:01.465467
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    # Mock these dicts from ansible.module_utils.facts.collector
    # in order to be able to instantiate AIXNetworkCollector
    mock_ansible_module = dict(params=dict(gather_subset=['!all', 'network']))
    mock_module_utils_facts_args = dict(module=mock_ansible_module)
    mock_module_utils_facts_network = dict(NetworkCollector=AIXNetworkCollector)
    module_utils_facts = dict(args=mock_module_utils_facts_args, network=mock_module_utils_facts_network)

    obj = AIXNetworkCollector(module_utils_facts)
    # Check that AIXNetworkCollector is instantiated
    assert obj is not None

# Generated at 2022-06-13 01:17:03.654962
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    assert AIXNetworkCollector._platform == 'AIX'
    assert AIXNetworkCollector._fact_class == AIXNetwork


# Generated at 2022-06-13 01:17:11.828450
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    import subprocess

    class Module():
        def get_bin_path(self, module_name, required=False):
            if module_name == 'netstat':
                return '../utils/netstat'
            elif module_name == 'ifconfig':
                return '../utils/ifconfig'
            elif module_name == 'lsattr':
                return '/usr/sbin/lsattr'
            elif module_name == 'entstat':
                return '/usr/sbin/entstat'
            elif module_name == 'uname':
                return '../utils/uname'

        def run_command(self, args):
            proc = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = proc.communicate()

# Generated at 2022-06-13 01:17:23.316756
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    ifconfig_path = './test/unit/module_utils/facts/network/testdata_AIX_ifconfig_a'
    ifconfig_options = '-a'
    temp = AIXNetwork()
    interfaces, ips = temp.get_interfaces_info(ifconfig_path,ifconfig_options)

# Generated at 2022-06-13 01:17:34.456649
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    module = AnsibleModuleMock()
    ifconfig_path = '/usr/sbin/ifconfig'
    ifconfig_options = '-a'
    result = [None] * 2
    rc = 0

    test_class = AIXNetwork()
    test_class.module = module
    test_class.get_interfaces_info(ifconfig_path, ifconfig_options)

    def mock_run_command(command):
        return rc, result[0], result[1]

    module.run_command = mock_run_command

    # case 1. default route v4 found in output of netstat command
    #         default route v6 missing in output of netstat command
    result[0] = '''
default 192.168.1.1 UG en1
default ::1 UG lo0
'''
    assert test_

# Generated at 2022-06-13 01:17:34.969467
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    obj = AIXNetworkCollector()
    assert obj

# Generated at 2022-06-13 01:17:36.472262
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    c = AIXNetwork()
    c.get_default_interfaces(route_path=None)



# Generated at 2022-06-13 01:17:45.878607
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():

    # create test class
    class Module:
        def get_bin_path(self, name):
            return '/usr/bin/netstat'
        def run_command(self, args):
            if args[0] == '/usr/bin/netstat':
                if args[1] == '-nr':
                    return 0, 'default 192.168.1.1 UGS 0 0 en0\ndefault ::1 UGS 0 0 en0', ''

# Generated at 2022-06-13 01:17:48.593343
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    network_collector = AIXNetworkCollector()
    assert network_collector


# Generated at 2022-06-13 01:17:58.219826
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    class MockModule(object):
        def __init__(self, val):
            self.val = val


# Generated at 2022-06-13 01:18:18.761592
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    module = AnsibleModule(
        argument_spec=dict(
            gather_subset=dict(default=['!all'], type='list')
        ),
        supports_check_mode=True,
    )
    network_collector = AIXNetworkCollector(module=module)
    gateway = network_collector.get_default_interfaces('/sbin/route')
    assert isinstance(gateway, tuple)
    assert len(gateway) == 2
    assert isinstance(gateway[0], dict)
    assert isinstance(gateway[1], dict)
    assert gateway[0]['interface'] == 'en5'
    assert gateway[0]['gateway'] == '10.1.0.1'
    assert gateway[1]['interface'] == 'en5'
    assert gateway[1]['gateway']

# Generated at 2022-06-13 01:18:28.663745
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    ifconfig_path = '/usr/sbin/ifconfig'
    route_path = '/usr/sbin/route'
    module = AnsibleModule(argument_spec=dict(path=dict(default='/usr/sbin/ifconfig', type='path'),
                                              gather_subset=dict(default=['!all'], type='list'),
                                              use_ipv6=dict(default=False, type='bool')),
                           supports_check_mode=False,
                           add_file_common_args=True)
    collector = AIXNetworkCollector(module=module)
    interface = collector.get_default_interfaces(route_path)

# Generated at 2022-06-13 01:18:39.812846
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    net = AIXNetwork()
    net.module = MagicMock()
    net.module.get_bin_path.return_value = "/usr/bin/netstat"
    interfaces = dict(v4={'gateway': '172.17.100.1', 'interface': 'tap0'}, v6={'gateway': 'fe80::a00:27ff:fe1a:90f0%tap0', 'interface': 'tap0'})
    out = '''
    default 172.17.100.1 UG 1 0 tap0
    default fe80::a00:27ff:fe1a:90f0%tap0 UGDAf 7 0 tap0
    '''
    net.module.run_command.return_value = (0, out, '')

# Generated at 2022-06-13 01:18:41.068483
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    ansible_module=AnsibleModule(argument_spec={})
    collector = AIXNetworkCollector(ansible_module)

    assert collector.platform == 'AIX'

# Generated at 2022-06-13 01:18:49.257078
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    network = AIXNetwork()
    network.module = AnsibleModuleMock()
    network.module.run_command = Mock(return_value=(0, netstat_nr_out, ''))
    default_interfaces = network.get_default_interfaces('route')
    assert default_interfaces == {'device': 'en0', 'gateway': '172.20.1.1', 'interface': '172.20.1.2'}, \
        "The gateway is not parsed properly with netstat command"


# Generated at 2022-06-13 01:18:58.465474
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    from ansible.module_utils.facts.network.aix import AIXNetwork

    fact_class = AIXNetwork()


# Generated at 2022-06-13 01:19:06.567878
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork
    try:
        aix_network_collector = AIXNetworkCollector()
        assert(aix_network_collector.__class__.__name__ == 'AIXNetworkCollector')
        assert(isinstance(aix_network_collector._fact_class, GenericBsdIfconfigNetwork))
        assert(aix_network_collector._fact_class.platform == 'AIX')
    except Exception as e:
        assert(False)


# Generated at 2022-06-13 01:19:14.719821
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    from ansible.module_utils.facts.network.aix import AIXNetwork
    from ansible.module_utils.facts.network.base import Network
    import sys

    my_object = AIXNetwork(Network())

    sys.modules['ansible'] = object
    sys.modules['ansible.module_utils'] = object
    sys.modules['ansible.module_utils.facts'] = object
    sys.modules['ansible.module_utils.facts.network'] = object
    sys.modules['ansible.module_utils.facts.network.base'] = object

    # If neccessary, set up ansible module helper
    if not hasattr(my_object, 'module'):
        my_object.set_module(None)

    # Test default gateway

# Generated at 2022-06-13 01:19:16.442859
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    module = MockModule()
    network = AIXNetwork(module)
    network.get_default_interfaces('netstat')



# Generated at 2022-06-13 01:19:21.123153
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    ai = AIXNetwork()
    interface = dict(v4={}, v6={})
    ai.get_default_interfaces('/sbin/route')
    eth0 = interface['v4']
    assert eth0['gateway'] == '172.20.0.1'
    assert eth0['interface'] == 'en0'
    inet6 = interface['v6']
    assert inet6['gateway'] == 'fe80::21a:a0ff:fe60:c345'
    assert inet6['interface'] == 'en0'


# Generated at 2022-06-13 01:19:55.162070
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    """
    Unit test for method get_interfaces_info of class AIXNetwork
    """
    class TestGenericModule():
        def __init__(self):
            self._result = {
                'rc': 0,
                'stdout': "",
                'stderr': ""
            }
            self.exit_json = {}
            self.fail_json = {}
            self.check_mode = False

        def run_command(self, cmd):
            return self._result['rc'], self._result['stdout'], self._result['stderr']

        def get_bin_path(self, name):
            return "/bin/%s" % name


# Generated at 2022-06-13 01:19:59.210002
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    test_AIXNetwork = AIXNetwork({'module': 'AIX_Module'})
    interface = test_AIXNetwork.get_default_interfaces('some_path_to_route_executable')
    assert interface is not None
    assert len(interface) == 1
    assert interface[0]['gateway'] is not None
    assert interface[0]['interface'] is not None


# Generated at 2022-06-13 01:20:09.811632
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    module = DummyModule()
    fact_class = AIXNetwork(module)
    command_output = """
default 128.0.0.1 UG      0 0        en0
default 192.168.0.1 UG      0 0        en1
default fe80::1%7 UGHD     0 0        en0
default ff00::%7/64 U       0 0        en0
    """
    module.run_command = MagicMock(return_value=(0, command_output, ""))
    assert fact_class.get_default_interfaces("/some/path") == ({'gateway': '128.0.0.1', 'interface': 'en0'}, {'gateway': 'fe80::1%7', 'interface': 'en0'})



# Generated at 2022-06-13 01:20:16.589311
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    fake_module = test_AIXNetwork_fake_module()
    expected_interfaces_info = test_AIXNetwork_fake_interfaces_info()
    AIXNetwork_fact_class = AIXNetwork()
    AIXNetwork_fact_class.module = fake_module
    interfaces_info = AIXNetwork_fact_class.get_interfaces_info(fake_module.get_bin_path('ifconfig'))
    assert interfaces_info == expected_interfaces_info


# Generated at 2022-06-13 01:20:23.811150
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    module = NetworkCollector()


# Generated at 2022-06-13 01:20:29.922444
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    module = AnsibleModule({
        "uname_path": "uname",
        "netstat_path": "netstat",
    })

    network = AIXNetwork(module, "netstat")
    assert network.get_default_interfaces("route") == ({u'interface': u'en6', u'gateway': u'172.16.0.1'}, {})

# Generated at 2022-06-13 01:20:40.367946
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    ifconfig_path = '/usr/sbin/ifconfig'
    ifconfig_options = '-a'
    module = AnsibleModuleMock()
    aix_network = AIXNetwork(module)
    (interfaces, ips) = aix_network.get_interfaces_info(ifconfig_path, ifconfig_options)
    assert interfaces['en0']['ipv4'][0]['address'] == '172.16.156.111'
    assert interfaces['en0']['mtu'] == '1500'
    assert interfaces['en1']['type'] == 'ether'
    assert interfaces['en1']['ipv4'][0]['broadcast'] == '172.16.157.255'

# Generated at 2022-06-13 01:20:48.237243
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    # Unit test for AIX method get_default_interfaces()
    run_result = {
        'stdout': """
Kernel IP routing table
Destination        Gateway            Flags   Refs   Use  If
default            192.168.122.1      UG      4       0   en0
        """,
        'stdout_lines': [
            '',
            'Kernel IP routing table',
            'Destination        Gateway            Flags   Refs   Use  If',
            'default            192.168.122.1      UG      4       0   en0'
        ],
        'parsed': {
            'v4': {
                'gateway': '192.168.122.1',
                'interface': 'en0'
            },
            'v6': {}
        }
    }
    m = AIX

# Generated at 2022-06-13 01:20:59.013087
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():

    def test_lines(netdev):
        rc, out, err = netdev.module.run_command([ifconfig_path, ifconfig_options])
        return out.splitlines()

    class NetDev:
        class AnsibleModule:
            class Parameters(object):
                def __init__(self):
                    self.data = list()

                def __setitem__(self, key, value):
                    self.data.append(dict(key=key, value=value))

                def __getitem__(self, key):
                    for d in self.data:
                        if d['key'] == key:
                            return d['value']
                    return None

                def __contains__(self, key):
                    for d in self.data:
                        if d['key'] == key:
                            return True
                    return False


# Generated at 2022-06-13 01:21:02.468312
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    """
    unit test for constructor of class AIXNetworkCollector
    """
    from ansible.module_utils.facts.network.aix import AIXNetworkCollector
    net_collector = AIXNetworkCollector()
    assert net_collector.platform == 'AIX'


# Generated at 2022-06-13 01:21:51.979197
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    '''Test constructor of class AIXNetworkCollector.'''
    assert AIXNetworkCollector

# Generated at 2022-06-13 01:21:56.300434
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    from ansible.module_utils.facts.collector import Collector

    AIXNetworkCollector.collect()
    assert Collector.__module__ == 'ansible.module_utils.facts.collectors.network.aix'
    assert AIXNetworkCollector.__module__ == 'ansible.module_utils.facts.collectors.network.aix'
    assert AIXNetworkCollector.__doc__ == 'Collect network information from AIX.'

# Generated at 2022-06-13 01:22:03.999765
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    test_AIXNetwork = AIXNetwork()
    test_route_path = '/usr/sbin/netstat'
    test_default_interfaces = test_AIXNetwork.get_default_interfaces(test_route_path)
    assert test_default_interfaces[0] == {'gateway': '10.115.255.254', 'interface': 'en1'}
    assert test_default_interfaces[1] == {'gateway': 'fe80::200:5aee:feaa:20a2', 'interface': 'en1'}

# Generated at 2022-06-13 01:22:10.531458
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    from ansible.module_utils.facts.network.aix import AIXNetwork

    ansible_module = MockAnsibleModule({
        'ansible_facts': {}
    })
    obj = AIXNetwork(ansible_module)

    assert obj.get_default_interfaces('/bin/netstat') == ({'gateway': '172.18.1.2', 'interface': 'e0'}, {'gateway': 'fd06:6b15:b18:0:250:56ff:fea7:181c', 'interface': 'e0'})



# Generated at 2022-06-13 01:22:16.385147
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    """ Unit test code for AIXNetwork get_interfaces_info
        This code test the format of the output of method get_interfaces_info
    """

    # Constructing a fake module
    fake_module = type('Fake Module', (object,), dict())()
    fake_module.run_command = lambda cmd: (0, '', '')
    fake_module.get_bin_path = lambda cmd: cmd


# Generated at 2022-06-13 01:22:27.072927
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    module = AnsibleModule(
        argument_spec=dict(
            gather_subset=dict(default=['!all'], type='list')
        ),
        supports_check_mode=True
    )
    ansible_facts = dict(
        ansible_net_interfaces={},
        ansible_net_all_ipv4_addresses=[],
        ansible_net_all_ipv6_addresses=[]
    )

    # open the file for reading
    filehandle = open ('/home/ansible/ansible/lib/ansible/module_utils/facts/network/AIX/resources/if_output.txt', 'r')

    # read all lines at once
    filehandle.seek(0, 0)
    lines = filehandle.read().splitlines()

    # close the pointer to that file


# Generated at 2022-06-13 01:22:31.701359
# Unit test for method get_interfaces_info of class AIXNetwork

# Generated at 2022-06-13 01:22:35.005687
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    try:
        import __builtin__ as builtins
    except ImportError:
        import builtins
    config = dict()
    config['gather_subset'] = ['all']
    network_collector = AIXNetworkCollector(builtins, config)
    assert network_collector._platform == 'AIX'

# Generated at 2022-06-13 01:22:44.575363
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    class AIXNetworkMock(AIXNetwork):
        def __init__(self):
            self.module = AnsibleModuleMock()

        def get_bin_path(self, path):
            if path == 'netstat':
                return '/usr/bin/netstat'
            else:
                return ''


# Generated at 2022-06-13 01:22:51.811959
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    module = mock.MagicMock()
    module.get_bin_path.return_value = 'netstat'
    module.run_command.return_value = (0, 'default 192.168.0.1 UG 1 2001 0 en0\ndefault fe80::1%lo0 UG 1 2001 0 lo0', None)
    aix_network = AIXNetwork(module)
    (ipv4_default, ipv6_default) = aix_network.get_default_interfaces('/usr/bin/netstat')
    assert ipv4_default == {'gateway': '192.168.0.1', 'interface': 'en0'}
    assert ipv6_default == {'gateway': 'fe80::1%lo0', 'interface': 'lo0'}

# Generated at 2022-06-13 01:24:30.097925
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    collector = AIXNetworkCollector()


# Generated at 2022-06-13 01:24:33.010536
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    module = AnsibleModule(argument_spec={})
    assert type(AIXNetwork.get_interfaces_info(AIXNetwork(), ifconfig_path='/usr/bin/ifconfig', ifconfig_options='-a')) is tuple


# Generated at 2022-06-13 01:24:35.742102
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    module = DummyAnsibleModule()
    aixnetwork_obj = AIXNetwork(module)

    assert aixnetwork_obj.get_default_interfaces() == ('', '')


# Generated at 2022-06-13 01:24:42.005282
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    module = AnsibleModule(argument_spec={})
    module.run_command = mock.Mock(return_value=(0, 'default 8.8.8.8 UGS 0 0 en0', ''))
    aix = AIXNetwork(module)
    gateway_v4, gateway_v6 = aix.get_default_interfaces('/usr/bin/netstat')
    assert gateway_v4 == {'gateway': '8.8.8.8', 'interface': 'en0'}
    assert gateway_v6 == {}


# Generated at 2022-06-13 01:24:44.799432
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    """
    Method to test constructor of AIXNetworkCollector
    """
    aix_fact_collector = AIXNetworkCollector()
    assert isinstance(aix_fact_collector, AIXNetworkCollector)


if __name__ == '__main__':
    test_AIXNetworkCollector()

# Generated at 2022-06-13 01:24:51.216663
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():

    mod = AnsibleModule(
        argument_spec=dict(
            gather_subset=dict(default=['!all', 'network'], type='list')
        ),
        supports_check_mode=True
    )

    # init
    aix_network = AIXNetwork(mod)

    # AIX ifconfig output

# Generated at 2022-06-13 01:24:52.884803
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    from ansible.module_utils.facts import collector
    n = collector.get_network_collector('AIXNetworkCollector', {'module': None})
    assert n is not None

# Generated at 2022-06-13 01:25:01.356317
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    """
    Test of the class AIXNetwork, method get_default_interfaces
    """
    network = AIXNetwork()

    def run_command(module, command, checkrc=True, **kwargs):
        assert command[0] == '/usr/bin/netstat'
        return 0, netstat_out, ''


# Generated at 2022-06-13 01:25:03.015086
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():

    module = MockModule()
    net_collector = AIXNetworkCollector(module=module)
    net_collector.get_facts()



# Generated at 2022-06-13 01:25:05.510581
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    _fact_class = AIXNetwork
    _platform = 'AIX'
    obj = AIXNetworkCollector(_fact_class, _platform)
    assert obj.fact_class._platform == 'AIX'
