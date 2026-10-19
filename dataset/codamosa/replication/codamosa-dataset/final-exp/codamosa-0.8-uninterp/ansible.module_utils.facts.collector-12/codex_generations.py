

# Generated at 2022-06-13 00:24:31.515625
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    class Collector1(BaseFactCollector):
        name = 'collector1'
        required_facts = frozenset(['fact1', 'fact2'])
    class Collector2(BaseFactCollector):
        name = 'collector2'
        required_facts = frozenset(['fact2', 'fact3'])

    all_fact_subsets = {}
    for collector_class in [Collector1, Collector2]:
        all_fact_subsets.setdefault(collector_class.name, []).append(collector_class)

    unresolved = find_unresolved_requires(['collector1', 'collector2'], all_fact_subsets)
    assert len(unresolved) == 0

    unresolved = find_unresolved_requires(['collector1'], all_fact_subsets)

# Generated at 2022-06-13 00:24:38.475055
# Unit test for function tsort
def test_tsort():
    data1 = {'a': ['b', 'c'],
             'b': ['d'],
             'c': ['e'],
             'd': ['f'],
             'e': ['f'],
             'f': [],
            }

    data2 = {'a': ['b', 'c'],
             'b': ['a'],
             'c': ['a'],
            }

    assert tsort(data1) == [('f', []), ('d', ['f']), ('e', ['f']), ('b', ['d']), ('c', ['e']), ('a', ['b', 'c'])]
    assert tsort(data2) == [('c', ['a']), ('b', ['a']), ('a', ['b', 'c'])]
test_tsort()



# Generated at 2022-06-13 00:24:46.171981
# Unit test for function get_collector_names
def test_get_collector_names():
    # Fixture for same defaults GatherFacts module
    platform_info = {
        'distribution': 'CentOS',
        'distribution_release': '7.4.1708',
        'distribution_version': '7',
        'kernel': 'Linux',
        'kernel_version': '3.10.0-693.21.1.el7.x86_64',
        'os_family': 'RedHat',
        'system': 'Linux',
        'system_vendor': 'innotek GmbH'
    }
    # Test with no subset
    result = get_collector_names(platform_info=platform_info)
    expected = frozenset(['all'])
    assert result == expected
    # Test with subset

# Generated at 2022-06-13 00:24:56.297614
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    class CollectorStub1(BaseFactCollector):
        _fact_ids = set(['foo', 'bar'])
        name = 'collector1'

    class CollectorStub2(BaseFactCollector):
        _fact_ids = set(['baz'])
        name = 'collector2'

    class CollectorStub3(BaseFactCollector):
        _fact_ids = set()
        name = 'collector3'

    all_collectors = [CollectorStub1, CollectorStub2, CollectorStub3]

    fact_id_to_collector_map, aliases_map = build_fact_id_to_collector_map(all_collectors)



# Generated at 2022-06-13 00:25:07.380981
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    from ansible.module_utils.facts.collector.system import SystemCollector
    from ansible.module_utils.facts.collector.system.distribution import DistributionCollector
    from ansible.module_utils.facts.collector.system.distribution.arch import ArchCollector
    from ansible.module_utils.facts.collector.system.distribution.debian import DebianCollector
    from ansible.module_utils.facts.collector.system.distribution.fedora import FedoraCollector
    from ansible.module_utils.facts.collector.system.distribution.freebsd import FreeBSDCollector
    from ansible.module_utils.facts.collector.system.distribution.gentoo import GentooCollector
    from ansible.module_utils.facts.collector.system.distribution.openbsd import OpenBSDCollect

# Generated at 2022-06-13 00:25:18.856319
# Unit test for function find_collectors_for_platform
def test_find_collectors_for_platform():
    all_collectors_list = list()
    all_collectors_list.append(
                        BaseFactCollector('Test',
                                          {'system': 'Darwin', 'kernel': '18.5.0'}))
    all_collectors_list.append(BaseFactCollector('Test2',
                                                 {'system': 'Darwin',
                                                  'kernel': '18.5.0'}))
    all_collectors_list.append(BaseFactCollector('Test',
                                                 {'system': 'Darwin'}))
    all_collectors_list.append(BaseFactCollector('Test',
                                                 {'system': 'Linux'}))
    all_collectors_list.append(BaseFactCollector('Test',
                                                 {'system': 'Linux'}))

    base_

