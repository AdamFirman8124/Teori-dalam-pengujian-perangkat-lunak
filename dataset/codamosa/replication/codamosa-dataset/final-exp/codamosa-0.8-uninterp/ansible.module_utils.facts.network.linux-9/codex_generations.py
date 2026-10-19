

# Generated at 2022-06-13 01:48:46.463827
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():

    # Test case where `route` fails
    # (i.e. no interfaces are specified, and no routing table can be retrieved)

    mock = MagicMock(side_effect=Exception)
    with patch.dict('sys.modules', **{'ansible.module_utils.network.common.utils': mock}):
        module = Mock()
        module.run_command = Mock(return_value=(1, '', ''))
        network = LinuxNetwork(module)
        ipv4, ipv6 = network.get_default_interfaces()
        assert ipv4 == {}
        assert ipv6 == {}

    # Test case where `ip address` fails
    # (i.e. no interfaces are specified, and no address table can be retrieved)

    mock = MagicMock(side_effect=Exception)

# Generated at 2022-06-13 01:48:56.614727
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    test_ip = '/usr/bin/ip'
    # get_default_interfaces() should return default_ipv4, default_ipv6
    default_ipv4 = {'address': '1.2.3.4', 'broadcast': '255.255.255.255', 'netmask': '255.255.255.255', 'network': '1.2.3.4'}
    default_ipv6 = {'address': '1:2:3:4:5:6:1.2.3.4', 'prefix': '64'}
    default_route_ipv4 = {'address': '1.2.3.4', 'interface': 'em1', 'gateway': '4.3.2.1'}

# Generated at 2022-06-13 01:49:03.133876
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    """
    Testing the method get_ethtool_data
    """

    with open("get_ethtool_data_output.txt", "r") as f:
        f_contents = f.read()

    linux_network_obj = LinuxNetwork()


# Generated at 2022-06-13 01:49:11.756398
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    # NOTE: Cannot mock the os module so using mocks from the mock library.
    # mock library will dynamically create an os module based on the provided
    # method and parameters.
    # There is no need to explicitly declare the os module mock when mocking
    # its methods.
    # The below code will mock the os.path.isdir method and add a side effect
    # to it. The return value will still be the default returned by the mock.
    # The side effect will be evaluated if the mocked method is called.
    @mock.patch.object(os.path, 'isdir')
    def test_it(mock_os_path_isdir):
        module = mock.MagicMock()
        mock_os_path_isdir.return_value = True

# Generated at 2022-06-13 01:49:19.023566
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    for version in [1, 2]:
        if version == 1:
            module = FakeAnsibleModuleV1
        elif version == 2:
            module = FakeAnsibleModuleV2

        network = LinuxNetwork(module)

        result_no_ethtool = {
            'features': {},
            'timestamping': [],
            'hw_timestamp_filters': [],
            'phc_index': -1,
        }
        assert network.get_ethtool_data('lo') == result_no_ethtool


# Generated at 2022-06-13 01:49:25.740859
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    # Initialize a fake class
    module_mock = MagicMock()
    module_mock.run_command.return_value = (0, 'test_data', '')
    module_mock.get_bin_path.return_value = '/fake/bin/path'
    fake_class = LinuxNetwork(module_mock)
    facts = {}
    fake_class.populate(facts)
    assert 'network' in facts
    assert 'interfaces' in facts['network']
    assert 'default_ipv4' in facts['network']
    assert 'default_ipv6' in facts['network']
    assert 'all_ipv4_addresses' in facts['network']
    assert 'all_ipv6_addresses' in facts['network']



# Generated at 2022-06-13 01:49:29.423763
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    import platform
    module = AnsibleModule(argument_spec={}, supports_check_mode=True)
    ip_path = module.get_bin_path('ip')
    if platform.system().lower() == 'sunos':
        ip_path = module.get_bin_path('ndd')
    ln = LinuxNetwork(module, ip_path)
    # FIXME: write tests for populate
    return False


# Generated at 2022-06-13 01:49:38.091252
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    device = 'lo'


# Generated at 2022-06-13 01:49:44.138563
# Unit test for method populate of class LinuxNetwork

# Generated at 2022-06-13 01:49:48.700962
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    module = AnsibleModule(
        argument_spec=dict(
            output=dict(default=None, choices=['text', 'dict'], type='str')
        )
    )
    network_module = NetworkModule(module)
    network = network_module.get_module_system_info()
    network.get_default_interfaces()
    module.exit_json(changed=False)



