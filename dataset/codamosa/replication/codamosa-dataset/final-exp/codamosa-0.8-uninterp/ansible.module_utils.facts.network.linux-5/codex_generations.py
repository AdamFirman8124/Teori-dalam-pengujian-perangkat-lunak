

# Generated at 2022-06-13 01:48:48.093221
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    ln = LinuxNetwork()
    devices = ln.get_interfaces()
    assert devices
    for dev in devices:
        features = ln.get_ethtool_data(dev).get('features')
        assert features is None or isinstance(features, dict)
        assert ln.get_ethtool_data(dev).get("timestamping") is None or isinstance(ln.get_ethtool_data(dev).get("timestamping"), list)
        assert ln.get_ethtool_data(dev).get("hw_timestamp_filters") is None or isinstance(ln.get_ethtool_data(dev).get("hw_timestamp_filters"), list)

# Generated at 2022-06-13 01:48:57.614787
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    # TODO: mock run_command to return test data
    # prepare default_ipv4
    default_ipv4 = dict(
        default_route={},
        default_interface={},
        default_address={},
        netmask={},
        broadcast={},
        macaddress={},
    )
    # prepare default_ipv6
    default_ipv6 = dict(
        default_route={},
        default_interface={},
        default_address={},
        prefix={},
        scope={},
        macaddress={},
    )

    # test_get_default_interfaces_v4
    # prepare interfaces

# Generated at 2022-06-13 01:49:08.885709
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    #cannot declare global variables (local?)
    ip_path = '/sbin/ip'
    module_path = '/usr/lib/python2.7/site-packages/ansible/modules'
    module_name = 'system'
    #declare instance and call method
    o = LinuxNetwork(ip_path, module_path, module_name)
    o.populate()

# in order to easily run this test outside of ansible,
# we need to instanciate the module object and call the method
if __name__ == '__main__':
    #define args
    ip_path = '/sbin/ip'
    module_path = '/usr/lib/python2.7/site-packages/ansible/modules'
    module_name = 'system'

    #declare instance and call method
    o = LinuxNetwork

# Generated at 2022-06-13 01:49:18.890490
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    module = AnsibleModule(argument_spec={})
    en = LinuxNetwork(module)
    all_ipv4, all_ipv6, default_ipv4, default_ipv6 = en.get_default_interfaces(ip_path=None)
    assert isinstance(all_ipv4, dict)
    assert isinstance(all_ipv6, dict)
    assert isinstance(default_ipv4, dict)
    assert isinstance(default_ipv6, dict)
    assert isinstance(all_ipv4, dict)
    assert isinstance(all_ipv6, dict)
    assert isinstance(default_ipv4, dict)
    assert isinstance(default_ipv6, dict)

# Generated at 2022-06-13 01:49:20.097623
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    # FIXME: write test
    pass


# Generated at 2022-06-13 01:49:20.911530
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    pass


# Generated at 2022-06-13 01:49:27.803109
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    module = AnsibleModule(argument_spec={})
    linux_network = LinuxNetwork(module=module)
    default_ipv4 = dict()
    default_ipv6 = dict()
    interfaces, ips = linux_network.get_interfaces_info(ip_path='', default_ipv4=default_ipv4, default_ipv6=default_ipv6)
    assert 'lo' in interfaces
    assert 'ipv4_secondaries' in interfaces['lo']
    assert 'lo' in interfaces
    assert 'ipv4_secondaries' in interfaces['lo']
    assert 'lo' in interfaces
    assert 'ipv4' in interfaces['lo']
    assert 'lo' in interfaces
    assert 'ipv6' in interfaces['lo']
    assert 'eth0' in interfaces

# Generated at 2022-06-13 01:49:36.986303
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    from ansible.module_utils import basic
    from ansible.module_utils.facts import is_ipv6
    from ansible.module_utils.facts import get_file_content
    from ansible.module_utils.facts.networking.linux import LinuxNetwork

    addr4 = '172.16.0.30'
    addr6 = '2001:db8::100'

    test_host = LinuxNetwork(dict(module=basic.AnsibleModule(
        argument_spec=dict()
    )))
    test_host.INTERFACE_TYPE = {'1': 'ethernet', '28': 'infiniband'}
    test_host.module.get_bin_path = lambda _: '/sbin/ip'


