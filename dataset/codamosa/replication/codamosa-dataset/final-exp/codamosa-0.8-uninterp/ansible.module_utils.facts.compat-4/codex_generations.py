

# Generated at 2022-06-13 00:24:18.372855
# Unit test for function ansible_facts
def test_ansible_facts():
    import os
    import tempfile

    # Import ansible 2.2 module_utils functions
    module_args = dict(
        gather_subset=['all'],
        gather_timeout=10,
        ansible_facts=dict(ansible_all_ipv4_addresses=['192.0.2.8']),
    )

    facts_dict = dict(ansible_all_ipv4_addresses=['192.0.2.8'])

    test_dir = tempfile.mkdtemp()
    test_env = dict(PATH=test_dir)

    with tempfile.NamedTemporaryFile(mode='w+t', dir=test_dir) as tmp_f:
        tmp_f.write('''#!/bin/bash
exit 0
''')
        tmp_f.flush()
       

# Generated at 2022-06-13 00:24:22.424000
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(argument_spec={})
    # gather_subset defaults to ['all']
    assert ansible_facts(module, gather_subset=None) is not None

# Generated at 2022-06-13 00:24:31.750887
# Unit test for function ansible_facts
def test_ansible_facts():
    import ansible.module_utils.facts.network as network
    from ansible.module_utils.facts import default_collectors
    import platform
    import time
    import socket
    import os

    class AnsibleModuleFake(object):
        def __init__(self, params):
            self.params = params

    class DefaultCollectorsFake(object):
        def __init__(self):
            self.network = network.NetworkCollector
            self.platform = platform.PlatformFactCollector
            self.time = time.TimeFactCollector
            self.socket = socket.SocketFactCollector
            self.os = os.OperatingSystemFactCollector

    def test_setup():
        return default_collectors.DEFAULT_GATHER_TIMEOUT

    def test_teardown(old):
        default_collectors.DEFAULT_G

# Generated at 2022-06-13 00:24:38.565215
# Unit test for function ansible_facts
def test_ansible_facts():
    class FakeModule:
        def __init__(self,params=None):
            self.params = params or {}
        # module_utils.facts.ansible_facts uses set_fact to save results to the in-memory AnsibleModule
        def set_fact(self,*args):
            key = args[0]
            value = args[1]
            self.params[key] = value

    fake_module = FakeModule()
    # pretend we are running with a gather_subset
    fake_module.params['gather_subset'] = ['!all']
    # pretend we are not running with a gather_timeout
    fake_module.params['gather_timeout'] = None
    # pretend we are not running with a fact filter
    fake_module.params['filter'] = None

    ansible_facts(module=fake_module)

# Generated at 2022-06-13 00:24:50.121776
# Unit test for function get_all_facts
def test_get_all_facts():
    import module_utils.facts
    import ansible.module_utils.facts as a_facts

    # Most of the functionality is tested in test_ansible_facts.
    # This test just checks the wrapping logic.

    # Strip the gather_subset from the non-compat api, wrapped by the compat get_all_facts(),
    # and make sure we get the same results.
    module_all_facts = a_facts.ansible_facts
    module_utils_get_all_facts = module_utils.facts.get_all_facts

    class DummyModule:
        def __init__(self, params):
            self.params = params

    module_params = {'gather_subset': ['all']}
    module = DummyModule(params=module_params)

    module_all_facts_results = module_all_

# Generated at 2022-06-13 00:24:58.145762
# Unit test for function ansible_facts
def test_ansible_facts():
    import sys
    import os
    import re
    import collections

    # python3, ansible 2.3+
    if sys.version_info[0] == 3:
        from ansible.module_utils.basic import AnsibleModule
        ANSIBLE_PATH = os.environ.get('ANSIBLE_PATH', '')
        PATHS = [x for x in os.environ.get('PYTHONPATH', '').split(':') if x]
        if ANSIBLE_PATH:
            PATHS.append(ANSIBLE_PATH)
        sys.path = PATHS

    # python2, ansible 2.0-2.2
    else:
        from ansible.module_utils.basic import *
        from ansible.module_utils.facts import collector

    # for test_module_utils_basic

# Generated at 2022-06-13 00:25:08.046129
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts.facts import Facts
    from ansible.module_utils.facts import ansible_collector as a_collector
    from ansible.module_utils.six import iteritems

    class FakeModule(object):
        '''A fake ansible module for testing get_all_facts'''

        def __init__(self):
            self.params = {}

        @staticmethod
        def get_bin_path(app, opts=None, required=False):
            return '/bin/' + app

        def run_command(self, cmd):
            return None, '', 0

    module = FakeModule()

    # collect a facts dict with all facts
    all_facts_dict = ansible_facts(module, gather_subset='all')
    # assert we found a fact for each collector
    assert all

