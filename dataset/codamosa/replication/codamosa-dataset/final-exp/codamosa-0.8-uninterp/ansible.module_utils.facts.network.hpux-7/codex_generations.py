

# Generated at 2022-06-13 01:37:53.630017
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    m = HPUXNetwork({})
    from ansible.module_utils.six import PY3
    if PY3:
        from io import StringIO
    else:
        from io import BytesIO as StringIO
    test_out = StringIO(u"default  129.127.168.1   UG   1   0   lan6\n")
    m.module.run_command = lambda args: (0, test_out.getvalue(), '')
    ifaces = m.get_default_interfaces()
    assert ifaces['default_interface'] == 'lan6'
    assert ifaces['default_gateway'] == '129.127.168.1'



# Generated at 2022-06-13 01:38:05.275512
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    """
    This method is called once in the beginning of the test.
    """

    # Create an instance of HPUXNetwork class
    hpuxnet = HPUXNetwork()

    # Make a Mock object for module
    hpuxnet.module = Mock()

    # Make a Mock object for run_command method
    hpuxnet.module.run_command = Mock()

    # The return value of the first call of run_command method
    hpuxnet.module.run_command.return_value = (0,
                                               'default 119.92.221.1 UGSc 0 0 lan0',
                                               '')

    # Call the method get_default_interfaces
    default_interfaces = hpuxnet.get_default_interfaces()
    # The default_interfaces should equal to
    # {'default_interface': '

# Generated at 2022-06-13 01:38:15.013221
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    m = AnsibleModule(
        argument_spec=dict(
            gather_subset=dict(default=[], type='list')
        ),
        supports_check_mode=True
    )

    n = HPUXNetwork()
    facts = n.populate()

# Generated at 2022-06-13 01:38:16.864092
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    h = HPUXNetwork()
    assert h.platform == 'HP-UX'


# Generated at 2022-06-13 01:38:27.315912
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    import os
    import platform

    from ansible.module_utils.facts.network.hpux import HPUXNetwork, HPUXNetworkCollector

    if platform.system() != 'HP-UX':
        return {'msg': ("Unit test for method populate of class HPUXNetwork only "
                        "works on HP-UX systems"),
                'skipped': True}

    Network = HPUXNetwork()
    NetworkCollector = HPUXNetworkCollector()
    module = Network.module

    netstat_path = os.path.join(os.sep, "usr", "bin", "netstat")

# Generated at 2022-06-13 01:38:37.634307
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():

    class TestModule(object):
        def run_command(self, cmd):
            test_cmd = ("/usr/bin/netstat -niw")
            if (cmd != test_cmd):
                assert("command not as expected: expected: %s, got: %s"
                       % (test_cmd, cmd))

# Generated at 2022-06-13 01:38:40.324603
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    assert HPUXNetworkCollector._platform == "HP-UX"
    assert HPUXNetworkCollector._fact_class == HPUXNetwork

# Generated at 2022-06-13 01:38:49.182756
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    test_module = type('test_module', (object,), {})()
    test_module.run_command = run_command
    test_network = HPUXNetwork(test_module)
    result = test_network.get_default_interfaces()
    expected_result = {'default_interface': 'lan0', 'default_gateway': '192.168.165.1'}
    assert result == expected_result, 'Expected: %s but got: %s' % (expected_result, result)



# Generated at 2022-06-13 01:38:56.776340
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    netstat_command = "/usr/bin/netstat -nr"
    netstat_result = "default  192.168.1.1 UGS 0 118384 lan0\n"
    test_module = AnsibleFakeModule(netstat_command, netstat_result)
    test_network = HPUXNetwork(test_module)
    default_interfaces = test_network.get_default_interfaces()
    assert default_interfaces['default_interface'] == 'lan0'
    assert default_interfaces['default_gateway'] == '192.168.1.1'



# Generated at 2022-06-13 01:38:58.578830
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    assert HPUXNetworkCollector()._platform == 'HP-UX'

# Generated at 2022-06-13 01:39:05.043889
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    HPUXNetworkCollector()

# Generated at 2022-06-13 01:39:07.917137
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    assert HPUXNetworkCollector._platform == 'HP-UX'
    assert HPUXNetworkCollector._fact_class == HPUXNetwork


# Generated at 2022-06-13 01:39:11.699433
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    module = FakeAnsibleModule()
    network = HPUXNetwork(module)
    assert network.get_default_interfaces() == {'default_interface': 'lan3',
                                                'default_gateway': '10.10.10.1'}


# Generated at 2022-06-13 01:39:14.258080
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    obj = HPUXNetworkCollector()
    assert obj.platform == HPUXNetwork._platform
    assert obj._fact_class == HPUXNetwork


