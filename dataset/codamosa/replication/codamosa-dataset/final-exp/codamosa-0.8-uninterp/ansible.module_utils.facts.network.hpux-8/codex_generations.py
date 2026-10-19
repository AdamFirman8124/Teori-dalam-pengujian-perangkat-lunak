

# Generated at 2022-06-13 01:37:52.541167
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    test_module = AnsibleModuleMock()
    klass = HPUXNetwork(test_module)
    rc = 0

# Generated at 2022-06-13 01:37:57.991401
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    network_facts = {}
    default_interfaces = {}
    default_interfaces['default_interface'] = 'lan0'
    default_interfaces['default_gateway'] = '10.17.180.97'
    network_facts.update(default_interfaces)

    assert HPUXNetwork().get_default_interfaces() == network_facts



# Generated at 2022-06-13 01:38:07.886490
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    class MockModule(object):
        """Mock class to return the interface info."""
        def __init__(self):
            self.result = [0, """lan0        Link encap:Ethernet  HWaddr 00:01:86:01:53:60
          inet addr:9.4.175.252  Bcast:9.4.175.255  Mask:255.255.255.0""", '']

        def run_command(self, cmd):
            return self.result

    hpuxt_network = HPUXNetwork(MockModule())

    result = hpuxt_network.get_interfaces_info()
    assert result['lan0']['device'] == 'lan0'
    assert result['lan0']['ipv4']['address'] == '9.4.175.252'
   

# Generated at 2022-06-13 01:38:10.746007
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    """ This function unit test get_interfaces_info method of class HPUXNetwork
    """
    network = HPUXNetwork()
    interfaces = network.get_interfaces_info()

    assert 'lan0' in interfaces

# Generated at 2022-06-13 01:38:11.717946
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    net_facts = HPUXNetwork()
    print(net_facts)


# Generated at 2022-06-13 01:38:13.989579
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    network_facts = HPUXNetwork()
    assert network_facts.populate()['interfaces'] == [u'lan0', u'lan1']
    assert network_facts.populate()['lan1']['ipv4']['network'] == '192.168.1.0'

# Generated at 2022-06-13 01:38:15.344771
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    collector = HPUXNetworkCollector()
    assert collector._fact_class.platform == 'HP-UX'

# Generated at 2022-06-13 01:38:18.964598
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    hpux_collector = HPUXNetworkCollector()
    assert hpux_collector.fact_class == HPUXNetwork
    assert hpux_collector.platform == 'HP-UX'

# Generated at 2022-06-13 01:38:25.374921
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    from ansible.module_utils import basic
    m = basic.AnsibleModule(
    )
    interfaces = HPUXNetwork().get_interfaces_info()
    for i in interfaces:
        iface = interfaces[i]
        if iface['device'] == 'lan1000':
            assert iface['ipv4']['address'] == '10.10.10.11'
            assert iface['ipv4']['network'] == '10.10.10.0'


# Generated at 2022-06-13 01:38:30.388461
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    network_facts = HPUXNetwork()

    default_interfaces_facts = network_facts.get_default_interfaces()
    assert len(default_interfaces_facts) == 2
    default_interface = default_interfaces_facts['default_interface']
    assert default_interface == 'lan5'
    default_gateway = default_interfaces_facts['default_gateway']
    assert default_gateway == '10.0.0.1'



# Generated at 2022-06-13 01:38:44.566724
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    from ansible.module_utils.facts.network.hpux import HPUXNetwork
    from ansible_collections.notstdlib.moveitallout.tests.unit.compat.mock import patch
    from ansible.utils.path import unfrackpath

    mock_module_path = 'ansible_collections.notstdlib.moveitallout.plugins.module_utils.facts.network.hpux.HPUXNetwork'

# Generated at 2022-06-13 01:38:50.014610
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    n = HPUXNetwork()
    test_input = "default  150.11.67.1        UG    0    0        lan0"
    n.module.run_command.return_value = (0, test_input, '')
    assert n.get_default_interfaces() == {'default_interface': 'lan0', 'default_gateway': '150.11.67.1'}


