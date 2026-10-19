

# Generated at 2022-06-13 01:48:47.233097
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
	module = AnsibleModule(argument_spec={})
	linux_network_obj = LinuxNetwork(module)

	# eth0 with valid info
	result = linux_network_obj.get_interfaces_info(
		"test_path/", {'address': '172.31.0.15', 'macaddress': '07:59:5e:b5:5b:e7'}, {'address': 'fe80::257:2eff:feb5:5be7%eth0'}
	)

# Generated at 2022-06-13 01:48:56.945708
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    module = AnsibleModule(
        argument_spec = dict(
            gather_subset=dict(default=['all'], type='list')
        )
    )

    ln = LinuxNetwork(module)
    all_groups = ['system', 'interfaces', 'routes']
    subset = ['all', 'system', 'interfaces', 'routes']
    def gather_subset(module, groups):
        return ln.gather_subset(module, groups)
    res = gather_subset(module, subset)
    assert isinstance(res, dict)
    assert set(res.keys()) == set(all_groups)
    subset.remove('all')
    res = gather_subset(module, subset)
    assert isinstance(res, dict)

# Generated at 2022-06-13 01:49:08.306410
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    # Mock the module
    class MockModule(object):
        def __init__(self, params):
            self.params = params
            self.run_command = params['run_command']

        # This method is only used by the get_ethtool_data method
        def get_bin_path(self, binary):
            # return 'fake_bin_path'
            return os.path.join(self.params['dirname'], 'sbin', binary)

    # Mock ethtool
    class MockEthTool(object):

        def __init__(self, module):
            self.module = module


# Generated at 2022-06-13 01:49:16.678987
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():

    from ansible.module_utils import basic

    module = basic.AnsibleModule(
        argument_spec=dict()
    )

    linux_network = LinuxNetwork(module)
    default_ipv4, default_ipv6 = linux_network.get_default_interfaces()

    # Check that the default_ipv4/6 are valid
    assert 'address' in default_ipv4
    assert 'address' in default_ipv6
    assert default_ipv4['address'] != '127.0.0.1'
    assert default_ipv6['address'] != '::1'



# Generated at 2022-06-13 01:49:24.341183
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    class ModuleTest(object):

        def __init__(self):
            self.params = {
                'config': '/etc/ansible/test_LinuxNetwork_config',
                'files': {},
                'module_name': 'test_LinuxNetwork',
                'failed': False,
                'changed': False,
            }

        def run_command(self, args, errors=''):
            print(args)
            command = args[0]
            if self.params['config'] not in command:
                if command == '/sbin/ip':
                    if '-o -f inet' in command or '-o -f inet6' in command:
                        return 0, self.params['files'][command], ''
                    else:
                        return 1, '', 'Unsupported command: {}'.format(command)

# Generated at 2022-06-13 01:49:26.872540
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    ln = LinuxNetwork()
    ln.module.run_command = mock.Mock(return_value=0)
    ln.get_interfaces_info()

# Generated at 2022-06-13 01:49:29.765481
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    # get_interfaces_info(ip_path, default_ipv4, default_ipv6)
    # Note that this method relies on static data and cannot be tested in isolation
    pass


# Generated at 2022-06-13 01:49:38.290488
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    linux_network = LinuxNetwork()
    linux_network.populate()

# Generated at 2022-06-13 01:49:40.222517
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    # TODO: create mock device and ethtool command output to return
    pass


# Generated at 2022-06-13 01:49:49.400723
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    def mock_get_file_content(f, default=None):
        content_file = dict(
            speed='100',
            operstate='up',
            bridge='bridge',
            bonding='bonding',
            bonding_slave='bonding_slave',
            mtu='1500',
            type='1',
            flags='0x1003',
        )
        if f == '/sys/class/net/test/bridge/bridge_id':
            return '8000.000c29a3b7d1'
        if f == '/sys/class/net/test/bridge/stp_state':
            return '1'
        if f == '/sys/class/net/test/bonding/slaves':
            return 'eth0 eth1 eth2'

