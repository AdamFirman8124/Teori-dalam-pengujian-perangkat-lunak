

# Generated at 2022-06-13 00:09:57.979789
# Unit test for method collect of class CollectorMetaDataCollector
def test_CollectorMetaDataCollector_collect():
    class mock_module:
        def __init__(self, collected_facts):
            self.collected_facts = collected_facts
    class mock_CollectorMetaDataCollector(CollectorMetaDataCollector):
        def __init__(self, collectors, namespace, gather_subset, module_setup):
            super(mock_CollectorMetaDataCollector, self).__init__(
                collectors, namespace, gather_subset, module_setup)
    # test

# Generated at 2022-06-13 00:10:03.341961
# Unit test for method collect of class CollectorMetaDataCollector
def test_CollectorMetaDataCollector_collect():
    from ansible.module_utils.facts import ansible_collector
    collector_meta_data_collector = ansible_collector.CollectorMetaDataCollector(gather_subset=['all'],
                                                                    module_setup=True)
    result = collector_meta_data_collector.collect()
    assert result == {'gather_subset': ['all'], 'module_setup': True}

# Generated at 2022-06-13 00:10:13.308128
# Unit test for method collect of class CollectorMetaDataCollector
def test_CollectorMetaDataCollector_collect():
    from ansible.module_utils.facts import ansible_collector
    import ansible.module_utils.facts.namespace as ns

    all_collector_classes = ansible_collector.FACT_COLLECTOR_CLASSES

    namespace = ns.PrefixFactNamespace(prefix='ansible_')
    gather_subset = ['all']

    collector_meta_data_collector = \
        CollectorMetaDataCollector(namespace=namespace,
                                   gather_subset=gather_subset)

    # Expect a single fact
    actual_facts = collector_meta_data_collector.collect()
    expected_facts = {'ansible_gather_subset': ['all'],
                      'ansible_module_setup': True}
    assert expected_facts == actual_facts

# Generated at 2022-06-13 00:10:26.712235
# Unit test for method collect of class CollectorMetaDataCollector
def test_CollectorMetaDataCollector_collect():

    collector_classes = {
        'facter': 'facter',
        'ohai': 'ohai',
        'puppet': 'puppet',
        'libvirt': 'libvirt',
        'virtualbox': 'virtualbox'
    }

    # If a module_setup is set to true, it should be present in the result
    collector_meta_data_collector = CollectorMetaDataCollector(module_setup=True)
    meta_facts = collector_meta_data_collector.collect()
    assert meta_facts['module_setup'] == True

    # Check if the result has the expected data
    collector_meta_data_collector = CollectorMetaDataCollector(gather_subset=collector_classes)
    meta_facts = collector_meta_data_collector.collect()

# Generated at 2022-06-13 00:10:35.657127
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    """Unit test for AnsibleFactCollector.collect()."""

    def _TestCollector(object):
        def collect(self, module=None, collected_facts=None):
            return {'foo': 'bar'}

    def test_collector():
        return _TestCollector()

    # test self.collect() with no namespacing
    fact_collector = get_ansible_collector(all_collector_classes=[test_collector])
    facts_dict = fact_collector.collect()
    assert facts_dict
    assert facts_dict['foo'] == 'bar'

    # test self.collect() with namespacing
    fact_collector = get_ansible_collector(all_collector_classes=[test_collector])

# Generated at 2022-06-13 00:10:48.658112
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    from . import test_utils
    from .test_utils import AnsibleFactCollectorTestCase

    class FakeAllCollectorClasses(object):
        def __iter__(self):
            return iter(test_utils.collector_classes)

    # pylint: disable=no-member
    all_collector_classes = FakeAllCollectorClasses()

    # copy test_utils.default_gather_subset over gather_subset
    gather_subset = test_utils.default_gather_subset[:]


# Generated at 2022-06-13 00:10:54.278599
# Unit test for method collect of class CollectorMetaDataCollector
def test_CollectorMetaDataCollector_collect():
    from ansible.module_utils.facts import namespace

    metadata_collector = CollectorMetaDataCollector(gather_subset=['all'],
                                                    module_setup=True)
    facts = metadata_collector.collect()
    assert facts == {'gather_subset': ['all'], 'module_setup': True}

