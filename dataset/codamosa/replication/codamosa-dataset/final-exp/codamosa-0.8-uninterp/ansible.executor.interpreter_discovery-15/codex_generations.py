

# Generated at 2022-06-12 21:30:16.408727
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.executor.discovery import discover_interpreter
    task_vars = {}
    action = "dummy"
    interpreter_name = "python"
    discovery_mode = "auto_silent"

    # test with exception
    try:
        discover_interpreter(action, interpreter_name, discovery_mode, task_vars)
    except InterpreterDiscoveryRequiredError as e:
        assert e.interpreter_name == "python"

# Generated at 2022-06-12 21:30:25.431575
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.module_utils.common.collections import ImmutableDict
    display.vvv = lambda msg: msg
    action = ImmutableDict()
    interpreter_name = 'python'
    # discovery_mode = 'auto'

# Generated at 2022-06-12 21:30:35.904238
# Unit test for function discover_interpreter
def test_discover_interpreter():
    import sys
    if sys.version_info[0] > 2:
        from unittest.mock import MagicMock
    else:
        from mock import MagicMock

    action = MagicMock()
    interpreter_name = 'python'
    discovery_mode = 'auto'
    task_vars = {}

    def exec_command(cmd, in_data, sudoable):
        if cmd in ('/usr/bin/python3', '/usr/bin/python2', '/usr/bin/python'):
            return {'stdout': """{
                    "osrelease_content": "ID=centos\nVERSION_ID=7.4.1708\n",
                    "platform_dist_result": ["", "", ""]
                }"""}

# Generated at 2022-06-12 21:30:46.041072
# Unit test for function discover_interpreter
def test_discover_interpreter():
    test_action = DummyActionModule()
    test_task_vars = dict(
        inventory_hostname='testhost',
        ansible_connection='local',
        # These are required for the config lookup
        ansible_user='dummy',
        ansible_ssh_user='dummy',
        ansible_ssh_pass='dummy',
        ansible_become_pass='dummy',
        remote_addr='127.0.0.1',
        transport='local',
    )
    # Test ST1: supported Linux distro with Python 2.7
    # FUTURE: expand to test ST2 and ST3
    # FIXME: this is fragile; ideally we discover the actual distro we're running in and use that...
    test_task_vars['ansible_distribution'] = 'CentOS'
    test

# Generated at 2022-06-12 21:30:57.122726
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # Yes, this is a huge unit test, but the logic of get_interpreter() is complex enough that it needs
    # to be broken down and to have tests for the individual parts.
    # NOTE: even though discover_interpreter is private, we need to call it in this test function.
    from ansible.executor.discovery import discover_interpreter

    class TestAction(object):
        def __init__(self):
            self._discovery_warnings = []
            self._connection = TestConnection()


# Generated at 2022-06-12 21:31:06.134097
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # Mockup _low_level_execute_command
    class test_action:
        def __init__(self):
            self._discovery_warnings = list()
            self._connection = Connection()


# Generated at 2022-06-12 21:31:17.636077
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # For now, we'll just infer a basic sanity check from the display filter:
    from ansible.module_utils._text import to_bytes
    from ansible.utils.display import Display

    display = Display()
    display.add_filter(to_bytes)
    display.verbosity = 4

    host = 'test.example.org'

    import copy
    import pkg_resources
    # TODO: fix paths in fixtures when this goes upstream
    bootstrap_python_list = [
        "/usr/bin/python",
        "/usr/bin/python2.7",
        "/usr/bin/python2",
        "/bin/python",  # py3-only case
        "/usr/local/bin/python",
        "/usr/bin/python3",
        "/usr/bin/python3.6",
    ]
   

# Generated at 2022-06-12 21:31:27.293949
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.playbook.play_context import PlayContext  # FIXME: need better way to get dict for a task_vars
    action = PlayContext()
    action._discovery_warnings = []
    action._connection = None  # FIXME: need a way to mock at least connection.has_pipelining
    action._low_level_execute_command = None  # FIXME: need a way to mock _low_level_execute_command

    interpreter_name = u'python'

