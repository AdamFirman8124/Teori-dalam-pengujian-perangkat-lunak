

# Generated at 2022-06-13 00:09:47.027587
# Unit test for method collect of class CollectorMetaDataCollector
def test_CollectorMetaDataCollector_collect():
    fact_collector = CollectorMetaDataCollector(gather_subset='all',
                                                module_setup=False)
    collected_facts = fact_collector.collect()
    assert collected_facts['gather_subset'] == 'all'


# Generated at 2022-06-13 00:09:52.805663
# Unit test for method collect of class CollectorMetaDataCollector
def test_CollectorMetaDataCollector_collect():
    # create object
    collector_meta_data_collector = CollectorMetaDataCollector(gather_subset='all')
    # call function
    meta_collector = collector_meta_data_collector.collect()
    # test expected results
    assert meta_collector['gather_subset'] == 'all'

# Generated at 2022-06-13 00:09:56.545934
# Unit test for method collect of class CollectorMetaDataCollector
def test_CollectorMetaDataCollector_collect():
    collector = CollectorMetaDataCollector(gather_subset=['all'], module_setup=True)
    result = collector.collect()
    assert result['gather_subset'] == ['all']
    assert result['module_setup'] == True

# Generated at 2022-06-13 00:10:07.315858
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    '''Verify that get_ansible_collector() returns the right subset of collectors
       based on gather_subset='' param. This is a <meta> test that verifies
       get_ansible_collector's behavior is consistent with the documented
       requirements for gather_subset.

       Note this is not a test of the individual fact collectors. We just call
       collect() on the collector and check that it returns the expected type
       of result. We do assume that each fact collector returns something unique.'''

    # Test parameters
    gather_subsets = [ 'all', 'min', '!min', 'network', '!network' ]

# Generated at 2022-06-13 00:10:15.415357
# Unit test for method collect of class CollectorMetaDataCollector
def test_CollectorMetaDataCollector_collect():
    collector_obj = CollectorMetaDataCollector(gather_subset=['something'])
    facts = collector_obj.collect()
    assert facts == {'gather_subset': ['something'], 'module_setup': True}

    collector_obj = CollectorMetaDataCollector()
    facts = collector_obj.collect()
    assert facts == {'gather_subset': ['all'], 'module_setup': True}

    collector_obj = CollectorMetaDataCollector()
    facts = collector_obj.collect(['something'])
    assert facts == {'gather_subset': ['something'], 'module_setup': True}

    collector_obj = CollectorMetaDataCollector(gather_subset=['something'])
    facts = collector_obj.collect(['something'])

# Generated at 2022-06-13 00:10:16.088625
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    pass

# Generated at 2022-06-13 00:10:28.690362
# Unit test for method collect of class CollectorMetaDataCollector
def test_CollectorMetaDataCollector_collect():
    collector = CollectorMetaDataCollector(namespace=None, gather_subset=['all', 'network', '!facter'])
    result = collector.collect()

    # method should return a dictionary
    assert type(result) is dict 
    # dictionary should have two elements
    assert len(result) == 2
    assert 'gather_subset' in result
    assert 'module_setup' in result
    # 'gather_subset' should be a list of strings
    assert type(result['gather_subset']) is list
    for item in result['gather_subset']:
        assert type(item) is str
    # 'module_setup' should be a boolean
    assert type(result['module_setup']) is bool

# Generated at 2022-06-13 00:10:32.172386
# Unit test for method collect of class CollectorMetaDataCollector
def test_CollectorMetaDataCollector_collect():
    collector_meta_data_collector = CollectorMetaDataCollector()
    collectors = []
    collector_meta_data_collector.collectors = collectors
    collector_meta_data_collector.gather_subset = 'test_gather_subset'
    collector_meta_data_collector.module_setup = 'test_module_setup'
    meta_facts = collector_meta_data_collector.collect()

    assert meta_facts is not None
    assert meta_facts['gather_subset'] == 'test_gather_subset'
    assert meta_facts['module_setup'] == 'test_module_setup'


