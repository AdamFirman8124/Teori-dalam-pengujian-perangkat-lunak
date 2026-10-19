

# Generated at 2022-06-12 21:30:18.693681
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.playbook.task_include import TaskInclude
    class MockAction(object):
        def __init__(self):
            self._discovery_warnings = []
            self._connection = MockConnection()
            self._task = TaskInclude()
            self._task_vars = dict()
        def _low_level_execute_command(self, args, sudoable=False, in_data=None):
            if args.startswith(u'command -v '):
                return { u'stdout' : u'/usr/bin/python' }
            elif args == u'/usr/bin/python':
                return { u'stdout' : u'{"platform_dist_result": ["redhat", "7.3", "Maipo"]}' }
            return { u'stdout' : u'' }


# Generated at 2022-06-12 21:30:25.703675
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.plugins.loader import action_loader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    inv_obj = InventoryManager(loader=loader, sources=['localhost,'])
    var_manager = VariableManager(loader=loader, inventory=inv_obj)

    action = action_loader.get('shell', task=dict(), connection='local')
    action.Runner = action.get_runner()

    action._shared_loader_obj = loader
    action._task = {}
    action._task_vars = {}
    action._connection = None
    action._low_level_execute_command = lambda cmd, sudoable=None, in_data=None: {'stdout': cmd}

# Generated at 2022-06-12 21:30:36.090474
# Unit test for function discover_interpreter
def test_discover_interpreter():

    interpreter_name = u'python'
    host = u'localhost'
    action = None
    discovery_mode = u'auto_legacy_silent'

# Generated at 2022-06-12 21:30:46.327381
# Unit test for function discover_interpreter
def test_discover_interpreter():
    '''
    Unit test for ansible.module_utils.interpreter_discovery.discover_interpreter()
    '''

    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils import interpreter_discovery
    from ansible.module_utils.compat import ipaddress

    # define a fake ansible.module_utils.connection.Connection class to mock '_low_level_execute_command'
    class mock_Connection:
        def __init__(self):
            self.saved_stdout = ''
            self.failed = False
            self.exc = None
            return

        @property
        def has_pipelining(self):
            return True


# Generated at 2022-06-12 21:30:57.383846
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.executor.task_executor import TaskExecutor

    class FakeAction(object):
        def __init__(self):
            self._connection = lambda: None
            self._connection.has_pipelining = True
            self._discovery_warnings = []

        def _low_level_execute_command(self, cmd, sudoable=False, in_data=None):
            class Result(object):
                def __init__(self, stdout, stderr):
                    self.stdout = stdout
                    self.stderr = stderr

            if cmd == '/usr/bin/python -c import platform;import json;print(json.dumps(platform.dist()))':
                return Result('(["", "", ""],)', '')

# Generated at 2022-06-12 21:31:06.285686
# Unit test for function discover_interpreter
def test_discover_interpreter():
    def _low_level_execute_command(cmd, sudoable, in_data=None):
        if cmd == 'echo FOUND; command -v \'python\'; echo ENDFOUND':
            return {'stdout': u'FOUND\r\n/usr/bin/python\r\nENDFOUND'}

        elif cmd == '/usr/bin/python':
            return {'stdout': u'{"platform_dist_result": ["redhat", "7.4", "Maipo"]}\n'}


# Generated at 2022-06-12 21:31:15.129326
# Unit test for function discover_interpreter
def test_discover_interpreter():
    class Task:
        def __init__(self, action, host_vars):
            self.action = action
            self.host_vars = host_vars

    class HostVar:
        def __init__(self, version=None, vstring=None, platform_type=None):
            self.version = version
            self.vstring = vstring
            self.platform_type = platform_type

    class Action:
        def __init__(self, result, conn, host_vars=None, name=None, discovery_warnings=None, interpreter_name=None,
                     discovery_mode=None):
            self.host_vars = host_vars
            self.conn = conn
            self.result = result
            self.name = name
            self.discovery_warnings = discovery_warnings

