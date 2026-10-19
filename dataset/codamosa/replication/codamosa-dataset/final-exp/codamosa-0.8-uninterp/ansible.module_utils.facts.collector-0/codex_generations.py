

# Generated at 2022-06-13 00:24:32.738473
# Unit test for function build_dep_data
def test_build_dep_data():
    all_fact_subsets = {
        'test1': [BaseFactCollector],
        'test2': [BaseFactCollector],
        'test3': [BaseFactCollector],
        'test4': [BaseFactCollector],
    }

    collector_names = {'test1', 'test2', 'test3', 'test4'}

    dep_map_answer = {
        'test1': {'test1', 'test2', 'test3'},
        'test2': {'test1', 'test2', 'test3'},
        'test3': {'test1', 'test2', 'test3'},
        'test4': {'test1', 'test2', 'test3', 'test4'},
    }


# Generated at 2022-06-13 00:24:41.705815
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    class SimpleCollector(BaseFactCollector):
        _fact_ids = ()
        name = 'foo'
        required_facts = ('bar',)

    class ComplexCollector(BaseFactCollector):
        _fact_ids = ('foo', 'boo')
        name = 'baz'
        required_facts = ('bar', 'bif', 'boo')

    fact_id_to_collector_map = {
        'foo': [SimpleCollector],
        'baz': [ComplexCollector],
    }

    unresolved = find_unresolved_requires(['foo', 'baz'], fact_id_to_collector_map)
    assert unresolved == {'bar', 'bif'}



# Generated at 2022-06-13 00:24:47.881175
# Unit test for function select_collector_classes
def test_select_collector_classes():
    class CollectorA(BaseFactCollector):
        _platform = 'Linux'
        _fact_ids = ['a']
        name = 'a'

    class CollectorB(BaseFactCollector):
        _platform = 'Linux'
        _fact_ids = ['b']
        name = 'b'

    class CollectorA2(CollectorA):
        _platform = 'Linux'
        _fact_ids = ['a']
        name = 'a2'

    class CollectorC(BaseFactCollector):
        _platform = 'Linux'
        _fact_ids = ['c']
        name = 'c'

    class CollectorD(BaseFactCollector):
        _platform = 'Linux'
        _fact_ids = ['d']
        name = 'd'
        required_facts = ['a2']


# Generated at 2022-06-13 00:24:55.611294
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    all_fact_subsets = {
        'a': [object()],
        'b': [object()],
        'c': [object()],
    }

    # Test the case where there are no unresolved fact collector names
    result = find_unresolved_requires(['a'], all_fact_subsets)
    assert not result

    # Test the case where 1/3 of the requested fact collectors has unresolved fact collector
    # requirements
    result = find_unresolved_requires(['a', 'b', 'c'], all_fact_subsets)
    assert 'b' in result



# Generated at 2022-06-13 00:25:07.064167
# Unit test for function find_collectors_for_platform
def test_find_collectors_for_platform():
    # Create simple dummy class for tests.
    class dummy_class1:
        _fact_ids = set()
        _platform = 'Generic'
        name = 'CIMC'
        required_facts = set()
        def __init__(self, collectors=None, namespace=None):
            self.collectors = collectors or []
            self.namespace = namespace
            self.fact_ids = set([self.name])
            self.fact_ids.update(self._fact_ids)

    class dummy_class2:
        _fact_ids = set()
        _platform = 'Linux'
        name = 'CIMC'
        required_facts = set()
        def __init__(self, collectors=None, namespace=None):
            self.collectors = collectors or []
            self.namespace = namespace
            self.fact_

# Generated at 2022-06-13 00:25:18.514840
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    class CollectorA(BaseFactCollector):
        name = 'A'
    class CollectorB(BaseFactCollector):
        name = 'B'
        required_facts = frozenset(['A'])
    class CollectorC(BaseFactCollector):
        name = 'C'
        required_facts = frozenset(['B', 'D'])
    class CollectorD(BaseFactCollector):
        name = 'D'
        required_facts = frozenset(['B'])

    fake_subsets = {
        'A': [CollectorA],
        'B': [CollectorB],
        'C': [CollectorC],
        'D': [CollectorD],
    }

    unresolved = find_unresolved_requires(['B', 'C', 'D'], fake_subsets)

# Generated at 2022-06-13 00:25:26.821029
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    class MockCollector:
        def __init__(self, name, required_facts=set()):
            self.name = name
            self.required_facts = set(required_facts)

    from ansible.module_utils import facts
    facts.os_data = {
        'default': {
            'network_gather_subset': ['default'],
        },
    }

    collector_names = frozenset([
        'a',
        'b',
        'c',
    ])

    # collectors_for_platform is a mapping of fact sets
    # to a collection of collector classes
    # Ex, if a system has 'a', 'b', and 'c',
    # it should have 'default'

