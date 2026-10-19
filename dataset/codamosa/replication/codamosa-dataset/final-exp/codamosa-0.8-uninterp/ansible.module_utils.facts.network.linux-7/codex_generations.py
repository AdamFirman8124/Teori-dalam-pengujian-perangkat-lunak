

# Generated at 2022-06-13 01:48:48.557519
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    """
    Unit tests for the module
    """

    from ansible.module_utils.facts.network.linux import LinuxNetwork
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(argument_spec={})
    module.params = {}
    module.exit_json = lambda *args: True

    network = LinuxNetwork()
    network.module = module

    default_ipv4 = {'address': '192.168.1.1'}
    default_ipv6 = {'address': 'fe80::5054:ff:fe12:3456'}
    ip_path = 'ip'
    interfaces = {'eth0': {'address': '52:54:00:12:34:56'}}

# Generated at 2022-06-13 01:48:57.677280
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    '''
    Unit test for method get_ethtool_data of class LinuxNetwork
    '''
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True,
    )
    module.params = dict()
    network = LinuxNetwork(module)
    # Ethtool is not installed or device doesn't exist
    assert {} == network.get_ethtool_data('lo')
    # Ethtool is installed. Device exist but ethtool don't support device.
    module.run_command = MagicMock(return_value=(0, '', ''))
    assert {} == network.get_ethtool_data('lo')
    # Ethtool is installed. Device exist and ethtool support device.

# Generated at 2022-06-13 01:49:08.928339
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    module = None
    ethtool_path = 'ethtool'
    device = 'lo'
    ln = LinuxNetwork(module, ethtool_path, device)
    # TODO: since we are not passing in a module, this will always be None
    # TODO: add a mocked module and require no arguments for testing
    assert ln.get_bin_path("ethtool")

    ln.module.run_command = Mock(return_value=(0, 'blah', ''))
    data = ln.get_ethtool_data(device)
    assert data.get('features') is None
    assert data.get('timestamping') is None
    assert data.get('hw_timestamp_filters') is None
    assert data.get('phc_index') is None


# Generated at 2022-06-13 01:49:19.623727
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    module = AnsibleModule(argument_spec=dict())
    ln = LinuxNetwork(module)
    # test get_default_interfaces with system not supporting IPv6
    def _fake_exec_command(cmd, *args, **kwargs):
        # FIXME: exec_command returns a tuple not two dicts
        return dict(rc=0, stdout='', stderr='')
    # FIXME: use mock.patch()
    ln.exec_command = _fake_exec_command


# Generated at 2022-06-13 01:49:23.175815
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    module = AnsibleModule(
        argument_spec = dict(),
        supports_check_mode = True
    )

    network = LinuxNetwork(module)
    overrides = {}
    data = network.populate(overrides)

    # populate should always return a dict
    assert isinstance(data, dict)
    # and it should not be empty
    assert data


# Generated at 2022-06-13 01:49:33.153344
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    from isc_dhcp_leases import IscDhcpLeases

    class MockModule(object):
        def __init__(self):
            self.params = dict()
            self.params['dhcp4'] = False
            self.params['dhcp6'] = False
            self.params['use_ipv6'] = False
            self.params['default_interface_ipv4'] = False
            self.params['default_interface_ipv6'] = False
            self.params['gather_network_resources'] = ['interfaces']
            self.params['gather_subset'] = ['all']
            self.run_command = lambda x, **kwargs: (0, x, '')
            self.get_bin_path = lambda x: x


# Generated at 2022-06-13 01:49:45.415544
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    from ansible.module_utils.network.common.utils import dict_diff

    # FIXME: this test is not very thorough
    def _run_module():
        module_args = dict(
            config='{"persistent_state": false}'
        )
        module = AnsibleModule(
            argument_spec=module_args,
            supports_check_mode=True
        )
        # Uses local import so we can test it
        from ansible.module_utils.network.common.network.linux.network import LinuxNetwork
        return module, LinuxNetwork(module).get_default_interfaces()

    def _run_module_v4_only():
        module_args = dict(
            config='{"persistent_state": false, "ipv4_only": true}'
        )

