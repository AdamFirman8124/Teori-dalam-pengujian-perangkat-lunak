

# Generated at 2022-06-13 09:44:50.643046
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.action import ActionModule
    from ansible.playbook.task import Task

    from ansible.vars.manager import VariableManager
    from ansible.inventory.host import Host
    from ansible.parsing.dataloader import DataLoader
 
    from ansible.template import Templar

    class AnsibleModuleTest(object):
        _ansible_verbosity=1
        def __init__(self):
            pass

    class PlayContext(object):
        def __init__(self):
            self.verbosity=1

    class Task(object):
        def __init__(self):
            self.action = 'debug'
            self.args = dict()

    playground=dict(
        hostvars=dict()
    )

    loader = DataLoader()


# Generated at 2022-06-13 09:45:01.059471
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    from ansible.utils.vars import combine_vars

    loader = DataLoader()
    variable_manager = VariableManager()
    variable_manager.extra_vars = {'var1': 'ansible', 'var2': 'rocks'}
    variable_manager.options_vars = {'global': {'var_a': 'option_a'}}
    variable_manager.constructed_vars['_run_async'] = False

# Generated at 2022-06-13 09:45:04.704973
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Get the test class
    ActionModuleTest = action_loader.get('debug', class_only=True)

    # Create a test action module
    test_module = ActionModuleTest()

    assert test_module != None

# Generated at 2022-06-13 09:45:06.524740
# Unit test for constructor of class ActionModule
def test_ActionModule():
    test_result = ActionModule()
    assert test_result == 'ActionModule'


# Generated at 2022-06-13 09:45:10.969569
# Unit test for constructor of class ActionModule
def test_ActionModule():
    
    actionmodule = ActionModule(1,2,3,4,5,6,7,8)
    assert actionmodule.TRANSFERS_FILES == False
    assert actionmodule._VALID_ARGS == frozenset(('msg', 'var', 'verbosity'))

# Generated at 2022-06-13 09:45:15.874539
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Initializations
    module = ActionModule({'Variable': 'Variable'}, 'Variable')
    # Results
    assert module.run({'Variable': 'Variable'}, {'Variable': 'Variable'}) == {'failed': False}
    assert module.run({'Variable': 'Variable'}, {'Variable': 'Variable'}) == {'_ansible_verbose_always': True, 'failed': False}

# Generated at 2022-06-13 09:45:27.715603
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task import Task
    from ansible.utils.vars import AnsibleVars
    from ansible.utils.display import Display
    from ansible.vars import VariableManager

    display = Display()
    variable_manager = VariableManager()
    task = Task()
    task._role = None
    task.args = dict()
    task.action = "debug"
    task._role_name = None

    result = dict(skipped=False, failed=False)

    am = ActionModule(task, variable_manager, display)
    result.update(am.run(None, AnsibleVars(task.vars, variable_manager)))

    assert result['skipped_reason'] == "Verbosity threshold not met."
    assert result['skipped'] is True
    assert result['failed'] is False

# Generated at 2022-06-13 09:45:32.918265
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module_loader, lookup_loader, path_loader = Mock()
    module_loader.get_all_plugin_loaders.return_value = [
        (module_loader, ActionModule),
    ]
    #initialize ActionModule instance
    action_instance = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    #check whether valid arguments(msg, var and verbosity) are set
    assert action_instance._VALID_ARGS == frozenset(('msg', 'var', 'verbosity'))
    #check whether plugin is not transferring files
    assert action_instance.TRANSFERS_FILES == False


# Generated at 2022-06-13 09:45:43.363057
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    class ActionModuleMock(ActionModule):

        def _execute_module(self, tmp=None, task_vars=None, persist_files=False):
            return dict()

        def _get_diff_data(self, task_vars, source, destination):
            return dict()


    act = ActionModuleMock({})

    # test verbosity threshold is not met
    result = act.run(task_vars = dict(), verbosity = 2)
    assert result['skipped_reason'] == "Verbosity threshold not met."
    assert result['skipped'] == True
    assert result['failed'] == False

    # test verbosity threshold is met
    result = act.run(task_vars = dict(), verbosity = 0)
    assert result['_ansible_verbose_always'] == True
    assert result['failed']

