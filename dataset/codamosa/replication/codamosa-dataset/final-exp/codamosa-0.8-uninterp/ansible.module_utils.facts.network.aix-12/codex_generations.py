

# Generated at 2022-06-13 01:17:01.142473
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():

    class AIXModule(object):

        def __init__(self):
            self.params = {}
            self.run_command_calls = []
            self.run_command_results = []
            self.run_command_checkrcs = []

        def get_bin_path(self, path):
            return "/usr/bin/%s" % path

        def run_command(self, command, check_rc=True):
            self.run_command_calls.append(command)
            self.run_command_checkrcs.append(check_rc)
            return self.run_command_results.pop(0)

    class AIXNetwork(AIXNetwork):

        def __init__(self, module):
            self.module = module


    module = AIXModule()

    net = AIXNetwork(module)

# Generated at 2022-06-13 01:17:10.321660
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    test_module = NetworkCollector()
    test_module.get_interfaces_info = AIXNetwork.get_interfaces_info
    test_module.run_command = lambda *_, **__: (0, SAMPLE_IFCONFIG_A, '')
    test_module.get_bin_path = lambda *_, **__: None

    interfaces, _ = test_module.get_interfaces_info('')

# Generated at 2022-06-13 01:17:19.116780
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    net = AIXNetwork(None)

    defs = net.get_default_interfaces(None)
    assert defs[0]['gateway'] == '192.168.1.1'
    assert defs[0]['interface'] == 'br0'
    assert defs[1]['gateway'] == 'fe80::1'
    assert defs[1]['interface'] == 'br0'



# Generated at 2022-06-13 01:17:21.739847
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    mod = None
    aixnc = AIXNetworkCollector(mod)
    assert aixnc._fact_class == AIXNetwork
    assert aixnc._platform == 'AIX'

# Generated at 2022-06-13 01:17:26.129121
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    # create AIXNetworkCollector object
    test_obj = AIXNetworkCollector()
    # assert fact class (within fact_class attribute)
    assert test_obj.fact_class == AIXNetwork
    # assert platform (within _platform attribute)
    assert test_obj._platform == 'AIX'


# Generated at 2022-06-13 01:17:36.512155
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    module = AnsibleModule(
        argument_spec=dict(
            gather_subset=dict(default=['!all'], type='list'),
            command=dict(default='ifconfig'),
        ),
        supports_check_mode=True,
    )

    # Create fake ifconfig output.
    default_interfaces = {
        'v4': {'gateway': '192.168.1.1',
               'interface': 'lo0'},
        'v6': {}}
    netstat_path = module.get_bin_path('netstat')

# Generated at 2022-06-13 01:17:45.939962
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    import os
    import sys
    from ansible.module_utils.facts.network.aix import AIXNetwork
    from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork
    from ansible.module_utils.facts.network.generic_bsd import GenericBsdNetwork
    from ansible.module_utils.facts.network.generic_bsd import GenericBsdNetworkCollector
    from ansible.module_utils.facts.facts import Facts
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.six.moves import filter
    import ansible.module_utils.facts.network.aix

    if os.isatty(sys.stdin.fileno()):
        raise AssertionError("stdin is not a pipe")

    stdin

# Generated at 2022-06-13 01:17:56.706048
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    aix_ifconfig_path='/usr/sbin/ifconfig'

    # create a mock module
    module = AnsibleModule(
        argument_spec = dict()
    )

    # create an instance of the AIXNetwork plugin class
    n = AIXNetwork(module)

    # generate test data and run get_interfaces_info on it
    result = dict()

    with open('/etc/ansible/facts.d/test_data/AIX_ifconfig_a', 'r') as f:
        data = f.readlines()
        data = [line.strip() for line in data]

        result = n.get_interfaces_info(aix_ifconfig_path, ifconfig_options='-a')

    # check if result is as expected

