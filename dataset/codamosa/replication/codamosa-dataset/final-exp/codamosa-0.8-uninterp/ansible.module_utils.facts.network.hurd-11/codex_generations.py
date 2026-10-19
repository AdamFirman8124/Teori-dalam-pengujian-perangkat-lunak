

# Generated at 2022-06-13 01:37:54.428445
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    # This method call the populate method of HurdPfinetNetwork class,
    # in order to verify that all conditions are respected, and return
    # an appropriate value
    #
    # Note that this test need a GNU Hurd system with pfinet
    # configured.

    # Why go through this? If we just instantiate a class directly, we
    # are missing out on some of the important logic in the
    # constructor that gets us the module object.  By going through the
    # collector, we can make sure that the class constructor runs as
    # intended.
    # Get the HurdPfinetNetwork object to have an instance of module
    network_facts = {}
    network_facts['ansible_facts'] = {'ansible_net_interfaces': []}
    collections_module = HurdNetworkCollector(module=None)
    network

# Generated at 2022-06-13 01:37:58.453452
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    from ansible.module_utils.facts import FactCollector

    fc = FactCollector()
    ansible_facts = fc.collect(module=None)
    fc = NetworkCollector(module=None)
    fc.populate(ansible_facts)
    # todo: add test for private_networks

# Generated at 2022-06-13 01:37:59.063482
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    pass

# Generated at 2022-06-13 01:37:59.664282
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    pass

# Generated at 2022-06-13 01:38:09.763122
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    class Module(object):
        def __init__(self, run_command):
            self.run_command = run_command

        def get_bin_path(self, *args, **kwargs):
            return args[0]

    class RunCommandMock(object):
        def __init__(self, socket_path):
            self.socket_path = socket_path

        def __call__(self, args, **kwargs):
            if args[0] == 'fsysopts':
                if args[3] == self.socket_path:
                    if self.socket_path == '/servers/socket/inet6':
                        return (0, '--interface=eth0 --address6=fce0::/64', '')

# Generated at 2022-06-13 01:38:11.265427
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    h = HurdPfinetNetwork({}, {}, {}, [], [])
    assert h.platform == 'GNU'
    assert h._socket_dir == '/servers/socket/'


# Generated at 2022-06-13 01:38:16.418151
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    module = FakeAnsibleModule()
    module.run_command = lambda c: (0, "--interface=foo --address=bar", "")
    network = HurdPfinetNetwork(module)
    facts = network.populate()
    assert facts == {
        'interfaces': ['foo'],
        'foo': {
            'active': True,
            'device': 'foo',
            'ipv4': {
                'address': 'bar',
            },
            'ipv6': [],
        },
    }


# Generated at 2022-06-13 01:38:26.885449
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    ipv4_foo = {'address': '1.2.3.4'}
    ipv6_foo = [{'address': 'fc00:fe11::1', 'prefix': '10'}]
    interfaces = ['foo']
    inet = os.path.join(HurdPfinetNetwork._socket_dir, 'inet')
    fsysopts_path = '/bin/fsysopts'
    out = ('--interface=/dev/foo --address=1.2.3.4 --netmask=255.255.0.0 '
           '--address6=fc00:fe11::1/10')
    rc = 0
    err = ''
    module_args = {'rc': rc, 'out': out, 'err': err}

# Generated at 2022-06-13 01:38:34.157540
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    import re
    from ansible.module_utils.facts.network.gnuhurd import HurdPfinetNetwork
    net = HurdPfinetNetwork({})

    nw_facts = {}
    nw_facts = net.assign_network_facts(nw_facts, 'fsysopts', '/servers/socket/inet')

    assert 'interfaces' in nw_facts
    assert 'lo' in nw_facts
    assert len(nw_facts['interfaces']) == 1
    assert nw_facts['interfaces'][0] == 'lo'

    # Check the enp0s3 interface too
    nw_facts = {}
    nw_facts = net.assign_network_facts(nw_facts, 'fsysopts', '/servers/socket/inet6')

    assert 'interfaces'

# Generated at 2022-06-13 01:38:34.755910
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    pass

# Generated at 2022-06-13 01:38:47.014674
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    module = AnsibleModuleMock()
    module.run_command = Mock()

    # mock for run_command function
    def run_command_mock_function(command, *args, **kwargs):
        # this is the output of fsysopts -L /servers/socket/inet
        if command[0].endswith('fsysopts'):
            if command[-1].endswith('/servers/socket/inet'):
                return 0, "--interface=eth0 --address=192.168.1.100 --netmask=255.255.255.0 --address6=fe80::a00:27ff:fe1b:e1cb/64", None
            else:
                return 0, "", None
        else:
            return 0, "", None

    module.run_command.side_effect