# Generated at 2022-06-13 09:45:45.165189
# Unit test for constructor of class ActionModule
def test_ActionModule():
    class AdhocModule(ActionModule):
        pass

    assert AdhocModule._VALID_ARGS == ('msg', 'var', 'verbosity')

# Generated at 2022-06-13 09:45:59.260680
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import pytest
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins.action import ActionBase
    from ansible.utils.vars import combine_vars

    # Create an ActionModule object
    am = ActionModule({"msg": "Hello World!"}, load_name="debug")
    # Create a PlayContext object
    play_context = PlayContext()
    # Create a TaskExecutor object
    task_executor = TaskExecutor()

    # Setup test environment
    task_executor.add_tqm(None)
    task_executor._task = am
    task_executor._loader = None
    task_executor._shared_loader_obj = None
    task_executor._final_q = None
    task_executor._loop_eval_queue = None
    task_executor

# Generated at 2022-06-13 09:46:04.812334
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import ansible.plugins.action.debug as debug
    # set up the default configurations
    action_mod = debug.ActionModule('action_name', 'task_args', 'module_args')
    # test the action_mod object
    assert isinstance(action_mod, debug.ActionModule)


# Generated at 2022-06-13 09:46:05.514818
# Unit test for constructor of class ActionModule
def test_ActionModule():
  assert(ActionModule)

# Generated at 2022-06-13 09:46:07.337872
# Unit test for constructor of class ActionModule
def test_ActionModule():
	assert True, "Test Action Module"

