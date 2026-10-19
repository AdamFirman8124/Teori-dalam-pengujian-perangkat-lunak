

# Generated at 2022-06-13 00:24:16.787635
# Unit test for function ansible_facts
def test_ansible_facts():
    import pytest
    from ansible.module_utils import basic
    gather_subset = ['min']
    filter_spec = '*'
    gather_timeout = 10

    # create a minimal fake AnsibleModule
    fake_module_args = {'gather_subset': gather_subset,
                        'filter': filter_spec,
                        'gather_timeout': gather_timeout}
    tmp = basic.AnsibleModule(argument_spec={},
                              supports_check_mode=False,
                              **fake_module_args)

    # generate & verify facts
    ansible_facts_dict = ansible_facts(module=tmp)

    # ansible_facts should return a dict with a top-level key for each fact that was collected
    for fact_name in gather_subset:
        assert fact_name in ansible

# Generated at 2022-06-13 00:24:26.574044
# Unit test for function get_all_facts
def test_get_all_facts():
    '''
    Test get_all_facts function

    :return:
    '''

    # Setup testing parameters
    gather_subset = ['all']
    gather_timeout = 10
    filter_spec = '*'

    # Setup a fake module
    module = AnsiModuleFakeClass(params={
        'gather_subset': gather_subset,
        'gather_timeout': gather_timeout,
        'filter': filter_spec,
    })

    # Call method get_all_facts()
    all_facts = get_all_facts(module)

    # Check the results
    for fact in gather_subset:
        assert isinstance(all_facts[fact], dict)



# Generated at 2022-06-13 00:24:29.524616
# Unit test for function get_all_facts
def test_get_all_facts():
    import module_utils.facts
    class AnsibleModule:
        def __init__(self):
            self.params = {'gather_subset': ['all']}

    module = AnsibleModule()
    facts_dict = module_utils.facts.get_all_facts(module)

    assert 'default_ipv4' in facts_dict

# Generated at 2022-06-13 00:24:39.399830
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.system.distribution import DistributionFactCollector
    from ansible.module_utils.facts import default_collectors

    # override the default collectors
    all_collector_classes = default_collectors.collectors
    all_collector_classes['Distribution'] = DistributionFactCollector

    # use an empty module
    module = object()

    # gather_subset=None means default value
    facts_dict = ansible_facts(module)

    # Check that facts['ansible_lsb'] is a dict
    assert type(facts_dict['lsb']) is dict

    # Check that we got the Distribution fact, and that it's the same as the DistributionFactCollector class

# Generated at 2022-06-13 00:24:51.468501
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts import module_lldp

    lldp_facts = ansible_facts(module_lldp, gather_subset=['!all', 'network'])

# Generated at 2022-06-13 00:24:57.624304
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils.basic import AnsibleModule

    data = {
        'k1': 'v1',
        'k2': 'v2',
        'k3': 'v3',
    }

    module = AnsibleModule(argument_spec={
        'gather_subset': dict(default=['all']),
    })

    module.params['k1'] = 'v1'
    module.params['k2'] = 'v2'
    module.params['k3'] = 'v3'

    assert get_all_facts(module=module) == data



# Generated at 2022-06-13 00:25:07.706367
# Unit test for function ansible_facts
def test_ansible_facts():
    '''test function ansible_facts('module')'''

    import ansible.module_utils.facts.namespace as namespace
    import ansible.module_utils.facts.collector as collector

    import re
    from mock import patch
    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils.facts import ansible_collector

    from ansible.module_utils.facts import this_is_ansible_module_mock as this_is_ansible_module
    from ansible.module_utils.facts import this_is_a_mock_ansible_module as this_is_a_mock_ansible_module


# Generated at 2022-06-13 00:25:19.174194
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts import ansible_facts

    from ansible_collections.ansible.netcommon.tests.unit.compat.mock import patch, MagicMock
    from ansible.module_utils.facts.namespace import PrefixFactNamespace

    gather_subset = set([])
    gather_timeout = 10
    filter_spec = '*'

    module = MagicMock()
    module.params = dict()
    module.params['gather_subset'] = gather_subset
    module.params['gather_timeout'] = gather_timeout

    with patch('ansible.module_utils.facts.ansible_collector.get_ansible_collector') as get_facts:

        ansible_facts(module)


