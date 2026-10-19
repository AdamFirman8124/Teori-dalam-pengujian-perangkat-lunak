

# Generated at 2022-06-13 00:24:31.075236
# Unit test for function get_collector_names
def test_get_collector_names():
    # assert get_collector_names(['all']) == set('all')
    assert get_collector_names(set(['all']), ['all']) == set(['all'])
    assert get_collector_names(set(['min']), ['all']) == set(['all'])
    assert get_collector_names(set(['all']), ['min']) == set(['min'])
    assert get_collector_names(set(['min']), ['min']) == set(['min'])
    assert get_collector_names(set(['min']), ['min', '!min']) == set(['min'])
    assert get_collector_names(set(['min']), ['min', '!all']) == set(['min'])


# Generated at 2022-06-13 00:24:38.133537
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    collectors = [
        FakeCollector(name='first', required_facts=['third']),
        FakeCollector(name='second', required_facts=['first']),
        FakeCollector(name='third'),
    ]
    all_fact_subsets = {c.name: [c] for c in collectors}
    # all should have no unresolved requires
    assert find_unresolved_requires(['first', 'second', 'third'], all_fact_subsets) == set()
    # missing second should have unresolved 'first'
    assert find_unresolved_requires(['first', 'third'], all_fact_subsets) == {'first'}
    # missing first should have unresolved first/second

# Generated at 2022-06-13 00:24:45.992570
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    from ansible.module_utils.facts import collector
    import ansible.module_utils.facts.system.linux.distro as linux_distro
    import ansible.module_utils.facts.system.linux.distribution as linux_distribution
    import ansible.module_utils.facts.network.linux as linux_network

    fact_id_to_collector_map, aliases_map = build_fact_id_to_collector_map(
        [collector.BaseFactCollector, linux_distro.DistroCollector, linux_distribution.DistributionCollector, linux_network.LinuxNetworkCollector]
    )

    assert 'distribution' in fact_id_to_collector_map

# Generated at 2022-06-13 00:24:56.209705
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    def make_collector_name_to_required(dict_of_sets):
        collector_name_to_required_facts = {}
        for fact_name, fact_set in dict_of_sets.items():
            class FakeClass:
                name = fact_name
                required_facts = fact_set
            collector_name_to_required_facts[fact_name] = [FakeClass]
        return collector_name_to_required_facts

    all_fact_subsets = make_collector_name_to_required({
        'a': set(),
        'b': set(),
        'c': set(),
        'd': set(),
    })

    assert find_unresolved_requires(['a'], all_fact_subsets) == set()

    all_fact_subsets = make_collector_name_to

# Generated at 2022-06-13 00:25:07.304335
# Unit test for function select_collector_classes
def test_select_collector_classes():
    """
    Test function select_collector_classes
    """
    class CollectorFoo:
        name = 'foo'
        _fact_ids = set(['foo'])
    class CollectorBar:
        name = 'bar'
        _fact_ids = set(['bar'])

    collector_names = ['foo', 'bar', 'foo']
    all_fact_subsets = {
        'foo': [CollectorFoo],
        'bar': [CollectorBar],
    }
    assert select_collector_classes(collector_names, all_fact_subsets) == [CollectorFoo, CollectorBar]
    collector_names = ['bar', 'foo', 'foo']
    assert select_collector_classes(collector_names, all_fact_subsets) == [CollectorBar, CollectorFoo]
    collector

# Generated at 2022-06-13 00:25:18.813798
# Unit test for function build_dep_data
def test_build_dep_data():
    from ansible.module_utils.facts import collector
    from ansible.module_utils.facts.collector.default import Default
    from ansible.module_utils.facts.collector.dns import Dns
    import pytest
    name = 'default'
    default_collector = collector.get_collector_class_by_name(name)
    name2 = 'dns'
    dns_collector = collector.get_collector_class_by_name(name2)
    expected_dep_map = {'default': {'dns'}, 'dns': set()}
    dep_map = build_dep_data(['default', 'dns'], {'default': [default_collector], 'dns': [dns_collector]})

