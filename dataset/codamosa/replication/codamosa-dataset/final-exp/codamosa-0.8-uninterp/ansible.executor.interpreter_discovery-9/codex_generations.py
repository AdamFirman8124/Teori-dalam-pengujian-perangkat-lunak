

# Generated at 2022-06-12 21:30:18.426887
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins.action import ActionBase
    from ansible.executor.task_result import TaskResult

    class TestAction(ActionBase):
        def run(self, tmp=None, task_vars=None):
            return TaskResult(host=self._task.host, return_data={'stdout': 'PLATFORM\nx86_64\nFOUND\n/usr/bin/python\nENDFOUND'})

    action = TestAction(task=None, connection=None, play_context=PlayContext(), loader=None, templar=None, shared_loader_obj=None)
    assert discover_interpreter(action, u'python', u'auto', task_vars={}) == '/usr/bin/python'
    assert action._discovery

# Generated at 2022-06-12 21:30:25.220401
# Unit test for function discover_interpreter
def test_discover_interpreter():
    import unittest
    from ansible.module_utils.basic import AnsibleModule
    import ansible.executor.discovery

    mock_action = unittest.mock.Mock()
    mock_action._connection = unittest.mock.Mock()

    # Test python interpreter discovery
    test_host_name = 'test_host'
    test_vars = {'inventory_hostname': test_host_name}

    # Python interpreter discovery with discovery mode 'auto'
    # Test Success
    # Test with unsupported platform type
    # Test with a not implemented error
    # Test with unexpected output
    # Test with python interpreter not found
    # Test with a missing python interpreter
    # Test with pipelining support not available

    # Python interpreter discovery with discovery mode 'auto_legacy'
    # Test Success
    # Test

# Generated at 2022-06-12 21:30:35.132117
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # This is not a full test. It is just a way to ensure that we do not break the
    # existing code. When python interpreter discovery gets more stable,
    # we can more fully test this function.

    # nc6 and amazon linux reports uname as linux
    result_linux = discover_interpreter(None, 'python', 'auto_legacy', {'inventory_hostname': 'nc6'})
    assert result_linux == u'/usr/bin/python'

    # debian 9 reports uname as linux
    result_linux = discover_interpreter(None, 'python', 'auto_legacy', {'inventory_hostname': 'deb9'})
    assert result_linux == u'/usr/bin/python'
    # old version of debian 8 reports uname as linux

# Generated at 2022-06-12 21:30:43.146549
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.module_utils.common.collections import ImmutableDict
    import sys

    if sys.version_info < (2, 7):
        import unittest2 as unittest
    else:
        import unittest

    class FakeActionModule(object):
        def __init__(self, task_vars=None, warnings=None, **kwargs):
            self._connection = ImmutableDict(has_pipelining=True)
            self._discovery_warnings = warnings

            if task_vars is None:
                self.task_vars = ImmutableDict()
            else:
                self.task_vars = ImmutableDict(task_vars)


# Generated at 2022-06-12 21:30:49.263193
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.executor.task_result import TaskResult
    from ansible.executor.task_executor import TaskExecutor
    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.playbook.block import Block
    from ansible.playbook.role import Role
    from ansible.plugins.loader import interpreter_loader

    play_context = PlayContext()
    play_context.network_os = 'network_os'

# Generated at 2022-06-12 21:30:59.604570
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.executor.task_result import TaskResult

    class TestAction:
        def __init__(self, displays, expected_warnings):
            self._display = displays
            self.results = []
            self._discovery_warnings = []
            self._expected_warnings = expected_warnings

        def _add_result(self, result):
            self.results.append(result)

        def _get_result(self):
            return self.results.pop()

        def _log_warn(self, msg):
            self._discovery_warnings.append(msg)

        def _assert_no_warnings(self):
            assert len(self._discovery_warnings) == len(self._expected_warnings)

# Generated at 2022-06-12 21:31:05.651985
# Unit test for function discover_interpreter
def test_discover_interpreter():
    discover_interpreter_result = discover_interpreter(object(), 'python', 'auto_legacy_silent', {})
    discover_interpreter_result_expected = u'/usr/bin/python'
    assert discover_interpreter_result == discover_interpreter_result_expected, \
        "discover_interpreter returns '%s' instead of expected '%s'" % (discover_interpreter_result,
                                                                        discover_interpreter_result_expected)

