

# Generated at 2022-06-13 01:37:48.156815
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    module = AnsibleModule(
        argument_spec={},
        supports_check_mode=True,
    )

    network_facts = HurdPfinetNetwork(module).populate()
    assert network_facts['interfaces'] == []


# Generated at 2022-06-13 01:37:49.702115
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    net_collector = HurdNetworkCollector()
    assert(net_collector.platform == 'GNU')
    assert(net_collector._fact_class == HurdPfinetNetwork)

# Generated at 2022-06-13 01:37:51.290079
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    HurdNetworkCollector()

# Generated at 2022-06-13 01:38:01.754466
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    class ModuleStub():
        def run_command(self, cmd):
            return 0, """\
--interface=eth0 --address=10.0.0.1 --netmask=255.255.255.0 --address6=fe80::5054:ff:fe12:3456/64
--interface=eth1 --address=192.168.0.1 --netmask=255.255.255.0 --address6=fe80::5054:ff:fe12:3456/64""", ""
    module_stub = ModuleStub()

    fsysopts_path = "/usr/bin/fsysopts"
    socket_path = "/servers/socket/inet"

    network_facts = {}
    # FIXME: build up a interfaces datastructure, then assign into network_facts
    network_facts['interfaces']

# Generated at 2022-06-13 01:38:04.820747
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    collector = HurdNetworkCollector()
    assert collector._fact_class.platform == 'GNU'

# Generated at 2022-06-13 01:38:09.138756
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    network = HurdPfinetNetwork(None)
    assert network
    assert network.device_name == '/dev/eth0'
    assert network.primary == 'eth0'
    assert network.interface_name == 'eth0'

# Generated at 2022-06-13 01:38:16.834765
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    test_module = type('test_module', (object,), {'run_command': fake_run_command})
    test_network = HurdPfinetNetwork(test_module)
    network_facts = {}
    network_facts = test_network.assign_network_facts(
        network_facts,
        '/some/path',
        '--interface=eth0 --address=192.168.1.2 --netmask=255.255.255.0'
    )

    assert network_facts['interfaces'] == ['eth0']
    assert network_facts['eth0']['active'] is True
    assert network_facts['eth0']['ipv4']['address'] == '192.168.1.2'

# Generated at 2022-06-13 01:38:27.273369
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    module_mock = MockModule()
    network_facts = {}
    fsysopts_path = 'fsysopts'
    socket_path = 'socket'

    # build up mocked output
    out = '--interface=/dev/eth0 --address=1.1.1.1 --netmask=255.255.255.0 --address6=fe80::/10'
    out = out.split()

    network_mock = HurdPfinetNetwork(module_mock)
    network_facts = network_mock.assign_network_facts(network_facts, fsysopts_path, socket_path)

    # only one interface should have been extracted
    assert len(network_facts['interfaces']) == 1
    assert network_facts['interfaces'][0] == 'eth0'
    assert network_facts

# Generated at 2022-06-13 01:38:37.540196
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    module_mock = MockAnsibleModule()
    fsysopts_path = module_mock.get_bin_path('fsysopts')

    module_mock.run_command.return_value = (0,
'--interface=eth0\n--address=10.0.0.1\n--netmask=255.255.255.0\n--mtu=1500\n--address6=fd00:1::1/64\n--address6=fd00:2::1/64\n--address6=fd00:3::1/64\n',
                                            '')
    for l in ('inet', 'inet6'):
        link = os.path.join('/servers/socket/', l)
        if os.path.exists(link):
            socket_path = link
            break

# Generated at 2022-06-13 01:38:45.804053
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    testc = HurdPfinetNetwork(dict())

    network_facts = {'interfaces': []}
    out = '''--interface=/dev/eth0 --address=10.0.2.15 --netmask=255.255.255.0 --broadcast=10.0.2.255 --address6=0:0:0:1::0/64 --route6=0:0:0:1::/64'''
    testc.assign_network_facts(network_facts, '/bin/fsysopts', '/servers/socket/inet')

# Generated at 2022-06-13 01:38:55.154735
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    mod = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )
    network = HurdPfinetNetwork(mod)
    assert len(network.collect()) == 0

