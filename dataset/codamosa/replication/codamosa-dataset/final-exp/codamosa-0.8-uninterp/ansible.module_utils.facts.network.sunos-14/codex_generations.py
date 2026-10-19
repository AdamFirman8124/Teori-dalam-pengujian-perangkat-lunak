

# Generated at 2022-06-13 01:48:24.905488
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    module = FakeAnsibleModule()

    # If the Solaris 'ifconfig' command doesn't exist on this system,
    # 'SunOSNetwork.get_interfaces_info' will just return ({}, {}).
    # Unfortunately this is what happens if you run it on a non-Solaris OS.
    # The test cases below assume that the 'ifconfig' command does exist.
    ifconfig_path = module.get_bin_path('ifconfig')
    if ifconfig_path is None:
        module.warn("Skipping tests. ifconfig command not found.")
        return None

    sunOS_network = SunOSNetwork(module=module)
    interfaces, ips = sunOS_network.get_interfaces_info(ifconfig_path)

    # FIXME: this test covers only the first few lines of output of 'ifconfig -a'.

# Generated at 2022-06-13 01:48:33.104088
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    import os
    import tempfile

# Generated at 2022-06-13 01:48:43.762411
# Unit test for method parse_interface_line of class SunOSNetwork
def test_SunOSNetwork_parse_interface_line():
    from ansible.module_utils.facts.network import SunOSNetwork
    from collections import OrderedDict
    interface_line = "lo0: flags=2001000849<UP,LOOPBACK,RUNNING,MULTICAST,IPv4,VIRTUAL> mtu 8232 index 2"
    current_if = {'device': 'lo0', 'ipv4': [], 'ipv6': [], 'type': 'unknown'}
    interfaces = OrderedDict()
    current_if = SunOSNetwork.parse_interface_line(SunOSNetwork(), interface_line.split(), current_if, interfaces)
    assert 'lo0' in interfaces
    assert current_if['type'] == 'loopback'
    ipv4 = current_if['ipv4']
    assert len(ipv4) == 1

# Generated at 2022-06-13 01:48:45.226940
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    fc = SunOSNetworkCollector()
    assert fc._platform == 'SunOS'

# Generated at 2022-06-13 01:48:55.493741
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    module = AnsibleModule(argument_spec=dict())
    module.exit_json = lambda: None

# Generated at 2022-06-13 01:49:02.488483
# Unit test for method parse_interface_line of class SunOSNetwork
def test_SunOSNetwork_parse_interface_line():
    module = FakeAnsibleModule()
    gbn = SunOSNetwork(module)

    device = 'e1000g'
    words = ['e1000g0:', 'flags=2001000849', 'mtu', '1500', 'index', '10']

    current_if = {}
    interfaces = {}
    current_if = gbn.parse_interface_line(words, current_if, interfaces)

    assert current_if['type'] == 'unknown'
    assert 'LOOPBACK' not in current_if['ipv4'][0]['flags']
    assert current_if['ipv4'][0]['mtu'] == '1500'
    assert current_if['ipv4'] == current_if['ipv6']

# Generated at 2022-06-13 01:49:11.386850
# Unit test for method get_interfaces_info of class SunOSNetwork

# Generated at 2022-06-13 01:49:14.359427
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    collector = SunOSNetworkCollector
    assert collector._fact_class is SunOSNetwork
    assert collector._platform is 'SunOS'

# Generated at 2022-06-13 01:49:16.489267
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    assert SunOSNetworkCollector.platform == 'SunOS'
    assert SunOSNetworkCollector._fact_class == SunOSNetwork


# Generated at 2022-06-13 01:49:24.146884
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    import sys
    import os
    import unittest
    import tempfile
    import types
    # Create temporary file with the command's output
    test_file = tempfile.NamedTemporaryFile(prefix='ansible_test_SunOSNetwork_get_interfaces_info_',
                                            dir='/tmp', delete=False)