# Generated at 2022-06-12 21:31:40.003758
# Unit test for function discover_interpreter
def test_discover_interpreter():
    interpreter_name = 'python'
    discovery_modes = ['auto_legacy', 'auto_legacy_silent', 'auto', 'auto_silent']
    task_vars = {}

# Generated at 2022-06-12 21:31:48.456033
# Unit test for function discover_interpreter
def test_discover_interpreter():
    try:
        from ansible.plugins.action.normal import ActionModule
    except ImportError:
        raise ImportError('ansible.plugins.action.normal is not importable')
    obj = ActionModule(connection=None, runner=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

    # Test run on Ubuntu 18.04
    task_vars = {
        'inventory_hostname': 'ubuntu-vm',
        'hostvars': {'ubuntu-vm': {}},
        'ansible_python_interpreter': '',
        'ansible_connection': 'local',
        'ansible_host': 'ubuntu-vm',
        'ansible_python_version': 2.7,
        'ansible_user': 'johndoe'
    }
    result

# Generated at 2022-06-12 21:32:10.467692
# Unit test for function discover_interpreter
def test_discover_interpreter():
    interpreter_name = 'python'
    discovery_mode = 'auto'
    task_vars = dict()
    action = ''
    try:
        res = discover_interpreter(action, interpreter_name, discovery_mode, task_vars)
    except Exception as e:
        display.warning(msg=u'Unhandled error in Python interpreter discovery for host {0}: {1}'.format(action, to_text(e)))
        res = to_text(e)
    assert res == '/usr/bin/python'

# Generated at 2022-06-12 21:32:15.987151
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # Unit test function
    test_action = type('test_action', (object,), dict(
        _low_level_execute_command=lambda self, cmd, sudoable, in_data=None, executable=None: None,
        _connection=type('test_connection', (object,), dict(has_pipelining=True))(),
        _discovery_warnings=[]
    ))()

    # Test discovery fails when interpreter discovery not supported
    try:
        discover_interpreter(test_action, "python2", "auto", None)
        assert False, "Expected ValueError"
    except ValueError:
        pass

    # Test discovery fails when platform not supported

# Generated at 2022-06-12 21:32:26.674328
# Unit test for function discover_interpreter
def test_discover_interpreter():

    # x_discovery_warnings used to accumulate warnings for this test
    _x_discovery_warnings = []

    # Dummy class for _low_level_execute_command()
    class DummyAction(object):

        def __init__(self):
            self._discovery_warnings = _x_discovery_warnings


# Generated at 2022-06-12 21:32:34.144224
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.executor.action_plugins.shell import ActionModule as shell_module
    action = shell_module(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    action._low_level_execute_command = None
    action.warn = None
    interpreter = discover_interpreter(action, 'python', 'auto', {'inventory_hostname': 'myhost'})
    assert interpreter == u'/usr/bin/python'

# Generated at 2022-06-12 21:32:43.901812
# Unit test for function discover_interpreter
def test_discover_interpreter():
    assert discover_interpreter(None, "python", "auto_silent", {}) == '/usr/bin/python'
    assert discover_interpreter(None, "python", "auto_legacy_silent", {}) == '/usr/bin/python'
    assert discover_interpreter(None, "python", "force_silent", {}) == '/usr/bin/python'
    assert discover_interpreter(None, "python", "auto", {}) == '/usr/bin/python'
    assert discover_interpreter(None, "python", "auto_legacy", {}) == '/usr/bin/python'
    assert discover_interpreter(None, "python", "force", {}) == '/usr/bin/python'

# Generated at 2022-06-12 21:32:52.669691
# Unit test for function discover_interpreter
def test_discover_interpreter():
    action = None
    try:
        import ansible.plugins.action.normal
        action = ansible.plugins.action.normal.ActionModule(None, None, None, None)
        action._discovery_warnings = []
    except Exception as dummy:
        assert False

    test_interpreter_name = 'python'
    test_discovery_mode = 'auto_legacy_silent'
    test_task_vars = {'inventory_hostname': 'example.com'}

    try:
        from ansible.plugins.action.normal import ActionModule
        action = ActionModule(None, None, None, None)
    except Exception:
        assert False

    action._discovery_warnings = []

    # FUTURE: add test cases for various error paths, especially host-specific stuff (e.g. bootstrap)

# Generated at 2022-06-12 21:33:05.396012
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # I really just want to test that we're using the virtualenv python, not the system one
    import platform
    import sys

    assert discover_interpreter(None, 'python', 'strict', {}) == platform.system_executable
    assert discover_interpreter(None, 'python', 'auto', {}) == platform.system_executable
    assert discover_interpreter(None, 'python', 'auto_silent', {}) == platform.system_executable
    assert discover_interpreter(None, 'python', 'auto_legacy', {}) == '/usr/bin/python'
    assert discover_interpreter(None, 'python', 'auto_legacy_silent', {}) == '/usr/bin/python'

    # Test invalid interpreter

# Generated at 2022-06-12 21:33:15.656321
# Unit test for function discover_interpreter
def test_discover_interpreter():
    import doctest
    import sys

    # Mock out _low_level_execute_command and _connection.has_pipelining, since we can't reliably test them.

    def _low_level_execute(self, cmd, sudoable=None, in_data=None):
        return {'stderr': u'', 'stdout': to_text(cmd, errors='surrogate_or_strict')}

    def _has_pipelining(self):
        return True

    class MockAction(object):
        _low_level_execute_command = _low_level_execute
        _connection = MockConnection()
        _discovery_warnings = []

    class MockConnection(object):
        has_pipelining = _has_pipelining

    # Mock out INTERPRETER_PYTHON_DISTRO_MAP and

# Generated at 2022-06-12 21:33:25.826318
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.plugins.action import ActionBase

    class MockAction(ActionBase):
        def __init__(self):
            self._low_level_execute_command = lambda *args, **kwargs: {"rc": 0, "stdout": "", "stderr": "", "stdin": "", "path": "/bin/sh"}
            self._discovery_warnings = []

    action = MockAction()

    res = discover_interpreter(action, 'python', 'auto_legacy_silent', {'inventory_hostname': 'testhost'})

    assert res == u'/usr/bin/python'

    assert action._discovery_warnings == []
    print(action._discovery_warnings)

# Generated at 2022-06-12 21:33:35.352951
# Unit test for function discover_interpreter
def test_discover_interpreter():
    import os

    # Info on the test fixtures...
    #
    # There are three main categories of tests:
    #
    # (1) platform.dist() data (which is the "fallback" data from the old distro module); note that some
    #     of the distro-specific code has been elided, so we're only testing specific distros that have
    #     been included
    #
    # (2) os-release data; this should be used for all Linux systems that have this file, regardless of
    #     whether distro-specific dist() data is available
    #
    # (3) "extended" tests which incorporate platform.dist() AND os-release data to test the combination
    #     of the two
    #
    # For the first two categories (1, 2) the full set of distributions is tested with each possible
    #

# Generated at 2022-06-12 21:33:55.491031
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.executor.task_result import TaskResult
    from ansible.plugins.action.script import ActionModule as ScriptActionModule

    class MockActionModule(ScriptActionModule):
        _discovery_warnings = []

        def __init__(self, task, connection, play_context, loader, templar, shared_loader_obj):
            super(MockActionModule, self).__init__(task, connection, play_context, loader, templar, shared_loader_obj)
            self._task_vars = dict()

        def _low_level_execute_command(self, cmd, sudoable=False, in_data=None, executable=None):

            # cmd should be "command -v 'python'" for bootstrap
            if cmd.endswith('command -v \'python\''):
                resp = dict()


# Generated at 2022-06-12 21:33:57.084383
# Unit test for function discover_interpreter
def test_discover_interpreter():
    assert isinstance(discover_interpreter('action', 'python', 'auto', 'taskvars'), str)

# Generated at 2022-06-12 21:34:07.599392
# Unit test for function discover_interpreter
def test_discover_interpreter():
    action = None

# Generated at 2022-06-12 21:34:17.044523
# Unit test for function discover_interpreter

# Generated at 2022-06-12 21:34:25.612525
# Unit test for function discover_interpreter
def test_discover_interpreter():
    """Test discover_interpreter"""

    # Test correct path
    action = None
    interpreter_name = 'python'
    discovery_mode = 'auto_legacy_silent'
    task_vars = dict()
    task_vars['_ansible_version'] = dict()
    task_vars['_ansible_version']['full'] = '2.9.10'
    task_vars['_ansible_version']['major'] = 2
    task_vars['_ansible_version']['minor'] = 9
    task_vars['inventory_hostname'] = 'localhost'
    task_vars['inventory_hostname_short'] = 'localhost'

# Generated at 2022-06-12 21:34:38.088999
# Unit test for function discover_interpreter
def test_discover_interpreter():

    class TestAction():
        pass

    action = TestAction()
    action._discovery_warnings = []
    interpreter_name = 'python'
    discovery_mode = 'auto_legacy'
    task_vars = {'inventory_hostname': "localhost"}

    # test 1, data has result from uname and from platform.dist, /usr/bin/python is present and gets used
    action._low_level_execute_command = lambda _: {'stdout': u"PLATFORM\nLinux\nFOUND\n/usr/bin/python\nENDFOUND"}
    linux_python_script = pkgutil.get_data('ansible.executor.discovery', 'python_target.py')

# Generated at 2022-06-12 21:34:47.896549
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # TODO: add a unit test that actually can verify results
    # this one is just to make sure that test_discovery runs
    from ansible.module_utils.connection import Connection
    from ansible.module_utils.network.common.config import NetworkConfig
    from ansible.playbook.task import Task
    from ansible.plugins.loader import connection_loader
    from ansible.plugins.loader import module_loader

    # TODO: fake-out _low_level_execute_command?
    # got this from test_socket_connection
    setattr(Connection, '_low_level_execute_command', lambda *args, **kwargs: "test")
    setattr(Connection, '_low_level_execute_script', lambda *args, **kwargs: "test")

# Generated at 2022-06-12 21:34:57.822540
# Unit test for function discover_interpreter
def test_discover_interpreter():
    import sys
    import os
    # Add the test/units directory to the python path so we can import MockOSReleaseFile
    sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'units'))
    from mock_os_release_file import MockOSReleaseFile

    # Make sure we are able to detect what is the platform interpreter for centos 6.6
    # Mock the correct response for the platform script which gets executed
    # (we don't want to execute it for real because it would rquire sudo)
    MockOSReleaseFile.set_os_release_file_content('CentOS release 6.6 (Final)\n')

    import ansible.plugins.action.discovery as discovery_module
    discovery_mode = 'auto_silent'
    task_v

