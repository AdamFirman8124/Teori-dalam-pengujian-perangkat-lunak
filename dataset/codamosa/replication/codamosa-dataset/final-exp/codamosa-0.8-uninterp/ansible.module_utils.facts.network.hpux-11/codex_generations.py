

# Generated at 2022-06-13 01:37:52.789338
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    hn = HPUXNetworkCollector()
    assert hn._platform == 'HP-UX', 'Expected HP-UX, got {}'.\
        format(hn._platform)
    assert isinstance(hn, NetworkCollector), 'Expected instance of NetworkCollector, got {}'.\
        format(type(hn))
    assert isinstance(hn, HPUXNetworkCollector), 'Expected instance of HPUXNetworkCollector, got {}'.\
        format(type(hn))

# Generated at 2022-06-13 01:38:00.658970
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    module = FakeModule()
    net = HPUXNetwork(module)
    out = "default 10.0.0.1 UG 2  lan0"
    net.module.run_command.return_value = (0, out, '')
    default_interfaces_facts = net.get_default_interfaces()
    assert len(default_interfaces_facts) == 2
    assert default_interfaces_facts['default_interface'] == 'lan0'
    assert default_interfaces_facts['default_gateway'] == '10.0.0.1'



# Generated at 2022-06-13 01:38:04.401266
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    h = HPUXNetworkCollector()
    assert(h._fact_class == HPUXNetwork)
    assert(h._platform == 'HP-UX')


# Generated at 2022-06-13 01:38:14.583122
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    mod = AnsibleModule(argument_spec={}, supports_check_mode=False)
    net_collector = HPUXNetworkCollector(module=mod)
    net_obj = HPUXNetwork(module=mod)
    net_collector.populate()
    (rc, out, err) = mod.run_command("/usr/bin/netstat -niw")
    if rc == 0:
        ifaces=[]
        lines = out.splitlines()
        for line in lines:
            words = line.split()
            for i in range(len(words) - 1):
                if words[i][:3] == 'lan':
                    ifaces.append(words[i])
                    break

        # Check default_interface fact

# Generated at 2022-06-13 01:38:19.768480
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():

    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )

    network_collector = HPUXNetworkCollector(module=module)
    network_object = network_collector.get_device()

    assert network_object.platform == 'HP-UX'

# Generated at 2022-06-13 01:38:21.226978
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    net = HPUXNetworkCollector()
    assert net._platform == 'HP-UX'

# Generated at 2022-06-13 01:38:30.132774
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    from ansible.module_utils.facts.network.hpux import HPUXNetwork

    module = FakeModule({'PATH': '/bin:/usr/bin'})
    hp_net = HPUXNetwork(module=module)

    status, out, err = module.run_command.call_args[0]
    assert "/usr/bin/netstat -nr" in status

    status, out, err = module.run_command.call_args[0]
    assert "/usr/bin/netstat -niw" in status

    net_facts = hp_net.populate()
    assert 'default_interface' in net_facts
    assert 'default_gateway' in net_facts
    assert net_facts['default_interface'] == 'lan0'

# Generated at 2022-06-13 01:38:35.983403
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    net = HPUXNetwork()
    out = "default  192.168.100.100  UG  lan1  0 0\n"
    net.module.run_command = lambda x: (0, out, '')
    expected = {'default_interface': 'lan1', 'default_gateway': '192.168.100.100'}
    assert net.get_default_interfaces() == expected


# Generated at 2022-06-13 01:38:45.011426
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    class MockModule:
        def __init__(self):
            self.run_command_called = False
            self.bin_path = {}

        def run_command(self, command):
            self.run_command_called = True
            self.run_command_called_with = command

# Generated at 2022-06-13 01:38:55.605642
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=False)

    obj = HPUXNetwork(module=module)
    rc, out, err = module.run_command("/usr/bin/netstat -nr")
    assert out == ""

    rc, out, err = module.run_command("/usr/bin/netstat -niw")
    assert out == ""

    network_facts = obj.populate()

# Generated at 2022-06-13 01:39:04.451200
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    module = AnsibleModule(
        argument_spec=dict(gather_subset=dict(default=['!all'], type='list')))
    hpux_network = HPUXNetwork(module)
    assert hpux_network.platform == 'HP-UX'

# Generated at 2022-06-13 01:39:07.398741
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    hpux_network = HPUXNetwork()
    assert hpux_network.platform == 'HP-UX'
    assert hpux_network.module is None



