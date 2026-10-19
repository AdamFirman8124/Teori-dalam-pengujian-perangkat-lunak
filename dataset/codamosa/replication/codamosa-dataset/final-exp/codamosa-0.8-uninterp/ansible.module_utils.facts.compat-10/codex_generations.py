

# Generated at 2022-06-13 00:24:16.452701
# Unit test for function get_all_facts
def test_get_all_facts():

    from ansible.module_utils.facts.core import AnsibleModuleMock
    import ansible.module_utils.facts.namespace as namespace_utils

    test_config = {'gather_subset': '!all', 'filter': '*', 'gather_timeout': 10}

    test_module = AnsibleModuleMock(params=test_config)

    # Assume that we were given an empty namespace
    # to start with
    assert len(namespace_utils.AnsibleFactNamespace.current_fact_namespace) == 0

    # Get all facts
    get_all_facts(test_module)

    # Verify that the namespace was populated
    assert len(namespace_utils.AnsibleFactNamespace.current_fact_namespace) > 0

    # Verify that the module's ansible_facts dictionary has all the

# Generated at 2022-06-13 00:24:27.619487
# Unit test for function ansible_facts

# Generated at 2022-06-13 00:24:35.882298
# Unit test for function get_all_facts
def test_get_all_facts():
    # Will fail if tested on an older ansible version without the gather_subsets param,
    # but should still run (and pass) on an older ansible version

    # Two basic tests, with empty gather_subset, and all.
    # Note: several facts are not tested, because they are not always available
    # (e.g. /proc/1/statm is not available if running tests under docker)

    # Empty gather_subset
    class Empty_Params:
        gather_subset = []
    class Empty_AnsibleModule:
        def __init__(self):
            self.params = Empty_Params()
    assert get_all_facts(Empty_AnsibleModule()) == {}

    # All gather_subset
    class All_Params:
        gather_subset = ['all']

# Generated at 2022-06-13 00:24:45.146071
# Unit test for function ansible_facts
def test_ansible_facts():

    import sys
    if sys.version_info[0] > 2:
        from unittest.mock import Mock
    else:
        from mock import Mock

    class Module(object):

        def __init__(self):
            self.params = {'filter': 'ansible_*'}
            self.facts = None

        def exit_json(self, **kwargs):
            self.facts = kwargs['ansible_facts']
            self.exited = True

        def fail_json(self, **kwargs):
            self.exited = False

    test_module = Module()

    test_module.run_command = Mock(return_value=(0, 'PARAMETER=VALUE', ''))

    ansible_facts(module=test_module)

    assert test_module.exited

# Generated at 2022-06-13 00:24:52.721398
# Unit test for function ansible_facts
def test_ansible_facts():
    '''
        Unit test for function ansible_facts
    '''
    print("Unit test for function ansible_facts")
    from ansible.module_utils.facts import ansible_facts
    test_facts_dict = ansible_facts()

    print("\nTest results:")
    for key, value in test_facts_dict.items():
        print(key + ":\n" + str(value))


if __name__ == '__main__':
    test_ansible_facts()

# Generated at 2022-06-13 00:24:58.440157
# Unit test for function get_all_facts
def test_get_all_facts():
    '''Test the get_all_facts function'''

    class MockModule(object):
        params = {'gather_subset': 'all'}

    mock_module = MockModule()

    fact_dict = get_all_facts(mock_module)
    assert 'ansible_architecture' in fact_dict



# Generated at 2022-06-13 00:25:05.340251
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils._text import to_bytes

    class Module(object):
        pass
    module = Module()
    module.params = dict()
    module.params['gather_subset'] = ['!all']
    module.params['filter'] = 'foo'
    module.params['gather_timeout'] = 0.1

    module.run_command = lambda args, check_rc=False, close_fds=False: (1, to_bytes('foo'), '')

    facts = ansible_facts(module)
    assert facts['failed_when_result'] == 1
    assert facts['failed_when_rc'] == 1
    assert facts['failed_when_stdout'] == 'foo'
    assert facts['failed_when_stderr'] == ''
    assert 'failed_when_delta' in facts


