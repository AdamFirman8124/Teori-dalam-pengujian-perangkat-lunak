

# Generated at 2022-06-13 01:48:48.153941
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    import unittest
    self = unittest
    class TestModule(object):
        def get_bin_path(self, path, opt_dirs=[]):
            return "/bin/%s" % path


# Generated at 2022-06-13 01:48:54.894152
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    network = LinuxNetwork()
    ethtool_path = network.module.get_bin_path("ethtool")

    # no ethtool
    if not ethtool_path:
        # FIXME: what constitutes a good test?
        # FIXME: assertRaises doesn't seem to take msg param
        with pytest.raises(AssertionError) as expected:
            network.get_ethtool_data("")
        assert "No ethtool available" in str(expected.value)

    # FIXME: how to test feature data?



# Generated at 2022-06-13 01:49:02.180362
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    module = AnsibleModule(argument_spec={})
    network = LinuxNetwork(module)
    device = 'lo'
    result = network.get_ethtool_data(device)
    assert result['features']['tx_checksumming'] == 'on', 'tx_checksumming'
    assert result['features']['rx_checksumming'] == 'on', 'rx_checksumming'
    assert result['features']['scatter_gather'] == 'on', 'scatter_gather'
    assert result['features']['tcp_segmentation_offload'] == 'on', 'tcp_segmentation_offload'
    assert result['features']['udp_fragmentation_offload'] == 'off', 'udp_fragmentation_offload'


    device = 'eth0'


# Generated at 2022-06-13 01:49:06.808031
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    from ansible.module_utils.six.moves import StringIO

    _stdout = StringIO()
    _stderr = StringIO()
    _module = LinuxNetwork()
    _module.run_command = lambda args, errors: (0, _stdout.read(), _stderr.read())
    _device = "test"

    _stdout.write("")
    assert _module.get_ethtool_data(_device) == {'features': {}}

    _stdout.write("""
Offload parameters for dummy0:
Cannot get device offload settings: Operation not supported
    """)
    assert _module.get_ethtool_data(_device) == {'features': {}}


# Generated at 2022-06-13 01:49:17.376231
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    module = AnsibleModule({'params': {}})
    l = LinuxNetwork(module)


# Generated at 2022-06-13 01:49:20.616574
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    module = AnsibleModule(
        argument_spec={},
        supports_check_mode=False
    )

    linux_network_instance = LinuxNetwork(module)
    # TODO: mock the linux_network_instance
    # TODO: assert correct results

# Generated at 2022-06-13 01:49:22.433884
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    # FIXME: add tests for this method of this class
    module = AnsibleModule({})
    linux_network = LinuxNetwork(module)
    device = 'eth0'
    result = linux_network.get_ethtool_data(device)
    assert result


# Generated at 2022-06-13 01:49:33.154458
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    ln = LinuxNetwork()
    default_ipv4 = {'address': u'10.1.2.2'}
    default_ipv6 = {'address': u'10.1.2.2'}

# Generated at 2022-06-13 01:49:45.414928
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    linux_network = LinuxNetwork()

# Generated at 2022-06-13 01:49:56.296514
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    network_linux = LinuxNetwork(None)

    ethtool_data = network_linux.get_ethtool_data("eth0")

# Generated at 2022-06-13 01:50:32.315331
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():

    os.environ['PATH'] = '/sbin:/usr/sbin:/bin:/usr/bin'

    n = LinuxNetwork()
    # Get interfaces dictionary without cache
    interfaces, ips = n.get_interfaces_info(ip_path='ip', default_ipv4={}, default_ipv6={})

    if not interfaces:
        print("No interfaces found")

    for interface in interfaces:
        print("{} - {}".format(interface, interfaces[interface]))

    for ip in ips:
        print("{} - {}".format(ip, ips[ip]))


# Generated at 2022-06-13 01:50:43.785047
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    klass, m_run_command, m_get_bin_path = get_mock_LinuxNetwork()
    m_get_bin_path.return_value = "/usr/sbin/ethtool"

# Generated at 2022-06-13 01:50:55.585655
# Unit test for method get_default_interfaces of class LinuxNetwork

# Generated at 2022-06-13 01:50:57.749935
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    device = "lo"
    ln = LinuxNetwork()
    print(ln.get_ethtool_data(device))