# Generated at 2022-06-13 00:10:57.362789
# Unit test for method collect of class CollectorMetaDataCollector
def test_CollectorMetaDataCollector_collect():
    collclass = CollectorMetaDataCollector(gather_subset=['all'])
    result = collclass.collect()
    assert result == {'gather_subset': ['all']}

# Generated at 2022-06-13 00:11:02.270695
# Unit test for method collect of class CollectorMetaDataCollector
def test_CollectorMetaDataCollector_collect():
    collector_obj = CollectorMetaDataCollector(gather_subset='no_facts',
                                               module_setup=True)
    result = collector_obj.collect()
    assert result == {'gather_subset': 'no_facts', 'module_setup': True}

# Generated at 2022-06-13 00:11:07.112246
# Unit test for method collect of class CollectorMetaDataCollector
def test_CollectorMetaDataCollector_collect():
    collector_obj = CollectorMetaDataCollector(
                        gather_subset = ['hardware'],
                        module_setup = True)
    result = collector_obj.collect()

    # Expected result is as follows:
    # {
    #   "gather_subset": ["hardware"],
    #   "module_setup": True
    # }
    assert result == {'gather_subset': ['hardware'],
                      'module_setup': True}

# Generated at 2022-06-13 00:11:21.962989
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    from ansible.module_utils.facts import namespace
    from ansible.module_utils.facts import collectors

    class DummyCollector(collectors.BaseFactCollector):
        name = 'dummy'

        def collect(self, module=None, collected_facts=None):
            if collected_facts:
                return {self.get_fact_id(): collected_facts}
            return {self.get_fact_id(): self.namespace.prefix}

    class DummyCollectorError(collectors.BaseFactCollector):
        name = 'dummy_error'

        def collect(self, module=None, collected_facts=None):
            raise Exception('Collector %s failed' % self.name)

    # Test facts are collected into the ansible_facts namespace

# Generated at 2022-06-13 00:11:29.864670
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():

    # Test collection with no filter spec
    #   - ensures that the method correctly gathers facts
    #     and returns those facts at a top level key
    #     'ansible_facts'.
    #
    #   - ensures that facts can be collected when a fact
    #     depends on another fact.
    #
    #   - ensures that the method calls and returns
    #     the same number of facts that are collected by
    #     all of the collectors.
    #
    #   - ensures that facts that are collected by
    #     collectors are not returned if they are not
    #     defined by the collectors.

    mock_collectors = ['collector1', 'collector2', 'collector3']
    mock_collected_facts = {
        'fact1': 'foo',
        'fact2': 'bar'
    }

    mock_

# Generated at 2022-06-13 00:11:40.727828
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    from ansible.module_utils.facts import namespaces
    from ansible.module_utils.facts import collectors

    def test_collector(collector_class, collector_obj, filter_spec, namespace):
        '''Test that collector class returns a collector_obj under the expected
           namespace with the expected filter_spec'''
        assert isinstance(collector_obj, collector_class)
        assert collector_obj.filter_spec == filter_spec
        assert collector_obj.namespace == namespace

    # No namespace, just filter_spec
    fact_collector = \
        get_ansible_collector(all_collector_classes=collectors,
                              namespace=None,
                              filter_spec=['a*', 'b*'])
    assert fact_collector

# Generated at 2022-06-13 00:11:50.042314
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    from ansible.module_utils.facts import namespace
    from ansible.module_utils.facts import BaseFactCollector

    # Mocked class for unit testing.
    class MockCollector(BaseFactCollector):

        def collect(self, module=None, collected_facts=None):
            return {'mock': 'data'}

    fact_collector = AnsibleFactCollector([MockCollector()])

    result = fact_collector.collect()

    assert result == {'ansible_facts': {'mock': 'data'}}



# Generated at 2022-06-13 00:11:58.841162
# Unit test for function get_ansible_collector
def test_get_ansible_collector():

    from ansible.module_utils.facts.collector import BaseFactCollector

    class TestBaseFactCollector(BaseFactCollector):

        name = 'test'
        _fact_ids = set()

        def __init__(self, namespace=None, test_arg=None):
            super(TestBaseFactCollector, self).__init__(namespace=namespace)
            self.test_arg = test_arg

        def collect(self, module=None, collected_facts=None):
            facts = {}
            facts[self.get_fact_name('test_fact')] = {'test_arg': self.test_arg}
            return facts

    # No namespace

