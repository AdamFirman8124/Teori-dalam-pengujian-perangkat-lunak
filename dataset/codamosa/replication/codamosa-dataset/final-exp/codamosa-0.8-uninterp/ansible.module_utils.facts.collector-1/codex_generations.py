

# Generated at 2022-06-13 00:24:30.916628
# Unit test for function collector_classes_from_gather_subset
def test_collector_classes_from_gather_subset():

    class CollectorA(BaseFactCollector):
        name = 'a'

    class CollectorB(BaseFactCollector):
        name = 'b'

    class CollectorC(BaseFactCollector):
        name = 'c'
        required_facts = frozenset(['a', 'b'])

    class CollectorD(BaseFactCollector):
        name = 'd'
        required_facts = frozenset(['c'])

    class CollectorE(BaseFactCollector):
        name = 'e'
        required_facts = frozenset(['c'])

    class CollectorF(BaseFactCollector):
        name = 'f'
        required_facts = frozenset(['d'])

    class CollectorG(BaseFactCollector):
        name = 'g'
        required_facts = frozenset(['f'])



# Generated at 2022-06-13 00:24:41.871983
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    class DummyCollector(BaseFactCollector):
        name = 'dummy'

    all_fact_subsets = {
        'dummy': [
            DummyCollector,
        ],
    }

    assert len(find_unresolved_requires(set(['dummy']), all_fact_subsets)) == 0
    assert len(find_unresolved_requires(set(['dummy', 'dummy_requires']), all_fact_subsets)) == 0

    DummyCollector.required_facts = {'dummy_requires'}
    assert len(find_unresolved_requires(set(['dummy']), all_fact_subsets)) == 1
    assert len(find_unresolved_requires(set(['dummy', 'dummy_requires']), all_fact_subsets)) == 0




# Generated at 2022-06-13 00:24:54.909890
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    '''Test cases for function find_unresolved_requires()'''
    import pytest

    def _stub_required_facts(cls):
        class _TestClass(cls):
            required_facts = set(['fact1', 'fact2', 'fact3'])
        return _TestClass

    all_fact_subsets = {
        'fact1': [_stub_required_facts(object), _stub_required_facts(object)],
        'fact2': [_stub_required_facts(object), _stub_required_facts(object)],
        'fact3': [_stub_required_facts(object), _stub_required_facts(object)],
    }

    # Test for no unresolved fact collector
    collector_names = ['fact1', 'fact2', 'fact3']
   

# Generated at 2022-06-13 00:25:01.104962
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    from ansible.module_utils.facts.collector.network import Network
    from ansible.module_utils.facts.collector.hardware import Hardware
    from ansible.module_utils.facts.collector.platform import Platform
    # TODO: test passing in some aliases

    class MyHardware(Hardware):
        name = 'myhardware'
        _fact_ids = set(['hardware', 'other'])

    collectors = [Network, Hardware, Platform, MyHardware]

    fact_id_to_collector_map, aliases_map = build_fact_id_to_collector_map(collectors)
    # we have all the fact_ids and names
    assert set(fact_id_to_collector_map.keys()) == set(['interface', 'hardware', 'network', 'other', 'platform'])
    #

# Generated at 2022-06-13 00:25:10.064639
# Unit test for function tsort

# Generated at 2022-06-13 00:25:20.287104
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    import ansible.module_utils.facts.collectors.linux.dns
    import ansible.module_utils.facts.collectors.linux.distribution

    collectors = [ansible.module_utils.facts.collectors.linux.dns.DnsCollector,
                  ansible.module_utils.facts.collectors.linux.distribution.DistributionCollector]

    fact_id_to_collector_map, _ = build_fact_id_to_collector_map(collectors)

    assert fact_id_to_collector_map['dns']
    assert fact_id_to_collector_map['dns'] == fact_id_to_collector_map['resolver']
    assert fact_id_to_collector_map['distribution']

# Generated at 2022-06-13 00:25:29.021043
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    from ansible.module_utils.facts import collector

    A_requires_C = {'A': {'required_facts': ['C']}, 'C': {'name': 'C'}}
    B_requires_A = {'B': {'required_facts': ['A']}, 'A': {'name': 'A'}}
    A_requires_C_B_requires_A = dict(A_requires_C, **B_requires_A)

    assert find_unresolved_requires(['A'], A_requires_C) == set(['C'])
    assert find_unresolved_requires(['B'], B_requires_A) == set(['A'])

