

# Generated at 2022-06-13 01:37:54.592558
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    module = MagicMock()
    module.run_command.return_value = (0, "default 192.168.1.1 UG lan0", "")
    network = HPUXNetwork(module)
    assert network.get_default_interfaces() == {'default_interface': 'lan0', 'default_gateway': '192.168.1.1'}
    module.run_command.assert_called_once_with("/usr/bin/netstat -nr")
    module.run_command.reset_mock()
    module.run_command.return_value = (0, "default 192.168.1.1 UG lan0\ndefault 192.168.1.1 UG lan1", "")

# Generated at 2022-06-13 01:37:55.956154
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    '''
    dummy test
    '''
    assert True

# Generated at 2022-06-13 01:37:59.883903
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    # Test the constructor and verify that it sets the '_fact_class'
    # and the '_platform' properties correctly.
    network_collector = HPUXNetworkCollector()

    assert network_collector._fact_class is HPUXNetwork
    assert network_collector._platform is 'HP-UX'

# Generated at 2022-06-13 01:38:06.213040
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    class TestHPUXNetwork(HPUXNetwork):
        def __init__(self):
            self.module = None
            self.netstat_path = '/usr/bin/netstat'
    network_collector = HPUXNetwork(module=None)
    default_interfaces_facts = network_collector.get_default_interfaces()
    assert default_interfaces_facts['default_interface'] == 'lan0'
    assert default_interfaces_facts['default_gateway'] == '10.0.0.1'


# Generated at 2022-06-13 01:38:10.332665
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    network = HPUXNetwork()
    network_facts = network.populate()
    assert network_facts['default_interface'] == "lan2"
    assert network_facts['lan127']['ipv4']['address'] == "127.0.0.1"

# Generated at 2022-06-13 01:38:15.797082
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    from ansible.module_utils.facts.network.hpux import HPUXNetwork
    from ansible.module_utils.facts.network.base import Network
    from ansible.module_utils.facts.network.base import NetworkCollector

    network = HPUXNetwork()
    interfaces = network.get_interfaces_info('')

    assert isinstance(interfaces, dict)

    for iface in interfaces:
        assert isinstance(iface, str)
        assert isinstance(interfaces[iface], dict)
        assert isinstance(interfaces[iface]['device'], str)
        assert isinstance(interfaces[iface]['ipv4'], dict)
        assert isinstance(interfaces[iface]['ipv4']['address'], str)

# Generated at 2022-06-13 01:38:25.511184
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    module = AnsibleModule(
        argument_spec=dict()
    )
    network_module = HPUXNetwork(module)
    out = network_module._get_default_interfaces_from_file('/dev/null')
    assert out == {}

    out = network_module._get_default_interfaces_from_file('/tmp/netstat_out2')
    assert out == dict(default_interface='lan0', default_gateway='10.1.1.1')

    out = network_module._get_default_interfaces_from_file('/tmp/netstat_out3')
    assert out == dict(default_interface='lan2', default_gateway='11.1.1.1')



# Generated at 2022-06-13 01:38:32.158083
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    class TestModule():
        def __init__(self):
            self.run_command_called = False

        def run_command(self, cmd):
            self.run_command_called = True
            return (0, "lan0  0    4920   0   0  0  6  0  0  0", "")

    module = TestModule()

    hpuxNetwork = HPUXNetwork(module)
    interfaces = hpuxNetwork.get_interfaces_info()
    assert module.run_command_called
    assert interfaces['lan0']['device'] == 'lan0'
    assert interfaces['lan0']['ipv4']['address'] == '0'

# Generated at 2022-06-13 01:38:37.469924
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    rhn = HPUXNetwork()
    interfaces = rhn.get_interfaces_info()
    assert isinstance(interfaces, dict)
    assert isinstance(interfaces['lan0'], dict)
    assert isinstance(interfaces['lan0']['ipv4'], dict)
    assert isinstance(interfaces['lan0']['ipv4']['address'], unicode)
    assert '0.0.0.0' not in interfaces['lan0']['ipv4']['address']
    assert isinstance(interfaces['lan0']['ipv4']['network'], unicode)
    assert '0.0.0.0' not in interfaces['lan0']['ipv4']['network']

