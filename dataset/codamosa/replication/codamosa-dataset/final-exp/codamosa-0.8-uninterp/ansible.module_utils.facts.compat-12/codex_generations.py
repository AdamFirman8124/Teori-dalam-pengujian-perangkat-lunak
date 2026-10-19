

# Generated at 2022-06-13 00:24:18.518850
# Unit test for function get_all_facts
def test_get_all_facts():

    import sys

    # This testcase assumes that the module has set the CWD to the common/lib dir
    from ansible.module_utils.facts.namespace import FactsNamespace
    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils.facts import ansible_collector
    from ansible.module_utils._text import to_bytes, to_native

    from ansible.module_utils.facts.hardware.cpu import HardwareCPUCollector
    from ansible.module_utils.facts.system.distribution import SystemDistributionCollector
    from ansible.module_utils.facts.system.pkg_mgr import SystemPkgMgrCollector

    class MyAnsibleModule(object):
        ''' Fake AnsibleModule to be used in unit tests '''

        params = dict()


# Generated at 2022-06-13 00:24:29.035207
# Unit test for function ansible_facts
def test_ansible_facts():
    import json
    import os
    import unittest

    TEST_DIR = os.path.dirname(__file__)
    TEST_DATA = os.path.join(TEST_DIR, 'test_data.json')

    def fake_module(arg1, arg2):
        return arg1

    with open(TEST_DATA) as f:
        test_data = json.load(f)

    for test in test_data:
        print(test)
        test_args = test.pop('test_args')
        test_kwargs = test.pop('test_kwargs')

        # Pop out the expected result
        expected_return = test.pop('expected_return')
        assert test == {}  # Make sure we consumed everything


# Generated at 2022-06-13 00:24:35.631775
# Unit test for function ansible_facts
def test_ansible_facts():
    class MockModule(object):
        def __init__(self, gather_subset, gather_timeout):
            self.params = {
                'gather_subset': gather_subset,
                'gather_timeout': gather_timeout,
            }

        def get_bin_path(self, executable, required=False, opt_dirs=[]):
            return '/bin/' + executable
    fact_dict = ansible_facts(MockModule(gather_subset=['all'], gather_timeout=10))

    assert fact_dict['users']
    assert fact_dict['local']['hostname']


# Generated at 2022-06-13 00:24:43.323443
# Unit test for function ansible_facts
def test_ansible_facts():
    class MockModule:
        class params:
            gather_subset = ['all']
            filter = '*'

        def get_option(self, name):
            return self.params[name]

    from ansible.module_utils.facts import default_collectors

    all_collector_classes = default_collectors.collectors

    # don't add a prefix
    namespace = PrefixFactNamespace(namespace_name='ansible', prefix='')

    facts_dict = ansible_facts(MockModule(), gather_subset=['all'])
    assert isinstance(facts_dict, dict)

# Generated at 2022-06-13 00:24:55.067836
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts.network.base import NetworkCollector

    class MockAnsibleModule(object):
        class Params(object):
            def __init__(self, gather_subset=None, gather_timeout=None, filter=None):
                self.gather_subset = gather_subset
                self.gather_timeout = gather_timeout
                self.filter = filter

        def __init__(self, gather_subset=None, gather_timeout=None, filter=None):
            self.params = self.Params(gather_subset=gather_subset, gather_timeout=gather_timeout, filter=filter)

    module = MockAnsibleModule(gather_subset=['all'], gather_timeout=10, filter='*')
    all_collector_classes = default_

# Generated at 2022-06-13 00:25:06.475811
# Unit test for function ansible_facts
def test_ansible_facts():
    import pytest
    from ansible.module_utils.facts.collector.base import BaseFactCollector
    from ansible.module_utils.facts.collector.network import NetworkFactCollector
    from ansible.module_utils.facts.collector.service_mgr import ServiceMgrCollector
    from ansible.module_utils.facts.network.base import Interface

    class MockModule():
        def __init__(self, params):
            self.params = params

    params = {'gather_subset': ['network']}
    mock_module = MockModule(params)

    mock_interface = Interface('eth0')
    mock_interface.addresses = (['1.2.3.4', '2.3.4.5'], [])

