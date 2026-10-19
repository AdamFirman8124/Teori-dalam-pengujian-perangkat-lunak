

# Generated at 2022-06-13 01:17:06.445711
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    module = MockModule()
    aix_facts = AIXNetwork(module=module)

    # Test return type
    interfaces, ips = aix_facts.get_interfaces_info(ifconfig_path='/sbin/ifconfig',
                                                              ifconfig_options='-a')
    assert type(interfaces) is dict
    assert type(ips) is dict

    # Test return values
    for interface in interfaces:
        assert type(interfaces[interface]) is dict
    for interface in interfaces:
        for key in interfaces[interface]:
            assert type(interfaces[interface][key]) is list or type(interfaces[interface][key]) is str or type(
                interfaces[interface][key]) is int
    for key in ips:
        assert type(ips[key]) is list


# Generated at 2022-06-13 01:17:11.874137
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    """ aix_network_collector.py: test_AIXNetworkCollector() """
    ansible = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )

    # instantiate AIXNetworkCollector class
    ansible_AIXNetworkCollector = AIXNetworkCollector(ansible)

    # check AIXNetworkCollector object's attribute '_platform'
    assert ansible_AIXNetworkCollector._platform == 'AIX'

    # check AIXNetworkCollector object's attribute '_fact_class'
    assert ansible_AIXNetworkCollector._fact_class == AIXNetwork

# Generated at 2022-06-13 01:17:23.315587
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():

    class Module(object):
        def get_bin_path(self, arg1):
            return '/usr/bin/netstat'

        def run_command(self, arg):
            if arg == ['/usr/bin/netstat', '-nr']:
                return 0, 'default  10.0.0.6 UG        0        5 en1\ndefault  fe80::2 UG        0        5 en1', ''
            else:
                return 1, '', 'netstat not found'

        def fail_json(self, **kwargs):
            return False

    module_inst = Module()

    class AIXNetwork(NetworkCollector):
        platform = 'AIX'

    ans = AIXNetwork(module_inst)


# Generated at 2022-06-13 01:17:34.458873
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    from ansible.module_utils.facts.network.base import NetworkCollector
    import os
    import json

    nc = NetworkCollector()
    nc.module = NetworkCollector()
    nc.module.run_command = run_command
    nc.module.get_bin_path = get_bin_path
    nc.module.debug = debug
    nc.module.run_command = run_command
    nc.module.get_bin_path = get_bin_path

    # empty file
    with open('./test_AIXNetwork_get_default_interfaces_no_lines', 'w') as f:
        f.write('')
        f.close()

# Generated at 2022-06-13 01:17:40.976093
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    ansible_module = mock_module()

    ifconfig_path = ansible_module.get_bin_path('ifconfig')

    interface_file = open(os.path.join(os.path.dirname(__file__), '../../output/interface.txt'), 'r')
    dump_interfaces = interface_file.read()
    interface_file.close()

    with open(os.path.join(os.path.dirname(__file__), '../../output/netstat.txt'), 'r') as netstat_file:
        dump_netstat = netstat_file.read()

    with open(os.path.join(os.path.dirname(__file__), '../../output/uname.txt'), 'r') as uname_file:
        dump_uname = uname_file.read()

# Generated at 2022-06-13 01:17:52.908480
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    ifconfig_path = 'ifconfig'
    ifconfig_options = '-a'
    ifconfig_path_result = 'ifconfig'
    ifconfig_options_result = '-a'

# Generated at 2022-06-13 01:17:54.218664
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    assert AIXNetworkCollector.__name__ == 'AIXNetworkCollector'


# Generated at 2022-06-13 01:18:03.074635
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():

    from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork
    from ansible.module_utils.facts.network.aix import AIXNetwork

    import sys
    import os

    sys.path.insert(0, os.path.dirname(__file__) + '/../../../../')
    from ansible.module_utils.facts import ModuleStub
    from ansible.module_utils.facts import FactCollector

    # ToDo: Create real file instead of StringIO as workaround
    #       to give the output of command to test
    import StringIO

    # ToDo: Create better tests

