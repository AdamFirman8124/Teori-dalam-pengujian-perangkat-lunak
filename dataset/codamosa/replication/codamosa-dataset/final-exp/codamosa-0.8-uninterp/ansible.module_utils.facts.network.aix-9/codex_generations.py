

# Generated at 2022-06-13 01:16:55.954902
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    # Create an instance of class AIXNetwork
    aix_network = AIXNetwork()

    # Get the ODM path of the network
    route_path = aix_network.get_route_path()

    # Get the default interfaces
    interface_ipv4, interface_ipv6 = aix_network.get_default_interfaces(route_path)

    assert interface_ipv4 == {}
    assert interface_ipv6 == {}



# Generated at 2022-06-13 01:17:02.317056
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    net_o = AIXNetwork()

# Generated at 2022-06-13 01:17:11.045603
# Unit test for method get_interfaces_info of class AIXNetwork

# Generated at 2022-06-13 01:17:16.529668
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    # Initialize mock of module
    module = AnsibleModule(argument_spec={})

    # run tested method
    ifconfig_path = '/usr/sbin/ifconfig'
    ret = AIXNetwork.get_interfaces_info(module, ifconfig_path)

    # check answer
    assert ret is not None, "Return object must not be None"
    assert len(ret) == 2, "Return object must have two propery"
    interfaces, ips = ret
    assert len(interfaces) > 0, "Interfaces propery must be non-empty dict"
    assert len(ips) > 0, "IPs propery must be non-empty dict"


from ansible.module_utils.basic import *  # noqa: F403
from ansible.module_utils.facts.utils import get_file_content  # noqa

# Generated at 2022-06-13 01:17:20.142702
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    network_collector = AIXNetworkCollector()
    assert network_collector._platform == 'AIX'
    assert network_collector._fact_class == AIXNetwork

# Generated at 2022-06-13 01:17:21.565856
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    assert AIXNetworkCollector is not None


# Generated at 2022-06-13 01:17:25.604149
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    firmware = None
    os_version = None
    module = AnsibleModule(argument_spec={})
    fact_network = AIXNetwork(module)
    fact_network.get_default_interfaces('/usr/bin/netstat')

# AnsibleModule class definition with AIXNetwork as argument

# Generated at 2022-06-13 01:17:31.945778
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    module = AnsibleModule(argument_spec={
        "gather_subset": dict(default=["!all"], type='list')
    })
    facts = dict()
    net = AIXNetwork(module)
    net.get_default_interfaces('/sbin/route')
    assert facts['ansible_default_ipv4'] == {}
    assert facts['ansible_default_ipv6'] == {}

# Generated at 2022-06-13 01:17:40.260485
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    # Create class object
    test_class = AIXNetwork()

    # Create test string
    test_string = 'default <ip> - 0 0x0 0x0 UG 0 0 0 en0 <interface>'

    # Create test string for IPv6
    test_string_IPv6 = 'default <ipv6> - 0 0x0 0x0 UG 0 0 0 en0 <interface>'

    # Test IPv4
    test_result = test_class.get_default_interfaces(test_string)
    assert test_result == ('<ip>', '<interface>'), \
        'IPv4 test failed. Expected result: ("<ip>", "<interface>")'

    # Test IPv6
    test_result = test_class.get_default_interfaces(test_string_IPv6)
    assert test

# Generated at 2022-06-13 01:17:52.119452
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    module = MockModule()
    aixnet = AIXNetwork(module)

    ifconfig_path = '/usr/sbin/ifconfig'
    ifconfig_options = '-a'
    ifc_info, ips = aixnet.get_interfaces_info(ifconfig_path, ifconfig_options)
    assert ifc_info
    assert ips
    assert len(ifc_info) > 0
    assert len(ips['all_ipv4_addresses']) > 0
    assert len(ips['all_ipv6_addresses']) > 0
    assert 'device' in ifc_info['lo0']
    assert 'ipv4' in ifc_info['lo0']
    assert 'flags' in ifc_info['lo0']

