

# Generated at 2022-06-13 01:37:54.311980
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    # first test if pfinet is loaded
    module = AnsibleModule(argument_spec={})
    network = HurdPfinetNetwork(module)
    module.run_command = MagicMock(return_value=(0, '', ''))
    module.get_bin_path = MagicMock(return_value=None)
    res = network.populate()
    # if pfinet is not loaded, return an empty dict
    assert res == {}

    # then test if fsysopts exists
    module = AnsibleModule(argument_spec={})
    network = HurdPfinetNetwork(module)
    module.run_command = MagicMock(return_value=(0, '', ''))
    module.get_bin_path = MagicMock(return_value=None)
    res = network.populate()
    #

# Generated at 2022-06-13 01:37:56.566822
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    # FIXME: the test would need a GNU Hurd system,
    #        but this module should work on GNU Hurd.
    assert True

# Generated at 2022-06-13 01:38:06.853317
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    module = FakeModule()
    module.run_command = FakeRunCommand()

    obj = HurdPfinetNetwork(module=module)

    fsysopts_path = '/path/to/fsysopts'
    socket_path = '/servers/socket/inet'

    network_facts = {}

    network_facts = obj.assign_network_facts(network_facts, fsysopts_path, socket_path)
    assert network_facts['interfaces'] == ['eth1', 'eth2']
    assert network_facts['eth1']['ipv4']['address'] == '10.0.0.5'
    assert network_facts['eth1']['ipv4']['netmask'] == '255.255.255.255'

# Generated at 2022-06-13 01:38:09.950684
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    o = HurdPfinetNetwork(None)
    assert o.platform == 'GNU'
    assert o._socket_dir == '/servers/socket/'


# Generated at 2022-06-13 01:38:17.315257
# Unit test for method assign_network_facts of class HurdPfinetNetwork

# Generated at 2022-06-13 01:38:20.308778
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    collector = HurdNetworkCollector()
    assert collector.platform == 'GNU'
    assert collector._fact_class == HurdPfinetNetwork

# Generated at 2022-06-13 01:38:29.394646
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    module = MagicMock()
    is_module_debug = False
    module.run_command = MagicMock(return_value=(0, '', ''))
    module.get_bin_path = MagicMock(return_value='fsysopts_path')

    network_facts = {}

    obj = HurdPfinetNetwork(module, is_module_debug)

    # run test 1
    obj.assign_network_facts(network_facts, 'fsysopts_path', '/servers/socket/inet')

# Generated at 2022-06-13 01:38:30.731098
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    """
    Constructor test
    """
    c = HurdNetworkCollector()



# Generated at 2022-06-13 01:38:34.149852
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    module = AnsibleModule(argument_spec={}, supports_check_mode=True)
    fact_class = HurdPfinetNetwork(module)
    assert fact_class.platform == 'GNU'

# Generated at 2022-06-13 01:38:39.349054
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    from ansible.module_utils.facts.network.apparmor import ApparmorNetwork
    from ansible.module_utils.facts.network.base import Network
    from ansible.module_utils.facts.network.gnu_hurd import HurdPfinetNetwork
    apparmor_test = ApparmorNetwork()
    HurdPfinetNetwork(apparmor_test)

# Generated at 2022-06-13 01:38:47.202266
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    network = HurdNetworkCollector()
    assert network.__class__.__name__ == 'HurdNetworkCollector'
    assert network._fact_class.__name__ == 'HurdPfinetNetwork'
    assert network._platform == 'GNU'

# Generated at 2022-06-13 01:38:51.957068
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    module = MagicMock()
    module.run_command = MagicMock()

    network = HurdPfinetNetwork(module)

    network.module.get_bin_path = MagicMock(return_value=None)
    network.populate()
    assert network._facts == {}

    network.module.get_bin_path = MagicMock(
        return_value='/hurd/fsysopts')

    fsysopts_output = (
        "--interface=/dev/eth0 --address=192.0.2.1 --netmask=255.255.255.0 "
        "--port=22 --address6=2001:db8:1::1/64 --address6=2001:db8:2::1/64"
    )

# Generated at 2022-06-13 01:39:03.477423
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    module = FakeModule()
    network_facts = {}
    fsysopts_path = 'fsysopts'
    socket_path = '/servers/socket/inet'
    network = HurdPfinetNetwork(module)

    network_facts = network.assign_network_facts(network_facts, fsysopts_path, socket_path)

    assert network_facts['interfaces'] == ['eth0', 'eth1']
    assert network_facts['eth0']['active'] == True
    assert network_facts['eth0']['device'] == 'eth0'
    assert network_facts['eth0']['ipv4']['address'] == '192.168.1.1'

