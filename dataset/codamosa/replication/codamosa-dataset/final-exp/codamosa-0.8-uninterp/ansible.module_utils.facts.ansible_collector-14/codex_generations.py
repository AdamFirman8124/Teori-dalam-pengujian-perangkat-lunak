

# Generated at 2022-06-13 00:09:51.907605
# Unit test for method collect of class CollectorMetaDataCollector
def test_CollectorMetaDataCollector_collect():
    expected_meta_facts = {'gather_subset': ['all'],
                           'module_setup': True}

# Generated at 2022-06-13 00:10:00.001955
# Unit test for method collect of class CollectorMetaDataCollector
def test_CollectorMetaDataCollector_collect():
    # Create CollectorMetaDataCollector object
    test_gather_subset = ['all']
    test_module_setup = True
    meta_collector = CollectorMetaDataCollector(gather_subset=test_gather_subset,
                                                module_setup=test_module_setup)
    # Call collect method
    meta_facts = meta_collector.collect()
    # Assert expected results
    assert meta_facts['gather_subset'] == test_gather_subset
    assert meta_facts['module_setup'] == test_module_setup

# Generated at 2022-06-13 00:10:02.981328
# Unit test for method collect of class CollectorMetaDataCollector
def test_CollectorMetaDataCollector_collect():
    c = CollectorMetaDataCollector(namespace='ansible_', gather_subset=['!all', 'min'], module_setup=False)
    facts = c.collect()
    assert facts['ansible_gather_subset'] == ['!all', 'min']
    assert 'ansible_module_setup' not in facts



# Generated at 2022-06-13 00:10:09.184228
# Unit test for method collect of class CollectorMetaDataCollector
def test_CollectorMetaDataCollector_collect():

    fact_collector = CollectorMetaDataCollector(gather_subset=['all'],
                                                module_setup=True)

    res = fact_collector.collect()
    assert res is not None
    assert 'gather_subset' in res.keys()
    assert 'module_setup' in res.keys()
    assert res['gather_subset'] == ['all']
    assert res['module_setup'] is True

# Generated at 2022-06-13 00:10:13.756293
# Unit test for method collect of class CollectorMetaDataCollector
def test_CollectorMetaDataCollector_collect():
    collect_subset='all'
    module_setup=True
    collector_meta_data_collector = CollectorMetaDataCollector(gather_subset=collect_subset,
                                   module_setup=module_setup)
    fact=collector_meta_data_collector.collect()
    assert fact['gather_subset'] == collect_subset
    assert fact['module_setup'] == module_setup

# Generated at 2022-06-13 00:10:26.866663
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    from ansible.module_utils.facts import collector
    from ansible.module_utils.facts import ansible_collector
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts.namespace import SimpleFactNamespace

    # test all collectors
    fact_collector = ansible_collector.get_ansible_collector(
        all_collector_classes=collector.all_collector_classes(),
        minimal_gather_subset=['all'],
        namespace=None)

    # test all with ansible_ facts

# Generated at 2022-06-13 00:10:31.378065
# Unit test for method collect of class CollectorMetaDataCollector
def test_CollectorMetaDataCollector_collect():
    from ansible.module_utils.facts import ansible_collector
    from ansible.module_utils.facts import ansible_local
    from ansible.module_utils.facts import network
    from ansible.module_utils.facts import ohai
    from ansible.module_utils.facts import virtual
    from ansible.module_utils.facts.system.dns import DNSFactCollector
    from ansible.module_utils.facts.system.pkg_mgr import PkgMgrFactCollector
    from ansible.module_utils.facts.system.pkg_mgr import PkgMgrFactCollector
    from ansible.module_utils.facts.system.platform import PlatformFactCollector
    from ansible.module_utils.facts.system.service_mgr import ServiceMgrFactCollector

# Generated at 2022-06-13 00:10:34.165271
# Unit test for method collect of class CollectorMetaDataCollector
def test_CollectorMetaDataCollector_collect():
    meta_data_collector = CollectorMetaDataCollector(gather_subset=['all'])
    meta_facts = meta_data_collector.collect()
    assert meta_facts['gather_subset'] == ['all']


