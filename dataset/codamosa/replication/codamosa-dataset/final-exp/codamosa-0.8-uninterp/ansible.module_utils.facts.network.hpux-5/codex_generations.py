

# Generated at 2022-06-13 01:37:47.156818
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    hpux_network = HPUXNetwork(None)
    assert hpux_network.platform == 'HP-UX'

# Generated at 2022-06-13 01:37:52.232417
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    network_module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True)


# Generated at 2022-06-13 01:37:53.382011
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
     result = HPUXNetworkCollector()
     assert result.platform == 'HP-UX'

# Generated at 2022-06-13 01:37:56.838173
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    collector = HPUXNetworkCollector(None)
    assert collector.platform == 'HP-UX'
    assert collector.fact_class == HPUXNetwork



# Generated at 2022-06-13 01:38:07.050364
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    module = Mock(params=dict())
    module.run_command.return_value = (0, "", "")

# Generated at 2022-06-13 01:38:15.968743
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    test_interface = 'lan0'
    test_address = '10.107.44.120'
    test_mask = '255.255.255.0'
    test_network = '10.107.44.0'

    class NetworkModule:
        def __init__(self):
            self.params = {}

        def get_bin_path(self, exe, opt_dirs=[]):
            return 'netstat-path'

    network = HPUXNetwork()
    network.module = NetworkModule()
    network.module.run_command = get_netstat_mock(test_address, test_mask, test_network)
    interfaces = network.get_interfaces_info()
    assert test_address == interfaces[test_interface]['ipv4']['address']

# Generated at 2022-06-13 01:38:26.344595
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    test_data = ['lan0: flags=842<BROADCAST,RUNNING,MULTICAST> mtu 1500 index 2',
                 '        address: 00:03:ba:6c:ff:40',
                 '        media: Ethernet autoselect (100baseTX <full-duplex>)',
                 '        status: active',
                 '        inet x.y.z.w netmask 0xffffff00 broadcast x.y.z.255']
    fact_class = HPUXNetwork()
    fact_class.module = MagicMock()
    fact_class.module.run_command.return_value = 0, '\n'.join(test_data), ''
    interfaces = fact_class.get_interfaces_info()

# Generated at 2022-06-13 01:38:29.170970
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    hn = HPUXNetwork()
    assert hn is not None
    assert hn.module is None
    assert hn.get_interfaces_info() != {}
    assert hn.get_default_interfaces() != {}

# Generated at 2022-06-13 01:38:33.747982
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    module = AnsibleModule(
        argument_spec=dict(gather_subset=dict(default=['!all'], type='list'))
    )
    if not HP_UX:
        module.fail_json(msg='platform not supported')
    network = HPUXNetwork(module=module)

    network_facts = network.populate()
    assert network_facts['default_interface'] != ""
    assert network_facts['default_gateway'] != ""
    assert len(network_facts['interfaces']) > 0

# Generated at 2022-06-13 01:38:36.734663
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    network = HPUXNetwork(None)
    assert network.platform == 'HP-UX'
    assert network.get_interfaces_info() is not None
    assert network.get_default_interfaces() is not None

# Generated at 2022-06-13 01:38:47.110094
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    hp_network = HPUXNetwork({})
    assert HPUXNetwork.platform == 'HP-UX'


# Generated at 2022-06-13 01:38:57.370639
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    class ModuleStub(object):
        def run_command(self):
            return 0, 'lan0: flags=843<UP,BROADCAST,RUNNING,MULTICAST> mtu 1500 index 1\n' \
                      '        inet 192.168.1.3 netmask ffffff00 broadcast 192.168.1.255\n' \
                      'lan1: flags=843<UP,BROADCAST,RUNNING,MULTICAST> mtu 1500 index 2\n' \
                      '        inet 192.168.3.3 netmask ffffff00 broadcast 192.168.3.255\n', \
                      ''
    module = ModuleStub()

    network = HPUXNetwork()
    network.module = module

    interfaces_info = network.get_interfaces_info()

    assert interfaces_

