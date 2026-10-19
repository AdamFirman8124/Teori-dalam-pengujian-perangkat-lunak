

# Generated at 2022-06-13 01:37:52.030409
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True)

    # mock module
    module.get_bin_path = MagicMock(return_value=None)

    network = HurdPfinetNetwork(module)
    network_facts = network.populate()
    assert network_facts == {}

# Generated at 2022-06-13 01:37:57.413802
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    from ansible.module_utils.facts import FactCollector

    module = AnsibleModule(
        argument_spec = dict(
            gather_network_resources=dict(type='bool', default=True),
        )
    )
    collector = FactCollector(module=module)
    collected_facts = collector.collect(['network'], None)['ansible_network_resources']
    assert collected_facts['interfaces'] == ['eth0']
    assert collected_facts['eth0']['device'] == 'eth0'
    assert collected_facts['eth0']['ipv4']['address'] == '192.168.56.4'
    assert collected_facts['eth0']['ipv4']['netmask'] == '255.255.255.0'

# Generated at 2022-06-13 01:38:07.152271
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True)
    network = HurdPfinetNetwork(module)

    fsysopts_path = network.module.get_bin_path('fsysopts')
    if fsysopts_path is None:
        return

    socket_path = None

    for l in ('inet', 'inet6'):
        link = os.path.join(network._socket_dir, l)
        if os.path.exists(link):
            socket_path = link
            break

    if socket_path is None:
        return

    network_facts = {}
    network.assign_network_facts(network_facts, fsysopts_path, socket_path)


# Generated at 2022-06-13 01:38:09.899368
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    assert HurdNetworkCollector._platform == 'GNU'
    assert HurdNetworkCollector._fact_class == HurdPfinetNetwork

# Generated at 2022-06-13 01:38:11.160392
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    assert HurdPfinetNetwork.platform == 'GNU'
    assert HurdPfinetNetwork._socket_dir == '/servers/socket/'

# Generated at 2022-06-13 01:38:13.340597
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    net = HurdPfinetNetwork()
    assert net.platform == 'GNU'
    assert net._socket_dir == '/servers/socket/'


# Generated at 2022-06-13 01:38:17.364391
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    from ansible.module_utils.facts.network.pfinet.collector import HurdPfinetNetwork
    obj = HurdPfinetNetwork(module=None)
    assert isinstance(obj, HurdPfinetNetwork)
    assert isinstance(obj, Network)
    assert obj.platform == 'GNU'
    assert obj.assign_network_facts(network_facts=None, fsysopts_path=None, socket_path=None) is None


# Generated at 2022-06-13 01:38:19.918544
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    collectors = {}
    collector = HurdNetworkCollector(collectors)
    assert collector is not None


# Generated at 2022-06-13 01:38:22.476116
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    
    h = HurdPfinetNetwork(None)
    h.module = None
    h.assign_network_facts({}, 'foo', 'bar')

# Generated at 2022-06-13 01:38:23.105644
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    assert HurdPfinetNetwork().platform == 'GNU'


# Generated at 2022-06-13 01:38:31.877673
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():

    my_network = HurdPfinetNetwork({'ansible_facts': {'ansible_machine': 'i686'}})
    assert my_network.get_platform() == 'GNU'
    assert my_network.get_socket_dir() == '/servers/socket/'



# Generated at 2022-06-13 01:38:34.961788
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    network = HurdPfinetNetwork()

    assert network.platform == 'GNU'
    assert network._socket_dir == '/servers/socket/'


# Generated at 2022-06-13 01:38:44.309809
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    module = AnsibleModule(argument_spec={})
    # TEST 1: fsysopts doesn't exist
    network = HurdPfinetNetwork(module=module)
    network_facts = network.populate()
    assert network_facts == {}
    # TEST 2: socket doesn't exist
    module = AnsibleModule(argument_spec={})
    network = HurdPfinetNetwork(module=module)
    network._socket_dir = __file__
    network_facts = network.populate()
    assert network_facts == {}
    # TEST 3: fsysopts and socket exist
    module = AnsibleModule(argument_spec={})
    network = HurdPfinetNetwork(module=module)
    network._fsysopts_path = __file__
    network_facts = network.populate()
    assert network_facts

