

# Generated at 2022-06-13 00:24:18.591466
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils.facts.__init__ import get_all_facts

    import sys
    import unittest

    class MockModule(object):
        def __init__(self, gather_subset):
            self.params = dict()
            self.params['gather_subset'] = gather_subset

    class MockAnsibleModule(object):
        def __init__(self, gather_subset):
            self.params = dict()
            self.params['gather_subset'] = gather_subset

    # test for ansible 2.4.x/2.3/2.2 fallback
    sys.modules['ansible'] = None
    class TestGetAllFactsAnsible24(unittest.TestCase):
        def test_get_all_facts(self):
            gather_subset

# Generated at 2022-06-13 00:24:29.076472
# Unit test for function ansible_facts
def test_ansible_facts():

    import os
    import json

    all_collector_classes = default_collectors.collectors

    # don't add a prefix
    namespace = PrefixFactNamespace(namespace_name='', prefix='')

    fact_collector = \
        ansible_collector.get_ansible_collector(all_collector_classes=all_collector_classes,
                                                namespace=namespace,
                                                filter_spec='default_ipv4',
                                                gather_subset=['all'],
                                                gather_timeout=10,
                                                minimal_gather_subset=None)

    facts_dict = fact_collector.collect()

    assert 'default_ipv4' in facts_dict, facts_dict
    assert 'default_ipv6' not in facts_dict, facts_dict

# Generated at 2022-06-13 00:24:36.915724
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts.collector import BaseFactCollector
    import ansible.module_utils.facts.system.distribution
    from ansible.module_utils.basic import AnsibleModule, env_fallback

    # The BaseFactCollector.__init__ requires 'all_collectors' to be an ordered dict
    class FakeOrderedDict(dict):
        def __init__(self, *args, **kwargs):
            self.ordered = True

            super(FakeOrderedDict, self).__init__(*args, **kwargs)

    class FakeDict(dict):
        def __init__(self, *args, **kwargs):
            self.ordered = False
            super(FakeDict, self).__init__(*args, **kwargs)


# Generated at 2022-06-13 00:24:45.349108
# Unit test for function ansible_facts
def test_ansible_facts():

    class TestAnsibleModule(object):
        def __init__(self, params):
            self.params = params
            self.fail_json = self.exit_json

        def exit_json(self, *args, **kwargs):
            pass

    # Expects to find test_collector_class in the test/unit/plugins/collector/test_test_plugin.py file
    # module_utils.facts.ansible_collector is used for unit testing for this module
    # since it is not available to the module when running in unit test mode.
    # The function get_ansible_collector() and the class AnsibleFactsCollector from this module
    # are mocked and the class must be implemented in the test/unit/plugins/collector/test_test_plugin.py file

# Generated at 2022-06-13 00:24:55.899366
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts import ansible_facts
    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.collector import TestTrueFactCollector
    from ansible.module_utils.facts.collector import TestFalseFactCollector

    class TestCollector(BaseFactCollector):
        def collect(self, module=None, collected_facts=None):
            return {'test': True}

    class BadCollector(BaseFactCollector):
        def collect(self, module=None, collected_facts=None):
            return {'test': False}


# Generated at 2022-06-13 00:25:02.966734
# Unit test for function get_all_facts
def test_get_all_facts():
    # test_module_data is defined in the helper method test_module
    test_gather_subset = test_module_data.get('gather_subset')
    test_facts = get_all_facts(test_module)
    assert (test_facts['ansible_all_ipv4_addresses'] is not None)
    assert (set(test_facts.keys()) == set(test_gather_subset))



# Generated at 2022-06-13 00:25:10.479323
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils import basic

    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils.facts import ansible_collector

    from ansible.module_utils.facts.sysinfo.bsd import BsdSysInfo


