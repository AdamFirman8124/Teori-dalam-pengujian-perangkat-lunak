

# Generated at 2022-06-13 00:24:17.938123
# Unit test for function ansible_facts
def test_ansible_facts():
    import copy
    import sys
    import os

    # stub out the actual implementation of AnsibleModule, since we don't need it,
    # and pytest collects it as a test, which we don't want to run.
    # would be nice if I could mock this
    class FakeAnsibleModule(object):
        def __init__(self, params):
            self.params = params
            self.params['gather_subset'] = self.params.get('gather_subset', [])

    class FakeFilePath(object):
        def exists(self):
            return True

    fake_module = FakeAnsibleModule({'gather_timeout': 10})
    # return empty facts for all facts

# Generated at 2022-06-13 00:24:28.419712
# Unit test for function ansible_facts
def test_ansible_facts():
    import json

    class TestModule:
        def __init__(self, params=None):
            self.params = params or {}

    params = dict(filter='*', gather_subset=['min'])
    test_module = TestModule(params)

    facts = ansible_facts(module=test_module)
    assert isinstance(facts, dict)

    assert len(facts) > 1

    params = dict(filter='ansible_distribution')
    test_module = TestModule(params)

    facts = ansible_facts(module=test_module)
    assert isinstance(facts, dict)

    assert len(facts) == 1

    # Example of a generated fact dict:
    #
    # {
    #   "ansible_architecture": "x86_64",
    #   "ansible_bios

# Generated at 2022-06-13 00:24:35.935468
# Unit test for function get_all_facts
def test_get_all_facts():

    # This is a simple stub for a class that implements the module API for Ansible modules
    class StubModule:

        def __init__(self, params):
            self.params = params

    # StubModule implements the ansible module API, so we can pass it to get_all_facts function.

    # the default for gather_subset
    params = dict(gather_subset=None)
    stub_module = StubModule(params)
    result = get_all_facts(stub_module)
    assert result

    # a specific gather_subset
    params = dict(gather_subset=['min'])
    stub_module = StubModule(params)
    result = get_all_facts(stub_module)
    assert result



# Generated at 2022-06-13 00:24:42.709557
# Unit test for function get_all_facts
def test_get_all_facts():
    import ansible.module_utils.facts
    import ansible.modules.system.tests.test_setup_py

    fact_collector = ansible.module_utils.facts.get_all_facts(ansible.modules.system.tests.test_setup_py.TestModule())

    assert isinstance(fact_collector, dict)
    assert ansible.module_utils.facts.__version__.__version__ in fact_collector.get('ansible_facts_version')


# Generated at 2022-06-13 00:24:54.986236
# Unit test for function ansible_facts
def test_ansible_facts():
    # Create a temporary environment variable
    os.environ['TEST_ENV_VAR'] = 'TEST'

    module = AnsibleModule(
        argument_spec=dict(
            # Add option to mock gather_subset param
            gather_subset=dict(type='list', default=[]),
        )
    )

    # Mock get_all_collectors function to return our own set of facts
    import ansible.module_utils.facts as facts_mod
    facts_mod.get_all_collectors = lambda module, *args, **kwargs: [
        facts_mod.default_collectors.get(fact) for fact in ['user_id',
                                                            'env']
    ]

    # Gather facts and assert no error
    result = ansible_facts(module)

# Generated at 2022-06-13 00:25:06.391219
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts import default_collectors as dc
    from ansible.module_utils.facts import ansible_collector as ac
    from ansible.module_utils.facts import ansible_facts as af
    from unittest.mock import MagicMock, patch
    import inspect

    # import the real collect method to test
    orig_collect = dc.FactsBase.collect

    # mock the real collect method and replace with a MagicMock object

    dc.FactsBase.collect = MagicMock(return_value=dc.FactsBase.collect(None))
    # replace the collect method with the MagicMock object

    # set up the args
    mock_module = MagicMock()
    mock_collector = MagicMock()
    mock_collector.collect.return_value = {} # set the return

# Generated at 2022-06-13 00:25:17.977889
# Unit test for function ansible_facts
def test_ansible_facts():
    import copy
    import os
    import time
    import json
    import pytest
    import shutil
    import tempfile

    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils.facts import ansible_collector
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts.system.service_mgr import _get_service_manager

    # make a temporary files that can be used as a fake remote_tmp
    old_cwd = os.getcwd()
    temp_files = tempfile.mkdtemp()
    os.chdir(temp_files)

