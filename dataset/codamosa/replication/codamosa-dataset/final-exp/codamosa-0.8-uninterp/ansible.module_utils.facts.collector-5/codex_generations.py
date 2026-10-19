

# Generated at 2022-06-13 00:24:51.469858
# Unit test for function find_collectors_for_platform
def test_find_collectors_for_platform():
    class MyBaseCollector(BaseFactCollector):
        name = 'mybase'

    class MyLinuxCollector(MyBaseCollector):
        _platform = 'Linux'

    class MyFreebsdCollector(MyBaseCollector):
        _platform = 'FreeBSD'

    mocked_platform_info = {'system': 'Linux'}
    assert(find_collectors_for_platform([MyLinuxCollector, MyFreebsdCollector], [mocked_platform_info]) == set([MyLinuxCollector]))



# Generated at 2022-06-13 00:24:56.475188
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    import pytest
    class TestFactCollectorA(BaseFactCollector):
        _fact_ids = set(['a'])
        name = 'a'
        required_facts = set(['b'])

    class TestFactCollectorB(BaseFactCollector):
        _fact_ids = set(['b'])
        name = 'b'
        required_facts = set()

    class TestFactCollectorC(BaseFactCollector):
        _fact_ids = set(['c'])
        name = 'c'
        required_facts = set(['a', 'd'])

    class TestFactCollectorD(BaseFactCollector):
        _fact_ids = set(['d'])
        name = 'd'
        required_facts = set(['e'])


# Generated at 2022-06-13 00:25:07.454343
# Unit test for function get_collector_names
def test_get_collector_names():
    # Test 1
    gather_subset = ['all']
    minimal_gather_subset = frozenset(['facter'])
    valid_subsets = frozenset(['facter', 'ohai', 'redhat'])
    aliases_map = defaultdict(set)
    expected_subsets = frozenset(['facter', 'ohai', 'redhat'])
    assert get_collector_names(valid_subsets=valid_subsets,
                               minimal_gather_subset=minimal_gather_subset,
                               gather_subset=gather_subset,
                               aliases_map=aliases_map) == expected_subsets
    # Test 2
    gather_subset = ['!facter']

# Generated at 2022-06-13 00:25:18.935913
# Unit test for function tsort
def test_tsort():
    # Test data which is the graph described in section 3 of
    # https://en.wikipedia.org/wiki/Topological_sorting#Algorithms
    test_data = {
        "7": set(["11", "8"]),
        "5": set(["11", "2"]),
        "3": set(["8", "10"]),
        "11": set(["2", "9", "10"]),
        "8": set(["9"]),
        "2": set(["9"])
    }
    sorted_list = tsort(test_data)

# Generated at 2022-06-13 00:25:23.096913
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    class Collector(BaseFactCollector):
        _fact_ids = set(['a', 'b'])
        name = 'primary'

    fact_id_to_collector_map, aliases_map = build_fact_id_to_collector_map([Collector])

    assert set(fact_id_to_collector_map.keys()) == {'a', 'b', 'primary'}
    assert aliases_map['primary'] == {'a', 'b'}



# Generated at 2022-06-13 00:25:28.151673
# Unit test for function find_collectors_for_platform
def test_find_collectors_for_platform():
    found_collectors = find_collectors_for_platform([LinuxFactCollector], ['Linux'])
    assert(LinuxFactCollector in found_collectors)
    assert(LinuxVirtualFactCollector in found_collectors)

    found_collectors = find_collectors_for_platform([LinuxFactCollector], ['NotLinux'])
    assert(LinuxFactCollector not in found_collectors)
    assert(LinuxVirtualFactCollector not in found_collectors)



# Generated at 2022-06-13 00:25:39.629535
# Unit test for function tsort
def test_tsort():
    def compare(input_deps, expected_deps):
        actual_deps = tsort(input_deps)
        assert actual_deps == expected_deps, "Failed: input: %s" % input_deps
    input_deps = {'a': ('b', 'c'),
                  'b': ('d', 'e'),
                  'c': ('f', 'g'),
                  'd': ('g',),
                  'e': (),
                  'f': (),
                  'g': ()}

