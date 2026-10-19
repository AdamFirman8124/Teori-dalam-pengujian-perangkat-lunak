

# Generated at 2022-06-13 00:24:14.914585
# Unit test for function ansible_facts
def test_ansible_facts():
    try:
        from ansible.module_utils import basic
    except:
        # ansible 2.2 and earlier
        from ansible.module_utils.basic import AnsibleModule
        basic = AnsibleModule
    module = basic.AnsibleModule(argument_spec={
        'gather_subset': {'type': 'list', 'default': ['all'], 'aliases': ['subset']}
    })

    facts = ansible_facts(module, gather_subset=['all'])
    if 'ansible_distribution' not in facts:
        raise Exception("Failed to get ansible facts")

# Generated at 2022-06-13 00:24:19.353221
# Unit test for function ansible_facts
def test_ansible_facts():

    # mock module
    class FakeModule():
        params = {}

    fake_module = FakeModule()

    # default params
    gathered_facts = ansible_facts(fake_module)
    assert len(gathered_facts) > 0

    # override params
    fake_module.params = {
        'filter': 'f*',
        'gather_subset': ['!all'],
        'gather_timeout': 0,
    }
    gathered_facts = ansible_facts(fake_module)
    assert len(gathered_facts) > 0

# Generated at 2022-06-13 00:24:19.912347
# Unit test for function ansible_facts
def test_ansible_facts():
    pass

# Generated at 2022-06-13 00:24:22.822995
# Unit test for function ansible_facts
def test_ansible_facts():
    ''' Run unit test for function ansible_facts '''

    ansible_facts({'name': 'test'}, gather_subset=['all'])

# Generated at 2022-06-13 00:24:23.415474
# Unit test for function get_all_facts
def test_get_all_facts():
    pass

# Generated at 2022-06-13 00:24:32.620902
# Unit test for function ansible_facts
def test_ansible_facts():
    import ansible.module_utils.facts.f5 as module_utils_facts_f5

    # import module snippets
    from ansible.module_utils.basic import AnsibleModule

    # set up the module object
    module = AnsibleModule(argument_spec=dict(gather_subset=dict(type='list', default=['all'])),
                           supports_check_mode=True)

    # set values for module params
    module.params = dict(gather_subset=['all'])
    module.params['gather_timeout'] = 5
    module.params['filter'] = '*'

    # run the code to test
    ansible_facts_data = ansible_facts(module)

    # make sure we got data back
    assert ansible_facts_data is not None

    # check some sample data


# Generated at 2022-06-13 00:24:42.516351
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    import ansible.module_utils.facts.namespace
    import ansible.module_utils.facts.default_collectors

    # Create 'mini' mocks for base classes that we need for a functional unit test
    class CollectorMock(BaseFactCollector):
        def __init__(self, **kwargs):
            super(CollectorMock, self).__init__(**kwargs)

        def collect(self, module=None, collected_facts=None):
            return collected_facts


# Generated at 2022-06-13 00:24:50.674195
# Unit test for function ansible_facts
def test_ansible_facts():
    class MockModule:
        def __init__(self):
            self.params = dict()

    mock_module = MockModule()

    result = ansible_facts(mock_module)

    assert 'ansible_all_ipv4_addresses' in result
    assert 'all_ipv4_addresses' not in result
    assert 'ansible_default_ipv4' in result
    assert 'default_ipv4' not in result

# Generated at 2022-06-13 00:24:55.371465
# Unit test for function ansible_facts
def test_ansible_facts():
    #
    # mock_module = Mock(spec=AnsibleModule)
    # mock_module.params = {
    #     'gather_subset': None,
    #     'filter': '*',
    #
    #     'config_file': '/etc/ansible/ansible.cfg'
    # }
    #
    # mock_module.get_bin_path = Mock(spec=AnsibleModule.get_bin_path)
    # mock_module.get_bin_path.return_value = '/usr/bin/python'
    #
    # # facts_dict = ansible_facts(module=mock_module)
    # #
    # # assert_equal(facts_dict['python']['has_sslcontext'], False)
    # #
    return

# Generated at 2022-06-13 00:24:58.761675
# Unit test for function get_all_facts
def test_get_all_facts():
    m = mock_module()
    result = get_all_facts(m)
    assert result['test'] == 'test_fact'



