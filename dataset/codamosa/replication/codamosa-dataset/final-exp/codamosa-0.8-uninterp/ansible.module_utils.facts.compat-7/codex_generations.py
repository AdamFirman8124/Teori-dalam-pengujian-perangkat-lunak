

# Generated at 2022-06-13 00:24:17.524568
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.modules.system.setup import main as setup_main
    from ansible.module_utils.facts import get_all_facts
    from ansible.module_utils.facts import ansible_facts
    from ansible.module_utils.facts.namespace import PrefixFactNamespace


    module_args = dict(
        filter='ansible_lsb',
        gather_timeout=3
        )

    test_module_instance = setup_main.AnsibleModule(argument_spec=setup_main.argument_spec,
                                                     supports_check_mode=setup_main.supports_check_mode,
                                                     bypass_checks=True)
    test_module_instance.params = module_args

    assert not test_module_instance._name


# Generated at 2022-06-13 00:24:28.216562
# Unit test for function ansible_facts
def test_ansible_facts():
    import unittest
    import test.support
    import types
    import datetime

    class TestAnsibleModule(object):
        def __init__(self, params):
            self.params = params

    class TestCollector(object):
        def __init__(self, name):
            self.name = name
            self.called = False

        def collect(self, module):
            self.called = True
            return {'ansible_%s' % self.name: 'yes'}

    all_collectors = [TestCollector(name='A'), TestCollector(name='B'), TestCollector(name='C')]

    class TestFacts(unittest.TestCase):
        def test_ansible_facts(self):
            params = {'gather_subset': ['A']}
            m = Test

# Generated at 2022-06-13 00:24:32.937363
# Unit test for function get_all_facts
def test_get_all_facts():
    '''function get_all_facts must return the complete facts'''
    test_module = FakeModule()
    # gather_subset must be 'all'
    test_module.params['gather_subset'] = 'all'
    facts = get_all_facts(test_module)
    assert facts['default_ipv4']['address'] == '10.10.10.10'
    assert facts['distribution'] == 'Debian'


# Generated at 2022-06-13 00:24:42.858804
# Unit test for function ansible_facts
def test_ansible_facts():
    import pytest

    class MockAnsibleModule(object):
        def __init__(self, gather_timeout=10, gather_subset=None, filter='*'):
            super(MockAnsibleModule, self).__init__()
            self.gather_timeout = gather_timeout
            self.gather_subset = gather_subset
            self.filter = filter

        @property
        def params(self):
            return {'gather_timeout' : self.gather_timeout,
                    'gather_subset' : self.gather_subset,
                    'filter' : self.filter,
                    }

    # ensure gather_timeout defaults to 10, gather_subset to None, filter to '*'

# Generated at 2022-06-13 00:24:55.030817
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts import ansible_facts
    from ansible.module_utils._text import to_text

    # ansible_facts will only succeed (i.e. not throw)
    # if the module it is called from is an instance of the AnsibleModule class
    # The create_module function below is a mock AnsibleModule class.
    # It returns a dict of module_utils.facts.FACT_NAMES
    # and their values as mock values.

    def create_module():
        class AnsibleModule:
            def __init__(self, *args, **kwargs):
                pass

            def fail_json(self, *args, **kwargs):
                print('fail_json called with args: %s, kwargs: %s' % (args, kwargs))


# Generated at 2022-06-13 00:25:06.433413
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts.network.base import NetworkCollector
    NetworkCollector.get_facts = lambda x: dict(ansible_default_ipv4=dict(address='1.2.3.4',
                                                                          alias='eth0:0',
                                                                          interface='eth0',
                                                                          macaddress='00:11:22:33:44:55'))

    from ansible.module_utils.facts.system.base import SystemCollector
    SystemCollector.get_distribution = lambda x: dict(distribution='debian')
    SystemCollector.get_distribution_release = lambda x: 'jessie'

    from ansible.module_utils.facts.system.distribution import DistributionCollector

# Generated at 2022-06-13 00:25:18.030697
# Unit test for function ansible_facts
def test_ansible_facts():
    import sys

    import pytest

    # monkey patch sys.path so we can import real ansible modules
    test_dir_path = os.path.dirname(os.path.realpath(__file__))
    sys.path.append(os.path.dirname(test_dir_path))
    import test_ansible_module
    sys.path.pop()

    # test ansible_facts function
    ansible_facts_module = test_ansible_module.TestAnsibleFacts()
    facts = ansible_facts(ansible_facts_module)

