

# Generated at 2022-06-12 21:30:18.669020
# Unit test for function discover_interpreter
def test_discover_interpreter():
    action = MagicMock()
    action._low_level_execute_command = MagicMock()
    action._low_level_execute_command.return_value = {
        'stdout': u'PLATFORM\nLinux\nFOUND\n/usr/bin/python\n/usr/bin/python2\n/usr/bin/python2.7\nENDFOUND',
        'stderr': u''
    }
    action._connection = MagicMock()
    action._connection.has_pipelining = True
    task_vars = dict()

    assert discover_interpreter(action, 'python', 'auto', task_vars) == u'/usr/bin/python2.7'

# Generated at 2022-06-12 21:30:27.448544
# Unit test for function discover_interpreter
def test_discover_interpreter():
    import os
    import tempfile
    import shutil

    import pytest

    # create a temp directory to store the test data
    test_dir = tempfile.mkdtemp()
    test_data_dir = os.path.join(test_dir, 'test_data')
    os.mkdir(test_data_dir)

    # create temp files in test_data_dir

    # mock a module_utils directory
    module_utils_dir = os.path.join(test_data_dir, 'ansible', 'module_utils')
    os.makedirs(module_utils_dir)

    # mock a distribution directory
    distribution_dir = os.path.join(module_utils_dir, 'distribution')
    os.mkdir(distribution_dir)

    # mock a platform.py file

# Generated at 2022-06-12 21:30:35.969509
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins.action.copy import ActionModule as CopyActionModule
    from ansible.executor.task_result import TaskResult

    display.verbosity = 4

    class ActionModule(CopyActionModule):
        def __init__(self, task, connection, play_context, loader, templar, shared_loader_obj):
            super(ActionModule, self).__init__(task, connection, play_context, loader, templar, shared_loader_obj)

    # ---------------------------------------------------------------------------------------
    # Test 1: normal case, success
    host = 'abc.com'
    task = Task()
    task._role = None
    task.action = 'copy'
    task.args = {}
    task._role_

# Generated at 2022-06-12 21:30:46.146695
# Unit test for function discover_interpreter
def test_discover_interpreter():
    task_vars = dict()
    action = dict()
    action['module_name'] = 'setup'

    # Test basic functionality
    platform_info = dict()
    platform_info['platform_dist_result'] = ['redhat', '6.5', 'Final']
    platform_info['osrelease_content'] = None
    actual_result = discover_interpreter(action, 'python', 'auto', task_vars)
    assert actual_result == '/usr/bin/python2', "Failed to discover python interpreter correctly"

    # Test when platform_dist_result is not valid
    platform_info['platform_dist_result'] = ['redhat', '6.5', 'Final']
    platform_info['osrelease_content'] = None

# Generated at 2022-06-12 21:30:57.210691
# Unit test for function discover_interpreter
def test_discover_interpreter():
    import os
    import shutil
    import tempfile


# Generated at 2022-06-12 21:31:06.185560
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # Setup mock test object
    # Display module not used in discovery
    display.display = None
    class MockAction:
        def __init__(self):
            self._discovery_warnings = []

        def _low_level_execute_command(self, cmd, sudoable=None, in_data=None):
            res = dict()
            if cmd == "echo PLATFORM; uname; echo FOUND; command -v 'python'; echo ENDFOUND":
                res['stdout'] = u"PLATFORM\nLinux\nFOUND\n/usr/bin/python\nENDFOUND"

# Generated at 2022-06-12 21:31:12.905126
# Unit test for function discover_interpreter
def test_discover_interpreter():
    import pytest

    from .discovery_test_data import parse_test_file

    discovery_test_data = parse_test_file(__file__.replace('.pyc', '.py'))

    pytest.importorskip("platform")

    for test in discovery_test_data:
        action = DiscoveryHostAction()
        test['action'] = action
        test['task_vars'] = dict(inventory_hostname='dummy')

        res = discover_interpreter(**test)
        assert res == test['expected_result']



# Generated at 2022-06-12 21:31:23.881447
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.plugins.action import ActionBase
    from ansible.plugins.loader import action_loader
    from ansible.playbook.task import Task
    from ansible.playbook.play import Play
    from ansible.playbook.block import Block
    class MockActionBase(ActionBase):

        def __init__(self, task, connection, play_context, loader, templar, shared_loader_obj):
            ActionBase._shared_loader_obj = shared_loader_obj
            super(MockActionBase, self).__init__(task, connection, play_context, loader, templar)

        def _low_level_execute_command(self, cmd, sudoable=True, in_data=None, stdin=None):
            return {"stdout" : cmd}