# Generated at 2022-06-13 00:25:34.620285
# Unit test for function collector_classes_from_gather_subset
def test_collector_classes_from_gather_subset():
    # class to store _fact_ids and name
    class DummyCollector:
        _fact_ids = set()

        def __init__(self, name):
            self.name = name

    # create a dict of collector_classes
    collector_classes = {}
    for c_id in ('all', 'hardware', 'network', 'cmdline'):
        collector_classes[c_id] = DummyCollector(c_id)

    # alias hardware -> devices, dmi
    collector_classes['hardware']._fact_ids.update(['devices', 'dmi'])

    # alias network -> interfaces
    collector_classes['network']._fact_ids.update(['interfaces'])

    # alias all -> hardware, network

# Generated at 2022-06-13 00:25:44.446831
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    # create a fake collector class
    class FakeFactsCollector_1(BaseFactCollector):
        name = 'fake_facts_primary'
        _fact_ids = ['fake_fact_a', 'fake_fact_b']

    class FakeFactsCollector_2(BaseFactCollector):
        name = 'fake_facts_alternate'
        _fact_ids = ['fake_fact_c']
    # create a list of the fake collection classes
    test_collector_classes = [FakeFactsCollector_1, FakeFactsCollector_2]
    # build the fact_id_to_collector_map
    fact_id_to_collector_map, aliases_map = build_fact_id_to_collector_map(
        test_collector_classes)
    # results should be two distinct elements
   

# Generated at 2022-06-13 00:25:55.917027
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    assert find_unresolved_requires(set(), {}) == set()
    assert find_unresolved_requires(set(['a', 'b']), {}) == set()

    assert find_unresolved_requires(set(['b']), {'a': [object()]}) == set(['a'])

    assert find_unresolved_requires(set(['b']), {'a': [object()], 'b': [object()]}) == set(['a'])

    assert find_unresolved_requires(set(['a']), {'a': [object()], 'b': [object()]}) == set(['b'])


# Generated at 2022-06-13 00:26:18.563024
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    class Collector(BaseFactCollector):
        name = 'collector_no_req'
        required_facts = ()
        def collect(self):
            return {}

    class Collector1(BaseFactCollector):
        name = 'collector1'
        required_facts = ('collector_no_req',)
        def collect(self):
            return {}

    class Collector2(BaseFactCollector):
        name = 'collector2'
        required_facts = ('collector_no_req', 'collector1')
        def collect(self):
            return {}

    class Collector3(BaseFactCollector):
        name = 'collector3'
        required_facts = ('collector_nonexist',)
        def collect(self):
            return {}


# Generated at 2022-06-13 00:26:23.829653
# Unit test for function get_collector_names
def test_get_collector_names():
    # test the function get_collector_names
    aliases_map = defaultdict(set)
    aliases_map['hardware'] = set(['devices', 'dmi'])

    valid_subsets = frozenset(['hardware', 'devices', 'dmi', 'network', 'virtual'])
    minimal_gather_subset = frozenset(['devices'])

    # test option 'gather_subset = ['network']
    gather_subset = ['network']
    expected_names = set(['network'])
    collector_names = get_collector_names(valid_subsets, minimal_gather_subset,
                                          gather_subset, aliases_map)
    assert collector_names == expected_names

    # test option 'gather_subset = ['network', '!network']
    gather_sub

# Generated at 2022-06-13 00:26:33.850949
# Unit test for function build_dep_data
def test_build_dep_data():
    from ansible.module_utils.facts import collector

    collector_names = set()
    for value in collector.all_collectors_classes.values():
        collector_names.update(value)
    collector_names = list(collector_names)

    all_fact_subsets = collector.build_fact_id_to_collector_map(collector_names)

    dep_map = build_dep_data(collector_names, all_fact_subsets)

    assert dep_map.get('facter') == {'system', 'distribution', 'all_ipv4_addresses'}



# Generated at 2022-06-13 00:26:42.254202
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    collector_names = ['test_collector', 'test_collector_2']
    test_subsets = {
        'test_collector': [MockFactCollector('test_collector', ['test_collector_2'])],
        'test_collector_2': [MockFactCollector('test_collector_2', ['test_collector'])],
    }

    unresolved = find_unresolved_requires(collector_names, test_subsets)
    assert unresolved == set(['test_collector_2'])



# Generated at 2022-06-13 00:26:52.354159
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    all_fact_subsets = {
            'a': [MockFactCollector('a', required_facts=set())],
            'b': [MockFactCollector('b', required_facts=set(['c']))],
            #'c': [MockFactCollector('c', required_facts=set())],
            'd': [MockFactCollector('d', required_facts=set(['b']))],
    }


