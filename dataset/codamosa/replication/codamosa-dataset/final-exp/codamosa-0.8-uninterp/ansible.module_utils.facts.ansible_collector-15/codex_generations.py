

# Generated at 2022-06-13 00:09:57.980699
# Unit test for function get_ansible_collector
def test_get_ansible_collector():

    # A bunch of collect classes that do nothing
    class ClassA(collector.BaseFactCollector):
        name = 'classa'

    class ClassB(collector.BaseFactCollector):
        name = 'classb'

    class ClassC(collector.BaseFactCollector):
        name = 'classc'

    all_collector_classes = [ClassA, ClassB, ClassC]

    gather_subset = ['all', 'network']
    gather_timeout = None
    minimal_gather_subset = frozenset([])


# Generated at 2022-06-13 00:10:04.965237
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():

    from ansible.module_utils.facts import cached, collector
    from ansible.module_utils.facts.namespace import PrefixFactNamespace

    class FakeCollector(collector.BaseFactCollector):

        def __init__(self):
            super(FakeCollector, self).__init__()

        def collect(self, module=None, collected_facts=None):
            return {'fake_fact': 'fake_value'}

    fake_collector = FakeCollector()
    fact_collector = \
        AnsibleFactCollector(collectors=[fake_collector],
                             namespace=PrefixFactNamespace(prefix='ansible_'))

    collected_facts = fact_collector.collect()

    assert collected_facts == {'ansible_fake_fact': 'fake_value'}


# Generated at 2022-06-13 00:10:14.263220
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    from ansible.module_utils.facts import default
    from ansible.module_utils.facts import cache
    from ansible.module_utils.facts.namespace import BaseFactNamespace
    from ansible.module_utils.facts.namespace import PrefixFactNamespace

    import platform
    import json

    class TestCollector(object):

        name = 'test'

        def collect(self, module=None, collected_facts=None):
            if module:
                return {'test': module.params}
            else:
                return {'test': None}

    all_collector_classes = [TestCollector]
    fact_collector = get_ansible_collector(all_collector_classes, namespace=None)


# Generated at 2022-06-13 00:10:27.398704
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    # mock a module
    module = collector.AnsibleModuleMock()

    c1 = AnsibleFactCollector(collectors=[], namespace=None)
    # collected_facts is the dict holding collected facts.
    # For each fact, the key is the name of the fact and the
    # value is the value of the fact.
    collected_facts = {'fact1': 'value1',
                       'fact2': 'value2',
                       'fact3': 'value3'}
    facts_dict = c1.collect(module, collected_facts)
    assert facts_dict == {'ansible_facts': {'fact1': 'value1',
                                            'fact2': 'value2',
                                            'fact3': 'value3'}}


# Generated at 2022-06-13 00:10:36.052248
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():

    # Setup a dummy AnsibleFactCollector
    collectors = []
    class DummyCollector1(collector.BaseFactCollector):
        def collect(self, module=None, collected_facts=None):
            return {'test_fact': 'a'}
    class DummyCollector2(collector.BaseFactCollector):
        def collect(self, module=None, collected_facts=None):
            return {'test_fact': 'b'}
    class DummyCollector3(collector.BaseFactCollector):
        def collect(self, module=None, collected_facts=None):
            return {'test_fact': 'c'}
    collectors.append(DummyCollector1())
    collectors.append(DummyCollector2())
    collectors.append(DummyCollector3())

# Generated at 2022-06-13 00:10:48.681105
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    import ansible.module_utils.facts.collector
    import ansible.module_utils.facts.cache
    import ansible.module_utils.facts.namespace
    import ansible.module_utils.facts.timeout

    gather_subsets = ['all', '!network', 'network']

    namespace_specifiers = [
        {'namespace': None},
        {'namespace': ansible.module_utils.facts.namespace.PrefixFactNamespace(prefix='ansible_')}
    ]

    for gather_subset in gather_subsets:
        for specifier in namespace_specifiers:
            namespace = specifier['namespace']

