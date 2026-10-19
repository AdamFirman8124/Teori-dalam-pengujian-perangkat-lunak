

# Generated at 2022-06-13 01:48:46.052780
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    class FakeModule(object):
        def __init__(self):
            self.run_command_count = 0
            self.run_command_count2 = 0
            self.fail_json_called = False
            self.fail_json_count = 0
            self.fail_json_count2 = 0
            self.module_args = dict()

        def run_command(self, args, errors=None):
            self.run_command_count += 1
            if errors is None:
                errors = "surrogate_then_replace"
            if errors == "surrogate_then_replace":
                _rc = 0
                # On the first run, return a bridge interface
                # On the second run, return a bond interface
                if self.run_command_count == 1:
                    _stdout = bridge_data

# Generated at 2022-06-13 01:48:56.225845
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    """Unit test for method `get_default_interfaces` of class LinuxNetwork"""
    module = AnsibleModule(argument_spec={})
    ln = LinuxNetwork(module)
    # Test empty
    data = (
        "\n",
        "",
        "Garbage",
        "0.0.0.0\n ::/0",
        "0.0.0.0\n default via ::/0",
    )
    for d in data:
        assert ln.get_default_interfaces(d) == (None, None)
    # Test IPv4
    data = "default via 192.168.1.1 dev eth0\n default via 192.168.1.1 dev eth1 proto dhcp metric 100"

# Generated at 2022-06-13 01:49:07.669082
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    ln = LinuxNetwork()
    ln.module = AnsibleModuleMock()
    ln.module.run_command = mock.Mock()
    ln.module.run_command.return_value = (
        0,
        '224.0.0.1 dev lo  proto kernel  scope link  src 127.0.0.1 \n'
        'default via 192.168.1.1 dev ens3  proto static  metric 100 \n'
        'default dev ens3  scope link  metric 100  \n'
        'default via fe80::1 dev ens3  metric 0  \n'
        'default dev ens3  proto kernel  metric 1024  \n',
        '')

# Generated at 2022-06-13 01:49:18.156337
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    # ensure we have a good env to test in
    assert 'ANSIBLE_LIBRARY' in os.environ
    assert 'ANSIBLE_MODULE_UTILS' in os.environ
    test_module_utils_path = os.path.join(os.environ['ANSIBLE_LIBRARY'],
                                          'modules', 'network', 'cloud', 'module_utils', 'basic.py')
    assert os.path.exists(test_module_utils_path)
    sys.path.append(os.path.dirname(test_module_utils_path))

    from ansible.module_utils.basic import AnsibleModule

# Generated at 2022-06-13 01:49:20.307754
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    module = None
    linux_network = LinuxNetwork(module)
    device = "lo"
    assert linux_network.get_ethtool_data(device) == {}


# Generated at 2022-06-13 01:49:27.168890
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )

    m_run_command = MagicMock(return_value=(0, '', ''))
    m_get_bin_path = MagicMock(return_value='/sbin/ip')


# Generated at 2022-06-13 01:49:36.544945
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    module = MockANSIBLE_MODULE()
    ln = LinuxNetwork(module)
    device = "eth0"
    assert ln.get_ethtool_data(device)["features"]["rx-all"] == "on"
    assert ln.get_ethtool_data(device)["features"]["tx-scatter-gather-fraglist"] == "off"

# Generated at 2022-06-13 01:49:47.581429
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    from ansible.utils.path import unfrackpath
    from ansible.module_utils.facts._mounts import Mounts
    from ansible.module_utils.facts._device_number import DeviceNumber
    from ansible.module_utils.facts._distribution import Distribution
    from ansible.module_utils.facts._swap import Swap
    from ansible.module_utils.facts.filesystems import FileSystems
    from ansible.module_utils.facts._system import System
    from ansible.module_utils.facts._lsb import Lsb
    from ansible.module_utils.facts._kernel import Kernel
    from ansible.module_utils.facts._cpu import Cpu
    from ansible.module_utils.facts._memory import Memory
    from ansible.module_utils.facts._local import Local


# Generated at 2022-06-13 01:49:59.338100
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    module = AnsibleModule(argument_spec={})
    ln = LinuxNetwork(module)

# Generated at 2022-06-13 01:50:07.911201
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    fake_module = FakeModule()
    fake_module.get_bin_path = lambda x: '/usr/sbin/ethtool'
    fake_module.run_command = lambda x, **kw: (0, '', '')
    linux_network = LinuxNetwork(fake_module)
    assert 'features' in linux_network.get_ethtool_data('enp0s8')
    assert 'timestamping' in linux_network.get_ethtool_data('enp0s8')
    assert 'hw_timestamp_filters' in linux_network.get_ethtool_data('enp0s8')


