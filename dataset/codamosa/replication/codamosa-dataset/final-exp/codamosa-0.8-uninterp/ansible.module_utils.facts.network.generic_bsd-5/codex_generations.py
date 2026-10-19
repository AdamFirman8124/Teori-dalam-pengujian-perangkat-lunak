

# Generated at 2022-06-13 01:28:00.463817
# Unit test for method parse_inet_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet_line():
    # Arrange
    ifconfig_module = GenericBsdIfconfigNetwork()
    data = ["flags=8843<UP,BROADCAST,RUNNING,SIMPLEX,MULTICAST> metric 0 mtu 1500",
            "options=9b<RXCSUM,TXCSUM,VLAN_MTU,VLAN_HWTAGGING>",
            "ether a8:20:66:d0:33:11",
            "inet6 fe80::aa20:66ff:fed0:3311%en0 prefixlen 64 scopeid 0x5",
            "inet 192.168.1.75 netmask 0xffffff00 broadcast 192.168.1.255",
            "nd6 options=1<PERFORMNUD>",
            "media: autoselect",
            "status: active"]

# Generated at 2022-06-13 01:28:05.898977
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():
    #
    # Unit test for the method populate of class GenericBsdIfconfigNetwork
    #
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.network.base import NetworkCollector

    test_platform_mock = dict(
        system='Darwin',
        release='17.0.0',
        machine='x86_64'
    )
    mock_module = basic.AnsibleModule(argument_spec={}, supports_check_mode=True)

    mock_module.run_command = MagicMock(return_value=(0, '', '', 0))

# Generated at 2022-06-13 01:28:09.131914
# Unit test for method parse_media_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_media_line():
    input = ['media:', 'Ethernet', 'autoselect', '(1000baseT)']
    current_if = {}
    ips = {}
    netinfo = GenericBsdIfconfigNetwork()
    netinfo.parse_media_line(input, current_if, ips)
    assert current_if['media_type'] == '1000baseT'

# Generated at 2022-06-13 01:28:19.378447
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():
    #
    # Unit test for method GenericBsdIfconfigNetwork.populate
    #
    #     Unit test for method populate of class GenericBsdIfconfigNetwork
    #
    #     Note: part of the unit test was converted from the test_ansiterm.py
    #     unit test written by Karl Ramm
    #
    #     :return:
    #     """
    assert True
# end of test_GenericBsdIfconfigNetwork_populate


# Source: module_utils/network/common/linux.py
#
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
#

# Generated at 2022-06-13 01:28:25.861475
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_default_interfaces():
    module = AnsibleModuleMock()
    module.run_command = MagicMock(return_value=(0, V4_INTERFACE_OUTPUT, ''))
    network = GenericBsdIfconfigNetwork(module)
    default_ipv4, default_ipv6 = network.get_default_interfaces('route')
    assert default_ipv4 == {'address': '192.168.2.254',
                            'gateway': '192.168.2.1',
                            'interface': 'en0'}
    assert default_ipv6 == {}


# Generated at 2022-06-13 01:28:34.662909
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_default_interfaces():
    class Object(object):
        pass
    class Module(object):
        def get_bin_path(self, arg):
            return '/sbin/route'
        def run_command(self, arg):
            if arg == ['/sbin/route', '-n', 'get', '-inet6', 'default']:
                return 0, '', ''
            return 0, 'interface: lo0\ngateway: fe80::1%lo0\nflags: recvpipe  sendpipe ' \
                                                           'ssthresh  rtt,msec  rttvar  hopcount  mtu  expire ' \
                                                           'timeout\n  inet 127.0.0.1 netmask 0xff000000 \n  ' \
                                                           'dest 127.0.0.1   ', ''
    m = Module

# Generated at 2022-06-13 01:28:39.666278
# Unit test for method get_interfaces_info of class GenericBsdIfconfigNetwork

