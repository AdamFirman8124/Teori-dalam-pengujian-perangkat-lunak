

# Generated at 2022-06-12 21:30:16.691046
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.executor.task_result import TaskResult
    from ansible.executor.task_executor import TaskExecutor
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.inventory.manager import InventoryManager
    from ansible.plugins.loader import plugin_loader

    from ansible.vars.manager import VariableManager
    from ansible.vars.hostvars import HostVars
    from ansible.vars.reserved import Reserved
    from ansible.parsing.dataloader import DataLoader

    display.verbosity = 3
    display.color = 'off'
    display.deprecation = 'stderr'

    inventory_path = ''
    loader = DataLoader()

    inventory = InventoryManager(loader=loader, sources='localhost,')
    variable_manager

# Generated at 2022-06-12 21:30:21.232374
# Unit test for function discover_interpreter
def test_discover_interpreter():

    try:
        from ansible_collections.testns.testcoll.plugins.modules import _test_discover_interpreter
        _test_discover_interpreter()
    except ImportError:
        # if we can't import the test module, we can't run the test.
        pass

# Generated at 2022-06-12 21:30:29.839846
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.plugins.loader import module_loader
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.vars import combine_vars
    from ansible.plugins.connection.local import Connection as LocalConnection
    from ansible.plugins.callback import CallbackBase
    import os
    import tempfile
    script_dir = os.path.dirname(os.path.abspath(__file__))


# Generated at 2022-06-12 21:30:32.276627
# Unit test for function discover_interpreter
def test_discover_interpreter():
    res = discover_interpreter('action', 'python', 'auto_legacy', 'task_vars')
    print(res)

# Generated at 2022-06-12 21:30:43.230357
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.playbook.task import Task
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible import context
    from ansible.plugins.loader import module_loader
    import ansible.constants as C

    class MockConnection:
        def __init__(self, has_pipelining):
            self._has_pipelining = has_pipelining

        def is_local(self):
            return False

        def has_pipelining(self):
            return self._has_pipelining

    class MockModule(object):
        def __init__(self):
            self._connection = MockConnection(False)

    # set up a dummy task
    task = Task()
    task.action = module_loader

# Generated at 2022-06-12 21:30:54.895975
# Unit test for function discover_interpreter
def test_discover_interpreter():

    if __name__ == '__main__':
        import os
        import sys

        __file__ = os.path.normpath(os.path.abspath(__file__))
        sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))

        # Save the original discover, so that we can restore it after the tests run
        original_discover_interpreter = discover_interpreter


# Generated at 2022-06-12 21:31:05.685775
# Unit test for function discover_interpreter
def test_discover_interpreter():
    try:
        # we can't directly import this as module_utils.discovery would have been imported first
        # and we need to test what happens when that happens
        import ansible.module_utils
        import ansible.module_utils.discovery
        # so we pop it off the module list so that it's reloaded when we import it
        del ansible.module_utils.discovery
    except ImportError:
        # this would be the case if ansible was run from an arbitrary directory
        # and the tests are run from the source root
        pass
    try:
        from ansible.module_utils.discovery import discover_interpreter
    except ImportError:
        from module_utils.discovery import discover_interpreter

    import copy

    import ansible.vars
    import ansible.utils.unsafe_proxy


# Generated at 2022-06-12 21:31:14.778177
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.plugins.action import ActionBase
    from ansible.plugins.connection import ConnectionBase
    from ansible.module_utils.six.moves import cStringIO
    import sys

    class TestAction(ActionBase):
        def __init__(self, *args, **kwargs):
            self._connection = TestConnection()
            self._low_level_execute_command = self._connection.execute
            super(TestAction, self).__init__(*args, **kwargs)

    class TestConnection(ConnectionBase):
        # In this case, we're emulating pipelining support
        def __init__(self, *args, **kwargs):
            super(TestConnection, self).__init__(*args, **kwargs)
            self._play_context = None
            self._shell = None
            self._connected = True
           

# Generated at 2022-06-12 21:31:25.440133
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.plugins.action import ActionBase
    from ansible.plugins.loader import action_loader

    class MockAction(ActionBase):
        def __init__(self):
            super(MockAction, self).__init__()
            self._discovery_warnings = []