# Generated at 2022-06-13 00:25:11.003409
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts.network.base import NetworkCollector
    from ansible.module_utils.facts.network.linux import LinuxInterfacesNetworkCollector
    import mock

    # test with a mock module
    module = mock.Mock()

    # cannot mock attribute __getattr__, so need to mock the module object's attrs we're interested in
    gather_subset = ['all']
    module.params = {'gather_subset': gather_subset}

    # run the unit test
    facts_dict = ansible_facts(module)
    # validate result
    assert facts_dict['distribution'] == 'Unknown'
    assert 'ansible_default_ipv4' in facts_dict



# Generated at 2022-06-13 00:25:20.791108
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts.utils import get_distribution as gd

    from ansible.module_utils.facts.test_utils import set_module_args, exit_json

    from ansible.module_utils.facts import ansible_collector

    from ansible.module_utils.facts import default_collectors

    from ansible.module_utils.facts.namespace import PrefixFactNamespace

    from ansible.module_utils.facts.system.distribution import Distribution
    from ansible.module_utils.facts.system.pkg_mgr import PkgMgr
    from ansible.module_utils.facts.system.platform import Platform
    from ansible.module_utils.facts.system.service_mgr import ServiceMgr
    from ansible.module_utils.facts.network.distribution import NetworkDistribution


# Generated at 2022-06-13 00:25:26.439733
# Unit test for function ansible_facts
def test_ansible_facts():
    # We need an actual ansible.module_utils.basic.AnsibleModule for this "test"
    from ansible.module_utils.basic import AnsibleModule

    parameters = dict(
        gather_subset=[],  # empty subset
        gather_timeout=1,  # some short timeout
    )
    module = AnsibleModule(argument_spec=parameters)

    facts = ansible_facts(module)  # test function

    assert(facts['os_family'] == 'OpenBSD')  # assert some known fact

# Generated at 2022-06-13 00:25:29.536378
# Unit test for function ansible_facts
def test_ansible_facts():
    pass


# Generated at 2022-06-13 00:25:41.030045
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts import ansible_collector
    import pprint
    import unittest

    class FakeAnsibleModule(object):
        def __init__(self, **kwargs):
            self.params = kwargs

    class FakeAnsibleModuleClass(object):
        def __init__(self, params=None, **kwargs):
            if params is None:
                params = {}
            self.params = params

    class FakeCollectorClass(object):
        def __init__(self, **kwargs):
            self.namespace = kwargs.get('namespace')
            self.filter_spec = kwargs.get('filter_spec')
            self.collect_fn = kwargs.get('collect_fn')

# Generated at 2022-06-13 00:25:48.558139
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts import ansible_facts
    from ansible.module_utils._text import to_native
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.namespace import PrefixFactNamespace

    import json
    from io import StringIO
    from tempfile import NamedTemporaryFile


    class FakeAnsibleModule():
        def __init__(self):
            self.exit_json = self.fail_json = self.run_command = self.get_bin_path = self.params = {}

        def set_command_result(self, cmd, rc, stdout, stderr):
            self.run_command_results[cmd] = (rc, stdout, stderr)


# Generated at 2022-06-13 00:25:58.360692
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils.facts import Facts, get_all_facts
    from ansible.module_utils.basic import AnsibleModule
    m = AnsibleModule(argument_spec=dict(
        gather_subset=dict(type='list', elements='str'),
        gather_timeout=dict(type='int', default=10),
        filter=dict(type='str', default='*'),
    ),
    )
    gather_subset = m.params.get('gather_subset', ['all'])
    f = Facts(m)
    r = get_all_facts(m)

    assert isinstance(r, dict)
    assert len(r) > 10


# Generated at 2022-06-13 00:26:08.633888
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils._text import to_text
    from ansible.module_utils.facts.virtual.bsd import BSDVirtual
    from ansible.module_utils.facts.virtual.openbsd import OpenBSDVirtual
    from ansible.module_utils.facts.virtual.linux import LinuxVirtual
    from ansible.module_utils.facts.virtual.netbsd import NetBSDVirtual
    from ansible.module_utils.facts.virtual.sunos import SunOSVirtual
    from ansible.module_utils.facts.virtual.freebsd import FreeBSDVirtual
    from ansible.module_utils.facts.virtual.xen import XenVirtual
    # Include this to avoid a race condition where a file is written to the tmpdir
    # between the os.rmdir() call in cleanup() and the os.path.exists() calls in