# Generated at 2022-06-13 00:25:28.840322
# Unit test for function ansible_facts
def test_ansible_facts():
    import ansible.module_utils.facts.ansible_collector as ac
    ac.ansible_collector = MockAnsibleCollector
    import ansible.module_utils.facts.default_collectors as dc
    dc.collectors = [ MockFactCollector1, MockFactCollector2 ]
    from ansible.module_utils.six import PY3

    module = MockModule()

    facts_dict = ansible_facts(module)

    assert set(facts_dict.keys()) == set(['fact_c1-1', 'fact_c2-0', 'fact_c2-1'])
    assert facts_dict['fact_c1-1'] == 'value_c1-1'
    assert facts_dict['fact_c2-0'] == 'value_c2-0'

# Generated at 2022-06-13 00:25:37.472686
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.basic import AnsibleModule

    gather_subset = ['all']
    gather_timeout = 10
    filter_spec = '*'

    module = AnsibleModule(
        argument_spec={
            'gather_subset': dict(default=gather_subset, type=list),
            'gather_timeout': dict(default=gather_timeout, type=int),
            'filter': dict(default=filter_spec)
        }
    )

    rv = ansible_facts(module)
    assert len(rv) > 0

# Generated at 2022-06-13 00:25:46.433542
# Unit test for function ansible_facts
def test_ansible_facts():
    import unittest
    import datetime
    import ansible.module_utils.facts.collector

    class TestModule(object):
        def __init__(self):
            self.params = {}
            self.params['gather_subset'] = ['all']
            self.params['gather_timeout'] = 10

    # Tests only run when executed as a python script by the makefile
    class TestAnsibleFacts(unittest.TestCase):

        def test_ansible_facts(self):
            module = TestModule()
            ansible_facts_dict = ansible_facts(module)
            self.assertEqual(datetime.datetime.now().isoformat(), ansible_facts_dict['date_time']['iso8601'])

# Generated at 2022-06-13 00:25:59.837157
# Unit test for function get_all_facts
def test_get_all_facts():
    import unittest
    import sys
    import copy

    class MockParams:
        def __init__(self, gather_subset=None):
            self.gather_subset = gather_subset
            self.params = {'gather_subset': gather_subset}

    # test_get_all_facts
    class TestAllFactsMethods(unittest.TestCase):

        def setUp(self):
            self.module = mock_module = MockParams(['min', '!non-existent-subset', '!other'])
            self.module.params = copy.deepcopy(self.module.params)

        def test_get_all_facts_min(self):
            set_module_args(gather_subset='min')

# Generated at 2022-06-13 00:26:07.883974
# Unit test for function get_all_facts
def test_get_all_facts():
    class Module(object):
        def __init__(self, params):
            self.params = params

    class Facts(object):
        def __init__(self, ansible_collector, gather_subset):
            self.ansible_facts_to_return = ansible_collector
            self.gather_subset = gather_subset

    mock_ansible_facts_return = dict(mock_ansible_facts_return=dict())

    module = Module(dict(gather_subset=['all']))

    assert get_all_facts(module) == mock_ansible_facts_return

# Generated at 2022-06-13 00:26:18.854289
# Unit test for function ansible_facts
def test_ansible_facts():
    import sys
    import json
    import os

    sys.modules['ansible.module_utils.facts'] = __import__('ansible.module_utils.facts')
    sys.modules['ansible.module_utils.facts.ansible_collector'] = __import__('ansible.module_utils.facts.ansible_collector')
    sys.modules['ansible.module_utils.facts.namespace'] = __import__('ansible.module_utils.facts.namespace')
    sys.modules['ansible.module_utils.facts.default_collectors'] = __import__('ansible.module_utils.facts.default_collectors')

    class DummyModule():

        def __init__(self, gather_subset):
            self.params = dict(gather_subset=gather_subset)

    gather

# Generated at 2022-06-13 00:26:20.791122
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils.basic import AnsibleModule
    mod = AnsibleModule()
    mod.params = {
        'gather_subset': [],
    }
    assert get_all_facts(mod)


# Generated at 2022-06-13 00:26:23.913864
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils.facts import ansible_facts
    class FakeModule:
        def __init__(self, gather_subset):
            self.params = {'gather_subset': gather_subset}
    assert get_all_facts(FakeModule(['!bogus'])) == ansible_facts(FakeModule(['!bogus']))
    assert get_all_facts(FakeModule(['all'])) == ansible_facts(FakeModule(['all']))

