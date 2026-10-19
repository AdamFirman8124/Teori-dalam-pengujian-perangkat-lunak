

# Generated at 2022-06-13 00:24:16.968916
# Unit test for function ansible_facts
def test_ansible_facts():
    import os
    import sys
    import unittest

    from ansible.module_utils import facts as mutils

    class TestFacts(unittest.TestCase):
        def setUp(self):
            '''set up a stub for AnsibleModule with a gather_subset param'''
            self.ansible_module = AnsibleModuleStub(params={'gather_subset': ['all']})

        def test_get_all_facts(self):
            results = mutils.get_all_facts(self.ansible_module)
            self.assertIsInstance(results, dict)
            self.assertGreater(len(results), 0)

        def test_ansible_facts(self):
            results = mutils.ansible_facts(self.ansible_module)

# Generated at 2022-06-13 00:24:28.078414
# Unit test for function ansible_facts
def test_ansible_facts():

    # Use the AnsibleModule fixture to create a mock module which will be used in our tests
    test_module = AnsibleModule(argument_spec={'gather_subset': dict(type='list', default=['all'])})

    # build a test facts_dict, with one fact per collector
    collectors = default_collectors.collectors
    statistics = {}

    # test_facts_dict maps bare fact name (no 'ansible_' namespace) to the fact value.
    # It is what ansible_facts(...) is expected to return
    test_facts_dict = {}
    for collector_class in collectors:
        collector = collector_class()

        # make up a test fact, e.g. ansible_distribution_release == 'test_distribution_release'
        fact_key = collector_class.__name__.lower()


# Generated at 2022-06-13 00:24:36.221709
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils.basic import AnsibleModule

    gather_facts = True
    gather_subset = [ 'all' ]

    mock_module = AnsibleModule(argument_spec={
        'gather_facts': { 'default': gather_facts },
        'gather_subset': { 'default': gather_subset }
    })

    facts_dict = ansible_facts(mock_module, gather_subset)

    assert 'ansible_default_ipv4' in facts_dict.keys()
    assert isinstance(facts_dict['ansible_default_ipv4'], dict)

    assert 'ipv4' in facts_dict['ansible_default_ipv4'].keys()

# Generated at 2022-06-13 00:24:36.576103
# Unit test for function get_all_facts
def test_get_all_facts():
    pass

# Generated at 2022-06-13 00:24:45.291438
# Unit test for function ansible_facts

# Generated at 2022-06-13 00:24:55.866774
# Unit test for function ansible_facts
def test_ansible_facts():
    # Create a fake module
    class FakeModule(object):
        def __init__(self, gather_subset):
            self.params = {
                'gather_subset': gather_subset,
                'filter': None,
                'gather_timeout': None,
            }

        def fail_json(self, **kwargs):
            pass

        @staticmethod
        def get_bin_path(binary, required=True, opt_dirs=[]):
            return binary

    # Test with gather_subset unset.
    # This test also checks that the module param 'gather_subset' is used if no gather_subset param is specified
    module = FakeModule(['some_collector'])
    subset = ansible_facts(module)['ansible_collector_subset']

# Generated at 2022-06-13 00:25:07.148009
# Unit test for function ansible_facts
def test_ansible_facts():

    from ansible.module_utils import basic
    import ansible.module_utils.facts.system.distribution

    class FakeModule(object):
        '''provide an object with a params attrib, as needed by v2.2-2.3 ansible_facts()

        This is only used by unit test code.
        '''

        def __init__(self, params):
            self.params = params

        def fail_json(self, **kwargs):
            '''module.fail_json() is used by ansible_collector, so provide a barebones stub

            It is only used in exceptional cases, and only used during unit test.
            It is not used in normal operation.
            '''

            return None

    # Test with default parameters

