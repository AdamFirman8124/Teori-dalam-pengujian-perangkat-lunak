

# Generated at 2022-06-13 01:37:54.693157
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    m = AnsibleModule(argument_spec={}, supports_check_mode=True)
    test_obj = HPUXNetwork(m)

    fake_out = '''
Name          Mtu   Network   Address            Ipkts     Ierrs     Opkts     Oerrs  Coll  Queue
lan2          1500  192.168.1.0   192.168.1.118  34173930   84975  13651136  236078    0    0
lan0          1500  10.10.10.0   10.10.10.3  14355734   90789  13651136  236078    0    0
lo            8232         127.0.0.0         127.0.0.1   239736        0   239736        0    0    0
'''


# Generated at 2022-06-13 01:38:05.525438
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    hpux_network = HPUXNetwork(None)

    def get_bin_path_mock(name):
        return "/usr/bin/netstat"

    hpux_network.module.get_bin_path = get_bin_path_mock


# Generated at 2022-06-13 01:38:08.467318
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    obj = HPUXNetworkCollector()
    assert obj._fact_class == HPUXNetwork
    assert obj._platform == 'HP-UX'

# Generated at 2022-06-13 01:38:14.392581
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    fact_network = HPUXNetworkCollector()
    assert "interface_" == fact_network._interface_prefix
    assert "HP-UX" == fact_network._fact_class.platform
    assert "HP-UX" == fact_network._platform
    assert "default_interface" == fact_network._default_interface_fact[0]
    assert "default_gateway" == fact_network._default_interface_fact[1]
    assert "interfaces" == fact_network._interfaces_fact
    assert __name__ == fact_network.__module__

# Generated at 2022-06-13 01:38:16.280409
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    module = HPUXNetwork()
    assert module is not None


# Generated at 2022-06-13 01:38:26.706121
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    """Unit test for method populate of class HPUXNetwork."""
    test_instance = HPUXNetwork(dict(), dict())
    test_instance.module.run_command = lambda args: [0, 'default xxxx xxxx lan0',
                                                     '0.0.0.0 xxx.xxx.xxx.0 lan1']
    network_facts = test_instance.populate()
    assert 'default_interface' in network_facts
    assert network_facts['default_interface'] == 'lan0'
    assert 'default_gateway' in network_facts
    assert network_facts['default_gateway'] == 'xxxx'
    assert 'interfaces' in network_facts
    assert 'lan0' in network_facts['interfaces']
    assert 'lan1' in network_facts['interfaces']

# Generated at 2022-06-13 01:38:34.052652
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    class DummyModule():
        def __init__(self):
            self.params = {
                'gather_subset': 'all',
                'gather_network_resources': 'all'
            }


# Generated at 2022-06-13 01:38:43.711137
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    netmod = Network()
    netstat_path = netmod.get_bin_path('netstat')
    if netstat_path is None:
        return False
    netmod.run_command = lambda x: (0, '', '')
    netmod.get_bin_path = lambda x: '/usr/bin/netstat'
    netmod.get_interfaces_info = lambda: {'lan0': {'device': 'lan0'}, 'lan1': {'device': 'lan1'}}
    netmod.get_default_interfaces = lambda: {'default_interface': 'lan1', 'default_gateway': '10.20.30.1'}
    net_facts = {}
    net_facts = netmod.populate()

# Generated at 2022-06-13 01:38:46.651230
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    module = AnsibleModule(argument_spec={})
    network_facts = HPUXNetwork(module)
    # The platform is HP-UX
    assert network_facts.platform == 'HP-UX'
    # The method populate is defined
    assert hasattr(network_facts, 'populate')
    # The result of populate method is not empty
    assert network_facts.populate()

# Generated at 2022-06-13 01:38:48.429873
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    m = HPUXNetwork()
    assert m.populate()['interfaces'] == ['lan0']

# Generated at 2022-06-13 01:38:59.424625
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    """Unit test for method populate of class HPUXNetwork"""
    network = HPUXNetwork()
    network.module = MockModule()
    collected_facts = {'default_gateway': '10.1.1.1',
                       'default_interface': 'lan1',
                       'interfaces': ['lan0', 'lan1']}

    network_facts = network.populate()
    assert network_facts == collected_facts

