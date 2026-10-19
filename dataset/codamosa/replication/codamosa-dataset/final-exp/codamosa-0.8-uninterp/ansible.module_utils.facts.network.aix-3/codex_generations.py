

# Generated at 2022-06-13 01:16:56.419835
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    from ansible.module_utils.facts.network.base import NetworkCollector
    from ansible.module_utils.facts.network.aix import AIXNetwork

    assert NetworkCollector._platform == 'Generic'
    assert NetworkCollector._fact_class == None

    collector = AIXNetworkCollector()
    assert collector._platform == 'AIX'
    assert collector._fact_class.__name__ == AIXNetwork.__name__


# Generated at 2022-06-13 01:16:58.587012
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    A = AIXNetworkCollector()
    assert A.platform == AIXNetworkCollector._platform
    assert A.fact_class == AIXNetworkCollector._fact_class


# Generated at 2022-06-13 01:17:08.573798
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    module = NetworkCollector()
    data = module.get_interfaces_info('/usr/sbin/ifconfig -a')
    assert len(data) == 1
    assert data[0]['device'] == 'lo0'
    assert len(data[0]['ipv6']) == 1
    assert data[0]['ipv6'][0]['address'] == '::1'
    assert len(data[0]['ipv4']) == 1
    assert data[0]['ipv4'][0]['broadcast'] == '127.0.255.255'
    assert data[0]['ipv4'][0]['netmask'] == '255.0.0.0'
    assert data[0]['ipv4'][0]['address'] == '127.0.0.1'

# Generated at 2022-06-13 01:17:13.618428
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    module = AnsibleModule(argument_spec={})
    module.params['gather_subset'] = ['!all', '!min']

    test_aixnetwork = AIXNetwork(module)
    route_path = '/etc/route'
    (v4gw, v6gw) = test_aixnetwork.get_default_interfaces(route_path)
    result = {}
    result['v4'] = v4gw
    result['v6'] = v6gw
    module.exit_json(ansible_facts={'ansible_network_resources': result})



# Generated at 2022-06-13 01:17:24.101259
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    from ansible.module_utils.facts.network.common import NetworkCollector
    from ansible.module_utils.facts.network.aix import AIXNetworkCollector
    from ansible.module_utils.facts.network.network_acl import NetworkACL
    from ansible.module_utils.facts.network.base import Network

    ifconfig_path = '/usr/sbin/ifconfig'
    ifconfig_options = '-a'

    # create AIXNetworkCollector class
    aixnetworkcollector = AIXNetworkCollector()
    # mock the network collector class with class aixnetworkcollector
    networkcollector = NetworkCollector(None)
    networkcollector.network = aixnetworkcollector

    # create NetworkACL class
    networkacl = NetworkACL(None)

    # create Network class
    network = Network

# Generated at 2022-06-13 01:17:34.816766
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():

    class ModuleMock:

        def get_bin_path(self, arg):
            return "/usr/bin/netstat"


# Generated at 2022-06-13 01:17:35.670390
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    assert AIXNetworkCollector.__doc__ is not None

# Generated at 2022-06-13 01:17:42.824735
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    """ Below is the output of 'ifconfig -a' from a AIX machine """

# Generated at 2022-06-13 01:17:54.822185
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    module = AnsibleModule(argument_spec=dict())

# Generated at 2022-06-13 01:18:03.771015
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():

    from ansible.module_utils.facts import NetworkingFactCollector
    from ansible.module_utils.facts import Networking

    # Mock NetworkingFactCollector().collect() call
    m_collect = NetworkingFactCollector.collect
    NetworkingFactCollector.collect = lambda self: {
        'collectors': [
            {'proto': 'inet', 'route_path': '/usr/bin/netstat'},
            {'proto': 'inet6', 'route_path': 'netstat6'}
        ],
        'defaults': {
            'proto': 'inet',
            'route_path': '/usr/bin/netstat'
        },
        'platform': 'AIX',
        'version': '7.2'
    }

    # Mock NetworkingFactCollector().get_default_interfaces()

# Generated at 2022-06-13 01:18:18.559952
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    network_collector = AIXNetworkCollector()
    network_collector.collect()