# Generated at 2022-06-13 00:10:43.783366
# Unit test for function get_ansible_collector
def test_get_ansible_collector():

    from ansible.module_utils.facts.kubectl import KubectlFactCollector
    from ansible.module_utils.facts.cloud.aws import AWSFactCollector
    from ansible.module_utils.facts.cloud.azure import AzureFactCollector
    from ansible.module_utils.facts.cloud.gcp import GCPFactCollector
    from ansible.module_utils.facts.cloud.openstack import OpenStackFactCollector

    all_collector_classes = \
        [KubectlFactCollector, AWSFactCollector, AzureFactCollector, GCPFactCollector, OpenStackFactCollector]

    # gather all cloud facts (but no kubectl facts)

# Generated at 2022-06-13 00:10:55.586686
# Unit test for function get_ansible_collector
def test_get_ansible_collector():

    class Test_Module_Setup(collector.BaseFactCollector):
        '''A test collector that sets module_setup to Fale.'''

        name = 'test_module_setup'
        _fact_ids = set([])

        def __init__(self, namespace=None):
            super(Test_Module_Setup, self).__init__(namespace=namespace)

        def collect(self, module=None, collected_facts=None):
            return {}

    def _get_collector_obj(collector_class, namespace=None):
        return collector_class(namespace=namespace)

    collector_classes = [Test_Module_Setup]


# Generated at 2022-06-13 00:11:18.019906
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    from ansible.module_utils.facts.default import DefaultCollector
    from ansible.module_utils.facts import namespace

    n = namespace.PrefixFactNamespace('ansible_')
    c = DefaultCollector(namespace=n)
    fact_collector = AnsibleFactCollector(collectors=[c])

    # Generate sample data

# Generated at 2022-06-13 00:11:25.892412
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts import collector
    from ansible.module_utils.facts import default

    namespace = PrefixFactNamespace(prefix='ansible_')
    namespace2 = PrefixFactNamespace(prefix='ansible_2_')

    fact_collector = collector.AnsibleFactCollector(namespace=namespace,
                                                    collectors=[default.DefaultCollector(namespace=namespace),
                                                                default.DefaultCollector(namespace=namespace2)])

    facts_dict = fact_collector.collect()

    assert facts_dict
    assert len(facts_dict) >= 0
    # we build key with prefix.
    assert facts_dict.get('ansible_system')

# Generated at 2022-06-13 00:11:34.448669
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    from ansible.module_utils.facts.collector.base import BaseFactCollector
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts.collector.network import NetworkFactCollector

    class TestCollector1(BaseFactCollector):
        name = 'testcollector1'
        _fact_ids = []

        def collect(self, module=None, collected_facts=None):
            return {}

    class TestCollector2(BaseFactCollector):
        name = 'testcollector2'
        _fact_ids = []

        def collect(self, module=None, collected_facts=None):
            return {}

    class TestCollector3(BaseFactCollector):
        name = 'testcollector3'
        _fact_ids = []


# Generated at 2022-06-13 00:11:44.213970
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    # Test case: collect everything
    fact_collector = \
        AnsibleFactCollector(collectors=[],
                             filter_spec='*',
                             namespace='test_namespace')
    fact_dict = fact_collector.collect()
    assert fact_dict == {'test_namespace': {}}

    # Test case: collect generic facts
    fact_collector = \
        AnsibleFactCollector(collectors=[],
                             filter_spec='*',
                             namespace='test_namespace')
    fact_dict = fact_collector.collect()
    assert fact_dict == {'test_namespace': {}}

# Generated at 2022-06-13 00:11:55.547350
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    import pytest

    class MockModuleSetup(object):
        # a mock empty module setup object
        def __init__(self, **kwargs):
            pass

        def __call__(self, **kwargs):
            return {}

    class MockCollector(collector.BaseFactCollector):
        def __init__(self, **kwargs):
            self.kwargs = kwargs

        def collect(self, module=None, collected_facts=None):
            self._called_with_module = module
            self._called_with_collected_facts = collected_facts
            return {}

        def collect_with_namespace(self, module=None, collected_facts=None):
            self._called_with_module = module
            self._called_with_collected_facts = collected_facts
            return {}


# Generated at 2022-06-13 00:12:06.172067
# Unit test for method collect of class AnsibleFactCollector

