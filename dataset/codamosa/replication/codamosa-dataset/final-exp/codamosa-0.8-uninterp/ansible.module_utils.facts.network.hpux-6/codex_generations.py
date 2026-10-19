

# Generated at 2022-06-13 01:37:53.799858
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    network = HPUXNetwork()
    network.module.run_command = MagicMock(
        side_effect=[(0, 'default 192.168.1.1 UG lan0', ''),
                     (0, '', "netstat: lan0: bad value"),
                     (0, '', 'mock error output')])

    network_facts = network.get_default_interfaces()
    assert network_facts['default_gateway'] == '192.168.1.1'
    assert network_facts['default_interface'] == 'lan0'

    network_facts = network.get_default_interfaces()

    assert not network_facts

    network_facts = network.get_default_interfaces()
    assert not network_facts



# Generated at 2022-06-13 01:37:59.153457
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    module = MockAnsibleModule()
    network = HPUXNetwork(module)
    network.module.run_command = Mock(
        return_value=(0, '', '')
    )
    network.get_default_interfaces()
    module.run_command.assert_called_once_with('/usr/bin/netstat -nr')


# Generated at 2022-06-13 01:38:05.763202
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    test_module = MockModule()
    test_module.run_command = Mock(return_value=(0, HP_NETSTAT_OUTPUT, ""))
    net = HPUXNetwork(test_module)
    default_routes = net.get_default_interfaces()
    assert default_routes == {'default_interface': 'lan0',
                              'default_gateway': '10.20.5.1'}



# Generated at 2022-06-13 01:38:08.207569
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    obj = HPUXNetworkCollector()
    assert obj.platform == 'HP-UX'


# Generated at 2022-06-13 01:38:12.850882
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    hpux_network = HPUXNetwork({}, dict(module=dict(run_command=run_command_mock)))
    # test populate
    hpux_network.populate()
    # test get_default_interfaces
    hpux_network.get_default_interfaces()
    # test get_interfaces_info
    hpux_network.get_interfaces_info()


# Generated at 2022-06-13 01:38:17.278820
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    test_data = {
        'lan0': {'device': 'lan0',
                 'ipv4': {'address': '10.10.10.10',
                          'network': '10.0.0.0',
                          'interface': 'lan0'}
                 },
        'lan1': {'device': 'lan1',
                 'ipv4': {'address': '10.10.10.10',
                          'network': '10.0.0.0',
                          'interface': 'lan1'}
                 },
    }
    obj = HPUXNetwork()
    data = obj.get_interfaces_info()
    assert data == test_data


# Generated at 2022-06-13 01:38:27.012254
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    class args():
        def __init__(self):
            self.run_command = run_command

    # Mock version of module.run_command
    def run_command(command):
        out = "default 192.168.0.254 UGS 0 0 0 lan0\n"
        err = ''
        rc = 0
        return rc, out, err

    # Create object of class HPUXNetwork and call
    # get_default_interfaces
    obj = HPUXNetwork(args())

    # Dict  of default_interface should have values.
    default_interfaces = obj.get_default_interfaces()
    assert 'default_interface' in default_interfaces
    assert 'default_gateway' in default_interfaces


# Generated at 2022-06-13 01:38:27.891536
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    assert HPUXNetwork is not None


# Generated at 2022-06-13 01:38:37.540673
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    # Create a class object
    test_obj = HPUXNetwork()
    # creating test dict
    test_dict = {'default_interface': 'lan0', 'default_gateway': '192.168.0.1', 'interfaces': ['lan0', 'lan1'], 'lan0': {'device': 'lan0', 'ipv4': {'network': '192.168.0.0', 'interface': 'lan0', 'address': '192.168.0.3'}}, 'lan1': {'device': 'lan1', 'ipv4': {'network': '172.16.20.0', 'interface': 'lan1', 'address': '172.16.20.2'}}}
    assert test_obj.populate() == test_dict

