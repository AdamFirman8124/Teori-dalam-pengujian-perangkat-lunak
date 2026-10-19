

# Generated at 2022-06-13 00:24:42.438981
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    # included a duplicate to verify that does not affect the result
    all_fact_subsets = {
        'f1': [object(), object()],
        'f2': [object(), object()],
        'f3': [object()],
    }
    # Create a mock collector class that requires 'f1'
    requires_f1 = object()
    requires_f1.required_facts = frozenset(['f1'])

    # Create a mock collect class that requires 'f2' and 'f3'
    requires_f2_f3 = object()
    requires_f2_f3.required_facts = frozenset(['f2', 'f3'])

    # Create a mock collect class that requires 'f4'
    requires_f4 = object()

# Generated at 2022-06-13 00:24:54.986405
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    from ansible.module_utils.facts.collectors.network import InterfacesCollector, RouteCollector
    from ansible.module_utils.facts.collectors import default
    from ansible.module_utils.facts.collectors.platform.aix import AixCollector
    from ansible.module_utils.facts.collectors.platform.openbsd import OpenBSDCollector
    from ansible.module_utils.facts.collectors.platform.netbsd import NetBSDCollector
    from ansible.module_utils.facts.collectors.platform.freebsd import FreeBSDCollector
    from ansible.module_utils.facts.collectors.platform.darwin import DarwinCollector
    from ansible.module_utils.facts.collectors.platform.windows import WindowsCollector

# Generated at 2022-06-13 00:24:59.218332
# Unit test for function build_dep_data
def test_build_dep_data():
    dep_map = {
        'foo': set(['bar']),
        'bar': set(['foo']),
    }
    foo_deps = set(['bar'])
    bar_deps = set(['foo'])
    dep_map_test = build_dep_data(set(['foo', 'bar']), dep_map)
    if foo_deps != dep_map_test['foo']:
        raise AssertionError
    if bar_deps != dep_map_test['bar']:
        raise AssertionError



# Generated at 2022-06-13 00:25:08.720517
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():

    class TestCollector1(BaseFactCollector):
        name = 'a'
        _fact_ids = frozenset(['b', 'c'])

    class TestCollector2(BaseFactCollector):
        name = 'd'
        _fact_ids = frozenset(['e', 'f', 'g'])

    class TestCollector3(BaseFactCollector):
        name = 'z'
        _fact_ids = frozenset(['y'])

    # this one has a name that is also in _fact_ids
    class TestCollector4(BaseFactCollector):
        name = 'h'
        _fact_ids = frozenset(['h', 'i', 'j', 'k'])

    class TestCollector5(BaseFactCollector):
        name = 'm'
        _fact_ids

# Generated at 2022-06-13 00:25:19.403091
# Unit test for function get_collector_names
def test_get_collector_names():
    all_subsets = set(['network', 'dmi', 'distribution', 'software', 'devices', 'memory', 'virtual'])
    minimal_subsets = set(['network'])
    aliases_map = defaultdict(set)
    aliases_map['hardware'] = set(['dmi', 'devices'])
    platform_info = {}
    # Test: gathering all
    gather_subset = ['all']
    assert get_collector_names(all_subsets, minimal_subsets, gather_subset, aliases_map, platform_info) == all_subsets

    # Test: gathering all with hardware excluded
    gather_subset = ['!hardware', 'all']

# Generated at 2022-06-13 00:25:27.947985
# Unit test for function build_dep_data

# Generated at 2022-06-13 00:25:39.530075
# Unit test for function get_collector_names
def test_get_collector_names():
    aliases_map = defaultdict(set)
    aliases_map['hardware'] = ['devices', 'dmi']
    aliases_map['software'].add('os')

    valid_subsets = frozenset(['network', 'hardware', 'virtual',
                               'interfaces', 'all', 'devices',
                               'software', 'dmi', 'os',
                               'min'])
    minimal_gather_subsets = frozenset(['network', 'hardware'])