# Generated at 2022-06-13 00:12:11.603743
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():

    class Collector(object):
        def collect_with_namespace(self, module=None, collected_facts=None):
            return {'foo': 'bar'}

    collector = Collector()
    fact = AnsibleFactCollector(collectors=[collector]).collect()
    assert {'foo': 'bar'} == fact

# Generated at 2022-06-13 00:12:18.383387
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():

    class MockCollector(collector.BaseFactCollector):
        name = 'foo'

        def collect(self, module=None, collected_facts=None):
            facts = collected_facts.copy()
            facts['foo'] = 'bar'
            return facts

    mock_collector_obj = MockCollector()
    fact_collector = AnsibleFactCollector(collectors=[mock_collector_obj])

    # test filter_spec '' or []
    facts_dict = fact_collector.collect(filter_spec='')
    assert facts_dict == {'foo': 'bar'}

    facts_dict = fact_collector.collect(filter_spec=[])
    assert facts_dict == {'foo': 'bar'}

    # test filter_spec *

# Generated at 2022-06-13 00:12:30.166332
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():

    # Given
    namespace = None
    filter_spec = None

    # When
    collector = AnsibleFactCollector(collectors=[], namespace=namespace)

    # Then
    result = collector.collect(collected_facts={'name': 'TestFactCollector'})
    assert isinstance(result, dict)
    assert not result

    # Given
    namespace = None
    filter_spec = None

    # When
    collector = AnsibleFactCollector(collectors=[], namespace=namespace)

    # Then
    result = collector.collect(collected_facts={'name': 'TestFactCollector'})
    assert isinstance(result, dict)
    assert not result

    # Given
    namespace = None
    filter_spec = []

    # When

# Generated at 2022-06-13 00:12:37.776791
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    class FakeCollector(collector.BaseFactCollector):
        def collect(self, module=None, collected_facts=None):
            return {'fake1': 1,
                    'fake2': 2,
                    'fake3': 3}

    fake_collector = FakeCollector()
    fact_collector = AnsibleFactCollector(collectors=[fake_collector], namespace='test')

    assert fact_collector.collect() == fake_collector.collect()



# Generated at 2022-06-13 00:12:59.366483
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    class MockCollector0(object):
        def collect(self, module=None, collected_facts=None):
            return {'mockfact0': 'mockval0'}

    class MockCollector1(object):
        def collect(self, module=None, collected_facts=None):
            return {'mockfact1': 'mockval1'}

    class MockCollectorSubset(object):
        def __init__(self, subset=None, *args, **kwargs):
            pass

        def collect(self, module=None, collected_facts=None):
            return {'mock_subset_fact': 'mock_subset_val'}

    class MockCollectorTimeout(object):
        def __init__(self, timeout=None, *args, **kwargs):
            self.timeout = timeout



# Generated at 2022-06-13 00:13:10.988064
# Unit test for function get_ansible_collector
def test_get_ansible_collector():

    from ansible.module_utils.facts.collector.base import BaseFactCollector
    from ansible.module_utils.facts.collector import collector_classes

    class MockCollector(object):

        def __init__(self, namespace):
            pass

        def collect_with_namespace(self, module, collected_facts):
            return {}

    class MockCollectorClass(BaseFactCollector):
        name = 'MOCK'

        def __init__(self, namespace):
            self._gather_ansible_test = MockCollector(namespace)

    fake_collectors = {
        'MOCK': MockCollectorClass
    }


# Generated at 2022-06-13 00:13:22.170106
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    class InternalDummyCollector(collector.BaseFactCollector):
        name = 'internal_dummy'
        _fact_ids = set(['internal_dummy_fact'])

        def _get_facts(self, collected_facts=None):
            return {'internal_dummy_fact': 'internal_dummy_fact_value'}

    class DummyCollector(AnsibleFactCollector):
        name = 'dummy'
        _fact_ids = set(['dummy_fact'])

        def collect(self, module=None, collected_facts=None):
            return {'dummy_fact': 'dummy_fact_value'}

    # create dummy collector
    dummy_collector = DummyCollector(namespace=None)

    # create internal dummy collector
    internal_dummy_collector = Internal

# Generated at 2022-06-13 00:13:22.846184
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    pass

