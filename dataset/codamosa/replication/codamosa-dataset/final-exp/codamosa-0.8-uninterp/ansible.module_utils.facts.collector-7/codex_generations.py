

# Generated at 2022-06-13 00:24:42.968665
# Unit test for function get_collector_names
def test_get_collector_names():
    assert get_collector_names(gather_subset=None) == frozenset(['all'])
    assert get_collector_names(gather_subset=['all']) == frozenset(['all'])
    assert get_collector_names(gather_subset=['!all']) == frozenset(['min'])
    assert get_collector_names(gather_subset=['!min']) == frozenset(['all'])
    assert get_collector_names(gather_subset=['!all', '!min']) == frozenset()
    assert get_collector_names(gather_subset=['!all', 'min']) == frozenset(['min'])

# Generated at 2022-06-13 00:24:55.029360
# Unit test for function get_collector_names
def test_get_collector_names():
    valid_subsets = frozenset(['all', 'min', 'network', 'hardware', 'devices', 'dmi'])

    minimal_gather_subset = frozenset(['min'])

    aliases_map = defaultdict(set)
    aliases_map['hardware'].update(['devices', 'dmi'])

    # Exclude from the minimal set
    # negative 'min' includes everything, then excludes
    # everything.
    assert get_collector_names(
        valid_subsets=valid_subsets,
        minimal_gather_subset=minimal_gather_subset,
        gather_subset=['!min']) == set()


# Generated at 2022-06-13 00:25:01.245548
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    from ansible.module_utils.facts.collector.package_manager.dnf import DNFFactCollector
    from ansible.module_utils.facts.collector.network.base import NetworkCollector
    from ansible.module_utils.facts.collector.network.linux import LinuxNetworkCollector

    all_fact_subsets = {
        'network': [NetworkCollector, LinuxNetworkCollector],
        'dnf': [DNFFactCollector],
    }

    assert find_unresolved_requires(['network'], all_fact_subsets) == set()
    assert find_unresolved_requires(['network', 'dnf'], all_fact_subsets) == set()
    assert find_unresolved_requires(['dnf'], all_fact_subsets) == {'network'}



# Generated at 2022-06-13 00:25:09.644938
# Unit test for function find_collectors_for_platform
def test_find_collectors_for_platform():
    import copy
    import sys
    import collections

    import unittest
    import ansible.module_utils.facts.collectors.default as default
    import ansible.module_utils.facts.collectors.network as network
    import ansible.module_utils.facts.collectors.processor as processor
    import ansible.module_utils.facts.collectors.hardware as hardware

    class TestFindCollectorsForPlatform(unittest.TestCase):

        def test_find_facter_collector_classes(self):
            test_platform = platform.system()

# Generated at 2022-06-13 00:25:19.969357
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    import unittest
    import copy
    class TestCollector1(BaseFactCollector):
        _fact_ids = set(['os', 'os_family', 'network'])
        name = 'test_one'
    class TestCollector2(BaseFactCollector):
        _fact_ids = set(['os_family', 'network'])
        name = 'test_two'
    class TestCollector3(BaseFactCollector):
        _fact_ids = set(['os', 'network'])
        name = 'test_three'

    class TestFactIdToCollectorMap(unittest.TestCase):
        def test_get_all_fact_ids(self):
            collectors_for_platform = set([TestCollector1, TestCollector2, TestCollector3])

# Generated at 2022-06-13 00:25:28.934562
# Unit test for function build_dep_data
def test_build_dep_data():
    # Get the set of facts that have dependencies
    fact_collector_path = [ 'ansible.module_utils.facts.collector', 'ansible.module_utils.facts.collectors' ]

    all_collector_classes = set()
    for path in fact_collector_path:
        all_collector_classes.update(collector_class for collector_class in
                                                    CollectorRegistry(path).collector_classes())
    print(all_collector_classes)
    for all_collector_class in all_collector_classes:
        print(all_collector_class.name)
    print(all_collector_classes)

    # Create the list of collectors for this platform
    platform_info = {'system': 'Linux'}

# Generated at 2022-06-13 00:25:34.510697
# Unit test for function select_collector_classes
def test_select_collector_classes():
    class FakeClass:
        name = 'fake1'

    class FakeClass2:
        name = 'fake2'

    class FakeClass3:
        name = 'fake3'

    class FakeClass4:
        name = 'fake4'

    all_fact_subsets = {
        'fake1': [FakeClass, FakeClass2, FakeClass3],
        'fake2': [FakeClass2],
        'fake3': [FakeClass3],
        'fake4': [FakeClass, FakeClass4]}

    selected_collectors = select_collector_classes(
        ['fake1'],
        all_fact_subsets
    )

    assert len(selected_collectors) == 3

