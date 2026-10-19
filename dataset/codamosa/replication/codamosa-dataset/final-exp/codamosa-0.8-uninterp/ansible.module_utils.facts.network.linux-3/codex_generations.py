

# Generated at 2022-06-13 01:48:48.841666
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    module_name = 'test_LinuxNetwork_get_default_interfaces'
    default_ip = 'foo'
    ipv4_address = 'bar'
    ipv4_broadcast = 'baz'
    ipv4_netmask = 'qux'
    ipv4_network = 'quux'
    ipv6_address = 'corge'
    ipv6_prefix = 'grault'
    ipv6_scope = 'garply'
    macaddress = 'waldo'
    mtu = 'fred'
    type = 'thud'
    modules = {'ip': module_name}
    mock_path_exists = MagicMock(return_value=True)

# Generated at 2022-06-13 01:48:58.181673
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    return_value_1 = {'v4': {'address': '192.168.0.3', 'interface': 'eth0', 'gateway': '192.168.0.1'}, 'v6': {'address': 'fe80::a00:27ff:fe3f:6f7b', 'interface': 'eth0'}}
    return_value_2 = {'v4': {'interface': 'eth0', 'address': '192.168.0.3', 'gateway': '192.168.0.1'}, 'v6': {'interface': 'eth0', 'address': 'fe80::a00:27ff:fe3f:6f7b'}}
    assert return_value_1 == LinuxNetwork().get_default_interfaces()
    assert return_value_2 == LinuxNetwork().get_default_inter

# Generated at 2022-06-13 01:49:09.404327
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    from ansible.module_utils import basic
    m = basic.AnsibleModule({})
    m.check_mode = False
    p = LinuxNetwork(m)

    class DummyIpFacts(object):

        def get_interfaces_info(self):
            return {
                'eth0': {'type': 'bonding', 'slaves': ['eth1', 'eth2']},
                'eth1': {'type': 'ethernet'},
                'eth2': {'type': 'ethernet'},
                'bond0': {'type': 'bridge', 'interfaces': ['eth0']},
                'br0': {'type': 'bridge', 'interfaces': ['bond0']},
                'vnet0': {'type': 'ethernet'},
            }


# Generated at 2022-06-13 01:49:20.082611
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():

    mock_module = MagicMock()
    mock_module.get_bin_path.return_value = False
    ln = LinuxNetwork(mock_module)
    assert ln.get_ethtool_data('eth0') == {}

    mock_module.get_bin_path.return_value = '/sbin/ethtool'

# Generated at 2022-06-13 01:49:25.107352
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    mock_module = MagicMock()
    mock_grep = MagicMock()
    mock_grep.stdout = 'default via 172.31.1.1 dev eth0'
    mock_module.run_command.return_value = (0, mock_grep, '')

    l = LinuxNetwork(mock_module)

    assert l.get_default_interfaces('') == {
        'v4': {
            'interface': 'eth0',
            'gateway': '172.31.1.1'
        },
    }


# Generated at 2022-06-13 01:49:34.839150
# Unit test for method get_ethtool_data of class LinuxNetwork

# Generated at 2022-06-13 01:49:42.720286
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    module = AnsibleModuleMock()
    # TODO: Maybe mock up /sys/class/net and /proc/net/dev

    # FIXME: this should be taking a filename and returning the contents
    module.get_bin_path = lambda x: ''
    get_file_content = lambda x, y=None: ''

    linux_network = LinuxNetwork(module)

    defn = []
    interfaces, ips = linux_network.get_interfaces_info(defn, {}, {})



# Generated at 2022-06-13 01:49:48.059242
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    module = AnsibleModule(argument_spec=dict())
    args = dict(
        interface_name='enp0s8',
        module=module,
    )
    cmds = dict(
        route='ls',
        ip='ls',
    )
    ln = LinuxNetwork(args)
    v4, v6 = ln.get_default_interfaces()
    assert v4 is None
    assert v6 is None


# Generated at 2022-06-13 01:49:59.887087
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )

    ln = LinuxNetwork(module)

    # test config
    interfaces_info = dict()

# Generated at 2022-06-13 01:50:01.825314
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
  assert False, "Test not implemented"


# Generated at 2022-06-13 01:50:38.263891
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_text
    # Create a module object to hold the module parameters
    module = AnsibleModule(argument_spec={
        'provider': {'type': 'dict', 'options': {'name': {}}}})
    # Create the LinuxNetwork class object
    module._network_os = LinuxNetwork(module)
    device = 'eth0'
    ethtool_path = module.get_bin_path("ethtool")