# Generated at 2022-06-13 00:27:02.221064
# Unit test for function get_collector_names
def test_get_collector_names():

    # test the basic case
    assert get_collector_names(valid_subsets=("A", "B", "C"), gather_subset=("A", "B")) == {"A", "B"}

    # test that explicitly excluded subsets are removed
    assert get_collector_names(valid_subsets=("A", "B", "C"),
                               gather_subset=("A", "B", '!B')) == {"A"}

    # test that normally excluded subsets are included as explicit inclusions
    assert get_collector_names(valid_subsets=("A", "B", "C"),
                               minimal_gather_subset=("C",),
                               gather_subset=("A", "B", '!C')) == {"A", "B"}

    # test that if all is used, the min are

# Generated at 2022-06-13 00:27:12.644533
# Unit test for function get_collector_names
def test_get_collector_names():
    # A trivial test, without aliases
    valid_subsets = frozenset(('all', 'network', 'facter'))
    minimal_gather_subset = frozenset(('facter',))
    aliases_map = defaultdict(set)

    assert ('all',) == get_collector_names(gather_subset=('all',),
                                           valid_subsets=valid_subsets,
                                           minimal_gather_subset=minimal_gather_subset,
                                           aliases_map=aliases_map)

# Generated at 2022-06-13 00:27:23.779634
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    class Collector0(BaseFactCollector):
        _fact_ids = set('foo fooness'.split())

    class Collector1(BaseFactCollector):
        _fact_ids = set('bar bardness'.split())

    class Collector2(BaseFactCollector):
        _fact_ids = set('bar bardness'.split())

    class Collector3(BaseFactCollector):
        _fact_ids = set('foo fooness'.split())

    collector_classes = [Collector0, Collector1, Collector2, Collector3]
    fact_id_to_collector_map, aliases_map = build_fact_id_to_collector_map(collector_classes)

    assert len(fact_id_to_collector_map['foo']) == 2

# Generated at 2022-06-13 00:27:32.317575
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    class FakeCollector1(BaseFactCollector):
        name = 'primary1'
        _fact_ids = frozenset(['secondary1', 'secondary2'])

    class FakeCollector2(BaseFactCollector):
        name = 'primary2'
        _fact_ids = frozenset(['secondary3'])

    # no aliases
    collectors_for_platform = set([FakeCollector1, FakeCollector2])
    fact_id_to_collector_map, aliases = build_fact_id_to_collector_map(collectors_for_platform)

# Generated at 2022-06-13 00:27:44.782697
# Unit test for function collector_classes_from_gather_subset
def test_collector_classes_from_gather_subset():
    def mock_collector_class(name, required_facts, _fact_ids=None):
        _fact_ids = _fact_ids or set()
        return type('MockCollector', (BaseFactCollector,), dict(name=name,
                                                                required_facts=required_facts,
                                                                _fact_ids=_fact_ids))
    collector_classes = [mock_collector_class('a', required_facts=set()),
                         mock_collector_class('b', required_facts=set()),
                         mock_collector_class('c', required_facts=set(['a']))]
    # 'c' depends on 'a'. this makes sure that it comes after 'a'.

# Generated at 2022-06-13 00:28:03.938175
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    _all_fact_subsets = {
        'a': [object],
        'b': [object],
        'c': [object],
        'd': [object],
        'e': [object],
    }

    # these are fake objects, so we must "annotate" the objects with
    # required facts.
    class a(object):
        required_facts = frozenset({'b'})
    class b(object):
        required_facts = frozenset({'a'})
    class c(object):
        required_facts = frozenset({'a'})
    class d(object):
        required_facts = frozenset({'c'})
    class e(object):
        required_facts = frozenset({'c', 'd'})


# Generated at 2022-06-13 00:28:14.737552
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    '''Test build_fact_id_to_collector_map.'''
    import copy
    import json

    # NOTE: this is a limited test to only test behavior in this function

    class TestCollectorA(BaseFactCollector):
        _fact_ids = set(['fact_id_a'])
        name = 'primary_name_a'

    class TestCollectorB(BaseFactCollector):
        _fact_ids = set(['fact_id_b'])
        name = 'primary_name_b'
        required_facts = set(['fact_id_a'])

    class TestCollectorC(BaseFactCollector):
        _fact_ids = set(['fact_id_c'])
        name = 'primary_name_c'

    class TestCollectorD(BaseFactCollector):
        _fact

