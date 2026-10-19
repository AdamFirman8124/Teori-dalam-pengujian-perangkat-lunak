

# Generated at 2022-06-13 01:48:23.889527
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    s = SunOSNetworkCollector()
    assert s.facts is None
    assert s._cache is None
    assert s._platform == 'SunOS'
    assert SunOSNetworkCollector._platform == 'SunOS'

# Generated at 2022-06-13 01:48:26.507248
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    assert 'SunOSNetworkCollector' in globals()
    c = SunOSNetworkCollector()
    assert isinstance(c, SunOSNetworkCollector)
    assert isinstance(c, NetworkCollector)
    assert c.platform == 'SunOS'
    assert c.fact_class == SunOSNetwork


# Generated at 2022-06-13 01:48:36.437702
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    fake_module = FakeModule({'ansible_facts': {}})
    fake_module.params = {'gather_network_resources': 'yes'}
    fake_module.run_command = run_command
    fake_module.run_command.mock = mock_run_command
    SunOSNetwork.get_interfaces_info = get_interfaces_info
    result = SunOSNetwork(fake_module).populate()
    assert result['ansible_all_ipv4_addresses'] == ['1.1.1.1', '3.3.3.3', '192.168.0.3', '192.168.0.27']

# Generated at 2022-06-13 01:48:40.842320
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    network_collector = SunOSNetworkCollector()
    assert network_collector is not None
    assert network_collector.platform == 'SunOS'
    assert network_collector.fact_class == SunOSNetwork
    assert network_collector.fact_subsets == {}

# Generated at 2022-06-13 01:48:44.334623
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    obj = SunOSNetworkCollector()
    assert obj._fact_class == SunOSNetwork
    assert obj._platform == 'SunOS'

# Generated at 2022-06-13 01:48:49.785445
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    module_name = 'ansible.module_utils.facts.network.sunos'
    module = __import__(module_name, fromlist=[module_name.split('.')[0]])
    network_collector = module.SunOSNetworkCollector()
    assert network_collector
    assert network_collector._fact_class.platform == 'SunOS'


# Generated at 2022-06-13 01:48:51.464499
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    collector = SunOSNetworkCollector()
    assert isinstance(collector, SunOSNetworkCollector)

# Generated at 2022-06-13 01:49:00.107502
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    from ansible.module_utils.facts.network.sunos import SunOSNetwork
    from collections import namedtuple
    FakeModule = namedtuple('FakeModule', ['run_command'])

# Generated at 2022-06-13 01:49:07.096182
# Unit test for method parse_interface_line of class SunOSNetwork
def test_SunOSNetwork_parse_interface_line():
    sn = SunOSNetwork()
    words = ["ce0:", "flags=1004843", "mtu=1500"]
    iface = {'device': 'ce0', 'ipv4': [], 'ipv6': [], 'type': 'unknown'}
    iface = sn.parse_interface_line(words, iface, {})
    assert iface['ipv4'][0] == {'flags': '1004843', 'mtu': '1500'}

# Generated at 2022-06-13 01:49:17.422219
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    module = AnsibleModuleMock()
    ifconfig_path = 'some_path'

# Generated at 2022-06-13 01:49:32.918464
# Unit test for method parse_interface_line of class SunOSNetwork
def test_SunOSNetwork_parse_interface_line():
    class mock_module:
        def __init__(self):
            self.run_command_count = 0

        def run_command(self, args):
            self.run_command_count += 1
            return 0, '', ''

    class mock_SunOSNetwork:
        def __init__(self):
            self.module = mock_module()
            self.interfaces = {}
            self.ips = dict(
                all_ipv4_addresses=[],
                all_ipv6_addresses=[],
            )

    class mock_words:
        def __init__(self):
            self.device = 'net0'
            self.index = 0

    module = mock_module()
    current_if = {}
    interface = mock_SunOSNetwork()
    words = mock_words()
    assert interface.parse

# Generated at 2022-06-13 01:49:36.163579
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    """Unit test for constructor of class SunOSNetworkCollector."""
    test_obj = SunOSNetworkCollector()
    assert test_obj
    assert test_obj.platform == 'SunOS'
    assert test_obj.fact_class == SunOSNetwork