# Generated at 2022-06-13 00:25:18.030483
# Unit test for function get_all_facts
def test_get_all_facts():
    '''Test for get_all_facts'''

    # pylint: disable=unused-argument
    # Bunch of unused argument from the ansible module stub
    # pylint: disable=redefined-builtin
    # Also unused builtin args, module_utils.facts.get_all_facts
    def test_module(params, ansible_facts, ansible_version, ansible_host):
        '''AnsibleModule stub'''
        return params

    params = {
        'gather_subset': ['!all', 'network']
    }
    my_module = test_module(params, [], [], [])
    # test the function
    result = get_all_facts(my_module)

    # compare to a known subset of expected results

# Generated at 2022-06-13 00:25:26.719434
# Unit test for function get_all_facts
def test_get_all_facts():
    import ansible.modules.system.setup
    module = ansible.modules.system.setup.AnsibleModule(argument_spec={'gather_subset': dict(type='list', default='all')})

    facts = get_all_facts(module)
    assert 'local' in facts

    module = ansible.modules.system.setup.AnsibleModule(argument_spec={'gather_subset': dict(type='list', default=['all'])})
    facts = get_all_facts(module)
    assert 'local' in facts

# Generated at 2022-06-13 00:25:34.977283
# Unit test for function ansible_facts
def test_ansible_facts():
    # create a dummy module to pass in
    class TestAnsibleModule:
        def __init__(self):
            self.params = {'gather_subset': ['all']}

    ansible_module_mock = TestAnsibleModule()
    facts_dict = ansible_facts(ansible_module_mock)

    # just test for some common fields
    assert 'default_ipv4' in facts_dict
    assert isinstance(facts_dict['default_ipv4'], dict)
    assert 'default_gateway' in facts_dict['default_ipv4']

# Generated at 2022-06-13 00:25:44.720010
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts import ansible_collector
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils.facts import namespace_manager
    from ansible.module_utils.facts import collector

    from ansible.compat.tests.mock import patch

    from ansible.module_utils.facts.default_collectors import collector_mock
    from ansible.module_utils.facts import collector_mock

    # sanity check that we have the class we need to mock

    assert isinstance(collector_mock, collector.Collector)

    # inject param to mock class, so we can look at it later
    collector_mock.some_param = 'some param'

    # skip the

# Generated at 2022-06-13 00:25:58.764088
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.modules.system import redhat_subscription
    from ansible.module_utils._text import to_bytes

    module = redhat_subscription.RedHatSubscriptionModule()

# Generated at 2022-06-13 00:26:03.020422
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.basic import AnsibleModule
    import json

    module = AnsibleModule(argument_spec={}, supports_check_mode=True)
    all_facts = ansible_facts(module)
    print(json.dumps(all_facts, indent=4, sort_keys=True))

# Generated at 2022-06-13 00:26:11.109831
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts.namespace import BaseFactNamespace
    from ansible.module_utils.facts.collector import BaseFactCollector

    class TestFactNamespace(BaseFactNamespace):
        _namespace_name = 'test'

        def collect(self, module, collected_facts=None):
            self._populate_fact_dict(module=module)
            return self._fact_dict

    class TestFactCollector(BaseFactCollector):
        _fact_namespaces = [TestFactNamespace]

    class TestAnsibleModule:
        def __init__(self):
            self.params = {'gather_subset': ['all'], 'gather_timeout': 1}

    ansible_facts(module=TestAnsibleModule())

# Generated at 2022-06-13 00:26:21.538004
# Unit test for function ansible_facts
def test_ansible_facts():
    import unittest
    import os
    import tempfile
    import sys
    import mock

    # generate a mock module, module_utils.facts.ansible_collect.* is mocked out
    module = mock.MagicMock()
    module.params.get.side_effect = lambda key, default: {'gather_subset': None}.get(key, default)
    module.run_command.side_effect = lambda cmd, check_rc=False: ['hello', 'world']
    collector_mock = mock.MagicMock()
    collector_mock.collect.return_value = {'some_fact': 'test'}

    # patch out anything that calls import_module

