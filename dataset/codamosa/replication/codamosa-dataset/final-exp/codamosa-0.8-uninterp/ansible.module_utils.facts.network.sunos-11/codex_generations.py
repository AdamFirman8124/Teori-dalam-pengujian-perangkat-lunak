

# Generated at 2022-06-13 01:48:24.267657
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    assert issubclass(SunOSNetworkCollector._fact_class, SunOSNetwork)
    assert issubclass(SunOSNetworkCollector._fact_class, NetworkCollector)
    assert SunOSNetworkCollector._platform == "SunOS"

# Generated at 2022-06-13 01:48:29.484194
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    result = {}

# Generated at 2022-06-13 01:48:39.825710
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    """Test case for method get_interfaces_info() of class SunOSNetwork"""
    module = AnsibleModule(argument_spec={})
    c = SunOSNetwork(module)

    interfaces, ips = c.get_interfaces_info('/sbin/ifconfig')

    assert 'lo0' in interfaces
    assert 'lo0' not in ips['all_ipv4_addresses']
    assert 'lo0' not in ips['all_ipv6_addresses']
    assert '127.0.0.1' not in ips['all_ipv4_addresses']
    assert interfaces['lo0']['ipv4'][0]['address'] == '127.0.0.1'

# Generated at 2022-06-13 01:48:51.509738
# Unit test for method parse_interface_line of class SunOSNetwork
def test_SunOSNetwork_parse_interface_line():
    words = ['e1000g0:', 'flags=1000843', 'mtu', '1500', 'index', '5']
    current_iface = {'device': 'e1000g0', 'ipv4': [], 'ipv6': [], 'type': 'unknown'}
    interfaces = {'e1000g0': current_iface}
    ips = dict(all_ipv4_addresses=[], all_ipv6_addresses=[])
    sunos_network = SunOSNetwork()
    sunos_network.parse_interface_line(words, current_iface, interfaces)

    assert interfaces['e1000g0']['ipv4'] == [{'flags': ['UP', 'BROADCAST', 'SIMPLEX', 'MULTICAST'], 'mtu': '1500'}]

# Generated at 2022-06-13 01:49:00.140253
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    SunOS_ansible_module = mock.MagicMock()
    SunOS_ansible_module.run_command.return_value = (0, ifconfig_output, None)
    SunOSNetwork_instance = SunOSNetwork(SunOS_ansible_module)

    interfaces, ips = SunOSNetwork_instance.get_interfaces_info("/sbin/ifconfig")

    assert len(interfaces) == 5
    expected_keys = [u'lo0', u'lo1', u'lo2', u'lo3', u'lo4']
    assert sorted(interfaces.keys()) == sorted(expected_keys)

    assert interfaces['lo0']['active'] == True
    assert interfaces['lo0']['device'] == 'lo0'

# Generated at 2022-06-13 01:49:10.420594
# Unit test for method get_interfaces_info of class SunOSNetwork

# Generated at 2022-06-13 01:49:15.112793
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    sunos_network = SunOSNetworkCollector()
    if not isinstance(sunos_network, SunOSNetworkCollector):
        raise AssertionError("Constructor of class SunOSNetworkCollector should return an instance of class SunOSNetworkCollector")



# Generated at 2022-06-13 01:49:19.666856
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    module = None
    if __name__ == '__main__':
        from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork
        sc = SunOSNetworkCollector(module=module)
        assert sc.get_device() == 'em0'
        # assert isinstance(sc.get_device_info(), GenericBsdNetwork)

# Generated at 2022-06-13 01:49:21.770249
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    import ansible.utils.network.SunOSNetwork
    obj = ansible.utils.network.SunOSNetwork.SunOSNetworkCollector()
    assert obj._platform == 'SunOS'

# Generated at 2022-06-13 01:49:28.531098
# Unit test for constructor of class SunOSNetworkCollector

# Generated at 2022-06-13 01:49:34.888866
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    assert SunOSNetworkCollector is not None

