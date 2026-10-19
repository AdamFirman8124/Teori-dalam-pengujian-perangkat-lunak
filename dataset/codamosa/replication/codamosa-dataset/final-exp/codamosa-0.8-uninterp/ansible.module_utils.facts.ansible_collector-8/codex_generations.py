

# Generated at 2022-06-13 00:09:53.364176
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    '''get_ansible_collector function unit test'''
    all_collector_classes = set()
    all_collector_classes.add(collector.FileSystemCollector)
    all_collector_classes.add(collector.CommandCollector)
    all_collector_classes.add(collector.VirtWhatCollector)

    # Basic test with a single gather_subset and no filter
    ansible_collector = get_ansible_collector(all_collector_classes,
                                              gather_subset=['!virtual'],
                                              gather_timeout=0)
    assert(len(ansible_collector.collectors) == 2)
    assert(isinstance(ansible_collector.collectors[0], collector.FileSystemCollector))

# Generated at 2022-06-13 00:10:04.044542
# Unit test for function get_ansible_collector
def test_get_ansible_collector(): # pylint: disable=R0915
    from ansible.module_utils.facts import collector
    from ansible.module_utils.facts.system.distribution import DistributionCollector
    from ansible.module_utils.facts.virtual import VirtualCollector

    all_collector_classes = [DistributionCollector, VirtualCollector]
    # Test namespace
    fact_collector = get_ansible_collector(all_collector_classes, namespace='testing')
    assert isinstance(fact_collector, AnsibleFactCollector)
    assert len(fact_collector.collectors) == 3

    collector_names = [x.__class__.__name__ for x in fact_collector.collectors]
    assert 'DistributionCollector' in collector_names
    assert 'VirtualCollector' in collector_names

# Generated at 2022-06-13 00:10:13.646643
# Unit test for function get_ansible_collector
def test_get_ansible_collector():

    # Test for coverage
    def test_collector_class(namespace=None):
        return collector.BaseFactCollector(namespace=namespace)
    test_collector_class.name = 'test_collector_class'

    collector_classes = [test_collector_class]

    # Importing each of the default collectors, so our test is 'dumb' and does not depend on any
    # of the default collectors in order to run
    from ansible.module_utils.facts.system import AllSubsetCollector, NetworkSubsetCollector
    collector_classes.extend([AllSubsetCollector, NetworkSubsetCollector])


# Generated at 2022-06-13 00:10:26.864448
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    namespace = None
    filter_spec = None
    gather_subset = ['all']
    gather_timeout = None
    minimal_gather_subset = None

    fact_collector = get_ansible_collector(
        all_collector_classes=collector.ALL_COLLECTOR_CLASSES,
        namespace=namespace,
        filter_spec=filter_spec,
        gather_subset=gather_subset,
        gather_timeout=gather_timeout,
        minimal_gather_subset=minimal_gather_subset
    )

    assert isinstance(fact_collector, AnsibleFactCollector)
    assert isinstance(fact_collector.collectors[0], collector.BaseFactCollector)
    assert isinstance(fact_collector.collectors[1], CollectorMetaDataCollector)

# Generated at 2022-06-13 00:10:29.071563
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    pass

if __name__ == '__main__':
    test_get_ansible_collector()

# Generated at 2022-06-13 00:10:36.823069
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    class mock_collector:
        def collect_with_namespace(self, module, collected_facts):
            info_dict = {'k01': 'v01',
                         'k02': 'v02',
                         'k03': 'v03'}
            return info_dict

    mock_collector_obj = mock_collector()
    fact_collector = AnsibleFactCollector(collectors=[mock_collector_obj])
    result = fact_collector.collect()
    assert result == {'k01': 'v01', 'k02': 'v02', 'k03': 'v03'}
    result = fact_collector.collect(filter_spec='*')
    assert result == {'k01': 'v01', 'k02': 'v02', 'k03': 'v03'}

    fact_

# Generated at 2022-06-13 00:10:48.467428
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    import ansible.module_utils.facts.collectors.hardware
    import ansible.module_utils.facts.collectors.linux

    collector = get_ansible_collector(all_collector_classes=[
        ansible.module_utils.facts.collectors.hardware.HardwareCollector,
        ansible.module_utils.facts.collectors.linux.LinuxCollector],
        namespace=None,
        filter_spec=None,
        gather_subset=['all'],
        gather_timeout=10)
    import json
    d = collector.collect()
    print(json.dumps(d, indent=4))


