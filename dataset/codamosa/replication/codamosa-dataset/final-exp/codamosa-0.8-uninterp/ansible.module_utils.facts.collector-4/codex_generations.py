

# Generated at 2022-06-13 00:24:28.171751
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    # test for case where no requires are unresolved

    valid_subsets = frozenset(['min', 'all', 'os', 'hardware', 'devices', 'virtual'])

    minimal_gather_subset = frozenset(['min', 'hardware'])

    # NOTE: the order of 'hardware', 'virtual' is important here.
    #       'virtual' requires 'hardware'
    gather_subset = ['os', 'hardware', 'virtual']

    collector_names = get_collector_names(valid_subsets=valid_subsets,
                                          minimal_gather_subset=minimal_gather_subset,
                                          gather_subset=gather_subset)


# Generated at 2022-06-13 00:24:34.934721
# Unit test for function tsort
def test_tsort():
    dep_map = {
        'a': set(),
        'b': set(['c']),
        'c': set(['a']),
        }
    sorted_list = [
        ('a', ()),
        ('c', ('a',)),
        ('b', ('c',))
        ]
    assert tsort(dep_map) == sorted_list

    dep_map = {
        'a': set(['b']),
        'b': set(['a']),
        }
    try:
        tsort(dep_map)
        assert False
    except CycleFoundInFactDeps:
        pass



# Generated at 2022-06-13 00:24:44.512476
# Unit test for function tsort
def test_tsort():
    testmap = {
        'a': set(['b']),
        'b': set(['c']),
        'c': set(['a'])
    }
    import pytest
    with pytest.raises(CycleFoundInFactDeps):
        tsort(testmap)

    testmap = {
        'a': set(['b', 'c']),
        'b': set(['c']),
        'c': set()
    }
    result = tsort(testmap)
    assert set(testmap.keys()) == set([a for a, b in result])
    result_set = set(result)
    assert ('a', set(['b', 'c'])) in result_set
    assert ('b', set(['c'])) in result_set
    assert ('c', set()) in result_

# Generated at 2022-06-13 00:24:54.514375
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    all_fact_subsets = {}
    collector_names = ['a', 'b', 'c']

    def _new_mock(name, requires=()):
        class MockCollector:
            pass

        mock = MockCollector()
        mock.name = name
        mock.required_facts = set(requires)
        all_fact_subsets[mock.name] = [mock]
        return mock

    _new_mock('a')
    _new_mock('b', requires=['c'])
    _new_mock('c')

    assert find_unresolved_requires(collector_names, all_fact_subsets) == set(['c'])



# Generated at 2022-06-13 00:25:00.626595
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    all_fact_subsets = {
        'collector_a': [object],
        'collector_b': [object],
        'collector_c': [object],
        'collector_d': [object]
    }
    class CollectorA:
        name = 'collector_a'
        required_facts = set()

    class CollectorB:
        name = 'collector_b'
        required_facts = {'collector_c'}

    class CollectorC:
        name = 'collector_c'
        required_facts = {'collector_d'}

    class CollectorD:
        name = 'collector_d'
        required_facts = {'collector_a'}

    all_fact_subsets['collector_a'] = [CollectorA, ]
    all_fact_subsets

# Generated at 2022-06-13 00:25:09.432023
# Unit test for function get_collector_names
def test_get_collector_names():
    assert get_collector_names(valid_subsets=frozenset(['a', 'b', 'c']), minimal_gather_subset=frozenset(['a']),
                               gather_subset=['a', 'b']) == set(['a', 'b'])
    assert get_collector_names(valid_subsets=frozenset(['a', 'b', 'c']), minimal_gather_subset=frozenset(['a']),
                               gather_subset=['!a', '!b']) == set(['c'])

# Generated at 2022-06-13 00:25:19.828928
# Unit test for function find_unresolved_requires

# Generated at 2022-06-13 00:25:27.230878
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    all_fact_subsets = {'a': ['A'], 'b': ['B'], 'c': ['C'], 'd': ['D']}
    assert len(find_unresolved_requires(['a', 'b', 'c'], all_fact_subsets)) == 0
    assert len(find_unresolved_requires(['a', 'b', 'c', 'd'], all_fact_subsets)) == 0
    assert len(find_unresolved_requires(['a', 'b', 'c', 'd', 'x'], all_fact_subsets)) == 1