# Generated at 2022-06-13 01:38:57.760099
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    module = AnsibleModule(
        argument_spec=dict(
            gather_subset=dict(default=['!all'], type='list'),
            gather_timeout=dict(default=10, type='int')
        ),
        supports_check_mode=True
    )

    n = HPUXNetwork(module)
    default_interfaces = n.get_default_interfaces()
    assert isinstance(default_interfaces, dict)
    assert 'default_interface' in default_interfaces
    assert 'default_gateway' in default_interfaces



# Generated at 2022-06-13 01:39:09.113462
# Unit test for method get_interfaces_info of class HPUXNetwork

# Generated at 2022-06-13 01:39:20.371827
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    network_module = HPUXNetwork({})
    network_module.module.run_command = mock_get_interfaces_list
    interfaces = network_module.get_interfaces_info()


# Generated at 2022-06-13 01:39:22.729155
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    collector = HPUXNetworkCollector()

    assert isinstance(collector, NetworkCollector)
    assert collector._platform == 'HP-UX'
    assert collector._fact_class == HPUXNetwork

# Generated at 2022-06-13 01:39:29.960234
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    interfaces = {'lan0': {'device': 'lan0',
                           'ipv4': {'address': '172.17.0.2/24',
                                    'network': '172.17.0.0', 'interface': 'lan0'}},
                  'lan1': {'device': 'lan1',
                           'ipv4': {'address': '172.18.0.2/16',
                                    'network': '172.18.0.0', 'interface': 'lan1'}}}
    interface_object = HPUXNetwork()
    assert interfaces == interface_object.get_interfaces_info()

# Generated at 2022-06-13 01:39:33.022874
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    module = AnsibleModule(argument_spec={})
    network_obj = HPUXNetwork(module)
    test_interfaces = network_obj.get_interfaces_info()
    for interface in test_interfaces:
        print("Interface: %s" % (interface))

# Generated at 2022-06-13 01:39:40.652981
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    module = AnsibleModule(argument_spec={})
    network = HPUXNetwork(module=module)
    interfaces = {'lan0': {'ipv4': {'address': '192.168.56.7',
                                    'network': '192.168.56.0',
                                    'interface': 'lan0'},
                           'device': 'lan0'},
                  'lan1': {'ipv4': {'address': '192.168.57.7',
                                    'network': '192.168.57.0',
                                    'interface': 'lan1'},
                           'device': 'lan1'}}
    default_interfaces = {'default_interface': 'lan0',
                          'default_gateway': '192.168.56.2'}
    network_facts = network.populate()

# Generated at 2022-06-13 01:39:42.734556
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    HPUXNet = HPUXNetwork()
    HPUXNet._module.run_command = fake_run_command

    assert HPUXNet.get_default_interfaces() == {'default_gateway': '127.0.0.1', 'default_interface': 'lan0'}


# Generated at 2022-06-13 01:39:51.622756
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    assert(HPUXNetwork.get_default_interfaces(['default 192.168.10.1 UG lan40']) == {'default_interface': 'lan40', 'default_gateway': '192.168.10.1'})

# Generated at 2022-06-13 01:39:54.940128
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    """ Unit test for constructor of class HPUXNetwork """
    hpu_netw = HPUXNetwork('Network')
    assert hpu_netw.platform == 'HP-UX'


# Generated at 2022-06-13 01:39:57.508231
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    net_obj = HPUXNetwork()
    module = AnsibleModule(argument_spec={})
    net_obj.module = module
    net_obj.populate()
    assert module.exit_json.called

# Generated at 2022-06-13 01:39:59.214891
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    hn = HPUXNetworkCollector()
    assert hn._fact_class == HPUXNetwork
    assert hn._platform == 'HP-UX'