# Generated at 2022-06-12 21:31:29.671666
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # This test is a placeholder for now, until we add more tests for this function.
    # The basic idea is that I want to test a few different cases of this, such as
    # when /usr/bin/python is not found, and when it is found, and in both of those
    # cases when the discovery mode is 'auto', 'auto_legacy', or 'auto_silent'.
    assert True

# Generated at 2022-06-12 21:31:34.653605
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.playbook.play_context import PlayContext
    from ansible.inventory.host import Host
    from ansible.vars.manager import VariableManager

    class FakeModule(object):
        def __init__(self, args, from_file=False):
            self.args = args
            self.from_file = from_file

    class FakeRunner(object):
        def __init__(self, *args, **kwargs):
            self._low_level_execute_command = self.low_level_execute_command

        def low_level_execute_command(self, cmd, in_data=None, sudoable=True):
            if in_data:
                if isinstance(cmd, to_text):
                    cmd = to_native(cmd)

# Generated at 2022-06-12 21:31:45.125614
# Unit test for function discover_interpreter
def test_discover_interpreter():
    pass

# Generated at 2022-06-12 21:31:55.286321
# Unit test for function discover_interpreter

# Generated at 2022-06-12 21:32:03.177754
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible import context
    context.CLIARGS = dict()

    from ansible.plugins.task.action.python_interpreter import ActionModule as pyint_action

    from ansible.executor.task_result import TaskResult
    from ansible.playbook.play_context import PlayContext

    def mock_exec_command(action, cmd, sudoable=False, in_data=None):
        class MockExecCommandResult(object):
            def get(self, key):
                return None

        return MockExecCommandResult()

    mocked_task_vars = dict()

    mocked_action = pyint_action()
    mocked_action._low_level_execute_command = mock_exec_command
    mocked_action._connection = object()
    mocked_action._connection.has_pipelining = True

    # TODO:

# Generated at 2022-06-12 21:32:16.536215
# Unit test for function discover_interpreter
def test_discover_interpreter():
    import sys
    import tempfile
    from ansible.module_utils.urls import open_url

    def fake_low_level_execute_command(cmd, sudoable=True, in_data=None):
        # Not exported; we assume this is used in a temp dir (thus writeable)
        with open('test_stdout', 'w') as f:
            f.write(to_text(result_data['stdout'], errors='surrogate_or_strict'))
        with open('test_stderr', 'w') as f:
            f.write(to_text(result_data['stderr'], errors='surrogate_or_strict'))
        return result_data


# Generated at 2022-06-12 21:32:26.886297
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.plugins.action import ActionBase

    class MockActionModule(ActionBase):

        def _low_level_execute_command(self, cmd, sudoable=False, in_data=None, executable=None):
            res = {
                'cmd': cmd,
                'in_data': in_data,
                'platform': self._connection._shell.run(cmd, in_data=in_data)
            }
            res['stdout'] = res['platform'].stdout.read()
            return res

    action_module = MockActionModule()


# Generated at 2022-06-12 21:32:39.031914
# Unit test for function discover_interpreter
def test_discover_interpreter():
    action = object()
    action._low_level_execute_command = object()
    action._low_level_execute_command.return_value = {'stdout': ''}
    action._connection = object()
    action._connection.has_pipelining = True
    action._discovery_warnings = []

    import ansible.executor.discovery
    ansible.executor.discovery.C.config = object()
    ansible.executor.discovery.C.config.get_config_value = object()
    ansible.executor.discovery.C.config.get_config_value.return_value = {'platform_python_map': {}, 'bootstrap_python_list': []}
    ansible.executor.discovery.LooseVersion = object()


# Generated at 2022-06-12 21:32:47.189614
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.utils.display import Display
    from ansible.parsing.dataloader import DataLoader

    class MockConnection(object):
        def __init__(self):
            self._shell = False

        def has_pipelining(self):
            return self._shell

        @property
        def shell(self):
            return self._shell

        @shell.setter
        def shell(self, value):
            self._shell = value

        def set_shell_type(self, shell):
            self._shell = True

        def _low_level_execute_command(self, cmd, sudoable=False, in_data=None, sudo_user=None):
            return dict(stdout=cmd)

    class MockInterpreter(object):
        def __init__(self):
            self._connection = MockConnection()

