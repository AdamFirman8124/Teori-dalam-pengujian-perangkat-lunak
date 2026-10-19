

# Generated at 2022-06-13 00:24:47.811796
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    collector_names = ['A', 'B', 'C', 'D']
    all_fact_subsets = {}
    for collector_name in collector_names:
        all_fact_subsets[collector_name] = [type(collector_name, (BaseFactCollector,), {})]()
    all_fact_subsets['B'].required_facts = frozenset(['A', 'C'])
    all_fact_subsets['D'].required_facts = frozenset(['B'])

    unresolved = set(find_unresolved_requires(collector_names, all_fact_subsets))

    assert not unresolved



# Generated at 2022-06-13 00:24:56.997206
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    collector_names = ['basic']
    all_fact_subsets = {
        'basic': set([BasicFactCollector]),
    }
    assert find_unresolved_requires(collector_names, all_fact_subsets) == set()

    collector_names = ['basic', 'hardware']
    all_fact_subsets = {
        'basic': set([BasicFactCollector]),
        'hardware': set([HardwareFactCollector]),
    }
    assert find_unresolved_requires(collector_names, all_fact_subsets) == set()

    collector_names = ['basic', 'hardware']
    all_fact_subsets = {
        'basic': set([BasicFactCollector]),
        'hardware': set([HardwareFactCollector]),
    }

# Generated at 2022-06-13 00:25:07.671891
# Unit test for function build_dep_data
def test_build_dep_data():
    collector_names = ['test_collector_a', 'test_collector_b', 'test_collector_c']
    collected_facts_a = CollectedFacts(
        collect=lambda module=None, collected_facts=None: {'a': 1},
        required_facts=set(),
        name='test_collector_a')
    collected_facts_b = CollectedFacts(
        collect=lambda module=None, collected_facts=None: {'b': 1},
        required_facts=set(['test_collector_a']),
        name='test_collector_b')

# Generated at 2022-06-13 00:25:18.469240
# Unit test for function find_collectors_for_platform
def test_find_collectors_for_platform():
    class MockCollector1:
        name = "test_collector"

    class MockCollector2:
        name = "other_test_collector"

        @classmethod
        def platform_match(cls, platform_info):
            if platform_info.get('system', None) == cls.name:
                return cls

    # 'system' will be matched
    platform_info = {'system': 'test_collector'}

    all_collector_classes = [MockCollector1, MockCollector2]
    collectors = find_collectors_for_platform(all_collector_classes, [platform_info])
    assert len(collectors) == 1
    assert collectors.pop().name == 'test_collector'



# Generated at 2022-06-13 00:25:28.872992
# Unit test for function build_dep_data
def test_build_dep_data():
    # Initialize test data
    collector_name1 = 'collector1'
    collector_name2 = 'collector2'
    collector_name3 = 'collector3'
    collector_name4 = 'collector4'
    collector_names = set([collector_name1, collector_name2, collector_name3, collector_name4])
    all_fact_subsets = {collector_name1: set(['collector1_dep1', 'collector1_dep2']),
                        collector_name2: set(['collector2_dep1', 'collector2_dep2']),
                        collector_name3: set(['collector3_dep1', 'collector3_dep2']),
                        collector_name4: set(['collector4_dep1', 'collector4_dep2'])}
   

# Generated at 2022-06-13 00:25:37.103279
# Unit test for function build_dep_data
def test_build_dep_data():
    import pytest
    from ansible_collections.notstdlib.moveitallout.plugins.module_utils.facts.collectors import network
    collector_names = ['network', 'uname']
    all_fact_subsets = {'network': [network.Network]}
    dep_map = build_dep_data(collector_names, all_fact_subsets)
    expected = defaultdict(set)
    expected['network'] = {'uname'}
    expected['uname'] = set()
    assert dep_map == expected



