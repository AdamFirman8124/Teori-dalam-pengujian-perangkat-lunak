

# Generated at 2022-06-13 01:16:53.245456
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    AIXNetworkCollector()


# Generated at 2022-06-13 01:17:03.344985
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    """
    Constructor of class AIXNetworkCollector
    """
    aix_nc = AIXNetworkCollector()
    aix_nc._check_files()
    assert aix_nc._platform == 'AIX'
    assert aix_nc._excluded_interfaces == []
    assert aix_nc._excluded_interfaces_re == []
    assert aix_nc._valid_proto == ['inet', 'inet6', 'vlan']
    assert aix_nc._device_options == ['v4']
    assert aix_nc._route_command == 'netstat -nr'
    assert aix_nc._gather_routes == False
    assert aix_nc._arp_path == '/usr/sbin/arp'


# Generated at 2022-06-13 01:17:11.650914
# Unit test for method get_interfaces_info of class AIXNetwork

# Generated at 2022-06-13 01:17:13.435212
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    # use the constructor for class AIXNetworkCollector
    collector = AIXNetworkCollector()
    assert collector._platform == 'AIX'
    assert collector._fact_class.platform == 'AIX'

# Generated at 2022-06-13 01:17:15.190884
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    assert isinstance(AIXNetworkCollector(), NetworkCollector)


# Generated at 2022-06-13 01:17:25.108118
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    from ansible.module_utils.facts.network.aix import AIXNetwork

    test_cases = []
    test_cases.append([['default xxx.xxx.xxx.xxx xxx.xxx.xxx.xxx UGS xxx'],
                       {'v4': {'gateway': 'xxx.xxx.xxx.xxx', 'interface': 'xxx'}, 'v6': {}}])

# Generated at 2022-06-13 01:17:27.440461
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
  # Invoke method under test
  m_AIXNetwork = AIXNetwork()
  m_AIXNetwork.get_default_interfaces(None)

# Generated at 2022-06-13 01:17:30.107418
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    """
    The class AIXNetworkCollector must not be unit tested.
    """
    assert False

# Generated at 2022-06-13 01:17:34.896809
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    module = AnsibleModule(
        argument_spec = dict(
        ),
        supports_check_mode=True
    )
    ansible_facts = {'ansible_system': 'AIX'}
    ac = AIXNetworkCollector(module=module, facts=ansible_facts)
    assert ac._fact_class.platform == 'AIX'


# Generated at 2022-06-13 01:17:37.935117
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    """
    Constructor for class AIXNetworkCollector
    """
    aix_network_collector = AIXNetworkCollector()
    assert(isinstance(aix_network_collector, NetworkCollector))

# Unit tests for class AIXNetwork

# Generated at 2022-06-13 01:17:52.640130
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    assert AIXNetworkCollector._platform == 'AIX'
    assert AIXNetworkCollector._fact_class is AIXNetwork

# Generated at 2022-06-13 01:17:53.399121
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    assert True

# Generated at 2022-06-13 01:17:57.686528
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )
    collector = AIXNetworkCollector(module=module)
    assert collector.facts == {'default_ipv4': {}, 'default_ipv6': {}, 'interfaces': {}, 'all_ipv4_addresses': [], 'all_ipv6_addresses': []}



# Generated at 2022-06-13 01:18:02.590565
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    c = AIXNetworkCollector(dict(module=dict()), None)
    assert c.__dict__ == {'module': dict(), '_facts': {'all_ipv4_addresses': [], 'all_ipv6_addresses': [], 'default_ipv4': {}, 'default_ipv6': {}, 'interfaces': {}, 'neighbors': {}}}


# Generated at 2022-06-13 01:18:08.508215
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    fake_module = FakeModule({})

    # fake run_command
    def run_command(args, *kwargs):
        for i in range(len(args)):
            if args[i] == '/usr/bin/netstat' and i < len(args)-1 and args[i+1] == '-nr':
                return 0, 'default 0.0.0.0 UG en0\ndefault fe80::%eth0 U en0\n', ''

# Generated at 2022-06-13 01:18:09.764140
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    """Unit test for constructor of class AIXNetworkCollector"""
    AIXNetworkCollector()

