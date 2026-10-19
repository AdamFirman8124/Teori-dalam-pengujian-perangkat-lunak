

# Generated at 2022-06-12 21:30:17.144718
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.plugins.action import ActionBase
    from ansible.executor.task_result import TaskResult
    import time

    class ActionModulePlaceholder(ActionBase):
        def run(self, tmp=None, task_vars=None):
            pass

    class UnprivilegedConnection(object):
        def has_pipelining(self):
            return True

    class ActionModulePipelining(ActionModulePlaceholder):
        def run(self, tmp=None, task_vars=None):
            # verify that pipelining is required
            assert self._connection.has_pipelining()

            # these are the results we would get back from the remote for the
            # platform.dist() call and /etc/os-release read
            # TODO: make a more realistic result set

# Generated at 2022-06-12 21:30:26.407157
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.module_utils import basic
    from ansible.plugins.action import ActionBase
    from ansible.executor.task_result import TaskResult

    class TestModule(object):
        def __init__(self, action_result):
            self._result = action_result

        def _execute_module(self, *args, **kwargs):
            display.vvvv(msg='executing module')
            display.vvvv(msg='args: {0}'.format(args))
            display.vvvv(msg='kwargs: {0}'.format(kwargs))
            self._result.update(dict(changed=True, msg='Fake result'))

    class TestActionBase(ActionBase):
        def __init__(self):
            self._task = TestModule(dict())
            self._connection = basic.AnsibleConnection

# Generated at 2022-06-12 21:30:36.996593
# Unit test for function discover_interpreter
def test_discover_interpreter():
    import sys
    import os

    display.display.verbosity = 4


# Generated at 2022-06-12 21:30:47.193265
# Unit test for function discover_interpreter
def test_discover_interpreter():

    import os
    import sys
    import unittest


    class TestDiscovery(unittest.TestCase):

        test_dir = os.path.dirname(os.path.realpath(__file__))
        test_data = os.path.join(test_dir, 'discover_interpreter_data')


# Generated at 2022-06-12 21:30:58.184750
# Unit test for function discover_interpreter
def test_discover_interpreter():
    class Action(object):
        def __init__(self, display_warning,
                     return_code=0, platform='linux', new_value='/usr/bin/python'):
            self._display_warning = display_warning
            self._return_code = return_code
            self._platform = platform
            self._new_value = new_value
            self._result = None
            self._discovery_warnings = []

        def _low_level_execute_command(self, *args, **kwargs):
            if self._platform == 'linux':
                command = "{0}\nFOUND\n/usr/bin/python\nENDFOUND".format(self._platform)

# Generated at 2022-06-12 21:30:58.823992
# Unit test for function discover_interpreter
def test_discover_interpreter():
    assert False

# Generated at 2022-06-12 21:31:06.997567
# Unit test for function discover_interpreter
def test_discover_interpreter():
    """
    Test the discover_interpreter function
    """
    display_data = []
    display_messages = []
    display_warnings = []

    ###########################################################################
    class MockParams(object):
        def __init__(self, **kwargs):
            self.__dict__.update(kwargs)

    ###########################################################################
    class MockTask(object):
        def __init__(self, name):
            self.name = name

    ###########################################################################
    class MockPlay(object):
        def __init__(self, name, hosts=None, tasks=None):
            self.name = name
            self.hosts = hosts
            self.tasks = tasks

        def get_tasks(self):
            return self.tasks

    ###########################################################################

# Generated at 2022-06-12 21:31:15.429016
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText

    test_input = u'''PLATFORM
Linux
FOUND
/usr/bin/python
/usr/bin/python2
/usr/bin/python2.7
/usr/bin/python3
/usr/bin/python3.6
/usr/bin/python3.7
/usr/bin/python3.8
ENDFOUND'''

    test_platform_dist_result = [u'', u'', u'']
    test_osrelease_content = ''


