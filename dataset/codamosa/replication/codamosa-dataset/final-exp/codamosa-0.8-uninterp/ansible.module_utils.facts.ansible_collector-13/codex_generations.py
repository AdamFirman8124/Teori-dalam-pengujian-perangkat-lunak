

# Generated at 2022-06-13 00:09:46.055736
# Unit test for method collect of class CollectorMetaDataCollector
def test_CollectorMetaDataCollector_collect():
    fact_collector = CollectorMetaDataCollector(gather_subset=['all'],
                                                module_setup=True)
    collected_facts = fact_collector.collect()
    assert collected_facts == {'gather_subset': ['all'], 'module_setup': True}

# Generated at 2022-06-13 00:09:48.401238
# Unit test for method collect of class CollectorMetaDataCollector
def test_CollectorMetaDataCollector_collect():
    meta_collector = CollectorMetaDataCollector('gather_subset')
    assert meta_collector.collect() == {'gather_subset': 'gather_subset'}

# Generated at 2022-06-13 00:09:56.651130
# Unit test for method collect of class CollectorMetaDataCollector
def test_CollectorMetaDataCollector_collect():
    fact_collector = CollectorMetaDataCollector('all')
    facts = fact_collector.collect()

    assert 'gather_subset' in facts.keys()
    assert facts['gather_subset'] == 'all'

    fact_collector = CollectorMetaDataCollector('min')
    facts = fact_collector.collect()

    assert 'gather_subset' in facts.keys()
    assert facts['gather_subset'] == 'min'

# Generated at 2022-06-13 00:10:00.869261
# Unit test for method collect of class CollectorMetaDataCollector
def test_CollectorMetaDataCollector_collect():
    collector_meta_data_collector = CollectorMetaDataCollector(gather_subset=['all'],
                                                               module_setup=True)
    assert collector_meta_data_collector.collect() == {'gather_subset': ['all'], 'module_setup': True}

# Generated at 2022-06-13 00:10:08.416028
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    from ansible.module_utils.facts import ansible_collector
    from ansible.module_utils.facts import default_collectors

    fact_collector = \
        get_ansible_collector(all_collector_classes=default_collectors,
                              gather_subset=['!all'],
                              gather_timeout=0)
    results = fact_collector.collect(module=None, collected_facts=None)
    assert results == {'gather_subset': ['!all'], 'module_setup': True}

# Generated at 2022-06-13 00:10:10.844321
# Unit test for method collect of class CollectorMetaDataCollector
def test_CollectorMetaDataCollector_collect():
    collector_meta_data_collector = \
        CollectorMetaDataCollector(gather_subset=['all', 'network'])
    result = collector_meta_data_collector.collect()
    assert result == {'gather_subset':['all', 'network']}


# Generated at 2022-06-13 00:10:23.663913
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    import ansible.module_utils.facts.system.distribution
    import ansible.module_utils.facts.system.system
    import ansible.module_utils.facts.network.interfaces
    collector_objs = []
    collector_objs.append(ansible.module_utils.facts.system.distribution.DistributionFactCollector())
    collector_objs.append(ansible.module_utils.facts.system.system.SystemFactCollector())
    collector_objs.append(ansible.module_utils.facts.network.interfaces.InterfacesFactCollector())
    ansible_factcollector = AnsibleFactCollector(collectors=collector_objs)
    result = ansible_factcollector.collect()
    assert 'distribution' in result
    assert result['distribution'] == 'Debian'


# Generated at 2022-06-13 00:10:28.335747
# Unit test for method collect of class CollectorMetaDataCollector
def test_CollectorMetaDataCollector_collect():
    collectors = [CollectorMetaDataCollector(gather_subset=['all'])]
    fact_collector = CollectorMetaDataCollector(collectors=collectors)
    assert fact_collector.collect() == {'gather_subset': ['all']}


# Generated at 2022-06-13 00:10:38.331695
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    module = None

# Generated at 2022-06-13 00:10:48.402241
# Unit test for method collect of class CollectorMetaDataCollector
def test_CollectorMetaDataCollector_collect():
    collector_meta_data_collector = CollectorMetaDataCollector()
    module = ['ehlo']
    collected_facts = {}
    meta_facts = collector_meta_data_collector.collect(module, collected_facts)
    assert 'gather_subset' in meta_facts
    assert 'module_setup' in meta_facts