# Generated at 2022-06-13 00:26:34.314871
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts.hardware.dmi import HardwareDmiCollector

    # TODO: note that the test_ansible_facts_with_filter_spec test has a
    # limitation-- a change to which default collectors are loaded will
    # cause the expected value to change, even though the call to ansible_facts
    # is unchanged.  If this happens, update the expected value.

    # TODO: should write a functional test to actually load a module and
    # call ansible_facts, but it looks like some work to set it up, so I'm
    # not doing that now.

    # TODO: probably should assert more, but this is a start.


# Generated at 2022-06-13 00:26:35.644271
# Unit test for function get_all_facts
def test_get_all_facts():
    pass

# Generated at 2022-06-13 00:26:43.054159
# Unit test for function ansible_facts
def test_ansible_facts():
    '''
    unit test for ansible_facts
    :return:
    '''
    try:
        from ansible.module_utils.facts.namespace import PrefixFactNamespace
        from ansible.module_utils.facts import default_collectors
        from ansible.module_utils.facts import ansible_collector
        print('ansible_facts: unit test passed')
        return True
    except ImportError as e:
        print(str(e))
        return False


if __name__ == '__main__':
    test_ansible_facts()

# Generated at 2022-06-13 00:26:51.926114
# Unit test for function ansible_facts
def test_ansible_facts():
    import module_utils.facts as facts

    class FakeModule(object):
        def __init__(self, params=None):
            self.params = params or {}

    gather_subset = ['all']
    gather_timeout = 10
    filter_spec = '*'

    # Test that default values are used
    module = FakeModule()
    assert ansible_facts(module) == facts.ansible_facts(module)

    # Test that values are passed to fact module
    module = FakeModule({'gather_subset': gather_subset,
                         'gather_timeout': gather_timeout,
                         'filter': filter_spec})
    assert ansible_facts(module) == facts.ansible_facts(module)

# Generated at 2022-06-13 00:27:01.994895
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts import get_all_facts, ansible_facts
    import ansible.module_utils.facts
    import ansible.module_utils.facts.networking
    import ansible.module_utils.facts.default_collectors

    # save original state of the global ansible.module_utils.facts.collector_classes
    ansible_collector_classes = ansible.module_utils.facts.collector_classes
    ansible_module_utils_facts_networking_collector_classes = ansible.module_utils.facts.networking.collector_classes
    ansible_module_utils_facts_default_collectors_collectors = ansible.module_utils.facts.default_collectors.collectors

    # swap in mocked collectors for testing
    ansible.module_utils.facts.collector

# Generated at 2022-06-13 00:27:12.450777
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts import ansible_collector
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts.collector import BaseFactCollector

    # Test data
    #
    # Test data for param module
    class TestModuleParams(object):
        def __init__(self):
            self.params = {}

        def __setitem__(self, key, value):
            self.params[key] = value

        def __getitem__(self, key):
            return self.params[key]

    # Test data for object to be used as arg to ansible_collector.get_ansible_collector

# Generated at 2022-06-13 00:27:17.474100
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils import basic
    import pytest
    module = basic.AnsibleModule(dict(gather_subset=['all']))
    ansible_facts = get_all_facts(module)
    assert 'ansible_architecture' in ansible_facts
    assert ansible_facts['ansible_architecture'] == 'x86_64'


# Generated at 2022-06-13 00:27:27.762416
# Unit test for function ansible_facts
def test_ansible_facts():
    import ansible.module_utils.facts.namespace as ns_module
    import ansible.module_utils.facts.system as sys_module
    import ansible.module_utils.facts.network as net_module

    # expectation: ansible_facts should return a dict mapping the fact name to its value
    # for example, the fact 'ansible_all_ipv4_addresses' should be mapped to something like
    # [ '172.16.10.250', '172.18.0.1' ]

    from ansible.module_utils.facts.system import Network

    class MyLinuxFactCollector(object):
        def __init__(self, module):
            pass
        def collect(self, module=None):
            return {'all_ipv4_addresses': Network().all_ipv4_addresses}

   

# Generated at 2022-06-13 00:27:34.863150
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils.facts import ansible_collector
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.facts import timeout
    import io

    module = AnsibleModule(argument_spec=dict(gather_subset=dict(default=['all'], type='list'),
                                              gather_timeout=dict(default=10, type='int'),
                                              filter=dict(default='*')))

    gather_subset = module.params['gather_subset']
    gather_timeout = module.params.get('gather_timeout', 10)


