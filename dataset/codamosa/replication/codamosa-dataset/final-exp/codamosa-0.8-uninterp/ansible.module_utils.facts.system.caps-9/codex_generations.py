

# Generated at 2022-06-13 02:19:55.736780
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(
        argument_spec = dict(),
        supports_check_mode=True
    )


# Generated at 2022-06-13 02:20:06.436657
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts.collector import FactsCollector
    import ansible.module_utils.facts.system.caps
    from ansible.module_utils.facts.system.caps import SystemCapabilitiesFactCollector
    import ansible.module_utils.facts.system
    from ansible.module_utils.facts.system import SystemCapabilitiesFactCollector

    master_collector = FactsCollector()
    master_collector.collectors = [SystemCapabilitiesFactCollector()]
    test_module = None
    # TODO: mock, set up collected_facts -akl
    collected_facts = None
    expected_facts = {
        'system_capabilities': [],
        'system_capabilities_enforced': 'NA',
    }

# Generated at 2022-06-13 02:20:14.125015
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts.fact_cache import FactCache
    fc = FactCache()
    fc.populate_cache = False
    fc.module = MockModule()
    fc.module.run_command = Mock()
    fc.module.run_command.return_value = (0, 'Current: =ep', '')
    scc = SystemCapabilitiesFactCollector(fc)

    collected_facts = {'other_fact':'value'}
    facts_dict = scc.collect(collected_facts=collected_facts)

    assert 'system_capabilities' in facts_dict
    assert facts_dict['system_capabilities_enforced'] == 'False'
    assert facts_dict['system_capabilities'] == []


# Generated at 2022-06-13 02:20:17.294700
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # NOTE: planned unit test for
    #   SystemCapabilitiesFactCollector._capsh_path = None
    #   SystemCapabilitiesFactCollector.collect()
    #   SystemCapabilitiesFactCollector._capsh_path = '/path/to/capsh'
    #   SystemCapabilitiesFactCollector.collect()
    pass

# Generated at 2022-06-13 02:20:24.652133
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts.system.caps.collector import SystemCapabilitiesFactCollector
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.plugins.loader import module_loader
    from ansible.vars.manager import VariableManager

    play_context = PlayContext()

    module_name = 'command'
    module_args = ''
    injected_args = {}
    loader.load_plugin(module_name)
    module = module_loader.get(module_name, **injected_args)

    variable_manager = VariableManager()
    variable_manager.extra_vars = {}

    results = None
    task_queue_manager = TaskQueue

# Generated at 2022-06-13 02:20:35.789102
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    module = MockAnsibleModule()
    module.get_bin_path.return_value = "capsh_path"
    capsh_cmd = ['capsh_path','--print']

# Generated at 2022-06-13 02:20:41.572177
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    """
    Test 'collect' method of SystemCapabilitiesFactCollector.
    """
    # Create an instance of SystemCapabilitiesFactCollector
    s = SystemCapabilitiesFactCollector()
    # Create an instance of AnsibleModule
    module = AnsibleModule()

    # Perform the method collect with no arguments
    # Returns nothing
    s.collect()



# Generated at 2022-06-13 02:20:50.170033
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # NOTE: using 'import mock' so we can mock both modules and functions!
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts import collector

    from unittest.mock import mock_open, patch
    from ansible.module_utils.facts.collector.system import SystemCapabilitiesFactCollector

    import builtins
    import os

    # the real 'open' method to restore after the test is done:
    real_open = builtins.open

    # the real 'os.path.exists' method to restore after the test is done:
    real_os_path_exists = os.path.exists

    # the real 'os.stat' method to restore after the test is done:
    real_os_stat = os.stat

    # the real '

# Generated at 2022-06-13 02:21:01.218818
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    """
    Create a dictionary of a dict with key "ansible_facts" and value that is a dict with the following keys:
    system_capabilities
    system_capabilities_enforced
    """
    # create a mock module and assign a mock return value to capsh_path
    from ansible.module_utils.facts.utils.capsh import get_caps_data, parse_caps_data
    import ansible.module_utils.facts.collector

    mock_module = ansible.module_utils.facts.collector.ModuleMock()
    mock_module.run_command = ansible.module_utils.facts.collector.ModuleMock()
    mock_module.get_bin_path.return_value = "capsh_path"

    # create a mock out and err string

