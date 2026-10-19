

# Generated at 2022-06-13 00:09:55.547541
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    from ansible.module_utils.facts import ansible_collector

    fact_collector = get_ansible_collector(
        all_collector_classes=ansible_collector.FACT_SUBSETS['all'],
        gather_subset=['!all', 'network'],
        filter_spec=['ansible_os_family', 'ansible_distribution'],
        gather_timeout=1,
        minimal_gather_subset=ansible_collector.FACT_SUBSETS['!all'])

    # This is testing the embedded CollectorMetaDataCollector
    # is in fact_collector.collectors
    assert isinstance(fact_collector.collectors[-1], CollectorMetaDataCollector)

    # This is testing that the filter spec was applied to the facts
    # correctly.
    facts

# Generated at 2022-06-13 00:09:56.545170
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    # TODO: Write unit test
    pass

# Generated at 2022-06-13 00:10:07.315660
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts import networking
    from ansible.module_utils.facts.utilities import get_file_lines
    from ansible.module_utils.facts import software
    import os

    collector_classes = [networking.NetworkCollector,
                         software.DpkgCollector,
                         software.RedHatReleaseCollector,
                         software.LinuxDistributionCollector]

    def count_lines_in_file(filename):
        try:
            return len(list(get_file_lines(filename)))
        except IOError:
            return 0


# Generated at 2022-06-13 00:10:15.414905
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    from ansible.module_utils.facts import default
    from ansible.module_utils.facts.namespace import PrefixFactNamespace

    collector_a = default.FactsCollector()
    collector_b = default.FactsCollector()

    collector_a_with_namespace = \
        PrefixFactNamespace(collector_a, namespace='ansible_')
    collector_b_with_namespace = \
        PrefixFactNamespace(collector_b, namespace='ansible_')

    fact_collector = AnsibleFactCollector(collectors=[collector_a_with_namespace,
                                                      collector_b_with_namespace],
                                          filter_spec=['*'],
                                          namespace='ansible_')

    facts = fact_collector.collect()

# Generated at 2022-06-13 00:10:16.038308
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    pass

# Generated at 2022-06-13 00:10:21.353043
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    fact_collector = get_ansible_collector(all_collector_classes=collector.ALL_COLLECTOR_CLASSES)
    assert(type(fact_collector) == AnsibleFactCollector)
    assert(type(fact_collector.collectors[0]) == collector.FacterFactCollector)

# Generated at 2022-06-13 00:10:32.978432
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    '''A unit test that tests the method collect of AnsibleFactCollector class.
    It tests two cases, one when the filter_spec is empty, and another one when there
    is already one entry in the filter_spec.
    '''
    facts = {
        'test_fact': 'test_val',
        'test_fact_2': 'test_val_2',
    }

    class MockCollector:
        def collect(self):
            return facts

    class AnotherMockCollector:
        def collect(self):
            return facts

    collectors = [MockCollector(), AnotherMockCollector()]

    afc = AnsibleFactCollector(collectors=collectors,
                               filter_spec=None)

    facts_dict = afc.collect()

    assert facts_dict == facts


# Generated at 2022-06-13 00:10:45.225998
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    import ansible
    import ansible.module_utils.facts.collector

    import ansible.module_utils.facts.cache

    import ansible.module_utils.facts.system

    import ansible.module_utils.facts.system.distribution
    import ansible.module_utils.facts.system.pkg_mgr
    import ansible.module_utils.facts.system.platform
    import ansible.module_utils.facts.system.profile
    import ansible.module_utils.facts.system.selinux
    import ansible.module_utils.facts.system.service_mgr
    import ansible.module_utils.facts.system.users
    import ansible.module_utils.facts.virtual
    import ansible.module_utils.facts.network

    # It requires only the facts collector to be run (except the

# Generated at 2022-06-13 00:10:55.664806
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    import ansible.module_utils.facts.network.ios

    module = {}
    all_collector_classes = [
        ansible.module_utils.facts.network.ios.IOSFactCollector,
    ]
    # Arrange
    fact_collector = \
        get_ansible_collector(
            all_collector_classes=all_collector_classes,
            namespace=None,
            filter_spec=None,
            gather_subset=['!all'],
            gather_timeout=None,
            minimal_gather_subset=frozenset())

    # Act
    facts_dict = fact_collector.collect(module=module)

    # Assert
    assert len(facts_dict) > 0