# Generated at 2022-06-13 00:28:20.896609
# Unit test for function tsort
def test_tsort():
    import unittest
    try:
        tsort({1: [2, 3], 2: [3]})
    except CycleFoundInFactDeps:
        pass
    else:
        raise AssertionError('expected CycleFoundInFactDeps')
    assert tsort({1: [2, 3], 2: []}) == [(1, [2, 3]), (2, [])]



# Generated at 2022-06-13 00:28:28.293094
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    # build our own private 'collectors' to test with
    class Collector1(BaseFactCollector):
        name = 'primary'
        _fact_ids = ('secondary',)
    class Collector2(BaseFactCollector):
        name = 'primary'
        _fact_ids = ('secondary', 'tertiary')
    class Collector3(BaseFactCollector):
        name = 'primary'
        _fact_ids = ('tertiary',)
    class Collector4(BaseFactCollector):
        name = 'primary'

    # build the map and aliases/valid_subsets
    collectors_for_platform = [Collector1, Collector2, Collector3, Collector4]
    fact_id_to_collector_map, aliases_map = build_fact_id_to_collector_map(collectors_for_platform)

    #

# Generated at 2022-06-13 00:28:37.865377
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    all_fact_subsets = {
        'a': [MockCollector('a', requires=('a',))],
        'b': [MockCollector('b')],
        'c': [MockCollector('c', requires=('b',))],
    }
    assert find_unresolved_requires(('a', 'c',), all_fact_subsets) == set(('a',))
    assert find_unresolved_requires(('a', 'c', 'b'), all_fact_subsets) == set()
    assert find_unresolved_requires(('a', 'c', 'b', 'z'), all_fact_subsets) == set(('z',))



# Generated at 2022-06-13 00:28:49.020410
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    fact_subsets = {'foo': [BaseFactCollector], 'bar': [BaseFactCollector]}
    fact_subsets['foo'] = (list(fact_subsets['foo']) +
                           [type('NewCollector',
                                 (BaseFactCollector,),
                                 {'required_facts': 'bar'})])
    assert find_unresolved_requires(['foo'], fact_subsets) == set()
    assert find_unresolved_requires([], fact_subsets) == set()

    assert find_unresolved_requires(['foo'], {}) == set(['bar'])
    assert find_unresolved_requires(['bar'], {}) == set()
    assert find_unresolved_requires([], {}) == set()


# Generated at 2022-06-13 00:28:53.333274
# Unit test for function collector_classes_from_gather_subset
def test_collector_classes_from_gather_subset():
    class LocalFactCollectorA(BaseFactCollector):
        name = 'A'
        required_facts = set()

    class LocalFactCollectorB(BaseFactCollector):
        name = 'B'
        required_facts = set()

    class LocalFactCollectorC(BaseFactCollector):
        name = 'C'
        required_facts = set(['A'])

    class LocalFactCollectorD(BaseFactCollector):
        name = 'D'
        required_facts = set(['A', 'B'])

    class LocalFactCollectorE(BaseFactCollector):
        name = 'E'
        required_facts = set(['F'])

    class LocalFactCollectorF(BaseFactCollector):
        name = 'F'
        required_facts = set(['E'])


# Generated at 2022-06-13 00:28:59.146158
# Unit test for function build_dep_data
def test_build_dep_data():
    dep_map = build_dep_data(['collector1', 'collector2'], {
        'collector1': [BaseFactCollector],
        'collector2': [BaseFactCollector],
    })
    assert dep_map['collector1'] == set()
    assert dep_map['collector2'] == set()

    # test that it can handle a collector that requires another
    dep_map = build_dep_data(['collector1', 'collector2'], {
        'collector1': [BaseFactCollector],
        'collector2': [type('SomeFactCollector', (BaseFactCollector,), {
            'required_facts': ('collector1',),
        })],
    })
    assert dep_map['collector1'] == set()

# Generated at 2022-06-13 00:29:09.388709
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    class FactCollector1(BaseFactCollector):
        name = 'test1'
        _fact_ids = ('test1', 'test1.1', 'test1.2')
    class FactCollector2(BaseFactCollector):
        name = 'test2'
        _fact_ids = ('test2', 'test2.1', 'test2.2')
        required_facts = ('test1.1',)

    collector_classes = [
        FactCollector1,
        FactCollector2,
    ]

    fact_id_to_collector_map, aliases_map = build_fact_id_to_collector_map(collector_classes)

    assert len(fact_id_to_collector_map) == 7
    assert len(aliases_map) == 2


