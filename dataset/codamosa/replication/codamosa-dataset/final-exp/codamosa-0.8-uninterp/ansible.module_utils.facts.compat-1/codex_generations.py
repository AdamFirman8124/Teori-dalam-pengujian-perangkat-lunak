

# Generated at 2022-06-13 00:24:16.374569
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts import default_collectors
    import mock

    # setup mock module
    module = mock.MagicMock(params=dict(gather_subset=['all'],
                                        gather_timeout=10,
                                        filter='*'))

    all_collector_classes = default_collectors.collectors

    # don't add a prefix
    namespace = PrefixFactNamespace(namespace_name='ansible', prefix='')

    # mock the fact collector

# Generated at 2022-06-13 00:24:27.129316
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts.facts import AnsibleModule
    import ansible.module_utils.facts.namespace as facts_namespace
    from ansible.module_utils.facts import collector
    import ansible.module_utils.facts.system as facts_system
    import ansible.module_utils.facts.virtual as facts_virtual
    import ansible.module_utils.facts.network as facts_network
    import ansible.module_utils.facts.collectors as facts_collectors
    import ansible.module_utils.facts.hardware as facts_hardware

    minimal_class_names = [facts_virtual.VirtualFactCollector,
                           facts_system.SystemFactCollector,
                           facts_network.NetworkFactCollector,
                           facts_hardware.HardwareFactCollector]

    minimal_collector_

# Generated at 2022-06-13 00:24:31.793113
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils.facts import get_all_facts

    module_mock = Mock()
    module_mock.params = {'gather_subset': ['all']}
    facts_dict = get_all_facts(module=module_mock)
    assert 'ansible_default_ipv4' in facts_dict


# Generated at 2022-06-13 00:24:38.587050
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils import basic
    class TestModule(basic.AnsibleModule):
        pass

    module = TestModule(argument_spec=dict(gather_subset=[None, 'all', 'min'],
                                           gather_timeout=10,
                                           filter='*'))
    module.params.update(gather_subset=None)
    facts = ansible_facts(module=module)
    assert facts['distribution']['full'] == u'RedHat'
    assert facts['distribution']['major_version'] == u'7'
    assert facts['distribution']['minor_version'] == u'2'
    assert facts['distribution']['name'] == u'RedHat'
    assert facts['distribution']['release'] == u'Maipo'

# Generated at 2022-06-13 00:24:45.928401
# Unit test for function ansible_facts
def test_ansible_facts():
    class TestModule(object):
        def __init__(self):
            self.params = dict()
            self.params['gather_subset'] = None
            self.params['gather_timeout'] = 10
            self.params['filter'] = '*'

    # Test that it can be called with no args
    ansible_facts(module=TestModule())

    # Test that it can be called with gather_subset arg
    ansible_facts(module=TestModule(), gather_subset=['all'])

# Generated at 2022-06-13 00:24:56.179952
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts import get_distribution
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts import ansible_collector
    import mock

    class FakeModule(object):
        def __init__(self, params=None):
            self.params = params

    def test_collect_distribution():
        fact_collector = ansible_collector.get_ansible_collector(all_collector_classes=[DefaultCollector,
                                                                                       DistributionCollector],
                                                                 namespace=namespace,
                                                                 gather_subset=gather_subset,
                                                                 gather_timeout=gather_timeout,
                                                                 minimal_gather_subset=minimal_gather_subset)


# Generated at 2022-06-13 00:24:58.063832
# Unit test for function ansible_facts
def test_ansible_facts():
    pass



# Generated at 2022-06-13 00:25:05.429665
# Unit test for function ansible_facts
def test_ansible_facts():
    class Module:
        pass

    # Create an instance of AnsibleModule
    module = Module()
    module.params = {'gather_subset': None, 'gather_timeout': 10, 'filter': '*'}

    # Call function ansible_facts
    result = ansible_facts(module)

    # Print the result
    print('result:')
    print(result)

    # Check the result
    assert result['os_family'] == 'RedHat'


if __name__ == '__main__':
    test_ansible_facts()

# Generated at 2022-06-13 00:25:16.910849
# Unit test for function get_all_facts
def test_get_all_facts():
    '''test the get_all_facts function'''

    from ansible import module_utils
    from ansible.module_utils import facts
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts.utils import get_collector_class

    class TestFacts(BaseFactCollector):

        NAME = 'test'
        NAMESPACE = PrefixFactNamespace(namespace_name='test_namespace', prefix='test_prefix')

        def gather(self, module):
            return {
                self.NAMESPACE.get_prefix(): {
                    'test_fact': 'test_value'
                }
            }

    original_get_collector_class = facts.get

