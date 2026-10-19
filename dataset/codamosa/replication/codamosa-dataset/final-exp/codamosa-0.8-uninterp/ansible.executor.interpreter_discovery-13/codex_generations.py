

# Generated at 2022-06-12 21:30:16.987787
# Unit test for function discover_interpreter
def test_discover_interpreter():
    output = discover_interpreter(action, interpreter_name='python', discovery_mode='auto_legacy', task_vars={})
    assert output == u'/usr/bin/python'
    output = discover_interpreter(action, interpreter_name='python', discovery_mode='auto_legacy_silent', task_vars={})
    assert output == u'/usr/bin/python'


# Generated at 2022-06-12 21:30:26.303247
# Unit test for function discover_interpreter
def test_discover_interpreter():
    class FakeActionModule(object):
        def __init__(self):
            self._discovery_warnings = list()

    fake_task_vars = dict()

    fake_action = FakeActionModule()

    # Either of these values should work for interpreter_name,
    # since we're only testing the Python interpreter currently
    # python or python3

    # These values should work for discovery_mode.
    #
    # auto_legacy
    # auto_legacy_silent
    # auto
    # auto_silent
    # explicit

    # The following tests are negative tests and skip interpreter discovery

# Generated at 2022-06-12 21:30:32.278120
# Unit test for function discover_interpreter
def test_discover_interpreter():
    import unittest

    class TestModule(unittest.TestCase):
        def test_simple(self):
            from ansible.module_utils import basic

            task_vars = {"inventory_hostname": "localhost"}
            result = discover_interpreter(basic, "python", "auto", task_vars)
            self.assertEqual(result, "/usr/bin/python")

    unittest.main()


if __name__ == "__main__":
    test_discover_interpreter()

# Generated at 2022-06-12 21:30:43.230467
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.executor.task_result import TaskResult
    from ansible.executor.action_result import AttributeDict
    import pkg_resources

    python_distro_map = json.loads(
        pkg_resources.resource_string(
            'ansible.executor.discovery',
            'python_distro_map.json'
        )
    )
    bootstrap_python_list = json.loads(
        pkg_resources.resource_string(
            'ansible.executor.discovery',
            'bootstrap_python_list.json'
        )
    )

    action = AttributeDict()
    action._low_level_execute_command = _test_action_execute_command
    action._connection = AttributeDict()
    action._connection.has_pipelining = True

# Generated at 2022-06-12 21:30:54.895565
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.module_utils.common.removed import removed
    from ansible.module_utils.common.removed import removed_module

    from ansible.plugins.action import ActionBase

    class ActionModule(ActionBase):
        def __init__(self, *args, **kwargs):
            self._discovery_warnings = []
            self._connection = DummyConnection()
            super(ActionModule, self).__init__(*args, **kwargs)

        def _low_level_execute_command(self, cmd, sudoable=True, in_data=None):
            # test cmds that would never actually be run with python
            if cmd == 'false':
                return {'rc': 1, 'stdout': u'', 'stderr': u'foo'}

# Generated at 2022-06-12 21:31:05.717090
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.playbook.action import Action
    from ansible.plugins.action import ActionBase
    from ansible.executor.task_result import TaskResult

    class MockSymbolTable(object):
        def __init__(self, result, warning):
            self._result = result
            self.warnings = []

            if warning:
                self.warnings.append(warning)

        def __getattr__(self, item):
            return self._result
    # set up a simple environment to emulate an embedded interpreter on a host

# Generated at 2022-06-12 21:31:17.005101
# Unit test for function discover_interpreter
def test_discover_interpreter():
    action = None
    host = None
    task_vars = dict(
        ansible_discovery_interpreter='yes',
        ansible_discovery_fallback_interpreter='auto_legacy_silent',
        ansible_discovery_interpreter_python_versions=['/usr/bin/python', '/opt/python/python-2.7.12/bin/python'],
        ansible_discovery_interpreter_python_platform_list=['/usr/bin/python'],
        ansible_discovery_interpreter_fallback_python_versions=['/usr/bin/python'],
    )