# Generated at 2022-06-13 00:11:59.448209
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    pass

# Generated at 2022-06-13 00:12:10.953385
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():

    # define a Mock class that implements method collect_with_namespace
    class MockAnsibleFactCollector(collector.BaseFactCollector):

        def collect_with_namespace(self, module=None, collected_facts=None):
            return {'a': 1}

    # create an instance of AnsibleFactCollector with one collector
    # that returns {'a':1} for any arg
    mock_obj = MockAnsibleFactCollector()
    fact_collector = \
        AnsibleFactCollector(collectors=[mock_obj],
                             filter_spec=None,
                             namespace=None)

    # collect facts
    facts = fact_collector.collect()

    # check if returned facts matches expected
    assert facts == {'a': 1}

# Generated at 2022-06-13 00:12:20.513251
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():

    import ansible.module_utils.facts.collector.network as network
    import ansible.module_utils.facts.collector.virtual as virtual
    import ansible.module_utils.facts.namespace as ns

    collectors_list = [
        virtual.VirtualCollector,
        network.NetworkCollector
    ]

    filter_spec = ['virtual']

    # Create a VirtualCollector object.
    namespace = ns.PrefixFactNamespace(prefix='ansible_')
    virtual_collector = virtual.VirtualCollector(namespace=namespace)

    # Create a NetworkCollector object.
    network_collector = network.NetworkCollector()

    # Create a list of collector objects, in this case VirtualCollector and NetworkCollector objects.
    collectors = [virtual_collector, network_collector]

    # Create an Ansible

# Generated at 2022-06-13 00:12:32.440642
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    test_classes = ['system', 'virtual']
    collector_classes = collector.collector_classes_from_gather_subset(all_collector_classes=test_classes)
    fact_collector = get_ansible_collector(all_collector_classes=test_classes,
                                           gather_timeout=timeout.DEFAULT_GATHER_TIMEOUT)
    # get_ansible_collector should have created a CollectorMetaDataCollector
    assert isinstance(fact_collector.collectors[0], CollectorMetaDataCollector)
    # get_ansible_collector should have created a collector for each class in test_classes.
    # [1:] because get_ansible_collector adds an extra collector
    assert len(fact_collector.collectors[1:]) == len(collector_classes)



# Generated at 2022-06-13 00:12:42.237143
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    from ansible.module_utils.facts import cache
    from ansible.module_utils.facts import core
    from ansible.module_utils.facts import network
    from ansible.module_utils.facts import system

    all_collector_classes = [
        cache.CacheFactCollector,
        core.CoreFactCollector,
        network.NetworkFactCollector,
        system.SystemFactCollector
    ]

    # test all collectors with default namespace
    fact_collector = get_ansible_collector(all_collector_classes=all_collector_classes)
    assert fact_collector.collectors
    assert isinstance(fact_collector.collectors, list)
    assert len(fact_collector.collectors) == 5
    for collector in fact_collector.collectors[0:4]:
        assert collector

# Generated at 2022-06-13 00:13:00.077413
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    import ansible.module_utils.facts.collectors.base
    import ansible.module_utils.facts.collectors.pipe_alias
    import ansible.module_utils.facts.collectors.distribution
    import ansible.module_utils.facts.collectors.network
    import ansible.module_utils.facts.collectors.platform
    import ansible.module_utils.facts.collectors.virtual


# Generated at 2022-06-13 00:13:10.259952
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    from ansible.module_utils.facts.collector.all import AllFactCollector

    all_collectors = AllFactCollector.collector_classes()
    subset_collectors = ['fake']
    collector = get_ansible_collector(all_collectors, subset_collectors)
    assert isinstance(collector, AnsibleFactCollector)

    collectors = collector.collectors
    assert isinstance(collectors, list)

    for collector in collectors:
        # FakeCollector is an already imported class which is not found in the all_collectors
        # it has been added to the collectors through the get_ansible_collector function
        assert collector.__class__.__name__ in subset_collectors + ['FakeCollector']

