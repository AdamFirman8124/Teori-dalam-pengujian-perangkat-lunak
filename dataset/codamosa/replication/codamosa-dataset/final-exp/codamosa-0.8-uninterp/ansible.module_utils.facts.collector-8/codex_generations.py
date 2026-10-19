

# Generated at 2022-06-13 00:24:44.243865
# Unit test for function find_collectors_for_platform
def test_find_collectors_for_platform():
    import sys
    import os
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
    from module_utils.facts import collectors

    os_platform = platform.system()
    os_release = platform.release()

    all_collector_classes = collectors.CollectorRegistry().collectors
    compat_platforms = [
        {'system': os_platform, 'release': os_release},
        {'system': 'Generic'},
    ]
    assert (find_collectors_for_platform(all_collector_classes, compat_platforms))



# Generated at 2022-06-13 00:24:55.342691
# Unit test for function select_collector_classes
def test_select_collector_classes():
    from ansible.module_utils.facts.collectors import FacterCollector
    from ansible.module_utils.facts.collectors import DHCPDCollector
    from ansible.module_utils.facts.collectors import LinuxDistributionCollector

    all_fact_subsets = defaultdict(list)
    all_fact_subsets['network'].extend([FacterCollector, DHCPDCollector])
    all_fact_subsets['distribution'].append(LinuxDistributionCollector)

    selected_collector_classes = select_collector_classes(['network', 'distribution'], all_fact_subsets)
    assert len(selected_collector_classes) == 3

    seen_classes = set(selected_collector_classes)

# Generated at 2022-06-13 00:25:01.545857
# Unit test for function select_collector_classes
def test_select_collector_classes():
    from ansible.module_utils.facts._fact_collector import (BaseFactCollector,
                                                            select_collector_classes)

    class A(BaseFactCollector):
        name = 'a'

    class B(BaseFactCollector):
        name = 'b'

    class A2(A):
        name = 'a'

    all_fact_subsets = {
        'a': [A, A2],
        'b': [B],
    }

    assert set(select_collector_classes(['a'], all_fact_subsets)) == set([A, A2])
    assert set(select_collector_classes(['a', 'a'], all_fact_subsets)) == set([A, A2])

# Generated at 2022-06-13 00:25:07.187183
# Unit test for function build_dep_data
def test_build_dep_data():
    collector_names = {'a', 'b', 'c'}
    all_fact_subsets = {'a': [1, 2], 'b': [1, 2], 'c': [2]}
    dep_map = build_dep_data(collector_names, all_fact_subsets)
    assert dep_map == {'a': {'c'}, 'b': {'c'}, 'c': set()}



# Generated at 2022-06-13 00:25:18.646185
# Unit test for function get_collector_names
def test_get_collector_names():
    # Test basic subset inclusion and exclusion.
    assert get_collector_names(valid_subsets=frozenset(['foo', 'bar']),
                               gather_subset=['foo', '!bar']) == {'foo'}
    assert get_collector_names(valid_subsets=frozenset(['foo']),
                               gather_subset=['!foo', 'bar']) == set()

    # Test bad subset exclusion.
    try:
        get_collector_names(valid_subsets=frozenset(['foo']),
                            gather_subset=['!bar'])
    except TypeError:
        pass
    else:
        assert False, "TypeError should have been raised."

    # Test bad subset inclusion.

# Generated at 2022-06-13 00:25:28.620587
# Unit test for function find_collectors_for_platform
def test_find_collectors_for_platform():
    from ansible.module_utils.facts.collector.system import SystemCollector
    from ansible.module_utils.facts.collector.hardware import HardwareCollector
    from ansible.module_utils.facts.collector.network import NetworkCollector

    all_collector_classes = (SystemCollector, HardwareCollector, NetworkCollector)
    compat_platforms = (dict(system='Linux'), )

    assert SystemCollector in find_collectors_for_platform(
        all_collector_classes, compat_platforms)
    assert HardwareCollector in find_collectors_for_platform(
        all_collector_classes, compat_platforms)
    assert NetworkCollector in find_collectors_for_platform(
        all_collector_classes, compat_platforms)



