

# Generated at 2022-06-13 01:48:26.012628
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    from ansible.module_utils.facts.network.sunos import SunOSNetwork

    words = ['lo0:', 'flags=2001000849<UP,LOOPBACK,RUNNING,MULTICAST,IPv4,VIRTUAL>', 'mtu', '8232', 'index', '1',
             'inet', '127.0.0.1', 'netmask', 'ffffff00', 'inet', '6::1', 'prefixlen', '128']
    current_if = {}
    interfaces = {}
    current_if = SunOSNetwork.parse_interface_line(SunOSNetwork, words, current_if, interfaces)
    assert current_if['device'] == 'lo0'
    assert current_if['ipv4'][0]['mtu'] == '8232'

# Generated at 2022-06-13 01:48:28.711217
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    """
    Constructor unit test for class SunOSNetworkCollector
    """
    assert SunOSNetworkCollector(dict(), dict())._platform == 'SunOS'


# Generated at 2022-06-13 01:48:38.828498
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    test_file = open("unit/ansible_facts/network/test_SunOSNetwork.json")
    test_json_data = test_file.read()
    test_file.close()

    test_module = NetworkCollector()
    test_module.module = DummyModule()
    # Fake an ifconfig to get the method get_interfaces_info tested
    test_module.module.run_command = lambda *args, **kw: [0, test_json_data, '']
    test_module.module.warn = lambda *args, **kw: None

    test_module.get_interfaces_info('/sbin/ifconfig')
    test_module.get_interfaces_facts()
    test_module.populate()

# Generated at 2022-06-13 01:48:42.511595
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    collector = SunOSNetworkCollector()
    assert collector.platform == 'SunOS'
    assert collector._fact_class.platform == 'SunOS'
    assert collector._fact_class.get_interfaces_info('/sbin/ifconfig') == (None, None)

# Generated at 2022-06-13 01:48:44.282194
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    assert SunOSNetworkCollector

# Generated at 2022-06-13 01:48:46.687451
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    fact_collection = SunOSNetworkCollector()
    assert fact_collection is not None
    assert fact_collection.platform == 'SunOS'
    assert fact_collection.fact_class._platform == 'SunOS'

# Generated at 2022-06-13 01:48:56.785399
# Unit test for method parse_interface_line of class SunOSNetwork
def test_SunOSNetwork_parse_interface_line():
    module = object()
    sun = SunOSNetwork(module)
    interfaces = {}
    line_ipv4 = "lo0: flags=1000849<UP,LOOPBACK,RUNNING,MULTICAST,IPv4> mtu 8232 index 1"
    line_ipv6 = "lo0: flags=1000829<UP,LOOPBACK,RUNNING,MULTICAST,IPv6> mtu 8252 index 2"
    current_if = sun.parse_interface_line(line_ipv4.split(), {}, interfaces)
    interfaces[current_if['device']] = current_if
    current_if = sun.parse_interface_line(line_ipv6.split(), current_if, interfaces)
    interfaces[current_if['device']] = current_if

# Generated at 2022-06-13 01:49:08.167747
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    module = FakeAnsibleModule()
    module.mock_command('/sbin/ifconfig -a', '/sbin/ifconfig -a')
    interfaces, ips = SunOSNetwork().get_interfaces_info('/sbin/ifconfig')\
        # pylint: disable=unused-variable
    # Test dictionary of interfaces
    for iface in interfaces:
        for v in 'ipv4', 'ipv6':
            assert len(interfaces[iface][v]) == 1
    assert interfaces['lo0']['type'] == 'loopback'
    assert interfaces['lo0']['macaddress'] == '00:00:00:00:00:00'
    assert interfaces['lo0']['ipv4'][0]['flags'] == ['UP', 'LOOPBACK', 'RUNNING']


# Generated at 2022-06-13 01:49:09.830592
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    assert SunOSNetworkCollector.platform == 'SunOS'
    assert SunOSNetworkCollector._fact_class == SunOSNetwork

