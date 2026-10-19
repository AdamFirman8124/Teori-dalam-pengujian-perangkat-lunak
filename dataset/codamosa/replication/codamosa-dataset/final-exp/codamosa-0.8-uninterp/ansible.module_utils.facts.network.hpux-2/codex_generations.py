

# Generated at 2022-06-13 01:37:49.672771
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    m = Network()
    assert m.platform is None
    assert m.default_interface is None
    assert m.interfaces is None

    m = HPUXNetwork()
    assert m.platform == 'HP-UX'
    assert m.default_interface is None
    assert m.interfaces is None
    assert m.facts['default_interface'] is None
    assert m.facts['interfaces'] is None


# Generated at 2022-06-13 01:37:59.611874
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )

    fixture_path = os.path.join(fixture_path, 'module_utils/facts/network')
    test_output_path = os.path.join(fixture_path, 'hpux_netstat_output')

    net_utils = HPUXNetwork(module)
    default_interface_facts = net_utils.get_default_interfaces(test_output_path)

    expected_result = {
        'default_interface': 'lan1',
        'default_gateway': '1.2.3.4'
    }

    assert default_interface_facts == expected_result


# Generated at 2022-06-13 01:38:09.732606
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    network = HPUXNetwork()
    network.module = AnsibleModuleMock()
    default_interfaces_facts = {'default_interface': 'lan1',
                                'default_gateway': '10.4.0.1'}
    network.module.run_command.return_value = (0, '', '')
    network.get_default_interfaces = \
        MagicMock(return_value=default_interfaces_facts)

# Generated at 2022-06-13 01:38:14.544756
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    from ansible.module_utils.facts.network.hpux import HPUXNetwork
    fact_network_object = HPUXNetwork({'module': {'run_command': run_command_mock}})
    default_interfaces = fact_network_object.get_default_interfaces()
    assert default_interfaces == {'default_interface': 'lan0',
                                  'default_gateway': '10.78.16.1'}



# Generated at 2022-06-13 01:38:20.215387
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    module = AnsibleModule(argument_spec=dict(), supports_check_mode=True)

    network = HPUXNetwork(module=module, collected_facts=dict())

    interfaces = network.get_default_interfaces()
    for name in interfaces.keys():
        assert type(interfaces[name]) == type('')



# Generated at 2022-06-13 01:38:21.983564
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    hpux_network = HPUXNetwork()
    assert hpux_network is not None


# Generated at 2022-06-13 01:38:30.672563
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    module = AnsibleModule(argument_spec={})

# Generated at 2022-06-13 01:38:31.987202
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    net_HPUXNetwork = HPUXNetwork()
    assert net_HPUXNetwork is not None


# Generated at 2022-06-13 01:38:42.635190
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    from ansible.module_utils.facts.hardware.hpux_network import HPUXNetwork

    out = '''
lan0: flags=104857<UP,LOOPBACK,RUNNING,MULTICAST,IPv4> mtu 4700
        inet 127.0.0.1 netmask ffffff00 broadcast 127.255.255.255
lan1: flags=104857<UP,LOOPBACK,RUNNING,MULTICAST,IPv4> mtu 1500
        inet 192.168.0.1 netmask ffffff00 broadcast 192.168.0.255
'''
    hn = HPUXNetwork({}, False)
    interfaces = hn.get_interfaces_info(out)

# Generated at 2022-06-13 01:38:53.531735
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    net = HPUXNetwork()
    interfaces = net.get_interfaces_info()
    assert 'lan0' in interfaces
    assert 'address' in interfaces['lan0']
    assert 'network' in interfaces['lan0']
    assert 'interface' in interfaces['lan0']
    assert 'device' in interfaces['lan0']
    assert interfaces['lan0']['device'] == 'lan0'
    assert interfaces['lan0']['interface'] == 'lan0'
    assert interfaces['lan0']['network'] == '172.18.150.0'
    assert interfaces['lan0']['address'] == '00:0c:29:67:9e:81'