# Generated at 2022-06-13 01:49:38.954648
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    module = NetworkCollector()
    ifconfig_path = module.get_bin_path('ifconfig', required=True)
    test_SunOSNetwork = SunOSNetwork(module)
    interfaces, ips = test_SunOSNetwork.get_interfaces_info(ifconfig_path)
    assert interfaces['lo0']['ipv4'][0]['mtu'] == '8232'
    assert interfaces['lo0']['ipv4'][0]['flags'] == ['UP', 'LOOPBACK', 'RUNNING', 'MULTICAST']
    assert interfaces['lo0']['ipv4'][0]['inet'] == ['127.0.0.1/8']
    assert interfaces['lo0']['macaddress'] == '00:00:00:00:00:00'

# Generated at 2022-06-13 01:49:42.720090
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    print('In test_SunOSNetworkCollector()')

    obj = SunOSNetworkCollector(module=None, facts={}, conditionals={})
    assert obj._platform == 'SunOS'
    assert obj._fact_class == SunOSNetwork


# Generated at 2022-06-13 01:49:43.856137
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    assert SunOSNetworkCollector._platform == 'SunOS'
    assert SunOSNetworkCollector._fact_class == SunOSNetwork

# Generated at 2022-06-13 01:49:44.452271
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    assert SunOSNetworkCollector


# Generated at 2022-06-13 01:49:45.459743
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    SunOSNetworkCollector()


# Generated at 2022-06-13 01:49:56.233015
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    """This is a unit test for method get_interfaces_info of class SunOSNetwork."""


# Generated at 2022-06-13 01:49:57.539193
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    obj = SunOSNetworkCollector()
    assert obj._platform == 'SunOS'

# Generated at 2022-06-13 01:50:07.846357
# Unit test for method get_interfaces_info of class SunOSNetwork

# Generated at 2022-06-13 01:50:18.638566
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    import unittest

    from ansible_collections.community.general.tests.unit.compat import unittest
    from ansible_collections.community.general.tests.unit.compat.mock import patch

    from ansible_collections.community.general.plugins.modules.network.facts import sunos

    FactsBaseTestCaseSunOS = sunos.FactsBaseTestCaseSunOS

    class TestSunOSNetworkCollector(FactsBaseTestCaseSunOS):
        def setUp(self):
            super(TestSunOSNetworkCollector, self).setUp()

    network_collector = TestSunOSNetworkCollector()

# Generated at 2022-06-13 01:50:28.515246
# Unit test for method get_interfaces_info of class SunOSNetwork

# Generated at 2022-06-13 01:50:39.424319
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    collector = SunOSNetworkCollector()
    assert collector._fact_class == SunOSNetwork
    assert collector._platform == 'SunOS'

# Generated at 2022-06-13 01:50:40.719522
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    SunOSNetworkCollector()

# Generated at 2022-06-13 01:50:45.398489
# Unit test for method get_interfaces_info of class SunOSNetwork

# Generated at 2022-06-13 01:50:57.041594
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=False
    )

    # This is an example of the output of 'ifconfig -a' command on Solaris
    # Tried to cover all possible cases

# Generated at 2022-06-13 01:50:59.821238
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    obj  = SunOSNetworkCollector()
    assert obj._fact_class == SunOSNetwork
    assert obj._platform == 'SunOS'

# Generated at 2022-06-13 01:51:02.391283
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    facts = SunOSNetworkCollector()
    assert facts.facts['all_ipv4_addresses'] == ['127.0.0.1']



# Generated at 2022-06-13 01:51:14.433946
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    module = NetworkCollector()
    ifconfigPath = 'ansible/module_utils/facts/network/test_ifconfig_SunOS.txt'
    interfaces, ips = SunOSNetwork().get_interfaces_info(ifconfigPath)
    assert len(interfaces) == 2
    assert len(ips) == 2
    assert len(interfaces['bge0']['ipv4']) == 2
    assert len(interfaces['bge0']['ipv6']) == 2
    assert len(interfaces['lo0']['ipv4']) == 1
    assert len(interfaces['lo0']['ipv6']) == 1
    assert interfaces['bge0']['macaddress'] == '00:14:4f:64:a6:0c'