# Generated at 2022-06-13 00:25:20.517803
# Unit test for function get_all_facts
def test_get_all_facts():
    import json
    import os
    import tempfile
    import unittest

    # test module source code
    TEST_MODULE_SOURCE_CODE = '''
#!/usr/bin/python

from ansible.module_utils.basic import *
from ansible.module_utils.facts import *

ansible_facts = get_all_facts(module)

try:
    # ansible 2.3/2.4 module_utils.facts.ansible_facts method exists
    ansible_facts = ansible_facts(module)
except Exception as e:
    # ansible 2.0/2.2 module_utils.facts.get_all_facts method exists
    ansible_facts = ansible_facts

module.exit_json(changed=False, ansible_facts=ansible_facts)
'''


# Generated at 2022-06-13 00:25:29.779867
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts import get_collector

    # we don't want to actually print to stdout, want to capture it
    import sys
    try:
        from cStringIO import StringIO
    except ImportError:
        from io import StringIO

    stdout = sys.stdout
    captured_stdout = None

    # This simulates the desired behavior of ansible to inject a new
    # parameter "myparam" into the module args.
    # This is not available in the current version of the Python module
    # template, so we have to fake this by monkey patching the module_args
    # param.  This is why we are using a class below instead of a dict as
    # would normally be done.


# Generated at 2022-06-13 00:25:35.949334
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts.user import User

    module = MockAnsibleModule()

    gathered_facts = ansible_facts(module)

    # Specific value check
    assert gathered_facts['version']['full'] == '2.3.1.0'

    # Specific class check
    assert isinstance(gathered_facts['user'], User)

# Generated at 2022-06-13 00:25:46.705826
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts.utils import FactsCache
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.basic import AnsibleModule, ModuleDeprecationWarning
    import sys
    if sys.version_info[0] < 3:
        from io import BytesIO
    else:
        from io import BytesIO, StringIO


    class MockAnsibleModule:
        '''Mock class for AnsibleModule'''
        def __init__(self, gather_timeout=10):
            self.params = {'gather_timeout': gather_timeout}
            self.warnings = []
            self._warnings = []

        def _load_params(self):
            pass

        def module_deprecation(self):
            pass


# Generated at 2022-06-13 00:25:57.360102
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils import facts

    # fake params
    module_params = {
        'filter': '*',
    }

    # make a fake module with the above params
    module = AnsibleModule(argument_spec=dict(), supports_check_mode=True)
    module.params = module_params

    # collect facts
    facts_dict = facts.ansible_facts(module)

    assert facts_dict is not None

    # check that the dict contains facts
    # TODO: make this more dynamic, maybe we can't guarantee the content of the fact dict
    assert 'uptime_seconds' in facts_dict



# Generated at 2022-06-13 00:26:07.842629
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts import ansible_collector

    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils.facts.virtual import BaseVirtual
    from ansible.module_utils.facts.collector import BaseFactCollector

    class MockModule(object):
        def __init__(self, params):
            self.params = params

    class MockNamespace(object):
        def __init__(self, namespace_name, prefix):
            self.namespace_name = namespace_name
            self.prefix = prefix


# Generated at 2022-06-13 00:26:18.808846
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts import ansible_facts
    import ansible.module_utils.facts.namespace as namespace_mod

    #unit test stub
    class StubModule(object):
        def __init__(self, params):
            self._params = params

        def params(self):
            return self._params

    # set up a minimal namespace, with a single namespace 'ansible' that has a single fact 'foo'
    @namespace_mod.NamespaceFactCollector('ansible', '',
                                          [namespace_mod.NamespaceKey('foo', False)])
    class StubFactsNamespace(object):
        def __init__(self, module):
            self._module = module

        def populate(self):
            return {'foo': 'bar'}

    # set up a module with config to collect

# Generated at 2022-06-13 00:26:24.066858
# Unit test for function ansible_facts
def test_ansible_facts():
    # test_ansible_facts requires the module_utils.ansible.module_utils.basic.AnsibleModule function
    # to be available. It is in the ansible.module_utils.basic module, so ansible.module_utils
    # should be available prior to running test_ansible_facts.
    #
    # This function is also called from test_ansible_facts in the test/unit/module_utils/network/nxos/test_facts.py
    # file
    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils.facts import ansible_collector

    # we will use os.path and platform modules for testing
    import os
    import platform

    # This is a utility function from the ansible.module_utils.facts.default_collectors module
    # The code