# Generated at 2022-06-13 01:39:09.441595
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    class MockModule(object):
        def __init__(self):
            self.module = self
            self.params = {}
            self.checked = []

        def get_bin_path(self, executable, required=True):
            self.checked.append(executable)
            if executable == "netstat":
                return True
            else:
                return None

        def fail_json(self, *args, **kwargs):
            raise Exception('An error occurred.')


# Generated at 2022-06-13 01:39:10.972317
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    obj = HPUXNetworkCollector()
    assert obj._platform == 'HP-UX'

# Generated at 2022-06-13 01:39:13.122430
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    hpn = HPUXNetworkCollector()
    assert hpn.platform == 'HP-UX'
    assert hpn._fact_class == HPUXNetwork

# Generated at 2022-06-13 01:39:22.208297
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    module = AnsibleModule(
        argument_spec={},
        supports_check_mode=True,
    )
    network_facts = HPUXNetwork().populate()

    if 'default_interface' in network_facts:
        module.exit_json(
            default_interface=network_facts['default_interface'],
            default_gateway=network_facts['default_gateway'],
            ansible_facts=network_facts
        )
    else:
        module.exit_json(ansible_facts=network_facts)


# import module snippets
from ansible.module_utils.basic import AnsibleModule
if __name__ == '__main__':
    main()

# Generated at 2022-06-13 01:39:22.936169
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    # ToDo:
    pass

# Generated at 2022-06-13 01:39:30.017929
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    out1 = "default/5.5.5.5/0/0/lan0"
    out2 = "default/1.2.3.4/0/0/lan1"
    out3 = "default/6.6.6.6/0/0/lan4"
    out4 = "default/8.8.8.8/0/0/lan8"
    out_list = [out1, out2, out3, out4]
    for out in out_list:
        test_class = HPUXNetwork()
        default_interfaces = test_class.get_default_interfaces(out)
        if out == out1:
            assert default_interfaces['default_interface'] == "lan0"
            assert default_interfaces['default_gateway'] == "5.5.5.5"


# Generated at 2022-06-13 01:39:31.936492
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    facts = {}
    ansible_module = {}
    instance = HPUXNetworkCollector(ansible_module, facts)
    assert not instance is None

# Generated at 2022-06-13 01:39:39.850723
# Unit test for method get_interfaces_info of class HPUXNetwork

# Generated at 2022-06-13 01:39:43.202064
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    gdi = HPUXNetwork()
    assert gdi
    default_interfaces = gdi.get_default_interfaces()
    assert default_interfaces
    assert default_interfaces['default_gateway'] == '10.0.0.1'
    assert default_interfaces['default_interface'] == 'lan0'


# Generated at 2022-06-13 01:39:48.812918
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    net = HPUXNetwork()

# Generated at 2022-06-13 01:39:56.455267
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    hpnp = HPUXNetworkCollector()
    assert hpnp.platform == 'HP-UX'


# Generated at 2022-06-13 01:40:01.830315
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    module = MockModule()
    module.run_command = Mock(return_value=(0, mock_default_interfaces(), ''))
    hpux_network = HPUXNetwork(module)
    network_facts = hpux_network.populate()
    expected_network_facts = {'default_interface': 'lan1',
                              'default_gateway': '10.101.1.1'}
    assert network_facts['default_interface'] == expected_network_facts['default_interface']
    assert network_facts['default_gateway'] == expected_network_facts['default_gateway']



# Generated at 2022-06-13 01:40:07.726983
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    network = HPUXNetwork()
    assert network.populate() is not None
    assert network.populate().get('metadata')['network']['interfaces'] is not None
    assert network.populate().get('metadata')['network']['default_interface'] is not None
    assert network.populate().get('metadata')['network']['default_gateway'] is not None


# Generated at 2022-06-13 01:40:16.156666
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    """
    Return a dictionary of all interfaces having an assigned IPv4 address,
    plus the default interface and gateway.
    """
    net = HPUXNetwork()
    netstat_path = net.module.get_bin_path('netstat')

    if netstat_path is None:
        return

    network_facts = {}
    interfaces = net.get_interfaces_info()

    assert len(interfaces) == 2
    assert 'lan0' in interfaces
    assert 'lan1' in interfaces
    assert interfaces['lan0']['ipv4']['address'] == '12.0.0.1'
    assert interfaces['lan0']['ipv4']['network'] == '12.0.0.0'