# Generated at 2022-06-13 00:25:42.812321
# Unit test for function build_dep_data
def test_build_dep_data():
    class C1(BaseFactCollector):
        name = 'one'
        required_facts = set(['foo'])
    class C2(BaseFactCollector):
        name = 'two'
        required_facts = set(['foo'])


    assert build_dep_data(collector_names=set(['one', 'two']),
                          all_fact_subsets=defaultdict(set,
                                                       one=set([C1]),
                                                       two=set([C2]))) == {'one': set(['foo']),
                                                                           'two': set(['foo'])}



# Generated at 2022-06-13 00:25:49.606052
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    all_fact_subsets = {
        'a': [object()],
        'b': [object()],
        'c': [object()],
        'd': [object()],
        'e': [object()],
    }

    # no requires
    collector_names = ['a', 'b', 'c']
    unresolved = find_unresolved_requires(collector_names, all_fact_subsets)
    assert not unresolved

    # 'b' requires 'a'
    collector_names = ['b', 'c']
    unresolved = find_unresolved_requires(collector_names, all_fact_subsets)
    assert not unresolved

    # 'b' requires 'a', 'c' requires 'd'
    collector_names = ['b', 'c']

# Generated at 2022-06-13 00:26:00.381481
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    '''test case for find_unresolved_requires'''

    class CollectorA(BaseFactCollector):
        name = 'collectorA'
        requires_facts = ['collectorB']

    class CollectorB(BaseFactCollector):
        name = 'collectorB'
        requires_facts = ['collectorC']

    class CollectorC(BaseFactCollector):
        name = 'collectorC'
        requires_facts = []

    class CollectorD(BaseFactCollector):
        name = 'collectorD'
        requires_facts = ['collectorC']

    all_fact_subsets = {
        'collectorA': [CollectorA],
        'collectorB': [CollectorB],
        'collectorC': [CollectorC],
        'collectorD': [CollectorD],
    }

    unresolved

# Generated at 2022-06-13 00:26:11.626451
# Unit test for function select_collector_classes
def test_select_collector_classes():
    a_class = type('a_class', (object, ), {})
    b_class = type('b_class', (object, ), {})
    c_class = type('c_class', (object, ), {})
    d_class = type('d_class', (object, ), {})
    e_class = type('e_class', (object, ), {})

    a_class.name = 'a'
    b_class.name = 'b'
    c_class.name = 'c'
    d_class.name = 'd'
    e_class.name = 'e'

    all_fact_subsets = {'a': [a_class, b_class],
                        'b': [b_class],
                        'c': [c_class],
                        'd': [d_class]}


# Generated at 2022-06-13 00:26:17.301385
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    all_fact_subsets = {'foo': [type('test_collector_foo', (BaseFactCollector,),
                                      {'name': 'foo', 'required_facts': ['bar']})]}
    collector_names = {'foo'}
    assert find_unresolved_requires(collector_names, all_fact_subsets) == {'bar'}



# Generated at 2022-06-13 00:26:26.124648
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():

    class FakeCollector1:
        required_facts = set()

    class FakeCollector2:
        required_facts = {'fake_fact_2'}

    class FakeCollector3:
        required_facts = {'fake_fact_3'}

    class FakeCollector4:
        required_facts = {'fake_fact_4'}

    all_fact_subsets = {'fact_2': [FakeCollector2],
                        'fact_3': [FakeCollector3],
                        'fact_4': [FakeCollector4],
                        }
    collector_names = ['fact_1']

    assert find_unresolved_requires(collector_names, all_fact_subsets) == set()

    collector_names = ['fact_1', 'fact_2']

# Generated at 2022-06-13 00:26:37.483401
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    # "collector_a" requires "collector_b"
    class CollectorA:
        required_facts = ['collector_b']

    class CollectorB:
        required_facts = []

    collector_names = ['collector_a', 'collector_b']

    all_fact_subsets = {
        'collector_a': [CollectorA],
        'collector_b': [CollectorB],
    }

    # no unresolved names
    assert find_unresolved_requires(collector_names, all_fact_subsets) == set()

    # remove "collector_b" from collector_names
    collector_names = ['collector_a']

    # expect "collector_b" to be unresolved
    assert find_unresolved_requires(collector_names, all_fact_subsets) == set

