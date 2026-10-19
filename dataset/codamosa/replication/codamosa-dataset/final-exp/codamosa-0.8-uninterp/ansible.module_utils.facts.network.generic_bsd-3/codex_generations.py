

# Generated at 2022-06-13 01:27:54.908303
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():
    network_facts = GenericBsdIfconfigNetwork()

    defaults = {'interface': 'lo0'}
    interfaces = {'lo0': {'device': 'lo0', 'ipv4': [{'address': '127.0.0.1', 'netmask': '255.0.0.0', 'network': '127.0.0.0', 'broadcast': '127.255.255.255'}], 'ipv6': [], 'type': 'loopback', 'flags': ['LOOPBACK', 'UP', 'RUNNING'], 'metric': '0', 'mtu': '16384'}}
    ip_type = 'ipv4'
    assert(network_facts.merge_default_interface(defaults, interfaces, ip_type) == None)

# Generated at 2022-06-13 01:27:58.904160
# Unit test for method get_interfaces_info of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_interfaces_info():
    # No code here - method is not static
    pass

# Generated at 2022-06-13 01:28:05.846612
# Unit test for method parse_inet_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet_line():
    module = AnsibleModule({'param': 'value'})
    mocked_self = Mock()
    mocked_current_if = Mock()
    mocked_ips = Mock()
    mocked_words = Mock()
    mocked_words.__getitem__.return_value = '192.0.2.1'
    mocked_self.get_options.return_value = ['UP', 'LOOPBACK', 'RUNNING', 'MULTICAST']

# Generated at 2022-06-13 01:28:16.852313
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():
    device={"device":"eth0", "type": "ether", "flags": ["BROADCAST", "MULTICAST", "UP", "LOWER_UP"], "mtu": "1500", "macaddress": "00:50:56:00:01:00", "ipv4": [{"address": "10.0.0.141", "netmask": "255.255.255.0", "broadcast": "10.0.0.255", "network": "10.0.0.0"}]}
    devices = {"eth0": device, "lo0": device}

# Generated at 2022-06-13 01:28:17.821846
# Unit test for method parse_media_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_media_line():
   pass


# Generated at 2022-06-13 01:28:24.574074
# Unit test for method populate of class GenericBsdIfconfigNetwork

# Generated at 2022-06-13 01:28:30.188278
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_default_interfaces():
    # This makes sure the code test is executed from the same directory it is located in
    path = os.path.dirname(os.path.realpath(__file__))
    p = os.path.join(path, 'ansible_module_GenericBsdIfconfigNetwork_get_default_interfaces.py')
    exec(compile(open(p, 'rb').read(), p, 'exec'), globals(), locals())
    del os
    del path
    del p
    del compile

# Generated at 2022-06-13 01:28:40.676406
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():
    test_object = GenericBsdIfconfigNetwork

    # Testing expected results
    eth_default_ipv4 = dict(interface='eth0', address='10.0.2.15', netmask='255.255.255.0',
                            network='10.0.2.0', broadcast='10.0.2.255', gateway='10.0.2.2')
    eth_default_ipv6 = dict(interface='eth0', address='fe80::a00:27ff:fea8:8dd4', prefix='64',
                            scope='link', gateway='fe80::a00:27ff:fe00:0')

    # In the ifconfig output below, eth0 has a valid IPv4 gateway, but no IPv6 gateway.  Ensure that
    # the returned IPv4 gateway is from eth0 and the returned IPv6 gateway is empty

# Generated at 2022-06-13 01:28:50.569537
# Unit test for method get_options of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_options():
    gbin = GenericBsdIfconfigNetwork()

    # test option string with single option
    options = gbin.get_options("<UP,LOOPBACK>")
    assert options == ['UP', 'LOOPBACK']

    # test option string with single option that contains a comma
    options = gbin.get_options("<UP,LOOPBACK,WITH,COMMA>")
    assert options == ['UP', 'LOOPBACK', 'WITH', 'COMMA']

    # test option string where options are not within the <>
    options = gbin.get_options("UP,LOOPBACK")
    assert options == []


