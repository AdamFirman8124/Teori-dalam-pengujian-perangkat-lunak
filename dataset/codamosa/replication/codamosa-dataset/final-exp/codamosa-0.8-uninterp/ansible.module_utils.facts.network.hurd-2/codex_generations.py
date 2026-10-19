

# Generated at 2022-06-13 01:37:51.865674
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    from ansible.module_utils.facts.network.gnu import HurdPfinetNetwork
    network = HurdPfinetNetwork()
    assert network is not None

# Generated at 2022-06-13 01:38:03.545501
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    module = None
    network_facts = {}

    fsysopts_path = "fsysopts"
    socket_path = "/servers/socket/inet"

    test_object = HurdPfinetNetwork(module)

    fsysopts_out = """--address=10.0.0.4 --netmask=255.0.0.0 --interface=/dev/eth0 --broadcast=10.255.255.255 --address6=fe80::a00:27ff:febb:f25a/64 --address6=::1/128"""
    test_object.module.run_command = lambda x: (0, fsysopts_out, "")


# Generated at 2022-06-13 01:38:06.769238
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    collector = HurdNetworkCollector()
    assert collector._platform == 'GNU'
    assert collector._fact_class == HurdPfinetNetwork

# Generated at 2022-06-13 01:38:15.764929
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    Module = type('Module', (object,), {'run_command':
                                        lambda self, cmd: (0, '', '')})
    module = Module()

    fact = HurdPfinetNetwork(module)

# Generated at 2022-06-13 01:38:22.406500
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    class MockModule(object):
        def __init__(self):
            self.run_command = lambda x: ('', '', '')
            self.get_bin_path = lambda x: '/usr/bin/fsysopts'

    module = MockModule()
    network = HurdPfinetNetwork(module)

    assert network.platform == 'GNU'
    assert network._fact_class == HurdPfinetNetwork
    assert network._socket_dir == '/servers/socket/'

# Generated at 2022-06-13 01:38:31.023013
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    import sys

    from ansible.module_utils.facts.network.gnu.hurd import HurdPfinetNetwork

    class FakeModule(object):
        def __init__(self):
            self.run_command = lambda x, check_rc=None: (0, '--address=192.168.1.10 --netmask=255.255.255.0', '')

    class FakeFacts(object):
        def __init__(self):
            self.network_collector = HurdPfinetNetwork(self)

    fake_module = FakeModule()
    fake_facts = FakeFacts()
    fake_facts.network_collector.module = fake_module

    # Python2

# Generated at 2022-06-13 01:38:41.873855
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    class Module:
        def __init__(self):
            self.run_command_called = False
            self.params = None
        def run_command(self, cmd, check_rc=False):
            self.run_command_called = True
            self.params = cmd
            return 0, '', ''

    class FakeSocket:
        def __init__(self, name='socket_name'):
            self.name = name

    def FakeExists(ios):
        return True

    def FakeLstat(ios):
        return [None] * len(ios)

    def FakeListdir(ios):
        return [FakeSocket(s) for s in ios]

    module = Module()
    module.get_bin_path = lambda x: 'bin_path'
    module.get_platform = lambda: 'platform'
   

# Generated at 2022-06-13 01:38:54.673121
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    from ansible.module_utils import basic
    from ansible.module_utils.facts import q_fact
    from ansible.module_utils.facts.network.hurd import HurdPfinetNetwork
    from ansible.module_utils.six import PY2, PY3
    from ansible.module_utils._text import to_bytes, to_text

    class FakeModule(object):
        def __init__(self, out):
            self.out = out.split(os.linesep)

        def run_command(self, cmd):
            return 0, self.out, ""

        def get_bin_path(self, cmd):
            return "/bin/" + cmd

    network_facts = {}

    # Use the mock to return a string (Python 3) or a byte string (Python 2)