# Generated at 2022-06-13 01:18:17.794543
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    mock_module = Mock(module)
    mock_module.run_command.return_value = (0, '', '')
    mock_module.get_bin_path.return_value = '/usr/sbin/ifconfig'

    interfaces = dict(
        en0=dict(device='en0', ipv4=[], ipv6=[], macaddress='unknown', type='unknown', mtu=None),
        en1=dict(device='en1', ipv4=[], ipv6=[], macaddress='unknown', type='unknown', mtu=None),
        lo0=dict(device='lo0', ipv4=[], ipv6=[], macaddress='unknown', type='unknown', mtu=None)
    )

# Generated at 2022-06-13 01:18:25.107580
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    module = AnsibleModule(argument_spec={
        'gather_subset': dict(type='list', default=['default'])
    })

    network_collector = AIXNetworkCollector(module)
    network_collector.collect()

    # no need to gather anything else
    module.exit_json(ansible_facts={
        'ansible_net_gather_subset': ['default']
    })

# for testing with this file directly

# Generated at 2022-06-13 01:18:36.369781
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():

    test_line_1 = 'en0       flags=1c43<UP,BROADCAST,RUNNING,ALLMULTI,SIMPLEX,MULTICAST>      mtu 1500'
    test_words_1 = test_line_1.split()

    test_line_2 = '        options=3<RXCSUM,TXCSUM>'
    test_words_2 = test_line_2.split()

    test_line_3 = '        media: Ethernet autoselect (1000baseT)'
    test_words_3 = test_line_3.split()

    test_line_4 = '        status: active'
    test_words_4 = test_line_4.split()


# Generated at 2022-06-13 01:18:44.164070
# Unit test for method get_interfaces_info of class AIXNetwork

# Generated at 2022-06-13 01:19:02.139163
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    ansible_module = setup_ansible_module_object()
    f = AIXNetwork(ansible_module)
    f.get_interfaces_info('/bin/notifconfig')



# Generated at 2022-06-13 01:19:11.648742
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    from ansible.module_utils.facts import Collector

    # collect test data
    m_params = dict(
        gather_subset='!all',
        gather_network_resources='yes'
    )
    collector = Collector(m_params=m_params, module=None, task_vars=None)
    res_facts = collector.collect()
    interfaces = res_facts['ansible_interfaces']
    interface_re = r'^\w*\d*: '
    intf_dict = dict()
    option_re = r'\s*options=(.*)'
    inet_re = r'\s*inet ([\d\.]*)'
    inet6_re = r'\s*inet6 (.*):'

# Generated at 2022-06-13 01:19:15.407785
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    import json

    interfaces = AIXNetwork()
    interfaces_info = interfaces.get_interfaces_info('/usr/bin/ifconfig', ifconfig_options='-a')
    print(json.dumps(interfaces_info, indent=4, sort_keys=True))

# Generated at 2022-06-13 01:19:17.412242
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    assert AIXNetworkCollector.platform == 'AIX'
    assert AIXNetworkCollector._fact_class == AIXNetwork
    assert AIXNetworkCollector._platform == 'AIX'

# Generated at 2022-06-13 01:19:24.178355
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    module = AnsibleModule(argument_spec=dict())

    mocker_get_bin_path = mocker.patch('ansible.module_utils.facts.network.aix.AIXNetwork.get_bin_path')
    mocker_get_bin_path.return_value = 'netstat'

    mocker_run_command = mocker.patch('ansible.module_utils.facts.network.aix.AIXNetwork.run_command')
    mocker_run_command.return_value = (0, 'default :: gateway 192.168.1.1\n', '')

    network_object = AIXNetwork(module)
    network_object.get_default_interfaces('')
    assert network_object.default_ipv4['gateway'] == '192.168.1.1'



# Generated at 2022-06-13 01:19:25.784441
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    """
    This does not work.
    The module.run_command() can not be mocked.
    """
    pass

# Generated at 2022-06-13 01:19:29.838025
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    """
    This is a unit test for constructor of class AIXNetworkCollector
    """

    assert AIXNetworkCollector._platform == 'AIX'
    assert AIXNetworkCollector._fact_class is AIXNetwork