# Generated at 2022-06-13 01:49:20.378177
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    """
    Test SunOSNetwork.get_interfaces_info() with real output from Solaris 11.

    The output of the command `ifconfig -a` differs on different Solaris
    versions, so we are testing with real output.
    The test output is captured in test/unittests/output/SunOS/ifconfig_a.txt
    """
    class Module(object):
        def __init__(self):
            self.run_command_calls = 0

        def run_command(self, args):
            self.run_command_calls += 1
            if self.run_command_calls == 1:
                return 0, open('test/unittests/output/SunOS/ifconfig_a.txt', 'r').read(), ''
            elif self.run_command_calls == 2:
                return 0, open

# Generated at 2022-06-13 01:49:26.733477
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    obj = SunOSNetworkCollector()
    assert(obj.platform == 'SunOS')
    assert(obj.fact_class == 'SunOSNetwork')

# Generated at 2022-06-13 01:49:28.820288
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    collect = SunOSNetworkCollector()
    assert collect._platform == SunOSNetworkCollector._platform
    assert collect._fact_class == SunOSNetwork

# Generated at 2022-06-13 01:49:31.773084
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    collector = SunOSNetworkCollector()
    assert isinstance(collector._fact_class, SunOSNetwork)
    assert collector._fact_class.platform == 'SunOS'
    assert collector._platform == 'SunOS'

# Generated at 2022-06-13 01:49:39.413752
# Unit test for method parse_interface_line of class SunOSNetwork
def test_SunOSNetwork_parse_interface_line():
    line = ['hme0:', 'flags=1000842', 'mtu', '1500', 'index']
    current_if = {}
    interfaces = {}
    SunOSNetwork.parse_interface_line(line, current_if, interfaces)
    assert 'hme0' in interfaces and interfaces['hme0']['device'] == 'hme0'
    assert 'ipv4' in interfaces['hme0'].keys() and len(interfaces['hme0']['ipv4']) == 1
    assert 'mtu' in interfaces['hme0']['ipv4'][0].keys() and interfaces['hme0']['ipv4'][0]['mtu'] == '1500'

# Generated at 2022-06-13 01:49:43.362693
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    module = AnsibleModuleMock()
    network = SunOSNetwork(module)
    ifconfig_path = '/sbin/ifconfig'
    interfaces, ips = network.get_interfaces_info(ifconfig_path)
    module.exit_json(ansible_facts={'interfaces': interfaces, 'all_ipv4_addresses': ips['all_ipv4_addresses'], 'all_ipv6_addresses': ips['all_ipv6_addresses']})



# Generated at 2022-06-13 01:49:44.821346
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    obj = SunOSNetworkCollector(None, {})
    assert obj.platform == 'SunOS'
    assert obj.fact_class == SunOSNetwork


# Generated at 2022-06-13 01:49:50.675000
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    from ansible.module_utils.facts.network.sunos import SunOSNetwork

    test_data_path = './unit/modules/ansible/module_utils/facts/network/sunos/data/'
    test_data_file = 'ifconfig_a.txt'
    test_data = open(test_data_path + test_data_file).read()
    ifconfig_path = '/sbin/ifconfig'

    interfaces, ips = SunOSNetwork(None).get_interfaces_info(ifconfig_path)

    # Verify interfaces
    assert len(interfaces.keys()) == 5
    assert interfaces['lo0']['type'] == 'loopback'
    assert interfaces['lo0']['ipv4'][0]['mtu'] == '1502'

# Generated at 2022-06-13 01:49:53.240433
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    collector = SunOSNetworkCollector()
    assert collector.platform == 'SunOS'
    assert collector.fact_class == SunOSNetwork
    assert collector.fact_class._platform == 'SunOS'



# Generated at 2022-06-13 01:49:57.495895
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    obj = SunOSNetworkCollector()

    assert isinstance(obj, SunOSNetworkCollector)
    assert obj._fact_class == SunOSNetwork
    assert obj._platform == 'SunOS'

