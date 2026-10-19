

# Generated at 2022-06-12 21:30:16.955091
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.module_utils.basic import AnsibleModule

    display.verbosity = 3
    task_vars = dict()
    action = AnsibleModule(argument_spec=dict())

    # Test a simple case where the platform is supported and /usr/bin/python is found
    task_vars['inventory_hostname'] = 'test'
    task_vars['_python_interpreter_discovery_mode'] = 'auto_legacy_silent'
    action._discovery_warnings = list()
    action._low_level_execute_command = lambda x, in_data=None, sudoable=False, **kwargs: {'stdout': 'PLATFORM\nLinux\nFOUND\n/usr/bin/python\nENDFOUND'}


# Generated at 2022-06-12 21:30:26.272270
# Unit test for function discover_interpreter

# Generated at 2022-06-12 21:30:36.876478
# Unit test for function discover_interpreter
def test_discover_interpreter():
    class ModuleTest(object):
        def __init__(self):
            self.params = dict()
            self.check_mode = False
            self.connection = 'local'
            self.no_log = False
            self.become = False
            self.become_method = None
            self.become_user = None

        def _low_level_execute_command(self, cmd, sudoable=False, in_data=None):
            print(u'Attempting to execute: {0}'.format(cmd))
            return dict(stdout=u'uname -s: {0}'.format(cmd))

    class ActionTest(object):
        def __init__(self, interpreter_name, task_vars):
            self._task_vars = task_vars
            self._module = ModuleTest()
            self

# Generated at 2022-06-12 21:30:46.327288
# Unit test for function discover_interpreter
def test_discover_interpreter():
    try:
        import platform
    except ImportError:
        pass

    interpreter_name = 'python'
    discovery_mode = 'auto'
    action = MockAutomaticInterpreter_action("c:\\test.yml")
    action._connection.has_pipelining = True
    task_vars = {'inventory_hostname': 'target', 'ansible_python_interpreter': '/test/test'}
    result = discover_interpreter(action, interpreter_name, discovery_mode, task_vars)

    # The result will be different on each machine
    assert result == '/test/test' or result == '/usr/bin/python' or result == platform.python_implementation()

# Mock object for unit test

# Generated at 2022-06-12 21:30:51.241169
# Unit test for function discover_interpreter
def test_discover_interpreter():
    result = discover_interpreter(None, 'python', 'auto_legacy_silent', {})
    assert result == u'/usr/bin/python'

    result = discover_interpreter(None, 'python', 'auto_silent', {})
    assert result == u'/usr/bin/python'

# Generated at 2022-06-12 21:31:00.459996
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # test_discovery_interpreter test cases array
    test_cases = tuple()

    # test case arrays
    uname_no_python = ('uname', u'', u'', None, None)
    # (return code, stdout, stderr, distro, version, interpreter, warnings)
    platform_checks = {}
    platform_checks[u'python_target.py output - no distro, no version'] = (
        0, u'{}', u'', None, None, u'/usr/bin/python', [],
    )
    platform_checks[u'python_target.py output - no version'] = (
        0, u'{"platform_dist_result": ["redhat", "", ""]}', u'', u'redhat', None, u'/usr/bin/python', [],
    )

# Generated at 2022-06-12 21:31:07.617750
# Unit test for function discover_interpreter
def test_discover_interpreter():
    import ansible.executor.module_common

    action = ansible.executor.module_common.ActionModule(None, None, None, None)

    task_vars_dict = {'ansible_python_interpreter': 'python2'}

    task_vars = ansible.vars.VariableManager(loader=None)._init_vars_module()
    task_vars.update(task_vars_dict)

    for discovery_mode in ('auto','auto_silent', 'auto_legacy', 'auto_legacy_silent'):
        action._discovery_warnings = []
        print("discovery_mode: %s" % discovery_mode)

