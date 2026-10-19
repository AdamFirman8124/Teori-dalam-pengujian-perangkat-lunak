

# Generated at 2022-06-13 02:19:42.804289
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():

    # run method collect of class SystemCapabilitiesFactCollector
    pass

# Generated at 2022-06-13 02:19:54.244621
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import mock
    import tempfile
    from ansible.module_utils.facts import collector

    # Stub out the module_util methods that interact with the system
    with mock.patch("ansible.module_utils.facts.collector.get_file_content"):
        get_file_content_obj = collector.get_file_content
        get_file_content_obj.return_value = "Current: =ep cap_sys_admin+p"
        # Run the method to be tested
        test_obj = SystemCapabilitiesFactCollector()
        result_obj = test_obj.collect()
        # Assert that the result is a dictionary (results of collect())
        assert isinstance(result_obj, dict)
        # Assert that False is returned for system_capabilities_enforced

# Generated at 2022-06-13 02:20:04.672548
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import json
    import os
    import sys
    import unittest
    import tempfile

    import ansible.module_utils.facts.collector
    import ansible.module_utils.facts.collector.system
    from ansible.module_utils.facts import collector

    class Module():
        def __init__(self):
            self.run_command = lambda x, checks=False, warnings=False: (0, x[1], '')
            self.get_bin_path = lambda x, fail_on_missing=True, opt_dirs=[] : 'true'

    class MockSubprocess():

        PIPE = -1

        call_log = []

        # NOTE(akl): simulate subprocess.Popen()
        def __init__(self, args, stdin, stdout, stderr):
            self

# Generated at 2022-06-13 02:20:12.377429
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import json
    import os
    import platform
    import shutil
    import tempfile
    import unittest

    from ansible.module_utils.facts.collector.system.capabilities import SystemCapabilitiesFactCollector

    class TestSystemCapabilitiesFactCollector(unittest.TestCase):
        def setUp(self):
            self.capsh_path = '/usr/bin/capsh'
            if platform.system() == 'FreeBSD':
                self.capsh_path = '/usr/sbin/capsh'
            if not os.path.exists(self.capsh_path):
                self.skipTest('%s does not exist' % self.capsh_path)

            # NOTE: py26 doesn't support unittest.skipIf() -akl

# Generated at 2022-06-13 02:20:20.458244
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    module = None
    # Abnormal execution when capsh returns error
    def capsh_side_effect(*args, **kwargs):
        return (1, '', 'Command line error')
    module_mock = MagicMock()
    module_mock.get_bin_path.return_value = 'capsh'
    module_mock.run_command.return_value = capsh_side_effect()
    result = SystemCapabilitiesFactCollector.collect(module_mock)
    assert result == {}

    # Expected execution

# Generated at 2022-06-13 02:20:31.128072
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    module = Mock()
    module.get_bin_path.return_value = 'capsh'
    module.run_command.return_value = 0, 'Current: =ep', ''
    collected_facts = {}

    f = SystemCapabilitiesFactCollector()
    f.collect(module=module, collected_facts=collected_facts)

    assert module.get_bin_path.called
    assert module.run_command.called

    assert collected_facts['system_capabilities_enforced'] == 'False'
    assert collected_facts['system_capabilities'] == []

    module.run_command.return_value = 0, 'Current: =ep cap_net_admin,cap_ipc_lock,cap_net_bind_service', ''
    collected_facts = {}

    f = SystemCapabilitiesFactCollector()

# Generated at 2022-06-13 02:20:38.894361
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    caps = SystemCapabilitiesFactCollector()
    # these are the facts this module should collect
    facts_to_collect = ['system_capabilities',
                        'system_capabilities_enforced']

    # collect each of these facts
    collected_facts = {}
    for fact in facts_to_collect:
        collected_facts[fact] = caps.collect(collected_facts)

    # test _fact_ids
    assert caps._fact_ids == {'system_capabilities',
                              'system_capabilities_enforced'}

    # test the facts have been collected
    for fact in facts_to_collect:
        assert fact in collected_facts
        assert collected_facts[fact]
        # test that every collected fact is something
        assert collected_facts[fact] != ''