# Generated at 2022-06-13 00:25:35.711910
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    find_unresolved_requires_test = find_unresolved_requires(['a', 'b', 'c'], {'a': [], 'b': [], 'c': [], 'd': []})
    assert find_unresolved_requires_test == set()
    find_unresolved_requires_test2 = find_unresolved_requires(['a', 'b', 'c'], {'a': [], 'b': [], 'd': []})
    assert find_unresolved_requires_test2 == set(['c'])



# Generated at 2022-06-13 00:25:45.213339
# Unit test for function get_collector_names
def test_get_collector_names():
    # test that get_collector_names works for 'all'
    subset = get_collector_names(valid_subsets=['network', 'hardware', 'software'])
    assert isinstance(subset, set)
    assert 'network' in subset
    assert 'hardware' in subset
    assert 'software' in subset

    # test that get_collector_names works fro '!all'
    subset = get_collector_names(valid_subsets=['network', 'hardware', 'software'],
                                 gather_subset=['!all'])
    assert isinstance(subset, set)
    assert 'network' not in subset
    assert 'hardware' not in subset
    assert 'software' not in subset

    # test that get_collector_names raises errors when a bad subset is encountered

# Generated at 2022-06-13 00:26:00.282703
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    from ansible_collections.ansible.community.plugins.module_utils.facts.collectors import all_collector_classes
    all_fact_subsets = {
        'all': all_collector_classes,
        'something': [],
        'test': [],
        'bad': [],
        'test_1': [],
        'test_2': [],
    }
    class _TestCollector1(BaseFactCollector):
        name = 'test_1'
        required_facts = ['something']
    class _TestCollector2(BaseFactCollector):
        name = 'test_2'
        required_facts = ['something', 'bad']
    all_fact_subsets['test_1'] = [_TestCollector1]

# Generated at 2022-06-13 00:26:09.821283
# Unit test for function get_collector_names
def test_get_collector_names():
    # Basic gather_subset='all'
    collector_names = get_collector_names(
        valid_subsets=frozenset(['all', 'network', 'hardware']),
        minimal_gather_subset=frozenset(['network']),
        gather_subset=['all'],
        aliases_map=defaultdict(set))
    assert collector_names == frozenset(['network', 'hardware'])

    # Basic gather_subset=['network']
    collector_names = get_collector_names(
        valid_subsets=frozenset(['all', 'network', 'hardware']),
        minimal_gather_subset=frozenset(['network']),
        gather_subset=['network'],
        aliases_map=defaultdict(set))
    assert collector

# Generated at 2022-06-13 00:26:17.914453
# Unit test for function select_collector_classes
def test_select_collector_classes():
    collector_list = ['test1', 'test2', 'test3']
    test_collector_list = [['test1'], ['test2', 'test3']]
    test_map = dict(zip(collector_list, test_collector_list))
    result = select_collector_classes(collector_list, test_map)
    assert(len(result) == 3)
    assert(result[0] == 'test1')
    assert(result[1] == 'test2')
    assert(result[2] == 'test3')



# Generated at 2022-06-13 00:26:25.431398
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    '''Test the find_unresolved_requires function'''

    # all_fact_subsets is a list of sets, a set for each fact_subset name.
    # each set contains the names of FactCollectors (fact sets) that are part of that fact_subset
    # for example, all_fact_subsets['networking'] = ['facts.networking.interfaces', 'facts.networking.routes']

# Generated at 2022-06-13 00:26:37.018469
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    all_fact_subsets = {
        'a': [A],
        'b': [B],
        'c': [C],
        'd': [D],
        'e': [E],
    }

    # No unresolved
    # a -> b -> c
    # d -> b -> c
    # d -> e
    collector_names = set(['a', 'b', 'c', 'd', 'e'])
    assert find_unresolved_requires(collector_names, all_fact_subsets) == set()

    # Unresolved
    # a -> b -> c
    # d -> b -> c
    # d -> e
    collector_names = set(['a', 'b', 'c', 'd'])

# Generated at 2022-06-13 00:26:45.879675
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    from ansible.module_utils.facts.collectors.network import NetworkFactCollector

    collector_name = 'network'
    all_fact_subsets = {
        'all': set(),
        collector_name: set([NetworkFactCollector]),
    }

    assert find_unresolved_requires([collector_name], all_fact_subsets) == set()
    assert find_unresolved_requires(['network', 'all'], all_fact_subsets) == set()

    all_fact_subsets[collector_name].clear()
    NetworkFactCollector.required_facts |= frozenset(['network'])

    # In this case we would be asking for 'network' again, and that
    # would cause a circular dependency.

