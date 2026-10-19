

# Generated at 2022-06-13 01:37:48.736598
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    # Test object create
    network = HPUXNetwork()

    # Test method populate
    network.populate()



# Generated at 2022-06-13 01:37:53.232992
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    test_object = HPUXNetwork()
    # pylint: disable=protected-access
    result = test_object._get_default_interfaces()
    assert result == {'default_interface': 'lan1', 'default_gateway': '192.168.244.1'}



# Generated at 2022-06-13 01:37:57.711843
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    network_fact_collector = HPUXNetworkCollector()
    assert network_fact_collector
    assert network_fact_collector._fact_class == HPUXNetwork
    assert network_fact_collector._platform == 'HP-UX'


# Generated at 2022-06-13 01:38:05.559478
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    module = type('_module', (object,), {})
    module.run_command = run_command_mock
    module.get_bin_path = get_bin_path_mock

    # Creating an instance of HPUXNetwork using the module
    hpux_net = HPUXNetwork(module)
    collected_facts = {}
    network_facts = hpux_net.populate(collected_facts)
    # the result is tested below in the assert statement
    assert network_facts['interfaces'] == ['lan0', 'lan1']


# Generated at 2022-06-13 01:38:09.883438
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    network_collector = HPUXNetworkCollector()
    # Test 1: Setup the class
    assert network_collector is not None
    # Test 2: Test the platform matches the class
    assert(network_collector.platform == 'HP-UX')
    # Test 3: Test the fact_class matches the class
    assert(network_collector.fact_class.__name__ == 'HPUXNetwork')

# Generated at 2022-06-13 01:38:13.382355
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    """ method HPUXNetwork.get_interfaces_info returns a dict """
    my_hpux_network = HPUXNetwork()
    interfaces = my_hpux_network.get_interfaces_info()
    key = interfaces.keys()[0]
    assert key is not None and type(interfaces[key]) is dict

# Generated at 2022-06-13 01:38:18.006329
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    device1 = {'device': 'lan0',
               'ipv4': {'network': '0.0.0.0', 'address': '192.168.1.1'}}
    device2 = {'device': 'lan1',
               'ipv4': {'network': '0.0.0.0', 'address': '192.168.1.101'}}

    module = AnsibleModule(argument_spec={})
    module.run_command = Mock(return_value=(0, "", ""))

    # Return two interfaces
    module.run_command = Mock(side_effect=[(0, "", ""), (0, unit_test_data, "")])

    network = HPUXNetwork(module)
    facts = network.populate()
    assert facts['default_interface'] == 'lan0'
   

# Generated at 2022-06-13 01:38:27.932052
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    network = HPUXNetwork()
    network.module = MagicMock()
    network.module.run_command.return_value = 0, '', ''

    network.get_default_interfaces = MagicMock()
    network.get_interfaces_info = MagicMock()

    interfaces = {'lan0': {'device': 'lan0',
                           'ipv4': {'address': '192.168.0.5'}}}
    network.get_interfaces_info.return_value = interfaces
    default_interfaces_facts = {'default_interface': 'lan0',
                                'default_gateway': '192.168.0.1'}
    network.get_default_interfaces.return_value = default_interfaces_facts


# Generated at 2022-06-13 01:38:38.953976
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    """
    test method 'populate' of class HPUXNetwork
    """
    mod = AnsibleModule(argument_spec={})
    obj = HPUXNetwork(mod)
    result = obj.populate()
    # Expected result for test1:
    #   interface lan3
    #        ip addresses: 10.100.100.100/24 and 10.100.100.101/24
    #   default interface: lan3
    #   default gateway: 10.100.100.1
    host = 'test1'

# Generated at 2022-06-13 01:38:42.188859
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    # Function under test
    network = HPUXNetwork()
    default_interfaces = network.get_default_interfaces()
    # The test
    assert default_interfaces['default_gateway'] == '127.0.0.1'


# Generated at 2022-06-13 01:38:51.745142
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    """
    Return true if HPUXNetworkCollector is instantiated correctly.
    """
    hn = HPUXNetworkCollector()
    assert isinstance(hn, NetworkCollector)


# If HPUXNetworkCollector is a class, the following line will
# call the constructor of HPUXNetworkCollector.
hn = HPUXNetworkCollector()