# Generated at 2022-06-13 00:25:18.602294
# Unit test for function get_all_facts
def test_get_all_facts():
    '''Unit test case for function get_all_facts'''

    from ansible.modules.system import setup

    module = setup.AnsibleModule(argument_spec={'gather_subset': dict(type='list', elements='str', required=False, default=['all'])})
    assert isinstance(module, setup.AnsibleModule)

    # test get_all_facts function
    # default gather_subset is 'all', no filter
    facts = get_all_facts(module)
    assert isinstance(facts, dict)
    assert 'all' in facts
    assert 'default_ipv4' in facts['all']
    # test setting gather_subset to ['min']
    facts = get_all_facts(module)
    assert isinstance(facts, dict)
    assert 'min' in facts

# Generated at 2022-06-13 00:25:26.892687
# Unit test for function get_all_facts
def test_get_all_facts():
    import time
    import unittest

    class MockModule(object):
        params = {}

    # This test only works if a hostname and dns fact is available
    if 'hostname' not in ansible_facts(MockModule()) or 'fqdn' not in ansible_facts(MockModule()):
        class NoTestsForThisPlatform(unittest.TestCase):
            def test_this_platform(self):
                self.assertEqual(True, True)

    else:
        class TestGetAllFacts(unittest.TestCase):
            def setUp(self):
                self.module = MockModule()
                self.start_time = time.time()
                self.facts = get_all_facts(self.module)

            def test_elapsed_time(self):
                elapsed_time = time

# Generated at 2022-06-13 00:25:38.216869
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils.facts import ansible_collector

    # Mock ansible_collector.get_ansible_collector so that it returns a
    # mock of type `FactCollector`
    def mock_get_ansible_collector(all_collector_classes=None, namespace=None,
                                   filter_spec=None, gather_subset=None, gather_timeout=None,
                                   minimal_gather_subset=None):
        '''
        Mock of ansible_collector.get_ansible_collector()
        '''
        class MockFactCollector(object):
            '''
            Mock of FactCollector class
            '''

# Generated at 2022-06-13 00:25:48.156684
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts.platform.networking import NetworkingGenericFactCollector
    from ansible.module_utils.facts.system.distribution import DistributionFactCollector
    from ansible.module_utils.facts.system.platform import PlatformFactCollector
    from ansible.module_utils.facts.system.pkg_mgr import PkgMgrFactCollector
    from ansible.module_utils.facts.system.service_mgr import ServiceMgrFactCollector
    from ansible.module_utils.facts.system.selinux import SELinuxFactCollector
    from ansible.module_utils.facts.system.user import UserFactCollector
    from ansible.module_utils.facts.system.distribution import DistributionFactCollector

    from ansible.module_utils.facts.system.kernel import KernelFactCollect

# Generated at 2022-06-13 00:25:59.152438
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts import ansible_collector
    from ansible.module_utils.facts.test_test_test import StubModule, get_mock_ansible_module

    # test that ansible_facts uses the test_ansible_module api
    def _test_ansible_facts(mock_module, **kwargs):
        return kwargs

    # ensure this is called via the _test_ansible_facts mock_module
    ansible_collector.get_ansible_collector = _test_ansible_facts

    # patch for the test
    default_collectors.collectors = [StubModule]

    # test that it uses the test_ansible_module api and that it passes through
    # the expected args
    m = get_mock_ansible_module()
    gather_sub

# Generated at 2022-06-13 00:26:09.195186
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils.facts import ansible_collector

    from ansible.module_utils.facts import get_all_facts

    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.collector import BaseFileCacheCollector
    from ansible.module_utils.facts.collector import NetworkInterfaceCollector
    from ansible.module_utils.facts.collector import BaseLegacyCollector
    from ansible.module_utils.facts.collector import FactsCacheCollector


# Generated at 2022-06-13 00:26:16.724656
# Unit test for function ansible_facts
def test_ansible_facts():
    module = AnsibleModule(argument_spec={'gather_subset': dict(default=['all'], type='list')})
    module.params['gather_subset'] = ['all']

    ansible_fact_dict = ansible_facts(module)
    assert ansible_fact_dict.get('hostname') == 'localhost'
    assert ansible_fact_dict.get('domain') == 'ansible'
    assert ansible_fact_dict.get('fqdn') == 'localhost.ansible'



