

# Generated at 2022-06-12 21:30:24.696420
# Unit test for function discover_interpreter
def test_discover_interpreter():

    task_vars = {}
    class MockAction(object):
        def __init__(self, action_vars):
            self._low_level_execute_command = lambda command, **kwargs: {'stdout': action_vars['stdout']}
            self._discovery_warnings = action_vars['warnings']
            self._connection = {'has_pipelining': False}

    # Test 1: check that the correct interpreter is returned
    action_vars = {'stdout': u'PLATFORM\nLinux\nFOUND\n/usr/bin/python2\n/usr/bin/python3\nENDFOUND',
                   'warnings': []}
    action = MockAction(action_vars)
    expected_output = u'/usr/bin/python2'
    assert discover_interpre

# Generated at 2022-06-12 21:30:33.260572
# Unit test for function discover_interpreter
def test_discover_interpreter():
    display.verbosity = 4
    fake_action = ActionModule()
    test_task_vars = {}
    assert discover_interpreter(fake_action, 'python', 'auto_silent', test_task_vars)

    test_task_vars = {'ansible_verbosity': '-vvvv'}

    platform_python_map = C.config.get_config_value('INTERPRETER_PYTHON_DISTRO_MAP', variables=test_task_vars)
    bootstrap_python_list = C.config.get_config_value('INTERPRETER_PYTHON_FALLBACK', variables=test_task_vars)

    assert discover_interpreter(fake_action, 'python', 'auto_silent', test_task_vars) == '/usr/bin/python'



# Generated at 2022-06-12 21:30:34.338505
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # unit test stub
    raise NotImplementedError()

# Generated at 2022-06-12 21:30:45.269180
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.executor.discovery import discover_interpreter
    from ansible.plugins.discovery import auto
    from ansible.plugins.action import ActionBase

    class TestAction(ActionBase):
        def _low_level_execute_command(self, cmd, sudoable=True, in_data=None):
            return {'stdout': self.bootstrap_results[cmd]}

        def run(self, tmp=None, task_vars=None):
            raise NotImplementedError()

    test_action = TestAction()

# Generated at 2022-06-12 21:30:56.493380
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.vars.hostvars import HostVars
    from ansible.vars.manager import VariableManager
    from ansible.plugins.loader import shared_loader_obj
    from ansible.plugins.action import ActionBase
    from ansible.plugins.connection.ssh import Connection
    from ansible.executor.task_queue_manager import TaskQueueManager
    import os

    # This needs to be custom for each test. To get the value, run `ansible -m setup -a "gather_subset=!all,min" localhost`
    # and look at the `ansible_facts['ansible_processor_vcpus']` value.
    num_vcpus = 1
    print("There are {0} CPUs available for this test".format(num_vcpus))
    # There are 1 CPUs available for this test

# Generated at 2022-06-12 21:31:05.780753
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.plugins.action import ActionBase
    from ansible.executor.task_result import TaskResult

    # success case
    class MockAction(ActionBase):
        def _low_level_execute_command(self, *args, **kwargs):
            cmd = args[0]
            if cmd.startswith('command'):
                return TaskResult(res=None, stdout='/usr/bin/python2', stderr='')
            elif cmd == '/usr/bin/python':
                return TaskResult(res=None, stdout='{"platform_dist_result": ["fedora", "21", "Twenty One"], '
                                                   '"osrelease_content": "ID=fedora\nVERSION_ID=21\n"}', stderr='')

# Generated at 2022-06-12 21:31:14.832560
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.module_utils._text import to_text
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.module_utils.connection import Connection
    from ansible.module_utils.connection.persistent import PersistentConnection
    from ansible.module_utils.connection.smart import SmartConnection

    task_vars = dict()
    task_vars['ansible_python_interpreter'] = u'/foo/bar'

    # test discover_interpreter
    action = Connection(None, None)
    # test connection type
    assert isinstance(action, Connection)
    assert issubclass(action.__class__, Connection)
    assert isinstance(action, PersistentConnection)
    assert issubclass(action.__class__, PersistentConnection)

