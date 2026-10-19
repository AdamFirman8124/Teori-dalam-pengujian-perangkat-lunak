

# Generated at 2022-06-13 00:09:58.948985
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    from ansible.module_utils.facts import cache
    from ansible.module_utils.facts import namespaced_fact
    from ansible.module_utils.facts import timeout

    all_collector_classes = ['ansible.module_utils.facts.cache.FacterFactCache',
                             'ansible.module_utils.facts.cache.OhaiFactCache',
                             'ansible.module_utils.facts.cache.NetworkFactCache',
                             'ansible.module_utils.facts.cache.LocalFactCache']


# Generated at 2022-06-13 00:10:04.721420
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    # Test the filtering of facts
    fact_collector = \
        AnsibleFactCollector(collectors=[collector.FacterCollector()],
                             filter_spec=['ansible_product_name', 'facter_test1', 'test2'],
                             namespace=None)

    # Test the filtering of facts
    facts_dict = fact_collector.collect(module=None, collected_facts={})

    assert facts_dict == {'ansible_product_name': 'core',
                          'ansible_facter_test1': 'testval1',
                          'ansible_test2': 'testval2'}

# Generated at 2022-06-13 00:10:07.672329
# Unit test for method collect of class CollectorMetaDataCollector
def test_CollectorMetaDataCollector_collect():
    collector = CollectorMetaDataCollector(gather_subset=['all'])
    result = collector.collect()
    assert result == {'gather_subset': ['all']}

# Generated at 2022-06-13 00:10:15.650111
# Unit test for method collect of class CollectorMetaDataCollector
def test_CollectorMetaDataCollector_collect():
    '''
    Unit test for method collect of class CollectorMetaDataCollector.
    The method collect shall return a dictionary that contains the value of
    the parameters gather_subset and module_setup.
    '''
    gather_subset = ['all', 'network']
    module_setup = True
    
    # Create the CollectorMetaDataCollector object
    collector_meta_data_collector = CollectorMetaDataCollector(gather_subset=gather_subset, module_setup=module_setup)
    
    # Invoke the method collect on the object
    result = collector_meta_data_collector.collect()
    
    # The dictionary returned by the method collect shall contain the value of the parameters gather_subset and module_setup
    assert result['gather_subset'] == gather_subset
    assert result['module_setup']

# Generated at 2022-06-13 00:10:21.407690
# Unit test for method collect of class CollectorMetaDataCollector
def test_CollectorMetaDataCollector_collect():
    c = CollectorMetaDataCollector(namespace=None,
                                   gather_subset=['foo', 'bar'],
                                   module_setup=False)
    facts = c.collect(module=None, collected_facts=None)
    assert facts['gather_subset'] == ['foo', 'bar']
    assert facts['module_setup'] == False

# Generated at 2022-06-13 00:10:26.864104
# Unit test for method collect of class CollectorMetaDataCollector
def test_CollectorMetaDataCollector_collect():
    c = CollectorMetaDataCollector(gather_subset='things to gather')
    c_dict = c.collect()
    assert c_dict['gather_subset'] == 'things to gather'
    assert c_dict['module_setup'] is True



# Generated at 2022-06-13 00:10:30.498768
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    facts = AnsibleFactCollector().collect()
    assert facts.get('ansible_architecture')
    assert facts.get('ansible_fqdn')
    assert facts.get('ansible_hostname')



# Generated at 2022-06-13 00:10:40.819224
# Unit test for method collect of class CollectorMetaDataCollector
def test_CollectorMetaDataCollector_collect():
    test_collectors = [
        collector.FacterFactCollector(namespace='ansible_facter_'),
        collector.PlatformFactCollector(namespace='ansible_platform_'),
        collector.NetworkCollector(namespace='ansible_network_'),
        CollectorMetaDataCollector(gather_subset='all', module_setup=True)]


