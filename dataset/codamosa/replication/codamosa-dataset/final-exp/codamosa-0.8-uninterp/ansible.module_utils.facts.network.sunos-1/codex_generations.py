

# Generated at 2022-06-13 01:48:26.955843
# Unit test for method parse_interface_line of class SunOSNetwork
def test_SunOSNetwork_parse_interface_line():
    # pylint: disable=protected-access
    """Unit test for method parse_interface_line of class SunOSNetwork

    This unit test does the following:
        1) Instantiate a SunOSNetwork object
        2) Call function parse_interface_line with three arguments:
           a) a list of words from an ifconfig -a line:
              ['lo0:', 'flags=1000849<UP,LOOPBACK,RUNNING,MULTICAST,IPv4>', 'mtu', '8232'],
           b) an empty dictionary
           c) a dictionary containing the interfaces defined so far.
           Both b) and c) should be empty because there is no current interface or
           previous interfaces.
        3) Evaluate the resulting dictionary.
    """

# Generated at 2022-06-13 01:48:37.759404
# Unit test for method parse_interface_line of class SunOSNetwork
def test_SunOSNetwork_parse_interface_line():
    # Testing function parse_interface_line
    # Example line: 'lo0: flags=2001000849<UP,LOOPBACK,RUNNING,MULTICAST,IPv4,VIRTUAL> mtu 8232 index 1'
    network = SunOSNetwork()
    current_if = {}
    interfaces = {}
    words = 'lo0: flags=2001000849<UP,LOOPBACK,RUNNING,MULTICAST,IPv4,VIRTUAL> mtu 8232 index 1'.split()
    current_if = network.parse_interface_line(words, current_if, interfaces)

# Generated at 2022-06-13 01:48:38.783183
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    SunOSNetworkCollector()


# Generated at 2022-06-13 01:48:47.461867
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    # create mock object of SunOSNetwork class
    test_obj = SunOSNetwork()

    ifconfig_path = "/sbin/ifconfig"
    # create mock of method 'run_command' of module
    test_obj.module.run_command = run_command_mock

    # call method 'get_interfaces_info'
    interfaces, ips = test_obj.get_interfaces_info(ifconfig_path)

    # check values returned by method

# Generated at 2022-06-13 01:48:49.718781
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    ansible_module_mock = {'run_command.return_value': (0, '', '')}
    collector = SunOSNetworkCollector(ansible_module_mock)
    assert collector.platform == 'SunOS'
    assert collector.fact_class == SunOSNetwork

# Generated at 2022-06-13 01:48:58.797525
# Unit test for method get_interfaces_info of class SunOSNetwork

# Generated at 2022-06-13 01:49:09.818785
# Unit test for method parse_interface_line of class SunOSNetwork
def test_SunOSNetwork_parse_interface_line():
    class module:
        def run_command(self, cmd):
            return 0, '', ''
    class Testclass:
        def __init__(self, module):
            self.module = module
    # Testcase
    #  t: Testclass object
    #  words: Test list of words
    #  current_if: Last interface (before the current one)
    #  interfaces: Known interfaces
    #  expected: Expected result

# Generated at 2022-06-13 01:49:20.376366
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    module = NetworkCollector()
    result = {}
    result['all_ipv4_addresses'] = ['127.0.0.1', '10.240.152.106', '192.168.122.1', '192.168.58.33']
    result['all_ipv6_addresses'] = ['fe80::800:27ff:fe00:0', '::1', 'fe80::a00:27ff:fe12:3456']
    interfaces = {}

# Generated at 2022-06-13 01:49:23.139686
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    module = AnsibleModule(argument_spec={})
    network_collector = SunOSNetworkCollector(module=module)
    assert network_collector._platform == 'SunOS'
    assert network_collector._fact_class == SunOSNetwork


# Generated at 2022-06-13 01:49:24.445339
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    SunOSNetworkCollector()


# Generated at 2022-06-13 01:49:34.804942
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    """Unit test for class SunOSNetworkCollector.

    This is a basic unit test for the constructor of class SunOSNetworkCollector.

    """
    # Test 1: SunOSNetworkCollector().
    # test for: ifconfig_path = self.module.get_bin_path('ifconfig', True)
    #ifconfig_path = self.module.get_bin_path('ifconfig', True)
    #assert(ifconfig_path != None)
    assert(True)