# Generated at 2022-06-13 00:25:21.978590
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils.facts import get_all_facts

    class MockAnsibleModule(object):
        def __init__(self):
            self.params = dict(gather_subset='!all')

    module = MockAnsibleModule()

    from ansible.module_utils.facts import get_all_facts

    assert module.params['gather_subset'] == '!all'

    facts = get_all_facts(module)

    assert 'ansible_all_ipv4_addresses' not in facts



# Generated at 2022-06-13 00:25:31.144120
# Unit test for function ansible_facts
def test_ansible_facts():
    try:
        from ansible.module_utils.basic import AnsibleModule
    except ImportError:
        # handle < 2.0 ansible
        from ansible.module_utils.basic import *

    class FakeModule(object):
        '''fake version of AnsibleModule that only provides module.params'''
        def __init__(self, module_params):
            self.params = module_params

    # gather_subset=None means we should use the default subset
    gathered_facts = ansible_facts(FakeModule({}))
    assert 'all' == gathered_facts['gather_subset'][0]

    # gather_subset=['!foo'] means we should exclude foo
    gathered_facts = ansible_facts(FakeModule({'gather_subset': ['!foo']}))

# Generated at 2022-06-13 00:25:42.100141
# Unit test for function ansible_facts
def test_ansible_facts():
    import sys

    from ansible.module_utils.facts import ansible_facts
    from ansible.module_utils.basic import AnsibleModule

    class DummyAnsibleModule(AnsibleModule):
        def __init__(self):
            # https://raw.githubusercontent.com/ansible/ansible/devel/lib/ansible/module_utils/basic.py
            # get_bin_path is hardcoded to None, which works fine for some facts (i.e. date_time),
            # but not all facts
            super(DummyAnsibleModule, self).__init__(argument_spec={},
                                                     bypass_checks=True,
                                                     no_log=True,
                                                     use_ansible_find_needles=False)

    module = DummyAnsibleModule()

    #

# Generated at 2022-06-13 00:25:52.845219
# Unit test for function ansible_facts
def test_ansible_facts():
    import sys

    module_name = 'test_ansible_facts_module'
    module_path = 'test_ansible_facts_module.py'
    sys.path.append('.')

    # Create a test module
    test_module = type(sys)(module_name)
    test_module.params = {
        'gather_subset': ['all'],
        'gather_timeout': 10,
        'filter': '*',
    }

    class AnsibleModule:
        def __init__(self, argument_spec, bypass_checks=False, no_log=False,
                     mutually_exclusive=None, required_together=None, required_one_of=None,
                     add_file_common_args=False, supports_check_mode=False):
            pass


# Generated at 2022-06-13 00:26:03.409812
# Unit test for function get_all_facts
def test_get_all_facts():
    class stub_module:
        def __init__(self, gather_subset=None):
            self.params = {'gather_subset': gather_subset}
    import sys
    if sys.version_info < (2, 7):
        from nose.plugins.skip import SkipTest
        raise SkipTest("temporarily not running <2.7 tests")
    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts import ansible_collector
    for gather_subset in (None, ['all'], ['network'], ['non_network']):
        mod = stub_module(gather_subset=gather_subset)
        facts = get_all_facts(mod)
       

# Generated at 2022-06-13 00:26:11.530634
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts.network.base import NetworkCollector
    from ansible.module_utils.facts.system.base import SystemCollector

    # unit test helpers to mock an AnsibleModule
    # pylint: disable=import-error
    from ansible_collections.notstdlib.moveitallout.tests.unit.compat.mock import Mock

    _ansible_module = Mock(params={'gather_subset': ['all']})
    _ansible_module.get_option = _ansible_module.params.get

    expected_network_collector = NetworkCollector()
    expected_system_collector = SystemCollector()

    # run the actual unit test
    facts_dict = ansible_facts(_ansible_module)

    assert 'network' in facts_dict
    assert facts_

# Generated at 2022-06-13 00:26:21.890039
# Unit test for function ansible_facts
def test_ansible_facts():
    '''AnsibleModule is a class with a bunch of methods, but the only thing
    we need here is the params dict.
    '''
    class AnsibleModule:
        def __init__(self, gather_subset):
            self.params = {'gather_subset': gather_subset}

    # Expected value of 'ipv4' fact.