# Generated at 2022-06-12 21:31:26.931730
# Unit test for function discover_interpreter
def test_discover_interpreter():
    class TestAction(object):
        def __init__(self):
            self._low_level_execute_command = None
            self._discovery_warnings = []

        def _low_level_execute_command(self, found_interpreters, sudoable, in_data):
            if not self._low_level_execute_command:
                raise NotImplementedError()
            return self._low_level_execute_command(found_interpreters, sudoable, in_data)

    from ansible.executor.discovery import INTERPRETER_PYTHON_DISTRO_MAP, INTERPRETER_PYTHON_FALLBACK

    test_action = TestAction()
    task_vars = dict()


# Generated at 2022-06-12 21:31:39.361790
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # Basic smoke test, not intended to be a complete test of all options covered in the module
    task_vars = {"inventory_hostname": "testhost", "group_names": ["local"],
                 "hostvars": {"testhost": {"ansible_host": "127.0.0.1", "ansible_connection": "local"}}}

    test_class = ActionModule()
    test_class._display = Display()
    test_class._e = 'local'
    test_class.task_vars = task_vars
    test_class._task = {'name': 'testtask'}

    res = discover_interpreter(test_class, 'python', 'auto_legacy', task_vars)
    assert res == u'/usr/bin/python'

# Generated at 2022-06-12 21:31:48.073196
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # case 1: python there, dist supported, exact match
    discovered = discover_interpreter(None, 'python', 'auto',
                                      {'inventory_hostname': 'test host', 'config':
                                          {'DEFAULT':
                                               {'interpreter_python_distro_map':
                                                    {'fedora':
                                                         {'27': u'/usr/bin/python'}},
                                                'interpreter_python_fallback': [u'/usr/bin/python']}
                                           }
                                       })

    assert discovered == u'/usr/bin/python'

    # case 2: python there, dist supported, fuzzy match

# Generated at 2022-06-12 21:32:03.676293
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.executor.action_plugins.discovery import discover_interpreter

    # Test data is a tuple of (target_os, interpreters_present, expected_interpreter)
    # test data doesn't have to be exhaustive, just enough to ensure the code is doing what we think it should be

# Generated at 2022-06-12 21:32:09.132585
# Unit test for function discover_interpreter
def test_discover_interpreter():
    assert discover_interpreter(
        'mock_action',
        'python',
        'auto_legacy',
        dict(inventory_hostname='test_host')
    ) == '/usr/bin/python'

# Generated at 2022-06-12 21:32:12.570231
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # TODO: write a unit test for discover_interpreter, but not just yet

    # def discover_interpreter(action, interpreter_name, discovery_mode, task_vars):
    assert False

# Generated at 2022-06-12 21:32:24.074282
# Unit test for function discover_interpreter
def test_discover_interpreter():
    host = "testhost"
    display = Display()
    display.verbosity = 3
    task_vars = {}

    def _fake_execute_command(cmd, sudoable=False, in_data=None):
        # See python_target.py for structure of script output
        return {'stdout': '{"platform_dist_result": ["RedHatEnterpriseServer", "7.7", "Maipo"]}'}

    action = type('FakeActionModule', (object,), {'_low_level_execute_command': _fake_execute_command})()

    interpreter = discover_interpreter(action, 'python', 'auto', task_vars)
    assert interpreter == u'/usr/bin/python'

    interpreter = discover_interpreter(action, 'python', 'auto_silent', task_vars)
   

# Generated at 2022-06-12 21:32:25.734399
# Unit test for function discover_interpreter
def test_discover_interpreter():
    assert discover_interpreter(None, 'python', 'auto', {'inventory_hostname': 'test'}) == '/usr/bin/python'



# Generated at 2022-06-12 21:32:37.368104
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.module_utils.facts.system.distribution import DistributionFactCollector

    fake_dist = DistributionFactCollector()
    fake_dist._distribution = 'Alpine'
    fake_dist._major_version = '3.5'
    fake_dist_dict = fake_dist.get_facts()

    try:
        discover_interpreter(fake_dist, 'python', 'auto', fake_dist_dict)
    except AssertionError as err:
        assert 'should be a string' in str(err)


# Generated at 2022-06-12 21:32:45.012205
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # Test case 1, discovering an interpreter
    action = module_common.ActionModule(connection=None, task_vars=dict())
    result = discover_interpreter(action, 'python', 'auto', dict())
    assert result == '/usr/bin/python'

    # Test case 2, discovering an interpreter with a discovery mode that does not start with auto, raises a ValueError
    action = module_common.ActionModule(connection=None, task_vars=dict())
    try:
        discover_interpreter(action, 'python', 'manual', dict())
    except Exception as e:
        assert isinstance(e, ValueError)

