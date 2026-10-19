

# Generated at 2022-06-13 00:24:35.526251
# Unit test for function get_collector_names
def test_get_collector_names():
    assert get_collector_names(gather_subset=['min']) == frozenset(['min'])
    assert get_collector_names(gather_subset=['!min', 'min']) == frozenset(['min'])
    assert get_collector_names(gather_subset=['!min', 'network']) == frozenset(['network'])
    assert get_collector_names(gather_subset=['!network', 'network']) == frozenset(['network'])
    assert get_collector_names(gather_subset=['!network', 'min']) == frozenset(['min'])
    assert get_collector_names(gather_subset=['!network', 'min'], gather_subset_exclude=['min']) == frozens

# Generated at 2022-06-13 00:24:44.907053
# Unit test for function get_collector_names
def test_get_collector_names():
    import pytest

    aliases_map = defaultdict(set)
    aliases_map['hardware'].update(['devices', 'dmi'])

    valid_subsets = frozenset(['hardware'])

    def test_cases():
        yield ('all', ['hardware'])
        yield ('min', ['min'])
        yield ('!all', ['min'])
        yield ('!min', ['hardware'])
        yield ('!all,!devices', ['min'])
        yield ('!min,!devices', ['hardware'])


# Generated at 2022-06-13 00:24:55.686703
# Unit test for function find_collectors_for_platform
def test_find_collectors_for_platform():
    import ansible.module_utils.facts.collector.base as base
    import ansible.module_utils.facts.collector.windows as windows

    platform_info = {
        'system': 'Darwin',
    }

    if platform.system() == 'Windows':
        platform_info = {
            'system': platform.system(),
            'release': platform.release(),
            'version': platform.version(),
            'distribution': platform.dist(),
            'distribution_version': platform.win32_ver()[1],
        }

    # find_collectors_for_platform is a static method and can be tested with a single iteration
    # of the find_collectors_for_platform function

# Generated at 2022-06-13 00:25:07.148914
# Unit test for function find_collectors_for_platform
def test_find_collectors_for_platform():
    from ansible.module_utils.network.common.facts.facts import NetworkFactCollector
    from ansible.module_utils.facts.hardware.linux import LinuxHardwareCollector
    from ansible.module_utils.facts.network.linux import LinuxNetworkCollector

    def test_match(self, platform_info):
        for key, value in platform_info.items():
            if self._platform_info.get(key) != value:
                return False
        return True

    # re-create these to not use the real classes
    class LinuxNetworkCollectorTest(LinuxNetworkCollector):
        @classmethod
        def platform_match(cls, platform_info):
            return test_match(cls, platform_info)


# Generated at 2022-06-13 00:25:18.602794
# Unit test for function select_collector_classes
def test_select_collector_classes():
    from ansible.module_utils.facts.system.distribution import DistributionFactCollector
    from ansible.module_utils.facts.system.platform import PlatformFactCollector
    from ansible.module_utils.facts.system.pkg_mgr import PkgMgrFactCollector
    from ansible.module_utils.facts.system.user import UserFactCollector
    from ansible.module_utils.facts.system.selinux import SelinuxFactCollector
    from ansible.module_utils.facts.system.capability import CapabilityFactCollector

    all_fact_subsets = {
        'distribution': [DistributionFactCollector],
        'platform': [PlatformFactCollector],
        'network': [],
    }

    collector_names = ['network', 'platform']
    selected_collector_classes = select_

# Generated at 2022-06-13 00:25:28.906365
# Unit test for function get_collector_names
def test_get_collector_names():
    '''test get_collector_names result'''
    from ansible.module_utils.facts import collector
    _platform = 'Linux'
    _subsets = frozenset(['min', 'hardware', 'network', 'system'])

    facts_subset = frozenset(['min', 'hardware', 'network', 'system'])
    result = get_collector_names(subsets=_subsets,
                                 minimal_subset=facts_subset,
                                 aliases_map=collector._FACT_SUBSETS_MAP,
                                 platform_info=dict(system=_platform))
    assert result == frozenset(['system', 'network', 'hardware'])

    facts_subset = frozenset(['min', 'hardware', 'network', 'system'])
    result = get_collect

