

# Generated at 2022-06-13 01:37:53.968761
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    from ansible.module_utils.facts.network.gnu.pfinet import HurdPfinetNetwork
    network = HurdPfinetNetwork(None)

    network_facts = {
        'interfaces': [],
    }

    fsysopts = '''--interface=eth0
--address=127.0.0.1
--netmask=255.0.0.0
--address6=::1/64
--interface=lo
--address=127.0.0.1
--netmask=255.0.0.0
--address6=::1/128
'''
    network_facts = network.assign_network_facts(network_facts, None, None)

# Generated at 2022-06-13 01:37:58.361914
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    class FakeModule:
        def run_command(self, command):
            return 0, '', ''

    module = FakeModule()
    fake_network = HurdPfinetNetwork(module)
    fake_network.assign_network_facts({}, '', '')
    # only check that this did not raise an exception

# Generated at 2022-06-13 01:37:59.751304
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    assert HurdPfinetNetwork(None)


# Generated at 2022-06-13 01:38:03.545157
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    c = HurdNetworkCollector()
    # Create an instance of HurdPfinetNetwork
    f = c.collect()

    assert f
    assert f.platform == 'GNU'

# Generated at 2022-06-13 01:38:06.380128
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    c = HurdNetworkCollector()
    assert c.platform == 'GNU'


# Generated at 2022-06-13 01:38:08.690907
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    collect_network_facts = HurdPfinetNetwork()
    assert collect_network_facts.platform == 'GNU'

# Generated at 2022-06-13 01:38:09.995678
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    # FIXME: it would be nice to be able to unit test this method.
    pass

# Generated at 2022-06-13 01:38:17.340740
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    class HurdModule(object):
        def __init__(self):
            self.run_command_count = 0

        def run_command(self, args):
            self.run_command_count += 1
            self.cmd = args
            return 0, '', ''

    class HurdPfinetNetworkTest(HurdPfinetNetwork):
        def __init__(self):
            self.module = HurdModule()

    class HurdNetworkCollectorTest(HurdNetworkCollector):
        def __init__(self):
            self.module = HurdModule()

    # test method assign_network_facts
    # test with empty return
    d = HurdNetworkCollectorTest()
    d.module.run_command = lambda x: (0, '', '')
    true_test = d.get_facts()
   

# Generated at 2022-06-13 01:38:19.106395
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    x = HurdNetworkCollector()

# Generated at 2022-06-13 01:38:21.308190
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    assert HurdPfinetNetwork.platform == 'GNU'
    assert HurdPfinetNetwork._socket_dir == '/servers/socket/'

# Generated at 2022-06-13 01:38:34.208964
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    m = MagicMock()
    m.run_command = MagicMock(return_value=(0, '--interface=/dev/eth0 --address=127.0.0.1 --netmask=255.255.255.0 --address6=::1/128', ''))

    c = HurdPfinetNetwork(m, '')
    network_facts = {}

# Generated at 2022-06-13 01:38:43.807354
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    module = AnsibleModule(argument_spec={})
    # populate() method use only module.get_bin_path()
    def mock_get_bin_path(arg):
        if arg == 'fsysopts':
            return True
        return None
    module.get_bin_path = mock_get_bin_path
    # populate() method use only module.run_command()
    def mock_run_command(arg):
        # fsysopts -L /servers/socket/inet
        if arg == ['fsysopts', '-L', '/servers/socket/inet']:
            return (0, "--interface=/dev/eth0 --address=192.168.1.5 --netmask=255.255.255.0 --address=/dev/eth1 --address6=fec0::1/64", None)


# Generated at 2022-06-13 01:38:46.466105
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    hpn = HurdPfinetNetwork()

    assert hpn.platform == 'GNU'


# Generated at 2022-06-13 01:38:56.684472
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    class MockMod():
        def __init__(self):
            self.fsysopts_path = '/bin/fsysopts'
            self.socket_path = '/servers/socket/inet'
            self.rc = 0
            self.out = '--interface=/dev/eth0 --address=192.168.0.1 --netmask=255.255.255.0'
            self.err = ''

        def run_command(self, cmd):
            assert cmd == [self.fsysopts_path, '-L', self.socket_path]
            return self.rc, self.out, self.err

    net = HurdPfinetNetwork(MockMod())
    net_facts = {'ansible_net_interfaces': []}

