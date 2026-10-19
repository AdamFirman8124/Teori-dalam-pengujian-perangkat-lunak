

# Generated at 2022-06-13 01:48:24.340469
# Unit test for method get_interfaces_info of class SunOSNetwork

# Generated at 2022-06-13 01:48:25.133762
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
	assert(SunOSNetworkCollector().platform == 'SunOS')


# Generated at 2022-06-13 01:48:33.462638
# Unit test for method get_interfaces_info of class SunOSNetwork

# Generated at 2022-06-13 01:48:44.133461
# Unit test for method get_interfaces_info of class SunOSNetwork

# Generated at 2022-06-13 01:48:46.471865
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    collector = SunOSNetworkCollector()
    assert collector.platform == 'SunOS'
    assert collector.facts == {}


# Generated at 2022-06-13 01:48:48.145788
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    collector = SunOSNetworkCollector()
    assert isinstance(collector, NetworkCollector)
    assert collector._fact_class is SunOSNetwork
    assert collector._platform is 'SunOS'


# Generated at 2022-06-13 01:48:49.121844
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    assert SunOSNetworkCollector._platform == 'SunOS'

# Generated at 2022-06-13 01:48:52.497162
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    """
    This is a constructor test for class SunOSNetworkCollector
    """
    network_collector = SunOSNetworkCollector()
    assert network_collector.__class__.__name__ == "SunOSNetworkCollector"


# Generated at 2022-06-13 01:49:00.646776
# Unit test for method parse_interface_line of class SunOSNetwork
def test_SunOSNetwork_parse_interface_line():
    module = MockAnsibleModule()
    module.params = {'gather_subset': 'all'}
    network_collector = SunOSNetworkCollector(module)
    network = network_collector.network
    eth_line_1 = 'lo0: flags=1000849<UP,LOOPBACK,RUNNING,MULTICAST,IPv4> mtu 8232 index 1'
    eth_words_1 = eth_line_1.split()
    eth_line_2 = 'lo0: flags=20000849<UP,LOOPBACK,RUNNING,MULTICAST,IPv6> mtu 8232 index 1'
    eth_words_2 = eth_line_2.split()

# Generated at 2022-06-13 01:49:03.402418
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    c = SunOSNetworkCollector()
    assert c.platform == 'SunOS'
    assert c.fact_class == SunOSNetwork

# Generated at 2022-06-13 01:49:15.112736
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    net_collector = SunOSNetworkCollector()
    assert net_collector._platform == 'SunOS'
    assert net_collector._fact_class == SunOSNetwork
    assert net_collector.platform == 'SunOS'
    assert net_collector._fact_class.platform == 'SunOS'

# Generated at 2022-06-13 01:49:16.816836
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    collector = SunOSNetworkCollector()
    assert collector._platform == SunOSNetwork.platform


# Generated at 2022-06-13 01:49:19.863609
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    """Test all possible combinations"""
    o = SunOSNetworkCollector(None, None, {}, [], None)
    assert o.fact_class._platform == 'SunOS'
    assert o.fact_class.platform == 'SunOS'

# Generated at 2022-06-13 01:49:21.662347
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    sunos_network_collector = SunOSNetworkCollector(None)
    assert sunos_network_collector._fact_class == SunOSNetwork

# Generated at 2022-06-13 01:49:28.417528
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    module = AnsibleModule(argument_spec={'gather_subset': dict(type='list', default=['all'])})
    facts = SunOSNetwork()
    # module.get_bin_path is not a method of a AnsibleModule but of a os
    # so we need to wrap it
    module.get_bin_path = lambda *args: '/sbin/ifconfig'
    interfaces, ips = facts.get_interfaces_info('/sbin/ifconfig')
    # we test only few keys
    interfaces_keys = ['lo0', 'net0', 'net1', 'net2']
    ips_keys = ['all_ipv4_addresses', 'all_ipv6_addresses']
    for key in interfaces_keys:
        assert key in interfaces
        assert 'device' in interfaces[key]