# Generated at 2022-06-13 01:50:38.219794
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    # Test init with empty input
    network = LinuxNetwork()
    network.populate()
    r = network.get_interfaces()
    assert r

    from pprint import pprint as pp
    pp(r)


# Generated at 2022-06-13 01:50:49.979706
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    module = AnsibleModule(argument_spec={'ip_path': {'type': 'str', 'default': '/sbin/ip'}})
    device_data = {
        'all_ipv4_addresses': [
            '192.0.2.1'
        ],
        'all_ipv6_addresses': [
            '2001:db8::1'
        ]
    }
    default_ipv4 = {
        'address': '192.0.2.1',
        'broadcast': '192.0.255.255',
        'netmask': '255.255.0.0',
        'network': '192.0.2.0'
    }

# Generated at 2022-06-13 01:51:00.110147
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    module = AnsibleModule(argument_spec={})
    ln = LinuxNetwork(module)
    rc, out, err = ln.module.run_command('ip addr list')
    if rc != 0:
        module.fail_json(msg="'ip' command not found")
    ip_path = ln.module.get_bin_path('ip')
    default_ipv4 = dict()
    default_ipv6 = dict()
    interfaces, ips = ln.get_interfaces_info(ip_path, default_ipv4, default_ipv6)
    # Unit test for method get_interfaces_info of class LinuxNetwork
    for iface, data in interfaces.items():
        assert 'device' in data
        assert 'type' in data

# Generated at 2022-06-13 01:51:12.566337
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    class ExpModule:
        def __init__(self):
            self.bin_path = None

        def get_bin_path(self, module_name, required=False, opt_dirs=[]):
            pass

        def run_command(self, args, errors='surrogate_then_replace'):
            pass

    class ExpGatherFacts:
        def __init__(self):
            self.gather_subset = None
            self.gather_network_resources = None

    class ExpTaskResult:
        def __init__(self):
            args = []

    # TODO: test this method, it is deprecated
    #module = ExpModule()
    #module.params = {
    #    "gather_subset": ["all"],
    #    "gather_network_resources": ["all"],
   

# Generated at 2022-06-13 01:51:24.368202
# Unit test for method get_default_interfaces of class LinuxNetwork

# Generated at 2022-06-13 01:51:29.980160
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    '''
    validate method get_ethtool_data.
    '''
    class MockModule(object):
        '''
        mock class for module
        '''
        def __init__(self):
            self.content = ''

        def get_bin_path(self, path, opt_dirs=[]):
            '''
            return bin path
            '''
            return "/bin/{}".format(path)

        def run_command(self, cmd, errors='surrogate_then_replace'):
            '''
            return command output
            '''
            # pylint: disable=unused-argument
            if cmd[-1] == '-k':
                return 0, self.content, None
            if cmd[-1] == '-T':
                return 0, self.content, None
            return

# Generated at 2022-06-13 01:51:41.975245
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    module = AnsibleModule(argument_spec={
        'addresses_format': {'type': 'str', 'default': 'mac_dash'}
    })

    if not PY3:
        module.fail_json('This module requires Python 3')

    ln = LinuxNetwork(module)

# Generated at 2022-06-13 01:51:50.507490
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():

    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes

    class TestModule(object):

        def run_command(self, args, **kwargs):
            return 0, None, None

        @staticmethod
        def get_bin_path(name, **kwargs):
            return "/bin/" + name

    class FakeSysmodule(object):
        def __init__(self):
            self.path = {}

        def isfile(self, path):
            return path in self.path

        def isdir(self, path):
            return path in self.path

        def walk(self, path):
            return []

        def readlink(self, path):
            return self.path[path]


# Generated at 2022-06-13 01:52:00.278978
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    from ansible.module_utils.basic import AnsibleModule
    from library._text import to_text

    class FakeAnsibleModule(AnsibleModule):
        def __init__(self):
            self.params = dict()
            self.params['ip_path'] = 'ip'
            self.params['default_ipv4'] = {'gateway': 'None'}
            self.params['default_ipv6'] = {'gateway': 'None'}
            self.run_command = run_command_mock
            self.get_bin_path = get_bin_path_mock

        # This is a hack to make the module work with 2.0 and 2.2 or
        # use Ansible 2.0.0+ and get_bin_path() is removed in 2.3