# Generated at 2022-06-13 00:10:47.125644
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    '''
    Unit test for method collect of class AnsibleFactCollector
    '''
    from ansible.module_utils.facts.namespace import PrefixFactNamespace

    class MockFactCollector1(collector.BaseFactCollector):
        def __init__(self, namespace):
            super(MockFactCollector1, self).__init__(namespace=namespace)

        def collect(self, module=None, collected_facts=None):
            return {'platform': 'platform_fact'}

    class MockFactCollector2(collector.BaseFactCollector):
        def __init__(self, namespace):
            super(MockFactCollector2, self).__init__(namespace=namespace)


# Generated at 2022-06-13 00:10:54.004592
# Unit test for method collect of class CollectorMetaDataCollector
def test_CollectorMetaDataCollector_collect():
    import ansible.module_utils.facts.dynamic_module.collector_metadata as c
    collector_mdc = c.CollectorMetaDataCollector(gather_subset=['all'], module_setup=False)
    meta_facts = collector_mdc.collect()
    assert meta_facts['gather_subset'] == ['all']
    assert 'module_setup' not in meta_facts.keys()


# Generated at 2022-06-13 00:11:08.025633
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    from ansible.module_utils.facts import collector

    class Collect1(collector.BaseFactCollector):
        name = 'collector1'
        _fact_ids = {'collect1', 'collect2'}

        def collect(self, module=None, collected_facts=None):
            return {'collect1': 'val1', 'collect2': 'val2'}

    class Collect2(collector.BaseFactCollector):
        name = 'collector2'

        def collect(self, module=None, collected_facts=None):
            return {}

    class Collect3(collector.BaseFactCollector):
        name = 'collector3'

        def collect(self, module=None, collected_facts=None):
            return {'collect3': 'val3'}

    fact_collector = AnsibleFactCollector

# Generated at 2022-06-13 00:11:15.995713
# Unit test for function get_ansible_collector
def test_get_ansible_collector():

    collector_obj = get_ansible_collector(all_collector_classes=set(),
                                          namespace=None,
                                          gather_subset=None,
                                          gather_timeout=None,
                                          minimal_gather_subset=None)

    assert isinstance(collector_obj, AnsibleFactCollector)

    # just the metadata collector
    assert len(collector_obj.collectors) == 1
    assert collector_obj.collectors[0].name == 'gather_subset'

# Generated at 2022-06-13 00:11:24.433137
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    from ansible.module_utils.facts.collector import FacterFactCollector, OhaiFactCollector
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts.namespace import FactNamespace

    fact_namespace = PrefixFactNamespace(prefix='my_')

    # FactCollector that collects facter and ohai
    fact_collector = AnsibleFactCollector(
        collectors=[
            fact_namespace(FacterFactCollector()),
            fact_namespace(OhaiFactCollector())
        ],
        namespace=FactNamespace(),
    )
    ansible_facts = fact_collector.collect(collected_facts=dict(my_facter=dict()),
                                           module=dict())

    # Only expect facter and ohai

# Generated at 2022-06-13 00:11:32.111753
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts import cached
    from ansible.module_utils.facts import platform

    fact_collector = AnsibleFactCollector(collectors=[cached.CachedFactCollector(),
                                                      platform.PlatformFactCollector()],
                                          namespace=PrefixFactNamespace(prefix='ansible_'))
    collected_facts = fact_collector.collect()
    ansible_platform_facts = collected_facts.get('ansible_facts')

    assert ansible_platform_facts is not None
    assert ansible_platform_facts.get('ansible_distribution') is not None



# Generated at 2022-06-13 00:11:43.044567
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    # Note that currently the AnsibleFactCollector class only
    # returns facts collected by the collectors in its collector list
    # The unit test here is essentially the same as the unit test
    # for class BaseFactCollector
    #
    # See test_BaseFactCollector_collect
    #
    # However, it is useful to keep test_AnsibleFactCollector_collect
    # in this file to document the simple usage of class
    # AnsibleFactCollector.
    #

    class MockCollector():

        name = 'mock'

        def __init__(self, namespace=None):
            self.namespace = namespace

        def collect_with_namespace(self):
            return {self.namespace: True}

    mock_collector = MockCollector(namespace='mock_namespace')


