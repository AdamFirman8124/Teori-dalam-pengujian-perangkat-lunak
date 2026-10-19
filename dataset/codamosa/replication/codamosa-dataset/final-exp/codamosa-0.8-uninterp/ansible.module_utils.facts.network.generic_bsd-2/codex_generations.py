

# Generated at 2022-06-13 01:27:53.116202
# Unit test for method parse_media_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_media_line():
    module = AnsibleModule({})
    network = GenericBsdIfconfigNetwork(module)
    current_if = {}
    ips = {}
    line = 'media: IEEE 802.11 Wireless Ethernet autoselect (autoselect)'
    words = line.split()

    network.parse_media_line(words, current_if, ips)

    assert current_if['media'] == 'IEEE'
    assert current_if['media_select'] == '802.11'
    assert current_if['media_type'] == 'Wireless'
    assert current_if['media_options'] == ['Ethernet', 'autoselect', '(autoselect)']



# Generated at 2022-06-13 01:27:58.887059
# Unit test for method parse_media_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_media_line():
    network = GenericBsdIfconfigNetwork()
    current_if = {}

    words = ['media:', 'Ethernet', 'autoselect', '(1000baseT', '<full-duplex>)']
    network.parse_media_line(words, current_if, {})
    assert current_if['media'] == 'Ethernet'
    assert current_if['media_type'] == '1000baseT'
    assert current_if['media_select'] == 'autoselect'
    assert current_if['media_options'] == ['full-duplex']

    words = ['media:', 'Ethernet', 'manual', '10baseT/UTP']
    network.parse_media_line(words, current_if, {})
    assert current_if['media'] == 'Ethernet'

# Generated at 2022-06-13 01:28:04.883247
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():
    module = AnsibleModule({})
    bsd = Generic_BSD_Ifconfig(module)
    res = bsd.populate()
    assert 'interfaces' in res
    assert 'default_ipv4' in res
    assert res['default_ipv4']['gateway'] == '10.209.255.254'
    assert 'all_ipv4_addresses' in res
    assert 'all_ipv6_addresses' in res

# Generated at 2022-06-13 01:28:09.953120
# Unit test for method parse_interface_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_interface_line():
    interface_line = 'lo0: flags=8049<UP,LOOPBACK,RUNNING,MULTICAST> metric 0 mtu 16384'
    expected = {'device': 'lo0', 'ipv4': [], 'ipv6': [], 'type': 'unknown', 'flags': ['UP', 'LOOPBACK', 'RUNNING', 'MULTICAST'], 'metric': '0', 'mtu': '16384', 'macaddress': 'unknown'}
    f = GenericBsdIfconfigNetwork()
    actual = f.parse_interface_line(interface_line.split())
    assert actual == expected


# Generated at 2022-06-13 01:28:19.906063
# Unit test for method populate of class GenericBsdIfconfigNetwork

# Generated at 2022-06-13 01:28:25.859812
# Unit test for method parse_media_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_media_line():
    # Test with a empty line
    line = ""
    words = line.split()
    current_if = {'device': 'mydevice', 'ipv4': [], 'ipv6': [], 'type': 'unknown'}
    ips = dict(all_ipv4_addresses=[], all_ipv6_addresses=[])
    GenericBsdIfconfigNetwork.parse_media_line(words, current_if, ips)
    assert (current_if['media'] != '0') is True


# Generated at 2022-06-13 01:28:34.695141
# Unit test for method detect_type_media of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_detect_type_media():
    # Setup test case
    generic_bsd_ifconfig_network = GenericBsdIfconfigNetwork()

# Generated at 2022-06-13 01:28:39.751596
# Unit test for method get_interfaces_info of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_interfaces_info():
    testcases = dict()
    # testcase 1
    data = dict()

# Generated at 2022-06-13 01:28:52.111538
# Unit test for method parse_inet6_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet6_line():
    fact_module = GenericBsdIfconfigNetwork()
    # Case 1: non-standard IP address
    iface = {}
    ip = []
    # ip = [{'address': 'fe80::1%lo0'}, {'address': '::1'}]
    fact_module.parse_inet6_line(['inet6', 'fe80::1%lo0', 'prefixlen', '64', 'scopeid', '0x1', 'lo0'], iface, ip)
    assert(iface['ipv6'][0] == {'address': 'fe80::1%lo0', 'prefix': '64', 'scope': '0x1'})
    assert(len(ip) == 0)  # we don't care about ipv6 addresses

    # Case 2: standard IPv6 address (cidr style)
   

