

# Generated at 2022-06-13 01:48:45.515845
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    m_mod = AnsibleModule(argument_spec=dict())
    inst = LinuxNetwork(m_mod)

    # NOTE: ioctl is ref to a method not other instance
    ioctl = m_mod.ioctl

    # NOTE: _, exit_json are ref to methods not other instances
    def exit_json(a, b):
        return a, b
    m_mod.exit_json = exit_json

    # NOTE: ip_path is ref to a class variable not instance
    m_mod.ip_path = 'ip'

    # FIXME: do we need to mock the methods that these call?

    # NOTE: get_interfaces_info is ref to a method not other instance

# Generated at 2022-06-13 01:48:51.922050
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    _ln = LinuxNetwork()
    _ln.module.get_bin_path = Mock(return_value='/usr/bin/ethtool')
    _ln.module.run_command = Mock(return_value=(0, 'key1: value1\nkey2: value2\n', ''))
    assert _ln.get_ethtool_data('eth0') == {'features': {'key1': 'value1', 'key2': 'value2'}}



# Generated at 2022-06-13 01:49:00.321503
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    class FakeModule(object):
        def __init__(self):
            pass
        def run_command(self, cmd, errors='surrogate_then_replace'):
            import json

# Generated at 2022-06-13 01:49:02.702550
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    # TODO: implement test here
    ansible_module = AnsibleModule(
        argument_spec=dict()
    )
    linux_network = LinuxNetwork(ansible_module)
    linux_network.get_interfaces_info(None, None, None)


# Generated at 2022-06-13 01:49:07.643345
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    with patch('os.readlink'):
        with patch('os.path.exists'):
            with patch('ansible_collections.ansible.community.plugins.module_utils.network.common.network.Linux.get_default_interfaces'):
                # NOTE: we are testing the method, not the *class*
                o = LinuxNetwork()
                o.get_default_interfaces()
                pass


# Generated at 2022-06-13 01:49:18.156142
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    # Change module name to LinuxNetwork, ensure that it gets changed back
    m = module_class.module
    module_class.module = 'LinuxNetwork'
    module_class.__module__ = 'ansible.module_utils.network.common.network.LinuxNetwork'

    # Get a working instance of LinuxNetwork
    ln = LinuxNetwork()

    # Sanity check: ensure that the LinuxNetwork class is as we expect
    assert hasattr(ln, 'get_default_interfaces')
    assert hasattr(ln, 'get_interfaces_info')
    assert hasattr(ln, 'populate')

    # Sanity check: ensure that the module class is as we expect
    assert hasattr(module_class, 'module')
    assert hasattr(module_class, 'params')

    # Manage module name
    assert module_class.module

# Generated at 2022-06-13 01:49:21.919548
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    module = AnsibleModule(
        argument_spec = dict(),
        supports_check_mode = True
    )

    # FIXME: use fake data instead of real data, need to depend on ddt
    test = LinuxNetwork(module)
    test.populate()
    module.exit_json(changed=False)


# Generated at 2022-06-13 01:49:33.105995
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    import json
    class TestModule(object):
        def run_command(self, command, check_rc=True, errors=None, data=''):
            if 'ethtool' not in command[0]:
                return 1, '', 'command not found'
            if '-k' in command[0]:
                output = 'some-key: on\n'
                output += 'some-other-key: off\n'
                output += 'some-key-with-no-value\n'
                return 0, output, ''
            elif '-T' in command[0]:
                output = 'SOF_TIMESTAMPING_SOFTWARE (hardware acceleration off)\n'
                output += 'SOF_TIMESTAMPING_TX_SOFTWARE (hardware acceleration off)\n'

# Generated at 2022-06-13 01:49:45.414721
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():

    from ansible_collections.notstdlib.moveitallout.plugins.module_utils.network.common.utils import transform_commands


# Generated at 2022-06-13 01:49:56.297776
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    try:
        from unittest.mock import Mock, patch
    except ImportError:
        from mock import Mock, patch

    test_device = 'test0'
    test_data = {
        'timestamping': ['hardware', 'software', 'legacy_hardware'],
        'hw_timestamp_filters': ['all', 'none'],
        'phc_index': 0
    }
    mock_run_command = Mock(return_value=(0, '', ''))
    with patch.dict(LinuxNetwork.__dict__, {'run_command': mock_run_command}):
        property_name = 'features'
        expected_output = {}
        actual_output = LinuxNetwork().get_ethtool_data(test_device).get(property_name, None)
        assert actual_output == expected_

