

# Generated at 2022-06-13 01:48:38.615931
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    pass


# Generated at 2022-06-13 01:48:45.630460
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    module = AnsibleModule(argument_spec={})
    module.get_bin_path = MagicMock(return_value="/bin/ip")
    module.run_command = MagicMock(side_effect=[(0, "192.168.1.1", ""), (0, "fe80::1", "")])
    networks = LinuxNetwork(module)

    default_ipv4, default_ipv6 = networks.get_default_interfaces()
    assert default_ipv4 == {"address": "192.168.1.1"}
    assert default_ipv6 == {"address": "fe80::1"}


# Generated at 2022-06-13 01:48:56.077370
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    module = AnsibleModule(
        argument_spec=dict(
            gather_subset=dict(default=[], type='list'),
            gather_network_resources=dict(default=None, type='list'),
            use_ipv6=dict(default=True, type='bool'),
            config_file=dict(default='/etc/ansible/facts.d/network.fact'),
        ),
        supports_check_mode=True
    )

    # do not instantiate with our own module
    pop = LinuxNetwork(module)

    # FIXME: mock the network function
    res_dict = pop.populate()

    assert 'interfaces' in res_dict
    assert 'default_ipv4' in res_dict
    assert 'default_ipv6' in res_dict
    assert 'all_ipv4_addresses'

# Generated at 2022-06-13 01:48:57.516529
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
  raise RuntimeError("Unit test not implemented")



# Generated at 2022-06-13 01:49:08.800110
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    module = Mock()
    module.get_bin_path.return_value = True

# Generated at 2022-06-13 01:49:19.423629
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    args = {
        'basedir': '',
        'name': 'test_LinuxNetwork',
    }
    module = NetworkModule(**args)
    ln = LinuxNetwork(module)

    if not os.path.exists('/sys/class/net/lo'):
        # this is probably not Linux
        return

    ip_path = module.get_bin_path("ip")
    if not ip_path:
        # this is probably not Linux, or at least not one we support
        return

    # minimal test to see if network interface names are replaced
    interfaces = {
        'lo': {},
        'eth0:0': {},
        'eth0_0': {},
        'eth0_0_0': {},
        'eth0::0': {},
    }

    # do not want to run

# Generated at 2022-06-13 01:49:25.847405
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    module = AnsibleModule(argument_spec={})
    nm = LinuxNetwork(module)
    default_ipv4, default_ipv6 = nm.execute_system_default_ifconfig_no_pager()
    print("default IPv4: %s" % default_ipv4)
    print("default IPv6: %s" % default_ipv6)
    assert default_ipv4 != {}
    assert default_ipv6 != {}

    interfaces, ips = nm.get_interfaces_info(None, default_ipv4, default_ipv6)
    print("interfaces: %s" % interfaces)
    print("ips: %s" % ips)
    assert interfaces != {}
    assert ips != {}


# Generated at 2022-06-13 01:49:27.959738
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    module = AnsibleModule(argument_spec={})
    linux_network = LinuxNetwork(module)
    device = 'eth0'
    print(linux_network.get_ethtool_data(device))



# Generated at 2022-06-13 01:49:37.115845
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    interface = 'eth0'
    # NOTE: the interface would be mocked elsewhere, but no need here
    m = LinuxNetwork([get_bin_path("ip"), get_bin_path("ethtool")])

# Generated at 2022-06-13 01:49:47.702142
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    dests = [
        ('default via fe80::fceb:abff:fe40:3e42 dev bond0  proto kernel  metric 1024  expires 598sec', ('bond0', 'fe80::fceb:abff:fe40:3e42')),
        ('not default via fe80::fceb:abff:fe40:3e42 dev bond0  proto kernel  metric 1024  expires 598sec', None),
        ('default via 10.65.128.1 dev bond0  proto kernel  metric 1024  expires 593sec', ('bond0', '10.65.128.1'))
        ]
    for test, expected in dests:
        result = LinuxNetwork.get_default_interfaces(test)
        assert result == expected


# Generated at 2022-06-13 01:50:16.744038
# Unit test for constructor of class LinuxNetworkCollector
def test_LinuxNetworkCollector():
    lnc = LinuxNetworkCollector(None)
    lnc.get_facts()
    assert lnc._platform == 'Linux'
    assert lnc._fact_class == LinuxNetwork


