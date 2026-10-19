

# Generated at 2022-06-13 00:09:57.122268
# Unit test for method collect of class CollectorMetaDataCollector
def test_CollectorMetaDataCollector_collect():
    import ansible.module_utils.facts.namespace
    collector_classes = {}
    namespace = ansible.module_utils.facts.namespace.PrefixFactNamespace(prefix='ansible_')
    filter_spec = ['*', 'facter*']
    gather_subset = ['all']
    gather_timeout = timeout.DEFAULT_GATHER_TIMEOUT
    minimal_gather_subset = frozenset()

    collector_classes = \
        collector.collector_classes_from_gather_subset(
            all_collector_classes=collector_classes,
            minimal_gather_subset=minimal_gather_subset,
            gather_subset=gather_subset,
            gather_timeout=gather_timeout)

    collectors = []

# Generated at 2022-06-13 00:10:00.552593
# Unit test for method collect of class CollectorMetaDataCollector
def test_CollectorMetaDataCollector_collect():
    collector_meta_data_collector = CollectorMetaDataCollector(gather_subset=['all'])
    meta_facts = collector_meta_data_collector.collect()
    assert 'gather_subset' in meta_facts


# Generated at 2022-06-13 00:10:04.146805
# Unit test for method collect of class CollectorMetaDataCollector
def test_CollectorMetaDataCollector_collect():
    meta_facts = CollectorMetaDataCollector(gather_subset="all", module_setup="true").collect()
    assert meta_facts == {'gather_subset': 'all', 'module_setup': 'true'}


# Generated at 2022-06-13 00:10:09.005826
# Unit test for method collect of class CollectorMetaDataCollector
def test_CollectorMetaDataCollector_collect():
    fact_collector = CollectorMetaDataCollector(namespace=None,
                                                gather_subset=None,
                                                module_setup=None)
    result = fact_collector.collect(collected_facts={})
    assert 'gather_subset' in result
    assert 'module_setup' in result



# Generated at 2022-06-13 00:10:16.978261
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    """Test the ansible fact collector"""

    # Create a mock fact collector to mock one single fact
    class MockFactCollector(collector.BaseFactCollector):
        name = 'my_fact'

        def collect(self, module=None, collected_facts=None):
            return {'my_fact': 'my_value'}

    # Create our ansible fact collector with the subset of facts to collect
    fact_collector = AnsibleFactCollector(collectors=[MockFactCollector()])

    # Collect the data
    facts = fact_collector.collect()

    # Make sure the method collect of class AnsibleFactCollector works
    assert facts == {'my_fact': 'my_value'}

# Generated at 2022-06-13 00:10:27.124931
# Unit test for method collect of class CollectorMetaDataCollector
def test_CollectorMetaDataCollector_collect():
    ''' Test the _collect method of CollectorMetaDataCollector '''

    # Initiate a CollectorMetaDataCollector object
    collector_meta_data_collector = CollectorMetaDataCollector()

    # Before module execution
    assert collector_meta_data_collector._fact_ids == set([])
    # Run the collector collect method
    assert collector_meta_data_collector.collect() == {'gather_subset': None, 'module_setup': None}
    # After module execution
    assert collector_meta_data_collector._fact_ids == set([])

# Generated at 2022-06-13 00:10:31.409064
# Unit test for method collect of class CollectorMetaDataCollector
def test_CollectorMetaDataCollector_collect():
    collector_meta_data_collector = \
        CollectorMetaDataCollector(gather_subset=['all'],
                                   module_setup=True)
    assert collector_meta_data_collector.collect() == {'module_setup': True, 'gather_subset': ['all']}

# Generated at 2022-06-13 00:10:42.473078
# Unit test for method collect of class CollectorMetaDataCollector
def test_CollectorMetaDataCollector_collect():
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    fact_collector = CollectorMetaDataCollector(gather_subset=['all'],
                                                module_setup=True,
                                                namespace=PrefixFactNamespace('VAR_'))
    fact_dict = fact_collector.collect()
    assert fact_dict == {'VAR_gather_subset': ['all'], 'VAR_module_setup': True}
    fact_collector = CollectorMetaDataCollector(gather_subset=['all'],
                                                namespace=PrefixFactNamespace('VAR_'))
    fact_dict = fact_collector.collect()
    assert fact_dict == {'VAR_gather_subset': ['all']}

