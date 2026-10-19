

# Generated at 2022-06-13 01:48:54.079852
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    class TestModule:
        def get_bin_path(self, name, required=False):
            return '/sbin/ip'

        def run_command(self, args, errors='surrogate_then_replace'):
            stdout = '''
inet 192.168.1.1/24 brd 192.168.1.255 scope global eth0
inet6 fe80::215:5dff:fe00:41d1/64 scope link
inet6 fd00::215:5dff:fe00:41d1/64 scope link
'''
            return 0, stdout, ''

    ln = LinuxNetwork(TestModule()).get_default_interfaces()
    assert ln['default_ipv4']['address'] == '192.168.1.1'

# Generated at 2022-06-13 01:49:04.974467
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    """Return the default interface for IPv{4,6}"""
    from distutils.version import LooseVersion

    module = AnsibleModule(
        argument_spec=dict(
            _ansible_check_mode=dict(default=False, type='bool'),
            _ansible_debug=dict(default=False, type='bool'),
        ),
        supports_check_mode=True,
    )
    obj = LinuxNetwork(module)
    rc, default_ipv4, default_ipv6 = obj.get_default_interface()
    assert rc == 0
    assert default_ipv4
    assert isinstance(default_ipv4, dict)
    assert 'address' in default_ipv4
    assert default_ipv6
    assert isinstance(default_ipv6, dict)
    assert 'address' in default_

# Generated at 2022-06-13 01:49:12.770970
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    module = AnsibleModule(argument_spec={})
    module.exit_json = lambda x: x
    command = 'cat %s' % os.path.join(CURR_PATH, 'sample_data', 'ip_addr_show_%s')
    module.run_command = lambda command: (0, command, '')
    # module.run_command = lambda command: (0, '%s %s' % (command, command), '')
    # module.run_command = lambda command: (0, '%s %s %s %s %s %s' % (command, command, command, command, command, command), '')
    network = LinuxNetwork(module, command)
    interfaces, ips = network.get_interfaces_info('/sbin/ip', {}, {})

# Generated at 2022-06-13 01:49:14.332407
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    # Create a LinuxNetwork object
    module = AnsibleModule(argument_spec=dict())
    ln = LinuxNetwork(module)
    rc, out, err = ln.get_default_interfaces()
    return out

# Generated at 2022-06-13 01:49:22.793828
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    from ansible.module_utils.basic import AnsibleModule, get_distribution

    module = AnsibleModule(
        argument_spec={},
        supports_check_mode=False,
    )
    distribution = get_distribution()
    if distribution.lower() in ('freebsd', 'macosx'):
        module.exit_json(**{'distribution': distribution, 'changed': False})
    linux_network = LinuxNetwork(module)

# Generated at 2022-06-13 01:49:29.400109
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    modobj = LinuxNetwork()
    modobj.module = Mock()
    # mock ethtool -T output for a VF
    modobj.module.run_command.return_value = (0, "Capabilities: none\nSOF_TIMESTAMPING_SOFTWARE SOF_TIMESTAMPING_RX_SOFTWARE SOF_TIMESTAMPING_RAW_HARDWARE\n", "")
    assert modobj.get_ethtool_data('eth0') == {'timestamping': ['software', 'rx_software', 'raw_hardware']}
    # mock ethtool -T output for a PF

# Generated at 2022-06-13 01:49:38.059455
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    class WithExitCodeZero(Base):
        def __init__(self, module_name, args=(), **kwargs):
            self.module = module_name
            self.args = args
            self.__dict__.update(kwargs)

        def run_command(self, args, **kwargs):
            return (0, "", "")

    linux_network = LinuxNetwork(WithExitCodeZero("mock module"))
    default_ipv4 = {'address': '192.0.2.1'}
    default_ipv6 = {'address': '2001:db8::1', 'scope': 'link'}
    interfaces, ips = linux_network.get_interfaces_info("ip path",
                                                        default_ipv4,
                                                        default_ipv6)