# Generated at 2022-06-13 00:25:23.491088
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    # given
    collector_names = frozenset(['nonsense', 'cpu', 'cpu_custom'])
    all_fact_subsets = {
        'cpu': [SomeCollectorClass],
        'cpu_custom': [SomeCollectorClass2],
        'nonsense': [SomeCollectorClass3]
    }
    # exercise
    unresolved = find_unresolved_requires(collector_names, all_fact_subsets)
    # assert
    assert unresolved == frozenset(['other_fact'])



# Generated at 2022-06-13 00:25:30.846988
# Unit test for function get_collector_names
def test_get_collector_names():
    assert get_collector_names(gather_subset=['all'],
                               valid_subsets=frozenset(('all', 'network'))) == frozenset(('network',)), \
        'get_collector_names(gather_subset=["all"], valid_subsets=frozenset(("all", "network"))) == frozenset(("network",))'

# Generated at 2022-06-13 00:25:41.887698
# Unit test for function tsort

# Generated at 2022-06-13 00:25:52.793513
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    fact_ids = ['a', 'b', 'c']
    all_fact_subsets = defaultdict(list)
    # add factcollectors for a and c
    for fact_id in fact_ids:
        fact_collector = None
        fact_collector = type('MockCollector', (BaseFactCollector, ), {
            'name': fact_id,
            'required_facts': set(),
            '_fact_ids': set([fact_id]),
            'platform_match': staticmethod(lambda *args, **kwargs: True)
        })
        all_fact_subsets[fact_id].append(fact_collector)
    # add factcollector for b with requires_facts=a

# Generated at 2022-06-13 00:26:09.680083
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    from ansible_collections.ansible.community.plugins.module_utils.facts.collector.platform import PlatformFactCollector
    from ansible_collections.ansible.community.plugins.module_utils.facts.collector.network import NetworkFactCollector
    from ansible_collections.ansible.community.plugins.module_utils.facts.collector.pip import PipFactCollector

    collectors_for_platform = [PlatformFactCollector, NetworkFactCollector, PipFactCollector]

    fact_id_to_collector_map, aliases_map = build_fact_id_to_collector_map(collectors_for_platform)

    assert isinstance(fact_id_to_collector_map, defaultdict)
    assert isinstance(aliases_map, defaultdict)
    assert fact_id_to_collector

# Generated at 2022-06-13 00:26:15.938622
# Unit test for function select_collector_classes
def test_select_collector_classes():
    collector_names = set(['first', 'second', 'third'])
    all_fact_subsets = {'first': [1],
                        'second': [2, 3],
                        'third': [4]}
    ret = select_collector_classes(collector_names, all_fact_subsets)
    assert sorted(ret) == [1, 2]
    assert sorted(seen_collector_classes) == sorted(ret)


# Generated at 2022-06-13 00:26:23.457212
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    class TestCollector(BaseFactCollector):
        name = 'TestCollector'
        _fact_ids = set()

        @classmethod
        def platform_match(cls, platform_info):
            if platform_info.get('system', None) == cls._platform:
                return cls
            return None

    fact_id_to_collector_map, aliases_map = build_fact_id_to_collector_map([TestCollector, TestCollector])
    assert len(fact_id_to_collector_map['TestCollector']) == 2
    assert TestCollector in fact_id_to_collector_map['TestCollector']



# Generated at 2022-06-13 00:26:35.897855
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    from ansible.module_utils.facts.processor.linux.uptime import Uptime
    from ansible.module_utils.facts.processor.linux.pkg_mgr import PkgMgr

    collectors_for_platform = set([Uptime, PkgMgr])
    fact_id_to_collector_map, aliases_map = build_fact_id_to_collector_map(collectors_for_platform)

    # Uptime example
    assert len(fact_id_to_collector_map['uptime']) == 1
    assert fact_id_to_collector_map['uptime'][0] == Uptime
    # PkgMgr example
    assert len(fact_id_to_collector_map['pkg_mgr']) == 1
    assert fact_id_to_collector_

# Generated at 2022-06-13 00:26:45.389369
# Unit test for function get_collector_names
def test_get_collector_names():
    # also tests get_collector_names's behavior when called with missing argumets...
    assert set() == get_collector_names()

    assert set(['all']) == get_collector_names(gather_subset=['all'])

    assert set(['min']) == get_collector_names(gather_subset=['min'])

    assert set(['all']) == get_collector_names(gather_subset=['all'],
                                               minimal_gather_subset=set(['min']))

    # 'network' or 'interfaces' is one subset
    assert set(['min', 'network']) == get_collector_names(gather_subset=['network'],
                                                          minimal_gather_subset=set(['min']))

    assert set

