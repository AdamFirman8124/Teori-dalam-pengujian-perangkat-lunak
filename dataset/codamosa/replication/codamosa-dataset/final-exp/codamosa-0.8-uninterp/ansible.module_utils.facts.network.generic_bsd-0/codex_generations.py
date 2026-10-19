

# Generated at 2022-06-13 01:27:46.513323
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():
    # init

    # mock
    mock_defaults = dict(interface='en0')
    mock_interfaces = dict(en0=dict(ipv4=[], ipv6=[]))
    mock_ip_type = 'ipv4'
    # tests

    # execute
    execute_code = '''\
GenericBsdIfconfigNetwork.merge_default_interface({}, {}, {})
'''.format(mock_defaults, mock_interfaces, mock_ip_type)
    with mock.patch('ansible_collections.notmintest.not_a_real_collection.plugins.module_utils.network.common.utils.ifconfig.GenericBsdIfconfigNetwork.merge_default_interface') as mock_GenericBsdIfconfigNetwork_merge_default_interface:
        exec(execute_code)
       

# Generated at 2022-06-13 01:27:51.991432
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():
    net = GenericBsdIfconfigNetwork()
    m = MockNetwork()
    m.module.run_command = lambda *args, **kwargs: (0, 'interface: lo0', '')
    net.module = m
    m.module.get_bin_path = lambda *args, **kwargs: '/sbin/route'
    net.get_default_interfaces = lambda *args, **kwargs: ({'interface': 'lo0'}, {})
    net.merge_default_interface({'ipv4': {'interface': 'lo0', 'address': '127.0.0.1'}}, {'lo0': {'ipv4': [{'address': '127.0.0.1'}]}}, 'ipv4')
    assert True

# Generated at 2022-06-13 01:27:56.718664
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():
    g = GenericBsdIfconfigNetwork()
    default_ipv4 = dict(interface='lo0')
    interfaces = dict(lo0=dict(ipv4=[dict(address='127.0.0.1', netmask='255.0.0.0')], ipv6=[], type='loopback'))
    g.merge_default_interface(default_ipv4, interfaces, 'ipv4')
    assert_equals(default_ipv4, dict(interface='lo0', address='127.0.0.1', netmask='255.0.0.0', type='loopback'))


# Generated at 2022-06-13 01:28:07.972179
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():
    network = GenericBsdIfconfigNetwork()
    ifconfig_path = '/sbin/ifconfig'
    route_path = '/sbin/route'
    
    # Interface lo0
    ifconfig_lo0 = '''lo0: flags=8049<UP,LOOPBACK,RUNNING,MULTICAST> metric 0 mtu 16384
        options=600003<RXCSUM,TXCSUM,RXCSUM_IPV6,TXCSUM_IPV6>
        inet 127.0.0.1 netmask 0xff000000
        inet6 ::1 prefixlen 128 
        inet6 fe80::1%lo0 prefixlen 64 scopeid 0x2 
        nd6 options=21<PERFORMNUD,AUTO_LINKLOCAL>
        groups: lo
'''
    
   

# Generated at 2022-06-13 01:28:18.808857
# Unit test for method parse_media_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_media_line():
    import platform
    import sys
    # Test variables
    words = ['media:', 'Ethernet', '10Gbase-LR', '(100baseTX <full-duplex>)'
        , 'status:', 'active', 'lladdr', '2c:56:dc:7a:20:d9']

    # Get platform
    if platform.system() != 'Darwin':
        pytest.xfail("Skipping because platform is not Mac OSX")
    else:
        module = Mock()

        # Create instance of class GenericBsdIfconfigNetwork
        generic_bsd_ifconfig_network = GenericBsdIfconfigNetwork(module)
        # Call method parse_media_line of GenericBsdIfconfigNetwork
        result = generic_bsd_ifconfig_network.parse_media_line(words, current_if, ips)

# Generated at 2022-06-13 01:28:19.521199
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():
    pass


