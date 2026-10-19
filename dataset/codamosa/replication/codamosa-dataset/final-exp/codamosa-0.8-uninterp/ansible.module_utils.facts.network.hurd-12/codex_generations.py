

# Generated at 2022-06-13 01:37:50.347182
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    a = HurdNetworkCollector()
    assert a.__repr__() == "{'_platform': 'GNU', '_fact_class': <class 'ansible.module_utils.facts.network.hurd.HurdPfinetNetwork'>}"
    assert a.__str__() == "<ansible.module_utils.facts.network.hurd.HurdNetworkCollector platform: GNU>"


# Generated at 2022-06-13 01:37:53.303200
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    assert HurdPfinetNetwork.platform == 'GNU'
    assert HurdPfinetNetwork._socket_dir == '/servers/socket/'


# Generated at 2022-06-13 01:37:55.957799
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    args = {}
    obj = HurdNetworkCollector(args)
    assert obj is not None


# Generated at 2022-06-13 01:37:57.292171
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    network = HurdNetworkCollector()
    assert network._platform == 'GNU'

# Generated at 2022-06-13 01:37:59.428442
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    a = HurdNetworkCollector()
    assert a.platform == a._platform
    assert a.fact_class == a._fact_class

# Generated at 2022-06-13 01:38:09.605240
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    network_facts = {'interfaces': []}
    fsysopts_path = '/servers/socket/fsysopts'
    socket_path = '/servers/socket/pfinet'

    class ModuleTest(object):
        def run_command(self, args, check_rc=True):
            return 0, '--interface=/dev/eth0 --address=192.168.1.1 --netmask=255.255.255.0 --address6=aa:bb:cc::/64', ''

    test_network = HurdPfinetNetwork(ModuleTest())

    result_network_facts = test_network.assign_network_facts(network_facts, fsysopts_path, socket_path)

# Generated at 2022-06-13 01:38:15.278321
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    """
    This test case is a POSIX platform specific testcase of the constructor of the class
    HurdNetworkCollector. It checks the class name of the object instantiated.

    :return:
        None
    """
    collector = HurdNetworkCollector()

    assert isinstance(collector, HurdNetworkCollector) == True, 'Was expecting to get an object of class HurdNetworkCollector'
    assert collector.__class__.__name__ == 'HurdNetworkCollector', 'Was expecting to get an object of class HurdNetworkCollector'


# Generated at 2022-06-13 01:38:25.843032
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    module = FakeModule()
    module.run_command = FakeRunCommand(
        returncode=0,
        out="""--interface=eth0 --address=192.168.0.1 --netmask=255.255.255.0 --broadcast=192.168.0.255
""")
    result = HurdPfinetNetwork(module).populate()
    assert 'interfaces' in result
    assert result['interfaces'] == ['eth0']
    assert 'eth0' in result
    assert 'ipv4' in result['eth0']
    assert 'address' in result['eth0']['ipv4']
    assert result['eth0']['ipv4']['address'] == '192.168.0.1'
    assert 'netmask' in result['eth0']['ipv4']

# Generated at 2022-06-13 01:38:27.443615
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    hpf_net = HurdPfinetNetwork()
    assert hpf_net.platform == 'GNU'

# Generated at 2022-06-13 01:38:34.477784
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    """
    Unit test for constructor of class HurdPfinetNetwork
    """
    _module = MockModule()
    _module.run_command = Mock()

    _module.run_command.return_value = ("""
  Address 0 (set)
  Address 6 (set)
  Flags 1 (set)
  MTU 2 (set)
  NETMASK 3 (set)
  Up 4 (set)
  Offload 5 (set)
  """, "", 0)

    _c = HurdPfinetNetwork(_module)
    _result = _c.populate()

    _module.run_command.assert_called_once_with(['fsysopts', '-L', '/servers/socket/inet'])

    assert 'interfaces' in _result.keys()

# Generated at 2022-06-13 01:38:41.182683
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    module = None
    HurdPfinetNetwork(module)


