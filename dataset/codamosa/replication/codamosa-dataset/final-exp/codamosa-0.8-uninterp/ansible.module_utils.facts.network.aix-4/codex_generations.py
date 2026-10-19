

# Generated at 2022-06-13 01:16:56.611382
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    # create empty object
    facts = AIXNetworkCollector()
    assert facts.platform == 'AIX'
    # pass fake module to object
    fake_module = type('', (), {})()
    fake_module.params = {}
    fake_module.run_command = type('', (), {})()
    fake_module.run_command.return_value = (0, '', '')
    facts = AIXNetworkCollector(module=fake_module)
    assert facts.module == fake_module
    assert facts.platform == 'AIX'

# Generated at 2022-06-13 01:17:00.072816
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    """Test constructor of AIXNetworkCollector uses AIXNetwork class."""
    network_collector = AIXNetworkCollector()
    assert network_collector.get_network_collector_platform() == 'AIX'
    assert network_collector.get_network_collector_class() is AIXNetwork

# Generated at 2022-06-13 01:17:09.943144
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    aix_network = AIXNetwork()


# Generated at 2022-06-13 01:17:23.236899
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    from ansible.module_utils.facts.collector.network.aix import AIXNetwork
    netw = AIXNetwork()
    netw.module.run_command = MagicMock()


# Generated at 2022-06-13 01:17:34.458096
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork
    from ansible.module_utils.facts.network.aix import AIXNetwork

    # initialize class for testing
    ansible_module = GenericBsdIfconfigNetwork.initialize_module()
    test_class = AIXNetwork(ansible_module)

    # Test AIX
    ifconfig_path = '/usr/sbin/ifconfig'
    ifconfig_options = '-a'


# Generated at 2022-06-13 01:17:35.345128
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    aix = AIXNetworkCollector()
    assert aix.get_facts() is not None

# Generated at 2022-06-13 01:17:42.861980
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    """
    This function is for unit tests for AIXNetwork.get_default_interfaces() method
    """
    # default netstat output

# Generated at 2022-06-13 01:17:54.821885
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    import os
    import json

    current_dir = os.path.dirname(os.path.realpath(__file__))
    data_filename = os.path.join(current_dir, 'output_netstat_-nr.txt')
    network = AIXNetwork()
    network.module = get_module_mock()
    with open(data_filename, 'r') as myfile:
        data = myfile.read().replace('\n', '')
    network.module.run_command.return_value = (0, data, None)

    interface = network.get_default_interfaces(None)
    expected = ({"gateway": "172.16.0.1", "interface": "en0"}, { "gateway": "fe80::1", "interface": "en1"})
    # AIX interface is a tuple

# Generated at 2022-06-13 01:17:56.560632
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    test_AIXNetwork = AIXNetwork()
    test_AIXNetwork.get_default_interfaces('netstat')


# Generated at 2022-06-13 01:18:02.714892
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    m = AIXNetworkCollector()
    # None is passed to m.get_default_interfaces because this method does not use the parameter
    m.get_default_interfaces(None)

    assert m.get_default_interfaces(None) == ({'gateway': '192.168.1.1', 'interface': 'bge1'}, {'gateway': 'fe80::21f:5bff:fe94:b0f1', 'interface': 'bge1'})


# Generated at 2022-06-13 01:18:15.853175
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    m = dict(params=dict(route_path='/usr/sbin/netstat'))
    aix = AIXNetwork(m)
    assert aix.get_default_interfaces('/usr/sbin/netstat') == ({}, {})

# Generated at 2022-06-13 01:18:22.039201
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )

    x = AIXNetworkCollector(module)

    assert x.platform == 'AIX'
    assert x.fact_class == AIXNetwork


# Generated at 2022-06-13 01:18:24.558718
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    """Test AIXNetworkCollector constructor"""
    facts = AIXNetworkCollector()
    assert facts.get_default_interfaces('/etc/crontab')

# Generated at 2022-06-13 01:18:29.337254
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    mc = AIXNetwork()
    assert mc.get_default_interfaces(route_path='netstat') == (
        {'gateway': '10.35.221.254', 'interface': 'en0'},
        {'gateway': '2001:db8:dead:beef::1', 'interface': 'en1'},
    )

