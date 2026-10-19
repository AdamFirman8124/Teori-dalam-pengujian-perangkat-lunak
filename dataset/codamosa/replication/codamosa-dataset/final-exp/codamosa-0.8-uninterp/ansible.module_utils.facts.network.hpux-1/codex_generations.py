

# Generated at 2022-06-13 01:37:54.513929
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    """ This is a unit test for method populate of class HPUXNetwork """
    module = FakeModule()
    fake_data = """
default  inet 0.0.0.0/0  gateway 10.0.2.2
lan0  inet 192.168.1.1 netmask 0xffffff00 broadcast 192.168.1.255
lan1  inet 192.168.2.1 netmask 0xffffff00 broadcast 192.168.2.255
    """
    module.run_command = FakeRunCommand(stdout=fake_data)
    output = HPUXNetwork(module).populate()

# Generated at 2022-06-13 01:38:05.421499
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    module = MockModule()
    module.run_command = Mock(return_value=(0, '', ''))

    facter = HPUXNetwork(module)
    facter.get_default_interfaces = Mock(return_value={'default_interface': 'lan0',
                                                       'default_gateway': '10.0.0.1'})
    facter.get_interfaces_info = Mock(return_value={'lan0': {'device': 'lan0',
                                                             'ipv4': {'address': '10.0.0.9'}}})

    facts = facter.populate()

    assert facts['default_interface'] == 'lan0'
    assert facts['default_gateway'] == '10.0.0.1'
    assert facts['interfaces'] == ['lan0']
   

# Generated at 2022-06-13 01:38:10.586214
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    """ test constructor of class HPUXNetworkCollector
    """
    obj = HPUXNetworkCollector()
    assert obj.platform == 'HP-UX'
    obj1 = HPUXNetworkCollector(None, True)
    assert obj1.facts is None
    assert obj1.conditional is True
    assert obj1.network_resources

# Generated at 2022-06-13 01:38:11.583626
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    collector = HPUXNetworkCollector()
    assert collector.platform == 'HP-UX'


# Generated at 2022-06-13 01:38:12.815774
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    collector = HPUXNetworkCollector()
    assert collector._fact_class == HPUXNetwork
    assert collector._platform == 'HP-UX'

# Generated at 2022-06-13 01:38:15.231571
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    _HPUXNetwork = HPUXNetwork()
    default_interfaces = _HPUXNetwork.get_default_interfaces()

    assert default_interfaces['default_interface'] == 'lan100'
    assert default_interfaces['default_gateway'] == '172.18.19.1'



# Generated at 2022-06-13 01:38:16.952654
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    hpux_network = HPUXNetwork()
    assert hpux_network.get_interfaces_info() is not None

# Generated at 2022-06-13 01:38:18.665685
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    HPUXNetworkCollector()

# Generated at 2022-06-13 01:38:27.184331
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=False
    )
    hpuxNetwork = HPUXNetwork()
    hpuxNetwork.module = module
    default_interfaces_facts = hpuxNetwork.get_default_interfaces()
    network_facts = hpuxNetwork.get_interfaces_info()
    hpuxNetwork.populate()
    assert hpuxNetwork.default_interface == default_interfaces_facts['default_interface']
    assert hpuxNetwork.interfaces == ['lan1000', 'lan400', 'lan401']
    assert hpuxNetwork['lan1000']['ipv4'] == network_facts['lan1000']['ipv4']

# Generated at 2022-06-13 01:38:28.670141
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    hpn = HPUXNetwork(dict())
    assert hpn is not None


# Generated at 2022-06-13 01:38:44.834566
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    from ansible.module_utils.facts.network import HPUXNetwork
    from ansible.module_utils.facts.utils.fake import FakeModule
    result = {'default_gateway': '172.16.0.1', 'default_interface': 'lan0'}
    f = FakeModule()
    hpx = HPUXNetwork(f)
    assert hpx.get_default_interfaces() == result


# Generated at 2022-06-13 01:38:46.953906
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    facts = HPUXNetwork()
    assert facts.__class__.__name__ == 'HPUXNetwork'

