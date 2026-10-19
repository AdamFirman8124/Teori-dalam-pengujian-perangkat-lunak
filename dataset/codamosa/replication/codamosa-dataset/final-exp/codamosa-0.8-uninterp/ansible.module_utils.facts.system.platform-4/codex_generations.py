

# Generated at 2022-06-13 03:13:09.936406
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    pfc = PlatformFactCollector()
    assert pfc
    assert pfc.name == 'platform'
    assert pfc._fact_ids == set(['system',
                                 'kernel',
                                 'kernel_version',
                                 'machine',
                                 'python_version',
                                 'architecture',
                                 'machine_id'])

# Generated at 2022-06-13 03:13:13.749822
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


# Generated at 2022-06-13 03:13:19.129574
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    platform_facts = {}
    pf = PlatformFactCollector()
    pf.collect(platform_facts=platform_facts)
    assert 'system' in platform_facts
    assert 'kernel' in platform_facts
    assert 'kernel_version' in platform_facts
    assert 'machine' in platform_facts
    assert 'python_version' in platform_facts
    assert 'architecture' in platform_facts
    assert 'machine_id' in platform_facts

# Generated at 2022-06-13 03:13:28.703418
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    """ platform.collect() Method Unit Test """
    # Unit test for platform.collect() method on PlatformFactCollector class
    # This test case is to ensure the contents of the collect method of PlatformFactCollector
    # class.
    # Create a PlatformFactCollector object
    # This is done using the AnsibleModuleHelper
    # Pass the module object and the collect method of PlatformFactCollector object
    # In this test case we test the input parameters to the collect method.
    # A custom module object is used for this so that the module interface is
    # bypassed. This will help in checking the contents of the returned collect

    PlatformModule = ansible_module_create()
    PlatformFactCollectorObj = PlatformFactCollector(PlatformModule)
    PlatformFactCollectorObj.collect()

    # Will create a result dictionary with the keys that are returned by the collect method


# Generated at 2022-06-13 03:13:33.036805
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

# Generated at 2022-06-13 03:13:40.088950
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    facts = PlatformFactCollector().collect()

    assert facts['system'] == platform.system()
    assert facts['kernel'] == platform.release()
    assert facts['kernel_version'] == platform.version()
    assert facts['machine'] == platform.machine()
    assert facts['python_version'] == platform.python_version()
    assert facts['fqdn'] == socket.getfqdn()
    assert facts['hostname'] == platform.node().split('.')[0]
    assert facts['nodename'] == platform.node()
    assert facts['domain'] == '.'.join(facts['fqdn'].split('.')[1:])
    assert facts['architecture'] == platform.machine()
    assert facts['userspace_bits'] == platform.architecture()[0].replace('bit', '')

# Generated at 2022-06-13 03:13:43.372532
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    x = PlatformFactCollector()
    assert x.name == "platform"
    assert x._fact_ids == set(['system',
                               'kernel',
                               'kernel_version',
                               'machine',
                               'python_version',
                               'architecture',
                               'machine_id'])
    assert x._platform_version is None

# Generated at 2022-06-13 03:13:49.955121
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    class _module(object):
        def __init__(self):
            self.params = {}
        def get_bin_path(self, name, required=False):
            if name == 'bootinfo':
                return '/usr/bin/bootinfo'
            elif name == 'getconf':
                return '/usr/bin/getconf'
    collector = PlatformFactCollector()
    result = collector.collect(_module())

# Generated at 2022-06-13 03:13:54.425507
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    p = PlatformFactCollector()
    assert p
    assert p.name == 'platform'
    assert p._fact_ids == {
        'system',
        'kernel',
        'kernel_version',
        'machine',
        'python_version',
        'architecture',
        'machine_id'
    }

# Generated at 2022-06-13 03:13:58.900386
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    # Get PlatformFactCollector instance
    platform_fact_collector = PlatformFactCollector()

    # Check instance of PlatformFactCollector
    assert isinstance(platform_fact_collector, PlatformFactCollector)

    # Check attribute of PlatformFactCollector
    assert hasattr(platform_fact_collector, 'name')
    assert hasattr(platform_fact_collector, '_fact_ids')

# Generated at 2022-06-13 03:14:34.313571
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    platform = PlatformFactCollector()
    assert platform.__class__.__name__ == 'PlatformFactCollector'

# Generated at 2022-06-13 03:14:39.563599
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
                                                     'machine_id'])