# Generated at 2022-06-13 00:25:34.486390
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    all_fact_subsets = {
        'min': (BaseFactCollector,),
        'platform_specific': (BaseFactCollector,),
        'not_selected': (BaseFactCollector,),
        'not_selected_platform_specific': (BaseFactCollector,),
    }

    assert find_unresolved_requires([], all_fact_subsets) == set()
    assert find_unresolved_requires(['min'], all_fact_subsets) == set()
    assert find_unresolved_requires(['min', 'platform_specific'], all_fact_subsets) == set()

    BaseFactCollector.required_facts = frozenset({'min'})
    assert find_unresolved_requires(['min'], all_fact_subsets) == set()
    assert find_unresolved

# Generated at 2022-06-13 00:25:42.439288
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    from ansible.module_utils.facts.collectors.network import NetworkCollector
    from ansible.module_utils.facts.collectors.hardware import HardwareCollector

    all_fact_subsets = {
        HardwareCollector.name: (
            HardwareCollector,
        ),
        NetworkCollector.name: (
            NetworkCollector,
        ),
    }

    assert find_unresolved_requires(['hardware'], all_fact_subsets) == set()

    assert find_unresolved_requires(['network'], all_fact_subsets) == set(['hardware'])



# Generated at 2022-06-13 00:25:45.821601
# Unit test for function build_dep_data
def test_build_dep_data():
    from ansible.module_utils.facts import collector
    all_fact_subsets=collector.get_collector_subsets()
    dep_map = build_dep_data(['all'], all_fact_subsets)
    assert dep_map == {'all': {'command'}}


# Generated at 2022-06-13 00:25:57.813950
# Unit test for function get_collector_names
def test_get_collector_names():
    # Test gather_subset=all
    assert get_collector_names(gather_subset=['all']) == {'all'}

    # Test gather_subset=!all
    assert get_collector_names(gather_subset=['!all']) == {'min'}

    # Test gather_subset=!all,foo
    assert get_collector_names(gather_subset=['!all', 'foo']) == {'min', 'foo'}

    # Test gather_subset=!all,foo,!bar
    assert get_collector_names(gather_subset=['!all', 'foo', '!bar']) == {'min', 'foo'}

    # Test gather_subset=!all,foo,!all

# Generated at 2022-06-13 00:26:19.425612
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    class FakeCollector:
        def __init__(self, name, required_facts):
            self.name = name
            self.required_facts = required_facts

# Generated at 2022-06-13 00:26:30.333248
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    import pytest
    from ansible.plugins.cache.collector import all_fact_subsets

    assert find_unresolved_requires(all_fact_subsets.keys(), all_fact_subsets) == set()

    # add a collector with a requires_facts() that won't be satisfied
    bad_collector = type('BadCollector', (BaseFactCollector, ), {
        'name': 'bad_collector',
        'required_facts': ['unkown_fact'],
    })
    all_fact_subsets['bad_collector'] = [bad_collector]

    assert find_unresolved_requires(all_fact_subsets.keys(), all_fact_subsets) == {'unkown_fact'}



# Generated at 2022-06-13 00:26:41.027364
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    from ansible.module_utils.facts.collector.network import Network
    from ansible.module_utils.facts.collector.virtual import Virtual

    # use a small subset of collectors to test build_fact_id_to_collector_map
    collectors = [Network, Virtual]
    # this is a minimal test harness, we aren't testing find_collectors_for_platform here.
    collectors_for_platform = set(collectors)
    fact_id_to_collector_map, aliases_map = build_fact_id_to_collector_map(collectors_for_platform)

    assert(len(fact_id_to_collector_map) == 5)
    assert(len(aliases_map) == 2) # 2 collectors were added to aliases_map

    # aliases_map should contain a set of names mapped to a

# Generated at 2022-06-13 00:26:51.229366
# Unit test for function select_collector_classes