# Generated at 2022-06-12 21:35:00.662408
# Unit test for function discover_interpreter
def test_discover_interpreter():
    task_vars = dict(
        ansible_distribution='RedHat',
        ansible_distribution_version='6',
    )
    discover_interpreter('', 'python', 'auto_legacy_silent', task_vars)

# Generated at 2022-06-12 21:35:08.062805
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.modules.system import platform
    from ansible.playbook import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.cli import CLI
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.utils.vars import load_extra_vars
    from ansible.utils.vars import load_options_vars

    cli = CLI(args=[])
    cli._load_plugins()
    loader = DataLoader()

    # initialize needed objects
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader)
    variable_

# Generated at 2022-06-12 21:35:29.218642
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.plugins.action import ActionBase
    from ansible import context
    action = ActionBase(connection=None, task=None, play_context=context.CLIARGS, loader=None, templar=None, shared_loader_obj=None)
    assert discover_interpreter(action=action, interpreter_name='python', discovery_mode='legacy', task_vars={}) == '/usr/bin/python'

# Generated at 2022-06-12 21:35:41.337344
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.modules.extras.system.platform import get_distribution
    from ansible.plugins.loader import module_loader

    class ActionModule:
        def __init__(self, connection):
            self._connection = connection
            self._discovery_warnings = []

        def _low_level_execute_command(self, cmd, sudoable=True, in_data=None, executable=None):
            if cmd == 'command -v \'/usr/bin/python\'':
                return {'stdout': '/usr/bin/python\n'}

            if cmd == '/usr/bin/python':
                dist = get_distribution()
                return {'stdout': json.dumps(dist)}

            raise Exception('Unhandled command {0}'.format(cmd))