# Generated at 2022-06-13 00:25:16.764730
# Unit test for function ansible_facts
def test_ansible_facts():
    '''Unit test for function ansible_facts.

    In this unit test, we mock the 'module'. An actual AnsibleModule would
    be an instance of AnsibleModule, with an 'ansible_facts' dict attribute.

    '''

    class MockAnsibleModule():
        def __init__(self):
            self.ansible_facts = {}

        def fail_json(self, msg):
            pass

    mock_ansible_module = MockAnsibleModule()

    facts = ansible_facts(mock_ansible_module)
    assert isinstance(facts, dict)

# Generated at 2022-06-13 00:25:17.768220
# Unit test for function ansible_facts

# Generated at 2022-06-13 00:25:23.511211
# Unit test for function ansible_facts
def test_ansible_facts():
    import ansible.module_utils.facts.collector.command
    from ansible.module_utils.facts import ansible_collector
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.namespace import PrefixFactNamespace

    class TestCollector(BaseFactCollector):
        NAME = 'test'

        def collect(self, module=None, collected_facts=None):
            if 'test_fact1' not in collected_facts:
                collected_facts['test_fact1'] = 'test_val1'
            if 'test_fact2' not in collected_facts:
                collected_facts['test_fact2'] = 'test_val2'
            return collected_facts


# Generated at 2022-06-13 00:25:36.533846
# Unit test for function ansible_facts
def test_ansible_facts():
    '''Unit test for function ansible_facts'''

    import ansible.module_utils.facts.namespace as namespace
    import ansible.module_utils.facts.collector as collector
    from ansible.module_utils.facts import fact_cache
    from ansible.module_utils.facts.collector import FacterCollector
    import ansible.module_utils.facts.utils as utils
    import ansible.module_utils.facts.system as system

    old_load_collectors = collector.load_collectors

    def fake_load_collector(cls, path, mod_name):
        '''Fake load_collector function, which doesn't actually try to load anything'''
        return []

    def fake_type(obj):
        '''Fake type function that always returns 'type' '''
        return 'type'

# Generated at 2022-06-13 00:25:45.804353
# Unit test for function get_all_facts
def test_get_all_facts():

    # Fake module object that AnsibleModule uses to pass variables to plugins.
    # This is used to fake up the way normal modules get their variables.
    module = '''
    class _AnsibleModule(object):
        def __init__(self, **kwargs):
            self.params = kwargs

        def _handle_aliases(self, value, aliases):
            return aliases.get(value, value)
    '''

    # Mock the AnsibleModule class and execute get_all_facts method.
    # This is used to fake up the way normal modules get their variables.
    ansible_module = '''
    try:
        from ansible.module_utils.facts import get_all_facts
    except ImportError:
        from ansible.module_utils.facts import ansible_facts as get_all_facts
    '''

# Generated at 2022-06-13 00:25:57.813590
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts import default_collectors

    default_collectors.validate_collector_classes()

    from ansible.module_utils.ansible_release import __version__ as ansible_version

    import ansible.module_utils.facts.ansible_collector as ac

    # monkey patch to avoid actual system calls
    def _get_all_legacy_facts(module, collector_classes):
        return {'test_fact': 'test_value'}

    ac._get_all_legacy_facts = _get_all_legacy_facts

    # this is what would be returned by the AnsibleModule class

# Generated at 2022-06-13 00:26:08.204608
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils._text import to_bytes, to_text
    from ansible.module_utils.facts import get_collector_class, ansible_facts
    from ansible.module_utils.facts.virtual import VirtualCollector
    from ansible.module_utils.facts.system import SystemCollector
    from ansible.module_utils.facts.collector import BaseFactCollector


    class MockModule(object):
        def __init__(self, params):
            self.params = params
            self.run_command_environ_update = dict()

    class ModuleCollector(BaseFactCollector):
        def collect(self, module=None, collected_facts=None):
            fact_name = 'ansible_%s' % self.namespace.namespace_name

# Generated at 2022-06-13 00:26:19.339379
# Unit test for function get_all_facts
def test_get_all_facts():
    import sys

    # Add this repository's lib path to import path
    # it is not added to the sys.path by default
    def add_lib_path():
        import os
        import inspect

        currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
        parentdir = os.path.dirname(currentdir)
        sys.path.insert(0, parentdir + "/lib/")

    add_lib_path()

    from ansible.module_utils.facts.namespace import PrefixFactNamespace

    from ansible.module_utils.facts.network.base import NetworkCollector

    from ansible.module_utils.facts.processor.base import ProcessorCollector

    from ansible.module_utils.facts.system.base import SystemCollector