# Generated at 2022-06-13 00:26:36.187802
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils.facts import DEFAULT_GATHER_SUBSET
    from ansible.module_utils._text import to_bytes

    import ansible.module_utils.facts.namespace as NAMESPACE
    # create a mock module
    class FakeModule(object):
        def __init__(self, params):
            self.params = params
    # unset any existing ansible_facts for this process
    oldansible_facts = None
    if hasattr(NAMESPACE, '__ansible_facts'):
        oldansible_facts = getattr(NAMESPACE, '__ansible_facts')
        delattr(NAMESPACE, '__ansible_facts')

# Generated at 2022-06-13 00:26:41.321457
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule()
    module.params = {'gather_subset': 'all'}

    facts = get_all_facts(module)

    assert 'distribution' in facts
    assert facts['distribution'] == 'Fedora'

    # TODO add more tests of specific facts



# Generated at 2022-06-13 00:26:51.624557
# Unit test for function get_all_facts
def test_get_all_facts():
    import sys
    import unittest

    class FakeAnsibleModule(object):
        def __init__(self, gather_subset=None):
            self.params = {'gather_subset': gather_subset}

    class TestUtilsFactsModule(unittest.TestCase):
        def test_get_all_facts_api(self):
            class FakeModule(object):
                def __init__(self, gather_subset=None):
                    self.params = {'gather_subset': gather_subset}

            module = FakeModule(gather_subset=['all'])

            fact_data = get_all_facts(module=module)
            self.assertTrue('distribution' in fact_data)

        def test_get_all_facts(self):
            module = FakeAnsible

# Generated at 2022-06-13 00:26:57.647128
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.basic import AnsibleModule
    # When using function ansible_facts directly (e.g. during unit testing)
    # you need to manually create the AnsibleModule instance.
    module = AnsibleModule(argument_spec={})
    the_facts = ansible_facts(module=module)

    # Verify the facts returned by ansible_facts are non-empty
    assert bool(the_facts)

# Generated at 2022-06-13 00:27:04.668394
# Unit test for function ansible_facts
def test_ansible_facts():
    # create a mock ansible module object
    class MockAnsibleModule(object):
        def __init__(self):
            self.params = {'gather_subset': 'fact_on_system'}

    # create a mock ansible module object
    ansible_module = MockAnsibleModule()

    # call function ansible_facts
    facts_dict = ansible_facts(ansible_module)

    # check if 'lsb' exists in the return dict
    for key in facts_dict:
        if key == 'lsb':
            break
    else:
        assert False, "failed test ansible_facts"

    print('Success: test_ansible_facts')



# Generated at 2022-06-13 00:27:10.655627
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts import ansible_facts
    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    facts = ansible_facts(None)
    assert isinstance(facts, dict)

# Generated at 2022-06-13 00:27:21.990715
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts.utils.file_discovery import get_file_lines
    from ansible.module_utils.facts.utils.file_discovery import path_dwim
    from ansible.module_utils.basic import AnsibleModule


# Generated at 2022-06-13 00:27:31.061221
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils.facts import ansible_collector
    import ansible.module_utils.facts.namespace
    import ansible.module_utils.facts.hardware
    import ansible.module_utils.facts.network
    import ansible.module_utils.facts.system
    import ansible.module_utils.facts._text_plugins
    import ansible.module_utils.facts.virtual
    import ansible.module_utils.facts.processor
    import ansible.module_utils.facts.mounts
    import ansible.module_utils.facts.locale
    import ansible.module_utils.facts.selinux
    import ansible.module_utils

# Generated at 2022-06-13 00:27:38.169392
# Unit test for function get_all_facts
def test_get_all_facts():
    '''Unit test for function get_all_facts'''
    from ansible.module_utils.basic import AnsibleModule
    from collections import namedtuple

    Parameter = namedtuple('Parameter', 'value')
    module = AnsibleModule(
        argument_spec={'gather_subset': Parameter(value=['!all', 'network'])})

    result = get_all_facts(module=module)
    assert 'ansible_facts' in result



# Generated at 2022-06-13 00:27:47.401093
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(argument_spec={'gather_subset': {'type': 'list', 'default': ['all']},
                                          'gather_timeout': {'type': 'int', 'default': 10},
                                          'filter': {'type': 'str', 'default': '*'}},)
    assert ansible_facts(module) == ansible_facts(module, ['all'])
    assert ansible_facts(module) == ansible_facts(module, gather_subset=['all'])