# Generated at 2022-06-13 01:28:26.313694
# Unit test for method parse_inet6_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet6_line():

    # Test without a cidr mask
    words1 = 'fe80::1%lo0%lo1 prefixlen 64 scopeid 0x2'.split()
    current_if = {'device': 'lo1', 'ipv6': [], 'type': 'unknown'}
    ips = dict(
        all_ipv6_addresses=[],
    )
    expected_ipv6 = [{'address': 'fe80::1%lo0', 'prefix': '64', 'scope': '0x2'}]
    expected_all_ipv6_addresses = ['fe80::1%lo0']
    GenericBsdIfconfigNetwork.parse_inet6_line(words1, current_if, ips)
    assert current_if['ipv6'] == expected_ipv6

# Generated at 2022-06-13 01:28:34.908157
# Unit test for method parse_media_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_media_line():
    current_if = OrderedDict()
    ips = dict(all_ipv4_addresses=[], all_ipv6_addresses=[])

    # Media type ether
    words = ['media:','Ethernet','autoselect','(1000baseT)','status:','active']
    GenericBsdIfconfigNetwork.parse_media_line(None, words, current_if, ips)
    assert current_if['media'] == words[1]
    assert current_if['media_select'] == words[2]
    assert current_if['media_type'] == words[3][1:]
    assert current_if['media_options'] == []
 
    # Media type unknown
    words = ['media:','10-GigabitEthernet','autoselect','status:','active']
    GenericBsdIfconfigNetwork

# Generated at 2022-06-13 01:28:39.869926
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork

# Generated at 2022-06-13 01:28:52.208032
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():
    module = MagicMock()
    module.get_bin_path.side_effect = lambda x: '/sbin/' + x
    network = GenericBsdIfconfigNetwork(module)


# Generated at 2022-06-13 01:29:27.084739
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():
    assert GenericBsdIfconfigNetwork.merge_default_interface(
        { 'interface' : 'lo0' },
        { 'lo0' : { 'ipv6' : [ { 'address' : '::1' } ] } },
        'ipv6') == {
            'interface' : 'lo0',
            'address' : '::1'
        }
    assert GenericBsdIfconfigNetwork.merge_default_interface(
        { 'interface' : 'lo0' },
        { 'lo0' : { 'ipv6' : [ { 'address' : '::1' } ] } },
        'ipv4') == { 'interface' : 'lo0' }



# Generated at 2022-06-13 01:29:34.207378
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():

    module = AnsibleModule(
        argument_spec = dict(),
        supports_check_mode = True
    )

    # get the ifconfig output
    rdata = open(os.path.join(fixture_path, 'output/ifconfig.out')).read()
    rc = 0
    err = ''
    ipout = open(os.path.join(fixture_path, 'output/ip-addr.out')).read()

    def run_command(self, args, check_rc=True):
        return (rc, rdata, err)

    def get_bin_path(self, arg):
        return arg

    module.run_command = run_command
    module.get_bin_path = get_bin_path

    n = GenericBsdIfconfigNetwork(module)

    data = n.populate()

   

# Generated at 2022-06-13 01:29:46.728957
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():
    from ansible_collections.notstdlib.moveitallout.tests.units.compat.mock import Mock
    from ansible_collections.notstdlib.moveitallout.tests.units.compat.mock import patch

    Mock = Mock()
    patch = patch('ansible_collections.notstdlib.moveitallout.plugins.module_utils.facts.networking.generic_bsd_ifconfig.GenericBsdIfconfigNetwork.get_default_interfaces', return_value=('v4','v6'))
    patch = patch('ansible_collections.notstdlib.moveitallout.plugins.module_utils.facts.networking.generic_bsd_ifconfig.GenericBsdIfconfigNetwork.get_interfaces_info', return_value=('interfaces','ips'))
    patch = patch

