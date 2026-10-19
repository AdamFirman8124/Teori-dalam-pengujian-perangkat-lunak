

# Generated at 2022-06-13 00:24:42.202946
# Unit test for function get_collector_names
def test_get_collector_names():
    valid_subsets = frozenset(['subsetA', 'subsetB', 'subsetC'])
    minimal_gather_subsets = frozenset(['subsetA', 'subsetB'])
    aliases_map = defaultdict(set, {'subsetC': ['subsetCA', 'subsetCB']})

    assert get_collector_names(valid_subsets, minimal_gather_subsets) == minimal_gather_subsets
    assert get_collector_names(valid_subsets, minimal_gather_subsets, ['!subsetA']) == frozenset(['subsetB'])

# Generated at 2022-06-13 00:24:51.006258
# Unit test for function tsort
def test_tsort():
    test_data_1 = {
        'x': {'a', 'b'},
        'a': {'c'},
        'b': {'a'},
        'c': set(),
    }
    print(tsort(test_data_1))
    assert tsort(test_data_1) == [('x', {'a', 'b'}), ('a', {'c'}), ('b', {'a'}), ('c', set())]



# Generated at 2022-06-13 00:24:58.576209
# Unit test for function get_collector_names
def test_get_collector_names():
    assert get_collector_names(
        valid_subsets=frozenset(['all', 'a', 'b', 'c']),
        gather_subset=['all'],
    ) == set(['all', 'a', 'b', 'c'])

    assert get_collector_names(
        valid_subsets=frozenset(['all', 'a', 'b', 'c']),
        gather_subset=['all', '!c'],
    ) == set(['all', 'a', 'b'])


# Generated at 2022-06-13 00:25:07.812016
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    '''Unit test for function find_unresolved_requires'''

    all_fact_subsets = {}
    all_fact_subsets['all'] = [FakeAllCollector]
    all_fact_subsets['os'] = [FakeOSCollector, FakeOSCollector2]

    assert find_unresolved_requires(['all'], all_fact_subsets) == set()
    assert find_unresolved_requires(['all', 'os'], all_fact_subsets) == set()
    assert find_unresolved_requires(['os'], all_fact_subsets) == set(['os'])
    assert find_unresolved_requires(['fake'], all_fact_subsets) == set(['fake'])



# Generated at 2022-06-13 00:25:19.251106
# Unit test for function get_collector_names
def test_get_collector_names():
    assert get_collector_names(
        ['all'],
        frozenset(['min']),
        ['all'],
    ) == frozenset(['min'])
    assert get_collector_names(
        ['all'],
        frozenset(['min']),
        ['network'],
    ) == frozenset(['network', 'min'])
    assert get_collector_names(
        ['network'],
        frozenset(['min']),
        ['all'],
    ) == frozenset(['network', 'min'])
    assert get_collector_names(
        ['network'],
        frozenset(['min']),
        ['!all'],
    ) == frozenset(['min'])

# Generated at 2022-06-13 00:25:28.937053
# Unit test for function select_collector_classes
def test_select_collector_classes():
    class A(BaseFactCollector):
        name = 'A'
        _fact_ids = ['B']

    class A1(BaseFactCollector):
        name = 'A'
        _fact_ids = ['B']

    class B(BaseFactCollector):
        name = 'B'

    class C(BaseFactCollector):
        name = 'C'

    all_fact_subsets = {
            'A': [A, A1],
            'B': [B],
            'C': [C],
            }

    # list is the same as input, expect no duplicates
    assert select_collector_classes(['A', 'B', 'C'], all_fact_subsets) == [A, B, C]

    # A and A1 both provide name A, but won't be in the output twice
   

# Generated at 2022-06-13 00:25:34.509891
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    all_fact_subsets = {'a': [BaseFactCollector],
                        'b': [BaseFactCollector],
                        'c': [BaseFactCollector],
                        }
    # have BaseFactCollector.required_facts be a frozenset for the test
    setattr(BaseFactCollector, 'required_facts', frozenset())

    # test normal usage
    assert find_unresolved_requires(['a'], all_fact_subsets) == set()
    assert find_unresolved_requires(['b'], all_fact_subsets) == set()

    # after adding requires_facts, fails
    setattr(BaseFactCollector, 'required_facts', frozenset(['b']))