# Generated at 2022-06-13 01:18:06.538359
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    test_AIXNetwork_get_interfaces_info.network_instance = AIXNetwork()

    # test_AIXNetwork_get_interfaces_info.network_instance.get_interfaces_info(ifconfig_path, ifconfig_options)
    assert test_AIXNetwork_get_interfaces_info.network_instance, 'Unable to create instance of AIXNetwork'

# Generated at 2022-06-13 01:18:15.302995
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts.network.utils import get_file_content

    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=False,
    )

    # set up the class
    my_class = AIXNetwork(module)
    # get the route content
    route_path = my_class.module.get_bin_path('route')
    route_txt = get_file_content(route_path)

    # set up the return values
    interface = dict(v4={}, v6={})
    interface['v4']['gateway'] = '192.168.2.1'
    interface['v4']['interface'] = 'en0'

# Generated at 2022-06-13 01:18:31.727279
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    from ansible.module_utils.facts.network.aix import AIXNetworkCollector
    from ansible.module_utils.facts.network.base import NetworkCollector
    from ansible.module_utils.facts.network.aix import AIXNetwork
    from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork
    from ansible.module_utils._text import to_bytes

    collector = AIXNetworkCollector()
    assert isinstance(collector, NetworkCollector)
    assert isinstance(collector._fact_class, AIXNetwork)
    assert isinstance(collector._fact_class, GenericBsdIfconfigNetwork)
    assert collector._platform == 'AIX'

# Generated at 2022-06-13 01:18:41.648289
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    from ansible_collections.misc.not_a_real_collection.tests.unit.compat.mock import patch
    from ansible_collections.misc.not_a_real_collection.tests.unit.modules.utils import AnsibleExitJson
    from ansible_collections.misc.not_a_real_collection.tests.unit.modules.utils import AnsibleFailJson
    from ansible_collections.misc.not_a_real_collection.tests.unit.modules.utils import ModuleTestCase
    from ansible_collections.misc.not_a_real_collection.tests.unit.modules.utils import set_module_args


# Generated at 2022-06-13 01:18:48.440160
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    assert AIXNetworkCollector.__name__ == 'AIXNetworkCollector'
    assert AIXNetworkCollector.platform == 'AIX'
    assert AIXNetworkCollector.get_default_interfaces.__name__ == 'AIXNetworkCollector.get_default_interfaces'
    assert AIXNetworkCollector.get_interfaces_info.__name__ == 'AIXNetworkCollector.get_interfaces_info'


# Generated at 2022-06-13 01:18:54.422739
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    from ansible.module_utils import basic
    from ansible.module_utils.facts.collector.network.aix import AIXNetworkCollector

    ansible_module = basic.AnsibleModule(
        argument_spec=dict()
    )

    network_collector = AIXNetworkCollector(ansible_module)

    assert network_collector.platform == 'AIX'
    assert isinstance(network_collector, AIXNetworkCollector)



# Generated at 2022-06-13 01:19:05.451990
# Unit test for method get_interfaces_info of class AIXNetwork

# Generated at 2022-06-13 01:19:13.912401
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    try:
        from ansible.module_utils.facts.network.aix import AIXNetwork
    except ImportError:
        return  # noqa

    module = DummyAnsibleModule()

    an = AIXNetwork(module)
    an.get_interfaces_info = an.get_interfaces_info.__func__

    rc = 0

# Generated at 2022-06-13 01:19:20.709569
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    interfaces = {}
    current_if = {}
    ips = dict(
        all_ipv4_addresses=[],
        all_ipv6_addresses=[],
    )

# Generated at 2022-06-13 01:19:26.834568
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    module = MockAnsibleModule(
        dict(
            route_path='/usr/sbin/netstat'
        ))
    get_default_interfaces_result = AIXNetwork._get_default_interfaces(module)
    assert get_default_interfaces_result[0] == '10.0.2.2'
    assert get_default_interfaces_result[1] == 'fe80::900:2ff:fe21:862c'


# Generated at 2022-06-13 01:19:27.672641
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    net = AIXNetwork()
    net.get_default_interfaces("/sbin/route")

# Generated at 2022-06-13 01:19:36.936957
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    # given
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=False)
    network_module = AIXNetwork(module)

    # and
    ifconfig_path = network_module.module.get_bin_path('ifconfig')
    # and
    rc, out, err = module.run_command([ifconfig_path, '-a'])

    # when
    interfaces, ips = network_module.get_interfaces_info(ifconfig_path, '-a')

    # then
    assert out, 'ifconfig command must return something'
    assert rc == 0, 'ifconfig command must return rc 0'
    assert len(interfaces) > 0, 'interfaces must contain at least one interface'
    assert len(ips['all_ipv4_addresses']) > 0