# Generated at 2022-06-13 01:50:28.606222
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    # Host variables
    # TODO: mock "ip" result
    ip_path = '/sbin/ip'
    module = MagicMock(**{'get_bin_path.return_value': ip_path})

# Generated at 2022-06-13 01:50:35.478460
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
  def test_LinuxNetwork_get_default_interfaces(self, *args):
    print(args)
    _, default_ipv4, default_ipv6 = self.get_default_interfaces()
    interfaces, ips = self.get_interfaces_info(self.module.get_bin_path('ip'), default_ipv4, default_ipv6)
    return interfaces, ips



# Generated at 2022-06-13 01:50:44.844270
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    """
    Unit test for method LinuxNetwork.populate()

    """
    #Create a Mock
    module = Mock()
    module.get_bin_path.return_value = ""
    module.run_command.return_value = [0, "", ""]
    obj = LinuxNetwork(module)
    obj.get_interfaces_info = lambda x, y, z: ([], {})
    output = obj.populate()
    assert output == {'interfaces': {}, 'all_ipv4_addresses': [], 'all_ipv6_addresses': [], 'default_ipv4': {}, 'default_ipv6': {}}


# Generated at 2022-06-13 01:50:56.572263
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    from ansible_collections.community.general.tests.unit.compat.mock import MagicMock, patch
    mock_module = MagicMock(name='ansible_collections.community.general.plugins.modules.network_tools.LinuxNetwork')

    mock_module.run_command.return_value = (0, '', '')

    mock_module.get_bin_path.return_value = "/fake_bin_path/ip"
    test_subject = LinuxNetwork(mock_module)
    test_subject.update_default_interface_info = MagicMock(return_value=None)

    test_subject.update_interface_info = MagicMock(return_value=None)

    test_subject.is_default_interface = MagicMock(return_value=True)


# Generated at 2022-06-13 01:50:58.848139
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    module = AnsibleModule(argument_spec={})
    os_obj = LinuxNetwork(module)
    assert os_obj.get_ethtool_data('') == {}



# Generated at 2022-06-13 01:51:09.843977
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    module = AnsibleModule(
        argument_spec=dict(
            gather_subset=dict(default=None, type='list'),
        ),
        supports_check_mode=True,
    )

    n = LinuxNetwork(module)
    default_ipv4, default_ipv6, interfaces, ips = n.populate()
    assert default_ipv4 == {"broadcast": "", "address": "", "network": "", "netmask": ""}
    assert default_ipv6 == {"address": "", "prefix": "", "scope": ""}
    assert isinstance(interfaces, dict)
    assert isinstance(ips, dict)


# Generated at 2022-06-13 01:51:22.250795
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    rhn = LinuxNetwork()
    dict_mock = {
        'default_ipv4': {
         'address': '10.0.0.15',
         'network': '10.0.0.0',
         'broadcast': '10.0.0.255',
         'netmask': '255.255.255.0'
        }
    }
    ipv4_dict_mock, ipv6_dict_mock = {}, {}
    interfaces_dict_mock, ips_dict_mock = {}, {}
    rhn.get_default_interfaces = MagicMock(return_value=(ipv4_dict_mock, ipv6_dict_mock))

# Generated at 2022-06-13 01:51:28.074650
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    # Test fixture for module
    module = AnsibleModule(
        argument_spec=dict(
            gather_subset=dict(required=False, type='list', default=['!all']),
            filter=dict(required=False, type='str'),
        )
    )

    # Test fixture for class LinuxNetwork
    net = LinuxNetwork(module)

    # Test fixture for factorization of class LinuxNetwork._populate
    net._populate()

    # Test fixture for function populate of class LinuxNetwork
    result = net.populate()

    # Test assertion
    assert ('all_ipv4_addresses' in result['ansible_facts']['ansible_all_ipv4_addresses'])
    assert ('ansible_all_ipv6_addresses' in result['ansible_facts'])

    # Test assertion


# Generated at 2022-06-13 01:51:40.300739
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(
        argument_spec=dict(
        ),
        supports_check_mode=False,
    )
    module.params['state'] = 'present'
    module.params['network'] = {'version': 4, 'interface': 'eth0', 'address': '192.168.1.1', 'netmask': '255.255.255.0', 'broadcast': '192.168.1.255'}
    module.params['routes'] = [{'version': 4, 'network': '172.16.0.0', 'netmask': '255.255.0.0', 'gateway': '192.168.1.254'}]

