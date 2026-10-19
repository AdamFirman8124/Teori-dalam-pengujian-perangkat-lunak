

# Generated at 2022-06-13 00:09:58.328982
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    # Create a mock module
    class MockModule:

        def fail_json(self, *args, **kwargs):
            raise RuntimeError()

        def exit_json(self, *args, **kwargs):
            raise RuntimeError()

        def has_key(self, *args, **kwargs):
            return False

        def debug(self, *args, **kwargs):
            raise RuntimeError()

        def get_bin_path(self, *args, **kwargs):
            return 'mock'

    module = MockModule()

    # Create a mock fact collector that returns facts
    class MockFactCollector:

        def collect_with_namespace(self, *args, **kwargs):
            return {
                'fact1': 'value1',
                'fact2': 'value2',
            }

    # Create a fact

# Generated at 2022-06-13 00:10:08.920098
# Unit test for function get_ansible_collector
def test_get_ansible_collector():

    from ansible.module_utils.facts import default_collector_classes

    fact_collector = get_ansible_collector(all_collector_classes=default_collector_classes,
                                           filter_spec='ansible_distribution*',
                                           gather_subset=['network'])

    assert len(fact_collector.collectors) == 2
    assert isinstance(fact_collector.collectors[0], collector.CollectorMetaDataCollector)

    assert fact_collector.collectors[0].gather_subset == ['network']

    facts = fact_collector.collect()
    assert 'ansible_facts' in facts
    assert 'gather_subset' in facts['ansible_facts']
    assert 'ansible_distribution' in facts['ansible_facts']

# Generated at 2022-06-13 00:10:16.328636
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    from ansible.module_utils.facts import collector_functions
    from ansible.module_utils.facts import cache
    from ansible.module_utils.facts import namespace
    from ansible.module_utils.facts import namespaced_fact_collectors
    from ansible.module_utils.facts import ansible_facts
    from ansible.module_utils.facts import ansible_facts_collector
    from ansible.module_utils.facts import network

    class TestCollectorA(collector.BaseFactCollector):
        name = 'a'
        _fact_id = 'a'

        def collect(self, module=None, collected_facts=None):
            return {'a': 1}

    class TestCollectorB(collector.BaseFactCollector):
        name = 'b'

# Generated at 2022-06-13 00:10:29.671944
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    from ansible.module_utils.facts import ansible_collector
    from ansible.module_utils.facts import timeout
    from ansible.module_utils.facts import network
    from ansible.module_utils.facts import defaults
    from ansible.module_utils.facts import system
    from ansible.module_utils.facts import virtual
    from ansible.module_utils.facts import hardware

    all_collector_classes = [ansible_collector.AnsibleCollector,
                             timeout.TimeoutCollector,
                             network.NetworkCollector,
                             defaults.DefaultsCollector,
                             system.SystemCollector,
                             virtual.VirtualCollector,
                             hardware.HardwareCollector]

    # Usually gather_subset is specified by the user in the playbook.
    gather_subset = ['all']


# Generated at 2022-06-13 00:10:37.171220
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    class TestCollector_1(collector.BaseFactCollector):
        name = 'test_collector_1'

        @classmethod
        def get_collector_requirements(self):
            return {}

        def collect(self, module=None, collected_facts=None):
            return {'a': 1}

    class TestCollector_2(collector.BaseFactCollector):
        name = 'test_collector_2'

        @classmethod
        def get_collector_requirements(self):
            return {'a': 1}

        def collect(self, module=None, collected_facts=None):
            return {'b': 2}

    class TestCollector_3(collector.BaseFactCollector):
        name = 'test_collector_3'


# Generated at 2022-06-13 00:10:46.377263
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    try:
        from ansible.module_utils.facts import default_collectors
    except ImportError:
        # ansible/module_utils/facts/default_collectors.py doesn't have to be present
        # during installation of ansible.module_utils.facts.
        return

    assert(get_ansible_collector(all_collector_classes=default_collectors.ALL_COLLECTOR_CLASSES,
                                 filter_spec=['ansible_os*', 'ansible_python_version'])
           )


# Generated at 2022-06-13 00:10:55.387577
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    from ansible.module_utils.facts import ansible_collector, network, hardware, system, virtual

    fact_collector = get_ansible_collector(
        all_collector_classes=[network.NetworkCollector,
                               system.SystemCollector,
                               virtual.VirtualCollector,
                               hardware.HardwareCollector]
    )
    assert isinstance(fact_collector, ansible_collector.AnsibleFactCollector)
    assert len(fact_collector.collectors) == 5
    for col in fact_collector.collectors:
        assert isinstance(col, collector.BaseFactCollector)