# Generated at 2022-06-13 01:39:12.737137
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    module = FakeAnsibleModule()
    hurd_network = HurdPfinetNetwork(module)

    # test the return value
    network_facts = hurd_network.populate()
    ifaces = network_facts.pop('interfaces')
    assert network_facts == {}
    assert ifaces == ['eth0']

    # test fake_pfinet_fsysopts
    pfinet_network = HurdPfinetNetwork(module, 'fake_pfinet_fsysopts')
    network_facts = pfinet_network.populate()
    ifaces = network_facts.pop('interfaces')
    assert network_facts == {}
    assert ifaces == ['eth0', 'eth1']


# Generated at 2022-06-13 01:39:13.769050
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    assert HurdPfinetNetwork()


# Generated at 2022-06-13 01:39:23.836982
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    class MockModule(object):
        def run_command(self, command):
            return (0, '--interface=/dev/eth0 --address=10.0.2.15 --netmask=255.255.255.0 --broadcast=10.0.2.255 --gateway=10.0.2.2 --address6=fe80::a00:27ff:fe0d:8f32%/64 --address6=::/0 --gateway6=::', None)

        def get_bin_path(self, name):
            return '/bin/fsysopts'

    module = MockModule()

    class MockNetwork(object):
        def __init__(self, module):
            self.module = module

        def get_bin_path(self, name):
            return '/bin/fsysopts'


# Generated at 2022-06-13 01:39:32.147984
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    from ansible.module_utils.facts.network.hurd import HurdPfinetNetwork
    # create a module object for test
    module = AnsibleModule(
        argument_spec = dict(),
        supports_check_mode = False,
    )
    # set up class object
    network = HurdPfinetNetwork(module)
    # test run
    network_facts = dict()
    network_facts = network.assign_network_facts(network_facts, 'fsysopts', '/servers/socket/inet')
    # check result
    assert network_facts['interfaces'][0] == 'eth0'
    assert network_facts['eth0']['device'] == 'eth0'
    assert network_facts['eth0']['ipv4']['address'] == '192.168.2.15'


# Generated at 2022-06-13 01:39:33.170310
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    collector = HurdNetworkCollector()
    assert collector._platform == 'GNU'

# Generated at 2022-06-13 01:39:35.061989
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    pfinet = HurdPfinetNetwork(dict())
    assert pfinet.platform == 'GNU'
    assert pfinet._socket_dir == '/servers/socket/'


# Generated at 2022-06-13 01:39:39.320322
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    # Create a HurdNetworkCollector object
    Hurd_collector_obj = HurdNetworkCollector()

    assert Hurd_collector_obj is not None
    assert Hurd_collector_obj.platform == 'GNU'
    assert isinstance(Hurd_collector_obj.fact_class, HurdPfinetNetwork)


# Generated at 2022-06-13 01:39:58.956761
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    assert HurdPfinetNetwork(None).assign_network_facts(
        {}, 'fsysopts', '/servers/socket/inet') == \
        {'interfaces': ['eth0'],
         'eth0': {'active': True,
                  'device': 'eth0',
                  'ipv4': {'address': '192.168.1.12',
                           'netmask': '255.255.255.0'},
                  'ipv6': [{'address': '2002:f34e:f3c3:8:33c6:559a:4093:d67d',
                            'prefix': '64'}]}}

# Generated at 2022-06-13 01:40:02.544345
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    assert HurdPfinetNetwork.platform == 'GNU'

    # Check if _socket_dir is defined
    assert HurdPfinetNetwork._socket_dir is not None

# Generated at 2022-06-13 01:40:12.592630
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    module = MockAnsibleModule()
    module.run_command = Mock(return_value=[0, '--interface=/dev/eth0 --address=10.0.0.99 --netmask=255.255.255.0', ''])
    module.get_bin_path = Mock(return_value='/bin/fsysopts')

    network_facts = {}
    fsysopts_path = module.get_bin_path('fsysopts')

    network = HurdPfinetNetwork(module=module)
    network.assign_network_facts(network_facts, fsysopts_path, '/servers/socket/inet')


# Generated at 2022-06-13 01:40:23.471117
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    from ansible.module_utils.facts.network.pfinet.utils import (
        FakeFsysopts,
        FakeModule,
        FakeSubprocess,
    )

    test_socket_dir = '/servers/socket/'
    test_fsysopts = 'fsysopts'

    test_fake_module = FakeModule({
        'bin_path': {
            test_fsysopts: '/hurd/foobar',
        },
    })

    test_fake_fsysopts = FakeFsysopts([
        ['--interface=eth0', '--address=10.0.2.15', '--netmask=255.255.255.0',
         '--address6=fe80::a00:27ff:fe6b:1a02/64'],
    ])

    test_fake