# Generated at 2022-06-13 00:25:47.765462
# Unit test for function get_collector_names
def test_get_collector_names():
    assert set() == get_collector_names(set(), set(), ['!all'])
    assert set() == get_collector_names(set(), set(), ['!min'])
    assert set() == get_collector_names(set(), set(), ['!all', '!min'])
    assert {'min'} == get_collector_names({'min'}, set(), ['!all'])
    assert {'min'} == get_collector_names({'min'}, set(), ['!min'])
    assert set() == get_collector_names({'min'}, set(), ['!all', '!min'])
    assert {'min'} == get_collector_names({'min'}, {'min'}, ['!all'])

# Generated at 2022-06-13 00:25:55.432930
# Unit test for function select_collector_classes
def test_select_collector_classes():
    collectors_for_platform = [
        (classnames_for_platform.get(platform.system(), []) or []),
        (classnames_for_platform.get('Generic', []))
    ]
    collectors_for_platform = list(itertools.chain(*collectors_for_platform))
    selected_collector_classes = select_collector_classes(collector_names, fact_id_to_collector_map)

    assert(set(selected_collector_classes) == set(collectors_for_platform))


# Generated at 2022-06-13 00:26:03.120459
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    from test_collector_classes import TestCollector1, TestCollector2, TestCollector3

    #  A <-- B <-- C
    all_fact_subsets = {
        'C': [TestCollector3],
        'B': [TestCollector2],
        'A': [TestCollector1],
    }

    assert find_unresolved_requires(['A', 'C'], all_fact_subsets) == {'B'}
    assert find_unresolved_requires(['B', 'C'], all_fact_subsets) == set()



# Generated at 2022-06-13 00:26:19.766076
# Unit test for function find_collectors_for_platform
def test_find_collectors_for_platform():

    class A(BaseFactCollector):
        name = "a"
        _platform = "ABS"

    class B(BaseFactCollector):
        name = "b"
        _platform = "BBS"

    all_collectors = [A, B]

    # no platform got
    assert(len(find_collectors_for_platform(all_collectors, [])) == 0)

    # platform_ABS got
    assert(len(find_collectors_for_platform(all_collectors, [{"system": "ABS"}])) == 1)

    # platform_BBS got
    assert(len(find_collectors_for_platform(all_collectors, [{"system": "BBS"}])) == 1)

    # platform_ABS and platform_BBS got

# Generated at 2022-06-13 00:26:31.712187
# Unit test for function find_collectors_for_platform
def test_find_collectors_for_platform():
    class Test1(BaseFactCollector):
        pass
    class Test2(BaseFactCollector):
        _platform = 'linux'
    class Test3(BaseFactCollector):
        _platform = 'linux'
    class Test4(BaseFactCollector):
        pass
    class Test5(BaseFactCollector):
        pass

    # create a set of all the class to be tested
    all_collector_classes = {Test1, Test2, Test3, Test4, Test5}

    # test that Test1, Test4, Test5 are returned for generic platform
    found_collectors = find_collectors_for_platform(all_collector_classes, [{'system': 'generic'}])
    assert {x.name for x in found_collectors} == {'Test1', 'Test4', 'Test5'}



# Generated at 2022-06-13 00:26:42.250019
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    class MockCollectorClass:
        def __init__(self, name, required_facts):
            self.name = name
            self.required_facts = set(required_facts)


# Generated at 2022-06-13 00:26:52.354359
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    class Foo(BaseFactCollector):
        name = 'foo'
        _fact_ids = ['foo']

    class Bar(BaseFactCollector):
        name = 'bar'
        _fact_ids = ['bar', 'baz']

    class Baz(BaseFactCollector):
        name = 'baz'
        _fact_ids = ['baz']

    collectors_for_platform = [Foo, Bar, Baz]

    # test function
    fact_id_to_collector_map, aliases_map = build_fact_id_to_collector_map(collectors_for_platform)

    class TestCollector(BaseFactCollector):
        # fact_ids to test
        _fact_ids = ['foo', 'bar', 'baz']

    # test cases

# Generated at 2022-06-13 00:27:02.221257
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    class FakeCollector:
        def __init__(self, name, requires):
            self.name = name
            self.required_facts = requires

    fake_collectors = [
        FakeCollector('all', set()),
        FakeCollector('A', set()),
        FakeCollector('B', set(['A'])),
        FakeCollector('C', set(['B'])),
        FakeCollector('D', set(['C', 'E'])),
    ]
    all_fact_subsets = {}
    for fake_collector in fake_collectors:
        all_fact_subsets.setdefault(fake_collector.name, []).append(fake_collector)

    # test empty subset
    collector_names = []