# Generated at 2022-06-13 00:13:20.467213
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():

    class MockFactsCollector(collector.BaseFactCollector):
        def collect(self, module=None, collected_facts=None):
            return {'test': 'test1'}

    class MockFactsCollector1(collector.BaseFactCollector):
        def collect(self, module=None, collected_facts=None):
            return {'test': 'test2'}

    mfc = MockFactsCollector()
    mfc1 = MockFactsCollector1()
    fc = AnsibleFactCollector(collectors=[mfc, mfc1],
                              filter_spec=None,
                              namespace=None)

    assert fc.collect() == {'test': 'test1'}

# Generated at 2022-06-13 00:13:27.739849
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    import ansible.module_utils.facts.ansible_collector
    import ansible.module_utils.facts.hardware
    import ansible.module_utils.facts.system

    test_collector_classes = [ansible.module_utils.facts.hardware.Hardware,
                              ansible.module_utils.facts.system.System,
                              ansible.module_utils.facts.ansible_collector.Ansible,
                              CollectorMetaDataCollector]

    test_collector = AnsibleFactCollector(collectors=test_collector_classes)
    facts_dict = test_collector.collect()

    assert len(facts_dict) > 0, 'Expected fact collected'
    assert not isinstance(facts_dict, list), 'Expected facts to be a dict'



# Generated at 2022-06-13 00:13:37.899398
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    from ansible.module_utils.facts import network
    from ansible.module_utils.facts import systems
    from ansible.module_utils.facts.namespace import PrefixFactNamespace

    gather_subset = ['network']
    gather_timeout = 0
    minimal_gather_subset = 'network'

    fact_collector = get_ansible_collector(
        all_collector_classes=[network.NetworkCollector,
                               systems.SystemsCollector],
        namespace=PrefixFactNamespace(prefix='ansible_'),
        filter_spec=[],
        gather_subset=gather_subset,
        gather_timeout=gather_timeout,
        minimal_gather_subset=minimal_gather_subset)

    facts = fact_collector.collect()

    # Make sure it returned

# Generated at 2022-06-13 00:13:43.040992
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    import ansible.module_utils.facts.collector.network
    import ansible.module_utils.facts.collector.hardware
    import ansible.module_utils.facts.collector.platform
    import ansible.module_utils.facts.collector.pkg_mgr
    import ansible.module_utils.facts.collector.virtual
    collect_obj = get_ansible_collector(all_collector_classes=
                                        ansible.module_utils.facts.collector.network.NetworkCollector.__subclasses__(),
                                        gather_subset=['all', 'network'],
                                        filter_spec=['ansible_*', 'facter_*', 'ohai_*'],
                                        minimal_gather_subset=frozenset(set(['!all', '!network'])))


# Generated at 2022-06-13 00:13:46.563339
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    class TestCollector(collector.BaseFactCollector):
        name = 'test'

    collector_class_list = [TestCollector]

    fact_collector = get_ansible_collector(all_collector_classes=collector_class_list)

    pass


# Generated at 2022-06-13 00:13:58.967191
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    import ansible.module_utils.facts.cloud
    import ansible.module_utils.facts.hardware
    import ansible.module_utils.facts.network
    import ansible.module_utils.facts.platform
    import ansible.module_utils.facts.system
    import ansible.module_utils.facts.virtual
    from ansible.module_utils.facts import namespace


# Generated at 2022-06-13 00:14:07.776491
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():

    class TestFactCollector(collector.BaseFactCollector):
        name = 'test'
        _fact_ids = set(['fact1'])

        def collect(self, module=None, collected_facts=None):
            return {'fact1': 'foo'}

    class TestFactCollector2(collector.BaseFactCollector):
        name = 'test2'
        _fact_ids = set(['fact2'])

        def collect(self, module=None, collected_facts=None):
            return {'fact2': 'bar'}

    # no filter specifier specified
    fact_collector = AnsibleFactCollector(collectors=[TestFactCollector(), TestFactCollector2()])
    result = fact_collector.collect()

# Generated at 2022-06-13 00:14:15.023751
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    class TestFactCollector(collector.BaseFactCollector):
        name = 'test'
        _fact_ids = set(['test_fact'])

        def collect(self, module=None, collected_facts=None):
            return {'test_fact': 'test_value'}

    fact_collector = AnsibleFactCollector(collectors=[TestFactCollector()])
    collected = fact_collector.collect()
    assert collected == {'test_fact': 'test_value'}