# Generated at 2022-06-13 00:11:54.410254
# Unit test for function get_ansible_collector
def test_get_ansible_collector():

    import ansible.module_utils.facts
    import ansible.module_utils.network.common.utils

    from ansible.module_utils import basic

    all_collector_classes = collector.get_collector_classes(
        root_dirs=[ansible.module_utils.facts.__path__[0],
                   ansible.module_utils.network.common.utils.__path__[0],
                   basic.__path__[0]])

    gather_subset = ['all', '!foo']

    fact_collector = \
        get_ansible_collector(all_collector_classes=all_collector_classes,
                              gather_subset=gather_subset)

    assert isinstance(fact_collector, AnsibleFactCollector)

# Generated at 2022-06-13 00:12:04.352842
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    from ansible.module_utils.facts import command
    from ansible.module_utils.facts import default
    from ansible.module_utils.facts import hardware
    from ansible.module_utils.facts import virtual
    from ansible.module_utils.facts.system import distro
    from ansible.module_utils.facts.system import ipv4_addresses
    from ansible.module_utils.facts.system import ipv6_addresses
    from ansible.module_utils.facts.system import network
    from ansible.module_utils.facts.system import selinux


# Generated at 2022-06-13 00:12:14.779756
# Unit test for function get_ansible_collector
def test_get_ansible_collector():

    class FakeCollector(collector.BaseFactCollector):
        def collect(self, module=None, collected_facts=None):
            return {'collector': 'truth'}

    import mock

    class FakeModule(object):
        def __init__(self):
            self.params = {}

    with mock.patch.object(collector, 'collector_classes_from_gather_subset') as \
        mock_collector_classes_from_gather_subset:
        mock_collector_classes_from_gather_subset.return_value = [FakeCollector]

# Generated at 2022-06-13 00:12:27.474811
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    from ansible.module_utils.facts import fact_cache
    from ansible.module_utils.facts import cache
    from ansible.module_utils.facts import cache_manager
    from ansible.module_utils.facts import bare

    all_collector_classes = {
        'bare': bare.BareFactCollector,
        'fact_cache': fact_cache.FactCacheCollector,
        'cache': cache.CacheCollector,
        'cache_manager': cache_manager.CacheManagerCollector,
    }
    namespace = None
    filter_spec = None
    gather_subset = 'all'
    gather_timeout = None
    minimal_gather_subset = frozenset()


# Generated at 2022-06-13 00:12:38.844239
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():

    class MockCollector(collector.BaseFactCollector):
        name = 'mock_collector'

        def collect(self, module=None, collected_facts=None):
            return {'mock_fact1': 'mock_fact_value1',
                    'mock_fact2': 'mock_fact_value2'}

    class MockCollectorMatchingFilter(collector.BaseFactCollector):
        name = 'mock_collector_matching_filter'

        def collect(self, module=None, collected_facts=None):
            return {'ansible_mock_fact1': 'ansible_mock_fact_value1',
                    'ansible_mock_fact2': 'ansible_mock_fact_value2'}

    module = {}

    mock_collector = MockCollector()

# Generated at 2022-06-13 00:12:55.972791
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    # mock a class to be used as a module
    class MockClass(object):
        pass

    mock_module = MockClass()
    mock_module.params = {}

    # mock a class to be used as the wanted ansible_facts
    class AnsibleFactMockClass(object):
        def __init__(self):
            self.dict = {}

        def update(self, other):
            self.dict.update(other)

        def __contains__(self, item):
            return item in self.dict

        def __getitem__(self, key):
            return self.dict[key]

    # mock a class to be used as the collectors
    class CollectorMockClass(object):
        def __init__(self, namespace=None):
            self.namespace = namespace


# Generated at 2022-06-13 00:13:04.015142
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():

    from ansible.module_utils.facts.hardware import hardware
    from ansible.module_utils.facts.system import system
    from ansible.module_utils.facts.virtual import virtual

    # Create a list of FactCollector objects for testing
    hw_collector = hardware.Hardware(namespace=hardware.HARDWARE_KEY)
    system_collector = system.System(namespace=system.SYSTEM_KEY)
    virtual_collector = virtual.Virtual(namespace=virtual.VIRTUAL_KEY)
    fact_collectors = [hw_collector, system_collector, virtual_collector]

    # Create an AnsibleFactCollector object for testing
    ansible_fact_collector = AnsibleFactCollector(collectors=fact_collectors,
                                                  namespace='ansible_')

    # Initial

# Generated at 2022-06-13 00:13:06.512214
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    m = collector.BaseFactCollector._get_platform_info_data('Linux')
    print(m)

