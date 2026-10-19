

# Generated at 2022-06-13 01:48:47.397362
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    # We only test the logic around the default IPv4 interface, we don't need to
    # test for default IPv6 interface since it is the same code.

    # Tests for an interface that is part of a bridge
    br0 = {'interfaces': ['eth0'], 'type': 'bridge', 'ipv4': {'address': '192.168.1.1', 'netmask': '255.255.255.0', 'broadcast': '192.168.1.255', 'network': '192.168.1.0'}}
    eth0 = {'type': 'ethernet'}
    eth1 = {'type': 'ethernet'}
    interfaces = {'br0': br0, 'eth0': eth0, 'eth1': eth1}

# Generated at 2022-06-13 01:48:57.025826
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():

    # test with no output of ip...
    module_args = {'gather_subset': ['network'], 'gather_timeout': 30}
    module = AnsibleModule(argument_spec={}, supports_check_mode=True, **module_args)
    m_run_command = MagicMock(return_value=(0, '', ''))
    module.run_command = m_run_command
    m_get_bin_path = MagicMock(return_value='/bin/ip')
    module.get_bin_path = m_get_bin_path

    # create LinuxNetwork object
    ln = LinuxNetwork(module)
    # get interfaces info
    interfaces, ips = ln.get_interfaces_info('ip', {}, {})

    # expected interfaces empty dict
    exp_interfaces = {}
   

# Generated at 2022-06-13 01:48:59.078382
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    m = AnsibleModule()
    ln_obj = LinuxNetwork(m)
    assert ln_obj.get_interfaces_info(None, None, None)

# Generated at 2022-06-13 01:49:10.116293
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    module = AnsibleModule(argument_spec=dict(test_output=dict(type='dict', default=dict())))
    n = LinuxNetwork(module)

    # Test network device name filter
    default_ipv4 = dict(address='10.0.0.1')
    default_ipv6 = dict(address='2001:db8::1')
    # test_network_devices is just a reference to module.params.test_output
    test_network_devices = module.params.get('test_output', dict())

# Generated at 2022-06-13 01:49:20.584158
# Unit test for constructor of class LinuxNetworkCollector
def test_LinuxNetworkCollector():
    res = LinuxNetworkCollector._fact_class(None)
    assert res is not None
    assert dir(res) == ['_get_dhcpv6_info',
                        '_get_dist_interfaces_info',
                        '_get_interfaces_from_ip',
                        '_get_interfaces_info',
                        'get_dist_interfaces_info',
                        'get_interfaces_info',
                        'get_interfaces_from_ip',
                        'get_default_interfaces',
                        'get_default_interface_from_route']
    assert res.get_dist_interfaces_info() == {}
    assert res.get_interfaces_from_ip() == ({}, {})
    assert res.get_interfaces_info() == ({}, {})

# Generated at 2022-06-13 01:49:27.457725
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():

    class MockModule(object):
        def __init__(self, params):
            self.params = params

        def get_bin_path(self, path, opt_dirs=None):
            return None

    class MockSubprocess(object):
        def __init__(self, commands):
            self.commands = commands

        def CalledProcessError(self, rc, out, err):
            return None

        def run_command(self, args, errors='surrogate_then_replace'):
            if args[1] == '-4':
                return self.commands['v4']
            else:
                return self.commands['v6']

    # case 1
    # FIXME: this is a bit too simple, not covering all of the code
    module = MockModule({})

# Generated at 2022-06-13 01:49:36.756058
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    # Dummy values for global variables in module
    l = dict(
        module=dict(
            get_bin_path=lambda x: None,
        )
    )
    ansible_facts = dict(
        ansible_net_interfaces={},
        ansible_net_all_ipv4_addresses=[],
        ansible_net_all_ipv6_addresses=[],
    )
    ln = LinuxNetwork(l, ansible_facts)
    facts = ln.populate()
    assert isinstance(facts, dict)
    assert ['ansible_net_gather_subset'] == list(facts.keys())
    assert isinstance(facts['ansible_net_gather_subset'], list)
    assert 1 == len(facts['ansible_net_gather_subset'])