# Generated at 2022-06-13 00:25:43.057959
# Unit test for function build_dep_data
def test_build_dep_data():
    dep_map = build_dep_data(['a', 'b'], {'a': [1,2], 'b': [3,4]})
    assert(dep_map['a'] == set())
    assert(dep_map['b'] == set())


# Generated at 2022-06-13 00:25:54.095188
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    class CollectorA(BaseFactCollector):
        name = 'A'
        required_facts = set()

    class CollectorB(BaseFactCollector):
        name = 'B'
        required_facts = {'A'}

    class CollectorC(BaseFactCollector):
        name = 'C'
        required_facts = set()

    class CollectorD(BaseFactCollector):
        name = 'D'
        required_facts = {'B', 'C'}

    class CollectorE(BaseFactCollector):
        name = 'E'
        required_facts = {'C', 'F'}

    fact_subsets = defaultdict(set)
    fact_subsets['A'].add(CollectorA)
    fact_subsets['B'].add(CollectorB)
    fact_subsets['C'].add

# Generated at 2022-06-13 00:26:05.099738
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.collector.system import SystemFactCollector

    # the trivial case, everything is already resolved
    collector_names = ['all', 'system']
    all_fact_subsets = {'all': [BaseFactCollector], 'system': [SystemFactCollector]}
    assert find_unresolved_requires(collector_names, all_fact_subsets) == set()

    # now we have a unresolved fact (dummy)
    collector_names = ['all', 'system', 'dummy']
    all_fact_subsets = {'all': [BaseFactCollector], 'system': [SystemFactCollector], 'dummy': [DummyCollector]}

# Generated at 2022-06-13 00:26:21.001850
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    logger_mock = Mock(name='Mock logger')
    all_fact_subsets = defaultdict(list)
    class FakeB:
        name = 'b'
        required_facts = {'foo', 'bar'}
    class FakeC:
        name = 'c'
        required_facts = {'foo'}
    class FakeD:
        name = 'd'
        required_facts = {'foo', 'bar', 'baz'}
    class FakeE:
        name = 'e'
        required_facts = {'foo', 'bar', 'baz'}
    all_fact_subsets['b'] = [FakeB]
    all_fact_subsets['c'] = [FakeC]
    all_fact_subsets['d'] = [FakeD]

# Generated at 2022-06-13 00:26:34.264478
# Unit test for function build_dep_data
def test_build_dep_data():
    '''Unit test for function build_dep_data
    '''
    all_fact_subsets = {
        'one': [FakeClass('one', ['two'])],
        'two': [FakeClass('two', ['three'])],
        'three': [FakeClass('three')],
        'four': [FakeClass('four', ['five', 'six'])],
        'five': [FakeClass('five', ['six'])],
        'six': [FakeClass('six')]
    }
    collector_names = ['one', 'two', 'three', 'four', 'five', 'six']

# Generated at 2022-06-13 00:26:44.840326
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    import sys
    import os
    import ansible.module_utils.facts.collector
    # Get a list of all the fact collectors
    fact_collectors = [sys.modules[__name__]]

    from ansible.module_utils.facts import system
    from ansible.module_utils.facts import virtual
    from ansible.module_utils.facts import hardware
    from ansible.module_utils.facts import network
    from ansible.module_utils.facts import distribution
    from ansible.module_utils.facts import collector
    fact_collectors.extend([system, virtual, hardware, network, distribution, collector])


# Generated at 2022-06-13 00:26:54.132998
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    from ansible.module_utils.facts.collector.base import (
        BaseFactCollector,
        build_fact_id_to_collector_map,
    )

    class Test1(BaseFactCollector):
        name = 'test1'
        _fact_ids = frozenset(['test_id1'])

    class Test2(BaseFactCollector):
        name = 'test2'
        _fact_ids = frozenset(['test_id2'])

    class Test3(BaseFactCollector):
        name = 'test3'
        _fact_ids = frozenset(['test_id3'])

    class Test4(BaseFactCollector):
        name = 'test4'
        _fact_ids = frozenset(['test_id4'])