# Generated at 2022-06-13 00:11:05.128001
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    from ansible.module_utils.facts import collector

    def dummy(namespace=None):
        return collector.BaseFactCollector(namespace=namespace)

    all_collector_classes = {
        'all': dummy,
        'interfaces': dummy,
        'network': dummy,
        'platform': dummy
    }

    collectors = [x.__class__.__name__ for x in get_ansible_collector(all_collector_classes,
                                                                     namespace=None,
                                                                     filter_spec=None,
                                                                     gather_subset=['all'],
                                                                     gather_timeout=10,
                                                                     minimal_gather_subset=frozenset()).collectors]


# Generated at 2022-06-13 00:11:17.074483
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    fact_collector = \
        get_ansible_collector(namespace=None,
                              all_collector_classes=collector.BaseFactCollector.get_collector_classes(),
                              filter_spec=None,
                              gather_subset=['all'],
                              gather_timeout=timeout.DEFAULT_GATHER_TIMEOUT,
                              minimal_gather_subset=frozenset())

    results = fact_collector.collect(module=None, collected_facts=None)
    assert 'ansible_processor_count' in results
    assert results['gather_subset'] == ['all']


# Generated at 2022-06-13 00:11:25.089720
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts.namespace import PrefixFactNamespacePerSubset
    from ansible.module_utils.facts.namespace import PrefixFactNamespaceByCollector

    # Skipping for Windows because the facts are not implemented for Windows.
    ansible_collector_obj = get_ansible_collector(
        all_collector_classes=None,
        namespace=None,
        filter_spec='*',
        gather_subset=None,
        gather_timeout=None,
        minimal_gather_subset=None)

    # Run collect with no namespace
    ansible_collector_obj.collect()

    # Run collect with namespace=PrefixFactNamespace
    ansible_collector_obj = get_ans

# Generated at 2022-06-13 00:11:30.670437
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    import ansible.module_utils.facts.hardware
    import ansible.module_utils.facts.system

    all_collector_classes = {
        'hardware': ansible.module_utils.facts.hardware.Hardware,
        'system': ansible.module_utils.facts.system.System,
    }
    get_ansible_collector(all_collector_classes=all_collector_classes,
                          gather_subset=['all'])

# Generated at 2022-06-13 00:11:41.661068
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    # fake all_collector_classes
    all_collector_classes = {
        'all': collector.BaseFactCollector,
        'minimal': collector.BaseFactCollector,
        'facter': collector.BaseFactCollector,
        'alternative_1': collector.BaseFactCollector,
        'alternative_2': collector.BaseFactCollector,
        'ohai': collector.BaseFactCollector,
        'network': collector.BaseFactCollector,
        'hardware': collector.BaseFactCollector,
        'virtual': collector.BaseFactCollector,
        'default': collector.BaseFactCollector}
    fact_collector = get_ansible_collector(all_collector_classes=all_collector_classes)

# Generated at 2022-06-13 00:11:53.422530
# Unit test for function get_ansible_collector
def test_get_ansible_collector():

    from ansible.module_utils.facts.collector import collect_all_subset

    all_collector_classes = frozenset([collect_all_subset.AllSubsetCollector])
    subset_collector = get_ansible_collector(all_collector_classes=all_collector_classes)

    assert subset_collector.gather_subset == ['all']

    subset_collector = \
        get_ansible_collector(all_collector_classes=all_collector_classes,
                              gather_subset=['foo'],
                              minimal_gather_subset=frozenset('all'))

    assert subset_collector.gather_subset == ['foo']



# Generated at 2022-06-13 00:12:00.318543
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    import module_utils.facts.platform.linux

    # This is a list of all the FactCollector classes available in this module
    all_collector_classes = [
        module_utils.facts.platform.linux.LinuxFactCollector,
        module_utils.facts.system.distribution.DistributionFactCollector,
        module_utils.facts.system.distribution.LinuxDistributionFactCollector,
        module_utils.facts.system.distribution.RedhatDistributionFactCollector,
    ]


# Generated at 2022-06-13 00:12:12.115012
# Unit test for method collect of class AnsibleFactCollector

# Generated at 2022-06-13 00:12:18.668929
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    class FakeFactCollector(collector.BaseFactCollector):

        def collect(self, module=None, collected_facts=None):
            return {'fake_fact': 'fake_fact'}

    fact_collector = AnsibleFactCollector([FakeFactCollector()])
    collected_facts = fact_collector.collect()
    assert collected_facts.keys() == ['ansible_facts']
    assert collected_facts['ansible_facts']['fake_fact'] == 'fake_fact'
    assert collected_facts['ansible_facts'].keys() == ['fake_fact']

    fact_collector = AnsibleFactCollector([FakeFactCollector(namespace=PrefixFactNamespace(prefix='foo_'))])
    collected_facts