# Generated at 2022-06-13 00:11:00.794760
# Unit test for function get_ansible_collector
def test_get_ansible_collector():

    import ansible.module_utils.facts
    all_collector_classes = ansible.module_utils.facts.collectors.all_collector_classes

    collector = get_ansible_collector(all_collector_classes=all_collector_classes)

    assert collector is not None



# Generated at 2022-06-13 00:11:17.837806
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    import unittest
    import copy

    class TestCollector(collector.BaseFactCollector):

        name = 'test1'
        _fact_id = 'test1_id'

        def collect(self, module=None, collected_facts=None):
            return {'test1': 'test1'}

    class TestCollector2(collector.BaseFactCollector):

        name = 'test2'
        _fact_id = 'test2_id'

        def collect(self, module=None, collected_facts=None):
            return {'test2': 'test2'}

    class TestNamespace(collector.BaseFactNamespace):

        name = 'test'

    class TestCollect(unittest.TestCase):

        def setUp(self):

            self.namespace = TestNamespace()

            self

# Generated at 2022-06-13 00:11:25.168479
# Unit test for function get_ansible_collector
def test_get_ansible_collector():

    from ansible.module_utils.facts import network

    all_collector_classes = collector.get_collector_class_map()

    gather_subset = ['!all', 'network', 'facter']

    fact_collector = get_ansible_collector(all_collector_classes,
                                           gather_subset=gather_subset,
                                           namespace='ansible_',
                                           filter_spec=['*ipv*', 'ansible_machine_id'])

    assert len(fact_collector.collectors) == 3
    fact_collector.collectors[0] == CollectorMetaDataCollector
    fact_collector.collectors[1] == network.NetworkCollector
    fact_collector.collectors[2] == CollectorMetaDataCollector

# Generated at 2022-06-13 00:11:33.839272
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    from ansible.module_utils.facts.collector.default import DefaultFactCollector
    from ansible.module_utils.facts.namespace import PrefixFactNamespace

    test_fact_collector = AnsibleFactCollector()
    test_fact_collector.collectors = [DefaultFactCollector(namespace=PrefixFactNamespace(prefix='ansible_'))]
    # Add a collector that knows what gather_subset we used so it it can provide a fact
    test_collector_meta_data_collector = CollectorMetaDataCollector(gather_subset=['all'],
                                                                     module_setup=True)

    test_fact_collector.collectors.append(test_collector_meta_data_collector)

# Generated at 2022-06-13 00:11:45.524392
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    import ansible.module_utils.facts.collector
    import ansible.module_utils.facts.gather
    import ansible.module_utils.facts.other
    import ansible.module_utils.facts.system
    import ansible.module_utils.facts.virtual
    import ansible.module_utils.facts.network

    def test_get_collectors(subset='all',
                            timeout=timeout.DEFAULT_GATHER_TIMEOUT,
                            minimal_subset=None,
                            namespace=None):
        import json
        import pprint

        print('gather_subset=%s' % (subset,))
        print('timeout=%s' % timeout)
        print('minimal_subset=%s' % (minimal_subset,))

# Generated at 2022-06-13 00:11:56.569288
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    from ansible.module_utils.facts import ansible_collector
    from ansible.module_utils.facts import namespaces
    from ansible.module_utils.facts import cache
    from ansible.module_utils.facts import timeout

    # make sure collector for 'ansible_*' facts are loaded even if not in gather_subset
    class AnsibleFactsCollector(ansible_collector.BaseFactCollector):
        name = 'ansible_facts'

        def __init__(self, namespace=None):
            super(AnsibleFactsCollector, self).__init__(namespace=namespace)

        def collect(self, module=None, collected_facts=None):
            return {'ansible_facts': 'foo'}

    all_collector_classes = [AnsibleFactsCollector,]



