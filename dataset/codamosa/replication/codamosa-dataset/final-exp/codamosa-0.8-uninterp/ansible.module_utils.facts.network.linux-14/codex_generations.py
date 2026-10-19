

# Generated at 2022-06-13 01:48:46.700303
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    """
    Unit test for method get_ethtool_data of class LinuxNetwork
    """
    import json
    import sys

    module_args = {"name": "test"}
    sys.path.append(os.path.join(os.path.dirname(__file__), "..", "..", "files"))

    from pylib.fake import MockModule

    fake_module = MockModule({})
    fake_module.run_command = (lambda x, y, z: (0, '', ''))

    linux_network = LinuxNetwork(fake_module)
    data = linux_network.get_ethtool_data("test")

    assert data == {}


# Generated at 2022-06-13 01:48:47.919218
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    pass



# Generated at 2022-06-13 01:48:52.911088
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    linux_network = LinuxNetwork()

    test_module = 'linux_network'
    args = {}
    args['gather_subset'] = []
    module = AnsibleModule(argument_spec=args)
    linux_network.module = module
    linux_network.populate()
    module.exit_json(**linux_network.data)


# Generated at 2022-06-13 01:48:57.560951
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    """
    This function tests the method get_default_interfaces of
    class LinuxNetwork.

    It is assumed that an interface with the IP address '192.0.2.1' is
    configured on the testing system.
    """

    # Get the module's path
    module_path = os.path.abspath(__file__)

    # Mock the AnsibleModule object and its module.params object
    mock_module = mock.MagicMock()
    mock_module.params = {}

    # Mock the LinuxNetwork module
    mock_LinuxNetwork = mock.MagicMock(spec=LinuxNetwork)
    mock_LinuxNetwork.module = mock_module

    # Mock the get_bin_path method of the LinuxNetwork module
    #
    # This method is called twice with the arguments 'ip' and 'ip6'
    #
    #

# Generated at 2022-06-13 01:49:08.844526
# Unit test for method get_ethtool_data of class LinuxNetwork

# Generated at 2022-06-13 01:49:19.504750
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    network = LinuxNetwork()

    ethtool_path1 = '/bin/ethtool'
    device1 = 'test1'
    rc1 = 0

# Generated at 2022-06-13 01:49:26.230142
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():

    def mock_get_bin_path(*args, **kwargs):
        return "/bin/ip"

    from ansible.module_utils import basic
    from ansible.module_utils.network.common.utils import get_file_content

    with patch.object(basic.AnsibleModule, "get_bin_path", new=mock_get_bin_path):
        to_patch = 'ansible.module_utils.network.common.utils.get_file_content'
        with patch(to_patch) as mock_get_file_content:
            mock_get_file_content.return_value = "0x11223344"

            module = basic.AnsibleModule(argument_spec=dict())
            network = LinuxNetwork(module)
            network.populate()

            assert network.is_linux is True

# Generated at 2022-06-13 01:49:32.152651
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    """
    Method `get_ethtool_data` of class `LinuxNetwork`
    """

    # Create a mock module
    module = AnsibleModule(argument_spec={})
    module.get_bin_path = Mock(return_value="/bin/ethtool")

    # Create a mock run_command

# Generated at 2022-06-13 01:49:45.040539
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    module = AnsibleModule(argument_spec={}, supports_check_mode=True)
    ln = LinuxNetwork(module=module)

    default_interface_path = "/proc/sys/net/ipv4/conf/default/rp_filter"
    with tempfile.NamedTemporaryFile() as f:
        f.write(b"2")
        f.flush()
        os.environ["_ANSIBLE_TEST_LINUX_NETWORK_DEFAULT_INTERFACE"] = f.name
        rp_filter, interface = ln.get_default_interfaces()
        assert rp_filter == 2
        assert interface == 'default'

    del os.environ["_ANSIBLE_TEST_LINUX_NETWORK_DEFAULT_INTERFACE"]


# Generated at 2022-06-13 01:49:48.541405
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    module = AnsibleModule(argument_spec={})
    module.exit_json = exit_json
    net = NetworkModule(module)
    iface = {}
    net.populate(iface)
    assert iface['device'] == 'lo'
    assert iface['type'] == 'loopback'

# Generated at 2022-06-13 01:50:32.040167
# Unit test for method get_ethtool_data of class LinuxNetwork