# Generated at 2022-06-13 01:51:10.229936
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    """the get_default_interfaces method of class LinuxNetwork returns a tuple of the default gateway interface for v4 and v6 traffic"""
    class MockModule(object):
        def get_bin_path(self, *args, **kwargs):
            return "/bin/ip"
        def run_command(self, *args, **kwargs):
            """mock the execution of an ip command
            get_default_interfaces should call the command
              ip -4 -o route get 8.8.8.8
              ip -6 -o route get 2001:4860:4860::8888
            it should consume the output from the command and return the interface names on which packets destined for those addresses are routed
            """

# Generated at 2022-06-13 01:51:22.684280
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    import platform
    import json
    import socket
    import struct
    import subprocess

    # Use platform module to detect system bits so we may get the right /proc content
    test_platform = platform.system().lower()
    bits = platform.architecture()[0]
    if test_platform == 'linux':
        system_file_path = '/etc/system-release'
    elif test_platform == 'darwin':
        system_file_path = '/System/Library/CoreServices/SystemVersion.plist'
    else:
        system_file_path = None

    # Get system version and name
    system_platform = None
    system_distribution = None
    system_version = None
    system_kernel = None
    if system_file_path:
        if test_platform == 'linux':
            system_distribution,

# Generated at 2022-06-13 01:51:28.533020
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    # Test that we can populate the interface data
    ln = LinuxNetwork()
    (interfaces, ips) = ln.get_interfaces_info('/sbin/ip', {}, {})
    assert isinstance(interfaces, dict)
    assert 'lo' in interfaces
    assert 'lo' in ips
    assert 'all_ipv4_addresses' in ips
    assert 'all_ipv6_addresses' in ips
    assert 'eth0' in interfaces
    assert 'eth0' in ips

# Generated at 2022-06-13 01:51:40.791616
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    module = AnsibleModule(argument_spec={
    })
    ln = LinuxNetwork(module, '1.7.0')
    device = 'eth0'
    ethtool_data = ln.get_ethtool_data(device)
    assert 'features' in ethtool_data, 'features key is not in ethtool_data'
    assert ethtool_data['features']['txvlan_hw_insert'] == 'on', 'txvlan_hw_insert value is not "on"'
    assert 'timestamping' in ethtool_data, 'timestamping key is not in ethtool_data'
    assert 'hw_timestamp_filters' in ethtool_data, 'hw_timestamp_filters key is not in ethtool_data'

# Generated at 2022-06-13 01:51:49.679778
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    module = AnsibleModule(argument_spec={})
    network = LinuxNetwork(module)


# Generated at 2022-06-13 01:51:53.226277
# Unit test for constructor of class LinuxNetworkCollector
def test_LinuxNetworkCollector():
    obj = LinuxNetworkCollector()
    assert obj.__class__.__name__ == 'LinuxNetworkCollector'
    assert obj.__class__.__bases__[0].__name__ == 'NetworkCollector'
    assert isinstance(obj, NetworkCollector)
    assert obj.platform == 'Linux'
    assert obj.fact_class.__name__ == 'LinuxNetwork'
    assert obj.required_facts == {'distribution', 'platform'}


# Generated at 2022-06-13 01:52:30.673397
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():

    # Test module args
    module_args = dict(
        config_file="/etc/sysconfig/network",
        default_ipv4=dict(address="10.11.12.13"),
        default_ipv6=dict(address="cafe::babe")
    )

    # get the module class obj
    obj = LinuxNetwork()

    # call the populate method
    result = obj.populate(module_args)

    # Verify the result

    assert result['interfaces']['eth0']['active'] == True
    assert result['interfaces']['eth0']['ipv4']['address'] == "10.11.12.13"
    assert result['interfaces']['eth0']['ipv4']['broadcast'] == "10.11.12.255"

# Generated at 2022-06-13 01:52:38.851749
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    from ansible.module_utils import basic
    # TODO: replace with dynamic paths to these fixtures
    n = LinuxNetwork(basic.AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    ))
    assert n.get_default_interfaces() == (
        {'address': u'10.18.1.57', 'gateway': u'10.18.1.1', 'interface': u'eth0'},
        {'address': u'fe80::250:56ff:fe86:6cb9', 'gateway': u'fe80::250:56ff:fe86:6c1', 'interface': u'eth0'}
    )