# Generated at 2022-06-13 01:29:00.366213
# Unit test for method detect_type_media of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_detect_type_media():
    """GenericBsdIfconfigNetwork - detect type media
    Test case to validate detect_type_media method of class GenericBsdIfconfigNetwork
    """
    iface1 = {'device': 'lo0', 'ipv4': [], 'ipv6': [], 'type': 100, 'flags': 'none'}
    iface2 = {'device': 'lo1', 'ipv4': [], 'ipv6': [], 'type': 'unknown', 'flags': 'none', 'media': 'unknown'}
    iface3 = {'device': 'lo2', 'ipv4': [], 'ipv6': [], 'type': 'ether', 'flags': 'none', 'media': 'ether'}

# Generated at 2022-06-13 01:29:20.966990
# Unit test for method parse_media_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_media_line():
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )

    words = [
        'media:',
        'Ethernet',
        '10Gbase-T',
        '(10Gbase-T <full-duplex,flow-control,rxpause,txpause>)',
        'status:',
        'active'
    ]

    expected = dict(
        type='ether',
        media='Ethernet',
        media_type='10Gbase-T',
        media_options=['full-duplex', 'flow-control', 'rxpause', 'txpause'],
        status='active'
    )

    current_if = dict(
        type='ether',
    )


# Generated at 2022-06-13 01:29:30.306551
# Unit test for method parse_inet6_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet6_line():
    iface = {
        'ipv6': [],
        'macaddress': None,
        'mtu': 1500,
        'device': 'lo0',
        'flags': ['LOOPBACK', 'UP', 'RUNNING'],
        'ipv4': [],
        'type': 'loopback',
    }
    ips = dict(all_ipv6_addresses=[])
    ifconfig = GenericBsdIfconfigNetwork()

    # test no prefix
    words = ['inet6', '::1', 'prefixlen', '128', '0x1', 'priority', '0', 'netmask', '0xff000000', 'scopeid', '0x1']
    ifconfig.parse_inet6_line(words, iface, ips)

# Generated at 2022-06-13 01:29:39.075778
# Unit test for method get_interfaces_info of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_interfaces_info():
    module = AnsibleModule({}, {}, {}, False, False)
    module.get_bin_path = mock.MagicMock(return_value="ifconfig_path")
    module.run_command = mock.MagicMock(return_value=(0, "out", ""))
    fact = GenericBsdIfconfigNetwork(module)

    ifconfig_path = "/path/to/ifconfig"
    ifconfig_options = "-a"
    r = fact.get_interfaces_info(ifconfig_path, ifconfig_options)
    assert r


# Generated at 2022-06-13 01:29:46.369456
# Unit test for method get_interfaces_info of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_interfaces_info():
    module = AnsibleModule(argument_spec={},
                           supports_check_mode=True)
    ifconfig_path = module.get_bin_path('ifconfig')
    ifconfig_options = '-a'
    interface_facts = GenericBsdIfconfigNetwork()
    interfaces, ips = interface_facts.get_interfaces_info(ifconfig_path, ifconfig_options)
    assert len(interfaces) > 0
    assert len(ips) > 0


# Generated at 2022-06-13 01:29:49.515140
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():
    ut_mock = UtMock(platform='Generic_BSD_Ifconfig')

    GenericBsdIfconfigNetwork = GenericBsdIfconfigNetwork()
    result = GenericBsdIfconfigNetwork.populate()
    assert True


# Generated at 2022-06-13 01:29:54.562074
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_default_interfaces():
    cmd_output = \
'''
default
        hopcount      0
        inifp         lo0
        interface     lo0
        recvpipe      0
        route-type    Static
        sendpipe      0
        srcaddr       127.0.0.1
'''
    ifconfig_platform = GenericBsdIfconfigNetwork()
    result = ifconfig_platform.get_default_interfaces(cmd_output)
    assert(result[0].get('interface') == 'lo0' and
           result[0].get('gateway') == '0.0.0.0')