# Generated at 2022-06-13 01:39:01.083661
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    module = HPUXNetwork(dict())
    network_facts = module.populate()
    assert network_facts['default_interface'] == 'lan0'
    assert network_facts['default_gateway'] == '10.111.11.4'
    assert network_facts['interfaces'] == ['lan0']
    assert network_facts['lan0']['device'] == 'lan0'
    assert network_facts['lan0']['ipv4']['address'] == '10.111.11.19'
    assert network_facts['lan0']['ipv4']['network'] == '10.111.11.0'


# Generated at 2022-06-13 01:39:02.159245
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    HPUXNetworkCollector()

# Generated at 2022-06-13 01:39:04.179557
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    network_collector = HPUXNetworkCollector()
    assert network_collector is not None

# Generated at 2022-06-13 01:39:14.530155
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    hpn = HPUXNetwork()
    hpn._module.run_command = lambda x: None
    hpn.default_interfaces = {'default_interface': 'lan0',
                              'default_gateway': '10.95.194.1'}
    hpn.get_interfaces_info = lambda: {'lan0': {'ipv4': {'address': '10.95.194.23'}}}
    out = hpn.populate()
    assert out['lan0'] == {'ipv4': {'address': '10.95.194.23'}, 'device': 'lan0'}
    assert out['default_interface'] == 'lan0'
    assert out['default_gateway'] == '10.95.194.1'
    assert out['interfaces'] == ['lan0']

# Generated at 2022-06-13 01:39:16.711424
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    h = HPUXNetworkCollector()
    h.collect()

    assert h.facts == {}

# Generated at 2022-06-13 01:39:22.925056
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    module = Mock()
    netstat = Mock(side_effect=lambda *args, **kwargs: (0, "", ""))
    module.get_bin_path.return_value = '/usr/bin/netstat'
    module.run_command.return_value = (0, "", "")
    hpux_network = HPUXNetwork(module)
    hpux_network.get_default_interfaces()
    hpux_network.get_interfaces_info()



# Generated at 2022-06-13 01:39:23.637488
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    HPUXNetwork()


# Generated at 2022-06-13 01:39:24.607592
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    assert HPUXNetworkCollector._platform == 'HP-UX'

# Generated at 2022-06-13 01:39:32.827902
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    # Test data, which is returned from module.run_command
    out_test = 'default 192.0.2.0   UG        0 0        0 lan0'
    # Test object
    test_hpux_network = HPUXNetwork()
    # Object method, which is under test
    method_of_test_object = test_hpux_network.get_default_interfaces
    # Methods of test object, which are necessary for calling the object
    # method under test, should be replaced to mock functions.
    test_hpux_network.module = MagicMock()
    test_hpux_network.module.run_command = MagicMock()
    test_hpux_network.module.run_command.return_value = (0, out_test, '')
    # Call the object method under test
    rc = method_of

# Generated at 2022-06-13 01:39:47.098638
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    class HPModule(object):
        @classmethod
        def run_command(cls, cmd, *args, **kwargs):
            return 0, test_output, ''

    test_output = '''
     Routing tables

Internet:
Destination        Gateway           Flags   Refs     Use  Iflags
default            172.168.242.254   UGRS      6   413372     0
127.0.0.1          127.0.0.1         UH         4  3168142     0

    '''

    result = HPUXNetwork().get_default_interfaces()
    #assert result == {'default_interface': 'lan0', 'default_gateway': '172.168.242.254'}
    print(result)



# Generated at 2022-06-13 01:39:48.856116
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    hpx_network = HPUXNetwork()
    assert hpx_network.platform == 'HP-UX'

# Generated at 2022-06-13 01:39:50.606610
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    network = HPUXNetwork()
    assert network.platform == 'HP-UX'


# Generated at 2022-06-13 01:39:59.749623
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    module = FakeAnsibleModule()
    m_run_command = FakeCommand()

# Generated at 2022-06-13 01:40:06.505989
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    """
    Unit test for method get_default_interfaces of class HPUXNetwork
    """
    fake_module = type('FakeModule', (), {'run_command': 'fake_run_command'})
    net = HPUXNetwork(fake_module)
    assert net.get_default_interfaces() == {'default_gateway': '127.0.0.1',
                                            'default_interface': 'lo0'}