# Generated at 2022-06-13 01:50:07.811508
# Unit test for method get_interfaces_info of class SunOSNetwork

# Generated at 2022-06-13 01:50:20.441812
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    """
    Check if this platform is supported.
    """
    collector = SunOSNetworkCollector()
    assert collector.platform == 'SunOS'


# Generated at 2022-06-13 01:50:22.587521
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    network = SunOSNetworkCollector()
    assert network.platform == 'SunOS'
    assert network._fact_class == SunOSNetwork

# Generated at 2022-06-13 01:50:27.192345
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    # Create an instance of the SunOSNetworkCollector class
    my_obj = SunOSNetworkCollector()
    # my_obj should be an instance of SunOSNetworkCollector
    assert isinstance(my_obj, SunOSNetworkCollector)
    # my_obj should also be instance of NetworkCollector
    assert isinstance(my_obj, NetworkCollector)

# Generated at 2022-06-13 01:50:28.194612
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    SunOSNetworkCollector()

# Generated at 2022-06-13 01:50:38.310044
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    assert SunOSNetworkCollector.platform == 'SunOS'
    assert SunOSNetworkCollector.fact_class._platform == 'SunOS'
    assert SunOSNetworkCollector.fact_class.platform == 'SunOS'
    assert SunOSNetworkCollector.fact_class._fact_class is SunOSNetwork
    assert SunOSNetworkCollector.fact_class._fact_class._platform == 'SunOS'
    assert SunOSNetworkCollector.fact_class._fact_class.platform == 'SunOS'
    assert SunOSNetworkCollector.fact_class.__name__ == 'SunOSNetwork'
    assert SunOSNetworkCollector.fact_class._fact_class.__name__ == 'SunOSNetwork'

# Generated at 2022-06-13 01:50:49.983659
# Unit test for method parse_interface_line of class SunOSNetwork
def test_SunOSNetwork_parse_interface_line():
    out = 'lo0: flags=1000849<UP,LOOPBACK,RUNNING,MULTICAST,IPv4,VIRTUAL> mtu 8232 index 1\n' \
          '      inet 127.0.0.1 netmask ff000000\n'            # v4
          # No v6
    c_dict = {'device': 'lo0', 'ipv4': [], 'ipv6': [], 'type': 'unknown'}
    c_words = out.split()
    c_interface = SunOSNetwork._parse_interface_line(c_words, c_dict)
    assert c_interface['device'] == 'lo0'
    assert c_interface['type'] == 'loopback'
    assert len(c_interface['ipv4']) == 1

# Generated at 2022-06-13 01:51:00.034289
# Unit test for method get_interfaces_info of class SunOSNetwork

# Generated at 2022-06-13 01:51:03.423388
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    facts = dict()
    exp_facts = dict()
    nc = SunOSNetworkCollector(facts, {})
    assert nc.get_facts() == exp_facts

# Generated at 2022-06-13 01:51:13.098927
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    interfaces, ips = SunOSNetwork().get_interfaces_info('/sbin/ifconfig')
    assert interfaces['lo0']['ipv4'][0]['mtu'] == '8754'
    assert interfaces['lo0']['ipv4'][0]['flags'] == ['UP', 'LOOPBACK', 'RUNNING']
    assert interfaces['lo0']['ipv4'][0]['broadcast'] == '127.0.0.1'
    assert interfaces['lo0']['ipv4'][0]['address'] == '127.0.0.1'
    assert interfaces['lo0']['ipv4'][0]['netmask'] == '255.0.0.0'

# Generated at 2022-06-13 01:51:24.826353
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    module = None

# Generated at 2022-06-13 01:51:43.926756
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    SunOSNetworkCollector.test_SunOSNetworkCollector()


if __name__ == '__main__':
    SunOSNetworkCollector.main()