# Generated at 2022-06-13 00:25:05.837502
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.basic import AnsibleModule

    dummy_ansible_module = AnsibleModule(argument_spec={})

    actual_facts = ansible_facts(dummy_ansible_module)
    assert type(actual_facts) == dict
    assert 'distribution' in actual_facts.keys()



# Generated at 2022-06-13 00:25:06.879779
# Unit test for function get_all_facts
def test_get_all_facts():
    pass

# Generated at 2022-06-13 00:25:18.241608
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts import facts
    from ansible.module_utils.facts import ansible_collector
    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils._text import to_text
    from ansible.module_utils.facts.namespace import PrefixFactNamespace

    class MyFakeModule(object):
        params = dict(gather_subset='all',
                      gather_timeout=10,
                      filter='ansible_all')

        def get_platform(self):
            return 'FakePlatform'

        def get_distribution(self):
            return 'FakeDistribution'

    facts_dict = ansible_facts(MyFakeModule())

    assert isinstance(facts_dict, dict)
    assert isinstance(facts, dict)
    assert facts_dict == facts

# Generated at 2022-06-13 00:25:28.873970
# Unit test for function get_all_facts
def test_get_all_facts():
    import test.support
    import test.support.ansible_mock
    import ansible.module_utils
    import ansible.module_utils.basic
    import copy
    import os
    import sys

    if sys.version_info[0] == 2:
        import mock
        import __builtin__ as builtins
    else:
        import unittest.mock as mock
        import builtins

    def _append_to_script_args(arg):
        '''mock module_args_parser.add_argument to collect our args into a list, as AnsibleModule
        does for args passed to the module script'''
        # print('_append_to_script_args called with arg: %s' % arg)
        global _script_args
        _script_args.append(arg)


# Generated at 2022-06-13 00:25:40.393303
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible_collections.ansible.zabbix.tests.unit.compat.mock import Mock
    from ansible_collections.ansible.zabbix.tests.unit.compat.mock import patch, MagicMock
    from ansible_collections.ansible.zabbix.tests.unit.modules.utils import set_module_args, set_default_args

    module_mock = MagicMock(name="AnsibleModule")
    module_mock.params = {'gather_subset': ['!all', 'foo']}
    set_default_args(module_mock)
    module = module_mock.return_value


# Generated at 2022-06-13 00:25:46.300110
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts import ansible_facts
    from ansible.module_utils.facts import Facts
    from ansible.module_utils.six import PY2

    facts = Facts()
    if PY2:
        facts_dict = ansible_facts(facts)
    else:
        facts_dict = ansible_facts(facts, gather_subset='!all')
    print(facts_dict)
    assert 'python' in facts_dict
    assert facts_dict['python'] == dict(version='2.7.5')


# Generated at 2022-06-13 00:25:58.409456
# Unit test for function get_all_facts
def test_get_all_facts():
    import ansible.module_utils.facts.namespace
    import ansible.module_utils.facts.default_collectors
    import ansible.module_utils.facts.ansible_collector
    import ansible.module_utils.facts
    import ansible.module_utils.facts.utils
    import ansible.module_utils.facts.collector

    import ansible.module_utils.facts.namespace_loader
    import ansible.module_utils.facts.loader
    import ansible.module_utils.facts.fact_cache
    import ansible.module_utils.facts.cache
    import ansible.module_utils.facts.namespace_symlinked_cache

    from ansible.module_utils.facts.namespace import PrefixFactNamespace

# Generated at 2022-06-13 00:26:08.670939
# Unit test for function get_all_facts
def test_get_all_facts():
    import ansible.module_utils.facts.namespace
    import ansible.module_utils.facts.collector
    import ansible.module_utils.facts.ansible_collector
    import ansible.module_utils.facts.default_collectors

    from ansible.module_utils.facts import get_all_facts
    from ansible.module_utils.facts import ansible_facts
    from ansible.module_utils.facts import get_collector_classes
    from ansible.module_utils.facts import get_minimal_gather_subset
    from ansible.module_utils.facts import get_timer_args
    from ansible.module_utils.facts import get_gather_subset
    from ansible.module_utils.facts import get_gather_timeout

# Generated at 2022-06-13 00:26:17.244719
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(argument_spec={'gather_subset': {'type': 'list', 'default': ['!all', '!min']}})

    result = get_all_facts(module)
    assert result['distribution'] == 'RedHat'
    assert result['distribution_version'] == '7'
    # assert distribution_release is in the facts
    assert 'distribution_release' in result
    # assert distribution_file_parsed is in the facts
    assert 'distribution_file_parsed' in result