# Generated at 2022-06-13 01:39:06.199692
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    """Check if populate return the expected network facts for a GNU Hurd machine"""
    module_name = 'ansible.module_utils.facts.network.gnu.hurd.HurdPfinetNetwork'
    module_args = {}
    from ansible.module_utils.facts import cache
    facts_cache = cache.FactsCache()
    mocked_module = type("mymodule", (object,), {})
    mocked_module.params = module_args
    mocked_module.run_command = lambda x: (0, "eth0\n", '')
    mocked_module.get_bin_path = lambda x: '/bin/fsysopts'
    module = HurdPfinetNetwork(mocked_module, facts_cache)
    collected_facts = {
        "ansible_facts": {
        }
    }

    facts

# Generated at 2022-06-13 01:39:09.387285
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    hurd_network_collector = HurdNetworkCollector
    assert hurd_network_collector._fact_class.platform == 'GNU'
    assert hurd_network_collector._platform == 'GNU'

# Generated at 2022-06-13 01:39:13.219947
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    module = None
    fact_ph = HurdPfinetNetwork(module)
    assert isinstance(fact_ph, HurdPfinetNetwork)
    assert fact_ph.platform == 'GNU'
    assert fact_ph._socket_dir == '/servers/socket/'

# Generated at 2022-06-13 01:39:20.731016
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    module = AnsibleModule(argument_spec={})
    network = HurdPfinetNetwork(module)
    facts = network.populate()
    interfaces_list = facts['interfaces']
    assert len(interfaces_list) > 0
    for iface in interfaces_list:
        ipv4 = facts[iface]['ipv4']
        ipv6 = facts[iface]['ipv6']
        assert len(ipv4) > 0
        assert len(ipv6) > 0


# Generated at 2022-06-13 01:39:22.659444
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    network_collector = HurdNetworkCollector()
    assert network_collector.platform == 'GNU'
    assert network_collector.fact_class == HurdPfinetNetwork

# Generated at 2022-06-13 01:39:25.670629
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    assert HurdNetworkCollector._platform == 'GNU'
    assert issubclass(HurdNetworkCollector._fact_class, HurdPfinetNetwork)


# Generated at 2022-06-13 01:39:30.714399
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    network_facts = {}
    network_facts['interfaces'] = []


# Generated at 2022-06-13 01:39:31.796915
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    HurdNetworkCollector()

# Generated at 2022-06-13 01:39:34.497198
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    from ansible.module_utils.facts.network.gnu.hurd import HurdPfinetNetwork
    network = HurdPfinetNetwork(None)
    collected_facts = dict(ansible_facts=dict(network=dict()))
    result = network.populate(collected_facts)
    assert result == co

# Generated at 2022-06-13 01:39:42.225631
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    module = AnsibleModuleMock()
    h_network = HurdPfinetNetwork(module)
    assert h_network.platform == 'GNU'
    assert h_network._socket_dir == '/servers/socket/'


# Generated at 2022-06-13 01:39:42.874361
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    nc = HurdNetworkCollector()
    assert nc._platform == 'GNU'

# Generated at 2022-06-13 01:39:52.588119
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    """ Unit tests for HurdPfinetNetwork's assign_network_facts() method """

    import os, sys
    sys.path.append(os.getcwd())
    import ansible.module_utils.facts.network.hurd.pfinet as pfinet

    # test empty facts
    output_facts = {'interfaces': []}
    pfinet_fact = pfinet.HurdPfinetNetwork()
    pfinet_fact.assign_network_facts(output_facts,
                                     '/usr/bin/fsysopts',
                                     '/servers/socket/inet')

# Generated at 2022-06-13 01:39:55.782408
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    network_facts = HurdPfinetNetwork(dict(), 'ansible.module_utils.facts.network.hurd_pfinet')
    return network_facts

# Generated at 2022-06-13 01:39:57.626929
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    collector = HurdNetworkCollector()
    assert collector.platform == 'GNU'
    assert collector.fact_class == HurdPfinetNetwork

# Generated at 2022-06-13 01:39:58.471908
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    collector = HurdNetworkCollector()
    assert collector

# Generated at 2022-06-13 01:40:06.881459
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    import ansible_collections.notstdlib.moveitallout.plugins.module_utils.facts.network.hurd.pfinet

    pf = ansible_collections.notstdlib.moveitallout.plugins.module_utils.facts.network.hurd.pfinet.HurdPfinetNetwork(None)

    assert isinstance(pf, ansible_collections.notstdlib.moveitallout.plugins.module_utils.facts.network.hurd.pfinet.HurdPfinetNetwork)