# Generated at 2022-06-13 00:26:44.181050
# Unit test for function build_dep_data
def test_build_dep_data():
    from . import collector
    collectors = collector.get_collectors()
    collector_names = ['all', 'allcommands', 'hardware', 'network']
    my_dep_data = build_dep_data(collector_names, collectors)
    expected_dep_data = {'all': {'all', 'allcommands', 'hardware', 'network'},
                         'allcommands': {'all'},
                         'hardware': {'all'},
                         'network': {'all'}}
    assert my_dep_data == expected_dep_data


# Generated at 2022-06-13 00:26:53.518815
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    # test the function against a contrived example collector
    class TestCollector(BaseFactCollector):
        pass
    # no requires
    TestCollector.required_facts = set()
    assert find_unresolved_requires(['TestCollector'], {'TestCollector': [TestCollector]}) == set()
    # found required facts
    TestCollector.required_facts = set(['Foo'])
    assert find_unresolved_requires(['TestCollector', 'Foo'], {
        'TestCollector': [TestCollector], 'Foo': [TestCollector]
    }) == set()
    # missing required facts
    assert find_unresolved_requires(['TestCollector'], {'TestCollector': [TestCollector]}) == set(['Foo'])



# Generated at 2022-06-13 00:27:02.577394
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    from ansible_collections.ansible.netcommon.plugins.module_utils.facts.collector import (NetworkCollector)

    class FakeCollector(BaseFactCollector):
        name = 'fake'
        _fact_ids = frozenset(['a', 'b', 'c'])

    fact_id_to_collector_map, aliases_map = build_fact_id_to_collector_map(
        [FakeCollector, NetworkCollector])

    assert len(fact_id_to_collector_map.keys()) == 9
    assert 'a' in fact_id_to_collector_map
    assert 'b' in fact_id_to_collector_map
    assert 'c' in fact_id_to_collector_map
    assert 'fake' in fact_id_to_collector_map

# Generated at 2022-06-13 00:27:12.971054
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    class DummyCollector1(BaseFactCollector):
        '''Collector 1'''
        _fact_ids = ('collector1_alias', )
        name = 'collector1_name'

    class DummyCollector2(BaseFactCollector):
        '''Collector 2'''
        _fact_ids = ('collector2_alias1', 'collector2_alias2')
        name = 'collector2_name'

    class DummyCollector3(BaseFactCollector):
        '''Collector 3'''
        _fact_ids = ()
        name = 'collector3_name'

    class DummyCollector4(BaseFactCollector):
        '''Collector 4'''
        _fact_ids = ()
        name = 'collector4_name'


# Generated at 2022-06-13 00:27:24.179790
# Unit test for function select_collector_classes
def test_select_collector_classes():
    collector1 = type('Collector1', (BaseFactCollector, object), {'name': 'collector1', '_fact_ids': ('collector1',)})
    collector2 = type('Collector2', (BaseFactCollector, object), {'name': 'collector2', '_fact_ids': ('collector2',)})
    collector3 = type('Collector3', (BaseFactCollector, object), {'name': 'collector3', '_fact_ids': ('collector3',)})
    collector4 = type('Collector4', (BaseFactCollector, object), {'name': 'collector4', '_fact_ids': ('collector4',)})

# Generated at 2022-06-13 00:27:32.642975
# Unit test for function build_dep_data
def test_build_dep_data():
    from ansibesible_facts.collector.network import NetworkCollector
    from ansibesible_facts.collector.smbios import SmbiosCollector
    from ansibesible_facts.collector.all import AllCollector

    network_collector = NetworkCollector()
    assert network_collector.required_facts == {'all', 'dmi', 'network'}

    smbios_collector = SmbiosCollector()
    assert smbios_collector.required_facts == {'all'}

    all_collector = AllCollector()
    assert all_collector.required_facts == set()

    collector_names = {'network', 'smbios', 'all'}

# Generated at 2022-06-13 00:27:50.468218
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    class FooClass(BaseFactCollector):
        _fact_ids = {'a', 'b', 'c'}

        def collect(self, module=None, collected_facts=None):
            return {'a': 1, 'b': 2, 'c': 3}
    class Foo2Class(BaseFactCollector):
        _fact_ids = {'a', 'b', 'c'}

        def collect(self, module=None, collected_facts=None):
            return {'a': 4, 'b': 5, 'c': 6}

    all_collector_classes = [FooClass, Foo2Class]

    fact_id_to_collector_map, aliases_map = build_fact_id_to_collector_map(all_collector_classes)