# Generated at 2022-06-13 01:18:35.066108
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    module = AnsibleModule(argument_spec={})
    collector = AIXNetworkCollector(module=module)
    assert collector.__class__.__name__ == 'AIXNetworkCollector'
    assert collector.get_fact_class().__name__ == 'AIXNetwork'
    assert collector.get_fact_class().platform == 'AIX'
    assert collector.get_platform() == 'AIX'



# Generated at 2022-06-13 01:18:38.841345
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    """
    This test case tests the constructor of the class AIXNetworkCollector.
    """
    assert AIXNetworkCollector._fact_class == AIXNetwork
    assert AIXNetworkCollector._platform == 'AIX'


# Generated at 2022-06-13 01:18:40.086404
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    network_collector = AIXNetworkCollector()
    assert network_collector.__class__.__name__ == 'AIXNetworkCollector'


# Generated at 2022-06-13 01:18:51.405220
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    module = AnsibleModule(argument_spec={})
    ifconfig_path = module.get_bin_path('ifconfig')
    c = AIXNetwork(module)
    interfaces, ips = c.get_interfaces_info(ifconfig_path)

    cdict = {'device': 'lo0', 'ipv4': [], 'ipv6': [], 'type': 'unknown', 'flags': ['UP', 'LOOPBACK', 'RUNNING'],
             'macaddress': '00:00:00:00:00:00', 'mtu': '65536'}
    assert interfaces['lo0'] == cdict


# Generated at 2022-06-13 01:18:53.059092
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    """
    test_AIXNetworkCollector:
    """
    assert Callable(AIXNetworkCollector)

# Generated at 2022-06-13 01:18:54.288885
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    assert AIXNetworkCollector._platform == 'AIX'

# Generated at 2022-06-13 01:19:15.225830
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    module = AnsibleModule(argument_spec={'config': {'required': False}})
    network = AIXNetwork(module)

    class args:
        def __init__(self, config):
            self.config = config

    def run_command(self, args, check_rc=True):
        return (0,
                """default 172.16.101.1 UG en0
default 192.168.1.254 UG en1
default fe80::8ad3:3f98:32e3:f2d1%en0 UG en0
default :: UG en0
""",
                '')

    module.run_command = run_command
    network.module.run_command = run_command


# Generated at 2022-06-13 01:19:17.242377
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    aix = AIXNetworkCollector()
    assert aix._fact_class == AIXNetwork
    assert aix._platform == 'AIX'


# Generated at 2022-06-13 01:19:18.932247
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    '''
    Constructor of class AIXNetworkCollector can be instantiated without any
    error. '''
    network_collector = AIXNetworkCollector()
    assert network_collector

# Generated at 2022-06-13 01:19:24.937153
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    # aix_network.py uses ansible.module_utils.facts.network.generic_bsd.GenericBsdIfconfigNetwork for most of its work.
    # this exception may be changed in future
    test_module_utils_facts_network_generic_bsd = {
        'ifconfig_path': '/usr/sbin/ifconfig',
        'get_bin_path': lambda x: '/usr/sbin/'+x,
    }
    test_module_run_command = lambda args: ['', '', '']
    test_module = {
        'run_command': test_module_run_command,
        'get_bin_path': test_module_utils_facts_network_generic_bsd['get_bin_path'],
    }
    ifconfig_path = test_module_utils_facts_network_

# Generated at 2022-06-13 01:19:34.753751
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    from ansible_collections.ansible.community.plugins.module_utils.facts.network.aix import AIXNetwork
    import io
    import os
    import sys
    import pytest
    import subprocess
    import unittest.mock


# Generated at 2022-06-13 01:19:41.699510
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    module = NetworkCollector._create_module_mock()

    # create an instance of the class to test
    ifconfig_path = '/usr/bin/ifconfig'
    ifconfig_options = '-a'
    netstat_path = '/usr/bin/netstat'

    network_collector = AIXNetwork(module=module, ifconfig_path=ifconfig_path, ifconfig_options=ifconfig_options, netstat_path=netstat_path)
    assert network_collector is not None

    # netstat not found: empty dict
    module.get_bin_path.return_value = None

    ipv4_gateway, ipv6_gateway = network_collector.get_default_interfaces('useless_arg')

    assert isinstance(ipv4_gateway, dict)
    assert isinstance

# Generated at 2022-06-13 01:19:51.194071
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    import platform
    import json

    # Return example network interfaces info of aix machine