# Generated at 2022-06-13 01:39:08.694010
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    import os
    import sys
    import unittest

    if os.path.exists('/etc/redhat-release'):
        test_dir = os.path.dirname(os.path.realpath(__file__))
        sys.path.append(test_dir + '/../../../../lib/ansible/module_utils/facts/')
        sys.path.append(test_dir + '/../../../../lib/ansible/module_utils/')
        from ansible.module_utils.facts import cache
        from ansible.module_utils.facts.system.base import Network
        from ansible.module_utils.facts.system.network import NetworkCollector
        from ansible.module_utils.facts.network.hpux import HPUXNetwork

# Generated at 2022-06-13 01:39:10.520876
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    test_HPUXNetwork = HPUXNetwork()
    assert test_HPUXNetwork is not None

# Generated at 2022-06-13 01:39:21.401106
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    module = MockModule()
    network_collector = HPUXNetworkCollector(module=module)
    network_collector._get_collector_platform = Mock(return_value=network_collector._platform)
    network = HPUXNetwork(module=module)
    result = network.populate()

    assert result['default_interface'] == 'lan0'
    assert result['default_gateway'] == '10.2.56.254'
    assert result['interfaces'][0] == 'lan0'
    assert result['lan0']['device'] == 'lan0'
    assert result['lan0']['ipv4']['address'] == '10.2.56.175'
    assert result['lan0']['ipv4']['network'] == '10.2.56.0'


#

# Generated at 2022-06-13 01:39:25.805610
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    module = Network()
    module.run_command = lambda cmd: (0, 'default:192.168.1.1:8.8.8.8:eth0', '')
    network_facts = HPUXNetwork()
    network_facts.module = module
    expected_result = {'default_interface': 'eth0',
                       'default_gateway': '192.168.1.1'}
    assert network_facts.get_default_interfaces() == expected_result


# Generated at 2022-06-13 01:39:26.978127
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    network = HPUXNetwork(dict(), dict())
    assert network.platform == 'HP-UX'



# Generated at 2022-06-13 01:39:28.741407
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    assert HPUXNetworkCollector._fact_class == HPUXNetwork
    assert HPUXNetworkCollector._platform == 'HP-UX'

# Generated at 2022-06-13 01:39:30.662486
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    h = HPUXNetworkCollector()
    assert h.platform == 'HP-UX'
    assert h.fact_class == HPUXNetwork


# Generated at 2022-06-13 01:39:33.373253
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    """ test the HPUXNetworkCollector constructor """
    hn = HPUXNetworkCollector()
    assert hn.platform == 'HP-UX'
    assert hn._fact_class == HPUXNetwork


# Generated at 2022-06-13 01:39:52.624683
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    from ansible.module_utils.facts.network.hpuxtest_get_interfaces_info import HPUXNetwork
    network = HPUXNetwork()
    network.netstat_path = r"/usr/bin/netstat"
    result = network.get_interfaces_info()

# Generated at 2022-06-13 01:40:01.260548
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    expected_default_gateway = "172.16.0.1"
    expected_default_interface = "lan0"
    expected_interfaces = ['lan0']
    expected_interface_lan0 = {'ipv4': {'address': '172.16.0.169',
                                        'network': '172.16.0.0',
                                        'interface': 'lan0'},
                               'device': 'lan0'}
    expected_network_facts = {'default_interface': expected_default_interface,
                              'default_gateway': expected_default_gateway,
                              'interfaces': expected_interfaces,
                              'lan0': expected_interface_lan0}
    network = HPUXNetwork()
    network_facts = network.populate()
    assert expected_network_facts == network_facts

# Generated at 2022-06-13 01:40:11.643399
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    mod = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True)
    network = HPUXNetwork(mod)
    result = network.populate()
    assert result['default_interface'].startswith('lan')
    assert result['default_gateway'] == '172.16.22.2'
    assert result['lo0']['ipv4']['address'] == '127.0.0.1'
    assert result['lo0']['ipv4']['network'] == '127.0.0'
    assert result['lo0']['ipv4']['interface'] == 'lo0'
    assert result['lo0']['device'] == 'lo0'