# Generated at 2022-06-13 00:25:44.405271
# Unit test for function build_dep_data
def test_build_dep_data():
    assert build_dep_data(['iama', 'ibma'], {
        'iama': [object, object],
        'ibma': [object, object],
        }
    ) == {
        'iama': set(),
        'ibma': set(),
    }
    assert build_dep_data(['iama', 'ibma'], {
        'iama': [object, object],
        'ibma': [object, object],
        }
    ) == {
        'iama': set(),
        'ibma': set(),
    }

# Generated at 2022-06-13 00:25:55.098045
# Unit test for function build_dep_data
def test_build_dep_data():
    all_fact_subsets = {'a': [object()], 'b': [object()]}

    dep_map = build_dep_data(['a'], all_fact_subsets)
    assert dep_map == {'a': set()}

    class Dep1(object):
        name = 'a'
        required_facts = []

    class Dep2(object):
        name = 'b'
        required_facts = ['a']

    all_fact_subsets = {'a': [Dep1()], 'b': [Dep2()]}

    dep_map = build_dep_data(['a', 'b'], all_fact_subsets)
    assert dep_map == {'a': set(), 'b': {'a'}}



# Generated at 2022-06-13 00:26:05.632949
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    result = find_unresolved_requires(['a', 'b'], {'a': [], 'b': [], 'c': []})
    assert result == set(['c'])

    result = find_unresolved_requires(['a'], {'a': [], 'b': [], 'c': []})
    assert result == set(['c', 'b'])

    result = find_unresolved_requires(['a'], {'a': [], 'b': [], 'c': []})
    assert result == set(['c', 'b'])

    result = find_unresolved_requires(['a'], {'a': [], 'b': [], 'c': []})
    assert result == set(['c', 'b'])



# Generated at 2022-06-13 00:26:16.142872
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    import pytest

    collector_names = ['f1', 'f2']
    all_fact_subsets = {'f1': [FakeFactCollector('f1', requires=set(['f3']))]}
    actual = find_unresolved_requires(collector_names, all_fact_subsets)
    assert set(['f3']) == actual



# Generated at 2022-06-13 00:26:24.572577
# Unit test for function find_collectors_for_platform
def test_find_collectors_for_platform():
    from ansible.module_utils.facts.collectors import (
        all as all_fact_collectors,
        generic,
        linux,
        network,
        windows,
        )
    from ansible.module_utils.facts.collectors.network import NetworkCollector

    assert not find_collectors_for_platform(all_fact_collectors, [{'system': 'any'}])
    assert set(find_collectors_for_platform(all_fact_collectors, [{'system': 'Linux'}])) == set([generic.GenericCollector, linux.LinuxCollector])
    assert set(find_collectors_for_platform(all_fact_collectors, [{'system': 'Linux'}, {'system': 'FreeBSD'}])) == set([generic.GenericCollector, linux.LinuxCollector])


# Generated at 2022-06-13 00:26:36.796455
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    class collector_0(BaseFactCollector):
        name = 'collector_0'
        _fact_ids = ['c0_fact']

    class collector_1(BaseFactCollector):
        name = 'collector_1'
        _fact_ids = ['c1_fact']

    class collector_2(BaseFactCollector):
        name = 'collector_2'
        _fact_ids = ['c2_fact']

    test_collectors = [collector_0,
                       collector_1,
                       collector_2]

    fact_id_to_collector_map, aliases_map = build_fact_id_to_collector_map(test_collectors)


# Generated at 2022-06-13 00:26:45.755691
# Unit test for function select_collector_classes
def test_select_collector_classes():
    class Collector1(BaseFactCollector):
        name = 'collector1'
        _fact_ids = set(('alias1',))

    class Collector2(BaseFactCollector):
        name = 'collector2'
        _fact_ids = set(('alias2',))

    class Collector3(BaseFactCollector):
        name = 'collector3'
        _fact_ids = set(('alias3',))

    class Collector4(BaseFactCollector):
        name = 'collector4'
        _fact_ids = set(('alias4',))

    # collector1 can be selected by specifying primary name or alias
    # collector2 cannot be selected by either primary name or alias
    # collector3 cannot be selected by the alias3
    # collector4 can be selected by primary name or alias4