# Generated at 2022-06-13 00:25:40.141270
# Unit test for function build_dep_data
def test_build_dep_data():
    def FakeCollector1():
        class FakeCollector():
            _fact_ids = set()
            required_facts = set()
            name = "FakeCollector1"
        return FakeCollector
    def FakeCollector2():
        class FakeCollector():
            _fact_ids = set()
            required_facts = set()
            name = "FakeCollector2"
        return FakeCollector
    def FakeCollector3():
        class FakeCollector():
            _fact_ids = set()
            required_facts = set()
            name = "FakeCollector3"
        return FakeCollector
    collector_names = {"FakeCollector1", "FakeCollector2"}

# Generated at 2022-06-13 00:25:48.100208
# Unit test for function tsort
def test_tsort():
    def assert_tsort(tsorted, dep_map):
        assert tsort(dep_map) == tsorted

    # A simple test case
    assert_tsort([
        ('a', set(['b'])),
        ('b', set(['c'])),
        ('c', set()),
    ], {
        'a': set(['b']),
        'b': set(['c']),
        'c': set(),
    })

    # Add in a node with no dependencies

# Generated at 2022-06-13 00:25:58.713258
# Unit test for function get_collector_names
def test_get_collector_names():
    # make sure that '!all' gives us what we expect.
    result = get_collector_names(frozenset(["network", "pci"]),
                                 frozenset(["network", "pci"]),
                                 ['!all'],
                                 platform_info=None)
    assert result == frozenset(["network", "pci"]), result
    # make sure that '!all,foo' gives us what we expect.
    result = get_collector_names(frozenset(["network", "pci"]),
                                 frozenset(["network", "pci"]),
                                 ['!all', 'pci'],
                                 platform_info=None)
    assert result == frozenset(["network", "pci"]), result



# Generated at 2022-06-13 00:26:05.888503
# Unit test for function find_collectors_for_platform
def test_find_collectors_for_platform():
    from ansible.module_utils.facts.collector import BaseFactCollector, find_collectors_for_platform

    class CollectorTest(BaseFactCollector):
        _platform = 'Test'
        name = 'test_collector'
        required_facts = set()

        def collect(self, module=None, collected_facts=None):
            return {}

    assert find_collectors_for_platform([CollectorTest], [{'system': 'Test'}]) == set([CollectorTest])



# Generated at 2022-06-13 00:26:22.610074
# Unit test for function build_dep_data
def test_build_dep_data():
    from ansible.module_utils.facts import collector

    collector_names = ['ansible_xxx', 'ansible_yyy']
    all_fact_subsets = {
        'ansible_xxx' : [collector.NetworkCollector],
        'ansible_yyy' : [collector.DistributionCollector],
    }
    expected = defaultdict(set)
    expected.update({
        'ansible_xxx' : {'ansible_distribution_release', 'ansible_distribution',
                         'ansible_distribution_version', 'ansible_os_family'},
        'ansible_yyy' : set()
    })

    dep_map = build_dep_data(collector_names, all_fact_subsets)

    assert expected == dep_map


# Generated at 2022-06-13 00:26:35.094562
# Unit test for function select_collector_classes

# Generated at 2022-06-13 00:26:45.068262
# Unit test for function get_collector_names
def test_get_collector_names():
    # no gather_subset, no minimal set, empty valid set
    assert get_collector_names(platform_info={}) == set()

    # no gather_subset, no minimal set, some valid set
    assert get_collector_names(frozenset(('foo', 'bar')), platform_info={}) == set()

    # no gather_subset, some minimal set, some valid set
    assert get_collector_names(frozenset(('foo', 'bar')), frozenset(('minimal1', 'minimal2')), platform_info={}) == frozenset(('minimal1', 'minimal2'))

    # empty gather_subset, some minimal set, some valid set

# Generated at 2022-06-13 00:26:48.705117
# Unit test for function select_collector_classes
def test_select_collector_classes():
    collector_names = ['local']
    all_fact_subsets = defaultdict(list,{'local':[class_local, class_local]})
    assert(select_collector_classes(collector_names, all_fact_subsets) == [class_local])


# Generated at 2022-06-13 00:26:53.006578
# Unit test for function build_dep_data
def test_build_dep_data():
    class dep_test(BaseFactCollector):
        name = 'test'
        required_facts = ['dep1', 'dep2', 'dep3']

    assert build_dep_data(['test'], {'test': [dep_test]}) == {'test': {'dep1', 'dep2', 'dep3'}}



