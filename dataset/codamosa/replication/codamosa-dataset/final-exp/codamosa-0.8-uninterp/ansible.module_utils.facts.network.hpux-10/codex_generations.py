

# Generated at 2022-06-13 01:37:49.296619
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    hpx_nw = HPUXNetwork()
    assert hpx_nw is not None
    assert hpx_nw.platform == 'HP-UX'



# Generated at 2022-06-13 01:38:00.298001
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    this_module = sys.modules[__name__]
    test_module = AnsibleModule(argument_spec={})
    setattr(test_module, 'run_command', this_module.fake_run_command)
    setattr(test_module, 'get_bin_path', this_module.fake_get_bin_path)
    net_ins = HPUXNetwork(test_module)
    interfaces = net_ins.get_interfaces_info()

    assert interfaces['lan0']['device'] == 'lan0'
    assert interfaces['lan0']['ipv4']['network'] == '172.16.0.0'
    assert interfaces['lan0']['ipv4']['address'] == '172.16.1.210'

# Generated at 2022-06-13 01:38:10.071014
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    class MockModule(object):
        def run_command(self):
            out = ('Kernel IP routing table\n'
                   'Destination        Gateway          Flags   Refs     Use      Interface\n'
                   'default            192.168.10.1     UG          0       0        lan0\n'
                   '127.0.0.1          127.0.0.1        UH          0       0    lo0\n')
            return 0, out, None

    class HPUXNetworkTest(object):
        def __init__(self):
            self.module = MockModule()

    hpux_network_test = HPUXNetworkTest()

    network_facts = hpux_network_test.get_default_interfaces()

# Generated at 2022-06-13 01:38:11.535268
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    t = HPUXNetworkCollector()
    assert t._platform == 'HP-UX'
    assert t._fact_class == HPUXNetwork


# Generated at 2022-06-13 01:38:16.783098
# Unit test for method populate of class HPUXNetwork

# Generated at 2022-06-13 01:38:27.226637
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    def run_command(self, args):
        out = "/usr/bin/netstat -nr\n" +\
              "Routing tables\n" +\
              "destination         gateway         mask         interface        flags refs use if\n" +\
              "default            172.16.10.1      255.255.255.0  lan10            UG        0  604 lan10\n" +\
              "127/8               127.0.0.1        127.0.0.0      lo0              UH        1  817 lo0\n" +\
              "172.16.10/24        172.16.10.2      255.255.255.0  lan10            U         0  814 lan10\n"
        err = "Bad route to host\n"
        rc = 0
       

# Generated at 2022-06-13 01:38:32.407104
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    module = FakeModule(Platform='HP-UX',
                        Command="/usr/bin/netstat -nr")
    hpux_network = HPUXNetwork(module)
    default_interfaces_facts = hpux_network.get_default_interfaces()
    assert default_interfaces_facts['default_interface'] == 'lan0'
    assert default_interfaces_facts['default_gateway'] == '192.168.1.1'

# Generated at 2022-06-13 01:38:39.775351
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    network_collector = HPUXNetworkCollector()
    assert network_collector.platform == "HP-UX"
    assert type(network_collector.default_interface()) is dict
    assert type(network_collector.interfaces()) is dict
    assert type(network_collector.default_interface_facts()) is dict
    assert type(network_collector.interfaces_facts()) is dict
    assert type(network_collector.interfaces_ifaddresses()) is dict

# Generated at 2022-06-13 01:38:51.257828
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    import os
    import sys
    if sys.version_info[0] >= 3:
        from io import StringIO
    else:
        from StringIO import StringIO
    from ansible.module_utils.facts import timeout


# Generated at 2022-06-13 01:39:00.301475
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    ansi_module = AnsibleModule(argument_spec={})
    net_collector = HPUXNetwork(ansi_module)
    assert net_collector.module == ansi_module
    assert net_collector.platform == "HP-UX"
    assert net_collector.network_providers == []
    assert net_collector.facts == {}
    assert net_collector.legacy_warnings == []
    assert net_collector.providers_supported == []
    assert net_collector.providers_configured == []
    assert net_collector.ignored_providers == []


# Generated at 2022-06-13 01:39:09.491845
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    nck = HPUXNetwork()
    assert nck.platform == 'HP-UX'
    assert nck._platform == 'HP-UX'
    assert nck.get_default_interfaces() is not None
    assert nck.get_interfaces_info() is not None