# Generated at 2022-06-13 00:27:58.138706
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    class TestCollector0(BaseFactCollector):
        _fact_ids = {"not-id", "also-not-id"}
        name = "test_collector_0"

    class TestCollector1(BaseFactCollector):
        _fact_ids = {"also-not-id"}
        name = "test_collector_1"

    class TestCollector2(BaseFactCollector):
        _fact_ids = set()
        name = "test_collector_2"

    test_collectors = {TestCollector0, TestCollector1, TestCollector2}
    fact_id_to_collector_map, aliases_map = build_fact_id_to_collector_map(test_collectors)


# Generated at 2022-06-13 00:28:05.115748
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    class DummyCollector(BaseFactCollector):
        _fact_ids = frozenset(['id1', 'id2', 'id3'])
    collectors_for_platform = [DummyCollector]
    (fact_id_to_collector_map, aliases_map) = build_fact_id_to_collector_map(collectors_for_platform)
    assert fact_id_to_collector_map == {
        'id1': [DummyCollector],
        'id2': [DummyCollector],
        'id3': [DummyCollector],
    }

# Generated at 2022-06-13 00:28:16.131484
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    Collectors_A = type('Collectors_A', (object,), dict(name='A', required_facts=frozenset(('X',))))
    Collectors_B = type('Collectors_B', (object,), dict(name='B', required_facts=frozenset(('Y', 'Z'))))
    Collectors_C = type('Collectors_C', (object,), dict(name='C', required_facts=frozenset(('Y',))))
    Collectors_D = type('Collectors_D', (object,), dict(name='D', required_facts=frozenset(('Y',))))
    Collectors_E = type('Collectors_E', (object,), dict(name='E', required_facts=frozenset(('Y', 'Z'))))

# Generated at 2022-06-13 00:28:25.954519
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    from ansible.module_utils.facts.system.distribution import DistributionFactCollector
    from ansible.module_utils.facts.system.pkg_mgr import PkgMgrFactCollector
    from ansible.module_utils.facts.system.seboolean import SEbooleanFactCollector

    all_collector_classes = [DistributionFactCollector,
                             SEbooleanFactCollector,
                             PkgMgrFactCollector]

    compatible_platforms = [{'system': 'Linux'}]
    collectors_for_platform = find_collectors_for_platform(all_collector_classes,
                                                           compatible_platforms)

    fact_id_to_collector_map, aliases_map = build_fact_id_to_collector_map(collectors_for_platform)

    # For

# Generated at 2022-06-13 00:28:37.999382
# Unit test for function get_collector_names
def test_get_collector_names():
    try:
        # Missing minimal_gather_subset
        get_collector_names(valid_subsets=())
    except TypeError:
        pass
    else:
        raise Exception('should have thrown error with no minimal_gather_subset')

    # minimal_gather_subset is always added
    assert get_collector_names(
        minimal_gather_subset=('minimal_fact',),
        valid_subsets=('fact1', 'fact2', 'fact3'),
        gather_subset=(),
    ) == {'minimal_fact'}

    # gather_subset='all' expand to all valid_subsets

# Generated at 2022-06-13 00:28:42.501634
# Unit test for function collector_classes_from_gather_subset
def test_collector_classes_from_gather_subset():
    mock_all_fact_subsets = {'a': 'A', 'b1': 'B1', 'b2': 'B2', 'c1': 'C1', 'c2': 'C2', 'c3': 'C3', 'd': 'D'}
    # Without aliases and subset/alias conflicts
    # 1. all
    selected_col_classes = collector_classes_from_gather_subset(gather_subset=['all'],
                                                                all_collector_classes=mock_all_fact_subsets.values())
    assert selected_col_classes == ['A', 'B1', 'B2', 'C1', 'C2', 'C3', 'D']

    # 2. all - b1, b2
    selected_col_classes = collector_classes_from_gather_sub

# Generated at 2022-06-13 00:28:54.162074
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    # 'all' collector that does nothing
    class DummyAllCollector(BaseFactCollector):
        _fact_ids = {'all', 'minimal'}

        def collect(self, module=None, collected_facts=None):
            return {}

    # 'all' collector that does something
    class RealAllCollector(BaseFactCollector):
        _fact_ids = {'all', 'minimal'}

        def collect(self, module=None, collected_facts=None):
            return {'real_all': 1}

    # 'os' collector that does something
    class OSCollector(BaseFactCollector):
        _fact_ids = {'os', 'minimal'}

        def collect(self, module=None, collected_facts=None):
            return {'os': 1}

    all_collector_classes