# Generated at 2022-06-13 00:11:03.161934
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    all_collector_classes = collector.get_collector_classes()
    fact_collector = get_ansible_collector(all_collector_classes,
                                           namespace=None,
                                           gather_subset=None,
                                           gather_timeout=None,
                                           minimal_gather_subset=None)
    # Simple sanity test, check we have some collectors
    assert(len(fact_collector.collectors) > 0)

# Generated at 2022-06-13 00:11:09.829393
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    '''Tests function get_ansible_collector'''

    # import random
    # gather_subset = random.sample(['hardware', 'virtual', 'facter'], 3)
    gather_subset = ['hardware', 'virtual', 'facter']
    filter_spec = ['hardware']
    gather_timeout = 120
    minimal_gather_subset = frozenset(['hardware', 'virtual', 'facter'])

# Generated at 2022-06-13 00:11:21.268921
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():

    # return empty dict when no filter spec is provided
    a_facts_namespace = 'ansible_facts'
    a_collector = AnsibleFactCollector(namespace=a_facts_namespace)

    facts = a_collector.collect()
    assert facts == {}

    # return dict with fact named 'a'
    class CollectingFactCollector(collector.BaseFactCollector):

        name = 'test'

        def collect(self, module=None, collected_facts=None):
            return {'a': 1}

    test_collector = CollectingFactCollector(namespace=a_facts_namespace)
    a_collector = AnsibleFactCollector(collectors=[test_collector],
                                       namespace=a_facts_namespace)

    facts = a_collector.collect()

# Generated at 2022-06-13 00:11:33.032477
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    import six

    if six.PY2:
        from ansible_collections.ansible.community.tests.unit.compat import mock
    else:
        import unittest.mock as mock
    mocked_collector = mock.create_autospec(collector.BaseFactCollector)
    mocked_collector.collect_with_namespace.return_value = {'test_fact': 'test_val'}

    ansible_facts_collector = AnsibleFactCollector(collectors=[mocked_collector])
    facts = ansible_facts_collector.collect(module=None, collected_facts=None)
    assert facts['test_fact'] == 'test_val'

# Generated at 2022-06-13 00:11:44.459209
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    # arrange
    collector.all_collector_classes = [MockCollector1]
    gather_subset = ['all']
    gather_timeout = timeout.DEFAULT_GATHER_TIMEOUT
    minimal_gather_subset = frozenset()
    namespace = None
    filter_spec = ['ansible_os_family', 'ansible_mounts', 'ansible_*']

    fact_collector = get_ansible_collector(all_collector_classes=collector.all_collector_classes,
                                           namespace=namespace,
                                           filter_spec=filter_spec,
                                           gather_subset=gather_subset,
                                           gather_timeout=gather_timeout,
                                           minimal_gather_subset=minimal_gather_subset)

    # act

# Generated at 2022-06-13 00:11:54.096919
# Unit test for function get_ansible_collector
def test_get_ansible_collector():

    all_collector_classes = []  # No collectors
    namespace = None
    filter_spec = None
    gather_subset = ['all']
    gather_timeout = 10
    minimal_gather_subset = frozenset()

    result = get_ansible_collector(all_collector_classes,
                                   namespace,
                                   filter_spec,
                                   gather_subset,
                                   gather_timeout,
                                   minimal_gather_subset)

    assert result.collectors == [CollectorMetaDataCollector(gather_subset=['all'],
                                                            module_setup=True)]


# Generated at 2022-06-13 00:12:04.249818
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():

    import ansible.module_utils.facts
    all_collector_classes = ansible.module_utils.facts.collectors.collector_classes

    from ansible.module_utils.facts import namespace
    from ansible.module_utils.facts import fetch

    # Note: for each collector, we need the namespace collector and the fetch collector.
    collectors = []
    for cls in all_collector_classes:
        namespace_cls = namespace.get_namespace_class(cls.name)
        if namespace_cls:
            namespace_obj = namespace_cls()
            collectors.append(namespace_obj)

        fetch_cls = fetch.get_fetch_class(cls.name)
        if fetch_cls:
            fetch_obj = fetch_cls()

# Generated at 2022-06-13 00:12:14.706613
# Unit test for function get_ansible_collector
def test_get_ansible_collector():

    from ansible.module_utils.facts.namespace import PrefixFactNamespace

    # A simple mock ansible_collector.  Just adds the namespace in to the facts.
    class Mock_FactNamespaceCollector(collector.BaseFactCollector):
        # returns {'linux': {'ansible_facts': {'my_fact': {'key': 'value'}}}}
        def collect(self, module=None, collected_facts=None):
            return {'my_fact': {'key': 'value'}}

    all_collector_classes = [Mock_FactNamespaceCollector]

    # gsubset all should return all facts