# Generated at 2022-06-13 01:49:43.870400
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    from ansible.module_utils.facts.network.generic_bsd import TestGenericBsdIfconfigNetwork
    import six
    import sys

    if six.PY3:
        from io import StringIO
    else:
        from StringIO import StringIO

    sys.path.insert(0, ".")
    sys.stdout = StringIO()

    test_ovs = TestGenericBsdIfconfigNetwork(SunOSNetwork)
    test_ovs.get_interfaces_info()

    sys.stdout = sys.__stdout__
    print(sys.stdout.getvalue())


# Generated at 2022-06-13 01:49:51.365492
# Unit test for method get_interfaces_info of class SunOSNetwork

# Generated at 2022-06-13 01:49:52.937296
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    collector = SunOSNetworkCollector(None, None)
    assert collector.fact_class == SunOSNetwork

# Generated at 2022-06-13 01:49:55.050847
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    assert isinstance(SunOSNetworkCollector(), NetworkCollector)


# Generated at 2022-06-13 01:50:05.928029
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    module = NetworkCollector()
    ifconfig_path = module.get_bin_path('ifconfig', True)
    network = SunOSNetwork(module=module)
    interfaces, ips = network.get_interfaces_info(ifconfig_path)
    assert interfaces['lo0']['device'] == 'lo0'
    assert interfaces['lo0']['ipv4'][0]['mtu'] == '8232'
    assert interfaces['lo0']['ipv4'][0]['flags'] == ['UP', 'LOOPBACK', 'RUNNING', 'MULTICAST']
    assert interfaces['lo0']['ipv6'][0]['mtu'] == '8252'

# Generated at 2022-06-13 01:50:11.711442
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    info, ips = SunOSNetwork().get_interfaces_info('/sbin/ifconfig')

# Generated at 2022-06-13 01:50:22.285579
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    hostname = 'lo0'
    device = 'lo0'
    options = 'UP LOOPBACK RUNNING MTU:8232 '
    flags = 'LOOPBACK,RUNNING,UP'
    mtu = '8232'
    ipv4 = '127.0.0.1'
    ipv6 = '::1'
    netmask = '8'
    netmask_ipv6 = '128'

    line1 = hostname
    line2 = 'flags=' + flags + ' mtu ' + mtu
    line3 = 'options=' + options
    line4 = 'inet ' + ipv4 + '/' + netmask
    line5 = 'inet6 ' + ipv6 + '/' + netmask_ipv6
    line6 = 'nd6 options=29'


# Generated at 2022-06-13 01:50:32.412678
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    """
    Unit test for method get_interfaces_info of class SunOSNetwork
    """

    bsd_facts = SunOSNetwork()
    bsd_facts.module = MockModule()
    ifconfig_path = '/usr/sbin/ifconfig'
    rc, out, err = bsd_facts.module.run_command([ifconfig_path, '-a'])
    interfaces, ips = bsd_facts.get_interfaces_info(ifconfig_path)
    assert len(interfaces) > 0
    assert len(ips['all_ipv4_addresses']) > 0
    assert len(ips['all_ipv6_addresses']) > 0

from ansible.module_utils.basic import AnsibleModule



# Generated at 2022-06-13 01:50:34.744809
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    assert isinstance(SunOSNetworkCollector._fact_class, type(SunOSNetwork(dict(), None)))



# Generated at 2022-06-13 01:50:45.807812
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    d = SunOSNetworkCollector()
    assert d._platform == 'SunOS'
    assert d._fact_class == SunOSNetwork

# Generated at 2022-06-13 01:50:57.312092
# Unit test for method parse_interface_line of class SunOSNetwork
def test_SunOSNetwork_parse_interface_line():
    current_if = {}
    interfaces = {}
    test_words = ['lo0:', 'flags=2004841<UP,LOOPBACK,RUNNING,MULTICAST,IPv6>', 'mtu', '8232']
    test_if = SunOSNetwork()
    current_if = test_if.parse_interface_line(test_words, current_if, interfaces)
    assert current_if['device'] == 'lo0'
    assert current_if['ipv4'] == []
    assert current_if['ipv6'] == [{'flags': ['UP', 'LOOPBACK', 'RUNNING', 'MULTICAST', 'IPv6'], 'mtu': '8232'}]
    assert current_if['type'] == 'loopback'