# Generated at 2022-06-13 00:27:06.008823
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.facts.collector import get_collector_name_map
    from ansible.module_utils.facts.collector import get_collector_names

    module = AnsibleModule(
        argument_spec=dict(
            gather_subset=dict(type='list'),
            gather_timeout=dict(type='int'),
            gather_subset=dict(type='list'),
            gather_network_resources=dict(type='int', default=0),
            namespace=dict(type='str'),
        )
    )

    # create a fake platform info
    platform_info = get_platform_info()
    platform_info['system'] = 'Linux'

    # The first step when gathering facts is to determine the compatible collectors for the platform
    #

# Generated at 2022-06-13 00:27:14.227250
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    all_fact_subsets = {
        'test_collector_a': [
            TestCollectorClassA,
        ],
        'test_collector_b': [
            TestCollectorClassB,
        ],
        'test_collector_c': [
            TestCollectorClassC,
        ],
        'test_collector_d': [
            TestCollectorClassD,
        ],
    }

    collector_names = ['test_collector_a']
    unresolved = find_unresolved_requires(collector_names, all_fact_subsets)

    assert unresolved == set(), 'Unresolved should be empty for trivial test case'

    collector_names = ['test_collector_a', 'test_collector_b']

# Generated at 2022-06-13 00:27:25.523341
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    import pytest
    from ansible.module_utils.facts import collector_mock

    # Make sure all our collectors have names
    collector_mock.CollectorA.name = 'CollectorA'
    collector_mock.CollectorB.name = 'CollectorB'
    collector_mock.CollectorC.name = 'CollectorC'

    # Quick-and-dirty mock of what we need from find_collectors_for_platform
    mock_fact_subsets = defaultdict(list)
    mock_fact_subsets['CollectorA'].append(collector_mock.CollectorA)
    mock_fact_subsets['CollectorB'].append(collector_mock.CollectorB)
    mock_fact_subsets['CollectorC'].append(collector_mock.CollectorC)



# Generated at 2022-06-13 00:27:29.166705
# Unit test for function find_collectors_for_platform
def test_find_collectors_for_platform():

    class TestCollector(BaseFactCollector):
        _platform = 'Generic'
        name = 'TestCollector'
        required_facts = set()

    test_collector = TestCollector()
    platform_info = {
        'distribution': 'distribution',
        'distribution_version': 'distribution_version',
        'system': 'Generic'
    }
    additional_collectors = find_collectors_for_platform([test_collector], [platform_info])
    assert len(additional_collectors) == 1



# Generated at 2022-06-13 00:27:35.676225
# Unit test for function find_collectors_for_platform
def test_find_collectors_for_platform():
    # Create example classes
    class LinuxAll(BaseFactCollector):
        name = "linux_all"
        _platform = 'Linux'
    class DarwinAll(BaseFactCollector):
        name = "darwin_all"
        _platform = 'Darwin'
    class UnknownAll(BaseFactCollector):
        name = "uknown_all"
        _platform = 'Unknown'
    class LinuxSpecific(BaseFactCollector):
        name = "linux_specific"
        _platform = 'Linux'
    class DarwinSpecific(BaseFactCollector):
        name = "darwin_specific"
        _platform = 'Darwin'
    class UnknownSpecific(BaseFactCollector):
        name = "uknown_specific"
        _platform = 'Unknown'

    # Create example arguments

# Generated at 2022-06-13 00:27:48.169437
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    # Test setup
    class Collector1(BaseFactCollector):
        _fact_ids = set(['c1_id1'])
        name = 'collector1'
        def collect(self, module=None, collected_facts=None):
            return {'1': 'collector1'}

    class Collector2(BaseFactCollector):
        _fact_ids = set(['c2_id1', 'c2_id2'])
        name = 'collector2'
        def collect(self, module=None, collected_facts=None):
            return {'2': 'collector2'}

    test_collectors_for_platform = [Collector1, Collector2]

    # Test basic functionality

