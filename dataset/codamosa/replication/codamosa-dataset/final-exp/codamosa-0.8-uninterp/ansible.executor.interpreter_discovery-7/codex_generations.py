

# Generated at 2022-06-12 21:30:29.292637
# Unit test for function discover_interpreter
def test_discover_interpreter():

    from ansible.plugins.action.normal import ActionModule

    action_set = {
        "ANSIBLE_MODULE_ARGS": {
            "discovery_mode": "auto_legacy_silent",
            "interpreter": "python"
        },
        "ANSIBLE_MODULE_NAME": "setup"
    }

    test_truth = "testing"
    hostname = "127.0.0.1"
    action_set["inventory_hostname"] = hostname

    class TestActionModule(ActionModule):
        def _execute_module(self, tmp=None, task_vars=None, persist_files=True):
            return {'interp': self.discover_interpreter(action_set)}

    action_test = TestActionModule()

# Generated at 2022-06-12 21:30:36.933007
# Unit test for function discover_interpreter
def test_discover_interpreter():
    display.verbosity = 4


# Generated at 2022-06-12 21:30:47.142622
# Unit test for function discover_interpreter
def test_discover_interpreter():
    import ansible.executor.discovery as discovery
    from ansible.executor.task_result import TaskResult

    results = {'/usr/bin/python': u'/usr/bin/python/n',
               '/usr/bin/python3': u'/usr/bin/python3',
               '/usr/bin/python26': u'/usr/bin/python26'}

    test_data = {'python': {'*': u'/usr/bin/python',
                            'RedHat': {'6': u'/usr/bin/python26',
                                       '7': u'/usr/bin/python'},
                            'Debian': {'8': u'/usr/bin/python'},
                            'SUSE': {'13': u'/usr/bin/python3'}}}


# Generated at 2022-06-12 21:30:58.142804
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.plugins.action import ActionBase
    import ansible.plugins.action.set_fact
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor import PlaybookExecutor
    from ansible.utils.vars import combine_vars

    #from ansible.plugins.loader import action_loader

    #from ansible.plugins.action import ActionBase
    #from ansible.plugins.action.copy import ActionModule as CopyActionModule
    #from ansible.plugins.action.file import ActionModule as FileActionModule
    #from ansible.plugins.action

# Generated at 2022-06-12 21:31:06.665949
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # test unit, requires yaml installed on test system -- this could be fixed
    import os, yaml
    from ansible.executor.discovery import discover_interpreter
    from ansible.module_utils import distribution
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.module_utils.compat.version import LooseVersion
    from ansible.module_utils.facts.system.distribution import DistributionFactCollector
    from ansible.module_utils.facts.system.distribution import DistroParser
    from ansible.module_utils.facts.system.distribution import LinuxDistribution
    from ansible.module_utils.facts.system.distribution import PlatformParser
    from ansible.module_utils.facts.system.distribution import RedHatDistroParser

    # tests should be run

# Generated at 2022-06-12 21:31:10.872700
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # Test for discover bootstrap with no pythons in path
    task_vars = {"inventory_hostname": "localhost",
                "ansible_connection": "local"}
    result = discover_interpreter(None, 'python', 'auto', task_vars)
    assert result == '/usr/bin/python'

# Generated at 2022-06-12 21:31:17.070179
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.plugins.action.normal import ActionModule as _ActionModule

    class ActionModule(_ActionModule):

        def _low_level_execute_command(self, cmd, sudoable=False, in_data=None):

            if cmd.endswith('-y install ansible'):
                return {'stdout': u'', 'rc': 0}
            if cmd.startswith('command -v'):
                return {'stdout': u'FOUND\n/usr/bin/python\n/usr/bin/python3\n/usr/bin/python2\nENDFOUND\n', 'rc': 0}


# Generated at 2022-06-12 21:31:26.956997
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins.action import ActionBase
    from ansible.inventory.host import Host
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()

    context = PlayContext()
    context.become = False
    context.become_method = 'sudo'
    context.become_user = 'root'
    context.remote_addr = '127.0.0.1'
    context.connection = 'local'
    context.port = 22

    inventory = Host(name='127.0.0.1', port=context.port)
    task_vars = VariableManager()
    task_vars.extra_vars = {}

    actionbase = ActionBase()

