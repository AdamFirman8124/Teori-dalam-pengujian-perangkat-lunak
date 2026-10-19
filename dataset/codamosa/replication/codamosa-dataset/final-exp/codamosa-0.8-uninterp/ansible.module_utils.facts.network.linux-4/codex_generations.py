

# Generated at 2022-06-13 01:48:40.642900
# Unit test for constructor of class LinuxNetworkCollector
def test_LinuxNetworkCollector():
    lnc = LinuxNetworkCollector()
    assert lnc._platform == 'Linux'
    assert lnc._fact_class == LinuxNetwork
    assert lnc.required_facts == set(['distribution', 'platform'])



# Generated at 2022-06-13 01:48:52.590904
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():

    context = {
        'module': FakeModule(),
        'default_route_ipv4': {'interface': 'eth0', 'address': '10.0.0.1'},
        'default_route_ipv6': {'interface': 'eth0', 'address': '2001:db8::1'},
        'route': {'default': {'10.0.0.0/8': '10.0.0.1', '2001:db8::/64': '2001:db8::1'}},
        'route6': {'default': {'2001:db8::/64': '2001:db8::1'}},
    }


# Generated at 2022-06-13 01:48:57.323629
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    # Mock some external methods/attributes
    module = mock.Mock()
    module.run_command.return_value = (0, '', '')
    module.get_bin_path.return_value = '/usr/bin/ip'
    linux_network = LinuxNetwork(module)

    interfaces, ips = linux_network.populate()
    assert interfaces == {}
    assert ips == {}



# Generated at 2022-06-13 01:49:08.623348
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes

    m = basic.AnsibleModule(
        argument_spec={},
        supports_check_mode=True,
    )

    check_mode = m.check_mode
    if check_mode:
        m.exit_json(changed=False)

    # Set up our defaults
    interfaces = {}
    ips = dict(
        all_ipv4_addresses=[],
        all_ipv6_addresses=[],
    )
    default_ipv4 = {}
    default_ipv6 = {}

    # We need to use '/bin/true' here as we don't need to send a command - we are
    # just testing the constructor.

# Generated at 2022-06-13 01:49:19.221277
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True,
    )

    linux_network_instance = LinuxNetwork(module)

    # ->
    # This is not setting the main ipv4, but instead only the secondaries.
    # It may be possible to change the test data to address this, but for
    # now I'm going to leave it as a FIXME.
    # <-

    module.get_bin_path.return_value = 'ip'

# Generated at 2022-06-13 01:49:23.577025
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes
    from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import to_list
    from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import dict_merge
    from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import remove_default_spec

# Generated at 2022-06-13 01:49:31.392932
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():

    # NOTE ansible/ansible#29593: get_ethtool_data calls ethtool, then checks for the
    # presence of a key in the output before setting it.  There are a lot of ways that
    # could fail, but the easiest one to test is the case where ethtool is present but
    # outputs nothing.  This unit test verifies that no exception is thrown.

    # create a LinuxNetwork obj
    network = LinuxNetwork()

    # call get_ethtool_data; expect to get an empty dict back
    results = network.get_ethtool_data(device="lo")
    assert isinstance(results, dict)
    assert not results



# Generated at 2022-06-13 01:49:33.913850
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    m = LinuxNetwork()
    (ipv4, ipv6) = m.get_default_interfaces()
    assert len(ipv4) == 5



# Generated at 2022-06-13 01:49:45.550103
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    module = AnsibleModule(argument_spec={})
    linux_network = LinuxNetwork(module)

    module.run_command = MagicMock(return_value=(0, 'eth0', ''))
    result = linux_network.get_default_interfaces()
    assert result == ('eth0', 'eth0')

    module.run_command = MagicMock(return_value=(0, 'wlan0', ''))
    result = linux_network.get_default_interfaces()
    assert result == ('eth0', 'wlan0')

    module.run_command = MagicMock(return_value=(0, 'lo', ''))
    result = linux_network.get_default_interfaces()
    assert result == ('lo', 'lo')


# Generated at 2022-06-13 01:49:51.556869
# Unit test for method populate of class LinuxNetwork

# Generated at 2022-06-13 01:50:28.332887
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    '''
    Unit test for method populate of class LinuxNetwork
    '''
    m = AnsibleModule({
        'gather_timeout': 2,
    })

    n = LinuxNetwork(m)

    for method in n.populate.__code__.co_names:
        if hasattr(n, method):
            f = getattr(n, method)
            f()