# Generated at 2022-06-13 01:38:42.071065
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    collector = HurdNetworkCollector()
    assert collector

# Generated at 2022-06-13 01:38:54.674872
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    module = MockModule()
    get_bin_path_result = "fsysopts"
    module.run_command_result = (0, '--interface=/dev/eth0 --protocol inet --address 10.0.0.1 --netmask 255.255.255.0', '')
    fake_network = HurdPfinetNetwork(module)
    fake_network.module.get_bin_path = Mock(return_value=get_bin_path_result)
    fake_network.module.run_command = Mock(return_value=module.run_command_result)
    network_facts = {
        'interfaces': [],
    }
    fsysopts_path = get_bin_path_result
    socket_path = '/servers/socket/inet'
    result = fake_network.assign_network

# Generated at 2022-06-13 01:38:56.110130
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    # For now we don't have a test case.
    pass

# Generated at 2022-06-13 01:39:07.545469
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    class ModuleMock:
        def run_command(self, command_list):
            out = """\
--interface=eth0 --address=192.168.0.1 --netmask=255.255.255.0 --address6=fe80::e0f9:c38e:aee6:8c96/64
--interface=lo --address=127.0.0.1 --netmask=255.0.0.0 --address6=::1/128
"""
            return 0, out, ''

    class NetworkFactsMock:
        def __init__(self):
            self._network_facts = {}

        def __getattr__(self, attr):
            return self._network_facts.get(attr)


# Generated at 2022-06-13 01:39:12.885559
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    from ansible.module_utils.facts.network.gnu.hurd import HurdPfinetNetwork
    from ansible.module_utils.facts.network.base import Network
    from ansible.module_utils.facts.network.gnu.hurd import HurdNetworkCollector
    assert issubclass(HurdPfinetNetwork, Network)
    assert issubclass(HurdNetworkCollector, HurdPfinetNetwork)

# Generated at 2022-06-13 01:39:15.447517
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    obj = HurdPfinetNetwork({})
    assert obj.platform == 'GNU'
    assert obj._socket_dir == '/servers/socket/'

# Generated at 2022-06-13 01:39:19.076424
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    assert HurdPfinetNetwork(module=None).platform == 'GNU'
    assert HurdPfinetNetwork(module=None)._socket_dir == '/servers/socket/'

# Generated at 2022-06-13 01:39:26.665176
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    class AnsibleModuleMock:
        def run_command(self, command, check_rc=False):
            return (0, '''--interface=lo
--flags=0x00001000
--flags=0x00000001
--flags=0x00000002
--address=127.0.0.1
--netmask=255.0.0.0
--address6=::1/128
--address6=fe80::1/64
--interface=eth0
--flags=0x00001002
--flags=0x00000001
--flags=0x00000002
--address=10.0.2.15
--netmask=255.255.255.0
--address6=fe80::a00:27ff:fe96:9e9/64
''', '')

        def fail_json(self):
            pass

   

# Generated at 2022-06-13 01:39:33.825123
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    from ansible.module_utils.facts.system.platform import Platform
    from ansible.module_utils.facts.network.utils import NetworkParser

    # FIXME: This test is not complete, we need to test assign network facts
    # on GNU Hurd - os.path.exists('/servers/socket') returns True, then
    # combine NetworkParser, get command output and check the result
    platform = Platform('GNU')
    module = object()
    module.run_command = lambda x: (0, '', '')
    parser = HurdPfinetNetwork(module, platform)

    network_facts = {'interfaces': []}
    fsysopts_path = '/bin/fsysopts'
    socket_path = '/servers/socket'