# Generated at 2022-06-13 01:49:43.824426
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    module = AnsibleModule(argument_spec=dict(
        name=dict(type='str', required=True),
    ))
    ln = LinuxNetwork(module)
    device = 'lo'
    module.add_network_root_path('/sys/class/net/{0}'.format(device))
    result = ln.get_ethtool_data(device)
    pprint(result)
    assert result == dict()



# Generated at 2022-06-13 01:49:50.875136
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    class mock_module(object):
        def __init__(self):
            self.fail_json = None
            self.exit_json = None
            self.warn = None

        def get_bin_path(self, name):
            return '/bin/' + name

        def run_command(self, cmd, errors='strict'):
            return 0, '', ''

    ln = LinuxNetwork()
    ln.module = mock_module()
    ln.get_interfaces_info(None, None, None)



# Generated at 2022-06-13 01:50:02.873067
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    from ansible.module_utils import basic

    results = {}

# Generated at 2022-06-13 01:50:47.565652
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    class MockModule:
        def get_bin_path(self, _):
            return True
        def run_command(self, *args, **kwargs):
            if args == (['ip', 'route', 'show', 'default'],):
                return (0, 'default via 192.0.2.1 dev eth0\n', '')
            elif args == (['ip', '-6', 'route', 'show', 'default'],):
                return (0, 'default via 2001:db8::1 dev eth0\n', '')
            elif args == (['ip', '-6', 'route', 'show', 'default'],):
                return (0, '', 'IPv6: ADDRCONF(NETDEV_UP): eth0: link is not ready')

    module = MockModule()
    default_ipv

# Generated at 2022-06-13 01:50:57.913632
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    module = AnsibleModule(argument_spec={})
    module.params['ip_path'] = '/bin/ip'
    module.params['default_ipv4'] = {}
    module.params['default_ipv6'] = {}
    network = LinuxNetwork(module)
    ip_path = module.params['ip_path']
    default_ipv4 = module.params['default_ipv4']
    default_ipv6 = module.params['default_ipv6']
    network.get_default_interfaces(ip_path, default_ipv4, default_ipv6)
    assert module.params['default_ipv4'] == {}
    assert module.params['default_ipv6'] == {}


# Generated at 2022-06-13 01:51:10.432135
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    """
    unit test of LinuxNetwork.populate
    """
    module = AnsibleModule(argument_spec={})
    network = LinuxNetwork(module)
    network.default_ipv4, network.default_ipv6 = network.get_default_interfaces()
    network.bootproto = 'static'
    network.ipv4['address'] = '192.168.5.5'
    network.ipv4['netmask'] = 24
    network.ipv4['gateway'] = '192.168.5.1'

    # NOTE: the assertions in this test should probably be improved.
    # This test should be re-written when is_valid_ipv6 is made more robust.

# Generated at 2022-06-13 01:51:22.914500
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    """
    test get_default_interfaces
    """
    class MockModule:
        def __init__(self):
            self.params = dict()

        def run_command(self, args, errors='surrogate_then_replace'):
            if self.params['out'] == "Default route via gateway 10.0.0.1 on interface eth0 with src 10.0.0.10":
                return 0, self.params['out'], ''
            elif self.params['out'] == "":
                return 0, '', ''
            else:
                return 0, self.params['out'], ''

        def get_bin_path(self, arg):
            return arg


# Generated at 2022-06-13 01:51:30.538123
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    import doctest
    import sys
    import platform
    from unittest import mock
    import ansible.module_utils.basic
    import ansible.module_utils.six

    # Hack to keep the tests running on Python 2, where we can't generate a
    # temporary module.
    #
    # The `with` block syntax only exists in Python 2.6; earlier versions
    # will raise a SyntaxError.
    #
    # The `get_file_content` function in the Utils class only works if the
    # module is constructed as a temporary module.
    #
    # The `StringIO` function only exists in Python 2, where we want to
    # raise an exception because the import of `io` from the standard
    # library will fail.
    if sys.version_info.major == 2:
        doctest.testmod