# Generated at 2022-06-13 00:12:23.314365
# Unit test for function get_ansible_collector
def test_get_ansible_collector():

    all_collectors = collector.ALL_COLLECTOR_CLASSES
    ansible_collector = get_ansible_collector(all_collectors)
    assert len(ansible_collector.collectors) > 1

# Generated at 2022-06-13 00:12:37.433902
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():

    # Create two collectors and test each separately
    f1 = collector.Fact('f1', {})
    f2 = collector.Fact('f2', {})
    c1 = collector.BaseFactCollector([f1])
    c2 = collector.BaseFactCollector([f2])

    # Create a collector with the two collectors
    c3 = AnsibleFactCollector(collectors=[c1, c2], filter_spec='*', namespace=None)

    # Create a dict with f1 and f2 facts
    facts_dict = {'f1': 1, 'f2': 2}

    # Create a fact dictionary in the fact_collector
    c3._create_fact_dict = lambda x: facts_dict

    # Call collect()
    result = c3.collect()

    # Verify collected facts
    assert result == facts_dict

# Generated at 2022-06-13 00:12:38.109734
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    pass

# Generated at 2022-06-13 00:12:46.378999
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    import ansible.module_utils.facts.collector
    fact_collector = get_ansible_collector(all_collector_classes=ansible.module_utils.facts.collector.ALL_COLLECTOR_CLASSES,
                                           minimal_gather_subset=ansible.module_utils.facts.collector.ALL_COLLECTOR_CLASSES.keys(),
                                           filter_spec=['ansible_*'],
                                           gather_subset=['all', 'network'],
                                           gather_timeout=timeout.GATHER_TIMEOUT)

    collected_facts = fact_collector.collect()
    assert collected_facts.get('gather_subset') == ['all', 'network']
    assert collected_facts.get('module_setup') is True

# Generated at 2022-06-13 00:12:59.322599
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    class Collector1(collector.BaseFactCollector):
        name = 'Collector1'
        _fact_ids = set(['fact1', 'fact2'])

        def collect(self, module=None, collected_facts=None):
            return {
                'fact1': 'value1',
                'fact2': 'value2',
                'fact3': 'value3',
            }

    class Collector2(collector.BaseFactCollector):
        name = 'Collector2'
        _fact_ids = set(['fact4', 'fact5'])

        def collect(self, module=None, collected_facts=None):
            return {
                'fact4': 'value4',
                'fact5': 'value5',
                'fact6': 'value6',
            }


# Generated at 2022-06-13 00:13:00.449910
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    pass

# Generated at 2022-06-13 00:13:11.148762
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    collector_classes = (collector.FacterFactCollector,
                         collector.OhaiFactCollector,
                         collector.LocalSetupFactCollector)
    fact_collector = get_ansible_collector(all_collector_classes=collector_classes,
                                           gather_subset=['all'],
                                           gather_timeout=30,
                                           minimal_gather_subset=['all'])

    assert fact_collector.collectors[0].name == 'facter'
    assert fact_collector.collectors[1].name == 'ohai'
    assert fact_collector.collectors[2].name == 'setup'
    assert fact_collector.collectors[3].name == 'gather_subset'



# Generated at 2022-06-13 00:13:22.299157
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    import ansible.module_utils.facts.network.linux.interfaces as linux_interfaces
    import ansible.module_utils.facts.network.linux.lldp as linux_lldp
    import ansible.module_utils.facts.system.distribution as system_distribution
    import ansible.module_utils.facts.system.pkg_mgr as pkg_mgr
    import ansible.module_utils.facts.virtual.lxc as lxc
    import ansible.module_utils.facts.virtual.kvm as kvm
    import ansible.module_utils.facts.virtual.xenapi as xenapi
    import ansible.module_utils.facts.virtual.vbox as vbox

    class NoneCollector(collector.BaseFactCollector):
        name = 'none'


# Generated at 2022-06-13 00:13:26.747151
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    test_collector_classes = [collector.BaseFactCollector]
    test_fact_collector = AnsibleFactCollector(test_collector_classes)
    test_facts = test_fact_collector.collect()
    assert isinstance(test_facts, dict)
    # assert 'collectors' in test_facts
    # assert test_facts['collectors'] == test_collector_classes

