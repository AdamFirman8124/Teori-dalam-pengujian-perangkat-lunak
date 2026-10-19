

# Generated at 2022-06-13 01:37:49.799833
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    nc = HPUXNetworkCollector()
    assert nc.__class__.__name__ == 'HPUXNetworkCollector'



# Generated at 2022-06-13 01:37:51.406577
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    HPUX = HPUXNetwork()

# Generated at 2022-06-13 01:38:01.836775
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    HPUXNetwork = HPUXNetwork()

    class MockModule(object):
        def get_bin_path(self, name):
            if name == "netstat":
                return 'netstat'
            else:
                return '/nopath/{}'.format(name)
        run_command = HPUXNetwork.run_command
    HPUXNetwork.module = MockModule()

    HPUXNetwork.populate()

    # test default values in the absence of data
    assert not HPUXNetwork.facts['default_interface']
    assert not HPUXNetwork.facts['default_gateway']
    assert not HPUXNetwork.facts['interfaces']
    assert not HPUXNetwork.facts['lan0']
    print("on empty data: \n\t{}".format(HPUXNetwork.facts))

    #

# Generated at 2022-06-13 01:38:06.883636
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=False)
    network = HPUXNetwork(module)
    default_interfaces = network.get_default_interfaces()
    assert 'default_interface' in default_interfaces
    assert 'default_gateway' in default_interfaces

# Generated at 2022-06-13 01:38:11.280206
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    """Fail if required methods are not implemented."""
    hpux_network = HPUXNetwork()
    methods = ['get_default_interfaces', 'get_interfaces_info']
    for method in methods:
        assert hasattr(hpux_network, method), 'method %r not implemented' % method

# Generated at 2022-06-13 01:38:15.194965
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    module = AnsibleModule(
        argument_spec=dict(gather_subset=dict(default=['!all'], type='list'))
    )

    ifaces = HPUXNetwork(module)
    all_iface_names = [iface for iface in ifaces.interfaces.keys()
                       if not iface.startswith('lo')]

    module.exit_json(
        ansible_facts={
            'ansible_network_resources': ifaces.populate()
        }
    )



# Generated at 2022-06-13 01:38:25.760947
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    m = AnsibleModule(argument_spec=dict())
    network = HPUXNetwork(m)
    network.module.run_command = MagicMock(return_value=(0, '\n', ''))
    network.get_default_interfaces = MagicMock(return_value={'default_interface': 'lan0', 'default_gateway': '192.168.1.1'})
    network.get_interfaces_info = MagicMock(return_value={'lan0': {'device': 'lan0', 'ipv4': {'address': '192.168.1.111'}}})
    network.populate()
    assert network.facts['default_interface'] == 'lan0'
    assert network.facts['default_gateway'] == '192.168.1.1'

# Generated at 2022-06-13 01:38:33.436564
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    n = HPUXNetwork()

    # Creating a mock of method module.run_command

# Generated at 2022-06-13 01:38:43.571807
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    # Create instance of HPUXNetwork
    hpuxnet = HPUXNetwork()

    hpuxnet.module.get_bin_path = mock_get_bin_path
    hpuxnet.module.run_command = mock_run_command

    # Invoke method populate of HPUXNetwork
    hpuxnet.populate()

    assert hpuxnet.facts['default_gateway'] == '172.16.1.1'
    assert hpuxnet.facts['default_interface'] == 'lan0'
    assert hpuxnet.facts['interfaces'] == ['lan2', 'lan3', 'lan0']
    assert hpuxnet.facts['lan2']['ipv4']['address'] == '172.16.1.32'

# Generated at 2022-06-13 01:38:44.806829
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    network_instance = HPUXNetwork()
    assert network_instance.platform == 'HP-UX'


# Generated at 2022-06-13 01:38:51.044364
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    network = HPUXNetwork()
    assert network is not None

# Generated at 2022-06-13 01:38:54.179264
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    """
    Test class HPUXNetwork
    """
    hpu_net = HPUXNetwork(None)
    assert hpu_net.platform == 'HP-UX'

# Generated at 2022-06-13 01:39:05.231548
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    hpu_network_obj = HPUXNetwork()
    hpu_network_obj.module.run_command = run_command_mock
    hpu_network_obj.get_interfaces_info = get_interfaces_info_mock
    hpu_network_obj.get_default_interfaces = get_default_interfaces_mock
    network_facts = hpu_network_obj.populate()

