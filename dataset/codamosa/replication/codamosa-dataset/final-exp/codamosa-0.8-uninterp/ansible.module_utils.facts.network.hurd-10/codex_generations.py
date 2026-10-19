

# Generated at 2022-06-13 01:37:47.000186
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    obj = HurdNetworkCollector()
    assert obj.platform == 'GNU'
    assert obj._fact_class == HurdPfinetNetwork

# Generated at 2022-06-13 01:37:54.513258
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    """
    Test method assign_network_facts of HurdPfinetNetwork.
    """
    fake_module = FakeAnsibleModule(fsysopts_output="""
--interface=/dev/eth0 --address=10.0.0.1 --netmask=255.0.0.0 --address6=fe80::3c0:8fff:fea5:c2f0/64
--interface=/dev/eth1 --address=192.168.0.1 --netmask=255.255.255.0 --address6=fe80::3c0:8fff:fea6:c2f0/64
""")
    # fake_module.run_command return res, out, err
    HurdPfinetNetwork(fake_module).assign_network_facts({}, 'fsysopts', '/socket/inet')

# Generated at 2022-06-13 01:38:05.421564
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    """
    Test result of populate method of class HurdPfinetNetwork.

    :returns: None
    :rtype: None
    """
    # needed for unittest
    from ansible.module_utils.facts import ansible_module
    from ansible.module_utils.facts.network import HurdPfinetNetwork

    # create the object under test
    test_object = HurdPfinetNetwork()

    # missing dependency
    ansible_module.run_command = lambda x: (1, '', '')
    test_object.module = ansible_module
    test_result = test_object.populate()
    assert test_result == {}, "Failed to report failure correctly."

    # success

# Generated at 2022-06-13 01:38:15.080841
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    from ansible.module_utils.facts.network.gnu.hurd import HurdPfinetNetwork as test_class

    test_class.module = DummyAnsibleModule()
    test_class.module.run_command = get_run_command_mock()
    test_class.module.get_bin_path = get_bin_path_mock()

    # Setup test data
    test_class.module.run_command.return_code = 0
    test_class.module.run_command.return_value = '--interface=eth0 --address=192.168.1.1'
    test_class.module.get_bin_path.return_value = '/usr/bin'

    network_facts = {}
    socket_path = '/servers/socket/inet'


# Generated at 2022-06-13 01:38:25.720601
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    import tempfile

    temp_directory = tempfile.mkdtemp(prefix="ansible_collections_network_ansible_network_plugins_'modules_extras_network_facts_network_facts")
    print(temp_directory)

    open(os.path.join(temp_directory, 'pfinet'), 'w').close()
    os.symlink('/dev/pfinet', os.path.join(temp_directory, 'inet'))

    from ansible.module_utils.facts.network.hurd import HurdPfinetNetwork
    import ansible.module_utils.facts.network.base

    ansible.module_utils.facts.network.base.HAVE_FSYSOPTS = True


# Generated at 2022-06-13 01:38:31.505436
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    result = {'interfaces': []}
    network = HurdPfinetNetwork(None)
    result = network.assign_network_facts(result, 'fsysopts',
                                          '/servers/socket/inet')
    ifacename = result['interfaces'][0]
    interface = result[ifacename]

    assert result['interfaces']
    assert interface['active']
    assert interface['device']
    assert interface['ipv4']['address']
    assert interface['ipv4']['netmask']
    assert interface['ipv6']

# Generated at 2022-06-13 01:38:33.339896
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    h = HurdNetworkCollector()
    assert h._platform == 'GNU'
    assert h._fact_class == HurdPfinetNetwork


# Generated at 2022-06-13 01:38:43.569677
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    module = None
    network_facts = {}
    fsysopts_path = '/path/to/fsysopts'
    socket_path = '/path/to/socket'

    out = '--interface=/dev/eth0 --address=192.168.1.1 --netmask=255.255.255.0'
    rc = 0
    err = []
    hpn = HurdPfinetNetwork(module)
    network_facts = hpn.assign_network_facts(network_facts, fsysopts_path, socket_path)

# Generated at 2022-06-13 01:38:52.410520
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    """
    Test assign_network_facts method of class HurdPfinetNetwork
    """
    # Fake module
    module = type('AnsibleModule', (object,), {})
    module.run_command = lambda *args, **kwargs : [0, '', '']

    # Fake network fact
    network_facts = {
        'interfaces': [],
    }

    # Fake path
    fsysopts_path = ''
    socket_path = ''

    HurdPfinetNetwork(module).assign_network_facts(network_facts, fsysopts_path, socket_path)
    assert network_facts['interfaces'] == []

