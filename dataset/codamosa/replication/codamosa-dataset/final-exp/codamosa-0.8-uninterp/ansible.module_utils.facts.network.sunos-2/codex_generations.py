

# Generated at 2022-06-13 01:48:23.313679
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    obj = SunOSNetworkCollector(None)
    assert obj.platform == 'SunOS'

# Generated at 2022-06-13 01:48:24.681269
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    assert SunOSNetworkCollector._platform == 'SunOS'
    assert SunOSNetworkCollector._fact_class == SunOSNetwork

# Generated at 2022-06-13 01:48:25.884726
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    collector = SunOSNetworkCollector(None)
    assert collector._platform == 'SunOS'
    assert collector._fact_class == SunOSNetwork

# Generated at 2022-06-13 01:48:34.622881
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    module = AnsibleModule(argument_spec={'gather_subset': dict(default=[], type='list')})
    out1 = "lo0: flags=1000849<UP,LOOPBACK,RUNNING,MULTICAST,IPv4> mtu 8232 index 1\n"
    out1 += "        inet 127.0.0.1 netmask ff000000 \n"
    out1 += "hme0: flags=1000843<UP,BROADCAST,RUNNING,MULTICAST,IPv4> mtu 1500 index 2\n"
    out1 += "        inet 192.168.0.10 netmask ffffff00 broadcast 192.168.0.255\n"
    out1 += "        ether 8:0:20:8a:2c:80 \n"

# Generated at 2022-06-13 01:48:45.362198
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    """Unit test of get_interfaces_info."""
    # Solaris can have different FLAGS and MTU for IPv4 and IPv6 on the same interface
    # so these facts have been moved inside the 'ipv4' and 'ipv6' lists.
    platform, ifconfig_path = SunOSNetwork._detect_platform_sunos()
    SunOSNetwork._detect_bsd_variant = lambda x: None
    network_collector = SunOSNetworkCollector()
    network_collector.get_interfaces_info = lambda x: mock_get_interfaces_info(x)
    module = MagicMock()
    network = SunOSNetwork(module)
    result = network.get_interfaces_info(ifconfig_path)

# Generated at 2022-06-13 01:48:46.472484
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    SunOSNetworkCollector()


# Generated at 2022-06-13 01:48:49.833182
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    network_collector = SunOSNetworkCollector()
    assert network_collector
    assert network_collector._fact_class == SunOSNetwork
    assert network_collector._platform == 'SunOS'

# Generated at 2022-06-13 01:48:57.995293
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    interfaces_info = SunOSNetwork.get_interfaces_info(ifconfig_path='/sbin/ifconfig')
    assert len(interfaces_info) == 2
    assert len(interfaces_info[0]) > 0
    assert len(interfaces_info[1]) > 0

    for device in interfaces_info[0]:
        for key in ['device', 'type', 'ipv6', 'ipv4', 'macaddress']:
            assert key in interfaces_info[0][device]
        for v in 'ipv6', 'ipv4':
            for info in interfaces_info[0][device][v]:
                for key in ['flags', 'mtu']:
                    assert key in info



# Generated at 2022-06-13 01:49:09.190420
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():

    module = AnsibleModule(
        argument_spec = dict(
            gather_subset=dict(default=['!all'], type='list')
        ),
        supports_check_mode=True
    )

    # Get SunOSNetwork object
    sunos_network = SunOSNetwork()

    # Create test string data to get_interfaces_info() function

# Generated at 2022-06-13 01:49:19.779460
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():

    ifconfig_path = '/usr/sbin/ifconfig'

# Generated at 2022-06-13 01:49:33.243279
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    # Setup fake module object
    from ansible.module_utils.facts import ansible_facts
    from ansible.module_utils.facts.network import NetworkCollector
    module = ansible_facts.AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )
    # Setup fake ifconfig command line output for Solaris

# Generated at 2022-06-13 01:49:36.470045
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    module = type(str("AnsibleModule"), (object,), {"run_command":lambda *args, **kwargs:("", "", 0)})
    collector = SunOSNetworkCollector(module)
    assert isinstance(collector, SunOSNetworkCollector)