# Generated at 2022-06-13 01:39:20.692553
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    module = MockModule()
    network = HPUXNetwork(module=module)
    network.populate()
    assert 'default_interface' in network.facts
    assert network.facts['default_interface'] == 'lan0'
    assert 'interfaces' in network.facts
    assert 'lan0' in network.facts['interfaces']
    assert 'ipv4' in network.facts['lan0']
    assert 'address' in network.facts['lan0']['ipv4']
    assert network.facts['lan0']['ipv4']['address'] == '127.0.0.1'
    assert 'network' in network.facts['lan0']['ipv4']
    assert network.facts['lan0']['ipv4']['network'] == '127.0.0.0'

# Generated at 2022-06-13 01:39:27.305350
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    from ansible.module_utils.facts.utils import get_file_content
    file_name = '../../../lib/ansible/module_utils/facts/network/hpux.py'
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    hpux = HPUXNetwork(file_path=file_path)

    # Test case 1: No interfaces
    expected_result = {}
    netstat_out = get_file_content('hpux_netstat_niw_1.out')
    result = hpux.get_interfaces_info(netstat_out)
    assert(result == expected_result)

    # Test case 2: Multiple interfaces

# Generated at 2022-06-13 01:39:29.657440
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    class module():
        def get_bin_path(self, arg):
            return None
    obj = HPUXNetwork(module)
    assert isinstance(obj, HPUXNetwork)


# Generated at 2022-06-13 01:39:30.968937
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    h = HPUXNetworkCollector()
    assert(h.show_custom_facts() == HPUXNetwork(''))

# Generated at 2022-06-13 01:39:34.903807
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    module = AnsibleModule(argument_spec={})
    network_collector = HPUXNetworkCollector(module=module)
    network_collector.collect()
    network_facts = network_collector.get_facts()
    assert 'default_interface' in network_facts
    assert 'default_gateway' in network_facts
    assert 'interfaces' in network_facts
    interface_facts = network_facts['default_interface']
    assert 'ipv4' in interface_facts

# Generated at 2022-06-13 01:39:36.646588
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    NetworkCollector = HPUXNetworkCollector()
    assert(str(type(NetworkCollector._fact_class)) == "<class 'ansible.module_utils.facts.network.hpux.HPUXNetwork'>")
    assert(NetworkCollector._platform == 'HP-UX')

# Generated at 2022-06-13 01:39:37.406748
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    HPUXNetworkCollector()

# Generated at 2022-06-13 01:39:39.439109
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    network = HPUXNetwork()
    network.populate()

# Generated at 2022-06-13 01:39:48.792688
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    net = HPUXNetwork()
    m = MockTestModule()
    net.module = m

# Generated at 2022-06-13 01:40:04.707932
# Unit test for method get_default_interfaces of class HPUXNetwork

# Generated at 2022-06-13 01:40:07.853774
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    # create an object of class HPUXNetworkCollector
    obj = HPUXNetworkCollector()
    assert obj.platform == 'HP-UX'
    assert obj.fact_class == HPUXNetwork


# Generated at 2022-06-13 01:40:12.348293
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    module = DummyAnsibleModule()
    network = HPUXNetwork(module)
    network.module.run_command = run_command
    default_interfaces = network.get_default_interfaces()
    assert default_interfaces == {'default_gateway': '172.17.0.1', 'default_interface': 'lan0'}



# Generated at 2022-06-13 01:40:19.847072
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    """
    Test for method HPUXNetwork.get_interfaces_info
    of class HPUXNetwork
    """
    # This is the output of '/usr/bin/netstat -niw' on HP-UX 11.11

# Generated at 2022-06-13 01:40:29.917346
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    # Creating instance of class HPUXNetwork
    network_facts = HPUXNetwork()

    # Creating facts for netstat result
    netstat_stdout = """
default  172.16.0.1 UG   1  0     lan0
172.16.0.0       172.16.0.209 U   1   0 lan0
"""

    # Creating mocked module object
    module_mock = MagicMock()

    # Creating mocked module object
    module_mock.run_command.return_value = (0, netstat_stdout, '')

    # Creating mocked module object
    module_mock.get_bin_path.return_value = '/usr/bin/netstat'

    # Assigning mocked module object
    network_facts.module = module_mock

    # Calling populate method
    network_facts.pop

