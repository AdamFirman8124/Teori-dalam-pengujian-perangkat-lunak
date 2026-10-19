

# Generated at 2022-06-13 01:37:49.788574
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    obj = HurdPfinetNetwork({}, None)
    assert obj.platform == 'GNU', 'Platform should be GNU'
    assert obj._socket_dir == '/servers/socket/', 'Socket dir should be /servers/socket/'


# Generated at 2022-06-13 01:37:52.642097
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    network = HurdPfinetNetwork({})
    assert network
    assert network.platform == 'GNU'


# Generated at 2022-06-13 01:38:04.367858
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    # Fake network_facts
    network_facts = {
        'interfaces': [],
    }
    facts = HurdPfinetNetwork(dict())
    # create fake *fsysopts output for pfinet

# Generated at 2022-06-13 01:38:14.544382
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    from ansible.module_utils.facts import Facts

    network_facts = {}
    i = HurdPfinetNetwork(module=Facts())
    fsysopts_path = '/usr/bin/fsysopts'
    socket_path = '/servers/socket/'

    out = "--interface=/dev/eth1 --address=1.2.3.4 --address6=::1/64 --netmask=255.0.0.0"
    network_facts = i.assign_network_facts(network_facts, fsysopts_path, socket_path)

    assert network_facts['interfaces'] == ['eth1']
    assert network_facts['eth1']['device'] == 'eth1'

# Generated at 2022-06-13 01:38:25.554860
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    test_module = AnsibleModule(argument_spec={})

    test_obj = HurdPfinetNetwork(test_module)

    network_facts = NewModule({'interfaces': []})

    fsysopts_path = test_module.get_bin_path('fsysopts')
    socket_path = '/servers/socket/inet'


# Generated at 2022-06-13 01:38:33.274230
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    module = FakeAnsibleModule()
    network = HurdPfinetNetwork(module)

    network_facts = network.populate()

    assert network_facts['interfaces'] == ['eth0']

    iface = network_facts['eth0']
    assert iface['active']
    assert iface['device'] == 'eth0'

    ipv4 = iface['ipv4']
    assert ipv4['address'] == '10.0.3.15'
    assert ipv4['netmask'] == '255.255.255.0'

    ipv6 = iface['ipv6']
    assert ipv6[0]['address'] == 'fe80::a00:27ff:fe74:36d3'
    assert ipv6[0]['prefix'] == '64'

# Generated at 2022-06-13 01:38:38.025165
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():

    # Test using the HurdPfinetNetwork constructor directly
    from ansible.module_utils.facts.network.hurd.pfinet import HurdPfinetNetwork
    h = HurdPfinetNetwork(dict(module=object()))
    assert isinstance(h, HurdPfinetNetwork)

# Generated at 2022-06-13 01:38:46.018043
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    import os
    import tempfile
    """
    First, we create a socket file in a temporary directory
    """
    tmpdir = tempfile.mkdtemp()

# Generated at 2022-06-13 01:38:50.875195
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():

    # Mock class ansible.module_utils.facts.network.base.Network
    from ansible.module_utils.facts.network.base import Network

    class MockNetwork(Network):
        def __init__(self, module):
            return

    # Mock class ansible.module_utils.basic.AnsibleModule
    from ansible.module_utils.basic import AnsibleModule

    class MockAnsibleModule:
        def __init__(self, argspec):
            self.params = {}
            self.run_command_args = []
            self.run_command_rc = 0
            self.run_command_err = ''
            self.run_command_out = ''

        def get_bin_path(self, executable):
            if self.run_command_rc == 1:
                return None
            else:
                return

# Generated at 2022-06-13 01:39:02.209841
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    from ansible_collections.ansible.community.tests.unit.compat.mock import MagicMock

    module = MagicMock()
    network_facts = {}
    network = HurdPfinetNetwork(module)

    fsysopts_path = '/bin/fsysopts'
    socket_path = '/servers/socket'

# Generated at 2022-06-13 01:39:08.419875
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    pass

