

# Generated at 2022-06-13 00:24:18.728867
# Unit test for function ansible_facts
def test_ansible_facts():
    '''Unit test for function ansible_facts'''

    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts.network.base import NetworkCollector
    from ansible.module_utils.facts.collector import BaseFactCollector

    class MyNetworkCollector(NetworkCollector):
        '''stub network collector to inject into ansible_collector.get_ansible_collector'''

        NAMESPACE = 'my_network'

        def __init__(self, filter_spec, gather_subset=None):
            super(MyNetworkCollector, self).__init__(filter_spec,
                                                     gather_subset=gather_subset)

# Generated at 2022-06-13 00:24:29.244867
# Unit test for function ansible_facts
def test_ansible_facts():

    from ansible import constants as C
    from ansible.module_utils.facts import default_collectors

    default_subset = C.DEFAULT_GATHER_SUBSET

    assert default_subset == ['all']

    default_timeout = C.DEFAULT_GATHER_TIMEOUT

    assert default_timeout == 10

    class FakeModule:
        def __init__(self, params):
            self.params = params

    # test default param names, default gather_subset
    module = FakeModule({})

    facts = ansible_facts(module)
    assert len(facts) > 0

    # check that datetime is not in the facts, which means it was filtered out
    assert 'datetime' not in facts

    # test gather_subset=hardware

# Generated at 2022-06-13 00:24:37.028297
# Unit test for function get_all_facts
def test_get_all_facts():
    import six
    import mock
    if six.PY2:
        import __builtin__ as builtins  # pylint: disable=import-error
    else:
        import builtins  # pylint: disable=import-error

    class Module(object):
        def __init__(self, params):
            self.params = params

    module_ansible_facts = mock.Mock()
    builtins.module = module_ansible_facts

    module = Module(params={'gather_subset': ['all']})

    result = get_all_facts(module)
    assert result == module_ansible_facts.ansible_facts.return_value

    module_ansible_facts.ansible_facts.assert_called_once_with(module, gather_subset=['all'])


# Generated at 2022-06-13 00:24:45.403912
# Unit test for function ansible_facts
def test_ansible_facts():
    import ansible.module_utils.facts as facts
    import json
    from ansible.module_utils.facts import default_collectors
    import mock
    import os

    DEFAULT_FILTER='*'
    gather_timeout=10
    namespace = PrefixFactNamespace(namespace_name='ansible', prefix='')

    # Test all gather subset
    module_mock = mock.Mock()
    module_mock.params = {
        'gather_subset': ['all']
    }

# Generated at 2022-06-13 00:24:55.932204
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts import namespaced_call
    from ansible.module_utils.basic import AnsibleModule
    def mock_collect(module):
        return dict(a=1, b=2)
    original_namespaced_call = namespaced_call.call
    namespaced_call.call = mock_collect
    original_prefix = PrefixFactNamespace.prefix
    PrefixFactNamespace.prefix = ''
    module = AnsibleModule(argument_spec=dict())
    result = ansible_facts(module)
    assert result == dict(a=1, b=2)
    namespaced_call.call = original_namespaced_call
    PrefixFactNamespace.prefix = original_prefix


# Generated at 2022-06-13 00:25:07.148408
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.module_utils.facts import ansible_collector

    mock_ansible_module = MockAnsibleModule()

    all_collector_classes = default_collectors.collectors

    # don't add a prefix
    namespace = PrefixFactNamespace(namespace_name='ansible', prefix='')

    fact_collector = ansible_collector.get_ansible_collector(all_collector_classes=all_collector_classes,
                                                             namespace=namespace)

    facts_dict = fact_collector.collect(module=mock_ansible_module)

    assert facts_dict.get('system') == 'Mock_System_OS'

# Generated at 2022-06-13 00:25:18.603761
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts import collector
    import ansible.module_utils.facts.cache

    class FakeAnsibleModule:
        def __init__(self):
            self.params = {}
            self.cache = {'ansible_facts_cacheable_%s' % k: v for k, v in ansible.module_utils.facts.cache.FACT_CACHE.items()}

        def exit_json(self, ansible_facts):
            raise Exception('Fake AnsibleModule exiting with %s' % ansible_facts)