# Generated at 2022-06-13 01:49:39.678924
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    network_collector = SunOSNetworkCollector()
    assert network_collector._fact_class is SunOSNetwork
    assert network_collector._platform is 'SunOS'



# Generated at 2022-06-13 01:49:41.636527
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    obj = SunOSNetworkCollector(None, None, None)
    assert isinstance(obj, SunOSNetworkCollector)

# Generated at 2022-06-13 01:49:47.567375
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    data = """lo0: flags=1000849<UP,LOOPBACK,RUNNING,MULTICAST,IPv4> mtu 8232 index 1
        inet 127.0.0.1 netmask ff000000
        ip6 ::1/128
        ip6 fe80::1/10
dnet0: flags=1100843<UP,BROADCAST,RUNNING,MULTICAST,ROUTER,IPv4> mtu 1500 index 2
        inet 192.0.2.1 netmask ffffff00 broadcast 192.0.2.255
        ether 8:0:20:ff:a8:9a
        ip6 fe80::a00:20ff:feff:a89a/10
"""

    sunos_obj = SunOSNetwork()
    interfaces, ips = sunos_obj.get_

# Generated at 2022-06-13 01:49:50.674946
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    # pylint: disable=protected-access
    assert SunOSNetworkCollector._platform == 'SunOS'
    assert SunOSNetworkCollector._fact_class == SunOSNetwork

# Generated at 2022-06-13 01:49:59.848324
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    my_obj = SunOSNetwork(dict(module=None))

    my_result = my_obj.get_interfaces_info('')

    # If a parameter is not passed to the method, it should return a tuple
    # with an empty dictionary as the first element and a dictionary of lists as
    # the second element.
    assert my_result == ({}, dict(all_ipv4_addresses=[], all_ipv6_addresses=[])), \
        "get_interfaces_info() did not return ({}, {'all_ipv4_addresses': [], 'all_ipv6_addresses': []})"



# Generated at 2022-06-13 01:50:10.109434
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    testobj = SunOSNetwork()

# Generated at 2022-06-13 01:50:16.869969
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    class TestModule(object):
        def __init__(self, params, args=None):
            self.params = params

        def run_command(self, cmd):
            return 0, "", ""

    params = {'gather_subset': '!all'}
    test_obj = SunOSNetwork(TestModule(params))
    test_obj.get_interfaces_info(ifconfig_path='/usr/sbin/ifconfig')

# Generated at 2022-06-13 01:50:19.407229
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    module_mock = {}
    collector = SunOSNetworkCollector(module_mock)
    assert collector.__class__.__name__ == 'SunOSNetworkCollector'

# Generated at 2022-06-13 01:50:35.372258
# Unit test for method parse_interface_line of class SunOSNetwork
def test_SunOSNetwork_parse_interface_line():
    """
    # On Solaris 'ifconfig -a' will display interfaces twice once for IPv4 and
    # again for IPv6. This test verifies that parse_interface_line accumulates
    # facts for each IP version on the interface into their ipv4 or ipv6 list.
    """
    # Object of class SunOSNetwork
    sunos_network = SunOSNetwork()


# Generated at 2022-06-13 01:50:46.359951
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    from ansible_collections.notmintest.not_a_real_collection.tests.unit.compat.mock import patch
    from ansible_collections.notmintest.not_a_real_collection.tests.unit.modules.utils import set_module_args
    from ..test_generic_bsd import TestGenericBsdIfconfigNetwork


# Generated at 2022-06-13 01:50:57.750512
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    import os
    import json

    test_dir = os.path.dirname(os.path.realpath(__file__))
    test_output_dir = os.path.join(test_dir, '../output')
    test_output_file = os.path.join(test_output_dir, 'SunOS_ifconfig.txt')

    with open(test_output_file, 'r') as f:
        ifconfig_output = f.read()

    module = type('Module', (object,), {})
    module.run_command = lambda args: (0, ifconfig_output, '')

    sunos_network = SunOSNetwork({'module': module})
    facts, additional_facts = sunos_network.get_interfaces_info('/usr/sbin/ifconfig')