# Generated at 2022-06-13 01:39:24.215853
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    """
    This is a unit test for testing get_interfaces_info method of class
    HPUXNetwork.
    """
    out = """Name  Mtu  Net/Dest      Address        Ipkts   Ierrs     Opkts  Oerrs Coll
lan0 1500  192.168.1.0  192.168.1.24   6073136  0      9340019  0      0
lan1 1500  172.16.4.0   172.16.4.100  3247934  0      2940707  0      0"""
    interfaces = HPUXNetwork.get_interfaces_info(out)

# Generated at 2022-06-13 01:39:32.506887
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    module = NetworkCollector(dict(module_args='', ansible_facts={}))
    setattr(module, 'get_bin_path', lambda x: '')
    setattr(module, 'run_command', lambda *x, **y: ('', 'default 192.168.1.1 UGS en0', ''))
    network_facts_class = HPUXNetwork(module)
    network_facts = network_facts_class.populate()
    assert network_facts['default_interface'] == 'en0'
    assert network_facts['default_gateway'] == '192.168.1.1'
    assert len(network_facts['interfaces']) == 0
    # Test with successful execution of netstat command
    setattr(module, 'get_bin_path', lambda x: '/usr/bin/netstat')
    set

# Generated at 2022-06-13 01:39:35.432801
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    obj = HPUXNetworkCollector()
    assert obj._platform == 'HP-UX'
    assert obj._fact_class == HPUXNetwork


# Generated at 2022-06-13 01:39:39.044312
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    module = AnsibleModule(argument_spec={})
    network_facts = HPUXNetwork(module)

    # constructor should set the following attributes
    assert network_facts.platform == "HP-UX"
    assert network_facts.interfaces == []
    assert network_facts.default_interface is None
    assert network_facts.default_gateway is None
    assert network_facts.module is module



# Generated at 2022-06-13 01:39:48.446588
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    result = {}
    network_facts = HPUXNetwork()
    result['default_gateway'] = '192.168.56.2'
    result['default_interface'] = 'lan0'
    result['interfaces'] = ['lan0', 'lan1', 'lan2', 'lan3']
    result['lan0'] = {'ipv4': {'address': '192.168.56.101',
                               'network': '192.168.56.0',
                               'interface': 'lan0',
                               'address': '192.168.56.101'},
                     'device': 'lan0'}

# Generated at 2022-06-13 01:39:49.434133
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    HPUXNetworkCollector()

# Generated at 2022-06-13 01:40:07.897427
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    """ Create a fake Network object with some interfaces
        and check if correct values are returned.
    """
    module = MockModule()
    fake_module = AnsibleModule(argument_spec={})
    module.run_command = Mock(return_value=(0, out, ""))
    interface = HPUXNetwork(module, fake_module)
    default_interfaces = interface.get_default_interfaces()
    assert default_interfaces['default_interface'] == 'lan0'
    assert default_interfaces['default_gateway'] == '10.10.1.1'


# Generated at 2022-06-13 01:40:14.594444
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    ext_module = mock.MagicMock()
    ext_module.get_bin_path.return_value = '/usr/bin/netstat'
    ext_module.run_command.return_value = (0, '', '')

    n = HPUXNetwork(ext_module)
    n.populate()
    ext_module.get_bin_path.assert_called_once_with('netstat')
    ext_module.run_command.assert_any_call('/usr/bin/netstat -nr')
    ext_module.run_command.assert_any_call('/usr/bin/netstat -niw')

# Generated at 2022-06-13 01:40:17.641869
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    module = MockAnsibleModule('HP-UX')
    hpux_network = HPUXNetwork(module)
    hpux_network.populate()
    module.run_command.assert_called_once_with('/usr/bin/netstat -nr')

# Generated at 2022-06-13 01:40:19.745344
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    """Unit test for constructor of class HPUXNetworkCollector"""
    obj = HPUXNetworkCollector()
    assert obj._fact_class.platform == 'HP-UX'
    assert obj._platform == 'HP-UX'

# Generated at 2022-06-13 01:40:22.735180
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    network = HPUXNetworkCollector()
    assert network.platform == 'HP-UX'
    assert network.fact_class == HPUXNetwork

# Generated at 2022-06-13 01:40:28.018324
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    module = AnsibleModule(argument_spec={})
    set_module_args(dict(gather_subset=["all"]))
    network_collector = HPUXNetworkCollector(module=module)
    network_collector.populate()
    assert 'default_interface' in network_collector.facts
    assert 'interfaces' in network_collector.facts
    assert 'lo0' in network_collector.facts['interfaces']