# Generated at 2022-06-12 21:32:52.209652
# Unit test for function discover_interpreter
def test_discover_interpreter():
    action = None
    interpreter_name = u'python'
    discovery_mode = u'auto'
    task_vars = {}
    task_vars["inventory_hostname"] = u'localhost'
    # if discover_interpreter is not properly working it will not be able to discover the interpreter and will fail with the following:
    # NotImplementedError: unsupported Linux distribution: Red Hat Enterprise Linux Server
    # or
    # NotImplementedError: unsupported Linux distribution:
    # NotImplementedError: unable to get Linux distribution/version info
    discover_interpreter(action, interpreter_name, discovery_mode, task_vars)

# Generated at 2022-06-12 21:33:04.917240
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.module_utils.common.removed import removed_module

    class MockAction():
        def __init__(self):
            self._discovery_warnings = []

    class MockModule():
        def __init__(self, *args, **kwargs):
            self.params = {
                'action': MockAction(),
                'task_vars': dict(),
            }

            for key in kwargs:
                self.params[key] = kwargs[key]

        def exit_json(self, *args, **kwargs):
            self.result = {
                'changed': False,
                'warnings': self.params['action']._discovery_warnings,
            }

    # no warnings

# Generated at 2022-06-12 21:33:15.656318
# Unit test for function discover_interpreter
def test_discover_interpreter():
    import collections
    action = collections.namedtuple('action', ['_low_level_execute_command', '_discovery_warnings'])(lambda x, sudoable=False, in_data=None: {'stderr': u'', 'stdout': x}, [])
    test = lambda interpreter_name, discovery_mode, task_vars: discover_interpreter(action, interpreter_name, discovery_mode, task_vars)

    test('python', 'auto_legacy', {})
    test('python', 'auto_legacy_silent', {})
    test('python', 'auto', {})
    test('python', 'auto_silent', {})

    # Discovering a non-python interpreter is not supported

# Generated at 2022-06-12 21:33:33.210829
# Unit test for function discover_interpreter
def test_discover_interpreter():
    TaskVars = {}
    action = object()
    action._discovery_warnings = []
    action._low_level_execute_command = lambda cmd, sudoable=False, in_data=None: [dict(stdout=cmd)]
    action._connection = object()
    action._connection.has_pipelining = True

    try:
        # noqa: F841
        discover_interpreter(action, 'not-python', 'auto_legacy_silent', TaskVars)
        assert False
    except ValueError as ex:
        assert str(ex).startswith('Interpreter discovery not supported for not-python')

# Generated at 2022-06-12 21:33:40.086402
# Unit test for function discover_interpreter
def test_discover_interpreter():
    action = None

# Generated at 2022-06-12 21:33:45.105652
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # The tests for this code are in test/units/lib/ansible/plugins/action/test_script.py
    # We don't have a good way to run the discover_interpreter function, as it relies on
    # low_level_execute_command and a command module.
    pass

# Generated at 2022-06-12 21:33:55.932817
# Unit test for function discover_interpreter
def test_discover_interpreter():
    """
    Unit test to assert the expected behavior of discover_interpreter method
    """

    # Make a mock action object to pass in
    class FakeAction(object):
        _low_level_execute_command_called = False
        _low_level_execute_command_result = {'rc': 0, 'stdout': '', 'stderr': ''}
        _discovery_warnings = []

        def _low_level_execute_command(self, cmd, sudoable=False, in_data=None):
            self._low_level_execute_command_called = True
            return self._low_level_execute_command_result

        def _check_in_data(self, in_data):
            if not isinstance(in_data, str):
                raise ValueError("invalid in_data")


# Generated at 2022-06-12 21:34:01.441688
# Unit test for function discover_interpreter
def test_discover_interpreter():
    import ansible.modules.system.setup

    class InterpreterAction(ansible.modules.system.setup.ActionModule):
        def _low_level_execute_command(self, cmd, sudoable=True, in_data=None):
            def get_stdout(cmd):
                if cmd == "command -v 'python3'":
                    return "/usr/bin/python3"
                elif cmd == "command -v 'python'":
                    return "/usr/bin/python"
                elif cmd == "echo PLATFORM; uname; echo FOUND; command -v 'python3'; echo ENDFOUND":
                    return u"""
PLATFORM
Linux
FOUND
/usr/bin/python3
ENDFOUND
"""