# Generated at 2022-06-13 01:51:04.541162
# Unit test for method parse_interface_line of class SunOSNetwork

# Generated at 2022-06-13 01:51:07.459318
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    collector = SunOSNetworkCollector()
    assert collector._platform == 'SunOS'
    assert collector._fact_class == SunOSNetwork


# Generated at 2022-06-13 01:51:09.889241
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    myobj = SunOSNetworkCollector()
    assert myobj._fact_class == SunOSNetwork
    assert myobj._platform == 'SunOS'

# Generated at 2022-06-13 01:51:12.657008
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    c = SunOSNetworkCollector()
    assert c._fact_class == SunOSNetwork
    assert c._platform == 'SunOS'

# Generated at 2022-06-13 01:51:24.414942
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    my_SunOSNetwork = SunOSNetwork()
    my_SunOSNetwork.module = AnsibleModule(argument_spec={})
    my_SunOSNetwork.module.run_command = run_command
    data = my_SunOSNetwork.get_interfaces_info()
    assert 'lo0' in data['interfaces']
    assert 'e1000g0' in data['interfaces']
    assert 'e1000g1' in data['interfaces']
    assert 'bge0' in data['interfaces']
    assert 'bge1' in data['interfaces']
    assert len(data['interfaces']['lo0']['ipv4']) == 1
    assert len(data['interfaces']['lo0']['ipv6']) == 1

# Generated at 2022-06-13 01:51:28.565361
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    """
    Unit test the get_interfaces_info method of class SunOSNetwork
    """
    obj = SunOSNetwork()
    obj.module = MockModule()
    interfaces, ips = obj.get_interfaces_info(obj.module.get_bin_path("ifconfig"))
    assert "lo0" in interfaces
    assert "igb0" in interfaces
    assert "igb1" in interfaces



# Generated at 2022-06-13 01:51:37.623516
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    from ansible.module_utils.facts.network.sunos import SunOSNetworkCollector
    from ansible.module_utils.facts.network.generic_bsd import GenericBsdNetwork
    from ansible.module_utils.facts.collector import BaseFactCollector

    obj = SunOSNetworkCollector(None, None, None, None)

    assert isinstance(obj, SunOSNetworkCollector) and isinstance(obj, BaseFactCollector)
    assert obj._fact_class is SunOSNetwork
    assert obj._platform == 'SunOS'


# Generated at 2022-06-13 01:51:49.033702
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    obj = SunOSNetworkCollector()
    assert isinstance(obj, NetworkCollector)
    assert isinstance(obj._fact_class, SunOSNetwork)
    assert obj._platform == 'SunOS'

# Generated at 2022-06-13 01:51:59.064980
# Unit test for method get_interfaces_info of class SunOSNetwork

# Generated at 2022-06-13 01:52:01.024546
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    nc = SunOSNetworkCollector()
    assert nc.fact_class == SunOSNetwork
    assert nc.platform == 'SunOS'

# Generated at 2022-06-13 01:52:10.355796
# Unit test for method parse_interface_line of class SunOSNetwork
def test_SunOSNetwork_parse_interface_line():
    mod = AnsibleModule(argument_spec={})
    interfaces = {}
    current_if = {}
    # test IPv4
    words = ['lo0:', 'flags=1000849', 'mtu', '8232']
    current_if = SunOSNetwork.parse_interface_line(mod, words, current_if, interfaces)
    assert current_if['device'] == 'lo0'
    assert current_if['ipv4'][0]['flags'] == 'LOOPBACK,RUNNING,MULTICAST,IPv4'
    assert current_if['type'] == 'loopback'
    # test IPv6
    words = ['lo0:', 'flags=1000841', 'mtu', '8232']

# Generated at 2022-06-13 01:52:11.805253
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    assert SunOSNetworkCollector.__bases__ == (NetworkCollector,)