# Generated at 2022-06-13 01:50:30.579146
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    # Create a new instance of LinuxNetwork class
    network = LinuxNetwork()
    # Create a new instance of AnsibleModule class
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )
    # Override the module.exit_json method
    module.exit_json = exit_json
    # Override the module.fail_json method
    module.fail_json = fail_json
    # Pass network.module to the network.populate method
    network.populate(network.module)
    # The first time the network.module.exit_json is called, the result is printed
    network.module.exit_json.called = False
    # The first time the network.module.fail_json is called, the result is printed
    network.module.fail_json.called = False
    #

# Generated at 2022-06-13 01:50:37.620083
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    module = MagicMock()
    module.get_bin_path.return_value = '/path/to/ethtool'
    module.run_command.return_value = (0, 'foo: bar\nother: true', '')
    m = LinuxNetwork()
    m.module = module
    assert m.get_ethtool_data('eth1') == {
        'features': {
            'foo': 'bar',
            'other': 'true'
        }
    }


# Generated at 2022-06-13 01:50:49.020662
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    # NOTE: this module *depends* on the LinuxNetwork module
    fake_module = type('', (), {})()
    fake_net = LinuxNetwork(fake_module)

    # NOTE: not using the fake module since trying to use the real get_bin_path
    fake_module.get_bin_path = lambda self, x: x

    interface_dict = {'eth0': '00:11:22:33:44:55', 'eth1': '00:44:33:22:11:00', 'bond0': '00:22:44:66:88:AA',
                      'lo': '00:00:00:00:00:00', 'bond1': '00:AA:88:66:44:22'}


# Generated at 2022-06-13 01:50:59.562022
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    network = LinuxNetwork()
    network.module.run_command = MagicMock()
    network.get_interfaces_info = MagicMock(return_value=([],[]))
    network.get_default_interfaces = MagicMock(return_value=({},{}))
    network.get_interfaces_counters = MagicMock(return_value={})
    network.get_routes = MagicMock(return_value=([],[],[]))
    network.get_facts_from_cachefile = MagicMock(return_value=({},[]))
    network.check_default_route = MagicMock(return_value=({},[]))
    network.time_hires = MagicMock(return_value={})
    network.get_capabilities = MagicMock(return_value={})
    network.pop

# Generated at 2022-06-13 01:51:12.132572
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    import sys

    # Mock module for function run_command
    # Changes behavior of module.run_command
    # Sends content from file to stdout and stderr, always returns (0, content, content)
    class MockedModule(object):

        def __init__(self, module_name):
            self.module_name = module_name

        def get_bin_path(self, name, required=False, opt_dirs=[]):
            bin_path = ''


            if name == 'ip':
                bin_path = os.path.join(os.path.dirname(__file__), 'ip.txt')
            if bin_path:
                self.module.exit_json(**{'msg': 'bin_path defined'})

# Generated at 2022-06-13 01:51:19.601266
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    module = AnsibleModule(
        argument_spec = dict(
        ),
        supports_check_mode=True
    )

    # These tests were originally in the original integration test
    # test/units/modules/utils/test_network_module.py
    # set basic facts for testing
    module.params['ansible_facts'] = {
        'ansible_distribution': 'Debian',
    }
    module.params['ansible_distribution_version'] = '10'

    set_module_args(dict(
        config = dict(
            config = '/etc/network/interfaces',
            state = 'present',
        ),
    ))

    # make sure a reasonable default is set for the path
    if not os.path.exists(module.params['path']):
        module.params['path'] = os.path

# Generated at 2022-06-13 01:51:24.871091
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    m = LinuxNetwork(module=None)
    if not m.module.get_bin_path('ethtool'):
        skip_if_not_root()
    # NOTE: mock_ethtool_data is defined in the test_LinuxNetwork_get_interfaces_info test
    return m.get_ethtool_data(device='eth0') == mock_ethtool_data


# Generated at 2022-06-13 01:51:30.446778
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    test = LinuxNetwork(module=MockLinux())

# Generated at 2022-06-13 01:51:42.375743
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    m = module_mock.MockModule()
    m.get_bin_path = class_mock.MockMethod(return_value="")

