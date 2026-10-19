

# Generated at 2022-06-12 21:30:18.105100
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from unittest import mock
    from ansible.errors import AnsibleAction, AnsibleActionFail
    from ansible.plugins.action import ActionBase
    from ansible.plugins.loader import ActionModuleLoader

    test_host = 'testhost'
    interpreter = 'python'

    # A mock class for ActionBase, since we can't create one easily
    class MockAction(ActionBase):
        def __init__(self, action, host, connection):
            super(MockAction, self).__init__(action, host, connection)
            self._discovery_warnings = []
            self._low_level_execute_command = mock.MagicMock()

    # A mock class for ActionModuleLoader.load_action_plugin, since it's staticmethod

# Generated at 2022-06-12 21:30:24.563487
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # test no double-backslash needed when path contains $HOME
    assert discover_interpreter(None, 'python', "auto_legacy_silent", dict(HOME="/home/user")) == "/usr/bin/python"

    # test double-backslash needed when path contains backslashes
    assert discover_interpreter(None, 'python', "auto_legacy_silent", dict(HOME=r"C:\Program Files\Ansible")) == r"C:\\Program Files\\Python36\\python.exe"

# Generated at 2022-06-12 21:30:33.166491
# Unit test for function discover_interpreter
def test_discover_interpreter():
    import unittest
    import ansible.module_utils.discovery
    from ansible.module_utils.common.process import get_bin_path
    import ansible.module_utils.discover_interpreter_version

    class TestModule(object):
        def __init__(self, interpreter, version, version_jessie, version_stretch, version_buster, version_bullseye):
            d = {}
            d.update(interpreter)
            d.update(version)
            d.update(version_jessie)
            d.update(version_stretch)
            d.update(version_buster)
            d.update(version_bullseye)

            self.check_mode = False
            self.no_log = False
            self.args = dict()
            self._debug = []
           

# Generated at 2022-06-12 21:30:34.223742
# Unit test for function discover_interpreter
def test_discover_interpreter():
    pass

# Generated at 2022-06-12 21:30:45.270132
# Unit test for function discover_interpreter
def test_discover_interpreter():
    mock_action = MockAction()
    # Existing interpreter
    interpreter_path = discover_interpreter(mock_action, 'python', 'auto', dict())
    assert interpreter_path == u'/usr/bin/python'
    # interpreter is missing
    mock_action.setResult(b"PLATFORM\nLinux\nFOUND\nENDFOUND")
    interpreter_path = discover_interpreter(mock_action, 'python', 'auto_silent', dict())
    assert interpreter_path == u'/usr/bin/python'
    # interpreter discovery is required
    mock_action.setResult(b"PLATFORM\nLinux\nFOUND\nENDFOUND")

# Generated at 2022-06-12 21:30:56.494997
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.executor.discovery import discover_interpreter
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.connection import Connection

    from ansible.inventory.host import Host

    from ansible.playbook.play_context import PlayContext

    from ansible.plugins import action

    acon = Connection(
        host=Host(name=u'localhost')
    )

    acon._connection = None
    acon._shell = None
    dummy_loader = action.ActionModule(acon, to_bytes(u'/test/test'), False, u'always', False, False, False)

    pcon = PlayContext()
    pcon.connection = u'network_cli'

    tsk = action.Task()
    tsk.async_val = 0

# Generated at 2022-06-12 21:31:05.776470
# Unit test for function discover_interpreter
def test_discover_interpreter():
    task_vars = dict()

    action = object()
    action._discovery_warnings = []
    action._connection = object()
    action._connection.has_pipelining = True

    class _ActionModule:
        def __init__(self, action):
            self.action = action
            self.module_name = ''

        def _low_level_execute_command(self, cmd, sudoable=False, in_data=None):
            if cmd == '/usr/bin/python':
                return {'stdout':
                    '''
                    PLATFORM
                    Linux
                    FOUND
                    /usr/bin/python3
                    /usr/bin/python
                    ENDFOUND
                    ''',
                        'stderr': ''}