# Generated at 2022-06-12 21:31:25.439629
# Unit test for function discover_interpreter
def test_discover_interpreter():

    interpreter_name = 'python'
    discovery_mode = 'auto'

    # Test set 1
    # Data for this test set is:
    #   No Python interpreter found for host localhost (tried [u'/usr/bin/python', u'/usr/bin/python2.6', u'/usr/bin/python2.7', u'/usr/local/bin/python2.7', u'/usr/bin/python3'])
    #   Platform darwin on host localhost is using the discovered Python interpreter at /usr/bin/python, but future installation of another Python interpreter could change the meaning of that path
    action = discover_interpreter(None, 'python', 'auto', {'inventory_hostname': 'localhost'})
    assert action is None

    # Test set 2
    # Data for this test set is:
    #   No python

# Generated at 2022-06-12 21:31:38.279065
# Unit test for function discover_interpreter
def test_discover_interpreter():
    import pytest
    from ansible.module_utils.common.removed import removed_class
    from ansible.executor.discovery import get_interpreter_facts
    from ansible.executor.task_queue_manager import TaskQueueManager
    import os
    import tempfile

    test_interpreter_facts_depth = ['python']

    with pytest.raises(ValueError):
        discover_interpreter(None, 'foo', 'auto_silent', {})

    # test that discovery raises an exception if the discovery mode is not supported
    with pytest.raises(NotImplementedError):
        discover_interpreter(None, 'python', 'auto', {})

    tmpdir = tempfile.mkdtemp(prefix='ansible-test-discover-python-interpreter-')

# Generated at 2022-06-12 21:31:39.640083
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # TODO: Implement unit test in unit tests directory
    pass

# Generated at 2022-06-12 21:32:00.674989
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.mock.plugins.action.discovery_test import TestInterpreterDiscovery

    test_host = 'testhost'
    find_python_result = """PLATFORM
Linux

FOUND
/usr/bin/python
/usr/bin/python2.7

ENDFOUND"""

    # first test: discovery mode is 'auto' and the target has python2.7. We expect output of the discovery_interpreter
    # function to be '/usr/bin/python2.7'
    task_vars = {'inventory_hostname': test_host}
    test_action = TestInterpreterDiscovery(task_vars)
    test_action._connection.has_pipelining = True

# Generated at 2022-06-12 21:32:13.531814
# Unit test for function discover_interpreter
def test_discover_interpreter():

    # GIVEN a direct call to the function with a discovery_mode
    self = None
    action = self
    action._connection = self
    action._connection.has_pipelining = True
    task_vars = {"inventory_hostname": "test_host", "ansible_python_interpreter": None}
    # WHEN the discovery_mode is "auto_legacy_silent"
    interpreter_name = "python"
    discovery_mode = "auto_legacy_silent"
    # THEN the function does not fail
    discovered_python_path = discover_interpreter(action, interpreter_name, discovery_mode, task_vars)
    assert discovered_python_path is not None

    # WHEN the discovery_mode is "auto_silent"
    interpreter_name = "python"

# Generated at 2022-06-12 21:32:24.840312
# Unit test for function discover_interpreter
def test_discover_interpreter():
    import ansible
    import os
    import shutil
    import tempfile
    import pytest
    from ansible.module_utils import interpreter_discovery
    from ansible.parsing.dataloader import DataLoader

    if os.path.isfile('/etc/os-release'):
        shutil.copy2('/etc/os-release', './os-release')

    class Action:
        def __init__(self):
            self.test_task_vars = {"ansible_python_interpreter": "/usr/bin/python2.7", "inventory_hostname": "fake_host"}
            self.ds = DataLoader()
            self.test_sys = 'Linux'
            self.test_discovery_mode = 'auto'
            self.test_base_dir = tempfile.mkdtemp

