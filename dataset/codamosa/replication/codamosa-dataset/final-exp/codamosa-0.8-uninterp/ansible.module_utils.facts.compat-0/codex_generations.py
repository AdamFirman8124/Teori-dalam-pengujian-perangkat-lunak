

# Generated at 2022-06-13 00:24:17.426219
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts import get_all_subsets
    from ansible.module_utils.common._collections_compat import MutableMapping
    from ansible.module_utils.facts import get_all_subsets

    class MockAnsibleModule(MutableMapping):
        def __init__(self, gather_subsets):
            self._gather_subsets = gather_subsets

        def __getitem__(self, key):
            return self._gather_subsets[key]

        def __setitem__(self, key, value):
            self._gather_subsets[key] = value

        def __delitem__(self, key):
            del self._gather_subsets[key]

        def __iter__(self):
            return iter(self._gather_subsets)

# Generated at 2022-06-13 00:24:19.179208
# Unit test for function get_all_facts
def test_get_all_facts():
    # TODO: add unit test
    pass


# Generated at 2022-06-13 00:24:24.261524
# Unit test for function ansible_facts
def test_ansible_facts():
    import json
    module = MockAnsibleModule()
    gather_subset = frozenset(['default'])
    ansible_facts_dict = ansible_facts(module, gather_subset=gather_subset)

    print(json.dumps(ansible_facts_dict, indent=4))


# Generated at 2022-06-13 00:24:33.319663
# Unit test for function get_all_facts
def test_get_all_facts():
    import json
    import re
    import tempfile

    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils.facts import ansible_collector

    from ansible.module_utils.basic import AnsibleModule

    argspec = {'gather_subset': dict(default=['all'], type='list')}

    module = AnsibleModule(argument_spec=argspec)
    gather_subset = module.params['gather_subset']
    gather_timeout = module.params.get('gather_timeout', 10)
    filter_spec = module.params.get('filter', '*')


# Generated at 2022-06-13 00:24:40.552772
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts import default_collectors

    class FakeModule:
        params = {'gather_subset': ['all']}

    mymodule = FakeModule()

    gathered_facts = ansible_facts(module=mymodule)

    # ansible_facts must return a dict
    assert isinstance(gathered_facts, dict)

    # ansible_facts must contain a fact for each registered fact collector
    for fact_class in default_collectors.collectors:
        assert fact_class.name in gathered_facts

# Generated at 2022-06-13 00:24:53.365658
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts import  ansible_facts
    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils.facts import ansible_collector
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts.collector import FailingFactCollector
    from ansible.module_utils._text import to_text
    all_collector_classes = default_collectors.collectors

    # don't add a prefix
    namespace = PrefixFactNamespace(namespace_name='ansible', prefix='')

    filter_spec = '*'
    gather_subset = ['all']
    gather_timeout = 10

# Generated at 2022-06-13 00:25:04.350005
# Unit test for function ansible_facts
def test_ansible_facts():

    class MockModule:
        '''Mock class for AnsibleModule'''

        def __init__(self, gather_subset):
            self.params = {'gather_subset': gather_subset}

    class MockModuleWithTimeout:
        '''Mock class for AnsibleModule'''

        def __init__(self, gather_subset):
            self.params = {'gather_subset': gather_subset, 'gather_timeout': 123}

    class MockOsDistribution:
        '''Mock class for os_distribution collector.
        '''

        def __init__(self, dist_name):
            self.distribution = dist_name
            self.codename = ''

    class MockOsRelease:
        '''Mock class for os_release collector.
        '''


# Generated at 2022-06-13 00:25:15.312339
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils import basic
    from ansible.module_utils.facts.network.base import NetworkCollector as NetworkCollector
    from ansible.module_utils.facts.network.default import DefaultNetworkCollector as DefaultNetworkCollector

    class MyNetworkCollector(NetworkCollector):
        def __init__(self, *args, **kwargs):
            self.facts = {'facts_data': True}
            super(MyNetworkCollector, self).__init__(*args, **kwargs)

        def collect(self, module=None, collected_facts=None):
            self._collected_facts = self.facts
            return self.facts