# Generated at 2022-06-13 01:39:05.728815
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    import ansible.module_utils.facts.network.gnu
    test_module = ansible.module_utils.facts.network.gnu.HurdPfinetNetwork(module=None)
    network_facts = {}
    test_module.assign_network_facts(network_facts, '/tmp/fsysopts', '/tmp/socket_path')
    assert len(network_facts['interfaces']) == 2
    assert network_facts['interfaces'][0] == 'eth0'
    assert network_facts['interfaces'][1] == 'lo'
    assert network_facts['eth0']['ipv4']['address'] == '10.0.2.15'
    assert network_facts['eth0']['ipv4']['netmask'] == '255.255.255.0'

# Generated at 2022-06-13 01:39:07.870593
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    hpn = HurdPfinetNetwork({})
    assert hpn.platform == 'GNU'



# Generated at 2022-06-13 01:39:24.253230
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    module = FakeModule({})
    fact_class = HurdPfinetNetwork(module)

    facts = {}

    fact_class.assign_network_facts(facts, '/usr/bin/fsysopts', '/servers/socket/inet')

    assert isinstance(facts['interfaces'], list)
    assert len(facts['interfaces']) == 1
    assert facts['interfaces'][0] == 'eth0'
    assert facts['eth0']['active']
    assert facts['eth0']['device'] == 'eth0'
    assert isinstance(facts['eth0']['ipv4'], dict)
    assert len(facts['eth0']['ipv4']) == 2
    assert facts['eth0']['ipv4']['address'] == '192.168.1.2'

# Generated at 2022-06-13 01:39:32.544239
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    module = FakeModule()
    obj = HurdPfinetNetwork(module)
    fsysopts_path = obj.module.get_bin_path('fsysopts')
    socket_path = os.path.join(obj._socket_dir, 'inet')
    network_facts = {}
    network_facts = obj.assign_network_facts(network_facts, fsysopts_path, socket_path)

    assert len(network_facts) == 2

    assert 'interfaces' in network_facts
    assert isinstance(network_facts['interfaces'], list)
    assert len(network_facts['interfaces']) == 1
    assert network_facts['interfaces'][0] == 'eth0'

    assert 'eth0' in network_facts
    assert network_facts['eth0']['active'] == True

# Generated at 2022-06-13 01:39:40.433418
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    network_facts = {}
    fsysopts_path = '/bin/fsysopts'
    socket_path = 'socket/inet'
    mock_module = MockAnsibleModule()
    network = HurdPfinetNetwork(module=mock_module)
    result = network.assign_network_facts(network_facts, fsysopts_path, socket_path)

# Generated at 2022-06-13 01:39:43.203939
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    """
    Constructor sets platform, module, and fact_subclass properties
    """
    hp = HurdPfinetNetwork({})
    assert hp.platform == 'GNU'
    assert hp.module != None
    assert hp.fact_subclass == 'gnu_hurd'

# Generated at 2022-06-13 01:39:44.955028
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    nm = HurdPfinetNetwork(None)
    assert(nm.platform == 'GNU')

# Generated at 2022-06-13 01:39:52.708858
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    module = type('test_module', (object,), {'run_command': run_command})

    def run_command(args, check_rc=False, close_fds=True, executable=None, data=None, binary_data=False):
        if args == ['fsysopts', '-L', '/servers/socket/socket']:
            return 0, 'interface=--interface=eth0\naddress=--address=192.168.0.2\nnetmask=--netmask=255.255.255.0\naddress6=--address6=fe80::42:acff:fe11:2/64\n', ''
        return 0, '', ''

    def get_bin_path(name):
        return '/bin/{}'.format(name)

    module.get_bin_path = get_bin_