# Generated at 2022-06-13 01:40:14.910707
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    test_hostname = 'hostname'
    test_module = NetworkCollector._get_test_module(test_hostname)
    test_device_name = 'test_device'
    test_device = {'device': test_device_name, 'ipv4': {'address': '10.10.10.10'}}
    test_default_interface = 'test_default_interface'
    test_default_gateway = 'test_default_gateway'
    test_interfaces = list(test_device.keys())
    test_facts = {'default_interface': test_default_interface,
                  'default_gateway': test_default_gateway,
                  'interfaces': test_interfaces,
                  test_device_name: test_device}
    test_network = HPUXNetwork(test_module)
   

# Generated at 2022-06-13 01:40:21.988304
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    hpnw = HPUXNetwork()
    # populate facts from mock data
    out = """
    default 192.168.0.1 UG
    """
    hpnw.module = None
    hpnw.module.run_command = lambda x: (0, out, '')
    hpnw.populate()
    network_facts = hpnw.facts
    assert network_facts['default_interface'] == 'lan0'
    assert network_facts['default_gateway'] == '192.168.0.1'
    assert network_facts['interfaces'] == ['lan0']
    assert network_facts['lan0']['device'] == 'lan0'
    assert network_facts['lan0']['ipv4']['address'] == '192.168.0.10'

# Generated at 2022-06-13 01:40:24.270623
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    net_obj = HPUXNetwork()
    interface = net_obj.get_default_interfaces()
    assert isinstance(interface, dict)

# Generated at 2022-06-13 01:40:30.037508
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    # Create instance of class HPUXNetworkCollector
    test_obj = HPUXNetworkCollector()
    assert test_obj
    # Tests whether the class name is the same
    assert test_obj.__class__.__name__ == "HPUXNetworkCollector"
    # Tests whether the platform name is the same
    assert test_obj._platform == "HP-UX"
    # Tests whether the fact class is the same
    assert test_obj._fact_class == HPUXNetwork


# Generated at 2022-06-13 01:40:41.108763
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    """
    Unit test for method get_interfaces_info of class HPUXNetwork
    """
    class MockModule(object):
        """
        Mock class for AnsibleModule
        """
        def __init__(self):
            self.params = {}

        def run_command(self, command):
            """
            Run command method
            """
            class MockCommand(object):
                """
                Mock class for command
                """

# Generated at 2022-06-13 01:40:52.399281
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    network = HPUXNetwork()
    assert network


# Generated at 2022-06-13 01:40:59.625955
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    from ansible.module_utils.facts import FactCollector
    from ansible.module_utils.facts.network.hpuux import HPUXNetwork
    from ansible.module_utils.facts.network import NetworkCollector
    from ansible.module_utils.facts.network.hpux import HPUXNetworkCollector

    fact_collector = FactCollector()
    fact_collector.collect_platform_facts()
    fact_collector.collect()

    hpux_network = HPUXNetwork(fact_collector)
    interfaces = hpux_network.get_interfaces_info()

    assert(interfaces['lan0']['device'] == 'lan0')

    hpux_network_collector = HPUXNetworkCollector()
    network_facts = hpux_network_collector.collect(fact_collector)

# Generated at 2022-06-13 01:41:07.118134
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    from ansible.module_utils.facts.network.hpux import HPUXNetwork
    from ansible.module_utils import basic

    mock_module = basic.AnsibleModule(
        argument_spec={
            'gather_subset': dict(default=[], type='list'),
            'gather_network_resources': dict(default=[], type='list')
        }
    )
    network = HPUXNetwork(mock_module)
    result = network.get_default_interfaces()
    assert result['default_interface'] == 'lan1000'

# Generated at 2022-06-13 01:41:08.000378
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    assert HPUXNetwork



# Generated at 2022-06-13 01:41:18.072266
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    """Unit test for constructor of class HPUXNetworkCollector"""

    def mock_run_commands(module, commands):
        rc, out, err = (0, '', '')
        for cmd in commands:
            if cmd[0] == '/usr/bin/netstat -nr':
                out = 'default 192.168.0.1 UGSc 5 0'
            if cmd[0] == '/usr/bin/netstat -niw':
                out = ('lan0 192.168.0.1 192.168.0.0 UP')
        rc, out, err = (0, out, err)
        return rc, out, err

    # Save the run_commands method.
    saved_commands = Network.run_commands