# Generated at 2022-06-13 00:27:56.434873
# Unit test for function ansible_facts
def test_ansible_facts():

    class AnsibleModule(object):

        def __init__(self):
            self.params = {}

        def fail_json(self, msg):
            raise Exception(msg)

    AM = AnsibleModule()

    # fake version of ansible_facts.py/ansible_facts/default_collectors.py
    class bogus_collector(object):
        pass

    # pretend we discovered the default_collectors.py module to run in ansible_facts.py
    default_collectors.collectors = [bogus_collector]

    # assert that we get back the expected keys
    try:
        facts_metadata = ansible_facts(module=AM)
    except Exception as e:
        if 'fail_json' in str(e):
            assert 'gather_subset is not supported by module' in str(e)


# Generated at 2022-06-13 00:28:04.082668
# Unit test for function ansible_facts
def test_ansible_facts():
    import json
    import sys
    import os
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '../library')
    sys.path.insert(0, path)
    from module_utils.common._collections_compat import OrderedDict
    from ansible.module_utils.facts import ansible_facts

    class MockAnsibleModule():
        def __init__(self, params=None, sdk=None):
            self.params = params or {}
            self.sdk = sdk

    class MockSdk():
        def __init__(self, hostname='localhost', username='default', password='default'):
            self.hostname = hostname
            self.username = username
            self.password = password


# Generated at 2022-06-13 00:28:14.879320
# Unit test for function ansible_facts
def test_ansible_facts():
    import sys

    try:
        # Python 3.X
        from unittest.mock import patch, Mock
        from io import StringIO
    except ImportError:
        # Python 2.X
        from mock import patch, Mock
        from StringIO import StringIO

    class FakeModule(object):
        def __init__(self, params, facts):
            self.params = params
            self.ansible_facts = facts

    module = FakeModule({}, {})

    # Test `filter` is used correctly
    with patch('ansible.module_utils.facts.ansible_collector.AnsibleFactsCollector._get_fact_subset') as _get_fact_subset:
        module = FakeModule({'filter': 'ansible_version'}, {})
        ansible_facts(module)
        _get_fact

# Generated at 2022-06-13 00:28:25.160561
# Unit test for function get_all_facts
def test_get_all_facts():
    import mock
    import os
    import pwd

    from ansible.module_utils.facts import ansible_module

    FactsParams = ansible_module.AnsibleModule.params['facts']
    FactsParams.update({'gather_subset': ['network']})
    facts_module = ansible_module.AnsibleModule(argument_spec=FactsParams,
                                                bypass_checks=True)
    facts_module.params.update({'gather_subset': ['network']})
    facts_module.params.update({'gather_timeout': 0})


# Generated at 2022-06-13 00:28:37.172847
# Unit test for function ansible_facts
def test_ansible_facts():
    import mock
    import os
    import io
    import sys

    # mock the module object
    module = mock.MagicMock()
    # mock the default gather_subset value
    module.params.get.return_value = ['!notvaliddefault', 'mandatory', 'min']
    # mock the default gather_timeout value
    module.params.get.return_value = 60
    # mock the default filter value
    module.params.get.return_value = '*'

    # mock the o/s dependent file system location
    # in /usr/share/ansible_test/facts/ansible.fact.utils
    # on each host that runs tests, which is mounted as
    # /usr/share/ansible/facts/ansible.fact.utils
    # on the docker container that runs the test playbook
    # test

# Generated at 2022-06-13 00:28:50.690835
# Unit test for function get_all_facts
def test_get_all_facts():
    '''Unit test for function get_all_facts

    Also demonstrates how to use this function'''

    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(
        argument_spec=dict(
            gather_subset=dict(default=['!all', '!fib'], type='list'),
            filter=dict(default='*', type='str')
        ),
        supports_check_mode=True
    )

    facts_dict = get_all_facts(module)

    assert facts_dict['default_ipv4']
    assert facts_dict['default_ipv4']['gateway']
    assert facts_dict['default_ipv4']['address']



# Generated at 2022-06-13 00:28:53.322125
# Unit test for function get_all_facts
def test_get_all_facts():
    module = FakeAegisModule()
    facts = get_all_facts(module=module)
    assert facts['platform'] == 'fake'


# Generated at 2022-06-13 00:28:59.112292
# Unit test for function ansible_facts
def test_ansible_facts():

    from ansible.module_utils.facts import __version__ as facts_version
    from ansible.module_utils.facts._text import to_text

    from ansible.module_utils.basic import AnsibleModule

    gather_subset = ['all']
    gather_timeout = 10
    filter_spec = ['*']
    ansible_module = AnsibleModule(
        argument_spec=dict(
            gather_subset=dict(default=['all'], type='list'),
            gather_timeout=dict(default=10, type='int'),
            filter=dict(default='*', type='str')
        ),
        supports_check_mode=True,
    )

    # Ansible's module_utils.py is responsible for importing the module_utils.facts package and
    # calling ansible_facts function.
    #
    #