# Generated at 2022-06-13 01:17:59.864699
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    """Test constructor of the generic network class"""

    network_facts_class = AIXNetworkCollector()

    assert isinstance(network_facts_class._fact_class, AIXNetwork)
    assert network_facts_class._platform == 'AIX'

# Generated at 2022-06-13 01:18:07.033511
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    # test data
    out = '''
default  10.0.0.1 UG        0 0   en0
default  fe80::b3a3:d0ff:fea3:84a9%en0 UG        0 0   en0
'''
    my_class = AIXNetwork(None)
    expected_result = {'gateway': '10.0.0.1', 'interface': 'en0'}, {'gateway': 'fe80::b3a3:d0ff:fea3:84a9%en0', 'interface': 'en0'}
    # call the method
    result = my_class.get_default_interfaces(None)
    # make asserts
    assert result == expected_result

# Generated at 2022-06-13 01:18:29.186368
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    module = NetworkCollector()

    # Test 1: Typical output for en0
    # Test input
    test_lines = """
Internet  172.24.1.1           1   en0      UGSc           28
Internet  172.24.2.2           1   en1      UGScI          0     en1
Internet6 fe80::7f:ff:fe02:0%1  1   en0      UGSc           0     en0
Internet6 fe80::7f:ff:fe03:0%2  1   en1      UGScI          0     en1
"""
    new_net_lines = test_lines.split('\n')
    # Result expected
    test_result = {'interface': 'en0', 'gateway': '172.24.1.1'}
    # Call the method
   

# Generated at 2022-06-13 01:18:34.848934
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    def run_get_default_interfaces(params, expected):
        testobj = AIXNetwork(params)
        actual = testobj.get_default_interfaces(params['route_path'])
        assert actual == expected

    for scenario in TEST_SCENARIOS_GET_DEFAULT_INTERFACES:
        yield run_get_default_interfaces, scenario['params'], scenario['expected']


# Generated at 2022-06-13 01:18:42.527444
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    module = AnsibleModule(argument_spec={})
    module.exit_json = Mock(return_value=None)
    module.run_command = Mock(return_value=(0, 'default 172.20.58.1 UG 0 0 en0', ''))
    module.get_bin_path = Mock(return_value='/usr/bin/netstat')
    interfaces = AIXNetwork(module)
    v4, v6 = interfaces.get_default_interfaces('/usr/bin/netstat')
    assert v4['gateway'] == '172.20.58.1'
    assert v4['interface'] == 'en0'
    assert v6 is None


# Generated at 2022-06-13 01:18:43.859722
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    aix = AIXNetworkCollector()
    assert aix.platform == 'AIX'

# Generated at 2022-06-13 01:18:45.262723
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    assert AIXNetworkCollector().platform == 'AIX'


# Generated at 2022-06-13 01:18:55.943220
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    from ansible.module_utils.facts.network.aix import AIXNetwork
    from ansible.module_utils.six import StringIO
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_bytes

    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True)


# Generated at 2022-06-13 01:19:01.582517
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():

    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True)

    aix_facts = AIXNetwork(module=module)
    interface = aix_facts.get_default_interfaces(route_path=None)
    assert interface == (None, None)



# Generated at 2022-06-13 01:19:06.142853
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    module = AnsibleModule(argument_spec={
        'route_path': {'required': True},
    })

    ansible_facts = {}
    ansible_facts['ansible_net_version'] = 2000000
    ansible_facts['ansible_net_hostname'] = 'testhost'
    ansible_facts['ansible_net_memtotal_mb'] = 1024

    AIXNetworkCollector(module=module).populate()

    route_path = module.params['route_path']
    default = AIXNetworkCollector(module=module).get_default_interfaces(route_path)
    assert default['v4']['gateway'] == '10.0.0.3'
    assert default['v4']['interface'] == 'en0'