# Generated at 2022-06-13 00:10:49.443845
# Unit test for method collect of class CollectorMetaDataCollector
def test_CollectorMetaDataCollector_collect():
    fact_collector = CollectorMetaDataCollector(gather_subset=['all', '!min'])
    collected_facts = fact_collector.collect()
    assert collected_facts is not None
    for k in ('module_setup', 'gather_subset'):
        assert collected_facts.get(k) is not None
    for v in ('all', '!min'):
        assert v in collected_facts['gather_subset']

# Generated at 2022-06-13 00:10:58.860963
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    import re
    import six
    import ansible.module_utils.facts.collector as collector

    assert six.PY2, 'do not use this test for python 3'

    class Collector1(collector.BaseFactCollector):

        name = 'collector1'
        _fact_ids = set([])

        def collect(self, module=None, collected_facts=None):
            return {'fact1': 1}

    class Collector2(collector.BaseFactCollector):

        name = 'collector2'
        _fact_ids = set([])

        def collect(self, module=None, collected_facts=None):
            return {'fact2': 2}

    all_collector_classes = {
        'collector1': Collector1,
        'collector2': Collector2,
    }

    # TOD

# Generated at 2022-06-13 00:11:17.271130
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    fact_collector = AnsibleFactCollector(collectors=[])

    collected_facts = {'a': 1}
    facts_dict = fact_collector.collect(module=None, collected_facts=collected_facts)

    assert facts_dict['ansible_facts'] == {}


# Generated at 2022-06-13 00:11:23.398615
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():

    # Create a dummy collector class
    class DummyCollector(collector.BaseFactCollector):
        def collect(self, module=None, collected_facts=None):
            return {'dummy1': 'value1', 'dummy2': 'value2'}

    fact_collector = \
        AnsibleFactCollector(collectors=[DummyCollector()])

    collected_facts = {}
    facts = fact_collector.collect(collected_facts=collected_facts)
    assert facts == {'dummy1': 'value1', 'dummy2': 'value2'}

# Generated at 2022-06-13 00:11:31.920298
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    fake_module = {}
    fake_facts = {}

    # create a collector_obj to be added to the list of collectors
    class fake_collector(collector.BaseFactCollector):
        def __init__(self, collectors=None, namespace=None):
            super(fake_collector, self).__init__(collectors, namespace)

        def collect(self, module=None, collected_facts=None):
            return {'fake_fact': 'fake_value'}

    fake_collector_obj = fake_collector()
    fake_collectors = [fake_collector_obj, fake_collector_obj]

    # Filter spec 'fake_fact'
    fact_collector1 = AnsibleFactCollector(collectors=fake_collectors,
                                           filter_spec='fake_fact')
    ansible_

# Generated at 2022-06-13 00:11:42.811849
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    import unittest
    import unittest.mock
    import ansible.module_utils.facts

    class TestFacts():
        def __init__(self, content=None):
            self.content = content

        def collect(self, module, collected_facts):
            return self.content

    # Construct a fact collection object, add 1 fact to the collection, and
    # test that the result of collect() on that object is the same as the
    # content added to the fact collection.  This test uses the
    # from_gather_subset() constructor.
    tfc = ansible.module_utils.facts.AnsibleFactCollector.from_gather_subset(['all'])
    tf = TestFacts({'dummy_fact': 'dummy_value'})

# Generated at 2022-06-13 00:11:50.286227
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    import ansible.module_utils.facts.collector
    import ansible.module_utils.facts.hardware
    import ansible.module_utils.facts.system
    import ansible.module_utils.facts.network
    import ansible.module_utils.facts.local

    all_collector_classes = \
        set(ansible.module_utils.facts.collector.ALL_COLLECTOR_CLASSES)
    get_ansible_collector(all_collector_classes)

# Generated at 2022-06-13 00:11:58.985775
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    from ansible.module_utils.facts import namespace
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.collector import collect_subset
    from ansible.module_utils.facts.collector import all_collector_classes
    from ansible.module_utils.facts.collector import is_valid_collector_name

    class p(BaseFactCollector):
        name = "p"

    class q(BaseFactCollector):
        name = "q"

    class r(BaseFactCollector):
        name = "r"

    class s(BaseFactCollector):
        name = "s"

    class t(BaseFactCollector):
        name = "t"

    class u(BaseFactCollector):
        name = "u"

    all

