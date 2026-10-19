

# Generated at 2022-06-13 01:37:52.286076
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    module = AnsibleModuleMock()
    hpuxnet = HPUXNetwork(module)

    # default interface lan0.
    lan0 = (0, 'default  192.168.0.1 UG        0 0         lan0', '')
    module.run_command.side_effect = [lan0]
    interfaces = hpuxnet.get_default_interfaces()
    assert interfaces['default_interface'] == 'lan0'
    assert interfaces['default_gateway'] == '192.168.0.1'

    # default interface lan1.
    lan1 = (0, 'default  192.168.0.1 UG        0 0         lan1', '')
    module.run_command.side_effect = [lan1]
    interfaces = hpuxnet.get_default_interfaces()

# Generated at 2022-06-13 01:37:56.975812
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    HPN = HPUXNetwork
    test_get_default_interfaces = HPN.get_default_interfaces(HPN)
    assert test_get_default_interfaces == {'default_interface': 'lan0',
                                           'default_gateway': '172.16.1.1'}

# Generated at 2022-06-13 01:38:04.589042
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    module_mock = Mock()
    module_mock.run_command = Mock(return_value=(0, "", ""))
    module_mock.get_bin_path = Mock(return_value="/usr/bin/netstat")
    network = HPUXNetwork(module_mock)
    net_facts = network.populate()
    assert net_facts['default_interface'] == 'lan0'
    assert net_facts['default_gateway'] == '127.0.0.1'

# Generated at 2022-06-13 01:38:06.082596
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    assert HPUXNetwork


# Generated at 2022-06-13 01:38:09.542227
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    obj = HPUXNetworkCollector()
    assert obj.platform == 'HP-UX'
    assert obj._fact_class == HPUXNetwork
    assert obj.gather_network_facts() == {}

# Generated at 2022-06-13 01:38:14.392828
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():

    module = MockModule()
    module.run_command.return_value = (1, 'default 192.168.0.1 UGS en0', '')

    fact = HPUXNetwork(module)
    default_interfaces = fact.get_default_interfaces()

    assert default_interfaces['default_interface'] == 'en0'
    assert default_interfaces['default_gateway'] == '192.168.0.1'



# Generated at 2022-06-13 01:38:18.865394
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    module = AnsibleModule(
        argument_spec={},
        supports_check_mode=True,
    )
    hpux = HPUXNetwork(module)

    assert hpux.platform == 'HP-UX'


# Generated at 2022-06-13 01:38:28.329712
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    import re

    # mock module class

# Generated at 2022-06-13 01:38:38.997368
# Unit test for method get_interfaces_info of class HPUXNetwork

# Generated at 2022-06-13 01:38:47.459909
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    test_module = AnsibleModuleHelper(HPUXNetwork)
    setattr(test_module, 'run_command',
            lambda *args, **kwargs: (0,
                                     'default         192.168.2.253 UGS lan0',
                                     ''))
    network = HPUXNetwork(module=test_module)
    expected = {'default_gateway': '192.168.2.253',
                'default_interface': 'lan0'}
    result = network.get_default_interfaces()
    assert result == expected


# Generated at 2022-06-13 01:38:59.274026
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    test_module = AnsibleModule(argument_spec=dict())
    test_network = HPUXNetwork(test_module)
    test_module.run_command = Mock(return_value=(0, "default 192.168.60.254 UG lan0", ""))
    result = test_network.get_default_interfaces()
    assert result == {'default_interface': 'lan0',
                      'default_gateway': '192.168.60.254'}


# Generated at 2022-06-13 01:39:09.818609
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    from unittest import TestCase, mock
    from ..hpux import HPUXNetwork

    f = HPUXNetwork({})
    f.module = mock.Mock()

# Generated at 2022-06-13 01:39:15.632788
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    test_module = AnsibleModule(argument_spec={}, supports_check_mode=True)
    test_network = HPUXNetwork(module=test_module)
    default_interfaces_facts = test_network.get_default_interfaces()
    assert("default_interface" in default_interfaces_facts)
    assert("default_gateway" in default_interfaces_facts)


# Generated at 2022-06-13 01:39:19.223154
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    h = HPUXNetwork()
    assert h.platform == 'HP-UX'
    assert h.get_interfaces_info() is not None
    assert h.get_default_interfaces() is not None

