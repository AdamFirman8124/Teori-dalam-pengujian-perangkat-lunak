

# Generated at 2022-06-13 01:17:05.489286
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    AIX_ifconfig_path = '/sbin/ifconfig'
    AIX_get_interfaces_info = AIXNetwork.get_interfaces_info

# Generated at 2022-06-13 01:17:11.300161
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    module = mock.Mock()
    module.run_command.return_value = (0, "default test-r1-eth0 UGS 20 0 en4", "")

    net = AIXNetwork()
    net.module = module
    net.get_interfaces_info = mock.Mock()

    net.get_interfaces_info.return_value = (dict(), dict())

    interface = net.get_default_interfaces(route_path="/usr/sbin/route")

    assert interface == { 'interface': 'en4' }



# Generated at 2022-06-13 01:17:14.219277
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    _fact_class = AIXNetworkCollector()
    assert _fact_class.get_facts()

# Generated at 2022-06-13 01:17:16.805664
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():

    network_collector = AIXNetworkCollector()
    assert network_collector._platform == 'AIX'
    assert network_collector._fact_class == AIXNetwork



# Generated at 2022-06-13 01:17:24.863382
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    aix_network = AIXNetwork()
    aix_network.module = Mock()
    setattr(aix_network.module, '_is_platform', lambda x: True)
    setattr(aix_network.module, 'run_command',
            lambda x: (0, 'default 192.168.122.1 UG en0\ndefault :: UG en1', ''))
    assert aix_network.get_default_interfaces('nothing') == ({'interface': 'en0', 'gateway': '192.168.122.1'},
                                                            {'interface': 'en1', 'gateway': '::'})

# Generated at 2022-06-13 01:17:33.899397
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    from collections import namedtuple
    from ansible.module_utils.facts.facts import Facts
    from ansible.module_utils.facts.network.base import NetworkCollector

    module = namedtuple('module', ['run_command', 'get_bin_path'])
    module.run_command = lambda command, check, encoding=None: ['', '', '']
    module.get_bin_path = lambda argument: ''
    network_collector = AIXNetworkCollector(module, Facts())
    assert type(network_collector) == NetworkCollector
    assert network_collector.network._platform == 'AIX'



# Generated at 2022-06-13 01:17:41.647996
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():

    # Stub class for class Network
    class StubModule:

        # Stub method for method run_command
        @staticmethod
        def run_command(args):

            if args[1] == '-W':
                rc = 0
                # Test of method get_interfaces_info when WPAR is not used
                out = '0'
                # Test of method get_interfaces_info when WPAR is used
                # out = '1'
                err = ''
            elif args[1] == '-nr':
                rc = 0

# Generated at 2022-06-13 01:17:46.203697
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    fact_class = AIXNetwork

    arg1 = fact_class('test_module')

    assert arg1.platform == 'AIX'
    assert arg1.module_name == 'test_module'
    assert arg1.module is None


# Generated at 2022-06-13 01:17:56.941840
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    import sys
    import os
    import unittest

    # Stub AIXNetwork class
    class AIXNetwork(GenericBsdIfconfigNetwork):
        def __init__(self, module, ifconfig_path):
            self.module = module
            self.ifconfig_path = ifconfig_path

    # Stub AnsibleModule
    class AnsibleModule:
        def __init__(self, ifconfig_path):
            self.ifconfig_path = ifconfig_path
            self.args = {}
            self.params = {}

        def get_bin_path(self, program):
            return self.ifconfig_path

        def run_command(self, command):
            return 0, "", ""

    # Stub system
    class System:
        def __init__(self, module, ifconfig_path):
            self.AIX

# Generated at 2022-06-13 01:18:05.540930
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    import sys
    import json
    import os.path

    test_dir = os.path.dirname(os.path.realpath(__file__))
    test_file = os.path.join(test_dir, 'test_AIXNetwork.json')

    with open(test_file) as data_file:
        data = json.load(data_file)
    # prepare arguments
    ifconfig_path = os.path.join(test_dir, 'ifconfig_aix')

    module = sys.modules['__main__']
    module.run_command = lambda cmd: (0, data['run_command_output'], '')

    # AIXNetwork is a class, not a method, so we need to instantiate it
    net = AIXNetwork()

    net.module = module

# Generated at 2022-06-13 01:18:23.416305
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    if_1 = AIXNetwork()
    interfaces = if_1.get_default_interfaces('/usr/sbin/route')
    assert "gateway" in interfaces[0]
    assert "interface" in interfaces[0]
    assert "ipv6" in interfaces[1]