# Generated at 2022-06-13 01:51:25.963258
# Unit test for method parse_interface_line of class SunOSNetwork
def test_SunOSNetwork_parse_interface_line():
    m = SunOSNetwork({})
    current_if = {}
    interfaces = {}
    current_if = m.parse_interface_line(['lo0:', 'flags=2001000849<UP,LOOPBACK,RUNNING,MULTICAST,IPv4,VIRTUAL>', 'metric', '0', 'mtu', '8232', 'index', '2'], current_if, interfaces)
    assert current_if['device'] == 'lo0'
    assert current_if['ipv4'][0]['flags'] == 'flags=2001000849<UP,LOOPBACK,RUNNING,MULTICAST,IPv4,VIRTUAL>'
    assert current_if['ipv4'][0]['mtu'] == '8232'
    assert current_if['ipv6'] == []

# Generated at 2022-06-13 01:51:38.163925
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    from sys import version_info
    if version_info[:2] == (2, 6):
        return
    import io
    import pytest
    sut = SunOSNetwork()
    sut._ifconfig_path = '/usr/sbin/ifconfig'
    sut.module = pytest.Mock()
    sut.module.run_command = pytest.Mock()
    sut.module.run_command.return_value = [0, '', '']

    with io.open('/proc/net/if_inet6', encoding='utf-8') as m:
        sut._get_ipv6_addresses = pytest.Mock(return_value=m.read())
    with io.open('/proc/net/route', encoding='utf-8') as m:
        sut._get_

# Generated at 2022-06-13 01:51:47.686862
# Unit test for method parse_interface_line of class SunOSNetwork

# Generated at 2022-06-13 01:52:04.313525
# Unit test for method get_interfaces_info of class SunOSNetwork

# Generated at 2022-06-13 01:52:07.428878
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    collector = SunOSNetworkCollector()
    assert collector.platform == 'SunOS'
    assert collector.fact_class == SunOSNetwork
    assert collector._supported_facts == set()
    assert collector._fact_class == SunOSNetwork
    assert collector._platform == 'SunOS'

# Generated at 2022-06-13 01:52:10.760775
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    nc = SunOSNetworkCollector()
    if nc.platform != 'SunOS' or nc._fact_class != SunOSNetwork:
        raise Exception('SunOSNetworkCollector instantiation test failed')

# Generated at 2022-06-13 01:52:20.161852
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    # Create an instance of class SunOSNetwork
    network_info = SunOSNetwork()

    # Set facts
    network_info.all_ipv4_addresses = ['192.168.1.1', '192.168.1.2', '10.0.0.1']
    network_info.all_ipv6_addresses = ['::1', 'fe80::e3c4:f4ff:fe1b:cf33', 'fe80::e3c4:f4ff:fe1b:cf34']

    # Set test lines
    test_line = ["lo0:1:", "flags=2001000849<UP,LOOPBACK,RUNNING,MULTICAST,IPv4,VIRTUAL>", "mtu 8232 index 1"]

# Generated at 2022-06-13 01:52:21.544317
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    net = SunOSNetworkCollector()
    assert net.platform == 'SunOS'


# Generated at 2022-06-13 01:52:27.298022
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )
    if_path = module.get_bin_path('ifconfig', True)

    # Create instance of SunOSNetwork class.
    # When getting the interfaces info, it will execute the command:
    # ifconfig -a
    # Which will return the following output to simulate the actual output of
    # the command:
    #
    # lo0: flags=2001000849<UP,LOOPBACK,RUNNING,MULTICAST,IPv4,VIRTUAL> mtu 8232 index 1
    #         inet 127.0.0.1 netmask ff000000
    # e1000g0: flags=1004843<UP,BROADCAST,RUNNING,MULTICAST,DHCP,IPv4> m

# Generated at 2022-06-13 01:52:37.584316
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    from ansible.module_utils.facts.network import SunOSNetworkCollector


# Generated at 2022-06-13 01:52:38.893388
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    SunOSNetworkCollector({}, {}, {}, {}, {})

# Generated at 2022-06-13 01:52:42.794965
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    module = AnsibleModule(argument_spec={})
    module.exit_json(ansible_facts={'ansible_network_resources': SunOSNetwork(module).get_interfaces_info(ifconfig_path='/sbin/ifconfig')})



