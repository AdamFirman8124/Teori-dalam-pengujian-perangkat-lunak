

# Generated at 2022-06-12 21:30:18.689754
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # TEST: Discovering interpreters.
    assert(discover_interpreter(action = None, interpreter_name = 'python', discovery_mode = "auto_legacy_silent", task_vars={}) == "/usr/bin/python")

# Generated at 2022-06-12 21:30:27.448281
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible import context
    from ansible.plugins.loader import action_loader
    from ansible.executor.task_result import TaskResult
    from ansible.vars.hostvars import HostVars
    from ansible.vars.manager import VariableManager

    context.CLIARGS = type('args', (object,), {
        'module_path': '',
        'roles_path': '',
        'lookup_plugins': '',
        'filter_plugins': '',
        'action_plugins': '',
    })()

    action = action_loader.get('command', class_only=True)
    task_vars = HostVars(
        sorted(
            {
                'inventory_hostname': 'localhost'
            }.items()
        )
    )
    vars_manager = Variable

# Generated at 2022-06-12 21:30:32.038596
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # FIXME: add unit test for discover_interpreter once it's not hidden behind a module name
    # FIXME: make sure that we're detecting and reporting when a py3-only module is run on an interpreter without py3
    # FIXME: add unit test for interpreter discovery with pipelining off, using a saved stdout value from a target
    # system with os-release and platform.dist() info for all supported distros?
    pass

# Generated at 2022-06-12 21:30:33.159859
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # TODO: use pytest and parametrize
    raise NotImplementedError

# Generated at 2022-06-12 21:30:35.212538
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # TODO: test_discover_interpreter, test_get_linux_distro, test_version_fuzzy_match
    pass

# Generated at 2022-06-12 21:30:43.252692
# Unit test for function discover_interpreter
def test_discover_interpreter():
    class ActionModule(object):
        def _low_level_execute_command(self, interp, sudoable=True, in_data=None):
            if interp == "/usr/bin/python":
                raw_stdout = u"PLATFORM\n'Linux'\nFOUND\n" \
                             u"/usr/bin/python\n/usr/bin/python2\n/usr/bin/python3\n" \
                             u"ENDFOUND\n"


# Generated at 2022-06-12 21:30:47.895925
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.playbook.task_include import TaskInclude
    task = TaskInclude()

    try:
        _ = discover_interpreter(task, 'perl', 'auto_legacy', None)
        assert False, "Should have thrown a ValueError"
    except ValueError:
        pass

    try:
        _ = discover_interpreter(task, 'python', 'auto_legacy', {'inventory_hostname': 'localhost'})
        assert False, "Should have thrown a NotImplementedError"
    except NotImplementedError:
        pass

# Generated at 2022-06-12 21:30:53.653787
# Unit test for function discover_interpreter
def test_discover_interpreter():
    task_vars = dict()
    task_vars['inventory_hostname'] = '127.0.0.1'
    action_class = MockAction()
    python_path = discover_interpreter(action_class, 'python', 'auto', task_vars)
    assert python_path == u'/usr/bin/python'



# Generated at 2022-06-12 21:30:57.948088
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.plugins.connection.local import Connection

    def _mock_execute_module(self, module_name, module_args, tmp=None, task_vars=None, **kwargs):
        module_output = {
            u'platform_dist_result': [u'CentOS', u'8.0', u''],
            u'osrelease_content': u'ID=centos\nVERSION="8 (Core)"\nVERSION_ID="8"\nVERSION_CODENAME=""\nPLATFORM_ID="platform:el8"\n',
        }


# Generated at 2022-06-12 21:31:06.104623
# Unit test for function discover_interpreter
def test_discover_interpreter():
    class ActionModule:
        def __init__(self, connection):
            self._connection = connection
            self._discovery_warnings = []

        def _low_level_execute_command(self, command, sudoable=False, in_data=None):
            # command is already escaped
            if command == "echo PLATFORM; uname; echo FOUND; command -v '/usr/bin/python'; echo ENDFOUND":
                return {
                    'stdout': 'PLATFORM\nLinux\nFOUND\n/usr/bin/python\nENDFOUND'
                }
            elif command == "/usr/bin/python":
                return {
                    'stdout': json.dumps({'osrelease_content': 'NAME="CentOS Linux"', 'platform_dist_result': ['', '', '']})
                }