# Generated at 2022-06-13 09:46:20.351709
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''
    Unit test for method run of class ActionModule.
    '''
    import os
    import sys
    import unittest

    # Mock AnsibleModule to test module
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes
    mock_module = basic.AnsibleModule(argument_spec={})
    # Test AnsibleModule._load_params
    mock_module.params = dict()
    for param in ['msg', 'var', 'verbosity']:
        mock_module.params[param] = mock_module.params
    mock_module.check_mode = False
    mock_module.no_log = False
    mock_module.debug = False
    mock_module.supports_check_mode = True

# Generated at 2022-06-13 09:46:31.951020
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    am = ActionModule()

    # Test verbosity <= display verbosity
    # msg is set and var is not set
    # Check result
    am._display.verbosity = 0
    am._task.args = {'msg': 'Hello world!', 'verbosity': 1}
    assert am.run() == {'failed': False, 'msg': 'Hello world!'}

    # Test verbosity > display verbosity
    # Check skipped reason and skipped
    am._display.verbosity = 2
    am._task.args = {'msg': 'Hello world!', 'verbosity': 1}
    assert am.run() == {'failed': False, 'msg': 'Hello world!', '_ansible_verbose_always': True, 'skipped_reason': 'Verbosity threshold not met.', 'skipped': True}

    # Test verbosity

# Generated at 2022-06-13 09:46:34.953146
# Unit test for constructor of class ActionModule
def test_ActionModule():
	assert ActionModule(1, 2, 3, 4) == None


# Generated at 2022-06-13 09:46:38.048386
# Unit test for constructor of class ActionModule
def test_ActionModule():
    test_action_module = ActionModule()
    assert test_action_module._VALID_ARGS==frozenset(('msg', 'var', 'verbosity'))

# Generated at 2022-06-13 09:46:39.544258
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(None, None)
    assert(module._task.args['verbosity'] == 0)

# Generated at 2022-06-13 09:46:49.567176
# Unit test for constructor of class ActionModule
def test_ActionModule():
    t_module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert t_module._task is None
    assert t_module._connection is None
    assert t_module._play_context is None
    assert t_module._loader is None
    assert t_module._templar is None
    assert t_module._shared_loader_obj is None
    assert t_module._display is not None
    assert t_module._config is not None
    assert t_module._valid_args == frozenset(('msg', 'var', 'verbosity'))
    assert t_module._always_run is False
    assert t_module.transfer_files == False

# Generated at 2022-06-13 09:47:08.128569
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.plugins.action import ActionBase
    from ansible.plugins.action.debug import ActionModule
    from ansible.module_utils.six import string_types
    from ansible.module_utils._text import to_text

    am = ActionModule("test")

    # Test the parameters
    assert am._VALID_ARGS == frozenset(('msg', 'var', 'verbosity')), "The member variable _VALID_ARGS should be equal to 'msg', 'var', 'verbosity'"
    assert am.TRANSFERS_FILES == False, "The member variable TRANSFERS_FILES should be equal to False"

    # test run() method
    assert am.run() == 'abc'
    #assert am.run() == dict()

# Generated at 2022-06-13 09:47:11.708747
# Unit test for constructor of class ActionModule
def test_ActionModule():
    actionmodule = ActionModule(loader=None, task=None, connection=None, play_context=None, loader_type='', templar=None, shared_loader_obj=None)
    assert isinstance(actionmodule, ActionModule)

# Generated at 2022-06-13 09:47:20.645438
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    am = ActionModule(None, None, None, None, None, None, None, None)
    # testcase1: call run with msg
    # set debug module verbosity
    am._display.verbosity = 0
    msg = {'msg': 'Hello world!'}
    assert am.run(None, None) == {'failed': False, 'msg': 'Hello world!'}

    # testcase2: call run with var and verbosity
    msg = {'var': 'myvar', 'verbosity': 2}
    assert am.run(None, {'myvar': 'Hello world'}) == {'failed': False, 'v': 'Hello world', 'verbosity': 2}

    # testcase3: call run with msg and verbosity
    msg = {'msg': 'Hello world!', 'verbosity': 2}

# Generated at 2022-06-13 09:47:30.342755
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    mock_self = lambda: None
    mock_self.file_args = None
    mock_self.module = None
    mock_self.method_name = None
    mock_self.module_name = None
    mock_self.module_args = None
    mock_self._handle_warnings = lambda *args: None
    
    mock_self._load_params = lambda: None
    mock_self._task = lambda: None
    mock_self._task.args = {u'verbosity': None}
    mock_self._task.action = u'debug'
    mock_self._connection = lambda: None
    mock_self._play_context = lambda: None
    mock_self._play_context.become = None
    mock_self._play_context.become_user = None

# Generated at 2022-06-13 09:47:40.233696
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # create a configuration for the module and populate the fields
    config = dict(one=1, two=2, three=3, ansible_verbosity=3)
    config['ANSIBLE_MODULE_ARGS'] = dict(msg='Hello world!', verbosity=1, _ansible_check_mode=False, _ansible_debug=False, _ansible_diff=False)
    config['ansible_version'] = dict(full='2.3.0.0')
    config['playbook_dir'] = '/etc/ansible/roles'
    config['checkmode'] = False
    config['debug'] = False
    config['diff'] = False
    config['no_log'] = False
    config['verbosity'] = 3

# Generated at 2022-06-13 09:47:43.149920
# Unit test for constructor of class ActionModule
def test_ActionModule():
    result = ActionModule(None, None, None, None, None).run(None, None)
    print(result)

# Generated at 2022-06-13 09:47:56.182370
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Get the object
    action_module_obj = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert action_module_obj._task is None
    assert action_module_obj.TRANSFERS_FILES is False
    assert action_module_obj.VALID_ARGS == frozenset(('msg', 'var', 'verbosity'))
    assert action_module_obj._connection is None
    assert action_module_obj._play_context is None
    assert action_module_obj._loader is None
    assert action_module_obj._templar is None
    assert action_module_obj._shared_loader_obj is None

# Generated at 2022-06-13 09:48:01.371109
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module_cls = ActionModule
    action = module_cls()
    # test valid args
    for args in [{'msg': 'Hello world!'}, {'var': 'myvar'}]:
        assert action.args == args
        assert action.run() == {'failed': False, 'msg': 'Hello world!'}
    # test invalid args
    action.args = {'msg': 'Hello world!', 'var': 'myvar'}
    assert action.run()['msg'] == "'msg' and 'var' are incompatible options"

# Generated at 2022-06-13 09:48:04.975935
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert isinstance(ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None), ActionModule)

# Generated at 2022-06-13 09:48:11.933728
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.module_utils.six import PY3
    from ansible.module_utils.six.moves import builtins
    from ansible.module_utils.six.moves.xmlrpc_client import ServerProxy
    from ansible import context
    import ansible.executor.task_queue_manager
    import ansible.playbook.play
    import ansible.playbook.task
    import ansible.playbook.block
    import ansible.playbook.role
    import ansible.utils.sentinel
    import ansible.vars
    import ansible.utils.display
    # Unit test do not need to support random feature
    import ansible.plugins.action.debug

    context._init_global_context(cli_args=None)
    display = ansible.utils.display.Display()
    fake_options

# Generated at 2022-06-13 09:48:32.490985
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 09:48:41.947677
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins import action
    # Test with no msg and no var args
    m = action.ActionModule(None, dict(msg=None, var=None), None)
    result = m.run(task_vars=dict(var1=1))
    # assert result, expect msg is Hello world!, and no failure
    assert result['msg'] == 'Hello world!' and result['failed'] == False

    # Test with msg and var args, expect exception
    m = action.ActionModule(None, dict(msg='msg', var='var'), None)
    result = m.run(task_vars=dict(var1=1))
    # assert result, expect error msg and failure
    assert result['failed'] == True and result['msg'] == "'msg' and 'var' are incompatible options"

    # Test with msg arg only, expect success

# Generated at 2022-06-13 09:48:51.218778
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # define test variables
    hostname = "www.ansible.com"
    task_vars = dict()
    result = dict()
    test_args = {'msg': 'Hello world!', 'verbosity': 1}

    # instantiate and set ansible options
    class ActionModule(ActionModule):
        def __init__(self):
            self._task = task
            self._connection = connection
            self._display = display
            self._loader = loader

    # instantiate action module
    action_module = ActionModule()

    # invoke test method
    action_module.run(result, task_vars)

    # assert result
    assert result == {'failed': False, 'msg': 'Hello world!', '_ansible_verbose_always': True}

# Generated at 2022-06-13 09:48:52.005221
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert True

# Generated at 2022-06-13 09:48:59.035704
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule(None, None, None)                                        # TODO
    result = module.run()
    assert result['msg'] == 'Hello world!'                                            # TODO

"""
Sample YAML
- action: debug
  msg: "System {{ inventory_hostname }} has uuid {{ ansible_product_uuid }}"
  verbosity: 1
"""

# Generated at 2022-06-13 09:49:03.473331
# Unit test for constructor of class ActionModule
def test_ActionModule(): 
    module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert module._valid_args == ActionModule._VALID_ARGS

# Generated at 2022-06-13 09:49:10.324515
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import sys
    import os
    import json
    import pytest
    import collections
    import ansible.plugins.action
    import ansible.utils.plugin_docs
    import ansible.utils.module_docs
    import ansible.inventory.host
    import ansible.playbook.task
    import ansible.vars.manager
    import ansible.template.template
    import ansible.parsing.dataloader

    if sys.version_info < (2, 7):
        pytest.skip("The unittests require python >= 2.7")

    if not os.path.isdir(os.path.join(os.path.dirname(__file__), '..', 'data')):
        pytest.skip("the data directory does not exist")


# Generated at 2022-06-13 09:49:21.557959
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins import action as ActionModule
    module_name = __name__ + '.test_ActionModule_run'
    am = ActionModule(module_name, dict())
    assert am.run() == dict(msg='Hello world!', failed=False, _ansible_verbose_always=True)
    assert am.run(task_vars=dict(test_var='test_value')) == dict(test_value='test_value', failed=False, _ansible_verbose_always=True)
    assert am.run(task_vars=dict(test_var=dict(sub_key='sub_value'))) == dict(dict='sub_value', failed=False, _ansible_verbose_always=True)

# Generated at 2022-06-13 09:49:22.125123
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert True

# Generated at 2022-06-13 09:49:26.557359
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Create a mock task, args and action_module
    task = MockTask()
    task._task.args = {'msg': 'Hello world!'}
    action_module = MockActionModule()

    # Run the test
    result = action_module.run(task_vars=dict(), task=task)

    # Assert result for test
    assert result == {
        '_ansible_verbose_always': True,
        'msg': 'Hello world!',
        'failed': False
    }


# Generated at 2022-06-13 09:50:11.684633
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''
    Unit test for constructor of class ActionModule
    '''
    action_module = ActionModule("msg", "var")
    assert action_module