# Generated at 2022-06-13 00:26:30.988586
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils.facts import get_all_facts as gaf

    class FakeModule(object):
        def __init__(self, params):
            self.params = params

    params = {'gather_subset': ['all']}
    # instance of a FakeModule object
    fm = FakeModule(params=params)
    # test w/ gather_subset
    assert gaf(fm) == ansible_facts(fm)

    params = {'gather_timeout': 10, 'filter': '*', 'gather_subset': ['all']}
    # instance of a FakeModule object
    fm = FakeModule(params=params)
    # test w/ gather_timeout, filter, gather_subset
    assert gaf(fm) == ansible_facts(fm)


# Generated at 2022-06-13 00:26:41.492611
# Unit test for function ansible_facts
def test_ansible_facts():
    import pytest
    from ansible.module_utils.facts import cache

    # the cache collector has no collect simple method, so just smoke test to see if it can be called.
    class FakeModule:
        params = dict(gather_subset=['all'])

    facts_d = ansible_facts(module=FakeModule)
    assert isinstance(facts_d, dict)

    # get rid of cached collectors and reset gather_subset
    cache.FACTS_CACHE = None
    FakeModule.params['gather_subset'] = ['min']

    with pytest.raises(AttributeError):
        assert ansible_facts(module=FakeModule) is None

    FakeModule.params['gather_subset'] = ['all']

# Generated at 2022-06-13 00:26:51.799533
# Unit test for function ansible_facts
def test_ansible_facts():
    gather_subset = ['all']
    gather_timeout = 10
    filter_spec = '*'

    minimal_gather_subset = frozenset(['apparmor', 'caps', 'cmdline', 'date_time',
                                       'distribution', 'dns', 'env', 'fips', 'local',
                                       'lsb', 'pkg_mgr', 'platform', 'python', 'selinux',
                                       'service_mgr', 'ssh_pub_keys', 'user'])

    from ansible.module_utils.facts import default_collectors
    all_collector_classes = default_collectors.collectors
    namespace = PrefixFactNamespace(namespace_name='ansible', prefix='')

# Generated at 2022-06-13 00:26:56.626295
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts import get_all_ansible_facts
    print('Testing')
    f = {}
    for key, value in get_all_ansible_facts(module).items():
        print('{}: {}'.format(key, value))
    print('end test')

# Generated at 2022-06-13 00:27:04.669011
# Unit test for function ansible_facts
def test_ansible_facts():
    import pytest
    from module_utils.facts.utils import get_all_collectors_from_namespace, get_collector_names_from_list

    module = pytest.fixture.AnsibleModule

    # get all facts, with no filter or gather_subset
    facts = ansible_facts(module=module)
    assert facts
    assert 'ansible_lsb' in facts
    assert 'all_ipv4_addresses' in facts
    assert 'all_ipv6_addresses' in facts

    # get facts with a filter, with no gather_subset
    facts = ansible_facts(module=module, filter_spec='ansible_*')
    assert facts
    assert 'ansible_lsb' in facts
    assert 'all_ipv4_addresses' not in facts

# Generated at 2022-06-13 00:27:14.833341
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts.core import get_default_gather_subset
    from ansible.module_utils.facts import ModuleUtilsLegacyFacts
    from ansible.module_utils.facts import ansible_facts
    from ansible.module_utils.facts.virtual.posix import LinuxVirtualFactsCollector
    from ansible.module_utils.facts import default_collectors

    # Overwrite the default collectors so I can add/remove items from it
    default_collectors.collectors = [LinuxVirtualFactsCollector]

    # Make a fake module.  AnsibleModule doesn't work for this, because it needs
    # to work with modules that inherit from it

# Generated at 2022-06-13 00:27:19.302491
# Unit test for function ansible_facts
def test_ansible_facts():

    import ansible.module_utils.facts as utils_facts
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_native

    def fail_json(*args, **kwargs):
        '''function to patch over fail_json'''
        kwargs['failed'] = True
        print('FAILED: {0}'.format(kwargs))
        return kwargs

    def exit_json(*args, **kwargs):
        '''function to patch over exit_json'''
        if 'changed' not in kwargs:
            kwargs['changed'] = False
        print('SUCCESS: {0}'.format(kwargs))
        return kwargs

    class FakeModule(object):
        '''Class with the minimum attributes needed to run ansible_facts'''
       

# Generated at 2022-06-13 00:27:20.385768
# Unit test for function ansible_facts
def test_ansible_facts():
    # TODO
    pass

