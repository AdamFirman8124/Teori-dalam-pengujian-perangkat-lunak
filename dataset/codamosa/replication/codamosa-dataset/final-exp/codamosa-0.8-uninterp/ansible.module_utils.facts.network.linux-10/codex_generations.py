

# Generated at 2022-06-13 01:48:50.134343
# Unit test for method get_interfaces_info of class LinuxNetwork

# Generated at 2022-06-13 01:48:52.430867
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    # get_interfaces_info should return a dict of dicts with the device as key
    result = LinuxNetwork().get_interfaces_info({}, {})
    assert isinstance(result, dict)
    assert isinstance(result[0], dict)
    assert isinstance(result[0].values()[0], dict)



# Generated at 2022-06-13 01:48:59.351416
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
  expected = {'v4': {'address': '192.168.1.56', 'gateway': '192.168.1.1', 'interface': 'enp0s3'}, 'v6': {'address': 'fe80::5054:ff:feb0:80b4', 'gateway': 'fe80::5054:ff:feb0:1', 'interface': 'enp0s3'}}
  ln = LinuxNetwork(dict(module=None))
  actual = ln.get_default_interfaces()
  assert actual == expected, "expected %s, got %s" % (expected, actual)


# Generated at 2022-06-13 01:49:10.357098
# Unit test for method get_default_interfaces of class LinuxNetwork

# Generated at 2022-06-13 01:49:20.651148
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import dict_merge
    from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import parse_result
    module = None
    result = parse_result('')
    linux_network = LinuxNetwork(module)
    cmd = {'bin_path': '/bin', 'run_command': lambda *args, **kwargs: (1, '', '')}
    paths = {'ip': '/bin/ip'}
    interfaces = linux_network.get_interfaces_info(paths, result['default_ipv4'], result['default_ipv6'])

# Generated at 2022-06-13 01:49:27.489613
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    module = mock.MagicMock()
    module.run_command.return_value = (0, "", "")
    instance = LinuxNetwork('/bin/true', module)

    # Check expected output with no command output
    rc, stdout, stderr = (0, '', '')
    module.run_command.assert_any_call(['/bin/true', '-k', ''])
    module.run_command.assert_any_call(['/bin/true', '-T', ''])
    assert instance.get_ethtool_data('') == {}

    # Check expected output with some command output
    rc, stdout, stderr = (0, '', '')
    module.run_command.return_value = (rc, stdout, stderr)
    module.run_command.assert_any

# Generated at 2022-06-13 01:49:36.791709
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    """
    test_LinuxNetwork_populate is the unit test for LinuxNetwork.populate
    @return: None
    """
    # set the module arguments

# Generated at 2022-06-13 01:49:41.775379
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    # Given
    module = AnsibleModule(argument_spec={})
    module.run_command = MagicMock(return_value=(0, '1.1.1.1', ''))
    ln = LinuxNetwork(module)

    # When - then
    default_v4, default_v6 = ln.get_default_interfaces()
    module.run_command.assert_called_with([module.get_bin_path('ip'), 'route', 'get', '8.8.8.8'])
    assert default_v4 == {'address': '1.1.1.1'}
    assert default_v6 == {}



# Generated at 2022-06-13 01:49:47.733079
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    in_dict = dict(
        module=dict(
            run_command=lambda *args: (0, '', '')
        )
    )
    network = LinuxNetwork(in_dict, dict())
    # Note: Route.populate isn't actually a method of Route
    # Note: Route.populate mutates the object it's called on
    # Note: Route.populate doesn't return anything, so result is None
    result = network.populate()
    assert not result



# Generated at 2022-06-13 01:49:59.521139
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    def _get_file_content(path):
        return '00:a0:c9:14:c8:29'

    import ansible.module_utils.basic
    from ansible.module_utils.facts import DefaultCollector

    class Mock(object):
        def __init__(self, *args, **kwargs):
            pass

        def get_bin_path(self, *args, **kwargs):
            return "/sbin/ip"

    class MockModuleUtils(object):
        class AnsibleModule(object):
            def __init__(self, *args, **kwargs):
                pass

            def run_command(self, *args, **kwargs):
                return 0, '', ''

    ln = LinuxNetwork(Mock(), MockModuleUtils())

    ln.get_file_content = _