# Generated at 2022-06-12 21:31:25.681907
# Unit test for function discover_interpreter
def test_discover_interpreter():
    import os
    import ansible
    import string
    import random

    def randomword(length):
        return ''.join(random.choice(string.lowercase) for i in range(length))

    # Create a temporary test directory
    test_dir = '%s/test_dir' % os.getenv('PWD')

    if os.path.exists(test_dir):
        os.system('rm -rf %s' % test_dir)

    # copy the directory test/units/modules to the temporary test directory
    from ansible.utils.path import makedirs_safe
    makedirs_safe(test_dir)
    os.system('cp -r ../../test/units/modules %s' % test_dir)

    # Add the test directory to the module_utils paths in ansible.cfg
    # This

# Generated at 2022-06-12 21:31:38.511286
# Unit test for function discover_interpreter
def test_discover_interpreter():
   from ansible.executor import task_executor
   from ansible.module_utils.common.collections import ImmutableDict
   from ansible.plugins.action import ActionBase
   from ansible.vars.hostvars import HostVars
   hostvars = HostVars(host_vars=dict(inventory_hostname='localhost', ansible_connection='local'))
   mock_task_executor = task_executor.TaskExecutor(task_vars=ImmutableDict({'localhost': hostvars, 'vars': {}}))
   mock_task_executor._tqm = task_executor.TaskQueueManager(inventory={'localhost': hostvars})
   mock_task_executor._play = dict()
   mock_task_executor._play['connection'] = 'local'
   mock_task

# Generated at 2022-06-12 21:31:47.527586
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.executor.task_result import TaskResult
    from ansible.executor.action_result import HostActionResult
    from ansible.plugins.action.normal import ActionModule

    mock_action = ActionModule(display=display, task_vars={'ansible_python_interpreter': '/usr/bin/python'})
    mock_action._connection = type('MockConnection', (object,), {})
    mock_action._connection.has_pipelining = False
    mock_action._low_level_execute_command = lambda c, sudoable, in_data=None: {'stdout': c}

    mock_action._task_result = TaskResult('mock_task', HostActionResult('mock_host'))

# Generated at 2022-06-12 21:31:58.814778
# Unit test for function discover_interpreter
def test_discover_interpreter():
    error_msg = ""
    try:
        discover_interpreter(action, interpreter_name, discovery_mode, task_vars)
    except Exception as e:
        error_msg = str(e)
    return error_msg

# Generated at 2022-06-12 21:32:10.466970
# Unit test for function discover_interpreter
def test_discover_interpreter():
    assert 'python2.7' == discover_interpreter(None, 'python2', 'auto', dict(
        ansible_python_interpreter='',
        ansible_python_interpreter_discovery_mode='auto',
    ))
    assert 'python2.6' == discover_interpreter(None, 'python2', 'auto', dict(
        ansible_python_interpreter='',
        ansible_python_interpreter_discovery_mode='auto',
    ))
    assert 'python2' == discover_interpreter(None, 'python2', 'auto', dict(
        ansible_python_interpreter='',
        ansible_python_interpreter_discovery_mode='auto',
    ))

# Generated at 2022-06-12 21:32:22.375200
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # multiple Linux distros with exact matches, past and present
    class MockAction(object):
        pass

    ACTION = MockAction()
    ACTION._discovery_warnings = []

    class MockConnection(object):
        pass

    CONNECTION = MockConnection()


# Generated at 2022-06-12 21:32:31.077419
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # File name is the test name
    test_file_name = inspect.stack()[0][3]
    test_file = open('/tmp/' + test_file_name + '.txt', 'w')
    test_file.write('Beginning unit test for function discover_interpreter...' + '\n')
    test_file.close()

    # Create an interpreter action for the test
    test_action = ActionModule(task=dict(), connection=None, play_context=PlayContext(), loader=None, templar=None, shared_loader_obj=None)

    # Test 1: Test the case of an unsupported interpreter.
    test_action._discovery_warnings = []
    test_interpreter_name = 'foo'
    test_discovery_mode = 'auto_legacy_silent'
    test_task_

