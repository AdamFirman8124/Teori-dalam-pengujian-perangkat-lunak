

# Generated at 2022-06-13 00:24:17.359518
# Unit test for function ansible_facts
def test_ansible_facts():
    '''Unit test for function ansible_facts

    Test that ansible_facts can be called before the ansible api class is imported.
    '''
    # Create a mock module for testing
    # pylint: disable=too-few-public-methods
    class MockModule(object):
        def __init__(self):
            self.params = {}
    # pylint: enable=too-few-public-methods
    mock_module = MockModule()
    facts_dict = ansible_facts(mock_module)
    assert isinstance(facts_dict, dict)
    assert 'os_family' in facts_dict
    assert facts_dict['os_family'] == 'Linux'

# Generated at 2022-06-13 00:24:26.779160
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.basic import AnsibleModule
    import sys

    module_args = dict()
    # running with minimal_gather_subset due to issue with the gather_subset arg in 2.3
    # https://github.com/ansible/ansible/issues/36003
    module_args['gather_subset'] = ['min']
    module_args['filter'] = '*'

    module = AnsibleModule(argument_spec=module_args)

    import pprint
    pprint.pprint(ansible_facts(module=module))
    print(ansible_facts(module=module))


if __name__ == '__main__':
    test_ansible_facts()

# Generated at 2022-06-13 00:24:28.796224
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts import ansible_facts
    assert ansible_facts(module=None)

# Generated at 2022-06-13 00:24:36.713910
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts import module_setup

    gather_subset = ['all']
    gather_timeout = 10
    filter_spec = '*'

    # unit test imports from ansible.module_utils.facts.module_setup
    ansible_module = module_setup(gather_subset=gather_subset,
                                  gather_timeout=gather_timeout,
                                  filter=filter_spec)

    # unit test imports from ansible.module_utils.facts.ansible_facts
    # cannot use @patch on ansible_facts since ansible_facts is decorator
    ansible_facts = ansible_facts(ansible_module, gather_subset)

    assert isinstance(ansible_facts, dict)

    # check that returned dictionary has some expected keys

# Generated at 2022-06-13 00:24:46.348363
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts import get_all_facts

    class FakeModule(object):
        def __init__(self, params):
            self.params = params
            self._name = params.get('module_name', 'fake_module')

    test_params_1 = {'module_name': 'fake_module_1',
                     'gather_subset': ['all']}
    test_params_2 = {'module_name': 'fake_module_2',
                     'gather_subset': ['!all', 'foo', 'bar']}
    test_params_3 = {'module_name': 'fake_module_3',
                     'gather_subset': ['!all'],
                     'filter': 'ansible_distribution_*'}

# Generated at 2022-06-13 00:24:49.870239
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts import get_all_facts

    all_facts = get_all_facts()
    ansible_facts = ansible_facts(all_facts)
    print(ansible_facts)

# Generated at 2022-06-13 00:24:58.020492
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.basic import AnsibleModule
    import json

    # minimal viable param set
    gather_subset = ['min']
    module_args = {'gather_subset': gather_subset}
    module = AnsibleModule(argument_spec=module_args)

    # run and test the facts
    facts_dict = ansible_facts(module)
    assert facts_dict['architecture'] == 'x86_64'
    assert facts_dict['date_time']['timezone'] == 'UTC'
    assert len(facts_dict['distribution']) == 1
    assert facts_dict['distribution'][0]['name'] == 'Ubuntu'
    assert facts_dict['fips']['status']

    # run and test some specific facts

# Generated at 2022-06-13 00:25:07.986395
# Unit test for function get_all_facts
def test_get_all_facts():

    from ansible.module_utils.facts.namespace import DEFAULT_GATHER_SUBSET

    from ansible.module_utils.facts import fallback_facts_collector
    from ansible.module_utils.facts import system_facts_collector
    from ansible.module_utils.facts import network_facts_collector
    from ansible.module_utils.facts import virtual_facts_collector
    from ansible.module_utils.facts import hardware_facts_collector
    from ansible.module_utils.facts import default_collectors

    from ansible.module_utils._text import to_bytes

    from ansible.module_utils.facts.virtual.virtualbox import VirtualBox
    from ansible.module_utils.facts.virtual.vmware import VMware

