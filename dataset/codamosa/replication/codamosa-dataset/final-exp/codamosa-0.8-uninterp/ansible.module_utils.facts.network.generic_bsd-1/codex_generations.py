

# Generated at 2022-06-13 01:28:07.921488
# Unit test for method parse_ether_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_ether_line():
    ifc = GenericBsdIfconfigNetwork()
    # the line 'ether 5c:f9:dd:a1:e7:ad' should produce a type ether entry
    # TODO: Testing on a 64 bit system without a 64bit MACHINE test fails
    if socket.has_ipv6:
        assert ifc.parse_ether_line(['ether', '5c:f9:dd:a1:e7:ad'], {'device': 'vmx0'}, {})['vmx0']['type'] == 'ether'
        assert ifc.parse_ether_line(['ether', '5c:f9:dd:a1:e7:ad'], {'device': 'vmx0', 'type': 'loopback'}, {})['vmx0']['type'] == 'loopback'

# Generated at 2022-06-13 01:28:12.134030
# Unit test for method get_options of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_options():
    network = GenericBsdIfconfigNetwork()
    result = network.get_options('<LOOPBACK,RUNNING>')
    expected = ['LOOPBACK', 'RUNNING']
    assert result == expected


# Generated at 2022-06-13 01:28:20.272228
# Unit test for method parse_ether_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_ether_line():
    module = AnsibleModule({})

    def get_bin_path(path):
        return path

    module.get_bin_path = get_bin_path

    network_facts = GenericBsdIfconfigNetwork()
    network_facts.module = module

    # create test data
    line = "ether 08:00:27:c5:5b:ee"
    words = line.split()
    current_if = {'device': "eth0"}

    # call the parse_ether_line function
    network_facts.parse_ether_line(words, current_if, None)

    # check if data is as expected
    assert current_if['macaddress'] == "08:00:27:c5:5b:ee"


# Generated at 2022-06-13 01:28:24.593651
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():
    bsdIfconfigNetwork = GenericBsdIfconfigNetwork(None, None)
    defaults = dict()
    interfaces = dict()
    ip_type = 'ipv6'
    bsdIfconfigNetwork.merge_default_interface(defaults, interfaces, ip_type)
    assert(defaults == {})


# Generated at 2022-06-13 01:28:33.428723
# Unit test for method parse_media_line of class GenericBsdIfconfigNetwork

# Generated at 2022-06-13 01:28:45.474982
# Unit test for method parse_inet_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet_line():
    # build sample objects
    net = GenericBsdIfconfigNetwork()
    # We don't want the side effect of passing ips to real code
    ips = dict(
        all_ipv4_addresses=[],
        all_ipv6_addresses=[],
    )

    # word list from a 'ifconfig -a' will be parsed
    words = ['lo0:', 'flags=8049<UP,LOOPBACK,RUNNING,MULTICAST>',
             'mtu', '16384', 'inet6', '::1', 'prefixlen', '128', 'inet6',
             'fe80::1%lo0', 'prefixlen', '64', 'scopeid', '0x1', 'inet',
             '127.0.0.1', 'netmask', '0xff000000']

# Generated at 2022-06-13 01:28:56.703703
# Unit test for method detect_type_media of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_detect_type_media():
    # Test normal function
    test_interfaces = GenericBsdIfconfigNetwork()

# Generated at 2022-06-13 01:29:02.208087
# Unit test for method get_interfaces_info of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_interfaces_info():
    d = GenericBsdIfconfigNetwork()
    ifconfig_path = '/sbin/ifconfig'
    data = d.get_interfaces_info(ifconfig_path)
    assert len(data[0]) == 0
    assert len(data[1]['all_ipv4_addresses']) == 0
    assert len(data[1]['all_ipv6_addresses']) == 0


# Generated at 2022-06-13 01:29:13.590614
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():
    defaults = {'gateway': '192.168.1.1', 'address': '192.168.1.2', 'interface': 'en0'}

