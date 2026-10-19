

# Generated at 2022-06-13 00:09:46.699609
# Unit test for method collect of class CollectorMetaDataCollector
def test_CollectorMetaDataCollector_collect():

    collector_meta_data_collector = \
        CollectorMetaDataCollector(gather_subset=['all'])
    expected_meta_facts = {'gather_subset': ['all']}
    actual_meta_facts = collector_meta_data_collector.collect()
    assert expected_meta_facts == actual_meta_facts

# Generated at 2022-06-13 00:09:50.593384
# Unit test for method collect of class CollectorMetaDataCollector
def test_CollectorMetaDataCollector_collect():
    collector = CollectorMetaDataCollector(gather_subset=['all'])
    facts = collector.collect()
    assert facts == {'gather_subset': ['all'], 'module_setup': True}

# Generated at 2022-06-13 00:10:01.611066
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    from ansible.module_utils.facts import collector as c
    from ansible.module_utils.facts import network as network
    from ansible.module_utils.facts.namespace import PrefixFactNamespace

    # get all the facts collectors, we don't really care about the actual facts
    # for this test
    all_collector_classes = c.collector_classes_from_gather_subset(
        all_collector_classes=c.get_collector_classes(),
        minimal_gather_subset=frozenset(),
        gather_subset=['all'],
        gather_timeout=None)

    # base test without namespace, not filter-specs, gather-subset=all

# Generated at 2022-06-13 00:10:11.311431
# Unit test for method collect of class CollectorMetaDataCollector
def test_CollectorMetaDataCollector_collect():
    test_cases = [
        {'gather_subset': 'min', 'module_setup': True,
         'expected': {'gather_subset': 'min', 'module_setup': True}},
        {'gather_subset': '!min', 'module_setup': None,
         'expected': {'gather_subset': '!min'}},
    ]
    for test_case in test_cases:
        collector_meta_data_collector = CollectorMetaDataCollector(gather_subset=test_case['gather_subset'],
                                                                   module_setup=test_case['module_setup'])
        actual = collector_meta_data_collector.collect()
        assert actual == test_case['expected']

# Generated at 2022-06-13 00:10:15.930170
# Unit test for method collect of class CollectorMetaDataCollector
def test_CollectorMetaDataCollector_collect():
    collector_meta_data_collector = CollectorMetaDataCollector(gather_subset=['all'], module_setup=True)
    expected_facts = {'gather_subset': ['all'], 'module_setup': True}
    assert collector_meta_data_collector.collect() == expected_facts

# Generated at 2022-06-13 00:10:24.513505
# Unit test for method collect of class CollectorMetaDataCollector
def test_CollectorMetaDataCollector_collect():
    # Setup
    collector_obj = CollectorMetaDataCollector(gather_subset={'all'})
    collected_facts = {}
    expected = {'ansible_gather_subset': {'all'},
                'ansible_module_setup': True}
    # Exercise
    result = collector_obj.collect(collected_facts=collected_facts)
    # Assert
    assert result == expected
    # Teardown - None



# Generated at 2022-06-13 00:10:34.409168
# Unit test for method collect of class CollectorMetaDataCollector
def test_CollectorMetaDataCollector_collect():
    """Tests method collect of class CollectorMetaDataCollector."""

    class TestCollectorMetaDataCollector(CollectorMetaDataCollector):
        """Subclass of CollectorMetaDataCollector to test its methods."""

    gathered_facts = None
    test_module = None

    # test gather_subset is provided
    test_collector_metadata_collector = TestCollectorMetaDataCollector(gather_subset="all")
    expected_meta_facts = {'gather_subset': 'all'}
    meta_facts = test_collector_metadata_collector.collect(collected_facts=gathered_facts, module=test_module)

    assert meta_facts == expected_meta_facts

    # test gather_subset is not provided
    test_collector_metadata_collector = TestCollectorMetaDataCollector()

# Generated at 2022-06-13 00:10:47.427948
# Unit test for method collect of class CollectorMetaDataCollector
def test_CollectorMetaDataCollector_collect():
    import unittest2 as unittest
    from ansible.module_utils.facts.namespace import PrefixFactNamespace

    class TestCollectorMetaDataCollector(unittest.TestCase):
        def setUp(self):
            self.collector = CollectorMetaDataCollector(gather_subset=['all'],
                                                        module_setup=True)

        def test_collect(self):
            test_instance = self.collector.collect()
            assert test_instance == {'gather_subset': ['all'],
                                     'module_setup': True}

    test_CollectorMetaDataCollector = TestCollectorMetaDataCollector()
    test_CollectorMetaDataCollector.setUp()
    test_CollectorMetaDataCollector.test_collect()


