

# Generated at 2022-06-13 01:16:59.500137
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    m = AIXNetwork({})
    m.module = MagicMock()

    m.module.run_command.return_value = (0, 'default     192.168.121.254      UG         0 0          en0', '')
    m.get_route_path.side_effect = ['netstat', None]
    assert m.get_default_interfaces('netstat') == {'ipv4': {'gateway': '192.168.121.254', 'interface': 'en0'}, 'ipv6': {}}
    # m.get_route_path('netstat') is called once during get_default_interfaces
    assert m.get_route_path.call_count == 1


# Generated at 2022-06-13 01:17:05.784885
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    fake_module = FakeAnsibleModule()
    net = AIXNetwork(module=fake_module)
    fake_module.run_command = FakeRunCommand(netstat_output='default 192.168.2.1 UG 2 201 en2')
    res = net.get_default_interfaces('')
    assert res == ({'gateway': '192.168.2.1', 'interface': 'en2'}, {})



# Generated at 2022-06-13 01:17:12.797845
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():

    fact_class = AIXNetwork

    ifconfig_path = '/usr/sbin/ifconfig'
    ifconfig_options = '-a'
    rc, out, err = module.run_command([ifconfig_path, ifconfig_options])
    interfaces, ips = fact_class.get_interfaces_info(ifconfig_path, ifconfig_options)

    assert 'lo0' in interfaces
    assert interfaces['lo0']['device'] == 'lo0'
    assert interfaces['lo0']['type'] == 'Loopback'
    assert interfaces['lo0']['flags'] == {'BROADCAST', 'MULTICAST', 'UP'}
    assert interfaces['lo0']['inet'] == ['127.0.0.1']

# Generated at 2022-06-13 01:17:15.813527
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    collector = AIXNetworkCollector(None, NetworkCollector)

    assert collector is not None
    assert collector._fact_class.__name__ == 'AIXNetwork'
    assert collector._platform == 'AIX'

# Generated at 2022-06-13 01:17:25.460636
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    """Test AIXNetworkCollector"""
    # Initialize the instance of AIXNetworkCollector
    net_collector = AIXNetworkCollector()
    # Apply the get_fact method to get the ansible_facts
    ansible_facts = net_collector.get_facts()
    # Check if the value of the ansible_facts['ansible_net_all_ipv4_addresses']
    # is not empty
    assert ansible_facts['ansible_net_all_ipv4_addresses']
    # Check if the value of the ansible_facts['ansible_net_all_ipv6_addresses']
    # is not empty
    assert ansible_facts['ansible_net_all_ipv6_addresses']
    # Check if the value of
    # ansible_facts['ansible_net

# Generated at 2022-06-13 01:17:36.154036
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    ifconfig_path = '/usr/sbin/ifconfig'
    ifconfig_options = '-a'

    class mock_module:
        def get_bin_path(self, arg):
            if re.match('ifconfig', arg):
                return ifconfig_path
            else:
                return None


# Generated at 2022-06-13 01:17:37.359857
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    assert AIXNetworkCollector.__name__ == 'AIXNetworkCollector'


# Generated at 2022-06-13 01:17:47.959363
# Unit test for method get_default_interfaces of class AIXNetwork

# Generated at 2022-06-13 01:17:57.865081
# Unit test for method get_default_interfaces of class AIXNetwork

# Generated at 2022-06-13 01:17:58.342691
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    assert True

# Generated at 2022-06-13 01:18:13.014932
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    """
    Make sure we can instantiate the AIXNetworkCollector class.
    """

    network_collector = AIXNetworkCollector()
    assert network_collector
    if isinstance(network_collector, AIXNetworkCollector):
        assert True
    else:
        assert False


# Generated at 2022-06-13 01:18:17.447807
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    m = AIXNetwork()
    d_interf = m.get_default_interfaces(route_path=None)

    assert len(d_interf) == 2
    assert 'gateway' in d_interf[0]
    assert 'interface' in d_interf[0]
    assert 'gateway' in d_interf[1]
    assert 'interface' in d_interf[1]