# Generated at 2022-06-12 21:35:52.249455
# Unit test for function discover_interpreter
def test_discover_interpreter():
    '''
    Testing discover_interpreter function in interpreter.py
    '''
    import mock
    import sys
    import os

    class MockConnection:
        def has_pipelining(self):
            return True

    # pylint: disable=too-few-public-methods
    class MockActionModule:
        '''
        Mock default action module
        '''
        class ActionModule(object):
            '''
            Mock action module
            '''
            class ActionModule:
                '''
                Mock action module class
                '''
                def __init__(self):
                    self.connection = MockConnection()
                    self.display = Display()
                    self.display._verbosity = 3
                    self.display.verbosity = 3

# Generated at 2022-06-12 21:36:03.176495
# Unit test for function discover_interpreter
def test_discover_interpreter():
    import ansible.module_utils.common.interpreter_discovery as interp_disc

    is_auto_legacy = 'auto_legacy'
    is_auto = 'auto'
    is_auto_silent = 'auto_silent'
    is_auto_legacy_silent = 'auto_legacy_silent'

    valid_mode = [is_auto_legacy, is_auto, is_auto_silent, is_auto_legacy_silent]


# Generated at 2022-06-12 21:36:13.461514
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.plugins.action.script import ActionModule as Script

    # test with no interpreter specified; should pick the first python found
    task_vars = dict(
        ansible_distribution='CentOS',
        ansible_distribution_version='6.6',
        ansible_python_interpreter='/usr/bin/python2.7'
    )
    action = Script(task=dict(action=dict(module_name='script')))
    display.verbosity = 2
    res = discover_interpreter(action, u'python', u'auto', task_vars)
    assert res == '/usr/bin/python', res
    display.verbosity = 1

    # test with interpreter specified

