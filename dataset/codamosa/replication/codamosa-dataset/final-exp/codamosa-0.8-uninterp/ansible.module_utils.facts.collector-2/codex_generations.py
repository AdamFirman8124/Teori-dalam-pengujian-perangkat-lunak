

# Generated at 2022-06-13 00:24:28.757416
# Unit test for function get_collector_names
def test_get_collector_names():
    sets = {
        "all": frozenset(("a", "b")),
        "other": frozenset(("b", "c")),
        "min": frozenset(("a", "b")),
    }

# Generated at 2022-06-13 00:24:35.171282
# Unit test for function build_dep_data
def test_build_dep_data():
    from ansible.module_utils.facts.collectors import network, virtual
    collector_classes = [network.DefaultNetwork, network.Network, network.DefaultAllNetwork, network.AllNetwork]
    collector_names = [collector_class.name for collector_class in collector_classes]
    all_fact_subsets = {collector_class.name: [collector_class] for collector_class in collector_classes}
    dep_map = build_dep_data(collector_names, all_fact_subsets)
    assert dep_map['all_network'] == set(['network', 'default_network'])



# Generated at 2022-06-13 00:24:44.591201
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    from ansible.module_utils.facts.collector.system.distribution import DistributionFactCollector
    from ansible.module_utils.facts.collector.network.base import NetworkCollector

    fact_id_to_collector_map = defaultdict(list)
    aliases_map = defaultdict(set)
    collectors_for_platform = set([DistributionFactCollector, NetworkCollector])
    fact_id_to_collector_map, aliases_map = build_fact_id_to_collector_map(collectors_for_platform)
    assert fact_id_to_collector_map['distribution'][0] == DistributionFactCollector
    assert fact_id_to_collector_map['distribution'][1] == NetworkCollector
    assert fact_id_to_collector_map['network'][0]

# Generated at 2022-06-13 00:24:55.534339
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    class test_impl(BaseFactCollector):
        _fact_ids = frozenset(['a', 'b'])
        name = 'primary'

    fact_id_to_collector_map, aliases_map = build_fact_id_to_collector_map([test_impl])

    assert 'primary' in fact_id_to_collector_map
    assert 'a' in fact_id_to_collector_map
    assert 'b' in fact_id_to_collector_map

    assert 'primary' in aliases_map
    assert 'a' not in aliases_map
    assert 'b' not in aliases_map

    assert 'primary' in aliases_map['primary']
    assert 'a' in aliases_map['primary']
    assert 'b' in aliases_map['primary']



# Generated at 2022-06-13 00:25:02.123922
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    from ansible.module_utils.facts.collector.hostname import HostnameFactCollector
    from ansible.module_utils.facts.collector.system import SystemFactCollector
    from ansible.module_utils.facts.collector.distribution import DistributionFactCollector
    from ansible.module_utils.facts.collector.virtual.openbsd import OpenBSDVirtualFactCollector
    from ansible.module_utils.facts.collector.virtual.freebsd import FreeBSDVirtualFactCollector
    from ansible.module_utils.facts.collector.virtual.netbsd import NetBSDVirtualFactCollector
    from ansible.module_utils.facts.collector.virtual.openbsd import OpenBSDVirtualFactCollector
    from ansible.module_utils.facts.collector.virtual.openvms import OpenVMSVirtualFactCollect

# Generated at 2022-06-13 00:25:10.104172
# Unit test for function find_collectors_for_platform
def test_find_collectors_for_platform():
    ''' unit test for find_collectors_for_platform

        This test is a bit brittle, which is why it is not a formal unit test.
        A better test would be to start up a Linux and Windows env and check the results
        there.

        This test does test:
        * a linux platform with a linux and a generic collector, the linux should win
        * a fake platform with no collectors and a generic collector, generic should win
        * a platform with multiple linux collectors, only one wins
        * a platform with a linux collector that matches a generic collector, linux should be in the list
    '''
    import ansible.module_utils.facts.collector.generic

    class CollectorA(BaseFactCollector):
        _platform = 'Linux'
        name = 'A'

    class CollectorB(BaseFactCollector):
        _platform = 'Linux'