# Generated at 2022-06-13 00:29:09.333672
# Unit test for function get_all_facts
def test_get_all_facts():

    from ansible.module_utils.facts import ansible_collector

    class mock_AnsibleModule(object):
        def __init__(self):
            self.params = {'gather_subset': ['all']}

    module = mock_AnsibleModule()

    facts_dict = get_all_facts(module)

    assert isinstance(facts_dict, dict)
    # confirm it has a subset of the expected facts
    assert facts_dict['group_names'] == ansible_collector.ansible_facts(module).get('group_names', None)
    assert facts_dict['distribution_release'] == ansible_collector.ansible_facts(module).get('distribution_release', None)
    assert facts_dict['distribution_version'] == ansible_collector.ansible_facts(module).get

# Generated at 2022-06-13 00:29:18.120728
# Unit test for function ansible_facts
def test_ansible_facts():
    '''Unit test for function ansible_facts'''

    from ansible.module_utils.facts import ansible_facts

    class MockAnsibleModule(object):
        def __init__(self):
            self.params = {'gather_timeout': 10}
            self.params['gather_subset'] = ['all']

    test_module = MockAnsibleModule()

    facts = ansible_facts(test_module)
    # print(facts)
    assert facts
    # print(facts['distribution'])
    assert facts['distribution']

    test_module.params['gather_subset'] = ['platform']
    facts = ansible_facts(test_module)
    # print(facts)
    assert 'distribution' not in facts
    assert 'platform' in facts
    assert facts['platform']


# Generated at 2022-06-13 00:29:28.302782
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts.collector import generic_fact_collector

    class MockModule(object):
        def __init__(self, params):
            self.params = params

        def get_bin_path(self, executable, required=True, opt_dirs=[]):
            pass

    module = MockModule(params={'gather_subset': ['all'],
                                'gather_timeout': 10,
                                'filter': '*'})
    fact_collector = generic_fact_collector.GenericFactCollector('test_collector',
                                                                 namespace=None,
                                                                 gather_subset=['all'],
                                                                 gather_timeout=10,
                                                                 supported_os=None,
                                                                 minimal_gather_subset=None)


# Generated at 2022-06-13 00:29:29.874295
# Unit test for function ansible_facts
def test_ansible_facts():
    module = None
    assert ansible_facts(module) == {}

# Generated at 2022-06-13 00:29:41.149549
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts import ansible_collector
    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils._text import to_bytes

    class TestModule(object):
        def __init__(self, params):
            self.params = params

    class FakeCollector(object):
        def __init__(self, name, fact_name, fact_value):
            self.name = name
            self.fact_name = fact_name
            self.fact_value = fact_value

        def collect(self, module):
            return {self.fact_name: self.fact_value}


# Generated at 2022-06-13 00:29:46.126061
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(argument_spec=dict(
        gather_subset=dict(default=['all'], type='list'),
        gather_timeout=dict(default=10, type='int'),
        filter=dict(default='*', type='str'),
    ))
    fact_dict = ansible_facts(module)
    assert len(fact_dict) > 0

# Generated at 2022-06-13 00:29:57.414136
# Unit test for function ansible_facts
def test_ansible_facts():
    class FakeModule:
        def __init__(self, fact_dict):
            self.params = fact_dict

    def verify_facts(fact_dict):
        fake_module = FakeModule(fact_dict)
        ansible_facts_dict = ansible_facts(fake_module)
        expected_fact_dict = dict(('ansible_' + k, v) for k,v in fact_dict.items())
        assert ansible_facts_dict == expected_fact_dict

    # test gather_subset
    verify_facts({'gather_subset': ['minimal']})
    verify_facts({'gather_subset': ['!minimal']})
    verify_facts({'gather_subset': ['all']})
    verify_facts({'gather_subset': 'minimal'})
    verify_

# Generated at 2022-06-13 00:30:14.549480
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils.facts import ansible_collector
    from ansible.module_utils.facts import ansible_facts as ansible_facts_orig

    from ansible.module_utils._text import to_native
    from ansible.module_utils.six.moves import reload_module

    import os
    import types
    import ansible
    import ansible.module_utils.facts.system.distribution as distribution
    import ansible.module_utils.facts.system.platform as platform
    import ansible.module_utils.facts.system.distribution as distribution
    import ansible.module_utils.facts.system.pkg_mgr as pkg_mgr


