

# Generated at 2022-06-13 03:13:08.777162
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    platform_fact_collector = PlatformFactCollector()
    assert platform_fact_collector.name == "platform"
    assert platform_fact_collector._fact_ids == set(['system',
                                                      'kernel',
                                                      'kernel_version',
                                                      'machine',
                                                      'python_version',
                                                      'architecture',
                                                      'machine_id'])

# Unit test

# Generated at 2022-06-13 03:13:22.152680
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    pfc = PlatformFactCollector()
    assert pfc.name == 'platform'
    assert set(pfc._fact_ids) == set(['system',
                                      'kernel',
                                      'kernel_version',
                                      'machine',
                                      'python_version',
                                      'architecture',
                                      'machine_id'])


# Generated at 2022-06-13 03:13:32.029863
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    pfc = PlatformFactCollector()
    assert pfc is not None


# Generated at 2022-06-13 03:13:39.208788
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():

    import platform

    import pytest

    import ansible.module_utils.facts.collector.platform

    platform_collector = ansible.module_utils.facts.collector.platform.PlatformFactCollector()

    # if os.name == 'posix':

    platform_facts_result = {
        'architecture':  platform.machine(),
        'domain': '',
        'fqdn': 'localhost',
        'hostname': 'localhost',
        'kernel': platform.release(),
        'kernel_version': platform.version(),
        'machine': platform.machine(),
        'nodename': 'localhost',
        'python_version': platform.python_version(),
        'system': platform.system()
    }

    assert platform_collector.collect() == platform_facts_result

# Generated at 2022-06-13 03:13:45.654716
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    p = PlatformFactCollector()
    platform_facts = p.collect()

    assert platform_facts['system'] == platform.system()
    assert platform_facts['kernel'] == platform.release()
    assert platform_facts['kernel_version'] == platform.version()
    assert platform_facts['machine'] == platform.machine()
    assert platform_facts['python_version'] == platform.python_version()
    assert platform_facts['fqdn'] == socket.getfqdn()
    assert platform_facts['domain'] == '.'.join(platform_facts['fqdn'].split('.')[1:])

# Generated at 2022-06-13 03:13:51.750435
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    pfc = PlatformFactCollector()
    assert (pfc.name == 'platform')
    assert (pfc._fact_ids == set(['system',
                                  'kernel',
                                  'kernel_version',
                                  'machine',
                                  'python_version',
                                  'architecture',
                                  'machine_id']))

# Generated at 2022-06-13 03:14:00.309696
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    import platform
    from ansible.module_utils.facts.collector.platform import PlatformFactCollector
    from ansible.module_utils.facts.utils import set_module_args
    from ansible.module_utils.facts.utils import AnsibleModule
    from ansible.module_utils.facts.utils import ModuleDeprecationWarning
    import warnings

    warnings.simplefilter('error', ModuleDeprecationWarning)
    set_module_args({})
    platform_facts_collector_ins = PlatformFactCollector()
    platform_facts = platform_facts_collector_ins.collect()
    assert type(platform_facts) is dict
    assert platform_facts['system'] == platform.system()
    assert platform_facts['kernel'] == platform.release()
    assert platform_facts['kernel_version'] == platform.version()
    assert platform

# Generated at 2022-06-13 03:14:09.395733
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    # Skip on Windows, which does not have platform.machine()
    # and also does not have the 'architecture' key.
    if platform.system() == 'Windows':
        pytest.skip("Facts not implemented on Windows")
    facts = {}
    fact_collector = PlatformFactCollector()
    fact_collector.collect(collected_facts=facts)
    assert 'system' in facts
    assert facts['system'] == platform.system()
    assert 'kernel' in facts
    assert facts['kernel'] == platform.release()
    assert 'kernel_version' in facts
    assert facts['kernel_version'] == platform.version()
    assert 'machine' in facts
    assert facts['machine'] == platform.machine()
    assert 'python_version' in facts
    assert facts['python_version'] == platform.python_version()


# Generated at 2022-06-13 03:14:11.568453
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    platform = PlatformFactCollector()
    fact_data = platform.collect()

    assert 'system' in fact_data
    assert 'kernel' in fact_data
    assert 'kernel_version' in fact_data
    assert 'machine' in fact_data
    assert 'python_version' in fact_data
    assert 'architecture' in fact_data
    assert 'userspace_bits' in fact_data
    assert 'userspace_architecture' in fact_data

# Generated at 2022-06-13 03:14:16.828001
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    pfc = PlatformFactCollector()
    assert pfc.name == 'platform'
    assert pfc._fact_ids == set([
            'system',
            'kernel',
            'kernel_version',
            'machine',
            'python_version',
            'architecture',
            'machine_id',
        ])

# Generated at 2022-06-13 03:15:15.330301
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    import platform
    import sys

    platform_facts = {
        'architecture': platform.machine(),
        'fqdn': 'host1.example.com',
        'domain': 'example.com',
        'hostname': 'host1',
        'nodename': 'host1.example.com',
        'kernel': platform.release(),
        'kernel_version': platform.version(),
        'machine': platform.machine(),
        'python_version': sys.version_info,
        'system': platform.system()
    }
    module = None
    collected_facts = None
    pfc = PlatformFactCollector()
    platform_facts_collected = pfc.collect(module, collected_facts)
    assert platform_facts == platform_facts_collected