# Generated at 2022-06-13 00:27:26.518831
# Unit test for function ansible_facts
def test_ansible_facts():
    import sys
    if sys.version_info[0] > 2:
        # ansible_collections is only available on ansible 2.5+
        # Skip unit test if running in ansible 2.4 or earlier.
        pass
    else:
        import ansible_collections
        from ansible_collections.ansible.netcommon.plugins.module_utils.facts import facts
        assert facts.ansible_facts is facts.ansible_facts_refactored

# Generated at 2022-06-13 00:27:33.475676
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils.facts import get_all_facts

    # The DEFAULT_GATHER_SUBSET may be set by Ansible, if it is not
    # we can set it to a default value
    import ansible
    if not hasattr(ansible, 'DEFAULT_GATHER_SUBSET'):
        ansible.DEFAULT_GATHER_SUBSET = ['all']

    # mock the 'module' arg for testing
    class FakeModule():
        def __init__(self):
            self.params = dict(gather_subset=ansible.DEFAULT_GATHER_SUBSET)
    module = FakeModule()

    assert get_all_facts(module) is not None

# Generated at 2022-06-13 00:27:46.244590
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.modules.system import setup
    import sys
    import os
    import json

    # This is to force 'setup' module to run and create the local facts file
    test_collector = ansible_collector.get_ansible_collector(all_collector_classes=default_collectors.collectors,
                                                             filter_spec='ansible_local')
    with setup.AnsibleModule(argument_spec={'gather_subset': dict(default='!all', type='list')},
                             check_invalid_arguments=False, bypass_checks=True) as module:
        test_collector.collect(module=module)

    # Copy the generated ansible_facts file to this directory

# Generated at 2022-06-13 00:27:50.437617
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts._collector.ansible import AnsibleCollector
    from ansible.module_utils.facts._collector.base import BaseFactCollector
    from ansible.module_utils.facts import ansible_collector
    # Monkey patch the AnsibleCollector class so its collect method
    # will return a known constant
    def fake_collect(module):
        return {'a fact': 'the fact'}

    orig_collect = AnsibleCollector.collect
    AnsibleCollector.collect = fake_collect

    module = FakeModule()

    # FakeModule.params doesn't have any params.
    # Check defaults.
    result1 = ansible_facts(module)
    AnsibleCollector.collect = orig_collect
    assert result1 == {'a fact': 'the fact'}

    # Still no

# Generated at 2022-06-13 00:27:58.072017
# Unit test for function get_all_facts
def test_get_all_facts():
    import json
    from ansible.module_utils.facts import get_all_facts
    from ansible.module_utils.facts.namespace import PrefixFactNamespace

    # pylint: disable=too-few-public-methods
    class FakeModule(object):
        '''
        fake module to mock out the AnsibleModule class
        '''

        def __init__(self):
            self.params = {'gather_subset': ['all']}

        def fail_json(self, **kwargs):
            raise Exception(json.dumps(kwargs))

    def mock_collect(self, module):
        return dict(test_get_all_facts=dict(test_get_all_facts='test_get_all_facts'))

    real_collect = PrefixFactNamespace.collect
    PrefixFact

# Generated at 2022-06-13 00:28:05.071819
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts.collector import CollectedFacts
    from ansible.module_utils._text import to_text

    class MockAnsibleModule(object):
        '''
        This is a "patched" version of AnsibleModule that is meant to be used in testing.

        See https://github.com/ansible/ansible/blob/devel/lib/ansible/module_utils/basic.py for
        details about the real class.
        '''

        def __init__(self, params):
            self.params = params

    # set up a minimal config and fact cache settings
    default_facts = CollectedFacts(None, {}, {}, {})

    config = {}
    config['gather_subset'] = ['all']
    config['gather_filter'] = '*'



# Generated at 2022-06-13 00:28:16.030886
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils.facts import collect_facts
    from ansible.module_utils.facts.collector.network import NetworkCollector
    from ansible.module_utils.facts.fact_cache import FactCache
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts import ansible_collector

    class FakeModule(object):
        '''A fake AnsibleModule that emulates some of the methods that are called by
        collect_facts & get_all_facts
        '''

        def __init__(self, params):
            self.params = params


# Generated at 2022-06-13 00:28:30.907919
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils.facts import ansible_collector
    test_module_name = 'test_module'

    class TestModule(object):
        params = {}

        def get_bin_path(self, arg, opt_dirs=[]):
            if arg in ('systemctl', 'ss', 'ps'):
                return arg

    test_module = TestModule()

    # call get_all_facts with params that tells it to load the all the default collectors
    facts = get_all_facts(module=test_module)

