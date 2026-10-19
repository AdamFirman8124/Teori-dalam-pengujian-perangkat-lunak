

# Generated at 2022-06-13 00:24:17.393618
# Unit test for function ansible_facts
def test_ansible_facts():
    import os
    import json
    import re

    # Mock out AnsibleModule so this module can be run as a unit test
    # See https://docs.ansible.com/ansible/developing_modules.html#unit-testing-modules

    class AnsibleModule:
        def __init__(self, argspec, **kwargs):
            self.params = kwargs
            self.facts = {}
            self.exit_json = self._exit_json
            self.fail_json = self._fail_json
            self.deprecate = self._deprecate

        def _exit_json(self, changed=False, ansible_facts=None):
            if ansible_facts:
                self.facts = ansible_facts


# Generated at 2022-06-13 00:24:20.551784
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule()

    facts = ansible_facts(module=module)

    assert facts['distribution'] == 'RedHat'

# Generated at 2022-06-13 00:24:30.909029
# Unit test for function ansible_facts
def test_ansible_facts():
    import collections
    import textwrap


# Generated at 2022-06-13 00:24:41.791975
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts.utils import get_all_collector_classes

    all_collectors = get_all_collector_classes()

    # Create a bare minimum module.  We don't have enough of the context here to construct a real module
    m = type('module', (object,), {})()

    # Define the minimum set of params we will need
    m.params = {}
    m.params['gather_subset'] = ['all']
    m.params['filter'] = '*'
    m.params['gather_timeout'] = 10

    # Define a few test facts for us to return when run
    #  We will return a different set of facts depending on the function name passed in as module.run_command

# Generated at 2022-06-13 00:24:47.919373
# Unit test for function get_all_facts
def test_get_all_facts():
    for x in [1, 2, 3]:
        class AnsibleModule(object):

            def __init__(self, params):
                self.params = params

        gather_subset = ['!all', 'network']
        gather_timeout = 10

        m = AnsibleModule({'gather_subset': gather_subset,
                           'gather_timeout': gather_timeout,
                           'filter': 'ansible_eth'})

        ansible_facts = get_all_facts(module=m)

        assert isinstance(ansible_facts, dict)
        assert 'ansible_eth0' in ansible_facts
        assert 'ansible_eth1' not in ansible_facts


# Generated at 2022-06-13 00:24:52.212867
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts.facts import a_fact, b_fact
    from ansible.module_utils.facts.ansible_collector import AnsibleCollector
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts.fact_cache import FactCache
    from ansible.module_utils.facts.collectors import default_collectors
    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils.facts import default_collectors


    # mock module
    class FakeModule(AnsibleModule):
        def __init__(self, *args, **kwargs):
            self.params = kwargs['params']

# Generated at 2022-06-13 00:24:55.572266
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts import ansible_facts
    assert ansible_facts(None, gather_subset=None)
    assert ansible_facts(None, gather_subset=[])
    assert ansible_facts(None, gather_subset=['all'])

# Generated at 2022-06-13 00:25:03.661403
# Unit test for function get_all_facts
def test_get_all_facts():
    assert get_all_facts.__name__ == 'get_all_facts'
    assert get_all_facts.__doc__ == '''compat api for ansible 2.2/2.3 module_utils.facts.get_all_facts method

    Expects module to be an instance of AnsibleModule, with a 'gather_subset' param.

    returns a dict mapping the bare fact name ('default_ipv4' with no 'ansible_' namespace) to
    the fact value.'''



# Generated at 2022-06-13 00:25:04.219127
# Unit test for function ansible_facts
def test_ansible_facts():
    pass

# Generated at 2022-06-13 00:25:11.079009
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts.namespace import FactNamespace
    import ansible.module_utils.facts.namespace as namespace_module

    # We do use the real module class, so that we can test the argument parsing of the
    # module. It's not a perfect / comprehensive test. (In particular it doesn't test
    # whether we actually parse the gather_facts from the playbook correctly into the
    # module params.

    from ansible.modules.system import setup
    module = setup.AnsibleModule(argument_spec={'gather_subset': dict(default=['*'], type='list'),
                                                'filter': dict(required=False, type='list'),
                                                'gather_timeout': dict(default=10, type='int')})

    # We first test the default case. We run the 'ansible