# Generated at 2022-06-13 01:38:55.057937
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    '''Test HurdPfinetNetwork.assign_network_facts()'''
    import shlex
    from subprocess import Popen, PIPE

    fsysopts = Popen(shlex.split('/bin/fsysopts -L /servers/socket/inet'), stdout=PIPE, stderr=PIPE)
    out, err = fsysopts.communicate()
    out = out.decode('utf-8')
    err = err.decode('utf-8')
    if fsysopts.returncode != 0:
        raise RuntimeError("Fail to run fsysopts: " + err)

    # XXX: we are assuming that the return value of fsysopts doesn't change

# Generated at 2022-06-13 01:38:57.663529
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    c = HurdNetworkCollector()
    assert c.platform == 'GNU'
    assert isinstance(c.fact_class, HurdPfinetNetwork)


# Generated at 2022-06-13 01:39:08.975684
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    from ansible.module_utils.facts.facts import Facts
    from ansible.module_utils.facts.network.hurd.pfinet import HurdPfinetNetwork
    from ansible.module_utils._text import to_bytes

    facts = Facts(dict())
    network = HurdPfinetNetwork(facts)
    network.module.run_command = lambda args, check_rc=True: (0, to_bytes('''\
--interface=eth0 --address=127.0.0.1 --netmask=255.0.0.0 --address6=fe80::7bda:e2ff:fe7d:5c5a/64
--interface=lo --address=127.0.0.1 --netmask=255.0.0.0 --address6=::1/128\
    '''), '')

# Generated at 2022-06-13 01:39:20.240407
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    class MockModule:
        def __init__(self):
            self.run_command = lambda args, check_rc=True: ([0, OUTPUT, ''], [''], [''])
    module = MockModule()
    network = HurdPfinetNetwork(module)
    result = network.assign_network_facts({}, 'fsysopts', '/servers/socket/inet')

# Generated at 2022-06-13 01:39:21.562584
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    obj = HurdNetworkCollector()
    assert obj.platform == 'GNU'

# Generated at 2022-06-13 01:39:28.698873
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    # Setup
    o = HurdPfinetNetwork(None)

    # Test
    # The provided fsysopts has output
    # --interface=eth0
    # --address=10.10.0.19
    # --netmask=255.255.255.0
    # --address6=fd00::1:2:3:4/64
    network_facts = o.assign_network_facts(
        {},
        os.path.join(os.path.dirname(__file__), 'fsysopts.py'),
        'toto'
    )

    # Assert
    assert 'interfaces' in network_facts
    assert network_facts['interfaces'] == ['eth0']

    assert 'eth0' in network_facts
    assert network_facts['eth0']['active']

# Generated at 2022-06-13 01:39:35.283694
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    from ansible.module_utils.facts.network.hurd_pfinet import HurdPfinetNetwork

    module = AnsibleModuleHelperMock(dict(
        ansible_facts=dict(),
        ansible_module_docker=dict(),
    ))
    module.run_command = run_command
    module.get_bin_path = get_bin_path

    hpn = HurdPfinetNetwork(module)

    hpn.populate()

# Generated at 2022-06-13 01:39:52.743983
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    from ansible.module_utils.facts.network.base import Platform
    from ansible.module_utils.facts.network.gnu.hurd import HurdPfinetNetwork
    from ansible.module_utils.facts.network.gnu.utils import FakeModule
    import io
    import sys

    # Manage diversity of Python version
    if sys.version_info[0] == 2:
        FileNotFoundError = OSError
    else:
        FileNotFoundError = FileNotFoundError

    class FakePlatform(Platform):
        def __init__(self, module, **kwargs):
            self.module = module
            self.facts = {}

        def get_device_name(self, iface):
            return iface

    class FakeFile:
        def __init__(self, content):
            self.content = content



# Generated at 2022-06-13 01:39:55.093860
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    hurd_network_collector = HurdNetworkCollector()
    # Check the constructor call
    assert hurd_network_collector