# Generated at 2022-06-13 00:25:20.975885
# Unit test for function ansible_facts
def test_ansible_facts():
    assert True

# Generated at 2022-06-13 00:25:29.209065
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.facts.collector import make_fact_cache_key
    from ansible.module_utils.facts.namespace import PrefixFactNamespace

    from ansible.module_utils.facts.default_collectors import (
        FacterCollector,
        OhaiCollector,
    )

    from ansible.module_utils.facts.ansible_collector import (
        AnsibleCollector,
        minimize_subset,
    )

    # Create an AnsibleModule to mimic the basic module class

# Generated at 2022-06-13 00:25:40.752870
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.six import PY3
    ansible_facts = dict()
    if PY3:
        exec("from ansible.module_utils.facts.os.freebsd import AnsibleFreeBSDModule as AnsibleModule")
    else:
        exec("from ansible.module_utils.facts.os.freebsd import AnsibleFreeBSDModule as AnsibleModule")
    m = AnsibleModule(argument_spec=dict())
    m.params = {'gather_subset': 'all',
                'filter': '*'}
    result = ansible_facts(m)
    assert result
    assert all(isinstance(f, (type(result), None.__class__)) for f in result.values())
    assert result['version'] == '10.1-STABLE'

# Generated at 2022-06-13 00:25:53.474077
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts.collector import BaseFactCollector

    class TestCollector(BaseFactCollector):
        name = 'test_fact'

        def collect(self, module=None, collected_facts=None):
            return {'test_fact_name': 'test_fact_value'}

    class MockModule(object):
        def __init__(self, gather_subset):
            self.params = {'gather_subset': gather_subset,
                           'gather_timeout': None,
                           'filter': '*'}

    all_collector_classes = default_collectors.collectors + [TestCollector]

    # don't add a prefix
    namespace = PrefixFactNamespace(namespace_name='ansible', prefix='')


# Generated at 2022-06-13 00:25:59.630099
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts import ansible_facts
    import ansible.module_utils.facts.system
    facts_dict = ansible_facts(ansible.module_utils.basic.AnsibleModule(argument_spec={}))
    assert to_bytes(facts_dict['python']['version']['major']) >= to_bytes(2)

# Generated at 2022-06-13 00:26:09.448800
# Unit test for function ansible_facts
def test_ansible_facts():
    # TODO: when we have a unit test framework, move unit test to a separate module,
    # and add unit test for get_all_facts
    class FakeAnsibleModule(object):

        def __init__(self, params):
            self.params = params

    # test with no filter_spec, will collect all facts
    fake_module = FakeAnsibleModule({'gather_subset': 'all'})
    facts = ansible_facts(fake_module)
    assert 'default_ipv4' in facts
    assert 'default_ipv6' in facts
    assert facts['domain'] is None

    # test with no filter_spec, will collect all facts
    fake_module = FakeAnsibleModule({'gather_subset': 'all', 'filter': '*domain'})
    # filter included 'domain' and

# Generated at 2022-06-13 00:26:20.134573
# Unit test for function ansible_facts
def test_ansible_facts():

    # ansible_facts returns a dict
    # mapping the bare fact name ('default_ipv4' with no 'ansible_' namespace) to the fact value.

    class AnsibleModule:

        params = {
            'gather_subset': ['network', 'virtual'],
            'gather_timeout': 10
        }

        def __init__(self, *args, **kwargs):
            pass

    from ansible.module_utils.facts import default_collectors
    import platform

    class FakeCollector:

        def __init__(self, *args, **kwargs):
            pass


# Generated at 2022-06-13 00:26:31.814512
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.basic import AnsibleModule
    import sys

    py_module_path = sys.modules['ansible.module_utils.facts'].__file__
    py_module_path = py_module_path.replace('.pyc', '.py')
    py_module_path = py_module_path.replace('.pyo', '.py')

    module = AnsibleModule(argument_spec={'gather_subset': dict(type='list', default=['!all'])})

    facts = ansible_facts(module=module)

    assert 'ansible_python' in facts
    assert facts['ansible_python'] == {'has_sslcontext': False, 'version': (2, 6, 6, 'final', 0), 'path': py_module_path}