# Generated at 2022-06-13 01:49:37.371384
# Unit test for method get_interfaces_info of class SunOSNetwork

# Generated at 2022-06-13 01:49:48.093983
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    """We make sure we have a load of information from /sbin/ifconfig -a output"""
    from os.path import abspath, split
    from sys import path
    from importlib import import_module

    # since we are messing up with sys.path, we need to know the correct root directory
    root_dir = split(abspath(__file__))[0]

    # Python3 requires __pycache__ to be appended
    if '__pycache__' not in root_dir:
        root_dir = root_dir + '/' + '__pycache__'

    # we need our test fixtures to be present in sys.path so the module loader can find them
    path.append(root_dir)

    # let's import our test fixture, a string with the output of "ifconfig -a"

# Generated at 2022-06-13 01:49:59.837837
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    module = AnsibleModule(argument_spec={})
    module.exit_json = lambda: None
    ifconfig_path = '../../../lib/ansible/module_utils/facts/network/fact_collector/solaris_ifconfig.out'

    with open(ifconfig_path, 'r') as f:
        ifconfig = f.read()

    module.run_command = lambda args, check_rc=True: (0, ifconfig, '')
    network_collector = SunOSNetwork(module)
    interfaces, ips = network_collector.get_interfaces_info(module)

    assert interfaces['lo0']['device'] == 'lo0'
    assert interfaces['lo0']['ipv4'][0]['mtu'] == '8232'

# Generated at 2022-06-13 01:50:10.109398
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    test = SunOSNetwork(dict(module=None))

    # Test parsing of the following interface:
    # hme0: flags=1000843<UP,BROADCAST,RUNNING,MULTICAST,IPv4> mtu 1500 index 1
    #       inet 207.111.96.18 netmask ffffff80 broadcast 207.111.96.127
    #       ether 8:0:20:98:1f:3e
    test_if_line = ['hme0:', 'flags=1000843<UP,BROADCAST,RUNNING,MULTICAST,IPv4>', 'mtu', '1500', 'index', '1']
    current_if = test.parse_interface_line(test_if_line, None, {})
    assert current_if['device'] == 'hme0'


# Generated at 2022-06-13 01:50:13.725042
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    import unittest

    class TestSunOSNetworkCollector(unittest.TestCase):

        def test_SunOSNetworkCollector(self):
            SunOSNetworkCollector()

    unittest.main()

# Generated at 2022-06-13 01:50:19.622950
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    SunOSNetworkCollector()

# Generated at 2022-06-13 01:50:29.447983
# Unit test for method parse_interface_line of class SunOSNetwork

# Generated at 2022-06-13 01:50:41.622440
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    from ansible.module_utils.facts.network import SunOSNetwork
    from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork
    import os
    import pytest

    # Unit-test code will execute the test from the tests directory, so use the abspath()
    # of the test_file to find a real path to the test_data directory.
    test_file = os.path.realpath(__file__)
    sunos_ifconfig_path = os.path.join(os.path.dirname(test_file), 'test_data', 'sunos_ifconfig_a.txt')

    # test_data/sunos_ifconfig_a.txt represents the output of the following command on a SunOS machine
    # ifconfig -a
    # By stripping the newlines, we can emulate

# Generated at 2022-06-13 01:50:45.182539
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    module = type('', (object,), dict(params=dict()))()
    fn = NetworkCollector.get_network_collector(module, 'SunOS')
    assert isinstance(fn, SunOSNetworkCollector)


# Generated at 2022-06-13 01:50:56.803864
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    test_module = FakeAnsibleModule()
    test_module.run_command = run_command
    facts_collector = SunOSNetwork(test_module)

    interfaces, ips = facts_collector.get_interfaces_info('/sbin/ifconfig')
    assert_interface('lo0', {'type': 'loopback',
                             'macaddress': '00:00:00:00:00:00',
                             'ipv4': [{'mtu': '1500', 'flags': []}],
                             'ipv6': [{'mtu': '1500', 'flags': ['IPv6', 'MULTICAST']}]}, interfaces)

