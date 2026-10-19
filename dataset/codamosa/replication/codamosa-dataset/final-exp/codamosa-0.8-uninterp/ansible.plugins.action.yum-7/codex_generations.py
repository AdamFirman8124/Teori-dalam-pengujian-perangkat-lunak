

# Generated at 2022-06-13 11:18:59.131509
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import json
    import sys

    from ansible.module_utils.facts import Facts
    from ansible.playbook.play_context import PlayContext

    from ansible.module_utils._text import to_bytes, to_native

    # Simple test to make sure we get a yum3 and yum4 backend

# Generated at 2022-06-13 11:19:00.114552
# Unit test for constructor of class ActionModule
def test_ActionModule():
    a = ActionModule()
    assert a is not None


# Generated at 2022-06-13 11:19:11.008235
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.module_utils.common.removed import removed_module

    am = ActionModule(
        task=dict(async_val=False, delegate_to="localhost", delegate=False, async_timeout=300),
        connection=dict(connect_timeout=10),
        play_context=dict(check_mode=False, diff=False),
        loader=dict(),
        templar=dict(),
        shared_loader_obj=dict()
    )
    # Test all options of module parameter
    assert am.run(tmp=None, task_vars=dict(ansible_pkg_mgr='auto')) == {'failed': True, 'msg': "Could not detect which major revision of yum is in use, which is required to determine module backend.", 'ansible_facts': {'pkg_mgr': 'auto'}}
   

# Generated at 2022-06-13 11:19:12.879252
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """Unit test for constructor of class ActionModule"""

    assert True

# Generated at 2022-06-13 11:19:14.649508
# Unit test for method run of class ActionModule
def test_ActionModule_run():
  # Test that if use and use_backend are specified it will raise error
  assert True == False


# Generated at 2022-06-13 11:19:22.102985
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule()

    # Check with args that do not include use/use_backend
    # This should throw an exception:
    args = {}
    try:
        module.run(args)
    except AnsibleActionFail as e:
        assert ("parameters are mutually exclusive: ('use', 'use_backend')" in e)

    # Check with args that includes both use/use_backend
    # This should throw an exception:
    args = { 'use': 'auto', 'use_backend': 'yum' }
    try:
        module.run(args)
    except AnsibleActionFail as e:
        assert ("parameters are mutually exclusive: ('use', 'use_backend')" in e)

# Generated at 2022-06-13 11:19:24.613186
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ''' Unit test for method run of class ActionModule
    '''
    import types

    display = Display()
    pm = ActionModule(None, display)
    assert type(pm.run) == types.MethodType



# Generated at 2022-06-13 11:19:28.572000
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule(load_from_file=False, task=True, connection=True, play_context=True, loader=True, templar=True, shared_loader_obj=True)
    assert len(action._shared_loader_obj.module_loader) == 2

# Generated at 2022-06-13 11:19:29.878475
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action1 = ActionModule()

# Generated at 2022-06-13 11:19:30.490667
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 11:19:45.820374
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule()

    # Testing "auto" detection
    # not a dictionary => auto
    assert module._execute_module(module_name="test", module_args={'auto': 'test'})['auto'] == 'test'
    # not a dictionary => auto
    assert module._execute_module(module_name="test", module_args={'auto': None})['auto'] is None
    # not a dictionary => auto
    assert module._execute_module(module_name="test", module_args={'auto': False})['auto'] is False
    # not a dictionary => auto
    assert module._execute_module(module_name="test", module_args={'auto': True})['auto'] is True

    # "auto" detection, this is a dictionary => package manager
    #  yum3

# Generated at 2022-06-13 11:19:50.450054
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    task_vars = dict()
    tmp = None
    proxy = None
    module_name = 'yum'
    module_args = dict(name='httpd')
    args = dict()
    result = dict()
    action = ActionModule(task=args, connection=proxy, play_context=args, loader=None, templar=None, shared_loader_obj=None)
    result = action.run(tmp, task_vars)
    assert result['failed'] == False



# Generated at 2022-06-13 11:19:52.338325
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(task=object(), connection=object(), play_context=object(), loader=object(),
                                 templar=object(), shared_loader_obj=object())
    assert action_module

