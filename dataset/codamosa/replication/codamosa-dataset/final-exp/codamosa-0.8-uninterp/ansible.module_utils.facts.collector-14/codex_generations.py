

# Generated at 2022-06-13 00:24:36.623543
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    from ansible.module_utils.facts import collector

    # Basic test
    collector_names = ('arch', 'distribution', 'distribution_release',
                       'distribution_version', 'ipv4_address', 'ipv6_address',
                       'kernel', 'kernel_version', 'machine_id',
                       'processor', 'processor_cores', 'processor_count',
                       'processor_threads_per_core', 'processor_vcpus', 'system',
                       'virtualization_role', 'virtualization_type')

    unresolved = find_unresolved_requires(collector_names, collector.ALL_FACTS_SUBSETS)
    assert not unresolved, "Found %s in %s" % (unresolved, collector_names)

    # Test a missing subset

# Generated at 2022-06-13 00:24:46.237681
# Unit test for function select_collector_classes
def test_select_collector_classes():
    class EmptyCollector(BaseFactCollector):
        name = 'EmptyCollector'

    class CollectorA(BaseFactCollector):
        name = 'a'

    class CollectorB(BaseFactCollector):
        name = 'b'

    class CollectorC(BaseFactCollector):
        name = 'c'

    class CollectorD(BaseFactCollector):
        name = 'd'
        _fact_ids = (
            'aa',
        )

    class CollectorE(BaseFactCollector):
        name = 'e'
        _fact_ids = (
            'bb',
            'cc',
        )

    class CollectorF(BaseFactCollector):
        name = 'f'

    class CollectorG(BaseFactCollector):
        name = 'g'


# Generated at 2022-06-13 00:24:56.326997
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    class TestCollector1(BaseFactCollector):
        name = 'test1'
        _fact_ids = set(['test1', 'network'])

    class TestCollector2(BaseFactCollector):
        name = 'test2'
        _fact_ids = set(['test2', 'network'])

    class TestCollector3(BaseFactCollector):
        name = 'test3'
        _fact_ids = set(['test3'])

    class TestCollector4(BaseFactCollector):
        name = 'test4'
        _fact_ids = set(['test4'])

    class TestCollector5(BaseFactCollector):
        name = 'test5'
        _fact_ids = set(['test5'])


# Generated at 2022-06-13 00:25:07.380594
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    from ansible.module_utils.facts.collectors import all_collectors
    from ansible.module_utils.facts.collectors.platform.linux import LinuxFactCollector

    collector_names = {'SomeCollector', 'SomeOtherCollector'}
    all_fact_subsets = {
        'SomeCollector': [
            type('SomeCollector', (LinuxFactCollector,), {
                'required_facts': set(['SomeOtherCollector']),
                'name': 'SomeCollector',
            }),
        ],
        'SomeOtherCollector': [
            type('SomeOtherCollector', (LinuxFactCollector,), {
                'required_facts': set(),
                'name': 'SomeOtherCollector',
            }),
        ],
    }

# Generated at 2022-06-13 00:25:18.855894
# Unit test for function build_dep_data
def test_build_dep_data():
    all_fact_subsets = {
        'processors': {FactCollector},
        'distribution': {FactCollector, DummyDistroFactCollector},
        'virtual': {FactCollector, DummyVirtualFactCollector},
        'dmi': {FactCollector, DummyDMIFactCollector},
        'all': {FactCollector},
        'min': {},
    }
    dep_map = build_dep_data(['processors', 'distribution', 'virtual', 'dmi'],
                             all_fact_subsets)
    assert dep_map == {
        'processors': {'all'},
        'distribution': {'min'},
        'virtual': {},
        'dmi': {'min'},
    }

# Generated at 2022-06-13 00:25:27.202076
# Unit test for function find_collectors_for_platform
def test_find_collectors_for_platform():
    '''unit test for function find_collectors_for_platform'''
    # test 1: no matches
    all_collector_classes = [A_Collector_MatchA_MatchB]
    compat_platforms = [{}, {'foo': 'bar'}]
    assert find_collectors_for_platform(all_collector_classes, compat_platforms) == set()

    # test 2: match on 1st platform
    # On first platform, find A_Collector_MatchA_MatchB
    all_collector_classes = [A_Collector_MatchA_MatchB]
    compat_platforms = [{'system': 'Foo'}, {'system': 'Bar'}]

