

# Generated at 2022-06-12 21:30:18.351800
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.executor.discovery import discover_interpreter
    from ansible.plugins.action.normal import ActionModule as ActionNormal
    from ansible.playbook.play_context import PlayContext

    class ActionModule(ActionNormal):
        def _discover_interpreter(self, *args, **kwargs):
            return discover_interpreter(*args, **kwargs)

    class Connection(object):
        def __init__(self, has_pipelining):
            self.has_pipelining = has_pipelining

    # this is an abridged version, just enough to pass the tests

# Generated at 2022-06-12 21:30:27.304530
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.vars.manager import VariableManager

    # Setup
    connection = DummyConnection()
    task_queue_manager = TaskQueueManager(None, None, connection, None, None, None, None)
    task_vars = dict(ANSIBLE_INTERPRETER_PYTHON="/usr/bin/python")
    variable_manager = VariableManager(loader=None, host_vars=task_vars)
    task_queue_manager._variable_manager = variable_manager

    # Success cases
    # - exact match to supported version
    res = discover_interpreter(task_queue_manager, 'python', 'auto', task_vars)
    assert res == '/usr/bin/python'

    # Failure cases
    # - invalid interpreter name


# Generated at 2022-06-12 21:30:35.808234
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

    class FakeAction(object):
        def __init__(self):
            self._discovery_warnings = []
            self._connection = None

        def _low_level_execute_command(self, interpreter, sudoable=False, in_data=None):
            if interpreter != u'/usr/bin/python':
                raise ValueError('unexpected interpreter name: {0}'.format(interpreter))

            if not in_data:
                raise ValueError('no in_data provided')

            f_data = to_text(in_data, errors='strict')


# Generated at 2022-06-12 21:30:44.647390
# Unit test for function discover_interpreter
def test_discover_interpreter():
    import pytest

    with pytest.raises(ValueError):
        discover_interpreter(None, 'fake_interpreter', 'auto', None)

    with pytest.raises(NotImplementedError):
        discover_interpreter(None, 'python', 'auto', None)

    with pytest.raises(NotImplementedError):
        discover_interpreter(None, 'python', 'auto_silent', None)

    with pytest.raises(NotImplementedError):
        discover_interpreter(None, 'python', 'auto_legacy', None)

    with pytest.raises(NotImplementedError):
        discover_interpreter(None, 'python', 'auto_legacy_silent', None)

# Generated at 2022-06-12 21:30:45.795626
# Unit test for function discover_interpreter
def test_discover_interpreter():
    pass

# Generated at 2022-06-12 21:30:56.907395
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # Test execute_command, low_level_execute_command
    r1 = {'stderr': '', 'stdout': "PLATFORM\nLinux\nFOUND\n/usr/bin/python\nENDFOUND"}
    r2 = {'stderr': '', 'stdout': json.dumps({'stderr': '', 'stdout': "PLATFORM\nLinux\nFOUND\n/usr/bin/python\nENDFOUND", 'platform_dist_result': ['', '', ''], 'os_release_error': '', 'osrelease_content': ""})}

    # test_discover_interpreter_linux_discovery
    a1 = {'_discovery_warnings': []}
    a2 = {'_discovery_warnings': []}