# Generated at 2022-06-13 01:19:30.167365
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    pass

# Generated at 2022-06-13 01:19:38.192601
# Unit test for method get_interfaces_info of class AIXNetwork

# Generated at 2022-06-13 01:19:45.813282
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    module = NetworkCollector()
    module.get_bin_path = lambda *_: '/usr/bin/path'
    module.run_command = lambda *_: (0, 'default 192.168.1.1 UGS 0 0 en0\ndefault ::1 UGS 0 0 lo0\n', '')
    expected = (dict(gateway='192.168.1.1', interface='en0'), dict(gateway='::1', interface='lo0'))
    assert AIXNetwork().get_default_interfaces('/usr/local/sbin/route') == expected



# Generated at 2022-06-13 01:20:20.984832
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    ifconfig_path = '/usr/sbin/ifconfig'
    ifconfig_options = '-a'

    aix_network = AIXNetwork()
    interfaces, ips = aix_network.get_interfaces_info(ifconfig_path, ifconfig_options)

    assert 'en1' in interfaces
    assert 'en1' in ips['all_ipv4_addresses']
    assert 'en1' in ips['all_ipv6_addresses']
    assert 'en2' in interfaces
    assert 'en2' in ips['all_ipv4_addresses']
    assert 'en2' in ips['all_ipv6_addresses']

    assert interfaces['en1']['type'] == 'ether'
    assert interfaces['en2']['type'] == 'ether'

# Generated at 2022-06-13 01:20:32.508678
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():

    class MockModule:
        def __init__(self, run_command_rc, run_command_out, run_command_err, get_bin_path_rc, get_bin_path_value):
            self.run_command_rc = run_command_rc
            self.run_command_out = run_command_out
            self.run_command_err = run_command_err
            self.get_bin_path_rc = get_bin_path_rc
            self.get_bin_path_value = get_bin_path_value

        def run_command(self, args, check_rc=True):
            if self.run_command_rc is None:
                self.run_command_rc = 0
            if self.run_command_out is None:
                self.run_command_out = ""

# Generated at 2022-06-13 01:20:42.874747
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    AIXNetworkInstance = AIXNetwork()

    def touch(path):
        with open(path, 'a'):
            os.utime(path, None)

    fake_path = '/tmp/ifconfig.txt'

    touch(fake_path)


# Generated at 2022-06-13 01:20:49.951935
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    # - filename defined in the mock_open_fixture
    # - ifconfig_path defined in the @mock.patch decorator
    # - ifconfig_options defined in the function declaration
    with open('/usr/sbin/ifconfig', 'r') as myfile:
        data = myfile.read().replace('\n', '')
    FakeAnsibleModule.fixture_data['src'] = '/usr/sbin/ifconfig'
    FakeAnsibleModule.fixture_data['content'] = data
    FakeModule().run()

# Generated at 2022-06-13 01:20:56.705992
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True,
    )

    route_path = module.get_bin_path('netstat')
    if not route_path:
        module.fail_json(msg="netstat not found")

    nc = AIXNetwork()
    (ipv4, ipv6) = nc.get_default_interfaces(route_path)
    assert len(ipv4) > 0
    assert len(ipv6) > 0


# Generated at 2022-06-13 01:21:05.430450
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    """Unit test for method get_default_interfaces of class AIXNetwork.
    """
    from .network_parsers import AIXNetwork, GenericBsdNetwork
    import textwrap
    expected_interface = {'v4': {'gateway': '192.168.1.254', 'interface': 'en0'}, 'v6': {'gateway': 'fe80::cc:caff:fe66:6e00%en0', 'interface': 'en0'}}

# Generated at 2022-06-13 01:21:09.162848
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    # init
    module = AnsibleModuleMock()
    c = AIXNetwork(module=module)

    # input
    route_path = '/etc/hosts'

    # expected
    interface = dict(v4={}, v6={})

    # test
    assert c.get_default_interfaces(route_path) == (interface['v4'], interface['v6'])



# Generated at 2022-06-13 01:21:19.183585
# Unit test for method get_interfaces_info of class AIXNetwork