# Generated at 2022-06-13 01:39:08.096741
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    module = type('',(object,),{
        'run_command': lambda self, cmd: (0, '--interface=/dev/eth0 --address=10.0.0.1 --netmask=255.255.255.0 --address6=fe80::1/64', ''),
        })()
    network_facts = {}
    expected = {
        'interfaces': ['eth0'],
        'eth0': {
            'device': 'eth0',
            'active': True,
            'ipv4': {'address': '10.0.0.1', 'netmask': '255.255.255.0'},
            'ipv6': [{'address': 'fe80::1', 'prefix': '64'}],
        },
    }
    h = HurdPfinetNetwork(module)
   

# Generated at 2022-06-13 01:39:19.171093
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    # test given
    module = MockModule()
    network = HurdPfinetNetwork(module=module, socket_path='/servers/socket')
    module.run_command = MockRunCommand()

    # when
    network_facts = network.assign_network_facts({}, 'fsysopts', '/servers/socket')

    # then

# Generated at 2022-06-13 01:39:21.550266
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    collector = HurdNetworkCollector(None)
    assert collector
    assert collector.platform == 'GNU'
    assert collector.fact_class == HurdPfinetNetwork

# Generated at 2022-06-13 01:39:23.670094
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    obj = HurdNetworkCollector()
    assert obj.platform == 'GNU'
    assert obj._fact_class == HurdPfinetNetwork

# Unit tests for pfinet interface class

# Generated at 2022-06-13 01:39:29.346743
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    test_module = type('AnsibleModule', (object,), dict(
        run_command=lambda self, args, check_rc=True: (0, "--interface=/dev/eth0 --address=192.168.0.2 --netmask=0.0.0.0 --address6=2001:db8::ff00:42:8329/64 --address6=2001:db8:1234:5678::ff00:42:8329/64", ""),
        get_bin_path=lambda self, arg: "/bin/fsysopts",
    ))
    test_network_facts = {}
    obj = HurdPfinetNetwork(test_module)
    fsysopts_path = "/bin/fsysopts"
    socket_path = '/servers/socket/inet'
    result = obj.assign

# Generated at 2022-06-13 01:39:30.121092
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    assert HurdPfinetNetwork is not None

# Generated at 2022-06-13 01:39:41.660131
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    module = AnsibleModuleMock({})
    assert HurdPfinetNetwork(module) is not None

# Generated at 2022-06-13 01:39:44.561517
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    from ansible.module_utils.facts.network.gnu import HurdPfinetNetwork
    module = AnsibleModuleMock()
    n = HurdPfinetNetwork(module)
    assert n.populate() == {}

# Generated at 2022-06-13 01:39:48.316004
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    fsysopts_path = 'tests/unittests/module_utils/facts/network/fsysopts'
    socket_path = 'tests/unittests/module_utils/facts/network/socket'

    n = HurdPfinetNetwork()
    n.module.run_command = lambda args, **kwargs: (0, '', '')
    n.module.get_bin_path = lambda s: fsysopts_path

    # FIXME: check empty
    result = n.populate()
    assert result == {}

    # FIXME: check content
    # n.module.run_command = do_run_command_with_content
    # n.module.get_bin_path = lambda s: fsysopts_path



# Generated at 2022-06-13 01:39:58.134733
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    module_mock = Mock()
    fsysopts_mock = Mock()
    module_mock.run_command.return_value = (0,
            "--interface=/dev/eth0 --address=10.0.0.1 --netmask=255.0.0.0 --address6=fdfd:7827::1/64\n",
            None)
    network_facts = {}
    network = HurdPfinetNetwork(module_mock)
    network.assign_network_facts(network_facts, fsysopts_mock, None)
    assert network_facts['interfaces'] == ['eth0']

# Generated at 2022-06-13 01:40:00.962455
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    collector = HurdNetworkCollector()
    assert collector.platform == 'GNU'
    assert collector.fact_class == HurdPfinetNetwork