# Generated at 2022-06-13 01:29:25.031328
# Unit test for method parse_inet6_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet6_line():
    gf = GenericBsdIfconfigNetwork()
    ips = dict(
        all_ipv4_addresses=list(),
        all_ipv6_addresses=list(),
    )
    words = []

    # test 1
    words = "['inet6', 'fe80::1:1:1:1%em0', 'prefixlen', '64', 'scopeid', '0x2']"
    current_if = {}
    gf.parse_inet6_line(eval(words), current_if, ips)
    assert('fe80::1:1:1:1' in ips['all_ipv6_addresses'])
    assert('address' in current_if)
    assert('prefix' in current_if)

# Generated at 2022-06-13 01:29:39.629091
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():
    pass

# Generated at 2022-06-13 01:29:50.289875
# Unit test for method parse_inet_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet_line():
    passed = True
    ifconfig = GenericBsdIfconfigNetwork()
    # Test basic IPv4 parsing
    test_inet_line = "inet 127.0.0.1 netmask 0xff000000"
    current_if = {'device': "lo0"}
    ips = {
        'all_ipv4_addresses':[],
        'all_ipv4_addresses':[],
    }
    test_inet_words = test_inet_line.split()
    ifconfig.parse_inet_line(test_inet_words, current_if, ips)

# Generated at 2022-06-13 01:30:01.088303
# Unit test for method parse_interface_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_interface_line():
    # netbsd, openbsd
    print(len(GenericBsdIfconfigNetwork().parse_interface_line(
        ['lo0', 'flags=8049<UP,LOOPBACK,RUNNING,MULTICAST>', 'mtu', '33184'])))
    print(len(GenericBsdIfconfigNetwork().parse_interface_line(
        ['em0', 'flags=8843<UP,BROADCAST,RUNNING,SIMPLEX,MULTICAST>', 'metric', '0', 'mtu', '1500', 'options=c1ab<RXCSUM,TXCSUM,VLAN_MTU>'])))

# Generated at 2022-06-13 01:30:09.407945
# Unit test for method parse_inet6_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet6_line():
    module = AnsibleModule(argument_spec=dict())
    ifconfig_facts = GenericBsdIfconfigNetwork(module)

    interface = {}
    words = "inet6 fe80::21b:77ff:fe8f:7c3a%nve0 prefixlen 64 scopeid 0x9".split()
    ips = dict()
    ifconfig_facts.parse_inet6_line(words, interface, ips)
    assert_equals(ips["all_ipv6_addresses"], ['fe80::21b:77ff:fe8f:7c3a'])

# Generated at 2022-06-13 01:30:15.319142
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():
    defaults = dict()
    interfaces = dict(en0=dict(ipv4=[dict(address='1.1.1.1')], ipv6=[dict(address='2.2.2.2')]))
    ng = GenericBsdIfconfigNetwork()
    ng.merge_default_interface(defaults, interfaces, 'ipv4')
    assert defaults == dict(interface='en0', address='1.1.1.1')


# Generated at 2022-06-13 01:30:24.737063
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_default_interfaces():
    import sys
    import os
    import inspect
    import tempfile
    import subprocess
    from ansible_collections.ansible.community.tests.unit.compat.mock import patch
    from ansible.module_utils.facts import NetworkCollector
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork
    from ansible.module_utils.facts.network.base import NetworkCollector as baseNetworkCollector
    from ansible.module_utils.facts.network.base import NetworkCollector
    from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork

# Generated at 2022-06-13 01:30:31.048008
# Unit test for method parse_media_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_media_line():
    import platform

    module = AnsibleModule(argument_spec=dict())
    conn = GenericBsdIfconfigNetwork(module)

    # most modern BSDs should use this media line formatting (FreeBSD, NetBSD, DragonFly)
    media_line = "media: Ethernet autoselect (1000baseT <full-duplex,flow-control,energy-detect-wakeup>)"
    current_if = {'device': 'em0'}
    ips = {
        'all_ipv4_addresses': [],
        'all_ipv6_addresses': [],
    }
    conn.parse_media_line(media_line.split(), current_if, ips)
    assert current_if['media'] == "Ethernet"
    assert current_if['media_select'] == "autoselect"
   