# Generated at 2022-06-13 00:25:38.114381
# Unit test for function build_dep_data
def test_build_dep_data():
    dep_map = {
        'a': set(['b']),
        'b': set(['c']),
        'c': set(['d']),
        'd': set(['e']),
        'e': set(),
    }

    collector_names = ['a']

    all_fact_subsets = {}

    def _get_collector_class(name):
        collector_cls = type(name, (BaseFactCollector,), {})
        collector_cls.name = name
        collector_cls.required_facts = dep_map[name]
        collector_cls._fact_ids = set()
        return collector_cls

    for dep_name, dep_deps in dep_map.items():
        collector_class = _get_collector_class(dep_name)
        all_

# Generated at 2022-06-13 00:25:39.679603
# Unit test for function build_dep_data
def test_build_dep_data():
    # FIXME: implement build_dep_data unit test
    pass



# Generated at 2022-06-13 00:25:48.864496
# Unit test for function find_unresolved_requires

# Generated at 2022-06-13 00:26:05.884489
# Unit test for function get_collector_names
def test_get_collector_names():

    valid_subsets = frozenset(['a', 'b', 'c'])
    minimal_gather_subset = frozenset(['a'])
    aliases_map = {
        'foo': set('a'),
        'bar': set('b', 'c'),
    }

    # by default, 'all' is used, so we get all the facts
    assert get_collector_names(valid_subsets, minimal_gather_subset,
                               aliases_map=aliases_map) == frozenset(['a', 'b', 'c'])

    assert get_collector_names(valid_subsets, minimal_gather_subset,
                               aliases_map=aliases_map,
                               gather_subset=['!all']) == frozenset()

    # we get all the valid subs

# Generated at 2022-06-13 00:26:16.388447
# Unit test for function build_dep_data
def test_build_dep_data():
    test_data = {
        'example_1': {
            'collector_names': {'a', 'b', 'c', 'd', 'e', 'f'},
            'expected': {'a': {}, 'b': {'a'}, 'c': {'a', 'b'}, 'd': {'b', 'c'}, 'e': {}, 'f': {'a', 'e'}, },
        },
        'example_2': {
            'collector_names': {'a', 'b', 'c', 'd', 'e', 'f'},
            'expected': {'a': {}, 'b': {}, 'c': {}, 'd': {}, 'e': {}, 'f': {}},
        }
    }


# Generated at 2022-06-13 00:26:24.753173
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    collector_names = {'a', 'b', 'c', 'd', 'e', 'f'}
    all_fact_subsets = {
        'a': [MockCollectorClass(name='a', required_facts=set(['b', 'c']))],
        'b': [MockCollectorClass(name='b', required_facts=set(['c']))],
        'c': [MockCollectorClass(name='c', required_facts=set(['e']))],
        'd': [MockCollectorClass(name='d', required_facts=set(['f']))],
        'e': [MockCollectorClass(name='e', required_facts=set())],
        'f': [MockCollectorClass(name='f', required_facts=set())],
    }
    assert find

# Generated at 2022-06-13 00:26:36.022751
# Unit test for function tsort
def test_tsort():
    data = [
        ('A', 'B'),
        ('B', 'C'),
        ('E', 'D'),
        ('D', 'C'),
    ]
    dep_map = {}
    for (key, value) in data:
        dep_map[key] = dep_map.get(key, set())
        dep_map[key].add(value)

    sorted_list = [
        ('A', ('B',)),
        ('B', ('C',)),
        ('E', ('D',)),
        ('D', ('C',)),
    ]
    assert tsort(dep_map) == sorted_list
    assert tsort(dep_map) == sorted_list


# Generated at 2022-06-13 00:26:45.457440
# Unit test for function select_collector_classes
def test_select_collector_classes():
    my_collector = BaseFactCollector
    my_collector._fact_ids = set(['foo', 'bar'])

    another_collector = BaseFactCollector
    another_collector._fact_ids = set(['foo', 'bar', 'another'])

    my_other_collector = BaseFactCollector
    my_other_collector._fact_ids = set(['foo'])

    my_random_collector = BaseFactCollector
    my_random_collector._fact_ids = set(['random'])


# Generated at 2022-06-13 00:26:54.710039
# Unit test for function build_dep_data
def test_build_dep_data():
    class A(BaseFactCollector):
        required_facts = set([])
        name = 'a'
    class B(BaseFactCollector):
        required_facts = set(['a'])
        name = 'b'
    class C(BaseFactCollector):
        required_facts = set(['a'])
        name = 'c'
    class D(BaseFactCollector):
        required_facts = set(['b', 'c'])
        name = 'd'
    all_fact_subsets = {'a': [A], 'b': [B], 'c': [C], 'd': [D]}
    deps = build_dep_data(['a', 'b', 'c', 'd'], all_fact_subsets)