# Generated at 2022-06-13 00:12:17.707211
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    # this is just a test, there shouldn't be a setup
    assert not collector.setup_done
    assert not collector.all_collectors

# Generated at 2022-06-13 00:12:29.398035
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    import ansible.module_utils.facts as facts

    class MockFactCollector(collector.BaseFactCollector):
        '''Mock FactCollector returns the same fact_id dict with name: fact_id
        provided.'''

        def __init__(self, collectors=None, namespace=None, fact_id=None):
            super(MockFactCollector, self).__init__(collectors=collectors, namespace=namespace)
            self.fact_id = fact_id

        def collect(self, module=None, collected_facts=None):
            fact_dict = {self.fact_id: self.fact_id}
            return fact_dict

    # Test with given filter specifier in constructor.
    # Return all facts when filter_spec = '*'

    # Case1: No namespace

# Generated at 2022-06-13 00:12:40.471598
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    from ansible.module_utils.facts import collector as collector_module
    from ansible.module_utils.facts.system import distribution as distribution_module
    from ansible.module_utils.facts import namespace as namespace_module

    ansible_collector = AnsibleFactCollector(
        collectors=[distribution_module.DistributionCollector(
            namespace=namespace_module.PrefixFactNamespace(prefix='ansible_'))],
        namespace=namespace_module.PrefixFactNamespace(prefix='ansible_'))


# Generated at 2022-06-13 00:12:48.335579
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():

    import copy

    class TestCollector(collector.BaseFactCollector):
        '''Collector that returns a predefined set of facts.'''

        _fact_ids = set(['A', 'B'])

        def collect(self, module=None, collected_facts=None):
            return {'A': 'a', 'B': 'b'}

    class TestCollector2(collector.BaseFactCollector):
        '''Collector that returns a predefined set of facts.'''

        _fact_ids = set(['C', 'D'])

        def collect(self, module=None, collected_facts=None):
            return {'C': 'c', 'D': 'd'}

    def test_collector_none_filter(fact_collector):
        '''Single TestCollector, no filter.'''

        collected

# Generated at 2022-06-13 00:12:59.581130
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    import os
    os.environ['ANSIBLE_COLLECTIONS_PATHS'] = os.path.join(os.getcwd(), 'test/unit/ansible_collections/ns')

    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts.namespace import SuffixFactNamespace
    from ansible.module_utils.facts import collector

    global filter_spec
    filter_spec = ['*']

    global ns_list

# Generated at 2022-06-13 00:13:17.353344
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():

    # mock '_collect', replacing it with a function that just returns a dict
    # with a single entry in it.
    def _collect(self, module=None, collected_facts=None):
        return {'foo': 'bar'}

    old_collect = AnsibleFactCollector._collect
    AnsibleFactCollector._collect = _collect

    # Create a instance object and call a method, the method will be override.
    fact_collector = AnsibleFactCollector()
    results = fact_collector.collect()

    # Restore the orignal method '_collect'
    AnsibleFactCollector._collect = old_collect

    assert results == {'foo': 'bar'}

# Generated at 2022-06-13 00:13:22.505810
# Unit test for function get_ansible_collector
def test_get_ansible_collector():

    fact_collector = \
        get_ansible_collector(all_collector_classes=collector.collector_classes,
                              gather_subset='all',
                              minimal_gather_subset=collector.MINIMAL_GATHER_SUBSET)

    assert isinstance(fact_collector, AnsibleFactCollector)
    assert len(fact_collector.collectors) > 1

# Generated at 2022-06-13 00:13:23.636057
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    # TODO: Need to implement unit tests for this class
    pass



# Generated at 2022-06-13 00:13:29.608194
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():

    # mock the module to make it return a predictable fact set
    mock_module = Mock()
    mock_module.params = {}

    class MockCollector:

        def __call__(self):
            return self

        def collect(self, module=None, collected_facts=None):

            # a single fact
            return {'foo': 'bar'}

    fact_collector = AnsibleFactCollector(collectors=[MockCollector()])
    collected_facts = fact_collector.collect(module=mock_module)

    # test for expected keys and values
    assert 'ansible_facts' in collected_facts
    assert 'foo' in collected_facts['ansible_facts']
    assert collected_facts['ansible_facts']['foo'] == 'bar'



# Generated at 2022-06-13 00:13:38.104897
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    class TestCollector(collector.BaseFactCollector):
        fact_ids = set(['a', 'b', 'c'])

        def collect(self, module=None, collected_facts=None):
            return {'a': 1, 'b': 2, 'c': 3}

    test_collector = TestCollector(namespace=collector.BaseFactNamespace())
    fact_collector = AnsibleFactCollector(collectors=[test_collector],
                                          namespace=collector.BaseFactNamespace())

    result = fact_collector.collect()
    assert result == {'a': 1, 'b': 2, 'c': 3}