# Generated at 2022-06-13 01:49:47.880186
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    module = AnsibleModule(argument_spec={})

    if not os.path.exists('/sys/class/net/lo'):
        module.fail_json(msg='missing kernel module?')

    ln = LinuxNetwork(module)


# Generated at 2022-06-13 01:49:51.396412
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    net = LinuxNetwork()
    interfaces, ips = net.get_interfaces_info("ip", {}, {})

    assert isinstance(interfaces, dict)
    assert isinstance(ips, dict)

# Generated at 2022-06-13 01:50:28.558266
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    network = LinuxNetwork()
    assert network.populate()


# Generated at 2022-06-13 01:50:40.617225
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    device = "eth0"
    ethtool_path = 'ethtool'
    commands = {
        'ethtool -k ' + device: "Features for eth0:",
        'ethtool -T ' + device: "PTP Hardware Clock: 0"
    }
    module = MagicMock()
    module.run_command.side_effect = lambda cmd: (0, commands[cmd], '')
    module.get_bin_path.side_effect = lambda cmd: cmd if cmd == ethtool_path else None
    ln = LinuxNetwork(module)

# Generated at 2022-06-13 01:50:52.248669
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    module = Mock()
    network = LinuxNetwork(module)

    def mock_bin_path_func(arg):
        return arg

    module.get_bin_path.side_effect = mock_bin_path_func


# Generated at 2022-06-13 01:50:55.735916
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    module = AnsibleModule(
        argument_spec = dict()
    )

    ln = LinuxNetwork(module)

    assert ln.get_default_interfaces() == "Unknown"


# Generated at 2022-06-13 01:51:07.793116
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    def impl(module_mock, ip_path_mock, default_ipv4, default_ipv6, expected_interfaces, expected_ips, is_stderr):

        data_glob = module_mock.glob.glob

# Generated at 2022-06-13 01:51:16.926959
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    args = {}
    args['fact_path'] = "/usr/share/ansible_plugins/facts/oracle_linux.fact"
    args['module'] = mock.Mock()
    args['module'].params = {}
    args['module'].params['gather_subset'] = ['!all', '!min']
    args['module'].params['gather_network_resources'] = 1
    args['module'].get_bin_path = mock.Mock(return_value='/bin/ip')
    args['module'].run_command = mock.Mock(return_value=(0, '10.0.0.1'))
    args['module'].get_option = mock.Mock(return_value='')

    l = LinuxNetwork(**args)

    ip_path = l.module.get_

# Generated at 2022-06-13 01:51:27.496828
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    mock_module = AnsibleModuleMock()
    mock_module.params = {}

    linux_network = LinuxNetwork(mock_module)


# Generated at 2022-06-13 01:51:34.485769
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    # FIXME: what is this doing?
    import os
    import sys

    sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'lib'))


    from unittest import TestCase

    class LinuxNetwork__get_ethtool_data(TestCase):
        def test_LinuxNetwork_get_ethtool_data(self):
            raise NotImplementedError



# Generated at 2022-06-13 01:51:45.193607
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.connection import Connection
    from ansible_collections.notmintest.not_a_real_collection.plugins.module_utils.network.common import mock

    # FIXME: since this is a closure, it can't mock the outside interface
    # Can we use the jinja2 env or something similar?
    def get_connection():
        conn = Connection(mock.MagicMock())
        conn.get_option = mock.MagicMock(return_value=None)
        conn.get_prompt = mock.MagicMock(return_value=None)
        conn.get_system_hostname = mock.MagicMock(return_value=None)
        return conn


# Generated at 2022-06-13 01:51:55.008382
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    # mock ethtool
    if sys.version_info[0] >= 3:
        # pylint: disable=import-error
        from unittest.mock import patch
    else:
        from mock import patch
    ethtool_bin = '/usr/bin/ethtool'

# Generated at 2022-06-13 01:52:46.262506
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    # setup
    module = MagicMock()
    module.run_command = MagicMock(return_value=(0, "success", ""))
    module.get_bin_path = MagicMock(return_value=True)
    module.params = dict(
        gather_subset=[],
        filter=dict(
        ),
    )

    # execute
    linux_network = LinuxNetwork(module)
    network = linux_network.populate()

    # assert

# Generated at 2022-06-13 01:52:51.614079
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    '''
    Functions that are useful for unit testing.
    '''
    # Output of "ip route"