if __name__ == '__main__':
    test_get_ansible_collector()

# Generated at 2022-06-13 00:10:50.454428
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    import ansible.module_utils.facts.namespace
    all_collector_classes = collector.get_collector_classes()
    fact_collector = get_ansible_collector(all_collector_classes,
                                           namespace=ansible.module_utils.facts.namespace.PrefixFactNamespace(prefix='ansible_'))

# Unit test CollectorMetaDataCollector

# Generated at 2022-06-13 00:10:59.421767
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    from ansible.module_utils.facts import collector
    from ansible.module_utils.facts.collectors import cpu
    from ansible.module_utils.facts.collectors import disk
    from ansible.module_utils.facts import namespace

    all_collector_classes = {'cpu': cpu.CPUFactCollector, 'disk': disk.DiskFactCollector}

    fact_collector = get_ansible_collector(all_collector_classes,
                                           namespace=namespace.BaseFactNamespace,
                                           gather_subset=['cpu'],
                                           gather_timeout=15,
                                           minimal_gather_subset=['cpu'])
    # should have cpu and metadatacollector
    assert len(fact_collector.collectors) == 2

# Generated at 2022-06-13 00:11:08.113903
# Unit test for function get_ansible_collector
def test_get_ansible_collector():

    import ansible.module_utils.facts.system.distribution as dist_collector
    import ansible.module_utils.facts.system.network as network_collector
    import ansible.module_utils.facts.system.platform as platform_collector
    import ansible.module_utils.facts.system.storage as storage_collector
    import ansible.module_utils.facts.system.virtual as virtual_collector

    all_collectors = [dist_collector.Distribution,
                      network_collector.Network,
                      platform_collector.Platform,
                      storage_collector.Storage,
                      virtual_collector.Virtual]


# Generated at 2022-06-13 00:11:14.768744
# Unit test for function get_ansible_collector
def test_get_ansible_collector():

    assert False
    pass


if __name__ == '__main__':
    test_get_ansible_collector()

# Generated at 2022-06-13 00:11:23.777374
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    from ansible.module_utils.facts.collector.network import NetworkFactCollector

    ansible_fact_collector = get_ansible_collector(all_collector_classes=[NetworkFactCollector],
                                                   filter_spec='*',
                                                   gather_subset='!all',
                                                   gather_timeout=10.0,
                                                   minimal_gather_subset=frozenset())

    assert 'ansible_network_' in ansible_fact_collector.collect()


# Generated at 2022-06-13 00:11:29.182376
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    '''Smoke for function get_ansible_collector.'''
    from ansible.module_utils.facts.collector import all_collector_classes

    fact_collector = \
        get_ansible_collector(all_collector_classes=all_collector_classes)

    facts_dict = fact_collector.collect()

    assert(facts_dict['gather_subset'] == 'all')
    assert('module_setup' in facts_dict)

    return facts_dict

# Generated at 2022-06-13 00:11:38.727160
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    from ansible.module_utils.facts import collector

    all_collector_classes = collector.ALL_COLLECTOR_CLASSES
    minimal_gather_subset = frozenset(['all'])
    gather_subset = frozenset(['all', 'network'])
    gather_timeout = 30

    fact_collector = get_ansible_collector(all_collector_classes=all_collector_classes,
                                           minimal_gather_subset=minimal_gather_subset,
                                           gather_subset=gather_subset,
                                           gather_timeout=gather_timeout)

    print(fact_collector.collectors)



# Generated at 2022-06-13 00:11:50.751830
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    import ansible.module_utils.facts.namespace as namespace
    import ansible.module_utils.facts.collectors.generic as generic
    import ansible.module_utils.facts.collectors.identity
    import ansible.module_utils.facts.collectors.system as system

    all_collector_classes = \
        [ system.SystemCollector,
          ansible.module_utils.facts.collectors.identity.IdentityCollector,
          generic.GenericFactCollector ]

    # No custom namespace
    namespace_obj = None
    filter_spec = 'ansible_*'
    gather_subset = ['all', 'network']
    gather_timeout = 10
    minimal_gather_subset = frozenset(['all'])


