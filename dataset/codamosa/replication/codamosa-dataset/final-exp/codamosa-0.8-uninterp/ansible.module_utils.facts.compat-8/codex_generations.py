

# Generated at 2022-06-13 00:24:17.147397
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible_collections.os_migrate.os_migrate.plugins.module_utils.facts import ansible_facts

    import os
    os.environ['ANSIBLE_HOST_KEY_CHECKING'] = 'False'

    class Module:
        def __init__(self, params):
            self.params = params

    params = dict(gather_subset=['all'])
    m = Module(params)

    # Run test in a try block so that we can catch the AssertionError when
    # the function returns unexpected values.
    try:
        ansible_facts(m)
    except AssertionError as e:
        raise AssertionError(e)

# Generated at 2022-06-13 00:24:18.244592
# Unit test for function get_all_facts
def test_get_all_facts():
    pass

# Generated at 2022-06-13 00:24:26.935112
# Unit test for function get_all_facts
def test_get_all_facts():

    class FakeModule(object):
        def __init__(self, params):
            self.params = params

    module = FakeModule({'gather_subset': ['all']})

    all_facts = get_all_facts(module)

    assert 'ansible_ssh_host' in all_facts
    assert 'ansible_default_ipv4' in all_facts

    module = FakeModule({'gather_subset': ['!all']})

    all_facts = get_all_facts(module)

    assert 'ansible_ssh_host' not in all_facts
    assert 'ansible_default_ipv4' not in all_facts



# Generated at 2022-06-13 00:24:35.668334
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts import ansible_facts

    import ansible.module_utils.facts.collector
    import ansible.module_utils.facts.system.distribution
    import ansible.module_utils.facts.system.fips
    import ansible.module_utils.facts.system.platform
    import ansible.module_utils.facts.system.python

    class MyMockModule(object):
        def __init__(self, params):
            self.params = params
            self.fail_json = self.failjson = self.fail_json_in_check_mode = self.warn = self.exit_json = \
                self.no_log_values = lambda **kwargs: None
            self.changed = False

# Generated at 2022-06-13 00:24:44.967773
# Unit test for function ansible_facts
def test_ansible_facts():

    # Unit-test for function ansible_facts

    # Helper function for constructing a module with the minimum set of args to call
    # the ansible_facts function and get a valid result.
    def get_module_with_minimal_args():
        import ansible.module_utils.facts as facts_module
        from ansible.module_utils.facts import default_collectors

        class StubModule(object):
            def __init__(self):
                self.params = dict(gather_subset=[])
                for collector_name, collector_class in \
                        default_collectors.collectors.items():
                    if hasattr(collector_class, 'DEFAULT_GATHER_SUBSET'):
                        self.params['gather_subset'] += \
                            collector_class.DEFAULT_GATHER_SUBSET



# Generated at 2022-06-13 00:24:50.819363
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts.collector import NullCollector

    class MyCollector(NullCollector):
        def collect(self, module=None, collected_facts=None):
            return {"foo": {'bar': 'baz'}}

    assert ansible_facts(module=None, gather_subset=None)['foo'] == {'bar': 'baz'}

# Generated at 2022-06-13 00:24:58.477838
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts.collector.network import Network

    from ansible.module_utils._text import to_bytes

    class MockModule(object):
        def __init__(self):
            self.params = {'gather_subset': ['all'], 'gather_timeout': 10}

    mock_ansible_module = MockModule()

    # Create a mock ansible_facts dict that contains all the results we expect to get from a real ansible run
    # for purposes of testing ansible-facts, we don't care about the contents of the actual facts.
    # just that the keys are all there.

    # create a mock 'ansible' namespace
    facts = dict()
    ansible_fact_namespace = dict()
    facts['ansible'] = ansible_fact_namespace

    ansible_fact_