# Generated at 2022-06-13 01:29:54.409914
# Unit test for method parse_inet_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet_line():
    module = AnsibleModuleMock(ifconfig_path="/sbin/ifconfig")
    ifconfig = GenericBsdIfconfigNetwork(module)

    assert ifconfig.parse_inet_line(['inet', '10.0.0.2', 'netmask', '255.255.255.0', 'broadcast','10.0.0.255'], {}, {'all_ipv4_addresses':[]}) == {'broadcast': '10.0.0.255', 'address': '10.0.0.2', 'netmask': '255.255.255.0', 'network': '10.0.0.0'}, "Test failed: parse_inet_line returned unexpected ipv4 address."


# Generated at 2022-06-13 01:29:59.826609
# Unit test for method detect_type_media of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_detect_type_media():
    network = GenericBsdIfconfigNetwork(None)

    interfaces = {'lo0': {'media': 'ether', 'device': 'lo0'},
                  'vtnet0': {'media': 'ether', 'device': 'vtnet0'},
                  'en0': {'media': 'ether', 'device': 'en0'},
                  'iwm0': {'media': '', 'device': 'iwm0'},
                  'vlan0': {'media': 'ethernet autoselect (1000baseT <full-duplex>)', 'device': 'vlan0'}}
    result = network.detect_type_media(interfaces)

# Generated at 2022-06-13 01:30:08.583674
# Unit test for method parse_media_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_media_line():
    generic_bsd_ifconfig = GenericBsdIfconfigNetwork()
    current_if = dict()
    ips = dict(all_ipv4_addresses=[], all_ipv6_addresses=[])

# Generated at 2022-06-13 01:30:12.885034
# Unit test for method get_options of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_options():
    x = GenericBsdIfconfigNetwork()
    option_string = 'type something? <some,options,some,where>'
    result = x.get_options(option_string)
    if result != ['some', 'options', 'some', 'where']:
        raise Exception('Option type parsing is broken')



# Generated at 2022-06-13 01:30:23.012642
# Unit test for method parse_media_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_media_line():
    # Initialize the class object
    genBsdNet = GenericBsdIfconfigNetwork()

    # Initialize the test data
    current_if = {'device':'test0', 'ipv4': [], 'ipv6': [], 'type': 'unknown'}
    words = ["media:", "Ethernet", "autoselect", "(1000baseT)", "status:", "active"]

    # Call the method and verify the results
    genBsdNet.parse_media_line(words, current_if, {})
    assert current_if['media'] == words[1]
    assert current_if['media_select'] == words[2]
    assert current_if['media_type'] == words[3][1:]
    assert current_if['media_options'] == ['1000baseT']



# Generated at 2022-06-13 01:30:30.974309
# Unit test for method parse_media_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_media_line():
    '''Test for method parse_media_line of class GenericBsdIfconfigNetwork'''
    module = ansible_module_mock()
    n = GenericBsdIfconfigNetwork(module)
    current_if = {}
    n.parse_media_line(['media:','Ethernet','10baseT/UTP','<link>','loopback','flowcontrol','autoselect'], 
        current_if, None)
    assert current_if['media'] == 'Ethernet'
    assert current_if['media_select'] == '10baseT/UTP'
    assert current_if['media_type'] == 'link'
    assert current_if['media_options'] == ['loopback', 'flowcontrol', 'autoselect']
    assert isinstance(current_if, dict)
    assert 'media' in current_if

# Generated at 2022-06-13 01:30:41.819370
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():
    # work with a copy of the class
    module = GenericBsdIfconfigNetwork()

    # dict of results from module.run_command