# Generated at 2022-06-13 00:27:02.541809
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    from ansible.module_utils.facts.collectors.network import NetworkFactCollector
    from ansible.module_utils.facts.collectors.default import DefaultFactCollector

    all_fact_subsets = defaultdict(list)
    all_fact_subsets['foo'].append(DefaultFactCollector)

    # collector_name of 'foo' has no requirements, so no unresolved
    collector_names = ['foo']
    assert not find_unresolved_requires(collector_names, all_fact_subsets)

    # collector_name of 'foo' requires 'bar', so one unresolved
    DefaultFactCollector.required_facts = frozenset(('bar',))
    assert find_unresolved_requires(collector_names, all_fact_subsets) == set(('bar',))



# Generated at 2022-06-13 00:27:12.936192
# Unit test for function find_collectors_for_platform
def test_find_collectors_for_platform():
    '''
    Test for function find_collectors_for_platform

    Unit test for function find_collectors_for_platform
    '''
    from ansible.module_utils.facts import collector

    # this is a list of valid (already loaded) FactCollector classes
    all_collector_classes = [collector.LinuxFactCollector, collector.GenericFactCollector]

    # this is a list of compat platforms (here, just one)
    platform_info = {'system': 'Linux'}
    compat_platforms = [platform_info]

    # this is a list of names of collector classes that are compatible with the platform
    # this should match the output of find_collectors_for_platform(all_collector_classes, compat_platforms)
    expected_output = [collector.LinuxFactCollector]

    # If

# Generated at 2022-06-13 00:27:24.132003
# Unit test for function find_collectors_for_platform
def test_find_collectors_for_platform():
    import ansible.module_utils.facts.collector.base

    # Mock a class that could be returned by find_collectors_for_platform()
    class FakeBaseCollector(BaseFactCollector):
        _fact_ids = set()
        name = 'test'
        required_facts = set()

        @classmethod
        def platform_match(cls, platform_info):
            if platform_info['system'] == 'Linux':
                return cls


    # Mock a class that could be returned by find_collectors_for_platform()
    class FakeBaseCollector2(BaseFactCollector):
        _fact_ids = set()
        name = 'test'
        required_facts = set()


# Generated at 2022-06-13 00:27:32.608097
# Unit test for function find_collectors_for_platform
def test_find_collectors_for_platform():

    # --Mock platform
    class Mock_X86_64(BaseFactCollector):

        # Mock platform based on linux_x86_64_collector
        _platform = 'X86_64'
        name = 'linux'
        required_facts = frozenset(['distribution', 'distribution_version'])

    # --Mock platform
    class Mock_FreeBSD(BaseFactCollector):

        # Mock platform based on linux_x86_64_collector
        _platform = 'FreeBSD'
        name = 'freebsd'
        required_facts = frozenset(['distribution', 'distribution_version'])

    def _test_find_collectors_for_platform(
        all_collector_classes,
        compat_platforms,
        expected_found_collectors
    ):
        assert find_collect

# Generated at 2022-06-13 00:27:45.040652
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    all_fact_subsets = {
        'a': ['a should never be in here'],
        'b': ['b should never be in here'],
    }

    class A:
        name = 'a'
        required_facts = {'b'}

    class B:
        name = 'b'
        required_facts = set()

    all_fact_subsets['a'] = [A]
    all_fact_subsets['b'] = [B]

    assert find_unresolved_requires(['b'], all_fact_subsets) == set()
    assert find_unresolved_requires(['a', 'b'], all_fact_subsets) == set()
    assert find_unresolved_requires(['a'], all_fact_subsets) == {'b'}



# Generated at 2022-06-13 00:28:01.289603
# Unit test for function select_collector_classes
def test_select_collector_classes():
    # Define some test objects
    class Collector1(BaseFactCollector):
        name = 'collector1'
    class Collector2(BaseFactCollector):
        name = 'collector2'
    class Collector4(BaseFactCollector):
        name = 'collector4'
    class CollectorAlias(BaseFactCollector):
        name = 'collectoralias'
        _fact_ids = set(['collector1'])

    # Define some test data
    selected_collector_names = ['collector2', 'collectoralias', 'collector1']
    all_fact_subsets = dict(
        collector1=[Collector1, CollectorAlias],
        collector2=[Collector2, CollectorAlias],
        collector4=[Collector4, CollectorAlias]
    )
    selected_collector_classes = select_collector_classes