# Generated at 2022-06-13 01:51:09.201973
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    module = None
    iface_path = '/sbin/ifconfig'
    collector = SunOSNetworkCollector(module, iface_path)
    iface_info, ips = collector.get_interfaces_info()
    assert 'em0' in iface_info
    assert iface_info['em0']['device'] == 'em0'
    assert iface_info['em0']['flags'] == ['UP', 'BROADCAST', 'RUNNING', 'SIMPLEX', 'MULTICAST']
    assert iface_info['em0']['mtu'] == '1500'
    assert iface_info['em0']['macaddress'] == '0:1:2:3:4:5'
    assert iface_info['em0']['ipv4'][0]['address']

# Generated at 2022-06-13 01:51:17.885121
# Unit test for method parse_interface_line of class SunOSNetwork
def test_SunOSNetwork_parse_interface_line():
    # Parameters for the unit test
    module_args = dict(
        gather_subset=['all'],
        config_file='/dev/null',
        ansible_facts=dict()
    )

    def get_cmd_output(*args, **kwargs):
        return rc, out, err

    class MyModule(object):
        def __init__(self, module_args):
            return

        def run_command(self, args):
            return get_cmd_output()

    module = MyModule(module_args)
    # Unit test begins
    sunos_network = SunOSNetwork(module)

# Generated at 2022-06-13 01:51:19.773754
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    obj = SunOSNetworkCollector()
    assert(type(obj) == SunOSNetworkCollector)

# Generated at 2022-06-13 01:51:28.783717
# Unit test for method parse_interface_line of class SunOSNetwork
def test_SunOSNetwork_parse_interface_line():
    module = MockAnsibleModule()
    sn = SunOSNetwork(module=module)
    interfaces = {}
    current_if = {}

    # Check that LOOPBACK interface is defined as 'loopback' and
    # that it uses the IPv4 parse_interface_line code.
    words = ['lo0:', 'flags=2001000849<UP,LOOPBACK,RUNNING,MULTICAST,IPv4,VIRTUAL>', 'mtu', '8232']
    current_if = sn.parse_interface_line(words, current_if, interfaces)
    assert current_if['device'] == 'lo0'
    assert current_if['type'] == 'loopback'
    assert len(current_if['ipv4']) == 1
    assert len(current_if['ipv6']) == 0

   

# Generated at 2022-06-13 01:51:40.970354
# Unit test for method parse_interface_line of class SunOSNetwork
def test_SunOSNetwork_parse_interface_line():
    from ansible.module_utils.facts.network.sunos.facts import SunOSNetwork
    from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork
    ifconfig_path = '/usr/sbin/ifconfig'

    sunosnet = SunOSNetwork(None)
    gensunosnet = GenericBsdIfconfigNetwork(None)

    # Test Solaris/Generic
    words = ['ce0:', 'flags=201000849<UP,LOOPBACK,RUNNING,MULTICAST,IPv4,VIRTUAL>', 'mtu=8232']
    current_if = {}
    interfaces = {}
    current_if = sunosnet.parse_interface_line(words, current_if, interfaces)
    assert current_if['device'] == 'ce0'
   

# Generated at 2022-06-13 01:51:47.226574
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    nc = SunOSNetworkCollector()
    assert nc._fact_class._platform == 'SunOS'

# Generated at 2022-06-13 01:51:57.240049
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    """
    Test method get_interfaces_info
    """
    test_file = './unit/modules/network/files/ifconfig_SunOS.out'
    with open(test_file) as f:
        test_ifconfig_output = f.read()

    # Unit test using mock module.
    class TestAnsibleModule(object):
        class TestRunCommand(object):
            def __init__(self, rc, stdout, stderr):
                """
                Return codes, STDOUT, and STDERR for test_SunOSNetwork.
                test_SunOSNetwork_get_interfaces_info()
                """
                self.rc = rc
                self.stdout = stdout
                self.stderr = stderr
        def __init__(self, run_command):
            self.run_command = run

