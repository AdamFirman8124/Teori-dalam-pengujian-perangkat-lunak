

# Generated at 2022-06-13 01:37:49.587454
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    c = HurdNetworkCollector()
    assert c._platform == 'GNU'
    assert c._fact_class == HurdPfinetNetwork

# Generated at 2022-06-13 01:37:51.881996
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    collector = HurdNetworkCollector()
    assert (collector is not None)
    assert (collector._platform == 'GNU')
    assert (collector._fact_class == HurdPfinetNetwork)

# Generated at 2022-06-13 01:37:53.123436
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    assert HurdPfinetNetwork(None).platform == 'GNU'

# Generated at 2022-06-13 01:37:57.570671
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    from ansible.module_utils.facts.network.gnu.hurd import HurdPfinetNetwork
    hurd_pfinet_network = HurdPfinetNetwork()
    assert isinstance(hurd_pfinet_network, HurdPfinetNetwork)


# Generated at 2022-06-13 01:38:05.115972
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    """
    Make sure that the constructor only accept the right class and the right platform
    """
    # Ensure the constructor only accept the right class
    try:
        HurdNetworkCollector(None)
    except TypeError:
        pass
    else:
        assert False, "Should not accept 'NoneType' object"

    # Ensure the constructor only accept the right platform
    try:
        HurdNetworkCollector(object())
    except ValueError:
        pass
    else:
        assert False, "Should not accept platform 'object'"

# Generated at 2022-06-13 01:38:07.168919
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    hn = HurdPfinetNetwork()
    assert hn.platform == 'GNU'

# Generated at 2022-06-13 01:38:10.584837
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    module = AnsibleModule(
        argument_spec = dict()
    )
    network_facts = HurdPfinetNetwork(module).populate()
    assert network_facts == expected_network_facts


# Generated at 2022-06-13 01:38:12.438939
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    assert HurdNetworkCollector._platform == 'GNU'
    assert HurdNetworkCollector._fact_class == HurdPfinetNetwork

# Generated at 2022-06-13 01:38:18.483903
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    import json
    from ansible.module_utils.facts.collector import MonolithicCollector
    from ansible.module_utils.facts.network.hurd.pfinet import HurdPfinetNetwork
    from ansible.module_utils.facts.network.hurd.pfinet import HurdNetworkCollector
    ###############################################
    c = MonolithicCollector()
    d = c.get_collected_facts()
    ###############################################
    HurdNetworkCollector.populate(d)
    ###############################################
    f = HurdNetworkCollector.get_sorted_collected_facts(d)
    ###############################################
    assert 'network' in f
    network_facts = json.loads(json.dumps(f['network'], indent=4, sort_keys=True))


# Generated at 2022-06-13 01:38:28.053248
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    class Module(object):
        def __init__(self, params):
            self.params = params

        def run_command(self, args):
            return (0, args[0] + '_' + os.path.basename(args[-1]) + '_out', '')

        def get_bin_path(self, program):
            return 'path'

    module = Module(params=None)
    network = HurdPfinetNetwork(module=module)

    network_facts = {
        'interfaces': []
    }

    network_facts = network.assign_network_facts(network_facts, 'path', '/servers/socket/inet')
    assert network_facts['interfaces'] == ['eth0', 'eth1']

# Generated at 2022-06-13 01:38:36.382605
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    n = HurdPfinetNetwork()
    assert n._platform == 'GNU'
    assert n._socket_dir == '/servers/socket/'


# Generated at 2022-06-13 01:38:45.270058
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_bytes
    module = AnsibleModule(argument_spec={})

    network_facts = {}
    fsysopts_path = '/hurd/pfinet'
    socket_path = '/servers/socket/inet'

    # test ipv6

# Generated at 2022-06-13 01:38:47.838992
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    collector = HurdNetworkCollector()
    assert collector._platform == 'GNU'
    assert collector._fact_class == HurdPfinetNetwork

# Generated at 2022-06-13 01:38:48.796811
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    assert HurdPfinetNetwork().populate() == {}

# Generated at 2022-06-13 01:38:49.536633
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    HurdNetworkCollector()
    HurdNetworkCollector()

