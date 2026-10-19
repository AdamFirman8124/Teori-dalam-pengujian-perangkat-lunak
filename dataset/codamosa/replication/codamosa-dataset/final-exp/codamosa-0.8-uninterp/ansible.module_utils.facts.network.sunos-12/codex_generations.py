

# Generated at 2022-06-13 01:48:31.801709
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    from ansible.module_utils.facts import FactCollector
    from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork
    fact_collector = FactCollector("test", "SunOS")
    network_collector = SunOSNetworkCollector(fact_collector)
    fact_collector.collect(network_collector)
    assert isinstance(network_collector._fact_class, GenericBsdIfconfigNetwork)

# Generated at 2022-06-13 01:48:42.425595
# Unit test for method parse_interface_line of class SunOSNetwork
def test_SunOSNetwork_parse_interface_line():
    from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork
    from ansible.module_utils.facts.network.sunos import SunOSNetwork

# Generated at 2022-06-13 01:48:44.280233
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    SunOSNetworkCollector()

# Generated at 2022-06-13 01:48:47.844463
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    assert(issubclass(SunOSNetworkCollector, NetworkCollector))
    assert(SunOSNetworkCollector._platform == 'SunOS')
    assert(SunOSNetworkCollector._fact_class is SunOSNetwork)

# Generated at 2022-06-13 01:48:57.341342
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    """
    Test get_interfaces_info() method of SunOSNetwork class
    """

    module = FakeModule()
    module.warn = FakeModuleWarn

    # make a SunOSNetwork object
    n = SunOSNetwork(module)

    # read in a test file
    n.get_interfaces_info("/tmp/ifconfig_test.out")


# Generate a test file in /tmp, comment the next line and run the file
# then uncomment the following to use the file for testing.
#open("/tmp/ifconfig_test.out","w").write("lo0: flags=2001000849<UP,LOOPBACK,RUNNING,MULTICAST,IPv4,VIRTUAL> mtu 8232 index 1 \n\tinet 127.0.0.1 netmask ff000000 \n\tinet6

# Generated at 2022-06-13 01:49:02.348833
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    collector = SunOSNetworkCollector(None, None)
    assert isinstance(collector, NetworkCollector)
    assert isinstance(collector, SunOSNetworkCollector)
    assert collector._fact_class == SunOSNetwork
    assert collector._platform == 'SunOS'


# Generated at 2022-06-13 01:49:11.300231
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    from ansible.module_utils.facts.network.sunos import SunOSNetwork
    import textwrap

    ifconfig_path = '/sbin/ifconfig'

    # Test unnumbered interface

# Generated at 2022-06-13 01:49:13.907855
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    module = NetworkCollector()
    collector = SunOSNetworkCollector(module)
    assert collector._platform == 'SunOS'

# Generated at 2022-06-13 01:49:15.685640
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    assert SunOSNetworkCollector._platform == 'SunOS'
    assert SunOSNetworkCollector._fact_class == SunOSNetwork

# Generated at 2022-06-13 01:49:19.504730
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    test_dir = os.path.dirname(os.path.realpath(__file__))
    ins = SunOSNetwork()
    # next call will raise an exception if any problem occurs
    ins.get_interfaces_info(os.path.join(test_dir, 'ifconfig_output'))

# Generated at 2022-06-13 01:49:34.924023
# Unit test for method get_interfaces_info of class SunOSNetwork

# Generated at 2022-06-13 01:49:46.255131
# Unit test for method get_interfaces_info of class SunOSNetwork

# Generated at 2022-06-13 01:49:52.110134
# Unit test for method get_interfaces_info of class SunOSNetwork

# Generated at 2022-06-13 01:49:53.760866
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    assert SunOSNetworkCollector._platform == 'SunOS'
    assert SunOSNetworkCollector._fact_class == SunOSNetwork

