

# Generated at 2022-06-12 21:30:25.251313
# Unit test for function discover_interpreter
def test_discover_interpreter():

    # Unit tests will use a connection plugin that supports pipelining
    class MockConnection:
        @property
        def has_pipelining(self):
            return True

    # Mock the low-level command execution interface to return canned responses
    def _low_level_execute_command(command, sudoable=False, in_data=None):
        if command == 'echo PLATFORM; uname; echo FOUND; command -v \'/usr/bin/python\'; echo ENDFOUND':
            result = dict(stdout=u'PLATFORM\nLinux\nFOUND\n/usr/bin/python\nENDFOUND',
                          stderr=u'',
                          rc=0)
        elif command == '/usr/bin/python':
            # first thing we get from the platform data script is the interpreter
            result = dict

# Generated at 2022-06-12 21:30:35.216518
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.plugins.action.normal import ActionModule as _ActionModule

    class ActionModule(_ActionModule):
        def run(self, *args, **kwargs):
            self._discovery_warnings = list()
            return super(ActionModule, self).run(*args, **kwargs)

        def _get_shebang(self, *args, **kwargs):
            return super(ActionModule, self)._get_shebang(*args, **kwargs)

        def _low_level_execute_command(self, *args, **kwargs):
            return {u'stdout': u'PLATFORM\nlinux\nFOUND\n/usr/bin/python\nENDFOUND'}


# Generated at 2022-06-12 21:30:45.704061
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # Define function variables
    action = dict()
    interpreter_name = 'python'
    discovery_mode = 'auto'
    task_vars = dict()

# Generated at 2022-06-12 21:30:56.857773
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # Input, try to discover Python interpreter on system
    task_vars = {'ansible_python_interpreter_discovery_mode': 'auto'}

    # Output, discovered type and version strings
    dist_name = 'unknown'
    dist_version = 'unknown'


# Generated at 2022-06-12 21:31:04.737655
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.playbook.play import Play
    from ansible.playbook.role import Role
    from ansible.playbook.task import Task
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.parsing.vault import VaultLib
    import os

    class Host:
        def __init__(self, name):
            self.name = name
            self.ip_address = '%s.%s' % (name, '100')
            self.port = 22
            self.ansible_python_interpreter = '/usr/bin/python'


# Generated at 2022-06-12 21:31:14.285799
# Unit test for function discover_interpreter
def test_discover_interpreter():
    import os

    mock_action = type('ActionModule', (object,), {'_low_level_execute_command': type('P', (object,), {'get': lambda _, k, d=None: d})()})()
    mock_task_vars = {'inventory_hostname': 'localhost'}
    mock_interpreter_name = 'python'
    mock_discovery_mode = 'auto_silent'
    mock_bootstrap_python_mapping = {'python2.6': ['python2.6'], 'python2.7': ['python2.7'], 'python3': ['python3']}
    mock_config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'mock_config.cfg')


# Generated at 2022-06-12 21:31:24.975187
# Unit test for function discover_interpreter
def test_discover_interpreter():
    import copy
    import sys
    import unittest
    import ansible.executor.task_queue_manager as tqm
    import ansible.plugins.action as action
    import ansible.vars.manager
    import ansible_collections.ansible.builtin.plugins.module_utils.python as py
    from ansible.executor.process.discovery import InterpreterDiscoveryRequiredError, discover_interpreter
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins import module_loader
    from ansible.vars.hostvars import HostVarsVarsManager

    # Set up a loop that runs through

# Generated at 2022-06-12 21:31:37.927568
# Unit test for function discover_interpreter
def test_discover_interpreter():
    class MyActionModule:
        def __init__(self):
            self._discovery_warnings = []

    class MyConnection:
        has_pipelining = True

        def _low_level_execute_command(self, command, sudoable=False, in_data=None):
            if command == u"command -v 'python2.6'":
                return {'stdout': '/usr/bin/python2.6\n/usr/bin/python'}
            elif command == u"command -v 'python2.7'":
                return {'stdout': '/usr/bin/python2.7\n/usr/bin/python'}

# Generated at 2022-06-12 21:31:47.103630
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # test for full coverage for _version_fuzzy_match
    assert _version_fuzzy_match('1.1.1', {'1.1.0': u'1.1.0', '1.2.0': u'1.2.0'}) == u'1.1.0'
    assert _version_fuzzy_match('1.2.1', {'1.1.0': u'1.1.0', '1.2.0': u'1.2.0'}) == u'1.2.0'
    assert _version_fuzzy_match('1.3.1', {'1.1.0': u'1.1.0', '1.2.0': u'1.2.0'}) == u'1.2.0'
    assert _version_f