# Generated at 2022-06-13 01:39:03.373856
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    collector = HPUXNetworkCollector()
    ansible_module_mock = MockAnsibleModule()
    collector._module = ansible_module_mock
    try:
        collector.collect()
    except:
        assert False, "Failing while collecting facts"

# Generated at 2022-06-13 01:39:05.603856
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    obj = HPUXNetworkCollector()
    assert obj.platform == 'HP-UX'
    assert obj._fact_class == HPUXNetwork

# Generated at 2022-06-13 01:39:12.830095
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    from ansible.module_utils.facts.network.base import Network
    from ansible.module_utils.facts.network import hpux

    module = hpux.HPUXNetwork
    module.run_command = mock_run_command

    interfaces = module().get_interfaces_info()
    assert 'lan0' in interfaces.keys()
    assert interfaces['lan0']['ipv4']['address'] == '10.1.1.1'
# End unit test for method get_interfaces_info of class HPUXNetwork


# Generated at 2022-06-13 01:39:21.954149
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    from ansible_collections.ansible.community.tests.unit.compat.mock import patch
    from ansible_collections.ansible.community.plugins.module_utils.facts.network.hp_ux.network import HPUXNetwork
    mock_module = patch('ansible_collections.ansible.community.tests.unit.modules.utils.get_module').start()
    mock_module.return_value = mock_module
    # Initialize the class and assign it to a local variable
    hp_ux_network = HPUXNetwork()
    # Assert that the class contains the following parameters
    assert hp_ux_network.platform == 'HP-UX'

# Generated at 2022-06-13 01:39:29.053389
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    module = AnsibleModule(argument_spec={})

    network_module = HPUXNetwork(module)

    assert network_module is not None

    assert network_module.platform == 'HP-UX'

    # Test get_interfaces_info() method
    rc, out, err = module.run_command("/usr/bin/netstat -niw")
    lines = out.splitlines()
    interfaces = {}
    for line in lines:
        words = line.split()
        for i in range(len(words) - 1):
            if words[i][:3] == 'lan':
                device = words[i]
                interfaces[device] = {'device': device}
                address = words[i + 3]
                interfaces[device]['ipv4'] = {'address': address}

# Generated at 2022-06-13 01:39:30.969235
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    module = MockModule(name='hpnw')
    hpnw = HPUXNetwork(module)
    assert hpnw
    assert hpnw.module == module



# Generated at 2022-06-13 01:39:35.062301
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    """
    Unit test for method get_interfaces_info of class HPUXNetwork
    """
    module = MockModule()
    hp_ux_network = HPUXNetwork(module)
    assert hp_ux_network.get_interfaces_info() == {'lan0': {'device': 'lan0',
                                                            'ipv4': {'address': '192.168.0.2'}}}



# Generated at 2022-06-13 01:39:36.469000
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    network = HPUXNetwork({})
    interfaces = network.get_interfaces_info()
    assert interfaces is not None

# Generated at 2022-06-13 01:39:37.717792
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    nc = HPUXNetworkCollector()
    assert nc._platform == 'HP-UX'

# Generated at 2022-06-13 01:39:50.172957
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    module = MockModule()
    net = HPUXNetwork(module)
    default_interfaces = net.get_default_interfaces()
    assert default_interfaces == {'default_interface': 'lan0',
                                  'default_gateway': '172.17.0.1'}



# Generated at 2022-06-13 01:39:59.541514
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    test_module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )

    ###########################################################################
    # Mock the module parameters and results of calls to external programs
    ###########################################################################

# Generated at 2022-06-13 01:40:10.570782
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    sample_output = """
Routing Information for "lan0"
Destination          Gateway           Flags   Refs     Use  If  Mtu  Window  IRTT
default              10.0.2.2         UG      0         0   lan0  -  16384  0
10.0.2.0           10.0.2.2          US      0         0   lan0  -  16384  0
10.0.2.2           127.0.0.1        UH      0         0  lo0    -  16384  0
127.0.0.1          127.0.0.1        UH      0         0  lo0    -  16384  0
"""
    expected_result = {'default_interface': 'lan0', 'default_gateway': '10.0.2.2'}
   