# Generated at 2022-06-13 01:49:38.030368
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    c = SunOSNetworkCollector()
    assert c.platform == 'SunOS', 'platform != SunOS'
    assert c._fact_class.platform == 'SunOS', '_fact_class.platform != SunOS'

# Generated at 2022-06-13 01:49:42.886149
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    snnc = SunOSNetworkCollector(None, None)
    assert issubclass(snnc._fact_class, NetworkCollector)
    assert snnc._fact_class.__name__ == 'SunOSNetwork'
    assert snnc._platform == 'SunOS'


# Generated at 2022-06-13 01:49:50.797658
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True,
    )
    # Use current working directory to locate test file
    test_data_file = os.path.join(os.getcwd(), 'test_data_SunOS_ifconfig')
    network_collector = SunOSNetwork(module=module)
    interfaces, ips = network_collector.get_interfaces_info(test_data_file)
    # Validate interfaces:
    assert 'lo0' in interfaces
    assert interfaces['lo0']['ipv4'][0]['flags'] == ['UP', 'LOOPBACK', 'RUNNING']
    assert interfaces['lo0']['type'] == 'loopback'

# Generated at 2022-06-13 01:50:02.701866
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    from ansible.module_utils.facts.network.generic_bsd import TestGenericBsdIfconfigNetwork
    from ansible.module_utils.facts.network.sunos import TestSunOSNetwork
    import json

    TestGenericBsdIfconfigNetwork.platform = 'SunOS'

# Generated at 2022-06-13 01:50:09.403861
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    """
    Unit test for method get_interfaces_info of class SunOSNetwork
    """
    from ansible.module_utils.facts.network.sunos import SunOSNetwork
    import os

    # Generate a fake output of ifconfig command
    # based on output of os.popen('/usr/sbin/ifconfig -a')
    ifconfig_path = '/usr/sbin/ifconfig'
    if not os.path.exists(ifconfig_path):
        ifconfig_path = '/sbin/ifconfig'
    if not os.path.exists(ifconfig_path):
        ifconfig_path = '/usr/bin/ifconfig'
    ifconfig_out = os.popen(ifconfig_path + ' -a').read()

    # Instantiate a SunOSNetwork object and call get_interfaces_info

# Generated at 2022-06-13 01:50:10.483490
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    obj = SunOSNetworkCollector()
    assert obj._platform=='SunOS'

# Generated at 2022-06-13 01:50:12.108082
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    results = SunOSNetworkCollector().collect()
    assert results is not None

# Generated at 2022-06-13 01:50:15.670583
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    sunos_platform_inheritance = issubclass(SunOSNetworkCollector, NetworkCollector)
    assert sunos_platform_inheritance is True


# Generated at 2022-06-13 01:50:25.326668
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    plugin = SunOSNetwork()
    plugin.module = AnsibleModule(argument_spec=dict())
    plugin.module.run_command = mock.Mock(return_value=(0, SUNOS_IFACE_DATA, ""))

# Generated at 2022-06-13 01:50:31.990460
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    network_collector = SunOSNetworkCollector()
    assert network_collector is not None


# Generated at 2022-06-13 01:50:43.362038
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    module = AnsibleModule(argument_spec={})
    network = SunOSNetwork(module)
    fake_ifconfig_path = '/fake-bin/ifconfig'

# Generated at 2022-06-13 01:50:45.692635
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    collector = SunOSNetworkCollector(None)
    assert collector.platform == 'SunOS'
    assert collector.fact_class is SunOSNetwork

# Generated at 2022-06-13 01:50:51.634175
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    """
    Basic test for constructor of class SunOSNetworkCollector
    """
    sunos_network_collector = SunOSNetworkCollector(None)

    assert isinstance(sunos_network_collector.platform, str)
    assert sunos_network_collector.platform == 'SunOS'

    assert isinstance(sunos_network_collector.fact_class, SunOSNetwork)

