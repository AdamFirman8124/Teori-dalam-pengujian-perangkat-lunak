

# Generated at 2022-06-13 01:37:59.763544
# Unit test for method get_default_interfaces of class HPUXNetwork

# Generated at 2022-06-13 01:38:02.254418
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True,
    )

    network = HPUXNetwork(module)
    network.populate()

    assert network.ipv4['address'] == '172.16.136.135'
    assert network.ipv4['network'] == '172.16.136.0'
    assert network.ipv4['interface'] == 'lan0'

# Generated at 2022-06-13 01:38:04.991161
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    net_obj = HPUXNetwork({"module": None})
    assert net_obj.platform == 'HP-UX'

# Generated at 2022-06-13 01:38:13.628830
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    HPUXNetwork_obj = HPUXNetwork(None)
    interfaces = HPUXNetwork_obj.get_interfaces_info()
    assert isinstance(interfaces, dict)

    for interface in interfaces:
        assert isinstance(interfaces[interface], dict)
        assert isinstance(interfaces[interface]['ipv4'], dict)
        assert interfaces[interface]['ipv4']['address'] == '127.0.0.1'
        assert interfaces[interface]['ipv4']['network'] == '127.0'
        assert interfaces[interface]['ipv4']['interface'] == interface
        assert interfaces[interface]['device'] == interface

# Generated at 2022-06-13 01:38:14.263591
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    HPUXNetworkCollector()

# Generated at 2022-06-13 01:38:21.937767
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    default_interfaces = {'default_interface': 'lan0', 'default_gateway': '192.168.1.1'}
    test_module = Network(module=None)
    test_module.run_command = lambda x, check_rc=True, close_fds=True: (0, 'default 192.168.1.1        UG        0        0        lan0', '')
    assert test_module.get_default_interfaces() == default_interfaces


# Generated at 2022-06-13 01:38:29.506210
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    module = FakeModule()
    network_facts_collector = HPUXNetworkCollector(module)
    network_facts = HPUXNetwork(network_facts_collector)

    assert network_facts.populate() == {'default_gateway': '192.168.10.1',
                                        'default_interface': 'lan99',
                                        'interfaces': ['lan99'],
                                        'lan99': {'device': 'lan99',
                                                  'ipv4': {'address': '192.168.10.10',
                                                           'interface': 'lan99',
                                                           'network': '192.168.10.0'}}}



# Generated at 2022-06-13 01:38:32.561149
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )
    network = HPUXNetwork(module)
    assert network._module is module
    assert network._platform == 'HP-UX'
    assert not network._facts


# Generated at 2022-06-13 01:38:34.654001
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    assert (HPUXNetwork.platform == 'HP-UX')


# Generated at 2022-06-13 01:38:44.141192
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    net = HPUXNetwork()
    net.module = MockModule()

# Generated at 2022-06-13 01:38:57.177534
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    test_module = Network({})
    test_module.run_command = lambda x: (0,
                                         'lan0 1000fe0100c8c05 FFFFFFFF lan0 1000fe0100c8c05 FFFFFFFF',
                                         '')
    hpux_network_facts = HPUXNetwork({})
    fact_value = hpux_network_facts.get_interfaces_info()
    assert fact_value == {'lan0': {'ipv4': {'address': '1000fe0100c8c05', 'network': 'FFFFFFFF', 'interface': 'lan0'}, 'device': 'lan0'}}

# Generated at 2022-06-13 01:39:02.110400
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    my_module = AnsibleModuleMock()
    network = HPUXNetwork(module=my_module)

    expected = {'default_interface': 'lan2', 'default_gateway': '192.0.2.2'}
    actual = network.get_default_interfaces()
    assert expected == actual

# Generated at 2022-06-13 01:39:03.674066
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    network = HPUXNetworkCollector()
    assert network is not None

# Generated at 2022-06-13 01:39:10.053033
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    test_module = AnsibleModule(
        argument_spec=dict(gather_subset=dict(default=['!all'], type='list'))
    )
    network_collector = HPUXNetworkCollector(test_module)

    network_facts = network_collector.collect()
    #print(network_facts)
    assert 'default_interface' in network_facts
    assert 'interfaces' in network_facts
    assert 'interface_lan0' in network_facts