# Generated at 2022-06-13 01:38:47.655693
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    pass

# Generated at 2022-06-13 01:38:57.899146
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    module = AnsibleModule({})
    fsysopts_path = '/bin/fsysopts'
    socket_path = '/servers/socket/inet'

    network_facts = {}

    with open('modules/network/doc/hurd/fsysopts.stdout', 'r') as f:
        out = f.read()

    HurdPfinetNetwork(module).assign_network_facts(network_facts, fsysopts_path, socket_path)


# Generated at 2022-06-13 01:39:00.442211
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    a = HurdPfinetNetwork(None)

    assert(a)
    assert(a.platform == 'GNU')

# Generated at 2022-06-13 01:39:02.208885
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    """
    Check constructor of class HurdNetworkCollector
    """
    HurdNetworkCollector()

# Generated at 2022-06-13 01:39:12.877289
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    '''
    Test method HurdPfinetNetwork.populate
    '''

    # Test with no fsysopts
    m = MockModule()
    m.get_bin_path.return_value = None
    c = HurdNetworkCollector(m)
    c.facts = {'network': {}}
    c.gather(c.facts)
    assert c.facts['network']['interfaces'] == []

    # Test with fsysopts but no inet and no inet6
    m = MockModule()
    m.get_bin_path.return_value = '/bin/fsysopts'
    c = HurdNetworkCollector(m)
    c.facts = {'network': {}}
    c.gather(c.facts)
    assert c.facts['network']['interfaces']

# Generated at 2022-06-13 01:39:23.172694
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    """
    Constructor HurdPfinetNetwork object
    """
    module = None
    hurd_pfinet_network = HurdPfinetNetwork(module)

    assert hurd_pfinet_network.platform == 'GNU'

    # test assign_network_facts() method
    network_facts = {
        'all_ipv4_addresses': [],
        'all_ipv6_addresses': [],
        'default_ipv4': {},
        'default_ipv6': {},
        'interface_ip': {},
        'interfaces': [],
        'module_hw': True,
        'routing_options': [],
    }

    fsysopts_path = '/hurd/pfinet'
    socket_path = '/servers/socket/inet'

    network_

# Generated at 2022-06-13 01:39:24.117055
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    result = HurdNetworkCollector()
    assert result is not None

# Generated at 2022-06-13 01:39:25.076358
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    assert str(HurdPfinetNetwork())


# Generated at 2022-06-13 01:39:25.744932
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    HurdPfinetNetwork()

# Generated at 2022-06-13 01:39:41.868796
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    from ansible.module_utils.facts import facts
    from ansible.module_utils._text import to_bytes

    facts_instance = facts.Facts(module=MockAnsibleModule())
    hurd_pfinet_network = HurdPfinetNetwork(facts_instance)


# Generated at 2022-06-13 01:39:51.162040
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    import sys
    import tempfile

    # backup sys.stdout
    stdout = sys.stdout

    # create a temporary file
    fd, t = tempfile.mkstemp()

    # replace stdout with the temporary file
    os.dup2(fd, sys.stdout.fileno())

    # run the test
    x = HurdPfinetNetwork({})

    # create a mock fsysopts command
    x.module.run_command = lambda cmd: (0, '--interface=tcp --address=127.0.0.1 --netmask=255.255.255.0', '')

    # run the assign_network_facts method
    x.assign_network_facts({}, 'fsysopts', '/servers/socket/inet')

    # close the temporary file

# Generated at 2022-06-13 01:40:00.196648
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    import os
    import tempfile
    from ansible.module_utils.facts.network.base import Network as base
    from ansible.module_utils.facts.network.hurd import HurdPfinetNetwork

    # Create a HurdPfinetNetwork object
    network_obj = HurdPfinetNetwork(base())

    # Create a temporary directory and enter the directory
    temp_dir = tempfile.mkdtemp()
    os.chdir(temp_dir)

    # Mock the run_command method of the network_obj

# Generated at 2022-06-13 01:40:03.053906
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    network = HurdPfinetNetwork(None)
    assert network.platform == 'GNU'
    assert network._socket_dir == '/servers/socket/'

# Generated at 2022-06-13 01:40:07.498042
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    # Run test if we are on 'GNU' platform
    if os.uname()[0] == 'GNU':
        obj = HurdNetworkCollector()
        assert(obj._platform == 'GNU')
        assert(obj._fact_class == HurdPfinetNetwork)

# Generated at 2022-06-13 01:40:08.852545
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    assert HurdPfinetNetwork({}).platform == 'GNU'