# Generated at 2022-06-13 01:38:48.664610
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    net = HPUXNetwork()
    ifaces = net.get_interfaces_info()
    assert 'lan0' in ifaces.keys()
    assert 'lan1' in ifaces.keys()
    assert 'lan0' in ifaces['lan0']['ipv4']['network']
    assert 'lan1' in ifaces['lan1']['ipv4']['network']
    assert '16.3.2.17' in ifaces['lan0']['ipv4']['address']
    assert '16.3.2.18' in ifaces['lan1']['ipv4']['address']
    assert 'lan0' in ifaces['lan0']['ipv4']['interface']

# Generated at 2022-06-13 01:38:59.715374
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    facts = HPUXNetwork()

# Generated at 2022-06-13 01:39:05.729185
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    hpxNetwork = HPUXNetwork()
    hpxNetwork.module.run_command = mock
    hpxNetwork.module.run_command.return_value = (0, 'default 192.168.0.1 UGDS 0 0 en3', '')
    assert hpxNetwork.get_default_interfaces() == {'default_gateway': '192.168.0.1', 'default_interface': 'en3'}


# Generated at 2022-06-13 01:39:07.870220
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    instance = HPUXNetworkCollector()
    assert HPUXNetworkCollector is instance.__class__


# Generated at 2022-06-13 01:39:08.836692
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    HPUXNetworkCollector()

# Generated at 2022-06-13 01:39:14.529738
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    test_class = HPUXNetwork({})
    test_class.module.run_command = function_mock(out='default        128.0.0.0      UG   1          0 lan0')
    result = test_class.get_default_interfaces()
    assert result['default_interface'] == 'lan0'
    assert result['default_gateway'] == '128.0.0.0'


# Generated at 2022-06-13 01:39:18.117661
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    collector = HPUXNetworkCollector()
    assert collector._platform == 'HP-UX'
    assert collector._fact_class == HPUXNetwork


# Generated at 2022-06-13 01:39:21.708091
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    network = HPUXNetwork()
    iface = network.get_default_interfaces()
    assert iface['default_interface'] == 'lan1'
    assert iface['default_gateway'] == '10.0.0.1'


# Generated at 2022-06-13 01:39:28.842976
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    hn = HPUXNetwork()
    hn.module = AnsibleModuleMock()


# Generated at 2022-06-13 01:39:33.423061
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    HPUXNetwork.module = MockAnsibleModule()
    HPUXNetwork.module.run_command = Mock(return_value=(0, "default 192.168.1.1 UG 1 2 3 lan0", 0))
    network_collector = HPUXNetworkCollection()
    facts = network_collector.collect()
    assert len(facts) == 1
    assert facts['default_interface'] == 'lan0'
    assert facts['default_gateway'] == '192.168.1.1'


# Generated at 2022-06-13 01:39:35.300040
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    '''
    Test HPUXNetworkCollector constructor with different values
    '''
    try:
        HPUXNetworkCollector()
    except Exception:
        assert False



# Generated at 2022-06-13 01:39:51.026150
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    module = FakeAnsibleModule()
    module.run_command = MagicMock(return_value=[0,
                                                 'default 172.28.229.1 UGSc  22 0 lan0',
                                                 ''])
    network = HPUXNetwork(module)
    default_interfaces_facts = network.get_default_interfaces()
    assert default_interfaces_facts['default_interface'] == 'lan0'
    assert default_interfaces_facts['default_gateway'] == '172.28.229.1'



# Generated at 2022-06-13 01:40:00.096159
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )

    netstat_path = module.get_bin_path('netstat')
    if netstat_path is None:
        module.fail_json(msg='netstat binary not found')

    network = HPUXNetwork(module)
    network_facts = network.populate()
    interfaces = network_facts['interfaces']
    for iface in interfaces:
        assert network_facts[iface]['device'] == iface
        assert 'ipv4' in network_facts[iface]
        assert 'address' in network_facts[iface]['ipv4']
        assert 'network' in network_facts[iface]['ipv4']

