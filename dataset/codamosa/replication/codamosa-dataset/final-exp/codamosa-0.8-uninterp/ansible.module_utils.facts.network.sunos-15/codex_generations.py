

# Generated at 2022-06-13 01:48:23.774667
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    """
    This is a test method for the method get_interfaces_info() of class SunOSNetwork
    """
    # I can't think of a way to unit test this method without
    # mocking out the entire module.run_command() call.
    # If you figure out how it should be done, please let me know.
    pass

# Generated at 2022-06-13 01:48:31.489154
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    # mock module
    module = type('', (), {
        'run_command': run_command_mock,
    })()


# Generated at 2022-06-13 01:48:42.120560
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():

    from ansible.module_utils.facts.network.sunos import SunOSNetwork
    from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork


# Generated at 2022-06-13 01:48:45.470823
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    obj = SunOSNetworkCollector()
    assert obj._fact_class is not None
    assert obj._platform == 'SunOS'

# Generated at 2022-06-13 01:48:48.615563
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    instance = SunOSNetworkCollector()
    assert isinstance(instance._fact_class, SunOSNetwork)
    assert isinstance(instance._platform, str)
    assert isinstance(instance._fact_class.platform, str)
    assert instance._platform == 'SunOS'
    assert instance._fact_class.platform == 'SunOS'


# Generated at 2022-06-13 01:48:51.094274
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    module = AnsibleModule(argument_spec={})
    collector = SunOSNetworkCollector(module=module)
    assert fact_class == SunOSNetwork
    assert platform == 'SunOS'

# Generated at 2022-06-13 01:48:54.434597
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    assert SunOSNetworkCollector.__name__ == 'SunOSNetworkCollector'
    assert SunOSNetworkCollector._platform == 'SunOS'
    assert SunOSNetworkCollector._fact_class.__name__ == 'SunOSNetwork'


# Generated at 2022-06-13 01:49:05.265777
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    module = AnsibleModule(
        argument_spec = dict(),
        supports_check_mode = True
    )

    instance = SunOSNetwork(module=module)

    # Example of output of 'ifconfig -a' on SunOS

# Generated at 2022-06-13 01:49:16.018522
# Unit test for method parse_interface_line of class SunOSNetwork
def test_SunOSNetwork_parse_interface_line():
    # Initialization
    current_if = {}
    interfaces = {}
    words = ['net0:', 'flags=1004843<UP,LOOPBACK,RUNNING,MULTICAST,IPv4>', 'mtu', '8232']

    # create a SunOSNetwork object
    sunos_network = SunOSNetwork()

    # call method parse_interface_line
    current_if = sunos_network.parse_interface_line(words, current_if, interfaces)

    # asserts
    assert 'mtu' in current_if['ipv4'][0]
    assert 'flags' in current_if['ipv4'][0]
    assert 'device' in current_if
    assert 'ipv4' in current_if
    assert 'type' in current_if
    assert 'ipv4' in current_

# Generated at 2022-06-13 01:49:17.329701
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    '''Unit test for SunOSNetworkCollector'''
    SunOSNetworkCollector()

# Generated at 2022-06-13 01:49:33.014045
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    fake_module = type('FakeModule', (object,), {'run_command': lambda x: ('', FAKE_IFCONFIG_DATA, '')})
    fake_collector = SunOSNetwork(fake_module)
    interfaces, ips = fake_collector.get_interfaces_info('/sbin/ifconfig')

    assert interfaces['e1000g0']['active'] is True
    assert interfaces['e1000g0']['device'] == 'e1000g0'
    assert interfaces['e1000g0']['ipv4'][0]['address'] == '10.0.0.123'
    assert interfaces['e1000g0']['ipv4'][0]['broadcast'] == '10.0.0.255'