# Generated at 2022-06-13 02:21:10.272761
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():

    # Mock AnsibleModule
    from ansible.module_utils.facts import ModuleFacts
    from ansible.module_utils.facts.collector.caps import SystemCapabilitiesFactCollector
    from ansible.module_utils.facts.system_capabilities import get_caps_data

    # Mock AnsibleModule
    mock_AnsibleModule = ModuleFacts.AnsibleModule

    # Mock FactsCollector
    class MockFactsCollector:
        def __init__(self):
            self.name = 'caps'
            self._fact_ids = set(['system_capabilities',
                                  'system_capabilities_enforced'])
        def collect(self, module=None, collected_facts=None):
            return collected_facts

    # Create empty results dictionary
    results_dict = {}
    # Add entries for _fact_

# Generated at 2022-06-13 02:21:17.670045
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts.collector import DummyModule
    from mock import MagicMock, patch

    module = DummyModule()
    module.run_command = MagicMock(return_value=(0, 'Current: \n', ''))

    facter = SystemCapabilitiesFactCollector()

    fact_out = facter.collect(module=module, collected_facts=None)

    assert fact_out['system_capabilities_enforced'] == 'NA'


# Generated at 2022-06-13 02:21:23.433209
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts import collector

    # Set up module
    module = MagicMock()
    module.run_command.return_value = (0, 'line1\nline2\nline3\n', '')
    module.get_bin_path.return_value = "capsh_path"

    # Run method under test and verify it returns expected facts
    cap_fc = SystemCapabilitiesFactCollector()
    res = cap_fc.collect(module)
    assert res == {'system_capabilities_enforced': 'True', 'system_capabilities': ['cap1', 'cap2', 'cap3']}

    # Verify the expected module methods are called

# Generated at 2022-06-13 02:21:35.278737
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # Mock module object
    class MockModule(object):
        def get_bin_path(self, program, opt_dirs=[]):
            capsh_path = 'capsh'
            return capsh_path
    dummy_module = MockModule()
    # Mock subprocess object
    class MockSubProcess(object):
        def __init__(self, capsh_path, errors='surrogate_then_replace'):
            self.capsh_path = capsh_path
            self.errors = errors
            self.rc = 0
            self.out = "Current: =ep"
            self.err = None

    dummy_subprocess = MockSubProcess(dummy_module.get_bin_path('capsh'))
    # Mock run_command method

# Generated at 2022-06-13 02:21:45.379199
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
  import tempfile
  import os
  from ansible.module_utils.facts.collector import BaseFactCollector

  cp = SystemCapabilitiesFactCollector()
  c_facts = BaseFactCollector()
 
  # Unit test to check if system capabilities are being collected
  # if capsh returns a non-zero exit code

# Generated at 2022-06-13 02:21:52.704345
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils.facts.collector import FactCollector

    # NOTE: inject mock module for testing

# Generated at 2022-06-13 02:21:54.304244
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    test_object = SystemCapabilitiesFactCollector()

    # Call method collect of object
    test_object.collect()

# Generated at 2022-06-13 02:22:01.825165
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    test_module = object()
    
    def test_run_command(args,errors):
        if args[0] == "/usr/bin/capsh":
            if args[1] == "--print":
                return (0,'Current: =ep\nBounding set =ep cap_audit_write+eip cap_dac_read_search+eip cap_setgid+ep cap_setuid+ep cap_setpcap+ep\nSecurebits: 00/0x0/1'+'\n'*11+'Secure LSM:   \nSecure LSM:   \n',None)
                # example output of command /usr/bin/capsh --print 
                # Current: =ep
                # Bounding set =ep cap_audit_write+eip cap_dac_read_search+eip cap

# Generated at 2022-06-13 02:22:07.421772
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # Create a mock module object
    class MockModule:
        def __init__(self, shell, shell_path, bin_path):
            self.bin_path = bin_path
        def run_command(self, cmd, errors):
            return 0, "", ""
        def get_bin_path(self, cmd):
            return self.bin_path
    # Test with and without capsh present
    # Test data consists of expected return data, output of capsh --print and path to capsh
    # We are not using a full blown mock as we want to see if the code really can cope with
    # the various outputs of capsh as this is the source of the data