# Generated at 2022-06-12 21:31:05.971051
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.plugins.action import ActionBase

    class MyAction(ActionBase):
        TRANSFERS_FILES = False

        def _low_level_execute_command(self, cmd, sudoable=True, in_data=None, executable=None):
            return {'stdout': "PLATFORM\nLinux\nFOUND\n/usr/bin/python\nENDFOUND"}

    my_action = MyAction(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    task_vars = {'ansible_facts': {
        'ansible_python_version': u'2.7.9'
    }}


# Generated at 2022-06-12 21:31:08.519471
# Unit test for function discover_interpreter
def test_discover_interpreter():
    assert (discover_interpreter(None, 'python', 'auto_silent', {}) == '/usr/bin/python')

# Generated at 2022-06-12 21:31:16.077477
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.plugins.loader import action_loader

    # validate mock data
    # 1. os-release is present and valid
    #    1. default python is present
    #       1. default python interpreter is used
    #    2. default python is missing
    #       1. older python interpreter is used
    #    3. os-release is invalid
    #       1. use platform.dist()
    # 2. os-release is missing
    #    1. invalid platform
    #       1. throw exception
    #    2. platform.dist() is partially valid
    #       1. partial match is found
    #   

# Generated at 2022-06-12 21:31:26.373700
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # setup task vars
    task_vars = dict(
        inventory_hostname='127.0.0.1',
    )

    test_interpreter_map = dict(
        ansible_python_interpreter='python',
        ansible_python_version='2.7.5'
    )


# Generated at 2022-06-12 21:31:45.941999
# Unit test for function discover_interpreter
def test_discover_interpreter():
    import os
    import shutil
    import tempfile
    import pkgutil
    from ansible.module_utils.basic import AnsibleModule

    host = 'localhost'
    task_vars = dict()

    # Generate a temporary directory to store the test data
    tmp_dir = tempfile.mkdtemp()

    # Generate a temporary Python script to test with
    tmp_script = tempfile.NamedTemporaryFile(suffix='.py', dir=tmp_dir, delete=False)
    tmp_script.write(b'print(1 + 1)')
    tmp_script.close()

    # Generate a temporary inventory
    tmp_inventory = tempfile.NamedTemporaryFile(mode="wt", dir=tmp_dir, delete=False)
    tmp_inventory.write('localhost')
    tmp_inventory.close()

# Generated at 2022-06-12 21:31:56.463269
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.module_utils._text import to_bytes
    from ansible.executor.discovery.bootstrap import pwsh_bootstrap
    from ansible.plugins.action.script import ActionModule as ScriptActionModule
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.inventory.manager import InventoryManager

    def _create_mock_connection():
        class MockConnection:
            def __init__(self):
                self._shell = 'powershell'
                self._shell_type = 'pwsh'
                self._pipelining = True
                self._become = False


# Generated at 2022-06-12 21:32:03.917457
# Unit test for function discover_interpreter
def test_discover_interpreter():
    """Test for function discover_interpreter"""
    import json
    import os
    from ansible.plugins.action.script import ActionModule as script_action
    from ansible.module_utils.facts import DefaultFactCollector
    from ansible.module_utils.facts.system.distribution import DistributionFactCollector
    from ansible.module_utils.facts.system.platform import PlatformFactCollector
    from ansible.module_utils.facts.system.pkg_mgr import PkgMgrFactCollector
    from ansible.module_utils.facts.system.distribution_files import DistributionFilesFactCollector
    from ansible.module_utils.facts.system.distribution_major_version import DistributionMajorVersionFactCollector
    from ansible.module_utils.facts.system.distribution_release import DistributionReleaseFactCollector

# Generated at 2022-06-12 21:32:05.322668
# Unit test for function discover_interpreter
def test_discover_interpreter():
    pass

# Generated at 2022-06-12 21:32:17.519158
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.plugins import action
    import ansible.executor
    from ansible.plugins.action import ActionModule
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.playbook import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.inventory import Inventory
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.plugins.loader import action_loader

    class TestActionModule(ActionModule):
        def __init__(self):
            self._display = Display()
            self._connection = None
            self._shell = None
            self._low_level_execute_command = action._low_level_

# Generated at 2022-06-12 21:32:25.111550
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.utils.display import Display
    display = Display()
    action = Display()
    task_vars = Display()
    task_vars.update({
        'inventory_hostname': 'localhost',
        'ansible_python_interpreter': '/usr/bin/python',
        'ansible_connection': 'local'
    })
    discover_interpreter(action=action,
                         interpreter_name='python',
                         discovery_mode='auto',
                         task_vars=task_vars)
    # TODO: assert something here

# Generated at 2022-06-12 21:32:25.743795
# Unit test for function discover_interpreter
def test_discover_interpreter():
    pass

# Generated at 2022-06-12 21:32:37.366803
# Unit test for function discover_interpreter
def test_discover_interpreter():
    import os
    from ansible.executor.task_executor import TaskExecutor
    from ansible.inventory.host import Host
    from ansible.vars.hostvars import HostVars
    from ansible.vars.manager import VariableManager

    class MyTaskExecutor(TaskExecutor):
        def __init__(self):
            self._connection = Connection()
            self.host = 'fakehost'

    class Connection(object):
        def __init__(self):
            self.has_pipelining = True
            self.become = False
            self.become_method = 'sudo'
            self.become_user = 'root'

        def exec_command(self, cmd, in_data=None):
            output = {'stdout': '', 'stderr': '', 'rc': 0}


# Generated at 2022-06-12 21:32:46.404843
# Unit test for function discover_interpreter
def test_discover_interpreter():
    import six
    from ansible.module_utils.common.collections import ImmutableDict

    # A method to test exceptions
    def test_exception(name, mode, **kwargs):
        try:
            print("\n{0}: {1} {2}\n".format("=" * 10, name, "=" * 10))
            discover_interpreter("action", name, mode, **kwargs)
            assert False, "The exception is not raised"
        except Exception as e:
            print("Exception: {0}".format(e))

    # Step 1: Test exceptions
    print("{0}: {1} {2}\n".format("=" * 10, "Step 1: Test exceptions", "=" * 10))
    # Test NotImplementedError

# Generated at 2022-06-12 21:32:54.590036
# Unit test for function discover_interpreter
def test_discover_interpreter():
  action = None
  interpreter_name = 'python'
  discovery_mode = 'auto_legacy_silent'
  task_vars = {}

  try:
    discover_interpreter(action, interpreter_name, discovery_mode, task_vars)
  except InterpreterDiscoveryRequiredError as ex:
    if ex.interpreter_name != 'python':
      raise
    if ex.discovery_mode != 'auto_legacy_silent':
      raise

  discovery_mode = 'foo'
  try:
    discover_interpreter(action, interpreter_name, discovery_mode, task_vars)
  except NotImplementedError as ex:
    if 'discovery mode' not in ex.args[0]:
      raise Exception('Unable to find discovery mode in error message')


# Generated at 2022-06-12 21:33:23.288183
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.module_utils import basic
    from ansible.vars import VariableManager

    module_loader, params, action = basic.AnsibleModule(argument_spec={}, supports_check_mode=True)

    action._low_level_execute_command = fake_low_level_execute_command
    action._discovery_warnings = []

    # mode, interpreter_name, name, expected_result

# Generated at 2022-06-12 21:33:33.389642
# Unit test for function discover_interpreter
def test_discover_interpreter():
    import os
    # path to test files
    base_path = os.path.dirname(__file__)
    test_data_path = os.path.join(base_path, '..', '..', '..', 'test', 'units', 'executor', 'discovery')

    # base test config

# Generated at 2022-06-12 21:33:33.965023
# Unit test for function discover_interpreter
def test_discover_interpreter():
    pass

# Generated at 2022-06-12 21:33:40.489725
# Unit test for function discover_interpreter
def test_discover_interpreter():
    class MockAction(object):
        def __init__(self):
            self._discovery_warnings = []
        def _low_level_execute_command(self, cmd, sudoable=False, in_data=None):
            if cmd == "echo PLATFORM; uname; echo FOUND; command -v '/usr/bin/python'; echo ENDFOUND":
                return dict(stdout=u"PLATFORM\nLinux\nFOUND\n/usr/bin/python\nENDFOUND", stderr=u"")

# Generated at 2022-06-12 21:33:52.893999
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # Test Case 1: Discover CentOS 5.6 distro
    distro, version = _get_linux_distro({"platform_dist_result": ["centos", "5.6", "Final"]})
    assert distro == "centos", "CentOS should be identified"
    assert version == "5.6", "CentOS version should be 5.6"

    # Test Case 2: Discover no distro
    distro, version = _get_linux_distro({})
    assert distro == "", "No distro discovered"
    assert version == "", "No version discovered"

    # Test Case 3: Discover Ubuntu 14.04

# Generated at 2022-06-12 21:33:59.917421
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.plugins.action.normal import ActionModule as _ActionModule

    class ActionModule(_ActionModule):
        def run(self, tmp=None, task_vars=None):
            if task_vars is None:
                task_vars = dict()

            result = super(ActionModule, self).run(tmp, task_vars)

            # Originally, we would raise an exception here if the discovery mode was 'silent' but
            # no interpreter was found.  This functionality is not possible.  Display.warning or
            # display.debug cannot be called within the interpreter discovery process.  If they are,
            # Ansible will attempt to call get_bin_path which will once again call discover_interpreter
            # (because of the self._interpreter hasn't been populated

# Generated at 2022-06-12 21:34:10.798933
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.executor.discovery import discover_interpreter
    from ansible.module_utils.connection import ConnectionBase
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.six.moves import StringIO
    from ansible.plugins.action import ActionBase
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.plugins.strategy import StrategyBase
    from ansible.executor.internal_runner import InternalRunner


# Generated at 2022-06-12 21:34:19.715002
# Unit test for function discover_interpreter

# Generated at 2022-06-12 21:34:27.671374
# Unit test for function discover_interpreter
def test_discover_interpreter():
    task_vars = {
        'ansible_python_interpreter': '/usr/bin/python',
        'inventory_hostname': 'testhost',
    }

    display.verbosity = 4

    # test error conditions

    # action is of wrong type
    try:
        discover_interpreter('', 'python', 'auto_legacy_silent', task_vars)
        assert False, "Interpreter discovery should fail when action is not of type ActionBase"
    except ValueError:
        pass

    # interpreter name is not just 'python'
    try:
        discover_interpreter(None, 'python3', 'auto_legacy_silent', task_vars)
        assert False, "Interpreter discovery should fail when interpreter name is not just 'python'"
    except ValueError:
        pass

    #

# Generated at 2022-06-12 21:34:39.742213
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.executor.action_plugins.discovery import discover_interpreter_legacy
    from .action_plugins.discovery import discover_interpreter
    from ansible.plugins.loader import action_loader
    from ansible.plugins.action import ActionBase

    class TestAction(ActionBase):
        def run(self, tmp=None, task_vars=None):
            raise ValueError('could not find remote python')
            return super(TestAction, self).run(tmp, task_vars)

    task_vars = dict()
    action_plugin = action_loader.get('debug', class_only=True)()
    action_loader.add_directory(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'action_plugins'))
    action_loader

