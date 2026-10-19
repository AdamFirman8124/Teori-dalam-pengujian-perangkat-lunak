

# Generated at 2022-06-13 00:24:32.187253
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    class FakeCollectorA(BaseFactCollector):
        name = 'A'
        required_facts = set(['B', 'C'])

    class FakeCollectorB(BaseFactCollector):
        name = 'B'
        required_facts = set(['C'])

    class FakeCollectorC(BaseFactCollector):
        name = 'C'
        required_facts = set(['B'])

    class FakeCollectorD(BaseFactCollector):
        name = 'D'
        required_facts = set()

    all_fact_subsets = {
        'A': [FakeCollectorA],
        'B': [FakeCollectorB],
        'C': [FakeCollectorC],
        'D': [FakeCollectorD],
    }

    # Case 1: Simple missing collector
    collector_names = fro

# Generated at 2022-06-13 00:24:42.042683
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    class CollectNetwork(BaseFactCollector):
        name = 'network'
        _fact_ids = frozenset(['network', 'net0'])

    class CollectHardware(BaseFactCollector):
        name = 'hardware'
        _fact_ids = frozenset(['hardware', 'cpuinfo'])

        @classmethod
        def platform_match(cls, platform_info):
            if platform_info.get('system', None) == 'Linux':
                return cls

    class CollectDistribution(BaseFactCollector):
        name = 'distribution'
        _fact_ids = frozenset(['distribution', 'uname_info'])

        @classmethod
        def platform_match(cls, platform_info):
            if platform_info.get('system', None) == 'Linux':
                return cls

# Generated at 2022-06-13 00:24:50.623150
# Unit test for function build_dep_data
def test_build_dep_data():
    from ansible.module_utils.facts.collectors import network

    all_fact_subsets = defaultdict(list)
    all_fact_subsets['network'] = [network.NetworkCollector]

    collector_names = ['network']
    dep_map = build_dep_data(collector_names, all_fact_subsets)
    assert({'network': set(['platform'])} == dep_map)


# Generated at 2022-06-13 00:24:58.413954
# Unit test for function build_dep_data
def test_build_dep_data():
    class MyCollector1(BaseFactCollector):
        name = 'MyCollector1'
        _fact_ids = ['id1', 'id2']
        required_facts = {"id1"}

    class MyCollector2(BaseFactCollector):
        name = 'MyCollector2'
        _fact_ids = ['id2', 'id3']
        required_facts = {"id3", "id4"}

    class MyCollector3(BaseFactCollector):
        name = 'MyCollector3'
        _fact_ids = ['id4', 'id5']
        required_facts = {"id4", "id5", "id6"}

    class MyCollector4(BaseFactCollector):
        name = 'MyCollector4'
        _fact_ids = ['id5', 'id6']

# Generated at 2022-06-13 00:25:08.228697
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    from ansible_collections.ansible.community.plugins.module_utils.facts import collectors
    valid_subsets = frozenset(['all', 'networking', 'network', 'min'])
    all_collector_classes = {collector for collector in collectors.__dict__.values() if hasattr(collector, 'name')}

    plat = {'system': platform.system()}
    collectors_for_platform = find_collectors_for_platform(all_collector_classes, (plat, {'system': 'Generic'}))
    fact_id_to_collector_map, aliases_map = build_fact_id_to_collector_map(collectors_for_platform)

# Generated at 2022-06-13 00:25:19.370117
# Unit test for function find_collectors_for_platform
def test_find_collectors_for_platform():
    import ansible.module_utils.facts.collectors.generic
    import ansible.module_utils.facts.collectors.system

    all_collector_classes = [
        ansible.module_utils.facts.collectors.generic.GenericFactCollector,
        ansible.module_utils.facts.collectors.system.SystemFactCollector
    ]
    compat_platforms = [{'system': 'Linux'}]
    found_collectors = find_collectors_for_platform(all_collector_classes, compat_platforms)
    assert len(found_collectors) == 2

    compat_platforms = [{'system': 'NonExistingPlatform'}]
    found_collectors = find_collectors_for_platform(all_collector_classes, compat_platforms)

