

# Generated at 2022-06-13 01:17:02.502483
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    from ansible.module_utils.facts.network.aix import AIXNetwork
    from ansible.module_utils.facts.network.generic_bsd import get_ifconfig_path
    from ansible.module_utils.facts.network.aix import AIXNetworkCollector
    from ansible.module_utils._text import to_bytes
    import io

    # --------------- Test input data -----------------------

# Generated at 2022-06-13 01:17:11.160756
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    module = AnsibleModule(
        argument_spec=dict(
            gather_subset=dict(default=['!all'], type='list'),
        ),
        supports_check_mode=True,
    )

    ifconfig_path = module.get_bin_path('ifconfig')
    netstat_path = module.get_bin_path('netstat')
    uname_path = module.get_bin_path('uname')

    if not all([ifconfig_path, netstat_path, uname_path]):
        module.fail_json(msg='Clould not find required commands: ifconfig, netstat, uname.')

    rc, out, err = module.run_command([uname_path, '-W'])

# Generated at 2022-06-13 01:17:22.946609
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    lines = [
        "default 192.168.1.254 UG 1 0 en0",
        "default ::/0 UG 1 0 en0",
    ]
    expected_v4 = {'gateway': '192.168.1.254', 'interface': 'en0'}
    expected_v6 = {'gateway': '::', 'interface': 'en0'}

    module = DummyAnsibleModule()
    network = AIXNetwork(module)
    module.run_command.return_value = (0, '\n'.join(lines), '')

    fact_v4, fact_v6 = network.get_default_interfaces('route')
    assert fact_v4 == expected_v4
    assert fact_v6 == expected_v6



# Generated at 2022-06-13 01:17:34.362615
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():

    class A():
        def __init__(self):
            self.bin_path = '/bin'
            self.get_bin_path = self.bin_path_mock


# Generated at 2022-06-13 01:17:35.872821
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    net = AIXNetwork()
    net.get_default_interfaces('netstat_path')



# Generated at 2022-06-13 01:17:41.614269
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    module = AnsibleModule(argument_spec=dict())
    ansible_network_facts = dict(
        network=AIXNetworkCollector(module).collect()
    )
    assert 'default_ipv4' in ansible_network_facts['network']
    assert 'default_ipv6' in ansible_network_facts['network']
    assert 'interfaces' in ansible_network_facts['network']
    assert 'all_ipv4_addresses' in ansible_network_facts['network']
    assert 'all_ipv6_addresses' in ansible_network_facts['network']


# Generated at 2022-06-13 01:17:50.263990
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    test_module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )
    test_AIXNetwork = AIXNetwork(test_module)
    test_default_interfaces = test_AIXNetwork.get_default_interfaces('/sbin/route')
    assert test_default_interfaces[0]['gateway'] == '172.16.44.254'
    assert test_default_interfaces[0]['interface'] == 'en0'


# Generated at 2022-06-13 01:17:59.170422
# Unit test for method get_interfaces_info of class AIXNetwork

# Generated at 2022-06-13 01:18:06.367043
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    # Test instantiation of AIXNetworkCollector
    obj = AIXNetworkCollector()

    # Test __new__ method of object
    assert isinstance(obj, NetworkCollector), "Object is not of type Network"
    assert isinstance(obj, AIXNetworkCollector), "Object is not of type AIXNetworkCollector"

    # Test __init__ method of object
    assert obj._fact_class is AIXNetwork, "Class AIXNetworkCollector should be of type AIXNetwork"
    assert obj._platform == "AIX", "Value of _platform should be 'AIX'"

    # Test get_facts function of object
    assert callable(obj.get_facts), "Function 'get_facts' is not callable"

# Generated at 2022-06-13 01:18:15.184827
# Unit test for method get_interfaces_info of class AIXNetwork

# Generated at 2022-06-13 01:18:39.340725
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    import os
    import sys
    import platform
    import tempfile
    import shutil
    import sys
    if sys.version_info[0] == 2:
        from cStringIO import StringIO
    else:
        from io import StringIO
    import ansible.module_utils.facts.network.aix
    _load_params = ansible.module_utils.facts.network.aix.load_params
    _get_default_interfaces = ansible.module_utils.facts.network.aix.AIXNetwork.get_default_interfaces

    # create temporary directory
    module_tmpdir = tempfile.mkdtemp()
    # create temporary module

# Generated at 2022-06-13 01:18:40.546476
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    assert isinstance(AIXNetworkCollector(), NetworkCollector)

# Generated at 2022-06-13 01:18:43.943020
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    network_collector = AIXNetworkCollector()
    assert network_collector._platform == 'AIX'
    assert network_collector._fact_class == AIXNetwork