# Generated at 2022-06-13 02:20:48.794789
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import module_utils.facts
    import os
    import tempfile
    module = module_utils.facts.AnsibleModuleMock()
    fd, capsh_path = tempfile.mkstemp()
    os.write(fd, b'''#! /bin/bash
    echo 'Current: =ep Bounding set =cap_net_raw,cap_sys_admin'
    ''')
    os.close(fd)
    os.chmod(capsh_path, 0o755)
    module.get_bin_path = lambda *args: capsh_path
    fact_collector = SystemCapabilitiesFactCollector()

    # TODO: use mock to set module.run_command() return value -akl
    facts = fact_collector.collect(module)
    assert facts['system_capabilities_enforced']

# Generated at 2022-06-13 02:20:59.087195
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import os
    import ansible.module_utils.facts.system.caps as caps_module
    if not os.path.exists('/usr/bin/capsh'):
        return

    module_fact_collector = SystemCapabilitiesFactCollector()
    root_fact_collector = caps_module.RootFactCollector()
    os_name_fact_collector = caps_module.OSNameFactCollector()

    root_facts_dict = root_fact_collector.collect()
    os_name_facts_dict = os_name_fact_collector.collect()

    facts_dict = module_fact_collector.collect(root_facts_dict, os_name_facts_dict)
    assert 'system_capabilities' in facts_dict
    assert 'system_capabilities_enforced' in facts_dict

# Generated at 2022-06-13 02:21:09.637442
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import sys
    import shutil
    #import unittest.mock as mock
    import unittest

    # Since we are testing against a system fact, we should skip this
    # test on Windows platforms.
    if 'win' in sys.platform:
        raise unittest.SkipTest('Not supported on Windows')

    # Arrange
    from ansible.module_utils.facts import ansible_collector
    from ansible.module_utils.facts.collector.system import SystemCapabilitiesFactCollector
    from ansible.module_utils.facts.system.capabilities import get_caps_data
    from ansible.module_utils.facts.system.capabilities import parse_caps_data
    from ansible.module_utils.facts.system.capabilities import CapshExecutableNotFound

# Generated at 2022-06-13 02:21:13.327622
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # NOTE: test should be updated to use module_utils.facts.collector
    pass

# Generated at 2022-06-13 02:21:20.529057
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    capsh_path = 'capsh'
    capsh_rc = 0

# Generated at 2022-06-13 02:21:31.753140
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts.collector import FakeModule

    fact_collector = SystemCapabilitiesFactCollector()
    capsh_path = '/usr/bin/capsh'

# Generated at 2022-06-13 02:21:39.941266
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    """Unit test for method collect of class SystemCapabilitiesFactCollector"""
    import mock
    import sys

    # If Python2, mock unicode string and bytes
    if sys.version_info[0] >= 3:
        from io import StringIO
        unicode_mock = u'unicode'
        bytes_mock = b'bytes'
    else:
        from StringIO import StringIO
        unicode_mock = b'unicode'
        bytes_mock = u'bytes'

    # Create mock module
    module = mock.Mock()
    module.get_bin_path.return_value = '/bin/capsh'

    # Create mock output
    rc = 0

# Generated at 2022-06-13 02:21:49.417789
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    system_capabilities_path = '/bin/capsh'
    system_capabilities_cmd = [system_capabilities_path, "--print"]

# Generated at 2022-06-13 02:21:53.583505
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    module = type('', (), {'run_command': lambda *args, **kwargs: (0, 'Current: =ep', '')})
    capsh = SystemCapabilitiesFactCollector(module=module)
    collected_facts = capsh.collect()
    assert collected_facts['system_capabilities_enforced'] == 'False'
    assert collected_facts['system_capabilities'] == []


# Generated at 2022-06-13 02:22:01.246840
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # create a fake module
    class FakeModule:
        def __init__(self, capsh_path):
            self.capsh_path = capsh_path
            return

        def get_bin_path(self, arg):
            return self.capsh_path

        def run_command(self, arg, errors):
            return 0, "Current: = cap_syslog+p"
    module = FakeModule(capsh_path='/bin/capsh')

    import facts.collectors.capsh
    reload(facts.collectors.capsh)
    from facts.collectors.capsh import SystemCapabilitiesFactCollector

    collector = SystemCapabilitiesFactCollector()
    result = collector.collect(module)
    assert result['system_capabilities_enforced'] == 'False'