# Generated at 2022-06-13 01:38:57.132996
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    HPUXNetwork._ansible_module = None
    HPUXNetwork._platform = "HP-UX"
    HPUXNetwork._module = None
    HPUXNetwork._bin_path = None
    HPUXNetwork._netstat_path = None
    HPUXNetwork._sysctl_path = None
    HPUXNetwork._route_path = None
    HPUXNetwork._ip_path = None
    HPUXNetwork._nmcli_path = None

    # Test case 1: Execute all functions in method populate
    # Input:
    #   HPUXNetwork._ansible_module = None
    #   HPUXNetwork._platform = "HP-UX"
    #   HPUXNetwork._module = None
    #   HPUXNetwork._bin_path = {'netstat': '/usr/bin/netstat'

# Generated at 2022-06-13 01:39:08.186688
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    class Object:
        def __init__(self):
            self.output = """Routing tables

Internet:
Destination        Gateway            Flags   Refs     Use     Int     Interface
default            129.35.6.1         UG          0        0       0      lan16
129.35.6.0         129.35.6.245       U          0        0       0      lan16
"""

        def run_command(self, command):
            return (0, self.output, '')

    module = Object()
    network = HPUXNetwork()

    result = network.get_default_interfaces()

    assert result['default_interface'] == 'lan16'
    assert result['default_gateway'] == '129.35.6.1'



# Generated at 2022-06-13 01:39:11.213872
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    hn = HPUXNetwork()
    assert hn.platform == 'HP-UX'
    assert hn._platform == 'HP-UX'
    assert hn.facts == {}


# Generated at 2022-06-13 01:39:16.440725
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    """
    This test checks that get_default_interfaces method
    of HPUXNetwork class works as intended and returns
    the right network facts.
    """

    result = {'default_interface': 'lan0',
              'default_gateway': '192.168.0.1'}
    assert result == HPUXNetwork().get_default_interfaces()


# Generated at 2022-06-13 01:39:18.547422
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    network_facts = HPUXNetwork()
    assert network_facts

# Generated at 2022-06-13 01:39:20.788845
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    """ Test constructor of HPUXNetworkCollector """
    obj = HPUXNetworkCollector()
    assert isinstance(obj, HPUXNetworkCollector)

# Generated at 2022-06-13 01:39:24.802291
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    module = AnsibleModule(argument_spec=dict())
    network_facts = HPUXNetwork(module)
    network_facts.populate()

    interfaces = network_facts.interfaces
    default = network_facts.default_interface
    gateway = network_facts.default_gateway

    assert 'lan0' in interfaces
    assert default == 'lan0'
    assert gateway == '10.10.10.9'


# Generated at 2022-06-13 01:39:26.629118
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    module = FakeModule()
    net = HPUXNetwork(module=module)
    net.get_default_interfaces()
    assert module.run_command_calls == 1



# Generated at 2022-06-13 01:39:38.605684
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    obj = HPUXNetwork()
    assert obj.platform == 'HP-UX'

# Generated at 2022-06-13 01:39:42.956528
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    """Unit test for method get_default_interfaces of class HPUXNetwork"""
    test_hpx_nw = HPUXNetwork()
    default_interfaces = test_hpx_nw.get_default_interfaces()
    result = False
    if (default_interfaces['default_gateway'] is not None and
        default_interfaces['default_interface'] is not None):
        result = True
    assert result is True


# Generated at 2022-06-13 01:39:48.812143
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    test_module = NetworkCollector()
    test_module.run_command = lambda x: (0, 'default 192.168.0.1 UGS 0 794 lan0\n', '')
    result = HPUXNetwork(test_module).get_default_interfaces()
    assert result['default_interface'] == 'lan0'
    assert result['default_gateway'] == '192.168.0.1'



# Generated at 2022-06-13 01:39:51.532918
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    h = HPUXNetworkCollector()
    assert h._fact_class == HPUXNetwork
    assert h._platform == 'HP-UX'

#Unit test for function populate in class HPUXNetwork

# Generated at 2022-06-13 01:39:55.960293
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    test_module = MockModule()
    test_network = HPUXNetwork(module=test_module)
    assert test_network.get_default_interfaces() == {'default_gateway': '10.0.0.1', 'default_interface': 'lan1'}


# Generated at 2022-06-13 01:39:57.140744
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    hpux = HPUXNetwork()
    assert hpux.platform == 'HP-UX'