# Generated at 2022-06-13 01:49:50.025507
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    module = AnsibleModule(argument_spec={})
    linux_network = LinuxNetwork(module)
    data = linux_network.get_ethtool_data('test')
    assert isinstance(data['features'], dict)
    assert isinstance(data['timestamping'], list)
    assert isinstance(data['hw_timestamp_filters'], list)



# Generated at 2022-06-13 01:50:01.951717
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    l = LinuxNetwork()
    # Test with a valid device name.
    (is_valid_dev,device) = l.check_interface_valid("lo")
    assert is_valid_dev is True
    etd = l.get_ethtool_data(device)
    # Test whether ethtool command is executed.
    # ethtool should return a 'features' key
    assert 'features' in etd
    # Test the value of 'features' key.
    # NOTE: 'features' key is a dictionary
    # NOTE: dictionary key should be 'rx'
    assert 'rx' in etd['features']
    # Test the value of 'rx' key in 'features' dictionary
    # NOTE: 'rx' key in 'features' dictionary is a string
    # NOTE: one of the values in the string is 'scatter'

# Generated at 2022-06-13 01:50:08.817329
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    # construct arguments for the module that we can control in the test
    module = AnsibleModule(
        argument_spec = dict(
        )
    )

    # instantiate class
    linux_network = LinuxNetwork(module)
    # run method
    linux_network.populate()
    # check
    assert linux_network.addresses == { 'all_ipv4_addresses': ['192.0.2.1'] }

# Generated at 2022-06-13 01:50:40.668636
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    # Arrange
    class ModuleUnderTest:
        def __init__(self):
            self.module = None

        def get_bin_path(self, arg):
            return True


# Generated at 2022-06-13 01:50:41.864860
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    assert True


# Generated at 2022-06-13 01:50:52.745600
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    ln = LinuxNetwork()
    ln.get_interfaces_info = lambda a,b,c: (None, None)
    ln.get_interface_defaults = lambda : ({}, {})
    ln.populate()
    ln.populate(ignore_interfaces=[])
    ln.populate()
    ln.populate(ignore_interfaces=['eth0'])
    ln.populate(ignore_interfaces=[],
                use_ipv4=True,
                use_ipv6=True)
    assert ln.ipv4['address'] == '127.0.0.1'
    assert ln.ipv6['address'] == '::1'



# Generated at 2022-06-13 01:51:01.750610
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    module = AnsibleModule(argument_spec={})
    result = dict(
        ansible_facts={
            "ansible_network_resources": {},
            "ansible_devices": {},
        }
    )
    network = LinuxNetwork(module)
    # set up the module.paths dict for testing, if needed
    result["ansible_facts"]["ansible_paths"] = {}
    result["ansible_facts"]["ansible_paths"]["ansible_bin_dir"] = "/usr/bin"
    network.facts = result["ansible_facts"]

    # test a device without ethtool, no failure
    device = "eth0"
    network.get_ethtool_data(device)

    # test a device with ethtool, but no features, expect empty dict

# Generated at 2022-06-13 01:51:13.920255
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    """
    Method get_default_interfaces of class LinuxNetwork returns a tuple of IPv4 and IPv6 dictionaries
    which contain details on the default interface, or None if no default interface is found.
    """

    # This fixture represents the default ipv4 interface details.
    ipv4_interface_dict = {
        "interface": "eth0",
        "address": "10.10.10.42",
        "netmask": "255.255.255.0",
        "network": "10.10.10.0"
    }

    # This fixture represents the default ipv6 interface details.