# Generated at 2022-06-13 00:25:21.723774
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts._cache import FactsCache
    from ansible.module_utils.facts import ansible_facts
    from ansible.module_utils.facts import default_collectors

    mock_get_all_subset_collectors = {'collectors': [frozenset(['foo']), frozenset(['bar']), frozenset(['baz'])]}

    mock_collector = dict()
    mock_collector['collect'] = lambda *args, **kwargs: {'foo': 'bar'}
    mock_collector['subset'] = frozenset(['foo'])
    mock_collector['depends_on'] = frozenset([])
    mock_collector['fqcn'] = 'test_ansible_facts'

    mock_get_all_subset_collectors

# Generated at 2022-06-13 00:25:29.746390
# Unit test for function ansible_facts
def test_ansible_facts():
    import os
    # hack to add the parent directory of this file to the pythonpath
    # so that we can import the AnsibleModule stub and set some arguments
    # (in case we want to test from a different directory)
    import sys
    import inspect
    this_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
    sys.path.append(os.path.dirname(this_dir))
    from ansible.module_utils.facts.utils import FactsHelper
    FactsHelper.default_gather_timeout = 0
    from ansible.module_utils.facts.ansible_collector import AnsibleCollector
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts.user.user import UserCollector

# Generated at 2022-06-13 00:25:41.272347
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts import ansible_facts as ansible_facts_func

    class AnsibleModule:
        def __init__(self, params):
            self.params = params

    # Test gather_subset='!all'
    params = dict(gather_subset='!all',
                  gather_timeout=10,
                  filter='*')
    am = AnsibleModule(params)

    facts_dict = ansible_facts_func(am)
    assert facts_dict
    assert not facts_dict.get('ansible_all_ipv4_addresses')

    # Test gather_subset=['!all']
    params = dict(gather_subset=['!all'],
                  gather_timeout=10,
                  filter='*')
    am = AnsibleModule(params)
    facts_

# Generated at 2022-06-13 00:25:45.112982
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils.facts import get_all_facts

    facts_dict = get_all_facts(module=None)
    assert facts_dict is not None
    assert 'ansible_lsb' in facts_dict
    assert 'ansible_lsb' not in facts_dict  # duplicate copy due to dup namespace


# Generated at 2022-06-13 00:25:54.743406
# Unit test for function ansible_facts
def test_ansible_facts():
    module = ansible.module_utils.basic.AnsibleModule(argument_spec={})

    # Test with gather_subset=all
    val = ansible_facts(module, gather_subset=['all'])
    assert 'ansible_kernel' in val
    assert 'ansible_architecture' in val
    assert 'ansible_virtualization_role' in val

    # Test with gather_subset=minimal
    val = ansible_facts(module, gather_subset=['minimal'])
    assert val['ansible_kernel'] == 'Linux'
    assert val['ansible_distribution'] == 'RedHat'

# Generated at 2022-06-13 00:26:03.214579
# Unit test for function ansible_facts
def test_ansible_facts():
    import ansible.module_utils.facts
    # todo; mock the module
    module = ansible.module_utils.facts.AnsibleModule(argument_spec={})
    facts = ansible_facts(module=module)
    assert facts
    assert 'distribution' in facts
    assert 'distribution_release' in facts
    assert 'distribution_version' in facts
    assert 'ansible_python' in facts
    assert 'ansible_python_version' in facts
    assert 'ansible_python_version_info' in facts
    assert 'python_version' in facts
    assert facts['ansible_python_version'] == facts['python_version']

# Generated at 2022-06-13 00:26:11.454690
# Unit test for function ansible_facts
def test_ansible_facts():
    '''Unit test for ansible_facts'''

    from ansible.module_utils.facts import namespace
    from ansible.module_utils.facts.system import distribution
    from ansible.module_utils.facts.system import selinux
    from ansible.module_utils.facts.virtual import lxc

    class FakeModule:
        params = {'filter': '*'}

    # get a subclass of FakeModule that has a gather_subset arg
    module_with_gather_subset = get_module_with_gather_subset(FakeModule)
    # get a subclass of FakeModule that does not have a gather_subset arg
    module_without_gather_subset = get_module_without_gather_subset(FakeModule)

    # test that when gather_subset is provided, only it's fact collectors are