# Generated at 2022-06-13 01:50:41.280709
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    class ModuleStub():
        def get_bin_path(self, path):
            return '/usr/bin/ethtool'
        def run_command(self, path):
            if '/usr/bin/ethtool -k' in path:
                return (0, 'Offload parameters for enp0s6\n\tgso-offload: on\n\tgro-offload: on\n\tnapi-offload: off\n\tchecksum-offload: on\n', '')

# Generated at 2022-06-13 01:50:52.964990
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    """
    Method: get_interfaces_info
    """

    def mock_get_file_content(path, default=None):
        if path == '/sys/class/net/lo/address':
            return '00:00:00:00:00:00'
        elif path == '/sys/class/net/lo/mtu':
            return '65536'
        elif path == '/sys/class/net/lo/operstate':
            return 'unknown'
        elif path == '/sys/class/net/lo/type':
            return '1'
        elif path == '/sys/class/net/lo/bridge':
            return ''
        elif path == '/sys/class/net/lo/bonding':
            return ''

# Generated at 2022-06-13 01:50:55.456491
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    # There is no easy way to test this - just return something
    # so that the test of the module itself won't complain.
    return True

# Generated at 2022-06-13 01:51:07.372789
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():

    class MockModule(object):
        def __init__(self):
            self.params = {}
            self.run_command = Mock(return_value=(0, "stdout", ""))
        def get_bin_path(self, name, opt_dirs=None):
            if name == "ip":
                return "ip"
            return
    class MockLinuxNetwork(LinuxNetwork):
        def __init__(self):
            self.module = MockModule()
            self.ip_path = "ip"
            self.default_ipv4 = { 'address':'10.0.0.1' }
            self.default_ipv6 = { 'address':'2001:0db8:85a3:0000:0000:8a2e:0370:7334' }


# Generated at 2022-06-13 01:51:10.585134
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    func = LinuxNetwork.get_ethtool_data
    class_obj = LinuxNetwork(None)
    assert func(class_obj, 'eth0')


# Generated at 2022-06-13 01:51:23.054747
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    """
    Test method `get_default_interfaces` of class `LinuxNetwork`
    """
    import platform
    # store `platform.*` in local variables to avoid Python 2 scoping issues
    p_distro = platform.linux_distribution
    p_release = platform.dist
    p_system = platform.system
    p_machine = platform.machine
    p_libc_ver = platform.libc_ver

    ln = LinuxNetwork()
    ln.module.get_bin_path = lambda *args: '/bin/ip'
    # FIXME: move these to constants
    ln.module.run_command = lambda *args: (
        0, '1.2.3.4 dev eth0', None)
    assert ln.get_default_interfaces() == ('1.2.3.4', {})

# Generated at 2022-06-13 01:51:23.821388
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    pass

# Generated at 2022-06-13 01:51:30.971766
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():

    import unittest
    from ansible_collections.notstdlib.moveitallout.tests.unit.compat.mock import patch
    from ansible_collections.notstdlib.moveitallout.tests.unit.compat.mock import MagicMock

    class TestNetwork(unittest.TestCase):
        def setUp(self):
            self.module = MagicMock()


# Generated at 2022-06-13 01:51:39.829393
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    # Create  instance of class LinuxNetwork
    interface = LinuxNetwork()
    # call method get_default_interfaces of class LinuxNetwork
    interface_r, interface_r1 = interface.get_default_interfaces()
    # Check if returned values are not empty
    if interface_r != {} and interface_r1 != {}:
        print("Success: method get_default_interfaces returns the value.")
        return True
    else:
        print("Error: method get_default_interfaces does not return the value.")
        return False



# Generated at 2022-06-13 01:51:49.005474
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    module = AnsibleModule(
        argument_spec = dict(),
        supports_check_mode = True
    )

    ln = LinuxNetwork(module)
    ln.populate()


# Generated at 2022-06-13 01:52:32.699049
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    module = AnsibleModule(argument_spec=dict())
    def get_bin_path(x):
        return True
    module.get_bin_path = get_bin_path
    network = LinuxNetwork(module)
    ip_path = None
    default_ipv4 = dict(address='172.17.1.1')
    default_ipv6 = dict(address='::1')
    interfaces, ips = network.get_interfaces_info(ip_path, default_ipv4, default_ipv6)
    assert isinstance(interfaces, dict)
    assert isinstance(ips, dict)