# Generated at 2022-06-13 01:40:13.246131
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    devices = HPUXNetwork().get_interfaces_info()
    assert(isinstance(devices, dict))
    assert('lan0' in devices)
    assert(isinstance(devices['lan0'], dict))


# Generated at 2022-06-13 01:40:16.228501
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    network = HPUXNetwork()
    default_interfaces = network.get_default_interfaces()
    assert default_interfaces['default_interface'] == 'lan0'
    assert default_interfaces['default_gateway'] == '10.41.128.1'


# Generated at 2022-06-13 01:40:17.889408
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    mod = AnsibleModule(argument_spec={})
    obj = HPUXNetwork(mod)
    obj.get_default_interfaces()

# Generated at 2022-06-13 01:40:24.916249
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    # Setup the class to test
    hn = HPUXNetwork()
    hn.module.run_command = lambda cmd: ('', 'default 192.168.1.1 UGS lan0', '')

    default_interfaces = hn.get_default_interfaces()
    assert default_interfaces['default_interface'] == 'lan0'
    assert default_interfaces['default_gateway'] == '192.168.1.1'



# Generated at 2022-06-13 01:40:33.633173
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    module = HPUXNetwork()
    out = [
        "default 192.168.1.1 UGS 1833 0 lan826",
        "192.168.1.0 192.168.1.1 UGS 1771 0 lan826",
    ]
    module.module = type('FakeModule', (object,), {'run_command': lambda x: (
        0, '\n'.join(out), '')})
    interface_facts = module.get_default_interfaces()
    assert interface_facts['default_interface'] == 'lan826'
    assert interface_facts['default_gateway'] == '192.168.1.1'



# Generated at 2022-06-13 01:40:40.574345
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    mock_module = MockModule()
    mock_module.run_command = Mock(return_value=(0, 'default 192.168.1.1 UGS 1 0 0 lan4\n', None))
    mock_network = HPUXNetwork(mock_module)
    mock_default_interfaces = mock_network.get_default_interfaces()
    assert mock_default_interfaces['default_interface'] == 'lan4'
    assert mock_default_interfaces['default_gateway'] == '192.168.1.1'



# Generated at 2022-06-13 01:40:51.020524
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    net_facts = HPUXNetwork()
    net_facts.module.run_command = lambda x: (0, '', '')
    net_facts.module.get_bin_path = lambda x: '/usr/bin/netstat'
    net_facts.get_default_interfaces = lambda: {'default_interface': 'lan5',
                                                'default_gateway': '10.1.2.2'}
    net_facts.get_interfaces = lambda: ['lan0', 'lan1', 'lan2', 'lan3',
                                        'lan4', 'lan5', 'lan6', 'lan7',
                                        'lan8', 'lan9']

# Generated at 2022-06-13 01:41:16.997308
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    module = MockModule()
    net_facts = HPUXNetwork(module)
    facts = net_facts.populate()
    interfaces = facts['interfaces']
    interface = interfaces[0]
    assert facts['default_interface'] == 'lan0'
    assert facts['default_gateway'] == '192.168.1.1'
    assert facts[interface]['device'] == interface
    assert facts[interface]['ipv4']['address'] == '192.168.1.105'
    assert facts[interface]['ipv4']['network'] == '192.168.1.0'

# Generated at 2022-06-13 01:41:21.078117
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    net = HPUXNetwork()
    net.module = AnsibleModuleStub()
    net.module.run_command = run_command_stub
    network_facts = net.get_default_interfaces()
    assert network_facts['default_interface'] == 'lan0'
    assert network_facts['default_gateway'] == '192.168.1.1'



# Generated at 2022-06-13 01:41:24.014617
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    module = AnsibleModule(argument_spec={})
    network = HPUXNetwork(module)
    out = network.get_default_interfaces()
    assert out == {'default_gateway': '192.168.1.1',
                   'default_interface': 'lan0'}



# Generated at 2022-06-13 01:41:26.540082
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    module = AnsibleModule(argument_spec={})
    facts = HPUXNetwork().populate()
    assert 'interfaces' in facts
    assert 'default_interface' in facts
    assert 'default_gateway' in facts
    assert facts['interfaces'] == ['lan0', 'lan1']