# Generated at 2022-06-12 21:32:42.732873
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.plugins.action.normal import ActionModule as _ActionModule
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.utils.connection import Connection
    from ansible.vars import VariableManager

    class ActionModule(_ActionModule):
        def _low_level_execute_command(
                self, cmd, sudoable=True, in_data=None, executable=C.DEFAULT_EXECUTABLE,
                stdin=None, stdout=None, stderr=None,
                use_unsafe_shell=False, encoding=None):
            return {'stdout': cmd}


# Generated at 2022-06-12 21:32:51.768524
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # NOTE: these tests use a local var for the module since the module is not patched when the tests run and we want
    # to be able to bypass the 'unsupported python version' check for testing purposes.
    # TODO: fix this to use the module itself
    from ansible.module_utils.interpreter_discovery import discover_interpreter
    from ansible.plugins.action import ActionBase
    from ansible.executor.task_result import TaskResult
    from ansible.executor.process.worker import WorkerProcess

    class TestAction(ActionBase):
        def _execute_module(self, module_name=None, module_args=None, task_vars=None, wrap_async=None):
            assert module_name == 'setup'

# Generated at 2022-06-12 21:33:04.372381
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.plugins.action.normal import ActionModule
    from ansible.module_utils.connection import Connection
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play

    class FakeOptions(object):
        def __init__(self, **kwargs):
            for key, value in kwargs.items():
                setattr(self, key, value)

    class FakeArgs(object):
        def __init__(self, **kwargs):
            for key, value in kwargs.items():
                setattr(self, key, value)


# Generated at 2022-06-12 21:33:12.212460
# Unit test for function discover_interpreter
def test_discover_interpreter():
    InterpreterMock = type('Mock', (object,), dict())

    class TestAction(InterpreterMock):
        def __init__(self):
            self._discovery_warnings = []
            self._connection = InterpreterMock()
            self._connection.has_pipelining = False

        def _low_level_execute_command(self, command, sudoable=False, in_data=None):
            pass

    class TestTaskVars(InterpreterMock):
        def __init__(self):
            self.inventory_hostname = InterpreterMock()

    # test simple interpreter discovery with uname-based discovery
    task_vars = TestTaskVars()
    task_vars.inventory_hostname.lower = lambda: 'linux'
    action = TestAction()
    res = discover

# Generated at 2022-06-12 21:33:23.290298
# Unit test for function discover_interpreter
def test_discover_interpreter():
    """ Testing discover_interpreter()"""

    class Action:
        """
        Mock class to create objects that mimic the Action class
        """
        def __init__(self):
            self._discovery_warnings = ['Dummy warning']
            self._low_level_execute_command = ['Dummy command']

    class Connection:
        """
        Mock class to create objects that mimic the Connection class
        """
        def __init__(self, has_pipelining=False):
            self.has_pipelining = has_pipelining

    class TaskVars:
        """
        Mock class to create objects that mimic the TaskVars class
        """
        def __init__(self):
            self._task_vars = {'inventory_hostname': 'dummy_host'}


# Generated at 2022-06-12 21:33:33.390648
# Unit test for function discover_interpreter
def test_discover_interpreter():
    import ansible.executor.discovery.python

    hostA = 'foo.example.org'
    hostB = 'bar.example.org'
    hostC = 'baz.example.org'
    hostD = 'qux.example.org'

    actionA = _InterpreterDiscoveryTestAction()
    actionB = _InterpreterDiscoveryTestAction(failed_list=[u'/usr/bin/python'])
    actionC = _InterpreterDiscoveryTestAction()


# Generated at 2022-06-12 21:33:52.455501
# Unit test for function discover_interpreter
def test_discover_interpreter():
    import ansible.plugins.action as action
    import ansible.plugins.loader as loader

    action_plugins = loader.ActionModuleLoader().all()
    action_plugins['script'] = action.ActionModule(connection=None)
    action_plugins['raw'] = action.ActionModule(connection=None)

    discover_interpreter(action_plugins['raw'], 'python', 'auto', {'inventory_hostname': 'test_host'})


if __name__ == '__main__':
    # simple unit test when running this module directly
    test_discover_interpreter()

# Generated at 2022-06-12 21:34:03.217919
# Unit test for function discover_interpreter