# Generated at 2022-06-13 00:27:01.838157
# Unit test for function find_collectors_for_platform
def test_find_collectors_for_platform():
    class MyFactCollector1(BaseFactCollector):
        pass
    MyFactCollector1._platform = 'Darwin'
    MyFactCollector1.name = 'MyFactCollector1'

    class MyFactCollector2(BaseFactCollector):
        pass
    MyFactCollector2._platform = 'Generic'
    MyFactCollector2.name = 'MyFactCollector2'

    class MyFactCollector3(BaseFactCollector):
        pass
    MyFactCollector3._platform = None
    MyFactCollector3.name = 'MyFactCollector3'

    class MyFactCollector4(BaseFactCollector):
        pass
    MyFactCollector4._platform = 'Linux'
    MyFactCollector4.name = 'MyFactCollector4'


# Generated at 2022-06-13 00:27:12.334652
# Unit test for function get_collector_names
def test_get_collector_names():
    import pytest
    from ansible.module_utils.facts.collector import get_collector_names
    from ansible.module_utils.facts import timeout

    # some basic fact subset names
    valid_subsets = valid_subsets = frozenset(['hardware', 'network', 'cmdline', 'virtual'])
    minimal_gather_subset = frozenset(['hardware', 'network'])
    aliases_map = defaultdict(set)
    aliases_map['hardware'].update(['devices', 'dmi'])
    aliases_map['cmdline'].update(['mounts'])

    # test: All of the valid subsets are returned

# Generated at 2022-06-13 00:27:23.395466
# Unit test for function select_collector_classes
def test_select_collector_classes():
    class FakeCollector(BaseFactCollector):
        name = 'fake'
        def __init__(self):
            BaseFactCollector.__init__(self)

    class FakeCollectorA(BaseFactCollector):
        name = 'fake_a'
        _fact_ids = {'fake_a', 'fake'}
        def __init__(self):
            BaseFactCollector.__init__(self)

    class FakeCollectorB(BaseFactCollector):
        name = 'fake_b'
        _fact_ids = {'fake_a', 'fake'}
        def __init__(self):
            BaseFactCollector.__init__(self)

    collector_names = ['fake', 'fake_b']

# Generated at 2022-06-13 00:27:32.055586
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    # Create a collector class for use in this function
    class CollectorStub(BaseFactCollector):
        name = 'CollectorStub'
        _fact_ids = ('stub1', 'stub2')

    # Try an empty set; expect no results
    assert build_fact_id_to_collector_map(set()) == ({}, {})

    # Now put a single collector class in a set and try
    fact_id_to_collector_map = build_fact_id_to_collector_map(set([CollectorStub]))[0]
    assert fact_id_to_collector_map[CollectorStub.name] == [CollectorStub]
    assert fact_id_to_collector_map['stub1'] == [CollectorStub]
    assert fact_id_to_collector

# Generated at 2022-06-13 00:27:44.359395
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    class TestCollector1(object):
        _fact_ids = frozenset(['foo', 'bar'])

        def __init__(self, *args, **kwargs):
            pass

        name = '1'

    class TestCollector2(object):
        _fact_ids = frozenset(['xyz', 'abc'])

        def __init__(self, *args, **kwargs):
            pass

        name = '2'

    fact_id_to_collector_map, aliases_map = build_fact_id_to_collector_map([TestCollector1, TestCollector2])
    assert fact_id_to_collector_map['1'] == [TestCollector1]
    assert fact_id_to_collector_map['2'] == [TestCollector2]
    assert fact_

# Generated at 2022-06-13 00:27:54.768575
# Unit test for function find_collectors_for_platform
def test_find_collectors_for_platform():

    # Test class, represents any collector
    class TestCollector(BaseFactCollector):

        # Platform name, corresponds to ansible_facts['system']
        _platform = 'Generic'

        # Collector name, corresponds to subset
        name = 'test_collector'

    # Test platform info
    test_platform_info = {'system': 'Linux'}

    # Test collector classes
    test_collector_classes = [TestCollector]

    # Test platform info
    test_compat_platforms = [test_platform_info]

    # Test function find_collectors_for_platform
    found_collectors = find_collectors_for_platform(test_collector_classes, test_compat_platforms)

    # The number of collectors should be one
    assert(len(found_collectors) == 1)

    # The

