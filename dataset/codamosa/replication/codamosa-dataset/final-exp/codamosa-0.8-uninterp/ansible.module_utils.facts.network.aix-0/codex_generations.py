

# Generated at 2022-06-13 01:16:57.927485
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    module = NetworkCollector()
    net = module.collect()['ansible_facts']['ansible_network_resources']
    if net['default_ipv4']:
        assert('interface' in net['default_ipv4'].keys())
        assert('gateway' in net['default_ipv4'].keys())


# Generated at 2022-06-13 01:17:03.069491
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    interfaces = AIXNetwork().get_interfaces_info()

    # Validate each interface has the required keys
    required_keys = ['active', 'device', 'ipv4', 'ipv6', 'macaddress', 'mtu',
                     'promisc', 'type']
    for interface in interfaces.itervalues():
        for key in required_keys:
            assert key in interface

# Generated at 2022-06-13 01:17:06.044513
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    iface = {
        'v4': {
            'gateway': '192.168.1.1',
            'interface': 'en1'
        },
        'v6': {
            'gateway': '::192.168.1.1',
            'interface': 'en1'
        }
    }
    aix = AIXNetwork()
    assert (iface == aix.get_default_interfaces(''))

# Generated at 2022-06-13 01:17:12.666101
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    # 'ifconfig -a' would return output like below
    netstat_output = """
        netstat: IPv4 addresses in output cannot be parsed by this parser
        netstat: IPv6 addresses in output cannot be parsed by this parser
        Routing Table: default
          Destination            Gateway           Flags   Refs     Interface
        -------------------- -------------------- ----- ------ -----------
          10.238.132.0          10.238.132.123          UG        0 hme0
          127.0.0.1             127.0.0.1               UH        8 lo0
        default                 10.238.132.123          UG        1 hme0
        """
    network = AIXNetwork()
    ipv4, ipv6 = network.get_default_interfaces(netstat_output)

# Generated at 2022-06-13 01:17:23.455986
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():

    class FakeModule(object):
        def __init__(self, return_value=None):
            self.params = {}
            self.exit_json = mock.Mock()
            self.fail_json = mock.Mock()
            self.run_command = mock.Mock(return_value=return_value)
            self.get_bin_path = mock.Mock(return_value='/sbin/route')

    class FakeCollector(object):
        def __init__(self, interfaces=None, default_interfaces=None):
            self.interfaces = interfaces
            self.default_interfaces = default_interfaces
            self.module = FakeModule()
            self.get_interfaces_info = mock.Mock(return_value=interfaces)


# Generated at 2022-06-13 01:17:34.497785
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    from ansible.module_utils.facts.network.interfaces.generic_bsd import GenericBsdIfconfigNetwork

    n = GenericBsdIfconfigNetwork()
    routes = [
        {
            'dst': 'default',
            'gw': '172.20.114.1',
            'proto': 'static,',
            'interface': 'en9',
            'src': '172.20.114.64',
            'flags': ['UG'],
            'dst_len': '0',
            'flags_ext': '0x0',
            'src_len': '0'
        }
    ]

    if_v4, if_v6 = n.get_default_interfaces(routes)
    assert if_v4['gateway'] == '172.20.114.1'
   

# Generated at 2022-06-13 01:17:37.530678
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    facts = AIXNetworkCollector(dict(), 'ansible_network_resources').collect()
    facts_dict = dict(ansible_network_resources=facts['ansible_network_resources'])
    assert 'ansible_default_ipv4' in facts_dict['ansible_network_resources']
    assert 'ansible_default_ipv6' in facts_dict['ansible_network_resources']

# Generated at 2022-06-13 01:17:48.246272
# Unit test for method get_interfaces_info of class AIXNetwork

# Generated at 2022-06-13 01:17:50.548757
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    collector = AIXNetworkCollector()
    assert collector.platform == 'AIX'
    assert collector.fact_class == AIXNetwork


# Generated at 2022-06-13 01:17:55.629612
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    module = AnsibleModule(argument_spec=dict())
    netinfo = AIXNetwork(module)
    (v4, v6) = netinfo.get_default_interfaces('/usr/sbin/route')
    assert('gateway' in v4)
    assert('interface' in v4)
    assert('link_layer_address' in v4)