# Generated at 2022-06-13 00:28:40.631290
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts import ansible_facts
    from ansible.module_utils.facts import icmp_unreachable_fact
    from ansible.module_utils.facts import default_collectors
    import sys
    import mock
    module = mock.Mock()
    module.params = {'filter': '*'}
    all_collector_classes = default_collectors.collectors
    class_names = [c.__class__.__name__ for c in all_collector_classes]
    if 'ICMPNetworkFactCollector' in class_names:
        all_collector_classes[class_names.index('ICMPNetworkFactCollector')] = icmp_unreachable_fact.ICMPNetworkFactCollector
    if 'DistributionFactCollector' in class_names:
        all_collect

# Generated at 2022-06-13 00:28:52.721422
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils.facts import ansible_collector

    class FakeModule:
        def __init__(self):
            self.params = {'gather_subset': ['all'],
                           'gather_timeout': 10,
                           'filter': '*'}

    class FakeCollector:
        def __init__(self):
            self.fact_dict = {}

        def collect(self, module):
            return self.fact_dict

    fake_module = FakeModule()

    # test no facts
    fake_collector = FakeCollector()
    ansible_collector.get_

# Generated at 2022-06-13 00:29:00.377290
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils.facts import get_all_facts
    from ansible.module_utils.facts import ansible_facts
    from ansible.module_utils.facts import ansible_collector
    from ansible.module_utils.facts import default_collectors

    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts.collector.ansible_collector import AnsibleFactCollector

    # Stub out a 'module' object
    class TestModule():
        def __init__(self, gather_subset):
            self.params = {'gather_subset': gather_subset}

        def fail_json(self, msg, **kwargs):
            pass


# Generated at 2022-06-13 00:29:08.942799
# Unit test for function get_all_facts
def test_get_all_facts():
    import ansible.module_utils.facts.namespace as ns
    import ansible.module_utils.facts.ansible_collector as ac
    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils.facts import ansible_collector
    import ansible.module_utils.facts.hardware.cpu as cpu

    def mock_collect(self, module):
        return {'processor': 'Intel'}

    cpu.cpu.collect = mock_collect
    # NOTE: this method is only used by tests. If/when this module is imported,
    # it will always be executed within module_utils/facts/__init__.py and the
    # module_utils/facts/ansible_collector.py get_ansible_collector function will
    # be used.

# Generated at 2022-06-13 00:29:13.013721
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts import module_utils

    module_util_class = module_utils()
    function_name = module_util_class.get_function('ansible_facts')

    # Test that function is copied over successfully
    assert function_name == ansible_facts

# Generated at 2022-06-13 00:29:20.471843
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts import __tree__ as facts_tree
    import os

    # make sure this is the facts directory
    assert os.path.basename(os.path.dirname(facts_tree.__file__)) == 'facts'

    from ansible.module_utils.six import iteritems
    from ansible.module_utils.facts import default_collectors

    all_fact_classes = default_collectors.collectors

    # make sure no fact class is duplicated
    assert len(all_fact_classes) == len(set([fact_class.__name__ for fact_class in all_fact_classes]))

    # build a fact collector class that only collects facts that are not a default fact

# Generated at 2022-06-13 00:29:33.163137
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts import ansible_collector
    from ansible.module_utils._text import to_bytes
    import json

    class MockModule(object):
        params = {'filter': 'ansible_ls', 'gather_subset': ['all']}

        def __init__(self):
            self.argument_spec = {'gather_subset': dict(default=[], type='list')}
            self.fail_json = fail_json

        def fail_json(self, *args, **kwargs):
            raise AssertionError("AnsibleModule.fail_json called with arguments %s %s" % (args, kwargs))


# Generated at 2022-06-13 00:29:43.465185
# Unit test for function get_all_facts
def test_get_all_facts():
    class AnsibleModule:
        def __init__(self, params=None):
            self.params = {}
            if params:
                self.params.update(params)

    class FakeCollector:
        def __init__(self, name):
            self.name = name

        def collect(self):
            return {'Fact': self.name}

    class FakeFactCollector:
        def __init__(self, module, collectors):
            self.module = module
            self.collectors = collectors
            self.collection = {}

        def collect(self):
            for c in self.collectors:
                self.collection.update(c.collect())
            return self.collection


# Generated at 2022-06-13 00:29:54.655159
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.basic import AnsibleModule
    import json

    # input_data is a dict of input params to the ansible module
    # gather_subset and gather_timeout are defined by module_utils.facts.GATHERING_SUBSET_ALL
    input_data = {
        "gather_subset": "network, hardware",
        "gather_timeout": 10,
        "filter": "ansible_all_ipv4_addresses"
    }

    # Module is an instance of AnsibleModule, with the parameters defined in input_data
    module = AnsibleModule(argument_spec=input_data)

    # call the method being tested
    facts = ansible_facts(module, gather_subset=['network', 'hardware'])

    # fact contains a dict of all facts, with key=names