# Generated at 2022-06-13 01:49:48.510170
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    '''
    test LinuxNetwork_get_default_interfaces
    '''
    target = LinuxNetwork()

    # ip route show 0/0
    # default via 10.0.1.1 dev eth1
    target.get_default_interfaces = MagicMock(return_value=(dict(interface="eth1", address="10.0.1.1"), dict()))
    assert dict(interface="eth1", address="10.0.1.1"), dict() == target.get_default_interfaces()

    # ip route show 0/0
    # default dev eth1  scope link  metric 100
    target.get_default_interfaces = MagicMock(return_value=(dict(interface="eth1"), dict()))
    assert dict(interface="eth1"), dict() == target.get_default_interfaces()

    # ip route

# Generated at 2022-06-13 01:49:54.190137
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    module = AnsibleModule(argument_spec={})
    module.run_command = MagicMock(return_value=(1, None, None))
    ln = LinuxNetwork(module)
    ln.populate()
    assert "default_ipv4" in ln.facts
    assert "default_ipv6" in ln.facts
    assert "interfaces" in ln.facts
    assert "all_ipv4_addresses" in ln.facts
    assert "all_ipv6_addresses" in ln.facts
    assert "interface_ip" in ln.facts
    assert "dns" in ln.facts
    assert "ipv4" in ln.facts
    assert "ipv6" in ln.facts
    assert "routes6" in ln.facts

# Generated at 2022-06-13 01:50:05.897137
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    import os
    import json
    import sys
    import tempfile
    import shutil
    from xml.etree import ElementTree

    from datetime import datetime
    from ansible_collections.notstdlib.moveitallout.tests.unit.compat import unittest
    from ansible_collections.notstdlib.moveitallout.tests.unit.compat.mock import patch

    def create_fake_interface(path, filename, interface_name, device_type, mac_address, mtu=None):
        """Create a fake network interface in the fake sys_class_net dir so that
        get_interfaces_info can find it.
        """
        # NOTE: a lot of this is duplicating the real purpose of os.makedirs
        # do we want to mock makedirs (and then rm -r in

# Generated at 2022-06-13 01:50:57.707845
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    myobj = LinuxNetwork()
    myobj.module = AnsibleModuleStub()
    myobj.module.get_bin_path = _default_mock_get_bin_path
    myobj.module.run_command = _default_mock_run_command

    #################################################################################
    # ADD YOUR TESTS HERE
    #################################################################################

    # test with ethtool_path = None
    #################################################################################
    ethtool_path = None
    device = "wxh"
    expected_return_value = {}
    #################################################################################
    return_value = myobj.get_ethtool_data(device)
    assert return_value == expected_return_value
    # test with ethtool_path = '/usr/sbin/ethtool' and device = 'eth0'
    #################################################################################
    ethtool

# Generated at 2022-06-13 01:51:10.229238
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    module = AnsibleModule(argument_spec={})

    class Args:
        module = module

    class Module:

        @staticmethod
        def get_bin_path(arg, opt_dirs=[]):
            if arg == 'ethtool':
                return arg
            return None

        class run_command:
            class run_command():
                def __init__(self):
                    self.rc = 0

# Generated at 2022-06-13 01:51:22.684876
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    class ModuleMock:
        def __init__(self, ignore_stderr=False, **kwargs):
            self.ignore_stderr = ignore_stderr


# Generated at 2022-06-13 01:51:30.402992
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    # TODO: this should be done with a patched module instead of mocking?
    #       It would also need to be patched at the class-level
    from collections import namedtuple
    from ansible.module_utils.basic import AnsibleModule

    # Mocking AnsibleModule
    FakeModule = namedtuple('FakeModule', ['run_command', 'get_bin_path'])
    FakeModule.run_command = lambda *args, **kwargs: (0, '', None)
    FakeModule.get_bin_path = lambda *args, **kwargs: '/tmp/does/not/exist'
    module = FakeModule(run_command='run_command', get_bin_path='get_bin_path')

    import sys
    sys.modules['ansible.module_utils.basic'] = FakeModule