# Generated at 2022-06-13 00:26:54.639907
# Unit test for function get_collector_names
def test_get_collector_names():
    assert get_collector_names() == frozenset(['all'])
    assert get_collector_names(frozenset(['all']), frozenset()) == frozenset(['all'])
    assert get_collector_names(frozenset(['all']), frozenset(['all'])) == frozenset(['all'])
    assert get_collector_names(frozenset(['foo', 'bar']), frozenset(['bar'])) == frozenset(['bar'])
    assert get_collector_names(frozenset(['foo', 'bar']), gather_subset=['foo']) == frozenset(['foo'])
    assert get_collector_names(gather_subset=['foo', '!all']) == frozenset(['foo'])


# Generated at 2022-06-13 00:27:06.236719
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    from ansible.module_utils.facts.namespace import FactNamespace
    some_collector = [BaseFactCollector(namespace=FactNamespace('ansible'))]
    some_collector[0].required_facts = {'a', 'b'}
    some_collector[0].name = 'A'
    some_collector[0]._fact_ids.add('B')

    some_collector.append(BaseFactCollector(namespace=FactNamespace('ansible')))
    some_collector[1].required_facts = {'c', 'd'}
    some_collector[1].name = 'C'
    some_collector[1]._fact_ids.add('D')

    fact_id_to_collector_map, _aliases_map = build_fact_id_to

# Generated at 2022-06-13 00:27:14.565441
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    class CollectorA(BaseFactCollector):
        _fact_ids = {'a'}
        required_facts = set()

    class CollectorB(BaseFactCollector):
        _fact_ids = {'b'}
        required_facts = {'x'}

    class CollectorX(BaseFactCollector):
        _fact_ids = {'x'}
        required_facts = set()

    class CollectorY(BaseFactCollector):
        _fact_ids = {'y'}
        required_facts = set()

    collector_classes = [CollectorA, CollectorB, CollectorX, CollectorY]
    all_fact_subsets = defaultdict(list)
    for collector_class in collector_classes:
        all_fact_subsets[collector_class.name].append(collector_class)
        all_fact

# Generated at 2022-06-13 00:27:24.721143
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    from ansible.module_utils.facts import collector
    a = collector.BaseFactCollector
    a._fact_ids = ['a', 'b']
    b = collector.BaseFactCollector
    b._fact_ids = ['c']

    fact_id_to_collector_map, aliases_map = build_fact_id_to_collector_map([a, b])
    assert fact_id_to_collector_map == {'a': [a], 'b': [a], 'c': [b]}
    assert aliases_map == defaultdict(set, {'a': {'a', 'b'}, 'b': {'a', 'b'}, 'c': {'c'}})



# Generated at 2022-06-13 00:27:33.011419
# Unit test for function build_dep_data
def test_build_dep_data():

    class MockCollector:
        def __init__(self, name=None, required_facts=None):
            self.name = name
            self.required_facts = required_facts or set()

        def platform_match(self, *args, **kwargs):
            return True

    all_fact_subsets = {'a': [MockCollector(name='a', required_facts=set(['d']))],
                        'b': [MockCollector(name='b', required_facts=set())],
                        'c': [MockCollector(name='c', required_facts=set(['d']))]}
    dep_map = build_dep_data(collector_names=['a', 'b', 'c'],
                             all_fact_subsets=all_fact_subsets)


# Generated at 2022-06-13 00:27:49.523602
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    import pytest

    class MyCollector(BaseFactCollector):
        _fact_ids = {'my_collector'}
        name = 'my_collector'

        required_facts = {'other_collector'}

    class OtherCollector(BaseFactCollector):
        _fact_ids = {'other_collector'}
        name = 'other_collector'

    all_fact_subsets = defaultdict(list)
    all_fact_subsets['my_collector'].append(MyCollector)
    all_fact_subsets['other_collector'].append(OtherCollector)

    unresolved = find_unresolved_requires(set(['my_collector']), all_fact_subsets)
    assert unresolved == set(['other_collector'])