# Generated at 2022-06-13 00:26:19.685151
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts import namespace
    import mock

    # prep
    class testModule(object):
        params = {
            'gather_timeout': 10,
            'filter': '*',
            'gather_subset': ['all'],
        }

    fact_collector_mock_obj = mock.MagicMock(spec=ansible_collector.BaseFactCollector)

    with mock.patch('ansible.module_utils.facts.ansible_collector.get_ansible_collector',
                    return_value=fact_collector_mock_obj):
        # test
        test_module = testModule()
        facts_dict = ansible_facts(test_module)

        # verify
        # make sure the default collector is used with the namespace 'ansible' and no prefix
        ans

# Generated at 2022-06-13 00:26:31.560452
# Unit test for function ansible_facts
def test_ansible_facts():
    import ansible.module_utils.facts.ansible_facts as target
    import ansible.module_utils.facts.collector as collect_f
    import ansible.module_utils.facts.namespace as ns
    import ansible.module_utils.facts.utils as utils
    import ansible.module_utils.facts.system as sys
    import ansible.module_utils.facts.default_collectors as dc
    import ansible.module_utils.facts.ansible_collector as ac
    import ansible.module_utils.facts.hardware as hw
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils.facts import ansible_collector

# Generated at 2022-06-13 00:26:41.911306
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts import ansible_collector

    class FakeAnsibleFactCollector(BaseFactCollector):
        def collect(self, module):
            return {'fake_ansible_fact': 'fake_ansible_fact_value'}

    class FakeNoAnsibleFactCollector(BaseFactCollector):
        def collect(self, module):
            return {'fake_no_ansible_fact': 'fake_no_ansible_fact_value'}

    class FakeModule(object):
        def __init__(self, params=None):
            self.params = params or {}

    old_ansible_collector = ansible_collector.ansible_collector_class
    ansible_collector.ansible

# Generated at 2022-06-13 00:26:48.540727
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.six import PY2
    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils.facts.namespace import PrefixFactNamespace

    # Pretend we are running in Ansible and set up a fake AnsibleModule()
    # See https://docs.python.org/2/library/unittest.mock.html
    # see http://www.voidspace.org.uk/python/mock/mock.html

    # we are calling the unit-tested function in here, so we need to put it in a module
    # call ansible_facts() with a fake module, and check the results look ok
    # also create our own default_collectors, and namespace, so that we test just our function
    # and are not relying on the class-level globals from module

# Generated at 2022-06-13 00:26:56.537938
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils._text import to_bytes

    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils.facts.collector import BaseFactCollector

    class DummyModule(object):
        def __init__(self):
            self.params = dict()

    module = DummyModule()
    module.params.update(gather_subset=['min'])
    module.params.update(gather_timeout=0)

    results = ansible_facts(module)
    assert isinstance(results, dict)

    # make sure we have some results
    assert len(results) > 0

    # make sure some of the results key names don't have a prefix
    assert 'lsb' in results

    # make sure we have a filesystem value

# Generated at 2022-06-13 00:27:07.072350
# Unit test for function ansible_facts
def test_ansible_facts():
    import sys
    import os
    import pytest
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))

    from units.compat.mock import MagicMock, call
    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils.facts import ansible_collector

    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.collector import NamespaceFactCollector
    from ansible.module_utils.facts.collector import FactsCacheFilter

# Generated at 2022-06-13 00:27:10.367370
# Unit test for function ansible_facts
def test_ansible_facts():
    class AnsibleModule(object):
        def __init__(self):
            self.params = dict()
            self.params['gather_subset'] = 'all'

    module = AnsibleModule()
    assert ansible_facts(module)



# Generated at 2022-06-13 00:27:21.991075
# Unit test for function get_all_facts
def test_get_all_facts():
    '''Unit test for get_all_facts

    Patch to return a specific dict of facts, and ensure the returned dict is what we patched in.
    '''

    try:
        from unittest.mock import patch
    except ImportError:
        from mock import patch

    expected_fact_dict = dict(foo='bar', baz='qux')

    # patch the ansible_facts function to return our expected dict of facts
    with patch('ansible.module_utils.facts.ansible_facts', return_value=expected_fact_dict):
        from ansible.module_utils.facts import get_all_facts
        from ansible.module_utils._text import to_bytes

        class AnsibleModule:
            def __init__(self):
                pass