# Generated at 2022-06-13 00:13:43.270308
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    class Collector1(collector.BaseFactCollector):
        name = 'one'
        _fact_ids = set(['foo'])

        def collect(self, module=None, collected_facts=None):
            return {'foo': 'bar'}

    class Collector2(collector.BaseFactCollector):
        name = 'two'
        _fact_ids = set(['baz'])

        def collect(self, module=None, collected_facts=None):
            return {'baz': 'qux'}

    all_collector_classes = [Collector1, Collector2]
    fact_collector = get_ansible_collector(gather_subset=['two'],
                                           all_collector_classes=all_collector_classes)
    facts = fact_collector.collect()
   

# Generated at 2022-06-13 00:13:44.818035
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():

    fact_collector = AnsibleFactCollector(collectors=None)

    assert fact_collector.collect() == {}

# Generated at 2022-06-13 00:13:52.053210
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    import unittest
    import itertools
    import json
    import os

    from ansible.module_utils.facts.collector.hardware import HardwareCollector
    from ansible.module_utils.facts.collector.network import NetworkCollector
    from ansible.module_utils.facts.collector.virtual import VirtualCollector
    from ansible.module_utils.facts.collector.facter import FacterCollector
    from ansible.module_utils.facts.collector.ohai import OhaiCollector

    class TestAnsibleFactCollector(unittest.TestCase):

        def setUp(self):
            self.hardware_collectors = HardwareCollector()
            self.network_collectors = NetworkCollector()
            self.virtual_collectors = VirtualCollector()
            self.facter_collectors

# Generated at 2022-06-13 00:13:58.190005
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():

    class SimpleFactCollector(collector.BaseFactCollector):
        def __init__(self, name, namespace):
            super(SimpleFactCollector, self).__init__(namespace=namespace)
            self.name = name

        def collect(self, module=None, collected_facts=None):
            return {self.name: 1}

    class EmptyFactCollector(collector.BaseFactCollector):
        def __init__(self, name, namespace):
            super(EmptyFactCollector, self).__init__(namespace=namespace)
            self.name = name

        def collect(self, module=None, collected_facts=None):
            return {}


# Generated at 2022-06-13 00:14:02.808851
# Unit test for function get_ansible_collector
def test_get_ansible_collector():     # pragma: no cover
    from ansible.module_utils.facts import ansible_local
    from ansible.module_utils.facts import ansible_network
    from ansible.module_utils.facts import ansible_distribution
    from ansible.module_utils.facts import ansible_system
    from ansible.module_utils.facts import ansible_virtualization
    from ansible.module_utils.facts import ansible_pkg_mgr

    all_collector_classes = [
        ansible_local.LocalFactCollector,
        ansible_network.NetworkFactCollector,
        ansible_distribution.DistributionFactCollector,
        ansible_system.SystemFactCollector,
        ansible_virtualization.VirtualizationCollector,
        ansible_pkg_mgr.PackageManagerFactCollector,
    ]

# Generated at 2022-06-13 00:14:16.487462
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    import types

    class Collector1(collector.BaseFactCollector):
        def collect(self, module=None, collected_facts=None):
            return {'facts': 'from_collector1'}

    class Collector2(collector.BaseFactCollector):
        def collect(self, module=None, collected_facts=None):
            return {'facts': 'from_collector2'}

    c1 = Collector1()
    c2 = Collector2()

    fact_collector = AnsibleFactCollector()
    fact_collector.collectors = [c1, c2]
    facts = fact_collector.collect()

    assert isinstance(facts, dict)
    assert 'from_collector1' in facts
    assert 'from_collector2' in facts

# Generated at 2022-06-13 00:14:17.237819
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    pass
    # TODO

# Generated at 2022-06-13 00:14:26.200812
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    import ansible.module_utils.facts.collector.command
    import ansible.module_utils.facts.namespace

    fact_ns = ansible.module_utils.facts.namespace.PrefixFactNamespace(prefix='ansible_')
    sys_collector = ansible.module_utils.facts.collector.command.SysInfoCollector(namespace=fact_ns)
    ansible_fact_collector = AnsibleFactCollector(collectors=[sys_collector])
    facts = ansible_fact_collector.collect()
    assert 'ansible_osc' in facts