# Generated at 2022-06-13 01:18:29.655670
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    fake_module = type("AnsibleModule", (object,), {"fail_json": lambda self, *args, **kwargs: None, "run_command": lambda self, *args, **kwargs: (0, "default 9.35.147.171 UG 1 0 en0", '')})
    fake_module.get_bin_path = lambda self, *args, **kwargs: "/usr/bin/netstat"
    aix_network = AIXNetwork(fake_module)
    assert aix_network.get_default_interfaces("/path/to/route") == ({'gateway': '9.35.147.171', 'interface': 'en0'}, {})

# Generated at 2022-06-13 01:18:40.310119
# Unit test for method get_interfaces_info of class AIXNetwork

# Generated at 2022-06-13 01:18:51.849787
# Unit test for method get_interfaces_info of class AIXNetwork

# Generated at 2022-06-13 01:19:00.270391
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():

    class Module():
        def __init__(self, run_command_results, path_results):
            self.run_command_results = run_command_results
            self.path_results = path_results
            self.run_command_calls = 0
            self.get_bin_path_calls = 0

        def get_bin_path(self, value, opt_dirs=[]):
            self.get_bin_path_calls += 1
            # only netstat uses opt_dirs
            if opt_dirs:
                return '/usr/bin/netstat'
            return self.path_results[value]

        def run_command(self, args, check_rc=True):
            self.run_command_calls += 1
            # only netstat should have opt_dirs

# Generated at 2022-06-13 01:19:02.675856
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    collector = AIXNetworkCollector(dict())
    assert collector._fact_class == AIXNetwork
    assert collector._platform == 'AIX'

# Generated at 2022-06-13 01:19:12.057620
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():

    module = AnsibleModule(argument_spec={})
    module.params = dict()

    # success
    rc = 0
    test_out = '''
192.168.2.1        link#2             UHS         0        0   em0
default            192.168.2.1        UGS         0        8   em0
'''
    test_err = ''

    module.run_command = lambda args, check_rc=True: (rc, test_out, test_err)

    try:
        aix_network = AIXNetwork(module)
    except:
        assert False, 'Cannot create AIXNetwork instance'

    v4_interface, v6_interface = aix_network.get_default_interfaces('/sbin/route')

# Generated at 2022-06-13 01:19:21.477276
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    """
    Constructor for the AIXNetworkCollector class.
    """
    from ansible_collections.ansible.community.plugins.module_utils.facts.network.aix import AIXNetworkCollector
    from ansible.module_utils.facts.network.base import NetworkConfig
    from ansible.module_utils.facts.network.generic_bsd import AIXNetwork

    # Constructor with no options
    AIXNetworkCollector()

    # Constructor with options
    AIXNetworkCollector(gather_subset=NetworkConfig().gather_subset)
    AIXNetworkCollector(gather_network_resources=NetworkConfig().gather_network_resources)

    # Constructor with unsupported options
    AIXNetworkCollector(gather_subset=['!all'])

# Generated at 2022-06-13 01:19:24.516416
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    expected = AIXNetworkCollector
    actual = AIXNetworkCollector()
    assert isinstance(actual, expected)


# Generated at 2022-06-13 01:19:25.663119
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    module = MagicMock()
    AIXNetworkCollector(module)

# Generated at 2022-06-13 01:19:57.986321
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    from collections import namedtuple
    from ansible.module_utils.facts.network.base import NetworkCollector

    MockModule = namedtuple('MockModule', ['run_command', 'get_bin_path'])

    ifconfig_path = '/usr/bin/ifconfig'
    ifconfig_result = (0, ifconfig_output, '')

# Generated at 2022-06-13 01:20:09.190444
# Unit test for method get_interfaces_info of class AIXNetwork

# Generated at 2022-06-13 01:20:16.628515
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():

    from ansible.module_utils.facts import ansible_aix_network as aix_network

    aix_network.run_command = lambda x: (0, 'default  gateway  x.x.x.x  UG         1  0  en0', '')
    aix_network.get_bin_path = lambda x: '/usr/bin/netstat' in x
    aix_net = aix_network.AIXNetwork()
    assert aix_net.get_default_interfaces('/usr/sbin/route') == ('x.x.x.x', None)

# Generated at 2022-06-13 01:20:24.137374
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    """ Test get_default_interfaces of AIXNetwork class

    Test will be run on AIX 7.1 TL1 SP2
    """
    net = AIXNetwork()
    net.module = MockModule()
    route_path = net.module.get_bin_path('route')
    if route_path is None:
        route_path = net.module.get_bin_path('netstat')

    # netstat output when no default gateway is set

# Generated at 2022-06-13 01:20:35.095850
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    uname_path = NetworkCollector().module.get_bin_path('uname')
    rc, out, err = NetworkCollector().module.run_command([uname_path, '-W'])
    if out.split()[0] == '0':
        import sys
        sys.stderr.write('Wrong WPAR name found, exiting unit test.\n')
        sys.exit(1)

    aix_network = AIXNetwork()

    route_path = aix_network.module.get_bin_path('route')
    if route_path:
        rc, out, err = NetworkCollector().module.run_command([route_path, '-n'])
        v4, v6 = aix_network.get_default_interfaces(route_path)
        assert len(v4) == 0