# Generated at 2022-06-12 21:31:25.915310
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.executor.task_queue_manager import TaskQueueManager

    #
    # Test case: "auto" discovery mode when platform has only single Python
    # interpreter installed.  This is a good candidate as it is the common case
    #
    tqm = TaskQueueManager('dummy')
    host = tqm.inventory.get_host('localhost')
    host_vars = dict()
    facts = dict()
    facts['ansible_python_interpreter'] = '/usr/bin/python'
    host.set_variable('ansible_python_interpreter', facts['ansible_python_interpreter'])
    host.vars = host_vars
    host.vars.update(facts)

    action = dict()
    action['host'] = host

# Generated at 2022-06-12 21:31:31.252711
# Unit test for function discover_interpreter
def test_discover_interpreter():
    action = None
    interpreter_name = 'python'
    discovery_mode = 'auto'
    task_vars = {}
    interpreter = discover_interpreter(action, interpreter_name, discovery_mode, task_vars)
    print(interpreter)

test_discover_interpreter()

# Generated at 2022-06-12 21:31:47.527807
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # per-host values are dictionaries, so we can't directly use the fixture
    # and have to extract/normalize the values we need
    test_fixture = _test_discover_interpreter_fixture()
    expected_ansible_python_interpreter = dict()

    for (host_name, host_data) in test_fixture.get('ansible_python_interpreter').items():
        expected_ansible_python_interpreter[host_name] = host_data.get('ansible_python_interpreter')

    for host_name, expected_value in expected_ansible_python_interpreter.items():
        # TODO: remove this when CI is updated to run pytest
        try:
            import pytest
        except ImportError:
            pytest = None


# Generated at 2022-06-12 21:31:49.656414
# Unit test for function discover_interpreter
def test_discover_interpreter():
    assert '/usr/bin/python' == discover_interpreter(action=None, interpreter_name='python', discovery_mode='auto_silent', task_vars={})

# Generated at 2022-06-12 21:32:00.229436
# Unit test for function discover_interpreter
def test_discover_interpreter():
    import ansible.module_utils.compat as compat
    import ansible.executor.task_queue_manager as task_queue_manager
    from ansible.executor.task_executor import TaskExecutor

    task_vars = dict()
    host = 'localhost'
    task = task_queue_manager._create_task(None, 'debug', {'msg': 'Hello World!!!'}, task_vars)
    task_executor = TaskExecutor(host, task, task_vars)
    task_executor.action = compat.get_action(task_executor)
    action = task_executor.action

    res = discover_interpreter(action, 'python', 'auto', task_vars)
    assert(res is not None)


# Generated at 2022-06-12 21:32:13.059437
# Unit test for function discover_interpreter
def test_discover_interpreter():
    action = None
    interpreter_name = 'python'

    # Case 1: test the legacy discovery mode
    try:
        discovery_mode = 'auto_legacy'
        task_vars = {'ansible_python_interpreter': None}
        result = discover_interpreter(action, interpreter_name, discovery_mode, task_vars)
        assert result == 'auto'
    except Exception:
        assert False

    # Case 2: test the default discovery mode
    try:
        discovery_mode = 'auto'
        task_vars = {'ansible_python_interpreter': None}
        result = discover_interpreter(action, interpreter_name, discovery_mode, task_vars)
        assert result == 'auto'
    except Exception:
        assert False

    # Case 3: test the directory discovery mode

# Generated at 2022-06-12 21:32:24.544405
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins.loader import interpreter_loader
    from ansible.executor.task_result import TaskResult
    from ansible.executor.play_context import PlayContext

    # This has to be a non-failure action
    action = interpreter_loader.get('yum_repository')
    # TODO: determine what task_vars are needed
    task_vars = {}
    # TODO: determine what project play_context is needed
    task_result = TaskResult(host=None, task=None, return_data={})

# Generated at 2022-06-12 21:32:35.367491
# Unit test for function discover_interpreter
def test_discover_interpreter():
    import os
    import sys

    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.facts.system.distribution import DistributionFactCollector

    from ansible.tests.unit.mock.loader import DictDataLoader

    def _mock_module_init(self, *args, **kwargs):
        self.params = {'action': 'test_action', 'interpreter_name': 'python', 'discovery_mode': 'auto_legacy_silent'}
        # force action.module_vars to have a fake minimum set of values