# Generated at 2022-06-12 21:34:12.729356
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # test for an unsupported interpreter type
    class ActionTest:
        _connection = None
        _discovery_warnings = []

        def _low_level_execute_command(self, cmd, sudoable=False, in_data=None):
            # return some arbitrary result
            return dict(stdout='some arbitrary result from low_level_execute_command')

    action = ActionTest()
    task_vars = dict(inventory_hostname='test_host',
                     connection='local',
                     ansible_connection='local')
    interpreter = 'python2'
    discovery_mode = 'auto'
    # test for an unsupported interpreter type

# Generated at 2022-06-12 21:34:21.675303
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # most stuff gets tested in unit/executor/discovery/test_python_interpreter_discovery.py
    assert to_native(_version_fuzzy_match('1.0', {'1.0': '/usr/bin/python', '1.1': '/usr/bin/python3'})) == '/usr/bin/python'
    assert to_native(_version_fuzzy_match('1.1', {'1.0': '/usr/bin/python', '1.1': '/usr/bin/python3'})) == '/usr/bin/python3'
    assert to_native(_version_fuzzy_match('1.2', {'1.0': '/usr/bin/python', '1.1': '/usr/bin/python3'})) == '/usr/bin/python3'
    assert to_

# Generated at 2022-06-12 21:34:28.880576
# Unit test for function discover_interpreter
def test_discover_interpreter():
    try:
        import tabulate
    except ImportError:
        print("Import error of tabulate. Please install the tabulate using 'pip install tabulate'")
        return False

    from ansible.plugins.action import ActionBase

    class TestAction(ActionBase):
        def run(self, tmp=None, task_vars=None):
            results = {}
            if task_vars is None:
                task_vars = dict()

            for host in task_vars.get("hosts", []):
                result = task_vars.get("_result")
                if result.get('changed', False):
                    results['changed'] = True
                    results['msg'] = "changed"
                else:
                    results['failed'] = True
                    results['msg'] = "failed"
            return results

    test_action = TestAction

# Generated at 2022-06-12 21:34:41.287090
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.module_utils import basic

    # due to https://github.com/ansible/ansible/issues/38126, we can't use action_plugins
    # for this testing; we'll have to mock the action object instead
    class TestAction(object):
        def __init__(self):
            self._discovery_warnings = []

        def _low_level_execute_command(self, command, **kwargs):
            res = basic.execute_command(self, command, **kwargs)
            res['stdout'] = to_bytes(res['stdout'], encoding='utf-8')
            res['stdout_lines'] = res['stdout'].splitlines()
            res['stderr'] = to_bytes(res['stderr'], encoding='utf-8')

# Generated at 2022-06-12 21:34:50.221932
# Unit test for function discover_interpreter
def test_discover_interpreter():
    """Test discover_interpreter function"""

    # test_interpreter_discovery
    task_vars = {'ansible_python_interpreter': '/usr/bin/python', 'ansible_host': '127.0.0.1'}
    action = None
    interpreter_name = 'python'
    discovery_mode = 'auto'

    # TODO: test cases for different discovery config values, different distro output
    res = discover_interpreter(action, interpreter_name, discovery_mode, task_vars)
    if res == u'/usr/bin/python' or res == '/usr/bin/python':
        return True
    else:
        return False


# Generated at 2022-06-12 21:34:59.754014
# Unit test for function discover_interpreter
def test_discover_interpreter():
    action = None
    try:
        results = discover_interpreter(action, 'python', 'explicit', {})
    except Exception as e:
        raise AssertionError('discover_interpreter explicit mode should not fail')

    if results is None:
        raise AssertionError('discover_interpreter explicit mode should not have a null result')

    results = discover_interpreter(action, 'python3', 'explicit', {})

    if results is not None:
        raise AssertionError('discover_interpreter explicit mode should have a null result for an invalid name')

    try:
        results = discover_interpreter(action, 'python', 'mock_mode', {})
    except Exception as e:
        raise AssertionError('discover_interpreter mock mode should not fail')


