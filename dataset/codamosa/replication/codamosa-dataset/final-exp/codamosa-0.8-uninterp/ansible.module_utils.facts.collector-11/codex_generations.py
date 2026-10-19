

# Generated at 2022-06-13 00:24:42.042940
# Unit test for function get_collector_names
def test_get_collector_names():
    valid_subsets = frozenset(['foo', 'bar', 'baz'])
    minimal_gather_subset = frozenset(['a', 'b'])
    aliases_map = defaultdict(set)
    aliases_map['a'].update(['c', 'd'])


# Generated at 2022-06-13 00:24:54.901524
# Unit test for function select_collector_classes
def test_select_collector_classes():
    from ansible.module_utils.facts.collector.all import AllCollector
    from ansible.module_utils.facts.collector.network import NetworkCollector
    from ansible.module_utils.facts.collector.dmi import DmiCollector

    all_fact_subsets = {
        'all': [
            AllCollector,
            AllCollector
        ],
        'network': [
            NetworkCollector,
            NetworkCollector
        ],
        'dmi': [
            DmiCollector
        ]
    }

    assert [AllCollector] == select_collector_classes(['all'], all_fact_subsets)
    assert [AllCollector, AllCollector] == select_collector_classes(['all', 'all'], all_fact_subsets)

# Generated at 2022-06-13 00:25:01.167250
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    def mock_get_requires_by_collector_name(collector_name):
        '''Just return all requires'''
        return _get_requires_by_collector_name(collector_name, all_fact_subsets)

    # Setup mock data
    all_fact_subsets = {
        'foo': [object()],
        'bar': [object()],
        'baz': [object()],
        'qux': [object()],
    }

    # Correct use case
    assert not find_unresolved_requires(['foo', 'qux'], all_fact_subsets)

    # Missing required facts
    assert find_unresolved_requires(['foo', 'bar'], all_fact_subsets) == {'baz'}

# Generated at 2022-06-13 00:25:10.110774
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    from ansible.module_utils.facts.collectors.base import BaseFactCollector

    class TestCollector(BaseFactCollector):
        name = 'test'
        _fact_ids = ('test1', 'test2')

    class TestCollector2(BaseFactCollector):
        name = 'test'
        _fact_ids = ('test1', 'test2')

    fact_id_to_collector_map, aliases_map = build_fact_id_to_collector_map([TestCollector, TestCollector2])

    assert fact_id_to_collector_map['test'][0] == TestCollector
    assert fact_id_to_collector_map['test1'][0] == TestCollector
    assert fact_id_to_collector_map['test1'][1] == TestCollector

# Generated at 2022-06-13 00:25:20.321427
# Unit test for function get_collector_names
def test_get_collector_names():
    valid_subsets = frozenset(['devices', 'disk_info', 'dmi', 'network', 'pkg_mgr', 'ohai'])
    minimal_gather_subset = frozenset(['dmi'])
    aliases_map_default = defaultdict(set)

    # empty gather_subset, check default (minimal_gather_subset)
    gather_subset = []
    assert set(get_collector_names(valid_subsets=valid_subsets, minimal_gather_subset=minimal_gather_subset,
                                   gather_subset=gather_subset, aliases_map=aliases_map_default)) == minimal_gather_subset

    # empty gather_subset, check default (valid_subsets)
    gather_subset = []

# Generated at 2022-06-13 00:25:27.513599
# Unit test for function build_dep_data
def test_build_dep_data():
    test_data = {
        "collectorA": [],
        "collectorB": ["collectorA", ],
        "collectorC": ["collectorA", "collectorB"],
        "collectorD": ["collectorC", "collectorA"],
    }
    dep_map = build_dep_data(test_data.keys(), test_data)
    assert dep_map == {
        "collectorA": set(),
        "collectorB": {"collectorA"},
        "collectorC": {"collectorA", "collectorB"},
        "collectorD": {"collectorC", "collectorA"}
        }



# Generated at 2022-06-13 00:25:39.077855
# Unit test for function get_collector_names
def test_get_collector_names():
    platforms = defaultdict(lambda: defaultdict(dict))
    platforms['Linux']['default']['gather_subset'] = frozenset(('all', '!facter'))
    platforms['Generic']['default']['gather_subset'] = frozenset(('network', 'hardware'))

    class FakeCollector:
        name = 'fake-name'
        required_facts = frozenset()

    valid_subsets = frozenset(('hardware', 'facter'))
    minimal_gather_subset = frozenset(('hardware'))
    aliases_map = defaultdict(set)
    aliases_map['hardware'] = frozenset(('devices', 'dmi'))