# Generated at 2022-06-13 00:28:11.253776
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    all_fact_subsets = dict(
        foo=set([
            object(),
            object()]),
        bar=set([
            object(),
            object()]))
    assert find_unresolved_requires(['foo'], all_fact_subsets) == set()
    assert find_unresolved_requires(['bar'], all_fact_subsets) == set()
    assert find_unresolved_requires(['baz'], all_fact_subsets) == set(['baz'])

    # now test one where the collector requires something
    class foo(object):
        required_facts = set(['bar'])
    class bar(object):
        required_facts = set()
    class baz(object):
        required_facts = set(['bar'])

# Generated at 2022-06-13 00:28:22.512132
# Unit test for function tsort
def test_tsort():
    # Test one-level
    dep_map = {'a': set(), 'b': set(), 'c': set()}
    assert tsort(dep_map) == [('a', set()), ('b', set()), ('c', set())]

    # Test two-level
    dep_map = {'a': set(['b']), 'b': set()}
    assert tsort(dep_map) == [('b', set()), ('a', set(['b']))]

    # Test three-level
    dep_map = {'a': set(['c']), 'b': set(['c']), 'c': set()}
    assert tsort(dep_map) == [('c', set()), ('a', set(['c'])), ('b', set(['c']))]

    # Test cycle
   

# Generated at 2022-06-13 00:28:31.564497
# Unit test for function tsort
def test_tsort():
    # Test case taken from https://en.wikipedia.org/wiki/Topological_sorting
    dep_map = {
        7: [11, 8],
        5: [11, 2],
        3: [8, 10],
        11: [2, 9, 10],
        8: [9],
        2: [],
        9: [],
        10: [],
    }

    sorted_list = tsort(dep_map)
    sorted_keys = [x[0] for x in sorted_list]
    correct_order = [2, 9, 10, 3, 8, 11, 7, 5]
    assert correct_order == sorted_keys



# Generated at 2022-06-13 00:28:41.040883
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    '''Test find_unresolved_requires logic'''
    from collections import defaultdict
    from ansible.module_utils.facts.collector.system.distribution import DistributionFactCollector

    all_fact_subsets = defaultdict(list)
    all_fact_subsets['dmi'].append(DistributionFactCollector)

    collector_names = ['dmi']

    unresolved = find_unresolved_requires(collector_names, all_fact_subsets)
    assert not unresolved

    collector_names.append('unknown')
    unresolved = find_unresolved_requires(collector_names, all_fact_subsets)
    assert unresolved == set(['unknown'])

    collector_names.remove('unknown')
    collector_names.append('lsb')

# Generated at 2022-06-13 00:28:41.930090
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    pass



# Generated at 2022-06-13 00:28:53.691903
# Unit test for function find_collectors_for_platform
def test_find_collectors_for_platform():
    class A(BaseFactCollector):
        _fact_ids = set(('a', 'b'))
        name = 'a'

    class B(BaseFactCollector):
        _fact_ids = set(('b', 'c'))
        name = 'b'
        _platform = 'Linux'

    class C(BaseFactCollector):
        _fact_ids = set(('c', 'd'))
        name = 'c'
        _platform = 'Linux'

    class D(BaseFactCollector):
        _fact_ids = set(('d',))
        name = 'd'
        _platform = 'FreeBSD'

    all_collectors = [A, B, C, D]


# Generated at 2022-06-13 00:29:03.540646
# Unit test for function find_collectors_for_platform
def test_find_collectors_for_platform():
    class A(BaseFactCollector):
        _platform = 'A'
        name = 'a'
    class B(BaseFactCollector):
        _platform = 'B'
        name = 'b'
    class C(BaseFactCollector):
        _platform = 'C'
        name = 'c'

    assert not find_collectors_for_platform(
        [A,B,C],
        [])
    assert not find_collectors_for_platform(
        [A,B,C],
        [{'system': 'E'}])

    # no match
    assert not find_collectors_for_platform(
        [A,B,C],
        [{'system': 'E'}])

    # direct match

# Generated at 2022-06-13 00:29:13.276053
# Unit test for function find_collectors_for_platform
def test_find_collectors_for_platform():
    class TestCollector(BaseFactCollector):
        _fact_ids = set()
        _platform = 'Linux'
        name = None
        required_facts = set()

        @classmethod
        def platform_match(cls, platform_info):
            if platform_info.get('system', None) == cls._platform:
                return cls
            return None

    class TestCollector2(TestCollector):
        _platform = 'Windows'

    class TestCollector3(TestCollector):
        _platform = 'Generic'

    test_platforms = [
        {'system': 'Linux'},
        {'system': 'Windows'}
    ]
    test_collectors = [TestCollector, TestCollector2, TestCollector3]
    expected_result = [TestCollector, TestCollector2]
   