# Generated at 2022-06-13 01:39:10.144930
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    c = HurdNetworkCollector()
    assert c._fact_class == HurdPfinetNetwork


# Generated at 2022-06-13 01:39:21.212878
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    import os
    import os.path
    import sys
    module = sys.modules[__name__]
    module.module = module
    module.run_command = lambda cmd: [cmd[0], cmd[1], os.path.join(os.getcwd(), 'testdata', 'cmd_output')]

    network_facts = HurdPfinetNetwork(module).populate()
    assert network_facts['interfaces'] == ['eth0']
    assert network_facts['eth0']['active'] is True
    assert network_facts['eth0']['device'] == 'eth0'
    assert network_facts['eth0']['ipv4']['address'] == '10.11.12.13'

# Generated at 2022-06-13 01:39:27.654209
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    """
    :type pfinet: HurdPfinetNetwork
    """
    pfinet = HurdPfinetNetwork()


# Generated at 2022-06-13 01:39:32.633798
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    from ansible.module_utils.facts.collector import CollectedFacts

    #         CollectedFacts is defined in this file
    # pylint: disable=undefined-variable
    gnu_facts = CollectedFacts({'network_resources': {'Linux': [], 'Hurd': ['ipv4', 'ipv6']}})
    c = HurdNetworkCollector(gnu_facts, 'Hurd')  # pylint: disable=undefined-variable
    assert c.facts is gnu_facts



# Generated at 2022-06-13 01:39:40.571792
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    from ansible.module_utils.facts import ansible_collector
    from ansible.module_utils.facts.network import HurdPfinetNetwork

    net = HurdPfinetNetwork()
    fake_facts = ansible_collector.get_platform_facts()

    expected = {
        'device': 'eth0',
        'ipv4': {'address': '10.0.0.1', 'netmask': '255.255.0.0'},
        'ipv6': [{'address': 'fe80::e86d:f2ff:feaf:843e', 'prefix': '64'}],
        'active': True
    }


# Generated at 2022-06-13 01:39:42.666936
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    from ansible.module_utils.facts.network.hurd import HurdPfinetNetwork
    n = HurdPfinetNetwork(None)
    assert n.platform == 'GNU'
    assert n.collector == None
    assert n._socket_dir == '/servers/socket/'


# Generated at 2022-06-13 01:39:51.297717
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    class module:
        def __init__(self):
            self._fd = os.fdopen(os.open('/tmp/fsysopts', os.O_CREAT | os.O_RDWR, 0o600))
            self._fd.write('--interface=/dev/eth0\n')
            self._fd.write('--address=192.168.1.1\n')
            self._fd.write('--netmask=255.255.255.0\n')
            self._fd.flush()

        def run_command(self, command):
            return (0, '', '')

        def get_bin_path(self, command):
            return '/bin/true'

        def _fdopen(self, fd):
            return fd

    nf = HurdPfinetNetwork()

# Generated at 2022-06-13 01:40:00.290218
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    module = FakeAnsibleModule()
    module.run_command.return_value = (0, '--interface=/dev/tap_dv_1 --address=10.21.3.89 --netmask=255.255.255.0', None)
    fact_klass = HurdPfinetNetwork(module)
    fact_klass.populate()
    module.assert_has_calls([
        [('run_command', ['/bin/fsysopts', '-L', '/servers/socket/inet'], None)],
    ])
    assert module.exit_json.call_count == 1

# Generated at 2022-06-13 01:40:09.259004
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    module = FakeAnsibleModule()
    mod_path = 'ansible.module_utils.facts.network.gnu.pfinet'
    doc = ':option:`address` must be specified.'

    with patch('%s.HurdPfinetNetwork.__init__' % mod_path) as mock_init:
        mock_init.return_value = None
        obj = HurdPfinetNetwork(module)
        assert isinstance(obj, HurdPfinetNetwork) is True
        assert obj.platform == 'GNU'
        assert obj._socket_dir == '/servers/socket/'
        assert obj.module is module