# Generated at 2022-06-13 01:52:49.465962
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    # Prepare test object
    obj = LinuxNetwork()
    # Test 'features' property
    features = {'rx_checksumming': 'off', 'udp_fragmentation_offload': 'off', 'ntuple_filters': 'on', 'generic_receive_offload': 'off', 'tx_checksumming': 'off', 'large_receive_offload': 'off', 'rx_vlan_offload': 'off', 'sctp_checksumming': 'off', 'rx_stcp_segmentation_offload': 'off', 'tx_stcp_segmentation_offload': 'off', 'generic_segmentation_offload': 'off', 'udp_segmentation_offload': 'off', 'tx_vlan_offload': 'off'}
    assert obj.get_ethtool_

# Generated at 2022-06-13 01:52:53.953872
# Unit test for constructor of class LinuxNetworkCollector
def test_LinuxNetworkCollector():
    """
    This test will check whether the member variables of the class LinuxNetworkCollector are correctly assigned.
    :return:
    """
    # Create a mock instance of class AnsibleModule
    mock_module = mock.create_autospec(AnsibleModule)

    # Create a mock instance of class LinuxNetworkCollector
    mock_distribution = mock.create_autospec(LinuxNetworkCollector)

    # Set the member variable _module of class LinuxNetworkCollector with the mock_module
    mock_distribution._module = mock_module

    # Create an actual instance of class LinuxNetworkCollector and assign it to the variable network_collector
    network_collector = LinuxNetworkCollector(mock_module)

    # Assert that the values of the member variables of the two instances are the same

# Generated at 2022-06-13 01:53:04.456787
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    class LinuxNetworkMock(LinuxNetwork):
        def __init__(self):
            self.module = ModuleMock()

    linux_network = LinuxNetworkMock()
    # TODO: add some more specific tests
    device = "hfjsdfk"
    rc_ok = 0

# Generated at 2022-06-13 01:53:11.747843
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    """
    Test the method get_interfaces_info of class LinuxNetwork
    """

    _, ips = LinuxNetwork().get_interfaces_info("ip_path", {"address":""}, {"address":""})
    assert len(ips) == 2
    assert isinstance(ips['all_ipv4_addresses'], list)
    assert isinstance(ips['all_ipv6_addresses'], list)



# Generated at 2022-06-13 01:53:15.987668
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    from ansible.module_utils.facts.networking.linux import LinuxNetwork
    linux_network = LinuxNetwork({}, {})
    linux_network.module.get_bin_path = lambda _: '/bin/false'
    interfaces, default_ipv4, default_ipv6 = linux_network.populate()
    assert interfaces == {}
    assert 'address' not in default_ipv4
    assert 'address' not in default_ipv6


# Generated at 2022-06-13 01:53:23.130863
# Unit test for method get_default_interfaces of class LinuxNetwork

# Generated at 2022-06-13 01:53:26.018274
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
  ip_path = "/usr/sbin/ip"
  default_ipv4 = dict()
  default_ipv6 = dict()
  l = LinuxNetwork(dict())
  for i in l.get_interfaces_info(ip_path, default_ipv4, default_ipv6):
    print(i)


# Generated at 2022-06-13 01:53:35.022473
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    import os
    import re

    # Save current working directory
    old_cwd = os.getcwd()

    # We may as well test all supported OSes

# Generated at 2022-06-13 01:54:11.488757
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    # pylint: disable=protected-access
    test_route_instance = LinuxNetwork()
    test_route = test_route_instance._get_default_interfaces()
    assert isinstance(test_route,tuple)
    assert isinstance(test_route[0],dict)
    assert isinstance(test_route[1],dict)


# Generated at 2022-06-13 01:54:21.785097
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    module_mock = MagicMock()
    ip_path_mock = MagicMock()
    ip_path_mock.return_value = True
    module_mock.get_bin_path.side_effect = ip_path_mock
    default_ipv4_mock = {}
    default_ipv6_mock = {}
    all_ipv4_addresses_mock = []
    all_ipv6_addresses_mock = []
    interfaces_mock = {}
    lo_mock = {}
    lo_mock.update({"device": "lo", "ipv4": {}, "ipv6": []})
    interfaces_mock.update({"lo": lo_mock})
    eth0_mock = {}