# Generated at 2022-06-12 21:36:24.267139
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.executor.task_result import TaskResult
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.module_utils.facts.system.distribution import Distribution
    from ansible.plugins.action import ActionBase
    from ansible.connection.connection_loader import get_connection_instance
    from ansible.module_utils.facts.system.platform import Platform
    from ansible.inventory.host import Host
    from ansible.playbook.play_context import PlayContext
    import ansible.executor.discovery
    import ansible.plugins.loader

    # TODO: The only way to change the interpreter name is to subclass the BaseModuleExecutor class.
    # When this test is moved to the test_module_utils_basic module we will be able to subclass properly
    # and make this test more

# Generated at 2022-06-12 21:36:35.244505
# Unit test for function discover_interpreter
def test_discover_interpreter():
    class TestAction:
        def __init__(self):
            self._connection = TestConnection(has_pipelining=True)
            self._discovery_warnings = []

        def _low_level_execute_command(self, cmd, sudoable=False, in_data=None):
            return self._connection._connect(cmd, sudoable, in_data)

    class TestConnection:
        def __init__(self, has_pipelining=False):
            self.has_pipelining = has_pipelining

        def _connect(self, cmd, sudoable=False, in_data=None):
            if self.has_pipelining:
                res = {}
                res['stdout'] = u'{"platform_dist_result": ["centos", "7.5.1804", "Core"]}'
                return