# Generated at 2022-06-13 01:51:49.355092
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    module = AnsibleModule(argument_spec={})
    linux_network = LinuxNetwork(module)
    interfaces = linux_network.get_interfaces_info(
        '/sbin/ip',
        {'address': '1.2.3.7'},
        {'address': '::1'}
    )[0]
    assert 'ipv4' in interfaces['eth0']
    assert interfaces['eth0']['ipv4']['broadcast'] == '192.168.255.255'
    assert interfaces['eth0']['ipv4']['network'] == '192.168.0.0'
    assert interfaces['eth0']['ipv4']['address'] == '192.168.0.10'
    assert 'ipv6' in interfaces['eth0']

# Generated at 2022-06-13 01:52:31.617414
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    '''Unit test for method get_ethtool_data of class LinuxNetwork'''
    # TODO: is this used?
    # TODO: is this testable in unit tests?
    assert False



# Generated at 2022-06-13 01:52:40.182536
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    # create object
    module = AnsibleModule(argument_spec=dict(
        supported=dict(type='bool'),
    ), supports_check_mode=True)
    linux_network = LinuxNetwork(module)

    # mock device
    device = "lo"

    # mock ethtool output, taken from a debian testing box
    import textwrap

# Generated at 2022-06-13 01:52:50.203783
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    from ansible.module_utils.basic import AnsibleModule as AM
    module = AM()
    module.get_bin_path = Mock(side_effect=lambda x: x)
    get_file_content = Mock(return_value='1')
    o = LinuxNetwork(module, get_file_content)

    default_ipv4 = {
        'address': '172.16.25.1',
        'network': '172.16.25.0',
    }
    default_ipv6 = {
        'address': '2c0f:fb50:4003:c00::1',
        'network': '2c0f:fb50:4003:c00::0',
    }
    interfaces, ips = o.get_interfaces_info('', default_ipv4, default_ipv6)

# Generated at 2022-06-13 01:52:56.317768
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    import platform
    ln = LinuxNetwork()
    ln.module = MagicMock()
    ln.module.run_command = run_command
    del ln.module.run_command.return_value
    ln.module.run_command.return_value = 0, '', ''
    ln.module.get_bin_path = MagicMock(return_value='/bin/ip')
    ln.module.fail_json = MagicMock()
    ln.module.warn = MagicMock()
    ln.module.check_mode = False
    ln.module.name = 'setup'
    ln.module.params = {}
    r4, r6 = ln.get_default_interfaces()
    assert r4 == {}
    assert r6 == {}



# Generated at 2022-06-13 01:53:06.248676
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    m = AnsibleModule({})

    n = LinuxNetwork(m)

    assert n.get_default_interfaces() == (defaultdict(lambda: None, {'interface': 'eth0', 'address': '10.0.2.15', 'gateway': '10.0.2.2'}), defaultdict(lambda: None, {'interface': 'eth0', 'address': '2601:646:4700:8ca0:21a:92ff:fe5b:f5b6', 'gateway': '2601:646:4700:8ca0:21a:92ff:fe5b:f5b1'}))

# Generated at 2022-06-13 01:53:17.953712
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():

    # Unit test for method get_default_interfaces(module, ip_path) of
    # class LinuxNetwork
    # TODO: add unit test for case where there are multiple interfaces
    # TODO: add unit test for case where there are no interfaces
    # TODO: add unit test for valid IPv6 interface

    ip_path = "/sbin/ip"
    if not os.path.exists(ip_path):
        ip_path = "/bin/ip"

    module = MagicMock()
    module.run_command.return_value = (0, OUTPUT_IP_ROUTE_SHOW_DEFAULT, '')
    network = LinuxNetwork(module)

    default_ipv4, default_ipv6 = network.get_default_interfaces(ip_path)


# Generated at 2022-06-13 01:53:24.392662
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    module = AnsibleModule(argument_spec=dict())

    command = dict(
        default='ifconfig -a',
        v4=['ip', 'route', 'get', '8.8.8.8'],
        v6=['ip', 'route', 'get', '2001:4860:4860::8888'],
    )

    (patch_socket_socket) = patch('socket.socket', MagicMock(return_value=MockSocket(io.BytesIO(b''))))
    (patch_get_bin_path) = patch.object(AnsibleModule, 'get_bin_path', return_value='ip')

    with patch_socket_socket, patch_get_bin_path:
        network = LinuxNetwork(module)