# Generated at 2022-06-13 01:52:00.560972
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    my_sunosnetworkcollector = SunOSNetworkCollector()
    assert my_sunosnetworkcollector._fact_class == SunOSNetwork
    assert my_sunosnetworkcollector._platform == 'SunOS'
    assert my_sunosnetworkcollector.collect() == {}

# Generated at 2022-06-13 01:52:03.741518
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    platform_facts = SunOSNetworkCollector().collect()
    assert 'SunOS' in platform_facts['ansible_network_resources']['platform']
    assert 'SunOS' in platform_facts['ansible_facts']['ansible_net_gather_platform']

# Generated at 2022-06-13 01:52:05.746486
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    obj = SunOSNetworkCollector()
    obj.collect()  # Just invoke collect() function of the class SunOSNetworkCollector



# Generated at 2022-06-13 01:52:15.485286
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    """Test method get_interfaces_info of class SunOSNetwork"""
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts import collector

    from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork
    from ansible.module_utils.facts.network.sunos import SunOSNetwork

    ifconfig_path = 'tests/unit/module_utils/facts/network/sunos/ifconfig.txt'
    rc, out, err = collector.get_file_content(ifconfig_path)
    ifconfig = to_bytes(out)

    test_collector = collector.collector_from_platform('SunOS')

    test_SunOSNetwork = SunOSNetwork()

# Generated at 2022-06-13 01:52:16.101311
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    SunOSNetworkCollector()


# Generated at 2022-06-13 01:52:17.132561
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    network_collector = SunOSNetworkCollector()
    assert network_collector.platform == 'SunOS'

# Generated at 2022-06-13 01:52:25.990262
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    """ test_SunOSNetwork_get_interfaces_info: Test if Solaris interfaces are parsed correctly """

# Generated at 2022-06-13 01:52:34.027761
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    facts = SunOSNetworkCollector()
    assert facts.get_facts() is None
    assert facts.get_devices() is None
    assert facts.get_ifconfig_path() is None
    assert facts.populate() is None
    assert facts.populate_from_file() is None
    assert facts.populate_from_ifconfig() is None
    assert facts.populate_ip_fact() is None
    assert facts.populate_route_facts() is None
    assert facts.populate_facts() is None
    assert facts.get_network_module_facts() is None

# Generated at 2022-06-13 01:52:43.255275
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    SunOSNetworkCollector({},{})

# Generated at 2022-06-13 01:52:45.161272
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    assert SunOSNetworkCollector._platform == 'SunOS'
    assert SunOSNetworkCollector._fact_class == SunOSNetwork

# Generated at 2022-06-13 01:52:47.643013
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    sunos_network = SunOSNetworkCollector()
    assert sunos_network._fact_class == SunOSNetwork
    assert sunos_network._platform == 'SunOS'

# Generated at 2022-06-13 01:52:50.729225
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    obj = SunOSNetworkCollector('ansible_facts')
    assert(obj.get_fqdn() == 'ansible_facts')
    assert(obj.fact_class == SunOSNetwork)
    assert(obj.platform == 'SunOS')

# Generated at 2022-06-13 01:52:52.536872
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    obj = SunOSNetworkCollector()
    assert obj._fact_class is SunOSNetwork
    assert obj._platform == 'SunOS'

# Generated at 2022-06-13 01:52:53.298667
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    # Create a instance.
    SunOSNetworkCollector()

# Generated at 2022-06-13 01:52:54.326979
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    """Test SunOSNetworkCollector constructor"""
    SunOSNetworkCollector()