# Generated at 2022-06-13 01:51:25.568771
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    from ansible.module_utils.basic import AnsibleModule
    '''The following test will assume that ethtool is present in the path,
       and that ethtool return something meaningful for all tested interfaces
    '''
    module = AnsibleModule(argument_spec=dict())
    f = FakeModule(module)
    ln = LinuxNetwork(f)
    interfaces_info = ln.get_interfaces_info(None, None, None)
    for device in interfaces_info[0]:
        ethtool_data = ln.get_ethtool_data(device)
        # 1 - if ethtool support is present, all tested devices must have the key 'features'
        assert 'features' in ethtool_data
        # 2 - if ethtool support is present, all tested devices must have the key 'timestamping'
        assert 'timestamping'

# Generated at 2022-06-13 01:51:30.891782
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():

    # mocking module.run_command
    module_obj = LinuxNetwork()
    module_obj.run_command = mock.Mock()
    # first output :
    # get_interfaces_info(ip_path='/sbin/ip',default_ipv4={},default_ipv6={})

# Generated at 2022-06-13 01:51:42.770886
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    import mock

    class Module(object):
        def __init__(self):
            pass
        def get_bin_path(self, path):
            return True

# Generated at 2022-06-13 01:51:51.025377
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    module = AnsibleModule(argument_spec=dict())
    network = LinuxNetwork(module);
    interfaces_info, default_ipv4, default_ipv6 = network.get_interfaces_info()

    # make sure the module works when /proc/net/dev doesn't have any
    # interface data
    os.rename('/proc/net/dev', '/proc/net/dev.bak')
    interface_file = open('/proc/net/dev', 'w')
    interface_file.write('')
    interface_file.close()
    interfaces_info, default_ipv4, default_ipv6 = network.get_interfaces_info()
    assert interfaces_info == {}
    assert default_ipv4 == {}
    assert default_ipv6 == {}

# Generated at 2022-06-13 01:52:00.779229
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    dev = 'eth0'

# Generated at 2022-06-13 01:52:22.297040
# Unit test for method populate of class LinuxNetwork

# Generated at 2022-06-13 01:52:33.924287
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    # TODO: a lot of dup logic with LinuxNetwork.get_interfaces_info()
    class MockedModule(object):
        def get_bin_path(self, arg, **kwargs):
            return arg

        def run_command(self, arg, **kwargs):
            return 0, "", ""
    

# Generated at 2022-06-13 01:52:41.709586
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    candidate = LinuxNetwork()
    candidate.module = MagicMock()
    candidate.get_default_interfaces = MagicMock(return_value=({'address': "172.17.0.1"}, {'address': "fe80::9eb4:4dff:fea4:7"},))
    candidate.get_interfaces_info = MagicMock(return_value=({}, {}))
    candidate.get_network_facts = MagicMock()

    fact_data = candidate.populate()

    candidate.get_default_interfaces.assert_called_with('/sbin/ip', {}, {})
    candidate.get_interfaces_info.assert_called_with('/sbin/ip', {}, {})


# Generated at 2022-06-13 01:52:51.492636
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    from ansible_collections.ansible.netcommon.tests.unit.compat.mock import patch
    from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.network import NetworkError
    from ansible_collections.ansible.netcommon.tests.unit.plugins.modules.utils import set_module_args
    from .test_linux_interfaces import TestLinuxInterfacesModule

    import sys
    sys.path.append("/path/to/ansible/ansible/lib/ansible/modules/network/linux")

    m = TestLinuxInterfacesModule()
    m.params = {
        'config': '',
        'interfaces': [],
        'naming_policy': 'mac',
        'state': '',
        'saveds': []
    }
    set_module

# Generated at 2022-06-13 01:52:58.075684
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    module = AnsibleModule(argument_spec={})
    interface = dict()

    module.get_bin_path = MagicMock(return_value="/sbin/ip")

    command = ["/sbin/ip", "-4", "route", "get", "8.8.8.8"]
    module.run_command = MagicMock(return_value=(0, "8.8.8.8 dev eth0  src 10.0.0.100 ", ""))

    obj = LinuxNetwork(module)
    ret = obj.get_default_interfaces(interface, command)

    assert ret == (0, interface)

    assert interface['v4']['interface'] == 'eth0'
    assert interface['v4']['address'] == '10.0.0.100'