# Generated at 2022-06-13 00:12:10.846042
# Unit test for function get_ansible_collector
def test_get_ansible_collector():

    def _test(all_collector_classes,
              namespace=None,
              filter_spec=None,
              gather_subset=None,
              gather_timeout=None,
              minimal_gather_subset=None):

        fact_collector = get_ansible_collector(all_collector_classes=all_collector_classes,
                                               namespace=namespace,
                                               filter_spec=filter_spec,
                                               gather_subset=gather_subset,
                                               gather_timeout=gather_timeout,
                                               minimal_gather_subset=minimal_gather_subset)
        return fact_collector

    NAMESPACE_PREFIX = 'ansible_'

    # Example (not used)

# Generated at 2022-06-13 00:12:13.049969
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    # FIXME: This requires a working _cache module which we have failed to get working on all distros
    #        so test is disabled for now.
    pass



# Generated at 2022-06-13 00:12:25.088913
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    class _MyCollector(collector.BaseFactCollector):

        name = 'my_collector'
        _fact_ids = set([])

        def collect(self, module=None, collected_facts=None):
            return {'my_collector': {'my_fact': 'my_value'}}

    my_collector = _MyCollector()
    fact_collector = \
        AnsibleFactCollector(collectors=[my_collector],
                             filter_spec='*')

    result = fact_collector.collect()
    assert result == {'my_fact': 'my_value'}

    fact_collector = \
        AnsibleFactCollector(collectors=[my_collector],
                             filter_spec='my_collector.*')

    result = fact_collector.collect()
    assert result

# Generated at 2022-06-13 00:12:36.540287
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():

    # test for when there are no collectors
    fact_collector = AnsibleFactCollector(collectors=[])
    assert fact_collector.collect() == {}

    # Create a facts dict from collector object
    info_dict = {'test_fact_key': 'test_fact_value'}
    fact_collector = \
        AnsibleFactCollector(collectors=[collector.BaseFactCollector(namespace='test')])
    fact_collector.collectors[0].collect = lambda x, y: info_dict
    facts_dict = fact_collector.collect()
    assert facts_dict['test_fact_key'] == 'test_fact_value'

    # Create a facts dict from collector object with namespace
    info_dict = {'test_fact_key': 'test_fact_value'}
    fact_collector

# Generated at 2022-06-13 00:12:47.664553
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    from ansible.module_utils.facts import namespace
    subset = ['!foo', 'minimal', 'bar']
    ansible_collector = get_ansible_collector(all_collector_classes=[],
                                              filter_spec=[],
                                              gather_subset=subset)

    assert ansible_collector
    assert ansible_collector.collectors
    assert isinstance(ansible_collector.collectors[0], CollectorMetaDataCollector)
    assert ansible_collector.collectors[0].gather_subset == subset

    assert ansible_collector.namespace == None
    assert ansible_collector.filter_spec == []
    assert ansible_collector.collectors[0].namespace == None


# Generated at 2022-06-13 00:12:49.790934
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    collect_result = AnsibleFactCollector._collect()
    assert collect_result == dict()

# Generated at 2022-06-13 00:12:58.087204
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    fact_collector = get_ansible_collector(all_collector_classes=set(['TestCollector']),
                                           gather_subset=['all'],
                                           filter_spec=['*'])

    facts_dict = fact_collector.collect(collected_facts={})

    assert isinstance(facts_dict, dict), \
        "Incorrect type for facts_dict, expected {}, but got {}".format(dict, type(facts_dict))
    assert 'test_fact' in facts_dict, \
        "Missing test_fact"


# Generated at 2022-06-13 00:13:10.258770
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    import ansible.module_utils.facts.collector
    import ansible.module_utils.facts.namespace
    import ansible.module_utils.facts.system
    import ansible.module_utils.facts.network
    import ansible.module_utils.facts.distribution

    mock_module = None
    mock_collected_facts = {'ansible_system': 'Dummy'}

    ansible_fact_collector = \
        AnsibleFactCollector(collectors=[], namespace=None, filter_spec=None)

    mock_facts_dict = {'ansible_system': 'Dummy'}