# Generated at 2022-06-13 00:10:49.606367
# Unit test for method collect of class CollectorMetaDataCollector
def test_CollectorMetaDataCollector_collect():
    from ansible.module_utils.facts import namespace
    # pylint: disable=unused-variable

    meta_fact_collector = CollectorMetaDataCollector(gather_subset='fake_gather_subset',
                                                     module_setup=True,
                                                     namespace=namespace.PrefixFactNamespace(prefix='ansible_'))
    collected_facts = meta_fact_collector.collect()
    assert collected_facts['ansible_gather_subset'] == 'fake_gather_subset'

# Generated at 2022-06-13 00:10:53.867086
# Unit test for method collect of class CollectorMetaDataCollector
def test_CollectorMetaDataCollector_collect():
    fact_collector = \
        CollectorMetaDataCollector(gather_subset='all',
                                   module_setup=True)
    assert fact_collector.collect() == {'gather_subset': 'all', 'module_setup': True}

# Generated at 2022-06-13 00:11:18.197988
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    import ansible.module_utils.facts.namespace
    import ansible.module_utils.facts.test_utils
    import ansible.module_utils.facts.test_utils.collector_test_cases

    all_namespaces = ansible.module_utils.facts.namespace.get_collected_facts_namespaces()
    all_namespaces.update(ansible.module_utils.facts.test_utils.get_test_namespaces())

    all_collector_classes = ansible.module_utils.facts.namespace.collector_classes_from_namespaces(all_namespaces)
    all_collector_classes.update(ansible.module_utils.facts.test_utils.collector_test_cases.collector_classes_from_test_modules())

    minimal_gather_subset = frozenset

# Generated at 2022-06-13 00:11:25.925039
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector
    class TestCollector(BaseFactCollector):
        name = 'test'
        _fact_ids = set([])
        def collect(self, module=None, collected_facts=None):
            return ['TestCollector']

    class TestCollectorSubclass(TestCollector):
        name = 'test_sub'

    import collections
    import pytest

    fact_collector = AnsibleFactCollector(collectors=[TestCollector(), TestCollectorSubclass()])
    assert fact_collector.collect() == collections.OrderedDict([('test', 'TestCollector'), ('test_sub', 'TestCollector')])

# Generated at 2022-06-13 00:11:29.922437
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    import ansible.module_utils.facts.collector
    collector_obj = ansible.module_utils.facts.collector.FactsCollector()
    collectors_list = [collector_obj]
    fact_collector = AnsibleFactCollector(collectors=collectors_list)
    fact_collector.collect()

# Generated at 2022-06-13 00:11:36.809420
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    '''
    Returns a new AnsibleFactCollector for gathering facts for a given subset of systems.

    The collect method of the returned AnsibleFactCollector gathers facts from the
    classes associated with the given gather_subset.
    '''

    import mock

    # placeholder classes for unit test
    class C1(object):
        name = 'c1'

    class C2(object):
        name = 'c2'

    class C3(object):
        name = 'c3'

    all_collector_classes = [C1, C2, C3]
    gather_subset = ['c1', 'c2']
    filter_spec = ['c1']

    # mock out just the class initializer of the collectors

# Generated at 2022-06-13 00:11:48.640350
# Unit test for function get_ansible_collector
def test_get_ansible_collector():

    import ansible.module_utils.facts.network.base
    import ansible.module_utils.facts.solaris.network
    import ansible.module_utils.facts.network.generic
    all_collector_classes = [
        ansible.module_utils.facts.network.base.Network,
        ansible.module_utils.facts.solaris.network.NetworkSolaris,
        ansible.module_utils.facts.network.generic.NetworkGeneric,
    ]

    fact_collector = \
        get_ansible_collector(all_collector_classes,
                              gather_subset=['all', 'min'],
                              minimal_gather_subset=['all'],
                              gather_timeout=10)

    collected_facts = {}

# Generated at 2022-06-13 00:11:55.514801
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    from ansible.module_utils.facts.system import distro
    from ansible.module_utils.facts.network import interfaces
    from ansible.module_utils.facts.virtual import virtual

    all_collector_classes = [
        distro.Distribution,
        interfaces.Interfaces,
        virtual.Virtual,
    ]

    collector = get_ansible_collector(all_collector_classes)
    facts = collector.collect()
    assert len(facts) > 0