# Generated at 2022-06-13 00:10:58.498225
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    fact_dict = {
        'true_facts': {'facts': True},
        'false_facts': {'facts': False},
        'ansible_facts': {'facts': 42}
    }

    class CollectedFactsClass(object):
        def __init__(self, fact_dict=None):
            self.fact_dict = fact_dict or {}

        def get(self, key, default=None):
            return self.fact_dict.get(key, default)

    class CollectorFact(object):
        collect_method_call_result = None

        def collect(self, module=None, collected_facts=None):
            return self.collect_method_call_result

    filter_spec = '*'

    not_collected_facts = {'not_collected': True}

    collected_facts = Collected

# Generated at 2022-06-13 00:11:07.819155
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    import ansible.module_utils.facts.platform.linux
    import ansible.module_utils.facts.hardware
    import ansible.module_utils.facts.network
    import ansible.module_utils.facts.system
    from ansible.module_utils.facts.namespace import PrefixFactNamespace

    collector_classes = [ansible.module_utils.facts.network.NetworkCollector,
                         ansible.module_utils.facts.hardware.HardwareCollector,
                         ansible.module_utils.facts.platform.linux.LinuxCollector,
                         ansible.module_utils.facts.system.SystemCollector]


# Generated at 2022-06-13 00:11:19.374582
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    assert len(get_ansible_collector(all_collector_classes=[],
                                     namespace=None,
                                     filter_spec=None,
                                     gather_subset=['!all', '!facter', '!ohai'],
                                     gather_timeout=None,
                                     minimal_gather_subset=None).collectors) == 0

    assert len(get_ansible_collector(all_collector_classes=[],
                                     namespace=None,
                                     filter_spec=None,
                                     gather_subset=[],
                                     gather_timeout=None,
                                     minimal_gather_subset=None).collectors) == 0


# Generated at 2022-06-13 00:11:19.921350
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    pass

# Generated at 2022-06-13 00:11:31.802263
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    # test with no filter_spec
    collector_1 = collector.BaseFactCollector()
    collector_2 = collector.BaseFactCollector()
    collector_3 = collector.BaseFactCollector()
    collector_4 = collector.BaseFactCollector()

    fact_collector = AnsibleFactCollector(collectors=[collector_1, collector_2])
    fact_collector.collect()

    fact_collector = AnsibleFactCollector(collectors=[collector_3, collector_4])
    fact_collector.collect()

    # test with filter_spec
    collector_1 = collector.BaseFactCollector()
    collector_2 = collector.BaseFactCollector()
    collector_3 = collector.BaseFactCollector()
    collector_4 = collector.BaseFactCollector()

    fact_collector = AnsibleFactCollect

# Generated at 2022-06-13 00:11:42.811141
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():

    collector_fact_dict = {'a': '1',
                           'b': '2',
                           'ansible_c': '3',
                           'd': '4'}

    def _collect(module=None, collected_facts=None):
        return collector_fact_dict

    class TestCollector(object):

        def __init__(self, namespace=None):
            self.name = 'test_collector'
            self.namespace = namespace

        def collect(self, module=None, collected_facts=None):
            return _collect(module=module, collected_facts=collected_facts)

    # Test:
    # 1. No filter_spec provided
    # 2. No namespace provided

    fact_collector = \
        AnsibleFactCollector(collectors=[TestCollector()])



# Generated at 2022-06-13 00:11:54.598184
# Unit test for function get_ansible_collector
def test_get_ansible_collector():

    from ansible.module_utils.facts import cache
    from ansible.module_utils.facts import network
    from ansible.module_utils.facts import namespace

    # This is a list of all the _fact_ids we may have
    all_collector_classes = [cache.CacheFactCollector,
                             network.NetworkFactCollector]

    # Initialize the namespace with a prefix
    ns = namespace.PrefixFactNamespace(prefix='ansible_')

    # Initialize the collector with a namespace, a filter_spec, a gather_subset,
    # the gather_timeout, and the minimal_gather_subset.

# Generated at 2022-06-13 00:12:03.744848
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    # mock up FactCollector with a collect() method
    class MockFactCollector(collector.BaseFactCollector):
        def collect(self, module=None, collected_facts=None):
            return {"mock_fact": "yes"}

    # make an AnsibleFactCollector with a mock FactCollector
    mock_collector = MockFactCollector()
    fact_collector = AnsibleFactCollector(collectors=[mock_collector])

    # collect ansible_facts
    ansible_facts = fact_collector.collect()

    # expect mock_fact to be included in the ansible facts
    assert "ansible_facts" in ansible_facts
    assert "mock_fact" in ansible_facts["ansible_facts"]