# Generated at 2022-06-13 00:25:08.258620
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts.ansible_collector import MyFactCollector, MyCollector

    class TestModule(object):
        params = dict(gather_subset=['all', 'network'], gather_timeout=30, filter='*',
                      fact_dir='/var/lib/ansible/facts', fact_path='/usr/bin/myfact.sh')

        class TestAnsibleModule(object):
            def get_bin_path(self, fact_path, fact_dir=None, opt_dirs=()):
                return fact_path

        def __init__(self):
            self.test_module = self.TestAnsibleModule()

    def fake_collect(self):
        return dict(test='test_value')

    # monkey patch

# Generated at 2022-06-13 00:25:19.367345
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts.facts import Facts
    from ansible.module_utils.facts import ansible_collector
    from ansible.module_utils.facts import default_collectors

    mock_module = MockAnsibleModule(params={})

    all_collector_classes = default_collectors.collectors

    # create a fact collector that collects all facts
    fact_collector = \
        ansible_collector.get_ansible_collector(all_collector_classes=all_collector_classes,
                                                filter_spec='*')

    # collect facts from the mock module
    facts = fact_collector.collect(module=mock_module)

    assert isinstance(facts, Facts)
    # facts should have the same __dict__ as the mock_module

# Generated at 2022-06-13 00:25:27.827154
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts import ansible_facts
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.facts.utils import get_file_content

    args = dict(gather_subset='!all,!min')
    module = AnsibleModule(argument_spec=dict())
    facts_dict = ansible_facts(module=module, gather_subset=args['gather_subset'])

    # check that all facts (excluding the minimal subset) were gathered
    for fact in facts_dict.keys():
        assert fact in facts_dict

    # check that some of the facts are correct
    f = facts_dict['fips']
    assert f == 'False'
    s = get_file_content('/proc/sys/kernel/random/uuid')

# Generated at 2022-06-13 00:25:41.359699
# Unit test for function get_all_facts
def test_get_all_facts():
    test_module = FakeAnsibleModule()
    default_collectors.setup(test_module)

    # test with gather_subset all
    facts = get_all_facts(test_module)

    # test for a known fact that should be there
    assert('distribution' in facts)

    # test for a known fact that should be there
    assert('default_ipv4' in facts)

    # test with gather_subset minimal
    test_module.params['gather_subset'] = ['minimal']
    facts = get_all_facts(test_module)

    # test for a known fact that should be there
    assert('distribution' in facts)

    # test for a known fact that should NOT be there
    assert('default_ipv4' not in facts)



# Generated at 2022-06-13 00:25:52.146443
# Unit test for function get_all_facts
def test_get_all_facts():
    '''Compatibility testing of get_all_facts with the ansible 2.2/2.3 function'''
    from ansible.module_utils.facts.namespace import BaseFactNamespace
    from ansible.module_utils.facts import collector
    import ansible.module_utils.facts as facts_mod
    import ansible.module_utils.facts.system.distribution as distribution_mod

    # we need a 'valid' ansible module, but we don't care what it was called,
    # and we don't want any of the validating or normalizing it would normally do.
    class FakeModule:
        def __init__(self):
            self.params = {}

    fake_module = FakeModule()

    # mock out the 2.2/2.3 module_utils.facts.ansible_collector method (which is a function)

# Generated at 2022-06-13 00:25:59.529076
# Unit test for function ansible_facts
def test_ansible_facts():

    filtered = ansible_facts(AnsibleModule({'fact_gather_timeout': 1}))
    assert filtered == {}

    filtered = ansible_facts(AnsibleModule({'fact_gather_timeout': 1, 'filter': '*'}))
    assert filtered == {}

    unfiltered = ansible_facts(AnsibleModule({'fact_gather_subset': ['all']}))
    assert 'ansible_all_ipv4_addresses' in unfiltered

    assert len(unfiltered) > len(filtered)

# Generated at 2022-06-13 00:26:09.386883
# Unit test for function ansible_facts
def test_ansible_facts():
    import json

    class TestModule(object):
        def __init__(self, params):
            self.params = params