# Generated at 2022-06-13 01:18:28.664120
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    test_module = NetworkCollector._create_module('AIX')

    # Normal case - there is 'default' line in the output
    route_path = '/sbin/route'
    test_module.run_command.return_value = (0, 'get_default_interfaces_in', '')
    iface = AIXNetwork(test_module)
    gateway, interface = iface.get_default_interfaces(route_path)
    assert gateway == '0.0.0.0' and interface == 'en0'

    # Error case - there is no 'default' line in the output
    test_module.run_command.return_value = (0, 'get_default_interfaces_out', '')
    gateway, interface = iface.get_default_interfaces(route_path)
    assert gateway == '' and interface

# Generated at 2022-06-13 01:18:39.812276
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    net = AIXNetwork()
    net.module.run_command = lambda cmd, check_rc=True: (0, '\n'.join([
        'default 192.168.0.1         UGS         0        5 en0',
        'default 192.168.0.1         UGS         0        7 en1',
        'ff02::1:ffe5:f3b6/64        UGRS        0        2 en0',
        'ff02::1:ffe5:f3b6/64        UGRS        0        2 en1',
    ]), '')
    v4, v6 = net.get_default_interfaces(route_path=None)
    assert v4 == {'gateway': '192.168.0.1', 'interface': 'en0'}

# Generated at 2022-06-13 01:18:44.188797
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    ifconfig_out = """
en0: flags=1e084863,480<UP,BROADCAST,NOTRAILERS,RUNNING,SIMPLEX,MULTICAST,GROUPRT,64BIT,CHECKSUM_OFFLOAD(ACTIVE),CHAIN>
        inet 172.17.245.154 netmask 0xffffff80 broadcast 172.17.245.255
        tcp_sendspace 65536 tcp_recvspace 65536 rfc1323 1
        ip6 ::1%1/0
        options=3<RXCSUM,TXCSUM>
"""
    module = AnsibleModule(argument_spec=dict())
    aixnet = AIXNetwork(module)
    def_v4, def_v6 = aixnet.get_default_interfaces('/usr/bin/netstat')


# Generated at 2022-06-13 01:18:47.552303
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    assert AIXNetworkCollector._platform == 'AIX'
    assert AIXNetworkCollector._fact_class == AIXNetwork

# unit test for constructor of class AIXNetwork

# Generated at 2022-06-13 01:18:57.204866
# Unit test for method get_default_interfaces of class AIXNetwork

# Generated at 2022-06-13 01:19:08.976350
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():

    class Args(object):
        def __init__(self, options='-a'):
            self.options = options

    class MockModule(object):
        def run_command(self, command):
            rc = 0

# Generated at 2022-06-13 01:19:20.833884
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    from ansible import module_utils
    from ansible.module_utils.facts.network.net_tools import NetTools
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes

    module = basic.AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )

    module_utils.basic._ANSIBLE_ARGS = to_bytes('')

    # run_command gets mocked

# Generated at 2022-06-13 01:19:31.821500
# Unit test for method get_interfaces_info of class AIXNetwork

# Generated at 2022-06-13 01:19:32.922306
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    aix_net = AIXNetworkCollector()
    assert aix_net._fact_class.platform == 'AIX'


# Generated at 2022-06-13 01:19:57.973577
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    aix = AIXNetworkCollector()
    assert aix.platform == 'AIX'
    assert aix.fact_class == AIXNetwork
    assert isinstance(aix.fact_class(), AIXNetwork)

# Generated at 2022-06-13 01:20:09.190424
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    class module:
        def __init__(self):
            self.fail_json = False
        def get_bin_path(self, bin):
            return bin
        def run_command(self, command):
            output = None
            if command[0] == 'uname' and command[1] == '-W':
                # unit test is run on standard AIX 7.1 system
                output = '0', '0', None
            elif command[0] == 'ifconfig':
                if command[1] == '-a':
                    output = 0, ifconfig_out, None
            if self.fail_json:
                output = 1, None, None
            return output

    def test_one_interface(ifconfig_out):
        module.fail_json = False
        network = AIXNetwork()

