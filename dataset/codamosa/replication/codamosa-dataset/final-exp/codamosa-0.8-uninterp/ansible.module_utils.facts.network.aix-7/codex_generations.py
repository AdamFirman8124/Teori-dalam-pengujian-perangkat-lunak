

# Generated at 2022-06-13 01:17:00.012291
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    m = AIXNetwork()
    # create a temporary ifconfig output file
    import tempfile
    tmpfile = tempfile.NamedTemporaryFile(mode="w+")

# Generated at 2022-06-13 01:17:09.945329
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    from ansible.module_utils.facts import FactCollector
    from ansible.module_utils.facts.utils import get_file_content
    from ansible.module_utils._text import to_bytes

    test_collector = AIXNetwork(module=FactCollector)

    # dummy ifconfig -a output

# Generated at 2022-06-13 01:17:14.077436
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    assert AIXNetworkCollector.platform == "AIX"

# This class is used to create the class to be tested

# Generated at 2022-06-13 01:17:15.467234
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    my_obj = AIXNetworkCollector()
    assert my_obj



# Generated at 2022-06-13 01:17:25.250973
# Unit test for method get_interfaces_info of class AIXNetwork

# Generated at 2022-06-13 01:17:35.341182
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    module = AnsibleModule(argument_spec=dict(route_path=dict(default='/bin/netstat')))
    module.run_command = MagicMock(return_value=(0, 'default 10.10.10.1 UG 1 0 en0\ndefault ::1 UG 1 0 en0', None))
    fact_class = AIXNetwork(module=module)
    real_return = fact_class.get_default_interfaces('/bin/netstat')
    assert real_return[0] == {'gateway': '10.10.10.1', 'interface': 'en0'}
    assert real_return[1] == {'gateway': '::1', 'interface': 'en0'}


# Generated at 2022-06-13 01:17:39.502094
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    aix_network = AIXNetworkCollector()
    assert aix_network
    assert hasattr(aix_network, '_fact_class')
    assert aix_network._fact_class
    assert issubclass(aix_network._fact_class, AIXNetwork)
    assert hasattr(aix_network, '_platform')
    assert aix_network._platform == 'AIX'

# Generated at 2022-06-13 01:17:51.212377
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    import os

    module = AnsibleModule(
        argument_spec=dict(
            gather_subset=dict(default=['!all'], type='list'),
            gather_network_resources=dict(default=['all'], type='list')
        )
    )

    # get_default_interfaces requires presence of 'netstat' command
    which_path = module.get_bin_path('which')

    if which_path:
        rc, out, err = module.run_command([which_path, 'netstat'])
        if rc != 0:
            # Failed to find 'netstat'.  Test is not applicable
            module.exit_json(changed=False)

    # full_path_name is required by get_default_interfaces
    # to construct the route_path.  Normally it's 'route'.
    module

# Generated at 2022-06-13 01:17:56.196331
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    aix_net = AIXNetwork
    aix_net.get_interfaces_info('./ansible/module_utils/facts/network/ifconfig_aix_example')
    # assertEqual(first, second, msg=None)
    # assertRegexpMatches(text, regexp, msg=None)
    # assertTrue(expr, msg=None)
    return 0

# Generated at 2022-06-13 01:18:00.625660
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    AIX_get_default_interfaces = AIXNetwork().get_default_interfaces
    assert AIX_get_default_interfaces('/sbin/route') == ({'interface': 'en4', 'gateway': '192.0.2.1'}, {'interface': 'en4', 'gateway': '2001:db8:0:1::1'})


# Generated at 2022-06-13 01:18:15.525599
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    assert AIXNetworkCollector.__module__ == 'ansible.module_utils.facts.network.aix'
    assert AIXNetworkCollector._fact_class == AIXNetwork
    assert AIXNetworkCollector._platform == 'AIX'

# Generated at 2022-06-13 01:18:27.612247
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    aix_net = AIXNetwork()

    def _test(expected_result):
        default_int = aix_net.get_default_interfaces('/sbin/route')
        assert default_int['v4']['gateway'] == expected_result['v4']['gateway'] and default_int['v4']['interface'] == expected_result['v4']['interface'] and \
               default_int['v6']['gateway'] == expected_result['v6']['gateway'] and default_int['v6']['interface'] == expected_result['v6']['interface']

    # no route, no netstat
    _test({'v4': {'gateway': '', 'interface': ''}, 'v6': {'gateway': '', 'interface': ''}})

    #