# Generated at 2022-06-13 01:38:48.575725
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    network = HPUXNetwork({'module': ''})

    network.get_default_interfaces = lambda: {'default_interface': "lan0",
                                              'default_gateway': "10.100.100.100"}

    network.get_interfaces_info = lambda: {'lan0': {'device': 'lan0',
                                                    'ipv4': {'address': '10.100.100.50',
                                                             'network': '10.100.100.0'}},
                                           'lan1': {'device': 'lan1',
                                                    'ipv4': {'address': '10.100.100.100',
                                                             'network': '10.100.100.0'}}}

    network_facts = network.populate()

# Generated at 2022-06-13 01:38:57.644979
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    hpuxtest = HPUXNetwork()
    out_list = ['default 172.17.16.252 UGS 0 0 lan1',
                'default 172.17.16.222 UGS 0 0 lan2']
    out = '\n'.join(out_list)
    hpuxtest.module.run_command = lambda x: (0, out, '')
    assert hpuxtest.get_default_interfaces() == {'default_gateway': '172.17.16.252', 'default_interface': 'lan1'}



# Generated at 2022-06-13 01:38:59.776737
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    hpux_network = HPUXNetwork({})
    assert hpux_network is not None

# Generated at 2022-06-13 01:39:04.179407
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    """
    Test method get_default_interfaces of class HPUXNetwork
    """
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )
    hpn = HPUXNetwork(module=module)

    return hpn.get_default_interfaces()

# Generated at 2022-06-13 01:39:14.530413
# Unit test for method get_interfaces_info of class HPUXNetwork

# Generated at 2022-06-13 01:39:15.589656
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    HPUXNetwork()

# Generated at 2022-06-13 01:39:16.531898
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    pass



# Generated at 2022-06-13 01:39:20.329780
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    '''
    Test HPUX constructor
    '''

    assert 'HP-UX' in HPUXNetworkCollector._platform
    assert HPUXNetworkCollector._fact_class == HPUXNetwork

# Generated at 2022-06-13 01:39:22.419298
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    hpux_network_collector = HPUXNetworkCollector()
    assert type(hpux_network_collector) == HPUXNetworkCollector

# Generated at 2022-06-13 01:39:23.486493
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    col = HPUXNetworkCollector()
    assert col is not None

# Generated at 2022-06-13 01:39:25.248400
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    network_collector = HPUXNetworkCollector()
    platform_name = network_collector.platform
    assert platform_name == 'HP-UX'


# Generated at 2022-06-13 01:39:35.397432
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    from ansible.module_utils.facts.network.hpux import HPUXNetwork
    network = HPUXNetwork()
    interfaces = network.get_interfaces_info()
    assert(len(interfaces) > 0)
    assert('lan0' in interfaces)
    assert(interfaces['lan0']['ipv4']['address'].split('.')[0] == '172')
    assert(interfaces['lan0']['ipv4']['network'].split('.')[0] == '172')
    assert(interfaces['lan0']['device'] == 'lan0')



# Generated at 2022-06-13 01:39:36.697653
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    obj = HPUXNetworkCollector()
    assert obj._fact_class == HPUXNetwork

# Generated at 2022-06-13 01:39:45.107622
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    from ansible.module_utils.facts.network.hpux.netstat import HPUXNetwork
    network = HPUXNetwork()
    interfaces = network.get_interfaces_info()
    assert interfaces['lan1'] == {'device': 'lan1',
                              'ipv4': {'address': '172.16.0.10',
                                       'network': '172.16.0.0',
                                       'interface': 'lan1',
                                       'address': '172.16.0.10'}}

# Generated at 2022-06-13 01:39:48.521124
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    hpn = HPUXNetworkCollector()
    assert hpn.platform == 'HP-UX'
    assert hpn.fact_class == HPUXNetwork

