

# Generated at 2022-06-13 01:48:24.509234
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    module = AnsibleModuleMock()
    collector = SunOSNetworkCollector.load_collector(module)
    assert collector._platform == 'SunOS'
    assert collector._fact_class == SunOSNetwork
    assert collector.facts == {}


# Generated at 2022-06-13 01:48:32.547444
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    facts = dict()
    module = AnsibleModule(argument_spec=dict())
    module.exit_json = exit_json
    obj = SunOSNetwork(module)
    interfaces, ips = obj.get_interfaces_info(ifconfig_path=obj.get_bin_path('ifconfig', required=True))
    ansible_facts = dict()
    ansible_facts['interfaces'] = interfaces
    ansible_facts['all_ipv4_addresses'] = ips['all_ipv4_addresses']
    ansible_facts['all_ipv6_addresses'] = ips['all_ipv6_addresses']
    facts.update(ansible_facts)

# Generated at 2022-06-13 01:48:43.187498
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():

    test_file_path = os.path.join(os.path.dirname(__file__), 'SunOS.txt')

    with open(test_file_path) as f:
        test_file_output = f.read()

    test_module = GetIfconfigModule()
    test_module.run_command = MagicMock(return_value=(0, test_file_output, None))

    sunos_network_collector = SunOSNetworkCollector(test_module)
    network_facts = sunos_network_collector.get_facts()

    assert 'all_ipv6_addresses' in network_facts['ansible_all_ipv6_addresses']
    assert len(network_facts['ansible_all_ipv6_addresses']['all_ipv6_addresses']) == 2


# Generated at 2022-06-13 01:48:53.944300
# Unit test for method parse_interface_line of class SunOSNetwork
def test_SunOSNetwork_parse_interface_line():
    # test1: Solaris IPv4 and IPv6 facts
    test1_current_if = {}
    test1_interfaces = {}
    test1_words = ['lo0:', 'flags=2001000849<UP,LOOPBACK,RUNNING,MULTICAST,IPv4,VIRTUAL>', 'mtu', '8232', 'index', '1']
    expected_test1_current_if = {
        'device': 'lo0',
        'ipv4': [
            {'flags': 'UP,LOOPBACK,RUNNING,MULTICAST,IPv4,VIRTUAL', 'mtu': '8232'}
        ],
        'ipv6': [],
        'type': 'loopback'
    }

# Generated at 2022-06-13 01:49:04.635260
# Unit test for method get_interfaces_info of class SunOSNetwork

# Generated at 2022-06-13 01:49:12.531211
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    facts = {'module_setup': True}
    mock_module = type('', (), {})()
    mock_module.params = {}
    mock_module.exit_json = exit_json
    mock_module.fail_json = fail_json
    mock_module.run_command = run_command

    m = SunOSNetwork(mock_module)
    interfaces, ips = m.get_interfaces_info('/sbin/ifconfig')
    assert len(interfaces) == 7
    assert 'lo0' in interfaces
    assert 'lo0' in ips['all_ipv4_addresses']
    assert 'lo0' in ips['all_ipv6_addresses']
    assert 'lo0' in ips['interfaces']
    assert 'inet' in ips['interfaces']['lo0']

# Generated at 2022-06-13 01:49:21.491856
# Unit test for method get_interfaces_info of class SunOSNetwork

# Generated at 2022-06-13 01:49:27.489243
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    """Unit test for constructor of class SunOSNetworkCollector"""
    sunos_network = SunOSNetworkCollector()

    # Asserting TypeError
    with pytest.raises(TypeError) as excinfo:
        sunos_network.get_facts()
    assert 'module is required' in str(excinfo.value)

    # Asserting ValueError
    module_mock = MagicMock()
    module_mock.params['gather_subset'] = ['fake']
    with pytest.raises(ValueError) as excinfo:
        sunos_network.get_facts(module=module_mock)
    assert 'invalid gather_subset value' in str(excinfo.value)

# Generated at 2022-06-13 01:49:29.572620
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    collector = SunOSNetworkCollector(None)
    if collector is None:
        raise Exception("Failed to create SunOSNetworkCollector")