# Generated at 2022-06-13 01:51:04.269464
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    """
    Test that get_interfaces_info returns the correct dictionary for Solaris.
    """
    # Solaris physical interface 'e1000g0'
    #  e1000g0: flags=201000843<UP,BROADCAST,RUNNING,MULTICAST,IPv4,CoS> mtu 1500 index 2
    #      inet 10.10.10.120 netmask ffffff00 broadcast 10.10.10.255
    #      ether 0:14:4f:d5:f0:7c
    #      nd6 options=29<PERFORMNUD,IFDISABLED,AUTO_LINKLOCAL>
    #      media: Ethernet autoselect (1000baseT full-duplex,rxpause,txpause)
    #      status: active
    #  e1000g0: flags=21

# Generated at 2022-06-13 01:51:16.127835
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    # Test that the SunOS get_interfaces_info() method parses the output of
    # ifconfig -a correctly
    from ansible.module_utils.facts.network.sunos.test_sunos import TestSunOSNetwork
    from ansible.module_utils.facts.network.sunos.test_sunos import TestSunOSModule
    tsn = TestSunOSNetwork()
    tsm = TestSunOSModule()
    tsm.module.run_command = tsn.run_command
    # tsm.module.get_bin_path('ifconfig')
    tsm.module.get_bin_path = tsn.get_bin_path
    interfaces, _ips = tsn.get_interfaces_info()
    assert interfaces.get('lo0')['ipv4'][0]['mtu'] == '8232'

# Generated at 2022-06-13 01:51:26.819620
# Unit test for method get_interfaces_info of class SunOSNetwork

# Generated at 2022-06-13 01:51:28.033530
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    assert SunOSNetworkCollector.platform == SunOSNetwork._platform

# Generated at 2022-06-13 01:51:31.129975
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    # Dummy import so that Ansible can import NetworkCollector without required
    # packages installed.
    from ansible.module_utils.facts.network import NetworkCollector

    NetworkCollector()


# Generated at 2022-06-13 01:51:35.569898
# Unit test for method get_interfaces_info of class SunOSNetwork

# Generated at 2022-06-13 01:51:45.984006
# Unit test for method parse_interface_line of class SunOSNetwork
def test_SunOSNetwork_parse_interface_line():
    # Test data
    test_data = "bge0: flags=201000843<UP,BROADCAST,RUNNING,MULTICAST,IPv4,COLLISION> mtu 1500 index 3\n"
    test_data += "       inet 10.16.1.40 netmask ffffff00 broadcast 10.16.1.255\n"
    test_data += "       ether 0:14:4f:4b:4e:51"
    # Test execution
    network = SunOSNetwork()
    current_if = network.parse_interface_line(test_data.split(), current_if={}, interfaces={})
    assert current_if.get('device') == 'bge0'
    assert current_if.get('type') == 'unknown'

# Generated at 2022-06-13 01:51:49.287965
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    """
    This test is created by the constructor of the class SunOSNetworkCollector
    """
    # Make sure it has set the class variables
    assert SunOSNetworkCollector._fact_class == SunOSNetwork
    assert SunOSNetworkCollector._platform == 'SunOS'

# Generated at 2022-06-13 01:52:17.350689
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    facts = dict()
    fact_class = NetworkCollector(None, facts, None, None, None)
    fact_class._init_platform()

    assert fact_class._platform == 'SunOS'
    assert fact_class.facts['all_ipv4_addresses'] == []
    assert fact_class.facts['all_ipv6_addresses'] == []
    assert fact_class.facts['interfaces'] == {}
    assert fact_class.facts['default_ipv4']['address'] == ''
    assert fact_class.facts['default_ipv4']['gateway'] == ''
    assert fact_class.facts['default_ipv4']['interface'] == ''
    assert fact_class.facts['default_ipv4']['macaddress'] == ''

# Generated at 2022-06-13 01:52:18.462457
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    assert SunOSNetworkCollector._platform == 'SunOS'

# Generated at 2022-06-13 01:52:21.512387
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    collector = SunOSNetworkCollector
    assert collector._platform == 'SunOS'
    assert collector._fact_class.platform == 'SunOS'
    assert collector._hostname_fact == 'ansible_hostname'



# Generated at 2022-06-13 01:52:22.245643
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    SunOSNetworkCollector()