# Generated at 2022-06-13 00:27:06.366498
# Unit test for function build_dep_data
def test_build_dep_data():
    from ansible.module_utils.facts.collector import setup_collector_names
    from ansible.module_utils.facts.collector import build_fact_id_to_collector_map
    from ansible.module_utils.facts.collector import select_collector_classes

    all_collector_classes = [
        TestCollectorA,
        TestCollectorB,
        TestCollectorC,
        TestCollectorD,
    ]

    fact_subset_names = {'all', 'test'}

    minimal_gather_subset = {'min'}

    gather_subset = {'all'}


# Generated at 2022-06-13 00:27:14.454090
# Unit test for function find_collectors_for_platform
def test_find_collectors_for_platform():
    import pytest

    # Build up a fake set of collectors to test with.
    # This test will never include the "min" collector.
    class TestCollectorA(BaseFactCollector):
        pass
    class TestCollectorB(BaseFactCollector):
        pass
    class TestCollectorC(BaseFactCollector):
        pass

    # TestCollectorA should match All platforms
    TestCollectorA._platform = 'Generic'
    TestCollectorA.name = 'collector_a'

    # TestCollectorB should only match Linux
    TestCollectorB._platform = 'Linux'
    TestCollectorB.name = 'collector_b'

    # TestCollectorC should only match FreeBSD
    TestCollectorC._platform = 'FreeBSD'
    TestCollectorC.name = 'collector_c'

    # Def

# Generated at 2022-06-13 00:27:25.747034
# Unit test for function find_collectors_for_platform
def test_find_collectors_for_platform():
    class TestCollector(BaseFactCollector):
        _fact_ids = {'collector_K'}
        _platform = 'Test'
        name = 'collector_A'
        required_facts = {'fact_foo'}
    class TestCollector2(BaseFactCollector):
        _fact_ids = {'collector_M'}
        _platform = 'Test'
        name = 'collector_B'
        required_facts = {'fact_bar'}
    class TestCollector3(BaseFactCollector):
        _fact_ids = {'collector_M'}
        _platform = 'Test'
        name = 'collector_B'
        required_facts = {'fact_zoo'}


# Generated at 2022-06-13 00:27:35.895890
# Unit test for function find_collectors_for_platform
def test_find_collectors_for_platform():
    """
    Example of Collector class used in the testing function
    """
    class ACollector(BaseFactCollector):
        name = 'a'
        _platform = 'Aplatform'

    class BCollector(BaseFactCollector):
        name = 'b'
        _platform = 'Bplatform'

    class CCollector(BaseFactCollector):
        name = 'c'
        _platform = 'Cplatform'

    class DCollector(BaseFactCollector):
        name = 'd'
        _platform = 'Dplatform'

    class ECollector(BaseFactCollector):
        name = 'e'
        _platform = 'Eplatform'

    class FCollector(BaseFactCollector):
        name = 'f'
        _platform = 'Fplatform'


# Generated at 2022-06-13 00:27:51.526780
# Unit test for function get_collector_names
def test_get_collector_names():
    def _check_get_collector_names(gather_subset,
                                   valid_subsets,
                                   minimal_gather_subsets,
                                   expected_result,
                                   expected_error=None):
        '''Helper function for test_get_collector_names'''
        try:
            result = get_collector_names(gather_subset=gather_subset,
                                         valid_subsets=valid_subsets,
                                         minimal_gather_subset=minimal_gather_subsets)
            assert result == expected_result, "%s != %s" % (result, expected_result)
        except Exception as e:
            if expected_error is None:
                raise

# Generated at 2022-06-13 00:27:58.483474
# Unit test for function get_collector_names
def test_get_collector_names():
    all_subsets = frozenset(['all'])
    assert(get_collector_names() == all_subsets)
    assert(get_collector_names(gather_subset=[]) == all_subsets)
    assert(get_collector_names(gather_subset=['all']) == all_subsets)
    assert(get_collector_names(gather_subset=['foo']) == frozenset(['foo', 'all']))
    assert(get_collector_names(gather_subset=['foo', 'bar']) == frozenset(['foo', 'bar', 'all']))
    assert(get_collector_names(gather_subset=['!foo']) == frozenset(['all']))

# Generated at 2022-06-13 00:28:05.606184
# Unit test for function find_collectors_for_platform
def test_find_collectors_for_platform():
    from ansible.module_utils.facts.collector.system import SystemCollector as SystemCollector_
    from ansible.module_utils.facts.collector.network import DefaultNetworkCollector as DefaultNetworkCollector_
    from ansible.module_utils.facts.collector.network import LinuxNetworkCollector as LinuxNetworkCollector_
    from ansible.module_utils.facts.collector.network import OpenBSDNetworkCollector as OpenBSDNetworkCollector_
    from ansible.module_utils.facts.collector.network import NetBSDNetworkCollector as NetBSDNetworkCollector_
    from ansible.module_utils.facts.collector.network import FreeBSDNetworkCollector as FreeBSDNetworkCollector_
    from ansible.module_utils.facts.collector.network import DarwinNetworkCollector as DarwinNetworkCollector_