# Generated at 2022-06-13 00:25:47.454956
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():

    class Picker:
        name = 'picker'

        @classmethod
        def platform_match(cls, platform_info):
            return cls

        def collect(self):
            return dict(foo='bar')

        def required_facts(self):
            return set()

    class Requiring:
        name = 'requiring'

        @classmethod
        def platform_match(cls, platform_info):
            return cls

        def collect(self):
            return dict(foo='bar')

        def required_facts(self):
            return set(['picker'])

    all_fact_subsets = dict()
    all_fact_subsets['picker'] = [Picker]
    all_fact_subsets['requiring'] = [Requiring]


# Generated at 2022-06-13 00:25:58.812018
# Unit test for function find_collectors_for_platform
def test_find_collectors_for_platform():
    class Collector1(BaseFactCollector):
        _collector = 'Collector1'
        _platform = 'Generic'
        name = 'collector1'
    class Collector2(BaseFactCollector):
        _collector = 'Collector2'
        _platform = 'AIX'
        name = 'collector2'
    class Collector3(BaseFactCollector):
        _collector = 'Collector3'
        _platform = 'Linux'
        name = 'collector3'

    class Linux:
        system = 'Linux'
    class Solaris:
        system = 'SunOS'

    # Verify the find_collectors_for_platform function returns the correct collector
    assert find_collectors_for_platform([Collector1, Collector2, Collector3], [Solaris]) == set()
    assert find_collectors_for

# Generated at 2022-06-13 00:26:08.997292
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    all_fact_subsets = {
        'a': [make_collector_class('a', required_facts=set(['b']))],
        'b': [make_collector_class('b', required_facts=set(['c']))],
        'c': [make_collector_class('c', required_facts=set(['d']))],
        'd': [make_collector_class('d', required_facts=set(['e']))],
        'e': [make_collector_class('e', required_facts=set([]))],
    }

    collector_names = ['a', 'b', 'c', 'd']

    unresolved = find_unresolved_requires(collector_names, all_fact_subsets)
    assert set(['e']) == unresolved

    unresolved = find_

# Generated at 2022-06-13 00:26:22.486393
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    class CollectorA(BaseFactCollector):
        name = 'A'
        _fact_ids = set(['foo'])

    class CollectorB(BaseFactCollector):
        name = 'B'

    class CollectorC(BaseFactCollector):
        name = 'C'
        _fact_ids = set(['foo'])

    class CollectorD(BaseFactCollector):
        name = 'D'
        _fact_ids = set(['foo'])

    mapped_collectors, aliases_map = build_fact_id_to_collector_map(
        [CollectorA, CollectorB, CollectorC, CollectorD])

    assert ['A'] == mapped_collectors['A']
    assert ['B'] == mapped_collectors['B']

# Generated at 2022-06-13 00:26:25.979219
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    return_value = build_fact_id_to_collector_map([])
    assert return_value == ((defaultdict(list), defaultdict(set)),), "The return value is not expected."



# Generated at 2022-06-13 00:26:37.377021
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    class Platform(object):
        def __init__(self, product_name):
            self.product_name = product_name

    class CollectTest1(BaseFactCollector):
        # platform not defined, it should match 'ProductX'
        name = 'collect_test1'
        fact_ids = ['collect_test1']

    class CollectTest2(BaseFactCollector):
        _platform = 'ProductY'
        name = 'collect_test2'
        fact_ids = ['collect_test2']

    class CollectTest3(BaseFactCollector):
        _platform = 'ProductZ'
        name = 'collect_test3'
        fact_ids = ['collect_test3']

    class CollectTest4(BaseFactCollector):
        _platform = 'ProductX'
        name = 'collect_test4'
        fact_

# Generated at 2022-06-13 00:26:46.062561
# Unit test for function select_collector_classes
def test_select_collector_classes():
    class Collector_A(BaseFactCollector):
        name = 'A'
    class Collector_B(BaseFactCollector):
        name = 'B'
        _fact_ids = ['x']
    class Collector_C(BaseFactCollector):
        name = 'C'
        _fact_ids = ['x', 'y']
    class Collector_D(BaseFactCollector):
        name = 'D'
        _fact_ids = ['y']
        required_facts = ['C']
    class Collector_E(BaseFactCollector):
        name = 'E'
        required_facts = ['A']

    test_all_fact_subsets = defaultdict(list)
    test_all_fact_subsets[Collector_A.name] = [Collector_A]
    test_all_fact_subsets['x']