# Generated at 2022-06-13 01:50:20.566788
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    module = AnsibleModule({})
    ln = LinuxNetwork(module)
    result = ln.get_interfaces_info("",
                                    {"address": "192.168.1.1"},
                                    {"address": "ff80::1"})
    assert True



# Generated at 2022-06-13 01:50:24.534413
# Unit test for constructor of class LinuxNetworkCollector
def test_LinuxNetworkCollector():
    module = AnsibleModule(argument_spec={})
    collector = LinuxNetworkCollector(module)
    assert collector.platform == 'Linux'
    assert collector.required_facts == set(['distribution', 'platform'])
    assert collector._fact_class == LinuxNetwork

# Unit tests for LinuxNetwork class

# Generated at 2022-06-13 01:50:36.401617
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    module = AnsibleModule(argument_spec={}, supports_check_mode=True)
    set_module_args(dict())

    # Create instance of NetworkCollector.
    network = LinuxNetwork(module)

    # Test ethtool features.
    rc = 0

# Generated at 2022-06-13 01:50:47.669844
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    # This is a dict of dicts, keyed by device name, with address and
    # interface found in the output of ip address
    interface_data = {
        'docker0': {
            'address': '172.17.0.1',
            'interface': 'docker0'
        },
        'lo': {
            'address': '127.0.0.1',
            'interface': 'lo'
        },
        'ens3': {
            'address': '1.2.3.4',
            'interface': 'ens3'
        }
    }
    ip_path = 'ip'
    default_ipv4 = {}
    default_ipv6 = {}

# Generated at 2022-06-13 01:50:58.641846
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    """Unit tests for LinuxNetwork.populate()"""
    module = AnsibleModule({
        'bootproto': 'static',
        'ipaddr': '192.168.0.1',
        'netmask': '255.255.255.0',
        'gateway': '192.168.0.254',
        'network': '192.168.0.0',
        'debug': True,
    })

    # NOTE: This is a hack to work around a bug in the functional tests
    # and is ignored when running this module in Ansible itself:
    # https://github.com/ansible/ansible/issues/27963
    LOG_PATH = "/tmp/ansible_network_module.log"

    # NOTE: This is another hack to work around a bug in the
    # functional tests and is ignored when running this module


# Generated at 2022-06-13 01:51:02.063302
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    from ansible.module_utils import basic
    module = basic.AnsibleModule(
        argument_spec={},
        supports_check_mode=True,
        bypass_checks=True,
    )
    network = LinuxNetwork(module)
    module.exit_json(**network.get_interfaces_info())



# Generated at 2022-06-13 01:51:06.336522
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    # Create a Network module object
    network = LinuxNetwork()

    # Check that result of populating is identical with expected
    assert not network.populate()



# Generated at 2022-06-13 01:51:15.918904
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    # Create an instance of our class
    module = AnsibleModule(argument_spec={}, supports_check_mode=True)
    ln = LinuxNetwork(module)
    # Use a known fqdn where we can control the response
    module._socket_path = os.path.join(os.path.dirname(__file__), "dns")
    # Verify that if no interfaces are on the host, an empty result is returned
    interfaces, ips = ln.populate()
    assert interfaces == {}
    assert ips['default_ipv4'] == {}
    assert ips['default_ipv6'] == {}
    # Verify that if only a lo interface is present, it is in the results, but
    #   default IPs are not
    interfaces, ips = ln.populate(['lo'])

# Generated at 2022-06-13 01:51:26.710498
# Unit test for method get_ethtool_data of class LinuxNetwork

# Generated at 2022-06-13 01:52:02.472874
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    module = AnsibleModule({})
    # AnsibleModule.run_command always streams output to stdout so,
    # AnsibleModule.run_command(args, errors='surrogate_then_replace')
    # will (in test environment) always return stdout and empty stderr.
    # Since get_interfaces_info uses AnsibleModule.run_command(args)
    # its output is captured by stdout and stderr but never checked.
    # We could return dummy data to stderr so that test_get_interfaces_info
    # checks the correct value but stdout will still containg the output
    # of the command which we can omit.
    #
    # patch_obj is a mock.patch object, see:
    # https://docs.python.org/3/library/unittest.mock.html#

# Generated at 2022-06-13 01:52:12.156601
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    module_args = dict(
        device='eth0',
    )
    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)
    network = LinuxNetwork(module)