# Generated at 2022-06-13 03:14:42.986596
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    __test__ = True
    myCollector = PlatformFactCollector()
    myFactIds = myCollector.get_fact_ids()
    assert myCollector.get_fact_ids() == set(['system',
                                           'kernel',
                                           'kernel_version',
                                           'machine',
                                           'python_version',
                                           'architecture',
                                           'machine_id']),\
                                           "platform - platformFacts.get_fact_ids() == " + str(myFactIds)
    assert myCollector.get_name() == 'platform', "platform - platformFacts.get_name() == " + myCollector.get_name()

# Generated at 2022-06-13 03:14:47.709215
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    platform_fact_collector = PlatformFactCollector()
    assert platform_fact_collector.name == 'platform'
    assert platform_fact_collector.collect()['system'] == platform.system()

# Generated at 2022-06-13 03:14:56.936626
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    # Create instance of the PlatformFactCollector class for testing
    plat_fact_collector = PlatformFactCollector()
    plat_fact_collector.name = 'platform'
    plat_fact_collector._fact_ids = {'system',
                                     'kernel',
                                     'kernel_version',
                                     'machine',
                                     'python_version',
                                     'architecture',
                                     'machine_id'}

    # Make sure that the collect method of the PlatformFactCollector
    # class returns the proper data structure
    facts = plat_fact_collector.collect(collected_facts={})
    assert isinstance(facts, dict)
    assert 'system' in facts
    assert 'kernel' in facts
    assert 'kernel_version' in facts
    assert 'machine' in facts

# Generated at 2022-06-13 03:15:00.330381
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():

    # mock class for module
    class MockModule(object):
        C = None
        params = None
        timeout = 10

        @staticmethod
        def get_bin_path(binary):
            return binary

        @staticmethod
        def run_command(command):
            return 0, '', ''

    # create object
    pfc = PlatformFactCollector()

    # check method collect
    pfc.collect(MockModule())

# Generated at 2022-06-13 03:15:10.097567
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

    # Unit test for collect method of class PlatformFactCollector
    def get_bin_path(self, in_path):
        # Mock/Stub method
        return "/bin/{0}".format(in_path)

    def get_file_content(self, filename):
        # Mock/Stub method
        return True

    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(argument_spec={})
    module.get_bin_path = get_bin_path


# Generated at 2022-06-13 03:15:11.980764
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    pfc = PlatformFactCollector()
    assert pfc.name == 'platform'
    assert 'system' in pfc.collect()

# Generated at 2022-06-13 03:15:23.216079
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():

    class FakeModule:

        def get_bin_path(self, arg):
            return 'getconf'

        def run_command(self, arg):
            return (0, 'bogus output', '')

    class FakeCollector:
        platform = {'machine_id': None, 'machine': 'x86_64'}
        python_version = '2.7.9'
        system = 'Linux'
        kernel = 'Linux'
        kernel_version = '3.13.0'
        nodename = 'bogus.example.com'

    def side_effect(arg):
        class FakeFqdn:
            def split(self, arg):
                return ['bogus', 'example', 'com']
        return FakeFqdn()

    module = FakeModule()

# Generated at 2022-06-13 03:15:30.647780
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    from ansible.module_utils.facts import FactCollector
    module = None
    fact_collector = FactCollector(module)
    platform_facts_collector = fact_collector.collectors['platform']
    platform_facts = platform_facts_collector.collect(module=module)

    assert set(platform_facts.keys()) == set(['system',
                                              'kernel',
                                              'kernel_version',
                                              'machine',
                                              'architecture',
                                              'python_version',
                                              'userspace_bits',
                                              'fqdn',
                                              'hostname',
                                              'nodename',
                                              'domain'])


# Generated at 2022-06-13 03:15:44.307303
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
                                                     'machine_id'])


# Generated at 2022-06-13 03:15:57.079353
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    pfc = PlatformFactCollector()
    assert pfc.name == 'platform'
    assert pfc._fact_ids == set(['system',
                                 'kernel',
                                 'kernel_version',
                                 'machine',
                                 'python_version',
                                 'architecture',
                                 'machine_id'])

# Generated at 2022-06-13 03:15:58.772241
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    # Create simple object
    x = PlatformFactCollector()
    # Call method collect
    x.collect()

# Generated at 2022-06-13 03:16:08.249641
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():

    # Makes an instance of the class PlatformFactCollector without args.
    pfc = PlatformFactCollector()

    # Calls the method collect of PlatformFactCollector.
    platform_facts = pfc.collect()
    assert platform_facts
    assert platform_facts.get('system')
    assert platform_facts.get('kernel')
    assert platform_facts.get('kernel_version')
    assert platform_facts.get('machine')
    assert platform_facts.get('python_version')
    assert platform_facts.get('userspace_bits')
    assert platform_facts.get('architecture')
    assert platform_facts.get('userspace_architecture')

    # Checks the value of `userspace_architecture` in case of 64-bit arch.