# Generated at 2022-06-13 01:39:56.373167
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    network = HurdPfinetNetwork(dict())
    assert network


# Generated at 2022-06-13 01:40:02.914510
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    class AnsibleModuleMock():
        def __init__(self, params, module_name):
            self.params = params
            self.module_name = module_name
            self.tmpdir = '/tmp'

        def get_bin_path(self, cmd):
            expected_cmd = ['fsysopts']
            return '/bin/' + cmd if cmd in expected_cmd else None

        def run_command(self, cmd):
            class ProcessResult():
                def __init__(self, stdout, stderr, rc):
                    self.stdout = stdout
                    self.stderr = stderr
                    self.rc = rc
            expected_cmd = ['/bin/fsysopts', '-L', '/servers/socket/inet']

# Generated at 2022-06-13 01:40:05.368055
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    module = NetworkCollector.get_network_module()
    return HurdNetworkCollector(module)

# Generated at 2022-06-13 01:40:06.943835
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    fact = dict()
    l = HurdPfinetNetwork(fact, dict(), dict())
    assert l._platform == 'GNU'
    assert l._fact_class == HurdPfinetNetwork


# Generated at 2022-06-13 01:40:15.511526
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    # FIXME: build a trivial module class for testing
    module = None


# Generated at 2022-06-13 01:40:22.250300
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )
    module.run_command = MagicMock(return_value=(0, 'version', ''))

    obj = HurdPfinetNetwork(module=module)
    # Try fsysopts not present
    obj.module.get_bin_path = MagicMock(return_value=None)
    network_facts = obj.populate()
    assert network_facts == {}

    # Try with fsysopts
    obj.module.get_bin_path = MagicMock(return_value='/bin/fsysopts')
    network_facts = obj.populate()

# Generated at 2022-06-13 01:40:28.756724
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    # FIXME: this is a placeholder unit test.
    # With the current refactoring it has been difficult to write a unit
    # test for this class without some mocking. I will work on this.
    module_path = os.path.join(os.path.dirname(__file__), '../../../../lib/ansible/module_utils/facts/network/hurd.py')
    os.system('PYTHONPATH=' + module_path + ' python -m ansible.module_utils.facts.network.hurd')
    return

# Generated at 2022-06-13 01:40:31.060024
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    class MockModule():
        def __init__(self):
            self.run_command = lambda *args, **kwargs: (256, '', 'ignore.py is not found or executable.')
            self.get_bin_path = lambda *args, **kwargs: None

    # Test constructor
    obj = HurdPfinetNetwork(MockModule())
    assert obj.platform == 'GNU'

# Generated at 2022-06-13 01:40:56.366642
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    # FIXME: global test setup
    # FIXME: test that it returns an empty hash when fsysopts doesn't exist
    # FIXME: test that it returns an empty hash when fsysopts exist but no /servers/socket/foo exists
    # FIXME: test that it returns an empty hash when fsysopts exist but no /servers/socket/foo is linked to neither inet nor inet6
    # FIXME: test that calling it when fsysopts exists and a link to inet or inet6 exists returns the expected result
    pass

# Generated at 2022-06-13 01:40:58.718311
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    mod = AnsibleModule({'module_utils': 'ansible.module_utils.basic'})
    mod.get_bin_path = lambda name: '/bin/' + name
    HurdPfinetNetwork(module=mod).populate()



# Generated at 2022-06-13 01:41:01.650647
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    ghn = HurdPfinetNetwork(None)
    assert ghn is not None
    assert ghn.platform == 'GNU'
    assert ghn._socket_dir == '/servers/socket/'


# Generated at 2022-06-13 01:41:04.558093
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    gnu_net = HurdPfinetNetwork({}, {}, {})
    assert gnu_net.platform == 'GNU'


# Generated at 2022-06-13 01:41:07.242114
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    '''Initialize a HurdPfinetNetwork object'''
    hp = HurdPfinetNetwork()
    assert hp
    assert hp.platform == 'GNU'