# Generated at 2022-06-13 00:12:14.339443
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    from ansible.module_utils.facts.collectors import all_collector_classes
    fact_collector = get_ansible_collector(all_collector_classes, gather_subset=['all'])
    facts_dict = fact_collector.collect()
    assert len(facts_dict) > 1
    # We should have a fact that lists what gather_subsets were used
    assert 'ansible_gather_subset' in facts_dict
    assert facts_dict['ansible_gather_subset'] == fact_collector.collectors[-1].gather_subset
    assert facts_dict['ansible_gather_subset'] == ['all']
    assert 'ansible_module_setup' in facts_dict
    assert facts_dict['ansible_module_setup'] is True

# Generated at 2022-06-13 00:12:26.954140
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():

    class FakeCollectorClass(collector.BaseFactCollector):
        def collect_with_namespace(self, module=None, collected_facts=None):
            return {'fake_key': 'fake_value'}

    class FakeCollectorClassNoFake(collector.BaseFactCollector):
        def collect_with_namespace(self, module=None, collected_facts=None):
            return {}

    # case 1 test filter_spec
    # facts_dict[fake_key] has value which contains substring('fake')
    # filter_spec = ['fake', 'fake1']
    collector_class_object = FakeCollectorClass()
    collector_class_object_no_fake = FakeCollectorClassNoFake()

# Generated at 2022-06-13 00:12:38.319102
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    '''
    Test the public get_ansible_collector function

    This test asserts against the following:
      - default collector_classes are returned when gather_subset is not specified
      - collector_classes are returned based on gather_subset
      - a CollectorMetaDataCollector is added to the list of collector_classes
      - an AnsibleFactCollector is returned.
    '''
    from ansible.module_utils.facts.collector import all_collector_classes

    gather_subset = ['all']
    fact_collector = get_ansible_collector(all_collector_classes, gather_subset=gather_subset)
    assert isinstance(fact_collector, AnsibleFactCollector)
    assert len(fact_collector.collectors) == len(gather_subset) + 1

# Generated at 2022-06-13 00:12:46.572896
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    ''' Testing method collect of AnsibleFactCollector class.'''

    # Testing when filter_spec is None and collectors
    # are initialized with empty list
    ansible_fact_collector_obj = AnsibleFactCollector(collectors=[])
    fact_collector_result = ansible_fact_collector_obj.collect()
    assert len(fact_collector_result) == 0

    # Testing when filter_spec is None and collectors
    # are initialized with empty dict
    ansible_fact_collector_obj = AnsibleFactCollector(collectors={})
    collected_facts = {'test': 'ansible'}
    fact_collector_result = ansible_fact_collector_obj.collect(collected_facts=collected_facts)
    assert len(fact_collector_result) == 0

    # Testing when

# Generated at 2022-06-13 00:12:58.988703
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    # This is a pretty funky class, so it's challenging to test.  We want to:
    # 1)  Make sure the module runs
    # 2)  Make sure it returns the results of the module run.

    test_collector = collector.BaseFactCollector()
    class AnsibleFactCollectorTestModule(object):
        results = {'ansible_facts': {'some_fact': 'foo'}}
        def run_command(self, *args, **kwargs):
            return 'some_cmd', 'some_rc'

    ansible_fact_collector = \
        AnsibleFactCollector(collectors=[test_collector])

    assert ansible_fact_collector.collect(AnsibleFactCollectorTestModule()) == {'some_fact': 'foo'}

# Generated at 2022-06-13 00:13:10.988347
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    import sys
    import io

    # Fake out the sys.stderr inside any exceptions raised by collect_with_namespace()
    # so that we can check the stderr output
    saved_sys_stderr = sys.stderr
    output = io.StringIO()
    sys.stderr = output

    class Collector1(collector.BaseFactCollector):
        name = 'collector1'
        _fact_ids = set()

        def collect(self, module=None, collected_facts=None):
            return {'collector1_fact1': 'collector1_fact_value'}

    class Collector2(collector.BaseFactCollector):
        name = 'collector2'
        _fact_ids = set()

        def collect(self, module=None, collected_facts=None):
            return