# Generated at 2022-06-13 00:29:20.623489
# Unit test for function build_dep_data
def test_build_dep_data():
    # Case 1: collector_names = ['foo', 'bar'], dep_map should be {'bar': set(), 'foo': set('bar')}
    collector_classes = [FakeCollector1, FakeCollector2]
    collector_names = ['foo', 'bar']
    dep_map = build_dep_data(collector_names, collector_classes)
    assert dep_map == {'bar': set(), 'foo': set(['bar'])}

    # Case 2: collector_names = ['foo', 'bar', 'baz'], dep_map should be {'bar': set(), 'baz': set(), 'foo': set(['bar'])}
    collector_classes = [FakeCollector1, FakeCollector2, FakeCollector3]
    collector_names = ['foo', 'bar', 'baz']
    dep_map

# Generated at 2022-06-13 00:29:44.308249
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    collector_names = ['a', 'b', 'c']
    all_fact_subsets = {'a': [], 'b': [], 'c': []}

    class A:
        name = 'a'
        required_facts = set()

    class B:
        name = 'b'
        required_facts = set()

    class C:
        name = 'c'
        required_facts = {'a'}

    class D:
        name = 'd'
        required_facts = set()

    for klass in (A, B, C, D):
        all_fact_subsets[klass.name].append(klass)

    assert find_unresolved_requires(collector_names, all_fact_subsets) == set()

    collector_names.append('d')
    assert find_unres

# Generated at 2022-06-13 00:29:55.540724
# Unit test for function find_collectors_for_platform
def test_find_collectors_for_platform():
    from .sunos import SunOSFactCollector
    from .linux import LinuxFactCollector
    from .bsd import BSDFactCollector
    from .generic_bsd import GenericBSDFactCollector
    from .generic_linux import GenericLinuxFactCollector
    from .generic_sunos import GenericSunOSFactCollector
    from ansible.module_utils.facts.collector import get_collector_platforms
    from ansible.module_utils.facts.collector import CollectorNamespace

    all_collector_classes = [
        SunOSFactCollector,
        LinuxFactCollector,
        BSDFactCollector,
        GenericBSDFactCollector,
        GenericLinuxFactCollector,
        GenericSunOSFactCollector,
    ]
    found_collectors = set()
    found_collectors_names = set()



# Generated at 2022-06-13 00:30:01.730054
# Unit test for function find_collectors_for_platform
def test_find_collectors_for_platform():
    all_collector_classes = [
        FakeCollectorA,
        FakeCollectorB,
        FakeCollectorC
    ]

    # test negative case
    assert not find_collectors_for_platform(all_collector_classes, [{'os_family': 'NonOS'}])

    # test positive case
    for compat_platform in [{'os_family': 'AIX'}, {'os_family': 'DB2'}]:
        found = find_collectors_for_platform(all_collector_classes, [compat_platform])
        assert len(found) == 1
        assert FakeCollectorB in found



# Generated at 2022-06-13 00:30:14.409553
# Unit test for function find_collectors_for_platform
def test_find_collectors_for_platform():
    class DummyCollector(BaseFactCollector):
        name = 'dummy'
        _fact_ids = set()
        _platform = 'Generic'
        required_facts = set()

    class LinuxCollector(BaseFactCollector):
        name = 'linux'
        _fact_ids = set()
        _platform = 'Linux'
        required_facts = set()

    class RedHatCollector(BaseFactCollector):
        name = 'redhat'
        _fact_ids = set()
        _platform = 'RedHat'
        required_facts = set()

    all_collectors = [DummyCollector, LinuxCollector]
    assert find_collectors_for_platform(all_collectors, [{'system': 'Linux'}]) == {LinuxCollector}
    # When platform does not match any known collector, an

# Generated at 2022-06-13 00:30:25.312734
# Unit test for function find_collectors_for_platform

