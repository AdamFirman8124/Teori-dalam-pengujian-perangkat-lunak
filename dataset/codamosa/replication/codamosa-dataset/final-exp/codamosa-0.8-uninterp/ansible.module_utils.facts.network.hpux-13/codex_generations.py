

# Generated at 2022-06-13 01:37:46.642337
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    net_coll = HPUXNetworkCollector()
    assert net_coll is not None

# Generated at 2022-06-13 01:37:54.283547
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    from ansible.module_utils.facts.network.base import Network, NetworkCollector
    from ansible.module_utils.facts.network.hpux import HPUXNetwork
    from ansible.module_utils.facts.network.hpux import HPUXNetworkCollector

    class m_module:
        def run_command(self, arg):
            """ Make this method return consistent data. """

# Generated at 2022-06-13 01:38:05.349800
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    # Create an instance of class HPUXNetwork
    hpn = HPUXNetwork()

    # Create a dictionary (mock_facts) containing the facts returned by method populate of class HPUXNetwork
    # and store it as class variable
    hpn.populate()
    collected_facts = hpn.facts
    print(collected_facts)

    # Test if method populate of HPUXNetwork class works correctly

# Generated at 2022-06-13 01:38:15.045152
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    module = AnsibleModule(argument_spec={})
    network = HPUXNetwork()
    # test case 1: no netstat binary
    module.run_command = MagicMock(return_value=(1, '', ''))
    assert network.populate() == {}
    # test case 2: netstat -r command exists
    module.run_command = MagicMock(return_value=(0, 'default 192.168.0.1 \
    192.168.0.0 lan0', ''))
    result = network.populate()
    assert result['default_interface'] == 'lan0'
    assert result['default_gateway'] == '192.168.0.1'
    # test case 3: netstat -niw command exists

# Generated at 2022-06-13 01:38:17.604588
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    HP_network = HPUXNetworkCollector()
    assert HP_network._platform == 'HP-UX'
    assert HP_network._fact_class == HPUXNetwork


# Generated at 2022-06-13 01:38:22.454219
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    instance = HPUXNetworkCollector()
    assert isinstance(instance, dict)
    assert isinstance(instance, HPUXNetworkCollector)
    assert not isinstance(instance, NetworkCollector)
    assert instance._fact_class is HPUXNetwork
    assert instance._platform == 'HP-UX'

# Generated at 2022-06-13 01:38:25.718966
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    module = type('obj', (object,), {'run_command': Network._null_run_command})
    fact = HPUXNetworkCollector(module)
    assert fact.platform == 'HP-UX'


# Generated at 2022-06-13 01:38:33.407548
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    """
    Test the method get_interfaces_info of the class HPUXNetwork on HP-UX system
    """
    class DummyModule:
        def __init__(self):
            self.run_command_stat = 'test'
            self.run_command = ['/usr/bin/netstat -niw', '/usr/bin/netstat -niw']
            self.run_command_rc = [0, 0]

        def run_command(self, cmd, check_rc=True):
            output = str(self.run_command.pop(0))
            return (self.run_command_rc.pop(0), output, '')

    class DummyNetwork:
        def __init__(self):
            self.module = DummyModule()
            self.module.run_command_stat = 'test'
           

# Generated at 2022-06-13 01:38:43.570868
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    net = HPUXNetwork()
    net.module = ModuleStub()

# Generated at 2022-06-13 01:38:49.100817
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    tmod = NetworkCollector()
    tfact = HPUXNetwork(tmod)
    # pylint: disable=protected-access
    result = tfact._get_default_interfaces()
    assert 'default_interface' in result
    assert 'default_gateway' in result
    del tmod
    del tfact
    return


# Generated at 2022-06-13 01:39:01.716022
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    module_mock = MockModule()
    netstat_mock = MockCommand("netstat -nr", '', '', 0)
    module_mock.run_command = netstat_mock
    hpux_network = HPUXNetwork(module_mock)
    default_interfaces_facts = hpux_network.get_default_interfaces()
    assert default_interfaces_facts['default_interface'] == "lan11"
    assert default_interfaces_facts['default_gateway'] == "192.168.11.1"