# Generated at 2022-06-13 00:11:59.203173
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    import ansible.module_utils.facts.collector.network
    import ansible.module_utils.facts.collector.platform

    # Check valid 'all' gather_subset
    all_gather_collector = \
        get_ansible_collector(all_collector_classes=[ansible.module_utils.facts.collector.network.NetworkCollector,
                                                     ansible.module_utils.facts.collector.platform.PlatformCollector],
                              gather_subset=['all'],
                              gather_timeout=0,
                              filter_spec=['interfaces', 'processor'])

    facts_dict = all_gather_collector.collect(module=None)

    assert 'interfaces' in facts_dict
    assert 'processor' in facts_dict
    assert 'network' in facts_dict



# Generated at 2022-06-13 00:12:11.044549
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    # Don't actually run the unit tests if we're running Ansible because this
    # fact collector will be used to gather facts
    if sys.argv[0].endswith("ansible-test") or sys.argv[0].endswith("ansible"):
        class StubFactCollector():
            def __init__(self, namespace=None):
                pass
            def collect(self, module=None, collected_facts=None):
                return dict(test='facts')
        collector = AnsibleFactCollector(collectors=[StubFactCollector()])
        raw_facts = collector.collect()
        assert isinstance(raw_facts, dict)
        assert 'test' in raw_facts
        assert raw_facts['test'] == 'facts'

# Generated at 2022-06-13 00:12:19.912759
# Unit test for function get_ansible_collector
def test_get_ansible_collector():

    from ansible.module_utils.facts import get_ansible_collector

    collector = get_ansible_collector(all_collector_classes=[],
                                      gather_subset=['hardware'])
    assert(collector.namespace == 'ansible_')
    assert(isinstance(collector, AnsibleFactCollector))

    facts_dict = collector.collect()
    assert(facts_dict == {})

    collector = get_ansible_collector(all_collector_classes=[],
                                      gather_subset=['hardware'],
                                      namespace=None)
    assert(collector.namespace == None)
    assert(isinstance(collector, AnsibleFactCollector))

    facts_dict = collector.collect()
    assert(facts_dict == {})

# Generated at 2022-06-13 00:12:31.827140
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    from ansible.module_utils.facts import _legacy_collector_classes
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts.namespace import CollectedFactNamespace

    namespace = CollectedFactNamespace()

    g = get_ansible_collector(_legacy_collector_classes,
                              gather_subset='!all,!min')
    assert isinstance(g, AnsibleFactCollector)
    assert isinstance(g.namespace, CollectedFactNamespace)
    assert g.collectors[-1].name == 'gather_subset'

    g = get_ansible_collector(_legacy_collector_classes,
                              namespace=namespace,
                              gather_subset='!all,!min')

# Generated at 2022-06-13 00:12:42.174984
# Unit test for function get_ansible_collector
def test_get_ansible_collector():

    # Stub out the class-method get_gather_subset()
    # so we can specify our own gather_subset to test
    original_get_gather_subset = collector.BaseFactCollector.get_gather_subset

# Generated at 2022-06-13 00:13:03.544995
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    from ansible.module_utils.facts import collector_functions
    from ansible.module_utils.facts import collector_modules
    from ansible.module_utils.facts import namespace_class
    from ansible.module_utils.facts import timeout

    # ansible.module_utils.facts.collector.collector_classes_from_gather_subset
    # has further unit tests that also cover get_ansible_collector

    # Test with namespace

# Generated at 2022-06-13 00:13:13.506828
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    class Collector1(collector.BaseFactCollector):
        name = 'collector1'

        def collect(self, module=None, collected_facts=None):
            return {'fact1': {'name': 'collector1', 'value': 1}}

    class Collector2(collector.BaseFactCollector):
        name = 'collector2'

        def collect(self, module=None, collected_facts=None):
            return {'fact2': {'name': 'collector2', 'value': 2}}

    collector1 = Collector1()
    collector2 = Collector2()

    collector_objs = [collector1, collector2]
    fact_collector = \
        AnsibleFactCollector(collectors=collector_objs,
                             filter_spec=['*'],
                             namespace='prefix_')



# Generated at 2022-06-13 00:13:23.316775
# Unit test for method collect of class AnsibleFactCollector