# Generated at 2022-06-13 00:30:35.222158
# Unit test for function find_collectors_for_platform
def test_find_collectors_for_platform():
    class Collector1(BaseFactCollector):
        _fact_ids = set(['collector1_1', 'collector1_2'])
        required_facts = set()

        def collect(self, module=None, collected_facts=None):
            pass

        @classmethod
        def platform_match(cls, platform_info):
            if platform_info['system'] == 'Linux' and platform_info['distribution'] == 'CentOS':
                return cls
            return None

    class Collector2(BaseFactCollector):
        _fact_ids = set(['collector2_1', 'collector2_2'])
        required_facts = set()

        def collect(self, module=None, collected_facts=None):
            pass


# Generated at 2022-06-13 00:30:46.427726
# Unit test for function build_dep_data
def test_build_dep_data():
    dep_map = {
        'base': set([]),
        'dns': set([]),
        'distribution': set(['base', 'dns']),
        'pkg_mgr': set(['base']),
        'virtualization': set(['pkg_mgr', 'distribution']),
        'network': set(['pkg_mgr', 'distribution']),
        'all': set(['network', 'virtualization'])}
    assert dep_map == build_dep_data(dep_map.keys(), dep_map)
    assert {'base': set()} == build_dep_data(['base'], dep_map)
    assert {'network': set(['base', 'dns', 'pkg_mgr', 'distribution'])} == build_dep_data(['network'], dep_map)

# Generated at 2022-06-13 00:30:56.371083
# Unit test for function select_collector_classes
def test_select_collector_classes():
    # Test that select_collector_classes works correctly with a single collector
    collector_names = ['network']
    all_fact_subsets = {'network': [1]}

    assert select_collector_classes(collector_names, all_fact_subsets) == [1]

    # Test that select_collector_classes works correctly with multiple collectors
    collector_names = ['network', 'network']
    all_fact_subsets = {'network': [1, 2]}

    assert select_collector_classes(collector_names, all_fact_subsets) == [1, 2]

    # Test that select_collector_classes works correctly with a single collector and an
    # unexpected collector that should be ignored
    collector_names = ['network', 'hardware']
    all_fact_subsets = {'network': [1]}



# Generated at 2022-06-13 00:31:07.891921
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    all_fact_subsets = defaultdict(list)
    class MyCollector():
        required_facts = set()
        name = 'my_collector'

    class OtherCollector():
        required_facts = set()
        name = 'other_collector'
    class BadCollector():
        required_facts = set(['bad_fact'])
        name = 'bad_collector'
    all_fact_subsets['my_collector'].append(MyCollector)
    all_fact_subsets['other_collector'].append(OtherCollector)
    all_fact_subsets['bad_collector'].append(BadCollector)
    collector_names = ['bad_collector']
    unresolved = find_unresolved_requires(collector_names, all_fact_subsets)
    # we do not

# Generated at 2022-06-13 00:31:15.669987
# Unit test for function build_dep_data
def test_build_dep_data():
    import unittest
    import collections
    class fakeclass:
        def __init__(self, name, required_facts):
            self.name = name
            self.required_facts = set(required_facts)
    class fakeplatform:
        def __init__(self, system, arch, release):
            self.system = system
            self.arch = arch
            self.release = release
    collectors = [fakeclass('fake1', ['fake4', 'fake2']),
                  fakeclass('fake2', ['fake4', 'fake3']),
                  fakeclass('fake3', []),
                  fakeclass('fake4', ['fake3'])]

# Generated at 2022-06-13 00:31:32.234243
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    class A(BaseFactCollector):
        name = 'A'
        required_facts = {'B'}

    class B(BaseFactCollector):
        name = 'B'

    class C(BaseFactCollector):
        name = 'C'
        required_facts = {'D'}

    all_fact_subsets = {
        'A': [A],
        'B': [B],
        'C': [C],
    }

    assert find_unresolved_requires(['C'], all_fact_subsets)



# Generated at 2022-06-13 00:31:44.146001
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    valid_subsets = frozenset(['min'])
    minimal_gather_subset = frozenset(['all'])
    gather_subset = ['all']
    aliases_map = defaultdict(set)

    # define a fake collector and valid Collector
    class FakeCollectorClass(BaseFactCollector):
        _fact_ids = set(['fakefact1', 'fakefact2'])

        _platform = 'Generic'
        name = 'fakecollector'
        required_facts = set()

        def collect(self, module=None, collected_facts=None):
            return dict()

    class ValidCollectorClass(FakeCollectorClass):
        _platform = 'Linux'

    all_collector_classes = [FakeCollectorClass, ValidCollectorClass]
    compat_platform = {'system': "Linux"}

   