# Generated at 2022-06-13 01:50:05.674069
# Unit test for method parse_interface_line of class SunOSNetwork
def test_SunOSNetwork_parse_interface_line():
    ic = SunOSNetwork({}, False)
    iface = {}
    print(iface)
    current_if = ic.parse_interface_line(['lo0:'], current_if, iface)
    assert current_if['device'] == 'lo0'
    assert current_if['type'] == 'unknown'
    assert current_if['ipv4'][0]['mtu'] == '8232'
    assert current_if['ipv4'][0]['flags'] == ['IPv4', 'LOOPBACK', 'RUNNING', 'MULTICAST']
    current_if = ic.parse_interface_line(['lo0:'], current_if, iface)
    assert current_if['device'] == 'lo0'
    assert current_if['type'] == 'unknown'

# Generated at 2022-06-13 01:50:07.755550
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    # Check class variables were set correctly
    assert SunOSNetworkCollector._platform == 'SunOS'
    assert SunOSNetworkCollector._fact_class == SunOSNetwork

# Unit tests for constructor of class SunOSNetwork

# Generated at 2022-06-13 01:50:09.499955
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    nc = SunOSNetworkCollector()
    assert nc._platform == "SunOS"


# Generated at 2022-06-13 01:50:20.271353
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    iface = SunOSNetwork(dict())
    iface.module.run_command = lambda x, check_rc=False: (0, ifconfig_sunos_out, '')
    interfaces, ips = iface.get_interfaces_info('/sbin/ifconfig')

# Generated at 2022-06-13 01:50:21.856160
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    collector = SunOSNetworkCollector()
    assert collector.fact_class._platform == 'SunOS'

# Generated at 2022-06-13 01:50:32.910471
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():

    module = None
    ifconfig_path = '/usr/sbin/ifconfig'
    contents = []

# Generated at 2022-06-13 01:50:44.642716
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    facts = {}
    SunOSNetworkCollector(facts, None)
    assert 'network' in facts
    assert facts['network'].platform == 'SunOS'

# Generated at 2022-06-13 01:50:56.284900
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    from ansible.module_utils.facts.network.sunos import SunOSNetwork

    test_SunOSNetwork = SunOSNetwork()

    interfaces, ips = test_SunOSNetwork.get_interfaces_info('/sbin/ifconfig')

    assert 'lo0' in interfaces
    assert 'lo0' in interfaces
    assert 'lo0' in interfaces
    assert 'lo0' in interfaces
    assert 'lo0' in interfaces
    assert 'lo0' in interfaces
    assert 'lo0' in interfaces
    assert 'lo0' in interfaces

    assert 1 == len(interfaces['lo0']['ipv4'])
    assert 1 == len(interfaces['lo0']['ipv6'])


# Generated at 2022-06-13 01:51:02.197733
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    collector = SunOSNetworkCollector()
    expected_fact_class = (NetworkCollector, SunOSNetwork)
    for x in expected_fact_class:
        assert isinstance(collector, x)
    assert collector._platform == 'SunOS'
    assert not collector._validate_interface_exists
    assert collector.platform == 'SunOS'
    assert collector.fallback_interface == 'lo0'

# Generated at 2022-06-13 01:51:14.322751
# Unit test for method parse_interface_line of class SunOSNetwork
def test_SunOSNetwork_parse_interface_line():
    m = SunOSNetwork({})
    current_if = {}
    interfaces = {}
    # test empty current_if
    current_if = m.parse_interface_line(['lo0', 'flags=849<UP,LOOPBACK,RUNNING,MULTICAST>', 'mtu', '8232'], current_if, interfaces)
    assert current_if['ipv4'] == [{'mtu': '8232', 'flags': 'LOOPBACK UP RUNNING MULTICAST'}]
    assert current_if['ipv6'] == []
    assert current_if['type'] == 'loopback'
    # test current_if with ipv4

# Generated at 2022-06-13 01:51:25.884794
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    """
    This test creates class SunOSNetwork, and test if the method get_interfaces_info
    returns the right information.
    """

    # Mocked ifconfig output