# Generated at 2022-06-13 00:25:28.941718
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts.system.distribution import DistributionFactCollector
    distribution_fact_name = DistributionFactCollector.fact_class.FACT_NAME
    distribution_namespace_name = DistributionFactCollector.fact_class.NAMESPACE.namespace_name

    from ansible.module_utils.facts.system.platform import PlatformFactCollector
    platform_fact_name = PlatformFactCollector.fact_class.FACT_NAME
    platform_namespace_name = PlatformFactCollector.fact_class.NAMESPACE.namespace_name

    from ansible.module_utils.facts.system.pkg_mgr import PkgMgrFactCollector
    pkg_mgr_fact_name = PkgMgrFactCollector.fact_class.FACT_NAME
    pkg_mgr_names

# Generated at 2022-06-13 00:25:31.203669
# Unit test for function ansible_facts
def test_ansible_facts():
    module = {}
    gather_subset = ['all']
    assert ansible_facts(module, gather_subset)

# Generated at 2022-06-13 00:25:42.975152
# Unit test for function get_all_facts
def test_get_all_facts():
    import unittest
    from ansible.module_utils.facts.facts import ansible_facts
    from ansible.module_utils import facts
    from unittest.mock import MagicMock
    from unittest.mock import patch

    class Module:
        pass

    module = Module()
    module.params = {'filter': '*'}

    with patch.dict(facts.ansible_facts.__dict__, {'ansible_facts': ansible_facts}):
        with patch.object(ansible_facts, 'ansible_facts', return_value={}):
            with patch.object(ansible_facts, 'ansible_facts', return_value={}):
                get_all_facts(module)



# Generated at 2022-06-13 00:25:53.521756
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils.facts import ansible_collector
    from ansible.module_utils.basic import AnsibleModule

    # Mock module construction
    module_mock = AnsibleModule(argument_spec={})

    # Gather facts
    facts = ansible_facts(module_mock)

    assert facts['lsb']['codename'] == 'xenial'
    assert facts['architecture'] == 'x86_64'
    assert facts['distribution'] == 'Ubuntu'
    assert facts['distribution_release'] == 'xenial'
    assert facts['distribution_version'] == '16.04'

# Generated at 2022-06-13 00:26:04.603021
# Unit test for function get_all_facts
def test_get_all_facts():
    import sys
    import json

    # Note: 'setup' and 'set_fact' (and in ansible < 2.3 'group_by' and 'add_host') are not implemented.
    # This is good enough to check the other parts of the module.
    # No code in this module uses the above four.
    class Mock(object):
        def __init__(self, **kwargs):
            self.params = kwargs

        def get_bin_path(self, *args, **kwargs):
            return '/usr/bin/uname'

        def run_command(self, *args, **kwargs):
            return (0, 'Linux', '')

    # this is how AnsibleModule creates a log object
    class MockLogger(object):
        def __init__(self, pathname):
            self.messages

# Generated at 2022-06-13 00:26:11.835704
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.module_utils.facts.namespace import PrefixNamespace

    class MyModule:
        '''module api compat class used by the ansible 2.0 facts module_utils'''

        def __init__(self, params):
            self.params = params

        def fail_json(self, **kwargs):
            assert False, kwargs

        def get_bin_path(self, exe, required=False, opt_dirs=[]):
            return '/path/to/{0}'.format(exe)

        def get_platform(self):
            return 'linux'

        def get_distribution(self):
            return 'debian'


# Generated at 2022-06-13 00:26:22.044875
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.facts.virtual import Virtual, GenericFactCollector
    from ansible.module_utils.facts.system import System, Distribution
    from ansible.module_utils.facts.user import User
    from ansible.module_utils.facts.network import Network, Interface

    class ModuleFake:
        def __init__(self, params):
            self.params = params