# Generated at 2022-06-13 11:20:03.987766
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''
    Unit test for method run of class ActionModule
    '''

    # Set up test inputs
    tmp = '/path'
    task_vars = {}
    ansible_facts = {}

    #Set up mock objects
    action_module = ActionModule()
    mock_display = Display()
    action_module._templar = mock_templar
    action_module._execute_module = mock_execute_module
    action_module._remove_tmp_path = mock_remove_tmp_path
    # Test with 'use' and 'use_backend' as arguments
    self._task.args = {'use': 'yum3', 'use_backend': 'yum4'}
    result = action_module.run(tmp, task_vars)
    assert result['failed'] is True

# Generated at 2022-06-13 11:20:06.960594
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Creating a class object for class ActionModule
    action_module_obj = ActionModule()

    # Asserting the retun of method run for class ActionModule
    assert(action_module_obj.run())

# Generated at 2022-06-13 11:20:08.280700
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule is not None

# Generated at 2022-06-13 11:20:09.365645
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule(None, {}, None, None)
    assert action is not None

# Generated at 2022-06-13 11:20:11.156570
# Unit test for constructor of class ActionModule
def test_ActionModule():
    yum_action_module = ActionModule(None, None, None, None, None, None)
    assert yum_action_module is not None

# Generated at 2022-06-13 11:20:12.466122
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert False



# Generated at 2022-06-13 11:20:12.922864
# Unit test for constructor of class ActionModule
def test_ActionModule():
    a = ActionModule()


# Generated at 2022-06-13 11:20:25.830049
# Unit test for constructor of class ActionModule
def test_ActionModule():
    mod = ActionModule('some_tmp_path')
    assert mod._shared_loader_obj is not None

# Generated at 2022-06-13 11:20:30.824163
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''Test the constructor of the ActionModule class'''

    action = ActionModule(None, None, None)
    assert action.TRANSFERS_FILES == False

    # Since it is not a dict.get method, we can not rely on the output of the action.run() method
    # in the constructor test case.
    # assert 'failed' in action.run()

# Generated at 2022-06-13 11:20:37.638879
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule(
        task=dict(action=dict(module='yum', args=dict(name='httpd', state='installed'))),
        connection=None,
        play_context=dict(check_mode=False, diff_mode=None),
        loader=None,
        templar=None,
        shared_loader_obj=None
    )
    assert action._connection is None
    assert action._play_context.check_mode is False
    assert action._loader is None
    assert action._templar is None
    assert action._task.action.args['state'] == 'installed'

# Generated at 2022-06-13 11:20:42.847269
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # variables for method run of class ActionModule
    fake_cli_connection_class = FakeCliConnection()
    # create object for class ActionModule
    action_module_obj = ActionModule(fake_cli_connection_class, 'test', {})
    assert action_module_obj is not None
    # call method run of class ActionModule
    result = action_module_obj.run(task_vars={'ansible_pkg_mgr': 'yum'})
    assert result is not None


# Generated at 2022-06-13 11:20:54.308875
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module._load_params()
    action = ActionModule(task, connection, play_context, loader, templar, shared_loader_obj)
    test_result = dict(
        ansible_facts=dict(
            ansible_pkg_mgr="yum4"
        ),
        ansible_job_id="103451504441123",
        changed=False,
        url_password=None,
        url_username=None
    )

    test_result2 = dict(
        ansible_facts=dict(
            ansible_pkg_mgr="auto"
        ),
        ansible_job_id="103451504441123",
        changed=False,
        url_password=None,
        url_username=None
    )

# Generated at 2022-06-13 11:20:57.008911
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert action_module

# Generated at 2022-06-13 11:21:06.024494
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils.common.text.converters import to_text
    from ansible.plugins.loader import action_loader
    import json

    # Necessary test objects
    display = Display()
    display.verbosity = 4
    display._screen_terminal_supports_colors = False
    display.display("TEST: test_ActionModule_run")

    # Setup ActionModule object
    action = action_loader.get('yum_selector', class_only=True)()
    action._connection = FakeConnection(
        constants.DEFAULT_TRANSPORT, '/usr/bin/python')

    # Test - No args
    result = action.run(task_vars={
        'ansible_facts': {},
        'ansible_pkg_mgr': "yum",
        })
   

# Generated at 2022-06-13 11:21:07.180381
# Unit test for constructor of class ActionModule
def test_ActionModule():  # pylint: disable=missing-docstring
    assert ActionModule('module_name', 'args', 'task')

# Generated at 2022-06-13 11:21:14.133282
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import ansible_collections.ansible.legacy.tests.unit.compat.mock as mock
    from ansible.vars.manager import VariableManager

    from ansible.plugins.action.yum import ActionModule as plugin

    mock_loader = mock.Mock()
    mock_loader.action_loader = mock.Mock()
    mock_task = mock.Mock()
    mock_task._role = None
    mock_task._task = mock.Mock()
    mock_task.args = {'use': 'auto'}

    plugin_obj = plugin(mock_task, mock_loader)

    assert plugin_obj.VALID_BACKENDS == frozenset(('yum', 'yum4', 'dnf'))
    assert plugin_obj.TRANSFERS_FILES == False