# Generated at 2022-06-13 00:30:14.988019
# Unit test for function ansible_facts
def test_ansible_facts():
    # hack the right modules into the import path so we can test import
    import sys
    import tempfile

    executable = sys.executable
    sys.path.append('./library')
    sys.path.append('./library/module_utils')

    from library.junos_get_facts import get_all_facts
    from ansible.module_utils.facts.utils import set_module_args
    from ansible.module_utils.basic import AnsibleModule

    with tempfile.NamedTemporaryFile() as f:
        set_module_args(args={
            'gather_subset': '!all',
            'filter': 'ansible_default_ipv4',
        })
        m = AnsibleModule(
            argument_spec=dict(),
            supports_check_mode=True
        )

        # http

# Generated at 2022-06-13 00:30:19.658158
# Unit test for function ansible_facts
def test_ansible_facts():
    '''unit test for ansible_facts function'''

    result = ansible_facts(module=DummyModule())
    assert result
    assert 'ansible_facts' in result
    assert result['ansible_facts']
    assert 'local' in result['ansible_facts']
    assert 'hostname' in result['ansible_facts']['local']
    assert result['ansible_facts']['local']['hostname'] == 'localhost'


# Generated at 2022-06-13 00:30:31.098338
# Unit test for function ansible_facts
def test_ansible_facts():
    import sys
    import os
    from ansible.module_utils.facts import ansible_collector
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts import default_collectors
    module_base = os.path.join(os.path.dirname(__file__), "..", "..")
    module_base = os.path.abspath(module_base)

    # module which doesn't use facts#ansible_facts
    module_path = os.path.join(module_base, "lib/ansible/modules/network/cisco/asa_config.py")
    module = import_module_from_path(module_path)

    original_sys_modules = sys.modules.copy()

# Generated at 2022-06-13 00:30:42.100432
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.facts.collector import get_file_namespace
    from ansible.module_utils.facts.collector import BaseFileCollector

    class DummyFileCollector(BaseFileCollector):
        name = 'dummy'
        _fact_ids = ['dummy_fact']

        def _collect(self, module=None, collected_facts=None):
            return {'dummy': 'dummy'}

    test_module = AnsibleModule({
        'gather_subset': 'all',
        'gather_timeout': 1,
        'filter': '*',
        'paths': ['dummy_path'],
    }, supports_check_mode=False)


# Generated at 2022-06-13 00:30:53.328959
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils import basic
    from ansible.module_utils.facts import ansible_collector

    module = basic.AnsibleModule(argument_spec={})
    module.params['gather_subset'] = ['all']
    module.params['gather_timeout'] = 10
    module.params['filter'] = '*'

    minimal_gather_subset = frozenset(['apparmor', 'caps', 'cmdline', 'date_time',
                                       'distribution', 'dns', 'env', 'fips', 'local',
                                       'lsb', 'pkg_mgr', 'platform', 'python', 'selinux',
                                       'service_mgr', 'ssh_pub_keys', 'user'])

    all_collector_classes = default_collectors.collectors

    expected_

# Generated at 2022-06-13 00:31:05.459540
# Unit test for function ansible_facts
def test_ansible_facts():
    class FakeModule(object):
        def __init__(self, params):
            self.params = params


    def run_ansible_facts(params):
        module = FakeModule(params=params)
        return ansible_facts(module=module)

    # make sure defaults work
    result = run_ansible_facts(params={})
    assert 'local' in result

    # make sure it filters the expected subset of facts
    result = run_ansible_facts(params={
        'gather_subset': ['local', 'non_existent'],
    })
    assert 'local' in result
    assert 'pkg_mgr' not in result

    # make sure it ignores extra collector_classes

# Generated at 2022-06-13 00:31:09.435934
# Unit test for function ansible_facts
def test_ansible_facts():
    class FakeAnsibleModule(object):
        class FakeParam(object):
            def __init__(self, value):
                self.value = value

            def __bool__(self):
                return bool(self.value)

        def __init__(self, gather_subset=None):
            self.params = {'gather_subset': gather_subset}

    # gather_subset is not specified
    module = FakeAnsibleModule()
    assert ansible_facts(module)

    module = FakeAnsibleModule(gather_subset=['all'])
    assert ansible_facts(module)

    # gather_subset is specified
    module = FakeAnsibleModule(gather_subset=['min'])
    assert ansible_facts(module)