# Generated at 2022-06-13 01:52:20.949759
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    '''
    This function is used to test the method get_interfaces_info of class SunOSNetwork.
    '''
    SunOSNetwork_test = SunOSNetwork()

    # the return value of run_command('ifconfig -a') is mocked to a test file
    SunOSNetwork_test.module.run_command = lambda args: (0, open('ifconfig_a.sample.txt', 'r').read(), None)

    interfaces, ips = SunOSNetwork_test.get_interfaces_info('ifconfig')

    assert len(interfaces) == 2
    assert len(interfaces['lo0']) == 6
    assert len(interfaces['lo0']['ipv4']) == 1
    assert len(interfaces['lo0']['ipv6']) == 1

# Generated at 2022-06-13 01:52:26.877534
# Unit test for method parse_interface_line of class SunOSNetwork
def test_SunOSNetwork_parse_interface_line():
    game = SunOSNetwork()
    game.module = dict()
    game.module['run_commands'] = dict()
    game.module['run_commands']['shell'] = dict()
    words = ['vnet0:', 'flags=20100843<UP,BROADCAST,RUNNING,SIMPLEX,MULTICAST,GROUPRT,64BIT>', 'mtu=']

    interfaces = dict()
    current_if = dict()
    current_if = game.parse_interface_line(words, current_if, interfaces)

# Generated at 2022-06-13 01:52:37.228098
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    """
    Test get_interfaces_info with FreeBSD ifconfig output
    """
    with open('tests/unit/facts/network/generic_bsd/test_SunOS_ifconfig_-a_output.txt', 'r') as f:
        test_data = f.read()

    # create the class object
    SunOSNetwork = SunOSNetwork()

    # run the test
    interfaces = {}
    ips = dict(
        all_ipv4_addresses=[],
        all_ipv6_addresses=[],
    )
    for line in test_data.splitlines():
        if line:
            words = line.split()

            if re.match(r'^\S', line) and len(words) > 2:
                current_if = SunOSNetwork.parse_interface_line(words, {}, interfaces)

# Generated at 2022-06-13 01:52:39.812069
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    obj = SunOSNetworkCollector()
    assert obj._fact_class == SunOSNetwork
    assert obj._platform == 'SunOS'

# Generated at 2022-06-13 01:52:49.770956
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    iface_with_mac_loopback = {
        'device': 'lo0',
        'ipv4': [
            {'flags': ['UP', 'LOOPBACK', 'RUNNING'], 'mtu': '8232'},
            {'flags': ['UP', 'LOOPBACK', 'RUNNING'], 'mtu': '8232'}
        ],
        'ipv6': [],
        'macaddress': '0:1:2:d:e:f',
        'type': 'loopback'
    }

# Generated at 2022-06-13 01:53:11.248055
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    from ansible.module_utils.facts.network.sunos import SunOSNetworkCollector
    assert SunOSNetworkCollector._platform == 'SunOS'

# Generated at 2022-06-13 01:53:18.362042
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    """
    This is the list of dictionaries returned by SunOSNetwork.get_interfaces_info()
    when the example output of 'ifconfig -a' is used.

    It is a unit test to verify that the method SunOSNetwork.get_interfaces_info()
    correctly parses the output of the 'ifconfig -a' command and returns
    a list of dictionaries.

    The test data was copied from the example output of 'ifconfig -a' on
    Solaris 11.3 and checked against the facts returned by the method.
    """

# Generated at 2022-06-13 01:53:19.561434
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    sunos = SunOSNetworkCollector()
    assert sunos._platform == 'SunOS'

# Generated at 2022-06-13 01:53:31.081668
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    # Create a dummy AnsibleModule object
    module = AnsibleModule(argument_spec={})
    module.run_command = MagicMock(return_value=(0, '', ''))
    module.warn = MagicMock()
    module.fail_json = MagicMock()

# Generated at 2022-06-13 01:53:32.860350
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    assert SunOSNetworkCollector.collect()


# Generated at 2022-06-13 01:53:34.526689
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    s = SunOSNetworkCollector()
    assert s.get_facts() is not None

# Generated at 2022-06-13 01:53:37.190360
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    net_collector = SunOSNetworkCollector(None, SunOSNetwork())
    assert net_collector._fact_class is SunOSNetwork


