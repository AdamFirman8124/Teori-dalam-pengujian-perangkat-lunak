

# Generated at 2022-06-13 01:27:54.546549
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():
    # Method populate of class GenericBsdIfconfigNetwork with arguments:
    #   collected_facts: {}
    # 
    # Returned value is:
    #   {}

    network = GenericBsdIfconfigNetwork()

# Generated at 2022-06-13 01:28:07.838334
# Unit test for method parse_inet_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet_line():
    module = AnsibleModule(argument_spec={})
    module.check_mode = False
    res = {}
    res['ansible_facts'] = {}

    # Testing IPv4 cidr style address
    words = ['lo0', 'flags=8049<UP,LOOPBACK,RUNNING,MULTICAST>', 'mtu', '33184', 'inet', '127.0.0.1/24', 'netmask', '0xffffff00', 'inet6', '::1/128', 'inet6', 'fe80::1%lo0', 'prefixlen', '64', 'scopeid', '0x1']
    current_if = {"device": 'lo0', 'ipv4': [], 'ipv6': [], 'type': 'unknown'}

# Generated at 2022-06-13 01:28:18.652704
# Unit test for method parse_media_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_media_line():
    from ansible.module_utils.network.common.utils import dict_merge

    nm = GenericBsdIfconfigNetwork()
    current_if = dict()
    ips = dict()

    current_if = dict()
    ips = dict()
    words = ['media:', 'Ethernet', 'autoselect', '(1000baseT)]']
    nm.parse_media_line(words, current_if, ips)
    assert words[0] == 'media:'
    assert words[1] == 'Ethernet'
    assert words[2] == 'autoselect'
    assert words[3] == '(1000baseT)]'
    assert 'media' in current_if
    assert 'media_select' in current_if
    assert 'media_type' in current_if
    assert not 'media_options' in current

# Generated at 2022-06-13 01:28:25.499439
# Unit test for method get_interfaces_info of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_interfaces_info():
    # Looks like modules are not loaded during unit tests
    from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.netlink.generic_bsd import GenericBsdIfconfigNetwork
    # Create a mock of the module class
    module = mock.MagicMock()
    # Create a mock of the params
    params = mock.MagicMock()
    # Create a mock of the run_command
    module.run_command = mock.MagicMock()
    # Create a mock of the return code
    rc = mock.MagicMock()
    rc.return_value = 0
    # Create a mock of the subprocess.Popen class
    proc = mock.MagicMock()
    # Create a mock of the read program stdout
    stdout = mock.MagicMock()

# Generated at 2022-06-13 01:28:34.370144
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():
    module = MagicMock()
    method = GenericBsdIfconfigNetwork(module)

    defaults = {
        'interface': 'em0',
        'address': '192.168.1.1'
    }


# Generated at 2022-06-13 01:28:46.894835
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():
    gbi = GenericBsdIfconfigNetwork()

    interface_info = {
        'eth0': {'ipv4': [{'address': '192.168.1.1'}], 'ipv6': [{'address': '1::1'}]},
        'eth1': {'ipv4': [{'address': '192.168.1.2'}], 'ipv6': [{'address': '2::2'}]},
        'eth2': {'ipv4': [{'address': '192.168.1.3'}], 'ipv6': [{'address': '3::3'}]},
    }
    default_ipv4 = {
        'interface': 'eth1',
        'address': '192.168.1.2',
    }
    default_ip

# Generated at 2022-06-13 01:28:57.322086
# Unit test for method get_interfaces_info of class GenericBsdIfconfigNetwork

# Generated at 2022-06-13 01:29:08.108506
# Unit test for method parse_inet6_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet6_line():
    network = GenericBsdIfconfigNetwork()
    words = ['inet6', 'fe80::1%lo0', 'prefixlen', '64', 'scopeid', '0x2']
    current_if = {'device': 'lo0', 'ipv4': [], 'ipv6': [], 'type': 'unknown', 'flags': ['UP', 'LOOPBACK', 'RUNNING', 'MULTICAST'], 'macaddress': 'unknown', 'metric': '0', 'mtu': '33184'}
    ips = dict(
        all_ipv4_addresses=[],
        all_ipv6_addresses=[],
    )
    assert(network.parse_inet6_line(words, current_if, ips) == None)