# Generated at 2022-06-13 00:26:32.069243
# Unit test for function ansible_facts
def test_ansible_facts():
    try:
        from ansible.module_utils.facts import __v2_2__ as facts_v2_2
        assert ansible_facts == facts_v2_2.ansible_facts
    except ImportError:
        try:
            from ansible.module_utils.facts import __v2_0__ as facts_v2_0
            assert ansible_facts == facts_v2_0.ansible_facts
        except ImportError:
            pass # ansible > 2.2


# Generated at 2022-06-13 00:26:42.514685
# Unit test for function ansible_facts
def test_ansible_facts():
    import ansible.module_utils.facts
    from ansible.module_utils.facts import default_collectors
    import ansible.module_utils.facts.ansible_collector
    import ansible.module_utils.facts.namespace
    import ansible.module_utils.facts.processors
    import ansible.module_utils.facts.system

    import ansible.module_utils.facts.hardware
    import ansible.module_utils.facts.network
    import ansible.module_utils.facts.other
    import ansible.module_utils.facts.software

    class Module(object):
        def __init__(self, gather_subset=None, gather_timeout=None, filter=None):
            self.params = {}
            if gather_subset:
                self.params['gather_subset'] = gather

# Generated at 2022-06-13 00:26:50.901182
# Unit test for function ansible_facts
def test_ansible_facts():
    '''Unit test to check basic functionality of ansible_facts function'''

    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(
        argument_spec={},
        supports_check_mode=True
    )

    # Enable tracing, it will cause fact collection
    # to be visible in debug output
    module.debug("STARTING unit test of ansible_facts()")

    facts = ansible_facts(module=module, gather_subset=['all'])

    module.debug("ENDING unit test of ansible_facts()")
    module.exit_json(changed=False, ansible_facts=facts)

# Generated at 2022-06-13 00:26:57.597665
# Unit test for function ansible_facts
def test_ansible_facts():

    import ansible.module_utils.facts.legacy

    class FakeModule:
        class FakeParams:
            def __init__(self):
                self.get_return_value = None

            def get(self, key, default):
                return self.get_return_value or default

        def __init__(self):
            self.fail_json_called = False
            self.fail_json_args = None
            self.params = self.FakeParams()

        def fail_json(self, *args, **kwargs):
            self.fail_json_args = args, kwargs
            self.fail_json_called = True

    m = FakeModule()

    ansible_facts(module=m)

    assert not m.fail_json_called
    assert m.params.get_return_value is None

   

# Generated at 2022-06-13 00:27:00.656584
# Unit test for function ansible_facts
def test_ansible_facts():
    module = FakeAnsibleModule(params={'filter': '*',
                                       'gather_subset': ['all']})

    facts = ansible_facts(module=module)

    assert facts['distribution'].lower() == 'unknown'



# Generated at 2022-06-13 00:27:13.713524
# Unit test for function ansible_facts
def test_ansible_facts():
    '''Test function ansible_facts'''

    import ansible.module_utils.facts.platform

    # first we must have a AnsibleModule
    # Create a test class
    class TestAnsibleModule():
        def __init__(self, params):
            self.params = params

        def warn(self, warning):
            '''Placeholder for AnsibleModule.warn'''
            pass

    # Create a test module
    module = TestAnsibleModule({'gather_subset': ['all']})

    # Find a valid fact to test with
    chosen_fact = None
    for fact in ansible.module_utils.facts.platform.FACTS:
        if fact.COLLECTORS:
            chosen_fact = fact
            break

    # Do the test against the fact

# Generated at 2022-06-13 00:27:25.013511
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils.facts import ansible_facts

    class Module(object):
        def __init__(self, gather_subset):
            self.params = dict(gather_subset=gather_subset)

    # test collect everything
    module = Module(['all'])
    facts = get_all_facts(module)
    assert 'ansible_facts' in facts
    assert 'ansible_env' in facts['ansible_facts']
    assert 'ansible_architecture' in facts['ansible_facts']

    # test collect nothing
    module = Module(['!all'])
    facts = get_all_facts(module)
    assert 'ansible_facts' in facts
    assert 'ansible_env' not in facts['ansible_facts']