# Generated at 2022-06-13 00:25:27.202145
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    from ansible.module_utils.facts.network.base import NetworkCollector
    from ansible.module_utils.facts.system.base import SystemCollector
    from ansible.module_utils.facts.distribution.base import DistributionCollector
    from ansible.module_utils.facts.virtual.base import VirtualNetworkCollector
    from ansible.module_utils.facts.virtual.base import VirtualSystemCollector
    from ansible.module_utils.facts.virtual.base import VirtualVmCollector


# Generated at 2022-06-13 00:25:38.620021
# Unit test for function build_dep_data
def test_build_dep_data():
    import mock
    import pytest

    class TestCollector1(BaseFactCollector):
        name = 'test1'
        required_facts = [ 'test3' ]
        def collect(self, module=None, collected_facts=None):
            return {}

    class TestCollector2(BaseFactCollector):
        name = 'test2'
        required_facts = [ 'test1' ]
        def collect(self, module=None, collected_facts=None):
            return {}

    class TestCollector3(BaseFactCollector):
        name = 'test3'
        required_facts = []
        def collect(self, module=None, collected_facts=None):
            return {}

    class TestCollector4(BaseFactCollector):
        name = 'test4'
        required_facts = []

# Generated at 2022-06-13 00:25:47.151845
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    class CollectDep(BaseFactCollector):
        name = 'test_dep'
        required_facts = ['ping', 'test_fact']
    class NoCollectDep(BaseFactCollector):
        name = 'nodep'
        required_facts = ['no_fact']

    class CollectFact(BaseFactCollector):
        name = 'test_fact'
        required_facts = ['ping']

    class CollectPing(BaseFactCollector):
        name = 'ping'
        required_facts = []

    all_fact_subsets = {
        'test_dep': [CollectDep],
        'nodep': [NoCollectDep],
        'test_fact': [CollectFact],
        'ping': [CollectPing],
    }

    # any reqs not in collector_names should be returned
    unresolved = find_unresolved_

# Generated at 2022-06-13 00:25:58.765287
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    a = b = c = 'a', 'b', 'c'
    FAKE_COLLECTORS = {
        a: [
            type('_A', (object,), dict(required_facts='b')),
        ],
        b: [
            type('_B', (object,), dict(required_facts='c')),
        ],
        c: [
            type('_C', (object,), dict(required_facts=set()))
        ]
    }
    assert find_unresolved_requires(a, FAKE_COLLECTORS) == set()
    assert find_unresolved_requires(b, FAKE_COLLECTORS) == set()
    assert find_unresolved_requires(c, FAKE_COLLECTORS) == set()

# Generated at 2022-06-13 00:26:14.795545
# Unit test for function build_dep_data
def test_build_dep_data():
    all_fact_subsets = {
        '1': [1, 2],
        '2': [3]
    }
    collector_names = ['1', '2']
    assert build_dep_data(collector_names, all_fact_subsets) == {
        '1': {},
        '2': set()
    }



# Generated at 2022-06-13 00:26:23.897828
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    # test data
    class Network(BaseFactCollector):
        _fact_ids = {'net0', 'net1'}
    class NetworkForms(BaseFactCollector):
        _fact_ids = {'net0', 'net1', 'network'}
    class All(BaseFactCollector):
        _fact_ids = {'all'}
    class Min(BaseFactCollector):
        pass

    # function to test
    def test_function(collectors_for_platform):
        return build_fact_id_to_collector_map(collectors_for_platform)

    # test cases

# Generated at 2022-06-13 00:26:36.187937
# Unit test for function get_collector_names
def test_get_collector_names():
    def check(additional_subsets, expected, gather_subset=None, minimal_gather_subset=None):
        # valid_subsets is ignored, but we need something for the test
        valid_subsets = frozenset()
        minimal_gather_subset = minimal_gather_subset or frozenset()
        result = get_collector_names(valid_subsets, minimal_gather_subset, gather_subset)
        assert result == additional_subsets, result

    # A few examples, mostly the same as the tests in module_utils/facts/__init__.py
    check(frozenset(), frozenset(),
          gather_subset=['!all'])