# Generated at 2022-06-13 01:39:12.332146
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    module = AnsibleModuleMock()
    module.run_command = run_command

    hpux_network = HPUXNetwork(module)
    hpux_network.get_default_interfaces = y
    hpux_network.get_interfaces_info = x

    network_facts = hpux_network.populate()
    assert network_facts['interfaces'] == ['lan0', 'lan1', 'lan2', 'lan3',
                                           'lan4', 'lan5', 'lan6', 'lan7']
    assert network_facts['default_interface'] == 'lan7'
    assert network_facts['default_gateway'] == '9.111.51.113'
    assert network_facts['lan0']['device'] == 'lan0'

# Generated at 2022-06-13 01:39:22.817726
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    network = HPUXNetwork()

# Generated at 2022-06-13 01:39:24.460996
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    HPUXNetworkCollector()


# Generated at 2022-06-13 01:39:26.902158
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    default_interfaces_facts = HPUXNetwork.get_default_interfaces(HPUXNetwork)
    assert 'default_interface' in default_interfaces_facts
    assert 'default_gateway' in default_interfaces_facts


# Generated at 2022-06-13 01:39:30.663497
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    from ansible.module_utils.facts.network.hpux import HPUXNetworkCollector
    from ansible.module_utils.facts.network.hpux import HPUXNetwork
    network = HPUXNetworkCollector()
    assert network
    assert network.platform == 'HP-UX'
    assert network.fact_class == HPUXNetwork


# Generated at 2022-06-13 01:39:31.760027
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    assert HPUXNetwork() is not None

# Generated at 2022-06-13 01:39:34.033286
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    test_object = HPUXNetwork()
    assert test_object.platform == 'HP-UX'
    assert test_object.collector._platform == 'HP-UX'
    assert test_object.collector._fact_class == HPUXNetwork

# Generated at 2022-06-13 01:39:40.790703
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    """Unit test for method get_interfaces_info of class HPUXNetwork"""
    import tempfile
    interface_file = tempfile.NamedTemporaryFile()
    interface_file.write(b'lan1       lan                 9        0        0\n')
    interface_file.seek(0)
    h = HPUXNetwork()
    h.module = MagicMock()
    h.module.run_command.return_value = 0, interface_file.read(), ''
    interfaces = h.get_interfaces_info()
    assert len(interfaces) == 1
    assert interfaces['lan1']['ipv4']['interface'] == 'lan1'
    assert interfaces['lan1']['ipv4']['address'] == '9'
    interface_file.close()

# Generated at 2022-06-13 01:39:42.433074
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    assert HPUXNetwork
    assert HPUXNetwork.platform
    hpn = HPUXNetwork()
    assert hpn.platform == 'HP-UX'

# Generated at 2022-06-13 01:39:58.249405
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    net_mod = HPUXNetwork
    net_mod.module = None
    net_mod.run_command = Mock()
    net_mod.run_command.return_value = (0, "default              192.168.1.1       UG   19      0   0 en0", "")
    default_interfaces = net_mod.get_default_interfaces()
    assert default_interfaces == {'default_interface': 'en0', 'default_gateway': '192.168.1.1'}


# Generated at 2022-06-13 01:40:09.503151
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    class MockModule:
        def __init__(self):
            self.run_command_called = 0
            self.run_command_output = '''lan0: flags=190896<UP,BROADCAST,MULTICAST,NOARP> mtu 1500
            inet 192.168.56.100 netmask 0xffffff00 broadcast 192.168.56.255
            lan1: flags=961<UP,POINTOPOINT,NOTRAILERS> mtu 1500'''

        def run_command(self, cmd):
            self.run_command_called = self.run_command_called + 1
            return (0, self.run_command_output, '')

    mock_module = MockModule()
    network = HPUXNetwork(mock_module)
    result = network.get_interfaces_info()

# Generated at 2022-06-13 01:40:17.498708
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    module = AnsibleModule(argument_spec={})
    default_interfaces_facts = {'default_interface': 'lan0',
                                'default_gateway': '192.168.100.100'}
    facts = {'interfaces': 'lan0',
             'lan0': {'device': 'lan0',
                      'ipv4': {'network': '192.168.100.0/24',
                               'interface': 'lan0',
                               'address': '192.168.100.100'}}}
    network = HPUXNetwork(module)
    module.run_command = Mock()
    module.run_command.return_value = (1, "pv -H | cut -c3-", "")
    facts = network.populate()

# Generated at 2022-06-13 01:40:28.018366
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    """Unit test for method get_interfaces_info of class HPUXNetwork"""

    fake_module = FakeNetworkModule()
    network = HPUXNetwork(fake_module)

    rc = 1