# Generated at 2022-06-13 01:40:22.666807
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    moduleArgs = {'path': ['/bin/', '/sbin/', '/usr/bin/', '/usr/sbin/']}
    module = AnsibleModule(argument_spec=moduleArgs)

    net = HPUXNetwork(module)

    # Sample output from netstat -niw command

# Generated at 2022-06-13 01:40:26.611987
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    """Test case to check the constructor of HPUXNetworkCollector
    """
    network_collector = HPUXNetworkCollector()
    assert network_collector is not None
    assert network_collector._fact_class == HPUXNetwork
    assert network_collector._platform == 'HP-UX'


# Generated at 2022-06-13 01:40:35.875854
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    net = HPUXNetwork({})
    interfaces = net.get_interfaces_info()
    assert isinstance(interfaces, dict), interfaces
    for interface in interfaces:
        assert isinstance(interface, str), interface
        assert isinstance(interfaces[interface], dict), interfaces[interface]
        assert isinstance(interfaces[interface]['ipv4'], dict), interfaces[interface]['ipv4']
        assert isinstance(interfaces[interface]['ipv4']['address'], str), interfaces[interface]['ipv4']['address']
        assert isinstance(interfaces[interface]['ipv4']['network'], str), interfaces[interface]['ipv4']['network']

# Generated at 2022-06-13 01:40:38.934708
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    print('Executing test: test_HPUXNetwork_get_interfaces_info')
    message = 'Remove this line and write the test'
    print(message)

# Generated at 2022-06-13 01:40:48.540555
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    """ Test method get_interfaces_info of class HPUXNetwork """
    from ansible.module_utils.facts.network.hpux import HPUXNetwork
    network_obj = HPUXNetwork()
    ipv4 = network_obj.get_interfaces_info()
    # Check if default gateway and default interface is defined
    assert 'default_interface' in ipv4
    assert 'default_gateway' in ipv4
    # Check if ipv4 interface is defined
    assert 'lan1' in ipv4
    assert 'network' in ipv4['lan1']['ipv4']
    assert 'interface' in ipv4['lan1']['ipv4']
    assert 'address' in ipv4['lan1']['ipv4']

# Generated at 2022-06-13 01:40:50.825533
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    network_col = HPUXNetworkCollector(None)
    assert network_col._fact_class == HPUXNetwork
    assert network_col._platform == 'HP-UX'

# Generated at 2022-06-13 01:41:05.561694
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    """
    Unit test for method populate of class HPUXNetwork
    """
    HPUXNetwork_obj = HPUXNetwork()

    assert HPUXNetwork_obj.populate() == {}

# Generated at 2022-06-13 01:41:15.930349
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts.network.hpux import HPUXNetwork
    from ansible.module_utils.facts.network.hpux import HPUXNetworkCollector

    net_collector = HPUXNetworkCollector()
    n = HPUXNetwork(None, net_collector)
    n.module = MockModule()
    n.module.run_command.return_value = (0,
                                         out_netstat,
                                         to_bytes(''))
    n.module.get_bin_path.return_value='/usr/bin/netstat'
    net_collector.add_network(n)
    facts = net_collector.gather_network_facts()
    assert(facts['default_interface'] == 'lan0')

# Generated at 2022-06-13 01:41:17.780908
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    hpux_network = HPUXNetwork()
    assert hpux_network.platform == 'HP-UX'


# Generated at 2022-06-13 01:41:25.215278
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    # create mocked module and Network-instance
    class Addr(object):
        ip = '192.168.0.1/24'
        broadcast = '192.168.0.255'
        netmask = '255.255.255.0'
        peer = None
        ptp = None
        family = socket.AF_INET

    class MockModule(object):
        run_command = lambda x: (0, '', '')
        get_bin_path = lambda x: ''

    class MockNetwork(object):
        module = MockModule()
        default_interface = 'lo'

    module = MockModule()
    network = MockNetwork()

    # execute method
    net = HPUXNetwork()
    net.module = module
    facts = net.populate()

    # test if it sets the facts in the Network instance
   