# Generated at 2022-06-13 00:27:30.474811
# Unit test for function get_all_facts
def test_get_all_facts():
    import ansible.module_utils.facts.namespace as ns
    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts import ansible_collector
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.basic import AnsibleModule

    class FakeAnsibleModule:
        def __init__(self):
            self.params = {'gather_subset': ['all']}

    fake_module = FakeAnsibleModule()

    fake_facts = get_all_facts(fake_module)

    assert 'default_ipv4' in fake_facts.keys()

# Generated at 2022-06-13 00:27:42.654813
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts._text import StringIO
    import sys
    import types
    import unittest

    class MockAnsibleModule(object):

        def __init__(self):
            self.params = {'gather_subset': ['all']}

    class TestFactsModule(unittest.TestCase):

        def setUp(self):
            self.input_stdout = sys.stdout
            self.input_stderr = sys.stderr
            sys.stdout = StringIO()
            sys.stderr = StringIO()
            self.module = MockAnsibleModule()

        def tearDown(self):
            sys.stdout.close()
            sys.stdout = self.input_stdout
            sys.stderr.close()

# Generated at 2022-06-13 00:27:48.128695
# Unit test for function get_all_facts
def test_get_all_facts():
    class AnsibleModule(object):
        def __init__(self):
            self.params = {}
            self.params['gather_subset'] = 'network'

    module = AnsibleModule()
    facts = get_all_facts(module)

    assert isinstance(facts, dict)
    assert len(facts) > 0



# Generated at 2022-06-13 00:27:56.470604
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.compat.tests.mock import patch, MagicMock
    from ansible.module_utils.facts.ansible_collector import AnsibleCollector

    with patch('ansible.module_utils.facts.ansible_collector.AnsibleCollector.collect') as magicmock:
        with patch.object(AnsibleCollector, '_get_fact_class_instances'):
            with patch.object(AnsibleCollector, '_get_collector_classes'):
                with patch.object(AnsibleCollector, '_filter_collectors'):
                    test_inst = AnsibleCollector()
                    test_inst.collect(None)
                    assert magicmock.called


# Generated at 2022-06-13 00:28:04.109447
# Unit test for function get_all_facts
def test_get_all_facts():

    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.namespace import BaseFactNamespace

    class TestNamespace1(BaseFactNamespace):
        name = 'test_ns1'
        @classmethod
        def populate(cls, collector):
            collector.add_fact(cls.name, 'foo')

    class TestNamespace2(BaseFactNamespace):
        name = 'test_ns2'
        @classmethod
        def populate(cls, collector):
            collector.add_fact(cls.name, 'bar')

    class TestCollector(BaseFactCollector):
        _fact_classes = [TestNamespace1, TestNamespace2]

    class FakeModule(object):
        params = {'gather_subset': ['all']}

# Generated at 2022-06-13 00:28:14.924554
# Unit test for function ansible_facts
def test_ansible_facts():
    import sys
    sys.modules['ansible'] = None

    try:
        import ansible
    except AttributeError:
        has_ansible = False
    else:
        has_ansible = True

    # import ansible.module_utils.facts
    try:
        import ansible.module_utils.facts
    except ImportError:
        assert not has_ansible
        return

    try:
        from ansible.module_utils.facts import default_collectors
    except ImportError:
        assert not has_ansible
        return

    class FakeModule:
        class FakeAnsibleModule:
            def get_bin_path(self, binary, required=True):
                return '/usr/bin/' + binary

            def run_command(self, cmd, check_rc=True):
                return '', '', 0

# Generated at 2022-06-13 00:28:25.196666
# Unit test for function get_all_facts
def test_get_all_facts():
    import unittest
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.facts import ansible_facts as af
    from ansible.module_utils.facts import get_all_facts as gaf

    class TestGetAllFacts(unittest.TestCase):
        def test_get_all_facts_compat_with_ansible_facts(self):
            module = AnsibleModule({'gather_subset': ['all']})
            all_facts = gaf(module)
            self.assertEqual(all_facts, af(module, ['all']))

    unit_test = unittest.TestLoader().loadTestsFromTestCase(TestGetAllFacts)
    unittest.TextTestRunner(verbosity=2).run(unit_test)

# Unit test