# Generated at 2022-06-13 01:52:43.825881
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    SunOSNetworkCollector()

# Generated at 2022-06-13 01:53:12.794851
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    my_SunOSNetwork = SunOSNetwork()
    ifconfig_path = '/sbin/ifconfig'
    interfaces, ips = my_SunOSNetwork.get_interfaces_info(ifconfig_path)
    #assert len(interfaces) == 2, "There should be 2 interfaces.  There are %d." % len(interfaces)
    #assert len(ips) == 2, "There should be 2 IP addresses.  There are %d." % len(ips)
    #assert interfaces['lo0']['macaddress'] == 'unknown'
    #assert interfaces['lo0']['type'] == 'loopback'
    #assert interfaces['lo0']['ipv4'][0]['flags'] == ['UP', 'LOOPBACK', 'RUNNING']
    #assert interfaces['lo0']['ipv4'][0

# Generated at 2022-06-13 01:53:15.233897
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    obj = SunOSNetworkCollector()
    assert obj.platform == 'SunOS'


# Generated at 2022-06-13 01:53:17.422671
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    net_collector = SunOSNetworkCollector()
    assert net_collector.platform == 'SunOS'
    assert net_collector.fact_class == SunOSNetwork


# Generated at 2022-06-13 01:53:18.523879
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    SunOSNetworkCollector()

# Generated at 2022-06-13 01:53:19.973693
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    assert SunOSNetworkCollector._platform == 'SunOS'
    assert SunOSNetworkCollector._fact_class == SunOSNetwork

# Generated at 2022-06-13 01:53:23.088635
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    module = FakeAnsibleModule()
    collector = SunOSNetworkCollector(module)
    assert collector._fact_class == SunOSNetwork


# Generated at 2022-06-13 01:53:24.977196
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    collector = SunOSNetworkCollector()
    assert collector.platform == 'SunOS'

# Unit tests for constructor of class SunOSNetwork

# Generated at 2022-06-13 01:53:28.686995
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    obj = SunOSNetworkCollector()
    assert obj.platform == 'SunOS'
    assert obj.fact_class == SunOSNetwork
    assert isinstance(obj.fact_class({}, {}), SunOSNetwork)

# Generated at 2022-06-13 01:53:32.527875
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )
    collector = SunOSNetworkCollector(module)
    assert collector._fact_class == SunOSNetwork
    assert collector._platform == 'SunOS'

# Generated at 2022-06-13 01:53:43.618617
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    module = None
    test_object = SunOSNetwork(module)
    ifconfig_path = '/usr/sbin/ifconfig'

# Generated at 2022-06-13 01:54:26.497386
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    this = SunOSNetwork(module=None)
    this.module = None

# Generated at 2022-06-13 01:54:28.958232
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    """Check if SunOSNetworkCollector can be initialized."""
    SunOSNetworkCollector()

# Generated at 2022-06-13 01:54:33.938524
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    module = AnsibleModuleMock({}, {}, {}, {})
    sunos_collector = SunOSNetworkCollector(module)
    assert sunos_collector._fact_class is SunOSNetwork
    assert sunos_collector._platform == 'SunOS'



# Generated at 2022-06-13 01:54:41.543470
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    facts = dict()
    SunOSNetworkCollector(facts, None)
    assert facts['ansible_facts'].get('ansible_interfaces')
    assert facts['ansible_facts'].get('ansible_all_ipv4_addresses')
    assert facts['ansible_facts'].get('ansible_all_ipv6_addresses')
    assert facts['ansible_facts'].get('ansible_default_ipv4')
    assert facts['ansible_facts'].get('ansible_default_ipv6')

# Generated at 2022-06-13 01:54:51.015784
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    module = FakeAnsibleModule()
    network = SunOSNetwork()
    interfaces, ips = network.get_interfaces_info(module.params['ifconfig_path'])

    # Solaris can have different MTU and FLAGS for IPv4 and IPv6 on the same interface.
    # check that IPv4 FLAGS and MTU are in the 'ipv4' list and not 'ipv6' list
    # and that IPv6 FLAGS and MTU are in the 'ipv6' list and not 'ipv4' list.
    count_ipv4_mtu = 0
    count_ipv6_mtu = 0
    count_ipv4_flags = 0
    count_ipv6_flags = 0