# Generated at 2022-06-13 01:41:17.282149
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    import sys
    if sys.version_info[0] == 2:
        import mock
        module = mock.Mock()
        module.run_command.return_value = (0, '--interface=/dev/eth0 --address=10.1.1.2 --netmask=255.255.255.0', '')
        fsysopt_path = '/bin/fsysopts'
        socket_path = '/servers/socket/inet'

        network = HurdPfinetNetwork(module)
        network_facts = {}
        network_facts = network.assign_network_facts(network_facts, fsysopt_path, socket_path)

        assert network_facts['interfaces'] == ['eth0']

# Generated at 2022-06-13 01:41:19.502634
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    n = HurdPfinetNetwork(None)
    assert (n.platform == 'GNU')
    assert (n._socket_dir == '/servers/socket/')

# Generated at 2022-06-13 01:41:21.513665
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    collector = HurdNetworkCollector()
    assert collector.__class__.__name__ == 'HurdNetworkCollector'
    assert collector._fact_class == HurdPfinetNetwork

# Generated at 2022-06-13 01:41:25.364568
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    assert HurdNetworkCollector().__class__.__name__ == 'HurdNetworkCollector'
    assert HurdNetworkCollector()._fact_class.__name__ == 'HurdPfinetNetwork'
    assert HurdNetworkCollector()._platform == 'GNU'


# Generated at 2022-06-13 01:41:34.168504
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    # Test without value
    mod = AnsibleModule(argument_spec={})
    collector = HurdNetworkCollector(mod)
    pfinet_network = collector.collect()[0]
    network_facts = {}
    network_facts = pfinet_network.assign_network_facts(network_facts, '/usr/bin/fsysopts', '/servers/socket/inet')

# Generated at 2022-06-13 01:42:16.706966
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    collector = HurdNetworkCollector()
    assert collector.platform == 'GNU'

# Generated at 2022-06-13 01:42:18.746665
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    collector = HurdNetworkCollector()
    assert collector._platform == 'GNU'
    assert collector._fact_class == HurdPfinetNetwork

# Generated at 2022-06-13 01:42:23.758861
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    # Create a `HurdPfinetNetwork` instance
    hurd_pfinet_network = HurdPfinetNetwork(None)
    # Return the list of `sysctl` commands from `NetworkCollector` instance
    assert isinstance(hurd_pfinet_network.commands(), dict)


# Generated at 2022-06-13 01:42:25.794019
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    assert HurdNetworkCollector._platform == 'GNU'
    assert HurdNetworkCollector._fact_class == HurdPfinetNetwork


# Generated at 2022-06-13 01:42:28.149898
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    network = HurdPfinetNetwork(None)
    assert network.platform == 'GNU'
    assert network._socket_dir == '/servers/socket/'


# Generated at 2022-06-13 01:42:30.048673
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    collector = HurdNetworkCollector()
    assert collector.fact_class._platform == HurdPfinetNetwork.platform
    assert collector.fact_class == HurdPfinetNetwork


# Generated at 2022-06-13 01:42:35.690115
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    hurdNetworkCollectorObj = HurdNetworkCollector()
    assert (hurdNetworkCollectorObj._platform == 'GNU')
    assert (hurdNetworkCollectorObj._fact_class == HurdPfinetNetwork)


# Generated at 2022-06-13 01:42:40.634249
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    test_module = FakeModule()
    test_network_facts = {}

    fsysopts_path = '/path/to/fsysopts'
    socket_path = '/path/to/socket1'
    test_module.run_command = [
        fsysopts_path,
        '-L',
        socket_path,
        'return_code=0',
        'stdout=--interface=/dev/eth0 --address=10.10.10.10 --netmask=255.255.255.0 --address6=fe80:1234::10/64',
        'stderr=',
    ]

    c = HurdPfinetNetwork(test_module)
    result = c.assign_network_facts(test_network_facts, fsysopts_path, socket_path)
    assert result

# Generated at 2022-06-13 01:42:52.543474
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    network = HurdPfinetNetwork()
    network.module.get_bin_path = lambda: None
    assert network.populate() == {}

    network.module.get_bin_path = lambda x: '/bin/fsysopts'
    network._socket_dir = 'tests/unit/module_utils/facts/network/hurd'