# Generated at 2022-06-13 00:26:55.018225
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    # This dict will be used as all_fact_subsets
    fake_fact_subsets = {
        'system': [SystemCollector],
        'distribution': [DistributionCollector],
    }
    collector_names = ['system']
    unresolved_requires = find_unresolved_requires(collector_names, fake_fact_subsets)
    assert unresolved_requires == set(['distribution'])
    collector_names = ['distribution']
    unresolved_requires = find_unresolved_requires(collector_names, fake_fact_subsets)
    assert unresolved_requires == set([])
    collector_names = ['system', 'distribution']
    unresolved_requires = find_unresolved_requires(collector_names, fake_fact_subsets)
    assert unresolved_requires == set([])



# Generated at 2022-06-13 00:27:03.483474
# Unit test for function find_collectors_for_platform
def test_find_collectors_for_platform():
    import ansible.module_utils.facts.collectors.hardware
    import ansible.module_utils.facts.collectors.redhat.processor
    import ansible.module_utils.facts.collectors.generic.architecture

    all_collector_classes = [getattr(ansible.module_utils.facts.collectors.hardware, attr)
                             for attr in dir(ansible.module_utils.facts.collectors.hardware)
                             if attr.endswith('HardwareCollector')]

# Generated at 2022-06-13 00:27:13.618452
# Unit test for function build_dep_data
def test_build_dep_data():
    from ansible.module_utils.facts.system.distribution import DistributionFactCollector
    from ansible.module_utils.facts.system.pkg_mgr import PkgMgrFactCollector
    from ansible.module_utils.facts.collector import BaseFactCollector

    class A(BaseFactCollector):
        _fact_ids = set()
        name = 'A'
        required_facts = set(['B'])

    class B(BaseFactCollector):
        _fact_ids = set()
        name = 'B'
        required_facts = set(['C'])

    class C(BaseFactCollector):
        _fact_ids = set()
        name = 'C'
        required_facts = set()


# Generated at 2022-06-13 00:27:24.922251
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    # Setup
    class Dummy:
        pass
    all_fact_subsets = {
        'all': [
            Dummy(),
            Dummy(),
            Dummy()
        ],
        'one': [
            Dummy(),
            Dummy()
        ],
        'two': [
            Dummy()
        ],
        'three': [
            Dummy()
        ],
        'four': [
            Dummy()
        ],
        'five': [
            Dummy(),
            Dummy()
        ]
    }
    all_fact_subsets['all'][0].required_facts = {"one", "two", "five"}
    all_fact_subsets['all'][1].required_facts = {"three"}
    all_fact_subsets['all'][2].required_facts = {"four"}


# Generated at 2022-06-13 00:27:41.682942
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    from collections import defaultdict

    class Collector1(BaseFactCollector):
        name = "Collector1"
        _fact_ids = {"primary_name"}

    class Collector2(BaseFactCollector):
        name = "Collector2"
        _fact_ids = {"dependent_fact_id"}
        required_facts = {'dependent_fact'}

    class Collector3(BaseFactCollector):
        name = "Collector3"

    class Collector4(BaseFactCollector):
        name = "Collector4"
        _fact_ids = {"fact_id_1", "fact_id_2"}


# Generated at 2022-06-13 00:27:52.927630
# Unit test for function get_collector_names
def test_get_collector_names():
    # the set of all things we have
    valid_subsets = frozenset(('min', 'a', 'b', 'c', 'd', 'e'))
    min_subsets = frozenset(('a',))
    # NOTE: aliases_map is only used for expanding the requested set by adding
    #       aliases, not for removing the aliases from the final result
    aliases_map = defaultdict(set,
                              hw=frozenset(('a', 'b')),
                              nw=frozenset(('c', 'd')),
                              )

    gather_subset = ['all']

# Generated at 2022-06-13 00:27:59.693313
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    class MyCollector(BaseFactCollector):
        name = 'my'
        _fact_ids = set(['my_fact'])

    class MyOtherCollector(BaseFactCollector):
        name = 'my_other'
        _fact_ids = set(['my_other_fact'])

    class DuplicateCollector(BaseFactCollector):
        name = 'dup'
        _fact_ids = set(['dup', 'dup_alt'])
    # end unit test

    fact_id_to_collector_map, aliases_map = build_fact_id_to_collector_map([
        MyCollector,
        MyOtherCollector,
        DuplicateCollector
    ])

    assert fact_id_to_collector_map['my'][0] == MyCollector
    assert fact_