# Generated at 2022-06-12 21:31:07.694398
# Unit test for function discover_interpreter
def test_discover_interpreter():
    assert discover_interpreter('','','',{}) == u'/usr/bin/python'

# Generated at 2022-06-12 21:31:18.740658
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.plugins.action import ActionModule

    class MockActionModule(ActionModule):
        def __init__(self, task_vars):
            self._task_vars = task_vars
            self._connection = None
            self._task = None
            self._loader = None
            self._templar = None
            self._play_context = None
            self._discovery_warnings = []


# Generated at 2022-06-12 21:31:24.861759
# Unit test for function discover_interpreter
def test_discover_interpreter():
    fake_action_class = type('FakeAction', (object,), dict())
    fake_action = fake_action_class()
    fake_action._discovery_warnings = []
    task_vars = dict()

    fake_connection_class = type('Connection', (object,), dict(has_pipelining=True))
    fake_connection = fake_connection_class()
    fake_action._connection = fake_connection

    base_cmd = u"command -v '{0}'"

# Generated at 2022-06-12 21:31:37.494654
# Unit test for function discover_interpreter
def test_discover_interpreter():
    assert discover_interpreter(None, 'python', 'auto_legacy_silent', {}) == u'/usr/bin/python'


# Generated at 2022-06-12 21:31:46.822078
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # Tests assume python interpreter is at /usr/bin/python
    mytask_vars = {'ansible_python_interpreter': '/usr/bin/python'}
    # Tests assume no python interpreters present at /usr/bin/python2
    mytask_vars['ansible_python_interpreter'] = '/usr/bin/python2'

    test_interpreter_name = 'python'
    test_action = 'dummy'


# Generated at 2022-06-12 21:31:55.462946
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # Test legacy auto_legacy mode
    result = discover_interpreter(action=None, interpreter_name='python', discovery_mode='auto_legacy', task_vars={
        'inventory_hostname': 'localhost',
        'ansible_connection': 'smart',
        'ansible_python_interpreter': '/path/to/python',
        'group_names': [],
        'groups': {
            'all': {
                'hosts': ['localhost'],
            }
        }
    })
    assert result == u'/usr/bin/python'
    pass



# Generated at 2022-06-12 21:32:03.288943
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.executor.discovery.legacy_interpreter_discovery import _get_versioned_python_interpreter
    from ansible.executor.discovery.legacy_interpreter_discovery import get_fallback_python
    from ansible.executor.discovery.legacy_interpreter_discovery import _get_python_interpreter_for_platform
    import ansible.module_utils.basic
    action = ansible.module_utils.basic.AnsibleModule(argument_spec={}, supports_check_mode=True)

    # does not call module_utils.basic._load_params(),
    # so we cannot use `action._task.args`
    task_vars = {}

    # attempt to discover interpreter, but get a NotImplementedError,
    # so try the fallback

# Generated at 2022-06-12 21:32:16.642410
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # Cause a failure
    task_vars = dict(inventory_hostname='badHost')
    action = "dummy"
    interpreter_name='test'
    discovery_mode='test'
    try:
        discover_interpreter(action, interpreter_name, discovery_mode, task_vars)
    except Exception as err:
        if isinstance(err, InterpreterDiscoveryRequiredError):
            if err.interpreter_name != 'test':
                raise Exception("Incorrect error interpreter_name value: " + err.interpreter_name)
            if err.discovery_mode != 'test':
                raise Exception("Incorrect error discovery_mode value: " + err.discovery_mode)
        else:
            raise Exception("Wrong type of exception thrown")
    else:
        raise Exception("Exception not raised")

   

# Generated at 2022-06-12 21:32:26.954474
# Unit test for function discover_interpreter
def test_discover_interpreter():
    '''
    Test interpreter discovery.
    :return:
    '''
    from ansible.plugins.loader import action_loader

    # Create an action and fake taskvars for Python 2
    action = action_loader.get('command')