# Generated at 2022-06-13 01:28:52.017439
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():
    # input data to the method
    defaults = dict(
        interface='lo0',
        gateway='0.0.0.0'
    )
    interfaces = dict(
        lo0=dict(
            device='lo0',
            metric='0',
            mtu='16384',
            flags=['UP', 'LOOPBACK', 'RUNNING', 'MULTICAST'],
            ipv4=[{'address': '127.0.0.1'}],
            ipv6=[{'address': '::1'}],
        )
    )
    ifconfig_net = GenericBsdIfconfigNetwork()

    # call the method
    ifconfig_net.merge_default_interface(defaults, interfaces, 'ipv4')

    # assert expected results

# Generated at 2022-06-13 01:29:00.308295
# Unit test for method detect_type_media of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_detect_type_media():
    input1 = dict(
        bge0=dict(
            device='bge0',
            flags=[
                'UP',
                'BROADCAST',
                'RUNNING',
                'SIMPLEX',
                'MULTICAST'
            ],
            ipv4=[],
            ipv6=[],
            macaddress='xx:xx:xx:xx:xx:xx',
            media='Ethernet autoselect (1000baseT<full-duplex>)'
        )
    )


# Generated at 2022-06-13 01:29:11.953418
# Unit test for method parse_inet_line of class GenericBsdIfconfigNetwork

# Generated at 2022-06-13 01:29:30.632247
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():
    import platform
    module = AnsiModule()
    module.run_command = MagicMock(return_value=('', '', ''))
    module.get_bin_path = MagicMock(return_value='/sbin/ifconfig')

# Generated at 2022-06-13 01:29:42.872165
# Unit test for method parse_inet6_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet6_line():
    # Example output from FreeBSD ifconfig -a
    ifconfig_output = """lo1: flags=8049<UP,LOOPBACK,RUNNING,MULTICAST> metric 0 mtu 16384
        options=600003<RXCSUM,TXCSUM,RXCSUM_IPV6,TXCSUM_IPV6>
        inet6 ::1 prefixlen 128
        inet6 fe80::1%lo1 prefixlen 64 scopeid 0x7
        inet 127.0.0.1 netmask 0xff000000
        groups: lo
        nd6 options=21<PERFORMNUD,AUTO_LINKLOCAL>
        media: Ethernet autoselect (1000baseT <full-duplex>)
        status: active
        """

    # Example output from NetBSD ifconfig -a

# Generated at 2022-06-13 01:29:52.313640
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_default_interfaces():
    print("Testing method get_default_interfaces of class GenericBsdIfconfigNetwork")

    assert (GenericBsdIfconfigNetwork.get_default_interfaces(route_path=None, out_v4="""
default: gateway 192.168.1.1
    interface: en1
    local addr: 192.168.1.2
    destination: default
    mask: default
    flags: <UP,GATEWAY,DONE,STATIC,PRCLONING>
    recvpipe  sendpipe  ssthresh  rtt,msec    rttvar  hopcount      mtu     expire
    0         0          0         0           0       0          1500
    """)) == ({'interface': 'en1', 'gateway': '192.168.1.1', 'address': '192.168.1.2'}, {})

   

# Generated at 2022-06-13 01:30:02.689080
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_default_interfaces():
    module = AnsibleModule({})
    ipv4_interfaces = {'my_interfaces': {'interface': 'lo0', 'gateway': '10.10.10.1', 'address': '10.10.10.1'}}
    ipv6_interfaces = {'my_interfaces': {'interface': 'lo0', 'gateway': '2001:41d0:e:b3db::1', 'address': '2001:41d0:e:b3db::1'}}
    iface = GenericBsdIfconfigNetwork(module=module)
    assert iface.get_default_interfaces(TEST_ROUTE_PATH) == (ipv4_interfaces['my_interfaces'], ipv6_interfaces['my_interfaces'])

# Generated at 2022-06-13 01:30:12.748135
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_default_interfaces():
    def route_path(self):
        return 'route'
    def get_bin_path(self, arg):
        return arg
    module = imp.new_module('test_module')
    module.get_bin_path = get_bin_path
    module.run_command = route_path
    network = GenericBsdIfconfigNetwork(module)


