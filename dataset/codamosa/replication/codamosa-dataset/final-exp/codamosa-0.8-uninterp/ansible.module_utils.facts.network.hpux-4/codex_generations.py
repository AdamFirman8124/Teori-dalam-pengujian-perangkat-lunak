

# Generated at 2022-06-13 01:37:48.848782
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    net = HPUXNetwork(None)
    interfaces = net.get_interfaces_info()
    assert 'lan0' in interfaces
    assert interfaces['lan0']['ipv4']['address'] in ('10.23.235.78', '172.17.81.190')



# Generated at 2022-06-13 01:37:55.633445
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    context = {}
    params = {}
    module = AnsibleModule(argument_spec=params,
                           supports_check_mode=False)
    set_module_args(params)
    net = HPUXNetwork(module=module, params=params)
    interfaces = net.get_interfaces_info()
    assert interfaces.get('lan0') is not None
    assert interfaces.get('lan0').get('ipv4').get('address') is not None
    assert interfaces.get('lan0').get('ipv4').get('network') is not None
    assert interfaces.get('lan0').get('ipv4').get('network') == '192.168.3.0'
    assert interfaces.get('lan0').get('ipv4').get('address') == '192.168.3.1'


# Generated at 2022-06-13 01:37:57.711940
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    hu = HPUXNetworkCollector()
    assert hu._fact_class == HPUXNetwork
    assert hu._platform == 'HP-UX'

# Generated at 2022-06-13 01:38:03.805272
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )
    network = HPUXNetwork(module)
    network_facts = network.populate()
    assert ('default_interface' in network_facts)
    assert ('interfaces' in network_facts)
    assert ('lan1' in network_facts['interfaces'])

# Generated at 2022-06-13 01:38:14.316207
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    module = FakeAnsibleModule()
    # We can't populate without '/usr/bin/netstat'
    netstat_path = module.get_bin_path('netstat')


# Generated at 2022-06-13 01:38:25.468595
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    test_module = AnsibleModule(
        argument_spec={
        },
        supports_check_mode=True
    )
    test_module.params = {}
    test_module.run_command = run_command_mock
    test_module.get_bin_path = get_bin_path_mock
    hpu_net = HPUXNetwork()
    hpu_net.module = test_module
    hpu_net.populate()

# Generated at 2022-06-13 01:38:33.206793
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    module = AnsibleModule(argument_spec={})
    module.run_command = mock.Mock(return_value=(0, """Kernel Interface Table
lan0   lan      0        10.10.10.1       10.10.10.255       UP
lan1   lan      1        10.10.20.1       10.10.20.255       UP
lan2   lan      2        10.10.30.1       10.10.30.255       UP""", ""))
    test_obj = HPUXNetwork()
    interfaces = test_obj.get_interfaces_info()

# Generated at 2022-06-13 01:38:43.569936
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    # Build the test object
    module = MockRunner()
    network = HPUXNetwork(module)

    # Build some test data
    fake_default_interfaces_out = """Kernel IP routing table
Destination     Gateway         Flags Refs Use If  Expire
default         172.16.0.1      UG        0     0  lan8002
172.16.0.0      172.16.0.1
172.17.0.0      172.17.0.1"""
    module.run_command.return_value = (0, fake_default_interfaces_out, '')

    # Get the interface info
    interface_facts = network.get_default_interfaces()

    # Assert that the data are correct
    assert interface_facts['default_interface'] == 'lan8002'

# Generated at 2022-06-13 01:38:51.171627
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    """
    Unit test for method populate of class HPUXNetwork

    This module will be mocked in the unit test, so all
    of these values will be the same
    """
    net_mod = HPUXNetwork(dict())
    facts = dict()
    collected_facts = dict()
    facts = net_mod.populate(collected_facts)
    assert 'default_interface' in facts
    assert 'default_gateway' in facts
    assert 'interfaces' in facts
    for key in facts['interfaces']:
        assert key in facts
    return