# Generated at 2022-06-13 01:40:10.875986
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    from ansible.module_utils.facts.network.hpu_x import HPUXNetwork
    hpux_network = HPUXNetwork()
    netstat_path = hpux_network.module.get_bin_path('netstat')
    if netstat_path is None:
        return
    rc, out, err = hpux_network.module.run_command("/usr/bin/netstat -nr")
    if rc == 0 and out is not None:
        lines = out.splitlines()
        default_interfaces_facts = hpux_network.get_default_interfaces()

        assert default_interfaces_facts['default_interface'] == 'lan0'
        assert default_interfaces_facts['default_gateway'] == '10.192.198.254'

        rc, out, err = hpux_network.module

# Generated at 2022-06-13 01:40:19.025647
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    module = AnsibleModule(argument_spec={})
    module.exit_json = exit_json
    module.fail_json = fail_json
    module.run_command = mocked_run_command

    populate_facts(HPUXNetwork())
    assert(facts['default_interface'] == 'lan0')
    assert(facts['interfaces'] == ['lan0'])
    assert(facts['lan0']['ipv4']['address'] == '10.81.109.17')
    assert(facts['lan0']['ipv4']['network'] == '10.81.109.0')


# Generated at 2022-06-13 01:40:21.937474
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )

    # Create an instance of HPUXNetwork
    hpux_network_facts = HPUXNetwork(module)
    result = hpux_network_facts.populate()

    assert result['default_interface'] == 'lan0'



# Generated at 2022-06-13 01:40:25.810423
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    hpux_network_collector = HPUXNetworkCollector()
    assert isinstance(hpux_network_collector, HPUXNetworkCollector)
    assert isinstance(hpux_network_collector._fact_class, HPUXNetwork)

# Generated at 2022-06-13 01:40:28.386032
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    network_collector = HPUXNetworkCollector()
    assert network_collector.platform == 'HP-UX'
    assert network_collector._fact_class == HPUXNetwork


# Generated at 2022-06-13 01:40:29.794493
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    nc = HPUXNetworkCollector()
    assert nc._fact_class == HPUXNetwork
    assert nc._platform == 'HP-UX'



# Generated at 2022-06-13 01:40:36.493855
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    net = HPUXNetwork({})
    assert net.module is None
    assert net.collector is None
    assert net.platform == 'HP-UX'
    assert net.default_interface is None
    assert net.default_gateway is None
    assert net.all_ipv4_addresses == set()
    assert net.all_ipv6_addresses == set()
    assert net.interfaces == {}


# Generated at 2022-06-13 01:40:38.537476
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    obj = HPUXNetworkCollector()
    assert obj.platform == 'HP-UX'
    assert obj._fact_class == HPUXNetwork
    assert obj._platform == 'HP-UX'


# Generated at 2022-06-13 01:41:07.803931
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    """
    HPUXNetwork.populate method unit test
    """
    from ansible.module_utils.facts.network.hpu import HPUXNetwork
    from ansible.module_utils.facts.network.linux import get_file_content
    from ansible.module_utils.facts.network.base import Network
    network = HPUXNetwork()
    setattr(network, 'module', FakeAnsibleModule())
    setattr(network, 'get_file_content', get_file_content)
    facts = network.populate()
    assert (facts['interfaces'] == ['lan0', 'lan1'])
    assert (facts['default_interface'] == 'lan1')
    assert (facts['default_gateway'] == '172.17.28.1')

# Generated at 2022-06-13 01:41:11.484722
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    net_coll = HPUXNetworkCollector()
    assert(net_coll._fact_class == HPUXNetwork)
    assert(net_coll._platform == 'HP-UX')