# Generated at 2022-06-12 21:32:45.365299
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # Test Python path discovery on a variety of OSes and versions
    # TODO: Add more tests once Windows support is added
    # see https://github.com/ansible/ansible/pull/54036
    # TODO: add more tests as discovery is expanded to handle more complex cases
    # see https://github.com/ansible/ansible/pull/54036
    class MockAction():
        def __init__(self):
            self._discovery_warnings = []

        def _low_level_execute_command(self, command, sudoable=False, in_data=None):
            return {'stdout': command, 'stderr': ''}

        def _get_distribution(self):
            return LinuxDistribution

        def _check_pipelining(self):
            return True

    test_task_vars = dict

# Generated at 2022-06-12 21:32:53.885224
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.module_utils.six import StringIO
    from ansible.plugins.loader import action_loader
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    from ansible.plugins import module_loader

    # Hide warning messages
    display.verbosity = 3

    class ShellModule():
        def __init__(self, _):
            self.run_command = lambda cmd: {'stdout': 'PLATFORM\r\nLinux\r\nFOUND\r\n/usr/bin/python\r\nENDFOUND'}

    module_loader.add_directory('./lib/ansible/modules/')
    module_loader.add_directory('./lib/ansible/modules/commands/')

# Generated at 2022-06-12 21:33:06.300008
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # Fake the necessary vars for debug output
    task_vars = {'inventory_hostname': 'localhost', 'ansible_debug': True}

    # Test the most common case
    display.verbosity = 3
    action = lambda: None
    action._connection = lambda: True
    action._connection.has_pipelining = True
    action._low_level_execute_command = lambda interpreter, sudoable, in_data: {'stdout': '''PLATFORM
Linux
FOUND
/usr/bin/python
ENDFOUND'''}
    action._discovery_warnings = []
    assert discover_interpreter(action, 'python', 'auto_legacy', task_vars) == '/usr/bin/python'
    assert action._discovery_warnings == []

    # Test a non-Linux case
    action

# Generated at 2022-06-12 21:33:15.682754
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.executor.task_result import TaskResult
    from ansible.executor.module_common import get_module_path
    action = TaskResult('uuuuuuuuuuuuuuuuuuuuuuuu', 'localhost', {})

    action._low_level_execute_command = lambda cmd, sudoable=False, in_data=None, executable=None: {'stdout': cmd}
    action._connection = type('', (), {'has_pipelining': True})()

    def _debug(msg, host='localhost'):
        print('DEBUG: %s' % msg)

    display.debug = _debug

    # Test sanity
    # print(to_text(discover_interpreter(action, 'python', 'auto', 'hahahahahahahahah', [])))

    # Test discover_interpreter
    action._

# Generated at 2022-06-12 21:33:33.477856
# Unit test for function discover_interpreter
def test_discover_interpreter():
    '''
    Unit test for discover_interpreter function.
    '''
    # These are all the tests are covered in this function
    #
    # 1. Fails if an interpreter other than python is given
    # 2. No python interpreters found for host test-host (tried ['python', 'python3', 'python2'])
    # 3. Platform test-platform on host test-host is using the discovered Python interpreter at /usr/bin/python,
    #    but future installation of another Python interpreter could change the meaning of that path. See
    #    http://docs.ansible.com/ansible/latest/interpreters/index.html for more information.
    # 4. Distribution test-distribution 1.0 on host test-host should use /usr/bin/python2, but is using /usr/bin/python,
    #   

# Generated at 2022-06-12 21:33:34.990623
# Unit test for function discover_interpreter
def test_discover_interpreter():

    assert discover_interpreter(None, 'python', 'auto_legacy', {}) == u'/usr/bin/python'
    # FIXME: INCOMPLETE

# Generated at 2022-06-12 21:33:37.120228
# Unit test for function discover_interpreter

# Generated at 2022-06-12 21:33:49.257322
# Unit test for function discover_interpreter
def test_discover_interpreter():
    import unittest
    from test.unit.utils.action_mocks import ActionBaseMock
    from ansible.utils.hashing import md5s
    from ansible.module_utils.six.moves import StringIO
    from ansible.module_utils import basic

    action = ActionBaseMock(StringIO())

    def get_python_cmd(cmd):
        if cmd:
            # if we are providing a cmd, we need to md5 it to ensure the response is consistent across runs
            return '/usr/bin/python{0}'.format(md5s(cmd))
        else:
            # if it's not specified, just return the baseline
            return '/usr/bin/python'