# Generated at 2022-06-13 01:38:53.781197
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    HurdNetworkCollector()

# Generated at 2022-06-13 01:39:08.975964
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    network_collector = HurdNetworkCollector()
    assert network_collector._fact_class == HurdPfinetNetwork
    assert network_collector._fact_class.platform == 'GNU'
    assert network_collector._collectors == [network_collector._fact_class]
    assert network_collector._platform == HurdPfinetNetwork.platform

# Generated at 2022-06-13 01:39:20.178139
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    faked_fsysopts_path = '/bin/fsysopts'
    faked_socket_path = '/servers/socket/inet'

    faked_module = None

    fakenet = HurdPfinetNetwork(faked_module)
    assert fakenet.module == None 

    assert fakenet.fsysopts_path == faked_fsysopts_path
    assert fakenet.socket_path == faked_socket_path

    # with specified argument
    fakenet = HurdPfinetNetwork(faked_module, fsysopts_path=faked_fsysopts_path, socket_path=faked_socket_path)
    assert fakenet.fsysopts_path == faked_fsysopts_path
    assert fakenet.socket_path == faked_socket_path



# Generated at 2022-06-13 01:39:27.142314
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    module = FakeModule()
    h = HurdPfinetNetwork(module)
    network_facts = h.assign_network_facts({}, 'fsysopts', '/servers/socket/inet')
    assert 'interfaces' in network_facts
    assert network_facts['interfaces'] == ['eth0']
    assert 'eth0' in network_facts
    assert 'lo' not in network_facts
    assert network_facts['eth0']['device'] == 'eth0'
    assert network_facts['eth0']['active'] is True
    assert 'ipv4' in network_facts['eth0']
    assert network_facts['eth0']['ipv4']['address'] == '192.168.1.2'
    assert network_facts['eth0']['ipv4']['netmask']

# Generated at 2022-06-13 01:39:30.328285
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    collected_facts = {}
    network_collector = HurdNetworkCollector(None, collected_facts)
    assert isinstance(network_collector, NetworkCollector)
    assert network_collector._platform == 'GNU'
    assert network_collector._fact_class == HurdPfinetNetwork


# Generated at 2022-06-13 01:39:36.308990
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    facts_mod = HurdPfinetNetwork(module=None)
    facts_mod.module.run_command = lambda x: (0, '', '')
    facts_mod.module.get_bin_path = lambda x: '/gnumach/fsysopts'
    network_facts = facts_mod.populate()
    assert network_facts['interfaces'] == ['eth0']
    assert network_facts['eth0']['ipv4']['address'] == '192.168.1.1'
    assert network_facts['eth0']['ipv4']['netmask'] == '255.255.255.0'
    assert network_facts['eth0']['ipv6'][0]['address'] == 'fe80::ba27:ebff:feb2:4a0b'

# Generated at 2022-06-13 01:39:37.844600
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    pfinet_network = HurdPfinetNetwork(None)
    assert pfinet_network.platform == 'GNU'



# Generated at 2022-06-13 01:39:39.889661
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    fnet = HurdPfinetNetwork(None)
    assert fnet.platform == 'GNU'


# Generated at 2022-06-13 01:39:49.147414
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    import sys
    import imp
    import os

    sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

    from ansible.module_utils.facts import Facts
    from ansible.module_utils.facts.system.base import BaseFactCollector

    # test path
    src_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    test_path = os.path.join(src_path, 'ansible-modules-extras/test/units/module_utils/facts/network/hurd')

    # read in the test data
    fsysopts_path = os.path.join(test_path, 'fsysopts')

# Generated at 2022-06-13 01:39:51.620195
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    obj = HurdPfinetNetwork()
    assert obj._platform == "GNU"
    assert obj._fact_class == HurdPfinetNetwork


# Generated at 2022-06-13 01:39:53.169859
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    network = HurdPfinetNetwork({}, ['/bin/false'])
    assert isinstance(network, Network)

