

# Generated at 2022-06-13 00:24:17.707087
# Unit test for function ansible_facts
def test_ansible_facts():
    '''
    Ansible facts returns a dict, with the ansible_ prefix and : replaced with _.
    '''
    import sys
    sys.path.insert(0, './library')
    import module_utils.facts
    import ansible.module_utils.basic
    import ansible.module_utils.facts
    from ansible.module_utils.facts import ansible_facts
    from ansible.module_utils.facts import default_collectors

    # test case 1: gather all facts
    gather_subset = ['all']

    # gather_subset = ['!all']
    # gather_subset = None

# Generated at 2022-06-13 00:24:28.256234
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible_collections.notstdlib.moveitallout.tests.unit.compat.mock import Mock
    from ansible.module_utils.facts import default_collectors, ansible_collector

    all_collector_classes = default_collectors.collectors

    # don't add a prefix
    namespace = PrefixFactNamespace(namespace_name='ansible', prefix='')

    # ensure that ansible_collector_mod module is not loaded
    ansible_collector_mod = Mock()
    ansible_collector_mod.get_ansible_collector = Mock()

    def __getattr__(name):
        if name == 'collect':
            return get_all_facts
        else:
            return Mock()

    ansible_collector_mod.get_ansible_collector.return_

# Generated at 2022-06-13 00:24:36.348245
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils.facts import ansible_collector
    from ansible.module_utils.facts.namespace import PrefixFactNamespace

    class MockModule(object):
        def __init__(self, gather_subset):
            self.params = dict()
            self.params['gather_subset'] = gather_subset

    # test when no 'gather_subset' param
    module = MockModule([])
    expected_subset = ['all']
    facts_dict = get_all_facts(module)
    assert facts_dict['ansible_fips'] == 'False'

    # test when there is a 'gather_subset' param


# Generated at 2022-06-13 00:24:45.155314
# Unit test for function ansible_facts
def test_ansible_facts():

    from ansible.module_utils.facts import ansible_facts
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.collector import DummyFactCollector
    from ansible.module_utils.facts.collector import FallbackCollector
    from ansible.module_utils.facts.namespace import BaseFactNamespace
    from ansible.module_utils.facts.namespace import PrefixFactNamespace

    import ansible.module_utils.facts.collector

    class TestModule(object):
        def __init__(self):
            self.params = dict()
            self.params['gather_subset'] = ['!not', 'all']
            self.params['gather_timeout'] = 10
            self.params['filter'] = '*'

    original

# Generated at 2022-06-13 00:24:55.794551
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts import ansible_facts
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts import Namespace
    from ansible.module_utils.facts.utils import get_all_collector_classes
    import os
    import tempfile
    import shutil

    # Create a fake fact module in a temp dir
    fact_dir = tempfile.mkdtemp()

# Generated at 2022-06-13 00:25:07.149924
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.six import PY2

    from ansible.module_utils._text import to_bytes
    from ansible.module_utils import basic

    from ansible.module_utils.facts.system.distribution import DistributionFactCollector
    from ansible.module_utils.facts.system.distribution import LinuxDistribution
    from ansible.module_utils.facts.system.distribution import LinuxDistributionFactory

    import os

    if PY2:
        FAKE_SYSTEM_INFO = to_bytes(os.path.join(os.path.dirname(__file__), 'resources', 'system_info'))
    else:
        FAKE_SYSTEM_INFO = os.path.join(os.path.dirname(__file__), 'resources', 'system_info')


# Generated at 2022-06-13 00:25:12.629402
# Unit test for function ansible_facts
def test_ansible_facts():
    '''
    unit testing for module_utils.facts.ansible_facts
    '''
    from ansible.module_utils.facts import ansible_facts

    module = FauxModule()
    facts = ansible_facts(module)

    assert facts['distribution'] == 'distribution_val'


# unit test for function get_all_facts

# Generated at 2022-06-13 00:25:14.392464
# Unit test for function ansible_facts
def test_ansible_facts():
    # TODO(rmeggins)
    pass