# Generated at 2022-06-13 01:38:57.855384
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    module = MockModule()
    network = HPUXNetwork(module)
    network.module.run_command = run_command_mock
    interfaces = network.get_interfaces_info()
    assert interfaces['lan0'] == {'device': 'lan0',
                                  'ipv4': {'network': '10.124.79',
                                           'interface': 'lan0',
                                           'address': '10.124.79.92'}}



# Generated at 2022-06-13 01:39:06.519360
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    network = HPUXNetwork()
    assert network is not None
    assert network.platform == "HP-UX"
    assert network.get_interfaces_info()
    assert network.get_default_interfaces()



# Generated at 2022-06-13 01:39:08.611766
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    facts = HPUXNetwork()
    assert facts.platform == 'HP-UX'


# Generated at 2022-06-13 01:39:14.718490
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    am = AnsibleModule(
        argument_spec={
            'gather_subset': dict(default=['!all'], type='list')
        }
    )
    nm = HPUXNetwork(am)
    expected_result = {'default_interface': 'lan0',
                       'default_gateway': '192.0.0.1'}
    actual_result = nm.get_default_interfaces()
    assert actual_result == expected_result


# Generated at 2022-06-13 01:39:24.442982
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():

    test_HPUXNetwork = HPUXNetwork(dict())
    # test_HPUXNetwork = HPUXNetwork({"ANSIBLE_MODULE_ARGS": {'gather_subset': '!all,!min'}})
    Interfaces = test_HPUXNetwork.get_interfaces_info()
    print("RESULTS: " + str(Interfaces))
    for i in Interfaces:
        print("\tRESULT: %s: %s" % (i, Interfaces[i]))
        for j in Interfaces[i]:
            print("\t\tRESULT: %s: %s" % (j, Interfaces[i][j]))

# Generated at 2022-06-13 01:39:30.057151
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    module = AnsibleModule(
        argument_spec={},
        supports_check_mode=False)
    network = HPUXNetwork()
    network.module = module

    hostname = socket.gethostname()
    if '.' in hostname:
        hostname = hostname.split('.')[0]
    default_interfaces = {'default_interface': 'lan0',
                          'default_gateway': '192.168.0.1'}
    assert network.get_default_interfaces() == default_interfaces



# Generated at 2022-06-13 01:39:31.370909
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    network = HPUXNetwork(dict())

# Unit test class HPUXNetworkCollector

# Generated at 2022-06-13 01:39:33.423431
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    """Test the HPUXNetworkCollector constructor"""
    hpuxnc = HPUXNetworkCollector()
    assert hpuxnc._fact_class == HPUXNetwork
    assert hpuxnc._platform == 'HP-UX'

# Generated at 2022-06-13 01:39:37.028068
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    net = HPUXNetwork()
    net.module.run_command = fake_run_command
    net.module.get_bin_path = fake_get_bin_path
    default_interfaces = net.get_default_interfaces()
    assert default_interfaces == {
        'default_interface': 'lan0',
        'default_gateway': '172.16.45.1'
    }



# Generated at 2022-06-13 01:39:42.296349
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    module = Network()
    module.run_command = run_command
    hpux_network = HPUXNetwork(module)
    expected_default_interfaces = {'default_interface': 'lan2', 'default_gateway': '172.17.0.1'}
    default_interfaces = hpux_network.get_default_interfaces()
    assert default_interfaces == expected_default_interfaces


# Generated at 2022-06-13 01:39:49.555034
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    from ansible.module_utils.facts.network.hpu_ux import HPUXNetwork
    module = AnsibleModuleMock()
    module.run_command = module_run_command
    netwrk = HPUXNetwork(module)
    interfaces = netwrk.get_interfaces_info()
    assert interfaces['lan0'] == {'device': 'lan0',
                                  'ipv4': {'address': '10.20.30.40',
                                           'network': '10.20.30.0',
                                           'interface': 'lan0'}}