# Generated at 2022-06-13 01:39:00.679265
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    module = FakeAnsibleModule()
    network_facts = HurdPfinetNetwork(module)

    # Default return value
    assert network_facts.populate() == {}

    # Return value when fsysopts is not found
    module.params['fsysopts_path'] = None
    assert network_facts.populate() == {}

    module.params['fsysopts_path'] = 'fsysopts'

    # Return value when no socket found
    module.params['socket_path'] = None
    assert network_facts.populate() == {}

    # Return value when socket exist
    module.params['socket_path'] = 'socket'

# Generated at 2022-06-13 01:39:02.894332
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    c = HurdPfinetNetwork(None)
    assert c.platform == 'GNU'
    # FIXME: add more unit tests


# Generated at 2022-06-13 01:39:13.399844
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    """
        Constructor of class HurdNetworkCollector.
    """
    from ansible.module_utils import basic
    from ansible.module_utils.facts import collect_facts
    from ansible.module_utils._text import to_bytes

    module = basic.AnsibleModule(
        argument_spec = dict(),
        supports_check_mode = False
    )

    def module_run_command(self):
        """
            Just to mock the module.run_command method.
        """
        stdout = to_bytes("""
            --interface=eth0
            --address=192.168.0.2
            --netmask=255.255.255.0
            --address6=2001:db8::100/64
        """)
        return (0, stdout, '')

    module.run_command = module

# Generated at 2022-06-13 01:39:15.170942
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    network = HurdPfinetNetwork({'module': 'test'})
    assert network

# Generated at 2022-06-13 01:39:24.541216
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    module = MockModule()
    module.run_command = Mock(return_value=(0, '--interface=/dev/eth0 --address=10.66.107.136 --netmask=255.255.254.0 --address6=fe80::250:56ff:fea7:dd2b/64 --address6=2001:470:20a1:13:250:56ff:fea7:dd2b/64', ''))
    network_facts = {}
    network = HurdPfinetNetwork(module)
    result = network.assign_network_facts(network_facts, '/bin/fsysopts', '/servers/socket/inet')

# Generated at 2022-06-13 01:39:41.504418
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    '''Unit test for method populate of class HurdPfinetNetwork'''
    from ansible.module_utils.facts import FactCollector
    from ansible.module_utils.facts.network.hurd_pfinet import HurdPfinetNetwork
    from ansible.module_utils.facts.network.hurd_pfinet import HurdNetworkCollector
    from ansible.module_utils.facts.network.base import Network
    from ansible.module_utils.facts.network.base import NetworkCollector
    from ansible.module_utils._text import to_bytes
    import os

    module = AnsibleModule()

    os.environ["PATH"] = "/bin:/usr/bin"

    test_class = HurdPfinetNetwork(module)
    result = test_class.populate()

# Generated at 2022-06-13 01:39:50.682725
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    module = AnsibleModuleMock()
    module.run_command = Mock(return_value=('0', """--interface=eth0 --address=192.168.0.1 --netmask=255.255.255.0""", ''))
    network = HurdPfinetNetwork()
    network.module = module
    network_facts = {}
    result = network.assign_network_facts(network_facts, '/bin/fsysopts', '/servers/socket/inet')
    assert result['interfaces'] == ['eth0']
    assert result['eth0']['ipv4']['address'] == '192.168.0.1'
    assert result['eth0']['ipv4']['netmask'] == '255.255.255.0'


# Generated at 2022-06-13 01:39:59.816908
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    module = FakeModule()
    facts = HurdPfinetNetwork(module)
    facts.module.get_bin_path.side_effect = None
    facts.module.get_bin_path.return_value = True
    facts.module.run_command.return_value = (0, '--interface=/dev/eth0 --address=192.168.0.1 --netmask=255.255.255.0 --address6=2001:db8::1/128', '')
    network_facts = facts.populate()

# Generated at 2022-06-13 01:40:10.612702
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    module = MockAnsibleModule()
    obj = HurdPfinetNetwork(module)
    test_data = "--interface=/dev/eth0 --address=192.168.1.1 --netmask=255.255.255.0 --address6=fd00::1/64 --address6=fd00::2/64"
    expected_if = {
        'active': True,
        'device': 'eth0',
        'ipv4': {'address': '192.168.1.1', 'netmask': '255.255.255.0'},
        'ipv6': [{'address': 'fd00::1', 'prefix': '64'}, {'address': 'fd00::2', 'prefix': '64'}]
    }