# Generated at 2022-06-13 11:21:18.560852
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = ActionModule()
    for module in VALID_BACKENDS:
        facts = {"ansible_facts": {'pkg_mgr': module}}
        result = action_module.run(task_vars={'ansible_facts': facts})
        assert module == result['ansible_facts']['pkg_mgr']

# Generated at 2022-06-13 11:21:58.474156
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Mock modules
    import ansible.overrides
    import ansible.plugins.action.normal
    import ansible.plugins.action.yum
    import ansible.plugins.action.yum_dnf
    import ansible.utils.display
    import ansible.module_utils.basic
    import ansible.module_utils.common.collections
    import ansible.module_utils.six
    import ansible.module_utils.urls
    import ansible.module_utils.facts.system.pkg_mgr
    import ansible.module_utils.connection

    # Get test fixtures
    from units.mock.loader import DictDataLoader
    from units.mock.path import mock_unfrackpath_noop

    # Test properties

# Generated at 2022-06-13 11:21:59.758300
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert isinstance(ActionModule(), ActionModule)

# Generated at 2022-06-13 11:22:02.943693
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # This implementation of the unit test method is required
    # because module ActionModule is a base class and the method
    # run of the module cannot be tested without instantiating
    # an object of one of the derived classes.
    pass

# Generated at 2022-06-13 11:22:04.605196
# Unit test for constructor of class ActionModule
def test_ActionModule():
    ''' unit test for constructor of class ActionModule '''
    action = ActionModule(None, None)
    print(action)

# Generated at 2022-06-13 11:22:05.180883
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 11:22:14.291201
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from unittest import mock
    from ansible.plugins.action import ActionBase
    from ansible.playbook.task import Task
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.utils.display import Display

    loader = mock.MagicMock(DataLoader)
    variable_manager = mock.MagicMock(VariableManager)
    inventory = mock.MagicMock(InventoryManager)

# Generated at 2022-06-13 11:22:23.368647
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = ActionModule()
    action_module._task = {}
    action_module._task.args = {'use': 'auto'}
    action_module._task.delegate_to = ''
    action_module._task.delegate_facts = False
    action_module._templar = {}
    # mock up the templar object to return a specific mocked up value
    action_module._templar.template = lambda x: "yum"
    action_module._shared_loader_obj = {}
    action_module._shared_loader_obj.module_loader = {}
    # mock up the module loader object to return a specific mocked up value
    action_module._shared_loader_obj.module_loader.has_plugin = lambda x: True

# Generated at 2022-06-13 11:22:23.929031
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert True

# Generated at 2022-06-13 11:22:33.666854
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    host = '127.0.0.1'
    connection = 'local'

    # Construct module_argv array
    module_argv = ['name', 'state=latest', 'disable_gpg_check=yes']
    module_args = dict()
    for x in module_argv:
        module_key, module_value = x.split('=', 1)
        module_args[module_key] = module_value

    # Construct task object

# Generated at 2022-06-13 11:22:35.653313
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert not ActionModule(dict(), dict(), task_uuid='', connection='')

# Generated at 2022-06-13 11:23:34.778290
# Unit test for constructor of class ActionModule
def test_ActionModule():
    yum_action_module = ActionModule(task=None, connection=None,
                                     play_context=None, loader=None, templar=None, shared_loader_obj=None)

    assert yum_action_module, "Failed to create yum_action_module!"

    # Test that all of the expected module attributes are present
    expect_attrs_present = {"_supports_check_mode", "_supports_async", "TRANSFERS_FILES"}
    assert expect_attrs_present.issubset(dir(yum_action_module))

    # Test that all of the attributes have the expected values
    assert yum_action_module._supports_check_mode is True
    assert yum_action_module._supports_async is True
    assert yum_action_module.TRANSF

# Generated at 2022-06-13 11:23:39.508777
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(
        {'async': 10, 'changed': False, 'invocation': {'module_args': 'args'},
         'module_name': 'yum', 'task_name': 'dnf', 'task_vars': 'vars'}, 'loader', 'templar', 'shared_loader_obj')._task.async_val == 10

# Generated at 2022-06-13 11:23:40.144620
# Unit test for constructor of class ActionModule
def test_ActionModule():
    global display
    display = Display()
    ActionModule()

# Generated at 2022-06-13 11:23:40.792389
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule is not None

# Generated at 2022-06-13 11:23:41.224168
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule()

# Generated at 2022-06-13 11:23:46.753472
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """Unit test method run of class ActionModule"""
    # Mock module arguments

# Generated at 2022-06-13 11:23:57.108262
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    #
    # Mock class ActionModule
    #
    class MockActionModule(ActionModule):
        def __init__(self):
            self._task = MockTask()

    #
    # Mock class MockTask
    #
    class MockTask:
        def __init__(self):
            self.async_val = False
            self.args = {'use': 'auto'}
            self.delegate_to = False
            self.delegate_facts = True
    #
    # Mock class MockConnection
    #
    class MockConnection:
        def __init__(self):
            self._shell = MockShell()

        def get_option(self, option):
            return True

    #
    # Mock class MockShell
    #