# Generated at 2022-06-12 21:31:14.748962
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.playbook.task import Task
    from ansible.plugins.action import ActionBase
    from ansible.inventory.host import Host
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    hostvars = {"inventory_hostname": 'testhost'}
    variable_manager = VariableManager()
    variable_manager.set_host_variable(Host('testhost'), hostvars)
    variable_manager.set_inventory(InventoryManager(loader=loader, sources=[]))
    variable_manager._extra_vars = {"ansible_python_interpreter": None}

    task = Task()
    task.action = 'setup'
    task.args = {}
    task_

# Generated at 2022-06-12 21:31:25.399238
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from . import action
    from . import action_plugins

    class FakeAction(action.ActionBase):
        def _execute_module(self, *args, **kwargs):
            return {}

        def _low_level_execute_command(self, cmd, in_data=None, sudoable=False, executable='/bin/sh',
                                       su=None, su_user=None, become_user=None):
            return {'stdout': cmd, 'stderr': '', 'rc': 0, 'stdin': None}

    class FakeConnection(object):
        def __init__(self, has_pipelining=None):
            if has_pipelining:
                self.has_pipelining = has_pipelining
            else:
                self.has_pipelining = has_pipelining


# Generated at 2022-06-12 21:31:38.231364
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.module_utils.facts.system.distribution import Distribution
    import copy
    import sys

    class NullAction(object):
        def __init__(self):
            self._discovery_warnings = []

        def _low_level_execute_command(self, command, sudoable=True, in_data=None):
            if command.strip() == "command -v '/usr/bin/python'":
                return {'rc': 0, 'stdout': "/usr/bin/python\r\n"}
            elif command.strip() == "command -v '/usr/bin/python3'":
                return {'rc': 0, 'stdout': "/usr/bin/python3\r\n"}

# Generated at 2022-06-12 21:31:58.914983
# Unit test for function discover_interpreter
def test_discover_interpreter():
    import copy
    import os
    import unittest
    import sys
    import tempfile
    import ansible_collections.ansible.community.plugins.module_utils.discovery as _mod_discovery
    import ansible.module_utils.basic as _module_utils_basic

    # TODO: better unit test data


# Generated at 2022-06-12 21:32:10.679475
# Unit test for function discover_interpreter
def test_discover_interpreter():
    test_action = object()
    test_action. _connection = object()
    test_action._connection.has_pipelining = True

    test_action._low_level_execute_command = lambda x: {'stdout': 'PLATFORM\r\nLinux\r\nFOUND\r\n/usr/bin/python\r\n'
                                                                 '/usr/bin/python3\r\nENDFOUND'}
    test_action._discovery_warnings = []

    test_task_vars = dict()
    test_task_vars['inventory_hostname'] = 'test_host'

    assert discover_interpreter(test_action, 'python', 'auto', test_task_vars) == '/usr/bin/python'

# Generated at 2022-06-12 21:32:22.557092
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # used in unit test
    class FakeDir(object):
        def __init__(self, dirc=None):
            self.dirc = dirc

        def get_config_value(self, key, variables=None, convert_to=None, default=None):
            '''
            There is no other way to patch module level functions
            '''
            if self.dirc == constants.INTERPRETER_PYTHON_DISTRO_MAP:
                return _get_interpreter_python_distro_map()

            elif self.dirc == constants.INTERPRETER_PYTHON_FALLBACK:
                return _get_interpreter_python_fallback()

    # used in unit test
    class FakeAction(object):
        def __init__(self):
            self.connection = FakeConnection()


# Generated at 2022-06-12 21:32:31.642335
# Unit test for function discover_interpreter
def test_discover_interpreter():
    test_action = object()
    test_action.sudoable = False
    test_action._low_level_execute_command = lambda x, sudoable, in_data=None: {'stdout':''}
    test_action._discovery_warnings = []
    test_action._connection = object()
    test_action._connection.has_pipelining = True
    test_task_vars = dict()

    test_task_vars['inventory_hostname'] = 'localhost'

    test_task_vars['__config_module__'] = dict()
    test_task_vars['__config_module__']['INTERPRETER_PYTHON_FALLBACK'] = '/usr/bin/python2.7'

# Generated at 2022-06-12 21:32:43.089648
# Unit test for function discover_interpreter

# Generated at 2022-06-12 21:32:49.940305
# Unit test for function discover_interpreter
def test_discover_interpreter():
    import sys, os
    sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..'))
    from ansible.executor.discovery import discover_interpreter

    task_vars = dict()
    action = dict()
    interpreter_name = 'python'
    discovery_mode = 'auto_legacy_silent'

    discover_interpreter(action, interpreter_name, discovery_mode, task_vars)