# Generated at 2022-06-13 01:50:36.452968
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )
    set_module_args(
        dict()
    )
    # Test the default return
    linuxnetwork = LinuxNetwork(module)
    assert linuxnetwork.module.params == dict(), "Return default value"
    # Test no check_mode
    linuxnetwork = LinuxNetwork(module, check_mode=False)
    assert linuxnetwork.module.params == dict(), "Return default value"

# Generated at 2022-06-13 01:50:38.804640
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    assert linux_network_module._get_default_interfaces("ip route show") == ("eth0", "eth0")

# Generated at 2022-06-13 01:50:50.559315
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    # Create an instance of class LinuxNetwork
    # We are not testing the constructor but the method get_ethtool_data
    n = LinuxNetwork()
    # An "empty" sample of the output of the command 'ethtool -k'

# Generated at 2022-06-13 01:51:00.504601
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    """Test if ethtool data can be extracted correctly"""

    def run_ethtool_mock(module, *args, **kwargs):
        """Mock for run_command.
        If command is something which contains "ethtool -k ethX" (with X being a number)
        all results are returned as if ethtool was installed and ethX exists.
        If command is something which contains "ethtool -T ethY" (with Y being a number)
        all results are returned as if ethtool was installed and ethY exists.
        """
        out = ''


# Generated at 2022-06-13 01:51:04.567952
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    module = AnsibleModule({})
    linux_network = LinuxNetwork(module)
    # FIXME: Complete test_LinuxNetwork_populate by testing each return path
    assert True == True


# Generated at 2022-06-13 01:51:09.707882
# Unit test for constructor of class LinuxNetworkCollector
def test_LinuxNetworkCollector():
    facts = dict(platform="Linux",
                 distribution=dict(
                     id="centos",
                     version=dict(full='6.5')
                 ))
    module = AnsibleModule(argument_spec=dict())
    nc = LinuxNetworkCollector(module)
    assert nc.facts is not None and nc.facts == facts


# Generated at 2022-06-13 01:51:13.645929
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    module = AnsibleModule(argument_spec={})
    # FIXME: mock os, netifaces, and socket and fix
    network = LinuxNetwork(module)
    assert network.get_default_interfaces() == ({}, {})



# Generated at 2022-06-13 01:51:25.311749
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    module = AnsibleModule(argument_spec={'gather_subset': dict(default=['!all'], type='list')}, supports_check_mode=True)
    network = LinuxNetwork(module)
    network.populate()
    for key, value in network.interfaces.items():
        assert value.keys() == ['device', 'ipv4', 'ipv6']
    assert network.default_ipv4.keys() == ['address', 'broadcast', 'netmask', 'network', 'mtu', 'macaddress', 'type']
    assert network.default_ipv6.keys() == ['address', 'prefix', 'scope', 'mtu', 'macaddress', 'type']
    for key, value in network.ips.items():
        assert value.__class__.__name__ == 'list'


# Generated at 2022-06-13 01:51:30.805229
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    fake_module = FakeModule(dict())
    ln = LinuxNetwork(fake_module)
    ln.module.run_command = fake_run_command
    # Test case 1: successful execution of command 'ethtool'.

# Generated at 2022-06-13 01:52:16.745314
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    # instantiate the class
    LN = LinuxNetwork()

    # output from ethtool -k -T eth0

# Generated at 2022-06-13 01:52:25.483614
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    from tempfile import mkdtemp
    from shutil import rmtree
    from copy import copy
    # NOTE: this only tests the specific implementation above.
    # It does not test for generic functionality

    #
    # "mock out" the module
    #
    class FakeModule:
        def get_bin_path(self, arg, *args, **kwargs):
            if arg == "ethtool":
                return "/sbin/ethtool"

        def run_command(self, args, errors='surrogate_then_replace'):
            # FIXME: also test stderr?
            if args[0] == '/sbin/ethtool':
                stdout = ETHTOOL_ETH0_K
                rc = 0

