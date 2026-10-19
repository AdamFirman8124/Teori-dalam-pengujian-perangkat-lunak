

# Generated at 2022-06-13 00:09:54.226753
# Unit test for method collect of class CollectorMetaDataCollector
def test_CollectorMetaDataCollector_collect():

    expected_facts = {'gather_subset': ['all']}

    actual_facts = CollectorMetaDataCollector(
            gather_subset=['all'],
            module_setup=True
        ).collect(
            module=None,
            collected_facts=None
        )

    assert expected_facts == actual_facts

# Generated at 2022-06-13 00:09:59.609601
# Unit test for method collect of class CollectorMetaDataCollector
def test_CollectorMetaDataCollector_collect():
    gather_subsets = ['all']
    module_setup = True
    # test for collect method of class CollectorMetaDataCollector
    c = CollectorMetaDataCollector(gather_subset=gather_subsets, module_setup=module_setup)
    assert c.collect() == {'gather_subset': ['all'], 'module_setup': True}

# Generated at 2022-06-13 00:10:10.047430
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    import ansible.module_utils.facts.collector
    import ansible.module_utils.facts.collectors.network.linux
    import ansible.module_utils.facts.collectors.system.distribution
    import ansible.module_utils.facts.collectors.system.fqdn
    import ansible.module_utils.facts.collectors.system.platform
    import ansible.module_utils.facts.collectors.system.pkg_mgr

    minimal_gather_subset = frozenset()
    filter_spec = []
    gather_subset = ['all']
    module_setup = True
    gather_timeout = 1
    default_timeout = 30
    timeout.DEFAULT_GATHER_TIMEOUT = default_timeout

    # test timeout set to 1 second

# Generated at 2022-06-13 00:10:21.092914
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    from ansible.module_utils.facts.collector import get_all_collector_classes
    from ansible.module_utils.facts.collector import BASE_COLLECTORS
    from ansible.module_utils.facts.collector import NetworkCollector
    from ansible.module_utils.facts.collector import SetupCollector

    all_collector_classes = get_all_collector_classes()
    collector = get_ansible_collector(all_collector_classes,
                                      gather_subset=['all', 'network', 'hardware'],
                                      filter_spec=['!facter', '!ohai'],
                                      gather_timeout=1,
                                      minimal_gather_subset=frozenset(['all']))
    # Make sure we have the right number of collectors

# Generated at 2022-06-13 00:10:32.780475
# Unit test for method collect of class CollectorMetaDataCollector
def test_CollectorMetaDataCollector_collect():
    import json
    import sys
    import os
    import inspect

    # Skip if not running tests
    if 'test' not in sys.argv[0]:
        return

    # Import needed module
    from ansible.module_utils.facts.system.base import BaseFactCollector

    # Hack needed to allow a module to be loaded from a subdirectory of a python package
    ansible_base_directory = os.path.dirname(inspect.getfile(BaseFactCollector))
    test_base_directory = os.path.join(ansible_base_directory, 'tests')
    sys.path.append(test_base_directory)
    from test_CollectorMetaDataCollector import dummy_BaseFactCollector

    gather_subset = ['all']
    minimal_gather_subset = frozenset()
    module_setup

# Generated at 2022-06-13 00:10:39.182372
# Unit test for method collect of class CollectorMetaDataCollector
def test_CollectorMetaDataCollector_collect():
    gather_subset = ['foo', 'bar']
    module_setup = True
    expected_result = {'gather_subset': ['foo', 'bar'], 'module_setup': True}
    test_collector = CollectorMetaDataCollector(gather_subset=gather_subset, module_setup=module_setup)
    result = test_collector.collect()
    assert result == expected_result


# Generated at 2022-06-13 00:10:52.094613
# Unit test for method collect of class CollectorMetaDataCollector
def test_CollectorMetaDataCollector_collect():
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts.namespace import NamespaceCollector

    test_fact_name = 'test_meta_data'
    test_fact_value = {'a': 1, 'b': '2'}

    class TestFactCollector(NamespaceCollector):

        name = test_fact_name

        def collect(self, module=None, collected_facts=None):
            return test_fact_value

    test_namespace = PrefixFactNamespace(prefix='test_')
    test_collector = TestFactCollector(namespace=test_namespace)
    test_metadata_collector = \
        CollectorMetaDataCollector(collectors=[test_collector],
                                   namespace=test_namespace)