# Generated at 2022-06-13 00:12:08.321561
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():

    from ansible.module_utils.facts import gather

    from ansible.module_utils.facts import collection

    import subprocess

    # helper function to run a single fact collection, provided
    # the module_utils/facts/ path has coverage for the given fact
    # module
    def test_fact(fact_module, mock_collector_return_value,
                  filter_spec=None,
                  collect_all_facts=True):

        mock_collector_class = type(fact_module + 'FactorCollector',
                                    (object,),
                                    {'collect': lambda self, module, collected_facts:
                                    mock_collector_return_value})

        mock_collector = mock_collector_class()

        # run an individual fact collection
        # this should return the dictionary returned by the mock_collector
        fact_collect

# Generated at 2022-06-13 00:12:15.191222
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    fact_collector = get_ansible_collector(all_collector_classes=collector.get_collector_classes(),
                                           filter_spec=['ansible_*'],
                                           gather_subset=['all'],
                                           gather_timeout=15,
                                           minimal_gather_subset=['all'])

    facts = fact_collector.collect()
    assert facts['gather_subset'] == ['all']
    assert facts['module_setup'] == True
    for fact in facts.keys():
        assert fact.startswith('ansible_')

# Generated at 2022-06-13 00:12:27.901842
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    """Test get_ansible_collector function."""
    all_collectors = [collector.FacterCollector, collector.OhaiCollector, collector.NetworkCollector,
                      collector.VirtualizationCollector, collector.HardwareCollector, collector.OpenStackCollector]

    gather_subset = ['hardware', 'all']
    minimal_gather_subset = frozenset({'all'})
    gather_timeout = 10
    namespace = 'ansible'

    ansible_collector = get_ansible_collector(
        all_collector_classes=all_collectors,
        gather_subset=gather_subset,
        minimal_gather_subset=minimal_gather_subset,
        gather_timeout=gather_timeout,
        namespace=namespace)

    assert ansible_collector

# Generated at 2022-06-13 00:12:39.259721
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    from ansible.module_utils.facts import anspath
    from ansible.module_utils.facts.system.distribution import DistributionFactCollector
    from ansible.module_utils.facts.system.distribution import RedHatFactCollector
    from ansible.module_utils.facts.system.distribution import DebianFactCollector
    from ansible.module_utils.facts.system.distribution import AlpineFactCollector
    from ansible.module_utils.facts.system.distribution import GentooFactCollector
    from ansible.module_utils.facts.system.distribution import SuseFactCollector
    from ansible.module_utils.facts.system.distribution import LinuxFactCollector
    from ansible.module_utils.facts.system.distribution import SysVInitFactCollector

# Generated at 2022-06-13 00:12:39.814037
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    pass

# Generated at 2022-06-13 00:12:58.511627
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():

    class MockCollectorClass:
        '''A mock collector class'''

        def __init__(self, namespace=None):
            self.namespace = namespace
            self.name = 'MockCollector'

        def collect_with_namespace(self, collected_facts=None, module=None):
            facts = {}
            if self.namespace is not None:
                facts['namespace'] = self.namespace

            facts['mock_facts'] = 'MOCK'
            return facts

    class MockWithoutNamespaceCollectorClass:
        '''A mock collector class'''

        def __init__(self, namespace=None):
            self.namespace = namespace
            self.name = 'MockWithoutNamespaceCollector'


# Generated at 2022-06-13 00:13:10.904249
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    import ansible.module_utils.facts.network.linux as linux
    import ansible.module_utils.facts.network.netbsd as netbsd
    import ansible.module_utils.facts.network.sunos as sunos
    import ansible.module_utils.facts.network.aix as aix
    import ansible.module_utils.facts.network.bsd as bsd
    import ansible.module_utils.facts.network.hardware as hardware
    import ansible.module_utils.facts.network.ios as ios


# Generated at 2022-06-13 00:13:22.128112
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():

    # class that provides a fact named 'network'
    class NetworkCollector(collector.BaseFactCollector):
        name = 'network'

        def collect(self, module=None, collected_facts=None):
            return {'network': 'some value'}

    # class that collects some fact not in the filter_spec
    class SomeFactCollector(collector.BaseFactCollector):
        name = 'some_fact'

        def collect(self, module=None, collected_facts=None):
            return {'some_fact': 'some value'}

    # Test filter_spec == '*'
    fact_collector = \
        AnsibleFactCollector(filter_spec='*',
                             collectors=[NetworkCollector()])
    facts_dict = fact_collector.collect()
    print(facts_dict)