# Generated at 2022-06-13 01:49:47.502833
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    import json
    from ansible.module_utils.facts.network.sunos import SunOSNetwork
    module = AnsibleModule(
        argument_spec=dict(gather_subset=dict(type='list', default=['!all', '!min']))
    )
    ifconfig_path = module.get_bin_path('ifconfig', required=True)
    sn = SunOSNetwork(module)
    interfaces, ips = sn.get_interfaces_info(ifconfig_path)

    interfaces_json = json.dumps(interfaces, indent=2, sort_keys=True)
    ips_json = json.dumps(ips, indent=2, sort_keys=True)
    print(interfaces_json)
    print(ips_json)

# Unit test get_interfaces_info method of SunOSNetwork

# Generated at 2022-06-13 01:49:59.136328
# Unit test for method get_interfaces_info of class SunOSNetwork

# Generated at 2022-06-13 01:50:09.538746
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    import sys
    import os.path
    import pytest

    sys.path.append(os.path.join(os.path.dirname(__file__), 'lib'))
    from ansible_test_utils import TempMockOpen
    from ansible_test_utils import mock_module


# Generated at 2022-06-13 01:50:20.316382
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    """
    Test parsing the output of the ifconfig command from the SunOS platform.
    """
    from ansible.module_utils.facts.network.sunos import SunOSNetwork
    from ansible.module_utils.facts.network import NetworkCollector

    facts_from_file = {'all_ipv4_addresses': ['192.168.1.2', '192.168.1.254'],
                       'all_ipv6_addresses': ['fc00::100', 'fe80::100', 'fc00::1', 'fe80::1']}

# Generated at 2022-06-13 01:50:23.859499
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    mod = type('AnsibleModule', (), {})
    setattr(mod, 'params', {})
    setattr(mod, 'run_command', lambda *_: (0, '', ''))
    fact_class = SunOSNetwork
    SunOSNetworkCollector(mod)

# Generated at 2022-06-13 01:50:35.529605
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    # No 'ip' command in Solaris. Use location of ifconfig from facts cache.
    ifconfig_path = '/sbin/ifconfig'
    # Ifconfig output from Solaris 11.3

# Generated at 2022-06-13 01:50:38.639614
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    assert SunOSNetworkCollector.platform == 'SunOS'
    assert SunOSNetworkCollector._fact_class == SunOSNetwork
    assert SunOSNetworkCollector._platform == 'SunOS'


# Generated at 2022-06-13 01:50:50.293860
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    from ansible.module_utils.facts.network.sunos import SunOSNetwork
    from ansible.module_utils.facts.network.sunos import SunOSNetworkCollector

    # Create a SunOSNetwork object to test
    sunos_net_obj = SunOSNetwork(dict(module=object()))

    # Create a SunOSNetworkCollector object to test
    sunos_net_coll_obj = SunOSNetworkCollector(dict(module=object()))

    # test Solaris output with mixed IPv4 and IPv6 interfaces

# Generated at 2022-06-13 01:51:10.228920
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():

    # Test data to use as input to 'get_interfaces_info' method.
    # This data is a string representing the output of 'ifconfig -a' on
    # OpenIndiana Hipster 3.13, illumos shared ZFS pool, running in VirtualBox
    # on macOS 10.12 (Sierra) client.
    test_data = """lo0: flags=2001000849<UP,LOOPBACK,RUNNING,MULTICAST,IPv4,VIRTUAL> mtu 8232 index 1\
        inet 127.0.0.1 netmask ff000000\
        options=3<RXCSUM,TXCSUM>\
        nd6 options=1<PERFORMNUD>""".splitlines()

    # Construct a SunOSNetwork class with the test input data.
    iface = SunOSNetwork()

    #

# Generated at 2022-06-13 01:51:17.200373
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    m = SunOSNetworkCollector()
    assert isinstance(m._fact_class, SunOSNetwork)
    assert m._platform == 'SunOS'
    assert m._fact_class.platform == 'SunOS'
    assert m._fact_class.collector == 'SunOSNetworkCollector'
    assert m._fact_class.get_interfaces_info.__doc__ == SunOSNetwork.get_interfaces_info.__doc__