# Generated at 2022-06-13 01:20:14.781971
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    test_vm = AIXNetwork()

    default_interfaces = test_vm.get_default_interfaces('/usr/sbin/netstat')
    assert default_interfaces[0] == {'gateway': '10.0.2.2', 'interface': 'en0'}, 'test1'
    assert default_interfaces[1] == {}, 'test2'



# Generated at 2022-06-13 01:20:22.713980
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():

    interfaces = {}
    current_if = {}
    ips = dict(
        all_ipv4_addresses=[],
        all_ipv6_addresses=[],
    )

    uname_rc = None
    uname_out = None
    uname_err = None
    uname_path = 'uname'
    uname_rc, uname_out, uname_err = 123, '0', ''


# Generated at 2022-06-13 01:20:33.413739
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():

    module = AnsibleModule(argument_spec=dict())
    ifconfig_path = module.get_bin_path('ifconfig')

    # Fake class
    class AIXNetwork():
        def __init__(self):
            self.module = module

    aixn = AIXNetwork()
    interfaces, ips = aixn.get_interfaces_info(ifconfig_path, ifconfig_options='-a')

    assert interfaces is not None

    # There is only one interface in my test env.
    # Will skip the loop below (to avoid TypeError) if no interface.
    if len(interfaces) > 0:
        # test results of method parse_interface_line
        for key, value in interfaces.items():
            assert 'flags' in value
            assert 'device' in value
            assert 'ipv4' in value


# Generated at 2022-06-13 01:20:38.232548
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    facts = AIXNetworkCollector(None, None).collect()
    assert 'default_ipv4' in facts
    assert 'default_ipv6' in facts
    assert 'interfaces' in facts
    assert 'all_ipv4_addresses' in facts
    assert 'all_ipv6_addresses' in facts

# Generated at 2022-06-13 01:20:47.020323
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    """ test method get_default_interfaces of class AIXNetwork """
    class AnsibleModuleFake(object):
        """ class AnsibleModuleFake as a stand-in for class AnsibleModule """
        def __init__(self, params):
            self.params = params

        def run_command(self, command):
            """ method run_command as a stand-in for actual Ansible.run_command """
            self.command = command
            self.rc = 0
            self.out = "default 10.0.0.1 UG en0\ndefault 192.168.20.1 UG en1"
            self.err = "Success"
            return self.rc, self.out, self.err


# Generated at 2022-06-13 01:20:57.732032
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )
    
    env_facts = dict(
        ansible_facts=dict(
            ansible_interfaces=["eth0", "eth1"],
        )
    )

    aixnetwork = AIXNetwork(module, env_facts)
    all_interfaces, ips = aixnetwork.get_interfaces_info(ifconfig_path="/usr/sbin/ifconfig", ifconfig_options="-a")

    # all_interfaces = {'eth0': {'device': 'eth0',
    #                            'flags': ['broadcast', 'multicast'],
    #                            'inet6': ['fe80::214:4dff:fe27:9a54', '2a02:8103:

# Generated at 2022-06-13 01:21:04.088529
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    """
    This test checks if the constructor of the class AIXNetworkCollector
    works correctly.
    Parameters:

    Returns:

    """
    module = AnsibleModuleMock()
    obj = AIXNetworkCollector(module)
    assert obj._platform == 'AIX'
    assert obj._fact_class is AIXNetwork


if __name__ == '__main__':
    my_obj = AIXNetworkCollector(AnsibleModuleMock())
    my_obj.collect()
    print(my_obj.get_facts())

# Generated at 2022-06-13 01:21:10.871886
# Unit test for method get_interfaces_info of class AIXNetwork

# Generated at 2022-06-13 01:22:02.850110
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    module = AnsibleModule(
        argument_spec={
            'gather_subset': dict(default=['!all'], type='list'),
        },
        supports_check_mode=True
    )
    # init network
    network_collector = AIXNetworkCollector(module=module)
    assert network_collector, 'NetworkCollector init failed'
    assert network_collector.module == module
    assert network_collector.network.module == module


# Generated at 2022-06-13 01:22:04.929159
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    my_class = AIXNetworkCollector()
    assert my_class._fact_class == AIXNetwork
    assert my_class._platform == 'AIX'