# Generated at 2022-06-13 00:27:12.685224
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    # Test empty input
    collector_names = []
    all_fact_subsets = {}
    unresolved = find_unresolved_requires(collector_names, all_fact_subsets)
    assert not unresolved

    # Test input that should return an empty set
    collector_names = ['groups', 'users']
    all_fact_subsets = {'groups': [object], 'users': [object]}
    unresolved = find_unresolved_requires(collector_names, all_fact_subsets)
    assert not unresolved

    # Test input that should raise an exception
    collector_names = ['users']
    all_fact_subsets = {'users': [object]}
    unresolved = find_unresolved_requires(collector_names, all_fact_subsets)
    assert unresolved
    assert 'groups' in unresolved

    #

# Generated at 2022-06-13 00:27:19.703794
# Unit test for function get_collector_names
def test_get_collector_names():

    gather_subset = ['!all', 'min', '!dmi', '!hardware']
    valid_subsets = ['all', 'dmi', 'hardware']
    aliases_map = {'hardware': ['devices', 'dmi']}
    names = get_collector_names(valid_subsets, aliases_map=aliases_map, gather_subset=gather_subset)
    assert set(names) == {'devices', 'min'}



# Generated at 2022-06-13 00:27:29.251348
# Unit test for function select_collector_classes
def test_select_collector_classes():
    import unittest

    class TestCollector(BaseFactCollector):
        _fact_ids = set(['a'])
        name = 'test'
        required_facts = set()

    class TestCollector2(BaseFactCollector):
        _fact_ids = set(['a', 'b'])
        name = 'test2'
        required_facts = set()

    class TestCollector3(BaseFactCollector):
        _fact_ids = set(['a', 'c'])
        name = 'test3'
        required_facts = set()

    class TestCollector4(BaseFactCollector):
        _fact_ids = set(['d'])
        name = 'test4'
        required_facts = set()


# Generated at 2022-06-13 00:27:41.682490
# Unit test for function select_collector_classes
def test_select_collector_classes():
    class TestCollector1(BaseFactCollector):
        name = 'test_name1'
        _fact_ids = set(['test_name1'])

        def collect(self):
            return {'test_name1': 'test_value1'}

    class TestCollector2(BaseFactCollector):
        name = 'test_name2'
        _fact_ids = set(['test_name2'])

        def collect(self):
            return {'test_name2': 'test_value2'}

    class TestCollector3(BaseFactCollector):
        name = 'test_name3'
        _fact_ids = set(['test_name3'])

        def collect(self):
            return {'test_name3': 'test_value3'}


# Generated at 2022-06-13 00:27:52.927789
# Unit test for function select_collector_classes
def test_select_collector_classes():
    # Given two collectors that provide the same fact id
    class CollectorA(BaseFactCollector):
        _fact_ids = ['test_fact']
        name = 'CollectorA'

    class CollectorB(BaseFactCollector):
        _fact_ids = ['test_fact']
        name = 'CollectorB'

    # And an all_fact_subsets map containing both
    all_fact_subsets = {
        'test_fact': set([CollectorA, CollectorB])
    }

    # When selecting the name for both
    selected_collector_names = select_collector_classes(['test_fact'], all_fact_subsets)

    # Then only CollectorA is returned
    assert len(selected_collector_names) == 1
    assert selected_collector_names[0] == CollectorA



# Generated at 2022-06-13 00:28:02.379935
# Unit test for function select_collector_classes
def test_select_collector_classes():
    collector_names = ['network', 'system']

    all_fact_subsets = {'network': [DisabledNetworkCollector, NetworkCollector],
                        'system': [DisabledSystemCollector, SystemCollector]}
    selected_collector_classes = select_collector_classes(collector_names, all_fact_subsets)
    assert len(selected_collector_classes) == 2
    assert NetworkCollector in selected_collector_classes
    assert SystemCollector in selected_collector_classes



# Generated at 2022-06-13 00:28:06.253802
# Unit test for function build_dep_data
def test_build_dep_data():
    collector_names = ['foo', 'bar']
    dep_map = build_dep_data(collector_names, all_fact_subsets)
    assert dep_map['foo'] == set('baz')
    assert dep_map['bar'] == set('baz')