# Generated at 2022-06-13 01:51:51.628490
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    """
    This test parses the output of 'ifconfig -a' on Solaris 11.3
    It confirms that the correct interface, IPv4 and IPv6 facts are discovered.
    IPv4 and IPv6 facts have been moved inside the ip4 and ip6 lists.
    """


# Generated at 2022-06-13 01:52:01.274302
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    testobj = SunOSNetwork()
    testobj.module.run_command = run_command

    interfaces, ips = testobj.get_interfaces_info('/sbin/ifconfig')
    assert interfaces['lo0'] == {'device': 'lo0',
                                 'ipv4': [{'flags': ['UP', 'BROADCAST', 'LOOPBACK', 'RUNNING', 'MULTICAST'], 'mtu': 8232}],
                                 'ipv6': [{'flags': ['UP', 'BROADCAST', 'LOOPBACK', 'RUNNING', 'MULTICAST'], 'mtu': 8232}],
                                 'type': 'loopback',
                                 'macaddress': 'unknown'}

# Generated at 2022-06-13 01:52:10.635199
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    from ansible.module_utils.facts.network.sunos import SunOSNetworkCollector
    sunosNetworkCollector = SunOSNetworkCollector()

    interfaces, ips = sunosNetworkCollector.get_interfaces_info('/sbin/ifconfig')
    assert interfaces['vni100']['ipv4'][0]['address'] == '10.10.10.1'
    assert interfaces['vni100']['ipv6'][0]['address'] == 'fe80::250:56ff:fed8:a8a8/64'

# Generated at 2022-06-13 01:52:20.031792
# Unit test for method parse_interface_line of class SunOSNetwork
def test_SunOSNetwork_parse_interface_line():
    '''Test method parse_interface_line() of class SunOSNetwork'''
    current_if = {}
    interfaces = {}
    interface = 'lo0:'
    words = [interface, 'UP', 'LOOPBACK,', 'RUNNING,', 'MULTICAST']
    current_if = SunOSNetwork.parse_interface_line(SunOSNetwork(), \
        words, current_if, interfaces)
    assert current_if['device'] == 'lo0'
    assert 'ipv4' in current_if
    assert 'ipv6' not in current_if

    # Solaris displays single digit octets in MAC addresses e.g. 0:1:2:d:e:f
    # Add leading zero to each octet where needed.

# Generated at 2022-06-13 01:52:30.281906
# Unit test for method parse_interface_line of class SunOSNetwork
def test_SunOSNetwork_parse_interface_line():
    # Create object for testing
    iface = SunOSNetwork()
    interfaces = {}
    current_if = {}

    # test1: interface doesn't exist
    words = ['test0:', '<UP,BROADCAST>', 'mtu', '1500']
    current_if = iface.parse_interface_line(words, current_if, interfaces)

    assert current_if['device'] == 'test0'
    assert current_if['ipv4'] == [{'flags': ['UP', 'BROADCAST'], 'mtu': '1500'}]
    assert current_if['ipv6'] == []
    assert current_if['type'] == 'unknown'

    # test2: interface already exists
    words = ['test0:', '<UP,BROADCAST,IPv6>', 'mtu', '1500']


# Generated at 2022-06-13 01:52:39.325115
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    module = type('test', (object,), {'run_command': run_command})
    setattr(module, '_ansible_version', (1, 9, 4))

    ifconfig_path = '/sbin/ifconfig'
    test_object = SunOSNetwork(module)
    interfaces_expected, ips_expected = test_object.get_interfaces_info(ifconfig_path)


# Generated at 2022-06-13 01:52:43.468043
# Unit test for method get_interfaces_info of class SunOSNetwork

# Generated at 2022-06-13 01:52:52.727603
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    module = AnsibleModule(argument_spec={})
    module.params['gather_subset'] = ['all']
    module.params['gather_network_resources'] = ['all']
    network = SunOSNetwork(module)

    mockery_path = '/dev/shm/ansibullbot-tests/SunOSNetwork/ifconfig-a'
    with open(mockery_path, 'r') as myfile:
        ifconfig_a_data = myfile.read()

    with patch('ansible.module_utils.network.common.run_commands') as mock_run_commands:
        mock_run_commands.return_value = (0, ifconfig_a_data, '')
        interfaces, ips = network.get_interfaces_info('/usr/sbin/ifconfig')

        # method