# Generated at 2022-06-13 01:40:01.318182
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    os.environ['PATH'] = ':'.join(['/bin', '/sbin', os.environ.get('PATH', '')])
    fsysopts_path = os.path.join(os.getcwd(), 'tests', 'unit', 'modules', 'ansible', 'module_utils', 'facts', 'network', 'fsysopts')

    fsysopts_stdout = '''--interface=/dev/eth0
--interface=/dev/eth1
--interface=/dev/eth1
--interface=/dev/eth0
--address=192.168.1.42
--address6=2407:7800:4004:806::1004/64
--netmask=255.255.255.0
--address6=2407:7800:4004:806::1002/64
'''

    m = H

# Generated at 2022-06-13 01:40:04.492439
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    network_collector = HurdNetworkCollector()
    assert network_collector._platform == 'GNU'
    assert network_collector._fact_class == HurdPfinetNetwork


# Generated at 2022-06-13 01:40:09.600099
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    network_facts= {'interfaces': []}
    fsysopts_path= '/foo/fsysopts'
    socket_path= '/foo/socket'

    module = AnsibleModule(
        argument_spec = dict(),
        supports_check_mode = True
    )

    network = HurdPfinetNetwork(module)

    network.assign_network_facts = HurdPfinetNetwork.assign_network_facts

# Generated at 2022-06-13 01:40:17.572570
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    from ansible_collections.ansible.community.tests.unit.compat import mock
    from ansible_collections.ansible.community.tests.unit.modules.utils import set_module_args
    from ansible_collections.ansible.community.plugins.module_utils.facts import FactCollector

    module = mock.MagicMock()
    module.run_command.return_value = (0, '', '')

    set_module_args({})
    fact_collector = FactCollector(module=module)
    network_collector = fact_collector.collect(network_collector=HurdNetworkCollector())

    assert network_collector._platform == 'GNU'
    assert isinstance(network_collector._fact_class(module), HurdPfinetNetwork)



# Generated at 2022-06-13 01:40:41.109897
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    import os
    import tempfile
    from ansible.module_utils.facts.network.base import Network
    from ansible.module_utils.facts.network.gnu import HurdPfinetNetwork
    from ansible.module_utils.facts.network.gnu import HurdNetworkCollector
    def write_file(filename, data):
        with open(filename, 'w') as f:
            f.write(data)

# Generated at 2022-06-13 01:40:51.609195
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    import pytest
    from ansible.module_utils.facts.network.gnu import Network, HurdPfinetNetwork

    network = Network()

    network_facts = {}
    current_if = ''
    fsysopts_path = 'fsysopts'
    socket_path = '/servers/socket/inet'

    out = '''\
--interface=/dev/eth0 --address=172.28.128.2 --netmask=255.255.255.0 --address6=2001:db8:aa::bb/128
'''

# Generated at 2022-06-13 01:40:54.294061
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    """Test HurdNetworkCollector class constructor"""

    collector = HurdNetworkCollector()

    assert collector.platform == 'GNU'
    assert collector.fact_class.__name__ == 'HurdPfinetNetwork'


# Generated at 2022-06-13 01:41:00.934102
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    m = MockModule()
    n = HurdPfinetNetwork(m)

    # Assume fsysopts returns the following text
    # --interface=fsysopts --address=192.168.1.10 --netmask=255.255.255.0
    fsysopts_stdout = '--interface=fsysopts --address=192.168.1.10 --netmask=255.255.255.0'
    network_facts = {}
    network_facts = n.assign_network_facts(network_facts, '/sbin/fsysopts',
                                           '/servers/socket/inet')
    assert 'interfaces' in network_facts
    assert 'interface_count' not in network_facts
    assert len(network_facts['interfaces']) == 1

# Generated at 2022-06-13 01:41:03.020133
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    network = HurdPfinetNetwork({}, {}, [])
    assert network.platform == 'GNU'


# Generated at 2022-06-13 01:41:06.000368
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    assert HurdPfinetNetwork._platform == 'GNU'
    assert HurdPfinetNetwork._socket_dir == '/servers/socket/'