# Generated at 2022-06-13 01:51:42.377190
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    module = AnsibleModule(argument_spec={})
    network = LinuxNetwork(module)
    default_ipv4, default_ipv6 = network.get_default_interfaces()
    ip_path = network.module.get_bin_path("ip")

    def mock_get_file_content(filename, default=None):
        if filename == '/proc/net/route':
            return b''
        elif filename == '/proc/net/ip_conntrack':
            return b''
        elif filename == '/proc/net/nf_conntrack':
            return b''
        elif filename == '/proc/net/fib_trie':
            return b''
        elif filename == '/proc/net/ip_tables_names':
            return b''

# Generated at 2022-06-13 01:51:50.786408
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    with patch('ansible_collections.ansible.netcommon.plugins.module_utils.network.common.linux.Linux.get_bin_path') as get_bin_path_mock:
        with patch('ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils.get_file_content') as get_file_content_mock:

            get_bin_path_mock.return_value = '/usr/sbin/ip'

            # Set the return value for get_file_content for the following files:
            # /sys/class/net/eth0/address
            # /sys/class/net/eth0/mtu
            # /sys/class/net/eth0/operstate
            # /sys/class/net/eth0/device/driver/module
            # /sys

# Generated at 2022-06-13 01:52:00.560256
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    src_device = 'source_device'
    src_ipv4_address = 'source_ipv4_address'
    src_ipv6_address = 'source_ipv6_address'
    src_mtu = 'source_mtu'
    src_macaddress = 'source_macaddress'
    src_bridge = 'source_bridge'
    src_bond = 'source_bond'
    src_module = 'source_module'
    src_type = 'source_type'

# Generated at 2022-06-13 01:52:09.692288
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.network.common.utils import load_platform_subclass

    def get_module_mock(params):
        module = AnsibleModule(argument_spec=params, supports_check_mode=False)
        module.run_command = lambda *args, **kwargs: (
            0,
            '',
            ''
        )
        return module

    params = {
        'provider': {},
    }
    module = get_module_mock(params)
    net_os = load_platform_subclass(NetworkLinux, 'linux', module)
    net = net_os()
    # make available

# Generated at 2022-06-13 01:52:19.304663
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    # create mock object
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
        ),
        supports_check_mode=True
    )

    # Mock ethtool_path
    #
    # Wrapping the AnsibleModule object's get_bin_path method
    # to return a known path.
    real_get_bin_path = module.get_bin_path
    module.get_bin_path = MagicMock(return_value="./ethtool_path")
    n = LinuxNetwork(module)

    # Mock ethtool's stdout
    #
    # Wrapping the AnsibleModule object's run_command method
    # to return a known stdout.

# Generated at 2022-06-13 01:52:28.670594
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    module = AnsibleModule(argument_spec=dict(), supports_check_mode=True)
    try:
        mock_get_file_content = Mock(return_value='')
        mock_get_bin_path = Mock(return_value=None)
        mock_run_command = Mock(return_value=(0, None, None))
        with patch('ansible.modules.network.linux._ansible_utils.get_file_content', mock_get_file_content), \
             patch('ansible.modules.network.linux.get_bin_path', mock_get_bin_path), \
             patch('ansible.modules.network.linux.run_command', mock_run_command):
            o = LinuxNetwork(module)
    except Exception as e:
        assert False, str(e)
    f = o.get_

# Generated at 2022-06-13 01:53:17.952926
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    module = AnsibleModule(argument_spec={})
    module.params['gather_subset'] = None
    module.params['gather_network_resources'] = ['all']
    ln = LinuxNetwork(module)
    default_ipv4 = {'address': '192.0.2.1'}
    default_ipv6 = {'address': '2001:0db8::0'}
    data, ips = ln.get_interfaces_info(None, default_ipv4, default_ipv6)
    assert 'lo' in data
    assert data['lo']['active'] is True
    assert data['lo']['mtu'] == 65536
    assert data['lo']['type'] == 'loopback'

# Generated at 2022-06-13 01:53:19.714208
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    test_obj = LinuxNetwork()

    # TODO: fix this test
    # test_obj.populate()