# Generated at 2022-06-13 00:26:45.493180
# Unit test for function select_collector_classes
def test_select_collector_classes():
    sys_platform = platform.system()
    compat_platforms = [
        {'system': sys_platform},
        {'system': 'Generic'},
    ]

    class CollectorA(BaseFactCollector):
        _platform = 'Linux'
        name = 'collector_a'
        _fact_ids = set(['a1', 'a2', 'c1'])

    class CollectorB(BaseFactCollector):
        _platform = 'Linux'
        name = 'collector_b'
        _fact_ids = set(['b1', 'b2', 'b3', 'c1'])

    class CollectorC(BaseFactCollector):
        _platform = 'Linux'
        name = 'collector_c'
        _fact_ids = set(['c1', 'c2'])


# Generated at 2022-06-13 00:26:52.560015
# Unit test for function select_collector_classes
def test_select_collector_classes():
    '''
    Selecting the correct collectors for specific platforms
    '''
    collector_list = ['all', 'hardware', 'dmi']
    all_fact_subsets = {'hardware': [LinuxHardware], 'dmi': [LinuxDMI]}

    returned_collectors = select_collector_classes(collector_list, all_fact_subsets)

    returned_names = [collector.name for collector in returned_collectors]

    for name in collector_list:
        if name == 'all':
            continue
        assert name in returned_names



# Generated at 2022-06-13 00:27:02.331706
# Unit test for function find_collectors_for_platform
def test_find_collectors_for_platform():
    import sys
    import copy


# Generated at 2022-06-13 00:27:12.756497
# Unit test for function get_collector_names
def test_get_collector_names():
    import pytest

    valid_subsets = frozenset(['dmi', 'hardware', 'networking'])

    minimal_gather_subset = frozenset(['dmi'])

    # NOTE: this is a list of lists, where each list is a test case and the
    #       arguments to get_collector_names for the test case

# Generated at 2022-06-13 00:27:23.931285
# Unit test for function get_collector_names
def test_get_collector_names():
    min_collector_names = frozenset(('dmi', 'devices'))
    all_collector_names = frozenset(('foo', 'bar'))
    aliases_map = defaultdict(set, {
        'hardware': frozenset(('dmi', 'devices'))
    })

    platform_info = {'system': 'my_system'}

    # happy path:
    subset_spec = ['hardware']
    collector_names = get_collector_names(valid_subsets=all_collector_names,
                                          aliases_map=aliases_map,
                                          platform_info=platform_info,
                                          gather_subset=subset_spec)

    assert collector_names == frozenset(('dmi', 'devices'))

    # happy path:
    subset_spec

# Generated at 2022-06-13 00:27:32.464188
# Unit test for function get_collector_names
def test_get_collector_names():
    valid_subsets = frozenset(['hardware', 'dmi', 'devices', 'virtual'])

    minimal_gather_subset = frozenset(['dmi'])

    # Case 1: gather_subset=None, gather_minimal_facts=None
    # expected facts = dmi, hardware
    actual_facts = get_collector_names(valid_subsets=valid_subsets,
                                       minimal_gather_subset=minimal_gather_subset,
                                       gather_subset=['all'])
    expected_facts = frozenset(['hardware', 'dmi', 'devices', 'virtual'])
    assert actual_facts == expected_facts

    # Case 2: gather_subset=None, gather_minimal_facts=False
    # expected facts = dmi, hardware
    actual

# Generated at 2022-06-13 00:27:44.884892
# Unit test for function select_collector_classes
def test_select_collector_classes():
    assert(len(select_collector_classes([], {})) == 0)
    assert(len(select_collector_classes([], defaultdict(list))) == 0)

    all_subsets = defaultdict(list)
    all_subsets['foo'].append('a')
    all_subsets['foo'].append('b')
    all_subsets['foo'].append('c')
    all_subsets['bar'].append('d')
    all_subsets['bar'].append('e')
    assert(len(select_collector_classes(['foo'], all_subsets)) == 3)

    all_subsets = defaultdict(list)
    all_subsets['foo'].append('a')
    all_subsets['foo'].append('b')