# Generated at 2022-06-13 00:27:33.189593
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts import ansible_facts
    from ansible.module_utils.basic import AnsibleModule

    from ansible.module_utils._text import to_native

    module = AnsibleModule(
        argument_spec=dict(
            gather_subset=dict(default=None, type='list'),
            gather_timeout=dict(default=10, type='int'),
            filter=dict(default='*', type='str'),
        ),
        supports_check_mode=False,
        check_invalid_arguments=False,
    )

    # Set up some fake 'facts' that we can check to see if the collector gets them
    module.params['module_setup'] = True
    # set some facts that we can use to check the output of ansible_facts()

# Generated at 2022-06-13 00:27:33.754669
# Unit test for function get_all_facts
def test_get_all_facts():
    pass

# Generated at 2022-06-13 00:27:47.131288
# Unit test for function get_all_facts
def test_get_all_facts():
    import mock
    module_return_facts = {'facts': {'default_ipv4': {'address': '172.18.0.2', 'netmask': '255.255.255.0', 'network': '172.18.0.0', 'broadcast': '172.18.0.255', 'interface': 'eth0', 'gateway': '172.18.0.1', 'macaddress': '02:42:ac:12:00:02', 'type': 'ipv4'}}}

# Generated at 2022-06-13 00:27:51.015306
# Unit test for function get_all_facts
def test_get_all_facts():
    import ansible.modules.system.setup as setup

    args = {'gather_subset': 'all'}
    module = setup.AnsibleModule(args=args)

    facts = get_all_facts(module)

    assert isinstance(facts, dict)
    assert 'ansible_' in facts.keys()[0]



# Generated at 2022-06-13 00:27:59.873809
# Unit test for function get_all_facts
def test_get_all_facts():
    import ansible.module_utils.facts.platform as platform
    import ansible.module_utils.facts.distribution as distribution
    import ansible.module_utils.facts.system as system
    import ansible.module_utils.facts.network as network
    import ansible.module_utils.facts.pkg_mgr as pkg_mgr

    class MockModule(object):
        def __init__(self, params, facts=None):
            self.params = params
            self.facts = {}
            if facts:
                self.facts.update(facts)

        def fail_json(self, **kwargs):
            class MockFailJson(object):
                def __init__(self, module, **kwargs):
                    self.msg = kwargs.get('msg', '')

# Generated at 2022-06-13 00:28:08.823334
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts import DEFAULT_GATHER_SUBSET
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.basic import AnsibleModule

    def get_ansible_module_mock(params):
        return AnsibleModule(argument_spec={'gather_subset': dict(type='list', elements='str',
                                                                  default=DEFAULT_GATHER_SUBSET),
                                            'gather_timeout': dict(type='int', default=10),
                                            'filter': dict(type='str', default=u'*')},
                             params=params)

    # test calling ansible_facts with no gather_subset param (i.e. ansible 2.0/2.1) usage
    module = get_ansible_module

# Generated at 2022-06-13 00:28:16.429178
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts import Facts

    initial_collectors = Facts.all_collectors
    try:
        Facts.all_collectors = default_collectors.collectors
        # Test a case that should return no facts
        facts = ansible_facts(module=None, gather_subset=['foo'])
        assert facts == {}

        # Test a real subset
        facts = ansible_facts(module=None, gather_subset=['min'])
        assert facts
    finally:
        Facts.all_collectors = initial_collectors

# Generated at 2022-06-13 00:28:22.380958
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts import ansible_facts
    result = ansible_facts(None, gather_subset=['!all', 'hardware', 'network', 'virtual'])
    assert 'ansible_os' not in result
    assert 'ansible_os_family' not in result
    assert 'ansible_system' not in result
    assert 'ansible_virtualization_role' not in result