# Generated at 2022-06-13 01:41:20.346253
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    class test_netstat():
        def __init__(self):
            self.out = """
[ace@ace_hppa1 ~]$ netstat -niw
Name Mtu   Network     Address            Ipkts Ierrs    Opkts Oerrs  Coll
lan1 1500 192.168.58       192.168.58.197 4144964     0   3823585     0     0
lan0 1500 192.168.1.0    192.168.1.200   1020545     0   1020765     0     0
"""
            self.rc = 0
            self.err = ''

        def run_command(self, cmd):
            return self.rc, self.out, self.err

    test_module = test_netstat()
    test_net = HPUXNetwork()

# Generated at 2022-06-13 01:41:23.003249
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    module = AnsibleModule(argument_spec={})
    network = HPUXNetwork(module)
    facts = network.populate()
    assert len(facts['interfaces']) > 0
    assert len(facts.keys()) > 0

# Generated at 2022-06-13 01:41:29.012860
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    hpux_network = HPUXNetwork()
    interfaces_info = hpux_network.get_interfaces_info()
    assert 'lan0' in interfaces_info
    assert 'ipv4' in interfaces_info['lan0']
    assert 'address' in interfaces_info['lan0']['ipv4']
    assert '192.168.40.2' == interfaces_info['lan0']['ipv4']['address']


# Generated at 2022-06-13 01:41:37.969752
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    class NetworkModule:
        def __init__(self):
            self.params = {}
            self.state = {}
            self.tmpdir = None

        def run_command(self, *args):
            command = args[0]
            out = """lan0  0 0.0.0.0 0.0.0.0 1.2.3.4"""
            return 0, out, ""

    mock_module = NetworkModule()
    HPUX_network = HPUXNetwork(mock_module)
    interfaces_info = HPUX_network.get_interfaces_info()

# Generated at 2022-06-13 01:41:44.164638
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    from ansible.module_utils.facts.network.hpux.eth0 import get_interfaces_info as get_interfaces_info_eth0
    from ansible.module_utils.facts.network.hpux.lo import get_interfaces_info as get_interfaces_info_lo
    import os
    network_facts = HPUXNetwork()
    network_facts.module = os
    network_facts.populate()

    interfaces = network_facts.get_interfaces_info()
    assert interfaces == get_interfaces_info_eth0()

    assert network_facts['default_interface'] == 'lan0'
    assert network_facts['default_gateway'] == '172.31.2.151'

# Generated at 2022-06-13 01:41:45.445835
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    hpx_network = HPUXNetwork()
    assert hpx_network.populate()


# Generated at 2022-06-13 01:41:51.015842
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    """Test module for testing the get_interfaces_info method of HPUXNetwork
    class.
    """
    # This test expects a file called netstat_niw_output.txt in the current
    # directory that contains the output of the command 'netstat -niw'.
    module_name = 'ansible.modules.network.hpux'
    module = __import__(module_name, globals(), locals(), [], -1)
    HPUXNetwork.module = module
    network = HPUXNetwork()
    interfaces = network.get_interfaces_info()
    for iface in interfaces:
        device = iface
        assert device == iface
        address = interfaces[iface]['ipv4']['address']
        assert address
        network = interfaces[iface]['ipv4']['network']
       

# Generated at 2022-06-13 01:41:54.371393
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    from ansible.module_utils.facts.network.hpux import HPUXNetwork

    foo = HPUXNetwork()
    print(foo.get_interfaces_info())
    assert foo.get_interfaces_info()


# Generated at 2022-06-13 01:42:39.671367
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    from ansible.module_utils.facts.network.hpux import HPUXNetwork
    network_facts = HPUXNetwork()
    collected_facts = None
    collected_facts = network_facts.populate(collected_facts)
    answers = {}
    for key in collected_facts:
        answers[key] = collected_facts[key]
    assert answers['default_interface'] == 'lan0'
    assert answers['default_gateway'] == '10.10.10.254'
    assert answers['interfaces'] == ['lan0']