# Generated at 2022-06-13 00:28:08.493318
# Unit test for function get_collector_names
def test_get_collector_names():

    # only suppress deprecation warning for unittest of deprecated function
    # pylint: disable=deprecated-method

    # Success case - multiple modules
    modules = ['network', 'hardware']
    valid_subsets = ['network', 'hardware']
    fact_names = get_collector_names(gather_subset=modules, valid_subsets=valid_subsets)
    assert fact_names == {'network', 'hardware'}

    # Success case - multiple modules, with min subset
    modules = ['network', 'hardware']
    valid_subsets = ['network', 'hardware']
    minimal_gather_subset = ['network']

# Generated at 2022-06-13 00:28:20.027748
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    class E(BaseFactCollector):
        name = 'E'
        required_facts = set()

    class D(BaseFactCollector):
        name = 'D'
        required_facts = set(['E'])

    class C(BaseFactCollector):
        name = 'C'
        required_facts = set(['D', 'E'])

    class B(BaseFactCollector):
        name = 'B'
        required_facts = set()

    class A(BaseFactCollector):
        name = 'A'
        required_facts = set(['C', 'B'])

    class X(BaseFactCollector):
        name = 'X'
        required_facts = set(['Y'])

    class Y(BaseFactCollector):
        name = 'Y'

# Generated at 2022-06-13 00:28:30.504763
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    class TestCollector(BaseFactCollector):
        name = 'test'
        _fact_ids = set(('test1','test2','test3','test4'))

    class TestCollector2(TestCollector):
        name = 'test2'
        _fact_ids = set(('test3','test4'))

    class TestCollector3(TestCollector2):
        name = 'test3'
        _fact_ids = set(('test4'))

    fact_id_to_collector_map, aliases_map = build_fact_id_to_collector_map([TestCollector, TestCollector2, TestCollector3])


# Generated at 2022-06-13 00:28:40.383345
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    from ansible.module_utils._text import to_text
    from ansible.module_utils.facts.namespace import BaseFactNamespace
    from ansible.module_utils.facts.utils import get_all_collector_classes, get_collector_classes, find_deps_for_collector_classes, _get_ordered_deps

    class A(BaseFactCollector):
        name = 'a'
        def collect(self, module=None, collected_facts=None):
            return {'a':'A'}

    class B(BaseFactCollector):
        name = 'b'
        def collect(self, module=None, collected_facts=None):
            return {'b':'B'}

    class C(BaseFactCollector):
        name = 'c'

# Generated at 2022-06-13 00:28:52.467392
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    # Goal: check the result of find_unresolved_requires
    # with a predictable set of collectors, some with requirements
    # and of course, some without.

    # all_fact_subsets is a dict of lists
    # keys are collector names, values are lists of classes
    all_fact_subsets = defaultdict(list)

    class CollectorClass(object):
        required_facts = None
        name = None

    class A(CollectorClass):
        required_facts = []
        name = 'A'

    class B(CollectorClass):
        required_facts = ['C']
        name = 'B'

    class C(CollectorClass):
        required_facts = ['D']
        name = 'C'

    class D(CollectorClass):
        required_facts = []
        name = 'D'


# Generated at 2022-06-13 00:28:56.769195
# Unit test for function collector_classes_from_gather_subset
def test_collector_classes_from_gather_subset():
    class FakeCollector(BaseFactCollector):
        _platform = 'Linux'

    class AnotherFakeCollector(BaseFactCollector):
        _platform = 'Linux'

    FakeCollector.required_facts = set()
    FakeCollector.name = 'fake'

    AnotherFakeCollector.required_facts = set()
    AnotherFakeCollector.name = 'another_fake'

    # test that these facts can be retrieved, even if the platform is not found.
    class AnotherFakeCollectorNonLinux(BaseFactCollector):
        pass
    AnotherFakeCollectorNonLinux.required_facts = set()
    AnotherFakeCollectorNonLinux.name = 'uname'

    all_collector_classes = [FakeCollector, AnotherFakeCollector, AnotherFakeCollectorNonLinux]


# Generated at 2022-06-13 00:29:07.260055
# Unit test for function select_collector_classes
def test_select_collector_classes():
    import sys
    import warnings
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts import collector
    from ansible.module_utils.facts.network.base import NetworkCollector

    selected_collector_classes = None
    try:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", DeprecationWarning)
            collector_names = ['all']
            all_fact_subsets = {
                collector.NetworkCollector.name: [collector.NetworkCollector, NetworkCollector]}
            selected_collector_classes = select_collector_classes(collector_names, all_fact_subsets)
    except TypeError as e:
        assert 'NetworkCollector' in to_bytes(e), e