# Generated at 2022-06-13 01:40:00.532888
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    module = AnsibleModuleMock()
    module.run_command = run_command_mock
    network = HPUXNetwork(module)
    interfaces = network.get_default_interfaces()
    assert interfaces['default_interface'] == 'lan1000'
    assert interfaces['default_gateway'] == '192.168.10.1'



# Generated at 2022-06-13 01:40:11.239730
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    """ Test case - test method `populate` of class HPUXNetwork """
    collect_network = HPUXNetworkCollector()
    facts = collect_network.get_facts()
    # Should be a dictionary
    assert isinstance(facts, dict)
    # Should have 4 keys
    assert len(facts.keys()) == 4
    # Dictionary should include:
    # - default_interface
    assert 'default_interface' in facts
    # - interfaces
    assert 'interfaces' in facts
    # - lan0
    assert 'lan0' in facts
    # - lan1
    assert 'lan1' in facts
    # Dictionary default_interface should be a string
    assert isinstance(facts['default_interface'], str)
    # Dictionary interfaces should be a list of 2 elements
    assert isinstance(facts['interfaces'], list)


# Generated at 2022-06-13 01:40:21.850052
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    module = AnsibleModule(argument_spec=dict())
    sample_text = b'''
default          172.20.58.2        UG   2   0        en0
10.1.1.1        10.1.1.3          UGHS 2      0  lan0
172.20.58        0.0.0.0          U     8      0  en0
172.20.58.2        0.0.0.0          UHS   0      0      lo0
localhost        0.0.0.0          UH       6      0      lo0
'''
    module.run_command = MagicMock(return_value=(0, sample_text, b''))
    hpux_network = HPUXNetwork(module)
    default_interfaces_facts = hpux_network.get_default_interfaces

# Generated at 2022-06-13 01:40:23.781398
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    assert HPUXNetwork.get_interfaces_info(None, None) is None, 'function did not return None'

# Generated at 2022-06-13 01:40:41.331441
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    class AnsibleModule:
        def run_command(self, cmd):
            return 0, "lan0  lan      80  802.3/Ethernet        UP        00:26:b6:07:6b:f6", ''

    class HPUXNetworkTestClass(HPUXNetwork):
        def __init__(self, module):
            self.module = module

    data = HPUXNetworkTestClass(AnsibleModule()).get_interfaces_info()
    assert data['lan0']['ipv4']['address'] == '80'

# Generated at 2022-06-13 01:40:42.109111
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    HPUXNetworkCollector()

# Generated at 2022-06-13 01:40:49.104877
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():

    # Create an instance of the class "HPUXNetworkCollector" to test
    test_obj = HPUXNetworkCollector()

    # Check the type of the object
    assert isinstance(test_obj, NetworkCollector)

    # Check the value of _fact_class
    assert test_obj._fact_class == HPUXNetwork

    # Check the value of _platform
    assert test_obj._platform == 'HP-UX'


# Generated at 2022-06-13 01:40:53.544747
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    test_module = type("ansible_module", (object,),
                       {'run_command': run_command})
    network_obj = HPUXNetwork(module=test_module)
    interfaces = network_obj.get_interfaces_info()
    result = interfaces['lan0']['ipv4']['address']
    assert result == '192.168.0.2'



# Generated at 2022-06-13 01:40:57.133460
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    module = AnsibleModule(argument_spec={})
    module.run_command = MagicMock(return_value=(0, '', ''))
    HPUXnetwork = HPUXNetwork(module=module)

    HPUXnetwork.populate()
    module.run_command.assert_any_call('/usr/bin/netstat -niw')
    module.run_command.assert_any_call('/usr/bin/netstat -nr')


# Generated at 2022-06-13 01:41:07.803534
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    module = FakeAnsibleModule()
    network_collector = HPUXNetworkCollector(module)
    facts = network_collector.collect(None)

    assert facts['default_interface'] == 'lan0'
    assert facts['default_gateway'] == '10.0.0.1'
    assert facts['interfaces'] == []
    assert facts['interface_lan0']['device'] == 'lan0'
    assert facts['interface_lan0']['ipv4']['address'] == '10.0.0.100'
    assert facts['interface_lan0']['ipv4']['network'] == '10.0.0.0'
    assert facts['interface_lan0']['ipv4']['interface'] == 'lan0'