# Generated at 2022-06-13 01:49:38.119502
# Unit test for method parse_interface_line of class SunOSNetwork
def test_SunOSNetwork_parse_interface_line():
    test = SunOSNetwork()
    test.module = FakeModule()


# Generated at 2022-06-13 01:49:44.411092
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    collector = SunOSNetworkCollector()
    assert collector.fact_class is SunOSNetwork

# Generated at 2022-06-13 01:49:51.664956
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    testmodule = dict(
        run_command=dict(
            return_value=dict(
                rc=0,
                stdout=open('tests/resources/SunOSNetwork_ifconfig_a').read(),
                stderr='',
            )
        )
    )

# Generated at 2022-06-13 01:49:53.283785
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    assert SunOSNetworkCollector._platform == 'SunOS'
    assert SunOSNetworkCollector._fact_class == SunOSNetwork

# Generated at 2022-06-13 01:49:57.882064
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    module = type('MockedModule', (object,), {})
    module.params = {}

    x = SunOSNetworkCollector(module=module)
    assert x._platform == 'SunOS'

# Generated at 2022-06-13 01:50:08.065061
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    module = AnsibleModuleMock()
    module.run_command = mock.MagicMock(return_value=(0, sunos_ifconfig_output, ''))
    net = SunOSNetwork(module)
    interfaces, ips = net.get_interfaces_info('ifconfig')

    assert interfaces['lo0'] == {
        'ipv4': [{'mtu': '8232', 'flags': ['UP', 'LOOPBACK', 'RUNNING']}],
        'device': 'lo0',
        'macaddress': 'unknown',
        'ipv6': [{'mtu': '8252', 'flags': ['UP', 'LOOPBACK', 'RUNNING', 'IPv6']}],
        'type': 'loopback'
    }

# Generated at 2022-06-13 01:50:11.462442
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    ansible_module = AnsibleModule(argument_spec={})
    test_collector = SunOSNetworkCollector(ansible_module)
    assert test_collector._platform == 'SunOS'
    assert test_collector._fact_class == SunOSNetwork

# Generated at 2022-06-13 01:50:22.027448
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    ifconfig_path = 'test/ansible_module_utils/facts/network/sample_output/ifconfig_sunos'

    ifc_net = SunOSNetwork(dict())
    interfaces, ips = ifc_net.get_interfaces_info(ifconfig_path)

    assert interfaces['lo0']['type'] == 'loopback'
    assert interfaces['lo0']['ipv4'][0]['flags'] == ['UP', 'LOOPBACK', 'RUNNING']
    assert interfaces['lo0']['ipv4'][0]['mtu'] == '8232'

    assert interfaces['hme0']['type'] == 'unknown'

# Generated at 2022-06-13 01:50:32.596412
# Unit test for method parse_interface_line of class SunOSNetwork
def test_SunOSNetwork_parse_interface_line():
    s = SunOSNetwork()
    r = {'device': 'lo0', 'ipv4': [{'flags': ['UP', 'RUNNING', 'LOOPBACK', 'MULTICAST'], 'mtu': '8232'}], 'ipv6': [{'flags': ['UP', 'RUNNING', 'LOOPBACK', 'ROUTER', 'MULTICAST', 'IPv6'], 'mtu': '8252'}], 'type': 'loopback'}
    s.parse_interface_line(['lo0:', 'flags=20010049<UP,LOOPBACK,RUNNING,MULTICAST>', 'mtu', '8232', 'index', '2'], {}, {})
    assert r == s.current_if

# Generated at 2022-06-13 01:50:44.045337
# Unit test for method get_interfaces_info of class SunOSNetwork

# Generated at 2022-06-13 01:50:55.737441
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    import sys
    import tempfile
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts import ansible_collection_ignore_dir

    # Create a temporary directory
    tmpdir = tempfile.mkdtemp(prefix='ansible_test_%s_' % SunOSNetwork.platform)
    # Create a text file in that directory
    fd, path_to_testfile = tempfile.mkstemp(prefix='test_', dir=tmpdir)
    os_file = os.fdopen(fd, 'w')