# Generated at 2022-06-13 00:13:22.584631
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():

    from ansible.module_utils.facts.core.distribution import DistributionFactCollector

    dist = DistributionFactCollector(namespace='distribution')
    collectors = [dist]
    fact_collector = \
            AnsibleFactCollector(collectors=collectors,
                                 filter_spec=None,
                                 namespace=None)

    facts = fact_collector.collect()
    assert(facts['distribution'] == {})

# Generated at 2022-06-13 00:13:29.148896
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():

    def fake_collector_collect(foo, bar):
        return {'a': 1}

    class FakeCollector(object):
        def collect(self, foo, bar):
            fake_collector_collect(foo, bar)

    class FakeFactCollector(AnsibleFactCollector):
        pass

    # Test case where FakeCollector.collect() is not decorated
    fact_collector = FakeFactCollector(collectors=[FakeCollector()])
    module = 'fake_module'
    facts = 'fake_facts'
    res = fact_collector.collect(module=module, collected_facts=facts)
    assert res == {'a': 1}

    # Test case where FakeCollector.collect() is decorated
    fact_collector = FakeFactCollector(collectors=[FakeCollector()])

# Generated at 2022-06-13 00:13:38.964767
# Unit test for function get_ansible_collector
def test_get_ansible_collector():

    # TODO: Use pytest fixtures

    namespace = 'test_namespace'
    filter_spec = 'filter_spec'
    gather_subset = ['all']
    gather_timeout = 10000
    minimal_gather_subset = frozenset()

    all_collector_classes = collector.get_collector_classes()

    fact_collector = get_ansible_collector(all_collector_classes,
                                           namespace=namespace,
                                           filter_spec=filter_spec,
                                           gather_subset=gather_subset,
                                           gather_timeout=gather_timeout,
                                           minimal_gather_subset=minimal_gather_subset)

    assert fact_collector.filter_spec == filter_spec
    assert fact_collector.namespace == namespace


# Generated at 2022-06-13 00:13:48.376359
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    import os
    import json

    def test_collector():
        return {'test1': True, 'test2': None}

    fake_collector = collector.BaseFactCollector(fact_ids=[],
                                                 namespaces=[collector.BaseFactNamespace()])
    fake_collector.collect = test_collector

    ansible_collector = AnsibleFactCollector([fake_collector])

    result = ansible_collector.collect()

    assert result['ansible_test1'] is True
    assert result['ansible_test2'] is None

    tmpfile = '/tmp/ansible-facts'
    with open(tmpfile, 'w') as fp:
        json.dump(result, fp)

    os.remove(tmpfile)

# Generated at 2022-06-13 00:14:00.378715
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector
    import time

    class MockFactCollector(BaseFactCollector):
        name = 'mock'

        def __init__(self, *args, **kwargs):
            super(MockFactCollector, self).__init__(*args, **kwargs)
            self._facts = self._load()

        def _load(self):
            return {'mock': 'Mock fact result'}

        def collect(self, module=None, collected_facts=None):
            return self._facts

    mock_fact_collector = MockFactCollector()

    # Make sure we can get the facts without a module arg
    ansible_fact_collector_wo_module = AnsibleFactCollector(collectors=[mock_fact_collector])
    facts

# Generated at 2022-06-13 00:14:08.818416
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    from ansible.module_utils import basic
    import time

    class StubModule(object):
        def __init__(self):
            self.params = {'gather_subset': ''}

        def fail_json(self, **kwargs):
            pass

        def exit_json(self, **kwargs):
            pass

    class TestCollector(collector.BaseFactCollector):
        name = 'test_collector'

        def collect(self, module=None, collected_facts=None):
            collected_facts['ansible_collected_test_collector'] = 'collected'
            return collected_facts

    class TestCollector2(collector.BaseFactCollector):
        name = 'test_collector2'


# Generated at 2022-06-13 00:14:18.436028
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    from .loader import all_collector_classes

    ansible_fact_collector = get_ansible_collector(all_collector_classes)
    ansible_facts = ansible_fact_collector.collect(module=None)

    assert isinstance(ansible_facts, dict)
    assert 'gather_subset' in ansible_facts
    assert 'module_setup' in ansible_facts
    assert 'ansible_facts' in ansible_facts
    assert ansible_facts['ansible_facts']
    assert ansible_facts['ansible_facts']['facter_processorcount'] == 8
    assert 'ansible_facts/hardware' in ansible_facts
    assert 'ansible_facts/virtual' in ansible_facts
    assert 'ansible_facts/virtual/virtualization_role' in ans