# Generated at 2022-06-13 00:28:33.915565
# Unit test for function ansible_facts
def test_ansible_facts():

    # pretend that AnsibleModule is the version of AnsibleModule that exists in Ansible 2.2
    # see https://github.com/ansible/ansible/blob/stable-2.2/lib/ansible/module_utils/basic.py
    class AnsibleModule(object):
        '''Mock AnsibleModule for testing'''
        def __init__(self, args):
            self.params = args

    # Setup test arguments for module under test
    params = dict(
        gather_subset=['network'],
        gather_timeout=10,
    )

    module = AnsibleModule(params)

    # execute the tested function
    facts_dict = ansible_facts(module=module, gather_subset=module.params['gather_subset'])

    # make sure that the facts_dict has network facts


# Generated at 2022-06-13 00:28:38.675392
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts import get_all_facts
    from ansible.module_utils.facts import ansible_facts

    ansible_facts_dict = ansible_facts({})
    get_all_facts_dict = get_all_facts({})

    assert ansible_facts_dict == get_all_facts_dict

# Generated at 2022-06-13 00:28:50.266919
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.compat.tests import unittest
    from ansible.compat.tests.mock import Mock, patch

    class AnsibleModule(object):
        def __init__(self):
            self.params = {'gather_subset': ['all'], 'gather_timeout': 10}

    # 2.3/2.4 modules get pass in a gather_subset list
    with patch('ansible_collections.ansible.distribution.plugins.modules.os_facts.ansible_collector.get_ansible_collector') as get_collector:
        get_collector.return_value = Mock(collect=lambda: {'foo': 'bar'})
        subsets = ['all']

# Generated at 2022-06-13 00:28:52.101243
# Unit test for function ansible_facts
def test_ansible_facts():
    assert ansible_facts(None) == {}
    assert ansible_facts(None, gather_subset=None) == {}

# Generated at 2022-06-13 00:29:00.060226
# Unit test for function ansible_facts
def test_ansible_facts():
    import os
    import tempfile
    import pytest

    os_path = os.path
    import ansible.module_utils.facts

    # Python 2/3 compat: os is a top-level module only in Python 3
    if not hasattr(os, 'path'):
        os.path = os_path

    # Create a fake AnsibleModule instance for the test
    import ansible.module_utils.facts.namespace
    import ansible.module_utils.facts.default_collectors
    import ansible.module_utils.facts.ansible_collector

    class FakeAnsibleModule(object):
        def __init__(self, params=None):
            params = params or {}
            self.params = params


# Generated at 2022-06-13 00:29:00.658285
# Unit test for function get_all_facts
def test_get_all_facts():
    pass

# Generated at 2022-06-13 00:29:09.097492
# Unit test for function get_all_facts
def test_get_all_facts():
    '''unit test for get_all_facts'''
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils.facts import ansible_collector

    all_collector_classes = default_collectors.collectors

    # don't add a prefix
    namespace = PrefixFactNamespace(namespace_name='ansible', prefix='')

    class FakeModule(object):
        '''fake module class'''

        def __init__(self):
            self.params = {'gather_subset': ['all']}

        def fail_json(self, *args, **kwargs):
            pass

    fake_module = FakeModule()

    gather_subset = ['all']
    gather_timeout

# Generated at 2022-06-13 00:29:17.698080
# Unit test for function ansible_facts
def test_ansible_facts():
    '''Unit test for function ansible_facts

    runs an end-to-end test of the ansible_facts() function'''
    from ansible.module_utils.facts.ansible_facts import ansible_collector
    from ansible.module_utils.facts.distribution.linux.redhat import LinuxDistributionRedHat
    from ansible.module_utils.basic import AnsibleModule

    test_module = AnsibleModule(argument_spec={'gather_subset': dict(default=['all'], type='list')})
    test_module.params['gather_subset'] = ['all']

    # Mock the ansible_collector.get_ansible_collector() method
    old_get_ansible_col = ansible_collector.get_ansible_collector

# Generated at 2022-06-13 00:29:27.583782
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(argument_spec=dict(gather_subset=dict(default=['all'], type='list')))
    # fake the module params
    module.params = dict(gather_subset=['!any'])
    facts = ansible_facts(module)
    assert facts['version'] == '2.0'
    assert to_bytes(facts['default_ipv4']['address']) == b'127.0.0.1'
    assert facts['local']['site']['facts_loaded']
    assert not facts['virtualization']['facts_loaded']