# Generated at 2022-06-13 00:31:55.555803
# Unit test for function find_unresolved_requires

# Generated at 2022-06-13 00:32:05.942683
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    class SomeCollector(BaseFactCollector):
        name = 'some_collector'
        required_facts = frozenset(['some_req'])

    class SomeReqCollector(BaseFactCollector):
        name = 'some_req'

    all_fact_subsets = defaultdict(list)
    all_fact_subsets['some_collector'].append(SomeCollector)
    all_fact_subsets['some_req'].append(SomeReqCollector)

    unresolved = find_unresolved_requires(['some_collector'], all_fact_subsets)
    assert unresolved == {'some_req'}, "Incorrect unresolved: %s" % unresolved

    unresolved = find_unresolved_requires(['some_req'], all_fact_subsets)
    assert len(unresolved)

# Generated at 2022-06-13 00:32:16.054333
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    c1 = BaseFactCollector()
    c1._fact_ids = set(('c1', 'alias'))
    c1.name = 'c1'

    c2 = BaseFactCollector()
    c2._fact_ids = set(('c2', 'alias'))
    c2.name = 'c2'

    c3 = BaseFactCollector()
    c3._fact_ids = set(('c2', 'alias'))
    c3.name = 'c3'

    rv = build_fact_id_to_collector_map(set((c1, c2, c3)))

    assert rv[0]['c1'][0] is c1
    assert rv[0]['c2'][0] is c2
    assert rv[0]['c3'][0]

# Generated at 2022-06-13 00:32:25.742107
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():

    class CollectorA(BaseFactCollector):
        name = 'a'
        _fact_ids = set(['id_a', 'id_b'])

    class CollectorB(BaseFactCollector):
        name = 'b'
        _fact_ids = set(['id_b', 'id_c'])

    class CollectorC(BaseFactCollector):
        name = 'c'
        _fact_ids = set(['id_d'])

    collector_list = [CollectorA, CollectorB, CollectorC]
    fact_id_to_collector_map, aliases_map = build_fact_id_to_collector_map(collector_list)


# Generated at 2022-06-13 00:32:35.551435
# Unit test for function build_dep_data
def test_build_dep_data():
    from ansible.module_utils.facts.network.hp_comware import HpComware

    # Test case 1
    HpComware.required_facts = set(['kernel'])
    collector_names = set(['kernel', 'hp_comware'])
    all_fact_subsets = {
        'kernel': [HpComware],
        'hp_comware': [HpComware]
    }
    expected_dep_map = {
        'kernel': set(),
        'hp_comware': set(['kernel'])
    }
    dep_map = build_dep_data(collector_names, all_fact_subsets)
    assert expected_dep_map == dep_map
    print('test_build_dep_data: [1] passed')



# Generated at 2022-06-13 00:32:44.908348
# Unit test for function build_dep_data
def test_build_dep_data():
    from ansible.module_utils.facts.collector.default import DefaultFactCollector
    from ansible.module_utils.facts.collector.network import NetworkFactCollector
    from ansible.module_utils.facts.collector.hardware import HardwareFactCollector
    from ansible.module_utils.facts.collector.filesystem import FileSystemFactCollector

    collectors = [DefaultFactCollector, NetworkFactCollector, HardwareFactCollector, FileSystemFactCollector]
    fact_ids = ('all', 'hardware', 'network', 'filesystem')
    fact_id_to_collector_map, aliases_map = build_fact_id_to_collector_map(collectors)
    all_fact_subsets = fact_id_to_collector_map

# Generated at 2022-06-13 00:32:52.174208
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    # Add collector_classes to test
    class CollectorA(BaseFactCollector):
        _fact_ids = ['a', 'b']
        name = 'a'
        required_facts = set()

    class CollectorB(BaseFactCollector):
        _fact_ids = ['b', 'c']
        name = 'b'
        required_facts = {'a', 'c'}

    class CollectorC(BaseFactCollector):
        _fact_ids = ['c']
        name = 'c'
        required_facts = set()

    # Create all_fact_subsets
    all_fact_subsets = {}
    for collector_class in [CollectorA, CollectorB, CollectorC]:
        all_fact_subsets[collector_class.name] = [collector_class]

    # Test find_unresolved_