# Generated at 2022-06-13 00:13:37.173342
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    '''A unit test on the get_ansible_collector() function used by get_facts module'''
    class TestCollector(collector.BaseFactCollector):
        name = 'ansible_facts'
        _fact_ids = set([])

        def __init__(self, namespace):
            super(TestCollector, self).__init__(namespace=namespace)
            self.collector_calls = 0

        def collect(self, module=None, collected_facts=None):
            self.collector_calls += 1
            return {}

    all_collector_classes = [TestCollector]
    gather_subset = ['all']
    gather_timeout = 10
    minimal_gather_subset = frozenset()
    filter_spec = []
    namespace = 'ansible_module_test'



# Generated at 2022-06-13 00:13:37.764754
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    pass


# Generated at 2022-06-13 00:13:48.040765
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():

    fact_name = 'dummy_fact'

    class DummyAnsibleFactCollector(collector.BaseFactCollector):
        name = fact_name
        _fact_ids = set([fact_name])

        def collect(self, module=None, collected_facts=None):
            return {'dummy_fact': 'test_value'}

    dummy_fact_collector = DummyAnsibleFactCollector()
    fact_collector = AnsibleFactCollector(collectors=[dummy_fact_collector])

    fact_dict = fact_collector.collect()
    assert fact_name in fact_dict

# Generated at 2022-06-13 00:14:00.078020
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():

    import ansible.module_utils.facts.system.distribution as distribution
    import ansible.module_utils.facts.system.platform as platform

    test_facts = {'distribution': {'name': 'Fedora', 'major_release': '28'},
                  'distribution_version': '28',
                  'os_family': 'RedHat',
                  'platform': 'Fedora',
                  'platform_version': '28'}

    test_collector_classes = [platform.Collector, distribution.Collector]

    test_collector = \
        get_ansible_collector(all_collector_classes=test_collector_classes)

    test_result = test_collector.collect()

    assert test_result == test_facts, \
        'AnsibleFactCollector collects incorrect facts'

# Unit test

# Generated at 2022-06-13 00:14:08.612419
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    class MockCollector2(CollectorMetaDataCollector):
        name = 'test2'
        _fact_ids = set(['test2'])

        def collect(self, module=None, collected_facts=None):
            info = {'test2': '#2'}
            return info

    class MockCollector1(CollectorMetaDataCollector):
        name = 'test1'
        _fact_ids = set(['test1'])

        def collect(self, module=None, collected_facts=None):
            info = {'test1': '#1'}
            return info

    collectors_list = [MockCollector1(), MockCollector2()]
    fact_collector = AnsibleFactCollector(collectors=collectors_list)

# Generated at 2022-06-13 00:14:18.436327
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    class FakeClassA(collector.BaseFactCollector):
        name = 'a'
    class FakeClassB(collector.BaseFactCollector):
        name = 'b'
    class FakeClassC(collector.BaseFactCollector):
        name = 'c'

    all_collector_classes = [FakeClassA, FakeClassB, FakeClassC]
    test_namespace = collector.Namespace.for_module_name(module_name='ansible')

    # Test when nothing is specified
    assert set(get_ansible_collector(all_collector_classes=all_collector_classes,
                                     namespace=test_namespace).collectors) == set([FakeClassA,
                                                                                  FakeClassB,
                                                                                  FakeClassC,
                                                                                  CollectorMetaDataCollector])

# Generated at 2022-06-13 00:14:29.722396
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    # Collectors that always return the same results
    class TestCollector(collector.BaseFactCollector):
        name = 'test'
        _fact_ids = set(['some', 'foo', 'bar'])

        def collect(self, module=None, collected_facts=None):
            return {'some': 'thing', 'foo': 'bar', 'bar': 'baz'}

    # make sure the filter_spec works
    fact_collector = AnsibleFactCollector(collectors=[TestCollector()],
                                          filter_spec=['a*'])
    facts_dict = fact_collector.collect()
    assert facts_dict == {}

    fact_collector = AnsibleFactCollector(collectors=[TestCollector()],
                                          filter_spec=['some', 'foo'])

# Generated at 2022-06-13 00:14:38.562437
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    import ansible.module_utils.facts.network
    import ansible.module_utils.facts.virtual
    import ansible.module_utils.facts.distribution

    network_collector = ansible.module_utils.facts.network.NetworkCollector(namespace=None)
    virtual_collector = ansible.module_utils.facts.virtual.VirtualCollector(namespace=None)
    distribution_collector = ansible.module_utils.facts.distribution.DistributionCollector(namespace=None)

    fact_collector = AnsibleFactCollector(collectors=[network_collector, virtual_collector, distribution_collector])
    result = fact_collector.collect()

    print(result)