# Generated at 2022-06-13 01:50:43.469630
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    module = AnsibleModule(
        argument_spec={},
        supports_check_mode=True
    )
    # Test args
    ip_path = module.get_bin_path('ip')
    # Test body
    ln = LinuxNetwork(module)
    res = ln.populate()
    # Test assertions
    assert res.get('default_ipv4',{}).get('address','None') == 'None'
    assert len(res.get('interfaces',{}).keys()) > 0
    assert len(res.get('interfaces',{}).values()[0].keys()) > 0
    assert len(res.get('interfaces',{}).values()[0].get('ipv4',{}).keys()) > 0

# Generated at 2022-06-13 01:50:55.264098
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    """Test :meth:`get_interfaces_info` method"""
    # fixture: fake data
    # FIXME: separate 'data' as a variable not as a function param

# Generated at 2022-06-13 01:51:03.165593
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    # FIXME: Dummy values for the required args
    module = None
    get_default_interfaces = None
    get_interfaces_info = None
    get_interfaces_ip = None
    # FIXME: Dummy values for the optional kwargs
    run_command = None
    get_bin_path = None
    get_default_interfaces_v6 = None

    linux_network = LinuxNetwork(module, get_default_interfaces, get_interfaces_info, get_interfaces_ip, run_command=run_command, get_bin_path=get_bin_path, get_default_interfaces_v6=get_default_interfaces_v6)
    #FIXME: Populate the required args here
    args = []
    #FIXME: Populate the optional args here
    kwargs = {}

# Generated at 2022-06-13 01:51:10.935908
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    """
    Test the method get_interfaces_info of class LinuxNetwork.
    """
    # This is a static method so it can be tested independently
    result, ips = LinuxNetwork.get_interfaces_info(None, None, None)
    assert isinstance(result, dict)
    for interface in result:
        assert isinstance(result[interface], dict)
    assert isinstance(ips, dict)
    assert 'all_ipv4_addresses' in ips
    assert 'all_ipv6_addresses' in ips



# Generated at 2022-06-13 01:51:21.463707
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    m = AnsibleModuleMock()
    l = LinuxNetwork(m)
    m.get_bin_path = Mock(return_value='/bin/ip')
    m.run_command = Mock(return_value=(0, 'fe00::0/64 dev eth0  proto kernel  metric 256  pref medium', ''))
    assert l.get_default_interfaces() == (
        {'address': '', 'broadcast': '', 'netmask': '', 'network': '', 'metric': 256},
        {'address': '', 'prefix': '64', 'scope': 'link'},
    )



# Generated at 2022-06-13 01:51:27.337207
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    # Generate a temporary file
    tempdir = tempfile.mkdtemp()
    file = os.path.join(tempdir, "linux_network_facts.py")
    # Write some data to the file
    with open(file, 'w') as f:
        content = """

from ansible.module_utils.basic import *
from ansible.module_utils.facts import *
import sys

if __name__ == '__main__':
    module = AnsibleModule(
        argument_spec={}
    )

    module.exit_json(
        ansible_facts={
            'ansible_system': 'Linux',
            'ansible_architecture': 'x86_64',
        }
    )"""
        f.write(content)

    # Test the method
    ln = LinuxNetwork(file)

# Generated at 2022-06-13 01:51:32.346374
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    ln = LinuxNetwork()
    ln.module = AnsibleModule(argument_spec=dict(
        config=dict(type='dict', required=False),
    ))
    ln.populate(dict(config=dict(foo='bar')))
    assert ln.config == dict(foo='bar')



# Generated at 2022-06-13 01:51:43.438054
# Unit test for method populate of class LinuxNetwork

# Generated at 2022-06-13 01:51:51.436482
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():

    class ModuleMock:

        def __init__(self, device):
            self.device = device

        def get_bin_path(self, *args, **kwargs):
            return True

        def run_command(self, *args, **kwargs):
            if self.device != 'eth0':
                return (1, None, None)
            else:
                return (0, ETHTOOL_OUTPUT, None)

    m = ModuleMock('eth0')
    l = LinuxNetwork(module=m)
    assert l.get_ethtool_data('eth0') == ETHTOOL_OUTPUT_EXPECTED
    assert l.get_ethtool_data('non_existent') == {}