# Generated at 2022-06-13 00:26:24.923220
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.basic import AnsibleModule, env_fallback
    from ansible.module_utils.facts import ansible_facts, default_collectors
    try:
        from collections import OrderedDict
    except ImportError:
        # ordered dict only available in 2.7
        # emulate it with regular dict for 2.6
        from ansible.module_utils.six import iteritems
        from ansible.module_utils.six.moves import UserDict

        class OrderedDict(dict, UserDict.DictMixin):
            def __init__(self, *args, **kwargs):
                if len(args) > 1:
                    raise TypeError('expected at most 1 arguments, got %d' % len(args))

# Generated at 2022-06-13 00:26:26.986159
# Unit test for function get_all_facts
def test_get_all_facts():

    class MockModule:
        def __init__(self, gather_subset):
            self.params = {'gather_subset': gather_subset}

    module = MockModule(['all', 'network', 'virtual'])
    ansible_facts(module)

# Generated at 2022-06-13 00:26:38.087003
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts import ansible_collector
    from ansible.module_utils.facts.namespace import PrefixFactNamespace

    from ansible.module_utils import basic
    from io import StringIO
    import sys

    # create a module instance
    module = basic.AnsibleModule(argument_spec={},
                                 bypass_checks=True,
                                 no_log=True)

    # create a string buffer for stderr
    module_stderr = StringIO()

    # redirect the stderr output to the string buffer
    sys.stderr = module_stderr

    # create a namespace and a filter_spec
    namespace = PrefixFactNamespace(namespace_name='ansible', prefix='')
    filter_spec = '*'

    # invoke the ansible_facts method

# Generated at 2022-06-13 00:26:48.757827
# Unit test for function ansible_facts
def test_ansible_facts():
    import sys
    # Mock 'ansible.module_utils.basic' so we can test the ansible_facts module util function.
    #
    # Must call 'ansible.module_utils.basic.ANSIBLE_VERSION' (which really is just sys.version_info)
    # before trying to mock 'sys.version_info' because otherwise, mocking sys.version_info will
    # wrongly change the value of 'ansible.module_utils.basic.ANSIBLE_VERSION'.

    import ansible.module_utils.basic
    old_sys_version_info = sys.version_info

    with mock.patch.object(sys, 'version_info') as mock_sys_version_info:
        mock_sys_version_info.__getitem__.return_value = 2
        ansible.module_utils.basic.ANSIBLE_VERSION
       

# Generated at 2022-06-13 00:26:52.732721
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils._text import to_bytes
    collect_subset = ['all']
    filtered_facts = {
        'distribution': 'Fedora',
        'distribution_major_version': '25',
        'distribution_version': '25',
        'ipv4_address': '10.0.0.5',
        'ipv6_address': 'fe80::250:56ff:fe8e:2b1a'}
    class MockModule:
        def __init__(self, collect_subset):
            self.params = {'gather_subset': collect_subset}

    module = MockModule(collect_subset)
    for fact in filtered_facts:
        assert filtered_facts[fact] == ansible_facts(module)[to_bytes(fact)]

# Generated at 2022-06-13 00:27:02.471943
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts import ansible_facts as unloaded_ansible_facts
    from ansible.module_utils.facts import collect_subset
    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils.facts.namespace import PrefixFactNamespace

    class MockModule(object):
        def __init__(self, params):
            self.params = params

        def fail_json(self, msg):
            raise AssertionError(msg)

    mock_module = MockModule(params={
        'gather_subset': [],
        'gather_timeout': 10,
    })
    mock_module.exit_json = lambda **kwargs: None

    # test gather subset of empty list
    results = ansible_facts(mock_module)
    assert results

# Generated at 2022-06-13 00:27:08.214694
# Unit test for function ansible_facts
def test_ansible_facts():
    module = MockAnsibleModule()
    facts_dict = ansible_facts(module)
    assert facts_dict == dict(state='present')