# Generated at 2022-06-13 00:13:28.974077
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    # NOTE: for now, just test that it doesn't crash
    from ansible.module_utils.facts.collector import \
        BaseFactCollector, \
        NetworkFactCollector
    from ansible.module_utils.facts.system.distribution import DistributionFactCollector

    all_collector_classes = [
        # BaseFactCollector,  # NOTE: not intended to be added
        # NetworkFactCollector,  # NOTE: not intended to be added
        DistributionFactCollector
    ]

    # NOTE: fact_collector object is unused here, just making sure it doesn't crash
    fact_collector = get_ansible_collector(all_collector_classes)
    fact_collector = get_ansible_collector(all_collector_classes,
                                           namespace='ansible_')
    fact_collector

# Generated at 2022-06-13 00:13:38.764187
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():

    # fake facts
    fact_a = {'a': 'a'}
    fact_b = {'b': 'b'}

    # fake result
    result = {}

    # fake collectors
    class FakeCollector(object):
        pass

    obj1 = FakeCollector()
    obj1.collect = lambda x, y: fact_a
    obj2 = FakeCollector()
    obj2.collect = lambda x, y: fact_b

    # test AnsibleFactCollector
    collector_ansible = AnsibleFactCollector(collectors=[obj1, obj2])
    collector_ansible.collect(result)
    assert result == {'ansible_facts': fact_a, 'b': 'b'}

    # test AnsibleFactCollector with namespace

# Generated at 2022-06-13 00:13:48.564008
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    '''Unit test for method collect of class AnsibleFactCollector'''

    # NOTE: the collector.FacterFactCollector and CollectrMetaDataCollector are
    # just test classes that return a fixed list of facts and a gather_subset
    # but they will call the collect method of the subclass
    all_collector_classes = [collector.FacterFactCollector,
                             CollectorMetaDataCollector]

    # get a instance of the AnsibleFactCollector with the FacterFactCollector and CollectorMetaDataCollector

# Generated at 2022-06-13 00:13:59.844646
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    from ansible.module_utils.facts.system.distribution import DistributionFactCollector
    from ansible.module_utils.facts.system.distribution import LinuxDistributionFactCollector
    from ansible.module_utils.facts.system.distribution import SystemReleaseFactCollector

    collect_all_collectors = \
        [DistributionFactCollector,
         LinuxDistributionFactCollector,
         SystemReleaseFactCollector]

    ansible_fact_collector = \
        AnsibleFactCollector(collectors=collect_all_collectors,
                             namespace=None)
    ansible_facts = ansible_fact_collector.collect()
    assert 'distribution' in ansible_facts
    assert ansible_facts['distribution'] == 'RedHat'

# Generated at 2022-06-13 00:14:08.434716
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    import ansible.module_utils.facts.namespace as namespace
    from ansible.module_utils.facts import cache
    from ansible.module_utils.facts.collector.network import NetworkFactCollector
    from ansible.module_utils.facts.collector.hardware import HardwareCollector

    all_collector_classes = [NetworkFactCollector, HardwareCollector]
    namespace_prefix = 'test_'

    fact_collector = get_ansible_collector(all_collector_classes,
                                           namespace=namespace.PrefixFactNamespace(namespace_prefix),
                                           gather_subset=['!all', 'network'])

    # Ensure we get the expected number of collectors
    assert len(fact_collector.collectors) == 2

    # Ensure we get an ansible_facts collector with the expected

# Generated at 2022-06-13 00:14:18.436111
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    def fake_collect(module=None, collected_facts=None):
        return {'key1': {'value1': 1},
                'key2': {'value2': 2}}

    def fake_collect_with_namespace(module=None, collected_facts=None):
        return {'namespace1': fake_collect()}

    class FakeCollector(object):
        def __init__(self, namespace=None):
            self.namespace = namespace

        def collect(self, module=None, collected_facts=None):
            return fake_collect()

        def collect_with_namespace(self, module=None, collected_facts=None):
            return fake_collect_with_namespace()