# Generated at 2022-06-13 00:14:33.932789
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():

    import time
    import random
    import string

    letters = string.ascii_lowercase

    class BaseCollectorTest(collector.BaseFactCollector):
        '''Simple base collector helper class for testing'''

        def __init__(self, name=None, namespace=None):
            super(BaseCollectorTest, self).__init__(namespace=namespace)
            self.name = name

        def collect(self, module=None, collected_facts=None):
            return {self.name: random.choice(letters)}

    class PrefixCollectorTest(collector.BaseFactCollector):
        '''Simple prefixed collector helper class for testing'''

        def __init__(self, name=None, namespace=None):
            super(PrefixCollectorTest, self).__init__(namespace=namespace)


# Generated at 2022-06-13 00:14:44.045183
# Unit test for function get_ansible_collector
def test_get_ansible_collector():

    from . import all_collectors

    all_collector_classes = all_collectors.collector_classes()

    ansible_fact_collector = \
        get_ansible_collector(all_collector_classes=all_collector_classes,
                              gather_subset=['all'])

    # Note: The fact dictionary also has ansible_facts.some_fact_name
    fact_data = ansible_fact_collector.collect_with_namespace()

    assert 'ansible_facts' in fact_data
    assert 'gather_subset' in fact_data
    assert 'module_setup' in fact_data

# Generated at 2022-06-13 00:14:48.550744
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    collectors = []
    namespace = collector.BaseFactNamespace()
    fact_collector = AnsibleFactCollector(collectors=collectors, namespace=namespace)

    collected_facts = fact_collector.collect()
    assert collected_facts == {}, \
        'Collected facts should be empty when no collectors have been specified'

# Generated at 2022-06-13 00:14:57.513899
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    class CollectorA(collector.BaseFactCollector):
        name = 'A'
        _fact_ids = set([])
        def collect(self, module=None, collected_facts=None):
            return {}

    class CollectorB(collector.BaseFactCollector):
        name = 'B'
        _fact_ids = set([])
        def collect(self, module=None, collected_facts=None):
            return {'a': 'a'}

    class CollectorC(collector.BaseFactCollector):
        name = 'C'
        _fact_ids = set([])
        def collect(self, module=None, collected_facts=None):
            return {'b': 'b'}

    class CollectorD(collector.BaseFactCollector):
        name = 'D'

# Generated at 2022-06-13 00:15:09.107615
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    import ansible.module_utils.facts.collectors
    import ansible.module_utils.facts.namespace

    all_collector_classes = [ansible.module_utils.facts.collectors.DistributionCollector,
                             ansible.module_utils.facts.collectors.LocalSubnetCollector,
                             ansible.module_utils.facts.collectors.NetworkCollector,
                             ansible.module_utils.facts.collectors.PlatformCollector,
                             ansible.module_utils.facts.collectors.SystemCollector]

    filter_spec = ['ansib*']
    namespace = ansible.module_utils.facts.namespace.PrefixFactNamespace(prefix='ansible_')


# Generated at 2022-06-13 00:15:20.492218
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    # Utility function to check the names of the fact collectos in fact_collector
    # and verify that expected_fact_collector_names match.
    def check_fact_collectors(fact_collector, expected_fact_collector_names):
        fact_collector_names = [f.name for f in fact_collector.collectors]
        if set(fact_collector_names) != set(expected_fact_collector_names):
            raise AssertionError('Expected the names of the fact collectors in fact_collector '
                                 'to be %r, but got %r' % (expected_fact_collector_names,
                                                           fact_collector_names))

    # setup
    class FakeCollector1(collector.BaseFactCollector):
        name = 'fake1'


# Generated at 2022-06-13 00:15:28.203498
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    import ansible.module_utils.facts.network.linux

    class FakeFactCollector(collector.BaseFactCollector):
        name = 'FakeFactCollector'
        _fact_ids = ['fake_fact']

        def collect(self):
            return {
                'fake_fact': 'fake_value',
            }

    fact_collector = \
        AnsibleFactCollector(
            collectors=[
                FakeFactCollector(),
                ansible.module_utils.facts.network.linux.LinuxNetworkCollector()
            ],
            filter_spec='ansible_eth*'
        )
    modules_setup_facts = {
        'ansible_module_setup': True,
    }

    collected_facts = fact_collector.collect(collected_facts=modules_setup_facts)


# Generated at 2022-06-13 00:15:40.944660
# Unit test for function get_ansible_collector
def test_get_ansible_collector():  # noqa
    # NOTE: this test assumes gather_subset='all' is the same as ['all']
    gather_subset = ['all']

    collectors = get_ansible_collector(all_collector_classes=collector.collector_classes).collectors

    assert len(collectors) == 1

    assert isinstance(collectors[0], AnsibleFactCollector)

    assert collectors[0].collectors

    assert len(collectors[0].collectors) == len(collector.collector_classes)

    assert collectors[0].collectors[0].name == 'facter'
    assert collectors[0].collectors[1].name == 'ohai'
    assert collectors[0].collectors[2].name == 'pip'
    assert collectors[0].collectors[3].name == 'pkg_mgr'