# Generated at 2022-06-13 00:13:14.872685
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    ''' Test for method collect of class AnsibleFactCollector

    Test a collect method of AnsibleFactCollector by using mocked objects.
    '''
    from copy import copy
    from unittest.mock import Mock, call
    from ansible.module_utils.facts.collector.base import BaseFactCollector
    from ansible.module_utils.facts.collector.facter import FacterFactCollector
    from ansible.module_utils.facts.namespace import PrefixFactNamespace

    # A mocked list of fact collectors
    fact_collectors = [
        Mock(spec=BaseFactCollector),
        Mock(spec=BaseFactCollector),
        Mock(spec=BaseFactCollector),
        Mock(spec=BaseFactCollector),
    ]

    # A mocked filter spec

# Generated at 2022-06-13 00:13:22.557602
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    '''Unit test for method collect of class AnsibleFactCollector'''

    # Create two objects derived from BaseFactCollector
    class FactCollectorA(collector.BaseFactCollector):
        pass

    class FactCollectorB(collector.BaseFactCollector):
        pass

    # Create a list of the objects.
    collectors = [FactCollectorA(), FactCollectorB()]

    # Create the AnsibleFactCollector and call the collect method.
    afc = AnsibleFactCollector(collectors=collectors)
    facts = afc.collect(collected_facts={'a': 12})

    # The collect method should return an empty dictionary
    assert len(facts) == 0



# Generated at 2022-06-13 00:13:29.124990
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    expected = \
        'ansible.module_utils.facts.collector.AnsibleFactCollector(collectors=[ansible.module_utils.facts.collector.CollectorMetaDataCollector(gather_subset=set([u\'all\']), module_setup=True), ansible.module_utils.facts.collector.GenericFactCollector(namespace=ansible.module_utils.facts.namespace.PrefixFactNamespace(prefix=u\'ansible_\'), fact_ids=[u\'all\'])], namespace=ansible.module_utils.facts.namespace.PrefixFactNamespace(prefix=u\'ansible_\'))'

# Generated at 2022-06-13 00:13:38.926268
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    import ansible.module_utils.facts.collector
    import ansible.module_utils.facts.system.distribution
    import ansible.module_utils.facts.network.interfaces

    all_collector_classes = [
        ansible.module_utils.facts.collector.Collector,
        ansible.module_utils.facts.system.distribution.DistributionCollector,
        ansible.module_utils.facts.network.interfaces.NetworkInterfacesCollector
    ]

    collector = get_ansible_collector(all_collector_classes=all_collector_classes,
                                      gather_subset=['all'],
                                      filter_spec=[u'*interfaces'])
    assert collector.collectors[0].name == 'distribution'

# Generated at 2022-06-13 00:13:46.211877
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    # GIVEN
    fact_namespace = 'ansible_'
    fact_collector = AnsibleFactCollector(namespace=fact_namespace,
                                          filter_spec=None)
    module_collector_class = collector.BaseFactCollector
    module_collector_object = module_collector_class(namespace=fact_namespace)

    # WHEN
    fact_namespace = ''
    module_collector = module_collector_object.collect_with_namespace()

    # THEN
    assert module_collector is not None

# Generated at 2022-06-13 00:13:53.056922
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    class C1(collector.BaseFactCollector):
        pass

    class C2(collector.BaseFactCollector):
        pass

    all_collector_classes = [C1, C2]

    # test gather_subset=all, collector_classes=all_collector_classes
    answer = get_ansible_collector(all_collector_classes)

    assert len(answer.collectors) is 3
    assert answer.collectors[0].__class__ is C1
    assert answer.collectors[1].__class__ is C2
    assert answer.collectors[2].__class__ is CollectorMetaDataCollector
    assert answer.collectors[2].module_setup is True
    assert answer.collectors[2].gather_subset == ['all']

    # test gather_subset=all, collector_

# Generated at 2022-06-13 00:13:59.066276
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    from ansible.module_utils.facts import collector
    from ansible.module_utils.facts.system.distribution import DistributionFactCollector
    from ansible.module_utils.facts.system.distribution import PopenDistributionFactCollector
    from ansible.module_utils.facts.system.distribution import NonLinuxDistributionFactCollector
    collectors = [
        DistributionFactCollector(),
        PopenDistributionFactCollector(),
        NonLinuxDistributionFactCollector(),
    ]
    fact_collector = \
        AnsibleFactCollector(collectors=collectors, namespace=None)
    facts = fact_collector.collect()
    print(facts)

    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    namespace = PrefixFactNamespace(prefix='ansible_')
    fact_