# Generated at 2022-06-13 00:28:16.986280
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    from . import get_collector_classes
    all_fact_subsets = get_collector_classes([])
    collector_names = ['on_redhat', 'on_debian']

    assert find_unresolved_requires(collector_names, all_fact_subsets)



# Generated at 2022-06-13 00:28:24.517132
# Unit test for function build_dep_data
def test_build_dep_data():
    collector_names = ["foo", "bar", "baz"]
    all_fact_subsets = {}
    all_fact_subsets["foo"] = ["foo_class"]
    all_fact_subsets["bar"] = ["bar_class"]
    all_fact_subsets["baz"] = ["baz_class"]
    dep_data = build_dep_data(collector_names, all_fact_subsets)
    assert dep_data["foo"] == set()
    assert dep_data["bar"] == set()
    assert dep_data["baz"] == set()


# Generated at 2022-06-13 00:28:36.434347
# Unit test for function get_collector_names
def test_get_collector_names():
    # Minimal gather subset is 'all'
    assert get_collector_names(['all'], ['all'], minimal_gather_subset=['all']) == {'all'}

    # Test that with no gather_subset, we return all
    assert get_collector_names(['all'], [], minimal_gather_subset=['all']) == {'all'}

    # Test that gather_subset=['min'] returns nothing
    assert get_collector_names(['all'], ['min'], minimal_gather_subset=['all']) == {'all'}

    # Test that gather_subset=['!all'] returns empty set
    assert get_collector_names(['all'], ['!all'], minimal_gather_subset=['all']) == set()

   

# Generated at 2022-06-13 00:28:45.867110
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    class MyCollectorClass2(BaseFactCollector):
        _fact_ids = {'another_fact_id'}

    class MyCollectorClass(BaseFactCollector):
        _fact_ids = {'fact_id'}

    all_collector_classes = [MyCollectorClass, MyCollectorClass2]
    fact_id_to_collector_map, aliases_map = build_fact_id_to_collector_map(all_collector_classes)

    assert len(fact_id_to_collector_map) == 2
    assert len(aliases_map) == 2

    assert fact_id_to_collector_map['fact_id'] == [MyCollectorClass]
    assert aliases_map['fact_id'] == {'fact_id'}

    assert fact_id_to_collector

# Generated at 2022-06-13 00:28:56.406414
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    # add fake collector classes to all_fact_subsets to test our
    # find_unresolved_requires
    all_fact_subsets = defaultdict(list)

    class collector_a(BaseFactCollector):
        name = 'a'
        required_facts = set()

    class collector_b(BaseFactCollector):
        name = 'b'
        required_facts = set()

    class collector_c(BaseFactCollector):
        name = 'c'
        required_facts = {'a'}

    class collector_d(BaseFactCollector):
        name = 'd'
        required_facts = {'b'}

    all_fact_subsets['a'].append(collector_a)
    all_fact_subsets['b'].append(collector_b)
    all_fact_sub

# Generated at 2022-06-13 00:29:07.183407
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    from ansible.module_utils.facts import hardware
    from ansible.module_utils.facts import network
    from ansible.module_utils.facts import system


# Generated at 2022-06-13 00:29:16.415751
# Unit test for function build_dep_data
def test_build_dep_data():
    import ansible.module_utils.facts.system.distribution
    from ansible.module_utils.facts.system import networking, selinux, distribution

    all_fact_subsets = {'networking': [networking.Networking, distribution.Distribution], 'distribution': [distribution.Distribution]}
    collector_names = ['networking', 'distribution']
    dep_map = build_dep_data(collector_names, all_fact_subsets)
    assert 'networking' in dep_map
    assert 'distribution' in dep_map
    assert 'selinux' not in dep_map
    assert len(dep_map['networking']) == 2
    assert 'distribution' in dep_map['networking']
    assert 'selinux' in dep_map['networking']