# Generated at 2022-06-13 01:42:51.734999
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    """
    test_HPUXNetwork_populate: Unit test of method HPUXNetwork.populate
    """
    module = FakeAnsibleModule()
    network = HPUXNetwork()
    network.set_module(module)
    netstat_path = network.module.get_bin_path('netstat')
    if netstat_path is None:
        return
    result = network.populate()
    assert result['default_interface'] == 'lanX'
    assert result['default_gateway'] == 'XX.XX.XX.XX'
    assert result['interfaces'] == ['lanX']

# Generated at 2022-06-13 01:42:53.676672
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    HPUXNetworkCollector()

# Generated at 2022-06-13 01:42:57.001979
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    default_interface = {'default_interface': 'lan0', 'default_gateway': '192.168.1.1'}
    assert HPUXNetwork().get_default_interfaces() == default_interface


# Generated at 2022-06-13 01:43:01.079304
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    network_finder = HPUXNetwork()
    interfaces = network_finder.get_interfaces_info()
    assert interfaces is not None
    for device in interfaces:
        assert interfaces[device]['ipv4']['address'] is not None
        assert interfaces[device]['ipv4']['network'] is not None

# Generated at 2022-06-13 01:43:03.512181
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    obj = HPUXNetworkCollector()
    assert obj._platform == 'HP-UX'
    assert obj._fact_class == HPUXNetwork

# Generated at 2022-06-13 01:43:10.277809
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    module = AnsibleModule(
        argument_spec={
            'gather_subset': dict(default=[], type='list'),
            'gather_network_resources': dict(default=['all'], type='list')
        }
    )

    # Instantiate HPUXNetwork object
    obj = HPUXNetwork(module)

    # Test get_default_interfaces() method
    assert obj.get_default_interfaces()

    # Test get_interfaces_info() method
    assert obj.get_interfaces_info()



# Generated at 2022-06-13 01:43:13.108361
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    test_module = AnsibleModule(argument_spec={})
    hpux_network = HPUXNetwork(test_module)
    hpux_network.get_default_interfaces()
    test_module.exit_json()



# Generated at 2022-06-13 01:43:18.688565
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    import sys
    import os

    sys.path.append(os.path.join(os.path.dirname(__file__), '../../../lib'))
    from ansible.module_utils.facts.network.hpux import HPUXNetwork
    from ansible.module_utils import basic

    module = basic.AnsibleModule(
        argspec=dict()
    )

    # set default values
    module.params = {}

    hpux_network = HPUXNetwork(module)
    result = hpux_network.populate()
    assert isinstance(result, dict)
    for key in ['interfaces', 'default_interface', 'default_gateway']:
        assert key in result

# Generated at 2022-06-13 01:43:23.541876
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    class TestModule(object):
        def __init__(self, out):
            self.out = out

        def run_command(self, cmd, check_rc=True):
            return (0, self.out, '')

    out = ("/usr/bin/netstat -nr")
    out += ("Kernel Interface table")
    out += ("Destination        Gateway           Flags   Refs Use If")
    out += ("-------------------- -------------------- ----- ----- ---------- ---------")
    out += ("default             192.168.1.1           UGS    0    1 lan0")
    out += ("192.168.1           link#2                UC     0    0 lan0")
    out += ("192.168.1.1         00:00:5e:00:53:00     UHLWIir    0    1 lo0")

# Generated at 2022-06-13 01:45:14.353107
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    class Module(object):
        def __init__(self, netstat):
            self.netstat = netstat

        def run_command(self, cmd):
            return 0, self.netstat, ""

    # Successful parsing of netstat output
    netstat = (
        "lan0: flags=847<UP,BROADCAST,RUNNING,MULTICAST> mtu 1500 index 3\n"
        "      inet 172.19.128.34 netmask ffffff00 broadcast 172.19.128.255")
    obj = HPUXNetwork(Module(netstat))
    facts = obj.populate()
    assert facts['lan0']['ipv4']['address'] == '172.19.128.34'

# Generated at 2022-06-13 01:45:15.559958
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    intel = HPUXNetwork()
    assert isinstance(intel, Network)