# Generated at 2022-06-13 01:54:52.660961
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    obj = SunOSNetworkCollector()
    assert obj._platform == 'SunOS'

# Generated at 2022-06-13 01:54:55.235534
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    assert SunOSNetworkCollector._fact_class is SunOSNetwork
    assert SunOSNetworkCollector._platform is 'SunOS'

# Generated at 2022-06-13 01:54:56.929798
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    """
    Constructor of class SunOSNetworkCollector.
    """
    sunos_network_collector = SunOSNetworkCollector()
    assert sunos_network_collector._fact_class == SunOSNetwork
    assert sunos_network_collector._platform == 'SunOS'


# Generated at 2022-06-13 01:54:58.138232
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    net = SunOSNetworkCollector()
    assert net.platform == 'SunOS'
    assert net.fact_class == SunOSNetwork

# Generated at 2022-06-13 01:55:00.838995
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    collectors = [SunOSNetworkCollector]

    for collector in collectors:
        obj = collector()
        assert obj.platform == 'SunOS'
        assert obj._fact_class == SunOSNetwork

# Generated at 2022-06-13 01:56:19.970531
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    import json
    import os

    # Initialize the class as it would be initialized by the module
    module = None
    ifconfig_path = '/sbin/ifconfig'
    sn = SunOSNetwork(module, ifconfig_path)

    # Provide the ifconfig output from which the interfaces information are going to be
    # collected.
    ifconfig_file = open(
        os.path.join(os.path.dirname(__file__), 'fixtures/sunos_ifconfig_a.txt')
    )
    ifconfig = ifconfig_file.read()
    ifconfig_file.close()

    # Create a mocked AnsibleModule object
    class AnsibleModuleMock(object):
        def __init__(self, ifconfig):
            self.params = {}
            self.ifconfig = ifconfig


# Generated at 2022-06-13 01:56:29.260350
# Unit test for method get_interfaces_info of class SunOSNetwork

# Generated at 2022-06-13 01:56:30.843460
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    assert issubclass(SunOSNetworkCollector, NetworkCollector)


# Generated at 2022-06-13 01:56:39.185269
# Unit test for method get_interfaces_info of class SunOSNetwork

# Generated at 2022-06-13 01:56:47.264739
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    # The 'in' variables below are those provided to a module when executing
    # 'ansible localhost -m setup'
    in_data = {
        'module_setup': True,
        'ansible_facts': {
            'ansible_machine': 'x86_64',
            'ansible_machine_id': '38f60b2d0b0308a33231896d15dfb110',
            'ansible_os_family': 'Solaris',
            'ansible_selinux': {'config_policy': 'disabled', 'status': 'disabled'},
            'ansible_system': 'SunOS',
            'ansible_system_vendor': 'Oracle Corporation',
            'ansible_user_id': 'root',
        }
    }

# Generated at 2022-06-13 01:56:49.063948
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    snc = SunOSNetworkCollector()
    assert snc._fact_class == SunOSNetwork

# Generated at 2022-06-13 01:56:58.709814
# Unit test for method get_interfaces_info of class SunOSNetwork
def test_SunOSNetwork_get_interfaces_info():
    """
    Test get_interfaces_info()
    """


# Generated at 2022-06-13 01:57:01.232207
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    collect = SunOSNetworkCollector()
    assert SunOSNetworkCollector._platform == 'SunOS'
    assert collect.get_facts() is None

# Generated at 2022-06-13 01:57:04.655832
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    """
    This is not actually a unit test, just a test to ensure that the class constructor
    for the class SunOSNetworkCollector works.
    Without this test, it would be difficult to ensure that no unit tests were missed.
    """
    return SunOSNetworkCollector()

# Generated at 2022-06-13 01:57:08.066597
# Unit test for constructor of class SunOSNetworkCollector
def test_SunOSNetworkCollector():
    from ansible.module_utils.facts.network.generic_bsd import GenericBsdNetworkCollector
    assert issubclass(SunOSNetworkCollector, GenericBsdNetworkCollector)