# Generated at 2022-06-13 00:25:19.368108
# Unit test for function ansible_facts
def test_ansible_facts():

    from ansible.module_utils.facts.virtual.openbsd import OpenBSDVirtual
    from ansible.module_utils.facts.system.distribution import Distribution
    from ansible.module_utils.facts.other.fips import Fips
    from ansible.module_utils.facts.system.distribution import DistributionRedHat

    class FakeModule:
        def __init__(self):
            self.params = {}

    class FakeAnsibleModule:
        def __init__(self, params):
            self.params = params

    module = FakeModule()
    ansible_module = FakeAnsibleModule({})

    # get_all_facts
    returned_facts = get_all_facts(module)
    assert returned_facts

    # ansible_facts
    returned_facts = ansible_facts(ansible_module)


# Generated at 2022-06-13 00:25:24.579313
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils.facts.namespace import PrefixFactNamespace

    class TestModule(object):
        def __init__(self, gather_subset):
            self.params = {'gather_subset': gather_subset}

    test_module = TestModule(gather_subset=['all'])
    facts = get_all_facts(test_module)

    assert facts is not None
    assert 'ansible_all_ipv4_addresses' in facts



# Generated at 2022-06-13 00:25:38.315944
# Unit test for function ansible_facts
def test_ansible_facts():
    import sys
    import io

    import pytest
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils.facts import ansible_collector
    from ansible.module_utils.facts.ansible_collector import AnsibleCollector

    from ansible.module_utils.facts import ansible_2_0_compat as compat
    from ansible.module_utils.facts.ansible_2_0_compat import AnsibleModule

    import ansible.module_utils.facts
    module_utils_facts_ansible_2_0_compat = ansible.module_utils.facts.ansible_2_0_compat


# Generated at 2022-06-13 00:25:46.994658
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.modules.system import setup
    from ansible_collections.ansible.community.plugins.module_utils.facts.network.base import NetworkCollector
    from ansible_collections.ansible.community.plugins.module_utils.facts.network.interfaces import InterfacesFactCollector
    from ansible_collections.ansible.community.plugins.module_utils.facts.network.interfaces import BOND_MASTER_KEYWORDS
    from ansible_collections.ansible.community.plugins.module_utils.facts.network.interfaces import VLAN_MASTER_KEYWORDS
    from ansible_collections.ansible.community.plugins.module_utils.module_common import ModuleBase

    from ansible_collections.ansible.community.plugins.module_utils._text import to_text

    setup_module

# Generated at 2022-06-13 00:25:57.563518
# Unit test for function get_all_facts
def test_get_all_facts():

    from ansible.module_utils.facts import module_proto
    # Get our test module instance
    module = module_proto.init_module_arg_spec(argument_spec={})
    module.params['gather_subset'] = ['all']

    # Get the facts
    facts_dict = get_all_facts(module)

    assert isinstance(facts_dict, dict)
    assert 'default_ipv4' in facts_dict
    assert 'all_ipv4_addresses' in facts_dict
    assert 'fqdn' in facts_dict
    assert 'distribution' in facts_dict
    assert 'domain' in facts_dict
    assert 'distribution_version' in facts_dict

# Generated at 2022-06-13 00:26:08.006681
# Unit test for function ansible_facts
def test_ansible_facts():
    class MockModule:
        def __init__(self):
            self.params = {}
            self.fail_json = lambda x: 'fail_json'

    module = MockModule()
    facts_dict = ansible_facts(module)
    assert(isinstance(facts_dict, dict))
    assert('distribution' in facts_dict)
    assert('distribution' in facts_dict)
    assert('system' in facts_dict)
    assert('pkg_mgr' in facts_dict)
    assert('python' in facts_dict)
    assert('lsb' in facts_dict)
    assert('platform' in facts_dict)
    assert('fips' in facts_dict)
    assert('date_time' in facts_dict)
    assert('ssh_pub_keys' in facts_dict)

# Generated at 2022-06-13 00:26:19.126814
# Unit test for function ansible_facts
def test_ansible_facts():
    import ansible.module_utils.facts
    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils.facts import ansible_collector

    # don't want to actually run collectors.
    # so patch ansible.module_utils.facts
    saved_collectors = ansible.module_utils.facts.collectors
    ansible.module_utils.facts.collectors = default_collectors.collectors
    # patch ansible_collector.get_ansible_collector
    old_ansible_collector = ansible_collector.get_ansible_collector