# Generated at 2022-06-13 00:13:27.902909
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts.network.base import NetworkCollector
    
    namespace = PrefixFactNamespace(prefix='ansible_')
    fact_collector = AnsibleFactCollector(namespace=namespace)
    fact_collector.collectors = [NetworkCollector(namespace)]
    
    fact_dicts = fact_collector.collect()
    assert type(fact_dicts) is dict
    assert 'ansible_all_ipv4_addresses' in fact_dicts



# Generated at 2022-06-13 00:13:38.065488
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    class CollectorClass1(collector.BaseFactCollector):
        name = 'collector_class1'

        def collect(self, module=None, collected_facts=None):
            return {'foo_dict': {'value': 'bar_dict'}}

    class CollectorClass2(collector.BaseFactCollector):
        name = 'collector_class2'

        def collect(self, module=None, collected_facts=None):
            return {'foo_list': ['bar_list']}

    class CollectorClass3(collector.BaseFactCollector):
        name = 'collector_class3'

        def collect(self, module=None, collected_facts=None):
            return {'foo_string': 'bar_string'}


# Generated at 2022-06-13 00:13:43.054940
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    import sys
    import mock

    try:
        from __main__ import AnsibleModule
    except ImportError:
        from ansible.module_utils.facts import ansible_module_mock as AnsibleModule

    module = AnsibleModule(argument_spec=dict())

    filter_spec = filter_spec or []

    collectors = [mock.Mock(), mock.Mock()]
    filter_spec = []
    fact_collector = AnsibleFactCollector(collectors, filter_spec)

    facts = {'first': '1', 'second': '2'}
    collected_facts = {}
    facts_dict = {'first': '1'}

    for collector_obj in collectors:

        # Set 'first' fact for first collector and check if it will be returned
        # with the collect method
        collector_obj.collect

# Generated at 2022-06-13 00:13:47.414872
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    class Fake(object):
        def collect_with_namespace(self, module=None, collected_facts=None):
            return {'fake1': 'value1', 'fake2': 'value2'}

    collector = AnsibleFactCollector(collectors=[Fake()])
    facts = collector.collect()
    assert facts == {'fake1': 'value1', 'fake2': 'value2'}


# Generated at 2022-06-13 00:13:53.968021
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    import copy
    import inspect

    from ansible.module_utils.facts.namespace import add_namespace_prefix

    # NOTE: This could run in parallel. Ensure that no unexpected global namespace
    # interference affects the tests.
    def make_caller_frame(collector_obj):
        caller_frame = inspect.currentframe()
        for c, m in inspect.getouterframes(caller_frame):
            if hasattr(c, 'f_locals') and 'self' in c.f_locals and c.f_locals['self'] is collector_obj:
                return c

    class BaseCollector(collector.BaseFactCollector):
        def __init__(self):
            super(BaseCollector, self).__init__()
            self.name = 'foo'


# Generated at 2022-06-13 00:14:04.208165
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    data0 = {'a': 'a', 'b': 'b', 'c': 'c'}
    data1 = {'a': 'aa', 'c': 'cc'}
    data2 = {'a': 'aaa', 'b': 'bbb'}

    class MyCollector0:
        def collect(self):
            return data0

    class MyCollector1:
        def collect(self):
            return data1

    class MyCollector2:
        def collect(self):
            return data2

    fact_collector = AnsibleFactCollector(collectors=[MyCollector0(), MyCollector1(), MyCollector2()])

    facts = fact_collector.collect()
    assert facts == {'a': 'a', 'b': 'bbb', 'c': 'cc'}


# Generated at 2022-06-13 00:14:29.722225
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    from ansible.module_utils.facts.collector import BaseFactCollector
    class Collector(BaseFactCollector):
        name = 'one'
        _fact_ids = set()

        def collect_with_namespace(self, collected_facts=None, module=None):
            return {'foo': 'bar'}

    class Collector2(BaseFactCollector):
        name = 'two'
        _fact_ids = set()

        def collect_with_namespace(self, collected_facts=None, module=None):
            return {'two': 'bar'}

    class Collector3(BaseFactCollector):
        name = 'three'
        _fact_ids = set()

        def collect_with_namespace(self, collected_facts=None, module=None):
            return {'three': 'bar'}

   