# Generated at 2022-06-13 02:22:07.174604
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    fact_collector = SystemCapabilitiesFactCollector()
    collected_facts = {}
    system_capabilities_enforced_result = 'NA'
    system_capabilities_result = []

    # test with failure result
    result = fact_collector.collect(None, collected_facts)
    assert system_capabilities_enforced_result == result['system_capabilities_enforced']
    assert system_capabilities_result == result['system_capabilities']

    # test with normal result

# Generated at 2022-06-13 02:22:17.267944
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    module = AnsibleModule(argument_spec={})
    fixture_path = os.path.join(os.path.dirname(__file__), '..', 'fixtures', 'capabilities.txt')
    with open(fixture_path) as f:
        capsh_output = f.read()
    # set up mock module
    module.run_command = Mock(return_value=(0, capsh_output, ''))
    module.get_bin_path = Mock(return_value='/bin/capsh')
    # run method
    results = SystemCapabilitiesFactCollector.collect(module)
    assert results['system_capabilities_enforced'] == 'True'
    assert 'chown' in results['system_capabilities']
    assert 'kill' in results['system_capabilities']
    assert 'fowner' in results

# Generated at 2022-06-13 02:22:23.426799
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # setup test
    _my_module = MockAnsibleModule()
    _my_module.run_command = MockRunCommand()
    _my_module.run_command.return_value = (0, "Current: = ", "")
    _my_SystemCapabilitiesFactCollector = SystemCapabilitiesFactCollector()
    _result = _my_SystemCapabilitiesFactCollector.collect(_my_module, None)
    # make assertion
    assert _result['system_capabilities_enforced'] == 'False'
    assert _result['system_capabilities'] == []

# MockAnsibleModule -- Utility class to mock AnsibleModule used by SystemCapabilitiesFactCollector._collect_facts

# Generated at 2022-06-13 02:22:35.852738
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    class DummyModule:
        def __init__(self):
            self.run_command_results = []
            
        def run_command(self, command, errors='surrogate_then_replace'):
            rslt = self.run_command_results[0]
            del self.run_command_results[0]
            return rslt

        def get_bin_path(self, cmd):
            return 'capsh'

    def run_command(cmd, errors='surrogate_then_replace'):
        return rc, out, err

    # # NOTE: [0] = capsh --print: '=ep' (not enforced)
    # rc, out, err = 0, "Current: =ep\nBounding set =cap_chown,cap_dac_override,cap_fowner,\
    # cap

# Generated at 2022-06-13 02:22:39.673455
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    '''
    Test ansible.module_utils.facts.system.capabilities.collect
    '''
    SystemCapabilitiesFactCollector_obj = SystemCapabilitiesFactCollector('foo')
    SystemCapabilitiesFactCollector_obj.collect({'foo':'bar', 'run_command':run_command_mocked})

# Unit test cases

# Generated at 2022-06-13 02:22:48.731361
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts.utils import get_file_content
    capsh_data = get_file_content('./test_files/capsh.txt')
    capsh_data = capsh_data.strip('\n')
    module = None
    collected_facts = {}
    sys_caps_facts_collector = SystemCapabilitiesFactCollector()
    result = sys_caps_facts_collector.collect(module, collected_facts, capsh_data)
    assert result['system_capabilities'] == ['cap_net_raw', 'cap_audit_read', 'cap_dac_override']
    assert result['system_capabilities_enforced'] == 'True'


# Generated at 2022-06-13 02:22:57.564198
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # Check with capsh
    fc = SystemCapabilitiesFactCollector()
    fc.get_bin_path = lambda *args: "/bin/capsh"

# Generated at 2022-06-13 02:22:58.352550
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    pass

# Generated at 2022-06-13 02:23:07.896982
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import ansible.module_utils.facts.collector
    import ansible.module_utils.facts.system.caps

    # Create a dummy module to use as 'mock_module' in this test
    class Options:
        def __init__(self, values=None):
            self.values = values or {}

        def __getattr__(self, key):
            return self.values[key]

        def __setattr__(self, key, value):
            self.values[key] = value

    class ReturnValue:
        def __init__(self, rc=None, stdout=None, stderr=None):
            self.rc = rc
            self.stdout = stdout
            self.stderr = stderr

    class ModuleExecutor:
        def __init__(self, module):
            self.module