# Generated at 2022-06-13 00:26:24.323965
# Unit test for function ansible_facts
def test_ansible_facts():

    from ansible.module_utils.facts.virtual import VirtualFactCollector
    from ansible.module_utils.facts.system import SystemFactCollector
    from ansible.module_utils.facts.distribution import DistributionFactCollector

    class MockModule(object):
        def __init__(self):
            self.params = dict()

    module = MockModule()
    module.params['gather_subset'] = ['!all', 'virtual']

    facts = ansible_facts(module=module)
    assert SubsetOf(dict(ansible_virtual=VirtualFactCollector.virtual)) == facts

    facts = ansible_facts(module=module, gather_subset=['!all', 'system'])
    assert SubsetOf(dict(ansible_system=SystemFactCollector.system)) == facts

    facts = ansible_facts

# Generated at 2022-06-13 00:26:36.532795
# Unit test for function ansible_facts
def test_ansible_facts():
    # mock the module being used to gather facts.
    import sys
    import types

    # mock the AnsibleModule class
    class AnsibleModule(object):
        def __init__(self, **kwargs):
            self.params = kwargs

    # mock the builtins module
    class MockBuiltinsModule(types.ModuleType):
        def __init__(self, *args, **kwargs):
            pass

        def getattr(self, key, default=None):
            return None

        def hasattr(self, name):
            return None

        def __getattr__(self, attr):
            return None

    # mock the sys module
    sys.modules['builtins'] = MockBuiltinsModule('builtins')
    # import the module being tested
    from ansible.module_utils.facts import ansible as facts_module

# Generated at 2022-06-13 00:26:40.853806
# Unit test for function ansible_facts
def test_ansible_facts():
    with pytest.raises(TypeError) as excinfo:
        ansible_facts()
    assert 'ansible_facts() takes exactly 2 arguments (0 given)' == str(excinfo.value)
    # TODO: need to mock module, how to do that in parametrized function?

# Generated at 2022-06-13 00:26:48.020407
# Unit test for function get_all_facts
def test_get_all_facts():
    import copy
    import pytest
    from ansible.module_utils.facts.network.base import NetworkCollector
    from ansible.module_utils.facts.system.base import SystemCollector
    from ansible.module_utils.facts.processor.base import ProcessorCollector
    from ansible.module_utils.facts.virtual.base import VirtualCollector
    from ansible.module_utils.facts.system.distribution import DistributionCollector
    from ansible.module_utils.facts.system.fips import FipsCollector

    class FakeModule(object):
        def __init__(self, gather_subset):
            params = dict(
                gather_subset=gather_subset,
                gather_timeout=1,
                filter='*'
            )
            self.params = params

    # If a collector is added or

# Generated at 2022-06-13 00:26:56.299598
# Unit test for function get_all_facts
def test_get_all_facts():
    '''
    Test to see if function get_all_facts returns a dict.
    '''
    try:
        import ansible
        from ansible.module_utils.facts import get_all_facts
        from ansible.module_utils.basic import AnsibleModule
    except ImportError:
        # we're not in an ansible module
        assert False

    # make this a dict, not a set, for compatibility if/when callers pass it to get_all_facts
    gather_subset = ['all']

    # make an AnsibleModule without fail_json
    module = AnsibleModule(argument_spec={'gather_subset': {'type': 'list', 'default': gather_subset}})

    facts = get_all_facts(module)

    # we can't deterministically control what facts are returned, but we can

# Generated at 2022-06-13 00:27:07.164464
# Unit test for function ansible_facts
def test_ansible_facts():
    from unittest import TestCase
    from ansible.module_utils.facts.default_collectors import DictCollector
    from ansible.module_utils.facts.namespace import PrefixFactNamespace

    class TestModule(TestCase):

        def test__gather_all_facts(self):
            # Test with empty subset
            gather_subset = []
            facts_dict = ansible_facts(module=self, gather_subset=gather_subset)
            expected = {}
            self.assertEqual(expected, facts_dict)

            # Test with 'all' subset
            gather_subset = ['all']
            facts_dict = ansible_facts(module=self, gather_subset=gather_subset)
            expected = {}
            self.assertEqual(expected, facts_dict)

            #