# Generated at 2022-06-13 01:30:59.747676
# Unit test for method parse_inet6_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet6_line():
    """test_GenericBsdIfconfigNetwork_parse_inet6_line"""
    iface = {}
    ips = {}
    module = AnsibleModule(argument_spec=dict())
    SocketPatch.setattr(socket, 'has_ipv6', True)
    network = GenericBsdIfconfigNetwork(module)
    network.parse_inet6_line(
        ['inet6', 'fe80::b6fa:d6ff:fed6:b1bb', 'prefixlen', '64', 'scopeid', '0x2'],
        iface,
        ips)
    assert iface == {'ipv6': [{'address': 'fe80::b6fa:d6ff:fed6:b1bb',
                               'prefix': '64',
                               'scope': '0x2'}]}




# Generated at 2022-06-13 01:31:11.750622
# Unit test for method parse_inet6_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet6_line():

    # Arrange
    mock_module = Mock()
    mock_module.run_command.return_value = (0, '', '')

    network_module = GenericBsdIfconfigNetwork(mock_module)

    words = ['inet6', 'fe80::1%lo0', 'prefixlen', '64', 'scopeid', '0x1', '', '', '']
    ips = dict(all_ipv6_addresses=[])
    current_if = dict(ipv4=[], ipv6=[])

    # Act
    network_module.parse_inet6_line(words, current_if, ips)

    # Assert
    assert ips['all_ipv6_addresses'] == ['fe80::1%lo0']
    assert len(current_if['ipv6']) == 1
   

# Generated at 2022-06-13 01:31:15.945217
# Unit test for method parse_ether_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_ether_line():
    from ansible.module_utils.network.common.ifconfig import GenericBsdIfconfigNetwork
    from ansible.module_utils.facts.network.base import NetworkCollector
    nc = NetworkCollector(GenericBsdIfconfigNetwork)
    nc.populate()
    assert nc.facts['default_ipv6']['macaddress'] == '52:54:00:12:34:33'

# Generated at 2022-06-13 01:31:22.327464
# Unit test for method get_interfaces_info of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_interfaces_info():
    from ansible.module_utils.network import get_module
    module = get_module(argument_spec={'gather_subset': {'choices': ['all']}, 'gather_network_resources': {'default': ['all'], 'type': 'list'}})

    generic_bsd_ifconfig_network = GenericBsdIfconfigNetwork(module)

    generic_bsd_ifconfig_network.get_interfaces_info(ifconfig_path='/tmp/ifconfig', ifconfig_options='-a')

# Generated at 2022-06-13 01:31:29.828087
# Unit test for method parse_inet6_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet6_line():
    test_host = GenericBsdIfconfigNetwork()
    interface = {}
    ips = dict(
        all_ipv4_addresses=[],
        all_ipv6_addresses=[],
    )
    test_host.parse_inet6_line(['inet6', 'fe80::1%lo0',
                                'prefixlen', '64',
                                'scopeid', '0x1'],
                               interface, ips)
    assert interface['ipv6'][0]['address'] == 'fe80::1%lo0'
    assert interface['ipv6'][0]['prefix'] == '64'
    assert interface['ipv6'][0]['scope'] == '0x1'
    assert len(ips['all_ipv6_addresses']) == 1

# Generated at 2022-06-13 01:31:41.355831
# Unit test for method parse_inet6_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet6_line():
    # generate a fake class instance to pass to ifconfig
    class FakeModule:
        def __init__(self):
            self.result = dict()
        def get_bin_path(self, *args):
            return 'path'
        def run_command(self, *args):
            return 0, '', ''
    fake_instance = GenericBsdIfconfigNetwork(FakeModule())

    # test the function
    words = 'fe80::1%lo0 prefixlen 64 scopeid 0x2'.split()
    current_if = dict()
    ips = dict()
    fake_instance.parse_inet6_line(words, current_if, ips)

# Generated at 2022-06-13 01:31:52.421757
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():
    results = GenericBsdIfconfigNetwork.populate(GenericBsdIfconfigNetwork)
    assert 'interfaces' in results
    assert sorted(results['interfaces']) == ['em0', 'lo0', 'vlan0']
    assert 'default_ipv4' in results
    assert 'broadcast' in results['default_ipv4']
    assert 'network' in results['default_ipv4']
    assert 'address' in results['default_ipv4']
    assert 'netmask' in results['default_ipv4']
    assert 'em0' in results
    assert 'type' in results['em0']
    assert results['em0']['type'] == 'ether'
    assert 'macaddress' in results['em0']