# Generated at 2022-06-13 01:54:28.507803
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    module = type('AnsModule', (object,), {})
    module.run_command = MagicMock(return_value=(0, 'success', ''))
    module.get_bin_path = lambda _: '/bin/path'
    module.params = {}
    module.run_command = MagicMock(return_value=(0, 'success', ''))

    os_path = type('AnsPOSIXPath', (object,), {})
    os_path.exists = lambda _: True
    os_path.isdir = lambda _: True
    os_path.is_mount = lambda _: True
    os.path = os_path
    os.getuid = lambda: 0

# Generated at 2022-06-13 01:54:36.126588
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    '''
    Unit test for method LinuxNetwork.get_default_interfaces
    '''
    module = AnsibleModule(argument_spec={})
    # NOTE: get_default_interfaces is static
    p = dict(default_interface_ipv4=dict(), default_interface_ipv6=dict())
    L = LinuxNetwork(module, p)
    gdi = L.get_default_interfaces()
    # TODO: test return values


# Generated at 2022-06-13 01:54:45.918951
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    module = AnsibleModule(argument_spec=dict())
    nm = LinuxNetwork(module)
    interfaces = nm.populate()
    assert isinstance(interfaces, dict)
    for k in interfaces:
        assert isinstance(interfaces[k], dict)
        # assert interfaces[k]['device'] == k
        # below are optional keys
        for opt_k in ('macaddress', 'ipv4', 'ipv6', 'promisc', 'mtu', 'type', 'active', 'module', 'pciid', 'speed'):
            if opt_k in interfaces[k]:
                assert isinstance(interfaces[k][opt_k], object)



# Generated at 2022-06-13 01:54:50.501812
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    class MockModule(object):
        @staticmethod
        def run_command(args, **kwargs):
            if args[1] == '-k':
                return 0, "abcd:     Off \n", ""
            elif args[1] == '-T':
                return 0, "SOF_TIMESTAMPING_HARDWARE\nHWTSTAMP_FILTER_NONE\nPTP Hardware Clock: 0\n", ""
            else:
                return 1, "", ""
        @staticmethod
        def get_bin_path(name):
            if name == "ethtool":
                return "/usr/bin/ethtool"
            else:
                return None

    mmodule = MockModule()
    ln = LinuxNetwork(module=mmodule)

# Generated at 2022-06-13 01:55:02.219306
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    """Tests get_interfaces_info method of LinuxNetwork class
    """
    import io
    import struct
    import subprocess
    import sys
    import tempfile
    import unittest.mock as mock
    import xml.etree.ElementTree as ET

    try:
        from collections.abc import Mapping
    except ImportError:
        # Python < 3.3
        from collections import Mapping

    class MockAnsibleModule(object):
        """Pretend to be an AnsibleModule for testing LinuxNetwork class.

        We avoid mocking AnsibleModule, instead take a few of the original
        class to reproduce the behavior correctly.
        """

        # pylint: disable=too-few-public-methods,too-many-instance-attributes

        def __init__(self, module_name):
            self.module_

# Generated at 2022-06-13 01:55:10.750339
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    """
    Test of method populate of class LinuxNetwork
    """
    m = AnsibleModule({})
    ln = LinuxNetwork(m)
    result = ln.populate()
    # assert the result is what we expect
    assert result['default_ipv4']['address'] == '192.168.122.2'
    assert result['default_ipv4']['netmask'] == '255.255.255.0'
    assert result['default_ipv4']['macaddress'] == '52:54:00:8c:a2:2b'
    assert result['default_ipv4']['broadcast'] == '192.168.122.255'
    assert result['default_ipv6']['address'] == 'fe80::5054:ff:fe8c:a22b'
   

# Generated at 2022-06-13 01:55:21.441529
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    '''
    Unit test for the method `get_ethtool_data` of the class `LinuxNetwork`.
    '''
    # Create a fake module
    fake_module = AnsibleModule(argument_spec={})

    # Enable the Ethtool module
    fake_module.get_bin_path = lambda x: "/usr/bin/ethtool"

    # Create a fake AnsibleModule object
    linux_network = LinuxNetwork(fake_module)

    # Create a device
    device = "lo"

    # Create a list of features

# Generated at 2022-06-13 01:55:27.792425
# Unit test for method populate of class LinuxNetwork

# Generated at 2022-06-13 01:56:04.042677
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    import platform
    import distutils.version
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.network.common.utils import dict_diff
    from ansible.module_utils.network.common.utils import remove_default_spec
    from ansible.module_utils.network.common.utils import compare_lists_of_dicts

    def create_module(ansible_options=None):
        if not ansible_options:
            ansible_options = {}

        args = dict(
            gather_subset='!all',
            # FIXME: add '!config'
            # FIXME: add '!min'
            gather_network_resources=[
                'interfaces',
            ],
        )
        args.update(ansible_options)