# Generated at 2022-06-13 01:40:25.281993
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    network = HurdNetworkCollector()
    assert isinstance(network, HurdNetworkCollector)


# Generated at 2022-06-13 01:40:35.541744
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    module = FakeModule()
    # create a fake fsysopts binary
    fsysopts = FakeBin(
        # fake the run cmd method
        'run_command',
        # fake the return code
        0,
        # fake the output
        ' --interface=lo  --address=127.0.0.1  --netmask=255.0.0.0')
    module.add_bin('fsysopts', fsysopts)

    # create a fake fsysopts binary
    socket_path = FakePath(
        # fake its existence
        True,
        # fake the path
        '/servers/socket/inet')
    module.add_path('/servers/socket/inet', socket_path)

    # instantiate a HurdPfinetNetwork object
    network_facts = HurdPfinet

# Generated at 2022-06-13 01:40:37.791269
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    network_collector = HurdNetworkCollector()
    assert isinstance(network_collector, HurdNetworkCollector)

# Generated at 2022-06-13 01:40:40.110883
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    n = HurdPfinetNetwork(object)
    assert n.platform == 'GNU'
    assert n._socket_dir == '/servers/socket/'


# Generated at 2022-06-13 01:40:50.461491
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    # Test with a empty dict
    module = AnsibleModule({})
    module.get_bin_path = MagicMock(return_value='/bin/fsysopts')

    # output of fsysopts command on GNU Hurd
    fsysopts_output = '''
--interface=eth0 --address=192.168.56.101 --netmask=255.255.255.0 --address6=2001:0db8::8a2e:370:7333/64
'''

    mod_run_comm = MagicMock()
    mod_run_comm.return_value = (0, fsysopts_output, '')
    module.run_command = mod_run_comm

    n = HurdPfinetNetwork(module)
    facts = {}
    n.populate(facts)


# Generated at 2022-06-13 01:40:52.238912
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    collector = HurdNetworkCollector()
    assert collector.__class__.__name__ == 'HurdNetworkCollector'


# Generated at 2022-06-13 01:41:15.536353
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    HurdNetworkCollector()

# Generated at 2022-06-13 01:41:19.425436
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    NetworkCollectorTestFramework(HurdNetworkCollector)


if __name__ == '__main__':
    from ansible.module_utils.facts.network.common import NetworkCollectorTestFramework
    network_collector_test_framework = NetworkCollectorTestFramework(HurdNetworkCollector)
    network_collector_test_framework.run()

# Generated at 2022-06-13 01:41:26.325362
# Unit test for method populate of class HurdPfinetNetwork

# Generated at 2022-06-13 01:41:31.108176
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    """
    Unit test for constructor of class HurdNetworkCollector
    """
    collector = HurdNetworkCollector()
    assert collector.platform == collector._platform, 'platform should be GNU'
    assert collector._fact_class == HurdPfinetNetwork, '_fact_class should be HurdPfinetNetwork'



# Generated at 2022-06-13 01:41:39.410522
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    HurdPfinetNetwork.module = FakeAnsibleModule()
    fsysopts_path = '/bin/fsysopts'

    # test with inet
    HurdPfinetNetwork.module.run_command_results = [
        (0, '--interface=/dev/eth0 --address=10.0.0.1 --netmask=255.255.255.0 --address6=fe80::d4af:4bff:fe95:51ae/64', '')
    ]
    network_facts = {}
    HurdPfinetNetwork.assign_network_facts(network_facts, fsysopts_path, '/servers/socket/inet')

    assert network_facts['interfaces'][0] == 'eth0'
    assert network_facts['eth0']['active'] is True

# Generated at 2022-06-13 01:41:47.290281
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    import ast
    from ansible.module_utils.facts.network.hurd import HurdPfinetNetwork
    from ansible.module_utils.facts.network.base import Network

    class FakeModule(object):
        def __init__(self, *args, **kwargs):
            self.params = {}

        def fail_json(self, *args, **kwargs):
            pass

    class FakeNetwork(Network):
        def __init__(self, *args, **kwargs):
            self.module = FakeModule()

    network = HurdPfinetNetwork(FakeNetwork())

    network_facts = {}
    fsysopts_path = '/usr/bin/fsysopts'
    socket_path = '/servers/socket/inet'

# Generated at 2022-06-13 01:41:49.541543
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    hn = HurdNetworkCollector()
    assert hn is not None