# Generated at 2022-06-12 21:32:54.914972
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.executor.connection_info import ConnectionInformation
    from ansible.executor.play_iterator import PlayIterator
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext

    loader = DataLoader()
    variable_manager = PlayIterator(loader=loader, inventory=None, play=None, play_context=PlayContext())

    # Make a fake action to test with
    action = object()

# Generated at 2022-06-12 21:33:06.596476
# Unit test for function discover_interpreter
def test_discover_interpreter():

    # mock the action object
    action = type('obj', (object,), {
        '_low_level_execute_command': lambda self, cmd, sud, in_data: {'stdout': cmd},
        '_connection': type('obj', (object,), {'has_pipelining': True,
                                               'supports_persistence': False,
                                               'persistent_connection': False})(),

    })()
    action._discovery_warnings = []
    result = discover_interpreter(action, 'python', 'auto', {})
    assert result

    result = discover_interpreter(action, 'python', 'auto_legacy', {})
    assert result

    # test with interpreter name other than python

# Generated at 2022-06-12 21:33:07.110541
# Unit test for function discover_interpreter
def test_discover_interpreter():
    raise NotImplementedError

# Generated at 2022-06-12 21:33:35.811075
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.executor.task_result import TaskResult
    from ansible.playbook.play_context import PlayContext

    context = PlayContext()

    result = TaskResult(host=None, task=None, return_data=dict(changed=True))
    result._result = {'stderr': '', 'stdout': 'PLATFORM\nLinux\nFOUND\n/usr/bin/python\nENDFOUND'}
    assert '/usr/bin/python' == \
           discover_interpreter(action=result, interpreter_name='python', discovery_mode='auto', task_vars={})

    # Test the case that platform uname returns an unexpected result

# Generated at 2022-06-12 21:33:48.065012
# Unit test for function discover_interpreter
def test_discover_interpreter():
    import ansible.executor.discovery
    import ansible.module_utils.facts.system.distribution
    import platform
    import sys

    def test_distro_match(d_result, osrelease_content, os_rel_id, os_rel_id_version, target_interpreter, hostname):
        # replace the real _parse_os_release_content with a mock that returns the given osrelease_content
        os_release_patch = ansible.module_utils.facts.system.distribution.os_release_patch

        def mock_parse_os_release_content(raw_content):
            return ansible.module_utils.facts.system.distribution._parse_os_release_content(osrelease_content)


# Generated at 2022-06-12 21:33:57.463489
# Unit test for function discover_interpreter
def test_discover_interpreter():
    task_vars = {'ansible_discovery_interpreter_python': 'auto_legacy'}
    task_vars.update(C.config.defaults.get('DEFAULT_VARIABLE_MERGE_DATA', {}))
    task_vars.update(C.config.defaults.get('DEFAULT_VARIABLE_PRECEEDENCE', {}))
    action = Action()
    python_interpreter = discover_interpreter(action, 'python', 'auto_legacy', task_vars)
    required_interpreter = task_vars.get('ansible_python_interpreter')
    assert python_interpreter is not None, 'Could not find interpreter'

# Generated at 2022-06-12 21:34:07.988625
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.plugins.action import ActionModule
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    from ansible.playbook.task_include import TaskInclude
    from ansible.inventory.host import Host
    from ansible.vars.manager import VariableManager


# Generated at 2022-06-12 21:34:09.172517
# Unit test for function discover_interpreter

# Generated at 2022-06-12 21:34:16.961750
# Unit test for function discover_interpreter
def test_discover_interpreter():
    import pytest
    task_vars = {}
    # test the code when there is no interpreter_name
    with pytest.raises(ValueError):
        discover_interpreter(None, '', '', task_vars)

    # test the code when the interpreter_name is not python
    with pytest.raises(ValueError):
        discover_interpreter(None, 'python2', '', task_vars)

    for item in ['', '_silent', 'auto', 'auto_legacy', 'auto_legacy_silent']:
        discover_interpreter(None, 'python', item, task_vars)