# Generated at 2022-06-13 00:25:26.893117
# Unit test for function ansible_facts
def test_ansible_facts():
    import sys
    import mock
    import unittest2
    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils.facts import ansible_collector
    from ansible.module_utils.facts import namespace

    class TestAnsibleModule(object):
        def __init__(self, module_args=None, fail_json=None, exit_json=None):
            self.params = {'gather_subset': module_args}
            self.fail_json = fail_json
            self.exit_json = exit_json

    class TestNamespace(namespace.FactNamespace):
        def get_vars(self, collector):
            return {'test': {'value': 'test value'}, 'empty': {'value': ''}}


# Generated at 2022-06-13 00:25:38.168390
# Unit test for function ansible_facts
def test_ansible_facts():
    ansible_facts_dict = ansible_facts(GatherSubset=['!all', 'network'])

    # check that only network facts are returned
    assert ansible_facts_dict.get('ansible_all_ipv4_addresses') is None
    assert ansible_facts_dict.get('ansible_device_links') is None
    assert ansible_facts_dict.get('ansible_default_ipv4') is None
    assert ansible_facts_dict.get('ansible_lo') is None
    assert ansible_facts_dict.get('ansible_machine_id') is None
    assert ansible_facts_dict.get('ansible_mounts') is None
    assert ansible_facts_dict.get('ansible_net_all_ipv4_addresses') is None
    assert ansible

# Generated at 2022-06-13 00:25:44.128959
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.facts.collector import BaseFactCollector

    class TestFactCollector(BaseFactCollector):
        name = 'test_collector'
        _fact_ids = set([u'test_fact'])
        _platform = u'test_platform'

        def collect(self, module=None, collected_facts=None):
            return {u'test_fact': u'testfact'}

    class FakeModule(object):
        params = {'gather_timeout': 10}

    module = AnsibleModule(argument_spec=dict())
    module.params = FakeModule().params
    module.params['gather_subset'] = ['all']

    all_collector_classes = default_collectors.collectors
    all_collector

# Generated at 2022-06-13 00:25:58.360394
# Unit test for function ansible_facts
def test_ansible_facts():
    import ansible.module_utils.facts.namespace_manager

    # Create an instance of FakeAnsibleModule to call the ansible_facts() function
    # with the FakeModule class.
    fake_module_class = FakeAnsibleModule(add_ansible_facts_module=False)
    module = fake_module_class.get_module_instance(param_check=False)

    # Prepare the filter specification and gather_subset for the call to ansible_facts.
    filter_spec = '*'
    gather_subset = ['all']
    gather_timeout = 10

    ansible_facts(module, gather_subset)

    # Check that ansible_facts() called the collect() method of the FakeCollector class
    # with the parameters above.

# Generated at 2022-06-13 00:26:08.634180
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts import get_all_collector_classes
    from ansible.module_utils.facts import get_collector_names

    default_collector_classes = default_collectors.collectors
    all_collector_classes = get_all_collector_classes(default_collector_classes=default_collector_classes)
    all_collector_names = get_collector_names(all_collector_classes=all_collector_classes)

    class DummyAnsibleModule:
        def __init__(self, params, *args, **kwargs):
            self.params = params

    # test with default args
    module = DummyAnsibleModule(params=dict())

    facts_dict = ansible_facts(module=module)

# Generated at 2022-06-13 00:26:15.356418
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts import ansible_facts

    module_name = 'test_ansible_facts'
    expected_facts = {'a': 1, 'b': 2}

    class TestModule(object):
        def __init__(self, module_name, *args, **kwargs):
            self.params = kwargs

    module = TestModule(module_name, **expected_facts)
    assert ansible_facts(module) == expected_facts

# Generated at 2022-06-13 00:26:24.238874
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils import basic
    from ansible.module_utils.facts import default_collectors

    test_module = basic.AnsibleModule(argument_spec={
            'gather_subset': dict(type='list', required=False, default=['all']),
            'gather_timeout': dict(type='int', required=False, default=10),
            'filter': dict(type='str', required=False, default='*'),
        },
        supports_check_mode=True)

    my_facts = ansible_facts(module=test_module, gather_subset=['all'])

    # try to get a fact that should exist with a gather_subset=all
    my_fact = my_facts.get('default_ipv4')
    assert my_fact is not None