# Generated at 2022-06-13 01:39:13.948496
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    from ansible.module_utils.facts.network.base import Network
    obj = HPUXNetwork()
    assert isinstance(obj, Network) is True, 'Object is not an instance of Network class'

if __name__ == '__main__':
    test_HPUXNetwork()

# Generated at 2022-06-13 01:39:22.854056
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    module = AnsibleModuleMock()
    network = HPUXNetwork(module)
    network_facts = network.populate()
    default_interface = network_facts['default_interface']
    default_gateway = network_facts['default_gateway']
    interfaces = network_facts['interfaces']
    assert 'default_interface' in network_facts
    assert 'default_gateway' in network_facts
    assert 'interfaces' in network_facts

    for i in interfaces:
        assert i == 'lo0' or i == 'lan0'

    assert default_interface == 'lan0'
    assert default_gateway == '172.23.18.1'

# Generated at 2022-06-13 01:39:28.815338
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    from ansible_collections.ansible.netcommon.tests.unit.compat.mock import patch, MagicMock
    from ansible.module_utils.facts.network.hpux import HPUXNetwork

    module = MagicMock()
    set_module_args = {
        'gather_subset': ['!all', '!min'],
        'gather_network_resources': ['default_interface', 'default_gateway'],
        'gather_network_resources.interface.ipv4': ['address']
    }
    module.params = set_module_args
    mock_ansible_module = patch('ansible_collections.ansible.netcommon.plugins.module_utils.network.common.module.AnsibleModule')
    mock_ansible_module.start()
    my_obj = HPU

# Generated at 2022-06-13 01:39:32.599525
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    network = HPUXNetwork()
    network.module = MagicMock()
    network.module.run_command.return_value = (0, 'default 129.159.236.1 UGS 14 0 lan9000\n', '')

    assert network.populate() == {'default_interface': 'lan9000', 'default_gateway': '129.159.236.1'}



# Generated at 2022-06-13 01:39:36.697225
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    hpux_network = HPUXNetwork()
    default_interfaces = hpux_network.get_default_interfaces()
    assert default_interfaces == {'default_interface': 'lan0',
                                  'default_gateway': '127.0.0.1'}


# Generated at 2022-06-13 01:39:37.442777
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    HPUXNetworkCollector()
    pass

# Generated at 2022-06-13 01:39:53.094480
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():

    module = AnsibleModule(argument_spec={}, supports_check_mode=True)
    module.run_command = lambda x, check_rc=True: (0, '', '')
    network = HPUXNetwork(module)

    # When netstat is not installed
    module.run_command = lambda x, check_rc=True: (
        256, '', 'sh: netstat: not found')
    network.populate()
    assert 'default_interface' not in network.facts
    assert 'default_gateway' not in network.facts

    # When netstat is installed
    module.run_command = lambda x, check_rc=True: (0, OUTPUT, '')
    network_facts = network.populate()
    assert network_facts['default_interface'] == 'lan1'

# Generated at 2022-06-13 01:39:55.464922
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    network_facts = HPUXNetwork()
    assert network_facts.platform == 'HP-UX'


# Generated at 2022-06-13 01:40:02.439880
# Unit test for method get_default_interfaces of class HPUXNetwork

# Generated at 2022-06-13 01:40:09.112587
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    data = {'default_gateway': '7.8.9.1',
            'default_interface': 'lan0'}
    test_network = HPUXNetwork()
    test_network.get_default_interfaces = \
        lambda: data
    d = test_network.populate()
    assert d['default_gateway'] == data['default_gateway']
    assert d['default_interface'] == data['default_interface']



# Generated at 2022-06-13 01:40:12.962187
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True)

    module.run_command = MagicMock(return_value=(0, '', ''))
    module.get_bin_path = MagicMock(return_value=True)

    net_collector = HPUXNetworkCollector(module=module)
    net_collector.populate()
    assert 'default_interface' in net_collector.network.facts
    assert 'default_gateway' in net_collector.network.facts
    assert 'interfaces' in net_collector.network.facts



# Generated at 2022-06-13 01:40:14.350019
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    try:
        assert(HPUXNetworkCollector)
    except NameError:
        raise AssertionError
    assert(issubclass(HPUXNetworkCollector, NetworkCollector))