# Generated at 2022-06-13 00:26:55.174352
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    '''
    Test find_unresolved_requires:
       - Should return empty set if all required facts in collector_names
       - Should return set with required fact, if required fact is not in collector_names
    '''
    test_collector_classes = []

    class collector1(BaseFactCollector):
        name = 'collector1'
        required_facts = set(['collector2'])
    test_collector_classes.append(collector1)

    class collector2(BaseFactCollector):
        name = 'collector2'
        required_facts = set(['collector3'])
    test_collector_classes.append(collector2)

    class collector3(BaseFactCollector):
        name = 'collector3'
    test_collector_classes.append(collector3)

    fact_

# Generated at 2022-06-13 00:27:03.617785
# Unit test for function select_collector_classes
def test_select_collector_classes():
    class Foo(BaseFactCollector):
        name = 'foo'

    class Bar(BaseFactCollector):
        name = 'bar'

    class FooBar(BaseFactCollector):
        name = 'foobar'

    class FooBarBaz(BaseFactCollector):
        name = 'foobarbaz'

    foobarbaz_class = FooBarBaz
    foobar_class = FooBar
    bar_class = Bar
    foo_class = Foo

    # build the all_fact_subsets structure with both normal (using Foo as Foo's collector class)
    # and using both slightly-different classes (using FooBar as Foo's collector class)

# Generated at 2022-06-13 00:27:13.617990
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    all_fact_subsets = {'a': [BaseFactCollector], 'b': [BaseFactCollector], 'c': [BaseFactCollector]}

    # Test when .required_facts is a list
    required_facts_list = ['a']
    all_fact_subsets['a'][0].required_facts = required_facts_list
    collector_names = ['a']
    unresolved = find_unresolved_requires(collector_names, all_fact_subsets)
    assert len(unresolved) == 0, 'Unresolved requirement: %s' % unresolved

    required_facts_list = ['a', 'b']
    all_fact_subsets['b'][0].required_facts = required_facts_list
    collector_names = ['b', 'c']

# Generated at 2022-06-13 00:27:24.922388
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    '''this is a function in a module, not a class method, so we can't use a class decorator'''
    import unittest

    class Collector1(BaseFactCollector):
        name = 'collector1'
    class Collector2(BaseFactCollector):
        name = 'collector2'
        _fact_ids = ['alt_name']
    class Collector3(BaseFactCollector):
        name = 'collector3'
        _fact_ids = ['alt_name', 'alt_name_second']

    class TestBuildFactIdToCollectorMap(unittest.TestCase):

        def test_collector_name(self):
            fact_id_to_collector_map, aliases_map = build_fact_id_to_collector_map([Collector1, Collector2, Collector3])

# Generated at 2022-06-13 00:27:33.131036
# Unit test for function get_collector_names
def test_get_collector_names():
    try:
        get_collector_names(set(['a']), set(['b']), set(['c']))
    except Exception as e:
        assert str(e) == "Bad subset 'c' given to Ansible. gather_subset options allowed: all, a"

    assert get_collector_names(set(['a']), set(['b']), set(['a'])) == set(['a'])
    assert get_collector_names(set(['a']), set(['a', 'b']), set(['a'])) == set(['a', 'b'])
    assert get_collector_names(set(['a']), set(['b']), set(['a', 'b'])) == set(['a', 'b'])

# Generated at 2022-06-13 00:27:45.610141
# Unit test for function tsort
def test_tsort():
    test1 = {
        'a': set(['b']),
        'b': set(['c']),
        'c': set(),
    }
    test2 = {
        'a': set(['b', 'c']),
        'b': set(['c']),
        'c': set(),
    }
    test3 = {
        'a': set(['b']),
        'b': set(['c']),
        'c': set(['a']),
    }
    test4 = {
        'a': set(['b']),
        'b': set(['c']),
        'c': set(['a']),
        'd': set([]),
    }


# Generated at 2022-06-13 00:28:07.301836
# Unit test for function find_collectors_for_platform
def test_find_collectors_for_platform():
    all_collector_classes = set([LinuxFactCollector,
                                 GenericFactCollector,
                                 SolarisFactCollector])
    compat_platforms = [{'system': 'Linux'},
                        {'system': 'SunOS'},
                        {'system': 'FreeBSD'}]
    assert find_collectors_for_platform(all_collector_classes, compat_platforms) == set([LinuxFactCollector,
                                                                                          GenericFactCollector,
                                                                                          SolarisFactCollector])

    all_collector_classes = set([LinuxFactCollector,
                                 GenericFactCollector,
                                 SolarisFactCollector])