# Generated at 2022-06-13 00:26:54.959679
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    collector_names = ['min', 'all', '!redundant']
    all_fact_subsets = {
        'min': [BaseFactCollector],
        'all': [BaseFactCollector],
        'redundant': [BaseFactCollector],
    }
    unresolved = find_unresolved_requires(collector_names, all_fact_subsets)
    assert not unresolved

    # make all require 'min'
    for collector_class in all_fact_subsets['all']:
        collector_class.required_facts = {'min'}

    unresolved = find_unresolved_requires(collector_names, all_fact_subsets)
    assert not unresolved

    # make 'redundant' require 'min'
    for collector_class in all_fact_subsets['redundant']:
        collector

# Generated at 2022-06-13 00:27:06.582457
# Unit test for function select_collector_classes
def test_select_collector_classes():
    class CollectorA(BaseFactCollector):
        _fact_ids = {'a', 'b'}
        name = 'a'
    class CollectorB(BaseFactCollector):
        _fact_ids = {'b', 'c'}
        name = 'b'
    class CollectorC(BaseFactCollector):
        _fact_ids = {'c', 'd'}
        name = 'c'
    class CollectorD(BaseFactCollector):
        _fact_ids = {'d', 'a'}
        name = 'd'

    all_fact_subsets = {
        'a': [CollectorA],
        'b': [CollectorB],
        'c': [CollectorC],
        'd': [CollectorD],
    }


# Generated at 2022-06-13 00:27:14.106027
# Unit test for function build_dep_data
def test_build_dep_data():
    collector_names = set(['a', 'b'])
    all_fact_subsets = {}
    all_fact_subsets['a'] = [base.BaseFactCollector(None, None)]
    all_fact_subsets['b'] = [base.BaseFactCollector(None, None)]
    all_fact_subsets['a'][0].required_facts = {'b'}
    all_fact_subsets['b'][0].required_facts = {'c'}
    dep_map = build_dep_data(collector_names, all_fact_subsets)
    assert dep_map == {'a': {'b'}, 'b': {'c'}}



# Generated at 2022-06-13 00:27:25.381493
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    import ansible.module_utils.facts.system.distribution as distribution
    distribution.DistributionFactCollector = distribution.FreeBSDDistributionFactCollector
    from ansible.module_utils.facts.system import distribution
    from ansible.module_utils.facts.system import dmidecode
    from ansible.module_utils.facts.system import hardware
    from ansible.module_utils.facts.system import lsbin
    from ansible.module_utils.facts.system import platform
    from ansible.module_utils.facts.system import selinux
    from ansible.module_utils.facts.system import user
    from ansible.module_utils.facts.system import virtual
    from ansible.module_utils.facts.system import zone


# Generated at 2022-06-13 00:27:33.420248
# Unit test for function find_collectors_for_platform
def test_find_collectors_for_platform():
    class TestCollector1(BaseFactCollector):
        _platform = 'TestPlatform'
        name = 'TestCollector1'

    class TestCollector2(BaseFactCollector):
        _platform = 'TestPlatform'
        name = 'TestCollector2'

    class TestCollector3(BaseFactCollector):
        _platform = 'TestPlatform'
        name = 'TestCollector3'

    class TestCollector4(BaseFactCollector):
        _platform = 'Linux'
        name = 'TestCollector4'

    class TestCollector5(BaseFactCollector):
        _platform = 'Linux'
        name = 'TestCollector5'

    class TestCollector6(BaseFactCollector):
        name = 'TestCollector6'


# Generated at 2022-06-13 00:27:45.833483
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    # NameError is raised when the collector is not found
    from ansible.module_utils.facts import collector

    collector_name = 'processor'
    with pytest.raises(NameError):
        _get_require_by_collector_name(collector_name)

    # AssertionError is raised when the collector's requires_facts
    # are not in the names of the other collectors
    collector_name = "procesor"
    with pytest.raises(AssertionError):
        _get_require_by_collector_name(collector_name)

    # KeyError is raised if a required fact is not in the
    # list of other collector names
    collector_name = "processor"

# Generated at 2022-06-13 00:28:05.010257
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    import ansible.module_utils.facts.system.linux as lnx
    import ansible.module_utils.facts.system.windows as win
    import ansible.module_utils.facts.network.bsd as bsd
    import ansible.module_utils.facts.system.freebsd as fbsd

    # We throw a random class as an example
    random_class = lnx.LinuxVirtual
    random_class.name = "random_class"
    random_class._fact_ids = ['linuxvirt']
    random_class._platform = 'Linux'

    # First class
    class1 = lnx.LinuxAll
    class1.name = "class1"
    class1._fact_ids = ['linuxall']
    class1._platform = 'Linux'

    # Second class
    class2 = lnx