# Generated at 2022-06-13 00:26:34.362721
# Unit test for function ansible_facts
def test_ansible_facts():

    class FakeAnsibleModule(object):
        def __init__(self, params):
            self.params = params

    filter = '*'
    gather_subset = ['network', 'system']
    gather_timeout = 10
    ansible_facts_module_params = {
        "filter": filter,
        "gather_subset": gather_subset,
        "gather_timeout": gather_timeout
    }
    ansible_facts_module = FakeAnsibleModule(ansible_facts_module_params)

    facts_dict = ansible_facts(ansible_facts_module)
    # ansible_facts API does not currently return facts from the 'all'
    # subset.  So don't expect the gather_subset param to be honored.
    # This API is deprecated in favor of the new facts.get() API

# Generated at 2022-06-13 00:26:43.304795
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts import default_collectors

    test_namespace = default_collectors.FactsCollector().get_namespace('test')
    import sys
    class MockModule:
        def __init__(self, params):
            self.params = params
            self.fail_json = lambda *args, **kwargs: sys.exit(1)

    results = ansible_facts(MockModule({
        'gather_subset': 'all',
        'filter': '*',
    }))

    assert 'test' in results
    assert results['test'] == test_namespace.get('test_fact')

# Generated at 2022-06-13 00:26:49.186074
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils.facts import ansible_facts as real_ansible_facts
    from ansible.module_utils.facts import get_all_facts as real_get_all_facts
    from ansible.module_utils.basic import AnsibleModule

    class FakeAnsibleModule(AnsibleModule):
        def __init__(self, *args, **kwargs):
            self.params = dict()
            super(FakeAnsibleModule, self).__init__(*args, **kwargs)

    # Test that ansible_facts(module) calls get_all_facts(module) with gather_subset=['all']
    fake_module = FakeAnsibleModule(argument_spec=dict())


# Generated at 2022-06-13 00:26:53.670026
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.basic import AnsibleModule
    facts = ansible_facts(AnsibleModule(argument_spec={},check_invalid_arguments=False, bypass_checks=True), gather_subset=['!all'])
    assert [item.startswith('ansible_') for item in facts.keys()] == [False]
    assert facts['local']

# Generated at 2022-06-13 00:26:58.759696
# Unit test for function ansible_facts
def test_ansible_facts():

    import ansible.module_utils.facts.collector
    import ansible.module_utils.facts.network.base
    import ansible.module_utils.facts.network.interfaces

    class AnsibleModule(object):
        def __init__(self):
            self.params = {'gather_subset': ['!all', 'network']}

    # Force ansible.module_utils.facts.collector.File.is_file to always return False
    # This will cause the /proc/cmdline file to not be parsed and no cmdline facts to be
    # collected.
    ansible.module_utils.facts.collector.File.is_file = lambda self: False

    # Patch the network interface fact collection to return some fake network interfaces
    # data, then restore the original method (so as not to affect other tests that could be


# Generated at 2022-06-13 00:27:06.754654
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.basic import AnsibleModule
    import json

    module = AnsibleModule(argument_spec={'gather_subset': dict(type='list', default=['!all']),
                                          'gather_timeout': dict(type='int', default=10),
                                          'filter': dict(type='str', default='*'),
                                          })

    result = ansible_facts(module=module)
    assert set(result.keys()) == set(('default_ipv4', 'machine_id', 'python', 'python_version', 'system',
                                      'system_vendor', 'uname_architecture', 'uname_os_version', 'uname_system'))



# Generated at 2022-06-13 00:27:14.696118
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils import basic
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts import default_collectors

    class DummyAnsibleModule(object):
        class ModuleDeprecationWarning(object):
            def __init__(self, message, version, collection_name=None):
                self.message = message
                self.version = version
                self.collection_name = collection_name
        def __init__(self, **kwargs):
            self.changed = False
            self.deprecations = []
            self._debug = False
            self.params = kwargs
            self.warn = self.module_deprecation_warning


# Generated at 2022-06-13 00:27:19.199791
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts.network.ansible_default_ipv4 import AnsibleDefaultIPv4
    from ansible.module_utils.facts.network.ansible_env_timezone import AnsibleEnvTimezone
    from ansible.module_utils.facts.system.ansible_local import AnsibleLocal

    class FakeModule:
        def __init__(self):
            self.params = dict()

    fake_module = FakeModule()
    fake_module.params['gather_subset'] = ['all']

    ansible_facts_dict = ansible_facts(fake_module, gather_subset=['all'])
    assert ansible_facts_dict['default_ipv4']['network'] == AnsibleDefault