# Generated at 2022-06-13 01:40:02.128622
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    lan0 = "lan0: flags=8843<UP,BROADCAST,RUNNING,SIMPLEX,MULTICAST> mtu 1500 " +\
           "options=8<VLAN_MTU> inet 172.28.128.1 netmask 0xffffff00 broadcast " +\
           "172.28.128.255 ether 08:00:09:52:e5:59 media: Ethernet autoselect (100baseTX full-duplex)"

# Generated at 2022-06-13 01:40:05.368347
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    module = AnsibleModule(argument_spec={})
    hpux_network = HPUXNetwork(module)
    assert len(hpux_network.get_interfaces_info()) == 0

# Generated at 2022-06-13 01:40:12.741150
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    module = Network(dict())
    network_facts = HPUXNetwork(module)
    network_facts.populate()
    interfaces_facts = network_facts.get_interfaces_info()
    default_interfaces_facts = network_facts.get_default_interfaces()
    assert 'default_interface' in default_interfaces_facts
    if 'default_interface' in default_interfaces_facts:
        assert 'default_gateway' in default_interfaces_facts
        if 'default_gateway' in default_interfaces_facts:
            assert 'ipv4' in interfaces_facts[
                default_interfaces_facts['default_interface']]

# Generated at 2022-06-13 01:40:23.515019
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    import sys
    import os
    import platform

    if platform.system() != 'HP-UX':
        return

    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..')))
    from ansible.module_utils.facts.network.hpux import HPUXNetwork
    net = HPUXNetwork()
    net.module.run_command = lambda x: (0, 'lan0 link#2 UP UP 127 127 0.0.0.0 0.0.0.0', '')
    net.module.get_bin_path = lambda x: '/usr/bin/netstat'
    fact_subset = net.populate()

# Generated at 2022-06-13 01:40:31.265300
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    module = AnsibleModule(argument_spec={})
    module.run_command = MagicMock(return_value=(0, 'lan0   lan0    0    0    0    0      0      0      0       0     0     0     0   0   0   0   0', ''))
    hpn = HPUXNetwork()
    hpn.module = module
    interfaces = hpn.get_interfaces_info()
    assert interfaces == {
        'lan0': {
            'ipv4': {'address': '0', 'network': '0', 'interface': 'lan0'}, 'device': 'lan0'
        }
    }



# Generated at 2022-06-13 01:40:41.905921
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    class ModuleMock(object):
        def get_bin_path(*args, **kwargs):
            return '/usr/bin/netstat'

        def run_command(*args, **kwargs):
            out = '''default         <null>         <null>         UG   0   0        0 lan0
127.0.0.0       127.255.255.255 UH   0   0        0 lo0
192.168.0.0     192.168.0.255   U     0   0   0    lan0
192.168.0.0     192.168.0.255   U     0   0   0    lan1
'''
            return 0, out, None

    module_mock = ModuleMock()
    n = HPUXNetwork(module_mock)
    ret = n.get_default_

# Generated at 2022-06-13 01:40:46.684147
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    """
    Unit test for method get_interfaces_info of class HPUXNetwork
    """
    hpuxnetwork = HPUXNetwork()
    interfaces = hpuxnetwork.get_interfaces_info()
    assert len(interfaces) > 0

# Generated at 2022-06-13 01:40:50.825069
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    from ansible.module_utils.facts.network.hpux import HPUXNetwork
    hpux_network = HPUXNetwork()
    assert hpux_network.get_default_interfaces() == {'default_interface': 'lan25', 'default_gateway': '192.168.1.1'}


# Generated at 2022-06-13 01:40:58.406689
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    from ansible_collections.ansible.netcommon.tests.unit.compat.mock import patch
    from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import dict_merge
    from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import dict_to_set
    from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import to_list

    mock_module = patch('ansible_collections.ansible.netcommon.plugins.modules.network.facts.network.HPUXNetwork.module')
    mock_run_command = patch('ansible_collections.ansible.netcommon.plugins.modules.network.facts.network.HPUXNetwork.run_command')

    module

