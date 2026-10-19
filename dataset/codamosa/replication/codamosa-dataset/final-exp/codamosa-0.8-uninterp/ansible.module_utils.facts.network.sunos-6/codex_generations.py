

# Generated at 2022-06-13 01:48:15.895452
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    SunOSNetworkCollector()

# Generated at 2022-06-13 01:48:16.418583
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    SunOSNetworkCollector()



# Generated at 2022-06-13 01:48:17.564998
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    f = SunOSNetworkCollector()
    assert f._fact_class == SunOSNetwork
    assert f._platform == 'SunOS'


# Generated at 2022-06-13 01:48:25.819534
# Unit test for method parse_interface_line of class SunOSNetwork
def test_SunOSNetwork_parse_interface_line():
    # prepare test data
    ifconfig_path = '/sbin/ifconfig'
    words = ['hme0:', 'flags=10000114843<UP,BROADCAST,RUNNING,MULTICAST,IPv6>', 'mtu', '1500']
    current_if = {'device': 'hme0', 'ipv4': [], 'ipv6': [], 'type': 'unknown'}
    interfaces = {}
    # run the test
    sn = SunOSNetwork()
    current_if_new = sn.parse_interface_line(words, current_if, interfaces)

    # verify results

# Generated at 2022-06-13 01:48:34.509280
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    my_obj = SunOSNetwork(None, None, None)
    my_obj.module = AnsibleModule(argument_spec={})
    my_obj.ifconfig_path = module_utils.basic.which('ifconfig')

    # Change these attributes to fit the output of the command:
    my_obj.platform = "SunOS"
    my_obj.module.run_command = lambda args: (0, OUT, "")

    interfaces, ips = my_obj.get_interfaces_info(my_obj.ifconfig_path)

    assert 'en0' in interfaces.keys()
    assert 'ipv4' in interfaces['en0'].keys()
    assert 'ipv6' in interfaces['en0'].keys()
    assert 'flags' in interfaces['en0']['ipv4'][0].keys()


# Generated at 2022-06-13 01:48:45.284487
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork
    from ansible.module_utils.facts.network.sunos import SunOSNetwork
    from ansible.module_utils.facts.network.sunos import SunOSNetworkCollector
    from ansible.module_utils.facts.network.base import NetworkCollector
    import module_utils.basic

    ifaces_info = SunOSNetworkCollector.get_interfaces_info(SunOSNetworkCollector, '/sbin/ifconfig', module_utils.basic.AnsibleModule(
    ))[0]

    # There should be at least one interface
    assert len(ifaces_info) >= 1

    # The keys of 'ifaces_info' will be the interfaces names

# Generated at 2022-06-13 01:48:55.536182
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    from ansible.module_utils.facts.network.sunos import SunOSNetwork
    from ansible.module_utils.facts.network.utils import get_file_content
    from ansible.module_utils.facts import Collector

    ifconfig_path = Collector().get_file_content('/usr/sbin/ifconfig')

    ifconfig_path = '/usr/sbin/ifconfig'
    ifconfig_output = get_file_content('/usr/sbin/ifconfig')
    sunos_ifconfig_output = get_file_content('/usr/sbin/ifconfig', 'sunos')

    def fake_run_command(self, args, check_rc=True):
        return 0, ifconfig_output, ''

    SunOSNetwork.run_command = fake_run_command

    facts = dict()
    interfaces,

# Generated at 2022-06-13 01:49:02.513655
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    module = {}

# Generated at 2022-06-13 01:49:09.791626
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():

    import sys
    # needs_type_resolution is broken in Python 3.7 with
    # TypeError: int() argument must be a string, a bytes-like object or a number, not 'NoneType'
    if sys.version_info >= (3, 7):
        return True

    from ansible.module_utils.facts.network.sunos.tests.test_sunos_network import SunOSNetwork_get_interfaces_info_output

    sunos_network_collector = SunOSNetworkCollector()
    sunos_network = sunos_network_collector.get_network_facts()

    assert sunos_network.get_interfaces_info(ifconfig_path='/sbin/ifconfig') == SunOSNetwork_get_interfaces_info_output