# Generated at 2022-06-13 00:26:20.054021
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts import bool_or_int
    from ansible.module_utils.facts import int_or_none
    from ansible.module_utils.facts import float_or_none

    # Create a mock for AnsibleModule class
    class MockAnsibleModule(object):
        def __init__(self):
            self.run_command_environ_update = {'LC_ALL': 'C'}

        def fail_json(self, *args, **kwargs):
            raise Exception('test')

        def params(self):
            # Return the expected params
            return {'gather_subset': ['all'],
                    'gather_timeout': 10,
                    'filter': '*'}

    # Create obj and use this func
    obj = MockAnsibleModule()
    result = ans

# Generated at 2022-06-13 00:26:32.171231
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts import cache
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils.facts.system.distribution import DistributionFactCollector
    from ansible.module_utils.facts.system.distribution import LinuxDistributionFactCollector
    from ansible.module_utils.facts.system.service_mgr import SystemdServiceManagerFactCollector
    from ansible.module_utils.facts.system.cloud.aws import AWSInstanceMetadataFactCollector
    from ansible.module_utils.facts.network.base import NetworkCollector
    from ansible.module_utils.facts.network.interfaces import InterfacesNetworkCollector
    from ansible.module_utils.facts.system.pkg_mgr import Y

# Generated at 2022-06-13 00:26:40.736240
# Unit test for function get_all_facts
def test_get_all_facts():
    from . import main
    module = main.AnsibleModule(
        argument_spec=dict(gather_subset=dict(required=False, type='list',
                                              default=['all'])),
        supports_check_mode=False
    )

    facts_dict = get_all_facts(module)

    # assert all of the facts expected in dict
    # iterate sub dicts to check any required keys/values

    # assert facts_dict['ansible_architecture'] == 'x86_64'
    # test that all the facts are available
    # there are currently 710 facts
    assert len(facts_dict) == 710

# Generated at 2022-06-13 00:26:47.691560
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts import default_collectors

    # Test function returns results
    import ansible.modules.system.setup as setup
    ansible_module = setup.AnsibleModule(argument_spec=dict(
        gather_subset=dict(default=None, type='list'),
        filter=dict(default='*', type='raw')
    ))

    ansible_module.params['gather_subset'] = ['all']

    facts_dictionary = ansible_facts(ansible_module)

    assert facts_dictionary

# Generated at 2022-06-13 00:26:56.116170
# Unit test for function ansible_facts

# Generated at 2022-06-13 00:27:03.461102
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils._text import to_bytes
    import json

    class MockAnsibleModule:
        def __init__(self):
            self.params = dict()

    module = MockAnsibleModule()
    module.params['gather_subset'] = ['all']

    facts_dict = ansible_facts(module=module)
    fact_json = to_bytes(json.dumps(facts_dict))
    assert fact_json is not None
    assert b'ansible_architecture' in fact_json

# Generated at 2022-06-13 00:27:15.088516
# Unit test for function ansible_facts
def test_ansible_facts():
    # set up the mock ansible_module
    class AnsibleModule:
        def __init__(self, **kwargs):
            self.params = kwargs

    # Gather all facts
    am = AnsibleModule(filter='*', gather_subset=['all'], gather_timeout=10)
    facts = ansible_facts(am)
    assert 'ansible_system' in facts
    assert facts['ansible_system'] == 'Linux'
    assert 'ansible_os_family' in facts
    assert facts['ansible_os_family'] == 'RedHat'

    # Gather subset of facts
    am = AnsibleModule(filter='ansible_system', gather_subset=['!all'], gather_timeout=10)
    facts = ansible_facts(am)

# Generated at 2022-06-13 00:27:25.878940
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils.facts import ansible_collector
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils.facts import ansible_collector
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    try:
        from collections import UserDict
    except ImportError:
        from UserDict import UserDict


    class FakeAnsibleModule(object):
        def __init__(self):
            self.params = {'subset':['all']}
    module = FakeAnsibleModule()