# Generated at 2022-06-13 00:14:19.356510
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    pass

# Generated at 2022-06-13 00:14:29.054227
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    from ansible.module_utils.facts import cache
    from ansible.module_utils.facts import namespace
    from ansible.module_utils.facts import system
    from ansible.module_utils.facts import distribution

    m = cache.FactsCacheModuleMock()

    fact_collector = AnsibleFactCollector(collectors=[
        system.SystemCollector(namespace=namespace._PrefixFactNamespace('ansible_')),
        distribution.DistributionCollector(namespace=namespace._PrefixFactNamespace('ansible_')),
    ])

    facts = fact_collector.collect(module=m)

    assert 'ansible_system' in facts
    assert 'ansible_distribution' in facts

# Generated at 2022-06-13 00:14:35.821135
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    all_collector_classes = collector.constants.DEFAULT_MINIMAL_GATHER_SUBSET
    fact_collector = get_ansible_collector(all_collector_classes=all_collector_classes)
    assert fact_collector
    assert len(fact_collector.collectors) == 1
    assert fact_collector.collectors[0].gather_subset == frozenset(['all'])
    assert fact_collector.collectors[0].module_setup

    all_collector_classes = collector.constants.DEFAULT_GATHER_SUBSET
    namespaces_to_exclude = ['facter', 'facter_extras', 'facter_timestamp']
    collect_subset = collector.constants.DEFAULT_MINIMAL_GATHER_SUBSET - frozens

# Generated at 2022-06-13 00:14:57.227862
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    # fake a metadata_collector object
    class FakeMetaDataCollector(collector.BaseFactCollector):
        def collect(self, module=None, collected_facts=None):
            return {'metadata_key': 'metadata_value'}

    # fake a fact_collector object
    class FakeFactCollector(collector.BaseFactCollector):
        def collect(self, module=None, collected_facts=None):
            return {'fake_key': 'fake_value'}

    # instantiate AnsibleFactCollector
    filtered_facts = {
        'fake_key': 'fake_value',
    }
    fact_collector = \
        AnsibleFactCollector(collectors=[FakeFactCollector()],
                             filter_spec=['fake_key'],
                             namespace=None)
    # collect facts


# Generated at 2022-06-13 00:15:08.675909
# Unit test for method collect of class AnsibleFactCollector

# Generated at 2022-06-13 00:15:20.115766
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    import ansible.module_utils.facts.system.distribution as distribution
    import ansible.module_utils.facts.system.platform as platform
    import ansible.module_utils.facts.system.pkg_mgr as pkg_mgr
    import ansible.module_utils.facts.system.users as users

    # Test with gather_subset=None:
    fact_collector = get_ansible_collector([],
                                           namespace=None,
                                           filter_spec=None,
                                           gather_subset=None,
                                           gather_timeout=None,
                                           minimal_gather_subset=None)

    fact_collector_collect_result = fact_collector.collect()
    assert fact_collector_collect_result == {}

    # Test with gather_subset=['min

# Generated at 2022-06-13 00:15:22.308037
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    collectors = []
    fact_collector = AnsibleFactCollector(collectors)
    assert fact_collector.collect() == {}

# Generated at 2022-06-13 00:15:26.990356
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    fact_collector = AnsibleFactCollector()
    collected_facts = fact_collector.collect()

    assert collected_facts
    assert collected_facts.get('facter_kernel') == 'Linux'
    assert 'ansible_lsb' in collected_facts
    assert collected_facts.get('ansible_facter_python') is None


# Generated at 2022-06-13 00:15:38.967679
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():

    class MockFactCollector(collector.BaseFactCollector):
        """Mock Fact Collector for testing purposes."""

        name = 'mock'
        _fact_ids = set([])

        def __init__(self, namespace=None, info_dict=None):
            super(MockFactCollector, self).__init__(namespace=namespace)
            self.info_dict = info_dict or {}

        def collect(self, module=None, collected_facts=None):
            return self.info_dict

    class MockNamespace(object):

        def __init__(self, prefix='', suffix=''):
            self.prefix = prefix
            self.suffix = suffix

        def namespaced(self, key):
            return '%s%s%s' % (self.prefix, key, self.suffix)