# Generated at 2022-06-13 00:26:42.325997
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils.facts import ansible_collector
    from ansible.module_utils import basic
    import os

    module_name = 'test_module'
    module_args = dict()

    module_path = '%s/module_utils/facts/test_module.py' % (os.path.dirname(os.path.realpath(__file__)))

    if os.path.exists(module_path):
        os.remove(module_path)

    with open(module_path, 'w') as fd:
        fd.write("#!/usr/bin/python\n")

# Generated at 2022-06-13 00:26:52.097938
# Unit test for function ansible_facts
def test_ansible_facts():
    # Test 1: check facts collection by passing all subset

    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(argument_spec={})

    # ansible_facts returns a dict mapping the bare fact name ('default_ipv4' with no 'ansible_' namespace) to
    # the fact value.
    facts_dict = ansible_facts(module, ['all'])

    # ansible_facts returns a dict mapping the bare fact name ('default_ipv4' with no 'ansible_' namespace) to
    # the fact value.
    assert facts_dict['distribution'] == 'Unknown'
    assert facts_dict['distribution_release'] == 'Unknown'
    assert facts_dict['distribution_version'] == 'Unknown'



# Generated at 2022-06-13 00:27:01.994563
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts import ansible_facts
    from ansible.module_utils.facts.system.distribution import DistributionFactCollector
    from ansible.module_utils.facts.system.distribution import Distribution
    from ansible.module_utils.facts.system.distribution import LinuxDistribution
    from ansible.module_utils.facts.system.distribution import RedHatDistribution
    from ansible.module_utils.facts.system.distribution import DebianDistribution
    from ansible.module_utils.facts.namespace import PrefixFactNamespace

    class MockModule(object):
        def __init__(self):
            self.params = dict(gather_subset=['distribution'])


# Generated at 2022-06-13 00:27:12.450872
# Unit test for function get_all_facts
def test_get_all_facts():

    from ansible.module_utils.basic import AnsibleModule

    import json

    test_module = AnsibleModule(
        argument_spec=dict(
            gather_subset=dict(required=False, type='list', default='all'),
            gather_network_resources=dict(required=False, type='list', default='all'),
            gather_timeout=dict(required=False, type='int', default=10),
            filter=dict(required=False, type='str', default='*'),
            config_file=dict(required=False, type='path')
        ),
        supports_check_mode=False
    )

    ansible_facts_dict = ansible_facts(test_module)

    print(json.dumps(ansible_facts_dict, indent=4, sort_keys=True))



# Generated at 2022-06-13 00:27:21.354627
# Unit test for function get_all_facts
def test_get_all_facts():
    try:
        # Ansible 2.3+
        from ansible.module_utils.facts import get_all_facts
    except ImportError:
        # Ansible 2.2
        from ansible.module_utils.facts import ansible_facts as get_all_facts
    if not callable(get_all_facts):
        # Ansible 2.0/2.1
        get_all_facts = get_all_facts()
    module = dict(params=dict(gather_subset=['all', 'network']))
    assert 'ansible_' == get_all_facts(module).__class__.__name__

# Generated at 2022-06-13 00:27:33.339091
# Unit test for function ansible_facts
def test_ansible_facts():
    import copy
    from ansible.module_utils.facts import namespace
    facts_dict = ansible_facts(AnsibleModule(argument_spec={}), gather_subset=['all'])
    assert isinstance(facts_dict, dict)

    # extract the set of facts provided by default collectors
    default_fact_names = []
    for fact in namespace.get_all_fact_names(default_collectors.collectors):
        default_fact_names.append(fact.name)

    # ensure that all default facts are present
    for name in default_fact_names:
        assert name in facts_dict

    # ensure that new facts have been added
    assert 'fips' in facts_dict

    # Test the namespace.PrefixFactNamespace class

# Generated at 2022-06-13 00:27:45.743939
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils.facts import ansible_collector
    from ansible.module_utils._text import to_text

    def mock_ansible_module(name):
        class MockAnsibleModule:
            def __init__(self):
                self.params = dict()

        return MockAnsibleModule()

    # test gathering all facts
    module = mock_ansible_module('test_ansible_facts_1')

    facts_dict = ansible_facts(module)

    assert 'distribution' in facts_dict
    assert 'distribution_release' in facts_dict
    assert 'distribution_version' in facts_dict
    assert 'python' in facts

