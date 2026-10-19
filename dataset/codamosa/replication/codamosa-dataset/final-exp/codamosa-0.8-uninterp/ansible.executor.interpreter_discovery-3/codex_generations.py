

# Generated at 2022-06-12 21:30:18.376613
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.module_utils.facts.virtual import Virtual, virtuals
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.task_executor import TaskExecutor
    from ansible.plugins.loader import action_loader

    # TODO: move class PlayContext to top-level
    #       to remove this import workaround
    import ansible.plugins.loader
    import tempfile
    import os
    import shutil

    orig_loader = ansible.plugins.loader.action_loader

    def cleanup():
        ansible.plugins.loader.action_loader = orig_loader

    class FakeTaskExecutor(TaskExecutor):
        def __init__(self, queue):
            self._queue = queue


# Generated at 2022-06-12 21:30:27.303780
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # TODO: more test cases, error handling/discovery failure, non-Linux platform/distro handling,
    # non-pipelining support
    display._verbosity = 4
    task_vars = dict()

    # Test: 'discover' should return '/usr/bin/python2.7' or '/usr/bin/python2.6', depending on which is
    #       present on the target; discovering a different Python should result in a warning
    action = dict(remote_user='root')
    action['args'] = dict()
    action._discovery_warnings = []
    action._low_level_execute_command = lambda command, sudoable=False, in_data=None: dict(stdout='/usr/bin/python2.7\n/usr/bin/python3.6')

# Generated at 2022-06-12 21:30:35.774877
# Unit test for function discover_interpreter

# Generated at 2022-06-12 21:30:41.299221
# Unit test for function discover_interpreter
def test_discover_interpreter():
    action = object
    action._discovery_warnings = []

    interpreter_name = 'python'
    discovery_mode = 'auto'
    task_vars = {}
    out = discover_interpreter(action, interpreter_name, discovery_mode, task_vars)
    if out is None:
        print("ERROR test_discover_interpreter: interpreter discovery failed")
        return -1
    else:
        return 0


if __name__ == '__main__':
    import sys
    rc = test_discover_interpreter()
    sys.exit(rc)

# Generated at 2022-06-12 21:30:48.265353
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.executor.task_result import TaskResult
    from ansible.action.action import ActionModule
    from ansible.module_utils.common.text.converters import to_bytes
    import json

    action = ActionModule('unity_linux.py', {}, False, [], [])
    discovery_mode = 'explicit'

    # test case for Ubuntu_12.0.4
    ubuntu_120_4 = {'stdout': b"PLATFORM\nLinux\nFOUND\n/usr/bin/python\n/usr/bin/python3\n/usr/bin/python2\nENDFOUND"}
    interpreter = discover_interpreter(action, 'python', discovery_mode, {'inventory_hostname': 'ubuntu_12.0.4'})

# Generated at 2022-06-12 21:30:59.176155
# Unit test for function discover_interpreter
def test_discover_interpreter():
    import platform
    import os
    import tempfile
    from ansible.plugins.action import ActionBase
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.playbook.play_context import PlayContext
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

    class MockAction(ActionBase):

        def __init__(self):
            self._discovery_warnings = []

        def get_discovery_warnings(self):
            return self._discovery_warnings

        def _low_level_execute_command(self, cmd, sudoable=True, in_data=None):
            return {"stdout": "", "stderr": "", "rc": 0}


# Generated at 2022-06-12 21:31:07.163336
# Unit test for function discover_interpreter
def test_discover_interpreter():
    assert _version_fuzzy_match('2.6.10', {'2.6.10': 'python2.6-legacy', '2.6.11': 'python2.6-legacy', '2.6.18': 'python2.6-legacy'}) \
        == 'python2.6-legacy'

    assert _version_fuzzy_match('2.7.9', {'2.7.10': 'python2.7'}) == 'python2.7'

    assert _version_fuzzy_match('3.7.0', {'3.7.0': 'python3.7', '3.7.1': 'python3.7', '3.6.0': 'python3.6'}) == 'python3.6'