# Generated at 2022-06-13 00:12:06.122465
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    import ansible.module_utils.facts.collector
    import ansible.module_utils.facts.hardware
    import ansible.module_utils.facts.network
    import ansible.module_utils.facts.system
    import ansible.module_utils.facts.virtual

    all_collector_classes =\
        ansible.module_utils.facts.collector.get_collector_classes()

    # This is a list of the classes we want to be run for a full collection

# Generated at 2022-06-13 00:12:09.523851
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    fact_collector = AnsibleFactCollector("collectors", "namespace")
    assert fact_collector.collect("module", "collected_facts"), "Should return True"

# Generated at 2022-06-13 00:12:17.332199
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    import ansible.module_utils.facts.namespace

# Generated at 2022-06-13 00:12:28.980192
# Unit test for function get_ansible_collector
def test_get_ansible_collector():

    class NetworkCollector(collector.BaseFactCollector):
        name = 'network'
        _fact_ids = set(['ansible_all_ipv4_addresses', 'ansible_all_ipv6_addresses'])

        def __init__(self, namespace=None):
            super(NetworkCollector, self).__init__(namespace=namespace)

        def collect(self, module=None, collected_facts=None):
            return {'ansible_all_ipv4_addresses': ['192.168.0.1'],
                    'ansible_all_ipv6_addresses': ['dead:beef::1']}

    class DummyCollector(collector.BaseFactCollector):
        name = 'dummy'
        _fact_ids = set(['dummy_fact'])



# Generated at 2022-06-13 00:12:43.233793
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    from ansible.module_utils.facts import namespace

    class TestCollector1(collector.BaseFactCollector):
        name = 'test1'
        _fact_ids = set([])

        def collect(self, module=None, collected_facts=None):
            return {'test1': 'test1'}

    class TestCollector2(collector.BaseFactCollector):
        name = 'test2'
        _fact_ids = set([])

        def collect(self, module=None, collected_facts=None):
            return {'test2': 'test2'}

    class TestCollector3(collector.BaseFactCollector):
        name = 'test3'
        _fact_ids = set([])


# Generated at 2022-06-13 00:12:55.221226
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    from ansible.module_utils.facts import collector_registry
    from ansible.module_utils.facts.namespace import PrefixFactNamespace

    # The top level key should be 'ansible' and not 'ansible_'
    ns = PrefixFactNamespace(prefix='ansible_')

    fact_collector = \
        get_ansible_collector(all_collector_classes=collector_registry.registered_collector_classes,
                              namespace=ns)

    print('gather_subset is %s' % fact_collector.collectors[-1].gather_subset)
    print('module_setup is %s' % fact_collector.collectors[-1].module_setup)

    #print(fact_collector.collectors)

    #print(fact_collector.collect())

# Generated at 2022-06-13 00:13:00.297543
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
  import ansible.module_utils.facts.collector.network
  import ansible.module_utils.facts.collector.platform
  import ansible.module_utils.facts.collector.hardware
  import ansible.module_utils.facts.collector.virtual
  all_collector_classes = [
      ansible.module_utils.facts.collector.network.NetworkCollector,
      ansible.module_utils.facts.collector.platform.PlatformCollector,
      ansible.module_utils.facts.collector.hardware.HardwareCollector,
      ansible.module_utils.facts.collector.virtual.VirtualCollector]
  filter_spec = None
  gather_subset = ['all']
  gather_timeout = 10
  minimal_gather_subset = None
  fact_collector = get_

# Generated at 2022-06-13 00:13:11.390370
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    from ansible.module_utils.facts import collector

    all_collector_classes = collector.get_collector_classes()

    fact_collector = get_ansible_collector(all_collector_classes,
                                           gather_subset=None)

    collected_facts = fact_collector.collect()

    assert collected_facts['ansible_facts']['gather_subset'] == ['all']
    assert 'ansible_module_setup' in collected_facts['ansible_facts']

    # Test a gather_subset
    fact_collector = get_ansible_collector(all_collector_classes,
                                           gather_subset=['network'])

    collected_facts = fact_collector.collect()