# Generated at 2022-06-12 21:34:24.923455
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # hosts without a suitable Python
    assert discover_interpreter('', 'python', 'silent_auto', {'discovery_warnings': []}) is None

    # hosts with a suitable Python
    class Action(object):
        def __init__(self):
            self._connection = None
        def _low_level_execute_command(self, cmd, sudoable, in_data=None):
            return dict(stdout=cmd)
    action = Action()
    action._connection = Action()
    action._connection.has_pipelining = True
    action._discovery_warnings = []

    assert discover_interpreter(action, 'python', 'silent_auto', {}) == 'python'
    assert action._discovery_warnings == []

# Generated at 2022-06-12 21:34:36.064078
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.plugins.loader import find_plugin
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.task_result import TaskResult
    try:
        from ansible.inventory.manager import InventoryManager
        inventory_manager = InventoryManager(action=None, loader=None, sources=None)
    except ImportError:
        from ansible.inventory import Inventory
        inventory_manager = Inventory(action=None, loader=None, sources=None)
    inventory_manager._inventory = []
    inventory_manager._hosts_cache = None
    inventory_manager._pattern_cache = None
    #
    # inventory_manager._set_inventory(None)
    # inventory_manager._get_hosts(None)
    # inventory_

# Generated at 2022-06-12 21:34:46.261267
# Unit test for function discover_interpreter
def test_discover_interpreter():
    import os.path
    import pytest
    from ansible.module_utils import basic

    # Mock the basic action
    class ActionModule(basic._ANSIBLE_ARGS):
        def __init__(self, *args, **kwargs):
            super(ActionModule, self).__init__(*args, **kwargs)
            self._discovery_warnings = []

        def _low_level_execute_command(self, *args, **kwargs):
            display.vvv('mock: low level execute command called with args {0} and kwargs {1}'.format(args, kwargs))

# Generated at 2022-06-12 21:34:48.737945
# Unit test for function discover_interpreter
def test_discover_interpreter():
    import json
    from ansible.module_utils.six import PY3
    # TODO: add tests
    pass

# Generated at 2022-06-12 21:35:39.521139
# Unit test for function discover_interpreter
def test_discover_interpreter():  # pragma: no cover
    from ansible.executor.module_common import InterpreterDiscoveryFailure, _get_interpreter_discovery_mode

    # TODO: find a better place to put this, perhaps wrappers.py?
    class FakeModuleAction(object):
        def __init__(self):
            self._connection = FakeConnection()
            self._discovery_warnings = []

        def _low_level_execute_command(self, command, sudoable=True, in_data=None):
            return {
                'stdout': command
            }


# Generated at 2022-06-12 21:35:50.492484
# Unit test for function discover_interpreter
def test_discover_interpreter():
    action = MockAction()


# Generated at 2022-06-12 21:35:57.023780
# Unit test for function discover_interpreter
def test_discover_interpreter():
    """
    This is a unittest for the discover_interpreter() function to make sure that python interpreter discovery works as
    expected.
    """
    from ansible import Context
    import ansible_collections.ansible.community.plugins.loader.action_plugin as action_plugin
    from ansible.executor import task_executor
    from ansible.executor.task_executor import ActionTaskExecutor
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.vault import VaultLib
    from ansible.plugins.loader import action_loader

    test_inventory = '''
    localhost ansible_python_interpreter=/usr/bin/python3
    '''


# Generated at 2022-06-12 21:36:07.806425
# Unit test for function discover_interpreter
def test_discover_interpreter():
    try:
        from ansible.plugins.action import ActionBase
        from ansible.plugins.connection import ConnectionBase
    except ImportError:
        # fallback for Ansible < 2.5
        from ansible.runner.action_plugins.action import ActionBase
        from ansible.runner.connection_plugins.connection import ConnectionBase
    
    class FakeAction(ActionBase):
        def __init__(self, connection):
            self._connection = connection
            self._low_level_execute_command = connection.exec_command
            # needed for debug output
            self._play_context = connection._play_context
            # needed for warning output
            self._discovery_warnings = []

    class FakeConnection(ConnectionBase):
        def __init__(self, platform_type):
            self._play_context = None
            self._platform_type