# Generated at 2022-06-13 01:40:31.968087
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    class ModuleStub:
        def get_bin_path(self, arg):
            return "/usr/bin/netstat"

        def run_command(self, arg):
            return (0, _out, "")

    net = HPUXNetwork(ModuleStub())
    assert 'lan2' in net.get_interfaces_info()
    assert 'lan0' in net.get_interfaces_info()
    assert 'lan1' in net.get_interfaces_info()
    assert 'lan6' in net.get_interfaces_info()
    assert 'lan3' in net.get_interfaces_info()
    assert 'lan4' in net.get_interfaces_info()
    assert 'lan5' in net.get_interfaces_info()



# Generated at 2022-06-13 01:40:37.986365
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    """ test_HPUXNetwork_get_default_interfaces() """
    network_obj = HPUXNetwork()
    default_interfaces_facts = network_obj.get_default_interfaces()
    assert 'default_interface' in default_interfaces_facts
    assert 'default_gateway' in default_interfaces_facts


# Generated at 2022-06-13 01:40:43.887572
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    from ansible.module_utils.facts import collector

    network = collector.get_network_collector(HPUXNetworkCollector, {})
    facts = network.get_facts()
    assert 'default_interface' in facts
    assert 'default_gateway' in facts
    assert 'interfaces' in facts
    assert 'lo0' in facts['interfaces']
    assert 'lo0' in facts
    assert 'ipv4' in facts['lo0']
    assert 'address' in facts['lo0']['ipv4']
    assert 'network' in facts['lo0']['ipv4']

# Generated at 2022-06-13 01:40:50.260847
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    module = AnsibleModule(argument_spec={})

    n = HPUXNetwork()
    n.module = module
    n.module.run_command = MagicMock(return_value=(0, '', ''))
    n.get_default_interfaces = MagicMock(return_value={
        'default_interface': 'lan1', 'default_gateway': '172.24.136.1'})

# Generated at 2022-06-13 01:41:16.087304
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    test_module = NetworkCollector()
    test_HPUXNetwork = HPUXNetwork(test_module)

    test_return = test_HPUXNetwork.get_interfaces_info()
    assert('lan0' in test_return)
    assert('lan1' in test_return)
    assert('lan1000' in test_return)
    assert('lan1001' in test_return)
    assert('lan1002' in test_return)
    assert('lan1003' in test_return)



# Generated at 2022-06-13 01:41:19.010313
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    """ This is a unit test for testing the constructor of HPUXNetworkCollector
    """
    hpx = HPUXNetworkCollector()
    assert hpx.__class__.__name__ == 'HPUXNetworkCollector'

# Generated at 2022-06-13 01:41:26.042633
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    test_network = HPUXNetwork()


# Generated at 2022-06-13 01:41:32.895720
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    m = module.HPUXNetwork()
    result = m.populate()
    assert result['default_interface'] == 'lan0'
    assert result['default_gateway'] == '10.223.254.254'
    assert result['interfaces'] == result.keys()
    for k in ['lan0', 'lo0']:
        assert k in result['interfaces']
        assert result[k]['ipv4'] == {'address': '10.223.254.200',
                                     'network': '10.223.254.0',
                                     'interface': k}

# Generated at 2022-06-13 01:41:41.236098
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    module = FakeAnsibleModule()

    n = HPUXNetwork(module)
    assert n.populate() == {
        'interfaces': ['lan0', 'lan1'],
        'default_interface': 'lan0',
        'default_gateway': '192.168.7.1',
        'lan0': {'ipv4': {'network': '192.168.7.0',
                        'interface': 'lan0',
                        'address': '192.168.7.7'},
                'device': 'lan0'},
        'lan1': {'ipv4': {'network': '192.168.13.0',
                        'interface': 'lan1',
                        'address': '192.168.13.13'},
                'device': 'lan1'}
    }



# Generated at 2022-06-13 01:41:42.214733
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    hn = HPUXNetwork()
    assert hn.device == "HP-UX"


# Generated at 2022-06-13 01:41:46.004286
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    HP_UXNetwork = HPUXNetwork()
    result = HP_UXNetwork.get_interfaces_info()
    correct_result = {'lan0': {'ipv4': {'interface': 'lan0',
                                        'address': '192.168.8.0',
                                        'network': '192.168.8.0'},
                               'device': 'lan0'}}
    assert result == correct_result