# Generated at 2022-06-13 00:25:22.022769
# Unit test for function ansible_facts
def test_ansible_facts():
    _module = MockAnsibleModule()

    fact_collector = ansible_collector.get_ansible_collector(MockCollectorSubclass.__name__)
    fact_collector.collect(module=_module)

    # make sure the collector got instantiated
    assert MockCollectorSubclass.instantiated


# Generated at 2022-06-13 00:25:29.948660
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.facts.utils import get_file_content

    module = AnsibleModule(argument_spec=dict(
        gather_subset=dict(default=['all'], type='list'),
    ))

    # all_collectors_collections has been moved to a different name,
    # so we must do "fact_collector.default_collector_classes" instead of
    # "fact_collector.all_collectors_classes"
    fact_collector = \
        ansible_collector.get_ansible_collector(all_collector_classes=default_collectors.collectors,
                                                namespace=PrefixFactNamespace(namespace_name='ansible', prefix=''))

# Generated at 2022-06-13 00:25:37.963891
# Unit test for function get_all_facts
def test_get_all_facts():
    import mock
    import os
    import types

    module = mock.Mock()
    module.params = dict(gather_subset=['all'], gather_timeout=10, filter='*')
    module.get_bin_path.return_value = "/usr/bin/python"

    facts = get_all_facts(module)
    assert facts['python']['executable'] == "/usr/bin/python"

# Generated at 2022-06-13 00:25:46.772098
# Unit test for function ansible_facts
def test_ansible_facts():
    '''Unit test for function ansible_facts

    Should return a dict.
    Should raise a ValueError if passed a bogus collector name.
    Should raise a ValueError if passed a non-existent collector name.
    '''

    import pytest
    from ansible.module_utils.facts import collectors
    from ansible.module_utils.basic import AnsibleModule

    def _test_helper(module, filter='*', gather_subset=['all'], gather_timeout=10):
        '''helper for test_collect_subset and test_collect_subset_no_module_param'''

        if module:
            assume_gather_subset = module.params.get('gather_subset', ['all'])
            assume_gather_timeout = module.params.get('gather_timeout', 10)

            expect

# Generated at 2022-06-13 00:25:58.560895
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts import ansible_module_facts
    from ansible.module_utils.facts import ansible_collector
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts import default_collectors

    class TestCollector(Collector):
        name = 'test_collector_name'
        _fact_ids = ['test_collector_fact']

        def collect(self, module=None, collected_facts=None):
            return {'test_collector_fact': 'test_collector_fact_value'}

    old_fact_collectors = default_collectors.collectors
    default_collectors.collectors = []

# Generated at 2022-06-13 00:26:08.782295
# Unit test for function ansible_facts
def test_ansible_facts():
    # WARNING: the module_utils/facts.get_ansible_facts method changed its
    # signature between Ansible 2.0 and 2.1.
    # This test only covers the case where the first argument is a trivial stub AnsibleModule
    # See the unittest for module_utils/facts.get_all_facts for a more complete example.

    class MockAnsibleModule:
        def __init__(self):
            self.params = {}

    # Test that we have the expected api for ansible 2.0/2.1.
    # The get_all_facts method does not take an arg for gather_subset
    # in older versions of Ansible.
    # These versions of Ansible do not pass in a gather_subset arg.
    # So ansible_facts should be happy with or without an arg.
    ansible_facts

# Generated at 2022-06-13 00:26:18.991550
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.basic import AnsibleModule
    # Set up some fake args to pass to the AnsibleModule() constructor
    test_arg_spec = dict(
        gather_subset=dict(type='list'),
        gather_timeout=dict(type='int'),
        filter=dict(type='list'),
        ansible_facts=dict(type='dict', required=False),
    )
    # create the AnsibleModule instance
    module = AnsibleModule(argument_spec=test_arg_spec, support_check_mode=True)
    # call the method we're testing
    ansible_facts = ansible_facts(module)
    # test that the method returned a dict
    assert isinstance(ansible_facts, dict)