# Generated at 2022-06-13 00:27:28.968992
# Unit test for function ansible_facts

# Generated at 2022-06-13 00:27:41.216362
# Unit test for function ansible_facts
def test_ansible_facts():
    '''Unit test for function ansible_facts'''

    import pytest
    from ansible.module_utils import basic
    from ansible.module_utils.facts import collector
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.sysconfig import DefaultSysconfigFactCollector

    class PropertyCollector(BaseFactCollector):
        '''Mock fact collector for ansible_facts unit test'''
        def __init__(self, namespace=None, filter_spec='*', gather_subset=None, gather_timeout=None):
            super(PropertyCollector, self).__init__(namespace, filter_spec, gather_subset, gather_timeout)
            self.props = {}


# Generated at 2022-06-13 00:27:51.848735
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils.facts import ansible_collector
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts.namespace import remove_prefix

    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils.facts import ansible_collector

    class AnsibleModule():

        def __init__(self, **kwargs):
            self.params = kwargs

        def fail_json(self, msg):
            raise Exception(msg)

    test_module = AnsibleModule(gather_subset=['all'])

    gather_subset = test_

# Generated at 2022-06-13 00:27:58.756790
# Unit test for function ansible_facts
def test_ansible_facts():
    import sys
    import argparse
    import collections

    class FakeAnsibleModule(object):
        '''Fake class representing an AnsibleModule, with just enough functionality to make ansible_facts return facts.

        facts_dict = ansible_facts(module)
        '''

        def __init__(self, fake_params):
            self.params = fake_params
            self._name = 'ansible_test'
            self.return_data = collections.defaultdict(dict)

        @property
        def name(self):
            '''Fake the ansible module name'''
            return self._name

        def exit_json(self):
            '''Fake the exit_json method'''
            sys.exit(1)


# Generated at 2022-06-13 00:28:02.608251
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts import ansible_facts
    from ansible.compat.tests.mock import Mock

    # fakes module.params
    fake_module_params = {
        'gather_subset': ['all'],
        'gather_timeout': 10,
        'filter': '*',
    }

    module = Mock()
    module.params = fake_module_params

    facts = ansible_facts(module=module, gather_subset=fake_module_params['gather_subset'])

    assert 'fips' in facts
    assert facts['fips'] is False

# Generated at 2022-06-13 00:28:13.520442
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils._text import to_bytes, to_text
    from ansible.module_utils.basic import AnsibleModule
    import pytest
    import os

    class MockModuleParams(object):
        def __init__(self, gather_subset, expected_fact_name, expected_fact_value):
            self.params = {'gather_subset': gather_subset,
                           'filter': '*'}

            self.expected_fact_name = expected_fact_name
            self.expected_fact_value = expected_fact_value

    # note that this module is being imported from the source directory,
    # which causes sys.path to be different from the normal path.
    #
    # test_module should be in __file__/../../../test/units/module_utils/test_ansible

# Generated at 2022-06-13 00:28:24.082137
# Unit test for function ansible_facts
def test_ansible_facts():
    import sys

    class FakeModule(object):
        def __init__(self, params):
            self.params = params

    params = dict(
        gather_subset=['all'],
        gather_timeout=10,
        filter = '*'
    )

    module_for_test = FakeModule(params)
    facts_dict = ansible_facts(module_for_test)
    print("Facts: %s" % facts_dict)


# Generated at 2022-06-13 00:28:38.840808
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts.network.base import NetworkCollector
    import ansible.module_utils.facts.network.generic as generic_network

    class TestGenericNetwork(generic_network.GenericNetwork):
        def __init__(self):
            self.default_ipv4 = '1.2.3.4'