# Generated at 2022-06-13 00:27:36.437995
# Unit test for function ansible_facts
def test_ansible_facts():
    pass

# Generated at 2022-06-13 00:27:48.649355
# Unit test for function ansible_facts
def test_ansible_facts():
    import sys
    import imp
    import unittest

    class AnsibleModule:

        def __init__(self, params):
            self.params = params

    class TestAnsibleFacts(unittest.TestCase):

        def test_ansible_facts(self):
            # Create mock module and params for call to ansible_facts
            moduleparams = {'filter': '*',
                            'gather_timeout': 10}
            module = AnsibleModule(moduleparams)

            filteredfacts = ansible_facts(module)

            self.assertTrue(filteredfacts['distribution'])
            self.assertTrue(filteredfacts['python']['version'])
            self.assertTrue(filteredfacts['kernel'])

    # Run the unit test
    unittest.main()



# Generated at 2022-06-13 00:27:57.636457
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts.collector.ansible_collector import AnsibleFactCollector

    # Create a mock instance of the AnsibleModule class
    module = MagicMock()

    # Create a mock instance of the AnsibleFactCollector class
    fact_collector = MagicMock()

    # Set the return value of the get_ansible_collector method to the mock fact_collector
    ansible_collector.get_ansible_collector = MagicMock(return_value=fact_collector)

    # Create a mock of the facts_dict
    facts_dict = {'default_ipv4':'192.168.1.1', 'debug':False}

    # Set the collect method on the fact_collector to return a facts_dict

# Generated at 2022-06-13 00:28:04.793313
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils.facts import ansible_collector

    minimal_gather_subset = frozenset(['apparmor', 'caps', 'cmdline', 'date_time',
                                       'distribution', 'dns', 'env', 'fips', 'local',
                                       'lsb', 'pkg_mgr', 'platform', 'python', 'selinux',
                                       'service_mgr', 'ssh_pub_keys', 'user'])

    all_collector_classes = default_collectors.collectors

    # don't add a prefix
    namespace = PrefixFactNamespace(namespace_name='ansible', prefix='')


# Generated at 2022-06-13 00:28:15.774169
# Unit test for function get_all_facts
def test_get_all_facts():

    # Import here, to make this test module independent of ansible-base
    from ansible.module_utils._text import to_native
    from ansible.module_utils.facts import ModuleArgsParser

    import sys
    import os

    os.environ['ANSIBLE_INVENTORY_ENABLED'] = 'False'

    # Use our own module_utils as FACTS_MODULE_PATH has not been set yet
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../module_utils')))

    from ansible.module_utils.ansible_release import __version__ as ANSIBLE_VERSION

    # Create script which will be used as a python module

# Generated at 2022-06-13 00:28:18.013981
# Unit test for function ansible_facts
def test_ansible_facts():
    # TODO: add a unit test for this function.
    pass

# Generated at 2022-06-13 00:28:26.605097
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible import constants as C
    from ansible.module_utils.facts import ansible_facts


# Generated at 2022-06-13 00:28:40.810871
# Unit test for function ansible_facts
def test_ansible_facts():
    '''
    test the output of module_utils.facts.ansible_facts method
    '''
    import pytest
    from ansible.module_utils.facts.namespace import PrefixFactNamespace


    class FakeAnsibleModule(object):
        def __init__(self, gather_subset, gather_timeout):
            self.params = {'gather_subset': gather_subset,
                           'gather_timeout': gather_timeout}


    class FakeCollectorClass(object):
        def __init__(self, ns, filter_spec, gather_subset, gather_timeout):
            self.ns = ns
            self.filter_spec = filter_spec
            self.gather_subset = gather_subset
            self.gather_timeout = gather_timeout

# Generated at 2022-06-13 00:28:52.822302
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils import basic
    from ansible.module_utils.facts.utils import set_module_facts
    import datetime
    import os
    import sys

    class DummyAnsibleModule(object):
        def __init__(self):
            self.params = {'gather_subset': ['all']}
            self.config = {'changed': False}
            self.fail_json = lambda **kwargs: self.config.update({'changed': True, 'failed': True, 'msg': kwargs['msg']})
            self.exit_json = lambda **kwargs: self.config.update({'changed': True, 'failed': False, 'msg': kwargs['msg']})