# Generated at 2022-06-13 00:25:46.223347
# Unit test for function find_collectors_for_platform
def test_find_collectors_for_platform():
    '''Unit test for function find_collectors_for_platform'''

    import sys
    import platform
    import unittest

    class metaclass_as_decorator(type):
        '''Metaclass that pretends to be a decorator (with arguments)'''
        def __init__(cls, name, bases, attrs):
            if '_platform' not in attrs:
                raised = True
                # call like a decorator
                return lambda cls: cls
            else:
                # call like a real metaclass and do the normal thing
                type.__init__(cls, name, bases, attrs)

        def __call__(cls, *args, **kwargs):
            if cls._platform:
                return type.__call__(cls, *args, **kwargs)

# Generated at 2022-06-13 00:25:58.312182
# Unit test for function get_collector_names
def test_get_collector_names():
    # first, test with a simple gather_subset
    gather_subset = ['hardware']
    valid_subsets = frozenset(('all', 'hardware', 'min'))
    minimal_gather_subset = frozenset(('min',))
    aliases_map = defaultdict(set, **{'!hardware': frozenset(('hardware',))})
    assert get_collector_names(valid_subsets=valid_subsets,
                               minimal_gather_subset=minimal_gather_subset,
                               gather_subset=gather_subset,
                               aliases_map=aliases_map) == frozenset(('hardware', 'min'))

    # now, test with a more complicated gather_subset

# Generated at 2022-06-13 00:26:08.593270
# Unit test for function get_collector_names

# Generated at 2022-06-13 00:26:19.683361
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    class Collector1(BaseFactCollector):
        name = 'collector1'

    class Collector2(BaseFactCollector):
        name = 'collector2'
        _fact_ids = {'collector2'}

    class Collector3(BaseFactCollector):
        name = 'collector3'
        _fact_ids = {'collector3', 'collector2'}

    class Collector4(BaseFactCollector):
        name = 'collector4'
        _fact_ids = {'collector4', 'collector3', 'collector2'}

    class Collector5(BaseFactCollector):
        name = 'collector5'
        _fact_ids = {'collector5', 'collector4'}

    class Collector6(BaseFactCollector):
        name = 'collector6'
        _fact

# Generated at 2022-06-13 00:26:34.362487
# Unit test for function build_dep_data
def test_build_dep_data():
    import os
    import sys
    import unittest
    import tempfile
    from ansible.module_utils.facts import collector, platform

    # Create a file for temporary testing
    tmpfile = tempfile.NamedTemporaryFile()

# Generated at 2022-06-13 00:26:44.878554
# Unit test for function find_collectors_for_platform
def test_find_collectors_for_platform():
    from ansible.module_utils.facts.collectors import network
    from ansible.module_utils.facts.collectors.base import CollectorNotFoundError

    all_collector_classes = [network.NetworkCollector]

    # moving the sysname check for linux to the first check
    compat_platforms = [{'system': 'Linux'}, {'system': 'FreeBSD'}]
    found_collectors = find_collectors_for_platform(all_collector_classes, compat_platforms)
    assert network.NetworkCollector in found_collectors

    # platform not found
    compat_platforms = [{'system': 'Darwin'}]
    found_collectors = find_collectors_for_platform(all_collector_classes, compat_platforms)
    assert len(found_collectors) == 0




# Generated at 2022-06-13 00:26:54.167900
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    class CollectA(BaseFactCollector):
        _fact_ids = frozenset(['a', 'b'])
    class CollectB(BaseFactCollector):
        _fact_ids = frozenset(['b', 'c'])
        name = 'c'
    class CollectC(BaseFactCollector):
        _fact_ids = frozenset(['a', 'c', 'd'])
        name = 'a'

    collectors = [CollectA, CollectB, CollectC]

    expected_fact_id_map = {
        'a': [CollectA, CollectC],
        'b': [CollectA, CollectB],
        'c': [CollectB, CollectC],
        'd': [CollectC],

    }