# Generated at 2022-06-13 00:28:09.778681
# Unit test for function collector_classes_from_gather_subset
def test_collector_classes_from_gather_subset():
    # Arrange
    from ansible.module_utils.facts.collectors.all import AllFactCollector
    from ansible.module_utils.facts.collectors.network import NetworkCollector

    valid_subsets = frozenset(('all', 'hardware'))
    minimal_gather_subsets = frozenset(('hardware'))

    all_collector_classes = [
        AllFactCollector,
        NetworkCollector
    ]

    # Act
    result = collector_classes_from_gather_subset(
        all_collector_classes=all_collector_classes,
        valid_subsets=valid_subsets,
        minimal_gather_subset=minimal_gather_subsets,
        gather_subset=['all'],
    )

    # Assert

# Generated at 2022-06-13 00:28:21.154698
# Unit test for function find_collectors_for_platform
def test_find_collectors_for_platform():
    from ansible.module_utils.facts import collector_linux
    from ansible.module_utils.facts import collector_windows
    from ansible.module_utils.facts import collector_network

    # Need to find a set of collectors for a platform
    (collector_linux_class, collector_windows_class, collector_network_class) = (collector_linux.LinuxFactCollector, collector_windows.WindowsFactCollector, collector_network.NetworkFactCollector)
    assert collector_linux_class.name == 'Linux'
    assert collector_windows_class.name == 'Windows'
    assert collector_network_class.name == 'Network'
    assert collector_linux_class.required_facts == frozenset({'kernel', 'os_family', 'system'})

# Generated at 2022-06-13 00:28:28.422288
# Unit test for function find_collectors_for_platform
def test_find_collectors_for_platform():

    # --- Mock module_utils.facts.utils.get_platform_info ---
    def get_platform_info():
        return {'system': 'Linux', 'version': '2.6.32-504.el6.x86_64'}

    # --- Mock class for collect facts ---
    class MockFactCollector:
        _fact_ids = set()

        _platform = 'Linux'
        name = None
        required_facts = set()

        def __init__(self, collectors=None, namespace=None):
            '''Base class for things that collect facts.

            'collectors' is an optional list of other FactCollectors for composing.'''
            self.collectors = collectors or []

            # self.namespace is a object with a 'transform' method that transforms
            # the name to indicate the namespace (ie, adds a prefix or suffix

# Generated at 2022-06-13 00:28:38.998397
# Unit test for function get_collector_names
def test_get_collector_names():
    # Bunch of aliases: hardware: [devices, dmi]
    aliases_map = defaultdict(set)
    aliases_map['hardware'].add('devices')
    aliases_map['hardware'].add('dmi')

    minimal_gather_subset = frozenset(['network'])
    valid_subsets = frozenset(['all', 'minimal', 'hardware', 'network', 'software', 'virtual'])
    # a bunch of test cases to ensure we have our act together

    gather_subset = ['all']
    expected_results = valid_subsets
    assert get_collector_names(valid_subsets, minimal_gather_subset, gather_subset, aliases_map) == expected_results

    gather_subset = ['all', '!minimal', '!software']
    expected_

# Generated at 2022-06-13 00:28:50.638221
# Unit test for function get_collector_names
def test_get_collector_names():
    def _fail(gather_subset, expected_error):
        try:
            get_collector_names(gather_subset=gather_subset)
        except TypeError as err:
            if str(err) == expected_error:
                return
            raise
        else:
            raise AssertionError("expected to get exception with ['%s'] but didnt" % expected_error)

    # a subset that is only in gather_subset, which requires all to be present
    _fail('all,!foo', "Bad subset 'foo' given to Ansible. gather_subset options allowed: all")

    # one that is not in valid_subsets
    _fail('bar', "Bad subset 'bar' given to Ansible. gather_subset options allowed: all")

    # one in the valid list
    assert get_collector

# Generated at 2022-06-13 00:28:59.248162
# Unit test for function find_collectors_for_platform
def test_find_collectors_for_platform():
    # create a fake compatible platform
    platform_info = {'system': 'Linux'}

    # Create a fake fact collector for the platform
    class LinuxCollector(BaseFactCollector):
        _fact_ids = set()
        _platform = 'Linux'
        name = 'linux_name'
        required_facts = set()

        @classmethod
        def platform_match(cls, platform_info):
            if platform_info.get('system', None) == cls._platform:
                return cls
            return None

        def collect(self, module=None, collected_facts=None):
            return {}

    # The test itself
    compat_platforms = [platform_info]
    all_collector_classes = [LinuxCollector]