# Generated at 2022-06-13 00:13:28.599382
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    class TestCollector(collector.BaseFactCollector):
        def collect(self, module=None, collected_facts=None):
            return {'test_1': 1, 'test_2': 2}

    fact_collector = \
        AnsibleFactCollector(collectors=[TestCollector()],
                             filter_spec=['test*'])
    expected_facts = {'test_1': 1, 'test_2': 2}
    result = fact_collector.collect()
    assert result == expected_facts, result

if __name__ == '__main__':
    test_AnsibleFactCollector_collect()

# Generated at 2022-06-13 00:13:38.668251
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    from ansible.module_utils.facts.namespace import PrefixFactNamespace

    def _get_namespaced_facts():
        return {
            'ansible_facts': {
                'ansible_subset_facts': {
                    'ansible_subsubset_facts': {
                        'my_fact': 'my_value'
                    }
                }, 'ansible_subset_fact': 'subset_value', 'ansible_fact': 'top_value'}
        }

    namespace = PrefixFactNamespace()

    def _get_facts(filter_spec):

        fact_collector = AnsibleFactCollector(filter_spec=filter_spec, namespace=namespace)

        return fact_collector.collect()


# Generated at 2022-06-13 00:13:47.885712
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    import ansible.module_utils.facts.system.distribution
    import ansible.module_utils.facts.system.host
    import ansible.module_utils.facts.system.platform

    collectors = [
        ansible.module_utils.facts.system.distribution.Distribution,
        ansible.module_utils.facts.system.host.Host,
        ansible.module_utils.facts.system.platform.Platform
        ]

    fact_collector = AnsibleFactCollector(collectors=collectors,
                                          namespace=None)

    facts = fact_collector.collect()

    assert 'distribution' in facts
    assert 'os_family' in facts
    assert 'system' in facts
    assert 'platform' in facts

# Generated at 2022-06-13 00:13:59.900407
# Unit test for function get_ansible_collector
def test_get_ansible_collector():

    try:
        from ansible.module_utils.facts import ansible_collection
        ansible_collection._load_collection_plugins('fixtures/ansible_collections/nope/not_a_real_collection')
    except:
        # Likely an older version of Ansible that does not support collections
        # Limiting unit test coverage here
        return

    from ansible_collections.nope.not_a_real_collection.plugins.module_utils.facts import gather_subset
    from ansible_collections.nope.not_a_real_collection.plugins.module_utils.facts import minimal_gather_subset

    filter_spec = filter_spec or []
    gather_subset = gather_subset or ['all']
    gather_timeout = 10
    minimal_gather_subset = minimal_gather_sub

# Generated at 2022-06-13 00:14:08.493816
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    from ansible.module_utils.facts import namespace

    # Test the collector with one namespace
    facts_collector = collector.AnsibleFactCollector(
        namespace=namespace.PrefixFactNamespace(prefix='ansible_'))
    facts_collector.collectors.append(collector.FakeFactCollector1)
    facts_collector.collectors.append(collector.FakeFactCollector2)

    all_facts = facts_collector.collect()
    assert all_facts['ansible_test_fact1'] == 'test-value-1'
    assert all_facts['test_fact2'] == 'test-value-2'
    assert len(all_facts) == 2

    # Test the collector with two namespaces

# Generated at 2022-06-13 00:14:09.437326
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    assert True

# Generated at 2022-06-13 00:14:09.997221
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    pass

# Generated at 2022-06-13 00:14:22.614541
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    from ansible.module_utils.facts import return_facts

    all_collector_classes = return_facts.all_collector_classes()
    fact_collector = get_ansible_collector(all_collector_classes)
    facts = fact_collector.collect()
    assert 'ansible_facts' in facts, "ansible_facts not in facts"

# Generated at 2022-06-13 00:14:32.409249
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():

    # import necessary objects
    from ansible.module_utils.facts import namespace, cache

    # create collector objects
    my_namespace = namespace.Namespace(name='my_ns')
    unapplied_coll = \
        collector.BaseFactCollector([], namespace.Namespace(name='unapplied_ns'))

    # create dictionary that defines facts to be returned in the mock collect method
    collected_facts = {'fact_a': 'first_value', 'fact_b': 'second_value'}

    # define mock collect method
    def mock_collect(self=None, module=None, collected_facts=None):
        return collected_facts

    # patch the collect method of the collector objects
    unapplied_coll.collect = mock_collect

    # create the facts collector under test
    fact_collector = \
        Ans