# Generated at 2022-06-13 00:27:06.008567
# Unit test for function find_collectors_for_platform
def test_find_collectors_for_platform():
    import sys
    import os
    sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'facts'))
    from facts.facts import AllFactCollectors

    # Testing for the 'os_family' field in the platform
    class FakeCollector:
        _fact_ids = set()
        _platform = 'FakeOS'
        name = 'fake'
        required_facts = set()

        def __init__(self, collectors=None, namespace=None):
            '''Base class for things that collect facts.

            'collectors' is an optional list of other FactCollectors for composing.'''
            self.collectors = collectors or []

            # self.namespace is a object with a 'transform' method that transforms
            # the name to indicate the namespace (ie, adds a prefix or suffix).

# Generated at 2022-06-13 00:27:14.165670
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    import copy
    import ansible_collections.ansible.community.plugins.module_utils.facts.collector.base as base_collector
    import ansible_collections.ansible.community.plugins.module_utils.facts.collector.network as network_collector
    import ansible_collections.ansible.community.plugins.module_utils.facts.collector.other as other_collector
    import ansible_collections.ansible.community.plugins.module_utils.facts.collector.platform as platform_collector
    import ansible_collections.ansible.community.plugins.module_utils.facts.collector.deb as deb_collector
    import ansible_collections.ansible.community.plugins.module_utils.facts.collector.pulp as pulp_collector


# Generated at 2022-06-13 00:27:25.473073
# Unit test for function get_collector_names
def test_get_collector_names():
    imports = [
        {'alias': 'hardware', 'fact_ids': ['cpu', 'mem']},
        {'alias': 'devices', 'fact_ids': ['devices']},
        {'alias': 'all', 'fact_ids': ['hardware', 'devices', 'network']},
        {'alias': 'network', 'fact_ids': ['interfaces', 'default_ipv4', 'default_ipv6']},
    ]
    # map of alias to list of fact names for that alias
    aliases_map = defaultdict(set)
    for alias_dict in imports:
        aliases_map[alias_dict['alias']] = set(alias_dict['fact_ids'])

    aliases_map['all'].update(set(chain(*aliases_map.values())))
    valid_subsets = aliases_map.keys

# Generated at 2022-06-13 00:27:33.488387
# Unit test for function get_collector_names
def test_get_collector_names():
    minimal_gather_subset = frozenset(['network'])
    aliases_map = defaultdict(set)
    aliases_map['hardware'].update(['devices', 'dmi'])

    def test(gather_subset, expect_valid_subsets):
        valid_subsets = get_collector_names(gather_subset=gather_subset,
                                            valid_subsets=frozenset(['all', 'hardware', 'network', 'ohai', 'facter', 'virtualization']),
                                            minimal_gather_subset=minimal_gather_subset,
                                            aliases_map=aliases_map)
        assert valid_subsets == expect_valid_subsets

    # test gather_subset = 'all'

# Generated at 2022-06-13 00:27:46.639533
# Unit test for function find_collectors_for_platform
def test_find_collectors_for_platform():
    class TestCollector(BaseFactCollector):
        _fact_ids = set()
        _platform = 'Darwin'
        name = 'test'
        required_facts = set()

        def collect(self, module=None, collected_facts=None):
            return {}

    class TestCollector2(BaseFactCollector):
        _fact_ids = set()
        _platform = 'Generic'
        name = 'test2'
        required_facts = set()

        def collect(self, module=None, collected_facts=None):
            return {}

    class TestCollector3(BaseFactCollector):
        _fact_ids = set()
        _platform = 'Generic'
        name = 'test3'
        required_facts = set()

        def collect(self, module=None, collected_facts=None):
            return {}