# Generated at 2022-06-13 00:13:15.964298
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    all_collector_classes = [collector.NetworkCollector]
    filter_spec = ['net*']
    gather_subset = ['network']
    gather_timeout = 63
    minimal_gather_subset = frozenset()

    fact_collector = get_ansible_collector(all_collector_classes,
                                           filter_spec=filter_spec,
                                           gather_subset=gather_subset,
                                           gather_timeout=gather_timeout,
                                           minimal_gather_subset=minimal_gather_subset)
    assert type(fact_collector) == AnsibleFactCollector


# Generated at 2022-06-13 00:13:16.907119
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    assert get_ansible_collector()

# Generated at 2022-06-13 00:13:25.576691
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    import tempfile

    from ansible.module_utils.facts import cache

    # Setup
    cache_dir = tempfile.mkdtemp()
    cache.FACT_CACHE_PLUGIN = 'jsonfile'
    cache.FACT_CACHE_PLUGIN_CONNECTION = cache_dir
    cache.FACT_CACHE = cache.FactCache()

    mock_module = MagicMock()
    mock_module.params = {'gather_subset': ['all']}

    # Test
    fact_collector = AnsibleFactCollector()
    facts = fact_collector.collect(mock_module)
    assert 'all' == facts.get('ansible_facts.gather_subset')
    assert 'True' == facts.get('ansible_facts.module_setup')

# Generated at 2022-06-13 00:13:36.363477
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():

    # Define few demo collectors, we will not instantiate them and mock the collec_with_namespace method to
    # return test data
    class DummyCollector1:

        def collect_with_namespace(self, module, collected_facts):
            return {'dummy_collector1': 1}

    class DummyCollector2:

        def collect_with_namespace(self, module, collected_facts):
            return {'dummy_collector2': 2}

    class DummyCollector3:

        def collect_with_namespace(self, module, collected_facts):
            return {'dummy_collector3': 3}

    class DummyCollector4:

        def collect_with_namespace(self, module, collected_facts):
            return {'dummy_collector4': 4}


# Generated at 2022-06-13 00:13:46.412045
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    import collections
    import unit_tests.test_utils as test_utils

    # mock an ansible_facts module for testing
    class AnsibleFactCollectorTestModule(test_utils.AnsibleFactsModule):
        pass

    # mock a collector that returns 'fact_1' and 'fact_2'
    class SimpleFactCollector(collector.BaseFactCollector):
        name = 'simple'

        def collect(self, module=None, collected_facts=None):
            facts_dict = {}
            facts_dict['fact_1'] = {'attr1': 'value1'}
            facts_dict['fact_2'] = {'attr2': 'value2'}

            return facts_dict

    # mock a collector that returns 'fact_3' and 'fact_4'

# Generated at 2022-06-13 00:13:58.879453
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    class DummyCollector(object):
        def __init__(self, name, namespace=None):
            self.name = name
            self.namespace = namespace

        def collect(self, module=None, collected_facts=None):
            return {'dummy': {'test'}}

    class DummyCollectorWithError(object):
        def __init__(self, name, namespace=None):
            self.name = name
            self.namespace = namespace

        def collect(self, module=None, collected_facts=None):
            raise Exception('dummy collector failed')

    class DummyFactNamespace(object):
        def __init__(self, prefix, name):
            self.prefix = prefix
            self.name = name


# Generated at 2022-06-13 00:14:08.519639
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    import ansible.module_utils.facts.network
    import ansible.module_utils.facts.system

    all_collector_classes = [ansible.module_utils.facts.network.NetworkFactCollector,
                             ansible.module_utils.facts.system.SystemFactCollector]

    fact_collector = get_ansible_collector(all_collector_classes,
                                           namespace=None,
                                           filter_spec=None,
                                           gather_subset=['all', '*'],
                                           gather_timeout=None,
                                           minimal_gather_subset=frozenset())

    assert isinstance(fact_collector, AnsibleFactCollector)

# Generated at 2022-06-13 00:14:18.436729
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    from ansible.module_utils.facts.namespace import PrefixFactNamespace

    import ansible.module_utils.facts.hardware.mac_utils
    import ansible.module_utils.facts.hardware.ec2

    import ansible.module_utils.facts.system.platform
    import ansible.module_utils.facts.system.distribution
    import ansible.module_utils.facts.system.user

    import ansible.module_utils.facts.virtual.virtualbox
    import ansible.module_utils.facts.virtual.kvm
    import ansible.module_utils.facts.virtual.xenserver
    import ansible.module_utils.facts.virtual.vmware

    import ansible.module_utils.facts.network.interfaces