# Generated at 2022-06-13 00:10:53.905366
# Unit test for method collect of class CollectorMetaDataCollector
def test_CollectorMetaDataCollector_collect():
    r = CollectorMetaDataCollector(gather_subset='foo', module_setup=False).collect()
    assert r == {'gather_subset': 'foo'}

    r = CollectorMetaDataCollector(gather_subset='bar', module_setup=True).collect()
    assert r == {'gather_subset': 'bar', 'module_setup': True}


# Generated at 2022-06-13 00:11:03.485970
# Unit test for method collect of class CollectorMetaDataCollector
def test_CollectorMetaDataCollector_collect():
    # Arrange
    obj_class = CollectorMetaDataCollector
    obj_class.name = 'gather_subset'
    obj_class._fact_ids = set([])
    ns = 'namespace'
    gs = 'all'
    ms = True
    obj = obj_class(collectors=None, namespace=ns,
                    gather_subset=gs, module_setup=ms)

    # Act
    meta_facts = obj.collect(module=None, collected_facts=None)

    # Assert
    assert meta_facts['gather_subset'] == gs
    assert meta_facts['module_setup'] == ms

# Generated at 2022-06-13 00:11:09.997467
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    # TODO: refactor get_ansible_collector() so it can be unit tested
    assert get_ansible_collector


# Backwards compat with old name
getAnsibleCollector = get_ansible_collector

# Generated at 2022-06-13 00:11:21.423393
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    with_meta = CollectorMetaDataCollector()
    without_meta = collector.BaseFactCollector()
    all_classes = [with_meta, without_meta]

    # Test that the without_meta class is added
    fact_collector = get_ansible_collector(all_collector_classes=all_classes,
                                           gather_subset=None,
                                           gather_timeout=None,
                                           minimal_gather_subset=None,
                                           filter_spec=None,
                                           namespace=None)
    assert len(fact_collector.collectors) > len(all_classes)
    assert with_meta not in fact_collector.collectors
    # The with_meta collector class is added by get_ansible_collector

# Generated at 2022-06-13 00:11:29.835206
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts.system.distribution import DistributionFactCollector

    namespace = PrefixFactNamespace(prefix='ansible_')
    distribution_collector = DistributionFactCollector(namespace=namespace)

    fact_collector = AnsibleFactCollector(collectors=[distribution_collector])
    result = fact_collector.collect()

    # If a namespace is used, the fact is collected under that namespace
    assert 'ansible_distribution' in result
    assert 'distribution' not in result

    # If a namespace is not used, the fact is collected in the current namespace
    fact_collector = AnsibleFactCollector(collectors=[distribution_collector])
    result = fact_collector.collect()

# Generated at 2022-06-13 00:11:36.554493
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    all_collector_classes = {'a': '1', 'b': '2'}
    namespace = None
    filter_spec = None
    gather_subset = None
    gather_timeout = None
    minimal_gather_subset = None

    fact_collector = get_ansible_collector(all_collector_classes,
                                           namespace,
                                           filter_spec,
                                           gather_subset,
                                           gather_timeout,
                                           minimal_gather_subset)

    assert isinstance(fact_collector, AnsibleFactCollector)
    assert fact_collector.collector_classes == all_collector_classes
    assert fact_collector.filter_spec == filter_spec
    assert fact_collector.namespace == namespace

# Generated at 2022-06-13 00:11:48.389725
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    '''Unit test for function get_ansible_collector.'''

    import ansible.module_utils.facts.namespace as namespace

    # list of AnsibleFactCollector collector classes
    all_collector_classes = [collector.PlatformFactCollector,
                             collector.LocalFactCollector]

    fact_collector = get_ansible_collector(all_collector_classes,
                                           namespace=namespace)
    assert fact_collector

    facts = fact_collector.collect()

    assert facts
    assert 'ansible_facts' in facts
    assert 'ansible_all_ipv4_addresses' in facts['ansible_facts']
    assert 'ansible_all_ipv6_addresses' in facts['ansible_facts']