# Generated at 2022-06-13 01:41:14.580503
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    import os

    try:
        os.stat('/servers/socket/inet')
    except OSError:
        print('/servers/socket/inet does not exist. Skipping unit test for class HurdPfinetNetwork')
        return

    from ansible.module_utils.facts import FactCollector
    module = AnsibleModuleMock()
    fact_class = HurdPfinetNetwork(module)
    result = fact_class.populate()
    interfaces = [x for x in os.listdir('/dev') if not x.startswith('.')]
    assert sorted(interfaces) == sorted(result['interfaces'])

# Generated at 2022-06-13 01:41:15.846785
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    collector = HurdNetworkCollector()
    assert collector is not None

# Generated at 2022-06-13 01:41:18.841034
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    """
    Test the constructor of HurdNetworkCollector
    """
    obj = HurdNetworkCollector()
    assert obj._fact_class == HurdPfinetNetwork, 'test_HurdNetworkCollector assert#1 has failed.'


# Generated at 2022-06-13 01:41:20.432014
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    assert HurdPfinetNetwork.platform == 'GNU'


# Generated at 2022-06-13 01:41:41.493257
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    # Defined success output of GNU Hurd command 'fsysopts -L /servers/socket/inet'
    gnu_hurd_output = """--address=192.168.122.91
--address6=fe80::5054:ff:fea7:d2c5/64
--interface=/dev/eth0
--metric=0
--netmask=255.255.255.0
--netmask6=64
--network=192.168.122.0
--network6=fe80::5054:ff:fea7:d2c5
--silent"""

    # Expected output

# Generated at 2022-06-13 01:41:44.229356
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    """
    Test class HurdNetworkCollector
    """
    print('Testing constructor of HurdNetworkCollector')
    # Test with parameters
    # Test without parameters
    network_collector = HurdNetworkCollector()
    assert network_collector.platform == 'GNU'

# Generated at 2022-06-13 01:41:48.378800
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    from ansible.module_utils.facts import collect_facts
    from ansible.module_utils.facts.network.gnu import HurdPfinetNetwork
    from ansible.module_utils.facts.collector import BaseFactCollector

    collected_facts = collect_facts.CollectFacts(dict(), dict()).populate()
    instance = HurdPfinetNetwork(collected_facts, dict())
    assert isinstance(instance, BaseFactCollector)
    assert isinstance(instance, HurdPfinetNetwork)

# Generated at 2022-06-13 01:41:50.391546
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    network_facts = {}
    network = HurdPfinetNetwork(network_facts)
    assert network_facts == {}

# Generated at 2022-06-13 01:42:00.689032
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    module = AnsibleModuleMock()
    network = HurdPfinetNetwork(module)

    test1 = network.assign_network_facts(
        {},
        '/usr/local/bin/fsysopts',
        '/servers/socket/inet',
        )
    assert test1['interfaces'] == ['eth0', 'eth1', 'lo']

# Generated at 2022-06-13 01:42:07.459073
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    class Module(object):
        def __init__(self, params):
            self.params = params

        def get_bin_path(self, executable, opt_dirs=[]):
            return '/bin'

        def get_bin_path(self, executable, opt_dirs=[]):
            return '/bin/fsysopts'

        def run_command(self, command):
            return 0, '', ''

    module = Module({})
    network = HurdPfinetNetwork(module)
    network.populate()

# Generated at 2022-06-13 01:42:17.561795
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    import tempfile
    tf = tempfile.NamedTemporaryFile()
    tf.write('#!/bin/sh\necho --interface=/dev/eth0 --address=192.168.1.1 --netmask=255.255.255.0 --address6=2001:db8:1:0:21a:4eff:fe22:9e96/64\n')
    tf.flush()

# Generated at 2022-06-13 01:42:22.519134
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    # overrides the _platform and _fact_class attributes
    collector = HurdNetworkCollector(None, None, platform='GNU', fact_class='HurdPfinetNetwork')
    assert collector._platform == 'GNU'
    assert collector._fact_class == HurdPfinetNetwork