# Generated at 2022-06-13 01:30:22.935398
# Unit test for method parse_media_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_media_line():

    testcase = dict(
        test='media, media_select and media_options',
        line='media: Ethernet autoselect (1000baseSX <full-duplex>)',
        current_if=dict(media=None,media_select=None,media_options=None),
        ips=None,
        expected_if=dict(media='Ethernet', media_select='autoselect',
            media_options=['1000baseSX','full-duplex'])
    )

    dut = GenericBsdIfconfigNetwork()
    dut.parse_media_line(testcase['line'].split(), testcase['current_if'],
        testcase['ips'])

    if testcase['current_if'] == testcase['expected_if']:
        print(testcase['test'] + ': pass')

# Generated at 2022-06-13 01:30:30.869531
# Unit test for method parse_media_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_media_line():
    def test_input(words, current_if, ips, expected):
        n = GenericBsdIfconfigNetwork()
        n.parse_media_line(words, current_if, ips)
        assert (current_if, ips) == expected, "input: '%s' expected: '%s', got: '%s'" % (
            words, expected, (current_if, ips))

    # test values gleaned from FreeBSD, OpenBSD and macOS running ifconfig
    # [media_string, [media_select string], [media_type], [media_options string]]

# Generated at 2022-06-13 01:30:41.593153
# Unit test for method get_options of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_options():
    m = module_utils.BasicModuleForTests('noop')
    m.params = {}
    n = GenericBsdIfconfigNetwork(m)
    assert n.get_options('<LOOPBACK,UP,LOWER_UP>') == ['LOOPBACK', 'UP', 'LOWER_UP']
    assert n.get_options('<LOOPBACK,UP,LOWER_UP> mtu') == ['LOOPBACK', 'UP', 'LOWER_UP']
    assert n.get_options('<>') == []
    assert n.get_options('<> mtu') == []
    assert n.get_options('<UP,LOWER_UP> mtu') == ['UP', 'LOWER_UP']
    assert n.get_options('mtu') == []

# Generated at 2022-06-13 01:30:46.520384
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():
    module_mock = mock.MagicMock()
    module_mock.get_bin_path.return_value = '/sbin/ifconfig'


# Generated at 2022-06-13 01:30:58.022444
# Unit test for method parse_media_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_media_line():
    from sys import platform as _platform
    from ansible.module_utils.network.freebsd.ifconfig import GenericBsdIfconfigNetwork

    # netbsd
    module_mock = MagicMock()
    module_mock.check_mode = False
    module_mock.run_command.return_value = (0, "media: Ethernet autoselect (1000baseT full-duplex,master,flowcontrol,rxpause,txpause)", "")
    gb = GenericBsdIfconfigNetwork(module_mock)

    current_if = {}
    current_if = gb.parse_media_line(current_if, "media: Ethernet autoselect (1000baseT full-duplex,master,flowcontrol,rxpause,txpause)".split())
    assert current_if['media'] == 'Ethernet'
   

# Generated at 2022-06-13 01:31:59.031294
# Unit test for method detect_type_media of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_detect_type_media():
    GenericBsdIfconfigNetwork = get_ansible_module('GenericBsdIfconfigNetwork')
    obj = GenericBsdIfconfigNetwork()
    interfaces = {
        'lo0': {'media': 'fddi0'},
        'en0': {'media': 'ether'},
        'en1': {'media': 'ethernet'},
        'en3': {'media': 'FooBar'},
    }
    interfaces = obj.detect_type_media(interfaces)

    assert 'lo0' not in interfaces
    assert 'type' not in interfaces['lo0']

    assert 'type' in interfaces['en0']
    assert interfaces['en0']['type'] == 'ether'

    assert 'type' in interfaces['en1']
    assert interfaces['en1']['type'] == 'ether'

# Generated at 2022-06-13 01:32:08.736937
# Unit test for method parse_inet_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet_line():
    module = generic_ansible_module

    # test cases for
    # get_interfaces_info(self, ifconfig_path, ifconfig_options='-a')


# Generated at 2022-06-13 01:32:17.936435
# Unit test for method get_interfaces_info of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_interfaces_info():
    global module
    global ifconfig_path
    global route_path
    print("Executing tests for module")
    # We create a class for testing get_interfaces_info method