# Generated at 2022-06-13 01:51:23.529415
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    """
    This is a unit test for constructor of class SunOSNetworkCollector
    with following conditions
        - No input
        - Default: _platform = 'SunOS'
    """

    expected_platform = 'SunOS'
    expected_fact_class = SunOSNetwork

    collector = SunOSNetworkCollector()

    assert collector._platform == expected_platform
    assert collector._fact_class == expected_fact_class

# Generated at 2022-06-13 01:51:25.568339
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    assert(SunOSNetworkCollector._platform == 'SunOS')
    assert(SunOSNetworkCollector._fact_class == SunOSNetwork)

# Generated at 2022-06-13 01:51:29.558741
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
  module = AnsibleModule(argument_spec={})
  module.run_command = MagicMock(return_value=(0, '', ''))
  ip = SunOSNetwork()
  ip._hostname = "hostname"
  ip._module = module
  # It uses the GenericBsdIfconfigNetwork get_interfaces_info.
  # It has not been implemented yet a unit test for the Solaris ifconfig.
  ip.get_interfaces_info()

# Generated at 2022-06-13 01:51:32.186098
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    obj = SunOSNetworkCollector()
    assert obj._fact_class.platform == "SunOS"


# Generated at 2022-06-13 01:51:35.264325
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    os_facts = {}
    os_facts['distribution'] = 'SunOS'
    SunOSNetworkCollector(os_facts, None)


# Generated at 2022-06-13 01:51:38.115013
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    obj = SunOSNetworkCollector()
    assert obj._fact_class == SunOSNetwork
    assert obj._platform == 'SunOS'

# Generated at 2022-06-13 01:51:47.609130
# Unit test for method parse_interface_line of class SunOSNetwork
def test_SunOSNetwork_parse_interface_line():
    facts = SunOSNetwork()
    facts.parse_interface_line(['lo0:', 'flags=2001000849', 'mtu', '8232'], {}, {})
    assert facts.parse_interface_line(['lo0:', 'flags=2001000849', 'mtu', '8232'], {}, {}) == {
        'device': 'lo0',
        'ipv4': [{'mtu': '8232', 'flags': ['IPv6', 'Loopback', 'Multicast', 'Running']}],
        'ipv6': [],
        'macaddress': 'unknown',
        'type': 'loopback',
    }

# Generated at 2022-06-13 01:51:49.472577
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    facts__network = SunOSNetworkCollector()
    assert facts__network._fact_class._platform == 'SunOS'


# Generated at 2022-06-13 01:52:12.982721
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    module = DummyAnsibleModule()
    module.run_command = MagicMock(return_value=get_ifconfig_return_values())
    sut = SunOSNetwork(module)
    (interfaces, ips) = sut.get_interfaces_info("/usr/sbin/ifconfig")

    # Check returned data structure
    expected_interfaces = get_expected_interfaces_for_test_get_interfaces_info()
    assert interfaces == expected_interfaces

    # Check 'ips' data structure
    expected_ips = get_expected_ips_for_test_get_interfaces_info()
    assert ips == expected_ips



# Generated at 2022-06-13 01:52:16.666817
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    assert SunOSNetworkCollector._platform == 'SunOS'
    assert type(SunOSNetworkCollector._fact_class) == type
    assert SunOSNetworkCollector._fact_class.__name__ == 'SunOSNetwork'
    assert SunOSNetworkCollector._fact_class.platform == 'SunOS'

# Generated at 2022-06-13 01:52:18.116725
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    assert SunOSNetworkCollector._platform == 'SunOS'
    assert SunOSNetworkCollector._fact_class == SunOSNetwork

# Generated at 2022-06-13 01:52:19.346829
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    SunOSNetworkCollector(None)

# Generated at 2022-06-13 01:52:25.926797
# Unit test for method parse_interface_line of class SunOSNetwork
def test_SunOSNetwork_parse_interface_line():
    interface = SunOSNetwork()
    interfaces = {}
    current_if = {}

    # Checking for 'ipv4'
    words = ['lo0:', 'flags=2001000849<UP,LOOPBACK,RUNNING,MULTICAST,IPv4,VIRTUAL>', 'mtu', '8232']
    current_if = interface.parse_interface_line(words, current_if, interfaces)
    assert current_if['device'] == 'lo0'
    assert current_if['ipv4'][0]['flags'] == '2001000849<UP,LOOPBACK,RUNNING,MULTICAST,IPv4,VIRTUAL>'
    assert current_if['ipv4'][0]['mtu'] == '8232'
    assert current_if['ipv6'] == []