# Generated at 2022-06-13 00:28:50.427696
# Unit test for function ansible_facts
def test_ansible_facts():
    '''Unit test for function ansible_facts

    TODO when 2.3 is released
    '''
    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils.facts import ansible_collector
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.ansible_release import __version__ as ansible_version

    # test class that inherits from BaseFactCollector
    class Collector(BaseFactCollector):
        def __init__(self, module=None, namesapce=None):
            super(Collector, self).__init__(module=module, namespace=namespace)

        def collect(self, module=None, collected_facts=None):
            return {'test': 'test'}

    # stub module
   

# Generated at 2022-06-13 00:28:59.128475
# Unit test for function ansible_facts
def test_ansible_facts():
    '''This is a fake unit test
    '''
    class FakeAnsibleModule(object):
        '''
        '''

        class FakeParams(object):
            '''
            '''
            
            def __init__(self):
                '''
                '''
                self.__params = {}

            def __getitem__(self, key):
                '''
                '''
                return self.__params[key]

            def __setitem__(self, key, value):
                '''
                '''
                self.__params[key] = value

            def __contains__(self, key):
                '''
                '''
                return key in self.__params

        
        def __init__(self, params):
            '''
            '''
            self.params = self.FakePar

# Generated at 2022-06-13 00:29:08.191005
# Unit test for function get_all_facts
def test_get_all_facts():
    import ansible.module_utils.facts.ansible_collector as ac
    import ansible.module_utils.facts.platform.sunos as sunos
    import ansible.module_utils.facts.platform.bsd as bsd
    import ansible.module_utils.facts.system.distribution as distribution
    import ansible.module_utils.facts.system.pkg_mgr as pkg_mgr

    import ansible.module_utils.facts.system.distribution as distribution
    import ansible.module_utils.facts.system.platform as platform
    import ansible.module_utils.facts.system.user as user
    import ansible.module_utils.facts.system.service_mgr as service_mgr
    import ansible.module_utils.facts.system.pkg_mgr as pkg_mgr

   

# Generated at 2022-06-13 00:29:17.227724
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts import ansible_facts
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils.facts import ansible_collector
    # module_utils.facts.ansible_facts(module, gather_subset=gather_subset)
    #   module_utils.facts.ansible_collector.get_ansible_collector(all_collector_classes,
    #       namespace, filter_spec, gather_subset, gather_timeout, minimal_gather_subset)

    try:
        from unittest.mock import create_autospec, patch, MagicMock
    except ImportError:
        from mock import create_autospec, patch, MagicM

# Generated at 2022-06-13 00:29:25.412228
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts.filesystem import FactsFilesystemModule
    import pytest

    class MockAnsibleModule:
        def __init__(self, params):
            self.params = params

    test_params = {'gather_subset': ['all'], 'gather_timeout': 10}
    module = MockAnsibleModule(test_params)

    ansible_facts_result = ansible_facts(module, gather_subset=['all'])
    assert isinstance(ansible_facts_result, dict)

# Generated at 2022-06-13 00:29:35.841920
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.ansible_release import __version__ as ansible_version

    # mock an AnsibleModule instance.  The only things we need are the params dict, and a log method
    class FakeAnsibleModule(object):
        def __init__(self):
            self.params = dict()
            self.params['gather_subset'] = None

        def log(self, msg):
            print('ansible_version: %s' % ansible_version)
            print(msg)

    module = FakeAnsibleModule()
    facts_dict = get_all_facts(module)

    assert 'distribution' in facts_dict
    assert 'distribution_version' in facts_dict

# Generated at 2022-06-13 00:29:40.546029
# Unit test for function ansible_facts
def test_ansible_facts():
    def test_module(params):
        return {}

    module = test_module
    module.params = {
        'gather_subset': ['all'],
        'gather_timeout': 10,
        'filter': '*'
    }

    facts_dict = ansible_facts(module)
    assert isinstance(facts_dict, dict)

# Generated at 2022-06-13 00:29:41.101458
# Unit test for function get_all_facts
def test_get_all_facts():
    pass

# Generated at 2022-06-13 00:29:51.695101
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.basic import AnsibleModule
    import json