# Generated at 2022-06-13 01:18:15.964602
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    module = AnsibleModule(argument_spec={
        'route_path': {'type': 'str', 'default': '/usr/sbin/route'},
    })
    network = AIXNetwork(module=module)
    assert network.get_default_interfaces(module.params['route_path']) == (
        {
            'gateway': '192.168.100.1',
            'interface': 'en0'
        },
        {
            'gateway': 'fe80::6c3:6aff:fe53:9eaa',
            'interface': 'en0'
        }
    )

# Unit tests for method get_interfaces_info of class AIXNetwork

# Generated at 2022-06-13 01:18:27.683527
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    """
    This method tests aix_network.get_interfaces_info()
    """
    import sys
    sys.path.append('/tmp/_ansible_test')

    from ansible.module_utils import basic
    if_mod = basic.AnsibleModule(argument_spec=dict())

    aix_network = AIXNetwork(if_mod)
    path = '/tmp/_ansible_test/aix_ifconfig'
    aix_interfaces, aix_ips = aix_network.get_interfaces_info(path)
    assert len(aix_interfaces) == 3
    assert len(aix_ips['all_ipv4_addresses']) == 2

    path = '/tmp/_ansible_test/aix_ifconfig_wpar'
    aix_interfaces, aix_

# Generated at 2022-06-13 01:18:30.846225
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    assert AIXNetworkCollector._platform == 'AIX'
    assert type(AIXNetworkCollector._fact_class) == type(AIXNetwork)


# Generated at 2022-06-13 01:18:40.021498
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    """
    Test method get_default_interfaces of class AIXNetwork
    """

    out = """
default        10.1.1.29        UG   3    0      en0
default        2001:41d0:a:1d1f:: UG   0    0      en0
"""

    ans = dict(
        gateway='10.1.1.29',
        interface='en0',
        ipv6=dict(
            gateway='2001:41d0:a:1d1f::',
            interface='en0',
        )
    )

    aix = AIXNetwork()
    assert ans == aix.get_default_interfaces(out)

# Generated at 2022-06-13 01:18:51.272060
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():

    from ansible.module_utils.facts.network.base import NetworkCollector

    class Module():

        def __init__(self):

            self.vars = dict()
            self.params = dict()

        def get_bin_path(self, name, opts=None, required=False):

            return name

        def run_command(self, args):

            rc = 0
            err = None

            if args[1] == '-nr':
                out = 'bad'


# Generated at 2022-06-13 01:18:53.672171
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    network_collector = AIXNetworkCollector()
    assert network_collector._platform == 'AIX'
    assert network_collector._fact_class == AIXNetwork



# Generated at 2022-06-13 01:19:01.466304
# Unit test for method get_interfaces_info of class AIXNetwork

# Generated at 2022-06-13 01:19:11.274265
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    # Helper: run_local_command, with side effect of modifying call_count and out_lines,
    # that can then be checked in the unit test
    class FakeModule:
        # pylint: disable=too-few-public-methods,no-self-use
        # Helper: run command
        def run_command(self, cmd, check_rc=True, close_fds=True, executable=None, data=None):
            call_count['run_command'] += 1

# Generated at 2022-06-13 01:19:15.526421
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    assert AIXNetworkCollector.platform == 'AIX'
    assert AIXNetworkCollector._platform == 'AIX'
    assert AIXNetworkCollector.fact_class.platform == 'AIX'
    assert AIXNetworkCollector._fact_class.platform == 'AIX'


# Generated at 2022-06-13 01:19:21.166921
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    with open('./test_data/AIX_netstat_nr.txt') as f:
        netstat_nr = f.read()

    test_mock = WindosNetwork()
    test_mock.module.run_command = lambda r: (0, netstat_nr, '')
    expected = {'v4': {'gateway': '172.16.1.1', 'interface': 'en1'}, 'v6': {'gateway': 'fe80::20c:29ff:fe0e:e221', 'interface': 'en1'}}

    output = test_mock.get_default_interfaces('')
    assert output == expected


# Generated at 2022-06-13 01:19:54.280125
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    module = AnsibleModule(argument_spec={})
    # create test data
    # data from AIX 7.1 TL04

# Generated at 2022-06-13 01:19:58.152888
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    module = AnsibleFakeModule()
    net = AIXNetwork(module)
    assert net.get_default_interfaces('/path/to/route') == ({'interface': 'en0', 'gateway': '192.0.2.5'}, {'interface': 'en1', 'gateway': '2001:db8:1::2'})