# Generated at 2022-06-13 00:27:36.486337
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.facts.facts import which
    import os
    import tempfile

    if not which('ssh'):
        raise AssertionError('ansible facts unit tests require an ssh executable')

    # create a temporary ansible.cfg with necessary defaults
    temp_config = tempfile.NamedTemporaryFile(delete=False)
    temp_config.write(u'[defaults]\n')
    temp_config.write(u'gathering = smart\n')
    temp_config.close()
    os.environ['ANSIBLE_CONFIG'] = temp_config.name


# Generated at 2022-06-13 00:27:42.901664
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts import ansible_facts

    # create a 'dummy' module object, with
    # - the param_reference() method returning the arg_spec,
    # - a params class attribute, mapping all param names to None, so you can access
    #   the value for a given param via module.params[param_name]
    import inspect
    import types

    class DummyModule(object):
        def __init__(self, params):
            self.params = params

            # add the param_reference() method to the module object, so it has
            # the same signature as a real AnsibleModule object
            def param_reference(self):
                arg_spec = {}
                for arg_name in self.params:
                    arg_spec[arg_name] = {}
                return arg_spec

            self.param

# Generated at 2022-06-13 00:27:49.690756
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts import ansible_facts

    import pytest

    # TODO: assert that it returns the same output as module_utils.facts.ansible_facts
    assert ansible_facts(module=None) == None
    assert ansible_facts(module=1) == None
    assert ansible_facts(module=any) == None
    assert ansible_facts(module='module') == None

    assert ansible_facts(module = pytest) == None

# Generated at 2022-06-13 00:27:58.319588
# Unit test for function ansible_facts
def test_ansible_facts():
    '''Basic test to make sure ansible_facts returns what we expect'''

    # this is just a mock function that pretends to be a real AnsibleModule
    # with the same parameters
    class AnsibleModuleMock:
        def __init__(self):
            self.params = {'gather_subset': ['all'], 'gather_timeout': 10, 'filter': '*'}

    facts = ansible_facts(AnsibleModuleMock())

    assert 'ansible_python' in facts
    assert 'ansible_python' in facts
    assert 'ansible_lsb' in facts
    assert 'ansible_date_time' in facts
    assert 'ansible_distribution' in facts
    assert 'ansible_platform' in facts


# Generated at 2022-06-13 00:28:03.326012
# Unit test for function ansible_facts
def test_ansible_facts():
    import ansible.module_utils.facts.collector
    import ansible.module_utils.facts.system.distribution
    import ansible.module_utils.facts.system.pkg_mgr
    from ansible.module_utils._text import to_text
    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils.facts import ansible_collector
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.six import PY2
    from ansible.module_utils.six.moves import mock

    # unset any existing facts in the global namespace
    test_dict = {}
    for k in ansible.module_utils.facts.collector.FACTS:
        test_dict[k] = None
    ans

# Generated at 2022-06-13 00:28:14.184681
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils._text import to_text
    import unittest2 as unittest


# Generated at 2022-06-13 00:28:23.302909
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils.facts import get_all_facts
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(argument_spec={
        'gather_subset': {'required': False, 'type': 'list', 'default': ['all']},
        'gather_timeout': {'required': False, 'type': 'int', 'default': 10},
        'filter': {'required': False, 'type': 'str', 'default': '*'},
    })
    all_facts = get_all_facts(module)

    assert all_facts['fqdn'].startswith('localhost.localdomain')

# Generated at 2022-06-13 00:28:34.368117
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts import ansible_facts
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.basic import AnsibleModule
    from io import StringIO
    import sys

    # Create a fake module object to use in the test
    class FakeModule(object):
        def __init__(self):
            self.params = dict()
            self.exit_json = dict()
            self.exit_args = dict()
            self.fail_json = dict()
            self.fail_args = dict()

        # Fake run method
        def run_command(self, args, check_rc=True):
            return dict(rc=0, stdout=b'', stderr=b'')

        def debug(self, arg):
            pass