# Generated at 2022-06-13 00:28:18.004587
# Unit test for function select_collector_classes
def test_select_collector_classes():
    class TestCollectorA(BaseFactCollector):
        name = 'a'
    class TestCollectorB(BaseFactCollector):
        name = 'b'
    class TestCollectorC(BaseFactCollector):
        name = 'c'
    class TestCollectorD(BaseFactCollector):
        name = 'd'
        _fact_ids = frozenset(['c'])

    all_fact_subsets = defaultdict(list)
    all_fact_subsets['a'].append(TestCollectorA)
    all_fact_subsets['b'].append(TestCollectorB)
    all_fact_subsets['b'].append(TestCollectorB) # add TestCollectorB twice
    all_fact_subsets['c'].append(TestCollectorC)
    all_fact_subsets

# Generated at 2022-06-13 00:28:25.125396
# Unit test for function build_dep_data
def test_build_dep_data():
    import examples
    # Test for the scenario where there exists a fact collector that depends on another fact collector
    # that does not exist
    collector_names = ['foo']
    all_fact_subsets = {
        'foo': [
            examples.MyFactCollector,
            examples.MyOtherFactCollector
        ]
    }
    dep_map = build_dep_data(collector_names, all_fact_subsets)
    assert list(dep_map.keys()) == ['foo']
    assert list(dep_map['foo']) == ['foo']
    # Test for the scenario where there exists a fact collector that depends on another fact collector
    # that does exist
    collector_names = ['foo']

# Generated at 2022-06-13 00:28:37.122722
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    class CollectorA(BaseFactCollector):
        _fact_ids = set(['a_fact'])
        name = 'collector-a'

    class CollectorB(BaseFactCollector):
        _fact_ids = set(['b_fact'])
        name = 'collector-b'

    collectors_for_platform = [CollectorA, CollectorB]

    collected_classes, aliases_map = build_fact_id_to_collector_map(collectors_for_platform)
    assert sorted(collected_classes.keys()) == sorted(['collector-a', 'collector-b', 'a_fact', 'b_fact'])
    assert sorted(aliases_map.keys()) == sorted(['collector-a', 'collector-b'])

# Generated at 2022-06-13 00:28:41.638937
# Unit test for function collector_classes_from_gather_subset
def test_collector_classes_from_gather_subset():
    from ansible.module_utils.facts import collector

    c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16 = [collector.BaseFactCollector for x in range(16)]

    c1._fact_ids = set(['c1', 'c1_1'])
    c1.name = 'c1_primary'
    c1.required_facts = set(['c2'])

    c2._fact_ids = set(['c2', 'c2_1'])
    c2.name = 'c2_primary'
    c2.required_facts = set(['c3'])


# Generated at 2022-06-13 00:28:53.422637
# Unit test for function find_collectors_for_platform
def test_find_collectors_for_platform():
    '''create a test case for a platform

    return a 2-tuple. first element is a set of collectors you would expect to
        be returned by find_collectors_for_platform. The second is a dict representing
        the system info.

    Code that uses this to give find_collectors_for_platform tries to do something clever.
        It iterates over all the collectors, asking if they are compatible with the
        platform info. The first collector to say yes, is used. If all return None,
        None is used.
    '''
    # register a few collectors to test
    # best practice is to add a name property to your class that is unique
    class Collector1(BaseFactCollector):
        _platform = 'system1'
        name = 'collector1'


# Generated at 2022-06-13 00:28:59.480900
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    all_fact_subsets = {
        'fact1': min_collector,
        'fact2': min_collector,
        'fact3': min_collector,
    }
    assert find_unresolved_requires(['fact1'], all_fact_subsets) == {'fact1'}
    assert find_unresolved_requires(['fact1', 'fact2'], all_fact_subsets) == {'fact2'}
    assert find_unresolved_requires(['fact1', 'fact2', 'fact3'], all_fact_subsets) == set()


# Generated at 2022-06-13 00:29:08.318535
# Unit test for function select_collector_classes
def test_select_collector_classes():
    class A(BaseFactCollector):
        _fact_ids = ['a', 'b']

    class B(BaseFactCollector):
        _fact_ids = ['b', 'c']

    class C(BaseFactCollector):
        _fact_ids = ['c', 'd']

    class D(BaseFactCollector):
        _fact_ids = ['d', 'e']

    collector_names = ['a', 'b', 'c', 'd', 'e']

    result = select_collector_classes(collector_names, {
        'a': [A],
        'b': [A, B],
        'c': [B, C],
        'd': [C, D],
        'e': [D],
    })

    assert result == [A, B, C, D]