# Generated at 2022-06-13 01:18:20.389326
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    obj = AIXNetworkCollector()
    assert obj._platform == 'AIX'
    assert obj._fact_class == AIXNetwork

# Generated at 2022-06-13 01:18:29.260121
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():

    # Just create instance of class, because we need just to check the method get_default_interfaces
    AIXNetwork = AIXNetworkCollector()._fact_class()

    # Set module.run_command to my-own method
    AIXNetwork.module.run_command = my_run_command

    # set route_path to FALSE (it is not necessary here)
    default_interfaces_v4, default_interfaces_v6 = AIXNetwork.get_default_interfaces(False)


# Generated at 2022-06-13 01:18:39.979420
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    # Creating object of class AIXNetwork, it has method get_default_interfaces
    ob = AIXNetwork()

    # Creating AnsibleModule, it has methods like get_bin_path(name, required=True)
    from ansible.module_utils.facts.network.generic_bsd import GenericBsdModule
    am = GenericBsdModule()

    # Mocking module.get_bin_path()
    from ansible.module_utils.facts import ansible_collections
    am.get_bin_path = ansible_collections.functools_lru_cache.lru_cache()(lambda name, required=True: '/usr/bin/netstat')

    # Mocking module.run_command()

# Generated at 2022-06-13 01:18:51.713809
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    module = FakeAnsibleModule()

    # given
    ifconfig_path = './tests/unit/module_utils/facts/network/files/AIX-ifconfig-a.txt'
    ifconfig_options = '-a'

# Generated at 2022-06-13 01:18:54.121311
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    module = AnsibleModule(argument_spec={})
    network_collector = AIXNetworkCollector()
    network_collector.get_default_interfaces('some path')



# Generated at 2022-06-13 01:18:57.481319
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    """
    Construct an instance of AIXNetworkCollector
    """
    AIX_fact_collector = AIXNetworkCollector()
    assert AIX_fact_collector._fact_class.platform == 'AIX'
    assert AIX_fact_collector._platform == 'AIX'

# Generated at 2022-06-13 01:19:09.073917
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():

    class MockModule(object):
        def __init__(self):
            self.run_command_results = [
                [0, '''default 172.16.1.100 UG        0        0 en0
default ::1      UG        0        0 lo0''', ''],
            ]

        def get_bin_path(self, name, required=False):
            return 'path/' + name

        def run_command(self, cmd, check_rc=True):
            return self.run_command_results.pop(0)

    module = MockModule()

    n = AIXNetwork()
    n.module = module
    route_path = module.get_bin_path('route')
    v4_default, v6_default = n.get_default_interfaces(route_path)

# Generated at 2022-06-13 01:19:20.867908
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    from ansible.module_utils.facts import stubs
    from ansible.module_utils.facts.network.aix import AIXNetworkClass
    from ansible.module_utils import basic

    module = basic.AnsibleModule(
        argument_spec={},
        supports_check_mode=True
    )

    try:
        # Set up stubs needed by AIXNetworkClass
        stubs.stub_module_for_class(module, AIXNetworkClass)
        network_collector = AIXNetworkClass(module)
        network_collector.populate()
    except Exception as e:
        print("test_AIXNetwork_get_interfaces_info failed: " + str(e))
        raise

    # Test the actual call to get_interfaces_info
    ifconfig_path = module.get_bin_path

# Generated at 2022-06-13 01:19:52.441684
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    from ansible.module_utils.facts.network.aix import AIXNetwork
    from ansible.module_utils.facts.network.aix import AIXNetworkCollector
    from ansible.module_utils.facts.network.aix import test_AIXNetwork_get_interfaces_info as test_interfaces_info
    from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork
    from ansible.module_utils.facts.network.generic_bsd import test_GenericBsdIfconfigNetwork_get_interfaces_info as test_interfaces_info_generic_bsd
    test_interfaces_info_generic_bsd(GenericBsdIfconfigNetwork)
    test_interfaces_info(AIXNetwork)
    test_interfaces_info(AIXNetworkCollector)

# Generated at 2022-06-13 01:19:56.286393
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    m = re.compile('AIXNetworkCollector')
    x = re.compile('GenericBsdIfconfigNetwork')
    for i in dir(AIXNetworkCollector):
        if not m.match(i) and x.match(i):
            print("UNIT TEST: AIXNetworkCollector METHOD = ", i)