# Generated at 2022-06-13 01:28:59.507806
# Unit test for method parse_media_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_media_line():

    # given
    line = 'media: Ethernet autoselect (100baseTX <full-duplex,flow-control>) status: active'
    words = line.split()
    current_if = {}
    ips = {}

    # when
    GenericBsdIfconfigNetwork.parse_media_line(words, current_if, ips)

    # then
    expected = {'media': words[1], 'media_select': words[2], 'media_type': words[3][1:], 'media_options': words[4].split(',')}

    for item in expected:
        if expected[item] != current_if[item]:
            print("Expected: %s: %s" % (item, expected[item]), file=sys.stderr)

# Generated at 2022-06-13 01:29:08.107392
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():
    assert True == True


# Generated at 2022-06-13 01:29:17.396995
# Unit test for method detect_type_media of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_detect_type_media():
    gn = GenericBsdIfconfigNetwork()
    interfaces = { 'interface_a': { 'ipv4': [], 'ipv6': [], 'type': 'unknown' },
                   'interface_b': { 'ipv4': [], 'ipv6': [], 'type': 'unknown', 'media': 'Ethernet' },
                   'interface_c': { 'ipv4': [], 'ipv6': [], 'type': 'unknown', 'media': 'Ethernet autoselect HOST-UNKNOWN' }
                 }
    result = gn.detect_type_media(interfaces)
    assert 'interface_a' in result
    assert result['interface_a']['type'] == 'unknown'
    assert 'interface_b' in result
    assert result['interface_b']['type'] == 'ether'
   

# Generated at 2022-06-13 01:29:28.063631
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_default_interfaces():
    module = ansible_module_mock()
    network = GenericBsdIfconfigNetwork(module)

    mock_open = mock.mock_open()

    route_path = '/sbin/route'

# Generated at 2022-06-13 01:29:29.756792
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():
    # This method is not directly testable.
    pass


# Generated at 2022-06-13 01:29:36.058336
# Unit test for method parse_interface_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_interface_line():
    parsed = _GenericBsdIfconfigNetwork.parse_interface_line(['lo0:', 'flags=8049<UP,LOOPBACK,RUNNING,MULTICAST>', 'metric', '0', 'mtu', '33184'])
    assert parsed['device'] == 'lo0'
    assert parsed['flags'] == ['UP', 'LOOPBACK', 'RUNNING', 'MULTICAST']
    assert parsed['macaddress'] == 'unknown'
    assert parsed['mtu'] == '33184'
    assert parsed['metric'] == '0'
    assert parsed['type'] == 'loopback'

# Generated at 2022-06-13 01:29:48.327310
# Unit test for method get_interfaces_info of class GenericBsdIfconfigNetwork

# Generated at 2022-06-13 01:29:55.255588
# Unit test for method get_options of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_options():
    network = GenericBsdIfconfigNetwork()
    
    # Test 1
    option_string = "UHLWIir"
    return_value = network.get_options(option_string)
    assert return_value == ['U', 'H', 'L', 'W', 'I', 'i', 'r']

    # Test 2
    option_string = "UHLWIirfoobar"
    return_value = network.get_options(option_string)
    assert return_value == ['U', 'H', 'L', 'W', 'I', 'i', 'r']

    # Test 3
    option_string = "UHLWIir_foobar"
    return_value = network.get_options(option_string)

# Generated at 2022-06-13 01:29:55.955468
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():
    pass

# Generated at 2022-06-13 01:30:05.878334
# Unit test for method parse_media_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_media_line():
    module = MagicMock()
    ansible_module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )
    iface = dict(
        device='identifier',
        ipv4=[],
        ipv6=[],
        type='unknown',
        flags=[],
        macaddress='unknown',
        mtu=65000,
        metric=0,
        options=[],
        media='100baseTX',
        media_select='autoselect',
        media_type='media',
        media_options=['mediaopt', 'mediaoptions'],
        status='none'
    )
    media_line_input = 'media: 100baseTX autoselect media mediaopt mediaoptions'
    media_line = media_line_input.split()
    network = GenericBsdIfconfig