# Generated at 2022-06-13 00:28:19.166448
# Unit test for function find_collectors_for_platform
def test_find_collectors_for_platform():
    class CollectorA(BaseFactCollector):
        name = 'A'
        _fact_ids = {'A1'}
        _platform = 'Generic'

    class CollectorB(BaseFactCollector):
        name = 'B'
        _fact_ids = {'B1'}
        _platform = 'Linux'

    class CollectorC(BaseFactCollector):
        name = 'C'
        _fact_ids = {'C1'}
        _platform = 'Linux'

    class CollectorD(BaseFactCollector):
        name = 'D'
        _fact_ids = {'D1'}
        _platform = 'Darwin'

    all_collectors = (CollectorA, CollectorB, CollectorC, CollectorD)


# Generated at 2022-06-13 00:28:27.307409
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    from ansible.module_utils.facts.network.base import NetworkCollector, NetworkDefault, NetworkHardware, NetworkInterface
    from ansible.module_utils.facts.system.base import Distribution, Machine, OSCollector

    collectors = [Distribution, Machine, OSCollector, NetworkCollector, NetworkDefault, NetworkHardware, NetworkInterface]
    all_fact_subsets = defaultdict(list)
    for collector in collectors:
        for fact_id in collector._fact_ids:
            all_fact_subsets[fact_id].append(collector)

    assert all_fact_subsets['network'] == [NetworkCollector]
    assert len(all_fact_subsets['network.interfaces']) == 2
    assert NetworkDefault in all_fact_subsets['network.interfaces']

# Generated at 2022-06-13 00:28:38.173664
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    '''
    Test find_unresolved_requires()
    '''

    class StubClass:
        def __init__(self, name, required_facts):
            self.name = name
            self.required_facts = set(required_facts)

    class StubCollectorClass(StubClass):
        pass

    class StubSubClass(StubClass):
        pass


# Generated at 2022-06-13 00:28:48.813000
# Unit test for function tsort
def test_tsort():
    # https://en.wikipedia.org/wiki/Topological_sorting#Depth-first_search

    unsorted_map = {'1': {'3', '4'}, '2': {'4'}, '3': {'4', '5'}, '4': set(), '5': {'6'}, '6': set()}

    # expected list of (node, edges)
    expected_list = [('2', {'4'}), ('1', {'3', '4'}), ('3', {'4', '5'}), ('5', {'6'}), ('6', set()), ('4', set())]

    assert tsort(unsorted_map) == expected_list, 'tsort returned unexpected result'



# Generated at 2022-06-13 00:28:58.282288
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    # setup test data
    class TestCollector1(BaseFactCollector):
        name = 'test1'
        _fact_ids = ['test1', 'test1.1']
    class TestCollector2(BaseFactCollector):
        name = 'test2'
        _fact_ids = ['test2']

    collectors_for_platform = [TestCollector1, TestCollector2]

    fact_id_to_collector_map, aliases_map = build_fact_id_to_collector_map(collectors_for_platform)

    # tests
    assert fact_id_to_collector_map['test1'][0] == TestCollector1
    assert fact_id_to_collector_map['test1.1'][0] == TestCollector1
    assert fact_id_to_collector_

# Generated at 2022-06-13 00:29:07.597917
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    import mock

    not_supported_collector = type('NotSupportedCollector', (BaseFactCollector,),
                                   dict(required_facts=set(), name='not_supported_collector'))
    supported_collector = type('SupportedCollector', (BaseFactCollector,),
                               dict(required_facts=set(), name='supported_collector'))
    collector_that_requires_not_supported = type('RequiringCollector', (BaseFactCollector,),
                                                 dict(required_facts=set(['not_supported_collector']),
                                                      name='requiring_collector'))

# Generated at 2022-06-13 00:29:16.750366
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    from ansible.module_utils.facts.system.platform import PlatformFactCollector
    from ansible.module_utils.facts.system.distribution import DistributionFactCollector
    from ansible.module_utils.facts.system.selinux import SELinuxFactCollector
    all_fact_subsets = {'platform': [PlatformFactCollector],
                        'distribution': [DistributionFactCollector],
                        'selinux': [SELinuxFactCollector]}

    assert find_unresolved_requires(['distribution'], all_fact_subsets) == set()
    assert find_unresolved_requires(['distribution','platform'], all_fact_subsets) == set()