# Generated at 2022-06-13 01:41:08.653350
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    HPUXNetworkCollector()

# Generated at 2022-06-13 01:41:18.803327
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    default_interfaces_facts = {'default_interface': 'lan0',
                                'default_gateway': '10.10.10.1'}
    interfaces = {'lan0': {'device': 'lan0',
                           'ipv4': {'network': '10.10.10.0',
                                    'interface': 'lan0',
                                    'address': '10.10.10.5'}}}
    module = MagicMock(return_value=(0, '', ''))
    HPUXNetwork.module = module
    HPUXNetwork.get_interfaces_info = MagicMock(return_value=interfaces)
    HPUXNetwork.get_default_interfaces = MagicMock(return_value=default_interfaces_facts)
    hpux_network_facts = HPUXNetwork()
   

# Generated at 2022-06-13 01:41:25.854605
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    from ansible.module_utils._text import to_text
    from ansible.module_utils.facts.utils import mock_module
    from ansible.module_utils.facts.utils import AnsibleModule

    from ansible.module_utils.facts.network.hpux import HPUXNetwork

    interfaces = {'lan0': {'device': 'lan0', 'ipv4': {'address': '192.168.1.3',
                                                      'network': '192.168.1.0',
                                                      'interface': 'lan0',
                                                      'address': '192.168.1.3'}}}
    runner = mock_module.MockModuleRunner(module_name='test_Class_get_interfaces_info')
    hpxnet = HPUXNetwork()

    rc, out, err = runner.run_

# Generated at 2022-06-13 01:41:30.743162
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    """
    Constructor HPUXNetworkCollector must set platform and fact_class.
    """
    hpux_network_collector = HPUXNetworkCollector()
    assert hpux_network_collector._platform == 'HP-UX'
    assert hpux_network_collector._fact_class == HPUXNetwork


# Generated at 2022-06-13 01:41:53.680061
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    fact_network = HPUXNetworkCollector()
    assert fact_network._platform == 'HP-UX'
    assert fact_network._fact_class == HPUXNetwork

# Generated at 2022-06-13 01:42:04.529592
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    class MockModule(object):
        def run_command(self, command):
            rc = 0
            if command == '/usr/bin/netstat -niw':
                out = 'lan0        lan       1   3   0           0     en0      UP   UP                    1.1.1.1'
            else:
                rc = 256
                out = 'Bad command: ' + command
            return rc,out,''
    module = MockModule()
    HPUXNetwork.module = module
    interfaces = HPUXNetwork.get_interfaces_info()
    assert interfaces['lan0']['device'] == 'lan0'
    assert interfaces['lan0']['ipv4']['address'] == '1.1.1.1'
    assert interfaces['lan0']['ipv4']['network'] == 'lan'

# Generated at 2022-06-13 01:42:10.947196
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    """Unit test for method populate of class HPUXNetwork"""
    out = """default  192.168.1.1         UG       0 0        lan0
192.168.1.0        localhost         UGS      0 10        lo0
224.0.0.0          192.168.1.1       UG       0 0        lan0
default            192.168.1.1       UG       0 0        lan0
default            192.168.1.1       UG       0 0        lan0
"""

    module = Mock({'run_command.return_value': (0, out, '')})
    facts = HPUXNetwork(module)

# Generated at 2022-06-13 01:42:12.040196
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    HPUXNetworkCollector()



# Generated at 2022-06-13 01:42:13.298418
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    assert HPUXNetworkCollector._platform is 'HP-UX'

# Generated at 2022-06-13 01:42:15.824806
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    module = HPUXNetworkCollector.load_module()
    iface = HPUXNetwork(module=module)
    assert iface is not None



# Generated at 2022-06-13 01:42:21.146717
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    module = AnsibleModule(argument_spec={}, supports_check_mode=True)
    hpux_network = HPUXNetwork(module=module)
    if hpux_network.platform != 'HP-UX':
        raise Exception("Platform is not HP-UX")

    keys = ['interfaces', 'default_interface', 'default_gateway']
    network_facts = hpux_network.populate()
    for key in keys:
        if key not in network_facts:
            raise Exception("Key %s is missing in network facts %s" %
                            (key, network_facts))