# Generated at 2022-06-13 01:39:18.409316
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    """
    This tests the method get_interfaces_info of class HPUXNetwork.
    """
    class FakeAnsibleModule(object):

        class FakeResult(object):
            stdout_lines = []
            rc = 0

        def __init__(self):
            self.params = {}
            self.run_command_return_value = FakeResult()

        def run_command(self, args, check_rc=False):
            return self.run_command_return_value

    fake_ansible = FakeAnsibleModule()


# Generated at 2022-06-13 01:39:26.274040
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    import os.path
    from ansible.module_utils.facts.network.hpux import HPUXNetwork
    from ansible.module_utils.facts.network.base import NetworkModule
    from ansible.module_utils._text import to_bytes

    # Test data
    netstat_path = '/usr/bin/netstat'
    netstat_out = b"""
      Routing tables
Destination           Gateway           Flags          Refs  Use If Exp
default              10.25.33.254      UG           18257    0  lan0
10.25.33.0            10.25.33.117      UH         3288592    0  lan0
"""
    default_interface_out = b"default          10.25.33.0            10.25.33.117      UH         3288592    0  lan0"



# Generated at 2022-06-13 01:39:33.391807
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    module = AnsibleModule(argument_spec={})
    network_facts = {
        'default_interface': 'lan0',
        'default_gateway': '10.0.0.1',
        'interfaces': ['lan0'],
        'lan0': {
            'ipv4': {
                'address': '10.0.0.3',
                'network': '10.0.0.0',
                'interface': 'lan0',
                'broadcast': '10.0.0.255'
            }
        }
    }
    HPUXNetworkFacts = HPUXNetwork(module)
    HPUXNetworkFacts.collect = Mock(return_value=(None, None, None))

# Generated at 2022-06-13 01:39:35.137827
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    nw_collector = HPUXNetworkCollector()
    assert nw_collector._fact_class == HPUXNetwork
    assert nw_collector._platform == 'HP-UX'

# Generated at 2022-06-13 01:39:41.551792
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    class ModuleMock(object):
        def __init__(self):
            self.run_command_value = (0, "lan0 192.168.0.0 192.168.0.1", '')

        def run_command(self, cmd):
            return self.run_command_value

    import sys
    import os
    sys.path.append(os.path.dirname(os.path.dirname(__file__)))
    from facts.network.hpux import HPUXNetwork
    module_mock = ModuleMock()
    net_obj = HPUXNetwork(module_mock)

    interfaces = net_obj.get_interfaces_info()


# Generated at 2022-06-13 01:39:42.922281
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    hpux_network_collector_facts = HPUXNetworkCollector()
    hpux_network_collector_facts

# Generated at 2022-06-13 01:39:52.626390
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    module = AnsibleModule(
        argument_spec=dict(gather_subset=dict(default=['!all'], type='list'))
    )
    network_facts = HPUXNetwork(module=module).populate()
    assert network_facts['default_interface'] == 'lan0'
    assert network_facts['default_gateway'] == '192.168.100.1'

    assert 'interfaces' in network_facts
    assert 'lan0' in network_facts['interfaces']
    assert 'lan1' in network_facts['interfaces']

    assert 'ipv4' in network_facts['lan0']
    assert network_facts['lan0']['ipv4']['address'] == '192.168.100.221'

# Generated at 2022-06-13 01:39:56.780225
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    hpx_network = HPUXNetwork()
    assert hpx_network.platform == "HP-UX"
    assert hpx_network.get_default_interfaces() == {}
    assert hpx_network.get_interfaces_info() == {}


# Generated at 2022-06-13 01:40:14.667536
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    """
    Unit test for method HPUXNetwork.get_default_interfaces
    """
    # pylint: disable=too-many-arguments,too-many-locals
    class Module:
        def __init__(self):
            self.run_command_counter = 0
            self.run_command_return_values = [
                (0,
                 '  Destination Gateway   Interface  State     Metric    Ref  Use  Iflags\n'
                 '  ---------- -------   ---------  -------  --------  ----  ---  ------',
                 ''),
                (0, 'default   192.168.1.1  lan0      UG        0         0     0', '')]

        def get_bin_path(self, name, opts=None, required=False):
            return '/usr/bin/netstat'



# Generated at 2022-06-13 01:40:17.781608
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    hpux_network = HPUXNetwork(dict())
    if hpux_network is not None:
        assert hpux_network.interfaces == []
        assert hpux_network.default_interface is None


if __name__ == '__main__':
    test_HPUXNetwork()

# Generated at 2022-06-13 01:40:19.708521
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    HPUXNetworkCollector.test_populate(HPUXNetwork)