# Generated at 2022-06-13 00:29:00.325436
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    class CollectorA(BaseFactCollector):
        name = 'A'
        _fact_ids = set(['A', 'AA'])

    class CollectorB(BaseFactCollector):
        name = 'B'
        _fact_ids = set(['B', 'BB'])
        required_facts = set(['A'])

    collectors = [CollectorA, CollectorB]

    fact_id_to_collector_map, aliases_map = build_fact_id_to_collector_map(collectors)

    assert collectors == fact_id_to_collector_map['A']
    assert collectors == fact_id_to_collector_map['AA']
    assert collectors == fact_id_to_collector_map['B']
    assert collectors == fact_id_to_collector_map['BB']


# Generated at 2022-06-13 00:29:04.941276
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    collector_name = {'a':'!*', 'b':'!*'}
    all_fact_subsets = {'c':'!*', 'b':'!*', 'a':'!*'}
    r = find_unresolved_requires(collector_name, all_fact_subsets)
    assert r['b'] == '!*'



# Generated at 2022-06-13 00:29:19.779103
# Unit test for function build_dep_data

# Generated at 2022-06-13 00:29:26.545403
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    class Collector(BaseFactCollector):
        name = 'collector'
        _fact_ids = {'collector', 'alias'}

        @classmethod
        def platform_match(cls, platform_info):
            return cls

    results = build_fact_id_to_collector_map([Collector])

    assert results == ({
        'collector': [Collector],
        'alias': [Collector],
    }, {
        'collector': {'collector', 'alias'},
    })



# Generated at 2022-06-13 00:29:38.231832
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    from ansible.module_utils.facts.collector.base import BaseFactCollector

    class Fact1(BaseFactCollector):
        _fact_ids = frozenset(['fact1', 'alias1'])
        name = 'primary1'

    class Fact2(BaseFactCollector):
        _fact_ids = frozenset(['fact2'])
        name = 'primary2'

    class Fact3(BaseFactCollector):
        _fact_ids = frozenset(['fact3', 'alias1'])
        name = 'primary3'

    CollectorClasses = [Fact1, Fact2, Fact3]


# Generated at 2022-06-13 00:29:45.927940
# Unit test for function get_collector_names
def test_get_collector_names():
    valid_subsets = frozenset(('network', 'virtual', 'facter'))

    assert get_collector_names(valid_subsets=valid_subsets, gather_subset=['all']) == frozenset(('network', 'virtual', 'facter'))
    assert get_collector_names(valid_subsets=valid_subsets, gather_subset=['min']) == frozenset()
    assert get_collector_names(valid_subsets=valid_subsets, gather_subset=['network', 'virtual']) == frozenset(('network', 'virtual'))
    assert get_collector_names(valid_subsets=valid_subsets, gather_subset=['network', 'virtual', 'min']) == frozenset(('network', 'virtual'))

    # NOTE: network takes precedence

# Generated at 2022-06-13 00:29:57.210617
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    class FooCollector(BaseFactCollector):
        name = 'foo'
    class BarCollector(BaseFactCollector):
        name = 'bar'
        required_facts = ['foo']
    class BazCollector(BaseFactCollector):
        name = 'baz'
        required_facts = ['bar']
    class QuxCollector(BaseFactCollector):
        name = 'qux'

    collectors = [FooCollector, BarCollector, BazCollector, QuxCollector]
    collector_names = [C.name for C in collectors]
    all_fact_subsets = defaultdict(list)
    for collector in collectors:
        all_fact_subsets[collector.name].append(collector)

    assert find_unresolved_requires(collector_names, all_fact_subsets) == set

# Generated at 2022-06-13 00:30:01.621597
# Unit test for function select_collector_classes
def test_select_collector_classes():
    import unittest
    import ansible.module_utils.facts

    class A1(ansible.module_utils.facts.BaseFactCollector):
        name = 'a1'
    class A1_1(ansible.module_utils.facts.BaseFactCollector):
        name = 'a1'
    class A1_2(ansible.module_utils.facts.BaseFactCollector):
        name = 'a1'
    class A2(ansible.module_utils.facts.BaseFactCollector):
        name = 'a2'
    class B1(ansible.module_utils.facts.BaseFactCollector):
        name = 'b1'
    class C1(ansible.module_utils.facts.BaseFactCollector):
        name = 'c1'