# Generated at 2022-06-13 00:27:14.972214
# Unit test for function get_all_facts
def test_get_all_facts():
    import sys
    import os
    import tempfile

    # make sure function is defined
    assert get_all_facts is not None

    # Make fake module
    module_dir = tempfile.mkdtemp()
    module_path = os.path.join(module_dir, 'ansible_local.py')
    with open(module_path, 'wt') as f:
        f.write('from ansible.module_utils.facts import get_all_facts\n')
        f.write('from ansible.module_utils.facts import ansible_collector\n')
        f.write('from ansible.module_utils.facts.collector import BaseFactCollector\n')
        f.write('from ansible.module_utils.facts.namespace import PrefixFactNamespace\n')

# Generated at 2022-06-13 00:27:25.879724
# Unit test for function ansible_facts
def test_ansible_facts():

    # Mock out module_utils.facts.ansible_collector.get_ansible_collector
    module_utils_facts_ansible_collector_get_ansible_collector = \
        'ansible.module_utils.facts.ansible_collector.get_ansible_collector'
    ansible_collector.get_ansible_collector = \
        Mock(return_value=MagicMock(collect=lambda module_: {'test_fact': 'test_value'}))

    # Mock out module_utils.facts.default_collectors.collectors
    module_utils_facts_default_collectors_collectors = \
        'ansible.module_utils.facts.default_collectors.collectors'
    import sys

# Generated at 2022-06-13 00:27:36.485070
# Unit test for function get_all_facts
def test_get_all_facts():
    # patch this out since we don't want to wait 10 seconds
    import ansible.module_utils.facts.system.distribution
    ansible.module_utils.facts.system.distribution.Distribution.timeout = 0.01

    from ansible.module_utils.facts import namespace as fact_namespace
    import ansible.module_utils.facts.system as system_facts
    from ansible.module_utils._text import to_bytes

    # import the minimal collectos we actually want to test
    import ansible.module_utils.facts.system.distribution
    import ansible.module_utils.facts.system.pkg_mgr
    import ansible.module_utils.facts.system.platform
    import ansible.module_utils.facts.system.service_mgr
    import ansible.module_utils.facts.system.user

# Generated at 2022-06-13 00:27:48.687977
# Unit test for function get_all_facts
def test_get_all_facts():
    class FakeModule(object):
        def __init__(self, gather_subset=None):
            self._module_params = {}
            if gather_subset:
                self._module_params['gather_subset'] = gather_subset

        def params(self):
            return self._module_params

    # Verify that we get a dict back
    module = FakeModule()
    result = get_all_facts(module)
    assert isinstance(result, dict)
    assert result

    # Try a valid gather_subset param
    module = FakeModule(['hardware'])
    result = get_all_facts(module)
    assert isinstance(result, dict)
    assert result

    # Try an invalid gather_subset param
    module = FakeModule(['invalid_type'])
    result = get_all_

# Generated at 2022-06-13 00:27:57.674587
# Unit test for function ansible_facts
def test_ansible_facts():

    from ansible.module_utils.facts import timeout_gather_facts
    from ansible.module_utils.facts import ansible_facts

    from ansible.module_utils.facts.network.linux import ip_by_name
    from ansible.module_utils.facts.network.linux import ip_by_name_v2
    from ansible.module_utils.facts.network.linux import ip_by_name_v3

    # setup fakes

# Generated at 2022-06-13 00:28:04.816888
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts import ModuleFacts
    from ansible.module_utils.facts.collector.test.test_module_utils_facts_ansible_collector import TestCaseModuleUtilsFactsAnsibleCollector

    mock_module = TestCaseModuleUtilsFactsAnsibleCollector.create_ansible_module(params={'gather_subset': ['all']})

    # disable test collector
    module_facts = ModuleFacts(module=mock_module)
    module_facts.collector_classes = {}
    module_facts._normalize_collector_classes()

    # add our own collector
    module_facts.collector_classes['test_collector'] = TestCaseModuleUtilsFactsAnsibleCollector.create_collector_class()

    # gather facts
    facts = ans

# Generated at 2022-06-13 00:28:11.303463
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(argument_spec={})

    results = get_all_facts(module=module)

    assert 'fact_namespace' in results
    assert results['fact_namespace'] == 'ansible'

    assert 'ansible_all_ipv4_addresses' in results
    assert isinstance(results['ansible_all_ipv4_addresses'], list)