# Generated at 2022-06-13 01:18:34.750310
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    module = MagicMock()
    module.run_command.return_value = (0, '', '')
    module.get_bin_path.return_value = '/usr/bin/netstat'

    an = AIXNetwork(module)
    expected = {'gateway': '9.9.9.9', 'interface': 'en1'}
    actual = an.get_default_interfaces('/sbin/route')
    assert_equal(expected, actual)



# Generated at 2022-06-13 01:18:37.347182
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    collector = AIXNetworkCollector()
    assert collector.platform == 'AIX'
    assert collector.fact_class == AIXNetwork


# Generated at 2022-06-13 01:18:38.340121
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    p = AIXNetworkCollector()
    asse

# Generated at 2022-06-13 01:18:39.639842
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    assert isinstance(NetworkCollector._instance, AIXNetworkCollector)

# Generated at 2022-06-13 01:18:45.524960
# Unit test for method get_interfaces_info of class AIXNetwork

# Generated at 2022-06-13 01:18:48.154705
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    """
    Constructor test of AIXNetworkCollector
    """
    assert AIXNetworkCollector()

# Generated at 2022-06-13 01:18:49.206510
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    AIXNetworkCollector()

# Generated at 2022-06-13 01:18:55.981800
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    from ansible.module_utils.facts.network.aix import AIXNetwork
    from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork

    net_abstract = AIXNetwork()
    # Test for IPv4
    net_abstract.get_default_interfaces(route_path='/usr/bin/netstat')['default4']['gateway'] == \
        GenericBsdIfconfigNetwork.get_default_interfaces(route_path='/usr/bin/netstat')['default4']['gateway']

# Generated at 2022-06-13 01:19:22.398361
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    from ansible.module_utils.facts.network.aix import AIXNetwork
    module = AnsibleModule(argument_spec=dict())
    instance = AIXNetwork(module)
    (interfaces, ips) = instance.get_interfaces_info('/usr/sbin/ifconfig', '-a')
    assert 'lo0' in interfaces
    assert '10.1.1.1' in ips['all_ipv4_addresses']
    assert 'fe80::1' in ips['all_ipv6_addresses']

# Generated at 2022-06-13 01:19:32.884707
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    module = AnsibleModuleMock()
    module.get_bin_path = lambda x: "/usr/bin/route"
    module.run_command = lambda x: (0, 'default 192.168.0.1 UG  1   0  en0\ndefault fe80::%utun0 UGcI 0 3 utun0', '')
    aix_network = AIXNetwork()
    aix_network.module = module

    # call the function under test
    v4, v6 = aix_network.get_default_interfaces('')
    assert v4['gateway'] == '192.168.0.1'
    assert v4['interface'] == 'en0'
    assert v6['gateway'] == 'fe80::%utun0'

# Generated at 2022-06-13 01:19:40.560024
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    module = NetworkCollector._create_module_mock()
    network_module = AIXNetworkCollector(module=module,
                                         config=dict(cache_max_age=1),
                                         condition=dict(gather_subset='!config,min'))  # force get_default_interfaces method
    # mock netstat_path binary
    module.get_bin_path.return_value = '/usr/bin/netstat'


# Generated at 2022-06-13 01:19:50.160062
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    modules = dict(run_command=run_command_mock)
    set_module_args(dict(gather_subset=['!all', '!min']))
    result = dict(changed=False, ansible_facts=dict(ansible_net_interfaces={}, ansible_net_gather_network_resources={}))
    facts_instance = AIXNetwork('module', modules, result)
    interfaces = {'v4': {'gateway': '192.168.1.1', 'interface': 'en0'}, 'v6': {'gateway': 'fe80::123:789:abc:def%p7p1', 'interface': 'p7p1'}}
    assert facts_instance.get_default_interfaces('/etc/my_route') == interfaces


# Generated at 2022-06-13 01:19:52.160055
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    assert issubclass(AIXNetworkCollector, NetworkCollector)
    assert AIXNetworkCollector._platform == 'AIX'