# Generated at 2022-06-13 02:22:14.841165
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # test run_command() is called, and system_capabilities set.
    m = None
    c = None
    f = SystemCapabilitiesFactCollector()
    module = lambda *args, **kwargs: (0, "Current: =ep\n", "")
    module.get_bin_path = lambda *args, **kwargs: 'capsh'
    facts = f.collect(module=module, collected_facts={})
    assert facts['system_capabilities_enforced'] == 'False'
    assert facts['system_capabilities'] == []

# test capsh executable not available

# Generated at 2022-06-13 02:22:23.371714
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():

    # Create a class C to be used for testing.
    # The next 3 methods of C will be used for mocks for module_utils.basic.AnsibleModule.run_command()
    # def run_command(self, args, check_rc=True, close_fds=True, executable=None, data=None, binary_data=False, path_prefix=None, cwd=None, use_unsafe_shell=False, prompt_regex=None, environ_update=None, umask=None, errors='strict', encoding=None):
    class C:

        def __init__(self):
            self.run_command_results = []


# Generated at 2022-06-13 02:22:31.250416
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # NOTE: SystemCapabilitiesFactCollector.collect() -> 'NA'
    # NOTE: SystemCapabilitiesFactCollector.collect() -> None
    # NOTE: SystemCapabilitiesFactCollector.collect() ->
    #       dict(system_capabilities=[], system_capabilities_enforced='NA')
    pass

# Generated at 2022-06-13 02:22:33.768711
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    fact_collector = SystemCapabilitiesFactCollector()
    module_mock = mock_module_helper()
    fact_collector.collect(module=module_mock)
    assert not module_mock.run_command.called

# Generated at 2022-06-13 02:22:39.471960
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():

    # Import module(s) and mock capabilities discovery
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts import collectd
    from ansible.module_utils.facts.collector import gather_subset

    # Create mock module
    module_mock = MagicMock()
    module_mock.run_command.return_value = (0, "Current: =ep", "")
    module_mock.get_bin_path.return_value = "/bin/capsh"

    # Create mock facts object
    collected_facts_mock = MagicMock()
    collected_facts_mock.update.return_value = ""

    # Create SystemCapabilitiesFactCollector object
    systemcapabilitiesfactcollector = SystemCapabilitiesFactCollector()

    # Collect facts
   

# Generated at 2022-06-13 02:22:49.861818
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts import collector
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils._text import to_bytes
    from mock import Mock
    from io import StringIO
    from ansible.module_utils.parsing.convert_bool import boolean
    mock_module = Mock()
    mock_module.run_command.return_value = (0, 'Current:=ep', '')
    system_capabilities_collector = SystemCapabilitiesFactCollector(mock_module)

    # Collector should return a dictionary with keys in fact_ids
    collected_facts = system_capabilities_collector.collect()
    assert 'system_capabilities_enforced' in collected_facts.keys()
    assert 'system_capabilities' in collected_facts.keys()

# Generated at 2022-06-13 02:22:58.150610
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import mock
    import os
    import tempfile
    module_mock = mock.Mock()
    module_mock.get_bin_path.return_value = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'test_data', 'capsh')
    fh, filepath = tempfile.mkstemp()
    os.write(fh, "line 1 \nline 2 \nline 3")
    os.close(fh)
    # execute method under test
    sut = SystemCapabilitiesFactCollector()
    result = sut.collect(module=module_mock, collected_facts=None)
    os.remove(filepath)
    # validate result
    assert(result['system_capabilities_enforced'] == 'True')

# Generated at 2022-06-13 02:23:07.681857
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    '''
    Unit test for method collect of class SystemCapabilitiesFactCollector.
    '''
    # NOTE: separate tests for each dict key
    #       -> easier to test key exists, expected value, etc.
    def run_caps_test(test_dict):
        '''
        Utility function for running SystemCapabilities test with defined
        dictionary and returning a dict of the results.
        '''
        from ansible.module_utils.facts.collector import BaseFactCollector
        import ansible.module_utils.basic

        class module_mock:
            def __init__(self, current_out, current_err, current_rc):
                self.run_command_output = current_out
                self.run_command_rc = current_rc

            def get_bin_path(self, path):
                return path