# Generated at 2022-06-13 01:31:59.955690
# Unit test for method get_interfaces_info of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_interfaces_info():
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True)
    network_module = GenericBsdIfconfigNetwork(module)
    interfaces, ips = network_module.get_interfaces_info(ifconfig_path=readdata('ifconfig_path'))

# Generated at 2022-06-13 01:32:09.640969
# Unit test for method get_interfaces_info of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_interfaces_info():
    import tempfile


# Generated at 2022-06-13 01:32:18.570448
# Unit test for method parse_media_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_media_line():
    class MockModule(object):
        # FIXME: this should not be a function so we can do some assertions about it
        def run_command(self, command):
            pass
        def get_bin_path(self, command):
            pass

    class MockIfconfig(object):
        def __init__(self):
            self.module = MockModule()
            self.current_if = {}

    obj = GenericBsdIfconfigNetwork(MockIfconfig())
    obj.parse_media_line(['media:', 'Ethernet', '10Gbase-SR', '(0x11)'], obj.current_if, {})
    assert obj.current_if['media'] == "Ethernet"
    assert obj.current_if['media_type'] == "10Gbase-SR"

# Generated at 2022-06-13 01:32:32.956755
# Unit test for method parse_inet_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet_line():
    module = AnsibleModule(argument_spec={})
    network = GenericBsdIfconfigNetwork(module)
    current_if = {}
    ips = dict(
        all_ipv4_addresses=[],
        all_ipv6_addresses=[],
    )

    for test in test_parse_inet_line:
        network.parse_inet_line(test[0], current_if, ips)
        assert current_if == test[1]
        assert ips == test[2]

# Generated at 2022-06-13 01:32:41.378641
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_default_interfaces():
    import io
    import pprint
    from ansible_collections.os_migrate.os_migrate.plugins.module_utils import network

    test_example1 = (
        "default via 192.0.2.1 dev eth2 proto static metric 100\n"
        "default via 198.51.100.1 dev eth1 proto static metric 100\n"
        "default via 2001:db8:100::1 dev eth1 proto static metric 100\n"
    )

    test_example2 = (
        "default via 2001:db8:100::1 dev eth1 proto static metric 100\n"
        "default via 198.51.100.1 dev eth1 proto static metric 100\n"
        "default via 192.0.2.1 dev eth2 proto static metric 100\n"
    )


# Generated at 2022-06-13 01:32:49.795503
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():
    m = MockModule()
    defaults = dict(interface='em0', gateway="192.168.0.1", address="192.168.0.10")
    interfaces = dict(em0=dict(device='em0', ipv4=[ dict(address="192.168.0.10") ], ipv6=[],
                               type='ether', metric='0', mtu='1500', macaddress='00:c0:f0:0c:0c:0c', options=[], status="active"))
    gbi = GenericBsdIfconfigNetwork(m)
    gbi.merge_default_interface(defaults, interfaces, 'ipv4')

# Generated at 2022-06-13 01:32:59.453335
# Unit test for method parse_inet_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet_line():
    module = AnsibleModule(argument_spec={})
    network = GenericBsdIfconfigNetwork(module)

    # netbsd show aliases like this
    #  lo0: flags=8049<UP,LOOPBACK,RUNNING,MULTICAST> mtu 33184
    #         inet 127.0.0.1 netmask 0xff000000
    #         inet alias 127.1.1.1 netmask 0xff000000
    current_if = {'device': 'lo0', 'ipv4': [], 'ipv6': [], 'mtu': '33184', 'type': 'unknown', 'flags': ['UP', 'LOOPBACK', 'RUNNING', 'MULTICAST']}