# Generated at 2022-06-13 00:26:26.124746
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils.facts.system.distribution import DistributionFactCollector
    from ansible.module_utils.facts.system.pkg_mgr import PkgMgrFactCollector

    # mock up module object to pass in
    class FakeModule:
        def __init__(self):
            self.params = {'filter': '*'}
    fake_module = FakeModule()

    # mock up a collector to test with
    # It should be instantiated with a namespace and a set of optional args.
    # It should also have a 'collect' method that takes a module arg and returns a list of facts
    # (or a dict in 2.3)

# Generated at 2022-06-13 00:26:35.179692
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.compat.tests.mock import MagicMock

    module = MagicMock()
    module.params = dict(
        gather_subset=[],
    )

    assert get_all_facts(module) == ansible_facts(module)

# Generated at 2022-06-13 00:26:45.104525
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils.facts.utils import get_file_content
    from ansible.module_utils.facts import ansible_collector

    import json
    import mock

    class FakeAnsibleModule:

        def __init__(self, params):
            self.params = params

    myparams = dict(gather_subset=None, gather_timeout=10)
    myparams['filter'] = '*'
    module = FakeAnsibleModule(myparams)

    # A copy of get_all_facts from ansible/module_utils/facts/__init__.py
    gather_subset = module.params['gather_subset']

# Generated at 2022-06-13 00:26:54.388481
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts import ansible_collector
    from ansible.module_utils.facts.system import distro
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    import json

    class MockOptions(object):
        def __init__(self, collect_subset):
            self.collect_subset = collect_subset

    class MockModule(object):
        def __init__(self):
            self.params = {'filter': 'ansible_hostname'}

        def get_bin_path(self, *args, **kwargs):
            return ''

    all_collector_classes = default_collectors.collectors

    # don

# Generated at 2022-06-13 00:27:06.052048
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts import ansible_collector
    from ansible.module_utils.facts.ansible_collectors import local_collector

    # create a mock module
    def run_command(*args, **kwargs):
        # Assume args[1]=0 means the command execution was successful.
        # Return the exit value immediately.
        # Ignore kwargs.
        return args[1]

    def get_bin_path(*args, **kwargs):
        return '/bin/true'

    class AnsibleModule:
        def __init__(self):
            self.params = {}

        def get_bin_path(self, *args, **kwargs):
            return get_bin_path(*args, **kwargs)



# Generated at 2022-06-13 00:27:14.256558
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils.facts import get_all_facts
    from ansible.module_utils.facts import ansible_facts
    from ansible.module_utils.basic import AnsibleModule
    import mock

    # a fake set of params to satisfy AnsibleModule __init__
    module_args = {}

    # instantiate our fake AnsibleModule
    am = AnsibleModule(argument_spec=module_args)

    # monkey patch method get_all_facts on our fake AnsibleModule.
    # this will call ansible_facts() with gather_subset param of
    # ['all']
    with mock.patch('ansible.module_utils.facts.get_all_facts', new=get_all_facts):
        facts = am.get_all_facts()

    # verify expected return from get_all_facts

# Generated at 2022-06-13 00:27:25.568107
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts import ansible_facts
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.parsing.convert_bool import boolean
    from ansible.module_utils.six.moves import shlex_quote
    from ansible.module_utils.urls import urlparse

    try:
        from __main__ import display
    except ImportError:
        from ansible.utils.display import Display
        display = Display()

    from ansible.module_utils.basic import AnsibleModule, missing_required_lib

    def get_command(module):
        command = [module.get_bin_path('ansible-facts', True)]
        # add basic options

# Generated at 2022-06-13 00:27:30.538264
# Unit test for function ansible_facts
def test_ansible_facts():
    # pylint: disable=import-error
    import sys
    from ansible.module_utils.facts import ansible_lsb
    from ansible.module_utils.basic import AnsibleModule

    module_args = {
        'gather_subset': ['all'],
        'filter': '*'
    }

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )
    ansible_lsb.FactsCollector(namespace=None,
                               filter_spec='*',
                               gather_subset=['all'])
    if sys.version_info[0] >= 3:
        # python 3
        assert isinstance(ansible_facts(module), dict)