# Generated at 2022-06-13 01:40:23.077479
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    h = HPUXNetworkCollector()
    assert h.platform == 'HP-UX'
    assert h._fact_class == HPUXNetwork


# Generated at 2022-06-13 01:40:24.049559
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    assert False, "Test not implemented"

# Generated at 2022-06-13 01:40:34.406430
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    module = NetworkCollector()
    network = HPUXNetwork()
    # Mock the method get_default_interface so that we
    # can call populate to get the interface and gateway
    def mocked_get_default_interfaces(x):
        return {'default_interface': 'lan0', 'default_gateway': '192.168.1.1'}
    network.get_default_interfaces = mocked_get_default_interfaces
    # Mock the method get_interfaces_info so that we
    # can call populate to get the interface and ipv4 info

# Generated at 2022-06-13 01:40:36.942679
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    """
    Create a new instance of HPUXNetworkCollector
    """
    result = HPUXNetworkCollector()
    assert result.platform == 'HP-UX'

# Generated at 2022-06-13 01:40:42.658215
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    class MockModule:
        def run_command(self, cmd):
            return (0, """
Routing tables

 Destination           Gateway           Flags Refs Use If
 127.0.0.1             127.0.0.1         UH    6    0 lo0
            """, '')

    assert HPUXNetwork(MockModule()).get_default_interfaces() == {
        'default_interface': 'lo0',
        'default_gateway': '127.0.0.1'}


# Generated at 2022-06-13 01:40:45.538288
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    network_facts = HPUXNetwork()
    assert isinstance(network_facts, HPUXNetwork)


# Generated at 2022-06-13 01:40:54.181429
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    class FakeModule:
        def run_command(self, cmd):
            output = 'lan0      Link encap:Ethernet  HWaddr 00:E0:29:C5:89:52\n'
            output += '          inet addr:10.130.72.117  Bcast:10.130.75.255  Mask:255.255.252.0\n'
            output += '          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1\n'
            output += '          lan0:0: flags=\n'

            return 0, output, ''

    fake_module = FakeModule()
    hpos_network = HPUXNetwork()
    hpos_network.module = fake_module
    interfaces = hpos_network.get_interfaces_info()


# Generated at 2022-06-13 01:41:21.276556
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    # Make a test HPUXNetwork instance
    hpxnet = HPUXNetwork()

    # Expected output

# Generated at 2022-06-13 01:41:31.501587
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    """Unit test for method populuate of class HPUXNetwork."""
    hpuxtest = HPUXNetwork()
    rc, out, err = hpuxtest.module.run_command("/usr/bin/netstat -nr")
    rc1, out1, err1 = hpuxtest.module.run_command("/usr/bin/netstat -niw")
    assert out == 'default         10.0.0.1          UG        0   0        0 lan0\n' or \
           out == 'default         10.0.0.1 UG        0   0        0 lan0\n'
    assert rc == 0
    assert err == ''
    assert rc1 == 0
    assert err1 == ''
    network_facts = hpuxtest.populate()

# Generated at 2022-06-13 01:41:32.822834
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    h = HPUXNetwork(dict())
    assert h.platform == 'HP-UX'



# Generated at 2022-06-13 01:41:37.766161
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    from ansible.module_utils.facts.network.hpux import HPUXNetwork
    hpux_network = HPUXNetwork()
    interfaces = hpux_network.get_interfaces_info()
    for key in interfaces:
        for item in interfaces[key].keys():
            print(item+":", interfaces[key][item])

# Test the function get_default_interfaces of HPUXNetwork

# Generated at 2022-06-13 01:41:40.705477
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    module = FakeModule()
    network = HPUXNetwork(module)
    assert isinstance(network, HPUXNetwork)


# Generated at 2022-06-13 01:41:47.629300
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    interfaces = {'lan1': {'device': 'lan1',
                           'ipv4': {'interface': 'lan1',
                                    'address': '172.31.128.1',
                                    'network': '172.31.128.0'}},
                  'lan2': {'device': 'lan2',
                           'ipv4': {'interface': 'lan2',
                                    'address': '10.48.128.1',
                                    'network': '10.48.128.0'}},
                  'lan3': {'device': 'lan3',
                           'ipv4': {'interface': 'lan3',
                                    'address': '20.128.1',
                                    'network': '20.128.0'}}}

    hp_network = HPUXNetwork()
    hp_network