# Generated at 2022-06-12 21:31:07.852978
# Unit test for function discover_interpreter
def test_discover_interpreter():
    pass

# Generated at 2022-06-12 21:31:18.973423
# Unit test for function discover_interpreter
def test_discover_interpreter():
    class action(object):
        def _low_level_execute_command(self, cmd, sudoable=None, in_data=None):
            return True

        def _discovery_warnings(self):
            return True

        def _discovery_warnings(self):
            return True

        def _discovery_warnings(self):
            return True

        def _discovery_warnings(self):
            return True

        def _discovery_warnings(self):
            return True

        def _discovery_warnings(self):
            return True

        def _discovery_warnings(self):
            return True

        def _discovery_warnings(self):
            return True

        def _discovery_warnings(self):
            return True

        def _discovery_warnings(self):
            return True

       

# Generated at 2022-06-12 21:31:25.161087
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.plugins.action.normal import ActionModule as _ActionModule

    class ActionModule(_ActionModule):
        def _low_level_execute_command(self, cmd, sudoable=True, in_data=None, executable=None):
            shell_bootstrap = "echo PLATFORM; uname; echo FOUND; {0}; echo ENDFOUND".format(cmd)
            shell_bootstrap_results = {
                'cmd': shell_bootstrap,
                'stdout': 'PLATFORM\r\nLinux\r\nFOUND\r\n/usr/local2/bin/python\r\nENDFOUND',
                'stderr': '',
                'rc': 0,
                'start': '',
                'end': '',
                'delta': '',
                'changed': False
            }


# Generated at 2022-06-12 21:31:37.549185
# Unit test for function discover_interpreter
def test_discover_interpreter():

    # TODO: need better fake action object, no connection object
    # TODO: stub os.path.exists calls
    # TODO: stub platform.dist
    pass

# Generated at 2022-06-12 21:31:46.859059
# Unit test for function discover_interpreter
def test_discover_interpreter():
    def test(test_name, action_mock, expected_interpreter, expected_warnings):
        task_vars = {}
        interpreter = discover_interpreter(action_mock, "python", "auto_silent", task_vars)
        assert interpreter == expected_interpreter
        if expected_warnings is None:
            expected_warnings = []
            assert sorted(expected_warnings) == sorted(action_mock.discovery_warnings)
        else:
            assert False, "test: %s failed with interpreter discovery warnings: %s" % (test_name, action_mock.discovery_warnings)
    # stub out variables needed by discover_interpreter function
    # TODO: create a mock for _low_level_execute_command which would be more efficient

# Generated at 2022-06-12 21:31:57.605301
# Unit test for function discover_interpreter
def test_discover_interpreter():

    # Testing DiscoverInterpreterUsingBootstrap class
    discover_interpreter({"ansible_python_interpreter": "/usr/bin/python"}, "python", "auto", {})
    discover_interpreter({"ansible_python_interpreter": "/usr/bin/python", "inventory_hostname": "localhost"}, "python", "auto", {})
    discover_interpreter({"ansible_python_interpreter": "/usr/bin/python"}, "python", "auto_legacy", {})
    discover_interpreter({"ansible_python_interpreter": "/usr/bin/python"}, "python", "auto_legacy_silent", {})

# Generated at 2022-06-12 21:32:07.477166
# Unit test for function discover_interpreter
def test_discover_interpreter():
    import os
    import pipes

    # Import ansible.module_utils.basic to get access to AnsibleModule
    from ansible.module_utils.basic import *

    # Import ansible.module_utils.connection to get access to Connection
    from ansible.module_utils.connection import Connection

    # Create a dummy module
    module = AnsibleModule(
        argument_spec={
            'name': {'required': True, 'type': 'str'},
            'interpreter_name': {'required': True, 'type': 'str'},
            'discovery_mode': {'required': True, 'type': 'str'},
        },
        supports_check_mode=True
    )

    temp_dir = os.environ['HOME'] + '/ansible-test'