# Generated at 2022-06-13 00:27:58.518140
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    class _Collector(BaseFactCollector):
        name = 'testcollector'
        required_facts = set()

    class _Collector1(_Collector):
        name = 'testcollector1'
        required_facts = {'testcollector'}

    class _Collector2(_Collector):
        name = 'testcollector2'
        required_facts = {'testcollector'}

    all_fact_subsets = {
        'testcollector': [_Collector,],
        'testcollector1': [_Collector1,],
        'testcollector2': [_Collector2,],
    }

    unresolved = find_unresolved_requires(['testcollector2'], all_fact_subsets)
    assert 'testcollector1' in unresolved

    unresolved = find_unresolved_

# Generated at 2022-06-13 00:28:05.655479
# Unit test for function get_collector_names
def test_get_collector_names():
    # Arrange
    gather_subset = ['all']
    valid_subsets = frozenset(('min', 'network', 'hardware', 'virtual', 'pkg_mgr'))
    minimal_set = frozenset(('min',))
    aliases_map = {
        'network': set(('network',)),
        'hardware': set(('hardware', 'devices', 'dmi')),
        'virtual': set(('virtual',)),
        'pkg_mgr': set(('pkg_mgr',)),
    }
    # Act
    wanted_collector_names = get_collector_names(valid_subsets, minimal_set, gather_subset, aliases_map)
    # Assert

# Generated at 2022-06-13 00:28:10.641141
# Unit test for function build_dep_data
def test_build_dep_data():
    dep_map = build_dep_data(['a', 'b', 'c'], {'a': ['d'], 'b': ['a', 'e'], 'c': ['a']})
    assert dep_map == {'a': [], 'b': ['a', 'e'], 'c': ['a']}



# Generated at 2022-06-13 00:28:21.815636
# Unit test for function get_collector_names
def test_get_collector_names():
    # Setup aliases_map
    test_aliases_map = dict(
        hardware=frozenset(['devices', 'dmi']),
        network=frozenset(['interfaces', 'ipv4']),
    )

    # Test case 1
    test_valid_subsets = frozenset(['all', 'network', 'hardware'])
    test_minimal_gather_subset = frozenset(['network', 'hardware'])
    test_gather_subset = ['all']
    test_platform_info = dict(system='Generic', uname='Linux')

    expected_result = frozenset(['hardware', 'network'])

# Generated at 2022-06-13 00:28:27.372274
# Unit test for function build_dep_data
def test_build_dep_data():
    fact_dict = {}
    class Test:
        name = 'test'
        required_facts = set()

    dep_map = build_dep_data({'test'}, {'test': [Test]})
    assert dep_map['test'] == set()

    class TestDep:
        name = 'testdep'
        required_facts = ('test',)

    dep_map = build_dep_data({'test', 'testdep'}, {'test': [Test], 'testdep': [TestDep]})
    assert dep_map['testdep'] == {'test'}



# Generated at 2022-06-13 00:28:38.216461
# Unit test for function get_collector_names
def test_get_collector_names():
    # pylint: disable=redefined-outer-name, unused-argument
    gs = get_collector_names
    (valid, min_valid, aliases) = gs.func_defaults[0:3]
    assert gs(valid) == gs.func_defaults[0], 'default is to return all facts'
    assert gs(valid, minimal_gather_subset=('min')) == gs.func_defaults[0], 'min facts are always returned'
    assert gs(valid, gather_subset=['all']) == gs.func_defaults[0], 'all facts is all facts'
    assert gs(valid, gather_subset=['min']) == set(('min',))

# Generated at 2022-06-13 00:28:49.684254
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    # All values with the same requires should match
    assert find_unresolved_requires(['all'], {'foo': [object], 'bar': [object]}) == set()
    assert find_unresolved_requires(['all', 'foo'], {'foo': [object], 'bar': [object]}) == set()
    assert find_unresolved_requires(['all', 'foo', 'bar'], {'foo': [object], 'bar': [object]}) == set()

    # All values without the same requires should fail
    assert find_unresolved_requires(['bar'], {'foo': [object], 'bar': [object]}) == {'foo'}
    assert find_unresolved_requires(['bar', 'foo'], {'foo': [object], 'bar': [object]}) == set()

    #

# Generated at 2022-06-13 00:28:53.382312
# Unit test for function build_dep_data
def test_build_dep_data():
    dep_map = {}
    dep_map['collector_name'] = {'dep1', 'dep2'}
    assert build_dep_data(['collector_name'], {'collector_name': []}) == dep_map