# Generated at 2022-06-13 01:39:06.561236
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    assert(HPUXNetwork().populate() is not None)

# Generated at 2022-06-13 01:39:16.849849
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    module = FakeAnsibleModule()
    net = HPUXNetwork(module)
    net.populate()
    assert module.params['gather_subset'] == ['!all', 'network']
    assert net.platform == 'HP-UX'
    assert net.default_gateway == '172.16.29.254'
    assert net.default_interface == 'lan1'
    assert net.interfaces == ['lan1']
    assert net.lan1.device == 'lan1'
    assert net.lan1.ipv4.address == '172.16.29.200'
    assert net.lan1.ipv4.interface == 'lan1'
    assert net.lan1.ipv4.network == '172.16.29.0'


# Generated at 2022-06-13 01:39:25.610710
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    from ansible.module_utils.facts import collector

    module = AnsibleModuleMock()
    module.run_command.return_value = (0,
                                       "default 192.0.2.1          UG        0 0        0 lan0\n"
                                       "192.0.2.0        192.0.2.1          U         0 0        0 lan0",
                                       None)
    module.get_bin_path.return_value = "/bin"

    fact_collector = collector.get_collector("HPUXNetworkCollector")
    my_network = fact_collector.collect(module=module)

    assert my_network.get('default_interface') == 'lan0'
    assert my_network.get('default_gateway') == '192.0.2.1'

# Generated at 2022-06-13 01:39:32.798637
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    test_class = HPUXNetwork(None)
    test_out_1 = "lan0    link#1  UP  7000   0.0.0.0\n" \
                 "lan1    link#2  UP  7000   0.0.0.0\n" \
                 "lan2    link#3  UP  7000   0.0.0.0"
    assert test_class._get_interfaces_info(test_out_1) == \
           {'lan0': {'device': 'lan0'},
            'lan1': {'device': 'lan1'},
            'lan2': {'device': 'lan2'}}

# Generated at 2022-06-13 01:39:35.764687
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    hn = HPUXNetworkCollector()
    assert HPUXNetworkCollector._platform == 'HP-UX'
    assert isinstance(hn.get_network_facts(), dict)

# Generated at 2022-06-13 01:39:41.779610
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    hn = HPUXNetwork()

    out = """
lan0       Link encap:Local Loopback
          inet addr:127.0.0.1  Mask:255.0.0.0
          UP LOOPBACK RUNNING  MTU:8232  Metric:1
          RX packets:305 errors:0 dropped:0 overruns:0 frame:0
          TX packets:305 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0
          RX bytes:26668 (25.9 Kb)  TX bytes:26668 (25.9 Kb)"""

    interfaces = hn.get_interfaces_info(out)
    assert interfaces['lan0']['ipv4']['address'] == '127.0.0.1'

# Generated at 2022-06-13 01:39:45.503085
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    from ansible.module_utils.facts.network.hpux import HPUXNetwork
    interfaces = HPUXNetwork().get_interfaces_info()
    assert interfaces
    assert len(interfaces) >= 1
    for interface in interfaces:
        assert 'device' in interfaces[interface]
        assert 'ipv4' in interfaces[interface]



# Generated at 2022-06-13 01:39:59.611973
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    """ This method unit test the get_default_interfaces
    of HPUXNetwork class
    """
    from ansible.module_utils.facts.network.hpux.netstat import HPUXNetwork
    from ansible.module_utils.facts.network.hpux.netstat import PytestModule
    from ansible.module_utils.facts.network.hpux.netstat import PytestCommand
    test_hpux_network = HPUXNetwork(PytestModule())
    expected_result = {'default_gateway': '192.168.1.1',
                       'default_interface': 'lan0'}
    netstat_path = "/usr/bin/netstat"
    cmd = netstat_path + " -nr"
    result = test_hpux_network.get_default_interfaces()
    assert result == expected_

# Generated at 2022-06-13 01:40:01.900813
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    network = HPUXNetwork({})
    assert network.populate() is not None


# Generated at 2022-06-13 01:40:06.731063
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    h1 = HPUXNetwork()
    default_interfaces_dict = h1.get_default_interfaces()
    assert default_interfaces_dict['default_interface'] == 'lan1'
    assert default_interfaces_dict['default_gateway'] == '192.168.0.1'


# Generated at 2022-06-13 01:40:08.283894
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    result = {'default_interface': 'lan17',
              'default_gateway': '1.1.1.1'}
    m = HPUXNetwork()
    assert result == m.get_default_interfaces()