# Generated at 2022-06-13 00:29:21.593968
# Unit test for function get_collector_names
def test_get_collector_names():
    assert get_collector_names() == frozenset(['all'])
    assert get_collector_names(valid_subsets=frozenset(['os', 'redhat']), gather_subset=['all']) == frozenset(['redhat', 'os'])
    assert get_collector_names(valid_subsets=frozenset(['os', 'redhat']), gather_subset=['os']) == frozenset(['os'])
    assert get_collector_names(valid_subsets=frozenset(['os', 'redhat']), gather_subset=['!redhat']) == frozenset(['os'])

# Generated at 2022-06-13 00:29:29.105544
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    all_fact_subsets = {
        'a': [MockCollector(('b', 'c')), MockCollector(('b', 'c'))],
        'b': [MockCollector(('c',))],
        'c': [MockCollector(())],
    }
    assert find_unresolved_requires(['a'], all_fact_subsets) == set()
    assert find_unresolved_requires(['b', 'c'], all_fact_subsets) == set()
    assert find_unresolved_requires(['c'], all_fact_subsets) == set()

    assert find_unresolved_requires(['b'], all_fact_subsets) == set(['c'])

# Generated at 2022-06-13 00:29:35.687040
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    all_fact_subsets = {
        'foo': [object()],
        'bar': [object()],
        'baz': [object()],
    }
    collector_names = ['foo', 'baz']
    assert find_unresolved_requires(collector_names, all_fact_subsets) == set(['bar'])
test_find_unresolved_requires()



# Generated at 2022-06-13 00:29:44.553879
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    class CollectorA(BaseFactCollector):
        name = 'a'
        _fact_ids = {'a', 'b'}

    class CollectorB(BaseFactCollector):
        name = 'b'
        _fact_ids = {'b', 'c'}

    class CollectorC(BaseFactCollector):
        name = 'c'
        _fact_ids = {'d', 'e'}

    fact_id_to_collector_map, aliases_map = build_fact_id_to_collector_map([CollectorA, CollectorB, CollectorC])

# Generated at 2022-06-13 00:29:55.840295
# Unit test for function get_collector_names
def test_get_collector_names():

    def test_get_collector_names_simple(valid_subsets=None,
                                        minimal_gather_subset=None,
                                        gather_subset=None,
                                        aliases_map=None,
                                        platform_info=None):
        return sorted(get_collector_names(valid_subsets, minimal_gather_subset, gather_subset, aliases_map, platform_info))

    # test with empty sets
    assert test_get_collector_names_simple() == ['all']
    # test some basics, 'interfaces', 'all'
    assert test_get_collector_names_simple(valid_subsets=['interfaces']) == ['all', 'interfaces']

# Generated at 2022-06-13 00:29:58.681415
# Unit test for function build_dep_data
def test_build_dep_data():
    dep_map = build_dep_data(['hardware'], {'hardware': [MockCollector("hardware", ["virtual"])]})
    assert dep_map["hardware"] == set(["virtual"])


# Generated at 2022-06-13 00:30:11.501416
# Unit test for function build_dep_data
def test_build_dep_data():
    all_fact_subsets = {
        'lala': [
            type('Collector', (BaseFactCollector,),
                  {
                      'name':'lala',
                      'required_facts':set(['foo', 'bar'])
                  }
                  )
        ],
        'foo': [
            type('Collector', (BaseFactCollector,),
                  {
                      'name':'foo',
                      'required_facts':set(['bar'])
                  }
                  )
        ],
        'bar': [
            type('Collector', (BaseFactCollector,),
                  {
                      'name':'bar',
                      'required_facts':set()
                  }
                  )
        ]
    }
    collector_names = ['lala', 'foo', 'bar']
    dep_map = build_dep_data

# Generated at 2022-06-13 00:30:23.077460
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    from ansible.module_utils.facts.namespace import BaseNamePart
    from ansible.module_utils.facts.collector.network import Network
    from ansible.module_utils.facts.collector.hardware import Hardware
    from ansible.module_utils.facts.collector.platform import Platform
    from ansible.module_utils.facts.collector.distribution import Distribution
    from ansible.module_utils.facts.collector.bios import BIOS
    from ansible.module_utils.facts.collector.cmdline import CmdLine
    from ansible.module_utils.facts.collector.interfaces import Interfaces
    from ansible.module_utils.facts.collector.mounts import Mounts
    from ansible.module_utils.facts.collector.package_mgr import PackageMgr