# Generated at 2022-06-13 00:30:14.420758
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    from ansible.module_utils.facts import collector
    from ansible.module_utils.facts.collector import namespaced_name
    import ansible_collections.ansible.community

    fake_subset_names = {
        'myns': 'myns',
        'myns:primary': 'myns',
        'myns:secondary': 'myns',
        'myns:invalid': 'myns:invalid'
    }

    class FakeSubsetClass:
        @property
        def name(self):
            return self.__class__.__name__

        @classmethod
        def platform_match(cls, platform_info):
            return True

        def collect(self, module=None, collected_facts=None):
            return {}


# Generated at 2022-06-13 00:30:18.550155
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    class FakeCollector:
        _fact_ids = {'a_fact'}
        required_facts = {'other_fact'}

    all_fact_subsets = {'my_fact': [FakeCollector]}

    collector_names = ['my_fact']
    assert find_unresolved_requires(collector_names, all_fact_subsets) == {'other_fact'}
    collector_names = ['other_fact', 'my_fact']
    assert find_unresolved_requires(collector_names, all_fact_subsets) == set()
    collector_names = ['bad_fact']
    assert find_unresolved_requires(collector_names, all_fact_subsets) == {'bad_fact'}



# Generated at 2022-06-13 00:30:22.029707
# Unit test for function collector_classes_from_gather_subset
def test_collector_classes_from_gather_subset():
    import os
    import sys
    import tempfile
    import subprocess


# Generated at 2022-06-13 00:30:26.873160
# Unit test for function collector_classes_from_gather_subset
def test_collector_classes_from_gather_subset():
    import doctest
    import ansible_test
    results = doctest.testmod(ansible_test)
    if results.failed == 0:
        print("Success: %d test(s)" % results.attempted)
    sys.exit(results.failed)



# Generated at 2022-06-13 00:30:42.830239
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    class X(BaseFactCollector):
        name = 'X'
        _fact_ids = ('x1', )

    class Y(BaseFactCollector):
        name = 'Y'
        _fact_ids = ('y1', 'y2')

    fact_id_to_collector_map, aliases_map = build_fact_id_to_collector_map(
        [X, Y]
    )

    assert set(fact_id_to_collector_map['X']) == set([X])
    assert set(fact_id_to_collector_map['Y']) == set([Y])
    assert set(fact_id_to_collector_map['x1']) == set([X])
    assert set(fact_id_to_collector_map['y1']) == set([Y])


# Generated at 2022-06-13 00:30:48.097756
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    from ansible.module_utils.facts.netdev import BaseNetwork
    a_fact = BaseNetwork()
    b_fact = BaseNetwork()
    b_fact.required_facts = set([a_fact.name])
    c_fact = BaseNetwork()
    c_fact.required_facts = set([b_fact.name])

    all_collectors = {
        a_fact.name: [a_fact],
        b_fact.name: [b_fact],
        c_fact.name: [c_fact],
    }

    # [a, c] is not a valid ordering.
    assert 'b' in find_unresolved_requires(['a', 'c'], all_collectors)



# Generated at 2022-06-13 00:30:57.386034
# Unit test for function get_collector_names
def test_get_collector_names():
    tests = []

    # Test getting all names
    tests.append(dict(
        gather_subset=None,
        valid_subsets=frozenset(['fact1', 'fact2', 'fact3']),
        expected=frozenset(['fact1', 'fact2', 'fact3'])
    ))

    # Test with basic subset match
    tests.append(dict(
        gather_subset=['fact2'],
        valid_subsets=frozenset(['fact1', 'fact2', 'fact3']),
        expected=frozenset(['fact2'])
    ))

    # Test with exclusion

# Generated at 2022-06-13 00:31:08.767598
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    # mock Collector
    class MockCollector:
        def __init__(self, name, _fact_ids):
            self.name = name
            self._fact_ids = _fact_ids

    # Known class(es)
    collectors_for_platform = [
        MockCollector(name="network", _fact_ids=["network", "net0", "net1"]),
        MockCollector(name="dmi", _fact_ids=["dmi", "bios_version", "system_uuid"]),
    ]

    # Build the map
    fact_id_to_collector_map, aliases_map = build_fact_id_to_collector_map(collectors_for_platform)

    # Verify the map