# Generated at 2022-06-13 00:25:20.321395
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():

    class Collector1:
        required_facts = set(['collector2'])
    class Collector2:
        required_facts = set(['collector3'])
    class Collector3:
        required_facts = set()

    all_fact_subsets = {
        'collector1': [Collector1],
        'collector2': [Collector2],
        'collector3': [Collector3],
    }

    collector_names = ['collector1']
    assert find_unresolved_requires(collector_names, all_fact_subsets) == set(['collector2', 'collector3'])

    collector_names = ['collector1', 'collector2']
    assert find_unresolved_requires(collector_names, all_fact_subsets) == set(['collector3'])



# Generated at 2022-06-13 00:25:29.492591
# Unit test for function find_collectors_for_platform
def test_find_collectors_for_platform():
    all_collector_classes = [
        FakeFactCollector_Linux,
        FakeFactCollector_Windows,
        FakeFactCollector_Generic,
        FakeFactCollector_GenericWithName,
    ]

    # match linux if the system is Linux
    compat_platforms = [{'system': 'Linux'}]
    collectors = find_collectors_for_platform(all_collector_classes, compat_platforms)
    assert len(collectors) == 1
    assert FakeFactCollector_Linux in collectors

    # match linux if the system is Linux
    compat_platforms = [{'system': 'Linux'}, {'system': 'Generic'}]
    collectors = find_collectors_for_platform(all_collector_classes, compat_platforms)
    assert len(collectors) == 1
    assert FakeFactCollect

# Generated at 2022-06-13 00:25:41.031571
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    all_fact_subsets = defaultdict(list)
    all_fact_subsets['a'].append(type(
        'a_collector_class',
        (object, ),
        {
            '_fact_ids': {'a', 'a1'},
            'name': 'a',
            'required_facts': {'b', 'c'}
        }
    ))
    all_fact_subsets['b'].append(type(
        'b_collector_class',
        (object, ),
        {
            '_fact_ids': {'b', 'b1'},
            'name': 'b',
            'required_facts': {'c'}
        }
    ))

# Generated at 2022-06-13 00:25:45.804257
# Unit test for function get_collector_names
def test_get_collector_names():
    gather_subset = ['all']
    minimal_gather_subset = ('minimal',)
    valid_subsets = ('minimal', 'all', 'hardware', 'network')

    additional_subsets = get_collector_names(valid_subsets, minimal_gather_subset, gather_subset)
    assert additional_subsets == set(('minimal', 'all', 'hardware', 'network'))


# Generated at 2022-06-13 00:26:07.883583
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    from ansible.module_utils.facts.system.distribution import DistributionFactCollector
    from ansible.module_utils.facts.system.platform import PlatformFactCollector
    from ansible.module_utils.facts.system.system import SystemFactCollector
    from ansible.module_utils.facts.virtual.docker import DockerFactCollector
    from ansible.module_utils.facts.virtual.kubelet import KubeletFactCollector
    from ansible.module_utils.facts.virtual.lxc import LXCFactCollector
    from ansible.module_utils.facts.virtual.openvz import OpenVZFactCollector
    from ansible.module_utils.facts.virtual.systemd import SystemdFactCollector
    from ansible.module_utils.facts.virtual.zlinux import ZLinuxFactCollector

# Generated at 2022-06-13 00:26:18.902103
# Unit test for function find_collectors_for_platform
def test_find_collectors_for_platform():
    import unittest
    import sys

    compat_platforms = [
        {'system': 'Linux'},
        {'system': 'FreeBSD'},
        {'system': 'NetBSD'},
        {'system': 'OpenBSD'},
        {'system': 'SunOS'},
        {'system': 'Windows'}
        ]

    all_collector_classes = [FakeLinuxCollector, FakeFreeBSDCollector,
                             FakeNetBSDCollector, FakeOpenBSDCollector,
                             FakeSunOSCollector, FakeGenericCollector]

    found_collectors = find_collectors_for_platform(all_collector_classes, compat_platforms)

    # Each platform should match to its own collector (plus both generic)
    if sys.version_info[0] == 2:
        assert found_collectors

# Generated at 2022-06-13 00:26:25.962915
# Unit test for function get_collector_names
def test_get_collector_names():
    from ansible_collections.ansible.community.plugins.module_utils.facts import collector_classes

    collector_classes = [x for x in collector_classes if x.name]
    valid_subsets = set([x.name for x in collector_classes])

    aliases = defaultdict(set)
    for collector_class in collector_classes:
        aliases[collector_class.name].add(collector_class.name)
        for alias in collector_class.aliases:
            aliases[alias].add(collector_class.name)

    platform_info = {'system': 'Linux'}