# Generated at 2022-06-13 01:50:49.981280
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    network_info = LinuxNetwork(dict(module=dict(run_command=mock_run_command), ansible_check_mode=True))


# Generated at 2022-06-13 01:50:55.402078
# Unit test for method populate of class LinuxNetwork

# Generated at 2022-06-13 01:51:03.221103
# Unit test for method get_default_interfaces of class LinuxNetwork

# Generated at 2022-06-13 01:51:08.350066
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    module = AnsibleModule(
        argument_spec=dict(
            device=dict(required=True),
        )
    )
    net = LinuxNetwork(module=module)
    expected = dict(
        features=dict(
            ptp=True,
            tso=True,
            gso=True,
            gro=True,
            lro=True,
            rxvlan=True,
            txvlan=True,
            ntuple=True,
            rxhash=True,
        ),
        timestamping=['all'],
        hw_timestamp_filters=['all'],
        phc_index=0,
    )
    actual = net.get_ethtool_data(module.params['device'])
    assert actual == expected



# Generated at 2022-06-13 01:51:17.361749
# Unit test for method get_ethtool_data of class LinuxNetwork

# Generated at 2022-06-13 01:51:27.530944
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    module = Mock(name="module")
    module.run_command.return_value = [
        0,
        '''default via 192.0.2.1 dev eth0
''',
        ""
    ]
    l = LinuxNetwork(module)
    assert l.get_default_interfaces(), ['eth0']

    module.run_command.return_value = [
        0,
        '''default via ::1 dev eth0
''',
        ""
    ]
    l = LinuxNetwork(module)
    assert l.get_default_interfaces(), ['eth0']

    module.run_command.return_value = [
        0,
        '''default via ::1 dev eth0
default via 192.0.2.1 dev eth0
''',
        ""
    ]
    l = LinuxNetwork(module)
   

# Generated at 2022-06-13 01:51:39.646032
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    # prepare data, will be used as fake input
    class FakeModule:
        @staticmethod
        def get_bin_path(name):
            return 'ethtool'

# Generated at 2022-06-13 01:51:44.311913
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    from ansible_collections.netcommon.plugins.module_utils.network.common.utils import dict_merge

    module = Mock()
    module.get_bin_path = lambda x: x
    module.run_command = lambda x: (0, '', '')
    linux_network = LinuxNetwork(module)

# Generated at 2022-06-13 01:51:47.082999
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    module = AnsibleModule({})
    ln = LinuxNetwork(module=module)
    ln.get_interfaces_info(ip_path='', default_ipv4={}, default_ipv6={})



# Generated at 2022-06-13 01:52:20.878468
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    module = AnsibleModule({})

    class ChdirDoubled:
        def __init__(self, newdir):
            self.newdir = newdir
        def __enter__(self):
            pass
        def __exit__(self, *args):
            pass

    class MockedRunCommand:
        def __init__(self, rc=0, stdout='', stderr=''):
            self.rc = rc
            self.stdout = stdout
            self.stderr = stderr

        def __call__(self, args, errors):
            return (self.rc, self.stdout, self.stderr)

    def test_ethtool_path(self):
        return '/bin/ethtool'


# Generated at 2022-06-13 01:52:31.803813
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    import __main__
    __main__.module = AnsibleModule(argument_spec={})
    # FIXME: this is not a real AnsibleModule!
    network = LinuxNetwork()
    sysfs_path = '/sys/class/net/'
    default_ipv4 = {}
    default_ipv6 = {}
    for filename in os.listdir(sysfs_path):
        path = os.path.join(sysfs_path, filename, 'address')
        if os.path.exists(path):
            macaddress = open(path).read().strip()
            if macaddress != '00:00:00:00:00:00':
                default_ipv4['device'] = filename
                default_ipv6['device'] = filename
                default_ipv4['macaddress'] = macaddress
                default_ip

# Generated at 2022-06-13 01:52:38.958341
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    module = AnsibleModule(
        argument_spec=dict(),
    )

    # FIXME: this should really be tested using a mock,
    # so we don't have a dependency on a running system
    if not os.path.exists('/run/systemd/netif/links'):
        module.exit_json(
            skipped=True,
            msg='LinuxNetwork_get_default_interfaces test requires "systemd".'
        )

    links = LinuxNetwork(module).get_default_interfaces()
    module.exit_json(
        changed=False,
        links=links,
    )



# Generated at 2022-06-13 01:52:49.517329
# Unit test for method get_interfaces_info of class LinuxNetwork