# Generated at 2022-06-13 01:49:45.368958
# Unit test for method parse_interface_line of class SunOSNetwork
def test_SunOSNetwork_parse_interface_line():

    module = FakeModule()
    network = SunOSNetwork(module)

    facts = {'enp0s3': {'ipv4': [{'flags': ['UP', 'BROADCAST', 'RUNNING',
                                            'SIMPLEX', 'MULTICAST'],
                                  'mtu': '1500'}],
                        'ipv6': [{'flags': ['UP', 'BROADCAST', 'RUNNING', 'MULTICAST'],
                                  'mtu': '1500'}],
                        'macaddress': 'unknown',
                        'type': 'loopback'}}

    # Test with IPv4

# Generated at 2022-06-13 01:49:55.893760
# Unit test for method parse_interface_line of class SunOSNetwork
def test_SunOSNetwork_parse_interface_line():
    module = type('AnsModule', (object,), {'run_command': None})()
    facts = SunOSNetwork(module)
    iface = {}
    ifaces = {}
    words = ['hme0:', 'flags=1000843<UP,BROADCAST,RUNNING,MULTICAST,IPv4>', 'mtu=1500']
    iface = facts.parse_interface_line(words, iface, ifaces)
    assert iface['device'] == 'hme0'
    assert iface['ipv4'][0]['flags'] == ['UP', 'BROADCAST', 'RUNNING', 'MULTICAST', 'IPv4']
    assert iface['ipv4'][0]['mtu'] == '1500'
    assert len(iface['ipv6']) == 0

# Generated at 2022-06-13 01:50:05.999527
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():

    # Unit test data
    test_data_filename = 'SunOS_ifconfig_output.txt'
    test_data_filedir = 'tests/unit/module_utils/facts/network/'
    test_data_filepath = test_data_filedir + test_data_filename

    # Open test data file
    test_data_filehandle = open(test_data_filepath, 'r')
    test_data = test_data_filehandle.read()
    test_data_filehandle.close()

    # Check get_interfaces_info of class SunOSNetwork
    # input data
    ifconfig_path = 'ifconfig'

    # instantiate class SunOSNetwork
    sunos = SunOSNetwork()

    # run method get_interfaces_info of class SunOSNetwork

# Generated at 2022-06-13 01:50:16.988132
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    """Unit test: SunOSNetwork.get_interfaces_info()."""

    from ansible.module_utils.facts.network.sunos import SunOSNetwork
    from ansible.module_utils.six import PY3

    net = SunOSNetwork()

    # SunOSNetwork.get_interfaces_info() returns a tuple
    # (interfaces, ips)
    interfaces, ips = net.get_interfaces_info(None)

    assert 'lo0' in interfaces
    assert 'net0' in interfaces

# Generated at 2022-06-13 01:50:27.012937
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():

    class FakeModule:
        def __init__(self):
            self.run_command_args = []
            self.run_command_rcs = dict()

        def run_command(self, args, check_rc=True):
            self.run_command_args.append(args)
            rc = self.run_command_rcs.get('rc')
            out = self.run_command_rcs.get('out')
            err = self.run_command_rcs.get('err')
            return rc, out, err

    fake_module = FakeModule()


# Generated at 2022-06-13 01:50:38.641081
# Unit test for method get_interfaces_info of class SunOSNetwork

# Generated at 2022-06-13 01:50:41.276219
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    assert SunOSNetworkCollector._platform == 'SunOS'
    assert SunOSNetworkCollector.platforms == ('SunOS',)

# Generated at 2022-06-13 01:50:52.860194
# Unit test for method parse_interface_line of class SunOSNetwork
def test_SunOSNetwork_parse_interface_line():
    test_SunOSNetwork = SunOSNetwork()
    test_interfaces = {}

    test_words = ['lo0:', 'flags=2001000849<UP,LOOPBACK,RUNNING,MULTICAST,IPv4,VIRTUAL>', 'mtu', '8232', 'index', '1']
    current_if = test_SunOSNetwork.parse_interface_line(test_words, {}, test_interfaces)
    assert current_if['device'] == 'lo0'
    assert current_if['type'] == 'loopback'
    assert current_if['ipv4'][0]['flags'] == ['UP', 'LOOPBACK', 'RUNNING', 'MULTICAST', 'IPv4', 'VIRTUAL']

