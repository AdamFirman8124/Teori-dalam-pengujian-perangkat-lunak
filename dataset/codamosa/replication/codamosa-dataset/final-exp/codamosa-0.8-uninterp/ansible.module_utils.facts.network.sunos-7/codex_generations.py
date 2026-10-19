

# Generated at 2022-06-13 01:48:22.933336
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    """Test SunOSNetworkCollector class."""
    net_collector = SunOSNetworkCollector()
    assert net_collector.__class__.__name__ == 'SunOSNetworkCollector'


# Generated at 2022-06-13 01:48:28.803924
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    """
    Test the method get_interfaces_info on class SunOSNetwork.

    The method get_interfaces_info returns a dictionary of dictionaries.
    The keys are the interface names and the values are dictionaries with
    the keys 'device', 'type', 'ipv4', 'ipv6'.
    The ipv4 and ipv6 values are lists of dictionaries with the keys 'address',
    'netmask', 'broadcast' and 'scope'.
    """
    module = AnsibleModuleMock()
    network = SunOSNetwork(module)
    ifconfig_path = '/sbin/ifconfig'

# Generated at 2022-06-13 01:48:33.890345
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():

    # test with different input values
    from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork
    test_obj = SunOSNetworkCollector()

    # check object type
    assert type(test_obj) == SunOSNetworkCollector

    # check if the fact class is SunOSNetwork
    assert test_obj._fact_class == SunOSNetwork

    # check if the platform is SunOS
    assert test_obj._platform == 'SunOS'

# Generated at 2022-06-13 01:48:44.585844
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    """
    Test the SunOSNetwork.get_interfaces_info() method.

    :return:
    """
    module = FakeModule()
    # Expected output

# Generated at 2022-06-13 01:48:55.020651
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    module = DummyModule()

    net_cli = SunOSNetwork(module)

    path_func = lambda x: 'dummy_path'
    get_bin_path_mocker = mock.patch.object(Network, 'get_bin_path', path_func)

    with get_bin_path_mocker as get_bin_path_func:
        interfaces, ips = net_cli.get_interfaces_info('ifconfig')

    assert isinstance(interfaces, dict)

    assert 'lo0' in interfaces
    lo0_dict = interfaces['lo0']
    assert lo0_dict['device'] == 'lo0'
    assert lo0_dict['type'] == 'loopback'
    assert lo0_dict['smask'] == '0x000080'

# Generated at 2022-06-13 01:49:02.205815
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():

    module = mock.MagicMock()
    module.run_command = MagicMock(return_value=(0, "", ""))


# Generated at 2022-06-13 01:49:11.236057
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork

    # Mock module
    module = Mock()
    module.run_command.return_value = (0, IFCONFIG_ALL, '')

    # Mock object
    ifconfig_module = SunOSNetwork()
    ifconfig_module.module = module

    interfaces, ips = ifconfig_module.get_interfaces_info('/bin/ifconfig')
    assert interfaces['lo0']['ipv4'][0]['address'] == '127.0.0.1'
    assert interfaces['lo0']['ipv6'][0]['address'] == '::1'
    assert interfaces['lo0']['ipv6'][0]['scope'] == 'Host'

# Generated at 2022-06-13 01:49:21.138928
# Unit test for method get_interfaces_info of class SunOSNetwork

# Generated at 2022-06-13 01:49:22.669873
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    obj = SunOSNetworkCollector()
    assert obj._fact_class is SunOSNetwork
    assert obj._platform is 'SunOS'

# Generated at 2022-06-13 01:49:29.621095
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    from ansible_collections.notstdlib.moveitallout.tests.unit.compat import unittest
    from ansible_collections.notstdlib.moveitallout.tests.unit.compat.mock import Mock

    class ModuleMock(object):
        pass

    module = ModuleMock()
    fact_class = SunOSNetworkCollector(module=module)
    assert fact_class._fact_class == SunOSNetwork
    assert fact_class._platform == 'SunOS'


# Generated at 2022-06-13 01:49:41.635953
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    print('Testing SunOSNetworkCollector')
    assert SunOSNetworkCollector.platform == 'SunOS'
    assert SunOSNetworkCollector.fact_class == SunOSNetwork
    # SunOSNetworkCollector is a subclass of NetworkCollector, which is a subclass of BaseNetworkCollector.
    assert issubclass(SunOSNetworkCollector, NetworkCollector)
    assert issubclass(SunOSNetworkCollector, NetworkCollector)
    assert issubclass(SunOSNetworkCollector, NetworkCollector)