# Generated at 2022-06-13 00:26:33.957748
# Unit test for function ansible_facts
def test_ansible_facts():
    import types

    import ansible.module_utils.facts.collector.transformers as transformers

    fake_module = types.ModuleType('_ansible_module_test')
    fake_module.ansible_module = types.ModuleType('ansible_module')
    fake_module.ansible_module.params = {'gather_subset': ['all']}
    fake_module.ansible_module.params['gather_subset'] = ['all']

    facts_dict = ansible_facts(module=fake_module)

    assert isinstance(facts_dict, dict)

    for fact in facts_dict:
        assert facts_dict[fact] != transformers.UNKNOWN_TRANSFORM_VALUE

    # FIXME: add some tests  to check the actual data

# Generated at 2022-06-13 00:26:42.705705
# Unit test for function ansible_facts
def test_ansible_facts():
    '''test the ansible_facts function'''
    from facts.test.test_ansible_collector import MockAnsibleModule

    gather_subset = frozenset(['foo', 'bar'])
    filter_spec = 'ansible_foo*'

    module = MockAnsibleModule(gather_subset=gather_subset,
                               filter=filter_spec,
                               timeout=5,
                               debug=True)

    all_facts = ansible_facts(module=module)

    assert set(all_facts.keys()) == {'foo', 'foo_bar'}
    assert all_facts.get('foo') == 'baz'
    assert all_facts.get('foo_bar') == 'quux'

# Generated at 2022-06-13 00:26:52.184818
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts import ansible_facts
    from ansible.module_utils.facts.namespace import PrefixFactNamespace

    class FakeAnsibleModule:
        def __init__(self):
            self.params = {'gather_subset': ['all'],
                           'gather_timeout': 10,
                           'filter': '*'}

    fake_module = FakeAnsibleModule()

    # PrefixFactNamespace defaults to namespace 'ansible', and prefix 'ansible_'.
    # so we check if the first key in the ansible_facts dict starts with 'ansible_'
    assert list(ansible_facts(fake_module).keys())[0].startswith('ansible_')

# Generated at 2022-06-13 00:27:02.076312
# Unit test for function ansible_facts
def test_ansible_facts():
    ''' Unit test for function ansible_facts
    '''

    collect_subset = frozenset(('networking', 'network'))

    collection_timeout = 10

    filter_spec = '*'

    # Test gathering 'networking' facts
    gathered_facts = ansible_facts(module=None, gather_subset=collect_subset)

    assert gathered_facts
    assert 'ansible_all_ipv4_addresses' in gathered_facts
    assert 'ansible_all_ipv6_addresses' in gathered_facts
    assert 'ansible_default_ipv4' in gathered_facts
    assert 'ansible_default_ipv6' in gathered_facts
    assert 'ansible_machine_id' in gathered_facts
    assert 'ansible_nodename' in gathered_facts

# Generated at 2022-06-13 00:27:13.900267
# Unit test for function get_all_facts
def test_get_all_facts():
    '''
    This is not a real unit test, but should document how to unit test the function
    get_all_facts for a given module.
    This is the only function exposed by this file, which does the actual work
    of collecting facts from AnsibleModule's facts module.

    1) Create an instance of AnsibleModuleMock.
    2) Invoke ansible_facts.
    3) Verify the facts in the returned dict
    '''
    class AnsibleModuleMock(object):
        def __init__(self):
            self.params = dict(gather_subset=['all'])

    module = AnsibleModuleMock()

    facts = ansible_facts(module)

    assert(facts['fqdn'])
    assert(facts['kernel'])

# Generated at 2022-06-13 00:27:25.196406
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils.facts import ansible_collector

    import ansible.module_utils.facts.namespace
    AnsibleFakeModule = ansible.module_utils.facts.namespace.AnsibleFakeModule

    module = AnsibleFakeModule(params={})

    gather_subset = ['all']
    gather_timeout = 10
    filter_spec = '*'


# Generated at 2022-06-13 00:27:27.841360
# Unit test for function get_all_facts
def test_get_all_facts():
    try:
        from ansible.module_utils.facts import get_all_facts
        assert get_all_facts == get_all_facts
    except ImportError:
        assert get_all_facts == get_all_facts

# Generated at 2022-06-13 00:27:34.912405
# Unit test for function ansible_facts
def test_ansible_facts():
    import json
    import random

    try:
        import test.support
        import test.support.import_helper
    except ImportError:
        pass

    try:  # Python 3.3 +
        from unittest.mock import patch, Mock
    except ImportError:
        from mock import patch, Mock

    # we need a class that is like a builtin 'dict', but is json-serializable,
    # and we need to call a constructor on it to get an instance.
    # so lets mock one up.
    class DictLike(dict):
        def __init__(self, *args, **kwargs):
            pass

    # we'll create a module that is an instance of this mock class, which will
    # be like a builtin 'dict', and which we can json-serialize