# Generated at 2022-06-13 00:28:15.983787
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    from . import default

    class CollectorA(BaseFactCollector):
        name = 'collector_a'
        required_facts = set(('collector_b',))

    class CollectorB(BaseFactCollector):
        name = 'collector_b'
        required_facts = set(('collector_c',))

    class CollectorC(BaseFactCollector):
        name = 'collector_c'

    def _make_collector_map(classes):
        return {cls.name: [cls] for cls in classes}

    all_fact_subsets = defaultdict(list)
    all_fact_subsets.update(_make_collector_map([ CollectorA, CollectorB, CollectorC ]))

# Generated at 2022-06-13 00:28:25.821881
# Unit test for function select_collector_classes
def test_select_collector_classes():
    required_by = {'a': frozenset(['b']),
                   'b': frozenset(['c']),
                   'c': frozenset(['d']),
                   'd': frozenset(['e']),
                   'e': frozenset(),
                   }
    ordered = topological_sort_names(required_by)
    assert ordered == ['e', 'd', 'c', 'b', 'a']

    required_by = {'a': frozenset(['b', 'c']),
                   'b': frozenset(['d']),
                   'c': frozenset(['d']),
                   'd': frozenset(['e']),
                   'e': frozenset(),
                   }
    ordered = topological_sort_names(required_by)

# Generated at 2022-06-13 00:28:37.866350
# Unit test for function find_collectors_for_platform
def test_find_collectors_for_platform():
    '''Test that the right collector classes are returned, given platform info and collector classes
    '''
    # generic linux must be found
    LinuxGenericCollector = type('LinuxGeneric',
                                 (BaseFactCollector,),
                                 {'_platform': 'linux', 'name': 'LinuxGeneric'},
                                 )
    # but, LinuxRedHat must be preferred for linux
    LinuxRedHatCollector = type('LinuxRedHat',
                                (BaseFactCollector,),
                                {'_platform': 'linux', 'name': 'LinuxRedHat'},
                                )
    # this guy is a 'generic' windows class. It should be found for windows.

# Generated at 2022-06-13 00:28:48.593347
# Unit test for function find_collectors_for_platform
def test_find_collectors_for_platform():
    from ansible.module_utils.facts.collector.linux import LinuxHardware
    from ansible.module_utils.facts.collector.linux import LinuxNetwork

    all_collector_classes = (LinuxHardware, LinuxNetwork)
    compat_platforms = ( dict(system='Linux'), dict(system='Generic') )
    platform_match_result = find_collectors_for_platform(all_collector_classes, compat_platforms)
    assert platform_match_result == set(all_collector_classes)

    compat_platforms = ( dict(system='Solaris'), dict(system='FreeBSD') )
    platform_match_result = find_collectors_for_platform(all_collector_classes, compat_platforms)
    assert platform_match_result == set()



# Generated at 2022-06-13 00:28:58.142803
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    class collector1(BaseFactCollector):
        _fact_ids = frozenset(['fact1a', 'fact1b'])
        name = 'primary-fact-id'

        def collect(self, module=None, collected_facts=None):
            return dict(fact1a=None, fact1b=None)

    class collector2(BaseFactCollector):
        _fact_ids = frozenset(['fact2a'])

        def collect(self, module=None, collected_facts=None):
            return dict(fact2a=None)

    collectors_for_platform = [collector1, collector2]

    fact_id_to_collector_map = build_fact_id_to_collector_map(collectors_for_platform)


# Generated at 2022-06-13 00:29:07.486176
# Unit test for function find_collectors_for_platform
def test_find_collectors_for_platform():
    class collector1(BaseFactCollector):
        name = 'collector1'
        _platform = 'Linux'

    class collector2(BaseFactCollector):
        name = 'collector2'

    collectors = set([collector1, collector2])
    platform_info = {'system': 'Linux', 'distribution': 'RedHat'}
    found_collectors = find_collectors_for_platform(collectors, [platform_info])
    assert(len(found_collectors) == 2)

    found_collectors = find_collectors_for_platform(collectors, [])
    assert(len(found_collectors) == 2)

    platform_info = {'system': 'Unknown', 'distribution': 'Unknown'}