# Generated at 2022-06-13 00:30:21.523177
# Unit test for function ansible_facts
def test_ansible_facts():
    import mock
    class FakeModule(object):
        def __init__(self):
            self.params = {}
        def get_option(self, k):
            return self.params.get(k)

    m = FakeModule()
    m.params = dict(
        gather_subset=['all'],
        filter='*',
        gather_timeout=10
    )
    with mock.patch.object(ansible_collector, 'get_ansible_collector') as get_ansible_collector:
        ansible_facts(m)


# Generated at 2022-06-13 00:30:32.921851
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts import collector
    collector.GATHERER_SUBSET = set()

    import ansible.module_utils.facts.collector
    ansible.module_utils.facts.collector.GATHERER_SUBSET = set()

    import ansible.module_utils.facts.default_collectors
    ansible.module_utils.facts.default_collectors.GATHERER_SUBSET = set()


# Generated at 2022-06-13 00:30:42.646256
# Unit test for function ansible_facts
def test_ansible_facts():
    '''Unit test for ansible_facts function'''
    class ModuleStub(object):
        '''minimal stub module'''
        def __init__(self, params=None):
            self.params = params or dict()

    # test gathering all facts
    module = ModuleStub()
    facts = ansible_facts(module)

    # test that all facts are returned
    for collector_class in default_collectors.collectors:
        assert collector_class.COLLECTOR_NAME in facts
        assert len(facts[collector_class.COLLECTOR_NAME]) > 0

    # test minimal gather subset (just the bare minimum to get a gather_subset to work)
    module = ModuleStub(params=dict(gather_subset=['min']))
    minimal_facts = ansible_facts(module)


# Generated at 2022-06-13 00:30:52.802004
# Unit test for function ansible_facts
def test_ansible_facts():
    facts_dict1 = ansible_facts()
    assert isinstance(facts_dict1, dict)

    facts_dict2 = ansible_facts(gather_subset=['all'])
    assert isinstance(facts_dict2, dict)
    assert facts_dict1 == facts_dict2

    facts_dict3 = ansible_facts(gather_subset=['min'])
    assert isinstance(facts_dict3, dict)
    assert len(facts_dict1) > len(facts_dict3)

    facts_dict4 = ansible_facts(gather_subset=['!all'])
    assert isinstance(facts_dict4, dict)
    assert facts_dict4 == {}

# Generated at 2022-06-13 00:31:05.347491
# Unit test for function ansible_facts
def test_ansible_facts():

    # Create a simple AnsibleModule for a test
    class FakeModule(object):

        def __init__(self, params):
            self.params = params

    # Test values
    fact_name = 'ansible_default_ipv4'
    fact_value = '123.123'
    gather_subset = ['network', 'all']
    gather_timeout = 5
    filter_spec = '*'

    # Create a simple module
    module = FakeModule(params={'gather_subset': gather_subset, 'gather_timeout': gather_timeout,
                                'filter': filter_spec})

    # Get some facts
    results = ansible_facts(module)

    # Check that module.params was used correctly
    assert(gather_subset == module.params['gather_subset'])

# Generated at 2022-06-13 00:31:13.928339
# Unit test for function ansible_facts
def test_ansible_facts():
    '''unit test for ansible_facts'''

    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.facts import ansible_collector

    module = AnsibleModule()

    # no gather_subset specified
    facts = ansible_facts(module=module)

    assert 'fqdn' in facts
    assert len(ansible_collector.ALL_COLLECTORS) == len(facts)

    # '!all' should have no facts other than ansible_facts
    facts = ansible_facts(module=module, gather_subset=['!all'])
    assert len(facts) == 1

    facts = ansible_facts(module=module, gather_subset=['!all', 'fqdn'])
    assert len(facts) == 2

# Generated at 2022-06-13 00:31:17.947907
# Unit test for function ansible_facts
def test_ansible_facts():
    import datetime
    import sys
    import types

    from ansible.module_utils.facts import ansible_facts

    # return a dict for the gathered facts
    def as_dict(fact_class):
        '''Convert an instance of a fact class to a dict, by iterating its
        public members.'''

        ret = {}

        for fact_name in fact_class.__dict__:
            if fact_name.startswith('_'):
                continue

            fact_value = fact_class.__dict__[fact_name]

            if isinstance(fact_value, types.FunctionType):
                continue

            ret[fact_name] = fact_value

        return ret

    # Test that ansible_facts returns the expected facts