# Generated at 2022-06-13 00:15:46.072308
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    # stub for collector classes
    class StubCollector(collector.BaseFactCollector):
        def collect(self):
            return {'ansible_Foo': 'bar'}

    fact_collector = AnsibleFactCollector(collectors=[StubCollector()])
    facts_dict = fact_collector.collect()
    assert facts_dict == {'ansible_facts' : {'ansible_Foo': 'bar'},
                          'ansible_gather_subset': ['all'],
                          'ansible_module_setup': True}


# Generated at 2022-06-13 00:15:56.664400
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    class MockCollector(collector.BaseFactCollector):
        def __init__(self):
            pass

        def collect_with_namespace(self, module=None, collected_facts=None):
            return {'fact_1': 'value_1', 'fact_2': 'value_2', 'fact_3': 'value_3'}

    class MockNamespace(object):
        def __init__(self):
            pass

        def namespace_data(self, value):
            return 'namespace_fact_%s' % value

    # Test 1: test with no namespace, no filter, no collected_facts
    collector_1 = AnsibleFactCollector(collectors=[MockCollector()])

# Generated at 2022-06-13 00:16:05.734488
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    class FakeCheeseFactCollector(collector.BaseFactCollector):
        name = 'cheese'
        _fact_ids = set(['cheese'])
        def collect(self, module=None, collected_facts=None):
            return {'cheese': 'cheddar'}

    class FakeFooFactCollector(collector.BaseFactCollector):
        name = 'foo'
        _fact_ids = set(['foo'])
        def collect(self, module=None, collected_facts=None):
            return {'foo': 'bar'}

    module = None
    collected_facts = None

    collectors = [
        FakeFooFactCollector(),
        FakeCheeseFactCollector(),
    ]

    filter_spec = ['cheese', 'foo']

# Generated at 2022-06-13 00:16:15.617990
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    # Note: We can only test the filter_spec option since we have no idea
    # what facts each of the collectors may return.
    class TestFactCollector(collector.BaseFactCollector):
        def collect(self, module=None, collected_facts=None):
            # Note: Don't prepend the namespace to the key (returned) here
            # since the FactCollector will do that for us.
            return {'test_fact': 'test_value'}

    test_collector = TestFactCollector(namespace=None)
    test_fact_collector = \
        AnsibleFactCollector(collectors=[test_collector],
                             filter_spec=['test_fact'])

    result = test_fact_collector.collect()
    assert result == {'test_fact': 'test_value'}




# Generated at 2022-06-13 00:16:27.072099
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    from ansible.module_utils.facts import default

    all_collector_classes = default.GATHER_SUBSET_ALL.values()

    # NOTE: These collector classes do not implement all abstract methods. Do not use for anything
    # other than testing!
    class MockCollector1(collector.BaseFactCollector):
        name = 'mock_collector_1'
        _fact_ids = set([])

        def collect(self, module=None, collected_facts=None):
            return {}

    class MockCollector2(collector.BaseFactCollector):
        name = 'mock_collector_2'
        _fact_ids = set([])

        def collect(self, module=None, collected_facts=None):
            return {}

    mock_fact_collector = \
        get_ansible_collect

# Generated at 2022-06-13 00:16:34.803693
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    from ansible.module_utils.facts import namespace
    test_collector_classes = [
        collector.FacterFactCollector,
        collector.OhaiFactCollector,
        collector.SystemdFactCollector,
        collector.PuppetFactCollector,
        collector.DarwinFactCollector,
        collector.LinuxHardwareInfoFactCollector,
        collector.NetInfoFactCollector,
        collector.NetworkFactCollector,
        collector.VirtualFactCollector,
        collector.DistributionFactCollector,
        collector.PlatformFactCollector,
        collector.PythonFactCollector,
        collector.CommandLineFactCollector
    ]


# Generated at 2022-06-13 00:16:45.424931
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():

    import ansible.module_utils.facts.namespace

    class A(collector.BaseFactCollector):
        name = 'a'
        _fact_ids = set(['a1', 'a2'])

        def collect(self, module=None, collected_facts=None):
            return {'a1': 'a1', 'a2': 'a2'}

    class B(collector.BaseFactCollector):
        name = 'b'
        _fact_ids = set(['b1', 'b2'])

        def collect(self, module=None, collected_facts=None):
            return {'b1': 'b1', 'b2': 'b2'}

    class C(collector.BaseFactCollector):
        name = 'c'