# Generated at 2022-06-13 01:20:07.035321
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    global module
    module = AnsibleModule(
        argument_spec=dict(
            gather_subset=dict(default=[], type='list')
        )
    )
    stdout = "default 0.0.0.0 UG 0 0 en0\ndefault 10.0.0.1 UG 0 0 en1"
    rc = 0
    err = ''

    route_path = module.get_bin_path('route')
    network_collector = AIXNetworkCollector()

    # without route command
    module.run_command.return_value = (rc, stdout, err)
    module.get_bin_path.return_value = None
    interface = network_collector.get_default_interfaces(route_path)

    assert interface['gateway'] is None
    assert interface['interface'] is None



# Generated at 2022-06-13 01:20:16.954634
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    """
    Run tests on network.AIXNetwork.get_interfaces_info()
    """
    class module_object():
        def __init__(self, bin_path):
            self.bin_path = bin_path
            self.run_command_calls = []
            self.run_command_returns = []

        def get_bin_path(self, name):
            return self.bin_path[name]

        def run_command(self, args):
            self.run_command_calls.append(args)
            return self.run_command_returns.pop()

    import pytest

    # test for not in wpar

# Generated at 2022-06-13 01:20:21.153482
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    """
    Unit test for method get_default_interfaces of class AIXNetwork
    :return: None
    """
    module = AnsibleModule(argument_spec={})
    aix_network = AIXNetwork(module=module)
    aix_network.get_default_interfaces('/usr/bin/netstat')

    # no exit_json or fail_json so that exception gets raised
    return True

# Generated at 2022-06-13 01:20:32.682363
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    class MockModule:
        def __init__(self):
            self.params = dict()
            self.run_command = Mock(return_value=(0, '', ''))
            self.fail_json = Mock(return_value=dict(failed=True))
        def get_bin_path(self, arg):
            if arg == 'uname':
                return '/usr/bin/uname'
            elif arg == 'netstat':
                return '/usr/bin/netstat'
            elif arg == 'ifconfig':
                return 'ifconfig'
            elif arg == 'entstat':
                return '/usr/bin/entstat'
            elif arg == 'lsattr':
                return '/usr/bin/lsattr'

    class MockUtilsModule:
        def __init__(self):
            self.is_cl

# Generated at 2022-06-13 01:20:43.044990
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    '''
    unit test function for method get_interfaces_info of class AIXNetwork
    :return: nothing
    '''
    import re
    ifconfig_path = "/usr/sbin/ifconfig"
    ifconfig_options = '-a'
    # Get interfaces_info from Linux
    aix = AIXNetwork(dict(module=None))
    interfaces_info = aix.get_interfaces_info(ifconfig_path, ifconfig_options)
    # Display test result
    print ("\n########## <Test>: test_AIXNetwork_get_interfaces_info ###########")

    print ("\n########## <Test>: interfaces info ###########")
    print (interfaces_info)

    # Get interfaces_info from Linux

# Generated at 2022-06-13 01:20:47.690036
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    aixnc = AIXNetworkCollector()
    assert aixnc.facts['all_ipv4_addresses'] == []
    assert aixnc.facts['all_ipv6_addresses'] == []
    assert aixnc.facts['default_ipv4']['gateway'] is None
    assert aixnc.facts['default_ipv6']['gateway'] is None

# Generated at 2022-06-13 01:20:51.113685
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    assert AIXNetworkCollector.platform == 'AIX'
    assert AIXNetworkCollector._fact_class == AIXNetwork
    assert AIXNetworkCollector.collect() == {}

# Generated at 2022-06-13 01:21:00.122382
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    from ansible_collections.ansible.community.tests.unit.compat import unittest

    class TestNetworkCollector(unittest.TestCase):
        """
        This is a class to test the AIXNetworkCollector class.
        """
        def test_constructor(self):
            """
            This is a constructor test case.
            """
            network_collector = AIXNetworkCollector()
            self.assertIsInstance(network_collector, AIXNetworkCollector)
            self.assertIsInstance(network_collector._fact_class, AIXNetwork)
            self.assertEqual(network_collector._platform, 'AIX')

    unittest.main()