# Generated at 2022-06-12 21:32:39.080346
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.executor.task_result import TaskResult
    from ansible.plugins.action import ActionBase
    from ansible.utils.vars import combine_vars

    class ActionModule(ActionBase):
        def _low_level_execute_command(self, cmd, in_data=None, sudoable=True):
            if cmd == 'command -v /usr/bin/python':
                return TaskResult(result={'rc': 0, 'stdout': '/usr/bin/python', 'stderr': ''})
            elif cmd == 'command -v /usr/bin/python2':
                return TaskResult(result={'rc': 0, 'stdout': '/usr/bin/python2', 'stderr': ''})

# Generated at 2022-06-12 21:32:47.222158
# Unit test for function discover_interpreter
def test_discover_interpreter():
    import pytest
    from collections import namedtuple

    test_action = namedtuple('ActionModule', ['_low_level_execute_command', '_connection', '_discovery_warnings'])
    test_task_vars = namedtuple('TaskVars', ['inventory_hostname', 'ansible_connection', 'ansible_python_interpreter'])


# Generated at 2022-06-12 21:32:55.070316
# Unit test for function discover_interpreter

# Generated at 2022-06-12 21:33:06.927546
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins.loader import action_loader
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.task_result import TaskResult
    from ansible.module_utils.connection import Connection

    def mock_llec(module_name, module_args=None, task_vars=None, tmp=None, sudoable=True,
                  chdir=None, executable=None, stdin=None, stdin_add_newline=True, use_persistent_connection=False,
                  strip_before_search=False, strip_after_search=False):
        return dict(cmd='', rc=0, stdout='', stderr='')


# Generated at 2022-06-12 21:33:22.125244
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.module_utils.six import binary_type
    from ansible.module_utils import basic
    from ansible.plugins.action import ActionBase

    # set up a test action, since we don't have any module_utils stuff in play here
    # FUTURE: if the test_runner stuff gets refactored enough, we can probably use that and not bother with this
    display.verbosity = 4
    action = ActionBase()

    test_host = u'example.org'

    # FUTURE: unify this with the stuff in test/units/module_utils/basic.py
    def _make_task_var(host, undef=False):
        if undef:
            return dict(inventory_hostname=host, ansible_check_mode=False, ansible_version=C.__version__)

# Generated at 2022-06-12 21:33:32.495085
# Unit test for function discover_interpreter
def test_discover_interpreter():
    import sys
    import os
    import tempfile
    import shutil
    import pytest
    import yaml


# Generated at 2022-06-12 21:33:39.695553
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.plugins.action import ActionBase
    from ansible.executor.task_result import TaskResult
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.play_iterator import PlayIterator
    from ansible.playbook.play import Play
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager


# Generated at 2022-06-12 21:33:52.322409
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.plugins.action import ActionBase

    class TestAction(ActionBase):
        _discovery_warnings = []
        _connection = None

        class TestConnection:
            has_pipelining = True

            @staticmethod
            def _low_level_execute_command(command, sudoable=False, in_data=None):
                if command == 'echo PLATFORM; uname; echo FOUND; command -v \'python3\'; echo ENDFOUND':
                    return {'stdout': 'PLATFORM\nLinux\nFOUND\n/usr/bin/python3\nENDFOUND'}

# Generated at 2022-06-12 21:33:59.615487
# Unit test for function discover_interpreter
def test_discover_interpreter():

    import unittest
    from ansible.module_utils.six import PY3
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.discovery import InterpreterDiscoveryRequiredError
    from ansible.module_utils.common.text.converters import (
        to_text,
    )
    from ansible.module_utils.common.collections import ImmutableDict

    class ShellModuleFake(object):

        class FakeConnection(object):

            def __init__(self, has_pipeline=True):
                self.has_pipelining = has_pipeline

        def __init__(self, action_attrs, connection, task_vars=None):
            self._attributes = action_attrs
            self._connection = connection