# Generated at 2022-06-13 01:53:25.922407
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    """Test the populate method of class LinuxNetwork"""

    # FIXME: This should probably be split into multiple tests,
    # and moved into test/sanity/common/utils.py

    # GIVEN: an initialized module
    module = AnsibleModule(argument_spec={}, supports_check_mode=False)

    # GIVEN: an initialized linux_system class
    linux_network = LinuxNetwork(module)

    # GIVEN: a mock run_command
    original_run_command = linux_network.module.run_command

    def mock_run_command(cmd, check_rc=False, close_fds=True, data=None, binary_data=False, environ_update=None, umask=None, encoding=None):
        rc = 0
        out = ''
        err = ''

# Generated at 2022-06-13 01:53:26.777755
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    # No tests so far
    pass


# Generated at 2022-06-13 01:53:29.740369
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():

    unit_test_utils = UnitTestUtils()
    unit_test_utils.fail_unless_exception(Exception,
                                          LinuxNetwork,
                                          unit_test_utils.get_ansible_module(''))



# Generated at 2022-06-13 01:53:40.603289
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    import NetworkInterface

    options = {}
    module = NetworkInterface.NetworkModule(argument_spec=options, supports_check_mode=True)
    module.params = {'_ansible_check_mode': False,
                     }

    ln = LinuxNetwork(module)

    # setup mock network data
    network_data = {}
    network_data['interfaces'] = {}
    network_data['interfaces']['lo'] = {}
    network_data['interfaces']['lo']['ipv4'] = {
        'address': '127.0.0.1',
        'broadcast': 'N/A',
        'netmask': '255.0.0.0',
        'network': '127.0.0.1',
    }

# Generated at 2022-06-13 01:53:45.929922
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    module = AnsibleModule(
        argument_spec=dict(
            gather_subset=dict(default=['!all'], type='list'),
            filter=dict(default=None),
        ),

        supports_check_mode=True,
    )
    ln = LinuxNetwork(module)

    module.exit_json(**ln.populate())

if __name__ == "__main__":
    test_LinuxNetwork_populate()

# Generated at 2022-06-13 01:53:52.143737
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    i = LinuxNetwork(dict(module=DummyModule()))
    i.populate()
    assert i.default_ipv4_interfaces == dict(
        address='10.1.1.153',
        broadcast='10.1.1.255',
        netmask='255.255.255.0',
        network='10.1.1.0',
        macaddress='00:11:22:33:44:55',
        mtu=1500,
        type='unknown',
        alias='eth0',
    )



# Generated at 2022-06-13 01:53:57.376458
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    net = LinuxNetwork()

    # Mock args and options
    net.module = MagicMock(name="module")
    net.module.get_bin_path = MagicMock(name="get_bin_path")
    net.get_bin_path = MagicMock()

    # Mock the LinuxNetwork.run_command method
    # The only input it takes is the run_command method.
    def mock_run_command(*args):
        """Mock run_command function"""
        # The first argument passed to run command is a string
        cmd = args[0]

        # Only the command matters for this test.
        # We should not have any other arguments.
        if len(args) > 1:
            return None, None, None

        # ip -4 route show to <default_ipv4['address']>

# Generated at 2022-06-13 01:54:03.601083
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    module = AnsibleModule({})
    l = LinuxNetwork(module=module)

    assert l.get_ethtool_data("eth0") == {}
    assert l.get_ethtool_data("eth0:0") == {}
    assert l.get_ethtool_data("eth0:1") == {}
    assert l.get_ethtool_data("eth0:2") == {}
    assert l.get_ethtool_data("eth0:3") == {}
    assert l.get_ethtool_data("eth0:4") == {}
    assert l.get_ethtool_data("eth0:5") == {}
    assert l.get_ethtool_data("eth0:6") == {}
    assert l.get_ethtool_data("eth0:7") == {}
    assert l.get_ethtool_data

# Generated at 2022-06-13 01:54:51.778435
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    default_ipv4 = {'address': '172.17.0.1'}
    default_ipv6 = {'address': '::1'}
    module = AnsibleModule(argument_spec={}, supports_check_mode=True)
    network = LinuxNetwork(module)
    try:
        from io import StringIO
    except ImportError:
        from StringIO import StringIO