# Generated at 2022-06-13 01:53:11.698470
# Unit test for method populate of class LinuxNetwork

# Generated at 2022-06-13 01:53:16.400289
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    """
    Construct LinuxNetwork object and run get_interfaces_info method
    """
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(argument_spec={})
    networking = LinuxNetwork(module)
    networking.get_interfaces_info('', '', '')


# Generated at 2022-06-13 01:53:18.155912
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    # TODO: write this
    raise SkipTest("I have not yet written this method in the unit test")

# Generated at 2022-06-13 01:53:25.012205
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    class FakeModule(object):
        def __init__(self):
            self.run_command_called = False

        def get_bin_path(self, name, opt_dirs=[]):
            return "/bin/%s" % name

        def run_command(self, cmd, check_rc=False, close_fds=False, executable=None, data=None, binary_data=False, path_prefix=None, cwd=None, use_unsafe_shell=False, prompt_regex=None, environ_update=None, umask=None, encoding=None, errors='surrogate_then_replace', expand_user=True, shell=False, ignore_errors=False, stdin=None, stdout=None, stderr=None, timeout=None):
            self.run_command_called = True
            return

# Generated at 2022-06-13 01:53:33.131631
# Unit test for method get_ethtool_data of class LinuxNetwork

# Generated at 2022-06-13 01:53:52.254090
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    # TODO: move this to a seperate test module
    from ansible.module_utils import basic
    from ansible_collections.notstdlib.moveitallout.tests.unit.compat.mock import patch, Mock

    path_exists_mock = Mock(return_value=True)
    mock_module = type('module', (object,), {'exit_json': Mock(), 'fail_json': Mock(), 'get_bin_path': Mock(return_value='/bin/ethtool')})
    with patch('os.path.exists', path_exists_mock):
        with patch.dict(basic.ANSIBLE_FACTS, {'distribution': 'Fedora'}):
            ln = LinuxNetwork()
            ln.module = mock_module
            rc = ln.get_ethtool_

# Generated at 2022-06-13 01:53:58.104213
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    module = AnsibleModule(argument_spec={}, supports_check_mode=False)
    n = LinuxNetwork(module)
    default_ipv4, default_ipv6 = n.get_default_interfaces_info()
    interfaces, ips = n.get_interfaces_info(n.paths['ip'], default_ipv4, default_ipv6)
    facts = dict(interfaces=interfaces,
                 default_ipv4=default_ipv4,
                 default_ipv6=default_ipv6,
                 ips=ips)
    facts['ansible_net_interfaces'] = {}
    facts['ansible_net_gather_network_resources'] = [
        'default_ipv4',
        'interfaces',
        'ips']

# Generated at 2022-06-13 01:54:01.388315
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    # Prepare test data and create the object
    data = dict()
    ln = LinuxNetwork(dict(module=AnsibleModule()), data)

    # Get the target method and arguments
    method = ln.populate
    args = {}

    # Return value
    return_value = method(**args)

    # Assertions (for example)
    assert return_value is None

    # Return the data
    return data

# Generated at 2022-06-13 01:54:05.808741
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    module = AnsibleModule(argument_spec={})
    interface = 'lo'
    device = LinuxNetwork(module)
    data = device.get_ethtool_data(interface)
    assert data, 'LinuxNetwork.get_ethtool_data did not return anything'
    assert 'features' in data, 'LinuxNetwork.get_ethtool_data did not return any features'
    assert 'tx_checksumming' in data['features'], 'LinuxNetwork.get_ethtool_data did not return tx_checksumming'



# Generated at 2022-06-13 01:54:09.119663
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    # Create a mock module
    module = AnsibleModule(
        argument_spec = dict(
            gather_subset=dict(type='list'),
        ),
        supports_check_mode=True,
    )

    # Create a net helper object
    network_module_helper = NetworkModuleHelper()

    network = LinuxNetwork(network_module_helper.module)
    # TODO: improve the test
    # assert the methods have been called
    network.populate()