# Generated at 2022-06-13 01:51:02.513226
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    obj = SunOSNetworkCollector()
    assert obj.platform == 'SunOS'
    obj.get_facts()

# Generated at 2022-06-13 01:51:14.521621
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    from ansible_collections.notmintest.not_a_real_collection.tests.unit.compat.mock import MagicMock
    from ansible_collections.notmintest.not_a_real_collection.tests.unit.compat.mock import patch

    obj = SunOSNetwork()
    obj._module = MagicMock()

# Generated at 2022-06-13 01:51:26.044923
# Unit test for method get_interfaces_info of class SunOSNetwork

# Generated at 2022-06-13 01:51:29.375325
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    sun_os_network_collector = SunOSNetworkCollector()
    assert sun_os_network_collector._platform == 'SunOS'
    assert sun_os_network_collector._fact_class == SunOSNetwork


# Generated at 2022-06-13 01:51:41.523042
# Unit test for method get_interfaces_info of class SunOSNetwork

# Generated at 2022-06-13 01:51:50.131184
# Unit test for method get_interfaces_info of class SunOSNetwork

# Generated at 2022-06-13 01:51:52.984748
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    net_collector = SunOSNetworkCollector()
    assert net_collector._fact_class == SunOSNetwork
    assert net_collector._platform == 'SunOS'

# Generated at 2022-06-13 01:52:02.391329
# Unit test for method parse_interface_line of class SunOSNetwork

# Generated at 2022-06-13 01:52:07.676127
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    module = MockModule()
    network = SunOSNetwork(module=module)

    # Solaris 'ifconfig -a' will print interfaces twice, once for IPv4 and again for IPv6.
    # MTU and FLAGS also may differ between IPv4 and IPv6 on the same interface.
    interfaces, ips = network.get_interfaces_info(
        ifconfig_path='./unit_tests/SunOS/fixtures/ifconfig_a_output.txt'
    )

    #   ppp0: flags=19000843<UP,POINTOPOINT,RUNNING,NOARP,MULTICAST,IPv4> mtu 1500 index 2
    #       inet 191.168.195.126 --> 10.0.0.1 netmask ffffff00
    #   lo0: flags=2001000849<

# Generated at 2022-06-13 01:52:10.626772
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    sunos_network = SunOSNetworkCollector()
    assert sunos_network.platform == 'SunOS'
    assert sunos_network.fact_class.platform == 'SunOS'

# Generated at 2022-06-13 01:52:20.998351
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    sunosNet = SunOSNetworkCollector()
    assert sunosNet._platform == "SunOS"

# Generated at 2022-06-13 01:52:22.259858
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    network_collector_obj = SunOSNetworkCollector()
    assert network_collector_obj._platform == 'SunOS'

# Generated at 2022-06-13 01:52:26.729587
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    """Test creation of SunOSNetworkCollector class"""

    # Test with _platform = SunOS
    obj = SunOSNetworkCollector(None, 'SunOS')
    assert obj

# vim: se ai ts=4 sw=4 et sts=4 ft=python

# Generated at 2022-06-13 01:52:27.326498
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    pass

# Generated at 2022-06-13 01:52:30.569249
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    result = SunOSNetworkCollector()
    assert result.platform == 'SunOS'
    assert result.fact_class.platform == result.platform


# Generated at 2022-06-13 01:52:39.491949
# Unit test for method get_interfaces_info of class SunOSNetwork

# Generated at 2022-06-13 01:52:40.525521
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    SunOSNetworkCollector()

# Generated at 2022-06-13 01:52:42.736191
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    assert SunOSNetworkCollector._platform == 'SunOS'
    assert SunOSNetworkCollector._fact_class._platform == 'SunOS'

# Generated at 2022-06-13 01:52:52.188280
# Unit test for method get_interfaces_info of class SunOSNetwork

# Generated at 2022-06-13 01:52:57.751798
# Unit test for method get_interfaces_info of class SunOSNetwork