# Generated at 2022-06-13 01:52:58.574951
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    module = AnsibleModule(argument_spec={})
    shared_obj = SunOSNetwork()

    ifconfig_path = '/usr/sbin/ifconfig'
    rc, out, err = module.run_command([ifconfig_path, '-a'])

    interfaces, ips = shared_obj.get_interfaces_info(ifconfig_path)
    assert interfaces['lo0']['ipv4'][0]['mtu'] == '8232'
    assert interfaces['lo0']['ipv6'][0]['mtu'] == '8252'



# Generated at 2022-06-13 01:53:01.045071
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    facts = SunOSNetworkCollector().collect()
    assert 'SunOS' in facts['network']


# Generated at 2022-06-13 01:53:03.162273
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    assert SunOSNetwork
    assert SunOSNetworkCollector

# vim: expandtab tabstop=4 shiftwidth=4

# Generated at 2022-06-13 01:53:31.041258
# Unit test for method parse_interface_line of class SunOSNetwork
def test_SunOSNetwork_parse_interface_line():
    # Create a simple interface dict
    dummy_interfaces = {
        "lo0": {
            "device": "lo0",
            "ipv4": [{
                "flags": ["UP", "LOOPBACK", "RUNNING"],
                "mtu": "8232",
            }],
            "ipv6": [],
            "macaddress": "unknown",
            "type": "loopback",
        },
    }

    # Test a simple line
    ifc = SunOSNetwork()
    words = ['lo0:', 'flags=2001000849', 'mtu', '8232']

# Generated at 2022-06-13 01:53:37.317849
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():

    mock_module = MockModule({})
    mock_module.run_command = Mock(return_value=(0, OPENBSD_IFCONFIG_WITH_IPV6, ''))
    mock_ifconfig_class = SunOSNetwork(mock_module)

    # Set up expected values for method get_interfaces_info

# Generated at 2022-06-13 01:53:48.203826
# Unit test for method get_interfaces_info of class SunOSNetwork

# Generated at 2022-06-13 01:53:50.544072
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    module = AnsibleModule(argument_spec=dict())
    network = SunOSNetwork(module=module)

    interfaces = network.get_interfaces_info('/sbin/ifconfig')
    assert interfaces is not None

# Generated at 2022-06-13 01:53:52.644583
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    # If there is no argument, we can assert it will fail by throwing a TypeError
    # which is what we want
    with pytest.raises(TypeError):
        SunOSNetworkCollector()

# Generated at 2022-06-13 01:53:53.782650
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    assert SunOSNetworkCollector._platform == 'SunOS'
    assert SunOSNetworkCollector._fact_class == SunOSNetwork

# Generated at 2022-06-13 01:53:55.790383
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    assert SunOSNetworkCollector._platform == 'SunOS'
    assert SunOSNetworkCollector._fact_class == SunOSNetwork
    assert issubclass(SunOSNetworkCollector._fact_class, NetworkCollector)


# Generated at 2022-06-13 01:54:00.582844
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    from ansible.module_utils.facts.network.generic_bsd import MockModule
    from ansible.module_utils.facts.network.sunos import SunOSNetwork
    from ansible.module_utils.facts.network.sunos import test_SunOSNetwork_get_interfaces_info

    # Create a mock object
    mock = MockModule(
        params=dict(
            gather_subset='!all',  # gather basic network facts only
        )
    )
    # Create an instance of the class SunOSNetwork
    mock_Network = SunOSNetwork(mock)

    # Create a dictionary of interfaces for test

# Generated at 2022-06-13 01:54:02.475935
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    collector = SunOSNetworkCollector()
    assert collector.platform == 'SunOS'
    assert collector._fact_class.__name__ == 'SunOSNetwork'

# Generated at 2022-06-13 01:54:08.659804
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    from ansible.module_utils.facts.network.base import NetworkCollector, Network
    from ansible.module_utils.facts.network.sunos import SunOSNetworkCollector, SunOSNetwork
    f = NetworkCollector
    fn = SunOSNetworkCollector
    assert issubclass(fn, f)
    assert fn._platform == 'SunOS'
    assert fn._fact_class == SunOSNetwork
    assert issubclass(fn._fact_class, Network)