# Generated at 2022-06-13 01:41:30.573308
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():

    facts = dict(default_interface='lan0',
                 default_gateway='10.64.29.1',
                 interfaces=['lan0'],
                 lan0={'device': 'lan0',
                       'ipv4': {'address': '10.64.29.10'}})

    f = HPUXNetworkCollector()
    assert f.collect() == facts

# Generated at 2022-06-13 01:41:38.392646
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    module = AnsibleModuleMock()
    net_collector = HPUXNetworkCollector(module=module)
    network_facts = net_collector.collect()
    assert network_facts['default_interface'] == 'lan0'
    assert network_facts['default_gateway'] == '0.0.0.0'
    assert 'interfaces' in network_facts
    assert 'lan0' in network_facts['interfaces']
    assert network_facts['lan0']['device'] == 'lan0'
    assert network_facts['lan0']['ipv4']['address'] == '192.168.0.7/32'
    assert network_facts['lan0']['ipv4']['network'] == '192.168.0.7'



# Generated at 2022-06-13 01:41:41.538056
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    objHPUXNetwork = HPUXNetwork()
    assert objHPUXNetwork.platform == 'HP-UX'


# Generated at 2022-06-13 01:41:45.558646
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    m = HPUXNetwork()
    rc, out, err = m.module.run_command("/usr/bin/netstat -niw")
    ans = {"lan0": {"device": "lan0", "ipv4": {"network": "1.1.1.0",
                    "address": "1.1.1.1", "interface": "lan0"}}}
    assert m.get_interfaces_info() == ans

# Generated at 2022-06-13 01:41:47.478168
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    network_collector = HPUXNetworkCollector()
    assert network_collector._platform == HPUXNetworkCollector._platform
    assert network_collector._fact_class == HPUXNetwork

# Generated at 2022-06-13 01:41:57.689105
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    """Unit test for constructor of class HPUXNetworkCollector"""
    ansible_module = AnsibleModule(
        argument_spec={
            'gather_subset': dict(default=['!all', 'network'], type='list')
        },
        supports_check_mode=True)
    if not HAS_NETSTAT:
        ansible_module.exit_json(
            skipped=True,
            msg="The platform is missing netstat needed to gather 'network' facts."
        )
    # Create a instance of HPUXNetworkCollector
    obj = HPUXNetworkCollector(ansible_module)
    # Check the properties of object
    assert obj.platform == 'HP-UX'
    assert obj.fact_class == 'HPUXNetwork'
    assert obj.subsets == ['!all', 'network']
    #

# Generated at 2022-06-13 01:42:30.139902
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    """
    Test parser
    """
    collected_facts = {}
    collected_facts['default_interface'] = 'lan0'
    collected_facts['default_gateway'] = '1.1.1.1'
    collected_facts['interfaces'] = ['lan0', 'lan1']
    collected_facts['lan0'] = {'ipv4': {'address': '10.10.10.10', 'interface': 'lan0', 'network': '10.10.0.0'}}
    collected_facts['lan1'] = {'ipv4': {'address': '127.0.0.1', 'interface': 'lan1', 'network': '127.0.0.0'}}

    test_obj = HPUXNetwork()

# Generated at 2022-06-13 01:42:32.469486
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    HPUXNetworkCollector()

# Generated at 2022-06-13 01:42:40.765137
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    net = HPUXNetwork()
    out = dict()
    out['rc'] = 0
    out['stdout'] = """Interface: lan0  Device: lan0  Internet Address: 192.168.16.190  Subnet Mask: 255.255.255.0  Net: 192.168.16.0"""
    out['stderr'] = ''
    net.module.run_command.return_value = out
    interfaces = net.get_interfaces_info()
    assert interfaces == {'lan0': {'device': 'lan0',
                                   'ipv4': {'address': '192.168.16.190',
                                            'network': '192.168.16.0',
                                            'interface': 'lan0'}}}
    return