# Generated at 2022-06-12 21:32:35.789534
# Unit test for function discover_interpreter
def test_discover_interpreter():
    host = 'testhost'
    res_mock = dict()

    # FUTURE: change this test to mock the action and _low_level_execute_command?
    # FUTURE: have a separate test for the bootstrap stage?

    # test not yet implemented
    try:
        discover_interpreter(None, 'python2', 'auto', dict())
    except NotImplementedError:
        pass
    else:
        raise AssertionError('"python2" interpreter discovery supported, expected not yet implemented')

    # test wrong interpreter name
    try:
        discover_interpreter(None, 'foo', 'auto', dict())
    except ValueError:
        pass
    else:
        raise AssertionError('wrong interpreter name, expected ValueError')

    # test known platform

# Generated at 2022-06-12 21:32:41.598803
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # Test without python interpreters in bootstrap list
    interpreter = discover_interpreter(None, 'python', 'auto', {'inventory_hostname': 'host'})
    assert interpreter == '/usr/bin/python'

    # Test without inventory hostname
    interpreter = discover_interpreter(None, 'python', 'auto', {})
    assert interpreter == '/usr/bin/python'

# Generated at 2022-06-12 21:32:44.684160
# Unit test for function discover_interpreter
def test_discover_interpreter():
    assert discover_interpreter('python', 'auto_legacy_silent') == '/usr/bin/python'
    assert discover_interpreter('python', 'auto_legacy_warn') == '/usr/bin/python'

# Generated at 2022-06-12 21:32:53.345644
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # Setup Mock Action
    class MockAction(object):
        def __init__(self):
            self._discovery_warnings = []
            self.warnings = []
            self._connection = MockConnection()

        def _low_level_execute_command(self, command, sudoable=True, in_data=None):
            cmd = 'echo PLATFORM\nlinux\necho FOUND\n/usr/bin/python\n/usr/bin/python3\necho ENDFOUND'
            res = {'stdout': cmd.encode('utf-8'), 'stderr': u'', 'rc': 0}
            return res

    class MockConnection(object):
        def __init__(self):
            self.has_pipelining = True

    mock_action = MockAction()

    # Test 1 - /usr/

# Generated at 2022-06-12 21:32:57.600513
# Unit test for function discover_interpreter
def test_discover_interpreter():
    action = None
    task_vars = {}

    try:
        discover_interpreter(action, 'python', 'auto', task_vars)
        assert False
    except NotImplementedError:
        pass

# Generated at 2022-06-12 21:33:08.838771
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.executor.task_executor import TaskExecutor
    from ansible.module_utils.facts.virtual import Virtual, virtuals
    from ansible.plugins.action import ActionBase

    class ModuleFailer(ActionBase):
        def run(self, *args, **kwargs):
            raise Exception('module failure')


# Generated at 2022-06-12 21:33:16.337742
# Unit test for function discover_interpreter
def test_discover_interpreter():
    """ Test for a variety of use cases the discover_interpreter function """

    from ansible.plugins.action.normal import ActionModule as _ActionModule
    from ansible.module_utils.six import binary_type

    class ActionModule(_ActionModule):
        _discovery_warnings = []

        def _low_level_execute_command(self, *args, **kwargs):
            return {'stdout': b'', 'stderr': ''}

    class MockConnection(object):
        has_pipelining = True

    action_module = ActionModule(task=dict(), connection=MockConnection(), play_context=None, loader=None, templar=None, shared_loader_obj=None)

    action_module._connection = MockConnection()

    host = 'mockhost'
    task_vars = dict()

   

# Generated at 2022-06-12 21:33:33.042350
# Unit test for function discover_interpreter
def test_discover_interpreter():
    try:
        import unittest2 as unittest
    except ImportError:
        import unittest
    from ansible import errors
    from ansible.mock import MagicMock
    from ansible.utils.connection import Connection

    # Needed to load the module/executor
    import ansible.modules.utilities.extract
    import ansible.executor.discovery
    import ansible.executor.task_result
    import ansible.executor.play_iterator
    import ansible.playbook.play

    # Stubs
    class FakeAction(object):
        def __init__(self):
            self._low_level_execute_command = MagicMock()