# Generated at 2022-06-13 01:49:44.500509
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    instance = SunOSNetworkCollector()
    assert isinstance(instance, SunOSNetworkCollector)
    assert instance.platform == 'SunOS'


# Generated at 2022-06-13 01:49:45.871828
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    assert SunOSNetworkCollector.platform == "SunOS"


# Generated at 2022-06-13 01:49:51.758534
# Unit test for method parse_interface_line of class SunOSNetwork
def test_SunOSNetwork_parse_interface_line():
    from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork

    test1 = ['lo1:', 'flags=2001000849<UP,LOOPBACK,RUNNING,MULTICAST,IPv4,VIRTUAL>', 'mtu', '8232', 'index', '2', 'inet', '127.0.0.1', 'netmask', 'ffffff00', 'groupname', 'lo%d']
    answer1 = {'device': 'lo1', 'ipv4': [{'flags': '2001000849<UP,LOOPBACK,RUNNING,MULTICAST,IPv4,VIRTUAL>', 'mtu': '8232'}], 'ipv6': [], 'type': 'loopback'}

# Generated at 2022-06-13 01:49:54.195404
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    unittest.TestLoader().loadTestsFromTestCase(SunOSNetworkCollector)

if __name__ == '__main__':
    unittest.main()

# Generated at 2022-06-13 01:49:57.940901
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    l = SunOSNetworkCollector()
    assert l
    assert 'SunOSNetwork' == l._fact_class
    assert 'SunOS' == l._platform

# Generated at 2022-06-13 01:50:08.118714
# Unit test for method get_interfaces_info of class SunOSNetwork

# Generated at 2022-06-13 01:50:19.119854
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():

    class ModuleMock():
        def __init__(self):
            self.params = {}
            self.run_command = run_command
            self.get_bin_path = get_bin_path

        # Mocking of module.run_command()
        def run_command(self, cmd, check_rc=True):
            rc = 0
            out = ""
            err = ""
            for line in ifconfig_out.splitlines():
                if re.match(r'^\S', line.decode()):
                    # Split the stated line of the output into words
                    words = line.split()
                    if words[0] == b'lo0' or words[0] == b'igb1':
                        out += line.decode()
                    else:
                        continue

# Generated at 2022-06-13 01:50:28.970766
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    module = type('module', (), dict(run_command=lambda x, **kwargs: (0, '', ''), params=dict()))()
    p = SunOSNetwork(module)
    ifconfig_path = '/sbin/ifconfig'
    interfaces, ips = p.get_interfaces_info(ifconfig_path)
    assert len(interfaces) == 3

    assert interfaces['lo0']['active'] is True
    assert len(interfaces['lo0']['ipv4']) == 1
    assert interfaces['lo0']['ipv4'][0]['address'] == '127.0.0.1'
    assert interfaces['lo0']['ipv4'][0]['netmask'] == '255.0.0.0'

# Generated at 2022-06-13 01:50:40.968676
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    from ansible_collections.notstdlib.moveitallout.tests.unit.compat.mock import patch
    from ansible_collections.notstdlib.moveitallout.plugins.module_utils.facts.network.sunos.sunos import SunOSNetwork

    mock_module = patch.multiple(SunOSNetwork, run_command=lambda self, args, check_rc=None: (0, '', ''))

# Generated at 2022-06-13 01:50:57.221297
# Unit test for method parse_interface_line of class SunOSNetwork

# Generated at 2022-06-13 01:50:58.760381
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    assert SunOSNetworkCollector._platform == 'SunOS'
    assert SunOSNetworkCollector._fact_class == SunOSNetwork

# Generated at 2022-06-13 01:51:01.148629
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    assert issubclass(SunOSNetworkCollector, NetworkCollector)