# Generated at 2022-06-13 01:19:57.818231
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    """
    This is a Unit-Test for AIXNetworkCollector.
    """
    # Print a message
    print("\nINFO: Starting Unit test for AIXNetworkCollector")

    # Print a message
    print("INFO: Unit test for AIXNetworkCollector: Creating a new AIXNetworkCollector")

    # Create a new AIXNetworkCollector
    my_obj = AIXNetworkCollector()

    # Print a message
    print("INFO: Unit test for AIXNetworkCollector: Created a new AIXNetworkCollector")

    # Print a message
    print("INFO: Unit test for AIXNetworkCollector: Completed")



# Generated at 2022-06-13 01:20:09.041795
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():

    from ansible_collections.misc.not_a_real_collection.plugins.module_utils.facts import Network
    from ansible.module_utils.common.collections import ImmutableDict

    # input for 'ifconfig -a'

# Generated at 2022-06-13 01:20:10.912991
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    """This function is used to test whether the constructor of AIXNetworkCollector is working properly.
    """
    AIXNetworkCollector()



# Generated at 2022-06-13 01:20:45.146936
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    import os
    import json
    import tempfile
    from ansible.module_utils.facts.network.aix import AIXNetwork
    import pytest
    testfile = tempfile.NamedTemporaryFile()
    testfile.write(open(os.path.join(os.path.dirname(__file__), 'AIXNetwork_ifconfig.txt'), 'rb').read())
    testfile.seek(0)
    test_interface = AIXNetwork()
    test_interface.module = type('obj', (object,), {})  # create a test object with the necessary module attributes

    interfaces, ips = test_interface.get_interfaces_info(testfile.name)

    output = {}

# Generated at 2022-06-13 01:20:47.331695
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    instance = AIXNetworkCollector()
    assert isinstance(instance, NetworkCollector)


# Generated at 2022-06-13 01:20:51.873953
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():

    collector = AIXNetworkCollector()

    # class attribute
    assert collector._fact_class == AIXNetwork  # pylint: disable=protected-access
    assert collector._platform == 'AIX'         # pylint: disable=protected-access


# Generated at 2022-06-13 01:21:01.820923
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():

    sample_output_route = 'netstat -nr'
    sample_output_uname = 'uname -W'
    sample_output_ifconfig = 'ifconfig -a'

    lines_route = sample_output_route.splitlines()
    ifs_route = dict(v4={}, v6={})

    for line in lines_route:
        words = line.split()
        if len(words) > 1 and words[0] == 'default':
            if '.' in words[1]:
                ifs_route['v4']['gateway'] = words[1]
                ifs_route['v4']['interface'] = words[5]
            elif ':' in words[1]:
                ifs_route['v6']['gateway'] = words[1]

# Generated at 2022-06-13 01:21:07.451273
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    module = NetworkCollector._create_module_mock()
    module.run_command = run_command_mock

    ifconfig_path = '/usr/bin/ifconfig'
    ifconfig_options = '-a'
    net = AIXNetwork(module)
    interfaces, ips = net.get_interfaces_info(ifconfig_path, ifconfig_options)
    assert len(interfaces) == 3
    assert len(ips['all_ipv4_addresses']) == 3
    assert len(ips['all_ipv6_addresses']) == 1



# Generated at 2022-06-13 01:21:09.719612
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    """
    Constructor of AIXNetworkCollector should return an object of AIXNetworkCollector
    """
    net_detect = AIXNetworkCollector(None, None)
    assert isinstance(net_detect, AIXNetworkCollector)

# Generated at 2022-06-13 01:21:19.348970
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():

    class ModuleStub:
        def get_bin_path(self, name):
            return '/bin/' + name

        def run_command(self, options):
            if options == ['/bin/lsattr', '-El', 'en0']:
                return (0, 'mtu 4k\nlarger_size yes', '')

# Generated at 2022-06-13 01:21:27.606283
# Unit test for method get_interfaces_info of class AIXNetwork

# Generated at 2022-06-13 01:21:31.730689
# Unit test for method get_interfaces_info of class AIXNetwork

# Generated at 2022-06-13 01:21:34.010353
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    assert AIXNetworkCollector.__doc__ is not None
    assert AIXNetworkCollector._platform is not None

# Generated at 2022-06-13 01:22:26.722500
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    module = None
    os = AIXNetwork(module)
    result = os.get_default_interfaces(None)
    assert result == (
        {'interface': 'en0', 'gateway': '10.1.1.1'},
        {'interface': 'en0', 'gateway': 'fe80::1%en0'})