# Generated at 2022-06-12 21:35:06.035996
# Unit test for function discover_interpreter
def test_discover_interpreter():
    module_args = dict(
        safe_mode=dict(default=False)
    )

# Generated at 2022-06-12 21:35:15.820730
# Unit test for function discover_interpreter
def test_discover_interpreter():
    import sys
    import os
    import tempfile
    from ansible.plugins.action import ActionBase
    from ansible.plugins.action.normal import ActionModule as ActionNormal
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.vars.hostvars import HostVars

    class ActionModule(ActionNormal):
        def get_bin_path(self, arg, required=False, opt_dirs=[]):
            return '/bin/' + arg

        def _low_level_execute_command(self, cmd, sudoable=False, in_data=None, executable=None, stdin=None):
            return dict(
                cmd=cmd,
                stdout=os.read(stdout_fd, 100000),
                stderr='',
                rc=0,
            )



# Generated at 2022-06-12 21:35:26.600636
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.executor.discovery import discover_interpreter
    from ansible.plugins.action.script import ActionModule
    from ansible.playbook.task_include import TaskInclude
    import os

    class Host():
        def __init__(self, hostname):
            self.name = hostname
            self.vars = dict()  # FIXME: add some vars here?

    class Play():
        def __init__(self, hostname):
            self.hosts = [Host(hostname)]

        def get_variable_manager(self):
            class VariableManager():
                def __init__(self):
                    self.vars = dict()

                def get_vars(self, play=None, host=None, task=None, include_hostvars=True):
                    return dict()
            return Variable