# Generated at 2022-06-13 00:26:24.225176
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils.facts import get_all_facts
    from ansible.module_utils.facts.collector.network import Network
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts.utils import _to_bytes
    import json

    # Mock module
    class MockModule(object):
        def __init__(self, params):
            self.params = params

    gather_subset = ['all']
    module = MockModule({'gather_subset': gather_subset})
    all_facts = get_all_facts(module)
    assert 'distribution' in all_facts
    # now test with 'network'
    gather_subset = ['network']
    module = MockModule({'gather_subset': gather_subset})

# Generated at 2022-06-13 00:26:36.456956
# Unit test for function ansible_facts
def test_ansible_facts():  # pylint: disable=redefined-outer-name
    '''Unit test for function ansible_facts

    This function is a wrapper around the function of the same name in the
    ansible.module_utils.facts.ansible_collector module, which is where the
    work is done.  The ansible.module_utils.facts.ansible_collector function is
    a partial, with several of its args are filled in/fixed.  This function
    unit tests by calling the ansible_collector function directly with the
    remainder of the arguments it would have gotten.
    '''

    # import module snippets
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils.facts import ansible_collector

    all_collector_classes

# Generated at 2022-06-13 00:26:38.751579
# Unit test for function ansible_facts
def test_ansible_facts():
    module = FakeAnsibleModule()

    assert isinstance(ansible_facts(module), dict)


# Generated at 2022-06-13 00:26:46.733967
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts import module_prefix_sorter

    try:
        from ansible.module_utils.facts import LazyDict
    except ImportError:
        from ansible.module_utils.facts import LazyDict2 as LazyDict

    try:
        from unittest import mock
    except ImportError:
        import mock

    from ansible.module_utils.facts import default_collectors

    # test default path
    LazyDict.__str__ = lambda self: 'test'

# Generated at 2022-06-13 00:26:55.537695
# Unit test for function ansible_facts
def test_ansible_facts():
    '''unit test for module_utils.facts.ansible_facts'''

    # TODO: figure out if there is a better way to test things that stub/mock AnsibleModule
    # Maybe a 'module_utils' pytest fixture that creates a custom module factory?

    # stub AnsibleModule
    class StubAnsibleModule(object):
        def __init__(self):
            self.params = {'filter': '*', 'gather_subset': ['all'], 'gather_timeout': 10}

    module = StubAnsibleModule()

    # module.params = {'filter': '*', 'gather_subset': ['all'], 'gather_timeout': 10}

    facts = ansible_facts(module)

    assert 'distribution' in facts

    # TODO: write more tests for ansible_facts

# Generated at 2022-06-13 00:27:06.230435
# Unit test for function ansible_facts
def test_ansible_facts():
    import sys
    import ansible.module_utils.facts.__init__

    class AnsibleModule(object):
        def __init__(self, params=None, facts=None):
            self.params = params
            self.facts = facts
            self.add_legacy_facts = False

    def fail_json(*args, **kwargs):
        if args:
            msg = args[0]
            raise Exception('AnsibleModule.fail_json() called with: ' + msg)
        else:
            raise Exception('AnsibleModule.fail_json() called.')

    def exit_json(**kwargs):
        if kwargs:
            raise Exception('AnsibleModule.fail_json() called with: ' + str(kwargs))


    # This test validates that the facts that are gathered when only a subset of

# Generated at 2022-06-13 00:27:14.373962
# Unit test for function ansible_facts
def test_ansible_facts():
    import unittest
    import sys
    from ansible.module_utils.six import PY3
    from ansible.module_utils.facts import ansible_collector
    from ansible.module_utils.facts import collector

    if sys.version_info[0] == 3 and sys.version_info[1] >= 4:
        from unittest import mock
    else:
        import mock

    ns = PrefixFactNamespace(namespace_name='ansible', prefix='')
    fs = frozenset(['all'])

    class TestAnsibleFacts(unittest.TestCase):
        '''Unit test for function ansible_facts'''