# Generated at 2022-06-13 00:13:22.299142
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    import unittest

    class TestAnsibleFactCollector(unittest.TestCase):

        # IMPORTANT: Do not change this class, the unittest has been written specifically for class AnsibleFactCollector
        class TestFactsCollector(collector.BaseFactCollector):
            name = 'Test_Facts_Collector'
            _fact_ids = set([])

            def collect(self, module=None, collected_facts=None):
                return {'foo': 'this is a foo fact'}

        test_collectors = [TestFactsCollector()]
        test_namespace = None
        test_filter_spec = []


# Generated at 2022-06-13 00:13:31.718368
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    class MyCollector(collector.BaseFactCollector):
        def collect(self, module=None, collected_facts=None):
                return {'a': 1, 'b': 2}

    module = {}

    # No filter specified
    fact_collector = AnsibleFactCollector(collectors=[MyCollector()])
    collected_facts = fact_collector.collect(module=module)

    assert collected_facts == {'a': 1, 'b': 2}

    # Filter matches all
    fact_collector = AnsibleFactCollector(collectors=[MyCollector()], filter_spec='*')
    collected_facts = fact_collector.collect(module=module)

    assert collected_facts == {'a': 1, 'b': 2}

    # Filter specified as a string
    fact_collector = AnsibleFactCollect

# Generated at 2022-06-13 00:13:42.309256
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    import tests.unit.ansible_collections.ansible.community.plugins.module_utils.network.common.facts.facts as test_facts

    namespace = 'custom_facts'
    gather_subset = ['all']
    filter_spec = []
    minimal_gather_subset = []
    gather_timeout = 0

    fact_collector = get_ansible_collector(
        all_collector_classes=test_facts.FACT_COLLECTORS_BASE,
        namespace=namespace,
        gather_subset=gather_subset,
        gather_timeout=gather_timeout,
        minimal_gather_subset=minimal_gather_subset)

    # ansible_interfaces fact collector should be created
    facts = fact_collector.collect()


# Generated at 2022-06-13 00:13:50.024424
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    import ansible.module_utils.facts.collector.network
    import ansible.module_utils.facts.collector.platform
    import ansible.module_utils.facts.collector.system

    all_collector_classes = [
        ansible.module_utils.facts.collector.network.NetworkCollector,
        ansible.module_utils.facts.collector.system.SystemCollector,
        ansible.module_utils.facts.collector.platform.PlatformCollector,
    ]
    gather_subset=None
    ansible_collector = get_ansible_collector(all_collector_classes, gather_subset=gather_subset)
    assert 'gather_subset' in ansible_collector.collect()
    assert 'module_setup' in ansible_collector.collect()


# Generated at 2022-06-13 00:14:02.161241
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts import collector
    from ansible.module_utils.facts import linux
    from ansible.module_utils.facts import system
    from ansible.module_utils.facts import virtual

    import ansible.module_utils.facts.collector.hardware
    import ansible.module_utils.facts.collector.network

    all_collector_classes = [
        ansible.module_utils.facts.collector.hardware.Hardware,
        ansible.module_utils.facts.collector.network.Network,
        linux.Distribution,
        system.AllSubset,
        system.System,
        virtual.Virtual,
    ]

    # test with default arguments
    fact_collector = get_ansible

# Generated at 2022-06-13 00:14:09.847553
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    # 1) FIXTTURES
    class DummyCollector(collector.BaseFactCollector):
        def collect(self):
            return {'foo': 'bar'}

    class DummyCollector2(collector.BaseFactCollector):
        def collect(self):
            return {'foo2': 'bar2'}

    all_collectors = [DummyCollector, DummyCollector2]
    # 2) GIVEN
    fact_collector = AnsibleFactCollector(collectors=all_collectors)
    # 3) WHEN
    facts_dict = fact_collector.collect()
    # 4) THEN
    assert facts_dict == {'foo': 'bar', 'foo2': 'bar2'}, 'It should return a dictionary with all the facts'