# Generated at 2022-06-13 00:29:13.691327
# Unit test for function build_dep_data
def test_build_dep_data():
    class TestClass(object):
        _fact_ids = ['bar']
        name = 'foo'
        required_facts = ['bar']
    collectors = [TestClass()]

    dep_map = build_dep_data([TestClass.name], collectors)
    assert dep_map[TestClass.name] == set(['bar'])


# Generated at 2022-06-13 00:29:32.940753
# Unit test for function get_collector_names
def test_get_collector_names():
    '''Unit test for function get_collector_names'''
    # pylint: disable=unused-argument
    import pytest
    # required modules don't get autoloaded.
    # pylint: disable=unused-variable
    from ansible.module_utils.facts import collector

    # "Only run test if we are testing the function"

# Generated at 2022-06-13 00:29:43.322515
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    from ansible.module_utils.facts import collectors

    all_collector_classes = collectors.get_collectors_for_names(
        ['distribution',
         'date_time',
         'virtual',
         'fips',
         'mounts',
         'selinux',
         'userspace_info',
         'ipv4_addr',
         'ipv6_addr',
         'processor',
         'memory',
         'kernel',
         'pkg_mgr',
         'service_mgr',
         'user',
         'cloud',
         'network',
         'fqdn',
         'system'],
        platform_info=dict(system='Linux'),
    )


# Generated at 2022-06-13 00:29:54.507325
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    #pylint: disable=missing-docstring
    import unittest
    import sys
    import os

    class UnitTest(unittest.TestCase):
        # pylint: disable=too-many-public-methods
        def test_find_unresolved_requires(self):
            # TODO: Add a test using a real fact collection module
            collector_name_a = 'a'
            collector_name_b = 'b'
            collectors = {collector_name_a: [],
                          collector_name_b: []}
            collectors[collector_name_a].append(
                type('_Collector_A', (object,), {'required_facts': (collector_name_b,)}))

# Generated at 2022-06-13 00:30:02.398473
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    all_fact_subsets = {}
    all_fact_subsets['a'] = [namedtuple('BaseFactCollector', 'name required_facts')(name='a', required_facts=set(['b']))]
    all_fact_subsets['b'] = [namedtuple('BaseFactCollector', 'name required_facts')(name='b', required_facts=set(['c']))]
    all_fact_subsets['c'] = [namedtuple('BaseFactCollector', 'name required_facts')(name='c', required_facts=set(['d']))]
    all_fact_subsets['d'] = [namedtuple('BaseFactCollector', 'name required_facts')(name='d', required_facts=set())]

    collector_names = ['a']
    unresolved = find_unresolved

# Generated at 2022-06-13 00:30:09.215258
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    class A(BaseFactCollector):
        name = 'A'
        required_facts = set(['B'])

    class B(BaseFactCollector):
        name = 'B'

    a = A()
    b = B()

    result = find_unresolved_requires(collector_names=set(['A']),
                                      all_fact_subsets={'A': [a], 'B': [b]})

    assert result == {'B'}



# Generated at 2022-06-13 00:30:20.553668
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    from ansible_collections.ansible.community.plugins.module_utils.facts.collectors import network
    from ansible_collections.ansible.community.plugins.module_utils.facts.collectors import hardware
    from ansible_collections.ansible.community.plugins.module_utils.facts.collectors import virtual

    collectors_for_platform = [
        network.NetworkInfoAll,
        hardware.Hardware,
        virtual.VirtualBox,
        virtual.VMWare,
    ]

    fact_id_to_collector_map, aliases_map = build_fact_id_to_collector_map(collectors_for_platform)

    # print('fact_id_to_collector_map', fact_id_to_collector_map)
    # print('aliases_map', aliases_map)

# Generated at 2022-06-13 00:30:32.003476
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    class A(BaseFactCollector):
        required_facts = set()
    class B(BaseFactCollector):
        required_facts = set(['a'])
    class C(BaseFactCollector):
        required_facts = set(['b'])
    class D(BaseFactCollector):
        required_facts = set(['c'])
    class E(BaseFactCollector):
        required_facts = set(['d'])
    class F(BaseFactCollector):
        required_facts = set(['e'])
    class G(BaseFactCollector):
        required_facts = set(['f', 'a'])