# Generated at 2022-06-13 01:49:12.600200
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    network_collector = SunOSNetworkCollector()
    assert network_collector.platform == 'SunOS'

# Generated at 2022-06-13 01:49:33.013964
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    module = AnsibleModule(argument_spec={'gather_subset': dict(type='list', default=['!all'])})
    network_collector = NetworkCollector(module=module, platform='SunOS')
    network_collector.collect()
    assert 'ansible_all_ipv6_addresses' in module.exit_json
    assert 'ansible_interfaces' in module.exit_json
    assert 'ansible_netmask6' in module.exit_json
    assert 'ansible_default_ipv6' in module.exit_json
    assert 'ansible_default_ipv4' in module.exit_json
    assert 'ansible_network6' in module.exit_json
    assert 'ansible_netmask' in module.exit_json
    assert 'ansible_ipv4' in module

# Generated at 2022-06-13 01:49:45.368927
# Unit test for method parse_interface_line of class SunOSNetwork
def test_SunOSNetwork_parse_interface_line():
    module = object()
    module.run_command = object()
    module.run_command.return_value = (0, '', '')
    SunOSNet = SunOSNetwork(module)

    # Test that when a new device is encountered, current_if is set to a new dict with
    # the device name and ipv4/ipv6 lists.
    assert {} == SunOSNet.parse_interface_line(['lo0:'], {}, {})

    # Test that if a device has already been seen and current_if is not empty,
    # we add the new device to interfaces and set current_if to that interface.

# Generated at 2022-06-13 01:49:52.189691
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    """
    SunOSNetwork.get_interfaces_info unit test
    """

    from ansible.module_utils.facts.network.sunos import SunOSNetwork
    from ansible.module_utils.facts.network.base import NetworkCollector
    from ansible.module_utils.facts import FactManager
    from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork
    from ansible.module_utils.facts.network import NetworkFactModule

    group_names = ['network']
    fact_manager = FactManager(
        NetworkFactModule(),
        network_collectors=NetworkCollector.get_network_collectors(group_names),
        group_names=group_names,
        )

    ifconfig_path = '/sbin/ifconfig'

# Generated at 2022-06-13 01:49:56.441596
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    module = AnsibleModuleStub()
    network = SunOSNetwork(module)

    assert network.__class__.__name__ == 'SunOSNetwork'


# Generated at 2022-06-13 01:49:58.469211
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    assert SunOSNetworkCollector.platform == 'SunOS'
    assert SunOSNetworkCollector._fact_class.platform == 'SunOS'

# Generated at 2022-06-13 01:50:02.234490
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    sunos_net = SunOSNetworkCollector(None)
    assert sunos_net.platform == 'SunOS'
    assert sunos_net.fact_class == SunOSNetwork


# Generated at 2022-06-13 01:50:02.899517
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    SunOSNetworkCollector()

# Generated at 2022-06-13 01:50:03.913667
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    assert SunOSNetworkCollector._platform == 'SunOS'


# Generated at 2022-06-13 01:50:05.485409
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    sunos_collector = SunOSNetworkCollector()
    assert sunos_collector.platform == 'SunOS'


# Generated at 2022-06-13 01:50:07.040204
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    # Test without arguments
    SunOSNetworkCollector()
    # Test with arguments
    SunOSNetworkCollector(None, None, None, None, None)

# Generated at 2022-06-13 01:50:28.834910
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    raw_out = """lo0: flags=1000849<UP,LOOPBACK,RUNNING,MULTICAST,IPv4> mtu 8232 index 1
        inet 127.0.0.1 netmask ff000000
        inet6 ::1/128 
        inet6 fe80::1:2:3:4/10
        nd6 options=21<PERFORMNUD,AUTO_LINKLOCAL>
        ether 8:0:20:1:c:35 
        media: Ethernet autoselect
        status: active
"""
    ifc = SunOSNetwork()
    result = ifc.get_interfaces_info('/sbin/ifconfig')
    assert result[0]['lo0']['ipv4'][0]['address'] == '127.0.0.1'
   