# Generated at 2022-06-13 01:39:26.751884
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    module = AnsibleModule(argument_spec={})
    hpux_network = HPUXNetwork(module)
    collected_facts = {}
    collected_facts['default_interface'] = "lan2"
    collected_facts['default_gateway'] = "10.30.71.1"
    collected_facts['interfaces'] = ['lan0', 'lan1', 'lan2']
    collected_facts['lan0'] = {'device': 'lan0',
                               'ipv4': {'address': '10.30.71.146',
                                        'network': '10.30.71.0',
                                        'interface': 'lan0'}}

# Generated at 2022-06-13 01:39:28.198095
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    h = HPUXNetwork({})
    assert h.get_interfaces_info() is not None

# Generated at 2022-06-13 01:39:34.928897
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    interfaces = {}
    testout = "    IPv4\nLAN0        0.0.0.0         0.0.0.0         UP                                            LAN1        0.0.0.0         0.0.0.0         UP"
    lines = testout.splitlines()
    for line in lines:
        words = line.split()
        for i in range(len(words) - 1):
            if words[i][:3] == 'lan':
                device = words[i]
                interfaces[device] = {'device': device}
                address = words[i + 3]
                interfaces[device]['ipv4'] = {'address': address}
                network = words[i + 2]

# Generated at 2022-06-13 01:39:35.593452
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    HPUXNetworkCollector()

# Generated at 2022-06-13 01:39:36.630198
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    result = HPUXNetworkCollector()
    assert result is not None



# Generated at 2022-06-13 01:39:44.706165
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    from ansible.module_utils.facts import ansible_collector
    from ansible.module_utils.facts.network.hpu_ux import HPUXNetworkCollector
    from ansible.module_utils.facts.network.base import Network
    from ansible.module_utils._text import to_bytes

    mod = AnsibleModule(
        argument_spec=dict()
    )

    # Create a non-functioning Network object that doesn't fail
    # when the AnsibleModule object is created.
    class TestNetwork(Network):

        def populate(self, collected_facts=None):
            return {'test_fact': 'test_fact'}

    # Add a TestNetwork object to the network collector
    test_network_collector = HPUXNetworkCollector(mod)
    test_network_collector._fact_class = Test

# Generated at 2022-06-13 01:39:57.222032
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    """
    Constructor of class HPUXNetworkCollector should set
    _fact_class to HPUXNetwork
    """
    hn = HPUXNetworkCollector()
    assert hn._fact_class == HPUXNetwork

# Generated at 2022-06-13 01:39:59.250112
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    hn = HPUXNetworkCollector()
    assert hn.platform == 'HP-UX'
    assert not hn.gather_subset


# Generated at 2022-06-13 01:40:05.604272
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    # Create instance of class HPUXNetwork
    network = HPUXNetwork({})
    # the path to command '/usr/bin/netstat' is not set in environment variable
    # PATH, because Ansible is not installed.
    # Set the path explicitly
    network.bin_path = '/usr/bin'
    assert network.get_interfaces_info() == {}

# Generated at 2022-06-13 01:40:07.767451
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    obj = HPUXNetworkCollector()
    assert obj.platform == 'HP-UX'
    assert obj._fact_class == HPUXNetwork

# Generated at 2022-06-13 01:40:12.813982
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    testNetwork = HPUXNetwork()
    interfaces = testNetwork.get_interfaces_info()
    assert isinstance(interfaces, dict)
    assert 'lan0' in interfaces
    assert 'lan0' in interfaces['lan0']
    assert 'lan0' in interfaces['lan0']['ipv4']
    assert '127.0.0.1' in interfaces['lan0']['ipv4']


# Generated at 2022-06-13 01:40:13.930624
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    my_net = HPUXNetwork()
    assert my_net is not None

# Generated at 2022-06-13 01:40:16.409753
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    module = AnsibleModule(argument_spec={})
    hpux_network_facts = HPUXNetwork(module)
    assert hpux_network_facts.populate() is not None



# Generated at 2022-06-13 01:40:17.747892
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    collector = HPUXNetworkCollector()
    assert collector.platform == 'HP-UX'