# Generated at 2022-06-13 01:40:36.692694
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    '''
    Unit test for constructor of class HPUXNetworkCollector
    '''
    fact_class = HPUXNetworkCollector._fact_class
    platform = HPUXNetworkCollector._platform
    hpu_net_col = HPUXNetworkCollector()
    assert hpu_net_col
    assert hpu_net_col._fact_class == fact_class
    assert hpu_net_col._platform == platform


# Generated at 2022-06-13 01:40:38.528080
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    hn = HPUXNetwork()
    assert hn.populate() is not None

# Generated at 2022-06-13 01:40:45.361867
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    module = AnsibleModule(argument_spec={}, supports_check_mode=True)
    hpux_network = HPUXNetwork(module)
    hpux_network.populate()
    assert hpux_network.default_interface == u'lan0'
    assert hpux_network.default_gateway == u'172.16.0.1'
    assert hpux_network.interfaces[0] == u'lan0'
    assert hpux_network.lan0['ipv4']['address'] == u'172.16.0.20'
    assert hpux_network.lan0['ipv4']['network'] == u'172.16.0.0'
    assert hpux_network.lan0['ipv4']['interface'] == u'lan0'

# Generated at 2022-06-13 01:40:48.932132
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    module = MockNetworkModule()
    network = HPUXNetwork(module)
    result = network.get_default_interfaces()
    assert result.has_key('default_interface')
    assert result.has_key('default_gateway')



# Generated at 2022-06-13 01:40:53.696803
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    testmodule = None
    network = HPUXNetwork(testmodule)
    output = network.get_default_interfaces()

    # Should return something like this
    # {'default_gateway': '172.16.14.1', 'default_interface': 'lan0'}
    assert output['default_interface'][:3] == 'lan'
    assert output['default_gateway'][:3] == '172'


# Generated at 2022-06-13 01:41:14.924377
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    HPUXNetworkCollector()

# Generated at 2022-06-13 01:41:23.033547
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    saved_run_command = __import__('ansible.module_utils.facts.network.hpux',
                                   globals(), locals(), ['run_command']).run_command
    expected_default_interfaces = {'default_gateway': '172.18.57.254',
                                   'default_interface': 'lan0'}
    __import__('ansible.module_utils.facts.network.hpux',
                globals(), locals(), ['run_command']).run_command = \
        lambda cmd: (0, '172.18.57.254 lan0', '')
    default_interfaces = HPUXNetwork().get_default_interfaces()
    __import__('ansible.module_utils.facts.network.hpux',
                globals(), locals(), ['run_command']).run_command = saved_run_

# Generated at 2022-06-13 01:41:25.745724
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    collector = HPUXNetworkCollector()
    assert collector._fact_class == HPUXNetwork
    assert collector._platform == 'HP-UX'

# Generated at 2022-06-13 01:41:27.891925
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    """
    Method:
      HPUXNetwork.get_interfaces_info

    Output:
      List of interfaces
    """
    hpux_network = HPUXNetwork()
    output = hpux_network.get_interfaces_info()
    assert isinstance(output, dict)



# Generated at 2022-06-13 01:41:35.600650
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    module = MockModule({'ANSIBLE_MODULE_ARGS': {'filter': 'ipv4'}})
    network = HPUXNetwork(module)
    network.module.run_command = Mock(return_value=(0,
                                                    "lan0 lan1",
                                                    ""))
    network.get_interfaces_info = Mock(return_value=
                                   {'lan0': {'device': 'lan0'},
                                    'lan1': {'device': 'lan1'}})
    network.get_default_interfaces = Mock(return_value=
                                          {'default_interface': 'lan0',
                                           'default_gateway': '1.1.1.1'})
    network_facts = network.populate()

# Generated at 2022-06-13 01:41:39.729479
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )
    nm = HPUXNetwork(module)
    nm.populate()



# Generated at 2022-06-13 01:41:45.212112
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    net = HPUXNetwork()
    net.module = MagicMock()
    net.module.run_command.return_value = (0,
                                           "default 0.0.0.0          172.31.128.2        UG         lan0",
                                           None)
    facts = net.get_default_interfaces()
    assert facts == {'default_interface': 'lan0', 'default_gateway': '172.31.128.2'}