# Generated at 2022-06-13 00:29:09.465345
# Unit test for function tsort
def test_tsort():
    from nose.tools import assert_equals
    a_map = {
        'foo': set(['bar']),
        'bar': set(['baz']),
        'baz': set(),
        'quux': set(['quuux']),
        'quuux': set()
    }

    tsort_results = tsort(a_map)
    assert_equals(len(tsort_results), 5)

    # test for missing edges
    a_map_bad = a_map.copy()
    a_map_bad['quuux'] = set(['quux'])
    try:
        tsort(a_map_bad)
    except CycleFoundInFactDeps:
        pass
    else:
        assert False, 'tsort did not raise with a cycle in the graph'


# Generated at 2022-06-13 00:29:27.037418
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    all_fact_subsets = dict()

    class CollectorA(BaseFactCollector):
        name = 'a'
    all_fact_subsets['a'] = [CollectorA]

    class CollectorB(BaseFactCollector):
        name = 'b'
    all_fact_subsets['b'] = [CollectorB]

    class CollectorC(BaseFactCollector):
        name = 'c'
        required_facts = {'a'}
    all_fact_subsets['c'] = [CollectorC]

    class CollectorD(BaseFactCollector):
        name = 'd'
        required_facts = {'b'}
    all_fact_subsets['d'] = [CollectorD]

    class CollectorE(BaseFactCollector):
        name = 'e'

# Generated at 2022-06-13 00:29:36.208989
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    class TestCollector(BaseFactCollector):
        _fact_ids = set(('test_collector_alias1', 'test_collector_alias2'))
        name = 'test_collector'
    collectors_for_platform = [TestCollector]

    ret = build_fact_id_to_collector_map(collectors_for_platform)
    assert 'test_collector' in ret[0].keys()
    assert 'test_collector_alias1' in ret[0].keys()
    assert 'test_collector_alias2' in ret[0].keys()



# Generated at 2022-06-13 00:29:37.743007
# Unit test for function select_collector_classes
def test_select_collector_classes():
    # TODO: add test(s)
    pass


# Generated at 2022-06-13 00:29:45.675679
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    import platform
    import copy
    import pytest

    test_collector_names = [
        'custom',
        'network',
        'virtual',
        'min',
        'system',
        'all'
    ]
    # define test requirements for each collector name
    test_requirements = {
        'custom': ['custom'],
        'network': ['network'],
        'virtual': ['virtual'],
        'min': ['min'],
        'system': ['system'],
        'all': ['all']
    }
    # add to the dictionary with all collectors names

# Generated at 2022-06-13 00:29:56.998154
# Unit test for function build_dep_data
def test_build_dep_data():
    dep_map = defaultdict(set)
    dep_map['one'] = set(['two', 'three'])
    dep_map['two'] = set(['three'])
    dep_map['three'] = set()
    dep_map['four'] = set(['five'])
    dep_map['five'] = set()

    # make sure dep_map matches what we expect from dep_map
    assert(build_dep_data(['one', 'two', 'three', 'four', 'five'], dep_map) == dep_map)

    # make sure adding a collector with no dependencies doesn't add to the dep_map
    assert(build_dep_data(['one', 'two', 'three', 'four', 'five', 'six'], dep_map) != dep_map)

    # make sure adding a collector that has a

# Generated at 2022-06-13 00:30:03.715215
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
     collectors_for_platform = [
        {'name': 'A', 'required_facts': ['B']},
        {'name': 'B', 'required_facts': ['C']},
        {'name': 'C'},
        {'name': 'D', 'required_facts': ['E']},
        {'name': 'E'},
    ]

# Generated at 2022-06-13 00:30:15.418345
# Unit test for function get_collector_names
def test_get_collector_names():
    spec = 'platform'
    valid_subsets = set(['network', 'platform', 'all'])
    assert get_collector_names(valid_subsets, gather_subset=[spec]) == set([spec])

    spec = 'platform,!min'
    assert get_collector_names(valid_subsets, minimal_gather_subset=set(['distribution']), gather_subset=[spec]) == set(['platform'])

    # add extra aliases_map items to test
    aliases_map = defaultdict(set)
    aliases_map['hardware'].update(set(['devices']))
    aliases_map['hardware'].update(set(['dmi']))
    spec = 'hardware,!min'

# Generated at 2022-06-13 00:30:26.604608
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    from ansible.module_utils.facts.hardware.linux import LinuxHardware
    from ansible.module_utils.facts.hardware.linux import LinuxVirtual
    from ansible.module_utils.facts.hardware.linux import LinuxArch
    from ansible.module_utils.facts.hardware.linux import LinuxCpu
    from ansible.module_utils.facts.hardware.linux import LinuxDmi
    from ansible.module_utils.facts.hardware.linux import LinuxDevices
    from ansible.module_utils.facts.hardware.linux import LinuxMemory
    from ansible.module_utils.facts.system.distribution import Distribution