# Generated at 2022-06-13 01:20:10.673636
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():

    from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork

    module = AnsibleModule()
    network = AIXNetwork(module=module)

    # Test correct parsing of 'ifconfig -a' output with wpar and no wpar
    with open('/tmp/test_AIXNetwork_get_interfaces_info.txt', 'r') as f:
        ifconfig_out = f.read()
        interfaces, ips = network.get_interfaces_info('/usr/sbin/ifconfig', '-a')

        assert interfaces['fcs0']['device'] == 'fcs0'
        assert interfaces['fcs0']['flags'] == ['UP', 'SIMPLEX', 'MULTICAST', 'NOARP', 'NOAUTOIND']

# Generated at 2022-06-13 01:20:11.545548
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    # FIXME: provide test
    pass

# Generated at 2022-06-13 01:20:16.032800
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    _platform = 'AIX'
    _fact_class = AIXNetwork
    x = AIXNetworkCollector(_platform, _fact_class)
    assert x._platform == 'AIX'
    assert x._fact_class == AIXNetwork
    assert issubclass(x._fact_class, NetworkCollector)

# Generated at 2022-06-13 01:20:23.439013
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    """
    Unit test for constructor of class AIXNetworkCollector
    """
    # Unit test to add option to command line or to update existing option
    def _set_command_line_options(option, value):
        # A dict will not work here, because 'dict' object does not support item assignment
        # So use setattr instead
        setattr(AIXNetworkCollector, option, value)

    # Unit test to set a new platform name
    def _set_platform_name(value):
        AIXNetworkCollector._platform = value

    def _assert(condition):
        # AssertionError will be raised if condition is not True
        assert condition


# Generated at 2022-06-13 01:20:34.189145
# Unit test for method get_interfaces_info of class AIXNetwork

# Generated at 2022-06-13 01:20:35.644744
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    assert isinstance(AIXNetworkCollector(), AIXNetworkCollector)

# Generated at 2022-06-13 01:20:45.576571
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    # pylint: disable=R0902
    # pylint: disable=R0915
    # pylint: disable=R1710
    """Unit test for method parse_interface_line of class AIXNetwork"""
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.facts.network.aix import AIXNetwork

    module = AnsibleModule(
        argument_spec=dict(),
    )

    network = AIXNetwork(module)
    ifconfig_path = 'ifconfig'
    ifconfig_options = '-a'
    interfaces, ips = network.get_interfaces_info(ifconfig_path, ifconfig_options)
    assert interfaces['lo0']['device'] == 'lo0'
    assert interfaces['lo0']['flags'] == ['UP']


# Generated at 2022-06-13 01:20:54.847681
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    obj = AIXNetworkCollector()
    assert obj._platform == 'AIX'
    assert obj._fact_class == AIXNetwork
    assert isinstance(obj._facts, dict)
    assert 'default_interface' not in obj._facts
    assert 'default_ipv4' not in obj._facts
    assert 'default_ipv6' not in obj._facts
    assert 'interfaces' not in obj._facts
    assert 'all_ipv4_addresses' not in obj._facts
    assert 'all_ipv6_addresses' not in obj._facts

# Generated at 2022-06-13 01:20:59.541709
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork
    from ansible.module_utils.facts.network.aix import AIXNetwork
    module = AnsibleModuleMock()
    ifconfig_path = module.get_bin_path('ifconfig')
    ifconfig_options = '-a'
    aix_network = AIXNetwork(module)
    interfaces, ips = aix_network.get_interfaces_info(ifconfig_path, ifconfig_options)
    generic_bsd_network = GenericBsdIfconfigNetwork(module)
    generic_interfaces, generic_ips = generic_bsd_network.get_interfaces_info(ifconfig_path, ifconfig_options)
    assert(interfaces == generic_interfaces)