# Generated at 2022-06-13 00:16:51.553695
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    '''test that get_ansible_collector returns a fact collector'''
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.collector import collector as c

    all_collectors = c.default_collectors
    ansible_fact_collector = \
        get_ansible_collector(all_collector_classes=all_collectors,
                              namespace=None,
                              filter_spec=None,
                              gather_subset=None,
                              gather_timeout=None,
                              minimal_gather_subset=None)

    assert isinstance(ansible_fact_collector, AnsibleFactCollector)
    assert isinstance(ansible_fact_collector.collectors, list)

# Generated at 2022-06-13 00:16:53.151562
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():

    fact_collector = AnsibleFactCollector()

    assert fact_collector.collect() == {}



# Generated at 2022-06-13 00:17:15.281308
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    import ansible.module_utils.facts.collector.test_collector

    ansible_collector = get_ansible_collector(all_collector_classes=[ansible.module_utils.facts.collector.test_collector.TestCollector],
                                              gather_subset=['!all', '!minimal'],
                                              minimal_gather_subset=['all'])

    for c in ansible_collector.collectors:
        print(c)

    assert len(ansible_collector.collectors) == 3



# Generated at 2022-06-13 00:17:23.036214
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    from ansible.module_utils.facts import namespace
    from ansible.module_utils.facts import network
    from ansible.module_utils.facts import ohai
    from ansible.module_utils.facts import systemd
    from ansible.module_utils.facts.util import load_collector_classes
    from ansible.module_utils.facts import virtual

    class DummyCollector(collector.BaseFactCollector):
        name = "dummy"


# Generated at 2022-06-13 00:17:31.533391
# Unit test for function get_ansible_collector
def test_get_ansible_collector():

    class TestCollector1(collector.BaseFactCollector):
        name = 'test1'
        _fact_ids = set(['test1'])

        def collect(self, module=None, collected_facts=None):
            return dict(test1='1')

    class TestCollector2(collector.BaseFactCollector):
        name = 'test2'
        _fact_ids = set(['test2', 'test3'])

        def collect(self, module=None, collected_facts=None):
            return dict(test2='2', test3='3')

    class TestCollector3(collector.BaseFactCollector):
        name = 'test3'
        _fact_ids = set(['test4'])


# Generated at 2022-06-13 00:17:37.464422
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():

    import  mock
    from ansible.module_utils.facts import ansible_collector
    from ansible.module_utils.facts import ansible_local
    from ansible.module_utils.facts import ansible_network

    class TestCollector(object):

        def collect(self):
            return {'test_collector': {'fact': 'dict'}}

    collector_obj = TestCollector()
    fact_collector = ansible_collector.AnsibleFactCollector(collectors=[collector_obj])
    facts = fact_collector.collect()
    assert facts == {'ansible_facts': {'test_collector': {'fact': 'dict'}}}

    namespace = ansible_local.LocalNamespace()

# Generated at 2022-06-13 00:17:48.136519
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    # patch the collector classes
    import ansible.module_utils.facts.collector.hardware

    class MockHardwareCollector1(ansible.module_utils.facts.collector.hardware.HardwareCollector):
        name = 'hardware1'

    class MockHardwareCollector2(ansible.module_utils.facts.collector.hardware.HardwareCollector):
        name = 'hardware2'

    def side_effect_hardware_collector_class_factory(*args, **kwargs):
        if args[0] == 'hardware1':
            return MockHardwareCollector1
        elif args[0] == 'hardware2':
            return MockHardwareCollector2
        else:
            raise Exception('unexpected args[0], %s' % args[0])


# Generated at 2022-06-13 00:17:50.568150
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    print(get_ansible_collector.__doc__)
    print(get_ansible_collector(None))


if __name__ == '__main__':
    test_get_ansible_collector()

# Generated at 2022-06-13 00:17:55.721599
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    from ansible.module_utils.facts import default
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    # import default collectors
    dummy_a = default.DummyFactCollectorA()
    dummy_b = default.DummyFactCollectorB()

    fact_collector = AnsibleFactCollector(collectors=[dummy_a, dummy_b],
                                          namespace=PrefixFactNamespace(prefix='ansible_'))
    fact_dict = fact_collector.collect()

    assert fact_dict['ansible_fakefacta'] == 'fake value'
    assert fact_dict['ansible_fakefactb'] == 'fake value'

# Generated at 2022-06-13 00:18:08.304581
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    from ansible_collections.ansible.community.plugins.module_utils import facts
    from ansible.module_utils.facts import collectors as collect_mod
    # Simple test to make sure function compiles
    fact_collector = get_ansible_collector(all_collector_classes=facts.FACT_CACHE,
                                           gather_subset=['all'],
                                           filter_spec=['ansible_*'],
                                           namespace=None)

    assert isinstance(fact_collector, facts.AnsibleFactCollector)
    assert isinstance(fact_collector.collectors, list)
    for collector in fact_collector.collectors:
        assert isinstance(collector, collect_mod.BaseFactCollector)