# Generated at 2022-06-12 21:35:05.902233
# Unit test for function discover_interpreter
def test_discover_interpreter():
    import ansible.executor.task_result
    import ansible.executor.task_executor
    import ansible.executor.module_common
    from ansible.executor.module_common import get_platform_subclass, PlatformBase
    from ansible.plugins.loader import action_loader

    class FakePlatformLinux(PlatformBase):
        # override abstract methods
        def platform_version(self):
            return '2.2.2'

        def platform_dist_version(self):
            return '3.3.3'

        def _platform_dist_full_version(self, use_dict=False):
            return '3.3.3'

        def which(self, binary):
            return 'test_binary'


# Generated at 2022-06-12 21:35:08.765444
# Unit test for function discover_interpreter
def test_discover_interpreter():
    res = discover_interpreter(None, 'python', 'auto_legacy', dict())
    assert res == '/usr/bin/python'



# Generated at 2022-06-12 21:35:28.845782
# Unit test for function discover_interpreter
def test_discover_interpreter():
    import pytest


# Generated at 2022-06-12 21:35:41.044067
# Unit test for function discover_interpreter
def test_discover_interpreter():

    from ansible.module_utils.facts.virtual import Virtual, virtuals
    from ansible.module_utils.facts import default_collectors

    # create a legacy module_utils path
    # TODO: move this to a shared fixture module?
    import sys
    import os
    if 'module_utils' not in sys.path:
        sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'module_utils'))

    # TODO: create a mock connection that supports pipelining and has all the interpreter paths

    # FIXME: these aren't valid task_vars, and this would never work, but it compiles for now

# Generated at 2022-06-12 21:35:51.953080
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # Fake task_vars
    task_vars = dict()
    # Fake action
    class Action:
        _connection = None
        _tqm = None
        _play = None
        _loader = None
        _ds = None
        _task = None
        _play_context = None
        _job = None
        _task = None
        _discovery_warnings = []
    action = Action()
    # Add fake low_level_execute_command

# Generated at 2022-06-12 21:36:02.989709
# Unit test for function discover_interpreter
def test_discover_interpreter():
    import mock
    from ansible.module_utils.common.text.converters import json
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.module_utils.six.moves import StringIO
    from ansible.executor.module_common import _load_params
    from ansible.parsing.plugin_docs import read_docstring
    import ansible.module_utils.compat.version

    payload = _load_params(StringIO(u"ansible_python_interpreter=/usr/bin/python"))
    result = discover_interpreter(mock.MagicMock(), u'python', u'auto', mock.MagicMock())
    assert result == u'/usr/bin/python'


# Generated at 2022-06-12 21:36:13.260300
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # Test 1
    # Test when interpreter is python and discovery_mode is auto_silent, exception is thrown
    dummy_action = {'foo': 'bar'}
    try:
        discover_interpreter(
            action=dummy_action,
            interpreter_name='python',
            discovery_mode='auto_silent',
            task_vars={}
        )
        assert False, "Expected exception not thrown"
    except InterpreterDiscoveryRequiredError as e:
        # Verify exception fields are correct
        assert e.interpreter_name == 'python'
        assert e.discovery_mode == 'auto_silent'

    # Test 2
    # Test when interpreter is not python, exception is thrown

# Generated at 2022-06-12 21:36:17.742904
# Unit test for function discover_interpreter
def test_discover_interpreter():
    class FakeAction(object):
        def _low_level_execute_command(self, command, in_data=None, sudoable=False):
            return {'stdout': "PLATFORM\nLinux\nFOUND\n/usr/bin/python\nENDFOUND"}

    assert discover_interpreter(FakeAction(), 'python', 'auto', {}) == "/usr/bin/python"

# Generated at 2022-06-12 21:36:29.106900
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # get test data
    test_data = list(pkgutil.iter_modules(['ansible/test/unit/executor/data/interpreter_discovery']))

    for loader, mod_name, ispkg in test_data:
        # import module
        test = loader.find_module(mod_name).load_module(mod_name)
        # get test data
        # test.data is a list of tuples:
        # (
        #   test_name, platform_type, os_release_info, target_python, bootstrap_python_list,
        #   expected_interpreter, expected_warnings
        # )
        for data in test.data:
            # get test values
            test_name, platform_type, os_release_info, target_python, bootstrap_python_list, \
               