# Generated at 2022-06-13 00:14:27.491723
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    import ansible.module_utils.facts.namespace as nmsp
    collect_nmsp = nmsp.NamespaceCollector(prefix='ansible_')

    ansible_collector = get_ansible_collector(all_collector_classes=[collect_nmsp],
                                              gather_timeout=0,
                                              gather_subset=['network'],
                                              namespace=collect_nmsp)

    facts = ansible_collector.collect()

    assert facts['ansible_facts']['ansible_interface_macs'] == facts['interface_macs']

# Generated at 2022-06-13 00:14:33.994983
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():

    class FakeCollector1(object):
        def collect(self, module=None, collected_facts=None):
            collected_facts['a'] = 'A'
            return collected_facts

    class FakeCollector2(object):
        def collect(self, module=None, collected_facts=None):
            collected_facts['b'] = 'B'
            return collected_facts

    fc1 = FakeCollector1()
    fc2 = FakeCollector2()

    afc = AnsibleFactCollector(collectors=[fc1, fc2])
    facts = afc.collect()
    assert facts['a'] == 'A'
    assert facts['b'] == 'B'


# Generated at 2022-06-13 00:14:42.432390
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    from ansible.utils.collection_loader import collect_subset
    all_collector_classes = collect_subset('all')
    fact_collector = get_ansible_collector(all_collector_classes,
                                           gather_subset=['hardware'],
                                           minimal_gather_subset=frozenset(['kernel']))
    assert len(fact_collector.collectors) == 3
    assert len(fact_collector.namespace.namespaces) == 0


# Generated at 2022-06-13 00:14:52.208250
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():

    # Helper class to test AnsibleFactCollector
    class MockFacterBaseFactCollector(collector.BaseFactCollector):
        def collect(self, module=None, collected_facts=None):
            return {'facter_test': 'facter_test'}

        def __init__(self, *args, **kwargs):
            super(MockFacterBaseFactCollector, self).__init__(*args, **kwargs)

    # Helper class to test AnsibleFactCollector
    class MockOhaiBaseFactCollector(collector.BaseFactCollector):
        def collect(self, module=None, collected_facts=None):
            collected_facts = collected_facts or {}
            collected_facts = {'ohai_test': 'ohai_test'}
            return collected_facts


# Generated at 2022-06-13 00:14:58.175613
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    import ansible.module_utils.facts.collector.platform
    from ansible.module_utils.facts.namespace import PrefixFactNamespace

    filter_spec = 'ansible_os*'
    namespace = PrefixFactNamespace(prefix='ansible_')
    collector = AnsibleFactCollector(collectors=None,
                                     namespace=namespace,
                                     filter_spec=filter_spec)

    # pylint: disable=protected-access
    # 1. Get all possible facts
    collector._collectors = [ansible.module_utils.facts.collector.platform.PlatformFactCollector()]
    facts = collector.collect()

    # Check that the filter_spec is respected
    assert 'ansible_os_version_maj' in facts
    assert 'os_version_maj' not in facts

    #

# Generated at 2022-06-13 00:15:10.101858
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    from ansible.module_utils.facts.namespace import PrefixFactNamespace

    # Define a mock that collects a dict that contains ansible, facter and ohai keys/value pairs
    class MyCollector(collector.Collector):
        name = 'MyCollector'

        def collect(self, module=None, collected_facts=None):
            my_fact = {}
            my_fact['ansible_foo'] = 'AnsibleFoo'
            my_fact['ansible_bar'] = 'AnsibleBar'
            my_fact['facter_foo'] = 'FacterFoo'
            my_fact['ohai_foo'] = 'OhaiFoo'
            return my_fact

    def my_assert(condition, msg):
        if not condition:
            raise AssertionError(msg)

    #

# Generated at 2022-06-13 00:15:21.186397
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    from ansible.module_utils.facts import namespace

    all_collector_classes = collector.all_collector_classes()
    namespace_obj = namespace.PrefixFactNamespace(prefix='ansible_')
    fact_collector = \
        get_ansible_collector(all_collector_classes=all_collector_classes,
                              namespace=namespace_obj,
                              gather_subset='all')

    assert(isinstance(fact_collector, (AnsibleFactCollector)))