# Generated at 2022-06-13 01:29:17.406105
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():

    import socket,struct

    class ModuleStub(object):

        class FakeAnsibleModule():

            def __init__(self):

                self.params = []

            def fail_json(self, **args):

                print(args)
                sys.exit(1)

        def __init__(self):

            self.module = self.FakeAnsibleModule()
            self.run_command = self.fake_run_command

        def fake_run_command(self, args, check_rc=True):
            
            if args[0] == 'ifconfig':
                self.stdout = fake_if_config
                self.stderr = ''
                self.rc = 0
            elif args[0] == 'route':
                self.stdout = fake_route_output
                self.stderr = ''
               

# Generated at 2022-06-13 01:29:28.063275
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_default_interfaces():
    # Arrange
    module = AnsibleModule(argument_spec={})
    network = GenericBsdIfconfigNetwork(module)


# Generated at 2022-06-13 01:29:44.429320
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():
    print('populate')

    # Test with the test platform's own data.

# Generated at 2022-06-13 01:29:49.333900
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork

# Generated at 2022-06-13 01:29:54.675552
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():
    generic_bsd_ifconfig_network = GenericBsdIfconfigNetwork()
    defaults = dict()
    interfaces = dict()
    ip_type = dict()
    assert generic_bsd_ifconfig_network.merge_default_interface(defaults, interfaces, ip_type) == None


# Generated at 2022-06-13 01:30:00.070112
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():
  module = AnsibleModule(argument_spec=dict())
  network = GenericBsdIfconfigNetwork(module)
  result = network.populate()
  assert result.pop('default_ipv4').pop('interface') == 'lo0'
  assert result.pop('default_ipv6').pop('interface') == 'lo0'
  assert result.pop('interfaces') == ['gif0', 'lo0', 'stf0', 'en0']
  assert result.pop('all_ipv4_addresses') == ['127.0.0.1']
  assert result.pop('all_ipv6_addresses') == ['fe80::1%lo0', '::1']
  assert result.pop('en0').pop('ipv4') == []
  assert result.pop('en0').pop('ipv6') == []

# Generated at 2022-06-13 01:30:08.748727
# Unit test for method parse_inet_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet_line():

    class FakeModule(object):
        def __init__(self, out, err=None):
            self.out = out
            self.err = err
            self.run_command_called_count = 0
            self.run_command_args = None
            self.run_command_kwargs = None

        def run_command(self, args, check_rc=False):
            self.run_command_called_count += 1
            self.run_command_args = args
            self.run_command_kwargs = {'check_rc': check_rc}
            return 0, self.out, self.err

    def run_parse_inet_line(data, ipv4_address, netmask, broadcast, network):
        ifconfig_path = '/sbin/ifconfig'

        module = FakeModule(data)


# Generated at 2022-06-13 01:30:19.349772
# Unit test for method detect_type_media of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_detect_type_media():
    n = GenericBsdIfconfigNetwork()
    i1 = {'media': 'Ethernet autoselect (10GbaseT <full-duplex>)', 'type': 'unknown'}
    i2 = {'media': 'Ethernet autoselect (10GbaseT <full-duplex>)', 'type': 'ether'}
    i3 = {'media': 'Ethernet', 'type': 'unknown'}
    i4 = {'media': 'none', 'type': 'unknown'}
    i5 = {'media': 'Ethernet/Ethernet 10GbaseT', 'type': 'unknown'}
    i6 = {'media': 'Ethernet/Ethernet 10GbaseT', 'type': 'ether'}

# Generated at 2022-06-13 01:30:27.395725
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():
    def_v4 = {'interface' : 'em0'}
    def_v6 = {'interface' : 'em0'}

# Generated at 2022-06-13 01:30:33.816139
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():
    host = GenericBsdIfconfigNetwork()
    host.module  = AnsibleModule(
        argument_spec = dict(),
        supports_check_mode = True
    )

    host.module.run_command = MagicMock(return_value=(1, '', '')) 
    result = host.populate()
    assert result == {}

    host.module.run_command = MagicMock(return_value=(0, '', '')) 
    result = host.populate()
    assert result == {}

    host.module.run_command = MagicMock(side_effect=OSError)
    result = host.populate()
    assert result == {}

    host.module.run_command = MagicMock(return_value=(0, '', '')) 