# Generated at 2022-06-13 01:51:38.164209
# Unit test for method parse_interface_line of class SunOSNetwork
def test_SunOSNetwork_parse_interface_line():
    module = AnsibleModule(
        argument_spec=dict()
    )
    module.exit_json = exit_json
    module.fail_json = fail_json
    set_module_args(dict(gather_subset=['!all', '!min']))
    network = SunOSNetwork(module)

    current_if = {}
    interfaces = {}
    interfaces_result = {}
    line = "lo0: flags=2001000849<UP,LOOPBACK,RUNNING,MULTICAST,IPv4,VIRTUAL> mtu 8232 index 1"
    words = line.split()
    current_if = network.parse_interface_line(words, current_if, interfaces)
    interfaces_result[current_if['device']] = current_if


# Generated at 2022-06-13 01:51:46.292251
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    net_collector = SunOSNetwork()
    ifaces = net_collector.get_interfaces_info('/sbin/ifconfig')
    assert ifaces[0]['lo0'] == {
        'device': 'lo0', 'ipv4': [{'flags': ['UP', 'LOOPBACK', 'RUNNING'], 'mtu': '8232', 'type': 'loopback'}],
        'ipv6': [{'flags': ['UP', 'LOOPBACK', 'RUNNING'], 'mtu': '8232'}],
        'macaddress': '00:00:00:00:00:00', 'type': 'loopback'
    }

# Generated at 2022-06-13 01:51:56.346372
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    ansible_module = AnsibleModule(argument_spec={})
    ansible_module.exit_json = exit_json
    ansible_module.fail_json = fail_json

    # Test SunOSNetwork.get_interfaces_info()
    # Test input is from Solaris 11.4 running on Virtualbox.
    # Test output was validated manually by inspection.

# Generated at 2022-06-13 01:52:05.215858
# Unit test for method get_interfaces_info of class SunOSNetwork

# Generated at 2022-06-13 01:52:14.953270
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    sample_ifconfig_output = """lo0: flags=2001000849 mtu 8232 index 1
        inet 127.0.0.1 netmask ff000000
        inet6 ::1/128
        ether 8:0:20:a5:d5:ac
        nd6 options=29
        media: Ethernet autoselect (1000baseT <full-duplex>)
        nd6 options=29
        status: active"""

    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=False,
    )

    class MockModule(object):
        def __init__(self):
            self.run_command = module.run_command
            self.params = dict()

    mock_module = MockModule()

    interfaces = dict()
    current_if = dict()

# Generated at 2022-06-13 01:52:34.244228
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    test_lines = """lo0: flags=2001000849 mtu 8232 index 1
        inet 127.0.0.1 netmask ff000000
        options=3<performnud,debug>
        nd6 options=3<performnud,debug>
        ether 0:1:2:3:4:5
        media: Ethernet autoselect (1000baseT full-duplex)
        status: active
name0: flags=2000841<UP,RUNNING,MULTICAST,IPv4> mtu 1500 index 3
        inet 10.1.1.1 netmask ffffff00 broadcast +
        inet6 dead:beef::1/128
        ether 0:1:2:3:4:5
        media: Ethernet autoselect
        status: active""".splitlines()
    test_

# Generated at 2022-06-13 01:52:36.971840
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    from ansible.module_utils.facts.network.sunos.test_sunos_network \
        import SunOSNetwork_unit_test_get_interfaces_info
    SunOSNetwork_unit_test_get_interfaces_info()

# Generated at 2022-06-13 01:52:40.569374
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    SunOSNetwork = SunOSNetwork()
    interfaces, ips = SunOSNetwork.get_interfaces_info("/sbin/ifconfig")
    assert interfaces['lo0']['macaddress'] == '00:00:00:00:00:00'

# Generated at 2022-06-13 01:52:50.448512
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    global module
    module = None

# Generated at 2022-06-13 01:52:53.397190
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    """This unit test is used to test whether the constructor is working of SunOSNetworkCollector.
    This will test whether the network_fact_class and platform_fact_class are set correctly.
    """
    sunos_network = SunOSNetworkCollector()
    assert sunos_network.fact_class._platform == 'SunOS'