# Generated at 2022-06-13 01:20:45.107961
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    from ansible.module_utils.facts.network.aix import AIXNetwork
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes
    m = basic.AnsibleModule(
        argument_spec=dict(
            gather_subset=dict(default=["!all", "!min"], type='list')
        )
    )
    result = dict(interfaces={}, ansible_all_ipv4_addresses=[], ansible_all_ipv6_addresses=[], changed=False)
    AixNetwork = AIXNetwork()
    interfaces, ips = AixNetwork.get_interfaces_info(AixNetwork.module.get_bin_path('ifconfig'))


# Generated at 2022-06-13 01:20:49.077319
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    network_collector = AIXNetworkCollector()

    # Check platform attribute
    assert hasattr(network_collector, 'platform')
    assert network_collector.platform == 'AIX'
    assert network_collector._platform == 'AIX'

    # Check fact_class attribute
    assert hasattr(network_collector, 'fact_class')
    assert network_collector.fact_class == AIXNetwork
    assert network_collector._fact_class == AIXNetwork

# Generated at 2022-06-13 01:20:50.236495
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():

    AIXNetworkCollector()

# Generated at 2022-06-13 01:20:51.197483
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    net = AIXNetworkCollector()



# Generated at 2022-06-13 01:21:01.190716
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    module = AnsibleModule(argument_spec={})
    rc, out, err = module.run_command('ls -l /usr/sbin/ifconfig')
    if rc != 0:
        module.fail_json(msg="ifconfig command not found")
    ifconfig_path = '/usr/sbin/ifconfig'
    ifconfig = 'lo0: flags=8049<UP,LOOPBACK,RUNNING,MULTICAST> mtu 65536 \
                index 1\n        inet 127.0.0.1 netmask 0xff000000 \
                broadcast 127.255.255.255\n        ether 0:0:0:0:0:0 \
                media: Ethernet autoselect (100baseTX <full-duplex>)\n        status: active\n'
    interfaces, ips = AIXNetwork().get_

# Generated at 2022-06-13 01:21:56.150787
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    result = dict(
            all_ipv4_addresses=[],
            all_ipv6_addresses=[],
            default_ipv4_address=dict(gateway='192.168.0.1', interface='en0'),
            default_ipv6_address=dict(gateway='fe80::5054:ff:fe46:b1c7', interface='en0'),
    )
    uname_rc = 0
    uname_out = '0'
    uname_err = ''
    netstat_path = '/usr/sbin/netstat'
    netstat_rc = 0

# Generated at 2022-06-13 01:22:06.490913
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    aix_net = AIXNetwork()

    # must return a dict with keys == ['v4']['interface', 'gateway'] or ['v6']['interface', 'gateway']
    assert aix_net.get_default_interfaces(route_path='/usr/bin/netstat') == ({'interface': 'en0', 'gateway': '192.168.1.2'}, {'interface': 'en0', 'gateway': 'fe80::800:27ff:fe00:0'})

    # must return a dict with keys == ['v4']['interface', 'gateway'] or ['v6']['interface', 'gateway']
    assert aix_net.get_default_interfaces(route_path='/usr/bin/test_netstat') == ({}, {})

    # must return a dict with

# Generated at 2022-06-13 01:22:08.009245
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    # test without parameters
    instance = AIXNetworkCollector()
    assert (isinstance(instance.facts, AIXNetwork))


# Generated at 2022-06-13 01:22:10.199226
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    network = AIXNetworkCollector()
    assert network.__class__.__name__ == 'AIXNetworkCollector'
    assert network.platform == 'AIX'

# Generated at 2022-06-13 01:22:12.910090
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    module = AnsibleModuleMock()
    ansible_facts = dict()
    up = AIXNetworkCollector(module=module, ansible_facts=ansible_facts)
    assert up.platform == 'AIX'



# Generated at 2022-06-13 01:22:19.319514
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    from ansible.module_utils.facts import ModuleDataConsumer
    from ansible.module_utils.facts.network.base import NetworkCollector

    facts = {u'kernel': u'AIX'}
    module_data_consumer = ModuleDataConsumer(facts)
    net_collector = NetworkCollector()
    net_collector._module_data_consumer = module_data_consumer
    aix_network = AIXNetwork()
    aix_network._module = net_collector._module_data_consumer
    output = aix_network.get_default_interfaces(route_path='/usr/sbin/netstat')

    assert(output[0]['interface'] == 'en0')
    assert(output[0]['gateway'] == '172.21.33.254')