# Generated at 2022-06-12 21:31:26.729613
# Unit test for function discover_interpreter
def test_discover_interpreter():
    try:
        # Neat trick, executing this module as a script will execute the unit tests
        import ansible.modules.system.uname as test_uname
        import ansible.modules.system.platform_dist as test_platform_dist
        import ansible.modules.system.os_release as test_os_release
    except ImportError as e:
        raise AssertionError('Failed to import test modules: %s' % to_native(e))


# Generated at 2022-06-12 21:31:39.502988
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # short circuit the rest of this test
    # pylint: disable=too-few-public-methods

    # TODO: improve coverage and tests on all the different modes and options
    class mock_action:
        def __init__(self):
            self._connection = mock_connection()
            self._discovery_warnings = list()

        def _low_level_execute_command(self, cmd, sudoable=False, in_data=None):
            if in_data:
                # pretend it's a script
                return {'stdout': '{"platform_dist_result": ["Debian", "9.4", "stretch"], "osrelease_content": "PRETEND_OS_RELEASE_CONTENT"}\n'}

# Generated at 2022-06-12 21:31:48.157784
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # Helpers
    class MockAction(object):
        """Pretend to be an action for testing purposes"""
        def __init__(self):
            self._connection = MockConnection()
            self._play_context = MockPlayContext()
            self._discovery_warnings = []

        def _low_level_execute_command(self, cmd, sudoable=True, in_data=None):
            """ Returns a result object with stdout set to the content of the command """
            return {'stdout': cmd}

    class MockTaskVars(object):
        """Pretend to be a task vars dict for testing purposes"""
        pass

    class MockConnection(object):
        """Pretend to be a connection"""
        def __init__(self):
            self.has_pipelining = True


# Generated at 2022-06-12 21:31:58.831148
# Unit test for function discover_interpreter
def test_discover_interpreter():

    assert discover_interpreter('python', 'auto', '', '') == u'/usr/bin/python'
    assert discover_interpreter('python', 'auto_legacy', '', '') == u'/usr/bin/python'
    assert discover_interpreter('python', 'auto_legacy_silent', '', '') == u'/usr/bin/python'

    action_class = type("ActionBase", (object,), {})()
    action_class._discovery_warnings = []

    assert discover_interpreter('python', 'auto_silent', '', action_class) == u'/usr/bin/python'
    assert len(action_class._discovery_warnings) == 1

    action_class._discovery_warnings = []

# Generated at 2022-06-12 21:32:10.519775
# Unit test for function discover_interpreter

# Generated at 2022-06-12 21:32:22.418880
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.plugins.action.command import ActionModule as CommandActionModule
    import ansible.plugins.action.python_interpreter as py
    import ansible.plugins.action.script as action_script
    import ansible.plugins.connection.local as connection_local
    import ansible.plugins.connection.chroot as connection_chroot
    import ansible.plugins.connection.ssh as connection_ssh
    import ansible.plugins.connection.winrm as connection_winrm
    import ansible.playbook.play_context as play_context

    #### Source files for python_target.py
    src_dir = os.path.dirname(os.path.dirname(ansible.plugins.action.python_interpreter.__file__))

# Generated at 2022-06-12 21:32:27.474517
# Unit test for function discover_interpreter
def test_discover_interpreter():
    interpreter_name = 'python'
    action = object
    task_vars = object
    discovery_mode = 'auto_legacy_silent'
    try:
        result = discover_interpreter(action, interpreter_name, discovery_mode, task_vars)
    except Exception as err:
        display.vvv("InterpreterDiscoveryRequiredError fault " + str(err))
        raise InterpreterDiscoveryRequiredError(str(err), interpreter_name, discovery_mode)
    return result