# Generated at 2022-06-13 01:18:05.470818
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    collector = AIXNetworkCollector()
    assert collector.platform == 'AIX'
    assert collector.fact_class == AIXNetwork


# Generated at 2022-06-13 01:18:09.274045
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    '''
    Unit test for method get_default_interfaces of class AIXNetwork
    '''
    aix_network = AIXNetwork()

    aix_network.get_default_interfaces('/usr/sbin/route')

    assert True



# Generated at 2022-06-13 01:18:17.380344
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    module = AnsibleModule(
        argument_spec=dict(
            gather_subset=dict(default=["!all", "!min"], type='list'),
        ),
        supports_check_mode=True
    )

    mock_run_command = MagicMock(return_value=(0, 'default 9.8.7.6 UG 1 1000004 en0 default 9.8.7.6 UG 22 1000004 en0', ''))
    with patch.object(AIXNetwork, 'run_command', mock_run_command):
        net = AIXNetwork(module=module)

    interface = net.get_default_interfaces('netstat')
    assert interface[0]['gateway'] == '9.8.7.6'
    assert interface[0]['interface'] == 'en0'



# Generated at 2022-06-13 01:18:27.917595
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    net = AIXNetwork()
    net.module = MagicMock()
    net.module.get_bin_path = MagicMock(return_value='/usr/bin/netstat')
    net.module.run_command = MagicMock(return_value=(0, 'default 192.168.122.1 UG 0 0 en1 default fe80::%utun0 UG 0 0 utun0 <Link#24>', None))
    result = net.get_default_interfaces('/sbin/route')
    expected = dict(gateway='192.168.122.1', interface='en1'), dict(gateway='fe80::%utun0', interface='utun0')
    assert result == expected
    net.module.get_bin_path.assert_called_once_with('netstat')
    net.module.run

# Generated at 2022-06-13 01:18:32.751344
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    assert AIXNetwork().get_default_interfaces(route_path=None) == ({'gateway': '10.0.2.2', 'interface': 'en0'}, {'gateway': 'fe80::a00:27ff:fe70:edbf', 'interface': 'en0'})



# Generated at 2022-06-13 01:18:42.295985
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    module = AnsibleModule(argument_spec={})
    ifconfig_path = module.get_bin_path('ifconfig')

    # Create temporary text file for ifconfig -a output
    tmp_file = tempfile.NamedTemporaryFile(delete=False)
    tmp_file.write('en0: flags=1e080863,c0<UP,BROADCAST,NOTRAILERS,RUNNING,SIMPLEX,MULTICAST,GROUPRT,64BIT,CHECKSUM_OFFLOAD(ACTIVE),PSEG,LARGESEND>\n')
    tmp_file.write('        inet 10.10.10.10 netmask 0xffffff00 broadcast 10.10.10.255\n')

# Generated at 2022-06-13 01:18:44.700693
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    from ansible.module_utils.facts.network.base import NetworkCollector
    collector = NetworkCollector()
    assert isinstance(collector, NetworkCollector)

# Generated at 2022-06-13 01:18:55.436545
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts import ModuleDeprecationWarning

    import warnings

    with warnings.catch_warnings(record=True) as w:
        # Cause all warnings to always be triggered.
        warnings.simplefilter("always")
        ifconfig_path = '/usr/sbin/ifconfig'
        ifconfig_options = '-a'

        # Trigger a deprecation warning.
        network_collector = AIXNetworkCollector()
        network_collector.get_interfaces_info(ifconfig_path, ifconfig_options)

        # Verify some things
        assert issubclass(w[-1].category, ModuleDeprecationWarning)
        assert "The AIXNetwork class is deprecated" in str(w[-1].message)

        # Go ahead

# Generated at 2022-06-13 01:18:59.947803
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    ifc = AIXNetwork()

    ifconfig_path = '/usr/sbin/ifconfig'
    ifconfig_options = '-a'
    interfaces, ips = ifc.get_interfaces_info(ifconfig_path, ifconfig_options)

    for iface in interfaces.keys():
        for k in interfaces[iface].keys():
            print('%s: %s' % (k, interfaces[iface][k]))