# Generated at 2022-06-12 21:34:11.686766
# Unit test for function discover_interpreter
def test_discover_interpreter():
    assert discover_interpreter(None, 'python', 'silent', {}) == u'/usr/bin/python'
    assert discover_interpreter(None, 'python', 'warn', {}) == u'/usr/bin/python'
    assert discover_interpreter(None, 'python', 'auto', {}) == u'/usr/bin/python'
    assert discover_interpreter(None, 'python', 'auto_legacy', {}) == u'/usr/bin/python'
    assert discover_interpreter(None, 'python', 'auto_legacy_silent', {}) == u'/usr/bin/python'
    assert discover_interpreter(None, 'python', 'auto_silent', {}) == u'/usr/bin/python'

# Generated at 2022-06-12 21:34:20.634456
# Unit test for function discover_interpreter
def test_discover_interpreter():
    import os
    import sys
    class TestActionModule(object):
        """ fake action plugin for testing """
        def __init__(self):
            self._low_level_execute_command = None
            self._discovery_warnings = []
            self._connection = test_connection()

    class test_connection(object):
        """ fake connection plugin for testing """
        def __init__(self):
            self.has_pipelining = True

    # allow running unit tests outside the ansible dir
    test_dir = os.path.dirname(__file__)
    sys.path.insert(0, os.path.join(test_dir, '..', '..', '..'))

    # setup task vars
    task_vars = {'inventory_hostname': 'testhost'}

    # run the test with a

# Generated at 2022-06-12 21:34:28.256015
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.executor.discovery import _version_fuzzy_match

    assert _version_fuzzy_match(u'1.3', {u'2.0b1': u'foo', u'2.0': u'bar'}) == u'foo'
    assert _version_fuzzy_match(u'2.0', {u'2.0b1': u'foo', u'2.0': u'bar'}) == u'bar'
    assert _version_fuzzy_match(u'2.1', {u'2.0b1': u'foo', u'2.0': u'bar'}) == u'bar'

# Generated at 2022-06-12 21:34:40.211798
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.executor.discovery import get_platform_interpreter

    module = AnsibleModule(argument_spec=dict(discovery_mode=dict(default='auto_legacy_silent')))
    task_vars = dict(action=AnsibleModule(argument_spec={}))

    try:
        res = discover_interpreter(module, u'python', module.params['discovery_mode'], task_vars)
    except InterpreterDiscoveryRequiredError as ex:
        res = get_platform_interpreter(ex.interpreter_name, ex.discovery_mode, task_vars)

    assert res is not None
    assert type(res) is str
    assert res != ''

# Generated at 2022-06-12 21:34:47.710256
# Unit test for function discover_interpreter
def test_discover_interpreter():
    test_action = type('', (), dict(
        _low_level_execute_command=lambda self, f, sudoable, in_data=u'': dict(stdout=u'PLATFORM\nLinux\nFOUND\n/usr/bin/python\nENDFOUND'),
        _discovery_warnings=[],
        _connection=type('', (), dict(has_pipelining=True))(),
    ))()

    test_vars = dict()

    result = discover_interpreter(test_action, 'python', 'smart', test_vars)
    assert result == u'/usr/bin/python'

# Generated at 2022-06-12 21:35:14.206456
# Unit test for function discover_interpreter
def test_discover_interpreter():
    assert discover_interpreter('', 'foo', 'bar', {}) == '/usr/bin/python'
    assert discover_interpreter('', 'python', 'auto', {}) == '/usr/bin/python'
    assert discover_interpreter('', 'python', 'auto_legacy', {}) == '/usr/bin/python'
    assert discover_interpreter('', 'python', 'auto_silent', {}) == '/usr/bin/python'

    assert discover_interpreter('', 'python', 'something_else', {}) == '/usr/bin/python'
    assert discover_interpreter('', 'python', 'auto_legacy_silent', {}) == '/usr/bin/python'