# To enable unit test for this module: python -m testtools.run tests.unit.module_utils.facts.test_ansible_fact_collector
# To run all unit test for this directory: python -m testtools.run tests.unit.module_utils.facts

# Generated at 2022-06-13 00:15:28.593283
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    from ansible.module_utils.facts.ansible_collection import AnsibleDistribution
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    import ansible.module_utils.facts.collector.network

    ansible_distro = AnsibleDistribution(distribution=None, major_version=None,
                                         minor_version=None)
    ansible_distro_collector = ansible.module_utils.facts.collector.network.AnsibleDistribution(namespace=ansible_distro)
    subset_collector = ansible.module_utils.facts.collector.network.GatherSubset(namespace=ansible_distro)


# Generated at 2022-06-13 00:15:52.954264
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    from importlib import import_module
    from ansible.module_utils.facts import ansible_collector
    from ansible.module_utils.facts.network.base import BaseNetworkCollector
    from ansible.module_utils.facts.overrides import overrides
    from ansible.module_utils.facts.system.base import BaseSystemCollector
    # Have to import AnsibleFactCollector here, as it is defined below import_module
    from ansible.module_utils.facts.cache import FactCache
    # Have to import modules explicitly here, because they are not imported in module directly
    import_module('ansible.module_utils.facts.namespace')
    import_module('ansible.module_utils.facts.system.distribution')
    import_module('ansible.module_utils.facts.cache.file')
    import_

# Generated at 2022-06-13 00:16:00.392351
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():

    class TestCollector(collector.BaseFactCollector):
        name = 'test'

        def collect(self, module=None, collected_facts=None):
            return {
                'foo': 'a',
                'bar': 'b',
                'baz': 'c',
            }

    fact_collector = AnsibleFactCollector(collectors=[TestCollector()])
    facts = fact_collector.collect()
    assert facts == {
        'foo': 'a',
        'bar': 'b',
        'baz': 'c',
    }

    fact_collector = AnsibleFactCollector(collectors=[TestCollector()], filter_spec='*')
    facts = fact_collector.collect()

# Generated at 2022-06-13 00:16:09.518702
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    '''Unit test for function get_ansible_collector'''
    # pylint: disable=import-error
    from ansible.module_utils.facts.system.base import BaseFactCollector

    class MyCollector(BaseFactCollector):
        '''Base class for MyCollector, which won't be used.'''
        def collect(self, module=None, collected_facts=None):
            return {}

    class MyFactCollector(BaseFactCollector):
        '''A sample fact collector that returns data based on the gather_subset.'''
        def collect(self, module=None, collected_facts=None):
            facts_dict = {}

# Generated at 2022-06-13 00:16:18.184822
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    all_collector_classes = [
        collector.AllSubsetCollector,
        collector.NetworkCollector,
        collector.HardwareCollector,
        collector.VirtualCollector
    ]

    gather_subset = ['all', 'min']
    minimal_gather_subset = frozenset(['all', 'min'])

    fact_collector = get_ansible_collector(all_collector_classes,
                                           gather_subset=gather_subset,
                                           namespace=None,
                                           filter_spec=None,
                                           minimal_gather_subset=minimal_gather_subset)
    facts = fact_collector.collect()
    assert(facts.get('ansible_all_ipv4_addresses') is not None)

# Generated at 2022-06-13 00:16:29.999611
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    class MockCollector(collector.Collector):
        '''Mock Collector to be used to test AnsibleFactCollector'''

        name = 'mock'
        _fact_ids = set([])

        def collect_with_namespace(self, module=None, collected_facts=None):
            return {self.namespace.namespace_prefix + 'mock1': 1,
                    'ansible_mock2': 2,
                    'ansible_mock3': 3,
                    'ansible_facter_mock4': 4,
                    'ansible_ohai_mock5': 5,
                    'facter_mock6': 6}

    class MockEmptyCollector(collector.Collector):
        '''Mock Collector to be used to test AnsibleFactCollector'''

        name = 'mock'

# Generated at 2022-06-13 00:16:36.382940
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    from ansible.module_utils.facts import collector
    import ansible.module_utils.facts.network.interfaces
    import ansible.module_utils.facts.system
    import ansible.module_utils.facts.virtual

    all_collectors = collector.get_collector_classes(collector.FACT_CACHE)

    gather_subset = ['all', 'network']
    minimal_gather_subset = frozenset(('min',))

    ansible_collector = \
        get_ansible_collector(all_collectors,
                              gather_subset=gather_subset,
                              minimal_gather_subset=minimal_gather_subset)

    import pprint
    pprint.pprint(ansible_collector.collect())