# Generated at 2022-06-13 01:55:03.313382
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    # NOTE: this will not test `get_interfaces_info` that returns
    # default_ipv4 and default_ipv6 as those are closely tied to the
    # `get_default_route()` method

    # TODO: test when interfaces is empty
    # TODO: test when interfaces is None
    # TODO: test when interfaces is [
    # TODO: test when interfaces is 0
    # TODO: test when interfaces is [""]
    # TODO: test when interfaces is ["a"]
    # TODO: test when interfaces is { "a": "b" }

    module = AnsibleModule(argument_spec={}, supports_check_mode=True)

    linux_network = LinuxNetwork(module)

    ip_path = None
    default_ipv4 = {}
    default_ipv6 = {}


# Generated at 2022-06-13 01:55:11.393985
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    # tests touch the environment in ways that are going to make future tests have issues,
    # calling init again here resets that state to safe defaults which allows other tests to run correctly
    NetModule.init()
    for arg in sys.argv:
        if arg.startswith('-t'):
            sys.argv = []
            break
    module = AnsibleModule(
        argument_spec=dict(),
    )
    module.run_command = Mock(return_value=(0, '', ''))
    network = LinuxNetwork()
    device = 'eth0'

    module.run_command.return_value = (0, EXAMPLES['ethtool-k'], '')
    data = network.get_ethtool_data(device)
    assert data['features']['rx_all'] == 'on'

    module.run

# Generated at 2022-06-13 01:55:21.996811
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():

    # =============================================================================================
    # LinuxNetwork_get_interfaces_info(ip_path, default_ipv4, default_ipv6)
    # =============================================================================================
    class Test_LinuxNetwork_get_interfaces_info:
        class Test_LinuxNetwork_get_interfaces_info_MockModule:
            def __init__(self, params):
                self.params = params

            def run_command(self, args, **kwargs):
                argv = args[0]
                cmd = ' '.join(argv)

                # Assume all paths match
                # FIXME: this may need to be more exact
                if cmd.startswith(self.get_bin_path("ip")):
                    return "0", self.params['ip_output'][argv[-1]], ""

# Generated at 2022-06-13 01:55:32.060342
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():

    # FIXME: mock all the things
    # FIXME: add more test cases
    # FIXME: test the output of the method
    command = dict(
        v4=['/sbin/ip', '-4', 'route', 'list', 'default'],
        v6=['/sbin/ip', '-6', 'route', 'list', 'default']
    )
    module = dict(
        get_bin_path=lambda x: x,
    )
    module_returned = dict(
        run_command=lambda x: (0,  "8.8.8.8 via 10.0.0.1 dev eth0\n", None)
    )
    module.update(module_returned)
    module = namedtuple('AnsibleModule', module.keys())(**module)

# Generated at 2022-06-13 01:55:43.932233
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    # the 'path' is necessary when instantiating the module
    # NOTE: we are not running any actual commands here, so 'path' may not matter
    m = LinuxNetwork(module=None, path='/usr/bin')

    # TODO: we should have a better way to test things
    #       for now, we check that the command is what we expect (hopefully)
    #       we should either test that the actual command is called
    #       or that the results of these commands are used correctly
    #       or both

# Generated at 2022-06-13 01:55:49.921976
# Unit test for method get_interfaces_info of class LinuxNetwork

# Generated at 2022-06-13 01:55:59.108850
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    module = AnsibleModule({})
    linux_network = LinuxNetwork(module)

# Generated at 2022-06-13 01:56:06.369736
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    '''
    Unit test for get_ethtool_data method of class LinuxNetwork
    '''
    module = AnsibleModule(argument_spec={}, supports_check_mode=False)
    module.get_bin_path = MagicMock(return_value='/usr/sbin/ethtool')