# Generated at 2022-06-13 00:27:15.585324
# Unit test for function ansible_facts
def test_ansible_facts():
    import ansible.module_utils.facts
    import ansible.module_utils.facts.default_collectors
    import ansible.module_utils.facts.ansible_collector
    import ansible.module_utils.facts.system.distribution

    import ansible.module_utils.common.dict_transformations
    import ansible.module_utils.common.collections
    import ansible.module_utils.common.json_utils

    import ansible.module_utils.six

    from ansible.module_utils.six.moves import cStringIO as StringIO

    import mock


# Generated at 2022-06-13 00:27:26.139062
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.facts import is_executable
    from ansible.module_utils.facts.system.distribution import DistributionFactCollector

    class TestModule(AnsibleModule):
        def __init__(self, *args, **kwargs):
            self.params = kwargs
        def get_bin_path(self, executable, required=False, opt_dirs=[]):
            # not implemented in integration testing
            return None
        def get_platform(self):
            # not implemented in integration testing
            return None
        def get_distribution(self):
            # not implemented in integration testing
            return None
        def get_distribution_version(self):
            # not implemented in integration testing
            return None


# Generated at 2022-06-13 00:27:31.214679
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts import ansible_facts

    bare_facts_dict = ansible_facts()
    assert len(bare_facts_dict) > 40

    # make sure that the default_ipv4 fact is present
    assert 'default_ipv4' in bare_facts_dict
    # make sure that the ansible_default_ipv4 fact is not present
    assert 'ansible_default_ipv4' not in bare_facts_dict



# Generated at 2022-06-13 00:27:43.197443
# Unit test for function ansible_facts
def test_ansible_facts():
    import sys

    import ansible.module_utils.facts.system.distribution
    from ansible.module_utils.facts.system.distribution import DistributionFactCollector
    from ansible.module_utils.facts.system.distribution import Distribution
    from ansible.module_utils.facts import __file__ as facts_utils_file

    # Make sure DistributionFactCollector is loaded for the test.
    # This happens automatically in ansible_facts(), but we can't use that here.
    ansible.module_utils.facts.system.distribution.collector = DistributionFactCollector()

    # Create a mock module.
    class MockModule(object):
        def __init__(self, name):
            self.name = name


# Generated at 2022-06-13 00:27:53.971574
# Unit test for function ansible_facts
def test_ansible_facts():
    module.fail_json = True
    result = ansible_facts(module)

# Generated at 2022-06-13 00:28:00.582385
# Unit test for function ansible_facts

# Generated at 2022-06-13 00:28:10.031031
# Unit test for function ansible_facts
def test_ansible_facts():

    # Stubbing out ansible module

    from ansible.module_utils.facts import ansible_collector

    class TestModule:

        class AnsibleModule:

            def __init__(self):
                print('init test module')
                self.params = {}

            def get_bin_path(self, executable, required=False):
                print('ansible module get_bin_path')
                return '/bin/date'

        def __init__(self):
            self.params = {}
            self.ansible_facts = {}
            self.ansible_facts['default_ipv4'] = {}
            self.ansible_facts['default_ipv4']['address'] = '192.168.1.10'

        def exit_json(self, module_results):
            print('exit_json')
            self.ansible

# Generated at 2022-06-13 00:28:21.287163
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils._text import to_native  # noqa: F401 # pylint: disable=import-error
    from ansible.module_utils.facts.collector import FactCollector  # noqa: F401 # pylint: disable=import-error

    from ansible.module_utils.facts import processor # noqa: F401 # pylint: disable=import-error
    from ansible.module_utils.facts import default_collectors # noqa: F401 # pylint: disable=import-error
    from ansible.module_utils.facts.namespace import FactNamespace # noqa: F401 # pylint: disable=import-error
    from ansible.module_utils.facts.cache import BaseFactCache # noqa: F401 # pylint: disable=import-error