# Generated at 2022-06-12 21:32:39.632151
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # Fail if module is not python interpreter
    action = u'python'
    interpreter_name = u'python'
    discovery_mode = u'auto'
    task_vars = {}
    try:
        result = discover_interpreter(action, interpreter_name, discovery_mode, task_vars)
    except ValueError as ex:
        if not (ex.message.startswith('Interpreter discovery not supported for') and \
            ex.message.endswith('python')):
            raise ex
    # TODO: Uncomment next line once this is supported
    #    action = u'python'
    #    interpreter_name = u'python'
    #    discovery_mode = u'auto'
    #    task_vars = {} 
    #   result = discover_interpreter(action, interpreter_name,

# Generated at 2022-06-12 21:32:47.585703
# Unit test for function discover_interpreter
def test_discover_interpreter():
    import mock

    # Test the discover_interpreter method

    # If a platform type is not Linux, NotImplementedError is raised
    mock_action = mock.MagicMock()
    interpreter_name = 'python'
    discovery_mode = 'auto'
    task_vars = {}
    assert discover_interpreter(mock_action, interpreter_name, discovery_mode, task_vars) == '/usr/bin/python'

    # If no interpreters are found, the default fallback of /usr/bin/python is used.
    mock_action._low_level_execute_command.return_value = {'stdout': u'PLATFORM\nLinux\nFOUND\nENDFOUND'}

# Generated at 2022-06-12 21:32:48.252514
# Unit test for function discover_interpreter
def test_discover_interpreter():
    raise NotImplementedError()

# Generated at 2022-06-12 21:33:24.332866
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.plugins.action import ActionBase

    class MockAction(ActionBase):
        def _low_level_execute_command(self, cmd, sudoable=False, in_data=None):
            if cmd.startswith('command -v'):
                output_list = []
                for python in self.bootstrap_python_list:
                    output_list.append(u'{}\n'.format(python))
                return {'stdout': u'\n'.join(output_list)}
            elif in_data:
                return {'stdout': in_data}

        def run(self, tmp=None, task_vars=None):
            self.bootstrap_python_list = self._task.args.get('bootstrap_python_list')

# Generated at 2022-06-12 21:33:31.317434
# Unit test for function discover_interpreter
def test_discover_interpreter():
    action = object()
    task_vars = None

    interpreter_name = 'python'
    discovery_mode = 'auto_legacy_silent'

    # pylint: disable=protected-access
    res = discover_interpreter(action, interpreter_name, discovery_mode, task_vars)

    # TODO: assert results are not None?
    import platform
    if platform.system() == "Windows":
        assert 'python.exe' in res
    else:
        assert 'python' in res



# Generated at 2022-06-12 21:33:39.011633
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.module_utils.common.text.converters import to_bytes

    # TODO: better unit tests for interpreter discovery
    assert discover_interpreter(None, 'python', 'auto', {}) == u'/usr/bin/python'

    # check that the pipe case even works for a simple module
    # TODO: move this into an integration test
    from ansible.plugins.action import ActionBase
    import ansible.executor.task_executor
    import ansible.executor.module_common
    ipython = u'/usr/bin/ipython'

# Generated at 2022-06-12 21:33:51.866322
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.module_utils.discovery import is_python2
    from ansible.plugins.action import ActionBase

    class ActionModule(ActionBase):

        def _discovery_warnings(self):
            return []


# Generated at 2022-06-12 21:34:01.375913
# Unit test for function discover_interpreter
def test_discover_interpreter():
    interpreter_name = 'python'
    test_correct_return = '/usr/bin/python'
    test_incorrect_return = '/usr/bin/python2'
    test_incorrect_return2 = '/usr/bin/python3'
    test_verbosity = None
    test_discovery_mode = None
    test_task_vars = None
    test_host = None
    test_matched_output = 'PLATFORM\nLinux\nFOUND\n/usr/bin/python\n/usr/bin/python2\n/usr/bin/python3\nENDFOUND'

    assert test_correct_return == discover_interpreter(None, interpreter_name, test_discovery_mode, test_task_vars)

# Generated at 2022-06-12 21:34:11.644275
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.utils.vars import combine_vars

    task_vars = combine_vars(dict(),
                             dict(ansible_distribution='CentOS',
                                  ansible_distribution_major_version='7',
                                  ansible_distribution_version='7.5'),
                             )

    interpreter_name = 'python'
    discovery_mode = 'auto'
    action = {'connection': {'has_pipelining': True, '_shell': False},
              '_low_level_execute_command': {'stdout': 'PLATFORM\r\nLinux\r\nFOUND\r\n/usr/bin/python\r\n/usr/bin/python3\r\nENDFOUND'},
              '_discovery_warnings': []
              }

    assert discover_