# Generated at 2022-06-13 01:52:55.844030
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    """Unit test for constructor of class SunOSNetworkCollector"""
    sunos_network_collector = SunOSNetworkCollector()
    assert sunos_network_collector._fact_class is SunOSNetwork
    assert sunos_network_collector._platform is 'SunOS'

# Generated at 2022-06-13 01:53:32.943153
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    instance = SunOSNetworkCollector()
    assert instance._fact_class == SunOSNetwork
    assert instance._platform == 'SunOS'

# Generated at 2022-06-13 01:53:36.138057
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    obj = SunOSNetworkCollector(None)
    assert isinstance(obj._fact_class, NetworkCollector)
    assert obj._fact_class.__class__.__name__ == 'SunOSNetwork'

# Generated at 2022-06-13 01:53:46.868390
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    module = AnsibleModule(argument_spec={
        'gather_subset': dict(default=[], type='list')})

# Generated at 2022-06-13 01:53:48.608099
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    network_collector = SunOSNetworkCollector()
    assert network_collector.__dict__['_fact_class'].__name__ == 'SunOSNetwork'

# Generated at 2022-06-13 01:53:53.081304
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    print("Test constructor SunOSNetworkCollector")
    obj = SunOSNetworkCollector()
    assert obj
    assert isinstance(obj, SunOSNetworkCollector)
    assert isinstance(obj, NetworkCollector)
    assert obj._fact_class == SunOSNetwork
    assert obj._platform == 'SunOS'

# Unit tests for constructor of class SunOSNetwork

# Generated at 2022-06-13 01:54:02.283864
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    # unit tests need to be in a separate class to avoid an import loop
    import json
    import sys
    import unittest
    from ansible.module_utils.facts import collector

    # Test data created using ifconfig -a on a Solaris 10 system

# Generated at 2022-06-13 01:54:11.582423
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    fake_module = type('obj', (object,), {'run_command': lambda self, commands: (0, sunos_ifconfig_output, '')})()
    fake_module.params = {}
    fake_network = SunOSNetwork(fake_module)
    interfaces, _ips = fake_network.get_interfaces_info('/sbin/ifconfig')
    assert interfaces == sunos_interfaces_expected



# Generated at 2022-06-13 01:54:14.236376
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    """ Test SunOSNetworkCollector constructor """
    SunOSNetworkCollector()

# Generated at 2022-06-13 01:54:17.143546
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    iface = SunOSNetworkCollector()
    assert iface.__class__.__name__ == 'SunOSNetworkCollector'
    assert iface.platform == 'SunOS'


# Generated at 2022-06-13 01:54:24.474531
# Unit test for method get_interfaces_info of class SunOSNetwork

# Generated at 2022-06-13 01:55:46.942904
# Unit test for constructor of class SunOSNetworkCollector

# Generated at 2022-06-13 01:55:57.797388
# Unit test for method parse_interface_line of class SunOSNetwork
def test_SunOSNetwork_parse_interface_line():
    o = SunOSNetwork(None)
    current_if = {}
    interfaces = {}

    words = ['lo0:', 'flags=2001000849<UP,LOOPBACK,RUNNING,MULTICAST,IPv4,VIRTUAL>', 'mtu', '8232']
    current_if = o.parse_interface_line(words, current_if, interfaces)
    assert current_if['device'] == 'lo0'
    assert current_if['macaddress'] == 'unknown'
    assert current_if['type'] == 'loopback'
    assert current_if['ipv4'][0]['flags'] == ['UP', 'LOOPBACK', 'RUNNING', 'MULTICAST', 'IPv4', 'VIRTUAL']
    assert current_if['ipv4'][0]['mtu']