# Generated at 2022-06-13 01:52:09.322200
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    # Create an object of class LinuxNetwork
    ln = LinuxNetwork()
    ip_path = ln.module.get_bin_path("ip", True, ["/sbin/", "/usr/sbin/"])
    # FIXME: code duplication with populate()
    # TODO: mock ip route get for both kernel versions
    # Find default IPv4 interfaces by running 'ip route get 8.8.8.8'
    rc, out, err = ln.module.run_command("%s route get 8.8.8.8" % ip_path, errors='surrogate_then_replace')
    default_ipv4 = {}
    if rc == 0:
        default_ipv4 = dict(list(zip(['interface', 'address', 'host'], out.split()[4:7])))

    # Find default IPv

# Generated at 2022-06-13 01:52:43.953246
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    default_interface = {'v4': {'interface': 'lo', 'address': '127.0.0.1', 'broadcast': '0.0.0.0', 'netmask': '255.0.0.0', 'network': '127.0.0.0'}, 'v6': {'interface': 'lo', 'address': '::1', 'prefix': '128', 'scope': 'host'}}
    linux_network_obj = LinuxNetwork()
    result = linux_network_obj.get_default_interfaces()
    assert compare_dictionaries(result, default_interface) is True


# Generated at 2022-06-13 01:52:49.275470
# Unit test for constructor of class LinuxNetworkCollector
def test_LinuxNetworkCollector():
    """This will test LinuxNetworkCollector class"""
    required_facts = {'distribution': 'Fedora', 'platform': 'Linux'}
    with patch('ansible.module_utils.facts.collector.get_ansible_module') as get_ansible_module_mock:
        module = MagicMock()
        module.run_command = MagicMock()
        module.run_command.return_value = [0, 'fake_retval', '']
        module.params = {'gather_subset': 'all'}
        get_ansible_module_mock.return_value = module
        network_collector_inst = LinuxNetworkCollector(module)
    # This will confirm that variable environ is set to os.environ
    assert network_collector_inst.environ is os.environ
    #

# Generated at 2022-06-13 01:52:55.401580
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    linux_network = LinuxNetwork({})

    # Interface names with : are not valid in ansible.
    # The method must replace it by _.

# Generated at 2022-06-13 01:53:08.402361
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True,
    )
    module.run_command = mock.Mock(return_value=(0, '', ''))
    linux_network = LinuxNetwork(module)

# Generated at 2022-06-13 01:53:19.290340
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    nm = LinuxNetwork()
    assert nm.is_linux()
    nm.module = FakeModule()
    assert 'get_file_content' in nm.module.__dict__
    nm.module.get_bin_path = lambda x: x

# Generated at 2022-06-13 01:53:24.699343
# Unit test for method get_interfaces_info of class LinuxNetwork

# Generated at 2022-06-13 01:53:32.776614
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    inventory = LinuxNetwork()
    inventory.module = MagicMock()
    inventory.module.run_command.return_value = (0, "", "")
    # test defaults
    inventory.populate()
    assert inventory.default_ipv4['address'] == '1.1.1.1'
    assert inventory.default_ipv6['address'] == '::1'
    assert inventory.default_ipv6['netmask'] == 'ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff'
    inventory.module.run_command.return_value = (0, "172.16.1.1", "")
    inventory.populate()
    assert inventory.default_ipv4['address'] == '172.16.1.1'
    assert inventory.default_ipv6['address'] == '::1'


# Generated at 2022-06-13 01:53:41.239784
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    linux_network = LinuxNetwork()
    linux_network.module = MagicMock()
    linux_network.module.run_command = MagicMock()
    linux_network.module.run_command.return_value = [0, "    default via 192.168.0.1", ""]
    data = linux_network.get_default_interfaces()
    expected = {
        'v4': {'gateway': '192.168.0.1'},
        'v6': {}}
    assert data == expected



# Generated at 2022-06-13 01:53:50.748411
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    from tempfile import TemporaryDirectory
    from textwrap import dedent

    with TemporaryDirectory() as tempdir:
        with open('/sys/class/net/lo/mtu', 'w') as f:
            f.write('65536')
        with open('/sys/class/net/lo/flags', 'w') as f:
            f.write('0x00001002')
        with open('/sys/class/net/lo/device/driver/module', 'w') as f:
            f.write('/lib/modules/whatever\n')
        with open('/sys/class/net/lo/type', 'w') as f:
            f.write('1\n')

        with open('/sys/class/net/lo/operstate', 'w') as f:
            f.write('down')


