

# Generated at 2022-06-13 11:18:57.937159
# Unit test for constructor of class ActionModule
def test_ActionModule():

    class test_module(ActionModule):
        _display = Display()
        _module_name = 'test_module'
        _supports_check_mode = False

        def run(self, tmp=None, task_vars=None):
            return None
    t = test_module(task=None, connection=None, play_context=None, loader=None,
                    templar=None, shared_loader_obj=None)
    assert t.run(tmp=None, task_vars=None) is None

# Generated at 2022-06-13 11:19:09.004780
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """Test the yum action plugin handles the use and use_backend parameters correctly."""
    import sys
    if sys.version_info < (2, 7):
        import unittest2 as unittest
    else:
        import unittest

    from ansible.compat.tests.mock import patch, Mock
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.parsing.vault import VaultLib

    class TestActionModule(unittest.TestCase):
        """Unit test for the _run() method of class ActionModule."""

        class MockActionBase(ActionBase):
            """Mock ActionBase object."""

            # pylint: disable=too-few-public-methods

            def __init__(self):
                """Initialize a Mock ActionBase object."""

# Generated at 2022-06-13 11:19:10.142132
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """
    Run unit test for module code.
    """
    pass

# Generated at 2022-06-13 11:19:20.151711
# Unit test for constructor of class ActionModule
def test_ActionModule():
    ''' setup and run tests for the yum action plugin '''
    from ansible.module_utils.common._collections_compat import MutableMapping
    from ansible.module_utils._text import to_text
    from ansible.plugins.action import ActionBase
    from ansible.utils.display import Display
    from ansible.utils.plugin import combine_vars, get_all_plugin_loaders

    display = Display()
    loader, action_loader, _ = get_all_plugin_loaders()

    # data and results --------------------------------------------------------
    class Controller():
        def __init__(self, data):
            self.data = data

        def get(self, key, default=None):
            return self.data.get(key, default)

    from collections import namedtuple

# Generated at 2022-06-13 11:19:26.518780
# Unit test for constructor of class ActionModule
def test_ActionModule():
    mock_action_module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert mock_action_module is not None
    assert isinstance(mock_action_module, ActionModule)
    assert mock_action_module.TRANSFERS_FILES is False


# Generated at 2022-06-13 11:19:29.009151
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule(None, None, None)

    assert VALID_BACKENDS == frozenset(('yum', 'yum4', 'dnf'))

# Generated at 2022-06-13 11:19:31.421169
# Unit test for constructor of class ActionModule
def test_ActionModule():
    ast_obj = ActionModule({}, {}, 'ansible.legacy.yum', {}, {'use_backend': 'auto'})
    assert ast_obj is not None

# Generated at 2022-06-13 11:19:39.821990
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule('action',
                                 dict(name='yum',
                                      args=dict(name=['zsh', 'vim'], state=['present', 'absent'], debug=True)),
                                 'test',
                                 'test',
                                 'test',
                                 'test',
                                 'test',
                                 'test',
                                 'test',
                                 'test',
                                 'test',
                                 'test',
                                 'test')
    assert action_module._supports_async is True
    assert action_module._supports_check_mode is True