# Generated at 2022-06-13 00:28:19.518860
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    class CollectorA(BaseFactCollector):
        name = 'A'
        _fact_ids = ['A']

    class CollectorB(BaseFactCollector):
        name = 'B'
        _fact_ids = ['B']

    class CollectorC(BaseFactCollector):
        name = 'C'
        _fact_ids = ['C']

    class CollectorD(BaseFactCollector):
        name = 'D'
        _fact_ids = ['D', 'E']

    # test some interesting cases
    # duplicate collector_classes
    collector_classes = (CollectorA, CollectorB, CollectorA, CollectorB)
    fact_id_to_collector_map, aliases_map = build_fact_id_to_collector_map(collector_classes)

# Generated at 2022-06-13 00:28:29.842190
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    import unittest
    import sys

    if sys.version_info.major < 3:
        from mock import MagicMock
    else:
        from unittest.mock import MagicMock

    class TestCase(unittest.TestCase):
        def test_no_unresolved(self):
            collector_names = ['a', 'b', 'c']
            all_fact_subsets = {
                'a': [MagicMock(spec=['required_facts'], required_facts=set(['b']))],
                'b': [MagicMock(spec=['required_facts'], required_facts=set(['c']))],
                'c': [MagicMock(spec=['required_facts'], required_facts=set(['a']))],
            }
            unresolved = find_unresolved_requires

# Generated at 2022-06-13 00:28:35.452965
# Unit test for function select_collector_classes
def test_select_collector_classes():
    class module:
        def __init__(self):
            self.params = dict()
            self.params['gather_subset'] = ['network']
            self.params['gather_timeout'] = 5
    from ansible.module_utils.facts import local
    l = local.Local(lambda:module())
    l.get_all([],l.module.params)


# Generated at 2022-06-13 00:28:42.564135
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    class FakeCollector(BaseFactCollector):
        name = 'fake'
        _fact_ids = frozenset(['one', 'two'])

    result = build_fact_id_to_collector_map([FakeCollector])
    assert len(result) == 2
    for fact_id_to_collector_map, aliases_map in result:
        assert fact_id_to_collector_map['fake'][0] == FakeCollector
        assert fact_id_to_collector_map['one'][0] == FakeCollector
        assert fact_id_to_collector_map['two'][0] == FakeCollector
        assert aliases_map['fake'] == frozenset(['one', 'two'])



# Generated at 2022-06-13 00:28:54.160612
# Unit test for function select_collector_classes
def test_select_collector_classes():
    import pytest

    # Test case 1
    # Assert that multiple classes are not added more then once
    class One(BaseFactCollector):
        name = 'one'
    class Two(One):
        name = 'two'
    class Three(One):
        name = 'three'

    all_fact_subsets = defaultdict(list)
    all_fact_subsets['one'].append(One)
    all_fact_subsets['two'].append(Two)
    all_fact_subsets['three'].append(Three)

    # Test 1a
    collector_names = ['one', 'two', 'three']
    expected_collector_classes = [One, Two, Three]
    collector_classes = select_collector_classes(collector_names, all_fact_subsets)
    assert collector_classes

# Generated at 2022-06-13 00:29:01.081674
# Unit test for function find_collectors_for_platform
def test_find_collectors_for_platform():
    class WinCollector(BaseFactCollector):
        _platform = 'Windows'
        name = 'windows'

    class PosixCollector(BaseFactCollector):
        _platform = 'Generic'
        name = 'posix'

    class LinuxCollector(PosixCollector):
        _platform = 'Linux'
        name = 'linux'

    class MacCollector(PosixCollector):
        _platform = 'Darwin'
        name = 'mac'

    class FreeBSDCollector(PosixCollector):
        _platform = 'FreeBSD'
        name = 'freebsd'

    class OpenBSDCollector(PosixCollector):
        _platform = 'OpenBSD'
        name = 'openbsd'


# Generated at 2022-06-13 00:29:06.669497
# Unit test for function build_dep_data
def test_build_dep_data():
    all_fact_subsets = {
        'all': [
            CollectorA,
            CollectorB,
            CollectorC,
            CollectorD
        ]
    }
    result = build_dep_data(['A', 'B', 'C'], all_fact_subsets)
    expected = {
        'A': {'B'},
        'B': set(),
        'C': {'A', 'B'}
    }
    assert result == expected