# Generated at 2022-06-13 00:28:28.486144
# Unit test for function ansible_facts
def test_ansible_facts():
    import ansible.module_utils.facts.network.real as real_network_facts
    import ansible.module_utils.facts.processor.real as real_processor_facts
    from ansible.module_utils.facts import default_collectors
    real_network_facts.NetworkInfo = lambda: 0
    real_processor_facts.CpuInfo = lambda: 0
    default_collectors.register(real_network_facts, real_processor_facts)
    all_collector_classes = default_collectors.collectors
    namespace = PrefixFactNamespace(namespace_name='ansible', prefix='')
    fact_collector = ansible_collector.get_ansible_collector(all_collector_classes=all_collector_classes,
                                                             namespace=namespace)

# Generated at 2022-06-13 00:28:43.233652
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils.facts import ansible_collector
    import ansible.module_utils.facts.system.distribution
    import ansible.module_utils.facts.system.platform
    import ansible.module_utils.facts.system.selinux
    import ansible.module_utils.facts.system.service_mgr
    import ansible.module_utils.facts.system.pkg_mgr
    import ansible.module_utils.facts.network.ipv4
    import ansible.module_utils.facts.network.ipv6
    import ansible.module_utils.facts.network.interfaces
    import ansible.module_utils.facts.network

# Generated at 2022-06-13 00:28:54.248831
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils.facts import ansible_collector
    from ansible.module_utils import basic

    results = []
    def run_command_mock(cmd, check_rc=True, close_fds=True, executable=None, data=None):
        results.append(cmd)
        return (None, 'fake data', None)

    class FakeModule(object):
        def __init__(self, params):
            self.params = params
            self.run_command = run_command_mock

    class TestCollector(object):
        def __init__(self, name):
            self.name = name


# Generated at 2022-06-13 00:29:04.289615
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts import get_all_facts
    import ansible.module_utils.facts.ansible_collector

    class FakeAnsibleModule(object):
        def __init__(self, module_id='setup'):
            self.params = {'filter': '*',
                           'gather_subset': 'all',
                           'gather_timeout': 10}
            self.id = module_id

    my_module = FakeAnsibleModule()

    # Get facts from all the collectors

    facts_dict = get_all_facts(my_module)

    # Get facts from only the ansible_distribution collector
    # This is a collector that I'm familiar with and that has been around for
    # awhile.
    # It should have the 'distribution' and the 'distribution_release'

# Generated at 2022-06-13 00:29:04.836137
# Unit test for function get_all_facts
def test_get_all_facts():
    pass

# Generated at 2022-06-13 00:29:08.674606
# Unit test for function get_all_facts
def test_get_all_facts():
    with patch('ansible.module_utils.facts.ansible_facts') as mocked_ansible_facts:
        module = Mock(params={'gather_subset': ['all']})
        get_all_facts(module)
        mocked_ansible_facts.assert_called_once_with(module, ['all'])

# Generated at 2022-06-13 00:29:12.400533
# Unit test for function ansible_facts
def test_ansible_facts():
    def mock_module(params):
        ret = dict(params=params)
        return ret

    # test that we get a dict back
    module = mock_module(dict(gather_subset=['all'], gather_timeout=10))
    module_facts = ansible_facts(module, gather_subset=['all'])
    assert isinstance(module_facts, dict)
    assert module_facts


# compat api.  Wrap up the legacy ansible_facts method in a class.

# Generated at 2022-06-13 00:29:20.102383
# Unit test for function ansible_facts
def test_ansible_facts():
    class MockModule(object):
        def __init__(self):
            self.params = dict(
                gather_subset=[],
                gather_timeout=10,
                filter='*',
            )

    def mock_collect(self, module):
        return dict(a='fake_value')

    m = MockModule()
    # this is the fragile part of the test.  It depends on the order of the dict keys in facts_dict
    # returned from ansible_facts
    assert ansible_facts(m) == dict(a='fake_value')


# Generated at 2022-06-13 00:29:28.715387
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts import ansible_collector
    # pylint: disable=unused-import,import-self
    import json
    import os
    import sys
    import yaml
    # pylint: enable=unused-import,import-self

    # mock ansible module
    # pylint: disable=too-many-locals