# Generated at 2022-06-13 01:52:56.819517
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    module = AnsibleModule(argument_spec=dict())
    network = LinuxNetwork(module)
    network.populate()

    # Module parameters
    module.fail_json.assert_called_with(msg="argument ip_path is required for this module")

    module = AnsibleModule(argument_spec=dict(ip_path=dict(type='path')))
    network = LinuxNetwork(module)
    network.populate()

    module.fail_json.assert_called_with(msg="argument ip_path is required for this module")

    module = AnsibleModule(argument_spec=dict(ip_path=dict(type='path'), check_invalid_interfaces=dict(type='bool')))
    network = LinuxNetwork(module)
    network.populate()

    check_invalid_interfaces = True
    module = Ansible

# Generated at 2022-06-13 01:53:01.952904
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
  ln = LinuxNetwork(FakeModule())
  ethtool_data = ln.get_ethtool_data('dummy0')

# Generated at 2022-06-13 01:53:05.820895
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    module = AnsibleModule(argument_spec={})
    network = LinuxNetwork(module)
    data = network.get_ethtool_data('lo')
    print(data['features'])


# Generated at 2022-06-13 01:53:17.016437
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    """
    Unit tests for the function get_default_interfaces of the class LinuxNetwork
    """
    module = AnsibleModule(argument_spec={}, supports_check_mode=False)
    if platform.system() != 'Linux' or not HAVE_NETIFACES:
        module.fail_json(msg='Test Module not supported on non-linux platforms')
    options = OPTIONS
    options.update(expand_vars_callback=lambda x: x)
    ln = LinuxNetwork(module, options)
    ip4, ip6 = ln.get_default_interfaces()
    assert type(ip4) is dict
    assert type(ip6) is dict


# Unit tests for method get_interfaces_info of class LinuxNetwork

# Generated at 2022-06-13 01:53:24.331084
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    # create an instance of the class LinuxNetwork to test
    # noinspection PyTypeChecker, PyArgumentList
    os = LinuxNetwork()

    # Strip the common prefix of all keys, so that a simple comparison is possible
    def strip_prefix(d, prefix):
        ret = {}
        for k, v in d.items():
            if k.startswith(prefix):
                ret[k[len(prefix):]] = v
            else:
                ret[k] = v
        return ret

    # define the expected interface dict according to content of test_data_get_interfaces_info

# Generated at 2022-06-13 01:53:32.274149
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    # TODO: mock get_file_content
    # TODO: mock run_command
    # TODO: test all values, not just interface and address
    # TODO: test no error handling
    module = type('module', (object,), {'run_command': mock.DEFAULT})
    network = LinuxNetwork(module)
    network.get_file_content = mock.MagicMock()

    # test empty ipv4 and ipv6 routes
    ipv4_route = []
    ipv6_route = []
    network.get_file_content.side_effect = [ipv4_route, ipv6_route]
    v4, v6 = network.get_default_interfaces()
    assert v4 == {}
    assert v6 == {}
    network.get_file_content.assert_has_calls

# Generated at 2022-06-13 01:54:17.349316
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():

    # Create a sample LinuxNetwork object instance
    linux_network = LinuxNetwork()

    # Provide a sample ethtool command output
    # NOTE: this is not a real sample output
    # its a debiased version of ethtool -k eth0

# Generated at 2022-06-13 01:54:25.605407
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():

    # Initialize the class
    ln = LinuxNetwork()

    # Get the default IPv4 and IPv6
    default_ipv4, default_ipv6 = ln.get_default_interfaces()

    # Get the interfaces that are up
    ip_path = ln.module.get_bin_path("ip")
    interfaces_in, ips = ln.get_interfaces_info(ip_path, default_ipv4, default_ipv6)

    # The actual test
    ln.populate()

    # Check IPv4
    assert ln.interfaces == interfaces_in
    assert ln.ipv4['address'] == '192.168.0.42'
    assert ln.ipv4['netmask'] == '255.255.255.0'

# Generated at 2022-06-13 01:54:29.512901
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    instance = Network()
    device = "lo"
    # FIXME: expand this
    assert instance.get_ethtool_data(device) == {}

# Generated at 2022-06-13 01:54:41.408479
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    module = AnsibleModule(argument_spec={})
    module.exit_json = exit_json
    module.params = {
        'gather_subset': ['all'],
        'gather_network_resources': ['all'],
    }
    network = LinuxNetwork(module)
    rc, gather_facts, changed, msg, facts = network.populate()
    assert rc == 0