# Generated at 2022-06-12 21:31:18.631433
# Unit test for function discover_interpreter
def test_discover_interpreter():

    c = {
        'inventory_hostname': 'test',
        'vars': {
            'ansible_python_interpreter': '/usr/bin/python'
        }
    }

    test_interpreter = discover_interpreter(action=None, interpreter_name='python', discovery_mode='auto',
                                            task_vars=c)
    # test_interpreter should be found by the shell command command -v 'python' and the first result returned
    assert test_interpreter == '/usr/bin/python'

    # test that an interpreter name other than 'python' raises a ValueError

# Generated at 2022-06-12 21:31:27.768160
# Unit test for function discover_interpreter
def test_discover_interpreter():
    import tempfile
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.plugins.loader import module_loader
    from ansible.executor.process.result import ResultProcessor
    from ansible.plugins.callback import CallbackBase

    # this is not a real test, just a quick way to manually test the function.
    # TODO: actual unit test

    # test action (with stdin support as a quick workaround for missing pipelining)

# Generated at 2022-06-12 21:31:40.224581
# Unit test for function discover_interpreter
def test_discover_interpreter():
    import json

    import pytest

    from ansible.module_utils.common._collections_compat import Sequence

    from ansible.module_utils.common.removed import removed
    from ansible.module_utils.parsing.convert_bool import boolean


# Generated at 2022-06-12 21:32:00.515155
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.executor.task_queue_manager import TaskQueueManager
    import os
    import tempfile
    import pytest
    import sys

    # This test class is based off of ansible.executor.task_queue_manager.TaskQueueManager

    # Create our temporary directory, and chdir to it
    cwd = os.getcwd()
    temp_dir = tempfile.mkdtemp()
    os.chdir(temp_dir)

    # Create our temp ansible.cfg

# Generated at 2022-06-12 21:32:13.233971
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # imports needed for unit tests
    from ansible.parsing.vault import VaultLib
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.handler_task_include import HandlerTaskInclude
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.plugins.loader import action_loader

    # generic results to stub calls to low-level execute_command
    generic_results = dict(stdout=u'', stderr=u'', rc=0, start=0.0, end=0.0, delta=0)

    # function for use in mocking the low_level_execute_command method

# Generated at 2022-06-12 21:32:24.672457
# Unit test for function discover_interpreter
def test_discover_interpreter():

    def _simple_execute_command(cmd, sudoable=None, in_data=None):
        # We need to do this so that we can mock a return value
        class FakeResponse:
            def __init__(self, stdout, stderr):
                self['stdout'] = stdout
                self['stderr'] = stderr
        if cmd == 'echo PLATFORM; uname; echo FOUND; command -v python; echo ENDFOUND':
            return FakeResponse('PLATFORM\nlinux\nFOUND\n/usr/bin/python2.7\nENDFOUND\n', '')

# Generated at 2022-06-12 21:32:25.206147
# Unit test for function discover_interpreter
def test_discover_interpreter():
    pass

# Generated at 2022-06-12 21:32:36.741257
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # InterpreterDiscoveryRequiredError is raised when no interpreter is found and discovery mode is not silent
    try:
        result = discover_interpreter('', 'python', 'auto', {})
        assert False, 'Expected an exception'
    except InterpreterDiscoveryRequiredError as e:
        assert e.interpreter_name == 'python'
        assert e.discovery_mode == 'auto'

    # InterpreterDiscoveryRequiredError is not raised when no interpreter is found and discovery mode is silent
    try:
        result = discover_interpreter('', 'python', 'auto_silent', {})
        assert result is None
    except InterpreterDiscoveryRequiredError as e:
        assert False, 'Expected no exception'

    # InterpreterDiscoveryRequiredError is not raised when the python version is found

# Generated at 2022-06-12 21:32:39.495018
# Unit test for function discover_interpreter
def test_discover_interpreter():
    d = discover_interpreter(None, 'python', 'auto_legacy', None)
    assert d == u'/usr/bin/python'

# Generated at 2022-06-12 21:32:44.769461
# Unit test for function discover_interpreter
def test_discover_interpreter():
    task_vars = dict(
        ansible_facts=dict(
            ansible_python_interpreter="",
            ansible_python_version={}
        )
    )

    def _noop_action(self, *args, **kwargs):
        # operates on self._low_level_execute_command
        return args[0]
    discover_interpreter(_noop_action, 'python', 'auto_legacy_silent', task_vars)