# Generated at 2022-06-13 00:11:57.949918
# Unit test for function get_ansible_collector
def test_get_ansible_collector():

    def test_func(all_collector_classes,
                  namespace=None,
                  filter_spec=None,
                  gather_subset=None,
                  gather_timeout=None,
                  minimal_gather_subset=None):
        return get_ansible_collector(all_collector_classes=all_collector_classes,
                                     namespace=namespace,
                                     filter_spec=filter_spec,
                                     gather_subset=gather_subset,
                                     gather_timeout=gather_timeout,
                                     minimal_gather_subset=minimal_gather_subset)

    # Test 1
    all_collector_classes = [collector.A]

# Generated at 2022-06-13 00:11:58.503410
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    pass

# Generated at 2022-06-13 00:12:10.352119
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    import types
    import unittest
    from ansible.module_utils.facts.collector import CollectorModuleFactCollector
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts.namespace import EmptyFactNamespace

    class TestCollector(CollectorModuleFactCollector):

        name = 'test_collector'

        def _collect_facts_from_module(self, module):

            if module.params['test_collector_error']:
                raise Exception('Test')

            facts = {
                'list': [1, 2, 3],
                'undefined': None,
            }

            return facts

    class TestCollector2(CollectorModuleFactCollector):

        name = 'test_collector_2'


# Generated at 2022-06-13 00:12:17.753964
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    class Dummy1Collector(collector.BaseFactCollector):
        '''Pretend collector 1'''
        name = 'dummy1'

        def collect(self):
            collected_facts = {}
            collected_facts['dummy1'] = 'abc'
            collected_facts['dummy1_namespace'] = 'abc'
            return collected_facts

    dummy_collector_classes = [Dummy1Collector]
    fact_collector = get_ansible_collector(all_collector_classes=dummy_collector_classes,
                                           minimal_gather_subset=['all'],
                                           gather_subset=['dummy1'],
                                           namespace=collector.PrefixFactNamespace(prefix='dummy1_'))
    collected_facts = fact_collector.collect

# Generated at 2022-06-13 00:12:28.308558
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    import ansible.module_utils.facts.system.dns

    all_collector_classes = \
        ansible.module_utils.facts.system.dns.__dict__.values()

    collector_obj = get_ansible_collector(all_collector_classes=all_collector_classes,
                                          namespace=None,
                                          filter_spec=list(),
                                          gather_subset=['all'],
                                          gather_timeout=None,
                                          minimal_gather_subset=frozenset())

    #print 'collector_obj is %s' % collector_obj

    assert(isinstance(collector_obj, AnsibleFactCollector))

# Generated at 2022-06-13 00:12:41.932211
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():

    # Create some collector objects, and set up their collect method to return some
    # dummy data. Note the use of a dict instead of a list, in case we want to do a
    # merge in future.
    collector_a = collector.BaseFactCollector()
    collector_a.collect = lambda: {'a': 1, 'b': 2}

    collector_b = collector.BaseFactCollector()
    collector_b.collect = lambda: {'c': 3, 'd': 4}

    # Create the fact collector, passing in the collector objects
    fact_collector = AnsibleFactCollector([collector_a, collector_b])

    # Now collect the facts
    facts = fact_collector.collect()

    # Check that the facts dict contains all the data from the other collectors

# Generated at 2022-06-13 00:12:48.021430
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    class TestCollector(collector.BaseFactCollector):
        name = 'test'
        def collect(self):
            return {'test-fact': 'dummy'}
    class TestFactNamespace(collector.BaseFactNamespace):
        name = 'test'

    collectors = [TestCollector(namespace=TestFactNamespace())]
    fact_collector = AnsibleFactCollector(collectors=collectors)

    facts = fact_collector.collect()

    assert facts == {'ansible_facts': {'test': {'test-fact': 'dummy'}}}


# Generated at 2022-06-13 00:12:59.539554
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    import ansible.module_utils.facts.collectors.base as base_collector
    class MockCollector(base_collector.BaseFactCollector):
        name = 'mock'
        _fact_ids = set(['mock'])
        def collect(self):
            return {'mock': 'fact'}
    fact_collector = get_ansible_collector(
        all_collector_classes=[MockCollector, CollectorMetaDataCollector],
        gather_subset=['all'])
    facts = fact_collector.collect()
    assert set(facts.keys()) == set(['ansible_facts', 'gather_subset', 'module_setup'])
    assert facts['ansible_facts']['mock'] == 'fact'

# Generated at 2022-06-13 00:13:11.069199
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    fact_collector = get_ansible_collector(all_collector_classes=None,
                                           namespace=None,
                                           filter_spec=None,
                                           gather_subset=None,
                                           gather_timeout=None,
                                           minimal_gather_subset=None)
    assert fact_collector
    assert len(fact_collector.collectors) == 1

    fact_collector = get_ansible_collector(all_collector_classes=None,
                                           namespace=None,
                                           filter_spec=[],
                                           gather_subset=['all'],
                                           gather_timeout=None,
                                           minimal_gather_subset=None)

    assert fact_collector
    assert len(fact_collector.collectors) == 1