# Generated at 2022-06-13 00:28:09.525925
# Unit test for function find_collectors_for_platform
def test_find_collectors_for_platform():
    import os
    import sys
    import inspect

    # Fake the presence of the modules in the search path.
    test_modules_dir = os.path.join(
        os.path.dirname(
            os.path.abspath(inspect.getfile(inspect.currentframe()))
        ),
        'fact_collector_plugins/'
    )
    sys.path.append(test_modules_dir)

    # Create fake platform info and fake fact collector classes.
    compat_platforms = [
        {'system': 'Linux'},
        {'system': 'Darwin'},
    ]

# Generated at 2022-06-13 00:28:20.939706
# Unit test for function find_collectors_for_platform
def test_find_collectors_for_platform():
    # Define some collectors
    class CollectA(BaseFactCollector):
        name = "A"
        _platform = "Foo1"

    class CollectB(BaseFactCollector):
        name = "B"
        _platform = "Foo1"

    class CollectC(BaseFactCollector):
        name = "C"
        _platform = "Foo2"

    class CollectD(BaseFactCollector):
        name = "D"
        _platform = "Foo2"

    class CollectE(BaseFactCollector):
        name = "E"
        _platform = "Foo3"

    class CollectF(BaseFactCollector):
        name = "F"
        _platform = "Foo4"

    class CollectG(BaseFactCollector):
        name = "G"

# Generated at 2022-06-13 00:28:28.316078
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    from a_collector import ACollector
    from b_collector import BCollector

    all_fact_subsets = {
        'a': [ACollector, ],
        'b': [BCollector, ],
    }

    assert find_unresolved_requires([], all_fact_subsets) == set()
    assert find_unresolved_requires(['a'], all_fact_subsets) == set()
    assert find_unresolved_requires(['a', 'b'], all_fact_subsets) == set()
    assert find_unresolved_requires(['b'], all_fact_subsets) == set(['a'])
    assert find_unresolved_requires(['a', 'b'], all_fact_subsets) == set()



# Generated at 2022-06-13 00:28:38.920861
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    class Collector1(BaseFactCollector):
        name = 'collector_1'
        _fact_ids = set(['c1'])

    class Collector2(BaseFactCollector):
        name = 'collector_2'
        _fact_ids = set(['c2', 'c2_alias'])

    @staticmethod
    def _platform_match(platform_info):
        return 'Generic'

    collectors_for_platform = set([Collector1, Collector2])
    fact_id_to_collector_map, aliases_map = build_fact_id_to_collector_map(collectors_for_platform)
    assert fact_id_to_collector_map['c1'][0] == Collector1
    assert fact_id_to_collector_map['c2'][0] == Collector2


# Generated at 2022-06-13 00:28:50.584058
# Unit test for function build_dep_data
def test_build_dep_data():
    from ansible.module_utils.facts.collector.system.distribution import DistributionFactCollector
    from ansible.module_utils.facts.collector.system.platform import PlatformFactCollector
    from ansible.module_utils.facts.collector.system.pkg_mgr import PkgMgrFactCollector
    expected_dict = {}
    expected_dict['distribution'] = {'system'}
    expected_dict['pkg_mgr'] = {'distribution'}
    expected_dict['platform'] = {}
    test_dict = {}
    test_dict['distribution'] = [DistributionFactCollector]
    test_dict['platform'] = [PlatformFactCollector]
    test_dict['pkg_mgr'] = [PkgMgrFactCollector]