# Generated at 2022-06-13 01:40:22.979018
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    # We can only check if the constructor works
    # because the methods are statically implemented
    # in the parent class
    assert HurdNetworkCollector()

# Generated at 2022-06-13 01:40:25.543665
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():

    obj = HurdNetworkCollector()
    assert obj._platform == 'GNU'
    assert obj._fact_class._socket_dir == '/servers/socket/'



# Generated at 2022-06-13 01:40:30.248918
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    module_name = 'ansible.module_utils.facts.network.hurd.pfinet.network'
    mocker_path = "ansible.module_utils.facts.network.hurd.pfinet.network.{0}.{1}"

    mocker = mocker_path.format('os', 'path')

    mocker_class = mocker.format('exists')
    with mocker_class as mocked_exists:
        mocked_exists.return_value = True

        m = mocker_path.format('subprocess', 'Popen')
        with m() as mocked_Popen:
            mocked_Popen.return_value.returncode = 0

# Generated at 2022-06-13 01:40:31.312620
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    HurdNetworkCollector()

# Generated at 2022-06-13 01:40:35.202055
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    system_cls = get_system_cls('Hurd')
    system = system_cls(dict())
    test_inst = system.get_network_class()(system)
    assert test_inst

# Generated at 2022-06-13 01:40:39.356936
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    # Check method populate with fsysopts available
    module = AnsibleModule(argument_spec={})
    network_collector = HurdNetworkCollector(module=module)
    network_collector._update_facts()
    # TODO: add assert


# Generated at 2022-06-13 01:40:49.487518
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    module = AnsibleModule(argument_spec={})
    network = HurdPfinetNetwork(module)
    network_facts = {}
    fsysopts_path = '/usr/bin/fsysopts'
    socket_path = '/servers/socket/inet'
    network_facts = network.assign_network_facts(network_facts, fsysopts_path, socket_path)
    assert len(network_facts['interfaces']) == 1
    assert 'eth0' in network_facts['interfaces']
    assert 'eth0' in network_facts
    assert 'ipv4' in network_facts['eth0']
    assert 'address' in network_facts['eth0']['ipv4']
    assert 'netmask' in network_facts['eth0']['ipv4']

# Generated at 2022-06-13 01:40:57.356524
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    from ansible.module_utils.facts.network import Network
    from ansible.module_utils.facts.network.base import NetworkCollector
    from ansible.module_utils.facts.network.gnu import HurdPfinetNetwork
    from ansible.module_utils.facts.network.gnu import HurdNetworkCollector

    class AnsibleModule:
        class params:
            fetch_all = True
        class return_values:
            ansible_facts = {'test': True}

        def __init__(self):
            self.params = self.params()
            self.return_values = self.return_values()

        def run_command(self, command):
            self.command = command
            return 0, '', ''


# Generated at 2022-06-13 01:40:58.600101
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    pass

# Generated at 2022-06-13 01:41:08.693280
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    module = AnsibleModule(argument_spec={})
    module.run_command = MagicMock(return_value=(0,
                                                 """--interface=eth0 --address=10.10.10.1 --netmask=255.255.255.0 --address6=fe80::5054:ff:fe2e:1a08/64""",
                                                 None))
    network_facts = HurdPfinetNetwork().populate(collected_facts=None)
    assert network_facts.get('all_ipv4_addresses') == []

# Generated at 2022-06-13 01:41:31.501161
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    n = HurdPfinetNetwork(None)
    assert n.platform == "GNU"

# Generated at 2022-06-13 01:41:39.869597
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    import mock
    from ansible.module_utils.facts.network import HurdPfinetNetwork
    from ansible.module_utils import basic
    Module = basic.AnsibleModule
    m = Module({})
    m.run_command = mock.MagicMock()
    m.run_command.return_value = (0, "--interface=/dev/eth0 --address=192.168.0.100 --netmask=255.255.255.0 --interface=/dev/eth1 --address6=de:ad:be:ef::5/64 --address6=de:ad:be:ef::6/64", "")
    n = HurdPfinetNetwork(m)