# Generated at 2022-06-12 21:33:58.066163
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.plugins.action import ActionBase
    from ansible.plugins.loader import action_loader

    # TODO: shouldn't be using private _low_level_execute_command()
    # TODO: shouldn't be using private _discovery_warnings[]

    class DummyAction(ActionBase):
        def _low_level_execute_command(self, cmd, sudoable=True, in_data=None, sudo_user=None, executable=None,
                                       no_log=False):
            return {'stdout': cmd}

        def run(self, tmp=None, task_vars=None):
            return dict(stdout=u'hi')


# Generated at 2022-06-12 21:33:58.651547
# Unit test for function discover_interpreter
def test_discover_interpreter():
    assert False

# Generated at 2022-06-12 21:34:03.825322
# Unit test for function discover_interpreter
def test_discover_interpreter():
    assert discover_interpreter(None, "python", "auto_silent", {}) == "/usr/bin/python"
    assert discover_interpreter(None, "python", "auto_silent", {"inventory_hostname": "test_host", "ansible_env": {}}) == "/usr/bin/python"

# Generated at 2022-06-12 21:34:13.283094
# Unit test for function discover_interpreter
def test_discover_interpreter():
    assert discover_interpreter('action', 'python', 'auto', {}) == '/usr/bin/python'
    assert discover_interpreter('action', 'python', 'auto_silent', {}) == '/usr/bin/python'
    assert discover_interpreter('action', 'python', 'auto_legacy', {}) == '/usr/bin/python'
    assert discover_interpreter('action', 'python', 'auto_legacy_silent', {}) == '/usr/bin/python'
    assert discover_interpreter('action', 'python', 'force', {}) == '/usr/bin/python'
    assert discover_interpreter('action', 'python', 'force_silent', {}) == '/usr/bin/python'

# Generated at 2022-06-12 21:34:22.224598
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.cli import CLI

    cli = CLI(['ansible-playbook', '-i', 'localhost,'])
    cli.options.connection = 'local'

    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.playbook.play_context import PlayContext

    from ansible.executor.task_queue_manager import TaskQueueManager

    from ansible.plugins import module_loader

    from ansible.playbook.play import Play
    from ansible.inventory.manager import InventoryManager

    from ansible.plugins.loader import module_loader

    from ansible.vars.manager import VariableManager
    from ansible.inventory.host import Host

    display.verbosity = 4
    C.DEFAULT_DEBUG = True


# Generated at 2022-06-12 21:34:25.959975
# Unit test for function discover_interpreter
def test_discover_interpreter():
    assert discover_interpreter("ansible.executor.discovery", "python", "explicit_silent", "none") == '/usr/bin/python'
    assert discover_interpreter("ansible.executor.discovery", "python", "auto_legacy_silent", "none") == '/usr/bin/python'

# Generated at 2022-06-12 21:34:50.881353
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.module_utils.facts.system.distribution import DistributionFactCollector

    import os

    class ActionModule:
        def __init__(self):
            self.connection = None
            self.name = None

            self.runner_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
            self._discovered_interpreter_path = {}
            self._discovery_warnings = []
            self._task_vars = {}

            self.action = 'setup'
            self.task = {
                'delegate_to': None,
                'action': 'setup'
            }


# Generated at 2022-06-12 21:35:00.263917
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.executor.discovery import discover_interpreter
    from ansible.plugins import connections, modules
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.inventory.host import Host
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play

    host = Host(name='test')
    inventory = InventoryManager(loader=DataLoader(), sources=None, sources_list=None)
    inventory.add_host(host)