# Generated at 2022-06-13 00:25:28.966646
# Unit test for function collector_classes_from_gather_subset
def test_collector_classes_from_gather_subset():

    # Setup
    minimal_gather_subset = frozenset(['min'])
    valid_subsets = frozenset(['min'])
    platform_info = {'system': 'Windows'}

    class fake_collector(BaseFactCollector):
        _fact_ids = set()

        name = 'foo'

    all_collector_classes = [fake_collector]

    # test an empty gather_subset
    # all subsets should be selected
    gather_subset = []
    expected = [fake_collector]

# Generated at 2022-06-13 00:25:40.498017
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    require_map = {}

    def make_collector(name, requires=[]):
        require_map[name] = set(requires)
        return type(name, (object,), {'name': name, 'required_facts': set(requires)})

    foo_collector = make_collector('foo', ['bar'])
    bar_collector = make_collector('bar', ['baz', '3rd_level_dependency']),
    baz_collector = make_collector('baz')
    baz_collector2 = make_collector('baz')

    all_fact_subsets = {
        'foo': [foo_collector],
        'bar': [bar_collector, bar_collector],
        'baz': [baz_collector2, baz_collector],
    }

# Generated at 2022-06-13 00:25:50.760661
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    from ansible.module_utils.facts.collectors.network import NetworkCollector
    from ansible.module_utils.facts.collectors.local import LocalCollector
    from ansible.module_utils.facts.collectors.system import SystemCollector
    all_fact_subsets = {
        'system': [SystemCollector],
        'network': [NetworkCollector],
        'local': [LocalCollector]
    }

    # Simple case that everything is resolved
    collector_names = ['system', 'network']
    unresolved = find_unresolved_requires(collector_names, all_fact_subsets)
    assert not unresolved, '%s should be empty' % unresolved

    # One collector has an unresolved require.
    collector_names = ['system', 'network', 'local']

# Generated at 2022-06-13 00:26:01.540492
# Unit test for function tsort
def test_tsort():
    # tests are based on examples from: https://en.wikipedia.org/wiki/Topological_sorting#Depth-first_search
    dep_map1 = {'1': set(['4', '7']),
                '2': set(['3', '8']),
                '3': set(['8', '9']),
                '4': set(['7', '9']),
                '5': set(['11']),
                '6': set(['5']),
                '7': set(['11']),
                '8': set(['11']),
                '9': set(['10']),
                '10': set(['11']),
                '11': set()}
    sorted_list = tsort(dep_map1)
    correct_order = [x[0] for x in sorted_list]


# Generated at 2022-06-13 00:26:12.516468
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    from . import all_collectors, fact_subsets
    collector_classes = select_collector_classes(['all'], fact_subsets)
    collector_names = all_fact_subsets.keys()

    unresolved = find_unresolved_requires(collector_names, all_fact_subsets)

    assert 'virtual' in unresolved, ('facter and ohai both require virtual')



# Generated at 2022-06-13 00:26:22.547527
# Unit test for function get_collector_names
def test_get_collector_names():
    assert(get_collector_names(valid_subsets=['a', 'b', 'c'],
                               aliases_map={'d': ['a', 'c']},
                               gather_subset=['a', 'd']) ==
           set(['a', 'c']))
    test_subsets = ['a', 'b', 'c']
    assert(get_collector_names(valid_subsets=test_subsets,
                               aliases_map=None,
                               gather_subset=['all']) ==
           set(test_subsets))

    # test that an unknown subset is not added

# Generated at 2022-06-13 00:26:35.050958
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    '''test that fact_id_to_collector_map works as expected'''
    _test_id_to_collector_map = build_fact_id_to_collector_map(set([MockCollector1, MockCollector2]))
    assert list(_test_id_to_collector_map[0].keys()) == ['mockcollector1', 'mockcollector2', 'by_mockcollector1', 'by_mockcollector2']
    assert _test_id_to_collector_map[1]['mockcollector1'] == set(['mockcollector1', 'by_mockcollector1'])

# Generated at 2022-06-13 00:26:45.031351
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    # we can't do much here at the moment, because we need some real
    # collectors to test with
    assert find_unresolved_requires([], {}) == set()
    assert find_unresolved_requires(['a', 'b'], {'a': [], 'b': []}) == set()

    # make up a graph with no unresolved dependencies
    class A(object):
        required_facts = set(['c'])
    class B(object):
        required_facts = set(['c'])
    class C(object):
        required_facts = set()

    classes = [A(), B(), C()]