# Generated at 2022-06-13 01:41:42.609189
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    hnc = HurdNetworkCollector()
    assert hnc._platform == 'GNU'
    assert hnc._fact_class == HurdPfinetNetwork

# Generated at 2022-06-13 01:41:49.198085
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    module = MockHurdModule()

    test_network_facts = {
            'interfaces': [],
    }

    network = HurdPfinetNetwork(module)

    # Populate the network facts with some data from fsysopts
    out = (
        "--interface=/dev/eth0 --address=10.0.0.1 --netmask=255.255.255.0 "
        "--broadcast=10.0.0.255 --address6=fe80::216:3eff:fe1a:f001/64 "
        "--broadcast6=ff02::1:ff1a:f001 --address6=fe80::216:3eff:fe1a:f002/64 "
        "--broadcast6=ff02::1:ff1a:f002 ")
    network.assign_network_

# Generated at 2022-06-13 01:41:54.328682
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    # works with GNU_Hurd
    ansible_os_family = 'GNU'
    ansible_distribution = ''
    ansible_distribution_version = ''
    pfinet_network = HurdPfinetNetwork(ansible_os_family,
                                       ansible_distribution,
                                       ansible_distribution_version)
    # nothing to test for now
    assert True

# Generated at 2022-06-13 01:42:05.144996
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    from ansible.module_utils import basic
    m = basic.AnsibleModule(
        argument_spec={
            'network_facts': dict(type='dict')
        }
    )
    n = HurdPfinetNetwork(m)

    network_facts = {
        'interfaces': [],
        'localhost': {
            'active': True,
            'ipv4': {},
            'ipv6': []
        }
    }

    fsysopts_path = '/bin/fsysopts'
    socket_path = '/servers/socket/inet'


# Generated at 2022-06-13 01:42:06.335629
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    assert issubclass(HurdPfinetNetwork, Network)


# Generated at 2022-06-13 01:42:09.082333
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    assert HurdNetworkCollector()._platform == 'GNU'
    assert HurdNetworkCollector()._fact_class == HurdPfinetNetwork


# Generated at 2022-06-13 01:42:12.352193
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    net = HurdPfinetNetwork(None)
    assert net.platform == 'GNU'
    assert net._socket_dir == '/servers/socket/'

# Generated at 2022-06-13 01:42:19.668262
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    module = type('module', (object,), {
        'get_bin_path': lambda self, x: '/sbin/fsysopts',
        'run_command': lambda self, x: ('', '--interface=eth0 --address=127.0.0.1 --netmask=255.0.0.0', ''),
    })()
    collect = HurdPfinetNetwork(module)
    network_facts = collect.populate()
    assert network_facts['interfaces'][0] == 'eth0'
    assert network_facts['eth0']['ipv4']['address'] == '127.0.0.1'

# Generated at 2022-06-13 01:43:11.860100
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    from ansible.module_utils.facts.network.hurd import HurdPfinetNetwork
    m = AnsibleModuleStub()
    fsysopts_path = '/servers/socket/inet'
    h = HurdPfinetNetwork(m)
    h.module.run_command = lambda command: {
        1: (1, '', 'fsysopts: unknown option -L'),
        2: (0, '--interface=/dev/eth0 --address=192.168.1.1 --netmask=255.255.255.0 --address6=2001:db8::/64', ''),
    }.get(command[-1], (1, '', ''))
    n = h.populate()

# Generated at 2022-06-13 01:43:13.044720
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    instance = HurdPfinetNetwork()
    assert instance is not None
    assert not instance.facts

# Generated at 2022-06-13 01:43:15.173105
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    myfact = HurdNetworkCollector('facts.d')
    assert myfact._platform == 'GNU'
    assert myfact._fact_class == HurdPfinetNetwork