# Generated at 2022-06-13 00:25:35.185188
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    # Test with a simple case
    collector_names = set(['a', 'b'])
    all_fact_subsets = {
        'a': [
            type('FakeCollectorA', (object,), {'required_facts': ['b']})
        ]
    }
    assert find_unresolved_requires(collector_names, all_fact_subsets) == set()

    # Test a missing collector
    assert 'missing' in find_unresolved_requires(collector_names, all_fact_subsets)



# Generated at 2022-06-13 00:25:44.897723
# Unit test for function find_collectors_for_platform
def test_find_collectors_for_platform():
    # Create class that 'matches' platform.
    class MockClass(BaseFactCollector):
        _platform = 'Linux'
        name = 'mock'

    # Assert that a class matches a platform.
    found_collectors = find_collectors_for_platform([MockClass], [dict(
        system='Linux',
        version='3.10.0-327.el7.x86_64',
        kernel='Linux',
        machine_type='x86_64',
        processor='x86_64',
    )])
    assert len(found_collectors) == 1
    assert MockClass == list(found_collectors)[0]

    # Assert that a non-matching class does not match a platform.

# Generated at 2022-06-13 00:25:56.512628
# Unit test for function get_collector_names
def test_get_collector_names():
    # type: () -> None
    from ansible.module_utils.facts.collector import get_collector_names

    # case 1
    assert get_collector_names() == set(['all'])
    # case 2
    assert get_collector_names(gather_subset='all') == set(['all'])
    # case 3
    assert get_collector_names(gather_subset='min') == set(['min'])
    # case 4
    assert get_collector_names(gather_subset=['all']) == set(['all'])
    # case 5
    assert get_collector_names(gather_subset=['min']) == set(['min'])
    # case 6

# Generated at 2022-06-13 00:26:07.253542
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    class FactCollector_dmi(BaseFactCollector):
        name = 'dmi'
        _fact_ids = set(('dmi', 'bios'))

    from ansible.module_utils.facts.collector import build_fact_id_to_collector_map

    platform_info = {'system': 'Linux'}

    collectors_for_platform = find_collectors_for_platform([FactCollector_dmi], [platform_info])
    fact_id_to_collector_map, aliases_map = build_fact_id_to_collector_map(collectors_for_platform)

    assert set(fact_id_to_collector_map.keys()) == {'dmi', 'bios'}
    assert set(aliases_map.keys()) == {'dmi'}


# Generated at 2022-06-13 00:26:29.234630
# Unit test for function select_collector_classes
def test_select_collector_classes():
    from tests.unit.modules.utils.test_find_collectors_for_platform import (test_find_collectors_for_platform,
                                                                            test_collectors_for_platform,
                                                                            all_fact_subsets_metadata,
                                                                            #all_collectors
                                                                            )

    test_find_collectors_for_platform()

    selected_collector_classes = select_collector_classes(['network', 'facter'], all_fact_subsets_metadata)

    assert set(selected_collector_classes) == set(test_collectors_for_platform)



# Generated at 2022-06-13 00:26:40.165885
# Unit test for function select_collector_classes
def test_select_collector_classes():
    all_fact_subsets = {
        # test simple case, a single collector for a fact
        'foo': [
            'ansible.module_utils.facts.foo'
        ],
        # test multiple collectors for a fact
        'bar': [
            'ansible.module_utils.facts.foo',
            'ansible.module_utils.facts.bar'
        ]
    }
    collector_names = ['foo']
    assert select_collector_classes(collector_names, all_fact_subsets) == ['ansible.module_utils.facts.foo']

    collector_names = ['bar']
    assert select_collector_classes(collector_names, all_fact_subsets) == ['ansible.module_utils.facts.foo', 'ansible.module_utils.facts.bar']

    # test de

# Generated at 2022-06-13 00:26:47.643870
# Unit test for function build_dep_data
def test_build_dep_data():
    from ansible_collections.ansible.community.plugins.module_utils.facts.collectors import all_collector_classes
    all_fact_subsets = {}
    for collector_class in all_collector_classes:
        all_fact_subsets.setdefault(collector_class.name, set()).add(collector_class)
    collector1 = 'network'
    collector2 = 'platform'
    collector3 = 'dmi'
    collector_names = [collector1, collector2, collector3]
    dep_map = build_dep_data(collector_names, all_fact_subsets)
    assert dep_map[collector1] == set()
    assert dep_map[collector2] == set()
    assert dep_map[collector3] == {'platform'}