# Generated at 2022-06-13 01:30:12.699306
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_default_interfaces():
    """Test method get_default_interfaces of class GenericBsdIfconfigNetwork"""
    print("\n### Test method get_default_interfaces of class "
          "GenericBsdIfconfigNetwork ###")
    module = AnsibleModule({})
    bsd_network = GenericBsdIfconfigNetwork(module)
    assert len(bsd_network.get_default_interfaces('./test/route')) == 2


# Generated at 2022-06-13 01:30:28.571312
# Unit test for method get_options of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_options():
    module = AnsibleModule(argument_spec={})
    module.exit_json = exit_json
    module.fail_json = fail_json
    m_args = Mock(spec_set=dict)
    m_args.return_value = (0, '/usr/bin/ifconfig', '')
    m_ifconfig = Mock(spec_set=dict)

# Generated at 2022-06-13 01:30:34.210367
# Unit test for method get_options of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_options():
    opt_string = '<UP,BROADCAST,LOOPBACK,MULTICAST>'
    options = GenericBsdIfconfigNetwork.get_options(opt_string)
    assert(options == ['UP', 'BROADCAST', 'LOOPBACK', 'MULTICAST'])

    opt_string = '<UP,LOWER_UP>'
    options = GenericBsdIfconfigNetwork.get_options(opt_string)
    assert(options == ['UP', 'LOWER_UP'])


# Generated at 2022-06-13 01:30:42.037259
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():
    facts = dict()
    facts['ansible_os_family'] = 'Generic'
    facts['ansible_distribution'] = 'BSD'
    network = GenericBsdIfconfigNetwork(dict(module=AnsibleModule(argument_spec=dict()), ansible_facts=facts))
    network.get_default_interfaces = Mock()
    network.get_interfaces_info = Mock()
    network.parse_interface_line = Mock()
    network.parse_options_line = Mock()
    network.parse_nd6_line = Mock()
    network.parse_ether_line = Mock()
    network.parse_media_line = Mock()
    network.parse_status_line = Mock()
    network.parse_lladdr_line = Mock()
    network.parse_inet_line = Mock()
    network.parse_inet

# Generated at 2022-06-13 01:30:45.144274
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():
    os.environ['PATH'] = get_bin_path()
    obj = GenericBsdIfconfigNetwork()
    network_facts = obj.populate()
    assert network_facts


# Generated at 2022-06-13 01:30:56.101302
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():
    the_module = GenericBsdIfconfigNetwork()
    defaults = { 'interface': 'lo0',
                 'address': '::1',
                 'ipv4': [],
                 'ipv6': [] }

# Generated at 2022-06-13 01:31:01.312150
# Unit test for method parse_media_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_media_line():
    network = GenericBsdIfconfigNetwork()
    current_if = {}
    network.parse_media_line(['media:', 'Ethernet', 'autoselect', '(none)'], current_if, {})
    assert current_if['media'] == 'Ethernet'
    assert current_if['media_select'] == 'autoselect'
    assert current_if['media_type'] == '(none)'
    assert current_if['media_options'] == []



# Generated at 2022-06-13 01:31:12.412776
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():
    facts = GenericBsdIfconfigNetwork()
    default_ipv4 = {'interface': 'bond0.20', 'address': '192.168.112.110'}
    interfaces = {'bond0.20': {'gateway': '192.168.112.1', 'device': 'bond0.20',
                  'metric': '50', 'ipv4': [{'netmask': '255.255.255.0',
                  'network': '192.168.112.0', 'address': '192.168.112.110',
                  'broadcast': '192.168.112.255'}], 'mtu': '1500',
                  'flags': ['BROADCAST', 'MULTICAST', 'UP', 'MASTER', 'RUNNING']}}
    ip_type = 'ipv4'

   