# Generated at 2022-06-13 01:41:59.536250
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    import sys
    import json
    import tempfile
    import os.path
    import textwrap

    # mock of module class
    class Options:
        connection = 'local'
        module_path = None
        forks = 5
        become = None
        become_method = None
        become_user = None
        check = False
        diff = False
        remote_user = 'test_user'
        timeout = 10
        private_key_file = None
        remote_pass = None
        sudo_user = 'root'
        sudo = True
        verbosity = 3

    class ModuleResult:
        def __init__(self, rc, out, err):
            self.rc = rc
            self.stdout = out
            self.stderr = err

    class AnsibleModule:
        def __init__(self):
            self

# Generated at 2022-06-13 01:42:08.762919
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    def test_method(mocker):
        mocker.patch('ansible.module_utils.facts.network.gnu_hurd.HurdPfinetNetwork.run_command')

        _run_command = HurdPfinetNetwork.run_command
        _run_command.return_value = (0, '--somekey=value --interface=/dev/eth0 --address=10.0.0.1 --netmask=255.255.255.0 --address6=fe80::1/64 --address6=fe80::2/64', '')

        _network_facts = {}
        _fsysopts_path = '/bin/fsysopts'
        _socket_path = '/servers/socket/inet'


# Generated at 2022-06-13 01:42:11.547346
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    module = MockModule()
    obj = HurdPfinetNetwork(module)
    assert obj.platform == 'GNU'


# Generated at 2022-06-13 01:43:00.220065
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    obj = HurdNetworkCollector()
    assert obj.platform == 'GNU'
    assert obj.fact_class == HurdPfinetNetwork

# Generated at 2022-06-13 01:43:03.349663
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    module = None
    network = HurdPfinetNetwork(module)
    assert network
    assert network.platform == 'GNU'
    assert network._socket_dir == '/servers/socket/'


# Generated at 2022-06-13 01:43:12.692825
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    from ansible.module_utils.facts.network.collector import NetworkCollector

    nc = NetworkCollector()
    nc.network = HurdPfinetNetwork(nc)
    nc.network.module = MockModule(dict(
        run_command=run_command
    ))

    network_facts = nc._collect_network_facts('ignored')
    network_facts['interfaces'] = ['lo']
    network_facts['lo'] = {}
    network_facts['lo']['active'] = True
    network_facts['lo']['device'] = 'lo'
    network_facts['lo']['ipv4'] = {}
    network_facts['lo']['ipv4']['address'] = '127.0.0.1'

# Generated at 2022-06-13 01:43:15.073567
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    """
    This function unit test the constructor of class HurdNetworkCollector
    """
    fact_class = HurdNetworkCollector()
    assert fact_class._platform == 'GNU'
    assert fact_class._fact_class == HurdPfinetNetwork

# Generated at 2022-06-13 01:43:22.502459
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    from ansible.module_utils.facts.network.gnu.hurd.pfinet.collector import HurdPfinetNetwork
    assert HurdPfinetNetwork._socket_dir == '/servers/socket/'
    assert HurdPfinetNetwork.platform == 'GNU'
    assert HurdPfinetNetwork.__doc__  == "This is a GNU Hurd specific subclass of Network. It use fsysopts to\n    get the ip address and support only pfinet."

# Generated at 2022-06-13 01:43:31.609957
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    # skeleton module args
    module_args = dict(
        test='test',
    )
    # skeleton facts
    facts = dict(
        test='test',
    )

    hn = HurdPfinetNetwork(module_args=module_args, facts=facts)

    # check if fsysopts command is present
    assert hn.module.get_bin_path('fsysopts') != None

    # check if the socket directory is present
    assert os.path.exists('/servers/socket/inet')
    assert os.path.isdir('/servers/socket/inet')
    assert os.path.exists('/servers/socket/inet6')
    assert os.path.isdir('/servers/socket/inet6')

    # mockup subprocess.Popen to avoid real execution of the

# Generated at 2022-06-13 01:43:33.980239
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    # test empty constructor
    collector = HurdNetworkCollector()
    assert collector.platform == 'GNU'
    assert collector.fact_class == HurdPfinetNetwork


# Generated at 2022-06-13 01:43:37.211064
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    from ansible.module_utils import basic
    module = basic.AnsibleModule(argument_spec={})
    module.run_command = run_command_mock
    iface = HurdPfinetNetwork(module)
    # FIXME: test more of this method
    iface.assign_network_facts({}, '/bin/true', 'socket')


# Generated at 2022-06-13 01:43:39.269688
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    assert (HurdNetworkCollector._platform == 'GNU')
    assert (HurdNetworkCollector._fact_class == HurdPfinetNetwork)