# Generated at 2022-06-13 00:10:59.918541
# Unit test for method collect of class CollectorMetaDataCollector
def test_CollectorMetaDataCollector_collect():
    all_collector_classes = []
    gather_subset = 'all'
    namespace = None
    gather_timeout = None
    minimal_gather_subset = frozenset()

    # invokes the collet method of CollectorMetaDataCollector
    collector_meta_data_collector = get_ansible_collector(all_collector_classes,
                                                          namespace,
                                                          filter_spec=[],
                                                          gather_subset=gather_subset,
                                                          gather_timeout=gather_timeout,
                                                          minimal_gather_subset=minimal_gather_subset)
    # should succeed
    assert collector_meta_data_collector.collect() == {
        'gather_subset': 'all',
        'module_setup': True
    }

# Generated at 2022-06-13 00:11:04.304430
# Unit test for method collect of class CollectorMetaDataCollector
def test_CollectorMetaDataCollector_collect():
    """ Unit test: test_CollectorMetaDataCollector_collect """
    import sys
    import io
    import pytest
    from ansible.module_utils.facts import collector

    sys.stdout = io.StringIO()

    # Create instance
    test_instance = collector.CollectorMetaDataCollector(collectors=None,
                                                         namespace=None,
                                                         gather_subset=None,
                                                         module_setup=None)

    # get collect() result
    test_result = test_instance.collect()

    # Compare our expectation with the result
    assert test_result == {'gather_subset': None}

    # Reset stdout
    sys.stdout = sys.__stdout__


# Generated at 2022-06-13 00:11:15.410194
# Unit test for method collect of class CollectorMetaDataCollector
def test_CollectorMetaDataCollector_collect():
    for gather_subset in [None, 'all', 'min', ['network'], ['network', 'hardware']]:
        for module_setup in [True, False]:
            for namespace in ['', 'ansible_', 'ansible_fake_']:
                collector_meta_data_collector = CollectorMetaDataCollector(
                    gather_subset=gather_subset,
                    module_setup=module_setup,
                    namespace=namespace)
                fact_dict = collector_meta_data_collector.collect()
                assert fact_dict['gather_subset'] == gather_subset
                assert fact_dict['module_setup'] == module_setup
                if module_setup:
                    if namespace:
                        assert fact_dict[namespace + 'gather_subset'] == gather_subset

# Generated at 2022-06-13 00:11:27.117818
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    global_prefix = ['global_prefix_']
    fact_collector = \
        get_ansible_collector(global_prefix)


# For backwards compatibility, use this as the default fact collector.
# This will collect facts for all gatherers
# and create a fact for gather_subset.
ansible_collector = AnsibleFactCollector

# Helper function to get the ansible fact collector
# for backwards compatibility.

# Generated at 2022-06-13 00:11:35.264613
# Unit test for function get_ansible_collector
def test_get_ansible_collector():

    test_collector_classes = ['Network', 'Hardware', 'Platform']
    test_gather_subset = ['min', '!network']
    test_minimal_gather_subset = ['!network']
    test_gather_timeout = 1
    test_filter_spec = ['ansible_f*', 'ansible_os_family']

    fact_collector = get_ansible_collector(all_collector_classes=test_collector_classes,
                                           gather_subset=test_gather_subset,
                                           gather_timeout=test_gather_timeout,
                                           minimal_gather_subset=test_minimal_gather_subset,
                                           filter_spec=test_filter_spec)

    # check for our custom collector

# Generated at 2022-06-13 00:11:45.170908
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    """
    Unit test for method collect of class AnsibleFactCollector

    """
    class SampleCollector(collector.BaseFactCollector):
        """
        Sample Class for unit test
        """

        def collect(self, module=None, collected_facts=None):
            """
            Sample Method for unit test
            """
            return {'fact1': 'value1', 'fact2': 'value2'}

    fact_collector = AnsibleFactCollector(collectors=[SampleCollector()])
    result = fact_collector.collect()
    assert result == {'fact1': 'value1', 'fact2': 'value2'}


# Generated at 2022-06-13 00:11:49.612851
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    collectors = [collector.BaseFactCollector()]
    fact_collector = AnsibleFactCollector(collectors=collectors)
    ansible_facts = fact_collector.collect()

    assert ansible_facts == {}