# Generated at 2022-06-13 00:13:22.256464
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    '''Unit Test method collect of AnsibleFactCollector class. '''

    # Test Case 1: When all args are null
    # Observe: should return an empty dict
    fact_collector_1 = AnsibleFactCollector()
    assert {} == fact_collector_1.collect()

    # Test Case 2: When only collectors argument is passed
    # Observe: should return what is returned by the collectors
    simple_collector_class = collector.type('SimpleCollector', (collector.BaseFactCollector,),
                                            {'name': 'simplecollector', '_fact_ids': set([]),
                                             'collect': lambda self: {'a': 1, 'b': 2}, })
    fact_collector_2 = AnsibleFactCollector(collectors=[simple_collector_class()])

# Generated at 2022-06-13 00:13:28.767886
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    from ansible.module_utils.facts import default, hardware, network, system
    facts_collector = AnsibleFactCollector([default.DefaultFactCollector(),
                                            hardware.HardwareFactCollector(),
                                            network.NetworkFactCollector(),
                                            system.SystemFactCollector()])
    facts_dict = facts_collector.collect()
    assert 'ansible_facts' in facts_dict
    assert 'default' in facts_dict['ansible_facts']
    assert 'system' in facts_dict['ansible_facts']
    assert 'network' in facts_dict['ansible_facts']
    assert 'hardware' in facts_dict['ansible_facts']
    assert 'ansible_distribution' in facts_dict['ansible_facts']['default']
    assert 'ansible_distribution' in facts

# Generated at 2022-06-13 00:13:38.766354
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    class DummyFactCollector(collector.BaseFactCollector):
        '''Dummy fact collector for testing AnsibleFactCollector.collect().'''

        name = 'dummy'
        _fact_ids = set(['fact_name'])

        def collect(self, module=None, collected_facts=None):
            collected_facts = collected_facts or {}
            collected_facts['fact_name'] = 'value of fact_name'
            return collected_facts

    fact_collector = \
        AnsibleFactCollector(collectors=[DummyFactCollector(namespace='ns')])

    facts = fact_collector.collect()

# Generated at 2022-06-13 00:13:48.559216
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    # NOTE: This assumes that we have the following collectors enabled
    #   ansible.module_utils.facts.system.distribution.DistributionFactCollector
    #   ansible.module_utils.facts.system.distribution.MacOSXDistributionFactCollector
    #   ansible.module_utils.facts.system.version.VersionFactCollector

    all_collector_classes = \
        collector.get_collector_classes(namespace=collector.ALL_NAMESPACE)

    # Test '*' gather_subset for all namespaces and for the 'ansible' namespace
    fact_collector = \
        get_ansible_collector(
            all_collector_classes=all_collector_classes,
            gather_subset='*')

    facts = fact_collector.collect()

    distribution = facts

# Generated at 2022-06-13 00:14:00.548734
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    '''Test the AnsibleFactCollector.collect method.'''
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts.fact_cache import BaseFactCollector

    class FooFactCollector(BaseFactCollector):
        pass

    ffc = FooFactCollector()
    ffc.collect_with_namespace = lambda collected_facts: {'test': 'bar'}
    fac_collector = AnsibleFactCollector(collectors=[ffc],
                                         namespace=PrefixFactNamespace(prefix='test_'))
    assert 'test_test' in fac_collector.collect()
    assert 'test' not in fac_collector.collect()
    fac_collector = AnsibleFactCollector(collectors=[ffc],
                                         namespace='')

# Generated at 2022-06-13 00:14:05.476016
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    class TestCollector(collector.BaseFactCollector):
        def collect_with_namespace(self, module=None, collected_facts=None):
            return {'test': 'test'}

    fact_collector = AnsibleFactCollector(collectors=[TestCollector()])
    facts = fact_collector.collect()
    assert facts['test'] == 'test'


# Generated at 2022-06-13 00:14:21.691832
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    from ansible.module_utils.facts import cache
    from ansible.module_utils.facts import network
    from ansible.module_utils.facts import installer
    from ansible.module_utils.facts import users

    import ansible.module_utils.facts.cache
    import ansible.module_utils.facts.network
    import ansible.module_utils.facts.installer
    import ansible.module_utils.facts.users

    all_collector_classes = [cache.NetworkFactsCache,
                             network.Network,
                             installer.Installer,
                             users.User]

    ansible_collector = \
        get_ansible_collector(all_collector_classes=all_collector_classes,
                              namespace=None)

    module = None
    collected_facts = ansible_collector