# Generated at 2022-06-13 00:30:34.141088
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    from ansible.module_utils.facts.system.distribution import DistributionFactCollector
    from ansible.module_utils.facts.system.distribution import DistributionNamespace
    from ansible.module_utils.facts.system.distribution import LinuxDistributionFactCollector

    linux_distribution = LinuxDistributionFactCollector()
    distribution = DistributionFactCollector()
    namespace = DistributionNamespace()

    all_subsets = {
        'distribution': [DistributionFactCollector, linux_distribution]
    }

    assert linux_distribution.required_facts == {'distribution'}, 'basic sanity check'

    unresolved = find_unresolved_requires(['distribution'], all_subsets)
    assert unresolved == set(), 'basic sanity check'


# Generated at 2022-06-13 00:30:43.302220
# Unit test for function get_collector_names
def test_get_collector_names():

    assert get_collector_names(gather_subset=['all']) == frozenset(['all'])
    assert get_collector_names(gather_subset=['!all']) == frozenset(['min'])
    assert get_collector_names(gather_subset=['!foo']) == frozenset(['min'])
    assert get_collector_names(gather_subset=['!all', '!foo']) == frozenset(['min'])
    assert get_collector_names(gather_subset=['foo']) == frozenset(['foo'])
    assert get_collector_names(gather_subset=['!min']) == set()

    assert get_collector_names(gather_subset=['foo', '!foo'])

# Generated at 2022-06-13 00:31:09.731636
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    import unittest
    class TestCollector(BaseFactCollector):
        name = 'thing'
        _fact_ids = ['thing']

    class Test1(TestCollector):
        name = 'test1'
        _fact_ids = TestCollector._fact_ids | {'test1'}

    class Test2(TestCollector):
        name = 'test2'
        _fact_ids = TestCollector._fact_ids | {'test2'}

    class Test3(Test1, Test2):
        name = 'test3'
        _fact_ids = TestCollector._fact_ids | Test1._fact_ids | Test2._fact_ids | {'test3'}

    class Test4(TestCollector):
        name = 'test4'
        _fact_ids = TestCollector._fact_ids

# Generated at 2022-06-13 00:31:21.557280
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    assert find_unresolved_requires(['base'], {'base': [object()]}) == set()
    assert find_unresolved_requires(['base'], {'base': [object()],
                                               'b': [object()]}) == set(['b'])
    assert find_unresolved_requires(['base', 'b', 'c'], {'base': [object()],
                                                         'b': [object()],
                                                         'c': [object()]}) == set()
    assert find_unresolved_requires(['b', 'c'], {'base': [object()],
                                                 'b': [object()],
                                                 'c': [object()]}) == set(['base'])

# Generated at 2022-06-13 00:31:28.107265
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    all_fact_subsets = {
        'fact-A': [object()],
        'fact-B': [object()],
        'fact-C': [object()],
        'fact-D': [object()],
        'fact-E': [object()],
        'fact-F': [object()],
    }

    # all_fact_subsets contains five objects, each of which has a .requires_facts() set
    for k, v in all_fact_subsets.items():
        v[0].required_facts = set([k])

    # so A requires that A be collected
    # so B requires that B be collected
    # C does not require anything be collected
    # D requires that A, B, C, and D be collected
    # E requires that A, B, C, and E be collected
    # F requires

# Generated at 2022-06-13 00:31:35.712857
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    from ansible.module_utils.facts.collector.network.linux import LinuxNetwork
    from ansible.module_utils.facts.collector.network.windows import WindowsNetwork
    from ansible.module_utils.facts.collector import defaultdict
    all_fact_subsets = defaultdict(set)
    all_fact_subsets[LinuxNetwork.name] = set([LinuxNetwork])
    all_fact_subsets[WindowsNetwork.name] = set([WindowsNetwork])

    collector_names = set(['all', LinuxNetwork.name])
    unresolved = find_unresolved_requires(collector_names, all_fact_subsets)
    assert unresolved == set()

    # fixed bug when requiring 'all'
    collector_names = set(['all', 'min', 'platform'])

# Generated at 2022-06-13 00:31:45.782692
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    from ansible.module_utils.facts.collectors import network

    all_fact_subsets = defaultdict(list)
    for collector in [network.AllInterfaces]:
        for fact in collector._fact_ids:
            all_fact_subsets[fact].append(collector)

    # all requirements are resolved
    collector_names = ['network']
    assert not find_unresolved_requires(collector_names, all_fact_subsets)

    # unresolved requirements
    collector_names = ['network', 'interface_ip']
    unresolved = find_unresolved_requires(collector_names, all_fact_subsets)
    unresolved_names = [c.name for c in unresolved]
    assert sorted(unresolved_names) == ['interface']