# Generated at 2022-06-13 01:18:46.428653
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    result = AIXNetworkCollector()
    assert result._platform == 'AIX'
    assert result._fact_class == AIXNetwork

# Generated at 2022-06-13 01:18:50.011605
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    a = AIXNetwork('/sbin/ifconfig', '', '')
    a.get_interfaces_info = mock_get_interfaces_info
    a.get_default_interfaces('')



# Generated at 2022-06-13 01:18:58.959068
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    ifconfg_path = '/etc/ifconfg'
    ifconfig_options = '-a'
    network = AIXNetwork(None)
    network.module.get_bin_path = lambda x: '/bin/ifconfig'

# Generated at 2022-06-13 01:19:09.598974
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():

    class MockModule(object):
        def __init__(self, bin_path_results):
            self._bin_path_results = bin_path_results

        def get_bin_path(self, name):
            return self._bin_path_results[name]

        def run_command(self, cmd):
            return 0, 'execute: ' + ' '.join(cmd), ''

    # Test the running in a WPAR
    bin_path_results = {
        'ifconfig': '/sbin/ifconfig',
        'entstat': '/usr/bin/entstat',
        'lsattr': '/usr/sbin/lsattr',
        'uname': '/usr/bin/uname',
    }
    module = MockModule(bin_path_results)

# Generated at 2022-06-13 01:19:20.937462
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    from ansible.module_utils.facts.network.base import NetworkCollector
    from ansible.module_utils.facts.network.aix import AIXNetwork

    class ModuleStub:

        @staticmethod
        def get_bin_path(name):
            return '/bin/' + name

    class ModuleUtilsStub:

        @staticmethod
        def run_command(command):
            return 0, '', ''

    class NetworkCollectorStub(NetworkCollector):

        def __init__(self, module):
            self.module = ModuleStub()
            self.module_utils = ModuleUtilsStub()

    class AIXNetworkStub(AIXNetwork):
        platform = 'AIX'

    ifconfig_path = '/bin/ifconfig'
    ifconfig_options = '-a'
    ifconfig_

# Generated at 2022-06-13 01:19:31.375075
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():

    from ansible.module_utils.facts.network.aix.collector import AIXNetworkCollector
    from ansible.module_utils.facts.network.aix.normalizer import AIXNetworkNormalizer

    try:
        from unittest.mock import Mock, patch
    except:
        from mock import Mock, patch

    facts = Mock()

    aix_collect = AIXNetworkCollector(facts)
    aix_collect.collect()

    assert isinstance(aix_collect._ifconfig, AIXNetwork)
    assert isinstance(aix_collect._normalizer, AIXNetworkNormalizer)
    assert isinstance(aix_collect._facts['ansible_' + AIXNetworkCollector._platform], dict)



# Generated at 2022-06-13 01:19:33.156650
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    module = NetworkCollector.get_module(params=dict())
    obj = AIXNetwork(module)
    route_path = module.get_bin_path('netstat')

    assert obj.get_default_interfaces(route_path) == ({}, {})

# Generated at 2022-06-13 01:19:58.897537
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    ansible_module = AnsibleModuleMock()
    platform = AIXNetworkCollector(ansible_module)
    assert platform.platform == 'AIX'
    assert platform.is_platform_supported()
    assert platform._fact_class == AIXNetwork



# Generated at 2022-06-13 01:20:02.988157
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    module = AnsibleModuleMock()
    fact_class = AIXNetworkCollector(module)
    assert isinstance(fact_class._fact_class(module), AIXNetwork)
    assert fact_class._platform == 'AIX'


# Generated at 2022-06-13 01:20:07.192875
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    network = AIXNetwork()
    net_default = network.get_default_interfaces("/usr/sbin/route")
    assert net_default == ({"gateway": "10.128.211.254", "interface": "en0"},{})


# Generated at 2022-06-13 01:20:17.114662
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    from ansible.module_utils.facts.network.aix import AIXNetwork

    route_path = '/usr/sbin/route'
    aix_net = AIXNetwork(dict(module=dict()))
    returned_value = aix_net.get_default_interfaces(route_path)
    returned_value_v4 = returned_value[0]
    returned_value_v6 = returned_value[1]
    assert returned_value_v4['gateway'] == '172.16.20.1', 'Failed AIXNetwork method get_default_interfaces v4 gateway'
    assert returned_value_v4['interface'] == 'en7', 'Failed AIXNetwork method get_default_interfaces v4 interface'