# Generated at 2022-06-13 01:52:59.483972
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    module = AnsibleModuleMock({})
    ifconfig_path = "/usr/sbin/ifconfig"
    c = SunOSNetwork(module)
    interfaces, ips = c.get_interfaces_info(ifconfig_path)

    assert interfaces['lo0']['type'] == 'loopback'
    assert interfaces['lo0']['ipv4'][0]['mtu'] == '8232'
    assert interfaces['lo0']['ipv4'][0]['flags'] == ['UP', 'RUNNING', 'IPv4', 'LOOPBACK', 'RUNNING', 'MULTICAST']
    assert interfaces['lo0']['ipv6'][0]['mtu'] == '8252'

# Generated at 2022-06-13 01:53:01.995949
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    network_facts = SunOSNetworkCollector()
    assert network_facts.__class__.__name__ == 'SunOSNetworkCollector'

# Generated at 2022-06-13 01:53:15.236321
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    # Fake module object
    fake_module = type('AnsibleModule', (object,), {'run_command': run_command})
    fake_module.params = {}
    # Fake network module object
    network_module = SunOSNetwork(fake_module)

    interfaces_info, ips_info = network_module.get_interfaces_info('/sbin/ifconfig')

    assert interfaces_info['hme0']['type'] == 'ether'
    assert interfaces_info['lo0']['type'] == 'loopback'
    assert ips_info['all_ipv4_addresses'] == ['10.0.0.1', '192.0.0.1']
    assert ips_info['all_ipv6_addresses'] == ['fe80::1', 'fe80::2']


# run

# Generated at 2022-06-13 01:53:22.476814
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    module = None
    ip_path = '/sbin/ip'

    # test Solaris 'ip -o' output with one interface
    # (Note there is no IPv4 on the interface in this test.)
    cmd_output = '''\
1: lo0: <LOOPBACK,UP,LOWER_UP> mtu 8252 index 1
    inet 127.0.0.1/8 scope host
    inet6 ::1/128
'''

# Generated at 2022-06-13 01:53:24.065742
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    """
    Unit test for constructor of NetworkCollector class
    """
    SunOSNetworkCollector()

# Generated at 2022-06-13 01:53:47.244959
# Unit test for method get_interfaces_info of class SunOSNetwork

# Generated at 2022-06-13 01:53:49.449078
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    network_collector = SunOSNetworkCollector()
    assert network_collector._fact_class.platform == 'SunOS'


# Generated at 2022-06-13 01:53:55.922298
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    """Test class SunOSNetwork.get_interfaces_info()."""
    # Initialise a SunOSNetwork object for testing.
    # Pass in a mocked AnsibleModule object.
    # Set the mocked AnsibleModule.run_command return_values.
    test_module = 'ansible.module_utils.facts.network.sunos.SunOSNetwork'
    test_class = 'SunOSNetwork'
    test_obj = SunOSNetwork(test_module)
    test_obj.module.run_command.return_value = (0, open('tests/SunOS_test_facts.txt',
                                                        'r').read(), "")

    # Call SunOSNetwork.get_interfaces_info
    # Return a tuple of (interfaces_info, ips).

# Generated at 2022-06-13 01:54:05.502182
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    """
    test_SunOSNetwork_get_interfaces_info verifies the SunOSNetwork
    class method get_interfaces_info.
    """
    fake_module = FakeModule(platform='SunOS')
    sunos_network = SunOSNetwork(fake_module)
    # Create a fake ifconfig and ifconfig output

# Generated at 2022-06-13 01:54:08.042264
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    collect = SunOSNetworkCollector()
    assert collect.platform == 'SunOS'

# Generated at 2022-06-13 01:54:09.178719
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    network = SunOSNetworkCollector()
    assert network.platform == 'SunOS'

# Generated at 2022-06-13 01:54:11.385303
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    collector = SunOSNetworkCollector()
    assert isinstance(collector, SunOSNetworkCollector)
    assert collector.platform == 'SunOS'


# Generated at 2022-06-13 01:54:21.497688
# Unit test for method get_interfaces_info of class SunOSNetwork