# Generated at 2022-06-13 01:51:42.508249
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    """Test case for method :meth:`LinuxNetwork.get_default_interfaces` of the class :class:`LinuxNetwork`

    """
    os.environ['PATH'] = '/usr/sbin'

    # TODO: find a test scenario where default_ipv4['network'] is not None
    default_ipv4 = {'address': None, 'broadcast': None, 'network': None, 'netmask': None}
    default_ipv6 = {'address': None, 'prefix': None, 'scope': None}

    # Arrange
    import tempfile
    temp_dir_obj = tempfile.TemporaryDirectory()
    temp_dir = temp_dir_obj.name

    arp_file = temp_dir + '/arp'
    with open(arp_file, 'w') as af:
        af.write

# Generated at 2022-06-13 01:51:48.187131
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    module = AnsibleModule(argument_spec={}, supports_check_mode=False)
    ln = LinuxNetwork(module)
    default_ipv4 = dict()
    default_ipv6 = dict()
    r = ln.get_interfaces_info('/sbin', default_ipv4, default_ipv6)
    assert r is not None
    assert default_ipv4 is not None
    assert default_ipv6 is not None



# Generated at 2022-06-13 01:51:58.259037
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    # Initialize class
    network = LinuxNetwork()
    network.module = ansible_module
    network.INTERFACE_TYPE = LinuxNetwork.INTERFACE_TYPE
    # state: defaults to 'present'

    # interfaces: defaults to {}
    interfaces = {}
    # i is a dict key (string) not an index int
    for i in interfaces:
        if ':' in i:
            new_interfaces[i.replace(':', '_')] = interfaces[i]
        else:
            new_interfaces[i] = interfaces[i]
    # ips: defaults to {}
    ips = {}
    # ip_path: deprecated
    ip_path = None

    # bridge_parameters: defaults to None
    bridge_parameters = None

    # bond_parameters: defaults to None
    bond_parameters = None

# Generated at 2022-06-13 01:52:02.308487
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    with exit_json.ensure_cleanup(module, default_ipv4, default_ipv6, interfaces, success=True):
        exit_json({
            "ipv4": default_ipv4,
            "ipv6": default_ipv6,
            "interfaces": interfaces,
        })



# Generated at 2022-06-13 01:52:11.983146
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():

    class MockModule(object):

        @staticmethod
        def run_command(args, **kwargs):
            output = dict(
                (1, (1, "no device valid\n", "")),
                (2, (0, "Features for devices:", "")),
                (3, (0, "Features for eth0:", "")),
                (4, (0, "", "/usr/sbin/ethtool: "))
            )[args[-1]]
            return output

        @staticmethod
        def get_bin_path(binary):
            return binary

    class MockCall(object):
        @staticmethod
        def fail_json(msg, **kwargs):
            raise AssertionError(msg)

    module = MockModule()
    call = MockCall()


# Generated at 2022-06-13 01:52:55.045550
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    module = AnsibleModule(argument_spec=dict())
    linux_net = LinuxNetwork(module)
    ipv4_expected = dict(
        address='172.29.121.28',
        broadcast='172.29.121.255',
        netmask='255.255.255.128',
        network='172.29.121.0',
        gateway='172.29.121.129',
        interface='en1'
    )
    ipv6_expected = dict(
        address='fe80::a00:27ff:fe84:6ebe',
        gateway='fe80::1',
        interface='en1'
    )
    ipv4_result, ipv6_result = linux_net.get_default_interfaces()
    assert ipv4_expected == ipv4_result
    assert ipv6

# Generated at 2022-06-13 01:53:07.299572
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    class FakeModule(object):
        run_command = lambda x, y, **kwargs: (0, '', '')
        get_bin_path = lambda x, y, **kwargs: 'foo'

    module = FakeModule()
    linux_network = LinuxNetwork(module)
    network_facts = {}
    linux_network.populate(network_facts)
    assert network_facts['default_ipv4']['address'] == '127.0.0.1'
    assert network_facts['default_ipv4']['netmask'] == '255.0.0.0'
    assert network_facts['default_ipv4']['network'] == '127.0.0.0'
    assert network_facts['default_ipv4']['broadcast'] == '127.255.255.255'
   

# Generated at 2022-06-13 01:53:18.725161
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    obj = LinuxNetwork({}, {}, {})