# Generated at 2022-06-13 01:40:00.744968
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    assert HPUXNetwork


# Generated at 2022-06-13 01:40:02.404289
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    hn = HPUXNetworkCollector.__new__(HPUXNetworkCollector)

# Generated at 2022-06-13 01:40:12.448957
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    hpx_net = HPUXNetwork()
    out = '''
lan0       Link encap:Ethernet  HWaddr 00:01:04:dd:b1:a1
           inet addr:192.168.10.117  Bcast:192.168.10.255  Mask:255.255.255.0
           UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
           RX packets:5826799 errors:0 dropped:0 overruns:0 frame:0
           TX packets:1349166 errors:0 dropped:0 overruns:0 carrier:0
           collisions:0 txqueuelen:0
           RX bytes:113524269 (108.2 MiB)  TX bytes:38465400 (36.6 MiB)
'''

# Generated at 2022-06-13 01:40:13.210184
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    HPUXNetworkCollector()

# Generated at 2022-06-13 01:40:19.847244
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    # Set of facts gathered from /usr/bin/netstat -nr on a HP-UX system
    output = "Routing tables\n" \
             "default 17.251.0.1 UG 1 6 lan1000\n" \
             "123.456.789.0 123.456.789.1 UH 2 5 lan0\n"
    module = MagicMock()
    module.run_command = Mock(return_value=(0, output, ''))
    hn = HPUXNetwork(module)
    result = hn.get_default_interfaces()
    assert result == {'default_gateway': '17.251.0.1',
                      'default_interface': 'lan1000'}


# Generated at 2022-06-13 01:40:24.953561
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    """Unit test for method get_interfaces_info of class HPUXNetwork"""

    def run_command_mock(self, command, check_rc=True):
        if command == '/usr/bin/netstat -niw':
            command_output = ("lan0    10.1.1.1     0    24   0   0   0   0   0   0   0   0   0   0   0   0   0\nlan1    10.1.1.2     0    24   0   0   0   0   0   0   0   0   0   0   0   0   0")
            return (0, command_output, '')

# Generated at 2022-06-13 01:40:41.256739
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    net = HPUXNetwork()

    net.module.run_command = MagicMock(return_value=(0, '', ''))
    net.module.get_bin_path = MagicMock(return_value=None)

    result = net.populate()
    assert result == {}

    expected = {
        'default_gateway': '192.168.1.254',
        'default_interface': 'lan0',
        'interfaces': ['lan0'],
        'lan0': {
            'device': 'lan0',
            'ipv4': {
                'address': '192.168.1.2',
                'interface': 'lan0',
                'network': '192.168.1.0'
            }
        }
    }


# Generated at 2022-06-13 01:40:45.019134
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    collector = HPUXNetworkCollector()
    assert collector._fact_class is HPUXNetwork
    assert collector._platform == 'HP-UX'


# Generated at 2022-06-13 01:40:46.764140
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    netMod = Network()
    netMod.get_interfaces_info()



# Generated at 2022-06-13 01:40:51.212346
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    module = MockModule()
    network_facts = HPUXNetwork().populate(module)
    ifaces = network_facts['interfaces']

    assert len(ifaces) == 1
    assert 'lan0' in ifaces
    assert network_facts['default_interface'] == 'lan0'
    assert network_facts['default_gateway'] == '10.5.5.5'

# Generated at 2022-06-13 01:40:53.317333
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    result = HPUXNetworkCollector()
    assert result is not None
    assert result._fact_class == HPUXNetwork
    assert result._platform == 'HP-UX'

# Generated at 2022-06-13 01:40:56.471452
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    network = HPUXNetwork()
    network.module = AnsibleModuleMock()
    network_facts = {'default_interface': 'lan0', 'default_gateway': '172.18.2.254'}
    assert network.get_default_interfaces() == network_facts