# Generated at 2022-06-13 01:54:15.247933
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    import platform
    import shutil
    import tempfile
    import re

    def get_iface_name(x):
        """Return the name of the iface from systemd-networkd output"""
        return x[0][0].split('.')[0]

    def get_iface_method(x):
        """Return the method of the iface from systemd-networkd output"""
        return x[0][1].split('=')[1]

    def get_iface_address(x):
        """Return the address of the iface from systemd-networkd output"""
        addresses = []
        for address in x[1:]:
            addresses.append(address[1].split('=')[1])
        return addresses


# Generated at 2022-06-13 01:54:23.645485
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    from ansible.module_utils import basic
    from ansible.module_utils.facts.network.common import get_file_content

    class MockModule(object):
        def __init__(self):
            self.exit_json = basic.AnsibleModule.exit_json
            self.fail_json = basic.AnsibleModule.fail_json
            self.params = dict(
                gather_subset=['all']
            )

    class MockFile(dict):
        def __init__(self, *args, **kwargs):
            pass

        def __getattr__(self, name):
            return self.get(name)

        def __contains__(self, name):
            return True if self.get(name) else False

        def read(self):
            return self.get('content')


# Generated at 2022-06-13 01:54:35.216033
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    unittest.TestCase.maxDiff = None
    # prepare fake arguments for the test
    ip_path = 'ip'
    default_ipv4 = {'address': '127.0.0.1', 'netmask': '255.255.0.0', 'network': '127.0.0.0'}
    default_ipv6 = {'address': '::1', 'prefix': '128', 'scope': 'host'}
    # run method
    linux_network = LinuxNetwork()
    results, ippam = linux_network.get_interfaces_info(ip_path, default_ipv4, default_ipv6)
    # FIXME: remove the need for this
    from copy import deepcopy
    ips = deepcopy(ippam)
    import pprint
    pprint.pprint(results)

# Generated at 2022-06-13 01:54:46.676527
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    module_name = 'test_network'
    module_path = os.path.join(fixtures_path, 'modules', module_name)
    test_module = imp.load_source(module_name, module_path)

    obj = LinuxNetwork(test_module)
    try:
        obj.get_default_interfaces()
    except NotImplementedError:
        pass

    test_module.run_command = Mock(return_value=(0, 'default via 192.168.1.1 dev eno16777736', ''))
    # Legacy return
    def_ipv4, def_ipv6 = obj.get_default_interfaces()
    assert def_ipv4['ipv4']['gateway'] == '192.168.1.1'

    # FIXME: this should be tested too
   

# Generated at 2022-06-13 01:54:57.670455
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    def _test(_input, _output, _test_device_name):
        m = mock.mock_open(_read_data=_input)
        with mock.patch('ansible.module_utils.basic.AnsibleModule.run_command', return_value=(0, '', '')), mock.patch('builtins.open', m):
            linux_network = LinuxNetwork('module')
            assert linux_network.get_ethtool_data(_test_device_name) == _output
    # Success case

# Generated at 2022-06-13 01:55:22.518870
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    module = AnsibleModule({})
    ln = LinuxNetwork(module)

    # Generate the fake output

# Generated at 2022-06-13 01:55:32.357719
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    #TODO: Compose the required data for args and kwargs
    #args = ['arg1', 'arg2', ...]
    args = []
    #kwargs = {'kwarg1': 'kwarg1', 'kwarg2': 'kwarg2', ...}
    kwargs = {}
    module = MagicMock(name='module')
    #module.run_command = {'stdout': 'stdout', 'stderr': 'stderr', 'rc': 0}
    module.run_command = {'rc': 0}
    n = LinuxNetwork(module)
    n.interfaces = {}
    n.interfaces = {'interface1': 'interface1'}
    n.ips = {}
    n.ips = {'all_ipv6_addresses': ['1234::']}
    n