# Generated at 2022-06-12 21:34:03.262444
# Unit test for function discover_interpreter
def test_discover_interpreter():
    assert discover_interpreter('python', '', 'auto_legacy_silent', {'inventory_hostname': 'localhost'}) == u'/usr/bin/python'

# Generated at 2022-06-12 21:34:12.771499
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # Test a basic case of an interpreter not in the python fallback list
    python_versions = [ u'/usr/bin/python', u'/usr/bin/python2.6', u'/usr/bin/python2.7']
    for ver in python_versions:
        task_vars = dict()
        task_vars['inventory_hostname'] = u'example.com'
        task_vars['ansible_python_interpreter'] = ver
        interpreter_name = u'python'
        expected_result = u'/usr/bin/python2.7'
        discovery_mode = u'auto_legacy'

        # default interpreter_name of python - should also work for python3
        res = discover_interpreter(None, interpreter_name, discovery_mode, task_vars)
        assert res == expected_result

   

# Generated at 2022-06-12 21:34:19.967886
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.module_utils.common._collections_compat import Mapping, Sequence

    # TODO: stub out action and host vars when we get around to implementing unit test infrastructure
    assert isinstance(C.config.get_config_value('INTERPRETER_PYTHON_DISTRO_MAP'), Mapping)
    assert isinstance(C.config.get_config_value('INTERPRETER_PYTHON_FALLBACK'), Sequence)

    # TODO: stub out action when we get around to implementing unit test infrastructure
    assert isinstance(discover_interpreter(None, 'python', 'auto', {}), str)

# Generated at 2022-06-12 21:34:20.913647
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # FIXME
    pass

# Generated at 2022-06-12 21:34:28.417479
# Unit test for function discover_interpreter
def test_discover_interpreter():
    platform_python_map = C.config.get_config_value('INTERPRETER_PYTHON_DISTRO_MAP', variables={})
    bootstrap_python_list = C.config.get_config_value('INTERPRETER_PYTHON_FALLBACK', variables={})
    action = None
    assert discover_interpreter(action, "python", "legacy", {}) == u'/usr/bin/python'
    assert discover_interpreter(action, "python3", "legacy", {}) == u'/usr/bin/python3'
    assert discover_interpreter(action, "python", "auto_legacy", {}) == u'/usr/bin/python'
    assert discover_interpreter(action, "python3", "auto_legacy", {}) == u'/usr/bin/python3'

# Generated at 2022-06-12 21:34:40.801384
# Unit test for function discover_interpreter
def test_discover_interpreter():
    action = MockActionModule()
    results = discover_interpreter(action, 'python', 'auto', {})

    assert results is not None



# Generated at 2022-06-12 21:34:44.801640
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.executor.discovery import InterpreterDiscoveryRequiredError, discover_interpreter, \
        _get_linux_distro

    from ansible.errors import AnsibleError

    from ansible.playbook.play_context import PlayContext
    from ansible.plugins import action_loader
    from ansible.template import Templar
    from ansible.vars import VariableManager

    # test case 1: invalid distribution map
    platform_python_map = {'suse': {'blah': '/usr/bin/python'}}
    discovery_mode = 'auto'

    action = action_loader._create_action_plugin('script')
    action.validate()

    display.verbosity = 4

# Generated at 2022-06-12 21:34:55.333977
# Unit test for function discover_interpreter
def test_discover_interpreter():
    class Action():
        _low_level_execute_command = lambda *args, **kwargs: {'stdout': args[0]}
        _low_level_execute_script = lambda *args, **kwargs: {'stdout': args[1]}
        _discovery_warnings = []
        _connection = lambda *args, **kwargs: {'has_pipelining': args[0]}

    # FUTURE: test exceptions where appropriate

    def _run_dic(*args):
        return discover_interpreter(*args, task_vars={})

    # TODO: make sure this data structure has everything it needs to
    # TODO: use real data from yaml file?