# Generated at 2022-06-13 01:40:20.152546
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    mod = MockModule()
    mod.run_command = Mock(return_value=(0,
                                         "lan0      default        "
                                         "192.168.7.1        UG        22       0        0 lan0\n",
                                         ""))
    mod.get_bin_path = Mock(return_value='/usr/bin/netstat')
    HPUXNetwork.module = mod
    default_interfaces_facts = HPUXNetwork().get_default_interfaces()
    assert default_interfaces_facts['default_interface'] == 'lan0'
    assert default_interfaces_facts['default_gateway'] == '192.168.7.1'



# Generated at 2022-06-13 01:40:25.543778
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    """Unit test for constructor of class HPUXNetwork"""
    from ansible.module_utils.facts.network.hpu_ux import HPUXNetwork
    network = HPUXNetwork(
        {'ANSIBLE_MODULE_ARGS': {}},
        {},
        {}
    )
    assert network.platform == 'HP-UX'

# Generated at 2022-06-13 01:40:27.465272
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    h_n = HPUXNetwork({})

    assert isinstance(h_n, HPUXNetwork) is True


# Generated at 2022-06-13 01:40:29.000632
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    myNetwork = HPUXNetwork()
    assert HPUXNetwork.platform == 'HP-UX'


# Generated at 2022-06-13 01:40:35.588950
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    facts_class = HPUXNetwork()
    out = "default           172.16.46.1 M         UG         0 0        en0"
    facts_class.module= AnsibleModuleMock("netstat -nr", out, 0)
    assert facts_class.get_default_interfaces() == \
        {'default_interface': 'en0', 'default_gateway': '172.16.46.1'}



# Generated at 2022-06-13 01:40:36.542016
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    HPUXNetworkCollector()

# Generated at 2022-06-13 01:40:38.430073
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    network = HPUXNetwork(dict())
    assert network


# Generated at 2022-06-13 01:41:01.155616
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    module = AnsibleModule(argument_spec={})
    network_collector = HPUXNetworkCollector()
    network_obj = network_collector.get_network_facts(module)
    assert network_obj._platform == "HP-UX"

# Generated at 2022-06-13 01:41:04.775911
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    network_collector = HPUXNetworkCollector(module=None)
    assert network_collector._fact_class == HPUXNetwork
    assert network_collector._platform == 'HP-UX'

# Generated at 2022-06-13 01:41:07.516920
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    h = HPUXNetworkCollector()
    assert(h.platform == 'HP-UX')
    assert(h.fact_class == HPUXNetwork)


# Generated at 2022-06-13 01:41:08.377991
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    return None


# Generated at 2022-06-13 01:41:10.949453
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    hn = HPUXNetwork()
    assert isinstance(hn, Network)

# Generated at 2022-06-13 01:41:18.401542
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    network_facts = HPUXNetwork().populate()

    assert network_facts['default_interface'] == 'lan2'
    assert network_facts['default_gateway'] == '10.0.0.1'
    assert len(network_facts['interfaces']) == 2
    assert 'lan2' in network_facts['interfaces']
    assert 'lan3' in network_facts['interfaces']
    assert network_facts['lan2']['ipv4']['address'] == '10.0.0.15'
    assert network_facts['lan2']['ipv4']['network'] == '10.0.0.0'

# Generated at 2022-06-13 01:41:24.884692
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    # create a HPUXNetwork object
    hn = HPUXNetwork({})
    # create an expected result
    expected_interfaces = {'lan0': {'device': 'lan0', 'ipv4': {'interface': 'lan0',
                           'network': '127.0.0.0', 'address': '127.0.0.1'}}}
    # declare a variable to hold the result
    result = {}
    # invoke the method to be tested
    result = hn.get_interfaces_info()
    # compare the result with the expected result
    assert expected_interfaces == result, 'Expected: %s, got: %s' % (expected_interfaces, result)