if __name__ == '__main__':
    test_discover_interpreter()

# Generated at 2022-06-12 21:33:01.048445
# Unit test for function discover_interpreter
def test_discover_interpreter():
    #from ansible_collections.notstdlib.moveitallout.plugins.module_utils.common.interpreters import python_discovery

    #FUTURE: this just a placeholder, and will fail without a fixture installed
    def get_versioned_doclink(doc):
        return "http://example.com/interpreter_discovery.html"

    # TODO: do this?
    class ActionModule:
        def __init__(self):
            self._discovery_warnings = []

        def _low_level_execute_command(self, command):
            pass


# Generated at 2022-06-12 21:33:10.457473
# Unit test for function discover_interpreter
def test_discover_interpreter():
    import pytest, re
    from ansible.module_utils.six import PY2


# Generated at 2022-06-12 21:33:14.257304
# Unit test for function discover_interpreter
def test_discover_interpreter():
    assert discover_interpreter(None, 'python', 'auto_silent', {}) == u'/usr/bin/python'
    assert discover_interpreter(None, 'python', 'auto_legacy_silent', {}) == u'/usr/bin/python'

# Generated at 2022-06-12 21:33:16.387493
# Unit test for function discover_interpreter
def test_discover_interpreter():
    assert discover_interpreter(None, 'python', 'auto_legacy_silent', None) == '/usr/bin/python'

# Generated at 2022-06-12 21:33:48.891907
# Unit test for function discover_interpreter

# Generated at 2022-06-12 21:33:57.871385
# Unit test for function discover_interpreter
def test_discover_interpreter():
    import sys
    import pytest
    sys.modules['ansible.plugins'] = {}
    sys.modules['ansible.module_utils.basic'] = {}

    task_vars = {'inventory_hostname': 'foo', 'ansible_interpreter_python': '/usr/bin/python3'}
    return_value = discover_interpreter(ansible_action=None, interpreter_name='python', discovery_mode='auto', task_vars=task_vars)
    assert return_value == '/usr/bin/python3'

    with pytest.raises(InterpreterDiscoveryRequiredError):
        discover_interpreter(ansible_action=None, interpreter_name='python', discovery_mode='off', task_vars=task_vars)

    with pytest.raises(ValueError):
        discover

# Generated at 2022-06-12 21:34:08.418505
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.module_utils.facts.hardware import Hardware
    from ansible.module_utils.facts.system import System
    from ansible.module_utils.facts.virtual import Virtual

    class FakeTask(object):
        _discovery_warnings = []
        _low_level_execute_command = None
        action = None

        def __init__(self):
            self.action = FakeAction(self)
            self.connection = FakeConnection()
            self.task_vars = {}

    class FakeAction(object):
        def __init__(self, task):
            self.task = task

    class FakeConnection(object):
        def __init__(self):
            self.has_pipelining = True


# Generated at 2022-06-12 21:34:17.753176
# Unit test for function discover_interpreter
def test_discover_interpreter():

    # Test with a basic interpreter_name
    interp_name = 'python'
    action = 'TEST'
    taskvars = {}

    # Test auto_legacy_silent
    # If the interpreter is available, use it, otherwise use the default
    taskvars['ansible_python_interpreter'] = '/usr/bin/python'
    discovery_mode = 'auto_legacy_silent'
    assert discover_interpreter(action, interp_name, discovery_mode, taskvars) == '/usr/bin/python'
    taskvars['ansible_python_interpreter'] = 'TEST/usr/bin/python'
    assert discover_interpreter(action, interp_name, discovery_mode, taskvars) == '/usr/bin/python'

    # Test auto_legacy
   

# Generated at 2022-06-12 21:34:21.380425
# Unit test for function discover_interpreter
def test_discover_interpreter():
    action = None
    interpreter_name = u'python'
    discovery_mode = u'auto_legacy_silent'
    task_vars = {}
    assert u'/usr/bin/python' == discover_interpreter(action, interpreter_name, discovery_mode, task_vars)

# Generated at 2022-06-12 21:34:28.707637
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.plugins.action import ActionBase
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    # Mocking a task_vars to call the discover_interpreter function.
    task_vars = {}

    # Mocking the INTERPRETER_PYTHON_DISTRO_MAP variable.