# Generated at 2022-06-13 01:20:05.601470
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    """
    This is a test function for the constructor of class AIXNetworkCollector.
    It shall return an object pointing to class AIXNetworkCollector.
    :return: An object pointing to class AIXNetworkCollector
    """
    network_collector_object = AIXNetworkCollector()
    assert isinstance(network_collector_object, AIXNetworkCollector)
    assert network_collector_object._fact_class is AIXNetwork
    assert network_collector_object._platform == 'AIX'

# Generated at 2022-06-13 01:20:13.648726
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():

    # Constructor of class AIXNetworkCollector must set _fact_class to
    # value of class AIXNetwork defined above.
    # To do this we use __dict__ which is a dictionary containing the
    # class's namespace.
    # See https://docs.python.org/3.5/tutorial/classes.html for details.
    assert AIXNetworkCollector.__dict__['_fact_class'] == AIXNetwork

    # Constructor of class AIXNetworkCollector must set _platform to
    # value of variable platform defined above.
    assert AIXNetworkCollector.__dict__['_platform'] == 'AIX'

# Generated at 2022-06-13 01:20:18.103199
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork
    network = AIXNetwork()
    info = network.get_interfaces_info('/usr/sbin/ifconfig', '')
    assert len(info[0]) > 0
test_AIXNetwork_get_interfaces_info.AIX_required = True

# Generated at 2022-06-13 01:20:28.093748
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():

    # test input data from AIX 6.1 TL8 SP3:
    aix_netstat_rc = 0

# Generated at 2022-06-13 01:20:33.497668
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    facts = AIXNetworkCollector(None, None).collect()
    interfaces = facts['interfaces']
    if 'lo0' in interfaces:
        assert interfaces['lo0']['type'] == 'loopback'
    if 'en0' in interfaces:
        assert interfaces['en0']['type'] == 'ether'
    if 'en1' in interfaces:
        assert interfaces['en1']['type'] == 'unknown'


# Generated at 2022-06-13 01:20:43.836588
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    def get_bin_path(name):
        return 'Unit test'

    class Mock_module(object):
        def __init__(self):
            self.params = {}
            self.path_implementation_map = {
                'command': 'generic',
                'shell': 'generic',
            }

        def get_bin_path(self, name, opt_dirs=None, required=False):
            """fake get_bin_path"""
            return get_bin_path(name)

        @staticmethod
        def run_command(commands, check_rc=True, close_fds=False, binary_data=False, encoding=None, errors=None,
                        expand_user_and_vars=False):
            """fake run_command"""
            return 0, AIX_ifconfig_a, ''


# Generated at 2022-06-13 01:20:54.891388
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    import tempfile
    fd, filename = tempfile.mkstemp()
    # the following lines will be written to file to simulate a route command

# Generated at 2022-06-13 01:21:03.717533
# Unit test for method get_default_interfaces of class AIXNetwork

# Generated at 2022-06-13 01:21:52.696999
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    assert AIXNetworkCollector._platform == 'AIX'
    assert AIXNetworkCollector._fact_class == AIXNetwork


# Generated at 2022-06-13 01:21:57.701626
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    ansible_module = AnsibleModule(argument_spec={'gather_subset': dict(type='list', default=['!all'])})
    gather_subset = ansible_module.params['gather_subset']
    fact_class = AIXNetwork(ansible_module)
    ansible_module.exit_json(ansible_facts=dict(ansible_net_gather_subset=gather_subset,
                                                ansible_net_gather_network_resources=fact_class.populate()))


# Generated at 2022-06-13 01:22:08.587147
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    from ansible_collections.notstdlib.moveitallout.tests.unit.compat import unittest
    from ansible_collections.notstdlib.moveitallout.tests.unit.compat.mock import patch, MagicMock
    from ansible_collections.notstdlib.moveitallout.plugins.modules import aix_network

    class AIXNetworkTestCase(unittest.TestCase):
        def setUp(self):
            self.AIXNetwork = AIXNetwork
            self.test_if = aix_network.AIXNetwork()


# Generated at 2022-06-13 01:22:16.275931
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    from ansible.module_utils.facts.network.aix import AIXNetwork

    module = type('module', (object,), dict(run_command=get_command_outputs_aix_ifconfig))
    module.exit_json = exit_json
    module.fail_json = exit_json
    module.get_bin_path = lambda _: '/usr/bin/'

    # Test with ifconfig output from AIX 6.1
    network = AIXNetwork(module)

    interfaces, ips = network.get_interfaces_info('/usr/bin/ifconfig', '-a')