# Generated at 2022-06-12 21:35:07.336795
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.plugins.action import ActionBase
    from ansible.plugins.loader import module_utils_loader

    action = ActionBase()
    task_vars = dict()
    interpreter_name = 'python'
    discovery_mode = 'auto'
    # Fake the taskQueueManager object
    taskQueueManager = TaskQueueManager()
    taskQueueManager.send_callback = lambda *a: None
    taskQueueManager._connection = None
    action._task_queue_manager = taskQueueManager
    # Fake the module_utils path
    action._shared_loader_obj = module_utils_loader
    # Fake the connection

# Generated at 2022-06-12 21:35:16.752659
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.executor.task_result import TaskResult
    from ansible.executor.action_result import HostActionResult
    from ansible.playbook.play_context import PlayContext

    # test target: ubuntu 16.04
    # test target: ubuntu 14.04
    # test target: ubuntu 12.04
    # test target: fedora 26
    # test target: fedora 25
    # test target: fedora 24
    # test target: freebsd 11.1
    # test target: freebsd 10.3
    # test target: centos 7
    # test target: centos 6
    # test target: altlinux 8.2
    # test target: altlinux 7.1

    # test results:
    #  * /usr/bin/python3 for all python3-only platforms
    #  *

# Generated at 2022-06-12 21:35:27.484430
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.module_utils import basic
    from ansible.playbook.play_context import PlayContext
    from ansible.module_utils.common.text.converters import to_bytes

    display = Display()
    display.verbosity = 4

    pc = PlayContext()
    action = basic.ActionModule(task=dict(), connection=None, play_context=pc, loader=None, templar=None, shared_loader_obj=None)
    action._shared_loader_obj = action._loader
    action._low_level_execute_command = lambda *a, **kw: {'stdout': 'PLATFORM\nLinux\nFOUND\n/usr/bin/python\nENDFOUND'}
    action._discovery_warnings = []


# Generated at 2022-06-12 21:35:39.672321
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.module_utils.discovery import InterpreterDiscovery
    import unittest

    try:
        import pytest
    except ImportError:
        pytest = None

    class TestInterpreterDiscovery(unittest.TestCase):
        def setUp(self):
            self.discovery_plugin = InterpreterDiscovery()

            # mock the module run function so we can test the discovery
            from ansible.plugins.action.normal import ActionModule
            action_module = ActionModule(task=None, connection=None, play_context=None, loader=None,
                                         templar=None, shared_loader_obj=None)
            action_module._shared_loader_obj = None
            action_module._task = None
            action_module._job_vars = {}
            action_module._play_context

# Generated at 2022-06-12 21:35:50.734198
# Unit test for function discover_interpreter
def test_discover_interpreter():
    import ansible.executor.discovery.python_target as python_target

    # test data
    py4 = u'/usr/bin/python4'
    py3 = u'/usr/bin/python3'
    py2 = u'/usr/bin/python2'

    # discovered python interpreters
    found = [py4]

    # platform info from python script on target

# Generated at 2022-06-12 21:35:58.048567
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # pylint: disable=protected-access
    # test with no connection to establish and no interpreter available
    ac = object()
    ac._connection = object()
    ac._connection._shell = object()
    ac._connection._shell.path_depth = 4
    ac._connection._shell._executable = "/bin/bash"
    task_vars = dict()
    task_vars['inventory_hostname'] = 'localhost'
    result = discover_interpreter(ac, 'python', 'auto', task_vars)
    assert result == 'python'



# Generated at 2022-06-12 21:36:08.633689
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.facts.system.distribution import DistributionFactCollector
    from ansible.module_utils.facts.utils import get_file_content

    class DummyModule(AnsibleModule):
        pass

    class DummyRunner(object):
        def __init__(self, become_user, become_method, become_flags):
            pass

    class ActionModule(object):
        _discovery_warnings = []

        def __init__(self, runner_type, source_file=None, action_plugins=None, runner_on_failed=None):
            self.runner = DummyRunner('run_as', 'unused_become_method', 'unused_become_flags')