# Generated at 2022-06-13 00:14:19.261778
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    class FakeCollector1_1():
        def collect(self):
            return {'ansible_fact_1': '1'}

    class FakeCollector2_2():
        def collect(self):
            return {'ansible_fact_1': '1'}

    f = AnsibleFactCollector(collectors=[FakeCollector1_1(), FakeCollector2_2()])
    facts = f.collect()
    assert 'ansible_fact_1' in facts
    assert facts['ansible_fact_1'] == '1'

# Generated at 2022-06-13 00:14:22.914693
# Unit test for function get_ansible_collector
def test_get_ansible_collector():

    # Just test that we can create an AnsibleFactCollector, not what collected facts are
    ansible_collector = get_ansible_collector(all_collector_classes=[])
    assert isinstance(ansible_collector, AnsibleFactCollector)

# Generated at 2022-06-13 00:14:32.648817
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    class Collector1(collector.BaseFactCollector):
        name = 'Collector1'

        def collect(self):
            facts = {}
            facts['included1'] = 1
            facts['included2'] = 'one'
            facts['included3'] = ['one']
            facts['excluded1'] = {'excluded1': 1}
            facts['excluded2'] = ['excluded2']
            return facts

    class Collector2(collector.BaseFactCollector):
        name = 'Collector2'

        def collect(self):
            facts = {}
            facts['included2'] = 'two'
            facts['included3'] = ['two']
            facts['excluded2'] = ['excluded2']
            return facts

    namespace = collector.PrefixFactNamespace(prefix='test_')

   

# Generated at 2022-06-13 00:14:45.100582
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    from ansible.module_utils.facts import default

    # set up minimal fact collection
    fact_collector = get_ansible_collector(
        all_collector_classes=default.FACT_COLLECTOR_CLASSES,
        namespace=None,
        filter_spec=None,
        gather_subset=['all'],
        gather_timeout=None,
        minimal_gather_subset=['all'])

    # do the collection
    collected_facts = fact_collector.collect()


# Generated at 2022-06-13 00:14:51.733249
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    class Fact(object):
        def __init__(self, fact_id):
            self.fact_id = fact_id
        def collect(self):
            return self.fact_id

    fact1 = Fact('fact1')
    fact2 = Fact('fact2')

    fact_collector = AnsibleFactCollector(collectors=[fact1, fact2])
    facts_dict = fact_collector.collect()

    assert facts_dict == {'fact1': 'fact1', 'fact2': 'fact2'}


# Generated at 2022-06-13 00:14:58.682072
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    collect_dict = {
        'name-space': {
            'fact_name': 'fact_value'
        }
    }

    class FactCollector(collector.BaseFactCollector):
        def __init__(self, namespace=None):
            super(FactCollector, self).__init__(namespace=namespace)

        def collect(self, module=None, collected_facts=None):
            return collect_dict

    fact_collector = AnsibleFactCollector([FactCollector('name-space')])
    ansible_facts = fact_collector.collect()

    assert ansible_facts == {'ansible_facts': {'name-space': collect_dict['name-space']}}

# Generated at 2022-06-13 00:15:10.804778
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    from ansible.module_utils.facts.collector.network import NetworkCollector
    from ansible.module_utils.facts.collector.platform import PlatformCollector

    collectors = get_ansible_collector(all_collector_classes=collector.FACT_COLLECTORS)
    facts_dict = collectors.collect()

    assert 'ansible_facts' in facts_dict
    assert 'ansible_facts' in facts_dict['ansible_facts']
    assert 'gather_subset' in facts_dict['ansible_facts']
    assert 'ansible_architecture' in facts_dict['ansible_facts']
    assert 'ansible_all_ipv4_addresses' in facts_dict['ansible_facts']

    network_collector = NetworkCollector(namespace=None)

# Generated at 2022-06-13 00:15:21.431940
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    all_collector_classes = \
        collector.get_collector_classes(resolved_namespaces=None)

    gather_subset = ['network', 'virtual', 'hardware']
    filter_spec = [
        'ansible_*', 'facter_*', 'ohai_*', 'netstat.all_tcp', 'netstat.all_udp',
        'netstat.tunnels'
    ]

    facts_collector = \
        get_ansible_collector(
            all_collector_classes=all_collector_classes,
            gather_subset=gather_subset,
            filter_spec=filter_spec,
            gather_timeout=5)

    gathered_facts = facts_collector.collect()