# Generated at 2022-06-13 01:39:52.672192
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    module = AnsibleModule(argument_spec={})
    net = HurdPfinetNetwork(module)

    input_file = 'sample.fsysopts'
    with open(input_file, 'r') as f:
        output = f.read()
    fsysopts_path = "/usr/bin/fsysopts"
    socket_path = "/dev/eth0"

    network_dict = net.assign_network_facts({}, fsysopts_path, socket_path)
    eth_dict = network_dict['eth0']

    assert eth_dict['active'] == True
    assert eth_dict['device'] == 'eth0'
    assert eth_dict['ipv4']['address'] == '192.0.2.2'
    assert eth_dict['ipv4']['netmask']

# Generated at 2022-06-13 01:40:01.318070
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    class ModuleTest:
        def __init__(self):
            self.run_command_count = 0
            self.run_command_result = None

        def get_bin_path(self, command):
            return None if command != 'fsysopts' else command

        def run_command(self, command):
            self.run_command_count += 1
            return self.run_command_result

    module = ModuleTest()

    module.run_command_result = (0, '--interface = /dev/eth0 --address = 192.168.0.1 --netmask = 255.255.255.0 --address6 = fe80::a4e4:2df4:7a9e:953a /64', '')
    network_facts = HurdPfinetNetwork(module).populate()

# Generated at 2022-06-13 01:40:10.990706
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    module = AnsibleModuleMock()
    fsysopts_path = module.get_bin_path('fsysopts')
    if fsysopts_path is None:
        return module.fail_json(msg="fsysopts not found")

    socket_path = None

    for l in ('inet', 'inet6'):
        link = os.path.join('/servers/socket/', l)
        if os.path.exists(link):
            socket_path = link
            break

    if socket_path is None:
        return module.fail_json(msg="No socket found")

    obj = HurdPfinetNetwork(module)
    obj.assign_network_facts({}, fsysopts_path, socket_path)

# Generated at 2022-06-13 01:40:21.570642
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    fsysopts_out = '--interface=eth0 --address=1.2.3.4 --netmask=255.0.0.0 --address6=aa:ff::00/12'
    fsysopts_path = '/gnu/hurd/fsysopts'
    socket_path = '/gnu/hurd/socket'

    module = FakeModule()
    network = HurdPfinetNetwork(module)
    facts = network.assign_network_facts({}, fsysopts_path, socket_path)

    assert facts['interfaces'] == ['eth0']

# Generated at 2022-06-13 01:40:25.069784
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    module = FakeAnsibleModule()
    network = HurdPfinetNetwork(module=module)
    assert network.platform == 'GNU'
    assert network._socket_dir == '/servers/socket/'



# Generated at 2022-06-13 01:40:35.298547
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    import ansible.module_utils.facts.network.gnu.hurd.pfinet.network

    network_facts = {}
    fsysopts_path = '/usr/bin/fsysopts'
    socket_path = '/servers/socket/inet'
    network_facts['interfaces'] = []

    out = """--interface=/dev/eth0 --address=1.2.3.4 --netmask=255.255.255.255 \
--address6=fec0::1/64 --address6=fec0::2/64"""
    rc = 0
    err = ''


# Generated at 2022-06-13 01:40:43.965817
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    import ansible.module_utils.facts.network.pfinet.gnu as gnu
    from ansible.module_utils.facts import FactModuleTestCase

    network_facts = {'interfaces': [], 'all_ipv4_addresses': []}

# Generated at 2022-06-13 01:40:44.344347
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    pass

# Generated at 2022-06-13 01:40:53.319380
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    module = MagicMock()
    module.run_command = MagicMock(return_value=(0, '--interface=/dev/eth0 --address=10.0.2.15 --netmask=255.255.255.0 --address6=fe80::5054:ff:fe4e:4d7f/64', ''))
    module.get_bin_path = MagicMock(return_value='/bin/fsysopts')
    network = HurdPfinetNetwork(module)
    network_facts = network.populate()
    assert network_facts['interfaces'] == ['eth0']
    assert network_facts['eth0']['ipv4']['address'] == '10.0.2.15'