# Generated at 2022-06-13 01:40:13.455464
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    module = None
    hpux_network_obj = HPUXNetwork(module)
    hpux_network_dict_obj = hpux_network_obj.populate()
    assert 'interfaces' in hpux_network_dict_obj
    assert 'default_interface' in hpux_network_dict_obj
    assert 'default_gateway' in hpux_network_dict_obj
    assert hpux_network_dict_obj['default_interface'] == 'lan0'



# Generated at 2022-06-13 01:40:24.354420
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    net_module_mock = network_module_mock()
    net_module_mock.run_command = run_command_mock
    net_module_mock.get_bin_path = get_bin_path_mock
    network_facts = HPUXNetwork()
    network_facts.module = net_module_mock
    network_facts.populate()
    facts = network_facts.get_facts()
    assert facts['default_interface'] == "lan0"
    assert facts['default_gateway'] == "192.0.2.1"
    assert facts['interfaces'] == ['lan0']
    assert facts['lan0']['device'] == "lan0"
    assert facts['lan0']['ipv4']['address'] == "192.0.2.10"
    assert facts

# Generated at 2022-06-13 01:40:34.733482
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.network.hpux import HPUXNetwork
    from ansible.module_utils.facts.network.hpux import HPUXNetworkCollector
    m1 = HPUXNetworkCollector()
    m1.default_interfaces_path = 'test/unit/test_facts/test_network_hpux/default_interfaces.out'
    m1.interfaces_path = 'test/unit/test_facts/test_network_hpux/interfaces.out'
    m1._read_file = lambda path: open(path).read().strip()
    m1.module = BaseFactCollector()

    m2 = HPUXNetwork()
   

# Generated at 2022-06-13 01:40:43.653421
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    mock_module = Mock(run_command=Mock())
    hpux_network = HPUXNetwork(mock_module)
    mock_module.run_command = Mock(return_value=(0, "default 127.0.0.0 UG lan0 ", ""))
    expected = {'default_interface': 'lan0', 'default_gateway': '127.0.0.0'}
    assert hpux_network.get_default_interfaces() == expected

    mock_module.run_command = Mock(return_value=(0, "predefined lan0 192.168.0.0 192.168.0.4 U ", ""))

# Generated at 2022-06-13 01:40:46.360421
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    module = FakeAnsibleModule()
    ifaces = HPUXNetwork(module)
    interfaces = ifaces.get_default_interfaces()
    assert('default_interface' in interfaces)
    assert(interfaces['default_interface'] == 'lan3')
    assert('default_gateway' in interfaces)
    assert(interfaces['default_gateway'] == '10.0.0.1')


# Generated at 2022-06-13 01:40:49.444017
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    module = FakeModule()
    network = HPUXNetwork(module)
    facts = network.populate()
    assert 'default_interface' in facts
    assert 'default_gateway' in facts
    assert 'interfaces' in facts


# Generated at 2022-06-13 01:41:11.049409
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )

    def _exit_json(changed=False, ansible_facts=None):
        if not isinstance(ansible_facts, dict):
            module.fail_json(msg='ansible_facts must be a dictionary')
        module.exit_json(changed=changed, ansible_facts=ansible_facts)

    def _run_command(command):
        command = command.replace('/usr/bin/netstat', 'test/netstat')
        if command[-1] == 'w':
            return (0, 'lan0      link#1        UP   1000   0x1000 09:00:43:E7:E8:D8', '')

# Generated at 2022-06-13 01:41:14.344707
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    hn = HPUXNetwork({}, {}, {})
    assert hn.get_default_interfaces() == {}
    assert hn.get_interfaces_info() == {}
    assert hn.populate() == {}


# Generated at 2022-06-13 01:41:22.578954
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    import ansible.module_utils.facts.network.hpux
    from ansible.module_utils.facts.network.base import Network as NetworkBase
    from ansible.module_utils.facts.network.hpux import (
        HPUXNetwork as HPUXNetworkClass
    )
    from ansible.module_utils.facts.network.hpux import (
        HPUXNetworkCollector as HPUXNetworkCollectorClass
    )

    # the following lines are used only to make the module work on python2
    from ansible.module_utils import basic
    from ansible.module_utils.facts.network.base import Network as NetworkBase
    if not hasattr(basic, 'AnsibleModule'):
        basic.AnsibleModule = basic.AnsibleModule_class

    # testing network populate method
    network_collector