# Generated at 2022-06-13 01:53:22.537639
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    hostname = 'testhost'
    ipv4 = {'interface': 'eth0',
            'address': '192.168.1.1',
            'netmask': '255.255.255.0',
            'network': '192.168.1.0'}
    ipv6 = {'interface': 'eth0',
            'address': 'fe80::a00:20ff:fea7:ccea/64',
            'prefix': '64',
            'scope': 'link'}
    module = MockModule()
    sunos_network_collector = SunOSNetworkCollector(module=module,
                                                    conductor=None)
    facts = sunos_network_collector.collect(module, [])['ansible_network_resources']['interfaces']

# Generated at 2022-06-13 01:53:33.302700
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    import tempfile
    module = MockModule()
    module.params = {}
    module.run_command = MockFunction()
    module.run_command.return_value = 0, get_ifconfig_data(), ''
    network = SunOSNetwork()
    network.module = module
    ifconfig_path = '/sbin/ifconfig'
    interfaces, ips = network.get_interfaces_info(ifconfig_path)

# Generated at 2022-06-13 01:53:44.435262
# Unit test for method parse_interface_line of class SunOSNetwork
def test_SunOSNetwork_parse_interface_line():
    fact_module = SunOSNetwork()
    test_word_1 = ['lo0:', 'flags=2001000849', 'mtu', '8232']
    test_words = test_word_1
    test_current_if = {}
    test_interfaces = {}
    correct_result = {'device': 'lo0',
                      'ipv4': [{'flags': '2001000849', 'mtu': '8232'}],
                      'ipv6': [],
                      'type': 'loopback',
                      'macaddress': 'unknown'}
    result = fact_module.parse_interface_line(test_words, test_current_if, test_interfaces)
    assert result == correct_result, "SunOSNetwork.parse_interface_line() test_word_1 failed."

    test_word_2

# Generated at 2022-06-13 01:53:53.199898
# Unit test for method parse_interface_line of class SunOSNetwork
def test_SunOSNetwork_parse_interface_line():

    test_object = SunOSNetwork({})

    test_object.parse_interface_line(['lo1:', 'flags=1000849<UP,LOOPBACK,RUNNING,MULTICAST,IPv4>', 'mtu', '16384'], {}, {})

# Generated at 2022-06-13 01:54:02.475944
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    interfaces_data = ('bge0: flags=1000843<UP,BROADCAST,RUNNING,MULTICAST,IPv4> mtu 1500 index 3\n'
                       '        inet 127.0.0.1 netmask ff000000 broadcast 127.255.255.255\n'
                       '        ether 0:14:4f:df:2b:c2\n'
                       'bge0: flags=2000842<BROADCAST,RUNNING,MULTICAST,IPv6,VIRTUAL> mtu 1500 index 3\n'
                       '        inet6 fd00::a00:27ff:fe0c:1f2d/64\n'
                       '        ether 0:14:4f:df:2b:c2')
    m = SunOSNetwork()

# Generated at 2022-06-13 01:54:04.807532
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    assert SunOSNetworkCollector.platform == 'SunOS'
    assert SunOSNetworkCollector._platform == 'SunOS'
    assert SunOSNetworkCollector._fact_class.platform == 'SunOS'


# Generated at 2022-06-13 01:54:15.951875
# Unit test for method parse_interface_line of class SunOSNetwork
def test_SunOSNetwork_parse_interface_line():
    platform = 'SunOS'
    module = AnsibleModuleMock()
    on = SunOSNetwork(module=module)

    facts = dict(
        interfaces = dict(),
        current = dict(),
    )
    words = ['lo0:', 'flags=2001000849', 'mtu', '8232']
    expected = dict(
        device = 'lo0',
        type = 'loopback',
        ipv4 = [
            dict(
                flags = ['RUNNING', 'MULTICAST', 'IPv4', 'LOOPBACK', 'ROUTER', 'PRIVATE'],
                mtu = '8232',
            ),
        ],
        ipv6 = [],
        macaddress = 'unknown',
    )