# Generated at 2022-06-12 21:31:39.738921
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.module_utils.common.process import _fixup_perms_for_non_root_path
    import tempfile
    import os
    import shutil
    import sys
    import pytest

    class FakeAction(object):
        def __init__(self):
            self._connection = None
            self._discovery_warnings = []


# Generated at 2022-06-12 21:31:48.294796
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # begin
    print('begin: test_discover_interpreter')
    from ansible.module_utils.facts.hardware.base import Hardware
    from ansible.module_utils.facts.system.base import System

    class TestActionModule(object):
        _connection = None

    action = TestActionModule()
    action._low_level_execute_command = _test_discover_interpreter_low_level_execute_command
    action._connection = _test_discover_interpreter_connection()
    task_vars = dict()
    hardware_facts = Hardware()
    hardware_facts.gather(action._connection)
    task_vars['ansible_facts'] = hardware_facts.populate()
    system_facts = System()
    system_facts.gather(action._connection)
    task_v

# Generated at 2022-06-12 21:32:07.249370
# Unit test for function discover_interpreter
def test_discover_interpreter():
    test_action = ActionModule()

    def execute_command_mock(command, *args, **kwargs):
        res = {}
        if command == 'command -v python':
            res['stdout'] = '/usr/bin/python'

        if command == 'command -v python3':
            res['stdout'] = '/usr/lib/python3\n/usr/bin/python3'

        if command == 'command -v python2':
            res['stdout'] = '/usr/bin/python2'


# Generated at 2022-06-12 21:32:18.660732
# Unit test for function discover_interpreter
def test_discover_interpreter():
    action = object()
    interpreter_name = 'python'
    discovery_mode = 'auto'
    task_vars = dict()
    platform_python_map = dict()

    # empty bootstrap list
    bootstrap_python_list = []
    C.config.data[constants.DEFAULT_CONFIG_PATH]['INTERPRETER_PYTHON_FALLBACK'] = bootstrap_python_list
    with pytest.raises(InterpreterDiscoveryRequiredError) as err_info:
        discover_interpreter(action, interpreter_name, discovery_mode, task_vars)
    assert err_info.value.interpreter_name == interpreter_name
    assert err_info.value.discovery_mode == discovery_mode

# Generated at 2022-06-12 21:32:28.078428
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.module_utils import basic
    import os


# Generated at 2022-06-12 21:32:40.308220
# Unit test for function discover_interpreter
def test_discover_interpreter():
    import ansible.executor.action_plugins.discovery as discovery
    import ansible.playbook
    import ansible.plugins
    import ansible.inventory

    class ActionBaseMock(ansible.plugins.ActionBase):
        def __init__(self):
            self._discovery_warnings = []
            self._connection = ConnectionMock()
            self._task_vars = {}

        @staticmethod
        def _low_level_execute_command(cmd, sudoable=False, in_data=None):
            return {
                'stdout': 'PLATFORM\nLinux\nFOUND\n/usr/bin/python\nENDFOUND',
                'std_err': '',
                'rc': 0
            }


# Generated at 2022-06-12 21:32:48.009453
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # update the INTERPRETER_PYTHON_DISTRO_MAP
    def _get_config_value(value, *args, **kwargs):
        if value == 'INTERPRETER_PYTHON_DISTRO_MAP':
            return {'fedora': {'23': '/usr/bin/python', '24': '/usr/libexec/platform-python'}}
        raise ValueError('Unsupported config value: {}'.format(value))
    C.config.get_config_value = _get_config_value

    # change the config value INTERPRETER_PYTHON_FALLBACK to `env python`

# Generated at 2022-06-12 21:32:55.426648
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # pylint: disable=too-many-locals
    from ansible.executor.discovery.lib import InterpreterDiscoveryRequiredError
    from ansible.executor.task_result import TaskResult
    from ansible.plugins.action import ActionBase
    from ansible.vars.hostvars import HostVars

    class MockModule(object):
        def __init__(self, *args, **kwargs):
            pass

        @staticmethod
        def run(*args, **kwargs):
            return None

        def _execute_module(*args, **kwargs):
            return None

        def _execute_module_with_interpreter(*args, **kwargs):
            return None


# Generated at 2022-06-12 21:33:01.312142
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.plugins.action.normal import ActionModule
    action = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

    assert discover_interpreter(action, 'python', 'strict', dict()) is None