# Generated at 2022-06-13 01:40:20.594543
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True)
    network_collector = HPUXNetworkCollector(module=module)

    assert network_collector._platform is not None
    assert network_collector._fact_class is not None



# Generated at 2022-06-13 01:40:30.633674
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    # empty facts passed
    network = HPUXNetwork(dict())
    # check_rc set to false because we don't care about the modules return code
    network.module = NetworkCollector.faked_module(check_rc=False)
    network.populate(dict())
    # check populated facts
    iface1 = {'ipv4': {'address': '172.27.255.1', 'network': '172.27.255.0',
                       'interface': 'lan0', 'netmask': '255.255.255.0'}}
    iface2 = {'ipv4': {'address': '172.27.255.2', 'network': '172.27.255.0',
                       'interface': 'lan1', 'netmask': '255.255.255.0'}}


# Generated at 2022-06-13 01:40:56.120764
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    """
    Unit test for method get_interfaces_info of class HPUXNetwork
    """

    class ModuleMock(object):
        """
        Mock class for Ansible module
        """
        def __init__(self):
            pass

        @staticmethod
        def run_command(command):
            """
            Function to run a command
            :param command: the command to run
            :return: tuple:rc, out, err
            """

# Generated at 2022-06-13 01:41:01.364954
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    net = HPUXNetwork()
    facts = net.populate()
    expected_keys = ['default_gateway',
                     'default_interface',
                     'interfaces']
    for key in expected_keys:
        assert key in facts
    expected_interfaces = ['lan0', 'lan1', 'lan2']
    assert isinstance(facts['interfaces'], list)
    for iface in facts['interfaces']:
        assert iface in expected_interfaces

# Generated at 2022-06-13 01:41:03.107216
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    assert HPUXNetworkCollector is not None and isinstance(HPUXNetworkCollector._fact_class, type)

# Generated at 2022-06-13 01:41:06.093439
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    obj = HPUXNetworkCollector()
    assert obj.platform == 'HP-UX'
    assert obj.fact_class == HPUXNetwork

# Generated at 2022-06-13 01:41:16.296460
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    default_interfaces = {'default_interface': 'lan0',
                          'default_gateway': '172.16.1.1'}

# Generated at 2022-06-13 01:41:17.822243
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    fact_subclass = HPUXNetworkCollector()
    assert fact_subclass._platform == 'HP-UX'

# Generated at 2022-06-13 01:41:20.004334
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    """
    Unit test for constructor of class HPUXNetwork
    """
    hn = HPUXNetwork()
    assert hn.platform == 'HP-UX'


# Generated at 2022-06-13 01:41:21.291397
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    test_obj = HPUXNetworkCollector()
    assert test_obj is not None


# Generated at 2022-06-13 01:41:22.541269
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    network = HPUXNetwork({})
    assert network


# Generated at 2022-06-13 01:41:31.143320
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    netstat_path = "/usr/bin/netstat"
    context = MockContext(netstat_path)
    hpu = HPUXNetwork(context)
    hpu._module.run_command = MockMethod(['default  12.34.56.78     UC         E2    -   2  en0',
                                          'default              UC  E2    -   2  lan0'])
    default_interfaces = hpu.get_default_interfaces()
    assert default_interfaces == {'default_interface': 'lan0', 'default_gateway': '12.34.56.78'}


# Base class for mocking

# Generated at 2022-06-13 01:42:09.465120
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    hpux_network_fact = HPUXNetworkCollector(dict(), dict())
    assert hpux_network_fact.platform == 'HP-UX'
    assert hpux_network_fact._fact_class == HPUXNetwork

# Generated at 2022-06-13 01:42:19.443674
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    class MockModule(object):
        def __init__(self, facts):
            self.facts = facts
            self.run_command_args_list = []
            self.run_command_calls = 0

        def get_bin_path(self, name):
            if name == 'netstat':
                return '/usr/bin/netstat'
            return None

        def run_command(self, args, check_rc=False):
            self.run_command_calls += 1
            self.run_command_args_list.append(args)

            if self.run_command_calls == 1:
                err = ''
                out = 'default 127.0.0.1 UGSc 127 1 0 lan0'
                rc = 0
                return rc, out, err