# Generated at 2022-06-13 01:52:57.108938
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    # Module's params
    module = AnsibleModuleMock(dict(
        config = True,
        running_config = False,
    ))
    # Instance of Network Class
    ni = Network(module)

    # Populate ansible_facts with network information
    ni.populate()

    # Assert the populate method return the correct value for an attribute
    assert ni.module.ansible_facts['ansible_all_ipv4_addresses'] == ['192.168.1.1']
    assert ni.module.ansible_facts['ansible_default_ipv4']['interface'] == 'eth0'



# Generated at 2022-06-13 01:52:59.118697
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    # TODO Assert something
    pass


# Generated at 2022-06-13 01:53:12.114060
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    # This is only executed when the -m option is used in the ansible-playbook command
    module = AnsibleModule(
        argument_spec = dict(),
        supports_check_mode = True
    )
    # Add necessary code here
    result = dict(
        changed=False,
    )
    # mock ip_path
    ln = LinuxNetwork(module)
    mock_ip_path = MagicMock()
    ln.get_bin_path = mock_ip_path
    mock_ip_path.return_value = '/sbin/ip'
    mock_module_run_command = MagicMock()
    module.run_command = mock_module_run_command
    mock_module_run_command.return_value = -1
    mock_ip_path.return_value = None

    # Execute method under

# Generated at 2022-06-13 01:53:19.890237
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():

    net_module = AnsibleModule(argument_spec={})
    net_module.params = {}
    net_module.exit_json = lambda x: x
    net_module.run_command = lambda x: (0, '', '')
    net_module.get_bin_path = lambda x: x
    net_module._socket_path = None  # FIXME: is this still used?
    mock_get_file_content = Mock(return_value='')
    net_module.get_file_content = mock_get_file_content
    mock_get_system_capabilities = Mock(return_value=None)
    net_module.get_system_capabilities = mock_get_system_capabilities
    mock_check_file_is_a_file = Mock(return_value={})
    net_module.check

# Generated at 2022-06-13 01:53:25.472721
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    """ Test for class LinuxNetwork.get_interfaces_info method """


# Generated at 2022-06-13 01:53:34.199939
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    module = AnsibleModule(argument_spec={})
    nm = LinuxNetwork(module)
    IP = namedtuple('IP', ['address', 'prefix'])
    default_ipv4 = IP('10.1.1.1', '24')
    default_ipv6 = IP('fe80::1', '64')
    interfaces, ips = nm.get_interfaces_info('/sbin/ip', default_ipv4, default_ipv6)
    default_ipv4 = default_ipv4._asdict()
    default_ipv6 = default_ipv6._asdict()
    assert interfaces.get('eno1')
    assert interfaces.get('eno1').get('ipv4')

# Generated at 2022-06-13 01:53:45.125618
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    # Mock module
    module = AnsibleModuleMock()
    module.mock_ping = True
    module.mock_ping_path = '/usr/bin/ping'
    module.mock_ip_path = '/sbin/ip'
    module.mock_get_bin_path = {
        'ping': '/usr/bin/ping',
        'ip': '/sbin/ip',
        'ethtool': '/sbin/ethtool'
    }
    module.mock_get_bin_path.update(dict((f, '/usr/local/bin/%s' % f) for f in module.mock_get_bin_path))

# Generated at 2022-06-13 01:53:53.582926
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    import platform
    from ansible.module_utils.basic import get_distribution
    from ansible.module_utils.six import PY3

    kernel = platform.release()
    distro = get_distribution()
    distro_release = platform.linux_distribution()[2]

    # Test 1: if NONEXISTENT directory is given to LinuxNetwork
    # result is localhost network information
    net = LinuxNetwork("NONEXISTENT")
    assert net
    hosts = LinuxHost()
    assert net.default_ipv4 == hosts.default_ipv4
    assert net.default_ipv6 == hosts.default_ipv6

    # Test 2: if None is given to LinuxNetwork
    # result is localhost network information
    net = LinuxNetwork(None)
    assert net
    hosts = LinuxHost()
   

# Generated at 2022-06-13 01:54:44.536667
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    module = AnsibleModule(argument_spec={}, supports_check_mode=True)

    l = LinuxNetwork(module)