# Generated at 2022-06-12 21:31:38.278582
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.executor.task_result import TaskResult
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager

    class Connection(object):

        def __init__(self, has_pipelining):
            self.has_pipelining = has_pipelining

    module_name = 'raw'
    loader = DataLoader()
    play_context = PlayContext()
    action = TaskResult(task=dict(action={'__use_supplied_args': True,
                                          'module_name': module_name,
                                          'args': {'name': 'test'}}),
                        loader=loader,
                        variable_manager=VariableManager(),
                        play_context=play_context)

# Generated at 2022-06-12 21:31:57.173305
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # initialize the task variable
    task_vars = {}

    # initialize the action variable
    from ansible.executor.task_result import TaskResult
    task_result = TaskResult()
    task_result.command = ''

    # for testing purpose, create a new action object
    class Action(object):
        def __init__(self):
            self._connection = {'has_pipelining': True}
            self._discovery_warnings = []

        def _low_level_execute_command(self, cmd, sudoable=True, in_data=None):
            import ansible.executor.module_common as module_common

            # initialize the result variable
            res = {}

            # if cmd is 'uname'

# Generated at 2022-06-12 21:32:04.338258
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.executor.task_result import TaskResult
    from ansible.module_utils.six import PY2
    from ansible.plugins.loader import _import_plugins
    from ansible.plugins.loader import action_loader
    from ansible.vars.manager import VariableManager

    _import_plugins()
    results = []
    action_name = 'setup'
    discovery_mode = 'auto_silent'
    python_interpreter = 'python'

    class ActionModule(object):
        def __init__(self):
            self.display = Display()
            self.discovery_warnings = []


# Generated at 2022-06-12 21:32:16.888959
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.playbook import Task

    # simple case: no overrides, no params
    action = Task()
    task_vars = {}

    # TODO: this doesn't actually work in isolation if nothing has been imported, because config is None
    #       on the first call to C.config.get_config_value
    # FUTURE: make test_plugin_config and test_config available to us
    result = discover_interpreter(action, 'python', 'auto', task_vars)

    assert result == u'/usr/bin/python'

    # Ubuntu 18.04 case

# Generated at 2022-06-12 21:32:18.569627
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # TODO: write test_discover_interpreter
    pass

# Generated at 2022-06-12 21:32:19.241443
# Unit test for function discover_interpreter
def test_discover_interpreter():
    pass

# Generated at 2022-06-12 21:32:28.379300
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # Lets create a mock object
    import io
    import sys

    class MockModule:
        class ActionModule:
            def _low_level_execute_command(self, command, sudoable=False, in_data=None):
                # match result
                try:
                    return {'command': command, 'stdout': next(self.list_of_results)}
                except StopIteration:
                    return None


# Generated at 2022-06-12 21:32:40.533748
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.plugins.action import ActionBase
    from ansible.executor._low_level_execute_command import Result
    from units.mock.loader import DictDataLoader

    class DiscoveryAction(ActionBase):
        def __init__(self, tb, connection, play_context, loader, templar, shared_loader_obj):
            self._task_blocks = []
            self._shared_loader_obj = shared_loader_obj
            self._loader = loader
            self._templar = templar
            self._tqm = None
            self._connection = connection
            self._play_context = play_context
            self._remote_tmp = None


# Generated at 2022-06-12 21:32:48.331614
# Unit test for function discover_interpreter
def test_discover_interpreter():
    #test discovery without discovery_mode
    action_instance = type('test',
                       (object,),
                       {'_low_level_execute_command': lambda self, cmd, sudoable=None, in_data=None:
                        {'stdout':u'PLATFORM\nLinux\nFOUND\n/usr/bin/python /usr/bin/python2\nENDFOUND'}})()
    interpreter_name = u'python'
    discovery_mode = 'normal'
    task_vars = {}
    res = discover_interpreter(action_instance, interpreter_name, discovery_mode, task_vars)
    assert res == '/usr/bin/python2'