# Generated at 2022-06-13 01:41:00.890512
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    from ansible.module_utils.facts.network import HurdPfinetNetwork

    module_mock = type('module', (), dict(run_command=lambda *args: (0, '', '')))

    network = HurdPfinetNetwork(module_mock)
    network_facts = network.assign_network_facts({}, '/bin/fsysopts', '/servers/socket/inet')

    assert network_facts['interfaces'] == ['eth0']
    assert network_facts['eth0']['ipv4']['address'] == '192.168.0.3'
    assert network_facts['eth0']['ipv4']['netmask'] == '24'

# Generated at 2022-06-13 01:41:31.969128
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    import ansible.module_utils.facts.network.hurd as hurd

    # Test IPv4 only
    fsysopts_path = '/usr/bin/fsysopts'
    socket_path = '/servers/socket/inet'
    h = hurd.HurdPfinetNetwork()
    # We should create the module to test assign_network_facts method
    import ansible.module_utils.basic
    h.module = ansible.module_utils.basic.AnsibleModule(
        argument_spec=dict()
    )
    # Mocking the run_command method
    h.module.run_command = lambda x: (0, '--interface=/dev/eth0 --address=10.0.2.15 --netmask=255.255.255.0', None)
    network_facts = h.assign_network_

# Generated at 2022-06-13 01:41:33.269557
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    network = HurdPfinetNetwork(None)
    assert network.platform == 'GNU'


# Generated at 2022-06-13 01:41:36.091878
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    collector = HurdNetworkCollector()
    assert collector._platform is HurdNetworkCollector._platform
    assert collector._fact_class is HurdPfinetNetwork


# Generated at 2022-06-13 01:41:43.083470
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    # Unit test for method assign_network_facts of class HurdPfinetNetwork
    # AnsibleModule object
    class AnsibleModule(object):
        @staticmethod
        def get_bin_path(bin_name, opt_dirs=[]):
            return fsysopts_path

        @staticmethod
        def run_command(cmd):
            if cmd == [fsysopts_path, '-L', socket_path]:
                return (0, fsysopts_output, '')
            else:
                return (255, '', '')

    # Unit test for method assign_network_facts of class HurdPfinetNetwork
    # Module params
    params = {}

    fsysopts_path = '/hurd/pfinet/fsysopts'
    socket_path = '/servers/socket/inet'

# Generated at 2022-06-13 01:41:45.419464
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    network = HurdPfinetNetwork(dict())
    assert network.name == 'HurdPfinetNetwork'
    assert network.platform == 'GNU'
    assert network.module is not None

# Generated at 2022-06-13 01:41:46.098713
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    HurdPfinetNetwork()


# Generated at 2022-06-13 01:41:48.878365
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    """
    Constructing a HurdPfinetNetwork Object.
    """
    obj = HurdPfinetNetwork({})

# Generated at 2022-06-13 01:41:58.729157
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    module = MockModule()
    module.run_command = Mock(return_value=(0, '--interface=/dev/eth1 --address=10.0.1.1 --netmask=255.255.255.0 --address6=fe80::5054:ff:fe46:97bc/64', ''))
    module.get_bin_path = Mock(side_effect=lambda x: x)

    # execute method populate
    network = HurdPfinetNetwork(module)
    facts = network.populate()

    # test results
    assert facts['interfaces'] == ['eth1']
    assert facts['lo'] == {'active': True,
                           'device': 'lo',
                           'ipv4': {},
                           'ipv6': [],
                          }

# Generated at 2022-06-13 01:42:08.275786
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    from ansible.module_utils.facts.network.gnu.hurd import HurdPfinetNetwork
    from ansible.module_utils.facts.network.base import Network
    from ansible.module_utils.facts.network.gnu.hurd import HurdNetworkCollector
    import os
    import shutil
    import tempfile

    class TestNetwork(Network):
        platform = 'GNU'
        _socket_dir = '/servers/socket/'

    class TestNetworkCollector(HurdNetworkCollector):
        _fact_class = TestNetwork

    # create a temporary directory to store the fake pfinet fsysopts
    temp_dir = tempfile.mkdtemp()
    # create test file
    filename = os.path.join(temp_dir, 'fsysopts_pfinet')