# Generated at 2022-06-13 01:41:00.512960
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    net = HPUXNetwork()
    net.module = lambda: None
    net.module.run_command = lambda: (0, '/usr/bin/netstat -nr', '')
    fact = net.get_default_interfaces()

    assert 'default_interface' in fact
    assert 'default_gateway' in fact



# Generated at 2022-06-13 01:41:02.599599
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    collector = HPUXNetworkCollector()
    assert collector.platform == 'HP-UX'
    assert collector._fact_class == HPUXNetwork

# Generated at 2022-06-13 01:41:13.961559
# Unit test for method get_interfaces_info of class HPUXNetwork

# Generated at 2022-06-13 01:41:18.245361
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    network = HPUXNetwork({'module': None})
    test_interfaces = {'lan0': {'device': 'lan0',
                                'ipv4': {'address': '10.0.0.1',
                                         'network': '10.0.0.0',
                                         'interface': 'lan0'}}}
    interfaces = network.get_interfaces_info()
    assert interfaces == test_interfaces


# Generated at 2022-06-13 01:41:37.588885
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    line = 'lan0        19      0       24      0           0     0       ' \
           '    -       0       0 0 0   0   ' \
           '  -       0       0    192.168.0.1        24'
    words = line.split()
    interfaces = {}
    for i in range(len(words) - 1):
        if words[i][:3] == 'lan':
            device = words[i]
            interfaces[device] = {'device': device}
            address = words[i + 3]
            interfaces[device]['ipv4'] = {'address': address}
            network = words[i + 2]
            interfaces[device]['ipv4'] = {'network': network, 'interface': device, 'address': address}

# Generated at 2022-06-13 01:41:44.746070
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    """ Test for method get_interfaces_info of class HPUXNetwork """

# Generated at 2022-06-13 01:41:55.729454
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    """Test class HPUXNetwork."""

    from ansible.module_utils.facts.network.hpux import HPUXNetwork
    from ansible.module_utils.facts.network.hpux import HPUXNetworkCollector

    module = Mock(params={})

    results = HPUXNetworkCollector.collect(module, [])

    assert type(results) == dict
    assert results['default_interface'] == 'lan0'
    assert results['interfaces'] == ['lan0']
    assert results['lan0'] == {'ipv4': {'address': '192.168.122.1', 'network': '192.168.122.0', 'interface': 'lan0'}, 'device': 'lan0'}
    assert results['default_gateway'] == '192.168.122.2'

# Generated at 2022-06-13 01:42:04.650826
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    class F:
        def __init__(self, rc, out, err):
            self.rc = rc
            self.out = out
            self.err = err
        def run_command(self, cmd):
            return (self.rc, self.out, self.err)
    hn = HPUXNetwork()
    hn.module = F(0, 'default 192.168.1.1 UG lan0', '')
    assert hn.get_default_interfaces() == {'default_interface': 'lan0',
                                           'default_gateway': '192.168.1.1'}


# Generated at 2022-06-13 01:42:05.862141
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    net = HPUXNetwork(None)
    assert net


# Generated at 2022-06-13 01:42:14.181901
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    """
    Return the facts for this platform.  This will be called by
    the callback which calls this during __init__.
    """
    class MockModule(object):
        def __init__(self):
            self.params = {}

        def run_command(self, command):
            return 0, None, None

        def get_bin_path(self, app):
            return app

    c = MockModule()
    hpn = HPUXNetwork(c)
    facts = hpn.populate()
    assert 'default_interface' in facts
    assert 'interfaces' in facts

# Generated at 2022-06-13 01:42:15.643067
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    network = HPUXNetworkCollector()
    assert network._platform == 'HP-UX'

# Generated at 2022-06-13 01:42:16.861916
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    hn_collector = HPUXNetworkCollector()
    assert hn_collector