# Generated at 2022-06-13 01:40:15.107043
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    expected_fsysopts_path = "/home/vagrant/gnumach-1.7/./build/i686-pc-gnu/sbin/fsysopts"
    expected_socket_path = "/servers/socket/inet"
    expected_address = "10.0.2.15"
    expected_prefix = "24"
    expected_netmask = "255.255.255.0"
    expected_interfaces = ["eth0"]

    # Mocking of module.run_command
    class ModuleMock():
        def __init__(self, fsysopts_path, socket_path):
            self.fsysopts_path = fsysopts_path
            self.socket_path = socket_path

        def get_bin_path(self, executable, required=True):
            return self.fsys

# Generated at 2022-06-13 01:40:17.678100
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    """
    Construct HurdPfinetNetwork class and test its instance
    variables.
    """
    network = HurdPfinetNetwork({}, {})
    assert network._socket_dir == '/servers/socket/'

# Generated at 2022-06-13 01:40:18.970315
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    hurdpfinetnetwork = HurdPfinetNetwork(None)
    assert hurdpfinetnetwork


# Generated at 2022-06-13 01:40:20.496927
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    assert HurdNetworkCollector().platform == 'GNU'
    assert HurdNetworkCollector().fact_class == HurdPfinetNetwork


# Generated at 2022-06-13 01:40:21.170450
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    assert HurdPfinetNetwork()

# Generated at 2022-06-13 01:40:30.682623
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    network_facts = {}
    fsysopts_path = 'fsysopts'
    socket_path = 'servers/socket/inet'

    expected_result = {
        'interfaces': [u'eth0'],
        'eth0': {
            'active': True,
            'device': 'eth0',
            'ipv4': {
                'address': '192.168.0.2',
                'netmask': '240.0.0.0'
            },
            'ipv6': [
                {
                    'address': 'fe80::a55:38ff:fe4d:2c06',
                    'prefix': '64'
                }
            ]
        }
    }


# Generated at 2022-06-13 01:40:52.109018
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    assert HurdNetworkCollector._platform == 'GNU'
    assert HurdNetworkCollector._fact_class == HurdPfinetNetwork

# Generated at 2022-06-13 01:40:54.200698
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    dummy_module = DummyModule()
    with pytest.raises(NotImplementedError):
        HurdPfinetNetwork(dummy_module)


# Generated at 2022-06-13 01:40:55.289481
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    assert isinstance(HurdPfinetNetwork(), HurdPfinetNetwork)

# Generated at 2022-06-13 01:40:56.366754
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    # function name is test_ + {class name}
    assert 1

# Generated at 2022-06-13 01:41:02.332927
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    module_mock = AnsibleModule(argument_spec={})
    module_mock.run_command = run_command_mock
    network = HurdPfinetNetwork(module_mock)
    network_facts = {}
    network_facts = network.assign_network_facts(network_facts, 'fsysopts', '/servers/socket/inet6')
    assert network_facts['interfaces'][0] == 'eth0'
    assert network_facts['eth0']['active'] == True
    assert network_facts['eth0']['device'] == 'eth0'
    assert network_facts['eth0']['ipv4'] == {'address': '192.168.1.5', 'netmask': '255.255.255.0'}

# Generated at 2022-06-13 01:41:07.304655
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    '''Unit test for method populate of class HurdPfinetNetwork'''

    # Initialize an instance of class HurdPfinetNetwork
    obj = HurdPfinetNetwork(None)

    # Same as up to the class
    assert obj.populate() == {'interfaces': []}

# Generated at 2022-06-13 01:41:10.500057
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    obj = HurdNetworkCollector()
    assert obj._platform == "GNU"
    assert obj._fact_class == HurdPfinetNetwork


# Generated at 2022-06-13 01:41:11.684823
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    assert HurdPfinetNetwork


# Generated at 2022-06-13 01:41:20.533048
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    module = AnsibleModule(argument_spec={})
    module.run_command = mock.Mock(return_value=(0, "--interface=/dev/eth0 --address=127.0.0.1 --netmask=255.0.0.0 --address6=::1/128", ""))
    module.get_bin_path = mock.Mock(return_value='/bin/fsysopts')
    module.fail_json = mock.Mock()

    collector = HurdNetworkCollector(module=module)

    facts = collector.collect()
    assert 'interfaces' in facts
    assert facts['interfaces'] == ['eth0']
    assert 'eth0' in facts
    assert facts['eth0']['active'] == True
    assert facts['eth0']['device'] == 'eth0'

