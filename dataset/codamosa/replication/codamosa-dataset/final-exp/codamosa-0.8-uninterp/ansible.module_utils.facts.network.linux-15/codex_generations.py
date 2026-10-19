

# Generated at 2022-06-13 01:48:48.271476
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    class FakeModule(object):
        def __init__(self):
            self.params = {

            }

        def get_bin_path(self, name, opts=None):
            if name == "ip":
                return "/sbin/ip"

            if name == "ethtool":
                return "/sbin/ethtool"

    class FakeShell(object):
        def __init__(self):
            self.shell = None


# Generated at 2022-06-13 01:48:53.273198
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule({}, {})
    module.run_command = lambda *args,**kwargs: (0, 'some output', '')
    ln = LinuxNetwork(module)
    device = 'eth0'
    assert 'features' in ln.get_ethtool_data(device)

# Generated at 2022-06-13 01:48:57.692263
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    module = AnsibleModule(argument_spec=dict())
    linux_network = LinuxNetwork(module=module)
    ethtool_data = linux_network.get_ethtool_data("em1")
    assert_equals(ethtool_data, {'features': {'tx_checksumming': 'off', 'rx_checksumming': 'off'}})



# Generated at 2022-06-13 01:49:08.968426
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():

    mock_module = Mock(
        get_bin_path=Mock(return_value="/bin/ip"),
        run_command=Mock(return_value=(0, "default via 192.0.2.1 dev eth1", ""))
    )
    mock_module.run_command.side_effect = [
        (0, "default via 192.0.2.1 dev eth1", ""),
        (0, "default via 2001:db8::1 dev eth1", ""),
    ]

    net = LinuxNetwork(mock_module)

    v4, v6 = net.get_default_interfaces()

    assert v4.get("address") == "192.0.2.1"
    assert v6.get("address") == "2001:db8::1"

    # assert that the mock was called

# Generated at 2022-06-13 01:49:19.623158
# Unit test for method populate of class LinuxNetwork

# Generated at 2022-06-13 01:49:20.867087
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    p = LinuxNetwork()
    p.get_interfaces_info()



# Generated at 2022-06-13 01:49:27.092975
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():

    # prepare test environment
    tmpdir = tempfile.mkdtemp()
    default_ipv4_path = os.path.join(tmpdir, 'default_ipv4')
    default_ipv6_path = os.path.join(tmpdir, 'default_ipv6')
    interfaces_path = os.path.join(tmpdir, 'interfaces')
    routes_path = os.path.join(tmpdir, 'routes')
    with open(default_ipv4_path, 'w'):
        pass
    with open(default_ipv6_path, 'w'):
        pass

# Generated at 2022-06-13 01:49:36.508410
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    module = AnsibleModule(argument_spec={})
    module.params = {}
    ln = LinuxNetwork(module)
    device = "eth0"

# Generated at 2022-06-13 01:49:47.541970
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    # this creates a fake ansible module
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(
        argument_spec={}
    )

    network = LinuxNetwork(module)

    # some fake vars

# Generated at 2022-06-13 01:49:53.553136
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    from io import StringIO
    from ansible.module_utils.six import StringIO
    from ansible.module_utils import basic
    from ansible.module_utils.facts import module_facts


# Generated at 2022-06-13 01:50:30.795944
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    # Dummy class for AnsibleModule
    class AnsibleModule(object):
        def __init__(self, **kwargs):
            self.params = kwargs

    # Create AnsibleModule mock
    module_mock = AnsibleModule(ip_path='/sbin/ip')

    # Create LinuxNetwork class mock
    network = LinuxNetwork(module_mock)

    # Return values of mock functions

# Generated at 2022-06-13 01:50:42.138267
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    import unittest
    import ansible_collections.ansible.community.tests.unit.compat.mock as mock

    module = mock.MagicMock()
    module.get_bin_path = mock.MagicMock(return_value='/usr/sbin/ethtool')

    linux_network = LinuxNetwork(module=module)

    device = 'eth1'

# Generated at 2022-06-13 01:50:53.882273
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    # In the future if we have more complex setup to do for unit tests we can split
    # these out into a single setup method and a single teardown method.
    cwd = os.path.join(os.path.dirname(__file__), "../")
    sys.path.append(cwd)
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.facts.network.base import NetworkCollector

    class FakeModule(object):
        def __init__(self, facts_data):
            self.exit_json = self.exit_json_no_exit
            self.params = {'gather_subset': ['all']}
            self.facts_data = facts_data
            self.fail_