# Generated at 2022-06-13 00:27:25.657054
# Unit test for function get_all_facts
def test_get_all_facts():
    import ansible.module_utils.facts.networking

    from ansible.module_utils.facts.system import distribution
    from ansible.module_utils.facts.system import platform

    from ansible.module_utils.facts.virtual import virtual

    datetime_namespace = ansible.module_utils.facts.datetime.datetime
    network_namespace = ansible.module_utils.facts.networking.network
    default_ipv4_namespace = ansible.module_utils.facts.networking.default_ipv4
    default_ipv6_namespace = ansible.module_utils.facts.networking.default_ipv6


# Generated at 2022-06-13 00:27:30.588601
# Unit test for function ansible_facts
def test_ansible_facts():
    import mock
    from ansible.module_utils import basic

    gather_subset = ['all', 'network']

    module = mock.MagicMock()
    module.params = {'gather_subset': gather_subset}
    module.params.get.side_effect = lambda k, f: {'gather_subset': gather_subset}[k]
    module.run_command = mock.MagicMock(return_value=(0, 'some output', ''))
    module.exists.return_value = True
    module.read_file = mock.MagicMock(return_value='some contents')
    module.which = mock.MagicMock(return_value='/some/path')
    module.get_bin_path = mock.MagicMock(return_value='/some/path')
    module.register

# Generated at 2022-06-13 00:27:42.762481
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils._text import to_text
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils.facts import ansible_collector

    class FakeModule():
        def __init__(self):
            self.params = dict()
            self.params['gather_subset'] = 'all'

            # FakeModule is a stub and doesn't gather anything

    fake_module = FakeModule()
    results = get_all_facts(fake_module)

    assert isinstance(results, dict)
    assert 'default_ipv4' in results
    assert 'default_ipv4' in results
    assert 'all_ipv4_addresses' in results



# Generated at 2022-06-13 00:27:53.626184
# Unit test for function ansible_facts
def test_ansible_facts():
    # Need a fake module with a few params.
    class FakeModule(object):
        def __init__(self, params):
            self.params = params
            self._filter = params['filter']

        def set_filter(self, filter):
            self._filter = filter

        # The 'filter' property. Not called by ansible_facts but by the ansible_collector
        # that ansible_facts calls.
        @property
        def filter(self):
            return self._filter

    # Test collect all facts
    params = dict(
        gather_subset=['all'],
        filter='*',
    )
    module = FakeModule(params)


# Generated at 2022-06-13 00:28:00.310417
# Unit test for function get_all_facts
def test_get_all_facts():
    import collections
    import ansible.module_utils.facts.ansible_collector as ansible_collector
    import ansible.module_utils.facts.namespace as namespace
    import ansible.module_utils.facts.collector as collector

    # Override the ansible_collector.get_ansible_collector with a stub
    # This stub will create a single test Collector class, whose collect method
    # returns a predictable dict with a single key/value pair.
    class TestCollector(collector.Collector):
        def collect(self, module=None):
            return {'test' : 'test'}

    # Stub out get_ansible_collector method.

# Generated at 2022-06-13 00:28:02.865033
# Unit test for function ansible_facts
def test_ansible_facts():
    class FakeModule:
        params = dict(gather_timeout=10, filter='*')

    facts = ansible_facts(FakeModule())
    assert 'distribution' in facts
    assert facts['distribution']['full'] == 'Devuan GNU/Linux'

# Generated at 2022-06-13 00:28:13.777375
# Unit test for function ansible_facts
def test_ansible_facts():
    import ansible.module_utils.facts.network
    import ansible.module_utils.facts.system
    import ansible.module_utils.facts.virtual

    import tempfile
    tmp_file = tempfile.mkstemp()
    tmp_dir = tempfile.mkdtemp()
    mk_fake_facts_module(tmp_dir)