# Generated at 2022-06-13 00:27:48.127426
# Unit test for function ansible_facts
def test_ansible_facts():
    ''' Unit test for function ansible_facts '''
    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils.facts import ansible_collector
    from ansible.module_utils.facts.namespace import PrefixFactNamespace

    # Test fact collector for GatherSubset == 'all'
    module = TestAnsibleModule()
    fact_collector = \
        ansible_collector.get_ansible_collector(all_collector_classes=default_collectors.collectors,
                                                namespace=PrefixFactNamespace(namespace_name='ansible', prefix=''),
                                                gather_subset=['all'],
                                                gather_timeout=10,
                                                minimal_gather_subset=set())

    facts_dict = fact_

# Generated at 2022-06-13 00:27:57.220964
# Unit test for function ansible_facts
def test_ansible_facts():
    import ansible
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts import collector

    class TestCollectorClass(BaseFactCollector):

        name = 'test_module_utils_facts'
        _fact_ids = set()

        def collect(self, module=None, collected_facts=None):
            return {
                'test_fact_key': 'test_fact_value'
            }

    class TestMockAnsibleModule:

        def __init__(self):
            self.params = {
                'gather_subset': ['all']
            }

    # Mock out AnsibleModule api
    module = TestMockAnsibleModule()
    test_collector = TestCollectorClass()

    # Mock out the _collector_classes variable


# Generated at 2022-06-13 00:28:03.386879
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils.facts.facts import ansible_virtualization_type
    from ansible.module_utils.facts.virtual import Virtual

    class AnsibleModule(object):
        def __init__(self):
            self.params = {'gather_subset': ['all']}
            self.exit_json = lambda exit_data: True

    a = AnsibleModule()

    results = get_all_facts(a)

    assert results
    # test for semi-random fact
    assert 'virtualization_type' in results
    assert results['virtualization_type'] == ansible_virtualization_type()



# Generated at 2022-06-13 00:28:14.286106
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible_collections.ansible.community.tests.unit.compat.mock import patch

    with patch('ansible_collections.ansible.community.tests.unit.compat.module_utils.facts.ansible_collector.get_ansible_collector') as mock_get_ansible_collector:
        mock_collector = mock_get_ansible_collector.return_value

        mock_module = object()
        mock_collector.collect.return_value = {'a': 'b', 'c': 'd'}

        result = ansible_facts(module=mock_module)
        assert result == {'a': 'b', 'c': 'd'}

        mock_collector.collect.assert_called_once_with(module=mock_module)
        mock_get_ans

# Generated at 2022-06-13 00:28:24.673675
# Unit test for function ansible_facts
def test_ansible_facts():
    import ansible.module_utils.facts
    import ansible.module_utils.facts.collector
    import ansible
    # import pytest

    # pylint: disable=no-member
    ansible.module_utils.facts.DEFAULT_GATHER_TIMEOUT = 0
    ansible.module_utils.facts.DEFAULT_GATHER_SUBSET = ['min', 'custom']

    expected_facts = {'namespace_1': 'value_1'}

    class CustomCollector(ansible.module_utils.facts.collector.BaseFactCollector):
        '''placeholder for custom fact collector'''
        name = 'custom_collector'
        _fact_ids = ['namespace_1']


# Generated at 2022-06-13 00:28:36.684978
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts.collector import FactsCollector
    import ansible.module_utils.basic
    from ansible.module_utils.facts import default_collectors

    def fake_collect(self, module):
        return {'this_is_a_fake': 'fact'}

    # monkeypatch FactsCollector.collect method to return fake facts
    FactsCollector.collect = fake_collect

    module = ansible.module_utils.basic.AnsibleModule(
        argument_spec={
            'gather_subset': {'default': ['all']},
            'filter': {'default': '*'},
            'gather_timeout': {'type': 'int', 'default': 10},
        })

    # expected input to ansible_facts
    # gather_subset defaults to ['all']
   

# Generated at 2022-06-13 00:28:55.070415
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils.facts import ansible_collector
    from ansible.module_utils.facts.cache import FactsCache

    ns = PrefixFactNamespace(namespace_name='ansible', prefix='')
    all_collector_classes = default_collectors.collectors

    # don't add a prefix
    namespace = PrefixFactNamespace(namespace_name='ansible', prefix='')