# Generated at 2022-06-13 01:54:23.395841
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    fc = SunOSNetworkCollector()
    assert isinstance(fc._fact_class, SunOSNetwork)
    assert fc._fact_class.platform == 'SunOS'

# Generated at 2022-06-13 01:54:24.670009
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    assert SunOSNetworkCollector.__name__ == 'SunOSNetworkCollector'



# Generated at 2022-06-13 01:55:00.192562
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    s = SunOSNetworkCollector()
    assert s.facts is None


# Generated at 2022-06-13 01:55:09.303200
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    testobj = SunOSNetwork()

# Generated at 2022-06-13 01:55:20.131430
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():

    module = type('FakeModule', (object,), dict(run_command=lambda x: (0, '', '')))()

    # ifconfig(1M) output for one interface.

# Generated at 2022-06-13 01:55:31.240891
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    obj = SunOSNetwork({})
    result = obj.get_interfaces_info('/sbin/ifconfig')
    assert result[0]['lo0']['ipv6'] == [{'mtu': '8670', 'flags': ['UP', 'RUNNING', 'LOOPBACK', 'MULTICAST', 'IPv6']}]
    assert result[0]['lo0']['ipv4'] == [{'mtu': '8670', 'flags': ['UP', 'RUNNING', 'LOOPBACK', 'MULTICAST']}]
    assert result[0]['lo0']['macaddress'] == 'unknown'
    assert result[0]['lo0']['type'] == 'loopback'

# Generated at 2022-06-13 01:55:35.692395
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    """
    Unit test class SunOSNetworkCollector
    """
    SunOSNetworkCollector_obj = SunOSNetworkCollector()
    assert SunOSNetworkCollector_obj.platform == 'SunOS'
    assert SunOSNetworkCollector_obj._platform == 'SunOS'

# Generated at 2022-06-13 01:55:40.620008
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    collector = SunOSNetworkCollector()
    assert collector.__class__.__name__ == 'SunOSNetworkCollector'
    assert collector._fact_class.__name__ == 'SunOSNetwork'
    assert collector._platform == 'SunOS'


# Generated at 2022-06-13 01:55:48.311965
# Unit test for method parse_interface_line of class SunOSNetwork
def test_SunOSNetwork_parse_interface_line():
    """ Unit test for method parse_interface_line of class SunOSNetwork. """

    # SunOS has separate FLAGS and MTU values for IPv4 and IPv6 addresses on the same interface.

    # Create an instance of class SunOSNetwork
    test_device = SunOSNetwork()
    current_if = {}

    # Testing with interface lo0
    # lo0: flags=1000849<UP,LOOPBACK,RUNNING,MULTICAST,IPv4> mtu 8232 index 1
    # lo0: flags=1000849<UP,LOOPBACK,RUNNING,MULTICAST,IPv4> mtu 8232 index 1
    words = 'lo0: flags=1000849<UP,LOOPBACK,RUNNING,MULTICAST,IPv4> mtu 8232 index 1'.split()
    current

# Generated at 2022-06-13 01:55:52.653851
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    """
    Test class constructor for SunOSNetworkCollector
    """
    sunos_network = SunOSNetworkCollector()
    assert sunos_network._fact_class == SunOSNetwork
    assert sunos_network._platform == 'SunOS'


# Generated at 2022-06-13 01:56:00.749143
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    module = FakeAnsibleModule()
    network = SunOSNetwork(module)

    # Test with ifconfig -a output from Solaris 11.3
    result = network.get_interfaces_info(ifconfig_path='/usr/sbin/ifconfig')

    # Test that interfaces is a dictionary and has the same keys as the output of ifconfig -a
    assert isinstance(result[0], dict)

# Generated at 2022-06-13 01:56:01.738232
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    assert SunOSNetworkCollector.platform == 'SunOS'
    assert SunOSNetworkCollector._fact_class == SunOSNetwork

# Generated at 2022-06-13 01:57:06.701006
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    SunOSNetworkCollector()