# Generated at 2022-06-13 00:30:11.977121
# Unit test for function ansible_facts
def test_ansible_facts():
    import json

    class FakeModule(object):
        def __init__(self):
            self.params = {}
            self.run_command = None

        def fail_json(self, **kwargs):
            import sys
            print('FAILED: %s' % json.dumps(kwargs))
            sys.exit(1)

        def exit_json(self, **kwargs):
            import sys
            print('SUCCESS: %s' % json.dumps(kwargs))
            sys.exit(0)

        def get_bin_path(self, binary, required, opt_dirs=[]):
            return binary

        def set_command_defaults(self, defaults):
            self.run_command = defaults['module_implementation_preferences']

    ###########################################################################
    # END OF TEST CODE

# Generated at 2022-06-13 00:30:23.620002
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts import ansible_facts
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts import processor

    from ansible.module_utils.facts.cache import FactCache
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.cpu.processor import ProcessorFactCollector
    from ansible.module_utils.facts.cpu.cpu import CpuFactCollector

    class AnsibleModule:
        def __init__(self, params):
            self.params = params

    module = AnsibleModule({'filter':'processor'})
    facts = ansible_facts(module)
    assert facts['processor'][0]['model_name'] == processor.fact_gather().get('model_name')

# Generated at 2022-06-13 00:30:28.224420
# Unit test for function get_all_facts

# Generated at 2022-06-13 00:30:36.851805
# Unit test for function ansible_facts
def test_ansible_facts():
    '''Unit test for ansible_facts'''

    # Test multiple collect_methods
    mock_module = MockAnsibleModule(
        dict(gather_subset=['all']),
        'module_utils.facts.ansible_facts',
        params={'filter': '*'},
        gather_subset=['all'])

    test_facts = ansible_facts(module=mock_module)

    # this is just a test to see if we get some facts back.
    for section in ('all', 'default', 'min', 'command', 'hardware', 'network',
                    'virtual', 'ohai', 'facter', 'system', 'pkg_mgr'):
        assert section in test_facts

    # Test empty gather_subset
    # As long as the function doesn't crash this is fine
    mock

# Generated at 2022-06-13 00:30:46.819817
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils._text import to_text
    from ansible.module_utils.facts import get_all_facts

    module_mock = AnsibleModuleMock()
    # pick some random subset of facts
    module_mock.params['gather_subset'] = ['all', 'min', 'hardware']
    all_facts = get_all_facts(module=module_mock)
    # pick some random facts from the list and make sure they exist
    for fact in ('architecture', 'distribution_major_version', 'serialnum'):
        assert fact in all_facts
        print(to_text(fact), all_facts[fact])



# Generated at 2022-06-13 00:30:56.662686
# Unit test for function ansible_facts
def test_ansible_facts():
    '''Test ansible facts across several ansible versions'''
    import sys
    import os
    import textwrap
    from tempfile import NamedTemporaryFile

    import pytest

    from ansible.module_utils.facts import ansible_collector
    from ansible.module_utils._text import to_bytes

    firmware_facts = u"""
    {
      "TEST1": "fact_value1",
      "TEST2": "fact_value2"
    }
    """


# Generated at 2022-06-13 00:30:58.926569
# Unit test for function ansible_facts
def test_ansible_facts():
    assert ansible_facts({}, gather_subset=['all']) is not None
    assert ansible_facts({}) is not None

# Generated at 2022-06-13 00:31:09.694904
# Unit test for function ansible_facts
def test_ansible_facts():
    import ansible.module_utils.facts.namespace as ns

    class ModuleMock(object):
        def __init__(self):
            self.params = {}

    m = ModuleMock()
    m.params['filter'] = '*'
    m.params['gather_subset'] = None

    # test that the namespace was passed to the base class constructor
    got = ansible_facts(module=m)
    expected = ns.PrefixFactNamespace
    assert isinstance(got, expected)

    # test that the namespace was passed to the base class constructor
    m.params['gather_subset'] = ['all']
    got = ansible_facts(module=m)
    expected = ns.PrefixFactNamespace
    assert isinstance(got, expected)

# Generated at 2022-06-13 00:31:12.810975
# Unit test for function ansible_facts
def test_ansible_facts():
    class FakeModule(object):
        def __init__(self, params):
            self.params = params

    fake_params = {'gather_timeout': 1}
    fake_module = FakeModule(params=fake_params)

    # *** This is the only line that really matters.
    #     Does it return a dict with just the ansible namespace trimmed?
    facts_dict = ansible_facts(fake_module)
    assert facts_dict.keys() == ['default_ipv4']