# Generated at 2022-06-13 00:14:38.097929
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():

    import ansible.module_utils.facts.test.test_items as items

    all_collector_classes = collector.get_collector_classes(items.FactCollection)
    fact_collector = \
        get_ansible_collector(all_collector_classes=all_collector_classes,
                              gather_subset='not_in_fixture_file')

    module = items.MockModule()
    fact_collector.collect(module=module)

    expected_dict = {}
    assert fact_collector.collectors[0].info_dict == expected_dict

    expected_dict = {'one': 1, 'two': 2}
    assert fact_collector.collectors[1].info_dict == expected_dict

    expected_dict = {'three': 3, 'four': 4}
    assert fact_

# Generated at 2022-06-13 00:14:48.805426
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    # if gather_subset is 'all' then all collectors should be included

    #get a set of all collectors
    collector_set = set(collector.FACT_SUBSETS['all'])
    fact_collector = get_ansible_collector(collector_set, gather_subset='all')
    assert set(fact_collector.collectors) == collector_set

    # if gather_subset is 'network' then only the 'network' collectors should be included
    network_set = set(collector.FACT_SUBSETS['network'])
    fact_collector = get_ansible_collector(collector_set, gather_subset='network')
    assert set(fact_collector.collectors) == network_set

    # if a subset is passed in that collects the same thing as another subset without subset
   

# Generated at 2022-06-13 00:14:57.710087
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    '''Unit test for AnsibleFactCollector.collect()'''
    from ansible.module_utils.facts import ansible_collector
    from ansible.module_utils.facts.system.distribution import DistributionFactCollector
    import collections

    # test data
    facts_dict = {
        'fact1': 'value1',
        'fact2': {
            'fact21': 'value21',
            'fact22': 'value22'},
        'fact3': 'value3'}
    facts_dict_with_ansible_prefix = collections.OrderedDict(
        ('ansible_' + k, v) for k, v in facts_dict.items())

    module_mock = object()

    # test setup
    distribution_collector = DistributionFactCollector()

# Generated at 2022-06-13 00:15:09.459038
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    import ansible.module_utils.facts.collector.network

    all_collector_classes = \
        dict(ansible.module_utils.facts.collector.network.__dict__)
    all_collector_classes.update(dict(ansible.module_utils.facts.collector.system.__dict__))

    gather_subset = ['all']
    fact_collector = \
        get_ansible_collector(all_collector_classes=all_collector_classes,
                              gather_subset=gather_subset,
                              filter_spec=[])
    module = None
    collected_facts = None
    facts_dict = fact_collector.collect(module=module, collected_facts=collected_facts)
    assert len(fact_collector.collectors) == 3
    assert facts

# Generated at 2022-06-13 00:15:20.842659
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts import namespace

    class DummyCollector(BaseFactCollector):
        name = 'dummy'

    real_collector_classes = {
        'dummy': set([DummyCollector]),
    }

    # If gather_subset=[] is provided, we should get an empty collector
    collector_obj = get_ansible_collector(all_collector_classes=real_collector_classes,
                                          gather_subset=[],
                                          namespace=namespace.BaseFactNamespace())
    assert collector_obj.collectors == []

    # If minimal_gather_subset=['dummy'] is provided with gather_subset=[], we should get an empty
    # collector
    collector_obj

# Generated at 2022-06-13 00:15:27.197675
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    '''Unit test for method collect of class AnsibleFactCollector'''

    class FakeCollector():
        '''A fake collector using a namespace'''

        def __init__(self):
            self.namespace = AnsibleNamespace()

        def collect_with_namespace(self, module=None, collected_facts=None):
            return {'fake_fact': 'fake_value'}

    ansible_collector = AnsibleFactCollector([FakeCollector()])

    fake_facts = ansible_collector.collect()

    assert(fake_facts == {'ansible_fake_fact': 'fake_value'})



# Generated at 2022-06-13 00:15:39.116373
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    from ansible.module_utils.facts.collector.base import BaseFactCollector
    class MyTestCollector(BaseFactCollector):
        name = 'my_test_collector'

        def collect(self, module=None, collected_facts=None):
            return {'my_test_fact': 'my_test_fact_value'}

    class MyOtherTestCollector(BaseFactCollector):
        name = 'my_other_test_collector'

        def collect(self, module=None, collected_facts=None):
            return {'my_other_test_fact': 'my_other_test_fact_value'}

    all_collector_classes = [MyTestCollector, MyOtherTestCollector]