# Generated at 2022-06-13 00:15:46.308386
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():

    import tempfile

    from ansible.module_utils.facts import prefixed_namespace

    from ansible.module_utils.facts import collectors

    from ansible.module_utils.facts import default_collector

    class CollectionFailed(Exception):
        pass

    class MockCollector(collectors.BaseFactCollector):

        name = 'mock'
        _fact_ids = set(['mock_foo',
                         'mock_bar'])

        def __init__(self, namespace=None):

            super(MockCollector, self).__init__(namespace=namespace)

        def collect(self, module=None, collected_facts=None):

            if module.params['fail']:
                raise CollectionFailed("mock collection fail")


# Generated at 2022-06-13 00:15:54.936484
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    class C1(collector.BaseFactCollector):
        name = 'c1'
        _fact_ids = set(['a', 'b'])

        def collect(self, module=None, collected_facts=None):
            return {'a': 'A', 'b': 'B'}

    fact_collector = \
        AnsibleFactCollector(collectors=[C1()],
                             filter_spec=['*'])

    collected_facts = fact_collector.collect()
    assert collected_facts == {'a': 'A', 'b': 'B'}


# Generated at 2022-06-13 00:16:03.740745
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector
    class TestCollector1(BaseFactCollector):
        name = 'test_collector_1'
        _fact_ids = set([])

        def _get_facts(self):
            return {'test1': 'test1'}

    class TestCollector2(BaseFactCollector):
        name = 'test_collector_2'
        _fact_ids = set([])

        def _get_facts(self):
            return {'test2': 'test2'}

    class TestCollector3(BaseFactCollector):
        name = 'test_collector_3'
        _fact_ids = set([])

        def _get_facts(self):
            return {'test3': 'test3'}

    test_collector1

# Generated at 2022-06-13 00:16:13.369228
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    import datetime
    import json
    import os
    import tempfile

    from ansible.module_utils.facts import cache
    from ansible.module_utils.facts import timeout
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts.collector import FactCache
    from ansible.module_utils.facts.collector.network import NetworkCollector
    from ansible.module_utils.facts.collector.network import NetworkGeneric

    # pretends to be a real module
    class TestModule(object):
        def __init__(self, ansible_facts):
            self.ansible_facts = ansible_facts


# Generated at 2022-06-13 00:16:37.463282
# Unit test for function get_ansible_collector
def test_get_ansible_collector():

    from ansible.module_utils.facts import (
        gather_subset as default_gather_subset,
        minimal_gather_subset as first_minimal_gather_subset,
    )

    collector = get_ansible_collector(collectors=['first'], gather_subset=['all'])
    assert set(collector.collectors) == set(['first', 'ansible_internal'])

    collector = get_ansible_collector(collectors=['first'], gather_subset=['!all'])
    assert set(collector.collectors) == set(['first'])

    collector = get_ansible_collector(collectors=['first'], gather_subset=['!all', 'second'])

# Generated at 2022-06-13 00:16:45.013098
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    collectors = []

    class MyCollector(collector.BaseFactCollector):
        name = 'my'
        _fact_ids = set(['a', 'b', 'c'])

        def collect(self, module=None, collected_facts=None):
            return {'a': 1, 'b': 2, 'c': 3}

    collectors.append(MyCollector(namespace=None))

    fact_collector = AnsibleFactCollector(collectors=collectors)

    assert fact_collector.collect() == {'a': 1, 'b': 2, 'c': 3}

# Generated at 2022-06-13 00:16:56.919625
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    filter_spec = filter_spec or []
    gather_subset = gather_subset or ['all']
    gather_timeout = gather_timeout or timeout.DEFAULT_GATHER_TIMEOUT
    minimal_gather_subset = minimal_gather_subset or frozenset()

    collector_classes = \
        collector.collector_classes_from_gather_subset(
            all_collector_classes=all_collector_classes,
            minimal_gather_subset=minimal_gather_subset,
            gather_subset=gather_subset,
            gather_timeout=gather_timeout)

    collectors = []
    for collector_class in collector_classes:
        collector_obj = collector_class(namespace=namespace)
        collectors.append(collector_obj)

    # Add a collector