# Generated at 2022-06-12 21:35:25.224579
# Unit test for function discover_interpreter
def test_discover_interpreter():
    import ansible.module_utils.discovery.python_interpreter

    # prepare test data
    python = ansible.module_utils.discovery.python_interpreter
    python.config = ansible.config.manager.ConfigManager
    python.display = ansible.utils.display.Display()
    python.config.CONFIG_FILE = 'test/ansible.cfg'
    ansible.config.manager.read_config_file(python.config)

    # test with interpreter
    action = ansible.playbook.action_write_locks.ActionWriteLocks()
    task_vars = dict()
    interpreter_name = 'python'
    discovery_mode = 'auto'

# Generated at 2022-06-12 21:35:37.418336
# Unit test for function discover_interpreter
def test_discover_interpreter():
    class MockAction(object):
        def __init__(self):
            self._discovery_warnings = []
            self._connection = MockConnection(False)

        def _low_level_execute_command(self, cmd, sudoable=False, in_data=None):
            if cmd == 'command -v /usr/bin/python3':
                return {'stderr': u'', 'stdout': u'/usr/bin/python3'}
            if cmd == 'command -v /usr/bin/python2':
                return {'stderr': u'', 'stdout': u'/usr/bin/python2'}

# Generated at 2022-06-12 21:35:49.011743
# Unit test for function discover_interpreter

# Generated at 2022-06-12 21:35:56.494864
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.executor.task_result import TaskResult
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.play_iterator import PlayIterator

    class TestTaskResult(TaskResult):
        def __init__(self, *args, **kwargs):
            super(TestTaskResult, self).__init__(*args, **kwargs)
            # Bypassing _low_level_execute_command via this hacky override.
            self._result = {'cmd': args[0], 'stdout': args[-1], 'stderr': ''}

    class TestPlayIterator(PlayIterator):
        def __init__(self, *args, **kwargs):
            super(TestPlayIterator, self).__init__(*args, **kwargs)


# Generated at 2022-06-12 21:36:06.604547
# Unit test for function discover_interpreter
def test_discover_interpreter():
    platform_type = 'linux'
    found_interpreters = [u'/usr/bin/python', u'/usr/bin/python2', u'/usr/bin/python3']

    raw_stdout = u'\nPLATFORM\n {0}\nFOUND\n {1}\nENDFOUND\n'.format(platform_type, found_interpreters[0])

    match = foundre.match(raw_stdout)
    if not match:
        raise ValueError('unexpected output from Python interpreter discovery')

    assert match.groups()[0] == platform_type
    assert match.groups()[1] == found_interpreters[0]
    assert match.groups()[1] == found_interpreters[0]

# Generated at 2022-06-12 21:36:14.282456
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.plugins.action import ActionBase
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, sources='localhost,')
    variable_manager.set_inventory(inventory)

    # create a play

# Generated at 2022-06-12 21:36:25.781780
# Unit test for function discover_interpreter
def test_discover_interpreter():
    test_host = {'ansible_host': 'test_host'}
    test_vars = {'inventory_hostname': 'test_host'}

    display.verbosity = 4

    # Failures for discovery mode auto_legacy_silent
    def test_discovery_auto_legacy_silent_failures():
        test_action = MockAction()
        interpreter_name = 'python'
        discovery_mode = 'auto_legacy_silent'

        # Error when discovery mode is not silent
        test_action._discovery_warnings = []
        interpret = discover_interpreter(test_action, interpreter_name, discovery_mode, test_vars)

        assert interpret is None
        assert not test_action._discovery_warnings

        # Fail when no interpreters found

# Generated at 2022-06-12 21:36:36.349322
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.executor import task_executor

    test_host = u'localhost'
    test_task_vars = dict()
    test_action = task_executor.ActionTaskExecutor(host=test_host, task_vars=test_task_vars)

    # impossible discovery_mode value to verify function args are checked
    impossible_discovery_mode = u'impossible'

    # test empty configs
    test_task_vars = dict(ansible_python_interpreter=u'/usr/bin/python2')
    test_action = task_executor.ActionTaskExecutor(host=test_host, task_vars=test_task_vars)
    test_action.display = display

    # With empty configs and discovery_mode=auto, we expect the fallback of /usr/bin/

# Generated at 2022-06-12 21:36:41.632888
# Unit test for function discover_interpreter
def test_discover_interpreter():
    assert _version_fuzzy_match('1.0', {'1.0': 'python_1.0'}) == 'python_1.0'
    assert _version_fuzzy_match('1.0', {'1.0': 'python_1.0', '2.0': 'python_2.0'}) == 'python_1.0'
    assert _version_fuzzy_match('1.0', {'1.0': 'python_1.0', '2.0': 'python_2.0', '2.1': 'python_2.1'}) == 'python_1.0'