# Generated at 2022-06-13 01:30:41.436337
# Unit test for method parse_inet_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet_line():
    ifconfig = GenericBsdIfconfigNetwork()
    words = ['en0:', 'flags=8088<POINTOPOINT,SIMPLEX,MULTICAST>', 'mtu', '1500',
             'inet', '192.168.1.1', 'netmask', '0xffffff00', 'destination', '192.168.1.2']

    current_if = ifconfig.parse_interface_line(words)
    ips = {}
    ifconfig.parse_inet_line(words, current_if, ips)

    assert ips['all_ipv4_addresses'] == ['192.168.1.1']
    assert ifconfig.get_options(words[1]) == ['POINTOPOINT', 'SIMPLEX', 'MULTICAST']



# Generated at 2022-06-13 01:30:50.025768
# Unit test for method parse_inet6_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet6_line():
    module = AnsibleModuleMock()
    net = GenericBsdIfconfigNetwork(module)
    current_if = {'ipv6': []}
    ips = dict(all_ipv6_addresses=[])
    iface = 'fxp0'
    scope = 'link'
    prefix = '64'
    address = 'fe80::8c44:f3ff:feb6:af7b%s' % iface
    net.parse_inet6_line([address, 'prefixlen', prefix, 'scopeid', scope], current_if, ips)
    assert len(current_if['ipv6']) == 1
    assert current_if['ipv6'][0]['address'] == address
    assert current_if['ipv6'][0]['prefix'] == prefix

# Generated at 2022-06-13 01:31:04.889264
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():
    # Define a test iface 
    test_iface = {'em1':{'type':'ether', 'metric':'100', 'mtu':'1500'}}
    # Define default interface info 
    default_interface = {'interface':'em1', 'gateway':'10.10.10.1', 'address':'10.10.10.11'}
    # Define ipv4 address for test interface 
    ipv4_info = {'address':'10.10.10.11', 'netmask':'255.255.0.0', 'network':'10.10.0.0', 'broadcast':'10.10.255.255'}
    # Define ipv6 address for test interface 

# Generated at 2022-06-13 01:31:14.690715
# Unit test for method parse_inet_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet_line():
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )
    ifcfg = GenericBsdIfconfigNetwork(module)

# Generated at 2022-06-13 01:31:24.855902
# Unit test for method parse_inet6_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet6_line():
    ansible_module_args = dict(
        config='/tmp/ansible_test_config.cfg',
        debug=dict(
            msg='{{inventory_hostname}} >> this is a debug message',
            verbosity=4,
        ),
    )
    ansible_module = AnsibleModule(
        argument_spec=ansible_module_args,
        supports_check_mode=False,
    )
    module = GenericBsdIfconfigNetwork(ansible_module)

    words = ["fe80::250:56ff:fe85:a2e7%br0", "prefixlen", "64", "scopeid", "0x1", "ether", "00:50:56:85:a2:e7"]

# Generated at 2022-06-13 01:31:30.878927
# Unit test for method parse_inet_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet_line():
    module = AnsibleModule(argument_spec={})
    module.get_bin_path = lambda x: x
    network = GenericBsdIfconfigNetwork()
    network.module = module

    # test case 1 - netbsd show addresses like this
    #  lo0: flags=8049<UP,LOOPBACK,RUNNING,MULTICAST> mtu 33184
    #         inet 127.0.0.1 netmask 0xff000000
    test_case_values = ["lo0", "inet", "127.0.0.1", "netmask", "0xff000000"]

# Generated at 2022-06-13 01:31:42.280044
# Unit test for method parse_media_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_media_line():
 
    # Set up mock input
    words = [
        'media:',
        'Ethernet',
        '10Gbase-R',
        '<full-duplex>',
        '(txpause)',
        'mediaopt',
        'mediaoptions',
    ]
    current_if = {}
    ips = {}
 
    # Invoke method
    obj = GenericBsdIfconfigNetwork()
    obj.parse_media_line(words, current_if, ips)
 
    # Verify results
    assert current_if['media'] == 'Ethernet'
    assert current_if['media_select'] == '10Gbase-R'
    assert current_if['media_type'] == 'full-duplex'

# Generated at 2022-06-13 01:31:49.424650
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():
    module = AnsibleModule(argument_spec={})

    defaults = {'interface': 'lo0'}
    interfaces = {'re0': {'mtu': '1500'}}

    generic_bsd_ifconfig_network = GenericBsdIfconfigNetwork(module)
    generic_bsd_ifconfig_network.merge_default_interface(defaults, interfaces, 'ipv4')

    assert defaults['mtu'] == '1500'