# Generated at 2022-06-13 00:26:36.496672
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils import basic
    from ansible.module_utils.facts import timeout_util
    from ansible.module_utils.facts import timeout_monitor
    from ansible.module_utils.facts import default_collectors

    class StubModule(object):
        def __init__(self, params):
            self.params = params

    def test_impl():
        params = dict(
            gather_subset=['all'],
            gather_timeout=10,
            # filter=['all'],
        )

        module = basic.AnsibleModule(argument_spec={}, supports_check_mode=True)
        module.params = params

        # need to stub out timeouts otherwise test will fail
        timeouts = timeout_util.TimeoutManager()

# Generated at 2022-06-13 00:26:45.625884
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts import ansible_facts

    import ansible.module_utils.basic
    import ansible.module_utils.facts
    import os

    class FakeModule(object):
        def __init__(self):
            self.params = dict()
            self.params['gather_subset'] = [os.path.dirname(ansible.module_utils.facts.__file__)]
            self.params['filter'] = None
            self.params['gather_timeout'] = 10

    fake_module = FakeModule()

    ansible_facts_dict = ansible_facts(fake_module)

    assert 'ansible_python' in ansible_facts_dict

    # make sure chris's test fact sources aren't in the list
    assert 'ansible_test' not in ansible_facts_dict

# Generated at 2022-06-13 00:26:54.816305
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts import ansible_collector
    from ansible.module_utils._text import to_bytes

    from ansible.module_utils import basic
    import base64
    import json
    import os

    def fake_get_bin_path(arg, required=True, opt_dirs=[]):
        # we can't just return /bin/echo because the module may have
        # been copied to another path (Windows)
        return 'echo'

    class FakeModule(object):
        def __init__(self, **kwargs):
            self.params = kwargs


# Generated at 2022-06-13 00:27:06.455164
# Unit test for function ansible_facts
def test_ansible_facts():
    '''mock up a module to unit test ansible_facts compat script'''
    from ansible.module_utils.facts import collectors
    from ansible.module_utils.six import iteritems

    # create a mock module with a var to return dict for compare
    class MockAnsibleModule():
        def __init__(self, params=None):
            self.params = params or {}
            self.fail_json = fail_json

        def exit_json(self, *args, **kwargs):
            self.exit_args = args
            self.exit_kwargs = kwargs
            raise Exception("should not get here")

    class MockFactCollector(collectors.BaseFactCollector):
        def collect(self, module=None, collected_facts=None):
            collected_facts = collected_facts or {}

            collected_facts

# Generated at 2022-06-13 00:27:13.526109
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.basic import AnsibleModule

    class TestModule(AnsibleModule):
        def __init__(self, *args, **kwargs):
            self.params = {
                'gather_subset': '!all',
                'filter': '*',
            }
            super(TestModule, self).__init__(*args, **kwargs)

    test_module = TestModule()

    facts = ansible_facts(test_module)

    assert isinstance(facts, dict)
    assert isinstance(facts['default_ipv4'], dict)
    assert isinstance(facts['default_ipv4']['ipv4'], str)

# Generated at 2022-06-13 00:27:24.824020
# Unit test for function ansible_facts
def test_ansible_facts():
    '''function to run unit tests for ansible_facts.
    Not to be executed as part of normal operation
    '''

    from ansible.module_utils.basic import AnsibleModule

    def dummy_fail_json(msg):
        assert False, msg

    def dummy_exit_json(facts):
        return facts

    module = AnsibleModule(
        argument_spec=dict(
            gather_subset=dict(type='list', default=['all']),
            gather_timeout=dict(type='int', default=10),
            filter=dict(type='str', default='*')
        ),
        supports_check_mode=True,
    )

    module.fail_json = dummy_fail_json
    module.exit_json = dummy_exit_json

    facts = ansible_facts(module)

    assert not facts

# Generated at 2022-06-13 00:27:41.113116
# Unit test for function ansible_facts
def test_ansible_facts():
    # import the module to test
    from ansible.module_utils.facts import ansible_facts
    from ansible.module_utils.facts.namespace import add_prefix, remove_prefix

    # make a fake module instance to use for testing
    fake_module = FakeAnsibleModule()

    # call the function that was imported to test
    ansible_facts_dict = ansible_facts(module=fake_module, gather_subset=None)

    # make a copy of the results, with the prefix removed
    ansible_facts_dict_no_prefix = dict()
    for (k,v) in ansible_facts_dict.items():
        ansible_facts_dict_no_prefix[remove_prefix(k)] = v

    # now compare the results to what we expect