# Generated at 2022-06-13 01:30:04.877092
# Unit test for method parse_interface_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_interface_line():
    """
    Test the method parse_interface_line of GenericBsdIfconfigNetwork class

    """
    # Arrange
    words = ["lo0:",
             "flags=8049<UP,LOOPBACK,RUNNING,MULTICAST>",
             "metric", "0",
             "mtu", "33184",
             "options=680003<RXCSUM,TXCSUM,LINKSTATE,RXCSUM_IPV6,TXCSUM_IPV6>",
             "groups=lo",
             "nd6", "options=21<PERFORMNUD,AUTO_LINKLOCAL>",
             "media:", "loopback",
             "status:", "active"]
    current_if = dict()
    # Act
    current_if = GenericBsdIfconfigNetwork.parse_interface

# Generated at 2022-06-13 01:30:16.790973
# Unit test for method parse_inet_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet_line():
    interfaces = {}
    current_if = {'device': 'lo0', 'ipv4': [], 'ipv6': [], 'type': 'unknown'}
    ips = {'all_ipv4_addresses': [], 'all_ipv6_addresses': []}
    genericBsdIfconfigNetwork = GenericBsdIfconfigNetwork()
    # test ipv4:
    words = ['lo0', 'inet', '10.236.22.48', 'netmask', '0xffffff00', 'broadcast', '10.236.22.255']
    genericBsdIfconfigNetwork.parse_inet_line (words, current_if, ips)
    # result should be:

# Generated at 2022-06-13 01:30:25.893399
# Unit test for method parse_inet_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet_line():
    network = GenericBsdIfconfigNetwork()
    line = "inet 127.0.0.1 netmask 0xff000000"
    current_if = dict(ipv4=[])
    ips = dict()
    words = line.split(' ')
    network.parse_inet_line(words, current_if, ips)
    assert current_if['ipv4'][0]['address'] == '127.0.0.1'
    assert current_if['ipv4'][0]['netmask'] == '255.255.255.0'
    assert current_if['ipv4'][0]['network'] == '127.0.0.0'
    assert current_if['ipv4'][0]['broadcast'] == '127.0.0.255'
    assert ips == dict()
    line

# Generated at 2022-06-13 01:30:34.452019
# Unit test for method get_interfaces_info of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_interfaces_info():
    ifconfig_path = '/sbin/ifconfig'

    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )

    # Mock the module
    generic_bsd_ifconfig_network = GenericBsdIfconfigNetwork()
    generic_bsd_ifconfig_network.module = module


# Generated at 2022-06-13 01:31:11.161092
# Unit test for method parse_inet6_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet6_line():
    # pylint: disable=no-self-use,star-args
    # Set up object
    module = MagicMock()
    current_if = {}
    ips = {}
    gb = GenericBsdIfconfigNetwork(module)
    # Call method
    gb.parse_inet6_line(['inet6', 'fe80::8'], current_if, ips)
    # Check results
    assert ips == {'all_ipv6_addresses': ['fe80::8']}
    assert current_if == {'ipv6': [{'address': 'fe80::8', 'prefix': None, 'scope': None}]}

# Generated at 2022-06-13 01:31:18.458699
# Unit test for method parse_inet_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet_line():
    mython = GenericBsdIfconfigNetwork()
    current_if = {'ipv4': []}
    ips = dict(
        all_ipv4_addresses=[],
    )
    mython.parse_inet_line(['inet', '172.20.0.1', 'netmask', '0xffffff00'], current_if, ips)
    assert current_if['ipv4'][0]['address'] == '172.20.0.1'
    assert current_if['ipv4'][0]['netmask'] == '255.255.255.0'
    assert current_if['ipv4'][0]['network'] == '172.20.0.0'
    assert current_if['ipv4'][0]['broadcast'] == '172.20.0.255'

# Generated at 2022-06-13 01:31:27.641847
# Unit test for method parse_inet_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet_line():
    gb = GenericBsdIfconfigNetwork()
    words = [
        'lo0',
        'inet',
        '127.0.0.1',
        'netmask',
        '0xff000000',
    ]
    current_if = {}
    current_if['device'] = words[0]
    ipv4 = []
    current_if['ipv4'] = ipv4
    ips = dict(
        all_ipv4_addresses=[],
        all_ipv6_addresses=[],
    )

    gb.parse_inet_line(words, current_if, ips)

    assert len(ipv4) == 1