# Generated at 2022-06-12 21:32:18.896953
# Unit test for function discover_interpreter
def test_discover_interpreter():
    '''
    Test cases for function discover_interpreter
    '''
    # Test case 1 to test if the interpreter exists and return interpreter
    # path would be returned
    platform_python_map = C.config.get_config_value('INTERPRETER_PYTHON_DISTRO_MAP')
    bootstrap_python_list = C.config.get_config_value('INTERPRETER_PYTHON_FALLBACK')
    platform_type = 'Linux'
    platform_info = {}
    platform_info['platform_dist_result'] = [u'Ubuntu', u'16.04', u'xenial']
    platform_info['osrelease_content'] = ""
    action = object()
    action._discovery_warnings = []
    host = 'localhost'
    res = object()

# Generated at 2022-06-12 21:32:28.192860
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.module_utils.facts.system.distribution import Distribution

    # Note that this is under tests/unit/module_utils/facts/system/test_distribution.py because the
    # module_utils/facts/system/distribution.py code is broken and we have to mock it.
    # It was broken in 3.0.0-3.1.0 and fixed in 3.1.1
    # See https://github.com/ansible/ansible/issues/29239
    # In 3.0.0-3.1.0, we use 'python_target.py' to discover the OS.
    # In 3.1.1+, we use 'distribution.py' to discover the OS.
    # Because the old code is broken, we have to mock it.
    # There are 3 cases:
    #   1.

# Generated at 2022-06-12 21:32:40.486258
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.executor.action_loader import ActionModuleLoader
    try:
        action_loader = ActionModuleLoader(None, None, '/usr/share/ansible_plugins/actions')
    except Exception as e:
        raise Exception(
            'cannot initialize action_loader: %s' % to_text(e)
        )

    execute_command_on_host = 'echo PLATFORM; uname; echo FOUND; echo /usr/bin/python; echo ENDFOUND'

    # mock module execute command in order to be able to run the test

# Generated at 2022-06-12 21:32:49.769307
# Unit test for function discover_interpreter
def test_discover_interpreter():
    import ansible.plugins.action.script as script
    import ansible.plugins.action.raw as raw
    import ansible.plugins.action.ping as ping
    import ansible.utils.plugin_docs as plugin_docs

    # Setup test data
    # Stored in test_data/discover_interpreter
    # If a new test case is added, please add corresponding
    # platform.dist() output by running the same command:
    # platform.dist()
    # Python 3.2.3 (default, Feb 22 2013, 22:39:10)
    # [GCC 4.6.3] on linux2
    # ('LinuxMint', '13', 'maya')
    #
    # Python 3.3.2 (default, Sep 15 2013, 01:05:08)
    # [GCC 4.7.2]

# Generated at 2022-06-12 21:32:51.233125
# Unit test for function discover_interpreter
def test_discover_interpreter():
    discovered_python_path = discover_interpreter(None, 'python', 'auto_legacy', {})
    assert discovered_python_path is not None

# Generated at 2022-06-12 21:33:03.521316
# Unit test for function discover_interpreter
def test_discover_interpreter():

    # Test data as returned by uname (success)
    test_platform_data = {'stdout': u'PLATFORM\nLinux\nFOUND\n'
                                    '/usr/bin/python3.4\n'
                                    '/usr/bin/python3.5\n'
                                    '/usr/bin/python2.7\n'
                                    '/usr/bin/python3.6\n'
                                    '/usr/bin/python3.3\n'
                                    '/usr/bin/python3\n'
                                    'ENDFOUND',
                          'rc': 0}


# Generated at 2022-06-12 21:33:23.998295
# Unit test for function discover_interpreter
def test_discover_interpreter():
    def test_discovery_warning(warnings, test_msg):
        if warnings is None:
            raise Exception(test_msg)
        if len(warnings) == 0:
            raise Exception(test_msg)

    class MockActionModule:
        def __init__(self):
            self._discovery_warnings = []

        def _low_level_execute_command(self, cmd, sudoable=False, in_data=None):
            class MockResults:
                def __init__(self, stdout=None, stderr=None):
                    self.stdout = stdout
                    self.stderr = stderr

            res_fallback = MockResults(stdout="PLATFORM\nLinux\nFOUND\n/usr/bin/python\nENDFOUND")