# Generated at 2022-06-13 00:15:25.459394
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    fake_collector = collector.BaseFactCollector(namespace=None)
    fake_collector.name = 'fake'
    fake_collector.collect_with_namespace = lambda x, y: {'a': 1}

    fact_collector = AnsibleFactCollector(collectors=[fake_collector], filter_spec=None)
    fact_dict = fact_collector.collect()

    assert fact_dict == {'a': 1}


# Generated at 2022-06-13 00:15:37.312038
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    ''' AnsibleFactCollector.collect() returns a dict under 'ansible_facts' top level key.'''

    class FakeFactCollector(collector.BaseFactCollector):

        def collect(self, module=None, collected_facts=None):
            return {'test': 'testval'}

    fact_collector = \
        AnsibleFactCollector(collectors=[FakeFactCollector()],
                             filter_spec=[])

    facts_dict = fact_collector.collect()
    assert 'ansible_facts' in facts_dict
    assert 'test' in facts_dict['ansible_facts']
    assert 'testval' == facts_dict['ansible_facts']['test']


# Generated at 2022-06-13 00:15:59.661887
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    class FakeFactCollector1(collector.BaseFactCollector):
        def collect(self, module=None, collected_facts=None):
            return {'factor1': 'val1',
                    'facto2': 'val2'}

    class FakeFactCollector2(collector.BaseFactCollector):
        def collect(self, module=None, collected_facts=None):
            return {'fact3': 'val3',
                    'fact4': 'val4'}

    # Use '*' as filter_specifier
    fact_collector = AnsibleFactCollector(collectors=[FakeFactCollector1(), FakeFactCollector2()],
                                          filter_spec='*',
                                          namespace=None)

# Generated at 2022-06-13 00:16:07.256019
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    '''
    To run this test on your local machine, follow the instructions below:

    1.  Define below the test_fact_dict as a python dictionary
        that contains the set of facts to be returned by the test.

    2.  Update the method collect of class TestableFactCollector below to return
        the test_fact_dict.

    3.  Execute this file using python on your local machine:
        python -m ansible.module_utils.facts.test.test_collector
    '''

    import os
    import sys
    import unittest

    from ansible.module_utils.facts import module
    from ansible.module_utils.facts import namespaced_fact
    from ansible.module_utils.facts import facts_module
    from ansible.module_utils.facts import collector


# Generated at 2022-06-13 00:16:14.286576
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    # pylint: disable=protected-access
    """ Test that the AnsibleFactCollector._filter function filters facts
        in case of several dicts.
    """
    collector_ = AnsibleFactCollector()
    collector_._filter_spec = "*"
    filtered_facts = collector_._filter({'a':1, 'b':2}, [''])
    assert filtered_facts == {'a': 1, 'b': 2}
    filtered_facts = collector_._filter({'a':1, 'b':2, 'c':3}, [''])
    assert filtered_facts == {'a': 1, 'b': 2, 'c': 3}
    filtered_facts = collector_._filter({'a':1, 'b':2}, ['*'])
    assert filtered_facts == {'a': 1, 'b': 2}

# Generated at 2022-06-13 00:16:15.823759
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    # It is not possible to unit test this method because AnsibleModule's instance
    # is required as argument.
    pass

# Generated at 2022-06-13 00:16:22.879252
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    from ansible.module_utils.facts.hardware.cpu import CpuCollector, CpuFactNamespace
    from ansible.module_utils.facts.system.distribution import DistributionCollector
    from ansible.module_utils.facts.system.platform import PlatformCollector

    cpu_collector = CpuCollector(namespace=CpuFactNamespace())
    distribution_collector = DistributionCollector()
    platform_collector = PlatformCollector()

    ansible_fact_collector = AnsibleFactCollector([cpu_collector, distribution_collector, platform_collector])

    facts = ansible_fact_collector.collect()

    assert 'ansible_facts' in facts
    assert 'ansible_processor_count' in facts['ansible_facts']
    assert 'ansible_all_ipv4_addresses'