# Generated at 2022-06-12 21:34:41.050053
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.plugins import connection
    from ansible.plugins.loader import action_loader
    from ansible.module_utils.controls import BaseControls

    class TestConnection(connection.ConnectionBase):
        transport = 'test'

        def _connect(self):
            pass

        def exec_command(self, cmd, sudoable=False, in_data=None):
            assert not sudoable
            return {'stdout': _test_interpreter_action_output, 'stderr': None}

    class TestControls(BaseControls):
        def _execute_module(self, templar, module_name, module_args, task_vars, wrap_async=False):
            raise NotImplementedError()

    class TestAction(object):
        def __init__(self):
            self.loader = action_

# Generated at 2022-06-12 21:34:41.422127
# Unit test for function discover_interpreter
def test_discover_interpreter():
    pass

# Generated at 2022-06-12 21:34:51.575602
# Unit test for function discover_interpreter
def test_discover_interpreter():
    def execute(action, cmd, in_data=None):
        class FakeResult:
            def __init__(self, stderr, stdout):
                self.stderr = stderr
                self.stdout = stdout
        if cmd.startswith('/usr/bin/python'):
            if '"' in cmd:
                return FakeResult(stderr="failed to run python", stdout="")
            if 'platform_dist_result' in cmd:
                return FakeResult(stderr="", stdout="(u'rhel', u'7', u'7.4')")
            if 'osrelease_content' in cmd:
                return FakeResult(stderr="", stdout="ID=rhel\nVERSION_ID=7.4")

# Generated at 2022-06-12 21:35:00.808222
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.module_utils.facts.system.distribution import Distribution
    from ansible.module_utils.facts.system.distribution import DistributionFactCollector

    # test for python
    interpreter = discover_interpreter('python','auto','',{})
    assert interpreter == '/usr/bin/python'

    interpreter = discover_interpreter('python','auto','auto',{})
    assert interpreter == '/usr/bin/python'

    interpreter = discover_interpreter('python','auto_legacy_silent','',{})
    assert interpreter == '/usr/bin/python'

    interpreter = discover_interpreter('python','auto_legacy','',{})
    assert interpreter == '/usr/bin/python'

    interpreter = discover_interpreter('python','auto_legacy_silent','',{})

# Generated at 2022-06-12 21:35:35.288231
# Unit test for function discover_interpreter

# Generated at 2022-06-12 21:35:46.820005
# Unit test for function discover_interpreter
def test_discover_interpreter():
    import pytest
    from ansible.module_utils import basic
    from ansible.module_utils.common.parameters import get_flat_transform_keys
    from ansible.parsing.vault import VaultLib  # needed for _load_params
    from ansible.plugins.action import ActionBase  # needed for _load_params
    from ansible.plugins.loader import action_loader

    # Create minimal task and task_vars based on fixture data
    task = dict(
        action=dict(
            module='shell',
            args='uname -m',
            interpreter='python'
        )
    )

# Generated at 2022-06-12 21:35:55.545091
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.errors import AnsibleError
    from ansible.plugins.loader import interpreter_loader
    from ansible.executor.task_result import TaskResult
    from ansible.executor.action_result import ActionResult
    host = 'localhost'
    task_vars = {'inventory_hostname': host}
    connection = Connection(host=host)
    action = ActionModule(connection=connection, play_context=PlayContext(), new_stdin=None)
    action._supports_check_mode = True
    action._discovery_warnings = []

    # Test case 1: invalid interpreter (invalid input)
    test_case_name = "Invalid interpreter (invalid input)"
    interpreter_name = 'perl'
    discovery_mode = 'auto_legacy'

# Generated at 2022-06-12 21:36:02.603936
# Unit test for function discover_interpreter
def test_discover_interpreter():
    action = Display()
    task_vars = {}
    assert discover_interpreter(action, interpreter_name='python', discovery_mode='auto', task_vars=task_vars) == u'/usr/bin/python'
    task_vars = {'ansible_python_interpreter':u'/usr/bin/python'}
    assert discover_interpreter(action, interpreter_name='python', discovery_mode='auto', task_vars=task_vars) == u'/usr/bin/python'

# Generated at 2022-06-12 21:36:12.878172
# Unit test for function discover_interpreter
def test_discover_interpreter():
    assert _get_linux_distro({'platform_dist_result': ['redhat', '7.6', 'Santiago']}) == ('redhat', '7.6')
    assert _get_linux_distro({'osrelease_content': ['NAME="Red Hat Enterprise Linux Server"', 'VERSION="7.6 (Maipo)"']}) == ('Red Hat Enterprise Linux Server', '7.6 (Maipo)')
    assert _get_linux_distro({'osrelease_content': ['NAME="CentOS Linux"', 'VERSION="7 (Core)"']}) == ('CentOS Linux', '7 (Core)')