# Generated at 2022-06-13 01:22:06.923356
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    assert AIXNetworkCollector._platform == 'AIX'
    assert AIXNetworkCollector._fact_class == AIXNetwork
    assert AIXNetworkCollector.platforms == ('AIX',)


# Generated at 2022-06-13 01:22:12.112959
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )
    net = AIXNetwork(module=module)

    result = net.get_default_interfaces(route_path=None)
    assert result == (
        {'gateway': '192.168.0.254', 'interface': 'en3'},
        {'gateway': 'fe80::1', 'interface': 'en3'}
    )



# Generated at 2022-06-13 01:22:17.072978
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    AIXModule = AnsibleModule(argument_spec={})
    AIXNetwork = AIXNetwork(AIXModule)
    ifconfig_path = 'tests/unit/module_utils/facts/network/bsd/ifconfig'
    res = AIXNetwork.get_interfaces_info(ifconfig_path)
    if len(res[0]) == 0 or len(res[1]) == 0:
        print("\nAIXNetwork.get_interfaces_info() is failed\n")
        sys.exit(1)



# Generated at 2022-06-13 01:22:27.781095
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    import re
    from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork
    testclass = AIXNetwork()
    test_get_interfaces_info = testclass.get_interfaces_info
    test_get_interfaces_info.__func__.__globals__['re'] = re
    test_get_interfaces_info.__func__.__globals__['GenericBsdIfconfigNetwork'] = GenericBsdIfconfigNetwork
    test_get_interfaces_info.__globals__['re'] = re
    test_get_interfaces_info.__globals__['GenericBsdIfconfigNetwork'] = GenericBsdIfconfigNetwork
    result = test_get_interfaces_info('/usr/sbin/ifconfig', '-a')
    num_

# Generated at 2022-06-13 01:22:35.946955
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    module = AnsibleModule(argument_spec=dict())
    path_list = dict(
        ifconfig_path='/usr/bin/ifconfig'
    )
    test_obj = AIXNetwork(module, path_list)

    rc_out_err = dict(
        rc=0,
        out=read_data_from_file('tests/unit/module_utils/facts/network/test_AIXNetwork_get_interfaces_info'),
        err=None
    )
    modules.run_command = Mock(return_value=rc_out_err)

    interfaces, ips = test_obj.get_interfaces_info('/usr/bin/ifconfig', ifconfig_options='-a')

    assert 'lo0' in interfaces
    assert interfaces['lo0']['type'] == 'unknown'
    assert interfaces

# Generated at 2022-06-13 01:22:37.991637
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    aix = AIXNetwork()
    aix.get_default_interfaces('/usr/sbin/route')



# Generated at 2022-06-13 01:22:47.332122
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    module = FakeModule()
    network_collector = AIXNetwork(module)
    rc, out, err = module.run_command(['netstat', '-nr'])

    out_lines = out.splitlines()
    for line in out_lines:
        words = line.split()
        if len(words) > 1 and words[0] == 'default':
            if '.' in words[1]:
                assert network_collector.get_default_interfaces(['netstat', '-nr'])[0]['gateway'] == words[1]
                assert network_collector.get_default_interfaces(['netstat', '-nr'])[0]['interface'] == words[5]

# Generated at 2022-06-13 01:22:53.955891
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork
    if_path = '/etc/ansible/facts.d/'
    ifconfig_path = '/usr/bin/ifconfig'
    ifconfig_options = '-a'
    # Load test data
    with open(if_path + 'ifconfig_AIX.txt', 'r') as test_data:
        test_data = test_data.read()
    # Create instance of class AIXNetwork
    an = AIXNetwork(module=None, ifconfig_path=ifconfig_path)
    # Create instance of class GenericBsdIfconfigNetwork
    gb = GenericBsdIfconfigNetwork(module=None, ifconfig_path=ifconfig_path)
    # Replace get_cmd_data method of object gb by mock method

# Generated at 2022-06-13 01:24:28.021835
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    assert AIXNetworkCollector.platform == "AIX"
    assert AIXNetworkCollector._platform == "AIX"
    assert AIXNetworkCollector.fact_class == AIXNetwork
    assert AIXNetworkCollector._fact_class == AIXNetwork