# Generated at 2022-06-13 00:11:58.638773
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    '''
    This is a test of the internal function get_ansible_collector().
    The internal function is tested since the API is not stable right now.
    '''

    class FakeCollectorClass:
        def __init__(self, **kwargs):
            self.name = kwargs['name']
            self.called = False

        def collect(self, module=None, collected_facts=None):
            self.called = True
            return {self.name: 'test_value'}

    fake_collector_classes = [FakeCollectorClass(name='test1'), FakeCollectorClass(name='test2')]


# Generated at 2022-06-13 00:12:06.123993
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    import ansible.module_utils.facts.collector
    from ansible.module_utils.facts import _legacy_collectors

    _all_collector_classes = _legacy_collectors + ansible.module_utils.facts.collector.collector_classes

    c = get_ansible_collector(_all_collector_classes)

    facts = c.collect()
    assert facts['gather_subset'] == ['all']
    assert 'module_setup' in facts


# Generated at 2022-06-13 00:12:15.784353
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    try:
        import ansible_facts.aux
        import ansible_facts.identity
        import ansible_facts.system
    except ImportError:
        # Skip this test if we do not have all the available collectors installed
        return

    ansible_collector, = \
        collector.collector_classes_from_gather_subset(
            all_collector_classes=collector.collector_classes(),
            minimal_gather_subset=frozenset(),
            gather_subset=['all'])

    my_collector = \
        get_ansible_collector(all_collector_classes=collector.collector_classes())

    assert isinstance(my_collector, ansible_collector)

if __name__ == '__main__':
    test_get_ansible_collector

# Generated at 2022-06-13 00:12:27.944285
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    import ansible.module_utils.facts.namespace

    # Note: there is no namespace class where the prefix is '' (empty)
    no_namespace = ansible.module_utils.facts.namespace.PrefixFactNamespace(prefix='')


# Generated at 2022-06-13 00:12:39.303935
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    import tempfile
    import os

    # mock gathered facts
    test_facts = {
        "testing1": "testing1",
        "testing2": "testing2",
        "testing3": "testing3",
        "testing_ansible_testing": "testing_ansible_testing",
        "testing_ansible_testing2": "testing_ansible_testing2"
    }
    class AnsibleFactCollectorTest(AnsibleFactCollector):
        def __init__(self, name, module, namespace=None, filter_spec=None):
            super(AnsibleFactCollectorTest, self).__init__(collectors=None,
                                                           namespace=namespace,
                                                           filter_spec=filter_spec)
            self.name = name
            self.module = module


# Generated at 2022-06-13 00:12:45.827231
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    '''Unit test for method collect of class AnsibleFactCollector.'''

    # initialize AnsibleFactCollector with a list of fact_collectors
    fc1 = FakeFactCollector({'a': 'b'})
    fc2 = FakeFactCollector({'c': 'd'})
    fact_collector = AnsibleFactCollector([fc1, fc2])

    # call method collect of AnsibleFactCollector
    result = fact_collector.collect()

    # check that the expected result is returned
    assert len(result) == 2
    assert result == {'a': 'b', 'c': 'd'}



# Generated at 2022-06-13 00:13:01.813330
# Unit test for function get_ansible_collector
def test_get_ansible_collector():

    from ansible.module_utils.facts.system.distribution import Distribution
    from ansible.module_utils.facts.system.distribution import LinuxDistribution
    from ansible.module_utils.facts.system.distribution import PlatformFamily

    class FakeDistribution(Distribution):

        name = 'fake_distro'
        release = 'fake_release'
        id = 'fake_id'
        distro = 'fake_distro'
        version_id = 'fake_version_id'
        codename = 'fake_codename'
        major_version = 'fake_major_version'
        minor_version = 'fake_minor_version'
        build_number = 'fake_build_number'
        platform = 'fake_platform'

        @staticmethod
        def LinuxDistribution_detect():
            return LinuxDistribution

# Generated at 2022-06-13 00:13:12.330485
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():

    from ansible.module_utils.facts.collector.hardware import HardwareFactCollector
    from ansible.module_utils.facts.collector.network import NetworkFactCollector
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.namespace import PrefixFactNamespace

    fact_collector = AnsibleFactCollector(collectors=[HardwareFactCollector(), NetworkFactCollector()])
    ansible_facts = fact_collector.collect()

    n_facts = len(ansible_facts)

    hw_fact_collector = HardwareFactCollector()
    nw_fact_collector = NetworkFactCollector()
    hw_facts = hw_fact_collector.collect()
    nw_facts = nw_fact_collector.collect()