# Generated at 2022-06-13 00:28:19.662968
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils.basic import AnsibleModule

    gather_timeout = 5

    module = AnsibleModule(
        argument_spec=dict(
            gather_timeout=dict(type='int', default=gather_timeout),
            gather_subset=dict()
        )
    )

    facts = get_all_facts(module=module)

    assert type(facts) is dict

# Generated at 2022-06-13 00:28:31.362070
# Unit test for function get_all_facts
def test_get_all_facts():
    class Module(object):
        params = {'gather_subset': ['all']}

    module = Module()
    facts = get_all_facts(module)
    assert isinstance(facts, dict)
    assert 'ansible_default_ipv4' in facts


# Generated at 2022-06-13 00:28:40.900279
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts import ansible_facts
    from ansible.module_utils._text import to_bytes, to_text
    import sys
    import tempfile
    import shutil
    import os

    test_args = [sys.executable, '-c',
                 'from ansible.module_utils.facts import ansible_facts; print(ansible_facts())']

    test_env = os.environ.copy()
    test_env['ANSIBLE_COLLECTIONS_PATHS'] = '/tmp/mock_collections'
    test_env['ANSIBLE_STRICT'] = 'False'
    test_env['ANSIBLE_NOCOWS'] = 'True'

# Generated at 2022-06-13 00:28:52.922979
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils._text import to_bytes
    import json
    import os
    import tempfile

    # Temporary ansible.cfg file for testing gather_subset config option
    (fd, config_file) = tempfile.mkstemp()
    with os.fdopen(fd, 'w') as tmp:
        tmp.write('[defaults]\n')
        tmp.write('gather_subset = hardware, virtual, network\n')

    os.environ['ANSIBLE_CONFIG'] = config_file
    os.environ['ANSIBLE_COLLECTIONS_PATHS'] = ''

    # Create a fake AnsibleModule object, since we're not running this in Ansible
    class FakeAnsibleModule(object):
        def __init__(self, params={}):
            self.params = params


# Generated at 2022-06-13 00:28:53.523246
# Unit test for function ansible_facts
def test_ansible_facts():
    pass

# Generated at 2022-06-13 00:29:00.792420
# Unit test for function ansible_facts
def test_ansible_facts():
    import ansible.module_utils.facts.collector.network as network_collector

    # values we'll expect in facts_dict
    os_family = 'RedHat'
    lsb_distributor_id = 'CentOS'
    lsb_distributor_id_lower = lsb_distributor_id.lower()
    lsb_version = '7.3.1611'

    # stub module
    class _AnsibleModule:
        def __init__(self):
            self.params = dict()

    class _AnsibleModule2:
        def __init__(self):
            self.params = dict(gather_subset='default')

    def _ret_false(self):
        return False

    def _ret_true(self):
        return True


# Generated at 2022-06-13 00:29:09.190666
# Unit test for function get_all_facts
def test_get_all_facts():
    import ansible.module_utils.facts.system.system
    ansible.module_utils.facts.system.system.DEFAULT_GATHER_SUBSET = ['all']
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts import get_all_facts

    module_mock = type('AnsibleModule', (object,), dict(
        params=dict(
            gather_subset=['all'],
            gather_timeout=0.5,
            filter='*',
            config_file=''
        )
    ))
    module_mock.params['ANSIBLE_MODULE_ARGS'] = module_mock.params
    module_mock.fail_json = lambda **kwargs: None
    module_mock.exit_json = lambda **kwargs: None