# Generated at 2022-06-13 01:41:24.705149
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    assert HPUXNetwork(MockModule()) is not None


# TODO Unit tests for the methods



# Generated at 2022-06-13 01:41:33.806013
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    from ansible_collections.ansible.netcommon.tests.unit.compat import unittest
    from ansible_collections.ansible.netcommon.tests.unit.compat.mock import patch

    class TestHPUXNetwork(unittest.TestCase):

        def setUp(self):
            self.mock_module = patch('ansible.module_utils.facts.network.hpux.HPUXNetwork.module')
            self.mock_module.start()
            self.addCleanup(self.mock_module.stop)

            self.hpux_network = HPUXNetwork()

        def tearDown(self):
            pass


# Generated at 2022-06-13 01:41:41.916158
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    """
    This test checks following facts:
        - default_interface
        - default_gateway
        - interfaces
        - ipv4.network
        - ipv4.address
    """
    module_mock = Mock(run_command=Mock(return_value=(0, out, err)))
    network_facts_obj = HPUXNetwork(module=module_mock)
    network_facts = network_facts_obj.populate()

    assert network_facts['default_interface'] == 'lan0'
    assert network_facts['default_gateway'] == '10.0.0.1'
    assert 'interfaces' in network_facts
    assert 'lan0' in network_facts['interfaces']

# Generated at 2022-06-13 01:41:44.050936
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    collector = HPUXNetworkCollector()
    assert collector.platform == 'HP-UX'
    assert collector._fact_class == HPUXNetwork
    assert collector._platform == 'HP-UX'

# Generated at 2022-06-13 01:41:45.066077
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    obj = HPUXNetworkCollector()
    assert isinstance(obj, NetworkCollector)

# Generated at 2022-06-13 01:41:53.407029
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    from ansible.module_utils.facts.network.hpux import HPUXNetwork
    from ansible.module_utils.facts.collector import TestModule
    interfaces = {}
    testmodule = TestModule(module_path="ansible/module_utils/facts/network/hpux")
    testnetwork = HPUXNetwork()
    testnetwork.module = testmodule
    testnetwork.get_interfaces_info()
    interfaces = testnetwork.get_interfaces_info()

    assert len(interfaces) > 0
    assert interfaces.get("lan0") is not None
    assert interfaces.get("lan1") is None

# Generated at 2022-06-13 01:41:57.958953
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    interfaces = {
        'lan0':
            {
                'device': 'lan0',
                'ipv4':
                    {
                        'interface': 'lan0',
                        'network': '10.5.5.0/24',
                        'address': '10.5.5.1'
                    }
            },
        'lan1':
            {
                'device': 'lan1',
                'ipv4':
                    {
                        'interface': 'lan1',
                        'network': '10.4.4.0/24',
                        'address': '10.4.4.1'
                    }
            }
    }

    hpu = HPUXNetwork()
    result = hpu.get_interfaces_info()

    assert result == interfaces


# Generated at 2022-06-13 01:42:13.424224
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    """
    Test constructor of class HPUXNetworkCollector
    Expected result:
    - return a HPUXNetworkCollector object
    """
    # Default network collector for HP-UX
    nc1 = HPUXNetworkCollector()
    assert isinstance(nc1, HPUXNetworkCollector)

# Generated at 2022-06-13 01:42:23.928982
# Unit test for method get_interfaces_info of class HPUXNetwork

# Generated at 2022-06-13 01:42:25.626873
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    hpx_net = HPUXNetworkCollector()
    assert hpx_net is not None

# Generated at 2022-06-13 01:42:27.831016
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    hpux = HPUXNetworkCollector()
    assert hpux.platform == 'HP-UX'
    assert hpux._fact_class.platform == 'HP-UX'


# Generated at 2022-06-13 01:42:30.623332
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    network = HPUXNetwork({})
    interfaces = network.get_interfaces_info()
    assert 'lan0' in interfaces.keys()
    lan0 = interfaces['lan0']
    assert lan0['ipv4']['address'] == '192.168.140.132'

# Generated at 2022-06-13 01:42:40.846669
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    network = HPUXNetwork()
    network.module.get_bin_path = lambda x: "/bin/true"
    network.module.run_command = lambda x: (0, "default default_gateway default_interface", None)
    network.module.run_command = lambda x: (0, "lan0 lan0_network lan0_address", None)
    network_facts = network.populate()