# Generated at 2022-06-13 01:40:13.388171
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    module = FakeAnsibleModule()
    network = HurdPfinetNetwork(module)

    network.module.get_bin_path = lambda x: '/bin/' + x

    os.stat = lambda x: FakeStatResult()
    os.access = lambda x, y: True
    os.path.exists = lambda x: True

    os.listdir = lambda x: ('inet', 'inet6', 'unix')

    network.module.run_command = lambda x: (0,
                                            ' --interface=/dev/eth0 --address=10.0.0.1 --netmask=255.255.255.0 --address6=fe80::9ef5:f8ff:fe50:d5a5/64',
                                            '')

    interfaces = network.populate()
    assert interfaces['interfaces']

# Generated at 2022-06-13 01:40:17.271060
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    """
    Test HurdNetworkCollector constructor
    """
    network_collector = HurdNetworkCollector()
    assert network_collector._platform == 'GNU'
    assert network_collector._fact_class.platform == 'GNU'


# Generated at 2022-06-13 01:40:27.807530
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    from ansible.module_utils.facts.network.gnuhurd import HurdPfinetNetwork
    import random
    import string

    fsysopts_path = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(32)])
    socket_path = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(32)])

    test_HurdPfinetNetwork = HurdPfinetNetwork({'bin_path': {'fsysopts': fsysopts_path}})

    network_facts = {}

# Generated at 2022-06-13 01:40:29.639146
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    test_net = HurdNetworkCollector()
    assert test_net.__class__.__name__ == 'HurdNetworkCollector'

# Generated at 2022-06-13 01:40:40.729933
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    # Test empty network_facts
    network_facts = {}
    facts = HurdPfinetNetwork(None)
    network_facts = facts.assign_network_facts(network_facts, 'fsysopts', '/servers/socket/inet')
    ifaces = ['eth0', 'lo']
    assert set(network_facts['interfaces']) == set(ifaces)
    assert 'eth0' in network_facts
    assert 'lo' in network_facts
    assert network_facts['eth0']['device'] == 'eth0'
    assert network_facts['eth0']['ipv4']['address'] == '192.168.1.1'
    assert network_facts['eth0']['ipv4']['netmask'] == '255.255.255.0'

# Generated at 2022-06-13 01:40:42.072914
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    HurdPfinetNetwork = HurdPfinetNetwork()
    HurdPfinetNetwork.populate()

# Generated at 2022-06-13 01:40:46.841031
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    network_collector = HurdNetworkCollector()
    assert network_collector is not None
    assert network_collector._platform == 'GNU'
    assert network_collector._fact_class == HurdPfinetNetwork


# Generated at 2022-06-13 01:40:49.573095
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    facts = HurdNetworkCollector()
    assert facts.__class__.__name__ == "HurdNetworkCollector"
    assert facts._fact_class.__name__ == "HurdPfinetNetwork"

# Generated at 2022-06-13 01:40:57.424468
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    module = AnsibleModule({})
    fsysopts_path = module.get_bin_path('fsysopts')
    socket_path = '/servers/socket/inet'
    n = HurdPfinetNetwork(module)
    facts = n.assign_network_facts({}, fsysopts_path, socket_path)
    print(facts)
    assert facts['interfaces'] == ['eth0']
    assert facts['eth0']['active'] == True
    assert facts['eth0']['device'] == 'eth0'
    assert facts['eth0']['ipv4']['address'] == '192.168.1.2/32'
    assert facts['eth0']['ipv4']['netmask'] == '255.255.255.0'

# Generated at 2022-06-13 01:41:08.256419
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    # Dummy Module
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes

    class Module(object):
        def __init__(self, params):
            self.params = params
            self.run_command_args = []
            self.run_command_rc = 0
            self.run_command_stdout = ''
            self.run_command_stderr = ''

        def get_bin_path(self, arg, **kwargs):
            return '/bin/fsysopts'

        def run_command(self, args, **kwargs):
            self.run_command_args.append(args)
            return self.run_command_rc, to_bytes(self.run_command_stdout), ''


# Generated at 2022-06-13 01:41:28.814038
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.facts.collector.network import HurdPfinetNetwork

    class ModuleMock(object):
        def run_command(self, args, check_rc=True):
            if args[0] == 'fsysopts':
                return 0, '--interface=/dev/eth0 --address=192.168.1.1 --netmask=255.255.255.0 --address6=2001::1/64', ''
            else:
                raise Exception('Unknown command: %s' % ' '.join(args))

        def get_bin_path(self, arg):
            if arg == 'fsysopts':
                return '/bin/fsysopts'
            else:
                raise Exception('Unknown arg: %s' % arg)

   