# Generated at 2022-06-12 21:36:17.913969
# Unit test for function discover_interpreter
def test_discover_interpreter():
    class DiscoveryAction(object):
        def __init__(self):
            self._connection = None
            self._discovery_warnings = None

        def _low_level_execute_command(self, cmd, sudoable=False, in_data=None):
            if cmd == "command -v 'python3'":
                return {'stdout': '/usr/bin/python3'}

            if cmd == "command -v 'python'":
                return {'stdout': '/usr/bin/python'}

            if cmd == '/usr/bin/python':
                return {'stdout': json.dumps({})}

            if cmd == '/usr/bin/python3':
                return {'stdout': json.dumps({'platform_dist_result': ['fedora', '27', '']})}

            return None

    #

# Generated at 2022-06-12 21:36:56.141538
# Unit test for function discover_interpreter
def test_discover_interpreter():
    """ Unit test for interpreter discovery module """
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.connection import Connection

    class MockAction(object):
        def __init__(self):
            self._low_level_execute_command = None
            self._connection = None
            self._discovery_warnings = []

        def set_low_level_execute_command(self, func):
            self._low_level_execute_command = func

        def set_connection(self, connection):
            self._connection = connection

        @property
        def discovery_warnings(self):
            return self._discovery_warnings

    action = MockAction()

    task_vars = {'inventory_hostname': 'localhost'}
    interpreter_name = 'python'

# Generated at 2022-06-12 21:37:06.170510
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # This works by mocking the action that the discover_interpreter function
    # is called by, and mocking the two low level command calls that are made.
    # This function can then call the discover_interpreter function and
    # provide expected results to test against.
    from ansible.module_utils.common.removed import removed
    from ansible.module_utils.six import text_type
    from io import StringIO

    class TestModuleAction:
        def __init__(self, host, display_warnings):
            self.host = host
            self.display_warnings = display_warnings
            self._discovery_warnings = []


# Generated at 2022-06-12 21:37:13.749482
# Unit test for function discover_interpreter
def test_discover_interpreter():
    my_path = "/usr/bin/python3"
    class MockAction(object):
        def __init__(self):
            self._connection = object()
            self._discovery_warnings = []

        def _low_level_execute_command(self, cmd, sudoable=False, in_data=None):
            class MockResult(object):
                def __init__(self):
                    self.stdout = "PLATFORM\nLinux\nFOUND\n{my_path}\nENDFOUND".format(my_path=my_path)
            return MockResult()

    class MockConnection(object):
        def __init__(self, has_pipelining):
            self.has_pipelining = has_pipelining

    class MockTaskVars(object):
        def __init__(self):
            pass

# Generated at 2022-06-12 21:37:19.047992
# Unit test for function discover_interpreter
def test_discover_interpreter():

    # test distro mapping
    platform_python_map = {
        'centos': {
            '6': '/usr/local/bin/python',
            '7': '/usr/bin/python',
            '8': '/usr/bin/python3',
        }
    }
    task_vars = {'ansible_interpreter_python': C.DEFAULT_INTERPRETER_PYTHON,
                 'ansible_interpreter_python_discovery': C.DEFAULT_INTERPRETER_DISCOVERY,
                 'ansible_interpreter_python_distro_map': platform_python_map}

    # Test discovery in discovery mode auto_legacy
    discovery_mode = 'auto_legacy'
    interpreter_name = 'python'
    action = _get_action(task_vars)


# Generated at 2022-06-12 21:37:29.426655
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.executor.task_result import TaskResult
    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins.action.script import ActionModule as ScriptAction
    from ansible.plugins.action.shell import ActionModule as ShellAction

    # LANG env is set to en_US.UTF-8 on Docker image
    # this test should be updated to run on Python 2.6

# Generated at 2022-06-12 21:37:36.804106
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # Create a dummy dict containing all the required fields.
    action = dict()
    interpreter_name = "python"
    discovery_mode = "auto"
    task_vars = dict()
    task_vars['ansible_python_interpreter'] = ''
    task_vars['ansible_python_version'] = ''
    task_vars['ansible_python_version_full'] = ''
    task_vars['ansible_python_full_version'] = ''
    task_vars['ansible_python_major_version'] = ''
    task_vars['ansible_python_arch'] = ''
    task_vars['ansible_python_distribution'] = ''
    task_vars['ansible_python_distribution_release'] = ''