# Generated at 2022-06-12 21:32:49.881552
# Unit test for function discover_interpreter
def test_discover_interpreter():
    """ Test discover_python_interpreter()
    """
    # Test case 1:
    # Test case 2:
    # Test case 3:
    # Test case 4:
    pass

# Generated at 2022-06-12 21:32:51.362169
# Unit test for function discover_interpreter
def test_discover_interpreter():
    """
    :return:
    """
    #TODO
    #raise NotImplementedError
    pass


# Generated at 2022-06-12 21:33:11.759269
# Unit test for function discover_interpreter
def test_discover_interpreter():
    class ActionWrapper:

        def __init__(self):
            self._connection = ConnectionWrapper()
            self._discovery_warnings = []

        def _low_level_execute_command(self, cmd, sudoable=None, in_data=None):
            return self._connection._low_level_execute_command(cmd, sudoable, in_data)

    class ConnectionWrapper:

        def __init__(self):
            self.has_pipelining = True

        def _low_level_execute_command(self, cmd, sudoable=None, in_data=None):
            if cmd.startswith('echo PLATFORM'):
                return self._simulate_uname()
            elif cmd.startswith('command -v'):
                return self._simulate_command_v()

# Generated at 2022-06-12 21:33:23.244215
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.playbook.play_context import PlayContext
    from ansible.module_utils.connection import Connection
    from ansible.module_utils.shell import Shell
    from ansible.plugins.loader import find_plugin
    from ansible.vars.manager import VariableManager
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager

    # The host object is used to load variables about the host, which will be used to set the variable 'ansible_python_interpreter'.
    class Host(object):
        def __init__(self, name='fuzzy_match'):
            self.name = name
           

# Generated at 2022-06-12 21:33:33.388756
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.executor.task_result import TaskResult
    from ansible.playbook.task import Task
    from ansible.executor.module_common import _load_params
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    import ansible.plugins.action
    import ansible.plugins.action.setup
    import ansible.plugins.action.command
    import ansible.plugins.action.copy
    import ansible.plugins.action.ping
    import ansible.plugins.action.raw
    import ansible.plugins.action.script
    import ansible.plugins.action.shell
    import ansible.plugins.action.k8s
    import ansible.plugins.action.net_tools

   

# Generated at 2022-06-12 21:33:43.994627
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.executor.task_result import TaskResult
    from ansible.executor.task_executor import TaskExecutor

    class FakeAction(object):
        def __init__(self):
            self._discovery_warnings = []
            self._connection = FakeConnection()
            self._task = FakeTask()

    class FakeTask(object):
        def __init__(self):
            self._ds = {
                'interpreter': 'python',
                'discovery_mode': 'auto_legacy_silent'
            }
            pass

    class FakeConnection(object):
        def __init__(self):
            self.has_pipelining = True
            self.supports_exec = False


# Generated at 2022-06-12 21:33:55.241146
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # Please note there are some changes in this test as
    # the script python_target.py was replaced by LinuxDistribution.
    from ansible.module_utils.distro import get_distro_info

    platform_python_map = {'redhat': {'7.0': '/usr/bin/python2.7', '6.0': '/usr/bin/python2.6'},
                           'centos': {'7.0': '/usr/bin/python2.7', '6.0': '/usr/bin/python2.6'}}
    bootstrap_python_list = ['/usr/bin/python2.6', '/usr/bin/python2.7', '/usr/bin/python']
    platform_info = {}
    platform_info["platform_dist_result"] = get_distro_info()

    #

# Generated at 2022-06-12 21:33:59.477252
# Unit test for function discover_interpreter
def test_discover_interpreter():
    """This should not raise InterpreterDiscoveryRequiredError"""
    action = None
    interpreter_name = 'python'
    discovery_mode = 'auto_legacy'
    task_vars = {}

    # This should not raise InterpreterDiscoveryRequiredError
    discover_interpreter(action, interpreter_name, discovery_mode, task_vars)

# Generated at 2022-06-12 21:34:07.858675
# Unit test for function discover_interpreter
def test_discover_interpreter():

    # Test case 1: no interpreter found
    assert discover_interpreter(None, 'python', 'auto_legacy_silent', None) == '/usr/bin/python'
    assert discover_interpreter(None, 'python', 'auto_legacy', None) == '/usr/bin/python'

    # Test case 2: python interpreter found
    assert discover_interpreter(None, 'python', 'auto_legacy_silent', None) == '/usr/bin/python'
    assert discover_interpreter(None, 'python', 'auto_legacy', None) == '/usr/bin/python'