# Generated at 2022-06-13 01:21:22.604452
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    """
    This is a unit test for the class AIXNetworkCollector
    """
    net_collect = AIXNetworkCollector()
    assert net_collect.platform == 'AIX'
    assert net_collect._platform == 'AIX'
    assert net_collect._fact_class == AIXNetwork

# Generated at 2022-06-13 01:21:24.184440
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    fact_class = AIXNetworkCollector()._fact_class
    assert fact_class == AIXNetwork


# Generated at 2022-06-13 01:22:27.072413
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():

    from ansible.module_utils.facts import Collector
    import sys
    import os
    import copy

    sys.path.append(os.path.join(os.path.dirname(__file__), '../../../../plugins/modules/network'))
    from network_common import NetworkModule

    # create dummy module and facts
    module = NetworkModule(argument_spec={}, supports_check_mode=False)
    module.params = {}
    facts = Collector().collect(module)

    aix = AIXNetwork(module)

    default_v4 = copy.deepcopy(aix.interface['ipv4'])
    default_v6 = copy.deepcopy(aix.interface['ipv6'])

    # test with obsolete /sbin/route

# Generated at 2022-06-13 01:22:35.411888
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    """
    Unit test for the AIXNetwork.get_interfaces_info() method.
    """
    module = AnsibleModule()
    current_if = {}
    ips = dict(
        all_ipv4_addresses=[],
        all_ipv6_addresses=[],
    )

# Generated at 2022-06-13 01:22:44.105108
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    data = '''
default 192.168.1.1 UG en0
default :: UG lo0
'''
    module = 'aix_network_facts'
    facts_collector = AIXNetworkCollector(module)
    ifconfig_path = '/sbin/ifconfig'
    interfaces = facts_collector.get_default_interfaces(ifconfig_path)

    assert interfaces['default4']['gateway'] == '192.168.1.1'
    assert interfaces['default4']['interface'] == 'en0'
    assert interfaces['default6']['gateway'] == '::'
    assert interfaces['default6']['interface'] == 'lo0'



# Generated at 2022-06-13 01:22:49.819701
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    m = type('module', (object,),
             {'run_command': lambda x, *args, **kwargs: (0, x[1], '')})()
    result = AIXNetwork(m).get_default_interfaces('/sbin/netstat')
    assert result[0] == {'gateway': '192.168.1.1', 'interface': 'en0'}
    assert result[1] == {'gateway': 'fe80::250:56ff:fe8e:b35c%en0', 'interface': 'en0'}


# Generated at 2022-06-13 01:22:53.159472
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    test_module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )
    test_module.exit_json(changed=False,
                          ansible_facts=dict(ansible_net_interfaces=AIXNetwork(test_module).get_interfaces()))



# Generated at 2022-06-13 01:22:58.853268
# Unit test for method get_interfaces_info of class AIXNetwork

# Generated at 2022-06-13 01:23:03.314359
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    # create mock object for module
    module = MockModule()

    # we want to mock ifconfig and lsattr output for an interface en0

# Generated at 2022-06-13 01:23:12.200151
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    """
    Test method get_default_interfaces / class AIXNetwork.
    """

    # define variables for test
    z_netstat_data_1 = (
        'default\t192.0.2.1\t0\t0\tUGS\tlo0\n'
        'default\t192.0.2.2\t0\t0\tUGS\tlo1\n'
        'default\t192.0.2.3\t0\t0\tUGS\tlo2\n'
    )

# Generated at 2022-06-13 01:23:15.885754
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():

    plugin = AIXNetworkCollector

    # Constructor of class AIXNetworkCollector creates a NetworkCollector object,
    # and assigns a AIXNetwork object to its '_fact_class' attribute
    assert plugin._fact_class == AIXNetwork

    # Platform name of AIX is 'AIX', and it is assigned to '_platform'
    # attribute of NetworkCollector object
    assert plugin._platform == 'AIX'