# Generated at 2022-06-13 00:16:32.859578
# Unit test for function get_ansible_collector
def test_get_ansible_collector():

    from ansible.module_utils.facts import ansible_collector
    from ansible.module_utils.facts import ansible_local_collector
    from ansible.module_utils.facts import hardware_collector
    from ansible.module_utils.facts import network_collector

    ac = get_ansible_collector(all_collector_classes=[ansible_collector,
                                                      ansible_local_collector,
                                                      hardware_collector,
                                                      network_collector],
                               filter_spec='*',
                               gather_subset='all',
                               gather_timeout=None,
                               minimal_gather_subset=None)

    facts=ac.collect()
    assert isinstance(facts, dict)
    assert 'ansible_facts' in facts

# Generated at 2022-06-13 00:16:43.795376
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    from ansible.module_utils.facts import namespace

    # Collect namespaced facts
    ns = namespace.PrefixFactNamespace(prefix='my_')
    actual = AnsibleFactCollector(namespace=ns).collect({'ansible_facts': {'my_v': 1,
                                                                           'bar': 2,
                                                                           'facts': {
                                                                               'foo': 3
                                                                           }}})
    expected = {'v': 1, 'bar': 2,
                'facts': {'foo': 3}}
    assert actual == expected

    # Collect non namespaced facts
    ns = namespace.FactNamespace()

# Generated at 2022-06-13 00:16:48.797007
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    ''' Unitary test for method collect of class AnsibleFactCollector '''

    # First create some collectors and add them in a list
    collectors = []
    collector1 = CollectorMetaDataCollector(gather_subset=['min'])
    collector2 = CollectorMetaDataCollector(gather_subset=['all'])

    collectors.append(collector1)
    collectors.append(collector2)

    # Create a collector with a custom filter
    fact_collector = AnsibleFactCollector(collectors=collectors,
                                     filter_spec='ansible_*')

    # Call the method to test
    result = fact_collector.collect()

    # Verify the results
    assert len(result) == 1
    assert result['ansible_gather_subset'] == ['all']

# Generated at 2022-06-13 00:16:59.434574
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    def test_collector_collect(collected_facts=None):
        return { 'test_key1': 'test_value1', 'test_key2': 'test_value2' }

    class TestCollector(collector.BaseFactCollector):
        name = 'test_collect'
        _fact_ids = set(['test_key1', 'test_key2'])

        def __init__(self, namespace):
            super(TestCollector, self).__init__(namespace=namespace)

        def collect(self, module=None, collected_facts=None):
            return test_collector_collect(collected_facts=collected_facts)

    # test with no_log=True (default)
    fact_collector = AnsibleFactCollector(collectors=[])

# Generated at 2022-06-13 00:17:08.849578
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    all_collector_classes = collector.AllCollectorFactNamespace.collector_classes
    namespace = collector.AllCollectorFactNamespace
    collector_obj = get_ansible_collector(all_collector_classes=all_collector_classes,
                                          namespace=namespace)

    #I'm not seeing how I can test 'collected_facts' with this function.
    #'collected_facts' for a given host is the output of
    #a previous 'setup' call. I don't see how to mock that here.
    collected_facts = {}
    facts = collector_obj.collect(collected_facts=collected_facts)
    return facts

if __name__ == '__main__':
    import json
    import pprint

    facts = test_get_ansible_collector()

# Generated at 2022-06-13 00:17:54.828803
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    from ansible.module_utils.facts import default_collector_classes

    all_collector_classes = default_collector_classes()

    c = get_ansible_collector(all_collector_classes)

    # The fact collector has a collector that knows the gather_subset fact
    gather_subset_fact_key = CollectorMetaDataCollector.name

    facts_dict = c.collect()
    assert gather_subset_fact_key in facts_dict

# Generated at 2022-06-13 00:18:07.201353
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    from ansible.module_utils.facts import collector_classes
    from ansible.module_utils.facts.namespace import BaseFactNamespace

    # Basic test: gather_subset=['all'], filter_spec=''
    filter_spec = filter_spec or []
    gather_subset = gather_subset or ['all']
    fact_collector = \
        get_ansible_collector(all_collector_classes=collector_classes,
                              minimal_gather_subset=frozenset(),
                              gather_subset=gather_subset,
                              filter_spec=filter_spec)

    assert isinstance(fact_collector, AnsibleFactCollector)
    assert fact_collector.collectors
    assert len(fact_collector.collectors) == len(collector_classes)