# Generated at 2022-06-13 00:31:16.554378
# Unit test for function ansible_facts
def test_ansible_facts():
    # define module as a stub
    class ModuleStub(object):
        def __init__(self, params):
            self.params = params

        class FailJsonException(Exception):
            pass

        class ExitJsonException(Exception):
            pass

        class ReturnValue(object):
            def __init__(self, invocations=None):
                self.invocations = invocations or {}

            def invoke_fail_json(self, *args, **kwargs):
                key = args[0] if args else ''
                self.invocations[key] = self.invocations.get(key, 0) + 1
                raise self.FailJsonException()

            def invoke_exit_json(self, *args, **kwargs):
                key = args[0] if args else ''
                self.invocations[key] = self.inv

# Generated at 2022-06-13 00:31:21.796702
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.basic import AnsibleModule
    def test_module():
        module = AnsibleModule(argument_spec={})
        return module

    module = test_module()
    result = ansible_facts(module)

    assert result
    assert type(result) == dict
    assert 'fqdn' in result
    assert 'domain' in result


# Generated at 2022-06-13 00:31:24.971835
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils.facts import get_all_facts
    import ansible.module_utils.facts.namespace as namespace
    namespace.namespace_manager = namespace.NamespaceManager()
    assert get_all_facts(None) == {}

# Generated at 2022-06-13 00:31:50.132923
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils._text import to_text
    from ansible.module_utils.facts import ansible_facts

    facts_dict = ansible_facts(module=None, gather_subset=[])

    keys = set()

    for key in facts_dict:
        keys.add(key)
        assert type(key) == str
        assert type(facts_dict[key]) == str
        assert to_text(facts_dict[key]) == facts_dict[key]

# Generated at 2022-06-13 00:31:58.192578
# Unit test for function ansible_facts
def test_ansible_facts():

    class FakeModule(object):
        def __init__(self, params, module_name='fake_ansible_module'):
            self.params = params
            self.name = module_name

        def return_values(self, *args, **kwargs):
            print('args = %s' % args)
            print('kwargs = %s' % kwargs)

        def fail_json(self, *args, **kwargs):
            print('args = %s' % args)
            print('kwargs = %s' % kwargs)

        def exit_json(self, *args, **kwargs):
            print('args = %s' % args)
            print('kwargs = %s' % kwargs)

        def debug(self, msg):
            print(msg)

    import sys
    import inspect


# Generated at 2022-06-13 00:32:05.336801
# Unit test for function ansible_facts
def test_ansible_facts():
    '''test for function ansible_facts'''
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(argument_spec={'filter': dict(type='list', default=['*'])})

    facts_dict = ansible_facts(module, gather_subset=None)

    assert isinstance(facts_dict, dict)
    assert 'distribution' in facts_dict
    assert 'distribution_release' in facts_dict
    assert 'distribution_major_version' in facts_dict



# Generated at 2022-06-13 00:32:10.579454
# Unit test for function ansible_facts
def test_ansible_facts():

    class AnsibleModule(object):
        def __init__(self, params):
            self.params = params

    test_module = AnsibleModule(params={'gather_subset': 'all', 'gather_timeout': 10,
                                        'filter': 'ansible_*'})

    test_data = ansible_facts(test_module)

    assert isinstance(test_data, dict)

# Generated at 2022-06-13 00:32:15.514264
# Unit test for function ansible_facts
def test_ansible_facts():
    # Test with AnsibleModule
    module = AnsibleModule(argument_spec={})
    module.params = {
        'filter': '*',
        'gather_subset': ['all'],
        'gather_timeout': 10,
    }

    assert ansible_facts(module) == get_all_facts(module)

# Generated at 2022-06-13 00:32:20.737259
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils.basic import AnsibleModule

    classmock = AnsibleModule(argument_spec={'gather_subset': dict(default=['all'], type='list')})
    allfacts = get_all_facts(classmock)

    assert isinstance(allfacts, dict)

    assert 'default_ipv4' in allfacts



# Generated at 2022-06-13 00:32:28.307212
# Unit test for function ansible_facts
def test_ansible_facts():
    '''Tests the return value of ansible_facts is as expected based on many different input params'''

    import sys
    import os
    import tempfile
    import shutil
    import stat
    import subprocess
    import pytest
    from collections import namedtuple

    class MockAnsibleModule:
        '''Mocks an AnsibleModule object'''

        class MockAnsibleModule():
            '''Mocks a params attribute on an AnsibleModule object'''

            def __init__(self, params):
                self.params = params

        def __init__(self, params):
            self.params = self.MockAnsibleModule(params)

    MockAnsibleModuleFixt = namedtuple('MockAnsibleModuleFixt', ['description', 'params', 'expected_facts'])