# Generated at 2022-06-13 01:30:38.025870
# Unit test for method get_interfaces_info of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_interfaces_info():
    module = AnsibleModule(
        argument_spec={},
        supports_check_mode=False
    )

    ifconfig_path = module.get_bin_path('ifconfig')

    # Testing with a file that contains the output of ifconfig -a
    filename = Path(__file__).absolute().parent / 'ifconfig_output.txt'
    with codecs.open(filename, 'r', encoding='utf-8', errors='ignore') as f:
        output = f.read()
    interfaces, ips = get_interfaces_info(ifconfig_path, output)

    assert interfaces['lo0']['device'] == 'lo0'
    assert interfaces['lo0']['ipv4'][0]['address'] == '127.0.0.1'

# Generated at 2022-06-13 01:30:45.022042
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():
    def_interface = dict(interface='lo0')
    ifconfigs = dict(lo0=dict(ipv4=[dict(address='127.1.1.1')]))

    genbsdifconfignetwork = GenericBsdIfconfigNetwork()
    genbsdifconfignetwork.merge_default_interface(def_interface, ifconfigs, 'ipv4')

    assert '127.1.1.1' in def_interface.values()



# Generated at 2022-06-13 01:30:56.054887
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_default_interfaces():
    module = AnsibleModule(argument_spec={})
    module.run_command = MagicMock()

    output_route_v4 = '''
interface: vtnet0
  destination: default
  mask: default
  gateway: 10.0.0.1
  metric: 0
'''

    output_route_v6 = '''
interface: vtnet0
  destination: default
  gateway: fe80::bba3:eaff:fe01:27a7%vtnet0
  flags: <UP,GATEWAY,DONE,STATIC>
  recvpipe  sendpipe  ssthresh  rtt,msec    rttvar  hopcount      mtu     expire
  0         0         0         0           0       0             1500    0
'''


# Generated at 2022-06-13 01:31:10.583560
# Unit test for method get_interfaces_info of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_interfaces_info():
    network_module = GenericBsdIfconfigNetwork()
    interfaces = network_module.get_interfaces_info("/sbin/ifconfig")
    assert interfaces is not None


# Generated at 2022-06-13 01:31:18.239164
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():
    defaults = {'interface':'lo0'}
    interfaces = {'lo0':{'ipv4':[{'address':'127.0.0.1','netmask':'255.255.255.0','broadcast':'127.0.0.1'}, {'address':'127.0.0.2','netmask':'255.255.255.0','broadcast':'127.0.0.2'}],'ipv6':[{'address':'::1','prefix':'128'}, {'address':'fe80::1%lo0','prefix':'64'}]}}
    testobj = GenericBsdIfconfigNetwork()
    testobj.merge_default_interface(defaults, interfaces, 'ipv4')

# Generated at 2022-06-13 01:31:27.480748
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():
    from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork
    class ModuleMock(object):
        def get_bin_path(self, arg):
            path = arg
            if arg == "ifconfig":
                path = "test/unit/module_utils/facts/network/generic_bsd/ifconfig"
        def run_command(self, arg):
            rc = 0
            out = ""
            err = ""
            return rc, out, err
    module = ModuleMock()
    class FactsMock(object):
        def __init__(self):
            self.__dict__['data'] = {}
    facts = FactsMock()
    network = GenericBsdIfconfigNetwork(module)
    network.populate(facts)

# Generated at 2022-06-13 01:31:39.607157
# Unit test for method get_interfaces_info of class GenericBsdIfconfigNetwork

# Generated at 2022-06-13 01:31:47.199892
# Unit test for method get_interfaces_info of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_interfaces_info():
  # Testing sample output for 'ifconfig' command for different interfaces
  # to check if the correct output can be parsed on the platform when the
  # 'ifconfig' command is executed.

  output_lo0 = '''
    lo0: flags=8049<UP,LOOPBACK,RUNNING,MULTICAST> metric 0 mtu 16384
        options=3<RXCSUM,TXCSUM>
        inet 127.0.0.1 netmask 0xff000000
        inet6 ::1 prefixlen 128
        inet6 fe80::1%lo0 prefixlen 64 scopeid 0x1
        nd6 options=1<PERFORMNUD>
        groups: lo
  '''