# Generated at 2022-06-13 01:50:54.412663
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    assert SunOSNetworkCollector._platform == 'SunOS'


# Generated at 2022-06-13 01:51:15.142930
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    from ansible.module_utils.facts.network.sunos import SunOSNetwork
    module = type('', (), {})()
    module.run_command = lambda *args, **kwargs: (0, '', '')
    ifconfig_path = '/sbin/ifconfig'
    sunosnet = SunOSNetwork(module)
    interfaces, ips = sunosnet.get_interfaces_info(ifconfig_path)
    assert 'lo0' in interfaces
    assert 'igb0' in interfaces
    assert 'igb1' in interfaces
    assert len(interfaces['lo0']['ipv4']) == 1
    assert len(interfaces['lo0']['ipv6']) == 1
    assert len(interfaces['igb0']['ipv4']) == 1

# Generated at 2022-06-13 01:51:21.830002
# Unit test for method get_interfaces_info of class SunOSNetwork

# Generated at 2022-06-13 01:51:23.264164
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    assert SunOSNetworkCollector._fact_class == SunOSNetwork
    assert SunOSNetworkCollector._platform == 'SunOS'

# Generated at 2022-06-13 01:51:33.975893
# Unit test for method parse_interface_line of class SunOSNetwork
def test_SunOSNetwork_parse_interface_line():
    """
    Test the function SunOSNetwork.parse_interface_line()
    """
    t = SunOSNetwork()
    interfaces = {}
    # This line is for a virtual interface so it is an 'unknown' type
    current_if = t.parse_interface_line(['kstat0', 'UP', 'LOOPBACK', 'mtu', '8232'], interfaces['kstat0'], interfaces)
    assert current_if == {'device': 'kstat0', 'macaddress': 'unknown', 'type': 'unknown', 'ipv4': [{'flags': ['UP', 'LOOPBACK'], 'mtu': '8232'}], 'ipv6': []}
    # This line is for the physical interface (not virtual) so it's 'physical' type

# Generated at 2022-06-13 01:51:44.660460
# Unit test for method get_interfaces_info of class SunOSNetwork

# Generated at 2022-06-13 01:51:46.997589
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    obj = SunOSNetworkCollector()
    assert isinstance(obj, SunOSNetworkCollector)
    assert obj._platform == 'SunOS'
    assert obj._fact_class == SunOSNetwork

# Generated at 2022-06-13 01:51:56.981530
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    # Create a module for the unit test.
    # This module has a method named run_command
    class Module:
        def __init__(self):
            self.run_command_calls = 0

        # Create a mock ansible_facts
        def run_command(self, args):
            self.run_command_calls += 1
            self._run_command_args = args
            # Create a mock 'ifconfig -a' output
            if len(args) == 2 and args[0] == '/sbin/ifconfig' and args[1] == '-a':
                return 0, _ifconfig_a_output, None
            else:
                self.fail_json(msg="Unexpected call to run_command: %s" % args)


# Generated at 2022-06-13 01:52:05.747257
# Unit test for method get_interfaces_info of class SunOSNetwork

# Generated at 2022-06-13 01:52:11.500092
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    # create fake module and fact class instances
    fake_module = type('', (), {'run_command': lambda x: (0, '', '')})
    fake_facts = type('', (), {'module': fake_module})
    fake_network = SunOSNetwork(fake_facts)

    # set input for the method to test
    fake_ifconfig_path = '/fake/ifconfig/path'

# Generated at 2022-06-13 01:52:13.494045
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    obj = SunOSNetworkCollector()
    assert obj._fact_class is SunOSNetwork
    assert obj._platform is 'SunOS'

# Generated at 2022-06-13 01:52:33.923117
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    sunos = SunOSNetworkCollector()
    assert sunos.__dict__.get('_fact_class').__name__ == 'SunOSNetwork'