# Generated at 2022-06-13 00:14:24.217449
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    from ansible.module_utils.facts import cache
    from ansible.module_utils.facts import system
    from ansible.module_utils.facts import virtual
    from ansible.module_utils.facts import network
    from ansible.module_utils.facts import hardware
    from ansible.module_utils.facts.collector import \
        AnsibleFactCollector as FACTCOLLECTOR

    all_collector_classes = {'cache': cache,
                             'system': system,
                             'virtual': virtual,
                             'network': network,
                             'hardware': hardware}
    expected_gather_subset = ['all']
    gather_subset = ['all']
    gather_timeout = timeout.DEFAULT_GATHER_TIMEOUT
    minimal_gather_subset = frozenset()

    fact_collect

# Generated at 2022-06-13 00:14:36.335543
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    # Arrange
    class MetaDataCollector(collector.BaseFactCollector):
        name = 'gather_subset'

        def collect(self, module=None, collected_facts=None):
            meta_facts = {'gather_subset': ['all']}
            return meta_facts

    class AnotherMetaDataCollector(collector.BaseFactCollector):
        name = 'another_subset'

        def collect(self, module=None, collected_facts=None):
            meta_facts = {'gather_subset': ['another']}
            return meta_facts

    fact_collector = AnsibleFactCollector(collectors=[MetaDataCollector(), AnotherMetaDataCollector()])

    # Act
    collected_facts  = fact_collector.collect()
    # Assert

# Generated at 2022-06-13 00:14:47.936351
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    from ansible.module_utils.facts.namespace import Namespace
    from ansible.module_utils.facts.test import TestCollector, TestCollector2

    collector_obj = TestCollector()
    collector_obj_2 = TestCollector2()
    collector = AnsibleFactCollector(collectors=[collector_obj, collector_obj_2])

    facts = collector.collect()
    assert facts['test_fact'] == 'test_fact_value'
    assert facts['test_fact2'] == 'test_fact2_value'

    # Test with namespace
    namespace_obj = Namespace('some_namespace')
    collector = AnsibleFactCollector(collectors=[collector_obj, collector_obj_2],
                                     namespace=namespace_obj)
    facts = collector.collect()

# Generated at 2022-06-13 00:14:48.556346
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    pass

# Generated at 2022-06-13 00:14:56.644369
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    all_collector_classes = frozenset([TestCollector1, TestCollector2])
    namespace = None
    filter_spec = []
    gather_subset = ['all']
    gather_timeout = timeout.DEFAULT_GATHER_TIMEOUT
    minimal_gather_subset = frozenset()
    fact_collector = \
        get_ansible_collector(all_collector_classes=all_collector_classes,
                              namespace=namespace,
                              filter_spec=filter_spec,
                              gather_subset=gather_subset,
                              gather_timeout=gather_timeout,
                              minimal_gather_subset=minimal_gather_subset)



# Generated at 2022-06-13 00:15:01.730996
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    from ansible.module_utils.facts import system
    from ansible.module_utils.facts import ansible_virtual
    from ansible.module_utils.facts import ansible_pkg_mgr

    # Our test_collector_classes are defined in this file
    test_collector_classes = [system.SystemFactCollector,
                              ansible_virtual.VirtualFactCollector,
                              ansible_pkg_mgr.PkgMgrFactCollector]

    # The collector that should be returned
    test_collector = AnsibleFactCollector(collectors=test_collector_classes)

    # The expected facts retrieved from the test_collector
    # They are not all the facts, more should be added if required

# Generated at 2022-06-13 00:15:12.901220
# Unit test for function get_ansible_collector
def test_get_ansible_collector():

    import ansible.module_utils.facts.collector.network
    import ansible.module_utils.facts.collector.system
    import ansible.module_utils.facts.mock

    network_collector_classes = \
        ansible.module_utils.facts.collector.network.network_collector_classes()
    system_collector_classes = \
        ansible.module_utils.facts.collector.system.system_collector_classes()
    all_collector_classes = \
        ansible.module_utils.facts.mock.all_collector_classes()

    all_collector_classes += system_collector_classes
    all_collector_classes += network_collector_classes


# Generated at 2022-06-13 00:15:20.542067
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    from ansible.module_utils.facts import ansible_collector
    from ansible.module_utils.facts import namespace
    fact_collector = \
        ansible_collector.AnsibleFactCollector(collectors=[],
                                               namespace=namespace.BaseFactNamespace(prefix=None))
    assert fact_collector.collect() == {}
    assert fact_collector.collect(collected_facts={"foo": "bar"}) == {"foo": "bar"}