# Generated at 2022-06-13 00:14:34.950016
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    m_module = {}
    m_collected_facts = {'ansible_local': {}}

    class M_Collector(collector.BaseFactCollector):
        def collect(self, module=None, collected_facts=None):
            return {'a': 'b'}

    class F_Collector(M_Collector):
        def collect(self, module=None, collected_facts=None):
            return {'ansible_f': 'g'}

    m_collector = M_Collector(namespace='ansible_local')
    f_collector = F_Collector(namespace='ansible_local')

    # test
    ansible_fact_collector = AnsibleFactCollector([m_collector, f_collector], 'ansible_local')
    facts_dict = ansible_fact_

# Generated at 2022-06-13 00:14:47.115729
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    # We are going to mock the module object passed to this class
    # so we don't accidently call module.exit_json()
    class FakeModule:
        def __init__(self):
            self.params = {}

        def run_command(self, command, check_rc=True, executable=None):
            if command[0] == 'lsb_release':
                return (0, 'CentOS', '')
            elif command[0] == 'cat':
                return (0, '/dev/null', '')
            else:
                return (1, '', '')

    fake_module = FakeModule()

    class FakeFactCollector:
        def __init__(self):
            self.data = {'test_fact': 'first'}
            self.name = 'fake_fact'


# Generated at 2022-06-13 00:14:51.949475
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    all_collector_classes = \
        collector.collector_classes_from_gather_subset(gather_subset=['all'],
                                                       gather_timeout=timeout.DEFAULT_GATHER_TIMEOUT)
    collector_obj = get_ansible_collector(all_collector_classes=all_collector_classes)
    assert collector_obj is not None

# Generated at 2022-06-13 00:14:57.797011
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts.system.base import BaseFactCollector

    # Dummy class, only used for testing
    class DummyCollector(BaseFactCollector):
        name = 'dummy'

        def collect(self, module=None, collected_facts=None):
            return {
                self.get_fact_name('fact1'): 'value1',
                self.get_fact_name('fact2'): 'value2',
                'fact3': 'value3',
            }

    test_collector = DummyCollector(namespace=PrefixFactNamespace(prefix='test_'))
    fact_collector = AnsibleFactCollector(collectors=[test_collector])
    facts = fact_collector.collect

# Generated at 2022-06-13 00:15:09.608230
# Unit test for function get_ansible_collector
def test_get_ansible_collector():

    class CollectorClass(collector.BaseFactCollector):
        name = 'collectorClass'
        _fact_ids = set(['a', 'b', 'c'])

    class CollectorClass2(collector.BaseFactCollector):
        name = 'collectorClass2'
        _fact_ids = set(['d', 'e', 'f'])

    class CollectorClass3(collector.BaseFactCollector):
        name = 'collectorClass3'
        _fact_ids = set(['g', 'h', 'i'])

    filter_spec = ['*']
    cur_collector_classes = {}
    cur_collector_classes['collectorClass'] = CollectorClass
    cur_collector_classes['collectorClass2'] = CollectorClass2
    cur_collector_classes['collectorClass3'] = CollectorClass

# Generated at 2022-06-13 00:15:21.046701
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    from ansible.module_utils.facts import collector
    args = {
        'all_collector_classes': collector.__all__,
        'minimal_gather_subset': ['*'],
        'gather_subset': ['!all'],
        'gather_timeout': 10,
        'filter_spec': ['ansible_distribution_major_version'],
    }
    fact_collector = get_ansible_collector(**args)
    assert fact_collector.filter_spec == args['filter_spec']
    assert fact_collector._collector_metadata_collector.gather_subset == args['gather_subset']
    assert fact_collector._collector_metadata_collector.module_setup
    assert fact_collector.namespace is None
    assert fact_collector

# Generated at 2022-06-13 00:15:28.544880
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    class Collector1(AnsibleFactCollector):
        name = 'collector1'
        _fact_ids = set(['fact1', 'fact2'])

    class Collector2(AnsibleFactCollector):
        name = 'collector2'
        _fact_ids = set(['fact3', 'fact4'])

    c1 = Collector1()
    c2 = Collector2()

    c1.collect = lambda module, collected_facts: {'fact1': 'fact1'}
    c2.collect = lambda module, collected_facts: {'fact3': 'fact3'}

    fc = AnsibleFactCollector(collectors=[c1, c2])

    facts_dict = fc.collect()
    assert len(facts_dict) == 2
    assert 'collector1__fact1' in facts_