# Generated at 2022-06-13 00:14:36.265264
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():

    class Collector(collector.BaseFactCollector):
        name = 'test'

        def collect(self, module=None, collected_facts=None):
            return {'test_fact': 'test_fact_value'}

    class NamespacedCollector(collector.PrefixedFactNamespace):
        name = 'test_namespaced'

        def __init__(self, namespace, prefix='ansible_'):
            self.namespace = namespace
            self.prefix = prefix

        def collect(self, module=None, collected_facts=None):
            return {'test_ns_fact': 'test_ns_fact_value'}

    class DependentCollector(collector.BaseFactCollector):
        name = 'test_dependent'


# Generated at 2022-06-13 00:14:44.000185
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    from ansible.module_utils.facts import default_collectors
    fact = get_ansible_collector(all_collector_classes=default_collectors)
    collection = fact.collect({'ANSIBLE_FACTS_CACHE_PLUGIN': None})
    assert isinstance(collection, dict)
    assert collection.get('ansible_facts')


__all__ = [
    'AnsibleFactCollector',
    'get_ansible_collector',
]

# Generated at 2022-06-13 00:14:54.144591
# Unit test for function get_ansible_collector
def test_get_ansible_collector():

    gather_subset = ['!all', 'min']
    filter_spec = ['!*_filter']
    filter_spec2 = ['!os', '!os_version']

    # unit test for normal case
    fact_collector = get_ansible_collector(all_collector_classes=collector.all_collector_classes,
                                           gather_subset=gather_subset,
                                           filter_spec=filter_spec)

    assert fact_collector.filter_spec == filter_spec

    assert len(fact_collector.collectors) == len(collector.all_collector_classes)

    assert isinstance(fact_collector, AnsibleFactCollector)

    # unit test for empty gather_subset case

# Generated at 2022-06-13 00:14:58.937160
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():

    # Arrange
    class CollectorA():
        def collect(self):
            return {'test_fact_a': 'a'}

    class CollectorB():
        def collect(self):
            return {'test_fact_b': 'b'}

    # Act
    ansible_collector = AnsibleFactCollector([CollectorA(), CollectorB()])
    ansible_collector.collect()

    # Assert
    assert 'test_fact_a' in ansible_collector.fact_ids
    assert 'test_fact_b' in ansible_collector.fact_ids


# Generated at 2022-06-13 00:15:00.469255
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    pass

# Generated at 2022-06-13 00:15:11.619741
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    """
    Unit test for method collect of class AnsibleFactCollector
    """
    from ansible.module_utils.facts.namespace import PrefixFactNamespace

    fact_1 = {u'fact_1': u'fact_1'}
    fact_2 = {u'fact_2': u'fact_2'}
    fact_3 = {u'fact_3': u'fact_3'}
    fact_4 = {u'fact_4': u'fact_4'}
    fact_5 = {u'fact_5': u'fact_5'}

    class Collector1(collector.BaseFactCollector):
        name = 'test_collector_1'

        def collect(self, module=None, collected_facts=None):
            return fact_1


# Generated at 2022-06-13 00:15:16.791697
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    gather_subset = ['all']
    collector_classes = collector.get_collector_classes()
    fact_collector = get_ansible_collector(all_collector_classes=collector_classes,
                                           gather_subset=gather_subset)
    assert fact_collector

# Generated at 2022-06-13 00:15:22.834346
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():

    class FactCollector(collector.BaseFactCollector):
        def collect(self, module=None, collected_facts=None):
            return {'foo': 'bar'}

    fact_collector = AnsibleFactCollector(collectors=[
        FactCollector(),
        FactCollector()
    ])

    result = fact_collector.collect()
    assert result == {'foo': 'bar', 'foo': 'bar'}



# Generated at 2022-06-13 00:15:34.970340
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    from ansible.module_utils.facts.system.base import BaseFactCollector
    from ansible.module_utils.facts.timeout import timeout_is_expired
    from ansible.module_utils.facts import namespaced_fact_collector

    # A dummy class to use for testing
    class DummyFactCollector(BaseFactCollector):
        name = 'dummy_fact'
        _fact_ids = {'dummy_fact_1', 'dummy_fact_2'}

        def collect(self, module=None, collected_facts=None):
            return {'dummy_fact_1': 'foo', 'dummy_fact_2': 'bar'}

    # A dummy class to use for testing
    class AnotherDummyFactCollector(BaseFactCollector):
        name = 'another_dummy_fact'