# Generated at 2022-06-13 01:33:09.591164
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_default_interfaces():
    g = GenericBsdIfconfigNetwork()
    g._run_command = _mock_run_command
    result = g.get_default_interfaces('route')
    assert result[0] == {'interface': 'gif0', 'gateway': '192.168.205.1', 'address': '192.168.205.1'}, "Default interface for IPv4 incorrect"
    assert result[1] == {'interface': 'gif0', 'gateway': '2001:db8::2', 'address': '2001:db8::2'}, "Default interface for IPv6 incorrect"


# Generated at 2022-06-13 01:33:10.615602
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_default_interfaces():
    pass



# Generated at 2022-06-13 01:33:17.248258
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():
    from ansible_collections.notstdlib.moveitallout.tests.unit.compat import unittest
    from ansible_collections.notstdlib.moveitallout.plugins.module_utils import basic
    from ansible_collections.notstdlib.moveitallout.plugins.module_utils.network.common.utils import dict_merge

    module = basic.AnsibleModule(
        argument_spec=dict(),
    )

    class MyGenericBsdIfconfigNetwork(GenericBsdIfconfigNetwork):
        @staticmethod
        def get_default_interfaces(route_path):
            return {
                'interface': 'lo0',
                'address': '127.0.0.1',
            }, None


# Generated at 2022-06-13 01:33:29.018334
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():
    from ansible.module_utils.network.common.network import Network
    from ansible.module_utils.network.common.utils import dict_merge

    class Facts(dict):
        def __init__(self):
            super(Facts, self).__init__()
            self['default_ipv4'] = dict(test='test_val')
            self['default_ipv6'] = dict(test='test_val')
            self['interfaces'] = []
            self['all_ipv4_addresses'] = []
            self['all_ipv6_addresses'] = []

    class args:
        def __init__(self):
            self.connection = 'network_cli'
            self.provider = None

    class Module:
        def __init__(self):
            self.params = dict()
           

# Generated at 2022-06-13 01:33:39.867563
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_default_interfaces():
    # create instance of class
    test_obj = GenericBsdIfconfigNetwork()
    # use this to pass mock object as route_path to get_default_interfaces method
    test_obj.module = Mock()
    # create mock object of route_path
    route_path = test_obj.module
    # mock side_effect of method get_bin_path so that it returns route_path
    route_path.get_bin_path.side_effect = lambda cmd: route_path
    # mock side_effect of method run_command so it returns the data required for the test

# Generated at 2022-06-13 01:33:50.060888
# Unit test for method get_interfaces_info of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_interfaces_info():
    module = AnsibleModule(argument_spec={})
    ifconfig_network = GenericBsdIfconfigNetwork(module)
    ifconfig_path = module.get_bin_path('ifconfig')

    rc, out, err = module.run_command([ifconfig_path, '-a'])
    ret = ifconfig_network.get_interfaces_info(ifconfig_path)

    # test return type
    assert isinstance(ret, tuple), "Unexpected return type"
    assert isinstance(ret[0], dict)
    assert isinstance(ret[1], dict)

    # test return length
    assert len(ret) == 2, "Unexpected return length"
    assert len(ret[0]) > 0, "Did not receive any interface information"
    assert len(ret[1]) > 0, "Did not receive any address information"

# Generated at 2022-06-13 01:34:05.550434
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_default_interfaces():
    method = GenericBsdIfconfigNetwork.get_default_interfaces
    cmd = dict(v4='route -n get default',
               v6='route -n get -inet6 default')
    out = dict(v4='',
               v6='''route: writing to routing socket: Invalid argument
       route: write returned: Invalid argument
       route: writing to routing socket: Invalid argument
       route: write returned: Invalid argument
       route to: default
        route via: fe80::1%lo0
       destination: default
            mask: default
      interface: lo0
         gateway: ::1''')

    # No IPv4 or IPv6 routes
    interfaces = dict(v4=dict(),
                      v6=dict())
    route_path = '/sbin/route'
    result = method(route_path)