# Generated at 2022-06-13 01:42:12.248591
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    module = AnsibleModule(argument_spec={})
    obj = HurdPfinetNetwork(module)
    assert obj.platform == 'GNU'
    assert obj._socket_dir == '/servers/socket/'


# Generated at 2022-06-13 01:43:04.798509
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    class MyModule:
        def get_bin_path(self, name):
            return '/bin/fsysopts'
        def run_command(self, cmd):
            cmd = ' '.join(cmd)
            if cmd == '/bin/fsysopts -L /servers/socket/inet':
                return (0, '--address=192.168.1.1 --netmask=255.255.255.0 --interface=/dev/eth0 --address6=fe80::216:3eff:fe69:8d08/64', '')

# Generated at 2022-06-13 01:43:05.791396
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    HurdNetworkCollector()

# Generated at 2022-06-13 01:43:14.616489
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    module = AnsibleModule(
        argument_spec=dict()
    )
    network = HurdPfinetNetwork(module=module)
    network_facts = {}
    fsysopts_path = '/bin/fsysopts'
    inet_socket_path = '/servers/socket/inet'
    out = '''
--interface=/dev/eth0 --address=10.1.1.10 --netmask=255.255.255.0
--interface=/dev/eth1 --address=10.1.1.11 --netmask=255.255.255.0
'''
    new_network_facts = network.assign_network_facts(network_facts, fsysopts_path, inet_socket_path)

# Generated at 2022-06-13 01:43:16.133576
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    assert HurdNetworkCollector._platform == 'GNU'
    assert HurdNetworkCollector._fact_class == HurdPfinetNetwork

# Generated at 2022-06-13 01:43:26.463407
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    HurdPfinetNetwork._socket_dir = 'tmp/'

    network_facts = {}
    fsysopts_path = 'tmp/fsysopts'
    socket_path = 'tmp/socket'

    # Test assign_network_facts with ipv4 address
    iface = "eth0"
    address = "192.168.1.1"
    netmask = "255.255.255.0"

    out = "--interface=/dev/" + iface + " --address=" + address + " --netmask=" + netmask
    rc = 0

    result = HurdPfinetNetwork(None).assign_network_facts(network_facts, fsysopts_path, socket_path)

# Generated at 2022-06-13 01:43:35.371186
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    fsysopts_path = 'bin/fsysopts'
    socket_path = '/servers/socket/inet'
    module = dict()
    module['run_command'] = lambda arg, **kwargs: ([fsysopts_path, '-L', socket_path], '--interface=/dev/eth0 --address=192.168.1.42 --netmask=255.255.255.0 --address6=::1/128', '')
    module['get_bin_path'] = lambda arg, **kwargs: fsysopts_path
    network_facts = dict()
    current_if = ''

    HurdPfinetNetwork.__init__(self, module)
    network_facts = self.assign_network_facts(network_facts, fsysopts_path, socket_path)

# Generated at 2022-06-13 01:43:47.517008
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    from ansible.module_utils.facts.network import HurdPfinetNetwork
    out = """--interface=/dev/eth0 --address 192.168.1.10 --netmask 255.255.255.0 --address6=2001:0db8:0a0b:12f0:0000:0000:0000:0001/64 --address6=2001:0db8:0a0b:12f0:0000:0000:0000:0002/64 --address6=2001:0db8:0a0b:12f0:0000:0000:0000:0003/64
--interface=/dev/eth1 --address 192.168.1.11 --netmask 255.255.255.0"""
    network_facts = HurdPfinetNetwork().assign_network_facts({}, None, None, None, out)

# Generated at 2022-06-13 01:43:51.616925
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    from ansible.module_utils.facts.network.hurd import HurdPfinetNetwork


# Generated at 2022-06-13 01:43:52.805222
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    assert HurdNetworkCollector() is not None