# Generated at 2022-06-12 21:32:53.443187
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.executor.task_result import TaskResult
    from ansible.plugins.action import ActionBase
    from ansible import context

    class TestAction(ActionBase):
        def run(self, tmp=None, task_vars=None):
            return TaskResult(host=self._play_context.remote_addr,
                              return_data=dict(changed=False),
                              task_fields=dict(action='test'))

    # Test 1 - Test that discover_interpreter looks up the correct value
    task_vars = dict(version='1.2.3', inventory_hostname='host')
    context._init_global_context(None)

    context.CLIARGS = lambda: None

# Generated at 2022-06-12 21:33:06.114318
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.playbook import PlayContext
    from ansible.plugins import module_loader
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    class MockAction(object):

        def __init__(self):
            self._discovery_warnings = []

        def _low_level_execute_command(self, command, sudoable=None, in_data=None):
            return dict(stdout='')

    class MockHost(object):

        def __init__(self, name, type):
            self.name = name
            self.host_type = type

    class MockConnection(object):

        def __init__(self, type):
            self.has_pipelining = type


# Generated at 2022-06-12 21:33:13.277031
# Unit test for function discover_interpreter
def test_discover_interpreter():
    assert discover_interpreter(None, interpreter_name='python', discovery_mode='auto_legacy_silent', task_vars={
        'inventory_hostname': 'testhost',
        'config': {
            'DEFAULT': {
                'interpreter_python_distro_map': {
                    'centos': {
                        '7.4': '/usr/bin/python2.7'
                    }
                }
            }
        }
    }) == u'/usr/bin/python'


# Generated at 2022-06-12 21:33:41.556227
# Unit test for function discover_interpreter
def test_discover_interpreter():
    task_vars = {}
    #setup task
    class FakeAction(object):
        def __init__(self):
            self._discovery_warnings = []

        def _low_level_execute_command(self, command, sudoable, in_data=u''):
            if command.startswith('python'):
                return dict(stdout=pkgutil.get_data('ansible.executor.discovery', 'os-release.json'))
            else:
                if in_data:
                    return dict(stdout=u'{0} /usr/bin/python'.format(command))
                else:
                    return dict(stdout=u'PLATFORM\nLinux\nFOUND\n/usr/bin/python\nENDFOUND')


# Generated at 2022-06-12 21:33:53.676858
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.module_utils import basic
    from ansible.plugins.action import ActionBase
    action = ActionBase()
    action._supports_async = False
    # For use of _low_level_execute_command
    action._low_level_execute_command = basic._low_level_execute_command
    action._connection = basic.Connection()

    res = discover_interpreter(action, 'python', 'auto', dict())
    assert res == u'/usr/bin/python'

    res = discover_interpreter(action, 'python', 'auto_legacy', dict())
    assert res == u'/usr/bin/python'

    res = discover_interpreter(action, 'python', 'auto_silent', dict())
    assert res == u'/usr/bin/python'

    res = discover_interpreter

# Generated at 2022-06-12 21:34:05.153011
# Unit test for function discover_interpreter
def test_discover_interpreter():

    osreleasetxt = '''NAME="Fedora"
VERSION="26 (Twenty Six)"
ID=fedora
VERSION_ID=26
'''

    host = 'foo.example.com'
    interpreter_name = 'python'
    discovery_mode = 'auto_legacy_silent'
    task_vars = {}

    from ansible.executor.discovery import discover_interpreter


# Generated at 2022-06-12 21:34:14.709084
# Unit test for function discover_interpreter
def test_discover_interpreter():
    task_vars = dict(
        ansible_connection='local',
        ansible_python_interpreter='/usr/bin/python'
    )

    action = None
    try:
        from ansible.plugins.action.script import ActionModule as ScriptActionModule
        action = ScriptActionModule(task=None, connection=None, play_context=None, loader=None, templar=None,
                                    shared_loader_obj=None)
    except:
        pass

    def execute_command(cmd, sudoable=False, in_data=None):
        if cmd.count(' ') == 0:
            command = cmd
        else:
            command = cmd.split(' ', 1)[0]