# Generated at 2022-06-13 00:29:16.638437
# Unit test for function find_collectors_for_platform
def test_find_collectors_for_platform():
    all_collector_classes = []
    class CollectableClass1:
        name='fake_collector_1'
        required_facts = set(['_platform_a'])
        _platform = 'fake'
        def __init__(self):
            self.fact_ids = set([self.name])
        @classmethod
        def platform_match(cls, platform_info):
            if platform_info.get('system', None) == cls._platform:
                return cls
            return None
    all_collector_classes.append(CollectableClass1)
    class CollectableClass2:
        name='fake_collector_2'
        required_facts = set(['_platform_b'])
        _platform = 'fake'

# Generated at 2022-06-13 00:29:27.347819
# Unit test for function select_collector_classes
def test_select_collector_classes():
    from ansible.module_utils.facts.system.distribution import DistributionFactCollector
    from ansible.module_utils.facts.system.pkg_mgr import PkgMgrFactCollector
    from ansible.module_utils.facts.system.distribution import DistributionFactCollector as D1
    from ansible.module_utils.facts.system.distribution import DistributionFactCollector as D2
    from ansible.module_utils.facts.system.distribution import DistributionFactCollector as D3
    from ansible.module_utils.facts.system.pkg_mgr import PkgMgrFactCollector as P1

    def check_contains(l, name):
        return len([x for x in l if x.name == name]) > 0

    class A(object):
        name = 'A'


# Generated at 2022-06-13 00:29:32.771029
# Unit test for function find_collectors_for_platform
def test_find_collectors_for_platform():
    '''Test find_collectors_for_platform'''
    import os

    module_name = os.path.basename(__file__)

    # This is a really simple test.
    #
    # The real test is in unit/test_ansible_facts.py
    # This is a unit test of a utility function that is used
    # to find the correct fact collectors for the system.

    class TestFactCollector(BaseFactCollector):
        '''TestFactsCollector is a dummy class for testing.'''
        name = 'TestFactCollector'
        _fact_ids = set(['test'])

    found_collectors = find_collectors_for_platform(
        [
            TestFactCollector,
        ],
        [
            {'system': 'Generic'},
        ],
    )

    # only

# Generated at 2022-06-13 00:29:52.891212
# Unit test for function get_collector_names
def test_get_collector_names():
    # all cases
    assert get_collector_names() == set(['network', 'hardware', 'virtual', 'firmware', 'software', 'system'])
    assert get_collector_names(gather_subset=[]) == set(['network', 'hardware', 'virtual', 'firmware', 'software', 'system'])
    assert get_collector_names(gather_subset=['all']) == set(['network', 'hardware', 'virtual', 'firmware', 'software', 'system'])
    assert get_collector_names(gather_subset=['!all']) == set(['network', 'hardware', 'virtual', 'firmware', 'software', 'system'])

# Generated at 2022-06-13 00:30:01.369116
# Unit test for function get_collector_names
def test_get_collector_names():
    def _test_get_collector_names(gather_subset,
                                  valid_subsets,
                                  minimal_gather_subset,
                                  aliases_map,
                                  expected):
        actual = get_collector_names(gather_subset=gather_subset,
                                     valid_subsets=valid_subsets,
                                     minimal_gather_subset=minimal_gather_subset,
                                     aliases_map=aliases_map)
        assert actual == expected, "actual={} != expected={}".format(actual, expected)

    # When gather_subset is none and valid_subsets is empty, empty set
    # should be returned

# Generated at 2022-06-13 00:30:14.359611
# Unit test for function find_collectors_for_platform

# Generated at 2022-06-13 00:30:25.262090
# Unit test for function build_dep_data
def test_build_dep_data():
    class A(BaseFactCollector):
        name = 'A'
        required_facts = set()

    class B(BaseFactCollector):
        name = 'B'
        required_facts = {'A'}

    class C(BaseFactCollector):
        name = 'C'
        required_facts = {'A', 'B'}

    class D(BaseFactCollector):
        name = 'D'
        required_facts = {'C'}

    all_fact_subsets = {
        'A': [A],
        'B': [B],
        'C': [C],
        'D': [D],
    }


# Generated at 2022-06-13 00:30:35.184225
# Unit test for function find_collectors_for_platform
def test_find_collectors_for_platform():
    import os

    # stub class so that we can access module_utils.facts without actually
    # importing it. This only works because the function under test creates
    # an instance of it and doesn't do anything with it except call methods
    # on it that already have stubs.
    class StubModuleBase(object):
        def __init__(self):
            self.params = {}

        # facts_module.find_collector_classes returns a list of FactCollectors
        # so stub that out here.
        # NOTE: if you change the return value of this, you likely also need
        # to change the return value of platform_match called during the test