# Generated at 2022-06-13 01:51:49.290216
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    '''Unit test for method get_interfaces_info of class LinuxNetwork'''

    from ansible.module_utils.basic import AnsibleModule

    test_module = AnsibleModule(
        argument_spec={},
        supports_check_mode=True
    )

    statements = []
    statements.append('(python_version == "2.6" or python_version == "2.7")')
    statements.append('ansible.module_utils.facts.network.linux.get_interfaces_info()')
    code = '\n'.join(statements)

    result = {}


# Generated at 2022-06-13 01:52:34.386849
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    '''The get_ethtool_data method should return expected output'''
    from ansible.module_utils._text import to_bytes

    # FIXME: this is a unit test that's also an integration test
    from ansible.module_utils.common.command import Command

    class Module(Command):
        def __init__(self):
            self.run_command_called = False
            self.run_command_args = []
            self.run_command_kwargs = {}
            self.run_command_rcs = []
            self.run_command_stdouts = []
            self.run_command_stderrs = []
            self.get_bin_path_paths = []
            self.get_bin_path_rc = 0
            self.get_bin_path_rcs = []
            self.get_bin

# Generated at 2022-06-13 01:52:44.079220
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    module = AnsibleModule(argument_spec={})
    module.exit_json = exit_json
    network = LinuxNetwork(module=module)

    # FIXME: make sure we have these paths, maybe mock them?

    rc, default_ipv4, default_ipv6 = network.get_default_interfaces_info()
    if rc == 0:
        default_ipv4['network'] = socket.inet_ntoa(struct.pack('!L', int(default_ipv4['network'], 16)))
        default_ipv4['netmask'] = socket.inet_ntoa(struct.pack('!L', int(default_ipv4['netmask'], 16)))

# Generated at 2022-06-13 01:52:53.227028
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    network = LinuxNetwork()
    data = network.get_ethtool_data("enp0s31f6")
    assert data['features']['rx_udp_tunnel_port_offload'] == "off"
    assert data['features']['tx_udp_tunnel_port_offload'] == "off"
    assert data['features']['rx_all'] == "off"
    assert data['features']['tx_all'] == "off"
    assert data['features']['fcoe_mtu'] == "off"
    assert data['features']['gso_partial'] == "off"
    assert data['features']['l2_fwd_offload'] == "off"
    assert data['features']['rx_udp_tunnel_port_offload'] == "off"


# Generated at 2022-06-13 01:52:54.787569
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    # test argument *device*
    device = "eth0"
    # test function call
    linux_network = LinuxNetwork()
    data = linux_network.get_ethtool_data(device)


# Generated at 2022-06-13 01:52:56.363489
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    assert LinuxNetwork(None).get_default_interfaces() == ({'default_ipv4': {}, 'default_ipv6': {}}, {})

# Generated at 2022-06-13 01:53:09.173058
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():

    module = AnsibleModule(
        argument_spec=dict(
            gather_subset=dict(default=['!config'], type='list'),
        ),
        supports_check_mode=True,
    )

    network = LinuxNetwork(module)
    network.populate()
    result = network.get_result(filter_exclude=['config'])

    keys = [
        'default_ipv4',
        'default_ipv6',
        'interfaces',
        'all_ipv4_addresses',
        'all_ipv6_addresses',
    ]

    for k in keys:
        assert k in result

    # FIXME: this should be wired together with the unit tests specified
    # in network_common.NetworkModuleTestCase

    assert len(result['interfaces']) == 4


# Generated at 2022-06-13 01:53:12.580565
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    linux_network=LinuxNetwork()
    result=linux_network.get_ethtool_data({'device': 'eth0'})
    assert result == {}


# Generated at 2022-06-13 01:53:16.941138
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():

    ln = LinuxNetwork()
    ln.get_default_interfaces = mock.Mock(return_value=('eth0', '2001:DB8::1'))
    (default_interface_v4, default_interface_v6) = ln.get_default_interfaces()
    assert default_interface_v4 == 'eth0'
    assert default_interface_v6 == '2001:db8::1'


# Generated at 2022-06-13 01:53:24.274999
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    module = AnsibleModule({})
    module.get_bin_path = Mock()
    module.run_command = Mock()
    get_bin_path_map = {
        'ip': '/sbin/ip',
        'route': '/sbin/route',
    }
    module.get_bin_path.side_effect = lambda x: get_bin_path_map[x]
    commands = {
        'v4': ['/sbin/ip', '-4', 'route', 'get', '8.8.8.8'],
        'v6': ['/sbin/ip', '-6', 'route', 'get', '2001:4860:4860::8888'],
    }

    def run_command_map(command, **kwargs):
        rc = 0