# Generated at 2022-06-12 21:37:29.584006
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # Test for default interpreter /usr/bin/python
    host = 'unknown'
    res = None
    platform_type = 'unknown'
    found_interpreters = [u'/usr/bin/python']  # fallback value
    is_auto_legacy = False
    is_silent = False

    platform_python_map = C.config.get_config_value('INTERPRETER_PYTHON_DISTRO_MAP', variables={})
    bootstrap_python_list = C.config.get_config_value('INTERPRETER_PYTHON_FALLBACK', variables={})

    display.vvv(msg=u"Attempting {0} interpreter discovery".format('python'), host=host)

    command_list = ["command -v '%s'" % py for py in bootstrap_python_list]
   

# Generated at 2022-06-12 21:37:36.925548
# Unit test for function discover_interpreter
def test_discover_interpreter():
    import socket
    import sys
    import unittest

    import ansible.config
    from ansible.executor.discovery import discover_interpreter

    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.connection import Connection


    class TestModule(AnsibleModule):
        def __init__(self, *args, **kwargs):
            super(TestModule, self).__init__(*args, **kwargs)
            self._ansible_version = '2.6.0'
            self._ansible_connection = 'local'
            self._ansible_module_name = 'mock test module'
            self._ansible_module_name_version = 'mock test module 1.0'
            self._ansible_verbosity = 1

# Generated at 2022-06-12 21:37:46.658517
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.module_utils.six import PY3
    from ansible.module_utils.facts import default_fact_collection
    action = default_fact_collection()
    task_vars = C.config.get_config_value('DEFAULT_MODULE_UTILS_PATH', variables=action._task.__dict__)
    # python2

# Generated at 2022-06-12 21:37:49.205206
# Unit test for function discover_interpreter
def test_discover_interpreter():
    discover_interpreter(None, 'python', 'auto_legacy_silent', {'inventory_hostname': 'test'})
    assert True

# Generated at 2022-06-12 21:38:01.299438
# Unit test for function discover_interpreter
def test_discover_interpreter():
    """
    This unit test verifies the functions used to discovered the interpreter works
    """
    # Get the interpreter_name and discovery_mode as a string
    test_vars = {'ansible_discovery_interpreter': 'python', 'discovery_mode': 'auto'}
    interpreter_name = test_vars['ansible_discovery_interpreter']
    discovery_mode = test_vars['discovery_mode']
    try:
        discover_interpreter(None, interpreter_name, discovery_mode, test_vars)
    except InterpreterDiscoveryRequiredError:
        # In this case an exception is what we want
        pass
    except Exception as ex:
        raise AssertionError('discover_interpreter throws unexpected exception during discovery: {0}'.format(to_text(ex)))

    #

# Generated at 2022-06-12 21:38:09.455970
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.plugins.action.discovery import ActionModule as discovery_action
    from ansible.parsing.vault import VaultLib
    from ansible.playbook.play_context import PlayContext
    # Set fake args

# Generated at 2022-06-12 21:38:17.212936
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.module_utils._text import to_bytes
    from ansible.plugins.action import ActionBase
    import os
    import shutil
    import tempfile

    class TestActionModule(ActionBase):
        def _low_level_execute_command(self, cmd, sudoable=False, in_data=None):
            if cmd.endswith(u'linux_target.py'):
                return {'stdout': to_bytes(u'{"platform_dist_result": ["ubuntu","18.04","bionic"],"osrelease_content": "\nVERSION="18.04 LTS (Bionic Beaver)"\n"}')}

# Generated at 2022-06-12 21:38:22.216761
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.plugins.action import action_base
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.process.task_result import TaskResult
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.inventory.host import Host
    from ansible.vars.hostvars import HostVars
    import mock


# Generated at 2022-06-12 21:38:31.468357
# Unit test for function discover_interpreter
def test_discover_interpreter():
    import json
    import sys
    import unittest
    from ansible.module_utils.compat.version import LooseVersion

    from ansible.executor.discovery import discover_interpreter
    from ansible.modules.system import platform