# Generated at 2022-06-13 00:29:05.539151
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts.network.base import NetworkCollector
    from ansible.module_utils.facts.virtual.base import VirtualCollector
    import ansible.module_utils.facts.system.base as system_base
    import ansible.module_utils.facts.network.base as network_base
    import ansible.module_utils.facts.virtual.base as virtual_base
    from ansible.module_utils.facts.system.base import CollectMode

    try:
        import unittest.mock as mock
    except ImportError:
        import mock

    # set up patchers
    mock_module = mock.Mock()
    mock_module.params = {'filter': '*', 'gather_subset': ['all']}
    mock_collector = mock.Mock()
    mock_collector

# Generated at 2022-06-13 00:29:14.760039
# Unit test for function ansible_facts
def test_ansible_facts():

    from ansible.module_utils.facts.system import DistributionFactCollector
    from ansible.module_utils.facts.system import DistributionLegacyFactCollector
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.collector import AnsibleCollector

    class mock_module:
        params = {'gather_subset': ['all'], 'gather_timeout': 10, 'filter': '*'}

    def test_default_collectors():
        # test that a dict is returned
        assert isinstance(all_collector_classes, dict)
        # test the dict has some collectors
        assert DistributionLegacyFactCollector in all_collector_classes
        assert DistributionFactCollector in all_collector_classes


# Generated at 2022-06-13 00:29:26.928298
# Unit test for function ansible_facts
def test_ansible_facts():
    import ansible.module_utils.facts.ansible_facts as ansible_facts

    class AnsibleModule:
        def __init__(self, gather_subset, gather_timeout, filter_spec):
            self.params = {'gather_subset': gather_subset,
                           'gather_timeout': gather_timeout,
                           'filter': filter_spec}

    gather_subset = ['all', 'min']
    gather_timeout = 10
    filter_spec = ['test_collector']

    expected_facts_dict = {'test_collector': 'test_fact'}

    def test_collect(self, module):
        return expected_facts_dict

    mock_collect = test_collect
    ansible_facts.AnsibleCollector = mock_collect

    # Test required arguments
    module = Ans

# Generated at 2022-06-13 00:29:38.696426
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils import facts as test_facts
    del sys.modules['ansible.module_utils.facts']
    sys.modules['ansible.module_utils.facts'] = test_facts

    # Run the fact collection normally, using the default collector classes
    result = ansible_facts(module=MagicMock())

    # Verify that the result is within an acceptable range
    assert 50 < len(result) < 60
    assert 'distribution' in result
    assert 'dns' in result
    assert 'distribution_version' in result['distribution']
    assert 'fqdn' in result['dns']

    # Now, while miscollecting facts, verify that the results are different
    class DistroCollector(object):
        """A class that abuses the DistroCollector api."""


# Generated at 2022-06-13 00:29:48.140333
# Unit test for function ansible_facts
def test_ansible_facts():
    # simple testing function to run with pytest and confirm that it doesn't blow up
    # returns dict of ansible facts
    class FakeAnsibleModule(object):
        def __init__(self, module_name='', params={}):
            self.module_name = module_name
            self.params = params

    module = FakeAnsibleModule('test_ansible_facts',
                               {'gather_subset': ['all'],
                                'filter': '*',
                                'gather_timeout': 10})
    facts = ansible_facts(module)
    assert type(facts) == dict
    assert len(facts.keys()) > 0
    assert facts.get('ansible_facts')

# Generated at 2022-06-13 00:29:59.102255
# Unit test for function ansible_facts
def test_ansible_facts():
    import unittest
    import ansible.module_utils.facts.system.apparmor as apparmor
    import ansible.module_utils.facts.system.platform as platform
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts import ansible_collector

    class AnsibleModule:

        def __init__(self, params):
            self.params = params

    class MockAnsibleCollector(ansible_collector.AnsibleCollector):

        def get_all_collectors(self):
            self.all_collectors['ansible_pkg_mgr'] = platform.Distribution()
            self.all_collectors['ansible_apparmor'] = apparmor.AppArmor()

        def collect(self, module):
            self.get_all_

# Generated at 2022-06-13 00:30:11.544595
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts.namespace import PrefixFactNamespace

    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils.facts import ansible_collector

    class FakeModule(object):
        def __init__(self, gather_subset=None, gather_timeout=None, filter_spec=None):
            self.params = dict()
            if gather_subset:
                self.params['gather_subset'] = gather_subset
            if gather_timeout:
                self.params['gather_timeout'] = gather_timeout
            if filter_spec:
                self.params['filter_spec'] = filter_spec

    # setup collector classes

