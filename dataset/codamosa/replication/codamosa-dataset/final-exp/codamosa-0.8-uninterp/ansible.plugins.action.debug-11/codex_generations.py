

# Generated at 2022-06-13 09:44:45.143254
# Unit test for constructor of class ActionModule
def test_ActionModule():
    instance = ActionModule()
    # The following will fail if new attributes are added to the class
    assert len(instance.__dict__) == 4

# Generated at 2022-06-13 09:44:45.789113
# Unit test for constructor of class ActionModule
def test_ActionModule():
    pass

# Generated at 2022-06-13 09:44:53.239805
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible import context
    from ansible.module_utils.common.text.converters import to_bytes
    from ansible.playbook import Play

    task_vars = {
        'cwd': '/home/bob',
        'home': '/home/bob',
        'inventory_dir': '/home/bob'
    }
    
    action_module = ActionModule(action_module='debug',
                                 task=Play().load(dict(name='test',
                                                       action=dict(msg='Test message',
                                                                   verbosity=5))),
                                 connection=None,
                                 play_context=context.CLIARGS._store,
                                 loader=None,
                                 templar=None,
                                 shared_loader_obj=None)
    
    result = action_module

# Generated at 2022-06-13 09:45:00.574734
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Check instance creation
    assert ActionModule(task=dict(args=dict(msg='Hello World')))

    # Check invalid args and their handling
    assert ActionModule(task=dict(args=dict(msg='Hello World', invalid_arg=5)))

    # Check valid args
    assert ActionModule(task=dict(args=dict(var='Hello World')))
    assert ActionModule(task=dict(args=dict(verbosity=5)))

    # Check error msg when both args are provided
    assert ActionModule(task=dict(args=dict(msg='Hello World', var='Hello World')))

# Generated at 2022-06-13 09:45:05.709522
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(
            task=dict(action=dict(module='debug'),
                args=dict(msg='Hello world!')),
            connection=None,
            play_context=None,
            loader=None,
            templar=None,
            shared_loader_obj=None)
    assert module.run()['msg'] == 'Hello world!'

# Generated at 2022-06-13 09:45:08.692936
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import ansible.plugins.action.debug
    debugAction = ansible.plugins.action.debug.ActionModule(2, 3, 4, 5, 6)
    assert debugAction is not None

# Generated at 2022-06-13 09:45:17.812632
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    
    # Mock modules
    ansible.module_utils.basic.AnsibleModule = mock.Mock()
    ansible.module_utils.six = mock.Mock()

    # Define class ActionModule
    class ActionModule(ansible.plugins.action.ActionModule):
        TRANSFERS_FILES = False
        _VALID_ARGS = frozenset(('msg', 'var', 'verbosity'))

    # Create an instance of class ActionModule
    _test_ActionModule = ActionModule(
        task=dict(action=dict()),
        connection=dict(),
        play_context=ansible.playbook.play_context.PlayContext(),
        loader=None,
        templar=ansible.parsing.dataloader.DataLoader(),
        shared_loader_obj=None
    )

   

# Generated at 2022-06-13 09:45:24.972137
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    args = dict(msg="test_data_01")
    obj = ActionModule(dict(task=dict(args=args)), dict())
    result = obj.run(tmp=None, task_vars=dict())
    assert result['failed'] == False
    assert result['msg'] == "test_data_01"
    assert result['skipped'] == False

if __name__ == '__main__':
    import pytest
    pytest.main([__file__])

# Generated at 2022-06-13 09:45:26.018058
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert True

# Generated at 2022-06-13 09:45:35.986915
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.compat.tests import unittest
    from ansible.compat.tests.mock import patch, Mock
    from ansible.module_utils.basic import AnsibleModule

    class TestActionModule(ActionModule):
        def run(self, tmp=None, task_vars=None):
            return super(ActionModule, self).run(tmp, task_vars)

    class TestAnsibleModule(AnsibleModule):
        def __init__(self, *args, **kwargs):
            kwargs['argument_spec'] = dict(
                msg=dict(type='str', default=''),
                var=dict(type='list', default=''),
                verbosity=dict(type='int', default=0),
            )

# Generated at 2022-06-13 09:45:49.580802
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils.basic import AnsibleModule
    import sys
    import io

    module = AnsibleModule(argument_spec = dict(
            var = dict(),
            verbosity = dict(default=0)
        ),
        supports_check_mode=False
    )

    # Set up the mock display object
    mocked_display = None
    if sys.version_info < (2, 7):
        import mock
        mocked_display = mock.Mock()
        mocked_display.__class__.verbosity = 1
    else:
        import unittest.mock as mock
        mocked_display = mock.Mock()
        mocked_display.verbosity = 1

    # Set up the mock templar object
    mocked_templar = None