# Generated at 2022-06-13 00:29:40.325342
# Unit test for function ansible_facts
def test_ansible_facts():
    ''' unit test to verify ansible_facts api backwards compatibility'''

    # trivial AnsibleModule with no arguments
    module = {
        'params': {
            # use minimal gather set (gather_minimal)
            'gather_subset': ['minimal'],
            # return all facts, no filtering
            'filter': '*'
        },
        'boolean': lambda v: bool(v)
    }

    # call ansible_facts with minimal gather set and no filtering
    facts = ansible_facts(module)

    # expect several facts
    assert len(facts) > 10

    # expect to find the platform fact
    assert facts['platform'] is not None

    # expect to find the dns fact
    assert 'dns' in facts

    # expect to find the distribution fact
    assert 'distribution' in facts


# Generated at 2022-06-13 00:29:41.951681
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils.facts.facts import ansible_facts

    ansible_facts()

# Generated at 2022-06-13 00:30:08.655567
# Unit test for function get_all_facts
def test_get_all_facts():
    '''Test get_all_facts() compat method
    '''

    # Create mock module
    module = MockAnsibleModule()

    # Module parameters
    module.params = {'gather_subset': ['foo']}

    # ansible_facts call
    ansible_facts_return = get_all_facts(module)

    # Ansible facts call
    ansible_facts_call = MockAnsibleModule.ansible_facts_call

    # Assert function is expected
    assert ansible_facts_call == ansible_facts

    # Assert arguments
    assert ansible_facts_return == ansible_facts_call(module, gather_subset=['foo'])



# Generated at 2022-06-13 00:30:20.102483
# Unit test for function ansible_facts
def test_ansible_facts():
    """
    This function checks the fact ansible_facts
    :return: N/A
    """

    from ansible.module_utils.facts.utils import AnsibleFactCollector
    from ansible.module_utils.facts.collector.distribution import DistributionFactCollector
    from ansible.module_utils.facts import default_collectors

    class AnsibleModuleMock:

        def __init__(self, gather_subset=None, gather_timeout=10, filter='*'):
            self.params = {'gather_subset': gather_subset, 'gather_timeout': gather_timeout, 'filter': filter}


# Generated at 2022-06-13 00:30:31.551406
# Unit test for function ansible_facts
def test_ansible_facts():
    import sys
    import os
    import json
    import pytest
    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils.facts import ansible_collector
    from ansible.module_utils._text import to_bytes, to_native
    from ansible.module_utils.facts.namespace import PrefixFactNamespace

    # Setting up dependencies
    all_collector_classes = default_collectors.collectors

    class TestModule(object):
        def __init__(self, params):
            self.params = params

    # Unit test for function ansible_facts with gather_subset == None
    module = TestModule({'gather_timeout': '10', 'fact_path': '/root/tempdir'})

# Generated at 2022-06-13 00:30:42.186444
# Unit test for function ansible_facts
def test_ansible_facts():
    import os
    import warnings
    import shutil
    import tempfile
    import yaml
    from ansible.module_utils import basic
    from ansible.module_utils import six
    import ansible.module_utils.facts.network.base as network_base
    # NOTE: be sure not to create a 'ansible.module_utils.facts.network' namespace package to
    # avoid interfering with the built-in network fact module while running the unit test.
    import ansible.module_utils.facts.network.dummy as network_dummy

    original_network_fact_module_name = network_dummy.network_fact_module_name


# Generated at 2022-06-13 00:30:53.415864
# Unit test for function ansible_facts
def test_ansible_facts():
    '''Unit test for function ansible_facts'''
    from ansible.module_utils.facts import ansible_facts
    from ansible.module_utils.basic import AnsibleModule
    from ansible_collections.notstdlib.moveitallout.plugins.module_utils.facts import collector

    module = AnsibleModule(argument_spec={}, supports_check_mode=True)
    all_facts = ansible_facts(module)
    assert 'ansible_facts' in all_facts
    assert 'ansible_service_mgr' in all_facts
    assert 'ansible_fips' in all_facts
    assert 'ansible_user' in all_facts
    assert 'ansible_distribution' in all_facts
    assert 'ansible_architecture' in all_facts