# Generated at 2022-06-12 21:34:14.113901
# Unit test for function discover_interpreter
def test_discover_interpreter():
    '''
    Unit test for function discover_interpreter
    '''
    # TODO: test_functional.test_discover_interpreter should also be a test here
    pass

# Generated at 2022-06-12 21:34:22.855418
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # Test using Ubuntu 16.04
    task_vars = dict(
        ansible_python_interpreter=None,
        ansible_facts=dict(
            ansible_distribution=u'Ubuntu',
            ansible_distribution_release=u'xenial',
        ),
    )

    res = discover_interpreter(None, u'python', u'auto', task_vars)
    assert res == u'/usr/bin/python3'

    # Test using Debian 8.6
    task_vars = dict(
        ansible_python_interpreter=None,
        ansible_facts=dict(
            ansible_distribution=u'Debian',
            ansible_distribution_release=u'8.6',
        ),
    )


# Generated at 2022-06-12 21:34:24.180891
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.module_utils import basic

    assert discover_interpreter(basic.AnsibleModule(argument_spec={}), 'python', 'auto', {}, ) == u'/usr/bin/python'

# Generated at 2022-06-12 21:34:28.252373
# Unit test for function discover_interpreter
def test_discover_interpreter():
    assert discover_interpreter('python', 'auto') == "/usr/bin/python"
    assert discover_interpreter('python', 'auto_legacy') == "/usr/bin/python"
    assert discover_interpreter('python', 'auto_legacy_silent') == "/usr/bin/python"
    assert discover_interpreter('python', 'auto_silent') == "/usr/bin/python"

# Generated at 2022-06-12 21:35:27.214776
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.plugins.action.normal import ActionModule
    from ansible.executor.task_result import TaskResult
    from ansible.executor.task_result import TaskResult
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    from ansible.playbook.role import Role

    class FakeConnection(object):
        def __init__(self):
            self._shell = 'sh'
            self._default_shell = u'sh'
            self._shell_executable = u'sh'
            self._shell_type = u'shell'
            self.has_pipelining = True

    class FakeModule(object):
        def __init__(self):
            self.action_plugins = []


# Generated at 2022-06-12 21:35:39.574080
# Unit test for function discover_interpreter
def test_discover_interpreter():
    import io
    import sys

    from ansible.module_utils.six.moves import StringIO
    import ansible.executor.discovery

    # Redirect stdout to capture module output
    saved_stdout = sys.stdout
    sys.stdout = StringIO()

    # Example stdout responses
    # 1. No python interpreters found
    # 2. Python 2 and 3 interpreters found
    # 3. Python 2.6 and 2.7 interpreters found
    # 4. Python 2.6.5 and 2.7.10 interpreters found
    # 5. Python 2.6 and 3.4 interpreters found
    # 6. Python 2.6, 2.7, and 3.5 interpreters found
    # 7. Python 2.6, 2.6.5, 2.7, and 3.5 interpreters found
    #

# Generated at 2022-06-12 21:35:50.599362
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.executor.task_result import TaskResult
    from ansible.executor.action_base import ActionBase
    from ansible.executor.task_executor import TaskExecutor
    from ansible.executor.play_iterator import PlayIterator
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.handler import Handler
    from ansible.playbook.role_include import IncludeRole
    from ansible.playbook.conditional import Conditional
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

# Generated at 2022-06-12 21:35:58.637325
# Unit test for function discover_interpreter
def test_discover_interpreter():
    print ('Testing discover_interpreter')
    assert "3.6" == LooseVersion(discover_interpreter(None, u"python", "auto_legacy_host_silent", {u'ansible_python_interpreter': u'/usr/bin/python'})).version
    assert "_" == LooseVersion(discover_interpreter(None, u"python", "auto_legacy_host_silent", {u'ansible_python_interpreter': u'/usr/bin/python'})).version