# Generated at 2022-06-13 01:40:11.565611
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    import ansible.module_utils.facts.network.pfinet.pfinet as pfinet
    import ansible.module_utils.facts.network.pfinet.collector as collector

    pfinet_module = collector.HurdNetworkCollector()
    pfinet_module.set_module(ansible_module=MockModule())
    pfinet_module.set_fsysopts_path(path='test/resources/test_fsysopts')

    socket_path = 'test/resources/test_socket'
    result = pfinet_module._populate_interface_info(socket_path)
    assert result['interfaces'] == ['eth0']
    assert result['eth0']['active']
    assert result['eth0']['device'] == 'eth0'

# Generated at 2022-06-13 01:40:13.044150
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    assert HurdPfinetNetwork(None).populate() == {}

# Generated at 2022-06-13 01:40:15.776438
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    nc = HurdNetworkCollector()
    assert nc._platform == 'GNU'
    assert nc._fact_class == HurdPfinetNetwork


# Generated at 2022-06-13 01:40:17.993401
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    test_network = HurdPfinetNetwork(None)
    assert test_network.platform == 'GNU'
    assert test_network._socket_dir == '/servers/socket/'


# Generated at 2022-06-13 01:40:19.005300
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    network = HurdPfinetNetwork({})
    assert network



# Generated at 2022-06-13 01:40:41.471215
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    from ansible.module_utils.facts.network.hurd.pfinet import HurdPfinetNetwork
    network_facts = HurdPfinetNetwork()

    assert network_facts.platform is 'GNU'

# Generated at 2022-06-13 01:40:45.310995
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    c = HurdNetworkCollector()
    assert c._platform == 'GNU'
    assert c._fact_class == HurdPfinetNetwork


# Generated at 2022-06-13 01:40:54.073335
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    from ansible.module_utils.facts.network.base import NetworkCollector

    network_facts = {}

    ipv4_addresses = [
        '192.168.1.1',
        '192.168.1.2',
        '192.168.1.3',
    ]

    ipv6_addresses = [
        '2001:d8::b',
        '2001:d8::c',
    ]

    out = NetworkCollector.combine_ip_output(ipv4_addresses, ipv6_addresses)

    nw = HurdPfinetNetwork()
    nw.module = MockModule()
    nw.module.run_command.return_value = (0, out, '')

# Generated at 2022-06-13 01:40:56.886093
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    """
    Create an instance of HurdNetworkCollector.
    """
    hurd_n_col = HurdNetworkCollector()
    assert hurd_n_col.platform == 'GNU'
    assert hurd_n_col._fact_class == HurdPfinetNetwork

# Generated at 2022-06-13 01:40:57.507210
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    HurdPfinetNetwork({})

# Generated at 2022-06-13 01:41:06.093844
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    network_facts = HurdPfinetNetwork()
    result = network_facts.get_device_info('eth0')
    assert result['device'] == 'eth0'
    assert result['ipv4']['address'] == '192.168.1.10'
    assert result['ipv4']['netmask'] == '255.255.255.0'
    assert result['ipv6'][0]['address'] == 'fe80::f816:3eff:fe44:715f'
    assert result['ipv6'][0]['prefix'] == '64'



# Generated at 2022-06-13 01:41:11.115319
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    nc = HurdNetworkCollector()
    assert nc._platform == 'GNU', "The _platform attribute of the HurdNetworkCollector instance should be GNU"
    assert nc._fact_class == HurdPfinetNetwork, "The _fact_class attribute of the HurdNetworkCollector instance should be HurdPfinetNetwork"


# Generated at 2022-06-13 01:41:13.299269
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    network_collector = HurdNetworkCollector()
    assert network_collector._platform == 'GNU'


# Generated at 2022-06-13 01:41:16.047588
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    ansible_facts = {'facts': {
                        'ansible_kernel': 'GNU',
                    }
    }
    assert HurdPfinetNetwork(None, ansible_facts).populate()