# Generated at 2022-06-13 01:45:26.566504
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    def mock_run_command(module, command):
        out = """default 172.16.2.254 UGS 0 36 lan0
        0.0.0.0/0 172.16.2.254 UG 0 452 lan0
        127.0.0.1 127.0.0.1 UH 6 3 lo0"""
        return 0, out, ""

    mocked_object = type('obj', (object,), {'run_command': mock_run_command})
    anobj = HPUXNetwork()
    anobj.module = mocked_object()
    default_interfaces = anobj.get_default_interfaces()
    assert default_interfaces['default_interface'] == 'lan0'
    assert default_interfaces['default_gateway'] == '172.16.2.254'


# Generated at 2022-06-13 01:45:35.718702
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    import json
    results = {'default_interface': 'lan2', 'default_gateway': '10.99.99.1'}
    rc, out, err = 0, \
        'default 10.99.99.1       U     0 0          0 lan2', None
    mock_module = MockModule()
    mock_module.run_command = Mock(return_value=(rc, out, err))
    obj_hpuxnet = HPUXNetwork()
    obj_hpuxnet.module = mock_module
    default_interfaces = obj_hpuxnet.get_default_interfaces()
    assert json.loads(json.dumps(default_interfaces)) == results


# Generated at 2022-06-13 01:45:44.111338
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    line1 = 'default  12.34.56.0 UG      0 0        0 lan0'
    line2 = '172.21.2.0        0.0.0.0         U        0 0          lan10   '
    module = Mock()
    module.run_command.return_value = (0, [line1, line2], '')
    facts = HPUXNetwork()
    expected_facts = dict(default_interface='lan0', default_gateway='12.34.56.0')
    facts.module = module
    assert facts.get_default_interfaces() == expected_facts


# Generated at 2022-06-13 01:45:51.348380
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    module = AnsibleModule(argument_spec=dict())
    network_facts = HPUXNetwork(module)
    network_facts.populate()
    assert network_facts.default_interface == 'lan0'
    assert network_facts.default_gateway == '10.1.1.1'
    assert network_facts.interfaces == ['lan0']
    assert network_facts.lan0['device'] == 'lan0'
    assert network_facts.lan0['ipv4']['address'] == '10.1.1.10'
    assert network_facts.lan0['ipv4']['network'] == '10.1.1.0'


# Generated at 2022-06-13 01:45:57.757419
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    module = FakeAnsibleModule()
    network = HPUXNetwork(module)

    # Case 1: netstat is not available
    assert network.netstat_path is None
    assert network.populate({}) == {}

    # Case 2: netstat is available
    network.netstat_path = '/usr/bin/netstat'

    # Case 2.1: /usr/bin/netstat -nr does not return default interface info
    network.module.run_command = fake_run_command
    assert network.populate({}) == {}

    # Case 2.2: /usr/bin/netstat -niw does not return interface info
    fake_run_command.commands = {'/usr/bin/netstat -nr': (0, 'default default default default default default default default default', '')}
    assert network.populate({})

# Generated at 2022-06-13 01:46:07.520454
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    test_module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )

    test_output = """
lan0: flags=8843 mtu 1500 inet 10.25.142.191 netmask ffffff00 broadcast 10.25.142.255
"""

    expected_output = {'lan0': {'ipv4': {'network': 'ff.ff.ff.00',
                                          'interface': 'lan0',
                                          'address': '10.25.142.191'},
                               'device': 'lan0'}}

    test_network = HPUXNetwork(test_module)

    test_network.module.run_command = MagicMock(return_value=(0, test_output, None))

    actual_output = test_network.get_interfaces_

# Generated at 2022-06-13 01:46:10.650651
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    h = HPUXNetwork()
    assert h.platform == 'HP-UX'
    assert h.get_default_interfaces()['default_interface'] == 'lan0'

# Generated at 2022-06-13 01:46:14.388151
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    facts = HPUXNetwork()
    assert facts.default_interface == 'lan0'
    assert len(facts.interfaces) == 1
    assert 'lan0' in facts.interfaces