# Generated at 2022-06-12 21:35:03.044533
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # Test for interpreter name 'python'
    try:
        discover_interpreter(action=None, interpreter_name='python', discovery_mode='auto_legacy_silent', task_vars={})
        #If no exception is raised, then the test is passed
        assert True
    except Exception as e:
        # If exception raises, then the test is failed
        assert False, e

    # Test for interpreter name not 'python'
    try:
        discover_interpreter(action=None, interpreter_name='python3', discovery_mode='auto_legacy_silent', task_vars={})
        # If no exception is raised, then the test is passed
        assert False
    except Exception as e:
        # If exception raises, then the test is failed
        assert True, e

# Generated at 2022-06-12 21:35:11.273278
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.plugins.action import ActionModule
    from ansible.plugins.action.discovery import ActionModule as DiscoveryActionModule

    def get_interpreter_path(action, interpreter_name, discovery_mode):
        task_vars = dict(inventory_hostname='localhost', ansible_python_interpreter='/usr/bin/python')
        action.set_task_vars(task_vars)
        return discover_interpreter(action, interpreter_name, discovery_mode, task_vars)

    # first test silent fallback-only path
    mock_action = DiscoveryActionModule(task=None, connection=None, play_context=None, loader=None, templar=None,
                                        shared_loader_obj=None)
    mock_action._discovery_warnings = []
    mock_action._connection

# Generated at 2022-06-12 21:35:22.338833
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # Global imports
    from ansible.plugins.action import ActionBase
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_result import TaskResult

    # Create action
    class ActionPlugin(ActionBase):
        def __init__(self, task, connection, play_context, loader, templar, shared_loader_obj):
            super(ActionPlugin, self).__init__(task, connection, play_context, loader, templar, shared_loader_obj)
            self._shell = None
            self._low_level_shell = None
            self._discovery_warnings = []

        def run(self, tmp=None, task_vars=None):
            return TaskResult(result=dict())


# Generated at 2022-06-12 21:35:31.204380
# Unit test for function discover_interpreter
def test_discover_interpreter():
    assert discover_interpreter(None, 'python', 'auto', {'inventory_hostname': 'localhost', 'platform': 'linux'}) == '/usr/bin/python'
    assert discover_interpreter(None, 'python', 'auto', {'inventory_hostname': 'localhost', 'platform': 'freebsd'}) == '/usr/bin/python'
    assert discover_interpreter(None, 'python', 'auto_silent', {'inventory_hostname': 'localhost', 'platform': 'linux'}) == '/usr/bin/python'
    assert discover_interpreter(None, 'python', 'auto_silent', {'inventory_hostname': 'localhost', 'platform': 'freebsd'}) == '/usr/bin/python'

# Generated at 2022-06-12 21:35:39.039764
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # Test centos7.3
    # Test centos7.1
    # Test centos6.8
    # Test ubuntu 16.04
    # Test rhel8.0
    # Test rhel7.6
    # Test rhel6.0
    # Test fedora 30
    # Test fedora 29
    # Test fedora 28
    # Test fedora 27
    # Test debian 8
    # Test debian 9
    # Test debian 10
    pass

# Generated at 2022-06-12 21:35:50.007934
# Unit test for function discover_interpreter
def test_discover_interpreter():
    class my_action():
        def __init__(myself):
            myself._connection = myself
            myself._connection.has_pipelining = False
            myself._discovery_warnings = []

        def _low_level_execute_command(myself, command, sudoable=False, in_data=None):
            # echo the output of platform.dist
            if command == '/usr/bin/python':
                return dict(stdout=b'{"platform_dist_result":["centos","6.10","Final"]}')

            # echo the output of uname

# Generated at 2022-06-12 21:35:53.940250
# Unit test for function discover_interpreter
def test_discover_interpreter():
    test_action = ActionModule()
    test_interpreter_name = 'python'
    test_discovery_mode = 'forced'
    test_task_vars = dict()
    print(discover_interpreter(test_action, test_interpreter_name, test_discovery_mode, test_task_vars))