# Generated at 2022-06-13 01:52:27.796786
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    """
    Tests the 'get_interfaces_info()' method of SunOSNetwork.

    :return:
    """
    from ansible.module_utils.facts import ModuleFactCollector
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts.collector.network.sunos import SunOSNetworkCollector

    # Loads a sample output of 'ifconfig -a' from a Solaris system.
    with open('./tests/unit/module_utils/facts/files/SunOS_ifconfig_a.txt') as f:
        ifconfig_file = f.read()

    # Creates the ModuleCollector which automatically loads all network collectors.
    module_collector = ModuleFactCollector()
    module_collector.collect(None, None, None)

    # Creates the object

# Generated at 2022-06-13 01:52:30.672426
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    my_obj = SunOSNetworkCollector()
    assert my_obj
    assert isinstance(my_obj, SunOSNetworkCollector)

# Generated at 2022-06-13 01:52:33.359592
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    network_collector = SunOSNetworkCollector()
    assert network_collector._fact_class == SunOSNetwork
    assert network_collector._platform == 'SunOS'


# Generated at 2022-06-13 01:52:36.815713
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    """Unit test class SunOSNetworkCollector"""
    from ansible.module_utils.facts.network.sunos import SunOSNetworkCollector
    network_collector = SunOSNetworkCollector()
    assert network_collector._platform is 'SunOS'


# Generated at 2022-06-13 01:52:38.493761
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    assert SunOSNetworkCollector._fact_class == SunOSNetwork
    assert SunOSNetworkCollector._platform == 'SunOS'

# Generated at 2022-06-13 01:52:48.965409
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    from ansible.module_utils.facts.network.sunos import SunOSNetwork
    from ansible.module_utils.facts import FactCollector
    # Get the interface, ips and routes info
    ifconfig_path = '/usr/sbin/ifconfig'

# Generated at 2022-06-13 01:53:27.645971
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    # Test 1
    unittest.main()

# Generated at 2022-06-13 01:53:30.731826
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    sunos_network_collector = SunOSNetworkCollector()
    assert sunos_network_collector._fact_class.platform == 'SunOS'
    assert sunos_network_collector._platform == 'SunOS'

# Generated at 2022-06-13 01:53:34.295838
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    network_collector = SunOSNetworkCollector()
    assert network_collector.__class__.__name__ == 'SunOSNetworkCollector'
    assert network_collector._platform == 'SunOS'
    assert network_collector._fact_class == SunOSNetwork

# Generated at 2022-06-13 01:53:36.008145
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    # Constructor of SunOSNetworkCollector should not raise an exception
    SunOSNetworkCollector()

# Generated at 2022-06-13 01:53:46.743671
# Unit test for method parse_interface_line of class SunOSNetwork
def test_SunOSNetwork_parse_interface_line():
    interfaces = {}
    current_if = {}
    sunos_network = SunOSNetwork()
    v = 'ipv4'
    device = 'lo0'
    flags = 'UP,BROADCAST,LOOPBACK,RUNNING'
    mtu = '8232'
    words = [device + ':', flags, 'mtu', mtu]
    current_if = sunos_network.parse_interface_line(words, current_if, interfaces)
    assert current_if['device'] == device
    assert len(current_if['ipv4']) == 1
    assert len(current_if['ipv6']) == 0
    assert current_if['ipv4'][0]['flags'] == flags
    assert current_if['ipv4'][0]['mtu'] == mtu
    assert current_

# Generated at 2022-06-13 01:53:49.413052
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    collector = SunOSNetworkCollector
    assert collector._platform == 'SunOS'
    assert collector._fact_class.platform == 'SunOS'

# Generated at 2022-06-13 01:53:51.329129
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    # This function is to ensure that SunOSNetworkCollector instantiates properly
    collector = SunOSNetworkCollector()
    assert collector.__class__.__name__ == 'SunOSNetworkCollector'

# Generated at 2022-06-13 01:53:52.612442
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    obj = SunOSNetworkCollector()
    assert obj.platform == SunOSNetwork._platform

# Generated at 2022-06-13 01:53:55.129908
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    assert SunOSNetworkCollector._platform == 'SunOS'
    assert SunOSNetworkCollector.platforms == set(['SunOS'])
    assert SunOSNetworkCollector._fact_class == SunOSNetwork
    assert SunOSNetworkCollector._fallback_fact_class == GenericBsdIfconfigNetwork

# Generated at 2022-06-13 01:53:55.891020
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    SunOSNetworkCollector()