# Generated at 2022-06-13 00:14:32.694956
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():

    # We need to run this in Ansible <= 2.6 to get
    # the base ansible_facts collector working properly.
    # In Ansible 2.7+, we do not need to do this.
    import ansible.module_utils.facts.base
    ansible.module_utils.facts.base.AnsibleCollector()

    # import pdb; pdb.set_trace()

    # We need this because we have to have the legacy ansible_facts
    # collector run first, even though we don't want it.
    from ansible.module_utils.facts import gather
    gather.GatherFacts()

    module_setup = True

    # Create a set of collectors
    minimal_gather_subset = frozenset()

    # Add a collector that knows what gather_subset we used so it it can provide a fact


# Generated at 2022-06-13 00:14:43.329129
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    '''Basic unit test of function get_ansible_collector'''

    fact_collector = get_ansible_collector(all_collector_classes=collector.default_collector_classes)

    try:
        facts = fact_collector.collect()
        # print(facts)  # UNCOMMENT TO DEBUG
    except Exception as e:
        assert False, "Failed to collect facts, Exception: %s" % repr(e)

    assert 'ansible_facts' in facts
    assert 'facter' in facts['ansible_facts']
    assert 'gather_subset' in facts['ansible_facts']

# Generated at 2022-06-13 00:14:43.800153
# Unit test for function get_ansible_collector
def test_get_ansible_collector():

    assert True

# Generated at 2022-06-13 00:14:53.845960
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    """Unit test for method collect of class AnsibleFactCollector"""

    namespace1 = collector.namespace.PrefixFactNamespace(prefix='ns1')
    namespace2 = collector.namespace.PrefixFactNamespace(prefix='ns2')


# Generated at 2022-06-13 00:15:00.396800
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():

    # Our mock collect method just return a dict with a single key
    def mock_collect(module, collected_facts):
        return {'module_setup': True}

    collector = collector.FactCollector()
    collector.collect = mock_collect

    # Base fact collector
    fact_collector = \
        AnsibleFactCollector([collector], namespace=None)
    facts = fact_collector.collect()
    assert facts['module_setup'] == True

    # Namespaced fact collector
    fact_collector = \
        AnsibleFactCollector([collector],
                             namespace=collector.namespace)
    facts = fact_collector.collect()
    assert facts['module_setup'] == True

    # Fact collector with filters

# Generated at 2022-06-13 00:15:11.525801
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    '''collector.get_ansible_collector()'''
    from ansible.module_utils.facts import cache
    from ansible.module_utils.facts import timeout

    gather_subset = ['all']
    gather_timeout = timeout.DEFAULT_GATHER_TIMEOUT
    minimal_gather_subset = ['hardware']

    fact_collector = \
        get_ansible_collector(all_collector_classes=cache.FACT_CACHE,
                              gather_subset=gather_subset,
                              gather_timeout=gather_timeout,
                              minimal_gather_subset=minimal_gather_subset)

    # Returns an AnsibleFactCollector object
    assert isinstance(fact_collector, AnsibleFactCollector)

    # Returns an AnsibleFactCollect

# Generated at 2022-06-13 00:15:22.919779
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    class DummyCollector(CollectorMetaDataCollector):
        def __init__(self, namespace=None):
            self._facts = {'dummyfact1': 'dummy value1',
                           'dummyfact2': 'dummy value2'}

        def collect(self, module=None, collected_facts=None):
            return self._facts

    namespace = collector.BaseFactNamespace()
    fact_collector = \
        AnsibleFactCollector(collectors=[DummyCollector(namespace=namespace)],
                             namespace=namespace)
    facts = fact_collector.collect()


# Generated at 2022-06-13 00:15:30.182132
# Unit test for function get_ansible_collector
def test_get_ansible_collector():

    # TODO: Add a test that exercises the __init__ code and that the collector
    # returned is an AnsibleFactCollector
    assert isinstance(get_ansible_collector({}, None, []), AnsibleFactCollector)

    # TODO: A test that exercises the collect() method.
    # It is currently only tested in the integration test


if __name__ == '__main__':
    test_get_ansible_collector()