# Generated at 2022-06-13 01:56:05.816754
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    from ansible.module_utils.facts.network.sunos.facts import get_interfaces_info
    ifconfig_path = 'ansible_ifconfig_path'

# Generated at 2022-06-13 01:56:10.446639
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    module = AnsibleModule(argument_spec={})
    collector = SunOSNetworkCollector(module=module)
    assert collector.module == module
    assert collector.platform == 'SunOS'
    assert collector.fact_class == SunOSNetwork



# Generated at 2022-06-13 01:56:21.294198
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    from ansible.module_utils.facts.network.solaris.solaris_ifconfig import get_interfaces_info
    from ansible.module_utils.facts.network.solaris.solaris_ifconfig import interfaces
    from ansible.module_utils.facts.network.solaris.solaris_ifconfig import ips

    interfaces, ips = get_interfaces_info('/sbin/ifconfig')


# Generated at 2022-06-13 01:56:27.680640
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    # In order to use the constructor, AnsibleModule has to be mocked
    module = MagicMock()

    # In order to use the constructor, SunOSNetwork has to be mocked
    sunosnetwork = MagicMock()
    sunosnetwork.platform = 'SunOS'

    # test if the constructor get properly created with the correct values
    sunoscollector = SunOSNetworkCollector(module, sunosnetwork)
    assert sunoscollector.fact_class == sunosnetwork
    assert sunoscollector.platform == sunosnetwork.platform


# Generated at 2022-06-13 01:56:35.480121
# Unit test for method parse_interface_line of class SunOSNetwork
def test_SunOSNetwork_parse_interface_line():
    item_all_zero = ('le0:', 'flags=843<UP,BROADCAST,RUNNING,MULTICAST>', 'mtu', '1500')
    item_all_one = ('bge1:', 'flags=843<UP,BROADCAST,RUNNING,MULTICAST>', 'mtu', '1500')
    item_one_zero = ('igb0:', 'flags=843<UP,BROADCAST,RUNNING,MULTICAST>', 'mtu', '1500')
    item_one_one = ('bge0:', 'flags=843<UP,BROADCAST,RUNNING,MULTICAST>', 'mtu', '1500')

# Generated at 2022-06-13 01:56:36.606497
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    return isinstance(SunOSNetworkCollector(), NetworkCollector)


# Generated at 2022-06-13 01:56:38.381901
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    assert SunOSNetworkCollector._fact_class == SunOSNetwork
    assert SunOSNetworkCollector._platform == 'SunOS'

# Generated at 2022-06-13 01:56:39.882398
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    assert issubclass(SunOSNetworkCollector, NetworkCollector)


# Generated at 2022-06-13 01:57:48.697847
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    facts = SunOSNetworkCollector()
    assert(facts._platform == 'SunOS')

# Generated at 2022-06-13 01:57:51.485527
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    collector = SunOSNetworkCollector(None)
    assert collector._platform == 'SunOS'
    assert collector._fact_class is SunOSNetwork
    assert isinstance(collector._fact_class({}, {}), SunOSNetwork)

# Generated at 2022-06-13 01:58:02.807180
# Unit test for method get_interfaces_info of class SunOSNetwork

# Generated at 2022-06-13 01:58:03.687977
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    SunOSNetworkCollector()


# Generated at 2022-06-13 01:58:08.229673
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    """
    Unit test for method get_interfaces_info of class SunOSNetwork
    """


# Generated at 2022-06-13 01:58:12.678756
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    # globals is a special 'local' variable that is not cleaned up at the end of a function
    # and is available to the caller at the next function call.
    # pylint: disable=global-statement,invalid-name
    global facts
    facts = {}
    collector_ads = ['ansible.module_utils.facts.network.sunos.SunOSNetworkCollector']
    collector = SunOSNetworkCollector(facts, collector_ads)
    assert collector._fact_class is SunOSNetwork
    assert collector._platform == 'SunOS'