# Generated at 2022-06-13 00:15:55.756010
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    '''Test the collect method of class AnsibleFactCollector'''
    import sys
    import os
    import shutil
    import tempfile

    # py3 compatibility hack
    if sys.version_info[:2] == (3, 5):
        from unittest import mock
    else:
        import mock


# Generated at 2022-06-13 00:16:04.728075
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    from ansible.module_utils.facts import default_collector_classes

    # Try with default gather_subset
    ansible_fact_collector = get_ansible_collector(all_collector_classes=default_collector_classes)
    # TODO: assert that the collector was constructed as expected

    # Try with all gather_subset
    ansible_fact_collector = get_ansible_collector(all_collector_classes=default_collector_classes,
                                                   gather_subset=['all'])
    # TODO: assert that the collector was constructed as expected

    # Try with invalid gather_subset
    ansible_fact_collector = get_ansible_collector(all_collector_classes=default_collector_classes,
                                                   gather_subset=['invalid'])


# Generated at 2022-06-13 00:16:14.545114
# Unit test for method collect of class AnsibleFactCollector

# Generated at 2022-06-13 00:16:20.543490
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    import ansible.module_utils.facts.collector.network
    all_collector_classes = [
        ansible.module_utils.facts.collector.network.NetworkCollector,
    ]
    fact_collector = get_ansible_collector(
        all_collector_classes=all_collector_classes)

    gathered_facts = fact_collector.collect()

    assert 'ansible_facts' in gathered_facts
    assert 'gather_subset' in gathered_facts['ansible_facts']
    assert 'module_setup' in gathered_facts['ansible_facts']

# Generated at 2022-06-13 00:16:31.143760
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    import unittest

    class TestCollector(collector.FallbackCollector):
        name = 'test'

        def __init__(self, namespace=None):
            super(TestCollector, self).__init__(namespace=namespace)

        def _collect(self, module=None, collected_facts=None):
            return {self.get_fact_id('test'): 'test_value'}

    class TestCollector2(collector.FallbackCollector):
        name = 'test2'

        def __init__(self, namespace=None):
            super(TestCollector2, self).__init__(namespace=namespace)

        def _collect(self, module=None, collected_facts=None):
            return {self.get_fact_id('test2'): 'test_value2'}



# Generated at 2022-06-13 00:16:36.887742
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    from ansible.module_utils.facts import test_collectors_classes as test_collector_classes

    collector_classes = [
        test_collector_classes.IncorrectCollector,
        test_collector_classes.TestCollector1,
        test_collector_classes.TestCollector2,
        test_collector_classes.TestCollector3,
    ]

    fact_collector = AnsibleFactCollector(collectors=collector_classes)

    ret = fact_collector.collect()
    assert ret == {'test_collector_1': {'fact1': 'value1'},
                   'test_collector_2': {'fact2': 'value2'},
                   'test_collector_3': {'fact3': 'value3'}}


# Generated at 2022-06-13 00:16:46.714413
# Unit test for function get_ansible_collector
def test_get_ansible_collector():

    class TestCollector(collector.BaseFactCollector):
        name = 'test'
        _fact_ids = set(['test_fact'])

        def collect(self, module=None, collected_facts=None):
            return {'test_fact': 5}

    assert get_ansible_collector([TestCollector],
                                 filter_spec=['test_fact']).collect() == \
            {'ansible_facts': {'test_fact': 5},
             'gather_subset': ['all'],
             'module_setup': True}


# Generated at 2022-06-13 00:16:54.042637
# Unit test for function get_ansible_collector
def test_get_ansible_collector():

    from ansible.module_utils.facts.collector import \
        AnsibleDefaultCollector, \
        AnsibleFacterFactCollector, \
        AnsibleOhaiFactCollector

    # gather_subset = ['all']
    collecters = get_ansible_collector(all_collector_classes=[AnsibleDefaultCollector,
                                                               AnsibleFacterFactCollector,
                                                               AnsibleOhaiFactCollector],
                                       gather_subset=['all'])
    assert Ansi