# Generated at 2022-06-13 00:29:00.723597
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():

    class TestCollector(BaseFactCollector):
        _fact_ids = set(['collector_1'])
        name = 'collector'

    class TestCollector2(BaseFactCollector):
        _fact_ids = set(['collector_2'])
        name = 'collector'

    test = [TestCollector, TestCollector2]

    fact_id_to_collector_map, aliases_map = build_fact_id_to_collector_map(test)

    assert fact_id_to_collector_map['collector_1'][0] == TestCollector
    assert fact_id_to_collector_map['collector_2'][0] == TestCollector2
    assert fact_id_to_collector_map['collector'][0] == TestCollector
    assert fact

# Generated at 2022-06-13 00:29:18.762085
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    class A(BaseFactCollector):
        required_facts = ['b']
        name = 'a'

    class B(BaseFactCollector):
        required_facts = []
        name = 'b'

    class C(BaseFactCollector):
        required_facts = ['a']
        name = 'c'

    class D(BaseFactCollector):
        required_facts = ['a']
        name = 'd'

    class E(BaseFactCollector):
        required_facts = ['d', 'c']
        name = 'e'

    all_fact_subsets = {
        'a': [A],
        'b': [B],
        'c': [C],
        'd': [D],
        'e': [E],
    }

    # Ensure all classes in all_fact_subsets are properly ordered

# Generated at 2022-06-13 00:29:28.304337
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    class MockFactCollector(BaseFactCollector):
        _fact_ids = set(['collector_id'])

        def collect(self, module=None, collected_facts=None):
            test_collector_dict = {}
            test_collector_dict['test_key'] = 'test_value'
            return test_collector_dict

        @classmethod
        def platform_match(cls, platform_info):
            return cls

    collector_for_platform = [MockFactCollector]
    fact_id_to_collector_map, aliases_map = build_fact_id_to_collector_map(collector_for_platform)
    assert set(fact_id_to_collector_map.keys()) == set(['collector_id', 'mock'])
    assert fact_id_to

# Generated at 2022-06-13 00:29:37.497640
# Unit test for function tsort
def test_tsort():
   assert(tsort({1: []})[0][0] == 1)
   assert(tsort({1: [2], 2: []})[0][0] == 1)
   assert(tsort({1: [2], 2: [1]})[0][0] == 2)
   assert(tsort({1: [2], 2: [3], 3: []})[0][0] == 3)
   assert(tsort({1: [2], 2: [3], 3: [4], 4: []})[0][0] == 4)
# EndUnit test for function tsort



# Generated at 2022-06-13 00:29:46.248257
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    class TestCollector_1(BaseFactCollector):
        name = 'test'
        _fact_ids = ['test_1', 'test_2']
    class TestCollector_2(BaseFactCollector):
        name = 'test_2'
        _fact_ids = ['test_2', 'test_3']

    collectors_for_platform = [TestCollector_1, TestCollector_2]
    expected = {'test_1': [TestCollector_1], 'test_2': [TestCollector_1, TestCollector_2],
                'test_3': [TestCollector_2], 'test': [TestCollector_1, TestCollector_2]}
    assert build_fact_id_to_collector_map(collectors_for_platform)[0] == expected


# Generated at 2022-06-13 00:29:57.541439
# Unit test for function build_fact_id_to_collector_map

# Generated at 2022-06-13 00:30:09.887836
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    facts_subset = defaultdict(list)
    class A(BaseFactCollector):
        name = 'a'
        required_facts = set()
    class B(BaseFactCollector):
        name = 'b'
        required_facts = set(['a'])
    class C(BaseFactCollector):
        name = 'c'
        required_facts = set(['b'])

    facts_subset['a'].append(A)
    facts_subset['b'].append(B)
    facts_subset['c'].append(C)

    unresolved = find_unresolved_requires(['b', 'c'], facts_subset)
    assert unresolved == set(['a'])

    unresolved = find_unresolved_requires(['a', 'c'], facts_subset)
    assert unresolved