# Generated at 2022-06-13 00:15:46.415817
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    from ansible.module_utils.facts.collector.local import LocalFactCollector
    from ansible.module_utils.facts.namespace.prefix import PrefixFactNamespace
    from ansible.module_utils.facts.namespace import FactNamespace

    # Boiler plate setup
    #-------------------
    # TODO: Replace with Mock FactCollectors
    lfc = LocalFactCollector(namespace=PrefixFactNamespace(prefix='ansible_'))
    #lfc.collect()
    # TODO: Replace with Mock FactCollectors
    stdns = FactNamespace()

    # Boilerplate teardown
    #---------------------

    # Test setup
    #-----------

# Generated at 2022-06-13 00:16:06.921461
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    import ansible.module_utils.facts.collector.network
    namespace = ansible.module_utils.facts.namespace

    collectors = [ansible.module_utils.facts.collector.network.NetworkCollector(
        namespace=namespace.PrefixFactNamespace(prefix='network_'))]

    fact_collector = AnsibleFactCollector(collectors=collectors)

    # test that if no filter specified, all facts collected
    facts_dict = fact_collector.collect()
    assert len(facts_dict) > 0

    # test that if filter is specified and matches, then we return only filtered facts
    facts_dict = fact_collector.collect(filter_spec='network_interfaces')
    assert len(facts_dict) > 0
    assert 'network_interfaces' in facts_dict

    # test that if

# Generated at 2022-06-13 00:16:16.536927
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    # Test variables
    namespace = 'test_ns'
    collector_name = 'collector_test'
    collector_fact_1 = 'fact_1'
    collector_fact_2 = 'fact_2'
    collector_fact_3 = 'fact_3'

    # Test empty collector
    assert collector.BaseFactCollector([], namespace).collect() == {}

    class CollectBaseFactCollector(collector.BaseFactCollector):
        def collect(self, module=None, collected_facts=None):
            return {collector_fact_1: collector_fact_1}

    class CollectCollector(collector.BaseFactCollector):
        def collect(self, module=None, collected_facts=None):
            return {collector_fact_2: collector_fact_2}

    # Add collectors with and without namespace
    collectors

# Generated at 2022-06-13 00:16:28.732370
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    import ansible.module_utils.facts.collector.network as network
    import ansible.module_utils.facts.collector.platform as platform
    import ansible.module_utils.facts.collector.system as system
    import ansible.module_utils.facts.collector.virtual as virtual

    all_collector_classes = [network.NetworkCollector, system.SystemCollector,
                             platform.PlatformCollector, virtual.VirtualCollector]
    # Collector setup
    collector_obj = get_ansible_collector(all_collector_classes, gather_subset='all')
    assert len(collector_obj.collectors) == 4
    for collector in collector_obj.collectors:
        assert isinstance(collector, collector.BaseFactCollector)


test_get_ansible_collector()

# Generated at 2022-06-13 00:16:35.819076
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    '''Test collect() on class AnsibleFactCollector.'''

    class MockCollector():
        def __init__(self, fact_name_prefix='mock_', return_val=None):
            self.fact_name_prefix = fact_name_prefix
            self.return_val = return_val

        def collect_with_namespace(self, module=None, collected_facts=None):
            if self.return_val:
                return {self.fact_name_prefix + 'fact1': self.return_val,
                        self.fact_name_prefix + 'fact2': self.return_val}
            return {}

    # simple test, no filtering
    test_collector = AnsibleFactCollector(collectors=[MockCollector(return_val='foo')])
    result = test_collector.collect()
   

# Generated at 2022-06-13 00:16:45.886702
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    import ansible.module_utils.facts.collector
    import ansible.module_utils.facts.namespace
    import ansible.module_utils.facts.cache

    all_fact_collector_classes = ansible.module_utils.facts.collector.collector_classes(subset=None,
                                                                                        gather_subset=['all'],
                                                                                        gather_timeout=1)

    all_collector_classes_set = set(all_fact_collector_classes)

    fact_collector = get_ansible_collector(all_collector_classes=all_collector_classes_set,
                                           namespace=ansible.module_utils.facts.namespace.PrefixFactNamespace(prefix='ansible_'),
                                           gather_subset=['all'])

    #