# Generated at 2022-06-13 01:50:53.882632
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    mock_module = AnsibleModule(argument_spec=dict(
        name=dict(type='str', default='eth0')
    ))
    mock_module.exit_json = lambda x: x
    mock_module.run_command = Mock(return_value=(0, '', ''))
    mock_module.get_bin_path = lambda x: '/bin/ethtool'

# Generated at 2022-06-13 01:51:04.674197
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    # FIXME: This could use a lot more tests.
    # It looks like this was started, then forgotten?
    module = AnsibleModule(argument_spec={})
    module.run_command = mock.MagicMock()
    module.run_command.return_value = (0, '', '')
    network = LinuxNetwork(module)


# Generated at 2022-06-13 01:51:09.424240
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():

        # Test invocation without argument.
        # Test will fail if exception is not raised (no LinuxNetwork object returned)
        with pytest.raises(Exception):
            LinuxNetwork()

        # Test invocation with correct argument
        ln = LinuxNetwork(AnsibleModuleDummy)
        assert ln



# Generated at 2022-06-13 01:51:17.982772
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    from ansible.module_utils.basic import AnsibleModule
    # Mock the module's AnsibleModule class
    am = AnsibleModule(argument_spec={})
    def mock_AnsibleModule_run_command(self, args, errors='surrogate_then_replace', check_rc=True):
        stdout = None
        rc = 0

# Generated at 2022-06-13 01:51:27.727722
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    get_interfaces_info = LinuxNetwork(None).get_interfaces_info
    assert get_interfaces_info("", {}, {}) == ({}, {'all_ipv4_addresses': [], 'all_ipv6_addresses': []})

# Generated at 2022-06-13 01:51:39.828555
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    import sys
    import os
    import __builtin__ as builtins
    class Mock(object):
        def __init__(self, *args, **kwargs):
            pass

        def get_bin_path(self, path, required=True):
            return "/bin/%s" % path

        def run_command(self, args, errors='surrogate_then_replace'):
            class Bunch(object):
                def __init__(self, **kwds):
                    self.__dict__.update(kwds)

            if args[0] == "/bin/ethtool":
                with open(os.path.join(os.path.dirname(__file__), 'ethtool_sample_output.txt'), 'r') as f:
                    return (0, f.read(), "")

# Generated at 2022-06-13 01:51:44.574042
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    module = AnsibleModule(argument_spec=dict(
        default_ipv4=dict(default=dict(address=None, netmask=None, network=None, broadcast=None), type='dict'),
        default_ipv6=dict(default=dict(address=None, prefix=None, network=None, scope='link'), type='dict'),
        ip_path=dict(default='/sbin/ip'),
    ))
    l = LinuxNetwork(module)
    # NOTE: not using assert_equal because it would be alot of typing
    #       we want to assert that these are equal, but the error message
    #       would be better if we used the assert_* methods

# Generated at 2022-06-13 01:51:45.363893
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    pass
    

# Generated at 2022-06-13 01:51:48.299548
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    # TODO: mock files in /sys
    module = AnsibleModule(argument_spec={}, supports_check_mode=True)

    rval = LinuxNetwork(module).get_interfaces_info()
    assert isinstance(rval, dict)



# Generated at 2022-06-13 01:51:58.385157
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():

    class MockModule(object):
        def run_command(self, args, errors='surrogate_then_replace'):
            return 0, '', ''

        def get_bin_path(self, arg):
            return None

    class MockNetwork(LinuxNetwork):
        def get_default_interfaces(self):
            return {'default_ipv4': {'address': ''}, 'default_ipv6': {'address': ''}}

        def get_route_info(self, ip_path):
            return {'v4': {}, 'v6': {}}

    ln = MockNetwork(MockModule())
    interfaces, ips = ln.get_interfaces_info(None)

    assert isinstance(interfaces, dict)
    assert isinstance(ips, dict)