# Generated at 2022-06-13 00:26:56.090189
# Unit test for function select_collector_classes
def test_select_collector_classes():
    # Testing dummy collectors
    class CollectorClassA(BaseFactCollector):
        name = 'A'
        _fact_ids = 'A'

    class CollectorClassA1(BaseFactCollector):
        name = 'A'
        _fact_ids = 'A1'

    class CollectorClassA2(BaseFactCollector):
        name = 'A'
        _fact_ids = 'A2'

    class CollectorClassB(BaseFactCollector):
        name = 'B'
        _fact_ids = 'B'

    class CollectorClassB1(BaseFactCollector):
        name = 'B'
        _fact_ids = 'B1'

    class CollectorClassB2(BaseFactCollector):
        name = 'B'
        _fact_ids = 'B2'


# Generated at 2022-06-13 00:27:07.894398
# Unit test for function select_collector_classes
def test_select_collector_classes():
    # setup
    class C1(BaseFactCollector):
        name = 'c1'
    class C2(BaseFactCollector):
        name = 'c2'
    class C2a(BaseFactCollector):
        name = 'c2'
    class C3(BaseFactCollector):
        name = 'c3'

    # test
    all_fact_subsets = {'c1': [C1],
                        'c2': [C2, C2a],
                        'c3': [C3],
                        'c4': [C3]} # doesn't exist

    out = select_collector_classes(['c2', 'c3'], all_fact_subsets)
    assert len(out) == 2

    assert type(out[0]) == C2



# Generated at 2022-06-13 00:27:15.397259
# Unit test for function select_collector_classes
def test_select_collector_classes():
    import pytest
    from ansible.module_utils.facts.collector import BaseFactCollector

    class CollectA(BaseFactCollector):
        name = 'a'

    class CollectB(BaseFactCollector):
        name = 'b'
        _fact_ids = {'b2', 'b3'}

    class CollectC(BaseFactCollector):
        name = 'c'
        _fact_ids = {'c2', 'c3'}

    all_fact_subsets = {
        'a': [CollectA],
        'b': [CollectB],
        'b2': [CollectB],
        'b3': [CollectB],
        'c': [CollectC],
        'c2': [CollectC],
        'c3': [CollectC],
    }

    # test we select the class

# Generated at 2022-06-13 00:27:25.966870
# Unit test for function get_collector_names
def test_get_collector_names():

    # Test case:
    # gather_subset = ['all', '!facter', 'devices'], gather_timeout = 10
    #
    # Expect:
    # gather_subset = ['min', 'all', '!facter', 'devices']
    #   To add: 'min', 'all' => ['distribution', 'system', 'virt', 'ipv4', 'network']
    #   To remove: '!facter' => ['facter']
    #   Result: ['all', 'devices', 'min', 'distribution', 'system', 'virt', 'ipv4', 'network']
    gather_subset = ['all', '!facter', 'devices']

# Generated at 2022-06-13 00:27:30.728287
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    class TestClass(BaseFactCollector):
        _fact_ids = set(['testfact'])
        name = 'test'

    assert build_fact_id_to_collector_map([TestClass]) == ({'test': [TestClass], 'testfact': [TestClass]},
                                                           defaultdict(set, {'test': {'testfact'}}))


# Generated at 2022-06-13 00:27:42.976317
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    collector_names = set(['this', 'that'])
    all_fact_subsets = {
        'this': [FakeCollector('this', ['another']), FakeCollector('this', ['that'])],
        'that': [FakeCollector('that', ['another'])]
    }
    # returns empty set
    assert not find_unresolved_requires(collector_names, all_fact_subsets)

    all_fact_subsets = {
        'this': [FakeCollector('this', ['another']), FakeCollector('this', ['that'])],
        'that': [FakeCollector('that', ['another'])],
        'another': [FakeCollector('another', [])]
    }
    # returns empty set

# Generated at 2022-06-13 00:27:47.750313
# Unit test for function tsort