# Generated at 2022-06-13 00:26:37.376352
# Unit test for function get_collector_names
def test_get_collector_names():
    valid_subsets = frozenset({'all', 'network', 'hardware', 'dmi', 'interfaces', 'devices'})
    minimal_gather_subset = frozenset({'network'})

    assert get_collector_names(valid_subsets, minimal_gather_subset) == minimal_gather_subset
    assert get_collector_names(valid_subsets, minimal_gather_subset, ['network']) == minimal_gather_subset
    assert get_collector_names(valid_subsets, minimal_gather_subset, ['network', 'hardware']) == set(['network', 'hardware'])
    assert get_collector_names(valid_subsets, minimal_gather_subset, ['!network', 'hardware']) == set(['hardware'])


# Generated at 2022-06-13 00:26:43.801394
# Unit test for function build_dep_data
def test_build_dep_data():
    dep_map = {
              'first_name': set(),
              'second_name': set(['first_name']),
              'third_name': set(['first_name', 'second_name'])
            }
    names = ['first_name', 'second_name', 'third_name']
    all_fact_subsets = build_dep_data(names, None)
    assert dep_map == all_fact_subsets



# Generated at 2022-06-13 00:26:53.168389
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    from ansible_collections.community.general.plugins.module_utils.facts import test_collector
    all_fact_subsets = {
        'a': [test_collector.CollectorA],
        'b': [test_collector.CollectorB],
        'c': [test_collector.CollectorC],
        'd': [test_collector.CollectorD],
        'e': [test_collector.CollectorE],
    }
    # test normal case
    assert find_unresolved_requires(['a'], all_fact_subsets) == set()
    assert find_unresolved_requires(['e'], all_fact_subsets) == {'c', 'd'}
    # test multi-class collector

# Generated at 2022-06-13 00:26:57.747108
# Unit test for function build_dep_data
def test_build_dep_data():
    collectors = {'collector1': {'required_facts': set(['dep1'])},
                  'collector2': {'required_facts': set(['dep2'])},
                  'collector3': {'required_facts': set(['dep1', 'dep2'])}}
    collector_names = set(collectors.keys())
    assert build_dep_data(collector_names, collectors) == {'collector1': {'dep1'},
                                                           'collector2': {'dep2'},
                                                           'collector3': {'dep1', 'dep2'}}



# Generated at 2022-06-13 00:27:05.204642
# Unit test for function get_collector_names
def test_get_collector_names():
    from ansible.module_utils.facts import aliases_map
    additional_subsets = get_collector_names(
        gather_subset=['network'],
        aliases_map=aliases_map,
    )
    assert additional_subsets == ['network']

    additional_subsets = get_collector_names(
        gather_subset=['network', 'network_resources'],
        aliases_map=aliases_map,
    )
    assert additional_subsets == ['network', 'network_resources']

    additional_subsets = get_collector_names(
        gather_subset=['network', '!network_resources'],
        aliases_map=aliases_map,
    )
    assert additional_subsets == ['network']



# Generated at 2022-06-13 00:27:12.666508
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    class NetworkCollector(BaseFactCollector):
        name = 'network'
        _fact_ids = {'network'}
    class RoutingCollector(BaseFactCollector):
        name = 'routing'
        _fact_ids = {'route'}
    class TestCollector(RoutingCollector):
        name = 'test'
        _fact_ids = {'test_info'}

    collectors_for_platform = [NetworkCollector, RoutingCollector, TestCollector]
    fact_id_to_collector_map, aliases_map = build_fact_id_to_collector_map(collectors_for_platform)
    assert fact_id_to_collector_map['network'] == [NetworkCollector]

# Generated at 2022-06-13 00:27:23.831320
# Unit test for function tsort
def test_tsort():
    # DAG
    sorted_list = tsort(
        {
            'a': set(['b']),
            'b': set(['c']),
            'c': set(['d']),
            'd': set(),
        })
    assert len(sorted_list) == 4
    assert sorted_list == [('d', set()), ('c', set(['d'])), ('b', set(['c'])), ('a', set(['b']))]

    # cycle
    try:
        tsort(
            {
                'a': set(['b']),
                'b': set(['c']),
                'c': set(['d']),
                'd': set(['a']),
            })
        assert False
    except CycleFoundInFactDeps:
        pass

    # non