# Generated at 2022-06-13 00:16:54.935020
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    ansible_collector = \
        get_ansible_collector(all_collector_classes=collector.ALL_COLLECTOR_CLASSES,
                              gather_subset=['!facter'],
                              filter_spec=['*'])
    assert(isinstance(ansible_collector, AnsibleFactCollector))

    ansible_collector = \
        get_ansible_collector(all_collector_classes=collector.ALL_COLLECTOR_CLASSES,
                              gather_subset=['all'],
                              filter_spec=['*'])
    assert(isinstance(ansible_collector, AnsibleFactCollector))

# Generated at 2022-06-13 00:17:03.464715
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    from ansible.module_utils.facts import ansible_collector
    # works with this namespace
    namespace = collector.PrefixFactNamespace(prefix='ansible_')

    fc = AnsibleFactCollector(collectors=[ansible_collector],
                              namespace=namespace)
    facts = fc.collect()
    assert 'ansible_all_ipv4_addresses' in facts
    assert 'ansible_all_ipv6_addresses' in facts
    assert 'ansible_processor_cores' in facts
    assert 'ansible_processor_vcpus' in facts



# Generated at 2022-06-13 00:17:09.671756
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    from ansible.module_utils.facts import namespaced_fact_collectors as nfc

    # Test when collector has some fact to collect
    facts_dict = nfc.AnsibleFactCollector(namespace=nfc.PrefixFactNamespace(prefix='ansible_')).collect()
    assert isinstance(facts_dict, dict)

    # Test when collector has no fact to collect
    facts_dict = nfc.AnsibleFactCollector(namespace=nfc.PrefixFactNamespace(prefix='ansible_'),
                                          collectors=[]).collect()
    assert len(facts_dict) == 0

# Generated at 2022-06-13 00:17:16.085371
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    module_mock = 'test_module'
    filter_spec_mock = {'fixture': 'fact_collector_fixture'}

    fc = AnsibleFactCollector(filter_spec=filter_spec_mock)
    obj = fc.collect(module=module_mock)

    assert(obj == {'fixture': {'fact_collector_fixture': True}})

# Generated at 2022-06-13 00:17:20.086233
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    from ansible.module_utils.facts.collector.netdev import NetDevFactCollector

    ansible_collector = \
        AnsibleFactCollector(collectors=[NetDevFactCollector()])

    facts = ansible_collector.collect()

    assert 'ansible_net_all_ipv4_addresses' in facts


# Generated at 2022-06-13 00:17:56.021073
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts.namespace import PrefixFactMetaDataNamespace
    from ansible.module_utils.facts.collectors.default.command_plugins.linux import (
        AnsibleDistributionFactCollector,
        AnsibleOSReleaseFactCollector,
        AnsibleLinuxKernelReleaseFactCollector,
        AnsibleKernelFactCollector,
    )
    from ansible.module_utils.facts.collectors.default.command_plugins.hardware import (
        AnsibleHardwareFactCollector,
    )
    from ansible.module_utils.facts.collectors.default.command_plugins.virtual import (
        AnsibleVirtualFactCollector,
    )

# Generated at 2022-06-13 00:18:08.613222
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    """Test the collection of facts using the AnsibleFactCollector class.

    The results should be returned as a dict that contains the key 'ansible_facts' and the
    value is another dict with the results of the collection of facts.
    """
    # Create a dict with some values to test
    info_dict = {'test_fact': 'test_value'}
    # Create a Mock BaseFactCollector object
    mock_BaseFactCollector_obj = collector.BaseFactCollector()
    type(mock_BaseFactCollector_obj).collect_with_namespace = \
        collector.collect_with_namespace_patcher_ansible_facts(return_value=info_dict)

    # Create a AnsibleFactCollector object and set 'collectors' attribute to
    # a list containing the Mock BaseFactCollector object
    fact_

# Generated at 2022-06-13 00:18:17.955974
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():

    # TODO: this test is mostly stubbed out, as the modules it uses are not
    #       usable outside of ansible itself.

    from ansible.module_utils.facts.collectors import (
        fact_collector,
        networking,
        virtual,
        hardware,
        system,
        collector,
        distribution,
        kernel,
        selinux,
        codec,
        ohai,
    )

    def _test_collect(collectors, namespace, expected_facts, **kwargs):
        kwargs['collectors'] = collectors
        kwargs['namespace'] = namespace
        kwargs['module'] = 'module'

        ansible_collector = AnsibleFactCollector(**kwargs)

        gathered_facts = ansible_collector.collect()
        assert gathered_facts == expected_facts

    #