# Generated at 2022-06-13 01:41:29.977734
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    import sys
    import json
    import mock
    import os

    class MockOS(object):
        def __init__(self, module):
          self.module = module

        def get_bin_path(self, path):
            return "/usr/bin/netstat"

        def run_command(self, cmd):
            if cmd == '/usr/bin/netstat -nr':
                out = 'default 0.0.0.0 128.144.136.1 UG 0 0 0 lan2\n' \
                      'default 10.32.159.254 10.32.159.24 UG 0 0 0 lan1'

# Generated at 2022-06-13 01:41:33.519490
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    net = HPUXNetwork()

    net.module.run_command = run_command
    default_interfaces = net.get_default_interfaces()
    assert default_interfaces['default_interface'] == 'lan1'
    assert default_interfaces['default_gateway'] == '10.0.2.2'


# Generated at 2022-06-13 01:41:39.551306
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    network_info = HPUXNetwork({'module_setup': True}).get_interfaces_info()
    # The test assumes that the host machine has at least one lan interface
    assert 'device' in network_info[next(iter(network_info))]
    assert 'ipv4' in network_info[next(iter(network_info))]
    assert 'address' in network_info[next(iter(network_info))]['ipv4']
    assert 'network' in network_info[next(iter(network_info))]['ipv4']

# Generated at 2022-06-13 01:42:21.866083
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    net_getter = HPUXNetwork()
    expected_result = {'default_gateway': '192.168.0.1',
                       'default_interface': 'lan0'}
    res = net_getter.get_default_interfaces()
    assert res == expected_result



# Generated at 2022-06-13 01:42:26.717478
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    hn = HPUXNetwork()
    hn.module = FakeModule("netstat", "netstat_rc", "netstat_out", "netstat_err")
    result = hn.get_default_interfaces()
    assert result == {'default_interface': 'lan0', 'default_gateway': '192.168.1.1'}



# Generated at 2022-06-13 01:42:30.648888
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    from ansible.module_utils.basic import AnsibleModule
    collected_facts = {"default_interface": "lan0",
                       "default_gateway": "10.10.10.1"}

    module = AnsibleModule(argument_spec={})
    module.run_command = lambda *args, **kwargs: (0,
                                                  '/usr/bin/netstat -r', '')
    network = HPUXNetwork(module)
    interfaces = network.get_default_interfaces()
    assert interfaces == collected_facts



# Generated at 2022-06-13 01:42:37.472023
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    net = HPUXNetwork()
    interfaces = net.get_interfaces_info()
    assert interfaces != {}
    for iface in interfaces.keys():
        assert iface is not None
        assert interfaces[iface]['ipv4']['address'] is not None
        assert interfaces[iface]['ipv4']['network'] is not None


# Generated at 2022-06-13 01:42:39.165485
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    network_collector = HPUXNetworkCollector()
    assert network_collector._fact_class == HPUXNetwork


# Generated at 2022-06-13 01:42:45.029636
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    m = HPUXNetwork()
    default_interfaces = m.get_default_interfaces()
    assert default_interfaces['default_interface'] == 'lan0'
    assert default_interfaces['default_gateway'] == '148.175.51.253'


# Generated at 2022-06-13 01:42:49.288133
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    module = MockHPUXModule()
    network = HPUXNetwork(module)

    network_facts = network.get_default_interfaces()
    assert network_facts['default_interface'] == 'lan1'
    assert network_facts['default_gateway'] == '172.16.1.1'



# Generated at 2022-06-13 01:42:52.658530
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    network = HPUXNetwork()
    default_interfaces = network.get_default_interfaces()
    assert default_interfaces == {'default_interface': 'lan3',
                                  'default_gateway': '146.186.200.1'}


# Generated at 2022-06-13 01:42:55.159157
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    PLATFORM = 'HP-UX'
    network_fact = HPUXNetworkCollector(facts=None)
    assert network_fact.platform == PLATFORM