# Generated at 2022-06-13 00:27:50.595721
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    class TestCollector1(BaseFactCollector):
        name = 'test1'
        _fact_ids = set(['fact1'])

    class TestCollector2(BaseFactCollector):
        name = 'test2'
        _fact_ids = set(['fact1', 'test2'])

    class TestCollector3(BaseFactCollector):
        name = 'test3'
        _fact_ids = set(['fact3'])

    test_dict = build_fact_id_to_collector_map(
        {TestCollector1, TestCollector2, TestCollector3})


# Generated at 2022-06-13 00:27:57.793355
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():

    from ansible.module_utils.facts import collectors

    fact_id_to_collector_map, aliases_map =  build_fact_id_to_collector_map(collectors_for_platform=collectors)

    # Basic tests for a few known issues
    assert fact_id_to_collector_map['all_ipv4_addresses'] == [collectors.collectors_map['NetworkingFactCollector']]
    assert fact_id_to_collector_map['all_ipv6_addresses'] == [collectors.collectors_map['NetworkingFactCollector']]
    assert aliases_map['NetworkingFactCollector'] == set(collectors.collectors_map['NetworkingFactCollector']._fact_ids)



# Generated at 2022-06-13 00:28:14.638344
# Unit test for function find_collectors_for_platform
def test_find_collectors_for_platform():
    class FakeCollector:
        def __init__(self, name):
            self.name = name

        @classmethod
        def platform_match(cls, platform_info):
            if platform_info.get('system', None) == 'Linux':
                return cls
            return None

    class FakeCollectorLinux:
        name = 'linux'
        _platform = 'Linux'

        @classmethod
        def platform_match(cls, platform_info):
            if platform_info.get('system', None) == cls._platform:
                return cls
            return None

    class FakeCollectorLinuxX86:
        name = 'linuxx86'
        _platform = 'Linux'
        _platform_version = (2, 6)


# Generated at 2022-06-13 00:28:24.936441
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    class CollectorA(BaseFactCollector):
        name = 'a'
    class CollectorB(BaseFactCollector):
        name = 'b'
    class CollectorC(BaseFactCollector):
        name = 'c'
        _fact_ids = set(['c_alias'])

    collectors_for_platform = {CollectorA, CollectorB, CollectorC}
    expected_fact_id_to_collector_map = {
        'a': [CollectorA],
        'b': [CollectorB],
        'c': [CollectorC],
        'c_alias': [CollectorC],
    }
    expected_aliases_map = {
        'a': set(),
        'b': set(),
        'c': {'c_alias'},
    }

    fact_id_to_collector_map

# Generated at 2022-06-13 00:28:36.887257
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    class Collector1(BaseFactCollector):
        _fact_ids = set(['c1_fact1', 'c1_fact2'])
        name = 'c1'

    class Collector2(BaseFactCollector):
        _fact_ids = ['c2_fact1', 'c2_fact2']
        name = 'c2'

    class Collector3(BaseFactCollector):
        _fact_ids = ['c3_fact1', 'c3_fact2']
        name = 'c3'

    collectors_for_platform = [Collector1, Collector2, Collector3]

    fact_id_to_collector_map, aliases_map = build_fact_id_to_collector_map(collectors_for_platform)


# Generated at 2022-06-13 00:28:46.814346
# Unit test for function find_collectors_for_platform
def test_find_collectors_for_platform():
    class Collector1(BaseFactCollector):
        _platform = 'Foo'
        name = 'collector1'
        required_facts = set()

    class Collector2(BaseFactCollector):
        _platform = 'Foo'
        name = 'collector2'
        required_facts = set()

    class Collector3(BaseFactCollector):
        _platform = 'Bar'
        name = 'collector3'
        required_facts = set()

    all_collector_classes = [Collector1, Collector2, Collector3]
    compat_platforms = [{'system': 'Foo'}]

    found_collectors = find_collectors_for_platform(all_collector_classes, compat_platforms)
    assert len(found_collectors) == 2