# Generated at 2022-06-13 01:21:07.183132
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    from ansible.module_utils.facts.network.generic_bsd import GenericBsdOpenBSDIfconfigNetwork
    from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork
    from ansible.module_utils.facts.collector import BaseFactCollector
    class MockedModule:
        def __init__(self):
            self.params = dict()

        def get_bin_path(self, path, opts=None):
            # we don't care about opts
            if path == 'uname':
                return '/usr/bin/uname'
            if path == 'entstat':
                return '/usr/bin/entstat'
            if path == 'lsattr':
                return '/usr/sbin/lsattr'

# Generated at 2022-06-13 01:21:56.381934
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    module = NetworkCollector.get_network_module(None)
    network = AIXNetwork(module)
    default_v4, default_v6 = network.get_default_interfaces()
    assert isinstance(default_v4, dict)
    assert isinstance(default_v6, dict)
    assert isinstance(default_v4.get('interface'), str) or default_v4.get('interface') is None
    assert isinstance(default_v4.get('gateway'), str) or default_v4.get('gateway') is None
    assert isinstance(default_v6.get('interface'), str) or default_v6.get('interface') is None
    assert isinstance(default_v6.get('gateway'), str) or default_v6.get('gateway') is None

# Generated at 2022-06-13 01:21:57.566626
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    result = AIXNetworkCollector()
    assert result is not None


# Generated at 2022-06-13 01:22:00.461046
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    network_collector = AIXNetworkCollector()
    network_collector.get_default_interfaces('/tmp')


if __name__ == '__main__':
    test_AIXNetwork_get_default_interfaces()

# Generated at 2022-06-13 01:22:06.490522
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    from ansible.module_utils.facts.network.aix import AIXNetwork
    test_module = {"run_command": lambda cmd, **kwargs: (0, '', '')}
    aix_net = AIXNetwork(test_module)
    aix_net.get_interfaces_info("test_ifconfig_path", "test_ifconfig_options")

# Generated at 2022-06-13 01:22:14.956954
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    """
    Check for:
    - should return dict with values, if netstat returns information about gateway
    - should return dict with empty strings, if netstat do not return information about gateway
    - should return dict with empty strings, if route file do not exist
    - should return dict with empty strings, if route is not executable
    - should return dict with empty strings, if route returns error
    """
    #
    # netstat should returns information about gateway, module should return dict with values
    #
    mock = {
        'run_command.return_value': (0, 'default 123.123.123.123 UG 0 15 en3', ''),
    }
    module = type('module', (object,), dict(params={}, run_command=lambda self, a: mock['run_command.return_value']))()
    aix_network = AI

# Generated at 2022-06-13 01:22:19.610579
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    AIX_NETWORK = AIXNetwork()
    TEST_LINES = [
        'en0: flags=1e084863,480<UP,BROADCAST,NOTRAILERS,RUNNING,SIMPLEX,MULTICAST,GROUPRT,64BIT,CHECKSUM_OFFLOAD(ACTIVE),CHAIN>',
        '        inet 192.168.1.33 netmask 0xffffff00 broadcast 192.168.1.255',
        '        nd6 options=3<PERFORMNUD,ACCEPT_RTADV>',
        '        media: autoselect',
        '        status: active',
    ]
    TEST_OBJ = AIX_NETWORK.get_interfaces_info('fake_ifconfig_path', TEST_LINES)

# Generated at 2022-06-13 01:22:20.973491
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    assert(AIXNetworkCollector().platform == 'AIX')

# Generated at 2022-06-13 01:22:26.684462
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    test_file = 'ansible/modules/network/facts/test_get_interfaces_info_aix.txt'
    fhandler = open(test_file, 'r')
    result = AIXNetwork().get_interfaces_info(None, fhandler.read())
    for interface in result:
        assert interface == 'en0', 'unexpected interface %s' % interface



# Generated at 2022-06-13 01:22:35.078422
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():

    test_obj = AIXNetwork()

    ifconfig_path = '/usr/sbin/ifconfig'
    ifconfig_options = '-a'

    # test output of ifconfig -a

# Generated at 2022-06-13 01:22:39.495353
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():

    class AIXModule:
        def get_bin_path(self, command, required=False):
            if command == 'netstat':
                return 'netstat'
            else:
                return None

        def run_command(self, args, check_rc=True, close_fds=True, executable=None, data=None):

            try:
                from StringIO import StringIO
            except ImportError:
                from io import StringIO
            import textwrap

            if args == ['netstat', '-nr']:
                output = textwrap.dedent("""\
                    default 172.17.0.1 UG 0 0 en0
                    default - UGS 0 0 lo0
                    default fe80::%lo0/64 UG 0 0 lo0
                    default fe80::%en0/64 UG 0 0 en0
                    """)