# Generated at 2022-06-13 01:41:08.495558
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    module = AnsibleModule(argument_spec=dict())
    network = HPUXNetwork(module)

    # Setup some dummy return codes. The test should pass
    # even if the platform is different to HP-UX
    network.module.run_command.return_value = 0, '', ''
    network.module.run_command.side_effect = [
        (0, 'default z.z.z.z z.z.z.z UG lan1', ''),
        (0, 'lan1 129.128.13.10 129.128.4.0 U lan1', ''),
        (0, 'lan0 129.128.5.10 129.128.5.0 U lan0', '')
    ]

    network.populate()
    assert network.default_interface == 'lan1'
    assert network.default_gate

# Generated at 2022-06-13 01:41:21.497162
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    network = HPUXNetwork()
    network.module.get_bin_path = lambda _: '/usr/bin/netstat'
    intf_info = {
        'f0:1': {
            'device': 'f0:1',
            'ipv4': {
                'address': '10.1.1.1',
                'network': '10.1.1.0',
                'interface': 'f0:1'},
        },
        'f0:2': {
            'device': 'f0:2',
            'ipv4': {
                'address': '10.2.2.2',
                'network': '10.2.2.0',
                'interface': 'f0:2'},
        },
    }

# Generated at 2022-06-13 01:41:23.364320
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    collector = HPUXNetworkCollector()
    assert collector.platform == 'HP-UX'
    assert collector.fact_class == HPUXNetwork


# Generated at 2022-06-13 01:41:24.599389
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    network_collector = HPUXNetworkCollector()
    assert network_collector._platform == 'HP-UX'

# Generated at 2022-06-13 01:41:33.487722
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    module = AnsibleModule(argument_spec={})
    network_collector = HPUXNetworkCollector(module)
    network_facts = network_collector.collect(None)
    assert 'default_interface' in network_facts
    assert isinstance(network_facts['default_interface'], str)
    assert 'default_gateway' in network_facts
    assert isinstance(network_facts['default_gateway'], str)
    assert 'interfaces' in network_facts
    assert isinstance(network_facts['interfaces'], list)
    assert len(network_facts['interfaces']) > 0
    assert network_facts['default_interface'] in network_facts['interfaces']
    assert network_facts['default_interface'] in network_facts


# Generated at 2022-06-13 01:41:35.971684
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    hpux_network = HPUXNetwork()
    assert hpux_network is not None
    assert hpux_network.module is not None


# Generated at 2022-06-13 01:41:37.993145
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    facts = HPUXNetwork()

    # Check default values
    assert facts.default_interface == ''
    assert facts.default_gateway == '0.0.0.0'

# Generated at 2022-06-13 01:41:39.472457
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    assert HPUXNetworkCollector().platform == 'HP-UX'

# Generated at 2022-06-13 01:41:44.233164
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    module = AnsibleModule(
        argument_spec = dict(),
    )
    module.run_command = MagicMock(return_value=(0, 'default 192.168.1.1  UG  0  0  lan0', ''))
    hpux_network = HPUXNetwork(module)
    network_facts = hpux_network.get_default_interfaces()
    assert network_facts == {'default_interface': 'lan0', 'default_gateway': '192.168.1.1'}



# Generated at 2022-06-13 01:41:46.410177
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    mynet = HPUXNetwork()
    assert mynet.platform == 'HP-UX'
    assert mynet._platform == 'HP-UX'
    assert mynet.get_interfaces_info()
    assert mynet.get_default_interfaces()

# Generated at 2022-06-13 01:41:49.295008
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    from ansible.module_utils.facts.network.hpux import HPUXNetwork
    n = HPUXNetwork()
    assert n

# Generated at 2022-06-13 01:42:08.848010
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    module = FakeModule(params={'src': '/etc/ansible/facts.d/network.fact'})
    out = "/usr/bin/netstat -nr"
    stdout = "default 192.168.42.67 UG lan0"
    net = HPUXNetwork(module)
    net.module.run_command = run_command_mock
    default_interfaces = net.get_default_interfaces()
    assert run_command_mock.called
    assert run_command_mock.call_args == call(out)
    assert stdout in run_command_mock.call_args_list[0][0][0]
    assert default_interfaces['default_interface'] == 'lan0'
    assert default_interfaces['default_gateway'] == '192.168.42.67'