# Generated at 2022-06-13 00:28:11.833727
# Unit test for function tsort
def test_tsort():
    test_dep_map = {'1': {'3', '4'},
                    '2': {'4'},
                    '3': {'4'},
                    '4': {}}
    result = [('1', {'3', '4'}),
              ('2', {'4'}),
              ('3', {'4'}),
              ('4', set())]
    assert tsort(test_dep_map) == result
    assert tsort(test_dep_map) != [('1', {'3', '4'}),
                                   ('3', {'4'}),
                                   ('2', {'4'}),
                                   ('4', set())]



# Generated at 2022-06-13 00:28:18.189124
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    from ansible.module_utils.facts.collectors import cache
    fact_id_to_collector_map, aliases_map = build_fact_id_to_collector_map(cache.collectors_for_platform)
    assert aliases_map['ssh_pub_keys'].difference(set(('authorized_keys', 'ssh_authorized_keys', 'ssh_keys'))) == set()



# Generated at 2022-06-13 00:28:25.404818
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    # required for test_find_unresolved_requires
    from ansible.module_utils.facts.collectors import all_collectors

    ansible_facts_map, ansible_facts_aliases_map = build_fact_id_to_collector_map(all_collectors)

    collector_names = ['facter', 'file']
    assert find_unresolved_requires(collector_names, ansible_facts_map) == set(['facter'])
    collector_names = ['file', 'facter']
    assert find_unresolved_requires(collector_names, ansible_facts_map) == set()



# Generated at 2022-06-13 00:28:37.471440
# Unit test for function get_collector_names
def test_get_collector_names():

    valid_subsets = frozenset(['first', 'second', 'third', 'fourth', 'fifth'])

    def testwith(gather_subset, result):
        res = get_collector_names(
            valid_subsets=valid_subsets,
            gather_subset=gather_subset,
        )
        assert frozenset(res) == frozenset(result)

    testwith(None, ('first', 'second', 'third', 'fourth', 'fifth'))
    testwith([], ('first', 'second', 'third', 'fourth', 'fifth'))
    testwith(['all'], ('first', 'second', 'third', 'fourth', 'fifth'))
    testwith(['!'], ('first', 'second', 'third', 'fourth', 'fifth'))
    testwith(['min'], ())

# Generated at 2022-06-13 00:28:48.213560
# Unit test for function get_collector_names
def test_get_collector_names():
    # Test with empty subset
    assert get_collector_names() == {'all'}
    # Test with subset of 'all'
    assert get_collector_names(gather_subset=['all']) == {'all'}
    # Test with subset of 'min'
    assert get_collector_names(gather_subset=['min']) == frozenset(['min'])
    # Test with subset of ['!all', 'min']
    assert get_collector_names(gather_subset=['!all', 'min']) == frozenset(['min'])
    # Test with subset of ['!min', 'all']
    assert get_collector_names(gather_subset=['!min', 'all']) == frozenset(['all'])
    # Test with subset of ['

# Generated at 2022-06-13 00:28:57.893921
# Unit test for function get_collector_names
def test_get_collector_names():
    _all_subsets = frozenset(['a', 'b', 'c'])
    _minimal_subsets = frozenset(['e', 'f'])
    _aliases_map = defaultdict(set)
    _aliases_map['hardware'].update(('devices', 'dmi'))

    # Test minimal_subsets over all_subsets
    subset_names = get_collector_names(_all_subsets, _minimal_subsets, ['dmi'])
    assert 'e' in subset_names
    assert 'f' in subset_names
    assert 'dmi' in subset_names
    assert 'devices' in subset_names
    assert len(subset_names) == 4


# Generated at 2022-06-13 00:29:07.374585
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    class A(BaseFactCollector):
        _fact_ids = frozenset(['a', 'aa'])
        name = 'a'
        required_facts = set()

    class B(BaseFactCollector):
        _fact_ids = frozenset(['b', 'bb'])
        name = 'b'
        required_facts = set()

    class C(BaseFactCollector):
        _fact_ids = frozenset(['c', 'cc'])
        name = 'c'
        required_facts = set()

    expected_fact_id_to_collector_map = {
        'a': [A],
        'aa': [A],
        'b': [B],
        'bb': [B],
        'c': [C],
        'cc': [C],
    }
    expected_