# Generated at 2022-06-13 00:31:22.376398
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils.facts import ansible_facts
    from ansible.module_utils.facts.namespace import BaseFactNamespace
    from ansible.module_utils import basic
    class FakeModule(object):
        def __init__(self, gather_subset=None):
            self.params = dict()
            self.params['gather_subset'] = gather_subset

    assert isinstance(ansible_facts(FakeModule()), BaseFactNamespace)
    assert isinstance(ansible_facts(FakeModule(['min'])), BaseFactNamespace)

    module = basic.AnsibleModule(argument_spec=dict())
    assert isinstance(get_all_facts(module), dict)

# Generated at 2022-06-13 00:31:50.622800
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts.system.distribution import DistributionFactCollector
    from ansible.module_utils.facts.system.pkg_mgr import PkgMgrFactCollector
    from ansible.module_utils.facts.system.platform import PlatformFactCollector
    from ansible.module_utils.facts.system.lsb import LsbFactCollector
    from ansible.module_utils.facts.system.service_mgr import ServiceMgrFactCollector
    from ansible.module_utils.facts.system.date_time import DateTimeFactCollector
    from ansible.module_utils.facts.system.uptime import UptimeFactCollector
    from ansible.module_utils.facts.system.user import UserFactCollector

# Generated at 2022-06-13 00:32:00.345881
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts import module_facts
    import pytest
    from ansible_collections.ansible.community.tests.unit.compat import unittest

    try:
        from test.support import EnvironmentVarGuard
    except ImportError:
        from test.test_support import EnvironmentVarGuard  # python2

    class test_ansible_facts(unittest.TestCase):
        def setUp(self):
            self.env = EnvironmentVarGuard()
            self.env.set('ANSIBLE_CHECK_MODE', '0')
            self.env.set('ANSIBLE_DEBUG', '0')
            self.env.set('ANSIBLE_DEPRECATION_WARNINGS', '0')
            self.env.set('ANSIBLE_FACT_CACHE_TIMEOUT', '0')

# Generated at 2022-06-13 00:32:09.778180
# Unit test for function ansible_facts
def test_ansible_facts():
    class MockModule(object):
        def __init__(self):
            self.params = {'gather_subset': ['default_ipv4']}

    module = MockModule()

    actual = ansible_facts(module)

# Generated at 2022-06-13 00:32:18.221849
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.facts import default_collectors

    module = AnsibleModule(
        argument_spec=dict(
            gather_subset=dict(type='list', default=['all']),
            gather_timeout=dict(type='int', default=10),
            filter=dict(type='str', default='*')
        )
    )

    ansible_collector.get_ansible_collector = lambda **kwargs: default_collectors.get_collector(namespace='ansible', **kwargs)

    # ensure we get a dict back
    facts_dict = ansible_facts(module)
    assert isinstance(facts_dict, dict)

# Generated at 2022-06-13 00:32:26.766368
# Unit test for function ansible_facts
def test_ansible_facts():

    from ansible.module_utils import basic
    from ansible.module_utils.facts import namespace as facts_namespace

    module = basic.AnsibleModule(argument_spec={})

    class FakeFactFinder:

        def __init__(self, *args):
            pass

        def collect(self, module):
            return {'foo': 'bar',
                    'ansible_namespace_foo_baz': 'bar',
                    'ansible_namespace_foo_qux': 'bar',
                    'ansible_namespace_foo_blip': 'bar',
                    }
    # no filter
    module.params['filter'] = ''
    fact_collector = ansible_facts(module=module,
                                   gather_subset=['all'])

    assert len(fact_collector.keys()) == 3
   