# Generated at 2022-06-13 01:51:01.132979
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    module = DummyAnsibleModule()
    network = SunOSNetwork(module=module)
    rc, out, err = module.run_command([network.ifconfig_path, '-a'])
    interfaces, ips = network.get_interfaces_info(network.ifconfig_path)
    assert len(interfaces.keys()) == 6

    # Test parsing interface line
    assert interfaces['lo0']['type'] == 'loopback'
    assert interfaces['lo0']['ipv4'][0]['flags'] == set(['IPv6', 'LOOPBACK', 'RUNNING', 'MULTICAST'])
    assert interfaces['lo0']['ipv4'][0]['mtu'] == '8232'

# Generated at 2022-06-13 01:51:06.177439
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    obj = SunOSNetworkCollector()
    assert obj.platform == 'SunOS'
    assert isinstance(obj.facts, SunOSNetwork)
    assert obj.facts.platform == 'SunOS'
    assert obj.facts._platform == 'SunOS'

# Generated at 2022-06-13 01:51:07.945039
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    obj = SunOSNetworkCollector()
    obj.collect()
    assert obj.facts['interfaces']

# Generated at 2022-06-13 01:51:16.995381
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    import sys
    import inspect
    import json
    import os

    from ansible.module_utils.facts.network.sunos import SunOSNetwork

    current_directory = os.path.dirname(os.path.realpath(inspect.getfile(inspect.currentframe())))
    parent_directory = os.path.dirname(current_directory)
    sys.path.insert(0, parent_directory)

    ifconfig_path = 'tests' + os.sep + 'unit' + os.sep + 'module_utils' + os.sep + 'facts' + os.sep + 'network' + os.sep + 'solaris' + os.sep + 'ifconfig_output'

# Generated at 2022-06-13 01:51:23.482528
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    module = type('', (), {})()
    module.run_command = lambda args: (0, '', '')
    network_collector = SunOSNetwork(module)
    network_collector.get_interfaces_info('/sbin/ifconfig')
    assert network_collector._interfaces['lo0']['ipv4'][0]['mtu'] == 8232


# Generated at 2022-06-13 01:51:26.517579
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    assert issubclass(SunOSNetworkCollector, NetworkCollector)
    assert SunOSNetworkCollector._fact_class == SunOSNetwork
    assert SunOSNetworkCollector._platform == 'SunOS'


# Unit tests for class SunOSNetwork

# Generated at 2022-06-13 01:51:35.944196
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    x = SunOSNetworkCollector()
    assert isinstance(x, NetworkCollector)


# Generated at 2022-06-13 01:51:40.243092
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    from ansible.module_utils.facts.network.sunos import SunOSNetworkCollector
    from ansible.module_utils.facts.network.base import NetworkCollector
    obj = SunOSNetworkCollector()
    assert isinstance(obj, NetworkCollector)


# Generated at 2022-06-13 01:51:48.669370
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    module = AnsibleModule(
        argument_spec=dict(gather_subset=dict(default=[], type='list')),
        supports_check_mode=True)
    network = SunOSNetwork(module)

    interfaces = network.get_interfaces_info()
    assert len(interfaces) > 0
    assert 'lo0' in interfaces
    assert interfaces['lo0']['ipv4'][0]['address'] == '127.0.0.1'
    assert 'flags' in interfaces['lo0']['ipv4'][0]
    assert 'mtu' in interfaces['lo0']['ipv4'][0]
    assert 'macaddress' in interfaces['lo0']

# This is a helper function for unit tests

# Generated at 2022-06-13 01:51:58.689445
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    module = None
    iface_info = SunOSNetwork.get_interfaces_info(module, 'ifconfig')
    # Mimic the object returned by the module.run_command()
    iface_info_out = {'stdout':
                      'lo0: flags=2001000849<UP,LOOPBACK,RUNNING,MULTICAST,IPv4,VIRTUAL> mtu 8232 index 1\n'
                      '        inet 127.0.0.1 netmask ff000000 ',
                      'stderr': '',
                      'rc': 0}
    # Verify that the object returned from function get_interfaces_info()
    # has the same keys as the object returned by module.run_command()
    iface_info_keys = iface_info_out.keys()