# Generated at 2022-06-13 01:19:10.087902
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    module = DummyModule()
    network = AIXNetwork(module)

    # Prepare a fake route information for method get_default_interfaces
    route_file = [
        'default 192.0.2.10',
        '192.0.2.0/32 0.0.0.0 192.0.2.1 en0',
        '192.0.2.0/24 0.0.0.0 192.0.2.1 en1',
        'default fe80::%en0 UGSc 18 0 en0',
        'fe80::/64 fe80::1%en1 UGcI 2 12 en1',
        'fe80::%en0 0:11:22:33:44:55 UHLc 1 318 en0 1188',
        '::1 ::1 UH 2 8 lo0',
    ]

# Generated at 2022-06-13 01:19:39.883037
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    aix_network = AIXNetwork()
    from ansible.module_utils.facts.network.net_tools import NetTools, InterfaceInfo
    net_tools = NetTools()
    expected_if, expected_ip = net_tools.get_interfaces_info(aix_network.get_bin_path('ifconfig'), "-a")
    actual_if, actual_ip = aix_network.get_interfaces_info(aix_network.get_bin_path('ifconfig'), "-a")

    import pprint
    pprint.pprint(expected_if)
    pprint.pprint(actual_if)

    assert expected_if == actual_if
    assert expected_ip == actual_ip

# Generated at 2022-06-13 01:19:42.550105
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    nc_test = AIXNetworkCollector()
    assert nc_test._fact_class.platform == 'AIX'
    assert nc_test._platform == 'AIX'

# Generated at 2022-06-13 01:19:52.081205
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    module = AnsibleModule(
        argument_spec=dict(
            gather_subset=dict(default=['!all', '!min'], type='list'),
            filter=dict(default='*', type='str'),
            route_path=dict(default="/usr/bin/netstat", type='str'),
            fact_subset=dict(default=None, type='dict')
        )
    )
    network_collector = AIXNetworkCollector(module=module)
    facts = network_collector.get_facts()
    assert 'default_ipv4' in facts
    assert 'default_ipv6' in facts
    assert 'default_ipv4' in facts['default_ipv4']
    assert 'default_ipv6' in facts['default_ipv6']


# Generated at 2022-06-13 01:19:58.751691
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    module = AnsibleModule(argument_spec={})
    network_module_obj = AIXNetwork()
    interfaces_v4, interfaces_v6 = network_module_obj.get_default_interfaces(route_path='/bin/netstat')
    assert_equals(interfaces_v4['gateway'], '10.0.0.1')
    assert_equals(interfaces_v4['interface'], 'en0')
    assert_equals(interfaces_v6['gateway'], 'fc00:0:0:0:0:0:0:1')
    assert_equals(interfaces_v6['interface'], 'en0')

# Generated at 2022-06-13 01:20:00.482147
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    module = AnsibleModule(arg_spec={})
    collector = AIXNetworkCollector(module)
    assert collector.platform == 'AIX'
    assert collector.fact_class == AIXNetwork


# Generated at 2022-06-13 01:20:06.696606
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    """Test initiation of class AIXNetworkCollector"""
    module = AnsibleModuleStub()
    nc = AIXNetworkCollector(module=module)
    assert nc.__class__.__name__ == 'AIXNetworkCollector'
    assert nc.platform == 'AIX'
    assert nc.fact_class.__name__ == 'AIXNetwork'


# Generated at 2022-06-13 01:20:08.380252
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    x = AIXNetworkCollector()
    assert x.get_facts() is not {}

# Generated at 2022-06-13 01:20:18.103345
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    from ansible.module_utils.facts.network.generic_bsd import GenericBsdNetworkCollector
    from ansible.module_utils.facts.network.aix import AIXNetwork
    import json

    f = GenericBsdNetworkCollector()
    g = AIXNetwork()
    g.module = f.module
    g.parse_interface_line = f.parse_interface_line
    g.parse_ether_line = f.parse_ether_line
    g.parse_inet_line = f.parse_inet_line
    g.parse_inet6_line = f.parse_inet6_line
    g.parse_nd6_line = f.parse_nd6_line
    g.parse_lladdr_line = f.parse_lladdr_line
    g.parse_media_line = f.parse_media