# Generated at 2022-06-13 00:25:22.241098
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts import cache

    cache.FACT_CACHE = {}

    def mock_ansible_module(params):
        class MockModule(object):
            def __init__(self, params):
                self.params = params

        module = MockModule(params)
        fact_cache = cache.FactCache(module)
        module.fact_cache = fact_cache
        return module

    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils.facts import ansible_collector
    from ansible.module_utils.facts.namespace import PrefixFactNamespace

    '''
    test a basic invocation with no params.
    Should return 'all' facts, default filter
    '''

# Generated at 2022-06-13 00:25:22.583628
# Unit test for function ansible_facts
def test_ansible_facts():
    pass

# Generated at 2022-06-13 00:25:28.332639
# Unit test for function ansible_facts
def test_ansible_facts():
    '''Unit test for function ansible_facts'''

    import os
    import shutil
    import tempfile
    import unittest

    from ansible_collections.community.general.tests.unit.compat import mock

    from ansible.plugins.loader import module_finder

    from ansible.module_utils.facts.ansible_collector import AnsibleCollector
    from ansible.module_utils.facts.collector.ansible_local import AnsibleLocalCollector
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.namespace import BaseFactNamespace
    from ansible.module_utils.facts.namespace import PrefixFactNamespace


# Generated at 2022-06-13 00:25:39.784762
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.collector import BaseFileReadCollector
    from ansible.module_utils.facts.collector import BaseFileWriteCollector

    # stub the BaseFactCollector base class
    class Thing:
        pass

    class StubBaseFactCollector(BaseFactCollector):
        def collect(self, module=None, collected_facts=None):
            return Thing()

    # stub the BaseFileReadCollector base class
    class StubBaseFileReadCollector(BaseFileReadCollector):
        def collect(self, module=None, collected_facts=None):
            return Thing()

    # stub the AnsibleModule

# Generated at 2022-06-13 00:25:41.864092
# Unit test for function get_all_facts
def test_get_all_facts():
    import json
    module_class = MockAnsibleModule
    module = module_class()
    f = get_all_facts(module)
    print(json.dumps(f, indent=4, sort_keys=True))



# Generated at 2022-06-13 00:25:49.045623
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils.facts import get_all_facts
    import ansible.module_utils.facts.system.distribution
    import ansible.module_utils.facts.system.pkg_mgr
    import ansible.module_utils.facts.system.user
    import ansible.module_utils.facts.system.platform
    import ansible.module_utils.facts.network.interfaces
    import ansible.module_utils.facts.network.default_ipv4
    import ansible.module_utils.facts.network.routing

    # pylint: disable=E0602
    module = AnsibleModule(
        argument_spec=dict(
            gather_subset=dict(default=['!all'], type='list')
        ),
        supports_check_mode=False
    )
    collected_facts

# Generated at 2022-06-13 00:25:58.063255
# Unit test for function ansible_facts
def test_ansible_facts():

    # Mock module object
    test_ansible_module = MockModule()

    # Mock filterspec
    test_ansible_filter = MockFilterSpec()

    # Mock subset
    test_ansible_subset = set(['all'])

    # call ansible facts
    ansible_facts(test_ansible_module, gather_subset=test_ansible_subset)

    # Mock collector object
    test_ansible_col = MockAnsibleCollector()

    # call ansible facts
    ansible_facts(test_ansible_module, gather_subset=test_ansible_subset)



# Generated at 2022-06-13 00:26:08.450062
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts import cache, collector
    from ansible.module_utils.facts import ansible_collector
    from ansible.plugins.loader import fact_loader

    # clear any in-memory caches for unit tests
    cache.FACT_CACHE = {}
    collector.CACHE = {}

    # mock AnsibleModule class
    from ansible.module_utils.facts import ansible_module
    class AnsibleModuleMock(object):
        def __init__(self, *args, **kwargs):
            self.params = {}
            self.connection = ""
            self.log = lambda *args, **kwargs: None

        def fail_json(self, result):
            raise Exception(result)

    module = AnsibleModuleMock()