# Generated at 2022-06-13 01:20:23.521983
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    """
    test method AIXNetwork.get_default_interfaces
    """
    route_path = '/etc/route'
    interface = {'v4': {'gateway': '192.168.1.1', 'interface': 'en3'},
                 'v6': {'gateway': 'fe80::21c:42ff:feab:552c', 'interface': 'en3'}}

    module = AnsibleModule(argument_spec={})
    module.params['network'] = 'AIXNetwork'
    module.params['route_path'] = route_path
    network = AIXNetwork(module)
    interfaces = network.get_default_interfaces(route_path)

    assert interfaces == interface



# Generated at 2022-06-13 01:20:27.130477
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    assert AIXNetworkCollector._platform == 'AIX'
    assert AIXNetworkCollector._fact_class == AIXNetwork

# Testing AIXNetwork

# Generated at 2022-06-13 01:20:29.445612
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    collector = AIXNetworkCollector()
    assert collector.platform == 'AIX'
    assert collector.fact_class == AIXNetwork

# Generated at 2022-06-13 01:20:39.936609
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    import os
    import tempfile
    import sys

    class MyModule(object):
        def __init__(self, arg1, arg2):
            self.params = arg1
            self.exit_json = arg2
            self.run_command = self.get_run_command()

        def get_run_command(self):
            def run_command(args, check_rc=True):
                netstat_path = self.get_bin_path('netstat')
                if not netstat_path:
                    return 127, '', 'FAIL: cannot run netstat'

# Generated at 2022-06-13 01:20:43.630801
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    '''
    Unit test for constructor of class AIXNetworkCollector
    '''
    collector = AIXNetworkCollector()
    assert collector.platform == 'AIX'
    assert collector.fact_class == AIXNetwork
    assert collector.fact_class._platform == 'AIX'


# Generated at 2022-06-13 01:20:45.399625
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    obj = AIXNetworkCollector()
    assert obj
    assert obj._fact_class == AIXNetwork
    assert obj._platform == 'AIX'

# Generated at 2022-06-13 01:21:35.113267
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    network_collector_obj = AIXNetworkCollector()
    assert network_collector_obj._platform == 'AIX'
    assert network_collector_obj._fact_class == AIXNetwork


# Generated at 2022-06-13 01:21:42.799990
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():

    test_module = AnsibleModule(
        argument_spec=dict(gather_subset=dict(default=['!all'], type='list')),
        supports_check_mode=True
    )

    ifconfig_path = test_module.get_bin_path('ifconfig', None)
    if not ifconfig_path:
        module.fail_json(msg='ifconfig command not found')

    network_handler = AIXNetwork()

    interfaces, ips = network_handler.get_interfaces_info(ifconfig_path)
    nr_interfaces_before = len(interfaces)

    test_interface = {}
    test_interface['device'] = 'en0'
    test_interface['ipv4'] = []
    test_interface['ipv6'] = []

# Generated at 2022-06-13 01:21:44.541277
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    aix_network = AIXNetworkCollector()
    assert aix_network.get_default_interfaces(None) == (None, None)

# Generated at 2022-06-13 01:21:48.602903
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    from ansible.module_utils.facts.network.aix import AIXNetwork
    aix_net = AIXNetwork()
    default_v4, default_v6 = aix_net.get_default_interfaces(route_path='/usr/sbin/route')
    assert default_v4['interface'] == 'en0'
    assert default_v6['interface'] == 'en0'

# Generated at 2022-06-13 01:21:56.073317
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    module = AnsibleModule(argument_spec={})

    obj = AIXNetwork()
    obj.module = module

    device = 'en0'
    ifconfig_out = '{0}: flags=63<UP,BROADCAST,NOTRAILERS,RUNNING> mtu 1500\n' \
                   '        inet 10.1.1.1 netmask 0xffffff00 broadcast 10.1.1.255\n' \
                   '        inet6 fe80::a8bb:ccff:febb:ddaa%en0 prefixlen 64 scopeid 0x1\n' \
                   '        ether a8:bb:cc:bb:dd:aa\n'.format(device)
    interfaces, ips = obj.get_interfaces_info(ifconfig_path=None, ifconfig_options=ifconfig_out)

# Generated at 2022-06-13 01:22:01.875245
# Unit test for method get_interfaces_info of class AIXNetwork

# Generated at 2022-06-13 01:22:07.175082
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    """
    Run the constructor of class AIXNetworkCollector.
    """
    collector = AIXNetworkCollector()
    assert collector._platform == 'AIX'
    assert collector.get_device() == 'en0'
    assert collector.get_device('en1') == 'en1'
    assert collector.get_device('lo0') == 'lo0'


# Generated at 2022-06-13 01:22:12.326753
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    """
    Constructor GNULinuxNetworkCollector should:
    """
    fact_network_class = AIXNetworkCollector._fact_class
    assert fact_network_class, "missing fact_network_class"
    fact_network_class_instance = fact_network_class(dict(module=None))
    assert fact_network_class_instance, 'missing fact_network_class_instance'
    assert fact_network_class_instance.platform == 'AIX'