# Generated at 2022-06-13 01:42:44.619904
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    collector = HPUXNetworkCollector()
    assert collector.fact_class == HPUXNetwork


# Generated at 2022-06-13 01:42:46.574349
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    collector = HPUXNetworkCollector('HPUX')
    assert collector._fact_class._platform == 'HP-UX'

# Generated at 2022-06-13 01:42:54.686490
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    mod = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True)

    result = {}
    net_ins = HPUXNetwork(mod)
    result = net_ins.populate()

    default_interface = 'lan0'
    default_gateway = '172.17.4.1'
    interfaces = ['lan0']
    interface_info = {'lan0': {'device': 'lan0', 'ipv4': {'address': '172.17.4.117', 'network': '172.17.4.0', 'interface': 'lan0'}}}

    assert result['default_interface'] == default_interface
    assert result['default_gateway'] == default_gateway
    assert result['interfaces'] == interfaces
    assert result['lan0'] == interface_info['lan0']

# Generated at 2022-06-13 01:42:58.171603
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    module = AnsibleModule({})
    network_collector = HPUXNetworkCollector(module)
    assert network_collector._platform == 'HP-UX'


# Generated at 2022-06-13 01:43:21.278994
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    net = HPUXNetwork()
    assert net.platform == 'HP-UX'

# Generated at 2022-06-13 01:43:29.372863
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    module = AnsibleModule(argument_spec={'filter': {}})

    m_get_bin_path = MagicMock(return_value='/usr/bin/netstat')
    module.get_bin_path = m_get_bin_path

    m_run_command = MagicMock(return_value=(0, 'default 192.168.1.1 UGS ptl0', ''))
    module.run_command = m_run_command

    network_collector = HPUXNetworkCollector(module)
    network = network_collector.get_device()
    results = network.get_default_interfaces()

    assert results == {'default_interface': 'ptl0', 'default_gateway': '192.168.1.1'}



# Generated at 2022-06-13 01:43:35.816968
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    net = HPUXNetwork()
    net.module = MagicMock()
    # Mock module run_command method
    net.module.run_command.return_value = ('default 192.168.1.1'
                                           '      UGSc      5  0    '
                                           'lan0', 'out', 'error')
    result = net.get_default_interfaces()
    assert result['default_interface'] == 'lan0'
    assert result['default_gateway'] == '192.168.1.1'


# Generated at 2022-06-13 01:43:39.988160
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    """Test to see that we create an HPUXNetwork object as expected"""
    m = HPUXNetwork()
    assert isinstance(m, HPUXNetwork)
    assert m.platform == "HP-UX"



# Generated at 2022-06-13 01:43:51.355317
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    expected = {'lan0': {'device': 'lan0',
                         'ipv4': {'address': '10.0.0.0',
                                  'interface': 'lan0',
                                  'network': '10.0.0.0'}},
                'lan1': {'device': 'lan1',
                         'ipv4': {'address': '10.0.0.1',
                                  'interface': 'lan1',
                                  'network': '10.0.1.0'}}}

# Generated at 2022-06-13 01:43:56.687307
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    module = MockModule()
    network = HPUXNetwork(module)

    netstat_path = module.get_bin_path('netstat')
    module.run_command.return_value = ('', 'fake_out', '')
    default_interfaces = {'default_interface': 'lan0',
                          'default_gateway': '172.16.1.1'}
    interfaces = {'lan10': {'device': 'lan10', 'ipv4': {'address': '172.16.1.10',
                                                       'network': '172.16.1.<0-252>',
                                                       'interface': 'lan10',
                                                       'address': '172.16.1.10'}}}
    network.get_default_interfaces = Mock(return_value=default_interfaces)
    network

# Generated at 2022-06-13 01:43:58.402039
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    network = HPUXNetwork()
    assert network.platform == 'HP-UX'



# Generated at 2022-06-13 01:44:01.931005
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    obj = HPUXNetworkCollector()
    assert obj.platform == 'HP-UX'
    assert obj._fact_class == HPUXNetwork
    assert obj._platform == 'HP-UX'


# Generated at 2022-06-13 01:44:02.773839
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    HPUXNetworkCollector()

# Generated at 2022-06-13 01:44:11.865827
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    hpux_network = HPUXNetwork()
    module = MockModule()
    hpux_network.module = module
    facts = hpux_network.populate()
    assert facts['default_interface'] == 'lan1'
    assert facts['default_gateway'] == '10.10.10.254'
    assert len(facts['interfaces']) == 4
    assert facts['lan1']['ipv4']['address'] == '10.10.10.11'
    assert facts['lan1']['ipv4']['network'] == '10.10.10.0'
    assert facts['lan1']['ipv4']['interface'] == 'lan1'
    assert facts['lan1']['device'] == 'lan1'