# Generated at 2022-06-13 01:20:24.724998
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    module = FakeAnsibleModule()

    # This is the ifconfig output in AIX 7.1

# Generated at 2022-06-13 01:20:30.870494
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    module = AnsibleModule(
        argument_spec=dict(
            gather_subset=dict(default=['!all', '!min'], type='list')
        ),
        supports_check_mode=True
    )
    # run the module with given values
    result = AIXNetwork(module).get_default_interfaces(None)

    assert result is not None

# Generated at 2022-06-13 01:21:22.729288
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    default.standard_module_utils.IS_HPUX = False
    default.standard_module_utils.IS_AIX = True
    network = AIXNetwork()

    out = '''
default 192.168.1.1 UG en0
default 192.168.2.1 US en1
default 192.168.3.1 UG en2
default 192.168.4.1 UG en3
default 192.168.5.1 UG en4
default 192.168.6.1 UG en5
default 192.168.7.1 UG en6
'''
    route_path = '/usr/bin/netstat'
    module_mock = MagicMock()
    module_mock.get_bin_path.side_effect = lambda x: route_path if x == 'netstat' else None
    module

# Generated at 2022-06-13 01:21:29.912199
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():

    class AIXModule:

        def run_command(self, args):
            return 0, "Routing tables\nInternet: \nDestination        Mask            Gateway         Interface\ndefault            0.0.0.0         172.21.200.1    ent12\n", 0

        def get_bin_path(self, arg):
            return '/usr/bin/netstat'

    data = AIXNetwork(AIXModule())

    interface = data.get_default_interfaces('/usr/bin/netstat')

    assert interface['v4']['interface'] == 'ent12'
    assert interface['v4']['gateway'] == '172.21.200.1'
    assert interface['v6'] == {}



# Generated at 2022-06-13 01:21:39.033346
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    from ansible.module_utils.facts.network import AIXNetwork
    from mock import patch, MagicMock


# Generated at 2022-06-13 01:21:42.906702
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    config = '''
    gateway        10.10.10.1     1
    destination    10.10.10.0     255.255.255.0
    destination    default        gateway         10.10.20.1
    '''
    result = AIXNetwork.get_default_interfaces(config)
    assert result['v4']['gateway'] == 'default'
    assert result['v4']['interface'] == 'gateway'
    assert result['v6']['gateway'] == '10.10.20.1'
    assert result['v6']['interface'] == 'gateway'

# Generated at 2022-06-13 01:21:49.607176
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():

    route_path = 'route'

    expected_result = (dict(gateway='10.10.10.1', interface='en0'), dict(gateway='fe80::1%1', interface='en0'))

    netstat_path = 'netstat'
    generic_bsd_ifconfig_network = AIXNetwork()
    generic_bsd_ifconfig_network.module.get_bin_path = lambda x: netstat_path
    (v4_interface, v6_interface) = generic_bsd_ifconfig_network.get_default_interfaces(route_path)

    assert v4_interface == expected_result[0]
    assert v6_interface == expected_result[1]

# Generated at 2022-06-13 01:21:56.496204
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    import logging
    import os
    from ansible.module_utils.facts import timeout

    def run_module(module_name, **kwargs):

        # the tester is running with this module (aix_facts)
        # get the real module name and its arguments
        import sys
        args = sys.argv.copy()
        args.remove('test')
        module_name = args.pop(0)

        kwargs['timeout'] = 0
        kwargs['gather_subset'] = 'all'

        # import the module
        module = __import__(module_name)
        if hasattr(module, 'run_ansible_module'):
            return module.run_ansible_module(module_name, args, kwargs)

        module.EXAMPLES = ''
        module.RETURN = ''