# Generated at 2022-06-12 21:33:10.615884
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.executor.task_result import TaskResult
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins.action import ActionBase

    def _execute_module(module_name=None, module_args=None, task_vars=dict(), persist_files=False):

        new_stdin = None
        if C.DEFAULT_SUDO_USER != 'root' and not os.path.exists(C.DEFAULT_SUDO_EXE):
            raise AnsibleError("%s does not exist" % C.DEFAULT_SUDO_EXE)
        sudo_user = task_vars.get('ansible_sudo_user')

# Generated at 2022-06-12 21:33:21.603882
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.executor.task_executor import TaskExecutor
    from ansible.executor.executor import Executor
    from ansible.executor.module_common import _load_params
    from ansible.vars.hostvars import HostVars
    from ansible.vars.hostvars import HostVarsVars
    from ansible.plugins.loader import action_loader
    from ansible.playbook.task import Task
    from ansible.playbook.handler import Handler
    from ansible.playbook.play import Play
    from ansible.playbook.block import Block
    from ansible.playbook.handler import Handler
    from ansible.inventory import Inventory
    from ansible.vars.manager import VariableManager
    from ansible.plugins.loader import module_loader

# Generated at 2022-06-12 21:33:32.040640
# Unit test for function discover_interpreter
def test_discover_interpreter():
    import unittest

    class TestDiscoverInterpreter(unittest.TestCase):
        """Unit test for function discover_interpreter"""

        class MockActionModule:
            def __init__(self):
                self.connection = TestDiscoverInterpreter.MockConnection(False)
                self.discovery_warnings = []

            def _low_level_execute_command(self, command_name, sudoable=None, in_data=None):
                assert(command_name in {"/usr/bin/python", "/usr/bin/python2", "/usr/local/bin/python2.7"})
                if command_name == "/usr/bin/python":
                    return {"stdout": u"PLATFORM\nLinux\nFOUND\n/usr/bin/python\nENDFOUND"}

# Generated at 2022-06-12 21:33:58.658174
# Unit test for function discover_interpreter
def test_discover_interpreter():

    task_vars = {}
    action = type('Action', (object,), {'_low_level_execute_command': _low_level_execute_command, '_discovery_warnings': []})()

    assert discover_interpreter(action, 'python', 'auto_legacy', task_vars) == u'/usr/bin/python'

    assert discover_interpreter(action, 'python2', 'auto_legacy', task_vars) == u'/usr/bin/python'

    assert discover_interpreter(action, 'python', 'best_match', task_vars) == u'/usr/bin/python2.7'

    assert discover_interpreter(action, 'python', 'best_match_silent', task_vars) == u'/usr/bin/python2.7'


# Generated at 2022-06-12 21:34:09.523609
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.module_utils._text import to_bytes
    from ansible.plugins.action import ActionBase

    # TODO: fix this up for testability
    class DummyActionBase(ActionBase):
        def __init__(self, task, connection, play_context, loader, templar, shared_loader_obj):
            self._task = task
            self._play_context = play_context
            self._loader = loader
            self._shared_loader_obj = shared_loader_obj
            self._templar = templar
            self._connection = connection
            self._low_level_execute_command = connection.exec_command
            self._discovery_warnings = []


# Generated at 2022-06-12 21:34:18.629479
# Unit test for function discover_interpreter
def test_discover_interpreter():
    import shutil
    import tempfile
    import unittest

    class TestDiscovery(unittest.TestCase):

        @staticmethod
        def _get_script_path(filename):
            return '{0}/{1}'.format(os.path.dirname(os.path.realpath(__file__)), filename)

        def setUp(self):

            self.loader = DataLoader()

            self.inventory = InventoryManager(loader=self.loader, sources='')
            self.variable_manager = VariableManager(loader=self.loader, inventory=self.inventory)

            self.host_vars = {
                'inventory_hostname': 'localhost'
            }

            # AnsibleHosts is a record-style object, so we can just set the
            # facts field to a dict object
            self.host = self

# Generated at 2022-06-12 21:34:26.855493
# Unit test for function discover_interpreter
def test_discover_interpreter():

    # global task_vars
    task_vars = {'inventory_hostname': 'localhost'}

    # FUTURE: mock action object?
    # action = None


# Generated at 2022-06-12 21:34:27.453767
# Unit test for function discover_interpreter
def test_discover_interpreter():
    pass