# Generated at 2022-06-13 00:26:10.268789
# Unit test for function ansible_facts
def test_ansible_facts():
    gathered_facts = ansible_facts(module={})

    assert gathered_facts is not None

# Generated at 2022-06-13 00:26:16.576594
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils.facts import Facts
    # use the module_utils facts.Facts class to simulate an AnsibleModule instance
    facts_module_mock = Facts(dict(gather_subset=['all']))
    return_dict = get_all_facts(facts_module_mock)
    assert isinstance(return_dict, dict)
    assert 'default_ipv4' in return_dict


# Generated at 2022-06-13 00:26:24.840066
# Unit test for function ansible_facts
def test_ansible_facts():
    # make sure we can import the MockAnsibleModule class
    from ansible.module_utils.facts import facts as mock_module_utils_facts
    from ansible.module_utils.facts import get_all_facts as mock_module_utils_get_all_facts

    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils import basic

    mock_ansible_module = mock_module_utils_facts.MockAnsibleModule()
    # simple usage
    facts_dict = ansible_facts(mock_ansible_module)
    assert 'default_ipv4' in facts_dict
    # default_ipv4.address should be a dict
    assert isinstance(facts_dict['default_ipv4']['address'], dict)

    # now check the return value of

# Generated at 2022-06-13 00:26:36.945905
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.compat.tests.mock import patch, MagicMock
    mock_module = MagicMock()
    mock_module.params = {
        'gather_subset': ['all'],
        'gather_timeout': 10,
        'filter': '*'
    }
    mock_module.run_command = MagicMock()

    with patch('ansible.module_utils.facts.ansible_collector.get_ansible_collector', return_value=MagicMock()) as mock_collector:
        result = ansible_facts(mock_module)
        # Ensure that get_ansible_collector was called with the correct params
        mock_collector.assert_called_once()
        _, kwargs = mock_collector.call_args

# Generated at 2022-06-13 00:26:47.928537
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts.network.base import NetworkCollector
    from ansible.module_utils.facts.network.linux import LinuxNetworkCollector
    from ansible.module_utils.facts.network.generic import GenericNetworkCollector
    from ansible.module_utils.facts.system.base import BaseFactCollector
    from ansible.module_utils.facts.system.distribution import DistributionFactCollector
    from ansible.module_utils.facts.system.generic import GenericDistributionFactCollector
    from ansible.module_utils.facts.system.linux import LinuxDistributionFactCollector

    import unittest

    class TestAnsibleFacts(unittest.TestCase):
        def test_ansible_facts(self):
            from ansible.module_utils.facts.system.linux import LinuxDistributionFactCollect

# Generated at 2022-06-13 00:26:56.248329
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.facts import default_collectors

    class DummyModule(object):
        def __init__(self, params):
            self.params = params

    # hack up some test stubs for the fact collectors.
    class DummyCollector(ansible_collector.BaseFactCollector):
        def __init__(self, *args, **kwargs):
            super(DummyCollector, self).__init__(*args, **kwargs)

        @ansible_collector.collects_with_properties('dummy_facts')
        def collect(self, module=None, collected_facts=None):
            return {'dummy_facts': {'dummy_fact': 'dummy_value'}}


# Generated at 2022-06-13 00:27:06.885455
# Unit test for function ansible_facts
def test_ansible_facts():
    class FakeModule(object):
        def __init__(self):
            self.params = {'gather_subset': ['all']}

    fake_module = FakeModule()
    fact_dictionary = ansible_facts(fake_module)

    # Verify that all the dictionary keys are namespaced
    assert all(key.startswith('ansible_') for key in fact_dictionary)

    # Verify that the dictionary values that start with 'ansible_' and have
    # anything after them are fact dictionaries, and not other types.
    for fact_name, fact_value in fact_dictionary.items():
        if isinstance(fact_value, dict):
            assert fact_name.startswith('ansible_')