# Generated at 2022-06-12 21:38:37.513919
# Unit test for function discover_interpreter
def test_discover_interpreter():
    action = object()
    task_vars = {}
    class AnsibleModule(object):
        def _low_level_execute_command(self, command, sudoable=False, in_data=None):
            assert command.split()[-1] in C.config.get_config_value('INTERPRETER_PYTHON_FALLBACK', variables=task_vars)
            if 'uname' in command:
                return {'stdout': u'PLATFORM\nLinux\nFOUND\n/usr/bin/python\nENDFOUND'}
            return {'stdout': u'{"osrelease_content": "ID=ubuntu\\nVERSION_ID=14.04.5\\n"}'}

    action._low_level_execute_command = AnsibleModule._low_level_execute_command

# Generated at 2022-06-12 21:39:11.105621
# Unit test for function discover_interpreter
def test_discover_interpreter():
    action = Mock()
    interpreter_name = 'python'
    discovery_mode = 'auto'
    task_vars = {
        'inventory_hostname': 'default'
    }
    discover_interpreter(action,interpreter_name,discovery_mode,task_vars)
    assert action._low_level_execute_command.call_count == 1
    action._low_level_execute_command.assert_called_with("command -v 'python3'",sudoable=False)

# Mock objects for unit testing

# Generated at 2022-06-12 21:39:19.015973
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.executor.discovery.host_info import HostInfo

    # FUTURE: move to pytest

    debug = False


# Generated at 2022-06-12 21:39:28.930214
# Unit test for function discover_interpreter
def test_discover_interpreter():
    import os
    import platform
    from ansible.module_utils.basic import AnsibleModule
    from ansible.plugins.action.normal import ActionModule as _ActionModule
    from ansible.playbook.task_include import TaskInclude
    from ansible.template import Templar
    from ansible.utils.vars import combine_vars
    from ansible.utils.vars import merge_hash
    action_module = 'normal'
    class ActionModule(_ActionModule):
        def run(self, tmp=None, task_vars=None):
            return {
                'discovery_warnings': [],
                '_ansible_no_log': False,
                'changed': False
            }
    name = 'test_discover_interpreter'

# Generated at 2022-06-12 21:39:39.991290
# Unit test for function discover_interpreter
def test_discover_interpreter():
    # TODO: expand this more
    found_interpreters = [u'/usr/bin/python', u'/opt/python/python-3.6.1/bin/python3.6']
    assert u'/usr/bin/python' == discover_interpreter('', 'python', 'auto_legacy_silent', {'inventory_hostname': 'unknown'})

    # TODO: add more tests for linux discovery

    # test _version_fuzzy_match()

# Generated at 2022-06-12 21:39:48.927851
# Unit test for function discover_interpreter
def test_discover_interpreter():

    class MockAction(object):
        def __init__(self):
            self._discovery_warnings = []

        def _low_level_execute_command(self, cmd, sudoable=True, in_data=None, executable='/bin/sh'):
            if cmd == 'command -v /usr/bin/python3':
                return {'stdout': '/usr/bin/python3', 'stderr': ''}
            elif cmd == 'command -v /usr/bin/python2':
                return {'stdout': '/usr/bin/python2', 'stderr': ''}
            elif cmd.startswith('command -v python'):
                return {'stdout': '', 'stderr': ''}

# Generated at 2022-06-12 21:39:59.733960
# Unit test for function discover_interpreter
def test_discover_interpreter():
    from ansible.module_utils.common.json_utils import _json_load

    # make copies of the test data, so we're not modifying the originals
    test_data_mod = pkgutil.get_data('ansible.executor.discovery', 'test_data_modified.json')
    test_data_mod_json = json.loads(test_data_mod)

    output_mod_python_target = pkgutil.get_data('ansible.executor.discovery', 'output_modified_python_target.py')

    # test data is intentionally non-sensical and not a real system (for example, Ubuntu 17.10 ships with Python 3.6.x
    # but that's not in the major version lists we support yet)

# Generated at 2022-06-12 21:40:04.086188
# Unit test for function discover_interpreter
def test_discover_interpreter():
    python_path = discover_interpreter(None, 'python', 'auto_legacy', {'ansible_python_interpreter': None})
    assert python_path is not None
    python_path = discover_interpreter(None, 'python', 'auto', {'ansible_python_interpreter': None})
    assert python_path is not None