# Generated at 2022-06-13 00:18:23.035442
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    """Unit test for function get_ansible_collector"""

    class FoobarCollector(collector.BaseFactCollector):
        """FoobarCollector"""

        name = 'foobar'

    collector_classes = [FoobarCollector]
    fact_collector = get_ansible_collector(collector_classes, gather_subset=[],
                                           gather_timeout=None)
    # expect FoobarCollector to be included
    assert FoobarCollector in fact_collector.collectors


if __name__ == '__main__':
    # Unit test for function get_ansible_collector
    test_get_ansible_collector()

# Generated at 2022-06-13 00:18:33.750140
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    from ansible.module_utils.facts.namespace import PrefixFactNamespace

    class FakeCollector1(collector.BaseFactCollector):
        _fact_ids = set(['fake_collector1_1'])

        def __init__(self, ns):
            self.name = 'fake_collector1'

    class FakeCollector2(collector.BaseFactCollector):
        _fact_ids = set(['fake_collector1_1', 'fake_collector2'])

        def __init__(self, ns):
            self.name = 'fake_collector2'

    class FakeCollector3(collector.BaseFactCollector):
        _fact_ids = set(['fake_collector3'])


# Generated at 2022-06-13 00:18:41.025665
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    import inspect

    from ansible.module_utils.facts.system.base import BaseFactCollector
    from ansible.module_utils.facts.system import distribution

    collector_classes = [c for (n, c) in inspect.getmembers(distribution) if inspect.isclass(c)
                         and issubclass(c, BaseFactCollector)]

    fact_collector = get_ansible_collector(collector_classes=collector_classes)
    assert fact_collector is not None

    # general test that collector_classes are all in the fact_collector
    for collector_class in collector_classes:
        assert collector_class.name in fact_collector.collectors

    # test that we can get the fact collector back from the object
    found_facts = fact_collector.collect()

    assert 'distribution' in found

# Generated at 2022-06-13 00:18:50.608915
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    import collections
    import os
    import sys
    import time

    from ansible.module_utils.facts import cache
    from ansible.module_utils.facts import collector

    # quick hack to set up dicts for testing
    sys.modules['ansible.module_utils.facts.collector'] = collector
    sys.modules['ansible.module_utils.facts.cache'] = cache

    class Collector1(collector.BaseFactCollector):
        name = 'collector1'
        _fact_ids = set([])
        def collect(self, module=None, collected_facts=None):
            return {'fact1': 'a'}

    # module setup is not built, so this should not be included
    class Collector2(collector.BaseFactCollector):
        name = 'collector2'

# Generated at 2022-06-13 00:18:56.723479
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    all_collector_classes = collector.collector_classes()
    fact_collector = get_ansible_collector(all_collector_classes)
    assert fact_collector is not None
    assert fact_collector.name == 'ansible'
    assert fact_collector.collectors is not None
    assert len(fact_collector.collectors) == len(all_collector_classes) + 1

# Generated at 2022-06-13 00:19:04.999539
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    import ansible.module_utils.facts.namespace as namesp
    class DummyCollector(collector.BaseFactCollector):
        def collect_with_namespace(self, module=None, collected_facts=None):
            facts_dict = {}
            for count in range(1, 10):
                facts_dict['foo%d' % count] = 'bar%d' % count
            return facts_dict

    dummy_collector = DummyCollector()

    fact_collector = AnsibleFactCollector(collectors=[dummy_collector], namespace=None)
    result = fact_collector.collect()
    assert isinstance(result, dict)

# Generated at 2022-06-13 00:19:11.577733
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    class TestCollector(collector.BaseFactCollector):
        name = 'test'

        def collect(self, module=None, collected_facts=None):
            return {'a': 1, 'b': 2, 'c': 3}

    collect_obj = AnsibleFactCollector(collectors=[TestCollector()])
    collected_facts = collect_obj.collect()
    assert collected_facts['a'] == 1
    assert collected_facts['b'] == 2
    assert collected_facts['c'] == 3