# Generated at 2022-06-13 01:53:25.350472
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    from ansible import context
    from ansible.module_utils.common.text.converters import to_text
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(
        argument_spec=dict()
    )

    ################################################################################################
    # get_interfaces_info()

    # TODO make this a mock so the heavy lifting is done in the test cases

    module_data = {'params': {'ansible_facts': {}}}
    module_data['params']['ansible_facts']['ansible_ethtool'] = {}

    # add data from module_utils.network
    netinfo = LinuxNetwork(module)

# Generated at 2022-06-13 01:53:32.604877
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    """ Unit test for method get_interfaces_info of class LinuxNetwork """
    # dummy class
    class module(object):
        def __init__(self):
            self.run_command = Mock(return_value=(0, "", ""))
        def get_bin_path(self, name):
            return "/sbin/%s" % name
    # call tested method
    ln = LinuxNetwork(module())
    rc = ln.get_interfaces_info("", {}, {})
    # check result
    assert rc[0] == {} and rc[1] == {'all_ipv4_addresses': [], 'all_ipv6_addresses': []}


# Generated at 2022-06-13 01:53:43.822008
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    # FIXME: this test is somewhat weak, we should make it stronger

    class FakeModule(object):
        @staticmethod
        def get_bin_path(name):
            # TODO: mock find_executable to make this test better
            return os.path.realpath(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'bin', name))

        def run_command(self, cmd, errors=None):
            assert cmd[0] == self.get_bin_path('ip')
            # TODO: mock run_command to make this test better
            # (or maybe just mock the real ip command?)

# Generated at 2022-06-13 01:53:52.798739
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    module = AnsibleModule(argument_spec={})
    # FIXME: stubs, how to do this better?
    module.get_bin_path = lambda name: name

# Generated at 2022-06-13 01:53:57.306864
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    module = AnsibleModule()
    linux_network = LinuxNetwork(module)
    result = linux_network.get_default_interfaces()
    assert result == {
        "ipv4": {"address": "172.17.0.1", "broadcast": "0.0.0.0", "netmask": "255.255.0.0", "network": "172.17.0.0"},
        "ipv6": {"address": "fe80::42:acff:fe11:1"},
        "macaddress": "02:42:ac:11:00:02",
        "mtu": 1500,
        "type": "bridge",
    }



# Generated at 2022-06-13 01:54:03.443578
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    import tempfile
    p = tempfile.mkdtemp()
    c = tempfile.mkdtemp(dir=p)
    # This is a fake device having a macaddr and a symlink to a PCI ID
    r = os.makedirs(os.path.join(c, 'device'))
    r = os.makedirs(os.path.join(c, 'device', 'driver'))
    r = os.makedirs(os.path.join(c, 'device', 'driver', 'module'))
    r = os.makedirs(os.path.join(c, 'bridge'))
    r = os.makedirs(os.path.join(c, 'bridge', 'brif'))
    r = os.makedirs(os.path.join(c, 'bonding'))
   

# Generated at 2022-06-13 01:54:08.803562
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    module = AnsibleModule({})
    ln = LinuxNetwork(module)

    # Test missing ethtool
    with patch('ansible.module_utils.network.common.linux.module.AnsibleModule.get_bin_path', return_value=False):
        assert ln.get_ethtool_data('eth0') == {}

    # Test good ethtool -k output

# Generated at 2022-06-13 01:54:52.105712
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    my_iface = LinuxNetwork()
    defaults = my_iface.get_default_interfaces()
    print(defaults)



# Generated at 2022-06-13 01:55:03.614026
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    module = AnsibleModule(argument_spec={})
    linux_network = LinuxNetwork(module)
    ethtool_path = linux_network.module.get_bin_path("ethtool")
    ts_features = ['hw_timestamp', 'software_timestamp', 'tx_software', 'rx_software', 'tx_hw']

# Generated at 2022-06-13 01:55:11.745976
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    # FIXME: shouldn't this be a pytest fixture?
    class FakeModule():
        def __init__(self, bin_path):
            self.bin_path = bin_path

        def get_bin_path(self, module):
            return self.bin_path