# Generated at 2022-06-13 00:28:45.469811
# Unit test for function get_all_facts
def test_get_all_facts():
    facts_dict = get_all_facts()
    assert type(facts_dict) == dict
    assert 'ansible_architecture' in facts_dict


# Generated at 2022-06-13 00:28:56.118667
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils.basic import AnsibleModule

    try:
        from __main__ import display
    except ImportError:
        from ansible.utils.display import Display
        display = Display()

    display.verbosity = 3

    from ansible.module_utils import facts

    module = AnsibleModule(argument_spec={'gather_subset': dict(required=True, type='list')})
    module.params['gather_subset'] = ['all']

    all_facts = facts.get_all_facts(module)

    fact_ns = facts.namespace.get_all_facts_impl_namespaces()
    assert 'ansible_distribution' in fact_ns
    assert set(all_facts.keys()) == set(fact_ns.keys())



# Generated at 2022-06-13 00:29:06.788425
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils.facts.namespace import PrefixFactNamespace

    class FakeAnsibleModule:
        def __init__(self, gather_subset=None):
            self.params = dict()
            if gather_subset:
                self.params['gather_subset'] = gather_subset

    # No gather_subset specified, default to 'all'
    fake_module = FakeAnsibleModule()
    facts = get_all_facts(fake_module)
    assert 'distribution' in facts
    assert 'architecture' in facts
    assert 'distribution' in facts
    assert 'default_ipv4' in facts
    assert 'users' in facts

    # gather_subset set to 'minimal'

# Generated at 2022-06-13 00:29:15.918094
# Unit test for function get_all_facts
def test_get_all_facts():

    from ansible.module_utils.facts import get_all_facts
    class AnsibleModule(object):
        def __init__(self, gather_subset):
            self.params = {'gather_subset': gather_subset}

    module = AnsibleModule(gather_subset=['foo'])
    assert module.params['gather_subset'] == ['foo']

    module = AnsibleModule(gather_subset=['foo', 'bar'])
    assert module.params['gather_subset'] == ['foo', 'bar']

    facts_dict = get_all_facts(module)
    bare_fact_names = facts_dict.keys()

# Generated at 2022-06-13 00:29:23.913642
# Unit test for function ansible_facts
def test_ansible_facts():
    class Module(object):
        def __init__(self, run_command_environ_update):
            self.params = {'gather_subset': ['all']}
            self.run_command_environ_update = run_command_environ_update

    result = ansible_facts(Module({'ansible_facts': 'foo', 'ansible_distribution': 'bar'}))
    assert result == {'facts': 'foo', 'distribution': 'bar'}

# Generated at 2022-06-13 00:29:28.370506
# Unit test for function ansible_facts
def test_ansible_facts():
    class FakeModule():
        def __init__(self):
            self.params = dict()

        def get_option(self, option):
            return self.params.get(option)

    ansible_facts(FakeModule())

# Generated at 2022-06-13 00:29:29.432043
# Unit test for function ansible_facts
def test_ansible_facts():
    assert ansible_facts(module=None) is not None

# Generated at 2022-06-13 00:29:40.863224
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils.facts import ansible_collector
    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils.facts import namespace
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils import basic
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.facts.utils import get_all_facts
    from ansible.module_utils.facts.utils import ansible_facts

    facts_dict = get_all_facts(AnsibleModule)
    assert facts_dict['distribution'] in ['CentOS', 'RedHat']
    assert facts_dict['lsb']['distributor_id'] in ['CentOS', 'RedHat']

    facts_dict = ansible