# Generated at 2022-06-13 01:41:57.775215
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    from ansible.module_utils.facts.network.hpsux import HPUXNetwork
    hpxnet = HPUXNetwork(None)

    netstat_output = '  Name  Mtu  Network     Address            Ipkts Ierrs     Opkts Oerrs  Coll    lan0  1492  172.16.125.0  172.16.125.178      5174     0      879     0     0\r\n'
    testvalue = hpxnet.get_interfaces_info(netstat_output=netstat_output)
    assert testvalue['lan0']['ipv4']['address'] == '172.16.125.178'
    assert testvalue['lan0']['ipv4']['network'] == '172.16.125.0'

# Generated at 2022-06-13 01:42:02.033234
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    """
    This is a test for the constructor of the class HPUXNetworkCollector
    """
    test_obj = HPUXNetworkCollector()
    assert test_obj
    assert isinstance(test_obj, HPUXNetworkCollector)

# Generated at 2022-06-13 01:42:09.663967
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    monkeypatch.setattr(HPUXNetwork, 'get_default_interfaces', lambda x: {'default_interface': 'lan1',
                                                                          'default_gateway': '192.168.0.1'})
    monkeypatch.setattr(HPUXNetwork, 'get_interfaces_info', lambda x: {'lan1': {'ipv4': {'address': '192.168.0.2'}}})

    result = HPUXNetwork().populate()
    assert result == {'default_interface': 'lan1',
                      'default_gateway': '192.168.0.1',
                      'interfaces': ['lan1'],
                      'lan1': {'ipv4': {'address': '192.168.0.2'}}}


# Generated at 2022-06-13 01:42:12.877050
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    collector = HPUXNetworkCollector()
    assert collector.fact_class is HPUXNetwork
    assert collector.platform == 'HP-UX'


# Generated at 2022-06-13 01:42:56.174270
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    class MockModule(object):
        def run_command(self, command):
            out = ("lan0    link#1   UP        1000   0x80e2ec00  0x80e2ec00     " +
                   "127.0.0.0      127.0.0.2      lan9000  lan9001")
            return 0, out, ""

        def get_bin_path(self, executable):
            return "/usr/bin/netstat"

    hpux_network = HPUXNetwork(MockModule())
    interfaces = hpux_network.get_interfaces_info()
    assert interfaces['lan0']['ipv4']['address'] == '127.0.0.2'
    assert interfaces['lan0']['ipv4']['network'] == '127.0.0.0'

# Generated at 2022-06-13 01:43:02.157555
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    from ansible.module_utils.facts.network.hpu_ux import HPUXNetwork
    net = HPUXNetwork()
    net.module = AnsibleModuleMock()
    assert net.get_interfaces_info() == {'lan0': {'device': 'lan0', 'ipv4': {'address': '10.1.1.2', 'network': '10.1.1.0', 'interface': 'lan0'}}}



# Generated at 2022-06-13 01:43:07.456283
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    module = FakeAnsibleModule()
    network = HPUXNetwork(module)
    collected_facts = {}
    network_facts = network.populate(collected_facts)
    assert 'interfaces' in network_facts
    assert 'default_interface' in network_facts
    assert 'default_gateway' in network_facts
    assert len(network_facts['interfaces']) > 0

# Generated at 2022-06-13 01:43:15.540130
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    module = AnsibleModule(argument_spec={})
    network = HPUXNetwork(module)
    ansible_facts = {'ansible_net_interfaces': ['lan0', 'lan1', 'lan2']}
    module.run_command = MagicMock(return_value=(0, '''default 164.99.135.254 UGS 0 2 lan2
lan0 164.99.135.242 UH 0 50 lan0
localnet link#3 UC 0 0 localnet
lan1 164.99.135.243 UH 0 18 lan1
localnet unspec 0 0 localnet
localnet unspec 0 0 localnet
localnet unspec 0 0 localnet
localnet unspec 0 0 localnet
default link#4 UC 0 0 lan2''', ''))
    network_facts = network.populate(ansible_facts)

# Generated at 2022-06-13 01:43:18.542350
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    hn = HPUXNetworkCollector()
    assert hn._fact_class is HPUXNetwork
    assert hn._platform is 'HP-UX'

# Generated at 2022-06-13 01:43:23.418516
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    module = AnsibleModule(argument_spec={})
    hn = HPUXNetwork(module)
    assert hn.platform == 'HP-UX'

    default_interfaces = hn.get_default_interfaces()
    assert 'default_interface' in default_interfaces
    assert 'default_gateway' in default_interfaces

    interfaces = hn.get_interfaces_info()
    assert interfaces
    assert 'lo0' in interfaces
    assert 'ipv4' in interfaces['lo0']
    assert 'network' in interfaces['lo0']['ipv4']
    assert 'address' in interfaces['lo0']['ipv4']
    network_facts = hn.populate()
    assert 'interfaces' in network_facts
    assert network_facts['interfaces']