# Generated at 2022-06-13 01:40:10.437814
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    hnc = HurdNetworkCollector()
    assert hnc._platform == 'GNU'
    assert hnc._fact_class == HurdPfinetNetwork
    assert hnc.facts == []
    assert not hnc._temporary_file


# Generated at 2022-06-13 01:40:18.232091
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    # NOTE: method signature is subject to change
    module = 'TBD'
    network = HurdPfinetNetwork(module)
    network_facts = {}
    network_facts = network.assign_network_facts(network_facts, 'fsysopts', 'socket')
    assert network_facts == {}
    assert 'interfaces' in network_facts
    assert 'eth0' in network_facts
    assert 'lo' in network_facts
    assert 'active' in network_facts['eth0']
    assert network_facts['eth0']['active']
    assert 'device' in network_facts['eth0']
    assert network_facts['eth0']['device'] == 'eth0'
    assert 'ipv4' in network_facts['eth0']
    assert 'ipv6' in network_facts['eth0']

# Generated at 2022-06-13 01:40:20.516452
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    hnc = HurdNetworkCollector()
    assert hnc._platform == 'GNU'
    assert hnc._fact_class == HurdPfinetNetwork

# Generated at 2022-06-13 01:40:35.108617
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    assert HurdNetworkCollector._platform == 'GNU'
    assert HurdNetworkCollector._fact_class == HurdPfinetNetwork

# Generated at 2022-06-13 01:40:43.899531
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    module = MockModule()
    network = HurdPfinetNetwork(module)
    fsysopts_path = '/fsysopts'
    socket_path = '/socket'
    network_facts = { 'interfaces':[] }
    network_facts_full = {
        'interfaces': ['eth0'],
        'eth0': {
            'active': True,
            'device': 'eth0',
            'ipv4': {
                'address': '192.168.1.1',
                'netmask': '255.255.255.0',
            },
            'ipv6': [
                {
                    'address': 'fe80::1',
                    'prefix': '64',
                },
            ],
        },
    }

# Generated at 2022-06-13 01:40:53.006846
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    network_facts = {'interfaces': []}
    n = HurdPfinetNetwork(dict(module=dict(run_command=lambda x, y, z: (0, "address=10.0.0.1\n--interface=/dev/eth0\n--netmask=255.255.255.0\n--address6=2001:db8::1/64"),
                                          get_bin_path=lambda x: True)))

    result = n.assign_network_facts(network_facts, "fake_path", "fake_socket")
    assert result['interfaces'] == ['eth0']
    assert result['eth0']['device'] == 'eth0'
    assert result['eth0']['ipv4']['address'] == '10.0.0.1'

# Generated at 2022-06-13 01:41:00.053661
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    from ansible.module_utils.facts import Facts
    from ansible.module_utils.facts.network.tests.unit.utils import \
        ModuleTestCase, VALIDATE_PARAMS
    import json

    import sys
    if sys.version_info[0] > 2:
        basestring = (str, bytes)

    class TestModule(object):
        def __init__(self, run_command_result, get_bin_path_result):
            self.run_command_result = run_command_result
            self.get_bin_path_result = get_bin_path_result

        def run_command(self, args, **kwargs):
            if args[0] == self.get_bin_path_result:
                return 0, '', ''

# Generated at 2022-06-13 01:41:02.829809
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    network_collector = HurdNetworkCollector()
    assert network_collector._platform == 'GNU'
    assert network_collector._fact_class == HurdPfinetNetwork


# Generated at 2022-06-13 01:41:14.158222
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    class ModuleMock(object):
        def __init__(self, *args, **kwargs):
            self.params = {'ansible_check_mode': False, 'ansible_facts': {}}

# Generated at 2022-06-13 01:41:16.553026
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    collector = HurdNetworkCollector()
    assert collector._platform == 'GNU'
    assert collector._fact_class == HurdPfinetNetwork


# Generated at 2022-06-13 01:41:22.962508
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    from ansible.module_utils.facts.gather_subset import gather_subset
    from ansible.module_utils.facts.collector.network import NetworkCollector
    from ansible.module_utils.facts.collector import get_collector_fact_classes
    for fact_class in get_collector_fact_classes():
        if fact_class._platform == 'GNU':
            c = fact_class()
            c.populate()
            assert c.platform == 'GNU'
            assert hasattr(c,'_socket_dir')


if __name__ == '__main__':
    test_HurdPfinetNetwork()