# Generated at 2022-06-13 00:26:14.796437
# Unit test for function ansible_facts
def test_ansible_facts():
    '''Unit test for function ansible_facts'''

    # ansible_facts should not throw an exception
    ansible_facts(AnsibleModule())


# Mock class for AnsibleModule with default params

# Generated at 2022-06-13 00:26:22.574037
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts.collector import TestModule
    module = TestModule()
    result = ansible_facts(module, gather_subset=['min'])
    assert result['python']['version']['major'] == 2 or result['python']['version']['major'] == 3
    result = ansible_facts(module, gather_subset=['all'])
    assert result['python']['version']['major'] == 2 or result['python']['version']['major'] == 3


if __name__ == "__main__":
    import pytest
    pytest.main()

# Generated at 2022-06-13 00:26:33.354107
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils.facts import get_all_facts
    import pytest
    class FakeModule:
        def __init__(self):
            self.params = {}

    valid_subset = [
        'all', 'min', '!all', '!min', 'foo', '!foo'
    ]

    @pytest.mark.parametrize("subset", valid_subset)
    def test_subset_is_valid(subset):
        fake_module = FakeModule()
        fake_module.params['gather_subset'] = subset
        facts = get_all_facts(fake_module)
        assert 'default_ipv4' in facts

# Generated at 2022-06-13 00:26:45.972635
# Unit test for function ansible_facts
def test_ansible_facts():
    '''Exercise get_all_facts with a made up ansible_module'''

    class MockAnsibleModule(object):
        '''Mock class of AnsibleModule to exercise get_all_facts

        This is no longer needed as of Ansible 2.3.2.1,
        ansible_facts.get_all_facts no longer calls ansible_facts.ansible_facts.
        (ansible_facts.get_all_facts is used by unit tests of 2.3.2.1 and 2.4)
        '''
        def __init__(self):
            self.params = {'gather_subset': ['all']}


# Generated at 2022-06-13 00:26:46.605017
# Unit test for function ansible_facts
def test_ansible_facts():
    pass

# Generated at 2022-06-13 00:26:55.480346
# Unit test for function get_all_facts
def test_get_all_facts():

    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts import collector
    import ansible.module_utils.facts.system.distribution as distribution

    class FakeBaseFactCollector(BaseFactCollector):

        def __init__(self, *args, **kwargs):
            super(FakeBaseFactCollector, self).__init__(*args, **kwargs)
            self.default_subset = set(['all'])
            self.gatherable = set()

        def collect(self, module=None, collected_facts=None):
            return {'name': 'test_fact_collector'}

    class FakeFactCollector(FakeBaseFactCollector, collector.FactCollector):
        pass

    # Each of these keys should map to an object in the
    #

# Generated at 2022-06-13 00:27:07.183207
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts.system import LinuxDistributionFactCollector
    from ansible.module_utils.facts.system import PlatformFactCollector
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.facts import namespace

    class TestModule(AnsibleModule):
        pass

    my_module = TestModule(argument_spec={
        'gather_subset': {'type': 'list', 'default': ['!all']},
        'gather_timeout': {'type': 'int', 'default': 10},
        'filter': {'type': 'str', 'default': '*'}},
        supports_check_mode=False,)

    my_module.params['gather_subset'] = ['!all']

# Generated at 2022-06-13 00:27:16.915818
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts import get_all_collector_classes
    from ansible.module_utils.facts.network.base import NetworkCollector
    import ansible.module_utils.facts.network.default
    from ansible.module_utils.facts.system.base import SystemCollector
    import ansible.module_utils.facts.system.distribution
    from ansible.module_utils.facts.virtual.base import VirtualCollector
    import ansible.module_utils.facts.virtual.jail

    class MyCollector:

        def __init__(self, module):
            pass

        @classmethod
        def is_available(cls, module=None):
            # return true for this test
            return True