# Generated at 2022-06-13 00:29:24.688743
# Unit test for function build_dep_data
def test_build_dep_data():
    collector_names = ['test_collector_name']
    all_fact_subsets = defaultdict(dict)
    all_fact_subsets['test_collector_name'] = ['test_collector_deps']
    dep_map = build_dep_data(collector_names, all_fact_subsets)
    assert 'test_collector_name' in dep_map
    assert 'test_collector_deps' in dep_map['test_collector_name']



# Generated at 2022-06-13 00:29:36.932735
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():

    from ansible.module_utils.facts import cache
    import ansible.module_utils.facts.collector.base
    import ansible.module_utils.facts.collector.network

    all_fact_subsets = cache.collector_classes_from_dir(
        (ansible.module_utils.facts.collector.base, ansible.module_utils.facts.collector.network))

    # if no unresolved names, should return empty list
    assert not find_unresolved_requires(['network'], all_fact_subsets)
    assert len(find_unresolved_requires(['network', 'dmi'], all_fact_subsets)) == 1
    assert 'dmi' in find_unresolved_requires(['network', 'dmi'], all_fact_subsets)
    assert not find_unres

# Generated at 2022-06-13 00:29:55.968749
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    known_collectors = frozenset([
        'platform', 'hardware', 'virtual', 'cpu', 'network', 'dmi', 'system'])
    minimal_gather_subset = ['network', 'virtual']
    gather_subset = ['all']
    fact_collector_names = get_collector_names(
        valid_subsets=known_collectors,
        minimal_gather_subset=minimal_gather_subset,
        gather_subset=gather_subset,
        platform_info=platform_info)
    all_fact_subsets = {}
    # intentionally not setting 'virtual' (because it is listed in minimal_gather_subset)
    # and not setting 'dmi' (because it depends on 'system' which we are not adding)

# Generated at 2022-06-13 00:30:03.112998
# Unit test for function get_collector_names
def test_get_collector_names():

    # Test without any subset or aliases
    valid_subsets = ('all', 'min', 'network', 'hardware', 'virtual', 'facter')
    minimal_gather_subset = frozenset(('facter',))
    gather_subset = ['!all']
    aliases_map = defaultdict(set)
    collector_names = get_collector_names(
        valid_subsets=valid_subsets,
        minimal_gather_subset=minimal_gather_subset,
        aliases_map=aliases_map,
        gather_subset=gather_subset,
    )
    assert (collector_names == minimal_gather_subset)

    # Test with subset aliases

# Generated at 2022-06-13 00:30:14.862258
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    from ansible_collections.notstdlib.moveitallout.plugins.module_utils.facts.collectors import (
        get_collector_names, build_fact_id_to_collector_map, select_collector_classes,
        find_unresolved_requires,
    )


# Generated at 2022-06-13 00:30:15.430404
# Unit test for function select_collector_classes
def test_select_collector_classes():
    pass



# Generated at 2022-06-13 00:30:20.775834
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    collector_names = [
        'foo',
        'bar',
        'baz',
    ]
    all_fact_subsets = dict(
        foo=[Foo(), Bar()],
        bar=[],
        baz=[Baz()],
    )

    assert find_unresolved_requires(collector_names, all_fact_subsets) == {'qux'}



# Generated at 2022-06-13 00:30:32.215120
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    from ansible.module_utils.facts.collectors.hardware import Hardware
    from ansible.module_utils.facts.collectors.network import Network
    from ansible.module_utils.facts.collectors.dmi import Dmi
    from ansible.module_utils.facts.collectors.pkg_mgr import PkgMgr
    from ansible.module_utils.facts.collectors.system import System
    from ansible.module_utils.facts.collectors.distribution import Distribution

    collectors_for_platform = set([Hardware, Network, Dmi, PkgMgr, System, Distribution])
    fact_id_to_collector_map, aliases_map = build_fact_id_to_collector_map(collectors_for_platform)

    # check dict size