# Generated at 2022-06-13 01:40:31.080053
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    from ansible.module_utils.facts import NetworkCollector
    fact_class = HPUXNetworkCollector()
    assert fact_class._fact_class is HPUXNetwork
    assert fact_class._platform is 'HP-UX'


# Generated at 2022-06-13 01:40:41.799472
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    module = AnsibleModule(argument_spec={})
    netstat_path = module.get_bin_path('netstat')
    if netstat_path is None:
        module.fail_json(msg="'netstat' command not found")
    rc, out, err = module.run_command("/usr/bin/netstat -niw")
    lines = out.splitlines()
    for line in lines:
        words = line.split()
        for i in range(len(words) - 1):
            if words[i][:3] == 'lan':
                device = words[i]
                interfaces = {device: {'device': device}}
                address = words[i + 3]
                interfaces[device]['ipv4'] = {'address': address}
                network = words[i + 2]

# Generated at 2022-06-13 01:40:47.726909
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    mock_module = MockModule('ansible.module_utils.facts.network.hpux.HPUXNetwork')
    generator = HPUXNetwork(mock_module)
    interfaces_info = generator.get_interfaces_info()
    assert type(interfaces_info) == dict
    assert interfaces_info is not None



# Generated at 2022-06-13 01:40:49.659548
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    network_fact_obj = HPUXNetwork({})
    print(network_fact_obj.populate())


# Generated at 2022-06-13 01:40:50.944489
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    collector = HPUXNetworkCollector()
    assert collector.platform == 'HP-UX'

# Generated at 2022-06-13 01:40:52.160620
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    nm = HPUXNetwork(dict(module=dict()), dict())
    assert nm

# Generated at 2022-06-13 01:41:13.737963
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    if not NetworkCollector._platforms['HP-UX']:
        return
    assert HPUXNetworkCollector()._platform == 'HP-UX'
    assert HPUXNetworkCollector()._fact_class == HPUXNetwork


# Generated at 2022-06-13 01:41:16.418760
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    module = AnsibleModule(argument_spec={})
    hpux_net = HPUXNetwork(module)
    assert hpux_net.module is module

# Unit tests for method get_default_interfaces()

# Generated at 2022-06-13 01:41:22.012990
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    my_module = AnsibleModule(argument_spec={}, supports_check_mode=True)

    netstat_path = my_module.get_bin_path('netstat')
    if netstat_path is None:
        my_module.fail_json(msg='netstat command not found.')
    else:
        hpu = HPUXNetwork()
        hpu.module = my_module
        interfaces = hpu.get_interfaces_info()
        assert len(interfaces) > 0

# Collect network facts

# Generated at 2022-06-13 01:41:32.084705
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    module = DummyModule()
    hpn = HPUXNetwork(module)
    hpn.get_default_interfaces = MagicMock(return_value={'default_interface': 'lan0',
                                                         'default_gateway': '172.16.105.1'})
    hpn.get_interfaces_info = MagicMock(return_value={'lan0': {'device': 'lan0',
                                                                'ipv4': {'address': '172.16.105.254',
                                                                         'network': '172.16.105.0'}}})
    fact_result = hpn.populate()

# Generated at 2022-06-13 01:41:34.057759
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    module = AnsibleModule(argument_spec={})
    hpn = HPUXNetwork(module)
    assert hpn.platform == 'HP-UX'



# Generated at 2022-06-13 01:41:41.857002
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    module = MockModule()
    hpnw = HPUXNetwork(module)
    rc = 0
    out1 = "Kernel Interface Table\n"
    out2 = "Destination           Gateway           Flags Refs Use  Interface\n"
    out3 = "default               10.82.104.254     UG    2    0  lan0\n"
    out = out1 + out2 + out3
    err = "Error\n"
    module.run_command.return_value = rc, out, err
    network_facts = hpnw.get_default_interfaces()
    assert network_facts['default_interface'] == 'lan0'
    assert network_facts['default_gateway'] == '10.82.104.254'



# Generated at 2022-06-13 01:41:48.056920
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    """
    Unit test for method get_interfaces_info of class HPUXNetwork
    """
    fake_module = AnsibleFakeModule()
    fake_module.run_command = lambda *a, **kw: (0,
                                                "lan0 lan0 00000000000395f0 UP 0 0 100 0\n"
                                                "lan1 lan1 00000000000395f0 UP 0 0 100 0\n", None)
    test_class = HPUXNetwork()
    test_class.module = fake_module
    interfaces = test_class.get_interfaces_info()
    assert interfaces['lan0']['device'] == 'lan0'
    assert interfaces['lan1']['device'] == 'lan1'
    assert interfaces['lan0']['ipv4']['address'] == '0'