# Generated at 2022-06-13 01:53:40.045345
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    collector = SunOSNetworkCollector()
    assert collector._fact_class == SunOSNetwork
    assert collector._platform == 'SunOS'

# Generated at 2022-06-13 01:53:49.851956
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    module = FakeModule()
    ifconfig_path = '/bin/ifconfig'
    fact_class = SunOSNetwork(module=module, ifconfig_path=ifconfig_path)
    facts = {'default_ipv4': {}, 'interfaces': {}, 'all_ipv6_addresses': [], 'all_ipv4_addresses': []}

# Generated at 2022-06-13 01:53:51.964528
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    """
    Check if SunOSNetworkCollector class can be instantiated.
    """
    assert SunOSNetworkCollector(None) is not None


# Generated at 2022-06-13 01:54:49.741311
# Unit test for method parse_interface_line of class SunOSNetwork
def test_SunOSNetwork_parse_interface_line():
    # Create a dictionary with testing attributes
    test_iface = {
        'device': '',
        'ipv4': [],
        'ipv6': [],
        'type': 'unknown',
        'macaddress': 'unknown',
    }

    # Create a SunOSNetwork object
    iface = SunOSNetwork()

    # Test parse_interface_line() method with IPv4 interface
    words = ['lo0:', 'flags=2001000849<UP,LOOPBACK,RUNNING,MULTICAST,IPv4,VIRTUAL>', 'mtu', '8232']
    iface.parse_interface_line(words, test_iface)
    assert test_iface['device'] == 'lo0'
    assert len(test_iface['ipv4']) == 1
    assert test_if

# Generated at 2022-06-13 01:54:50.753923
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
  SunOSNetworkCollector()

# Generated at 2022-06-13 01:54:52.380919
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    assert isinstance(SunOSNetworkCollector(), NetworkCollector)

# Generated at 2022-06-13 01:54:56.826887
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    from ansible.module_utils.facts.network.sunos import SunOSNetwork

    fake_module = lambda: None
    fake_module.run_command = lambda cmd: (0, '', '')

    net = SunOSNetwork(fake_module)

    ifconfig_path = '/sbin/ifconfig'

# Generated at 2022-06-13 01:55:03.511484
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    # Create an instance of class SunOSNetwork
    sunos_network = SunOSNetwork()
    # Get the 'ifconfig -a' output
    ifconfig_path = sunos_network.module.get_bin_path('ifconfig', True)
    rc, out, err = sunos_network.module.run_command([ifconfig_path, '-a'])
    # Call the get_interfaces_info method of that instance
    sunos_network.get_interfaces_info(ifconfig_path)

# Generated at 2022-06-13 01:55:09.118653
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    """Test that the constructor of the class SunOSNetworkCollector works."""
    # Unsupported/unknown platform
    network_collector = SunOSNetworkCollector()
    assert network_collector.platform == 'SunOS'
    assert network_collector.fact_class.platform == 'SunOS'
    # Supported platform
    network_collector = SunOSNetworkCollector('SunOS')
    assert network_collector.platform == 'SunOS'
    assert network_collector.fact_class.platform == 'SunOS'

# Generated at 2022-06-13 01:55:19.918072
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    """Unit test of method get_interfaces_info in SunOSNetwork class
    """
    #  input data

# Generated at 2022-06-13 01:55:22.405416
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    assert issubclass(SunOSNetworkCollector, NetworkCollector)


# Generated at 2022-06-13 01:55:29.095700
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    testobject = SunOSNetwork()
    # I would like to use the "assertIs(a,b)" method, but it has been added in Python 3.1
    # and I have to test this on a Solaris 10 machine which uses Python 2.6.2
    assert testobject.get_interfaces_info('/sbin/ifconfig') == ({},
                                                                {'all_ipv4_addresses': [],
                                                                 'all_ipv6_addresses': []})


# Generated at 2022-06-13 01:55:36.073911
# Unit test for method get_interfaces_info of class SunOSNetwork