# Generated at 2022-06-13 00:14:49.052206
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    # It is important to test that the namespace used is the one requested.
    # The test fact collectors are not designed to work with a namespace
    # and the namespace must be stripped off before using the test fact collector.
    #
    # It is also important to test no namespace is used when requested.

    class TestFactNamespace(object):
        def __init__(self, prefix):
            self.prefix = prefix

        def wrap(self, name):
            return self.prefix + name

        def unwrap(self, name):
            if name.startswith(self.prefix):
                return name[len(self.prefix):]
            return name

    fact_subset_pattern_re = r'^(test_test_|test_the_|test_filter_|test_no_namespace_|test_subset_)'
    fact_

# Generated at 2022-06-13 00:14:57.864459
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    import ansible.module_utils.facts.collector.network

    all_collector_classes = \
        ansible.module_utils.facts.collector.network.NetworkColletor.collector_classes()

    minimal_gather_subset = set()
    gather_subset = ['!min', 'network']
    gather_timeout = 10

    ansible_collector = \
        get_ansible_collector(all_collector_classes=all_collector_classes,
                              gather_subset=gather_subset,
                              minimal_gather_subset=minimal_gather_subset,
                              gather_timeout=gather_timeout)

    ansible_facts = ansible_collector.collect()

    assert 'ansible_net_interfaces' in ansible_facts

# Generated at 2022-06-13 00:15:09.699276
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    from ansible.module_utils.facts import all_collector_classes as all_collectors
    from ansible.module_utils.facts import namespace

    # Note: this will collect the full set of facts (minus system version)
    collector_obj = get_ansible_collector(all_collectors, namespace=namespace)
    # This will fail the unit test if it fails
    facts_dict = collector_obj.collect()

    assert facts_dict['gather_subset'] == ['all']
    assert facts_dict['module_setup'] is True
    # We don't do a full fact collection, but at least make sure the 'ansible_facts' namespace is there
    assert 'ansible_facts' in facts_dict

    # Note: this will collect a minimal subset of facts
    minimal_collector_obj = get_ansible_collect

# Generated at 2022-06-13 00:15:21.138397
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    #
    # TODO: FACT-1740 add tests for
    #       - namespace
    #       - gather_subset
    #       - gather_timeout
    #       - minimal_gather_subset
    #
    all_collector_classes = collector.get_collector_classes()
    # noinspection PyUnresolvedReferences
    fact_collector = get_ansible_collector(all_collector_classes)
    assert fact_collector is not None
    # noinspection PyTypeChecker
    assert fact_collector.filter_spec is None

    fact_collector = \
        get_ansible_collector(all_collector_classes,
                              filter_spec='ansible_distribution_version')
    facts = fact_collector.collect()

# Generated at 2022-06-13 00:15:36.039129
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    from ansible.module_utils.facts import collector_namespace

    all_collector_classes = [collector_namespace.AptCollector]

    ansible_collector = \
        get_ansible_collector(all_collector_classes=all_collector_classes,
                              gather_subset='all')

    assert isinstance(ansible_collector, AnsibleFactCollector)

    assert ansible_collector.collectors[0].name == 'apt'
    assert ansible_collector.collectors[1].name == 'gather_subset'

    assert len(ansible_collector.collectors) == 2

# Generated at 2022-06-13 00:15:42.061177
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():

    ##############################################################
    # make a namespace that adds a prefix to each fact
    ##############################################################

    class MyFactNamespace:
        def __init__(self, prefix):
            self.prefix = prefix

        def __call__(self, fact):
            return '%s_%s' % (self.prefix, fact)

    ##############################################################
    # make a fact collector that knows about the namespace
    ##############################################################

    class MyFactCollector(collector.BaseFactCollector):
        def __init__(self, namespace=None):
            super(MyFactCollector, self).__init__(namespace=namespace)


# Generated at 2022-06-13 00:15:53.041770
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    from ansible.module_utils.facts.collector.network import NetworkFactCollector
    from ansible.module_utils.facts.collector.processor import ProcessorFactCollector

    minimal_gather_subset = frozenset('network')
    gather_subset = 'all'
    gather_timeout = 60
    filter_spec = '*net*'
    namespace = None

    fact_collector = get_ansible_collector(all_collector_classes=[NetworkFactCollector,
                                                                   ProcessorFactCollector],
                                           minimal_gather_subset=minimal_gather_subset,
                                           gather_subset=gather_subset,
                                           gather_timeout=gather_timeout,
                                           filter_spec=filter_spec,
                                           namespace=namespace)

   