# Generated at 2022-06-13 01:21:50.357016
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    test_module = NetworkCollector()
    test_class = AIXNetwork(test_module)

    netstat_rc = None
    netstat_out = None
    netstat_err = None
    netstat_path = test_class.module.get_bin_path('netstat')
    if netstat_path:
        netstat_rc, netstat_out, netstat_err = test_class.module.run_command([netstat_path, '-nr'])

    assert test_class.get_default_interfaces(test_class.route_path) == (
        {'gateway': '10.10.10.1', 'interface': 'en0'},
        {'gateway': 'fd00::1', 'interface': 'en0'}
    )

# Generated at 2022-06-13 01:21:52.016353
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    # constructor without argument
    AIXNetworkCollector()

# Generated at 2022-06-13 01:21:59.059428
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():

    # Inputs
    ifconfig_path = '/usr/sbin/ifconfig'
    ifconfig_options = '-a'

    # Expected results

# Generated at 2022-06-13 01:22:09.668640
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    module = AnsibleModule(argument_spec={'path': {'required': True, 'type': 'list'},
                                          'route_path': {'required': True},
                                          })
    module.params['path'] = ['/bin', '/sbin', '/usr/bin', '/usr/sbin']
    module.params['route_path'] = '/usr/sbin/netstat'
    ip = AIXNetwork()

    ip.module = module

    interfaces_v4, interfaces_v6 = ip.get_default_interfaces(route_path='/usr/sbin/netstat')

    print("interfaces_v4")
    print(interfaces_v4)
    print("interfaces_v6")
    print(interfaces_v6)



# Generated at 2022-06-13 01:22:17.126891
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
  from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork

  ifconfig_path = './tests/unit/utils/facts/network/files/aix_ifconfig.dat'
  ifconfig_options = '-a'
  c = AIXNetwork(dict(module=None, params=dict(gather_subset='!all')))
  c.get_interfaces_info(ifconfig_path, ifconfig_options)

# Generated at 2022-06-13 01:22:21.402925
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():

    from ansible.module_utils.facts.network.aix import AIXNetworkCollector

    assert AIXNetworkCollector._platform == 'AIX'
    assert AIXNetworkCollector._fact_class == AIXNetwork
    assert AIXNetworkCollector.platform == 'AIX'

# Generated at 2022-06-13 01:22:24.534463
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    assert AIXNetworkCollector._platform == 'AIX'
    assert AIXNetworkCollector._fact_class == AIXNetwork

# Unit tests for constructor of class AIXNetwork

# Generated at 2022-06-13 01:22:33.359201
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    """
    Checks if method get_default_interfaces of class AIXNetwork
    returns 'interface v4' or 'interface v6' with correct gateway.
    """
    ifconfig_path = '/usr/bin/ifconfig'
    route_path = '/usr/bin/netstat'
    AIXNetworkCollector.set_module(None)
    AIXnetwork = AIXNetwork(ifconfig_path, route_path)
    interface_v4, interface_v6 = AIXnetwork.get_default_interfaces(route_path)
    assert interface_v4['interface'] == 'en0'
    assert interface_v4['gateway'] == '10.0.0.1'
    assert interface_v6['interface'] == 'en1'
    assert 'gateway' not in interface_v6


# Generated at 2022-06-13 01:22:34.326979
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    collector = AIXNetworkCollector()
    assert collector.platform == 'AIX'


# Generated at 2022-06-13 01:22:37.996326
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    aix_net = AIXNetwork()
    aix_net.module = AnsibleModule(argument_spec={
    })
    interfaces = aix_net.get_default_interfaces('/etc/route')
    assert interfaces == (
        {'gateway': '192.168.0.1', 'interface': 'lo0'},
        {'gateway': 'fe80::1', 'interface': 'lo0'}
    )


# Generated at 2022-06-13 01:24:05.806261
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    network_obj = AIXNetworkCollector()
    assert network_obj.platform == 'AIX'
    assert network_obj._fact_class == AIXNetwork