# Generated at 2022-06-12 21:36:20.421950
# Unit test for function discover_interpreter
def test_discover_interpreter():
    import sys
    try:
        # if we're running under pytest, no need to try to use the action plugin system
        import __main__
        if hasattr(__main__, '__file__') and __main__.__file__.endswith('pytest'):
            return
    except ImportError:
        pass

    from ansible.module_utils._text import to_bytes
    from ansible.plugins.action import ActionBase
    from ansible.plugins.action.basic import ActionModule

    class FakeActionModule(ActionModule):
        def run(self, tmp=None, task_vars=None):
            pass

    class FakeConnection(object):
        def __init__(self, has_pipelining=True, is_local=False):
            self.has_pipelining = has_pipelining
            self

# Generated at 2022-06-12 21:36:28.836909
# Unit test for function discover_interpreter
def test_discover_interpreter():

    # inputs
    action = None
    interpreter_name = 'python'
    discovery_mode = 'auto_legacy_silent'
    task_vars = {'inventory_hostname': 'unknown',
                 'connection_type': 'paramiko'}

    #execution
    try:
        discover_interpreter(action, interpreter_name, discovery_mode, task_vars)
    except Exception as ex:
        assert False, 'Exception raised in discover_interpreter: {0}'.format(ex)

    # cleanup

    #asserts
    assert True

# Generated at 2022-06-12 21:36:38.760634
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.executor.task_result import TaskResult
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()


# Generated at 2022-06-12 21:36:44.271537
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # Test python discovery
    action = None
    task_vars = {}
    py = discover_interpreter(action, 'python', 'silent', task_vars)
    assert py == '/usr/bin/python'

    # Test discovery with discovery_warnings
    action = None
    task_vars = {}
    action._discovery_warnings = []
    py = discover_interpreter(action, 'python', 'warn', task_vars)
    assert py == '/usr/bin/python'
    assert action._discovery_warnings != []

    # Test non-existent interpreter_name
    action = None
    task_vars = {}
    action._discovery_warnings = []
    py = discover_interpreter(action, 'foo', 'warn', task_vars)

# Generated at 2022-06-12 21:36:53.885239
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.executor.task_executor import *
    from ansible.plugins.loader import *
    from ansible.executor.action_plugins.script import *

    class DummyPlugin(object):
        def __init__(self):
            self.action = ActionModule()

    class DummyConnection(object):
        def __init__(self):
            self.action = ActionModule()
            self.has_pipelining = True

    class DummyModule(object):
        def __init__(self):
            self._connection = DummyConnection()
            self._task = TaskExecutor()

# Generated at 2022-06-12 21:38:02.530410
# Unit test for function discover_interpreter
def test_discover_interpreter():

    interpreter_name = 'python'
    discovery_mode = 'auto'
    task_vars = dict()

    try:
        assert None == discover_interpreter(None, interpreter_name, discovery_mode, task_vars)
    except:
        assert False

    # verify the fallback is working properly
    try:
        discover_interpreter(None, 'perl', discovery_mode, task_vars)
        assert False
    except ValueError:
        assert True

    # verify the not implemented error is being raised
    task_vars['inventory_hostname'] = 'test_host'
    try:
        discover_interpreter(None, interpreter_name, discovery_mode, task_vars)
        assert False
    except NotImplementedError:
        assert True


# Generated at 2022-06-12 21:38:10.361697
# Unit test for function discover_interpreter
def test_discover_interpreter():

    test_mock_dict = dict()

    test_mock_dict ['python_version'] = {
        'python': {
            'platform_python_map': {
                'debian': {
                    '6': '/usr/bin/python',
                    '7': '/usr/bin/python'
                },
                'ubuntu': {
                    '12.04': '/usr/bin/python',
                    '14.04': '/usr/bin/python',
                },
                'centos': {
                    '6': '/usr/bin/python',
                    '7': '/usr/bin/python'
                }
            },
            'python_fallback': ['/usr/bin/python'],
        }
    }

    from ansible.executor import discovery
    from ansible.module_utils.connection import Connection