# Generated at 2022-06-13 01:19:59.726478
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    # Mocked values for hostname and route command
    def _check_config_merge(ansible_facts, merge):
        assert 'ansible_hostname' in ansible_facts
        assert 'ansible_default_ipv4' in ansible_facts
        assert 'ansible_default_ipv6' in ansible_facts
        assert ansible_facts['ansible_default_ipv4']['gateway'] == merge['v4']['gateway']
        assert ansible_facts['ansible_default_ipv4']['interface'] == merge['v4']['interface']
        assert 'gateway' in ansible_facts['ansible_default_ipv6']
        assert 'interface' in ansible_facts['ansible_default_ipv6']


# Generated at 2022-06-13 01:20:05.022208
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    module = AnsibleModule(argument_spec=dict())
    if not module.check_mode:
        module.exit_json(ansible_facts={'network': AIXNetwork(module).get_interfaces_info(
            module.get_bin_path('ifconfig'))[1]})


# Generated at 2022-06-13 01:20:15.341518
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    #import pprint
    #pp = pprint.PrettyPrinter(indent=2)

    net = AIXNetwork()
    net.module = MockModule()
    net.module.run_command.return_value = (1, "entstat output", "entstat error")
    net.module.get_bin_path.return_value = "/usr/bin/netstat"


# Generated at 2022-06-13 01:20:23.107149
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork

    # some general variables
    ifconfig_path = '/usr/bin/ifconfig'
    ifconfig_options = '-a'
    interfaces = {}
    current_if = {}
    ips = dict(
        all_ipv4_addresses=[],
        all_ipv6_addresses=[],
    )


# Generated at 2022-06-13 01:20:33.842897
# Unit test for method get_default_interfaces of class AIXNetwork

# Generated at 2022-06-13 01:21:23.422417
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    from ansible.module_utils.facts.network.net_tools.aix import AIXNetwork
    from ansible.module_utils.facts.network.net_tools.generic_bsd import GenericBsdNetwork

    # Set interface info
    interface = {
        'v4': {
            'gateway': '10.1.1.254',
            'interface': 'en0'
        },
        'v6': {
            'gateway': '2001:db8:42:42::254',
            'interface': 'en0'
        }
    }

    # Set input output
    aixnet = AIXNetwork(None)

# Generated at 2022-06-13 01:21:27.822600
# Unit test for method get_interfaces_info of class AIXNetwork

# Generated at 2022-06-13 01:21:35.919949
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    class AnsibleModuleMock(object):
        def __init__(self):
            self.params = None

        def get_bin_path(self, command):
            return '/usr/bin/netstat'


# Generated at 2022-06-13 01:21:37.785555
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    try:
        AIXNetworkCollector()
    except Exception:
        raise AssertionError("Construction of class AIXNetworkCollector failed.")


# Generated at 2022-06-13 01:21:45.624499
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():

    from ansible.module_utils.facts.network.aix import AIXNetwork
    from ansible.module_utils.facts.network.aix import test_AIXNetwork_get_interfaces_info

    aixnetwork = AIXNetwork()

    ifconfig_path = aixnetwork.module.get_bin_path('ifconfig')

    interfaces, ips = aixnetwork.get_interfaces_info(ifconfig_path, '-a')

    if interfaces:
        has_address = False
        assert 'lo0' in interfaces
        assert len(interfaces['lo0']['flags']) == 11
        assert 'UP' in interfaces['lo0']['flags']
        assert 'mtu' in interfaces['lo0']
        assert interfaces['lo0']['mtu'] == '65536'


# Generated at 2022-06-13 01:21:53.057361
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    # Test 1: bash returns returns 'netstat -nr' output
    class UName:
        def __init__(self, bin_path_value='uname'):
            self.bin_path_value = bin_path_value

        def get_bin_path(self, arg, opt_dirs=[]):
            return self.bin_path_value

    class RC:
        def __init__(self, rc_value=0, out_value='', err_value=''):
            self.rc_value = rc_value
            self.out_value = out_value
            self.err_value = err_value

        def run_command(self, arg, check_rc=True):
            return (self.rc_value, self.out_value, self.err_value)


# Generated at 2022-06-13 01:21:55.489596
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    network = AIXNetwork()
    interfaces = network.get_interfaces_info('/sbin/ifconfig', '-a')[0]
    assert len(interfaces) > 0


# Generated at 2022-06-13 01:21:57.838870
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    myAix = AIXNetworkCollector()
    assert myAix.__class__.__name__ == 'AIXNetworkCollector'