# Generated at 2022-06-12 21:36:38.937830
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # Test python version matching
    version = '2.7.5'
    version_map = {
        '2.7.2': '/usr/bin/python2.7.2',
        '2.7.5': '/usr/bin/python2.7.5',
        '3.4.9': '/usr/bin/python3.4.9',
        '3.6.3': '/usr/bin/python3.6.3'
    }
    result = _version_fuzzy_match(version, version_map)
    assert result == '/usr/bin/python2.7.5'

    version = '2.7.6'
    result = _version_fuzzy_match(version, version_map)
    assert result == '/usr/bin/python2.7.5'


# Generated at 2022-06-12 21:36:44.423280
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.module_utils.basic import AnsibleModule

    action = AnsibleModule(argument_spec={}, supports_check_mode=True)
    action._ansible_version = 2.8

    # test case: default (silent, non-legacy)
    res = discover_interpreter(action, interpreter_name='python', discovery_mode='default', task_vars={})
    assert res == u'/usr/bin/python', 'expected /usr/bin/python, got "{0}"'.format(res)
    assert not action._discovery_warnings, 'expected no warnings, got {0}'.format(action._discovery_warnings)

    # test case: legacy
    res = discover_interpreter(action, interpreter_name='python', discovery_mode='auto_legacy', task_vars={})

# Generated at 2022-06-12 21:36:54.028260
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # set up dummy action and task vars
    class FakeAction:
        def __init__(self):
            self._discovery_warnings = []

        def _low_level_execute_command(self, cmd, sudoable=False, in_data=None):
            if cmd == "command -v 'python3'":
                return {'stdout': '/usr/bin/python3', 'stderr': '', 'rc': 0}


# Generated at 2022-06-12 21:37:11.789288
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.plugins.action.discovery import ActionModule as DiscoveryAction
    from ansible.plugins.action.script import ActionModule as ScriptAction
    from ansible.plugins.action.raw import ActionModule as RawAction
    from ansible.plugins.action.setup import ActionModule as SetupAction
    from ansible.plugins.connection.local import Connection as ConnectionLocal
    from ansible.plugins.connection.ssh import Connection as ConnectionSsh
    from ansible.plugins.loader import action_loader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from units.mock.procenv import swap_stdin_and_argv

    action_list = [DiscoveryAction, ScriptAction, RawAction, SetupAction]
    conn_list = [ConnectionLocal, ConnectionSsh]

    basedir = os

# Generated at 2022-06-12 21:37:20.540945
# Unit test for function discover_interpreter
def test_discover_interpreter():
    """
    unit test function tests discover_interpreter

    :param self: Unit test object
    :return: None
    """

    action = object()
    interpreter = 'python'
    task_vars = {}

    # Test host discovery with the default discovery_mode
    try:
        test_res = discover_interpreter(action, interpreter, 'auto', task_vars)
        assert False
    except NotImplementedError:
        pass

    # Test host discovery with the 'auto_legacy' discovery_mode that supports the legacy behavior
    try:
        test_res = discover_interpreter(action, interpreter, 'auto_legacy', task_vars)
        assert test_res == u'/usr/bin/python'
    except NotImplementedError:
        pass

    # Test host discovery with the 'auto_

# Generated at 2022-06-12 21:37:29.148726
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.executor import action_write_locks

    action = action_write_locks.ActionModule(connection=None,
                                             play_context=None,
                                             new_stdin=None,
                                             loader=None,
                                             templar=None,
                                             shared_loader_obj=None)
    task_vars = {
        'inventory_hostname': 'localhost',
        'ansible_connection': 'local',
        'ansible_python_interpreter': '/usr/bin/python'
    }

    result = discover_interpreter(action, 'python', 'auto', task_vars)
    assert result == '/usr/bin/python'

# Generated at 2022-06-12 21:37:31.022263
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # FUTURE: test against a wider variety of host-side Python versions/configurations/etc
    # FUTURE: more coverage?
    assert True