# Generated at 2022-06-13 00:26:54.315304
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    from ansible.module_utils.facts.system.distribution import DistributionFactCollector
    from ansible.module_utils.facts.system.distribution import DebianFactCollector
    from ansible.module_utils.facts.system.distribution import AlpineFactCollector

    systemd_found = platform.system() == "Linux"
    valid_subsets = frozenset(('all', 'network', 'virtual', 'hardware', 'firmware', 'identification', 'default'))

    minimal_gather_subset = frozenset(('!all', '!min'))

    all_collectors = [
        DistributionFactCollector,
        DebianFactCollector,
        AlpineFactCollector,
    ]

    # Test for fact_id_to_collector_map


# Generated at 2022-06-13 00:27:06.052849
# Unit test for function build_dep_data
def test_build_dep_data():
    import fact_retrieval
    import fact_namespace
    import fact_data
    import ansible_collections
    import module_utils.facts.virtual

    all_collector_classes = list(fact_data.get_collector_classes(collector_types=[fact_data.FactsCollector]))
    all_collector_classes.extend(fact_retrieval.get_collector_classes())
    all_collector_classes.extend(fact_namespace.get_collector_classes())
    all_collector_classes.extend(ansible_collections.get_collector_classes())
    all_collector_classes.extend(module_utils.facts.virtual.get_collector_classes())


# Generated at 2022-06-13 00:27:12.897190
# Unit test for function build_dep_data
def test_build_dep_data():
    all_fact_subsets = defaultdict(set)
    collector_classes = [TestCollectorA, TestCollectorB, TestCollectorC]
    for collector_class in collector_classes:
        collector_name = collector_class.name
        all_fact_subsets[collector_name].add(collector_class)
    collector_names = ['A', 'B', 'C']
    dep_map = build_dep_data(collector_names, all_fact_subsets)
    assert dep_map['A'] == set()
    assert dep_map['B'] == {'A'}
    assert dep_map['C'] == {'B'}



# Generated at 2022-06-13 00:27:24.082395
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    # Test different collectors
    # All Collector classes have a name attribute.
    # The _fact_ids attribute is a list of all the fact ids that are collected by that collector
    # The _fact_ids_deps attribute is a list of all the fact ids that are required by that collector
    import ansible.module_utils.facts.collectors.base

    # Simple case
    class Dummycollector0(ansible.module_utils.facts.collectors.base.BaseFactCollector):
        _platform = 'Generic'
        name = 'foo'
        _fact_ids = ['foo.id1', 'foo.id2']
        _fact_ids_deps = ['foo.dep1']


# Generated at 2022-06-13 00:27:32.573376
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    from ansible.module_utils.facts import hardware

    assert hardware.find_unresolved_requires([], {}) == set()
    assert hardware.find_unresolved_requires(['dmi'], {}) == set()

    fact_id_to_collector_map = {
        'fake_fact_1': [MockFactCollector(['fake_fact_2'], 'fake_fact_1')],
        'fake_fact_2': [MockFactCollector(['fake_fact_3'], 'fake_fact_2')],
        'fake_fact_3': [MockFactCollector([], 'fake_fact_3')],
    }

    assert hardware.find_unresolved_requires(['fake_fact_3'], fact_id_to_collector_map) == set()
    assert hardware

# Generated at 2022-06-13 00:27:45.037183
# Unit test for function tsort
def test_tsort():
    tsort_data1 = {'collector-A': {'collector-B'}, 'collector-B': {'collector-C'}, 'collector-C': {'collector-A'}}
    tsort_data2 = {'collector-A': {'collector-B'}, 'collector-B': {'collector-C'}, 'collector-C': {}}
    tsort_data3 = {'collector-A': {'collector-B'}, 'collector-B': {'collector-C'}, 'collector-C': {}}

    assert tsort(tsort_data1) == []