# Generated at 2022-06-13 00:13:22.522162
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    '''Tests the result of collect method of class AnsibleFactCollector'''

    namespace = None
    # TODO: add mock Collector instances and test filter_spec
    gather_subset = None
    gather_timeout = timeout.DEFAULT_GATHER_TIMEOUT
    minimal_gather_subset = frozenset()
    all_collector_classes = frozenset()

    fact_collector = get_ansible_collector(all_collector_classes=all_collector_classes,
                                           minimal_gather_subset=minimal_gather_subset,
                                           namespace=namespace,
                                           gather_subset=gather_subset,
                                           gather_timeout=gather_timeout,
                                           filter_spec=None)

    collected_facts = None
    # TODO

# Generated at 2022-06-13 00:13:32.253039
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    from ansible.module_utils.facts import namespace

    class TestCollector1(collector.BaseFactCollector):
        name = 'test1'
        _fact_ids = set(['test1_fact1', 'test1_fact2'])

        def collect(self, module=None, collected_facts=None):
            return {'test1_fact1': 5, 'test1_fact2': 6}

    class TestCollector2(collector.BaseFactCollector):
        name = 'test2'
        _fact_ids = set(['test2_fact1', 'test2_fact2'])

        def collect(self, module=None, collected_facts=None):
            return {'test2_fact1': 7, 'test2_fact2': 8}


# Generated at 2022-06-13 00:13:43.134301
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    class FooCollector(collector.BaseFactCollector):
        name = 'foo'
        _fact_ids = set(['foo_fact1', 'foo_fact2', 'foo_fact3'])
        def collect(self, module=None, collected_facts=None):
            return {'foo_fact1': {'foo1': 'bar1'}, 'foo_fact2': {'foo2': 'bar2'}}

    # Expected result if there is no filter spec
    expected_collector = {
        'foo_fact1': {'foo1': 'bar1'},
        'foo_fact2': {'foo2': 'bar2'},
    }

    # Expected result if filter_spec='foo*'

# Generated at 2022-06-13 00:13:53.785372
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    '''Unit test for method collect of class AnsibleFactCollector
    '''

    import unittest
    import ansible.module_utils.facts.collector.any_collector as any_collector
    import ansible.module_utils.facts.collector.network as network
    from ansible.module_utils.facts import namespace

    def get_test_any_collector():
        test_namespace = namespace.BaseFactNamespace()  # pylint: disable=assigned-non-slot

        class TestAnyCollector(any_collector.AnyFactCollector):
            name = 'testany'
            _fact_ids = set(['ansible_testany_key'])

            def __init__(self, namespace=None):
                super(TestAnyCollector, self).__init__(namespace=namespace)

# Generated at 2022-06-13 00:13:54.378519
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    pass

# Generated at 2022-06-13 00:14:04.591609
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():

    # import ansible.module_utils.facts.namespace
    from ansible.module_utils.facts import namespace

    class Stub_FactNamespace(namespace.BaseFactNamespace):

        name = 'fact_namespace_test_one'

        def __init__(self, *args, **kwargs):
            super(Stub_FactNamespace, self).__init__(*args, **kwargs)
            self.fact_ids = set(['test_one_foo', 'test_one_bar'])

    class Stub_Collector(collector.BaseFactCollector):

        name = 'fact_namespace_test_one'

        def __init__(self, *args, **kwargs):
            super(Stub_Collector, self).__init__(*args, **kwargs)
            self.fact_ids = set

# Generated at 2022-06-13 00:14:07.380259
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    def collector_mock(s):
        return s
    fact_collector = AnsibleFactCollector(namespace=None, filter_spec=None, collectors=[collector_mock])
    fact_dict = fact_collector.collect(module=None, collected_facts=None)
    assert fact_dict == {'ansible_facts': {'ansible_local': {'test1': 'test1'}}}


# Generated at 2022-06-13 00:14:17.616715
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():

    class Collector:
        def collect_with_namespace(self, module=None, collected_facts=None):
            return {'fact_%d' % self.index: True}

    class Namespace:
        def to_safe(self, key):
            return 'ns_%s' % key

    ImportCollector = Collector
    NetworkCollector = Collector
    PlatformCollector = Collector

    collectors = [ImportCollector(index=1),
                  NetworkCollector(index=2),
                  PlatformCollector(index=3)]

    namespace = Namespace()

    fact_collector = \
        AnsibleFactCollector(collectors=collectors, namespace=namespace)

    results = fact_collector.collect()