# Generated at 2022-06-13 01:43:50.001556
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    class MockModule(object):
        def run_command(self, args):
            if args[-1] == '/servers/socket/inet':
                return 0, '--interface=/dev/eth0 --address=192.168.1.1 --netmask=255.255.255.0 --address6=2001::1/64', ''
            elif args[-1] == '/servers/socket/inet6':
                return 0, '--interface=/dev/eth1 --address6=2001::2/64', ''
            else:
                raise Exception("Unsupported argument %s" % args)

        def get_bin_path(self, path):
            return path

    module = MockModule()
    network_facts = {}

    n = HurdPfinetNetwork()
    n.module = module
    n.assign_network_

# Generated at 2022-06-13 01:45:58.602141
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    nm = HurdNetworkCollector()
    assert nm._platform == 'GNU'
    assert nm._fact_class == HurdPfinetNetwork

# Generated at 2022-06-13 01:46:01.106146
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    network = HurdPfinetNetwork()
    assert HurdPfinetNetwork.platform == 'GNU'
    assert HurdPfinetNetwork._socket_dir == '/servers/socket/'



# Generated at 2022-06-13 01:46:09.900371
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    network_facts = {}
    fsysopts_path = '/usr/bin/fsysopts'
    socket_path = '/servers/socket/inet'
    n = HurdPfinetNetwork(None)
    network_facts = n.assign_network_facts(network_facts, fsysopts_path, socket_path)
    assert 'interfaces' in network_facts
    assert network_facts['interfaces'] == ['eth0']
    assert 'eth0' in network_facts
    assert network_facts['eth0']['device'] == 'eth0'
    assert network_facts['eth0']['active'] is True
    assert 'ipv4' in network_facts['eth0']
    assert 'ipv6' in network_facts['eth0']

# Generated at 2022-06-13 01:46:11.185788
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    x = HurdPfinetNetwork(None)
    assert x is not None

# Generated at 2022-06-13 01:46:20.600726
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    from ansible.module_utils.facts.network import HurdPfinetNetwork
    from ansible_collections.ansible.community.plugins.module_utils.facts.network.tests.unit.utils.fake_module import FakeModule
    module = FakeModule()
    network = HurdPfinetNetwork(module=module)

    fsysopts_path = module.get_bin_path('fsysopts')
    socket_path = module.get_bin_path('inet')

    network_facts = module.params['network_facts'] = {}
    network_facts = network.assign_network_facts(network_facts, fsysopts_path, socket_path)


# Generated at 2022-06-13 01:46:25.173509
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    HurdPfinetNetwork.module = FakeAnsibleModule()
    HurdPfinetNetwork().module.run_command = FakeRun
    result = HurdPfinetNetwork().populate()
    assert result == {'interfaces': ['eth0'], 'eth0': {'active': True, 'device': 'eth0', 'ipv4': {'netmask': 'ffff:ffff:ffff::', 'address': 'fe80::20c:29ff:fe5f:ba15'}, 'ipv6': [{'prefix': '64', 'address': 'fe80::1'}]}}


# Generated at 2022-06-13 01:46:26.394634
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    h = HurdPfinetNetwork({})
    assert isinstance(h, HurdPfinetNetwork)

# Generated at 2022-06-13 01:46:35.148815
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    module = AnsibleModule(
        argument_spec = dict(),
    )
    module.run_command = Mock(return_value=('stdout', 'stderr'))
    module.get_bin_path = Mock(return_value='/path/to/fsysopts')
    net = HurdPfinetNetwork()
    net.module = module


# Generated at 2022-06-13 01:46:43.220874
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    class ModuleMock():
        def get_bin_path(self, _):
            return '/fsysopts'

        def run_command(self, _):
            return 0, '''--interface=/dev/eth0
                          --address=10.0.0.10
                          --netmask=255.255.255.0
                          --address6=fe80::ec4:7aff:fe7b:2d8e/64''', ''

    def module_faker(module):
        mod = ModuleMock()
        mod.params = module.params
        mod.run_command = module.run_command
        return mod

    network = HurdPfinetNetwork({'module': module_faker})
    result = network.populate()

    assert result['interfaces'] == ['eth0']

# Generated at 2022-06-13 01:46:50.151775
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    import ansible.module_utils.facts.network.hurd_pfinet as hp
    test_data = """--interface=eth0\n--address=10.0.0.1\n--netmask=255.255.255.0\n--address6=fe80::64:ff:fe:10:0/64\n--address6=2001:db8:0:0:2::1/64"""

    network_facts = {'interfaces': [], 'all_ipv4_addresses': [], 'all_ipv6_addresses': []}