# Generated at 2022-06-12 21:34:17.296354
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # Setup a minimal action that can be used to run the interpreter discovery
    class Action:
        def __init__(self):
            self._discovery_warnings = []
            self._connection = Connection()

        def _low_level_execute_command(self, command, sudoable=True, in_data=None, executable='/bin/sh',
                                       use_unsafe_shell=False):
            return self._connection.send(command, sudoable, in_data, executable,
                                         use_unsafe_shell)

    class Connection:
        def __init__(self):
            self.has_pipelining = True


# Generated at 2022-06-12 21:34:25.826508
# Unit test for function discover_interpreter
def test_discover_interpreter():
    import json

    resp_format = {'stdout': '', 'stderr': ''}
    task_vars = {}

    class LowLevelExecuteCommand(object):
        def __init__(self, data):
            self._data = data

        def __getitem__(self, key):
            return self._data.get(key)

        def __contains__(self, key):
            return key in self._data

    class CustomActionModule(object):
        def __init__(self, data):
            self._data = data
        
        def __getitem__(self, key):
            return self._data.get(key)

        def __contains__(self, key):
            return key in self._data


# Generated at 2022-06-12 21:34:31.090285
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from collections import namedtuple
    from six import string_types

    failed = False
    Action = namedtuple('Action', ['_low_level_execute_command', '_connection', '_discovery_warnings'])
    HostVars = namedtuple('HostVars', ['ansible_connection', 'inventory_hostname', 'ansible_distribution'])
    Connection = namedtuple('Connection', ['has_pipelining'])
    action = Action(None, Connection(has_pipelining=True), [])