# Generated at 2022-06-13 01:22:13.440550
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    """
    Test AIXNetworkCollector
    """
    AIXNetworkCollector()

# Generated at 2022-06-13 01:22:19.409787
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    module = AnsibleModule(
        argument_spec=dict()
    )
    platform_facts = dict()
    network_collector = AIXNetworkCollector(module, platform_facts)
    assert network_collector.platform == 'AIX'
    assert isinstance(network_collector.facts, AIXNetwork)


ANSIBLE_METADATA = {'metadata_version': '1.0',
                    'status': ['preview'],
                    'supported_by': 'network'}


DOCUMENTATION = '''
---
module: aix_network_facts
author: "Jean-Philippe Luiggi (@jplelu)"
short_description: Facts from AIX ifconfig facts
description:
  - Facts from AIX ifconfig
version_added: "2.2"
'''

# Generated at 2022-06-13 01:23:58.308014
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    module = None
    device_name = 'en5'
    netstat_cmd = ['netstat', '-nr']

# Generated at 2022-06-13 01:24:00.536545
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    x = AIXNetworkCollector()
    assert x.__dict__ == {'_fact_class': AIXNetwork, '_platform': 'AIX'}
    assert x._fact_class == AIXNetwork
    assert x._platform == 'AIX'

# Generated at 2022-06-13 01:24:02.136270
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    test_obj = AIXNetworkCollector()
    assert test_obj._fact_class == AIXNetwork
    assert test_obj._platform == 'AIX'

# Generated at 2022-06-13 01:24:08.060632
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    # Create a fake module with its own tmpdir as /etc/ansible/facts/ dir
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=False
    )
    module.tmpdir = '/tmp/ansible'
    module.exit_json = exit_json
    module.run_command = run_command
    module.get_bin_path = get_bin_path

    # Create a file with fake `netstat -nr` output

# Generated at 2022-06-13 01:24:13.122022
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    options = dict(
        module=dict(),
        params=dict()
    )
    module = FakeAnsibleModule(**options)
    fake_net = AIXNetwork(module)
    fake_net.ifconfig_path = '/usr/bin/ifconfig'
    fake_net.netstat_path = './tests/netstat'

    v4, v6 = fake_net.get_default_interfaces('/usr/bin/netstat')

    assert v4['interface'] == 'en0'
    assert v4['gateway'] == '172.16.12.1'
    assert v6['interface'] == 'en0'
    assert v6['gateway'] == 'fe80::21b:77ff:fe49:b7de'


# Generated at 2022-06-13 01:24:15.579105
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    aixnc = AIXNetworkCollector()
    assert aixnc.platform == 'AIX'


# Generated at 2022-06-13 01:24:23.040551
# Unit test for constructor of class AIXNetworkCollector
def test_AIXNetworkCollector():
    ifconfig_path = '/usr/bin/ifconfig'
    aix_net = AIXNetwork(dict(module=dict(get_bin_path=lambda x: ifconfig_path)))
    assert aix_net.fact_subsets['default'] == dict(
        command=ifconfig_path,
        options='-a',
        vars=[
            'all_ipv4_addresses',
            'all_ipv6_addresses',
            'default_ipv4',
            'default_ipv6',
            'interfaces',
            'interface_ipv4',
            'interface_ipv6'
        ]
    )

# Generated at 2022-06-13 01:24:31.973036
# Unit test for method get_default_interfaces of class AIXNetwork
def test_AIXNetwork_get_default_interfaces():
    # mock os.path.exists to avoid iterating through files in /sbin,/bin,/usr/bin,/usr/sbin
    mock_path = Mock(return_value=True)
    with patch('os.path.exists', mock_path):
        # mock module.run_command to simulate return values of commands
        class MockAnsibleModule(object):
            def get_bin_path(self, arg1):
                return arg1
            def run_command(self, arg1):
                if arg1[0] == 'netstat':
                    return 0, """
default            10.255.255.1       UGS        0         0                    en0
default            10.255.255.1       UGS        0         0                    en1
                    """, 0

# Generated at 2022-06-13 01:24:41.217282
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    # input data and expected result
    ifconfig_path = "/usr/bin/ifconfig"
    ifconfig_options = "-a"

# Generated at 2022-06-13 01:24:48.693816
# Unit test for method get_interfaces_info of class AIXNetwork
def test_AIXNetwork_get_interfaces_info():
    from ansible.module_utils.facts.facts import Facts
    from ansible.module_utils.facts.network.aix import AIXNetwork