# Generated at 2022-06-13 01:41:19.930514
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    hnetwork = HurdPfinetNetwork(None)
    assert hnetwork.module is None
    assert hnetwork.platform == 'GNU'
    assert hnetwork._platform == 'GNU'
    assert hnetwork._socket_dir == '/servers/socket/'
    assert hnetwork._fact_class == HurdPfinetNetwork


# Generated at 2022-06-13 01:42:05.186644
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    klass = HurdNetworkCollector()
    assert klass.platform == 'GNU'
    assert klass._fact_class == HurdPfinetNetwork

# Test for HurdNetworkCollector.populate()
# Test for HurdPfinetNetwork.populate()

# Generated at 2022-06-13 01:42:11.271288
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    module = MagicMock()
    module.run_command = MagicMock(return_value=(0,
                                                 '--address=10.0.2.15 --netmask=255.255.255.0 --address6=fe80::a00:27ff:fea7:fa6d/64 --netmask6=ffff:ffff:ffff:ffff::',
                                                 '',))
    module.get_bin_path = MagicMock(return_value='/boot/test')
    fact = HurdPfinetNetwork(module)
    network_facts = fact.populate()


# Generated at 2022-06-13 01:42:14.099963
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    fact_class = HurdPfinetNetwork(dict())
    assert fact_class.platform == 'GNU'
    assert fact_class._socket_dir == '/servers/socket/'


# Generated at 2022-06-13 01:42:24.559363
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    module = AnsibleModuleMock()
    module.run_command = MagicMock(return_value=(0, '--interface=/dev/eth0 --address=192.168.1.5 --netmask=255.255.255.0 --address6=2001:6b0:1:10a2::2/64', ''))
    network_facts = {}
    # FIXME: test with ipv6
    network_facts = HurdPfinetNetwork(module).assign_network_facts(network_facts, '/bin/fsysopts', '/servers/socket/inet')
    assert network_facts['interfaces'] == ['eth0']
    assert network_facts['eth0']['ipv4']['address'] == '192.168.1.5'

# Generated at 2022-06-13 01:42:31.372950
# Unit test for method assign_network_facts of class HurdPfinetNetwork

# Generated at 2022-06-13 01:42:34.921152
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    fact_class = HurdNetworkCollector()
    assert fact_class.get_fact_class() is HurdPfinetNetwork

# Generated at 2022-06-13 01:42:37.388046
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    obj1=HurdPfinetNetwork()
    assert obj1.platform=='GNU'
    assert obj1._socket_dir=='/servers/socket/'


# Generated at 2022-06-13 01:42:38.824777
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    # Should return an empty dict
    HurdPfinetNetwork().populate({})



# Generated at 2022-06-13 01:42:41.106782
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    assert HurdNetworkCollector._platform == 'GNU'
    assert HurdNetworkCollector._fact_class is HurdPfinetNetwork

# Generated at 2022-06-13 01:42:48.630091
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    module = AnsibleModule(argument_spec={})
    module.run_command = MagicMock(return_value=(0, '--interface=eth0 --address=127.0.0.1 --netmask=255.255.255.0', ''))
    network = HurdPfinetNetwork(module)
    network.populate()
    assert module.run_command.called


# Generated at 2022-06-13 01:44:36.825067
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    import sys
    sys.path.append('lib/ansible/module_utils/facts/network')
    from module_utils.facts.network import Network

    # We are not using module, we are using Network directly
    from importlib import reload
    module = Network()
    module.run_command = test_run_command
    module.params = {}

    net = HurdPfinetNetwork()
    net.module = module
    net.platform = 'GNU'

    # test with invalid fsysopts_path
    assert net.assign_network_facts({}, 'invalid_path', '/servers/socket/inet') == {}

    # test with valid fsysopts_path and invalid socket_path
    assert net.assign_network_facts({}, 'fsysopts_path', 'invalid_path') == {}



# Generated at 2022-06-13 01:44:44.710381
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    # Assign network facts
    network_facts = {}
    network_facts['interfaces'] = []
    current_if = 'eth0'
    socket_path = '/servers/socket/inet'
    fsysopts_path = '/hurd/fsysopts'
    out = '--interface=/dev/eth0 --address=192.168.0.3 --netmask=255.255.255.0 --address6=2a00:1450:400c:c03::6c/64'
    network_facts = HurdPfinetNetwork().assign_network_facts(network_facts, fsysopts_path, socket_path)

    # Assert network facts
    assert sorted(network_facts) == ['interfaces', u'eth0']
    assert network_facts['interfaces'] == [u'eth0']

