

# Generated at 2022-06-13 01:37:52.505622
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    network_collector = HurdNetworkCollector()
    assert network_collector.platform == 'GNU'
    assert network_collector._fact_class == HurdPfinetNetwork



# Generated at 2022-06-13 01:37:54.924952
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    collector = HurdNetworkCollector()
    assert collector._platform == 'GNU'


# Generated at 2022-06-13 01:37:57.018703
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    hurd_pfinet_network = HurdPfinetNetwork({}, {})
    assert hurd_pfinet_network is not None

# Generated at 2022-06-13 01:37:59.520374
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    hnc = HurdNetworkCollector()

    assert(hnc.platform == 'GNU')
    assert(type(hnc._fact_class) == type(HurdPfinetNetwork))

# Generated at 2022-06-13 01:38:04.821364
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    # create test HurdPfinetNetwork instance
    from ansible.module_utils.facts import _NetworkCollectorBase
    test_instance = HurdPfinetNetwork(_NetworkCollectorBase.ModuleMock())
    assert test_instance
    assert isinstance(test_instance, HurdPfinetNetwork)

# Generated at 2022-06-13 01:38:14.763867
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )
    m_module = MagicMock(return_value=module)
    network = HurdPfinetNetwork(m_module)
    m_module.get_bin_path.return_value = None

    assert network.populate() is None

    m_module.get_bin_path.return_value = '/bin/fsysopts'
    m_module.run_command.return_value = (0, '''
        --interface=/dev/eth0
        --address=10.0.2.15
        --netmask=255.255.255.0
        --address6=fe80::7:8:9:a/64''', None)


# Generated at 2022-06-13 01:38:25.637634
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    from ansible.module_utils.facts.network.gnu import HurdPfinetNetwork
    from ansible.module_utils.facts.network.common import Network
    class MockModule:
        def command_help(a,b):
            return
        def run_command(self,xcmd):
            if xcmd[0] == '/rofs/bin/fsysopts':
                return (0,
"""
--address=10.1.1.1
--netmask=255.255.255.0
--interface=eth0
""", "")
            elif xcmd[0] == '/rofs/bin/foo':
                return (0,
"""
--address=10.1.1.1
--netmask=255.255.255.0
--interface=eth0
""", "")

# Generated at 2022-06-13 01:38:27.226633
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    network = HurdPfinetNetwork(dict())
    assert network.platform == 'GNU'

# Generated at 2022-06-13 01:38:30.198309
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    """
    Returns class object of HurdNetworkCollector.

    :return: class object of HurdNetworkCollector.
    :rtype: object
    """
    return HurdNetworkCollector(None)


# Generated at 2022-06-13 01:38:32.407219
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    obj = HurdNetworkCollector()
    assert obj._platform == 'GNU'
    assert obj._fact_class == HurdPfinetNetwork


# Generated at 2022-06-13 01:38:46.041487
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    module = AnsibleModule({})

    class MockHurdPfinetNetwork:
        def __init__(self, module):
            self.module = module

# Generated at 2022-06-13 01:38:51.861780
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    import ansible.module_utils.facts.network.hurd_pfinet as hurd_pfinet
    from ansible.module_utils.facts.network.hurd_pfinet import HurdPfinetNetwork

    class FakeHurdPfinetNetwork(HurdPfinetNetwork):
        def __init__(self, module, collected_facts=None):
            self.module = module
            self.collected_facts = collected_facts or {}

    class FakeMockRunner:
        def __init__(self, module):
            self.module = module


# Generated at 2022-06-13 01:38:53.028434
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    c = HurdNetworkCollector()
    assert c._platform == 'GNU'
    assert c._fact_class == HurdPfinetNetwork


# Generated at 2022-06-13 01:38:54.030379
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    HurdNetworkCollector()


# Generated at 2022-06-13 01:38:56.586336
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    assert HurdNetworkCollector.collect() == {
        'default_ipv4': {},
        'default_ipv6': [],
        'interfaces': []
    }

# Generated at 2022-06-13 01:39:07.963279
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    network_facts = {}
    fsysopts_path = '/bin/fsysopts'
    socket_path = '/servers/socket/inet6'
    network = HurdPfinetNetwork(None)

    # FIXME: cover the IPv6 path
    network_facts = network.assign_network_facts(
            network_facts, fsysopts_path, socket_path)
    assert network_facts

    assert 'interfaces' in network_facts
    assert 'lo' in network_facts['interfaces']
    assert 'eth0' in network_facts['interfaces']

    assert 'eth0' in network_facts
    assert network_facts['eth0']

    assert 'active' in network_facts['eth0']
    assert 'device' in network_facts['eth0']
    assert 'ipv4' in network