# Generated at 2022-06-13 01:52:38.983969
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    # Initialization and setup
    module = AnsibleModule(argument_spec={
    })

    module.get_bin_path = MagicMock(return_value='/bin/')
    module.run_command = MagicMock(return_value=(0, '', ''))

    # Test the method
    linux_network = LinuxNetwork(module)
    assert linux_network.populate() is None



# Generated at 2022-06-13 01:52:45.037705
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    device = "test_device"
    module = AnsibleModuleMock()
    module.get_bin_path.return_value = True
    e = LinuxNetwork(module)

    args = [ethtool_path, '-k', device]

# Generated at 2022-06-13 01:52:50.855213
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    """
    For now, we just make sure that get_interfaces_info() does not raise an exception
    """
    module = MagicMock()
    module.run_command = MagicMock(return_value=(0, "", ""))
    module.get_bin_path = MagicMock(return_value=None)
    class_obj = LinuxNetwork(module)
    class_obj.get_interfaces_info(None, dict(), dict())



# Generated at 2022-06-13 01:52:56.032375
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    com = "ifconfig -a"

    # Example output of ifconfig

# Generated at 2022-06-13 01:53:08.500970
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data(): # pylint: disable=invalid-name
    (data, _) = LinuxNetwork().get_ethtool_data("lo")
    assert 'features'  in data
    assert isinstance(data['features'], dict)
    assert 'tx_checksumming' in data['features']
    assert 'timestamping' in data
    assert isinstance(data['timestamping'], list)
    assert 'tx_types' in data['timestamping']
    assert 'hw_timestamp_filters' in data
    assert isinstance(data['hw_timestamp_filters'], list)
    assert 'all' in data['hw_timestamp_filters']
    assert 'phc_index' in data
    assert data['phc_index'] == 0


# Generated at 2022-06-13 01:53:19.329661
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    # This is a unit test.
    # TODO: add more tests
    import os
    import sys
    import json
    import mock
    import collections

    # Mock the core module
    MockedModule = collections.namedtuple('MockedModule', [
        'run_command',
        'load_file',
        'get_bin_path',
    ])
    module = MockedModule(
        run_command=mock.Mock(),
        load_file=mock.Mock(),
        get_bin_path=mock.Mock()
    )
    module.run_command.return_value = [0, 'eth0', '']
    module.get_bin_path.return_value = '/bin/ip'

# Generated at 2022-06-13 01:53:21.967511
# Unit test for constructor of class LinuxNetworkCollector
def test_LinuxNetworkCollector():
    """
    Constructor test of LinuxNetworkCollector class
    """
    module = AnsibleModule(argument_spec=dict())
    collector_obj = LinuxNetworkCollector(module)
    assert collector_obj._platform == 'Linux'
    assert collector_obj._fact_class == LinuxNetwork
    assert collector_obj.required_facts == {'distribution', 'platform'}


# Generated at 2022-06-13 01:53:24.356411
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    module = get_test_module_argspec()
    module.params = {}

    ln = LinuxNetwork()
    ln.module = module
    ln.populate()

    assert ln.ipv4
    assert ln.ipv6
    assert ln.default_ipv4



# Generated at 2022-06-13 01:53:30.580364
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    '''
    Test method / module
    '''
    module = AnsibleModule(argument_spec={})

    # FIXME: test against "real" output
    module.run_command = MagicMock(return_value=(0, '192.168.1.1', ''))
    module.get_bin_path = MagicMock(return_value=True)

    obj = LinuxNetwork(module)
    ipv4, ipv6 = obj.get_default_interfaces()
    assert ipv4 == {'address': '192.168.1.1'}
    assert isinstance(ipv6, dict)