# Generated at 2022-06-13 00:27:16.472655
# Unit test for function ansible_facts
def test_ansible_facts():
    import ansible.module_utils.facts
    import ansible.module_utils.facts.collector

    import datetime
    import unittest
    import mock

    class SimpleCollector(ansible.module_utils.facts.collector.BaseFactCollector):
        NAME = 'simple'

        def __init__(self, *args, **kwargs):
            super(SimpleCollector, self).__init__(*args, **kwargs)
            self.collected_facts = {u'a': u'b'}

    class DateTimeCollector(ansible.module_utils.facts.collector.BaseFactCollector):
        NAME = 'date_time'

# Generated at 2022-06-13 00:27:26.179360
# Unit test for function get_all_facts
def test_get_all_facts():
    import datetime
    import time
    import unittest

    class MockModule:
        class MockFailJson:
            called = False

            def __call__(self, *args, **kwargs):
                self.called = True

        fail_json = MockFailJson()
        params = dict(gather_timeout=1)

    start_time = datetime.datetime.now()

    class TestFacts(unittest.TestCase):
        def test_get_all_facts(self):
            module = MockModule()
            facts = get_all_facts(module)
            self.assertEqual(type(facts), dict)
            self.assertFalse(MockModule.fail_json.called)

    unittest.main()

# Generated at 2022-06-13 00:27:37.534914
# Unit test for function get_all_facts
def test_get_all_facts():
    # test using ansible_module_utils.facts.test_module_utils.TestModule
    import sys
    import os
    import json

    from ansible.module_utils.facts.test_module_utils import (
        TestAnsibleModule,
        get_all_collector_classes
    )

    path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
    sys.path.insert(0, path)

    test_module = type(str("AnsibleModule"), (TestAnsibleModule,),
                       {'params': {}})
    fake_module = test_module()

    all_collector_classes = get_all_collector_classes()

   

# Generated at 2022-06-13 00:27:49.204106
# Unit test for function ansible_facts
def test_ansible_facts():

    from ansible.compat.tests import unittest
    from ansible.compat.tests.mock import patch, Mock

    import ansible.module_utils.facts.ansible_facts as ansible_facts

    class TestAnsibleModule(object):
        def __init__(self, params):
            self.params = params

    class TestOptions(object):
        def __init__(self, params):
            self.params = params

    class TestAnsibleModuleUtilsFacts(unittest.TestCase):

        module = TestAnsibleModule(params={'gather_subset': ['all'],
                                           'gather_timeout': 10,
                                           'filter': '*'})


# Generated at 2022-06-13 00:27:56.190212
# Unit test for function ansible_facts
def test_ansible_facts():
    # Set up a fake module
    from ansible.module_utils.basic import AnsibleModule
    from collections import namedtuple

    module = AnsibleModule(
        argument_spec=dict(
            gather_subset=dict(type='list', default=['all']),
            filter=dict(type='list', default='*'),
            gather_timeout=dict(type='int', default=10)),
        supports_check_mode=True,
    )

    assert ansible_facts(module)


__all__ = ('ansible_facts', 'get_all_facts')

# assert test_ansible_facts()

# Generated at 2022-06-13 00:28:03.941881
# Unit test for function ansible_facts
def test_ansible_facts():

    from ansible.module_utils.facts import module_utils
    from ansible.modules.system.setup import setup_module_impl as setup_module
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    import ansible.module_utils.facts.network.distribution.redhat as redhat_network_dist_facts
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils.facts import ansible_collector
    import ansible.module_utils.facts.system.distribution.redhat as redhat_dist_facts

    import os
    import sys
    import mock

    # gets created by AnsibleModule
    class FakeModule(object):
        pass


# Generated at 2022-06-13 00:28:14.738170
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils.facts import LegacyCollector, PrefixFactNamespace
    from ansible.module_utils.facts import ansible_collector

    class C(LegacyCollector):
        @property
        def fact_list(self):
            return ['foo']

        def collect(self, module=None, collected_facts=None):
            return {'foo': 5}

    tmp_collector_classes = default_collectors.copy()
    tmp_collector_classes[C.namespace] = C