# Generated at 2022-06-13 01:42:52.620572
# Unit test for method get_default_interfaces of class HPUXNetwork

# Generated at 2022-06-13 01:42:55.840812
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    """
    Constructor for class HPUXNetworkCollector
    """
    hpn = HPUXNetworkCollector()
    assert hpn._fact_class is not None
    assert hpn._platform == 'HP-UX'


# Generated at 2022-06-13 01:43:04.798522
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    module = AnsibleModule(argument_spec={})
    net = HPUXNetwork(module=module)
    collected_facts = {}
    collected_facts['ansible_net_hostname'] = 'host1'
    collected_facts['ansible_all_ipv4_addresses'] = ['1.1.1.1']
    collected_facts['ansible_all_ipv4_addresses'] = ['1.1.1.1']
    facts = net.populate(collected_facts)
    assert facts['default_interface'] == 'lan0'
    assert facts['default_gateway'] == '172.18.31.253'
    assert facts['interfaces'] == ['lan0', 'lan1000', 'lan2000']

# Generated at 2022-06-13 01:43:06.415015
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    a = HPUXNetworkCollector()


# Generated at 2022-06-13 01:43:13.487125
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    module = MockModule()


# Generated at 2022-06-13 01:43:23.975622
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    class TestModule(object):

        def __init__(self):
            self.run_command_called = False
            self.run_command_count = 0

        def get_bin_path(self, arg):
            return '/usr/bin/netstat'

        def run_command(self, arg):
            self.run_command_called = True
            self.run_command_count += 1

# Generated at 2022-06-13 01:43:33.399712
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    out_netstat_nr_1 = (
        'default         123.4.56.789 UG        0 0        0 lan0\n'
        '123.4           10.123.45.0   U         0 0        0 lan1\n'
        '123.12          10.9.8.0      U         0 0        0 lan2\n'
    )


# Generated at 2022-06-13 01:44:32.726346
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    hpn = HPUXNetwork({})
    assert hpn.platform == 'HP-UX'

# Generated at 2022-06-13 01:44:34.172218
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    net = HPUXNetwork(None)
    assert net.platform == net.__class__.platform

# Generated at 2022-06-13 01:44:37.959235
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    fact_class = HPUXNetworkCollector._fact_class
    platform = HPUXNetworkCollector._platform
    fact_class_obj = fact_class()

    # Check if the platform and fact class attributes are set correctly
    assert fact_class_obj.platform == platform

# Generated at 2022-06-13 01:44:39.526243
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    net = HPUXNetwork()
    assert 'lan0' in net.get_interfaces_info()


# Generated at 2022-06-13 01:44:46.256478
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    """Unit test for method get_interfaces_info of class HPUXNetwork.
    It does not use any real data. Instead, it defined a data structure
    for the output of command `netstat -niw` and calls the method to
    be tested.
    """
    network = HPUXNetwork()

    # This is example output of the command executed by HPUXNetwork.get_interfaces_info()

# Generated at 2022-06-13 01:44:54.989250
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():

    # mocking classes and objects
    class mock_module:
        def get_bin_path(self, cmd, required=False):
            m = {'netstat': '/usr/bin/netstat'}
            return m[cmd]

    mock_module_instance = mock_module()
    mock_module_instance.run_command = MagicMock(
        return_value=(
            0,  # rc
            'default 192.168.1.1 UGS 0 0 lan0\ndefault 192.168.1.1 UGS 0 0 lan1',  # out
            '')  # err
    )

    # instantiate HPUXNetwork class
    obj = HPUXNetwork()
    obj.module = mock_module_instance

    # run populate method
    obj.populate()

    # assert results
    assert obj.default_

# Generated at 2022-06-13 01:44:57.405882
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    network = HPUXNetwork()
    assert network


if __name__ == '__main__':
    test_HPUXNetwork()