# Generated at 2022-06-13 01:52:07.348499
# Unit test for method get_interfaces_info of class SunOSNetwork

# Generated at 2022-06-13 01:52:11.894819
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    """Unit test for constructor of SunOSNetworkCollector"""
    collector = SunOSNetworkCollector(None)
    assert SunOSNetworkCollector._platform == "SunOS"
    assert SunOSNetworkCollector._fact_class == SunOSNetwork
    assert SunOSNetworkCollector.platforms == ['SunOS']


# Generated at 2022-06-13 01:52:13.827399
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    net = SunOSNetworkCollector()
    assert net.platform == 'SunOS'
    assert net.fact_class == SunOSNetwork


# Generated at 2022-06-13 01:52:22.544969
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    test_module = AnsibleModule(argument_spec={})
    test_network = SunOSNetwork(module=test_module)
    test_ifconfig_path = '/sbin/ifconfig'

# Generated at 2022-06-13 01:52:27.997496
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    module = AnsibleModule(
        argument_spec=dict(gather_subset=dict(default=['!all'], type='list')),
        supports_check_mode=True)

    # SunOSNetwork.get_interfaces_info() returns a tuple of interfaces and ips
    interfaces, ips = SunOSNetwork().get_interfaces_info('/sbin/ifconfig')

    # Dump the interfaces/ips data structure and compare to expecte output
    print(json.dumps(interfaces, sort_keys=True, indent=4))
    print(json.dumps(ips, sort_keys=True, indent=4))

    module.exit_json(changed=False, ansible_facts=dict(interfaces=interfaces,
                                                       ips=ips))


from ansible.module_utils.basic import *

# Generated at 2022-06-13 01:52:38.122777
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    import json
    import os
    import warnings

    warnings.simplefilter("ignore")
    from ansible.module_utils.facts.network.sunos import SunOSNetwork
    from ansible.module_utils.facts.network.sunos import SunOSNetworkCollector

    try:
        os.path.isfile(SunOSNetworkCollector._fallback_interface_file)
    except:
        raise Exception ('No fallback interface file')

    # Create an instance of SunOSNetwork
    sn = SunOSNetwork()

    # Generate test data
    data = ""
    with open(os.path.join(os.path.dirname(__file__), 'test_data', 'ifconfig_output'), errors='replace') as out:
        data = out.read()

    # Run test and measure the time
    before = time.time()


# Generated at 2022-06-13 01:52:54.897607
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    assert SunOSNetworkCollector._platform == 'SunOS'
    assert SunOSNetworkCollector._fact_class is SunOSNetwork


# Generated at 2022-06-13 01:53:00.003447
# Unit test for method get_interfaces_info of class SunOSNetwork

# Generated at 2022-06-13 01:53:03.110538
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    fixtures = {'/sbin/ifconfig': ''}
    collector = SunOSNetworkCollector(dict(), fixtures=fixtures)
    assert collector.facts['network']


# Generated at 2022-06-13 01:53:05.159359
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    obj = SunOSNetworkCollector()
    assert isinstance(obj, NetworkCollector)


# Generated at 2022-06-13 01:53:06.522870
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    SunOSNetworkCollector()

# Generated at 2022-06-13 01:53:09.908183
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    sunos_fact_class = SunOSNetwork()
    assert sunos_fact_class._platform == 'SunOS'

# Unit tests for the class SunOSNetwork

# Generated at 2022-06-13 01:53:20.338215
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    network = SunOSNetwork()
    fake_ifconfig_path = 'tests/unit/module_utils/facts/network/fake_ifconfig'
    interfaces, ips = network.get_interfaces_info(fake_ifconfig_path)
    # This is what the facts should look like