# Generated at 2022-06-13 00:17:02.312618
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    # Test a regular fact collection
    fact_collector = \
        AnsibleFactCollector(filter_spec=['facter_*'],
                             namespace=None)

    # These example facts don't have a 'facter_' prefix
    facts_dict_from_collector = {
        'ansible_architecture': 'x86_64',
        'ansible_distribution': 'Debian',
    }

    # expected result: no facts should be returned
    result_facts_dict = \
        fact_collector.collect(collected_facts=facts_dict_from_collector)
    assert len(result_facts_dict) == 0

    # Test fact collection with a fact that match the fact_filter

# Generated at 2022-06-13 00:17:10.266267
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    import ansible.module_utils.facts.collectors.system
    import ansible.module_utils.facts.collectors.network

    filter_spec = ['*', '!ansible_date_time']
    ansible_fact_collector = get_ansible_collector(all_collector_classes=[
        ansible.module_utils.facts.collectors.system.SystemFactCollector,
        ansible.module_utils.facts.collectors.network.NetworkFactCollector],
        filter_spec=filter_spec)

    facts_dict = ansible_fact_collector.collect()


# Generated at 2022-06-13 00:17:20.718510
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    """ Test AnsibleFactCollector.collect method.
    """

    import ansible.module_utils.facts.test.unit.test_module_setup

    # Note: the _test_module_setup function is the module setup function from
    #       the test_module_setup.py module.
    fact_collector = \
        AnsibleFactCollector(collectors=[ansible.module_utils.facts.test.unit.test_module_setup.TestCollector()],
                             filter_spec='*')
    collected_facts = {}
    facts_dict = fact_collector.collect(collected_facts=collected_facts)
    assert facts_dict == {'test': 'This is a test'}

    # Now test filtering of the facts

# Generated at 2022-06-13 00:17:29.039984
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    print("test_get_ansible_collector should work")
    # Fails with network namespace set
    n = collector.PrefixFactNamespace(prefix='test')
    all_collector_classes = collector.get_collector_classes()
    a = get_ansible_collector(all_collector_classes=all_collector_classes,
                              namespace=n,
                              gather_subset="all")
    d = a.collect()
    assert isinstance(d, dict), "Expected a dict"
    assert d.get("test_gather_subset") == "all"
    assert d.get("ARGUMENTS") == sys.argv[1:]

# Generated at 2022-06-13 00:17:35.425604
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    import ansible_collector
    from ansible.module_utils.facts import ssl_cert
    from ansible.module_utils.facts import system
    from ansible.module_utils.facts import network
    from ansible.module_utils.facts import virtual
    from ansible.module_utils.facts import hardware
    from ansible.module_utils.facts import timezone
    from ansible.module_utils.facts import systemd
    from ansible.module_utils.facts import distribution
    from ansible.module_utils.facts import filesystem
    from ansible.module_utils.facts import user
    from ansible.module_utils.facts import package
    from ansible.module_utils.facts import selinux


# Generated at 2022-06-13 00:17:44.206197
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    # Initialize the AnsibleFactCollector
    fact = CollectorFact('collector_fact',
                         namespace=None,
                         filter_spec=None,
                         gather_subset=None,
                         gather_timeout=None,
                         minimal_gather_subset=None)

    # Call the collect method of AnsibleFactCollector class
    result = fact.collect(module=None, collected_facts=None)
    assert result == {'collector_fact': 42}

    # TODO: Add collect method unit test of class AnsibleCollectedFacts
    #       (from fact_cache_control)


# Generated at 2022-06-13 00:17:53.144472
# Unit test for function get_ansible_collector
def test_get_ansible_collector():

    def check_collector_attributes(collected_facts,
                                   expected_fact_ids,
                                   expected_gather_subset,
                                   expected_module_setup):
        assert collected_facts
        assert 'ansible_facts' in collected_facts

        # Validate that we got all the facts we were expecting
        fact_ids = [fact_id for fact_id in collected_facts['ansible_facts'].keys()]
        fact_ids = set(fact_ids)
        assert fact_ids == expected_fact_ids

        # Validate that the 'ansible_facts' contain the proper metadata
        assert 'ansible_facts' in collected_facts
        assert 'gather_subset' in collected_facts['ansible_facts']
        assert 'module_setup' in collected_facts['ansible_facts']
       