# Generated at 2022-06-12 21:31:57.649971
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.plugins.action import ActionBase
    action = ActionBase()
    action.execute_module = lambda *args, **kwargs: {u'stdout': u'PLATFORM\nLinux\nFOUND\n/usr/bin/python\nENDFOUND'}
    action.__dict__['_connection'].has_pipelining = True

    # TODO: do an integration test where the bootstrap script needs to be run?
    task_vars = {}
    result = discover_interpreter(action, interpreter_name='python', discovery_mode='auto_legacy', task_vars=task_vars)
    assert result == '/usr/bin/python'


# Generated at 2022-06-12 21:32:17.655695
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.executor.module_common import _mock_module_params
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins.action import ActionBase

    class MockAction(ActionBase):
        def __init__(self):
            self._discovery_warnings = []

        def _display(self, msg, color=None):
            self._discovery_warnings.append(msg)

        def _discovery_fail(self, msg):
            self._discovery_warnings.append(msg)


# Generated at 2022-06-12 21:32:27.596091
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.executor.discovery import discover_interpreter
    from ansible.module_utils.basic import AnsibleModule
    m = AnsibleModule(name='discover_interpreter', argument_spec={})
    m._debug = True
    m._low_level_execute_command = lambda *args, **kwargs: {'stdout': 'PLATFORM\nLinux\nFOUND\n/usr/bin/python\n/usr/bin/python2\n/usr/bin/python3\n/usr/bin/python2.7\nENDFOUND',
                                                            'stderr': '',
                                                            'rc': 0}
    assert discover_interpreter(m, 'python', 'auto_legacy_silent', {}) == '/usr/bin/python'

    m._low

# Generated at 2022-06-12 21:32:30.331758
# Unit test for function discover_interpreter
def test_discover_interpreter():

    result = discover_interpreter(None, 'python', 'auto', {'inventory_hostname': 'localhost'})

    assert result == u'/usr/bin/python'


# Generated at 2022-06-12 21:32:42.194459
# Unit test for function discover_interpreter
def test_discover_interpreter():
    class TestAction(object):
        def __init__(self):
            self._discovery_warnings = []
            self._connection = self  # hack to avoid a lot of stubbing for our test

        def _low_level_execute_command(self, command, **kwargs):
            res = {'stdout': command, 'rc': 0}
            return res

    # Test no interpreter found
    task_vars = {'inventory_hostname': 'host1', 'ansible_connection': 'local'}
    action = TestAction()
    res = discover_interpreter(action, 'python', 'auto_legacy_silent', task_vars)
    assert(res == u'/usr/bin/python')

# Generated at 2022-06-12 21:32:51.726929
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.executor.task_executor import TaskExecutor

    def _mock_execute_command(cmd, sudoable=None, in_data=None):
        res = {'stdout': '', 'stderr': ''}

        if in_data:
            res['stdout'] = json.dumps({'platform_dist_result': ['RedHatEnterpriseServer', '7.1', 'Maipo'],
                                        'osrelease_content': 'NAME="Red Hat Enterprise Linux Server"\n'
                                                             'VERSION="7.1 (Maipo)"\n'
                                                             'ID="rhel"\n'
                                                             'ID_LIKE="fedora"'})
            return res


# Generated at 2022-06-12 21:33:04.324195
# Unit test for function discover_interpreter
def test_discover_interpreter():
    assert discover_interpreter(None, 'python', 'auto', {}) == '/usr/bin/python', "Auto discovery does not work"
    assert discover_interpreter(None, 'python', 'force', {}) == '/usr/bin/python', "Force discovery does not work"
    assert discover_interpreter(None, 'python', 'auto_legacy', {}) == '/usr/bin/python', "Auto Legacy discovery does not work"
    assert discover_interpreter(None, 'python', 'auto_silent', {}) == '/usr/bin/python', "Auto Legacy discovery does not work"
    assert discover_interpreter(None, 'python', 'auto_silent_legacy', {}) == '/usr/bin/python', "Auto Legacy discovery does not work"