# Generated at 2022-06-12 21:34:53.155608
# Unit test for function discover_interpreter
def test_discover_interpreter():
    """
    Test that discover_interpreter returns a string.

    """
    from ansible.plugins.action import ActionBase
    task_vars = {'interpreter_python_version': 2}
    action = ActionBase(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert  isinstance(discover_interpreter(action, 'python', 'auto', task_vars), str)

# Generated at 2022-06-12 21:35:01.955700
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.plugins import action

    def action_plugin_for_platform(platform, script):
        def action_plugin(task_vars=None):
            class ActionModule(ActionBase):
                def run(self, tmp=None, task_vars=None):
                    return dict(command=self._low_level_execute_command)

            action_result = ActionModule.run(task_vars=task_vars)
            action_result['stdout'] = platform + "\n" + script + "\n"
            return action_result

        return action_plugin

    localhost = action.ActionModule(connection='local', module_name='', module_args='')

    expected_interpreter = '/usr/bin/python'

# Generated at 2022-06-12 21:35:09.953915
# Unit test for function discover_interpreter
def test_discover_interpreter():
    import os
    # Make sure we are in a module directory so we can find our data files
    assert os.path.basename(os.getcwd()).startswith('lib')

    # TODO: move to pytest, maybe create a mock object with some of the action methods
    from ansible.plugins.action.normal import ActionModule as norm

    action = norm()
    action._discovery_warnings = []

    # TODO: make a mock connection for action, for something that can run the command and return stuff?
    # This is required for discover_interpreter to work
    action._low_level_execute_command = lambda x, y, z: False

    task_vars = {
        'inventory_hostname': 'localhost',
        'config': {},
        'ns': 'foo'
    }

    # TODO

# Generated at 2022-06-12 21:35:20.619374
# Unit test for function discover_interpreter
def test_discover_interpreter():
    import unittest

    class DisplayStub(object):
        def __getattr__(self, item):
            return (lambda *args, **kwargs: None)

    from ansible.executor.task_result import TaskResult
    from ansible.plugins import module_loader
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.utils.color import Colorizer

    class HostTest(object):
        pass

    class ConnectionTest(object):
        def __init__(self, is_pipelining):
            self._is_pipelining = is_pipelining

        def has_pipelining(self):
            return self._is_pipelining


# Generated at 2022-06-12 21:35:29.514770
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.action import ModuleAction
    from ansible.inventory.host import Host

    from ansible.module_utils.basic import AnsibleModule

    test_host = Host(name="test_host", port=22)


# Generated at 2022-06-12 21:35:41.573175
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # Test case 1: supported Linux distro
    action = object()
    setattr(action, '_low_level_execute_command', lambda *args, **kwargs: {u'stdout': u''})
    setattr(action, '_connection', object())
    setattr(action._connection, 'has_pipelining', True)
    setattr(action, '_discovery_warnings', [])

    task_vars = dict()

    # Mock the INTERPRETER_PYTHON_DISTRO_MAP
    python_distro_map = dict()
    python_distro_map['rhel'] = dict()
    python_distro_map['rhel']['6'] = u'/opt/rh/python27/root/usr/bin/python'

# Generated at 2022-06-12 21:35:52.413486
# Unit test for function discover_interpreter
def test_discover_interpreter():
    display = Display()
    display.verbosity = 4
    import unittest
    import os
    import shutil
    import tempfile

    class TestModule(object):
        def __init__(self, action_plugin, connection_plugin):
            self._action_plugin = action_plugin
            self._connection_plugin = connection_plugin

        def run(self):
            connection = self._connection_plugin.Connection(task_uuid='uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu',
                                                            connection=self._connection_plugin.shell.connection, host='localhost',
                                                            port=None, username=None, password=None)

# Generated at 2022-06-12 21:36:03.354750
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # noinspection PyUnusedLocal
    def fake_low_level_execute_command(cmd, **kwargs):
        # noinspection PyUnresolvedReferences
        if cmd == 'command -v python':
            return {'rc': 0, 'stderr': '', 'stdout': '/usr/bin/python'}
        elif cmd == 'command -v python3':
            return {'rc': 0, 'stderr': '', 'stdout': '/usr/bin/python3'}
        elif cmd == 'command -v python2':
            return {'rc': 0, 'stderr': '', 'stdout': '/usr/bin/python2'}

# Generated at 2022-06-12 21:36:13.663608
# Unit test for function discover_interpreter
def test_discover_interpreter():
    class MockAction(object):
        def __init__(self):
            self._discovery_warnings = []
            self._low_level_execute_command = self.ll_execute

        def ll_execute(self, *args, **kwargs):
            return dict(stdout='PLATFORM\nLinux\nFOUND\n/usr/bin/python\n/usr/bin/python3\nENDFOUND')

    class MockConnection(object):
        def __init__(self):
            self.has_pipelining = True

    mockaction = MockAction()
    mockaction._connection = MockConnection()
    mockaction.task_vars = dict(ansible_python_interpreter_discovery='auto')


# Generated at 2022-06-12 21:36:18.271067
# Unit test for function discover_interpreter
def test_discover_interpreter():

    action = {}
    interpreter_name = 'python'
    discovery_mode = 'auto_legacy_silent'
    task_vars = {}

    global display
    display = Display()

    res = discover_interpreter(action, interpreter_name, discovery_mode, task_vars)
    assert res == u'/usr/bin/python'


if __name__ == '__main__':
    test_discover_interpreter()

# Generated at 2022-06-12 21:36:41.379938
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.plugins.action import ActionBase

    class MockActionModule(ActionBase):
        def __init__(self):
            self._discovery_warnings = []

        def warn(self, msg):
            self._discovery_warnings.append(msg)

        def _low_level_execute_command(self, cmd, sudoable=True, in_data=None):
            res = {
                'command': cmd,
                'rc': 0,
                'stdout': u'PLATFORM\nLinux\nFOUND\n/usr/bin/python\n/usr/bin/python2.7\nENDFOUND',
            }
            res['stdout'] = res['stdout'].encode('utf8') if isinstance(res['stdout'], unicode) else res['stdout']
            return res

# Generated at 2022-06-12 21:36:52.374693
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.modules.system.setup import get_var
    from ansible.playbook.task import Task

    class Fake_action():
        def __init__(self):
            self.task_vars = dict()
            self._low_level_execute_command = dict()
            self._is_pipelining = False
            self._connection = dict()
            self._connection['has_pipelining'] = False

        def _low_level_execute_command(self, cmd, in_data=None, sudoable=False):
            return dict()


    action = Fake_action()
    action.task_vars['ansible_connection'] = 'local'
    action._low_level_execute_command = get_var
    action._is_pipelining = False
    action._connection['has_pipelining'] = False

# Generated at 2022-06-12 21:36:58.460878
# Unit test for function discover_interpreter
def test_discover_interpreter():
    action = None
    interpreter_name = 'python'
    discovery_mode = 'auto_legacy'
    task_vars = {}

    pt = discover_interpreter(action, interpreter_name, discovery_mode, task_vars)

    assert pt == '/usr/bin/python'

    interpreter_name = 'python'
    discovery_mode = 'auto_legacy_silent'
    task_vars = {}

    pt = discover_interpreter(action, interpreter_name, discovery_mode, task_vars)

    assert pt == '/usr/bin/python'

# Generated at 2022-06-12 21:37:08.661135
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.executor.discovery import discover_interpreter
    from ansible.utils.vars import combine_vars


# Generated at 2022-06-12 21:37:16.315986
# Unit test for function discover_interpreter
def test_discover_interpreter():
    assert discover_interpreter(action=None, interpreter_name=u"python", discovery_mode=u"auto", task_vars={}) is not None
    assert discover_interpreter(action=None, interpreter_name=u"python", discovery_mode=u"auto_legacy", task_vars={}) is not None
    assert discover_interpreter(action=None, interpreter_name=u"python", discovery_mode=u"auto_legacy_silent", task_vars={}) is not None
    assert discover_interpreter(action=None, interpreter_name=u"python", discovery_mode=u"auto_silent", task_vars={}) is not None

# Generated at 2022-06-12 21:37:23.079848
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.plugins.action.script import ActionModule
    from ansible.plugins.action.normal import ActionModule as _ActionModule
    #setup monkey patching
    ActionModule._low_level_execute_command = fake_low_level_execute_command
    ActionModule.get_bin_path = fake_get_path


# Generated at 2022-06-12 21:37:24.716770
# Unit test for function discover_interpreter
def test_discover_interpreter():
    discover_interpreter(None, 'python', 'legacy', None)

# Generated at 2022-06-12 21:37:28.737373
# Unit test for function discover_interpreter
def test_discover_interpreter():
    executor_module = __import__('ansible.executor.discovery', fromlist=['discover_interpreter'])
    result = executor_module.discover_interpreter(None, 'python', 'auto_silent', None)
    # On success, the function returns the discovered python interpreter
    assert isinstance(result, str)

# Generated at 2022-06-12 21:37:36.291232
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.executor.task_result import TaskResult
    from ansible.plugins.action.script import ActionModule
    from ansible.module_utils.facts import cache


# Generated at 2022-06-12 21:37:45.538895
# Unit test for function discover_interpreter
def test_discover_interpreter():
    task_vars = {'inventory_hostname': 'localhost',
                 'platform_python_map': {'darwin': {'10.12': '/usr/bin/python'},
                                         'freebsd': {'11.0': '/usr/local/bin/python'},
                                         'linux': {'6': '/usr/bin/python2.6',
                                                   '8': '/usr/bin/python3.7'}},
                 'interpreter_python_fallback': ['/usr/bin/python', '/usr/bin/python2.7']}

    action = MockAction()
    print(discover_interpreter(action, interpreter_name='python', discovery_mode='auto', task_vars=task_vars))



# Generated at 2022-06-12 21:38:21.933797
# Unit test for function discover_interpreter
def test_discover_interpreter():
    print(discover_interpreter(action=None, interpreter_name='python', discovery_mode='auto', task_vars={}))

# Generated at 2022-06-12 21:38:31.232018
# Unit test for function discover_interpreter
def test_discover_interpreter():
    class MockLowLevelExecCommandReturns(object):
        def __init__(self, stdout=None, stderr=None, rc=None):
            self.stdout = stdout
            self.stderr = stderr
            self.rc = rc
        def get(self, key):
            return getattr(self, key)
    class MockLowLevelExecCommandObj(object):
        _low_level_execute_command_return_val = None
        def __init__(self, sudoable):
            self.sudoable = sudoable
        def _low_level_execute_command(self, command, sudoable, in_data=None):
            if in_data:
                self._low_level_execute_command_return_val = in_data
            return self._low_level_execute_command_return_val
   

# Generated at 2022-06-12 21:38:32.638735
# Unit test for function discover_interpreter
def test_discover_interpreter():


    # TODO: fix /var/tmp/python_target.py version check
    pass



# Generated at 2022-06-12 21:38:42.095288
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # FIXME: use fake hosts so we don't need anything real in the task_vars
    task_vars = dict()
    discovery_warnings = list()
    action = type('ActionModule', (object,), {
        '_discovery_warnings': discovery_warnings,
    })
    assert(discover_interpreter(action, 'python', 'auto_legacy', task_vars) == '/usr/bin/python')
    assert(discovery_warnings == [u'No python interpreters found for host unknown (tried [u\'/usr/bin/python\', u\'/usr/local/bin/python\'])'])

    def _low_level(command, sudoable, in_data):
        if command == u'uname':
            return dict(stdout=u'Linux')

# Generated at 2022-06-12 21:38:46.515779
# Unit test for function discover_interpreter
def test_discover_interpreter():
    assert(discover_interpreter("action", "python", "auto_legacy_silent", {}) == u"/usr/bin/python")
    assert(discover_interpreter("action", "python3", "auto_silent", {}) is None)

# Generated at 2022-06-12 21:38:56.447119
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.module_utils.six.moves import StringIO
    from ansible.plugins.action import ActionBase
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext

    loader = DataLoader()

    def dummy_loader_find_file(path):
        # TODO: tests for missing fallbacks
        return '/usr/bin/python'

    # get_raw_module_path is used to create a tmp loadable module named
    # python_target.py, but we wont be using it
    dummy_loader_get_raw_module_path = lambda x: None

    # Abstract base class for connection plugins
    class DummyConnection(object):
        def __init__(self, has_pipelining):
            self.has_pipelining = has_

# Generated at 2022-06-12 21:39:06.603761
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.plugins.loader import action_loader
    from ansible.inventory.manager import InventoryManager
    import ansible.constants as C
    import os


# Generated at 2022-06-12 21:39:15.794338
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.plugins.action import ActionBase
    from ansible.vars.manager import VariableManager
    from ansible.inventory import Inventory
    from ansible.inventory.host import Host
    from ansible.parsing.dataloader import DataLoader

    class FakeAction(ActionBase):
        _discovery_warnings = []

        class _FakeConnection(object):
            has_pipelining = True

        def __init__(self, dl):
            self._loader = dl

        def _low_level_execute_command(self, *args, **kwargs):
            return dict(stdout=u'PLATFORM\nLinux\nFOUND\n/usr/bin/python\nENDFOUND')

        def _execute_module(self, *args, **kwargs):
            pass


# Generated at 2022-06-12 21:39:27.276846
# Unit test for function discover_interpreter
def test_discover_interpreter():
    import pytest
    from ansible.executor.task_result import TaskResult
    from ansible.executor.module_common import _load_params
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins.action import ActionBase
    from ansible.vars import VariableManager

    class FakeConnection(object):
        def __init__(self, has_pipelining):
            self.has_pipelining = has_pipelining

    class FakeAction(ActionBase):
        def __init__(self, interpreters, warn_on_no_interpreters):
            self._discovered_python_interpreter = None
            self._discovery_warnings = []
            self._interpreters = interpreters
            self._warn_on_no_interpreters = warn_on_no_inter

# Generated at 2022-06-12 21:39:34.710554
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.executor.task_result import TaskResult

    # Called from a task that doesn't actually need interpreter discovery, but needs to be able to do it
    class DummyModule:
        def __init__(self):
            self._discovery_warnings = []

    # External library that we can patch to get fake introspection responses
    class DummyConnection:
        def __init__(self):
            self.has_pipelining = True

    class DummyAction:
        def __init__(self):
            self._discovery_warnings = []
            self._connection = DummyConnection()