# Generated at 2022-06-13 01:43:26.136947
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    module = FakeAnsibleModule()

    def mock_run_command(args, check_rc=True, close_fds=True, executable=None, data=None, binary_data=False):
        if args == ['/boot/servers/pfinet.static']:
            return 0, '', ''
        elif args == ['/boot/servers/pfinet.static', '-L', '/servers/socket/inet']:
            return 0, '--interface=/dev/eth0 --address=192.168.1.10 --netmask=255.255.255.0 --address6=2001:db8::1/64', ''
        else:
            raise Exception('unknown run_command args: {}'.format(args))

    module.run_command = mock_run_command


# Generated at 2022-06-13 01:43:35.137217
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    module = MockModule()
    network = HurdPfinetNetwork(module)
    fsysopts_path = module.get_bin_path('fsysopts')
    if fsysopts_path is None:
        # On GNU/Hurd, we require fsysopts to be present
        print('fsysopts not found, skipping tests of HurdPfinetNetwork')
        return

    socket_path = '/servers/socket/inet'
    network_facts = {
        'default_ipv4': {},
        'default_ipv6': None,
        'interfaces': [],
    }
    network_facts = network.assign_network_facts(network_facts, fsysopts_path, socket_path)

    assert 'eth0' in network_facts['interfaces']

# Generated at 2022-06-13 01:43:38.903572
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    c = HurdNetworkCollector()
    assert c.platform == 'GNU'
    assert c._fact_class == HurdPfinetNetwork


# Generated at 2022-06-13 01:43:49.710306
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    # Required values for module arguments
    module_args = dict()

    # Init module
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )

    #Init network collector with mocked module
    collector = HurdNetworkCollector(module=module)
    #Get network facts from collector
    #network_facts = collector.collect()
    #Asserting values from network fact
    #assert 'interfaces' in network_facts
    #assert 'eth0' in network_facts['interfaces']
    #assert network_facts['eth0']['device'] == 'eth0'
    #assert network_facts['eth0']['ipv4']['address'] == '192.168.122.42'
    #assert network_facts['eth0']['ipv4'][

# Generated at 2022-06-13 01:43:52.754102
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    network_collector = HurdNetworkCollector()
    assert isinstance(network_collector._fact_class, HurdPfinetNetwork)
    assert network_collector._fact_class.platform == 'GNU'

# Generated at 2022-06-13 01:43:54.633409
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    obj = HurdNetworkCollector()
    assert obj.platform == 'GNU'
    assert obj.fact_class == HurdPfinetNetwork

# Generated at 2022-06-13 01:43:58.197291
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    x = HurdNetworkCollector()
    assert x._platform == 'GNU'
    assert isinstance(x._fact_class, HurdPfinetNetwork)

# Generated at 2022-06-13 01:45:55.441221
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    module = FakeModule()
    module.run_command = lambda *args, **kwargs: (0, '', '')
    network = HurdPfinetNetwork(module)
    module.get_bin_path = lambda *args, **kwargs: '/bin/fsysopts'
    assert network.populate() == {
        'interfaces': ['eth1'],
        'eth1': {
            'active': True,
            'device': 'eth1',
            'ipv4': {
                'address': '192.168.1.123',
                'netmask': '255.255.255.0',
            },
            'ipv6': [
                {
                    'address': '2001:db8::1',
                    'prefix': '64',
                },
            ],
        },
    }



# Generated at 2022-06-13 01:46:05.634753
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    # import the module under test
    from ansible.module_utils.facts.network.gnu_hurd import HurdPfinetNetwork

    # import needed arguments for the method under test
    from ansible.module_utils.facts.network.base import Network

    # create a instance of the class under test using the needed argument
    class_under_test = HurdPfinetNetwork(Network(None, None))

    # create input parameters and expected results
    network_facts = {}
    fsysopts_path = 'fsysopts_path'
    socket_path = 'socket_path'

    # create a mock object for the used method run_command of class ansible.module_utils.common.run_command
    class run_command_mock(object):

        def __init__(self):
            pass