# Generated at 2022-06-12 21:37:46.576799
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.plugins.action.wait_for import ActionModule as WaitForActionModule
    from ansible.plugins.action.copy import ActionModule as CopyActionModule
    import ansible.plugins.connection.local as local
    import ansible.plugins.action.script as script
    import ansible.utils.plugin_docs as pd

    display = Display()
    display.verbosity = 6

    # Setup an action module to call discover_interpreter
    class ActionModule(CopyActionModule):
        _discovery_warnings = []

    # Setup a task
    task = dict(
        command=dict(
            interpreter=u'python',
            discovery_mode=u'auto',
        ),
        action=u'copy',
        _ansible_verbosity=6,
    )

# Generated at 2022-06-12 21:37:59.229493
# Unit test for function discover_interpreter
def test_discover_interpreter():
    module_name = 'test_interpreter_discovery'
    module_args = dict()

    # This will be the action plugin.  We're just testing the interpreter discovery function,
    # so this will only be used to hold task_vars.
    from ansible.plugins.action import ActionBase
    class TestAction(ActionBase):
        def run(self, tmp=None, task_vars=None):
            # We don't actually run the action.
            raise AssertionError('Should not get here')
    action = TestAction(task=dict(action=dict(module_name=module_name, module_args=module_args)))
    action._discovery_warnings = []

    # We need a host.
    task_vars = dict()

# Generated at 2022-06-12 21:38:07.874122
# Unit test for function discover_interpreter

# Generated at 2022-06-12 21:38:11.980305
# Unit test for function discover_interpreter
def test_discover_interpreter():
    res = discover_interpreter(None, 'python', 'auto', {})
    if not res:
        print('discover_interpreter returned None')
        return False

    if res != u'/usr/bin/python':
        print('discover_interpreter returned unexpected result: {0}'.format(res))
        return False

    return True



# Generated at 2022-06-12 21:39:19.077100
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # Test with invalid interpreter name
    try:
        discover_interpreter('action', 'invalid_interpreter', 'auto')
    except ValueError as e:
        assert 'not supported' in to_native(e)
    # Test with invalid discovery mode
    try:
        discover_interpreter('action', 'python', 'invalid_discovery_mode')
    except ValueError as e:
        assert 'not supported' in to_native(e)

    # Test for python
    try:
        discover_interpreter('action', 'python', 'auto_legacy_silent', 'task_vars')
    except NotImplementedError as e:
        assert 'unable to get Linux distribution/version info' in to_native(e)



# Generated at 2022-06-12 21:39:29.067807
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.module_utils.basic import AnsibleModule

    class TestModule(object):
        def __init__(self, interpreter_name, discovery_mode, task_vars):
            self.interpreter_name = interpreter_name
            self.discovery_mode = discovery_mode
            self.task_vars = task_vars
            # The following are necessary to avoid failures when running the unit tests (with TestModule)
            # and in the normal execution path.
            self.deprecation_warnings = []
            self.fail_json = AnsibleModule._fail_json
            self.exit_json = AnsibleModule._exit_json

    module = TestModule('python', 'auto_legacy_silent', dict())

# Generated at 2022-06-12 21:39:40.122327
# Unit test for function discover_interpreter
def test_discover_interpreter():

    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from ansible.plugins.action import ActionBase


# Generated at 2022-06-12 21:39:49.033732
# Unit test for function discover_interpreter
def test_discover_interpreter():
    interpreter_name = 'python'
    discovery_mode = 'auto'
    task_vars = {'INTERPRETER_PYTHON_DISTRO_MAP': {'ubuntu': {'14.04': '/usr/bin/python2.7',
                                                              '16.04': '/usr/bin/python2.7'}},
                 'INTERPRETER_PYTHON_FALLBACK': ['/usr/bin/python3', '/usr/bin/python2.7']}
    action = type("ActionClass", (object,), {'_low_level_execute_command': _test_command,
                                             '_discovery_warnings': []})()
    interpreter = discover_interpreter(action, interpreter_name, discovery_mode, task_vars)

# Generated at 2022-06-12 21:39:59.845573
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible_collections.misc.not_a_real_collection.plugins.module_utils.gathering.interpreter_discovery import discover_interpreter

    # Test for a valid interpreter name