# Generated at 2022-06-12 21:36:14.351775
# Unit test for function discover_interpreter
def test_discover_interpreter():
    action = None
    interpreter_name = 'python'
    discovery_mode = 'auto'
    task_vars = {'ansible_python_interpreter': '/usr/bin/python',
                 'ansible_python_major_version': 2,
                 'ansible_python_version': '2.7.5',
                 'ansible_distribution': 'RedHat',
                 'ansible_distribution_version': '7.4',
                 'ansible_facts': {'platform': 'Linux'}}
    assert discover_interpreter(action, interpreter_name, discovery_mode, task_vars) == '/usr/bin/python'

# Generated at 2022-06-12 21:36:15.314542
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # interpret_discovery_results not implemented yet
    pass

# Generated at 2022-06-12 21:36:23.693423
# Unit test for function discover_interpreter
def test_discover_interpreter():
    '''
    Test the discover_interpreter function.
    '''
    assert discover_interpreter(None, 'python', 'auto_silent', {}) == '/usr/bin/python'
    assert discover_interpreter(None, 'python', 'auto_silent', {'inventory_hostname': 'localhost'}) == '/usr/bin/python'
    assert discover_interpreter(None, 'python', 'auto_legacy_silent', {'inventory_hostname': 'localhost'}) == '/usr/bin/python'



# Generated at 2022-06-12 21:36:34.808945
# Unit test for function discover_interpreter
def test_discover_interpreter():
    """Unit test for function discover_interpreter
    We need a mocked action object to test this, but it's not easy to create such an object.
    A solution is to use Python's mock framework and patch the _low_level_execute_command
    method on the object.
    """

    # mock setUp
    import sys
    import mock

    if sys.version_info[0] == 2:
        import __builtin__ as builtins
    else:
        import builtins

    with mock.patch.object(builtins, 'open'):
        from ansible.plugins.action import ActionBase

        class ActionModule(ActionBase):
            def _low_level_execute_command(self, cmd, sudoable=False, in_data=None):
                """"Mock method for _low_level_execute_command"""
                module = {}

# Generated at 2022-06-12 21:36:42.163586
# Unit test for function discover_interpreter
def test_discover_interpreter():

    interpreter_name = 'python'

    # Empty task_vars in case it's needed in the future
    task_vars = {}

    # Set up an empty action
    class MockAction:
        def __init__(self):
            self._connection = MockConnection()
            self._discovery_warnings = []

        def _low_level_execute_command(self, cmd, sudoable=False, in_data=None):
            return MockAction._low_level_execute_command(cmd, sudoable, in_data)

        @staticmethod
        def _low_level_execute_command(cmd, sudoable=False, in_data=None):
            # Make sure we only pass in strings
            cmd = to_text(cmd, errors='surrogate_or_strict')

# Generated at 2022-06-12 21:36:44.745611
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # This can't be made a standalone unit test as task_vars is a param and real task_vars
    # aren't available in this test. Issue is FIXME'd in the body of the function.
    # TODO: should be able to stub task_vars via pytest fixtures
    assert discover_interpreter(None, 'python', 'auto', {})

# Generated at 2022-06-12 21:37:35.177605
# Unit test for function discover_interpreter
def test_discover_interpreter():
   action={}
   task_vars={}
   role = 'python'
   interpreter_path = discover_interpreter(action, role, "auto", task_vars)
   assert(isinstance(interpreter_path, str))

if __name__ == '__main__':
   test_discover_interpreter()

# Generated at 2022-06-12 21:37:44.296695
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # load test data
    platform_python_map = json.loads(pkgutil.get_data('ansible.executor.discovery', 'os_python_map.json').decode('utf-8'))
    bootstrap_python_list = json.loads(pkgutil.get_data('ansible.executor.discovery', 'python_fallback.json').decode('utf-8'))
    demo = json.loads(pkgutil.get_data('ansible.executor.discovery', 'demo_data.json').decode('utf-8'))
    # generate test cases
    testcases = []

# Generated at 2022-06-12 21:37:56.425144
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # pylint: disable=import-error,no-name-in-module,redefined-variable-type
    from ansible.executor.discovery import discover_interpreter
    from ansible.executor.discovery import _get_linux_distro
    from ansible.executor.discovery import _version_fuzzy_match
    import ansible.module_utils.distro

    task_vars = {
        'inventory_hostname': 'localhost',
        'connection': 'local',
        'ansible_host': 'localhost',
    }

    display.vvv = True
    display.verbosity = 0
    display.debug = True
    display.warning = True

    # test _version_fuzzy_match function