# Generated at 2022-06-13 01:43:26.916155
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    module = AnsibleModule(
        argument_spec=dict(gather_subset=dict(default=['all'], type='list')))
    network_obj = HPUXNetwork()
    network_obj.module = module
    network_obj.populate()



# Generated at 2022-06-13 01:43:33.071478
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    class Module(object):
        @staticmethod
        def run_command(cmd):
            out = ("Routing tables\n"
                   "Destination        Gateway          Flag    Refs     Interface\n"
                   "default            10.2.2.2         UG       11        lan0\n"
                   "10.1.1.0           10.1.1.1         UH       1         lan1\n")
            err = ""
            return 0, out, err
    module = Module()
    hpux = HPUXNetwork(module)
    default_interfaces = hpux.get_default_interfaces()
    assert default_interfaces == {'default_interface': 'lan0',
                                  'default_gateway': '10.2.2.2'}


# Generated at 2022-06-13 01:43:39.041297
# Unit test for method get_default_interfaces of class HPUXNetwork

# Generated at 2022-06-13 01:43:43.807235
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    facts_network = {'default_interface': 'lan0',
                     'default_gateway': '10.0.2.2'}
    network = HPUXNetwork(dict(module=None))
    network.populate()
    assert network.facts == facts_network



# Generated at 2022-06-13 01:45:34.043980
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    o = HPUXNetwork()
    o.module = MockModule()
    o.module.run_command = Mock(return_value=(0, c, ''))

    assert o.get_interfaces_info() == {'lan0': {'device': 'lan0',
                                               'ipv4': {'network': '192.168.0.0',
                                                        'address': '192.168.0.1',
                                                        'interface': 'lan0'}}}


# Generated at 2022-06-13 01:45:35.466707
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    net_info = HPUXNetwork()
    assert net_info.platform == 'HP-UX'


# Generated at 2022-06-13 01:45:36.346375
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    obj = HPUXNetworkCollector()
    assert obj is not None


# Generated at 2022-06-13 01:45:46.409079
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    hw = HPUXNetwork()
    hw.populate()
    assert hw.default_interface == 'lan0', 'default_interface is not lan0'
    assert hw.default_gateway == '192.168.0.1', 'default_gateway is not 192.168.0.1'
    assert 'lan0' in hw.interfaces, 'lan0 not found in interface list'
    assert hw.lan0['ipv4']['network'] == '192.168.0.0', 'network is not 192.168.0.0'
    assert hw.lan0['ipv4']['address'] == '192.168.0.2', 'address is not 192.168.0.2'

# Generated at 2022-06-13 01:45:53.325701
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    interfaces = {}
    network = HPUXNetwork()
    interfaces = network.get_interfaces_info()
    for device in interfaces:
        for key in interfaces[device]:
            assert(key == 'ipv4' or key == 'device')
            if key == 'ipv4':
                for val in interfaces[device][key]:
                    assert(val == 'network' or val == 'interface'
                            or val == 'address')
                    if val == 'network' or val == 'interface' or val == 'address':
                        assert(interfaces[device][key][val] != '')
            if key == 'device':
                assert(interfaces[device][key] == device)

# Generated at 2022-06-13 01:45:59.083194
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    """Test method get_interfaces_info of class HPUXNetwork"""

# Generated at 2022-06-13 01:46:04.967118
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    hpux_network = HPUXNetwork(None)
    hpux_network.module.run_command = mock_run_command
    interfaces = hpux_network.get_default_interfaces()
    assert 'default_interface' in interfaces
    assert 'default_gateway' in interfaces
    assert interfaces['default_interface'] == 'lan1'
    assert interfaces['default_gateway'] == '10.10.10.1'


# Generated at 2022-06-13 01:46:05.465455
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    pass

# Generated at 2022-06-13 01:46:07.827087
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    assert HPUXNetworkCollector.fact_class is HPUXNetwork
    assert HPUXNetworkCollector.platform == 'HP-UX'


# Generated at 2022-06-13 01:46:11.844325
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    net_collector = HPUXNetworkCollector()
    assert net_collector.__class__.__name__ == 'HPUXNetworkCollector'
    assert net_collector._platform == 'HP-UX'
    assert net_collector._fact_class == 'HPUXNetwork'