# Generated at 2022-06-13 01:39:19.031204
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():

    class test_module(object):
        def run_command(self, cmd):
            if cmd == ['fsysopts', '-L', '/servers/socket/inet']:
                return 0, """--interface=/dev/eth0 --address=192.168.10.122 --netmask=255.255.255.192 --broadcast=192.168.10.127 --network=192.168.10.128 --address6=fe80::5c00:f4ff:fe5e:d5f5/10""", ''

# Generated at 2022-06-13 01:39:26.636103
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():

    module = mock.Mock()
    module.run_command.return_value = 0, '--interface=/dev/lo0 --address=127.0.0.1 --netmask=255.0.0.0', None
    fact = HurdPfinetNetwork(module)
    facts = {}
    facts = fact.assign_network_facts(facts, "/bin/fsysopts", "/servers/socket/inet")

    assert facts['interfaces'] == ['lo0']
    assert facts['lo0'] == {
        'active': True,
        'device': 'lo0',
        'ipv4': {
            'address': '127.0.0.1',
            'netmask': '255.0.0.0',
        },
        'ipv6': [],
    }

# Generated at 2022-06-13 01:39:27.705568
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    x = HurdNetworkCollector()
    assert isinstance(x, HurdNetworkCollector)


# Generated at 2022-06-13 01:39:31.074539
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    module = NetworkCollector()
    for fact_class in HurdNetworkCollector.get_network_collector_classes():
        obj = fact_class(module)
        facts = obj.populate()
        assert 'interfaces' in facts
        assert len(facts['interfaces']) == 1
        assert 'eth0' in facts['interfaces']

# Generated at 2022-06-13 01:39:51.381739
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    m = AnsibleModule(
        argument_spec=dict(),
    )
    instances = [
        {
            'name': 'VM',
            'platform': HurdPfinetNetwork.platform,
            'default_ipv4': {
                'address': '10.0.0.1',
                'network': '10.0.0.0',
                'netmask': '255.255.255.0',
                'gateway': '10.0.0.2',
            },
            'default_ipv6': {
                'address': 'fe80::a00:27ff:fe87:48b8',
                'prefix': '64',
                'gateway': 'fe80::a00:27ff:fe87:48b9',
            },
        }
    ]
    nc = HurdNetwork

# Generated at 2022-06-13 01:39:55.419391
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    # test init function
    inst = HurdPfinetNetwork(None)

    # test assign_network_facts
    result = inst.assign_network_facts({}, '/path/to/fsysopts', '/socket/path')

    assert result['interfaces'] == []

# Generated at 2022-06-13 01:39:57.301728
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    c = HurdNetworkCollector()
    assert c is not None
    assert c._fact_class == HurdPfinetNetwork


# Generated at 2022-06-13 01:40:08.073094
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    module = MockModule()
    module.run_command.return_value = (0,
            '--interface=/dev/eth0 --address=192.168.0.1 --netmask=255.255.255.0 --mtu=1500',
            '')
    network_collector = HurdNetworkCollector(module)
    network_facts = network_collector.collect()

    assert network_facts['interfaces'] == ['eth0']
    assert network_facts['eth0']['active'] == True
    assert network_facts['eth0']['device'] == 'eth0'
    assert network_facts['eth0']['ipv4']['address'] == '192.168.0.1'

# Generated at 2022-06-13 01:40:14.747391
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    """
    Construct a HurdPfinetNetwork object and check if the
    socket_dir is correctly set.
    """
    import ansible.module_utils.facts.network.gnu
    import ansible.module_utils.facts.network.gnu_network_pfinet

    network_collector = ansible.module_utils.facts.network.gnu.HurdNetworkCollector()
    network_fact = ansible.module_utils.facts.network.gnu_network_pfinet.HurdPfinetNetwork(network_collector)
    assert network_fact._socket_dir == '/servers/socket/'