# Generated at 2022-06-13 01:31:23.240186
# Unit test for method parse_inet6_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet6_line():
    network = GenericBsdIfconfigNetwork(module)

    # Test IPv6 address without scope
    words = ['inet6', '2a02:898:16:8000::1/64', 'prefixlen', '64', 'inet6', 'fe80::1%lo0', 'prefixlen', '64', 'scopeid', '0x1', 'inet6', 'fe80::%en0', 'prefixlen', '64', 'scopeid', '0x5']
    current_if = {'ipv6': []}

    network.parse_inet6_line(words, current_if, {})

    assert len(current_if['ipv6']) == 1
    assert current_if['ipv6'][0]['address'] == '2a02:898:16:8000::1'

# Generated at 2022-06-13 01:31:30.420383
# Unit test for method parse_inet_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet_line():

    # read in the module code
    import inspect
    import sys
    import imp

    global_ns = {}
    local_ns = {}

    file_path = os.path.dirname(os.path.abspath(__file__)) + '/../../../lib/ansible/module_utils/facts/network/generic_bsd.py'

    module_code = inspect.getsource(imp.load_source('ifconfig', file_path))

    # Some older versions of python dont have compileflags set (pre 2.6)
    compileflags = getattr(sys, 'compileflags', None)

    exec(module_code, global_ns, local_ns)

    # create the object
    obj = local_ns['GenericBsdIfconfigNetwork']()

    # Get the datastructure we want to test

# Generated at 2022-06-13 01:31:41.921681
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_default_interfaces():
    module = AnsibleModule({})
    platform = 'Generic_BSD_Ifconfig'
    network = GenericBsdIfconfigNetwork(module)
    # mock route command outputs
    out_inet_default = b'interface: en0\ngateway: 192.168.1.1\nflags: <UP,GATEWAY,HOST,DONE,STATIC,PRCLONING>\nrecvpipe  sendpipe  ssthresh  rtt,msec    mtu    weight    expire\n0         0         0         0           1500   0         0\nunreach\n   0\n'

# Generated at 2022-06-13 01:32:07.975305
# Unit test for method get_interfaces_info of class GenericBsdIfconfigNetwork

# Generated at 2022-06-13 01:32:17.296897
# Unit test for method parse_interface_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_interface_line():
    # prepare test data
    line_1 = "em0: flags=8843<UP,BROADCAST,RUNNING,SIMPLEX,MULTICAST> mtu 1500\n"
    lines_2 = ["elan: flags=8049<UP,LOOPBACK,RUNNING,MULTICAST> metric 0 mtu 2136\n",
               "me0: flags=8802<BROADCAST,SIMPLEX,MULTICAST> metric 0 mtu 1500\n"]

    # test data for FreeBSD >= 8.0
    line_8 = "bge0: flags=8843<UP,BROADCAST,RUNNING,SIMPLEX,MULTICAST> metric 0 mtu 1500\n"

# Generated at 2022-06-13 01:32:25.121142
# Unit test for method parse_interface_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_interface_line():
    test_inst = GenericBsdIfconfigNetwork()
    words = ['ix0:', 'flags=8843<UP,BROADCAST,RUNNING,SIMPLEX,MULTICAST>', 'metric', '0', 'mtu', '1500', 'ether',
             'xx:xx:xx:xx:xx:xx', 'inet', '10.68.0.1', 'netmask', '0xffffffc0', 'broadcast', '10.68.0.1']

# Generated at 2022-06-13 01:32:32.486363
# Unit test for method parse_interface_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_interface_line():
    ifc = GenericBsdIfconfigNetwork()
    words = ['lo0:', 'flags=8049<UP,LOOPBACK,RUNNING,MULTICAST>', 'metric', '0', 'mtu', '16384']
    intf = ifc.parse_interface_line(words)
    assert intf['device'] == 'lo0'
    assert intf['flags'] == ['UP', 'LOOPBACK', 'RUNNING', 'MULTICAST']
    assert intf['metric'] == '0'
    assert intf['mtu'] == '16384'