# Generated at 2022-06-13 01:40:21.604550
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    from ansible.module_utils.facts.network.hpux import HPUXNetwork
    import pytest
    from ansible.module_utils.ansible_release import __version__ as ansible_version

    fixtures = (
        'default_interfaces',
        'interfaces',
    )

    # Run tests for ansible 2.1 only
    if ansible_version.startswith('2.1.'):
        pytest.skip('This test is not valid for ansible 2.0.x')

    m = HPUXNetwork({})
    m.run_command = lambda *args, **kwargs: (0, command_output[args[0]], '')

    def run_get_interfaces_info():
        return m.get_interfaces_info()

    for fixture in fixtures:
        yield check_output, run

# Generated at 2022-06-13 01:40:29.482422
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    """ Unit test for method get_default_interfaces of class HPUXNetwork"""
    from types import ModuleType
    from ansible.module_utils.facts.network.hparray import HPUXNetwork
    from ansible.module_utils.facts.network.hpux import HPUXNetworkCollector
    from ansible.module_utils.facts.network.hpux import HPUXNetwork
    hpu = HPUXNetworkCollector(ModuleType('ansible.module_utils.facts.network.hpux'))
    result = hpu.populate()
    assert (type(result) is dict) is True
    assert 'default_gateway' in result
    assert 'default_interface' in result

# Generated at 2022-06-13 01:40:31.661356
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    obj = HPUXNetworkCollector([])
    assert obj._fact_class == HPUXNetwork
    assert obj._platform == 'HP-UX'

# Generated at 2022-06-13 01:40:40.109596
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    """
    This test unit performs the following tests:
    - creates a class HPUXNetwork
    - checks if the method populate returns the right data
    - checks that all keys are present
    """
    mock_module = NetworkCollector()
    mock_module.run_command = run_command_mock
    hpux_network = HPUXNetwork(mock_module)
    hpux_network.populate()
    for key in ['default_interface', 'interfaces', 'lo0', 'lan0']:
        assert key in hpux_network.facts


# Generated at 2022-06-13 01:41:01.365463
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    try:
        HPUXNetworkCollector()
    except NameError:
        assert False, 'Failed to create HPUXNetworkCollector'

    assert True, 'Created HPUXNetworkCollector'



# Generated at 2022-06-13 01:41:08.117635
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    module = AnsibleModule(argument_spec={})
    module.run_command = MagicMock(return_value=(0, 'default      xxx.xxx.xxx.xxx  UGSx       xxxx   0     0     lan0  ', ''))
    hpuxnetwork = HPUXNetwork(module)
    assert hpuxnetwork.get_default_interfaces() == {'default_interface': 'lan0', 'default_gateway': 'xxx.xxx.xxx.xxx'}



# Generated at 2022-06-13 01:41:12.554385
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    """
    Unit test for constructor of class HPUXNetworkCollector
    """
    network_collector = HPUXNetworkCollector()
    assert network_collector._fact_class == HPUXNetwork
    assert network_collector._platform == 'HP-UX'

# Generated at 2022-06-13 01:41:17.405043
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    expected = {'lan0': {'device': 'lan0',
                         'ipv4': {'address': '192.1.1.111',
                                  'network': '192.1.1',
                                  'interface': 'lan0',
                                  }}}
    result = HPUXNetwork.get_interfaces_info('lan0')
    assert expected['lan0'] == result['lan0']

# Generated at 2022-06-13 01:41:24.947538
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    """
    Test get_interfaces_info
    """

    from ansible.module_utils.facts.network.hpu import HPUXNetwork
    from ansible.module_utils.facts.network.hpu import HPUXNetworkCollector
    from test.units.compat import unittest

    class TestHPUXNetwork(unittest.TestCase):
        """
        Test HPUXNetwork class methods
        """

        def setUp(self):
            """
            Test setup
            """
            self.network = HPUXNetwork()
            self.net_collector = HPUXNetworkCollector()
            self.net_collector.get_all_facts = lambda: True


# Generated at 2022-06-13 01:41:30.651747
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    """
    This function is a unit test for the constructor of class HPUXNetworkCollector
    """
    ansible_module = AnsibleModule(
        argument_spec = dict(gather_subset=dict(default=['all'], type='list')))
    network_collector = HPUXNetworkCollector(ansible_module)
    assert network_collector.gather_subset == ['all']