# Generated at 2022-06-13 01:31:52.745896
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_default_interfaces():
    platform = 'Generic_BSD_Ifconfig'
    module = MockModule(platform=platform)
    network = GenericBsdIfconfigNetwork(module=module)

    network.get_default_interfaces(route_path='route')



# Generated at 2022-06-13 01:31:55.641009
# Unit test for method get_options of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_options():
    mock_class = GenericBsdIfconfigNetwork(dict(bin_dir='/bin'))
    result=mock_class.get_options("<LOOPBACK,UP,LOWER_UP>")
    assert result[0] == "LOOPBACK"
    assert result[1] == "UP"
    assert result[2] == "LOWER_UP"


# Generated at 2022-06-13 01:32:07.335859
# Unit test for method get_interfaces_info of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_interfaces_info():
    platform = 'Generic_BSD_Ifconfig'
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )
    mock_ifconfig_path = os.path.join(os.path.dirname(__file__), 'mock-ifconfig')
    network = GenericBsdIfconfigNetwork(module)
    interfaces, ips = network.get_interfaces_info(mock_ifconfig_path)
    # print(interfaces)
    # print(ips)
    assert len(interfaces) == 3
    assert interfaces['lo0']
    assert interfaces['lo0']['device'] == 'lo0'
    assert interfaces['lo0']['type'] == 'loopback'
    assert interfaces['re0']

# Generated at 2022-06-13 01:32:16.735258
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():
    # Initial test of populate method
    p = platform.system()

    if p == 'FreeBSD':
        module = AnsibleModule(argument_spec={})

        if not module.get_bin_path('ifconfig'):
            module.fail_json(msg="'ifconfig' command not found")

        if not module.get_bin_path('route'):
            module.fail_json(msg="'route' command not found")
        # FreeBSD ifconfig output
        module.run_command = MagicMock(return_value=(0, freebsd_ifconfig, ''))
        ifconfig = GenericBsdIfconfigNetwork(module)
        print(ifconfig.populate())
    if p == 'OpenBSD':
        module = AnsibleModule(argument_spec={})


# Generated at 2022-06-13 01:32:34.789861
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():

    # Test input parameters
    defaults = dict(interface='en0', address='192.168.1.12')
    interfaces = dict(en0=dict(device='en0', ipv4=[{'address': '192.168.1.12', 'netmask': '255.255.255.0'}]))

    # Call method
    module = AnsibleModule(argument_spec=dict())
    cls = GenericBsdIfconfigNetwork(module=module)
    cls.merge_default_interface(defaults, interfaces, 'ipv4')

    # Assert
    assert 'address' in defaults, "defaults has no key address"
    assert 'netmask' in defaults, "defaults has no key netmask"
    assert defaults['address'] == '192.168.1.12', "invalid value for address"
   

# Generated at 2022-06-13 01:32:42.648720
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_default_interfaces():
    # Initialize the module class
    generic_module = GenericBsdIfconfigNetwork()

    # Set up the argument spec
    options = dict(
        root_dir=dict(default='/', type='str'),
        all_devices=dict(default=False, type='bool'),
        arp=dict(default=False, type='bool'),
        device_links=dict(default=False, type='bool'),
        show_duplicates=dict(default=False, type='bool'),
        include_loopback=dict(default=True, type='bool'),
        include_wireless=dict(default=False, type='bool'),
        interfaces=dict(default='', type='str'),
        no_aliases=dict(default=False, type='bool'),
        aliases=dict(default=0, type='int'),
    )

    #

# Generated at 2022-06-13 01:32:50.596053
# Unit test for method parse_inet6_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet6_line():
    # current_if = {}
    # ips = dict(all_ipv6_addresses=[])
    # words = ['inet6', 'fe80::1%lo0', 'prefixlen', '64', 'scopeid', '0x2', '(localnet)']

    current_if = {}
    ips = dict(all_ipv6_addresses=[])
    words = ['inet6', 'fe80::1%lo1', 'prefixlen', '64', 'scopeid', '0x3', '(localnet)']

    mod_name = 'unit_tests.plugins.network.test_generic_bsd_ifconfig'
    module = importlib.import_module(mod_name)
    instance = module.GenericBsdIfconfigNetwork(module)