# Generated at 2022-06-13 09:50:24.505052
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # One test case has been provided to you.
    # Write additional test cases to test different functionality of the run method.
    actionModule = ActionModule(
        task={'args': {'msg': "Hello World!"}},
        connection=None,
        play_context=None,
        loader=None,
        templar=None,
        shared_loader_obj=None
    )

    expected = {
        'failed': False,
        'msg': "Hello World!",
        '_ansible_verbose_always': True
    }

    result = actionModule.run(tmp=None, task_vars=None)
    assert expected==result, "Expected: \n%s, Actual: \n%s" % (expected, result)

    # Add additional test cases here.
    # actionModule = ActionModule(
    #

# Generated at 2022-06-13 09:50:37.872110
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import ansible
    from ansible.plugins.action import ActionModule
    from ansible.playbook.play import Play

    # construct the object
    fake_loader = DictDataLoader({})
    fake_inventory = Inventory(loader=fake_loader, variable_manager=VariableManager(), host_list=[])

    fake_play = Play().load({"hosts": 'host', "gather_facts": "no", "tasks": [{"action": {"module": "debug", "args": {}}}]}, variable_manager=fake_inventory.get_variable_manager(), loader=fake_loader)
    t = Task().load(fake_play.get_tasks()[0], variable_manager=fake_inventory.get_variable_manager(), loader=fake_loader)
    tqm = None

    am = ActionModule(t, tqm)