# Generated at 2022-06-13 01:32:41.027459
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_default_interfaces():
    """Test method get_default_interfaces for class GenericBsdIfconfigNetwork."""
    facts = GenericBsdIfconfigNetwork()
    # Test with good input
    route_path = '/sbin/route'
    rc = None
    out = r'''add net default: gateway localhost
    interface: en0
    flags: <UP,GATEWAY,DONE,STATIC,PRCLONING>
    recvpipe  sendpipe  ssthresh  rtt,msec    rttvar  hopcount      mtu     expire
    0         0         0         0           0       0             1500    0
    '''
    err = ''
    result = dict(v4=dict(gateway='localhost', interface='en0'), v6=dict())

# Generated at 2022-06-13 01:32:49.498179
# Unit test for method parse_inet6_line of class GenericBsdIfconfigNetwork

# Generated at 2022-06-13 01:32:56.114679
# Unit test for method parse_inet6_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet6_line():
    network = GenericBsdIfconfigNetwork()

    # normal case
    words = 'inet6 ::1 prefixlen 128'.split()
    current_if = {'ipv6': []}
    ips = dict(all_ipv6_addresses=[])
    network.parse_inet6_line(words, current_if, ips)
    assert current_if == {'ipv6': [{'address': '::1', 'prefix': '128'}]}
    assert ips == dict(all_ipv6_addresses=["::1"])

    # cidr case
    words = 'inet6 ::1/128 scopeid 0x8'.split()
    current_if = {'ipv6': []}
    ips = dict(all_ipv6_addresses=[])
    network.parse_inet6_

# Generated at 2022-06-13 01:32:59.665858
# Unit test for method get_options of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_options():
    obj = GenericBsdIfconfigNetwork()
    assert obj.get_options('UP') == ['UP']
    assert obj.get_options('UP,LOOPBACK') == ['UP', 'LOOPBACK']
    assert obj.get_options('UP,LOOPBACK,RUNNING') == ['UP', 'LOOPBACK', 'RUNNING']

# Generated at 2022-06-13 01:33:11.901872
# Unit test for method parse_inet_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet_line():
    net = GenericBsdIfconfigNetwork()
    iface = {}
    ips = {}

    # Basic case of ipv4 address
    words = ['internet0', 'inet', '192.168.1.1', 'netmask', '0xffffff00']
    net.parse_inet_line(words, iface, ips)
    assert iface['ipv4'][0]['address'] == '192.168.1.1'
    assert iface['ipv4'][0]['netmask'] == '255.255.255.0'
    assert iface['ipv4'][0]['network'] == '192.168.1.0'
    assert iface['ipv4'][0]['broadcast'] == '192.168.1.255'

    # Case of ipv4 address with extra column

# Generated at 2022-06-13 01:33:23.485107
# Unit test for method parse_inet_line of class GenericBsdIfconfigNetwork

# Generated at 2022-06-13 01:34:21.154111
# Unit test for method get_interfaces_info of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_interfaces_info():
    obj = GenericBsdIfconfigNetwork()

    rc, out, err = obj.module.run_command("ifconfig -a")

    interfaces, ips = obj.get_interfaces_info("ifconfig")


# Generated at 2022-06-13 01:34:30.215089
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():
    # Setup as if run in networking/get_facts.py
    facts_module = AnsibleModule(
        argument_spec=dict(
            gather_subset=dict(default=['!all'], type='list')
        ),
        supports_check_mode=True)
    network = GenericBsdIfconfigNetwork(facts_module)
    # Test defaults dict with 'interface' key
    defaults = dict(interface='lo0')
    # Test interfaces dict with 'lo0' and 'lo1' interfaces
    interfaces = dict(lo0=dict(ipv4=[], ipv6=[], type='loopback'), lo1=dict(ipv4=[], ipv6=[]))
    # Test interfaces['lo0'] dict with 'ipv4' and 'ipv6' keys