# Generated at 2022-06-13 00:28:59.218659
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    all_fact_subsets = defaultdict(list)

    all_fact_subsets['test-a'].append(object())
    all_fact_subsets['test-b'].append(object())
    all_fact_subsets['test-c'].append(object())

    # create dummy class to use for testing
    class DummyCollector:
        def __init__(self, name, requires):
            self.name = name
            self.required_facts = requires

        def __repr__(self):
            return self.name

        def __hash__(self):
            return id(self)

        def __eq__(self, other):
            return hash(self) == hash(other)

    # create a set of collectors that require other collectors that are not in the collector names set.

# Generated at 2022-06-13 00:29:09.418037
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    # checking if collector mapping works
    collectors_for_platform = [
        {'_collector_classes': [
            [{'_fact_ids': None,
              'name': 'z',
              '_platform': 'Generic'},
             {'_fact_ids': None,
              'name': 'a',
              '_platform': 'Generic'}],
            [{'_fact_ids': None,
              'name': 'z',
              '_platform': 'Generic'}]]},
        {'_platform': 'Generic'}]

    assert build_fact_id_to_collector_map(collectors_for_platform) == ({}, defaultdict(set))

    # checking if collector mapping works

# Generated at 2022-06-13 00:29:13.489285
# Unit test for function build_dep_data
def test_build_dep_data():
    from collections import defaultdict
    collectors_for_platform = [BaseFactCollector, BaseFactsNetwork]
    
    # Test 1
    expected_dep_map = [{'network': ['BaseFactCollector'], 'BaseFactCollector': ['BaseFactsNetwork'], 'BaseFactsNetwork': []}]
    dep_map = defaultdict(set)
    for collector_name in all_fact_subsets:
        collector_deps = set()
        for collector in all_fact_subsets[collector_name]:
            for dep in collector.required_facts:
                collector_deps.add(dep)
        dep_map[collector_name] = collector_deps
    assert (dep_map == expected_dep_map)

    # Test 2

# Generated at 2022-06-13 00:29:22.429478
# Unit test for function build_dep_data
def test_build_dep_data():
    all_fact_subsets = {
        'system_info': [BaseFactCollector],
        'memory': [BaseFactCollector],
    }
    collector_names = [
        'system_info',
        'memory',
    ]
    dep_map = build_dep_data(collector_names, all_fact_subsets)
    assert dep_map == {
        'system_info': set(),
        'memory': set(),
    }


# Generated at 2022-06-13 00:29:35.013545
# Unit test for function get_collector_names
def test_get_collector_names():
    """Test get_collector_names"""
    assert get_collector_names(['a', 'b']) == set([])
    assert get_collector_names(set(['a', 'b']), ['a', 'b']) == set(['a', 'b'])

    # just checking it is reentrant and returns the same value regardless of whether
    # gather_subset is known
    assert get_collector_names(set(['a', 'b', 'c']), ['a', 'b'], set(['a', 'b'])) == set(['a', 'b'])
    assert get_collector_names(set(['a', 'b', 'c']), ['c'], set(['a', 'b'])) == set(['a', 'b'])

# Generated at 2022-06-13 00:29:57.690847
# Unit test for function find_collectors_for_platform
def test_find_collectors_for_platform():
    # test the function without any collector classes
    assert find_collectors_for_platform((), ()) == set()

    # test the function without any platform info
    class A(BaseFactCollector):
        name = 'a'
    assert find_collectors_for_platform((A,), []) == set()

    # test with a class that does not match any platform info
    class B(BaseFactCollector):
        name = 'b'
        _platform = 'UNKNOWN'
    assert find_collectors_for_platform((A, B), []) == {A}

    # test with a class that does match a platform
    platform_info = {
        'system': 'Linux'
    }
    assert find_collectors_for_platform((A, B), [platform_info]) == {A, B}

    # test with a classes