# Generated at 2022-06-12 21:36:41.014312
# Unit test for function discover_interpreter
def test_discover_interpreter():

    fakes = FakeModule()

    args = {
        "interpreter_name": "python",
        "discovery_mode": "auto",
        "task_vars": {},
    }

    # Test case 1: Unix
    fakes.ansible_os_family = 'Unix'
    output = discover_interpreter(fakes, **args)
    # Test case 1: if test is fail output is different
    assert output == '/usr/bin/python'

    # Test case 2: Windows
    fakes.ansible_os_family = 'Windows'
    output = discover_interpreter(fakes, **args)
    # Test case 2: if test is fail output is different
    assert output == '/usr/bin/python'


# Class with all attributes and methods of class TaskExecutor.

# Generated at 2022-06-12 21:36:52.368432
# Unit test for function discover_interpreter
def test_discover_interpreter():
    test_interpreter = 'python'
    warn_message = []
    test_action = lambda: None
    test_action._discovery_warnings = warn_message
    test_action._connection = lambda: None
    test_action._connection.has_pipelining = True
    test_task_vars = dict()


# Generated at 2022-06-12 21:37:01.746342
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # Positive test cases where interpreter identification should succeed
    # identifiers and expected interpreter paths should be paired
    identifier_interpreter_expected = [
        ('python', '/usr/bin/python'),
        ('python2', '/usr/bin/python2'),
        ('python3.4', '/usr/bin/python3.4'),
        ('python3.5', '/usr/bin/python3.5'),
        ('python3.5.5', '/usr/bin/python3.5.5'),
        ('python3.6', '/usr/bin/python3.6'),
        ('python3.7', '/usr/bin/python3.7'),
        ('python3.8', '/usr/bin/python3.8'),
        ('python3.9', '/usr/bin/python3.9')
    ]

    # Negative test cases where interpreter

# Generated at 2022-06-12 21:37:51.650296
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.plugins.action import ActionBase
    class TestAction(ActionBase):
        _discovery_warnings = []
        class Connection:
            transport = u'ssh'
            def has_pipelining(self):
                return True
        @staticmethod
        def _low_level_execute_command(cmd, sudoable=False, in_data=None):
            return {'stdout':cmd, 'stderr':None}

    action = TestAction()
    task_vars = {}
    res = discover_interpreter(action, u'python', u'auto_legacy_silent', task_vars)
    print(res)
    assert res == '/usr/bin/python'

if __name__ == '__main__':
    test_discover_interpreter()

# Generated at 2022-06-12 21:38:03.002396
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.executor.discovery import discover_interpreter
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    display = Display(v=3)

    # No match, no exception, fallback to /usr/bin/python
    test_case = u'PLATFORM\nLinux\nFOUND\ndoes_not_exist\nENDFOUND'
    task_vars = ImmutableDict({
        u'ansible_python_interpreter': u'/usr/bin/python',
        u'ansible_python_interpreter_fallback': u'/usr/bin/python'
    })

# Generated at 2022-06-12 21:38:10.811511
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.module_utils.discovery.test_lib import AnsibleAction
    from ansible.module_utils.facts.virtual.base import Virtual
    from ansible.plugins.action.discovery import ActionModule as Discovery

    # Create a task_vars object for the tests
    task_vars = {
        "ansible_facts": {
            "virtualization_type": Virtual.VIRTUALS.get("kvm")
        },
        "ansible_interpreter_python": {
            "test_interpreter_name": {
                "test_discovery_mode": "/path/to/python",
            }
        },
    }