# Generated at 2022-06-13 01:41:25.181274
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    """
    Create an instance of HurdNetworkCollector
    """
    hurd_network_collector = HurdNetworkCollector()
    assert hurd_network_collector is not None
    assert hurd_network_collector._platform == 'GNU'
    assert hurd_network_collector._fact_class == HurdPfinetNetwork

# Unit tests for class HurdPfinetNetwork

# Generated at 2022-06-13 01:42:08.531745
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    assert HurdNetworkCollector._platform == 'GNU'
    assert HurdNetworkCollector._fact_class == HurdPfinetNetwork

# Generated at 2022-06-13 01:42:18.710795
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    from ansible.module_utils.facts import ansible_facts
    import unittest

    try:
        import test.support
    except ImportError:
        import test.support.__init__
        import test.support.test_module
        import test.support.test_module.test_builtin
    from test.support.test_module.test_builtin import AnsibleModule

    class FakeModule(AnsibleModule):
        def __init__(self, *args, **kwargs):

            def fake_run_command(args, *kwargs):
                if args[0] == '/foo/fsysopts':
                    return (0, '--interface=/dev/eth0 --address=10.0.0.5 --netmask=255.0.0.0', '')

# Generated at 2022-06-13 01:42:28.850218
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    module = AnsibleModule(argument_spec={})
    module._ansible_debug = True

    fsysopts_path = '/usr/bin/fsysopts'
    socket_path = '/servers/socket/inet'

    network_facts = {
        'interfaces': [],
        'all_ipv4_addresses': [],
        'all_ipv6_addresses': [],
        'default_ipv4': {},
        'local4': None,
        'local6': None,
        'gateway4': None,
        'gateway6': None
    }


# Generated at 2022-06-13 01:42:39.293186
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    test_class = HurdPfinetNetwork({})

    # testing with only one interface which has IPv4 and IPv6 address information
    real_return = test_class.assign_network_facts(
            {}, None, 'examples/fsysopts-output-1')
    # ipv4 address is a string
    assert(isinstance(real_return['en0']['ipv4']['address'], str))
    # ipv4 network is a string
    assert(isinstance(real_return['en0']['ipv4']['netmask'], str))
    # ipv6 address is a string
    assert(isinstance(real_return['en0']['ipv6'][0]['address'], str))
    # ipv6 prefix is a string

# Generated at 2022-06-13 01:42:43.774827
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    o = HurdPfinetNetwork()
    assert o.platform == 'GNU'
    assert o._socket_dir == '/servers/socket/'


# Generated at 2022-06-13 01:42:47.417542
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    """This function tests the constructor of HurdNetworkCollector class."""
    obj = HurdNetworkCollector()
    assert obj._platform == 'GNU'
    assert obj._fact_class == HurdPfinetNetwork



# Generated at 2022-06-13 01:42:49.994279
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    network = HurdNetworkCollector()
    assert network.platform == 'GNU'
    assert network._fact_class == HurdPfinetNetwork
    assert network.facts == {}

# Generated at 2022-06-13 01:42:51.265340
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    from ansible.module_utils.facts.network.gnu_hurd import HurdPfinetNetwork
    assert HurdPfinetNetwork.assign_network_facts(None, None, None) == {}

# Generated at 2022-06-13 01:42:55.594110
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    hnc = HurdNetworkCollector()
    assert hnc._platform == 'GNU'
    assert hnc._fact_class == HurdPfinetNetwork
    assert hnc.platform == 'GNU'
    assert hnc.fact_class == HurdPfinetNetwork

# Generated at 2022-06-13 01:42:58.822592
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    module = HurdNetworkCollector(None)

    # Test the correct platform is chosen
    assert module.platform == 'GNU'