# Generated at 2022-06-13 11:19:44.096697
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''
    Unit test for method run of class ActionModule
    '''

    test1 = ActionModule()
    test1._shared_loader_obj.module_loader.has_plugin = lambda plugname : True
    test1._execute_module = lambda plugname, module_name, task_vars: {"failed": False}
    test1._task.async_val = False
    test1._connection._shell.tmpdir = "/tmp/asdf"
    test1._task.delegate_to = None
    test1._task.delegate_facts = True
    test1._task.args = dict(use="yum")

    test2 = ActionModule()
    test2._shared_loader_obj.module_loader.has_plugin = lambda plugname : False
    test2._task.async_val = True
    test2

# Generated at 2022-06-13 11:19:44.646380
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True

# Generated at 2022-06-13 11:20:01.243042
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # 'module' is a reserved keyword
    from ansible.module_utils import basic
    # instantiate module class
    module = basic.AnsibleModule(argument_spec={
        'use_backend': {'required': False, 'type': 'str'}},
        supports_check_mode=True,
        add_file_common_args=True,
    )
    # create class instance
    action = ActionModule(module, {'use_backend': 'auto'})
    # action module handler
    result = action.run({}, {})
    assert(type(result) == dict)
    assert('failed' in result)
    assert(result['failed'])
    assert('msg' in result)
    assert(result['msg'])

# Generated at 2022-06-13 11:20:02.993757
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule()
    assert isinstance(action_module, ActionBase)

# Generated at 2022-06-13 11:20:06.849031
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule(
        task=dict(args=dict(use='auto')),
        connection=dict(),
        play_context=dict(),
        loader=dict(),
        templar=dict(),
        shared_loader_obj=dict())
    am.run(tmp=None, task_vars=None)

# Generated at 2022-06-13 11:20:12.456918
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    import sys
    if sys.version_info[:2] < (2, 7):
        import unittest2 as unittest
    else:
        import unittest

    class TestActionModule(unittest.TestCase):

        # """Test class to test run method in class ActionModule"""

        def test_normal_actions(self):

            # """Test run method with normal inputs"""

            test_action_module = ActionModule()
            test_action_module._task = {}
            test_action_m

# Generated at 2022-06-13 11:20:14.136993
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(task=dict(), connection=dict(), play_context=dict(), loader=dict(), templar=dict(), shared_loader_obj=dict())

# Generated at 2022-06-13 11:20:15.832158
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule()
    assert action_module is not None

# Generated at 2022-06-13 11:20:18.634001
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """ Unit test for method run of class ActionModule """
    _task = {'args': {'name': 'ansible'}}
    test_obj = ActionModule(task=_task)
    assert test_obj is not None

# Generated at 2022-06-13 11:20:19.752893
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Unimplemented and no testable component
    pass

# Generated at 2022-06-13 11:20:22.673949
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

# Generated at 2022-06-13 11:20:24.220430
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(task=dict())
    assert isinstance(action_module, ActionBase)

# Generated at 2022-06-13 11:20:37.173221
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule({},{})
    assert module


# Generated at 2022-06-13 11:20:38.659612
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = 'ansible.legacy.yum'
    assert module == ActionModule._ActionModule__name

# Generated at 2022-06-13 11:20:40.094299
# Unit test for constructor of class ActionModule
def test_ActionModule():

    module = ActionModule(
        task=dict(args=dict())
    )
    assert module

# Generated at 2022-06-13 11:20:50.789461
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.module_utils.six import StringIO
    from ansible.utils.vars import ModuleArgsParser

    m3 = {'ansible_pkg_mgr': 'yum3'}
    m4 = {'ansible_pkg_mgr': 'yum4'}


# Generated at 2022-06-13 11:20:52.584713
# Unit test for constructor of class ActionModule
def test_ActionModule():
    obj = ActionModule()
    assert obj


# Generated at 2022-06-13 11:21:01.893642
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.loader import add_all_plugin_dirs
    from ansible.plugins.action.yum import ActionModule
    from ansible.modules.package.yum import YumModule
    import os

    # Create fake plugin directories
    plugin_dirs = []
    for i in range(2):
        d = 'test_ActionModule_run/' + str(i)
        os.makedirs(d)
        plugin_dirs.append(d)

    # Add fake plugin dirs to ansible plugin search path
    add_all_plugin_dirs(plugin_dirs)

    # Create fake yum module
    class YumModule(object):
        def __init__(self, remote_module=None):
            self.remote_module = remote_module


# Generated at 2022-06-13 11:21:02.437139
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 11:21:11.629017
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Part 1: Create instance of class ActionModule
    mod = ActionModule()

    # Part 2: Check that class ActionModule is subclass of ActionBase
    assert issubclass(ActionModule, ActionBase), 'ActionModule is not subclass of ActionBase'

    # Part 3: Check that class ActionModule is instance of ActionBase
    assert isinstance(mod, ActionBase), 'ActionModule is not instance of ActionBase'

    # Part 4: Call method run and check that it doesn't raise any exceptions
    assert mod.run() == {'failed': True, 'msg': "Could not detect which major revision of yum is in use, which is required to determine module backend.", 'msg': "You should manually specify use_backend to tell the module whether to use the yum (yum3) or dnf (yum4) backend"}

# Generated at 2022-06-13 11:21:12.173190
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 11:21:15.537396
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule()
    assert action_module._supports_check_mode == True
    assert action_module._supports_async == True

# Generated at 2022-06-13 11:21:39.612070
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(task=dict())
    assert module is not None

# Generated at 2022-06-13 11:21:40.293911
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 11:21:43.791503
# Unit test for constructor of class ActionModule
def test_ActionModule():

    p = ActionModule("task_module", {})
    assert p._shared_loader_obj is not None
    assert p._connection is not None
    assert p._templar is not None
    assert p._task is not None
    assert p._loader is not None
    assert p._play_context is not None

    # _supports_async should be True as it is set in constructor
    assert p._supports_async is True
    # _supports_check_mode should be True as it is set in constructor
    assert p._supports_check_mode is True

    # TRANSFERS_FILES should be False as it is set in the class
    assert p.TRANSFERS_FILES is False

# Generated at 2022-06-13 11:21:59.427581
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.task import Task
    from ansible.executor.task_result import TaskResult
    from ansible.executor.play_context import PlayContext
    from ansible.playbook.play_context import PlayContext as AnsiblePlayContext
    from ansible.playbook.play import Play
    from ansible.module_utils.six import string_types

    action_module = ActionModule()

    action_module._task = Task()
    action_module._task.async_val = None

    action_module._connection = {}
    action_module._connection['_shell'] = {}

    action_module._connection['_shell']['tmpdir'] = '/tmp'

    action_module._task.delegate_to = None
    action_module._task.delegate_facts = None

    action_module._templ

# Generated at 2022-06-13 11:22:04.453530
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule()
    assert(module.run() == {'failed': True, 'msg': ('Could not detect which major revision of yum is in use, which is required to determine module backend.',
      "You should manually specify use_backend to tell the module whether to use the yum (yum3) or dnf (yum4) backend})")}
    )

# Generated at 2022-06-13 11:22:04.999467
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 11:22:07.860981
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Prepare Mocks & Stubs
    display = DisplayStub()
    my_action = ActionModule(display)

    # Run test case
    result = my_action.run(None, {})


# Class stubs

# Generated at 2022-06-13 11:22:15.913268
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # == Tests for action module run method ==
    # Test1:
    # In this test we pass the test_ActionModule_run.module into the run method
    # and check if the run method returns the module name
    test_module_name = "test_module"
    test_Task = type("test_Task", (object, ), {
        "args": {"use": test_module_name},
        "delegate_to": None,
        "delegate_facts": True,
        "async_val": False,
    })
    test_TaskVars = {}
    test_Connection = type("test_Connection", (object, ), {
        "_shell": type("_shell", (object, ), {"tmpdir": "/tmp"})
    })
    test_Connection._shell.tmpdir = "/tmp"
    test_SharedLoader

# Generated at 2022-06-13 11:22:19.756492
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule()
    print(action_module.VALID_BACKENDS)
    print(action_module._supports_async)
    print(action_module._supports_check_mode)
    print(action_module.run(tmp=None, task_vars=None))

# Generated at 2022-06-13 11:22:21.055738
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    module = ActionModule()

    # Execute the run() method
    module.run()

# Generated at 2022-06-13 11:23:08.203130
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert isinstance(ActionModule(), ActionModule)


# Generated at 2022-06-13 11:23:10.003006
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(None, None)
    assert module != None


# Generated at 2022-06-13 11:23:15.174859
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    #test for not supported parameters
    action_module = ActionModule(None, None)
    task_args = {'use': 'yum4', 'use_backend': 'yum4'}
    result = action_module.run(None, None, task_args=task_args)
    assert result['failed'] == True
    assert result['msg'] == "parameters are mutually exclusive: ('use', 'use_backend')"

# Generated at 2022-06-13 11:23:17.406599
# Unit test for constructor of class ActionModule
def test_ActionModule():
    task_args = dict(A=10)
    am = ActionModule(None, task_args)
    assert task_args == am._task.args

# Generated at 2022-06-13 11:23:24.852128
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task_include import TaskInclude
    from ansible.plugins.loader import action_loader
    from ansible.vars.manager import VariableManager

    playbook = "test.yml"
    play_context = PlayContext()
    play_context._loader = None
    task = TaskInclude()
    task._role = None
    # var_manager = VariableManager()
    var_manager = None
    action_mod = action_loader.get("yum", play_context, task, var_manager)
    action_mod = action_mod()
    action_mod._config = None
    action_mod._task = task
    action_mod.display = Display()
    action_mod.display.verbosity = 2

# Generated at 2022-06-13 11:23:26.486347
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(None, None) is not None

# Generated at 2022-06-13 11:23:39.008469
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Declare fake objects for testing.
    class _fake_module():
        def __init__(self):
            self._debug = True
            self._supports_check_mode = True
            self._supports_async = True
            self._templar = lambda x: None
    class _fake_connection():
        def __init__(self):
            self._shell = lambda: None
            self._shell.tmpdir = '/tmp/ansible'
    class _fake_task():
        def __init__(self):
            self._debug = True
            self._templar = lambda x: x
            self._shared_loader_obj = _fake_module()

# Generated at 2022-06-13 11:23:39.886856
# Unit test for constructor of class ActionModule
def test_ActionModule():
    test_class = ActionModule()
    assert test_class is not None

# Generated at 2022-06-13 11:23:47.230150
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import socket
    import pytest
    from ansible.plugins.action.yum import ActionModule
    from ansible.utils.path import makedirs_safe
    from ansible.utils.display import Display
    from ansible.module_utils._text import to_bytes, to_text
    from ansible.module_utils.common.collections import is_iterable
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins.connection.local import Connection
    from ansible.executor.task_queue_manager import TaskQueueManager

    display = Display()

    # Open a new connection
    socket_path = '/tmp/ansible_action_plugin_yum_unit.socket'
    makedirs_safe(socket_path)
    connection = Connection(socket_path)
    connection.connect()

   

# Generated at 2022-06-13 11:23:54.859919
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """
    ActionModule
    """

    # Arrange
    action_raw_params = {}
    action_connection = 'local'
    action_persistent_action = None
    action_task_vars = {}
    action_loader = None

    # Act
    action = ActionModule(
        action_raw_params,
        action_connection,
        action_persistent_action,
        action_task_vars,
        action_loader
    )

    # Assert
    assert action._shared_loader_obj is not None
    assert action._templar is not None

# Generated at 2022-06-13 11:25:39.027213
# Unit test for constructor of class ActionModule
def test_ActionModule():
    in_action = {
        'module': 'yum',
        'version_added': '2.1',
        'short_description': 'Manages packages with the yum package manager',
        'description': 'Manages packages with the yum package manager. This module',
        'options': {'arg1': {'required': True, 'type': 'str'}, 'arg2': {'default': 'value for arg2', 'type': 'str'}},
        '_uses_shell': False,
        '_uses_delegate': True,
        '_raw_params': '',
        '_params': '',
        '_task_cache': None,
        '_executor_data': {},
        '_async_val': 'test_val',
        'args': {}
    }
    in_task_v

# Generated at 2022-06-13 11:25:40.835500
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Constructor test for ActionModule
    module = ActionModule(task=dict(), connection=dict(), play_context=dict(), loader=dict(), templar=dict(), shared_loader_obj=dict())
    assert module

import os


# Generated at 2022-06-13 11:25:50.138826
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # create an instance of the class with the mock and assert that
    # the run() method does what it's supposed to do
    action_module = ActionModule()
    action_module._execute_module = lambda x: {'failed': True, 'stdout': '', 'stderr': '', 'rc': 1, 'stdout_lines': [], 'stderr_lines': []}
    action_module._remove_tmp_path = lambda x: None
    action_module._display.vvv = lambda x, hostname=None: None
    # store the initial connection object
    initial_connection = action_module._connection
    action_module._connection = MagicMock()
    action_module._connection._shell.tmpdir = '/tmp/test'
    action_module._task.args = {'use': 'yum'}


# Generated at 2022-06-13 11:26:03.234557
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    rtn = {}
    def x(task_vars):
        if task_vars['failed']:
            raise AnsibleActionFail("error")
        rtn['failed'] = task_vars['failed']
        rtn['msg'] = task_vars['msg']
        rtn['ansible_facts'] = task_vars['ansible_facts']
        pass
    mod = ActionModule(x, x)
    mod.display = display
    mod._task.args = {}

    def test_templar(x):
        if x == 'hostvars[\'host1\'][\'ansible_facts\'][\'pkg_mgr\']':
            return 'yum4'
        if x == 'ansible_facts.pkg_mgr':
            return 'yum4'
        return None
    mod._tem

# Generated at 2022-06-13 11:26:07.308620
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    m = ActionModule()
    result = m.run(task_vars=dict(ansible_facts=dict(pkg_mgr='yum3')))
    assert result.get('changed', True) == False
    assert result.get('msg', "pass") == "pass"

# Generated at 2022-06-13 11:26:14.378714
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils.common.text.converters import to_bytes
    import os
    import tempfile
    import yaml
    from ansible.module_utils._text import to_text

    # Preparing tempfile and data we need, this is only for running unit test
    tmp_dir = tempfile.mkdtemp()
    tempfile_path = os.path.join(tmp_dir, 'test_file.yaml')
    temp_file = open(tempfile_path, 'wb')
    test_data = {'test_data_key': 'test_data_value'}

    yaml.dump(test_data, stream=temp_file, default_flow_style=False)
    # Closing tempfile
    temp_file.close()


# Generated at 2022-06-13 11:26:18.641076
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    result = dict(
        changed=False,
        failed=True,
        msg='Could not detect which major revision of yum is in use, which is required to determine module backend.',
        ansible_facts=dict(
            pkg_mgr='auto'
        )
    )
    assert ActionModule().run(task_vars=dict(ansible_pkg_mgr='auto')), result

# Generated at 2022-06-13 11:26:22.090457
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import sys
    import unittest

    # Constructor of class ActionModule
    class TestActionModule(unittest.TestCase):
        def test_constructor_without_args(self):
            action_module = ActionModule()
            self.assertIsInstance(action_module, ActionModule)

# Generated at 2022-06-13 11:26:26.704734
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    task_vars = {'ansible_facts': {'pkg_mgr': 'auto'}}
    tmp = None
    module = "yum"
    task_args = {'use': 'auto'}
    my_obj = ActionModule(task_vars, tmp, module, task_args)
    my_result = my_obj.run(tmp, task_vars)
    assert my_result['failed'] == True

# Generated at 2022-06-13 11:26:28.322535
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert action_module is not None