# Generated at 2022-06-13 01:56:58.897812
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    """
    This function unit tests the constructor of the class SunOSNetworkCollector
    """
    # Execute constructor of SunOSNetworkCollector() and verify object
    sunos_net = SunOSNetworkCollector()
    assert isinstance(sunos_net, NetworkCollector), "The constructor is broken"
    # Verify platform attribute
    assert sunos_net._platform == 'SunOS', "The SunOSNetworkCollector()._platform has the wrong value"
    # Verify fact_class attribute
    assert sunos_net._fact_class is SunOSNetwork, "The SunOSNetworkCollector()._fact_class has the wrong value"



# Generated at 2022-06-13 01:57:02.130500
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    instance = SunOSNetworkCollector()
    assert instance.platform == 'SunOS'
    assert isinstance(instance.facts, SunOSNetwork)
    assert instance.facts._platform == 'SunOS'


# Generated at 2022-06-13 01:57:09.696740
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    '''
    This unit test is for method get_interfaces_info of class SunOSNetwork.
    '''
    module = Mock(RunCommand=Mock(return_value=(0, open(
        'test/unit/ansible_collections/ansible/netcommon/plugins/test_data/test_SunOSNetwork_get_interfaces_info.txt',
        'r').read(), '')))
    ifconfig_path = '/usr/sbin/ifconfig'
    obj_SunOSNetwork = SunOSNetwork(module, ifconfig_path)
    interfaces, ips = obj_SunOSNetwork.get_interfaces_info(ifconfig_path)

# Generated at 2022-06-13 01:57:17.276491
# Unit test for method get_interfaces_info of class SunOSNetwork

# Generated at 2022-06-13 01:57:22.527596
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    """ Unit test for method get_interfaces_info of class SunOSNetwork """
    from ansible.module_utils.facts.network.network_sunos import SunOSNetwork
    import json

    args_dict = dict(
        ansible_command_linux_interfaces="/sbin/ifconfig -a",
    )
    module = FakeModule(params=args_dict)
    sunosnetwork = SunOSNetwork(module=module)
    assert sunosnetwork.get_interfaces_info is not None
    out_dict = sunosnetwork.get_interfaces_info(ifconfig_path = "/sbin/ifconfig")
    assert out_dict is not None
    assert "interfaces" in out_dict.keys()
    assert "ips" in out_dict.keys()

# Generated at 2022-06-13 01:57:29.354403
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    from ansible.module_utils.facts.network.sunos import SunOSNetwork
    module = AnsibleModuleMock()
    net = SunOSNetwork()
    net.module = module
    net.get_interfaces_info('/sbin/ifconfig')
    assert module.run_command.call_count == 1
    assert module.run_command.call_args[0] == (['/sbin/ifconfig', '-a'], )
    assert module.run_command.call_args[1] == {'encoding': None, 'errors': 'surrogate_then_replace', 'warn': False}

# Unit test class AnsibleModuleMock

# Generated at 2022-06-13 01:57:30.356904
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    obj = SunOSNetworkCollector()
    assert obj._fact_class is SunOSNetwork
    assert obj._platform is 'SunOS'

# Generated at 2022-06-13 01:57:34.410087
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    module = AnsibleModule()
    # ifconfig_path is set to /bin/true as it is not needed for the test.
    sunos_network = SunOSNetwork(module, ifconfig_path='/bin/true')

# Generated at 2022-06-13 01:57:36.350620
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    network = SunOSNetworkCollector()

    assert network._fact_class.platform == 'SunOS'

# Generated at 2022-06-13 01:57:46.466621
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    test_data_path = os.path.join(os.path.dirname(__file__), os.path.pardir, 'unit', 'data')
    platform_path = os.path.join(test_data_path, 'SunOS_ifconfig_a.txt')
    platform_path_empty = os.path.join(test_data_path, 'empty')
    module = FakeModule()
    inst = SunOSNetwork(module)
    # Test with no data
    interfaces, ips = inst.get_interfaces_info(platform_path_empty)
    assert interfaces == {}
    assert ips['all_ipv4_addresses'] == []
    assert ips['all_ipv6_addresses'] == []
    # Test with the real data