# Generated at 2022-06-13 00:30:23.123239
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.compat.tests import unittest
    from ansible.compat.tests.mock import patch, Mock

    test_dict = {'foo': 'bar'}

    class TestModule(object):
        def __init__(self):
            pass

        def params(self):
            return test_dict

    class FakeArgs(object):
        def __init__(self):
            self.gather_subset = None
            self.filter = None
            self.gather_timeout = None

    module = TestModule()
    test_args = FakeArgs()
    test_args.gather_subset = ['all']

# Generated at 2022-06-13 00:30:27.902167
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils.basic import AnsibleModule

    test_module = AnsibleModule(argument_spec={}, supports_check_mode=False)
    test_module.params['gather_subset'] = ['!all']
    facts = ansible_facts(test_module)

    assert 'fqdn' in facts
    assert 'os_family' in facts
    assert 'distribution' in facts
    assert 'distribution_version' in facts
    assert 'distribution_major_version' in facts
    assert 'timezone' in facts
    assert 'uptime_seconds' in facts

    assert 'all_ipv4_addresses' not in facts
    assert 'all_ipv6_addresses' not in facts
    assert 'architecture' not in facts
    assert 'default_ipv4' not in facts


# Generated at 2022-06-13 00:30:48.664296
# Unit test for function ansible_facts
def test_ansible_facts():

    from ansible.module_utils.facts import hardware
    from ansible.module_utils.facts import network

    # mock out hardware.get_all_facts
    hardware.get_all_facts = lambda: {'dmi': {'a': 1}}

    # mock network.get_all_facts
    network.get_all_facts = lambda: {'default_ipv4': {'address': 'x.x.x.x'}}

    # mock out the module itself
    class AnsibleModule:
        # noinspection PyMissingConstructor
        def __init__(self, *args, **kwargs):
            self.params = {}
        def exit_json(self, *args, **kwargs):
            pass

    # call the function under test
    module = AnsibleModule()
    facts = ansible_facts(module)

# Generated at 2022-06-13 00:30:53.340243
# Unit test for function ansible_facts
def test_ansible_facts():
    # Note: This function is not itself tested, it is just documented
    # Note: this is not really a unit test, it is an example of using the new-style fact collectors
    # in Ansible 2.2 or 2.3.
    # See test_default_collectors.py for more examples of how to unit test fact collector classes.

    from ansible.module_utils.facts import ansible_collector

    GATHERER_CLASSES = ansible_collector.get_gather_classes()

    # This is not a real module class. It just needs to be something that has a
    # return_values() method.
    module = FakeModule()

    # mock_facts is a dict containing the facts we want to force the fact
    # collection to produce.  It is used by the mock_fact_class class.

# Generated at 2022-06-13 00:31:05.458529
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.basic import AnsibleModule

    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils.facts.collector.script import ScriptCollector
    from ansible.module_utils.facts.collector.text import TextCollector

    module = AnsibleModule(argument_spec={'gather_subset': dict(required=False, type='list',
                                                                default=['all']),
                                          'gather_timeout': dict(required=False, type='int', default=10),
                                          'filter': dict(required=False, type='str', default='*')})

    # Note that the request_timeout's and set_options's are set to nonsense values to simplify
    # the testing of

# Generated at 2022-06-13 00:31:14.004641
# Unit test for function ansible_facts
def test_ansible_facts():
    import sys
    import os.path
    sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))


# Generated at 2022-06-13 00:31:24.112612
# Unit test for function ansible_facts
def test_ansible_facts():
    import unittest
    import platform
    import sys
    import os
    import io

    from ansible.module_utils import facts

    # build a module
    class FakeModule:
        def __init__(self):
            self.params = {'gather_wait': 0, 'gather_timeout': 1}
            self.fail_json = None

    class FakeConnection:
        pass

    class AnsibleModule:
        def __init__(self, argument_spec, bypass_checks=False, no_log=True,
                     check_invalid_arguments=True, mutually_exclusive=None,
                     required_together=None, required_one_of=None,
                     add_file_common_args=False, supports_check_mode=False):
            self.exit_json = None
            self.fail_json = None


# Generated at 2022-06-13 00:31:28.806648
# Unit test for function ansible_facts
def test_ansible_facts():
    DUMMY_MODULE = {'params': {'gather_subset': ['all']}}
    facts_dict = ansible_facts(module=DUMMY_MODULE)
    assert 'default_ipv4' in facts_dict
    assert 'default_ipv6' in facts_dict