# Generated at 2022-06-13 00:28:22.510349
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts import cache

    # create a fake module object
    class Options:
        gather_subset = '!all'
        gather_timeout = 10

    class AnsibleModule:
        def __init__(self, argument_spec, bypass_checks=False, 
                no_log=False, check_invalid_arguments=True, mutually_exclusive=(), required_together=(), 
                required_one_of=(), add_file_common_args=False, supports_check_mode=False, 
                required_if=()):
            self.argument_spec = argument_spec
            self.params = Options()

        def exit_json(self, **kwargs):
            pass


# Generated at 2022-06-13 00:28:28.070240
# Unit test for function ansible_facts
def test_ansible_facts():
    module = MockAnsibleModule()

    assert ansible_facts(module) == {'default_ipv4': {'address': '1.2.3.4', 'network': '1.2.3.0'}}
    assert ansible_facts(module, gather_subset='!network') == {'default_ipv4': {'address': '1.2.3.4'}}



# Generated at 2022-06-13 00:28:44.418739
# Unit test for function ansible_facts
def test_ansible_facts():
    import sys
    sys.path.append('../')
    from ansible.module_utils import facts
    import mock
    mocked_ansible_module = mock.Mock()
    mocked_ansible_module.params = {
        'gather_subset': ['all'],
        'gather_timeout': 10
    }

    # Patch module_utils.facts.py
    fact_dic = {}
    fact_dic.update(facts.ansible_facts(mocked_ansible_module))

    assert fact_dic['distribution'] == 'Darwin'

# Generated at 2022-06-13 00:28:47.804753
# Unit test for function ansible_facts
def test_ansible_facts():
    class AnsibleModuleFake(object):
        params = {'filter': '*', 'gather_timeout': 10}

    assert ansible_facts(module=AnsibleModuleFake()) is not None

# Generated at 2022-06-13 00:28:57.637833
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts._text_facts import _default_collectors, _minimal_collectors, \
        _collector_classes, _collectors_as_namespace_dicts, _collector_classes_as_namespace_dicts, \
        _collector_keys, _collector_namespaces, _collector_classes_as_dict, _collector_as_namespace_dict, \
        _collector_class_as_dict, _get_collector_classes, get_collector_class, _get_collector_keys, \
        _get_collector_namespaces, _get_collector_class_path
    from ansible.module_utils.facts import default_collectors, ansible_collector, \
        _AnsibleCollector, _AnsibleCollectorMeta
   

# Generated at 2022-06-13 00:29:05.028983
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils.facts.facts import Facts
    import ansible.compat.tests.mock

    class AnsibleModule(object):
        def __init__(self):
            self.params = {
                'gather_subset': ['all'],
                'gather_timeout': 10,
                'filter': '*'
            }

    test_module = AnsibleModule()
    current_facts = Facts(ansible_facts(test_module, gather_subset=['all']))
    assert 'cmdline' in current_facts['ansible_facts']

# Generated at 2022-06-13 00:29:14.413786
# Unit test for function ansible_facts
def test_ansible_facts():
    import json
    import sys
    # mock
    class MockModule:
        def __init__(self, params):
            self.params = params
        def get_bin_path(self, name, required=False, opt_dirs=[]):
            if not name == 'myapp':
                return None
            return 'mockbin/myapp'

    # test all info
    params = {
        'filter': '*',
    }
    module = MockModule(params=params)
    result = ansible_facts(module)
    #print(json.dumps(result, sort_keys=True, indent=4))
    assert 'myapp' in result

    # test with filter
    params = {
        'filter': 'myapp',
    }
    module = MockModule(params=params)
    result = ansible

# Generated at 2022-06-13 00:29:19.443887
# Unit test for function ansible_facts
def test_ansible_facts():
    import sys
    import os
    sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
    from ansible.module_utils.basic import AnsibleModule

    test_params = dict(gather_subset='all')
    test_module = AnsibleModule(argument_spec=dict(gather_subset=dict(type='list')))
    test_module.params = test_params

    facts = ansible_facts(test_module, gather_subset=test_params['gather_subset'])

    assert facts['default_ipv4']['address'] == '192.168.56.3'

# Generated at 2022-06-13 00:29:27.951869
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils import basic
    import json

    m = basic.AnsibleModule(argument_spec={'gather_subset': dict(type='list', default=['all'])})

    # The default 'all' value for gather_subset should return a large set of facts
    facts_dict = get_all_facts(m)
    assert isinstance(facts_dict, dict)
    num_facts = len(json.dumps(facts_dict))

    # A little crude, but assert that we have a decent set of facts returned
    # The 2.0/2.2 api is just returning a list of facts, not a dictionary.
    # So the length of that list should be pretty large.
    assert num_facts > 10000