# Generated at 2022-06-13 01:31:50.606767
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_default_interfaces():
    facts = GenericBsdIfconfigNetwork()
    for bsd_type in ['freebsd', 'openbsd', 'netbsd', 'dragonflybsd', 'macosx']:
        facts.platform = bsd_type + "_ifconfig"
        default_ipv4, default_ipv6 = facts.get_default_interfaces('route')
        assert('interface' in default_ipv4)
        assert('interface' in default_ipv6)


# Generated at 2022-06-13 01:31:58.949205
# Unit test for method get_interfaces_info of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_interfaces_info():
    import os
    import tempfile

    # Test interfaces.

# Generated at 2022-06-13 01:32:08.649283
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():
    generic_bsd_ifconfig_network = GenericBsdIfconfigNetwork({'bin_path_settings': {'ifconfig': u'/sbin/ifconfig', 'route': u'/sbin/route'}, 'run_command': run_command})

# Generated at 2022-06-13 01:32:17.834673
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_default_interfaces():
    # TODO: mock out subprocess.Popen and catch the command
    #       so we can ensure the right one is called
    #       and insert canned output
    # TODO: mock out the platform module to test the other platforms
    m = {
        'route  -n get default'.split(): 'default: gateway: 10.0.3.2 interface: utun2',
        'route  -n get -inet6 default'.split(): 'default: gateway: ::1%lo0 interface: lo0',
    }
    p = run_command(m)
    g = GenericBsdIfconfigNetwork(dict(module=p))
    v4, v6 = g.get_default_interfaces('route')

    assert v4['gateway']=='10.0.3.2'

# Generated at 2022-06-13 01:32:30.819784
# Unit test for method parse_interface_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_interface_line():
    from ansible.module_utils.network.common.utils import load_platform_subclass
    from ansible_collections.notstdlib.moveitallout.plugins.module_utils.network.common import ipaddress

    obj = load_platform_subclass(GenericBsdIfconfigNetwork, platform='Generic_BSD_Ifconfig')
    iface = "lo0: flags=8049<UP,LOOPBACK,RUNNING,MULTICAST> metric 0 mtu 16384"
    iface2 = "lo0: flags=8049<UP,LOOPBACK,RUNNING,MULTICAST> metric 0 mtu 16384\n        options=123456789"
    iface3 = "lo0: flags=8049<UP,LOOPBACK,RUNNING,MULTICAST> metric 0 options=123456789"

# Generated at 2022-06-13 01:32:42.824865
# Unit test for method get_interfaces_info of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_interfaces_info():
    GenericBsdIfconfigNetwork.get_interfaces_info()


# Generated at 2022-06-13 01:32:50.694297
# Unit test for method parse_interface_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_interface_line():
    # Test 1
    module = MockModule({'PATH': '/bin:/usr/bin'})
    network = GenericBsdIfconfigNetwork(module)
    words = ['lo0:', 'flags=8049<UP,LOOPBACK,RUNNING,MULTICAST>', 'mtu', '33184', 'metric', '1']

    current_if = network.parse_interface_line(words)
    assert current_if['device'] == 'lo0'
    assert current_if['flags'] == ['UP', 'LOOPBACK', 'RUNNING', 'MULTICAST']
    assert current_if['macaddress'] == 'unknown'
    assert current_if['type'] == 'loopback'
    assert current_if['metric'] == '1'
    assert current_if['mtu'] == '33184'

   