# Generated at 2022-06-13 00:29:18.030371
# Unit test for function get_all_facts
def test_get_all_facts():

    from ansible.module_utils.facts.facts import AnsibleFakeFactCollector
    from ansible.module_utils.facts.facts import AnsibleFakeFacts
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    import inspect
    import os

    module_file = inspect.getfile(AnsibleFakeFactCollector)
    path = os.path.dirname(module_file)
    lib_path = os.path.join(path, 'lib')
    if os.path.exists(lib_path):
        sys.path.append(lib_path)

    import AnsibleModuleMock

    class FakeModule(object):
        params = dict()

        def _load_params(self):
            return


# Generated at 2022-06-13 00:29:28.303734
# Unit test for function ansible_facts
def test_ansible_facts():
    '''
    Unit test for function ansible_facts
    '''

    # Mock a module. The imported ansible.module_utils.facts.collector uses certain modules like
    # ansible.module_utils.facts.system.distribution to determine the distribution name and version.
    # So we also need to patch these modules in the test.
    from ansible.module_utils.facts import system

    # define the mock module with minimal necessary attrs

# Generated at 2022-06-13 00:29:39.907185
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts.collector import CollectedFilter
    from ansible import context
    from ansible.module_utils._text import to_bytes

    # context.CLIARGS object was not getting populated during ansible-test network test execution
    # So force populate it here

# Generated at 2022-06-13 00:29:44.087610
# Unit test for function ansible_facts
def test_ansible_facts():
    module = DummyAnsibleModule()
    facts = ansible_facts(module)

    assert isinstance(facts, dict)


# Dummy class to allow test_ansible_facts to run without failing with an AttributeError
# on missing ansible.module_utils.basic.AnsibleModule

# Generated at 2022-06-13 00:30:10.347213
# Unit test for function ansible_facts
def test_ansible_facts():

    # create a fake module for facts to use
    class FakeModule:
        def __init__(self):
            self.params = {
                'gather_subset': None,
                'gather_timeout': 10,
                'filter': '*',
            }

        def fail_json(self, msg):
            raise AssertionError(msg)

    fake_module = FakeModule()

    # invoke the ansible_facts collector
    ansible_facts_result = ansible_facts(fake_module)

    # iterate through the resulting dict.
    # Check that each value is not empty
    for k, v in list(ansible_facts_result.items()):
        assert v is not None

# Generated at 2022-06-13 00:30:21.787845
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils.facts import ansible_collector
    # pylint: disable=unused-argument
    class AnsibleModule:
        def __init__(self, argument_spec=None, bypass_checks=False, no_log=False,
                     check_invalid_arguments=True, mutually_exclusive=None, required_together=None,
                     required_one_of=None, add_file_common_args=False,
                     supports_check_mode=False):
            self.params = {}
            self.params['gather_subset'] = ['all']
    gather_subset = ['all']
    m = AnsibleModule()

# Generated at 2022-06-13 00:30:32.744565
# Unit test for function ansible_facts
def test_ansible_facts():
    from mock import MagicMock, patch

    module_patcher = patch('ansible.module_utils.facts.default_collectors.AnsibleModule')
    module_patcher.start()
    module = MagicMock()

    module.params = {'gather_subset': ['all'], 'gather_timeout': 10, 'filter': '*'}

    fact_patcher = patch('ansible.module_utils.facts.collector.FactCollector')
    fact_patcher.start()
    facts_patcher = patch('ansible.module_utils.facts.collector.Facts')
    facts_patcher.start()

    ansible_facts(module)

    fact_patcher.stop()
    facts_patcher.stop()
    module_patcher.stop()

# Generated at 2022-06-13 00:30:38.114703
# Unit test for function ansible_facts
def test_ansible_facts():
    '''Run the ansible_facts function against a mock Ansible Module.'''
    import sys
    try:
        from unittest import mock
    except ImportError:
        import mock

    mock_ansible_module = mock.Mock()
    mock_ansible_module.params = None
    mock_ansible_module.params.get.return_value = 'all'

    all_facts_dict = ansible_facts(module=mock_ansible_module)

    # TODO: should we validate more than the type of the returned data structure?

    assert isinstance(all_facts_dict, dict)