# Generated at 2022-06-13 00:27:33.793313
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils.facts import Facts

    obj = Facts()

    fact = obj.get_all_facts(subset='network')

    assert fact['default_ipv4']['address'] == '127.0.0.1/8'

# Generated at 2022-06-13 00:27:42.975232
# Unit test for function ansible_facts
def test_ansible_facts():
    # some hacks to fake out ansible module, without having to import ansible.module_utils.basic
    mock_module = type('AnsibleModule', (), {'params': {}})
    mock_params = mock_module.params
    mock_params['gather_subset'] = ['all']

    mock_module.exit_json = lambda facts: facts
    mock_module.fail_json = lambda msg: msg

    fake_facts = ansible_facts(mock_module)
    assert fake_facts['distribution'] == 'Linux'

# Generated at 2022-06-13 00:27:53.781745
# Unit test for function ansible_facts
def test_ansible_facts():
    # stub to provide module, with config for stubbed modules
    class ModuleStub(object):
        def __init__(self, params):
            self.params = params

    # Stub to provide a filter method on the result of get_all_facts,
    # which returns a dict mapping bare fact names to values.
    class FactDict(dict):
        def filter(self, filter_spec):
            return self

    class StubbedFactCollector:
        def __init__(self, filter_spec, gather_subset, gather_timeout,
                     minimal_gather_subset, namespace, module):
            self.collector_classes = ['collector_stub']
            self.filtered_fact_names = []
            self.filter_spec = filter_spec
            self.gather_subset = gather_subset

# Generated at 2022-06-13 00:28:04.135096
# Unit test for function get_all_facts
def test_get_all_facts():
    '''Unit test for function get_all_facts
    '''
    import sys

    if sys.version_info < (2, 7):
        import unittest2 as unittest
    else:
        import unittest

    from ansible.module_utils.facts import get_all_facts

    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_bytes

    from six import StringIO

    from io import StringIO

    from ansible.module_utils.urls import open_url

    FAKE_URL_RESPONSE = "fake_url_response"

    # Test urlopen failures
    def fake_urlopen(query):
        class TestException(Exception):
            pass

        raise TestException

    # Test urlopen success

# Generated at 2022-06-13 00:28:14.925134
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts import ansible_collector

    # Stub out the AnsibleModule class
    class AnsibleModule(object):
        def __init__(self):
            self.params = {'gather_subset': ['all']}

        def fail_json(self, **kwargs):
            raise AssertionError(kwargs)

    mod = AnsibleModule()

    # Call the function we want to test
    facts_dict = get_all_facts(mod)

    # Assert that we got results
    assert facts_dict, 'Expected to get results'

    # Assert the keys are correct
    keys = facts_dict.keys()
    assert 'default_ipv4' in keys, keys

# Generated at 2022-06-13 00:28:25.196580
# Unit test for function get_all_facts
def test_get_all_facts():
    import os
    import json
    import unittest
    import tempfile
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.module_utils.basic import AnsibleModule

    # build the mock module
    test_dir = tempfile.mkdtemp()
    test_file_path = os.path.join(test_dir, 'ansible_facts.json')

    module_args = dict(
        _ansible_version='2.2.2.0',
        ansible_version='2.2.2.0',
        # use filter='*' for the test, since we're testing the gather_subset functionality
        filter='*',
    )
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )



# Generated at 2022-06-13 00:28:37.224901
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils.facts import ansible_collector

    # this is a fake ansible module
    module = FakeAnsibleModule()

    # Define some fakes for testing
    # This class was not designed to be fakeable, so we have to recreate the
    # methods we need
    class FakeAnsibleCollector(object):
        def __init__(self):
            self.facts_dict = dict()

        def collect(self, module):
            # just return what we set in the dict
            return self.facts_dict


# Generated at 2022-06-13 00:28:41.074244
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils import basic
    class FakeModule(object):
        def __init__(self, params):
            self.params = params
            self.args = []
    module_params = {'gather_subset': ['all']}
    module = FakeModule(module_params)
    get_all_facts(module=module)


# Generated at 2022-06-13 00:28:45.865517
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils.facts import module_utils
    test_module = module_utils.basic_info('test_get_all_facts')
    fact_dict = get_all_facts(module=test_module)
    assert 'distribution' in fact_dict