# Generated at 2022-06-12 21:38:18.333070
# Unit test for function discover_interpreter
def test_discover_interpreter():
    assert discover_interpreter(None, 'python', 'auto', {}) == u'/usr/bin/python'

    action = MockAction()
    action._discovery_warnings = []
    assert discover_interpreter(action, 'python', 'auto_silent', {}) == u'/usr/bin/python'
    assert len(action._discovery_warnings) == 0

    action = MockAction()
    action._discovery_warnings = []
    assert discover_interpreter(action, 'python', 'auto_legacy', {}) == u'/usr/bin/python'
    assert len(action._discovery_warnings) == 1

    action = MockAction()
    action._discovery_warnings = []

# Generated at 2022-06-12 21:38:28.028404
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # pylint: disable=unused-argument
    import os
    import sys
    import unittest

    def _mock_execute_command(cmd, exe, failure_dict, module_name, verbosity):  # pylint: disable=unused-argument
        path = os.path.realpath(__file__).rsplit('/', 2)[0]
        py_test_data = os.path.join(path, 'test', 'python_test_data.json')

        with open(py_test_data) as data_f:
            data = json.load(data_f)

        ret = data.get(cmd)
        assert ret is not None

        return ret

    # mocked parts of AnsibleModule needed for test

# Generated at 2022-06-12 21:38:37.364271
# Unit test for function discover_interpreter
def test_discover_interpreter():
    import ansible.executor.discovery
    import ansible.plugins.action.normal
    import ansible.plugins.loader
    import ansible.utils.vars

    loader = ansible.plugins.loader.ActionModuleLoader()
    action = ansible.plugins.action.normal.ActionModule(loader=loader, task=None, connection=None, play_context=None,
                                                        shared_loader_obj=loader, templar=ansible.utils.vars.Templar(loader=loader),
                                                       loader_cache={}, task_vars={})

    # TEST 1
    # Test that a bad interpreter name throws a ValueError

# Generated at 2022-06-12 21:38:45.256884
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # Use the available library function to find the python interpreter
    from ansible.executor.discovery import discover_interpreter
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.module_utils.facts.system.distribution import Distribution
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.vars.manager import VariableManager

    # A fake inventory source
    # TODO: need actual hosts
    inventory = [u'localhost']

    # A fake variable manager, populated with the hostname
    variable_manager = VariableManager()
    variable_manager.extra_vars = {u'inventory_hostname': inventory[0]}

    # A fake play

# Generated at 2022-06-12 21:38:55.939963
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.plugins.action.normal import ActionModule as _ActionModule
    from ansible.executor.discovery import discover_interpreter

    class ActionModule(_ActionModule):
        def _low_level_execute_command(self, cmd, sudoable=True, in_data=None):
            return {'stdout': "PLATFORM\nLinux\nFOUND\n/usr/bin/python\nENDFOUND"}

    task_vars = dict()
    am = ActionModule(task_vars=task_vars)
    discover_interpreter(am, 'python', 'smart', task_vars)
    assert am._discovery_warnings, "Expected to find a warning"
    assert len(am._discovery_warnings) == 1, "Expected to find only one warning"
    assert am._

# Generated at 2022-06-12 21:39:06.095315
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.executor.action_plugins.discovery import discover_interpreter

    assert discover_interpreter(None, 'python', 'off', {}) is None
    assert discover_interpreter(None, 'python', 'legacy', {}) == u'/usr/bin/python'
    assert discover_interpreter(None, 'python', 'auto', {}) == u'/usr/bin/python'
    assert discover_interpreter(None, 'python', 'auto_legacy', {}) == u'/usr/bin/python'
    assert discover_interpreter(None, 'python', 'explicit', {}) == u'/usr/bin/python'

    assert discover_interpreter(None, 'python', 'silent_legacy', {}) == u'/usr/bin/python'

# Generated at 2022-06-12 21:39:15.259221
# Unit test for function discover_interpreter