# Generated at 2022-06-13 00:30:10.215623
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    class FakeCollector1(object):
        _fact_ids = ['foo', 'bar']
        name = 'fake_collector_1'

    class FakeCollector2(FakeCollector1):
        _fact_ids = ['baz']

    class FakeCollector3(FakeCollector2):
        _fact_ids = ['baz', 'bar']

    class FakeCollector4(FakeCollector3):
        _fact_ids = ['baz']

    class FakeCollector5(FakeCollector4):
        _fact_ids = ['baz']

    class FakeCollector6(FakeCollector5):
        _fact_ids = ['baz']

    collectors = [FakeCollector1, FakeCollector2, FakeCollector3,
                  FakeCollector4, FakeCollector5, FakeCollector6]

    fact_id

# Generated at 2022-06-13 00:30:21.577113
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():

    from ansible_collections.notstdlib.moveitallout.plugins.module_utils.facts import collectors

    all_collector_classes = list(collectors.get_collector_classes())

    fact_id_to_collector_map, aliases_map = build_fact_id_to_collector_map(all_collector_classes)

    assert len(fact_id_to_collector_map) == len(all_collector_classes)

    for collector_class in all_collector_classes:
        assert collector_class in fact_id_to_collector_map[collector_class.name]

    # each fact_id_to_collector_map item should be a list, containing one or more collectors

# Generated at 2022-06-13 00:30:32.965141
# Unit test for function get_collector_names
def test_get_collector_names():
    assert get_collector_names(gather_subset=['all'],
                               valid_subsets=frozenset(
                                   ['foo', 'bar', 'baz'])) == frozenset(
                                       ['foo', 'bar', 'baz'])
    assert get_collector_names(gather_subset=['foo'],
                               aliases_map={'foo': ['bar', 'baz']},
                               valid_subsets=frozenset(['bar', 'baz'])) == frozenset(
                                   ['bar', 'baz'])
    assert get_collector_names(
        gather_subset=['!foo'],
        aliases_map={'foo': ['bar', 'baz']},
        valid_subsets=frozenset(['bar', 'baz']))

# Generated at 2022-06-13 00:30:42.678442
# Unit test for function find_collectors_for_platform
def test_find_collectors_for_platform():

    class Collector1(BaseFactCollector):
        _fact_ids = "C1_F1,C1_F2".split(',')
        name = 'C1'
        required_facts = "C1_F1,C1_F2".split(',')

        @classmethod
        def platform_match(cls, platform_info):
            if platform_info.get('system', None) == cls._platform:
                return cls
            return None

    class Collector2(BaseFactCollector):
        _fact_ids = "C2_F1,C2_F2".split(',')
        name = 'C2'
        required_facts = "C2_F2,C2_F3".split(',')


# Generated at 2022-06-13 00:30:47.375711
# Unit test for function build_dep_data
def test_build_dep_data():
    all_fact_subsets = {'A': [1, 2], 'B': [3], 'C': [4, 5]}
    expected = {'A': {'B', 'C'}, 'B': set(), 'C': set()}
    class A:
        required_facts = {'B', 'C'}
    class B:
        required_facts = set()
    class C:
        required_facts = set()

    collector_names = ['A', 'B', 'C']
    assert build_dep_data(collector_names, all_fact_subsets) == expected

# Generated at 2022-06-13 00:30:56.504586
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    from . import network

    collector_names = frozenset([
        'network'
    ])

    all_fact_subsets = {
        'network': [network.NetworkFactCollector]
    }

    unresolved = find_unresolved_requires(collector_names, all_fact_subsets)
    assert len(unresolved) == 0, 'there should be no unresolved requires'

    collector_names = frozenset([
        # 'ohai'
    ])

    unresolved = find_unresolved_requires(collector_names, all_fact_subsets)
    assert len(unresolved) == 1, 'there should be 1 unresolved requires'

    assert 'ohai' in unresolved, 'it should be the ohai collector'