# Generated at 2022-06-13 00:27:51.768181
# Unit test for function ansible_facts
def test_ansible_facts():
    '''Utility function used in unittest to get ansible facts
    '''

    # override module_utils.facts.default_collectors.DEFAULT_GATHER_SUBSET with ['all'] to
    # ensure we load all fact collectors.
    # In Ansible 2.5, this is used to populate ansible_facts in ansible/module_utils/facts/__init__.py
    # In Ansible 2.6, it will be used to populate ansible_facts in ansible/module_utils/facts/collector.py
    default_collectors.DEFAULT_GATHER_SUBSET = ['all']

    from ansible.module_utils.facts.__init__ import AnsibleModule

    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True,
    )


# Generated at 2022-06-13 00:27:52.272337
# Unit test for function ansible_facts
def test_ansible_facts():
    pass

# Generated at 2022-06-13 00:27:59.114863
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils.six import PY3, integer_types
    from ansible.module_utils._text import to_native
    from ansible.module_utils.facts import ansible_facts
    import ansible.module_utils.facts

    class DummyAnsibleModule(object):
        def __init__(self):
            self._result = {}
            self._ansible_facts_cache = None

            self.params = {'gather_subset': ['all']}
            self.warnings = []

        def exit_json(self, **kwargs):
            self._result.update(kwargs)

        def fail_json(self, **kwargs):
            raise Exception(to_native(kwargs.get('msg', 'Failed')))


# Generated at 2022-06-13 00:28:01.859842
# Unit test for function ansible_facts
def test_ansible_facts():

    class MockModule(object):
        def __init__(self, params=None):
            self.params_dict = params if params is not None else {}

        def params(self):
            return self.params_dict

    mock_module = MockModule()

    facts_dict = ansible_facts(mock_module, gather_subset=['all'])
    assert len(facts_dict) > 0

# Generated at 2022-06-13 00:28:12.557499
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts.core import BasicFactCollector
    from ansible.module_utils.facts.core import FactNamespace
    from ansible.module_utils.facts.core import get_collector_namespace_classes
    from ansible.module_utils.facts.core import get_collector_classes

    collection = get_collector_namespace_classes()
    all_collector_classes = get_collector_classes(collection)

    class BareFactNamespace(FactNamespace):
        def __init__(self):
            super(BareFactNamespace, self).__init__(name='bare')
            self.ns = {}

    # No prefix to namespace
    namespace = PrefixFactNamespace(namespace_name='ansible', prefix='')

    # Make a fact collector for bare fact namespace
   

# Generated at 2022-06-13 00:28:21.069238
# Unit test for function ansible_facts
def test_ansible_facts():
    class FakeAnsibleModule():
        def __init__(self):
            self.params = dict()
            self._facts_cache = dict()
            self._ansible_facts = dict()

        def get_bin_path(self, arg, required=False, opt_dirs=[]):
            return "/bin/%s" % arg

    module = FakeAnsibleModule()
    module.params['gather_subset'] = ["all"]
    module.params['filter'] = "*"
    module.params['gather_timeout'] = 10

    assert isinstance(ansible_facts(module), dict)

# Generated at 2022-06-13 00:28:28.382038
# Unit test for function ansible_facts
def test_ansible_facts():

    class Module(object):

        def __init__(self):
            self.params = dict(gather_subset=['all'], filter='*')


    m = Module()
    facts = ansible_facts(m, 'all')

    # test some facts
    assert isinstance(facts['distribution'], str)
    assert isinstance(facts['distribution_version'], str)
    assert isinstance(facts['distribution_release'], str)
    assert isinstance(facts['distribution_major_version'], str)
    assert isinstance(facts['fqdn'], str)
    assert isinstance(facts['kernel'], str)
    assert isinstance(facts['machine'], str)
    assert isinstance(facts['os_family'], str)
    assert isinstance(facts['python_version'], str)