# Generated at 2022-06-13 01:32:57.336660
# Unit test for method get_interfaces_info of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_interfaces_info():
    module = AnsibleModule({})
    g = GenericBsdIfconfigNetwork(module)


# Generated at 2022-06-13 01:33:04.068382
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():
    # set up the ifconfig and routing commands
    ifconfig_path = '/usr/sbin/ifconfig'
    route_path = '/sbin/route'
    # set up the return data for the ifconfig command in this case
    # just the interface
    ifconfig_lines = [
        'lo0: flags=8049<UP,LOOPBACK,RUNNING,MULTICAST> metric 0 mtu 16384\n'
    ]
    ifconfig_resp = (0, ''.join(ifconfig_lines), '')
    # set up the return data for the route command in this case
    # just the interface and the address

# Generated at 2022-06-13 01:33:13.115859
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():
    mock_module = type('AnsibleModule', (), {})()
    mock_module.get_bin_path = mock.MagicMock(return_value="/usr/sbin/ifconfig")
    expected_default_ipv4 = {'interface': 'en0', 'type': 'ether', 'mtu': '1500',
                             'flags': ['BROADCAST', 'SMART', 'UP', 'RUNNING', 'SIMPLEX', 'MULTICAST'],
                             'device': 'en0', 'address': '192.168.1.167'}
    network_facts = GenericBsdIfconfigNetwork(mock_module).populate()

    assert network_facts['default_ipv4'] == expected_default_ipv4

 

# Generated at 2022-06-13 01:33:19.227063
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():
    n = GenericBsdIfconfigNetwork()
    default_ipv4 = {
        'interface': 'vtnet0',
        'address': '10.0.0.1'
    }

# Generated at 2022-06-13 01:33:31.045285
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_default_interfaces():
    class MockModule(object):
        def get_bin_path(self, arg):
            return "/usr/local/bin/route"

        def run_command(self, arg):
            return (0, "default: interface: en0 destination: default gateway: 10.0.0.1 flags: <UP,GATEWAY,DONE,STATIC,PRCLONING> recvpipe  sendpipe  ssthresh  rtt,msec    rttvar  hopcount      mtu     expire", "")

    module = MockModule()
    ifconfig_network = GenericBsdIfconfigNetwork(module)
    ifconfig_network.platform = "FreeBSD"
    actual = ifconfig_network.get_default_interfaces("/usr/local/bin/route")

# Generated at 2022-06-13 01:33:35.364099
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_default_interfaces():
    network = GenericBsdIfconfigNetwork()
    assert network.get_default_interfaces(route_path='route') == ({u'interface': u'lo0'},
                                                                  {u'interface': u'lo0'})


# Generated at 2022-06-13 01:33:37.724014
# Unit test for method parse_inet6_line of class GenericBsdIfconfigNetwork

# Generated at 2022-06-13 01:33:54.819412
# Unit test for method detect_type_media of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_detect_type_media():
    interface_list = dict(
        foo1={'device': 'foo1', 'media': 'Ether'},
        foo2={'device': 'foo2', 'media': 'Ether'},
        foo3={'device': 'foo3', 'media': 'Ether'},
        foo4={'device': 'foo4', 'media': 'Ether'},
        bar1={'device': 'bar1', 'media': 'something'},
        bar2={'device': 'bar2', 'media': 'something'},
        bar3={'device': 'bar3', 'media': 'something'},
        bar4={'device': 'bar4', 'media': 'something'},
    )

    for media in ['ether', 'Ether']:
        for val in interface_list:
            interface_list[val]['media']

# Generated at 2022-06-13 01:34:05.896983
# Unit test for method parse_inet_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet_line():
    module = AnsibleModule(argument_spec={})
    module.run_command = MagicMock(return_value=(0, "", ""))
    module.params = {'v4': True, 'v6': True}

    network = GenericBsdIfconfigNetwork(module)
    # Parse the inet line with cidr style address
    # For example on netbsd ifconfig -e output after 7.1
    # lo0: flags=8049<UP,LOOPBACK,RUNNING,MULTICAST> mtu 33184
    #         inet 127.0.0.1/24 netmask 0xff000000

    current_if = {'device': 'lo0', 'ipv4': [], 'ipv6': [], 'type': 'unknown'}