# Generated at 2022-06-12 21:36:14.862647
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.module_utils.distro import LinuxDistribution
    from ansible.utils.plugin_docs import get_versioned_doclink
    from ansible.executor.discovery import _version_fuzzy_match

    class MockAction(object):
        _discovery_warnings = []

        def __init__(self, host, data):
            self._connection = MockConnection(host, data)

        def _low_level_execute_command(self, name, sudoable=True, in_data=None):
            res = self._connection.run(name, in_data)
            res['parsed'] = True
            if res.get('rc', 0) != 0:
                raise Exception('Mock execute command failed')
            return res


# Generated at 2022-06-12 21:36:21.424535
# Unit test for function discover_interpreter
def test_discover_interpreter():
    import os
    from ansible.module_utils.six.moves import StringIO
    from ansible.module_utils.six import PY3

    tmpdir = os.path.join(os.path.dirname(__file__), os.path.pardir, 'tmp')
    os.makedirs(tmpdir, mode=0o700, exist_ok=True)

    with open(os.path.join(tmpdir, 'python_target.py'), 'w') as f:
        if PY3:
            f.write("#!/usr/bin/python3\n")
        else:
            f.write("#!/usr/bin/python\n")
        f.write("import json\n")
        f.write("import platform\n")
        f.write("import os\n")
        f.write

# Generated at 2022-06-12 21:36:22.570948
# Unit test for function discover_interpreter
def test_discover_interpreter():
    pass

# Generated at 2022-06-12 21:36:33.865724
# Unit test for function discover_interpreter
def test_discover_interpreter():
    import unittest

    import ansible.module_utils.distro
    from ansible.module_utils.distro import distro_detection_mock_data

    class TestModule(unittest.TestCase):
        def setUp(self):
            # mock global get_distribution_version()
            self.original_get_distribution_version = ansible.module_utils.distro.get_distribution_version
            ansible.module_utils.distro.get_distribution_version = self.mock_get_distribution_version

        def tearDown(self):
            # restore global get_distribution_version()
            ansible.module_utils.distro.get_distribution_version = self.original_get_distribution_version

        def mock_get_distribution_version(self):
            return self