# Generated at 2022-06-13 01:52:36.527255
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    # Create a SunOSNetwork object
    sunos_network = SunOSNetwork({})

    # Create a sample output of 'ifconfig -a'

# Generated at 2022-06-13 01:52:46.823215
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    """
    This is a functional test of the method 'get_interfaces_info'
    of class SunOSNetwork
    """
    module = AnsibleModule(argument_spec={})
    module.exit_json = lambda x: x
    mocker = Mocker()
    mock_cmd = mocker.replace('ansible.module_utils.facts.network.generic_bsd.GenericBsdIfconfigNetwork.run_command')
    mock_cmd(ANY, ['/usr/sbin/ifconfig', '-a'])
    mocker.result(None)

# Generated at 2022-06-13 01:52:48.572330
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    module = AnsibleModuleMock()
    n = SunOSNetworkCollector(module)
    assert n.module == module

# Generated at 2022-06-13 01:52:49.514408
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    SunOSNetworkCollector()

# Generated at 2022-06-13 01:52:51.098583
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    assert SunOSNetworkCollector._platform == 'SunOS'
    assert SunOSNetworkCollector._fact_class == SunOSNetwork

# Generated at 2022-06-13 01:53:25.675931
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    facts = SunOSNetworkCollector().collect()
    assert 'SunOS' in facts['network']['platform']
    assert 'lo0' in facts['network']['interfaces']
    assert 'inet' in facts['network']['interfaces']['lo0']['ipv4'][0]
    assert 'mtu' in facts['network']['interfaces']['lo0']['ipv4'][0]
    assert 'netmask' in facts['network']['interfaces']['lo0']['ipv4'][0]
    assert 'ether' in facts['network']['interfaces']['lo0']

# Generated at 2022-06-13 01:53:32.203982
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    mock_module = None
    mock_collector = {'_NetworkCollector__ifconfig': 'ifconfig'}
    mock_class = {'platform': 'SunOS'}
    network_collector = SunOSNetworkCollector(mock_module, mock_collector, mock_class)
    assert network_collector._fact_class.platform == 'SunOS'
    assert network_collector._platform == 'SunOS'

# Generated at 2022-06-13 01:53:37.349557
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    """
    Test constructor of class SunOSNetworkCollector
    """
    _platform = 'SunOS'
    _fact_class = SunOSNetwork
    network_collector = SunOSNetworkCollector(_platform, _fact_class)
    assert network_collector._platform == 'SunOS'
    assert network_collector._fact_class == SunOSNetwork

# Generated at 2022-06-13 01:53:48.246337
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    '''
    Unit test for method get_interfaces_info of class SunOSNetwork
    '''
    # This ifconfig -a output is from a x86 Solaris 11.4 VM
    # The MAC address in the output looks like a VMware MAC but is not.

# Generated at 2022-06-13 01:53:50.770292
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    assert issubclass(SunOSNetwork, NetworkCollector), "Class SunOSNetwork should be subclass of NetworkCollector"
    assert issubclass(SunOSNetworkCollector, NetworkCollector), "Class SunOSNetworkCollector should be subclass of NetworkCollector"

# Generated at 2022-06-13 01:53:51.713985
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    assert SunOSNetworkCollector._platform == 'SunOS'

# Generated at 2022-06-13 01:53:55.997731
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    module = FakeAnsibleModule()
    fixtures = load_fixtures('interfaces_ifconfig_a_SunOS')
    collector = SunOSNetwork(module=module)
    interfaces, ips = collector.get_interfaces_info("/sbin/ifconfig")
    assert interfaces == fixtures['interfaces']
    assert ips == fixtures['ips']


# Generated at 2022-06-13 01:54:05.621292
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    """
    This unit test parses the Solaris 'ifconfig -a' output and compares the results.
    """
    from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork
    from ansible_collections.misc.not_a_real_collection.tests.unit.compat import unittest
    from ansible_collections.misc.not_a_real_collection.tests.unit.compat.mock import patch

    class TestGenericBsdIfconfigNetwork(GenericBsdIfconfigNetwork):
        pass

    class TestSunOSNetwork(SunOSNetwork):
        pass

    # input data