# Generated at 2022-06-13 01:40:13.593448
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    from ansible.module_utils import basic

    facts = basic.AnsibleModule(argument_spec={}, supports_check_mode=True).exit_json()

    class TestAnsibleModule:
        def __init__(self, facts):
            self.params = {}
            self.facts = facts

        def fail_json(self, *args, **kwargs):
            raise Exception(kwargs["msg"])

        def get_bin_path(self, *args, **kwargs):
            return '/bin/fsysopts'


# Generated at 2022-06-13 01:40:20.963481
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    module = type('FakeModule', (object,), {
        'run_command': lambda *args, **kwargs: (0, '', ''),
        'get_bin_path': lambda self, arg: 'fsysopts',
    })
    module_obj = module()
    network = HurdPfinetNetwork(module_obj)
    collected_facts = {}

    network.populate(collected_facts)
    assert collected_facts['interfaces'] is not None
    assert len(collected_facts['interfaces']) > 0

    for i in collected_facts['interfaces']:
        assert collected_facts[i]['active'] is True
        assert collected_facts[i]['device'] is not None
        assert collected_facts[i]['ipv4'] is not None

# Generated at 2022-06-13 01:40:22.842455
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    h = HurdPfinetNetwork({})
    assert h.platform == 'GNU'

# Generated at 2022-06-13 01:40:32.135117
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    # create a module
    module = AnsibleModule(argument_spec={})

    # create a HurdPfinetNetwork
    networkFact = HurdPfinetNetwork(module)

    # create a test network_facts
    network_facts = {'interface': {}}

    # simulate a GNU/Hurd system, if the GNU/Hurd system doesn't have the interface
    # the populate method should return an empty dictionary
    # /servers/socket/inet doesn't exist
    assert networkFact.populate(network_facts) == {}

    # create /servers/socket/inet
    os.mkdir('/servers/socket')
    os.mkdir('/servers/socket/inet')

    # simulate a GNU/Hurd system, if the GNU/Hurd system doesn't have
    # the fsysopts the populate method should return

# Generated at 2022-06-13 01:40:53.545428
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    my_network = HurdPfinetNetwork()
    assert my_network.get_platform() == 'GNU'


# Generated at 2022-06-13 01:41:00.422704
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    import json

    module = AnsibleModule(argument_spec={})
    module.run_command = lambda args, check_rc=True: (0, '--interface=/dev/eth0 --address=192.168.1.2 --address6=2001::2/64', '')
    module.get_bin_path = lambda name, required=False: '/bin/' + name
    network_facts = HurdPfinetNetwork(module).populate()
    assert network_facts['interfaces'] == ['eth0']
    assert network_facts['eth0']['device'] == 'eth0'
    assert network_facts['eth0']['ipv4']['address'] == '192.168.1.2'
    assert network_facts['eth0']['ipv6'][0]['address'] == '2001::2'

# Generated at 2022-06-13 01:41:04.776094
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    # Without parameters
    net = HurdPfinetNetwork(None)
    assert net.platform == 'GNU'

    # With parameters
    module = None
    net = HurdPfinetNetwork(module)
    assert net.platform == 'GNU'


# Generated at 2022-06-13 01:41:15.302229
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    input = """--interface=eth1
--address=127.0.0.1
--netmask=255.0.0.0
--address6=fe80:1:2:3:4:5:6:7/64"""

    class TestModule(object):
        def run_command(args, check_rc=True):
            assert args == ['fsysopts', '-L', '/servers/socket/inet']
            return 0, input, ''

    class TestConfig(object):
        def __init__(self):
            self.module = TestModule()

    config = TestConfig()
    network = HurdPfinetNetwork(config)

    result = network.assign_network_facts({}, 'fsysopts', '/servers/socket/inet')

# Generated at 2022-06-13 01:41:17.489743
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    x = HurdPfinetNetwork()
    assert x.platform == 'GNU'
    assert x._socket_dir == '/servers/socket/'

# Generated at 2022-06-13 01:41:19.076995
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    j = HurdPfinetNetwork(dict(module=dict()))
    assert j is not None



# Generated at 2022-06-13 01:41:28.737183
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    from ansible.module_utils.facts.network.hurd import HurdPfinetNetwork
    from ansible.module_utils.facts.network.netinfo import NetworkInfo
    from ansible.module_utils.facts.network.hw import Interface
    from ansible.module_utils.facts.network.pfinet import PfinetNetwork

    network_facts = PfinetNetwork().populate()
    # change the platform to GNU
    network_facts['default_ipv4']['network'] = 'GNU'
    interface = network_facts['interfaces'][0]
    interface_info = network_facts[interface]
    fsysopts_path = '/hurd/fsysopts'
    socket_path = '/servers/socket/inet'
    # set the address to an ipv4, just to be sure that we