# Generated at 2022-06-13 01:40:21.909197
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    module = MockModule()
    network = HurdPfinetNetwork(module)
    module.run_command.return_value = (0, "--interface=/dev/eth0 --address=10.0.2.15 --netmask=255.255.255.0 --address6=fe80::5054:ff:fe6d:6483/64", "")
    network.populate()

    assert module.run_command.called == 1
    assert module.run_command.call_args[0][0] == ['/bin/fsysopts', '-L', '/servers/socket/inet']
    assert 'interfaces' in network.data
    assert network.data['interfaces'] == ['eth0']
    assert len(network.data['eth0']['ipv6']) == 1

# Generated at 2022-06-13 01:40:22.686590
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    pass

# Generated at 2022-06-13 01:40:31.940746
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    import platform
    from ansible.module_utils.facts.network.gnu import HurdPfinetNetwork

    def mock_run_command(self, args, check_rc=False, close_fds=True, executable=None, data=None, binary_data=False, path_prefix=None, cwd=None, use_unsafe_shell=False, prompt_regex=None):
        return (0, "option1=value1\noption2=value2\noption3=value3\n", "")

    module = platform
    module.run_command = mock_run_command
    fsysopts_path = '/usr/bin/fsysopts'
    socket_path = '/servers/socket/inet'
    network_facts = {}


# Generated at 2022-06-13 01:40:42.391386
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    module = AnsibleModule(argument_spec={})
    collector = HurdNetworkCollector(module=module)
    network = collector.collect()[0]
    network_facts = {}

    # test empty output
    network_facts = network.assign_network_facts(network_facts, 'fsysopts', '/servers/socket/inet6')
    assert network_facts == {}

    # test full output
    module.run_command = MagicMock(return_value=(0,
"""--interface=/dev/eth0 --address=10.20.30.40 --netmask=255.255.255.0 --address6=fe80::2030:4050:6070:8090/64
""",
        ""))


# Generated at 2022-06-13 01:40:52.851095
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    from ansible.module_utils.facts.network.hurd import HurdPfinetNetwork

    # When fsysopts_path is None
    network = HurdPfinetNetwork({}, {}, [])
    assert network.populate() == {}

    # When fsysopts_path is found and socket_path is None
    network = HurdPfinetNetwork({}, {}, [])
    network.module.get_bin_path = lambda x: '/bin/' + x
    assert network.populate() == {}

    # When fsysopts_path is found and socket_path is found
    network = HurdPfinetNetwork({}, {}, [])
    network._socket_dir = '../test_sockets/'

# Generated at 2022-06-13 01:41:18.071947
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    network = HurdPfinetNetwork({})

    assert network.platform == 'GNU', 'platform should be GNU'
    assert network._socket_dir == '/servers/socket/', 'socket_dir should be /servers/socket/'



# Generated at 2022-06-13 01:41:25.359193
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    # Test with a valid 'fsysopts'
    m = AnsibleModule(argument_spec={})
    m._ansible_version = 2.7
    m.run_command = MagicMock(return_value = (0, "--address10.1.1.1 --netmask255.255.255.0 --interface/dev/eth0 --address6fe80::32e7:f6ff:fea2:e422/64", ""))
    m.get_bin_path = MagicMock(return_value = "/bin/fsysopts")

    n = HurdPfinetNetwork(m)
    network_facts = {'interfaces': []}
    network_facts = n.assign_network_facts(network_facts, "/bin/fsysopts", "/servers/socket/inet")
    assert network

# Generated at 2022-06-13 01:41:34.167678
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    test_module = HurdPfinetNetwork({})
    test_network_facts = {
        "interfaces": [],
    }
    test_fsysopts_path = "/bin/fsysopts"
    test_socket_path = "/tmp"
    test_command_output = """--interface=/dev/eth0
--address=1.2.3.4
--netmask=255.255.255.0
--address6=2::4/64
--interface=/dev/eth1
--address=5.6.7.8
--netmask=255.255.255.0
--address6=2::8/64"""
    test_module.module.run_command = MagicMock(return_value=(0, test_command_output, None))

# Generated at 2022-06-13 01:41:37.693041
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    m = type('Module', (), dict())
    m.get_bin_path = lambda x: '/bin/' + x
    m.run_command = lambda x: (0, '', '')
    # TODO: assert over content
    HurdPfinetNetwork(m).populate()

# Generated at 2022-06-13 01:41:39.085421
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    hpn = HurdPfinetNetwork(None)
    assert hpn.platform == 'GNU'


# Generated at 2022-06-13 01:41:43.050226
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    """This is to test the constructor of class HurdNetworkCollector"""
    hnc = HurdNetworkCollector()
    assert hnc._platform == 'GNU'
    assert hnc._fact_class == HurdPfinetNetwork