# Generated at 2022-06-12 21:38:17.996670
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.executor import module_common
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.plugins.loader import action_loader
    import sys

    class FakeOptions(object):
        module_name = 'shell'
        become = False
        gather_facts = 'no'
        host_vars = {}
        remote_user = 'testuser'
        remote_pass = None
        become_user = 'testuser'
        become_pass = None
        become_method = None
        connection = 'smart'
        forks = 10
        remote_tmp = '/tmp'
        private_key_file = None
        module_paths = None
        listtags = False
        listtasks = False
        listhosts = None
        syntax = False
        subset = None
        inventory = None

# Generated at 2022-06-12 21:38:27.733662
# Unit test for function discover_interpreter
def test_discover_interpreter():
    import unittest
    from ansible.module_utils.ansible_release import __version__ as ansible_version
    from ansible.module_utils.six import StringIO

    class TestException(Exception):
        pass

    # Mock class to wrap the action object
    class MockAction:
        def __init__(self, requested_interpreter, discovery_mode, task_vars):
            self._requested_interpreter = requested_interpreter
            self._discovery_mode = discovery_mode
            self._task_vars = task_vars
            self._discovery_warnings = []
            self._connection = MockConnection()

        @property
        def interpreter(self):
            return self._requested_interpreter

        @property
        def discovery_mode(self):
            return self._discovery_mode



# Generated at 2022-06-12 21:38:37.017050
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.plugins.action import ActionBase
    from ansible.module_utils._text import to_bytes

    class FakeAction(ActionBase):

        def __init__(self):
            self.args_supported_by_discovery = True
            self._discovery_warnings = []
            self._low_level_execute_command = self._dummy_execute
            class FakeConn:
                has_pipelining = True
            self._connection = FakeConn()


# Generated at 2022-06-12 21:38:45.010862
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # Need to mock the following globals
    # display = Display()
    # foundre = re.compile(r'(?s)PLATFORM[\r\n]+(.*)FOUND(.*)ENDFOUND')
    global display
    global foundre

    # mock display
    display = type('Display', (object,), dict())()

    # mock foundre
    foundre = type('RegexObject', (object,), dict())()
    foundre.match = lambda x: type('MatchObject', (object,), dict(groups=lambda: ['linux', '\n/usr/bin/python']))

    # mock the _get_linux_distro function for _version_fuzzy_match
    def mock_linux_distro(platform_info):
        return u'centos', u'5.11'

    #

# Generated at 2022-06-12 21:38:55.726024
# Unit test for function discover_interpreter
def test_discover_interpreter():
    class Action:
        def __init__(self):
            self._low_level_execute_command = None
            self._connection = None
            self._module_version_was_not_found = False
            self._discovery_warnings = []

    action = Action()
    task_vars = {}
    test_interpreter_name = 'python'
    test_discovery_mode = 'force_legacy_silent'
    interpreter = discover_interpreter(action=action,
                                       interpreter_name=test_interpreter_name,
                                       discovery_mode=test_discovery_mode,
                                       task_vars=task_vars)
    assert interpreter == '/usr/bin/python'
    action._low_level_execute_command = None
    action._connection = None
    action._module_version

# Generated at 2022-06-12 21:39:05.881481
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.plugins.action.script import ActionModule
    am = ActionModule(task=None, connection=None, play_context=None, loader=None, shared_loader_obj=None, templar=None)
    # Set default interpreter to python2.7 as some distro stop providing python2.7 by default.
    am.default_interpreter = "/usr/bin/python2.7"
    am.discovery_warnings = []
    am._connection.has_pipelining = True

    am.action = 'script'  # we only support the script action for now

    assert discover_interpreter(am, "python", "auto_legacy_silent", {'inventory_hostname': 'localhost'}) == '/usr/bin/python'

# Generated at 2022-06-12 21:39:08.397604
# Unit test for function discover_interpreter
def test_discover_interpreter():
    display.verbosity = 4
    display.debug_level = 5
    print(discover_interpreter('test', 'python', 'auto_legacy_silent', {}))

# Generated at 2022-06-12 21:39:17.110737
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.plugins.action import ActionBase
    import ansible.executor.discovery
    import sys

    class TestActionBase(ActionBase):
        def __init__(self, task, connection, play_context, loader, templar, shared_loader_obj):
            self._task = task
            self._connection = connection
            self._play_context = play_context
            self._loader = loader
            self._templar = templar
            self._shared_loader_obj = shared_loader_obj

            # self._task.environment is not available at this stage
            self._task.environment = dict()
            self._task.args = dict()
            self._task.no_log = False

            self._low_level_execute_command = None
            # this is needed to raise exception in case of connection failure