if __name__ == '__main__':
    test_discover_interpreter()
    print('done')

# Generated at 2022-06-12 21:36:09.276303
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.module_utils.facts.system.distribution import DistributionFactModule
    from ansible.module_utils.facts.system import DefaultSysinfo
    from ansible.module_utils.facts.virt.kvm.collector import KVMFactCollector
    from ansible.module_utils.facts.networking.linux.collector import LinuxInterfaceCollector

    default_fact_collection = [DistributionFactModule, DefaultSysinfo, KVMFactCollector, LinuxInterfaceCollector]

    test_dist_os_release = u'''\
[os_release]
ID=centos
VERSION_ID=7.5
PRETTY_NAME="CentOS Linux 7 (Core)"
NAME="CentOS Linux"
VERSION="7 (Core)"
VERSION_CODENAME="Core"
ID_LIKE=rhel fedora
'''



# Generated at 2022-06-12 21:36:18.609622
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # Create a task with an action that includes interpreter discovery
    # TODO: most of this is boilerplate that should be moved to a common test fixture
    from ansible.playbook.task import Task
    from ansible.executor.action_base import ActionBase
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    class TestAction(ActionBase):
        def __init__(self, task, connection, *args, **kwargs):
            self._task = task
            self._connection = connection
            self._low_level_execute_command = connection.exec_command
            self._discovery_warnings = []

        def run(self, tmp=None, task_vars=None):
            return task_vars

    task = Task()
    task._role = None
    task.action

# Generated at 2022-06-12 21:36:30.016481
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # we're only testing non-Linux cases here, since the whole point of the extended discovery for Linux is to support
    # a wide variety of versions, and since logic/success cases are already tested in the regular interpreter
    # code paths

    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.six import b

    from ansible.executor.discovery import discover_interpreter
    from ansible.module_utils import interpreter_discovery

    assert interpreter_discovery.discover_interpreter.__module__ == 'ansible.module_utils.interpreter_discovery'

    # fake action is good enough for this test
    # pylint: disable=unused-variable
    class FakeAction(object):
        def __init__(self):
            self._discovery_warnings = []

       

# Generated at 2022-06-12 21:36:31.327882
# Unit test for function discover_interpreter
def test_discover_interpreter():
    raise NotImplementedError

# Generated at 2022-06-12 21:36:40.089883
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.executor.discovery import discover_interpreter
    from ansible.module_utils.facts.system.distribution import DistributionFactCollector

    # Linux: test both exact version and version truncation
    action = DistributionFactCollector()
    action._discovery_warnings = []

    assert discover_interpreter(action, 'python', 'auto', {'python_interpreter_discovery': 'auto'}) == '/usr/bin/python3.7'
    assert len(action._discovery_warnings) == 1
    assert 'double-check that the versions match' in action._discovery_warnings[0]

    action._discovery_warnings = []


# Generated at 2022-06-12 21:36:50.763786
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.module_utils.discovery.python import discover_interpreter
    from ansible.executor.task_result import TaskResult

    task_result = TaskResult('/usr/bin/python', 'ok', dict(stdout=b''))
    action = MagicMock()
    action.task_vars = dict()
    action._low_level_execute_command.return_value = task_result
    action._discovery_warnings = dict()

    action.get_connection.return_value = dict(has_pipelining=True)

    assert discover_interpreter(action, 'python', 'auto', dict()) == u'/usr/bin/python'

# Generated at 2022-06-12 21:38:30.137969
# Unit test for function discover_interpreter
def test_discover_interpreter():
    import os
    import tempfile

    class MockLowLevelExecuteCommand():
        def __init__(self):
            self.stdout_value = "PLATFORM\nLinux\nFOUND\n/usr/bin/python\n/usr/local/bin/python3\nENDFOUND"
            self.return_value = dict(
                cmd="command -v 'python'",
                rc=0,
                stdout=self.stdout_value,
                stderr="",
            )

        def __call__(self, *args, **kwargs):
            return self.return_value