# Generated at 2022-06-13 01:41:19.160500
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    module = None
    network = HPUXNetwork(module=module)
    assert network.populate() is not None

# Generated at 2022-06-13 01:41:24.565202
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    """Unit test to check constructor of class HPUXNetworkCollector"""
    hupux_network_collector = HPUXNetworkCollector()
    assert isinstance(hupux_network_collector, HPUXNetworkCollector)
    assert hupux_network_collector._fact_class is HPUXNetwork
    assert hupux_network_collector._platform is 'HP-UX'


# Generated at 2022-06-13 01:41:25.960273
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    network = HPUXNetwork()
    assert network.platform == 'HP-UX'

# Generated at 2022-06-13 01:41:27.866861
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    collector = HPUXNetworkCollector()
    assert collector.platform == "HP-UX"
    assert collector.fact_class == HPUXNetwork

# Generated at 2022-06-13 01:41:33.451830
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    module = MagicMock()
    module.run_command = MagicMock(return_value=(0,
                                                 'lan0 lan0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0 '
                                                 '0x2a0b03000800fe07 24576   8589934592 8589934592 '
                                                 '8.589934E+09 8.589934E+09 0xffff8000 127.0.0.1', ''))
    HPUXNetwork = HPUXNetworkCollector._fact_class()
    HPUXNetwork.module = module
    iface_info = HPUXNetwork.get_interfaces_info()

# Generated at 2022-06-13 01:42:03.104723
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    collected_facts = {}
    HPUXNetworkCollector(collected_facts).populate_facts()
    assert 'default_interface' in collected_facts
    assert 'default_gateway' in collected_facts
    assert 'interfaces' in collected_facts
    assert 'lan0' in collected_facts
    assert 'lan0' in collected_facts['interfaces']
    assert 'ipv4' in collected_facts['lan0']
    assert 'network' in collected_facts['lan0']['ipv4']
    assert 'address' in collected_facts['lan0']['ipv4']

# Generated at 2022-06-13 01:42:06.180336
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    module = AnsibleModule(argument_spec=dict())
    network_info = HPUXNetwork(module)
    assert network_info
    assert network_info.platform == 'HP-UX'
    assert network_info.module is module


# Generated at 2022-06-13 01:42:09.849196
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    net = HPUXNetwork(dict(module=dict()))
    assert net is not None
    assert net.platform == 'HP-UX'
    assert net._fact_class == HPUXNetwork
    assert net.populate() == {}



# Generated at 2022-06-13 01:42:19.745742
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    module = AnsibleModule(
        argument_spec=dict()
    )
    network = HPUXNetwork(module)

    # mock the get_bin_path method to return the path of the netstat command
    def mypath(path):
        return "/usr/bin/netstat"
    network.get_bin_path = mypath

    # mock get_default_interfaces()
    def mydefault_interfaces():
        return {'default_interface': 'lan0',
                'default_gateway': '127.0.0.1'}
    network.get_default_interfaces = mydefault_interfaces

    # mock get_interfaces_info

# Generated at 2022-06-13 01:42:22.521476
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    network_collector_info = HPUXNetworkCollector()
    assert network_collector_info is not None

# Generated at 2022-06-13 01:42:26.711816
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    net = HPUXNetwork()
    result = net.get_default_interfaces()
    assert 'default_interface' in result
    assert 'default_gateway' in result
    assert result['default_interface'] == 'lan0'
    assert result['default_gateway'] == '172.16.0.254'


# Generated at 2022-06-13 01:42:32.476308
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    """
    Test get_default_interfaces method of HPUXNetwork class
    """
    # Sample output from netstat -nr
    netstat_out = 'default 192.168.122.0 UGSc 0 0 lan0'
    class Module:
        def __init__(self):
            pass

        def get_bin_path(self, path):
            return 'path'

        def run_command(self, command):
            return 0, netstat_out, ''

    module = Module()
    network = HPUXNetwork(module)
    default_interface = network.get_default_interfaces()
    default_interface_expected = {
        'default_interface': 'lan0',
        'default_gateway': '192.168.122.0'
    }
    assert default_interface == default_interface_expected




# Generated at 2022-06-13 01:42:34.371055
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    pass