# Generated at 2022-06-13 00:28:07.393537
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    class CollectorOne(BaseFactCollector):
        """Test collector class"""
    CollectorOne.name = 'one'
    CollectorOne._fact_ids = set(['one', 'one_alias'])

    class CollectorTwo(BaseFactCollector):
        """Test collector class"""
    CollectorTwo.name = 'two'
    CollectorTwo._fact_ids = set(['two', 'two_alias', 'two_another_alias'])

    all_collectors_classes = set([CollectorTwo, CollectorOne])


# Generated at 2022-06-13 00:28:19.255183
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    from ansible.module_utils.facts import collector

    def _check_map(expected_result, _fact_id_to_collector_map):
        for fact_id in expected_result.keys():
            for collector_class in expected_result[fact_id]:
                assert fact_id_to_collector_map[fact_id].count(collector_class) == 1

    class FakeCollector(BaseFactCollector):
        name = 'fake'

    class FakeCollectorSubClass(FakeCollector):
        name = 'fake_subclass'

    fake_collector_classes = (FakeCollector, FakeCollectorSubClass)

    fact_id_to_collector_map, aliases_map = build_fact_id_to_collector_map(fake_collector_classes)


# Generated at 2022-06-13 00:28:27.345612
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    collector_names = ['ansible_os_family', 'ansible_architecture']
    all_fact_subsets = {
        'ansible_architecture': [],
        'ansible_distribution': [],
        'ansible_distribution_release': [],
        'ansible_distribution_version': [],
        'ansible_os_family': [],
        'ansible_pkg_mgr': []
    }
    unresolved = find_unresolved_requires(collector_names, all_fact_subsets)
    assert len(unresolved) == 0

    collector_names = ['ansible_os_family', 'ansible_architecture', 'ansible_distribution', 'ansible_distribution_release']

# Generated at 2022-06-13 00:28:38.216738
# Unit test for function find_collectors_for_platform
def test_find_collectors_for_platform():
    class CollectorImpl_generic(BaseFactCollector):
        pass

    class CollectorImpl_redhat(BaseFactCollector):
        _platform = 'Linux'
        _distribution = 'RedHat'

    class CollectorImpl_centos(BaseFactCollector):
        _platform = 'Linux'
        _distribution = 'CentOS'

    class CollectorImpl_ubuntu(BaseFactCollector):
        _platform = 'Linux'
        _distribution = 'Ubuntu'

    # case 1: simple match
    found = find_collectors_for_platform(
        all_collector_classes=[CollectorImpl_generic, CollectorImpl_redhat, CollectorImpl_centos],
        compat_platforms=[{'system': 'Linux', 'distribution': 'RedHat'}])

    assert len(found) == 2

# Generated at 2022-06-13 00:28:47.041290
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    collector_names = frozenset(['col-1', 'col-2'])
    all_fact_subsets = {
        'col-1': [object()],
        'col-2': [object()],
    }

    assert not find_unresolved_requires(collector_names, all_fact_subsets)

    for bad_requires in ['', 'foo', object(), 'col-1']:
        all_fact_subsets['col-2'][0].required_facts = {bad_requires}
        assert find_unresolved_requires(collector_names, all_fact_subsets)



# Generated at 2022-06-13 00:28:57.120871
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    from ansible.module_utils.facts.collectors import network, hardware, default
    from ansible.module_utils.facts.collectors.linux.network import LinuxNetwork
    from ansible.module_utils.facts.collectors.linux.hardware import LinuxHardware
    from ansible.module_utils.facts.collectors.linux.default import LinuxDefault
    from ansible.module_utils.facts.collectors.freebsd.network import FreeBSDBaseNetwork
    from ansible.module_utils.facts.collectors.freebsd.hardware import FreeBSDHardware

    facts_collector_classes = [LinuxNetwork, LinuxHardware, LinuxDefault,
                               FreeBSDBaseNetwork, FreeBSDHardware]


# Generated at 2022-06-13 00:29:07.298526
# Unit test for function build_dep_data
def test_build_dep_data():
    class A(BaseFactCollector):
        name = 'a'
        required_facts = set()
    class B(BaseFactCollector):
        name = 'b'
        required_facts = set()
    class C(BaseFactCollector):
        name = 'c'
        required_facts = set(['b'])

    all_fact_subsets = {
        A.name: [A],
        B.name: [B],
        C.name: [C],
    }
    collector_names = {'a', 'b', 'c'}
    expected_dep_map = {'a': set(), 'b': set(), 'c': {'b'}}

    dep_data = build_dep_data(collector_names, all_fact_subsets)
    assert dep_data == expected_dep_map