# Generated at 2022-06-13 00:29:00.429453
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.facts.namespace import PrefixFactNamespace

    _ansible_module = AnsibleModule(argument_spec=dict(filter="*", gather_subset="all"))
    _gather_subset = _ansible_module.params.get("gather_subset", ['all'])

    _namespace = PrefixFactNamespace(namespace_name='ansible', prefix='')

    ZDOTDIR = "/Users/zach"
    facts_dict = ansible_facts(_ansible_module, gather_subset=_gather_subset)
    assert isinstance(facts_dict, dict)
    assert len(facts_dict) > 0

# Generated at 2022-06-13 00:29:06.045723
# Unit test for function ansible_facts
def test_ansible_facts():
    # mock the module
    module = MockModule()

    # test the trivial case where we don't accept the gather_subset parameter
    # and the default is to gather everything
    try:
        ansible_facts(module)
    except TypeError:
        assert False, "shouldn't have gotten a TypeError, missing gather_subset arg"

    # test that we can pass a gather_subset parameter
    ansible_facts(module, gather_subset=['min', 'platform'])

# Generated at 2022-06-13 00:29:08.207583
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts import facts
    assert ansible_facts(facts)

if __name__ == '__main__':
    test_ansible_facts()

# Generated at 2022-06-13 00:29:17.258770
# Unit test for function ansible_facts
def test_ansible_facts():
    class FakeAnsibleModule:
        """
        Fake AnsibleModule class
        """

        def __init__(self):
            self.params = {
                'gather_timeout': 2,
                'gather_subset': ['all'],
                'filter': '*'
            }

    def fake_get_all_facts(module):
        return ansible_facts(module, gather_subset=gather_subset)

    # create fake AnsibleModule
    fake_module = FakeAnsibleModule()

    # test with no gather_subset
    gather_subset = None
    assert fake_get_all_facts(fake_module)

    # test with gather_subset
    gather_subset = ['all']
    assert fake_get_all_facts(fake_module)


# old compat api


# Generated at 2022-06-13 00:29:27.801271
# Unit test for function ansible_facts
def test_ansible_facts():
    '''Unit test for function ansible_facts'''
    import ansible.module_utils.facts as real_facts_module
    # a fake 'module' with a fake config
    module = real_facts_module.AnsibleFakeModule(
        gather_subset=[],
        gather_timeout=0,
        gather_network_resources=[],
        filter='*',
        env={},
    )

    # invoke the function
    returned_fact_dict = ansible_facts(module)

    # and test the results
    # should have a 'session' fact
    assert returned_fact_dict

    # should be dict containing a hostvars dict (a copy of the module return_vals,
    # which we populated with the same values above)

# Generated at 2022-06-13 00:29:39.431789
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts import ansible_collector
    from ansible.module_utils.facts import default_collectors

    collector_class_name = 'LinuxDistribution'
    fact_subset = frozenset([collector_class_name])
    gather_subset = [collector_class_name]
    gather_timeout = 10
    filter_spec = '*'
    ansible_facts_path = 'ansible.module_utils.facts'
    namespace_name = 'ansible'
    prefix = 'ansible_'

    # Make sure we can import CollectorBase
    ansible_collector = __import__(ansible_facts_path,
                                   globals(), locals(), ['AnsibleCollector'])
    assert ansible_collector

    # Make sure we can import default_collectors
   

# Generated at 2022-06-13 00:29:49.420081
# Unit test for function ansible_facts
def test_ansible_facts():
    '''Unit test for function ansible_facts (no module arg, creates 'fake' module)

    :return:
    '''

    import datetime
    import json
    import os
    import shutil
    import tempfile
    import time

    import ansible.module_utils.facts.facts as ans_facts
    from ansible.module_utils.facts import default_collectors

    # compare_dicts function from _sysinfo.py
    # Compares two dictionary and returns True if they are the same
    def compare_dicts(dict1, dict2):
        """
        Compares two dictionaries and returns True if they are the same
        :param dict1:
        :param dict2:
        :return:
        """
        if dict1 is None:
            dict1 = dict()