# Generated at 2022-06-13 01:54:11.315504
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    module = object()
    facts = object()

    facts_network = SunOSNetworkCollector(module=module, facts=facts).collect()
    assert 'default_ipv4' in facts_network
    assert 'default_ipv6' in facts_network
    assert 'interfaces' in facts_network
    assert 'all_ipv4_addresses' in facts_network
    assert 'all_ipv6_addresses' in facts_network

# Generated at 2022-06-13 01:54:14.610658
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    assert SunOSNetworkCollector.platform == 'SunOS'
    assert SunOSNetworkCollector._fact_class.platform == 'SunOS'


# Generated at 2022-06-13 01:55:32.717526
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    from ansible.module_utils.facts.network.sunos.sunos import SunOSNetwork
    c = SunOSNetwork()
    c.module = Mock()
    c.module.run_command.return_value = (0, c.ifconfig_output, '')
    interfaces, ips = c.get_interfaces_info('')
    assert interfaces[c.iface]['ipv4'][0]['mtu'] == '9000'
    assert interfaces[c.iface]['ipv4'][0]['address'] == '172.17.0.2'
    assert interfaces[c.iface]['ipv6'][0]['mtu'] == '1500'

# Generated at 2022-06-13 01:55:44.218001
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    module = FakeModule()
    SunOSNetwork.module = module
    SunOSNetwork.ifconfig_path = 'ifconfig'
    interfaces, ips = SunOSNetwork().get_interfaces_info(SunOSNetwork.ifconfig_path)

    assert interfaces is not None
    assert 'aggr0' in interfaces
    assert interfaces['aggr0']['macaddress'] == '00:0c:29:b6:49:6e'
    assert interfaces['aggr0']['type'] == 'ether'
    assert interfaces['aggr0']['ipv4'][-1]['address'] == '172.16.1.1'
    assert interfaces['aggr0']['ipv4'][-1]['netmask'] == '255.255.255.0'

# Generated at 2022-06-13 01:55:45.267865
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    assert SunOSNetworkCollector._platform == 'SunOS'

# Generated at 2022-06-13 01:55:56.480733
# Unit test for method get_interfaces_info of class SunOSNetwork

# Generated at 2022-06-13 01:56:01.128400
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    # Constructor of class SunOSNetworkCollector should store the value of
    # _fact_class
    sunosNetworkCollector = SunOSNetworkCollector()
    assert sunosNetworkCollector._fact_class == SunOSNetwork
    # Constructor of class SunOSNetworkCollector should store the value of
    # _platform
    assert sunosNetworkCollector._platform == 'SunOS'

# Generated at 2022-06-13 01:56:02.545640
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    network_collector = SunOSNetworkCollector()
    assert network_collector._fact_class is SunOSNetwork
    assert network_collector._platform is 'SunOS'

# Generated at 2022-06-13 01:56:07.369860
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    # pylint: disable=protected-access
    ifconfig_path = '/usr/sbin/ifconfig'


# Generated at 2022-06-13 01:56:19.570539
# Unit test for method parse_interface_line of class SunOSNetwork
def test_SunOSNetwork_parse_interface_line():
    from ansible.module_utils.facts.network.sunos import SunOSNetwork
    interfaces = {}
    current_if = {}
    words = ['net0', 'flags=10201005', 'mtu', '1500', '', 'options=3']
    current_if = SunOSNetwork.parse_interface_line(None, words, current_if, interfaces)
    ifaces_dict = {'ipv4': [{'flags': '10201005', 'mtu': '1500', 'options': '3'}], 'type': 'unknown', 'macaddress': 'unknown'}
    ifaces_dict.update(current_if)

# Generated at 2022-06-13 01:56:29.179899
# Unit test for method get_interfaces_info of class SunOSNetwork

# Generated at 2022-06-13 01:56:32.076995
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    """
    Unit test for SunOSNetworkCollector
    """
    assert SunOSNetworkCollector._platform == 'SunOS'
    assert issubclass(SunOSNetworkCollector._fact_class, NetworkCollector)