# Generated at 2022-06-13 01:33:00.143701
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():
    # Because the GenericBsdIfconfigNetwork class is abstract,
    # we can't instantiate it directly. We must test it
    # via a subclass that provides concrete implementations for
    # all abstract methods.
    class GenericBsdIfconfigNetworkSubclass(GenericBsdIfconfigNetwork):
        # This class isn't abstract, so we can directly instantiate an object
        # for testing.
        def __init__(self, *args, **kwargs):
            super(GenericBsdIfconfigNetworkSubclass, self).__init__(*args, **kwargs)
            # We need to stub the module so that it returns a valid path
            # to the "ifconfig" utility.
            self.module = AnsibleModuleStub()

    # The string we're going to pass to ifconfig to test the parser

# Generated at 2022-06-13 01:33:11.945594
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():
    a_platform = 'Generic_BSD_Ifconfig'
    a_interfaces_dict = dict(eth0=dict(device='eth0', flags=['LOOPBACK', 'RUNNING']),
                             eth1=dict(device='eth1', flags=['LOOPBACK', 'RUNNING']))
    a_default_ipv4 = dict(interface='eth1', address='fe80::1')
    a_default_ipv6 = dict(interface='eth1', address='fe80::1')

    a_instance = GenericBsdIfconfigNetwork()

    a_instance.merge_default_interface(a_default_ipv4, a_interfaces_dict, 'ipv4')

# Generated at 2022-06-13 01:33:21.653467
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_default_interfaces():
    """Test get_default_interfaces function of GenericBsdIfconfigNetwork"""

    module = AnsibleModule(
        argument_spec=dict(
            route_path=dict(required=True),
        ),
        supports_check_mode=False
    )

    route_path = module.params['route_path']
    net_facts = GenericBsdIfconfigNetwork()
    ipv4, ipv6 =  net_facts.get_default_interfaces(route_path)
    module.exit_json(changed=False, ansible_facts={'ipv4': ipv4, 'ipv6': ipv6})


# Generated at 2022-06-13 01:33:33.140982
# Unit test for method parse_media_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_media_line():
    network_module = GenericBsdIfconfigNetwork()
    words = ['media:','Ethernet','10Gbase-SR','<full-duplex>','status:','active','nordic', 'word']
    current_if = {'device': 'eth0', 'ipv4': [], 'ipv6': []}
    ips = {'ipv4': [], 'ipv6': []}

    expected_current_if = {'device': 'eth0', 'ipv4': [], 'ipv6': [], 'media': 'Ethernet', 'media_select': '10Gbase-SR', 'media_type': 'full-duplex', 'media_options': ['full-duplex']}

    network_module.parse_media_line(words, current_if, ips)


# Generated at 2022-06-13 01:33:37.520437
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_default_interfaces():
    module = AnsibleModule(argument_spec={})
    actual = GenericBsdIfconfigNetwork(module).get_default_interfaces('route')
    assert actual == ({'interface': 'lo0', 'gateway': None}, {'interface': 'lo0', 'gateway': None})


# Generated at 2022-06-13 01:33:48.298152
# Unit test for method get_interfaces_info of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_interfaces_info():
    # Requires Python 2.7 or above
    from unittest import TestCase
    from mock import patch
    from ansible.module_utils.facts.network.generic_bsd import get_interfaces_info

    class MockModule:
        def __init__(self):
            self.run_command = patch("ansible.module_utils.facts.network.generic_bsd.run_command").start()

    class MockPopen:
        def __init__(self, pid):
            self.pid = pid
            self.stdout = []
            self.stderr = []

        def communicate(self):
            stdout = "\n".join(self.stdout)
            stderr = "\n".join(self.stderr)
            return stdout, stderr


# Generated at 2022-06-13 01:33:54.253189
# Unit test for method detect_type_media of class GenericBsdIfconfigNetwork

# Generated at 2022-06-13 01:34:05.104143
# Unit test for method parse_media_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_media_line():
    module = AnsibleModule(argument_spec=dict())
    module.exit_json = exit_json
    module.fail_json = fail_json

    words = [
        'media:',
        'Ethernet',
        'autoselect',
        '(1000baseT)',
    ]

    host_facts = GenericBsdIfconfigNetwork().get_interfaces_info(
        ifconfig_path=None, ifconfig_options=None)
    current_if = host_facts[0][list(host_facts[0].keys())[0]]
    GenericBsdIfconfigNetwork().parse_media_line(words, current_if, host_facts[1])

    assert 'media' in current_if
    assert 'media_select' in current_if
    assert 'media_type' in current_if