# Generated at 2022-06-13 01:50:40.875676
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():

    module = AnsibleModule(
        argument_spec = dict(),
        supports_check_mode = True,
    )

    # read test data from file
    path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'ifconfig')
    with open(path) as f:
        test_data = f.read()

    # create the object under test
    sunos_network = SunOSNetwork(module)

    # replace module.run_command() with a mock which returns testdata
    sunos_network.module.run_command = MagicMock(return_value=(0, test_data, ''))

    interfaces, ips = sunos_network.get_interfaces_info('/sbin/ifconfig')

    # get_interfaces_info() returns two dicts, interfaces and 

# Generated at 2022-06-13 01:50:43.308430
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    obj = SunOSNetworkCollector()
    assert obj._fact_class == SunOSNetwork
    assert obj._platform == 'SunOS'

# Generated at 2022-06-13 01:50:46.543151
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    sunosnc = SunOSNetworkCollector().__dict__

    assert sunosnc.get('_fact_class') == SunOSNetwork
    assert sunosnc.get('_platform') == 'SunOS'

# Generated at 2022-06-13 01:50:51.141865
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    network_collector = SunOSNetworkCollector()
    fact_class = network_collector.get_fact_class()
    assert fact_class == SunOSNetwork
    platform = network_collector.get_platform()
    assert platform == 'SunOS'

# Generated at 2022-06-13 01:51:00.836254
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    # Ansible modules do not run in a complete shell environment.
    # Fake the fact that a jdk is installed so that Solaris' 'ifconfig -a' will
    # behave like when run from a complete shell environment.
    # Refer to Solaris man page for 'ifconfig' for details.
    ifconfig_path = 'java -Djava.net.preferIPv4Stack=true sun.net.util.ip.IPAddr.ifconfig -a'

    module = FakeAnsibleModule(ifconfig_path,
                               'SunOS',
                               'ifconfig -a',
                               'facts/network/generic_bsd/ifconfig_SunOS.out')

    obj = SunOSNetwork(module)
    interfaces, ips = obj.get_interfaces_info(ifconfig_path)

    # The "status" fact

# Generated at 2022-06-13 01:51:13.021039
# Unit test for method get_interfaces_info of class SunOSNetwork

# Generated at 2022-06-13 01:51:24.779702
# Unit test for method parse_interface_line of class SunOSNetwork
def test_SunOSNetwork_parse_interface_line():
    iface = SunOSNetwork({})
    interfaces = {}
    current_if = {}
    words = ['net0:', 'flags=2001000842<UP,BROADCAST,RUNNING,MULTICAST,IPv4,'
                    'NOFAILOVER,FAILEDOVER_LEGACY,DEPRECATED,USE_FAILOVER_LINK>',
             'mtu=1500', 'index=2']
    current_if = iface.parse_interface_line(words, current_if, interfaces)
    assert current_if['device'] == 'net0'
    assert current_if['type'] == 'unknown'
    assert current_if['macaddress'] == 'unknown'


# Generated at 2022-06-13 01:51:30.282307
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    # Test data
    device1 = 'device1'
    device2 = 'device2'
    device3 = 'device3'
    ifconfig_path = '/sbin/ifconfig'
    regex_v4_inet6_line = re.compile(r'^(\S+)\s+(.*)$')

# Generated at 2022-06-13 01:51:33.976531
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    """test constructor of class SunOSNetworkCollector"""
    obj = SunOSNetworkCollector()
    assert obj.__class__.__name__ == 'SunOSNetworkCollector'

# Generated at 2022-06-13 01:51:44.619296
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    obj = SunOSNetworkCollector()
    assert obj.platform == 'SunOS'
    assert obj.fact_class == SunOSNetwork


# Generated at 2022-06-13 01:51:45.897840
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    N = SunOSNetworkCollector()
    assert N.platform == 'SunOS'