# Generated at 2022-06-13 00:14:32.680256
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    class collect:
        def __init__(self, names):
            self._names = names

        def collect(self, module=None, collected_facts=None):

            if not self._names:
                return None

            return {self._names[0]: self._names[0]}

    class Collector:
        def __init__(self, names):
            self._names = names

        def collect(self, module=None, collected_facts=None):

            if not self._names:
                return None

            return {self._names[0]: self._names[0]}

    class CollectorObj:
        def __init__(self, name):
            self._name = name

        @property
        def name(self):
            return self._name


# Generated at 2022-06-13 00:14:45.185325
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    import test.support
    test.support.import_module('ansible.module_utils.facts.collector')

    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts import namespace
    from ansible.module_utils.facts.collector.system import SystemCollector
    from ansible.module_utils.facts.collector.virtual import VirtualCollector
    from ansible.module_utils.facts.collector.pip import PipCollector
    from ansible.module_utils.facts.collector.pkg_mgr import PkgMgrCollector
    from ansible.module_utils.facts.collector.local import LocalCollector

    # create a SystemCollector that returns a useless fact

# Generated at 2022-06-13 00:14:52.681812
# Unit test for function get_ansible_collector
def test_get_ansible_collector():

    # Collect all facts
    fact_collector = get_ansible_collector(all_collector_classes=collector.all_collector_classes())

    # Collect all facts (same as above)
    fact_collector = get_ansible_collector(all_collector_classes=collector.all_collector_classes(),
                                           gather_subset='all')

    # Collect all network facts
    fact_collector = get_ansible_collector(all_collector_classes=collector.all_collector_classes(),
                                           gather_subset='network')

    # Collect only ip facts

# Generated at 2022-06-13 00:14:59.852461
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    fact_namespace = collector.BaseFactNamespace()
    fact_collector = AnsibleFactCollector([], namespace=fact_namespace)
    facts = fact_collector.collect()
    assert facts == {}
    fact_namespace = collector.BaseFactNamespace(prefix='9')
    fact_collector = AnsibleFactCollector([], namespace=fact_namespace)
    facts = fact_collector.collect()
    assert facts == {}
    fact_namespace = collector.BaseFactNamespace(prefix='ansible_')
    fact_collector = AnsibleFactCollector([], namespace=fact_namespace)
    facts = fact_collector.collect()
    assert facts == {}
    fact_collector = AnsibleFactCollector([], filter_spec=['*'])
    facts = fact_collector.collect()


# Generated at 2022-06-13 00:15:11.214964
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    class FakeFactCollector(collector.BaseFactCollector):
        def collect(self, module, collected_facts):
            collected_facts.update({'ansible_fake_1': 'fake_1 value'})
            return {'ansible_fake_1': 'fake_1 value'}

    class FakeFactCollector2(collector.BaseFactCollector):
        def collect(self, module, collected_facts):
            collected_facts.update({'ansible_fake_2': 'fake_2 value'})
            return {'ansible_fake_2': 'fake_2 value'}

    ffc = FakeFactCollector()
    ffc2 = FakeFactCollector2()
    fact_collector = AnsibleFactCollector(collectors=[ffc, ffc2], filter_spec=None)


# Generated at 2022-06-13 00:15:22.622226
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    import ansible.module_utils.facts.hardware
    import ansible.module_utils.facts.default

    try:
        import ansible.module_utils.facts.virtual
        is_virtual_collector_available = True
    except ImportError:
        is_virtual_collector_available = False

    all_collectors = collector.collector_classes() + \
                     [ansible.module_utils.facts.virtual.VirtualCollector,
                      ansible.module_utils.facts.virtual.ZVMVirtualCollector,
                      ansible.module_utils.facts.virtual.VMwareCollector,
                      ansible.module_utils.facts.virtual.OVirtCollector]