# Generated at 2022-06-13 01:52:21.282341
# Unit test for method get_interfaces_info of class LinuxNetwork

# Generated at 2022-06-13 01:52:32.463597
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    module = MagicMock()
    module.get_bin_path.return_value = "/usr/bin/ethtool"
    l = LinuxNetwork(module)
    rc, stdout, stderr = (0, "off", "")
    module.run_command.return_value = (rc, stdout, stderr)
    assert l.get_ethtool_data("eth0") == {'features': {'rx_checksumming': 'off'}}

    rc, stdout, stderr = (1, "stdout", "stderr")
    module.run_command.return_value = (rc, stdout, stderr)
    assert l.get_ethtool_data("eth0") == {}


# Generated at 2022-06-13 01:52:40.732660
# Unit test for method get_interfaces_info of class LinuxNetwork

# Generated at 2022-06-13 01:52:49.685194
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    m = LinuxNetwork()
    args = ['ls', '-l', '/sys/class/net/lo']
    rc, stdout, stderr = m.module.run_command(args, errors='surrogate_then_replace')
    if rc == 0:
        args = ['/sbin/ethtool', '-k', 'lo']
        rc, stdout, stderr = m.module.run_command(args, errors='surrogate_then_replace')
        if rc == 0:
            print(json.dumps(m.get_ethtool_data('lo'), ensure_ascii=True, sort_keys=True, indent=4, separators=(',', ': ')))


# Generated at 2022-06-13 01:52:52.630607
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    module = AnsibleModule(
        argument_spec=dict(
            config=dict(type='dict', default={}),
        ),
    )
    config = dict(foo='bar')
    l = LinuxNetwork(module)
    l.populate(config)
    assert module.params['config'] == config


# Generated at 2022-06-13 01:52:58.149581
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    mac = 'FF:EE:DD:CC:BB:AA'
    module = AnsibleModule(argument_spec={})
    module.run_command = MagicMock()

    ifaces_paths = ('/sys/class/net/a/b', '/sys/class/net/b/c', '/sys/class/net/c/d')
    module.run_command.return_value = (0, '', '')

    def mock_glob(path):
        return ifaces_paths

    mock_isfile = MagicMock()
    mock_isfile.return_value = True
    mock_isdir = MagicMock()
    mock_isdir.return_value = True


# Generated at 2022-06-13 01:53:11.704641
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(
        argument_spec={},
    )

    interface_res_keys = [
        'macaddress', 'mtu', 'promisc', 'type', 'device', 'active', 'module',
        'pciid', 'speed', 'features', 'timestamping', 'hw_timestamp_filters',
        'phc_index',
    ]

    ln = LinuxNetwork(module)

    # test get_interfaces_info with a simple mocked ip command

# Generated at 2022-06-13 01:53:19.418839
# Unit test for method get_ethtool_data of class LinuxNetwork

# Generated at 2022-06-13 01:53:52.546402
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    # Arrange

    # Create a test module
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule({}, {})

    # Construct a LinuxNetwork object, with stubbed out
    # methods, and properties.
    ln = LinuxNetwork(module)

    get_file_content = lambda path, default=None: "/sys/class/net/eth0/mtu"
    ln.get_file_content = get_file_content

    # Act
    result = ln.populate()

    # Assert
    assert result['interfaces']['eth0']['mtu'] == 1500
# end of method unit test


# Generated at 2022-06-13 01:53:57.762154
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():

    class TestModule(object):
        def get_bin_path(self, cmd, opt_dirs=[]):
            return '/bin/ethtool'


# Generated at 2022-06-13 01:54:03.964870
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    # change working dir to path of this file for testing
    os.chdir(os.path.dirname(__file__))

    def clean_any_dict_attr(data):
        for k, v in data.items():
            if isinstance(v, dict):
                data[k] = clean_any_dict_attr(v)
            if isinstance(v, list):
                data[k] = [clean_any_dict_attr(i) for i in v]
            if k.startswith('_') or k in ('ansible_facts', 'ansible_module_args'):
                del data[k]
        return data

    # FIXME: a test that doesn't need to run on *real* hardware would be nice

    # this is the dict that will be used to fake a module

# Generated at 2022-06-13 01:54:07.111853
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    m = AnsibleModule({})
    m.get_bin_path = lambda x: '/usr/bin/'+x
    l = LinuxNetwork(m)

    assert l.get_ethtool_data("test") == {}
    assert l.get_ethtool_data("test") == {}
    assert l.get_ethtool_data("test") == {}
    assert l.get_ethtool_data("test") == {}