# Generated at 2022-06-13 00:16:42.754951
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    from ansible.module_utils.facts import collectors

    all_collector_classes = [collectors.NetworkCollector]
    fact_collector = get_ansible_collector(all_collector_classes)
    facts_dict = fact_collector.collect()

    assert facts_dict['ansible_all_ipv4_addresses']
    assert 'ansible_os_family' in facts_dict



# Generated at 2022-06-13 00:16:49.889219
# Unit test for function get_ansible_collector
def test_get_ansible_collector():

    class TestCollector1(collector.BaseFactCollector):
        name = 'test1'
        _fact_ids = set(['test1'])

        def collect(self, module=None, collected_facts=None):
            return {'test1': 'fake_test1_fact'}

    class TestCollector2(collector.BaseFactCollector):
        name = 'test2'
        _fact_ids = set(['test2'])

        def collect(self, module=None, collected_facts=None):
            return {'test2': 'fake_test2_fact'}

    test_collector_classes = [TestCollector1, TestCollector2]

    # Test case 1
    #   gather_subset: ['test1']
    #   filter_spec: []
    #   namespace: None


# Generated at 2022-06-13 00:17:00.502427
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    import unittest

    class DummyFactCollector(collector.BaseFactCollector):
        '''A Dummy FactCollector class'''
        name = 'dummy'

        def collect(self, module=None, collected_facts=None):
            return {'dummy_fact': 'dummy_fact_value'}

    class WrongDummyFactCollector(collector.BaseFactCollector):
        '''A Dummy FactCollector class'''
        name = 'dummy'

        def collect(self, module=None, collected_facts=None):
            return {'dummy_fact': 'dummy_fact_value'}

    class MyError(Exception):
        pass
        # TODO: add msg to constructor, and stringify it in __str__


# Generated at 2022-06-13 00:17:06.364246
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():

    facts_dict = {'a': '1', 'b': '2', 'c': '3'}

    class MockCollector(collector.BaseFactCollector):
        def collect(self, module=None, collected_facts=None):
            return facts_dict

    fact_collector = \
        AnsibleFactCollector(collectors=[MockCollector()])

    facts = fact_collector.collect()

    assert facts == facts_dict

# Generated at 2022-06-13 00:17:32.921021
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    import ansible.module_utils.facts.namespace as namespace

    # Standup a class with a single namespace (on collect_with_namespace)
    # and a single fact that does not have a namespace prefix
    class TestAnsibleFactCollector1(AnsibleFactCollector):
        def __init__(self):
            self._fact_ids = set(['test_fact'])
            self._collectors = []

        def collect_with_namespace(self, module=None, collected_facts=None):
            return {'test_fact': 'aaa'}

    test_collector = TestAnsibleFactCollector1()
    test_result = test_collector.collect()

    assert test_result == {'test_fact': 'aaa'}

    # Standup a class with two namespaces (on collect_with_

# Generated at 2022-06-13 00:17:40.527073
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    from ansible.module_utils.facts.collector.base import BaseFactCollector

    class MockCollector(BaseFactCollector):
        name = 'mock'

        def collect(self, module=None, collected_facts=None):
            return {'test_this': '5'}

    fact_collector = AnsibleFactCollector(collectors=[MockCollector()])

    result = fact_collector.collect()
    assert result == {'test_this': '5'}


# Generated at 2022-06-13 00:17:41.093819
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    pass

# Generated at 2022-06-13 00:17:51.004787
# Unit test for function get_ansible_collector
def test_get_ansible_collector():

    import ansible.module_utils.facts.system
    import ansible.module_utils.facts.network

    filter_spec = filter_spec or []
    gather_subset = gather_subset or ['!all']
    gather_timeout = gather_timeout or timeout.DEFAULT_GATHER_TIMEOUT
    minimal_gather_subset = minimal_gather_subset or frozenset()

    all_fact_collector_classes = \
        set(ansible.module_utils.facts.system.__dict__.values()) | \
        set(ansible.module_utils.facts.network.__dict__.values())