# Generated at 2022-06-13 01:32:22.302426
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_default_interfaces():
    generic_bsd_ifconfig_network = GenericBsdIfconfigNetwork()
    generic_bsd_ifconfig_network.get_default_interfaces(route_path)
    assert True

# Generated at 2022-06-13 01:32:33.698041
# Unit test for method get_interfaces_info of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_interfaces_info():
    module = AnsibleModule(argument_spec={})

    if not hasattr(module, 'run_command'):
        module.run_command = lambda x, check_rc=True: (0, '', '')
    if not hasattr(module, 'get_bin_path'):
        module.get_bin_path = lambda x: None

    ifconfig_network = GenericBsdIfconfigNetwork(module)

    # call it with an arbitrary path
    interfaces, ips = ifconfig_network.get_interfaces_info('/bin/ifconfig')

    # we should have some lists
    assert isinstance(interfaces, dict)
    assert isinstance(ips, dict)
    assert 'all_ipv4_addresses' in ips
    assert 'all_ipv6_addresses' in ips

# Generated at 2022-06-13 01:32:41.748649
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():
    g = GenericBsdIfconfigNetwork()

    defaults = {'interface': 'tun0', 'address': '10.0.0.1'}

# Generated at 2022-06-13 01:32:50.050544
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():
    class config:
        pass

    class params:
        pass

    # setup test fixture
    defaults = {'interface': 'vlan0', 'address': '10.10.10.1', 'gateway': '10.10.10.1'}

# Generated at 2022-06-13 01:32:55.163564
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_default_interfaces():
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )
    network_facts = GenericBsdIfconfigNetwork()
    network_facts.module = module
    network_facts.get_default_interfaces('/sbin/route')

# Generated at 2022-06-13 01:33:02.469467
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():
    module = AnsibleModule(argument_spec={})
    ifconfig_path = module.get_bin_path('ifconfig')
    route_path = module.get_bin_path('route')
    if not ifconfig_path:
        pytest.skip("test needs ifconfig")
    if not route_path:
        pytest.skip("test needs route")
    module.run_command = MagicMock(return_value=(0, '', ''))
    module.run_command.side_effect = RuntimeError(
        """Unknown media: <none>, expected ether
        ifconfig: SIOCSIFFLAGS: No such file or directory
        ifconfig: SIOCSIFFLAGS: No such file or directory"""
    )
    network = GenericBsdIfconfigNetwork(module)
    output = network.populate()

# Generated at 2022-06-13 01:33:12.536192
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():
    BsdNet = GenericBsdIfconfigNetwork()
    defaults = {'interface' : 'lo0', 'address' : '127.0.0.1'}
    interfaces = {'lo0' : {'ipv4': [{'address': '127.0.0.1'}]}}
    BsdNet.merge_default_interface(defaults, interfaces, 'ipv4')
    assert defaults == {'interface' : 'lo0', 'address' : '127.0.0.1'}
    defaults = {'interface' : 'lo0', 'address' : '127.0.0.8'}
    interfaces = {'lo0' : {'ipv4': [{'address': '127.0.0.1'}]}}

# Generated at 2022-06-13 01:33:36.358760
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_default_interfaces():
    result = {'default_ipv4': {'interface': 'lo0', 'gateway': '127.0.0.1', 'address': '127.0.0.1'}, 'default_ipv6': {'interface': 'lo0', 'gateway': '::1'}}
    assert GenericBsdIfconfigNetwork().get_default_interfaces('route') == result


# Generated at 2022-06-13 01:33:47.070872
# Unit test for method populate of class GenericBsdIfconfigNetwork

# Generated at 2022-06-13 01:33:48.723267
# Unit test for method get_interfaces_info of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_interfaces_info():
    generic_ifconfig_class = GenericBsdIfconfigNetwork()
    generic_ifconfig_class.get_interfaces_info("ifconfig");


# Generated at 2022-06-13 01:33:51.993624
# Unit test for method get_options of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_options():
    network = GenericBsdIfconfigNetwork()
    options = network.get_options("<UP,BROADCAST,RUNNING,PROMISC,SIMPLEX,MULTICAST>")
    assert 6 == len(options)
    assert "UP" in options
    assert "BROADCAST" in options
    assert "RUNNING" in options
    assert "PROMISC" in options
    assert "SIMPLEX" in options
    assert "MULTICAST" in options