# Generated at 2022-06-13 00:28:56.405854
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.compat.tests import unittest
    from ansible.compat.tests.mock import patch
    from ansible.module_utils.facts import _gather_subset

    class TestModule(object):
        def __init__(self):
            self.params = {'gather_subset': 'all'}

    class MockAnsibleModule(object):
        def __init__(self):
            self.params = {'gather_subset': 'all'}

        def main(self, facts=None):
            return facts


# Generated at 2022-06-13 00:28:58.629406
# Unit test for function get_all_facts
def test_get_all_facts():
    # TODO: write unit test
    pass

# Generated at 2022-06-13 00:29:07.596629
# Unit test for function get_all_facts
def test_get_all_facts():
    try:
        # load the module_utils/facts/ansible_facts.py
        from ansible.module_utils.facts.ansible_facts import get_all_facts as old_get_all_facts
    except ImportError:
        # If we're on 2.2, we don't need to do anything
        old_get_all_facts = None

    from ansible.module_utils.facts.ansible_facts import get_all_facts as new_get_all_facts

    try:
        assert old_get_all_facts == new_get_all_facts
    except AssertionError:
        print(
            "Failed assertion that the old get_all_facts method equals the new get_all_facts method"
        )
        raise


# Generated at 2022-06-13 00:29:16.751945
# Unit test for function get_all_facts
def test_get_all_facts():
    import ansible.module_utils.facts.system
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.collector import AnsibleFactCollector
    class DummyModule(object):
        def __init__(self, params=None):
            self.params = params
    def test_fact_collector_class(BaseFactCollector):
        def __init__(self):
            super(test_fact_collector_class, self).__init__()
        def collect(self, module=None, collected_facts=None):
            return "Facts"
    all_collector_classes = {'test_collector': test_fact_collector_class}
    ansible_collector.AnsibleFactCollector = DummyModule()
    ansible.module

# Generated at 2022-06-13 00:29:29.039443
# Unit test for function get_all_facts
def test_get_all_facts():

    import sys
    import pytest
    from collections import defaultdict
    from ansible.modules.system.setup import setup_module as setup_module_base
    from ansible.module_utils.facts.namespace import PrefixFactNamespace

    class FakeModule(object):
        def __init__(self, *args, **kwargs):
            self.params = {}

    setup_module_base.DEFAULT_GATHER_SUBSET = ['all']
    all_collector_classes = default_collectors.collectors

    # don't add a prefix
    namespace = PrefixFactNamespace(namespace_name='ansible', prefix='')


# Generated at 2022-06-13 00:29:40.543414
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils.facts.facts import MODULE_CACHE
    from ansible.module_utils.facts import ansible_collector

    # create a fake ansiblemodule
    class FakeAnsiblemodule(object):
        def __init__(self, module_name):
            self.params = dict(gather_subset='all')
            self.params['module_name'] = module_name
            self._debug = dict()

    # create a fake module class
    class FakeModuleClass(object):
        def __init__(self):
            self.collect = lambda x: set([module_name])

        def add_prefix(self, fact_name):
            '''
            A fake add_prefix method for a module class, for unit testing
            :return:
            '''
            return 'ansible_' + fact

# Generated at 2022-06-13 00:29:50.374356
# Unit test for function get_all_facts
def test_get_all_facts():

    class FakeModule:
        def __init__(self, gather_subset=['all']):
            self.params = {'gather_subset': gather_subset}

    facts = get_all_facts(FakeModule(gather_subset=['!all', 'network']))

    assert 'ansible_hostname' in facts
    assert 'default_ipv4' in facts
    assert 'default_ipv6' in facts
    assert 'kernel' in facts
    assert 'network' in facts

    assert facts['ansible_hostname'] == 'test'
    assert facts['default_ipv4']['address'] == '1.2.3.4'
    assert facts['default_ipv6']['address'] == '1::2:3:4:5:6:7'
    assert facts['kernel']

# Generated at 2022-06-13 00:29:57.081745
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils import basic
    import argparse

    class MockAnsibleModule(object):
        def __init__(self, params):
            self.params = params

    ansible_module = MockAnsibleModule(params={'gather_subset': ['all']})

    facts = get_all_facts(ansible_module)
    assert isinstance(facts, dict)
    assert len(facts.keys()) > 0