# Generated at 2022-06-13 01:42:29.213566
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    """This test case verifies that HPUXNetworkCollector is subclass of NetworkCollector class and instantiates all objects correctly.
    """
    network_collector = HPUXNetworkCollector()
    assert isinstance(network_collector, NetworkCollector), "HPUXNetworkCollector object is not instance of NetworkCollector"
    assert isinstance(network_collector._fact_class, HPUXNetwork), "HPUXNetworkCollector._fact_class object is not instance of HPUXNetwork"
    assert network_collector._platform == 'HP-UX', "HPUXNetworkCollector._platform is not equal to HP-UX"


# Generated at 2022-06-13 01:42:33.727454
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    """
    Create an instance of HPUXNetwork and verify if the default_gateway,
    default_interface, interfaces, interface_<name> dictionaries are
    created correctly.
    """
    hpux_network_collector = HPUXNetworkCollector()
    hpux_network = HPUXNetwork(hpux_network_collector.module)
    hpux_network.get_default_interfaces()
    hpux_network.get_interfaces_info()
    hpux_network.populate()
    assert hpux_network.network_facts['interfaces'] == ['lan0']

# Generated at 2022-06-13 01:42:35.059503
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    c = HPUXNetworkCollector()
    assert c.platform == 'HP-UX'
    assert c._fact_class.platform == 'HP-UX'


# Generated at 2022-06-13 01:43:03.661060
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    """
    Test returns correct default interface and gateway
    """
    network = HPUXNetwork()
    network.module = MockModule()
    network.module.run_command.return_value = (0,
                                               'default 192.168.100.1 UG 2 0 lan0\n',
                                               '')
    default_interfaces = network.get_default_interfaces()
    assert default_interfaces['default_interface'] == 'lan0'
    assert default_interfaces['default_gateway'] == '192.168.100.1'


# Generated at 2022-06-13 01:43:12.996289
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    from ansible_collections.ansible.community.plugins.module_utils.facts.network.hpux.facts import Network

    this_network = HPUXNetwork()
    default_interfaces = this_network.get_default_interfaces()
    interfaces = this_network.get_interfaces_info()

    default_interface = default_interfaces['default_interface']
    default_gateway = default_interfaces['default_gateway']

    network_facts = this_network.populate()

    assert network_facts['default_interface'] == default_interface
    assert network_facts['default_gateway'] == default_gateway
    assert network_facts['interfaces'] == interfaces.keys()

# Generated at 2022-06-13 01:43:14.975450
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    obj = HPUXNetworkCollector()
    assert obj._fact_class is HPUXNetwork
    assert obj._platform == 'HP-UX'


# Generated at 2022-06-13 01:43:25.885412
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    module = NetworkCollector(dict(gather_subset=['network']))
    module.get_bin_path = lambda _: '/usr/bin/netstat'
    module.run_command = lambda _: (0, 'default 192.168.1.1 UG 1 0 lan0\n'
                                         'lan0        192.168.1.1  192.168.1.0         UHLWI  0  0  0 lan0', '')
    facts = module.gather_facts()
    assert 'network' in facts.keys()
    assert facts['network']['default_interface'] == 'lan0'
    assert facts['network']['default_gateway'] == '192.168.1.1'
    assert 'lan0' in facts['network']['interfaces']

# Generated at 2022-06-13 01:43:28.322904
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    module = FakeModule()
    nc = HPUXNetworkCollector(module)

    assert nc.module == module
    assert nc.platform == 'HP-UX'


# Generated at 2022-06-13 01:43:30.317688
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    # Test the constructor of HPUXNetworkCollector class
    hn = HPUXNetworkCollector()
    assert hn.__class__.__name__ == 'HPUXNetworkCollector'


# Generated at 2022-06-13 01:43:38.142765
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    import os
    import re
    import unittest

    class TestHPUXNetwork(unittest.TestCase):
        def setUp(self):
            self.hpux_network = HPUXNetwork()

        def test_get_default_interfaces(self):
            """
            Test get_default_interfaces() function of class HPUXNetwork.
            """
            # netstat -nr output