# Generated at 2022-06-13 01:41:32.960044
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    args = { 'INVOCATION': {'module_name': ''}, 'module': None }
    m = HurdPfinetNetwork(args)
    nm = {
        'interfaces': [],
    }
    out = "--interface=/dev/eth0 --address=192.168.1.10 --netmask=255.255.255.0\n"
    out += "--address6=::ffff:192.168.1.10/128 --address6=fe80::7c61:f4ff:fe04:dd6d/64\n"
    m.assign_network_facts(nm, '', '')
    assert nm['interfaces'] == ['eth0', 'eth0'], nm['interfaces']

# Generated at 2022-06-13 01:41:35.170725
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    network_module = HurdPfinetNetwork(None)
    assert network_module is not None

# Generated at 2022-06-13 01:41:54.463931
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    """
    test case for method assign_network_facts of class HurdPfinetNetwork
    """
    network_facts = {}
    new_network_facts = {}
    fsysopts_path = "fsysopts"
    socket_path = "servers/socket/"
    network = HurdPfinetNetwork()
    new_network_facts = network.assign_network_facts(network_facts, fsysopts_path, socket_path)
    assert 'interfaces' in new_network_facts


# Generated at 2022-06-13 01:41:57.199431
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    network = HurdPfinetNetwork()
    assert network.platform == 'GNU'
    assert network._socket_dir == '/servers/socket/'


# Generated at 2022-06-13 01:42:06.140330
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    m = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True)
    # Module parameters
    if command_check_return('fsysopts -L /servers/socket/inet6') != 0 \
        and command_check_return('fsysopts -L /servers/socket/inet') != 0:
        m.fail_json(msg='No socket found')
    else:
        # test assign_network_facts
        HurdPfinetNetwork.assign_network_facts(
            dict(), m.get_bin_path('fsysopts'),
            command_check_output('readlink -f /servers/socket/inet'))

# Generated at 2022-06-13 01:42:08.318572
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    # Let's run this to see if there is any errors
    HurdPfinetNetwork().populate()

# Generated at 2022-06-13 01:42:18.528241
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    tests = (
        (
            dict(),
            dict(
                interfaces=['eth0'],
                eth0=dict(
                    active=True,
                    device='eth0',
                    ipv4=dict(
                        address='192.168.50.1',
                        netmask='255.255.255.0',
                    ),
                    ipv6=[dict(
                        address='fe80::5a67:b9ff:fefd:8b7',
                        prefix='64',
                    )],
                ),
            ),
        ),
    )
    for test in tests:
        module = AnsibleModuleMock()
        module.run_command_values = test[0]
        pfinet = HurdPfinetNetwork(module)
        assert pfinet.populate() == test[1]

# vim:

# Generated at 2022-06-13 01:42:28.679403
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    # Create a module for this test
    from ansible.module_utils.facts.network.gnu.hurd import HurdNetworkCollector
    module = HurdNetworkCollector()
    # Create a Network for this test with a module
    from ansible.module_utils.facts.network.base import Network
    network_instance = Network(module)
    # Create a HurdPfinetNetwork to test
    from ansible.module_utils.facts.network.gnu.hurd import HurdPfinetNetwork
    test_instance = HurdPfinetNetwork(module)
    # Call the method we want to test
    fsysopts_path = '/hurd/pfinet'
    socket_path = '/servers/socket/inet'

# Generated at 2022-06-13 01:42:34.150064
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    """
    Testing assign_network_facts for GNU Hurd
    """
    if os.path.exists('/servers/socket/inet'):
        socket_path = '/servers/socket/inet'
    elif os.path.exists('/servers/socket/inet6'):
        socket_path = '/servers/socket/inet6'
    else:
        return

    # Setting fsysopts_path
    fsysopts_path = '/hurd/fsysopts'

    network_facts = {'interfaces': [], 'all_ipv4_addresses': [], 'all_ipv6_addresses': []}
    # Testing
    pfinet_network = HurdPfinetNetwork(None)

# Generated at 2022-06-13 01:42:41.544539
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    class AnsibleModule(object):
        def __init__(self):
            self.run_command = self

        def run_command(self, a):
            self.a = a
            return 0, '--interface=/dev/eth0 --address=192.168.1.10 --netmask=255.255.255.0 --address6=::1/120', ''

    class Network(HurdPfinetNetwork):
        def __init__(self):
            self.module = AnsibleModule()

    network = Network()

    network_facts = {'interfaces': ['eth0']}
    network_facts = network.assign_network_facts(network_facts, '/bin/fsysopts', '/servers/socket/inet')
    assert network_facts['interfaces'] == ['eth0']