# Generated at 2022-06-13 00:31:08.068567
# Unit test for function build_dep_data
def test_build_dep_data():
    from ansible.module_utils.facts.platform.linux import Linux, Debian, Oracle, Ubuntu, RedHat, Alpine, Suse, OpenSuse, Fedora
    dep_map = build_dep_data(['RedHat', 'Debian', 'Oracle', 'Ubuntu', 'Alpine', 'Suse', 'OpenSuse', 'Fedora', 'Linux'], {'RedHat': [RedHat], 'Debian': [Debian], 'Oracle': [Oracle], 'Ubuntu': [Ubuntu], 'Alpine': [Alpine], 'Suse': [Suse], 'OpenSuse': [OpenSuse], 'Fedora': [Fedora], 'Linux': [Linux]})

# Generated at 2022-06-13 00:31:15.815637
# Unit test for function build_dep_data
def test_build_dep_data():
    class TestDepA(BaseFactCollector):
        name = 'a'
        def collect(self, module=None, collected_facts=None):
            return {'a': '1'}
    class TestDepB(BaseFactCollector):
        name = 'b'
        required_facts = set(['a'])
        def collect(self, module=None, collected_facts=None):
            return {'b': '1'}
    class TestDepC(BaseFactCollector):
        name = 'c'
        required_facts = set(['b'])
        def collect(self, module=None, collected_facts=None):
            return {'c': '1'}
    class TestDepD(BaseFactCollector):
        name = 'd'
        required_facts = set(['e'])

# Generated at 2022-06-13 00:31:25.876367
# Unit test for function find_collectors_for_platform
def test_find_collectors_for_platform():

    class CollectorA(BaseFactCollector):
        _platform = 'Linux'
        name = 'a'

    class CollectorB(BaseFactCollector):
        _platform = 'Windows'
        name = 'b'

    class CollectorC(BaseFactCollector):
        _platform = 'BSD'
        name = 'c'

    class CollectorD(BaseFactCollector):
        name = 'd'

        def platform_match(self, platform_info):
            platform_system = platform_info.get('system', None)
            if platform_system == 'Linux' and platform_info.get('distribution', '').startswith('Arch'):
                return self

    # this is used because the various platform info
    # use different words for the same thing

# Generated at 2022-06-13 00:32:05.981109
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    from ansible.module_utils.facts import collection
    c0 = type('TestCollector0', (BaseFactCollector,),
              {'name': 'test_collector_0',
               '_fact_ids': {'test_fact_id_0', 'test_collector_0'}})
    c1 = type('TestCollector1', (BaseFactCollector,),
              {'name': 'test_collector_1',
               '_fact_ids': {'test_fact_id_1', 'test_alias1_1'}})
    c2 = type('TestCollector2', (BaseFactCollector,),
              {'name': 'test_collector_2',
               '_fact_ids': {'test_fact_id_2', 'test_alias2_2'}})
    f_

# Generated at 2022-06-13 00:32:16.113504
# Unit test for function get_collector_names
def test_get_collector_names():
    import pytest
    valid_subsets = frozenset(['subset1', 'subset2', 'subset3'])
    minimal_gather_subset = frozenset(['subset3'])
    aliases_map = defaultdict(set)
    aliases_map['subset2'].update(['subset1', 'subset3'])

    def assert_valid_subsets(subsets):
        for subset in subsets:
            assert subset in valid_subsets, 'subset %s is not in valid_subsets' % subset

    # all
    # no aliases
    assert_valid_subsets(get_collector_names(valid_subsets=valid_subsets, aliases_map=aliases_map, gather_subset=[]))

# Generated at 2022-06-13 00:32:25.811304
# Unit test for function find_collectors_for_platform
def test_find_collectors_for_platform():
    from ansible.module_utils.facts import collector


# Generated at 2022-06-13 00:32:35.915174
# Unit test for function get_collector_names
def test_get_collector_names():
    aliases = {
        'hardware': ['devices', 'dmi'],
    }

    aliases_map = defaultdict(set)
    for base, aliases_list in aliases.items():
        for alias in aliases_list:
            aliases_map[alias].add(base)

    # test valid subsets
    valid_subsets = frozenset(['foo', 'bar', 'hardware'])

    # test everything excluded
    assert not get_collector_names(valid_subsets=valid_subsets,
                                   gather_subset=['!']) - set(['min'])

    # test negation
    expected = set(['foo', 'bar']) - {'hardware'}