# Generated at 2022-06-13 01:22:08.709041
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    test_module = AnsibleModule(argument_spec={})
    network = AIXNetwork(test_module)

    # Put the test input into the system's PATH environment variable
    test_bin_dir = os.path.join(
        os.path.normpath(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))),
        'test',
        'units',
        'module_utils',
        'facts',
        'network',
        'bin')
    os.environ['PATH'] = '%s:%s' % (os.environ['PATH'], test_bin_dir)

    # Test for case where all default routes are IPv4

# Generated at 2022-06-13 01:22:16.404231
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    module = AnsibleModule({})

    # set up class instance
    Network = AIXNetwork(module)

    route_path = '/usr/bin/netstat'

    # test with a standard route-command output

# Generated at 2022-06-13 01:23:50.104852
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    """Test constructor and properties of AIXNetworkCollector"""

    collector = AIXNetworkCollector(
        module=dict(run_command=dict(return_value=(0, '', ''))))

    assert collector
    assert collector.platform == 'AIX'
    assert collector.fact_class == AIXNetwork


# Generated at 2022-06-13 01:23:57.992195
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    from ansible.module_utils.facts.network.aix import AIXNetwork
    AIXNetwork = AIXNetwork()
    ifconfig_path = AIXNetwork.module.get_bin_path('ifconfig')
    ifconfig_options = '-a'

# Generated at 2022-06-13 01:24:04.514927
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    module = AnsibleModule(argument_spec=dict())
    network = AIXNetwork(module)
    network.route_path = '/usr/sbin/netstat'

    # options string only
    rc, out, err = module.run_command("echo 'default gateway 192.168.1.1 dev em0'")
    v4, v6 = network.get_default_interfaces('')
    assert v4['gateway'] == '192.168.1.1'
    assert v4['interface'] == 'em0'
    assert v6 == {}

    # options string only
    rc, out, err = module.run_command("echo 'default gateway fe80::212:4fff:fe95:4e3 dev em0'")
    v4, v6 = network.get_default_interfaces('')

# Generated at 2022-06-13 01:24:05.895978
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    """
    This is test of constructor of class AIXNetworkCollector.
    """
    AIXNetworkCollector()



# Generated at 2022-06-13 01:24:10.719601
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    # check if function works with string as arg
    small_interface = AIXNetwork().get_default_interfaces('default 1')
    assert small_interface['v4']['gateway'] == '1'
    assert small_interface['v4']['interface'] == 'default'
    assert 'v6' not in small_interface
    # check if function works with empty string as arg
    small_interface = AIXNetwork().get_default_interfaces('')
    assert small_interface['v4']['gateway'] == ''
    assert 'v6' not in small_interface
    assert small_interface['v4']['interface'] == ''

# Generated at 2022-06-13 01:24:19.936655
# Unit test for method get_interfaces_info of class AIXNetwork

# Generated at 2022-06-13 01:24:20.784509
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    x = AIXNetworkCollector()


# Generated at 2022-06-13 01:24:30.175310
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    """
    This will test if the method get_default_interfaces() of class AIXNetwork is working as expected
    """

    # Define test values
    data1 = 'default 192.168.0.1 UGS 0 1500 en1'
    data2 = 'default 2000:1::1 UGS 0 1500 en2'
    expected_v4 = {'gateway': '192.168.0.1', 'interface': 'en1'}
    expected_v6 = {'gateway': '2000:1::1', 'interface': 'en2'}

    # Define test variables
    route_path = '/sbin/route'
    rc = 0
    out = data1 + '\n' + data2
    err = ''

    # Create an AIXNetwork object
    network = AIXNetwork()

    # Force the module to

# Generated at 2022-06-13 01:24:38.709480
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():

    test_module = AnsibleModule(
        argument_spec=dict(
            route_path=dict(type='str', required=False),
        ),
        supports_check_mode=True
    )

    test_module.run_command = MagicMock(return_value=(0, TEST_NETSTAT_TEXT, None))

    test_network = AIXNetwork(test_module)

    assert test_network.get_default_interfaces(route_path='/usr/bin/netstat') == ({'gateway': '172.16.12.1', 'interface': 'en0'}, {'gateway': 'fe80::21a:6eff:fe6d:1c3d', 'interface': 'en0'})


# Generated at 2022-06-13 01:24:41.570932
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    obj = AIXNetworkCollector()
    # _fact_class is hardcoded to AIXNetwork
    assert obj._fact_class.platform == 'AIX'
    # _platform is hardcoded to AIX
    assert obj._platform == 'AIX'