# Generated at 2022-06-13 01:43:03.595553
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    fact = HPUXNetwork()

    rc, out, err = fact.module.run_command('/usr/bin/netstat -nr')
    lines = out.splitlines()

    for line in lines:
        words = line.split()
        if len(words) > 1:
            if words[0] == 'default':
                default_interface = words[4]
                default_gateway = words[1]

    default_interfaces_facts = fact.get_default_interfaces()
    assert default_interfaces_facts['default_interface'] == default_interface
    assert default_interfaces_facts['default_gateway'] == default_gateway


# Generated at 2022-06-13 01:44:41.720968
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    module = MockModule()
    net = HPUXNetwork(module)
    net.populate()
    assert module.exit_json.called
    assert module.exit_json_args['ansible_facts']['default_interface'] == 'lan1000'
    assert module.exit_json_args['ansible_facts']['default_gateway'] == '10.10.0.1'
    assert module.exit_json_args['ansible_facts']['interfaces'] == ['lan0', 'lan1000']
    assert module.exit_json_args['ansible_facts']['lan1000']['ipv4']['address'] == '10.10.0.1'

# Generated at 2022-06-13 01:44:44.285442
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    """
    Test method get_interfaces_info of class HPUXNetwork
    """
    HPUXNetwork = HPUXNetwork()
    interfaces_dict = HPUXNetwork.get_interfaces_info()

    assert isinstance(interfaces_dict, dict)

# Generated at 2022-06-13 01:44:50.057887
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    class FakeModule(object):
        def run_command(self, cmd):
            return 0, 'default 10.10.10.1 UG lan0', None

    network = HPUXNetwork(module=FakeModule())
    default_facts = network.get_default_interfaces()
    assert default_facts['default_interface'] == 'lan0'
    assert default_facts['default_gateway'] == '10.10.10.1'



# Generated at 2022-06-13 01:44:51.591910
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    obj = HPUXNetworkCollector()
    assert obj._fact_class == HPUXNetwork

# Generated at 2022-06-13 01:44:58.096197
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    module = AnsibleModule(argument_spec={})
    hpn = HPUXNetwork(module)
    out = hpn.populate()
    assert out.get('default_interface') is not None
    assert out.get('default_gateway') is not None
    assert 'interfaces' in out
    for interface in out['interfaces']:
        assert 'device' in interface
        assert 'ipv4' in interface
        assert 'address' in interface['ipv4']
        assert 'network' in interface['ipv4']
        assert 'interface' in interface['ipv4']
    module.exit_json(ansible_facts={'ansible_net_' + key: out[key] for key in out})

# Generated at 2022-06-13 01:45:00.992995
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    net_facts = HPUXNetwork()
    assert net_facts._platform == 'HP-UX'
    assert net_facts._fact_class.__name__ == 'HPUXNetwork'
    assert net_facts._fact_class._platform == 'HP-UX'


# Generated at 2022-06-13 01:45:03.301352
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    n = HPUXNetwork()
    assert n is not None


# Generated at 2022-06-13 01:45:09.117663
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
   # Create an empty object of class HPUXNetworkCollector
   network_collector = HPUXNetworkCollector()
   # Assert that _fact_class of network_collector is equal to HPUXNetwork
   assert network_collector._fact_class == HPUXNetwork
   # Assert that _platform of network is equal to HP-UX
   assert network_collector._platform == 'HP-UX'


# Generated at 2022-06-13 01:45:10.642642
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    net_coll = HPUXNetworkCollector()
    assert net_coll.platform == 'HP-UX'

# Generated at 2022-06-13 01:45:15.297594
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    interfaces = {'lan0': {'device': u'lan0',
                           'ipv4': {'address': u'127.0.0.1',
                                    'network': u'127',
                                    'interface': u'lan0'}}}
    HPUX_Network = HPUXNetwork()
    assert interfaces == HPUX_Network.get_interfaces_info()