# Generated at 2022-06-13 00:29:17.361415
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    class CollectorA(BaseFactCollector):
        _fact_ids = set(['collectorA'])
        name = 'collectorA'
        required_facts = set(['collectorB'])
    class CollectorB(BaseFactCollector):
        _fact_ids = set(['collectorB'])
        name = 'collectorB'
    class CollectorC(BaseFactCollector):
        _fact_ids = set(['collectorC'])
        name = 'collectorC'

    collector_classes = [CollectorA, CollectorB, CollectorC]

    all_fact_subsets = build_fact_id_to_collector_map(collector_classes)

    assert find_unresolved_requires(['collectorA'], all_fact_subsets) == set(['collectorB'])
    assert find

# Generated at 2022-06-13 00:29:40.280207
# Unit test for function build_dep_data
def test_build_dep_data():
    from collections import namedtuple
    Collector = namedtuple("Collector", ['required_facts'])
    collector_names = ('X', 'Y', 'A', 'B', 'C')
    all_fact_subsets = {
        'X': [Collector(['A'])],
        'Y': [Collector(['B'])],
        'A': [Collector(['B'])],
        'B': [Collector(['C'])],
        'C': [Collector([])]
        }
    res_dep_map = {
        'X': {'A'},
        'Y': {'B'},
        'A': {'B'},
        'B': {'C'},
        'C': set()
        }

# Generated at 2022-06-13 00:29:50.225833
# Unit test for function find_collectors_for_platform
def test_find_collectors_for_platform():
    '''test the find collectors'''

    import unittest
    import logging

    class PlatformTestCollector(BaseFactCollector):
        '''a collector that declares it is a mac'''
        _fact_ids = ['fact_2']

        _platform = 'Linux'
        name = 'collector_name'
        required_facts = set()

    def find_collectors_for_platform_mock_match(self, platform_info):
        if platform_info.get('system', None) == self._platform:
            return self

    class TestFindCollectors(unittest.TestCase):
        '''Test the find collectors functions'''
        def test_find_collectors_for_platform_basic(self):
            '''test find_collectors_for_platform_basic'''


# Generated at 2022-06-13 00:29:53.069372
# Unit test for function select_collector_classes
def test_select_collector_classes():
    # This function is tested by TestSelectCollectorClasses in test_ansible_module_utils_facts.py
    pass



# Generated at 2022-06-13 00:30:01.546265
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    import pytest

    all_fact_subsets = dict()
    all_fact_subsets["A"] = [1, 2]
    all_fact_subsets["B"] = [3, 4]
    all_fact_subsets["C"] = [5, 6]

    # Test an empty list
    assert find_unresolved_requires([], all_fact_subsets) == set([])

    # Test for a simple case
    # A has no deps
    # B depends on A
    # C depends on B
    collector_names = ["A", "B", "C"]

    all_fact_subsets["A"][0].required_facts = set()
    all_fact_subsets["A"][1].required_facts = set()

# Generated at 2022-06-13 00:30:06.644545
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    class A(BaseFactCollector):
        _fact_ids = set(['A'])
        name = 'A'
        required_facts = set(['B', 'C'])

    class B(BaseFactCollector):
        _fact_ids = set(['B'])
        name = 'B'
        required_facts = set()

    class C(BaseFactCollector):
        _fact_ids = set(['C'])
        name = 'C'
        required_facts = set()

    class D(BaseFactCollector):
        _fact_ids = set(['D'])
        name = 'D'
        required_facts = set()


# Generated at 2022-06-13 00:30:17.446685
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    class A(BaseFactCollector):
        _fact_ids = ['a1', 'a2']
        name = 'a1'
        required_facts = set()

    class B(BaseFactCollector):
        _fact_ids = ['b1', 'b2']
        name = 'b1'
        required_facts = {'c1'}

    class C(BaseFactCollector):
        _fact_ids = ['c1', 'c2']
        name = 'c1'
        required_facts = {'a1'}

    class D(BaseFactCollector):
        _fact_ids = ['d1', 'd2']
        name = 'd1'
        required_facts = {'c1', 'd2'}

    # 'b' requires 'c', 'c' requires 'a' and 'd