# Generated at 2022-06-12 21:33:39.991810
# Unit test for function discover_interpreter
def test_discover_interpreter():
    import ansible.executor.module_common as module_common
    from ansible.executor.module_common import CACHED_INTERPRETER_DISCOVERIES

    test_task_vars = dict(ansible_facts=dict(distribution=u'RedHat', ansible_distribution=u'RedHat', ansible_distribution_version=u'7.1'))
    action_plugin = module_common.ActionBase()


# Generated at 2022-06-12 21:33:52.591487
# Unit test for function discover_interpreter
def test_discover_interpreter():

    import os


# Generated at 2022-06-12 21:34:03.497007
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.executor.discovery import discover_interpreter
    from ansible.plugins.action import ActionBase
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager

    # Test with a python3 interpreter
    class TestAction(ActionBase):
        _discovery_warnings = []
        _discovery_failed = False
        _low_level_execute_command_calls = []
        _connection = None
        _task = None

        def warn(self, msg):
            self._discovery_warnings.append(msg)

        def fail_json(self, *args, **kwargs):
            self._discovery_failed = True


# Generated at 2022-06-12 21:34:12.986730
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    action = object()
    action.name = 'test_task'
    action._connection = object()
    action._connection.has_pipelining = True
    action._connection.supports_persistence = False

# Generated at 2022-06-12 21:34:21.931010
# Unit test for function discover_interpreter
def test_discover_interpreter():
    action = None
    interpreter_name = "python"
    discovery_mode = "auto_legacy"
    task_vars = {'inventory_hostname': 'test_host'}

    try:
        print("Testing interpreter discovery.")
        print("Interpreter discovery should succeed.")
        print("Expected result: /usr/bin/python")
        print("Received result: " + discover_interpreter(action, interpreter_name, discovery_mode, task_vars))
    except Exception as e:
        print("Interpreter discovery failed.")
        print(e)

    task_vars['inventory_hostname'] = 'test_host2'


# Generated at 2022-06-12 21:34:29.025323
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.utils.vars import combine_vars
    from ansible.inventory.host import Host
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    # FIXME: create a pseudo-action object?
    loader = DataLoader()
    host = Host('foo', False)
    hostvars = dict(ansible_connection='local')
    loader.set_basedir('/')
    vars_manager = VariableManager()
    vars_manager._fact_cache = dict()
    vars_manager._host_vars_files = dict()
    vars_manager.set_inventory(loader.load(hostvars))
    host.set_variable_manager(vars_manager)

    # test auto discovery, specific to EL8
    # FIX

# Generated at 2022-06-12 21:34:41.408985
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.executor.module_common import ACTION_SHELL

    action = ACTION_SHELL
    interpreter_name = 'python'
    discovery_mode = 'auto'
    task_vars = {'inventory_hostname': 'localhost'}

    # test with default config file
    result = discover_interpreter(action, interpreter_name, discovery_mode, task_vars)
    assert result == '/usr/bin/python'

    # test with non-default config file
    C.config.initialize_safe_config_dir('/tmp/ansible_test')
    # make sure the modules subdir exists
    C.config.initialize_module_cache()
    result = discover_interpreter(action, interpreter_name, discovery_mode, task_vars)
    assert result == '/usr/bin/python'



# Generated at 2022-06-12 21:34:51.529177
# Unit test for function discover_interpreter
def test_discover_interpreter():
    import unittest

    import ansible.module_utils.common.collections
    import ansible.module_utils.connection
    import ansible.module_utils.network
    import ansible.module_utils.shell
    import ansible.module_utils.system

    import ansible.module_utils.compat.ipaddress

    result = ansible.module_utils.system.distribution_detector()
    discovery_mode = 'auto_legacy_silent'
    task_vars = {'ansible_interpreter_python': discover_interpreter}
    action = ansible.module_utils.shell.ShellModule(
        connection=ansible.module_utils.connection.Connection(play_context=None),
        no_log=False,
        task_vars=task_vars
    )