# Generated at 2022-06-13 01:41:31.274124
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    h = HurdNetworkCollector()
    assert isinstance(h, HurdNetworkCollector)

# Generated at 2022-06-13 01:41:39.621504
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    from ansible.module_utils.facts import Facts

    facts = Facts(dict(), dict())
    network_facts_collector = HurdNetworkCollector(facts, None)

    network_facts = network_facts_collector._get_network_facts()

    assert isinstance(network_facts, dict)

    assert 'interfaces' in network_facts
    assert isinstance(network_facts['interfaces'], list)

    for interface in network_facts['interfaces']:
        assert interface in network_facts
        assert isinstance(network_facts[interface], dict)
        assert 'device' in network_facts[interface]
        assert network_facts[interface]['device'] == interface
        assert 'active' in network_facts[interface]
        assert 'ipv4' in network_facts[interface]
        assert 'ipv6' in network

# Generated at 2022-06-13 01:41:44.671970
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    # Test HurdPfinetNetwork()
    module = AnsibleModule(argument_spec={}, supports_check_mode=True)
    network = HurdPfinetNetwork(module)
    assert network.module == module
    assert network.platform == 'GNU'
    assert network._socket_dir == '/servers/socket/'
    assert network.ipv4_interface_map == {}


# Generated at 2022-06-13 01:42:31.929855
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    from ansible.module_utils.six import StringIO
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(
        argument_spec={},
        supports_check_mode=False)

    network = HurdPfinetNetwork(module)

    fsysopts_path = 'fsysopts'
    socket_path = '/servers/socket/inet'

    old_stdout = module.sys_stdout
    module.sys_stdout = StringIO()
    network.assign_network_facts({}, fsysopts_path, socket_path)
    out = module.sys_stdout.getvalue().strip()
    module.sys_stdout = old_stdout

# Generated at 2022-06-13 01:42:34.877337
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    """
    This tests the constructor of class HurdNetworkCollector.
    """
    HurdNetworkCollector()

# Generated at 2022-06-13 01:42:36.223784
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    """Test HurdNetworkCollector constructor"""
    HurdNetworkCollector()

# Generated at 2022-06-13 01:42:41.075629
# Unit test for method populate of class HurdPfinetNetwork

# Generated at 2022-06-13 01:42:52.881758
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    from ansible.module_utils.facts import FactCollector
    from ansible.module_utils.facts.network.gnu import HurdNetworkCollector
    from ansible.module_utils._text import to_text
    from ansible.module_utils.six import PY3
    from ansible.module_utils.six.moves import StringIO
    from ansible.module_utils.six.moves import mock
    from ansible.module_utils.six.moves.urllib.error import URLError
    from ansible.module_utils.urls import open_url

    if PY3:
        BUILTIN_STR = 'builtins'
    else:
        BUILTIN_STR = '__builtin__'


# Generated at 2022-06-13 01:43:02.312369
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    network_facts = {}
    network = HurdPfinetNetwork(None)
    fsysopts_path = 'fsysopts'
    output = '--interface=/dev/eth0 --address=127.0.0.1 --netmask=255.0.0.0 --address6=::1/128'
    socket_path = '/servers/socket/inet'

    network_facts = network.assign_network_facts(
        network_facts, fsysopts_path, socket_path)
    assert network_facts['interfaces'] == ['eth0']

# Generated at 2022-06-13 01:43:11.859990
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    """
    Unit test to test the populate of HurdPfinetNetwork
    """
    from ansible.module_utils.facts import FactCollector
    from ansible.module_utils._text import to_bytes
    from io import StringIO
    from ansible.module_utils import basic
    import platform

    module = basic.AnsibleModule(arg_spec=dict())
    setattr(module, 'run_command', run_command_result)
    setattr(module, 'get_bin_path', lambda x, opt_dirs=None: fake_bin)
    setattr(module, '_debug', lambda msg, *args, **kwargs: debug(msg,
            *args, **kwargs))

    if platform.system() != 'GNU':
        return {}


# Generated at 2022-06-13 01:43:12.995785
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    obj = HurdPfinetNetwork()
    assert obj is not None


# Generated at 2022-06-13 01:43:18.043044
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    """
    This test is for constructor of class HurdNetworkCollector.
    """
    # Call method to test constructor
    hurd_network_collector = HurdNetworkCollector()
    # Assert value of variable is expected result
    assert hurd_network_collector._platform == 'GNU'
    assert hurd_network_collector._fact_class == HurdPfinetNetwork