# Generated at 2022-06-13 00:32:45.226933
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    required_facts_override = {
        'foo': ['bar'],
        'bar': ['baz'],
    }

    class Collector:
        def __init__(self, name, required_facts):
            self.name = name
            self.required_facts = required_facts

        @property
        def required_facts(self):
            return required_facts_override.get(self.name, [])

    all_fact_subsets = {
        'foo': [Collector('foo', ['bar'])],
        'bar': [Collector('bar', ['baz'])],
        'baz': [Collector('baz', [])],
        'quux': [Collector('quux', ['foo', 'bar'])],
    }

    collector_names = ['foo', 'bar', 'baz']

# Generated at 2022-06-13 00:32:56.627739
# Unit test for function find_collectors_for_platform
def test_find_collectors_for_platform():
    from ansible.module_utils.facts import collectors

    platform_info = {'system': 'Linux'}
    all_collector_classes = [collectors.LinuxCollector]

    found_collectors = find_collectors_for_platform(all_collector_classes, [platform_info])
    assert found_collectors == set(all_collector_classes)

    platform_info = {'system': 'Darwin'}
    all_collector_classes = [collectors.LinuxCollector, collectors.DarwinCollector]

    found_collectors = find_collectors_for_platform(all_collector_classes, [platform_info])
    assert found_collectors == {collectors.DarwinCollector}

    platform_info = {'system': 'Darwin'}

# Generated at 2022-06-13 00:33:00.702653
# Unit test for function build_dep_data
def test_build_dep_data():
    all_fact_subsets = {'a': [object()], 'b': [object()]}
    assert build_dep_data(['a', 'b'], all_fact_subsets) == {
        'a': set(),
        'b': set()
    }



# Generated at 2022-06-13 00:33:11.331920
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    class FactCollector_A(BaseFactCollector):
        _fact_ids = {
            'all_facts',
        }
        name = 'A'

    class FactCollector_B(BaseFactCollector):
        _fact_ids = {
            'B',
            'all_facts',
        }
        name = 'B'

    class FactCollector_C(BaseFactCollector):
        _fact_ids = {
            'C',
            'all_facts',
            'alias_for_B',
        }
        name = 'C'

    class FactCollector_D(BaseFactCollector):
        _fact_ids = {
            'D',
            'alias_for_A',
        }
        name = 'D'

    class FactCollector_E(BaseFactCollector):
        _fact

# Generated at 2022-06-13 00:33:19.025829
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    all_fact_subsets = {'a': [object()],
                        'b': [object()]}

    assert find_unresolved_requires(['a'], all_fact_subsets) == set()
    assert find_unresolved_requires(['a', 'b', 'c'], all_fact_subsets) == set(['c'])
    assert find_unresolved_requires(['a', 'b', 'c'], {'a': [object(required_facts=('b', 'c'))]}) == set()


# Generated at 2022-06-13 00:33:30.628002
# Unit test for function build_fact_id_to_collector_map

# Generated at 2022-06-13 00:34:04.205421
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    class FooFactClass1(BaseFactCollector):
        _fact_ids = ('foo1',)
        required_facts = ('bar1',)

    class BarFactClass(BaseFactCollector):
        _fact_ids = ('bar1',)
        required_facts = ()

    collector_names = ('foo1', 'bar1')
    all_fact_subsets = defaultdict(list)
    all_fact_subsets['foo1'].append(FooFactClass1)
    all_fact_subsets['bar1'].append(BarFactClass)
    assert find_unresolved_requires(collector_names, all_fact_subsets) == set()

    collector_names = ('foo1',)