# Generated at 2022-06-13 00:16:00.441508
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    from ansible.module_utils.facts import collector
    from ansible.module_utils.facts import utils
    from ansible.module_utils.facts import default_collectors
    import types

    gather_subset = ['all', 'some']
    gather_timeout = 10
    minimal_gather_subset = frozenset(['some'])

    collector_obj = \
        get_ansible_collector(all_collector_classes=default_collectors,
                              namespace=None,
                              filter_spec=None,
                              gather_subset=gather_subset,
                              gather_timeout=gather_timeout,
                              minimal_gather_subset=minimal_gather_subset)

    assert(isinstance(collector_obj, AnsibleFactCollector))

    # Check that the

# Generated at 2022-06-13 00:16:09.653947
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():

    # mock the fact collectors
    fact_collector_1 = \
        collector.BaseFactCollector({'a_fact': 'a_value'}, namespace=None)
    fact_collector_2 = \
        collector.BaseFactCollector({'b_fact': 'b_value'}, namespace=None)

    fact_collector = \
        AnsibleFactCollector(filter_spec='*',
                             collectors=[fact_collector_1, fact_collector_2])

    # Fact collector with filter_spec=None should collect all facts
    facts = fact_collector.collect()
    assert sorted(facts) == ['a_fact', 'b_fact']

    # Fact collector with filter_spec=* should collect all facts
    facts = fact_collector.collect(filter_spec='*')

# Generated at 2022-06-13 00:16:11.650821
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    fact_collector = get_ansible_collector(['all'],'','')
    assert type(fact_collector) == AnsibleFactCollector

# Generated at 2022-06-13 00:16:17.236390
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    from ansible.module_utils.facts.system.distribution import DistributionFactCollector

    # Initialize fact collector that collects fact 'distribution'
    fact_collector = AnsibleFactCollector(collectors=[DistributionFactCollector()])
    # Run collect method
    collected_facts = fact_collector.collect()
    # Check that collection of fact 'distribution' from DistributionFactCollector is same as expected
    assert collected_facts['distribution'] == DistributionFactCollector().collect_with_namespace()['distribution']

# Generated at 2022-06-13 00:16:20.702497
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    l = []
    c = get_ansible_collector(l)
    assert(isinstance(c, AnsibleFactCollector))

# Generated at 2022-06-13 00:16:24.505994
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    fact_collector = AnsibleFactCollector(collectors=[collector.FacterFactCollector(namespace='')],
                                          filter_spec=['*'])

    result = fact_collector.collect()
    assert result

# Generated at 2022-06-13 00:16:33.538981
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    from ansible.module_utils.facts import namespace
    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils.facts import module_setup_collectors

    fact_collector = get_ansible_collector(all_collector_classes=default_collectors)
    facts = fact_collector.collect()
    assert facts is not None
    assert facts['gather_subset'] == ['all']
    assert facts['module_setup']

    fact_collector = get_ansible_collector(all_collector_classes=default_collectors,
                                           minimal_gather_subset=('ohai_facts',))
    facts = fact_collector.collect()
    assert facts is not None
    assert facts['gather_subset'] == ['all']

# Generated at 2022-06-13 00:16:49.951131
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    import ansible

    sys.modules['ansible'] = ansible
    try:
        collector_obj = \
            AnsibleFactCollector.from_gather_subset(
                '*',
                gather_subset=None,
                namespace=None,
                filter_spec=None)
        assert collector_obj
    finally:
        del sys.modules['ansible']

# Generated at 2022-06-13 00:17:00.589529
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():

    module = None
    collected_facts = {
        'test_fact': 'this is a test fact',
        'some_other_fact': 'other_fact'
    }

    def test_collector(module, collected_facts):
        return {'new_facts': 'this are test new facts'}

    fact_collector = \
        AnsibleFactCollector(collectors=[test_collector],
                             filter_spec=['*'])
    collected_facts = fact_collector.collect(module=module, collected_facts=collected_facts)
    assert collected_facts == {'new_facts': 'this are test new facts'}

    # test with no filter_spec
    fact_collector = \
        AnsibleFactCollector(collectors=[test_collector],
                             filter_spec=[])
    collected

# Generated at 2022-06-13 00:17:09.675956
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    from ansible.module_utils.facts import namespace
    from ansible.module_utils.facts import collector
    from ansible.module_utils.facts import collectors
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts.collector.filesystem import FilesystemCollector
    from ansible.module_utils.facts.collector.devicemanage import DeviceManageCollector

    gather_subset = ['all', 'network', 'virtual']
    gather_subset_empty = []
    minimal_gather_subset = frozenset()
    minimal_gather_subset2 = frozenset(('network', 'virtual'))
    # Return list of collectors sorted by class name