# Generated at 2022-06-13 01:52:38.613513
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    """
    Test the method to get info on all network interfaces
    """
    # TODO: test with a vrf interface
    # TODO: test with a bridge/bond interface
    # TODO: test with kernel modules loaded
    # TODO: test with a secondary IP
    # TODO: test with a virtual interface (e.g. eth0:1)
    # TODO: test with macvlan

    # define fake data to use for unit tests
    # Contents of files /sys/class/net/*
    #   address     - mac address
    #   mtu         - mtu size
    #   operstate   - up/down
    #   type        - type of interface (1=loopback, 24=ethernet, etc.).
    #                 Note: some interfaces lack this file.
    #   device      - symbolic link to parent

# Generated at 2022-06-13 01:52:49.195802
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    # FIXME: use a standard assertion framework
    module = AnsibleModule(
        argument_spec=dict(),
    )

    ln = LinuxNetwork(module)
    # FIXME: use a standard dunder test name method
    ln.populate()
    net_facts = ln.network_facts

    # v4 gateway
    assert 'gateway4' in net_facts
    assert net_facts['gateway4'] in (True, False)
    # v6 gateway
    assert 'gateway6' in net_facts
    assert net_facts['gateway6'] in (True, False)
    # interfaces
    # FIXME: is this really a valid assertion?
    assert 'interfaces' in net_facts
    assert isinstance(net_facts['interfaces'], dict)

# Generated at 2022-06-13 01:52:55.321636
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    module = AnsibleModule(argument_spec={})
    module.get_bin_path = MagicMock(return_value='/bin/ethtool')

# Generated at 2022-06-13 01:53:05.253856
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    # The typical input to LinuxNetwork.get_default_interfaces() is
    #   default_ipv4, default_ipv6
    module = MockModule({
        "version": 2
    })
    module.run_command = MagicMock(return_value=(0, "default via 1.2.3.4 dev eth0", ""))
    network = LinuxNetwork(module)
    ipv4, ipv6 = network.get_default_interfaces()
    assert ipv4['address'] == "1.2.3.4"
    assert ipv4['devicename'] == "eth0"
    assert ipv6 == None

# Generated at 2022-06-13 01:53:15.482741
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    module = AnsibleModule(
        argument_spec=dict(
            gather_subset=dict(type='list', required=False)
        )
    )
    # We need this to test module_name
    module.params['gather_subset'] = ['all']

    ln = LinuxNetwork(module)
    data = ln.populate()

    assert isinstance(data, dict)
    for k in ['all_ipv4_addresses', 'all_ipv6_addresses', 'default_ipv4', 'default_ipv6', 'interfaces']:
        assert k in data


# Generated at 2022-06-13 01:53:22.741703
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    l = LinuxNetwork()
    # Heavily relies on mock.patch, unsure if it's best to include here
    # or in test_ansible_module_get_network_facts
    l.module = mock.MagicMock()
    l.module.run_command = mock.MagicMock(return_value = (0, "198.51.100.1 via 10.0.0.1 dev eth0 proto static src 10.0.0.2 metric 100", ""))

# Generated at 2022-06-13 01:53:28.923521
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():

    # Create empty object
    module_obj = AnsibleModule(argument_spec={})
    # TODO: need to mock get_bin_path()
    # TODO: need to mock run_command()
    # create empty object of class LinuxNetwork
    ln_obj = LinuxNetwork(module_obj)

    # Run the method get_interfaces_info
    # NOTE: input arguments are in order
    # NOTE: output arguments are in order
    # NOTE: not really sure how to test this, it's one of the most complicated methods
    actual = ln_obj.get_interfaces_info()

    # TODO: assert actual == expected
    print("The actual returned value is:")
    pprint(actual)


# Generated at 2022-06-13 01:53:38.634160
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    module = AnsibleModule(
        argument_spec = dict(
            gather_subset = dict(type='list')
        )
    )
    # NOTE: technically this is two tests but we're not testing the actual population here
    ln = LinuxNetwork(module=module, options=None)
    assert 'all_ipv4_addresses' not in ln.interfaces['eth0']
    ln.populate('all_ipv4_addresses')
    assert 'all_ipv4_addresses' in ln.interfaces['eth0']

    ln = LinuxNetwork(module=module, options={'gather_subset': ['!all']})
    assert 'all_ipv4_addresses' not in ln.interfaces['eth0']

# Generated at 2022-06-13 01:53:49.413829
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    module = AnsibleModule(argument_spec={})
    module_mock = MagicMock()
    module_mock.run_command = MagicMock(return_value=(0, '', ''))
    module_mock.get_bin_path = MagicMock(return_value='/usr/sbin/ethtool')
    net = LinuxNetwork(module_mock)