# Generated at 2022-06-13 01:53:41.717410
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    ln = LinuxNetwork()
    ln.module = FakeModule()

    # test 1: missing ethtool_bin
    result = ln.get_ethtool_data(device="eth0")
    expected = {}
    assert result == expected, "result is '%s' instead of '%s'" % (result, expected)

    # test 2: not all options enabled
    ln.module.set_base_bin_paths('/sbin')
    result = ln.get_ethtool_data(device="eth0")

# Generated at 2022-06-13 01:54:29.272030
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    # TODO: actually write a test for this class

    obj = LinuxNetwork()
    module = DummyModule()
    obj.module = module
    obj.populate()

    rc, out, err = module.run_command([module.get_bin_path("ip"), 'addr', 'show', 'dev', 'eth0'])
    if rc != 0:
        raise AssertionError()


# Generated at 2022-06-13 01:54:41.311746
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    '''
    Unit test for method get_ethtool_data of class LinuxNetwork
    '''
    import ansible.module_utils.basic
    import ansible.module_utils.network.common.utils
    import ansible.module_utils.network.common.config
    import ansible.module_utils.network.common.ansible_utils
    import ansible.module_utils.network.common.ifconfig
    import ansible.module_utils.network.linux.iproute2
    import ansible.module_utils.network.linux.route
    import ansible.module_utils.network.linux.netinfo
    import ansible.module_utils.network.linux.bond
    import ansible.module_utils.network.linux.base

    module = ansible.module_utils.basic.AnsibleModule

# Generated at 2022-06-13 01:54:48.493591
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    test_object = LinuxNetwork()
    # FIXME: test with bad paths?
    fake_ip_path = '/bin/ip'
    fake_default_ipv4 = {}
    fake_default_ipv6 = {}
    assert test_object.get_interfaces_info(fake_ip_path, fake_default_ipv4, fake_default_ipv6) == ({}, {'all_ipv6_addresses': [], 'all_ipv4_addresses': []})


# Generated at 2022-06-13 01:55:00.786527
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    from ansible_collections.ansible.netcommon.tests.unit.compat.mock import MagicMock


# Generated at 2022-06-13 01:55:09.755236
# Unit test for method get_ethtool_data of class LinuxNetwork

# Generated at 2022-06-13 01:55:20.583015
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    from ansible.module_utils import basic

    class ModuleCmd(object):
        def __init__(self):
            self.run_command_calls = []
            self.run_command_rcs = []
            self.run_command_exceptions = []
            self.get_bin_path_calls = []
            self.get_bin_path_paths = []

        def run_command(self, args, **kwargs):
            self.run_command_calls.append(args)
            if self.run_command_exceptions:
                raise self.run_command_exceptions.pop(0)
            rc = self.run_command_rcs.pop(0)
            if rc == 0:
                return (0, '', '')
            return (rc, '', 'command failed')


# Generated at 2022-06-13 01:55:31.538208
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    # setup
    import mock
    import sys
    if sys.version_info.major == 2:
        import __builtin__ as builtins
    else:
        import builtins
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes

    mock_module = mock.MagicMock(basic.AnsibleModule)
    mock_module.run_command = mock.MagicMock()
    mock_module.get_bin_path = mock.MagicMock()
    mock_module.run_command.return_value = (0, '', '')
    mock_module.get_bin_path.return_value = "/bin/ip"

    mock_open = mock.mock_open(read_data='00:1a:4a:16:01:38')

# Generated at 2022-06-13 01:55:33.613806
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    assert LinuxNetwork(None).get_ethtool_data(None) is not None


# Generated at 2022-06-13 01:55:41.402870
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    """
    Test LinuxNetwork.get_interfaces_info()
    """
    from ansible.module_utils.basic import AnsibleModule
    global module
    module = AnsibleModule(
        argument_spec=dict(
            gather_network_resources=dict(type='int', required=False, default=1)
        )
    )

    linux_network = LinuxNetwork()
    netinfo = linux_network.get_interfaces_info()
    assert isinstance(netinfo, dict)



# Generated at 2022-06-13 01:55:44.018237
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    obj = LinuxNetwork()
    out = obj.get_ethtool_data('eth0')
    assert isinstance(out, dict)