# Generated at 2022-06-13 00:29:16.441585
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    '''
    Test for the build_fact_id_to_collector_map function
    '''
    from ansible.module_utils.facts.collectors import network, virtual
    test_collectors_for_platform = [network.NetworkCollector, virtual.VirtualCollector]
    test_fact_id_to_collector_map, test_aliases_map = build_fact_id_to_collector_map(test_collectors_for_platform)
    assert isinstance(test_fact_id_to_collector_map, defaultdict)
    assert isinstance(test_aliases_map, defaultdict)
    assert 'network' in test_fact_id_to_collector_map
    assert isinstance(test_fact_id_to_collector_map['network'], list)

# Generated at 2022-06-13 00:29:27.214606
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    all_fact_subsets = {'a': [object()], 'b': [object()], 'c': [object()]}

    # b requires a, c requires b
    class B(BaseFactCollector):
        required_facts = ('a',)

    class C(BaseFactCollector):
        required_facts = ('b',)

    all_fact_subsets['b'] = [B]
    all_fact_subsets['c'] = [C]

    assert find_unresolved_requires(['a'], all_fact_subsets) == set()
    assert find_unresolved_requires(['a', 'b'], all_fact_subsets) == set()
    assert find_unresolved_requires(['b'], all_fact_subsets) == {'a'}
    assert find_unresolved

# Generated at 2022-06-13 00:29:38.949626
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    from ansible.module_utils.facts import collectors as c
    from ansible.module_utils.facts.collectors.base import CollectorNotFoundError

    test_classes = [c.CPU, c.DMI, c.Network, c.ZScore, c.System, c.Hardware]

    fact_id_to_collector_map, aliases_map = build_fact_id_to_collector_map(test_classes)

    assert list(fact_id_to_collector_map['distribution']) == [c.System]
    assert list(fact_id_to_collector_map['system']) == [c.System]
    assert list(fact_id_to_collector_map['network']) == [c.Network]

# Generated at 2022-06-13 00:30:15.247849
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    collector_names = ['a', 'b', 'c', 'd', 'e', 'f']

    a_requires = frozenset(['d', 'x'])
    b_requires = frozenset(['a'])
    c_requires = frozenset(['a', 'x'])
    d_requires = frozenset()
    e_requires = frozenset(['b'])
    f_requires = frozenset(['d', 'e'])

    class FakeBaseFactCollector:
        def __init__(self, required_facts):
            self.required_facts = required_facts


# Generated at 2022-06-13 00:30:26.424221
# Unit test for function build_dep_data
def test_build_dep_data():
    collector_names = ['foo', 'bar']
    all_fact_subsets = dict(foo=[], bar=[])
    actual_dep_map = build_dep_data(collector_names, all_fact_subsets)
    expected_dep_map = dict(foo=set(), bar=set())
    assert expected_dep_map == actual_dep_map

    collector_names = ['foo', 'bar', 'baz']
    collector_foo = [object()]
    collector_bar = [object()]
    collector_baz = [object()]
    collector_foo[0].required_facts = set(['bar'])
    collector_bar[0].required_facts = set(['foo'])
    collector_baz[0].required_facts = set([])

# Generated at 2022-06-13 00:30:35.864649
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    from ansible.module_utils.facts.collector import BaseFactCollector, BaseFileCacheCollector
    class FakeCollector(BaseFactCollector):
        _fact_ids = ('fake')
    class FakeFileCollector(BaseFileCacheCollector):
        _fact_ids = ('fake_file')
    c1 = FakeCollector()
    c2 = FakeFileCollector()
    # add two classes that both have_id 'fake'
    fact_id_to_collector_map, aliases_map = build_fact_id_to_collector_map([c1, c2])
    assert 'fake' in fact_id_to_collector_map
    assert 'fake_file' in fact_id_to_collector_map
    assert len(fact_id_to_collector_map['fake']) == 2