# Generated at 2022-06-13 01:57:10.997162
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    facts = {}
    network_collector = SunOSNetworkCollector(facts, None)
    assert network_collector.facts == facts
    assert network_collector.platform == 'SunOS'
    assert network_collector.fact_class == SunOSNetwork
    assert network_collector.fact_subclass == None


# Generated at 2022-06-13 01:57:20.990783
# Unit test for method parse_interface_line of class SunOSNetwork
def test_SunOSNetwork_parse_interface_line():
    # Dummy class for testing
    class Dummy:
        def __init__(self):
            self.interfaces = {}
            self.module = Dummy()
            self.module.params = {}
            self.module.run_command = lambda x, check_rc=True: (0, '', '')

    a = SunOSNetwork(Dummy())
    # Test a line returned by "ifconfig -a"
    words = 'lo0: flags=1000849<UP,LOOPBACK,RUNNING,MULTICAST,IPv4> mtu 8232 index 1'.split()
    current_if = {'device': 'lo0', 'type': 'unknown', 'ipv4': [{'flags': [], 'mtu': ''}, ], 'ipv6': []}

# Generated at 2022-06-13 01:57:24.632671
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    """
    Constructor test for class SunOSNetworkCollector
    """
    SunOS_NetworkCollector_obj = SunOSNetworkCollector()
    assert SunOS_NetworkCollector_obj._fact_class == SunOSNetwork
    assert SunOS_NetworkCollector_obj._platform == 'SunOS'


# Generated at 2022-06-13 01:57:32.135905
# Unit test for method parse_interface_line of class SunOSNetwork
def test_SunOSNetwork_parse_interface_line():
    """
    This function tests the method parse_interface_line
    """
    # This is a fake interface
    interface = 'lo0'
    # This is a fake ipv4 flags
    ipv4_flags = 'UP LOOPBACK RUNNING'
    # This is a fake ipv6 flags
    ipv6_flags = 'UP LOOPBACK RUNNING IPv6'
    # This is a fake mtu
    mtu = '8232'
    # These are some fake words
    words = [interface, ipv4_flags, 'mtu', mtu]
    if_lo0 = {interface: {'device': interface, 'ipv4': [], 'ipv6': [], 'type': 'unknown'}}

# Generated at 2022-06-13 01:57:37.410909
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    """ This will test if SunOSNetworkCollector is a subclass of NetworkCollector"""
    assert issubclass(SunOSNetworkCollector, NetworkCollector)
    assert issubclass(SunOSNetwork, GenericBsdIfconfigNetwork)

    net_collector = SunOSNetworkCollector()
    assert isinstance(net_collector, SunOSNetworkCollector)
    assert not net_collector._cache.invalid_cache

# Generated at 2022-06-13 01:57:41.497504
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    mc = SunOSNetworkCollector(None, None)
    assert isinstance(mc, SunOSNetworkCollector)
    assert mc.platform == 'SunOS'
    assert mc._fact_class == SunOSNetwork
    assert mc._fact_class.platform == 'SunOS'

# Generated at 2022-06-13 01:57:45.430416
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    """
    Unit test for constructor of class SunOSNetworkCollector
    """
    # Test with no argument
    net_collector = SunOSNetworkCollector()
    assert net_collector._fact_class == SunOSNetwork
    assert net_collector._platform == 'SunOS'

# Generated at 2022-06-13 01:57:52.168118
# Unit test for method parse_interface_line of class SunOSNetwork
def test_SunOSNetwork_parse_interface_line():
    # Initialize test object state
    test_SunOSNetwork_obj = SunOSNetwork()
    test_SunOSNetwork_obj._module = {
        'run_command': [
            ('/usr/sbin/ifconfig -a', 0, '', ''),
            ('/usr/sbin/ifconfig -a', 0, '', ''),
            ('/usr/sbin/ifconfig -a', 0, '', '')
        ]
    }
    test_SunOSNetwork_obj.module.run_command = test_SunOSNetwork_obj.run_commands

# Generated at 2022-06-13 01:57:56.460699
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    network_collector = SunOSNetworkCollector()
    assert network_collector._platform == 'SunOS'
    assert network_collector._fact_class == SunOSNetwork