# Generated at 2022-06-13 00:29:27.215559
# Unit test for function build_dep_data
def test_build_dep_data():
    # test case with 2 single dependencies and a mutual dependency
    collector_names = ['One', 'Two', 'Three']
    dep_map = build_dep_data(collector_names, {
        'One': [BaseFactCollector(required_facts=['Two'])],
        'Two': [BaseFactCollector(required_facts=['One', 'Three'])],
        'Three': [BaseFactCollector(required_facts=['Two'])]
    })
    assert 'One' in dep_map
    assert 'Two' in dep_map
    assert 'Three' in dep_map
    assert len(dep_map) == 3
    assert dep_map['One'] == set(['Two'])
    assert dep_map['Two'] == set(['One', 'Three'])

# Generated at 2022-06-13 00:29:38.997686
# Unit test for function build_dep_data
def test_build_dep_data():
    from .facts import FACT_SUBSETS
    from .facts import collectors as fact_collectors
    from .facts.collector import BaseFactCollector
    class DummyBase(BaseFactCollector):
        pass
    class Dummy1(DummyBase):
        name = 'dummy1'
        required_facts = ['dummy2']
    class Dummy2(DummyBase):
        name = 'dummy2'
        required_facts = ['dummy1']

    all_fact_subsets = FACT_SUBSETS
    all_fact_subsets['dummy1'] = [Dummy1]
    all_fact_subsets['dummy2'] = [Dummy2]

    dep_map = build_dep_data(['dummy1', 'dummy2'], all_fact_subsets)

# Generated at 2022-06-13 00:29:49.335234
# Unit test for function select_collector_classes
def test_select_collector_classes():
    # smoke test for select_collector_classes
    collector_a = type('collector_a', (object,), dict(name='a'))
    collector_b = type('collector_b', (object,), dict(name='b', _fact_ids=frozenset(['b', 'c'])))
    collector_c = type('collector_c', (object,), dict(name='d', _fact_ids=frozenset(['d', 'c'])))
    # this collector_d is only named 'c' and not 'c_other'
    collector_d = type('collector_d', (object,), dict(name='c'))
    all_fact_subsets = defaultdict(list)
    all_fact_subsets[collector_a.name].append(collector_a)
    all

# Generated at 2022-06-13 00:30:11.865452
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    # all these test classes are defined just below this function
    TestCollector1
    TestCollector2
    TestCollector3
    TestCollector4

    collectors_for_platform = set([TestCollector1])
    id_map, aliases_map = build_fact_id_to_collector_map(collectors_for_platform)
    assert 'all' in id_map
    assert 'all' in aliases_map
    assert len(id_map['all']) == 1

    assert id_map['all'][0] == TestCollector1
    assert id_map['one'] == id_map['all']

    collectors_for_platform = set([TestCollector1, TestCollector2])
    id_map, aliases_map = build_fact_id_to_collector_map(collectors_for_platform)


# Generated at 2022-06-13 00:30:23.474320
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    class FakeFactCollector:
        _fact_ids = set()

        _platform = 'Generic'
        name = None
        required_facts = set()

    class CollectorA(FakeFactCollector):
        name = 'A'
        required_facts = set(['B'])

    class CollectorB(FakeFactCollector):
        name = 'B'
        required_facts = set()

    class CollectorD(FakeFactCollector):
        name = 'D'
        required_facts = set(['F'])

    all_fact_subsets = defaultdict(list)
    all_fact_subsets['A'] = [CollectorA]
    all_fact_subsets['B'] = [CollectorB]
    all_fact_subsets['D'] = [CollectorD]

    unresolved = find_unresolved_requires

# Generated at 2022-06-13 00:30:34.457102
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    # Simple success case
    all_fact_subsets = defaultdict(list)
    collector_names = ['os_version']
    all_fact_subsets['os_version'] = [FakeCollectorClass1]
    assert not find_unresolved_requires(collector_names, all_fact_subsets)

    # Complex success case
    collector_names = ['os_version', 'os_family', 'os_major_version']
    all_fact_subsets['os_version'] = [FakeCollectorClass1]
    all_fact_subsets['os_family'] = [FakeCollectorClass2]
    all_fact_subsets['os_major_version'] = [FakeCollectorClass3]
    assert not find_unresolved_requires(collector_names, all_fact_subsets)

    # One failure case