# Generated at 2022-06-13 00:29:30.384466
# Unit test for function get_all_facts
def test_get_all_facts():
    import inspect
    from ansible.module_utils.facts import get_all_facts
    assert inspect.isfunction(get_all_facts)


# Generated at 2022-06-13 00:29:56.693487
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils._text import to_text
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.namespace import BaseFactNamespace
    from ansible.module_utils.facts import default_collectors

    class FakeAnsibleModule(object):
        params = {
            'gather_subset': '!all',
            'minimal': True,
        }
        def __init__(self, module_name=''):
            self.module_name = module_name
            self.changed = False
            self.fail_json = lambda x: None

    class FakeBaseFactCollector(BaseFactCollector):
        COLLECTOR_NAME = 'fake'


# Generated at 2022-06-13 00:29:59.383615
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule({'gather_subset': ['all']})

    assert get_all_facts(module) == ansible_facts(module, gather_subset=['all'])

# Generated at 2022-06-13 00:30:11.633773
# Unit test for function ansible_facts
def test_ansible_facts():
    class FakeAnsibleModule(object):
        def __init__(self, gather_subset, gather_timeout, filter):
            self.params = {'gather_subset': gather_subset, 'gather_timeout': gather_timeout, 'filter': filter}

    mod = FakeAnsibleModule(gather_subset=['all'], gather_timeout=20, filter=('*', '!ansible_fqdn,!ansible_mounts'))
    fake_facts_dict = ansible_facts(module=mod)
    # The fake facts dict should have some facts
    assert fake_facts_dict
    # there should only be two key/value pairs in this fact list, ansible_fqdn and ansible_mounts should not be there
    assert len(fake_facts_dict) == 2

    # Now test

# Generated at 2022-06-13 00:30:23.214150
# Unit test for function ansible_facts
def test_ansible_facts():

    class MockModule(object):
        def __init__(self, params):
            self.params = params
            self.fail_json = False

    default_params = {'gather_timeout': 10, 'filter': '*'}

    # test just the default collectors
    params = default_params.copy()
    m = MockModule(params)
    facts_dict = ansible_facts(m)
    assert 'uptime' in facts_dict
    assert 'uptime_seconds' in facts_dict

    # test that minimal_gather_subset works
    params = default_params.copy()
    params['gather_subset'] = ['fake']
    m = MockModule(params)
    facts_dict = ansible_facts(m)
    assert 'uptime' in facts_dict
    assert 'uptime_seconds'

# Generated at 2022-06-13 00:30:26.371146
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts import ansible_facts

    assert len(ansible_facts(None).keys()) > 0

# Generated at 2022-06-13 00:30:33.050878
# Unit test for function get_all_facts
def test_get_all_facts():
    '''test the get_all_facts function'''

    class ModuleMock(object):
        '''mock object to simulate an ansible module'''

        def __init__(self, params):
            '''initialize the mock object'''
            self.params = params

    module_mock = ModuleMock({'gather_subset': ['all']})
    ansible_facts = get_all_facts(module_mock)

    assert 'default_ipv4' in ansible_facts

# Generated at 2022-06-13 00:30:42.752838
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.ansible_collector import AnsibleCollector
    from ansible.module_utils.facts.default_collectors import DefaultCollector

    class FakeModule:
        def __init__(self, gather_subset):
            self.params = {
                'gather_subset': gather_subset,
            }


# Generated at 2022-06-13 00:30:48.605484
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts import socket
    from ansible.module_utils.facts import osfamily
    from ansible.module_utils.facts import lsb
    from ansible.module_utils.facts import selinux
    from ansible.module_utils.facts import cmdline
    from ansible.module_utils.facts import distribution
    from ansible.module_utils.facts import network
    from ansible.module_utils.facts import user

# Generated at 2022-06-13 00:30:51.613417
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils.facts import ansible_facts
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    prefix_fact_namespace = PrefixFactNamespace(namespace_name='ansible_facts', prefix='')
    fact_collector = ansible_facts.get_ansible_collect(gather_subset=None)
    fact_collector.add_namespace(prefix_fact_namespace)
    fact_collector.collect(module=AnsibleModule(argument_spec=dict()))