# Generated at 2022-06-13 00:29:59.910703
# Unit test for function ansible_facts
def test_ansible_facts():
    from time import time
    from ansible.module_utils.facts.collector.network import NetworkCollector
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts.utils import get_file_content

    def FakeModule():
        am = argparse.ArgumentParser()
        am.add_argument('gather_subset', default=['all'])
        am.add_argument('gather_timeout', default=10)
        am.add_argument('filter', default='*')

        return am

    # This is a bit ugly, but it is the easiest way to get the dunder vars
    # populated so we can perform assertions against them.
    fake_module = FakeModule()



# Generated at 2022-06-13 00:30:20.190327
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts.collector.command import CommandCollector

    class TestModule(object):
        pass

    test_module = TestModule()
    test_module.params = dict(gather_subset=['all'], gather_timeout=10, filter='*')

    # Before we do any mocking lets see if the function will work if we don't do
    # any mocking at all.
    all_facts_dict = ansible_facts(module=test_module)

    # Now lets get rid of the command collector with a
    # mock
    backup_collectors_classes = default_collectors.collectors
    command_collector_class = default_collectors.collectors['command']
    # use a shallow copy, not a deep copy
    all_collectors_classes = dict(default_collectors.collectors)

# Generated at 2022-06-13 00:30:30.506228
# Unit test for function get_all_facts
def test_get_all_facts():
    try:
        from ansible.module_utils.facts import get_all_facts
        # If we can import this, then use the new get_all_facts method and the namespace will be 'ansible_'
        return get_all_facts(None)
    except ImportError:
        import ansible.module_utils.facts
        ansible.module_utils.facts.get_all_facts = \
            lambda module: ansible_facts(module, gather_subset=None)

        from ansible.module_utils.facts import get_all_facts
        # If we can import this, then use the new get_all_facts method and the namespace will be 'ansible_'
        return get_all_facts(None)

# Generated at 2022-06-13 00:30:42.056001
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils.facts import module_depends
    module_depends()

    import ansible.module_utils.facts.ansible_facts as m_ansible_facts
    import sys
    import json

    if sys.version_info[0] == 2:
        from mock import Mock
    else:
        from unittest.mock import Mock

    import ansible.module_utils.facts.sysconfig as m_sysconfig

    mock_module = Mock()

    mock_module.params = dict(
        filter='',
    )

    m_sysconfig.get_configured_facts = lambda: m_sysconfig.DEFAULT_GATHER_SUBSET

    result = m_ansible_facts.get_all_facts(mock_module)

    # We do not want to make a bunch of assumptions about

# Generated at 2022-06-13 00:30:53.285384
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts import ansible_facts
    from ansible.module_utils.six import PY3

    # Dummy ansible module
    class AnsibleModule(object):
        class _AnsibleModule(object):
            pass

        module = _AnsibleModule()
        module.params = dict()
        module.params['filter'] = 'ansible_local'

        @staticmethod
        def get_bin_path(name, required=False, opt_dirs=[]):
            if PY3:
                assert isinstance(name, str)
            else:
                assert isinstance(name, unicode)
            assert isinstance(required, bool)
            assert isinstance(opt_dirs, list)
            return '/bin/' + name

    # Gather facts
    facts = ansible_facts

# Generated at 2022-06-13 00:31:02.685914
# Unit test for function get_all_facts
def test_get_all_facts():
    class AnsibleModuleStub:
        def __init__(self, gather_subset):
            self.params = {
                'gather_subset': gather_subset,
            }

    validate = [
        ['all', True],
        [['min'], True],
        ['min', False],
        [['foo'], False],
    ]
    for gather_subset_param, expected in validate:
        module = AnsibleModuleStub(gather_subset=gather_subset_param)
        facts = get_all_facts(module)
        assert facts['has_journal'] == expected

# Generated at 2022-06-13 00:31:12.209969
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils.facts.virtual import VirtualCollector
    import ansible_module_init as h
    from ansible.module_utils.facts import namespace
    from mock import Mock
    from mock import MagicMock

    #########################################################################
    # Setup Module
    #########################################################################
    module = h.AnsibleModule(argument_spec={
        'gather_subset': dict(default=None, type='list'),
        'gather_timeout': dict(default=10, type='int')
    })
    namespace.AnsiblePrefixFactNamespace.__bases__ = (VirtualCollector,)
    h.AnsibleModule.run_command = MagicMock(return_value=['', '', 0])