# Generated at 2022-06-13 01:53:52.543579
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(
        argument_spec=dict(
            name=dict(type='str'),
        ),
    )
    linux_network = LinuxNetwork(module)
    default_ipv4 = {}
    default_ipv6 = {}
    interfaces, ips = linux_network.get_interfaces_info(linux_network.ip_path, default_ipv4, default_ipv6)
    return interfaces, ips



# Generated at 2022-06-13 01:54:46.586731
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():

    linux = init_linux_distribution()
    linux.update({'name': 'Ubuntu', 'version_info': ['16', '04', '1', 'LTS']})
    g_module = Mock()
    g_module.run_command.return_value = (1, 'ignored', 'ignored')
    g_module.get_bin_path.return_value = 'ignored'
    g_module.params = {'collect_route': True}
    network = LinuxNetwork(g_module)
    network.interface = {'eth0': {'device': 'eth0', 'type': 'unknown'}}

# Generated at 2022-06-13 01:54:55.560856
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    m = LinuxNetwork()
    # FIXME: test with linux_distribution on all supported platforms
    # TODO: test loopback with ethtool installed
    if platform.dist()[0] == 'centos':
        # TODO: test real eth with ethtool installed
        # TODO: test real eth with ethtool not installed
        data = m.get_ethtool_data("lo")
        assert data == {}
    else:
        # TODO: test real eth with ethtool installed
        # TODO: test real eth with ethtool not installed
        data = m.get_ethtool_data("lo")
        assert data == {}
    return True


# Generated at 2022-06-13 01:55:06.038293
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    ln = LinuxNetwork()
    ln.module = mock.Mock()
    ln.module.get_bin_path = lambda x: "/bin/ethtool"

# Generated at 2022-06-13 01:55:16.807489
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    class TestModule(object):
        def __init__(self):
            self.exit_json = lambda x: x
            self.run_command = lambda x, **kwargs: (0, '', '')
            self.get_bin_path = lambda x: '/bin/ip'
    class TestSystem(object):
        def __init__(self):
            self.network = LinuxNetwork(TestModule())
    system = TestSystem()
    system.network.populate()
    assert system.network.default_ipv4['address'] == '10.0.0.2'
    assert system.network.default_ipv4['gateway'] == '10.0.0.1'
    assert system.network.default_ipv6['address'] == 'fe80::20c:29ff:fef2:744d'


# Generated at 2022-06-13 01:55:24.822634
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    #FIXME: should be in test/units/?
    # create a fake module
    module = AnsibleModule(argument_spec={}, supports_check_mode=True)
    # create a fake command module to inject into the class
    command = {'run_command': lambda args: (0, '66:b9:40:00:c3:56', '')}
    # create an instance of this class
    linux_network = LinuxNetwork(module, command)
    # run get_interfaces_info with a faked ip command output
    interfaces, ips = linux_network.get_interfaces_info(
        '/bin/ip',
        {'address': '192.0.2.1', 'network': ''},
        {'address': '::1', 'network': ''}
    )
    # test results

# Generated at 2022-06-13 01:55:33.989500
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():

    ########################################################################
    # Stub functions
    ########################################################################
    class StubLinuxNetworkModule:

        def __init__(self):
            self.bin_path_items = {}

        def get_bin_path(self, item):
            return self.bin_path_items.get(item, None)

        def run_command(self, args, errors):
            self.last_args = args
            return self.run_command_results[args[1]]

    ########################################################################
    # Unit tests
    ########################################################################
    class TestLinuxNetwork:

        def setup_method(self, method):
            self.linux_network = LinuxNetwork()
            self.linux_network.default_ipv4 = {"address": "1.2.3.4"}
            self.linux_network.default_ipv

# Generated at 2022-06-13 01:55:34.496260
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    return None


# Generated at 2022-06-13 01:55:45.555978
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    # Initialization
    # FIXME: technically we don't need ModuleTestCase here, just module_runner
    module = ansible_module()
    module_args = dict(
        gather_subset=['all'],
    )
    module.params = module_args
    module.exit_json = lambda x: x  # don't exit early
    mock_obj = LinuxNetwork(module)

    # Call method
    mock_obj.populate()

    # FIXME: we need to inspect the output of module.exit_json.  Can we
    # mock module.exit_json so we don't have to do that here?
    assert 'default_ipv4' in module._result
    assert 'default_ipv6' in module._result


if __name__ == '__main__':
    test_LinuxNetwork_populate()