#

# Generated at 2022-06-13 01:42:14.980418
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    module = MagicMock()
    module.run_command.return_value = 0, "default 172.27.1.1 UGS 0 0 lan0\n", ""
    hpux_network = HPUXNetwork(module)
    expected = {'default_interface': 'lan0', 'default_gateway': '172.27.1.1'}
    assert expected == hpux_network.get_default_interfaces()


# Generated at 2022-06-13 01:42:17.294870
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    assert HPUXNetworkCollector.platform is 'HP-UX'
    assert HPUXNetworkCollector.fact_class is HPUXNetwork


# Generated at 2022-06-13 01:42:20.840115
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    hpn = HPUXNetwork()
    assert type(hpn) == HPUXNetwork

    assert hpn.platform == "HP-UX"

# Usable as a main program for testing.
if __name__ == '__main__':
    test_HPUXNetwork()

# Generated at 2022-06-13 01:42:27.516691
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    net = HPUXNetwork({})
    out = 'lan0          Lan 0             Up  10.233.58.144/24                lan0'
    interfaces = net.get_interfaces_info()
    assert interfaces['lan0'] == {'device': 'lan0',
                                  'ipv4': {'address': '10.233.58.144',
                                           'interface': 'lan0',
                                           'network': '10.233.58.0'}}

# Generated at 2022-06-13 01:42:34.034474
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    """
    This test mocks the run_command method of class AnsibleModule
    to simulate a standard output of the netstat -niw command
    and verify if the response returned by the method
    get_interfaces_info matches the expected result
    """

    # Creates an object of class HPUXNetwork which will be used to run
    # the method to be tested get_interfaces_info
    test_network = HPUXNetwork(None)

    # Simulates the standard output of the netstat -niw command

# Generated at 2022-06-13 01:42:41.472962
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    """
    This method tests the get_default_interfaces method of class HPUXNetwork()
    
    Input:
    A sample output from the command netstat -nr
    
    Returns:
    Default interface and Default Gateway
    """

    sample_output = """Routing tables

Internet:
Destination        Gateway           Flags    Refs     Use    If  Expire
default            10.39.59.254      UG            0    7876    lan0
10.0/16            10.39.59.254      U         14     458    lan0
10.39.59.0         10:02:b5:b1:59:30  UHLWI           0   10410    lan0  587
"""


# Generated at 2022-06-13 01:42:46.278910
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    module = MockModule()
    network = HPUXNetwork(module)
    ifaces = network.get_default_interfaces()
    assert 'default_interface' in ifaces
    assert 'default_gateway' in ifaces

# Generated at 2022-06-13 01:42:54.543277
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    output_netstat_nr = 'default 148.1.1.1 UGn0  default'
    output_netstat_niw = 'lo0  lan0  lan1'
    HPUX_facts = HPUXNetwork()
    HPUX_facts.module.run_command = lambda *args, **kwargs: (0, output_netstat_nr, '')
    HPUX_facts.module.get_bin_path = lambda *args, **kwargs: '/usr/bin/netstat'
    HPUX_facts.module.get_file_content = {}
    fact_network = HPUX_facts.populate()
    assert fact_network['default_interface'] == 'UGn0'

# Generated at 2022-06-13 01:43:00.328915
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    test_collected_facts = {}
    collector = HPUXNetworkCollector(None, test_collected_facts, None)
    assert collector.platform == 'HP-UX'
    assert collector._collector == 'HPUXNetwork'
    assert collector.module == None
    assert collector.collected_facts == test_collected_facts
    assert collector._key == 'ansible_net_'