# Generated at 2022-06-13 00:27:27.301134
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts.network.base import NetworkCollector

    test_gather_subset = ['network']
    test_gather_timeout = 1
    test_filter_spec = 'ansible_'
    test_minimal_gather_subset = ['network']

    collector_class = NetworkCollector

    # To test ansible_facts we fake out an AnsibleModule
    class ModuleFake:
        def __init__(self, gather_subset, gather_timeout, filter, minimal_gather_subset):
            self.params = {
                'gather_subset': gather_subset,
                'gather_timeout': gather_timeout,
                'filter': filter,
                'minimal_gather_subset': minimal_gather_subset
            }


# Generated at 2022-06-13 00:27:32.813793
# Unit test for function ansible_facts
def test_ansible_facts():
    try:
        from ansible.module_utils.facts import ansible_facts
    except ImportError:
        # ansible_facts is only in Ansible modules after 2.2
        return

    from ansible.module_utils.basic import AnsibleModule
    facts = ansible_facts(AnsibleModule(argument_spec={}))
    assert 'kernel' in facts
    assert facts['kernel'] == 'Linux'
    assert 'python' in facts
    assert facts['python']['version']['major'] == 3

test_ansible_facts()

# Generated at 2022-06-13 00:27:45.182736
# Unit test for function ansible_facts
def test_ansible_facts():
    import collections
    import sys
    import unittest
    import warnings
    import types

    class FakeModule:
        def __init__(self, gather_subset, gather_timeout, filter_spec=None):
            self.params = {
                'gather_subset': gather_subset,
                'gather_timeout': gather_timeout,
                'filter': filter_spec}

    class FakeAnsibleModule:
        def __init__(self, gather_subset, gather_timeout, filter_spec=None):
            self.params = {
                'gather_subset': gather_subset,
                'gather_timeout': gather_timeout,
                'filter': filter_spec}

    class TestAnsibleFacts(unittest.TestCase):
        def setUp(self):
            pass


# Generated at 2022-06-13 00:27:45.793660
# Unit test for function ansible_facts
def test_ansible_facts(): pass

# Generated at 2022-06-13 00:27:50.071184
# Unit test for function get_all_facts
def test_get_all_facts():

    from collections import namedtuple
    from ansible.module_utils.facts.namespace import PrefixFactNamespace

    class AnsibleModuleFake:
        def __init__(self, params):
            self.params = params

    # test simplest case
    ansible_module = AnsibleModuleFake(
        params={'gather_subset': ['all']})
    result = get_all_facts(ansible_module)
    assert 'ansible_os_family' in result, \
        'ansible_os_family should be in result, but is not'
    assert 'ansible_all_ipv4_addresses' in result, \
        'ansible_all_ipv4_addresses should be in result, but is not'

# Generated at 2022-06-13 00:28:04.839931
# Unit test for function ansible_facts
def test_ansible_facts():
    # FakeAnsibleModule with mocked_params compatible with the logic in ansible_facts:
    # gather_subset defaults to ['all']
    # gather_timeout defaults to 10

    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils.facts import ansible_collector

    class AnsibleModule(object):
        def __init__(self, mocked_params):
            self.params = mocked_params

    module = AnsibleModule({})
    gather_subset = None
    ansible_facts = ansible_facts(module, gather_subset=gather_subset)
    assert isinstance(ansible_facts, dict)
    print(ansible_facts)
    assert 'default_ipv4' in ansible_facts



# Generated at 2022-06-13 00:28:13.320132
# Unit test for function ansible_facts
def test_ansible_facts():
    '''Returns bare fact name and value; no prefix, no namespace, no fact_list'''

    # make a mock AnsibleModule
    class MockModule:
        def __init__(self, params):
            self.params = params

    module = MockModule({'f': 'ansible_lsbinfo.architecture'})
    result = ansible_facts(module)
    assert result['lsbinfo']['architecture'] == 'mock_arch'

    result = ansible_facts(module, ['lsbinfo'])
    assert result['lsbinfo']['architecture'] == 'mock_arch'