# Generated at 2022-06-13 00:29:59.518320
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils.basic import AnsibleModule

    module_args = dict(gather_subset="!all")
    fake_module = AnsibleModule(module_args=module_args)

    facts = get_all_facts(fake_module)

    assert isinstance(facts, dict)

    assert 'default_ipv4' in facts
    assert 'distribution' in facts



# Generated at 2022-06-13 00:30:11.719016
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.facts.namespace import PrefixFactNamespace

    module = AnsibleModule(
            argument_spec = dict(gather_subset=dict(default=['all'], type='list')),
            supports_check_mode=True
    )

    # fake the 'ansible_facts' namespace
    # (shouldn't be needed, but some modules do this so test that it works)
    ansible_facts = PrefixFactNamespace(namespace_name='ansible', prefix='ansible_')
    ansible_facts.set_fact('default_ipv4', {'address': '10.90.150.255', 'interface': 'mgt0'})

# Generated at 2022-06-13 00:30:23.329619
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils.facts.facts import get_all_facts
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils import facts
    import sys

    if sys.version_info < (2, 7):
        import unittest2 as unittest
    else:
        import unittest

    module = AnsibleModule(argument_spec={})

    class TestAnsibleFacts(unittest.TestCase):
        SETUP_MODULE = None

        @classmethod
        def setUpClass(cls):
            if cls.SETUP_MODULE:
                cls.SETUP_MODULE()

        def setUp(self):
            pass

        def tearDown(self):
            pass

        def test_get_all_facts(self):
            module_

# Generated at 2022-06-13 00:30:34.299696
# Unit test for function get_all_facts
def test_get_all_facts():
    '''Unit test for ansible.module_utils.facts.get_all_facts'''

    from ansible.module_utils.facts import get_all_facts

    class FakeModule(object):

        def __init__(self, params):
            self.params = params

    # no gather_subset
    module = FakeModule({})

    all_facts = get_all_facts(module)

    assert 'default_ipv4' in all_facts

    # with gather_subset
    gather_subset = ['all', 'network', 'hardware']
    module = FakeModule({'gather_subset': gather_subset})
    all_facts = get_all_facts(module)

    assert 'default_ipv4' in all_facts
    assert 'devices' in all_facts
    assert 'architecture'

# Generated at 2022-06-13 00:30:43.405076
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils.facts import ansible_collector

    #self.all_facts
    #self.all_facts_options
    #self.gather_subset
    #self.gather_timeout
    #self.minimal_gather_subset
    #self.filter
    #self.namespace

# Generated at 2022-06-13 00:30:53.877293
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils.six import StringIO
    from ansible.module_utils.basic import AnsibleModule

    class MockModule(object):
        def __init__(self, *args):
            pass

        def fail_json(self, **kwargs):
            pass

        def params(self):
            return {'gather_subset': 'network'}

    class MockTaskQueueManager(object):
        def run(self):
            return {'contacted': {'127.0.0.1': {'ansible_facts': {'default_ipv4': {'ipv4': '192.168.0.1'}}}}}

    class MockTask(object):
        def __init__(self, args=None, **kwargs):
            pass

        def __getattr__(self, name):
            return

# Generated at 2022-06-13 00:31:07.804033
# Unit test for function get_all_facts
def test_get_all_facts():
    module = MockAnsibleModule()
    facts = get_all_facts(module)
    assert 'default_ipv4' in facts
    assert facts['default_ipv4'] == {'default_ipv4': {'address': '1.2.3.4', 'interface': 'eth0'}}



# Generated at 2022-06-13 00:31:09.075813
# Unit test for function get_all_facts
def test_get_all_facts():
    get_all_facts(module=get_module())


# Generated at 2022-06-13 00:31:14.038205
# Unit test for function get_all_facts
def test_get_all_facts():
    # Mock the AnsibleModule class
    from ansible.module_utils.facts.ansible_module import AnsibleModule
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from six import iteritems
    class MockAnsibleModule():
        def __init__(self):
            self.params = {}
            self.params['gather_subset'] = []
            self.params['gather_timeout'] = 10
            self.params['filter'] = '*'
            self.fact_namespace = PrefixFactNamespace(namespace_name='ansible', prefix='')

    mocked_module = MockAnsibleModule()

    # facts from get_all_facts function
    all_facts = get_all_facts(module = mocked_module)

    # facts from ansible_facts function
   