# Generated at 2022-06-12 21:33:33.867909
# Unit test for function discover_interpreter
def test_discover_interpreter():
    import pytest
    from ansible.utils.collection_loader import AnsibleCollectionLoader, ansible_collections_paths
    from ansible.plugins.loader import callback_loader
    from ansible.module_utils.common.text.converters import to_bytes
    from ansible.utils.plugin_docs import find_plugin_docs

    # Test data directory
    #
    # contains a copy of "tests/units/executor/discovery/data/interpreter_discovery.yml"
    test_data_directory = os.path.join(os.path.dirname(__file__), 'data')

    # Load up the test data
    #
    # test_data_file is a tuple of the ACTION NAME: TEST DATA
    #
    # test_data is a tuple of TEST NAME, TEST DATA
    #
   

# Generated at 2022-06-12 21:33:40.428606
# Unit test for function discover_interpreter
def test_discover_interpreter():
    import ansible.plugins.action as action
    import ansible.plugins.action.discovery as discovery
    import ansible.playbook.play_context as play_context
    import ansible.playbook.task as task
    import ansible.vars.manager as vars_manager
    import ansible.template as template

    action._DiscoveryAction = discovery.DiscoveryAction

    task_vars = dict()
    task_vars['inventory_hostname'] = 'localhost'
    task_vars['ansible_connection'] = 'local'

    play_context = play_context.PlayContext()
    loader = template.AnsibleLoader(None)


# Generated at 2022-06-12 21:33:45.660476
# Unit test for function discover_interpreter
def test_discover_interpreter():
    action = None
    interpreter_name = 'python'
    discovery_mode = 'auto'
    task_vars = {}

    discover_interpreter(action, interpreter_name, discovery_mode, task_vars)

if __name__ == "__main__":
    test_discover_interpreter()

# Generated at 2022-06-12 21:33:56.372108
# Unit test for function discover_interpreter
def test_discover_interpreter():
    import ansible.module_utils.discovery as discovery
    import ansible.module_utils.facts as facts
    import ansible.plugins.action as action

    action._discovery_warnings = []   # this is normally a member of the BaseAction class, but we can't import that
    task_vars = facts.ansible_facts(dict())
    task_vars['ansible_inventory_hostname'] = 'localhost'
    task_vars['ansible_connection'] = 'local'
    task_vars['ansible_python_interpreter'] = '/usr/bin/python'
    task_vars['ansible_remote_tmp'] = '/tmp'

    action.BaseAction.set_options({})

    # unfortunately this needs to be mocked. we can't just plop a file into the data directory
    platform_python

# Generated at 2022-06-12 21:34:06.764154
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # these are used for testing dundler of the function.
    import os
    import sys

    # ansible.cfg must be in the same dir as test file
    ansible_path = os.path.dirname(os.path.abspath(__file__))
    # The configure system will look for ansible.cfg in the current user home directory
    # before looking in the current working directory.  Make the current working directory
    # the same as the current user directory to keep things simple
    home_path = os.path.expanduser('~')
    os.chdir(home_path)
    # this does not work in python <= 2.7.5
    # if it does not work comment out the line above and change the line below to set C.DEFAULT_LOCAL_TMP
    # path to a temp dir like /tmp or C

# Generated at 2022-06-12 21:34:16.245292
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.module_utils.six.moves import StringIO
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )
    setattr(module, '_low_level_execute_command', lambda *args: {'stdout': u'PLATFORM\nLinux\nFOUND\n/usr/bin/python\nENDFOUND'})
    setattr(module, '_discovery_warnings', StringIO())
    setattr(module, '_connection', StringIO())
    setattr(module, '_connection', StringIO())


# Generated at 2022-06-12 21:34:21.885841
# Unit test for function discover_interpreter
def test_discover_interpreter():
    assert discover_interpreter(None, 'python', 'auto', None) == '/usr/bin/python'
    assert discover_interpreter(None, 'python', 'auto_legacy', None) == '/usr/bin/python'
    assert discover_interpreter(None, 'python', 'auto_silent', None) == '/usr/bin/python'
    assert discover_interpreter(None, 'python', 'auto_legacy_silent', None) == '/usr/bin/python'