# Generated at 2022-06-12 21:35:00.771587
# Unit test for function discover_interpreter
def test_discover_interpreter():
    import pytest
    from ansible.executor.discovery import discover_interpreter
    from ansible.utils.display import Display
    import ansible.module_utils.distro
    import ansible.module_utils.six
    from ansible.module_utils.six.moves import cStringIO as StringIO

    # disable cache so we can get to our fake LinuxDistribution.__str__()
    ansible.module_utils.distro.os_release_cache = {}

    # give our test a "not-implemented" error
    def fake_not_implemented_error_handler(err, task_vars):
        raise NotImplementedError()
    Display.exception = fake_not_implemented_error_handler

    # give our test a "known-python-on-host" error

# Generated at 2022-06-12 21:35:22.338772
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # python discovery with exact match
    task_vars = dict()
    task_vars['inventory_hostname'] = 'testhost'
    task_vars['ansible_python_interpreter'] = '/usr/bin/python'
    task_vars['ansible_python_version'] = '2.7.5'
    action = dict()
    action['_connection'] = dict()
    action['_connection']['has_pipelining'] = True
    action['_low_level_execute_command'] = dict()
    action['_low_level_execute_command']['stdout'] = 'PLATFORM; Linux; FOUND; /usr/bin/python; echo ENDFOUND'
    result = discover_interpreter(action, 'python', 'auto', task_vars)

# Generated at 2022-06-12 21:35:30.298157
# Unit test for function discover_interpreter
def test_discover_interpreter():

    from ansible.module_utils.common._collections_compat import MutableMapping, MutableSequence

    class FakeAction(object):
        def __init__(self, result_dict=None, exc_info=None, stderr=None, warnings=None):
            self._low_level_execute_command_result_dict = result_dict
            self._low_level_execute_command_exc_info = exc_info
            self._low_level_execute_command_stderr = stderr
            self._discovery_warnings = warnings

        def _low_level_execute_command(self, **kwargs):
            return self._low_level_execute_command_result_dict


# Generated at 2022-06-12 21:35:42.307593
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # The following test cases are so that we get code coverage to 100%.
    # The actual functionality is tested in functional tests.
    task_vars = dict()
    action = dict()
    action_result = dict()
    action_result['stdout'] = u'''PLATFORM
Linux
FOUND

ENDFOUND'''
    action['_low_level_execute_command'] = lambda a, b: action_result
    action['_discovery_warnings'] = []

    action['_connection'] = dict()
    action['_connection']['has_pipelining'] = False

    try:
        discover_interpreter(action, u'python', u'auto_legacy_silent', task_vars)
    except Exception as e:
        print(e)
        assert False


# Generated at 2022-06-12 21:35:52.648311
# Unit test for function discover_interpreter
def test_discover_interpreter():

    initial_task_vars = dict(
        ansible_distribution=None,
    )

    # Python interpreter discovery not supported for other interpreters
    try:
        discover_interpreter('', '', '', initial_task_vars)
        assert False
    except ValueError:
        assert True

    # Test discovery for python interpreter
    initial_task_vars['ansible_distribution'] = 'Debian'
    initial_task_vars['ansible_distribution_version'] = '8.7'

    # Test for discovery mode of auto_legacy_silent
    python_path = discover_interpreter('', 'python', 'auto_legacy_silent', initial_task_vars)
    assert python_path == '/usr/bin/python'

# Generated at 2022-06-12 21:36:03.625274
# Unit test for function discover_interpreter
def test_discover_interpreter():
    class FakeAction:
        def __init__(self):
            self.connection = FakeConnection()
            self.become_method = ''
            self.become_username = ''
            self.become_password = ''
            self.become_exe = ''
            self.become_flags = ''
            self.become_info = ''
            self.become_allow_executable = None
            self.become_pass = ''
            self.deprecated = ''
            # Hack for coverage
            self._low_level_execute_command = lambda *args, **kwargs: {}

        def _discovery_warnings(self):
            return []

    class FakeConnection:
        def __init__(self):
            self.has_pipelining = True
            self.become = True