# Generated at 2022-06-13 01:51:55.875193
# Unit test for method parse_interface_line of class SunOSNetwork
def test_SunOSNetwork_parse_interface_line():
    line = 'lo0: flags=1000849<UP,LOOPBACK,RUNNING,MULTICAST,IPv4> mtu 8232'
    words = line.split()
    current_if = {}
    interfaces = {}
    net = SunOSNetwork(None)
    current_if = net.parse_interface_line(words, current_if, interfaces)
    assert current_if == {'device': 'lo0', 'ipv4': [{'flags': '1000849<UP,LOOPBACK,RUNNING,MULTICAST,IPv4>', 'mtu': '8232'}], 'ipv6': [], 'type': 'loopback', 'macaddress': 'unknown'}

# Generated at 2022-06-13 01:52:04.766752
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    from ansible.module_utils import basic
    from ansible.module_utils.facts import collector
    from ansible.module_utils._text import to_bytes

    #########################################################################
    # Mock Module
    #########################################################################
    class MockModule(object):
        @staticmethod
        def fail_json(*args, **kwargs):
            raise AssertionError('Ansible Module Failed!')


# Generated at 2022-06-13 01:52:14.275273
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    # mock module parameters, file contents and results of calls to 'run_command'.
    # TODO: mock 'run_command' or use unittest.mock to simulate module execution in a test
    test_ifconfig_path = "ifconfig"

# Generated at 2022-06-13 01:52:22.885409
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    """
    This is the unittest for class SunOSNetwork get_interfaces_info method.
    """
    test_module = type('module', (object, ), {'run_command': run_command_mock})()

    ifc = SunOSNetwork(module=test_module)
    # run_command should be called only once
    test_module.run_command.assert_called_once_with([ifc.ifconfig_path, '-a'])
    interfaces, ips = ifc.get_interfaces_info(ifc.ifconfig_path)

    assert len(interfaces) == 1
    assert len(interfaces['lo0']) == 3
    assert len(interfaces['lo0']['ipv4']) == 1

# Generated at 2022-06-13 01:52:34.432913
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    module = AnsibleModule(argument_spec=dict())
    test_object = SunOSNetwork()
    test_object.module = module
    test_object.module.params = dict()


# Generated at 2022-06-13 01:52:44.079828
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    module = FakeAnsibleModule({'gather_subset': 'all'})
    result = SunOSNetwork().get_interfaces_info(ifconfig_path='./unittests/facts/network/sunos_ifconfig_output')

# Generated at 2022-06-13 01:52:44.729155
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    pass

# Generated at 2022-06-13 01:52:53.611023
# Unit test for method parse_interface_line of class SunOSNetwork
def test_SunOSNetwork_parse_interface_line():
    c = SunOSNetwork({})
    current_if = {}
    interfaces = {}

    # Testing IPv4 interface
    words = ['lo0:', 'flags=2001000849<UP,LOOPBACK,'
             'RUNNING,MULTICAST,IPv4,VIRTUAL>', 'mtu', '8232',
             'index', '2']
    current_if = c.parse_interface_line(words, current_if, interfaces)
    assert current_if['device'] == 'lo0'
    assert current_if['type'] == 'loopback'
    assert current_if['ipv4'][0] == {'flags': ['UP', 'LOOPBACK', 'RUNNING', 'MULTICAST', 'IPv4', 'VIRTUAL'], 'mtu': '8232'}

    # Testing

# Generated at 2022-06-13 01:53:03.780840
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    assert issubclass(SunOSNetworkCollector, NetworkCollector)


# Generated at 2022-06-13 01:53:06.310160
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    """Test case to validate that the constructor will call the parent class
    constructor and return an object."""
    SunOSNetworkCollector()

# Generated at 2022-06-13 01:53:17.912832
# Unit test for method get_interfaces_info of class SunOSNetwork