# Generated at 2022-06-13 00:30:29.172187
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    from ansible.module_utils.facts import collector

    def _collector(*args):
        return type('collector', (BaseFactCollector,), {'required_facts': set(args)})

    class TestCollector1(_collector('f1', 'f2')):
        name = 'c1'
    class TestCollector2(_collector('f1', 'f2', 'c1')):
        name = 'c2'

    result = find_unresolved_requires(['c1'], {'c1': [TestCollector1], 'c2': [TestCollector2]})
    assert result == set(['f1', 'f2'])


# Generated at 2022-06-13 00:30:37.408117
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():

    class collector1(BaseFactCollector):
        name = 'collector1'
        required_facts = ('collector1_required',)

    class collector2(BaseFactCollector):
        name = 'collector2'
        required_facts = ('collector2_required',)

    class collector3(BaseFactCollector):
        name = 'collector3'
        required_facts = ('collector1_required', 'collector2_required')

    all_fact_subsets = {
        'collector1': [collector1],
        'collector2': [collector2],
        'collector3': [collector3],
    }

    collector_names = set(['collector1', 'collector2'])

# Generated at 2022-06-13 00:30:48.539027
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    class A(BaseFactCollector):
        name = 'A'
    class B(BaseFactCollector):
        name = 'B'
        required_facts = {'A'}

    all_fact_subsets = {
        'A': A,
        'B': B,
    }
    assert find_unresolved_requires(['A', 'B'], all_fact_subsets) == set()
    assert find_unresolved_requires(['B', 'A'], all_fact_subsets) == set()
    assert find_unresolved_requires(['A'], all_fact_subsets) == {'B'}
    assert find_unresolved_requires(['B'], all_fact_subsets) == set()

    class B2(BaseFactCollector):
        name = 'B'


# Generated at 2022-06-13 00:30:57.593316
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    collector1_class = type('Collector1',
                            (BaseFactCollector,),
                            {'_fact_ids': {'fact1', 'fact2'},
                             'name': 'collector1'})

    collector2_class = type('Collector2',
                            (BaseFactCollector,),
                            {'_fact_ids': {'fact1'},
                             'name': 'collector2'})

    fact_id_to_collector_map, aliases_map = build_fact_id_to_collector_map(
        {collector1_class, collector2_class})

    assert aliases_map == defaultdict(set, {'collector1': {'fact1', 'fact2'},
                                            'collector2': {'fact1'}})
    assert fact_id

# Generated at 2022-06-13 00:31:21.893556
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    from ansible.module_utils.facts import collector
    from ansible.module_utils.facts.system.distribution import DistributionFactCollector
    from ansible.module_utils.facts.system.distribution.uname import UnameFactCollector

    class DummyCollector(DistributionFactCollector):
        _fact_ids = ('distribution',)
        name = 'dummy'

        @classmethod
        def platform_match(cls, platform_info):
            return cls

    # All subclass requirements should get picked up
    collector_name_list = ['non-existent', 'uname', 'distribution']
    unresolved = find_unresolved_requires(collector_name_list, collector.FACT_SUBSETS)

# Generated at 2022-06-13 00:31:26.653094
# Unit test for function select_collector_classes
def test_select_collector_classes():
    from ansible.module_utils.facts.system.distribution import DistributionFactCollector

    # Setup data
    collector_names = ['distribution']
    all_fact_subsets = {
        'distribution' : [DistributionFactCollector]
    }

    # Test function
    selected = select_collector_classes(collector_names, all_fact_subsets)
    assert selected == [DistributionFactCollector]

    # Test again with a ordering that has a duplicate
    collector_names = ['distribution', 'distribution']
    selected = select_collector_classes(collector_names, all_fact_subsets)
    assert selected == [DistributionFactCollector]



# Generated at 2022-06-13 00:31:34.446864
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    collector_names = ['foo','bar','baz','unknown']
    all_fact_subsets = {
        'foo': [
            MockCollector(name='foo',required_facts=set()),
        ],
        'bar': [
            MockCollector(name='bar',required_facts=set(['foo'])),
        ],
        'baz': [
            MockCollector(name='baz',required_facts=set(['foo','bar'])),
        ],
        'unknown': [
            MockCollector(name='unknown',required_facts=set(['foo','bar','missing'])),
        ],
    }

    assert set(find_unresolved_requires(collector_names, all_fact_subsets)) == set(['missing'])