# Generated at 2022-06-13 01:41:33.421626
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    class TestModule:
        def run_command(self, cmd):
            return 0, cmd
    test_module = TestModule()
    test_hpux_network = HPUXNetwork(module=test_module)
    assert test_hpux_network.get_interfaces_info() == {}

# Generated at 2022-06-13 01:41:41.675922
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    module = MockModule()
    HPUXNetwork_object = HPUXNetwork()
    HPUXNetwork_object.module = module
    HPUXNetwork_object.get_interfaces_info = Mock(return_value={})
    result = HPUXNetwork_object.populate()
    assert isinstance(result, dict), "HPUXNetwork_populate method should return a dictionary"
    assert len(result.keys()) == 3, "HPUXNetwork_populate method should return a dictionary of length 3"
    assert 'default_interface' in result.keys(), "HPUXNetwork_populate method should return a dictionary \
                                                  with key 'default_gateway'"
    assert 'interfaces' in result.keys(), "HPUXNetwork_populate method should return a dictionary \
                                                  with key 'interfaces'"
   

# Generated at 2022-06-13 01:41:46.767292
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    module = AnsibleModule(argument_spec=dict())
    network_facts_obj = HPUXNetwork(module)
    interfaces = network_facts_obj.get_interfaces_info()
    default_interfaces = network_facts_obj.get_default_interfaces()
    network_facts = network_facts_obj.populate()

    assert 'default_interface' in network_facts
    assert 'interfaces' in network_facts
    assert network_facts['interfaces'] == interfaces.keys()
    assert 'default_gateway' in default_interfaces
    assert 'default_interface' in default_interfaces



# Generated at 2022-06-13 01:41:57.423545
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    network = HPUXNetwork()
    network.module = get_module_mock()
    network.module.run_command = run_command_mock

    # Default route is a not a virtual interface
    network.module.run_command.return_value = 0, 'default   192.168.0.1              UGS        0        7200 lan0', ''

    # Network interface with physical address is a not a virtual interface
    network.module.run_command.return_value = 0, 'lan0   192.168.0.1              UGS        0        7200 lan0  link#1', ''

    # Network interface with virtual address is a not a virtual interface
    network.module.run_command.return_value = 0, 'lan0   192.168.0.1              UGS        0        7200 lan0:1', ''



# Generated at 2022-06-13 01:42:38.128588
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    network = HPUXNetwork({})
    assert network.facts['default_gateway'] == '192.168.56.1'

# Generated at 2022-06-13 01:42:40.529044
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    obj = HPUXNetworkCollector()
    assert obj.__class__.__name__ == 'HPUXNetworkCollector'

# Generated at 2022-06-13 01:42:44.312061
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    network = HPUXNetwork()
    assert network.platform == 'HP-UX'
    assert network.populate() is None

# Generated at 2022-06-13 01:42:53.207857
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    test_object = HPUXNetwork()
    test_output = """Name  Mtu  Network  Address  Ipkts  Ierrs  Opkts  Oerrs  Coll  Queue"""
    test_output = test_output + """\nlsp0 1500     lan9  0:123:abc:def:ghi:jkl      0      0      0      0     0      0"""

    assert test_object.get_interfaces_info() == {'lan9':
                                                 {'ipv4': {'address': '0:123:abc:def:ghi:jkl',
                                                  'network': 'lan9',
                                                  'interface': 'lan9'},
                                                  'device': 'lan9'}}

# Generated at 2022-06-13 01:43:02.448951
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    m = HPUXNetwork()
    m.module = MockAnsibleModule()
    m.module.run_command = MockRunCommand()
    m.module.run_command.side_effect = [
        (0, "default  172.20.10.254  UG       0 0        en2", ''),
        (0, "lan10    172.20.10.0    255.255.255.0  U           0 0        lan10 ", '')
    ]
    res = m.populate()
    assert res['default_gateway'] == '172.20.10.254'
    assert res['default_interface'] == 'en2'
    assert res['interfaces'][0] == 'lan10'

# Generated at 2022-06-13 01:43:05.171870
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    """
    Constructor test of class HPUXNetworkCollector
    """
    obj = HPUXNetworkCollector()
    assert obj.platform == 'HP-UX'
    assert obj._fact_class is HPUXNetwork