# Generated at 2022-06-13 00:30:38.941904
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    class CollectorA(BaseFactCollector):
        name = 'collector_a'
        _fact_ids = frozenset(['a', 'b'])

    class CollectorB(BaseFactCollector):
        name = 'collector_b'
        _fact_ids = frozenset(['b', 'c'])

    class CollectorC(BaseFactCollector):
        name = 'collector_c'
        _fact_ids = frozenset(['d', 'e'])

    def do_test(collectors_for_platform, expected_data):

        # Run function
        fact_id_to_collector_map, aliases_map = build_fact_id_to_collector_map(collectors_for_platform)

        # Verify results
        assert sorted(fact_id_to_collector_map.keys())

# Generated at 2022-06-13 00:30:49.688494
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    from . import platform
    from .platform import test_data_from_file
    from . import dmi
    from . import network
    from . import network_linux
    from . import network_windows
    from . import network_aws

    my_platform_data = test_data_from_file('fact_platform_data.json')

    all_collectors = [platform.RegisterAllFactCollectors,
                      dmi.RegisterDmiFactCollector,
                      network.RegisterAllFactCollectors,
                      network_linux.RegisterAllLinuxNetworkFactCollectors,
                      network_windows.RegisterAllWindowsNetworkFactCollectors,
                      network_aws.RegisterAllNetworkFactCollectors,
                      ]

    # get all fact collectors for this platform

# Generated at 2022-06-13 00:30:54.457123
# Unit test for function tsort
def test_tsort():
    try:
        tsort({'a': ['b'], 'b': ['a']})
        assert False, 'did not raise CycleFoundInFactDeps'
    except CycleFoundInFactDeps:
        pass
    res = tsort({'a': ['b'], 'b': []})
    assert res == [('b', set()), ('a', {'b'})]


# Generated at 2022-06-13 00:31:11.141267
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    from ansible_collections.ansible.community.plugins.module_utils.facts.collectors import network
    from ansible_collections.ansible.community.plugins.module_utils.facts.collectors import virtual
    class FakeOs(object):
        system = 'Linux'

    all_fact_subsets = defaultdict(list)
    all_fact_subsets.update({
        'network': [network.NetworkFactCollector],
        'virtual': [virtual.VirtualFactCollector],
    })
    # the ordering here is incorrect, but the test is still valid
    collector_names = ('network', 'virtual')

    try:
        unresolved_requires = find_unresolved_requires(collector_names, all_fact_subsets)
    except UnresolvedFactDep:
        unresolved_requires = None

    # there should be

# Generated at 2022-06-13 00:31:23.088314
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    from ansible.module_utils.facts.collector.parsers import ParserCollector
    from ansible.module_utils.facts.collector.rpm import RpmCollector
    from ansible.module_utils.facts.collector.zfs import ZFSCacheCollector
    test_alias1_class = type('test_alias1_class', (BaseFactCollector,), {})
    test_alias1_class.name = 'test_alias1'
    test_alias1_class._fact_ids = set(('test_id1', 'test_id2', 'test_id3'))

    test_alias2_class = type('test_alias2_class', (BaseFactCollector,), {})
    test_alias2_class.name = 'test_alias2'
    test_alias2_class._fact

# Generated at 2022-06-13 00:31:31.957417
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    all_fact_subsets = {
        'a': [BaseFactCollector],
        'b': [BaseFactCollector],
        'c': [BaseFactCollector],
    }
    all_fact_subsets['a'][0].required_facts = frozenset(['b'])
    all_fact_subsets['b'][0].required_facts = frozenset(['c'])
    all_fact_subsets['c'][0].required_facts = frozenset(['a'])

    assert find_unresolved_requires(['a'], all_fact_subsets) == set()
    assert find_unresolved_requires(['b'], all_fact_subsets) == set()
    assert find_unresolved_requires(['c'], all_fact_subsets) == set()


# Generated at 2022-06-13 00:31:44.146135
# Unit test for function collector_classes_from_gather_subset
def test_collector_classes_from_gather_subset():

    # call with no options, ie, use system from platform, and gather_subset=['all']
    selected_collector_classes = collector_classes_from_gather_subset()

    # gather_subset=['all'] doesn't mean we get *every* fact.
    # The '!all' still excludes virtual and network.
    acceptable_names = [x.name for x in selected_collector_classes if x.name != 'hardware']
    assert acceptable_names == ['platform']

    # Add in some extra classes, and ask it to select only 'network'
    all_collector_classes = (selected_collector_classes + [NetworkFactCollector])