# Generated at 2022-06-13 00:31:24.155889
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils.facts import _get_all_facts
    # If both methods seem to be available, then use the new one.
    if hasattr(ansible_collector, 'get_all_facts'):
        #ansible_collector.get_all_facts()
        if _get_all_facts is ansible_collector.get_all_facts:
            return
    # If either of the methods is not available, then don't change the current one to the new name.
    if hasattr(ansible_collector, 'get_all_facts'):
        _get_all_facts = ansible_collector.get_all_facts
    else:
        ansible_collector.get_all_facts = _get_all_facts


test_get_all_facts()

# Generated at 2022-06-13 00:31:32.802942
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils import basic

    class FakeModule(object):
        def __init__(self):
            self.params = {
                'gather_subset': ['all'],
                'gather_timeout': 10,
                'filter': '*'
            }

    m = FakeModule()

    facts = get_all_facts(m)


# Generated at 2022-06-13 00:31:44.223594
# Unit test for function get_all_facts
def test_get_all_facts():
    '''
    test that get_all_facts() works, but only with Ansible 2.2
    '''

    import sys
    import types
    import imp

    import module_utils.facts
    import ansible.module_utils.facts

    if sys.version_info[:2] != (2, 7):
        print('unittest2 is not installed, cannot run tests')
        sys.exit(0)


# Generated at 2022-06-13 00:31:55.638095
# Unit test for function get_all_facts
def test_get_all_facts():
    import sys
    # Reload the module under the unit test
    sys.path.insert(0, 'unit_tests')
    import ansible_module_custom_facts
    from ansible.module_utils.facts import get_all_facts
    from ansible.module_utils import facts
    # Re-assign the original method
    facts.get_all_facts = ansible_module_custom_facts.get_all_facts

    module = ansible_module_custom_facts.AnsibleModule(argument_spec={
        'gather_subset': dict(type='list', required=False, default=['all']),
    })

    # Invoke the module
    all_facts = get_all_facts(module)

    # Validate the results

# Generated at 2022-06-13 00:31:59.858397
# Unit test for function get_all_facts
def test_get_all_facts():
    passed_module = MagicMock()
    passed_module.params = {'gather_subset': ['network']}
    facts_dict = get_all_facts(passed_module)
    assert facts_dict == passed_module.params

# Generated at 2022-06-13 00:32:08.010362
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils.basic import AnsibleModule

    # Fake a module
    class FakeModule(object):
        def __init__(self, gather_subset):
            self.params = {
                'gather_subset': gather_subset,
                'filter': '*'
            }

        def get_bin_path(self, binary, required=False, opt_dirs=[]):
            return 'foo'

    module = FakeModule(['platform', 'virtual'])

    gathered_facts = get_all_facts(module)

    # just a smoke test that this works as expected,
    # test that it actually works in get_all_facts_test.py
    assert gathered_facts['os_family'] == 'RedHat'

# Generated at 2022-06-13 00:32:15.137117
# Unit test for function get_all_facts
def test_get_all_facts():
    module = MagicMock()
    module.params = {}
    module.params['gather_subset'] = 'all'
    facts = get_all_facts(module)
    assert isinstance(facts, dict)
    assert 'distribution' in facts
    module.params['gather_subset'] = '!all'
    facts = get_all_facts(module)
    assert isinstance(facts, dict)
    assert 'distribution' not in facts


# Generated at 2022-06-13 00:32:41.839085
# Unit test for function get_all_facts
def test_get_all_facts():
    '''
    test get_all_facts method

    Run this test with:

        python -m testtools.run --target=./test_utils/facts_2_2.py --list

    '''
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts import ansible_collector

    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils.facts import cache

    from ansible.module_utils.facts.utils import get_all_ansible_facts

    from ansible.module_utils.facts.collections import distribution

    from test_utils.facts.base import AnsibleModuleMock

    import testtools



# Generated at 2022-06-13 00:32:46.026776
# Unit test for function get_all_facts
def test_get_all_facts():
    class FakeModule(object):
        def __init__(self):
            self.params = {}

    module = FakeModule()
    module.params['gather_subset'] = ['all']
    all_facts = get_all_facts(module)
    assert isinstance(all_facts, dict), 'facts is not type dict'
    assert all_facts, 'facts is empty'