# Generated at 2022-06-13 02:23:18.094787
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    
    class mock_module:
        def __init__(self):
            self.run_command_result = 0

# Generated at 2022-06-13 02:23:28.329163
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector

    class MockModule():
        class MockRunCommand():
            def __init__(self, *args):
                if args[0] == ['/usr/bin/capsh', '--print']:
                    self.rc = 0
                    self.out = '''Current: =ep
Bounding set =ep
Secure bits: 00/0x0/1'b0
secure-noroot: no (unlocked)
secure-no-suid-fixup: no (unlocked)
secure-keep-caps: no (unlocked)
uid=0(root)
gid=0(root)
groups=0(root)'''
                    self.err = ''
                else:
                    raise ValueError('Invalid call to MockRunCommand: {}'.format(args))
           

# Generated at 2022-06-13 02:23:37.624585
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    class FakeAnsibleModule():
        def get_bin_path(self, name):
            return '/bin/capsh'
        def run_command(self, cmd, errors='surrogate_then_replace'):
            return (0, ' Current: = cap_chown,cap_dac_override,cap_dac_read_search+eip', None)
    sut = SystemCapabilitiesFactCollector()
    data = sut.collect(FakeAnsibleModule())
    assert 'system_capabilities' in data
    assert 'system_capabilities_enforced' in data
    assert data['system_capabilities'] == ['cap_chown', 'cap_dac_override', 'cap_dac_read_search']
    assert data['system_capabilities_enforced'] == 'True'

# Generated at 2022-06-13 02:23:47.170493
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # make an instance of the class to test
    cp = SystemCapabilitiesFactCollector()
    # need to setup some fake values
    cp.module = None
    cp.collected_facts = None
    #
    module = cp.module
    collected_facts = cp.collected_facts
    rc = 0

# Generated at 2022-06-13 02:24:01.462992
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # NOTE: implement unit test of method collect of class SystemCapabilitiesFactCollector -akl
    pass

# Generated at 2022-06-13 02:24:09.529817
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts.system.caps import SystemCapabilitiesFactCollector
    from ansible.module_utils._text import to_native
    from ansible.module_utils.facts.system import cached_facts

    # Mock 'module' object
    class MockModule(object):
        def __init__(self, bin_path_value, return_value):
            self.bin_path_value = bin_path_value
            # 'capsh' path should return the correct output
            self.run_command_value = return_value

        # The get_bin_path method
        def get_bin_path(self, arg, opt_dirs=None):
            if arg == 'capsh':
                return self.bin_path_value

        # The run_command method

# Generated at 2022-06-13 02:24:21.103389
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import sys
    import platform
    import pprint

    test_module = get_module_mock(platform.system(), sys.version_info)

    # NOTE: for unit tests -akl
    ModuleReturn = namedtuple('ModuleReturn', ['rc','stdout','stderr'])

# Generated at 2022-06-13 02:24:30.039445
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import sys
    if sys.version_info[0] == 2:
        from mock import patch
    else:
        from unittest.mock import patch

    from ansible.module_utils.facts import collector


    class ModuleMock(object):
        def __init__(self):
            self.params={'collect_subset':['all']}
            self.check_mode=False
            self.debug=False
            self.run_command=lambda *args, **kwargs: (0, 'Current: =ep', '')
            self.get_bin_path=lambda *args, **kwargs: '/pretend/path/to/capsh'

    class TestClass(object):
        # Test class via collect()
        def __init__(self):
            self.module = ModuleMock()
            self.collector

# Generated at 2022-06-13 02:24:37.183286
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts.collector import ResolvedFacts
    from ansible.module_utils.facts.collector import get_collector_instance
    from ansible.module_utils.facts import ansible_collector

    mod = ansible_collector._create_ansible_module()
    mod.run_command = lambda x, errors='surrogate_then_replace': \
            ('0', 'Current: = cap_chown,cap_dac_override,cap_fowner+ep', '')

    module = mod

    resolved_facts = ResolvedFacts()
    _collected_facts = get_collector_instance('system_capabilities').collect(module=module, collected_facts=resolved_facts)