# Generated at 2022-06-13 01:53:32.188014
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    """
    Test method populate of class LinuxNetwork
    """
    # NOTE: this test is not really a unit test per se, it exercises the whole module
    # NOTE: should be converted to a proper ansible test
    module = AnsibleModule(
        argument_spec={},
        supports_check_mode=False
    )
    # FIXME: remove this check in a later version when core support is added (see https://github.com/ansible/ansible/pull/59591)
    if not module._name.startswith('community.general.'):
        module.fail_json(msg='This module has been replaced. Please use "network_cli" instead')
    linux_network = LinuxNetwork(module)
    linux_network.populate()

# Generated at 2022-06-13 01:54:12.472628
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    # create a temporary directory
    tmpdir = tempfile.mkdtemp()
    # fake the sysfs filesystem in the temporary directory
    os.makedirs(os.path.join(tmpdir, 'sys/class/net/lo'))
    os.makedirs(os.path.join(tmpdir, 'sys/class/net/eth0'))
    os.makedirs(os.path.join(tmpdir, 'sys/class/net/eth1'))
    os.makedirs(os.path.join(tmpdir, 'sys/class/net/br0'))
    os.makedirs(os.path.join(tmpdir, 'sys/class/net/br0/brif'))

# Generated at 2022-06-13 01:54:21.817706
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    ln = LinuxNetwork()
    ln.module = Mock()

# Generated at 2022-06-13 01:54:22.624253
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    assert False, "No tests for this module"

# Generated at 2022-06-13 01:54:29.109180
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    def mock_run_command(module, command, errors='surrogate_then_stderr'):
        out = (
            'default via 192.168.1.1 dev eno16777736 proto static metric 100\n'
            'default dev eno16777736  proto static  metric 100\n'
            'default via fe80::f816:3eff:fe6e:c7f4 dev eno16777736 proto ra metric 100 expires 86580sec mtu 1500 hoplimit 64 pref medium\n'
            'default via fe80::f816:3eff:fe6e:c7f4 dev eno16777736 proto ra metric 100 expires 2619sec hoplimit 64 pref medium\n'
            'default dev eno16777736  proto kernel  metric 100\n'
        )
        return 0

# Generated at 2022-06-13 01:54:35.170160
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    # arrange
    mock_module = Mock()
    mock_module.run_command.return_value = (0, 'foo', '')
    network_linux = LinuxNetwork(module=mock_module)

    # act
    result = network_linux.get_ethtool_data('eth0')

    # assert
    assert result == {}


# Generated at 2022-06-13 01:54:44.536089
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    # FIXME: better way to test a class method?
    # NOTE: this is a class method
    interfaces_info = LinuxNetwork.get_interfaces_info("/sbin/ip")[0]
    assert len(interfaces_info) > 0
    assert 'default_ipv4' in interfaces_info
    assert 'default_ipv6' in interfaces_info
    default_iface = interfaces_info['default_ipv4']
    assert 'address' in default_iface
    assert 'macaddress' in default_iface
    assert 'mtu' in default_iface
    assert 'type' in default_iface

# Generated at 2022-06-13 01:54:52.308735
# Unit test for method get_interfaces_info of class LinuxNetwork

# Generated at 2022-06-13 01:55:03.922643
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    """Test get_default_interfaces method of LinuxNetwork class"""
    module = MagicMock()
    module.run_command.return_value = (0, '1.2.3.4 dev eth0  src  1.2.3.4  via 2.2.2.2 dev eth0  src 2.2.2.2 metric 1024', '')
    module.fail_json.return_value = None
    module.get_bin_path.return_value = '/sbin/ip'
    ln = LinuxNetwork(module)
    assert ln.get_default_interfaces() == ({'address': '1.2.3.4', 'gateway': '2.2.2.2'}, {'address': '2.2.2.2', 'gateway': '1.2.3.4'})

#