# Generated at 2022-06-13 01:22:07.256026
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    """
    This unit test tests that the method get_interfaces_info of the AIXNetwork class
    returns the correct interfaces when called with ifconfig output from AIX 7.2.

    The expected interfaces are:
    en0, en1, en2, en3, ent0
    """

    test_class = AIXNetwork()
    test_module = None
    ifconfig_path = None


# Generated at 2022-06-13 01:22:09.868960
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    module = AnsibleModule()
    network = AIXNetwork(module)
    interfaces = network.get_interfaces_info()
    assert 'lo0' in interfaces['interfaces'].keys()


# Generated at 2022-06-13 01:22:12.005269
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    aix_network_collector = AIXNetworkCollector(None, 'AIX')
    assert aix_network_collector._platform == 'AIX'



# Generated at 2022-06-13 01:22:15.415566
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    assert isinstance(AIXNetworkCollector(None).fact_class.platform, str)
    assert isinstance(AIXNetworkCollector(None).fact_class.get_default_interfaces(None), tuple)
    assert isinstance(AIXNetworkCollector(None).fact_class.get_interfaces_info(None), tuple)

# Generated at 2022-06-13 01:23:52.953995
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    net_obj = AIXNetwork()
    net_obj.module = mock_module()
    net_obj.module.run_command.return_value = (0, 'default 0.0.0.0 UG 0 0 0 en0\ndefault ::1 UG 1024 0 0 lo0\ndefault fe80::%en0 U 0 0 0 en0\ndefault fe80::1%lo0 U 16384 0 0 lo0', None)
    interface_v4, interface_v6 = net_obj.get_default_interfaces('/tmp/route')
    assert interface_v4 == dict(gateway='0.0.0.0', interface='en0')
    assert interface_v6 == dict(gateway='::1', interface='lo0')


# Generated at 2022-06-13 01:23:57.196920
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    mock_module = type('MockModule', (object,), {})
    collector = AIXNetworkCollector(mock_module)
    assert collector.platform == 'AIX'
    assert collector.fact_class == AIXNetwork


# Generated at 2022-06-13 01:23:57.927076
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    collector = AIXNetworkCollector()

# Generated at 2022-06-13 01:24:01.543309
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    "Unit test for constructor of class AIXNetworkCollector"
    ansible_module = dict()
    nc = AIXNetworkCollector(ansible_module)
    assert nc.fact_class._platform == 'AIX'


if __name__ == '__main__':
    test_AIXNetworkCollector()

# Generated at 2022-06-13 01:24:04.351834
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )
    nm = AIXNetwork(module)
    nm.get_default_interfaces('/usr/sbin/route')
    # the test works because the function just returns the default value
    

# Generated at 2022-06-13 01:24:05.008077
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    AIXNetworkCollector()

# Generated at 2022-06-13 01:24:10.953504
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetworkTest
    from os import environ
    from sys import executable
    from json import dumps
    from ansible.module_utils.facts import default_collectors

    environ['PATH'] = '/usr/bin:/usr/sbin'
    output = GenericBsdIfconfigNetworkTest().run_ifconfig('-a')
    network_fact_class =  default_collectors.get('network')
    collector = AIXNetworkCollector({'network': network_fact_class}, {}, {}, {}, {}, executable)
    interfaces, ips = collector.get_interfaces_info('/usr/sbin/ifconfig', '-a')

    assert interfaces['lo0']['device'] == 'lo0'

# Generated at 2022-06-13 01:24:20.285150
# Unit test for method get_interfaces_info of class AIXNetwork

# Generated at 2022-06-13 01:24:22.451371
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    collectors = list()
    collectors.append(AIXNetworkCollector())
    assert collectors[0]._platform == 'AIX'
    assert collectors[0]._fact_class == AIXNetwork

# Generated at 2022-06-13 01:24:31.524843
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    """Unit test for method get_interfaces_info of class AIXNetwork"""

    ## BEGIN tests
    ##############################################################################################

    # test for single ipv4 and single ipv6 interface