# Generated at 2022-06-13 00:30:47.287075
# Unit test for function get_collector_names
def test_get_collector_names():
    assert get_collector_names(
        gather_subset=['all'],
        valid_subsets=frozenset(['network']),
        aliases_map=defaultdict(set, {'hardware': frozenset(['devices', 'dmi'])})
    ) == frozenset(['network'])

    assert get_collector_names(
        gather_subset=['network'],
        valid_subsets=frozenset(['network']),
        aliases_map=defaultdict(set, {'hardware': frozenset(['devices', 'dmi'])})
    ) == frozenset(['network'])


# Generated at 2022-06-13 00:30:56.930407
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():

    class TestCollector1(BaseFactCollector):
        name = 'TestCollector1'
        required_facts = {'TestCollector2',}

    class TestCollector2(BaseFactCollector):
        name = 'TestCollector2'
        required_facts = set()

    assert find_unresolved_requires(['TestCollector1', 'TestCollector2'], {'TestCollector1':[TestCollector1,], 'TestCollector2':[TestCollector2,]}) == set()
    assert find_unresolved_requires(['TestCollector2', 'TestCollector1'], {'TestCollector1':[TestCollector1,], 'TestCollector2':[TestCollector2,]}) == set()

# Generated at 2022-06-13 00:31:08.373308
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    collector_names = ['collector_name_1', 'collector_name_2', 'collector_name_3']
    all_fact_subsets = {
        'collector_name_1': [object()],
        'collector_name_2': [object(), object()],
        'collector_name_3': [object()]
    }
    collector_name_1 = all_fact_subsets['collector_name_1'][0]
    collector_name_2 = all_fact_subsets['collector_name_2'][0]
    collector_name_3 = all_fact_subsets['collector_name_3'][0]
    collector_name_2_second = all_fact_subsets['collector_name_2'][1]

# Generated at 2022-06-13 00:31:15.973953
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    TempCollector = type(
        'TempCollector',
        (BaseFactCollector,),
        {
            'name': 'temp',
            'required_facts': frozenset(),
        }
    )
    TempCollector2 = type(
        'TempCollector2',
        (BaseFactCollector,),
        {
            'name': 'temp2',
            'required_facts': frozenset(['temp']),
        }
    )
    TempCollector3 = type(
        'TempCollector3',
        (BaseFactCollector,),
        {
            'name': 'temp3',
            'required_facts': frozenset(['temp2']),
        }
    )

# Generated at 2022-06-13 00:31:26.051256
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    # gather_subset is a spec describing which facts to gather
    valid_subsets = ('all', 'min', 'hardware', 'virtual', 'network')

    # the list of everything that 'all' expands to
    valid_subsets = frozenset(valid_subsets)

    # if provided, minimal_gather_subset is always added, even after all negations
    minimal_gather_subset = frozenset()

    # Retrieve all facts elements
    additional_subsets = set()
    exclude_subsets = set()

    # total always starts with the min set, then
    # adds of the additions in gather_subset, then
    # excludes all of the excludes, then add any explicitly
    # requested subsets.
    gather_subset_with_min = ['min']

# Generated at 2022-06-13 00:31:34.290195
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    class Mock(BaseFactCollector):
        pass

    class A(Mock):
        name = 'a'
        required_facts = set(['b'])

    class B(Mock):
        name = 'b'
        required_facts = set(['c'])

    class C(Mock):
        name = 'c'
        required_facts = set()

    class D(Mock):
        name = 'd'
        required_facts = set(['a'])

    class E(Mock):
        name = 'e'
        required_facts = set(['a'])

    class F(Mock):
        name = 'f'
        required_facts = set(['z'])

    class Z(Mock):
        name = 'z'
        required_facts = set(['b'])

   

# Generated at 2022-06-13 00:31:44.463549
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    all_fact_subsets = {
        'a': [MockFactCollector(['b'])],
        'b': [MockFactCollector([])],
        'c': [MockFactCollector(['a', 'd'])],
    }

    # collect a, b, then c, no unresolved deps
    collector_names = ['a', 'b', 'c']
    unresolved = find_unresolved_requires(collector_names, all_fact_subsets)
    assert not unresolved

    # collect c first, unresolved should be 'd'
    collector_names = ['c', 'a', 'b']
    unresolved = find_unresolved_requires(collector_names, all_fact_subsets)
    assert unresolved == {'d'}