# Generated at 2022-06-13 01:19:09.210133
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    """Test AIXNetworkCollector constructor"""
    network_collector = AIXNetworkCollector()
    assert network_collector._fact_class == AIXNetwork
    assert network_collector._platform == 'AIX'

# Generated at 2022-06-13 01:19:14.558889
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    """Unit test for constructor of class AIXNetworkCollector"""
    # Test initialisation of AIXNetworkCollector
    my_obj = AIXNetworkCollector()
    assert my_obj
    assert my_obj._platform == 'AIX'



# Generated at 2022-06-13 01:19:35.269629
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    net = AIXNetwork(dict(module=dict()))
    net.module.run_command = lambda x: (0, 'default  10.0.2.2        UG        0 0        en0\ndefault  2001:db8::1        UG        0 0        en1\n', '')

    v4, v6 = net.get_default_interfaces('/sbin/route')

    assert v4 == {'gateway': '10.0.2.2', 'interface': 'en0'}
    assert v6 == {'gateway': '2001:db8::1', 'interface': 'en1'}

# Generated at 2022-06-13 01:19:42.049289
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    class custom_module(object):
        def get_bin_path(self, name):
            return name

        def run_command(self, command):
            return (None, None, None)

    # test 1
    module = custom_module()
    ifconfig_path = '/usr/sbin/ifconfig'
    ifconfig_options = '-a'
    network = AIXNetwork()
    network.module = module
    interfaces, ips = network.get_interfaces_info(ifconfig_path, ifconfig_options)
    assert interfaces['en0']['device'] == 'en0'
    assert interfaces['en0']['type'] == 'ether'
    assert interfaces['en0']['flags'] == ['UP']
    assert interfaces['en0']['macaddress'] == 'unknown'

# Generated at 2022-06-13 01:19:51.558991
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    from ansible.module_utils.facts.network import AIXNetwork
    test_class = AIXNetwork()
    test_class.module = True
    test_class.run_command = True

# Generated at 2022-06-13 01:19:54.437787
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True,
    )

    net = AIXNetwork(module)
    net.get_default_interfaces('/usr/bin/netstat')


# Generated at 2022-06-13 01:20:01.060337
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    """
    Parse AIX ifconfig output, it is exported in ifconfig_out.txt
    """

# Generated at 2022-06-13 01:20:11.268041
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    aix_network = AIXNetwork()

    network_module_mock = Mock()
    network_module_mock.get_bin_path.return_value = '/usr/sbin'

    aix_network.module = network_module_mock

    command_out = '''
0.0.0.0          10.104.18.1      UG     0   0     0 en0
192.168.1.0      10.104.18.1      UG     0   0     0 en0
default          10.104.18.1      UG    50   0   110 en0
default          fe80::a00:27ff:fe95:b070   UG    50   0   110 en0
'''

# Generated at 2022-06-13 01:20:20.777715
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    import tempfile
    import os
    from ansible.module_utils.facts.network.aix import AIXNetwork, AIXNetworkCollector
    from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork

    temp_file = tempfile.NamedTemporaryFile(mode='rw', delete=False)

# Generated at 2022-06-13 01:20:31.945547
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    fake_module = FakeAnsibleModule()
    fake_module.run_command = lambda args, check_rc=False: (0, fake_netstat_output, None)
    network_collector = AIXNetworkCollector(fake_module)
    network_facts = network_collector.collect()
    assert network_facts['default_ipv4']['gateway'] == '172.16.204.254'
    assert network_facts['default_ipv4']['interface'] == 'en8'
    assert network_facts['default_ipv6']['gateway'] == 'fe80::300:4fff:fee8:d7b4'
    assert network_facts['default_ipv6']['interface'] == 'en8'


# Generated at 2022-06-13 01:20:42.322585
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():

    class Module:
        def __init__(self):
            self.params = {}

    class DummyModule:
        def __init__(self):
            self.params = {}

    module = Module()