# Generated at 2022-06-13 00:30:43.538394
# Unit test for function get_collector_names
def test_get_collector_names():
    all_collector_names = ['a', 'b', 'c']
    alias_map = defaultdict(set)
    alias_map['x'].update(['a'])

    # when all is listed, we need all
    assert get_collector_names(gather_subset=['all'], valid_subsets=all_collector_names) == set(all_collector_names)

    # not listing all should not give us all
    assert get_collector_names(gather_subset=[], valid_subsets=all_collector_names) == set()

    # when min is listed, we need the min

# Generated at 2022-06-13 00:30:52.613383
# Unit test for function get_collector_names
def test_get_collector_names():
    # input data
    list_valid_subsets = ['a', 'b']
    list_minimal_gather_subset = ['c']
    list_gather_subset = ['d']
    aliases_map = defaultdict(set)
    aliases_map['d'].update(['a'])

    # expected output
    expected_output = set(['d', 'a'])

    # actual output
    actual_output = get_collector_names(list_valid_subsets, list_minimal_gather_subset, list_gather_subset, aliases_map)

    # assert
    assert(actual_output == expected_output)



# Generated at 2022-06-13 00:30:55.736183
# Unit test for function collector_classes_from_gather_subset
def test_collector_classes_from_gather_subset():
    '''already tested, use list for doc purposes'''
    # _collector_classes_from_gather_subset(all_collector_classes=None,
    #                                      valid_subsets=None,
    #                                      minimal_gather_subset=None,
    #                                      gather_subset=None,
    #                                      gather_timeout=None,
    #                                      platform_info=None):



# Generated at 2022-06-13 00:31:06.098527
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    collector_names = set([
        'c1',
        'c2',
        'c3',
    ])

    all_fact_subsets = {
        'c1': [MockCollector('c1', ['c4'])],
        'c2': [MockCollector('c2', ['c3'])],
        'c3': [MockCollector('c3', ['c1'])],
        'c4': [MockCollector('c4', [])],
    }

    unresolved = find_unresolved_requires(collector_names, all_fact_subsets)
    assert len(unresolved) == 1
    assert unresolved == set(['c3'])



# Generated at 2022-06-13 00:31:14.464763
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    class Test1(BaseFactCollector):
        _fact_ids = set(['f1'])
        name = 'test1'

    class Test2(BaseFactCollector):
        _fact_ids = set(['f2'])
        name = 'test2'

    class Test3(BaseFactCollector):
        _fact_ids = set(['f3'])
        name = 'test3'

    class Test4(BaseFactCollector):
        _fact_ids = set(['f4'])
        name = 'test4'

    class Test5(BaseFactCollector):
        _fact_ids = set(['f5'])
        name = 'test5'

    class Test6(BaseFactCollector):
        _fact_ids = set(['f1'])
        name = 'test6'

   

# Generated at 2022-06-13 00:31:24.604095
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    all_fact_subsets = {
        'collector_1': [FactCollector1],
        'collector_2': [FactCollector2],
        'collector_3': [FactCollector3],
        'collector_4': [FactCollector4],
    }

    # Test collector_1's dependency, collector_2, is unresolved
    collector_names = ['collector_1', ]
    try:
        unresolved_collector_names = find_unresolved_requires(collector_names,
                                                              all_fact_subsets)
    except CollectorNotFoundError:
        assert False, "'collector_1' is not found!"
    assert len(unresolved_collector_names) == 1, \
        "Should have exactly 1 unresolved collector"

# Generated at 2022-06-13 00:31:33.136377
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    # Define some mock collectors and test data
    class A(BaseFactCollector):
        _fact_ids = set(['mock_a'])
        name = 'mock_a'
    class B(BaseFactCollector):
        _fact_ids = set(['mock_b'])
        name = 'mock_b'
    class C(BaseFactCollector):
        _fact_ids = set(['mock_c'])
        name = 'mock_c'
        required_facts = set(['mock_a'])
    class D(BaseFactCollector):
        _fact_ids = set(['mock_d'])
        name = 'mock_d'
    class E(BaseFactCollector):
        _fact_ids = set(['mock_e'])