# Generated at 2022-06-13 00:27:50.015151
# Unit test for function ansible_facts
def test_ansible_facts():

    # import the facts module class
    from ansible.modules.system.facts import Facts

    # instantiate an AnsibleModule with the correct parameters
    module = Facts.AnsibleModule(argument_spec=Facts.argument_spec,
                                 bypass_checks=False)

    '''
    # mock the params
    module.params = {'filter': '*',
                     'gather_timeout': 10, 'gather_subset': None}

    # collect the facts
    facts = ansible_facts(module)

    # check for the 'default_ipv4' fact
    assert 'default_ipv4' in facts

    # check that the default_ipv4 is '127.0.0.1'
    assert facts['default_ipv4'] == '127.0.0.1'
    '''

    # mock

# Generated at 2022-06-13 00:27:56.394115
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.basic import AnsibleModule

    # mock module
    module = AnsibleModule(
        argument_spec={
            "gather_subset": dict(default='all', type='list'),
            "gather_timeout": dict(default=10, type='int'),
            "filter": dict(default='*', type='str'),
        },
    )

    result = get_all_facts(module)
    assert 'distribution' in result



# Generated at 2022-06-13 00:28:04.054453
# Unit test for function ansible_facts
def test_ansible_facts():
    import unittest
    import AnsibleModuleMock
    import test_collector

    class TestAll(unittest.TestCase):
        def setUp(self):
            '''set up before all tests in this class'''
            self.mock_ansible_module = AnsibleModuleMock.AnsibleModuleMock('test_collector')
            self.facts = ansible_facts(self.mock_ansible_module, gather_subset='all')

        def testFacts(self):
            self.assertEqual(self.facts['interfaces'], ['lo', 'eth0', 'eth1'])

# Generated at 2022-06-13 00:28:09.575992
# Unit test for function get_all_facts
def test_get_all_facts():

    import ansible.module_utils.facts

    # 2.4 or later
    if hasattr(ansible.module_utils.facts, 'get_all_facts'):

        # get_all_facts is a function (not a method, it doesn't take a module param)
        assert(callable(get_all_facts))
        return

    # 2.3 or earlier
    assert(False)

# Generated at 2022-06-13 00:28:20.983481
# Unit test for function get_all_facts
def test_get_all_facts():
    '''test the get_all_facts function by loading a minimal AnsibleModule instance,
    providing a gather_subset, and making sure it was picked up correctly.
    '''
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.facts.namespace import PrefixFactNamespace

    gather_subset = ['min']
    module_args = dict(gather_subset=gather_subset)
    module = AnsibleModule(argument_spec=dict(), supports_check_mode=False, bypass_checks=False, no_log=True)

    # get the facts
    facts = get_all_facts(module)

    # make sure the value is present in the facts
    assert facts['os_family'] == 'RedHat'

    # make sure the 'ansible_' namespace is not

# Generated at 2022-06-13 00:28:28.338777
# Unit test for function ansible_facts
def test_ansible_facts():
    try:
        from ansible.module_utils.facts import ansible_collector
    except ImportError:
        # ansible 2.7 dropped ansible_collector
        # set to None so test_ansible_facts_compat_27 is run
        ansible_collector = None

    if ansible_collector is None:
        # ansible 2.7+
        from ansible.module_utils.facts import Facts
        from ansible.module_utils.facts import get_default_collectors
        from ansible.module_utils.facts import get_collector_plugins

        output = ansible_facts(module=None)
        assert isinstance(output, dict)
        # make sure fact collection was done for all collectors
        for collector in get_default_collectors():
            assert output.get(collector)

# Generated at 2022-06-13 00:28:32.338023
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts import ansible_collector

    from ansible.module_utils.facts.system.distribution import DistributionFactCollector
    from ansible.module_utils.facts.system.platform import PlatformFactCollector
    from ansible.module_utils.facts.system.capabilities import CapabilitiesFactCollector
    from ansible.module_utils.facts.system.selinux import SElinuxFactCollector
    from ansible.module_utils.facts.system.fips import FipsFactCollector
    from ansible.module_utils.facts.system.lsb import LsbFactCollector
    from ansible.module_utils.facts.system.pkg_mgr import PkgMgrFactCollector