# Generated at 2022-06-13 01:42:55.840020
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    module = AnsibleModule(argument_spec={})
    network_facts = HurdPfinetNetwork(module)
    assert network_facts.platform == "GNU"
    assert network_facts._socket_dir == "/servers/socket/"

# Generated at 2022-06-13 01:44:37.494267
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    c = HurdNetworkCollector()
    assert c.platform == 'GNU'
    assert c._fact_class == HurdPfinetNetwork


# Generated at 2022-06-13 01:44:43.451228
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    m = {
        'run_command.return_value': (0, '', ''),
        'get_bin_path.return_value': '/path/to/fsysopts',
    }
    class M:
        def __init__(self, d):
            self.__dict__.update(d)
    m = M(m)

    # test constructor
    n = HurdPfinetNetwork(m)
    assert type(n) is HurdPfinetNetwork
    assert n.module == m



# Generated at 2022-06-13 01:44:47.328344
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    from ansible_collections.notstdlib.moveitallout.plugins.module_utils.facts.network.hurd import HurdPfinetNetwork

    assert HurdPfinetNetwork._socket_dir == '/servers/socket/'
    assert HurdPfinetNetwork.platform == 'GNU'

# Generated at 2022-06-13 01:44:55.893883
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    # It is important to import here because we want facts to run before
    from ansible.module_utils.facts.network.gnu_hurd import HurdPfinetNetwork

    network_facts = {}

# Generated at 2022-06-13 01:45:05.849716
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    facts = dict()
    facts['interfaces'] = []

    path = '-L'
    out = '/dev/eth0 --interface=/dev/eth0 --address=10.0.0.11 --netmask=255.255.255.0'
    fsysopts_path = '/bin/fsysopts'

    Hurd = HurdPfinetNetwork()

    Hurd.assign_network_facts(facts, fsysopts_path, path)


# Generated at 2022-06-13 01:45:15.646588
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    network_facts = {}
    network_facts['interfaces'] = []
    fsysopts_path = './tests/unit/module_utils/facts/network/pfinet/fsysopts'
    socket_path = './tests/unit/module_utils/facts/network/pfinet/socket'
    network_facts = HurdPfinetNetwork.assign_network_facts(None, network_facts, fsysopts_path, socket_path)
    assert len(network_facts) == 4

# Generated at 2022-06-13 01:45:26.608769
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    targets = [
        # network_facts, fsysopts_path, socket_path
        (
            {},
            'fsysopts',
            '/servers/socket/inet',
        ),
    ]

    for network_facts, fsysopts_path, socket_path in targets:
        module = MockModule()
        fact_class = HurdPfinetNetwork(module)
        module.run_command.return_value = (0, '--interface=/dev/eth0 --address=172.16.1.10 --netmask=255.255.255.0 --address6=fe80::5054:ff:fea5:7142/64', '')
        fact_class.assign_network_facts(network_facts, fsysopts_path, socket_path)
        module.run_command.assert_

# Generated at 2022-06-13 01:45:31.248935
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    # Required as it does not exists on a GNU Hurd system
    import __builtin__
    setattr(__builtin__, '__salt__', {})
    from ansible.module_utils.facts.network.hurd import HurdPfinetNetwork
    from ansible.module_utils.facts.network.base import Network

    network_collector = HurdPfinetNetwork(dict(module_mock_args='file_mock_args'))

    # Setup the expected results
    expected_network_facts = Network(dict(module_mock_args='file_mock_args'))
    expected_network_facts['interfaces'] = ['eth0', 'eth1']

# Generated at 2022-06-13 01:45:34.633408
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    x = HurdNetworkCollector()
    assert x.platform == 'GNU'
    assert x.fact_class == HurdPfinetNetwork
    assert x.fact_subclasses == {}
    assert x.network_providers == {}

# Generated at 2022-06-13 01:45:36.607178
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    mod = AnsibleModule(argument_spec={})
    collection = HurdPfinetNetwork(mod)

    assert collection._socket_dir == '/servers/socket/'