# Generated at 2022-06-13 02:24:47.917141
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import sys
    import os.path

    class m_module(object):
        def get_bin_path(self, cmd):
            return cmd
        def run_command(self, cmd, *args, **kwargs):
            class m_result(object):
                def __init__(self, cmd):
                    self.cmd = cmd
                    self.rc = 1
                    self.stdout = ''
                    self.stderr = 'run_command() called with %s' % cmd
            if cmd[0] == 'capsh':
                # capsh --print
                self.calls['run_command'] += 1
                return m_result(cmd)
            else:
                raise Exception("unexpected run_command() call: %s" % cmd)

    # set up mocks
    m_module_instance = m_module()


# Generated at 2022-06-13 02:24:55.156246
# Unit test for method collect of class SystemCapabilitiesFactCollector

# Generated at 2022-06-13 02:25:05.982359
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts.collector import AnsibleModule
    from ansible.module_utils import basic
    from ansible.module_utils.six import b
    from ansible.module_utils._text import to_bytes


# Generated at 2022-06-13 02:25:12.453763
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    module_mock = MagicMock()
    failed_module_mock = MagicMock()


# Generated at 2022-06-13 02:25:23.071052
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    class mock_module(object):
        def __init__(self):
            self.run_command_called = 0

        @staticmethod
        def get_bin_path(binary):
            return '/bin/capsh'

        def run_command(self, args, **kwargs):
            self.run_command_called += 1

# Generated at 2022-06-13 02:25:54.305728
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import mock

    testmodule = mock.MagicMock()
    testmodule.get_bin_path.return_value = '/usr/bin/capsh'

# Generated at 2022-06-13 02:25:54.954759
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    pass

# Generated at 2022-06-13 02:26:05.350188
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.collectors.system.caps import SystemCapabilitiesFactCollector
    from ansible.module_utils.facts.collectors.system import caps

    module = BaseFactCollector()
    caps_collector = SystemCapabilitiesFactCollector(module=module)
    # NOTE: mock run_command() to return predefined caps data -akl
    result = caps_collector.collect()

    assert result['system_capabilities_enforced'] == 'True'

# Generated at 2022-06-13 02:26:09.234658
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # NOTE: future - turn this into a pytest
    mod = None
    facts = {} # NOTE: refactor to use facts.pop(SystemCapabilitiesFactCollector.name, {})
    sut = SystemCapabilitiesFactCollector()
    result = sut.collect(mod, facts)
    assert result
    assert result['system_capabilities']
    assert result['system_capabilities_enforced']

# Generated at 2022-06-13 02:26:14.815920
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # Initial setup of test data and test object
    data={'system_capabilities': ['cap_sys_admin', 'cap_sys_nice'], \
          'system_capabilities_enforced': 'False'}
    collector = SystemCapabilitiesFactCollector()
    # Call method collect with mock data
    result = collector.collect(module=None, collected_facts=data)
    # Verify results
    assert data == result

# Generated at 2022-06-13 02:26:23.869153
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils import basic
    import os
    import sys

    class TestModule(object):
        def __init__(self, **kwargs):
            for k, v in kwargs.items():
                setattr(self, k, lambda *a, **kw: v)

        def run_command(self, cmd, check_rc=None, close_fds=None, executable=None, data=None, binary_data=False, path_prefix=None, cwd=None, use_unsafe_shell=False, env_strings=None, environ_update=None, umask=None, errors='surrogate_or_stderr', warn_only=False, created_tempfiles=None):
            import json

# Generated at 2022-06-13 02:26:33.975087
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # Create instance of module
    module = AnsibleModule(argument_spec={})

# Generated at 2022-06-13 02:26:41.372330
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts.system.caps import SystemCapabilitiesFactCollector
    import os
    import re
    import tempfile
    import os.path
    mytmpdir = tempfile.gettempdir()
    mytmpfile = os.path.join(mytmpdir, 'capsh.out')

# Generated at 2022-06-13 02:26:43.527960
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    class TestModule(object):
        def get_bin_path(self, prog):
            return '/bin/capsh'

        def run_command(self, args, errors):
            return 0, '', ''

    x = SystemCapabilitiesFactCollector()
    x.collect(module=TestModule(), collected_facts={})