# Generated at 2022-06-13 00:28:23.921692
# Unit test for function ansible_facts
def test_ansible_facts():

    from ansible.module_utils.facts.hardware import Hardware
    from ansible.module_utils.facts.system import System
    from ansible.module_utils.facts.virtual import Virtual
    from ansible.module_utils.facts.network import Network
    from ansible.module_utils.facts.misc import Misc

    import unittest

    class TestModule:
        def __init__(self, params):
            self.params = params
        def fail_json(self, **kwargs):
            raise unittest.TestCase.failureException(kwargs['msg'])
        def user_has_persistent_connections(self):
            return False
        def get_bin_path(self, binary, opt_dirs=[]):
            return binary


# Generated at 2022-06-13 00:28:35.403156
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts.utils import get_all_collector_classes
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.facts.utils import get_collector
    from ansible.module_utils._text import to_text

    all_collector_classes = get_all_collector_classes()

    # don't add a prefix
    namespace = PrefixFactNamespace(namespace_name='', prefix='')


# Generated at 2022-06-13 00:28:42.920092
# Unit test for function ansible_facts
def test_ansible_facts():
    '''Unit test for function ansible_facts'''
    import unittest
    import ansible.module_utils.facts.system.distribution
    class FakeModule(object):
        def __init__(self):
            self.params = {'gather_subset': ['all'], 'filter': ['*', '!faked'], 'gather_timeout': 5}


# Generated at 2022-06-13 00:28:54.205123
# Unit test for function get_all_facts
def test_get_all_facts():
    import os
    import sys
    import collections
    import tempfile

    pytest_plugins = 'pytest_ansible'


# Generated at 2022-06-13 00:28:59.200060
# Unit test for function ansible_facts
def test_ansible_facts():
    '''Unit test for module_utils.facts.ansible_facts'''

    from ansible.module_utils.facts import ansible_facts

    from ansible.module_utils.facts.test_utils import AnsibleModuleMock
    module = AnsibleModuleMock()

    facts_dict = ansible_facts(module)

    assert 'distribution' in facts_dict

# Generated at 2022-06-13 00:29:09.376741
# Unit test for function get_all_facts
def test_get_all_facts():
    import sys
    import os

    # the import ansible.module_utils.facts.legacy causes the current working dir to be added
    # to the system path. if we don't remove it we'll pick up the wrong ansible module
    sys.path.pop(0)

    # we need to remove the current working dir from sys.path as well so we don't hit the wrong
    # 'ansible' package dir
    local_dir = os.path.dirname(__file__)
    cwd = os.getcwd()
    if cwd in sys.path:
        del sys.path[sys.path.index(cwd)]

    from ansible.module_utils.facts.legacy import ModuleStub

    module = ModuleStub(params={'gather_subset': ['all']})
    facts_dict = get_all

# Generated at 2022-06-13 00:29:17.082644
# Unit test for function get_all_facts
def test_get_all_facts():

    from ansible.module_utils.facts import ansible_facts
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils.facts import ansible_collector

    class FakeModule(object):
        def __init__(self, gather_subset):
            self.params = {'gather_subset': gather_subset, 'gather_timeout': 10}

    module = FakeModule(['all'])

    facts_dict = ansible_facts(module)

    assert facts_dict['architecture'] == 'x86_64'


# Generated at 2022-06-13 00:29:23.016114
# Unit test for function ansible_facts
def test_ansible_facts():

    from collections import namedtuple
    AnsibleModule = namedtuple('AnsibleModule', ('params',))

    module = AnsibleModule(params={})

    facts_dict = ansible_facts(module)
    expected_dict = {}

    assert facts_dict == expected_dict



# Generated at 2022-06-13 00:29:48.989145
# Unit test for function ansible_facts
def test_ansible_facts():

    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.facts import default_collectors

    class FakeModule(AnsibleModule):
        def get_bin_path(self, arg, required=False, opt_dirs=[]):
            return None

        def get_platform(self):
            return 'linux'

        def get_distribution(self):
            return 'FooOS'

    module = FakeModule({})

    facts = ansible_facts(module)

    # Expect facts to be a dict with at least keys 'ansible_date_time' and 'ansible_local'
    assert isinstance(facts, dict), "facts is not a dict, but %s" % type(facts)