# Generated at 2022-06-13 01:41:31.648919
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    collector = HurdNetworkCollector()
    assert collector._platform == 'GNU'
    assert collector._fact_class == HurdPfinetNetwork

# Generated at 2022-06-13 01:41:40.037810
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    # module is not instantiated
    collector_fixture = HurdNetworkCollector()
    # fact_class is not instantiated
    network_facts_fixture = HurdPfinetNetwork(collector_fixture.module)
    network_facts_fixture.fsysopts_path = '../../../t/unit/facts/fixtures/lib/ansible/module_utils/facts/network/fsysopts'
    network_facts_fixture._socket_dir = '../../../t/unit/facts/fixtures/servers/socket/'
    network_facts_fixture._socket_path = '../../../t/unit/facts/fixtures/servers/socket/inet'

    # hack a way to call a protected method

# Generated at 2022-06-13 01:41:42.643677
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    nc = HurdNetworkCollector()
    assert nc._platform == 'GNU'
    assert nc._fact_class == HurdPfinetNetwork

# Generated at 2022-06-13 01:41:45.477919
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    collector = HurdNetworkCollector()
    assert collector.platform == 'GNU'
    assert collector.fact_class == HurdPfinetNetwork
# # Unit test for populator of class HurdPfinetNetwork
# def test_HurdPfinetNetwork_populate():
#     pass

# Generated at 2022-06-13 01:41:46.665707
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    pass

# Generated at 2022-06-13 01:41:57.333283
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    module = AnsibleModule(
        argument_spec=dict(),
    )
    network = HurdPfinetNetwork({'module': module})

    out = '--interface=/dev/eth0 --address=192.168.0.1 --netmask=255.255.255.0 --address6=fe80::1/64'
    out += '--interface=/dev/eth1 --address=192.168.1.1 --netmask=255.255.255.0 --address6=fe80::1/64'
    network_facts = network.assign_network_facts({}, '/bin/true', '/dev/null')

# Generated at 2022-06-13 01:41:58.280936
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    hurd_nc = HurdNetworkCollector()

# Generated at 2022-06-13 01:42:00.687257
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    for x in ['HurdPfinetNetwork', 'HurdNetworkCollector']:
        assert x in globals(), 'Global variable %s not found' % x

# Generated at 2022-06-13 01:42:03.902164
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    _HurdNetworkCollector = HurdNetworkCollector()
    assert _HurdNetworkCollector.__class__.__name__ == 'HurdNetworkCollector'


# Generated at 2022-06-13 01:42:27.830807
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    hnc = HurdNetworkCollector()
    assert hnc.platform == 'GNU'

# Generated at 2022-06-13 01:42:33.458627
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts.collector import get_collector_instance

    module = basic.AnsibleModule(
        argument_spec={},
        supports_check_mode=True
    )

    def mock_run_command(cmd, run_kwargs):
        def clean(s):
            return s.replace('\r\n', '\n').replace('\r', '\n')


# Generated at 2022-06-13 01:42:34.634219
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    pfinet_network = HurdPfinetNetwork(dict())
    assert pfinet_network is not None


# Generated at 2022-06-13 01:42:35.556289
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    network = HurdPfinetNetwork()
    assert network

# Generated at 2022-06-13 01:42:37.638396
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    gnu_network = HurdPfinetNetwork(None)
    assert gnu_network.platform == 'GNU'


# Generated at 2022-06-13 01:42:43.001304
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    module = Mock()
    run_command = Mock()
    module.run_command = run_command
    module.run_command.return_value = (0, '--interface=eth0 --address=192.168.1.10 --netmask=255.255.255.0 --address6=2001:db8:0:1:1:1:1:1/64 --address6=2001:db8:0:1:1:1:1:2/64', '')
    network_facts = {
        'interfaces': [],
    }
    obj = HurdPfinetNetwork()
    obj.module = module
    obj.assign_network_facts(network_facts, 'test', 'test')


# Generated at 2022-06-13 01:42:53.177811
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    test_module = AnsibleModule(argument_spec={})
    test_network = HurdPfinetNetwork(module=test_module)

    facts = {
        'interfaces': [],
    }

    out = textwrap.dedent('''\
        --interface=/dev/eth0
        --address=192.168.33.10
        --netmask=255.255.255.0
        --address6=fe80::5054:ff:feac:ef04/64
        ''')

    test_network.assign_network_facts(facts, 'fsysopts', '/servers/socket/inet')