# Generated at 2022-06-13 00:28:38.960445
# Unit test for function ansible_facts
def test_ansible_facts():
    import ansible.module_utils.facts.ansible_facts_dumper
    import ansible.module_utils.facts.system.distribution
    import ansible.module_utils.facts.system.lsb

    class FakeAnsibleModule(object):
        def __init__(self, **kwargs):
            self.params = kwargs

        def fail_json(self, *args, **kwargs):
            raise Exception(kwargs)

    # Verify default when gather_subset not specified.
    ansible_facts = ansible_facts(module=None)
    assert ansible_facts['module_setup']['filter'] == '*'
    assert 'ansible' in ansible_facts and 'system' in ansible_facts['ansible']

# Generated at 2022-06-13 00:28:50.584971
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts.collector import FactsCollector
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils.facts import ansible_collector
    from ansible.module_utils._text import to_bytes
    import json
    import types

    class AnsibleModuleMock:

        def __init__(self):
            self.params = {'gather_subset': ['all']}


# Generated at 2022-06-13 00:29:07.890896
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts.collector import BaseFactCollector

    class FakeCollector(BaseFactCollector):
        def collect(self, module=None, collected_facts=None):
            self.collected_facts = {}
            return self.collected_facts

    fake_collector = FakeCollector()
    collectors = [fake_collector]

    class FakeModule(object):
        def __init__(self):
            self.params = {'gather_subset': ['all']}

    fake_module = FakeModule()
    fact_collector = ansible_collector.get_ansible_collector(all_collector_classes=collectors,
                                                             filter_spec='',
                                                             namespace=None)
    fact_collector.collect(fake_module)

    assert fake_

# Generated at 2022-06-13 00:29:16.973031
# Unit test for function get_all_facts
def test_get_all_facts():
    '''
    Warning, this is a crappy unit test, but of the 'if it runs too long it fails' variety.
    '''
    import ansible.module_utils.facts.legacy_collectors as legacy_collectors
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.six import StringIO

    class MockModule:  # pylint: disable=too-few-public-methods
        def __init__(self, params_dict):
            self.params = params_dict

    fake_filter = '*'
    fake_gather_subset = ['all']
    fake_module = MockModule({'filter': fake_filter, 'gather_subset': fake_gather_subset})

    # do not force the ansible fact collector to be in the path
    save

# Generated at 2022-06-13 00:29:17.932613
# Unit test for function ansible_facts
def test_ansible_facts():
    # TODO
    pass


# Generated at 2022-06-13 00:29:28.276520
# Unit test for function ansible_facts
def test_ansible_facts():
    import ansible.modules.system.setup as setup

    # patch module to avoid  'I/O operation on closed file' errors during test
    setattr(setup, 'file', open('/dev/null', 'w'))
    setattr(setup, 'open_file', open('/dev/null', 'w'))

    # make sure the desired fact exists
    fact_d = ansible_facts(setup)
    assert 'default_ipv4' in fact_d

    # make sure an invalid fact is not in the result
    assert 'nonesuch' not in fact_d

    # make sure a filtered out fact is not in the result
    assert 'ipv4_interface' not in fact_d

    # make sure we get the filtered fact if we ask for it
    fact_d = ansible_facts(setup, ['network'])

# Generated at 2022-06-13 00:29:33.316678
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils.facts import get_all_facts
    from ansible.module_utils.facts.system.distribution import DistributionFactCollector
    module = AnsiModule()
    facts = get_all_facts(module)
    assert 'distribution' in facts
    assert isinstance(facts['distribution'], DistributionFactCollector)


# Generated at 2022-06-13 00:29:43.605964
# Unit test for function get_all_facts
def test_get_all_facts():
    import ansible.module_utils.facts.namespace
    import ansible.module_utils.facts
    try:
        from unittest.mock import patch, MagicMock
    except ImportError:
        from mock import patch, MagicMock
    module = MagicMock()
    module.params = {'gather_subset': ['all', 'network']}
    module.params['gather_subset'].append('software')


# Generated at 2022-06-13 00:29:54.784550
# Unit test for function ansible_facts
def test_ansible_facts():
    import os
    import sys
    import pytest
    sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'test'))
    from test_module_utils.ansible_module_mock import AnsibleModuleMock
    from ansible.module_utils.facts.collector import get_file_content
    from ansible.module_utils.facts.cache import FactsCache

    # No gather_subset param is given
    module = AnsibleModuleMock()
    facts = ansible_facts(module)
    assert '' not in facts
    # 'os' should be a fact
    assert 'os' in facts
    # 'ansible_os' is not valid
    assert 'ansible_os' not in facts
    assert 'architecture' in facts