# Generated at 2022-06-13 01:54:52.716660
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    module = AnsibleModule(argument_spec=dict())
    network_collector = SunOSNetworkCollector(module=module)
    assert network_collector is not None

# Generated at 2022-06-13 01:54:53.867682
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    SunOSNetworkCollector()

# Generated at 2022-06-13 01:55:05.046918
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    """
    Test the get_interfaces_info method of SunOSNetwork class.

    Parameters
    ----------

    Returns
    -------
    True if correct otherwise False
    """
    from ansible.module_utils.facts import collector
    import re

    # Set up class
    network = collector.get_network_collector('SunOS', {})

    # Run _get_interfaces_info()
    interfaces, ips = network._get_interfaces_info('/sbin/ifconfig')

    # Test interface e1000g0
    assert interfaces['e1000g0']['macaddress'] == '08:00:27:1a:29:e3'
    assert interfaces['e1000g0']['type'] == 'ether'

    assert len(interfaces['e1000g0']['ipv4']) == 1


# Generated at 2022-06-13 01:55:14.502741
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    testobj = SunOSNetwork()
    testobj.module.run_command = lambda *args: (0,
        'lo0: flags=1000849 mtu 8232 index 1\n        inet 127.0.0.1 netmask ff000000\n        inet6 ::1/128\n        options=3<performnud,accept_rtadv>\n        groups: lo\n        nd6 options=3<performnud,accept_rtadv>\n', '')
    interfaces, ips = testobj.get_interfaces_info('/sbin/ifconfig')
    assert interfaces['lo0']['type'] == 'loopback'
    assert interfaces['lo0']['macaddress'] == 'unknown'
    assert len(interfaces['lo0']['ipv4']) == 1
    ipv

# Generated at 2022-06-13 01:55:18.779876
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    assert not SunOSNetworkCollector.__init__.__defaults__
    assert not SunOSNetworkCollector.__init__.__kwdefaults__
    assert SunOSNetworkCollector.__init__.__code__.co_argcount == 5


# Generated at 2022-06-13 01:55:30.881512
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    module = AnsibleModule(
        argument_spec=dict(
            gather_subset=dict(default=['min'], type='list'),
            gather_network_resources=dict(default=['all'], type='list'),
        )
    )

    # 'ifconfig_path' is expected by a lot of the inherited methods.
    # It only needs to be a string, not a list.
    # Create fake executable with correct name.
    ifconfig_path = 'ifconfig'
    module.get_bin_path = lambda x: ifconfig_path

    # create fake text output

# Generated at 2022-06-13 01:55:33.207490
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    module = MagicMock()
    obj = SunOSNetworkCollector(module)
    assert isinstance(obj, NetworkCollector)
    assert obj.platform == 'SunOS'


# Generated at 2022-06-13 01:55:44.585730
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    """
    This test is intented to test the SunOSNetwork method get_interfaces_info. It tests
    that the correct interfaces are found for a given string. It also tests that the
    correct amount of lines are parsed.
    """
    # Setup string
    # ------------

# Generated at 2022-06-13 01:55:47.045773
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    facts_collector = SunOSNetworkCollector()
    assert facts_collector.platform == 'SunOS'
    assert facts_collector.fact_class == SunOSNetwork

# Generated at 2022-06-13 01:55:48.551252
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    assert SunOSNetworkCollector.platform == 'SunOS'
    assert SunOSNetworkCollector._fact_class == SunOSNetwork
    assert SunOSNetworkCollector._platform == 'SunOS'

# Generated at 2022-06-13 01:57:08.151200
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    """
    Testing method get_interfaces_info of class SunOSNetwork
    """
    # Run tested method
    ifconfig_path = "/usr/sbin/ifconfig"
    test_SunOSNetwork = SunOSNetwork(None)
    ifconfig = test_SunOSNetwork.get_interfaces_info(ifconfig_path)
    # Check result
    # assert len(ifconfig['interfaces']) == 3
    # assert 'ipv4' in ifconfig['interfaces']['lo0']
    # assert 'ipv6' in ifconfig['interfaces']['lo0']
    # assert 'ipv4' in ifconfig['interfaces']['le0']
    # assert 'ipv6' in ifconfig['interfaces']['le0']
    # assert 'ipv4' in ifconfig['interfaces'