# Generated at 2022-06-13 01:42:24.269063
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    net = HurdPfinetNetwork({})
    assert isinstance(net, HurdPfinetNetwork)

# Generated at 2022-06-13 01:42:32.043691
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    from ansible.module_utils.facts.network.hurd import HurdPfinetNetwork
    pfinet = HurdPfinetNetwork(None)
    pfinet.module = MagicMock()
    pfinet.module.run_command.return_value = (0,
                                              '--interface=/dev/eth0 --address=10.0.0.10 --netmask=255.0.0.0 --address6=fe80::a00:27ff:fe51:57a1/64',
                                              '')

    network_facts = {'interfaces': ['eth0']}

# Generated at 2022-06-13 01:43:05.326974
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    module = AnsibleModule(
        argument_spec = dict()
    )

    module.run_command = Mock(return_value=(0, '--interface=/dev/eth0 --address=172.16.42.165 --netmask=255.255.255.0', ''))

    network = HurdPfinetNetwork(module)
    network._socket_dir = 'test/unit/module_utils/facts/network/socket_dir/'
    network.module.get_bin_path = Mock(return_value='/fake/bin/fsysopts')

    os.path.exists = Mock(return_value=True)

    network.populate()

# Generated at 2022-06-13 01:43:06.913836
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    obj = HurdPfinetNetwork()
    assert obj


# Generated at 2022-06-13 01:43:15.304092
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    # Check GNU Hurd specific network values in network facts.
    # The test case is based on the fsysopts output of GNU Hurd
    # machine.
    module = FakeModule()
    fsysopts_path = '/servers/socket/inet6'
    socket_path = '/servers/socket/inet6'
    network = HurdPfinetNetwork({}, module)


# Generated at 2022-06-13 01:43:26.321886
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    module = AnsibleModule(argument_spec={})
    module.run_command = MagicMock()

# Generated at 2022-06-13 01:43:35.272178
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    module = FakeAnsibleModule()
    iface = HurdPfinetNetwork(module)
    ret = iface.populate()
    assert ret['interfaces'] == ['eth0'], ret['interfaces']
    assert ret['eth0']['ipv4']['address'] == '192.168.1.3', ret['eth0']['ipv4']['address']
    assert ret['eth0']['ipv4']['netmask'] == '255.255.255.0', ret['eth0']['ipv4']['netmask']
    assert ret['eth0']['ipv6'][0]['address'] == '2001:0db8:ac10:fe01:0000:0000:0000:0000', ret['eth0']['ipv6'][0]['address']

# Generated at 2022-06-13 01:43:45.939007
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    from ansible.module_utils.facts.network.hurd import HurdPfinetNetwork
    from ansible.module_utils.facts.network.base import Network
    from ansible.module_utils.facts.network.linux.ifconfig import LinuxIfconfigNetwork
    import ansible.module_utils.facts.facts
    import os

    # Test if HurdPfinetNetwork is a subclass of Network
    assert issubclass(HurdPfinetNetwork, Network)

    # Test if HurdPfinetNetwork is not a subclass of LinuxIfconfigNetwork
    assert not issubclass(HurdPfinetNetwork, LinuxIfconfigNetwork)


# Test if HurdNetworkCollector is a subclass of NetworkCollector

# Generated at 2022-06-13 01:43:47.413718
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    assert HurdPfinetNetwork


# Generated at 2022-06-13 01:43:55.335503
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    """
    For testing, how to use the HurdPfinetNetwork class
    """

    class MockModule(object):
        def get_bin_path(self, arg):
            return '/bin/fsysopts'


# Generated at 2022-06-13 01:44:05.048994
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    module = AnsibleModule(
        argument_spec=dict(
            gather_subset=dict(default=['!all', '!min'], type='list')
        ),
        supports_check_mode=True
    )

    if not module.params['gather_subset']:
        module.params['gather_subset'] = ['!all', '!min']

    gather_subset = module.params['gather_subset']
    runable_subset = frozenset(gather_subset).intersection(HurdPfinetNetwork.collector_subset())
    if not runable_subset:
        module.exit_json(ansible_facts={})

    failed_subset = []
    facts = dict()