# Generated at 2022-06-13 01:24:08.225807
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    network_collector = AIXNetworkCollector()
    assert network_collector.facts is None
    assert network_collector.fact_class == AIXNetwork
    assert network_collector.platform == 'AIX'
    assert network_collector.config == {}

# Unit tests for AIXNetwork

# Generated at 2022-06-13 01:24:12.454399
# Unit test for method get_interfaces_info of class AIXNetwork

# Generated at 2022-06-13 01:24:22.345394
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():

    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )

    # mocked content of /etc/rc.tcpip file
    #   route add default 173.16.40.254
    #   route add -net 10.1.1.0/24 10.1.1.254 -interface en3
    #   route add -net 10.1.2.0/24 10.1.2.254 -interface en2
    #   route add -net 10.1.3.0/24 10.1.3.254 -interface en1
    #   route add -net 10.1.4.0/24 10.1.4.254 -interface en0

# Generated at 2022-06-13 01:24:31.460718
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    test_module = AnsibleModule(
        argument_spec=dict(gather_subset=dict(default=['!all'], type='list'))
    )
    test_AIXNetwork = AIXNetwork(test_module)
    test_AIXNetwork.gather_facts = True

    interfaces_info_return = test_AIXNetwork.get_interfaces_info('ifconfig', '-a')
    interfaces_return = interfaces_info_return[0]

    # This particular interface has a mtu attribute in ODM
    test_device_1 = interfaces_return['en0']
    assert test_device_1['device'] == 'en0'
    assert test_device_1['flags'] == ['UP', 'BROADCAST', 'RUNNING', 'SIMPLEX', 'MULTICAST']
    assert test_device

# Generated at 2022-06-13 01:24:40.776072
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    # create underlying platform and test class
    platform = 'AIX'
    uname_path = '/usr/bin/uname'
    netstat_path = '/usr/sbin/netstat'

    test_def_interfaces = AIXNetwork()
    test_def_interfaces.module = FakeModule(paths={'uname': uname_path, 'netstat': netstat_path})

    # set command output
    uname_output = '0 AIX'
    netstat_output = 'Routing tables\n' \
                     'Destination Gateway Flags  Refs Use  If  Expire\n' \
                     'default  128.0.0.1 UG        2  324 en4        0\n' \
                     'default  128.0.0.1 UG        2  324 en4        0\n'

# Generated at 2022-06-13 01:24:48.328499
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    import os
    import sys

    # Get information about current environment
    exists = os.path.exists
    environ = os.environ
    path_join = os.path.join
    split = os.path.split
    path_dirname = os.path.dirname
    curdir = split(__file__)[0]
    parentdir = path_dirname(curdir)
    testdir = path_join(parentdir, 'test_module_utils.network.interfaces.resources')
    dirname = path_dirname
    sys.path.append(parentdir)
    file_open = open

    # Mock modules
    class AnsibleModule():
        def __init__(self):
            self.run_command = self.mock_run_command
            self.get_bin_path = self.mock_

# Generated at 2022-06-13 01:24:52.619183
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    aixNetworkCollector = AIXNetworkCollector()
    assert aixNetworkCollector.facts['default_ipv4_interface'] == 'lo0'
    assert aixNetworkCollector.facts['default_ipv4_gateway'] == '127.0.0.1'
    assert aixNetworkCollector.facts['default_ipv6_interface'] == 'lo0'
    assert aixNetworkCollector.facts['default_ipv6_gateway'] == '::1'


# Generated at 2022-06-13 01:25:01.251126
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    module = AnsibleModuleMock()
    module.get_bin_path.side_effect = ['netstat']
    module.run_command.side_effect = [[0, 'default 192.168.1.1 UG en1', ''],
                                      [0, 'default fec0:0:0:ffff::1 UG en1', '']]
    ansible_network = AIXNetwork()
    ansible_network.module = module
    assert ansible_network.get_default_interfaces('route') == {'gateway': '192.168.1.1',
                                                               'interface': 'en1'}, \
        'Failed to return valid interface for v4'

# Generated at 2022-06-13 01:25:08.372950
# Unit test for method get_interfaces_info of class AIXNetwork