# Generated at 2022-06-13 00:31:45.178388
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    '''Check that build_fact_id_to_collector_map creates correct mappings
    for fact_id_to_collector_map and aliases_map
    '''
    class A(BaseFactCollector):
        _fact_ids = set()
        name = 'A'

    class B(BaseFactCollector):
        _fact_ids = set()
        name = 'B'

    class C(BaseFactCollector):
        _fact_ids = {'C'}
        name = 'C'

    class D(BaseFactCollector):
        _fact_ids = {'D'}
        name = 'D'

    class E(BaseFactCollector):
        _fact_ids = {'E', 'E1'}
        name = 'E'

    class F(BaseFactCollector):
        _fact

# Generated at 2022-06-13 00:31:56.208318
# Unit test for function select_collector_classes
def test_select_collector_classes():
    class Collector_class:
        name = 'name'
        fact_ids = set()


# Generated at 2022-06-13 00:32:06.547956
# Unit test for function build_dep_data
def test_build_dep_data():
    from ansible.module_utils._text import to_text
    from ansible.module_utils.facts.collector.system import SystemFactCollector
    import json
    dep_data = build_dep_data(['all'], {'all': [SystemFactCollector]})
    dep_data = json.loads(to_text(json.dumps(dep_data)))
    assert "all" in dep_data.keys()
    assert "generic" in dep_data["all"]
    assert "system" in dep_data["all"]
    assert "virtual" in dep_data["all"]
    assert "mounts" in dep_data["all"]
    assert "distribution" in dep_data["all"]
    assert "python" in dep_data["all"]
    assert "default_ipv4" in dep_data["all"]

# Generated at 2022-06-13 00:32:09.477227
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    class TestCollector(BaseFactCollector):
        _fact_ids = ['test_foo']
        name = 'test'
    assert len(build_fact_id_to_collector_map([TestCollector])[0]) == 2


# Generated at 2022-06-13 00:32:18.747439
# Unit test for function select_collector_classes
def test_select_collector_classes():
    config_collector_class = type(
        'ConfigCollector',
        (BaseFactCollector,),
        {'name': 'config', '_fact_ids': {'all_config'}})

    ntp_collector_class = type(
        'NTPCollector',
        (BaseFactCollector,),
        {'name': 'ntp', '_fact_ids': {'ntp'}})

    ssl_cert_collector_class = type(
        'SSLCertCollector',
        (BaseFactCollector,),
        {'name': 'ssld', '_fact_ids': {'ssld', 'ssl_cert'}})


# Generated at 2022-06-13 00:32:27.135148
# Unit test for function build_dep_data
def test_build_dep_data():
    collector_names = ['SystemHardware', 'SystemProduct', 'SystemPlatform', 'SystemSerialNumber', 'Environment', 'NetworkConfig', 'NetworkInterfaces', 'Localhost']

# Generated at 2022-06-13 00:32:36.909967
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    '''test finding unresolved requires'''
    class MockAllFactsSubsetsClass:
        '''a mock of the all_fact_subsets object'''
        def __init__(self, collector_to_classes_map):
            self.collector_to_classes_map = collector_to_classes_map

        def __iter__(self):
            return iter(self.collector_to_classes_map)

        def __contains__(self, key):
            return key in self.collector_to_classes_map

        def __getitem__(self, key):
            return self.collector_to_classes_map[key]

    class MockCollectorClass:
        '''a mock of the CollectorClass class'''
        def __init__(self, required_facts):
            self.required_facts = required_facts

# Generated at 2022-06-13 00:33:01.249927
# Unit test for function select_collector_classes
def test_select_collector_classes():
    class CollectorClassA(BaseFactCollector):
        _fact_ids = set(['a'])
        name = 'a'
        required_facts = set()

    class CollectorClassB(BaseFactCollector):
        _fact_ids = set(['b'])
        name = 'b'
        required_facts = set()

    class CollectorClassC(BaseFactCollector):
        _fact_ids = set(['c'])
        name = 'c'
        required_facts = set(['a'])

    class CollectorClassD(BaseFactCollector):
        _fact_ids = set(['d'])
        name = 'd'
        required_facts = set()

    class CollectorClassE(BaseFactCollector):
        _fact_ids = set(['e'])
        name = 'e'
        required_