# Generated at 2022-06-13 00:14:31.780519
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():

    class TestCollector1(collector.BaseFactCollector):
        name = 'test1'

        def collect(self, module=None, collected_facts=None):
            return {'test1': {'a': 1, 'b': 2, 'c': 3}}

    class TestCollector2(collector.BaseFactCollector):
        name = 'test2'

        def collect(self, module=None, collected_facts=None):
            return {'test2': {'a': 10, 'b': 20, 'c': 30}}

    class TestCollector3(collector.BaseFactCollector):
        name = 'test3'

        def collect(self, module=None, collected_facts=None):
            return {'test3': {'a': 100, 'b': 200, 'c': 300}}

    filter_spec

# Generated at 2022-06-13 00:14:43.861244
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():

    # test 1
    f = AnsibleFactCollector(namespace=None, filter_spec=None)
    f.collectors = [collector1]
    assert f.collect(module=None, collected_facts={}) == {}

    # test 2
    f = AnsibleFactCollector(namespace=None, filter_spec=None)
    f.collectors = [collector1, collector2]
    assert f.collect(module=None, collected_facts={}) == facts2

    # test 3
    f = AnsibleFactCollector(namespace=None, filter_spec=None)
    f.collectors = [collector1, collector2, collector3]
    assert f.collect(module=None, collected_facts={}) == {}

    # test 4

# Generated at 2022-06-13 00:14:44.284644
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    pass

# Generated at 2022-06-13 00:14:54.441647
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    '''
    ex1: call AnsibleFactCollector.collect() without providing a filter_spec
    expect: ansible_facts contains all gathered facts

    ex2: call AnsibleFactCollector.collect() with a filter_spec that matches
         3 gathered facts (see mock_collector.MockFactCollector.collect())
    expect: ansible_facts only contains the 3 matched facts

    ex3: call AnsibleFactCollector.collect() with a 'ansible_' prefixed filter_spec
         that matches 2 facts
    expect: ansible_facts only contains the 2 matched facts
    '''

    from ansible.module_utils.facts import namespace

    from mock_collector import MockFactCollector, MockFactNamespaceCollector


# Generated at 2022-06-13 00:14:59.204294
# Unit test for function get_ansible_collector
def test_get_ansible_collector():

    from ansible.module_utils.facts.collector import FactCollector
    from ansible.module_utils.facts.system import NetworkCollector

    fact_collector = \
        get_ansible_collector(all_collector_classes=[FactCollector,
                                                     NetworkCollector],
                              gather_subset=['all', 'network', 'virtual'],
                              filter_spec=['network', 'network.interfaces'],
                              namespace=None)

    fact_dict = fact_collector.collect()

    print('Fact dictionary: %s' % fact_dict)

    return fact_collector

# Generated at 2022-06-13 00:15:11.169560
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    # return results under 'ansible_facts' top level key.
    import mock
    import os
    import sys
    from ansible.module_utils.facts import cache
    from ansible.module_utils.facts import ansible_collector
    from ansible.module_utils.facts.system.distribution import DistributionCollector
    from ansible.module_utils.facts.system.distribution import UbuntuDistributionCollector

    _os_version = os.uname()[2]
    _os_major_version = sys.version_info[0]
    _os_distribution = ' '.join(os.uname()[3].split('-')[1:])

    def mock_facts(self, module, collected_facts=None):
        name = self.__class__.__name__

# Generated at 2022-06-13 00:15:22.579047
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():

    class FakeCollector(collector.BaseFactCollector):
        name = 'fake'
        _fact_ids = set(['fact_id_0'])

        def collect(self, module=None, collected_facts=None):
            return {'fact_id_0': 'fact_value_0'}

    class OtherFakeCollector(collector.BaseFactCollector):
        name = 'fake'
        _fact_ids = set(['fact_id_0'])

        def collect(self, module=None, collected_facts=None):
            return {'other_fact_id_0': 'other_fact_value_0',
                    'other_fact_id_1': 'other_fact_value_1',
                    'other_fact_id_2': 'other_fact_value_2'}