# Generated at 2022-06-13 00:28:41.847446
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils.facts.collector.system import SystemCollector
    from ansible.module_utils.facts.collector.default import DefaultCollector
    from ansible.module_utils.facts.collector import get_collector_names, get_collector_classes
    from ansible.module_utils.basic import AnsibleModule

    # Mock module
    module = AnsibleModule(argument_spec={
        'gather_subset': dict(default=None, type='list'),
        'gather_timeout': dict(default=10, type='int'),
        'filter': dict(default='*', type='str')})

    # Mock facts

# Generated at 2022-06-13 00:28:53.603394
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts.utils import get_fact_cache
    from ansible.module_utils.facts import ansible_facts
    from ansible.module_utils.facts.system.distribution import DistributionFactCollector
    from ansible.module_utils.facts.system import distro

    # Monkey patch the distro module to pretend to be a Linux system.  This is
    # so we can test the facts without requiring any special system
    # dependencies.  We don't actually use any Linux-specific facts, but we
    # need this to tell the facts module not to attempt to run system-specific
    # tests (which may or may not be successful).
    distro.distro_cache = {}
    distro.linux_distribution = lambda: ('Linux', '', '')

    module_mock = Mock()
    module_m

# Generated at 2022-06-13 00:29:03.326792
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts.network.base import NetworkCollector
    from ansible.module_utils.facts.network.default import DefaultNetworkCollector
    from ansible.module_utils.facts.network.linux import LinuxNetworkCollector

    from ansible.module_utils.facts.system.base import SystemCollector
    from ansible.module_utils.facts.system.default import DefaultSystemCollector

    from ansible.module_utils.facts.virtual.base import VirtualCollector
    from ansible.module_utils.facts.virtual.default import DefaultVirtualCollector

    class MockAnsibleModule(object):
        def __init__(self, facts_dict):
            self.facts_dict = facts_dict

        def exit_json(self, **kwargs):
            self.exit_json_kwargs = kwargs



# Generated at 2022-06-13 00:29:08.910998
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils.basic import AnsibleModule
    test_module = AnsibleModule(argument_spec=dict(
        gather_subset=dict(default=['!all'], type='list'),
        filter=dict(default='*'),
    ))
    assert not get_all_facts(test_module)
    assert ansible_facts(test_module)
    test_module.params['gather_subset'] = ['all']
    assert get_all_facts(test_module)
    assert ansible_facts(test_module)

# Generated at 2022-06-13 00:29:14.334376
# Unit test for function ansible_facts
def test_ansible_facts():
    # We need to trick the code above into thinking it is being run by ansible,
    # so we mock out an ansible.module_utils.basic.AnsibleModule object, and pass it to the
    # function

    try:
        from ansible.module_utils.basic import AnsibleModule
    except ImportError:
        import sys
        print("Ansible 2.3 is not installed. \
               To run unit tests, install Ansible 2.3", file=sys.stderr)
        sys.exit(1)


# Generated at 2022-06-13 00:29:20.865997
# Unit test for function ansible_facts
def test_ansible_facts():
    '''
    This is a test function for facts.ansible_facts function
    '''
    import os
    import sys

    import pytest

    # import module snippets
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../plumbing'))

    from ansible.module_utils.basic import AnsibleModule

    from ansible.module_utils.facts.collector import FactsCollector

    from ansible.module_utils.facts import ansible_collector
    from ansible.module_utils.facts.namespace import PrefixFactNamespace

    # Define the module
    module = AnsibleModule(argument_spec={},
                           supports_check_mode=False)

    # NOTE: Passing None to gather_subset because gather_subset is an optional arg.


# Generated at 2022-06-13 00:29:28.787173
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts import ansible_facts
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.basic import AnsibleModule

    def assert_facts(module, expected, gather_subsets=['all'], gather_timeout=10, filter_spec="*"):
        module = AnsibleModule(
            argument_spec=dict(
                gather_subset=dict(type='list', default=gather_subsets),
                gather_timeout=dict(type='int', default=gather_timeout),
                filter=dict(type='str', default=filter_spec)
            )
        )
        facts = ansible_facts(module, gather_subset=['all'])
        assert facts == expected