# Generated at 2022-06-13 01:23:23.754586
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    import tempfile
    # define a test file in memory
    netstat_path = tempfile.NamedTemporaryFile(mode='w+')

    # write the following text
    netstat_path.write('''
default       192.168.1.1        UG        0      0        en0
default       192.168.1.1        UG        0      0        en0
default       ::1                UGc       0      0        en0
default       fe80::1%lo0        UGcI      0      0        lo0
''')
    # return to the beginning of the file
    netstat_path.seek(0)

    # create a test module
    module = type('obj', (object,), {'get_bin_path': lambda self, path: netstat_path.name})

    # create a test

# Generated at 2022-06-13 01:25:14.322237
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    """Unit test for constructor of class AIXNetworkCollector"""
    # Test without any parameter
    network_collector = AIXNetworkCollector()
    assert network_collector
    assert network_collector.fact_class == AIXNetwork
    assert network_collector.platform == 'AIX'
    # Test with a fake fact_class
    network_collector = AIXNetworkCollector('fake_fact_class')
    assert network_collector
    assert network_collector.fact_class == 'fake_fact_class'



# Generated at 2022-06-13 01:25:21.023390
# Unit test for method get_interfaces_info of class AIXNetwork

# Generated at 2022-06-13 01:25:23.201784
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    collector = AIXNetworkCollector()
    assert collector.platform == 'AIX'
    assert collector.fact_class.__name__ == 'AIXNetwork'

# Generated at 2022-06-13 01:25:31.741620
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    import os
    platform = 'AIX'
    test_dir = os.path.dirname(os.path.realpath(__file__))
    test_file = os.path.join(test_dir, 'test_'+platform+'_ifconfig.txt')
    test_file_wpar = os.path.join(test_dir, 'test_' + platform + '_ifconfig_wpar.txt')

    # Test the function to be sure it is working properly
    # This test is a little different for AIX because AIX does not show the MTU in the output of ifconfig
    # Also, the MAC address shown by ifconfig is for the logical network interface, not for the physical device
    # Ifconfig still used to get the link status
    # To get the actual MAC address we have to use entstat
    # To get the actual

# Generated at 2022-06-13 01:25:39.623578
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    module = AnsibleModule(
        argument_spec=dict(
            gather_subset=dict(default=[], type='list')
        ),
        supports_check_mode=True
    )
    # create AIXNetwork object for testing
    network = AIXNetwork(module)
    interfaces = {}

    netstat_path = module.get_bin_path('netstat')
    # test when netstat is present
    if netstat_path:
        interfaces = network.get_default_interfaces(netstat_path)
        assert 'gateway' in interfaces
        assert 'interface' in interfaces

    netstat_path = None
    # test when netstat is not present
    interfaces = network.get_default_interfaces(netstat_path)
    assert not interfaces



# Generated at 2022-06-13 01:25:49.190069
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    def test(in_mocker):
        ifconfig_path = '/usr/sbin/ifconfig'
        ifconfig_options = '-a'
        # mock output of ifconfig command

# Generated at 2022-06-13 01:25:55.646379
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    module = FakeAnsibleModule()

    words = ['default', '10.0.0.1', '0.0.0.0', 'UG', '0', '0', '0', 'em1']
    module.run_command_result = (0, ''.join(words), None)
    interface = dict(v4={}, v6={})

    netstat_path = '/usr/bin/netstat'
    module.get_bin_path_result = netstat_path

    aix_network = AIXNetwork(module)

    interface['v4']['gateway'], interface['v6']['interface'] = aix_network.get_default_interfaces(netstat_path)
    assert interface['v4']['gateway'] == words[1]

# Generated at 2022-06-13 01:26:03.043358
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    module = AnsibleModule(argument_spec=dict(gather_subset=dict(default=['!all'], type='list')))
    result = dict(changed=False)
    # instantiate our NetworkCollector
    collect_subset = module.params['gather_subset']
    network_collector = AIXNetworkCollector(module=module, collect_subset=collect_subset)

    # instantiate our AIXNetwork object
    network_object = network_collector.get_network_objects()[0]

    # setup our 'ping' result

# Generated at 2022-06-13 01:26:04.972027
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    collector = AIXNetworkCollector()
    assert collector.__class__.__name__ == 'AIXNetworkCollector'


# Generated at 2022-06-13 01:26:12.647551
# Unit test for method get_interfaces_info of class AIXNetwork