# Generated at 2022-06-13 00:27:42.975396
# Unit test for function find_collectors_for_platform
def test_find_collectors_for_platform():
    platform_info = {'system': 'linux'}
    platform_info2 = {'system': 'Illumos'}

    class CollectorLinux(BaseFactCollector):
        _fact_ids = set()
        _platform = 'linux'
        name = 'collector_linux'
        required_facts = set()

    class CollectorIllumos(BaseFactCollector):
        _fact_ids = set()
        _platform = 'Illumos'
        name = 'collector_illumos'
        required_facts = set()

    class CollectorGeneric(BaseFactCollector):
        _fact_ids = set()
        _platform = 'generic'
        name = 'collector_generic'
        required_facts = set()

    collectors = [CollectorLinux, CollectorIllumos, CollectorGeneric]
    found_collectors = find

# Generated at 2022-06-13 00:27:50.744864
# Unit test for function build_dep_data
def test_build_dep_data():
    import unittest
    class FakeCollector(BaseFactCollector):
        name = 'fake_collector'
        required_facts = set()

    collector_names = ['fake_collector']
    all_fact_subsets = {'fake_collector': [FakeCollector]}

    dep_map = build_dep_data(collector_names, all_fact_subsets)
    expected_dep_map = {'fake_collector': set()}
    unittest.TestCase().assertEqual(dep_map, expected_dep_map)



# Generated at 2022-06-13 00:27:58.363171
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    import ansible.module_utils.facts.collector.base
    import ansible.module_utils.facts.collector.bsd
    import ansible.module_utils.facts.collector.linux
    import ansible.module_utils.facts.collector.network
    import ansible.module_utils.facts.collector.service
    import ansible.module_utils.facts.collector.sunos
    import ansible.module_utils.facts.collector.system
    import ansible.module_utils.facts.collector.virtual


# Generated at 2022-06-13 00:28:05.306126
# Unit test for function find_collectors_for_platform
def test_find_collectors_for_platform():
    # these are where we store the test data.
    # TODO: Can we make this parameterized so we can loop over different
    #       sets of test data?

    # in this test all classes are 'Linux' so we can just test the
    # results of that platform
    all_collectors = {
        'Foo': {'name': 'Foo',
                '_platform': 'Linux'},
        'Bar': {'name': 'Bar',
                '_platform': 'Linux'},
        'Baz': {'name': 'Baz',
                '_platform': 'Linux'},
    }
    platform_infos = [
        {'system': 'Linux'},
    ]
    # targets are a list of expected results. They are tuples of:
    #  - expand_set: a set of expandable (all,

# Generated at 2022-06-13 00:28:16.276549
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    class dummy_collector():
        name = 'something'
        _fact_ids = set()

    class test_collector(dummy_collector):
        _fact_ids = set(['one', 'two'])

    class test_collector2(dummy_collector):
        _fact_ids = set()

    class test_collector3(dummy_collector):
        _fact_ids = set(['one', 'three'])

    class test_collector4(dummy_collector):
        _fact_ids = set(['four', 'five'])

    class test_collector5(dummy_collector):
        name = 'something else'
        _fact_ids = set(['six', 'seven'])


# Generated at 2022-06-13 00:28:26.019282
# Unit test for function find_collectors_for_platform
def test_find_collectors_for_platform():

    class AllCollectorClass(BaseFactCollector):

        @classmethod
        def platform_match(cls, platform_info):
            if 'system' in platform_info:
                if platform_info['system'] == cls._platform:
                    return True
                return False
            return False

    class Platform1(AllCollectorClass):
        _platform = 'Platform1'
        name = 'Platform1'

    class Platform2(AllCollectorClass):
        _platform = 'Platform2'
        name = 'Platform2'

    class Platform3(AllCollectorClass):
        _platform = 'Platform3'
        name = 'Platform3'

    all_collector_classes = [Platform1, Platform2, Platform3]

    def get_collectors(platform_info, found_makers=None):
        found_makers = found_makers

# Generated at 2022-06-13 00:28:37.999322
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    class A: required_facts = {'b', 'c'}
    class B: required_facts = {'d'}
    class C: required_facts = {'b', 'e'}
    class D: required_facts = {'f'}
    class E: required_facts = {'g'}

    all_fact_subsets = {'a': [A], 'b': [B], 'c': [C], 'd': [D], 'e': [E]}

    assert find_unresolved_requires({}, all_fact_subsets) == set()
    assert find_unresolved_requires({'q'}, all_fact_subsets) == {'q'}
    assert find_unresolved_requires({'a'}, all_fact_subsets) == {'b', 'c'}