# Generated at 2022-06-13 00:30:33.897034
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    from ansible.module_utils.facts import collectors
    unordered = set(collectors.all_collector_classes)
    all_fact_subsets = defaultdict(set)
    for collector_class in collectors.all_collector_classes:
        all_fact_subsets[collector_class.name].add(collector_class)

    collectors_names = unordered - find_unresolved_requires(unordered, all_fact_subsets)

    assert set(collectors.all_collector_classes).issubset(set(collectors_names))



# Generated at 2022-06-13 00:30:43.161826
# Unit test for function select_collector_classes
def test_select_collector_classes():
    assert(select_collector_classes(['facter_linux_system'],
                                    {'facter_linux_system': [1, 2]}) == [1,2])
    assert(select_collector_classes(['facter_linux_system'],
                                    {'facter_linux_system': [1, 2],
                                     'facter_linux_dmi': [3, 4]}) == [1,2,3,4])
    assert(select_collector_classes(['facter_linux_system'],
                                    {'facter_linux_system': [1, 2],
                                     'facter_linux_dmi': [3, 4],
                                     'facter_linux_network': [2, 3]}) == [1,2,3,4])


# Generated at 2022-06-13 00:30:56.185215
# Unit test for function find_collectors_for_platform
def test_find_collectors_for_platform():

    class FCollector1(BaseFactCollector):
        _fact_ids = set()

        _platform = 'Windows'
        name = 'Name1'
        required_facts = set()

    class FCollector2(BaseFactCollector):
        _fact_ids = set()

        _platform = 'Linux'
        name = 'Name2'
        required_facts = set()

    class FCollector3(BaseFactCollector):
        _fact_ids = set()

        _platform = 'Generic'
        name = 'Name3'
        required_facts = set()

    all_collector_classes = [FCollector1, FCollector2, FCollector3]
    compat_platforms = [{'system': 'Windows'}]

# Generated at 2022-06-13 00:31:01.297482
# Unit test for function find_collectors_for_platform
def test_find_collectors_for_platform():
    platform_info = {
        'system': 'FreeBSD'
    }
    all_collector_classes = [BaseFactCollector]
    compat_platforms = platform_info
    assert not find_collectors_for_platform(all_collector_classes, compat_platforms)



# Generated at 2022-06-13 00:31:07.583206
# Unit test for function build_dep_data
def test_build_dep_data():
    collector_names = ['hardware']
    all_fact_subsets = {
        'hardware': [PlatformCollector, HardwareCollector],
    }
    dep_map = build_dep_data(collector_names, all_fact_subsets)
    assert dep_map == defaultdict(set, {
        'hardware': {
            'platform'
        }
    })
test_build_dep_data()



# Generated at 2022-06-13 00:31:15.461885
# Unit test for function find_collectors_for_platform
def test_find_collectors_for_platform():
    class Collector1(BaseFactCollector):
        _platform = 'linux'
        name = 'gather_subset_1'
    class Collector2(BaseFactCollector):
        _platform = 'linux'
        name = 'gather_subset_2'
    class Collector3(BaseFactCollector):
        _platform = 'generic'
        name = 'gather_subset_3'
    class Collector4(BaseFactCollector):
        _platform = 'windows'
        name = 'gather_subset_4'
    class Collector5(BaseFactCollector):
        _platform = 'windows'
        name = 'gather_subset_5'
    class Collector6(BaseFactCollector):
        _platform = 'darwin'
        name = 'gather_subset_6'

    import sys

# Generated at 2022-06-13 00:31:25.577575
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    # Test - normal case
    from ansible.module_utils.facts.collector import BaseFactCollector

    class CollectorA(BaseFactCollector):
        _fact_ids = set(['a', 'aa'])
        name = 'a'

    class CollectorB(BaseFactCollector):
        _fact_ids = set(['b'])
        name = 'b'

    class CollectorC(BaseFactCollector):
        _fact_ids = set(['c', 'cc'])
        name = 'c'

    class CollectorD(BaseFactCollector):
        _fact_ids = set(['d'])
        name = 'd'

    class CollectorE(BaseFactCollector):
        _fact_ids = set(['e'])
        name = 'e'


# Generated at 2022-06-13 00:31:33.915138
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    import ansible.module_utils.facts.system.distribution as distribution
    import ansible.module_utils.facts.system.platform as platform

    all_fact_subsets = {
        'distribution': [distribution],
        'distribution.family': [distribution],
        'platform': [platform]
    }


    # Case: All dependencies resolved
    collector_names = [
        'distribution'
    ]
    unresolved = find_unresolved_requires(collector_names, all_fact_subsets)
    assert not unresolved

    # Case: Unresolved dependency
    collector_names = [
        'distribution.family'
    ]
    unresolved = find_unresolved_requires(collector_names, all_fact_subsets)
    assert unresolved == set(['distribution'])
    # Case:

# Generated at 2022-06-13 00:31:44.505810
# Unit test for function get_collector_names
def test_get_collector_names():
    """
    test_get_collector_names: validate the behavior of the gathering_subset handling
    """
    # these are the valid names for the 'all' subset
    valid_subsets = frozenset(('a', 'b', 'c'))

    # these are the 'min' subset names (ie, always added even after a '!all')
    minimal_gather_subsets = frozenset(('a', 'b', 'd'))

    # these are the aliases map (ie, '!hardware' includes ['!devices', '!dmi'])
    aliases_map = defaultdict(set, {'hardware': set(('devices', 'dmi'))})

    # test equal handling with no additional parameters set

    # collect 'all' by default

# Generated at 2022-06-13 00:31:55.818474
# Unit test for function get_collector_names
def test_get_collector_names():
    # test with no args (everything implicitly added)
    names = get_collector_names()
    assert names == {'all'}

    # test with explicit 'all'
    names = get_collector_names(gather_subset=['all'])
    assert names == {'all'}

    # test with explicit 'all' and aliases_map
    names = get_collector_names(gather_subset=['all'], aliases_map=defaultdict(set, {'a': {'b'}}))
    assert names == {'all'}

    # test with explicit 'all' and aliases_map with 'all' in it

# Generated at 2022-06-13 00:32:06.121508
# Unit test for function get_collector_names
def test_get_collector_names():
    assert get_collector_names(gather_subset=['network']) == set(
        ['network'])  # basic inclusion
    assert get_collector_names(gather_subset=['network', '!all']) == set(
        ['network'])  # basic exclusion
    assert get_collector_names(gather_subset=['network',
                                              '!network']) == set(['network'])  # double exclusion

    # Note: this is a hacky way of testing for 'min' in minimal_gather_subset
    #  I couldn't think of a better way, short of creating a fake MinFactCollector
    #  that may never be used.

# Generated at 2022-06-13 00:32:16.227583
# Unit test for function tsort
def test_tsort():
    # Test a basic case
    tsort_result = tsort({'a': set(['b', 'c']), 'b': set(['c']), 'c': set()})
    assert tsort_result == [('c', set()), ('b', set(['c'])), ('a', set(['b', 'c']))]

    # Test a case with a cycle
    try:
        tsort_result = tsort({'a': set(['b']), 'b': set(['a'])})
        assert False, 'tsort should have raised CycleFoundInFactDeps with a cycle in the input, but did not'
    except CycleFoundInFactDeps:
        pass

    # Test a case where there are independent nodes that can be sorted first

# Generated at 2022-06-13 00:32:28.546737
# Unit test for function get_collector_names
def test_get_collector_names():
    assert 'disks' in get_collector_names(
        valid_subsets=('all', 'hardware', 'network', 'virtual', 'min', 'disks'),
        gather_subset=('!network', 'disks'),
        minimal_gather_subset=('min',)
    )
    assert 'network' not in get_collector_names(
        valid_subsets=('all', 'hardware', 'network', 'virtual', 'min', 'disks'),
        gather_subset=('!network', 'disks'),
        minimal_gather_subset=('min',)
    )

# Generated at 2022-06-13 00:32:37.973005
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    class FakeCollector(object):
        def __init__(self, name, required_facts):
            self.name = name
            self.required_facts = required_facts
    all_fact_subsets = {
        'a': [FakeCollector('a', set()), FakeCollector('a', set())],
        'b': [FakeCollector('b', {'a'}), FakeCollector('b', {'a'})],
        'c': [FakeCollector('c', {'d'}), FakeCollector('c', {'d'})],
        'd': [FakeCollector('d', {'b'}), FakeCollector('d', {'b'})],
    }
    assert find_unresolved_requires(['a', 'b'], all_fact_subsets) == set()

# Generated at 2022-06-13 00:32:46.457385
# Unit test for function build_dep_data
def test_build_dep_data():
    # mock collector
    class Collector1(BaseFactCollector):
        name = 'collector1'
        required_facts = ['collector2']
    class Collector2(BaseFactCollector):
        name = 'collector2'
        required_facts = ['collector3']
    collectors = [
        Collector1,
        Collector2
    ]
    all_fact_subsets = {}
    for collector in collectors:
        all_fact_subsets[collector.name] = [collector]
    collector_names = ['collector1', 'collector2']
    results = build_dep_data(collector_names, all_fact_subsets)
    assert results['collector1'] == {'collector2'}
    assert results['collector2'] == {'collector3'}



# Generated at 2022-06-13 00:32:59.414629
# Unit test for function get_collector_names
def test_get_collector_names():
    '''Verify that get_collector_names() returns expected results'''

    # Tests for get_collector_names()

    # Arrange
    valid_subsets = frozenset(('network', 'hardware', 'virtual'))
    minimal_gather_subset = frozenset(('network', 'hardware'))
    aliases = defaultdict(set, hardware=('devices', 'dmi'))