# Generated at 2022-06-13 01:42:20.910105
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    dev = dict(module=dict(run_command=lambda *args, **kwargs:
                           (0, 'netstat output', 'some error')))
    dn = HPUXNetwork(dev)
    interfaces = dn.get_interfaces_info()
    assert 'lan0' in interfaces
    assert interfaces['lan0']['ipv4']['address'] == '192.168.1.10'
    assert interfaces['lan0']['ipv4']['network'] == '192.168.1.0'

# Generated at 2022-06-13 01:42:30.475035
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    import json
    import platform
    import sys
    # Create a HPUXNetwork object as self
    sys_maj_ver = platform.release().split('.')[0]
    sys_maj_ver = int(sys_maj_ver)
    if sys_maj_ver <= 11:
        netstat_path = '/usr/sbin/netstat'
    else:
        netstat_path = '/usr/bin/netstat'
    hpn = HPUXNetwork(None, netstat_path)
    # create result string for the hpn.get_interfaces_info method

# Generated at 2022-06-13 01:43:02.123173
# Unit test for method get_interfaces_info of class HPUXNetwork

# Generated at 2022-06-13 01:43:04.286583
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    collector = HPUXNetworkCollector()
    assert collector.platform == "HP-UX"
    assert collector._fact_class == HPUXNetwork

# Generated at 2022-06-13 01:43:07.701470
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    network_collector = HPUXNetworkCollector()
    assert HPUXNetworkCollector is type(network_collector)
    assert network_collector._platform is 'HP-UX'


# Generated at 2022-06-13 01:43:09.315507
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    net = HPUXNetwork()
    ifaces = net.get_default_interfaces()
    assert ifaces is not None

# Generated at 2022-06-13 01:43:16.368915
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    test_instance_HPUXnetwork = HPUXNetwork()
    test_instance_HPUXnetwork.module = module
    interfaces = {'lan0': {'device': 'lan0',
                           'ipv4': {'address': '10.10.10.10',
                                    'interface': 'lan0',
                                    'network': '10.10.10.0'}},
                  'lan1': {'device': 'lan1',
                           'ipv4': {'address': '10.10.11.10',
                                    'interface': 'lan1',
                                    'network': '10.10.11.0'}}}
    assert interfaces == test_instance_HPUXnetwork.get_interfaces_info()

# Generated at 2022-06-13 01:43:17.807312
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    nc = HPUXNetworkCollector()
    assert nc is not None

# Generated at 2022-06-13 01:43:23.976927
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )
    hpux = HPUXNetwork(module)
    out = str(hpux)
    assert 'HPUXNetwork' in out
    assert 'default_interface=' in out
    assert 'default_gateway=' in out
    assert 'interfaces=' in out
    assert 'lan0' in out



# Generated at 2022-06-13 01:43:24.820515
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    h=HPUXNetwork()


# Generated at 2022-06-13 01:43:29.262733
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    test_class = HPUXNetwork()
    out = 'lan0      UP            UP  10.10.10.10   255.255.255.240'
    interfaces = test_class.get_interfaces_info()
    assert interfaces['lan0']['device'] == 'lan0'
    assert interfaces['lan0']['ipv4']['address'] == '10.10.10.10'

# Generated at 2022-06-13 01:43:34.647004
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    module = AnsibleModule(argument_spec=dict())
    network = HPUXNetwork(module=module)
    all_interfaces = network.get_default_interfaces()
    assert type(all_interfaces) == type({})
    assert all_interfaces['default_interface'] == 'lan0'
    assert all_interfaces['default_gateway'] == '10.10.10.1'


# Generated at 2022-06-13 01:44:41.904127
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    network = HPUXNetwork()
    network.out = '''HP-UX nfsa B.11.31 U ia64      0610664591 unlimited-user license

Kernel 1033.5.0.0 on an ia64
10/31/16 20:55:55

default  192.168.1.254        UG   1   0        - lan0
192.168.1.0       127.0.0.0       255.255.255.0   U     1   0        - loopback
'''
    default_interfaces = network.get_default_interfaces()
    assert default_interfaces['default_interface'] == 'lan0'
    assert default_interfaces['default_gateway'] == '192.168.1.254'