# Generated at 2022-06-13 00:29:16.535315
# Unit test for function find_collectors_for_platform
def test_find_collectors_for_platform():
    from ansible.module_utils.facts.collector.macosx import MacOSXHardwareCollector
    from ansible.module_utils.facts.collector.linux import LinuxHardwareCollector
    from ansible.module_utils.facts.collector.network import NetworkCollector
    from ansible.module_utils.facts.collector.windows import WindowsHardwareCollector

    class TestPlatform:
        def __init__(self, system, release):
            self.system = system
            self.release = release

    LinuxHardwareCollector._platform = 'Linux'
    LinuxHardwareCollector.name = 'linux_hw'

    WindowsHardwareCollector._platform = 'Windows'
    WindowsHardwareCollector.name = 'windows_hw'

    MacOSXHardwareCollector._platform = 'Darwin'

# Generated at 2022-06-13 00:29:27.284965
# Unit test for function get_collector_names
def test_get_collector_names():
    from ansible.module_utils.facts import _get_platform_subset_info
    platform_info = _get_platform_subset_info(platform.system(), platform.release())

    # Each platform has different subsets, so we add the subset we need for each platform
    if platform_info.get('system', None) == 'Linux':
        valid_subsets = frozenset(['all', 'network', 'virtual', 'hardware', 'fibrechannel', 'system', 'logging', 'storage'])
    elif platform_info.get('system', None) == 'FreeBSD':
        valid_subsets = frozenset(['all', 'network', 'virtual', 'hardware', 'system'])

# Generated at 2022-06-13 00:29:38.997679
# Unit test for function find_collectors_for_platform
def test_find_collectors_for_platform():
    import ansible.module_utils.facts.collectors.network as network
    from ansible.module_utils.facts.collectors.network import NetworkCollectorFact
    import ansible.module_utils.facts.collectors.system as system
    from ansible.module_utils.facts.collectors.system import SystemCollectorFact
    import ansible.module_utils.facts.collectors.virtual as virtual
    from ansible.module_utils.facts.collectors.virtual import VirtualCollectorFact

    all_collector_classes = [NetworkCollectorFact, SystemCollectorFact, VirtualCollectorFact]
    compat_platform = [{'system':'Generic',
                        'distribution': 'Generic'},
                       {'system':'Linux',
                        'distribution': 'Generic'}]
    found_collectors = find_collectors_for_

# Generated at 2022-06-13 00:30:01.637831
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    # pylint: disable=unused-argument,no-value-for-parameter,no-self-use
    class MockCollector:
        def __init__(self, name, requires_facts=None):
            self.name = name
            self.required_facts = requires_facts or set()

    def unf(collector_names, all_fact_subsets):
        return find_unresolved_requires(collector_names, all_fact_subsets)

    c1 = MockCollector('1', ('2', '3'))
    c2 = MockCollector('2', ('3',))
    c3 = MockCollector('3', ('4',))
    c4 = MockCollector('4', ('5',))
    c5 = MockCollector('5')

    all_fact_subsets = {}
    all

# Generated at 2022-06-13 00:30:14.420226
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    # TODO: replace with a less complex mock for testing
    class MockCollector(BaseFactCollector):
        pass
    class MockCollector_A(BaseFactCollector):
        name = 'A'
        required_facts = set(['B'])
    class MockCollector_B(BaseFactCollector):
        name = 'B'
        required_facts = set(['C'])
    class MockCollector_C(BaseFactCollector):
        name = 'C'
        required_facts = set()
    class MockCollector_D(BaseFactCollector):
        name = 'D'
        required_facts = set(['E', 'F'])
    class MockCollector_E(BaseFactCollector):
        name = 'E'
        required_facts = set()

# Generated at 2022-06-13 00:30:25.312414
# Unit test for function get_collector_names
def test_get_collector_names():

    def get_all_subsets_for_gather_subset(gather_subset, minimal=frozenset()):
        return get_collector_names(gather_subset=gather_subset,
                                   valid_subsets=frozenset(['network', 'hardware', 'virtual', 'facter']),
                                   minimal_gather_subset=minimal)

    def test_gather_subset(gather_subset, expected_result, minimal=frozenset()):
        result = get_all_subsets_for_gather_subset(gather_subset, minimal)
        assert result == frozenset(expected_result), "'%s' %s %s" % (gather_subset, result, expected_result)


# Generated at 2022-06-13 00:30:35.221761
# Unit test for function find_collectors_for_platform
def test_find_collectors_for_platform():
    '''test find_collectors_for_platform by passing it some invalid/valid input'''