# Generated at 2022-06-13 00:28:49.387381
# Unit test for function find_collectors_for_platform
def test_find_collectors_for_platform():
    # test class
    class TestAllCollectorClasses(BaseFactCollector):
        _platform = 'Generic'
        name = 'generic_platform'
        required_facts = set()

    # create compat_platforms
    compat_platforms = [{'system': 'Generic'}]

    # create all_collector_classes
    all_collector_classes = [TestAllCollectorClasses]

    # check for valid class
    output = find_collectors_for_platform(all_collector_classes, compat_platforms)
    if output != set([TestAllCollectorClasses]):
        raise AssertionError('test_find_collectors_for_platform failed')

    # check for invalid class
    compat_platforms = [{'system': 'Generic1'}]
    output = find_collectors_for_

# Generated at 2022-06-13 00:28:58.639784
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    real_all_collector_classes = get_all_collector_classes()
    collectors_for_platform = find_collectors_for_platform(real_all_collector_classes, [ platform.system_alias(platform.system(), platform.release(), platform.version()) ])

    fact_id_to_collector_map, aliases_map = build_fact_id_to_collector_map(collectors_for_platform)

    # NOTE: this test only cares about the number of values for the dict keys because
    #       it is an internal helper function that get_collector_classes() relies upon
    #       to build the returned dict of fact_id_to_collector_map.
    #
    #       Only counting the number of values for each dict key is a simple and
    #       conservative way to ensure that get_collector_classes()

# Generated at 2022-06-13 00:29:07.596708
# Unit test for function find_collectors_for_platform
def test_find_collectors_for_platform():
    from ansible.module_utils.facts import collector

    class TestFact1(BaseFactCollector):
        name = 'test1'
        _platform = 'Generic'

    class TestFact2(BaseFactCollector):
        name = 'test2'
        _platform = 'TestOS'

    class TestFact3(BaseFactCollector):
        name = 'test3'
        _platform = 'Generic'

    all_collector_classes = [TestFact1, TestFact2, TestFact3]
    compat_platforms = [{'system': 'Generic'}, {'system': 'TestOS'}]

    assert set([TestFact1, TestFact2, TestFact3]) == find_collectors_for_platform(all_collector_classes, compat_platforms)



# Generated at 2022-06-13 00:29:27.074532
# Unit test for function build_dep_data
def test_build_dep_data():
    from ansible.module_utils.facts import collector
    reqs = {'collectors.d': {'linux.collectors': []}}
    _, all_fact_subsets, all_collector_classes = collector.collector_classes(reqs, [])
    collector_names = ['all', 'min']
    fact_ids = set()
    fact_ids.update(collector_names)
    for collector_class in all_collector_classes:
        fact_ids.update(collector_class._fact_ids)
    collector_names = list(fact_ids)
    dep_map = build_dep_data(collector_names, all_fact_subsets)
    collector_names.remove('min')

# Generated at 2022-06-13 00:29:38.849974
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    from ansible_collections.notstdlib.moveitallout.plugins.module_utils.facts.collector import BaseFactCollector
    from ansible_collections.notstdlib.moveitallout.plugins.module_utils.facts.collector import get_collector_names

    all_fact_subsets = defaultdict(list)

    class A(BaseFactCollector):
        name = 'A'
        required_facts = set()

    class B(BaseFactCollector):
        name = 'B'
        required_facts = {'A'}

    class C(BaseFactCollector):
        name = 'C'
        required_facts = {'B'}

    all_fact_subsets['A'].append(A)
    all_fact_subsets['B'].append(B)
    all_fact

# Generated at 2022-06-13 00:29:45.953062
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    class DummyCollector(BaseFactCollector):
        _fact_ids = ('dummy', 'dummy_primary')
        name = 'dummy_primary'
        required_facts = set()

    assert build_fact_id_to_collector_map([DummyCollector]) == ({
        'dummy': [DummyCollector],
        'dummy_primary': [DummyCollector],
    }, {'dummy_primary': {'dummy', 'dummy_primary'}})