# Generated at 2022-06-13 00:15:28.232459
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    '''
    This tests the AnsibleFactCollector.collect() method
    '''
    class CollectorFake():
        def __init__(self, data):
            self.data = data
        def collect(self):
            return self.data

    class NamespaceFake():
        def __init__(self, namespace, data):
            self.namespace = namespace
            self.data = data
        def collect(self):
            return self.data
        def get_namespace(self):
            return self.namespace

    import sys
    sys.modules['ansible.module_utils.facts'] = ""

    from ansible.module_utils.facts.namespace import PrefixFactNamespace

    namespace_facts = {'a.b': 'c', 'a.d': 'e'}

# Generated at 2022-06-13 00:15:39.969546
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    from ansible.module_utils.facts.system.platform import PlatformFactCollector
    from ansible.module_utils.facts.system.distribution import DistributionFactCollector

    collector_classes = [PlatformFactCollector, DistributionFactCollector]
    collectors = [c() for c in collector_classes]
    fact_collector = AnsibleFactCollector(collectors=collectors)

    # test all
    facts_dict = fact_collector.collect()
    assert 'ansible_facts' in facts_dict
    assert 'ansible_distribution' in facts_dict['ansible_facts']
    assert 'ansible_distribution_version' in facts_dict['ansible_facts']
    assert 'ansible_machine' in facts_dict['ansible_facts']

# Generated at 2022-06-13 00:15:44.280859
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    # The facts_dict we actually return is a 'list of tuples' rather than a dictionary.
    # This is so we can keep the ordering of the facts as they were returned by their
    # collectors.
    facts_dict = []
    collectors = [AnsibleFactCollector(collectors=[])]
    fact_collector = AnsibleFactCollector(collectors=collectors, filter_spec='*')
    assert facts_dict == fact_collector.collect()

# Generated at 2022-06-13 00:16:03.548114
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    class TestCollector(collector.BaseFactCollector):
        name = 'test'

        def collect(self, module=None, collected_facts=None):
            return {'test': True}

    class CollectorNamespace(collector.FactNamespace):
        name = 'test'

    class CollectorNamespaceNonEmpty(collector.FactNamespace):
        name = 'test'
        key = 'test'

    cl = TestCollector()
    namespace = CollectorNamespace()

    ans_fact_collector = get_ansible_collector(
        all_collector_classes=[cl],
        filter_spec=['test'],
        gather_subset=['test'])
    ans_fact_collector.collect()


# Generated at 2022-06-13 00:16:11.437616
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    class CollectorObj(object):
        def __init__(self):
            self.name = 'test'
            self.collected_facts = {}

        def collect_with_namespace(self, module, collected_facts=None):
            self.collected_facts = {}
            self.collected_facts['test_fact'] = 'test_value'
            return self.collected_facts

    collectors = []
    collectors.append(CollectorObj())

    fact_collector = AnsibleFactCollector(collectors=collectors)
    result = fact_collector.collect()
    assert result == {'test_fact': 'test_value'}



# Generated at 2022-06-13 00:16:16.718566
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts.system.distribution import DistributionFactCollector

    fact_collector = \
        AnsibleFactCollector(collectors=[DistributionFactCollector()],
                             namespace=PrefixFactNamespace(prefix='ansible_'))

    facts = fact_collector.collect()

    assert facts.get('ansible_distribution') == 'Linux'

# Generated at 2022-06-13 00:16:23.539840
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    '''This is the equivalent of test/support/unit/module_utils/facts/ansible/__init__.py:test_get_ansible_collector()'''

    from ansible.module_utils.facts import darwin
    from ansible.module_utils.facts import network
    from ansible.module_utils.facts import timeout
    from ansible.module_utils.facts import distro
    from ansible.module_utils.facts import hardware
    from ansible.module_utils.facts import packaging
    from ansible.module_utils.facts import system
    from ansible.module_utils.facts import virtual

    # all collectables

# Generated at 2022-06-13 00:16:31.936847
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    from ansible.module_utils.facts.utils import DictFactCollector

    c = get_ansible_collector([DictFactCollector],
                              gather_subset=[],
                              filter_spec='*',
                              namespace=None,
                              gather_timeout=None,
                              minimal_gather_subset=None)

    sys.modules['ansible.module_utils.facts'] = sys.modules[__name__]  # in case we are being tested
    facts = c.collect()

    assert 'ansible_facts' in facts
    assert facts['ansible_facts']['gather_subset'] == ['all']