# Generated at 2022-06-13 00:30:14.579753
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    from ansible.module_utils.facts import processor

    assert find_unresolved_requires(['all'], processor.all_fact_subsets) == set()
    assert find_unresolved_requires(['all_network'], processor.all_fact_subsets) == set()
    assert find_unresolved_requires(['all', 'all_network'], processor.all_fact_subsets) == set()

    assert not find_unresolved_requires(['!all'], processor.all_fact_subsets)
    assert not find_unresolved_requires(['!all_network'], processor.all_fact_subsets)
    assert find_unresolved_requires(['!all', '!all_network'], processor.all_fact_subsets) == set()


# Generated at 2022-06-13 00:30:25.450133
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    class FakeCollector(BaseFactCollector):
        pass
    FakeCollector._fact_ids = set(['fake1', 'fake2'])
    FakeCollector.name = 'fake'

    class FakeCollector2(BaseFactCollector):
        pass
    FakeCollector2._fact_ids = set(['fake3', 'fake4'])
    FakeCollector2.name = 'fake2'

    fact_id_to_collector_map, aliases_map = build_fact_id_to_collector_map(
        [FakeCollector, FakeCollector2])


# Generated at 2022-06-13 00:30:35.327420
# Unit test for function select_collector_classes
def test_select_collector_classes():
    class AA:
        _fact_ids = set(['a'])

    class BB:
        _fact_ids = set(['b'])

    class CC:
        _fact_ids = set(['c'])

    class DD:
        _fact_ids = set(['d'])

    class EE:
        _fact_ids = set(['e'])

    class FF:
        _fact_ids = set(['f'])

    all_facts = {'aa': [AA],
                 'bb': [BB],
                 'cc': [CC],
                 'dd': [DD],
                 'ee': [EE],
                 'ff': [FF],
                 }

    selected = select_collector_classes(['bb', 'dd', 'aa'], all_facts)

# Generated at 2022-06-13 00:30:46.556196
# Unit test for function select_collector_classes
def test_select_collector_classes():
    class Collector1(BaseFactCollector):
        name='collector1'
        _fact_ids = set(['collector1'])
    class Collector1_1(BaseFactCollector):
        name='collector1'
        _fact_ids = set(['collector1.1'])
    class Collector2(BaseFactCollector):
        name='collector2'
        _fact_ids = set(['collector2'])
    all_fact_subsets = {
        'collector1': [Collector1, Collector1_1, Collector2],
        'collector2': [Collector2],
    }
    collector_names = ['collector1', 'collector2', 'collector3']
    selected_collector_classes = select_collector_classes(collector_names, all_fact_subsets)

# Generated at 2022-06-13 00:31:35.433874
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    collector_names = ['cpu', 'virtual', 'ohai', 'hardware']
    unresolved = find_unresolved_requires(collector_names, all_fact_subsets)
    assert len(unresolved) == 0
    collector_names = ['cpu', 'virtual', 'ohai', 'hardware', 'network']
    unresolved = find_unresolved_requires(collector_names, all_fact_subsets)
    assert len(unresolved) == 0
    collector_names = ['cpu', 'virtual', 'ohai', 'hardware', 'network', 'ansible_network']
    unresolved = find_unresolved_requires(collector_names, all_fact_subsets)
    assert len(unresolved) == 0

# Generated at 2022-06-13 00:31:45.784023
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    class F1(BaseFactCollector):
        name = 'F1'
        required_facts = set()
    class F2(BaseFactCollector):
        name = 'F2'
        required_facts = set(['F3'])
    class F3(BaseFactCollector):
        name = 'F3'
        required_facts = set()

    a = F1()
    b = F2()
    c = F3()
    all_fact_subsets = {a.name: [a], b.name: [b], c.name: [c]}
    unresolved = find_unresolved_requires(['F1', 'F2'], all_fact_subsets)
    assert len(unresolved) == 1
    assert 'F3' in unresolved



# Generated at 2022-06-13 00:31:56.641607
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    from ansible.module_utils.facts.collectors.base import BaseFactCollector

    class CollectorFoo(BaseFactCollector):
        name = 'foo'
        required_facts = {'bar'}

    class CollectorBar(BaseFactCollector):
        name = 'bar'
        required_facts = {'baz'}

    class CollectorBaz(BaseFactCollector):
        name = 'baz'
        required_facts = {}

    class CollectorQux(BaseFactCollector):
        name = 'qux'
        required_facts = {}

    class CollectorNotFound(BaseFactCollector):
        name = 'not found'
        required_facts = {}