# Generated at 2022-06-13 00:15:30.734265
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    from ansible.module_utils import facts
    from ansible.module_utils.facts import collector as facts_collector

    fact_collector = \
        get_ansible_collector(all_collector_classes=facts.get_collector_classes(),
                              gather_subset='all',
                              namespace='ansible')

    assert isinstance(fact_collector, AnsibleFactCollector)
    assert len(fact_collector.collectors) == len(facts_collector.ALL_COLLECTORS)

# Generated at 2022-06-13 00:15:40.745166
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():

    # Test 1. Create a collector with a single fact.
    def test_collector(module, collected_facts):
        return {'test_fact': True}
    test_collector_class = type('TestCollectorClass', (collector.BaseFactCollector,), {'collect': test_collector})
    test_collector_object = test_collector_class()
    fact_collector = AnsibleFactCollector(collectors=[test_collector_object])
    fact_dict = fact_collector.collect()
    assert fact_dict == {'ansible_facts': {'test_fact': True}}

    # Test 2. Create a collector with multiple facts.
    def test_collector2(module, collected_facts):
        return {'test_fact': True, 'another_fact': 42}
    test_collector

# Generated at 2022-06-13 00:15:47.383450
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    import ansible.module_utils.facts.collector.network
    import ansible.module_utils.facts.collector.hardware
    import ansible.module_utils.facts.collector.platform
    import ansible.module_utils.facts.collector.virtual
    import ansible.module_utils.facts.collector.distribution
    import ansible.module_utils.facts.collector.facter
    import ansible.module_utils.facts.collector.systemd
    import ansible.module_utils.facts.collector.pkg_mgr
    import ansible.module_utils.facts.collector.ohai
    import ansible.module_utils.facts.collector.pip


# Generated at 2022-06-13 00:15:55.913466
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    '''
    Unit test for method collect of class AnsibleFactCollector
    '''

    class TestCollector(collector.BaseFactCollector):
        name = 'test'

        def collect(self, module=None, collected_facts=None):
            return {self.name: 'test'}

    fact_collector = \
        AnsibleFactCollector(collectors=[TestCollector()],
                             namespace=None,
                             filter_spec=None)
    # FactCollector has no dependency on a module
    facts = fact_collector.collect(module=None, collected_facts=None)
    assert facts == {'test': 'test'}  # facts are collected without namespace

# Generated at 2022-06-13 00:16:14.488681
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    from ansible.module_utils.facts.collector.kernel import KernelFactCollector
    from ansible.module_utils.facts.collector.distribution import DistributionFactCollector
    from ansible.module_utils.facts.collector.network import NetworkFactCollector

    # Construct with minimal gather_subset=[]
    collector = get_ansible_collector(all_collector_classes=[],
                                      minimal_gather_subset=[],
                                      filter_spec=[],
                                      gather_subset=[],
                                      gather_timeout=1)
    assert len(collector.collectors) == 1

    # Construct with minimal gather_subset=['network']

# Generated at 2022-06-13 00:16:15.043485
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    pass

# Generated at 2022-06-13 00:16:22.383527
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    collector_1 = CollectorMock()
    collector_2 = CollectorMock()
    collector_3 = CollectorMock()

    fact_collector = AnsibleFactCollector([collector_1, collector_2, collector_3],
                                          filter_spec=['fake_fact',
                                                       'ansible_fake_2',
                                                       'ansible_fake_3',
                                                       'ansible_fake_4'])

    module = DummyModule()

    # test case: collect only one fact
    # collector_1 is expected to be called but not collector_2 and collector_3
    # expected fact:
    #       {
    #           'ansible_facts': {
    #               'fake_fact': 'value'
    #           }
    #       }

# Generated at 2022-06-13 00:16:32.480658
# Unit test for function get_ansible_collector
def test_get_ansible_collector():

    from ansible.module_utils.facts.collector import all_collector_classes

    collector_classes = \
        [
            collector_class for collector_class in all_collector_classes()
            if 'Network' in collector_class.__name__
        ]

    gather_subset = ['network', 'network_resources']

    fact_collector = get_ansible_collector(all_collector_classes=collector_classes,
                                           gather_subset=gather_subset,
                                           filter_spec='*interface*',
                                           namespace=None,
                                           gather_timeout=None,
                                           minimal_gather_subset=None)

    collected_facts = fact_collector.collect(module=None, collected_facts=None)

    # print(collected_facts)