# Generated at 2022-06-13 01:54:12.764581
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    # instantiate an empty module, with a fake self.module in the arguments
    module = type('FakeModuleForLinuxNetwork', (), dict(run_command=lambda *_, **__: (0, '', ''), get_bin_path=lambda *_, **__: None))
    network = LinuxNetwork(module)

    # test_with_ipv6_no_ipv4_addresses_no_interfaces_in_ifcfg
    interfaces, ips = network.get_interfaces_info(None, {}, {'address': 'fe80::a00:27ff:fe58:8b9a', 'type': 'ether'})
    assert interfaces == {}
    assert ips == dict(all_ipv4_addresses=[], all_ipv6_addresses=[])

    # test_with_ipv6_ipv

# Generated at 2022-06-13 01:54:18.150610
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    ln = LinuxNetwork()

    interfaces, ips = ln.get_interfaces_info(None, {}, {})

    assert type(interfaces) == dict
    list_interfaces_key = list(interfaces.keys())
    if 'lo' in list_interfaces_key:
        list_interfaces_key.remove('lo')
    device = list_interfaces_key[0]
    assert device == interfaces[device]['device']
    assert 'ipv4' in interfaces[device]
    if 'ipv6' in interfaces[device]:
        assert 'address' in interfaces[device]['ipv6'][0]
        assert 'prefix' in interfaces[device]['ipv6'][0]
        assert 'scope' in interfaces[device]['ipv6'][0]

# Generated at 2022-06-13 01:54:25.695076
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes
    import sys
    import os

    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'network_dummy_data')
    sys.path.insert(0, path)
    from get_ethtool_dummy_data import get_ethtool_dummy_data

    class TestModule(object):
        def __init__(self):
            return

        def get_bin_path(self, name):
            return 'ethtool'

        def run_command(self, args, **kwargs):
            return get_ethtool_dummy_data(' '.join(args), **kwargs)


# Generated at 2022-06-13 01:54:38.503306
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():

    class AboutToDieModule(AnsibleModule):
        '''AnsibleModule wrapper for unit testing'''

# Generated at 2022-06-13 01:54:49.481900
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    m = AnsibleModuleMock(LinuxNetwork)
    m.get_bin_path.return_value = '/usr/sbin/ethtool'

    # ethtool should be found
    assert LinuxNetwork(m).get_ethtool_data('device') == {}


# Generated at 2022-06-13 01:54:52.829155
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    m = LinuxNetwork()
    r = m.get_ethtool_data('eth0')
    assert isinstance(r, dict)
#
# ===========================================
# Subclass, distro dependent utils
#



# Generated at 2022-06-13 01:55:30.971438
# Unit test for method get_interfaces_info of class LinuxNetwork

# Generated at 2022-06-13 01:55:32.504396
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    assert LinuxNetwork(None).get_ethtool_data('eth0') == {}


# Generated at 2022-06-13 01:55:44.144597
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():

    # Mock module
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=False
    )

    # Mock command_retrieve
    def command_retrieve(cmd):
        if cmd == 'ip route get 8.8.8.8':
            return {
                'stdout': '8.8.8.8 via 10.0.0.1 dev eth0 src 10.0.0.2 metric 100',
                'stderr': '',
                'rc': 0,
                'changed': False
            }

# Generated at 2022-06-13 01:55:51.738258
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    ln = LinuxNetwork()
    ln.module = MagicMock()
    ln.module.run_command = MagicMock(return_value=(0, "default via 192.168.1.1 dev eth0  proto static  metric 1024\n", ""))
    dif = ln.get_default_interfaces()
    assert dif['v4']['interface'] == 'eth0'
    assert dif['v4']['gateway'] == '192.168.1.1'



# Generated at 2022-06-13 01:56:00.179347
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    obj = LinuxNetwork()

# Generated at 2022-06-13 01:56:04.883661
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():

    module = Mock(params={})
    linux_network = LinuxNetwork(module)


# Generated at 2022-06-13 01:56:12.938553
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():

    # NOTE: This changes the state of the system, so the test should be
    #       performed within a virtual machine or container.

    class ModuleMock(object):
        class RunCommandMock(object):
            class stdout(object):
                pass
        def __init__(self):
            self.run_command = self.RunCommandMock()
        def get_bin_path(self, path):
            return path
    module = ModuleMock()

    linux = LinuxNetwork(module)

    linux.populate('interfaces')