# Generated at 2022-06-13 01:55:44.020846
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():

    module = AnsibleModule(argument_spec=dict())
    module.run_command = Mock()

    linux = LinuxNetwork(module)

    unit_test_utils.get_ethtool_testcase('eth0', 0, ['rx', 'tx', 'tx-non-tcp', 'rx-check'],
                                         ['rx', 'tx', 'tx-non-tcp', 'rx-check'], 3, 1, True, linux)
    unit_test_utils.get_ethtool_testcase('eth1', 1, ['tx', 'rx'], ['tx', 'rx'], 3, 2, False, linux)
    unit_test_utils.get_ethtool_testcase('eth2', 2, None, None, 3, 1, False, linux)

# Generated at 2022-06-13 01:55:48.877576
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    m = MockModule()
    ln = LinuxNetwork(m)
    ln.EXEC_PATHS.update(dict(ethtool='/usr/bin/ethtool'))
    ethtool_mock = MagicMock()
    with patch.multiple(ln, get_bin_path=MagicMock(return_value='/usr/bin/ethtool'),
                        run_command=ethtool_mock):
        ethtool_mock.return_value = (0, "", "")
        data = ln.get_ethtool_data('eth0')
        assert data == {'features': {}, 'timestamping': [], 'hw_timestamp_filters': []}


# Generated at 2022-06-13 01:55:58.586045
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    m = AnsibleModuleMock()
    ln = LinuxNetwork(m)

    # ethtool not installed
    m.get_bin_path.return_value = "/usr/bin/ethtool"
    m.run_command.side_effect = [
        (1, b"", b""),
        (1, b"", b""),
        (1, b"", b""),
        (1, b"", b""),
        (1, b"", b""),
    ]
    assert ln.get_ethtool_data("eth0") == {}

    # ethtool installed

# Generated at 2022-06-13 01:56:06.052789
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    # Initialize empty test object
    linux_network = LinuxNetwork()
    device = 'eth0'

# Generated at 2022-06-13 01:56:18.391046
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    module = MockModule()    
    linux_network = LinuxNetwork(module)
    ip_path = module.get_bin_path("ip")
    default_ipv4 = {'address':'10.0.2.15'}
    default_ipv6 = {'address':'2001:db8::ff00:42:8329'}
    (interfaces, ips) = linux_network.get_interfaces_info(ip_path, default_ipv4, default_ipv6)
    assert(interfaces['eth0']['macaddress'] == '56:43:92:1A:B7:0D')
    assert(interfaces['eth0']['ipv4']['address'] == '10.0.2.15')

# Generated at 2022-06-13 01:56:27.286335
# Unit test for method get_interfaces_info of class LinuxNetwork

# Generated at 2022-06-13 01:56:35.247385
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    M = AnsibleModule({})
    LN = LinuxNetwork(M)

    M.run_command = Mock(return_value=(0, '', ''))

    # /sys/class/net/enp0s3/address
    macaddress = '52:54:00:12:34:56'
    # /sys/class/net/enp0s3/mtu
    mtu = 1500
    # /sys/class/net/enp0s3/operstate
    active = True
    # /sys/class/net/enp0s3/type
    device_type = '1'
    # /sys/class/net/enp0s3/iflink
    iflink = '3'
    # /sys/class/net/enp0s3/device/driver/module

# Generated at 2022-06-13 01:56:43.445537
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    '''test method get_interfaces_info of class LinuxNetwork'''

    # FIXME: dir_util functions need os and shutil available
    # FIXME: also this needs sys.path.append(parent_dir)
    parent_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    sys.path.insert(0, parent_dir)
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_bytes, to_native
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.module_utils.parsing.convert_bool import boolean
    import ansible.module_utils.basic
    import shutil
    # FIXME: why is this second import of

# Generated at 2022-06-13 01:57:08.499201
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():

    def get_ethtool_data(self):
        output = {}
        if self.ethtool_path:
            args = [self.ethtool_path, '-k', self.interface]
            rc, stdout, stderr = self.module.run_command(args, errors='surrogate_then_replace')
            if rc == 0:
                features = {}
                for line in stdout.strip().splitlines():
                    if not line or line.endswith(":"):
                        continue
                    key, value = line.split(": ")
                    if not value:
                        continue
                    features[key.strip().replace('-', '_')] = value.strip()
                output['features'] = features

            args = [self.ethtool_path, '-T', self.interface]
            rc, stdout, stder