# Generated at 2022-06-13 00:28:32.534899
# Unit test for function ansible_facts
def test_ansible_facts():
    import ansible.module_utils
    from ansible.module_utils.facts import get_all_facts
    from ansible.module_utils._text import to_text

    m = ansible.module_utils.basic.AnsibleModule(
            argument_spec = dict(
                    gather_subset=dict(default='all', type='list')
                    ),
            supports_check_mode=True,
        )
    # Once we have a module that supports gather_subset, we can test with
    # gather_subset=['local', 'network', 'cmdline']

    all_facts = get_all_facts(module=m)

    # TODO: assert that all facts have non-empty value
    for fact, value in all_facts.items():
        assert value is not None
        assert fact in all_facts

    # TOD

# Generated at 2022-06-13 00:28:35.705999
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.basic import AnsibleModule
    test_module = AnsibleModule(argument_spec={})
    facts = ansible_facts(test_module)
    assert not facts.keys()

# Generated at 2022-06-13 00:28:43.901739
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils.facts import ansible_collector

    gather_subset = ['all']
    gather_timeout = 10

    minimal_gather_subset = frozenset(['apparmor', 'caps', 'cmdline', 'date_time',
                                       'distribution', 'dns', 'env', 'fips', 'local',
                                       'lsb', 'pkg_mgr', 'platform', 'python', 'selinux',
                                       'service_mgr', 'ssh_pub_keys', 'user'])

    all_collector_classes = default_collectors.collectors

    # don't add a prefix to facts
    namespace = PrefixFactNamespace

# Generated at 2022-06-13 00:28:54.811017
# Unit test for function get_all_facts
def test_get_all_facts():
    import ansible.module_utils.facts.namespace

    class MockModule:
        class Facts:
            class Fact:
                pass

        def __init__(self):
            self.params = {'gather_subset': ['!all', 'network']}

        def get_option(self, _):
            return None

    class MockFact:
        def __init__(self, name=None, value=None, namespace=None):
            self.name = name
            self.value = value
            self.namespace = namespace

    # Setup facts
    ansible.module_utils.facts.namespace.FACTS_CACHE = [MockFact('ios_facts', 'value', 'ansible_')]

    # Call get_all_facts
    facts = get_all_facts(MockModule())

    # Check

# Generated at 2022-06-13 00:28:55.224829
# Unit test for function get_all_facts
def test_get_all_facts():
    pass

# Generated at 2022-06-13 00:29:05.749749
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils.six import PY3
    if not PY3:
        try:
            import ansible.module_utils.facts.legacy
            module_utils_facts_legacy = ansible.module_utils.facts.legacy
        except ImportError:
            from ansible.module_utils.facts import legacy
            module_utils_facts_legacy = legacy

        get_all_facts = module_utils_facts_legacy.get_all_facts
    else:
        get_all_facts = ansible.module_utils.facts.get_all_facts

    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(
        argument_spec=dict(
            gather_subset=dict(default=['all'], type='list'),
        ),
    )

   

# Generated at 2022-06-13 00:29:08.634380
# Unit test for function ansible_facts
def test_ansible_facts():
    class MockModule():
        params = {'gather_subset': ['all']}

    mock_module = MockModule()
    facts = ansible_facts(module=mock_module)

    # just assert something in the returned fact dict.
    assert 'distribution' in facts

# Generated at 2022-06-13 00:29:14.150601
# Unit test for function get_all_facts
def test_get_all_facts():
    import sys

    # An AnsibleModule object will be mocked to return the bare facts
    # dictionary.
    class AnsibleModule(object):
        def __init__(self, *args, **kwargs):
            self.params = dict()

        def param(self, arg, *args, **kwargs):
            return self.params.get(arg)

    sys.modules['ansible.module_utils.facts.namespace'] = sys.modules[__name__]
    sys.modules['ansible.module_utils.facts'] = sys.modules[__name__]

    # ansible_facts() checks for this attribute.
    module = AnsibleModule()

    # Facts are keyed by bare fact name.
    facts = dict(ansible_distribution='my_distro')

    # Create a bare facts dictionary from the facts dictionary.