# Generated at 2022-06-13 00:29:59.668026
# Unit test for function ansible_facts
def test_ansible_facts():
    'Test the ansible_facts function in module_utils.facts'
    import json
    import unittest
    from ansible.module_utils import facts as facts_consolidation

    class TestAnsibleModule(object):
        'A dummy AnsibleModule class to pass to ansible_facts'
        class ArgumentSpec(object):
            def __init__(self):
                self.args = {}
        class SupportModuleDeprecationWarning(object):
            def __init__(self):
                self.messages = []
            def warn(self, msg):
                self.messages.append(msg)
        def __init__(self):
            self.params = {}
            self.argument_spec = TestAnsibleModule.ArgumentSpec()
            self.deprecations = TestAnsibleModule.SupportModuleDeprecationWarning()

# Generated at 2022-06-13 00:30:11.814550
# Unit test for function ansible_facts
def test_ansible_facts():
    import json
    import sys

    import ansible.module_utils.facts.network as network_facts
    import ansible.module_utils.facts.system as system_facts

    system_facts_collector_classes = {
        'default': system_facts.SystemFacts,
        'hardware': system_facts.Hardware,
        'virtual': system_facts.Virtual,
        'network': network_facts.Network,
    }

    class MockAnsibleModule:
        def __init__(self, params):
            self.params = params

    # Simple test
    params = {'filter': 'ansible_default_ipv4.address'}
    module = MockAnsibleModule(params)
    ansible_facts_by_collector_class = ansible_facts(module)
    assert ansible_facts_by_

# Generated at 2022-06-13 00:30:22.652658
# Unit test for function get_all_facts
def test_get_all_facts():
    import pytest
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(argument_spec=dict(gather_subset=dict(default='all', required=False)))
    facts = get_all_facts(module)
    assert facts is not None
    assert len(facts) > 1
    for fact in facts.keys():
        assert fact.startswith('ansible_')

    module = AnsibleModule(argument_spec=dict(gather_subset=dict(default='all', required=False)))
    facts = ansible_facts(module)
    assert facts is not None
    assert len(facts) > 1
    for fact in facts.keys():
        assert fact.startswith('ansible_')

# Generated at 2022-06-13 00:30:33.773391
# Unit test for function ansible_facts
def test_ansible_facts():
    import unittest
    import mock

    class DummyModule(object):
        def __init__(self, params):
            self.params = params

    class TestAnsibleFacts(unittest.TestCase):
        @mock.patch('ansible.module_utils.facts.default_collectors.collectors')
        @mock.patch('ansible.module_utils.facts.ansible_collector.get_ansible_collector')
        def test_ansible_facts(self, mock_ansible_collector, mock_default_collectors):
            mock_fact_collector = mock.MagicMock()

            mock_ansible_collector.return_value = mock_fact_collector

            dummy_params = {'gather_subset': ['all']}

            expected_all_collector_classes

# Generated at 2022-06-13 00:30:39.964664
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils.facts.collector import AnsibleModule as AM
    m = AM(argument_spec={'gather_subset': {'type': 'list'}})
    m.params['gather_subset'] = 'hardware'
    facts_dict = get_all_facts(m)
    assert 'default_ipv4' in facts_dict.keys()
    assert 'distribution' in facts_dict.keys()
    assert 'default_ipv4' in facts_dict.keys()

# Generated at 2022-06-13 00:30:48.138969
# Unit test for function ansible_facts
def test_ansible_facts():
    import json
    import socket
    from ansible.module_utils.facts import ansible_facts

    module = MockModule()

    # get_all_facts returns a dict
    assert ansible_facts.ansible_facts(module)

    # get_all_facts() return dict is dict-like
    # It should have a __getitem__ method
    assert ansible_facts.ansible_facts(module).__getitem__

    # get_all_facts() return dict should have some values
    # test machine has an ip address
    assert ansible_facts.ansible_facts(module)['default_ipv4']['address']