# Generated at 2022-06-13 00:16:43.367257
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    # Note: This test is not executed during normal testing as it requires a module_utils/facts/ directory
    #
    # Test that class AnsibleFactCollector works as expected
    # when used for the gather_subset=all
    import sys
    import os

    from ansible.module_utils.facts import timeout
    from ansible.module_utils.facts.freebsd import hardware

    class TestFacts(hardware.Hardware):
        name = 'testfacts'
        fact_ids = ['testfact1', 'testfact2', 'testfact3']

        def __init__(self, collected_facts=None, namespace=None):
            super(TestFacts, self).__init__(collected_facts, namespace)

        def collect(self, module=None, collected_facts=None):
            info_dict = {}
            info

# Generated at 2022-06-13 00:16:47.253803
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    import ansible.module_utils.facts.collector.network as network_collector
    import ansible.module_utils.facts.collector.system as system_collector

    network_collector_obj = network_collector.NetworkFactCollector()
    system_collector_obj = system_collector.SystemFactCollector()

    collectors = [network_collector_obj, system_collector_obj]
    fact_collector = AnsibleFactCollector(collectors)

    facts_dict = fact_collector.collect()

    assert 'all_ipv4_addresses' in facts_dict

# Generated at 2022-06-13 00:16:51.177149
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    ac = AnsibleFactCollector()
    # make sure method collect works when passed None collected_facts
    ac_collect_none = ac.collect(collected_facts=None)

# Generated at 2022-06-13 00:17:01.815890
# Unit test for function get_ansible_collector
def test_get_ansible_collector():

    from ansible.module_utils.facts import cache
    from ansible.module_utils.facts import cache_manager
    from ansible.module_utils.facts import network
    from ansible.module_utils.facts import system
    from ansible.module_utils.facts import virtual

    all_collector_classes = [cache.CacheFactCollector,
                             cache_manager.CacheManagerFactCollector,
                             network.NetworkFactCollector,
                             system.SystemFactCollector,
                             virtual.VirtualFactCollector]


# Generated at 2022-06-13 00:17:09.997573
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    import unittest

    class TestCollector1(collector.BaseFactCollector):
        name = 'test_collector1'
        _fact_ids = set(['ansible_test1', 'ansible_test2'])

        def collect(self, module=None, collected_facts=None):
            return {'ansible_test1': 'test1', 'ansible_test2': 'test2'}

    class TestCollector2(collector.BaseFactCollector):
        name = 'test_collector2'
        _fact_ids = set(['ansible_test3', 'ansible_test4'])

        def collect(self, module=None, collected_facts=None):
            return {'ansible_test3': 'test3', 'ansible_test4': 'test4'}


# Generated at 2022-06-13 00:17:20.543033
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():

    fact_collector = AnsibleFactCollector()

    facts = fact_collector.collect()

    expected_facts = {'fact1': {'fact1': 1, 'fact2': 2, 'fact3': 3, 'fact4': 4},
                      'fact2': {'fact1': 2, 'fact2': 3, 'fact3': 4, 'fact4': 5},
                      'fact3': {'fact1': 3, 'fact2': 4, 'fact3': 5, 'fact4': 6},
                      'fact4': {'fact1': 4, 'fact2': 5, 'fact3': 6, 'fact4': 7}}

    assert(facts == expected_facts)

    # test filtering
    facts = fact_collector.collect(filter_spec=['fact2*'])


# Generated at 2022-06-13 00:17:55.938224
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    all_collector_classes = \
        {'a': MockCollector, 'b': MockCollector, 'c': MockCollector, 'd': MockCollector}
    collector_obj = \
        get_ansible_collector(all_collector_classes=all_collector_classes,
                              minimal_gather_subset=frozenset(['all']),
                              gather_subset=['all', '!a'],
                              gather_timeout=5)
    assert len(collector_obj.collectors) == 3
    assert len(collector_obj.namespaces) == 3
    assert collector_obj.namespaces['b'] == 'ansible_'
    assert collector_obj.namespaces['d'] == 'ansible_'

# Generated at 2022-06-13 00:18:02.853768
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    '''Unit test for get_ansible_collector().'''
    all_collector_classes = collector.get_ansible_collector_classes()
    fact_collector = \
        get_ansible_collector(all_collector_classes=all_collector_classes,
                              filter_spec=[],
                              gather_subset=[],
                              gather_timeout=0,
                              minimal_gather_subset=frozenset())
    assert fact_collector