# Generated at 2022-06-13 01:41:53.786286
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    sample_out = "default 192.168.1.254 UGSc 1 0 lan0 192.168.1.0 USc 0 0 lan0 127.0.0.1 UCS 0 0 lo0"
    expected_default_gateway = "192.168.1.254"
    expected_default_interface = "lan0"
    net = HPUXNetwork(module=None)
    default_interfaces = net.get_default_interfaces()
    assert default_interfaces['default_gateway'] == expected_default_gateway
    assert default_interfaces['default_interface'] == expected_default_interface



# Generated at 2022-06-13 01:42:02.447450
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    from ansible.module_utils.facts.network.hpux import HPUXNetwork
    from ansible.module_utils.facts.network.base import Network
    from ansible.module_utils import basic
    module = basic.AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )
    network = HPUXNetwork(module)
    collected_facts = Network.populate(network)
    interfaces = collected_facts['interfaces']
    for interface in interfaces:
        assert type(interface) is str
        assert interface == collected_facts[interface]['device']

# Generated at 2022-06-13 01:42:09.225001
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    class TestModule():
        def __init__(self):
            self.params = dict()

        def run_command(self, cmd):
            return 0, "lan0 0 0 127.0.0.1 127.0.0.1 UGHS 0 0 0 lo0 127.0.0.1 127.0.0.1 UH 2 0 0 ", ""

    obj = HPUXNetwork(TestModule())
    interfaces_info = obj.get_interfaces_info()
    assert interfaces_info == {'lan0': {'ipv4': {'interface': 'lan0', 'address': '127.0.0.1', 'network': '127.0.0.1'}, 'device': 'lan0'}}

# Generated at 2022-06-13 01:42:51.297158
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    assert HPUXNetworkCollector._platform == 'HP-UX'
    assert HPUXNetworkCollector._fact_class == HPUXNetwork


# Generated at 2022-06-13 01:42:55.638567
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    from ansible.module_utils.facts.network.hpux import HPUXNetwork
    hw = HPUXNetwork()
    output = hw.get_interfaces_info()
    for k, v in output.items():
        print(k, v)

# Generated at 2022-06-13 01:43:04.681311
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    from ansible.module_utils.facts.network.hpux import HPUXNetwork
    from units.mock.proc import MockProcessor, MockConnection
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils.facts.network.hpux import HPUXNetworkCollector

    class MockModule(object):
        def __init__(self):
            self.params = {}
            self.connection = MockConnection()

        def get_bin_path(self, name, optional=False):
            return name

    module = MockModule()
    hpux_network = HPUXNetwork(module)

# Generated at 2022-06-13 01:43:06.317312
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    t = HPUXNetwork()
    assert t.platform == 'HP-UX'

# Generated at 2022-06-13 01:43:14.860442
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )
    fact = HPUXNetwork(module)

# Generated at 2022-06-13 01:43:20.483850
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    test_module = AnsibleModule(
        argument_spec={})
    test_network = HPUXNetwork(test_module)
    result = test_network.populate()

# Generated at 2022-06-13 01:43:29.301024
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    collector = HPUXNetworkCollector()
    assert collector.__class__.__name__ == "HPUXNetworkCollector"
    assert collector._platform == "HP-UX"
    assert collector._fact_class == HPUXNetwork

    rc, out, err = collector.module.run_command("/usr/bin/netstat -nr")
    lines = out.splitlines()
    for line in lines:
        words = line.split()
        if len(words) > 1:
            if words[0] == 'default':
                default_interface = words[4]

    rc, out, err = collector.module.run_command("/usr/bin/netstat -niw")
    lines = out.splitlines()
    for line in lines:
        words = line.split()

# Generated at 2022-06-13 01:43:32.083998
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    hduxNetwork = HPUXNetwork()
    assert hduxNetwork.interfaces == ['lan0', 'lan1']


# Generated at 2022-06-13 01:43:38.600386
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    net = HPUXNetwork()
    out = """lan0         link#1                          UP    1000baseT <Full-duplex,Flow-control,MII,100Mbps>
lan0        129.71.137.37            255.255.255.0   U     1 0          0 lan0
lan1         link#2                          UP    1000baseT <Full-duplex,Flow-control,MII,100Mbps>
lan1        129.71.137.85            255.255.255.0   U     1 0          0 lan1
lo0          link#3                          UP    1000baseT <>
lo0          127.0.0.1                127.0.0.1      U     16 384       0 lo0
lo0          ::1                      ::1            U     256 0        0 lo0
"""
    rc = 0
   