# Generated at 2022-06-13 01:42:54.760564
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    collector = HurdNetworkCollector()
    assert collector.fact_class == HurdPfinetNetwork

# Generated at 2022-06-13 01:43:00.777942
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    module = AnsibleModule(
        argument_spec={},
        supports_check_mode=True
    )

    fsysopts_path = 'fsysopts'
    socket_path = '/servers/socket'

    network_facts = {}
    network_facts['interfaces'] = []

    network = HurdPfinetNetwork(module)
    network.assign_network_facts(network_facts, fsysopts_path, socket_path)

# Generated at 2022-06-13 01:43:01.508232
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    assert HurdNetworkCollector._platform == 'GNU'

# Generated at 2022-06-13 01:43:51.051219
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts.network import Network as AnsibleNetwork
    from ansible.module_utils.facts.network.base import Network, NetworkCollector
    from ansible.module_utils.facts.network.pfinet import HurdPfinetNetwork
    from ansible.module_utils.facts.network.pfinet import HurdNetworkCollector
    fsysopts_path = '/bin/fsysopts'
    socket_path = '/servers/socket'
    test_network_facts = {
        'interfaces': [],
    }

# Generated at 2022-06-13 01:43:52.674991
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    hurd_network_collector = HurdNetworkCollector()
    assert HurdPfinetNetwork == hurd_network_collector._fact_class

# Generated at 2022-06-13 01:43:57.388817
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    """
    Test that a HurdNetworkCollector can be initialized.
    The class can not be used because it needs module_utils.basic.AnsibleModule.
    The initialized class is discarded quietly.
    :return:
    """
    try:
        HurdNetworkCollector(None)
    except Exception:
        assert False

# Generated at 2022-06-13 01:44:02.011773
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    '''HurdNetworkCollector'''
    x = HurdNetworkCollector()
    assert x.platform == 'GNU'
    assert issubclass(x.fact_class, HurdPfinetNetwork)
    assert x.fact_class.platform == 'GNU'


# Generated at 2022-06-13 01:44:07.866210
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    try:
        from ansible.module_utils.facts.network.gnu.hurd import HurdPfinetNetwork
    except ImportError:
        assert False, "Unable to import HurdPfinetNetwork from ansible.module_utils.facts.network.gnu.hurd"
    from ansible.module_utils.facts.network.gnu.hurd import HurdNetworkCollector
    from ansible.module_utils._text import to_bytes

    class FakeModule():
        def __init__(self):
            self.params = {}
            self.run_command = run_command_mock

        def fail_json(self, *args, **kwargs):
            assert False, "fail_json"


# Generated at 2022-06-13 01:44:18.265431
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    # Test1: populate with no result
    mod = AnsibleModule(argument_spec={}, supports_check_mode=False)
    mod.run_command = MagicMock(return_value=(0, '', ''))
    mod.get_bin_path = MagicMock(return_value=None)
    network = HurdPfinetNetwork(mod)
    assert network.populate() == {}

    # Test2: populate with one interface with ipv4
    mod = AnsibleModule(argument_spec={}, supports_check_mode=False)
    mod.run_command = MagicMock(return_value=(0, '--interface=/dev/eth0 --enable=yes --address=10.0.0.1 --netmask=255.255.255.0', ''))

# Generated at 2022-06-13 01:44:25.800219
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    """
    For now this test doesn't run on every platform since we use only GNU Hurd
    internal functions
    """
    from ansible.module_utils.facts import Collector

    class FakeModule(object):
        def run_command(self, command):
            return (0, 'foo', None)

        def get_bin_path(self, command):
            return None

    class FakeCollectedFacts(object):
        def __init__(self):
            self.kernel = 'GNU'

    module = FakeModule()
    collected_facts = FakeCollectedFacts()

    network_collector = HurdNetworkCollector(module, collected_facts)
    network_collector.populate()