# Generated at 2022-06-13 01:39:58.134814
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )

    network_facts = HPUXNetwork(module)
    network_facts.populate()
    facts = network_facts.get_facts()

    assert facts['default_interface'] == 'lan4'
    assert facts['default_gateway'] == '172.19.103.254'
    assert facts['interfaces'] == ['lan4']
    assert facts['lan4']['device'] == 'lan4'
    assert facts['lan4']['ipv4']['address'] == '172.19.103.111'
    assert facts['lan4']['ipv4']['network'] == '172.19.103.0'

from ansible.module_utils.basic import *  # noqa:

# Generated at 2022-06-13 01:40:00.162733
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    network = HPUXNetwork({})
    assert network
    assert network.platform == 'HP-UX'


# Generated at 2022-06-13 01:40:09.504203
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    network = HPUXNetwork()
    rc, out, err = network.module.run_command("/usr/bin/netstat -niw")
    interfaces = network.get_interfaces_info()
    assert 'lan4' in interfaces
    assert 'lan4' in interfaces
    assert 'lan4' in interfaces
    assert 'lan4' in interfaces
    assert interfaces['lan4']['ipv4']['network'] == '192.168.1.0'
    assert interfaces['lan4']['ipv4']['address'] == '192.168.1.101'
    assert interfaces['lan4']['device'] == 'lan4'


# Generated at 2022-06-13 01:40:14.261756
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    obj = HPUXNetwork()
    obj.get_default_interfaces = lambda: {'default_interface': 'lan1',
                                          'default_gateway': '10.10.10.1'}
    obj.get_interfaces_info = lambda: {'lan0': {'device': 'lan0',
                                                 'ipv4': {'address': '10.10.10.10',
                                                          'network': '10.10.10.0',
                                                          'interface': 'lan0',
                                                          'address': '10.10.10.10'}}}
    returned_facts = obj.populate()

# Generated at 2022-06-13 01:40:21.519992
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():

    from ansible.module_utils.facts.network.hpux import HPUXNetwork
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.six.moves import builtins

    out = '''Kernel IP routing table
Destination         Gateway         Flags        Refs Use Netif Expire
default            10.7.245.1      UG         0   127 lan2
10/8                link#6         U          0   519 lan2
10.7.245          link#7          UHS         0     0 lan2
10.7.245.0        10.7.245.240    UGS         0     0 lan2
10.7.245.240      link#7          UH         28    51 lan2
'''


# Generated at 2022-06-13 01:40:22.695598
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    assert HPUXNetwork(dict())

# Generated at 2022-06-13 01:40:42.659122
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    module = AnsibleModule(argument_spec={})
    network = HPUXNetwork(module=module)

    # netstat is in PATH
    netstat_path = '/usr/bin/netstat'
    try:
        os.symlink('/bin/true', '/usr/bin/netstat')
        network_facts = network.populate()
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    finally:
        os.unlink(netstat_path)

    assert 'ipv4' in network_facts, "ipv4 not in network_facts"
    assert 'address' in network_facts['ipv4'], \
           "address not in network_facts['ipv4']"

# Generated at 2022-06-13 01:40:52.849098
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    module = AnsibleModule(argument_spec={}, supports_check_mode=True)
    module.run_command = MagicMock(return_value=(0, '', ''))
    module.get_bin_path = MagicMock(return_value='/usr/bin/netstat')
    collected_facts = {}
    net = HPUXNetwork(module)
    interface_facts = net.populate(collected_facts)
    assert interface_facts['interfaces'] == ['lan0', 'lan1000', 'en0']
    assert interface_facts['en0']['ipv4']['address'] == '192.168.0.15'
    assert interface_facts['en0']['ipv4']['network'] == '192.168.0.0'
    assert interface_facts['en0']['device']

# Generated at 2022-06-13 01:40:59.969652
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    from ansible.module_utils.facts.network.hpuxtestdata import HPUX_NETSTAT_NIW_OUTPUT
    interfaces = {}
    hpuxtest = HPUXNetwork()
    lines = HPUX_NETSTAT_NIW_OUTPUT.splitlines()
    for line in lines:
        words = line.split()
        for i in range(len(words) - 1):
            if words[i][:3] == 'lan':
                device = words[i]
                interfaces[device] = {'device': device}
                address = words[i + 3]
                interfaces[device]['ipv4'] = {'address': address}
                network = words[i + 2]