# Generated at 2022-06-13 01:43:16.367583
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    dummy_module = AnsibleModule(argument_spec={'test': {'type': 'bool', 'required': False, 'default': False}})
    network = HPUXNetwork()
    iface_data = network.get_interfaces_info()
    if iface_data:
        dummy_module.exit_json(changed='false', ansible_facts=dict(ansible_net_interfaces=iface_data))
    else:
        dummy_module.exit_json(changed='false', msg="No output from command")


# Generated at 2022-06-13 01:43:26.684010
# Unit test for method get_interfaces_info of class HPUXNetwork

# Generated at 2022-06-13 01:43:28.754637
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    obj = HPUXNetwork()
    assert obj.platform == 'HP-UX'

# Generated at 2022-06-13 01:43:37.119172
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    expected_default_interfaces = {'default_interface': 'lan8',
                                   'default_gateway': '10.20.30.250'}
    m = MagicMock()
    m.run_command.return_value = (0, '''
Destination       Gateway           Flags    Refs    Use   Interface
default           10.20.30.250      UG         1      0     lan8
127.0.0.1         127.0.0.1         UH         1      0     lo0
10.20.30.0        10.20.30.250      U          1      0     lan8
10.20.30.250      127.0.0.1         UH         1      0     lo0''', None)
    h = HPUXNetwork(m)
    assert h.get_default_interfaces

# Generated at 2022-06-13 01:43:43.117964
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    network = HPUXNetwork()
    network.module = FakeAnsibleModule()
    default_interfaces_expected = {'default_interface': 'lan2',
                                   'default_gateway': '192.168.1.1'}
    default_interfaces = network.get_default_interfaces()
    assert default_interfaces == default_interfaces_expected


# Generated at 2022-06-13 01:43:46.802402
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    hn = HPUXNetwork({})
    assert hn.platform == 'HP-UX'
    assert hn.default_gateway is None
    assert hn.default_interface is None
    assert hn.interfaces is None
    assert isinstance(hn.ipv4, dict)
    assert hn.ipv4['address'] is None
    assert hn.ipv6 is None
    assert hn.netmask is None
    assert hn.network is None


# Generated at 2022-06-13 01:43:47.500155
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    hpux_network_collector = HPUXNetworkCollector()
    assert hpux_network_collector is not None

# Generated at 2022-06-13 01:43:49.520873
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    facts = {}
    HPUXNetworkCollector(facts, None)
    assert 'ansible_net_default_interface' in facts
    assert 'ansible_net_interfaces' in facts
    for item in facts['ansible_net_interfaces']:
        assert 'ansible_' + item in facts


# Generated at 2022-06-13 01:43:55.136077
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    hn = HPUXNetwork()
    interfaces = {'lan0': {'device': 'lan0', 'ipv4': \
                           {'network': '127.0.0.0', \
                            'interface': 'lan0', 'address': '127.0.0.1'}, \
                            'wireless_mode': None, 'macaddress': None}, \
                 'lan1': {'device': 'lan1', 'ipv4': {'address': '172.20.1.42'}}}

    assert (interfaces == hn.get_interfaces_info())

# Generated at 2022-06-13 01:43:58.283988
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    obj = HPUXNetworkCollector(None, None, None, None)
    assert obj._fact_class == HPUXNetwork
    assert obj._platform == 'HP-UX'

# Generated at 2022-06-13 01:44:43.389592
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    """ Unit test to test get_default_interfaces method of class HPUXNetwork

        Use a mock of the module object and monkey patch the methods run_command
        and get_bin_path.
    """
    class Module:
        def __init__(self):
            self.run_command_results = []
            self.run_command_calls = []
            self.get_bin_path_return_value = "/usr/bin"

        def run_command(self, args, check_rc=False):
            self.run_command_calls.append(args)
            return self.run_command_results.pop(0)

        def get_bin_path(self, arg, opt_dirs=[]):
            return self.get_bin_path_return_value