# Generated at 2022-06-12 21:34:29.001842
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # Step 1: From the interpreters list pick the first one in the list as the default interpreter
    # if discovery is explicitly turned on and that interpreter was not found
    action = 'some_action'
    interpreter_name = 'python'
    discovery_mode = 'auto'
    task_vars = {}
    task_vars['ansible_hostname'] = 'host'
    task_vars['ansible_system'] = 'linux'
    task_vars['ansible_facts'] = dict(platform_dist_result=[u'RedHatEnterpriseServer', u'7.6', u'Maipo'])

# Generated at 2022-06-12 21:34:33.045922
# Unit test for function discover_interpreter
def test_discover_interpreter():
    res = discover_interpreter(None, 'python', 'auto_legacy', 'test')
    assert res == u'/usr/bin/python', 'unexpected result {0}'.format(res)

# Generated at 2022-06-12 21:35:00.338532
# Unit test for function discover_interpreter
def test_discover_interpreter():
    import os
    import sys
    import tempfile
    import shutil

    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.module_utils.discovery._test_interpreter_discovery import TestActionModule
    from ansible.module_utils.discovery._test_interpreter_discovery import TestConnectionPlugin

    def _connect(module_name, *_, **__):
        # TODO: this is horrible; make a real connection plugin that doesn't require a file to work
        return TestConnectionPlugin(module_name, *_, **__)

    def _find_file(path_to_file):
        b_path = to_text(os.path.abspath(path_to_file))


# Generated at 2022-06-12 21:35:07.444366
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.mock import patch
    from ansible.playbook.play_context import PlayContext

    # Test discover_interpreter method with valid distribtuion
    with patch('ansible.executor.discovery.get_platform_info') as mock_get_platform_info:
        with patch('ansible.executor.discovery.get_version_map') as mock_get_version_map:
            with patch('ansible.executor.discovery.get_fallback_list') as mock_get_fallback_list:
                mock_get_fallback_list.return_value = ["/usr/bin/python", "/usr/bin/python2", "/usr/bin/python3"]
                mock_get_version_map.return_value = {"18.04": "/usr/bin/python3"}
                mock_

# Generated at 2022-06-12 21:35:11.237887
# Unit test for function discover_interpreter
def test_discover_interpreter():
    assert discover_interpreter('action', 'python', 'auto_legacy_silent', {'inventory_hostname': 'unknown'}) == u'/usr/bin/python'
    assert discover_interpreter('action', 'python', 'auto_silent', {'inventory_hostname': 'unknown'}) == u'/usr/bin/python'

# Generated at 2022-06-12 21:35:22.343867
# Unit test for function discover_interpreter
def test_discover_interpreter():

    # Test with no discovery mode
    action = None
    interpreter_name = 'python'
    discovery_mode = 'none'
    task_vars = dict()

    try:
        discover_interpreter(action, interpreter_name, discovery_mode, task_vars)
    except ValueError:
        pass
    except Exception as e:
        assert False, "Exception raised: %s"%str(e)

    # Test with mode not supported
    action = None
    interpreter_name = 'python'
    discovery_mode = 'auto_legacy'
    task_vars = dict()

    try:
        discover_interpreter(action, interpreter_name, discovery_mode, task_vars)
    except NotImplementedError:
        pass

# Generated at 2022-06-12 21:35:31.204016
# Unit test for function discover_interpreter
def test_discover_interpreter():
    """make sure we handle all the permutations of params"""
    class MockAction:
        def __init__(self):
            self.discovery_warnings = []
            self.connection = MockConnection(False)


# Generated at 2022-06-12 21:35:43.232067
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.plugins.action.normal import ActionModule

    action = ActionModule(
        task=dict(),
        connection=None,
        play_context=None,
        loader=None,
        templar=None,
        shared_loader_obj=None)