# Generated at 2022-06-12 21:33:12.184140
# Unit test for function discover_interpreter
def test_discover_interpreter():
    import mock

    # Mock necessary attribute of ActionBase
    class FakeActionBase(object):
        def __init__(self):
            self._connection = mock.Mock()
            self._discovery_warnings = []

        @property
        def _low_level_execute_command(self):
            return mock.Mock()

    # Mock return value of _low_level_execute_command
    class FakeResponse(object):
        def __init__(self, stdout):
            self.stdout = stdout

    # Interpreter Discovery for Ubuntu Linux
    def test_discover_interpreter_ubuntu():
        interpreter_name = 'python'
        discovery_mode = 'auto_legacy_silent'

        action = FakeActionBase()
        action._connection.has_pipelining = True
        action._low_level_

# Generated at 2022-06-12 21:33:13.387317
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # Nothing yet!
    pass

# Generated at 2022-06-12 21:33:24.571666
# Unit test for function discover_interpreter
def test_discover_interpreter():
    """Test discovery of interpreters"""
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins.action import ActionBase

    class TestAction(ActionBase):

        def _discovery_warnings(self):
            return []

        def _discovery_warn(self, msg):
            self._discovery_warnings().append(msg)

        def _discovery_exception(self, exc):
            self._discovery_warnings().append(exc)

    class TestPlayContext(PlayContext):
        def __init__(self):
            super(TestPlayContext, self).__init__()
            self.prompt = None
            self.verbosity = 3
            self.check_mode = False
            self.become = False
            self.become_method = False
            self.become_user

# Generated at 2022-06-12 21:33:34.373185
# Unit test for function discover_interpreter
def test_discover_interpreter():
    class ActionModule:
        def __init__(self):
            self._low_level_execute_command_result = None
            self._low_level_execute_command_called = False
            self._discovery_warnings = []

        def _low_level_execute_command(self, cmd, sudoable, in_data=None):
            if in_data:
                raise Exception("Pipelining not supported!")

            self._low_level_execute_command_called = True
            return self._low_level_execute_command_result

    action = ActionModule()

    host = 'localhost'

    def _run_discovery(discovery_mode, low_level_execute_command_result, expected_path):
        action._low_level_execute_command_result = low_level_execute_command_result
        action._discovery

# Generated at 2022-06-12 21:33:52.321878
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # TODO: unit test for warning(?) output
    from ansible.plugins.action.__init__ import ActionBase
    action = ActionBase()

    import ansible.executor.discovery.interpreter
    assert (ansible.executor.discovery.interpreter.discover_interpreter(
        action, 'python', 'auto_legacy', {
            'inventory_hostname': 'localhost',
            'ansible_distribution': 'CentOS',
            'ansible_distribution_version': '7.1'
        }) == '/usr/bin/python'
    )

# Generated at 2022-06-12 21:33:52.903156
# Unit test for function discover_interpreter
def test_discover_interpreter():
    pass

# Generated at 2022-06-12 21:34:03.964776
# Unit test for function discover_interpreter
def test_discover_interpreter():
    def test_discovery(discovery_mode, interpreter_name, task_vars, expected_python):
        try:
            python = discover_interpreter(action, interpreter_name, discovery_mode, task_vars)
            assert(python == expected_python)
        except InterpreterDiscoveryRequiredError as err:
            assert(expected_python is None)
            assert(err.interpreter_name == interpreter_name)
            assert(err.discovery_mode == discovery_mode)
        except Exception as err:
            assert(False)

    import mock
    import sys

    if sys.version_info.major == 2:
        reload(mock)

    # Test shell_bootstrap response
    # Note - this test case needs to be changed if the shell_bootstrap command changes

    # Test python discovery
    # Note -

# Generated at 2022-06-12 21:34:13.420236
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # test case for `discover_interpreter`
    from ansible.playbook.play_context import PlayContext

    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor

    from ansible.plugins.loader import module_loader
    from ansible.plugins.action.normal import ActionModule as _ActionModule

    class ActionModule(_ActionModule):
        pass

    # NOTE: running unit test in your local terminal use the following command
    # python -m pytest test/unit/executor/test_interpreter.py -s -v

    # NOTE: if you don't how to run unit test,
    #       please reference https://github.com/ansible/ansible/tree/devel/test/units/modules

    # config variables