# Generated at 2022-06-13 01:44:50.593241
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    modules = dict()
    modules['ansible.module_utils.facts.network.base'] = Network
    modules['ansible.module_utils.facts.network.hpux'] = HPUXNetwork
    set_module_args({'ANSIBLE_MODULE_ARGS': dict()})
    from ansible.module_utils.facts.network.hpux import HPUXNetwork

    hpux_network = HPUXNetwork()
    interfaces = hpux_network.get_interfaces_info()

    assert interfaces['lan0']['ipv4']['network'] == "192.168.122.0"

    return interfaces

# Generated at 2022-06-13 01:44:52.678991
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    mod = AnsibleModule(argument_spec={})
    net = HPUXNetwork(mod)
    assert(net.platform == 'HP-UX')


# Generated at 2022-06-13 01:44:59.472412
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    class MockNetwork(HPUXNetwork):
        def __init__(self, module):
            self.module = module
        def run_command(self, cmd):
            return [0, '/usr/bin/netstat -nr', None]

    class MockModule(object):
        def __init__(self):
            self.run_command_called = 0
        def run_command(self, cmd):
            self.run_command_called += 1
            return [0, '/usr/bin/netstat -nr', None]

    module = MockModule()
    net = MockNetwork(module)
    fact = net.get_default_interfaces()
    assert 'default_interface' in fact
    assert fact['default_interface'] == 'lan2'
    assert 'default_gateway' in fact
    assert fact['default_gateway']

# Generated at 2022-06-13 01:45:00.833930
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    network_collector = HPUXNetworkCollector()
    assert network_collector.platform == 'HP-UX'

# Generated at 2022-06-13 01:45:12.577369
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    hn = HPUXNetwork()
    hn.module.run_command = lambda x: (0, "default 172.16.251.202 UGS 0 1194 lan0", "")
    default_interfaces_facts = hn.get_default_interfaces()
    assert type(default_interfaces_facts) is dict
    assert default_interfaces_facts['default_gateway'] == '172.16.251.202'
    assert default_interfaces_facts['default_interface'] == 'lan0'
    hn.module.run_command = lambda x: (1, "", "")
    default_interfaces_facts = hn.get_default_interfaces()
    assert type(default_interfaces_facts) is dict
    assert len(default_interfaces_facts) == 0



# Generated at 2022-06-13 01:45:16.605423
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    test_netstat_out = 'default 192.168.1.1 UG  lan0'
    test_HPUXNetwork = HPUXNetwork({})
    test_HPUXNetwork.netstat_path = "/usr/bin/netstat"
    test_HPUXNetwork.module = MockModule({'run_command': (0, test_netstat_out, '')})
    assert test_HPUXNetwork.get_default_interfaces() == {'default_interface': 'lan0', 'default_gateway': '192.168.1.1'}



# Generated at 2022-06-13 01:45:18.644045
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    collect = HPUXNetworkCollector()
    assert collect._fact_class == HPUXNetwork
    assert collect._platform == 'HP-UX'

# Generated at 2022-06-13 01:45:29.810021
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    m_module = MockModule()
    m_module.run_command = get_run_command()
    net = HPUXNetwork(m_module)
    defaults = net.get_default_interfaces()
    assert defaults['default_interface'] == 'lan1'
    assert defaults['default_gateway'] == '172.17.8.1'

testinput_netstat_niw = """\
lan1   0.0.0 B/s  0.0.0 B/s  17.2.8.24   172.17.8.0
lan2   0.0.0 B/s  0.0.0 B/s  17.2.8.25   172.17.8.0
"""


# Generated at 2022-06-13 01:45:30.700237
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    HPUXNetworkCollector()

# Generated at 2022-06-13 01:46:31.707984
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    hpn = HPUXNetwork()
    default_interfaces = hpn.get_default_interfaces()
    assert 'default_interface' in default_interfaces
    assert 'default_gateway' in default_interfaces



# Generated at 2022-06-13 01:46:37.671513
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    """Test for method get_interfaces_info of class HPUXNetwork."""
    from ansible.module_utils.facts.network.hpux import HPUXNetwork
    mod = FakeModule()
    hn = HPUXNetwork(mod)
    hn.get_interfaces_info()
    output = mod.run_command.call_args[0][0]
    assert output == '/usr/bin/netstat -niw'
    assert mod.run_command.call_count == 1