# Generated at 2022-06-12 21:38:35.165154
# Unit test for function discover_interpreter
def test_discover_interpreter():
    class TestAction(object):
        _discovery_warnings = []

    task_vars = {}
    action = TestAction()
    action._low_level_execute_command = lambda x, sudoable, in_data: {'stdout': 'PLATFORM\nlinux\nFOUND\n/usr/bin/python\nENDFOUND'}
    assert discover_interpreter(action, 'python', 'auto_legacy', task_vars) == u'/usr/bin/python'



# Generated at 2022-06-12 21:38:35.904347
# Unit test for function discover_interpreter
def test_discover_interpreter():
    raise NotImplementedError()

# Generated at 2022-06-12 21:38:44.290274
# Unit test for function discover_interpreter
def test_discover_interpreter():
    '''Unit test for function discover_interpreter'''

    class TestActionModule:
        def __init__(self):
            self._low_level_execute_command_result = None
            self._discovery_warnings = []

        def _low_level_execute_command(self, command, sudoable=True, in_data=None):
            return self._low_level_execute_command_result

    # test case 1: error from low_level_execute_command
    action = TestActionModule()
    action._low_level_execute_command_result = {
        'stdout': 'mock output',
        'stderr': 'mock error message'
    }
    discovered = discover_interpreter(action, 'python', 'auto', {'inventory_hostname': 'test.example.com'})

# Generated at 2022-06-12 21:38:54.864983
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.module_utils.facts.system.distribution import DistributionFactCollector

    python_interpreter = '/usr/bin/python'
    python_version = 'unknown'
    discovered_python = discover_interpreter(DistributionFactCollector(), 'python', 'auto', {})
    assert discovered_python is not None
    assert discovered_python == python_interpreter
    assert python_version == 'unknown'

    python_version = '3.7.1'
    discovered_python = discover_interpreter(DistributionFactCollector(), 'python', 'auto', {})
    assert discovered_python is not None
    assert discovered_python == python_interpreter
    assert python_version == '3.7.1'

# Generated at 2022-06-12 21:39:04.979454
# Unit test for function discover_interpreter
def test_discover_interpreter():
    import ansible.executor.discovery
    def do_interp_test(python_discovery, expected_result, expected_warnings=None):
        # This is a bit of a hack, but we need to mock the plugin's config value
        # and we don't have a reliable way to get the executing plugin. So we'll
        # use our own module, which is guaranteed to be nearby and have the same
        # namespace
        C.config.parser.set_config_value('ansible.executor.discovery', 'interpreter_python_distro_map',
                                         {'bogusdistro': {'1.1': '/usr/bin/python_interpreter'}})

# Generated at 2022-06-12 21:39:14.240676
# Unit test for function discover_interpreter

# Generated at 2022-06-12 21:39:25.178384
# Unit test for function discover_interpreter
def test_discover_interpreter():
    action = None
    # no warning triggered when silent
    assert discover_interpreter(action, 'python', 'auto_legacy_silent', {}) == u'/usr/bin/python'
    assert discover_interpreter(action, 'python', 'auto_silent', {}) == u'/usr/bin/python'

    # will throw if not silent
    try:
        discover_interpreter(action, 'python', 'auto_legacy', {})
        assert False
    except InterpreterDiscoveryRequiredError:
        pass
    try:
        discover_interpreter(action, 'python', 'auto', {})
        assert False
    except InterpreterDiscoveryRequiredError:
        pass

    # should just pass through

# Generated at 2022-06-12 21:39:33.457917
# Unit test for function discover_interpreter
def test_discover_interpreter():
    import tempfile

    def fake_low_level_execute_command(command, sudoable=False, in_data=None):
        d = {}
        d['command'] = command

        with tempfile.NamedTemporaryFile('w', delete=False) as f:
            f.write(in_data)

        d['stdout'] = '/usr/bin/python\npython3.6\n/usr/local/bin/python\n/usr/bin/python3\n'

        return d

    task_vars = {}
    action = _fake_action()
    action._low_level_execute_command = fake_low_level_execute_command

    task_vars = {}
    action._task_vars = task_vars

# Generated at 2022-06-12 21:39:36.423523
# Unit test for function discover_interpreter
def test_discover_interpreter():
    assert discover_interpreter('', 'python', 'auto', {}) == '/usr/bin/python'