# Generated at 2022-06-13 00:31:59.801777
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    all_fact_subsets = {
        'f1': [object()],
        'f2': [object()],
        'f3': [object()],
        'f4': [object()],
        'f5': [object()],
        'f6': [object()],
    }

    def _unresolved(collector_names):
        unresolved = find_unresolved_requires(collector_names, all_fact_subsets)
        return list(unresolved)

    assert _unresolved(['f1']) == []
    assert _unresolved(['f1', 'f2']) == []
    assert _unresolved(['f1', 'f3']) == ['f2']
    assert _unresolved(['f1', 'f2', 'f3']) == []
   

# Generated at 2022-06-13 00:32:06.469485
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    # Create Collector subclass that has a list of required facts
    class _TestCollector(BaseFactCollector):
        required_facts = ['required_fact_name']

    # Create a map of all facts
    all_fact_subsets = {
        'fact_name_1': [_TestCollector],
        'fact_name_2': [_TestCollector],
        'required_fact_name': [_TestCollector],
    }

    return find_unresolved_requires(['fact_name_1', 'fact_name_2'], all_fact_subsets)



# Generated at 2022-06-13 00:32:15.075853
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    all_fact_subsets = {
        'collector1': [CollectorClass(['collector3'])],
        'collector2': [CollectorClass([])],
        'collector3': [CollectorClass(['collector2'])],
    }

    # Test a case where there are no unresolved requires
    collector_names = ['collector1']
    unresolved = find_unresolved_requires(collector_names, all_fact_subsets)
    assert len(unresolved) == 0

    # Test a case where collector3 has an unresolved require
    collector_names = ['collector3']
    unresolved = find_unresolved_requires(collector_names, all_fact_subsets)
    assert len(unresolved) == 1
    assert 'collector2' in unresolved

    # Test a case where collector

# Generated at 2022-06-13 00:32:24.743472
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    import types
    from ansible.module_utils.facts.collectors import collect_platform_facts
    from ansible.module_utils.facts import timeout
    from ansible.module_utils._text import to_text
    from ansible.module_utils.facts.system.distribution import DistributionFactCollector

    # A fake platform info
    class FakePlatformInfo(object):
        def __init__(self):
            self.system = 'Linux'
            self.machine = 'x86_64'
            self.release = '5.11.0-RELEASE'
            self.distribution = 'FreeBSD'
            self.distribution_version = '11.0'
            self.distribution_release = 'RELEASE'

    platform_info = FakePlatformInfo()
    # Get all the fact_ids of the collectors
    fact_id

# Generated at 2022-06-13 00:32:35.314617
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    from ansible.module_utils.facts import platform
    from ansible.module_utils.facts.collectors import network

    fact_id_to_collector_map, aliases_map = build_fact_id_to_collector_map(
        find_collectors_for_platform([platform.LinuxDistribution,
                                      network.Hardware],
                                     [{'distribution': 'CentOS'}, {'system': 'Linux'}]))

    assert 'distribution' in fact_id_to_collector_map
    assert len(fact_id_to_collector_map['distribution']) == 1
    assert 'hardware' in fact_id_to_collector_map
    assert len(fact_id_to_collector_map['hardware']) == 1


# Generated at 2022-06-13 00:32:44.649226
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    from ansible.module_utils.facts.collector import BaseFactCollector

    class Collector1(BaseFactCollector):
        _fact_ids = {'fact_id_1'}
        name = 'collector_1'

    class Collector2(BaseFactCollector):
        _fact_ids = {'fact_id_2'}
        name = 'collector_2'

    fact_id_to_collector_map, aliases_map = build_fact_id_to_collector_map([Collector1, Collector2])


# Generated at 2022-06-13 00:32:52.015620
# Unit test for function select_collector_classes
def test_select_collector_classes():
    import unittest

    class Collector1(BaseFactCollector):
        name = 'a'
        required_facts = frozenset()
        def __init__(self, *args, **kwargs):
            super(Collector1, self).__init__(*args, **kwargs)
    class Collector2(BaseFactCollector):
        name = 'b'
        required_facts = frozenset()
        def __init__(self, *args, **kwargs):
            super(Collector2, self).__init__(*args, **kwargs)
    class Collector3(BaseFactCollector):
        name = 'c'
        required_facts = frozenset()
        def __init__(self, *args, **kwargs):
            super(Collector3, self).__init__(*args, **kwargs)
   