# Generated at 2022-06-13 00:30:02.569480
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts import ansible_facts
    from ansible.module_utils.facts import is_collection_fragment
    from ansible.module_utils.facts import get_suitable_check_file
    from ansible.module_utils.facts import get_collection_fragment_spec
    from ansible.module_utils.facts import get_default_filter_spec

    import socket
    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils.facts import ansible_collector
    from ansible.module_utils._text import to_bytes

    ansible_facts(MockModule(
        dict(gather_subset=None, gather_timeout=10, filter=None)))

# Generated at 2022-06-13 00:30:14.594434
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils._text import to_text
    from ansible.module_utils.basic import AnsibleModule
    import os
    import sys

    # wrap sys.exit so that it throws an exception when called
    def fake_sys_exit(*args):
        raise Exception("sys.exit called")
    sys.exit = fake_sys_exit

    # create a fake ansible module for testing
    class FakeAnsibleModule(object):
        def __init__(self):
            self.params = {}
            self.env = None

        def _load_params(self):
            ''' load fake params into the module '''
            self.params['filter'] = 'ansible_*'
            self.params['gather_subset'] = ['all']
            self.params['gather_timeout'] = 10


# Generated at 2022-06-13 00:30:21.567384
# Unit test for function ansible_facts
def test_ansible_facts():
    '''Test harness for ansible_facts function'''
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts import default_collectors

    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.collector import CacheableFactCollector
    from ansible.module_utils.facts.collector import ComponentFactCollector
    from ansible.module_utils.facts.collector import FactsCollector
    from ansible.module_utils.facts.utils import get_file_content
    from ansible.module_utils.facts.utils import get_file_lines
    from ansible.module_utils.facts.utils import get_mount

# Generated at 2022-06-13 00:30:42.635722
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.common._collections_compat import Mapping

    import mock
    mock_module = mock.Mock()
    mock_module.params = {'gather_subset': ['all']}
    facts_dict = ansible_facts(mock_module)
    assert isinstance(facts_dict, Mapping)

# Generated at 2022-06-13 00:30:52.432221
# Unit test for function ansible_facts
def test_ansible_facts():
    # Start with a simple test, with no transformed facts
    # Create a fake AnsibleModule with a single gather_subset param
    module = FakeModule(params={'gather_subset': ['!all', 'network']})
    facts = ansible_facts(module)
    assert 'ipv4' in facts

    # Next create an AnsibleModule with a single gather_subset param
    # that should trigger a transformed fact
    module = FakeModule(params={'gather_subset': ['all', 'network']})
    facts = ansible_facts(module)
    assert 'default_ipv4' in facts
    assert 'ipv4' not in facts


# Generated at 2022-06-13 00:30:58.974051
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts.virtual import VirtualCollector
    from ansible.module_utils.facts.system import SystemCollector
    from ansible.module_utils.facts.network import NetworkCollector

    import mock
    from ansible.module_utils.basic import AnsibleModule

    def test_collect(self, module):
        return {'ansible_' + self.namespace_name + '_' + self.fact_name(): self.fact()}

    class MyMockVirtualCollector(VirtualCollector):
        def __init__(self):
            self.fact_name = mock.MagicMock(return_value='virtual')
            self.fact = mock.MagicMock(return_value='virtual')
            self.collect = test_collect


# Generated at 2022-06-13 00:31:10.063279
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts import ModuleFacts
    from ansible.module_utils.facts import namespace
    from ansible.module_utils.facts.utils import get_file_content
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.collector.hardware import Hardware
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts.collector import DefaultCollector

    import types

    class MockAnsibleModule(object):
        def __init__(self):
            self.params = {'filter': '*', 'gather_subset': []}