# Generated at 2022-06-13 01:55:22.234967
# Unit test for method get_ethtool_data of class LinuxNetwork

# Generated at 2022-06-13 01:55:25.117561
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    retval = LinuxNetwork(module=None).get_ethtool_data(device='eth1')
    assert 'timestamping' in retval
    assert 'hw_timestamp_filters' in retval


# Generated at 2022-06-13 01:55:30.745773
# Unit test for constructor of class LinuxNetworkCollector
def test_LinuxNetworkCollector():
    module = Mock()
    module.run_command = Mock()
    module.get_bin_path = Mock()

    ls = LinuxNetworkCollector(module, [])

    assert isinstance(ls, NetworkCollector)
    assert ls._platform == 'Linux'
    assert ls.required_facts == {'distribution', 'platform'}
    assert hasattr(ls, 'collect')


# Generated at 2022-06-13 01:55:36.568523
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():

    module = AnsibleModule(argument_spec=dict())
    ip_path = module.get_bin_path('ip')

    if module.params['ip_path'] is not None and ip_path is None:
        module.warn('%s requested but not found on target system' % module.params['ip_path'])

    default_ipv4 = {
        'interface': 'eth0'
    }
    default_ipv6 = {}

    # FIXME: move to __init__ or use setUp
    network = LinuxNetwork(module)
    network.get_interfaces_info(ip_path, default_ipv4, default_ipv6)

    populate_result = network.populate()

    assert populate_result is not None


# Generated at 2022-06-13 01:55:45.555047
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    """Test method get_interfaces_info of class LinuxNetwork"""
    # pylint: disable=import-error
    from ansible.module_utils.network.common.utils import get_file_content
    # pylint: enable=import-error
    socket.inet_aton("192.168.1.1")
    fn_path = '/sys/class/net/foo/bonding/slaves'
    fn_value = 'eth0 eth1\n'
    linux_network = LinuxNetwork()
    assert linux_network.get_interfaces_info(fn_path, fn_value) == 'device: foo, type: bonding, slave: eth0 eth1'


# Generated at 2022-06-13 01:55:54.742667
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    module = AnsibleModule(argument_spec={
        'interfaces_path': {'type': 'str'},
        'ip_path': {'type': 'str'},
    })

    linux_network = LinuxNetwork(module)  # Unit test mockup

    # Call the method under test
    interfaces = linux_network.get_default_interfaces(module.params['interfaces_path'],
                                                      module.params['ip_path'])

    # FIXME: do some kind of assertion here

    # Indicate the test was successful
    module.exit_json(changed=False)



# Generated at 2022-06-13 01:55:59.694699
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():

    module = AnsibleModule(
        argument_spec=dict(
            source=dict(type='str', default='system'),
        ),
        supports_check_mode=True,
    )

    # init module
    m = LinuxNetwork(module)

    # tests
    assert m.get_default_interfaces() == {'interface': 'lo', 'gateway': '::1', 'address': '127.0.0.1'}, \
        "failed to get default interfaces"


# Generated at 2022-06-13 01:56:41.442784
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    from ansible.utils.path import unfrackpath
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.common._collections_compat import Mapping

    # TODO: inject this
    sort = sorted
    platform_linux = object()
    platform_openbsd = object()
    platform_osx = object()
    # ansible/lib/ansible/utils/path.py unfrackpath
    mock_unfrackpath = lambda path, follow=True: path
    # ansible/lib/ansible/module_utils/basic.py get_platform
    mock_get_platform = lambda: platform_linux
    # ansible/lib/ansible/module_utils/basic.py get_distribution

# Generated at 2022-06-13 01:56:48.954958
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    """ validate the LinuxNetwork.populate() function """

    # Use a mock module with a mock file
    module = AnsibleModule({},
                           supports_check_mode=True)

    module.run_command = MagicMock(return_value=(0, '', ''))
    module.get_bin_path = MagicMock(return_value='')

    # This is a mostly blank class for testing
    class TestLinuxNetworkModule(LinuxNetworkModule):

        def get_interfaces_info(self, ip_path, default_ipv4, default_ipv6):
            return {}, {}

    ##########################################################################
    # Test cases

    # Test setup
    lm = TestLinuxNetworkModule(module)
    lm.get_ip_version = MagicMock(return_value=4)
    lm.get_