# Generated at 2022-06-13 01:54:47.586837
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )

    ln = LinuxNetwork(module)
    interfaces_info = ln.get_interfaces_info()
    module.exit_json(ansible_facts=dict(ansible_net_interfaces=interfaces_info[0]), interface=interfaces_info[0])



# Generated at 2022-06-13 01:54:59.625604
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    # Initialize arguments
    args = dict(
        ip_path='/bin/ip',
    )

    c_obj = LinuxNetwork(None, args)
    c_obj.module.run_command = MagicMock(return_value=(0, "", ""))
    ip_opts = ['-o', '-f', 'inet', 'addr', 'show']

    # Test case 1 - Without any argument
    c_obj.get_default_interfaces()
    assert c_obj.module.run_command.call_count == 2
    args, kwargs = c_obj.module.run_command.call_args_list[0]
    assert args[0] == ip_opts + ['dev', 'lo']

# Generated at 2022-06-13 01:55:03.915535
# Unit test for constructor of class LinuxNetworkCollector
def test_LinuxNetworkCollector():
    facts = dict(
        distribution='Ubuntu',
        platform='Linux',
    )
    # contrived list of options to compare against
    options = dict(
        ansible_data_convergence_timeout=30,
        ansible_facts_cacheable=['!all'],
        ansible_facts_cache_time=3600,
        ansible_facts_gather_timeout=30,
        ansible_get_timeout=10,
        ansible_local_tmp='/tmp/ansible'
    )
    # collect and initialize a LinuxNetworkCollector object
    # Note: any unset options will get the configuration default or module default
    network = NetworkCollector(dict(module=DummyModule, params=options), facts=facts).collect()

    # format the LinuxNetworkCollector object as a dict
    # (this is

# Generated at 2022-06-13 01:55:11.722447
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    module = AnsibleModule(argument_spec={}, supports_check_mode=False)
    l = LinuxNetwork(module)

    # use the docstring from the method as the source for this test
    #   trim the leading spaces off of each line
    source = inspect.getdoc(l.get_interfaces_info).splitlines()
    source = [x.lstrip() for x in source]
    source = '\n'.join(source)
    source = source.strip()

    # test_LinuxNetwork_get_interfaces_info.py is in the same directory as the module.
    #   use that as the template
    path = os.path.join(os.path.dirname(sys.modules['__main__'].__file__), 'test_LinuxNetwork_get_interfaces_info.py')

# Generated at 2022-06-13 01:55:16.996382
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    '''
    Test case for LinuxNetwork.get_ethtool_data
    '''
    module = AnsibleModule(argument_spec={})
    name = 'test'
    data = LinuxNetwork._get_ethtool_data(LinuxNetwork, module, name)
    assert data == {}



# Generated at 2022-06-13 01:55:28.829918
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():

    module = MagicMock()
    module.get_bin_path.return_value = 'ethtool'

    # Setup a mock for the run_command function and set expected values for unit tests.
    # If a command is not in the expected commands, then it is simply returned with rc 0.

# Generated at 2022-06-13 01:56:13.085486
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    module = MockedModule()
    ln = LinuxNetwork(module)
    assert 'interface' not in ln.default_ipv4
    assert 'interface' not in ln.default_ipv6
    assert 'interface' not in ln.interfaces['eth0']
    ln.populate('eth0')
    assert ln.default_ipv4['interface'] == 'eth0'
    assert ln.default_ipv6['interface'] == 'eth0'
    assert ln.interfaces['eth0']['interface'] == 'eth0'
    assert 'address' in ln.interfaces['eth0']



# Generated at 2022-06-13 01:56:24.526877
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    module = AnsibleModule(argument_spec={})
    module.exit_json = exit_json
    module.fail_json = fail_json
    ln = LinuxNetwork(module)

    # default values provided in the module
    assert ln.get_default_interfaces() == (dict(address='127.0.0.1', network='127.0.0.0', netmask='255.0.0.0'), dict(address='::1', network='::', prefix='128'))

    # set default_ipv4 to value found on system
    default_ipv4 = dict(address='192.168.100.100', network='192.168.100.0', netmask='255.255.255.0')
    ln.default_ipv4 = default_ipv4

# Generated at 2022-06-13 01:56:32.994318
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():

    module = AnsibleModule(argument_spec={})
    module.params = {}

    # create an instance and run the function
    mocker = Mocker()
    network = LinuxNetwork(module)
    mock_module = mocker.replace(module)
    mock_module.run_command('ip route list', errors='surrogate_then_replace', check_rc=True)
    mocker.result((0, '169.254.169.254 via 192.168.0.1 dev eth0', ''))
    mock_module.run_command('ip -6 route list', errors='surrogate_then_replace', check_rc=True)