# Generated at 2022-06-13 00:15:34.520694
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    '''Unit test for method collect of class AnsibleFactCollector'''

    namespace = 'test_namespace'
    namespace_obj = collector.PrefixFactNamespace(prefix=namespace)

    # Create a Fact subclass that increments a static int and uses that to return a value
    class TestingFactCollector(collector.BaseFactCollector):
        i = 0

        def collect(self, module=None, collected_facts=None):
            TestingFactCollector.i += 1
            return {'testing': TestingFactCollector.i}

    # Create a Fact subclass that uses the value returned by the TestingFactCollector
    class DependsOnTestingFact(collector.BaseFactCollector):

        def collect(self, module=None, collected_facts=None):
            testing_fact = collected_facts['test_namespace']['testing']


# Generated at 2022-06-13 00:15:36.916363
# Unit test for function get_ansible_collector
def test_get_ansible_collector():

    import ansible.module_utils.facts.collector

    fact_collector = get_ansible_collector(all_collector_classes=ansible.module_utils.facts.collector.collector_classes)

    facts_dict = fact_collector.collect()

    return facts_dict

# Generated at 2022-06-13 00:15:55.360673
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    import unittest
    from ansible.module_utils.facts import namespace


# Generated at 2022-06-13 00:16:04.241347
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    class TestFactCollector(collector.BaseFactCollector):
        name = 'test'

        def collect(self, module=None, collected_facts=None):
            return {'test_fact': 'collect_this'}

    class TestFactCollectorFail(collector.BaseFactCollector):
        name = 'test'

        def collect(self, module=None, collected_facts=None):
            raise Exception('return_this')

    test_fact_collector = TestFactCollector()
    test_fact_collector_fail = TestFactCollectorFail()
    ansible_fact_collector = AnsibleFactCollector(collectors=[test_fact_collector, test_fact_collector_fail])

    assert ansible_fact_collector.collect() == {'test_fact': 'collect_this'}

# Generated at 2022-06-13 00:16:13.908573
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    from ansible.module_utils.facts.system.base import BaseFactCollector
    from ansible.module_utils.facts.system.distribution import DistributionFactCollector

    all_collector_classes = [
        BaseFactCollector,
        DistributionFactCollector,
    ]

    fact_collector = get_ansible_collector(all_collector_classes=all_collector_classes)
    assert BaseFactCollector in fact_collector.collectors
    assert DistributionFactCollector in fact_collector.collectors
    assert fact_collector.filter_spec is None
    assert fact_collector.namespace is None

    fact_collector = get_ansible_collector(all_collector_classes=all_collector_classes,
                                           gather_subset=['!all', 'network'])
   

# Generated at 2022-06-13 00:16:21.517636
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    class Collect1(collector.BaseFactCollector):

        name = 'collect1'
        _fact_ids = set([])

        def collect(self, module=None, collected_facts=None):
            return {'k1': 'v1', 'k2': 'v2'}

    class Collect2(collector.BaseFactCollector):

        name = 'collect2'
        _fact_ids = set([])

        def collect(self, module=None, collected_facts=None):
            return {'k3': 'v3', 'k4': 'v4'}

    collectors = [Collect1(), Collect2()]

    fact_collector = AnsibleFactCollector(collectors=collectors)
    facts_dict = fact_collector.collect()

# Generated at 2022-06-13 00:16:27.524930
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    import ansible.module_utils.facts.system
    ac = AnsibleFactCollector(collectors=[ansible.module_utils.facts.system.SystemCollector()])
    f = ac.collect()
    assert 'system' in f
    assert 'distribution' in f['system']
    assert 'release' in f['system']
    assert 'system' in f

# Generated at 2022-06-13 00:16:35.020277
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    class DummyCollector1(collector.BaseFactCollector):
        name = 'dummy1'
        _fact_ids = set([])

        def collect(self, module=None, collected_facts=None):
            return {'f1': 1}

    class DummyCollector2(collector.BaseFactCollector):
        name = 'dummy2'
        _fact_ids = set([])

        def collect(self, module=None, collected_facts=None):
            return {'f1': 2, 'f2': 2}

    class DummyCollector3(collector.BaseFactCollector):
        name = 'dummy3'
        _fact_ids = set([])


# Generated at 2022-06-13 00:16:45.467318
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():

    # test of collecting fake facts
    c1 = collector.BaseFactCollector(namespace='ansible')
    c2 = collector.BaseFactCollector(namespace='ansible')
    c3 = collector.BaseFactCollector(namespace='ansible')
    c3 = collector.BaseFactCollector(namespace='ansible')

    c1.collect = lambda: {'c': 'a'}
    c2.collect = lambda: {'d': 'b'}
    c3.collect = lambda: {'e': 'c'}

    fact_collector = \
        AnsibleFactCollector(collectors=[c1, c2, c3])

    collected_facts = fact_collector.collect()

    assert 'ansible' not in collected_facts