# Generated at 2022-06-13 00:32:06.875592
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    class Dep1(BaseFactCollector):
        _fact_ids = set(['dep1'])
        name = 'dep1'

    class Dep2(BaseFactCollector):
        _fact_ids = set(['dep2'])
        name = 'dep2'

    class Primary(BaseFactCollector):
        _fact_ids = set(['primary1', 'primary2', 'primary3'])
        name = 'primary'

    result = build_fact_id_to_collector_map([Dep1, Dep2, Primary])

    # result[0] is the dict
    assert 'dep1' in result[0]
    assert result[0]['dep1'][0] == Dep1

    assert 'primary1' in result[0]
    assert result[0]['primary1'][0] == Primary

    #

# Generated at 2022-06-13 00:32:15.409893
# Unit test for function build_dep_data
def test_build_dep_data():
    collector_names = ['a', 'b', 'c', 'd']
    all_fact_subsets = {'a': [], 'b': [], 'c': [], 'd': []}
    class A():
        name = 'a'
        required_facts = set()
    class B():
        name = 'b'
        required_facts = set()
    class C():
        name = 'c'
        required_facts = set('a')
    class D():
        name = 'd'
        required_facts = set('b', 'c')
    all_fact_subsets = {'a': [A()], 'b': [B()], 'c': [C(), C()], 'd': [D()]}

# Generated at 2022-06-13 00:32:24.825398
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    def test_all_fact_subsets(fact_name):
        # returns a fact class that lists fact_name as a requires_facts.
        class fact_class:
            required_facts = (fact_name,)
        return [fact_class]

    all_fact_subsets = {
        'fact1': test_all_fact_subsets('fact2'),
        'fact2': test_all_fact_subsets('fact1'),
    }

    # Should raise CycleFoundInFactDeps
    try:
        find_unresolved_requires({'fact1'}, all_fact_subsets)
    except CycleFoundInFactDeps:
        pass
    else:
        assert False, 'Expected UnresolvedFactDep error when fact collector depends on itself.'



# Generated at 2022-06-13 00:32:35.314402
# Unit test for function build_dep_data
def test_build_dep_data():
    class FakeCollector:
        def __init__(self, name, reqs):
            self.name = name
            self.required_facts = reqs
    c1 = FakeCollector('first', set(['test1', 'test2']))
    c2 = FakeCollector('second', set(['test1', 'test2']))
    c3 = FakeCollector('third', set(['test2']))
    c4 = FakeCollector('fourth', set(['test3']))
    fact_id_to_collector_map = {
        'first': [c1],
        'second': [c2],
        'third': [c3],
        'fourth': [c4],
    }

# Generated at 2022-06-13 00:32:44.651043
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    from ansible.module_utils.facts import default
    from ansible.module_utils.facts.collector import GenericFactCollector

    class TestCollector(GenericFactCollector):
        name = 'test'
        _fact_ids = set(['test1', 'test2'])
        required_facts = set()

    class TestCollector2(GenericFactCollector):
        name = 'test2'
        _fact_ids = set(['test3'])
        required_facts = set()

    fact_id_to_collector_map, aliases_map = build_fact_id_to_collector_map([TestCollector, TestCollector2])

    def test_aliases():
        assert 'test1' in aliases_map['test']
        assert 'test2' in aliases_map['test']

# Generated at 2022-06-13 00:32:48.639781
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    # stub collector classes that have a required fact
    class Collector1:
        required_facts = ['fake_fact_1']
    class Collector2:
        required_facts = ['fake_fact_2']
    class Collector3:
        required_facts = ['fake_fact_3']
    all_fact_subsets = {
        'fake_fact_1': [Collector1],
        'fake_fact_2': [Collector2],
        'fake_fact_3': [Collector3]
    }
    collector_names = ['fake_fact_1', 'fake_fact_2']

    # check that returning unresolved fact names is correct
    assert find_unresolved_requires(collector_names, all_fact_subsets) == set(['fake_fact_3'])

    # add Collector3's required fact to collector_