# Generated at 2022-06-13 00:30:57.387390
# Unit test for function get_all_facts
def test_get_all_facts():

    from ansible.module_utils.facts.utils import AnsibleModule, get_module_path
    from ansible.module_utils.facts import default_collectors

    class AnsibleModuleForTesting(AnsibleModule):
        def __init__(self):
            self.params = {
                'gather_subset': ['all'],
                'gather_timeout': 10,
                'filter': '*'
            }

    module = AnsibleModuleForTesting()
    facts_dict = get_all_facts(module=module)

    assert type(facts_dict) is dict

    # The 'ephemeral_storage_interested' fact should be present in returned dictionary.
    assert 'ephemeral_storage_interested' in facts_dict
    assert type(facts_dict['ephemeral_storage_interested']) is bool

    #

# Generated at 2022-06-13 00:31:08.768198
# Unit test for function ansible_facts
def test_ansible_facts():
    # just test that module can be imported and the 'ansible_facts' function exists.
    from ansible.module_utils import basic
    from ansible.module_utils.facts import ansible_fact_definitions
    from ansible.module_utils.facts.namespace import PrefixFactNamespace

    module = basic.AnsibleModule(argument_spec=dict(
        gather_subset=dict(type='list', elements='str', default=None),
        gather_timeout=dict(type='int', default=None)
    ))

    facts_dict = ansible_facts(module)

    assert isinstance(facts_dict, dict)

    assert 'gather_subset' in facts_dict
    assert 'gather_timeout' in facts_dict

    for fact_name in facts_dict:
        assert fact_name in ansible

# Generated at 2022-06-13 00:31:16.203889
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils.facts import MagicMock
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts import default_collectors

    module = MagicMock()
    module.params = { 'gather_subset': ['all'] }

    prefix_fact_namespace = PrefixFactNamespace(namespace_name='ansible', prefix='')
    test_collectors = default_collectors.collectors

# Generated at 2022-06-13 00:31:57.584393
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts.collector import TestCollectedFact
    from ansible.module_utils.facts import TestCollector

    class TestCollector1(TestCollector):
        pass

    class TestCollector2(TestCollector):
        pass

    facts_dict = ansible_facts(module=None, gather_subset=None)

    assert type(facts_dict) is dict
    assert 'test_collected_fact' in facts_dict
    assert type(facts_dict['test_collected_fact']) is TestCollectedFact
    assert facts_dict['test_collected_fact'].namespace == 'ansible'
    assert facts_dict['test_collected_fact'].name == 'test_collected_fact'

# Generated at 2022-06-13 00:32:05.743048
# Unit test for function get_all_facts
def test_get_all_facts():
    class FakeAnsibleModule(object):
        def __init__(self, gather_subset):
            self.params = {}
            self.params['gather_subset'] = gather_subset

    # The facts will vary depending on the host.
    # So just check that we get back a dict-like object for the key
    # 'ansible_default_ipv4'
    gather_subset = ['all']
    ansibleModule = FakeAnsibleModule(gather_subset)
    factsDict = get_all_facts(ansibleModule)

    assert isinstance(factsDict['ansible_default_ipv4'], dict)

# Generated at 2022-06-13 00:32:09.605110
# Unit test for function ansible_facts
def test_ansible_facts():
    # This is unit test of function 'ansible_facts' which is compatible with ansible 2.0 and 2.3.
    # It verifies that facts are collected as expected when provided with
    # gather_subset=all and gather_subset=minimal.
    # This test also verifies that facts are filtered based on the filter_spec passed in.

    # Import modules used by the unit test.
    import ansible.modules.system.setup as setup_mod
    import ansible.module_utils.basic as basic_mod
    basic_mod.ANSIBLE_VERSION = "2.3"

    # Define bare_minimum subset of facts to collect.
    minimal_subset = ['ansible_lsb']

    # Define args to be passed to ansible_facts.