# Generated at 2022-06-13 01:54:52.308497
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    mock = MagicMock()
    mock.module = {'get_bin_path': MagicMock(return_value="/path/to/ethtool")}
    e = LinuxNetwork(mock)
    mock.module.run_command = MagicMock(return_value=(0, "", 0))
    assert e.get_ethtool_data("eth0") == {}
    mock.module.run_command.return_value = (1, "", 0)
    assert e.get_ethtool_data("eth0") == {}
    mock.module.run_command.return_value = (0, '''
    Offload parameters for eth0:
    Cannot get device offloads: Operation not supported
    ''', 0)
    assert e.get_ethtool_data("eth0") == {}
    mock.module.run_command.side

# Generated at 2022-06-13 01:55:03.871332
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    expected_result_v4 = {
        'ipv4': {
            'address': '192.0.2.1',
            'broadcast': '192.0.2.255',
            'netmask': '255.255.255.0',
            'network': '192.0.2.0'
        },
        'ipv6': {
            'address': '2001:db8:abc8::4',
            'prefix': '64',
            'scope': 'link'
        }
    }
    expected_result_v6 = {
        'ipv6': {
            'address': '2001:db8:abc8::4',
            'prefix': '64',
            'scope': 'link'
        }
    }
    results_v4, results_v6 = LinuxNetwork.get_default_

# Generated at 2022-06-13 01:55:11.671052
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    obj = LinuxNetwork()
    default_ipv4 = {'address': '192.168.254.254'}
    default_ipv6 = {'address': 'fe80::2'}
    result = obj.get_default_interfaces(default_ipv4, default_ipv6)
    assert result == (
        {'macaddress': '00:50:56:c0:00:08',
         'mtu': 1500,
         'type': 'ethernet'},
        {'macaddress': '00:50:56:c0:00:08',
         'mtu': 1500,
         'type': 'ethernet'}
    )

    # no default ipv6
    default_ipv6 = {}

# Generated at 2022-06-13 01:55:22.235322
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    ln = LinuxNetwork()
    ln.module = AnsibleModule(argument_spec={'type': {'choices': ['all', 'device', 'name'], 'default': 'all'}})
    device = 'e1000'
    ethtool_path = ln.module.get_bin_path("ethtool")
    ethtool_path = "/bin/true"

# Generated at 2022-06-13 01:55:32.173642
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    module = AnsibleModule(
        argument_spec={},
        supports_check_mode=True,
    )
    module.exit_json = Mock(return_value=None)
    module.run_command = Mock(return_value=(0, "", ""))
    module.get_bin_path = Mock(return_value=True)

    observer = PopulateObserver()

# Generated at 2022-06-13 01:55:43.896891
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    test_module = AnsibleModule(argument_spec={})
    test_linux_network = LinuxNetwork(test_module)
    test_default_ipv4 = {'address': '192.0.2.1'}
    test_default_ipv6 = {'address': '2001:db8::64'}
    test_interfaces, ips = test_linux_network.get_interfaces_info(
        "/usr/bin/ip", test_default_ipv4, test_default_ipv6)
    assert 'c' in test_interfaces
    # FIXME: test that this is actually a copy of the content of the
    # default_ipv4 dict (but don't do that by mutating it and expecting it to
    # have mutated)
    assert 'broadcast' in test_interfaces['c']
   

# Generated at 2022-06-13 01:55:55.509150
# Unit test for method populate of class LinuxNetwork

# Generated at 2022-06-13 01:56:03.472561
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    module = AnsibleModule(argument_spec={}, supports_check_mode=True)
    module.exit_json = MagicMock()
    module.run_command = MagicMock()
    test_cases = (
        # test data
        # expected result
        (
            {}, # test data
            {}, # expected result
        ),
    )
    for test_data, expected_result in test_cases:
        module.run_command.return_value = test_data
        network = LinuxNetwork(module)
        network.populate()
        # mock assertion
        # NOTE: this is not implemented
        assert "populate was not written yet" in "populate was not written yet"


# Generated at 2022-06-13 01:56:09.338570
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    # Common test function to check the test cases of get_default_interfaces()
    def check_default_interfaces(test_case, default_interfaces):
        if test_case['test_default_gw']:
            # Assert that default_interfaces['ipv4'] has the right gateway
            assert default_interfaces['ipv4']['gateway'] == test_case['default_gw']
        else:
            assert 'gateway' not in default_interfaces['ipv4']
        if test_case['test_default_addr']:
            # Assert that default_interfaces['ipv4'] has the right ip address
            assert default_interfaces['ipv4']['address'] == test_case['default_addr']