# Generated at 2022-06-13 00:17:20.245932
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts.collector import NetworkInterfaceCollector, PlatformCollector
    from ansible.module_utils.facts.platform.linux import DistributionCollector

    fact_collector = AnsibleFactCollector(collectors=[
        NetworkInterfaceCollector(namespace=PrefixFactNamespace(prefix='ansible_')),
        PlatformCollector(namespace=PrefixFactNamespace(prefix='ansible_')),
        DistributionCollector(namespace=PrefixFactNamespace(prefix='ansible_'))
    ])

    gathered_facts = fact_collector.collect()

    # Make sure the facts are collected
    assert gathered_facts.get('ansible_facts')
    assert 'ansible_all_ipv4_addresses'

# Generated at 2022-06-13 00:17:28.881718
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    class TestCollector(collector.BaseFactCollector):

        name = 'test'

        def __init__(self, namespace=None, **kw):
            super(TestCollector, self).__init__(namespace=namespace)
            self.kw = kw

        def collect(self, module=None, collected_facts=None):
            collected_facts = collected_facts or {}
            collected_facts.update(self.kw)
            return collected_facts

    fact_collector = AnsibleFactCollector(collectors=[TestCollector(testkw=True)],
                                          filter_spec=None)
    assert fact_collector.collect() == {'ansible_test': True}


# Generated at 2022-06-13 00:17:35.278363
# Unit test for function get_ansible_collector
def test_get_ansible_collector():

    import ansible.module_utils.facts.hardware
    import ansible.module_utils.facts.network
    import ansible.module_utils.facts.system
    import ansible.module_utils.facts.virtual

    all_collector_classes = [
        ansible.module_utils.facts.hardware.Hardware,
        ansible.module_utils.facts.network.Network,
        ansible.module_utils.facts.system.System,
        ansible.module_utils.facts.virtual.Virtual,
    ]

    my_collector = get_ansible_collector(all_collector_classes=all_collector_classes)

    my_facts = my_collector.collect()

    assert my_facts['gather_subset'] == ['all'], my_facts

# Generated at 2022-06-13 00:17:46.336251
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    from ansible.module_utils.facts import collector
    from ansible.module_utils.facts.system.distribution import DistributionCollector
    from ansible.module_utils.facts.system.distribution.openbsd import OpenBSDCollector
    from ansible.module_utils.facts.system.distribution.fedora import FedoraCollector
    from ansible.module_utils.facts.system.distribution.debian import DebianCollector
    from ansible.module_utils.facts.system.distribution.arch import ArchCollector
    from ansible.module_utils.facts.system.distribution.suse import SuseCollector
    from ansible.module_utils.facts.system.distribution.gentoo import GentooCollector
    from ansible.module_utils.facts.system.distribution.mandriva import MandrivaCollector


# Generated at 2022-06-13 00:17:54.464181
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    assert get_ansible_collector(all_collector_classes=[collector.NetworkFactsCollector])
    assert get_ansible_collector(all_collector_classes=[collector.NetworkFactsCollector],
                                 filter_spec=['ansible_device*'])
    assert get_ansible_collector(all_collector_classes=[collector.NetworkFactsCollector],
                                 gather_subset=['!all'])
    assert get_ansible_collector(all_collector_classes=[collector.NetworkFactsCollector],
                                 gather_timeout=timeout.DEFAULT_GATHER_TIMEOUT)
    assert get_ansible_collector(all_collector_classes=[collector.NetworkFactsCollector],
                                 minimal_gather_subset=frozenset())


# Generated at 2022-06-13 00:18:06.659168
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    from ansible.module_utils.facts import namespace
    from ansible.module_utils.facts import network
    from ansible.module_utils.facts import systemd
    from ansible.module_utils.facts import time
    from ansible.module_utils.facts import virtual
    from ansible.module_utils.facts import ohai
    namespace_obj = namespace.PrefixFactNamespace(prefix='ansible_')
    collectors = [network.DefaultNetworkCollector(namespace=namespace_obj),
                  time.DefaultTimeCollector(namespace=namespace_obj),
                  virtual.DefaultVirtualCollector(namespace=namespace_obj),
                  ohai.DefaultOhaiCollector(namespace=namespace_obj)]
    fact_collector = AnsibleFactCollector(collectors=collectors)

# Generated at 2022-06-13 00:18:09.645155
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    """
    Verify that the AnsibleFactCollector.collect() method behaves properly
    when it receives invalid or valid input
    """
    assert False, 'No test for AnsibleFactCollector.collect() implemented yet'