# Generated at 2022-06-13 01:22:27.081422
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    # Test values
    ifconfig_path = '/usr/bin/ifconfig'
    ifconfig_options = '-a'

# Generated at 2022-06-13 01:22:35.444936
# Unit test for method get_default_interfaces of class AIXNetwork

# Generated at 2022-06-13 01:22:37.254850
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    m = AIXNetworkCollector()
    print(m.__dict__)


# Generated at 2022-06-13 01:22:40.661500
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    assert AIXNetworkCollector._platform == 'AIX'
    assert AIXNetworkCollector._fact_class == AIXNetwork
    x = AIXNetworkCollector()
    assert x.platform == 'AIX'

# Generated at 2022-06-13 01:22:48.865766
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():

    # Get the interfaces information from AIX
    aix_network = AIXNetwork()
    rc, out, err = aix_network.module.run_command("ifconfig -a")
    interfaces_info = aix_network.get_interfaces_info(aix_network.module.get_bin_path('ifconfig'), '-a')

    # Iterate over interface_info and create a dictionary of expected data
    expected_interfaces = {}
    for line in out.splitlines():
        if line:
            words = line.split()

            if re.match(r'^\w*\d*:', line):
                device = words[0][0:-1]

# Generated at 2022-06-13 01:22:50.539415
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    facts={}
    ansible_module = MockAnsibleModule(facts)
    AIXNetworkCollector(ansible_module, facts)


# Generated at 2022-06-13 01:24:32.766512
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    module = AnsibleModule(argument_spec={})

    # values of file netstat -nr

# Generated at 2022-06-13 01:24:41.966572
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    module = AnsibleModule(argument_spec=dict())
    test_obj = AIXNetwork(module)

    ifconfig_path = module.get_bin_path('ifconfig')
    ifconfig_options = '-a'

    interfaces, ips = test_obj.get_interfaces_info(ifconfig_path, ifconfig_options)

    assert 'lo0' in interfaces
    assert interfaces['lo0']['flags'] == ['UP', 'LOOPBACK', 'RUNNING']
    assert interfaces['lo0']['macaddress'] == 'unknown'

    assert 'en0' in interfaces
    assert interfaces['en0']['flags'] == ['UP', 'BROADCAST', 'RUNNING', 'SIMPLEX', 'MULTICAST']
    assert interfaces['en0']['macaddress'] == 'unknown'
   

# Generated at 2022-06-13 01:24:43.631482
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    aix = AIXNetwork()
    aix.get_default_interfaces()


# Generated at 2022-06-13 01:24:49.968829
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    module = NetworkCollector.get_module_mock()
    facts = AIXNetwork(module=module)

    # test with invalid netstat path
    module.get_bin_path.return_value = None
    assert facts.get_default_interfaces('') == (None, None)

    # test with bad output from netstat
    module.get_bin_path.return_value = '/usr/bin/netstat'
    module.run_command.return_value = (0, 'bad response', '')
    assert facts.get_default_interfaces('') == (None, None)

    # test with good output from netstat

# Generated at 2022-06-13 01:24:51.480276
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    assert AIXNetworkCollector._platform == 'AIX'
    assert AIXNetworkCollector._fact_class == AIXNetwork


# Generated at 2022-06-13 01:24:56.867552
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    from ansible.module_utils.facts.network.aix import AIXNetwork
    from ansible.module_utils.facts.network.aix import AIXNetworkCollector
    from ansible.module_utils.facts.network.ifconfig import IfconfigNetwork
    from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork
    from ansible.module_utils.facts.network.generic_bsd import IfconfigNetworkCollector
    from ansible.module_utils.facts.network.base import NetworkCollector
    import ansible.module_utils.facts.network.aix as test_aix
    import ansible.module_utils.facts.network.base as test_base
    import ansible.module_utils.facts.network.generic_bsd as test_generic_bsd

    test_base

# Generated at 2022-06-13 01:24:59.826031
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    _fact_class = AIXNetwork
    _platform = 'AIX'
    assert AIXNetworkCollector._fact_class is _fact_class
    assert AIXNetworkCollector._platform is _platform

# Generated at 2022-06-13 01:25:07.279931
# Unit test for method get_default_interfaces of class AIXNetwork

# Generated at 2022-06-13 01:25:09.786063
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    """
    Constructor of class AIXNetworkCollector can be created without any error.
    """
    AIXNetworkCollector()



# Generated at 2022-06-13 01:25:17.636947
# Unit test for method get_interfaces_info of class AIXNetwork