# Generated at 2022-06-13 02:23:14.687835
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    module_mock = Mock()
    collected_facts = {}

    module_mock.get_bin_path.return_value = '/bin/capsh'

# Generated at 2022-06-13 02:23:15.728504
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    SystemCapabilitiesFactCollector().collect

# Generated at 2022-06-13 02:23:16.057408
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    pass

# Generated at 2022-06-13 02:23:26.427049
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():

    # create an instance of the SystemCapabilitiesFactCollector class with
    # a minimum set of args
    system_capabilities_fact_collector = SystemCapabilitiesFactCollector(
        module=None,
        collected_facts=None)

    # simulate module.get_bin_path() returning capsh_path = 'usr/bin/capsh'
    # and module.run_command() returning capsh_path = 'usr/bin/capsh'
    capsh_path = 'usr/bin/capsh'
    module = {'get_bin_path' : lambda *args, **kwargs: capsh_path}
    module.update({'run_command' : lambda *args, **kwargs: (0, 'Current: =ep', '')})

    # Use the module above to simulate a call to collect() and assert the
    #

# Generated at 2022-06-13 02:23:44.226835
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    module_mock = AnsibleModuleMock(return_values=[0, 'Current: =eip', ''])
    assert SystemCapabilitiesFactCollector(module_mock).collect() == {
        'system_capabilities': ['eip'],
        'system_capabilities_enforced': 'True',
    }

    module_mock = AnsibleModuleMock(return_values=[0, 'Current: =ep', ''])
    assert SystemCapabilitiesFactCollector(module_mock).collect() == {
        'system_capabilities_enforced': 'False',
        'system_capabilities': [],
    }


# Generated at 2022-06-13 02:23:51.549961
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import os
    import sys
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.collector.system.capabilities import SystemCapabilitiesFactCollector

    import pytest

    for ver in ['2.6', '2.7', '3.3', '3.4', '3.5', '3.6', '3.7']:
        if to_bytes(ver) not in sys.version:
            continue

        class MockModule(object):

            def __init__(self, *args, **kwargs):
                self._ansible_module = basic.AnsibleModule(*args, **kwargs)


# Generated at 2022-06-13 02:23:57.025277
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    """
    Test that SystemCapabilitiesFactCollector can collect capabilities
    """
    try:
        import sys
        sys.path.insert(0, 'src/ansible_collections/ansible/system/plugins/modules/')  # noqa: E402
        from ansible.modules.system import capsh
    except ImportError:
        pass

    test_obj = SystemCapabilitiesFactCollector()
    test_obj.collect()

# Generated at 2022-06-13 02:24:04.249308
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    class MockModule(object):
        def __init__(self, stdout_data, returncode_data):
            self.rc = returncode_data
            self.stdout = stdout_data
            self.stderr = ''
            self.run_command_called = False

        def run_command(self, args, errors='surrogate_then_replace'):
            self.run_command_called = True
            return (self.rc, self.stdout, self.stderr)

        def get_bin_path(self, executable, required=True):
            return '/bin/capsh'

    class MockFacts(object):
        def __init__(self):
            self.facts = {}

        def __getitem__(self, key):
            return self.facts[key]


# Generated at 2022-06-13 02:24:12.611134
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    try:
        import __builtin__ as builtins
    except ImportError:
        import builtins
    import ansible.module_utils.facts.collector
    from ansible.module_utils.facts.collector import SystemCapabilitiesFactCollector

    run_command_mock = None
    capsh_path_mock = '/usr/bin/capsh'

# Generated at 2022-06-13 02:24:17.230424
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts.collector import Cache
    from ansible.module_utils.facts.system.caps import SystemCapabilitiesFactCollector
    from ansible.module_utils.facts.utils import get_file_lines
    import os

    def mock_module(tmpdir):
        from ansible.module_utils.facts import ModuleFacts
        return ModuleFacts(module_name='ansible.modules.system.setup', module_args='', basedir=tmpdir.strpath, tmpdir=tmpdir.strpath)


# Generated at 2022-06-13 02:24:25.334671
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import json
    import os
    import tempfile
    from ansible.module_utils.facts.collector import BaseFactCollector

    os.environ['HOME'] = tempfile.mkdtemp()