# Generated at 2022-06-13 00:29:39.575456
# Unit test for function ansible_facts
def test_ansible_facts():
    '''Unit tests for compat method ansible_facts'''

    import sys
    if sys.version_info[0] < 3:
        import mock
    else:
        from unittest import mock

    m_module = mock.MagicMock()

    m_module.params = dict()
    m_module.params['gather_subset'] = ['all']
    m_module.params['gather_timeout'] = 10
    m_module.params['filter'] = '*'

    # Test with only gather_subset in params dict
    ansible_facts(m_module)
    m_module.fail_json.assert_not_called()
    m_module.exit_json.assert_called_once_with(
        ansible_facts=mock.ANY,
        changed=False)

    # Test with gather

# Generated at 2022-06-13 00:29:49.419796
# Unit test for function ansible_facts
def test_ansible_facts():
    '''For testing, create a mock AnsibleModule instance and call the
    ansible_facts function.
    '''

    from ansible.module_utils.facts import ansible_facts
    from ansible.module_utils.basic import AnsibleModule

    # create a mock module instance with some parameters
    # For test purposes, we don't need the actual argument_spec
    # and we can mock the params
    mock_module = AnsibleModule(argument_spec={})
    mock_module.params = {'gather_subset': ['!all'], 'filter': 'ansible_distribution'}

    facts_dict = ansible_facts(module=mock_module)

    assert isinstance(facts_dict, dict)
    assert 'distribution' in facts_dict
    assert 'version' in facts_dict['distribution']
   

# Generated at 2022-06-13 00:29:54.884354
# Unit test for function get_all_facts
def test_get_all_facts():
    import ansible.module_utils.facts.ansible_facts as facts_module

    test_module = mock.MagicMock()
    test_module.params = {'gather_subset': []}
    results = facts_module.get_all_facts(test_module)
    assert results == {}


# Generated at 2022-06-13 00:30:19.915867
# Unit test for function ansible_facts
def test_ansible_facts():
    '''Unit test for ansible.module_utils.facts.ansible_facts'''
    from ansible.module_utils.facts import ansible_facts

    module = FakeModule()

    gather_subset = {'all'}

    ansible_facts_dict = ansible_facts(module, gather_subset=gather_subset)
    assert module.ansible_facts_called == 1
    assert 'ansible_facts' in ansible_facts_dict

    # Test 'version' filtering
    ansible_facts_dict = ansible_facts(module, gather_subset=gather_subset, filter='version')
    assert module.ansible_facts_called == 2
    assert 'ansible_facts' in ansible_facts_dict

# Generated at 2022-06-13 00:30:31.326477
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.system.distribution import DistributionFactCollector
    from ansible.module_utils.facts import ansible_collector
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts import default_collectors

    all_collector_classes = default_collectors.collectors

    # simulated module instance
    class MockAnsibleModule:
        def __init__(self):
            self.params = {}

        def fail_json(self, *args, **kwargs):
            pass

    # don't add a prefix
    namespace = PrefixFactNamespace(namespace_name='ansible', prefix='')

    # make it look like we aren't running

# Generated at 2022-06-13 00:30:42.144388
# Unit test for function get_all_facts
def test_get_all_facts():

    class FakeModule(object):
        def __init__(self, gather_subset):
            self.params = {'gather_subset': gather_subset}

    #test gather_subset is 'all'
    module = FakeModule('all')
    facts = get_all_facts(module)
    assert facts['os']['name'] == 'Linux'
    assert facts['hostname'] == 'localhost'
    assert facts['fqdn'] == 'localhost'
    assert facts['distribution'] == 'CentOS'
    assert facts['distribution_major_version'] == '6'
    assert facts['kernel'] == 'Linux'
    assert facts['interface_ip']['lo']['ipv4']['address'] == '127.0.0.1'