# Generated at 2022-06-13 00:30:40.645646
# Unit test for function get_collector_names
def test_get_collector_names():
    '''Test for function `get_collector_names`.
    '''
    valid_subsets = frozenset(['hardware', 'network'])
    debug_collectors = get_collector_names(valid_subsets=valid_subsets, gather_subset=['all'])
    assert len(debug_collectors) == 2
    debug_collectors = get_collector_names(valid_subsets=valid_subsets, gather_subset=['hardware'])
    assert len(debug_collectors) == 1
    debug_collectors = get_collector_names(valid_subsets=valid_subsets, gather_subset=['!hardware'])
    assert len(debug_collectors) == 1

# Generated at 2022-06-13 00:30:51.879152
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    # mock all_fact_subsets so that we can test this function in isolation
    all_fact_subsets = {
        'a': [object()],
        'b': [object()],
        'c': [object()],
    }

    # collector b requires a and this is set up by _get_requires_by_collector_name
    def mock_get_requires_by_collector_name(collector_name, all_fact_subsets):
        if collector_name == 'b':
            return {'a'}
        return set()

    # ensure that 'b' is listed as unresolved if it requires 'a'

# Generated at 2022-06-13 00:30:57.842549
# Unit test for function find_collectors_for_platform
def test_find_collectors_for_platform():
    from ansible.module_utils.facts.collectors import network
    all_collector_classes = (network.NetworkCollector, )
    assert find_collectors_for_platform(all_collector_classes, [{'system': 'Linux'}]) == set()
    assert find_collectors_for_platform(all_collector_classes, [{'system': 'Generic'}]) == set([network.NetworkCollector])
    assert find_collectors_for_platform(all_collector_classes, [{'system': 'Generic'}, {'system': 'Linux'}]) == set([network.NetworkCollector])



# Generated at 2022-06-13 00:31:09.163625
# Unit test for function build_dep_data
def test_build_dep_data():
    # Test case 1
    all_fact_subsets = {'1': [1], '2': [2], '3': [3]}
    collector_names = ['1']
    dep_map = build_dep_data(collector_names, all_fact_subsets)
    assert dep_map == {'1': {}}

    # Test case 2
    all_fact_subsets = {'1': [1], '2': [2], '3': [3]}
    collector_names = ['1', '2']
    dep_map = build_dep_data(collector_names, all_fact_subsets)
    assert dep_map == {'1': {}, '2': {}}

    # Test case 3

# Generated at 2022-06-13 00:31:16.451929
# Unit test for function build_dep_data
def test_build_dep_data():
    class FactCollectorX(BaseFactCollector):
        _fact_ids = ('basic', )
        required_facts = ('dep_unknown', )

    class FactCollectorY(BaseFactCollector):
        _fact_ids = ('basic', )
        required_facts = ('dep_unknown', )

    class FactCollectorZ(BaseFactCollector):
        _fact_ids = ('z', )
        required_facts = ('dep_unknown', )

    class FactCollectorA(BaseFactCollector):
        _fact_ids = ('a', )
        required_facts = ('z', 'basic', )

    class FactCollectorB(BaseFactCollector):
        _fact_ids = ('b', )
        required_facts = ('z', 'basic', )

    class FactCollectorC(BaseFactCollector):
        _fact_

# Generated at 2022-06-13 00:31:26.522365
# Unit test for function find_collectors_for_platform
def test_find_collectors_for_platform():
    assert find_collectors_for_platform([], []) == set()

    class Collector1(BaseFactCollector):
        _platform = 'CAT'
        name = 'CAT_collector'

        def collect(self, module=None, collected_facts=None):
            return {'cat': True}

    class Collector2(BaseFactCollector):
        _platform = 'DOG'
        name = 'DOG_collector'

        def collect(self, module=None, collected_facts=None):
            return {'dog': True}

    class Collector3(BaseFactCollector):
        _platform = 'GOOSE'
        name = 'GOOSE_collector'

        def collect(self, module=None, collected_facts=None):
            return {'goose': True}


# Generated at 2022-06-13 00:31:54.349893
# Unit test for function find_collectors_for_platform
def test_find_collectors_for_platform():
    class W(BaseFactCollector):
        _platform = 'Generic'
        name = 'so'
    class X(BaseFactCollector):
        _platform = 'Generic'
        name = 'some'
    class Y(BaseFactCollector):
        _platform = 'Generic'
        name = 'something'
    class Z(BaseFactCollector):
        _platform = 'Generic'
        name = 'somethingelse'
    all_collectors = [W, X, Y, Z]
    compat_platforms = [{'system': 'Generic'}]
    found_collectors = find_collectors_for_platform(all_collectors, compat_platforms)
    assert (found_collectors == set(all_collectors))
    # some classes not compat with this platform