# Generated at 2022-06-13 00:32:56.998231
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils.facts import ansible_facts

    import types
    import sys

    class TestModule(object):
        def __init__(self):
            self.params = dict()
            self.params['gather_subset'] = ['all']

    tm = TestModule()
    facts_dict = get_all_facts(tm)

    assert isinstance(facts_dict, dict)
    assert len(facts_dict) > 0

    # make sure we don't leak private stuff
    assert 'git_ansible' not in facts_dict
    assert 'ansible_python' not in facts_dict
    assert 'ansible_module_generated' not in facts_dict



# Generated at 2022-06-13 00:33:04.529559
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils.common._collections_compat import Mapping
    import pytest

    class FakeAnsibleModule:
        params = {'gather_subset': ['fake_subset'], 'gather_timeout': '10'}
        class FactsCache:
            def __init__(self, *args, **kwargs):
                pass

        def __init__(self, *args, **kwargs):
            self.exit_json = lambda x: None
            self.fail_json = lambda x: None
            self.ansible_facts = {}
            self.facts_cache = self.FactsCache()

    def fake_ansible_facts(module, gather_subset):
        return {'fake_fact': True}

    ansible_facts_original = ansible_collector.get_ansible_

# Generated at 2022-06-13 00:33:07.330185
# Unit test for function get_all_facts
def test_get_all_facts():
    module = FakeAnsibleModule()
    ansible_facts = get_all_facts(module)
    assert 'default_ipv4' in ansible_facts



# Generated at 2022-06-13 00:33:15.276896
# Unit test for function get_all_facts
def test_get_all_facts():
    import ansible.module_utils.facts as facts
    import ansible.module_utils.facts.collector.base as base
    import ansible.module_utils.facts.collector.platform as platform
    import ansible.module_utils.facts.collector.network as network
    try:
        from unittest import mock
    except ImportError:
        import mock
    from ansible.module_utils._text import to_bytes

    class MockedModule:
        def __init__(self, params):
            self.params = params

    def return_none(self):
        return None


# Generated at 2022-06-13 00:33:26.728012
# Unit test for function get_all_facts
def test_get_all_facts():
    class FakeAnsibleModule():
        def __init__(self, params):
            self.params = params

    class FakeFactsCollector():
        def collect(self, module):
            return {'fake_fact': 'fake_value'}

    module = FakeAnsibleModule(params={'gather_subset': ['all']})

    # Monkey patch the default_collector.get_fact_collector method to return our fake facts collector
    import ansible.module_utils.facts.default_collectors as default_collectors
    default_collectors.get_fact_collector = lambda: FakeFactsCollector()

    # get_all_facts will call the real get_fact_collector() and return our monkey patched version
    facts_dict = get_all_facts(module)

# Generated at 2022-06-13 00:33:33.959557
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils._text import to_text
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts import ansible_collector

    from ansible.module_utils.facts import collector
    from ansible.module_utils.facts import utils as fact_utils

    all_collector_classes = default_collectors.collectors

    # don't add a prefix
    namespace = PrefixFactNamespace(namespace_name='ansible', prefix='')

    from ansible.module_utils.facts import ansible_facts

    # create a dummy AnsibleModule with the gather_subset param.
    fake_module = fact_utils.create_dummy_ansible_module()

    fact_collector = \
        ansible_collector.get_

# Generated at 2022-06-13 00:33:43.633847
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils._text import to_bytes

    # Not importing AnsibleModule because it causes an error when unit testing
    class FakeAnsibleModule(object):

        def __init__(self, params):
            self.params = params

    # test list type
    params = {
        'gather_subset': '!all,!min,!facter'
    }
    mod = FakeAnsibleModule(params)

    assert (get_all_facts(mod) is not None)
    # test string type
    params = {
        'gather_subset': '!all,!min,!facter'
    }
    mod = FakeAnsibleModule(params)

    assert (get_all_facts(mod) is not None)
    # test invalid type

# Generated at 2022-06-13 00:33:50.606059
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils.facts import ansible_collector
    from ansible.module_utils.facts import namespace_manager
    from ansible.module_utils.facts import namespace_util

    from ansible.module_utils._text import to_bytes

    from ansible.module_utils.six import PY3
    from ansible.module_utils.six.moves import builtins

    gather_subset = []
    all_collector_classes = default_collectors.collectors

    # don't add a prefix
    namespace = PrefixFactNamespace(namespace_name='ansible', prefix='')
    namespace_manager.add_namespace(namespace)

   