# Generated at 2022-06-13 01:57:16.495298
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    # Make sure we have a class to test
    assert LinuxNetwork

    # Initialize a variable for the facts dict
    output = dict()

    # Initialize class
    linux_network = LinuxNetwork(None, None)

    # Populate the variable with the facts from the class
    linux_network.populate()
    # Store the facts in the output dict
    facts = linux_network.facts

    # Assert the default localhost facts are present
    assert 'ansible_facts' in facts
    assert 'ansible_network_resources' in facts['ansible_facts']
    assert 'default_ipv4' in facts['ansible_facts']['ansible_network_resources']
    assert 'default_ipv6' in facts['ansible_facts']['ansible_network_resources']

# Generated at 2022-06-13 01:57:25.722220
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    mocked_linux_net = create_autospec(LinuxNetwork)
    mocked_linux_net.module = Mock()

# Generated at 2022-06-13 01:57:29.412883
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    hostvars = {}
    network = LinuxNetwork(module=None)
    network.populate(hostvars)
    assert hostvars['ansible_all_ipv4_addresses'] == []
    assert hostvars['ansible_all_ipv6_addresses'] == []
    assert 'ansible_interface_mapping' in hostvars
    assert 'ansible_default_ipv6' in hostvars
    assert 'ansible_default_ipv4' in hostvars
    assert hostvars['ansible_interfaces'] == ['lo']



# Generated at 2022-06-13 01:57:35.522966
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    module = AnsibleModule(
        argument_spec = dict(
            gather_subset=dict(default=['!all'], type='list'),
            dir_path=dict(default='/etc/ansible')
        ),
        supports_check_mode=True,
    )
    result = dict(
        changed=False,
        ansible_facts=dict()
    )
    target = LinuxNetwork(module=module)

    # TODO: test the gather_subset here?
    target.populate()


# Generated at 2022-06-13 01:57:45.736289
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    # Test with a "with" statement so we get error handling/messaging
    # Test with a "with" statement so we get error handling/messaging
    with LinuxNetwork(omit=['all_ipv4_addresses', 'all_ipv6_addresses']) as linux_network:
        linux_network.populate()
        assert 'interfaces' in linux_network.data
        assert 'default_ipv4' in linux_network.data
        assert 'default_ipv6' in linux_network.data
        assert linux_network.data['default_ipv6']['address'] == os.getenv('default_ipv6', '::')
        assert 'dns' in linux_network.data
        assert 'default_ipv4' in linux_network.data

# Generated at 2022-06-13 01:57:52.392088
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    # Call class constructor to create a new object
    o = LinuxNetwork()

    # Create a module and set the module arguments to the dict below
    # NOTE: module arguments makes up the kwargs dict passed to the __init__
    module = AnsibleModule(
        argument_spec = {},
        supports_check_mode = False,
    )

    # set module.params and run
    module.params = {'path': '/bin:/sbin:/usr/bin:/usr/sbin'}
    o.populate(module)

    # Check the results
    assert o.default_ipv4 == {'broadcast': '', 'address': '127.0.0.1', 'network': '127.0.0.0', 'netmask': '255.0.0.0'}

# Generated at 2022-06-13 01:57:58.638239
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    # The input param must be a dict
    # The return must be a 2-tuple
    # test if ipv4 and ipv6 are present in the output
    # test that all interfaces are present
    # test that all interfaces are present multiple times
    # test that all interfaces have a ipv4 and ipv6 address
    pass


# Generated at 2022-06-13 01:58:07.480646
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    fake_ansible_module = AnsibleModule(
        argument_spec=dict(),
    )

    module = LinuxNetwork(fake_ansible_module)

    fake_ip_path = "/bin/ip"

# Generated at 2022-06-13 01:58:07.973898
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    pass