if __name__ == '__main__':
    test_ansible_facts()

# Generated at 2022-06-13 00:31:36.099917
# Unit test for function ansible_facts
def test_ansible_facts():
    """ ansible_facts unit test.
    !!! NOTE: this test needs the path to this file to be the first in the PYTHONPATH
    """
    from ansible.module_utils.basic import AnsibleModule
    # Dummy class to represent AnsibleModule
    class AModule():
        def __init__(self, params):
            self.params = params

    params = {'filter': 'ansible_.*', 'gather_subset': 'all', 'gather_timeout': 10}
    module = AModule(params=params)
    ansible_facts_dict = ansible_facts(module)
    assert isinstance(ansible_facts_dict, dict)
    # Ensure all gathered facts begin with 'ansible_'
    for fact_key in ansible_facts_dict:
        assert fact_key.start

# Generated at 2022-06-13 00:31:42.372469
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils._text import to_text
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils.facts import ansible_collector
    from ansible.module_utils.facts import ansible_posix_default_collectors
    from ansible.module_utils.facts.ansible_local import NetworkCollector
    import os

    gather_subset = ['all']
    gather_timeout = 10

    # Don't add a prefix
    namespace = PrefixFactNamespace(namespace_name='ansible', prefix='')

    # Setup a collector
    collector1 = ansible_posix_default_collectors.PosixDefaultNetworkCollector()

    # Setup an instance of NetworkCollector

# Generated at 2022-06-13 00:31:53.747811
# Unit test for function get_all_facts
def test_get_all_facts():
    '''
    Unit tests for get_all_facts method
    '''
    from ansible.module_utils.facts import ansible_facts

    from ansible.module_utils.facts.collector import BaseFactCollector

    class FakeAnsibleModule(object):
        '''
        A fake ansible module to allow us to mock the params we are testing
        '''
        def __init__(self, params=None):
            self.params = dict()

            if params:
                self.params = params

    class FakeCollector(BaseFactCollector):
        '''
        A fake fact collector to allow us to mock the collection results we are testing
        '''

        def __init__(self):
            pass


# Generated at 2022-06-13 00:32:00.225742
# Unit test for function ansible_facts
def test_ansible_facts():
    import builtins
    import sys
    import os
    import tempfile
    if sys.version_info[0] == 3:
        from importlib import reload
    else:
        from imp import reload
    from ansible.module_utils import basic
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts import ansible_collector

    # mock_builtins = True forces all builtins to use mocks, even those that should not be mocked.
    # Testing the code at the end of this unit test is a test of the function ansible_facts.
    # To test that function, we need to mock functions that will be called by the code in
    # ansible_facts.
    #
    # We have updated the code in ansible_facts to get the object it needs using


# Generated at 2022-06-13 00:32:40.131898
# Unit test for function get_all_facts
def test_get_all_facts():
    import sys
    import os
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from units.compat.mock import patch
    from .common_mocks import mock_module, MockAnsibleModule, MockAnsibleModuleInstance

    def test_get_all_facts_mocked(mock_module, MockAnsibleModuleInstance):
        mocked_module = mock_module({'gather_subset': ['all']})
        inst = MockAnsibleModuleInstance(params={'gather_subset': ['all']})
        with patch.object(inst, 'AnsibleModule', return_value=mocked_module):
            result = get_all_facts(inst.AnsibleModule)

# Generated at 2022-06-13 00:32:47.616788
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts.virtual import VirtualFactCollector
    from ansible.module_utils.facts.network import NetworkFactCollector
    from ansible.module_utils.facts.system import SystemFactCollector

    # test that we return expected keys when gather_subset is 'all'
    #
    # Note: this test doesn't include 'network' since the NetworkFactCollector checks
    # for module.params.get('gather_subset').
    # 2.2/2.3 doesn't have a gather_subset param.
    # 2.0/2.1 doesn't have a gather_subset param.
    #
    # This means the test is not testing return of 'network' in the gather_subset = 'all'
    # case. This is a known issue.

# Generated at 2022-06-13 00:32:57.120160
# Unit test for function get_all_facts
def test_get_all_facts():
    # With gather_subset
    m = AnsibleModule(argument_spec=dict(gather_subset=dict(required=False, type='list', default=['all'])))
    check_all_facts(m)

    # With gather_subset and gather_timeout
    m = AnsibleModule(argument_spec=dict(gather_subset=dict(required=False, type='list', default=['all']),
                                          gather_timeout=dict(required=False, type='int', default=10)))
    check_all_facts(m)