# Generated at 2022-06-13 01:51:01.938384
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    import pytest

    from units.mock.procfs import ProcFS
    from units.mock.linux_network import MockLinuxNetworkModule

    class MockModule:
        def get_bin_path(self, *args, **kwargs):
            return "/usr/bin/ethtool"

        def run_command(self, *args, **kwargs):
            return 0, "", ""

    module = MockLinuxNetworkModule()
    module.module = MockModule()

    ip = LinuxNetwork(module)
    results = ip.get_ethtool_data("test_device")

    assert 'features' in results.keys()
    assert 'timestamping' in results.keys()
    assert 'hw_timestamp_filters' in results.keys()


# Generated at 2022-06-13 01:51:14.101267
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    from ansible.module_utils._text import to_text
    from ansible.module_utils.common.removed import removed_module
    result = removed_module()
    network = LinuxNetwork(result, {})

    # Gather network information.
    network.default_ipv4 = {}
    network.default_ipv6 = {}
    interfaces, ips = network.get_interfaces_info('', network.default_ipv4, network.default_ipv6)

    DEFAULT_INTERFACE = network.get_default_interface()
    if DEFAULT_INTERFACE:
        network.default_ipv4['interface'] = DEFAULT_INTERFACE
        network.default_ipv6['interface'] = DEFAULT_INTERFACE
    public_ipv4, public_ipv6 = network.get_public_interfaces_info

# Generated at 2022-06-13 01:51:21.102295
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    net = LinuxNetwork("/path/to/bin", "/path/to/file")
    net.module = AnsibleModule(
       argument_spec = dict(
           gather_subset=dict(default=None),
           config=dict(default=None),
           probe=dict(default=None),
       ),
    )

# Generated at 2022-06-13 01:51:27.019268
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    # calling LinuxNetwork instance with spec=None will cause the module to fallback to the default lib_path
    test = LinuxNetwork(None)
    # set up some module params for the unit test
    test.module.params['ip_path'] = '/bin/ip'
    interfaces, ips = test.get_interfaces_info()

# Generated at 2022-06-13 01:51:35.211971
# Unit test for constructor of class LinuxNetworkCollector
def test_LinuxNetworkCollector():
    module = AnsibleModuleMock()
    distro_name = 'centos'
    distro_major_version = '7'
    facts = {'distribution': distro_name,
             'distribution_major_version': distro_major_version,
             'platform': 'linux'}
    network_collector = LinuxNetworkCollector(module, facts)
    assert network_collector.distro_name == distro_name
    assert network_collector.distro_version == distro_major_version


# Generated at 2022-06-13 01:51:45.766659
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    from ansible.module_utils import basic
    module = basic.AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True,
    )
    module.exit_json = lambda **kwargs: os._exit(0)
    module.run_command = lambda **kwargs: (0, '', '')
    module.get_bin_path = lambda **kwargs: ''
    get_file_content = get_file_content_mocker('/sys/class/net')
    get_file_content.__name__ = 'get_file_content'


# Generated at 2022-06-13 01:51:52.732835
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    mod = AnsibleModule({u'interfaces': {u'eth0': {u'mtu': u'1500', u'promisc': True, u'interface': u'eth0', u'speed': u'10Gbit/s', u'active': True, u'module': u'ixgbe', u'type': u'unknown', u'macaddress': u'00:00:00:00:00:00'}}}, check_invalid_arguments=False)
    net = LinuxNetwork(mod)

# Generated at 2022-06-13 01:52:32.749253
# Unit test for method get_default_interfaces of class LinuxNetwork

# Generated at 2022-06-13 01:52:40.952555
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    module = ansible_module_get_network_info()
    network = LinuxNetwork(module)

    device = "eth_test_data"

    # Test with no ethtool
    module.params['run_command_check_rc'] = False
    module.run_command = lambda *args, **kwargs: (1, "", "")
    assert network.get_ethtool_data(device) == {}

    # Test with invalid device

# Generated at 2022-06-13 01:52:50.845085
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():

    # NOTE: This unit test is incomplete in that we cannot fully test
    # the LinuxNetwork.get_interfaces_info() method.
    # At this point the only test we can do is to
    # verify that the method "runs" without raising an exception.

    # Set up the module context
    module = AnsibleModule(argument_spec=dict())

    # Create the test case
    # We need to create the following directories:
    # /sys/class/net/enp1s0f1/
    # /sys/class/net/enp1s0f1/device/
    # /sys/class/net/enp1s0f1/device/driver/
    # /sys/class/net/enp1s0f1/device/driver/module/
    # /sys/class/net/enp1s0

# Generated at 2022-06-13 01:52:56.356255
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    # type: () -> None
    module = Mock()
    module.get_bin_path = Mock(return_value="/fake/path")
    module.run_command = Mock(return_value=(0, "", ""))
    linux_network = LinuxNetwork(module)
    linux_network.get_ethtool_data(None)
    assert module.run_command.call_count == 2
    args = [arg[0][0] for arg in module.run_command.call_args_list]
    assert '/fake/path -k' in args
    assert '/fake/path -T' in args