# Generated at 2022-06-13 01:53:24.901690
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork
    network = GenericBsdIfconfigNetwork()
    result = network.get_interfaces_info("/sbin/ifconfig")
    assert result[0]['lo0']['device'] == 'lo0'
    assert result[0]['lo0']['type'] == 'loopback'
    assert result[0]['lo0']['macaddress'] == 'unknown'
    assert result[0]['lo0']['ipv4'][0]['mtu'] == 8232
    assert result[0]['lo0']['ipv4'][0]['flags'] == ['UP', 'RUNNING', 'MULTICAST', 'IPv4']

# Generated at 2022-06-13 01:53:29.366919
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    network_collector = SunOSNetworkCollector()
    assert network_collector.__class__.__name__ == 'SunOSNetworkCollector'
    assert network_collector.platform == 'SunOS'
    assert network_collector._fact_class == SunOSNetwork

# Generated at 2022-06-13 01:53:36.728644
# Unit test for method get_interfaces_info of class SunOSNetwork

# Generated at 2022-06-13 01:53:47.909395
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    # Create a Mock object of class module
    mockmodule = type('module', (), dict(run_command=run_command_mock))()
    # Create a Mock object of class SunOSNetwork
    mockclass = type('SunOSNetwork', (SunOSNetwork, ), dict(module=mockmodule))
    # Create an instance of the Mock class
    facts = mockclass()

    # Get the result of method get_interfaces_info
    interfaces = facts.get_interfaces_info('/usr/sbin/ifconfig')

    # Test the result
    assert interfaces[0]['lo0']['type'] == 'loopback'

# Generated at 2022-06-13 01:53:49.471376
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    """ Test the constructor of the class SunOSNetworkCollector
    """
    try:
        SunOSNetworkCollector()
    except NameError:
        assert False

# Generated at 2022-06-13 01:53:58.534291
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    '''
    Unit test for method get_interfaces_info of class SunOSNetwork

    Function input:
    Content of /sbin/ifconfig -a output

    Test case #1:
    Function output must be equal to dictionary interfaces and ips as defined below.
    '''

# Generated at 2022-06-13 01:54:08.480541
# Unit test for method get_interfaces_info of class SunOSNetwork

# Generated at 2022-06-13 01:54:31.513320
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    """Constructor for SunOSNetworkCollector class"""
    SunOSNetworkCollector()

# Generated at 2022-06-13 01:54:37.193006
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    sunos_network_collector = SunOSNetworkCollector()
    assert sunos_network_collector.__class__.__name__ == 'SunOSNetworkCollector'
    assert sunos_network_collector._platform == 'SunOS'
    assert sunos_network_collector._fact_class.__name__ == 'SunOSNetwork'


# Generated at 2022-06-13 01:54:38.554251
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    network = SunOSNetworkCollector()
    assert network.platform == 'SunOS'

# Generated at 2022-06-13 01:54:49.482103
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    """
    Test get_interfaces_info method of SunOSNetwork class
    """

    class _module():
        def __init__(self):
            self.params = {}
        def run_command(self, cmd):
            return 0, '', ''

    class _NetworkCollector():
        def __init__(self, module):
            self.module = module


# Generated at 2022-06-13 01:54:51.823791
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    # Test instance creation with SunOS network class
    collector = SunOSNetworkCollector()
    assert collector.get_facts() is not None



# Generated at 2022-06-13 01:55:03.268718
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    """ Test get_interfaces_info() of SunOSNetwork class """
    from io import BytesIO
    from ansible.module_utils.facts.network.sunos import SunOSNetwork


# Generated at 2022-06-13 01:55:05.436870
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    c = SunOSNetworkCollector()
    assert c._platform == 'SunOS'
    assert c._fact_class.platform == 'SunOS'

# Generated at 2022-06-13 01:55:07.614271
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    network_collector = SunOSNetworkCollector()
    assert network_collector.platform == 'SunOS'
    assert network_collector.fact_class == SunOSNetwork

# Generated at 2022-06-13 01:55:08.748305
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    assert SunOSNetworkCollector._platform == 'SunOS'