# Generated at 2022-06-12 21:35:53.570404
# Unit test for function discover_interpreter
def test_discover_interpreter():
    task_vars = dict()
    task_vars['ansible_distribution'] = 'Ubuntu'
    task_vars['ansible_distribution_version'] = '18.04'
    task_vars['ansible_interpreter_python'] = '/usr/bin/python2.7'

    res = discover_interpreter(None, 'python', 'auto', task_vars)
    assert res == '/usr/bin/python2.7'

    task_vars['ansible_distribution'] = 'RedHat'
    task_vars['ansible_distribution_version'] = '7'
    task_vars['ansible_interpreter_python'] = '/usr/bin/python2.7'

    res = discover_interpreter(None, 'python', 'auto', task_vars)

# Generated at 2022-06-12 21:36:04.542983
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.module_utils.common.removed import removed
    from ansible.module_utils import basic
    from ansible.plugins.action import ActionModule

    # Test inputs
    action = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    interpreter_name = 'python'
    discovery_mode = 'normal'
    task_vars = {'inventory_hostname': 'localhost',
                 'ansible_python_interpreter': '/usr/bin/python',
                 }

    # Test

# Generated at 2022-06-12 21:36:11.326001
# Unit test for function discover_interpreter

# Generated at 2022-06-12 21:36:15.490060
# Unit test for function discover_interpreter
def test_discover_interpreter():
    try:
        result = discover_interpreter('action', 'python', 'auto', 'task_vars')
        print(result)
    except InterpreterDiscoveryRequiredError as e:
        print(e)
if __name__ == "__main__":
    test_discover_interpreter()

# Generated at 2022-06-12 21:36:41.538483
# Unit test for function discover_interpreter
def test_discover_interpreter():
    class module_mock:
        def __init__(self):
            self.discovery_warnings = []
            self.discovery_exceptions = []

        class connection_mock:
            has_pipelining = True

            def __init__(self):
                self.success = True
                self.action = module_mock()

            def _low_level_execute_command(self, cmd, sudoable, in_data):
                display.debug('running command: {0}'.format(cmd))

                if cmd.startswith("command -v"):
                    if cmd.endswith("python2.6"):
                        return dict(stdout="error: python2.6 not found\n", stderr="", rc=1)
                    elif cmd.endswith("python3.3"):
                        return dict

# Generated at 2022-06-12 21:36:52.368268
# Unit test for function discover_interpreter
def test_discover_interpreter():
    import unittest
    import tempfile
    import ansible_collections.ansible.executor.plugins.module_utils.interpreter_discovery \
        as interpreter_discovery
    from ansible_collections.ansible.executor.plugins.module_utils.interpreter_discovery \
        import _version_fuzzy_match

    class TempFileTestCase(unittest.TestCase):
        """
        Unit tests for method _version_fuzzy_match
        """

        def setUp(self):
            self.version_map = {'2.7': 'ok_interpreter',
                                '3.5': 'ok_interpreter',
                                '3.6': 'ok_interpreter',
                                '3.7': 'ok_interpreter'}


# Generated at 2022-06-12 21:37:01.791449
# Unit test for function discover_interpreter
def test_discover_interpreter():
    task_vars = dict(
        ansible_os_family='Linux',
        ansible_distribution='Amazon',
        ansible_distribution_major_version='2',
        ansible_interpreter_python='/usr/bin/python',
    )
    test_ansible_vars = {}
    test_ansible_vars.update(task_vars)
    test_ansible_vars.update(C.config.get_config_value('DEFAULT_CURRENT_VARS', variables=task_vars))
    test_ansible_vars.update(C.config.get_config_value('DEFAULT_GROUP_VARS', variables=task_vars))

# Generated at 2022-06-12 21:37:10.650648
# Unit test for function discover_interpreter
def test_discover_interpreter():
    import pytest

    task_vars = {
        'ansible_become': 'yes',
        'ansible_become_method': 'sudo',
        'ansible_become_user': 'root',
        'ansible_connection': 'ssh',
        'ansible_ssh_pass': u'',
        'ansible_ssh_user': 'root',
        'ansible_ssh_host': 'localhost',
        'ansible_interpreter': 'auto'
    }
    display_info = {
        "verbosity": 4
    }
    task_vars.update(display_info)
    # Create an action plugin
    action = ActionModule(task_vars)
    # Create an interpreter name
    interpreter_name = 'python'
    # Create a discovery mode