# Generated at 2022-06-13 01:53:09.123268
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    from units.mock.procfs_mock import ProcFsMock
    from units.mock.sys_mock import SysFsMock
    from ansible.module_utils.basic import Environment
    from ansible.module_utils.facts import Facts
    from ansible.module_utils.network import NetworkModule

    module = NetworkModule(argument_spec={},
                           supports_check_mode=False)
    module.run()
    env = Environment(module.params)
    facts = Facts(env)
    module.exit_json(ansible_facts=facts.get_facts())
    sysfs = SysFsMock()
    procfs = ProcFsMock(sysfs)
    module._sysfs_path = sysfs.path()
    network = LinuxNetwork(module, procfs)
    assert network.get_eth

# Generated at 2022-06-13 01:53:19.792470
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    module = AnsibleModule(argument_spec={})
    module.get_bin_path = MagicMock(return_value="/bin/")
    module.run_command = MagicMock(side_effect=lambda x, **kwargs: (0, "", ""))
    module.fail_json = MagicMock()
    args = dict(
        default_ipv4=dict(
            address="192.168.0.15",
            netmask="255.255.255.0",
            network="192.168.0.0",
            broadcast="192.168.0.255",
        ),
        default_ipv6=dict(
            address='fe80::f816:3eff:fe00:ffff',
            prefix=64,
            scope='link',
        ),
    )
    obj = LinuxNetwork(module)

# Generated at 2022-06-13 01:53:25.982869
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    a = LinuxNetwork()


# Generated at 2022-06-13 01:53:34.933434
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():

    from ansible_collections.notstdlib.moveitallout.tests.unit.compat import unittest
    from ansible_collections.notstdlib.moveitallout.tests.unit.compat.mock import patch, MagicMock
    from ansible_collections.notstdlib.moveitallout.plugins.module_utils import basic

    class TestLinuxNetwork(unittest.TestCase):

        def setUp(self):
            self.mock_module = MagicMock(
                    get_bin_path=MagicMock(return_value="/usr/bin/ip")
            )
            self.mock_module.run_command = self.run_command
            self.ln = LinuxNetwork(self.mock_module)

        def run_command(self, args, *args2):
            _ = args

# Generated at 2022-06-13 01:53:38.432345
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    # FIXME: make this a testcase
    n = LinuxNetwork()
    import sys
    n.module = sys.modules[__name__]
    n.populate()


# Generated at 2022-06-13 01:53:47.863409
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    module = AnsibleModule(argument_spec=dict())
    linux_network = LinuxNetwork(module)
    default_ipv4, default_ipv6 = linux_network.get_default_interfaces()
    interfaces, ips = linux_network.get_interfaces_info("/sbin/ip", default_ipv4, default_ipv6)
    linux_network.populate(interfaces, ips)
    assert linux_network.interfaces == interfaces
    assert linux_network.ips == ips
    assert linux_network.default_ipv4 == default_ipv4
    assert linux_network.default_ipv6 == default_ipv6


# Generated at 2022-06-13 01:54:52.662084
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    module_mock = Mock()
    module_mock.get_bin_path.return_value = 'ip'
    module_mock.run_command.return_value = (0, '', '')
    ln = LinuxNetwork(module_mock)
    result = ln.get_interfaces_info('', {}, {})
    module_mock.run_command.assert_any_call(['ip', '-o', 'addr', 'show', 'primary', 'all'], errors='surrogate_then_replace')
    module_mock.run_command.assert_any_call(['ip', '-o', 'addr', 'show', 'secondary', 'all'], errors='surrogate_then_replace')



# Generated at 2022-06-13 01:55:04.198849
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    module = MockAnsibleModule()
    lnxnet = LinuxNetwork(module)
    lnxnet.populate()

# Generated at 2022-06-13 01:55:10.176353
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    module = FakeAnsibleModule()
    ln = LinuxNetwork(module)

    assert module.exit_json.call_count == 0
    assert module.fail_json.call_count == 0

    # Given the attached shippable data, the result is going to be a dict with the following structure
    assert ln.get_default_interfaces() == {'ipv6': {'address': '2000:0000:0000:0000:0000:0000:0000:0001'}, 'ipv4': {'address': '10.8.0.1'}}



# Generated at 2022-06-13 01:55:14.415596
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    # Tests LinuxNetwork.get_interfaces_info
    m = LinuxNetwork()
    default_ipv4 = {}
    default_ipv6 = {}
    m.get_interfaces_info('ip', default_ipv4, default_ipv6)



# Generated at 2022-06-13 01:55:23.770170
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    """Method get_ethtool_data of class LinuxNetwork"""

    # Initialize AnsibleModule instance
    global module
    module = AnsibleModule(argument_spec=dict())

    # Initialize LinuxNetwork instance
    global ln
    ln = LinuxNetwork(module)

    # Create fake ethtool output