# Generated at 2022-06-13 00:33:10.004910
# Unit test for function find_collectors_for_platform
def test_find_collectors_for_platform():

    class Coll_1(BaseFactCollector):
        _platform = 'Linux'
        name = 'coll_1'

    class Coll_2(BaseFactCollector):
        _platform = 'Linux'
        name = 'coll_2'

    class Coll_3(BaseFactCollector):
        _platform = 'Generic'
        name = 'coll_3'

    class Coll_4(BaseFactCollector):
        _platform = 'Darwin'
        name = 'coll_4'

    class Coll_5(BaseFactCollector):
        _platform = 'Windows'
        name = 'coll_5'

    # Test matching on specific platform
    compat_platforms = [
        {'system': 'Linux'},
        {'system': 'Darwin'},
    ]

# Generated at 2022-06-13 00:33:14.875998
# Unit test for function build_dep_data
def test_build_dep_data():
    collector_names = ['a', 'b', 'c']
    all_fact_subsets = {
        'a': [object()],
        'b': [object(), object()],
        'c': [object()],
    }
    dep_data = build_dep_data(collector_names, all_fact_subsets)
    expected = {
        'a': set(),
        'b': set(),
        'c': set(),
    }
    assert dep_data == expected


# Generated at 2022-06-13 00:33:19.983865
# Unit test for function select_collector_classes
def test_select_collector_classes():
    import unittest

    class TestCollector1(BaseFactCollector):
        name = 'test_collector1'
        _fact_ids = set()

    class TestCollector2(BaseFactCollector):
        name = 'test_collector2'
        _fact_ids = set()

    class TestCollector3(BaseFactCollector):
        name = 'test_collector3'
        _fact_ids = ('test_id1', 'test_id2')


# Generated at 2022-06-13 00:33:31.066108
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    class TestCollectorA(BaseFactCollector):
        name = 'test_collector_a'

        _fact_ids = set(['network'])

    class TestCollectorB(BaseFactCollector):
        name = 'test_collector_b'

        _fact_ids = set(['network'])

    class TestCollectorC(BaseFactCollector):
        name = 'test_collector_c'

        _fact_ids = set(['test_collector_c_id'])

    fact_id_to_collector_map, aliases_map = build_fact_id_to_collector_map(
        [TestCollectorA, TestCollectorB, TestCollectorC])

    assert 'test_collector_a' in fact_id_to_collector_map

# Generated at 2022-06-13 00:33:42.167055
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    test_collector_class = type('test_collector_class', (BaseFactCollector, ), {})
    test_collector_class._fact_ids = {'1', '2'}
    test_collector_class.name = '3'
    test_collector_class.required_facts = set()
    test_collector_class.platform_match = lambda x: True
    test_collector_class.collect = lambda: {}

    assert build_fact_id_to_collector_map({test_collector_class}) == ({
        '1': [test_collector_class],
        '2': [test_collector_class],
        '3': [test_collector_class],
    }, {
        '3': {'1', '2'},
    })
# end of test_build_

# Generated at 2022-06-13 00:33:49.561377
# Unit test for function find_collectors_for_platform
def test_find_collectors_for_platform():
    import os
    import sys
    import tempfile

    sys.path.insert(0, os.path.dirname(__file__))
    test_collector_file = tempfile.NamedTemporaryFile(mode='w+',
                                                      suffix='.py',
                                                      prefix='test_',
                                                      delete=False)


# Generated at 2022-06-13 00:34:02.023385
# Unit test for function find_collectors_for_platform
def test_find_collectors_for_platform():

    class TestCollector(BaseFactCollector):
        _fact_ids = set()
        _platform = 'Generic'
        required_facts = set()
        def platform_match(cls, platform_info):
            if platform_info['system'] == cls._platform:
                return cls
            return None

    TestCollector.name = 'test_collector'
    TestCollector.required_facts = set()
    found_collectors = find_collectors_for_platform([TestCollector], [{'system': 'Generic'}])
    assert found_collectors == set([TestCollector])



# Generated at 2022-06-13 00:34:09.003632
# Unit test for function find_collectors_for_platform
def test_find_collectors_for_platform():
    class CollectorA(BaseFactCollector):
        _fact_ids = {'A'}
        _platform = 'PlatformA'
        name = 'CollectorA'


    class CollectorB(BaseFactCollector):
        _fact_ids = {'B'}
        _platform = 'PlatformB'
        name = 'CollectorB'


    all_collector_classes = [CollectorA, CollectorB]
    compat_platforms = [{'system': 'PlatformA'}, {'system': 'PlatformB'}]

    found_collectors = find_collectors_for_platform(all_collector_classes, compat_platforms)

    assert found_collectors == {CollectorA, CollectorB}