# Generated at 2022-06-13 00:29:15.791710
# Unit test for function get_collector_names
def test_get_collector_names():
    all_collectors = {'virtual', 'network', 'kernel'}
    minimal_collectors = {'virtual'}
    aliases_map = {'hardware': {'dmi', 'devices'}}

    # a test case for gather_subset, expected result

# Generated at 2022-06-13 00:29:27.073790
# Unit test for function build_dep_data
def test_build_dep_data():
    import unittest
    class TestCollectorFoo(BaseFactCollector):
        _fact_ids = set()
        _platform = 'Generic'
        name = 'foo'
        required_facts = set(['bar', 'baz'])
        def collect(self, module=None, collected_facts=None):
            return {'fact': 'fact_foo'}

    class TestCollectorBar(BaseFactCollector):
        _fact_ids = set()
        _platform = 'Generic'
        name = 'bar'
        required_facts = set()
        def collect(self, module=None, collected_facts=None):
            return {'fact': 'fact_bar'}

    class TestCollectorBaz(BaseFactCollector):
        _fact_ids = set()
        _platform = 'Generic'

# Generated at 2022-06-13 00:29:38.848921
# Unit test for function find_collectors_for_platform
def test_find_collectors_for_platform():
    from ansible.module_utils.facts import collectors
    import unittest
    import sys

    class Test_find_collectors_for_platform(unittest.TestCase):

        def setUp(self):

            class CollectorA(BaseFactCollector):
                name = 'A'
                _platform = 'Test'

            class CollectorB(BaseFactCollector):
                name = 'B'
                _platform = 'Test'

            class CollectorC(BaseFactCollector):
                name = 'C'
                _platform = 'Test'

            collectors.all_collectors = (CollectorA, CollectorB, CollectorC)

        def test_empty_list_compat_platforms(self):
            result = find_collectors_for_platform(collectors.all_collectors, [])

# Generated at 2022-06-13 00:30:14.598619
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    from ansible.module_utils.facts.collector.network import NetworkFactCollector
    from ansible.module_utils.facts.collector.network_legacy import NetworkLegacyFactCollector

    CollectorA = type('CollectorA', (BaseFactCollector,),
                      {'name': 'A', 'required_facts': ['unknown']})
    CollectorB = type('CollectorB', (BaseFactCollector,),
                      {'name': 'B', 'required_facts': ['C']})
    CollectorC = type('CollectorC', (BaseFactCollector,),
                      {'name': 'C', 'required_facts': ['D']})
    CollectorD = type('CollectorD', (BaseFactCollector,),
                      {'name': 'D', 'required_facts': []})


# Generated at 2022-06-13 00:30:25.495935
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    from test.units.compat import unittest
    from test.units.compat.mock import patch

    TEST_COLLECTOR_CLASSES = ['fake_collector_class_1', 'fake_collector_class_2']
    TEST_ALL_FACT_SUBSETS = {
        'fake_collector_class_1': ['FakeCollectorClass1']
    }

    class FakeCollectorClass1(object):
        required_facts = set()

    class FakeCollectorClass2(object):
        required_facts = set()


# Generated at 2022-06-13 00:30:35.363186
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():

    # build the input
    from ansible.module_utils.facts import Collector, Popen
    class Collector1(Collector):
        name = 'collector1'
        _fact_ids = frozenset(['fact1', 'fact2'])
        def collect(self):
            return {'fact1': 'collector1', 'fact2': 'collector1'}

    class Collector2(Collector):
        name = 'collector2'
        _fact_ids = frozenset(['fact2', 'fact3', 'fact4'])
        def collect(self):
            return {'fact2': 'collector2', 'fact3': 'collector2', 'fact4': 'collector2'}

    class Collector3(Collector):
        name = 'collector3'