# Generated at 2022-06-13 00:30:42.722582
# Unit test for function ansible_facts
def test_ansible_facts():

    class FakeModule:
        def __init__(self,
                     params=dict(gather_subset=['all'], gather_timeout=10)):
            self.params = params

    module = FakeModule()

    result = ansible_facts(module)
    assert 'default_ipv4' in result


# Generated at 2022-06-13 00:30:46.258109
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts import ModuleStub

    module = ModuleStub()
    module.params = {'gather_subset': ['all'], 'gather_timeout': 10}

    fact_dict = ansible_facts(module)

    # check that all_facts is a dict
    assert isinstance(fact_dict, dict)

    # check that the dict is not empty
    assert len(fact_dict) > 0

# Generated at 2022-06-13 00:30:48.438268
# Unit test for function get_all_facts
def test_get_all_facts():
    '''Test the get_all_facts function

    Nothing to test right now.
    '''
    pass


# Generated at 2022-06-13 00:30:56.662807
# Unit test for function get_all_facts
def test_get_all_facts():
    class AnsibleModule(object):
        '''mock for an AnsibleModule'''
        def __init__(self, params):
            self.params = params

    # test with subset specified.
    module = AnsibleModule({'gather_subset': ['min']})
    fact_names = get_all_facts(module).keys()

    assert('distribution' in fact_names)
    assert('version' not in fact_names)

    # test with subset not specified
    module = AnsibleModule({})
    fact_names = get_all_facts(module).keys()

    assert('distribution' in fact_names)
    assert('version' in fact_names)

# Generated at 2022-06-13 00:31:08.112531
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts.collector.network import Network


# Generated at 2022-06-13 00:31:15.810405
# Unit test for function ansible_facts
def test_ansible_facts():
    import ansible.module_utils.facts.namespace
    import ansible.module_utils.basic
    import ansible.module_utils.facts.collectors.cpu
    import ansible.module_utils.facts.collectors.distribution
    import ansible.module_utils.facts.collectors.kernel
    import ansible.module_utils.facts.collectors.pkg_mgr

    # Return several of each fact type.
    # All facts should be returned if gather_subset is ['all']
    # Only minimal facts should be returned if gather_subset is None
    # If a requested fact is not availible, the fact should not be returned
    mock_module = ansible.module_utils.basic.AnsibleModule(argument_spec=dict())

    # Setup a 'distribution' fact collector that returns two facts

# Generated at 2022-06-13 00:31:55.248081
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.basic import AnsibleModule

    # simple test to make sure we can get a fact value
    module = AnsibleModule({'gather_timeout': 10, 'filter': 'ansible_default_ipv4'}, check_invalid_arguments=False,
                           bypass_checks=True)

    facts_dict = ansible_facts(module)

    assert 'default_ipv4' in facts_dict
    assert facts_dict['default_ipv4']['address'] == '127.0.0.1'

# Generated at 2022-06-13 00:32:05.865478
# Unit test for function get_all_facts
def test_get_all_facts():
    '''Tests for function ansible_internal.module_utils.facts.get_all_facts'''

    from ansible.module_utils.facts import get_all_facts
    from ansible.module_utils.facts import ansible_facts

    from ansible.module_utils.facts._fact_cache import fact_cache

    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.parsing.convert_bool import boolean

    # load cache with test facts
    fact_cache.update({'test1': 'value1', 'test2': 'value2'})

    # test with gathering enabled, gather_subset not specified

# Generated at 2022-06-13 00:32:15.985617
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    # test get_all_facts method
    # using dummy AnsibleModule
    class AnsibleModule:
        def __init__(self):
            self.params = {}
            self.params['gather_subset'] = ['all']

    module = AnsibleModule()
    bare_fact_names_to_facts = get_all_facts(module)
    assert 'ansible_lsb' in bare_fact_names_to_facts

    # test ansible_facts method
    bare_fact_names_to_facts = ansible_facts(module)
    assert 'ansible_lsb' in bare_fact_names_to_facts

    # test ansible_facts method with gather_subset argument