# Generated at 2022-06-13 01:55:34.504412
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    net_class = SunOSNetworkCollector.fact_class({})
    net_class.module = MockModule()
    net_class.module.run_command.return_value = (0, sun_output, '')
    interfaces, ips = net_class.get_interfaces_info('/sbin/ifconfig')
    assert(interfaces['lo0']['ipv6'][0]['addresses'] == ['fe80::1', '::1'])
    assert(interfaces['lo0']['ipv6'][0]['flags'] == ['IPv6'])
    assert(interfaces['lo0']['type'] == 'loopback')
    assert(interfaces['lo0']['mtu'] == 8232)
    assert(interfaces['lo0']['macaddress'] == 'unknown')


# Generated at 2022-06-13 01:55:36.027242
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
   facts = SunOSNetworkCollector()
   assert facts.get_facts() is not None

# Generated at 2022-06-13 01:55:44.254919
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    # Mock module
    module = AnsibleModule(argument_spec={})
    module.params = {}
    network_collector = SunOSNetworkCollector(module)
    # Retrieve facts
    facts = network_collector.get_facts()
    # Assert that SunOSNetworkCollector has been initialized properly
    assert(facts is not None)

if __name__ == '__main__':
    from ansible.module_utils.basic import *

    # Unit test for constructor of class SunOSNetworkCollector
    test_SunOSNetworkCollector()

# Generated at 2022-06-13 01:55:55.593094
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    '''Expect a list of dictionaries containing facts about all interfaces (including loopback).
       Note that IPv4 and IPv6 facts are included in 'ipv4' and 'ipv6' lists respectively.
       '''
    test_module = dict(run_command=lambda x, **kwargs: (0, TEST_IFCONFIG_OUTPUT, ''))
    test_class = SunOSNetwork(module=test_module)
    test_class.get_interfaces_info(ifconfig_path='/sbin/ifconfig -a')
    interfaces = test_class.interfaces
    ips = test_class.ips

    # Interface lo0
    assert interfaces['net0']['device'] == 'net0'
    assert interfaces['net0']['type'] == 'loopback'

# Generated at 2022-06-13 01:56:04.280239
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    (interfaces, ips) = SunOSNetwork(None).get_interfaces_info('/sbin/ifconfig')

    assert len(interfaces.keys()) == 13
    assert len(interfaces['net0']['ipv4']) == 1
    assert interfaces['net0']['ipv4'][0]['address'] == '192.168.0.15'
    assert len(interfaces['net0']['ipv4'][0]['broadcast']) == 1
    assert interfaces['net0']['ipv4'][0]['broadcast'][0] == '192.168.0.255'
    assert len(interfaces['net0']['ipv4'][0]['netmask']) == 1

# Generated at 2022-06-13 01:56:16.197922
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    from module_utils.facts.network.sunos import SunOSNetwork
    from ansible.module_utils._text import to_bytes

    sn = SunOSNetwork({'ansible_module_instance': None}, '', '')

    # Set up an ifconfig output that looks like a Solaris 10 x86 non-global zone
    # that only has IPv6 and lo0 configured

# Generated at 2022-06-13 01:56:26.103276
# Unit test for method parse_interface_line of class SunOSNetwork
def test_SunOSNetwork_parse_interface_line():
    module = AnsibleModule(argument_spec={})
    words = r'lo0: flags=2001000849<UP,LOOPBACK,RUNNING,MULTICAST,IPv4,VIRTUAL> mtu 8232 index 1'.split()
    current_if = {}
    interfaces = {}
    sunos_network = SunOSNetwork()
    output = sunos_network.parse_interface_line(words, current_if, interfaces)
    assert output == {'device': 'lo0', 'ipv6': [], 'ipv4': [{'flags': 'UP,LOOPBACK,RUNNING,MULTICAST,IPv4,VIRTUAL',
        'mtu': '8232'}], 'type': 'loopback', 'macaddress': 'unknown'}
    # assert output == {'ipv6':

# Generated at 2022-06-13 01:56:28.478923
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    collector = SunOSNetworkCollector()
    assert (collector._fact_class is SunOSNetwork)
    assert (collector._platform is 'SunOS')

# Generated at 2022-06-13 01:56:30.472638
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    c = SunOSNetworkCollector()
    assert c._platform == 'SunOS'
    assert c._fact_class == SunOSNetwork



# Generated at 2022-06-13 01:56:38.887689
# Unit test for method get_interfaces_info of class SunOSNetwork