# Generated at 2022-06-13 00:18:13.024358
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    """
    Test the AnsibleFactCollector.collect method.

    """
    from ansible.module_utils.facts import default
    from ansible.module_utils.facts import default_collectors

    config = default.get_config()

    # TODO: Add CollectorMetaDataCollector to list of collectors?
    all_collector_classes = default.get_collectors_classes(config=config)
    fc = get_ansible_collector(all_collector_classes=all_collector_classes)
    facts_dict = fc.collect(module=None)
    assert isinstance(facts_dict, dict)
    assert facts_dict['gather_subset'] == ['all']

# Generated at 2022-06-13 00:18:22.964564
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    class Collector1(object):
        def collect_with_namespace(self, module=None, collected_facts=None):
            return {'foo': 'bar'}

    class Collector2(object):
        def collect_with_namespace(self, module=None, collected_facts=None):
            return {'bar': u'foo'}

    class Collector3(object):
        def collect_with_namespace(self, module=None, collected_facts=None):
            return {u'ansible_bar': u'foo'}

    class Collector4(object):
        def collect_with_namespace(self, module=None, collected_facts=None):
            return {u'ansible_baz': u'foo'}


# Generated at 2022-06-13 00:18:28.195104
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    def fake_collect_with_namespace(module=None, collected_facts=None):
        return {'test': 'nothing'}

    fake_collector = type('FakeCollector', (object,), {'collect_with_namespace': fake_collect_with_namespace})

    collector = AnsibleFactCollector([fake_collector()])
    facts = collector.collect()
    assert facts['test'] == 'nothing'

# Generated at 2022-06-13 00:18:37.944048
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    # Create a mock namespace
    class MockFactNamespace(object):
        def __init__(self, prefix):
            self.prefix = prefix

        def namespace_id(self):
            return self.prefix

        def namespace_facts(self, facts):
            return facts

    # Create mock facts
    class MockFact(object):
        def __init__(self, namespace, name, value):
            self.namespace = namespace
            self.name = name
            self.value = value

    # Create mock collector
    class MockCollector(collector.BaseFactCollector):
        def __init__(self, namespace=None, filters=None):
            super(MockCollector, self).__init__(namespace=namespace)


# Generated at 2022-06-13 00:18:47.365341
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    from ansible.module_utils.facts.collector.base import BaseFactCollector
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts.collector import memory
    from ansible.module_utils.facts.collector import network


# Generated at 2022-06-13 00:18:54.322604
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    collectors = []
    collector1 = collector.BaseFactCollector()
    collector1.name = 'collector1'
    collector2 = collector.BaseFactCollector()
    collector2.name = 'collector2'

    collector1.collect_with_namespace = \
        lambda module=None, collected_facts=None: \
            {'fact1': 'value1', 'fact2': 'value2'}
    collector2.collect_with_namespace = \
        lambda module=None, collected_facts=None: \
            {'fact3': 'value3', 'fact4': 'value4'}

    collectors.append(collector1)
    collectors.append(collector2)

    fact_collector = AnsibleFactCollector(collectors=collectors)
    facts_dict = fact_collector.collect()



# Generated at 2022-06-13 00:19:03.608468
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    class TestCollector(collector.BaseFactCollector):
        '''Collector for testing only.'''

        name = 'test'
        _fact_ids = set(['test_test'])

        def collect(self, module=None, collected_facts=None):
            return {'test_test': 'test'}

    class TestCollector2(collector.BaseFactCollector):
        '''Collector for testing only.'''

        name = 'test2'
        _fact_ids = set(['test_test2'])

        def collect(self, module=None, collected_facts=None):
            return {'test_test2': 'test2'}

    class TestFilterSpec(object):
        '''Mock object to call method _filter'''


# Generated at 2022-06-13 00:19:04.160261
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    pass

# Generated at 2022-06-13 00:19:43.658131
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    from ansible.module_utils.facts import namespace

    # minimal_gather_subset is the set of collector_class names that are executed when gather_subset is 'minimal'
    minimal_gather_subset = frozenset(['facter'])

    # all_collector_classes is a dict with keys as collector_class names and values as the collector class
    from ansible.module_utils.facts.collector.facter import FacterCollector
    from ansible.module_utils.facts.collector.systemd import SystemdCollector

    all_collector_classes = {
        'facter': FacterCollector,
        'systemd': SystemdCollector,
    }

    # test with gather_subset='all'