# Generated at 2022-06-12 21:36:13.952391
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # This test is only supported on platforms with /bin/sh as /bin/sh

    hosts = ['localhost']
    action = BashAction(task_vars={'inventory_hostname': hosts[0]})
    action.module_name = 'shell'
    action.task = dict(action='shell')
    # Fake the low level execute
    action._low_level_execute_command = lambda command, sudoable, in_data=None, executable=None: {
        'stdout': '/usr/bin/python\n',
        'stderr': 'stderr'
    }
    result = discover_interpreter(action, interpreter_name='python', discovery_mode='auto_silent', task_vars={})
    assert(result == u'/usr/bin/python')


# Generated at 2022-06-12 21:36:25.228116
# Unit test for function discover_interpreter
def test_discover_interpreter():
    res = discover_interpreter(None, 'python', 'auto', None)
    assert res == u'/usr/bin/python'

    res = discover_interpreter(None, 'python3', 'auto', None)
    assert res == u'/usr/bin/python3'

    res = discover_interpreter(None, 'python', 'auto_legacy', None)
    assert res == u'/usr/bin/python'

    res = discover_interpreter(None, 'python3', 'auto_legacy', None)
    assert res == u'/usr/bin/python3'

    res = discover_interpreter(None, 'python', 'auto_legacy_silent', None)
    assert res == u'/usr/bin/python'


# Generated at 2022-06-12 21:36:28.350897
# Unit test for function discover_interpreter
def test_discover_interpreter():
    """

    :return:
    """
    task_vars = {}
    interpreter_name = 'python'
    discovery_mode = 'auto_legacy'
    pass # TODO: Implement test case


# Generated at 2022-06-12 21:36:38.325890
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.plugins.action import ActionBase
    import sys

    class TestAction(ActionBase):
        def run(self, tmp=None, task_vars=None):
            if task_vars is None:
                task_vars = dict()

            # Return ok for now, the fail case is tested by test_discovery_fails
            return dict(
                changed=False,
                ansible_facts=dict(ansible_python=discover_interpreter(self, 'python', 'auto_silent', task_vars))
            )

    # Test that the method returns None if we call it without self
    if discover_interpreter('python', 'auto_silent', dict()) is not None:
        raise AssertionError("Method discover_interpreter should return None if it is called without self")

    # Test

# Generated at 2022-06-12 21:36:39.398648
# Unit test for function discover_interpreter
def test_discover_interpreter():
    raise NotImplementedError("Unit test not implemented for discover_interpreter")

# Generated at 2022-06-12 21:37:04.879335
# Unit test for function discover_interpreter
def test_discover_interpreter():
    test_result = discover_interpreter(None, 'python', 'auto_legacy', {})
    assert test_result == u'/usr/bin/python'
    #TODO: Add test for the Linux case.

# Generated at 2022-06-12 21:37:12.816851
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.module_utils.facts.system.distribution import DistributionFactCollector

    obj = DistributionFactCollector()
    facts_dict = obj.collect(None, None)

    task_vars = {
        'inventory_hostname': 'testhost',
        'ansible_facts': facts_dict,
        '_ansible_no_log': False,
        '_ansible_verbosity': 2
    }

    # For the test, disable interpreter discovery
    C.config.set_config_value('INTERPRETER_PYTHON_DISCOVERY_MODE', 'off', variables=task_vars)

    class MockActionModule(object):
        def __init__(self, *args, **kwargs):
            self._connection = MockConnection()
            self._discovery_warnings = []


# Generated at 2022-06-12 21:37:14.834438
# Unit test for function discover_interpreter
def test_discover_interpreter():
    assert discover_interpreter('action', 'python', 'auto', dict()) == u'/usr/bin/python'