# Generated at 2022-06-13 01:55:56.799922
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    ln = LinuxNetwork()
    # if these are wrong, you probably need to update this test method
    ln.module.run_command.return_value = (0, 'default via 192.0.2.1 dev eth0  proto static  metric 100', '')
    ln.module.get_bin_path.return_value = "/sbin/ip"
    assert ln.get_default_interfaces() == {'v4': {'interface': 'eth0', 'address': '192.0.2.1'}, 'v6': {}}
    ln.module.run_command.assert_any_call(["/sbin/ip", "-4", "-o", "route", "get", "8.8.8.8"])

# Generated at 2022-06-13 01:55:58.883635
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    # this method generates a temporary config file
    # and returns a dict of results
    pass

# Generated at 2022-06-13 01:56:45.259371
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    module = AnsibleModule({})
    ln = LinuxNetwork(module)

# Generated at 2022-06-13 01:56:56.180833
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    module = AnsibleModule(argument_spec={})
    class LinuxNetwork:
        def __init__(_self, module):
            _self.module = module
            _self.INTERFACE_TYPE = {}
    linux_network = LinuxNetwork(module)
    rc, stdout, stderr = module.run_command(["/usr/bin/getent", "ai"], errors='surrogate_then_replace')
    if rc == 0:
        # getent ai returns default route, so just take that
        default_v4, default_v6 = linux_network.get_default_interfaces(stdout)
    else:
        # getent not present or some other issue
        default_v4 = {'gateway': '172.31.12.1'}

# Generated at 2022-06-13 01:57:01.918970
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    module = AnsibleModule(argument_spec={})
    ln = LinuxNetwork(module)
    data = ln.get_ethtool_data('eth0')
    assert 'features' in data
    assert 'timestamping' in data
    assert 'hw_timestamp_filters' in data
    assert 'phc_index' in data


# ===========================================
# Module execution.
#


# Generated at 2022-06-13 01:57:09.042658
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    # initialize the module and its arguments.
    module = AnsibleModule(
        argument_spec=dict(
            gather_subset=dict(type='list', default=['all'])
        )
    )

    # execute the populate function and get group and parameter results.
    linux_network = LinuxNetwork(module)
    groups, per_host_params = linux_network.populate()

    # since we are testing the return of a function here, we caputure the result as result
    result = dict(
        changed=True,
        failed=False,
        groups=groups,
        per_host_params=per_host_params
    )

    module.exit_json(**result)



# Generated at 2022-06-13 01:57:16.773611
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    # Create a mock module
    sysfs_path = '/sys'
    module = AnsibleModule({
        'ANSIBLE_MODULE_ARGS': {'gather_subset': 'all'}
    })
    # Mock module arguments
    module.params = {'gather_subset': 'all'}

    # Create a LinuxNetwork object
    ln = LinuxNetwork(module, sysfs_path)

    # Create a mock 'default_ipv4' dictionary
    default_ipv4 = {'address':'10.1.1.1'}

    # Create a mock 'default_ipv6' dictionary
    default_ipv6 = {'address':'fe80::f2de:f1ff:fe85:23bd'}

    # Invoke the get_interfaces_info method with mock arguments
    interfaces,

# Generated at 2022-06-13 01:57:17.399502
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    pass

# Generated at 2022-06-13 01:57:26.383340
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    # Test parameters
    mod = AnsibleModule([],  check_invalid_arguments=False)
    mod.run_command = MagicMock()
    mod.run_command.return_value = (0, '', '')
    ins = LinuxNetwork(mod)

    # Test cases

    class Args:
        def __init__(self):
            self.name = 'eth0'
            self.command = 'show'
            self.state = 'present'
            self.target = 'eth0'
            self.device = 'eth0'
            self.options = []
            self.use_ipv6 = False
            self.address = '10.1.1.1'
            self.prefix = '24'
            self.netmask = '255.255.255.0'

# Generated at 2022-06-13 01:57:28.350386
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    ln = LinuxNetwork()
    assert ln.get_default_interfaces() == ('lo', 'lo')


# Generated at 2022-06-13 01:57:32.135711
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    module = AnsibleModule(argument_spec=dict())
    iface = 'eno1'
    path = module.get_bin_path('ethtool')
    if not path:
        module.fail_json(msg="No path for `ethtool` was found.")

    instance = LinuxNetwork()
    data = instance.get_ethtool_data(iface)
    assert type(data) is dict

# Generated at 2022-06-13 01:57:42.370564
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    args = dict(
        device='eth0',
    )
    command = 'ethtool -k %(device)s' % args