# Generated at 2022-06-12 21:34:22.266105
# Unit test for function discover_interpreter
def test_discover_interpreter():
    task_vars = dict()
    # Empty map
    python_map = dict()
    task_vars['ansible_python_interpreter_distro_map'] = python_map
    interpreter_list = ['python3', 'python']
    task_vars['ansible_python_interpreter_fallback'] = interpreter_list
    interpreter_name = 'python'
    discovery_mode = 'auto_legacy_silent'
    action = object()

    interp = discover_interpreter(action, interpreter_name, discovery_mode, task_vars)

    assert interp == '/usr/bin/python'

    # Map with 1 entry
    python_map['redhat'] = {'6.1': '/usr/bin/python'}

# Generated at 2022-06-12 21:34:28.291036
# Unit test for function discover_interpreter
def test_discover_interpreter():
    """
    Unit test for function discover_interpreter
    """
    assert (discover_interpreter(None, 'python', 'auto_legacy_silent', None) == '/usr/bin/python')
    assert (discover_interpreter(None, 'python2', 'auto_legacy_silent', None) == '/usr/bin/python')
    assert (discover_interpreter(None, 'python', 'auto_legacy', None) == '/usr/bin/python')
    assert (discover_interpreter(None, 'python', 'auto', None) == '/usr/bin/python')
    assert (discover_interpreter(None, 'python2', 'auto', None) == '/usr/bin/python')

    # testing with an actual ActionBase class would be better, but I need to mock it


# Generated at 2022-06-12 21:34:39.781423
# Unit test for function discover_interpreter
def test_discover_interpreter():
    failed = "failed"
    interpreter_name = 'python'
    action = None
    discovery_mode = 'auto_legacy_silent'
    task_vars = { constants.INVENTORY_HOSTNAME: None }

    display.vvv(msg=u"Attempting {0} interpreter discovery".format(interpreter_name), host=None)

    display.debug(u"found interpreters: {0}".format([]), host=None)

    if not found_interpreters:
        display.debug(u"raw interpreter discovery output: {0}".format(raw_stdout), host=None)
        assert(False)

if __name__ == "__main__":
    test_discover_interpreter()

# Generated at 2022-06-12 21:34:49.858238
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.module_utils.connection import Connection
    from ansible.plugins.action import ActionBase

    connection = Connection(None)
    action = ActionBase(connection, C.DEFAULT_MODULE_NAME, '/', 'discovery', False, False)


# Generated at 2022-06-12 21:34:55.188989
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.plugins import action
    action_obj = action.ActionModule(task=dict(), connection=dict(), play_context=dict(), loader=None, templar=None, shared_loader_obj=None)
    result = discover_interpreter(action_obj, 'python', 'auto', dict())
    assert result.startswith('/usr')
    assert result.endswith('python')

# Generated at 2022-06-12 21:35:03.172205
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.executor.task_result import TaskResult
    from ansible.executor.task_queue_manager import TaskQueueManager

    res = TaskResult({'cmd': 'echo PLATFORM; uname; echo FOUND; /usr/bin/python; /usr/bin/python3; echo ENDFOUND'})
    res._stdout = u'''PLATFORM
Linux
FOUND
/usr/bin/python
/usr/bin/python3
ENDFOUND'''
    action = TaskQueueManager()
    action._discovery_warnings = []
    action._low_level_execute_command = lambda x: res
    action._connection = type('connection', (object,), {'has_pipelining': True})()


# Generated at 2022-06-12 21:35:23.344480
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.executor.task_result import TaskResult
    from ansible.executor.module_common import ViewModifyModule
    from ansible.plugins.action import ActionBase
    from ansible.executor.action_plugins.script import ActionModule as ScriptAction
    from ansible.executor.play_iterator import PlayIterator

    fake_vars=dict(
        ansible_python_interpreter='/usr/bin/python'
    )

    # mocking up a task object
    task = dict(
        action=dict(
            module_name='script',
            module_args='/bin/true',
            module_vars=dict(
                ansible_python_interpreter='/usr/bin/python'
            )
        )
    )


# Generated at 2022-06-12 21:35:34.099584
# Unit test for function discover_interpreter
def test_discover_interpreter():

    config = {
        'INTERPRETER_PYTHON_DISTRO_MAP':
            {
                "centos":
                    {
                        "6": "/usr/libexec/platform-python",
                        "7": "/usr/bin/platform-python-2.7",
                    },
                "ubuntu":
                    {
                        "10.04": "/usr/lib/python2.6",
                        "12.04": "/usr/lib/python2.7",
                        "14.04": "/usr/bin/python2.7",
                    },
                "rhel":
                    {
                        "7": "/usr/bin/python2.7",
                    },
            },
        'INTERPRETER_PYTHON_FALLBACK':
            ['/usr/bin/python']
    }