# Generated at 2022-06-13 01:20:44.207415
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    assert AIXNetworkCollector.platform == 'AIX'
    assert AIXNetworkCollector._fact_class == AIXNetwork


# Generated at 2022-06-13 01:21:19.446863
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    import shutil
    import tempfile

    from ansible.module_utils.facts.network.aix import AIXNetwork

    m = AIXNetwork(dict(), dict())

    """Create temporary directory"""
    tmpdir = tempfile.mkdtemp()

    netstat_file = open(tmpdir + '/netstat', 'w')
    netstat_file.write('Routing tables\n')
    netstat_file.write('Destination        Gateway            Flags Refs     Use Interface\n')
    netstat_file.write('default            10.20.91.1        UG        3        0 en0\n')
    netstat_file.close()

    (v4, v6) = m.get_default_interfaces(tmpdir)
    assert v4['gateway'] == '10.20.91.1'
   

# Generated at 2022-06-13 01:21:27.707874
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    module = AnsibleModule(argument_spec={})
    f = AIXNetwork(module=module)

    route_path = '/usr/bin/netstat'
    output = '''
    Kernel Interface table
    Destination        Gateway            Flags   Refs     Use  If  Expire
    default            192.168.0.1        UG        0          0  en0
    default            fe80::%default%    UG        0          0    0
    127.0.0.1          127.0.0.1          UH        0          0  lo0
    192.168.0.0/24     link#3             UC        0          0  en0
    '''


# Generated at 2022-06-13 01:21:35.149223
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    # Test data
    lines = [['1', 'default', '172.16.23.2', 'UGS', '0', '0', 'en0'], ['2', '10.10.10.0/24', '10.10.10.1', 'U', '0', '0', 'en0']]
    expected_v4 = {'gateway': '172.16.23.2', 'interface': 'en0'}
    expected_v6 = {'gateway': '', 'interface': ''}

    # Test
    result_v4, result_v6 = AIXNetwork.get_default_interfaces(AIXNetwork(), lines)
    assert expected_v4 == result_v4
    assert expected_v6 == result_v6

# Generated at 2022-06-13 01:21:40.836844
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    module = AnsibleModule(argument_spec=dict())

    class AIXNetwork_get_interfaces_info_Mock():
        def __init__(self):
            self.rc = 0

# Generated at 2022-06-13 01:21:49.492877
# Unit test for method get_default_interfaces of class AIXNetwork

# Generated at 2022-06-13 01:21:56.455406
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    obj = AIXNetwork()
    obj.module.run_command = lambda x: (0, '', '')

    obj.module.get_bin_path = lambda x: False

    # test with short command output

# Generated at 2022-06-13 01:22:06.186348
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    """Test get_default_interfaces function of AIXNetwork class"""

    collector = AIXNetworkCollector()
    network = AIXNetwork(
        module=collector._module,
        command=collector._command,
        ifconfig=collector.get_bin_path('ifconfig'),
        netstat=collector.get_bin_path('netstat'),
    )

    route_path = collector.get_bin_path('netstat')

    assert network.get_default_interfaces(route_path) == ({'gateway': '10.0.2.2', 'interface': 'en0'}, {'gateway': 'fe80::5054:ff:fe6a:f1de', 'interface': 'en0'}), 'Wrong default interfaces'

# Generated at 2022-06-13 01:22:13.042633
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    class MockModule:

        def __init__(self, rc, out, err):
            self.rc = rc
            self.out = out
            self.err = err

        def get_bin_path(self, name, opts=None):
            return self.name

        def run_command(self, cmd, environ_update=None, check_rc=True, close_fds=True, executable=None, data=None):
            if cmd[0] == self.name:
                return self.rc, self.out, self.err
            else:
                return 0, '', ''
    ifconfig_path = 'ifconfig'
    # test_AIXNetwork_get_interfaces_info_000