# Generated at 2022-06-12 21:36:38.398692
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.plugins.action.script import ActionModule as script_module

    # Instantiate a script module
    action_script = script_module(task=dict(), connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    interpreter = discover_interpreter(action_script, 'python', 'auto', dict())
    assert interpreter != None

# Generated at 2022-06-12 21:36:44.212999
# Unit test for function discover_interpreter
def test_discover_interpreter():

    from ansible.module_utils.discovery.python_interpreter import discover_interpreter
    from ansible.module_utils.connection import Connection
    from ansible.executor.task_result import TaskResult
    from ansible.module_utils.network.common.utils import to_list

    dummy_result = TaskResult(
        'localhost',
        'setup',
        {},
        'ok',
        'non-json-result-was-here',
        'no_plugin',
        'no_plugin',
        'no_plugin',
    )

    # Discovery must be done with a pipelining connection.
    test_connection = Connection('localhost')
    test_connection.has_pipelining = True

    # Simple test

# Generated at 2022-06-12 21:36:53.854993
# Unit test for function discover_interpreter
def test_discover_interpreter():
    ## Test case 1: uname_output is linux, dist_output is empty dict
    def test_discover_interpreter_case1(monkeypatch):
        version_map = {"1.1": '/usr/bin/python1', "2.2": '/usr/bin/python2'}

        def _version_fuzzy_match(version, version_map):
            return version_map.get(version)

        monkeypatch.setattr("ansible.executor.discovery.python.version_fuzzy_match", _version_fuzzy_match)
        assert discover_interpreter(None, 'python', 'legacy', None) == '/usr/bin/python1'


# Generated at 2022-06-12 21:37:02.263752
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_result import TaskResult
    action = TaskResult(host=object(), task=object(), task_fields=dict(action=dict()))
    play_context = PlayContext()
    action._low_level_execute_command = lambda x, sudoable, in_data: {'stdout': x}
    action._connection = MockConnection()
    action._connection.has_pipelining = True
    task_vars = dict()
    assert discover_interpreter(action, 'python', 'auto', task_vars) == '/usr/bin/python'



# Generated at 2022-06-12 21:37:10.897728
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.plugins.action.script import ActionModule
    from ansible.plugins.shell.bash import ActionModule as BashActionModule
    from ansible.plugins.shell.sh import ActionModule as ShActionModule
    class FakeActionModule(ActionModule):
        _shell = BashActionModule
        _shell_executable = 'bash'
        ACTION_WARNINGS = []

        def _get_connection(self):
            return FakeConnection()

    class FakeConnection:
        def __init__(self):
            self._shell = BashActionModule
            self._shell_executable = 'bash'

        def has_pipelining(self):
            return True

        def _connect(self):
            pass

        def exec_command(self):
            return dict()

        def _check_shell_executable(self):
            pass


# Generated at 2022-06-12 21:37:19.959425
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # set up a basic action for the test
    action = MockAction()

    # set up a basic task_vars for the test
    task_vars = {}

    # set up a basic config for the test
    C.config = MockConfig()

    # test without the changes to C.config
    result = discover_interpreter(action, interpreter_name='python', discovery_mode='auto_legacy_silent', task_vars=task_vars)
    assert result == '/usr/bin/python'
    assert action._discovery_warnings == []

    # test with the changes to C.config
    C.config._data = {
        'DEFAULT': {
            'ANSIBLE_INTERPRETER_DISCOVERY_MODE': "auto_legacy_silent",
        }
    }

    result = discover_

# Generated at 2022-06-12 21:38:01.388103
# Unit test for function discover_interpreter
def test_discover_interpreter():
    '''
    Test discover_interpreter()
    Test cases to run:
      - 1 actions, 3 interpreter_name, 3 discovery_mode, 1 task_vars
          1 * 3 * 3 * 1 = 9 * 3 = 27
    '''
    action_list = ['ping', 'service', 'setup']
    interpreter_name_list = ['python', 'python2', 'python3']
    discovery_mode_list = ['auto_legacy_silent', 'auto_legacy', 'auto_current']
    task_vars_list = ['', ]


# Generated at 2022-06-12 21:38:09.523186
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from .discovery_test_fakes import ActionModule
    from .discovery_test_fakes import Connection
    import ansible.playbook.task_include
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    import ansible.compat.six as six
    import os

    # We are using in-memory objects but they are similar to normal inventory
    loader = DataLoader()
    var_manager = VariableManager()
    host = InventoryManager(loader=loader, sources=('')).get_host('localhost')
    var_manager.set_host_variable(host, 'ansible_python_interpreter', '/usr/bin/python')

# Generated at 2022-06-12 21:38:12.260605
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.plugins.action import ActionBase
    action = ActionBase()
    action._discovery_warnings = []
    assert discover_interpreter(action, 'python', 'auto', dict()) == '/usr/bin/python'

# Generated at 2022-06-12 21:38:19.215354
# Unit test for function discover_interpreter
def test_discover_interpreter():
    display = Display()
    display.verbosity = 4
    action = DummyAction('test_discover_interpreter')
    action._connection = DummyConnection()
    task_vars = dict()
    conf_dict = dict()

# Generated at 2022-06-12 21:38:20.441528
# Unit test for function discover_interpreter
def test_discover_interpreter():
    discover_interpreter(None, 'python', 'auto', None)

# Generated at 2022-06-12 21:38:23.550598
# Unit test for function discover_interpreter
def test_discover_interpreter():
    #We need a 'discovery_mode' param but it can be anything since it is not used for the test
    assert discover_interpreter(None,'python',None,None) == u'/usr/bin/python'



# Generated at 2022-06-12 21:38:29.670297
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.plugins.action import ActionBase
    class TestActionBase(ActionBase):
        _low_level_execute_command = lambda *args, **kwargs: dict(stdout='PLATFORM\nlinux\nFOUND\n/usr/bin/python\nENDFOUND')
    action = TestActionBase()
    action._discovery_warnings = []
    interpreter = discover_interpreter(action, 'python', 'auto', dict())
    assert interpreter == u'/usr/bin/python'

# Generated at 2022-06-12 21:38:38.966595
# Unit test for function discover_interpreter
def test_discover_interpreter():

    # Test connection class needed for testing
    class TestConnection:
        def __init__(self):
            self.has_pipelining = True

    # Test action class needed for testing
    class TestAction:
        def __init__(self):
            self._connection = TestConnection()
            self._discovery_warnings = []
            self._low_level_execute_command = None

    action = TestAction()

    # Basic test for checking to make sure we find python
    def _low_level_execute_command(command, sudoable=None, in_data=None):
        res = dict()
        if command == 'command -v \'python\'':
            res['stdout'] = u'/usr/bin/python'
        elif command == 'command -v \'python2\'':
            res['stdout'] = u''


# Generated at 2022-06-12 21:38:46.584829
# Unit test for function discover_interpreter
def test_discover_interpreter():
    task_vars = dict(
        ansible_python_interpreter=u'/usr/bin/python',
        ansible_distribution=u'Debian',
        ansible_distribution_version=u'8.0',
        ansible_distribution_major_version=u'8',
        inventory_hostname=u'localhost',
    )

    class Action(object):
        _low_level_execute_command_results = []

        def _low_level_execute_command(self, command, sudoable=True, in_data=None):
            return dict(
                stdout=self._low_level_execute_command_results.pop(0)
            )

        def _load_params(self):
            pass

        def _announce_deprecations(self, *args, **kwargs):
            pass

# Generated at 2022-06-12 21:38:55.853698
# Unit test for function discover_interpreter
def test_discover_interpreter():
    class Action:
        def __init__(self):
            self._discovery_warnings = []

        def _low_level_execute_command(self, cmd, sudoable=False, in_data=None):
            return {'stdout': cmd}

    task_vars = dict(
        ansible_distribution='RedHat',
        ansible_distribution_major_version='7',
    )
    action = Action()
    action.connection = Display()
    action.connection.has_pipelining = True

    C.config.initialize()

    assert discover_interpreter(action, "python", 'auto', task_vars) == '/opt/rh/rh-python36/root/usr/bin/python'



# Generated at 2022-06-12 21:39:50.011036
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # TODO: switch to using MockConnection
    from ansible.plugins.action import ActionBase
    from ansible.plugins.connection.local import Connection as LocalConnection
    from ansible.executor.discovery import discover_interpreter
    from ansible.module_utils.common.collections import ImmutableDict

    class MyAction(ActionBase):
        def _execute_module(self, tmp=None, task_vars=None, persist_files=True):
            return {}

    display.verbosity = 1

    # We need to override some distro mappings so the test doesn't care about specific distros
    # override the values for keys that exist, and add a new key for alpine

# Generated at 2022-06-12 21:40:01.044216
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # setup
    class MockAction(object):
        def __init__(self, in_data=None, stdout='', stderr='', rc=0):
            self._discovery_warnings = []
            self.in_data = in_data
            self.stdout = stdout
            self.stderr = stderr
            self.rc = rc
        def _low_level_execute_command(self, command, sudoable=True, in_data=None):
            if not in_data:
                return {'stdout': self.stdout, 'stderr': self.stderr, 'rc': self.rc}
            return {'stdout': self.stdout, 'stderr': self.stderr, 'rc': self.rc, 'in_data': self.in_data}