# Generated at 2022-06-12 21:35:45.522520
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.plugins import interpreter_discovery
    from ansible.plugins.action import ActionBase

    try:
        find_interpreter = interpreter_discovery.find_interpreter
    except AttributeError:
        # older Ansible
        find_interpreter = interpreter_discovery.InterpreterDiscovery

    class MyAction(ActionBase):
        def _low_level_execute_command(self, cmd, in_data=None, sudoable=True):
            return dict(stdout='', stderr='')

    class MyTaskVars:
        def __init__(self):
            self.inventory_hostname = 'testhost'
            self.config = {}


# Generated at 2022-06-12 21:35:54.947880
# Unit test for function discover_interpreter
def test_discover_interpreter():
    try:
        import ansible.executor.task_executor.action
    except ImportError:
        import ansible.utils.display
        ansible.utils.display.Display().warning(
            'Unable to import ansible.executor.task_executor.action. Skipping test_discover_interpreter.')
        return

    action = ansible.executor.task_executor.action.ActionModule(None, None, None)
    interpreter_name = 'python'
    discovery_mode = 'auto_legacy_silent'

# Generated at 2022-06-12 21:36:05.893679
# Unit test for function discover_interpreter
def test_discover_interpreter():
    import pytest
    from ansible.errors import AnsibleError
    from ansible.executor.discovery import (
        discover_interpreter,
        InterpreterDiscoveryRequiredError,
    )
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.plugins.action.normal import ActionModule
    from ansible.module_utils._text import to_text

    pytest.importorskip('platform')

    class FakeRunner(object):
        def __init__(self):
            self.host_vars = ImmutableDict([(u'1.1.1.1', ImmutableDict()), (u'2.2.2.2', ImmutableDict())])


# Generated at 2022-06-12 21:36:13.377534
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from copy import deepcopy

    # FUTURE: add more test cases for various Linux platforms, plus test cases for non-Linux platforms
    ev = deepcopy(C.DEFAULT_CUSTOM_VARS)
    ev['ansible_python_interpreter'] = u'/usr/bin/python'
    fail_msg = u"Fallback Python interpreter discovery failed for host {0}: {1}"


# Generated at 2022-06-12 21:36:14.417749
# Unit test for function discover_interpreter
def test_discover_interpreter():
    raise NotImplementedError

# Generated at 2022-06-12 21:36:15.478030
# Unit test for function discover_interpreter
def test_discover_interpreter():
    raise NotImplementedError('test_discover_interpreter needs to be written')

# Generated at 2022-06-12 21:36:21.736229
# Unit test for function discover_interpreter
def test_discover_interpreter():
    assert discover_interpreter(None, 'python', 'auto_legacy_silent', None) == u'/usr/bin/python'
    assert discover_interpreter(None, 'python', 'auto_legacy_warn', None) == u'/usr/bin/python'
    assert discover_interpreter(None, 'python', 'auto_silent', None) == u'/usr/bin/python'
    assert discover_interpreter(None, 'python', 'auto_warn', None) == u'/usr/bin/python'
    assert discover_interpreter(None, 'python', 'force_silent', None) == u'/usr/bin/python'
    assert discover_interpreter(None, 'python', 'force_warn', None) == u'/usr/bin/python'

# Generated at 2022-06-12 21:36:28.141863
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.module_utils.common.collections import ImmutableDict
    import tempfile

    tempdir = tempfile.mkdtemp(prefix='ansible_test_python_discovery')

    def setup_tempdir(platform, os_release='', platform_dist_result=None, except_value=None, version='1'):
        class ActionModule:
            class LowLevelExecuteCommand:
                def __init__(self, result):
                    self.result = result

                def __call__(self, executable, sudoable=False, in_data=None, executable_args=None):
                    return self.result

            class Connection:
                def __init__(self, has_pipelining):
                    self.has_pipelining = has_pipelining