# Generated at 2022-06-13 00:15:37.650060
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    import ansible.module_utils.facts.system.distribution as distribution

    fact_collector = get_ansible_collector(all_collector_classes=[distribution.DistributionFactCollector],
                                           filter_spec=['ansible_distribution*'])

    # NOTE: tests will fail with 'No distribution detected' if we don't mock
    # facts_dict['ansible_facts']
    facts_dict = fact_collector.collect(module=None, collected_facts={})
    assert 'ansible_distribution' in facts_dict

# Generated at 2022-06-13 00:15:45.293777
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils.facts import default_minimal_collectors

    default_collector = \
        get_ansible_collector(all_collector_classes=default_collectors,
                              namespace='custom.ansible_',
                              gather_subset='all')

    # Verify we created an AnsibleFactCollector
    assert isinstance(default_collector, AnsibleFactCollector)

    # Verify we got the collectors we wanted
    assert len(default_collector.collectors) == len(default_collectors) + 1

    minimal_collector = \
        get_ansible_collector(all_collector_classes=default_collectors,
                              namespace='custom.ansible_',
                              gather_subset='min')



# Generated at 2022-06-13 00:15:55.953861
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    import ansible.module_utils.facts.collector.ansible_only as collected_ansible_only
    import ansible.module_utils.facts.collector.base as collected_base
    import ansible.module_utils.facts.collector.network as collected_network
    import ansible.module_utils.facts.collector.pkg_mgr as collected_pkg_mgr
    import ansible.module_utils.facts.collector.platform as collected_platform
    import ansible.module_utils.facts.collector.service_mgr as collected_service_mgr
    import ansible.module_utils.facts.collector.setup as collected_setup
    import ansible.module_utils.facts.collector.virtual as collected_virtual

    import ansible.module_utils.facts.namespace as namespace

# Generated at 2022-06-13 00:16:30.758569
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    from ansible.module_utils.facts.system.base import BaseFactCollector
    from ansible.module_utils.facts.system.distribution import DistributionFactCollector
    from ansible.module_utils.facts.system.platform import PlatformFactCollector

    base_fcollector = BaseFactCollector()
    dist_fcollector = DistributionFactCollector()
    plat_fcollector = PlatformFactCollector()

    ansible_fcollector = AnsibleFactCollector([base_fcollector,
                                               dist_fcollector,
                                               plat_fcollector])

    collected_facts = ansible_fcollector.collect()
    assert type(collected_facts) is dict
    assert collected_facts != {}



# Generated at 2022-06-13 00:16:38.909268
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    import sys

    collector_class = collector.collector_class_by_name('facter')
    collector_obj = collector_class()

    fact_collector = AnsibleFactCollector(collectors=[collector_obj])

    try:
        returned_facts = fact_collector.collect()
    except Exception as e:
        # we can't actually test exception raising in a module test because it will cause
        # a whole bunch of other tests to fail.
        sys.stderr.write(repr(e))
        sys.stderr.write('\n')
        returned_facts = {'failed': True,
                          'msg': repr(e)}

    assert 'facter_osfamily' in returned_facts

# Generated at 2022-06-13 00:16:40.168280
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    # TODO: implement unit test
    pass

# Generated at 2022-06-13 00:16:48.715271
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    from ansible.module_utils.facts import ansible_collector
    from ansible.module_utils.facts import network_collector
    from ansible.module_utils.facts import system_collector

    fact_collector = ansible_collector.AnsibleFactCollector(
        [
            # when both system and network are requested, this should go in this order
            # as system depends on network
            system_collector.SystemCollector(),
            network_collector.NetworkCollector()
        ],
        # when both system and network are requested, this should go in this order
        # as system depends on network
        ['ansible', 'network', 'system']
    )

    facts = fact_collector.collect()