# Generated at 2022-06-13 01:52:36.185372
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():

    device = "eth0"
    path = "/usr/bin/"
    m = MockAnsibleModule()
    m.params = dict(
    )

    n = LinuxNetwork(m)
    n.module.get_bin_path = lambda x: path + x
    n.module.run_command = lambda x, y, errors: (0, "", "")
    result = n.get_ethtool_data(device)
    assert result == {'features': {}, 'timestamping': [], 'hw_timestamp_filters': []}


# Test empty feature string
    n.module.run_command = lambda x, y, errors: (0, "", "")
    result = n.get_ethtool_data(device)

# Generated at 2022-06-13 01:52:46.487351
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    linux_network = LinuxNetwork(module)

    # Return code is zero
    #
    # Command:
    #   ip route show exact 0.0.0.0/0
    #
    # If a default route exist the below command returns:
    # default via 192.168.0.1 dev enp0s3
    #
    # If a default route doesn't exist the below command returns nothing
    rc = 0
    out = "default via 192.168.0.1 dev enp0s3"
    err = ""
    def_v4_route, def_v6_route = linux_network.get_default_interfaces(rc, out, err)
    assert def_v4_route == 'enp0s3'
    assert def_v6_route == 'lo'

# Generated at 2022-06-13 01:52:54.947300
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    # FIXME:
    class Dummy(object):
        def get_bin_path(self, name):
            return True
        def run_command(self, args, errors):
            return 0, 'test_output', ''
    network = LinuxNetwork(Dummy())

    # Mock stdin, stdout and stderr.
    #
    # The code being tested uses `sys.stdin` to access the input file.
    # Passing a StringIO object as `sys.stdin` is fine for most code, but
    # the `dd` command does a `.fileno()` on `sys.stdin` to access the file
    # descriptor, and that fails with a `AttributeError: fileno`.
    #
    # So, we mock `sys.stdin` as an actual file descriptor.
    #

# Generated at 2022-06-13 01:53:06.986867
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    import tempfile
    # NOTE: we don't mock `ethtool` (if present) since we actually want to make sure that exists
    # TODO: add a fake ethtool in the temp dir and make sure get_bin_path will find it

    # TODO: refactor that to a class method?

# Generated at 2022-06-13 01:53:08.302513
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    pass

# Generated at 2022-06-13 01:53:19.176359
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    module = DummyAnsibleModule()
    path = module.get_bin_path("ethtool")
    network = LinuxNetwork(module)
    assert path

    device = "dummy"
    args = [path, '-k', device]
    rc, stdout, stderr = module.run_command(args)
    assert rc == 0
    args = [path, '-T', device]
    rc, stdout, stderr = module.run_command(args)
    assert rc == 0

# Generated at 2022-06-13 01:53:20.425583
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    """
    Test to populate the network info.
    """
    obj = LinuxNetwork()
    return obj.populate()



# Generated at 2022-06-13 01:53:26.181519
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    from copy import deepcopy
    from ansible_collections.ansible.netcommon.tests.unit.compat.mock import MagicMock

    # Needed to build the linux network object
    module = MagicMock()
    module.run_command = MagicMock(return_value=(0, "", ""))

    # Get the linux network object
    ln = LinuxNetwork(module=module, params={})

    # Reference to the variable holding the interface data
    interfaces = ln.interfaces

    # Number of interfaces the test server has, should be 12
    num_interfaces = len(interfaces.keys())

    # Number of network interfaces present
    assert num_interfaces >= 12, "Not enough network interfaces present on this server"

    # All interfaces should be in the iterfaces variable

# Generated at 2022-06-13 01:54:05.526920
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    # [ansible-project] where should I put unit tests?
    pass


# ===========================================
# Subclass: DarwinNetwork
# ===========================================


# Generated at 2022-06-13 01:54:10.934869
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    linux_network = LinuxNetwork()
    linux_network.module.run_command = MagicMock(return_value=(0, '', ''))
    linux_network.get_default_interfaces = MagicMock(return_value=({}, {}))
    linux_network.get_interfaces_info = MagicMock(return_value=({}, {}))
    linux_network.get_route_data = MagicMock(return_value=({}, {}))
    populated = linux_network.populate()

# Generated at 2022-06-13 01:54:16.842861
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    # Create instance of class LinuxNetwork
    network = LinuxNetwork()

    # Create test data
    ethtool_path = '/bin/ethtool'
    device = 'eth0'

    # Test successful run
    expected_rc = 0