# Generated at 2022-06-12 21:36:54.555455
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.module_utils._text import to_bytes
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins.loader import module_loader
    from ansible.plugins.action import ActionBase

    class TestAction(ActionBase):
        def _discovery_warnings(self):
            return []

        def _display_warnings(self):
            return []

        def _low_level_execute_command(self, *args, **kwargs):
            return {}

    def _do_test(config, task_vars, action, interpreter_name, discovery_mode, expected_interpreter):
        d = discover_interpreter(action, interpreter_name, discovery_mode, task_vars)
        assert d == expected_interpreter
        assert expected_interpreter in action._low_level

# Generated at 2022-06-12 21:37:05.002982
# Unit test for function discover_interpreter
def test_discover_interpreter():
    import mock

    if not hasattr(mock, 'mock_open'):
        # not in Python 2.7, so we can't test this
        return

    action = MockAction()

# Generated at 2022-06-12 21:37:12.914793
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.plugins.action.normal import ActionModule as _ActionModule
    from ansible.template import Templar

    class ActionModule(_ActionModule):
        def _execute_module(self, module_name=None, module_args=None, task_vars=None, wrap_async=None, inject=None):
            if inject is None:
                inject = {}
            if task_vars is None:
                task_vars = dict()
            self._display.debug("injected: %s" % inject)
            if not task_vars.get('ansible_facts'):
                task_vars['ansible_facts'] = dict()

            if not isinstance(inject, dict):
                raise Exception('invalid inject value')

            facts = task_vars['ansible_facts']
            # add any facts from the

# Generated at 2022-06-12 21:37:20.541293
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.module_utils.facts.system.distribution import Distribution
    import contextlib

    # Instance of a FactCacheModule
    fact_cache_module = Distribution()

    # Return a dict containing the distribution facts without any flags
    result = fact_cache_module.get_facts(None, {}, {})

    # Construct the task_vars dict so that it can be passed as a parameter to the function
    fact_dict = result.get('ansible_facts')

    # Function discover_interpreter returns python2.7 by default
    assert discover_interpreter(None, 'python', 'auto_silent', task_vars=fact_dict) == u'/usr/bin/python2.7'



# Generated at 2022-06-12 21:37:27.417935
# Unit test for function discover_interpreter
def test_discover_interpreter():
    try:
        import mock
        from ansible.plugins.action.script import ActionModule, _compute_environment
    except ImportError:
        pytest.skip("mock module is not installed")


# Generated at 2022-06-12 21:37:35.272167
# Unit test for function discover_interpreter

# Generated at 2022-06-12 21:37:44.334149
# Unit test for function discover_interpreter
def test_discover_interpreter():
    import ansible.plugins.loader as plugin_loader

    class DummyAction(object):
        def __init__(self):
            self._discovery_warnings = []

        def _low_level_execute_command(self, command, sudoable=True, in_data=None):
            return {'stdout': 'PLATFORM\nLinux\nFOUND\n/usr/bin/python\nENDFOUND'}

        def _connection_set_shell_type(self, shell='sh'):
            pass

        def _connection_supports_pipelining(self):
            return True

        def get_shell_type(self):
            pass

    class DummyModule(object):
        def __init__(self):
            self.action = DummyAction()

# Generated at 2022-06-12 21:37:56.468996
# Unit test for function discover_interpreter
def test_discover_interpreter():
    print("test discover_interpreter function start!")
    # test not impletement
    action = []
    task_vars = []
    res = discover_interpreter(action, 'python2', 'auto', task_vars)
    print("test discover_interpreter res: " + str(res))
    assert res is None

    # test not impletement
    res = discover_interpreter(action, 'python2', 'auto', [])
    print("test discover_interpreter res: " + str(res))
    assert res is None

    # test not impletement
    res = discover_interpreter(action, 'python', 'auto', [])
    print("test discover_interpreter res: " + str(res))
    assert res is None

# Generated at 2022-06-12 21:38:06.289081
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # pylint: disable=unused-argument
    # pylint: disable=too-many-locals

    from ansible.plugins.action import ActionBase

    class FakeAction(ActionBase):
        def __init__(self):
            # pylint: disable=abstract-class-instantiated
            self._low_level_execute_command = None
            self._discovery_warnings = []
            self._connection = FakeConnection()

    class FakeConnection:
        def __init__(self):
            self.has_pipelining = True

    # pylint: disable=bad-continuation,line-too-long