# Generated at 2022-06-13 01:22:35.110147
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    test_mod = AnsibleModuleMock()
    test_class = AIXNetwork()

    ifconfig_path = test_class.module.get_bin_path('ifconfig')
    assert ifconfig_path, "ifconfig is not in $PATH"

    # mock 'ifconfig -a' output

# Generated at 2022-06-13 01:22:43.786953
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():

    from ansible.module_utils.facts.network.aix import AIXNetwork
    netstat_path = "/usr/bin/netstat"
    network = AIXNetwork(netstat_path)
    network.module = Mock()
    network.module.run_command.return_value = (0, "default            10.0.0.1          UG        0 0          en4\n"
                                                   "10.0.0.0/24        10.0.0.1          U         1 0          en4", "")

    ret = network.get_default_interfaces("")
    assert ret == ({'gateway': '10.0.0.1', 'interface': 'en4'}, {})

# Generated at 2022-06-13 01:22:51.447387
# Unit test for method get_interfaces_info of class AIXNetwork

# Generated at 2022-06-13 01:22:54.763020
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    """
    This test case is for checking the attributes of
    AIXNetworkCollector class.
    """
    assert hasattr(AIXNetworkCollector, '_fact_class')
    assert isinstance(AIXNetworkCollector._fact_class, AIXNetwork)
    assert hasattr(AIXNetworkCollector, '_platform')
    assert isinstance(AIXNetworkCollector._platform, str)

# Generated at 2022-06-13 01:23:00.059189
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    import os
    import sys
    import tempfile
    import pytest
    from ansible.module_utils.facts import collector

    # Set up the 'module' object required by the module
    test_dir = os.path.dirname(os.path.realpath(__file__))
    module = pytest.fixture(
        fixture=collector.get_module_mock(
            ansible_facts={},
            ansible_module=dict(
                config=dict(
                    config_file=os.path.join(test_dir, 'fixtures/ansible.cfg')
                )
            ),
        )
    )

    # Get a temp directory for 'ansible.cfg'
    tmp_dir = pytest.fixture(
        fixture=tempfile.TemporaryDirectory()
    )

    # Write a fake '

# Generated at 2022-06-13 01:23:08.159702
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():

    # create stubs
    module = AnsibleModule({})
    module.run_command = MagicMock(return_value=(0, '', ''))
    module.get_bin_path = MagicMock(return_value='/usr/bin')
    module.params = {'gather_subset': '!all'}
    module.is_executable = MagicMock(return_value=True)

    # /usr/bin/ifconfig -a

# Generated at 2022-06-13 01:23:14.088549
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    # create object instance
    obj = AIXNetwork(dict(module=dict(run_command=run_command)))
    assert obj

    # get_default_interfaces() should return a tuple of two dicts with keys gateway and interface
    default_v4, default_v6 = obj.get_default_interfaces('/tmp')
    assert set(default_v4.keys()) == {'gateway', 'interface'}
    assert set(default_v6.keys()) == {'gateway', 'interface'}


# Generated at 2022-06-13 01:23:15.917570
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    nc = AIXNetworkCollector()
    assert nc._fact_class.platform == 'AIX'
    assert nc._platform == 'AIX'


# Generated at 2022-06-13 01:23:22.145818
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    # make class instance
    aix_network = AIXNetwork()

    result = aix_network.get_interfaces_info('ifconfig')

    assert len(result) == 2
    assert type(result[0]) == dict
    assert type(result[1]) == dict
    assert isinstance(result[0]['lo0'], dict)
    assert 'inet' in result[0]['lo0']
    assert '127.0.0.1' in result[0]['lo0']['inet']
    assert 'inet' in result[1]['lo0']
    assert '::1' in result[1]['lo0']['inet']

# Generated at 2022-06-13 01:25:06.583784
# Unit test for method get_interfaces_info of class AIXNetwork

# Generated at 2022-06-13 01:25:15.136439
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    # Create an empty structure of AIXNetwork Class
    my_AIX_Net = AIXNetwork()

    # Set module and route_path to expected values
    my_AIX_Net.module = FakeModule()
    my_AIX_Net.route_path = '/usr/bin/netstat'

    # netstat command output
    netstat_out = '''
Destination     Gateway         Genmask         Iface
default         10.17.16.1      0.0.0.0         en0
10.17.16.0      *               255.255.254.0   en0
127.0.0.1       *               255.255.255.255 lo
'''

    # Define Fake 'run_command' function
    def fake_run(self, cmd):
        out = netstat_out
        err = ''