# Generated at 2022-06-13 01:52:41.654164
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    module = { 'run_command' : run_command_bsd }
    ifconfig_path = '/sbin/ifconfig'

# Generated at 2022-06-13 01:52:51.415733
# Unit test for method parse_interface_line of class SunOSNetwork
def test_SunOSNetwork_parse_interface_line():
    """Test the parse_interface_line() NetworkCollector method"""
    # first we define some test data
    # This is the output from 'ifconfig -a' on my Solaris 11.4 system

# Generated at 2022-06-13 01:52:58.012901
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts.network.sunos import SunOSNetwork
    from ansible.module_utils.facts.network.sunos import test_SunOSNetwork_data
    # Create a SunOSNetwork object
    network = SunOSNetwork()
    # Prepare a test
    test_SunOSNetwork_data.TEST_INTERFACES_INFO_OUTPUT = to_bytes(test_SunOSNetwork_data.TEST_INTERFACES_INFO_OUTPUT)
    # Run the test
    interfaces, ips = network.get_interfaces_info(test_SunOSNetwork_data.TEST_GET_INTERFACES_INFO_IFCONFIG_PATH)
    # test interfaces
    assert interfaces != None

# Generated at 2022-06-13 01:53:10.052577
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    '''Unit test for method get_interfaces_info of class SunOSNetwork'''
    # Create instance of class Network
    sunos_net = SunOSNetwork()

    # Get module params
    ifconfig_path = sunos_net.module.params['path_to_ifconfig']

    # Get interfaces info
    interfaces, ips = sunos_net.get_interfaces_info(ifconfig_path)

    # Check the facts returned
    if interfaces['solaris01']['ipv4'][0]['mtu'] == '1500':
        print("mtu 1500 was returned")
        print("The test passed")
    else:
        print("An unexpected value was returned for the 'mtu' fact")
        print("The test failed")

# Generated at 2022-06-13 01:53:20.406756
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    test = SunOSNetwork()

# Generated at 2022-06-13 01:53:24.337461
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    module = AnsibleModule(argument_spec={})
    collector1 = SunOSNetworkCollector(module=module)
    assert collector1.platform == 'SunOS'
    assert collector1.fact_class == SunOSNetwork


# Generated at 2022-06-13 01:53:34.792409
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    # Only run these test on SunOS/Solaris
    import sys
    if not sys.platform.startswith('sunos'):
        return

    module = AnsibleModule({})
    obj = SunOSNetwork(module=module)

    from ansible.module_utils.facts.network.sunos import SunOSNetwork


# Generated at 2022-06-13 01:53:38.944727
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    """
    This testcase checks if correct SunOSNetworkCollector object is initialized.
    """
    net_collector = SunOSNetworkCollector()
    assert net_collector.__class__.__name__ == 'SunOSNetworkCollector'



# Generated at 2022-06-13 01:53:49.561692
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    module = MockModule()
    obj = SunOSNetwork(None)
    obj.get_interfaces_info(module)

# Generated at 2022-06-13 01:54:37.792614
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    result = SunOSNetworkCollector()
    assert result.__class__.__name__ == 'SunOSNetworkCollector'
    assert result._fact_class == SunOSNetwork
    assert result._platform == 'SunOS'

# Generated at 2022-06-13 01:54:48.888376
# Unit test for method get_interfaces_info of class SunOSNetwork

# Generated at 2022-06-13 01:55:00.839407
# Unit test for method parse_interface_line of class SunOSNetwork
def test_SunOSNetwork_parse_interface_line():
    sunos = SunOSNetwork()
    words = 'lo0: flags=2001000849<UP,LOOPBACK,RUNNING,MULTICAST,IPv4,VIRTUAL> mtu 8232 index 1'.split()
    current_if = {}

    sunos.parse_interface_line(words, current_if)

    assert current_if['device'] == 'lo0'
    assert current_if['ipv4'][0]['flags'] == ['UP', 'LOOPBACK', 'RUNNING', 'MULTICAST', 'IPv4', 'VIRTUAL']
    assert current_if['ipv4'][0]['mtu'] == '8232'
    assert current_if['ipv6'] == []
    assert current_if['type'] == 'loopback'