# Generated at 2022-06-13 09:45:51.788464
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # TODO: Add test to check variable printing behaviour
    pass

# Generated at 2022-06-13 09:45:55.565966
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """
    ActionModule creates a new instance by calling the constructor
    """
    action = ActionModule(None, None, None, None)
    assert type(action) is ActionModule
    assert action.TRANSFERS_FILES is False


# Generated at 2022-06-13 09:46:04.903177
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from io import StringIO


# Generated at 2022-06-13 09:46:07.151942
# Unit test for constructor of class ActionModule
def test_ActionModule():
      action = ActionModule('test', 'test', {})
      assert action is not None

# Generated at 2022-06-13 09:46:10.815161
# Unit test for constructor of class ActionModule
def test_ActionModule():
    a = ActionModule()
    assert a.run() == {'failed': False, '_ansible_verbose_always': True, 'msg': 'Hello world!'}

# Generated at 2022-06-13 09:46:12.090200
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule('message', dict())

# Generated at 2022-06-13 09:46:19.591498
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Just to avoid "print" to stdout
    class FakeDisplay():
        @property
        def verbosity(self):
            return 0

    # Initialize
    mock = ActionModule()
    mock._display = FakeDisplay()
    mock._task.args = {'msg': 'Hi there'}

    # Run the code to be tested
    result = mock.run()

    # Assertions
    assert result['msg'] == 'Hi there'