# Generated at 2022-06-13 01:44:07.934567
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    '''
    Expected result: creation of an HurdPfinetNetwork object
    '''
    assert HurdPfinetNetwork(None)



# Generated at 2022-06-13 01:45:32.325058
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    from ansible.module_utils.facts.network.hurd import HurdPfinetNetwork

    network_factory = HurdPfinetNetwork()
    network_facts = network_factory.populate()

    assert type(network_facts) == dict
    assert len(network_facts) > 0
    assert type(network_facts['interfaces']) == list
    assert len(network_facts['interfaces']) > 0

    default_if = network_facts['interfaces'][0]
    assert type(default_if) == str
    assert len(default_if) > 0

    assert type(network_facts[default_if]) == dict
    assert type(network_facts[default_if]['ipv4']) == dict
    assert type(network_facts[default_if]['ipv4']['address'])

# Generated at 2022-06-13 01:45:34.231125
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    module = AnsibleModule(argument_spec={})
    obj = HurdPfinetNetwork(module)
    assert obj.populate() == {}

# Generated at 2022-06-13 01:45:35.964155
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    """
    All this routine does is instantiate the class.
    """

    hurd_network_collector = HurdNetworkCollector()

# Generated at 2022-06-13 01:45:41.982488
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    """
    This test check the assign_network_facts method of the HurdPfinetNetwork class.
    """
    import json
    import mock
    import sys

    if sys.version_info[:2] < (2, 7):
        import unittest2 as unittest
    else:
        import unittest

    from ansible.module_utils import basic

    from ansible.module_utils.facts.network.gnu_hurd import HurdPfinetNetwork

    class TestModule(object):
        def __init__(self):
            self.params = None

# Generated at 2022-06-13 01:45:51.469011
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    from ansible.module_utils.facts.network.hurd.pfinet import HurdPfinetNetwork
    from ansible.module_utils._text import to_bytes

    network_facts = {}
    # WARNING: the following fsysopts output has been generated on my Debian GNU/Hurd system,
    # it is hardcoded in this unit test because fetching it dynamically through the system API
    # would obviously be an overkill.
    # On a GNU/Hurd system running the pfinet translator, fsysopts can be used to extract
    # the network configuration.
    # For example, on my Debian GNU/Hurd system:
    #   fsysopts '/servers/socket/inet'
    # returns:
    #   interface=--interface=/dev/eth0
    #   address=--address=192.168.0.

# Generated at 2022-06-13 01:45:56.064349
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    test_module = type('', (object, ), {
        'run_command': lambda x: (0, test_module.response, '')
    })
    test_module.response = '''--interface=eth0 --address=127.0.0.1 --netmask=255.0.0.0 --gateway=127.0.0.1 --address6=::1/128'''
    test_network = HurdPfinetNetwork(test_module)

    network_facts = test_network.assign_network_facts({}, '/usr/bin/fsysopts', '/servers/socket/inet')
    assert network_facts['interfaces'] == ['eth0']

# Generated at 2022-06-13 01:45:56.837433
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    assert(HurdPfinetNetwork())

# Generated at 2022-06-13 01:46:01.141034
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    hnc = HurdNetworkCollector()
    assert isinstance(hnc, NetworkCollector)
    assert float('.'.join(map(str, hnc.GNU))) == hnc.max_version
    assert hnc.platform == 'GNU'
    assert hnc.min_version == hnc.max_version

# Generated at 2022-06-13 01:46:01.627352
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    assert True

# Generated at 2022-06-13 01:46:04.965449
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    network_collector = HurdNetworkCollector()
    assert network_collector.platform == 'GNU'
    assert network_collector.fact_class == HurdPfinetNetwork