# Generated at 2022-06-13 00:32:25.704253
# Unit test for function ansible_facts
def test_ansible_facts():
    '''
    unit test for ansible_facts

    This is a unit test for ansible_facts, which is a compatibility wrapper for the
    facts.ansible_facts method.

    AnsibleModule is a mock object which provides the minimal number of attributes needed
    by ansible_facts - in this case, the attribute 'params', which is a dict.

    The 'params' dict itself is also mocked, and could be set to any reasonable configuration.
    In this case, we use a minimal configuration, and assert that we get the expected results.
    '''

    mock_AnsibleModule = MagicMock()
    mock_AnsibleModule.params = {'filter': 'ansible_distribution*'}
    facts_dict = ansible_facts(mock_AnsibleModule)
    ansible_distribution = facts_dict['distribution']


# Generated at 2022-06-13 00:32:34.480832
# Unit test for function ansible_facts
def test_ansible_facts():
    # ansible_facts expects an AnsibleModule instance, but we don't want to
    # need Ansible to do unit tests. So create a dummy class instance with
    # a gather_subset attribute that looks like the AnsibleModule params
    # gather_subset attribute.
    class DummyAnsibleModule:
        def __init__(self):
            self.params = {'gather_subset': ['!all', 'network']}

    fact_dict = ansible_facts(DummyAnsibleModule())

    assert 'network' in fact_dict, 'Gather network facts'
    assert 'all' not in fact_dict, "Do not gather 'all's facts"

# Generated at 2022-06-13 00:32:43.878938
# Unit test for function ansible_facts
def test_ansible_facts():
    import pytest

    try:
        from ansible.module_utils.facts import ansible_facts
        from ansible.module_utils.facts.namespace import PrefixFactNamespace
    except ImportError:
        pytest.skip("this module_utils.facts helper function is only used in ansible 2.3 and up")
        return

    class FakeModule:
        class FakeParams(object):
            gather_subset = None
            gather_timeout = 10
            filter = 'ansible_*'

        def __init__(self):
            self.params = self.FakeParams()

        def get_option(self, option):
            return self.params.get(option)

    # Make sure that gather_subset is optional
    fact_collector = FakeModule()

# Generated at 2022-06-13 00:32:50.401579
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts.platform.base import PlatformFactCollector
    from ansible.module_utils.facts.network.base import NetworkFactCollector
    from ansible.module_utils.facts.system.base import SystemFactCollector

    class MockModule():
        params = {
            'gather_subset': ['all'],
            'gather_timeout': 10,
            'filter': '*',
        }

    mock_module = MockModule()
    print(ansible_facts(module=mock_module))
    print(ansible_facts(module=mock_module, gather_subset=['platform', 'network', 'system']))

# Generated at 2022-06-13 00:33:01.213312
# Unit test for function ansible_facts
def test_ansible_facts():
    '''compat api for ansible 2.2/2.3 module_utils.facts.get_all_facts method

    Expects module to be an instance of AnsibleModule, with a 'gather_subset' param.

    returns a dict mapping the bare fact name ('default_ipv4' with no 'ansible_' namespace) to
    the fact value.'''

    import ansible.module_utils.facts.system.distribution as distribution_module

    # setup the mock module args
    module_params = {
        'gather_subset': ['all'],
        'gather_timeout': 10,
        'filter': '*'
    }
    module = type('module', (object,), module_params)

    # run the ansible_facts function
    facts = ansible_facts(module=module)

    # verify

# Generated at 2022-06-13 00:33:06.364156
# Unit test for function get_all_facts
def test_get_all_facts():
    '''Test get_all_facts function.

    This is an example test module. It has a single testing function, which
    can be executed by executing the test module.

    This test module tests the get_all_facts function. It requires a `pytest`
    framework installed.
    '''
    pass

# Generated at 2022-06-13 00:33:14.724652
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils.facts.collector import get_all_collectors