# Generated at 2022-06-13 00:31:05.457671
# Unit test for function ansible_facts
def test_ansible_facts():
    '''
    Create a mock AnsibleModule with gather_subset set to a non-default value,
    call ansible_facts and make sure the returned dict is correct.
    '''
    from ansible.module_utils.facts.collector import FactsCache
    from ansible.module_utils.facts import get_all_collectors
    from ansible.module_utils.facts.namespace import DefaultFactNamespace
    from ansible.module_utils.facts.utils import get_prefix_from_argspec
    from ansible.module_utils._text import to_bytes, to_native

    # We want to make sure _ prefixes are preserved

    # To do this, we'll replace single underscore facts with facts that have
    # a double underscore
    old_facts = {'_ansible_test_fact': 'original_value'}
   

# Generated at 2022-06-13 00:31:06.477984
# Unit test for function ansible_facts
def test_ansible_facts():
    raise NotImplementedError

# Generated at 2022-06-13 00:31:14.724938
# Unit test for function get_all_facts

# Generated at 2022-06-13 00:31:16.807741
# Unit test for function ansible_facts
def test_ansible_facts():
    '''
    Tests:
        ansible_facts

    Unit test for the ansible_facts function.
    '''
    pass

# Generated at 2022-06-13 00:31:26.834067
# Unit test for function ansible_facts
def test_ansible_facts():
    import unittest
    from ansible.module_utils.facts.util import which

    class FakeModule(object):
        class FakeAnsibleModule(object):
            class FakeAnsibleModuleArgSpec(object):
                def __init__(self):
                    self.args = ['filter', 'gather_subset', 'gather_timeout']

            def __init__(self):
                self.params = {'filter': 'ansible_*', 'gather_subset': ['all'], 'gather_timeout': 10}
                self.get_bin_path = staticmethod(which)
                self.exit_json = object()
                self.fail_json = object()
                self.fail_json.side_effect = SystemExit()
                self.argspec = FakeAnsibleModuleArgSpec()


# Generated at 2022-06-13 00:32:08.257069
# Unit test for function ansible_facts
def test_ansible_facts():
    import json

    class AnsibleModule:
        def __init__(self, gather_subset):
            self.params = {
                'gather_subset': gather_subset,
            }

    # gather_subset=None, should use default gather_subset
    module = AnsibleModule(gather_subset=None)
    result = ansible_facts(module)
    assert(result is not None)

    # gather_subset=True, should use default gather_subset
    module = AnsibleModule(gather_subset=True)
    result = ansible_facts(module)
    assert(result is not None)

    # gather_subset=False, should use default gather_subset
    module = AnsibleModule(gather_subset=False)
    result = ansible_facts(module)


# Generated at 2022-06-13 00:32:15.699587
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils.facts import ansible_facts
    from mock import MagicMock

    module = MagicMock()
    module.params = dict(gather_subset=['all'])
    module.params = dict(filter='*')
    module.params = dict(gather_timeout=10)

    result = get_all_facts(module)

    assert isinstance(result, dict), "Expect result to be a dict"
    assert len(result) > 0, "Expect result to be populated"

# Generated at 2022-06-13 00:32:25.440601
# Unit test for function ansible_facts
def test_ansible_facts():
    import unittest
    import ansible.module_utils.facts.namespace
    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils.facts import ansible_collector
    from ansible.module_utils.facts import ansible_facts
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_text
    import tempfile
    import sys

    # Mocks
    import mock

    class AnsibleModule:
        def __init__(self, params):
            self.params = params

    class MockAnsibleModule(basic.AnsibleModule):
        def __init__(self, params):
            self.params = params

    class MockAnsibleModulePath:
        path = 'ansible.module_utils.basic'