# Generated at 2022-06-13 00:31:27.782664
# Unit test for function ansible_facts
def test_ansible_facts():
    # setup a test module
    module = AnsibleModule(
        argument_spec=dict(
            gather_subset=dict(default=['all']),
            gather_timeout=dict(default=10)
        )
    )

    facts_dict = ansible_facts(module)

    keys = facts_dict.keys()
    keys.sort()

# Generated at 2022-06-13 00:31:35.513160
# Unit test for function ansible_facts
def test_ansible_facts():
    # stub only what we need for this unit test
    class Module:
        def __init__(self, gather_subset=None, gather_timeout=10, filter=None):
            self.gather_subset = gather_subset
            self.gather_timeout = gather_timeout
            self.filter = filter

    class AnsibleModule:
        def __init__(self, gather_subset=None, gather_timeout=10, filter=None):
            self.module = Module(gather_subset=gather_subset,
                                 gather_timeout=gather_timeout,
                                 filter=filter)
            self.params = {'gather_subset': gather_subset,
                           'gather_timeout': gather_timeout,
                           'filter': filter}

    # test a valid file
    assert ansible

# Generated at 2022-06-13 00:31:56.365152
# Unit test for function ansible_facts
def test_ansible_facts():
    module = AnsibleModule(argument_spec={})
    collected_facts = ansible_facts(module)

    facts_with_ansible_namespace = set()
    facts_with_ansible_namespace.add('ansible_all_ipv4_addresses')
    facts_with_ansible_namespace.add('ansible_all_ipv6_addresses')
    facts_with_ansible_namespace.add('ansible_architecture')
    facts_with_ansible_namespace.add('ansible_bios_date')
    facts_with_ansible_namespace.add('ansible_bios_version')
    facts_with_ansible_namespace.add('ansible_cmdline')
    facts_with_ansible_namespace.add('ansible_date_time')
   

# Generated at 2022-06-13 00:32:06.660021
# Unit test for function ansible_facts
def test_ansible_facts():
    import ansible.module_utils.facts.generic
    import ansible.module_utils.facts.network

    # This test runs the ansible_facts() function by calling it directly.
    # Normally this function is called by the AnsibleModule framework
    # when collecting facts.  When running the function in this test environment
    # we do not want the AnsibleModule framework to attempt to call the ansible_facts()
    # function again.  This test function will call it directly.  So we set the
    # AnsibleModule framework value to None to tell it to not call it again.

    ansible.module_utils.facts.generic.ansible_facts = None
    ansible.module_utils.facts.network.ansible_facts = None

    from ansible.module_utils._text import to_text

# Generated at 2022-06-13 00:32:15.210547
# Unit test for function ansible_facts
def test_ansible_facts():

    # mock AnsibleModule
    from ansible.module_utils.facts import ansible_facts

    class MockAnsibleModule:
        # __init__ is called by AnsibleModule, so we can't stub out the class that way.
        # Instead, we mock it out with a mock_init method
        def mock_init(self, _):
            self.params = {'gather_subset': ['network']}

    ansible_module = MockAnsibleModule()

# Generated at 2022-06-13 00:32:24.902969
# Unit test for function ansible_facts
def test_ansible_facts():
    pass
    # For python 2.6, we need to add support for unit tests.
    # import mock
    # from ansible.module_utils import facts
    # from ansible.module_utils.facts import default_collectors

    # class MockModule():
    #     def __init__(self):
    #         self.params = {
    #             'filter': '*',
    #         }

    #     class MockFailJson():
    #         def __init__(self, module, msg):
    #             self.module = module
    #             self.msg = msg

    #         def __call__(self, *args, **kwargs):
    #             if args == ():
    #                 # This is a call to fail_json()
    #                 msg = self.msg
    #                 if kwargs:


# Generated at 2022-06-13 00:32:35.314996
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts import ansible_facts
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils.facts import ansible_collector
    from ansible.module_utils.facts import collector

    from ansible.module_utils.facts.virt_types import VirtualizationType

    import mock
    import os.path

    # Mock the ansible module
    mock_module = mock.MagicMock()
    mock_module.params = {'filter': '*'}

    # Mock the collector.get_file_content method
    mock_get_file_content = mock.MagicMock()