# Generated at 2022-06-13 00:16:59.347906
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    import ansible.module_utils.facts.network.dns
    import ansible.module_utils.facts.network.interfaces
    import ansible.module_utils.facts.system.distribution

    fact_collector = AnsibleFactCollector(collectors=[
        ansible.module_utils.facts.network.dns.DnsCollector(),
        ansible.module_utils.facts.network.interfaces.InterfacesCollector()
    ])

    collected_facts = fact_collector.collect()
    assert set(collected_facts.keys()) == set(['ansible_dns', 'ansible_interfaces'])


# Generated at 2022-06-13 00:17:08.787200
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():

    from ansible.module_utils.facts import hardware
    from ansible.module_utils.facts import system
    from ansible.module_utils.facts import network
    from ansible.module_utils.facts.system.distribution import DistributionFactCollector
    from ansible.module_utils.facts.distribution.redhat import DistributionRedHatFactCollector
    from ansible.module_utils.facts.distribution.arch import DistributionArchFactCollector
    from ansible.module_utils.facts.distribution.freebsd import DistributionFreeBSDFactCollector
    from ansible.module_utils.facts.distribution.suse import DistributionSUSEFactCollector
    from ansible.module_utils.facts.distribution.openbsd import DistributionOpenBSDFactCollector
    from ansible.module_utils.facts.distribution.alpine import Distribution

# Generated at 2022-06-13 00:17:19.647611
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    # get_ansible_collector() is used in several places. If a call is added to one of those places
    # make sure a test is added here to test it.

    all_collector_classes = \
        collector.ALL_COLLECTOR_CLASSES().copy()
    all_collectors_dict = {}
    for collector_class in all_collector_classes:
        collector_obj = collector_class()
        all_collectors_dict[collector_obj.name] = collector_obj
    all_collectors_names = all_collectors_dict.keys()

    # test the default gather_subset
    fact_collector = get_ansible_collector(all_collector_classes=all_collector_classes)
    assert fact_collector.gather_subset == ['all']

    # test the default

# Generated at 2022-06-13 00:17:29.552413
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():

    # Setup stubs
    class StubCollector(object):
        def __init__(self, *args, **kwargs):
            super(StubCollector, self).__init__(*args, **kwargs)
            self.facts_dict = {}
            self.returned_facts_dict = {}

        def collect_with_namespace(self, module=None, collected_facts=None):
            collected_facts = collected_facts or {}
            # Shallow copy of the facts_dict to make each collector independent
            return self.facts_dict.copy()

    def stub_collector_factory(namespace):
        stub_collector = StubCollector(namespace=namespace)
        return stub_collector

    class StubNamespace(object):

        def __init__(self, prefix):
            self.prefix = prefix

       

# Generated at 2022-06-13 00:17:35.937600
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    from ansible.module_utils.facts.collector.legacy import DefaultFactCollector
    from ansible.module_utils.facts.collector.network import NetworkFactCollector
    from ansible.module_utils.facts.collector.pip import PipFactCollector
    from ansible.module_utils.facts.namespace.prefix import PrefixFactNamespace

    gs = ['network', 'pip']
    facts = get_ansible_collector(all_collector_classes=[NetworkFactCollector, PipFactCollector],
                                  gather_subset=gs,
                                  filter_spec=['*', 'n*'])

    # Test that the collectors were setup properly
    all_collectors = facts.collectors
    assert isinstance(all_collectors[0],
                      NetworkFactCollector)

# Generated at 2022-06-13 00:17:37.212428
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    pass

# Generated at 2022-06-13 00:18:38.550048
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():

    from ansible.module_utils.facts import cache
    from ansible.module_utils.facts import timeout

    all_collector_classes = collector.get_fact_collector_classes()

    module = None

    # fake the collected_facts

# Generated at 2022-06-13 00:18:48.096197
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    import json
    import os
    import sys
    import platform
    import socket
    import operator

    sys.path.append(os.path.join(os.path.dirname(__file__), '../../test/units/module_utils/facts'))

    from test_ansible_fact_collector import TestCollector
    from test_ansible_fact_collector import TestCollector1

    from ansible.module_utils.facts import namespace
    from ansible.module_utils.facts import default_collectors

    test_namespace = namespace.PrefixFactNamespace(prefix='prefix_')
    test_namespace1 = namespace.PrefixFactNamespace(prefix='prefix1_')