# Generated at 2022-06-13 01:25:21.406658
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    # Dummy class for testing
    class DummyNetwork:
        platform = 'AIX'

        def __init__(self):
            self.default_gateway_ipv4 = ''
            self.default_interface_ipv4 = ''
            self.default_gateway_ipv6 = ''
            self.default_interface_ipv6 = ''

    net = DummyNetwork()
    net_collector = AIXNetworkCollector()
    net_collector.get_default_interfaces(net, '/etc/myroute')
    assert net.default_gateway_ipv4 == ''
    assert net.default_interface_ipv4 == ''
    assert net.default_gateway_ipv6 == ''
    assert net.default_interface_ipv6 == ''

# Generated at 2022-06-13 01:25:30.797908
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():

    # mock module class
    class MockModule:

        # mock run_command to read a file
        def run_command(self, command, check_rc=True):
            lines = []

            if command[1] == '-a':
                with open('tests/unit/ansible_collections/ansible/netcommon/files/network/multi_interface_aix') as f:
                    lines = f.read().splitlines()

            return 0, '\n'.join(lines), ''

        # mock get_bin_path to return mocked file path
        def get_bin_path(self, binary):
            if binary == 'ifconfig':
                return 'tests/unit/ansible_collections/ansible/netcommon/files/network/multi_interface_aix'

# Generated at 2022-06-13 01:25:32.487235
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    m = AIXNetworkCollector(None, None)
    assert isinstance(m._fact_class, AIXNetwork)
    assert m._platform == 'AIX'

# Generated at 2022-06-13 01:25:40.470721
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    test_class = AIXNetwork()

    # testing get_default_interfaces with ifconfig output
    test_class.module.run_command = lambda args, check_rc=True: (0, '''default       172.31.4.254         UGS         en0
127           127.0.0.1  UGRS     lo0
default       fe80::1%lo0   UG         lo0
127           ::1                 UGRS     lo0
''', '')

    interfaces = test_class.get_default_interfaces(None)

    assert interfaces[0] == {'gateway': '172.31.4.254', 'interface': 'en0'}
    assert interfaces[1] == {'gateway': 'fe80::1%lo0', 'interface': 'lo0'}

    # testing get_default_

# Generated at 2022-06-13 01:25:47.405860
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    module = AnsibleModuleMock()
    net = AIXNetworkCollector(module=module, custom_conditions=None,
                              *[], **{})
    assert net.module == module
    assert net.platform == 'AIX'
    assert repr(net) == '<ansible.module_utils.facts.network.aix.AIXNetworkCollector (/run/ansible/facts.d, None, *(), **{})>'
    assert net.custom_conditions == None
    assert isinstance(net.fact_class, AIXNetwork) # this must be a class name



# Generated at 2022-06-13 01:25:53.762512
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    facts_dict = {}
    _module = None
    net = AIXNetwork(_module, facts_dict, {'config': '/etc/hostname.lo0', 'options': '-a', 'path': '/usr/sbin/ifconfig'})

    ifconfig_path = net.module.get_bin_path('ifconfig')

    if ifconfig_path:
        net.module.run_command = get_interfaces_info_test_run_command
        net.get_interfaces_info(ifconfig_path, '-a')
        assert facts_dict['interfaces'] == _interfaces_dict


# Generated at 2022-06-13 01:25:55.891141
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    assert isinstance(AIXNetworkCollector(), NetworkCollector)
    assert AIXNetworkCollector._platform == 'AIX'


# Generated at 2022-06-13 01:26:03.192283
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    module = AnsibleModule(argument_spec=dict())
    fake_path = dict(route="/usr/bin/route1")
    network = AIXNetwork(module, fake_path)

    # fake_out is the output of the command 'netstat -nr'
    fake_out = """
    Routing tables

    Internet:
    Destination Gateway Flags Ref Use Interface
    default  1.2.3.1    UG      1 94 eth0
    default  1::3      UG       1 34 eth1

    Internet6:
    Destination/Mask Gateway Flags Ref Use If
    default  1::3      UG       1 34 eth1
    """
    fake_in = list(fake_out.splitlines())
    fake_in = filter(None, fake_in)