# Generated at 2022-06-13 00:15:40.706156
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    import ansible.module_utils.facts.system
    from ansible.module_utils.facts.namespace import PrefixFactNamespace

    collector_classes = ansible.module_utils.facts.system.collector_classes

    all_gather_subset = set(['all'])
    all_filter_spec = '*'
    all_namespace = None

    all_fact_collector = get_ansible_collector(collector_classes,
                                               gather_subset=all_gather_subset,
                                               filter_spec=all_filter_spec,
                                               namespace=all_namespace)
    ansible_facts = all_fact_collector()
    assert ansible_facts['gather_subset'] == ['all']
    assert ansible_facts['module_setup'] == True



# Generated at 2022-06-13 00:15:47.361875
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    # Declare FactCollectors to be added in AnsibleFactCollector
    class FirstFactCollector(collector.BaseFactCollector):
        name = 'first'

        def collect(self, module=None, collected_facts=None):
            return {'first_fact': 'first_value'}

    class SecondFactCollector(collector.BaseFactCollector):
        name = 'second'

        def collect(self, module=None, collected_facts=None):
            return {'second_fact': 'second_value'}

    # Initialize an AnsibleFactCollector with collectors
    collectors = [FirstFactCollector(namespace=None),
                  SecondFactCollector(namespace=None)]

# Generated at 2022-06-13 00:16:19.231298
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():

    class Collector1(collector.BaseFactCollector):
        name = 'collector1'
        _fact_ids = set(['a', 'b', 'c'])

    class Collector2(collector.BaseFactCollector):
        name = 'collector2'
        _fact_ids = set(['d', 'e', 'f'])

    class Collector3(collector.BaseFactCollector):
        name = 'collector3'
        _fact_ids = set(['g', 'h', 'i'])

        def collect(self, module=None, collected_facts=None):
            raise Exception("Failed to collect facts for '%s' (%s)" %
                            (collected_facts, self._fact_ids))

    collector1 = Collector1()
    collector2 = Collector2()
    collector3 = Collector3

# Generated at 2022-06-13 00:16:21.032035
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():

    fact_collector = AnsibleFactCollector(collectors=[],
                                          namespace=None)

    # No fact collector should be able to be initialized
    assert fact_collector is not None

# Generated at 2022-06-13 00:16:31.295529
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    import ansible.module_utils.facts.collector.network

    fact_collector = get_ansible_collector(all_collector_classes=ansible.module_utils.facts.collector.network.__all__,
                                           gather_subset='network')

    assert(fact_collector.collectors)
    assert(len(fact_collector.collectors) > 0)
    assert(fact_collector.collectors[0].name)
    assert(fact_collector.collectors[-1].name == 'gather_subset')
    assert(fact_collector.collectors[0].collector_class)
    assert(fact_collector.collectors[-1].collector_class.__name__ == 'CollectorMetaDataCollector')

# Generated at 2022-06-13 00:16:38.908320
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():

    class StubCollector(collector.BaseFactCollector):

        def __init__(self, *args, **kwargs):
            super(StubCollector, self).__init__(*args, **kwargs)
            self.name = 'stub'
            self._fact_ids = set([])

        def collect(self, module=None, collected_facts=None):
            return {'stub': True}

    fact_collector = \
        AnsibleFactCollector(collectors=[StubCollector(namespace=None)],
                             filter_spec=None)

    facts = fact_collector.collect()

    assert 'stub' in facts

# Generated at 2022-06-13 00:16:48.187716
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    # FilterSpec should not filter for '*' when the list of facts is empty
    fact_collector = AnsibleFactCollector(filter_spec='*')
    facts_dict = fact_collector.collect()
    assert len(facts_dict) == 0

    # FilterSpec should return all facts when '*' is provided
    fact_collector = AnsibleFactCollector(filter_spec='*')
    info_dict = {'fact1': 'value1', 'fact2': 'value2'}
    facts_dict = fact_collector.collect(collected_facts=info_dict)
    assert len(facts_dict) == 2

    # FilterSpec should return only matched fact if a list of facts are provided
    fact_collector = AnsibleFactCollector(filter_spec=['fact1', 'fact3'])
    info_