# Generated at 2022-06-13 01:34:17.449919
# Unit test for method get_interfaces_info of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_interfaces_info():
    module_name = 'ansible.module_utils.network.bsd.ifconfig'
    module = import_module(module_name)
    if not hasattr(module, 'GenericBsdIfconfigNetwork'):
        raise SkipTest("test_GenericBsdIfconfigNetwork_get_interfaces_info "
                       "requires %s" % module_name)

    #
    # FreeBSD 11.3
    #

# Generated at 2022-06-13 01:34:26.074968
# Unit test for method parse_media_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_media_line():
    test_cases = [
        ['media: Ethernet autoselect (100baseTX <full-duplex>)', {'media': 'Ethernet', 'media_select': 'autoselect', 'media_type': '(100baseTX', 'media_options': ['full-duplex']}],
        ['media: Ethernet autoselect (basT/UTP <full-duplex>)', {'media': 'Ethernet', 'media_select': 'autoselect', 'media_type': '(basT', 'media_options': ['UTP', 'full-duplex']}],
        ['media: Ethernet autoselect (none) status: inactive', {'media': 'Ethernet', 'media_select': 'autoselect', 'media_type': '(none)', 'status': 'inactive'}],
    ]


# Generated at 2022-06-13 01:34:33.961145
# Unit test for method get_interfaces_info of class GenericBsdIfconfigNetwork

# Generated at 2022-06-13 01:34:43.710981
# Unit test for method parse_inet_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet_line():
    from mock import MagicMock, patch
    from ansible.module_utils.facts import ansible_facts

    # test case 1: normal case
    test_module = MagicMock()
    test_ifconfig_path = ['ifconfig', '-a']
    test_run_command_rc = 0

# Generated at 2022-06-13 01:34:53.155679
# Unit test for method get_interfaces_info of class GenericBsdIfconfigNetwork

# Generated at 2022-06-13 01:35:03.752001
# Unit test for method parse_inet_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet_line():
    c = GenericBsdIfconfigNetwork()
    i = {}
    ips = {}
    # netbsd show aliases like this
    #  lo0: flags=8049<UP,LOOPBACK,RUNNING,MULTICAST> mtu 33184
    #         inet 127.0.0.1 netmask 0xff000000
    #         inet alias 127.1.1.1 netmask 0xff000000
    c.parse_inet_line(["lo0:", "127.0.0.1", "netmask", "0xff000000"], i, ips)
    assert i["ipv4"][0]["address"] == "127.0.0.1"
    assert i["ipv4"][0]["netmask"] == "255.255.0.0"
    i = {}
    c.parse_

# Generated at 2022-06-13 01:35:11.444565
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():
    module = AnsibleModule
    module.run_command = mock.Mock(return_value=[0, 'success', None])
    module.get_bin_path = mock.Mock(return_value=True)
    obj = GenericBsdIfconfigNetwork(module)
    obj.populate()

    assert 'success' in obj.get_default_interfaces()[1]
    assert 'success' in obj.get_interfaces_info('test')[0][0]['ipv6'][0]
    assert obj.detect_type_media(obj.get_interfaces_info('test')[0])['interface']['type'] == 'ether'



# Generated at 2022-06-13 01:35:16.723523
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():
    module_args = dict()

    # In the absence of any source of network facts, the populate function
    # should fail with an error.
    check_ifconfig_facts(module_args, True, [], [], {})

    # Ensure that our ifconfig stubs work
    check_ifconfig_facts(module_args, False, [], [], {})

    # Ensure that our route stubs work
    check_ifconfig_facts(module_args, False, [], [], {})


# Generated at 2022-06-13 01:35:48.144007
# Unit test for method detect_type_media of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_detect_type_media():
    interfaces = dict()
    interfaces['em0'] = dict()
    interfaces['em0']['media'] = 'Ethernet autoselect (1000baseT full-duplex)'

    network_facts = GenericBsdIfconfigNetwork()
    network_facts.detect_type_media(interfaces)

    assert(interfaces['em0']['type'] == 'ether')


# Generated at 2022-06-13 01:35:53.623500
# Unit test for method get_interfaces_info of class GenericBsdIfconfigNetwork