# Generated at 2022-06-13 00:28:56.950391
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    # If we have one collector with the name 'key1', and we have one
    # collector with the name 'key2', and they both have the _fact_ids
    # of 'key3', 'key4' and 'key5', we should be able to retrieve either
    # collector by any of the 5 keys.

    class FakeCollector1(BaseFactCollector):
        pass

    class FakeCollector2(BaseFactCollector):
        pass

    FakeCollector1.name = 'key1'
    FakeCollector1._fact_ids = set(['key3', 'key4', 'key5'])

    FakeCollector2.name = 'key2'
    FakeCollector2._fact_ids = set(['key3', 'key4', 'key5'])


# Generated at 2022-06-13 00:29:06.369004
# Unit test for function find_collectors_for_platform
def test_find_collectors_for_platform():
    class fake_collector:
        _fact_ids = set()

        _platform = None
        name = None
        required_facts = set()

        @classmethod
        def platform_match(cls, platform_info):
            if platform_info.get('system', None) == cls._platform:
                return cls
            return None

    class collector_A(fake_collector):
        _platform = 'A'
        name = 'A'
        required_facts = set()

    class collector_B(fake_collector):
        _platform = 'B'
        name = 'B'
        required_facts = set()

    class collector_C(fake_collector):
        _platform = 'C'
        name = 'C'
        required_facts = set()


# Generated at 2022-06-13 00:29:15.451221
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    from ansible.module_utils.facts import collector

    class CollectorA(BaseFactCollector):
        name = 'A'
        required_facts = frozenset(['B'])

    class CollectorB(BaseFactCollector):
        name = 'B'

    class CollectorC(BaseFactCollector):
        name = 'C'
        required_facts = frozenset(['B', 'D'])

    class CollectorD(BaseFactCollector):
        name = 'D'

    assert frozenset(find_unresolved_requires(['A'], collector.all_fact_subsets)) == frozenset('A')
    assert not find_unresolved_requires(['B'], collector.all_fact_subsets)

# Generated at 2022-06-13 00:29:25.810362
# Unit test for function build_dep_data
def test_build_dep_data():
    # given
    collector_names = ['a', 'b']
    def collect(collected_facts=None):
        return {}

    class C:
        name = 'a'
        required_facts = set()
    class D:
        name = 'b'
        required_facts = {'c'}

    all_fact_subsets = {
        'a': [C],
        'b': [D]
    }

    # when
    dep_map = build_dep_data(collector_names, all_fact_subsets)

    # then
    assert dep_map == {
        'a': set(),
        'b': {'c'}
    }



# Generated at 2022-06-13 00:29:33.218994
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    class FakeCollector:
        name = 'fake_collector'
        required_facts = set(['one', 'two'])
    all_fact_subsets = defaultdict(list)
    all_fact_subsets['fake_collector'].append(FakeCollector)

    assert find_unresolved_requires(['fake_collector'], all_fact_subsets) == set(['one', 'two'])
    assert find_unresolved_requires(['one'], all_fact_subsets) == set(['one'])



# Generated at 2022-06-13 00:29:43.537358
# Unit test for function find_collectors_for_platform
def test_find_collectors_for_platform():
    import ansible.module_utils.facts.collector.linux as linux
    import ansible.module_utils.facts.collector.windows as windows

    all_collectors = []
    all_collectors.extend(list(linux.collectors))
    all_collectors.extend(list(windows.collectors))

    linux_platform = {
        'system': 'Linux',
        'distribution': 'Debian'
    }
    compat_linux = [
        linux_platform,
        {'system': 'Linux'}
    ]

    filtered_collectors = find_collectors_for_platform(all_collectors, compat_linux)

    assert len(filtered_collectors) == 2
    assert linux.LinuxDistribution.name in (c.name for c in filtered_collectors)
    assert linux.GenericLinux