# Generated at 2022-06-13 00:29:40.369433
# Unit test for function ansible_facts
def test_ansible_facts():
    # Don't use the ansible 2.3 AnsibleModule mock, because it doesn't support gather_subset
    # use a mock that is exactly the same as the one from 2.2
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule()

    from ansible.module_utils.facts import assemble_facts
    from ansible.module_utils.facts import default_collectors

    # don't need to define module.params, since get_all_facts only uses them by name
    # and the param names are defined in the module_utils.facts code

    # Make the ansible_facts function think it was called by the module_utils.get_all_facts function
    # This is important so that the ansible_facts function will NOT check the gather_subset parameter,
    # and will instead use the configured gather_sub

# Generated at 2022-06-13 00:29:50.226346
# Unit test for function ansible_facts
def test_ansible_facts():
    import unittest
    from ansible.module_utils import facts

    class GetAnsibleFactsTester(unittest.TestCase):
        def setUp(self):
            self.module = AnsibleModule(argument_spec={}, supports_check_mode=True)

        def test_get_ansible_facts(self):
            facts_dict = facts.ansible_facts(self.module)

            self.assertTrue('distribution' in facts_dict)
            self.assertTrue('distribution_version' in facts_dict)
            self.assertTrue('distribution_major_version' in facts_dict)
            self.assertTrue('os_family' in facts_dict)
            self.assertTrue('selinux' in facts_dict)


# Generated at 2022-06-13 00:30:00.045476
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.basic import AnsibleModule, missing_required_lib
    from ansible.module_utils.facts import default_collectors, ansible_collector

    # needs to be a subclass of ansible.module_utils.basic.AnsibleModule
    class TestModule(AnsibleModule):
        pass

    module = TestModule()

    gather_subset = ['all']
    gather_timeout = 10
    filter_spec = '*'

    # Test that ansible_facts(module, gather_subset) returns a non-empty dict
    gathered_facts = ansible_facts(module, gather_subset=gather_subset)
    assert isinstance(gathered_facts, dict)
    assert len(gathered_facts) > 0

# Generated at 2022-06-13 00:30:16.589256
# Unit test for function ansible_facts
def test_ansible_facts():
    pass


# Generated at 2022-06-13 00:30:22.760164
# Unit test for function ansible_facts
def test_ansible_facts():
    def dummy_module(params):
        '''returns a dummy module'''
        return mock.Mock()

    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils.facts import ansible_collector
    import mock


# Generated at 2022-06-13 00:30:33.866892
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts import default_collectors

    # this is the mock module we are collecting facts from
    class AnsibleModuleFake:
        def __init__(self, params):
            self.params = params

    params = {'gather_subset': ['all'],
              'filter': '*',
              'gather_timeout': 10,
              }
    fake_module = AnsibleModuleFake(params=params)

    # setup
    # find a collector that returns a known fact
    all_collector_classes = default_collectors.collectors
    for collector_class in all_collector_classes:
        if collector_class.depends_on in ['python']:
            break

    # don't add a prefix

# Generated at 2022-06-13 00:30:43.125383
# Unit test for function ansible_facts
def test_ansible_facts():
    '''Test the ansible_facts() function.'''

    import ansible.module_utils.facts.network.base
    from ansible.module_utils.facts.network.base import NetworkCollector

    from ansible.module_utils.facts.network.linux import LinuxNetwork

    from ansible.module_utils.facts.system.base import SysinfoCollector

    from ansible.module_utils.facts.system.distribution import DistributionCollector

    from ansible.module_utils.facts.system.linux.distribution import LinuxDistribution

    # No module object, just verify the correct result
    # register a fake NetworkCollector with a fake collect method
    fake_collect_method = lambda x: {'network_facts': 'fake_network_facts'}
    ansible.module_utils.facts.network.base.NetworkCollector = type

# Generated at 2022-06-13 00:30:53.877738
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.facts import default_collectors

    # Create a fake instance of AnsibleModule
    class FakeAnsibleModule(object):
        def __init__(self, collect_facts, gather_timeout):
            self.params = {
                'gather_facts': collect_facts,
                'gather_timeout': gather_timeout,
                'filter': '*'
            }

    # Create a fake AnsibleModule that collects facts
    fake_module = FakeAnsibleModule(True, 10)

    # call ansible_facts function
    results = ansible_facts(fake_module)

    # Make sure results is a dict
    assert isinstance(results, dict)

    # If AnsibleModule.params['gather_facts'] was true,