# Generated at 2022-06-13 01:34:38.075722
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():
    import sys
    sys.path.append('../../')
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(
        argument_spec = dict(),
        supports_check_mode = True
    )

    test = GenericBsdIfconfigNetwork(module)
    network_facts = test.populate()
    print(network_facts)

if __name__ == "__main__":
    test_GenericBsdIfconfigNetwork_populate()

# Generated at 2022-06-13 01:34:45.699990
# Unit test for method populate of class GenericBsdIfconfigNetwork

# Generated at 2022-06-13 01:34:54.456892
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_default_interfaces():
    from ansible_collections.ansible.netcommon.tests.unit.compat.mock import Mock
    from ansible_collections.ansible.netcommon.tests.unit.compat.mock import patch

    module = Mock()
    module.run_command.return_value = (0, """
add net default: gateway 192.168.1.1
add net default: gateway 192.168.1.1
""", "")
    module.get_bin_path.return_value = 'route'
    net = GenericBsdIfconfigNetwork(module)

    default_ipv4, default_ipv6 = net.get_default_interfaces('route')
    assert default_ipv4['gateway'] == '192.168.1.1'
    assert default_ipv4['interface'] == 'net'


#

# Generated at 2022-06-13 01:35:05.077301
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():
    print('Testing merge_default_interface() of class GenericBsdIfconfigNetwork')
    defaults = {
        'interface': 'lo0',
        'address': '::1'
    }
    interfaces = {
        'lo0': {
            'ipv4': [{'address': '127.0.0.1'}],
            'ipv6': [{'address': '::1'}]
        }
    }
    expected_ip_type = 'ipv6'
    expected_defaults = {
        'interface': 'lo0',
        'address': '::1',
        'ipv4': [{'address': '127.0.0.1'}],
        'ipv6': [{'address': '::1'}]
    }


# Generated at 2022-06-13 01:35:10.975264
# Unit test for method get_options of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_options():
    network_config = GenericBsdIfconfigNetwork()

    # test 1
    assert network_config.get_options('foo<bar,baz>') == ['bar', 'baz']
    # test 2
    assert network_config.get_options('foo<bar>') == ['bar']
    # test 3
    assert network_config.get_options('foo<>') == []
    # test 4
    assert network_config.get_options('foo') == []



# Generated at 2022-06-13 01:35:18.537711
# Unit test for method parse_inet_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet_line():
    '''
    Test that parse_inet_line collects the correct addresses
    '''
    from ..plugins.module_utils.network.linux.facts import LinuxNetworkFacts
    iface = dict()
    common = dict()
    network = LinuxNetworkFacts(dict(), dict())
    # create a list of tests and expected answers
    tests = list()
    tests.append(('inet 127.0.0.1 netmask 0xff000000  broadcast 127.255.255.255', '127.0.0.1'))
    tests.append(('inet6 fe80::1%lo0 prefixlen 64  scopeid 0x2  ', 'fe80::1'))

# Generated at 2022-06-13 01:35:28.079895
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():
    # create the class
    network_fact_class = GenericBsdIfconfigNetwork()

    # create an input dictionary
    defaults = {'interface': 'lo0'}

# Generated at 2022-06-13 01:35:35.546167
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():
    module = AnsibleModule(
        argument_spec = dict(),
        supports_check_mode = True
    )

    ifconfig_path = module.get_bin_path('ifconfig')
    route_path = module.get_bin_path('route')

    if ifconfig_path is None:
        module.exit_json(changed=False, ansible_facts={}, skipped=True)

    if route_path is None:
        module.exit_json(changed=False, ansible_facts={}, skipped=True)

    n = GenericBsdIfconfigNetwork(module)
    network_facts = n.populate()

    if network_facts['default_ipv4']['interface'] is None:
        network_facts['default_ipv4'] = {}