# Generated at 2022-06-13 00:33:00.867549
# Unit test for function select_collector_classes
def test_select_collector_classes():
    ''' test for function select_collector_classes '''
    all_fact_subsets = {'test1': ['test1a', 'test1b', 'test1b'],
                        'test2': ['test2a', 'test2b'],
                        'test3': ['test3a', 'test3b']}

    selected_collector_classes = select_collector_classes(['test1', 'test2', 'test1'],
                                                          all_fact_subsets)
    assert selected_collector_classes == ['test1a', 'test1b', 'test2a', 'test2b']



# Generated at 2022-06-13 00:33:11.541980
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    collectors = [
        # classname, name, aliases
        ('CollectorA', 'a', ['a1', 'a2']),
        ('CollectorB', 'b', ['b1', 'b2']),
        ('CollectorC', 'c', ['c1', 'c2']),
        ('CollectorD', 'd', ['d1', 'd2']),
    ]

    for classname, primary_name, aliases in collectors:
        fakecollector_class = type(classname, (object, ), {
            'name': primary_name,
            '_fact_ids': set(aliases + [primary_name])
        })
        all_collector_classes = []
        all_collector_classes.append(fakecollector_class)
        fact_id_to_collector_map, _ = build_fact

# Generated at 2022-06-13 00:33:23.310410
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    class a(BaseFactCollector):
        name = 'a'
        _fact_ids = ['1', '2']

    class b(BaseFactCollector):
        name = 'b'
        _fact_ids = ['2', '3']

    class c(BaseFactCollector):
        name = 'c'
        _fact_ids = ['3', '4']

    result = build_fact_id_to_collector_map(set([a, b, c]))

# Generated at 2022-06-13 00:33:46.200629
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    from ansible_collections.notmintest.not_a_real_collection.plugins.module_utils.facts.collectors import (
        all_fact_subsets
    )
    # This test is in this file, rather than test_utils.py, because we do not want
    # to add a dep on 'all_fact_subsets' unless we really have to

    # Base case:
    assert find_unresolved_requires(['all'], all_fact_subsets) == set()

    # Add a requirement that is not resolved
    assert find_unresolved_requires(['all', 'sudo'], all_fact_subsets) == set(['sudo'])

    # Add a requirement that is resolved
    assert find_unresolved_requires(['all', 'system'], all_fact_subsets) == set()




# Generated at 2022-06-13 00:33:55.317795
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    class FakeCollector(object):
        name = 'a'
        required_facts = set()

    class FakeCollectorRequiresA(object):
        name = 'b'
        required_facts = set(['a'])

    class FakeCollectorRequiresB(object):
        name = 'c'
        required_facts = set(['b'])

    class FakeCollectorRequiresC(object):
        name = 'd'
        required_facts = set(['c'])

    class FakeCollectorRequiresD(object):
        name = 'e'
        required_facts = set(['d'])

        # FakeCollectorRequiresD does not provide a means to resolve itself, so
        # find_unresolved_requires() should raise an error
    class FakeCollectorRequiresE(object):
        name = 'f'
        required_facts

# Generated at 2022-06-13 00:34:01.558365
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    class Collector1(BaseFactCollector):
        name = 'collector1'
        _fact_ids = frozenset(['primary1', 'alias1'])

    class Collector2(BaseFactCollector):
        name = 'collector2'
        _fact_ids = frozenset(['primary2', 'alias2'])

    class Collector3(BaseFactCollector):
        name = 'collector3'
        _fact_ids = frozenset(['primary3', 'alias3'])

    class Collector4(BaseFactCollector):
        name = 'collector4'
        _fact_ids = frozenset(['primary4', 'alias4'])


# Generated at 2022-06-13 00:34:09.385561
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    collector_names = ['fact_b', 'fact_e', 'fact_a', 'fact_c']
    all_fact_subsets = {
        'fact_b': [BaseFactCollector],
        'fact_e': [BaseFactCollector],
        'fact_a': [BaseFactCollector],
        'fact_c': [BaseFactCollector],
    }

    assert find_unresolved_requires(collector_names, all_fact_subsets) == set(['fact_b'])

    collector_names = ['fact_b', 'fact_e', 'fact_a', 'fact_c']