# Generated at 2022-06-13 00:32:01.090292
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    class TestCollector1(BaseFactCollector):
        _fact_ids = set()
        _platform = 'Generic'
        name = 'test1'
        required_facts = set()

    class TestCollector2(BaseFactCollector):
        _fact_ids = set()
        _platform = 'Generic'
        name = 'test2'
        required_facts = set()

    class TestCollector3(BaseFactCollector):
        _fact_ids = {'test3-fact'}
        _platform = 'Generic'
        name = 'test3'
        required_facts = set()

    class TestCollector4(BaseFactCollector):
        _fact_ids = {'test4-fact', 'test4-fact-2'}
        _platform = 'Generic'
        name = 'test4'
        required_

# Generated at 2022-06-13 00:32:11.249235
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    from ansible.module_utils.facts.collectors import (
        BaseFactCollector,
        Hardware,
        Default,
    )

    platform_info = {'system': 'Linux'}

    all_collector_classes = (
        Hardware,
        Default,
    )

    collectors_for_platform = find_collectors_for_platform(all_collector_classes, (platform_info,))

    fact_id_to_collector_map, aliases_map = build_fact_id_to_collector_map(collectors_for_platform)

    assert Hardware in fact_id_to_collector_map['hardware']
    assert Hardware in fact_id_to_collector_map['devices']
    assert Hardware in fact_id_to_collector_map['dmi']

    assert Default in fact_id

# Generated at 2022-06-13 00:32:19.083752
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    test_fact_subsets = {'one': [], 'two': [], 'three': []}
    one_requires = ['two', 'three']
    two_requires = []
    three_requires = ['four']

    class DummyCollector():
        required_facts = set()

    test_fact_subsets[one_requires[0]].append(DummyCollector())
    test_fact_subsets[one_requires[1]].append(DummyCollector())
    test_fact_subsets[two_requires[0]].append(DummyCollector())
    test_fact_subsets[three_requires[0]].append(DummyCollector())

    test_fact_subsets['one'][0].required_facts = set(one_requires)
    test_fact_subsets['two'][0].required

# Generated at 2022-06-13 00:32:27.305882
# Unit test for function get_collector_names
def test_get_collector_names():
    """
    This function tests get_collector_names.
    """
    valid_subsets = frozenset(['all', 'command', 'hardware', 'network', 'system'])
    minimal_gather_subset = frozenset(['all', 'system'])
    aliases_map = defaultdict(set, {'hardware': frozenset(['devices', 'dmi'])})
    assert get_collector_names(valid_subsets=valid_subsets,
                               minimal_gather_subset=minimal_gather_subset,
                               aliases_map=aliases_map) == frozenset(['all', 'command', 'devices', 'dmi', 'hardware',
                                                                     'network', 'system'])

# Generated at 2022-06-13 00:32:37.334816
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    all_fact_subsets = {
        'fact_a': [
            FakeCollector(name='fact_a', required_facts=set()),
        ],
        'fact_b': [
            FakeCollector(name='fact_b', required_facts={'fact_c'}),
        ],
        'fact_c': [
            FakeCollector(name='fact_c', required_facts=set()),
        ],
    }

    unresolved = find_unresolved_requires(collector_names=set(), all_fact_subsets=all_fact_subsets)
    assert not unresolved

    unresolved = find_unresolved_requires(collector_names={'fact_a'}, all_fact_subsets=all_fact_subsets)
    assert not unresolved


# Generated at 2022-06-13 00:32:41.843288
# Unit test for function build_dep_data
def test_build_dep_data():
    all_fact_subsets = {'A': [CollectorA(), CollectorB()],
                        'B': [CollectorC(),]}
    collector_names = ['A', 'B']
    assert build_dep_data(collector_names, all_fact_subsets) == {'A': {'B'}, 'B': {'C'}}