# Generated at 2022-06-13 00:18:17.676117
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    from ansible.module_utils.facts import collector
    from ansible.module_utils.facts import default
    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils.facts import network
    from ansible.module_utils.facts import network_collectors

    # get all the collector classes
    all_collector_classes = set()
    for collector_classes in [default_collectors.collector_classes,
                              network_collectors.collector_classes]:

        all_collector_classes.update(collector_classes)

    # Just some random subset to use in the tests.
    gather_subset = ['all', 'hardware', 'default']

# Generated at 2022-06-13 00:18:22.356406
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    from ansible.module_utils.facts import namespace
    class DummyCollector(collector.BaseFactCollector):
        def collect(self, module=None, collected_facts=None):
            return {'ansible_foo': {'bar': 1}}

    dum = DummyCollector(namespace=namespace.PrefixFactNamespace(prefix='ansible_'))
    c = AnsibleFactCollector(collectors=[dum], filter_spec='*')
    o = c.collect()
    assert o['ansible_foo']['bar'] == 1
    assert len(o) == 1



# Generated at 2022-06-13 00:19:00.116522
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    # Test when filter_spec=None,
    # all facts should be returned
    collectors = []
    ns = collector.BaseFactNamespace('ns')

    fact = collector.FactsBase('fact1', 0, '', '1', '', '', '', '')
    fact_collector = collector.BaseFactCollector([fact], ns)
    collectors.append(fact_collector)

    fact = collector.FactsBase('fact2', 0, '', '2', '', '', '', '')
    fact_collector = collector.BaseFactCollector([fact], ns)
    collectors.append(fact_collector)

    filter_spec = None
    fact_collector = \
        AnsibleFactCollector(collectors=collectors,
                             filter_spec=filter_spec,
                             namespace=None)

   

# Generated at 2022-06-13 00:19:04.865807
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    class Collect(object):
        name = 'test'

        def collect(self, module=None, collected_facts=None):
            return {self.name: 'test'}

    collect = Collect()

    fact_collector = \
        AnsibleFactCollector(collectors=[collect])

    collected_facts = fact_collector.collect()

    correct_facts = {'ansible_facts': {'test': 'test'}}

    assert collected_facts == correct_facts

# Generated at 2022-06-13 00:19:09.618071
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    import ansible.module_utils.facts.collectors.network
    collectors = [ansible.module_utils.facts.collectors.network.NetworkCollector()]
    collector = AnsibleFactCollector(collectors=collectors)
    facts_dict = collector.collect()
    assert 'ansible_all_ipv4_addresses' in facts_dict
    assert 'ansible_all_ipv6_addresses' in facts_dict


# Generated at 2022-06-13 00:19:19.618482
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    from ansible.module_utils.facts import cache
    from ansible.module_utils.facts import network
    from ansible.module_utils.facts import systemd
    from ansible.module_utils.facts import virtual
    from ansible.module_utils.facts import hardware
    from ansible.module_utils.facts import ohai
    from ansible.module_utils.facts import assemblies
    import ansible.module_utils.facts.collector.facter


# Generated at 2022-06-13 00:19:24.887622
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():

    # We don't have any collectors, so just return an empty dict
    fc = AnsibleFactCollector(collectors=[])

    res = fc.collect()

    assert len(res) == 0

    # Dummy collector class
    class DummyCollector:

        def __init__(self, namespace=None):
            self.results = {'a': 'a_value', 'b': 'b_value'}
            self.namespace = namespace

        def collect_with_namespace(self, module=None, collected_facts=None):
            return self.results

    # We have two dummy collectors with no namespace
    fc = AnsibleFactCollector(collectors=[DummyCollector(), DummyCollector()])
    res = fc.collect()
    assert len(res) == 4

# Generated at 2022-06-13 00:19:35.584487
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    import ansible.module_utils.facts.facts
    collector_classes = ansible.module_utils.facts.facts.collector_classes

    fact_collector = get_ansible_collector(all_collector_classes=collector_classes,
                                           gather_subset={'all', 'test_subset'})
    collected_facts = fact_collector.collect()

    # assert that the result dict has 'ansible_fact' top level key
    assert 'ansible_facts' in collected_facts

    # assert that gather_subset metadata fact is present
    metadata_facts = ['gather_subset', 'module_setup']
    assert all([fact in collected_facts['ansible_facts'] for fact in metadata_facts])

    # verify the facts that are expected to be collected based on gather_subset settings
    fact