# Generated at 2022-06-13 01:41:44.605066
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    network = HurdPfinetNetwork({'ansible_facts': {}})
    assert network

# Generated at 2022-06-13 01:41:50.486458
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    net_facts = HurdPfinetNetwork()
    # create a fake module
    class FakeModule(object):
        def run_command(self, command):
            return (0, \
'''--interface=eth0
--address=192.168.1.1
--netmask=255.255.255.0
--interface=eth1
--address=192.168.2.1
--netmask=255.255.255.0
--address6=2001:db8:0:1234::/64
--address6=2001:db8:0:5678::/64''', '')
    net_facts.module = FakeModule()
    network_facts = net_facts.assign_network_facts({}, '/bin/fsysopts', '/socket/inet6')

# Generated at 2022-06-13 01:41:53.834710
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    g = HurdNetworkCollector()
    assert g._platform == "GNU"
    assert g._fact_class == HurdPfinetNetwork
    assert g.platform == "GNU"
    assert g.fact_class == HurdPfinetNetwork

# Generated at 2022-06-13 01:41:57.375205
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    from ansible.module_utils import basic
    from ansible.module_utils.facts import collector

    data = {
        'ansible_facts': {
            'os_family': 'GNU',
        },
    }
    facts = collector.collect(basic.AnsibleModule(data), data)
    assert 'interfaces' not in facts['ansible_network_resources']
    assert 'ipv4' not in facts['ansible_network_resources']
    assert 'ipv6' not in facts['ansible_network_resources']
    assert 'device' not in facts['ansible_network_resources']

# Generated at 2022-06-13 01:42:52.920271
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    module = AnsibleModule(argument_spec={})
    network = HurdPfinetNetwork(module)
    network_facts = {}
    fsysopts_path = '/hurd/pfinet'
    socket_path = '/servers/socket/inet'
    module.run_command = MagicMock(return_value=(0, 'interface=/dev/eth0  address=192.168.1.10  netmask=255.255.255.0  --address6=fe80::216:3eff:fea3:2bbf/64', None))
    network_facts = network.assign_network_facts(network_facts, fsysopts_path, socket_path)
    assert network_facts['interfaces'] == ['eth0']

# Generated at 2022-06-13 01:43:02.311684
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    module = AnsibleModule(
        argument_spec = dict(),
        supports_check_mode = True
    )

    pfinet_network = HurdPfinetNetwork(module)
    network_facts = pfinet_network.populate()

    assert('interfaces' in network_facts)
    assert('lo' in network_facts['interfaces'])
    assert('eth0' in network_facts['interfaces'])

    assert('lo' in network_facts)
    assert('ipv4' in network_facts['lo'])
    assert('address' in network_facts['lo']['ipv4'])
    assert('netmask' in network_facts['lo']['ipv4'])
    assert('ipv6' in network_facts['lo'])
    assert('eth0' in network_facts)


# Generated at 2022-06-13 01:43:11.864904
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    from ansible_collections.ansible.gnu.plugins.modules.network.os import facts
    module = facts.setup_module()
    module.params = {'gather_network_resources': 'all', 'gather_subset': ['all']}
    module.expand_dhcp_options = lambda x: x

    # create an HurdPfinetNetwork object
    network = HurdPfinetNetwork(module)

    # obtain raw value of fsysopts output
    with open(os.path.join(os.path.dirname(__file__),
                           'fsysopts_output'), 'rb') as f:
        fsysopts_output = f.read().decode('utf-8')

    # create an empty dict to store network_facts
    network_facts = dict()

    # assign network resources

# Generated at 2022-06-13 01:43:13.549208
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    obj = HurdNetworkCollector()

    assert obj.platform == 'GNU'
    assert obj.fact_class == HurdPfinetNetwork


# Generated at 2022-06-13 01:43:24.054459
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    mod = AnsibleModule(argument_spec=dict())
    HurdPfinetNetwork.module = mod

    HurdPfinetNetwork.module.get_bin_path = MagicMock(return_value='/usr/bin/fsysopts')
    HurdPfinetNetwork.module.run_command = MagicMock(return_value=(0, "abcd"))

    network_facts = HurdPfinetNetwork.populate()
    assert len(network_facts['interfaces']) == 0

    HurdPfinetNetwork.module.run_command = MagicMock(return_value=(0, "--interface=/dev/eth0 --address=10.10.10.10 --netmask=255.255.255.0 --address6=fd00::1/64"))
    network_facts = HurdPfinetNetwork.pop