# Generated at 2022-06-13 00:31:13.841485
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    class Collector1(BaseFactCollector):
        name = 'test_collector_1'
        _fact_ids = {
            'test_fact_1',
            'test_fact_2',
            'test_fact_3'
        }

    class Collector2(BaseFactCollector):
        name = 'test_collector_2'
        _fact_ids = {
            'test_fact_3',
            'test_fact_4'
        }
    
    class Collector3(BaseFactCollector):
        name = 'test_collector_3'
        _fact_ids = {
            'test_fact_5'
        }

    collectors_for_platform = [
        Collector1,
        Collector2,
        Collector3
    ]

    fact_id_to_collector_map, aliases_map

# Generated at 2022-06-13 00:31:23.929147
# Unit test for function get_collector_names
def test_get_collector_names():
    # 1) gather_subset=None, aliases_map=None
    assert get_collector_names(gather_subset=None) == ['all']
    # 2) gather_subset=None, aliases_map=defaultdict(set)
    assert get_collector_names(gather_subset=None, aliases_map=defaultdict(set)) == ['all']
    # 3) gather_subset=[], aliases_map=None
    assert get_collector_names(gather_subset=[], aliases_map=None) == ['all']
    # 4) gather_subset=[], aliases_map=defaultdict(set)
    assert get_collector_names(gather_subset=[], aliases_map=defaultdict(set)) == ['all']
    # 5) gather_subset=['min'], aliases_

# Generated at 2022-06-13 00:31:31.011505
# Unit test for function select_collector_classes
def test_select_collector_classes():

    collectors = [CollectorFoo, CollectorBar, CollectorBaz, CollectorFooBar]
    collector_names = [CollectorFoo.name, CollectorBar.name, CollectorBaz.name]
    seen_collector_classes = set()

    selected_collector_classes = []

    for collector_name in collector_names:
        collector_classes = collectors
        for collector_class in collector_classes:
            if collector_class not in seen_collector_classes:
                selected_collector_classes.append(collector_class)
                seen_collector_classes.add(collector_class)

    return selected_collector_classes


# Generated at 2022-06-13 00:31:43.578561
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    class TestCollector(BaseFactCollector):
        _fact_ids = ['ABC']
        name = 'test_collector'

    expected_fact_id_to_collector_map = defaultdict(list)
    expected_fact_id_to_collector_map['test_collector'] = [TestCollector]
    expected_fact_id_to_collector_map['ABC'] = [TestCollector]

    expected_aliases_map = defaultdict(set)
    expected_aliases_map['test_collector'] = set(['ABC'])

    result_fact_id_to_collector_map, result_aliases_map = build_fact_id_to_collector_map([TestCollector])

    assert result_fact_id_to_collector_map == expected_fact_id_to_collect

# Generated at 2022-06-13 00:31:55.024901
# Unit test for function build_dep_data

# Generated at 2022-06-13 00:32:05.824796
# Unit test for function build_dep_data
def test_build_dep_data():
    from . import collectors
    import sys
    platform_info = {'system': 'FreeBSD', 'release': '12.0-RELEASE'}
    collectors = find_collectors_for_platform(collectors.__collector_classes__(), [platform_info])
    collector_name_to_class = build_fact_id_to_collector_map(collectors)
    collector_names = set(collector_name_to_class)
    deps = build_dep_data(collector_names, collector_name_to_class)
    assert deps['virtual_subtype'] == {'virtual'}
    assert deps['virtual'] == set()
    assert deps['kernel'] == set()
    assert deps['selinux'] == set()
    assert deps['ssh_host_key'] == set()
   

# Generated at 2022-06-13 00:32:32.540710
# Unit test for function build_dep_data
def test_build_dep_data():
    collector_names = ['foo', 'bar', 'baz', 'qux']
    all_fact_subsets = defaultdict(list)
    all_fact_subsets['foo'].append(BaseFactCollector(['foo'], ['bar', 'baz', 'qux']))
    all_fact_subsets['bar'].append(BaseFactCollector(['bar'], ['qux', 'baz']))
    all_fact_subsets['baz'].append(BaseFactCollector(['baz'], ['qux']))
    all_fact_subsets['qux'].append(BaseFactCollector(['qux']))
    
    expected_dep_map = defaultdict(set)
    expected_dep_map['foo'] = {'bar', 'baz', 'qux'}
    expected_dep

# Generated at 2022-06-13 00:32:40.964477
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    # Test good case
    assert not find_unresolved_requires(['a'], {'a': [1], 'b': [2]})

    # Test different order
    assert not find_unresolved_requires(['b', 'a'], {'a': [1], 'b': [2]})

    # Test with unresolved
    assert find_unresolved_requires(['a'], {'a': [1], 'b': [2]}) == set(['b'])

    # Test with unresolved that has an alias
    assert find_unresolved_requires(['a'], {'a': [1], 'b': [2], 'c': [3]}) == set(['b', 'c'])