# Generated at 2022-06-13 01:56:15.943744
# Unit test for method get_default_interfaces of class LinuxNetwork

# Generated at 2022-06-13 01:56:26.009562
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    # set up a faked module, and module.run_command method
    class FakeModule:
        def __init__(self):
            self.run_command_called = False
            self.run_command_return_values = []

        def get_bin_path(self, key, required=None):
            return '/usr/bin/ethtool'


# Generated at 2022-06-13 01:56:28.351843
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    ''' test get_ethtool_data method '''
    m = LinuxNetwork()
    res = m.get_ethtool_data("fake")
    assert res == {}



# Generated at 2022-06-13 01:56:37.446410
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():
    from ansible.module_utils.basic import AnsibleModule

    mock_run_command = lambda cmd : (0, 'some data', '')
    mock_get_bin_path = lambda cmd : 'some data'

    module = AnsibleModule(
        argument_spec = {},
    )

    module.run_command = mock_run_command
    module.get_bin_path = mock_get_bin_path

    obj = LinuxNetwork(module)
    result = obj.get_ethtool_data('ens160')

    assert result['phc_index'] == 2
    assert 'timestamping' in result
    assert 'hw_timestamp_filters' in result
    assert 'features' in result
    assert 'rx_checksumming' in result['features']
    assert 'tx_checksumming' in result['features']

# Generated at 2022-06-13 01:56:41.437908
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    module = AnsibleModule(argument_spec=dict())
    facts_module = LinuxNetwork(module=module)
    facts_module.populate()
    assert 'default_ipv4' in facts_module.network
    assert 'default_ipv6' in facts_module.network

# Generated at 2022-06-13 01:56:52.799274
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    hostname = "fake_hostname"
    module = MockLinuxNetwork(hostname)
    module.build_module_command_line = MagicMock(return_value=True)
    module.get_bin_path = MagicMock(return_value=True)

    # Initialize instance for testing
    network = LinuxNetwork(module)

    # Define dict for any absolute defaults

# Generated at 2022-06-13 01:56:58.248977
# Unit test for method populate of class LinuxNetwork
def test_LinuxNetwork_populate():
    '''
    Unit test for method LinuxNetwork.populate()
    '''
    module = mock.MagicMock()
    module.run_command.return_value = (0, '', '')
    module.get_bin_path.return_value = '/bin/ip'
    module.fail_json.side_effect = FailJsonException()
    module.deprecate.return_value = None
    network = LinuxNetwork(module)
    network.populate()


# Generated at 2022-06-13 01:57:07.667157
# Unit test for method get_ethtool_data of class LinuxNetwork
def test_LinuxNetwork_get_ethtool_data():

    module = AnsibleModule(argument_spec=dict())
    ln = LinuxNetwork(module)

    # ethtool -k <device>

# Generated at 2022-06-13 01:57:16.007213
# Unit test for method get_default_interfaces of class LinuxNetwork
def test_LinuxNetwork_get_default_interfaces():
    # NOTE: this test is going to be system-dependent
    # Should we be mocking /sys too?
    # I tried to make the test for an interface that is likely to be there
    # but that is not the loopback interface, so we can do aggressive mocking
    # of /sys, but that's not sufficient because we still need to mock the code
    # that uses the default routes and interfaces.
    #
    # In the bad old days we used to depend on /proc/net/route and ifconfig
    # and there was a single mock for these because it was just a file.
    module = AnsibleModule(argument_spec={})
    network = LinuxNetwork(module)
    # The commented-out one is on Fedora
    # For my current machine the one that's relevant is the last one,
    # but this method is under test
    #
    #

# Generated at 2022-06-13 01:58:07.672096
# Unit test for method get_interfaces_info of class LinuxNetwork
def test_LinuxNetwork_get_interfaces_info():
    module = FakeModule()
    class FakeLinuxNetwork(LinuxNetwork):
        def __init__(self):
            self.module = module
    l = FakeLinuxNetwork()
    l.module.run_command = fake_run_command
    default_ipv4 = {}
    default_ipv6 = {}
    l.get_interfaces_info(['ip'], default_ipv4, default_ipv6)