# Generated at 2022-06-13 00:30:39.027521
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    all_fact_subsets = {
        'network': [
            FactCollectorNetwork
        ],
        'system': [
            FactCollectorSystem,
        ],
        'interfaces': [
            FactCollectorInterfaces,
        ],
        'ipv4_addresses': [
            FactCollectorIPv4Addresses,
        ],
        'ipv6_addresses': [
            FactCollectorIPv6Addresses,
        ],
    }

    # all collectors are available
    collector_names = ['network', 'system', 'interfaces', 'ipv4_addresses', 'ipv6_addresses']
    assert find_unresolved_requires(collector_names, all_fact_subsets) == set()

    # network collector is missing

# Generated at 2022-06-13 00:30:49.792697
# Unit test for function select_collector_classes
def test_select_collector_classes():
    #  Select collectors which represents 'all' gather_subset
    #  but collect facts only from 'system_system' and 'ohai_system' collectors
    config = {'system': {'*': {'system': {'system': 'ohai_system',
                                          'system_system': 'system_system'}}}}

    #  Simulate fact_ids, fact_ids can be subset of fact_names
    fact_ids = {'system_system': {'system_system', 'ohai_system'},
                'ohai_system': {'system_system', 'ohai_system'}}

    #  Simulate list of all fact collectors
    class CollectorsContainer:
        def __init__(self, collector_name, fact_ids):
            self.name = collector_name
            self._fact_ids = fact_ids

# Generated at 2022-06-13 00:30:56.231095
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    class TestCollector(BaseFactCollector):
        name = 'test_collector'
        _fact_ids = ('test_collector', 'test_alias')

    assert build_fact_id_to_collector_map([TestCollector]) == (
        defaultdict(list, {
            'test_collector': [TestCollector],
            'test_alias': [TestCollector]
        }),
        defaultdict(set, {
            'test_collector': {'test_collector', 'test_alias'}
        })
    )



# Generated at 2022-06-13 00:31:07.760415
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    from ansible.module_utils.facts import collector

    # We will use some of the existing FactCollectors for this test
    all_fact_subsets = {
        # collectors that have no requires
        'subset_one': [collector.FactsCollector],
        'subset_two': [collector.FactsCollector],
        'subset_three': [collector.FactsCollector],
        # collectors that require subset_three
        'subset_four': [collector.FactsCollector],
        'subset_five': [collector.FactsCollector],
        # subset_six requires subset_four and subset_five
        'subset_six': [collector.FactsCollector]
    }
    for collector_name in all_fact_subsets:
        collector_class = all_fact_sub

# Generated at 2022-06-13 00:31:23.392623
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    class A(BaseFactCollector):
        name = 'A'
    class B(BaseFactCollector):
        name = 'B'
    class C(BaseFactCollector):
        name = 'C'
        required_facts = {'A'}

    all_fact_subsets = {'A': [A], 'B': [B], 'C': [C]}

    assert find_unresolved_requires(['A', 'B'], all_fact_subsets) == set()
    assert find_unresolved_requires(['B', 'C'], all_fact_subsets) == set(['A'])
    assert find_unresolved_requires(['A', 'B', 'C'], all_fact_subsets) == set()



# Generated at 2022-06-13 00:31:32.283139
# Unit test for function build_dep_data
def test_build_dep_data():
    collector_names = set()
    all_subsets = {}
    dep_map = build_dep_data(collector_names, all_subsets)
    assert dep_map == {}

    class TestCollector:
        required_facts = set()

    class A(TestCollector):
        name = 'A'
    class B(TestCollector):
        name = 'B'
        required_facts = set(['A'])
    class C(TestCollector):
        name = 'C'
        required_facts = set(['B'])

    collector_names = set(['A', 'B', 'C'])
    all_subsets = {'A': [A], 'B': [B], 'C': [C]}
    dep_map = build_dep_data(collector_names, all_subsets)


# Generated at 2022-06-13 00:31:44.147123
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    class FakeCollector(BaseFactCollector):
        _fact_ids = ('foo', 'bar')
        name = 'fake_collector'

    class FakeCollector2(BaseFactCollector):
        _fact_ids = ('foo2',)
        name = 'fake_collector2'

    class FakeCollector3(BaseFactCollector):
        _fact_ids = ('foo', 'bar',)
        name = 'fake_collector3'

    fact_id_to_collector_map, aliases_map = build_fact_id_to_collector_map(
        [FakeCollector, FakeCollector2, FakeCollector3])