# Generated at 2022-06-13 00:28:41.422565
# Unit test for function ansible_facts
def test_ansible_facts():
    # Mock the module
    module = Mock()
    module.params.get.return_value = None

    fact_dict = ansible_facts(module)
    assert 'date_time' in fact_dict
    assert 'local' in fact_dict

    # should support gather_timeout
    module.params.get.return_value = None
    module.params.get.return_value = 3
    fact_dict = ansible_facts(module)
    assert 'date_time' in fact_dict
    assert 'local' in fact_dict

    # should support gather_subset
    module.params.get.return_value = None
    module.params.get.return_value = ['local', 'date_time']
    fact_dict = ansible_facts(module)
    assert 'date_time' in fact_dict

# Generated at 2022-06-13 00:28:58.384751
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts.ansible_collector import AnsibleFileFactsCollector
    import ansible.module_utils.facts.collector.file
    import ansible.module_utils.facts.collector

    class AnsibleModuleMock(object):
        def __init__(self):
            self.params = {'filter': '*', 'gather_subset': ['all'],
                           'gather_timeout': 10}

    class AnsibleFileFactsCollectorMock(AnsibleFileFactsCollector):
        def add(self, collector_cls):
            pass

    # Test create collector object from ansible_facts()
    ansible_facts(module=AnsibleModuleMock())

    # Test create ansible's collector object from ansible_collector.get_ansible_collector

# Generated at 2022-06-13 00:29:07.668281
# Unit test for function get_all_facts
def test_get_all_facts():
    # TODO: these tests should be moved into their own unit test
    # ansible.module_utils.facts.get_all_facts module

    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils.facts import ansible_collector

    # mock class for expected module methods
    class AnsibleModule(object):

        def __init__(self, params):
            self.params = params

    # end mock class

    # module parameters
    good_params = dict(gather_subset=['all'])
    bad_params = dict(gather_subset='bad')

    # mock instance of an AnsibleModule
    module = AnsibleModule(params=good_params)

    # make sure gather_sub

# Generated at 2022-06-13 00:29:12.950375
# Unit test for function ansible_facts
def test_ansible_facts():
    # Create a module stub
    module = AnsibleModule(
        argument_spec=dict(
            gather_subset=dict(required=False, default=['all']),
            gather_timeout=dict(required=False, default=10)
        )
    )

    # Run the ansible_facts function
    facts = ansible_facts(module)

    # Verify that platform.system_alias() is in the results
    assert 'system_alias' in facts

# Generated at 2022-06-13 00:29:20.445231
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts.gathering import get_collector_classes
    from ansible.module_utils.facts import ansible_collector

    # ansible_facts could use the ansible_collector.get_ansible_collector method,
    # which would in turn use the ansible_collector.get_collector_classes method
    # to get a list of collectors. get_collector_classes is tested in a separate
    # unit test. So ansible_facts is tested here by mocking out the get_collector_classes
    # method.

    # patch get_collector_classes to return a list containing a single collector,
    # a mock_collector, which returns a single fact, the mock_fact_dict.

    mock_collector_class = ansible_collector.AnsibleCollector._get_collect

# Generated at 2022-06-13 00:29:28.739620
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts.namespace import PrefixFactNamespace

    # assert the ansible_facts just uses the fact_collector
    class FakeModule:
        def __init__(self, params):
            self.params = params

    class FakeCollector:
        def __init__(self, gather_subset=None):
            self.gather_subset = gather_subset

        def collect(self, module=None):
            return dict(gather_subset=self.gather_subset)

    gather_subset = ['!foo', 'bar']
    params = dict(
        gather_subset=gather_subset,
        filter='*',
    )
    module = FakeModule(params=params)

# Generated at 2022-06-13 00:29:33.617885
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts import get_all_facts
    from ansible.module_utils.facts import ansible_facts
    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils.facts import ansible_collector
    from ansible.module_utils.facts.namespace import PrefixFactNamespace

    class FakeAnsibleModule:
        def __init__(self):
            self.params = {}

    class FakeCollector:
        def __init__(self, namespace, filter_spec, gather_subset, gather_timeout, minimal_gather_subset):
            self.namespace = namespace
            self.filter_spec = filter_spec
            self.gather_subset = gather_subset
            self.gather_timeout = gather_timeout
            self.min