# Generated at 2022-06-13 01:56:29.219843
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    dummy_module = AnsibleModule(argument_spec={})
    dummy_module.run_command = Mock(return_value=(0, "", ""))
    ln = LinuxNetwork(dummy_module)

    # No route, no IP
    dummy_module.run_command.return_value = (1, "", "")
    assert ln.get_default_interfaces() == ({'v4': None, 'v6': None}, {})

    # No IPv4
    dummy_module.run_command.return_value = (0, """::1 dev lo proto kernel metric 256 pref medium
    default dev eth0 metric 100  proto bird pref medium
    default via fe80::c23:fcff:fe95:9e82 dev eth0 metric 100  proto bird pref medium""", "")
    expected_interface = {}
    expected_interface

# Generated at 2022-06-13 01:56:38.364528
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    import unittest
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes

    class TestLinuxNetwork(unittest.TestCase):
        def setUp(self):
            class ModuleStub(object):
                _ansible_module = None
                def __init__(self):
                    self.params = dict(
                        name='test',
                    )
                def get_bin_path(self, arg):
                    return '/usr/bin/%s' % arg

# Generated at 2022-06-13 01:56:43.632534
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    # file functions
    with patch('os.path.isfile', Mock(return_value=True)):
        with patch('os.stat', Mock(return_value=Mock(st_mode=33188))):
            with patch('os.access', Mock(return_value=True)):
                def mock_get_file_content(path):
                    return 'test'

                # get_file_content

# Generated at 2022-06-13 01:56:48.931634
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    module = AnsibleModule(argument_spec={'gather_subset': dict(type='list', required=True, elements='str')})
    mod = LinuxNetwork(module)
    res = mod.get_default_interfaces()
    assert res == ('eth0', 'ens224')

# Generated at 2022-06-13 01:56:58.709451
# Unit test for method populate of class LinuxNetwork

# Generated at 2022-06-13 01:57:07.999305
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():

    # create an instance of the LinuxNetwork class
    network = LinuxNetwork()
    network.module = AnsibleModuleMock()
    # initialise interfaces
    # set some extra attributes to the instance
    network.device = 'eth0'
    network.family = None
    network.bond = {}
    network.vlan = {}
    network.gateway = {}
    network.bridge = {}
    network.ipv4 = {'address': '10.0.0.2', 'netmask': '255.255.255.0', 'gateway': '10.0.0.1'}

# Generated at 2022-06-13 01:57:16.262957
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    interfaces = {}

    # FIXME: this module is tested below, do we need to split it?
    ip_path = ''
    default_ipv4 = {}
    default_ipv6 = {}
    # TODO: put in a dict that can be passed to the constructor?
    #       that could replace most of the mocking below
    linux_network = LinuxNetwork()
    linux_network.module = ansible_module_mock()
    linux_network.module.get_bin_path = lambda *a: False
    interfaces, ips = linux_network.get_interfaces_info(ip_path, default_ipv4, default_ipv6)
    assert interfaces == {}
    assert ips == dict(all_ipv4_addresses=[], all_ipv6_addresses=[])

    # FIXME: this module is

# Generated at 2022-06-13 01:57:16.790022
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    assert False



# Generated at 2022-06-13 01:57:25.945286
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    module = AnsibleModule({})
    network = LinuxNetwork(module)

    # Case 1

# Generated at 2022-06-13 01:57:33.273386
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():

    import random
    import string
    import unittest

    class TestLinuxNetwork(unittest.TestCase):

        # FIXME: is this really worth it?
        def generate_random_string(self, length=8, chars=string.ascii_letters + string.digits):
            return ''.join(random.choice(chars) for _ in range(length))

        def test_get_interfaces_info(self):
            ansible_module = AnsibleModule(argument_spec={}, supports_check_mode=True)
            linux_network = LinuxNetwork(ansible_module)
            ip_path = linux_network.module.get_bin_path("ip")
            # FIXME: does this need to be random?
            # FIXME: does ipv6 need to be random?
            device = linux_network.gener