# Generated at 2022-06-12 21:35:39.469161
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # FUTURE: set things up for more extensive tests
    # we don't want to test the shell bootstrap, so mock it out
    import ansible.context
    from ansible.mock import patch

    testaction = ansible.context._init_global_context()
    testaction.task_vars = dict()

# Generated at 2022-06-12 21:35:40.520879
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # placeholder for future unit tests
    pass

# Generated at 2022-06-12 21:35:51.463858
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # pylint: disable=import-error
    import ansible.plugins
    import ansible.plugins.action
    import ansible.plugins.action.discovery

    # pylint: disable=protected-access
    # pylint: disable=no-member

    # these need to be ordered by priority (first match wins)
    python_paths = [
        '/usr/bin/python3',
        '/usr/bin/python2',
        '/usr/bin/python',
    ]

    class FakeTask:
        def __init__(self):
            self.args = {}
            self.noop_task = False
            self.action = None
            self.async_val = None
            self.notify = []
            self.on_failed = []
            self.on_skipped = []
            self.de

# Generated at 2022-06-12 21:36:02.373674
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.executor.discovery import discover_interpreter

    action = None
    interpreter_name = 'python'
    task_vars = {
        'ansible_python_interpreter': '/tmp/does/not/exist/i.hope',
        'ansible_interpreter_python': '/tmp/does/not/exist/i.hope',
    }

    # In silent mode we should get the default path back, if it is in the list of found python
    # interpreters. This is basically a test for the fallback.
    task_vars['ansible_python_interpreter'] = discover_interpreter(action, interpreter_name, 'auto_silent', task_vars)