# Generated at 2022-06-13 01:52:40.922936
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    module = AnsibleModule(argument_spec=dict())
    linux_network = LinuxNetwork(module)

    # Test 1
    stdout = '''
    Pre-set maximums:
    RX:			15000
    TX:			15000
    Other:			1000000
    Combined:			15000
    RQ:			512
    TQ:			512
    '''.strip()

    assert linux_network.get_ethtool_data('testdevice') == {
        'features': {
            'rx': '15000',
            'tx': '15000',
            'other': '1000000',
            'combined': '15000',
            'rq': '512',
            'tq': '512',
        }
    }

    # Test 2
    # Test

# Generated at 2022-06-13 01:52:45.754606
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    """LinuxNetwork - get_interfaces_info unit test stubs"""

    # FIXME: construct object with mandatory attributes with examples
    # FIXME: execute the code block
    # FIXME: manipulate the data and assert an expected result
    raise Exception("Coding error detected in Ansible code. "
                    "get_interfaces_info() method must be implemented.")



# Generated at 2022-06-13 01:52:54.362769
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():

    # TODO: create a fake module for us to use
    module = 0
    # TODO: create a fake module for us to use
    if True:
        ln = LinuxNetwork(module)
        ln.module = module
        ln.module.exit_json = exit_json
        ln.module.fail_json = fail_json
        ln.module.run_command = run_command

        # Test 1:
        ln.populate()
        ln.module.exit_json.assert_called_once_with(
            ansible_facts={'ansible_network_resources': {}},
            changed=True
        )


# Generated at 2022-06-13 01:53:01.276249
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    module = AnsibleModule(argument_spec={})
    ip = '/sbin/ip'
    default_ipv4 = {'address': None}
    default_ipv6 = {'address': None}
    interfaces = LinuxNetwork(module).get_interfaces_info(ip, default_ipv4, default_ipv6)
    assert interfaces is None
    assert default_ipv4 == {'address': None}
    assert default_ipv6 == {'address': None}



# Generated at 2022-06-13 01:53:14.578130
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    module = AnsibleModule(argument_spec={
        "device": dict(type="str", default="eth0")
    }, supports_check_mode=True)
    linux_network = LinuxNetwork(module)
    result = linux_network.get_ethtool_data("eth0")
    assert(result['features']['tx_checksumming'] is not None)
    assert(result['features']['vlan_tagging'] == 'on')
    assert(result['features']['rx'] == 'on')
    assert(result['features']['tx'] == 'on')
    assert(result['features']['ufo'] == 'on')
    assert(result['features']['rx_hashing'] == 'on')
    assert(result['features']['ntuple_filters'] == 'off')

# Generated at 2022-06-13 01:53:15.700330
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    assert not LinuxNetwork().get_interfaces_info()


# Generated at 2022-06-13 01:53:22.913017
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():

    from ansible_collections.misc.not_a_real_collection.plugins.module_utils.basic import AnsibleModule
    module = AnsibleModule()

    path_values = {
        'bin/ethtool': '/usr/sbin/ethtool',
    }
    mock_path_exists = Mock(return_value=True)
    mock_get_bin_path = Mock(side_effect=lambda x, paths=path_values: paths[x])

    test_subject = LinuxNetwork(module)
    test_subject.get_bin_path = mock_get_bin_path
    test_subject.path_exists = mock_path_exists

    # Test
    rc, stdout, stderr = Mock(return_value=0), """\
""", ''

    # the "ethtool -T" call
   

# Generated at 2022-06-13 01:53:30.122793
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    # FIXME: add tests
    module = AnsibleModule(
        argument_spec=dict(),
    )
    n = LinuxNetwork(module)
    n.ALL_IPV4_ADDRS = 'all_ipv4_addresses'
    n.ALL_IPV6_ADDRS = 'all_ipv6_addresses'
    data = dict()

    # 0: no input and output
    n.populate(data)
    assert data == dict()

    # 1: ipv4 and ipv6 interfaces in data
    data = dict(
        ipv4=dict(address='1.2.3.4'),
        ipv6=dict(address='1::2'),
    )
    n.populate(data)

# Generated at 2022-06-13 01:53:41.194803
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    '''
    Unit test for method get_interfaces_info of class LinuxNetwork
    '''

    # NOTE: Assumes that the test environment contains
    # eth0, eth1, eth2 and lo interfaces.

    class LinuxNetworkTester(LinuxNetwork):
        '''
        Derived class for testing LinuxNetwork.get_interfaces_info() method.
        '''
        def __init__(self):
            '''
            Constructor.
            '''
            super(LinuxNetworkTester, self).__init__(module=None)

    ln = LinuxNetworkTester()

    default_ipv4 = dict(address='127.0.0.1')
    default_ipv6 = dict(address='::1')