# Generated at 2022-06-12 21:34:15.328890
# Unit test for function discover_interpreter
def test_discover_interpreter():
    assert True

# Generated at 2022-06-12 21:34:24.036326
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.executor.task_executor import TaskExecutor
    from ansible.executor.play import Play
    from ansible.executor.playbook_executor import PlaybookExecutor

    class _TaskExecutor(TaskExecutor):
        def __init__(self, host, task, task_vars, play_context):
            self._host = host
            self._task = task
            self._task_vars = task_vars.copy()
            self._play_context = play_context.copy()

            self._low_level_execute_command = _low_level_execute_command


# Generated at 2022-06-12 21:34:33.637715
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # Mock module action
    action = type('Action', (), {})
    action._connection = type('Connection', (), {'has_pipelining': True})
    action._discovery_warnings = []

    # Mock function _low_level_execute_command
    def _low_level_execute_command(command, sudoable=False, in_data=None):
        res = type('Response', (), {'get': lambda *args: ''})
        if command == 'command -v \'python3\'':
            return res()
        if command == 'command -v \'python\'':
            return res()
        if command == 'command -v \'python2\'':
            return res()

# Generated at 2022-06-12 21:34:44.387332
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.module_utils.discovery.interpreter import (
        discover_interpreter,
        InterpreterDiscoveryRequiredError,
    )

    def _fail(msg):
        raise AssertionError(msg)


# Generated at 2022-06-12 21:34:54.870834
# Unit test for function discover_interpreter
def test_discover_interpreter():

    from ansible.module_utils.common._collections_compat import Mapping

    class MockActionModule(object):
        def __init__(self):
            self._connection = MockConnection()
            self._discovery_warnings = []

    class MockConnection(object):
        def __init__(self):
            self.has_pipelining = True

        def _low_level_execute_command(self, cmd, in_data=None, sudoable=False):
            if cmd == 'echo PLATFORM; uname; echo FOUND; command -v \'python\'; echo ENDFOUND':
                return dict(stdout='PLATFORM\nLinux\nFOUND\n/usr/bin/python\nENDFOUND',
                            stderr='', rc=0)

# Generated at 2022-06-12 21:35:02.989163
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.executor.action_factory import ActionFactory
    from ansible.plugins.action.python_interpreter import ActionModule as PythonInterpreterAction
    from ansible.plugins.action.setup import ActionModule as SetupAction
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.vars import combine_vars

    setup_action = SetupAction(
        task=dict(action=dict(module=u'setup')),
        connection=dict(host=None),
        play_context=dict(become=False, become_user=None),
        loader=DataLoader(),
        templar=None,
        shared_loader_obj=None
    )

    action

# Generated at 2022-06-12 21:35:54.948588
# Unit test for function discover_interpreter
def test_discover_interpreter():
    class MockAction(object):
        pass

    class MockTaskVars(object):
        pass

    task_vars = MockTaskVars()
    task_vars.inventory_hostname = 'localhost'

    maction = MockAction()
    maction._discovery_warnings = []
    maction._connection = MockConnection()
    maction._low_level_execute_command = low_level_execute_command

    assert discover_interpreter(maction, 'python', 'auto', task_vars) == u'/usr/bin/python'
    assert discover_interpreter(maction, 'python', 'auto', task_vars) == u'/usr/bin/python'
    assert discover_interpreter(maction, 'python', 'auto', task_vars) == u'/usr/bin/python'