# Generated at 2022-06-13 01:55:01.815245
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    SunOSNetwork.get_interfaces_info()

# Generated at 2022-06-13 01:55:03.612047
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    assert SunOSNetworkCollector._platform == 'SunOS'
    assert SunOSNetworkCollector._fact_class == SunOSNetwork

# Generated at 2022-06-13 01:55:05.652544
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    network_collector = SunOSNetworkCollector()
    assert network_collector._platform == 'SunOS'



# Generated at 2022-06-13 01:55:12.467401
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    mock_module = create_ansible_mock()

# Generated at 2022-06-13 01:55:22.552411
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    s = SunOSNetwork()
    path_to_mock = 'ansible.module_utils.facts.network.generic_bsd.GenericBsdIfconfigNetwork.get_interfaces_info'
    path_to_mock = path_to_mock.replace('generic_bsd.GenericBsdIfconfigNetwork', 'sunos.SunOSNetwork')
    s.module.run_command = MagicMock(return_value=(0, '', ''))
    s.module.get_bin_path = MagicMock(return_value='/sbin/ifconfig')
    with patch(path_to_mock, MagicMock(return_value=('', ''))):
        s.get_interfaces_info('/sbin/ifconfig')
    assert s.module.run_command.called
    assert s.module.get

# Generated at 2022-06-13 01:55:24.945802
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    result = SunOSNetworkCollector()
    assert result.platform == 'SunOS'
    assert result._fact_class.platform == 'SunOS'


# Generated at 2022-06-13 01:55:28.332035
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    SunosNetworkCollector = SunOSNetworkCollector()
    assert (SunosNetworkCollector._fact_class == SunOSNetwork)
    assert (SunosNetworkCollector._platform == 'SunOS')

# Generated at 2022-06-13 01:56:56.821401
# Unit test for method get_interfaces_info of class SunOSNetwork

# Generated at 2022-06-13 01:57:06.331149
# Unit test for method get_interfaces_info of class SunOSNetwork

# Generated at 2022-06-13 01:57:15.026368
# Unit test for method get_interfaces_info of class SunOSNetwork

# Generated at 2022-06-13 01:57:16.494572
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    obj = SunOSNetworkCollector()
    assert obj.platform == 'SunOS'
    assert obj.fact_class == SunOSNetwork

# Generated at 2022-06-13 01:57:18.439159
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    obj = SunOSNetworkCollector()
    assert obj._fact_class is SunOSNetwork
    assert obj._platform == 'SunOS'


# Generated at 2022-06-13 01:57:21.164288
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    facts = SunOSNetworkCollector()
    assert facts.get_network_gather_subset() is None
    assert facts.get_network_gather_network_resources() is None

# Generated at 2022-06-13 01:57:23.102699
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    o = SunOSNetworkCollector()
    assert o._fact_class == SunOSNetwork
    assert o._platform == 'SunOS'

# Generated at 2022-06-13 01:57:26.102292
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    obj = SunOSNetworkCollector()
    assert isinstance(obj, NetworkCollector)
    assert obj._fact_class == SunOSNetwork
    assert obj._platform == 'SunOS'
# END of unit test for SunOSNetworkCollector


# Generated at 2022-06-13 01:57:28.598025
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    assert SunOSNetworkCollector.__name__ == 'SunOSNetworkCollector'
    assert SunOSNetworkCollector._platform == 'SunOS'
    assert SunOSNetworkCollector._fact_class == SunOSNetwork

# Generated at 2022-06-13 01:57:30.502236
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    assert SunOSNetworkCollector._platform == 'SunOS'
    assert SunOSNetworkCollector._fact_class == SunOSNetwork
    assert SunOSNetworkCollector._sysfs_path == ''