# Generated at 2022-06-13 01:57:11.079730
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    module = None
    obj = SunOSNetworkCollector(module)
    assert obj._platform == 'SunOS'
    assert obj._fact_class.__name__ == 'SunOSNetwork'


# Generated at 2022-06-13 01:57:21.122205
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():

    # Create a mock module, and mock the result from the 'run_command' method
    module = AnsibleModule(
        argument_spec={
            'gather_subset': dict(default=['!all'], type='list')
        }
    )
    mock_ifconfig_path = '/sbin/ifconfig'
    mock_ifconfig_rc = 0
    # This ifconfig output is taken from a Solaris 10 box.

# Generated at 2022-06-13 01:57:28.416838
# Unit test for method parse_interface_line of class SunOSNetwork

# Generated at 2022-06-13 01:57:34.767628
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    facts = SunOSNetwork()
    ret = facts.get_interfaces_info("/sbin/ifconfig")
    interfaces = ret[0]
    ips = ret[1]

    assert ret
    assert interfaces['lo0']
    assert interfaces['lo0']['type'] == 'loopback'
    assert interfaces['lo0']['ipv4']
    assert len(interfaces['lo0']['ipv4']) == 1
    assert interfaces['lo0']['ipv4'][0]['address'] == '127.0.0.1'
    assert interfaces['lo0']['ipv4'][0]['netmask'] == '255.0.0.0'
    assert interfaces['lo0']['ipv4'][0]['broadcast'] == '127.255.255.255'

# Generated at 2022-06-13 01:57:36.699007
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    SunOS = SunOSNetwork()

    assert SunOS.platform == 'SunOS'



# Generated at 2022-06-13 01:57:46.814973
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    module = type('AnsibleModule', (object,), {'run_command': run_command})
    setattr(module, '_ansible_debug', True)
    setattr(module, 'params', {})
    setattr(module, 'fail_json', fail_json)
    network = SunOSNetwork(module)

    interfaces = network.get_interfaces_info(IFCONFIG_PATH)
    assert len(interfaces[0]) == 2
    assert interfaces[0]['lo0']['ipv4'][0]['mtu'] == '1500'
    assert interfaces[0]['vboxnet0']['ipv4'][0]['mtu'] == '1500'
    assert interfaces[0]['vboxnet0']['ipv6'][0]['mtu'] == '1500'




# Generated at 2022-06-13 01:57:52.042240
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    # Constructor of SunOSNetworkCollector class
    module = type('', (), {'argument_spec': {}, 'params': {}})
    type(module)._ansible_version = type(
        '', (), {'__version__': (2, 4, 3, 'final', 0)})
    setattr(module, 'exit_json', lambda x: x)
    setattr(module, 'fail_json', lambda x: x)
    setattr(module, 'run_command', lambda x: ([0, '', ''], None))
    net = SunOSNetworkCollector(module=module)
    assert net.get_facts() == {}

# Generated at 2022-06-13 01:57:54.939190
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    module = None
    SunOSNetworkCollector(module)

# unit test for SunOSNetwork

# Generated at 2022-06-13 01:58:04.904557
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    # Mocking the module
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True,
    )

    # Reading the ifconfig -a output from a file
    myfile = open("/tmp/sunos_ifconfig_a", "r")
    ifconfig_out = ""
    for myline in myfile.readlines():
        ifconfig_out = ifconfig_out + myline
    myfile.close()

    # Mocking the module run_command
    def run_command(self, command):
        return (0, ifconfig_out, None)

    # Mocking the module execute function because we don't want to run it
    def execute_module(self):
        pass

    # Mocking the Module class