# Generated at 2022-06-13 00:32:18.911657
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts.facts import Facts
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.collector import NetworkCollector
    from ansible.module_utils.facts.collector import HardwareCollector
    from ansible.module_utils.facts.collector import DefaultCollector

    import os
    import stat

    import pytest

    class NoneFactCollector(BaseFactCollector):
        def __init__(self, *args, **kwargs):
            super(NoneFactCollector, self).__init__(*args, **kwargs)
            self.boot_timestamp = os.stat('/proc/1/exe').st_mtime


# Generated at 2022-06-13 00:32:27.222799
# Unit test for function ansible_facts
def test_ansible_facts():
    import ansible.module_utils.facts.namespace as amu
    import ansible.module_utils.facts.collector as ac
    import mock

    with mock.patch('ansible.module_utils.facts.namespace.PrefixFactNamespace') as mock_namespace:
        module = mock.MagicMock(name='module')
        mock_namespace.return_value = 'namespace'
        with mock.patch('ansible.module_utils.facts.collector.get_ansible_collector') as mock_collector:
            mock_collector.return_value = 'collector'
            with mock.patch('ansible.module_utils.facts.ansible_collector.AnsibleCollector') as mock_ansible_collector:
                ansible_facts(module)
                assert mock_namespace.call

# Generated at 2022-06-13 00:32:36.990639
# Unit test for function ansible_facts
def test_ansible_facts():
    import sys
    import os
    import yaml

    # when run as unit test, the current working directory is the python directory,
    # so do an absolute path to the test directory
    testfile_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'test_data', 'unit', 'module_utils', 'facts')

    # Note that this could be captured from the gather_subset param in the playbook.
    # In a unit test, I will define it here.
    gather_subset = ['!all', '!network']

    class MockModule:
        def __init__(self):
            self.params = {}
            self.params['filter'] = 'ansible_distribution_version'

    m = MockModule()

# Generated at 2022-06-13 00:32:45.995838
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts import get_all_facts
    from ansible.module_utils._text import to_text

    class FakeAnsibleModule(object):
        def __init__(self, params):
            self.params = params

    # gather all facts, without providing a gather_subset
    module = FakeAnsibleModule(params={})
    all_facts = ansible_facts(module)
    assert 'ansible_lsb' in all_facts

    # gather all facts, by explicitly providing a gather_subset=all
    module = FakeAnsibleModule(params={'gather_subset': [all]})
    all_facts = ansible_facts(module)
    assert 'ansible_lsb' in all_facts

    # gather only the minimal set of facts, by providing gather_subset=

# Generated at 2022-06-13 00:32:48.719151
# Unit test for function ansible_facts
def test_ansible_facts():
    import pytest

    module_mock = None
    gather_subset = ['all']
    ansible_facts(module=module_mock, gather_subset=gather_subset)
    # Make sure we don't fail without a gather_subset arg
    ansible_facts(module=module_mock)
    with pytest.raises(TypeError):
        ansible_facts()

# Generated at 2022-06-13 00:33:00.867697
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils._text import to_native, to_text
    from ansible.module_utils.facts.facts import ansible_local
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts import namespace
    import os

    class MockModule(object):
        def __init__(self):
            self.params = {
                'gather_subset': ['all']
            }
    class MockCollector(BaseFactCollector):
        def collect(self, module=None, collected_facts=None):
            return {
                'mock': 'mock_ansible_module_get_all_facts_unit_test'
            }
    class MockNamespace(namespace.Namespace):
        def __init__(self):
            self.fact

# Generated at 2022-06-13 00:33:11.543310
# Unit test for function ansible_facts
def test_ansible_facts():
    try:
        # Import module_utils/ansible which is the minimal amount of code needed to mock
        # a module object.
        from ansible.module_utils.ansible_release import __version__ as ansible_version
        from ansible.module_utils.ansible_release import __version_info__ as ansible_version_info
        from ansible.module_utils.facts import DEFAULT_GATHER_SUBSET
    except ImportError:
        import sys
        sys.stderr.write("ERROR: failed to import ansible.module_utils.ansible_release.\n")
        sys.stderr.write("ERROR: could not import test_ansible_facts()\n")
        raise

    ansible_major_version = ansible_version_info[0]

    # fake_ansible_module is needed to