# Generated at 2022-06-13 00:31:55.598467
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    import pytest

    test_data = [
        (['Base'], ['Base'], []),
        (['Base'], ['Base', 'A'], []),
        (['A'], ['Base', 'A'], ['Base']),
        (['A'], ['Base', 'A', 'B'], ['Base']),
        (['A', 'B'], ['Base', 'A', 'B'], ['Base']),
    ]

    class Base(BaseFactCollector):
        name = 'Base'

    class A(BaseFactCollector):
        name = 'A'
        required_facts = ['Base']

    class B(BaseFactCollector):
        name = 'B'
        required_facts = ['Base']


# Generated at 2022-06-13 00:32:05.980689
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    from ansible.module_utils.facts import collector as facts_collector
    from ansible.module_utils.facts import default
    all_collector_classes = facts_collector.get_collector_classes(default.ALL_SUBSETS)

    all_fact_subsets = defaultdict(list)
    for collector_class in all_collector_classes:
        all_fact_subsets[collector_class.name].append(collector_class)

    assertions = dict(
        dead_required=("foo", "bar", {"foo", "bar", "baz"}),  # (unknown, known, output)
        no_required=("foo", "baz", {'foo', 'baz'}),
        has_required=("bar", "baz", {"baz", "foo", 'bar'}),
    )

# Generated at 2022-06-13 00:32:14.966986
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():

    class SubsetFactCollector(BaseFactCollector):
        name = 'subset_fact'
        _fact_ids = set()

    class SubsetSubFactCollector(BaseFactCollector):
        name = 'subset_sub_fact'
        _fact_ids = set()

    class SubsetSubSubFactCollector(BaseFactCollector):
        name = 'subset_sub_sub_fact'
        _fact_ids = set()

    collectors_for_platform = [SubsetSubSubFactCollector, SubsetFactCollector, SubsetSubFactCollector]
    fact_id_to_collector_map, aliases_map = build_fact_id_to_collector_map(collectors_for_platform)

# Generated at 2022-06-13 00:32:21.846741
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    class A(BaseFactCollector):
        name = 'a'
        _fact_ids = {'x'}

    class B(BaseFactCollector):
        name = 'b'
        _fact_ids = {'x', '_x'}

    import pytest
    with pytest.raises(ValueError) as error:
        build_fact_id_to_collector_map([A, B])
    assert 'more than one collector' in str(error.value)
    assert 'x' in str(error.value)


# Generated at 2022-06-13 00:32:28.941558
# Unit test for function build_dep_data
def test_build_dep_data():
    class DepCollectorA(BaseFactCollector):
        name = 'A'
        def collect(self, module=None, collected_facts=None):
            return {'A':'A'}
    class DepCollectorB(BaseFactCollector):
        name = 'B'
        def collect(self, module=None, collected_facts=None):
            return {'B':'B'}
    class DepCollectorC(BaseFactCollector):
        name = 'C'
        required_facts = frozenset(['B'])
        def collect(self, module=None, collected_facts=None):
            return {'C':'C'}
    class DepCollectorD(BaseFactCollector):
        name = 'D'
        required_facts = frozenset(['A'])

# Generated at 2022-06-13 00:32:38.398596
# Unit test for function build_dep_data
def test_build_dep_data():
    collector_names = ['A', 'B', 'C']
    all_fact_subsets = {
        'A': [BaseFactCollector()],
        'B': [BaseFactCollector()],
        'C': [BaseFactCollector()],
    }
    all_fact_subsets['A'][0].required_facts = ['B']
    all_fact_subsets['B'][0].required_facts = ['C']
    all_fact_subsets['C'][0].required_facts = ['A']

    dep_map = build_dep_data(collector_names, all_fact_subsets)
    assert dep_map == {
        'A': {'B'},
        'B': {'C'},
        'C': {'A'},
    }



# Generated at 2022-06-13 00:32:51.552339
# Unit test for function build_dep_data
def test_build_dep_data():
    pass



# Generated at 2022-06-13 00:33:01.965830
# Unit test for function get_collector_names
def test_get_collector_names():
    platform_info = {
        'system': platform.system(),
        'machine': platform.machine(),
        'distribution': platform.dist(),
        'distribution_release': platform.release(),
        'distribution_version': platform.version(),
        'distribution_major_version': platform.dist()[1].split('.')[0]
    }
    valid_subsets = set(['all', 'network', 'hardware', 'virtual', 'min'])
    minimal_gather_subsets = ['min']
    aliases_map = defaultdict(set, {'hardware': set(['devices', 'dmi'])})
    # gather_subset could be None, empty list, or one of 'all', 'network', 'hardware', 'virtual', 'min'