# Generated at 2022-06-13 00:17:04.834638
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    from ansible.module_utils.facts import collector
    from ansible.module_utils.facts.network.osc import OpenStackNetworkCollector
    from ansible.module_utils.facts.namespace import PrefixFactNamespace

    # This is the minimal set of collectors from which any set can be built
    # in 'gather_subset' or 'gather_network_resources'
    minimal_collector_classes = collector.get_collector_classes()

    # Pick a random collector that we have
    collector_class = OpenStackNetworkCollector

    # Pick a random namespace that is not already in use
    namespace = PrefixFactNamespace(prefix='osc_')

    # Pick a random filter that is not already in use
    filter = 'osc_*'

    # Pick a random subset string that is not already in use
    # not using a

# Generated at 2022-06-13 00:17:10.516217
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    import unittest

    class CollectingFactCollector(collector.BaseFactCollector):
        '''Fake collector that simply collects an info dict.'''

        def __init__(self, namespace=None, info_dict=None):
            self.info_dict = info_dict
            super(CollectingFactCollector, self).__init__(namespace=namespace)

        def collect(self, module=None, collected_facts=None):
            return self.info_dict

    class TestAnsibleFactCollector(unittest.TestCase):
        '''Test the collect method of AnsibleFactCollector.'''

        def setUp(self):
            self.info_dict = dict(a=1, b=2, c=3)

# Generated at 2022-06-13 00:17:33.679727
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    from ansible.module_utils.facts import collector_registry
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts.plugins.system import VersionFactCollector

    gathered_facts = {}

    fact_collector = get_ansible_collector(all_collector_classes=collector_registry,
                                           gather_subset=['all'],
                                           filter_spec=['version_*'],
                                           namespace=PrefixFactNamespace(prefix='ansible_'))

    # Note that the collector will only be in the list of collectors if it is used (gather_subset='all')
    assert fact_collector.collectors_from_class(VersionFactCollector)

# Generated at 2022-06-13 00:17:44.781940
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    from ansible.module_utils.facts import ansible_collector
    from ansible.module_utils.facts import namespaced_fact
    # Setup the collector
    prefix = 'test_get_ansible_collector'
    namespace = namespaced_fact.PrefixFactNamespace(prefix=prefix)
    assert namespace.get_prefix() == prefix
    an_ansible_collector = ansible_collector.get_ansible_collector(all_collector_classes=[],
                                                                   namespace=namespace,
                                                                   filter_spec=[],
                                                                   gather_subset=[],
                                                                   gather_timeout=None,
                                                                   minimal_gather_subset=['all'])
    # Get the facts
    facts_dict = an_ansible_collector.collect()
    #

# Generated at 2022-06-13 00:17:53.524451
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    from ansible.module_utils.facts import default
    from ansible.module_utils.facts.default import MyFactCollector1, MyFactCollector2
    from ansible.module_utils.facts.system.distribution import DistributionFactCollector
    from ansible.module_utils.facts.collector import module_collector_classes
    fact_collector = get_ansible_collector(module_collector_classes(),
                                           namespace=default.FACT_NAMESPACE)

    collected_facts = fact_collector.collect(module=None, collected_facts=None)

    # test results of the two collections
    assert collected_facts.get('myfact1') == [1, 2, 3]
    assert collected_facts.get('myfact2') == [4, 5, 6]

    # test for the distribution collection

# Generated at 2022-06-13 00:18:05.216505
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    import unittest

    class MockCollector(collector.BaseFactCollector):
        def collect(self, collected_facts=None, module=None):
            return {'ansible_all_ipv4_addresses': '1.2.3.4'}

    class MockCollector2(collector.BaseFactCollector):
        def collect(self, collected_facts=None, module=None):
            return {'ansible_default_ipv4': {'address': '2.3.4.5'}}

    class MockCollector3(collector.BaseFactCollector):
        def collect(self, collected_facts=None, module=None):
            return {'facter_all_ipv4_addresses': '9.8.7.6'}