# Generated at 2022-06-13 01:54:21.460230
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    from ansible.module_utils.facts.network.sunos.solaris_network import SunOSNetworkCollector
    from ansible.module_utils.facts.network.sunos.solaris_network import SunOSNetwork
    s = SunOSNetworkCollector()
    assert s.__class__.__name__ == 'SunOSNetworkCollector'

    # Test _fact_class
    assert s._fact_class.__name__ == 'SunOSNetwork'

    # Test _platform
    assert s._platform == 'SunOS'

# Generated at 2022-06-13 01:54:28.155442
# Unit test for method parse_interface_line of class SunOSNetwork
def test_SunOSNetwork_parse_interface_line():
    # make a fake module object
    module = type('', (), {})()
    module.run_command = lambda *args, **kwargs: (0, '', '')
    module.get_bin_path = lambda *args, **kwargs: ''

    # create an instance of the SunOSNetwork class
    sun = SunOSNetwork(module=module)

    # create a fake 'current_if' dict
    current_if = {'device': 'lo0', 'ipv4': [], 'ipv6': [], 'type': 'unknown'}

    # create a fake 'interfaces' dict
    interfaces = {'lo0': current_if}

    # create a fake 'words' list

# Generated at 2022-06-13 01:54:40.369211
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    module = AnsibleModule(
        argument_spec=dict(
            gather_subset=dict(default=[], type='list'),
            gather_network_resources=dict(type='list', default=['all']),
        )
    )

    collector = SunOSNetworkCollector(module)

    facts = collector.get_facts().popitem()[1]

    # ifconfig -a output from Solaris 10.

# Generated at 2022-06-13 01:55:06.122385
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    """ test_SunOSNetwork_get_interfaces_info """
    from ansible.module_utils.facts.network.sunos.test_sunos import TestSunOSNetworkSunOSNetwork
    from ansible.module_utils._text import to_bytes

    this_sunos_network = TestSunOSNetworkSunOSNetwork()
    interfaces, ips = this_sunos_network.get_interfaces_info('/sbin/ifconfig')

    assert interfaces['lo0']['ipv6'][0]['address'] == '::1'
    assert interfaces['lo0']['ipv6'][0]['prefix'] == '128'
    assert interfaces['vlan1']['ipv4'][0]['netmask'] == '255.255.255.0'

# Generated at 2022-06-13 01:55:07.932836
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    os = SunOSNetworkCollector()

    assert os != None
    assert os._fact_class.__name__ == 'SunOSNetwork'

# Generated at 2022-06-13 01:55:12.868712
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    """
    Constructor test.

    This is unit test for constructor. It checks whether it is possible to create
    instance of class SunOSNetworkCollector.

    Returns:
        None

    """
    collector = SunOSNetworkCollector()
    assert isinstance(collector, SunOSNetworkCollector)
    assert collector.platform == 'SunOS'

# Generated at 2022-06-13 01:55:15.248449
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    obj = SunOSNetworkCollector()
    assert obj._fact_class == SunOSNetwork
    assert obj._platform == 'SunOS'


# Generated at 2022-06-13 01:55:24.170480
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    ifconfig_path = 'tests/unit/module_utils/facts/network/solaris_ifconfig_sample'
    interfaces, ips = SunOSNetwork().get_interfaces_info(ifconfig_path)
    assert 'lo0' in interfaces
    assert 'lo0' in interfaces['lo0']
    assert 'ipv4' in interfaces['lo0']
    assert interfaces['lo0']['type'] == 'loopback'
    assert 'lo0' in interfaces
    assert 'lo0' in interfaces['lo0']
    assert 'ipv4' in interfaces['lo0']
    assert interfaces['lo0']['type'] == 'loopback'
    assert 'ipv4' in interfaces['lo0']['ipv4'][0]

# Generated at 2022-06-13 01:55:25.118844
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    SunOSNetworkCollector()

# Generated at 2022-06-13 01:55:31.408933
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    """Unit test for method get_interfaces_info of class SunOSNetwork"""

    # Create an instance of class SunOSNetwork
    obj = SunOSNetwork()

    # Set the value of attribute ifconfig_path
    obj.ifconfig_path = '/sbin/ifconfig'

    # Test the method get_interfaces_info
    test_obj = obj.get_interfaces_info(obj.ifconfig_path)

    # assert for the test result
    assert test_obj is not None