# Generated at 2022-06-13 00:30:46.557261
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts.utils import timeout

    class Collector1(BaseFactCollector):
        _fact_ids = set(['fact1', 'fact2'])

    class Collector2(BaseFactCollector):
        _fact_ids = set(['fact3'])

    class Collector3(BaseFactCollector):
        _fact_ids = set(['fact4'])

    class Collector4(BaseFactCollector):
        _fact_ids = set(['fact5'])

    class Collector5(BaseFactCollector):
        _fact_ids = set(['fact6', 'fact7'])

    class Collector6(BaseFactCollector):
        _fact_ids = set(['fact8'])


# Generated at 2022-06-13 00:30:56.471612
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    '''Test find_unresolved_requires:

    Most of the 'facts' in this test are fake/unimplemented.

    '''

    class FakeCollector1(BaseFactCollector):
        name = 'collector1'
        required_facts = set('fact1')

    class FakeCollector2(BaseFactCollector):
        name = 'collector2'
        required_facts = set(['fact1', 'fact2'])

    class FakeCollector3(BaseFactCollector):
        name = 'collector3'
        required_facts = set(['fact2', 'fact3'])

    class FakeCollector4(BaseFactCollector):
        name = 'collector4'
        required_facts = set(['collector1', 'collector2'])


# Generated at 2022-06-13 00:31:07.978093
# Unit test for function get_collector_names
def test_get_collector_names():
    assert get_collector_names(
        # valid_subsets
        frozenset(['hardware', 'network']),
        # minimal_gather_subset
        frozenset(['hardware']),
        # gather_subset
        ['network'],
        # aliases_map
        defaultdict(set),
        # platform_info
        {}
    ) == frozenset(['network'])

# Generated at 2022-06-13 00:31:13.928632
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    collector_names = ['a', 'b', 'c']
    all_fact_subsets = {'a': [1], 'b': [2], 'c': [3]}
    unresolved = find_unresolved_requires(collector_names, all_fact_subsets)
    assert unresolved == set()

    all_fact_subsets = {'a': [1, 2], 'b': [2], 'c': [3]}
    unresolved = find_unresolved_requires(collector_names, all_fact_subsets)
    assert unresolved == set(['c'])



# Generated at 2022-06-13 00:31:24.020528
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    # This is a minimal example that creates 3 collectors and then
    # collects them, skipping one of them.
    #
    # If there is no error raised, then the test passes.

    all_fact_subsets = defaultdict(list)

    class CollectorA(BaseFactCollector):
        _fact_ids = {'a'}
        name = 'a'

        def collect(self, module=None, collected_facts=None):
            return {'a': 'a'}

    all_fact_subsets['a'].append(CollectorA)

    class CollectorB(BaseFactCollector):
        _fact_ids = {'b'}
        name = 'b'
        required_facts = ('a',)


# Generated at 2022-06-13 00:31:30.074166
# Unit test for function build_dep_data
def test_build_dep_data():
    test_dep_map = {}
    test_dep_map = {
        'a': set(['c']),
        'b': set(['c']),
        'c': set(),
        'd': set(['a', 'c']),
        'e': set(['a', 'b', 'd']),
        'f': set(['e'])
    }
    assert(build_dep_data(list(test_dep_map), test_dep_map) == test_dep_map)


# Generated at 2022-06-13 00:31:36.742937
# Unit test for function get_collector_names
def test_get_collector_names():
    valid_subsets = frozenset(['hardware', 'network', 'virtual'])
    minimal_gather_subset = frozenset(['virtual'])

    assert get_collector_names(gather_subset=['all'],
                               valid_subsets=valid_subsets,
                               minimal_gather_subset=minimal_gather_subset) == frozenset(['network', 'virtual'])
    assert get_collector_names(gather_subset=['network'],
                               valid_subsets=valid_subsets,
                               minimal_gather_subset=minimal_gather_subset) == frozenset(['network'])

# Generated at 2022-06-13 00:31:55.783497
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    import pytest
    from ansible.module_utils.facts.collector.base import BaseFactCollector
    from ansible.module_utils.facts.collector.command_output import CommandOutputCollector
    from ansible.module_utils.facts.collector.file import FileCollector
    from ansible.module_utils.facts.collector.network import NetworkCollector
    from ansible.module_utils.facts.collector.hardware import HardwareCollector
    from ansible.module_utils.facts.collector.virtual import VirtualCollector
    from ansible.module_utils.facts.collector.distribution import DistributionCollector
    from ansible.module_utils.facts.collector.service import ServiceCollector