# Generated at 2022-06-13 00:29:43.768501
# Unit test for function ansible_facts
def test_ansible_facts():
    import json
    import ansible.module_utils.facts.system.distribution as distribution
    # pylint: disable=unused-variable
    class AnsibleModule:

        def __init__(self, params):
            self.params = params

    class LinuxDistribution(distribution.LinuxDistribution):
        def __init__(self, module):
            super(LinuxDistribution, self).__init__(module)
            self.distribution = 'Raspbian'
            self.major_version = '9'

    distribution.LinuxDistribution = LinuxDistribution


# Generated at 2022-06-13 00:29:54.784293
# Unit test for function ansible_facts
def test_ansible_facts():
    import ansible.module_utils.facts.namespace
    import ansible.module_utils.facts.default_collectors
    import ansible.module_utils.facts.ansible_collector
    import ansible.module_utils.facts.cache
    import ansible.module_utils.facts.hardware
    import ansible.module_utils.facts.processor
    import ansible.module_utils.facts.virtual
    from ansible.module_utils._text import to_bytes

    import os
    import sys
    import tempfile
    import unittest

    from collections import namedtuple

    from ansible.plugins.loader import add_all_plugin_dirs
    from ansible.module_utils.facts import ansible_collector

    from ansible.module_utils.facts.namespace import PrefixFactNamespace

# Generated at 2022-06-13 00:30:02.569971
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils.facts import ansible_collector

    import mock
    import copy

    # gather_subset_functions is expected to be a subset of ansible_facts_functions
    gather_subset_functions = ['cmdline', 'local']

# Generated at 2022-06-13 00:30:11.501739
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.basic import AnsibleModule
    import os

    this_dir = os.path.dirname(os.path.realpath(__file__))
    path_to_module = os.path.join(this_dir, '../../../../lib/ansible/modules/system/setup.py')
    module = AnsibleModule(path_to_module=path_to_module)
    result = ansible_facts(module)

    assert result

    for fact in result:
        assert result[fact] is not None, ("fact '%s' should not be 'None' "
                                          "actual value was: %s" % (fact, result[fact]))

# Generated at 2022-06-13 00:30:35.864926
# Unit test for function ansible_facts
def test_ansible_facts():
    '''Unit test for ansible.module_utils.facts.facts_module.ansible_facts'''
    from ansible.module_utils import basic
    from ansible.module_utils.facts.facts import Facts
    from ansible.module_utils.facts.collector.file import Directory

# Generated at 2022-06-13 00:30:42.229635
# Unit test for function ansible_facts
def test_ansible_facts():
    # Fact collector for '*'
    all_fact_collector = ansible_facts('*')

    # Load in the ansible_facts.yaml file
    all_fact_file = open(os.path.join(os.path.dirname(__file__), '../../ansible_facts.yaml'))
    yaml_all_fact_file = yaml.load(all_fact_file)

    # Compare the two dictionaries
    assert all_fact_collector == yaml_all_fact_file

# Generated at 2022-06-13 00:30:53.458977
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts.network.base import NetworkCollector
    from ansible.module_utils.facts.system.base import SystemCollector

    class TestNetworkCollector(NetworkCollector):
        COLLECTOR_NAME = 'test'

        def collect(self, module=None, collected_facts=None):
            return {'test_network_fact': 12345}

    class TestSystemCollector(SystemCollector):
        COLLECTOR_NAME = 'test'

        def collect(self, module=None, collected_facts=None):
            return {'test_system_fact': 12345}

    class TestModule:
        def __init__(self, params=None,
                     gather_subset=None,
                     gather_timeout=10):
            self.params = params
            self.gather_subset = gather

# Generated at 2022-06-13 00:31:05.465904
# Unit test for function ansible_facts
def test_ansible_facts():
    '''
    Exercises function ansible_facts() with an AnsibleModule and returns facts
    collected from the OS.
    '''
    from ansible.module_utils.basic import AnsibleModule
    import argparse

    parser = argparse.ArgumentParser(description='Ansible module for network devices')
    parser.add_argument('file', help='path to task yaml')
    args, unknown_args = parser.parse_known_args()

    task_args = {
        'filter': 'ansible'
    }

    module = AnsibleModule(argument_spec=task_args, supports_check_mode=False)
    got = ansible_facts(module, gather_subset=None)

    # Should return a dict with keys and values
    assert isinstance(got, dict)

    # Every key in these facts should