# Generated at 2022-06-13 00:16:56.964709
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts import ansible_collector

    class TestCollector(collector.BaseFactCollector):

        name = 'test'

        def __init__(self, namespace=None):
            super(TestCollector, self).__init__(namespace=namespace)

        def collect(self, module=None, collected_facts=None):
            return {'test_key': 'value'}

        def collect_with_namespace(self, module=None, collected_facts=None):
            return self.namespace.fact({self.name: {'test_key': 'value'}})

    test_collector = TestCollector(namespace=PrefixFactNamespace(prefix='ansible_'))

    ansible

# Generated at 2022-06-13 00:17:02.384791
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    '''
    Test function for method AnsibleFactCollector.collect()
    of class AnsibleFactCollector
    '''

    # Prepare the collector to be tested
    ansible_fact_collector = AnsibleFactCollector()

    # Prepare a fact dictionary

# Generated at 2022-06-13 00:17:07.420654
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    from ansible.module_utils.facts import ansible_collector
    fact_collector = ansible_collector.get_ansible_collector(dict(), namespace=None,
                                                             filter_spec='*', gather_subset=[],
                                                             gather_timeout=timeout.DEFAULT_GATHER_TIMEOUT,
                                                             minimal_gather_subset=frozenset())
    assert fact_collector.collect() == {}

# Generated at 2022-06-13 00:17:31.870140
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    import datetime
    import time
    import json

    import ansible.module_utils.facts.collector
    import ansible.module_utils.facts.hardware

    collector_class_list = \
        ansible.module_utils.facts.collector.get_collector_classes()

    all_collector_classes = {}
    for c in collector_class_list:
        all_collector_classes[c.name] = c

    fact_collector = \
        get_ansible_collector(all_collector_classes=all_collector_classes,
                              gather_subset=['all'],
                              filter_spec=['ansible_eth*'])

    facts = fact_collector.collect()

# Generated at 2022-06-13 00:17:34.916177
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    # Note: For now, the test 'name' is used by the test.py script of the facts module.
    # If you rename the test case, be sure to update that script.

    fact_collector = get_ansible_collector(all_collector_classes=None)

    facts = fact_collector.collect()

    assert len(facts) > 0

# Generated at 2022-06-13 00:17:41.660447
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    try:
        from ansible.module_utils.facts import collector
    except Exception:
        pass
    collectors = []
    collector_obj = collector.DefaultCollector()
    collectors.append(collector_obj)

    fact_collector = AnsibleFactCollector(collectors=collectors)
    facts = fact_collector.collect()

    assert 'default_facts' in facts
    assert facts['default_facts'] == 'foo'

# Generated at 2022-06-13 00:17:49.992262
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    class MockCollector(object):
        def __init__(self, name):
            self.name = name

        def collect_with_namespace(self, module=None, collected_facts=None):
            return {self.name: self.name}

    collector_list = [MockCollector('test1'), MockCollector('test2')]
    fact_collector = AnsibleFactCollector(collectors=collector_list)

    expected_dict = {'test1': 'test1', 'test2': 'test2'}
    actual_dict = fact_collector.collect()
    assert(expected_dict == actual_dict)


# Generated at 2022-06-13 00:18:00.615947
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    '''Test get_ansible_collector'''

    class TestCollector(collector.BaseFactCollector):
        name = 'test'
        def collect(self, module=None, collected_facts=None):
            return {'ansible_facts': {'moo': 'cow'}}

    all_collector_classes = [TestCollector]

    ansible_collector = get_ansible_collector(all_collector_classes=all_collector_classes)

    assert type(ansible_collector) is AnsibleFactCollector
    assert ansible_collector.filter_spec == []
    assert ansible_collector.namespace is None

    assert len(ansible_collector.collectors) == 2

    test_collector = ansible_collector.collectors[0]

# Generated at 2022-06-13 00:18:01.947552
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    pass


# Generated at 2022-06-13 00:18:13.237702
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():

    # create a module_setup collector that provides two facts
    class ModuleSetupCollector(collector.BaseFactCollector):
        name = "module_setup"

        def collect(self, module=None, collected_facts=None):
            return {'module_setup_key_1': 'module_setup_value_1',
                    'module_setup_key_2': 'module_setup_value_2'}

    # create a plain collector that depends on the two module_setup facts
    class PlainCollector(collector.BaseFactCollector):
        name = "plain"