# Generated at 2022-06-13 00:31:16.808724
# Unit test for function get_all_facts
def test_get_all_facts():

    from ansible.module_utils.facts.utils import AnsibleModule

    module = AnsibleModule(argument_spec=dict(gather_subset=dict(default=['all'], type='list')))

    facts = get_all_facts(module)

    assert type(facts) is dict

# Generated at 2022-06-13 00:31:20.990174
# Unit test for function ansible_facts
def test_ansible_facts():
    '''# Unit test for function ansible_facts'''

    import sys
    import ansible.module_utils.facts.collector
    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils.facts import ansible_collector
    from ansible.module_utils.facts import namespace
    import ansible.module_utils.facts.collectors.distribution
    import ansible.module_utils.facts.collectors.hardware
    import ansible.module_utils.facts.collectors.network
    import ansible.module_utils.facts.collectors.platform
    import ansible.module_utils.facts.collectors.system
    import ansible.module_utils.facts.collectors.config
    import ansible.module_utils.facts.collectors.pkg_mgr
    import ans

# Generated at 2022-06-13 00:31:27.110851
# Unit test for function ansible_facts
def test_ansible_facts():
    '''Unit test for ansible_facts function'''

    # simulate the module
    class FakeModule(object):
        def __init__(self, params):
            self.params = params
    # simulate module args
    params = dict(
        gather_subset=['all'],
        gather_timeout=10,
        filter='*',
    )
    module = FakeModule(params)

    all_facts = ansible_facts(module)

    assert all_facts['distribution'] == 'Unknown'

# Generated at 2022-06-13 00:31:35.029470
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts.virtual.base import VirtualCollector
    from ansible.module_utils.facts import disk

    from ansible.module_utils.facts.virtual.lxc import LXC
    from ansible.module_utils.facts.virtual.openvz import OpenVZ

    class AnsibleFactCollectorModule(object):
        def __init__(self, gather_subset, gather_timeout):
            self.params = dict(
                gather_subset=gather_subset,
                gather_timeout=gather_timeout
            )

        def fail_json(self, **kwargs):
            self.failed = True
            self.msg = kwargs.get('msg')


# Generated at 2022-06-13 00:32:04.424941
# Unit test for function ansible_facts
def test_ansible_facts():
    import json
    import os

    TEST_DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'unit', 'modules', 'network', 'nxos', 'test_data')

    from ansible.module_utils.facts import ansible_local
    from ansible.module_utils.facts.collector import GetAnsibleModuleImplementation
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts.collector.network.nxos.ansible_facts import NxosFactsModule
    from ansible.module_utils.facts.collector.base import BaseFactCollector


# Generated at 2022-06-13 00:32:14.310515
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.six import iteritems
    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils.facts import ansible_collector
    from ansible.module_utils.facts.namespace import PrefixFactNamespace

    class DummyModule(object):

        def __init__(self):
            self.params = dict()
            self.params['gather_subset'] = '!all'

    class DummyAnsibleModule(object):

        def __init__(self):
            self.params = dict()
            self.params['gather_timeout'] = 10

    dummy_module = DummyModule()
    dummy_ansible_module = DummyAnsibleModule()

# Generated at 2022-06-13 00:32:23.827612
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts import ansible_collector
    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    import sys
    import os

    class FakeAnsibleModule():
        '''Fake ansible module to supply to ansible_facts function'''
        def __init__(self):
            self.params = {}
            self.params['gather_subset'] = ['all']
            self.params['gather_timeout'] = 10

        def get_bin_path(self, executable, opts=None, required=False):
            return '/bin/' + executable

        def get_bin_paths(self, executable, opts=None, required=False):
            return ['/bin/' + executable]

       

# Generated at 2022-06-13 00:32:29.507318
# Unit test for function ansible_facts
def test_ansible_facts():
    # test_module_mock
    test_module = MagicMock()
    # test_module.params['gather_subset'] = ['all']
    test_module.params = {'gather_subset': ['all']}

    assert ansible_facts(test_module)
    assert ansible_facts(test_module)['default_ipv4']