# Generated at 2022-06-13 01:41:53.579890
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    module = AnsibleModule(
        argument_spec = dict()
    )
    ifaces = HPUXNetwork(module)
    default_interfaces = ifaces.get_default_interfaces()
    assert default_interfaces['default_interface'] == 'lan0'
    assert default_interfaces['default_gateway'] == '192.168.2.2'

# Unit test fo method get_interfaces_info of class HPUXNetwork

# Generated at 2022-06-13 01:42:04.443815
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    class FakeModule:
        def run_command(self, command):
            return (0, 'lan0: flags=1e080863,480<UP,BROADCAST,NOTRAILERS,RUNNING,SIMPLEX,MULTICAST,GROUPRT,64BIT> mtu 1500 index 1\n'
                         '        inet 10.200.199.166 netmask ff000000 broadcast 10.255.255.255\n'
                         'lan3: flags=1e080863,480<UP,BROADCAST,NOTRAILERS,RUNNING,SIMPLEX,MULTICAST,GROUPRT,64BIT> mtu 1500 index 1\n'
                         '        inet 10.200.199.165 netmask ff000000 broadcast 10.255.255.255\n', None)
    module = FakeModule()
   

# Generated at 2022-06-13 01:42:10.903512
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    import os
    import sys
    # Fix module path to import ansible properly
    sys.path = [os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, os.pardir)] + sys.path
    import ansible.module_utils.facts.network.hpux.hpux as hpux

    result = {
        'default': {'ipv4': {'interface': 'default', 'network': 'default', 'address': 'default'}},
        'lan0': {'ipv4': {'interface': 'lan0', 'network': '192.168.1.0', 'address': '192.168.1.42'}},
    }


# Generated at 2022-06-13 01:42:49.953086
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    hpu = HPUXNetwork()
    hpu.module = AnsibleModule(argument_spec={})
    hpu.get_default_interfaces()


# Generated at 2022-06-13 01:42:56.095725
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    """
    Input:
    Output:
    """
    module = AnsibleModule(argument_spec={})
    network = HPUXNetwork()
    # Test without netstat_path
    facts = network.populate()
    assert facts == {}

    # Test with netstat_path
    netstat_path = '/usr/bin/netstat'
    module.get_bin_path = MagicMock(return_value=netstat_path)

    # Test run_command
    module.run_command = MagicMock(return_value=(0, 'example', ''))
    network.module = module
    facts = network.populate()
    assert facts == {}

    # Test get_default_interfaces
    network.get_default_interfaces = MagicMock(return_value={})
    facts = network.populate()
   

# Generated at 2022-06-13 01:42:59.332095
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    collector = HPUXNetworkCollector()
    assert collector.platform == 'HP-UX'
    assert collector._fact_class == HPUXNetwork

# Generated at 2022-06-13 01:43:00.295276
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    hpux_network = HPUXNetwork()


# Generated at 2022-06-13 01:43:10.238772
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    module = AnsibleModule(argument_spec={})

# Generated at 2022-06-13 01:43:13.928625
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    module = AnsibleModule(
        argument_spec=dict(gather_subset=dict(default=['!all'], type='list'))
    )
    hpu = HPUXNetwork(module)
    module.exit_json(ansible_facts=dict(hpu=hpu.populate()))


# Generated at 2022-06-13 01:43:17.637819
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    hpu_network_obj = HPUXNetworkCollector()

    # check that it is instance of the class
    assert isinstance(hpu_network_obj, HPUXNetworkCollector)

    # check the value of platform
    assert hpu_network_obj._platform == 'HP-UX'

    # check that it is instance of the Network class
    assert issubclass(hpu_network_obj._fact_class, Network)

# Generated at 2022-06-13 01:43:19.312374
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    facts = HPUXNetwork()
    assert facts.platform == 'HP-UX'

# Generated at 2022-06-13 01:43:22.622712
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    module = None
    network_facts = HPUXNetwork(module).populate()
    print(network_facts)

if __name__ == '__main__':
    test_HPUXNetwork_populate()