# Generated at 2022-06-13 00:31:51.964387
# Unit test for function build_dep_data
def test_build_dep_data():
    collector_dep_data = build_dep_data(['one', 'two'], {'one': ['one', 'three'], 'two': ['two', 'three']})
    assert(collector_dep_data['one'] == set('three'))
    assert(collector_dep_data['two'] == set('three'))



# Generated at 2022-06-13 00:31:57.754589
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    expected_missing_collector_names = set(['ipv4'])
    collector_names = {'interfaces', 'all'}
    all_fact_subsets = {
        'all': [
            FactCollectorWithRequires,
            FactCollectorWithoutRequires,
            FactCollectorWithRequires2
        ],
        'interfaces': [FactCollectorWithoutRequires]
    }

    missing_collector_names = find_unresolved_requires(collector_names, all_fact_subsets)
    assert missing_collector_names == expected_missing_collector_names



# Generated at 2022-06-13 00:32:07.376943
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    from ansible.module_utils.facts.collector.hardware.cpu import CPUCollector
    from ansible.module_utils.facts.collector.hardware.ps import PSCollector

    fact_id_to_collector_map, aliases_map = build_fact_id_to_collector_map([CPUCollector, PSCollector])

    assert aliases_map == defaultdict(set, {
        'cpu': {'processor', 'processors'},
        'ps': {'procs', 'processes'},
        })


# Generated at 2022-06-13 00:32:16.704777
# Unit test for function build_dep_data
def test_build_dep_data():
    class FakeClass(object):
        pass
    alist = []
    alist.append(FakeClass())
    alist.append(FakeClass())
    i = 2
    for elem in alist:
        elem.name = "elem" + str(i)
        elem.required_facts = []
        i -= 1
    bdict = {}
    bdict['elem1'] = [alist[0]]
    bdict['elem2'] = [alist[1]]
    input_list = ['elem1', 'elem2']
    dep_map = build_dep_data(input_list, bdict)
    assert dep_map == {'elem1':set(), 'elem2':set()}



# Generated at 2022-06-13 00:32:26.007033
# Unit test for function get_collector_names
def test_get_collector_names():
    valid_subsets = frozenset()
    minimal_gather_subset = frozenset()
    aliases_map = defaultdict(set)

    # all and min
    assert get_collector_names(valid_subsets,
                               minimal_gather_subset,
                               ['all'],
                               aliases_map) == valid_subsets
    assert get_collector_names(valid_subsets,
                               minimal_gather_subset,
                               ['min'],
                               aliases_map) == minimal_gather_subset

    # !all and !min

# Generated at 2022-06-13 00:32:50.672069
# Unit test for function find_collectors_for_platform
def test_find_collectors_for_platform():
    from os.path import dirname
    import sys
    from ansible.module_utils.facts.collectors import (
        generic, redhat, solaris, ubuntu, osx, aix,
        netbsd, openbsd, windows, openwrt
    )
    sys.path.append(dirname(generic.__file__))
    sys.path.append(dirname(redhat.__file__))
    sys.path.append(dirname(solaris.__file__))
    sys.path.append(dirname(ubuntu.__file__))
    sys.path.append(dirname(osx.__file__))
    sys.path.append(dirname(aix.__file__))
    sys.path.append(dirname(netbsd.__file__))

# Generated at 2022-06-13 00:33:01.466944
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    class test_collector_class(BaseFactCollector):
        name = 'foo'
        _fact_ids = {'bar'}

    class test_collector_class_2(BaseFactCollector):
        name = 'bar'
        _fact_ids = {'baz'}

    test_collector_classes = [test_collector_class, test_collector_class_2]

    fact_id_to_collector_map, aliases_map = build_fact_id_to_collector_map(test_collector_classes)

    assert len(fact_id_to_collector_map) == 3, \
        "build_fact_id_to_collector_map should contain 3 entries"


# Generated at 2022-06-13 00:33:12.163213
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    class DummyCollector(BaseFactCollector):
        name = 'dummy_collector'
        required_facts = frozenset(['bar', 'baz'])

    class CollectorRequires(BaseFactCollector):
        name = 'collector_requires'
        required_facts = frozenset(['dummy_collector'])

    class CollectorRequires1(BaseFactCollector):
        name = 'collector_requires1'
        required_facts = frozenset(['dummy_collector1'])

    class CollectorRequires2(BaseFactCollector):
        name = 'collector_requires2'
        required_facts = frozenset(['dummy_collector2'])

    class CollectorRequires3(BaseFactCollector):
        name = 'collector_requires3'