# Generated at 2022-06-13 00:32:37.749850
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts.namespace import PrefixFactNamespace

    from ansible.module_utils.basic import AnsibleModule
    import imp
    import os

    class TestModule(AnsibleModule):
        pass

    module = TestModule(argument_spec={'gather_subset': {'type': 'list', 'default': ['all']},
                                       'gather_timeout': {'type': 'int', 'default': 10}},
                        supports_check_mode=True)

    module.params['gather_subset'].extend(('default', 'network'))

    module_path = os.path.join(os.path.dirname(__file__), 'ansible_facts.py')
    test_module = imp.load_

# Generated at 2022-06-13 00:32:46.308545
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils.facts.network.linux import Lsip_interfaces
    from ansible.module_utils import facts
    import mock
    import __builtin__ as builtins

    # Define test parameters
    gather_timeout = 5
    gather_subset = ['all']
    filter_spec = 'Ethernet'
    module_params = {'gather_timeout': gather_timeout,
                     'gather_subset': gather_subset,
                     'filter': filter_spec}

    # Define test fixtures

# Generated at 2022-06-13 00:32:59.189471
# Unit test for function ansible_facts
def test_ansible_facts():
    import StringIO
    try:
        from test.support import EnvironmentVarGuard, run_unittest
    except ImportError:
        from unittest.mock import patch

        from ansible.module_utils.facts import ansible_facts

        import unittest

        class TestAnsibleFacts(unittest.TestCase):

            @patch('ansible.module_utils.facts.default_collectors.collectors', {'test_collector': 'test_value'})
            @patch('ansible.module_utils.facts.ansible_collector.get_ansible_collector')
            def test_ansible_facts(self, collector):
                '''Test ansible_facts with basic args'''

# Generated at 2022-06-13 00:33:44.206264
# Unit test for function get_all_facts
def test_get_all_facts():

    import ansible.module_utils.facts.namespace

    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts import default_collectors, ansible_collector
    from ansible.module_utils.facts import get_all_facts

    module = ansible.module_utils.facts.get_all_facts.FakeModule()

    # fake the gather_subset param
    module.params['gather_subset'] = ['all']

    facts_dict = get_all_facts(module)

    assert isinstance(facts_dict, dict)
    assert 'virtualization_type' in facts_dict
    assert 'distribution' in facts_dict
    assert facts_dict['virtualization_type'] == 'lxc'

# Generated at 2022-06-13 00:33:53.931848
# Unit test for function get_all_facts
def test_get_all_facts():
    # What happens if gather_subset is absent?  We should default.
    module_mock = mock.MagicMock()
    module_mock.params = {'gather_subset':None}
    assert get_all_facts(module_mock) == ansible_facts(module_mock)

    # What happens if gather_subset is an empty list?
    # We should still use the full list
    module_mock.params['gather_subset'] = []
    assert get_all_facts(module_mock) == ansible_facts(module_mock)

    # What happens if gather_subset is present?  We should use that list
    module_mock.params['gather_subset'] = ['oh', 'hai']
    assert get_all_facts(module_mock) == ansible

# Generated at 2022-06-13 00:34:04.216614
# Unit test for function ansible_facts
def test_ansible_facts():
    # Import module here because it's not available in 2.2 and lower.
    from ansible.module_utils.facts import ansible_facts
    from ansible.module_utils.facts.collector import BaseFactCollector, CollectedFact
    from ansible.module_utils.facts.namespace import BaseFactNamespace
    from ansible_collections.notstdlib.moveitallout.plugins.module_utils.facts.network.base import NetworkCollector
    from ansible_collections.notstdlib.moveitallout.plugins.module_utils.facts.network.default import DefaultNetworkCollector
    from ansible_collections.notstdlib.moveitallout.plugins.module_utils.facts.network.linux import LinuxNetworkCollector


# Generated at 2022-06-13 00:34:10.858323
# Unit test for function ansible_facts
def test_ansible_facts():
    import ansible.module_utils.facts.ansible_facts as __fixture
    import ansible.module_utils.facts.ansible_facts as ansible_facts
    import ansible.module_utils.facts.cache as cache
    import ansible.module_utils.facts.namespace as namespace
    import ansible.module_utils.facts.collector as collector
    import ansible.module_utils.facts.file_dmesg as file_dmesg
    import ansible.module_utils.facts.file_ldconfig as file_ldconfig
    import ansible.module_utils.facts.file_lldp as file_lldp
    import ansible.module_utils.facts.file_mount as file_mount
    import ansible.module_utils.facts.file_uptime as file_uptime
    import ansible.module