# Generated at 2022-06-13 01:42:46.277752
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    """
    Unit test class HurdNetworkCollector
    """
    assert HurdNetworkCollector._platform == 'GNU'
    assert HurdNetworkCollector._fact_class == HurdPfinetNetwork


# Generated at 2022-06-13 01:42:48.081509
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    net = HurdPfinetNetwork()
    assert net.platform == 'GNU'


# Generated at 2022-06-13 01:43:13.218288
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    network = HurdPfinetNetwork({'module': {}})

    assert network.interfaces == []

# Generated at 2022-06-13 01:43:18.361940
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    from ansible.module_utils.facts.network.hurd import HurdPfinetNetwork
    from ansible.module_utils._text import to_text
    from ansible.module_utils.facts import FallbackFactCollector

    facts = FallbackFactCollector().collect()
    assert isinstance(facts['network'], HurdPfinetNetwork)
    assert facts['network'].platform is not None
    assert facts['network']._socket_dir is not None
    assert to_text(facts['network']._socket_dir) == u'/servers/socket/'

# Constructor of class HurdNetworkCollector

# Generated at 2022-06-13 01:43:27.924397
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    import json
    from ansible.module_utils._text import to_text
    from ansible.module_utils.facts.network.gnu.hurd import HurdPfinetNetwork
    from ansible.module_utils.facts.network.gnu.hurd import HurdNetworkCollector
    from ansible.module_utils.six import PY3
    from ansible.module_utils.six.moves import StringIO

    if PY3:
        from io import StringIO

    # FIXME: mock this all out
    module = type('module', (object,), {
        'run_command': lambda self, args, check_rc=True: (0, None, None),
    })()

    # FIXME: mock this all out

# Generated at 2022-06-13 01:43:33.643686
# Unit test for method assign_network_facts of class HurdPfinetNetwork

# Generated at 2022-06-13 01:43:35.034279
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    """
    This is a unit test for constructor of class HurdPfinetNetwork
    """
    pass

# Generated at 2022-06-13 01:43:38.409578
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    collector = HurdNetworkCollector()
    assert collector._platform == 'GNU'
    assert collector._fact_class is HurdPfinetNetwork

# Generated at 2022-06-13 01:43:46.189896
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    module = FakeAnsibleModule()
    obj = HurdPfinetNetwork(module)
    ifaces_count = 0
    if obj.populate():
        ifaces_count = len(obj.populate()['interfaces'])
        for iface in obj.populate()['interfaces']:
            assert obj.populate()[iface]['device'] == iface
            assert 'ipv4' in obj.populate()[iface]
            assert 'ipv6' in obj.populate()[iface]
    assert ifaces_count > 0



# Generated at 2022-06-13 01:43:50.464014
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    module = AnsibleModule(argument_spec={
        'path_to_fsysopts': {'required': True, 'type': 'str'},
        'path_to_socket': {'required': True, 'type': 'str'}
    })
    pfinet_network = HurdPfinetNetwork(module)
    network_facts = {}
    fsysopts_path = module.params['path_to_fsysopts']
    socket_path = module.params['path_to_socket']
    network_facts = pfinet_network.assign_network_facts(network_facts, fsysopts_path, socket_path)
    assert network_facts['interfaces'] == ['eth0', 'enp0s3']
    asse

# Generated at 2022-06-13 01:43:51.282985
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    pass

# Generated at 2022-06-13 01:44:02.145096
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    from ansible.module_utils.facts.network.base import Network
    from ansible.module_utils.facts.network.hurd.pfinet.pfinet_utils import HurdPfinetNetwork

    class FakeModule(object):
        def run_command(self, command):
            # create a temporary fake output with the well known format
            out = "--interface=/dev/eth0 --address=10.0.0.1 --netmask=255.255.255.0 --address6=/10.0.0.1/24 --address6=/10.0.0.2/24"
            return (0, out, None)

        def get_bin_path(self, name):
            # FIXME: fake
            return '/bin/fsysopts'


# Generated at 2022-06-13 01:45:14.690832
# Unit test for constructor of class HurdPfinetNetwork
def test_HurdPfinetNetwork():
    from ansible.module_utils.facts.network.gnu.pfinet import HurdPfinetNetwork
    n = HurdPfinetNetwork()
    assert n._socket_dir == '/servers/socket/'
    assert n._platform == 'GNU'