# Generated at 2022-06-13 00:29:51.417917
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts.network.base import NetworkCollector
    from ansible.module_utils.facts.system.distribution import DistributionCollector
    from ansible.module_utils.facts.system.distribution import RedHatCollector
    import ansible.module_utils.facts.network.openbsd
    import ansible.module_utils.facts.system.distribution.openbsd

    class MockNetworkCollector(NetworkCollector):
        def collect(self, module=None, collected_facts=None):
            return {'default_ipv4': {'address': '1.2.3.4'}}

    class MockDistributionCollector(DistributionCollector):
        def collect(self, module=None, collected_facts=None):
            return {'os_family': 'OpenBSD'}


# Generated at 2022-06-13 00:29:58.686498
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils.facts import ansible_collector

    class module():

        def __init__(self):
            self.params = {'gather_subset': ['hardware', 'virtual', 'network']}

    my_module = module()
    all_facts = get_all_facts(my_module)
    assert isinstance(all_facts, dict)
    assert all_facts.get('virtual') == 'physical'


# Generated at 2022-06-13 00:30:17.819976
# Unit test for function ansible_facts
def test_ansible_facts():
    import platform

    class FakeModule(object):
        def __init__(self):
            self.params = { 'filter': 'cmdline,distribution' }
        def get_bin_path(self, component, required=False, opt_dirs=[]):
            return component

    module = FakeModule()
    facts = ansible_facts(module)
    assert facts['cmdline']['argv'] == [platform.python]
    assert facts['distribution'] == {'distribution': platform.system()}

# Generated at 2022-06-13 00:30:29.320247
# Unit test for function get_all_facts
def test_get_all_facts():
    class FakeAnsibleModule:
        def __init__(self, gather_subset):
            self.params = dict()
            self.params['gather_subset'] = gather_subset

    test_all = FakeAnsibleModule(['all'])
    test_min = FakeAnsibleModule(['min'])
    test_wildcard = FakeAnsibleModule(['network'])
    test_several = FakeAnsibleModule(['network', 'virtual'])

    assert 'lsb' in get_all_facts(test_all)
    assert 'lsb' in get_all_facts(test_min)
    assert 'lsb' not in get_all_facts(test_wildcard)
    assert 'lsb' not in get_all_facts(test_several)


# Generated at 2022-06-13 00:30:37.520038
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils.facts import ansible_collector
    from ansible.module_utils.facts.system.distribution import DistributionFactCollector

    class MockAnsibleModule(object):
        def __init__(self, params):
            self.params = params

    class MockCollectorClass(object):
        def __init__(self, name):
            self.name = name

        def collect(self, module):
            return {self.name: 'collector ' + self.name}

    module = MockAnsibleModule({'gather_subset': ['all']})

# Generated at 2022-06-13 00:30:45.143016
# Unit test for function ansible_facts
def test_ansible_facts():
    class AnsibleModule(object):
        def __init__(self, params):
            self.params = params

    module = AnsibleModule({'gather_subset': ['all'], 'filter': '*'})
    facts_dict = ansible_facts(module)
    assert 'lsb' in facts_dict.keys() and 'distribution' in facts_dict.keys() and \
           'distribution_version' in facts_dict.keys()
    assert len(facts_dict) > 0

# Generated at 2022-06-13 00:30:55.337757
# Unit test for function ansible_facts
def test_ansible_facts():
    '''
    This function is not really a unit test. It is a partial integration test.
    It relies on the fact that ansible does not load the system facts (and it is not easily
    possible to mock out the system facts for a full integration test).
    '''

    import copy
    import sys
    import inspect

    import ansible
    from ansible.module_utils.facts.system.base import BaseFactCollector
    import ansible.module_utils.facts.system.apparmor as apparmor_collector
    import ansible.module_utils.facts.system.caps as caps_collector
    import ansible.module_utils.facts.system.cmdline as cmdline_collector
    import ansible.module_utils.facts.system.date_time as date_time_collector