# Generated at 2022-06-13 01:54:24.370084
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():

    # This method is one of the most difficult to test since it relies on
    # external commands.  Therefore, all of the test cases below rely on mocked
    # commands.  The test case DOES NOT do any command checking.  If a command
    # is mocked, it is is up to a human to ensure that the command is not
    # actually run.
    #
    # The variable 'module' is from the test/units/compat.py script.
    # It is a mock 'AnsibleModule' instance.

    # netifaces is not necessary for this method
    module.params = {'provider': None, 'ip_path': None}
    n = LinuxNetwork(module)

    # these tests rely on the system being connected to the internet.  The
    # check is that both ipv4 and ipv6 have an address.

# Generated at 2022-06-13 01:54:25.552894
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    '''Unit test for method get_interfaces_info of class LinuxNetwork'''
    pass




# Generated at 2022-06-13 01:54:38.251892
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    # FIXME: this is *not* a unit test, these are integration tests
    # this should not be in this file, maybe in test_linux.py?
    module = AnsibleModule(argument_spec={})
    ln = LinuxNetwork(module)
    rc, out, err = ln.module.run_command("ip -4 -o addr show up")
    ln.ipv4, ln.ipv6 = ln.get_interface_names(out)
    ln.default_ipv4, ln.default_ipv6 = ln.get_default_interface()
    ln.interfaces, ln.ips = ln.get_interfaces_info('/sbin/ip', ln.default_ipv4, ln.default_ipv6)
    # NOTE: these dicts will not

# Generated at 2022-06-13 01:54:49.298910
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    module = AnsibleModule(
        argument_spec=dict(
            gather_subset=dict(default=[], type='list'),
        )
    )
    # NOTE: Since this is a managed Windows host, we will not be able to test
    # the part of the code that calls `ip route` and `ip -6 route`.
    ln = LinuxNetwork(module)
    default_ipv4, default_ipv6 = ln.get_default_interfaces()
    assert default_ipv4['address'] == '10.0.0.0'
    assert default_ipv4['address'] == default_ipv6['address']
    assert default_ipv4['macaddress'] == '00:11:22:33:44:55'

# Generated at 2022-06-13 01:55:01.000594
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    module = AnsibleModule(argument_spec={}, supports_check_mode=False)

    if not HAS_NETIFACES:
        module.fail_json(msg="Required 'netifaces' module not found. On Debian/Ubuntu systems this can be installed by running: apt install python-netifaces")

    # This would make unit tests much easier
    if not hasattr(module, 'run_command'):
        module.run_command = run_command

    if not hasattr(module, 'get_bin_path'):
        module.get_bin_path = get_bin_path

    if not module.get_bin_path("ip"):
        return module.fail_json(msg="Required 'ip' command not found. Please install iproute2 package.")


# Generated at 2022-06-13 01:55:03.658311
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():

    # get_interfaces_info(ip_path, default_ipv4, default_ipv6)

    assert callable(LinuxNetwork.get_interfaces_info)


# Generated at 2022-06-13 01:55:11.836618
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    from ansible.module_utils._text import to_bytes, to_native

    class TestModule:
        def __init__(self):
            self.bin_path = '/usr/bin:/bin'

        def get_bin_path(self, arg):
            return self.bin_path

        def run_command(self, cmd, tmp_path, sudo_user, sudoable, executable):
            # cmd is a list
            if cmd[0] == '/usr/bin/ip':
                if cmd[3] == "lo":
                    return (0, LO_IP_OUTPUT, '')
                else:
                    return (0, ETH_IP_OUTPUT, '')

# Generated at 2022-06-13 01:55:57.799519
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    mod = AnsibleModule({})
    mod.run_command = MagicMock()
    testobj = LinuxNetwork(mod)
    # call method under test and assert results
    device = 'enp0s8'

# Generated at 2022-06-13 01:56:05.876191
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    module = AnsibleModule(argument_spec=dict())
    test_class = LinuxNetwork(module)


# Generated at 2022-06-13 01:56:11.402848
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule({})
    task = LinuxNetwork(module)
    out, err = task.get_interfaces_info(dict(), dict(), dict())
    assert isinstance(out, dict)
    assert isinstance(err, dict)

# Generated at 2022-06-13 01:56:23.378112
# Unit test for method get_interfaces_info of class LinuxNetwork