# Generated at 2022-06-13 00:33:06.835276
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    from ansible.module_utils.facts.collector.cloud.aws import AWSCollector
    assert find_unresolved_requires({'network'}, {'network': [AWSCollector]}) == {'aws'}
    assert find_unresolved_requires({'aws'}, {'network': [AWSCollector]}) == set()



# Generated at 2022-06-13 00:33:15.026139
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    import pytest
    # Make a mock set of all_fact_subsets

# Generated at 2022-06-13 00:33:26.727875
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    class TestCollector1(BaseFactCollector):
        name = 'test_collector_1'
    class TestCollector2(BaseFactCollector):
        name = 'test_collector_2'
        _fact_ids = set(['test_collector_2', 'test_collector_2_alias'])
    class TestCollector3(BaseFactCollector):
        name = 'test_collector_3'
        _fact_ids = set(['test_collector_3', 'test_collector_3_alias1', 'test_collector_3_alias2'])

    fact_id_to_collector_map, aliases_map = build_fact_id_to_collector_map([TestCollector1, TestCollector2, TestCollector3])

    assert fact_id_to_collector_

# Generated at 2022-06-13 00:33:32.564627
# Unit test for function build_dep_data
def test_build_dep_data():
    dep_map = build_dep_data(['a', 'b', 'c', 'd', 'e'], {
        'a': ['d', 'e'],
        'b': ['e'],
        'c': ['d'],
        'd': ['a'],
        'e': ['c']})
    assert dep_map == {
        'a': set(['d', 'e']),
        'b': set(['e']),
        'c': set(['d']),
        'd': set(['a']),
        'e': set(['c'])}



# Generated at 2022-06-13 00:33:42.976152
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    from .system.distribution import DistributionFactCollector
    from .hardware.bios import BiosFactCollector
    from .hardware.main import MainCollector, main_collector_classes
    from ansible.module_utils.facts.system.hostname import HostnameFactCollector

    all_collector_classes = set()
    all_collector_classes.update(main_collector_classes)
    all_collector_classes.add(DistributionFactCollector)
    all_collector_classes.add(BiosFactCollector)
    all_collector_classes.add(HostnameFactCollector)

    # we should be able to get all the classes for the platform
    platform_info = {
        'system': 'Linux'
    }
    compat_platforms = (platform_info, )

    collectors_for

# Generated at 2022-06-13 00:33:53.249526
# Unit test for function build_dep_data
def test_build_dep_data():
    from . import linux as linux_collectors

    collectors = [
        linux_collectors.DistributionCollector,
        linux_collectors.DmiFacts,
        linux_collectors.HardwareCollector,
        linux_collectors.NetworkCollector,
    ]

    all_fact_subsets = defaultdict(set)

    for collector in collectors:
        for fact_id in collector._fact_ids:
            all_fact_subsets[fact_id].add(collector)

    dep_map = build_dep_data(set(all_fact_subsets.keys()), all_fact_subsets)
    assert set(dep_map.keys()) == set(all_fact_subsets.keys())


# Generated at 2022-06-13 00:34:00.178243
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    all_fact_subsets = {
        'a': [object()]
    }

    assert find_unresolved_requires(['b'], all_fact_subsets) == {'b'}

    class A(object):
        required_facts = {'b'}

    class B(object):
        required_facts = set()

    all_fact_subsets = {
        'a': [A],
        'b': [B]
    }

    assert find_unresolved_requires(['a'], all_fact_subsets) == set()
    assert find_unresolved_requires(['a', 'b'], all_fact_subsets) == set()
    assert find_unresolved_requires(['b', 'a'], all_fact_subsets) == set()
    assert find_unres

# Generated at 2022-06-13 00:34:08.396066
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    class CollectorClass1(BaseFactCollector):
        name = 'fact_name_1'
        _fact_ids = ('fact_id_1',)
        required_facts = set()
    class CollectorClass2(BaseFactCollector):
        name = 'fact_name_2'
        _fact_ids = ('fact_id_1', 'fact_id_2')
        required_facts = set()
    class CollectorClass3(BaseFactCollector):
        name = 'fact_name_3'
        _fact_ids = ('fact_id_3',)
        required_facts = set()
    collector_classes = (CollectorClass1, CollectorClass2, CollectorClass3)