# Generated at 2022-06-13 01:41:27.751102
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    assert HPUXNetworkCollector._platform == 'HP-UX'


# Generated at 2022-06-13 01:41:34.549617
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    mod = AnsibleModule(
        argument_spec={},
    )

    net_facts = HPUXNetwork()
    res = net_facts.populate()

    mod.exit_json(ansible_net_interfaces=res.get('interfaces', []),
                  ansible_net_gather_network_resources=res,
                  ansible_net_gather_subset=['!all'],
                  ansible_net_gather_timeout=10)

from ansible.module_utils.basic import *
main = lambda: test_HPUXNetwork_populate()

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 01:41:36.253900
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    obj_HPUXNetwork = HPUXNetwork()
    assert obj_HPUXNetwork


# Generated at 2022-06-13 01:41:40.237798
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    module = AnsibleModuleMock()
    module.run_command = MagicMock(return_value=(0, OUTPUT_NETSTAT_NR, ''))
    network = HPUXNetwork(module=module)

    default = network.get_default_interfaces()

    assert default['default_interface'] == 'lan1'
    assert default['default_gateway'] == '192.168.1.1'



# Generated at 2022-06-13 01:41:42.326875
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    n = HPUXNetwork()
    assert n.platform == 'HP-UX'



# Generated at 2022-06-13 01:41:43.765716
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    network = HPUXNetwork({})
    assert network.platform == network.platform



# Generated at 2022-06-13 01:42:27.716116
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    """
    Test the method get_interfaces_info of class HPUXNetwork.
    """
    module = None
    hpuxtn = HPUXNetwork()
    result = hpuxtn.get_interfaces_info()
    Lan_interfaces = ['lan0', 'lan1', 'lan3', 'lan9', 'lan13',
                      'lan15', 'lan17', 'lan19', 'lan21', 'lan23']
    assert result.keys() == Lan_interfaces

# Generated at 2022-06-13 01:42:33.364658
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    class Param():
        module = ""
        def __init__(self, module):
            self.module = module

    class TestHPUXNetwork():
        module = ""
        _net_defaults = {}

        def __init__(self, module):
            self.module = module
            self._net_defaults = {}

        def get_default_interfaces(self):
            return self._net_defaults

    class TestModule():
        def __init__(self):
            self.params = Param("")


# Generated at 2022-06-13 01:42:38.440850
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    '''
    Test to verify the method get_interfaces_info of class HPUXNetwork
    '''
    test_object = HPUXNetwork()
    test_get_interfaces_info = HPUXNetwork.get_interfaces_info(test_object)
    assert isinstance(test_get_interfaces_info, dict)
    assert 'lan0' in test_get_interfaces_info.keys()
    assert 'lan1' in test_get_interfaces_info.keys()
    assert 'lan2' in test_get_interfaces_info.keys()
    assert 'lan3' in test_get_interfaces_info.keys()
    assert test_get_interfaces_info['lan0']['device'] == 'lan0'

# Generated at 2022-06-13 01:42:50.865880
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    hpux_network = HPUXNetwork()
    hpux_network.module = MockModule()

# Generated at 2022-06-13 01:42:52.733859
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    network = HPUXNetwork()
    assert network._platform == 'HP-UX'
    assert network._fact_class == HPUXNetwork

# Generated at 2022-06-13 01:43:00.673811
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    module = AnsibleModuleMock()
    hpuxtate = HPUXNetwork(module)
    expected = {'default_interface': 'lan0',
                'default_gateway': '192.168.0.1',
                'interfaces': ['lan0'],
                'lan0': {'device': 'lan0',
                         'ipv4': {'address': '192.168.0.10',
                                  'network': '192.168.0.0',
                                  'interface': 'lan0'}}}
    result = hpuxtate.populate()
    assert_equal(result, expected)

# Generated at 2022-06-13 01:43:04.287409
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    """
    Unit test for constructor of class HPUXNetworkCollector
    """
    fact_class, platform = HPUXNetworkCollector._get_fact_class_platform()
    assert fact_class == HPUXNetwork
    assert platform == 'HP-UX'