# Generated at 2022-06-13 01:33:55.488679
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():
    module = AnsibleModule(argument_spec=dict(
        gather_subset=dict(default=['!all'], type='list')
    ))
    obj = GenericBsdIfconfigNetwork(module)
    result = obj.populate()
    assert result['default_ipv4']['interface'] != 'unknown'

# Generated at 2022-06-13 01:34:06.564324
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_default_interfaces():
    from ansible_collections.ansible.community.tests.unit.compat.mock import patch, PropertyMock

    class TestGenericBsdIfconfigNetwork(GenericBsdIfconfigNetwork):
        platform = 'Generic_BSD_Ifconfig'

        def populate(self, collected_facts=None):
            pass

    def my_run_command(self, args, check_rc=True):
        class ret:
            def __init__(self, rc, out, err):
                self.rc = rc
                self.stdout = out
                self.stderr = err
                self.stdin = None

        class MockCommandResult:
            def __init__(self, out, err, rc):
                self.stdout = out
                self.stderr = err
                self.rc = rc


# Generated at 2022-06-13 01:34:18.004584
# Unit test for method parse_inet_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet_line():
    generic_bsd_ifconfig_network = GenericBsdIfconfigNetwork()
    current_if = {}
    ips = {}
    words = ['lo0:', 'inet', '127.0.0.1', 'netmask', '0xff000000']
    generic_bsd_ifconfig_network.parse_inet_line(words, current_if, ips)

# Generated at 2022-06-13 01:34:26.447772
# Unit test for method parse_interface_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_interface_line():
    """
    Test for method parse_interface_line of class GenericBsdIfconfigNetwork
    """
    bsd_ifconfig_network = GenericBsdIfconfigNetwork(None)

# Generated at 2022-06-13 01:34:34.168214
# Unit test for method parse_inet_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet_line():
    cmd1 = "lo0: flags=8049<UP,LOOPBACK,RUNNING,MULTICAST> metric 0 mtu 16384 options=600003<RXCSUM,TXCSUM,RXCSUM_IPV6,TXCSUM_IPV6> groups: lo nd6 options=21<PERFORMNUD,AUTO_LINKLOCAL> inet 127.0.0.1 netmask 0xff000000 inet6 ::1 prefixlen 128 inet6 fe80::1%lo0 prefixlen 64 scopeid 0x1 inet6 fe80::1%lo0 prefixlen 64 scopeid 0x1 inet 127.1.1.1 netmask 0xff000000"

# Generated at 2022-06-13 01:34:43.872327
# Unit test for method detect_type_media of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_detect_type_media():
    test_GenericBsdIfconfigNetwork = GenericBsdIfconfigNetwork()

# Generated at 2022-06-13 01:35:26.403935
# Unit test for method parse_interface_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_interface_line():
    module = AnsibleModule(argument_spec={})
    module.check_mode = True
    module.exit_json = Mock()
    module.run_command = Mock()
    module.run_command.side_effect = [(0, None, None), (0, None, None)]
    module.get_bin_path = Mock()
    module.get_bin_path.side_effect = ['/sbin/route', '/sbin/ifconfig']
    network = GenericBsdIfconfigNetwork(module) 
    current_if = network.parse_interface_line(['lo0', 'flags=8049<UP,LOOPBACK,RUNNING,MULTICAST>', 'metric', '0', 'mtu', '1280'])
    assert current_if['device'] == 'lo0'

# Generated at 2022-06-13 01:35:33.926547
# Unit test for method get_interfaces_info of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_interfaces_info():
    m = GenericBsdIfconfigNetworkModule(argument_spec={},
                                        check_invalid_arguments=False,
                                        bypass_checks=True)

    # for coverage we need more of a real example but this is a
    # simple start
    ifconfig_path = m.get_bin_path('ifconfig')

    if ifconfig_path:
        ifconfig_options = "-a"
        network = GenericBsdIfconfigNetwork()
        interfaces, ips = network.get_interfaces_info(ifconfig_path, ifconfig_options)
        assert 'lo0' in interfaces
        assert 'flags' in interfaces['lo0']
        assert 'mtu' in interfaces['lo0']
        assert 'ipv4' in interfaces['lo0']
        assert 'ipv6' in interfaces['lo0']

        # TODO