# Generated at 2022-06-13 00:31:06.197930
# Unit test for function ansible_facts
def test_ansible_facts():
    import ansible.module_utils.facts.collector
    import ansible.module_utils.facts

    all_collector_classes = ansible.module_utils.facts.collector.collectors
    fact_collector = ansible.module_utils.facts.ansible_collector.get_ansible_collector(all_collector_classes=all_collector_classes,
                                                                                        namespace=None,
                                                                                        filter_spec='default_ipv4',
                                                                                        gather_subset=None,
                                                                                        gather_timeout=10,
                                                                                        minimal_gather_subset=frozenset(['default_ipv4']))
    collected_facts = fact_collector.collect()
    assert collected_facts['default_ipv4']['address']

# Generated at 2022-06-13 00:31:14.534382
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils.facts import ansible_collector
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils import facts

    # mock AnsibleModule instance
    module = AnsibleModule(
        argument_spec={},
    )

    gather_subset = ['!all', 'network']
    gather_timeout = 10
    filter_spec = '*'


# Generated at 2022-06-13 00:31:24.783996
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.facts.system.distribution import DistributionFactCollector
    from ansible.module_utils.facts.system.pkg_mgr import PkgMgrFactCollector
    from ansible.module_utils.facts.system.distribution import DistributionFactCollector
    from ansible.module_utils.facts.system.apparmor import ApparmorFactCollector
    from ansible.module_utils.facts.system.platform import PlatformFactCollector
    from ansible.module_utils.facts.system.dns import DnsFactCollector
    from ansible.module_utils.facts.system.service_mgr import ServiceMgrFactCollector
    from ansible.module_utils.facts.system.python import PythonFactCollector
    from ansible.module_utils.facts.system.env import EnvFactCollector
   

# Generated at 2022-06-13 00:31:33.283841
# Unit test for function ansible_facts
def test_ansible_facts():

    import os
    import sys
    TEST_DIR = os.path.dirname(__file__)
    TEST_DIR = TEST_DIR[:-len('/lib/ansible/module_utils/facts/facts')]
    sys.path.insert(0, TEST_DIR)

    from ansible.module_utils.basic import AnsibleModule

    fake_module = AnsibleModule(
        argument_spec=dict(
            gather_subset=dict(type='list', default=['all']),
            gather_timeout=dict(type='int', default=10),
        )
    )
    fake_module.params = {'gather_subset': ['all'],
                          'gather_timeout': 10}
    ansible_facts = ansible_facts(fake_module)

    assert ansible_facts['lsb']


# Generated at 2022-06-13 00:31:44.304305
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.facts.utils import get_collector_members

    m = AnsibleModule(argument_spec={'gather_subset': {'type': 'list', 'default': ['all']}})

    fact_dict = get_all_facts(m)

    known_facts = {'default_ipv4', 'fqdn', 'kernel', 'lsb', 'kernel_version', 'os_family', 'system', 'distribution',
                   'hostname', 'python', 'python_version', 'architecture'}
    assert set(fact_dict.keys()) == known_facts

    # TODO: assert the values are what we'd expect.

    # test that all the members of the collector class were called during a collection.
    fact_collector

# Generated at 2022-06-13 00:32:25.592435
# Unit test for function ansible_facts
def test_ansible_facts():
    '''
    Unit test for ansible_facts function
    '''
    import sys
    import os
    import interop_common
    my_dir = os.path.dirname(__file__)
    (m_path, m_file) = os.path.split(__file__)
    sys.path.append(os.path.join(my_dir, '../../'))
    from ansible.module_utils.facts import ansible_facts
    from ansible.module_utils.basic import AnsibleModule

    # create a dummy module
    module = AnsibleModule(argument_spec={})

    # set up the expected result

# Generated at 2022-06-13 00:32:32.699957
# Unit test for function ansible_facts
def test_ansible_facts():
    import pytest
    from ansible.module_utils._text import to_bytes
    module = pytest.Mock()
    module.params = {
        'filter': '*',
        'gather_subset': ['all']
    }
    fact_namespace = ansible_facts(module=module, gather_subset=['all']).keys()
    for fact in ('default_ipv4', 'default_ipv6', 'hostname', 'hostvars'):
        assert fact in fact_namespace