# Generated at 2022-06-13 00:33:12.420464
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    def _make_all_fact_subsets(collector_classes):
        all_fact_subsets = defaultdict(set)
        for collector_class in collector_classes:
            for fact_id in collector_class.fact_ids:
                all_fact_subsets[fact_id].add(collector_class)
        return all_fact_subsets

    class CollectA(BaseFactCollector):
        name = 'a'
        # requires nothing to run
        required_facts = set()

    class CollectB(BaseFactCollector):
        name = 'b'
        # requires a to run
        required_facts = {'a'}

    class CollectC(BaseFactCollector):
        name = 'c'
        # requires a to run
        required_facts = {'a'}


# Generated at 2022-06-13 00:33:24.771120
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    '''Test if the find_unresolved_requires function works'''
    # collector_names = Collectors to run
    # all_fact_subsets = All collectors available on system
    # collector_name = Name of the collector to run
    # collector_classes = List of collectors that have name collector_name
    # required_facts = List of required facts for each collector that have name collector_name

    # Create a dict of collectors
    all_fact_subsets = dict()
    # Create a fake collector
    collector_class = FakeCollector()
    # Create a set of collectors classes with this collector
    collector_classes = {collector_class}
    # Create a set of collector names
    collector_names = set()
    # append one collector name with the name of fake collector
    collector_names.add(collector_class.name)
   

# Generated at 2022-06-13 00:33:33.058187
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    all_fact_subsets = defaultdict(list)
    class FactCollectorA(BaseFactCollector):
        name = 'a'
        required_facts = set(['b', 'c'])
    class FactCollectorB(BaseFactCollector):
        name = 'b'
        required_facts = set(['d'])
    class FactCollectorC(BaseFactCollector):
        name = 'c'
        required_facts = set(['d'])
    class FactCollectorD(BaseFactCollector):
        name = 'd'
        required_facts = set()

    all_collectors = [FactCollectorA, FactCollectorB, FactCollectorC, FactCollectorD]

# Generated at 2022-06-13 00:33:39.881435
# Unit test for function build_dep_data
def test_build_dep_data():
    data = {'A': ['C', 'B'],
            'B': ['C', 'A'],
            'C': ['A']}
    dep_map = build_dep_data(list(data.keys()), data)

    assert dep_map['A'] == {'C', 'B'}
    assert dep_map['B'] == {'C', 'A'}
    assert dep_map['C'] == {'A'}


# Generated at 2022-06-13 00:33:47.191726
# Unit test for function get_collector_names
def test_get_collector_names():
    minimal_gather_subset = frozenset(['hw', 'virtual', 'network'])
    valid_subsets = frozenset(['all', 'network'])
    aliases_map = defaultdict(set, {'hardware': frozenset(['hw', 'virtual'])})

    # Test: All
    collectors = get_collector_names(gather_subset=['all'],
                                     minimal_gather_subset=minimal_gather_subset,
                                     valid_subsets=valid_subsets,
                                     aliases_map=aliases_map)
    assert collectors == minimal_gather_subset | set(['network'])

    # Test: All, one additional

# Generated at 2022-06-13 00:33:56.033055
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    from ansible.module_utils.facts.collector import (
        MockLinuxCollector2 as MockLinuxCollector,
        MockLinuxCollector4 as MockLinuxCollector4,
        MockLinuxCollector5 as MockLinuxCollector5,
    )

    # add two fact collectors:
    # - linux_collector depends on dmi_collector
    # - dmi_collector has no special dependencies
    all_fact_subsets = {
        'linux_collector': [MockLinuxCollector],
        'dmi_collector': [MockLinuxCollector4],
    }

    # put linux_collector first in the list.
    collector_names = ['linux_collector', 'dmi_collector']

    unresolved = find_unresolved_requires(collector_names, all_fact_subsets)
    #

# Generated at 2022-06-13 00:34:06.304954
# Unit test for function get_collector_names
def test_get_collector_names():
    from ansible.module_utils.facts.utils.get_file_lines import get_file_lines

    # Test with all gather_subset options
    validset_file = 'test/unit/module_utils/facts/test_get_collector_names_validset.txt'
    valid_subsets = get_file_lines(validset_file)

    # Test 'all' option
    assert get_collector_names(valid_subsets=valid_subsets) == {'all'}
    assert get_collector_names(valid_subsets=valid_subsets,
                               gather_subset=['all']) == {'all'}

    # Test 'min' option