# Generated at 2022-06-13 01:43:44.982546
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    module = AnsibleModuleMock()
    network = HPUXNetwork(module=module)
    rc, out, err = module.run_command("/usr/bin/netstat -niw")
    default_interfaces = network.get_default_interfaces()
    assert default_interfaces['default_interface'] == 'lan1'
    assert default_interfaces['default_gateway'] == '10.15.1.1'


# Generated at 2022-06-13 01:45:44.500125
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts import collector

    module = basic.AnsibleModule(
        argument_spec={},
        supports_check_mode=False
    )

    hpuxnetwork_collector = HPUXNetworkCollector(module=module,
                                                 collected_facts={})
    hpuxnetwork = HPUXNetwork(hpuxnetwork_collector)
    module.run_command = hpuxnetwork.run_command
    interfaces = hpuxnetwork.get_interfaces_info()
    assert interfaces['lan0']['ipv4']['network'] == to_bytes('172.16.92.0')

# Generated at 2022-06-13 01:45:50.089567
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    sample_input = '''
default  128.130.1.2     UG   0   0  lan0
    '''
    module = FakeModule()
    module.run_command = lambda command: (0, sample_input, '')
    h = HPUXNetwork(module)
    d = h.get_default_interfaces()
    assert d['default_gateway'] == '128.130.1.2'
    assert d['default_interface'] == 'lan0'


# Generated at 2022-06-13 01:45:56.945607
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=False)
    module.run_command = MagicMock(return_value=(0, '', ''))
    module.get_bin_path = MagicMock(return_value='')
    network = HPUXNetwork(module)
    network.get_default_interfaces = MagicMock(
        return_value={'default_interface': 'lan0', 'default_gateway': '10.0.2.2'})

# Generated at 2022-06-13 01:45:59.722762
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    module = AnsibleModule()
    network_module = HPUXNetwork(module)
    network_module.populate()



# Generated at 2022-06-13 01:46:08.955306
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    """
    Unit test for method populate of class HPUXNetwork
    """
    class MockModule(object):
        def run_command(self, command):
            """
            Mocking method run_command.
            """
            if command == "/usr/bin/netstat -nr":
                return (0, "default  10.144.170.1     UG   lan0", "")
            elif command == "/usr/bin/netstat -niw":
                return (0, "lan0      link#3        192.168.1.0   U 1000   0   0 lan0", "")
            elif command == "/usr/bin/netstat -niw":
                return (0, "lan0      link#3        192.168.1.0   U 1000   0   0 lan0", "")


# Generated at 2022-06-13 01:46:15.367806
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    out = """default 192.168.1.1 USNK 0 0 - -""".strip()
    module = MockModule(out, err='', rc=0)
    network = HPUXNetwork(module=module)
    interfaces = network.get_default_interfaces()
    assert interfaces == {'default_interface': 'USNK',
                          'default_gateway': '192.168.1.1'}


# Generated at 2022-06-13 01:46:16.504281
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    hn = HPUXNetworkCollector()
    assert hn.facts is None

# Generated at 2022-06-13 01:46:23.285247
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    lans = {
        'lan0': '0x00010014',
        'lan0.188': '0x00010015',
        'lan1': '0x00010016',
        'lan1.138': '0x00010017',
        'lan1.189': '0x00010018',
        'lan2': '0x00010019',
        'lan2.103': '0x0001001a',
        'lan2.130': '0x0001001b',
        'lan2.136': '0x0001001c',
        'lan2.187': '0x0001001d',
        'lan2.193': '0x0001001e',

    }


# Generated at 2022-06-13 01:46:28.586963
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    m = MockModule()
    n = HPUXNetwork(m)
    n._execute_module = n.module.run_command
    out = '''default 127.0.0.1 UGSc       0      0        lo0
default 151.101.0.0 UGH        0      0       lan0
'''
    n.run_command = lambda x: (0, out, '')
    assert n.get_default_interfaces() == {'default_interface': 'lan0', 'default_gateway': '151.101.0.0'}


# Generated at 2022-06-13 01:46:29.958453
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    HPUXNetworkCollector()