# Generated at 2022-06-13 00:32:06.086524
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    # Some fake classes, for this test only
    class Collector_A(BaseFactCollector):
        name = 'A'
        required_facts = ['X', 'Y']
    class Collector_B(BaseFactCollector):
        name = 'B'
        required_facts = ['X']
    class Collector_C(BaseFactCollector):
        name = 'C'
        required_facts = ['D']
    class Collector_X(BaseFactCollector):
        name = 'X'
        required_facts = []
    class Collector_Y(BaseFactCollector):
        name = 'Y'
        required_facts = ['A']
    class Collector_Z(BaseFactCollector):
        name = 'Z'
        required_facts = ['A', 'Q', 'W']

    # Some fake data, for this test only
    all

# Generated at 2022-06-13 00:32:16.200899
# Unit test for function get_collector_names
def test_get_collector_names():
    '''this is a test stub to ensure the get_collector_names() function returns the correct set of
       subsets for a variety of params.

       The goal is not to test that the gather subsets are valid (ie, no module will ever generate
       a gather_subset of 'test-subset') but that the selection logic is correct.
       '''

    valid_subsets = frozenset(['all', 'network', 'hardware'])
    minimal_subsets = frozenset(['network'])

    collect_all = get_collector_names(valid_subsets=valid_subsets, minimal_gather_subset=minimal_subsets)
    assert collect_all == valid_subsets, \
        "collect_all %s != valid_subsets %s" % (collect_all, valid_subsets)

   

# Generated at 2022-06-13 00:32:25.845971
# Unit test for function build_fact_id_to_collector_map
def test_build_fact_id_to_collector_map():
    class TestCollector(BaseFactCollector):
        _fact_ids = {'name1', 'name2'}
        name = 'name'
        required_facts = set()

        def collect(self, module=None, collected_facts=None):
            pass

        @classmethod
        def platform_match(cls, platform_info):
            return cls

    class TestCollector2(BaseFactCollector):
        _fact_ids = {'name3'}
        name = 'name'
        required_facts = set()

        def collect(self, module=None, collected_facts=None):
            pass

        @classmethod
        def platform_match(cls, platform_info):
            return cls

    fact_id_to_collector_map, aliases_map = build_fact_id_to_collector

# Generated at 2022-06-13 00:32:35.956673
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    from ansible.module_utils.facts.collector import BaseFactCollector
    unresolved_requires = []
    class FactCollector_1(BaseFactCollector):
        name = 'FactCollector_1'
        required_facts = ('required_fact_1', 'required_fact_2')
    class FactCollector_2(BaseFactCollector):
        name = 'FactCollector_2'
        required_facts = ('required_fact_1', 'required_fact_2')
    all_fact_subsets = {
        'all_fact_subsets_key': 'all_fact_subsets_value',
        'FactCollector_1': FactCollector_1,
        'FactCollector_2': FactCollector_2,
    }

# Generated at 2022-06-13 00:32:45.296974
# Unit test for function build_dep_data
def test_build_dep_data():
    test_collector_names = ('test1', 'test2', 'test3')
    test_all_fact_subsets = {
        'test1': [
            TestCollector1(required_facts=set(['test2'])),
            TestCollector2(required_facts=set(['test3']))
        ],
        'test2': [
            TestCollector1(required_facts=set(['test3']))
        ],
        'test3': [
            TestCollector1(required_facts=set(['test1']))
        ]
    }

    test_dep_map = {
        'test1': set(['test2', 'test3']),
        'test2': set(['test3']),
        'test3': set(['test1'])
    }

    assert build_dep

# Generated at 2022-06-13 00:32:56.771667
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    class ACollector(BaseFactCollector):
        name = 'a'
        required_facts = ['b', 'c']
    class BCollector(BaseFactCollector):
        name = 'b'
        required_facts = ['c', 'd', 'e']
    class CCollector(BaseFactCollector):
        name = 'c'
        required_facts = ['d']

    class DCollector(BaseFactCollector):
        name = 'd'
    class ECollector(BaseFactCollector):
        name = 'e'
    class FCollector(BaseFactCollector):
        name = 'f'