# Generated at 2022-06-12 21:36:05.894081
# Unit test for function discover_interpreter
def test_discover_interpreter():
    def test_discovery(host, discovery_mode, platform, version_map, version,
                       expected_result, expected_warnings):
        class MockAction(object):
            connection = MockConnection(supports_pipelining=True)

            def _low_level_execute_command(self, command, sudoable=False, in_data=None):
                self._llc_called = command, sudoable, in_data
                return {'stdout': self._llc_return}

            _llc_called = None
            _discovery_warnings = []

        class MockConnection(object):
            def __init__(self, supports_pipelining=False):
                self.has_pipelining = supports_pipelining

        class MockDisplay(object):
            def __init__(self):
                self._msgs = []

# Generated at 2022-06-12 21:36:13.378229
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.plugins.action import ActionBase


# Generated at 2022-06-12 21:36:24.128711
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # Test for case of python
    assert discover_interpreter(action=None, interpreter_name='python', discovery_mode='auto_legacy',
                                task_vars={}) == u'/usr/bin/python'

    # Test for case of python not equal to python
    try:
        discover_interpreter(action=None, interpreter_name='python1', discovery_mode='auto_legacy',
                             task_vars={})
    except ValueError:
        assert True
    else:
        assert False

    # Test for case of unsupported platform
    try:
        discover_interpreter(action=None, interpreter_name='python', discovery_mode='auto_legacy',
                             task_vars={})
    except NotImplementedError:
        assert True
    else:
        assert False

    # Test for

# Generated at 2022-06-12 21:36:30.566933
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # test basic parsing of command output
    test_command_output = "PLATFORM\nLinux\nFOUND\n/usr/bin/python\nENDFOUND"
    got = discover_interpreter("", "", "", {'inventory_hostname': ''}, test_command_output)
    assert got == '/usr/bin/python'

if __name__ == '__main__':
    test_discover_interpreter()

# Generated at 2022-06-12 21:36:39.635416
# Unit test for function discover_interpreter
def test_discover_interpreter():

    '''
    This is a testing function for ansible.executor.discovery.discover_interpreter()
    '''

    from ansible.module_utils._text import to_bytes

    # Test id 1:
    # Test interpreter_name, not only 'python'
    # But, in this test, only 'python' is supported

    print ('[*] Test id 1: test interpreter_name, not only python')
    interpreter_name_list = ['python', 'python3']
    for interpreter_name in interpreter_name_list:
        test_success = 0
        try:
            discover_interpreter('any action', interpreter_name, 'auto', 'any task_vars')
            print ('[-] Failed to test interpreter_name: {}'.format(interpreter_name))
        except ValueError:
            test_

# Generated at 2022-06-12 21:36:44.949155
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.executor.task_result import TaskResult


# Generated at 2022-06-12 21:36:54.396052
# Unit test for function discover_interpreter
def test_discover_interpreter():
    class TestAction(object):
        def __init__(self):
            self._discovery_warnings = []

        def _low_level_execute_command(self, cmd, in_data=None, sudoable=False):
            return {'stdout': "PLATFORM\nLinux\nFOUND\n/usr/bin/python\nENDFOUND", 'stderr': None}

    class TestTaskVars(object):
        def get(self, name, default):
            return default

    action = TestAction()
    task_vars = TestTaskVars()

    assert discover_interpreter(action, 'python', 'auto', task_vars) == '/usr/bin/python'
    assert len(action._discovery_warnings) == 1

# Generated at 2022-06-12 21:36:56.377676
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.executor.discovery import discover_interpreter

    # Test not yet implemented
    return True

# Generated at 2022-06-12 21:37:06.414993
# Unit test for function discover_interpreter
def test_discover_interpreter():
    fake_action = object()
    fake_action._low_level_execute_command = lambda command, sudoable, in_data: {
        'stdout': u"PLATFORM\nLinux\nFOUND\n/usr/bin/python\nENDFOUND\n",
        'stderr': u'',
    }
    fake_action._connection = object()
    fake_action._connection.has_pipelining = True

    # test known-working discovery mode

# Generated at 2022-06-12 21:39:02.732406
# Unit test for function discover_interpreter
def test_discover_interpreter():
    interp = discover_interpreter('', 'python', 'auto')
    print(interp)
    #assert interp == '/usr/bin/python'