# Generated at 2022-06-13 00:29:20.816301
# Unit test for function ansible_facts
def test_ansible_facts():
    # Mock up module and gather_subset params
    import ansible.module_utils.facts.ansible_facts as af
    import ansible.module_utils.facts.collector as collector
    import ansible.module_utils.facts.namespace as namespace

    class MockModule:
        class MockAnsibleModule(object):
            def __init__(self, module_args, facts_module=True, **kwargs):
                self.params = module_args

        def __init__(self, module_args, facts_module=True, **kwargs):
            self.mock_ansible_module = self.MockAnsibleModule(module_args, facts_module=facts_module, **kwargs)


# Generated at 2022-06-13 00:29:22.584211
# Unit test for function ansible_facts
def test_ansible_facts():
    facts_dict = ansible_facts(None)
    assert isinstance(facts_dict, dict)


# Generated at 2022-06-13 00:29:43.501471
# Unit test for function ansible_facts
def test_ansible_facts():
    # pylint: disable=unused-variable
    class FakeModule(object):
        # Added to make pylint happy
        def __init__(self, *args, **kwargs):
            self.params = dict()
            self.params['filter'] = '*'

        # Added to make pylint happy
        def fail_json(self, *args, **kwargs):
            pass

    module = FakeModule()

    facts_dict = ansible_facts(module=module)

    assert facts_dict.get('selinux') is not None

# Generated at 2022-06-13 00:29:54.694885
# Unit test for function ansible_facts
def test_ansible_facts():
    import os
    import tempfile
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils.facts import ansible_collector
    import ansible.module_utils.facts.system.distribution

    class MockAnsibleModule:
        def __init__(self, facts_dict=None):
            self.params = {'filter': '*'}
            self.facts = facts_dict

        def exit_json(self, **kwargs):
            if 'ansible_facts' in kwargs:
                self.facts = kwargs['ansible_facts']
            else:
                self.facts = None


    # Test for empty result

# Generated at 2022-06-13 00:30:02.513679
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils.facts import get_all_facts
    import re

    get_all_facts.__module__ = 'ansible.module_utils.facts'
    get_all_facts.__name__ = 'get_all_facts'

    # get_all_facts is the same as the version that get_all_facts was split back into in 2.2
    facts_module = {
        'get_all_facts': get_all_facts,  # used by ansible 2.0/2.1/2.2 modules
        'ansible_facts': ansible_facts,  # used by ansible 2.3+ modules
    }

    class AnsibleModule(object):
        pass

    module = AnsibleModule()
    module.params = {'gather_subset': ['all']}

    facts = get

# Generated at 2022-06-13 00:30:14.596509
# Unit test for function ansible_facts
def test_ansible_facts():
    '''Unit test for function ansible_facts.'''

    from ansible.module_utils.facts import ansible_facts

    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils.facts import gather_subset
    from ansible.module_utils.facts import gather_timeout
    from ansible.module_utils.facts import minimal_gather_subset

    class MockModule(object):
        def __init__(self, params):
            self.params = params

    collected_facts = ansible_facts(MockModule({'gather_subset': gather_subset}))

    assert collected_facts is not None

    # check that the minimal set of facts are collected, with the expected keys
    assert set(collected_facts.keys()) == minimal_gather_subset

# Generated at 2022-06-13 00:30:21.568458
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.six import iteritems

    class FakeBaseFactCollector(BaseFactCollector):
        def collect(self, module=None, collected_facts=None):
            return collected_facts

    # return a faked fact value
    class FakeModule(object):
        def __init__(self, gather_subset=None, params=None):
            self.params = params

    # mock
    def mock_ansible_facts(module, gather_subset=None):
        res = {'fact_with_ansible_prefix': 'value_1',
               'not_a_fact': 'value_2'}
        return res

    old_ansible_facts = ansible_facts
    ansible_facts = mock_ansible_

# Generated at 2022-06-13 00:30:32.964528
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts import ansible_facts
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.compat.misc import missing_compat_util

    class FakeAnsibleModule:
        def __init__(self):
            self.params = {}

        def get_bin_path(self, executable, required=True, opt_dirs=[]):
            return executable

        def get_module_path(self):
            return 'tests/module_utils/facts'

        def get_os_family(self):
            return 'NotImplementedError'

        def fail_json(self, msg):
            assert False, to_bytes(msg)

        def warn(self, msg):
            assert False, to_bytes(msg)