# Generated at 2022-06-12 21:36:07.552847
# Unit test for function discover_interpreter
def test_discover_interpreter():
    res = discover_interpreter(action=None, interpreter_name='python', discovery_mode='auto', task_vars={})
    assert res == '/usr/bin/python'

    res = discover_interpreter(action=None, interpreter_name='python', discovery_mode='auto_legacy', task_vars={})
    assert res == '/usr/bin/python'

# Generated at 2022-06-12 21:36:17.043775
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # for now, just run an integration test

    from ansible.plugins.action import ActionBase

    class DummyModule(object):
        def __init__(self):
            self.warnings = []

        def warn(self, msg, *args, **kwargs):
            self.warnings.append(msg)

        def exit_json(self, changed=False, result=None):
            print(json.dumps(result))

        def fail_json(self, msg, **kwargs):
            print(json.dumps(dict(failed=True, msg=msg)))


# Generated at 2022-06-12 21:36:28.350707
# Unit test for function discover_interpreter
def test_discover_interpreter():
    test_platform_python_map = {
        'redhat': {
            "6": "/usr/bin/python",
            "7": "/usr/bin/python",
        },
        'centos': {
            "5": "/usr/bin/python",
            "7": "/usr/bin/python",
        }
    }
    test_bootstrap_python_list = [
        "/usr/bin/python",
        "/usr/bin/python2",
        "/usr/bin/python3",
    ]
    test_task_vars = {
        'inventory_hostname': "test_host",
        'ansible_python_interpreter': "/usr/bin/python2.6"
    }
    test_action = None
    test_interpreter_name = "python"
    test_discovery

# Generated at 2022-06-12 21:37:19.238927
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # Copy of _execute_module() testing framework.
    action = None
    interpreter_name = "python"
    discovery_mode = "auto"
    task_vars=dict(
        inventory_hostname='test-host',
        ansible_python_interpreter='/usr/bin/python',
        ansible_python_interpreter_discovery_mode=discovery_mode,
        ansible_verbosity=4,
        ansible_version=dict(full=2, major=2, minor=5),
        path_info=dict(path='/usr/bin')
    )