# Generated at 2022-06-12 21:37:17.642183
# Unit test for function discover_interpreter
def test_discover_interpreter():
    dsppath = discover_interpreter(None, 'python', 'auto', None)
    print(dsppath)

if __name__ == '__main__':
    test_discover_interpreter()

# Generated at 2022-06-12 21:37:23.826197
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # Test basic case where we have a python interpreter we can use
    task_vars = {'inventory_hostname': 'localhost', 'ansible_python_interpreter': '/usr/bin/python',
                 'is_python_interpreter_discovery': True,
                 'is_python_interpreter_discovery_silent': False,
                 'is_python_interpreter_discovery_auto': True,
                 'is_python_interpreter_discovery_legacy': False}
    python_interpreter = discover_interpreter(task_vars)
    assert python_interpreter == "/usr/bin/python"

    # Test that we do not mess up on unknown values

# Generated at 2022-06-12 21:37:32.371985
# Unit test for function discover_interpreter
def test_discover_interpreter():
    try:
        import ansible.executor.action_plugins.command as command
        from ansible.executor.task_queue_manager import TaskQueueManager
        from ansible.parsing.dataloader import DataLoader
        from ansible.vars.manager import VariableManager
        from ansible.inventory.manager import InventoryManager
        from ansible.playbook.play import Play
        from ansible.executor.playbook_executor import PlaybookExecutor
    except ImportError:
        # skip test on Windows
        return

    class TestConnection(object):
        def __init__(self, has_pipelining=True):
            self._has_pipelining = has_pipelining

        def has_pipelining(self):
            return self._has_pipelining


# Generated at 2022-06-12 21:37:38.862170
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.facts import decorate_module_utils_facts
    from ansible.module_utils.facts.system.distribution import Distribution
    from ansible.module_utils.facts.system.distribution import get_distribution
    from ansible.module_utils.facts.system.distribution import get_distribution_version
    from ansible.module_utils.facts.system.distribution import get_distribution_release
    from ansible.module_utils.facts.system.distribution import get_linux_distribution
    from ansible.module_utils.facts.system.distribution import get_sunos_version
    from ansible.module_utils.facts.system.distribution import get_sunos_kernel_version

# Generated at 2022-06-12 21:37:49.474534
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # This system actually has python 2.6 installed but /usr/bin/python is a symlink to /usr/bin/python2.4
    task_vars = {'ansible_python_interpreter': u'/usr/bin/python3.6', 'inventory_hostname': u'test host'}

    # fallback discovery
    action = dict()

# Generated at 2022-06-12 21:38:01.431902
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible import constants as C

    # Test cases below are:
    #
    # Test case [0] = "use_interpreter" boolean,
    # Test case [1] = expected value of "use_interpreter" in the context,
    # Test case [2] = "interpreter" string,
    # Test case [3] = expected value of "interpreter" in the context
    # Test case [4] = "discovery_mode" string,
    # Test case [5] = expected "discovery_mode" in the context,
    # Test case [6] = "python" string,
    # Test case [7] = "platform_python_map" dictionary
    # Test case [8] = "bootstrap_python_list" list
    # Test case [9] = "shell_bootstrap" string,

# Generated at 2022-06-12 21:38:03.386539
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # TODO: flesh out this unit test
    assert discover_interpreter(None, 'python') == u'/usr/bin/python'

# Generated at 2022-06-12 21:38:55.725722
# Unit test for function discover_interpreter
def test_discover_interpreter():
    
    action = ActionModule(connection='', play_context=None, loader=None, templar=None, shared_loader_obj=None)
    task_vars = dict()
    
    # Test for distro fedora
    # Expected to return the interpreter /usr/bin/python
    platform_python_map = {'fedora': {'20':'/usr/bin/python', '28':'/usr/bin/python2', '29':'/usr/bin/python3'}}
    discovery_mode = 'auto'
    interpreter_name = 'python'