# Generated at 2022-06-13 01:41:50.573733
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    hn = HPUXNetwork()
    hn.module.run_command = lambda args, check_rc=True: ["", "", ""]
    hn.populate()
    assert hn.populate() == {'default_interface': 'lan0', 'interfaces': ['lan0'],
                             'lan0': {'device': 'lan0', 'ipv4': {'interface': 'lan0',
                                                                 'network': '10.4.4.0',
                                                                 'address': '10.4.4.21'}},
                             'default_gateway': '10.4.4.1'}

# Generated at 2022-06-13 01:41:53.409862
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    hpux_network = HPUXNetworkCollector()
    assert hpux_network._fact_class is HPUXNetwork
    assert hpux_network._platform is HPUXNetwork.platform

# Generated at 2022-06-13 01:41:57.906903
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    fact_network = HPUXNetwork()

    test_data = {}
    test_data['default_line_len_4'] = 'default 127.0.0.1 UG 0 4 lo0\n'
    test_data['default_line_len_5'] = 'default 127.0.0.1 UG 0 4 lo0 lan0\n'
    test_data['default_line_len_6'] = 'default 127.0.0.1 UG 0 4 lo0 lan1062\n'
    test_data['default_line_len_7'] = 'default 127.0.0.1 UG 0 4 lo0 lan1062 lan0\n'

    default_interfaces = {}
    default_interfaces = fact_network.get_default_interfaces()
    assert 'default_interface' in default_interfaces


# Generated at 2022-06-13 01:42:50.199413
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    module = MockModule()

    # Create a HPUXNetwork object and set it up for unit testing
    fact_class = HPUXNetwork(module)
    fact_class.module.get_bin_path = Mock(return_value=True)


# Generated at 2022-06-13 01:42:51.164039
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    HPUXNetworkCollector()

# Generated at 2022-06-13 01:42:56.089688
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    module = AnsibleModule(argument_spec={})
    hpuxnetwork = HPUXNetwork(module)
    assert hpuxnetwork.default_interfaces() == {}
    assert hpuxnetwork.interfaces() == {}
    assert hpuxnetwork.__doc__ is not None
    assert hpuxnetwork.__init__ is not None

# Generated at 2022-06-13 01:42:58.314669
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    HPUXNetworkCollector()

# Generated at 2022-06-13 01:43:03.930406
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    network = HPUXNetwork()
    interfaces = network.get_interfaces_info()
    assert interfaces == {'lan0': {'device': 'lan0', 'ipv4': {'network': '10.99.99.0', 'interface': 'lan0', 'address': '10.99.99.11'}},
                          'lan1': {'device': 'lan1', 'ipv4': {'network': '10.99.99.0', 'interface': 'lan1', 'address': '10.99.99.1'}}}

# Generated at 2022-06-13 01:43:09.002438
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    module = NetworkCollector.get_instance().module
    network_facts = HPUXNetwork(module).populate()
    assert 'interfaces' in network_facts
    assert 'default_interface' in network_facts
    assert 'default_gateway' in network_facts
    for interface in network_facts['interfaces']:
        assert 'ipv4' in network_facts[interface]

# Generated at 2022-06-13 01:43:12.174174
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():

    fact_class = HPUXNetwork
    platform = 'HP-UX'

    # Test initialization of HPUXNetworkCollector class
    obj = HPUXNetworkCollector(fact_class, platform)

    assert obj.fact_class == fact_class
    assert obj.platform == platform

# Generated at 2022-06-13 01:43:18.690318
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    from ansible.module_utils.facts.network.hpux import HPUXNetwork
    expected_default_interfaces = {'default_interface': 'lan0',
                                   'default_gateway': '10.10.10.1'}
    mock_module = MockAnsibleModule()
    mock_module.run_command().splitlines.return_value = (
        ["Kernel Interface table",
         "Destination        Gateway      Flags Refs Use Mtu Interface",
         "default            10.10.10.1 UG        0   0    1500 lan0",
         "10.10.10.0         10.10.10.2 U          0   0    1500 lan0",
         "127.0.0.0          127.0.0.1 UH         0   0    32768 lo0"])

    hpux_

# Generated at 2022-06-13 01:43:28.176554
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    net = HPUXNetwork()
    ifaces = net.get_interfaces_info()
    assert (len(ifaces) > 0)
    assert('lan0' in ifaces)
    assert('lan2' in ifaces)
    assert('lan2' in ifaces.keys())
    assert('lan0' in ifaces.keys())
    assert('lan0' in ifaces)
    assert('lan2' in ifaces)
    assert('lan2' in ifaces.keys())
    assert('lan0' in ifaces.keys())
    assert('ipv4' in ifaces['lan0'].keys())
    assert(ifaces['lan0']['ipv4']['address'] != '')
    assert(ifaces['lan0']['ipv4']['network'] != '')