# Generated at 2022-06-13 01:53:32.194591
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    module = get_module_mock()

    sn = SunOSNetwork(module=module)

    rc = 0

# Generated at 2022-06-13 01:53:43.283763
# Unit test for method get_interfaces_info of class SunOSNetwork

# Generated at 2022-06-13 01:53:52.311080
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    '''
    Unit test for method get_interfaces_info of class SunOSNetwork
    '''

# Generated at 2022-06-13 01:54:36.372250
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    collector = SunOSNetworkCollector(None, None)
    assert collector.fact_class.platform is 'SunOS'
    assert collector.fact_class.platform_fact is True


# Generated at 2022-06-13 01:54:47.576948
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    test_object = SunOSNetwork(None)

    with open("tests/unit/module_utils/facts/network/sunos_sample_ifcfg_a.txt") as f:
        rc = 0
        out = f.read()
    err = None
    test_object.module.run_command = lambda command: (rc, out, err)

    test_result = test_object.get_interfaces_info("/sbin/ifconfig")

# Generated at 2022-06-13 01:54:49.598394
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    assert SunOSNetworkCollector._platform == 'SunOS'
    assert SunOSNetworkCollector._fact_class == SunOSNetwork

# Generated at 2022-06-13 01:55:01.248642
# Unit test for method get_interfaces_info of class SunOSNetwork

# Generated at 2022-06-13 01:55:03.923524
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    """
    test_SunOSNetworkCollector provides unit test for constructor of class
    SunOSNetworkCollector

    :return:
    """
    SunOSNetworkCollector()

# Generated at 2022-06-13 01:55:11.645249
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    module = type('', (), {})()
    module.run_command = type('', (), {})()
    module.run_command.return_value = (0, '', '')

# Generated at 2022-06-13 01:55:22.152497
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    module = FakeAnsibleModule()
    module.run_command = FakeRunCommand(platform='SunOS')
    ifconfig_path = module.get_bin_path('ifconfig', True, ['/sbin/', '/usr/sbin'])
    fact_cls = SunOSNetwork()
    interfaces, ips = fact_cls.get_interfaces_info(ifconfig_path)
    assert 'lo0' in interfaces.keys()
    assert 'ipv4' in interfaces['lo0'].keys()
    assert 'ipv6' in interfaces['lo0'].keys()
    assert 'flags' in interfaces['lo0']['ipv4'][0].keys()
    assert interfaces['lo0']['ipv4'][0]['flags'][0] == 'UP'
    assert 'mtu' in interfaces

# Generated at 2022-06-13 01:55:32.099052
# Unit test for method get_interfaces_info of class SunOSNetwork

# Generated at 2022-06-13 01:55:37.796820
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    # Create an instance of SunOSNetworkCollector
    sunos_network_fact_collector = SunOSNetworkCollector()
    # Check the __init__() of SunOSNetworkCollector
    assert sunos_network_fact_collector._fact_class == SunOSNetwork
    assert sunos_network_fact_collector._platform == 'SunOS'

# Generated at 2022-06-13 01:55:46.859890
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    """
    Unit test for method get_interfaces_info of class SunOSNetwork
    """

# Generated at 2022-06-13 01:56:57.618133
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    module = AnsibleModule(
        argument_spec=dict(
            gather_subset=dict(default=['!all'], type='list')
        ),
        supports_check_mode=True
    )

    sunos_fact_collector = SunOSNetworkCollector(module)
    assert isinstance(sunos_fact_collector, SunOSNetworkCollector)
    assert not getattr(sunos_fact_collector, '_gather_subset', None)
    assert sunos_fact_collector._platform == 'SunOS'