# Generated at 2022-06-13 00:30:44.049844
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    collector_names = ['one', 'two']
    all_fact_subsets = {
        'one': [_TestOne],
        'two': [_TestTwo],
        }
    assert find_unresolved_requires(collector_names, all_fact_subsets) == set()
    collector_names = ['one', 'two', 'three']
    all_fact_subsets = {
        'one': [_TestOne],
        'two': [_TestTwo],
        'three': [_TestThree],
        }
    assert find_unresolved_requires(collector_names, all_fact_subsets) == set()
    collector_names = ['one', 'three']

# Generated at 2022-06-13 00:30:54.420393
# Unit test for function select_collector_classes
def test_select_collector_classes():
    from ansible.module_utils.facts import default
    import copy
    import unittest

    class MockDefaultCollectorClass(BaseFactCollector):
        name = 'default'
        required_facts = set()

    class MockNetworkCollectorClass(BaseFactCollector):
        name = 'network'
        required_facts = set()

    class MockHardwareCollectorClass(BaseFactCollector):
        name = 'hardware'
        required_facts = set(['network', 'default'])

    class MockNetworkHWCollectorClass(BaseFactCollector):
        name = 'hardware'
        required_facts = set(['network'])

    class MockDefaultHWCollectorClass(BaseFactCollector):
        name = 'hardware'
        required_facts = set(['default'])


# Generated at 2022-06-13 00:31:06.334858
# Unit test for function find_collectors_for_platform
def test_find_collectors_for_platform():
    from ansible.module_utils.facts.collectors import network

    # Remove cached collections
    for collector in network.NetworkCollector.__subclasses__():
        if collector._instances:
            collector._instances.clear()

    # Make collection of collectors
    collector_classes = [
        c
        for c in network.NetworkCollector.__subclasses__()
        if c.name != 'default'
    ]

    # Useful for debugging/making tests
    for c in collector_classes:
        print(c.name)

    # Basic fetching
    assert find_collectors_for_platform(collector_classes, [{'system': 'AIX'}]) == set([network.AIXCollector])
    assert find_collectors_for_platform(collector_classes, [{'system': 'Generic'}]) == set

# Generated at 2022-06-13 00:31:14.630062
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    '''This test demonstrates how to write a unit test for find_unresolved_requires.
       You can run this with "python -m unit_test -v test_utils.test_find_unresolved_requires".
    '''
    # test_collectors is a list of collector classes. Since the find_unresolved_requires
    # function only needs the names of the collectors, we can create a simple list of
    # tuples to use in the test.
    test_collectors = [
        ('c1',),
        ('c2', 'c3'),
        ('c3', 'c4'),
        ('c4',),
    ]

    # This function converts the test_collectors tuple into the form that find_unresolved_requires
    # requires. It returns a dictionary where the keys are the collector name and the values
    # are

# Generated at 2022-06-13 00:31:24.813103
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    from ansible.module_utils.facts.system.base import BaseFactCollector
    from ansible.module_utils.facts.system.distribution.freebsd import FreeBSDFactCollector

    # Test case 1: no collector class has requires_facts()
    all_fact_subsets = {'foo': [BaseFactCollector,]}
    collector_names = ['foo',]
    assert(find_unresolved_requires(collector_names, all_fact_subsets) == set())

    # Test case 2: no 'requires_facts' is in collector_names
    all_fact_subsets = {'foo': [BaseFactCollector,]}
    collector_names = ['foo',]
    assert(find_unresolved_requires(collector_names, all_fact_subsets) == set())

    # Test case 3: has

# Generated at 2022-06-13 00:31:52.395471
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    from ansible.module_utils.facts import collectors
    from ansible.module_utils.facts.collectors.base import BaseFactCollector

    class Collector1(BaseFactCollector):
        name = 'collector1'


    class Collector2(BaseFactCollector):
        name = 'collector2'


    class Collector3(BaseFactCollector):
        name = 'collector3'
        _fact_ids = {'_fact_ids2'}


    use_collectors = [Collector1, Collector2, Collector3]

    fact_id_to_collector_map, aliases_map = build_fact_id_to_collector_map(use_collectors)

    assert fact_id_to_collector_map['collector1'] == [Collector1]
    assert fact_id_to_collect