# Generated at 2022-06-13 01:35:42.502941
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_default_interfaces():
    gni = GenericBsdIfconfigNetwork()
    # Test IPv4 route
    gni._module = Mock(run_command = Mock(return_value=(0, """
route to: default
destination: default
  route to: default
       gateway: 10.188.10.1
    interface: eth5
      priority: 1
       address: 10.188.10.57
""", '')))
    expected_v4 = {'address': '10.188.10.57', 'interface': 'eth5', 
                   'priority': '1', 'gateway': '10.188.10.1'}
    # Test IPv6 route

# Generated at 2022-06-13 01:35:50.443263
# Unit test for method parse_inet_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet_line():

  current_if = dict(device='lo0', ipv4=[])
  words = ['inet', '127.0.0.1', 'netmask', '0xff000000']

  gen_net = GenericBsdIfconfigNetwork()
  gen_net.parse_inet_line(words, current_if)

  assert current_if == {
    'device': 'lo0',
    'ipv4': [
      {
        'address': '127.0.0.1',
        'netmask': '255.0.0.0',
        'network': '127.0.0.0',
        'broadcast': '127.255.255.255'
      }
    ]
  }


  current_if = dict(device='lo0', ipv4=[])

# Generated at 2022-06-13 01:35:56.517662
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():
    defaults = {'interface': 'em0'}
    interfaces = {'em0': {'ipv4': [{'broadcast': '192.168.1.255', 'netmask': '255.255.255.0', 'network': '192.168.1.0', 'address': '192.168.1.100'}], 'device': 'em0', 'macaddress': '00:1f:c6:d6:3c:3f'}}
    network = GenericBsdIfconfigNetwork()
    network.merge_default_interface(defaults, interfaces, 'ipv4')

# Generated at 2022-06-13 01:36:06.621500
# Unit test for method get_interfaces_info of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_interfaces_info():
    obj = GenericBsdIfconfigNetwork()
    interfaces_info = obj.get_interfaces_info(ifconfig_path="tests/ifconfig_example.txt")

# Generated at 2022-06-13 01:36:13.853869
# Unit test for method get_interfaces_info of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_interfaces_info():
    # Create module object to pass as self to get_interfaces_info
    module = MagicMock()
    module.run_command = MagicMock()
    module.run_command.return_value = (0, '', '')
    interface_info = GenericBsdIfconfigNetwork(module)

    # Test case 1 - macos

# Generated at 2022-06-13 01:36:21.837043
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_default_interfaces():
    module = AnsibleModule(argument_spec=dict())
    if not module.check_mode:
        route_path = module.get_bin_path('route')
        if route_path is None:
            module.exit_json(msg="route not found in PATH.")
    # Emulate the route command output - a list of strings, each string is a line
    output = [
        "default 192.168.128.1 UGSc 96 0 en0",
        "25:26:27:28:29:30%en0 link#7 UHLWIi  108327 10   en1",
        "26:27:28:29:30:31%en0 link#7 UHLWIi  108327 10   en1",
    ]
    # Instantiate the class under test and call the method under test
    class_under_test

# Generated at 2022-06-13 01:36:27.914786
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_default_interfaces():
    class MockModule():
        def __init__(self):
            self.params = dict()

        def get_bin_path(self, arg, required=False):
            return arg


# Generated at 2022-06-13 01:36:36.587551
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():
    object = GenericBsdIfconfigNetwork(module)
    iface1 = {
        'device': 'lo0',
        'ipv4': [{'address': '127.0.0.1', 'netmask': '255.0.0.0', 'broadcast': '0.0.0.0', 'network': '127.0.0.0'}],
        'ipv6': [],
        'mtu': '16384',
        'type': 'loopback',
        'flags': ['UP', 'LOOPBACK', 'RUNNING']
    }