# Generated at 2022-06-13 00:18:38.120101
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    collector_classes = [collector.SystemCollector, collector.FileSystemCollector]
    collector_obj = get_ansible_collector(all_collector_classes=collector_classes,
                                          filter_spec=['ansible_*', 'file_systems'],
                                          gather_subset=['all'])
    facts = collector_obj.collect()
    assert 'ansible_facts' in facts
    assert 'gather_subset' in facts
    assert 'ansible_date_time' in facts['ansible_facts']
    assert 'file_systems' in facts['ansible_facts']

# Generated at 2022-06-13 00:18:43.470787
# Unit test for function get_ansible_collector
def test_get_ansible_collector():  # pragma: no cover
    from ansible.module_utils.facts import disc
    from ansible.module_utils.facts import network
    from ansible.module_utils.facts import system
    from ansible.module_utils.facts import collector

    all_collector_classes = [system.SystemCollector,
                             disc.DiscCollector,
                             network.NetworkCollector]

    c = get_ansible_collector(all_collector_classes)
    f = c.collect()

# Generated at 2022-06-13 00:18:44.808208
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    pass

# Generated at 2022-06-13 00:18:52.872641
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    class FakeCollector(collector.BaseFactCollector):
        name = 'fake'
        _fact_ids = set(['fake_fact_1', 'fake_fact_2', 'fake_fact_3'])

        def collect(self, module=None, collected_facts=None):
            collected_facts = collected_facts or {}
            return {'fake_fact_1': 1, 'fake_fact_2': 2, 'fake_fact_3': 3}

    fake_collector = FakeCollector()
    fact_collector = AnsibleFactCollector(collectors=[fake_collector])

    facts_dict = {'fake_fact_1': 1, 'fake_fact_2': 2, 'fake_fact_3': 3}
    assert fact_collector.collect(module=None, collected_facts=None) == facts

# Generated at 2022-06-13 00:19:02.782829
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():

    import ansible.module_utils.facts.test_collector as test_collector

    test_fact_collector = CollectorMetaDataCollector(gather_subset='test_subset', module_setup=False)
    fact_collectors = [test_fact_collector]

    fact_collector = AnsibleFactCollector(collectors=fact_collectors, namespace=None)
    collected_facts = fact_collector.collect(module=test_collector)

    from ansible.module_utils.facts.test_collector import TestCollector
    expected_facts = TestCollector().collect(module=test_collector)
    expected_facts['gather_subset'] = 'test_subset'

    assert collected_facts == expected_facts


# Generated at 2022-06-13 00:19:10.142772
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    from ansible.module_utils.facts.avx import AvxFactCollector
    from ansible.module_utils.facts.system import SystemFactCollector

    # Create a fact collector with filters
    collector = AnsibleFactCollector(filter_spec=['test_fact*'])

    # Add mocked fact collectors to it
    fact_collectors = []
    fact_collectors.append(AvxFactCollector(namespace=None))
    fact_collectors.append(SystemFactCollector(namespace=None))
    fact_collectors.append(collector)

    # Call collect method with mocked fact collectors
    facts = collector.collect(fact_collectors)

    # If a fact collector is added, it should be tested here
    assert 'test_fact' in facts
    assert 'test_fact_1' in facts

# Unit

# Generated at 2022-06-13 00:19:11.743113
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    # TODO: Write a unit test for method collect of class AnsibleFactCollector
    pass

# Generated at 2022-06-13 00:19:12.914418
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():

    pass



# Generated at 2022-06-13 00:19:21.261431
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():

    import mock
    import os.path
    import pkgutil
    import tempfile

    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

    from ansible.module_utils.facts import collector
    from ansible.module_utils.facts import cache
    from ansible.module_utils.facts.collector import _collectors

    from_cache = False

    # Get a cache object for the tests.
    (fd, cache_path) = tempfile.mkstemp()
    os.close(fd)
    cache_obj = cache.FactCache(cache_path)

    # get a AnsibleFactCollector with mocked collectors
    info_dict_1 = {'info_dict_1': 'info_dict_1'}
    info_dict_

# Generated at 2022-06-13 00:19:24.870900
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    class TestCollector(collector.BaseFactCollector):
        pass

    fact_collector = \
        AnsibleFactCollector(collectors=[TestCollector()],
                             filter_spec=None,
                             namespace=None)

    assert fact_collector.collect() == {}