# Generated at 2022-06-13 00:30:42.689034
# Unit test for function ansible_facts
def test_ansible_facts():
    import pytest
    from ansible.module_utils.facts import ansible_collector

    GATHER_SUBSET = ['network']
    FILTER_SPEC = 'ansible_lo*'

    class FakeAnsibleModule(object):
        def __init__(self):
            self.params = {}
            self.params['filter'] = 'ansible_lo*'

    class DummyCollector(object):
        def __init__(self, **kwargs):
            pass

    class DummyFactCollector(ansible_collector.BaseFactCollector):
        name = "dummy"
        _fact_class = DummyCollector
        _fact_ids = frozenset(['ansible_loopback'])

    all_collectors = [DummyFactCollector]

    module = FakeAnsibleModule()


# Generated at 2022-06-13 00:30:43.734200
# Unit test for function ansible_facts
def test_ansible_facts():
    assert ansible_facts({}, gather_subset=['!all']) == {}

# Generated at 2022-06-13 00:30:54.154416
# Unit test for function get_all_facts
def test_get_all_facts():
    import ansible.module_utils.facts.network

    class FakeAnsibleModule:
        def __init__(self):
            self.params = {'gather_subset': ['all']}

    fake_module = FakeAnsibleModule()
    ansible.module_utils.facts.network.get_interfaces_info = lambda: [{'name': 'eth0', 'ipv4': {'address': '1.2.3.4'}}]

    facts = get_all_facts(fake_module)


# Generated at 2022-06-13 00:31:01.608358
# Unit test for function ansible_facts
def test_ansible_facts():
    module = AnsibleModule(argument_spec=dict(gather_subset=dict(default=['all']),
                                              gather_timeout=dict(default=10, type='int'),
                                              filter=dict(default='*'),
                                              ansible_facts=dict(default=dict(), type='dict')))

    ansible_facts = ansible_facts(module)
    return module.exit_json(ansible_facts=ansible_facts)



# Generated at 2022-06-13 00:31:39.875686
# Unit test for function ansible_facts
def test_ansible_facts():

    class FakeModule:
        class FakeParams:
            gather_subset = ['all']
            gather_timeout = 10
            filter = '*'

        params = FakeParams()

    module = FakeModule()

    facts = ansible_facts(module)
    assert facts['lsb']['codename'] == 'xenial'
    assert facts['distribution_release'] == '16.04'
    assert facts['fqdn'] == 'xenial.local'

# Generated at 2022-06-13 00:31:51.179135
# Unit test for function ansible_facts
def test_ansible_facts():
    import sys
    import ansible.module_utils.facts.default_collectors as F

    for k,v in sys.modules.items():
        if k.startswith('ansible'):
            del sys.modules[k]
    from units.compat import unittest
    from units.compat.mock import patch
    from ansible.module_utils._text import to_bytes, to_native
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils.facts import ansible_collector

    class FakeModule(object):
        def __init__(self, params):
            self.params = params


# Generated at 2022-06-13 00:32:01.394685
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts import Facts

    # this will be needed by the fact collector, unfortunately
    import collections

    import os
    import pwd

    # Basic sanity test for ansible_facts.

    # Create and populate a module object.
    module_path = '/tmp/ansible_test_facts_playbook'
    if not os.path.exists(module_path):
        os.makedirs(module_path)
    module_name = 'test_module_facts.py'
    module_file_path = os.path.join(module_path, module_name)

# Generated at 2022-06-13 00:32:06.911837
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils.facts import module
    module = module
    # Module parameters
    module.params = {
        'gather_subset': '!all,!min,!fact',
        'gather_timeout': 10,
    }

    ansible_facts = get_all_facts(module)
    assert isinstance(ansible_facts, dict)
    assert 'distribution' in ansible_facts
    assert 'default_ipv4' in ansible_facts