# Generated at 2022-06-13 03:16:13.829306
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    x = PlatformFactCollector()
    assert x.name == 'platform'
    assert x._fact_ids == set(['system',
                               'kernel',
                               'kernel_version',
                               'machine',
                               'python_version',
                               'architecture',
                               'machine_id'])

# Generated at 2022-06-13 03:16:22.594126
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts.collectors.platform import PlatformFactCollector
    from ansible.module_utils.facts.utils import compare_dict
    import platform

    Collector._fact_collectors = []
    Collector.collectors = []
    collector = PlatformFactCollector(None)
    facts_d = collector.collect()
    assert facts_d['system'] == platform.system()
    assert facts_d['kernel'] == platform.release()
    assert facts_d['kernel_version'] == platform.version()
    assert facts_d['machine'] == platform.machine()
    assert facts_d['python_version'] == platform.python_version()

# Generated at 2022-06-13 03:16:25.522986
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    pfc = PlatformFactCollector()

    assert pfc.name == 'platform'
    assert pfc._fact_ids == set(['system',
                     'kernel',
                     'kernel_version',
                     'machine',
                     'python_version',
                     'architecture',
                     'machine_id'])

# Generated at 2022-06-13 03:16:27.747378
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    from ansible.module_utils.facts import collector
    pfc = collector.get_collector('platform')
    assert isinstance(pfc, PlatformFactCollector)

# Generated at 2022-06-13 03:16:30.640792
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    ff = PlatformFactCollector()
    assert ff.name == 'platform'
    assert set(ff._fact_ids) == { 'system',
                                  'kernel',
                                  'kernel_version',
                                  'machine',
                                  'python_version',
                                  'architecture',
                                  'machine_id' }

# Generated at 2022-06-13 03:16:34.663231
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    platform_fact_collector_obj = PlatformFactCollector()
    assert platform_fact_collector_obj
    assert platform_fact_collector_obj.name == 'platform'
    assert platform_fact_collector_obj._fact_ids == {'system', 'kernel', 'kernel_version', 'machine', 'python_version', 'architecture', 'machine_id'}


# Generated at 2022-06-13 03:17:15.823457
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    PlatformFactCollector()

# Generated at 2022-06-13 03:17:23.476497
# Unit test for method collect of class PlatformFactCollector

# Generated at 2022-06-13 03:17:26.313567
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    collector = PlatformFactCollector()

    # checks for class attributes
    assert collector.name == 'platform'
    assert collector._fact_ids == set(['system',
                                       'kernel',
                                       'kernel_version',
                                       'machine',
                                       'python_version',
                                       'architecture',
                                       'machine_id'])

# Generated at 2022-06-13 03:17:28.428072
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    platform_fact_collector = PlatformFactCollector()
    assert platform_fact_collector.name == 'platform'
    assert set(platform_fact_collector._fact_ids) == set(['system', 'kernel', 'kernel_version', 'machine', 'python_version', 'architecture', 'machine_id'])

# Generated at 2022-06-13 03:17:30.678444
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    assert PlatformFactCollector.name == "platform"
    assert PlatformFactCollector._fact_ids == set(['system',
                                                   'kernel',
                                                   'kernel_version',
                                                   'machine',
                                                   'python_version',
                                                   'architecture',
                                                   'machine_id'])


# Generated at 2022-06-13 03:17:36.988814
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    fact_collector = PlatformFactCollector()
    fact_collector._name = 'platform'
    fact_collector._fact_ids = set(['system',
                                    'kernel',
                                    'kernel_version',
                                    'machine',
                                    'python_version',
                                    'architecture',
                                    'machine_id'])
    
    assert fact_collector.name == 'platform'
    assert fact_collector._fact_ids == set(['system',
                                            'kernel',
                                            'kernel_version',
                                            'machine',
                                            'python_version',
                                            'architecture',
                                            'machine_id'])

# Generated at 2022-06-13 03:17:37.985972
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    plat_collector = PlatformFactCollector()
    assert plat_collector.name == 'platform'

# Generated at 2022-06-13 03:17:40.251942
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    assert PlatformFactCollector().name == 'platform'
    assert sorted(PlatformFactCollector()._fact_ids) == sorted([
        'system',
        'kernel',
        'kernel_version',
        'machine',
        'python_version',
        'architecture',
        'machine_id',
    ])

# Generated at 2022-06-13 03:17:42.881119
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    platform_collector = PlatformFactCollector()
    assert platform_collector.name == 'platform'
    assert platform_collector._fact_ids == set(['system',
                                                'kernel',
                                                'kernel_version',
                                                'machine',
                                                'python_version',
                                                'architecture',
                                                'machine_id'])