# Generated at 2022-06-13 01:41:05.023800
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    from ansible.module_utils.facts.network.hpux import HPUXNetwork

    default_interfaces = \
        HPUXNetwork._get_default_interfaces(HPUXNetwork, "default lan1\n")

    assert default_interfaces == {'default_gateway': 'lan1',
                                  'default_interface': 'lan1'}

# Generated at 2022-06-13 01:41:08.921751
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    assert HPUXNetwork._platform == 'HP-UX'
    assert HPUXNetwork.platform == 'HP-UX'
    assert HPUXNetwork.default_interfaces == []
    assert HPUXNetwork.interfaces == []
    assert HPUXNetwork.network_count == 1


# Generated at 2022-06-13 01:41:12.554724
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    from ansible.module_utils.facts import FactCollector
    from ansible.module_utils.facts.network import NetworkCollector
    from ansible.module_utils.facts.network.hpux import HPUXNetworkCollector

    facts = FactCollector()
    network_collector = NetworkCollector()
    network_collector.populate(facts)

    assert 'network' in facts.data
    assert 'interfaces' in facts.data['network']

    hpux_network_collector = HPUXNetworkCollector()
    hpux_network_collector.populate(facts)

    assert 'default_interface' in facts.data['network']
    assert facts.data['network']['default_interface'] == 'lan0'

    assert 'default_gateway' in facts.data['network']

# Generated at 2022-06-13 01:41:21.266928
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    """
    Unit test for method populate of class HPUXNetwork.

    There is enough information to get all facts requested by this module.
    """
    # pylint: disable=import-error
    from ansible.module_utils.facts.network.hpuxtools import HPUXNetwork
    from ansible.module_utils.facts import BaseFactsCollection

    class MockModule(object):
        """Mock class for ansible module."""
        def __init__(self):
            self.params = {}

        # pylint: disable=unused-argument

# Generated at 2022-06-13 01:41:22.221680
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    assert HPUXNetwork


# Generated at 2022-06-13 01:41:24.565627
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    module = AnsibleModuleMock()
    network = HPUXNetwork(module)
    network.get_interfaces_info()



# Generated at 2022-06-13 01:41:27.368165
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    net = HPUXNetwork()
    assert (net.get_default_interfaces() ==
            {"default_interface": "lan0", "default_gateway": "192.168.10.1"})



# Generated at 2022-06-13 01:41:51.307511
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    module = FakeAnsibleModule()
    net_collector = HPUXNetworkCollector(module=module)
    network_facts = net_collector.collect()['ansible_network_resources']
    assert network_facts['default_interface'] == 'lan1'


# Generated at 2022-06-13 01:42:01.945276
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    module = AnsibleModule(argument_spec={})
    network = HPUXNetwork(module)

    # To test the autodetection of default gateway, a default route
    # must be configured in the test environment.
    network_facts = network.populate()

    # FIXME: This test relies on the presence of an interface with
    # device name 'lan0' in the test environment.
    assert 'lan0' in network_facts['interfaces']
    assert 'lan0' == network_facts['default_interface']
    assert '10.0.2.2' == network_facts['lan0']['ipv4']['network']
    assert '10.0.2.15' == network_facts['lan0']['ipv4']['address']

# Generated at 2022-06-13 01:42:05.488989
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    module = FakeModule()
    interfaces = HPUXNetwork(module)
    result = interfaces.get_default_interfaces()
    assert result['default_interface'] == 'lo0'
    assert result['default_gateway'] == '127.0.0.1'



# Generated at 2022-06-13 01:42:14.013590
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    facts = dict()
    module = MockResourceModule(facts)
    network = HPUXNetwork(module)
    default_interfaces = network.get_default_interfaces()
    interfaces = network.get_interfaces_info()
    network_facts = network.populate()
    assert len(network_facts) == 3
    assert network_facts['default_interface'] == default_interfaces['default_interface']
    assert network_facts['default_gateway'] == default_interfaces['default_gateway']
    assert network_facts['interfaces'] == interfaces.keys()



# Generated at 2022-06-13 01:42:15.825191
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    interfaces = HPUXNetwork().get_interfaces_info()
    assert isinstance(interfaces, dict)