# Generated at 2022-06-13 00:16:37.444086
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    try:
        import unittest2 as unittest
    except ImportError:
        import unittest

    from ansible.module_utils.facts.collector.base import BaseFactCollector
    from ansible.module_utils.facts.collector.network import NetworkFactCollector
    from ansible.module_utils.facts.namespace import PrefixFactNamespace

    class TestCollector(BaseFactCollector):

        name = 'testcollector'
        _fact_ids = set([])

        def collect(self, module=None, collected_facts=None):
            return {'test_fact': 'test_fact_value'}

    class TestCollector2(BaseFactCollector):

        name = 'testcollector2'
        _fact_ids = set([])


# Generated at 2022-06-13 00:16:45.012661
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    import ansible.module_utils.facts.collector as collector
    import ansible.module_utils.facts.namespace as namespace

    fact_collector = get_ansible_collector(all_collector_classes=collector.collector_classes(),
                                           namespace=namespace.PrefixFactNamespace(prefix='ansible_'),
                                           gather_subset=['all'],
                                           gather_timeout=10)

    assert isinstance(fact_collector, AnsibleFactCollector)
    assert len(fact_collector.collectors) > 1

# Generated at 2022-06-13 00:16:46.246070
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    pass

# Generated at 2022-06-13 00:16:57.548031
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    class Collector(object):
        def __init__(self, fact_dict):
            self.fact_dict = fact_dict

        def collect(self, module=None, collected_facts=None):
            return self.fact_dict

    class Namespace(object):
        def __init__(self, prefix):
            self.prefix = prefix

        def namespace(self, value):
            return self.prefix + value

    class TestFilter(object):
        def __init__(self):
            self.testkey1 = False
            self.testkey2 = False
            self.testkey3 = False


# Generated at 2022-06-13 00:17:07.307042
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    collector_classes = [collector.NetworkCollector,
                         collector.HardwareCollector]
    namespace = collector.Namespace()
    fact_collector = get_ansible_collector(all_collector_classes=collector_classes,
                                           namespace=namespace,
                                           gather_subset='hardware,network')
    module = None
    collected_facts = {}
    new_facts = fact_collector.collect(module=module,
                                       collected_facts=collected_facts)
    assert 'ansible_facts' in new_facts
    assert 'ansible_hardware' in new_facts['ansible_facts']
    assert 'ansible_network' in new_facts['ansible_facts']
    assert 'gather_subset' in new_facts['ansible_facts']

# Generated at 2022-06-13 00:17:52.603479
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    import sys
    sys.path.append('/usr/local/lib/python2.7/dist-packages/ansible/module_utils/facts')
    from ansible.module_utils.facts import namespace
    import platform
    import sys
    import os
    import ansible.module_utils.facts.system.distribution
    class TestCollector(ansible.module_utils.facts.system.distribution.DistributionFactCollector):
        name = 'system.distribution'

        def collect(self, module=None, collected_facts=None):
            return {'system_distribution': 'TEST DISTRIBUTION'}

    collector = TestCollector(namespace.PrefixFactNamespace(prefix='ansible_'))

# Generated at 2022-06-13 00:18:02.624523
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    # Set up a MockCollector to return a dict of facts
    class MockCollector(collector.BaseFactCollector):

        name = 'mock'
        _fact_ids = set(['ansible_mock'])

        def collect(self, module=None, collected_facts=None):
            return {'ansible_mock': 1}

    # Set up the AnsibleFactCollector using the MockCollector
    fact_collector = AnsibleFactCollector(collectors=[MockCollector()])
    # Collect the facts
    collected_facts = fact_collector.collect()
    # Test the result
    assert collected_facts['ansible_mock'] == 1