# Generated at 2022-06-13 01:46:11.705174
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    from ansible_collections.ansible.community.tests.unit.compat import unittest
    import collections
    from ansible.module_utils.facts.network.gnu_hurd import HurdPfinetNetwork
    from ansible.module_utils.facts.network.base import Network
    from ansible.module_utils._text import to_text

    # This test requires python 2.7 for unittest.mock
    if not hasattr(unittest, 'mock'):
        reason = 'Requires python 2.7 or newer'
        raise unittest.SkipTest(reason)

    # tests
    network = HurdPfinetNetwork(None, {})


# Generated at 2022-06-13 01:46:16.087538
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    '''
    Unit test for method populate of class HurdPfinetNetwork
    '''

    # Create a stub module to use in the test case
    import ansible.module_utils.facts.network.gnu.hurd.pfinet as target
    module = type('ModuleStub', (object,), {})()
    module.run_command = lambda x, check_rc=True: (0, "--interface=/dev/eth0=eth0 --address=10.0.0.1 --netmask=255.255.0.0 --address6=2001:db8:0:1:1:1:1:1/64", "")

    # Create an HurdPfinetNetwork object
    hpnet = target.HurdPfinetNetwork(module)

    # Call the populate method address
    network_facts = hpnet.pop

# Generated at 2022-06-13 01:46:23.051224
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    import sys

    if sys.version_info < (2, 7):
        import unittest2 as unittest
    else:
        import unittest
    from ansible.module_utils.facts.network.gnu.pfinet import HurdPfinetNetwork


# Generated at 2022-06-13 01:46:29.887193
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )

    m_run_command = MagicMock(return_value=(0, "--interface=/dev/eth0 --address=127.0.0.1 --netmask=255.0.0.0 --address6=2001:123:45::1/64", ""))
    m_get_bin_path = MagicMock(return_value="/bin/fsysopts")
    module.run_command = m_run_command
    module.get_bin_path = m_get_bin_path

    hpn = HurdPfinetNetwork(module)
    hpn.populate()

    assert hpn.facts['interfaces'] == ['eth0']

# Generated at 2022-06-13 01:46:31.276383
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    assert HurdPfinetNetwork(None)._socket_dir == '/servers/socket/'

# Generated at 2022-06-13 01:46:40.045468
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    class TestClass:
        def __init__(self):
            self.run_command_list = []
            self.out_command_list = []
            self.out_command_list_idx = 0
            self.err_command_list = []
            self.rc_list = []
            self.rc_list_idx = 0
            self.run_command_idx = 0

        def run_command(self, command):
            rc = self.rc_list[self.rc_list_idx]
            self.rc_list_idx = self.rc_list_idx + 1
            if rc == 0:
                out = self.out_command_list[self.out_command_list_idx]
                if out is not None:
                    out = out.encode('UTF-8')
                self

# Generated at 2022-06-13 01:46:47.714023
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    (rc, out, err) = (0,
    '--interface=/dev/eth0 --address=172.17.0.2 --netmask=255.255.0.0 --address6=fe80::42:acff:fe11:2/64',
    '')
    test_module = AnsibleModule(argument_spec={})
    test_module.run_command = lambda *args, **kwargs: (rc, out, err)
    test_module.check_mode = False
    test_module.no_log = False
    test_class = HurdPfinetNetwork(module=test_module)
    network_facts = {}
    result = test_class.assign_network_facts(network_facts, '/sbin/fsysopts', 'dummy_path')

# Generated at 2022-06-13 01:46:53.945890
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    from ansible.module_utils.facts.network.gnu_hurd.subprocess_helper import ModuleTestCase, ModuleHelper, \
        MockProcess, MockProcessHelper

    class TestHurdPfinetNetwork(HurdPfinetNetwork):

        def __init__(self, module):
            super(TestHurdPfinetNetwork, self).__init__(module)

        def assign_network_facts(self, network_facts, fsysopts_path, socket_path):
            return super(TestHurdPfinetNetwork, self).assign_network_facts(network_facts, fsysopts_path, socket_path)

        def ensure_dir(self, path):
            # Do nothing
            return