# Generated at 2022-06-12 21:37:37.937830
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.executor.task_result import TaskResult
    from ansible.executor.action_result import ActionResult

    action = ActionResult('test', {}, {}, {}, {})
    task = TaskResult('test', {}, {}, None, action)
    task.host = 'localhost'
    task.task_vars = dict()
    task.task_vars['ansible_python_interpreter'] = ''
    action.task_result = task

    # Test case 1: no interpreter found (possible on exotica)
    # The interpreter warnings are suppressed because this is run in automated tests. The warning would be logged
    # in production.

# Generated at 2022-06-12 21:37:48.179211
# Unit test for function discover_interpreter
def test_discover_interpreter():

    import control
    import lookup_plugins
    import test.utils.module_runner
    import test.utils.remote_cache

    action = test.utils.module_runner.ModuleRunner()

    action.set_fake_execute(control.execute)
    action.set_fake_loader(lookup_plugins)
    action.set_fake_provider(test.utils.remote_cache.get)

    task_vars = dict()
    task_vars['ansible_facts'] = dict()

    # TODO: use the supported_interps module to determine interpreter name,
    # or remove support for non-python interpreters in test runner
    # interpreter_name = 'python'

    # TODO: add a separate test for _version_fuzzy_match

    # list of tuples: discovery_mode, expected_interp, expected_

# Generated at 2022-06-12 21:38:00.468089
# Unit test for function discover_interpreter
def test_discover_interpreter():
    platform_python_map = {
        'amzn': {
            '2.0.0': '/usr/bin/python27',
            '2.1.0': '/usr/bin/python27',
            '2.2.0': '/usr/bin/python27',
            '2.3.0': '/usr/bin/python27',
            '2.4.0': '/usr/bin/python27',
            '2.5.0': '/usr/bin/python27',
            '2.6.0': '/usr/bin/python27',
            '2.7.0': '/usr/bin/python27',
        },
        'centos': {
            '7': '/usr/bin/python2',
        },
    }


# Generated at 2022-06-12 21:38:08.825867
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.executor.discovery import InterpreterDiscoveryRequiredError
    from ansible.plugins.action.raw import ActionModule as RawActionModule

    import unittest

    class TestInterpreterDiscoveryRequiredError(unittest.TestCase):
        def test_interpreter_discovery_required_error(self):
            error = InterpreterDiscoveryRequiredError("Test", "test", "test")
            self.assertEqual(repr(error), "Test")

    class TestRawActionModule(RawActionModule):
        def _low_level_execute_command(self, cmd, sudoable=False, in_data=None, executable=None):
            res = dict(rc=0, stdout="", stderr="")


# Generated at 2022-06-12 21:38:14.500308
# Unit test for function discover_interpreter
def test_discover_interpreter():
    task_vars = {}
    action = None
    interpreter_name = None
    discovery_mode = None
    # successful test
    interpreter_name = 'python'
    discovery_mode = 'smart'
    result = discover_interpreter(action, interpreter_name, discovery_mode, task_vars)
    assert result is not None
    # use pipe-lining
    action = True
    result = discover_interpreter(action, interpreter_name, discovery_mode, task_vars)
    assert result is not None


# Generated at 2022-06-12 21:38:24.584253
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.executor.discovery_test import TestActionModule
    
    # Test for proper interperter discovery on macOS
    real_action = TestActionModule('/bin/command', 'system', 'freebsd', '/bin/command -v python', 'system', 'darwin', '')
    action = TestActionModule('/bin/command', 'system', 'freebsd', '/bin/command -v python', 'system', 'darwin', '')
    task_vars = {
    'ansible_python_interpreter': '/bin/python',
    'ansible_python_version': None
    }
    discover_interpreter(action, 'python', 'auto_legacy_silent', task_vars)
    assert action != real_action

# Generated at 2022-06-12 21:38:48.456918
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # discover_interpreter('', 'python', 'auto_legacy_silent', {})
    assert discover_interpreter('', 'python', 'auto_legacy_silent', {}) == u"/usr/bin/python"

# Generated at 2022-06-12 21:38:55.030442
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # Init
    action = None
    task_vars = {}

    # Test discover_interpreter
    discover_interpreter(action, 'python', 'auto', task_vars)
    discover_interpreter(action, 'python', 'auto_silent', task_vars)
    discover_interpreter(action, 'python', 'auto_legacy', task_vars)
    discover_interpreter(action, 'python', 'auto_legacy_silent', task_vars)