# Generated at 2022-06-13 02:24:33.931841
# Unit test for method collect of class SystemCapabilitiesFactCollector

# Generated at 2022-06-13 02:24:39.966846
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts.collector import AnsibleModuleFake
    from ansible.module_utils.facts.collector import DictAsAttribute
    from ansible.module_utils.facts import ansible_facts
    from ansible.module_utils.facts.collector import FactsCollector

    # Initialize mock module and facts_dicts
    module = AnsibleModuleFake()
    module.params = {}
    facts_dicts = {}

# Generated at 2022-06-13 02:24:49.823757
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts import FactCollector
    from ansible.module_utils.facts.utils.test_utils import load_fixture
    from ansible.module_utils._text import to_text

    fact_collector_obj = SystemCapabilitiesFactCollector()

    mock_module = FactCollector(collected_facts={})
    mock_module.run_command = lambda x, errors='surrogate_then_replace': (0, load_fixture('capsh', to_text(x[0], errors=errors)), '')

    mock_module.get_bin_path = lambda x: '/bin/%s' % x

    result = fact_collector_obj.collect(module=mock_module, collected_facts={})

# Generated at 2022-06-13 02:25:23.757850
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    """
    Test method collect of class SystemCapabilitiesFactCollector
    """
    # Note: To mock this properly for testing - the following is required:
    #       * mock the run_command method of module object
    #       * mock the get_bin_path method of module object
    #       * Test systems with / without capsh installed.

    # Mock result from capsh

# Generated at 2022-06-13 02:25:31.799709
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts import collector
    from ansible.module_utils.facts.collector.system import SystemFactCollector
    from ansible.module_utils.facts.collector.system.capabilities import SystemCapabilitiesFactCollector

    # Initialize a mock module for getting correct binary paths
    module = type('Module', (object,), dict(run_command = lambda self, args, **kwargs: 0))

    caps_collector = SystemCapabilitiesFactCollector(module)

    # Initialize a mock system_facts dict
    system_facts = dict(collector=SystemFactCollector.name)

    # Collect facts and verify if the system_caps key is present
    caps_collector.collect(module=module, collected_facts=system_facts)

# Generated at 2022-06-13 02:25:41.927805
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    mod = MockModule()

# Generated at 2022-06-13 02:25:47.788790
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # NOTE: can't mock module.get_bin_path()?
    module = AnsibleModule()
    module.get_bin_path = get_bin_path

    collector = SystemCapabilitiesFactCollector(module=module)
    result = collector.collect()

    assert result == {
        'system_capabilities_enforced': 'False',
        'system_capabilities': ['cap_setuid', 'cap_setgid', 'cap_net_bind_service', 'cap_dac_override']
    }

# Generated at 2022-06-13 02:25:54.619416
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    class CollectedFacts():
        pass
    class Module():
        def __init__(self):
            self.params = {}
            self.called = False
        def get_bin_path(self, _):
            self.called = True
            return '/bin/capsh'
        def run_command(self, _, **kwarg):
            self.called = True
            return 0, 'Current: =ep\n', 'error'

    res = {'system_capabilities': [], 'system_capabilities_enforced': 'False'}
    module = Module()
    facts = CollectedFacts()
    facts.capsh_path = '/bin/capsh'
    facts = CollectedFacts()
    collector = SystemCapabilitiesFactCollector(module)
    result = collector.collect(module, facts)
    assert result

# Generated at 2022-06-13 02:25:56.355667
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    _SystemCapabilitiesFactCollector = SystemCapabilitiesFactCollector()
    _SystemCapabilitiesFactCollector.collect()

# Generated at 2022-06-13 02:25:59.801557
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # TODO: mock module.get_bin_path('capsh') and/or module.run_command(...) -akl
    pass

# Generated at 2022-06-13 02:26:08.135929
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import ansible.utils.display
    # set up test
    def run_module(*args, **kwargs):
        (rc, out, err) = (0,
            'Current: =ep',
            '')
        return rc, out, err
    module_mock = MagicMock()
    module_mock.run_command.side_effect = run_module
    module_mock.get_bin_path.return_value = True
    sys_caps_collector = SystemCapabilitiesFactCollector()
    collected_facts = {}

    # run test
    sys_caps_collector.collect(module_mock, collected_facts)

    # check results
    assert collected_facts['system_capabilities'] == []
    assert collected_facts['system_capabilities_enforced'] == 'False'