# Generated at 2022-06-12 21:37:29.507368
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.plugins.action.normal import ActionModule as _ActionModule

    class ActionModule(_ActionModule):
        def _execute_module(self, tmp=None, task_vars=None):
            raise Exception("_execute_module() should not be called!")

    am = ActionModule(task=dict(), connection=dict(), play_context=dict(), loader=dict(),
                      templar=dict(), shared_loader_obj=dict())

    # test with no argv
    try:
        discover_interpreter(am, "foo", "auto_legacy_silent", dict())
        raise Exception("No exception is raised")
    except ValueError as e:
        assert "Interpreter discovery not supported for foo" in str(e)

    # test with no inventory_hostname

# Generated at 2022-06-12 21:37:36.895192
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.executor.task_result import TaskResult
    from ansible.executor.action_result import ActionResult
    from ansible.executor.module_common import _low_level_execute_command

    host = 'localhost'
    module_name = 'shell'
    module_args = {'_raw_params': 'ansible --version'}
    task_vars = {}
    tmp_path = '.'

    task_result = TaskResult(host, module_name, module_args, task_vars)
    action_result = ActionResult(task_result, tmp_path)
    action_result._low_level_execute_command = _low_level_execute_command
    action_result._discovery_warnings = []

    # 'auto_legacy_silent_success' is the default
    assert discover

# Generated at 2022-06-12 21:37:46.658578
# Unit test for function discover_interpreter
def test_discover_interpreter():
    global display
    display = Display()

    # assure that full discovery works
    action = MockActionModule()
    result = discover_interpreter(action, u'python', u'auto', {}, {})
    assert result == u'/usr/bin/python'

    # assure that discovery falls back in the auto_legacy case
    action = MockActionModule()
    result = discover_interpreter(action, u'python', u'auto_legacy', {}, {})
    assert result == u'/usr/bin/python'

    # assure that discovery fails in the explicit mode, since /usr/bin/python isn't available
    action = MockActionModule()
    result = discover_interpreter(action, u'python', u'explicit', {}, {})
    assert result == u'/usr/bin/python'

# Generated at 2022-06-12 21:37:59.327675
# Unit test for function discover_interpreter
def test_discover_interpreter():
    fake_action = type("FakeAction", (object,), {"_low_level_execute_command": lambda *args, **kwargs:{"stdout": "PLATFORM\nLinux\nFOUND\n/usr/bin/python\n/usr/bin/python3\nENDFOUND"}})()

    res = discover_interpreter(fake_action, 'python', 'auto', {})
    assert res == "/usr/bin/python"

    res = discover_interpreter(fake_action, 'python', 'auto_legacy', {})
    assert res == "/usr/bin/python"

    res = discover_interpreter(fake_action, 'python', 'auto_silent', {})
    assert res == "/usr/bin/python"


# Generated at 2022-06-12 21:38:07.947981
# Unit test for function discover_interpreter
def test_discover_interpreter():

    """ Unit test for function discover_interpreter """
    import sys
    import re
    from ansible.executor.discovery import discover_interpreter
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.module_utils.six import StringIO
    from ansible.module_utils.ansible_release import __version__ as ANSIBLE_VERSION
    from ansible.module_utils._text import to_bytes, to_text
    from ansible.module_utils.distro import LinuxDistribution

    # import python script use to compile to bytescode
    platform_script = pkgutil.get_data('ansible.executor.discovery', 'python_target.py')


# Generated at 2022-06-12 21:38:13.991150
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.executor.module_common import _shared_module_utils, InterpreterDiscoveryRequiredError

    # This is the value returned by "uname"
    host_os = 'Linux'
    host_os_version = '4.15.0-1054-aws'

    # The InterpreterDiscoveryRequiredError is expected to be raised since
    # there is no linux distributions found in the list of linux distributions
    # supported by ansible
    with pytest.raises(InterpreterDiscoveryRequiredError):
        _shared_module_utils._gen_rhel_interpreter_args(host_os, host_os_version)