# Generated at 2022-06-12 21:38:58.439721
# Unit test for function discover_interpreter
def test_discover_interpreter():
    test_result = discover_interpreter('action', 'python', 'auto_silent', 'task_vars')
    assert test_result is None, 'Function discover_interpreter is not working properly'

# Generated at 2022-06-12 21:39:08.701008
# Unit test for function discover_interpreter
def test_discover_interpreter():
    import os
    import random
    import string
    import tempfile
    from ansible.plugins.action import ActionBase

    # Create a random string we'll use for our temporary directory to work in
    rand_str = ''.join(random.choice(string.ascii_lowercase) for _ in range(10))
    temp_dir = tempfile.gettempdir()

    # Create the temporary directory
    temp_path = os.path.join(temp_dir, rand_str)
    os.mkdir(temp_path)

    # Create the interpreter_python_distro_map for Debian

# Generated at 2022-06-12 21:39:17.331670
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.plugins.action import ActionBase
    action = ActionBase()
    task_vars = {}

    # Test 1: only python interpreters
    action._connection = DummyConnection(has_pipelining=True, bootstrap_python_list=['/usr/bin/python', '/usr/local/python', '/usr/local/bin/python'],
                                         platform_type='linux', distro='redhat', version='6.7',
                                         return_interpreter=True)
    result = discover_interpreter(action, 'python', 'auto', task_vars)
    assert result == '/usr/bin/python'

    # Test 2: only python interpreters, but remote python not found

# Generated at 2022-06-12 21:39:27.854540
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.plugins.action import ActionBase
    from ansible.parsing.dataloader import DataLoader

    class TestAction(ActionBase):
        def __init__(self):
            self._connection = None
            self._play_context = None
            self._loader = DataLoader()
            self._templar = None
            self._task = None
            self.task_vars = {}

        @staticmethod
        def _low_level_execute_command(cmd, sudoable=True, in_data=None, executable=None):
            pass

    action = TestAction()

    # Should return /usr/bin/python with no exception
    try:
        discover_interpreter(action, 'python', 'auto', {})
    except Exception as e:
        assert False, e

    # Should throw exception with bad interpreter

# Generated at 2022-06-12 21:39:35.017273
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # Testing case of discover_interpreter for happy path of platform linux
    discovered_interpreter = discover_interpreter("action", "python", "auto_legacy_silent", {"inventory_hostname": "localhost"})
    assert discovered_interpreter == "/usr/bin/python"

    # Testing case of discover_interpreter for when platform is not linux and it returns NotImplementedError
    try:
        discover_interpreter("action", "python", "auto_legacy_silent", {"inventory_hostname": "notlinuxhost"})
    except NotImplementedError as e:
        assert "unsupported platform" in str(e)

    # Testing case of discover_interpreter to check if it returns 'None' when cannot find platform

# Generated at 2022-06-12 21:39:45.272027
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.plugins.action import ActionBase

    action = ActionBase()

    class DummyConnection:
        def __init__(self):
            self.has_pipelining = True

    conn = DummyConnection()

    action._connection = conn

    platform_python_map = {
        'debian': {
            '7': '/usr/bin/python',
            '8': '/usr/bin/python',
        },
    }


# Generated at 2022-06-12 21:39:50.954126
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # FUTURE: add tests for failures/warnings/etc.
    assert discover_interpreter(None, 'python', 'auto', {}) == u'/usr/bin/python'
    assert discover_interpreter(None, 'python', 'auto_legacy', {}) == u'/usr/bin/python'
    assert discover_interpreter(None, 'python', 'auto_silent', {}) == u'/usr/bin/python'
    assert discover_interpreter(None, 'python', 'auto_legacy_silent', {}) == u'/usr/bin/python'

# Generated at 2022-06-12 21:40:02.196880
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.module_utils.six import StringIO

    from units.mock.connection import Connection
    from ansible.module_utils.common.network import NetworkError

    task_vars = dict()
    conn = None
    action = None

    # results to return from execute
    results = {}