# Generated at 2022-06-13 01:42:41.646515
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    def run_mock():
        return 0, 'default 192.168.1.1 UGSc 22 0 lan0\n' \
                  'default 192.168.1.2 UGSc 24 0 lan1', ''
    get_bin_path_mock = lambda self, x: 'netstat'
    module = Mock()
    module.get_bin_path = get_bin_path_mock
    module.run_command = run_mock
    hpux_network = HPUXNetwork(module)
    default_interfaces = hpux_network.get_default_interfaces()
    assert default_interfaces is not None
    assert default_interfaces['default_interface'] == 'lan0'
    assert default_interfaces['default_gateway'] == '192.168.1.1'



# Generated at 2022-06-13 01:42:52.917433
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    # Test with no arguments
    hpn = HPUXNetwork()
    hpn_facts = hpn.populate()
    assert 'default_interface' in hpn_facts
    assert hpn_facts['default_interface'] == 'lan0'
    assert hpn_facts['default_gateway'] == '10.0.2.2'
    assert 'interfaces' in hpn_facts
    assert 'lan0' in hpn_facts['interfaces']
    assert hpn_facts['lan0']['device'] == 'lan0'
    assert hpn_facts['lan0']['ipv4']['address'] == '10.0.2.15'
    assert hpn_facts['lan0']['ipv4']['network'] == '10.0.2.0'

# Generated at 2022-06-13 01:43:46.448856
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    from ansible.module_utils.facts.network.hpux import HPUXNetwork
    input_data = """
Kernel Interface table
lan0         Link encap:Ethernet  HWaddr 0:c0:bf:8a:1e:9f
             inet addr:10.8.8.28  Bcast:10.8.8.255  Mask:255.255.255.0
             inet6 addr: fe80::2c0:bfff:fe8a:1e9f%lan0/64 Scope:Link
"""
    expected_result = {'lan0': {'ipv4': {'address': '10.8.8.28',
                                         'interface': 'lan0',
                                         'network': '10.8.8.0'},
                                'device': 'lan0'}}
   

# Generated at 2022-06-13 01:43:52.909499
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    module = AnsibleModule(argument_spec={})
    module.run_command = MagicMock(return_value=(0, 'default          192.168.0.1        UG        lan3                  1', ''))
    h = HPUXNetwork(module=module)
    out = h.get_default_interfaces()
    assert out == {'default_interface': 'lan3', 'default_gateway': '192.168.0.1'}


# Generated at 2022-06-13 01:43:56.287085
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    module = AnsibleModule(argument_spec={})
    hpux_network = HPUXNetwork(module)
    assert hpux_network.platform == 'HP-UX'

# Generated at 2022-06-13 01:43:58.686730
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    netcol = HPUXNetworkCollector()
    assert netcol.platform == 'HP-UX'
    assert netcol._fact_class.platform == 'HP-UX'


# Generated at 2022-06-13 01:44:04.053510
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    net_mod = HPUXNetwork(NetworkCollector)
    net_mod.module.run_command = run_command_mock
    net_mod.get_default_interfaces()
    expected_result = {'default_interface': 'lan0', 'default_gateway': '10.10.10.144'}
    assert expected_result == default_interfaces_result


# Generated at 2022-06-13 01:44:09.218853
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    # Test with no argument
    test_net = HPUXNetwork()
    assert test_net.platform == "HP-UX", "Test with no argument failed"
    # Test with argument
    module_mock = "Test module"
    test_net = HPUXNetwork(module_mock)
    assert test_net.module == "Test module", "Test with argument failed"



# Generated at 2022-06-13 01:44:19.643686
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    module = AnsibleModule(argument_spec={})

    iface = HPUXNetwork(module)

    out_interfaces = ['lan0', 'lan1', 'lan2', 'lan3', 'lan4', 'lan5',
                      'lan6', 'lan7', 'lan8', 'lan9', 'lan10', 'lan11',
                      'lan12', 'lan13', 'lan14', 'lan15', 'lan16', 'lan17',
                      'lan18', 'lan19', 'lan20', 'lan21', 'lan22', 'lan23',
                      'lan24', 'lan25', 'lan26', 'lan27', 'lan28', 'lan29',
                      'lan30', 'lan31', 'lan32', 'lan33', 'lan34']

    assert iface.populate()['interfaces'] == out_interfaces