# Generated at 2022-06-13 00:30:58.075518
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils.facts import get_all_facts

    def mock_module_params(params):
        class MockModule:
            def __init__(self, params):
                self.params = params
        return MockModule(params)

    gather_subset_params = {'gather_subset': ['all', 'network']}
    gather_timeout_params = {'gather_timeout': 10}
    filter_params = {'filter': '*'}
    module = mock_module_params({'gather_subset': ['all', 'network'], 'gather_timeout': 5})

    facts = get_all_facts(module)
    assert facts['hostname'] == 'localhost'

# Generated at 2022-06-13 00:31:35.417000
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts import ansible_facts

    # Sometimes you'd want to test a function that expects an ansible module,
    # but you might not actually want to make a real api call to a real device.
    # To do that you need to make a fake ansible module, that mocks out all the
    # api calls.

    # have ansible facts default to gather everything
    class FakeAnsibleModule():
        def __init__(self, **kwargs):
            self.params = {
                'gather_subset': ['all'],
                'gather_timeout': 10,
                'filter': '*'
            }

    # create an instance of our fake ansible module
    fake_ansible_module = FakeAnsibleModule()

    # get ansible facts
    ansible_facts_results = ans

# Generated at 2022-06-13 00:31:41.995923
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(
        argument_spec=dict(
            gather_subset=dict(default=None, type='list'),
        ),
    )
    module.params = dict(gather_subset=['all'])
    fact_dict = get_all_facts(module)
    assert fact_dict['distribution'] == 'Darwin'

# Generated at 2022-06-13 00:31:53.334542
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils.facts import ansible_collector
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils._text import to_bytes

    # Mock AnsibleModule class
    class AnsibleModuleMock(object):

        def __init__(self, *args, **kwargs):
            pass

        def params(self):
            return {'gather_subset': ['all'],
                    'gather_timeout': 10,
                    'filter': '*'}

        def fail_json(self, *args, **kwargs):
            return None

    # Mock collector class

# Generated at 2022-06-13 00:32:00.007748
# Unit test for function ansible_facts
def test_ansible_facts():
    import pytest
    from ansible.module_utils.facts import ansible_facts
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts.utils import legacy_facts

    class AnsibleModuleMock:
        '''Mock AnsibleModule'''
        def __init__(self):
            self.params = dict()
            self.fail_json = dict()

    module = AnsibleModuleMock()

    # test with empty gather_subset
    module.params['gather_subset'] = []
    facts_dict = ansible_facts(module)
    assert facts_dict == dict(), 'empty gather_subset should return empty dict'

    # test with incorrect gather_subset

# Generated at 2022-06-13 00:32:05.979526
# Unit test for function ansible_facts
def test_ansible_facts():
    module = dict(
        gather_subset=['all'],
        gather_timeout=10,
        filter='*',
        params=dict(
            gather_subset=['all']
        )
    )
    result = ansible_facts(module=module)
    assert result is not None
    assert result['lsb']['description'][:4] == 'Ubuntu'
    assert result['kernel'] == result['kernel_version']
    assert 'ansible_version' in result


# Generated at 2022-06-13 00:32:16.083662
# Unit test for function get_all_facts
def test_get_all_facts():
    module_utils_path = '../../../../module_utils'
    sys.path.insert(0, os.path.realpath(module_utils_path))
    from ansible.module_utils.facts.facts import get_all_facts
    import mock

    # make a mock AnsibleModule class with a dictionary as argspec
    am = mock.MagicMock()
    # use a simple argspec - module only takes one param 'gather_subset'
    # set module.params to same dictionary
    am.params = {'gather_subset': ['all']}

    # TODO: test with ansible 2.0/2.1 AnsibleModule, which doesn't have gather_subset or gather_timeout
    # need to set up fake sys.modules[['ansible', 'module_utils'] + ANSIBLE_MODULE_