# Generated at 2022-06-13 00:32:41.651895
# Unit test for function get_all_facts
def test_get_all_facts():
    from ansible.module_utils.facts import module_parsers
    from ansible.module_utils.facts.network.generic import Interface

    class TestModule(object):
        def __init__(self, params):
            self._params = params

        def params(self):
            return self._params

    # Test with a single Interface
    params = dict(gather_subset=['network'])
    nm = TestModule(params)
    module_parsers.populate_facts(nm, dict(interfaces=['eth0']))
    res = get_all_facts(nm)

    assert 'default_ipv4' in res
    assert 'default_ipv6' in res
    assert 'interfaces' in res

    ifs = res['interfaces']
    assert len(ifs) == 1

# Generated at 2022-06-13 00:32:45.330483
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(argument_spec={'gather_subset': dict(type='list', default=['all'])})
    facts = ansible_facts(module)
    assert isinstance(facts, dict)
    assert isinstance(facts.get('default_ipv4'), dict)

# Generated at 2022-06-13 00:32:54.273538
# Unit test for function ansible_facts
def test_ansible_facts():
    import mock

    mock_module = mock.MagicMock()
    mock_module.params = dict(gather_subset=['min'])
    mock_module.get_bin_path = mock.Mock(return_value='/usr/bin/pwd')

    facts_dict = ansible_facts(module=mock_module)

    expected_keys = ['cmdline', 'env', 'platform']

    assert set(facts_dict.keys()).issuperset(expected_keys)

    for key in expected_keys:
        assert facts_dict[key] is not None



# Generated at 2022-06-13 00:33:03.288230
# Unit test for function ansible_facts
def test_ansible_facts():
    # module_utils.facts.ansible_facts() is not part of devel branch,
    # so write a unit test here in case it shows up in a future branch
    import pytest
    from ansible.module_utils._text import to_text

    class AnsibleModuleFake:
        def __init__(self):
            from ansible.module_utils.common._collections_compat import Mapping
            self.params = Mapping()
            self.params['filter'] = '*'

    module = AnsibleModuleFake()

    with pytest.warns(None) as warnings:
        facts_dict = ansible_facts(module)
        assert not warnings
        assert facts_dict['system']

# Generated at 2022-06-13 00:33:13.363415
# Unit test for function ansible_facts
def test_ansible_facts():
    import pytest
    from ansible.module_utils.facts.utils import get_all_collector_classes

    class FakeModule:
        def __init__(self, params):
            self.params = params

    all_collector_classes = get_all_collector_classes()

    fake_module = FakeModule({'gather_subset': ['all'], 'filter': '*'})

    fact_dict = ansible_facts(fake_module, ['all'])
    assert fact_dict
    for collector_class in all_collector_classes:
        # assert the collector collected facts
        fact_name = collector_class.NAMESPACE
        if hasattr(collector_class, 'FACT_NAME'):
            fact_name = fact_name + '_' + collector_class.FACT_NAME

# Generated at 2022-06-13 00:33:25.745052
# Unit test for function ansible_facts
def test_ansible_facts():
    import ansible
    from ansible.module_utils.facts import ansible_facts
    from ansible.module_utils.common.collections import ImmutableDict

    class FakeAnsibleModuleMeta(type):
        '''Metaclass for module_utils.basic.AnsibleModule, to be used in tests.
        Replaces the module_args and params attributes with a deepcopy of the
        test_module_args. This is necessary to avoid modifying the test input
        data, which is i.e. used in other tests.

        The original module_args and params attribute values are None.
        There is no need to reset them, since the fake instance is ephemeral
        and is not reused.
        '''


# Generated at 2022-06-13 00:33:33.509865
# Unit test for function ansible_facts
def test_ansible_facts():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils import facts

    module = AnsibleModule(argument_spec={'filter': {}, 'gather_subset': {'required': False}})
    gather_subset = module.params['gather_subset']


# Generated at 2022-06-13 00:33:43.567534
# Unit test for function get_all_facts
def test_get_all_facts():
    '''
    Test the get_all_facts function
    '''
    # Import required packages
    import sys
    import unittest

    class AnsibleParams():
        '''
        Fake AnsibleModule class with params class
        '''
        class ModuleFailException(Exception):
            '''
            Fake AnsibleModule exception class
            '''
            pass

        class AnsibleFailJsonException(Exception):
            '''
            Fake AnsibleModule exception class
            '''
            pass

        def __init__(self, params):
            '''
            Constructor
            '''
            self.params = params

        def fail_json(self, *args, **kwargs):
            '''
            Fake AnsibleModule fail_json method
            '''