# Generated at 2022-06-13 00:29:57.249070
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    class TestCollector1(BaseFactCollector):
        _fact_ids = set(['dep_collector_a', 'dep_collector_b'])

        name = 'test_collector_1'
        required_facts = set()

    class TestCollector2(BaseFactCollector):
        _fact_ids = set(['dep_collector_a', 'dep_collector_b'])

        name = 'test_collector_2'
        required_facts = set()

    class TestCollector3(BaseFactCollector):
        name = 'test_collector_3'
        required_facts = set(['test_collector_2'])

    class TestCollector4(BaseFactCollector):
        _fact_ids = set(['dep_collector_b'])


# Generated at 2022-06-13 00:30:02.838060
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    import pytest
    from ansible.module_utils._text import to_native

    class DummyCollector1:
        required_facts = set()

    class DummyCollector2:
        required_facts = {'fact1'}

    class DummyCollector3:
        required_facts = {'fact1', 'fact2'}

    class DummyCollector4:
        required_facts = {'badfact'}

    class DummyCollector5:
        required_facts = {'fact1', 'fact2', 'loop3'}


# Generated at 2022-06-13 00:30:07.200511
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():

    class TestCollector1(BaseFactCollector):
        name = 'test1'
        _fact_ids = {'test1_id_1', 'test1_id_2', 'test1_id_3'}

    class TestCollector2(BaseFactCollector):
        name = 'test2'
        _fact_ids = {'test2_id_1', 'test2_id_2', 'test2_id_3'}

    class TestCollector3(BaseFactCollector):
        name = 'test3'
        _fact_ids = {'test3_id_1', 'test3_id_2', 'test3_id_3'}

    # this is the end-to-end test, as if called from ModuleBase
    fact_id_to_collector_map, aliases_map = build_

# Generated at 2022-06-13 00:30:18.325689
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.network.base import NetworkCollector

    class RequiresB(BaseFactCollector):
        _fact_ids = (
            'b',
            'c',
        )
        required_facts = (
            'b',
        )
    class RequiresC(BaseFactCollector):
        _fact_ids = (
            'c',
        )
        required_facts = (
            'c',
        )
    class RequiresBAndC(BaseFactCollector):
        _fact_ids = (
            'b_and_c',
        )
        required_facts = (
            'b',
            'c',
        )


# Generated at 2022-06-13 00:30:22.325915
# Unit test for function build_dep_data
def test_build_dep_data():
    dep_map = build_dep_data(['software', 'os_family'], {'software': ['software'], 'os_family': ['os_family']})
    assert(dep_map == {'software': set(), 'os_family': set()})



# Generated at 2022-06-13 00:30:33.477502
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    the_map = {
        'foo': [object()],
        'bar': [object(), object()],
        'baz': [object()],
    }

    aliases_map = {
        'foo': ['foo', 'foo2'],
        'bar': ['bar', 'bar2', 'bar3'],
        'baz': ['baz', 'baz2'],
    }


    class FakeCollector(object):
        _fact_ids = ['foo', 'foo2']

        def __init__(self, name):
            self.name = name

    class AnotherFakeCollector(object):
        _fact_ids = ['bar', 'bar2', 'bar3']

        def __init__(self, name):
            self.name = name

    class YetAnotherFakeCollector(object):
        _fact_

# Generated at 2022-06-13 00:30:39.771077
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    all_fact_subsets = {'collector-a': ['collector_class'],
                        'collector-b': ['collector_class']}
    collector_names = ['collector-a', 'collector-b']

    class collector_class:
        required_facts = set(['foo'])

    assert find_unresolved_requires(collector_names, all_fact_subsets) == set(['foo'])

    collector_class.required_facts.clear()
    assert find_unresolved_requires(collector_names, all_fact_subsets) == set()



# Generated at 2022-06-13 00:30:57.305312
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    assert build_fact_id_to_collector_map([]) == ({}, defaultdict(set))

    class test1(BaseFactCollector):
        _fact_ids = set(['test1id'])
        name = 'test1'

    class test2(BaseFactCollector):
        _fact_ids = set(['test2id'])
        name = 'test2'

    class test3(BaseFactCollector):
        _fact_ids = set(['test3id'])
        name = 'test3'

    class test4(BaseFactCollector):
        _fact_ids = set(['test4id'])
        name = 'test4'

    class test5(BaseFactCollector):
        _fact_ids = set(['test5id'])
        name = 'test5'