# Generated at 2022-06-13 00:32:35.505683
# Unit test for function ansible_facts
def test_ansible_facts():
    import ansible
    from ansible.module_utils.facts.resource_module import get_module

    init_module = get_module()

    # initialize the module
    init_module.params = dict()
    init_module.params['gather_subset'] = ['all']
    init_module.params['gather_timeout'] = 3

    facts_dict = ansible_facts(init_module)

    # gather_subset=['all'] will collect all facts, so we check we got both a python and a platform fact
    assert 'python' in facts_dict, "Failed to gather basic facts"
    assert 'platform' in facts_dict, "Failed to gather basic facts"

    # this part of the test will have to change to test different versions if we ever change the
    # version of Ansible we run tests with, but for now

# Generated at 2022-06-13 00:32:42.307020
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts import get_all_facts
    from ansible.module_utils.facts import ansible_facts

    class FakeModule(object):
        def __init__(self):
            self.params = {}

    # test with only gather_subset, no filter.
    fake_module = FakeModule()
    fake_module.params['gather_subset'] = ['all']
    all_facts = get_all_facts(module=fake_module)
    assert 'default_ipv4' in all_facts

# Generated at 2022-06-13 00:32:51.130604
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts.virtual.openbsd_pkg import OpenBSD_PkgFactCollector
    from ansible.module_utils.common._collections_compat import Mapping

    # Test for Ansible 2.2/2.3 compat

    # Test that config does nothing when gather_subset is specified
    selected_collectors = set(['platform', 'virtual'])
    override_subset = ['platform', 'virtual']
    minimal = True

# Generated at 2022-06-13 00:33:00.203985
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils.facts import ansible_version
    from ansible.module_utils.facts.test.test_default_collectors import MockAnsibleModule

    mock_module = MockAnsibleModule()
    facts = get_all_facts(mock_module)

    assert facts['distribution'] == 'MockDistro'

    if ansible_version.__version__.startswith('2.1'):
        # 2.1 does not support the gather_subset param
        assert len(facts) == 17
    else:
        # 2.2+
        assert len(facts) == 15



# Generated at 2022-06-13 00:33:08.530071
# Unit test for function ansible_facts
def test_ansible_facts():
    import ansible.module_utils.facts.network as net_facts
    fact_dict = {}
    for fact_cls in net_facts.collectors:
        fact_dict[fact_cls.name] = fact_cls.get_device_info.__doc__
    # print fact_dict
    # test_fact_dict = ansible_facts(module, ['network'])
    # print test_fact_dict['ansible_network_resources']
    # print test_fact_dict

if __name__ == '__main__':
    test_ansible_facts()

# Generated at 2022-06-13 00:33:15.929558
# Unit test for function ansible_facts
def test_ansible_facts():
    # initialize module with args and return was expected
    # this module is only used in place of AnsibleModule in order to make
    # ansible_facts being tested as standalone function
    class AnsibleModule:
        def __init__(self, args, return_value):
            self.params = args
            self.exit_json = return_value

    # test if 'ansible' namespace was added
    module = AnsibleModule(args={'gather_subset':['all'], 'gather_timeout': 10, 'filter': '*'},
                           return_value=None)
    facts = ansible_facts(module)
    assert facts['distribution'] == 'Gathering_subset_all'
    assert facts['distribution_version'] == 'Gathering_subset_all'

# Generated at 2022-06-13 00:33:27.232487
# Unit test for function get_all_facts
def test_get_all_facts():
    #
    # NOTE:
    #   The fact_collector.collect method is tested separately. See 'test_all_ansible_facts'
    #   and 'test_minimal_sube_facts' in tests/module_utils/facts/ansible_collector_test.py
    #
    import pytest

    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.facts import __find_yaml_version

    from ansible.module_utils.facts import default_collectors

    from ansible.module_utils.facts import ansible_collector
    from ansible.module_utils.facts import ansible_vars
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts.system import DistributionFact

    G