# Generated at 2022-06-13 01:55:33.304030
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    # test: on a device that has features
    device = 'eno1'

# Generated at 2022-06-13 01:55:44.727418
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    module = FakeAnsibleModule()
    module.run_command = MagicMock()
    module.get_bin_path = MagicMock(return_value='/usr/bin/ethtool')


# Generated at 2022-06-13 01:55:56.021199
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    # default_ipv4, default_ipv6, default_interface is assumed to be None
    # and therefore set to 'unknown' for the purpose of this test
    # interfaces, ips = get_interfaces_info(ip_path, default_ipv4, default_ipv6)
    ip_path = None
    default_ipv4 = {'address': '192.168.56.1'}
    default_ipv6 = {'address': 'fe80::5054:ff:fe12:3400'}
    interfaces, ips = get_interfaces_info(ip_path, default_ipv4, default_ipv6)
    # NOTE: Ansible 2.6 changed the ordering of secondaries, so test passed
    #       when they were out of order, and now fails when they are in order
    assert interfaces

# Generated at 2022-06-13 01:56:04.500075
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    module = MagicMock()
    module.get_bin_path.return_value = '/bin'
    module.run_command.return_value = 0, '', ''
    l = LinuxNetwork(module)

    l.get_ethtool_data = MagicMock()
    l.get_ethtool_data.return_value = {}

    interfaces = {}

    def mock_glob(path):
        if path == '/sys/class/net/*':
            return [
                '/sys/class/net/test',
                '/sys/class/net/bond0',
                '/sys/class/net/br0',
                '/sys/class/net/lo',
            ]

# Generated at 2022-06-13 01:56:14.590968
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    class AnsibleModule(object):
        @staticmethod
        def run_command(command, check_rc=True):
            return 0, '', ''

        @staticmethod
        def get_bin_path(name):
            return '/sbin/' + name

    class Test(object):
        module = AnsibleModule()

    def get_file_content(path, default=None):
        return 'foo'

    test = Test()
    test.get_file_content = get_file_content
    v4, v6 = test.get_default_interfaces()
    assert(v4['address'] == 'foo')
    assert(v6['address'] == 'foo')


# Generated at 2022-06-13 01:57:24.837300
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    module = AnsibleModule(
        argument_spec=dict(
            ip_path=dict(default='ip')
        ),
        supports_check_mode=True
    )
    n = LinuxNetwork(module)
    # Test for v4 and v6 addresses
    default_interface_v4, default_interface_v6 = n.get_default_interfaces()
    assert default_interface_v4.get('interface')
    assert default_interface_v6.get('interface')
    # Test for v4 only address
    default_interface_v4, default_interface_v6 = n.get_default_interfaces(v6=False)
    assert default_interface_v4.get('interface')
    # Test for v6 only address
    default_interface_v4, default_interface_v6 = n.get_default_

# Generated at 2022-06-13 01:57:32.475979
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    net = LinuxNetwork()
    net.module = MagicMock()


# Generated at 2022-06-13 01:57:42.370496
# Unit test for method get_interfaces_info of class LinuxNetwork

# Generated at 2022-06-13 01:57:50.700840
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    module = AnsibleModule(
        argument_spec=dict(
            device=dict(type='str', default='eth0'),
        ),
        supports_check_mode=False,
        add_file_common_args=True,
    )

    if not HAS_STDLIB:
        module.fail_json(msg='stdlib not found')

    linux_network = LinuxNetwork(module)

    # Linux kernel 4.17.0-rc5-next-20180322

# Generated at 2022-06-13 01:58:01.703058
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
  # set up
  m = ModuleStub({'get_bin_path': lambda _: '/sbin/ip'})

  # Test 1: two default interfaces, one IPv4, one IPv6
  ln = LinuxNetwork(m, {})
  ln.get_file_lines_iter = lambda _: (
      ['default via 192.168.1.254 dev eth0 \n'],
      ['default via fe80::22ae:5cff:fe83:0 dev eth0 \n']
  )
  # run
  v4_default, v6_default = ln.get_default_interfaces()
  # assert
  assert v4_default == {'gateway': '192.168.1.254', 'interface': 'eth0'}

# Generated at 2022-06-13 01:58:09.972267
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    module = MockLinuxNetworkModule()
    lnn = LinuxNetwork(module)
    default_ipv4 = {'address': '192.168.0.1'}
    default_ipv6 = {'address': '2001:0db8::68'}
    interfaces_info, ips_info = lnn.get_interfaces_info('/bin/ip', default_ipv4, default_ipv6)
    assert "eth0" in interfaces_info
    assert interfaces_info["eth0"]["ipv4"]["address"] == '192.168.0.1'
    assert interfaces_info["eth0"]["ipv4"]["broadcast"] == '192.168.0.255'