# Generated at 2022-06-13 01:34:27.701798
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_default_interfaces():
    module = AnsibleModule(argument_spec=dict())
    p = GenericBsdIfconfigNetwork(module)
    assert p.get_default_interfaces('') == ({}, {})


# Generated at 2022-06-13 01:34:34.967758
# Unit test for method parse_interface_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_interface_line():
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )
    words = ['lo0:', 'flags=8049<UP,LOOPBACK,RUNNING,MULTICAST>', 'metric', '0', 'mtu', '16384', 'options=600003<RXCSUM,TXCSUM,RXCSUM_IPV6,TXCSUM_IPV6>']


# Generated at 2022-06-13 01:34:44.340916
# Unit test for method get_interfaces_info of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_interfaces_info():
    platform = 'Generic_BSD_Ifconfig'
    ifconfig_path = 'ifconfig'
    module = AnsibleModule(argument_spec={})
    obj = GenericBsdIfconfigNetwork(platform, module)

    interfaces, ips = obj.get_interfaces_info(ifconfig_path)


# Generated at 2022-06-13 01:34:53.619322
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():
    fd, src = tempfile.mkstemp(text=True)


# Generated at 2022-06-13 01:35:04.227984
# Unit test for method parse_media_line of class GenericBsdIfconfigNetwork

# Generated at 2022-06-13 01:35:13.401177
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():
    import platform
    generic_bsd_ifconfig_network = GenericBsdIfconfigNetwork()

# Generated at 2022-06-13 01:35:20.056988
# Unit test for method parse_inet_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet_line():
    """For FreeBSD 6.4"""
   # ifconfig_lines = [
  #      "bge0: flags=8843<UP,BROADCAST,RUNNING,SIMPLEX,MULTICAST> metric 0 mtu 1500",
  #      "        options=9<RXCSUM,VLAN_MTU>",
  #      "        ether 00:1e:37:4c:03:93",
  #      "        inet 192.168.1.66 netmask 0xffffff00 broadcast 192.168.1.255",
  #      "        media: Ethernet autoselect (100baseTX <full-duplex>)",
  #      "        status: active",
 #   ]
   # fact_network = GenericBsdIfconfigNetwork()
  #  fact_network.parse_inet_line(ifconfig_lines

# Generated at 2022-06-13 01:35:29.442608
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():
    class ModuleStub():
        def __init__(self):
            self.params = dict()

        def get_bin_path(self, binary, required=False):
            return 'bin_path_stub'

        def run_command(self, command):
            return (0, 'out', 'err')
    class ModuleUtilsDetectPlatformStub():
        def __init__(self):
            pass

        def get_platform(self):
            return 'platform_stub'

        def get_distribution(self, codename=False):
            return ('distro_stub', 'release_stub', 'codename_stub')

        def get_distribution_codename(self):
            return 'codename_stub'

        def get_distribution_version(self):
            return 'version_stub'
   

# Generated at 2022-06-13 01:35:36.727953
# Unit test for method parse_inet_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet_line():

    # This will not actually be called.
    class FakeAnsibleModule():
        pass

    # Test 1:
    # test = GenericBsdIfconfigNetwork('Non-existant ifconfig path', 'Non-existant route path')
    # Test 2:
    # This results in a failure in parse_options_line
    # test = GenericBsdIfconfigNetwork('/sbin/ifconfig', '/sbin/route')
    # Test 3:
    test = GenericBsdIfconfigNetwork('/usr/sbin/ifconfig', '/usr/sbin/route')

    # Test 3:
    # call the method parse_inet_line
    current_if = {'device': 'lo0', 'ipv4': [], 'ipv6': [], 'type': 'unknown'}