# Generated at 2022-06-13 01:44:54.073739
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    class TestModule:
        def run_command(self, command):
            return (0, '--address6=2a01:e34:ee2e:7c10:a00:20ff:fe73:9d9b/64 --address=149.13.33.59 --netmask=255.255.255.0 --interface=/dev/eth0 --interface_mode=none --address6=2a01:e34:ee2e:7c10::22/64 --address6=fe80::a00:20ff:fe73:9d9b/64', None)
    tm = TestModule()
    hn = HurdPfinetNetwork(tm)
    network_facts = hn.assign_network_facts({}, 'fsysopts', '/servers/socket/inet')

# Generated at 2022-06-13 01:45:03.831862
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    from ansible_collections.ansible.community.tests.unit.module_utils._text import to_bytes
    from ansible.module_utils.facts.network.gnu import HurdPfinetNetwork
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.network.gnu import HurdNetworkCollector
    from ansible.module_utils.facts.network.generic_bsd import GenericBsdNetwork
    from ansible.module_utils.facts.network.rename_link import RenameLinkNetwork

    #test that it's a subclass of GenericBsdNetwork and RenameLinkNetwork
    assert issubclass(HurdPfinetNetwork, GenericBsdNetwork)
    assert issubclass(HurdPfinetNetwork, RenameLinkNetwork)

    #test that it's a

# Generated at 2022-06-13 01:45:06.317943
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    hnc = HurdNetworkCollector()
    assert hnc.platform == 'GNU'
    assert hnc._fact_class == HurdPfinetNetwork

# Generated at 2022-06-13 01:45:09.816394
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    assert issubclass(HurdNetworkCollector, NetworkCollector)
    assert HurdNetworkCollector._platform == 'GNU'
    assert HurdNetworkCollector._fact_class == HurdPfinetNetwork


# Generated at 2022-06-13 01:45:17.223681
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    from ansible.module_utils.facts.network.hurd import HurdPfinetNetwork
    module = AnsibleModule(
        argument_spec = dict(),
        supports_check_mode = False
    )
    network = HurdPfinetNetwork(module)
    fsysopts_path = '/bin/fsysopts'
    socket_path = '/servers/socket/inet'
    out = '--interface=/dev/eth0 --address=127.0.0.1 --netmask=255.0.0.0'
    network_facts = {}
    network_facts = network.assign_network_facts(network_facts, fsysopts_path, socket_path)
    assert network_facts['lo']['ipv4']['address'] == '127.0.0.1'
    assert network_

# Generated at 2022-06-13 01:45:20.755552
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    '''
    This is a unit test for constructor of class HurdNetworkCollector
    '''
    obj = HurdNetworkCollector()
    assert obj._platform == 'GNU'
    assert obj._fact_class == HurdPfinetNetwork


# Generated at 2022-06-13 01:45:31.646905
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    module = AnsibleModule(argument_spec={})
    i = HurdPfinetNetwork(module)
    network_facts = {}
    network_facts = i.assign_network_facts(network_facts, i.module.get_bin_path('fsysopts'), '/servers/socket/inet')
    assert network_facts['interfaces'] == ['eth0']
    assert network_facts['eth0']['ipv4']['address'] == '192.168.1.5'
    assert network_facts['eth0']['ipv4']['netmask'] == '255.255.255.0'
    assert network_facts['eth0']['ipv6'] == [{'prefix': '64', 'address': '2001:db8::2'}]


# Generated at 2022-06-13 01:45:36.995864
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    module = AnsibleModule(argument_spec={})
    # create instance of HurdPfinetNetwork
    network = HurdPfinetNetwork(module)

    collected_facts = {}
    # call method populate of HurdPfinetNetwork
    result = network.populate(collected_facts)
    assert result
    assert 'interfaces' in result
    assert result.get('interfaces', None) != []
    assert result.get('lo', None) != {}