# Generated at 2022-06-13 01:43:20.066406
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    hnc = HurdNetworkCollector()
    assert hnc._platform == 'GNU'


# Generated at 2022-06-13 01:45:15.567409
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    from ansible.module_utils.facts.network.hurd_pfinet import HurdPfinetNetwork

    FACT_NETWORK_MODULE_PATH = os.path.realpath(os.path.join(os.path.dirname(__file__), "../../../../../lib/ansible/module_utils/facts/network/hurd_pfinet.py"))

    network_module = imp.load_source('network', FACT_NETWORK_MODULE_PATH)

    class MockModule(object):
        def __init__(self):
            self.params = {}

    class MockFactCollector(object):
        def __init__(self):
            self.network_module = network_module
            self.fsysopts_path = '/hurd/fsysopts'

# Generated at 2022-06-13 01:45:26.565494
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    # mock_module must be imported this way to be able to be used with mock_command
    from ansible.module_utils.facts.network.hurd import HurdPfinetNetwork
    from ansible.module_utils.facts.network.base import Network
    from ansible.module_utils.facts.network.hurd import HurdNetworkCollector
    import ansible.module_utils.facts.network.base

    # init module and HurdPfinetNetwork class
    module = Network._init_module()
    network = HurdPfinetNetwork(module=module)

    # init HurdNetworkCollector class and set the _network class attribute
    collector = HurdNetworkCollector()
    collector._network = network

    # mock_command will be used to return a specific value from the fsysopts command
    # stdout and stderr

# Generated at 2022-06-13 01:45:31.288484
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    try:
        # Creating a class instance
        obj = HurdPfinetNetwork()
        # testing the first populate
        assert obj.populate() == {
            'interfaces': [],
        }
    except Exception as e:
        # Raise any unexpected exceptions
        raise e


# Generated at 2022-06-13 01:45:33.647192
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    assert HurdNetworkCollector.platform == 'GNU'
    assert HurdNetworkCollector._fact_class == HurdPfinetNetwork


# Generated at 2022-06-13 01:45:40.520889
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    module_mock = MockModule()
    fsysopts_path = os.path.join(os.path.dirname(__file__), 'fixtures', 'fsysopts_output')
    socket_path = '/servers/socket/inet6'

    # Get the output of GNU Hurd's fsysopts -L /servers/socket/inet6
    with open(fsysopts_path) as f:
        out = f.read()

    network_facts = {}
    network = HurdPfinetNetwork(module_mock)
    facts = network.assign_network_facts(network_facts, fsysopts_path, socket_path)
    assert facts['interfaces'] == ['eth0']
    assert facts['eth0']['active'] is True

# Generated at 2022-06-13 01:45:43.723448
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    hnc = HurdNetworkCollector()
    assert hnc.platform == 'GNU'
    assert hnc.fact_class == HurdPfinetNetwork


# Generated at 2022-06-13 01:45:50.982326
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    module = AnsibleModule(
        argument_spec={},
        supports_check_mode=True
    )
    ip = HurdPfinetNetwork(module)
    ip.populate()
    assert ip.facts ==  {
        'interfaces': ['lo'],
        'lo': {
            'active': True,
            'device': 'lo',
            'ipv4': {
                'address': '127.0.0.1',
                'netmask': '255.0.0.0',
            },
            'ipv6': [
                {
                    'address': '::1',
                    'prefix': '128',
                },
            ],
        },
    }

# Generated at 2022-06-13 01:45:55.598554
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    module = AnsibleModule(argument_spec={
        'collect_default_ipv4': dict(type='bool', default=True),
        'collect_default_ipv6': dict(type='bool', default=True),
        'filter': dict(type='list', default=[]),
    })

    network_facts = HurdPfinetNetwork(module)
    collected_facts = network_facts.populate()

    assert 'interfaces' in collected_facts
    assert isinstance(collected_facts['interfaces'], list)
    assert len(collected_facts['interfaces']) > 0

    for i in collected_facts['interfaces']:
        assert i in collected_facts
        assert 'ipv4' in collected_facts[i]
        assert 'ipv6' in collected_facts[i]

# Generated at 2022-06-13 01:45:58.792818
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    assert 'GNU' == HurdNetworkCollector._platform
    assert 'GNU' == HurdNetworkCollector().platform
    assert HurdPfinetNetwork == HurdNetworkCollector._fact_class


# Generated at 2022-06-13 01:46:00.113384
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    network = HurdPfinetNetwork(None)
    assert network