# Generated at 2022-06-13 01:57:07.045705
# Unit test for method parse_interface_line of class SunOSNetwork
def test_SunOSNetwork_parse_interface_line():
    from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork
    from ansible.module_utils.facts.network.sunos import SunOSNetwork
    test_if = SunOSNetwork()
    test_interfaces = {}
    current_if = {}
    test_words = ['hme0:', 'flags=1000843', 'mtu=1500', 'index=6']
    expected_current_if = {'device': 'hme0', 'ipv4': [{'flags': ['BROADCAST', 'IPv4', 'MULTICAST'], 'mtu': '1500'}], 'ipv6': [], 'type': 'unknown', 'macaddress': 'unknown'}

# Generated at 2022-06-13 01:57:15.521492
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    # This test is run only against platform SunOS and we are using it to test
    # the output of ifconfig -a.
    platform = 'SunOS'
    module = {}
    module['run_command'] = run_command
    collector = SunOSNetworkCollector(module)
    interfaces, ips = collector.get_interfaces_info('ifconfig')

    assert len(interfaces['lo0']['ipv4']) == 1
    assert interfaces['lo0']['ipv4'][0]['address'] == '127.0.0.1'
    assert interfaces['lo0']['ipv4'][0]['netmask'] == '255.0.0.0'
    assert interfaces['lo0']['ipv4'][0]['broadcast'] == '127.255.255.255'
   

# Generated at 2022-06-13 01:57:16.658128
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    return SunOSNetworkCollector()

# Generated at 2022-06-13 01:57:25.787459
# Unit test for method get_interfaces_info of class SunOSNetwork

# Generated at 2022-06-13 01:57:33.118589
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    """
    Test the output of the SunOSNetwork.get_interfaces_info() method
    This is the output of /sbin/ifconfig -a on Solaris 10u11
    """

# Generated at 2022-06-13 01:57:34.834721
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    m = SunOSNetworkCollector()
    assert m._fact_class == SunOSNetwork
    assert m._platform == 'SunOS'


# Generated at 2022-06-13 01:57:44.755769
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    """This function tests the get_interfaces_info function of class SunOSNetwork"""
    module = NetworkCollector()
    sunosNetwork = SunOSNetwork(module)
    ifconfig_path = '/sbin/ifconfig'
    interfaces, ips = sunosNetwork.get_interfaces_info(ifconfig_path)
    assert('lo0' in interfaces)
    assert('bge0' in interfaces)
    assert('bge0' in interfaces)
    assert('bge1' in interfaces)
    assert('vlan0' in interfaces)
    assert('vlan1' in interfaces)
    assert('net0' in interfaces)
    assert('net1' in interfaces)
    assert(len(interfaces) == 7)
    assert(len(ips) == 2)


# Generated at 2022-06-13 01:57:51.913270
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    import platform
    import os
    import json
    from ansible.module_utils.facts.network.sunos import SunOSNetwork
    from ansible.module_utils.facts.network.sunos import SunOSNetworkCollector
    from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork

    def get_fixture(filename):
        filename = os.path.join(os.path.dirname(__file__), 'fixtures', filename)
        with open(filename, encoding='utf-8') as fixture_file:
            return [line.strip() for line in fixture_file]

    # Build the SunOSNetwork that we will test
    SunOSNetwork = SunOSNetwork(module)
    SunOSNetwork.module.params['gather_subset'] = '!all'

# Generated at 2022-06-13 01:58:03.287102
# Unit test for method parse_interface_line of class SunOSNetwork
def test_SunOSNetwork_parse_interface_line():
    SunOSTest = SunOSNetwork()
    iface1 = {'device': 'lo0', 'ipv4': [], 'ipv6': [], 'type': 'unknown'}
    iface2 = {'device': 'lo1', 'ipv4': [], 'ipv6': [], 'type': 'unknown'}
    iface3 = {'device': 'lo2', 'ipv4': [], 'ipv6': [], 'type': 'unknown'}
    iface4 = {'device': 'lo3', 'ipv4': [], 'ipv6': [], 'type': 'unknown'}
    iface5 = {'device': 'lo4', 'ipv4': [], 'ipv6': [], 'type': 'unknown'}