# Generated at 2022-06-13 01:43:33.765859
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():

    # Mocking module instance
    test_module = type('test_module', (), {
        'run_command': lambda _self, command: (0, 'lan15: flags=8043<UP,BROADCAST,RUNNING,MULTICAST>', None),
        'get_bin_path': lambda _self, _bin: '/usr/bin'
    })()

    # Mocking ansible module instance
    test_ansible_module = type('test_ansible_module', (), {
        'module': test_module
    })()

    # Creation of HPUXNetwork instance
    test_HPUXNetwork = HPUXNetwork(module=test_ansible_module)
    test_HPUXNetwork.populate()

    # Checking expected output
    interfaces = test_HPUXNetwork.get_interfaces_info()



# Generated at 2022-06-13 01:45:26.608654
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    net = HPUXNetwork()
    intercept = {'command': '/usr/bin/netstat -nr', 'rc': 0, 'stdout': 'default 223.100.0.129 UG 0 0 lan0\ndefault 10.0.0.1 UG 0 0 lan1\n'}
    net.module.run_command = intercept
    default_interfaces_facts = {'default_interface': 'lan0'}

    assert net.get_default_interfaces() == default_interfaces_facts



# Generated at 2022-06-13 01:45:31.278821
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    from ansible.module_utils.facts.network import Network as Net
    from ansible.module_utils.facts.network.hpux import HPUXNetwork
    from ansible.module_utils.facts.network.hpux import HPUXNetworkCollector

    module_mock = MagicMock()
    netstat_path = module_mock.get_bin_path.return_value = '/usr/bin/netstat'
    default_interfaces_facts = {
        'default_interface': 'lan0',
        'default_gateway': '10.0.2.2'}

# Generated at 2022-06-13 01:45:34.001244
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    nc = HPUXNetworkCollector()
    assert nc._fact_class == HPUXNetwork
    assert nc._platform == 'HP-UX'



# Generated at 2022-06-13 01:45:35.430331
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    from ansible.module_utils.facts import Network

    my_network = Network()
    assert my_network is not None

# Generated at 2022-06-13 01:45:41.681879
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    # Example data for netstat -nr
    nr_data = "default 192.168.0.1 UG 0 0 0 lan0\n" + \
              "192.168.0.0 192.168.1.1 U 0 0 0 lan0\n" + \
              "192.168.1.0 192.168.0.1 U 0 0 0 lan0\n"
    # Example data for netstat -niw

# Generated at 2022-06-13 01:45:50.618360
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    class MockModule:
        def run_command(self, command):
            return (0,
                    'lan0      lan0    UP             192.168.1.100  192.168.1.0   \n'
                    'lan1      lan1    UP             192.168.1.100  192.168.1.0   \n'
                    'lan2      lan2    DOWN           192.168.1.100  192.168.1.0   \n',
                    '')

    network = HPUXNetwork(MockModule())
    interfaces = network.get_interfaces_info()
    assert interfaces['lan0']['ipv4']['address'] == '192.168.1.100'



# Generated at 2022-06-13 01:45:52.338559
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    module = MockModule()
    network = HPUXNetwork(module)
    network.get_default_interfaces()


# Generated at 2022-06-13 01:45:58.424932
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    from ansible.module_utils.facts.network.hpux import HPUXNetwork
    network_facts = HPUXNetwork().populate()
    assert 'default_interface' in network_facts
    assert 'default_gateway' in network_facts
    assert 'interfaces' in network_facts
    assert 'lo0' in network_facts
    assert 'default_interface' in network_facts
    assert 'default_gateway' in network_facts
    assert 'interfaces' in network_facts
    assert 'lo0' in network_facts
    iface = 'lo0'
    assert 'device' in network_facts[iface]
    assert 'ipv4' in network_facts[iface]
    assert 'address' in network_facts[iface]['ipv4']

# Generated at 2022-06-13 01:46:07.708683
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    from ansible.module_utils.facts.network.hpux.get_default_interfaces import HPUXNetwork
    from ansible.module_utils.six import StringIO

    dc = HPUXNetwork()

    class FakeModule(object):
        def __init__(self, *args, **kwargs):
            self.run_command = lambda *args, **kwargs: (0, StringIO(args[0]), '')
            self.params = {'gather_subset': ['!all', '!min']}

    dc.module = FakeModule()

    expected_value = dict(default_interface='lan0', default_gateway='10.0.3.1')
    output = dc.get_default_interfaces()
    assert output == expected_value



# Generated at 2022-06-13 01:46:18.474353
# Unit test for method get_interfaces_info of class HPUXNetwork