# Generated at 2022-06-13 01:44:46.008032
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    """
    This unit test is testing the method assign_network_facts of the class
    HurdPfinetNetwork of module ansible.module_utils.facts.network.hurd
    """
    test_module = type('module', (object,), {})()
    test_module.run_command = lambda x, check_rc=True, close_fds=True: (0, 'pfinet --interface eth0 --address 10.0.1.1 --netmask 255.0.0.0', '')
    test_module.get_bin_path = lambda x: '/bin/fsysopts'
    test_network = HurdPfinetNetwork(test_module)
    test_interfaces = ['eth0']

# Generated at 2022-06-13 01:44:49.210942
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    from ansible.module_utils.facts.network.gnu.pfinet import HurdPfinetNetwork
    h = HurdPfinetNetwork()
    assert h.platform == 'GNU'

# Generated at 2022-06-13 01:44:52.992950
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    """
    Test the constructor of HurdNetworkCollector.

    It should return a instance of a class that is derived of NetworkCollector
    """
    obj = HurdNetworkCollector()

    assert obj is not None, 'Object is None'
    assert isinstance(obj, NetworkCollector), 'Object is instance of NetworkCollector'


# Generated at 2022-06-13 01:44:55.435506
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    collector = HurdNetworkCollector()

    # Assert that the collector is of class HurdNetworkCollector
    assert type(collector) == HurdNetworkCollector

    # Assert that the platform is GNU
    assert HurdNetworkCollector._platform == 'GNU'

    # Assert that the fact class is HurdPfinetNetwork
    assert HurdNetworkCollector._fact_class == HurdPfinetNetwork

# Generated at 2022-06-13 01:45:05.804170
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    """
    This method unit test the populate method of class HurdPfinetNetwork
    on GNU Hurd with pfinet
    """
    path_fsysopts = '/usr/bin/fsysopts'
    path_socket = '/servers/socket/inet'
    network_facts = {}
    network = HurdPfinetNetwork(None)
    network_facts = network.assign_network_facts(network_facts,
                                                 path_fsysopts,
                                                 path_socket)
    assert network_facts['interfaces'] == ['eth0']
    assert network_facts['eth0']['active'] is True
    assert network_facts['eth0']['device'] == 'eth0'

# Generated at 2022-06-13 01:45:15.646804
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    import json
    import sys
    import os

    class ModuleFake(object):
        def __init__(self):
            self.run_command_rc = 0
            self.run_command_out = ''
            self.run_command_err = ''
            self.run_command_calls = []

        def get_bin_path(self, *args, **kwargs):
            return './fsysopts'

        def run_command(self, args, *kwargs, **kwargs2):
            self.run_command_calls.append(args)
            return (self.run_command_rc, self.run_command_out,
                    self.run_command_err)


# Generated at 2022-06-13 01:45:17.446050
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    HurdPfinetNetwork()

# Generated at 2022-06-13 01:45:20.582617
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    '''
    Unit test for class HurdPfinetNetwork
    '''
    hurd_pfinet_network = HurdPfinetNetwork()
    assert hurd_pfinet_network.platform == 'GNU'

# Generated at 2022-06-13 01:45:31.523152
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    # This is a regression test, which verify that the HurdPfinetNetwork
    # subclass of Network works.

    # Create a fake module, which emulate the running of commands on the target
    # system.
    module = MockModule()

    # Create a instance of HurdPfinetNetwork.
    network_collector = HurdPfinetNetwork(module)

    # Simulate, that we run 'fsysopts' to get the network information.
    network_collector.module.run_command.return_value = (0, '--interface=eth0 --address=1.2.3.4 --netmask=255.255.0.0 --address6=2::2/64', '')

    # Call populate() on the instance of HurdPfinetNetwork.
    network_collector.populate()

    # Verify that fsys

# Generated at 2022-06-13 01:45:39.497355
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    os.environ["ANSIBLE_LIBRARY"] = os.path.dirname(__file__) + "/../library/network/"

    from ansible.module_utils.facts.network.hurd.pfinet.collector import HurdPfinetNetwork
    test_class = HurdPfinetNetwork("test_module")

    expected_network_facts = {
        'interfaces': ['eth0'],
        'eth0': {
            'active': True,
            'device': 'eth0',
            'ipv4': {'address': '192.168.0.10', 'netmask': '255.255.255.0'},
            'ipv6': [{'address': '2001:db8::10', 'prefix': '64'}],
        }
    }

    # Dummy run command func