# Generated at 2022-06-13 09:50:41.133891
# Unit test for constructor of class ActionModule
def test_ActionModule():
    m = ActionModule(None, None, None, None, None)
    assert m.TRANSFERS_FILES == False
    assert m._VALID_ARGS == frozenset(('msg', 'var', 'verbosity'))

# Generated at 2022-06-13 09:50:42.828506
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule()
    print(action_module)
    assert action_module != None

# Generated at 2022-06-13 09:50:53.362980
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # import python library modules
    import os
    import tempfile
    import shutil
    import traceback
    import types
    import json

    test_path = os.path.dirname(os.path.realpath(__file__))
    test_root = os.path.join(test_path, "testing_action_plugin")

    # Create temporary directory to stage testing directories
    test_dir = tempfile.mkdtemp(dir=test_root)
    os.rmdir(test_dir)
    print("Created testing_action_plugin at: " + test_dir)

    # Create 'hello_world' directory and copy in testing assets
    hello_dir = os.path.join(test_dir, "hello_world")
    tasks_dir = os.path.join(hello_dir, 'tasks')
    vars

# Generated at 2022-06-13 09:50:54.465178
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(None, None, None)
    assert isinstance(module, object)

# Generated at 2022-06-13 09:51:02.327679
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Create instance of class ActionModule
    actionModule = ActionModule('setup', '', '', '', '', '', '', '', '')
    # Check instance attributes
    assert isinstance(actionModule._VALID_ARGS, frozenset)
    assert actionModule._VALID_ARGS == frozenset(('msg', 'var', 'verbosity'))
    assert actionModule.TRANSFERS_FILES == False

# Generated at 2022-06-13 09:51:09.644078
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """Test to make sure that run method is working as expected"""

    # Create a mock object for display
    display = MockDisplay()

    # Create a fake task
    task = MockTask()
    task.args = {'msg': 'Hello Test World!', 'var': 'Hello Test World!', 'verbosity': 2}

    # Create a mock object for connection
    connection = MockConnection('localhost')

    # Create a mock object for options
    options = MockOptions()

    # Create a mock object for Ansible module
    ansible = MockAnsibleModule()

    # Create a mock object for AnsibleFile class
    ansible_file = MockAnsibleFile()

    # Create a mock object for AnsibleModule class
    ansible_module = MockAnsibleModuleClass()

    # Create a mock object for ActionBase class
    action = MockAction