# Generated at 2022-06-13 00:31:09.803048
# Unit test for function ansible_facts
def test_ansible_facts():

    from ansible.compat.tests.mock import Mock, patch
    from ansible.module_utils import facts

    class TestModule:

        def __init__(self):
            self.params = dict()

    class TestFactsModule:

        def __init__(self, params={}, facts={}):
            self.params = params
            self.ansible_facts = facts
            self.exit_args = None
            self.fail_json_args = None

        def exit_json(self, **kwargs):
            self.exit_args = kwargs

        def fail_json(self, **kwargs):
            self.fail_json_args = kwargs
            raise Exception('fail_json exception')


# Generated at 2022-06-13 00:31:21.556162
# Unit test for function ansible_facts
def test_ansible_facts():

    # it's not obvious how to test, as ansible_facts depends on the
    # availability of a module as a parameter.
    module = None

    # minimal test case where we don't filter any facts, and
    # try to gather all facts without a gather_subset param
    facts_dict = ansible_facts(module)

    # ansible_all_ipv4_addresses should be in the result, because it is one of the default
    # values
    assert 'all_ipv4_addresses' in facts_dict

    # ansible_bios_date should NOT be in the result, because it is not one of the default
    # values
    assert 'bios_date' not in facts_dict

    # ansible_bios_version should not be in the result, because we have set
    # filter='*', which excludes all

# Generated at 2022-06-13 00:31:24.764883
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts import ModuleStub
    ms = ModuleStub()
    facts_dict = ansible_facts(module=ms)
    assert 'hostname' in facts_dict
    assert facts_dict['hostname'] == 'localhost'

# Generated at 2022-06-13 00:31:33.282317
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.six.moves import mock

    with mock.patch('ansible.module_utils.basic.AnsibleModule.params', new_callable=dict) as mock_params:
        mock_params['gather_subset'] = ['all']
        mock_params['gather_timeout'] = 10
        mock_params['filter'] = '*'

        # mock for basic. AnsibleModule
        from ansible.module_utils.basic import AnsibleModule
        from ansible.module_utils.facts import ansible_facts
        from ansible.module_utils.facts.system.distribution import DistributionFactCollector

# Generated at 2022-06-13 00:31:41.822802
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils import basic
    from ansible.module_utils.facts import collector

    module = basic.AnsibleModule(argument_spec={})

    module_mock = Mock()
    module_mock.params = {'gather_subset': ['all'],
                          'gather_timeout': 10,
                          'filter': '*'}

    collector.collect.return_value = {'testfact': 'testvalue'}

    facts = ansible_facts(module_mock)

    assert facts['testfact'] == 'testvalue'

# Generated at 2022-06-13 00:31:53.203113
# Unit test for function ansible_facts
def test_ansible_facts():
    '''test function ansible_facts

    ansible_facts is a function, not a class.

    So we use a mock AnsibleModule, and call ansible_facts with it.
    '''
    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils.facts import ansible_collector

    module = FakeAnsibleModule(gather_subset=['all'])

    # noinspection PyProtectedMember
    assert getattr(ansible_collector, '_fact_collectors') == {}

    # noinspection PyProtectedMember

# Generated at 2022-06-13 00:32:31.344125
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils.facts import get_all_facts
    from ansible.module_utils.facts import ansible_facts
    from ansible.module_utils.facts.utils import AnsibleModule

    module = AnsibleModule(argument_spec={'gather_timeout': { 'default': 10 },
                                          'gather_subset': { 'default': ['all']},
                                          'filter': { 'default': '*' }})

    gaf_dict = get_all_facts(module)
    af_dict = ansible_facts(module)

    assert gaf_dict == af_dict

# Generated at 2022-06-13 00:32:38.457068
# Unit test for function ansible_facts
def test_ansible_facts():
    '''Unit test for function ansible_facts'''

    class FakeModule(object):
        '''Fake module class used for testing'''
        def __init__(self):
            self.params = {}

    fake_module = FakeModule()

    facts_dict = ansible_facts(fake_module)

    assert isinstance(facts_dict, dict)
    assert 'default_ipv4' in facts_dict
    assert isinstance(facts_dict['default_ipv4'], dict)
    assert isinstance(facts_dict['default_ipv4']['interface'], str)
    assert 'localhost' in facts_dict['default_ipv4']['interface']