# Generated at 2022-06-13 00:32:55.464500
# Unit test for function select_collector_classes
def test_select_collector_classes():
    collector_names = ['all', '!network']

    all_fact_subsets = {
        'all': [BaseFactCollector, BaseFactCollector],
        'network': [BaseFactCollector, BaseFactCollector]
    }

    assert select_collector_classes(collector_names, all_fact_subsets) == [BaseFactCollector, BaseFactCollector]



# Generated at 2022-06-13 00:33:24.818567
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    from ansible.module_utils.facts.collector.fallback import Fallback

    all_fact_subsets = {
        'test1': [],
        'test2': [],
        'test3': [],
        'test4': [],
        'test5': [],
        'test6': [],
    }
    collector_names = ['test1', 'test2', 'test3', 'test4', 'test5', 'test6']
    unresolved = set(find_unresolved_requires(collector_names, all_fact_subsets))
    assert unresolved == set()

    collector_names = ['test1', 'test2', 'test3', 'test4', 'test5']
    unresolved = set(find_unresolved_requires(collector_names, all_fact_subsets))
    assert unresolved

# Generated at 2022-06-13 00:33:33.234051
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    collector_names = set([
        'x', 'y', 'z', 'a'
    ])
    all_fact_subsets = {
        'x': [_CollectorClass(None, required_facts=['y'])],
        'y': [_CollectorClass(None, required_facts=['x', 'z'])],
        'z': [_CollectorClass(None, required_facts=set())],
        'a': [_CollectorClass(None, required_facts=['z'])],
    }
    unresolved = find_unresolved_requires(collector_names, all_fact_subsets)
    assert unresolved == set()
    # now remove 'a' that has a requirement of 'z'
    collector_names.remove('a')

# Generated at 2022-06-13 00:33:43.567532
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    class Collector(BaseFactCollector):
        _fact_ids = ['fact_1', 'fact_2']
        name = 'PrimaryName'

    class CollectorB(Collector):
        _fact_ids = ['fact_3', 'fact_4']

    class CollectorC(Collector):
        _fact_ids = ['fact_1', 'fact_3']

    real_dict = {}
    real_aliases_map = defaultdict(set)

    fact_id_to_collector_map, aliases_map = build_fact_id_to_collector_map(
        collectors_for_platform=(Collector, CollectorB, CollectorC)
    )


# Generated at 2022-06-13 00:33:53.529358
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    # Test data
    all_fact_subsets = {
        'a_requires_d': [BaseFactCollector],
        'd_no_requires': [BaseFactCollector],
        'c_requires_d': [BaseFactCollector],
        'b_requires_c': [BaseFactCollector],
    }
    all_fact_subsets['a_requires_d'][0].required_facts = set(['d'])
    all_fact_subsets['d_no_requires'][0].required_facts = set()
    all_fact_subsets['c_requires_d'][0].required_facts = set(['d'])
    all_fact_subsets['b_requires_c'][0].required_facts = set(['c'])

    # test_a_and_d_and_b

# Generated at 2022-06-13 00:34:00.285829
# Unit test for function get_collector_names
def test_get_collector_names():
    from ansible.module_utils.facts import FACT_SUBSETS
    from ansible.module_utils.facts import MINIMAL_GATHER_SUBSET
    from ansible.module_utils.facts import gather_subset_definitions
    from ansible.module_utils.facts import gather_subset_aliases

    def get_collector_names_test(platform_info, gather_subset, expected_result):
        # We need to override the "min" set of collectors with the "minimal_gather_subset"
        # set since we want to test the "min" subset.
        # Otherwise, it will not be considered as a valid subset by the get_collector_names
        # method.
        minimal_gather_subset = MINIMAL_GATHER_SUBSET.copy()
        minimal_gather

# Generated at 2022-06-13 00:34:08.195068
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    # all_fact_subsets is a defaultdict to mimic reality
    all_fact_subsets = defaultdict(list)

    class CollectorA(BaseFactCollector):
        name = 'a'
        required_facts = {'b'}

    class CollectorB(BaseFactCollector):
        name = 'b'
        required_facts = {}

    all_fact_subsets['a'].append(CollectorA)
    all_fact_subsets['b'].append(CollectorB)

    unresolved = find_unresolved_requires(['a', 'b'], all_fact_subsets)
    assert not unresolved

    unresolved = find_unresolved_requires(['a'], all_fact_subsets)
    assert unresolved == {'b'}