# Generated at 2022-06-12 21:34:39.533301
# Unit test for function discover_interpreter
def test_discover_interpreter():

    find_re = re.compile(r'(?s)PLATFORM[\r\n]+(.*)FOUND(.*)ENDFOUND')

    class _MockResult(object):
        def __init__(self, stdout, stderr, rc=0):
            self.stdout = stdout
            self.stderr = stderr
            self.rc = rc

    class _MockAction(object):
        def __init__(self, discovery_warnings):
            self._discovery_warnings = discovery_warnings

        def _low_level_execute_command(self, cmd, sudoable=False, in_data=None):
            display.debug(u"low_level_execute_command: {0}".format(to_text(cmd)), host='localhost')

# Generated at 2022-06-12 21:34:49.574358
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.module_utils.basic import AnsibleModule

    def _run(version, distro_map, expected, expected_warning=None):
        """
        Helper function to construct a test case

        :param version: target version to test
        :param distro_map: map of versions to interpreters to use as the platform-specific lookup data
        :param expected: string of the expected result
        :param expected_warning: expected warning, if one is expected. Should be a portion of the warning message, or None
        if the case should not produce a warning.
        """
        test_instance = AnsibleModule(argument_spec={})

        test_instance._discovery_warnings = []


# Generated at 2022-06-12 21:34:59.161594
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.executor.task_executor import TaskExecutor
    from ansible.playbook.task import Task
    import os

    action = TaskExecutor(Task(), {})
    action._low_level_execute_command = lambda x, y: {'stdout' : x, 'stderr' : 'stderr', 'rc' : 0}
    action._connection = type('connection', (object,), dict(has_pipelining=True))


# Generated at 2022-06-12 21:35:04.988613
# Unit test for function discover_interpreter

# Generated at 2022-06-12 21:35:11.023111
# Unit test for function discover_interpreter
def test_discover_interpreter():
    assert discover_interpreter(None, 'python', 'auto', None) == '/usr/bin/python'


if __name__ == '__main__':
    import sys
    import argparse

    parser = argparse.ArgumentParser(description='Test interpreter discovery script')
    parser.add_argument('-d', dest='debug', action='store_true', help='Enable debug output')
    args = parser.parse_args()

    if args.debug:
        display.verbosity = 4

    test_discover_interpreter()

# Generated at 2022-06-12 21:35:54.760378
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.executor.task_result import TaskResult
    action = TaskResult(host='localhost')
    task_vars = dict()

    # test exception match
    try:
        discover_interpreter(action, 'not-python', 'foo', task_vars)
    except ValueError as e:
        assert "unsupported" in to_text(e)

    try:
        discover_interpreter(action, 'python', 'foo', task_vars)
    except ValueError as e:
        assert "unsupported" in to_text(e)

    # test invalid response
    action._low_level_execute_command = lambda x, **kwargs: dict(stdout=u'not what we want')
    assert discover_interpreter(action, 'python', 'foo', task_vars) is None
   

# Generated at 2022-06-12 21:36:00.995472
# Unit test for function discover_interpreter
def test_discover_interpreter():
    check_result = True
    for test_case in ["auto_legacy_silent", "auto_silent"]:
        try:
            from ansible.executor.discovery_test import test_case2
            if test_case2.test_discover_interpreter(test_case) is not True:
                check_result = False
        except ImportError as e:
            print("test not available!")
            pass
    return check_result

# Generated at 2022-06-12 21:36:11.254577
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.mock.connection import Connection

    class FakeActionModule(object):
        def __init__(self, connection, warnings, discovery_mode):
            self._connection = connection
            self._discovery_warnings = warnings
            self.discovery_mode = discovery_mode
            self._connection.has_pipelining = True

        def _low_level_execute_command(self, cmd, sudoable=True, in_data=None):
            display.debug(u"===== CMD =====\n{0}".format(cmd))
            display.debug(u"===== IN_DATA =====\n{0}".format(in_data))
            return self._connection.independent_connection_test(cmd, sudoable, in_data)


# Generated at 2022-06-12 21:36:19.512877
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.executor.task_result import TaskResult

    result = TaskResult(None, None)
    result.stdout = u''
    result.stderr = u''
    result.module_stdout = u''
    result.module_stderr = u''
    result._ansible_no_log = False
    result._ansible_item_result = False
    result._ansible_ignore_errors = False
    result._ansible_delegated_vars = {}
    result._ansible_parsed = False
    result._ansible_failed = False
    result._ansible_item_label = None
    result._ansible_action = None
    result._ansible_async_seconds = 0
    result._ansible_fact_cacheable = False
    result._ansible_facts = {}