# Generated at 2022-06-13 00:29:59.564404
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    all_fact_subsets = defaultdict(list)
    all_fact_subsets['foo'] = []
    all_fact_subsets['bar'] = [object()]
    all_fact_subsets['baz'] = [object()]

    obj = object()
    obj.required_facts = set(['bar'])
    all_fact_subsets['buzz'] = [obj]

    unresolved = find_unresolved_requires(set(['foo']), all_fact_subsets)
    assert unresolved == set()

    unresolved = find_unresolved_requires(set(['foo', 'bar']), all_fact_subsets)
    assert unresolved == set()

    unresolved = find_unresolved_requires(set(['foo', 'buzz']), all_fact_subsets)

# Generated at 2022-06-13 00:30:11.716591
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    class BananaFactCollector(BaseFactCollector):
        _fact_ids = ('banana',)
        name = 'banana'

    class OrangeFactCollector(BaseFactCollector):
        _fact_ids = ('orange',)
        name = 'orange'

    class BananaOrangeFactCollector(BaseFactCollector):
        _fact_ids = ('bananaorange',)
        name = 'bananaorange'

    class AppleFactCollector(BaseFactCollector):
        _fact_ids = ('apple',)
        name = 'apple'

    class AppleOrangeFactCollector(BaseFactCollector):
        _fact_ids = ('appleorange', 'orangeapple',)
        name = 'appleorange'


# Generated at 2022-06-13 00:30:23.328755
# Unit test for function get_collector_names
def test_get_collector_names():
    # Test getting collector names when everything is specified in the gather subset
    assert get_collector_names(valid_subsets=('hardware', 'network'), gather_subset=('hardware', 'network')) == frozenset(('hardware', 'network'))
    # Test getting collector names when gather subset is 'all'
    assert get_collector_names(valid_subsets=('hardware', 'network'), gather_subset=('all',)) == frozenset(('hardware', 'network'))
    # Test getting collector names when the gather subset contains an alias
    aliases_map = defaultdict(set)
    aliases_map['hardware'].add('network')

# Generated at 2022-06-13 00:30:28.673168
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    from ansible.module_utils.facts.collector import python_version_collector
    all_fact_subsets = {
        'python_version': [python_version_collector],
    }
    assert find_unresolved_requires(['python_version'], all_fact_subsets) == set()



# Generated at 2022-06-13 00:30:37.116515
# Unit test for function get_collector_names
def test_get_collector_names():
    assert get_collector_names(['a', 'b', 'c'], gather_subset=['a', 'b']) == {'a', 'b'}
    assert get_collector_names(['a', 'b', 'c'], gather_subset=['a', 'b', '!a']) == {'b'}
    assert get_collector_names(['a', 'b', 'c'], gather_subset=['!a']) == {'b', 'c'}
    assert get_collector_names(['a', 'b', 'c'], gather_subset=['a', '!a']) == {'a'}


# Generated at 2022-06-13 00:30:45.821287
# Unit test for function build_dep_data
def test_build_dep_data():
    collector_names = ['foo', 'bar', 'bleep', 'bloop']
    all_fact_subsets = {'foo': [A, B1], 'bar': [B2], 'bleep': [C], 'bloop': [D]}
    dep_map = build_dep_data(collector_names, all_fact_subsets)
    assert dep_map == {'foo': set(), 'bar': set(), 'bleep': set(['foo', 'bar']), 'bloop': set(['bleep'])}

test_build_dep_data()



# Generated at 2022-06-13 00:30:55.883396
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    # Setup
    class Collector(object):
        _fact_ids = ['a', 'b', 'c']
        name = 'd'
    collector_classes = [Collector]

    # Execute
    map_to_test, aliases_map = build_fact_id_to_collector_map(collector_classes)

    # Assert
    assert len(aliases_map) == 1
    assert len(aliases_map['d']) == 3
    for key in aliases_map['d']:
        assert key in ['a', 'b', 'c']

    assert len(map_to_test) == 4
    for key in map_to_test:
        assert key in ['a', 'b', 'c', 'd']
        assert len(map_to_test[key]) == 1