# Generated at 2022-06-13 00:32:13.962261
# Unit test for function get_all_facts
def test_get_all_facts():
    class FakeModule:
        def __init__(self, params):
            self.params = params

    module = FakeModule(params={'filter': '*', 'gather_subset': ['all'], 'gather_timeout': 10})
    facts_dict = get_all_facts(module)
    assert 'python' in facts_dict
    assert 'system' in facts_dict
    assert 'lsb' in facts_dict
    assert 'pkg_mgr' in facts_dict



# Generated at 2022-06-13 00:32:23.442795
# Unit test for function ansible_facts
def test_ansible_facts():
    import json
    import copy
    import sys

    from ansible.module_utils.facts import cache

    from collections import namedtuple

    from ansible.compat.tests import mock

    from ansible.module_utils.facts import namespaces

    from ansible.module_utils.facts import ansible_collector

    # py2/py3 compat
    if sys.version_info < (3,):
        text_type = unicode
    else:
        text_type = str

    def _json_serialize(obj):
        return json.dumps(obj, indent=2, sort_keys=True, default=_json_serialize)


# Generated at 2022-06-13 00:32:32.361579
# Unit test for function get_all_facts
def test_get_all_facts():

    # test with empty subset
    class MockModule(object):

        def __init__(self, gather_subset):
            self.params = dict(gather_subset=gather_subset)
    module = MockModule([])
    facts = get_all_facts(module)
    assert len(facts) > 0

    # test with a subset
    module = MockModule(['hardware'])
    facts = get_all_facts(module)
    assert len(facts) > 0

    # test with no subset specified
    module = MockModule(None)
    facts = get_all_facts(module)
    assert len(facts) > 0


# Generated at 2022-06-13 00:32:41.843871
# Unit test for function ansible_facts
def test_ansible_facts():
    '''Unit test for ansible_facts function. Verify it returns correct fact values'''

    try:
        from ansible.module_utils.facts import ansible_facts
    except ImportError:
        return

    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(
        argument_spec=dict(
            gather_subset=dict(type='list', required=False, default=['all']),
            gather_timeout=dict(type='int', required=False, default=10),
            filter=dict(type='str', required=False, default='*'),
        )
    )

    facts = ansible_facts(module=module)
    print('facts: %s' % facts)

    # FIXME: add asserts

if __name__ == '__main__':
    test_ansible_

# Generated at 2022-06-13 00:32:50.701125
# Unit test for function get_all_facts
def test_get_all_facts():
    import ansible.module_utils.facts.network.base
    import ansible.module_utils.facts.virtual

    def mock_ansible_module(*args, **kwargs):
        class AnsibleModule:
            def __init__(self, *args, **kwargs):
                self.params = {'gather_subset': ['network']}

        return AnsibleModule(*args, **kwargs)

    # Ensure that instances of interested collectors are returned for this test
    # We can then check if these collectors have the required methods

# Generated at 2022-06-13 00:33:01.478265
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts import _get_ansible_facts_module_mock
    from ansible.module_utils.facts.collector import BaseFactCollector

    module = _get_ansible_facts_module_mock()

    ansible_facts = ansible_facts(module)

    assert 'default_ipv4' in ansible_facts

    # truthy value
    assert ansible_facts['default_ipv4']['address']

    # truthy value
    assert ansible_facts['sysctl']['kernel']['osrelease']

    # falsey value
    assert not ansible_facts['default_ipv6']['address']

    # falsey value
    assert not ansible_facts['sysctl']['vm']['laptop_mode']



# Generated at 2022-06-13 00:34:10.380018
# Unit test for function ansible_facts
def test_ansible_facts():
    # test minimal facts
    assert ansible_facts(FakeModule(gather_subset=['!all', '!min'])) == {
        'gather_subset': frozenset(),
        'gather_timeout': 10,
        'localhost': {'ansible_python': {'version': (2, 7, 13, 'final', 0), 'executable': '/usr/bin/python'}},
        'minimal_facts_module': {'facts': {'facts': 'minimal facts'}},
        'module_setup': True
    }

    # test all facts