# Generated at 2022-06-13 01:53:55.774746
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    module = MagicMock()
    module.run_command.return_value = (0, '', '')
    module.get_bin_path.return_value = '/bin/ip'
    ln = LinuxNetwork(module)
    ln.get_default_interfaces.return_value = '1.1.1.1', '::1'
    ln.get_interfaces_info.return_value = {'iface': {}}, {'all_ipv4_addresses': []}
    ln.get_routes_info.return_value = {}, {}
    ln.interfaces = {}
    ln.ips = {}
    ln.routes = {}
    connections = {}
    ln.populate()
    assert ln.interfaces
    assert ln.ips
    assert l

# Generated at 2022-06-13 01:54:49.080809
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    module = MagicMock()
    module.get_bin_path.return_value = "/usr/bin/ip"


# Generated at 2022-06-13 01:55:00.886244
# Unit test for method get_interfaces_info of class LinuxNetwork

# Generated at 2022-06-13 01:55:06.449810
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    # Make sure we have the same output in all cases
    linux_network = LinuxNetwork(module)
    instance = linux_network.get_default_interfaces
    assert isinstance(instance, tuple)
    assert len(instance) == 2
    assert isinstance(instance[0], dict)
    assert isinstance(instance[1], dict)
    assert "address" in instance[0]
    assert "gateway" in instance[0]



# Generated at 2022-06-13 01:55:17.429191
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    module = AnsibleModule(argument_spec=dict())
    module.fail_json = Mock()
    linux_network = LinuxNetwork(module)
    linux_network.get_default_interfaces()

# Generated at 2022-06-13 01:55:22.279575
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    ipv4, ipv6 = LinuxNetwork().get_default_interfaces()
    assert isinstance(ipv4, dict)
    assert isinstance(ipv6, dict)



# Generated at 2022-06-13 01:55:24.050044
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    # TODO: setup mock
    pass


# Find out which named interfaces are up and running

# Generated at 2022-06-13 01:55:33.517380
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    from ansible.module_utils.facts._text_extractors.linux_network import LinuxNetwork

    # Fake module for testing method get_interfaces_info of class LinuxNetwork
    class FakeModule:

        def __init__(self, ip_path, default_ipv4, default_ipv6):
            self.ip_path = ip_path
            self.default_ipv4 = default_ipv4
            self.default_ipv6 = default_ipv6

        def get_bin_path(self, name, required=False, opt_dirs=[]):
            return '/sbin/ip'

        def run_command(self, args, errors='surrogate_then_replace'):
            command = args[0]
            device = args[-1]


# Generated at 2022-06-13 01:55:44.864984
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    my_net = LinuxNetwork()
    features, timestamping, hw_timestamp_filters, phc_index = my_net.get_ethtool_data('lo')

# Generated at 2022-06-13 01:55:56.189501
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    p = mock.patch("os.path.exists")
    mock_patched_exists = p.start()
    mock_patched_exists.return_value = True

    p = mock.patch("os.access")
    mock_patched_access = p.start()
    mock_patched_access.return_value = True

    p = mock.patch("os.stat")
    mock_patched_stat = p.start()
    mock_patched_stat.return_value = os.stat_result(0)

    p = mock.patch("os.readlink")
    mock_patched_readlink = p.start()
    mock_patched_readlink.return_value = "test/path"

    p = mock.patch("os.listdir")

# Generated at 2022-06-13 01:56:02.390827
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    network = LinuxNetwork()
    network.module = MagicMock()
    network.module.run_command = MagicMock(side_effect=[
        [0, 'ipv4-forwarding 1']
    ])
    network.module.params = {
        'use_ipv4': True
    }
    network.populate()
    network.module.run_command.assert_called_with(['sysctl', '-n', 'net.ipv4.ip_forward'])
    assert network.ipv4_forwarding == 1


# Generated at 2022-06-13 01:56:51.484615
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    m = MagicMock(spec=SystemTools)
    m.get_bin_path.return_value = 'ip'
    m.run_command.return_value = 0, '1\tlo\t\n', ''

    ln = LinuxNetwork(m)
    assert ln.get_interfaces_info('ip', {'address': ''}, {'address': ''}) == ({'lo': {'device': 'lo', 'ipv4': {'address': '', 'broadcast': '', 'netmask': '255.0.0.0', 'network': '0.0.0.0'}, 'type': 'unknown'}}, {'all_ipv4_addresses': ['0.0.0.0'], 'all_ipv6_addresses': []})