# Generated at 2022-06-13 01:22:18.656353
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    module = MagicMock()
    module.run_command.return_value = 0, _OUT_NETSTAT, ''
    module.get_bin_path.return_value = '/usr/bin/netstat'
    net = AIXNetwork(module=module)
    expected = {
        'v4': {
            'gateway': '192.168.1.254',
            'interface': 'en1'
        },
        'v6': {
            'gateway': 'fec0::11',
            'interface': 'en1'
        }
    }
    result = net.get_default_interfaces('/etc/myroute')
    assert expected == result


# Generated at 2022-06-13 01:22:20.108597
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    assert AIXNetworkCollector._platform == 'AIX'


# Generated at 2022-06-13 01:23:18.214946
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    inet_with_bcast = 'ad0: flags=1004843<UP,BROADCAST,RUNNING,MULTICAST,DHCP,IPv4> mtu 1500 index 5 inet 157.50.20.2 netmask 0xffffff00 broadcast 157.50.20.255'
    inet_without_bcast = 'ad0: flags=1004843<UP,RUNNING,MULTICAST,DHCP,IPv4> mtu 1500 index 5 inet 157.50.20.2 netmask 0xffffff00'

# Generated at 2022-06-13 01:23:26.637228
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    from ansible.module_utils.facts.network.network import Interfaces
    from ansible.module_utils.facts.network.generic_bsd import GenericBsdNetwork

    def create_first_route_line(route_line_template, network, netmask='ffffff00', interface='eno1'):
        return route_line_template.format(network, netmask, network, netmask, interface)

    ifconfig_path = '/usr/bin/ifconfig'
    ifconfig_options = '-a'
    netstat_path = '/usr/bin/netstat'


# Generated at 2022-06-13 01:23:33.782755
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    from ansible.module_utils.facts.network.aix.aix import AIXNetwork
    from ansible.module_utils._text import to_bytes, to_text
    from ansible_collections.community.general.tests.unit.compat import unittest

    from ansible_collections.community.general.tests.unit.compat.mock import patch


# Generated at 2022-06-13 01:23:39.335888
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    module = Mock()
    aix_network = AIXNetwork(module)
    ips = dict(
        all_ipv4_addresses=[],
        all_ipv6_addresses=[],
    )


# Generated at 2022-06-13 01:23:47.540760
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    module = FakeAnsibleModule()
    module.run_command = fake_run_command

    fact_class = AIXNetwork(module)


# Generated at 2022-06-13 01:23:50.219688
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    collector = AIXNetworkCollector()
    assert collector.platform == 'AIX'
    assert isinstance(collector.facts, AIXNetwork)

# Generated at 2022-06-13 01:23:55.969812
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    module = AnsibleModule(argument_spec=dict(route_path=dict(required=True, type='str')))
    interface = AIXNetwork(module=module).get_default_interfaces(module.params['route_path'])
    assert len(interface) == 2
    assert 'gateway' and 'interface' in interface[0]
    assert 'gateway' and 'interface' in interface[1]
    assert '.' in interface[0]['gateway']
    assert '.' not in interface[1]['gateway']


# Generated at 2022-06-13 01:23:57.992746
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    """
    Unit test for constructor of class AIXNetworkCollector.
    :return: None
    """
    network_collector = AIXNetworkCollector()
    assert network_collector is not None

# Generated at 2022-06-13 01:24:01.376252
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    """ A trivial test to see if get_default_interfaces is recognized """
    aix_network = AIXNetwork()
    assert aix_network.get_default_interfaces('/etc/route') is not None, \
        "get_default_interfaces should return a value"

# Generated at 2022-06-13 01:24:06.088537
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    import json
    from ansible.module_utils.facts.network.aix import AIXNetwork

    test_device = AIXNetwork()

    json_file = open('/tmp/ansible_facts_network_aix.json')
    json_data = json.load(json_file)
    json_file.close()

    test_interface, test_ips = test_device.get_interfaces_info('/usr/bin/ifconfig', '-a')

    assert test_interface == json_data['interfaces']
    assert test_ips == json_data['default_ipv4']