# Generated at 2022-06-13 01:53:32.357894
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    interface = {'device': 'eth0'}
    _LinuxNetwork__instance = LinuxNetwork()
    _LinuxNetwork__instance.module = MagicMock()

    _LinuxNetwork__instance.module.run_command.return_value = (0, '', '')
    _LinuxNetwork__instance.module.get_bin_path.return_value = False
    assert _LinuxNetwork__instance.get_ethtool_data(interface['device']) == {}

    _LinuxNetwork__instance.module.get_bin_path.return_value = True
    _LinuxNetwork__instance.module.run_command.return_value = (0, '', '')
    assert _LinuxNetwork__instance.get_ethtool_data(interface['device']) == {}


# Generated at 2022-06-13 01:53:38.047000
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    args = ({'device': '/sys/class/net/eth0'},)
    module = AnsibleModule(argument_spec=dict(), supports_check_mode=False)
    ln = LinuxNetwork(module, True)
    res = ln.get_ethtool_data(*args)
    assert res['features']['tx_checksumming'] == 'on'



# Generated at 2022-06-13 01:53:46.746021
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    # Test invocation with dummy module
    module_mock = AnsibleModule(argument_spec={})
    module_mock.run_command = Mock(return_value=(0, "", ""))
    module_mock.get_bin_path = Mock(side_effect=[None, '/bin/ip'])
    network = LinuxNetwork(module=module_mock)
    # Test invocation with valid ip path
    interfaces, ips = network.get_interfaces_info('/bin/ip', {}, {})
    assert len(interfaces) == 0
    assert ips == dict(all_ipv4_addresses=[], all_ipv6_addresses=[])



# Generated at 2022-06-13 01:54:34.508529
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    # TODO: get_default_interfaces is not supported in unit test
    assert True


# Generated at 2022-06-13 01:54:45.917988
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    import platform
    import subprocess
    import os
    module = AnsibleModule(argument_spec={})
    network = LinuxNetwork(module)
    all_eth_devices = [dev.rstrip() for dev in subprocess.check_output(['ls', '-1', '/sys/class/net']).decode().split('\n') if dev.startswith('eth')]
    # get the first two ethernet devices
    eth_devices = all_eth_devices[:2]
    eth_devices_data = {}
    for eth_dev in eth_devices:
        eth_devices_data[eth_dev] = network.get_ethtool_data(eth_dev)
    assert isinstance(eth_devices_data, dict)

# Generated at 2022-06-13 01:54:48.726880
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    connection = Connection(module_name='fake')
    module = Network(connection)
    ln = LinuxNetwork(module)
    assert ln.get_ethtool_data('eth0') == {}



# Generated at 2022-06-13 01:54:54.553407
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    #cmd = '/usr/bin/env ls'
    cmd = '/usr/bin/env cat /etc/aix-release'
    (rc, out, err) = module.run_command(cmd, errors='surrogate_then_replace')
    module.fail_json(rc=rc, out=out, err=err)


# Generated at 2022-06-13 01:55:03.657916
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    network = LinuxNetwork()
    default_ipv4 = {'address': '192.168.2.2', 'interface': 'eth0'}
    default_ipv6 = {'address': '2001:cdba::3257:9652', 'interface': 'eth0'}
    call_result = network.get_default_interfaces(default_ipv4, default_ipv6)
    assert call_result == {'ipv4': {'interface': 'eth0', 'address': '192.168.2.2'},
                           'ipv6': {'interface': 'eth0', 'address': '2001:cdba::3257:9652'}}


# Generated at 2022-06-13 01:55:11.534137
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():

    module = AnsibleModule(
        argument_spec={},
        supports_check_mode=True,
    )
    nm = LinuxNetwork(module)


# Generated at 2022-06-13 01:55:22.114552
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    with tempfile.TemporaryDirectory() as tmpdir:
        module = AnsibleModule(
            argument_spec=dict(
                config=dict(type='str'),
            ),
            supports_check_mode=True,
        )
        module.params['config'] = os.path.join(tmpdir, 'interfaces')

# Generated at 2022-06-13 01:55:32.099530
# Unit test for method get_interfaces_info of class LinuxNetwork

# Generated at 2022-06-13 01:55:43.932187
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    module = AnsibleModule({})
    ln = LinuxNetwork(module)
    default_ipv4, default_ipv6 = ln.get_default_interface()
    interfaces = ln.get_interfaces_info(ln.ip_path, default_ipv4, default_ipv6)
    ln.populate(ln.ip_path, interfaces[0], interfaces[1], default_ipv4, default_ipv6)
    facts = ln.get_facts()
    assert 'default_ipv4' in facts
    assert 'default_ipv6' in facts
    assert 'interfaces' in facts
    assert 'all_ipv4_addresses' in facts
    assert 'all_ipv6_addresses' in facts
    assert len(facts['interfaces']) >= 0