# Generated at 2022-06-13 01:51:13.244125
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():

    from ansible.module_utils.facts.network.sunos import SunOSNetwork
    sunos = SunOSNetwork(None)

    # Mock the SunOS implementation of the ifconfig command
    interfaces = {'lo0': {},
                  'igb0': {},
                  'igb1': {},
                  'igb2': {},
                  'aggr0': {},
                  'bge0': {},
                  'external0': {},
                  'bge1': {},
                  'external1': {},
                  'nge0': {},
                  'nge1': {}}

# Generated at 2022-06-13 01:51:25.006024
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    module = MockModule()
    spec = {'run_command.return_value': (0, open(os.path.join(os.path.dirname(__file__), 'ifconfig_solaris10')).read(), '')}
    module.params = {}
    module.config.params = {}
    with mock.patch.multiple(module, **spec):
        obj = SunOSNetwork(module)
        interfaces, ips = obj.get_interfaces_info('/sbin/ifconfig')
        assert interfaces['lo0']['type'] == 'loopback'
        assert interfaces['lo0']['ipv4'][0]['address'] == '127.0.0.1'
        # Solaris reports 'mtu 65535'
        assert interfaces['lo0']['ipv4'][0]['mtu']

# Generated at 2022-06-13 01:51:26.538689
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    '''
    Constructor for class SunOSNetworkCollector
    '''
    collector = SunOSNetworkCollector()
    assert collector.platform == 'SunOS'

# Generated at 2022-06-13 01:51:27.310154
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    SunOSNetworkCollector()

# Generated at 2022-06-13 01:51:28.194709
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    SunOSNetworkCollector()

# Generated at 2022-06-13 01:51:40.380861
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    """
    This will test get_interfaces_info method of the SunOSNetwork class.
    """
    module = NetworkCollector._create_ansible_module_mock()


# Generated at 2022-06-13 01:51:49.354624
# Unit test for method parse_interface_line of class SunOSNetwork
def test_SunOSNetwork_parse_interface_line():
    # Create a new instance of the SunOSNetwork class. This is required
    # to load the correct platform.
    sunos_network = SunOSNetwork()
    # The test platform for this method is the SunOSNetwork class.
    # Since the SunOSNetwork class extends the GenericBsdIfconfigNetwork class
    # it is possible to use both instances for testing.
    sunos_network.set_module(None)
    # Set the lines required to test this method.

# Generated at 2022-06-13 01:52:00.560994
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    test_class = SunOSNetworkCollector()
    assert test_class.platform == 'SunOS'
    assert test_class._fact_class == SunOSNetwork


# Generated at 2022-06-13 01:52:09.593395
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    from ansible.module_utils import basic
    from ansible.module_utils.facts import collector


# Generated at 2022-06-13 01:52:19.143743
# Unit test for method get_interfaces_info of class SunOSNetwork

# Generated at 2022-06-13 01:52:20.802504
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    sun = SunOSNetworkCollector()
    assert sun.platform == 'SunOS'


# Generated at 2022-06-13 01:52:22.111276
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    facts_module = NetworkCollector()
    assert facts_module.get_all_facts() is not None

# Generated at 2022-06-13 01:52:25.282420
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    obj = SunOSNetworkCollector()
    assert obj.get_fact_class() == SunOSNetwork
    assert obj.get_platform() == 'SunOS'


# Generated at 2022-06-13 01:52:35.876573
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    """Unit test for method get_interfaces_info of class SunOSNetwork"""


# Generated at 2022-06-13 01:52:46.170291
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    """Test parsing of output of:
    ifconfig -a
    """

    # SunOS

# Generated at 2022-06-13 01:52:52.384131
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    from ansible.module_utils.facts.network import NetworkCollector
    from ansible.module_utils.facts.network.sunos.sunos import SunOSNetwork

    network = SunOSNetwork()
    network.get_interfaces_info('/sbin/ifconfig')
    facts = NetworkCollector.gather(network)
    assert facts['ansible_' + network.platform].get('interfaces') is not None
    assert facts['ansible_' + network.platform].get('default_ipv4') is not None


# Generated at 2022-06-13 01:52:53.511768
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    obj = SunOSNetworkCollector()
    assert obj.platform == 'SunOS'