# Generated at 2022-06-13 02:26:47.649439
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    collector = SystemCapabilitiesFactCollector()
    module = object
    module.run_command = lambda x: ("", "Current: =ep", "")
    collector.collect(module)
    assert collector._fact_ids == set(['system_capabilities', 'system_capabilities_enforced'])

# Generated at 2022-06-13 02:28:00.114326
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts import FactCollector
    # Setup
    Module = MockModule()
    FactCollector.collectors = [SystemCapabilitiesFactCollector()]
    # Exercise/Assert
    facts = FactCollector._collect(Module)
    assert facts['system_capabilities_enforced'] == 'True'

# Generated at 2022-06-13 02:28:04.858230
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import ansible.module_utils.facts.collector
    ansible.module_utils.facts.collector.CAPSH_PATH="/usr/bin/capsh"
    ansible.module_utils.facts.collector.CAPSH_PATH=None
    import ansible.module_utils.facts.collector.SystemCapabilitiesFactCollector as C
    c = C.SystemCapabilitiesFactCollector()
    c.collect()


# Generated at 2022-06-13 02:28:08.967711
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import builtins
    from ansible.module_utils.facts.collector import BaseFactCollector
    isinstance(SystemCapabilitiesFactCollector(BaseFactCollector), builtins.object)
    #self.assertIsInstance(SystemCapabilitiesFactCollector(BaseFactCollector), builtins.object)

# Generated at 2022-06-13 02:28:14.109413
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    '''
    test method collect of class SystemCapabilitiesFactCollector
    '''
    # NOTE: add example capsh output to file 'ut_system_caps.txt'
    f = open('./ut_system_caps.txt', 'r')
    capsh_output = f.read()
    f.close()

    class MockModule(object):

        def __init__(self):
            self.params = None

        def run_command(self, cmd, errors='surrogate_then_replace'):
            return 0, capsh_output, ''

        def get_bin_path(self, bin_name):
            return '/usr/bin/capsh'

    class MockCollectedFacts(object):
        def __init__(self):
            self.system_capabilities = None
            self.system_capabilities_

# Generated at 2022-06-13 02:28:18.189657
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts.collector import AnsibleModule, get_bin_path

    # ansible module requires init of module_utils
    AnsibleModule(argument_spec=dict())

    # prepare input data
    capsh_path = get_bin_path('capsh')
    if capsh_path:
        # NOTE: -> get_caps_data()/parse_caps_data() for easier mocking -akl
        rc, out, err = AnsibleModule.run_command([capsh_path, "--print"], errors='surrogate_then_replace')
        enforced_caps = []
        enforced = 'NA'
        for line in out.splitlines():
            if len(line) < 1:
                continue

# Generated at 2022-06-13 02:28:18.518706
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    assert 1 == 2

# Generated at 2022-06-13 02:28:22.940091
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    '''
    unit test for SystemCapabilitiesFactCollector method 'collect'
    '''

    # Mock module object
    module = AnsibleModule(argument_spec={}, supports_check_mode=True)
    module.run_command = Mock(return_value=(0, 'Current: =ep\n', ''))
    module.get_bin_path = Mock(return_value='/bin/capsh')

    # Create instance of SystemCapabilitiesFactCollector class
    S = SystemCapabilitiesFactCollector()

    # Use instance of SystemCapabilitiesFactCollector class to invoke its collect method
    result = S.collect(module)

    # Verify that result is correct
    expected = dict(system_capabilities=[],system_capabilities_enforced='False')
    assert result == expected

# Generated at 2022-06-13 02:28:32.257774
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts.collectors.system.capabilities import SystemCapabilitiesFactCollector
    collector_name = SystemCapabilitiesFactCollector.name
    capsh_path = '/bin/capsh'

# Generated at 2022-06-13 02:28:40.782050
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible_collections.ansible.community.tests.unit.compat.mock import Mock

    module = Mock()
    module.get_bin_path.return_value = 'capsh_test'

    mock_run_command = Mock()

# Generated at 2022-06-13 02:28:42.680832
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    fixture = SystemCapabilitiesFactCollector(None)
    output = fixture.collect()
    assert 'system_capabilities' in output.keys()
    # NOTE: remove 'capsh' invocation, as it is distracting -akl
    assert 'system_capabilities_enforced' in output.keys()