# Generated at 2022-06-13 01:44:30.689113
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    fsysopts_path = '/pfinet/fsysopts'
    socket_path = '/servers/socket/inet'
    module = MockModule()

    module.run_command_values = [
        (0, '--interface=eth0 --address=127.0.0.1 --netmask=255.0.0.0 --address6=::1/128 --address6=fd00::1/64', ''),
    ]

    network = HurdPfinetNetwork(module)

    network_facts = network.assign_network_facts({}, fsysopts_path, socket_path)

    assert network_facts['interfaces'] == ['eth0']
    assert network_facts['eth0']['active'] is True

# Generated at 2022-06-13 01:44:33.064585
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    obj = HurdPfinetNetwork({'module': None})
    assert not obj is None, "Unable to create an instance of HurdPfinetNetwork"

# Generated at 2022-06-13 01:44:42.508400
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    from ansible.module_utils.facts.network.os.hurd_pfinet.facts import HurdPfinetNetwork
    from ansible.module_utils.facts import ansible_virtual_iface_fact
    from ansible.module_utils.facts import ansible_virtual_iface_default_ipv4_address_fact

    socket_dir = '/servers/socket/'

    def ip_v4(iface=ansible_virtual_iface_fact, address=ansible_virtual_iface_default_ipv4_address_fact):
        return {'address': address, 'netmask': '255.255.255.0'}

    def ip_v6(iface=ansible_virtual_iface_fact):
        return []


# Generated at 2022-06-13 01:46:40.079922
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    from ansible.module_utils.facts.network.gnu import HurdNetworkCollector
    facts = HurdNetworkCollector()
    assert isinstance(facts, HurdNetworkCollector)



# Generated at 2022-06-13 01:46:47.748156
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    """
    HurdPfinetNetwork - populate
    """
    from ansible.module_utils.facts import ModuleTestCase
    from ansible.module_utils.facts.network.hurd_pfinet import HurdPfinetNetwork
    from ansible.module_utils.facts.network.hurd_pfinet import HurdNetworkCollector

    module = ModuleTestCase('test', network_name='hurd_pfinet')

    network_collector = HurdNetworkCollector(module)
    # Test with no fsysopts path
    HurdPfinetNetwork.populate(network_collector, {})
    assert 'interfaces' not in network_collector.facts['ansible_network_resources']['hurd_pfinet']
    assert 'ansible_default_ipv4' not in network_collect

# Generated at 2022-06-13 01:46:49.810030
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    module = MockModule()
    obj = HurdPfinetNetwork(module)
    obj.populate({'kernel': 'GNU'})
    assert module.run_command.call_count == 1

# Generated at 2022-06-13 01:46:51.998798
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    test_module = AnsibleModule(argument_spec={})
    test_network = HurdPfinetNetwork(module=test_module)
    assert test_network.platform == 'GNU'
    assert test_network._socket_dir == '/servers/socket/'


# Generated at 2022-06-13 01:46:52.859511
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    """
    Constructor of class HurdNetworkCollector can be invoked.
    """
    HurdNetworkCollector()

# Generated at 2022-06-13 01:46:53.948700
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    network = HurdPfinetNetwork(None)
    assert network._socket_dir == '/servers/socket/'

# Generated at 2022-06-13 01:46:55.669628
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    from ansible.module_utils.facts.network.gnu import HurdPfinetNetwork
    h = HurdPfinetNetwork()
    assert h is not None


# Generated at 2022-06-13 01:47:02.911209
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    module = AnsibleModule(argument_spec={})
    module.params = {}
    module.exit_json = Mock()
    module.run_command = MagicMock()
    module.run_command.return_value = (0, "--interface=/dev/eth0 --address=10.0.2.15 --netmask=255.255.255.0", "")
    module.get_bin_path = MagicMock()
    module.get_bin_path.return_value = "/usr/bin/fsysopts"

    huh = HurdPfinetNetwork(module)
    facts = huh.populate()

# Generated at 2022-06-13 01:47:06.688568
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    facter_collector = HurdNetworkCollector()
    assert facter_collector.__class__.__name__ == 'HurdNetworkCollector'
    assert facter_collector._platform == 'GNU'
    assert facter_collector._fact_class == HurdPfinetNetwork

# Generated at 2022-06-13 01:47:11.609078
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    test = HurdPfinetNetwork({})
    test.module = get_module('/dev/eth0', 'address=127.0.0.1,netmask=255.255.255.0,address6=::1/64')
    test.assign_network_facts({}, test.module.get_bin_path('fsysopts'), '/servers/socket/inet')
    # FIXME: the rest needs to be implemented