# Generated at 2022-06-13 01:24:37.464279
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    from ansible.module_utils.facts.network.aix.collector import AIXNetworkCollector

    defaults = dict(
        ansible_python_interpreter='/usr/bin/python3',
        ansible_facts=dict(
            ansible_net_gather_network_resources='no',
        ),
    )

    module = FakeModule(**defaults)
    module.run_command = run_command_mock
    module.get_bin_path = get_bin_path_mock

    network_collector = AIXNetworkCollector(module=module)
    ifconfig_path = network_collector.get_bin_path(name='ifconfig')

    interfaces = network_collector.get_default_interfaces(ifconfig_path)

# Generated at 2022-06-13 01:24:45.466260
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    collector = AIXNetworkCollector()
    network = AIXNetwork(module=None)

    v4_exp = dict(gateway='10.0.0.1', interface='en0')
    v6_exp = dict(gateway='fe80::21e:c7ff:fe77:1', interface='en0')
    out = '''default 10.0.0.1         UG        0 0        en0
default fe80::21e:c7ff:fe77:1 UG        0 0        en0'''
    v4_act, v6_act = network.get_default_interfaces(route_path='/sbin/route')
    assert v4_exp == v4_act
    assert v6_exp == v6_act


# Generated at 2022-06-13 01:24:51.527300
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    import sys
    import platform

    class MockModule(object):
        def __init__(self, platform, uname_path=None, uname_stdout=None,
                     ifconfig_path=None, ifconfig_stdout=None, entstat_path=None,
                     entstat_stdout=None, lsattr_path=None, lsattr_stdout=None):
            self.platform = platform
            self.params = {
                'gather_subset': ['all'],
                'gather_network_resources': ['all'],
            }

            self.bin_path_cache = {}

            self.run_command_calls = []

            def mock_run_command(args, check_rc=False):
                self.run_command_calls.append(args)

# Generated at 2022-06-13 01:24:56.907118
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    class Mod(object):
        def __init__(self):
            self.bin_path = {}
        def get_bin_path(self, arg):
            return self.bin_path.get(arg, '')
        def run_command(self, arg):
            return (0, '', '')
    m = Mod()
    m.bin_path = {}
    assert AIXNetwork().get_default_interfaces('') == ({}, {})
    m.bin_path = {'netstat': '/bin/netstat'}

# Generated at 2022-06-13 01:24:59.228367
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    network_collector = AIXNetworkCollector()
    assert network_collector._platform == 'AIX'



# Generated at 2022-06-13 01:25:05.369380
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )
    a = AIXNetwork()

    v4_returned = a.get_default_interfaces(module)[0]
    assert 'gateway' in v4_returned
    assert 'interface' in v4_returned

    v6_returned = a.get_default_interfaces(module)[1]
    assert 'gateway' in v6_returned
    assert 'interface' in v6_returned


if __name__ == '__main__':
    from ansible.module_utils.basic import *
    main()

# Generated at 2022-06-13 01:25:13.221673
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    net_collector = AIXNetworkCollector()
    net = AIXNetwork('/', net_collector)
    test_result = net.get_default_interfaces("/sbin/route")
    assert len(test_result) == 2
    assert '192.168.1.1' in test_result[0].values()
    assert '192.168.1.1' not in test_result[1].values()
    assert '2001:0db8:85a3:0000:0000:8a2e:0370:7334' in test_result[1].values()
    assert '2001:0db8:85a3:0000:0000:8a2e:0370:7334' not in test_result[0].values()


# Generated at 2022-06-13 01:25:14.591524
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    assert AIXNetworkCollector._platform == 'AIX'
    assert AIXNetworkCollector._fact_class == AIXNetwork

# Generated at 2022-06-13 01:25:21.206598
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts.collector import TestModule
    from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork

    test_module = TestModule()
    test_module.params = {}
    test_module.run_command = lambda args, check_rc=True: (0, '', '')

    network = AIXNetwork(test_module)

    ifconfig_path = '/usr/bin/ifconfig'
    ifconfig_options = '-a'
    interfaces = {}