# Generated at 2022-06-13 01:31:39.607523
# Unit test for method parse_inet_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet_line():
    ifconfig_mock_path = 'ansible.module_utils.basic.AnsibleModule.run_command'
    ifconfig_mockup = {'inet': u'netmask 0xffffff00 broadcast 10.0.0.255'}

    ifconfig_mockup2 = {'inet': u'netmask 255.255.255.0 broadcast 10.0.0.255'}


# Generated at 2022-06-13 01:31:43.328307
# Unit test for method get_options of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_options():
    facter = GenericBsdIfconfigNetwork()

    assert facter.get_options('flags=8843<UP,BROADCAST,RUNNING,SIMPLEX,MULTICAST>') == ['UP', 'BROADCAST', 'RUNNING', 'SIMPLEX', 'MULTICAST']



# Generated at 2022-06-13 01:31:50.512663
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_default_interfaces():
    network = GenericBsdIfconfigNetwork()
    from collections import namedtuple
    module = namedtuple('module', ['run_command'])
    module.run_command = lambda x: [0, '', '']
    network.module = module

    ipv4_ret, ipv6_ret = network.get_default_interfaces('sbin/route')

    assert ipv4_ret == {}
    assert ipv6_ret == {}

# Generated at 2022-06-13 01:31:55.866176
# Unit test for method get_options of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_options():

    # Set context
    module = AnsibleModule({})
    network = GenericBsdIfconfigNetwork(module)

    # Check result
    option_csv = 'UP,LOOPBACK,RUNNING'
    option_string = 'flags=8049<' + option_csv + '>, mtu 33184'
    assert network.get_options(option_string) == option_csv.split(',')


# Generated at 2022-06-13 01:32:07.494392
# Unit test for method parse_inet6_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet6_line():
    # Test for the inet6_line of the GenericBsdIfconfigNetwork class.
    # The interface that is passed as argument will be modified to
    # include the IP address information.
    #
    # :param words: List of values from the ifconfig command
    # :param current_if: dictionary with the new interface informatio
    # :param ips: dictionary with all the found IP addresses
    #
    # :return: Modified current_if and ips dictionaries
    #
    #
    # This is the current_if dictionary, which will store the parsed
    # data of a network interface.
    #
    # current_if = {'device': device, 'ipv4': [], 'ipv6': [], 'type': 'unknown'}

    current_if={}
    ips={}

    # Case 1 - address without

# Generated at 2022-06-13 01:32:16.893202
# Unit test for method populate of class GenericBsdIfconfigNetwork

# Generated at 2022-06-13 01:32:17.457222
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():
    pass



# Generated at 2022-06-13 01:32:38.492290
# Unit test for method detect_type_media of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_detect_type_media():
    TestGenericBsdIfconfigNetwork = GenericBsdIfconfigNetwork(dict(params=dict()), dict(ansible_facts=dict()))


# Generated at 2022-06-13 01:32:47.472173
# Unit test for method parse_inet_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet_line():
    ipnet = GenericBsdIfconfigNetwork()
    current_if = {}
    ips = dict(
        all_ipv4_addresses=[],
    )
    w = ['inet', '10.3.3.3', 'netmask', '0xffffff00']
    ipnet.parse_inet_line(w, current_if, ips)
    assert current_if == {'ipv4': [{'netmask': '255.255.255.0', 'address': '10.3.3.3', 'broadcast': '10.3.3.255', 'network': '10.3.3.0'}]}
    w = ['inet', '10.3.3.3', 'netmask', '255.255.255.0', 'broadcast', '10.3.3.255']
    ip

# Generated at 2022-06-13 01:32:54.379213
# Unit test for method parse_interface_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_interface_line():
    ifconfig_path = ""
    ifconfig_options = '-a'
    module = MagicMock()
    module.get_bin_path.return_value = "ifconfig"
    module.run_command.return_value = 0, "", ""
    gbifconfig = GenericBsdIfconfigNetwork(module)


# Generated at 2022-06-13 01:33:01.190062
# Unit test for method get_interfaces_info of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_interfaces_info():
    # Mock modules
    import sys

    MOCK_MODULES = [
        'socket',
    ]

    sys.modules.update((mod_name, Mock()) for mod_name in MOCK_MODULES)


# Generated at 2022-06-13 01:33:04.952649
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_default_interfaces():
    module = AnsibleModule(argument_spec=dict())
    network = GenericBsdIfconfigNetwork(module)
    assert network.get_default_interfaces('/bin/route') == ({}, {})