# Generated at 2022-06-13 01:42:29.559521
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    import os
    import platform

    def os_environ_patch(self, attr):
        if attr == 'PATH':
            return '/usr/bin:/bin'
        elif attr == 'ANSIBLE_NET_IFACES_CACHE_DIR':
            return os.path.join(os.path.dirname(__file__), '../../../test/units/module_utils/network/hpux/cache')
        else:
            return os.environ[attr]

    def command_runner_patch(self, cmd, *args, **kwargs):
        pattern = '/usr/bin/netstat -nr'

# Generated at 2022-06-13 01:42:34.237807
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    h = HPUXNetworkCollector(None, None)
    assert h.platform == 'HP-UX'
    assert h._fact_class == HPUXNetwork

# Generated at 2022-06-13 01:42:36.691562
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    network_collector = HPUXNetworkCollector()
    assert network_collector.platform == "HP-UX"
    assert network_collector._fact_class == HPUXNetwork

# Generated at 2022-06-13 01:42:40.946236
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    module = AnsibleModule(argument_spec={})
    test_obj = HPUXNetwork(module)
    test_out = test_obj.get_interfaces_info()
    result = {'lan0': {'device': 'lan0',
                       'ipv4': {'network': '172.22.222.0',
                       'interface': 'lan0',
                       'address': '172.22.222.101'}}}
    assert test_out == result


# Generated at 2022-06-13 01:42:45.673034
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    net_collector = HPUXNetworkCollector()
    assert net_collector._fact_class == HPUXNetwork
    assert net_collector._platform == 'HP-UX'

# Generated at 2022-06-13 01:42:51.989817
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    network = HPUXNetwork()
    network.module = FakeAnsibleModule()
    network.module.run_command = FakeRunCommand(
        'default',
        "default 10.77.77.1 UGSc 6 1690 lan0")
    default_interfaces_facts = network.get_default_interfaces()
    assert default_interfaces_facts['default_gateway'] == '10.77.77.1'
    assert default_interfaces_facts['default_interface'] == 'lan0'



# Generated at 2022-06-13 01:42:54.481957
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    hpux_network = HPUXNetwork()
    assert hpux_network.platform == 'HP-UX'

# Generated at 2022-06-13 01:42:56.005689
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    network = HPUXNetwork()
    assert network.platform == 'HP-UX'


# Generated at 2022-06-13 01:44:18.660539
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    """
    Create an instance of HPUXNetworkCollector
    """
    net_coll = HPUXNetworkCollector()
    assert net_coll._platform == 'HP-UX'

# Generated at 2022-06-13 01:44:21.557903
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    fact_network = HPUXNetworkCollector()
    assert fact_network.platform == "HP-UX"
    assert fact_network._fact_class is HPUXNetwork



# Generated at 2022-06-13 01:44:24.255941
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    """
    Simple test for constructor of class HPUXNetworkCollector
    """
    module = DummyAnsibleModule()
    collector = HPUXNetworkCollector(module=module)
    assert collector.module == module
    assert collector._platform == 'HP-UX'


# Generated at 2022-06-13 01:44:25.690489
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    obj = HPUXNetworkCollector()
    assert obj._fact_class == HPUXNetwork

# Generated at 2022-06-13 01:44:27.074923
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    HPUXNetwork()


# Generated at 2022-06-13 01:44:37.182526
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    import sys

    class TestModule(object):
        def __init__(self):
            pass


# Generated at 2022-06-13 01:44:44.932067
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    module = AnsibleModuleMock()
    module.run_command = run_command_mock
    network = HPUXNetwork(module)

# Generated at 2022-06-13 01:44:49.139374
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    module = HPUXNetworkCollector()
    assert module.platform == 'HP-UX'
    assert module._fact_class.platform == 'HP-UX'
    assert module.fact_subclass == 'network'
    assert module.fact_class_name == 'HPUXNetwork'

# Generated at 2022-06-13 01:44:52.284630
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    network_collector = HPUXNetworkCollector()
    assert isinstance(network_collector._fact_class, HPUXNetwork)
    assert isinstance(network_collector._platform, str)
    assert network_collector._platform == 'HP-UX'

# Generated at 2022-06-13 01:44:55.024999
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    hpux_network_collector = HPUXNetworkCollector()
    assert (hpux_network_collector.platform == 'HP-UX')
    assert (hpux_network_collector._fact_class == HPUXNetwork)