# Generated at 2022-06-13 00:31:07.359015
# Unit test for function get_collector_names
def test_get_collector_names():
    VALID_SUBSETS = frozenset(['a', 'b', 'c'])


# Generated at 2022-06-13 00:31:15.310642
# Unit test for function find_collectors_for_platform
def test_find_collectors_for_platform():
    import sys

    class TestCollector1(BaseFactCollector):
        name = 'test_collector_1'
        _platform = 'test_platform'

        def collect(self):
            return {'test': 1}

    class TestCollector2(BaseFactCollector):
        name = 'test_collector_2'

        def collect(self):
            return {'test': 2}

    class TestCollector3(BaseFactCollector):
        name = 'test_collector_3'
        _platform = 'test_platform_2'

        def collect(self):
            return {'test': 3}

    if sys.version_info >= (3, 0):
        from unittest.mock import MagicMock
    else:
        from mock import MagicMock


# Generated at 2022-06-13 00:31:25.445375
# Unit test for function build_dep_data
def test_build_dep_data():
    class TestCollectorA(BaseFactCollector):
        _fact_ids = {'a_facts'}
        name = 'a'
        required_facts = {'b'}

    class TestCollectorB(BaseFactCollector):
        _fact_ids = {'b_facts'}
        name = 'b'
        required_facts = {'c'}

    class TestCollectorC(BaseFactCollector):
        _fact_ids = {'c_facts'}
        name = 'c'
        required_facts = {}

    collectors = [TestCollectorA, TestCollectorB, TestCollectorC]
    collector_classes = find_collectors_for_platform(collectors, [{'system': platform.system()}])
    fact_id_to_collector_map, aliases_map = build_fact

# Generated at 2022-06-13 00:31:46.157171
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    from ansible.module_utils.facts import collector

    # Python3 mock doesn't have MagicMock.assert_not_called, so we mock _load_collectors
    # to return a specific set of objects, and then see if they are called in the correct
    # order.
    # NOTE: we also fire up the collector with gather_subset=all, so we can see that they
    #       are all called

    class Test(BaseFactCollector):
        name = 'test'
        required_facts = set()

        def collect(self, module=None, collected_facts=None):
            return {'test': 'data'}

    class Test2(BaseFactCollector):
        name = 'test2'
        _fact_ids = set(['test2_alias'])
        required_facts = set()


# Generated at 2022-06-13 00:31:56.942971
# Unit test for function build_dep_data
def test_build_dep_data():
    all_fact_subsets = {}
    all_fact_subsets['test1'] = [TestCollector1(), TestCollector2()]
    all_fact_subsets['test2'] = [TestCollector3()]
    all_fact_subsets['test3'] = [TestCollector3()]
    all_fact_subsets['test4'] = [TestCollector4()]
    all_fact_subsets['test5'] = [TestCollector5()]
    all_fact_subsets['test6'] = [TestCollector6()]

    collector_names = ['test1', 'test2', 'test3', 'test4', 'test5', 'test6']
    dep_map = build_dep_data(collector_names, all_fact_subsets)

# Generated at 2022-06-13 00:32:07.088518
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    from ansible.module_utils.facts.collector import setup_collector_classes
    from ansible.module_utils.facts.collector.hardware.cpu import CPUCollector
    from ansible.module_utils.facts.collector.hardware.system import SystemCollector
    from ansible.module_utils.facts import timeout

    all_collector_classes = setup_collector_classes()

    # Test cases

# Generated at 2022-06-13 00:32:15.003200
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    # NOTE: we can't use the real 'Network' class here because the class-level attributes are
    # replaced by the decorator and we can't just mock the decorator, so we make a fake class
    class FakeNetwork(BaseFactCollector):
        name = 'network'
        _fact_ids = {'interfaces', 'all_ipv4_addresses', 'default_ipv4', 'all_ipv6_addresses',
                     'default_ipv6'}
    assert build_fact_id_to_collector_map([FakeNetwork])[0]['network'] == [FakeNetwork]
    assert build_fact_id_to_collector_map([FakeNetwork])[0]['interfaces'] == [FakeNetwork]