# Generated at 2022-06-13 01:33:12.896388
# Unit test for method detect_type_media of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_detect_type_media():
    from ansible.module_utils.facts import Network

    gbin = GenericBsdIfconfigNetwork(module=Network)

    interfaces = {
        'em0': {'media':'Ethernet autoselect (1000baseT <full-duplex,flow-control>)', 'type':''}
    }
    result = {
        'em0': {'media':'Ethernet autoselect (1000baseT <full-duplex,flow-control>)', 'type':'ether'}
    }
    assert gbin.detect_type_media(interfaces) == result, \
        "detect_type_media failed"


# Generated at 2022-06-13 01:33:19.113341
# Unit test for method populate of class GenericBsdIfconfigNetwork

# Generated at 2022-06-13 01:33:30.247778
# Unit test for method parse_interface_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_interface_line():
    network = GenericBsdIfconfigNetwork()

    words = "lo0: flags=8049<UP,LOOPBACK,RUNNING,MULTICAST> mtu 3300"
    words = words.split()
    actual_result = network.parse_interface_line(words)
    expected_result = {
        "device": "lo0",
        "ipv4": [],
        "ipv6": [],
        "type": "loopback",
        "flags": ["UP", "LOOPBACK", "RUNNING", "MULTICAST"],
        "macaddress": "unknown",
        "metric": None,
        "mtu": "3300"
    }
    assert actual_result == expected_result


# Generated at 2022-06-13 01:33:40.215059
# Unit test for method parse_inet_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet_line():
    module = AnsibleModule({})
    gen = GenericBsdIfconfigNetwork(module=module)

    words = ['lo0', 'flags=8049<UP,LOOPBACK,RUNNING,MULTICAST>', 'mtu', '33184', 'inet', '127.0.0.1', 'netmask', '0xff000000']
    current_if = {}
    ips = dict(
        all_ipv4_addresses=[],
        all_ipv6_addresses=[]
    )
    gen.parse_interface_line(words=words, current_if=current_if, ips=ips)

# Generated at 2022-06-13 01:33:50.245252
# Unit test for method parse_inet_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet_line():
    # basic testing of ipv4 parsing
    ifinfo = dict(device='lo0', ipv4=[], ipv6=[], type='unknown')
    ips = dict(all_ipv4_addresses=[], all_ipv6_addresses=[])
    GenericBsdIfconfigNetwork.parse_inet_line(['inet', '127.0.0.1', 'netmask', '0xff000000'], ifinfo, ips)
    assert ifinfo['ipv4'][0]['address'] == '127.0.0.1'
    assert ifinfo['ipv4'][0]['netmask'] == '255.0.0.0'
    assert ifinfo['ipv4'][0]['network'] == '127.0.0.0'

# Generated at 2022-06-13 01:34:22.936137
# Unit test for method detect_type_media of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_detect_type_media():
    assert GenericBsdIfconfigNetwork({}).detect_type_media({'eth0': {'media': 'Ethernet autoselect'}}) == {'eth0': {'media': 'Ethernet autoselect', 'type': 'ether'}}

# Generated at 2022-06-13 01:34:31.711499
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():
    generic_bsd_ifconfig_network = GenericBsdIfconfigNetwork()

# Generated at 2022-06-13 01:34:41.970700
# Unit test for method parse_inet_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet_line():
    module = AnsibleModule(
        argument_spec=dict()
    )

    current_if = dict(
        ipv4=[],
        ipv6=[],
        type='unknown',
    )

    ips = dict(
        all_ipv4_addresses=[],
        all_ipv6_addresses=[],
    )


# Generated at 2022-06-13 01:34:51.740321
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():
    module = AnsibleModule({})


# Generated at 2022-06-13 01:34:57.365965
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():
    module = AnsibleModule(
        argument_spec=dict(
            gather_subset=dict(default=['!all', '!min'], type='list')
        ),
        supports_check_mode=True
    )

    # Load the actual plugin and run method
    from ansible.plugins.net_fact.BSD import GenericBsdIfconfigNetwork
    n = GenericBsdIfconfigNetwork()

    module.run_command = MagicMock(return_value=(0, "ifconfig", ""))
    result = n.populate()

    module.run_command = MagicMock(return_value=(1, "", "error"))
    result = n.populate()

    module.run_command = MagicMock(return_value=(0, "", ""))
    result = n.populate()