# Generated at 2022-06-13 00:30:53.371770
# Unit test for function ansible_facts
def test_ansible_facts():
    import pytest
    from ansible.module_utils.facts import ansible_collector

    class MockAnsibleModule(object):
        class MockParams(object):
            def __init__(self):
                self.params = {
                    'gather_subset': ['!all', 'network'],
                    'gather_timeout': 15,
                    'filter': 'ansible_*'
                }

            def get(self, key, default=None):
                return self.params.get(key, default)

        def __init__(self):
            self.params = self.MockParams()

    mock_module = MockAnsibleModule()

    class MockCollector(object):
        @classmethod
        def get_ansible_collector(cls, **kwargs):
            return cls()


# Generated at 2022-06-13 00:30:59.351230
# Unit test for function ansible_facts
def test_ansible_facts():
    module = MockModule()
    facts_dict = ansible_facts(module)
    assert facts_dict['system']['distribution'] == 'MockOS'
    assert facts_dict['system']['name'] == 'MockSystem'
    assert facts_dict['cloud']['name'] == 'MockCloud'
    assert facts_dict['system']['distribution'] == 'MockOS'



# Generated at 2022-06-13 00:31:10.350263
# Unit test for function ansible_facts
def test_ansible_facts():
    import sys
    import os
    import io

    class AnsibleMockModule(object):
        '''Mocks an ansible.module_utils.basic.AnsibleModule object'''

        def __init__(self, gather_subset, gather_timeout, filter):
            self.params = {'gather_subset': gather_subset,  # list of fact 'groups' to collect
                           'gather_timeout': gather_timeout,
                           'filter': filter}

    class AnsibleMockModule2(object):
        '''Mocks an ansible.module_utils.basic.AnsibleModule object (2.1.x)'''


# Generated at 2022-06-13 00:31:22.043278
# Unit test for function ansible_facts
def test_ansible_facts():
    import os
    import pytest

    test_outdir = os.path.join(os.path.dirname(__file__), 'test_output')

    UUT = ansible_facts

    class AnsibleModule():
        def __init__(self, params={}):
            self.params = params

    # module is None, so get_all_facts should raise Exception
    with pytest.raises(Exception):
        UUT(module=None)

    # defaults for gather_subset and gather_timeout, but module.params is defined,
    # so use module.params
    module = AnsibleModule({'gather_subset': ['all']})
    facts_dict = UUT(module)
    assert facts_dict is not None
    assert len(facts_dict) > 0

    # gather_subset and gather_timeout

# Generated at 2022-06-13 00:31:28.703841
# Unit test for function get_all_facts
def test_get_all_facts():
    # TODO use mock in future
    try:
        # test with no gather_subset param
        module = AnsibleModule(argument_spec=dict(gather_timeout=dict(required=False, type='int', default=10)))
        facts_dict = get_all_facts(module)
        assert(facts_dict)

        # test with no gather_subset param
        module = AnsibleModule(argument_spec=dict(gather_subset=dict(type='list', default=['!all']),
                                                  gather_timeout=dict(required=False, type='int', default=10)))
        facts_dict = get_all_facts(module)
        assert(facts_dict)
    except ImportError:
        # ansible 2.1 does not have AnsibleModule
        pass



# Generated at 2022-06-13 00:31:36.036019
# Unit test for function get_all_facts
def test_get_all_facts():

    class AnsibleModule:
        def __init__(self):
            self.params = {'gather_subset': ['all']}

    module = AnsibleModule()
    # comparing the fact to the given sample output from ansible 2.2.2

# Generated at 2022-06-13 00:31:46.157498
# Unit test for function ansible_facts
def test_ansible_facts():
    import ansible.module_utils.facts.system.distribution
    import ansible.module_utils.facts.system.pkg_mgr
    import ansible.module_utils.facts.system.platform

    class MockModule:
        class MockParams:
            def __init__(self):
                self.subset = 'distribution'

        def __init__(self):
            self.params = self.MockParams()

    mock = MockModule()
    facts = ansible_facts(mock)
    assert facts['distribution']['distribution'] == 'unknown'
    assert facts['distribution']['version'] == 'unknown'
    assert facts['distribution']['changed'] == True
    assert facts['distribution']['failed'] == True
    assert facts['pkg_mgr'] == None
    assert facts

# Generated at 2022-06-13 00:32:33.721499
# Unit test for function ansible_facts
def test_ansible_facts():
    import os
    from ansible.module_utils import basic

    class FakeModule(object):
        def __init__(self):
            self.params = {}

    test_module = FakeModule()

    # gather_subset is not set. sets to default
    assert 'ansible_facts' in get_all_facts(test_module)
    assert 'ansible_facts' in ansible_facts(test_module)
    test_module.params['gather_subset'] = []
    assert 'ansible_facts' in get_all_facts(test_module)
    assert 'ansible_facts' in ansible_facts(test_module)

    # get the facts via default collectors
    test_module.params['gather_subset'] = ['all']