# Generated at 2022-06-13 09:46:24.126139
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(load_module_spec(None, 'ansible.plugins.action.debug', _ANSIBLE_ACTION_PLUGINS), task=dict(action=dict()), connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert action_module is not None

# Generated at 2022-06-13 09:46:26.834453
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(None,None)
    assert module is not None
    assert not module.TRANSFERS_FILES

# Generated at 2022-06-13 09:46:41.662352
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible import constants as C
    C.HOST_KEY_CHECKING = False
    C.DEFAULT_DEBUG = False
    C.DEFAULT_VERBOSITY = 0
    C.DEFAULT_SUDO = False
    C.DEFAULT_SU = False
    C.DEFAULT_KEEP_REMOTE_FILES = False
    am = ActionModule(None, None)
    assert isinstance(am, ActionModule)



# Generated at 2022-06-13 09:46:52.348409
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Variables needed for testing
    from ansible.module_utils.basic import AnsibleModule, ModuleDeprecationWarning
    from ansible.utils.path import unfrackpath
    from ansible.modules.extras._text import to_text

    # Create mock AnsibleModule
    old_module = AnsibleModule
    AnsibleModule = lambda *args, **kwargs: old_module(*args, **kwargs)
    AnsibleModule._module_name = 'debug'
    del(old_module)

    # Create mock ActionBase
    class ActionBaseMock:
        def __init__(self, *args, **kwargs):
            pass
        def _exception(self, *args, **kwargs):
            raise Exception()
        def run(self, *args, **kwargs):
            return True

    # Create mock Ansible

# Generated at 2022-06-13 09:46:54.186840
# Unit test for constructor of class ActionModule
def test_ActionModule():
    t = dict()
    am = ActionModule(task=t)
    assert isinstance(am, ActionBase)

# Generated at 2022-06-13 09:47:05.624232
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import inspect
    import json
    import sys
    import os
    import unittest
    import ansible.plugins

    class TestActionModule(unittest.TestCase):
        def setUp(self):
            self.amodule = ansible.plugins.action.debug.ActionModule(
                task=dict(action=dict(module_name='debug', module_args={})),
                connection=None,
                play_context=None,
                loader=None,
                templar=None,
                shared_loader_obj=None)

        def test_argspec(self):
            ''' check if the argspec is correct '''
            # self.assertEqual(inspect.getargspec(ActionModule), (['self', 'task', 'connection', 'play_context', 'loader', 'templar', 'shared_loader

# Generated at 2022-06-13 09:47:07.466189
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule(1,2,3)
    assert am._task == 1

# Generated at 2022-06-13 09:47:17.945281
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    test_task = AnsibleTask("debug:")
    result = test_task.run()
    assert result.get("_ansible_verbose_always") == True
    assert result.get("failed") == False

    test_task = AnsibleTask("debug:", {"verbosity": 1})
    result = test_task.run()
    assert result.get("_ansible_verbose_always") == True
    assert result.get("failed") == False
    assert result.get("msg") == 'Hello world!'

    test_task = AnsibleTask("debug:", {"verbosity": 2})
    result = test_task.run()
    assert result.get("failed") == False
    assert result.get("skipped_reason") == "Verbosity threshold not met."
    assert result.get("skipped") == True

    test

# Generated at 2022-06-13 09:47:25.524450
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager

    mock_loader = Mock()
    mock_loader.path_dwim = Mock(return_value='/')

    args = {'msg': 'Hello world'}
    task = Mock()
    task.args = args
    play_context = PlayContext()
    tqm = TaskQueueManager(Mock(), Mock(), play_context)
    ac = ActionModule(task, play_context, tqm._loader, tqm.shared_loader_obj, None)
    ac.run(Mock(), Mock())

    args = {'var': 'myvar'}
    task.args = args
    ac.run(Mock(), Mock())

# Generated at 2022-06-13 09:47:27.212732
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule()
    for module_name in action_module._VALID_ARGS:
        assert module_name in action_module._task.args
        assert not module_name in action_module._task.args_template

# Generated at 2022-06-13 09:47:27.786004
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 09:47:36.398714
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task import Task
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.inventory.host import Host

    task_source = dict(
        name = "Test",
        action = dict(module='debug'),
        args = dict(msg="Running a test")
    )
    task = Task.load(task_source)

    loader = DataLoader()
    host = Host()
    inventory = InventoryManager(loader=loader, sources=None)
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    result = dict()


# Generated at 2022-06-13 09:48:04.998790
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # create a instance of class ActionModule()
    act = ActionModule()

    # create a dict, this is a dict of all variables which
    # Ansible has at its disposal
    task_vars = dict()

    # create a dict, this is a dict of all arguments which
    # Ansible has at its disposal
    args = dict()

    # set values in args dict
    args['verbosity'] = 0

    # set values in task_vars dict
    task_vars['test_var_1'] = 'test_var_1'
    task_vars['test_var_2'] = 'test_var_2'

    # test for assert condition
    # assertTrue() takes two parameters, true/false and failure message

# Generated at 2022-06-13 09:48:15.722032
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import sys
    import os
    #import socket
    pwd = os.path.dirname(os.path.abspath(__file__))
    module_path = os.path.join(pwd, '../../')
    sys.path.insert(0, module_path)

    from ansible.plugins.action import ActionModule
    #from ansible.compat import six

    try:
        from __main__ import display
    except ImportError:
        from ansible.utils.display import Display
        display = Display()

    from ansible.plugins.loader import action_loader
    plugin_loader = action_loader.get("debug", class_only=True)


    #data = {"a" : {"b":"c"}}
    #a = six.binary_type(json.dumps(data, indent=0))


# Generated at 2022-06-13 09:48:16.732636
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule()

# Generated at 2022-06-13 09:48:22.774715
# Unit test for constructor of class ActionModule
def test_ActionModule():
  am = ActionModule(None, None, {})
  assert am._VALID_ARGS == ('msg', 'var', 'verbosity'), "Expected _VALID_ARGS to be ('msg', 'var', 'verbosity')"
  assert am._task is None and am._loader is None and am._templar is None, \
    "Expected _task, _loader and _templar to be None"


# Generated at 2022-06-13 09:48:26.372371
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """
    Make sure constructor of ActionModule works and all the methods are accessible
    """
    assert_success = False
    try:
        assert_success = True
        am = ActionModule()
    except:
        assert (False)

    if assert_success:
        assert (True)

# Generated at 2022-06-13 09:48:34.423487
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''
    Run simple unit tests for the constructor of class ActionModule
    '''
    import ansible.plugins.action
    import ansible.utils
    import ansible.utils.template

    fake_loader = ansible.utils.plugins.PluginLoader(
        'action',
        'ansible.plugins.action',
        'ActionModule',
        'debug'
    )
    fake_play_context = ansible.playbook.play_context.PlayContext()
    fake_task = ansible.playbook.task.Task()
    fake_task.args = dict()
    fake_action_base = ansible.plugins.action.ActionBase(
        fake_loader,
        fake_play_context,
        fake_task,
        None,
        None
    )
    templar = ansible.utils.template.Tem

# Generated at 2022-06-13 09:48:38.279904
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    module = ActionModule()
    module._task = dict(args = dict())

    module.run(task_vars = dict())
    assert(module._result['msg'] == 'Hello world!')
    assert(module._result['failed'] == False)
    assert(module._result['changed'] == False)



# Generated at 2022-06-13 09:48:46.081946
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    import unittest
    import sys
    import tempfile
    from ansible.plugins.action import ActionBase
    from ansible.executor.task_result import TaskResult
    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.playbook.block import Block
    from ansible.playbook.role import Role
    from ansible.playbook.task_include import TaskInclude
    from ansible.utils.display import Display
    import ansible.constants as C
    import io

    class MockTask(TaskResult):

        def __init__(self, args):
            self._task = Task()
            self._task.args = args


# Generated at 2022-06-13 09:48:48.634476
# Unit test for constructor of class ActionModule
def test_ActionModule():
    ans_obj = AnsibleModule()

    act_obj = ActionModule(ans_obj, {})
    assert act_obj._task.action == 'debug'

# Generated at 2022-06-13 09:49:00.372734
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    #Test for valid arguments
    task = {'args': {'var': 'myvar'}}
    task_vars = {'myvar': 10}
    am = ActionModule(task, dummy_connection(), '/', None, None)
    assert not am.run(task_vars=task_vars)['failed']

    task = {'args': {'msg': 'Hello world!', 'var': 'myvar'}}
    task_vars = {}
    am = ActionModule(task, dummy_connection(), '/', None, None)
    assert am.run(task_vars=task_vars)['failed']

    #Test for invalid argument
    task = {'args': {'msg': 'Hello world!', 'var': 'myvar', 'myarg': 'myval'}}
    task_vars = {}
   

# Generated at 2022-06-13 09:49:50.320905
# Unit test for constructor of class ActionModule
def test_ActionModule():
    global_vars = dict()
    loader = dict()
    hostvars = dict()
    empty_var = dict()
    task_vars = dict()

    my_actionmodule = ActionModule(None, dict(), False, loader, global_vars, hostvars, empty_var, task_vars)

    # Test init of ActionModule
    assert my_actionmodule._VALID_ARGS == frozenset(('msg', 'var', 'verbosity'))
    assert my_actionmodule.TRANSFERS_FILES == False
    assert my_actionmodule._task.action == 'debug'


# This unit test is tested with python test/unit/plugins/action/test_debug.py

# Generated at 2022-06-13 09:49:54.767349
# Unit test for constructor of class ActionModule
def test_ActionModule():
    try:
        am = ActionModule()
        print("Result: Passed")
    except Exception as e:
        print("Result: Failed")
        print("Error: " + str(e))

# Execute the unit test if this file is called as a standalone program.
if __name__ == '__main__':
    test_ActionModule()

# Generated at 2022-06-13 09:49:56.006361
# Unit test for constructor of class ActionModule
def test_ActionModule():
    http = ActionModule()  # check that this does not raise an exception

# Generated at 2022-06-13 09:49:59.949533
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """
    Test to create instance of class ActionModule
    """
    action_module = ActionModule(connection=None, runner_queue=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert action_module is not None

# Generated at 2022-06-13 09:50:07.173233
# Unit test for constructor of class ActionModule
def test_ActionModule():
  am = ActionModule()
  am._task = {
    "action": {
      "__ansible_module__": "debug",
      "__ansible_arguments__": {
        "msg": "Hello world!"
      },
      "__ansible_module_name__": "debug"
    }
  }
  am._templar = 'templar'

# Generated at 2022-06-13 09:50:08.406140
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(None, None, None)

# Generated at 2022-06-13 09:50:20.997031
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task import Task
    from ansible.playbook.role_include import IncludeRole
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.playbook import Playbook

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, sources=['local,'])
    variable_manager.set_inventory(inventory=inventory)
    loader.set_basedir("./test/unit/modules/")

# Generated at 2022-06-13 09:50:32.028875
# Unit test for constructor of class ActionModule
def test_ActionModule():
    sample_task_vars = {'abcdef': 'abcdef'}
    sample_task = {'args': {'msg': 'hello world'}}
    sample_connection = {}
    sample_loader = {}
    sample_templar = {}
    sample_shared_loader_obj = {}
    sample_play_context = {}
    sample_new_stdout = False
    sample_display = {}
    action_module = ActionModule(sample_connection, sample_play_context, sample_loader, sample_templar, sample_shared_loader_obj, sample_display)
    assert action_module is not None
    result = action_module.run(task_vars=sample_task_vars, task_ds=sample_task)
    assert result is not None
    assert result['msg'] == 'hello world'

# Generated at 2022-06-13 09:50:34.263975
# Unit test for constructor of class ActionModule
def test_ActionModule():
    data = {"msg":"test", "var":"foo", "verbosity":"2"}
    ActionModule(None, data)

# Generated at 2022-06-13 09:50:34.963410
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 09:52:22.090309
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert isinstance(ActionBase(), ActionBase)

# Generated at 2022-06-13 09:52:27.276688
# Unit test for constructor of class ActionModule
def test_ActionModule():
    testArgs = {}
    a = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert a._VALID_ARGS == frozenset(('msg', 'var', 'verbosity'))
    assert a.TRANSFERS_FILES == False


# Generated at 2022-06-13 09:52:27.829183
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 09:52:30.475880
# Unit test for constructor of class ActionModule
def test_ActionModule():
    try:
        assert ActionModule._VALID_ARGS == frozenset(('msg', 'var', 'verbosity'))
    except AssertionError as e:
        print(e)
        raise AssertionError

# Generated at 2022-06-13 09:52:37.848463
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Test with valid agruments and verbosity greater than 0
    _task = {}
    _task['args'] = {}
    _task['args']['msg'] = "Hello world!"
    _task['args']['verbosity'] = 2
    _task['args']['_ansible_check_mode'] = False
    _display = Display()
    _display.verbosity = 2
    _templar = Templar(loader=None, variables=None)

    action_module_obj = ActionModule()
    action_module_obj.__dict__['_task'] = _task
    action_module_obj.__dict__['_display'] = _display
    action_module_obj.__dict__['_templar'] = _templar

    expected_result = {}

# Generated at 2022-06-13 09:52:47.755612
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """Constructor of class ActionModule"""

    # Create an instance of class ActionModule
    action_module = ActionModule(
        task=dict(args=dict(), async_val=1, async_jid=1),
        connection=dict(host='localhost'),
        play_context=dict(),
        loader=None,
        templar=None,
        shared_loader_obj=None)

    # Assert that isinstance(action_module._task.args, dict)
    assert isinstance(action_module._task.args, dict)
    # Assert that action_module._task.args == {}
    assert action_module._task.args == {}
    # Assert that action_module._task.async_val == 1
    assert action_module._task.async_val == 1
    # Assert that action_module._task

# Generated at 2022-06-13 09:52:50.995596
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # This is a hack so that unittest can test the constructor
    # directly.  The constructor is an abstractmethod
    from ansible.plugins.action.debug import ActionModule
    assert ActionModule("args")

# Generated at 2022-06-13 09:52:55.147220
# Unit test for constructor of class ActionModule
def test_ActionModule():

    '''Unit test for constructor of class ActionModule'''

    mod = ActionModule()

    assert mod._VALID_ARGS == frozenset(('msg', 'var', 'verbosity'))
    assert mod.TRANSFERS_FILES == False

# Generated at 2022-06-13 09:53:09.155206
# Unit test for constructor of class ActionModule
def test_ActionModule():
    class AnsibleModule(object):
        def __init__(self, argument_spec, bypass_checks=False, no_log=False,
                     check_invalid_arguments=None, mutually_exclusive=None,
                     required_together=None, required_one_of=None, add_file_common_args=False,
                     supports_check_mode=False):
            self.argument_spec = argument_spec
            self.bypass_checks = bypass_checks
            self.no_log = no_log
            self.check_invalid_arguments = check_invalid_arguments
            self.mutually_exclusive = mutually_exclusive
            self.required_together = required_together
            self.required_one_of = required_one_of
            self.add_file_common_args = add_file_common_args
           

# Generated at 2022-06-13 09:53:17.266006
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Define variables to mock

    class Class(object):
        name = 'mock_name'
        tags = list()
    class_obj = Class()

    class ModuleResult(object):
        def __init__(self):
            self.__dict__['_ansible_verbose_always'] = True
            self.__dict__['failed'] = False
            self.__dict__['skipped'] = True
            self.__dict__['skipped_reason'] = 'Verbosity threshold not met'
            self.__dict__['msg'] = 'Hello world!'

    class Task(object):
        def __init__(self):
            self.__dict__['_ansible_no_log'] = False
            self.__dict__['_ansible_verbosity'] = 0