# Generated at 2022-06-13 01:43:07.098498
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    h = HPUXNetworkCollector()
    # test empty constructor
    assert h.platform_requirements is None

# Generated at 2022-06-13 01:43:10.433977
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    test = HPUXNetwork(dict())
    iface = test.get_default_interfaces()
    assert iface['default_interface'] == 'lan0'
    assert iface['default_gateway'] == '192.168.1.1'


# Generated at 2022-06-13 01:43:17.611593
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    network_module_output = "default 10.0.0.1 UGn 0 0 lan0 \r\n"\
                            "10.0.10.0         10.0.10.255      U           2        0        lan0\r\n"\
                            "10.0.10.1         10.0.10.255      UHS         0        0        lo0\r\n"
    module = MockModule(network_module_output)
    network_facts = HPUXNetwork(module).populate()

# Generated at 2022-06-13 01:43:26.679949
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():

    ret = HPUXNetwork.populate()

    assert ret['default_interface'] == 'lan0'
    assert ret['default_gateway'] == '192.168.1.2'

    ret = HPUXNetwork.get_interfaces_info()
    assert ret['lan0']['ipv4']['address'] == '192.168.1.10'
    assert ret['lan1']['ipv4']['address'] == '192.168.1.20'

    ret = HPUXNetwork.get_default_interfaces()
    assert ret['default_interface'] == 'lan0'
    assert ret['default_gateway'] == '192.168.1.2'

# Generated at 2022-06-13 01:45:13.830086
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    networking = HPUXNetwork()
    rc, out, err = networking.module.run_command("/usr/bin/netstat -niw")
    interfaces = out.splitlines()
    network_info = networking.get_interfaces_info()
    assert len(interfaces) >= len(network_info.values())

# Generated at 2022-06-13 01:45:14.930708
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    n = HPUXNetwork(dict(module=dict()))
    assert n is not None

# Generated at 2022-06-13 01:45:17.842549
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    assert HPUXNetwork.platform == 'HP-UX'
    h = HPUXNetwork({})
    assert h.module is not None


# Generated at 2022-06-13 01:45:18.758819
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    HPUXNetworkCollector()

# Generated at 2022-06-13 01:45:23.120302
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    default_interfaces = HPUXNetwork.get_default_interfaces()
    assert len(default_interfaces) == 2
    assert default_interfaces['default_interface'] == 'lan2'
    assert default_interfaces['default_gateway'] == '10.49.64.254'



# Generated at 2022-06-13 01:45:27.740081
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    from ansible.module_utils import basic
    m = basic.AnsibleModule(
        argument_spec={},
        supports_check_mode=True
    )
    HPNetwork = HPUXNetwork(m)
    HPNetwork.populate()



# Generated at 2022-06-13 01:45:29.561071
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    network = HPUXNetwork()
    assert network.platform == 'HP-UX'


# Generated at 2022-06-13 01:45:30.444587
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    HPUXNetworkCollector()

# Generated at 2022-06-13 01:45:38.473741
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    from ansible.module_utils.facts.network.base import Network
    from ansible.module_utils.facts.network.hpux import HPUXNetworkCollector
    from ansible.module_utils.facts.network.hpux import HPUXNetwork

    collector = HPUXNetworkCollector()
    network_facts = collector.collect()

    assert network_facts is not None
    assert network_facts['default_interface'] == 'lan0'
    assert network_facts['interfaces'] == ['lan0']
    assert network_facts['lan0'] == {'ipv4': {'network': '192.168.122.0', 'interface': 'lan0', 'address': '192.168.122.1'}, 'device': 'lan0'}



# Generated at 2022-06-13 01:45:43.774379
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    interfaces = {'lan0': {'device': 'lan0', 'ipv4': {'network': '127.0.0.0',
                                                      'interface': 'lan0',
                                                      'address': '127.0.0.1'}}}
    netstat_path = '/usr/bin/netstat'
    class MockModule():
        def get_bin_path(self, path):
            return netstat_path

        def run_command(self, command):
            return 0, """lan0   link#1  UP  127.0.0.1  127.0.0.0
lo0   loopback  UP  localhost  localhost  localhost  localhost""", ''

    class MockHPNetwork():
        module = MockModule()

    HPUXNetwork.module = MockModule()

    result = HPU