# Generated at 2022-06-13 01:35:06.366366
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_default_interfaces():
    module = AnsibleModule({})
    module.run_command = MagicMock()

    # FreeBSD
    module.run_command.return_value = (0,
        'default 172.16.0.1 UGS 0 37721 en0\n'
        '127.0.0.1 link#5 UH lo0', None)
    obj = GenericBsdIfconfigNetwork()
    obj.get_default_interfaces('/sbin/route')
    assert module.run_command.call_count == 1
    assert module.run_command.call_args == call(['/sbin/route', '-n', 'get', 'default'])

    # NetBSD 7.1 or older

# Generated at 2022-06-13 01:35:15.177853
# Unit test for method get_options of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_options():

    ifc = GenericBsdIfconfigNetwork()
    # case 1: no options
    options = ifc.get_options('hello')
    assert options == []

    # case 2: no options, with string
    options = ifc.get_options('something<>')
    assert options == []

    # case 3: one option with no spaces
    options = ifc.get_options('something<hello>')
    assert options == ['hello']

    # case 4: one option
    options = ifc.get_options('something< hello >')
    assert options == ['hello']

    # case 5: two options
    options = ifc.get_options('something<hello,world>')
    assert options == ['hello', 'world']

    # case 6: leading/trailing whitespace on option is removed
    options = ifc.get_

# Generated at 2022-06-13 01:35:26.077159
# Unit test for method parse_inet_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet_line():
    facter_spec.setargs(dict(
        module_name='facts.collector.network',
        module_args=dict(gather_subset='!all', filter='ansible_lo'))
    )
    module = ansible_module_get_network_module(facter_spec, supports_check_mode=False)
    test_obj = GenericBsdIfconfigNetwork(module)
    test_if = dict()
    test_ips = dict()
    test_if['ipv4'] = []
    test_ips['all_ipv4_addresses'] = []

    test_words1 = ['lo0', 'inet', '127.0.0.1', 'netmask', '0xff000000']
    test_obj.parse_inet_line(test_words1, test_if, test_ips)
   

# Generated at 2022-06-13 01:35:33.125422
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():
    import yaml
    from ansible.module_utils.facts import Network
    from ansible.module_utils.facts.collector import TestNetworkFactsModule

    test_ifconfig_path = "/ifconfig/path"
    test_route_path = "/route/path"
    test_ifconfig_options = "-a"


# Generated at 2022-06-13 01:35:39.528958
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_default_interfaces():
    from ansible_collections.ansible.community.tests.unit.modules.utils import AnsibleExitJson, AnsibleFailJson, ModuleTestCase, set_module_args

    class AnsibleGenericBsdIfconfigNetworkGetDefaultInterfaces(GenericBsdIfconfigNetwork):
        # On the class, override the module exit hooks so we can control what happens
        def __init__(self):
            self.exit_json = AnsibleExitJson
            self.fail_json = AnsibleFailJson

        def get_default_interfaces(self, route_path):
            return ("", "")

    ansible_module = AnsibleGenericBsdIfconfigNetworkGetDefaultInterfaces()
    assert ansible_module.get_default_interfaces("/path/to/route") == ("", "")

# Generated at 2022-06-13 01:36:51.960693
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_default_interfaces():
    module = None
    bin_path = dict(route='/dev/null')
    platform = dict(distribution=dict(lower='freebsd'))
    network = GenericBsdIfconfigNetwork(module, bin_path, platform)
    route_path = bin_path['route']
    expect = (dict(interface='lo0', gateway='127.0.0.1', address='127.0.0.1'),
              dict(interface='lo0', gateway='::1', address='::1'))

    actual = network.get_default_interfaces(route_path)
    assert actual == expect



# Generated at 2022-06-13 01:37:01.187839
# Unit test for method populate of class GenericBsdIfconfigNetwork

# Generated at 2022-06-13 01:37:08.872647
# Unit test for method get_options of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_options():
    import sys
    import mock
    from ansible.module_utils import basic

    host_name = 'localhost'
    port = 22
    user_name = 'root'
    pass_word = 'password'
    private_key = 'private_key'
    ansible_module = mock.MagicMock(spec=AnsibleModule)
    ansible_module.params = {
        'host': host_name,
        'port': port,
        'username': user_name,
        'password': pass_word,
        'private_key_file': private_key
    }
    ansible_module.get_bin_path = basic.get_bin_path
    task_vars = dict()