# Generated at 2022-06-13 01:42:20.002328
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    net = HPUXNetwork(None)
    net.module.run_command = test_HPUXNetwork_run_command
    facts = net.get_default_interfaces()
    assert facts['default_interface'] == "lan0"
    assert facts['default_gateway'] == "172.16.0.1"



# Generated at 2022-06-13 01:42:29.829910
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    """
    Unit tests for ansible.module_utils.facts.network.hpux.HPUXNetwork.get_default_interface
    """
    from ansible.module_utils.facts.network.hpux import HPUXNetwork
    from ansible.module_utils._text import to_text


# Generated at 2022-06-13 01:42:37.295276
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    testModule = Network()
    testModule.module.params['gather_subset'] = ['!all', 'network']
    hpux_net = HPUXNetwork(testModule)
    result = hpux_net.get_default_interfaces()
    assert (result['default_interface'] == 'lan0')
    assert (result['default_gateway'] == '188.99.243.1')


# Generated at 2022-06-13 01:42:39.035331
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    interfaces = HPUXNetwork().get_interfaces_info()
    assert len(interfaces.keys()) >= 1


# Generated at 2022-06-13 01:42:42.830770
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    assert HPUXNetworkCollector._platform == 'HP-UX'
    assert HPUXNetworkCollector._fact_class == HPUXNetwork


# Generated at 2022-06-13 01:43:25.430475
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    module = 'ansible'
    hpux_network = HPUXNetwork(module)
    assert hpux_network.module == module
    assert hpux_network.platform == 'HP-UX'

# Generated at 2022-06-13 01:43:27.667579
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    module = AnsibleModule(
        argument_spec=dict()
    )

    hpuxnetwork = HPUXNetwork(module)
    assert hpuxnetwork.platform == 'HP-UX'

# Generated at 2022-06-13 01:43:29.121436
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    obj = HPUXNetwork()
    assert obj


# Generated at 2022-06-13 01:43:32.163880
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    hpuxnetwork = HPUXNetworkCollector()
    assert hpuxnetwork.platform == 'HP-UX'
    assert hpuxnetwork._fact_class == HPUXNetwork


# Generated at 2022-06-13 01:43:34.053814
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    collect_network_data = HPUXNetworkCollector()
    assert collect_network_data._platform == 'HP-UX'


# Generated at 2022-06-13 01:43:35.875273
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    """
    Constructor of class HPUXNetwork
    """
    hw = HPUXNetwork()
    assert hw.platform == 'HP-UX'



# Generated at 2022-06-13 01:43:47.764984
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    from ansible.module_utils.facts.network.hpux import HPUXNetwork
    from ansible.module_utils.six import StringIO

    class TestModule(object):
        def __init__(self):
            self.params = {}
            self.run_command_calls = []
            self.STDERR_ARG = 2

        def get_bin_path(self, arg, opt_dirs=[]):
            return '/bin/' + arg

        def run_command(self, cmd, check_rc=True):
            self.run_command_calls.append(cmd)


# Generated at 2022-06-13 01:43:55.468955
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    intf1 = {'device': 'lan0',
             'ipv4': {'network': '192.168.1.1',
                      'interface': 'lan0',
                      'address': '192.168.1.76'}}
    intf2 = {'device': 'lan1',
             'ipv4': {'network': '192.168.2.1',
                      'interface': 'lan1',
                      'address': '192.168.2.76'}}
    intf3 = {'device': 'lan2f0',
             'ipv4': {'network': '192.168.3.1',
                      'interface': 'lan2f0',
                      'address': '192.168.3.76'}}

# Generated at 2022-06-13 01:43:58.959042
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    from ansible.module_utils.facts.network.hpu import HPUXNetwork
    interfaces = {}
    hn = HPUXNetwork({})
    interfaces = hn.get_interfaces_info()
    print (interfaces)