# Generated at 2022-06-13 00:18:48.558702
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    # ansible_fact_collector = AnsibleFactCollector()

    class TestFactCollector(collector.BaseFactCollector):
        name = 'testing'
        _fact_ids = ['test1', 'test2']

        def collect(self, module=None, collected_facts=None):
            return {'test1': 'test1', 'test2': 'test2'}

    class TestFactCollector2(collector.BaseFactCollector):
        name = 'testing2'
        _fact_ids = ['test3', 'test4']

        def collect(self, module=None, collected_facts=None):
            return {'test3': 'test3', 'test4': 'test4'}


# Generated at 2022-06-13 00:18:59.347186
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    '''Test collect()'''

    from ansible.module_utils.facts.collector import Cache
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts.collector.network import NetworkCollector
    from ansible.module_utils.facts.collector.hardware import HardwareCollector
    from ansible.module_utils.facts.collector.platform import PlatformCollector

    namespace = PrefixFactNamespace(prefix='ansible_')
    collectors = [NetworkCollector(namespace=namespace), HardwareCollector(namespace=namespace),
                  PlatformCollector(namespace=namespace)]

    # Setup the collector
    fact_collector = AnsibleFactCollector(collectors=collectors, namespace=namespace)

    # Setup the cache with the collected facts


# Generated at 2022-06-13 00:19:06.971063
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    import collections
    import mock

    # Mock a CollectedFact class for the fact collector to use
    class TestFactMeta(collections.namedtuple('TestFactMeta', ['name', 'timeout'])):
        def __new__(cls, name, timeout):
            self = super(TestFactMeta, cls).__new__(cls, name, timeout)
            self.name = name
            self.timeout = timeout
            return self

    TestFactMeta.__name__ = 'TestFactMeta'

    test_fact_meta = TestFactMeta('test_fact', 0.5)

    # Assert that we can filter facts to just that fact. We will collect a 'test_fact'
    # and assert that it was filtered

# Generated at 2022-06-13 00:19:12.428652
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():

    class FakeCollector(collector.BaseFactCollector):
        name = None
        _fact_ids = set(["fake_fact"])

        def __init__(self, namespace=None):
            super(FakeCollector, self).__init__(namespace=namespace)

        def collect(self, module=None, collected_facts=None):
            return {'fake_fact': 'fake_value'}

    fact_collector = AnsibleFactCollector(namespace=None, collectors=[FakeCollector()])
    facts = fact_collector.collect()

    # test that returned facts are under 'ansible_facts' key
    assert 'ansible_facts' in facts
    assert facts['ansible_facts']['fake_fact'] == 'fake_value'



# Generated at 2022-06-13 00:19:13.194227
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    assert(0)

# Generated at 2022-06-13 00:19:21.459597
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    '''Unit test for function get_ansible_collector.'''
    from ansible.module_utils.facts import network
    from ansible.module_utils.facts import network_legacy
    from ansible.module_utils.facts import network_linux
    from ansible.module_utils.facts import network_ios

    assert get_ansible_collector([network,
                                  network_legacy,
                                  network_linux,
                                  network_ios],
                                 filter_spec=['ansible_lo'])

    assert get_ansible_collector([network,
                                  network_legacy,
                                  network_linux,
                                  network_ios],
                                 filter_spec=['ansible_lo'],
                                 gather_subset='!all,!min')


# Generated at 2022-06-13 00:19:32.423518
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts.system.distribution import DistributionFactCollector
    from ansible.module_utils.facts.system.distribution import LinuxDistributionFactCollector
    from ansible.module_utils.facts.system.distribution import BSDDistributionFactCollector
    from ansible.module_utils.facts.system.distribution import SolarisDistributionFactCollector

    ansible_namespace = PrefixFactNamespace(prefix='ansible_')
    all_collectors = [DistributionFactCollector, LinuxDistributionFactCollector, BSDDistributionFactCollector, SolarisDistributionFactCollector]

    filters = ['ansible_distribution', 'ansible_distribution_file_parsed']

# Generated at 2022-06-13 00:19:38.340124
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    gather_subset = ['all']
    fact_collector = \
        get_ansible_collector(all_collector_classes={'all': [collector.BaseFactCollector]},
                              namespace=None,
                              filter_spec=None,
                              gather_subset=gather_subset,
                              gather_timeout=None,
                              minimal_gather_subset=None)
    assert fact_collector is not None
    assert len(fact_collector.collectors) == 2
    for collector_obj in fact_collector.collectors:
        assert isinstance(collector_obj, collector.BaseFactCollector)