# Generated at 2022-06-13 00:31:06.149037
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    from ansible.module_utils.facts.collector.generic import GenericFactCollector
    from ansible.module_utils.facts.collector.hardware.base import HardwareFactCollector
    from ansible.module_utils.facts.collector.network.base import NetworkFactCollector

    collectors = [GenericFactCollector, HardwareFactCollector, NetworkFactCollector]
    _, aliases_map = build_fact_id_to_collector_map(collectors)

    assert aliases_map['network'] == {'local', 'interfaces', 'devices'}



# Generated at 2022-06-13 00:31:14.500712
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():

    # test class for testing_build_fact_id_to_collector_map
    class TestCollector1(BaseFactCollector):
        _platform = 'Linux'
        name = 'test_collector_a'
        _fact_ids = set(['test_fact_a', 'test_fact_b'])

        def collect(self, module=None, collected_facts=None):
            return {'test_fact_a': 'a', 'test_fact_b': 'b'}

    # test class for testing_build_fact_id_to_collector_map
    class TestCollector2(BaseFactCollector):
        _platform = 'Linux'
        name = 'test_collector_b'
        _fact_ids = set(['test_fact_a', 'test_fact_c'])


# Generated at 2022-06-13 00:31:24.715754
# Unit test for function build_dep_data
def test_build_dep_data():
    dep_map = build_dep_data(('collector1', 'collector2', 'collector3', 'collector4'),
                             {'collector1': ['dep1', 'dep2'],
                              'collector2': ['dep3'],
                              'collector3': ['collector2', 'collector4'],
                              'collector4': []})
    assert dep_map == {'collector1': {'dep1', 'dep2'},
                       'collector2': {'dep3'},
                       'collector3': {'collector2', 'collector4'},
                       'collector4': set()}
    assert not dep_map['collector4']
    assert dep_map['collector1'] and dep_map['collector2'] and dep_map['collector3']




# Generated at 2022-06-13 00:31:32.035173
# Unit test for function find_collectors_for_platform
def test_find_collectors_for_platform():
    fake_collector = {
        '_platform': 'FakeOS',
        'name': 'fake',
        'required_facts': set(),
    }
    all_collector_classes = [fake_collector]
    compat_platforms = [{'system': 'FakeOS'}]
    assert find_collectors_for_platform(all_collector_classes, compat_platforms) == set([fake_collector])

    all_collector_classes = [fake_collector]
    compat_platforms = [{'system': 'OtherOS'}]
    assert find_collectors_for_platform(all_collector_classes, compat_platforms) == set()



# Generated at 2022-06-13 00:31:44.145786
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    class A(BaseFactCollector):
        _fact_ids = set(['Foo', 'Bar'])
        name = 'A'
    class B(BaseFactCollector):
        _fact_ids = set(['Foo', 'Bar'])
        name = 'B'

    all_collectors = [A, B]

    fact_id_to_collector_map, aliases_map = build_fact_id_to_collector_map(all_collectors)

    assert fact_id_to_collector_map['A'] == [A]
    assert fact_id_to_collector_map['Foo'] == [A, B]

    assert aliases_map['A'] == set(['Foo', 'Bar'])
    assert aliases_map['B'] == set(['Foo', 'Bar'])




# Generated at 2022-06-13 00:31:55.555621
# Unit test for function find_collectors_for_platform
def test_find_collectors_for_platform():

    from ansible.module_utils.facts.hardware import Hardware
    from ansible.module_utils.facts.virtual import Virtual

    system_to_test = platform.system()
    platform_info = {'system': system_to_test}
    compat_platforms = [platform_info]

    # Register all the default classes
    collector_classes = [Hardware, Virtual]
    collector_classes_by_name = {klass.name: klass for klass in collector_classes}

    # Find the collectors that match the supplied platform
    found_collectors = find_collectors_for_platform(collector_classes, compat_platforms)
    assert len(found_collectors) == 1

    # For each class, try to instantiate them
    for found_collector_class in found_collectors:
        collector = found_collector

# Generated at 2022-06-13 00:32:05.904001
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    import pytest
    from ansible.module_utils.facts.namespace import BaseFactNamespace
    from ansible.module_utils.facts.core import BaseFactCollector

    class FakeCollectorA(BaseFactCollector):
        name = 'a'
        required_facts = set('b')

    class FakeCollectorB(BaseFactCollector):
        name = 'b'
        required_facts = set()

    class FakeCollectorC(BaseFactCollector):
        name = 'c'
        required_facts = set('d')

    all_fact_subsets = {
        'a': (FakeCollectorA, ),
        'b': (FakeCollectorB, ),
        'c': (FakeCollectorC, ),
    }

    with pytest.raises(CollectorNotFoundError):
        assert find_un