# Generated at 2022-06-13 00:18:14.057017
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    from ansible.module_utils.facts.collector.base import BaseFactCollector
    from ansible.module_utils.facts.namespace import PrefixFactNamespace

    test_fact1 = 'hello'
    test_fact2 = 'world'
    test_facts = [test_fact1, test_fact2]

    class TestCollector(BaseFactCollector):
        '''A test collector that returns all the facts under their own namespace.'''
        name = 'test_collector'
        _fact_ids = set([])

        def collect(self, module=None, collected_facts=None):
            facts_dict = {}
            for fact in test_facts:
                if self.namespace:
                    facts_dict[self.namespace.get_name(fact)] = fact
                else:
                    facts_dict[fact]

# Generated at 2022-06-13 00:18:23.967256
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    import ansible.module_utils.facts.collector.network
    import ansible.module_utils.facts.collector.base

    # For testing, the collector will do this:
    # - if name == 'test_collect_from_collector_meta_data_collector'
    #       - Return {'module_setup': True}
    # - else if name == 'test_collect_from_all_collector_class'
    #       - Return {'test_collect_from_all_collector_class': 'collected'}
    # - else if name == 'test_collect_from_all_collector_class_with_setup'
    #       - Return {'test_collect_from_all_collector_class_with_setup': 'collected'}
    # - else
    #       - Return {}
   

# Generated at 2022-06-13 00:18:24.581814
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    pass

# Generated at 2022-06-13 00:18:34.067015
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    all_collector_classes = [collector.Hardware, collector.Network, collector.Cmdline]
    fact_collector = get_ansible_collector(all_collector_classes,
                                           gather_subset='!all,!network')
    expected_fact_ids = ['facter_hardware', 'facter_cmdline']
    fact_ids = fact_collector._fact_ids
    assert fact_ids == expected_fact_ids, 'Expected fact ids %s, but got %s' % (expected_fact_ids, fact_ids)


__all__ = ['AnsibleFactCollector', 'CollectorMetaDataCollector', 'test_get_ansible_collector']

# Generated at 2022-06-13 00:18:37.953676
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    from ansible.module_utils.facts.namespace import PrefixFactNamespace

    class TestFactCollector(collector.BaseFactCollector):
        _fact_id = 'test_fact_collector'

        def collect(self, module=None, collected_facts=None):
            ret = {'myfact1': 'myvalue1'}
            return ret

    fact_collector = AnsibleFactCollector(namespace=PrefixFactNamespace(prefix='ansible_'))
    fact_collector.register_collector(TestFactCollector())
    results = fact_collector.collect()
    assert results['ansible_myfact1'] == 'myvalue1'

# Generated at 2022-06-13 00:18:43.596226
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    import ansible.module_utils.facts.collector.network
    collector_for_all = get_ansible_collector(
        all_collector_classes=ansible.module_utils.facts.collector.network.FACT_SUBSETS,
        namespace=None,
        gather_subset='all',
        filter_spec=None,
        gather_timeout=None,
        minimal_gather_subset=frozenset())
    assert isinstance(collector_for_all, AnsibleFactCollector)



# Generated at 2022-06-13 00:18:52.568368
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    import json
    import copy

    class TestAnsibleFactCollector(AnsibleFactCollector):
        def __init__(self, collectors, namespace):
            super(TestAnsibleFactCollector, self).__init__(collectors, namespace)

    class TestCollector1(collector.BaseFactCollector):
        name = 'test_collector_1'
        _fact_ids = set([])
        def collect(self, module=None, collected_facts=None):
            test_dict = {'test_collector_1_key_1': 'test_collector_1_value_1',
                         'test_collector_1_key_2': 'test_collector_1_value_2'}
            return test_dict

    class TestCollector2(collector.BaseFactCollector):
        name

# Generated at 2022-06-13 00:19:02.857280
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    ''' Unit test for method collect of class AnsibleFactCollector '''
    sys.path.append('./lib/ansible/module_utils/facts')
    from AnsibleFactCollector import AnsibleFactCollector
    from ansible.module_utils.facts import fact_namespace
    from ansible.module_utils.facts.collectors import command

    # Test all required parameters
    fact_collector = AnsibleFactCollector()
    result = fact_collector.collect()
    assert len(result) == 0

    # Test with namespace
    namespace = fact_namespace.PrefixFactNamespace(prefix='ansible_')
    fact_collector = AnsibleFactCollector(namespace=namespace)
    result = fact_collector.collect()
    assert len(result) == 0

    # Test with namespace, init collectors