# Generated at 2022-06-13 03:15:20.771127
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    platform_collector = PlatformFactCollector()
    assert platform_collector
    assert platform_collector.name == 'platform'
    assert platform_collector._fact_ids == set(['system',
                                                'kernel',
                                                'kernel_version',
                                                'machine',
                                                'python_version',
                                                'architecture',
                                                'machine_id'])

# Generated at 2022-06-13 03:15:24.768146
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    obj = PlatformFactCollector()
    assert obj.name == 'platform'
    assert obj._fact_ids == set(['system',
                                 'kernel',
                                 'kernel_version',
                                 'machine',
                                 'python_version',
                                 'architecture',
                                 'machine_id'])

# Generated at 2022-06-13 03:15:34.926389
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    module = get_module_mock()
    module.params = {'gather_subset': ['!all', '!min']}
    platform_collector = PlatformFactCollector(module)
    collected_facts = platform_collector.collect(module=module, collected_facts=None)

    assert 'system' in collected_facts
    assert 'kernel' in collected_facts
    assert 'kernel_version' in collected_facts
    assert 'machine' in collected_facts
    assert 'architecture' in collected_facts
    assert 'python_version' in collected_facts
    assert 'fqdn' in collected_facts
    assert 'hostname' in collected_facts
    assert 'nodename' in collected_facts
    assert 'domain' in collected_facts
    assert 'userspace_bits' in collected_facts

# Generated at 2022-06-13 03:15:35.415154
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    pass

# Generated at 2022-06-13 03:15:36.463149
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    x = PlatformFactCollector()
    assert x
    assert x.name == 'platform'

# Generated at 2022-06-13 03:15:46.824077
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    '''
    Tests the constructor of the PlatformFactCollector class.
    '''

    platform_collector = PlatformFactCollector()

    assert platform_collector.name == 'platform', "Expected 'platform', got: " + platform_collector.name

    assert 'system' in platform_collector.collect().keys(), "Expected 'system' in keys of platform_collector.collect()"

    assert 'kernel' in platform_collector.collect().keys(), "Expected 'kernel' in keys of platform_collector.collect()"

    assert 'kernel_version' in platform_collector.collect().keys(), "Expected 'kernel_version' in keys of platform_collector.collect()"

    assert 'machine' in platform_collector.collect().keys(), "Expected 'machine' in keys of platform_collector.collect()"

   

# Generated at 2022-06-13 03:15:49.183618
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    x = PlatformFactCollector()
    assert x.name == 'platform'
    x._collect()

# Generated at 2022-06-13 03:15:57.916082
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    # Setup
    test_platform = PlatformFactCollector()
    test_system = platform.system()
    test_kernel = platform.release()
    test_kernel_version = platform.version()
    test_machine = platform.machine()
    test_python_version = platform.python_version()
    test_fqdn = socket.getfqdn()
    test_hostname = platform.node().split('.')[0]
    test_nodename = platform.node()
    test_domain = '.'.join(test_fqdn.split('.')[1:])
    test_userspace_bits = platform.architecture()[0].replace('bit', '')
    test_architecture = test_machine

# Generated at 2022-06-13 03:16:05.543887
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    platform_fact_collector = PlatformFactCollector()
    assert platform_fact_collector.name == 'platform'
    assert platform_fact_collector._fact_ids == set(['system',
                                                     'kernel',
                                                     'kernel_version',
                                                     'machine',
                                                     'python_version',
                                                     'architecture',
                                                     'machine_id',
                                                     'fqdn',
                                                     'domain',
                                                     'hostname',
                                                     'nodename',
                                                     'userspace_bits',
                                                     'userspace_architecture'])

# Generated at 2022-06-13 03:17:32.376703
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    class MockModule():
        def __init__(self, params=None):
            self.params = params or {}

        def get_bin_path(self, path):
            return '/bin/getconf'

        def run_command(self, args):
            if args == ['/bin/getconf', 'MACHINE_ARCHITECTURE']:
                return (0, 'ppc64', None)
            elif args == ['/bin/bootinfo', '-p']:
                return (0, 'ppc64', None)
            return (0, '', None)

    platform_facts = PlatformFactCollector()
    collected_facts = platform_facts.collect(MockModule())

    assert platform_facts.system == 'AIX'
    assert platform_facts.kernel == '41'
    assert platform_facts.kernel_version

# Generated at 2022-06-13 03:17:33.312130
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    platform = PlatformFactCollector()
    assert platform.collect() is not None

# Generated at 2022-06-13 03:17:36.044647
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    platform_facts = PlatformFactCollector()
    assert platform_facts.name == 'platform'
    assert platform_facts._fact_ids == set(['system', 'kernel', 'kernel_version', 'machine', 'python_version', 'architecture', 'machine_id'])

# Generated at 2022-06-13 03:17:36.620312
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    PlatformFactCollector()