# Generated at 2022-06-13 01:56:55.779291
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    linuxnetwork = LinuxNetwork()
    mocked_module = MagicMock()
    mocked_module.run_command = MagicMock(return_value=(0, '', ''))
    linuxnetwork.module = mocked_module
    linuxnetwork.get_default_interfaces = MagicMock(return_value=({'alias': '', 'macaddress': '', 'mtu': 1500, 'type': 'unknown'}, {}))
    linuxnetwork.get_interfaces_info = MagicMock(return_value=(None, None))
    linuxnetwork.get_routes_data = MagicMock(return_value=(None, None))
    linuxnetwork.get_dns_data = MagicMock(return_value=({}, {}))
    linuxnetwork.get_all_subclasses = MagicMock(return_value=[])
    mocked_module.params

# Generated at 2022-06-13 01:57:06.091875
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    (options, left, right) = parse_cli(["-T"])
    m = ESMock(options)
    mock_to_shell = {
        'ethtool -k persist-control': (0, 'tx-skb-tstamp: off\n', ''),
        'ethtool -T eth0': (0, 'PTP Hardware Clock: 0\n', ''),
    }
    m.register_shell_command_to_result(mock_to_shell, keep_invocation_order=True)
    f = LinuxNetwork(m)

    # run
    result = f.get_ethtool_data('persist-control')
    assert result == {}

    result = f.get_ethtool_data('eth0')

# Generated at 2022-06-13 01:57:14.855929
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():

    #NOTE: iptables and ip6tables commands
    iptables_path = "/sbin/iptables"
    ip6tables_path = "/sbin/ip6tables"

    #NOTE: fake_input will be used as test input
    fake_input = {
        'running_config': {
            'iptables': {
                'v4': [],
                'v6': []
            }
        }
    }

    #NOTE: fake_input will be used as test input
    fake_error = {
        'msg': "some msg",
        'rc': 1
    }

    #NOTE: fake_result will be used as expected result

# Generated at 2022-06-13 01:57:24.917779
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    module = AnsibleModule(argument_spec=dict())
    # NOTE: in the ansible repo, this is implemented as an inner class
    #       as a result, we pass the module ref to the class constructor
    #       so that `self.module` is available to the class
    net = LinuxNetwork(module)
    assert net.get_ethtool_data('lo') == {}

# Generated at 2022-06-13 01:57:29.601434
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    inventory = {}
    module = Mock(params=dict())
    linux = LinuxNetwork()
    if 'default_ipv4' not in inventory:
        inventory['default_ipv4'] = {}
    if 'default_ipv6' not in inventory:
        inventory['default_ipv6'] = {}

    linux.populate(module, inventory)
    assert inventory['default_ipv4']
    assert inventory['default_ipv6']



# Generated at 2022-06-13 01:57:37.779471
# Unit test for method get_interfaces_info of class LinuxNetwork

# Generated at 2022-06-13 01:57:47.951797
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    from ansible.module_utils.common.collections import ImmutableDict
    # TODO: mock out the ethtool_path stuff
    m = MockedModule()
    # TODO: improve upon this fake device
    ln = LinuxNetwork(m, device='em1')

# Generated at 2022-06-13 01:57:59.343091
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    ip_path = '/sbin/ip'
    module = FakeAnsibleModule()
    l = LinuxNetwork(module=module)
    v4, v6 = l.get_default_interfaces(ip_path=ip_path)
    assert v4 == {'interface': 'eth1',
                  'address': '192.168.0.3',
                  'gateway': '192.168.0.1',
                  'netmask': '255.255.255.0',
                  'macaddress': '52:54:00:4e:4f:44'}

# Generated at 2022-06-13 01:58:08.159153
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    module = AnsibleModule(argument_spec=dict(
        test_get_interfaces_info_name=dict(required=True, type='str'),
    ))
    tmp_path = tempfile.mkdtemp()
    test_arg_paths = [
        'interfaces/all_paths',
        'interfaces/no_ipv4_paths/no_ipv4_config_paths',
        'interfaces/no_ipv4_paths/no_ipv4_config_paths',
        'interfaces/no_ipv4_paths/no_ipv4_config_paths',
        'interfaces/no_ipv4_paths/with_ipv4_config_paths/with_ipv4_config_paths',
    ]