# Generated at 2022-06-13 00:32:49.882327
# Unit test for function tsort
def test_tsort():
    # Test a simple sort
    dep_map = dict(
        a=set('c'),
        b=set('c'),
        c=set('d'),
        d=set('e'),
        e=set(),
        g=set(),
    )

    sorted_list = tsort(dep_map)
    in_order = ['e', 'd', 'c', 'a', 'b', 'g']
    for i in range(len(sorted_list)):
        assert sorted_list[i][0] == in_order[i]

    # Test a more complex graph

# Generated at 2022-06-13 00:33:00.948463
# Unit test for function find_collectors_for_platform
def test_find_collectors_for_platform():
    class Collect1(BaseFactCollector):
        _platform = 'Linux'
        name = 'collect1'
    assert find_collectors_for_platform([Collect1], [{'system': 'Linux'}]) == {Collect1}

    class Collect2(BaseFactCollector):
        _platform = 'Generic'
        name = 'collect2'
    assert find_collectors_for_platform([Collect2, Collect1], [{'system': 'Linux'}]) == {Collect1, Collect2}

    assert find_collectors_for_platform([Collect2, Collect1], [{'system': 'haiku'}]) == {Collect2}

    class Collect3(BaseFactCollector):
        _platform = 'haiku'
        name = 'collect3'

# Generated at 2022-06-13 00:33:11.667958
# Unit test for function tsort
def test_tsort():
    test_list = [
        ('a', ['b']),
        ('b', ['c']),
        ('c', []),
        ('d', ['e']),
        ('e', ['f', 'g']),
        ('f', ['g']),
        ('g', []),
    ]

    test_map = {k: set(v) for k, v in test_list}

    assert tsort(test_map) == test_list

    bad_map = {
        1: set([2]),
        2: set([3]),
        3: set([1]),
    }
    try:
        tsort(bad_map)
    except CycleFoundInFactDeps as exc:
        assert 'cycle' in str(exc)

# Generated at 2022-06-13 00:33:23.475243
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    from ansible.module_utils.facts import collector
    all_fact_subsets = collector.get_fact_subsets()

    assert find_unresolved_requires(('dmi', 'all', 'facter', 'min'), all_fact_subsets).symmetric_difference(
        set(['devices', 'lsb', 'virtual', 'python'])) == set()

    assert find_unresolved_requires(('dmi', 'all', 'facter', 'min', '!devices'), all_fact_subsets).symmetric_difference(
        set(['lsb', 'virtual', 'python'])) == set()


# Generated at 2022-06-13 00:33:24.249690
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    pass



# Generated at 2022-06-13 00:33:32.941301
# Unit test for function find_collectors_for_platform
def test_find_collectors_for_platform():
    def class_name(all_collector_class):
        return all_collector_class.__name__

    all_collector_classes = [CollectorFooA, CollectorFooB, CollectorBar]
    found_collectors = find_collectors_for_platform(all_collector_classes, ['Foo'])

    assert all(isinstance(collector, BaseFactCollector)
               for collector in found_collectors)

    assert all(collector.platform == 'Foo'
               for collector in found_collectors)

    assert set(map(class_name, found_collectors)) == {
        'CollectorFooA',
        'CollectorFooB',
    }

    found_collectors = find_collectors_for_platform(all_collector_classes, ['Bar'])

# Generated at 2022-06-13 00:33:43.334245
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    class TestCollector1(BaseFactCollector):
        name = 'test1'
        _fact_ids = {'test1_alias1', 'test1_alias2'}
    class TestCollector2(BaseFactCollector):
        name = 'test2'
        _fact_ids = {'test2_alias1', 'test2_alias2'}

    fact_id_to_collector_map, aliases_map = build_fact_id_to_collector_map([TestCollector1, TestCollector2])

    assert len(fact_id_to_collector_map) == 5

# Generated at 2022-06-13 00:33:53.530463
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    global test_all_fact_subsets
    import datetime
    test_all_fact_subsets = defaultdict(list)
    test_all_fact_subsets['f1'].append('f1')
    test_all_fact_subsets['f2'].append('f2')
    test_all_fact_subsets['f3'].append('f3')
    test_all_fact_subsets['f4'].append('f4')
    test_all_fact_subsets['f5'].append('f5')

    res = find_unresolved_requires(['f1','f2','f3','f4','f5'], test_all_fact_subsets)
    assert len(res) == 0