# Generated at 2022-06-13 01:56:59.827905
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    class MockModule(object):
        class MockRunResult(object):
            def __init__(self, rc, out, err):
                self.rc = rc
                self.stdout = out
                self.stderr = err

        def __init__(self, rc, out, err):
            self.run_result = self.MockRunResult(rc, out, err)

        def get_bin_path(self, arg, opt_dirs=None):
            if arg == "ip":
                return "/bin/ip"
            else:
                return None


# Generated at 2022-06-13 01:57:08.527659
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    # First check that a connection is made
    m = AnsibleModule(argument_spec={})
    n = LinuxNetwork(m)
    assert n
    # Check the result with dummy data
    m = AnsibleModule(argument_spec={})
    n = LinuxNetwork(m)

# Generated at 2022-06-13 01:57:17.474785
# Unit test for method get_default_interfaces of class LinuxNetwork

# Generated at 2022-06-13 01:57:25.943883
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    """
    function to test get_ethtool_data
    """
    module = Mock()
    module.get_bin_path = Mock()
    module.run_command = Mock()
    net = LinuxNetwork(module)
    net.get_ethtool_data('eth0')
    module.get_bin_path.assert_called_once_with('ethtool')
    module.run_command.assert_called_once_with(['/bin/ethtool', '-k', 'eth0'], errors='surrogate_then_replace')
    module.get_bin_path.reset_mock()
    module.run_command.reset_mock()
    net.get_ethtool_data('eth1')


# Generated at 2022-06-13 01:57:33.300095
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    import glob
    import socket
    from copy import deepcopy
    from unittest.mock import patch
    from ansible.module_utils._text import to_text
    from ansible.module_utils.network.common.utils import get_file_content

    def set_module_args(args):
        args = json.dumps({'ANSIBLE_MODULE_ARGS': args})
        basic._ANSIBLE_ARGS = to_text(args)


# Generated at 2022-06-13 01:57:41.583199
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    module = AnsibleModule(argument_spec={})
    set_module_args(dict(gather_subset=['!all', 'interfaces']))
    ln = LinuxNetwork(module)
    facts = ln.populate()
    assert 'default_ipv4' in facts
    assert 'default_ipv6' in facts
    assert 'default_interface' in facts
    assert 'interfaces' in facts
    assert 'all_ipv4_addresses' in facts['interfaces']
    assert 'all_ipv6_addresses' in facts['interfaces']
    assert 'default_ipv4' in facts
    assert 'default_ipv6' in facts



# Generated at 2022-06-13 01:57:50.202838
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    # Check the case where the interface is in the bridge.
    import platform
    import random
    import string
    import time

    class FakeModule:

        def __init__(self):
            self.params = dict()
            self.run_command_calls = 0
            self.run_command_count = dict()

        def get_bin_path(self, _, **__):
            return '/sbin/ip'

        def run_command(self, argv, **kwargs):
            self.run_command_count[argv] = self.run_command_count.get(argv, 0) + 1
            self.run_command_calls += 1


# Generated at 2022-06-13 01:58:01.380397
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    # NOTE: we are not actually running this on a Linux system, so
    #       we may need to loosen assertions or add/modify some tests
    module = None
    ln = LinuxNetwork(module)

    # Fake output of the command
    rc = 0
    out = None
    err = None

    # Default IPv4 address should be modified if ip route output is correct
    ipv4 = dict()
    ipv6 = dict()
    out = 'default via 192.168.0.1 dev eth0  proto static  metric 100  \n'
    ln.get_default_interfaces(rc, out, err, ipv4, ipv6)
    assert ipv4['address'] == '192.168.0.1'

    # Default IPv6 address should be modified if ip route output is correct
    ipv4 = dict()

# Generated at 2022-06-13 01:58:09.836425
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    ln = LinuxNetwork()
    # sample data from ip addr show
    intf = dict(
        name = "lo",
        link_down = False,
        addresses = [
            dict(
                address = "127.0.0.1",
                prefix = "8",
                valid_lft = "forever",
                preferred_lft = "forever",
                scope = "host",
            ),
            dict(
                address = "::1",
                prefix = "128",
                valid_lft = "forever",
                preferred_lft = "forever",
                scope = "host",
            ),
        ],
    )
    data = dict(
        interfaces = dict(
            lo = intf,
        )
    )