# Generated at 2022-06-13 01:43:31.959710
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    # Test that get_interfaces_info does not fail
    out = """lan0: flags=0x8943<UP,BROADCAST,RUNNING,PROMISC,SIMPLEX,MULTICAST> mtu 1500
        index 2
        inet 192.168.1.1 netmask ffffff00 broadcast 192.168.1.255"""
    ifaces = {}
    lines = out.splitlines()
    for line in lines:
        words = line.split()
        for i in range(len(words) - 1):
            if words[i][:3] == 'lan':
                device = words[i]
                ifaces[device] = {'device': device}
                address = words[i + 3]
                ifaces[device]['ipv4'] = {'address': address}

# Generated at 2022-06-13 01:45:25.407099
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    from ansible.module_utils.facts import FactManager
    from ansible.module_utils.facts.network.hpux import HPUXNetwork
    from ansible.module_utils import basic

    module_mock = basic.AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True)

    module_mock.run_command = lambda x: (0, '', '')
    fact_manager = FactManager(module_mock, None, None)
    fact_manager.add_collector(HPUXNetworkCollector)
    facts_dict = fact_manager.collect(['network'], [])


# Generated at 2022-06-13 01:45:30.094506
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    module = FakeModule()
    network = HPUXNetwork(module)

    # Only netstat is expected to be called.
    # Using run_command method to avoid skip_on_facts method
    module.run_command = MagicMock(return_value=(0, "", ""))

    facts = network.populate()

    module.run_command.assert_called_once_with("/usr/bin/netstat -nr")


# Generated at 2022-06-13 01:45:34.825781
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    net = HPUXNetwork()
    interfaces_info = net.get_interfaces_info()
    assert interfaces_info['lan0'] == {'device': 'lan0',
                                       'ipv4': {'network': '172.20.0.0',
                                                'interface': 'lan0',
                                                'address': '172.20.0.1'}}

# Generated at 2022-06-13 01:45:39.114479
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    module = AnsibleModule(argument_spec={})
    module.run_command = MagicMock(return_value=(0, "default 0.0.0.0 UG  lan0", ""))
    network_facts = HPUXNetwork()
    network_facts.module = module
    result = network_facts.get_default_interfaces()
    assert result == {'default_gateway': '0.0.0.0', 'default_interface': 'lan0'}


# Generated at 2022-06-13 01:45:40.995931
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    hpux_network_instance = HPUXNetwork()
    assert type(hpux_network_instance) == HPUXNetwork



# Generated at 2022-06-13 01:45:47.316124
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    net_facts = HPUXNetwork()
    collected_facts = {'ansible_net_interfaces': ['lan2', 'lan1']}
    net_facts.populate(collected_facts)
    assert collected_facts['ansible_net_interfaces'] == ['lan2', 'lan1']


if __name__ == '__main__':
    # Unit test for method populate of class HPUXNetwork
    test_HPUXNetwork_populate()

# Generated at 2022-06-13 01:45:48.846396
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    net = HPUXNetwork(dict())
    print(net.populate())



# Generated at 2022-06-13 01:45:55.868787
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True)

    hw = HPUXNetwork(module)
    netstat_output = '''Kernel Interface table
Destination        Gateway          Flags   Refs     Use  If  Expire
default            some_IP          UG       0        0   lan1
10.30.0.0          lan1             UC       1        0   lan1
10.30.0.0          some_IP          UC       1        0   lan1
127.0.0.1          127.0.0.1        UH       1  8090517   lo0
'''
    interfaces = hw.get_default_interfaces()
    assert interfaces['default_interface'] == 'lan1'



# Generated at 2022-06-13 01:46:05.962500
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True)
    # Instantiate HPUXNetwork class
    hpux_network = HPUXNetwork(module=module)
    # Execute populate method
    hpux_network.populate()
    assert hpux_network.facts['default_interface'] == 'lan9'
    assert hpux_network.facts['default_gateway'] == '172.16.1.1'
    assert 'default_interface' in hpux_network.facts
    assert 'default_gateway' in hpux_network.facts
    assert 'interfaces' in hpux_network.facts
    assert hpux_network.facts['interfaces'] == ['lan9']
    assert 'lan9' in hpux_network.facts

# Generated at 2022-06-13 01:46:08.002594
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    c = HPUXNetworkCollector()
    assert c.platform == "HP-UX"
    assert c._fact_class == HPUXNetwork