# Generated at 2022-06-13 00:31:55.556919
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    all_fact_subsets = {
        'os': [],
        'virtual': [],
        'network': [],
        'hardware': [],
        'distribution': [],
        'puppet': []
    }
    assert set(['os']) == find_unresolved_requires(['puppet', 'hardware'], all_fact_subsets)

    all_fact_subsets = {
        'os': [],
        'virtual': [],
        'network': [],
        'hardware': [],
        'distribution': [],
        'puppet': []
    }
    assert set() == find_unresolved_requires(['os'], all_fact_subsets)

    all_fact_subsets = {}

# Generated at 2022-06-13 00:32:05.942300
# Unit test for function build_dep_data
def test_build_dep_data():
    import unittest
    import simplejson as json
    from ansible.module_utils.facts import collector

    class TestCollectorA(collector.BaseFactCollector):
        name = 'collector_a'
        required_facts = set(['collector_b'])

    class TestCollectorB(collector.BaseFactCollector):
        name = 'collector_b'
        required_facts = set(['collector_c', 'collector_d'])

    class TestCollectorC(collector.BaseFactCollector):
        name = 'collector_c'

    class TestCollectorD(collector.BaseFactCollector):
        name = 'collector_d'

    test_collector_classes = [TestCollectorA, TestCollectorB, TestCollectorC, TestCollectorD]
    all_

# Generated at 2022-06-13 00:32:16.053142
# Unit test for function select_collector_classes
def test_select_collector_classes():
    from ansible.module_utils.facts.collector import select_collector_classes
    all_fact_subsets = defaultdict(dict)
    all_fact_subsets['foo'][1] = 'a'
    all_fact_subsets['foo'][2] = 'c'
    all_fact_subsets['foo'][3] = 'b'
    all_fact_subsets['bar'][2] = 'a'
    all_fact_subsets['bar'][3] = 'b'
    all_fact_subsets['bar'][4] = 'c'
    all_fact_subsets['bar'][5] = 'd'

    collector_names = ['foo', 'bar']


# Generated at 2022-06-13 00:32:25.751568
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    assert find_unresolved_requires(
        collector_names=['all'],
        all_fact_subsets={'all': ['linux']}
    ) == {'linux'}
    assert find_unresolved_requires(
        collector_names=['linux'],
        all_fact_subsets={'linux': ['all']}
    ) == {'all'}
    assert find_unresolved_requires(
        collector_names=['linux'],
        all_fact_subsets={'linux': [{'required_facts': ['all']}]}
    ) == {'all'}
    assert find_unresolved_requires(
        collector_names=['linux'],
        all_fact_subsets={'linux': [{'required_facts': []}]}
    ) == set()
    assert find_

# Generated at 2022-06-13 00:32:31.165531
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    all_fact_subsets = {'foo': [object(), object()],
                        'bar': [object(), object()]}

    collector_names = ['foo']
    results = find_unresolved_requires(collector_names, all_fact_subsets)
    assert list(results) == ['foo', 'bar']



# Generated at 2022-06-13 00:32:40.616874
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    import sys
    import os
    import unittest

    from ansible.module_utils.facts import get_collector_classes, get_collector_class_for_name

    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'lib', 'ansible', 'module_utils', 'facts'))

    class DummyFactCollector1(BaseFactCollector):
        name = 'dummy1'
        _fact_ids = ['foo', 'bar']

    class DummyFactCollector2(BaseFactCollector):
        name = 'dummy2'
        _fact_ids = ['foo', 'baz']

    class DummyFactCollector3(BaseFactCollector):
        name = 'dummy3'
        _fact_ids

# Generated at 2022-06-13 00:32:47.896822
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():

    class TestCollectorA(BaseFactCollector):
        name = 'A'
        required_facts = {'B'}

    class TestCollectorB(BaseFactCollector):
        name = 'B'
        required_facts = {'C'}

    class TestCollectorC(BaseFactCollector):
        name = 'C'
        required_facts = set()

    # Collectors A and B exist, but no C
    all_fact_subsets = {'A': [TestCollectorA], 'B': [TestCollectorB]}

    # When collector_names has only collector A
    collector_names = set(['A'])
    unresolved = find_unresolved_requires(collector_names, all_fact_subsets)
    assert 'C' in unresolved

    # When collector_names has only collector B
    collector

# Generated at 2022-06-13 00:33:00.201675
# Unit test for function build_dep_data
def test_build_dep_data():
    pass