# Generated at 2022-06-13 00:32:00.561576
# Unit test for function build_dep_data
def test_build_dep_data():
    from ansible.module_utils.facts.collector.networking import NetworkingFactCollector
    from ansible.module_utils.facts.collector.platform import PlatformFactCollector
    from ansible.module_utils.facts.collector.pkg_mgr import PkgMgrFactCollector

    collectors = [
        PlatformFactCollector,
        NetworkingFactCollector,
        PkgMgrFactCollector
    ]

    collector_names = set()
    for collector in collectors:
        collector_names |= collector._fact_ids

    fact_deps = build_dep_data(collector_names, all_fact_subsets)
    assert 'pkg_mgr' in fact_deps
    assert 'platform' in fact_deps['pkg_mgr']

# Generated at 2022-06-13 00:32:09.969093
# Unit test for function find_collectors_for_platform
def test_find_collectors_for_platform():
    import sys
    class f1(BaseFactCollector):
        name = 'f1'
        _platform = 'generic'
    class f2(BaseFactCollector):
        name = 'f2'
        _platform = 'Linux'
    class f3(BaseFactCollector):
        name = 'f3'
        _platform = 'Linux'

    all_collectors = [f1, f2, f3]

    platform_info_generic = {'system': 'generic'}
    platform_info_linux = {'system': 'Linux'}

    # no match
    found = find_collectors_for_platform(all_collectors, [{'system': 'XXX'}])
    assert not found

    # generic match

# Generated at 2022-06-13 00:32:18.738170
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    from ansible.module_utils.facts.collector import BaseFactCollector

    # we're not testing here that this is a valid fact name, just that the
    # functions work.
    valid_fact_names = frozenset(['f1', 'f2', 'f3'])

    # we're not testing that BaseFactCollector is a good mock here, just that the
    # functions work.
    class FC1(BaseFactCollector):
        name = 'f1'
        required_facts = set(['f2', 'f3'])

    class FC2(BaseFactCollector):
        name = 'f2'

    class FC3(BaseFactCollector):
        name = 'f3'
        required_facts = set(['f2'])


# Generated at 2022-06-13 00:32:27.104129
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    from ansible.module_utils.facts.collector import BaseFactCollector

    class CollectorA(BaseFactCollector):
        name = 'a'
        required_facts = set(['b'])

    class CollectorB(BaseFactCollector):
        name = 'b'
        required_facts = set(['c'])

    class CollectorC(BaseFactCollector):
        name = 'c'

    all_fact_subsets = {
        'a': [CollectorA],
        'b': [CollectorB],
        'c': [CollectorC],
    }

    assert find_unresolved_requires(['a'], all_fact_subsets) == set(['c'])
    assert find_unresolved_requires(['b'], all_fact_subsets) == set(['c'])
   

# Generated at 2022-06-13 00:32:35.273200
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    """Validate find_unresolved_requires.

    This test uses a dummy collector class with manually defined
    required facts.
    """
    class my_collector(BaseFactCollector):
        required_facts = ['test_fact']
        name = 'my_collector'

    test_fact_subsets = defaultdict(list)
    test_fact_subsets[my_collector.name].append(my_collector)

    collector_names = ['test_fact']
    assert find_unresolved_requires(collector_names, test_fact_subsets) == set(['test_fact'])



# Generated at 2022-06-13 00:32:44.610595
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    import ansible.module_utils.network.common.fact_collectors.base
    import ansible.module_utils.network.common.fact_collectors.network
    import ansible.module_utils.network.common.fact_collectors.types
    import ansible.module_utils.network.common.fact_collectors.vendor

    # setup
    results = {
        'ansible_network_os': 'ios',
        'ansible_system': 'ios',
        'ansible_network_os_version': '15.4',
        'ansible_system_version': '15.4',
    }

    # Test