# Generated at 2022-06-13 00:33:04.572607
# Unit test for function ansible_facts
def test_ansible_facts():
    # these are all of the things that can be part of gather_subset
    all_fact_subsets = ['all', '!nxos_lnx', 'nxos_lnx', 'hardware', 'network',
                        'virtual', 'facter', 'ohai', 'collectd']

    # create a dummy module to pass to ansible_facts
    class AnsibleModule(object):
        class AnsibleModule(object):
            def __init__(self, **kwargs):
                self.params = kwargs

    # run ansible_facts with each gather_subset
    for gather_subset in all_fact_subsets:
        module = AnsibleModule(gather_subset=gather_subset)
        facts = ansible_facts(module)
        keys = facts.keys()
        # check that ansible

# Generated at 2022-06-13 00:33:13.697227
# Unit test for function ansible_facts
def test_ansible_facts():
    import unittest
    try:
        import test.support
        import test.support.script_helper
    except ImportError:
        import unittest.mock as mock
        def setUpModule():
            pass
        def tearDownModule():
            pass
        def test_main():
            pass
    else:
        setUpModule = test.support.script_helper.setUpModule
        tearDownModule = test.support.script_helper.tearDownModule
        test_main = test.support.script_helper.test_main

    class TestAnsibleFacts(unittest.TestCase):

        def test_ansible_facts(self):

            class FakeModule(object):
                params = dict(gather_subset=['all'])

            module = FakeModule()

            facts_dict = ans

# Generated at 2022-06-13 00:33:26.195475
# Unit test for function ansible_facts
def test_ansible_facts():
    # Dummy AnsibleModule instance
    # see
    #   https://github.com/ansible/ansible/blob/2.2.0/lib/ansible/module_utils/basic.py#L158-L310
    #   https://github.com/ansible/ansible/blob/2.2.0/lib/ansible/module_utils/facts/__init__.py
    #   https://github.com/ansible/ansible/blob/2.2.0/lib/ansible/module_utils/facts/system/
    class AnsibleModule(object):
        def __init__(self, argument_spec, bypass_checks=False):
            self.argument_spec = argument_spec
            self.check_mode = bypass_checks

# Generated at 2022-06-13 00:33:26.884174
# Unit test for function ansible_facts
def test_ansible_facts():
    pass

# Generated at 2022-06-13 00:33:34.040677
# Unit test for function ansible_facts
def test_ansible_facts():

    # Generate a fake ansible module
    class FakeModule(object):
        def __init__(self, gather_subset=None, gather_timeout=None, filter=None):
            self.params = {}
            if gather_subset is not None:
                self.params['gather_subset'] = gather_subset
            if gather_timeout is not None:
                self.params['gather_timeout'] = gather_timeout
            if filter is not None:
                self.params['filter'] = filter

    # call ansible_facts
    facts = ansible_facts(FakeModule(gather_subset=['network']))
    # make sure we found the hostvars
    assert isinstance(facts, dict)
    # make sure we got the network facts
    assert 'ipv4' in facts



# Generated at 2022-06-13 00:33:43.665660
# Unit test for function ansible_facts
def test_ansible_facts():
    # we'll use an instance of AnsibleModule as a mock
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(
        argument_spec=dict(
            gather_subset=dict(type='list', default=['all']),
            #fqdn=dict(type='str' ),
            #gather_timeout=dict(type='int', default=10),
            #filter=dict(type='list' )
        )
    )

    # 2.2/2.3 api
    facts = ansible_facts(module, gather_subset=['all'])

    for fact in ('default_ipv4', 'distribution', 'distribution_version', 'pip'):
        assert fact in facts, 'Failed to collect fact {}'.format(fact)

    # 2.0/2

# Generated at 2022-06-13 00:33:50.632737
# Unit test for function ansible_facts
def test_ansible_facts():
    # GIVEN an AnsibleModule
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(argument_spec={})

    # WHEN ansible_facts is called
    facts = ansible_facts(module)

    # THEN the returned facts should contain a subset of the expected key, values
    assert 'ansible_all_ipv4_addresses' in facts
    assert 'ansible_machine' in facts
    assert 'ansible_package_mgr' in facts
    assert 'ansible_pkg_mgr' in facts
    assert 'ansible_python' in facts
    assert 'ansible_selinux' in facts
    assert 'ansible_service_mgr' in facts
    assert 'ansible_user_id' in facts