# Generated at 2022-06-13 01:35:55.565045
# Unit test for method get_interfaces_info of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_interfaces_info():
    module = AnsibleModule(
        argument_spec=dict(),
    )
    network_module = GenericBsdIfconfigNetwork(module)

    network_module.get_interfaces_info()



# Generated at 2022-06-13 01:36:04.095279
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_default_interfaces():
    module = AnsibleModule({})
    my_obj = GenericBsdIfconfigNetwork()

    my_obj.module = module
    if hasattr(my_obj, 'get_default_interfaces'):
        route_path = module.get_bin_path('route')
        result = my_obj.get_default_interfaces(route_path)
        print("{}".format(result))
        if result is not None:
            if 'gateway' in result[0] or 'gateway' in result[1]:
                module.exit_json(changed=False)
    module.exit_json(changed=True)


# Generated at 2022-06-13 01:36:11.513164
# Unit test for method parse_inet_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet_line():
    # Test passing in empty words list
    network = GenericBsdIfconfigNetwork()
    current_if = {'device': 'lo0'}
    ips = dict(all_ipv4_addresses=[])
    words = []
    network.parse_inet_line(words, current_if, ips)
    assert ('ipv4' not in current_if and
            'all_ipv4_addresses' not in ips)

    # Test passing in alias
    current_if = {'device': 'lo0'}
    ips = dict(all_ipv4_addresses=[])
    words = ['inet', 'alias', '127.1.1.1', 'netmask', '0xff000000']
    network.parse_inet_line(words, current_if, ips)

# Generated at 2022-06-13 01:36:19.680152
# Unit test for method get_interfaces_info of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_interfaces_info():
    m = module_args()
    m['command'] = '/sbin/ifconfig -a'
    m['_ansible_check_mode'] = True
    m['_ansible_verbosity'] = 0
    m['_ansible_debug'] = False
    m['_ansible_diff'] = False
    m['_ansible_no_log'] = False
    m['_ansible_string_conversion_action'] = 'warn'
    m['_ansible_remote_tmp'] = '/tmp'
    m['_ansible_keep_remote_files'] = False
    m['_ansible_remote_tmp_exec_timeout'] = 60
    m['_ansible_module_name'] = 'command'
    m['_ansible_module_setup'] = True
    m['_ansible_socket'] = None

# Generated at 2022-06-13 01:36:26.438600
# Unit test for method get_interfaces_info of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_interfaces_info():
    ifconfig_path = '/sbin/ifconfig'
    #ifconfig_path = 'ifconfig'
    ifconfig_options = '-a'
    module = FakeModule()
    net_mod = GenericBsdIfconfigNetwork(module)
    interfaces, ips = net_mod.get_interfaces_info(ifconfig_path, ifconfig_options)
    assert interfaces['lo0']['macaddress'] == 'unknown'
    assert interfaces['lo0']['ipv4'][0]['broadcast'] == '127.255.255.255'
    #assert interfaces['lo0']['ipv4'][0]['netmask'] == '255.0.0.0'
    #assert interfaces['lo0']['ipv4'][0]['network'] == '127.0.0.0'
   

# Generated at 2022-06-13 01:36:35.548635
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork

# Generated at 2022-06-13 01:36:44.361659
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():
    network = GenericBsdIfconfigNetwork()
    defaults = dict(interface='lo0')
    interfaces = dict(
        lo0=dict(
            flags=['UP', 'LOOPBACK', 'RUNNING'],
            ipv4=[
                dict(address='127.0.0.1', broadcast='0.0.0.0', netmask='255.0.0.0', network='127.0.0.0')
            ],
            ipv6=[
                dict(address='::1/128', broadcast='0.0.0.0', netmask='255.0.0.0', network='127.0.0.0')
            ],
            macaddress='unknown',
            metric='0',
            mtu='33184',
            type='loopback'
        )
    )
    network.merge_default

# Generated at 2022-06-13 01:36:51.986255
# Unit test for method parse_inet6_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet6_line():
    a = {'address': 'fe80::21f:c9ff:fef3:45e'}
    b = {'address': 'fe80::21f:c9ff:fef3:45e', 'prefix': '64', 'scope': 'link'}
    c = {'address': 'fe80::21f:c9ff:fef3:45e/64', 'scope': 'link'}

    d = {'address': 'fe80::21f:c9ff:fef3:45e/64'}
    e = {'address': 'fe80::21f:c9ff:fef3:45e/64', 'scope': 'link'}