# Generated at 2022-06-13 09:51:15.962381
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.utils.display import Display

    data = {'hostvars': {}}
    variable_manager = VariableManager()
    variable_manager.extra_vars = {'test_extra_vars': 'test_extra_vars', 'test_hostvars': 'test_hostvars'}
    variable_manager.set_inventory(InventoryManager(loader=None, sources=None))

    task = Task()
    task.action = "debug"
    task.args = {'msg': 'Hello world!', 'verbosity': 1}

    play_context = PlayContext()

# Generated at 2022-06-13 09:53:15.678162
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True


# Generated at 2022-06-13 09:53:22.176528
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(
            task=dict(action=dict(module='debug', args=dict())),
            connection=None,
            play_context=dict(check_mode=True, diff=True),
            loader=None,
            templar=None,
            shared_loader_obj=None
    )

    assert isinstance(module, ActionModule)

# Generated at 2022-06-13 09:53:22.967081
# Unit test for constructor of class ActionModule
def test_ActionModule():
    ActionModule()

# Generated at 2022-06-13 09:53:28.316610
# Unit test for constructor of class ActionModule
def test_ActionModule():
    mock_loader = None
    mock_path_params = {}
    mock_task_vars = {'foo': 'bar', 'bat': 'baz'}
    mock_task_name = 'irrelevant'
    mock_task_args = {'msg': 'Hello Ansible!'}

    # construct the class and test for name, args, and task_vars
    action_module = ActionModule(mock_loader, mock_path_params, mock_task_vars)
    assert action_module._name == 'debug'
    assert action_module.DEFAULT_VERBOSITY == 2
    assert action_module._task_vars == mock_task_vars


# Generated at 2022-06-13 09:53:36.862934
# Unit test for method run of class ActionModule

# Generated at 2022-06-13 09:53:37.763113
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule.__name__ == "ActionModule"

# Generated at 2022-06-13 09:53:49.072462
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Setup mock objects
    args_msg = {"msg": "This is a message"}
    args_msg_verbose = {"msg": "This is a message", "verbosity": 2}
    args_var = {"var": "ff"}
    args_var_verbose = {"var": "ff", "verbosity": 2}
    args_var_list_verbose = {"var": ["ff", "gg"], "verbosity": 2}
    args_var_dict_verbose = {"var": {"ff": "gg"}, "verbosity": 2}
    args_msg_var_verbose = {"msg": "This is a message", "var": "ff", "verbosity": 2}
    args_incompatible = {"msg": "This is a message", "var": "ff"}
    task_vars = dict()

    # Create mock objects


# Generated at 2022-06-13 09:53:54.172262
# Unit test for method run of class ActionModule
def test_ActionModule_run():

  # Example of a simple unit test
  action_module = ActionModule(load_params=False)
  result = action_module.run(tmp='/tmp', task_vars=dict())

  assert result['failed'] == False

  # Example of a simple unit test
  action_module = ActionModule(load_params=True, args={'msg': 'Hello', 'verbosity':0})
  result = action_module.run(tmp='/tmp', task_vars=dict())

  assert result['failed'] == False
  assert result['msg'] == 'Hello'

  # Example of a simple unit test
  action_module = ActionModule(load_params=True, args={'var': 'name', 'verbosity':0})

# Generated at 2022-06-13 09:53:57.059161
# Unit test for constructor of class ActionModule
def test_ActionModule():
    actionmodule = ActionModule()
    assert actionmodule is not None

# Generated at 2022-06-13 09:54:08.129386
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Test with string
    test = ActionModule()
    test.run(tmp="test", task_vars={"test": "test"})
    test.run(tmp="test", task_vars={"test": 2})
    test.run(tmp="test", task_vars={"test": 2.5})
    test.run(tmp="test", task_vars={"test": False})
    test.run(tmp="test", task_vars={"test": [1, 2]})
    test.run(tmp="test", task_vars={"test": (1, 2)})
    test.run(tmp="test", task_vars={"test": {"test": "test"}})
    test.run(tmp="test", task_vars={"test": {"test": 2}})
    test.run