# Generated at 2022-06-13 03:17:46.791270
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():

    platform_facts = PlatformFactCollector()
    data = platform_facts.collect()
    assert data["system"] == "Linux"
    assert not data["machine_id"]



# Generated at 2022-06-13 03:19:09.989389
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    p = PlatformFactCollector()

    assert p.name == 'platform'
    assert p._fact_ids == set(['system',
                               'kernel',
                               'kernel_version',
                               'machine',
                               'python_version',
                               'machine_id'])



# Generated at 2022-06-13 03:19:11.548680
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    x = PlatformFactCollector()
    assert x
    assert x.name == 'platform'
    assert 'system' in x._fact_ids


# Generated at 2022-06-13 03:19:13.703695
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    p = PlatformFactCollector()
    result = p.collect()

    assert 'system' in result
    assert 'kernel' in result
    assert 'kernel_version' in result
    assert 'machine' in result
    assert 'python_version' in result
    assert 'architecture' in result

# Generated at 2022-06-13 03:19:19.704555
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    platform_collector = PlatformFactCollector()

    assert platform_collector.name == 'platform'
    assert platform_collector._fact_ids == set(['system',
                                                'kernel',
                                                'kernel_version',
                                                'machine',
                                                'python_version',
                                                'architecture',
                                                'machine_id'])

# Generated at 2022-06-13 03:19:26.562402
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():

    my_platform_collector = PlatformFactCollector()
    # Test with no parameter
    my_facts = my_platform_collector.collect()
    assert 'system' in my_facts
    # Test with empty params
    my_facts = my_platform_collector.collect(collected_facts={})
    assert 'system' in my_facts
    # Test with random params
    my_facts = my_platform_collector.collect(module='toto', collected_facts={'toto': 'toto'})
    assert 'system' in my_facts

# Generated at 2022-06-13 03:19:30.491866
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    p = PlatformFactCollector()
    # ensure the constructor doesn't fail
    assert p is not None
    assert p.name == 'platform'
    assert p._fact_ids == {'system', 'kernel', 'kernel_version',
                           'machine', 'python_version',
                           'architecture', 'machine_id'}

# Generated at 2022-06-13 03:19:40.947009
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    assert PlatformFactCollector.name == 'platform'
    assert len(PlatformFactCollector._fact_ids) == 9
    assert 'system' in PlatformFactCollector._fact_ids
    assert 'kernel' in PlatformFactCollector._fact_ids
    assert 'kernel_version' in PlatformFactCollector._fact_ids
    assert 'machine' in PlatformFactCollector._fact_ids
    assert 'python_version' in PlatformFactCollector._fact_ids
    assert 'architecture' in PlatformFactCollector._fact_ids
    assert 'machine_id' in PlatformFactCollector._fact_ids
    assert 'userspace_bits' in PlatformFactCollector._fact_ids
    assert 'fqdn' in PlatformFactCollector._fact_ids
    assert 'hostname' in PlatformFactCollector._fact_ids

# Generated at 2022-06-13 03:19:45.788984
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    pfc = PlatformFactCollector()
    assert pfc.name == 'platform'
    assert pfc._fact_ids == set(['system',
                                 'kernel',
                                 'kernel_version',
                                 'machine',
                                 'python_version',
                                 'architecture',
                                 'machine_id'])


# Generated at 2022-06-13 03:19:55.506611
# Unit test for method collect of class PlatformFactCollector
def test_PlatformFactCollector_collect():
    """Test method collect of class PlatformFactCollector"""
    # Patch module loader so that platform.system() returns 'Linux'
    import ansible.module_utils.facts.collectors.platform.platform as patched_platform
    patched_platform.system = lambda: 'Linux'

    # Patch module loader so that platform.release() returns '2.6.18-371.3.1.el5'
    patched_platform.release = lambda: '2.6.18-371.3.1.el5'

    platform_fact_collector = PlatformFactCollector()
    platform_facts = platform_fact_collector.collect()
    assert set(platform_facts.keys()) == set(['system', 'kernel', 'kernel_version',
                                              'machine', 'architecture', 'python_version',
                                              'machine_id'])

# Generated at 2022-06-13 03:20:00.722135
# Unit test for constructor of class PlatformFactCollector
def test_PlatformFactCollector():
    fc = PlatformFactCollector()
    assert fc.name == 'platform'
    assert fc._fact_ids == set(['system',
                                'kernel',
                                'kernel_version',
                                'machine',
                                'python_version',
                                'architecture',
                                'machine_id'])