# Generated at 2022-06-13 01:53:20.641561
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    interfaces = {'lo0': {'device': 'lo0', 'type': 'loopback', 'ipv4': [{'flags': ['UP', 'LOOPBACK', 'RUNNING'], 'mtu': 8232}],
                          'ipv6': [{'flags': ['UP', 'LOOPBACK', 'RUNNING'], 'mtu': 8232}],
                          'macaddress': '00:00:00:00:00:00'},
                  'igb0': {'device': 'igb0', 'type': 'unknown', 'ipv4': [], 'ipv6': [], 'macaddress': '00:00:00:00:00:00'}}
    ips = {'all_ipv4_addresses': [], 'all_ipv6_addresses': []}

    test_

# Generated at 2022-06-13 01:53:22.882453
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    obj = SunOSNetworkCollector()
    assert obj.platform == 'SunOS'

# Generated at 2022-06-13 01:53:26.529210
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    """
    Unit test for constructor of class SunOSNetworkCollector
    """
    sunos_network_collector = SunOSNetworkCollector()
    assert sunos_network_collector._platform == 'SunOS'
    assert sunos_network_collector._fact_class == SunOSNetwork

# Generated at 2022-06-13 01:53:29.554360
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    net_collector = SunOSNetworkCollector()
    assert net_collector.platform == 'SunOS'
    assert net_collector.fact_class == SunOSNetwork


# Generated at 2022-06-13 01:53:31.001530
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    obj = SunOSNetworkCollector()
    assert obj._fact_class is SunOSNetwo

# Generated at 2022-06-13 01:53:35.381102
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    """
    Test for method get_interfaces_info
    of class SunOSNetwork
    """

    # Bind network information to a variable
    sunos_interfaces = SunOSNetwork()
    interfaces_info = sunos_interfaces.get_interfaces_info('/sbin/ifconfig')

    # Verify that the dictionary of interfaces is not empty
    assert(len(interfaces_info) > 0)

# Generated at 2022-06-13 01:53:46.186256
# Unit test for method parse_interface_line of class SunOSNetwork
def test_SunOSNetwork_parse_interface_line():
    """
    Test if parse_interface_line returns the expected dictionary
    """
    # Declare dictionary to hold test arguments
    words = []
    current_if = {}
    interfaces = {}
    
    # Declare dictionary to hold expected output
    expected_out = {}
    expected_out['device'] = 'lo0'
    expected_out['ipv4'] = [{'flags': ['UP',
                                       'BROADCAST',
                                       'LOOPBACK',
                                       'RUNNING',
                                       'MULTICAST',
                                       'IPv4'],
                             'mtu': '8622'}]

# Generated at 2022-06-13 01:53:50.362950
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    """Unit test for constructor of class SunOSNetworkCollector"""
    assert SunOSNetworkCollector._platform == 'SunOS'
    assert SunOSNetworkCollector._fact_class == SunOSNetwork
    assert SunOSNetworkCollector.platform == 'SunOS'\
        and SunOSNetworkCollector.fact_class == SunOSNetwork

# Generated at 2022-06-13 01:53:53.301222
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    fact_class = SunOSNetworkCollector()

    assert fact_class._fact_class.__name__ == SunOSNetwork.__name__
    assert fact_class._platform == SunOSNetwork.platform


# Generated at 2022-06-13 01:54:01.542908
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    from ansible.module_utils.facts.network.sunos.facts import SunOSNetwork
    from ansible.module_utils.facts.network.sunos.legacy import SunOSNetwork as LegacySunOSNetwork
    from ansible.module_utils.facts.network.base import NetworkCollector

    # ---- test with legacy facts ----

    network = LegacySunOSNetwork()
    interfaces, ips = network.get_interfaces_info(network.module.get_bin_path('ifconfig'))

    assert interfaces
    assert ips

    # ---- test with new facts ----

    collector = SunOSNetworkCollector()
    interfaces, ips = collector.get_interfaces_info()

    assert interfaces
    assert ips

# Generated at 2022-06-13 01:54:44.893984
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    """Unit test for class 'SunOSNetworkCollector'
    """
    SunOSNetworkCollector()

# Generated at 2022-06-13 01:54:48.888546
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    import json

    testobj = SunOSNetwork({})
    interfaces, ips = testobj.get_interfaces_info('/sbin/ifconfig')

    if testobj.module.check_mode:
        print(json.dumps({'INTERFACES': interfaces, 'IPS': ips}, indent=4))