# Generated at 2022-06-13 01:22:29.300480
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts.facts import ansible_facts
    from ansible.module_utils.facts.network.aix import AIXNetwork

# Generated at 2022-06-13 01:22:31.570074
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    """
    Instantiate a AIXNetworkCollector class
    """
    collector = AIXNetworkCollector()
    assert isinstance(collector, NetworkCollector)

# Generated at 2022-06-13 01:22:38.492438
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():

    class FakeModule(object):
        def __init__(self, **kwargs):
            self.params = kwargs

        def fail_json(self, *args, **kwargs):
            pass

        def get_bin_path(self, name, **kwargs):
            if name in ('netstat', 'route'):
                return name

        def run_command(self, args, **kwargs):
            # Return route command output
            if args[0] == 'route':
                if '-4' in args:
                    out = """
Destination        Gateway            Flags   Ref      Use     Interface    MSS    MTU    RTT    Window  IRTT
default            10.0.0.1           UG          2        0      en0           0      -      -      -       -
"""

# Generated at 2022-06-13 01:22:40.703532
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    # Test that object is initialized without fail
    NetworkCollector()

# Generated at 2022-06-13 01:24:22.387961
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    module = AnsibleModuleMock()
    ifconfig_path = '/usr/sbin/ifconfig'
    ifconfig_options = '-a'

# Generated at 2022-06-13 01:24:31.493276
# Unit test for method get_interfaces_info of class AIXNetwork

# Generated at 2022-06-13 01:24:38.457168
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    # Create test object
    network_collector = AIXNetworkCollector()
    network_fact_class = network_collector._fact_class
    net_fact_instance = network_fact_class(dict(module=dict(run_command=run_command_mock)))

    # Call test method
    v4, v6 = net_fact_instance.get_default_interfaces('/usr/bin/netstat')

    assert v4['gateway'] == '10.0.2.2'
    assert v4['interface'] == 'lo0'
    assert not v6



# Generated at 2022-06-13 01:24:46.544510
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    class FakeModule(object):
        class FakeRunCommand(object):
            def __init__(self):
                self.count = 0
            def run_command(self, args):
                if 'uname' in args:
                    # uname_path is present (count == 0) so this is the first command run
                    if self.count == 0:
                        self.count += 1
                        return 0, '0', ''
                    # uname_path not present (count == 1) so this is the second command run
                    if self.count == 1:
                        self.count += 1
                        return 1, '', ''
                if 'netstat' in args:
                    # netstat_path is present (count == 2) so this is the third command run
                    if self.count == 2:
                        self.count += 1

# Generated at 2022-06-13 01:24:52.987613
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    module = type('', (), {'get_bin_path': lambda self, x: 'bin_path', 'run_command': lambda self, x: (0, '', '')})()
    network = AIXNetwork(module)

    import os
    import sys
    import imp
    import re

    # Step 1: get a list of all test files, then load and process them one by one
    test_dir = os.path.dirname(os.path.realpath(sys.argv[0])) + "/AIXNetwork_get_interfaces_info"
    files = os.listdir(test_dir)

    # Step 2: sort the test files to make sure they are processed in the right order
    files.sort()

# Generated at 2022-06-13 01:24:57.461575
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    module = AnsibleModuleMock()
    module.run_command.return_value = (0, 'default 192.168.1.1 UG en0', '')
    network = AIXNetwork(module)
    interface = network.get_default_interfaces('path')
    assert interface == {'gateway': '192.168.1.1', 'interface': 'en0'}


# Generated at 2022-06-13 01:25:00.958164
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    aix_network = AIXNetworkCollector()
    assert type(aix_network) == AIXNetworkCollector
    assert aix_network._platform == 'AIX'
    assert aix_network._fact_class == AIXNetwork
    assert type(aix_network._fact_class) == type


# Generated at 2022-06-13 01:25:02.609726
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    collector = AIXNetworkCollector()
    assert collector.ipv6_enabled() is True
    assert collector.platform == 'AIX'

# Generated at 2022-06-13 01:25:10.285262
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    module = AnsibleModule(argument_spec=dict())

# Generated at 2022-06-13 01:25:18.102979
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    module = AnsibleModule('')
    # fake the module
    module.get_bin_path = fake_get_bin_path
    # fake the interface lines
    rc, out, err = 0, aix_ifconfig_lines, ''

    # create the network class
    network_class = AIXNetwork(module)

    # call the method
    interfaces, ips = network_class.get_interfaces_info('ifconfig', '-a')

    # check the expected results
    assert rc == 0, "rc = %d" % rc
    assert len(err) == 0, "err = %s " % err

    # print the results
    print("interfaces = {0}".format(interfaces))
    print("ips = {0}".format(ips))

    # check the interfaces