# Generated at 2022-06-13 01:43:33.470491
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    network_facts = {}
    network_facts['interfaces'] = []
    fsysopts_path = '/gnumach/fsysopts'
    socket_path = '/servers/socket/inet'
    class mock_module:
        def run_command(self, command):
            out = '''--interface=/dev/eth0 --address=172.16.0.100 --netmask=255.255.255.0 --address6=fde7:f80:45ab:7a2:1d6c:9b73:56e:5fa6/64 --address6=fe80::1d6c:9b73:56e:5fa6/64'''
            return 0, out, ''
    class fake_self:
        def __init__(self, module):
            self.module = module
    module

# Generated at 2022-06-13 01:43:37.665085
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    mod = MagicMock()
    mod.exit_json.side_effect = SystemExit

    hpn = HurdPfinetNetwork(module=mod)
    assert hpn.netmask is None
    assert hpn.module is mod
    assert hpn.ipv4 is None
    assert hpn.ipv6 is None
    assert hpn.network is None
    assert hpn.prefix is None
    assert hpn.broadcast is None
    assert hpn.macaddress is None



# Generated at 2022-06-13 01:43:39.761038
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    assert HurdNetworkCollector._platform == 'GNU'
    assert HurdNetworkCollector._fact_class == HurdPfinetNetwork



# Generated at 2022-06-13 01:43:44.352035
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    device = HurdPfinetNetwork()
    collected_facts = {
        'ansible_facts': {
            'module_setup': True
        }
    }
    result = device.populate(collected_facts)
    assert 'interfaces' in result.keys()

# Generated at 2022-06-13 01:43:45.359308
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    pfinet = HurdPfinetNetwork()
    assert pfinet.platform == 'GNU'


# Generated at 2022-06-13 01:45:45.720843
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    assert isinstance(HurdPfinetNetwork(), HurdPfinetNetwork)



# Generated at 2022-06-13 01:45:47.316664
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    '''Unit test for constructor of class HurdPfinetNetwork'''
    HurdPfinetNetwork(dict())

# Generated at 2022-06-13 01:45:55.005021
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    HurdSock = {
        'inet' : ['/servers/socket/inet'],
        'inet6' : []
    }


# Generated at 2022-06-13 01:45:58.360568
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    collector = HurdNetworkCollector()
    assert collector.platform == 'GNU'
    assert collector._fact_class == HurdPfinetNetwork

# Generated at 2022-06-13 01:46:07.934558
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    '''
    Unit test for method populate of class HurdPfinetNetwork
    '''
    # mock module and return a network facts as expected by HurdPfinetNetwork
    module_mock = MockModule({
        'run_command': (0, '/dev/eth0\n--address=10.0.2.15\n--address6=fe80::a00:27ff:fe8c:d221/64\n--interface=/dev/eth0\n--link=2a:00:27:8c:d2:21\n--mtu=1500\n--netmask=255.255.255.0\n', '')
    })
    # create instance of HurdPfinetNetwork
    network = HurdPfinetNetwork(module_mock)
    # call populate
    network.populate()
   

# Generated at 2022-06-13 01:46:09.757845
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    from ansible.module_utils.facts.network.hurd import HurdPfinetNetwork
    facts_obj = HurdPfinetNetwork(None, {})
    assert facts_obj.platform == 'GNU'

# Generated at 2022-06-13 01:46:19.575171
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    class MockModule:
        def get_bin_path(self, command):
            return 'fsysopts'

        def run_command(self, command):
            # fsysopts -L /servers/socket/inet output
            if command == ['/servers/socket/inet', '-L', '/servers/socket/inet']:
                return (0, '''--interface=/dev/eth0 --address=10.0.2.15 --netmask=255.255.255.0 ''', '')
            # fsysopts -L /servers/socket/inet6 output

# Generated at 2022-06-13 01:46:21.769452
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    assert HurdNetworkCollector.__name__ == 'HurdNetworkCollector'
    assert HurdNetworkCollector._platform == 'GNU'
    assert HurdNetworkCollector._fact_class == HurdPfinetNetwork


# Generated at 2022-06-13 01:46:22.428851
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    HurdNetworkCollector()

# Generated at 2022-06-13 01:46:23.079674
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    assert HurdPfinetNetwork()