# Generated at 2022-06-13 01:34:16.957802
# Unit test for method parse_media_line of class GenericBsdIfconfigNetwork

# Generated at 2022-06-13 01:34:25.716551
# Unit test for method get_interfaces_info of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_interfaces_info():
    with open(GENERIC_BSD_IFCONFIG_INPUT) as f:
        test_data = f.read()

    class Options:
        def __init__(self, bin_path=None):
            self.bin_path = bin_path
    options = Options()

    class Test:
        def __init__(self, ifconfig_path, bin_path=None):
            self.ifconfig_path = ifconfig_path
            self.bin_path = bin_path

        def get_bin_path(self, binary):
            if binary == 'ifconfig':
                return self.ifconfig_path
            else:
                raise Exception("Unexpected binary used: %s" % binary)


# Generated at 2022-06-13 01:34:33.687476
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():
    defaults = dict(interface='lo0')
    interfaces = dict(
        lo0=dict(
            ipv4=[
                dict(address='127.0.0.1')],
            ipv6=[
                dict(address='::1')]))

    GenericBsdIfconfigNetwork().merge_default_interface(defaults, interfaces, 'ipv4')
    assert defaults['address'] == '127.0.0.1'
    assert defaults['interface'] == 'lo0'

    defaults = dict(interface='eth0')
    interfaces = dict(
        eth0=dict(
            ipv4=[
                dict(address='10.0.0.100'),
                dict(address='10.0.55.55')],
            ipv6=[
                dict(address='::1')]))

    GenericBsdIfconfig

# Generated at 2022-06-13 01:34:39.229661
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():
    default = dict(interface='test', address='test_test')
    iface = {'test': dict(ipv4=[dict(address='test_test')], ipv6=[])}
    actual = GenericBsdIfconfigNetwork().merge_default_interface(default, iface, 'ipv4')
    assert actual == None


# Generated at 2022-06-13 01:34:42.427215
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():
    """Test GenericBsdIfconfigNetwork.populate"""
    module = AnsibleModule(argument_spec=dict())
    network = GenericBsdIfconfigNetwork(module)
    network.populate()


# Generated at 2022-06-13 01:34:52.138803
# Unit test for method parse_inet6_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_inet6_line():
    # Simple test to check the output of parse_inet6_line of
    # GenericBsdIfconfigNetwork
    test_inst = GenericBsdIfconfigNetwork()
    words = ['inet6', 'fe80::1%lo0', 'prefixlen', '64', 'scopeid', '0x2' ]
    current_if = {'device': 'lo0', 'ipv4': [], 'ipv6': [], 'type': 'unknown'}
    ips = dict(
        all_ipv4_addresses=[],
        all_ipv6_addresses=[],
    )
    test_inst.parse_inet6_line(words, current_if, ips)
    # Check the output
    assert current_if['ipv6'][0]['address'] == 'fe80::1%lo0'

# Generated at 2022-06-13 01:35:02.579686
# Unit test for method parse_ether_line of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_parse_ether_line():
    test_class = GenericBsdIfconfigNetwork()
    current_if = dict()
    words = ['lo0:', 'flags=8049<UP,LOOPBACK,RUNNING,MULTICAST>',
      'metric', '0', 'mtu', '33184', 'options=680003<RXCSUM,TXCSUM,LINKSTATE,RXCSUM_IPV6,TXCSUM_IPV6>',
      'ether', '00:00:00:00:00:00', 'hwtype', '0', 'lladdr', '00:00:00:00:00:00']
    test_class.parse_interface_line(words)
    test_class.parse_ether_line(words, current_if)

# Generated at 2022-06-13 01:35:09.744429
# Unit test for method get_interfaces_info of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_interfaces_info():
    network = GenericBsdIfconfigNetwork()