# Generated at 2022-06-13 01:55:45.892219
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    # TODO: add tests for LinuxNetwork.populate(self, current_facts)
    return False

# Generated at 2022-06-13 01:56:29.298909
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    ln = LinuxNetwork()
    ln.run_command = MagicMock(return_value=(0, '''default via 10.0.0.1 dev eth0
10.0.0.0/8 via 10.0.0.1 dev eth0  metric 100
172.16.42.0/24 dev virbr0  proto kernel  scope link  src 172.16.42.1
192.168.122.0/24 dev virbr0  proto kernel  scope link  src 192.168.122.1''', ''))
    ln.get_file_content = MagicMock(return_value='\n')

    default_ipv4, default_ipv6 = ln.get_default_interfaces()

    assert len(ln.run_command.call_args_list) == 2
    assert ln.get_

# Generated at 2022-06-13 01:56:38.484824
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(argument_spec={})

    rc, stdout, stderr = module.run_command(["ip", "-br", "link"])
    devices = [dev.split()[0] for dev in stdout.splitlines()]

    mock_interfaces = {}

# Generated at 2022-06-13 01:56:46.965201
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    rc, command, err = module.run_command('ip -o -0 -4 a | tr 0 "\n"')
    assert rc == 0
    output = command.split('\\000')

    network = LinuxNetwork(module)
    default_ipv4 = {}
    default_ipv6 = {}
    interfaces, ips = network.get_interfaces_info(output, default_ipv4, default_ipv6)
    print(yaml.dump(interfaces, default_flow_style=False))
    print(yaml.dump(ips, default_flow_style=False))
    assert interfaces
    assert isinstance(interfaces, dict)

    # check we parsed all interfaces
    #
    # we don't include lo in the expected results
    actual_interfaces = set(interfaces.keys())
    assert actual_inter

# Generated at 2022-06-13 01:56:51.043486
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    module = AnsibleModule(argument_spec=dict())
    net = LinuxNetwork(module)
    # TODO: fix mocking issue
    data = {}
    assert net.get_ethtool_data(data) == {}



# Generated at 2022-06-13 01:56:59.607661
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    module = FakeModule()
    module.get_bin_path = MagicMock(return_value='/bin/ip')
    module.run_command = MagicMock(return_value=0)
    module.fail_json = MagicMock()


# Generated at 2022-06-13 01:57:07.944226
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    test_object = LinuxNetwork({}, dict())

# Generated at 2022-06-13 01:57:16.235369
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():

    class MockModule:
        def __init__(self, *args, **kwargs):
            self.params = args[0]
            self.result = kwargs['result']

        def get_bin_path(self, *args, **kwargs):
            return "/bin/ip"

        def run_command(self, *args, **kwargs):
            if len(args[0][3]) == 1:
                return 0, testdata[args[0][3][0]], None
            elif args[0][3] == ["eth1"]:
                # for the default address
                return 0, testdata["eth0"], None
            elif args[0][3] == ["eth0"]:
                # for the secondary addres
                return 0, testdata["eth0:1"], None

# Generated at 2022-06-13 01:57:25.501852
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    '''
    Unit test for method get_default_interfaces of class LinuxNetwork
    '''
    import sys
    import os
    import tempfile

    module = sys.modules['ansible.module_utils.basic']
    class Module(object):
        def __init__(self):
            self.module = module
            self.get_bin_path = module.get_bin_path
        def run_command(self, command, errors=None):
            return 0, '', ''
    module = Module()

    tmp_dir = os.path.realpath(tempfile.mkdtemp(prefix='ansible-test-'))

# Generated at 2022-06-13 01:57:28.603287
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    module_args = dict(
        config_file="/etc/sysconfig/network-scripts/ifcfg-eth0",
        running_config="/sbin/ip a show dev eth0",
        running_config_path="/sbin/",
    )
    module = AnsibleModule(argument_spec=module_args)
    network_facts = LinuxNetwork(module)
    network_facts.get_default_interface()
    network_facts.get_interfaces_info()



# Generated at 2022-06-13 01:57:30.468276
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    # Initializing test data
    device = "eth0"

    # Creating an instance of the LinuxNetwork class
    linux_network = LinuxNetwork()
    result = linux_network.get_ethtool_data(device)

    assert True == isinstance(result, dict)