# Generated at 2022-06-13 00:32:50.700892
# Unit test for function get_collector_names
def test_get_collector_names():
    def test(gather_subset, expected_subset,
             aliases_map=defaultdict(set),
             minimal_gather_subset=frozenset(),
             valid_subsets=frozenset('a b c d'.split())):
        assert get_collector_names(
            gather_subset=gather_subset,
            valid_subsets=valid_subsets,
            minimal_gather_subset=minimal_gather_subset,
            aliases_map=aliases_map,
        ) == frozenset(expected_subset.split())

    test(['!a'], 'b c d')
    test(['all', '!a'], 'b c d')
    test(['!all', '!a'], 'min')

# Generated at 2022-06-13 00:33:01.430876
# Unit test for function get_collector_names
def test_get_collector_names():

    # when no gather_subset is specified
    assert get_collector_names() == frozenset()

    # when 'all' is specified
    assert get_collector_names(['network'], None, ['all']) == frozenset({'network'})

    # when '!network' is specified
    assert get_collector_names(['network', 'hardware'], None, ['!network']) == frozenset({'hardware'})

    # when 'network' is specified
    assert get_collector_names(['network', 'hardware'], None, ['!network']) == frozenset({'hardware'})

    # when nothing is specified
    assert get_collector_names(['network', 'hardware'], None, []) == frozenset({'network', 'hardware'})

    # when network

# Generated at 2022-06-13 00:33:12.123777
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    from ansible.module_utils.facts.system.base import BaseFactCollector
    class C1(BaseFactCollector):
        _fact_ids = {'c1'}
        required_facts = {'a', 'b'}
    class C2(BaseFactCollector):
        _fact_ids = {'c2'}
        required_facts = {'a'}
    class C3(BaseFactCollector):
        _fact_ids = {'c3'}
        required_facts = {'a'}
    class C4(BaseFactCollector):
        _fact_ids = {'c4'}
        required_facts = {'a'}
    class A(BaseFactCollector):
        _fact_ids = {'a'}
        required_facts = set()

# Generated at 2022-06-13 00:33:24.283829
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    class FactA(BaseFactCollector):
        name = 'A'
        required_facts = set()
    class FactB(BaseFactCollector):
        name = 'B'
        required_facts = set()
    class FactC(BaseFactCollector):
        name = 'C'
        required_facts = set(['A'])
    class FactD(BaseFactCollector):
        name = 'D'
        required_facts = set(['B'])

    all_fact_subsets = {
        'A': [FactA],
        'B': [FactB],
        'C': [FactC],
        'D': [FactD]
    }


# Generated at 2022-06-13 00:33:46.451212
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    import pytest
    from ansible.module_utils.facts.network.legacy import Base

    class CollectorA(Base):
        _fact_ids = ('A',)
        name = 'CollectorA'
        required_facts = ('B', 'D')

    class CollectorB(Base):
        _fact_ids = ('B',)
        name = 'CollectorB'

    class CollectorC(Base):
        _fact_ids = ('C',)
        name = 'CollectorC'
        required_facts = ('D',)

    class CollectorD(Base):
        _fact_ids = ('D',)
        name = 'CollectorD'


# Generated at 2022-06-13 00:33:55.510180
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    class FC1(BaseFactCollector):
        _fact_ids = ['a', 'b', 'c']
        _platform = 'Linux'
        name = 'foo'
        required_facts = set(['foo', 'a', 'b'])

    class FC2(BaseFactCollector):
        _fact_ids = ['a', 'b', 'c']
        _platform = 'Linux'
        name = 'foo'
        required_facts = set(['foo', 'a', 'c'])

    class FC3(BaseFactCollector):
        _fact_ids = ['a', 'b', 'c']
        _platform = 'Linux'
        name = 'foo'
        required_facts = set(['a', 'b', 'd'])


# Generated at 2022-06-13 00:34:05.694581
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    from . import fact_collector
    from . import namespace_class

    class FactA(BaseFactCollector):
        name = 'fact_a'

    class FactB(BaseFactCollector):
        name = 'fact_b'
        required_facts = set(('fact_a',))

    class FactC(BaseFactCollector):
        name = 'fact_c'
        required_facts = set(('fact_a',))

    class FactD(BaseFactCollector):
        name = 'fact_d'
        required_facts = set(('fact_b', 'fact_c'))

    class FactE(BaseFactCollector):
        name = 'fact_e'
        required_facts = set(('fact_d', 'fact_z'))