# Generated at 2022-06-13 00:32:40.704374
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.compat.tests import unittest

    module = FakeAnsibleModule()
    facts_dict = get_all_facts(module)
    assert isinstance(facts_dict, dict)
    assert 'default_ipv4' in facts_dict
    assert facts_dict['default_ipv4'] == {'address':'127.0.0.1', 'interface':'localhost'}


# Generated at 2022-06-13 00:32:49.715857
# Unit test for function ansible_facts
def test_ansible_facts():
    import ansible.module_utils.facts.collector
    ansible.module_utils.facts.collector._COLLECTORS = default_collectors.collectors

    class TestModule(object):

        def __init__(self):
            self.params = None

        def fail_json(self, msg, **kwargs):
            raise Exception(msg)

    class DummyFactsModule(TestModule):
        def __init__(self):
            self.params = {'gather_subset': ['!all'], 'gather_timeout': 30}
            self.fail_json = TestModule.fail_json

    module = DummyFactsModule()
    facts = ansible_facts(module)
    assert 'all' not in facts
    assert 'default_ipv4' in facts


# Generated at 2022-06-13 00:33:00.950281
# Unit test for function ansible_facts
def test_ansible_facts():
    class Module():
        def __init__(self):
            self.params = {'fact_path': '/tmp'}

    module = Module()

    facts = ansible_facts(module)

# Generated at 2022-06-13 00:33:11.665051
# Unit test for function ansible_facts
def test_ansible_facts():
    import collections
    import json
    import os
    import re
    import shutil
    import tempfile
    import time
    import unittest

    try:
        from unittest import mock
    except ImportError:
        import mock

    from ansible.module_utils._text import to_bytes

    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts.collector.apparmor import AppArmorFactCollector
    from ansible.module_utils.facts.collector.base import BaseFactCollector
    from ansible.module_utils.facts.collector.cmdline import CmdlineFactCollector
    from ansible.module_utils.facts.collector.date_time import DateTimeFactCollect

# Generated at 2022-06-13 00:33:23.434811
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils import basic
    import mock

    bare_fact_name = 'default_ipv4'
    ansible_fact_name = 'ansible_default_ipv4'

    # create a mock instance of AnsibleModule
    mock_module = mock.MagicMock(spec=basic.AnsibleModule)
    mock_module.params['gather_subset'] = ['all']  # module.params['gather_subset'] is used in get_all_facts
    mock_module.params['gather_timeout'] = 10
    mock_module.params['filter'] = '*'

    ansible_facts = get_all_facts(module=mock_module)

    assert ansible_facts[bare_fact_name] == ansible_facts[ansible_fact_name]

# Generated at 2022-06-13 00:33:51.205302
# Unit test for function ansible_facts
def test_ansible_facts():
    import ansible.module_utils.facts.ansible_facts as ansible_facts
    import ansible.module_utils.facts.default_collectors as default_collectors

    class module(object):
        def __init__(self):
            self.params = {'gather_subset': ['all'], 'gather_timeout': 10,
                           'filter': '*'}

    facts_dict = ansible_facts.ansible_facts(module())

    default_collectors.default_collector.assert_called_once()

    assert facts_dict['os_family'] == 'Debian'

# Generated at 2022-06-13 00:33:56.311100
# Unit test for function get_all_facts
def test_get_all_facts():
    mock_module = type(u'MockModule', (), {u'params': {u'gather_subset': [u'all']}})
    mock_module = mock_module()

    all_facts = get_all_facts(mock_module)

    assert type(all_facts) == dict
    assert u'lsb' in all_facts
    assert u'ansible_date_time' in all_facts
    assert len(all_facts) == 75



# Generated at 2022-06-13 00:34:06.615510
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts import ansible_facts
    from ansible.module_utils.facts.system.distribution import DistributionFactCollector
    from ansible.module_utils.facts.system.distribution import LinuxDistributionFactCollector

    # test we get a dict of ansible_facts data back
    ansible_facts_dict = ansible_facts(module=None)
    assert isinstance(ansible_facts_dict, dict)

    # test that ansible_facts has the correct keys
    assert isinstance(ansible_facts_dict, dict)
    #test that ansible_distribution is always present
    assert 'distribution' in ansible_facts_dict
    # test that a Linux distribution get the LinuxDistributionCollector

# Generated at 2022-06-13 00:34:11.264019
# Unit test for function get_all_facts
def test_get_all_facts():
    module = AnsibleModule(argument_spec={
        'gather_subset': dict(type='list', default=['!all']),
    }, supports_check_mode=True)
    result = get_all_facts(module)
    assert result['fqdn'] == 'localhost.localdomain'