# Generated at 2022-06-12 21:38:06.251375
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # make sure discovery fails when the discovery mode is empty
    try:
        discover_interpreter(None, 'python', '', None)
    except InterpreterDiscoveryRequiredError as e:
        assert e.message == 'interpreter_name=python must specify a supported discovery mode'
        assert e.interpreter_name == 'python'
        assert e.discovery_mode == ''
    else:
        assert False  # wrong or no exception thrown
    try:
        discover_interpreter(None, 'python', 0, None)
    except ValueError as e:
        assert str(e) == 'Interpreter discovery not supported for python'
    else:
        assert False  # wrong or no exception thrown

    # make sure discovery fails when the discovery mode is invalid

# Generated at 2022-06-12 21:38:15.918951
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.playbook.task import Task
    from ansible.executor.task_result import TaskResult
    from ansible.playbook.play import Play
    from ansible.vars.manager import VariableManager

    results_callback = lambda x: None
    playbook_task = Task()
    playbook_task._role = None
    playbook_task._block = None
    playbook_task._parent = None
    playbook_task._parent_role = None
    playbook_task._play = Play().load(dict(
        name="Ansible Play",
        hosts='localhost',
        gather_facts='no',
        tasks=[dict(action=dict(module='command', args='ls'))]
    ), variable_manager=VariableManager(), loader=None)

# Generated at 2022-06-12 21:38:21.364297
# Unit test for function discover_interpreter
def test_discover_interpreter():
    global display
    display = Display()

    assert discover_interpreter('action', 'python', 'auto_legacy_silent', {'inventory_hostname': 'testhost'}) == '/usr/bin/python'
    assert 'No python interpreters found' in display.display.messages[0]
    display.display.clean()

    assert discover_interpreter('action', 'python', 'auto_silent', {'inventory_hostname': 'testhost'}) == '/usr/bin/python'
    assert 'No python interpreters found' in display.display.messages[0]
    display.display.clean()

    assert discover_interpreter('action', 'python', 'fail_silent', {'inventory_hostname': 'testhost'}) == '/usr/bin/python'

# Generated at 2022-06-12 21:38:27.858494
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # failed discover_interpreter.
    try:
        discover_interpreter(None, 'python', 'auto', {})
    except InterpreterDiscoveryRequiredError as e:
        assert e.interpreter_name == 'python'
        assert e.discovery_mode == 'auto'
    except Exception as e:
        assert False, "discover_interpreter failed, with unexpected exception: %s" % to_native(e)
    else:
        assert False, "discover_interpreter failed, with no exception"

# Generated at 2022-06-12 21:38:37.166650
# Unit test for function discover_interpreter
def test_discover_interpreter():
    import sys

    if sys.version_info < (2, 7):
        import unittest2 as unittest
    else:
        import unittest

    from ansible_collections.ansible.python.plugins.module_utils.legacy import (
        ActionModule as OldStyleActionModule
    )

    from ansible.executor.discovery import ActionModule

    from ansible.plugins.action import ActionBase

    from ansible.utils.vars import combine_vars

    task_vars = dict()

    class TestModule(object):
        """
        Mock module
        """
        def __init__(self, module_name='', module_args='', module_deprecated=False, check_invalid_arguments=True):
            self.task_vars = task_vars

# Generated at 2022-06-12 21:38:40.161651
# Unit test for function discover_interpreter
def test_discover_interpreter():
    import ansible.plugins.action.normal
    action = ansible.plugins.action.normal.ActionModule('shell', )
    assertion = discover_interpreter(action, 'python', 'auto', {})
    assert assertion is not None

# Generated at 2022-06-12 21:38:50.447837
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.plugins.action import ActionBase
    from ansible.utils.connection import Connection
    from ansible.module_utils.connection import ConnectionError

    class DummyActionModule(ActionBase):
        __traceable_doc__ = False
        __metaclass__ = type
        _discovery_warnings = []

        def _low_level_execute_command(self, command, sudoable=True, in_data=None, executable=None):
            if command == ['command', '-v', '/usr/bin/python']:
                return dict(stdout=u'FOUND\n/usr/bin/python\nENDFOUND')

            if command == '/usr/bin/python':
                return dict(stdout=json.dumps(dict(platform_dist_result=['', '', ''])))