# Generated at 2022-06-13 01:45:17.841634
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    """
    This test class uses a mock module to simulate module input parameters,
    and also mocks AnsibleModule to simulate AnsibleModule object.
    """
    from ansible.module_utils import facts
    from ansible.module_utils.facts import network
    from ansible.module_utils.facts.network.hpux import HPUXNetwork
    from ansible.module_utils.facts.network.hpux import HPUXNetworkCollector
    from ansible.module_utils.facts.network.hpux import test_HPUXNetwork_populate
    from ansible.module_utils.six import StringIO
    from ansible.module_utils.six.moves import reload_module
    from ansible.module_utils._text import to_bytes
    import ansible.module_utils.facts.network.hpux

# Generated at 2022-06-13 01:45:29.024357
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    module = ansible_module_hpux_network_facts
    n = HPUXNetwork(module)
    facts = n.populate()
    assert facts['default_interface'] == 'lan0'
    assert facts['default_gateway'] == '10.76.33.254'
    assert facts['interfaces'] == ['lan1', 'lan0']
    assert facts['lan1']['ipv4']['address'] == '172.17.121.17'
    assert facts['lan1']['ipv4']['network'] == '172.17.121.0'
    assert facts['lan1']['ipv4']['interface'] == 'lan1'
    assert facts['lan0']['ipv4']['address'] == '10.76.33.17'

# Generated at 2022-06-13 01:45:37.618131
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    class TestModule(object):
        def __init__(self):
            self.run_command_responses = list()
            self.run_command_responses.append(('0', 'Mtu        Address          Ipkts Ierrs   Opkts Oerrs Collis Queue', ''))
            self.run_command_responses.append(('0', '1500        lan0              1025     0     860     0   0    0', ''))
            self.run_command_responses.append(('0', '1500        lan0              1025     0     860     0   0    0', ''))

        def run_command(self, cmd, check_rc=True):
            return self.run_command_responses.pop(0)

    test_module = TestModule()

# Generated at 2022-06-13 01:45:40.037305
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    module = AnsibleModule(argument_spec={})
    mod = HPUXNetwork(module=module)
    default_interfaces = mod.get_default_interfaces()
    assert default_interfaces['default_gateway'].startswith("192.168")


# Generated at 2022-06-13 01:45:41.425666
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    h = HPUXNetwork()
    assert h is not None


# Generated at 2022-06-13 01:45:45.681079
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    obj = HPUXNetworkCollector(None)
    assert isinstance(obj, NetworkCollector)
    assert isinstance(obj.network, HPUXNetwork)
    assert obj._fact_class is HPUXNetwork
    assert obj._platform == 'HP-UX'

# Generated at 2022-06-13 01:45:47.930062
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    collector = HPUXNetworkCollector()
    assert collector.platform == 'HP-UX'
    assert collector._fact_class is HPUXNetwork


# Generated at 2022-06-13 01:45:55.458040
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    facts = HPUXNetworkCollector.collect(None)
    assert facts['default_interface'] == 'lan0'
    assert facts['default_gateway'] == '10.76.24.1'
    assert facts['interfaces'] == ['lan0', 'lan1']
    fact = 'lan0'
    assert facts[fact]['device'] == 'lan0'
    assert facts[fact]['ipv4'] == {'address': '10.76.24.51',
                                   'network': '10.76.24.0',
                                   'interface': 'lan0',
                                   'address': '10.76.24.51'}
    fact = 'lan1'
    assert facts[fact]['device'] == 'lan1'

# Generated at 2022-06-13 01:45:59.812705
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    net = HPUXNetwork()
    default_interfaces_facts = net.get_default_interfaces()
    assert default_interfaces_facts['default_interface'] == 'lan0'
    assert default_interfaces_facts['default_gateway'] == '10.0.0.1'


# Generated at 2022-06-13 01:46:05.532342
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    network = HPUXNetwork()
    interfaces = network.get_interfaces_info()
    assert len(interfaces) > 0, "No interfaces found."
    for iface in interfaces:
        assert len(interfaces[iface]['ipv4']['address']) > 0, "No address found."
        assert len(interfaces[iface]['ipv4']['network']) > 0, "No network found."