# Generated at 2022-06-13 01:25:47.733508
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    aixnc = AIXNetworkCollector(dict(), False, '/bin/ifconfig', '/sbin/route')
    assert aixnc._network._platform == 'AIX'

# Generated at 2022-06-13 01:25:55.166556
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():

    class ModuleMock:

        def __init__(self, module_args):
            pass

        def run_command(self, command):
            out = AIX_IFCONFIG_OUTPUT
            return 0, out, None

        def get_bin_path(self, command):
            return True

    module_mock = ModuleMock({})
    net_cls = AIXNetwork(module_mock)
    net_cls.get_interfaces_info('ifconfig', ifconfig_options='-a')

# Generated at 2022-06-13 01:26:02.730914
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():

    class ModuleTest(object):
        """
        Mock class for AnsibleModule
        """
        def __init__(self, path):
            self.path = path
            self.exit_args = []
            self.exit_json = None
            self.fail_json = None

        def get_bin_path(self, cmd, opt_dirs=[]):
            return self.path

        def run_command(self, args, check_rc=True):
            return 0, 'default 172.16.13.1 UG 0 0 en7', ''

    module = ModuleTest('/usr/bin/netstat')
    aix_net = AIXNetwork(module)

# Generated at 2022-06-13 01:26:10.999221
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    im = dict()
    im['en0'] = dict(
        addresses=[]
    )
    im['en1'] = dict(
        addresses=[]
    )
    im['en2'] = dict(
        addresses=[]
    )
    im['en3'] = dict(
        addresses=[dict(
            address='9.3.19.229',
            netmask='255.255.255.192',
            broadcast='9.3.19.255'
        )]
    )
    im['en33'] = dict(
        addresses=[dict(
            address='9.3.19.230',
            netmask='255.255.255.192',
            broadcast='9.3.19.255'
        )]
    )
    im['en99'] = dict(
        addresses=[]
    )

# Generated at 2022-06-13 01:26:16.202107
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():

    class MockNetworkModule:
        def __init__(self):
            self.params = {'gather_subset': 'default', 'gather_network_resources': 'yes'}

        def get_bin_path(self, path):
            return 'netstat'


# Generated at 2022-06-13 01:26:21.037482
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    module = AnsibleModuleMock()
    module.get_bin_path.side_effect = lambda x: '/sbin/' + x

    facts = AIXNetwork(module)
    (ipv4, ipv6) = facts.get_default_interfaces('/sbin/route')

    assert ipv4['gateway'] == '192.168.1.1'
    assert ipv4['interface'] == 'en0'
    assert ipv6['gateway'] == 'fe80::64:ff:fe65:1e00%en0'
    assert ipv6['interface'] == 'en0'


# Generated at 2022-06-13 01:26:26.928537
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    """
    Test function get_interfaces_info of class
    AIXNetwork.
    :return:
    """

# Generated at 2022-06-13 01:26:32.467635
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    """
    Function tests method get_interfaces_info of AIXNetwork and
    compares the result to the expected result
    """
    # initialize
    module = AnsibleModule(argument_spec={})
    networking = AIXNetwork(module)

    # set the paths
    ifconfig_path = '/usr/bin/ifconfig'
    ifconfig_options = ''

    # expected result for 4 interfaces

# Generated at 2022-06-13 01:26:36.825275
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    from ansible.module_utils.facts.network.aix import AIXNetwork


# Generated at 2022-06-13 01:26:40.266831
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    module = Mock()
    module.run_command = Mock(return_value=(0, '', ''))
    network_ins = AIXNetwork(module)
    route_path = '/usr/bin/routel'
    expected_if = dict(v4='eth0', v6='eth0')
    assert expected_if == network_ins.get_default_interfaces(route_path)