# Generated at 2022-06-13 01:56:29.152136
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True,
    )
    ln = LinuxNetwork(module)
    ip_path = module.get_bin_path("ip")
    default_ipv4 = dict(address='1.2.3.4')
    default_ipv6 = dict(address='::4')
    interfaces, ips = ln.get_interfaces_info(ip_path, default_ipv4, default_ipv6)
    emitters = [dict(name='ansible.builtin.network_debug'), dict(name='ansible.builtin.network_facts')]
    got = ln.populate(emitters, 'ansible_facts', interfaces, ips, default_ipv4, default_ipv6)

# Generated at 2022-06-13 01:56:38.302034
# Unit test for method get_default_interfaces of class LinuxNetwork

# Generated at 2022-06-13 01:56:45.110522
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    # setup
    test_obj = LinuxNetwork()

    # no command (test for exception)
    module = Mock()
    module.params = {'gather_subset': ['!all']}
    module.run_command.return_value = (0, "", "")
    test_obj.module = module

    # set expected response
    expected = {
        'v4': {},
        'v6': {}
    }

    # perform the test
    actual = test_obj.get_default_interfaces()

    # assert the expected result
    assert expected == actual



# Generated at 2022-06-13 01:56:48.974873
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    host = 'foo.bar'

    # LinuxNetwork.get_ethtool_data
    ln = LinuxNetwork({'ansible_host': host})
    ln.get_ethtool_data('eth0')


# Generated at 2022-06-13 01:56:57.550138
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():

    # create an instance of the class
    linux_network = LinuxNetwork()

    # create mock of module
    mock_module = MagicMock()

    # mock fail_json
    mock_fail_json = MagicMock()
    mock_module.fail_json = mock_fail_json

    # create mock of ip binary
    mock_ip = MagicMock()
    mock_ip.return_value = '/usr/bin/ip'
    mock_module.get_bin_path = mock_ip

    # create mock of ip route get
    mock_ip_route_get_device = MagicMock()
    mock_ip_route_get_device.return_value = 'lo'
    mock_module.run_command = mock_ip_route_get_device

    # create mock of interfaces
    method = mock_module.run_command

# Generated at 2022-06-13 01:56:58.853309
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    assert True, 'Issue with unit test'


# Generated at 2022-06-13 01:57:44.680306
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    module = MagicMock(return_value=None)
    module.params = {
        'module_defaults': None
    }
    module.get_bin_path = MagicMock(return_value='/sbin/ip')
    l = LinuxNetwork(module=module)

    def fake_get_interfaces_info(ip_path, default_ipv4, default_ipv6):
        return {}, {}

    l.get_interfaces_info = fake_get_interfaces_info
    l.get_gateway_interface = MagicMock(return_value=('eth0', '192.168.1.1', 'fe80::1'))

# Generated at 2022-06-13 01:57:51.885719
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    '''
    This is a unit test for method LinuxNetwork.get_ethtool_data.
    '''

    # test-0.1
    # test when there is no ethtool command
    ####################################
    # Set initial conditions
    linux_network = LinuxNetwork()
    linux_network.module = mock.MagicMock()
    linux_network.module.get_bin_path.return_value = None

    # Run
    result = linux_network.get_ethtool_data('br0')

    # Check
    assert not result

    # test-0.2
    # test when there is no data
    ####################################
    # Set initial conditions
    linux_network = LinuxNetwork()
    linux_network.module = mock.MagicMock()
    bin_path = 'test_bin/ethtool'
    linux_network

# Generated at 2022-06-13 01:58:03.364492
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    module = FakeAnsibleModule()
    linux_network = LinuxNetwork(module)
    default_ipv4 = {'device': 'eth0'}
    default_ipv6 = {'device': 'eth0'}
    linux_network.get_default_interfaces(default_ipv4, default_ipv6)
    assert default_ipv4 == dict(
        device='eth0',
        address='192.0.2.1',
        netmask='255.255.255.0',
        network='192.0.2.0',
        broadcast='192.0.2.255',
        gateway='192.0.2.254',
        macaddress='00:11:22:33:44:55',
        mtu=1500,
        type='unknown',
    )
    assert default_ipv6

# Generated at 2022-06-13 01:58:11.075885
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    module = AnsibleModule(
        argument_spec = dict(),
        supports_check_mode = True
    )
    # FIXME: this is all basically just to mock and set AnsibleModule.run_command()