# Generated at 2022-06-13 01:54:28.831682
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():

    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes

    interface = 'eth0'
    module = basic.AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True,
        add_file_common_args=True,
    )
    module.params['gather_subset'] = 'all'
    # We need to write a file to disk to test get_file_content()
    path = os.path.join(module.tmpdir, 'test_ansible_network_file')
    with open(path, 'w') as f:
        f.write('test_ansible_network_file')
    # We need to create a fake interface directory in sysfs

# Generated at 2022-06-13 01:54:31.181436
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    assert(LinuxNetwork.get_default_interfaces() == ("eth0", "eth0"))


# Generated at 2022-06-13 01:54:42.506913
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    with ExitStack() as stack:
        module = AnsibleModule(argument_spec={})
        stack.enter_context(modules.load_module_spec('ANSIBLE_MODULE_ARGS', module._load_params(module.params)))
        LinuxNetwork.populate(module)
        assert module.params['network'] == {}
        assert module.params['default_ipv4'] == {}
        assert module.params['default_ipv6'] == {}
        assert module.params['ansible_facts']['network'] == {}
        assert module.params['ansible_facts']['all_ipv4_addresses'] == []
        assert module.params['ansible_facts']['all_ipv6_addresses'] == []
        assert module.exit_json.call_count == 1
        assert module.warn.call_count

# Generated at 2022-06-13 01:54:51.487853
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    from io import StringIO
    from ansible.module_utils.basic import AnsibleModule

    # set up our test double
    module = AnsibleModule(argument_spec={})

    # test double

# Generated at 2022-06-13 01:55:03.077383
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    """This method is automatically called by test.module_utils.linux.py"""
    module = AnsibleModule({"path": "test"})
    ln = LinuxNetwork(module)
    # FIXME: there's no test file here, is this testable?
    with patch("ansible.module_utils.network.common.interfaces.get_file_content", return_value=False):
        # FIXME: this should be a list, not a tuple, to be consistent
        ifupdown = ("lo", "eth0")
        # FIXME: the mocking is not like this
        # with patch("ansible.module_utils.network.common.interfaces.get_file_content", return_value=ifupdown):
        assert ("lo", "eth0") == ln.get_default_interfaces(module)



# Generated at 2022-06-13 01:55:11.245174
# Unit test for method get_interfaces_info of class LinuxNetwork

# Generated at 2022-06-13 01:55:21.879808
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    import textwrap

    class FakeModule(object):
        def __init__(self, ip_path, default_ipv4, default_ipv6, rc, stdout):
            self.ip_path = ip_path
            self.default_ipv4 = default_ipv4
            self.default_ipv6 = default_ipv6
            self.rc = rc
            self.stdout = textwrap.dedent(stdout).strip()

        def run_command(self, args, errors='surrogate_then_replace'):
            assert args[0] == self.ip_path
            assert args[1:] == ['addr', 'show', 'primary', 'lo']
            return self.rc, self.stdout, ''

    # FIXME: add tests for ethtool support
    #        add tests for bonding


# Generated at 2022-06-13 01:55:28.088391
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    # This test creates a fake AnsibleModule object. The result of calling
    # the module's run_command method is recorded and can be asserted on.
    module_args = dict(
        gather_subset=['all'],
        gather_network_resources=['all']
    )
    module = AnsibleModule(argument_spec=module_args, supports_check_mode=False)
    if not HAS_IFADDR:
        module.fail_json(msg="Missing required ifaddr module", exception=IFADDR_IMP_ERR)

    # Constructor
    network = LinuxNetwork(module)
    network.on_open_shell()

    # Populate
    network.populate(module.params, module.params['gather_subset'])

# Generated at 2022-06-13 01:55:31.940623
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    """LinuxNetwork.get_default_interfaces"""
    ## TODO: tests
    # FIXME: add a test with a blank ip route
    # FIXME: add a test with a blank ip -6 route
    # FIXME: add a test with a blank ip route
    pass