# Generated at 2022-06-13 01:24:10.295299
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    module = AnsibleModule(argument_spec={}, supports_check_mode=True)
    network_collector = AIXNetworkCollector(module=module)
    network = network_collector.get_network_facts()
    assert 'default_ipv4' in network, "Default IPv4 interface was not found"
    assert 'default_ipv4' in network['default_ipv4'], "Default IPv4 interface name was not found"
    assert 'default_ipv6' in network, "Default IPv6 interface was not found"
    assert 'default_ipv6' in network['default_ipv6'], "Default IPv6 interface name was not found"

# Generated at 2022-06-13 01:24:18.708167
# Unit test for method get_interfaces_info of class AIXNetwork

# Generated at 2022-06-13 01:24:28.870144
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    """
    This function is used to test the constructor of
    class AIXNetworkCollector.
    :return: Returns a message about the test success or
    test failure along with the list of interfaces.
    """
    ansible = AnsibleModuleMock()
    result = AIXNetworkCollector(ansible=ansible)
    assert str(result) == 'Networking Facts AIX Module', \
        'Actual: {0}'.format(result)
    assert ansible == result._module, \
        'Actual: {0}'.format(result._module)
    assert isinstance(result._classes['AIXNetwork'], AIXNetwork), \
        'Actual: {0}'.format(result._classes['AIXNetwork'])

# Generated at 2022-06-13 01:24:30.509085
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    AIXNetworkCollector()

# Generated at 2022-06-13 01:24:31.940910
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    assert AIXNetwork(NetworkCollector()).get_default_interfaces('/bin/netstat') == ({}, {})

# Generated at 2022-06-13 01:24:33.604450
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    instance = AIXNetworkCollector()
    assert isinstance(instance, AIXNetworkCollector)


# Generated at 2022-06-13 01:24:42.829106
# Unit test for method get_interfaces_info of class AIXNetwork

# Generated at 2022-06-13 01:24:49.646826
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    fact_data = dict()
    fact_data['default_ipv4'] = dict(gateway='1.1.1.1', interface='eth0')
    fact_data['default_ipv6'] = dict(gateway='fd4f:45a4:76e8::1', interface='eth0')
    fact_data['interfaces'] = dict(eth0=dict(active=True,
                                             device_id='eth0',
                                             macaddress='00:11:22:33:44:55',
                                             type='ether'))
    fact_data['all_ipv4_addresses'] = ['10.10.10.10',
                                       '1.1.1.1',
                                       '192.168.1.1',
                                       '172.16.1.1']
    fact

# Generated at 2022-06-13 01:24:55.690486
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    mod = AnsibleModule(argument_spec={})
    net_collector = AIXNetworkCollector(module=mod)
    assert net_collector._fact_class == AIXNetwork
    assert net_collector._platform == 'AIX'
    assert net_collector._network_provider == 'NetworkCollector'
    assert net_collector.ignore_on_vars == ['ansible_eth0']
    assert net_collector.ignore_interfaces == ['lo']
    assert net_collector._ignore_interfaces == ['lo']
    assert net_collector._ignore_params == ['interface', 'type', 'aliases', 'ipv4', 'ipv6']
    assert net_collector._provider == 'NetworkCollector'

# Generated at 2022-06-13 01:25:03.962352
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():

    # start with empty AixNetwork class
    aix_network = AIXNetwork()

    # set some attributes for test
    setattr(aix_network, '_module', open('/dev/null', 'a+'))
    setattr(aix_network, 'module', open('/dev/null', 'a+'))
    setattr(aix_network.module, 'bin_path', lambda x: '/sbin/netstat')
    setattr(aix_network.module, 'run_command', lambda x: (0, 'default xxx.xxx.xxx.xxx UG 0 0 32768 en1\ndefault ::1 UG 0 0 32768 en2', ''))

    if_v4, if_v6 = aix_network.get_default_interfaces('/sbin/route')

    assert if_