# Generated at 2022-06-12 21:38:15.919077
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # Preparing test cases
    res_1 = {'stdout': u'PLATFORM\nLinux\nFOUND\n/usr/bin/python2.6\n/usr/bin/python3\nENDFOUND\n', 'rc': 0}
    res_1_1 = {'stdout': u'PLATFORM\nLinux\nFOUND\n/usr/bin/python2.7\n/usr/bin/python3\nENDFOUND\n', 'rc': 0}
    res_2 = {'stdout': u'PLATFORM\nLinux\nFOUND\n/usr/bin/python3\nENDFOUND\n', 'rc': 0}

# Generated at 2022-06-12 21:39:00.284213
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # test case for Linux
    platform_info = {
        'platform_uname': ['Linux'],
        'platform_dist_result': ['', '', ''],
        'osrelease_content': ['NAME="Ubuntu"\nVERSION="16.04.5 LTS (Xenial Xerus)"\n', '']
    }
    discovered_interpreter = discover_interpreter(platform_info, 'python')
    assert discovered_interpreter == 'python3'

    platform_info = {
        'platform_uname': ['Linux'],
        'platform_dist_result': ['', '', ''],
        'osrelease_content': ['NAME="Red Hat Enterprise Linux Server"\nVERSION="7.0 (Maipo)"\n', '']
    }

# Generated at 2022-06-12 21:39:07.026723
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.executor.task_result import TaskResult
    from ansible.playbook.task import Task

    task = Task()
    task_result = TaskResult(host='localhost', task=task)

    interpreter_name = 'python'
    discovery_mode = 'auto_legacy'
    task_vars = {'inventory_hostname': 'localhost'}

    actual_interpreter = discover_interpreter(task, interpreter_name, discovery_mode, task_vars)

    assert actual_interpreter is not None

# Generated at 2022-06-12 21:39:16.235229
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # import the module that these tests are for
    import ansible.executor.discovery


# Generated at 2022-06-12 21:39:27.720426
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.plugins.action.normal import ActionModule as ActionNormal
    from ansible.plugins.loader import module_loader

    # Create a mock action module object.

# Generated at 2022-06-12 21:39:34.945876
# Unit test for function discover_interpreter
def test_discover_interpreter():
    import os
    os.environ['ANSIBLE_INVENTORY_ENABLED'] = 'False'
    from ansible.parsing.plugin_docs import read_docstring
    from ansible.plugins.action import ActionBase
    doc = read_docstring(discover_interpreter, verbose=False, style='epydoc', prepend_first=False)
    assert doc.get('description', '').startswith(u'Python interpreter discovery')
    platform_type = 'Linux'
    discovered_interpreters = ['/usr/bin/python']
    hostname = 'localhost'
    task_vars = {}
    action = ActionBase()
    action._connection = type('connection', (object,), {'has_pipelining': True})

# Generated at 2022-06-12 21:39:45.189896
# Unit test for function discover_interpreter
def test_discover_interpreter():
    test_interpreter_name = u'python'

    def _get_task_vars(platform_python_map, shell_python_list='', override_shell_python=''):
        task_vars = dict(
            ansible_python_interpreter=u'/usr/bin/python',
            ansible_python_version=u'2.7.14',
        )
        task_vars['ansible_python_interpreter_py3'] = u'/usr/bin/python3'

        task_vars['ansible_python_version_interpreter_py3'] = u'3.6.6'

        task_vars['ansible_architecture'] = u'x86_64'

        task_vars['ansible_distribution'] = u'Fedora'
        task_vars

# Generated at 2022-06-12 21:39:52.474491
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # This test is not so much a unit test as it is a collection of integration test assertion examples with printouts.
    # TODO: add more interestingly mocked out platforms
    class Action(object):
        def __init__(self):
            self._discovery_warnings = []

        def _low_level_execute_command(self, cmd, sudoable, in_data=None):
            print('Running {0!r}, sudoable={1!r}'.format(cmd, sudoable))
            return {
                'stdout': self._mock_stdout,
                'stdin': self._mock_stdin,
            }

        _mock_stdin = b'python_platform_script_contents'


# Generated at 2022-06-12 21:40:04.010528
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.executor.action_loader import ActionModuleLoader
    from ansible.plugins.action import ActionBase
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    class TestAction(ActionBase):
        TRANSFERS_FILES = True

        def __init__(self, task, connection, play_context, loader, templar, shared_loader_obj):
            super(TestAction, self).__init__(task, connection, play_context, loader, templar, shared_loader_obj)
            self._discovery_warnings = []