# Generated at 2022-06-13 00:33:04.441494
# Unit test for function get_collector_names
def test_get_collector_names():
    # Test case for the 'gather_subset' argument
    assert get_collector_names(gather_subset=['!min', '!all']) == frozenset()
    assert get_collector_names(gather_subset=['!all']) == frozenset()
    assert get_collector_names(gather_subset=['all']) != frozenset()
    assert get_collector_names(gather_subset=['hardware']) == frozenset(['hardware'])
    assert get_collector_names(gather_subset=['dmi']) == frozenset(['hardware'])
    assert get_collector_names(gather_subset=['dmi', '!hardware']) == frozenset()

# Generated at 2022-06-13 00:33:13.666564
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    # Case where there are no unresolved requires
    all_fact_subsets = {
        'all': [],
        'test_fact': [
            type('Collector1', (BaseFactCollector, object), {'name': 'test_fact', 'required_facts': set()})
        ]
    }
    collector_names = ['all', 'test_fact']
    returned = find_unresolved_requires(collector_names, all_fact_subsets)
    assert(returned == set())
    # Case where there is an unresolved require

# Generated at 2022-06-13 00:33:26.154258
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    import doctest
    from ansible.module_utils.facts import ansible_collector_names
    from ansible.module_utils.facts import ansible_fact_subsets

    results = doctest.testmod(ansible_collector_names)
    if results.failed:
        raise AssertionError('Failed tests: %s' % results.failed)

    results = doctest.testmod(ansible_fact_subsets)
    if results.failed:
        raise AssertionError('Failed tests: %s' % results.failed)

    unresolved = find_unresolved_requires(ansible_collector_names.FACT_SUBSETS['all'],
                                          ansible_fact_subsets.ALL_FACT_SUBSETS)


# Generated at 2022-06-13 00:33:43.788295
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    # Dummy FactCollector that doesn't actually collect anything,
    # but will be used for testing find_unresolved_requires.
    # name is the name of the collector.
    # required_facts is the list of FactCollectors this Collector
    # depends on.
    class DummyCollector(BaseFactCollector):
        name = None
        required_facts = None

        def __init__(self, name, required_facts=None):
            super(DummyCollector, self).__init__()
            self.name = name
            self.required_facts = required_facts or []

        def collect(self, module=None, collected_facts=None):
            # Dummy method to satisfy BaseFactCollector API
            pass


# Generated at 2022-06-13 00:33:53.624321
# Unit test for function get_collector_names
def test_get_collector_names():
    alias_map = defaultdict(set)
    alias_map['hardware'].update(['devices', 'dmi'])
    alias_map['kernel'].update(['version'])
    alias_map['system'].update(['kernel', 'version'])
    alias_map['all'].update(['network', 'hardware'])

    # Common used subset
    subset = ['network']
    valid_subsets = frozenset(['all', 'network'])
    minimal_gather_subset = frozenset(['network'])
    collector_names = get_collector_names(valid_subsets=valid_subsets,
                                          minimal_gather_subset=minimal_gather_subset,
                                          gather_subset=subset, aliases_map=alias_map)
    assert collector

# Generated at 2022-06-13 00:34:04.175324
# Unit test for function find_unresolved_requires
def test_find_unresolved_requires():
    # Mocks
    module = 'MockModule'

    # Fact collector dependencies
    class GenericA(BaseFactCollector):
        name = 'A'
        required_facts = set()
    class GenericB(BaseFactCollector):
        name = 'B'
        required_facts = set(['A'])
    class GenericC(BaseFactCollector):
        name = 'C'
        required_facts = set(['B'])
    class GenericD(BaseFactCollector):
        name = 'D'
        required_facts = set(['A'])
    class GenericE(BaseFactCollector):
        name = 'E'
        required_facts = set()

    class WindowsA(BaseFactCollector):
        name = 'A'
        required_facts = set()