# Generated at 2022-06-13 01:35:45.976687
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_default_interfaces():
    from ansible.utils.network_lsr import GenericBsdIfconfigNetwork
    class NetworkModule(object):
        def get_bin_path(self, arg):
            return '/sbin/ifconfig'

# Generated at 2022-06-13 01:36:17.359296
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():
    obj = GenericBsdIfconfigNetwork()
    obj.merge_default_interface(dict(), dict(), '')
    #assert False # TODO: implement your test here
    #assert isinstance(GenericBsdIfconfigNetwork.merge_default_interface, object)
    return True


# Generated at 2022-06-13 01:36:24.916160
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_default_interfaces():
    module = AnsibleModule(argument_spec={})
    test_class = GenericBsdIfconfigNetwork(module)
    # test for ipv4 routing
    test_class.get_default_interfaces = MagicMock(return_value=({'interface': 'lo0', 'gateway': '127.0.0.1'}, {}))
    (default_ipv4, default_ipv6) = test_class.get_default_interfaces(None)
    assert default_ipv4 == {'interface': 'lo0', 'gateway': '127.0.0.1'}
    assert default_ipv6 == {}
    # test for ipv6 routing

# Generated at 2022-06-13 01:36:33.716321
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_default_interfaces():
    module = AnsibleModule(argument_spec={})
    def mock_run_command(command, check_rc=True):
        for item in ['route.get_default.v4.out',
                     'route.get_default.v4.rc',
                     'route.get_default.v4.err',
                     'route.get_default.v6.out',
                     'route.get_default.v6.rc',
                     'route.get_default.v6.err']:
            if item in os.environ:
                val = os.environ[item]
                if val.isdigit():
                    val = int(val)
                return val, None, None
        raise Exception("this test is not properly configured")

    module.run_command = mock_run_command

# Generated at 2022-06-13 01:36:42.911575
# Unit test for method get_interfaces_info of class GenericBsdIfconfigNetwork

# Generated at 2022-06-13 01:36:50.894220
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():
    from ansible.module_utils.facts.hardware.generic_bsd_ifconfig import GenericBsdIfconfigNetwork
    net = GenericBsdIfconfigNetwork(None)

    # testing if parsing the interface is working properly

# Generated at 2022-06-13 01:37:00.602782
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():
    network_interface = GenericBsdIfconfigNetwork()

    defaults = {'interface': 'lo0'}
    interfaces = {'lo0': {'ipv4': [{'netmask': '255.255.255.255', 'address': '0.0.0.0'}, {'netmask': '255.255.255.255', 'address': '172.16.0.1'}, {'netmask': '255.255.255.255', 'address': '172.16.0.2'}]}}
    network_interface.merge_default_interface(defaults, interfaces, 'ipv4')

    assert 'interface' in defaults
    assert 'netmask' in defaults
    assert defaults['netmask'] == '255.255.255.255'
    assert 'address' in defaults

# Generated at 2022-06-13 01:37:07.642263
# Unit test for method parse_inet_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet_line():
    iface = 'lo0'
    line = 'inet 127.0.0.1 netmask 0xff000000'
    junos_iface = dict()
    junos_iface['device'] = iface
    iface_dict = dict()
    iface_dict['device'] = iface
    iface_dict['ipv4'] = list()
    ips = dict()
    ips['all_ipv4_addresses'] = list()
    junos_iface['type'] = 'unknown'
    GenericBsdIfconfigNetwork().parse_inet_line(line.split(), junos_iface, ips)
    assert junos_iface['type'] != 'unknown'


# Generated at 2022-06-13 01:37:13.526650
# Unit test for method get_interfaces_info of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_interfaces_info():
    # fake output for test case with an empty output
    rc, out, err = 0, '', ''
    assert_equal(GenericBsdIfconfigNetwork().get_interfaces_info('ifconfig', ifconfig_options='-a'), ({},
     {'all_ipv4_addresses': [], 'all_ipv6_addresses': []}))
    rc, out, err = 0, 'lo0: flags=8049<UP,LOOPBACK,RUNNING,MULTICAST> metric 0 mtu 16384', ''