# Generated at 2022-06-13 00:18:19.310711
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    import ansible.module_utils.facts.collector.network

    fact_collector = \
        AnsibleFactCollector(collectors=[
                             ansible.module_utils.facts.collector.network.NetworkCollector(),
                             ],
                             namespace=namespace)

    facts_dict = fact_collector.collect(module=None)

    print('displaying collected data')
    print(facts_dict)

    assert 'ansible_device_eth0' in facts_dict



# Generated at 2022-06-13 00:18:25.676255
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    class TestCollector(collector.BaseFactCollector):
        def collect(self, module=None, collected_facts=None):
            collected_facts = collected_facts or {}
            return {'test_fact': 'test_value'}

    c = AnsibleFactCollector(collectors=[TestCollector()])

    facts = c.collect()
    assert facts['ansible_facts']['test_fact'] == 'test_value'



# Generated at 2022-06-13 00:18:35.958151
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():

    import unittest
    import ansible.module_utils.facts.collector.network as network
    from ansible.module_utils.facts.namespace import PrefixFactNamespace

    class TestNetworkCollector(network.NetworkCollector):

        def _get_interface_info(self):
            return [{'interface': 'eth0', 'macaddress': '00:0c:29:d8:6f:b7', 'ipv4': '192.168.20.69',
                    'ipv6': 'fe80::20c:29ff:fed8:6fb7'}]

    class AnsibleNetworkCollector(AnsibleFactCollector):

        def __init__(self, namespace=None):
            collectors = [TestNetworkCollector(namespace=namespace)]

# Generated at 2022-06-13 00:19:11.213937
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    import os
    import re
    import tempfile
    import time

    # Need to be able to mock a module to pass to a fact collection
    class FakeModule:
        def __init__(self):
            class FakeParams:
                def __init__(self):
                    self.gather_timeout = None
            class FakeAnsibleModule:
                def __init__(self):
                    self.params = FakeParams()

                def fail_json(self, msg):
                    sys.stderr.write("%s\n" % msg)
                    sys.stderr.flush()
            self.ansible_module = FakeAnsibleModule()

        def get_bin_path(self, name, mandatory=False):
            return None

        def fail_json(self, msg):
            self.ansible_module.fail_

# Generated at 2022-06-13 00:19:20.243510
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    '''Unit test for AnsibleFactCollector'''

    # NOTE: this test is simple and just tests that the collector returns
    # facts under 'ansible_facts' top level key and filters correctly
    # More in-depth testing of each collector is in the modules/utils/facts/collector

    class FakeCollector(collector.BaseFactCollector):
        name = 'fake'

        def collect(self, module=None, collected_facts=None):
            return dict(foo=1, bar=2)

    class FakeCollector2(collector.BaseFactCollector):
        name = 'fake2'

        def collect(self, module=None, collected_facts=None):
            return dict(foo=10, bar=20)

    class FakeCollector3(collector.BaseFactCollector):
        name = 'fake'

       

# Generated at 2022-06-13 00:19:31.502666
# Unit test for function get_ansible_collector
def test_get_ansible_collector():

    # FIXME : this is pretty fragile.  We should find a better way to test this.
    #         For now, just make sure the major parts of the system are in place
    #         and are not returning some unexpected exception.

    from ansible.module_utils.facts import cache
    from ansible.module_utils.facts import timeout
    from ansible.module_utils.facts import cache_dir

    from ansible.module_utils.facts.system.distribution import DistributionFactCollector
    from ansible.module_utils.facts.system.mounts import MountFactCollector
    from ansible.module_utils.facts.system.pkg_mgr import PkgMgrFactCollector
    from ansible.module_utils.facts.system.platform import PlatformFactCollector
    from ansible.module_utils.facts.system.user import UserFact

# Generated at 2022-06-13 00:19:38.799144
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    # Create Collectors
    class Collector1(collector.BaseFactCollector):
        def collect(self, module=None, collected_facts=None):
            return dict(col1_fact1='col1_fact1')

    class Collector2(collector.BaseFactCollector):
        def collect(self, module=None, collected_facts=None):
            return dict(col2_fact1='col2_fact1')

    # Namespace
    class NameSpace(object):
        def __init__(self, prefix='', suffix='', separator=''):
            self.prefix = prefix
            self.suffix = suffix
            self.separator = separator