# Generated at 2022-06-12 21:36:31.258557
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.plugins.action.script import ActionModule
    import ansible.constants as C

    # Mock out the connection and low-level execute_command to prevent
    # running real commands on the local system
    class MyConnection(object):
        def has_pipelining(self):
            return True
    class MyTask(object):
        _connection = MyConnection()
        _low_level_execute_command = staticmethod(lambda x, y, z: {'stdout': x})
        def __init__(self, hostname):
            self._play_context = {'inventory_hostname': hostname}
    class MyActionModule(ActionModule):
        def __init__(self, task):
            self._task = task
            self._discovery_warnings = []
    C.config = C.ConfigParser()

    #

# Generated at 2022-06-12 21:36:40.024860
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.executor.task_result import TaskResult

    # test discovery of multiple interpreters
    success_result = TaskResult('<test hostname>', '<test module name>')
    success_result._result['stdout'] = u"""PLATFORM
Linux
FOUND
/usr/bin/python2
/usr/bin/python
ENDFOUND
"""
    action = FakeAction()
    interpreter = discover_interpreter(action, 'python', 'auto', {})
    action._low_level_execute_command.assert_called_once_with("command -v '/usr/bin/python2'")
    assert interpreter == u'/usr/bin/python2'

    # test silent discovery
    action = FakeAction()
    interpreter = discover_interpreter(action, 'python', 'auto_silent', {})
   

# Generated at 2022-06-12 21:36:52.325681
# Unit test for function discover_interpreter
def test_discover_interpreter():
    """
    Test the discover_interpreter function for a simple case.
    """

    plugin_name = "action_plugin.py"
    class_name = "Executor"

    class Executor:
        def __init__(self):
            self._connection = None
            self._connection_info = None
            self._loader = None
            self._templar = None
            self._shared_loader_obj = None
            self._discovery_warnings = []

        def set_loader(self, loader):
            self._loader = loader

        def set_connection(self, connection):
            self._connection = connection

        def _low_level_execute_command(self, cmd, sudoable=False, in_data=None):
            """
            Executes a command via low-level run with a lock and a timer
            """


# Generated at 2022-06-12 21:37:01.638790
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.plugins.action import ActionBase
    from ansible.plugins.action.net_tools import ActionModule as NetAction
    from ansible.module_utils.connection import ConnectionBase
    from ansible.plugins.connection import network_cli

    class TestConnection(ConnectionBase):
        def set_host_overrides(self, host):
            self.has_pipelining = True
            # FUTURE: add a test with pipelining disabled

    class TestModule(NetAction):
        def run(self, tmp=None, task_vars=None):
            super(TestModule, self).run(tmp, task_vars)

    class TestAction(ActionBase):
        def _execute_module(self, tmp=None, task_vars=None):
            # FUTURE: actually test something?
            pass

    test

# Generated at 2022-06-12 21:37:10.613714
# Unit test for function discover_interpreter
def test_discover_interpreter():
    def fake_low_level_execute_command(cmd, in_data=None, sudoable=True):
        if cmd.startswith('echo '):
            return dict(stdout='PLATFORM\nDarwin\nFOUND\n/usr/bin/python\n/usr/bin/python\nENDFOUND\n')
        if cmd.startswith('/usr/bin/python'):
            return dict(stdout=json.dumps({'osrelease_content': u'ID=macos\nVERSION_ID=10.14.6\n'}))

    import ansible.plugins.action
    action_plugin = ansible.plugins.action.ActionBase()
    action_plugin._low_level_execute_command = fake_low_level_execute_command

# Generated at 2022-06-12 21:37:16.847730
# Unit test for function discover_interpreter
def test_discover_interpreter():
    """Test discover interpreter function

    :return:
    """
    from io import StringIO
    class ActionTest:
        def __init__(self):
            self._discovery_warnings = []
            self._connection = Connection()

        @property
        def connection(self):
            return self._connection

        def _low_level_execute_command(self, command, sudoable, in_data=None):
            self._last_command = command
            fake_res = dict(
                stdout=fake_responses[command][0],
                stderr=fake_responses[command][1],
            )
            return fake_res
    class Connection:
        def __init__(self):
            self.has_pipelining = True