# Generated at 2022-06-13 01:56:41.397582
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    module = AnsibleModule(argument_spec = dict())
    linux_network = LinuxNetwork(module)
    module._ansible_version = '2.5.5'
    module._ansible_no_log = False
    module._ansible_verbosity = 0
    module._ansible_debug = True
    default_ipv4 = dict(address='10.1.1.1')
    default_ipv6 = dict(address='::1')
    ip_path = 'ip'
    interfaces_ipv4, interfaces_ipv6 = linux_network.get_default_interfaces(ip_path, default_ipv4, default_ipv6)
    interfaces, ips = linux_network.get_interfaces_info(ip_path, default_ipv4, default_ipv6)

# Generated at 2022-06-13 01:56:46.894173
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    module = AnsibleModule(argument_spec={})
    module.exit_json = exit_json
    obj = LinuxNetwork(module)
    v4 = {'interface': 'eth0', 'default_gateway': '192.168.56.1'}
    v6 = {'interface': 'eth0', 'default_gateway': '2001:db8::1/64'}
    (v4, v6) = obj.get_default_interfaces()
    assert v4 == v4
    assert v6 == v6



# Generated at 2022-06-13 01:56:52.898338
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    module = AnsibleModule(argument_spec={
        "gather_subset": {"required": False, "type": "list", "default": ["!all", "!min"]},
        "gather_network_resources": {"required": False, "type": "dict"},
    })
    linux = LinuxNetwork(module)
    output = linux.populate()
    assert isinstance(output, dict)



# Generated at 2022-06-13 01:56:59.508848
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    # this test is not being run from the same directory as the module
    # adjust the include path to load the module from its source location
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True)

    ln = LinuxNetwork(module)

    assert ln
    assert ln.get_ethtool_data("enp0s3") == {'features': {}, 'timestamping': [], 'hw_timestamp_filters': []}



# Generated at 2022-06-13 01:57:03.303570
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    # idem (file is not present)
    test_LinuxNetwork = LinuxNetwork()
    interfaces_info = test_LinuxNetwork.get_interfaces_info(None, {}, {})
    assert interfaces_info == ({}, {'all_ipv4_addresses': [], 'all_ipv6_addresses': []}), "Unexpected output of LinuxNetwork.get_interfaces_info"



# Generated at 2022-06-13 01:57:10.293742
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    class FakeModule(object):
        def __init__(self):
            self.run_command_exc = None

        def get_bin_path(self, name):
            return {
                'ip': '/usr/sbin/ip',
                'ethtool': '/usr/sbin/ethtool'
            }.get(name, False)

        def run_command(self, args, errors=None):
            if self.run_command_exc:
                raise self.run_command_exc
            if args == ['/usr/sbin/ip', 'addr', 'show', 'eth0']:
                return 0, IP_ADDR_SHOW_ETH0, ''
            elif args == ['/usr/sbin/ip', '-o', 'addr']:
                return 0, IP_O_ADDR, ''
            el

# Generated at 2022-06-13 01:57:20.078546
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    module = AnsibleModule(argument_spec = dict())
    module.exit_json = exit_json
    class FakeModule(object):
        def __init__(self, *args, **kwargs):
            self.params = {}
            self.exit_json = exit_json
            self.run_command = kwargs.get('run_command', self.fake_run_command)
            self.get_bin_path = kwargs.get('get_bin_path', self.fake_get_bin_path)


# Generated at 2022-06-13 01:58:08.778233
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    mock_module = MockModule([])

    # configures mock module helper
    mock_module.run_command.side_effect = [
        (0, '', ''),
        (0, '', ''),
        (0, '', ''),
        (0, '270', ''),
        (0, '123456', ''),
        (0, '65536', ''),
        (0, '00000000', ''),
        (0, '00000000', ''),
        (0, '0', ''),
    ]

    mock_module.get_bin_path.side_effect = lambda x, required=False, opt_dirs=[] : '/sbin/%s' % x

    mock_module.params = {}

    network = LinuxNetwork(module=mock_module)

    # FIXME: this is lame, we should be

# Generated at 2022-06-13 01:58:20.152254
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    
    def __init__(self):
        self.module = AnsibleModule()
        (os.path, os.path.exists, get_file_content, glob.glob,
         os.path.isdir, os.path.basename, os.readlink,
         os.path.realpath, os.path.join, socket.inet_aton,
         socket.inet_ntoa, struct.pack, struct.unpack) = (None,)*15

    # Mocked methods