# Generated at 2022-06-13 00:32:41.911669
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils.facts import ansible_collector

    gather_subset='all'
    all_collector_classes = default_collectors.collectors

    # don't add a prefix
    namespace = PrefixFactNamespace(namespace_name='ansible', prefix='')


# Generated at 2022-06-13 00:32:50.773648
# Unit test for function ansible_facts
def test_ansible_facts():
    import ansible.module_utils.facts.ansible_facts as testmodule
    import ansible.module_utils.facts.system.distribution as testdistribution

    class TestModule(object):
        def __init__(self, params):
            self.params = params

    test_params = {'gather_subset': ['all']}
    test_module = TestModule(params=test_params)

    try:
        test_ansible_facts_dict = testmodule.ansible_facts(module=test_module,
                                                           gather_subset=test_module.params['gather_subset'])
    except:
        raise AssertionError("ansible_facts failed, exception raised!")


# Generated at 2022-06-13 00:33:01.502590
# Unit test for function ansible_facts

# Generated at 2022-06-13 00:33:09.827191
# Unit test for function get_all_facts
def test_get_all_facts():

    def get_params(gather_subset):
        return dict(gather_subset=gather_subset)

    # arbitrary class that conforms to the AnsibleModule interface
    class AnsibleModule:
        def __init__(self, params):
            self.params = params

    # call function under test get_all_facts
    gather_subset = ['all']
    module = AnsibleModule(params=get_params(gather_subset))
    facts = get_all_facts(module)

    assert facts['distribution'] == 'Ubuntu'


# Generated at 2022-06-13 00:33:15.058345
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts import set_fs_uuid_facts
    set_fs_uuid_facts()

    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(argument_spec={})

    facts_dict = ansible_facts(module)

    assert 'distribution' in facts_dict


# Generated at 2022-06-13 00:33:26.734691
# Unit test for function ansible_facts
def test_ansible_facts():
    ''' unit test for ansible_facts function
    '''
    import ansible.module_utils.facts as facts
    import ansible.module_utils.facts.system.distribution as distribution
    from ansible.module_utils.facts import collectors

    # provide a 'mock' module
    module = facts.AnsibleModule(argument_spec=dict(a=dict(required=True)))

    # set this to collectors that should be called by ansible_facts
    module.params['gather_subset'] = ['distribution']

    # update the module's facts list to include the fact to be tested
    collectors.FACTS_COLLECTORS = [distribution]

    # execute the function under test
    result = ansible_facts(module)
    # test that the function returned the expected data
    assert result['distribution_version']

# Generated at 2022-06-13 00:33:34.109894
# Unit test for function ansible_facts
def test_ansible_facts():
    '''Stub for a future unit test.

    For now just document the interface'''

    def module_mock(params):
        '''emit a mock instance of ansible.module_utils.basic.AnsibleModule

        Args:
            params: a dict mapping module param names to values
                    should contain a gather_subset key, with a list of fact subset names

        Returns:
            instance of the module_mock, to be used as the module arg in ansible_facts()
        '''

        class FakeModule(object):
            '''emit a mock instance of ansible.module_utils.basic.AnsibleModule

            This is a stub for a real implementation, which would need to
            read the ansible_facts code to know how to emit a module mock.
            '''


# Generated at 2022-06-13 00:33:43.667013
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils.facts import get_all_facts as get_all_facts_func
    from ansible.module_utils._text import to_text
    import json


# Generated at 2022-06-13 00:33:50.632331
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts import ansible_facts
    from ansible.module_utils._text import to_bytes

    class AnsibleModule():

        def __init__(self, module_name):
            self.module_name = module_name
            self.params = dict()
            self.params['gather_subset'] = ['!all', 'network']
            self.params['gather_timeout'] = 10
            self.params['filter'] = '*'

    class UserModule(AnsibleModule):

        def __init__(self):
            super(UserModule, self).__init__(module_name='user')

        def get_bin_path(self, executable, required=False, opt_dirs=[]):
            return "/usr/bin/grep"

    # Test case 1: Default
    user