# Generated at 2022-06-13 00:18:58.922511
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    class FactCollector_test(collector.BaseFactCollector):
        name = 'fact'
        _fact_ids = set(['ansible_test'])

        def collect(self, module=None, collected_facts=None):
            return {'ansible_test': True}

    class FactCollector_skip(collector.BaseFactCollector):
        name = 'skip'
        _fact_ids = set(['ansible_skip'])

        def collect(self, module=None, collected_facts=None):
            return {'ansible_skip': True}

    ansible_fact_collector = AnsibleFactCollector(collectors=[FactCollector_test(namespace=''), FactCollector_skip(namespace='')])

# Generated at 2022-06-13 00:19:04.516351
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    '''test the get_ansible_collector function'''
    from ansible.module_utils.facts import linux
    from ansible.module_utils.facts import network
    from ansible.module_utils.facts import packages
    from ansible.module_utils.facts import virtual
    from ansible.module_utils.facts import aix
    from ansible.module_utils.facts import bsd
    from ansible.module_utils.facts import collector

    all_collector_classes = \
        collector.all_collector_classes_from_module(
            sys.modules[__name__],
            exclude_classes=[AnsibleFactCollector, CollectorMetaDataCollector])

    # call the function under test

# Generated at 2022-06-13 00:19:11.189023
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    '''Unit test for collect method of class AnsibleFactCollector'''

    #
    # Test with a fact collector that returns a single fact with a name matching the filter
    # pattern
    #
    class TestFactCollectorSingleFact(collector.BaseFactCollector):
        '''Test collector that returns a single fact.

        This collector returns a fact with name matching the filter_spec'''

        name = 'test_facts'
        _fact_ids = set([])

        def __init__(self, namespace=None):
            super(TestFactCollectorSingleFact, self).__init__(namespace=namespace)

        def collect(self, module=None, collected_facts=None):
            facts = {'my_fact': 'my_fact_value'}
            return facts


# Generated at 2022-06-13 00:19:20.254571
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    from ansible.module_utils.facts.collector.hardware import HardwareCollector
    from ansible.module_utils.facts.collector.network import NetworkCollector
    class FakeHardwareCollector(HardwareCollector):

        name = 'hardware'
        _fact_ids = set(['test_fact'])

        def collect(self, module=None, collected_facts=None):
            return {'test_fact': 'test_fact_val'}

    class FakeNetworkCollector(NetworkCollector):

        name = 'network'
        _fact_ids = set(['test_fact'])

        def collect(self, module=None, collected_facts=None):
            return {'test_fact': 'test_fact_val'}

    hardware_collector_obj = FakeHardwareCollector(namespace='')
    network

# Generated at 2022-06-13 00:19:28.327119
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    ansible_collector = get_ansible_collector(all_collector_classes=None,
                                              namespace=None,
                                              filter_spec=None,
                                              gather_subset=None,
                                              gather_timeout=None,
                                              minimal_gather_subset=None)

    stats = ansible_collector.collect()

    assert isinstance(stats, dict), "stats was not a dict"
    assert 'ansible_all_ipv4_addresses' in stats, "ansible_all_ipv4_addresses not in stats"


# Generated at 2022-06-13 00:19:35.194450
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    fact_collector = AnsibleFactCollector()
    ansible_facts_dict = fact_collector.collect()
    assert 'system' in ansible_facts_dict
    assert 'distribution' in ansible_facts_dict['system']
    assert ansible_facts_dict['system']['distribution'] == 'other'
    assert 'network' in ansible_facts_dict
    assert 'interfaces' in ansible_facts_dict['network']
    assert 'lo' in ansible_facts_dict['network']['interfaces']

# Generated at 2022-06-13 00:19:40.132023
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    import ansible.module_utils.facts.collector.network

    collectors = [collector.NetworkCollector()]
    namespace = None
    fact_collector = AnsibleFactCollector(collectors=collectors, namespace=namespace)

    # First test that a fact not in the fact_collector isn't returned
    filter_spec = None
    facts_dict = fact_collector.collect(filter_spec=filter_spec)
    assert 'ansible_facts' in facts_dict
    assert 'ansible_interfaces' not in facts_dict['ansible_facts']

    # Now test that a fact_collector can filter the results
    filter_spec = 'ansible_facts.*_interfaces'
    facts_dict = fact_collector.collect(filter_spec=filter_spec)