# Generated at 2022-06-13 00:31:21.604994
# Unit test for function ansible_facts
def test_ansible_facts():
    import ansible.module_utils.facts.namespace as namespace_module
    import ansible.module_utils.facts.collector as collector_module
    import ansible.module_utils.facts.utils as facts_module
    from ansible.module_utils.facts.namespace import PrefixFactNamespace

    class MockModule:
        def __init__(self, params, facts):
            self.params = params
            self.facts = facts

    class MockFact:
        def __init__(self, fact_name, fact_value):
            self.fact_name = fact_name
            self.fact_value = fact_value

    class MockCollector:
        def __init__(self, namespace, fact_classes, fact_names, fact_values):
            self.namespace = namespace
            self.fact_classes = fact_classes

# Generated at 2022-06-13 00:31:25.346216
# Unit test for function ansible_facts
def test_ansible_facts():
    import pytest

    from ansible.compat import mock
    from ansible.module_utils.facts.utils import get_file_lines

    # unit test for 2.0-2.2 api (no gather_subset arg)
    default_gather_subset = ['all']
    gather_timeout = 10
    filter_spec = '*'

    # the below is for 2.4 or later, which requires a gather_subset arg
    # NOTE: gather_timeout and filter_spec are only used when gather_subset is specified.
    # gather_timeout = module.params.get('gather_timeout', 10)
    # filter_spec = module.params.get('filter', '*')

    # create and initialize a mock module
    mocked_module = mock.Mock()

# Generated at 2022-06-13 00:31:33.740266
# Unit test for function ansible_facts
def test_ansible_facts():
    # import module
    from ansible.module_utils.basic import AnsibleModule

    # prepare arguments
    args = dict(
        gather_subset=['all'],
        gather_timeout=10,
        filter='*'
    )

    # initialize AnsibleModule
    module = AnsibleModule(argument_spec={})

    # prepare test data

# Generated at 2022-06-13 00:31:44.383519
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts.facts import Facts
    from ansible.module_utils.facts.collector.text import TextFactCollector
    from ansible.module_utils.facts.collector.network import NetworkFactCollector
    from ansible.module_utils.facts.namespace import PrefixFactNamespace


    from ansible.module_utils._text import to_bytes
    import os
    import pytest
    import sys
    import tempfile

    f_out, f_path = tempfile.mkstemp()
    os.close(f_out)

    f = os.fdopen(os.open(f_path, os.O_WRONLY), 'wb')


# Generated at 2022-06-13 00:31:55.783847
# Unit test for function ansible_facts
def test_ansible_facts():
    import json
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils.facts import ansible_collector
    from ansible.module_utils.facts import namespace_manager
    class mock_module:
        def __init__(self):
            self.params = {}
        def params_dict(self):
            return self.params
    mod = mock_module()
    mod.params['filter'] = '*'

    gather_subset = mod.params['gather_subset']
    gather_timeout = mod.params.get('gather_timeout', 10)
    filter_spec = mod.params.get('filter', '*')


# Generated at 2022-06-13 00:32:06.050570
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts import default_collectors

    minimal_gather_subset = frozenset(['apparmor', 'caps', 'cmdline', 'date_time',
                                       'distribution', 'dns', 'env', 'fips', 'local',
                                       'lsb', 'pkg_mgr', 'platform', 'python', 'selinux',
                                       'service_mgr', 'ssh_pub_keys', 'user'])

    # Don't add a prefix
    namespace = PrefixFactNamespace(namespace_name='ansible', prefix='')

    # Set up the AnsibleModule mock
    class AnsibleModuleMock(object):
        def __init__(self):
            self.params = {'gather_subset': ['all']}


# Generated at 2022-06-13 00:32:46.276544
# Unit test for function ansible_facts
def test_ansible_facts():
    import ansible.module_utils.facts.facts as facts
    import ansible.module_utils.facts.collectors as collectors
    module = {}
    module['faker'] = True
    module['faker_facts'] = True
    module['ansible_facts'] = {}
    module['params'] = {'gather_subset': ['hardware']}

    def test_module_wrapper(module, *args, **kwargs):
        return module

    facts_dict = ansible_facts(module, ['hardware'])
    assert isinstance(facts_dict, dict) is True
    assert isinstance(facts_dict['ansible_system'], str) is True
    assert isinstance(facts_dict['ansible_distribution'], str) is True