# Generated at 2022-06-13 01:35:16.624818
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_default_interfaces():
    generic_bsd_ifconfig_network = GenericBsdIfconfigNetwork(None)
    ipv4 = {'interface': 'en0', 'gateway': '192.0.2.2'}
    ipv6 = {'interface': 'en1', 'gateway': '2001:db8::2'}
    with patch.object(generic_bsd_ifconfig_network, 'get_default_interfaces') as mock_get_default_interfaces:
        mock_get_default_interfaces.return_value = (ipv4, ipv6)
        assert (mock_get_default_interfaces.return_value == (ipv4, ipv6))


# Generated at 2022-06-13 01:36:39.169909
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_default_interfaces():
    # Check FreeBSD output
    route_path = '/sbin/route'
    route_v4 = [route_path, '-n', 'get', 'default']
    route_v6 = [route_path, '-n', 'get', '-inet6', 'default']
    test_route_v4_out = b"default: gateway: 172.16.1.1 interface: em0 " \
                        b"if address: 172.16.1.34 local addr: 172.16.1.34"

# Generated at 2022-06-13 01:36:45.315658
# Unit test for method get_options of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_options():
    assert GenericBsdIfconfigNetwork.get_options('<UP,BROADCAST,RUNNING,PROMISC>') == ['UP', 'BROADCAST', 'RUNNING', 'PROMISC']
    assert GenericBsdIfconfigNetwork.get_options('<NOARP>') == ['NOARP']
    assert GenericBsdIfconfigNetwork.get_options('NOARP>') == []
    assert GenericBsdIfconfigNetwork.get_options('<NOARP') == []

# Generated at 2022-06-13 01:36:52.318104
# Unit test for method populate of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_populate():
    temp = {'_ansible_no_log': False,
            '_ansible_verbosity': 4,
            '_ansible_version': '2.6.0',
            '_ansible_module_name': 'GenericBsdIfconfigNetwork',
            '_ansible_debug': True,
            '_ansible_supports_check_mode': True,
            '_ansible_check_mode': False,
            '_ansible_module_generated': False,
            'parsed': True
            }

    moduleMock = type('', (), {})()
    moduleMock.params = temp
    moduleMock.get_bin_path = type('', (), {'__call__': lambda self, *args:  '/sbin/ifconfig'})

# Generated at 2022-06-13 01:37:01.372582
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():
    network = GenericBsdIfconfigNetwork()
    defaults = {'interface': 'en0', 'gateway': '10.1.1.1'}
    interfaces = {'en0': {'device': 'en0', 'ipv4': [{'address': '10.1.1.100', 'netmask': '255.255.255.0', 'broadcast': '10.1.1.255', 'network': '10.1.1.0'}]}}
    network.merge_default_interface(defaults, interfaces, 'ipv4')

# Generated at 2022-06-13 01:37:05.313517
# Unit test for method get_default_interfaces of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_get_default_interfaces():
    """get_default_interfaces(self)"""
    # Silly test to get coverage working ...
    test_interface = GenericBsdIfconfigNetwork()
    test_interfaces = test_interface.get_default_interfaces("")
    assert test_interfaces == ({}, {})


# Generated at 2022-06-13 01:37:11.566927
# Unit test for method merge_default_interface of class GenericBsdIfconfigNetwork
def test_GenericBsdIfconfigNetwork_merge_default_interface():
    defaults = dict(interface="tun0", gateway="192.168.1.1")
    interfaces = dict(tun0=dict(device="tun0", ipv4=[dict(address="192.168.1.2")]),
                      wlan0=dict(device="wlan0", ipv4=[dict(address="192.168.1.3")]))
    ip_type = "ipv4"

    print("Testing merge_default_interface() with interface={}, gateway={}, ip_type={}".format(defaults['interface'],
                                                                                                defaults['gateway'],
                                                                                                ip_type))
    ifconfig = GenericBsdIfconfigNetwork()
    ifconfig.merge_default_interface(defaults, interfaces, ip_type)