# Generated at 2022-06-13 00:31:00.679990
# Unit test for function get_all_facts
def test_get_all_facts():
    class Mock:
        pass

    mock_module = Mock()
    mock_module.params = {'gather_subset': ['all'], 'filter': '*'}

    result = get_all_facts(module=mock_module)

    # make sure we got back a dict
    assert isinstance(result, dict)



# Generated at 2022-06-13 00:31:10.828633
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils.facts.collector import BaseFactCollector
    import sys
    import types

    # Make sure ansible_facts exposes the right 'gather_subset' and 'filter'

    # mock an AnsibleModule with params for gather_subset and filter
    class FakeModule(object):
        params = {'gather_subset': 'fake_subset',
                  'filter': 'fake_filter'}

    # mock a GatherFacts() instance with a collect method
    class FakeGatherFacts(object):
        def __init__(self, module):
            pass

        def collect(self, module=None):
            self.collect_called = True
            self.collect_module = module

# Generated at 2022-06-13 00:31:22.705857
# Unit test for function ansible_facts
def test_ansible_facts():
    import json
    import os
    import tempfile
    import time

    test_data_dir = os.path.join(os.path.dirname(__file__), 'test_data')

    data_set = ('hostname', 'platform', 'system', 'virtualization', 'distribution', 'distribution_release', 'kernel')

    # read in test data
    with open(os.path.join(test_data_dir, 'test_data.json'), 'r') as f:
        test_data = json.loads(f.read())

    # run test fixture
    with open(os.path.join(test_data_dir, 'test_data.py'), 'r') as f:
        fixture = f.read()
    exec(fixture)

    # read ansible_facts from disk
    ansible_facts_dir

# Generated at 2022-06-13 00:31:26.216776
# Unit test for function get_all_facts
def test_get_all_facts():
    class Module(object):
        pass
    module = Module()
    module.params = dict()
    module.params['gather_subset'] = ['all']
    assert get_all_facts(module) == ansible_facts(module)


# Generated at 2022-06-13 00:31:34.414761
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils.facts.network.base import NetworkCollector
    from ansible.module_utils.facts.system.base import SystemCollector
    from ansible.module_utils import basic
    import sys

    mod = basic.Basic()
    mod.params['gather_subset'] = ['all']
    mod.params['gather_timeout'] = 10
    mod.params['filter'] = '*'

    results = get_all_facts(mod)

    assert len(results) == 123
    assert 'ansible_network_resources' in results
    assert 'ansible_all_ipv4_addresses' not in results
    assert 'ansible_all_ipv6_addresses' not in results
    assert 'ansible_default_ipv4' not in results

# Generated at 2022-06-13 00:32:14.050702
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils._text import to_text
    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils.facts import ansible_collector
    from ansible.module_utils.facts import namespace
    import ansible.module_utils.facts.system.distribution as distribution
    import ansible.module_utils.facts.system.platform as platform

    # TODO: need to duplicate the ansible_facts function, substituting a mock AnsibleModule for 'module'
    #       then perhaps we can test with very simple mock 'collectors' (eg: return {'fact_name': 'fact_value'})
    #       then test various scenarios (eg: mock 'gather_subset')

# Generated at 2022-06-13 00:32:23.528974
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts.collector.network import NetworkCollector

    def mock_get_all_collector_classes(*args, **kwargs):
        return {'network': NetworkCollector}

    # use a set of known facts as a test gold standard

# Generated at 2022-06-13 00:32:24.269347
# Unit test for function ansible_facts
def test_ansible_facts():
    # TODO: write a unit test
    pass

# Generated at 2022-06-13 00:32:34.734304
# Unit test for function ansible_facts
def test_ansible_facts():

    # TODO: make this unit test work on both python2 and python3
    try:
        from ansible.module_utils.facts.namespace import PrefixFactNamespace
        from ansible.module_utils.facts import default_collectors
        from ansible.module_utils.facts import ansible_collector
        from ansible.module_utils.facts import get_all_facts
    except ImportError:
        return

    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.module_utils.basic import AnsibleModule

    import sys
    old_argv = sys.argv

    sys.argv[1:] = ['ansible_facts']