# Generated at 2022-06-13 00:32:36.438974
# Unit test for function ansible_facts
def test_ansible_facts():
    import mock

    class MockModule(object):
        def __init__(self):
            self.params = {}

    module = MockModule()
    module.params['gather_subset'] = ['all']

    mock_facts_dict = dict(foo='bar')

    mock_collector = mock.MagicMock()
    mock_collector.collect.return_value = mock_facts_dict

    with mock.patch('ansible.module_utils.facts.ansible_collector.get_ansible_collector',
                    return_value=mock_collector):
        actual_facts_dict = ansible_facts(module=module)
        assert mock_collector.collect.call_args[0][0] == module
        assert actual_facts_dict == mock_facts_dict

# Generated at 2022-06-13 00:32:45.639488
# Unit test for function ansible_facts
def test_ansible_facts():
    import ansible.module_utils.facts.collector
    import ansible.module_utils.facts.system.distribution
    import ansible.module_utils.facts.system.pkg_mgr
    from ansible.module_utils._text import to_text

    class ModuleStub():
        class params():
            gather_subset = ['all']
            gather_timeout = 10

    module = ModuleStub()
    fd = ansible.module_utils.facts.collector.FactsCollector(namespace=None,
                                                             fact_list=None,
                                                             all_collectors=None,
                                                             gather_subset=None,
                                                             gather_timeout=None)

    # Return a value for the module.get_bin_path() method
    ansible.module_utils.facts

# Generated at 2022-06-13 00:32:52.507867
# Unit test for function ansible_facts
def test_ansible_facts():
    # Unit test for function ansible_facts
    # Returns a dict where each key is a bare fact name, such as 'default_ipv4',
    # and each value is the fact value

    import pytest

    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils.facts import ansible_collector

    from ansible.module_utils._text import to_text

    from ansible.module_utils.facts.system.distribution import DistributionFactCollector

    # We need an AnsibleModule instance to instantiate a collector, so we'll have
    # a pytest test function pass the module to us.

# Generated at 2022-06-13 00:33:02.543396
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.facts import ansible_facts
    try:
        from unittest.mock import patch
    except ImportError:
        from mock import patch

    class Args(object):
        def __init__(self):
            self.gather_subset = 'all'
            self.gather_timeout = 10
            self.filter = '*'

    class AnsibleModuleMock(AnsibleModule):
        def __init__(self):
            self.params = Args()
            self.fail_json = None
            self.exit_json = None

        def fail_json(self, msg, **kwargs):
            raise AssertionError(msg)

        def exit_json(self, **kwargs):
            pass

   

# Generated at 2022-06-13 00:33:12.880155
# Unit test for function get_all_facts
def test_get_all_facts():
    """Test for function get_all_facts."""
    # ansible 2.2 and ansible 2.3 have different semantics for
    # gather_subset, but both are supported.  Pre Ansible 2.3,
    # gather_subset was a list
    gather_subset_list = ['all']
    gather_subset_scalar = 'all'
    filter_all = '*'
    filter_not_all = '!fake_fact'
    filter_not_all_list = ['!fake_fact']

    # The actual value of the 'ansible_*' prefixed fact doesn't matter,
    # so long as the returned facts are in the correct format

# Generated at 2022-06-13 00:33:56.067420
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils.facts.collector import BaseFactCollector, NamespacedFactDict
    from ansible.module_utils._text import to_text

    if not hasattr(__builtins__, '__ansible_test_dummy_module__'):
        class DummyModule(object):
            def __init__(self, params):
                self.params = params

        setattr(__builtins__, '__ansible_test_dummy_module__', DummyModule)

    if not hasattr(__builtins__, '__ansible_test_dummy_factcollector__'):
        class DummyFactCollector(BaseFactCollector):
            def __init__(self, module=None, collected_facts=None):
                self

# Generated at 2022-06-13 00:34:05.418679
# Unit test for function ansible_facts
def test_ansible_facts():
    import ansible.module_utils.facts
    module = ansible.module_utils.facts.AnsibleModule(
        argument_spec=dict(
            gather_subset=dict(type='list', default=['all'])
        )
    )
    facts = ansible_facts(module)
    # return a dict from 'ansible_facts' (current ansible 2.0/2.1 api) to something with a
    # 'ansible_' namespace for ansible 2.2+ (which uses get_all_ansible_facts)
    import copy
    ansible_facts = copy.deepcopy(facts)
    ansible_facts['ansible_facts'] = facts
    return ansible_facts