# Generated at 2022-06-13 11:24:03.794273
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    task_vars = {
        "ansible_pkg_mgr": "yum"
    }
    task_args = {
        "package": ["python3", "python2"]
    }

    plugin = ActionModule({}, {}, task_vars)

    # simulate loading a template from a task
    plugin._templar.template = lambda text: text
    result = plugin.run(task_args=task_args)

    assert result["module_name"] == "ansible.legacy.yum"
    assert result["module_args"]["package"] == task_args["package"]

# Generated at 2022-06-13 11:24:13.987375
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # make a simple test case
    host = {'hostname': 'hostname.domain.com'}
    task = {'action': {'module': 'yum', 'args': {'name': 'rake', 'state': 'absent'}}}
    connection = {}

    # create an instance of the ActionModule
    action_plugin = ActionModule(task=task, connection=connection, play_context=None, loader=None, templar=None, shared_loader_obj=None)

    # test 'run' method
    with pytest.raises(Exception) as exc_info:
        action_plugin.run(task_vars={})

    exc_info.match("Action plugin failed to find a valid backend module among: '(yum, dnf)'")

# Generated at 2022-06-13 11:24:20.874221
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Tests for class ActionModule
    global YamlDir
    YamlDir = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        'module_utils', 'yum', 'yum3', 'backend.yaml')

    test_module = ActionModule(
        task=None, connection=None, play_context=None, loader=None,
        templar=None, shared_loader_obj=None)

    assert test_module is not None

# Generated at 2022-06-13 11:26:09.062523
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """
    Unit test for ActionModule class. Ensures that attributes are set
    correctly when initializing.
    """
    mock_loader = MockLoader()
    mock_connection = MockConnection()
    action_module = ActionModule(mock_loader, mock_connection, '/path/to/ansible/ansible.cfg')

    assert action_module._shared_loader_obj == mock_loader
    assert action_module._connection == mock_connection
    assert action_module._config.config_file == '/path/to/ansible/ansible.cfg'
    assert action_module._task.async_val == 100
    assert action_module._task.loop is None
    assert action_module._task.loop_args is None
    assert action_module._supports_async is True
    assert action_module._task._role is None




# Generated at 2022-06-13 11:26:13.263433
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Instantiate a module instance
    a = ActionModule("test_test", {}, {}, {}, {}, True)
    # Confirm all sub-objects were instantiated
    assert a.action_name == "test"
    assert 'yum' in VALID_BACKENDS
    assert 'auto' in VALID_BACKENDS

# Generated at 2022-06-13 11:26:16.106687
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module_params = {
        'use': True
    }
    action_module_obj = ActionModule(None, action_module_params, None)
    assert action_module_obj != None

# Generated at 2022-06-13 11:26:20.017152
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(
        task=dict(args=dict(name='vim-enhanced')),
        connection=dict(play_context=dict(check_mode=False)),
        templar=None,
        shared_loader_obj=None)
    assert action_module is not None

# Generated at 2022-06-13 11:26:28.374729
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.six import iteritems
    from ansible.utils.display import Display
    from ansible.utils.vars import combine_vars

    MOD_BACKEND = "ansible.legacy.yum"
    module = ActionModule()

    # set up some mock data
    task_vars = {'ansible_facts': {'pkg_mgr': 'yum'}}

# Generated at 2022-06-13 11:26:29.335291
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_plugin_class = ActionModule()
    return action_plugin_class

# Generated at 2022-06-13 11:26:32.579616
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """
    Unit test for constructor of class ActionModule.
    """
    module = ActionModule(
        task=None,
        connection=None,
        _play_context=None,
        loader=None,
        templar=None,
        shared_loader_obj=None
    )

    assert module is not None

# Generated at 2022-06-13 11:26:33.312485
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # TODO:
    #assert True
    pass

# Generated at 2022-06-13 11:26:36.085488
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module_obj = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert action_module_obj.TRANSFERS_FILES is False

# Generated at 2022-06-13 11:26:43.900243
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import sys
    import io
    import unittest
    import unittest.mock
    import collections

    import ansible.plugins

    class MockVars(dict):
        def __init__(self, *args, **kwargs):
            dict.__init__(self, *args, **kwargs)

        def get(self, key, value=None):
            return dict.get(self, key, value)

        def __getitem__(self, key):
            return dict.get(self, key, None)

    class MockConnection:
        class MockShell:
            def __init__(self):
                self.tmpdir = "/tmp"

        def __init__(self, *args, **kwargs):
            self.shell = self.MockShell()