# Generated at 2022-06-13 00:32:24.662379
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    class FakeCollectorWithAliases(BaseFactCollector):
        _platform = 'Linux'
        _fact_ids = set(['foo', 'bar'])
        name = 'fake-collector'
        required_facts = frozenset(('foo', ))

    class FakeCollector(BaseFactCollector):
        _platform = 'Linux'
        name = 'fake-collector-2'
        required_facts = frozenset(('foo', ))

    collector_mapping, aliases_map = build_fact_id_to_collector_map([FakeCollector, FakeCollectorWithAliases])
    assert collector_mapping['fake-collector'] == [FakeCollectorWithAliases]
    assert collector_mapping['fake-collector-2'] == [FakeCollector]

# Generated at 2022-06-13 00:32:35.232077
# Unit test for function find_collectors_for_platform
def test_find_collectors_for_platform():
    from ansible.module_utils.facts.namespace import BaseFactNamespace
    from ansible.module_utils.facts.collector import BaseFactCollector
    class TestCollector(BaseFactCollector):
        _platform = 'FreeBSD'
        name = 'test'
    class TestCollector2(BaseFactCollector):
        _platform = 'FreeBSD'
        name = 'test2'
    class TestCollector3(BaseFactCollector):
        _platform = 'Darwin'
        name = 'test3'
    class TestCollector4(BaseFactCollector):
        _platform = 'Linux'
        name = 'test4'
    class TestCollector5(BaseFactCollector):
        _platform = 'Generic'
        name = 'test5'

# Generated at 2022-06-13 00:32:44.571861
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    class Collector(BaseFactCollector):
        _fact_ids = frozenset(['id1', 'id2', 'id3'])
        name = 'name'

    class CollectorNoAliases(BaseFactCollector):
        _fact_ids = frozenset()
        name = 'name'

    class CollectorNoName(BaseFactCollector):
        _fact_ids = frozenset(['id1', 'id2', 'id3'])
        name = None

    class CollectorNoIds(BaseFactCollector):
        _fact_ids = frozenset()
        name = 'name'

    mapped, aliases = build_fact_id_to_collector_map(set([Collector, CollectorNoAliases, CollectorNoName, CollectorNoIds]))
    assert Collector in mapped['id1']

# Generated at 2022-06-13 00:32:51.969904
# Unit test for function get_collector_names
def test_get_collector_names():
    import pytest

    valid_subsets = frozenset(['all', 'network', 'baremetal', 'firmware', 'hardware', 'virtual'])
    minimal_gather_subset = frozenset()
    aliases_map = defaultdict(set)
    aliases_map['hardware'].update(['devices', 'dmi', 'firmware'])
    aliases_map['virtual'].update(['libvirt', 'ovirt', 'virtualization'])

    # test all
    gather_subset = ['all']

# Generated at 2022-06-13 00:32:52.649118
# Unit test for function find_collectors_for_platform
def test_find_collectors_for_platform():
    pass



# Generated at 2022-06-13 00:33:02.603044
# Unit test for function find_collectors_for_platform
def test_find_collectors_for_platform():
    class Collectors(BaseFactCollector):
        name = 'test'
        _platform = 'Linux'

    class Collectors2(BaseFactCollector):
        name = 'test2'
        _platform = 'Linux'

    class Collectors3(BaseFactCollector):
        name = 'test3'
        _platform = 'Darwin'

    class Collectors4(BaseFactCollector):
        name = 'test4'
        _platform = 'Generic'

    assert set(find_collectors_for_platform([Collectors], [{'system': 'Linux'}, {'system': 'Generic'}])) == \
        set([Collectors])