# Generated at 2022-06-13 01:44:05.816939
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    net_info = HPUXNetwork()
    net_info.module = MagicMock()
    net_info.module.run_command = MagicMock(return_value=(0, '', ''))
    net_info.populate()
    assert net_info.default_interface == 'lan0'
    assert net_info.default_gateway == '10.0.0.1'

    assert net_info.interfaces == ['lan0']
    assert net_info.lan0['device'] == 'lan0'
    assert net_info.lan0['ipv4']['address'] == '10.0.0.2'

# Generated at 2022-06-13 01:45:54.518085
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    HPUXNetworkCollector()

# Generated at 2022-06-13 01:45:56.236688
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    result = HPUXNetwork()
    assert result is not None, "Network is None"

# Generated at 2022-06-13 01:46:01.117677
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    interface_info = HPUXNetwork().get_interfaces_info()
    # lan1 should be present
    assert('lan1' in interface_info)
    # 10.1.1.1 should be the address of lan1
    assert('10.1.1.1' in interface_info['lan1']['ipv4']['address'])


# Generated at 2022-06-13 01:46:08.068330
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    from ansible.module_utils.basic import AnsibleModule
    def exec_command(command, check_rc=True):
        return 0, 'default 192.168.1.1 UG lan0 224', ''
    module = AnsibleModule(exec_command=exec_command, argument_spec={})
    results = HPUXNetwork(module).get_default_interfaces()
    assert results['default_gateway'] == '192.168.1.1'
    assert results['default_interface'] == 'lan0'


# Generated at 2022-06-13 01:46:11.000111
# Unit test for constructor of class HPUXNetwork
def test_HPUXNetwork():
    # Unit test for constructor of class HPUXNetwork
    module = MockModule()
    net_obj = HPUXNetwork(module)
    assert net_obj.module == module


# Generated at 2022-06-13 01:46:18.406852
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    net = HPUXNetwork()
    net.module = FakeAnsibleModule()

    expected_default_interface = 'lan0'
    expected_default_gateway = '127.0.0.1'

    net.module.run_command = execute_cmd
    net.get_default_interfaces = net.get_default_interfaces()

    assert net.get_default_interfaces['default_interface'] == expected_default_interface
    assert net.get_default_interfaces['default_gateway'] == expected_default_gateway



# Generated at 2022-06-13 01:46:22.455410
# Unit test for method populate of class HPUXNetwork
def test_HPUXNetwork_populate():
    fact_class = HPUXNetwork()
    interfaces = fact_class.get_interfaces_info()
    print(interfaces)
    for iface in interfaces:
        print(iface)
        for k in interfaces[iface]:
            print('  '+ k +':' + str(interfaces[iface][k]))
        print()


# Generated at 2022-06-13 01:46:28.706469
# Unit test for method get_default_interfaces of class HPUXNetwork
def test_HPUXNetwork_get_default_interfaces():
    class MockModule():
        def __init__(self, rc, out, err):
            self.rc = rc
            self.out = out
            self.err = err

        def run_command(self, cmd):
            return self.rc, self.out, self.err

    module = MockModule(0, 'default/UDP      *               *      *                    *  0     -      -                    rloc-4-0', None)
    obj = HPUXNetwork()
    obj.module = module
    expected_result = {'default_interface': 'lan0', 'default_gateway': '192.168.1.1'}
    result = obj.get_default_interfaces()
    assert result == expected_result

# Generated at 2022-06-13 01:46:35.220141
# Unit test for method get_interfaces_info of class HPUXNetwork
def test_HPUXNetwork_get_interfaces_info():
    """HPUXNetwork.get_interfaces_info() Test
    """
    from ansible.module_utils.facts.network.hpux.hpux_network import HPUXNetwork
    network = HPUXNetwork()
    interfaces = network.get_interfaces_info()
    assert interfaces == {'lan0': {'device': 'lan0',
                                   'ipv4': {'address': '0.0.0.0',
                                            'network': '0.0.0.0',
                                            'interface': 'lan0'}}}

# Generated at 2022-06-13 01:46:37.961011
# Unit test for constructor of class HPUXNetworkCollector
def test_HPUXNetworkCollector():
    """
    Constructor test HPUXNetworkCollector
    """
    hm = HPUXNetworkCollector()
    assert hm._fact_class == HPUXNetwork
    assert hm._platform == 'HP-UX'