# Generated at 2022-06-13 00:33:24.332609
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    from ansible.module_utils.facts._collectors.system.distribution import DistributionFactCollector
    from ansible.module_utils.facts._collectors.system.distribution.openbsd import OpenBSDDistributionFactCollector
    from ansible.module_utils.facts._collectors.system.distribution.smartos import SmartOSDistributionFactCollector

    collectors_for_platform = [
        DistributionFactCollector(),
        OpenBSDDistributionFactCollector(),
        SmartOSDistributionFactCollector()
    ]

    fact_id_to_collector_map, aliases_map = build_fact_id_to_collector_map(collectors_for_platform)


# Generated at 2022-06-13 00:33:30.856066
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    all_fact_subsets = {}
    all_fact_subsets['a'] = [BaseFactCollector]
    all_fact_subsets['b'] = [BaseFactCollector]
    all_fact_subsets['d'] = [BaseFactCollector]
    all_fact_subsets['e'] = [BaseFactCollector]

    class ClassA(BaseFactCollector):
        _fact_ids = set(['a'])
        name = 'a'
        required_facts = set(['b'])

    class ClassB(BaseFactCollector):
        _fact_ids = set(['b'])
        name = 'b'
        required_facts = set(['c'])

    class ClassC(BaseFactCollector):
        _fact_ids = set(['c'])
        name = 'c'


# Generated at 2022-06-13 00:33:35.455438
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    from ansible.modules.system.setup import FakeFactsCollector

    ffc = FakeFactsCollector
    ffc.name = 'test'
    ffc.required_facts = ['test1', 'test2', 'test3']
    all_fact_subsets = {'test': [ffc]}

    assert find_unresolved_requires(['test2', 'test3'], all_fact_subsets) == set(['test'])
    assert find_unresolved_requires(['test2', 'test3', 'test'], all_fact_subsets) == set()



# Generated at 2022-06-13 00:33:43.012750
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    all_fact_subsets = {}
    all_fact_subsets['a'] = [object()]

    assert not find_unresolved_requires(['a'], all_fact_subsets)

    all_fact_subsets['b'] = [object()]

    assert find_unresolved_requires(['b'], all_fact_subsets) == {'a'}
    assert find_unresolved_requires(['a'], all_fact_subsets) == {'b'}
    assert not find_unresolved_requires(['a', 'b'], all_fact_subsets)



# Generated at 2022-06-13 00:33:53.249683
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    from ansible.module_utils.facts.collectors.system import Hardware

    # test aliases_map
    fact_id_to_collector_map, aliases_map = build_fact_id_to_collector_map(set([Hardware]))
    print("fact_id_to_collector_map: %s" % fact_id_to_collector_map)
    assert 'system' in fact_id_to_collector_map
    assert 'hardware' in fact_id_to_collector_map
    assert 'devices' in fact_id_to_collector_map
    assert 'dmi' in fact_id_to_collector_map
    assert fact_id_to_collector_map['system'] == fact_id_to_collector_map['hardware'] == fact_id_to_collector

# Generated at 2022-06-13 00:33:57.698445
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    from ansible.module_utils.facts.utils import TestFactCollector
    from ansible.module_utils.facts.utils import TestGenericFactCollector
    FAKE_COLLECTOR_CLASSES = {
        # key is name, value is the fact IDs it provides
        'test_fact_collector': ['test_fact_collector'],
        'test_generic_fact_collector': ['test_generic_fact_collector'],
        'test_fact_collector_with_alias': ['test1', 'test2'],
        'test_generic_fact_collector_with_alias': ['test3', 'test4'],
    }

# Generated at 2022-06-13 00:34:07.842229
# Unit test for function build_dep_data
def test_build_dep_data():
    from ansible.module_utils.facts import local
    from ansible.module_utils.facts import timeout
    from ansible.module_utils.facts import local_facts

    collector_names = set()
    for fact_name, fact_class in local_facts.items():
        for fact_subclass in fact_class.__subclasses__():
            collector_names.add(fact_subclass.name)

    all_fact_subsets = local.get_fact_subsets(fact_classes=local_facts,
                                              collector_names=collector_names,
                                              timeout=timeout.Timeout(5),
                                              debug=False)

    dep_map = build_dep_data(collector_names, all_fact_subsets)