# Generated at 2022-06-13 00:32:59.109557
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts import ansible_facts

    import mock
    import sys

    class FakeModule():
        '''
        Fake class to be used as ansible module
        '''
        def __init__(self, **kwargs):
            for key, value in kwargs.items():
                self.__dict__[key] = value

    class FakeAnsibleModule():
        '''
        Fake class to be used as argument for the ansible_facts function
        '''
        def __init__(self, module):
            self.module = module

    class FakeFactCollector():
        '''
        Fake class to be used as return value of FakeAnsibleCollector.get_ansible_collector
        '''

# Generated at 2022-06-13 00:33:09.965106
# Unit test for function ansible_facts
def test_ansible_facts():
    import unittest

    # Mock out the AnsibleModule
    # Replace the MOCK_MODULE object with your test object here
    class MOCK_MODULE(object):
        def __init__(self, params):
            self.params = params

    # How to mock up the module_utils functions this function expects
    # to access.

    import sys
    # Mock out the ANSIBLE_COLLECTION_INCLUDE_PATHS
    sys.modules['ansible'] = type('module', (), {'collections': type('collection', (), {'collection_paths': ['/mock/dir1', '/mock/dir2']})})

# Generated at 2022-06-13 00:33:13.293130
# Unit test for function get_all_facts
def test_get_all_facts():
    import json
    import mock

    fake_module = mock.MagicMock()
    fake_module.params = {'gather_subset': '!all'}
    res = get_all_facts(fake_module)
    print(json.dumps(res, indent=4))


# Generated at 2022-06-13 00:33:20.320350
# Unit test for function get_all_facts
def test_get_all_facts():
    class AnsibleModule(object):
        def __init__(self, params):
            self.params = params

    module = AnsibleModule({'gather_subset': ['all']})
    facts = get_all_facts(module)
    assert facts
    assert isinstance(facts, dict)
    assert len(facts) > 0
    assert 'default_ipv4' in facts



# Generated at 2022-06-13 00:33:31.065869
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts import ansible_facts
    # Just smoke test it
    import ansible.module_utils.facts.collector.platform
    assert ansible_facts({'gather_subset': ['all']})
    assert ansible_facts({'gather_subset': ['all'], 'filter': '*'})
    assert ansible_facts({'gather_subset': ['all'], 'filter': 'a*'})
    assert ansible_facts({'gather_subset': ['all'], 'filter': ['a*', 'b*']})
    assert ansible_facts({'gather_subset': ['all'], 'filter': ['a*', 'b*'], 'gather_timeout': 20})



# Generated at 2022-06-13 00:33:42.167182
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils._text import to_text
    from ansible.module_utils.facts import ansible_collector
    import ansible.module_utils.facts.system.distribution
    import ansible.module_utils.facts.system.platform
    # Create a mock instance of AnsibleModule
    class MockAnsibleModule(object):
        def __init__(self):
            self.facts = {}
        def fail_json(self, **kwargs):
            assert False

    mock_module = MockAnsibleModule()
    # Collect the facts using AnsibleModule
    mock_module.facts = ansible_facts(module=mock_module)

    # Verify the platform fact is set and equal to the os name
    assert 'platform' in mock_module.facts
    assert mock_module.facts['platform'] == ans

# Generated at 2022-06-13 00:33:51.682893
# Unit test for function ansible_facts
def test_ansible_facts():
    # Mock ansible module
    import ansible.module_utils.facts
    class AnsibleModuleMock(object):
        def __init__(self, params):
            self.params = params
        def fail_json(self, msg):
            self.msg = msg

    params = {
        'gather_subset': ['all'],
        'gather_timeout': 10,
        'filter': '*'
    }
    am = AnsibleModuleMock(params)
    # Run test
    facts = ansible_facts(am)
    # Assert at least one fact was returned
    assert len(facts) == 1
    for fact in facts:
        # Assert fact is not empty
        assert facts[fact]

# Generated at 2022-06-13 00:33:56.446932
# Unit test for function get_all_facts
def test_get_all_facts():
    try:
        import unittest2 as unittest
    except ImportError:
        import unittest
    import ansible.module_utils.facts.collector

    class MockModule(object):
        class params(object):
            gather_subset = None

    mock_module = MockModule()
    module_facts = ansible.module_utils.facts.get_all_facts(mock_module)
    assert module_facts

# Generated at 2022-06-13 00:33:56.899161
# Unit test for function ansible_facts
def test_ansible_facts():

    pass