# Generated at 2022-06-13 01:56:14.589619
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    # No need to check with LinuxNetwork(None)
    assert False


# Generated at 2022-06-13 01:56:25.557630
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    from collections import namedtuple
    # Mock class for the module object
    module = namedtuple('FakeModule', ['get_bin_path', 'run_command'])
    module.get_bin_path.return_value = '/bin/ip'

    # Mock for the ip command output

# Generated at 2022-06-13 01:56:33.836759
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    module = LinuxNetwork()

    v4_output = """0.0.0.0         10.12.1.1       0.0.0.0         UG    100    0        0 eth0
    10.12.1.0      *               255.255.255.0   U     100    0        0 eth0"""
    v4_result = {'device': 'eth0', 'broadcast': '10.12.1.255', 'address': '10.12.1.1', 'netmask': '255.255.255.0', 'network': '10.12.1.0'}
    assert module.get_default_interfaces(v4_output, default_ipv4={}) == (v4_result, {})


# Generated at 2022-06-13 01:57:30.059433
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    module = mock.MagicMock(
        get_bin_path=lambda x: 'get_bin_path_mock',
        run_command=lambda x: (0, 'run_command_mock', 'mock_stderr'),
    )
    module.params = {}

    ln = LinuxNetwork(module)
    ln.populate()
    assert ln.module == module
    assert ln.ip_path == 'get_bin_path_mock'
    assert ln.default_ipv4 == {}
    assert ln.default_ipv6 == {}
    assert ln.version == {}
    assert ln.release == {}
    assert ln.distribution == {}
    assert ln.interface_driver == {}
    assert ln.sysconfig == {}

# Generated at 2022-06-13 01:57:38.650423
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    test = LinuxNetwork({})

# Generated at 2022-06-13 01:57:48.616083
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    module = AnsibleModule(argument_spec={})
    module.HAS_PARAMIKO = False
    module.HAS_NET_IFACES = False
    module.SUDO_EXE = ''
    module.SUDO_FLAGS = []
    module.params = {}
    module.params['purge'] = False
    module.check_mode = True
    module.exit_json = lambda a: a
    module.run_command = lambda cmd, **kwargs: (0, '', '')

    ln = LinuxNetwork(module)
    assert ln.get_ethtool_data('lo') == {}


# Generated at 2022-06-13 01:57:59.937467
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    from ansible.module_utils import basic
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.connection import Connection
    from ansible.module_utils.network.common.utils import dict_merge

    module = AnsibleModule(argument_spec={})
    module.params = {}

    connection_class_mock = Connection(module._socket_path)
    connection_class_mock.get_connection_type = mock.Mock()
    connection_class_mock.get_connection_type.return_value = 'network_cli'
    connection_class_mock.get_default_network_os = mock.Mock()
    connection_class_mock.get_default_network_os.return_value = 'linux'
    connection_class_mock.get_network_os

# Generated at 2022-06-13 01:58:08.634778
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    m_inst = Mock(spec=AnsibleModule)
    m_inst.get_bin_path.return_value = '/usr/sbin/ethtool'

    m = {'run_command.side_effect': [
        (0, 'a: b\n', ''),
        (0, 'a: b\n', ''),
        (1, '', 'ethtool: unrecognized option \'--a\''),
    ]}
    with mock.patch.multiple(m_inst, **m):
        n = LinuxNetwork(m_inst)
        assert n.get_ethtool_data('eth0') == {'a': 'b'}
        assert n.get_ethtool_data('eth0') == {'a': 'b'}
        assert n.get_ethtool_data('eth0') is None



# Generated at 2022-06-13 01:58:19.917726
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    # init object
    module = MockModule()
    l = LinuxNetwork(module)

    # patch with_ethtool
    l.with_ethtool = True

    # patch ethtool_path
    l.module.get_bin_path = Mock(return_value='/sbin/ethtool')

    # patch run_command
    def run_command_side_effect(*args, **kwargs):
        if 'timestamping' in args[0]:
            return 0, 'SOF_TIMESTAMPING_TX_SOFTWARE       SOF_TIMESTAMPING_RX_SOFTWARE       SOF_TIMESTAMPING_SOFTWARE', ''