# Generated at 2022-06-12 21:37:16.874477
# Unit test for function discover_interpreter

# Generated at 2022-06-12 21:37:23.392586
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.errors import AnsibleError, AnsibleAction
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins.connection.connection_loader import get_connection_loader
    from ansible.vars import VariableManager
    from ansible.utils.vars import combine_vars
    from ansible.template import Templar

    action_class = AnsibleAction.action_loader.get('test_discovery', class_only=True)
    action = action_class(
        task=dict(name='test'),
        connection=get_connection_loader().get('local', None, PlayContext(), variable_manager=VariableManager()),
        play_context=PlayContext()
    )

# Generated at 2022-06-12 21:37:25.448840
# Unit test for function discover_interpreter
def test_discover_interpreter():
    value = discover_interpreter(None, 'python', 'auto_legacy_silent', None)
    assert isinstance(value, str)

# Generated at 2022-06-12 21:37:33.716265
# Unit test for function discover_interpreter
def test_discover_interpreter():
    import pytest
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.connection import Connection
    from ansible.module_utils.six import BytesIO
    from ansible.parsing.ajson import AnsibleJSONEncoder

    class FakeTask(object):
        def __init__(self):
            self.args = {
                '_ansible_version': '2.8.0',
                '_ansible_syslog_facility': 'LOG_USER',
                '_ansible_connection': 'local',
                '_ansible_no_log': False,
                '_ansible_check_mode': False,
                '_ansible_verbosity': 0,
            }
            self.action = 'test'


# Generated at 2022-06-12 21:37:42.829202
# Unit test for function discover_interpreter
def test_discover_interpreter():
    import mock
    import sys
    import tempfile
    import os
    import shutil
    from ansible.executor.discovery import discover_interpreter
    from ansible.utils.display import Display
    from ansible.utils.plugin_docs import get_versioned_doclink

    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.parsing.convert_bool import boolean

    display = Display()
    display.verbosity = 4

    # Create temporary directory to store test files
    temp_dir = tempfile.mkdtemp()

    # Store data in a temporary files to test
    script = pkgutil.get_data('ansible.executor.discovery', 'python_target.py')

# Generated at 2022-06-12 21:37:54.582081
# Unit test for function discover_interpreter
def test_discover_interpreter():

    class _ActionModule:
        def __init__(self):
            self._connection = 'pipelining'
            self._discovery_warnings = []

        def _low_level_execute_command(self, command, sudoable=False, in_data=None):
            return {'stdout': 'FOUND\n'
                              '/usr/bin/python\n'
                              '/usr/bin/python3\n'
                              '/usr/local/bin/python2.7'}

    class _TaskVars:
        def __init__(self):
            self._config = _Config()


# Generated at 2022-06-12 21:38:35.940856
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # check uname linux case
    mock_uname_linux_res = {'rc': 0, 'stdout': 'Linux\nFOUND\n/usr/bin/python\nENDFOUND'}
    python_target_script = pkgutil.get_data('ansible.executor.discovery', 'python_target.py')
    mock_python_linux_res = {'rc': 0,
                             'stdout': '{"platform_dist_result":["debian", "8.0", "jessie"],"osrelease_content":"NAME=\\"Debian GNU/Linux\\"\nVERSION=\\"8 (jessie)\\"\n"}'}
    mock_cmd_true_res = {'rc': 0, 'stdout': 'True\n'}

# Generated at 2022-06-12 21:38:44.321800
# Unit test for function discover_interpreter
def test_discover_interpreter():

    # Unit test for function discover_interpreter
    from ansible.module_utils import basic
    from ansible.executor.discovery import discover_interpreter

    class TestActionModule(object):
        def __init__(self, interpreter_name, discovery_mode, task_vars):
            self.tmpdir = '/tmp/ansible-tmp-%s' % basic._generate_random_id()
            self.name = 'Discovery'
            self._shared_loader_obj = None
            self._task = None
            self._loader = None
            self._connection = None
            self._templar = None
            self._task_vars = task_vars
            self._task_vars['ansible_discovery_interpreter'] = interpreter_name