# Generated at 2022-06-13 01:56:58.678072
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    '''
    Unit test for method get_interfaces_info of class LinuxNetwork
    '''

    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )

    # set up test cases
    test_cases = [
        'get_interfaces_info_0',
        'get_interfaces_info_1',
    ]

    for test_case in test_cases:
        # set up mocks
        mock_module = MagicMock(name='module')
        mock_module.check_mode = False
        mock_module.get_bin_path = MagicMock(name='get_bin_path')
        mock_module.run_command = MagicMock(name='run_command')

        # set up module arguments

# Generated at 2022-06-13 01:57:07.965158
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    # Unit test
    #   python -c 'from ansible.module_utils.network.linux.linux_network import test_LinuxNetwork_get_ethtool_data; test_LinuxNetwork_get_ethtool_data()'
    import random, string

    MOCK_BIN_PATH = "/tmp/my-mock-bin-path"
    MOCK_DEVICE = "".join(random.sample(string.ascii_letters, 10))  # FIXME: random string is not particularly stable

    # Prepare

# Generated at 2022-06-13 01:57:13.261360
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    module = AnsibleModule(argument_spec={}, supports_check_mode=True)
    module.params = {
    }
    ln = LinuxNetwork(module)
    ln.populate()

if __name__ == '__main__':
    from ansible.module_utils.basic import *
    from ansible.module_utils.netcli import *
    from ansible.module_utils.network import *
    main()

# Generated at 2022-06-13 01:57:24.338585
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    net = LinuxNetwork()
    # Test lo interface
    main_iface = {'device': 'lo',
                  'mtu': 65536,
                  'macaddress': None,
                  'type': 'loopback',
                  'active': True,
                  'ipv4': {'address': '127.0.0.1',
                           'broadcast': 'host',
                           'netmask': '255.0.0.0',
                           'network': '127.0.0.0'},
                  'ipv6': [{'address': '::1',
                            'prefix': '128',
                            'scope': 'host'}]}
    assert net.interfaces['lo'] == main_iface
    # Test default IPv4

# Generated at 2022-06-13 01:57:31.913093
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    '''Unit test for method get_ethtool_data of class LinuxNetwork'''
    module = MockModule({})
    obj = LinuxNetwork(module)

    # ethtool_output is mocked data,
    # neither a dict nor a named tuple.

# Generated at 2022-06-13 01:57:42.042022
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    """
    test get_ethtool_data method of LinuxNetwork class
    """
    # get_ethtool_data method should return empty data for given device name if the device does not exists.
    linux_network = LinuxNetwork()
    assert linux_network.get_ethtool_data('eth0') == {}, "get_ethtool_data() should return empty data for device name passed as parameter if device does not exists."
    # get_ethtool_data method should return empty data for given device name if the device is not UP.
    assert linux_network.get_ethtool_data('wlan0') == {}, "get_ethtool_data() should return empty data for device name passed as parameter if device is not UP."
    # get_ethtool_data method should return empty data for given device name if ethtool is not installed.
    linux_network.module

# Generated at 2022-06-13 01:57:50.511974
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    # Unit test for method get_interfaces_info of class LinuxNetwork
    # Define Arguments to test
    ip_path = None
    default_ipv4 = None
    default_ipv6 = None


# Generated at 2022-06-13 01:58:01.500693
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    import os
    import tempfile
    import platform
    from units.compat import unittest

    class LinuxNetworkGetEthtoolDataTests(unittest.TestCase):
        def setUp(self):
            self.tmpdir = tempfile.mkdtemp(prefix='ansible_test_linux_network')
            self.ethtool_bin = os.path.join(self.tmpdir, 'ethtool')
            self.linux_network = LinuxNetwork()

            # FIXME: make these less fragile
            self.linux_network.module = lambda: None
            self.linux_network.module().run_command = lambda *args, **kwargs: 0, "", ""
            self.linux_network.module().get_bin_path = lambda *args: self.ethtool_bin