# Generated at 2022-06-13 00:32:39.049197
# Unit test for function ansible_facts
def test_ansible_facts():
    '''Unit test for function ansible_facts

    ansible_facts calls the ansible_collector.get_ansible_collector
    method, and then calls the collector's collect method.  These
    unittests test that the collect method returns the expected
    results.
    '''

    import json
    import unittest

    from ansible.module_utils.facts import default_collectors

    # Mock AnsibleModule class
    class BaseAnsibleModule(object):
        def __init__(self, **kwargs):
            for k in kwargs:
                setattr(self, k, kwargs[k])

    class AnsibleModule(BaseAnsibleModule):
        def __init__(self, **kwargs):
            super(AnsibleModule, self).__init__(**kwargs)

    # Mock

# Generated at 2022-06-13 00:32:47.016541
# Unit test for function get_all_facts
def test_get_all_facts():
    import json
    import os
    import tempfile
    from ansible.module_utils._text import to_bytes

    filename = 'testfacts.json'
    file_path = os.path.join(tempfile.gettempdir(), filename)

    with open(file_path, 'w') as factfile:
        json.dump(dict(fact1='data1', fact2='data2'), factfile)


# Generated at 2022-06-13 00:32:57.331182
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.basic import AnsibleModule

    class MockModule(AnsibleModule):
        '''Mock of AnsibleModule.

        Define a mock AnsibleModule class, with some data attributes so that the default
        ansible module args are available for testing.
        '''
        def __init__(self):
            self.params = {
                'gather_subset': ['!all'],
                'gather_timeout': 10,
                'filter': '*',
            }

    module = MockModule()

    facts = ansible_facts(module)

    assert isinstance(facts, dict)
    assert len(facts) > 0

# Generated at 2022-06-13 00:33:04.877728
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts import ansible_facts
    from ansible.module_utils._text import to_bytes, to_text
    from ansible.module_utils.six import PY3, iteritems
    from ansible.module_utils.facts.namespace import PrefixFactNamespace

    class MockModule:
        def __init__(self):
            self.params = {}

    if PY3:
        for k, v in iteritems(ansible_facts(MockModule())):
            assert isinstance(k, str)
            assert isinstance(v, str)
            assert isinstance(ansible_facts(MockModule())[k], str)
    else:
        for k, v in iteritems(ansible_facts(MockModule())):
            assert isinstance(k, str)

# Generated at 2022-06-13 00:33:09.827800
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(argument_spec={'gather_subset': dict(type='list', default=['all']),
                                          'gather_timeout': dict(type='int', default=10),
                                          })

    collected_facts = get_all_facts(module)


# Generated at 2022-06-13 00:33:16.631171
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts import ansible_facts as _ansible_facts
    from ansible.module_utils.basic import AnsibleModule as _AnsibleModule
    module = _AnsibleModule(
        argument_spec=dict(
            gather_subset=dict(type='list', default=['!all'], required=False),
            gather_timeout=dict(type='int', default=10, required=False),
            filter=dict(type='str', default='*', required=False)
        )
    )
    assert _ansible_facts(module, '!all') is not None
    assert _ansible_facts(module) is not None

# Generated at 2022-06-13 00:34:01.432957
# Unit test for function get_all_facts
def test_get_all_facts():
    import ansible

    if ansible.__version__.startswith('2.0'):
        expected_subset = None
    else:
        expected_subset = ['!config', '!network']

    test_module = AnsibleModuleMock(params={'gather_subset': expected_subset})
    actual_facts = get_all_facts(test_module)
    assert actual_facts['gather_subset'] == expected_subset
    assert actual_facts['gather_timeout'] == 10



# Generated at 2022-06-13 00:34:05.696842
# Unit test for function ansible_facts
def test_ansible_facts():
    mock_module = object()

    # No gather subset provided, should still find facts
    facts_dict = ansible_facts(module=mock_module)
    assert facts_dict

    # Gather subset provided, should still find facts
    facts_dict = ansible_facts(module=mock_module, gather_subset=['all'])
    assert facts_dict

# Generated at 2022-06-13 00:34:08.804091
# Unit test for function get_all_facts
def test_get_all_facts():
    collect_all = ['all']
    collect_min = ['min']

    assert not get_all_facts(create_dummy_module(collect_all))
    assert get_all_facts(create_dummy_module(collect_min))