# Generated at 2022-06-13 00:32:49.847358
# Unit test for function get_collector_names
def test_get_collector_names():
    assert get_collector_names(valid_subsets=('foo', 'bar', 'baz'), gather_subset=('foo',)) == set(['foo'])
    assert get_collector_names(valid_subsets=('foo', 'bar', 'baz'), gather_subset=('!foo',)) == set(['bar', 'baz'])
    assert get_collector_names(valid_subsets=('foo', 'bar', 'baz'), gather_subset=('!foo', 'bar')) == set(['bar'])



# Generated at 2022-06-13 00:33:00.949154
# Unit test for function get_collector_names
def test_get_collector_names():
    # Passing gather_subset with 'all'
    # Expected result: Return all Facts from 'valid_subsets'
    valid_subsets = frozenset(['eth1', 'eth2', 'eth0', 'min'])
    minimal_gather_subset = frozenset(['eth2'])
    gather_subset = ['all']
    aliases_map = defaultdict(set)
    assert get_collector_names(valid_subsets, minimal_gather_subset, gather_subset, aliases_map) == valid_subsets

    # Passing gather_subset with 'all' and aliases_map
    # Expected result: Return all Facts found in 'aliases_map'

# Generated at 2022-06-13 00:33:11.664609
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    class TestCollector1(BaseFactCollector):
        _fact_ids = ['test_fact_id1']
        name = 'test_name1'

        def collect(self):
            return dict(test_fact_id1='value1')

    class TestCollector2(BaseFactCollector):
        _fact_ids = ['test_fact_id2']
        name = 'test_name2'

        def collect(self):
            return dict(test_fact_id2='value2')

    class TestCollector3(BaseFactCollector):
        _fact_ids = ['test_fact_id3']
        name = 'test_name3'

        def collect(self):
            return dict(test_fact_id3='value3')


# Generated at 2022-06-13 00:33:30.755569
# Unit test for function get_collector_names
def test_get_collector_names():
    aliases_map = defaultdict(set)
    for alias, names in [('all', ('hardware', 'network', 'interfaces', 'virtual')), ('hardware', ('dmi', 'devices'))]:
        aliases_map[alias].update(names)

    MODULE_RETURN = dict(failed=False,
                         changed=False,
                         ansible_facts=dict(ansible_system='Linux'))


# Generated at 2022-06-13 00:33:41.803814
# Unit test for function get_collector_names
def test_get_collector_names():
    all_subsets = frozenset(['a', 'b', 'c', 'd', 'e'])
    minimal_subsets = frozenset(['a'])
    aliases = {'d': set(['d1', 'd2'])}


# Generated at 2022-06-13 00:33:52.108147
# Unit test for function build_dep_data
def test_build_dep_data():
    from ansible.module_utils.facts.system.base import BaseFactCollector as SystemfactCollector
    from ansible.module_utils.facts.virtual.base import BaseFactCollector as VirtualfactCollector
    from ansible.module_utils.facts.cpu.base import BaseFactCollector as CpufactCollector
    from ansible.module_utils.facts.network.base import BaseFactCollector as NetworkfactCollector
    all_fact_subsets = {
        "system": [SystemfactCollector],
        "virtual": [VirtualfactCollector],
        "cpu": [CpufactCollector],
        "network": [NetworkfactCollector]
    }
    collector_names = set(["system", "virtual", "cpu", "network"])

# Generated at 2022-06-13 00:33:59.517013
# Unit test for function get_collector_names
def test_get_collector_names():
    # when gather_subset=='all', returns everything that is valid for the platform.
    #    This is the usual case.
    assert get_collector_names(frozenset(['some_fact', 'another_fact']), '', ['all']) == set(['another_fact', 'some_fact'])
    # when gather_subset=='some_fact', return just that fact.
    assert get_collector_names(frozenset(['some_fact', 'another_fact']), '', ['some_fact']) == set(['some_fact'])
    # when gather_subset=='!some_fact, still return the min

# Generated at 2022-06-13 00:34:08.241980
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    valid = frozenset(['collector1', 'collector2', 'collector3', 'collector4'])

    deps = {
        'collector1': ['collector2'],
        'collector2': ['collector3'],
        'collector3': [],
        'collector4': ['collector1', 'collector3'],
    }

    def _get_requires_by_collector_name(collector_name):
        return set(deps[collector_name])

    unresolved = find_unresolved_requires(['collector1'], deps,
                                          _get_requires_by_collector_name)

    assert not unresolved

    # requires for collector4 exist, but are not in the set, so
    # this will return collector1 and collector3
    unresolved = find_