# Generated at 2022-06-12 21:39:12.676319
# Unit test for function discover_interpreter
def test_discover_interpreter():
    import pytest
    from ansible.module_utils.six.moves import StringIO
    from ansible.utils.display import Display
    from ansible.module_utils.distro import LinuxDistribution

    class FakeDisplay(object):
        def __init__(self):
            self.stdout = StringIO()
            self.stderr = StringIO()

        def __getattr__(self, name):
            return getattr(self.stdout, name)

    pytest.importorskip("OpenSSL")
    display = Display()
    display._display = FakeDisplay()
    interpreter_name = 'python'
    discovery_mode = 'auto'
    task_vars = {}
    fake_connection = FakeConnection()

# Generated at 2022-06-12 21:39:16.378843
# Unit test for function discover_interpreter
def test_discover_interpreter():
    action = None
    interpreter_name = 'python'
    discovery_mode = 'auto_legacy_silent'
    task_vars = dict(INVENTORY_HOSTNAME='host',
                     INTERPRETER_PYTHON_DISTRO_MAP={},
                     INTERPRETER_PYTHON_FALLBACK=[])

    assert discover_interpreter(action, interpreter_name,
                                discovery_mode, task_vars) == u'/usr/bin/python'

# Generated at 2022-06-12 21:39:24.420983
# Unit test for function discover_interpreter
def test_discover_interpreter():
    test_action = "test action"
    test_interpreter = "test interpreter"
    test_discovery_mode = "test discovery mode"
    test_task_vars = "test task vars"

    # setup display
    class Display:
        verbosity = 0

    display.verbosity = Display.verbosity
    display.verbosity = 1

    print(discover_interpreter(test_action, test_interpreter, test_discovery_mode, test_task_vars))

# Generated at 2022-06-12 21:39:32.977095
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.play_context import PlayContext
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.plugins.loader import connection_loader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.executor.playbook_executor import PlaybookExecutor

    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.inventory.source import Source

    from ansible.parsing.dataloader import DataLoader

    from ansible.vars.hostvars import HostVars
    from ansible.vars.manager import VariableManager


# Generated at 2022-06-12 21:39:43.902725
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.executor.action_write_cache import ActionModule as ActionWriteCache
    from ansible.plugins.action.script import ActionModule as ActionScript
    from ansible.plugins.action.shell import ActionModule as ActionShell
    from ansible.plugins.action.copy import ActionModule as ActionCopy

    interpreter_name = 'python'
    discovery_mode = 'explicit'
    # TODO: add a unit test task_vars fixture
    task_vars = {}

    action_modules = (ActionWriteCache, ActionScript, ActionShell, ActionCopy)


# Generated at 2022-06-12 21:39:51.702932
# Unit test for function discover_interpreter
def test_discover_interpreter():

    class ActionModule(object):
        pass

    action = ActionModule()
    action.task_vars = dict()
    action.task_vars['ansible_python_interpreter'] = '/usr/bin/python'
    action._connection = object()

    action._connection.has_pipelining = True

    def __init__(self, in_data=''):
        self.in_data = in_data
        self.cmd = '/bin/usr/python --version'
        self.sudoable = False

    def __str__(self):
        return '<LocalCommand cmd="%s">' % self.cmd

    action._low_level_execute_command = lambda self, cmd, sudoable=True, in_data=u'': __init__(self, in_data=in_data)


# Generated at 2022-06-12 21:40:03.040501
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.executor.task_executor import TaskExecutor
    from ansible.executor.process.worker import ConnectionWorkerProcess
    from ansible.module_utils.connection import Connection

    conn = Connection('local')
    conn_worker = ConnectionWorkerProcess(conn)
    action = TaskExecutor(None, 'test', None, None, conn_worker)

    task_vars = dict()
    interpreter_name = 'python'
    discovery_mode = 'auto'

    assert discover_interpreter(action, interpreter_name, discovery_mode, task_vars) == '/usr/bin/python'

    discovery_mode = 'auto_legacy'

    assert discover_interpreter(action, interpreter_name, discovery_mode, task_vars) == '/usr/bin/python'