# Generated at 2022-06-13 01:55:33.077027
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    obj = SunOSNetworkCollector()
    assert obj.platform == 'SunOS'
    assert obj.fact_class.platform == 'SunOS'

# Generated at 2022-06-13 01:55:44.516651
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    module = FakeModule()
    ifconfig_path = './unit/library/ansible/module_utils/facts/network/interfaces/sunos/ifconfig'
    network_fact_class = SunOSNetwork(module)
    interfaces, ips = network_fact_class.get_interfaces_info(ifconfig_path)

# Generated at 2022-06-13 01:55:55.773417
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    # Get data from a test file
    output_file = open('test/unit/utils/facts/network/test_SunOSNetwork_data.txt')
    output = output_file.read()
    output_file.close()

    module = AnsibleModule({'gather_network_resources': 'no'})
    NetObj = SunOSNetwork()
    interfaces, ips = NetObj.get_interfaces_info('/sbin/ifconfig')


# Generated at 2022-06-13 01:56:32.716655
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    print('Testing SunOSNetworkCollector')
    module = AnsibleModule(argument_spec={})
    ifc = SunOSNetworkCollector(module)
    assert 'ansible_'+str(ifc._fact_class.platform) in ifc.get_facts(), 'Facts for SunOSNetwork not found'


# Generated at 2022-06-13 01:56:41.064070
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    """
    This test verifies that the output of the method get_interfaces_info() for
    the class SunOSNetwork matches the structure of the fact ansible_interfaces
    """

    from ansible.module_utils.facts.network.sunos import SunOSNetwork
    output_map = SunOSNetwork(dict(module=None)).get_interfaces_info('ifconfig')

    # The following variable contains a dictionary as listed below.
    # The dictionary lists all interfaces, multiple IPv4 and IPv6 addresses per interface.
    # For example:
    # 'bge0': {'device': 'bge0',
    #              'ipv4': [{'address': '10.203.9.85',
    #                        'broadcast': '10.203.15.255',
    #                        'netmask': '255.255.240.

# Generated at 2022-06-13 01:56:42.258914
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    obj = SunOSNetworkCollector()
    obj.collect()


# Generated at 2022-06-13 01:56:44.694078
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    '''Initialize SunOSNetworkCollector() and check if it's an instance of NetworkCollector'''
    c = SunOSNetworkCollector()
    assert isinstance(c, NetworkCollector)


# Generated at 2022-06-13 01:56:55.532438
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    network_facts = SunOSNetwork()

    # Solaris 'ifconfig -a' will print interfaces twice, once for IPv4 and again for IPv6.
    # MTU and FLAGS also may differ between IPv4 and IPv6 on the same interface.
    # 'get_interfaces_info()' returns a dictionary.
    # 'parse_interface_line()' checks for previously seen interfaces before defining
    # 'current_if' so that IPv6 facts don't clobber IPv4 facts (or vice versa).
    interfaces_info = network_facts.get_interfaces_info('/usr/sbin/ifconfig')

    # Possible output of interfaces_info['lo0']['ipv4']
    # [{'flags': ['UP', 'LOOPBACK', 'RUNNING', 'MULTICAST'], 'mtu': '8232'

# Generated at 2022-06-13 01:56:58.811611
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    network_collector = SunOSNetworkCollector()
    assert network_collector._fact_class == SunOSNetwork
    assert network_collector._platform == 'SunOS'

# Generated at 2022-06-13 01:57:08.028253
# Unit test for method get_interfaces_info of class SunOSNetwork

# Generated at 2022-06-13 01:57:16.232193
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    """
    Run unit test for SunOSNetwork.get_interfaces_info(ifconfig_path)
    """
    # ifconfig output for Solaris 11.3

# Generated at 2022-06-13 01:57:18.924261
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    collector = SunOSNetworkCollector()
    assert isinstance(collector, NetworkCollector) and isinstance(collector, SunOSNetworkCollector)
    assert collector.platform == 'SunOS'


# Generated at 2022-06-13 01:57:20.253419
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    print(SunOSNetworkCollector())