# Generated at 2022-06-13 00:32:03.873676
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    import pytest

    class CollectorA(BaseFactCollector):
        name = 'A'
        required_facts = set(['B'])

    class CollectorB(BaseFactCollector):
        name = 'B'
        required_facts = set(['C'])

    class CollectorC(BaseFactCollector):
        name = 'C'

    class CollectorD(BaseFactCollector):
        name = 'D'
        required_facts = set(['B', 'E'])
        # NOTE/TODO: unused.
        #        required_facts = set(['B', 'C'])

    class CollectorE(BaseFactCollector):
        name = 'E'
        required_facts = set(['A'])

    class CollectorF(BaseFactCollector):
        name = 'F'


# Generated at 2022-06-13 00:32:14.286628
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    all_fact_subsets = {
        'a': [
            MockCollectorClass(name='a', required_facts=set()),
        ],
        'b': [
            MockCollectorClass(name='b', required_facts=set(['c'])),
        ],
    }
    unresolved = find_unresolved_requires(['a'], all_fact_subsets)
    assert unresolved == set()

    unresolved = find_unresolved_requires(['a', 'b'], all_fact_subsets)
    assert unresolved == set(['c'])

    unresolved = find_unresolved_requires(['b'], all_fact_subsets)
    assert unresolved == set(['c'])

    unresolved = find_unresolved_requires(['c'], all_fact_subsets)

# Generated at 2022-06-13 00:32:15.106236
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    # TODO: assert something here
    pass



# Generated at 2022-06-13 00:32:24.824795
# Unit test for function build_dep_data
def test_build_dep_data():
    from ansible.module_utils.facts.virtual.base import VirtualCollector
    from ansible.module_utils.facts.virtual.openvz import OpenVZCollector
    from ansible.module_utils.facts.virtual.zstack import ZStackCollector
    from ansible.module_utils.facts.virtual.vserver import VServerCollector
    from ansible.module_utils.facts.virtual.vbox import VBoxCollector
    from ansible.module_utils.facts.virtual.vmware import VMWareCollector
    from ansible.module_utils.facts.virtual.xenapi import XenAPICollector
    from ansible.module_utils.facts.virtual.xen import XenCollector
    from ansible.module_utils.facts.virtual.vmware_desktop import VMWareDesktopCollector

# Generated at 2022-06-13 00:32:35.314285
# Unit test for function get_collector_names
def test_get_collector_names():
    result = get_collector_names(minimal_gather_subset={'a', 'b'},
                                 gather_subset=['c', '!d'],
                                 aliases_map={'alias_c': {'c1', 'c2', 'c3'}},
                                 valid_subsets={'c', 'd', 'a', 'b'})
    assert result == {'a', 'b', 'c1', 'c2', 'c3'}  # c is added, d is excluded

# Generated at 2022-06-13 00:32:43.712428
# Unit test for function find_collectors_for_platform
def test_find_collectors_for_platform():
    class TestCollector(BaseFactCollector):
        _platform = 'Linux'
        name = 'test'

    class TestCollector2(BaseFactCollector):
        _platform = 'Linux'
        name = 'test2'

    class TestCollector3(BaseFactCollector):
        _platform = 'Linux'
        name = 'test3'

    all_collector_classes = [TestCollector, TestCollector2, TestCollector3]
    compat_platforms = [platform.linux_distribution()]
    found = find_collectors_for_platform(all_collector_classes, compat_platforms)
    assert found == set([TestCollector, TestCollector2, TestCollector3])



# Generated at 2022-06-13 00:32:51.413287
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    # Collectors: a, b, c, d
    # requires: b requires a, c requires b and d
    # the order could be: a, b, d, c
    # or a, d, b, c

    # when given a, d, b, c, we should get: [] (no errors)
    # when given a, b, d, c, we should get: [c]
    # when given a, c, b, d, we should get: [c, d]
    # when given c, b, c, d, we should get: [a, b, d]

    class CollectA(BaseFactCollector):
        name = 'a'

    class CollectB(BaseFactCollector):
        name = 'b'
        required_facts = set(['a'])