# Generated at 2022-06-12 21:38:55.552454
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.plugins.action import ActionBase
    from ansible.executor.task_result import TaskResult
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.utils.vars import combine_vars
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.role import Role
    from ansible.playbook.handler import Handler
    from ansible.playbook.play_context import PlayContext


# Generated at 2022-06-12 21:39:05.713273
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # Create mock action
    class MyAction(object):
        def __init__(self):
            self._discovery_warnings = []

        def _low_level_execute_command(self, command, sudoable, in_data=None, environ_update=None):
            print(u"low_level_execute_command: {0}".format(command))
            return {u'stdout': u"PLATFORM\nLinux\nFOUND\n/usr/bin/python\nENDFOUND", u'stderr': u'', u'rc': 0,
                    u'changed': False}

        def _discovery_warn(self, warning):
            self._discovery_warnings.append(warning)


# Generated at 2022-06-12 21:39:14.896571
# Unit test for function discover_interpreter

# Generated at 2022-06-12 21:39:21.300720
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # Create a mock object to fake _action_plugin (and thus _connection)
    class MockActionModule:
        # class variables
        _display = Display()
        _connection = MockConnection()

        # instance variables
        _discovery_warnings = []
        _task_vars = {}
        _low_level_execute_command = MockActionModule.low_level_execute_command

        @classmethod
        def low_level_execute_command(cls, executable, in_data=None, sudoable=True):
            return {'stderr': '', 'stdout': cls.command}

    # Create a mock object to fake _shell_plugin (and thus _low_level_execute_command)
    class MockConnection:
        # class variables
        _display = Display()
        _shell = None
        has_pipelining

# Generated at 2022-06-12 21:39:31.105242
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.module_utils.facts.system.distribution import Distribution
    from ansible.module_utils.facts.system.distribution import LinuxDistribution
    from ansible.module_utils.facts.system.distribution import Platform

    # We are going to use two functions to ensure the output is what we want
    # We can not use the built-in assert as it is a keyword in Python
    # we can define function inside function
    def assert_equal(a, b):
        if a != b:
            raise AssertionError('%r != %r' % (a, b))
    # if the output is not what we expected, we raise an exception
    # this will make python unit test return with non-zero code


# Generated at 2022-06-12 21:39:42.488997
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.module_utils._text import to_bytes
    from ansible.plugins.action import ActionBase

    class ActionModule(ActionBase):
        def _execute_module(self, module_name=None, module_args=None, task_vars=dict(), persist_files=True):
            results = dict()
            results['ansible_facts'] = {}
            return results

    def _low_level_execute_command(self, cmd, sudoable=True, in_data=None, executable='/bin/sh', sudo_user=None):
        class Result:
            def __init__(self):
                self.stdout = ''
                self.stderr = ''
        result = Result()

# Generated at 2022-06-12 21:39:50.857200
# Unit test for function discover_interpreter
def test_discover_interpreter():
    fake_action = type('FakeAction', (object, ), {'_low_level_execute_command': lambda self, *args, **kwargs: dict(),
                                                  '_discovery_warnings': []})

    # Test interpreter_name != python
    try:
        discover_interpreter(fake_action(), 'python3', 'auto', None)
        assert False, "discover_interpreter() did not raise ValueError for interpreter_name != python"
    except ValueError as e:
        pass

    # Test no platform_python_map
    C.config.get_config_value = lambda self, config_name, variables=None: dict() if config_name == 'INTERPRETER_PYTHON_DISTRO_MAP' else None

# Generated at 2022-06-12 21:39:55.118023
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # Unit test for function discover_interpreter
    # test simple shell bootstrap
    assert discover_interpreter(None, 'python', 'auto_legacy_silent', {}) == '/usr/bin/python'