# Generated at 2022-06-13 00:18:16.720246
# Unit test for function get_ansible_collector
def test_get_ansible_collector():

    class FakeCollector(collector.BaseFactCollector):
        name = 'fake'

        def collect(self, module=None, collected_facts=None):
            return {'fake': 'foo'}

    fake_fact_collector = FakeCollector()
    fake_collector_classes = [FakeCollector]
    fact_collector = get_ansible_collector(fake_collector_classes,
                                           namespace=None,
                                           filter_spec=None,
                                           gather_subset=['fake'],
                                           gather_timeout=None,
                                           minimal_gather_subset=frozenset())
    facts = fact_collector.collect()
    fake_facts = fake_fact_collector.collect()
    assert facts == fake_facts

test_get_ansible_

# Generated at 2022-06-13 00:18:23.391296
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts.collectors.filesystem.posix import FileSystemFactCollector
    from ansible.module_utils.facts.collectors.network.linux import LinuxNetworkFactCollector

    namespace = PrefixFactNamespace(prefix='test_filter_')

    file_system_collector = FileSystemFactCollector()
    network_collector = LinuxNetworkFactCollector()

    ansible_fact_collector = \
        AnsibleFactCollector(collectors=[file_system_collector,
                                         network_collector],
                             namespace=namespace)

    facts = ansible_fact_collector.collect()

    assert 'test_filter_system' in facts

# Generated at 2022-06-13 00:18:34.066339
# Unit test for method collect of class AnsibleFactCollector

# Generated at 2022-06-13 00:18:41.227684
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    import ansible.module_utils.facts.disk.smart as smart
    import ansible.module_utils.facts.system.sysctl as sysctl
    import ansible.module_utils.facts.system.distribution as distribution
    import ansible.module_utils.facts.system.path as path
    import ansible.module_utils.facts.zabbix as zabbix

    all_collector_classes = [smart.SmartFactCollector,
                             sysctl.SysctlFactCollector,
                             distribution.DistributionFactCollector,
                             path.PathFactCollector,
                             zabbix.ZabbixFactCollector]

    filter_spec = ['zabbix']
    gather_subset = ['all']
    gather_timeout = 5
    namespace = 'ansible'


# Generated at 2022-06-13 00:18:50.752420
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():

    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.namespace import PrefixFactNamespace

    class FakeCollectorA(BaseFactCollector):
        '''Fake collector class'''
        def collect(self, module=None, collected_facts=None):
            return {'a': 'A'}

    class FakeCollectorB(BaseFactCollector):
        '''Fake collector class'''
        def collect(self, module=None, collected_facts=None):
            return {'b': 'B'}

    class FakeCollectorC(BaseFactCollector):
        '''Fake collector class'''
        def collect(self, module=None, collected_facts=None):
            return {'c': 'C'}


# Generated at 2022-06-13 00:19:01.097920
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    from ansible.module_utils.facts.collector.nxos import LegacyNxosFacts

    fact_collector = AnsibleFactCollector(namespace=None)
    info_dict = {'version': '7.0(3)I3(1)',
                 'serialnumber': 'FOC1748Y12B',
                 'model': 'N9K-C93180YC-EX',
                 'vendor': 'Cisco'}

    nxos_collector_with_namespace = LegacyNxosFacts()
    nxos_collector_without_namespace = LegacyNxosFacts(namespace=None)

    fact_collector.collectors.append(nxos_collector_with_namespace)

# Generated at 2022-06-13 00:19:05.056031
# Unit test for function get_ansible_collector
def test_get_ansible_collector():

    def Collector_klass_factory(namespace=None, name=None):
        is_loaded = True
        class Collector_klass(object):
            def __init__(self, namespace=None):
                self.namespace = namespace
                self.name = name
            def collect(self):
                pass
            def get_fact_ids(self):
                return set([name])
        Collector_klass.__name__ = name
        Collector_klass.is_loaded = is_loaded
        return Collector_klass

    # Collect minimal subset, no namespace
    fact_collector = get_ansible_collector(
        all_collector_classes={'one': Collector_klass_factory(name='one')},
        minimal_gather_subset=['one'],
        filter_spec=[])
    assert fact

# Generated at 2022-06-13 00:19:05.610757
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    assert False