# Generated at 2022-06-13 00:18:09.357482
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    from ansible.module_utils.facts import ansible_collector
    collector_obj = ansible_collector()
    assert 'module_setup' in collector_obj.collect()


if __name__ == '__main__':
    test_get_ansible_collector()

# Generated at 2022-06-13 00:18:18.587636
# Unit test for function get_ansible_collector
def test_get_ansible_collector():

    fact_collector = \
        get_ansible_collector(all_collector_classes=collector.CollectorRegistry.collector_classes,
                              gather_subset='network',
                              minimal_gather_subset=['all'],
                              gather_timeout=None,
                              filter_spec=None,
                              namespace=None)

    assert len(fact_collector.collectors) == 2

    fact_collector = \
        get_ansible_collector(all_collector_classes=collector.CollectorRegistry.collector_classes,
                              gather_subset=['network'],
                              minimal_gather_subset=['all'],
                              gather_timeout=None,
                              filter_spec=None,
                              namespace=None)


# Generated at 2022-06-13 00:18:29.226176
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts import tools as tools

    class One(BaseFactCollector):
        name = 'one'

        def collect(self, module=None, collected_facts=None):
            return {'one': '1'}

    class Two(BaseFactCollector):
        name = 'two'

        def collect(self, module=None, collected_facts=None):
            return {'two': '2'}

    fact_collector = AnsibleFactCollector(collectors=[One(), Two()])
    collected_facts = fact_collector.collect()

    assert collected_facts['ansible_facts']['one'] == '1'
    assert collected_facts['ansible_facts']['two'] == '2'

# Generated at 2022-06-13 00:18:38.526644
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    from ansible.module_utils.facts import fact_namespace
    from ansible.module_utils.facts.cpu.cpu import CpuFactCollector
    from ansible.module_utils.facts.distribution.distribution import DistributionFactCollector
    from ansible.module_utils.facts.system.system import SystemFactCollector

    test_namespace = fact_namespace.PrefixFactNamespace(prefix='ansible_test_ns_')
    gather_subset = ['all', 'test_system']
    gather_timeout = 10
    minimal_gather_subset = frozenset(['all'])

    filter_spec = ['ansible_test_ns_*']
    collector_classes = [SystemFactCollector, CpuFactCollector, DistributionFactCollector]

    ansible_collect = get_ansible_collector

# Generated at 2022-06-13 00:18:48.057028
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    # set up
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    collectors = ['Network', 'Distribution']
    namespace = PrefixFactNamespace(prefix='ansible_')
    ansible_fact_collector = AnsibleFactCollector(collectors=collectors,
                                                  namespace=namespace)

    # Assert that ansible_facts dictionary doesn't have "ansible_network" or "ansible_distribution"
    ansible_facts = ansible_fact_collector.collect()
    assert not ansible_facts.get('ansible_network', False)
    assert not ansible_facts.get('ansible_distribution', False)

    # Assert that ansible_facts dictionary has the expected keys.
    collectors = ['Network', 'Distribution', 'Machine']
    ansible_

# Generated at 2022-06-13 00:18:53.697556
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    import types

    class MockFactCollector(object):
        def __init__(self):
            self.method_call_count = 0

        def collect_with_namespace(self, collected_facts):
            self.method_call_count += 1
            return {'foo': 'bar'}

    fact_collector = AnsibleFactCollector(collectors=[MockFactCollector()])
    collected_facts = {}
    results = fact_collector.collect(collected_facts=collected_facts)
    assert isinstance(list(results.keys())[0], types.IntType)
    assert results['foo'] == 'bar'

# Generated at 2022-06-13 00:19:35.969597
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    import mock
    from ansible.module_utils.facts import namespace

    mock_collector_cls = mock.MagicMock()
    mock_collector_cls.name = 'mock_collector_cls'
    mock_collector_obj = mock.MagicMock()
    mock_collector_cls.return_value = mock_collector_obj
    mock_collector_obj.collect_with_namespace.return_value = {'mock_collector_name': 'mock_collector_value'}

    mock_orig_collector_cls = mock.MagicMock()
    mock_orig_collector_cls.name = 'mock_orig_collector_cls'
    mock_orig_collector_obj = mock.MagicMock()
    mock_orig_collector_