# Generated at 2022-06-13 00:32:46.738483
# Unit test for function get_all_facts
def test_get_all_facts():
    import json
    import platform
    import socket
    import sys

    from collections import namedtuple

    from ansible.module_utils import facts

    # Fake module API
    AnsibleModule = namedtuple('AnsibleModule', ['params'])

    module = AnsibleModule({'gather_subset': ['min', 'hardware'], 'gather_timeout': 60})

    actual_fact_dict = facts.get_all_facts(module)

    assert type(actual_fact_dict) == dict


# Generated at 2022-06-13 00:32:59.636895
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.facts import get_all_facts

    module = AnsibleModule(argument_spec={
        'gather_subset': dict(type='str', default='!all'),
        'filter': dict(type='str', default='*')
    })

    # As of Ansible 2.1, AnsibleModule allows only unicode input.
    # The actual param passed to the module is always a unicode object.
    # So, we convert the input here to unicode before passing it to the module
    gather_subset = '!all'

# Generated at 2022-06-13 00:33:06.966400
# Unit test for function get_all_facts
def test_get_all_facts():

    class Module(object):
        def __init__(self, params):
            self.params = params
            self.facts = None

        def exit_json(self, facts=None):
            self.facts = facts

    m = Module(dict(gather_subset='some, subset'))
    get_all_facts(m)
    assert m.facts is not None
    assert m.facts.get('ansible_some') is not None
    assert m.facts.get('ansible_subset') is not None


# Generated at 2022-06-13 00:33:15.107891
# Unit test for function ansible_facts
def test_ansible_facts():

    class MockModule(object):
        def __init__(self, filters):
            self.params = {'filter': filters, 'gather_subset': None}

    import pytest
    from ansible.module_utils.facts import default_collectors
    all_fact_names = [fact.name for fact in default_collectors.collectors]

    # test that we can retrieve all facts
    with pytest.warns(None) as record:
        ansible_facts(MockModule(filter_spec='*'), gather_subset=all_fact_names)
    assert len(record) == 0, "should not have emitted any warnings"

    # test that we can retrieve all facts even if not all gather_subsets are listed

# Generated at 2022-06-13 00:33:26.728905
# Unit test for function ansible_facts
def test_ansible_facts():

    import os
    import io
    import sys
    from ansible.module_utils.facts import collector
    from ansible.module_utils.facts import default_collectors

    class FakeModule(object):
        def __init__(self):
            self.params = dict()


# Generated at 2022-06-13 00:33:34.110012
# Unit test for function ansible_facts
def test_ansible_facts():
    '''Unit test for function ansible_facts'''
    import pytest
    from ansible.module_utils.facts.facts import Facts

    facts_data = {'distribution': {'distribution': 'other', 'distribution_release': '1.0', 'distribution_version': '1.2.3'},
                  'lsb': {'major_release': 1, 'distributor_id': 'debian', 'description': 'debian 1.2.3 1.0', 'codename': 'jessie',
                          'release': '1.2.3'},
                  'system': 'Linux'}

    test_facts = Facts(facts_data)

    class MockAnsibleModule(object):
        def __init__(self, params):
            self.params = params


# Generated at 2022-06-13 00:33:43.086565
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils.basic import AnsibleModule
    import ast

    test_params = ast.literal_eval('''{
            "gather_subset": [
                "all"
            ]
    }''')

    test_module = AnsibleModule(argument_spec=dict(
        gather_subset=dict(required=False, type='list'),
        gather_timeout=dict(required=False, type='int'),
        filter=dict(required=False),
    ),
        supports_check_mode=False,
        check_invalid_arguments=False,
    )

    test_module.params = test_params

    facts = get_all_facts(test_module)
    assert len(facts) > 1

# Generated at 2022-06-13 00:33:50.189600
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.module_utils._text import to_text
    from ansible.module_utils.facts import default_collectors

    # This is what a dict of facts looks like at the end of the ansible_facts function
    # for a RedHat 6 Linux system.