# Generated at 2022-06-13 01:55:12.705390
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    # This is called by the module to load params
    module = AnsibleModule(supports_check_mode=True)

    # Construct an instance of the class we test
    instance = LinuxNetwork(module)

    # Check the method we test
    rc, out, err = instance.get_default_interfaces()

    # Make sure that the output we got is what we expect.
    assert rc == 0
    # Check that out is a dict, not a string
    assert isinstance(out, dict)
    assert 'v4' in out
    assert 'v6' in out
    assert 'default_ipv4' in out
    assert 'default_ipv6' in out

    # The out dict should at least have some keys
    assert out['v4']
    assert out['v6']
    assert out['default_ipv4']


# Generated at 2022-06-13 01:55:22.750354
# Unit test for method get_interfaces_info of class LinuxNetwork

# Generated at 2022-06-13 01:56:05.856484
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():

    device = 'eth0'
    module = MockModule()
    mock_ethtool_path = lambda: module.get_bin_path('ethtool')

    # unit test can't mock module.run_command

# Generated at 2022-06-13 01:56:10.596399
# Unit test for constructor of class LinuxNetworkCollector
def test_LinuxNetworkCollector():
    lnc = LinuxNetworkCollector()
    assert(lnc._platform == 'Linux')
    assert(lnc._fact_class == LinuxNetwork)
    assert(lnc.required_facts == set(['distribution', 'platform']))


# Generated at 2022-06-13 01:56:21.433936
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    module = AnsibleModule(argument_spec=dict())
    ln = LinuxNetwork(module)
    module.run_command = MagicMock()
    module.get_bin_path = MagicMock(return_value=None)

# Generated at 2022-06-13 01:56:22.270264
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    pass

# Generated at 2022-06-13 01:56:30.827465
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    o = LinuxNetwork()
    assert o.NIC_NAME == 'eno1'

# Generated at 2022-06-13 01:56:39.237847
# Unit test for method get_interfaces_info of class LinuxNetwork

# Generated at 2022-06-13 01:56:51.181659
# Unit test for method populate of class LinuxNetwork

# Generated at 2022-06-13 01:56:59.650905
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():

    import pytest
    from ansible_collections.notstdlib.moveitallout.plugins.module_utils.common.removed import removed

    class FakeModule(object):

        DEFAULT_GET_BIN_PATH_RESULT = True


# Generated at 2022-06-13 01:57:08.026997
# Unit test for method get_ethtool_data of class LinuxNetwork

# Generated at 2022-06-13 01:57:16.292441
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    module = AnsibleModule(
        argument_spec=dict(),
    )
    module.params['gather_subset'] = ['all']
    module.params['gather_network_resources'] = 'all'
    parent = Network(module)

    # Test case 1. No default interfaces
    content = "default via 10.20.30.40 dev eth0\n"
    fd, fname = tempfile.mkstemp()
    with open(fname, 'w') as f:
        f.write(content)
    path = os.path.dirname(fname)
    obj = LinuxNetwork(module)
    default_ipv4, default_ipv6 = obj.get_default_interfaces(path)
    assert default_ipv4 == default_ipv6 == {}

    # Test case 2. Default v

# Generated at 2022-06-13 01:58:08.914362
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    # input data
    interfaces = {}
    ips = dict(
        all_ipv4_addresses=[],
        all_ipv6_addresses=[],
    )
    default_ipv4 = {
        'address': '',
        'broadcast': '',
        'netmask': '',
        'network': '',
        'macaddress': '',
        'mtu': 0,
        'type': '',
        'alias': '',
    }
    default_ipv6 = {
        'address': '',
        'prefix': '',
        'scope': '',
        'macaddress': '',
        'mtu': 0,
        'type': '',
    }
    # expected data

# Generated at 2022-06-13 01:58:15.494882
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    module = AnsibleModule(argument_spec={})
    module.run_command = MagicMock(return_value=(0, '', ''))
    module.get_bin_path = MagicMock(return_value='/bin/true')

    # test for loop in /sys/class/net/*
    def glob_side_effect(path):
        if path == '/sys/class/net/*':
            return ['/sys/class/net/eth0', '/sys/class/net/eth1']
        else:
            return []
    glob.glob = MagicMock(side_effect=glob_side_effect)

    # test for loop in os.path.exists