# Generated at 2022-06-13 00:18:02.492100
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    from ansible.module_utils.facts import namespace

    # Test with no collectors
    afc = AnsibleFactCollector(collectors=[], namespace=None)
    result = afc.collect()
    assert result == {}

    # Test with one collector that returns an empty dictionary
    def c1_collect(module=None, collected_facts=None):
        return {}

    class C1(object):
        def collect(self, module=None, collected_facts=None):
            return c1_collect(module=module, collected_facts=collected_facts)

    c1 = C1()
    afc = AnsibleFactCollector(collectors=[c1], namespace=None)
    result = afc.collect()
    assert result == {}

    # Test with one collector that returns a dictionary with a single key

# Generated at 2022-06-13 00:18:13.928052
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    import ansible.module_utils.facts.cache
    import ansible.module_utils.facts.collector
    import ansible.module_utils.facts.namespace
    import ansible.module_utils.facts.system

    fact_collector = AnsibleFactCollector(collectors=[])
    assert fact_collector.collect() == {}
    assert fact_collector.collect(filter_spec=None) == {}
    assert fact_collector.collect(filter_spec=[]) == {}
    assert fact_collector.collect(filter_spec="") == {}
    assert fact_collector.collect(filter_spec="*") == {}


# Generated at 2022-06-13 00:18:14.488464
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    pass

# Generated at 2022-06-13 00:18:24.472723
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    # Example collector that returns a dummy fact for each call
    # It's not a real fact collector
    class DummyCollector(collector.BaseFactCollector):
        name = 'dummy'

        def collect(self, module=None, collected_facts=None):
            return {self.name: 1}

    # 'dummy-1' and 'dummy-2' are two collectors of type DummyCollector
    collectors = [DummyCollector('dummy-1'), DummyCollector('dummy-2')]

    fact_collector = AnsibleFactCollector(collectors=collectors)

    facts_dict = fact_collector.collect()

    assert facts_dict.get('dummy-1') == 1
    assert facts_dict.get('dummy-2') == 1



# Generated at 2022-06-13 00:18:34.969462
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    from ansible.module_utils.facts import timeout
    from ansible.module_utils.facts.collector.base import BaseFactCollector
    from ansible.module_utils.facts.collector.network import NetworkCollector

    assert issubclass(get_ansible_collector(all_collector_classes=[NetworkCollector],
                                            gather_subset=['network']).collectors[0].__class__,
                      BaseFactCollector)

    assert get_ansible_collector(all_collector_classes=[NetworkCollector],
                                 gather_subset=['network']).collectors[0].gather_subset == ['network']


# Generated at 2022-06-13 00:18:41.740389
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():

    # build collectors
    class Collector1:

        name = 'collector1'

        def collect(self, module=None, collected_facts=None):
            collected_facts = collected_facts or {}
            info_dict = dict(a=1, b=2)
            return info_dict

    class Collector2:

        name = 'collector2'

        def collect(self, module=None, collected_facts=None):
            collected_facts = collected_facts or {}
            info_dict = dict(c=3, d=4)
            return info_dict

    class Namespace:
        is_empty = False

        def __init__(self, prefix=None):
            self.prefix = prefix

        def should_prefixed(self):
            return self.prefix is not None

        def prefixed(self, key):
            return

# Generated at 2022-06-13 00:19:26.958449
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    def fake_collect(self, module=None, collected_facts=None):
        return {'a': 'A', 'b': 'B'}
    class FakeCollector(object):
        collect = fake_collect
    fake_fact_collector = AnsibleFactCollector(collectors=[FakeCollector()])

    results = fake_fact_collector.collect()

    assert results == {'a': 'A', 'b': 'B'}

# Generated at 2022-06-13 00:19:35.897498
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    '''Unit test for method collect of class AnsibleFactCollector
    '''
    from ansible.module_utils.facts.collector import TestFactCollector

    test_fact_collector = TestFactCollector()
    fact_collector = AnsibleFactCollector()

    collected_facts = None

    fact_collector.gather(fact_collector.collect(collected_facts=collected_facts))
    assert fact_collector.facts['test_fact'] == 'ok'

    collected_facts = {'test_fact': 'ko'}
    facts = fact_collector.collect(collected_facts=collected_facts)
    assert collected_facts != facts


# Unit Test for method collect of class CollectorMetaDataCollector