# Generated at 2022-06-13 01:46:45.706876
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    class AnsibleModuleMock(object):
        def __init__(self):
            self.params = {}
            self.fail_json = lambda: None

        def get_bin_path(self, arg):
            return "/usr/bin/netstat"

        def run_command(self, arg):
            return 0, raw_data, ""

    class FactsMock(object):
        def __init__(self):
            self.data = {}

    hp_ux = HPUXNetwork(AnsibleModuleMock())
    facts = FactsMock()
    hp_ux.populate(facts)

    assert set(facts.data.keys()) == {'default_interface', 'default_gateway', 'interfaces', 'lan0'}

    assert facts.data['default_interface'] == 'lan0'
    assert facts.data

# Generated at 2022-06-13 01:46:46.432845
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    obj = HPUXNetworkCollector()
    assert obj is not None

# Generated at 2022-06-13 01:46:51.586195
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    mock_module = MockModule()
    mock_module.run_command = Mock(return_value=(0, '/usr/bin/netstat -nr', ''))
    mock_module.run_command.return_value = (0,
                                            ('default 172.16.0.0 UG lan4               172.16.0.2 UGHS', ''))
    network = HPUXNetwork(mock_module)
    default_interfaces_facts = network.get_default_interfaces()
    assert default_interfaces_facts == {'default_interface': 'lan4',
                                        'default_gateway': '172.16.0.0'}


# Generated at 2022-06-13 01:46:57.131822
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    module = MockModule()
    network = HPUXNetwork(module)
    interfaces = network.get_interfaces_info()
    assert interfaces is not None
    assert isinstance(interfaces, dict)
    assert 'lan0' in interfaces
    assert 'lan1' in interfaces
    lan0 = interfaces['lan0']
    assert lan0['ipv4']['address'] == '10.0.2.15'
    assert lan0['ipv4']['interface'] == 'lan0'
    assert lan0['ipv4']['network'] == '10.0.2.0'
    lan1 = interfaces['lan1']
    assert lan1['ipv4']['address'] == '192.168.56.2'
    assert lan1['ipv4']['interface'] == 'lan1'

# Generated at 2022-06-13 01:47:04.813591
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    #Interface information from netstat -niw
    #---------------
    #lan0           5         0          0     0.0    0.0       0   0.0   0.0
    #lan0      172.19.21.3      172.19.21.0  255.255.255.0     0.0    0.0       0   0.0   0.0
    #
    net_facts = HPUXNetwork()
    ifcfgs = net_facts.get_interfaces_info()
    assert ifcfgs['lan0']['device'] == 'lan0'
    assert ifcfgs['lan0']['ipv4']['address'] == '172.19.21.3'

# Generated at 2022-06-13 01:47:05.272325
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    pass

# Generated at 2022-06-13 01:47:12.814926
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    # Arrange
    mock_module = MockModule()
    mock_module.run_command = Mock(return_value=[0, "default 192.168.0.1 UGS 0 268435456 192.168.0.8 lan2\n", ""])

    expected_default_interfaces = {'default_interface': 'lan2', 'default_gateway': '192.168.0.1'}

    test_object = HPUXNetwork(mock_module)
    # Act
    interfaces = test_object.get_default_interfaces()
    # Assert
    assert interfaces == expected_default_interfaces



# Generated at 2022-06-13 01:47:17.642093
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    network = HPUXNetwork()
    network.netstat_path = '/usr/bin/netstat'
    network.populate()
    assert network.default_interface == 'lan0'
    assert network.default_gateway == '192.168.1.1'
    assert network.interfaces == ['lan0']
    assert network.lan0 == {'device': 'lan0',
                            'ipv4': {'network': '192.168.1.0',
                                     'interface': 'lan0',
                                     'address': '192.168.1.226'}}