# Generated at 2022-06-13 01:54:51.935428
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    facts = SunOSNetworkCollector().collect()
    # Test whether the correct class is instantiated
    assert(facts['network'].__class__.__name__ == 'SunOSNetwork')

# Generated at 2022-06-13 01:54:53.058543
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    SunOSNetworkCollector()

# Generated at 2022-06-13 01:55:04.396760
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    module = AnsibleModule(argument_spec={'gather_subset': dict(default=['!all'], type='list')})

    # Create a SunOSNetwork object
    n = SunOSNetwork(module)

    # Get interfaces_info from SunOSNetwork
    interfaces, ips = n.get_interfaces_info(n.module.get_bin_path('ifconfig'))

    # Test loopback device
    assert 'lo0' in interfaces
    assert interfaces['lo0']['type'] == 'loopback'

    # Test MAC is present & valid
    assert 'macaddress' in interfaces['lo0']

# Generated at 2022-06-13 01:55:06.408799
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    """
    Unit test for constructor of class SunOSNetworkCollector
    """
    SunOSNetworkCollector()


# Generated at 2022-06-13 01:55:07.252135
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    SunOSNetworkCollector()

# Generated at 2022-06-13 01:55:08.479364
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    collector = SunOSNetworkCollector()
    assert collector is not None


# Generated at 2022-06-13 01:55:19.358641
# Unit test for method get_interfaces_info of class SunOSNetwork

# Generated at 2022-06-13 01:55:23.071457
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    net = SunOSNetworkCollector()
    assert net.__class__.__name__ == 'SunOSNetworkCollector'


# Generated at 2022-06-13 01:56:40.830256
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():

    from ansible.module_utils.facts.network.sunos import SunOSNetwork


# Generated at 2022-06-13 01:56:43.394528
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    sunos_network_collector = SunOSNetworkCollector()
    assert sunos_network_collector._platform == 'SunOS'
    assert sunos_network_collector._fact_class == SunOSNetwork

# Generated at 2022-06-13 01:56:44.279434
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    SunOSNetworkCollector()

# Generated at 2022-06-13 01:56:52.154669
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    """ Return a list of interfaces with facts and IP addresses """
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True,
    )
    ifconfig_path = module.get_bin_path('ifconfig', True)

    network_collector = SunOSNetwork(module=module)
    interfaces, ips = network_collector.get_interfaces_info(ifconfig_path)

    assert interfaces is not None
    assert ips is not None



# Generated at 2022-06-13 01:57:00.344107
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    """
    unit test for method get_interfaces_info of class SunOSNetwork
    """
    ifconfig_path = '/sbin/ifconfig'
    mock_module = MagicMock()


# Generated at 2022-06-13 01:57:04.073486
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    """Unit test for constructor of class SunOSNetworkCollector"""
    _fact_class = SunOSNetwork
    _platform = 'SunOS'
    result = SunOSNetworkCollector(_fact_class, _platform)
    assert result.fact_class == _fact_class
    assert result.platform == _platform


# Generated at 2022-06-13 01:57:13.893710
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    module = AnsibleModuleMock()
    module.run_command.return_value = (0, test_facts_SunOS, '')
    fact_class = SunOSNetwork(module=module)
    interfaces, ips = fact_class.get_interfaces_info('/sbin/ifconfig')

# Generated at 2022-06-13 01:57:24.675452
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    # TODO: how do we get ifconfig_path?
    # ifconfig_path = module.get_bin_path('ifconfig')
    ifconfig_path = '/sbin/ifconfig'

    test_0 = {'device': 'e1000g0',
              'ipv4': [{'flags': ['UP', 'BROADCAST', 'RUNNING', 'IPv4'], 'mtu': '1500'}],
              'ipv6': [{'flags': ['UP', 'BROADCAST', 'RUNNING', 'IPv6', 'AUTOCONF', 'MULTICAST'], 'mtu': '1500'}],
              'macaddress': 'c0:ff:ee:c0:ff:ee',
              'type': 'unknown'}

# Generated at 2022-06-13 01:57:25.792776
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    # test instantiation of SunOSNetworkCollector
    SunOSNetworkCollector()

# Generated at 2022-06-13 01:57:26.768677
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    netcollector = SunOSNetworkCollector()
    assert netcollector.platform == 'SunOS'