# Generated at 2022-06-13 00:32:21.227747
# Unit test for function ansible_facts
def test_ansible_facts():

    # module_utils.facts.ansible_collector.AnsibleCollector._get_ansible_filter_spec used to
    #  include a default of '*'. So include that as a test case
    module_params = {'filter': '*'}

    class FakeModule:
        def __init__(self, module_params):
            self.params = module_params

    fake_module = FakeModule(module_params)

    ansible_facts_dict = ansible_facts(module=fake_module)

    # verify that there are keys in the dict
    assert len(ansible_facts_dict) > 0

    # verify that the keys start with 'ansible_'
    for key, value in ansible_facts_dict.items():
        assert key.startswith('ansible_')

    # verify that the dict contains

# Generated at 2022-06-13 00:32:28.591951
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils.facts import ansible_collector
    from ansible.module_utils.facts.collector import BaseFactCollector
    import ansible.module_utils.facts as facts_module
    import ansible.module_utils.facts.network as network
    import ansible.module_utils.facts.distribution as distribution
    import ansible.module_utils.facts.service as service
    import ansible.module_utils.facts.system as system
    import ansible.module_utils.facts.virtual as virtual

    # test mocks
    import unittest.mock as mock
    import sys

# Generated at 2022-06-13 00:32:37.635930
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts.network.base import NetworkCollector

    module_mock = MagicMock()
    module_mock.params = {
        'gather_subset': ['all'],
        'gather_timeout': 10
    }

    collect_mock = MagicMock(return_value={"test": 'foo', 'test2': 'bar'})
    facts_collector_mock = MagicMock(spec=NetworkCollector)
    facts_collector_mock.collect = collect_mock
    facts_collector_mock.REQUIRED_SUBSET = frozenset()

    facts_module = ansible_facts(module_mock)
    assert facts_module == {'test': 'foo', 'test2': 'bar'}

# Generated at 2022-06-13 00:32:46.213753
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts.network.base import NetworkCollector
    from ansible.module_utils.facts.system.base import SystemCollector
    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils.facts import ansible_collector
    from ansible.module_utils.facts.namespace import PrefixFactNamespace

    class MockAnsibleModule(object):
        def __init__(self, params):
            self.params = params

    class MockNetworkCollector(NetworkCollector):
        def collect(self, module=None, collected_facts=None):
            return {'foo': 'hello'}


# Generated at 2022-06-13 00:33:51.270844
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts import ansible_facts

    module_mock = Mock()
    module_mock.params = {'gather_subset': ['apparmor']}
    collected_facts = ansible_facts(module_mock)
    assert isinstance(collected_facts, dict)
    assert 'apparmor' in collected_facts
    assert collected_facts['apparmor'] is not None

# Generated at 2022-06-13 00:33:58.913234
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils.facts import ansible_collector
    from ansible.module_utils._text import to_bytes
    from dummy_ansible_module import AnsibleModule

    gather_subset = 'all'
    gather_timeout = 10
    filter_spec = '*'


# Generated at 2022-06-13 00:34:06.787232
# Unit test for function get_all_facts
def test_get_all_facts():
    # test for get_all_facts when gather_subset is ['all']
    module = MockModule()
    module.params = {'gather_subset': ['all']}
    facts = get_all_facts(module)
    assert ('default_ipv4' in facts)


    # test for get_all_facts when gather_subset is ['all']
    module = MockModule()
    module.params = {'gather_subset': ['platform']}
    facts = get_all_facts(module)
    assert ('default_ipv4' in facts)
    assert ('ansible_apparmor' not in facts)



# Generated at 2022-06-13 00:34:14.874216
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts import facts
    from ansible.module_utils.facts import ansible_collector

    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.facts._text import to_text

    test_module = AnsibleModule(argument_spec={}, supports_check_mode=True)

    ansible_facts = ansible_facts(test_module)

    assert ansible_facts['python'] == facts.get_python_facts()

    assert ansible_facts['sysctl'] == facts.get_sysctl_facts()

    # determine if we're running on linux
    if ansible_facts['system'] == 'Linux':
        assert ansible_facts['selinux'] == facts.get_selinux_facts()

    raw_facts = facts.get_raw_