# Generated at 2022-06-13 01:55:19.535566
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    module = type('', (), dict(run_command=lambda *args, **kwargs: (0, '', '')))()
    network = SunOSNetwork(module)
    interfaces, ips = network.get_interfaces_info("/bin/ifconfig")

    assert len(interfaces["qfe0"]["ipv4"]) == 1
    assert interfaces["qfe0"]["ipv4"][0] == {"mtu": "1500", "flags": "BROADCAST,MULTICAST,UP"}
    assert len(interfaces["qfe0"]["ipv6"]) == 1
    assert interfaces["qfe0"]["ipv6"][0] == {"mtu": "1500", "flags": "BROADCAST,MULTICAST,IPv6,UP"}

# Generated at 2022-06-13 01:55:51.234286
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    SunOSNetworkCollector()

# Generated at 2022-06-13 01:55:59.865139
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    sunos_ifconfig_path = "/usr/sbin/ifconfig"

# Generated at 2022-06-13 01:56:01.816721
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    module = AnsibleModule(argument_spec={})
    network_collector = SunOSNetworkCollector(module)
    assert network_collector.fact_class == SunOSNetwork
    assert network_collector.platform == 'SunOS'



# Generated at 2022-06-13 01:56:03.464712
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    assert SunOSNetworkCollector.platform == 'SunOS'
    assert SunOSNetworkCollector._fact_class == SunOSNetwork


# Generated at 2022-06-13 01:56:09.271917
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():

    # Create class instance for testing
    network = SunOSNetwork()

    # Read test data
    with open('./test/unit/module_utils/facts/network/test_SunOSNetwork_get_interfaces_info.txt', 'r') as test_data:
        test_data = test_data.read()

    # Create mock objets for module.run_command()
    class Mock_module:
        def __init__(self):
            self.run_command = Mock_run_command
    class Mock_run_command:
        def __call__(self, command, *args, **kwargs):
            stdout = test_data
            return 0, stdout, ''

    # Call method
    network.module = Mock_module()

# Generated at 2022-06-13 01:56:20.007547
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    net = SunOSNetwork(dict(module=dict()))
    net.get_interfaces_info = net.get_interfaces_info.im_func

    fake_output = '''
lo0: flags=2001000849 mtu 8232 index 1
        inet 127.0.0.1 netmask ff000000
en3: flags=1000843 mtu 1500 index 2
        inet 10.0.0.1 netmask ffffff00 broadcast 10.0.0.255
        inet6 fe80::223:6cff:fe8d:e235%en3 prefixlen 64 scopeid 0x4
        ether 00:23:6c:8d:e2:35
        media: autoselect
        status: active
'''


# Generated at 2022-06-13 01:56:29.259493
# Unit test for method get_interfaces_info of class SunOSNetwork

# Generated at 2022-06-13 01:56:31.567193
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    collector = SunOSNetworkCollector()
    assert collector.platform == "SunOS"
    assert collector.fact_class == SunOSNetwork


# Generated at 2022-06-13 01:56:40.141137
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    my_obj = SunOSNetwork({})

# Generated at 2022-06-13 01:56:42.703236
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    sunos_network_fact = SunOSNetworkCollector()
    assert sunos_network_fact._platform == 'SunOS'
    assert sunos_network_fact._fact_class.platform == 'SunOS'

# Generated at 2022-06-13 01:58:03.652688
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    """Unit test for method get_interfaces_info of class SunOSNetwork """

    module = AnsibleModule(argument_spec={'gather_subset': dict(default=[], type='list')})

    ifconfig_path = '/sbin/ifconfig'
    ifc = SunOSNetwork(module)


# Generated at 2022-06-13 01:58:07.167968
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    """
    Unit test for constructor of class SunOSNetworkCollector
    """

    sunos_collector_obj = SunOSNetworkCollector(None, None, None, None)
    assert sunos_collector_obj._fact_class == SunOSNetwork
    assert sunos_collector_obj._platform == 'SunOS'

# Generated at 2022-06-13 01:58:08.267893
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    collector = SunOSNetworkCollector(None, None, None)
    assert collector