# Generated at 2022-06-13 00:33:10.661054
# Unit test for function select_collector_classes
def test_select_collector_classes():
    from ansible.module_utils.facts import command
    from ansible.module_utils.facts import system
    from ansible.module_utils.facts import virtual
    from ansible.module_utils.facts import hardware
    from ansible.module_utils.facts import network
    from ansible.module_utils.facts import distribution
    from ansible.module_utils.facts import darwin
    from ansible.module_utils.facts import pkg_mgr
    from ansible.module_utils.facts import systemd

    all_fact_subsets = {}
    platform_info = {'system': 'Darwin'}

# Generated at 2022-06-13 00:33:22.173933
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    from . import facts

    all_fact_collectors = facts.get_collector_classes()

    result = find_unresolved_requires(['service_mgr'], all_fact_collectors)
    assert result == set([])

    result = find_unresolved_requires(['service_mgr'], {})
    assert result == set([])

    result = find_unresolved_requires(['sevice_mgr'], all_fact_collectors)
    assert result == set(['sevice_mgr'])

    result = find_unresolved_requires(['default_ipv4', 'default_ipv6'], all_fact_collectors)
    assert result == set([])


# Generated at 2022-06-13 00:33:28.974775
# Unit test for function build_dep_data
def test_build_dep_data():
    result = build_dep_data(['apt','ip','dmi','facter','augeas','docker','networking'], all_fact_subsets)
    assert result['apt'] == set()
    assert result['ip'] == set(['networking'])
    assert result['augeas'] == set(['facter'])
    assert result['docker'] == set(['networking'])
    assert result['networking'] == set(['facter'])


# Generated at 2022-06-13 00:33:35.283302
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    # Setup
    all_fact_subsets = {
        'a': [1, 2, 3],
        'b': [4, 5, 6],
        'c': [7, 8, 9],
        'd': [10, 11, 12],
        'e': [13, 14, 15],
        'f': [16, 17, 18]
    }

    # Test
    res = find_unresolved_requires(['a'], all_fact_subsets)
    assert res == set()

    res = find_unresolved_requires(['a', 'b'], all_fact_subsets)
    assert res == set()

    res = find_unresolved_requires(['a', 'b', 'c'], all_fact_subsets)
    assert res == set()

    res = find_unres

# Generated at 2022-06-13 00:33:44.484832
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    import json
    import sys

    import ansible.module_utils.facts.collector.network as network_collector
    import ansible.module_utils.facts.collector.hardware as hardware_collector
    import ansible.module_utils.facts.collector.platform as platform_collector

    class MockCollector(BaseFactCollector):
        name = 'mock_collector'
        _fact_ids = set()

    class MockNetworkCollector(network_collector.NetworkCollector):
        name = 'mock_network_collector'
        _fact_ids = set()
        required_facts = {'network'}

    class MockHardwareCollector(hardware_collector.HardwareCollector):
        name = 'mock_hardware_collector'
        _fact_ids = set()
        required_facts

# Generated at 2022-06-13 00:33:54.121262
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    from ansible.module_utils.facts import collector as facts_collector
    import pytest

    def test_collector_class(some_facts):
        return type('TestCollector', (facts_collector.BaseFactCollector, ), {
            'name': 'test_collector',
            '_fact_ids': some_facts
        })

    class TestMinCollector(facts_collector.BaseFactCollector):
        name = 'test_min_collector'


# Generated at 2022-06-13 00:34:02.064624
# Unit test for function select_collector_classes
def test_select_collector_classes():
    class FakeSubset(object):
        _fact_ids = ['fake']
    fake_subset = FakeSubset()
    class FakeSubsetB(object):
        _fact_ids = ['fake']
    fake_subset_b = FakeSubsetB()
    all_fact_subsets = {'fake': [fake_subset, fake_subset_b]}
    assert len(select_collector_classes(['fake'], all_fact_subsets)) == 1
    assert len(select_collector_classes(['fake', 'fake'], all_fact_subsets)) == 1



# Generated at 2022-06-13 00:34:09.269396
# Unit test for function get_collector_names
def test_get_collector_names():
    '''Test function get_collector_names.'''
    additional_subsets_expect = set(['min', '!network', 'hardware', 'devices'])
    additional_subsets = get_collector_names(
        valid_subsets=frozenset(['network', 'hardware', 'devices', 'disks', 'virtual']),
        minimal_gather_subset=frozenset(['min']),
        gather_subset=['min', '!network', 'hardware', 'devices'],
        aliases_map=defaultdict(set, {
            'hardware': frozenset(['devices', 'dmi']),
        })
    )
    assert additional_subsets == additional_subsets_expect