# Generated at 2022-06-13 00:33:02.338368
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    from ansible.module_utils.facts.collector.hardware import Hardware
    from ansible.module_utils.facts.collector.lspci import Lspci
    from ansible.module_utils.facts.collector.network import Network

    # test with 2 different collectors, one w/o alias, one w/ alias
    collectors = [Network, Hardware, Lspci]
    fact_map, aliases_map = build_fact_id_to_collector_map(collectors)

# Generated at 2022-06-13 00:33:23.012880
# Unit test for function find_collectors_for_platform
def test_find_collectors_for_platform():
    assert find_collectors_for_platform([], []) == set()



# Generated at 2022-06-13 00:33:32.472767
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    # mock a Collector
    class Collector1(BaseFactCollector):
        _fact_ids = set()
        required_facts = set()
        name = 'collector1'
    # mock a Collector
    class Collector2(BaseFactCollector):
        _fact_ids = set(['collector2'])
        required_facts = set()
        name = 'collector2'
    # mock a Collector
    class Collector3(BaseFactCollector):
        _fact_ids = set(['collector3a', 'collector3b'])
        required_facts = set()
        name = 'collector3'
    # mock a Collector
    class Collector4(BaseFactCollector):
        _fact_ids = set(['collector1'])
        required_facts = set(['collector2'])

# Generated at 2022-06-13 00:33:40.257342
# Unit test for function build_dep_data
def test_build_dep_data():
    assert(build_dep_data(['collector1'], {'collector1': [base]}) ==
           {'collector1': {'dep1', 'dep2'}})
    assert(build_dep_data(['collector1', 'collector2'],
                          {'collector1': [base], 'collector2': [sub]}) ==
           {'collector1': {'dep1', 'dep2'},
            'collector2': {'dep1', 'dep2', 'dep3'}})



# Generated at 2022-06-13 00:33:47.410106
# Unit test for function get_collector_names
def test_get_collector_names():
    fake_platform_info = {'system': 'Linux'}
    aliases_map = defaultdict(set)
    aliases_map.update({'os': {'distribution'}})
    valid_subsets = frozenset({'os', 'distribution'})
    assert get_collector_names(valid_subsets=valid_subsets,
                               aliases_map=aliases_map,
                               platform_info=fake_platform_info,
                               gather_subset=['os']) == {'os', 'distribution'}

    assert get_collector_names(valid_subsets=valid_subsets,
                               aliases_map=aliases_map,
                               platform_info=fake_platform_info,
                               gather_subset=['!os']) == {'os', 'distribution'}



# Generated at 2022-06-13 00:33:55.449311
# Unit test for function build_dep_data
def test_build_dep_data():
  from collections import namedtuple
  class CollectorBaseA(BaseFactCollector):
      _fact_ids = ['a']
      require_facts = set()
      name = 'a'
  class CollectorBaseB(BaseFactCollector):
      _fact_ids = ['b']
      require_facts = set()
      name = 'b'

  # Named tuple FactSubset
  FactSubset = namedtuple('FactSubset', ('collector_classes', 'dep_map'))
  # Fact subset
  fact_subsets = FactSubset([CollectorBaseA,CollectorBaseB], build_dep_data(['a', 'b'], {}))
  # List of collector names
  collector_names = ['a','b']
  # Function to test

# Generated at 2022-06-13 00:34:01.630335
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():

    class Garbage(BaseFactCollector):
        '''A mock fact collector for testing
        '''
        # pylint: disable=too-few-public-methods
        # pylint: disable=no-self-use
        name = 'garbage'

    class Air(BaseFactCollector):
        '''A mock fact collector for testing
        '''
        # pylint: disable=too-few-public-methods
        # pylint: disable=no-self-use
        name = 'air'

    class Single(BaseFactCollector):
        '''A mock fact collector for testing
        '''
        required_facts = frozenset(('garbage', 'air'))
        # pylint: disable=too-few-public-methods
        # pylint: disable=no-self-use


# Generated at 2022-06-13 00:34:09.412993
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    import ansible.module_utils.facts.collectors

    # one class that returns only the fact it is named for
    class ACollector(BaseFactCollector):
        name = 'a'
        _fact_ids = {'a'}

    # one class that returns ['a', 'b']
    class BCollector(BaseFactCollector):
        name = 'b'
        _fact_ids = {'a', 'b'}

    # 'c' collector has no aliases to other facts
    class CCollector(BaseFactCollector):
        name = 'c'
        _fact_ids = set()

    all_collector_classes = [ACollector, BCollector, CCollector]