# Generated at 2022-06-13 00:33:01.933569
# Unit test for function find_collectors_for_platform
def test_find_collectors_for_platform():
    # Test with no collectors
    assert len(find_collectors_for_platform(set(), set())) == 0

    # Test with two collectors
    class TestCollector1(object):
        @classmethod
        def platform_match(cls, platform_info):
            return cls

    class TestCollector2(TestCollector1):
        pass

    class TestCollector3(object):
        @classmethod
        def platform_match(cls, platform_info):
            return None
    all_collectors = {TestCollector1, TestCollector2, TestCollector3}
    found_collectors = find_collectors_for_platform(all_collectors, [{}])
    assert found_collectors == all_collectors

    # Test with no platform info
    found_collectors = find_collectors_for_

# Generated at 2022-06-13 00:33:12.385425
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    class C1:
        name = 'one'
        required_facts = set()

    class C2:
        name = 'two'
        required_facts = set(['one'])

    class C3:
        name = 'three'
        required_facts = set()

    class C4:
        name = 'four'
        required_facts = set(['three'])

    class C5:
        name = 'five'
        required_facts = set(['three', 'six'])

    all_fact_subsets = {C1.name: [C1], C2.name: [C2], C3.name: [C3], C4.name: [C4], C5.name: [C5]}

    # only two has unresolved requires

# Generated at 2022-06-13 00:33:41.603149
# Unit test for function select_collector_classes
def test_select_collector_classes():
    '''Unit test for function select_collector_classes'''

    class CollectorA(BaseFactCollector):
        name = 'CollectorA'
        _fact_ids = ('foo', )

    class CollectorB(BaseFactCollector):
        name = 'CollectorB'
        _fact_ids = ('bar', )

    class CollectorD(BaseFactCollector):
        name = 'CollectorD'
        _fact_ids = ('baz', )

    # CollectorC inherits from CollectorA
    class CollectorC(BaseFactCollector):
        name = 'CollectorC'
        _fact_ids = ('baz', )

    class CollectorE(BaseFactCollector):
        name = 'CollectorE'
        # CollectorE is missing from all_fact_subsets
        _fact_ids = ('bing', )

    #

# Generated at 2022-06-13 00:33:51.761466
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    import pytest
    from ansible.module_utils.facts import collector

    @collector('name')
    class CollectorA(BaseFactCollector):
        _fact_ids = ['A']

    @collector('name')
    class CollectorB(BaseFactCollector):
        _fact_ids = ['B']

    @collector('name')
    class CollectorC(BaseFactCollector):
        _fact_ids = ['C']
        required_facts = {'B'}

    @collector('name')
    class CollectorD(BaseFactCollector):
        _fact_ids = ['D']
        required_facts = {'A'}

    @collector('name')
    class CollectorE(BaseFactCollector):
        _fact_ids = ['E']
        required_facts = {'D', 'C'}



# Generated at 2022-06-13 00:33:59.310513
# Unit test for function build_dep_data
def test_build_dep_data():
    import collections
    import pytest
    class FakeDepCollector:
        name = "fake"
        def __init__(self):
            self.required_facts = {}
    class FakeCollector1(FakeDepCollector):
        required_facts = {"test1", "test2"}
    class FakeCollector2(FakeDepCollector):
        required_facts = {"test3"}
    class FakeCollector3(FakeDepCollector):
        required_facts = {"test4"}
    class FakeCollector4(FakeDepCollector):
        required_facts = {"test5"}
    class FakeCollector5(FakeDepCollector):
        required_facts = {"test2", "test3"}

    collector_names = {"test1", "test2", "test3", "test4", "test5"}

# Generated at 2022-06-13 00:34:07.111201
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    collector_names = ['all', 'some', 'none']
    all_fact_subsets = {'some': [MockCollector('some', required_facts=['all'])]}
    result = find_unresolved_requires(collector_names, all_fact_subsets)
    assert result == set()

    collector_names = ['all', 'some', 'none']
    all_fact_subsets = {'some': [MockCollector('some', required_facts=['unexpected'])]}
    result = find_unresolved_requires(collector_names, all_fact_subsets)
    assert result == set(['unexpected'])



# Generated at 2022-06-13 00:34:13.813355
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    all_fact_subsets = {
        'a': [MockCollector(name='a', required_facts=set(['b', 'c']))],
        'b': [MockCollector(name='b', required_facts=set([]))],
        'c': [MockCollector(name='c', required_facts=set(['d', 'e']))],
        'd': [MockCollector(name='d', required_facts=set(['e']))],
        # 'e' doesn't even exist!
    }

    assert find_unresolved_requires(set(['a', 'c']), all_fact_subsets) == set(['e'])