# Generated at 2022-06-12 21:38:38.846392
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins import module_loader
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager

    # this should run the discovery_warnings several times and end on the second one.

    # in order to mock a task, we only need to include the bits we care about...
    class test_task:
        def __init__(self, action):
            self._action = action
            self._discovery_warnings = []

        def _low_level_execute_command(self, interp, sudoable=False, in_data=None):
            if interp == "commandlist":
                return dict(stdout=u'python2.7')

# Generated at 2022-06-12 21:38:40.064747
# Unit test for function discover_interpreter
def test_discover_interpreter():
    discover_interpreter('test', 'python', 'test', 'test')



# Generated at 2022-06-12 21:38:50.160894
# Unit test for function discover_interpreter
def test_discover_interpreter():
    """
    Test function for discover_interpreter

    Test Case 1:
    Test Case 2:
    Test Case 3:
    """
    import mock
    from ansible.plugins.action.normal import ActionModule as _ActionModule
    from ansible.module_utils import basic
    import ansible.config


# Generated at 2022-06-12 21:38:59.950741
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.plugins.action.discovery import ActionModule as DiscoveryAction
    from ansible.module_utils.common.collections import ImmutableDict
    task_vars = ImmutableDict({})

    action = DiscoveryAction(task=dict(), connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

    # Simulate no interpreter present on host
    action._low_level_execute_command = lambda x, sudoable=False, in_data=None: ImmutableDict({'stdout': u'PLATFORM\nUNKNOWN\nFOUND\nENDFOUND'})
    res = discover_interpreter(action=action, interpreter_name=u'python', discovery_mode=u'auto_legacy_silent', task_vars=task_vars)

# Generated at 2022-06-12 21:39:09.836260
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # Here we update the value of INTERPRETER_PYTHON_FALLBACK and config.ini at runtime to run the unit test.
    # We need to do this otherwise we will not be able to run the unit test as the value at playbooks/config.ini
    # will be used for running any playbook.
    # We make sure that the original value of config.ini is restored after the unit test has finished.
    # Also we make sure that the variable INTERPRETER_PYTHON_DISTRO_MAP is not changed during the unit test.
    # That way, the test can run without changing the current behaviour of interpreter discovery, which is expected
    # by the rest of the code.
    original_interpreter_python_fallback = C.DEFAULT_INTERPRETER_PYTHON_FALLBACK

# Generated at 2022-06-12 21:39:14.200415
# Unit test for function discover_interpreter
def test_discover_interpreter():
    assert discover_interpreter(None, 'python', 'auto_silent', dict()) == u'/usr/bin/python'
    assert discover_interpreter(None, 'python', 'auto_silent', dict(config=dict(dict(INTERPRETER_PYTHON_FALLBACK=['/tmp/doesntexist'])))) == u'/usr/bin/python'

# Generated at 2022-06-12 21:39:20.931111
# Unit test for function discover_interpreter
def test_discover_interpreter():
    class FakeLoaderModule():
        def __init__(self, *args, **kwargs):
            pass

        def _execute_module(self, *args, **kwargs):
            return {
                'stdout': u"PLATFORM\nLinux\nFOUND\n"
                          u"/usr/bin/python\n"
                          u"/usr/bin/python2\n"
                          u"/usr/bin/python3\n"
                          u"ENDFOUND",
                'stderr': u'',
                'rc': 0,
            }

    class FakeAction():
        def __init__(self, *args, **kwargs):
            pass

        @classmethod
        def get_loader_module(cls, *args, **kwargs):
            return FakeLoaderModule()


# Generated at 2022-06-12 21:39:30.841304
# Unit test for function discover_interpreter

# Generated at 2022-06-12 21:39:33.024208
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # For now, just verify the existence of the function
    assert callable(discover_interpreter)

# Generated at 2022-06-12 21:39:43.945220
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible_collections.ansible.netcommon.tests.unit.compat.mock import patch
    from ansible.module_utils.six import b, StringIO

    class MockAction:
        def __init__(self):
            self._discovery_warnings = []
            self._connection = MockConnection()

        def set_connection(self, connection):
            self._connection = connection

        def _low_level_execute_command(self, command, sudoable=None, in_data=None):
            # _low_level_execute_command is expected to be called twice,
            # first with shell_bootstrap and then with Python script
            # so we use a counter to mock the responses
            if self._connection.has_pipelining:
                if self._connection.call_count == 0:
                    self._connection.call_