# Generated at 2022-06-12 21:38:20.125020
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # Test bad interpreter
    try:
        discover_interpreter('', 'my_interpreter', 'auto')
        assert False, 'Expected error'
    except ValueError as e:
        assert 'not supported' in str(e)

    # Test not implemented
    try:
        discover_interpreter('', 'python', 'auto', {'ansible_os_family': 'OSX'})
        assert False, 'Expected error'
    except NotImplementedError as e:
        assert 'unsupported platform' in str(e)

    # Test interpreter discovery required

# Generated at 2022-06-12 21:38:21.056868
# Unit test for function discover_interpreter
def test_discover_interpreter():
    pass

# Generated at 2022-06-12 21:38:27.519440
# Unit test for function discover_interpreter
def test_discover_interpreter():
    action = None
    interpreter_name = 'python'
    discovery_mode = 'auto_legacy'
    task_vars = dict()

    try:
        display.debug(msg=u"attempting interpreter discovery")
        result = discover_interpreter(action, interpreter_name, discovery_mode, task_vars)
        display.debug(msg=u'Result: {0}'.format(result))

    except Exception as ex:
        display.display(msg=u"Test case FAILED!")


# Generated at 2022-06-12 21:39:14.450530
# Unit test for function discover_interpreter
def test_discover_interpreter():
    import unittest


# Generated at 2022-06-12 21:39:25.779208
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.module_utils.basic import AnsibleModule

    def run_module():

        module_args = dict(
            interpreter_name='python',
            discovery_mode='auto',
            task_vars=dict(
                ansible_distribution='RedHat',
                ansible_distribution_version='6.0'
            )
        )

        result = dict(
            changed=False,
            interpreter_path='/usr/bin/python',
        )

        module = AnsibleModule(
            argument_spec=dict(
                interpreter_name=dict(type='str', required=True),
                discovery_mode=dict(type='str', required=True),
                task_vars=dict(type='dict', required=True),
            ),
            supports_check_mode=True
        )


# Generated at 2022-06-12 21:39:33.749523
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.executor.task_result import TaskResult

    result = TaskResult(host='host1')

    class FakeAction(object):
        def __init__(self):
            self._discovery_warnings = []

        def _low_level_execute_command(self, command, sudoable=False, in_data=''):
            stdout_data = "PLATFORM\nLinux\nFOUND\n/usr/bin/python\n/bin/python\nENDFOUND"
            return dict(failed=False, rc=0, stdout=stdout_data, stderr='')

        def _connection_has_pipelining(self):
            return True

    action = FakeAction()
    interpreter_name = 'python'

    # If discovery mode is auto, auto_legacy, or auto_silent

# Generated at 2022-06-12 21:39:44.706455
# Unit test for function discover_interpreter
def test_discover_interpreter():
    import re
    test_data = {'inventory_hostname': 'localhost', 'ansible_python_interpreter': '/usr/bin/python'}

    # Test InterpreterDiscoveryRequiredError Exception
    try:
        discover_interpreter('', 'foo', 'auto', test_data)
    except ValueError as e:
        assert 'Interpreter foo is not supported' in to_text(e)

    # Test InterpreterDiscoveryRequiredError Exception
    try:
        discover_interpreter('', 'python', 'foo', test_data)
    except ValueError as e:
        assert 'Interpreter discovery mode foo is not supported' in to_text(e)

    # Test Interpreter Not Supported Exception

# Generated at 2022-06-12 21:39:47.285344
# Unit test for function discover_interpreter
def test_discover_interpreter():
    action = None
    interpreter_name = 'python'
    discovery_mode = 'auto'
    task_vars = {}
    assert discover_interpreter(action, interpreter_name, discovery_mode, task_vars)

# Generated at 2022-06-12 21:39:57.638291
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.plugins.action.script import ActionModule as ScriptAction
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    class FakeHost(object):
        def __init__(self, name):
            self.name = name
            self.vars = {'ansible_python_interpreter': '/usr/bin/python'}

        def get_vars(self):
            return self.vars

    class FakeConnection(object):

        def __init__(self):
            self.transport = 'local'