# Generated at 2022-06-13 01:45:19.589886
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    import os
    import tempfile
    mod = FakeModule()
    mod.run_command = fake_run_command
    net = HurdPfinetNetwork(module=mod)

    expected_network_facts = {'interfaces': ['lo', 'eth0'],
           'eth0': {'ipv4': {'netmask': '255.255.0.0', 'address': '192.168.0.3'},
                    'active': True,
                    'device': 'eth0',
                    'ipv6': [{'prefix': '64', 'address': '2a02::1'}]},
           'lo': {'ipv4': {},
                  'active': True,
                  'device': 'lo',
                  'ipv6': []}}

    # Create a fake fsysopts output file

# Generated at 2022-06-13 01:45:22.629366
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    hnc = HurdNetworkCollector()
    assert hnc._platform == 'GNU'
    assert hnc._fact_class == HurdPfinetNetwork



# Generated at 2022-06-13 01:45:33.523227
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    output = (
        "--address=10.0.0.31 --netmask=255.255.255.0 --address6=fe80::a00:27ff:fe39:5e5d/64 --interface=/dev/eth0 --interface=/dev/eth1\n"  # noqa
    )
    hostname = None
    env = dict()
    ansible_module = FakeAnsibleModule(output, hostname, env)
    network_facts = {}
    fsysopts_path = '/bin/fsysopts'
    socket_path = '/servers/socket/inet'
    pfinet_network = HurdPfinetNetwork(ansible_module)
    result = pfinet_network.assign_network_facts(network_facts, fsysopts_path, socket_path)
    interfaces

# Generated at 2022-06-13 01:45:40.507853
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    module = AnsibleModule(argument_spec={})
    module.run_command = lambda *args, **kwargs: (0, '--interface=/dev/eth0 --address=192.168.1.100 --netmask=255.255.255.0', '')
    module.get_bin_path = lambda arg: arg
    a = HurdPfinetNetwork(module=module)
    print(a.assign_network_facts({}, 'fsysopts', '/servers/socket/inet'))
    module.run_command = lambda *args, **kwargs: (0, '--interface=/dev/eth0 --address=192.168.1.100 --netmask=255.255.255.0 --address6=2001::/64', '')

# Generated at 2022-06-13 01:45:47.148712
# Unit test for method populate of class HurdPfinetNetwork
def test_HurdPfinetNetwork_populate():
    from ansible.module_utils.facts.network.dummy import DummyNetworkModule
    from ansible.module_utils.facts.network.dummy import DummyNetworkPrefs
    network_module = DummyNetworkModule()
    network_prefs = DummyNetworkPrefs()
    network_prefs.paths['ifconfig'] = '/bin/true'
    HurdPfinetNetwork(network_module, network_prefs).populate()
    assert 'interface' in network_module.facts['ansible_interfaces']

# Generated at 2022-06-13 01:45:49.327216
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    assert HurdNetworkCollector(None)._platform == 'GNU'
    assert HurdNetworkCollector(None)._fact_class == HurdPfinetNetwork


# Generated at 2022-06-13 01:45:56.449383
# Unit test for method assign_network_facts of class HurdPfinetNetwork
def test_HurdPfinetNetwork_assign_network_facts():
    module = type('Module', (object,), {})
    module.run_command = type('run_command', (object,), {})
    module.run_command.return_value = type('return_value', (object,), {
        'rc': 0,
        'stdout': """--interface=/dev/eth0 --address 192.168.0.1 --netmask 255.255.255.0 --address6=fe80::216:3eff:fe31:80c1/64 --address6=2001:db8:0:1:216:3eff:fe31:80c1/64""",
        'stderr': ''
    })

    obj = HurdPfinetNetwork(module)
    result = obj.assign_network_facts({}, '/bin/true', '/servers/socket/inet')
    assert result

# Generated at 2022-06-13 01:45:58.988409
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    collector = HurdNetworkCollector()
    assert collector.__class__.__name__ == 'HurdNetworkCollector'


# Generated at 2022-06-13 01:46:03.891554
# Unit test for constructor of class HurdNetworkCollector
def test_HurdNetworkCollector():
    network_collector = HurdNetworkCollector()
    assert network_collector.__class__.__name__ == 'HurdNetworkCollector'
    assert network_collector._platform == 'GNU'
    assert network_collector._fact_class == HurdPfinetNetwork
    assert network_collector._networks == []