# Generated at 2022-06-13 01:43:07.700323
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    net = HPUXNetwork()
    interfaces = net.get_default_interfaces()
    assert "default_gateway" in interfaces
    assert "default_interface" in interfaces



# Generated at 2022-06-13 01:43:09.275940
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    facts_network = Network()
    assert isinstance(facts_network, Network)



# Generated at 2022-06-13 01:43:14.545124
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    network = HPUXNetwork(None)
    interfaces = network.get_interfaces_info()
    assert isinstance(interfaces, dict)
    assert 'lan0' in interfaces
    assert 'device' in interfaces['lan0']
    assert 'ipv4' in interfaces['lan0']
    assert 'address' in interfaces['lan0']['ipv4']
    assert 'network' in interfaces['lan0']['ipv4']
    assert 'interface' in interfaces['lan0']['ipv4']

# Generated at 2022-06-13 01:44:54.950999
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    network = HPUXNetworkCollector()
    assert network.platform == "HP-UX"
    assert network.fact_class == HPUXNetwork
    assert isinstance(network.fact_class, object)


# Generated at 2022-06-13 01:44:57.580355
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    # Instantiate a HPUXNetworkCollector object
    hpux_network_collector = HPUXNetworkCollector()
    assert(hpux_network_collector.fact_class == HPUXNetwork)
    assert(hpux_network_collector.platform == 'HP-UX')

# Generated at 2022-06-13 01:44:58.999873
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    net = HPUXNetwork({}, {}, {})
    assert type(net) is HPUXNetwork


# Generated at 2022-06-13 01:45:00.622894
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    obj = HPUXNetworkCollector(None)
    assert obj._fact_class is HPUXNetwork
    assert obj._platform == 'HP-UX'

# Generated at 2022-06-13 01:45:08.216919
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    hostname = 'localhost'
    ipaddress = '127.0.0.1'
    ansible_module = DummyAnsibleModule()
    network_facts = HPUXNetwork(ansible_module)
    default_interfaces = network_facts.get_default_interfaces()
    assert default_interfaces['default_interface'] == 'lo0'
    assert default_interfaces['default_gateway'] == '127.0.0.1'


# Generated at 2022-06-13 01:45:16.496297
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    from ansible.module_utils import basic
    from ansible.module_utils.facts.network import HPUXNetwork
    from ansible.module_utils.facts import FactCollector

    mock_module = basic.AnsibleModule(
        argument_spec=dict()
    )

    mock_module.run_command = lambda x: (0, "lan0        lan0          217.172.176.58  255.255.255.252  UP", "")
    mock_network = HPUXNetwork(mock_module)
    assert mock_network.get_interfaces_info() == {'lan0': {'device': 'lan0', 'ipv4': {'address': '217.172.176.58', 'interface': 'lan0', 'network': '255.255.255.252'}}}

    mock_module.run

# Generated at 2022-06-13 01:45:20.036422
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    import sys
    if sys.version_info[0] == 2 and sys.version_info[1] == 6:
        import unittest2 as unittest
    else:
        import unittest

    class TestHPUXNetworkCollector(unittest.TestCase):
        def test_constructor(self):
            hpux_network_collector = HPUXNetworkCollector()
            self.assertEqual(hpux_network_collector._fact_class, HPUXNetwork)
            self.assertEqual(hpux_network_collector._platform, 'HP-UX')

    unittest.main()

# Generated at 2022-06-13 01:45:24.689518
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    hpn = HPUXNetwork()

    default_interfaces_facts = hpn.get_default_interfaces()
    assert default_interfaces_facts['default_interface'] == 'lan0'
    assert default_interfaces_facts['default_gateway'] == '172.16.50.1'


# Generated at 2022-06-13 01:45:28.582404
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    hpux_obj = HPUXNetworkCollector()
    assert hpux_obj._fact_class == HPUXNetwork
    assert hpux_obj._platform == 'HP-UX'


# Generated at 2022-06-13 01:45:33.647201
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    fake_ansible_module = HPUX_fake_ansible_module()
    network = HPUXNetwork(fake_ansible_module)
    default_interfaces_facts = network.get_default_interfaces()
    assert default_interfaces_facts['default_interface'] == 'lan0'
    assert default_interfaces_facts['default_gateway'] == '10.1.1.1'