# Generated at 2022-06-13 01:44:22.898618
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    def __init__(self, module):
        pass

    assert HPUXNetworkCollector.__init__ == __init__
    assert HPUXNetworkCollector.platform == 'HP-UX'


# Generated at 2022-06-13 01:44:23.626680
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    HPUXNetworkCollector()

# Generated at 2022-06-13 01:44:30.199586
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    module = AnsibleModule(
        argument_spec = dict()
    )

    facts_dict = {}
    network_collector = BaseNetworkCollector()
    network_facts = network_collector.populate(facts_dict, module)
    
    assert network_facts.get('default_interface', None) is not None
    assert network_facts.get('default_gateway', None) is not None
    assert network_facts.get('interfaces', None) is not None
    assert network_facts.get('lo0', None) is not None
    assert network_facts['lo0']['device'] == 'lo0'
    assert network_facts['lo0']['ipv4']['address'] == '127.0.0.1'

    ifaces = network_facts.get('interfaces', None)
    iface

# Generated at 2022-06-13 01:46:22.517532
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    module = MockModule()
    module.run_command.return_value = (0, 'default 192.168.1.1 UGSc      3 0 lan0', '')
    hpux_network = HPUXNetwork(module)
    default_interfaces = {'default_interface': 'lan0', 'default_gateway': '192.168.1.1'}
    assert hpux_network.get_default_interfaces() == default_interfaces



# Generated at 2022-06-13 01:46:29.408636
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    module = AnsibleModule(argument_spec={})

# Generated at 2022-06-13 01:46:33.991382
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    test_module = FakeModule()
    test_args = {}

    test_network = HPUXNetwork(module=test_module)

    test_default_interfaces_facts = {'default_interface': 'lan238',
                                     'default_gateway': '172.31.100.254'}
    test_default_interfaces = test_network.get_default_interfaces()
    assert test_default_interfaces == test_default_interfaces_facts


# Generated at 2022-06-13 01:46:38.132634
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    module = NetworkCollector()
    network_facts = HPUXNetwork()
    network_facts.populate()
    network_facts.get_default_interfaces()
    network_facts.get_interfaces_info()
    assert network_facts.platform == 'HP-UX'


# Generated at 2022-06-13 01:46:40.009980
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    facts = HPUXNetworkCollector()
    assert facts._fact_class is not None
    assert facts._platform == 'HP-UX'

# Generated at 2022-06-13 01:46:43.012845
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    facts = { 'system': {}, 'ansible_facts': {} }
    facts['system']['platform'] = 'HP-UX'
    network = HPUXNetwork(facts)
    assert network.platform == 'HP-UX'
    assert network._fact_class == HPUXNetwork

# Generated at 2022-06-13 01:46:45.433403
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    module = AnsibleModule(argument_spec=dict())
    hpux_network = HPUXNetwork(module)
    assert HPUXNetwork.platform == 'HP-UX'



# Generated at 2022-06-13 01:46:51.690998
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():

    class TestModule:
        def __init__(self):
            self.run_command_calls = 0
            self.run_command_paths = []
            self.rc = 0
            self.out = 'out'
            self.err = 'err'

        def get_bin_path(self, _):
            return '/usr/bin/netstat'

        def run_command(self, path):
            self.run_command_calls += 1
            self.run_command_paths.append(path)
            self.rc = 0
            self.out = 'out'
            self.err = 'err'
            self.run_command_value = (self.rc, self.out, self.err)
            return self.run_command_value

    test_module = TestModule()
    net = HPUX

# Generated at 2022-06-13 01:46:57.195083
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    ansible_module_get_bin_path = lambda x: "netstat"
    module = FakeAnsibleModule(
        dict(
            ansible_module_get_bin_path=ansible_module_get_bin_path,
            fact_subset=[
                'all',
                {'default_interface': ['default_interface']},
                {'interfaces': ['interfaces', {'interface_lo0': ['ipv4']}]}
            ]
        )
    )
    network_collector = HPUXNetworkCollector(module)
    network_collector.populate()
    network_facts_subset = network_collector.get_facts()
    # check to make sure default_interface was collected
    assert 'default_interface' in network_facts_subset['default_interface']



# Generated at 2022-06-13 01:46:58.568378
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    net = HPUXNetwork()
    assert net.platform == 'HP-UX'