# Generated at 2022-06-13 00:32:16.052601
# Unit test for function build_dep_data
def test_build_dep_data():
    dep_map = {
        'hardware': set(),
        'interface': {'hardware', 'system'},
        'network': set(),
        'cmdline': {'system'},
        'system': set(),
        'facter': set(),
        'ohai': set(),
        'augeas': set(),
        'virtual': {'system'},
        'puppet': set(),
        'salt': {'system'},
        'hoe': set()
    }
    collector_names = list(dep_map)

# Generated at 2022-06-13 00:32:25.742064
# Unit test for function find_collectors_for_platform
def test_find_collectors_for_platform():
    '''Unit test for function find_collectors_for_platform'''

# Generated at 2022-06-13 00:33:31.544735
# Unit test for function get_collector_names
def test_get_collector_names():
    assert get_collector_names(
        valid_subsets=frozenset({'network'}),
        minimal_gather_subset=frozenset({'min'}),
        gather_subset=['all'],
        aliases_map=defaultdict(set),
        platform_info=None,
    ) == frozenset({'network'})

    assert get_collector_names(
        valid_subsets=frozenset({'network'}),
        minimal_gather_subset=frozenset({'min'}),
        gather_subset=['network'],
        aliases_map=defaultdict(set),
        platform_info=None,
    ) == frozenset({'network'})


# Generated at 2022-06-13 00:33:42.674001
# Unit test for function build_dep_data
def test_build_dep_data():
    # Let the collector_names be a,b,c,d,e and all_fact_subsets be [a->[b,c], b->[d,e], c->[d], d->[], e->[]] 
    collector_names = 'abcde'
    all_fact_subsets = {'a':{'b','c'}, 'b':{'d','e'}, 'c':{'d'}, 'd':set(), 'e':set()}
    dep_map = build_dep_data(collector_names,all_fact_subsets)
    assert dep_map['a'] == {'b','c'}
    assert dep_map['b'] == {'d','e'}
    assert dep_map['c'] == {'d'}
    assert dep_map['d'] == set()


# Generated at 2022-06-13 00:33:53.087936
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    # GIVEN:
    #     all_fact_subset = {
    #         'collector-a': [collector_a],
    #         'collector-b': [collector_b],
    #         'collector-c': [collector_c],
    #         'collector-d': [collector_d]
    #     }

    #     where collector_a.requires_facts = [collector-b]
    #     where collector_b.requires_facts = [collector-c]
    #     where collector_c.requires_facts = [collector-d]

    #     and collector_b.required_facts = [collector-d]

    def _make_collector(name, requires_facts, required_facts=None):
        class Collector:
            name = name
            required_facts

# Generated at 2022-06-13 00:34:00.151275
# Unit test for function find_collectors_for_platform
def test_find_collectors_for_platform():
    compat_platforms = [
        {'system': 'Linux',
         'distribution': 'RedHat',
         'version': '7.2'},
        {'system': 'Linux',
         'distribution': 'RedHat'},
        {'system': 'Linux'},
        {},
    ]
    all_collector_classes = [
        CollectorBaseClass(None, None),
        CollectorBaseClass(None, {'system': 'Linux'}),
        CollectorBaseClass(None, {'system': 'Linux',
                                  'distribution': 'Ubuntu'}),
        CollectorBaseClass(None, {'system': 'Linux',
                                  'distribution': 'RedHat'}),
    ]
    found_collectors = find_collectors_for_platform(all_collector_classes, compat_platforms)


# Generated at 2022-06-13 00:34:08.362694
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    all_fact_subsets = {
        "a": (BaseFactCollector,),
        "b": (BaseFactCollector,),
        "c": (BaseFactCollector,),
        "d": (BaseFactCollector,),
    }

    # Set up a dummy BaseFactCollector 'a' that "requires" b and d
    BaseFactCollector._fact_ids = set(["b", "d"])

    # We can't collect "a" because "b" is not a known collector
    collector_names = set(["a"])
    unresolved = find_unresolved_requires(collector_names, all_fact_subsets)
    assert(unresolved == set(["b", "d"]))

    # But we can collect "a" if we also collect "b"