# Generated at 2022-06-13 00:16:53.508697
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    fake_module = {}
    fake_collector = collector.BaseFactCollector()
    fake_collector.collect = lambda _: {'foo': 'bar'}

    ansible_collector = AnsibleFactCollector([fake_collector])
    assert {'foo': 'bar'} == ansible_collector.collect(module=fake_module)


# Generated at 2022-06-13 00:17:04.268745
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect(): # [1]
    from ansible.module_utils.facts.collector import FileDictCollector
    from ansible.module_utils.facts.namespace import PrefixFactNamespace

    class MockFileDictCollector(FileDictCollector):
        '''A mock FileDictCollector that just returns a static dict.'''
        name = 'file.dict'
        def collect(self, module=None, collected_facts=None):
            return dict(foo=1, bar=2)

    # We need to collect with a namespace to test the namespace stuff
    mock_file_dict_collector = MockFileDictCollector(namespace=PrefixFactNamespace(prefix='MOCK_'))
    fact_collector = AnsibleFactCollector([mock_file_dict_collector], namespace=None)

    # Simple collect test

# Generated at 2022-06-13 00:17:10.094753
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():

    def _test_collector_class(namespace=None):
        class _test_collector(collector.BaseFactCollector):
            name = 'test'
            _fact_ids = set(['test1', 'test2'])

            def __init__(self, namespace=None):
                super(_test_collector, self).__init__(namespace=namespace)

            def collect(self, module=None, collected_facts=None):
                if namespace:
                    # Expected namespace
                    assert self.namespace.fact_prefix == namespace
                else:
                    # Expected no namespace
                    assert self.namespace is None

                return {'test1' : 'fact1', 'test2' : 'fact2'}

        return _test_collector

    collector_class = _test_collector_class()
   

# Generated at 2022-06-13 00:17:20.614413
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    filter_spec = filter_spec or []
    gather_subset = ['all']
    gather_timeout = timeout.DEFAULT_GATHER_TIMEOUT
    minimal_gather_subset = frozenset()

    # NOTE: This line will fail unless you have the redhat-access-insights package installed
    all_collector_classes = collector.all_collector_classes()
    desired_collector_classes = [
        'collectors.network.NetworkCollector',
        'collectors.platform.PlatformCollector',
        'collectors.distribution.DistributionCollector',
        'redhat_access_insights.ansible_facts.collectors.insights.InsightsCollector'
    ]

# Generated at 2022-06-13 00:17:30.178521
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():

    class TestCollector(collector.BaseFactCollector):
        name = 'test'

        def collect(self, module=None, collected_facts=None):
            collected_facts = collected_facts or {}
            return {'ansible_greeting': 'hello',
                    'ansible_goodbye': 'goodbye'}

    test_collector = TestCollector()
    collectors = [test_collector]

    filter_spec = ['ansible*']
    fact_collector = AnsibleFactCollector(collectors=collectors, filter_spec=filter_spec)

    facts_dict = fact_collector.collect()

    assert 'ansible_greeting' in facts_dict
    assert facts_dict['ansible_greeting'] == 'hello'
    assert 'ansible_goodbye' in facts_dict
   

# Generated at 2022-06-13 00:18:16.164973
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    pass

# Generated at 2022-06-13 00:18:26.239611
# Unit test for function get_ansible_collector
def test_get_ansible_collector():

    try:
        from ansible.module_utils.facts.system.distribution import DistributionFactCollector
    except:
        # Test should be updated to effectively skip when distribution module is not available
        pass
    try:
        from ansible.module_utils.facts.system.pkg_mgr import PkgMgrFactCollector
    except:
        # Test should be updated to effectively skip when pkg_mgr module is not available
        pass

    filter_spec = ['distribution']
    gather_subset = ['all']
    gather_timeout = timeout.DEFAULT_GATHER_TIMEOUT
    minimal_gather_subset = frozenset(['all'])

    all_collector_classes = [DistributionFactCollector, PkgMgrFactCollector]

    collector_classes = \
        collector.collector_classes_from