# Generated at 2022-06-13 01:44:50.632414
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    network_collector = HPUXNetworkCollector()
    network_collector.module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )

    hpu_network_obj = HPUXNetwork(network_collector)


# Generated at 2022-06-13 01:44:52.392736
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    """
    Constructor of class HPUXNetworkCollector can be called without
    any error.
    """
    HPUXNetworkCollector()

# Generated at 2022-06-13 01:44:55.388574
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    collected_facts = {}
    p = HPUXNetwork(module=None)

    assert p.platform == 'HP-UX'

    assert p.populate(collected_facts=collected_facts) is not None
    assert 'default_gateway' in collected_facts



# Generated at 2022-06-13 01:45:01.249252
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    net = HPUXNetwork()
    net.module = FakeModule()
    net.get_default_interfaces = mock_get_default_interfaces
    net.get_interfaces_info = mock_get_interfaces_info
    net.netstat_path = "/usr/bin/netstat"
    network_facts = net.populate()
    assert network_facts
    assert network_facts['default_interface'] == "lan0"
    assert network_facts['default_gateway'] == "17.80.40.254"
    assert network_facts['interfaces'] == ['lan0', 'lan1']
    assert network_facts['lan0']['device'] == "lan0"
    assert network_facts['lan0']['ipv4']['network'] == "17.80.36.0"
    assert network

# Generated at 2022-06-13 01:45:07.224995
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    interfaces = HPUXNetwork.get_interfaces_info()

    assert interfaces['lan0'] == {
        'ipv4': {
            'address': '192.168.56.101',
            'network': '192.168.56.0',
            'interface': 'lan0',
        },
        'device': 'lan0',
    }


# Generated at 2022-06-13 01:45:09.731472
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    network_collector = HPUXNetworkCollector()
    assert network_collector._platform == "HP-UX"
    assert network_collector._fact_class == HPUXNetwork

# Generated at 2022-06-13 01:45:12.330722
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    test_network_collector = HPUXNetworkCollector()
    assert test_network_collector._fact_class == HPUXNetwork

# Generated at 2022-06-13 01:45:17.587911
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    test_module = type('test_module', (object,), dict(run_command=test_run_command))
    network = HPUXNetwork(test_module)
    facts = network.get_interfaces_info()
    assert facts['lan0'] == {'ipv4': {'network': '172.16.2.0', 'address': '172.16.2.1', 'interface': 'lan0'}, 'device': 'lan0'}
    assert facts['lan1'] == {'ipv4': {'network': '172.17.2.0', 'address': '172.17.2.1', 'interface': 'lan1'}, 'device': 'lan1'}


# Generated at 2022-06-13 01:45:28.785531
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    """Unit test for get_interfaces_info of class HPUXNetwork."""
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes

    module = basic.AnsibleModule(argument_spec={})
    network_facts_instance = HPUXNetwork(module)

# Generated at 2022-06-13 01:47:29.698812
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    hpux_network = HPUXNetworkCollector()
    assert hpux_network._platform == 'HP-UX'
    assert hpux_network._fact_class == HPUXNetwork


# Generated at 2022-06-13 01:47:32.857866
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    y = HPUXNetworkCollector()
    x = str(y)
    assert x == '<ansible.module_utils.facts.network.hpux.HPUXNetworkCollector object at 0x2b4ee7d35050>'
    assert y._platform == 'HP-UX'
    assert y._fact_class == HPUXNetwork


# Generated at 2022-06-13 01:47:39.189132
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    net = HPUXNetwork()
    net_info = net.get_interfaces_info()
    for iface, info in net_info.items():
        print("interface: %s" % iface)
        print("  device: %s" % info['device'])
        print("  ipv4:")
        print("    interface: %s" % info['ipv4']['interface'])
        print("    address: %s" % info['ipv4']['address'])
        print("    network: %s" % info['ipv4']['network'])