# Generated at 2022-06-13 02:26:18.550806
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # Initialization of class
    obj = SystemCapabilitiesFactCollector()

    # stub for method get_bin_path
    class_obj = SystemCapabilitiesFactCollector()
    class_obj.get_bin_path1 = lambda path : "/bin/capsh"
    # stub for method run_command
    class_obj.run_command1 = lambda cmd : (1, "Current: =", "")
    class_obj.run_command2 = lambda cmd : (1, "Current: =ep", "")
    # stub for method fact_id
    class_obj.fact_ids1 = lambda : {'system_capabilities':''}

    # execute code path 1 with method collect
    obj.get_bin_path = class_obj.get_bin_path1
    obj.fact_ids = class_obj.fact_ids1


# Generated at 2022-06-13 02:26:26.601351
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    def run_command_mock(module, command, check_rc=False, errors='surrogate_then_replace', run_on_shell=False):
        rc = 0

# Generated at 2022-06-13 02:27:29.253954
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    module = 'ansible.module_utils.facts.collector.get_file_content'
    capsh_path = 'ansible.module_utils.facts.collector.run_command'
    capsh_path_value = '/bin/capsh'

    # Test if system_capabilities_enforced returns NA
    m = importlib.import_module(module)
    m.get_file_content.return_value = ''
    c = importlib.import_module(capsh_path)
    c.run_command.return_value = (1, '', '')
    fact_collector = SystemCapabilitiesFactCollector()
    assert fact_collector.collect()['system_capabilities_enforced'] == 'NA'
    m.get_file_content.assert_called_with(capsh_path_value)


# Generated at 2022-06-13 02:27:39.567102
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():

    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts.system.caps import SystemCapabilitiesFactCollector

    class MockModule:
        def __init__(self):
            self.params = dict()
            self.paths = dict(
                [('bin', 'bin/')])

        def get_bin_path(self, path):
            return os.path.join(self.paths.get('bin'), path)


# Generated at 2022-06-13 02:27:49.129558
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.collector.system_capabilities import SystemCapabilitiesFactCollector

    # Test run of collect on platforms that do not support SystemCapabilitiesFactCollector
    # NOTE: in the future, when we have an instance method mocking lib, refactor/mock get_caps_data() -akl
    def get_bin_path(self, executable=None):
        return None
    # NOTE: in the future, when we have an instance method mocking lib, refactor/mock run_command() -akl

# Generated at 2022-06-13 02:27:52.244378
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    """
    Method collect() tests for
    SystemCapabilitiesFactCollector class
    Arguments: None
    Returns: None
    Raises: None
    """
    # NOTE: -akl to be implemented
    pass

# Generated at 2022-06-13 02:28:02.071844
# Unit test for method collect of class SystemCapabilitiesFactCollector

# Generated at 2022-06-13 02:28:10.653453
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import os
    import mock
    import ansible.module_utils.facts.collectors.system.capabilities as system_capabilities
    import ansible.module_utils.facts.collectors.system.capabilities as SystemCapabilitiesFactCollector

    test_capsh_path = os.path.join(os.path.dirname(__file__), '../../../support/capsh')

# Generated at 2022-06-13 02:28:13.534807
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector
    # TODO: Implement unit test
    # assert True


# Generated at 2022-06-13 02:28:23.234665
# Unit test for method collect of class SystemCapabilitiesFactCollector

# Generated at 2022-06-13 02:28:32.471316
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    class FakeModule:
        def __init__(self):
            self.paths = ["/bin"]
        def get_bin_path(self, cmd):
            if cmd == "capsh":
                return "/bin/capsh"
            return None
        def run_command(self, cmd, errors=None):
            return (0, "Current: =ep\nBounding set =cap_sys_chroot+ep\n", '')


# Generated at 2022-06-13 02:28:37.134060
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    module = MockModule(
        return_values={
            '/usr/sbin/capsh --print': (0, 'foo', ''),
        }
    )
    c = SystemCapabilitiesFactCollector(module=module)
    facts = c.collect()
    assert facts['system_capabilities'] == []
    assert facts['system_capabilities_enforced'] == 'NA'