# Generated at 2022-06-12 21:38:56.276516
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # Can't import the module due to a circular dependency
    pass

# Generated at 2022-06-12 21:39:06.434780
# Unit test for function discover_interpreter
def test_discover_interpreter():
    import tempfile
    tmpdir = tempfile.mkdtemp()
    tmpfile = '/'.join((tmpdir, 'testfile'))

# Generated at 2022-06-12 21:39:10.820369
# Unit test for function discover_interpreter
def test_discover_interpreter():
    action = None
    interpreter_name = 'python'
    discovery_mode = 'explicit'
    task_vars = dict()
    task_vars['inventory_hostname'] = 'localhost'

    result = discover_interpreter(action, interpreter_name, discovery_mode, task_vars)
    print(result)

# Generated at 2022-06-12 21:39:18.798603
# Unit test for function discover_interpreter
def test_discover_interpreter():
    import unittest

    class TestInterpreterDiscovery(unittest.TestCase):

        """
        Minimal test case for interpreter discovery
        """

        def setUp(self):
            # stub class to be able to pass the test case
            # In real use the interpreter discovery is called
            # on the action plugin
            class StubAction():
                def __init__(self):
                    self._discovery_warnings = []

            self.stub_action = StubAction()

        def test_discover_interpreter_fails_on_unsupported_interpreter(self):
            with self.assertRaises(ValueError):
                discover_interpreter(self.stub_action,
                                     'notSupported', 'auto_legacy_silent', {})


# Generated at 2022-06-12 21:39:28.763526
# Unit test for function discover_interpreter
def test_discover_interpreter():
    class mockAction(object):
        def __init__(self):
            self.discovery_warnings = []
            self._low_level_execute_command = lambda x, y, z: {'stdout': 'foo'}
            self._connection = mockConnection()
            self.name = u'testaction'
            self.async_val = 0

    class mockConnection(object):
        def __init__(self):
            self.has_pipelining = True

    action = mockAction()
    task_vars = dict(
        ansible_python_interpreter='/usr/bin/python'
    )

    # Test - discovery mode disabled
    result = discover_interpreter(action, 'python', 'auto', task_vars)
    assert result == "/usr/bin/python"

    # Test - discovery

# Generated at 2022-06-12 21:39:35.489825
# Unit test for function discover_interpreter
def test_discover_interpreter():
    class action:
        def __init__(self):
            class connection:
                def __init__(self):
                    self.pipelining = True

            self._connection = connection()
            self._discovery_warnings = []

        @staticmethod
        def _low_level_execute_command(command, sudoable=False, in_data=None):
            #TEST1
            if command == 'command -v \'python3.6\'':
                return {'stdout': u'/usr/bin/python3.6\n'}
            #TEST2
            if command == 'command -v \'python3.5\'':
                return {'stdout': u'/usr/bin/python3.5\n'}
            #TEST3

# Generated at 2022-06-12 21:39:45.691741
# Unit test for function discover_interpreter
def test_discover_interpreter():
    import unittest
    import pickle
    from ansible.parsing.yaml.objects import AnsibleMapping
    from ansible.playbook.play_context import PlayContext

    class TestAction(object):
        def __init__(self, connection, task_vars=None):
            self._connection = connection
            self._task_vars = task_vars
            self._discovery_warnings = []

        # pylint: disable=no-self-use

# Generated at 2022-06-12 21:39:55.998887
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.plugins.action import ActionBase
    action = ActionBase()
    host = 'localhost'

    #Test for the cases found when a host does not have the bootstrap pythons installed
    action._discovery_warnings = []
    res = discover_interpreter(action, 'python', 'auto_legacy_silent', dict())
    assert res == '/usr/bin/python'
    assert action._discovery_warnings == ['No python interpreters found for host localhost (tried /usr/bin/python3, '
                                          '/usr/bin/python2.7, /usr/bin/python2.6, /usr/bin/python2, '
                                          '/usr/bin/python)']

    #Test for the cases when a host does not have the bootstrap pythons and the default fallback is not