# Generated at 2022-06-13 00:18:31.365465
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    all_collector_classes = collector.get_collector_classes()
    fact_collector = get_ansible_collector(all_collector_classes)
    assert len(fact_collector.collectors) == len(all_collector_classes)
    assert fact_collector.collectors[-1].__class__.name == 'gather_subset'




# Generated at 2022-06-13 00:18:37.209860
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    class CollectFacts:
        def collect(self, collected_facts=None, module=None):
            return {'ansible_facts':{'foo': 'bar'}}

    c = AnsibleFactCollector(collectors=[CollectFacts()])
    res = c.collect()

    # Test if 'ansible_facts' are added as root key
    assert 'ansible_facts' in res
    assert res['ansible_facts'] == {'foo': 'bar'}



# Generated at 2022-06-13 00:18:47.035125
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    class FakeFacter(AnsibleFactCollector):
        '''Fake facter class to test get_ansible_collector function'''
        name = 'fake_facter'
        _fact_ids = set(['fake_facter_id'])

    class FakeOhai(AnsibleFactCollector):
        '''Fake ohai class to test get_ansible_collector function'''
        name = 'fake_ohai'
        _fact_ids = set(['fake_ohai_id'])

    class FakeDMFacter(AnsibleFactCollector):
        '''Fake dmfacter class to test get_ansible_collector function'''
        name = 'fake_dmfacter'
        _fact_ids = set([])


# Generated at 2022-06-13 00:18:56.961375
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    '''Test AnsibleFactCollector.collect()'''

    class MockFactCollector(object):

        def __init__(self, namespace=None):
            pass

        def collect(self, module=None, collected_facts=None):
            return {'test_fact': 'test_value'}

    import ansible.module_utils.facts.namespace as namespace
    ansible_namespace_obj = namespace.AnsibleNamespace()
    fact_collector = AnsibleFactCollector(collectors=[MockFactCollector(namespace=ansible_namespace_obj)],
                                          namespace=ansible_namespace_obj)
    fact_collection = fact_collector.collect()
    assert fact_collection.get('test_fact') == 'test_value'

    # Test filter '*'
    fact_collect

# Generated at 2022-06-13 00:19:05.186397
# Unit test for function get_ansible_collector
def test_get_ansible_collector():
    all_collector_classes = collector.collector_classes_from_gather_subset(gather_subset=['all'])
    fact_collector = AnsibleFactCollector(collectors=[])

    # Test list of all subsystems
    collectors = get_ansible_collector(all_collector_classes=all_collector_classes,
                                       namespace='ansible').collectors
    assert len(collectors) > 1
    assert type(collectors[0]) is collector.BaseFactCollector
    assert type(collectors[1]) is collector.NetworkFactCollector
    assert type(collectors[-1]) is CollectorMetaDataCollector

    # Test single subsystem

# Generated at 2022-06-13 00:19:08.914481
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    import ansible.module_utils.facts.system.base as base
    # See class AnsibleFactCollector for an example of how to filter facts
    filter_spec = ['ansible_os_family', 'ansible_virtualization_type']
    ans_fact_collector = AnsibleFactCollector(collectors=[base.BaseFactCollector()],
                                              filter_spec=filter_spec)
    ans_fact_collector.collect()

# Generated at 2022-06-13 00:19:18.925796
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    

    # name of this test case is required
    def test(all_collector_classes,
             namespace,
             filter_spec,
             gather_subset,
             gather_timeout,
             minimal_gather_subset,
             expect_facts_dict):
        collector_meta_data_collector = \
            CollectorMetaDataCollector(namespace=namespace,
                                       gather_subset=gather_subset,
                                       module_setup=True)

        ansible_fact_collector = \
            AnsibleFactCollector(collectors=[collector_meta_data_collector],
                                 namespace=namespace)

        facts_dict = ansible_fact_collector.collect()

        assert facts_dict == expect_facts_dict


# Generated at 2022-06-13 00:19:24.481262
# Unit test for method collect of class AnsibleFactCollector
def test_AnsibleFactCollector_collect():
    import ansible.module_utils.facts.tools as tools