# Generated at 2022-06-13 03:17:37.170860
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    PlatformFactCollector.collect()

# Generated at 2022-06-13 03:17:37.768732
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    PlatformFactCollector.collect()

# Generated at 2022-06-13 03:17:39.649775
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    x = PlatformFactCollector()
    assert x.name == 'platform'
    assert x._fact_ids == set(['system', 'kernel', 'kernel_version', 'machine',
                               'python_version', 'architecture', 'machine_id'])

# Generated at 2022-06-13 03:17:44.009542
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    pfc = PlatformFactCollector()
    assert pfc.name == 'platform'
    assert platform.system() in pfc.collect()['system']
    assert pfc.collect()['python_version'] == platform.python_version()
    assert pfc.collect()['machine'] == platform.machine()
    assert pfc.collect()['fqdn'] == pfc.collect()['nodename']

# Generated at 2022-06-13 03:17:49.069149
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
  platform_facts = {}
  platform_facts['system'] = platform.system()
  platform_facts['kernel'] = platform.release()
  platform_facts['kernel_version'] = platform.version()
  platform_facts['machine'] = platform.machine()
  print(json.dumps(platform_facts,indent=2))

# Generated at 2022-06-13 03:17:59.746250
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    def get_fact_data():
        return {'fqdn': 'test_fqdn',
                'hostname': 'test_hostname',
                'nodename': 'test_nodename',
                'domain': 'test_domain',
                'kernel': 'test_kernel',
                'kernel_version': 'test_kernel_version',
                'machine': 'test_machine',
                'architecture': 'test_architecture',
                'system': 'test_system'
                }

    module = MagicMock()
    # defining a class variable to mock method get_bin_path of module
    module.get_bin_path.return_value = "getconf"
    module.run_command.return_value = 0, 'x86_64', ''
    module.params = {}
    # defining a class variable

# Generated at 2022-06-13 03:20:35.822669
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    p = PlatformFactCollector()
    assert isinstance(p, PlatformFactCollector)


# Generated at 2022-06-13 03:20:37.593813
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    x = PlatformFactCollector()
    assert x.name == 'platform'
    assert isinstance(x.collect(), dict)

# Generated at 2022-06-13 03:20:41.213561
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    assert PlatformFactCollector().name == 'platform'
    assert PlatformFactCollector()._fact_ids == set(['system',
                                                     'kernel',
                                                     'kernel_version',
                                                     'machine',
                                                     'python_version',
                                                     'architecture',
                                                     'machine_id'])

# Generated at 2022-06-13 03:20:44.861690
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():

    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts.collectors import get_collector_instance

    # Create a Collector object
    collector = get_collector_instance(Collector)

    # Make sure the collector object is an instance of BaseFactCollector
    assert isinstance(collector, BaseFactCollector)

# Generated at 2022-06-13 03:20:47.179049
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    platform_facts = PlatformFactCollector().collect()
    assert isinstance(platform_facts, dict)
    assert isinstance(list(platform_facts.keys()), list)
    assert isinstance(list(platform_facts.values()), list)

# Generated at 2022-06-13 03:20:51.139421
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    assert PlatformFactCollector.name == 'platform'
    assert PlatformFactCollector._fact_ids == set(['system', 'kernel', 'kernel_version',
                                                   'machine', 'python_version', 'architecture',
                                                   'machine_id'])

# Generated at 2022-06-13 03:20:57.423742
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    from ansible.module_utils.facts.collector import FactCollector
    from ansible.module_utils.facts.collector import FactCache
    from ansible.module_utils.facts.collector import BaseFactCollector

    fact_collector = FactCollector()

    with FactCache() as fact_cache:
        fact_collector.populate_facts(fact_cache=fact_cache)

    assert isinstance(fact_collector._collectors[0], PlatformFactCollector)
    assert issubclass(PlatformFactCollector, BaseFactCollector)

# Test collect method of class PlatformFactCollector

# Generated at 2022-06-13 03:20:58.932596
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    platform_facts = PlatformFactCollector().collect()
    assert set(platform_facts.keys()) == PlatformFactCollector._fact_ids

# Generated at 2022-06-13 03:21:01.948933
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    p = PlatformFactCollector()
    assert p.name == 'platform'
    assert p._fact_ids == set(['system',
                               'kernel',
                               'kernel_version',
                               'machine',
                               'python_version',
                               'architecture',
                               'machine_id'])

# Generated at 2022-06-13 03:21:07.342255
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():

    platform = PlatformFactCollector()

    # Set the expected name of the collector
    expected_name = 'platform'

    assert platform.name == expected_name

    # Set the expected set of fact ids collected by the collector
    expected_fact_ids = set(['system',
                             'kernel',
                             'kernel_version',
                             'machine',
                             'python_version',
                             'architecture',
                             'machine_id'])

    assert platform._fact_ids == expected_fact_ids

    # Set the expected set of additional dependency fact names
    # collected by the collector
    expected_additional_dependency_names = set()

    assert platform._additional_dependency_names == expected_additional_dependency_names