# Generated at 2022-06-13 01:43:47.617883
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    m = HPUXNetwork(FakeModule('/usr/bin/netstat',
                               '/usr/bin/netstat -niw'))
    interfaces = m.get_interfaces_info()
    assert len(interfaces.keys()) == 1
    assert 'lan0' in interfaces
    assert len(interfaces['lan0'].keys()) == 2
    assert 'ipv4' in interfaces['lan0']
    assert 'device' in interfaces['lan0']
    assert 'address' in interfaces['lan0']['ipv4']
    assert interfaces['lan0']['ipv4']['address'] == '15.12.243.60'



# Generated at 2022-06-13 01:43:55.426334
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    module = AnsibleModule(
        argument_spec=dict(
            gather_subset=dict(default=['!all'], type='list')
        ),
        supports_check_mode=True)

    hpux_network = HPUXNetwork(module=module)

    out = hpux_network.get_interfaces_info()
    assert out['lan0'] == {'device': 'lan0',
                           'ipv4': {'address': '192.168.40.25',
                                    'network': '192.168.40.0',
                                    'interface': 'lan0'}
                           }

# Generated at 2022-06-13 01:44:01.036355
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    interfaces = {'lan1': {
        'device': 'lan1',
        'ipv4': {
            'address': '00:08:9b:40:aa:ea',
            'interface': 'lan1',
            'network': '1'
        }
    }}
    assert HPUXNetwork().get_interfaces_info() == interfaces
    return True

# Generated at 2022-06-13 01:45:09.222788
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    nw_info = HPUXNetwork.get_interfaces_info()
    if nw_info == '':
        assert 'test_HPUXNetwork_get_interfaces_info failed!'
    else:
        assert 'test_HPUXNetwork_get_interfaces_info passed!'

# Generated at 2022-06-13 01:45:10.819384
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    network_facts = HPUXNetwork()
    assert network_facts.platform == 'HP-UX'

# Generated at 2022-06-13 01:45:13.377951
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    network_facts = HPUXNetwork()
    assert isinstance(network_facts, Network)
    assert isinstance(network_facts, HPUXNetwork)

# Generated at 2022-06-13 01:45:15.036935
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    """Unit test for constructor of class HPUXNetwork."""
    network = HPUXNetwork()
    assert network.platform == 'HP-UX'

# Generated at 2022-06-13 01:45:26.094954
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    from ansible.module_utils.facts.network.hpux.hpuxnetwork import HPUXNetwork
    from ansible.module_utils.facts.network.base import NetworkCollector
    from ansible.module_utils import basic
    from ansible.compat.tests import unittest
    from ansible.module_utils._text import to_bytes

    module = basic.AnsibleModule(argument_spec={})
    module.run_command = run_command_mock
    module.get_bin_path = get_bin_path_mock

    inet_collector = HPUXNetwork(module)
    interfaces_facts = inet_collector.populate()

# Generated at 2022-06-13 01:45:28.823008
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    networkfact = HPUXNetworkCollector()
    assert networkfact._platform == 'HP-UX'

# Generated at 2022-06-13 01:45:33.958592
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    interfaces = {'lan0': {'ipv4': {'address': '10.0.2.15',
                                    'interface': 'lan0',
                                    'network': '10.0.2'},
                           'device': 'lan0'}}
    hpux_network = HPUXNetwork()
    assert hpux_network.get_interfaces_info() == interfaces



# Generated at 2022-06-13 01:45:38.693174
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    interfaces = HPUXNetwork().get_interfaces_info()
    assert len(interfaces.keys()) > 0
    assert 'lan0' in interfaces.keys()
    assert 'ipv4' in interfaces['lan0'].keys()
    assert 'address' in interfaces['lan0']['ipv4'].keys()
    assert 'network' in interfaces['lan0']['ipv4'].keys()
    assert 'interface' in interfaces['lan0']['ipv4'].keys()

# Generated at 2022-06-13 01:45:40.758270
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    """ Unit test for constructor of class HPUXNetworkCollector"""
    HPUXNw = HPUXNetworkCollector()

    assert HPUXNw is not None

# Generated at 2022-06-13 01:45:47.398240
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    """ Unit test for method get_interfaces_info of class HPUXNetwork """
    test_obj = HPUXNetwork()
    rc, out, err = test_obj.module.run_command("/usr/bin/netstat -niw")
    test_obj.get_interfaces_info()
    assert rc == 0
    assert out == "/usr/bin/netstat: stat: No such file or directory"
    assert err == "/usr/bin/netstat: stat: No such file or directory"