# Generated at 2022-06-13 01:56:18.060762
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    p = dict(
        ip_path="/sbin/ip",
        bridge_path="/usr/sbin/brctl",
        module=dict(
            get_bin_path=Mock(return_value="/sbin/ip")
        ),
        run_command=Mock(return_value=(0, "", ""))
    )

    n = LinuxNetwork(**p)
    n.interfaces = {"eth0": {"ipv4": {"address": "192.168.0.2"}}}
    assert n.populate() == n.network_info

    # TODO: add some extra asserts here (https://github.com/ansible/ansible/pull/37038#issuecomment-283581452)

# Testing LinuxNetwork()

# Generated at 2022-06-13 01:57:01.245060
# Unit test for method get_default_interfaces of class LinuxNetwork

# Generated at 2022-06-13 01:57:09.242819
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    from ansible.module_utils._text import to_bytes as to_native
    from ansible.module_utils.six import StringIO

    def _get_io(**kwargs):
        for k, v in kwargs.items():
            if k == 'stdout':
                kwargs[k] = to_native(v, encoding=None, errors='surrogate_then_replace')
        return StringIO(**kwargs)

    # IP v4
    ipv4_addr = _get_io(stdout='1.2.3.4')
    ipv4_dev = _get_io(stdout='eth0')
    ipv4_route = _get_io(stdout='default via 1.2.3.5 dev eth0 onlink')

# Generated at 2022-06-13 01:57:12.201051
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    m = LinuxNetwork()
    assert m.get_ethtool_data("eth0")['features']['rx_checksumming'] == 'off'

# Unit test data for method get_ip_details of class LinuxNetwork

# Generated at 2022-06-13 01:57:22.975002
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import get_interface_dict
    from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import sort_list_of_dicts
    from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import sort_dict
    from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import dict_diff
    from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.ip import IPNetwork

    # Initialize test variables
    net = LinuxNetwork()

# Generated at 2022-06-13 01:57:29.617768
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    import tempfile

    # Example file content
    # Output of the command:
    #    ip route | grep ^default | cut -d' ' -f3-
    routes = '''
default via 10.0.2.2 dev eth0  proto static
default dev virbr0  scope link
'''
    # Example file content
    # Output of the command:
    #   ip -6 route | grep ^default | cut -d' ' -f6-
    routes6 = '''
default via fe80::5054:ff:fe12:3456 dev eth0  proto static metric 1024 pref medium
default via fe80::5054:ff:fe12:3456 dev eth0  metric 1024
'''
    # Create a temp file and write the file content

# Generated at 2022-06-13 01:57:37.780947
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    module = AnsibleModule(argument_spec={}, supports_check_mode=True)
    ln = LinuxNetwork(module)  # noqa

# Generated at 2022-06-13 01:57:47.987923
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    module = MagicMock()
    default_ipv4 = {
        'address': '192.168.33.10',
        'broadcast': '',
        'netmask': '',
        'network': '',
        'macaddress': '',
        'mtu': '',
        'type': '',
        'alias': '',
    }
    default_ipv6 = {
        'address': 'fe80::5054:ff:fe12:3456',
        'prefix': '',
        'scope': '',
        'macaddress': '',
        'mtu': '',
        'type': '',
    }
    module.get_bin_path.return_value = '/sbin/ip'
    module.run_command.return_value = (0, '', '')

    l = Linux

# Generated at 2022-06-13 01:57:59.302911
# Unit test for method get_ethtool_data of class LinuxNetwork

# Generated at 2022-06-13 01:58:08.085512
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():

    # This is a stub to allow a unit test to be written
    # such that it can be used as a reference when developing on a host
    # system where get_interfaces_info would otherwise be difficult
    # to test due to the path to ip being un-testable
    #
    # To run this test:
    #
    #   # Install testing dependencies:
    #   pip install pytest
    #
    #   # Run the test
    #   pytest test_LinuxNetwork_get_interfaces_info.py
    #

    from ansible.module_utils.basic import AnsibleModule

    from ansible.module_utils.network.common.network import NetworkModule, NetworkError, NetworkError, to_list, ComplexList


# Generated at 2022-06-13 01:58:18.507725
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    module = AnsibleModule({})