# Generated at 2022-06-13 00:32:44.207758
# Unit test for function ansible_facts
def test_ansible_facts():
    import os
    import sys
    import unittest

    tests_dir = os.path.dirname(os.path.realpath(__file__))
    sys.path.append(os.path.join(tests_dir, 'unit', 'mock_module_utils'))

    from mock_module_utils.common import AnsibleModule

    class TestAnsibleFacts(unittest.TestCase):
        '''Test case to verify ansible_facts function returns expected results'''

        def setUp(self):
            self.module = AnsibleModule(argument_spec={'gather_subset': dict(default=['all']),
                                                       'gather_timeout': dict(default=10),
                                                       'filter': dict(default='*')})


# Generated at 2022-06-13 00:32:47.490966
# Unit test for function ansible_facts
def test_ansible_facts():
    class FakeModule:
        def __init__(self):
            self.params = {
                'gather_subset': ['all'],
            }

    module_inst = FakeModule()

    facts_dict = ansible_facts(module_inst)
    assert len(facts_dict) > 0

# Generated at 2022-06-13 00:33:00.073782
# Unit test for function ansible_facts
def test_ansible_facts():
    '''Test function ansible_facts with:

        gather_timeout = 10
        gather_subset = None
        filter_spec = '*'
    '''

    # I know this is not how a unit test should be written, but I don't know how to make the
    # args to the unit test take the role of the module passed to ansible_facts.

    import json
    # ansible_facts requires that the module passed in is an instance of AnsibleModule,
    # so create a fake AnsibleModule instance.
    class FakeAnsibleModule(object):
        pass

    fake_module = FakeAnsibleModule()
    fake_module.params = {'gather_timeout': 10,
                          'gather_subset': None,
                          'filter': '*'}

    # Invoke the function under test
    facts

# Generated at 2022-06-13 00:33:10.486890
# Unit test for function get_all_facts
def test_get_all_facts():
    import ansible.module_utils.facts.network.iosxr
    import ansible.module_utils.facts.network.ios
    import ansible.module_utils.facts.network.nxos
    import ansible.module_utils.facts.network.iosxr
    import ansible.module_utils.facts.network.junos
    from ansible.module_utils.facts import default_collectors

    # this is the only module with a main method
    from ansible.module_utils.facts.network.ios import main as ios_main

    class FakeModule(object):
        def __init__(self, gather_subset, gather_timeout):
            self.params = dict(gather_subset=gather_subset, gather_timeout=gather_timeout)


# Generated at 2022-06-13 00:33:22.127722
# Unit test for function ansible_facts
def test_ansible_facts():
    # todo: this unit test is incomplete
    # todo: it needs to deal with the collect(module) call
    # todo: which raises AttributeError: '_COMPAT' object has no attribute 'ansible_module'
    # todo: because it's expecting to be given an AnsibleModule
    # todo: consider making a dummy AnsibleModule for the unit test

    from ansible.module_utils.facts import ansible_collector

    # inject a dummy collector class for testing
    DummySubsetCollector = \
        ansible_collector.get_ansible_collector_class('dummy_subset_collector',
                                                      'dummy_subset_collector')


# Generated at 2022-06-13 00:33:31.629490
# Unit test for function get_all_facts
def test_get_all_facts():
    import ansible.module_utils.facts as facts_module
    import ansible.module_utils.facts.collector as collector

    class AnsibleModule:
        params = dict()

    mock_module = AnsibleModule()
    mock_module.params['gather_subset'] = ['default', 'some_other_gather_subset']

    class MockCollector(collector.BaseFactCollector):
        name = 'mock_collector'
        def collect(self, module=None, collected_facts=None):
            self.collected_facts = "some_facts"
            return self.collected_facts

    facts_module.default_collectors.collectors = [MockCollector, ]

    all_facts = get_all_facts(mock_module)