# Generated at 2022-06-13 01:55:37.569753
# Unit test for constructor of class LinuxNetworkCollector
def test_LinuxNetworkCollector():
    # Failed if distro facts
    module = AnsibleModule(
        argument_spec={
            'gather_subset': dict(default=['all'], type='list'),
            'filter': dict(),
        },
        supports_check_mode=True
    )
    # Hardcode for retrieving facts for testing
    module.params['filter'] = ["(?i)^((?!(lo|cali)).)*$"]
    module.params['gather_subset'] = ['all']
    # Mock facts
    set_module_args({})
    from ansible.modules.system.setup import Setup
    setup = Setup(module)
    facts = setup.get_facts()
    facts['distribution_version'] = "18.04"
    facts['kernel'] = "4.15.0-20-generic"

# Generated at 2022-06-13 01:56:25.628549
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    module = MockANSModule()
    network = LinuxNetwork(module)
    ip_path = '/bin/ip'
    default_ipv4 = {}
    default_ipv6 = {}

    interfaces, ips = network.get_interfaces_info(ip_path, default_ipv4, default_ipv6)

    assert(interfaces['lo']['pciid'] == '0000:00:00.0')
    assert(interfaces['enp0s25']['pciid'] == '0000:00:19.0')
    assert(interfaces['lo']['speed'] == 1000)
    assert(interfaces['enp0s25']['speed'] == 1000)
    assert(interfaces['vnet0']['speed'] == 1000)

# Generated at 2022-06-13 01:56:33.871025
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    module = AnsibleModule(argument_spec={})
    net = LinuxNetwork(module)


# Generated at 2022-06-13 01:56:39.260434
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    import shutil
    import tempfile
    # NOTE: this is not a real test
    from ansible.module_utils.basic import AnsibleModule
    # make sure we can find 'ethtool' so we can test the error handling
    module = AnsibleModule(
        {'ethtool_path': shutil.which('ethtool')},
        supports_check_mode=False,
    )
    net = LinuxNetwork(module)
    print(net.get_ethtool_data('lo'))



# Generated at 2022-06-13 01:56:51.181912
# Unit test for method populate of class LinuxNetwork

# Generated at 2022-06-13 01:57:01.191690
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():

    # init a class
    sut = LinuxNetwork()

    # set some inputs
    sut.path = '/sbin:/usr/sbin:/bin:/usr/bin'
    sut._ips_path = ''
    sut._ethtool_path = 'echo'
    sut._default_ipv4 = {'address': '127.0.0.1'}
    sut._default_ipv6 = {'address': '::1'}

    # call method under test
    answer = sut.get_interfaces_info('/sbin:/usr/sbin:/bin:/usr/bin',
                                     {'address': '0.0.0.0'},
                                     {'address': '::'})
    # check results

# Generated at 2022-06-13 01:57:06.048684
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    m = LinuxNetwork()
    d = m.get_ethtool_data(device='e1000e')
    assert d.get('features')
    assert d.get('timestamping')
    assert d.get('hw_timestamp_filters')
    assert d.get('phc_index') is None
    d = m.get_ethtool_data(device='bogus')
    assert d == {}



# Generated at 2022-06-13 01:57:09.484268
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    module = AnsibleModule(supports_check_mode=True)
    ln = LinuxNetwork(module)
    assert ln.get_ethtool_data("eth0") == ln.get_ethtool_data("fakeethdevice")



# Generated at 2022-06-13 01:57:17.178250
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():

    IO_LOG_LEN = 100

    class ModuleMock(object):
        """Mock for class AnsibleModule"""

        def __init__(self):
            self.fail_json = lambda *_, **__: None
            self.log = []
            self.debug = lambda s: self.log.append(s)
            self.params = {}
            self.ip_path = 'PATH_TO_IP'


# Generated at 2022-06-13 01:57:26.210442
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    import pytest
    import tempfile
    import sys
    import os

    @pytest.fixture
    def AutoAnsibleModule():
        # FIXME: add this to test/lib instead.
        import re
        import ansible.module_utils.basic
        import ansible.module_utils.ansible_release
        import ansible.module_utils.network.common.utils
        import ansible.module_utils.network.common.config
        import ansible.module_utils.network.common.network
        import ansible.module_utils.six
        import ansible.module_utils.six.moves.builtins

        class ModuleBuilder(object):
            def __init__(self, module_name):
                self.module_name = module_name
                self.params = {}


# Generated at 2022-06-13 01:57:33.484561
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    linux_network = LinuxNetwork()
    device = 'eth0'

    class MockModule(object):
        def get_bin_path(self, arg):
            return 'ethtool'