# Generated at 2022-06-13 01:43:56.508413
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    network_facts = HurdPfinetNetwork({"module": None})
    assert network_facts.platform == 'GNU'
    assert network_facts._socket_dir == '/servers/socket/'

# Generated at 2022-06-13 01:45:58.742769
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    from ansible.module_utils.facts import ansible_facts
    from ansible.module_utils._text import to_text

    temp = ansible_facts._get_facts(
        dict(),
        HurdPfinetNetwork,
        ansible_facts.FallbackNetwork(),
    )

    assert temp is not None
    assert 'eth0' in temp['interfaces']
    assert 'ipv4' in temp['eth0']
    assert 'address' in temp['eth0']['ipv4']
    assert 'netmask' in temp['eth0']['ipv4']
    if 'eth1' in temp['interfaces']:
        assert 'ipv6' in temp['eth1']
        assert 'address' in temp['eth1']['ipv6'][0]

# Generated at 2022-06-13 01:46:00.035290
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    assert HurdPfinetNetwork({}, {}).populate() == {}

# Generated at 2022-06-13 01:46:00.822157
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    HurdPfinetNetwork()

# Generated at 2022-06-13 01:46:09.708701
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    class TestModule:
        def run_command(self, command_args):
            class RC:
                def __init__(self, stdout, stderr):
                    self.stdout = stdout
                    self.stderr = stderr
                    self.rc = 0

            out = '''--interface=/dev/eth0
--address=1.2.3.4
--netmask=255.255.255.0
--address6=1234:5678:9abc:def0:1234:5678:9abc:def0/56'''
            return (0, out, '')

        def get_bin_path(self, name):
            return '/bin/fsysopts'

    module = TestModule()
    network_fact = HurdPfinetNetwork(module)
    facts = network_fact.pop

# Generated at 2022-06-13 01:46:19.514358
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    test_module = type('TestModule', (object,), {})

    class AnsibleModule(object):
        def __init__(self):
            self.run_command = test_module.run_command
            self.tmpdir = test_module.tmpdir

    test_module.run_command = (0, 'pfinet: interface=eth0 address=127.0.0.1 netmask=255.255.255.0 address6=::1 prefix=128', '')

    test_module.tmpdir = 'test'

    test_network_facts = {
        'interfaces': [],
    }

    test_fsysopts = 'fsysopts'
    test_socket = 'socket'

    testnet = HurdPfinetNetwork(AnsibleModule())

# Generated at 2022-06-13 01:46:22.634780
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    from ansible.module_utils.facts.network.gnu.hurd import HurdNetworkCollector
    from ansible.module_utils.facts.network.gnu.hurd import HurdPfinetNetwork
    hnc = HurdNetworkCollector()
    assert hnc._platform == 'GNU'
    assert hnc._fact_class == HurdPfinetNetwork

# Generated at 2022-06-13 01:46:25.021866
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    network_collector = HurdNetworkCollector()
    assert network_collector.platform == 'GNU'
    assert network_collector.fact_class == HurdPfinetNetwork

# Generated at 2022-06-13 01:46:26.488564
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    cl = HurdNetworkCollector()
    assert cl.platform == 'GNU'
    assert cl._fact_class == HurdPfinetNetwork

# Generated at 2022-06-13 01:46:35.220014
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    from ansible.compat.tests.mock import patch
    from ansible.module_utils.facts import Facts
    from ansible.module_utils.facts.collector import get_collector

    mocked_module = patch.object(Facts, 'module')
    mocked_module.start()
    mocked_run_command = patch.object(Facts.module, 'run_command')
    mocked_run_command.start()
    mocked_get_bin_path = patch.object(Facts.module, 'get_bin_path')
    mocked_get_bin_path.start()


# Generated at 2022-06-13 01:46:36.495121
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    result = HurdNetworkCollector()
    assert result is not None
    assert result._platform == result.__class__._platform