# Generated at 2022-06-13 01:45:07.954849
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    class ModuleStub(object):
        def __init__(self, retval):
            self.retval = retval

        def run_command(self, *args, **kwargs):
            return self.retval

    input_string = """Kernel Interface table
lan0        lan0           internet      172.22.33.56     172.22.11.1     UP
lan1        lan1           internet6     fe80:1::4fe4:4c4f:4e:4c4f fe80:1::4fe4:4c4f:4e:4c4f UP"""
    retval = (0, input_string, '')
    module = ModuleStub(retval)
    network_facts = HPUXNetwork(module)
    interfaces = network_facts.get_interfaces_info()

# Generated at 2022-06-13 01:45:15.173637
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    test_module = AnsibleModule(argument_spec=dict())
    test_module.params = dict(gather_subset="min")
    result = HPUXNetwork.populate(test_module)
    assert 'interfaces' in result
    assert 'default_interface' in result
    assert result['default_interface'] == 'lan8'
    for iface in result['interfaces']:
        assert 'ipv4' in result[iface]
        assert 'address' in result[iface]['ipv4']
        assert result[iface]['ipv4']['address'] != None

# Generated at 2022-06-13 01:45:20.252971
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    hpuxnetwork = HPUXNetwork()
    interfaces = hpuxnetwork.get_default_interfaces()
    assert interfaces is not None
    assert len(interfaces) == 2
    assert interfaces['default_gateway'] == '192.0.2.2'
    assert interfaces['default_interface'] == 'lan0'



# Generated at 2022-06-13 01:47:20.762663
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    interfaces = HPUXNetwork().get_interfaces_info()
    assert interfaces is not None
    assert len(interfaces) > 0
    for interface in interfaces:
        assert interface is not None
        assert interfaces[interface] is not None
        address = interfaces[interface]['ipv4']['address']
        network = interfaces[interface]['ipv4']['network']
        intf = interfaces[interface]['ipv4']['interface']
        assert address is not None and len(address) > 0
        assert network is not None and len(network) > 0
        assert intf is not None and len(intf) > 0
        assert intf == interface


# Generated at 2022-06-13 01:47:25.471233
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    """
    Class HPUXNetwork: unit test for the method get_interfaces_info
    that returns a dictionary containing network interface information.
    """

    lan_input1 = ('lan0               lan     0        0     4673938  300152'
                  '      0    0      0      0      0   300152',
                  'lan1               lan     0        1     9131801   '
                  '59662    0    0      0      0      0    59660',
                  'lan2               lan     0        2     2455181   135580'
                  '      0    0      0      0      0   135580')

    # Test the method with lan interface data containing IP address
    class HPUXNetworkForTest(HPUXNetwork):

        def get_interfaces_info(self):
            return HPUX

# Generated at 2022-06-13 01:47:30.474005
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    network = HPUXNetwork()
    def_out = """default <GATEWAY> UGS 0 1000 - hdi nic0
default <GATEWAY> UGS 0 1000 - bsdi nic0
default 127.0.0.1 UG 0 0 32768 lo0
"""
    default_interfaces = network.get_default_interfaces()
    assert default_interfaces['default_interface'] == 'nic0'
    assert default_interfaces['default_gateway'] == '<GATEWAY>'



# Generated at 2022-06-13 01:47:34.740026
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():

    class HPUXNetworkTest(HPUXNetwork):

        def __init__(self, module):
            self.module = module

    import ansible.module_utils.facts.utils

    class MockModule:
        def __init__(self):
            self.run_command_results = []

        def run_command(self, command):
            return self.run_command_results.pop()

    mock_module = MockModule()

# Generated at 2022-06-13 01:47:41.434600
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    from ansible.module_utils.facts.network.hpux.facts import HPUXNetwork
    from ansible.module_utils.facts.network.hpux.facts import HPUXNetworkCollector
    from ansible.module_utils.facts.network.hpux.facts import HPX_NETSTAT_OUT
    from ansible.module_utils.facts.network.hpux.facts import HPX_NETSTAT_OUT_SPLIT
    from ansible.module_utils.facts.network.hpux.facts import HPX_INTERFACE_INFO

    collected_facts = {'ansible_facts': {'ansible_net_gather_network_resources': HPX_NETSTAT_OUT}}

    network_collector = HPUXNetworkCollector(collected_facts=collected_facts)

    interfaces_info = network_collector._