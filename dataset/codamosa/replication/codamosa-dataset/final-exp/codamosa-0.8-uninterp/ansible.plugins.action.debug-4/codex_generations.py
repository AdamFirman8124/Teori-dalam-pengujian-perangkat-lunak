

# Generated at 2022-06-13 09:44:49.695554
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Create arguments for ActionModule constructor
    fake_loader = "fake_loader"
    fake_path = "fake_path"
    fake_play = "fake_play"
    fake_new_play = "fake_new_play"
    fake_task = "fake_task"
    args = []
    fake_templar = "fake_templar"
    fake_shared_loader_obj = "fake_shared_loader_obj"
    facts_module = "facts_module"

    action_module = ActionModule(fake_loader, fake_path, fake_play, fake_new_play, fake_task, args, fake_templar, fake_shared_loader_obj, facts_module)

    fake_tmp = "fake_tmp"
    fake_task_vars = "fake_task_vars"

# Generated at 2022-06-13 09:44:50.308120
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 09:44:56.478942
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.loader import action_loader
    action = action_loader.get('debug', class_only=True)
    assert action._task.args == {}
    assert action._task.action == 'debug'
    assert action._task.action_type == 'debug'
    
    # Test verbosity
    action._task.args['msg'] = 'Hello world!'
    action._task.args['verbosity'] = 1
    action._display.verbosity = 0
    result = action.run(None, None)
    assert result['skipped_reason'] == "Verbosity threshold not met."
    assert result['skipped'] == True

    action._task.args['msg'] = 'Hello world!'
    action._task.args['verbosity'] = 0
    action._display.verbosity = 0

# Generated at 2022-06-13 09:45:01.032504
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.playbook.task import Task
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.utils.vars import load_extra_vars
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.utils.ssh_functions import check_for_controlpersist

    # Test var option with list
    testargs = {'var': {'a': 1, 'b': 2}}
    testresult = {'var': testargs['var']}
    testinclude = {}
    testresult['failed'] = False
   

# Generated at 2022-06-13 09:45:01.830004
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 09:45:02.785628
# Unit test for constructor of class ActionModule
def test_ActionModule():
    print('This is a mock test of ActionModule class')

# Generated at 2022-06-13 09:45:14.154961
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager

    loader = DataLoader()
    variable_manager = VariableManager()
    play_context = PlayContext()
    play_context._become_methods = {}  # Obviously not valid
    play_context._become_user     = None
    play_context.connection       = 'local'
    play_context.network_os       = 'default'
    play_context.remote_addr      = None
    play_context.port             = None
    play_context.remote_user      = None
    play_context.verbosity        = 4
    play_context.other_vars       = None


# Generated at 2022-06-13 09:45:18.044397
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    print("Unit test for method run of class ActionModule")
    actionModule = ActionModule(None, None, None, None, None)
    print("Test results: " + str(actionModule.run()))


# Generated at 2022-06-13 09:45:22.735331
# Unit test for constructor of class ActionModule
def test_ActionModule():
    a = ActionModule(task='', connection='', play_context='', loader='', templar='', shared_loader_obj='')
    assert ActionModule.TRANSFERS_FILES == False
    assert hasattr(a, 'run')

# Generated at 2022-06-13 09:45:23.561071
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True

# Generated at 2022-06-13 09:45:32.867948
# Unit test for constructor of class ActionModule
def test_ActionModule():
    test_variable = 'Hello world!'
    test_module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    test_task_args = dict()
    test_task_args['var'] = test_variable

    result = test_module.run(None, dict(), test_task_args)
    assert result['failed'] is False
    assert test_variable in result

# Generated at 2022-06-13 09:45:38.870499
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """
    Constructor of class ActionModule
    """
    
    #1.
    print("1")
    a = ActionModule(None,None)
    assert(a.TRANSFERS_FILES == False)
    del a
    #2.
    print("2")
    a = ActionModule(None,None)
    assert(a.TRANSFERS_FILES == False)
    del a

# Generated at 2022-06-13 09:45:46.251816
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Create a mock task object to pass to ActionModule
    task_args = {'msg': 'Hello world!'}
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.task import Task
    variable_manager = VariableManager()
    loader = DataLoader()
    options = PlayContext()
    inventory = InventoryManager(loader=loader, sources='localhost,')
    variable_manager.set_inventory(inventory)

# Generated at 2022-06-13 09:45:57.310462
# Unit test for method run of class ActionModule

# Generated at 2022-06-13 09:45:58.322571
# Unit test for constructor of class ActionModule
def test_ActionModule():
    m = ActionModule(None, None)
    assert m is not None

# Generated at 2022-06-13 09:46:01.087621
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass



# Generated at 2022-06-13 09:46:09.358592
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Create a test action module
    test_object = ActionModule(None, None, None)

    # Create a test result
    result = {'failed': False}

    # Create a test task with msg as 'Hello world!'
    task = {
        "args": {
            'msg': 'Hello world!'
        }
    }

    # Set verbosity of display to verbose
    test_object._display.verbosity = 4

    # Test run() method
    test_object.run(task_vars=result, tmp=None, task_vars=None)

    # Assert that the result contains the same message that was passed as argument to task
    assert result['msg'] == 'Hello world!'

    # Create a test task with msg as 'Hello world!'

# Generated at 2022-06-13 09:46:21.646067
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Test with message
    test_task = dict(msg="Hello World")
    test_task_args = dict(msg="Hello World")
    test_task_args = dict(verbosity=1)
    test_task_args = dict(verbosity=0)
    test_task_args = dict(verbosity=0, msg="Hello World")
    test_task_args = dict(verbosity=1, msg="Hello World")
    test_task = dict(var="Hello World")
    test_task_args = dict(var="Hello World")
    test_task_args = dict(verbosity=0, var="Hello World")
    test_task_args = dict(verbosity=1, var="Hello World")
    test_task = dict(var=["Hello World", "Hell World"])
    test_task_args = dict

# Generated at 2022-06-13 09:46:26.418221
# Unit test for constructor of class ActionModule
def test_ActionModule():

    module = ActionModule()
    assert module.TRANSFERS_FILES == False
    assert module._VALID_ARGS == frozenset(('msg', 'var', 'verbosity'))
    assert module._task.args == {}


# Generated at 2022-06-13 09:46:29.411106
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ac = ActionModule({},{})
    result = ac.run({'verbosity': 1})
    assert result['msg']=='Hello world!'

# Generated at 2022-06-13 09:46:41.833128
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule()
    assert isinstance(action._VALID_ARGS, frozenset)

# Generated at 2022-06-13 09:46:42.656827
# Unit test for method run of class ActionModule

# Generated at 2022-06-13 09:46:53.000911
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.playbook.task import Task

    from ansible.playbook.play_context import PlayContext
    from ansible.executor import task_queue_manager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.vars import load_extra_vars
    from ansible.utils.vars import load_options_vars
    inventory = InventoryManager(loader=DataLoader(), sources=['localhost,'])

# Generated at 2022-06-13 09:46:53.390943
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 09:46:54.151599
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """
    Test ActionModule constructor.
    """
    pass

# Generated at 2022-06-13 09:46:56.681085
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.play_context import PlayContext
    context = PlayContext()
    assert id(context) != id(None)
    del context

# Generated at 2022-06-13 09:47:00.327228
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(timeout=10)
    assert module.TRANSFERS_FILES == False
    assert module._VALID_ARGS == frozenset(('msg', 'var', 'verbosity'))

# Generated at 2022-06-13 09:47:02.412921
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(task=dict(action=dict(module_name='debug'), args={}))

# Generated at 2022-06-13 09:47:10.040450
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=['localhost,'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    play_source = dict(
            name = "Ansible Play",
            hosts = 'localhost',
            gather_facts = 'no',
            tasks = [
                dict(action=dict(module='debug', args=dict(msg='Hello World!')))
             ]
        )

# Generated at 2022-06-13 09:47:18.627341
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task

    #      var=foo msg=bar verbosity=1
    module = ActionModule(Task(), PlayContext())
    module._display = module._display()
    module._display.verbosity = 0
    module._task.args = {
        'var': 'foo',
        'msg': 'bar',
        'verbosity': 1,
        }
    result = module.run()
    assert result['failed'] == False
    assert result['skipped'] == True

    module = ActionModule(Task(), PlayContext())
    module._display = module._display()
    module._display.verbosity = 3

# Generated at 2022-06-13 09:47:52.573666
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import pytest
    from ansible.playbook.task import Task
    from ansible.playbook.play import Play

    # msg option
    task = Task()
    task.args = {'msg': "Hello world!", 'verbosity': 0}
    action = ActionModule(task, dict())
    result = action.run(None, dict())
    assert result.get('msg') == "Hello world!"
    assert result.get('failed') is False

    # var option with a string
    task = Task()
    task.args = {'var': "test_var", 'verbosity': 0}
    action = ActionModule(task, dict())
    result = action.run(None, dict(test_var="Hello world!"))
    assert result.get('test_var') == "Hello world!"

# Generated at 2022-06-13 09:47:55.971914
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    obj = ActionModule(None, None)
    assert obj.run(None, None) == {'failed': False, '_ansible_verbose_always': True, 'msg': 'Hello world!'}


# Generated at 2022-06-13 09:47:59.719493
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert 'msg' == action_module.run(None)['msg']
    assert 'Hello world!' == action_module.run(task_vars={'msg': 'Hello world!'})['msg']


# Generated at 2022-06-13 09:48:00.696706
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 09:48:15.279014
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task import Task
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager

    task_src = dict(action=dict(__ansible_module__='debug'))

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources='')
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    task = Task.load(task_src, variable_manager=variable_manager, loader=loader)
    action = task.action
    assert isinstance(action, ActionModule)
    assert hasattr(action, 'run')
    assert action.TRANSFERS_FILES is False
    assert action._task.action == 'debug'


# Generated at 2022-06-13 09:48:25.657505
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.action import ActionModule
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from ansible.executor.task_result import TaskResult
    from ansible.parsing.dataloader import DataLoader

    # Set options
    options = {
        '_ansible_check_mode': False,
        '_ansible_no_log': False,
        '_ansible_remote_tmp': '.ansible/tmp',
        '_ansible_verbosity': 2,
    }
    display = {
        'verbosity': 2
    }

    # Set task
    loader = DataLoader()

# Generated at 2022-06-13 09:48:33.922458
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import mock
    import sys
    import ansible.playbook
    import ansible.plugins

    # Mocking modules imported by ActionModule
    mock_display = mock.Mock()
    mock_templar = mock.Mock()
    mock_task = mock.Mock()

    mock_module_utils_module_loader = mock.Mock()
    sys.modules['ansible.module_utils.module_loader'] = mock_module_utils_module_loader
    mock_module_utils_module_loader.ModuleUtilsLoader = mock.Mock()


    sys.modules['ansible.plugins.action'] = mock.Mock()
    sys.modules['ansible.plugins.connection'] = mock.Mock()
    sys.modules['ansible.plugins.loader'] = mock.Mock()

# Generated at 2022-06-13 09:48:34.475887
# Unit test for constructor of class ActionModule
def test_ActionModule():
    ActionModule()

# Generated at 2022-06-13 09:48:38.701064
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import json
    test = '''
        - name: Test Action Module constructor
          debug:
            msg: "This is a test"'''
    print("Input:\n", test)
    ds = json.loads(test)
    am = ActionModule(ds[0], {})
    print("Result:", am)

# Generated at 2022-06-13 09:48:46.269814
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''
    Unit test for method ActionModule.run
    '''

    from ansible.playbook.task import Task
    from ansible.vars.manager import VarManager
    from ansible.template.template import Templar
    from ansible.parsing.yaml.objects import AnsibleUnicode
    import ansible.plugins.action.debug as debug
    import ansible.plugins.loader as loader
    from ansible.vars.hostvars import HostVars

    # Task with msg argument
    task = Task()
    task.args = dict(msg="Test")
    task_vars = dict()
    hostvars = HostVars()
    hostvars._data['expect'] = "expect"
    display = dict(verbosity=0)

# Generated at 2022-06-13 09:49:32.220393
# Unit test for constructor of class ActionModule
def test_ActionModule():
    test_obj = ActionModule(None, {}, None, {})
    assert('failed' in test_obj.run(None, None))
    assert('msg' in test_obj.run(None, None))

# Generated at 2022-06-13 09:49:40.373824
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from collections import namedtuple

    from ansible.plugins.action.debug import ActionModule

    #Prepare the required objects and set their properties
    #in order to pass the signature of method run of class ActionModule
    task_vars = {} # type: dict
    display = namedtuple('display', ['verbosity'])

    # Note: In python 3 namedtuples become new style classes.
    # to_text and to_bytes return the string as it is in python 3
    # In python 2, to_text and to_bytes are no-ops.
    # Therefore, in python 2, the strings appear as unicode type,
    # whereas in python 3, the strings appear as str type.
    display.verbosity = 0
    display.verbosity = 1
    display.verbosity = 2

    task_args = {} # type: dict
   

# Generated at 2022-06-13 09:49:46.555171
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    options = dict(connection='local', module_path='', forks=1, become=None, become_method=None, become_user=None, check=False, diff=False)
    loader = DataLoader()
    passwords = dict()
    inventory = InventoryManager(loader=loader, sources=['localhost'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    play_context = PlayContext(variables=variable_manager, options=options)
    queue

# Generated at 2022-06-13 09:49:57.604336
# Unit test for method run of class ActionModule
def test_ActionModule_run():
   action = ActionModule({'args': {'msg': 'Hello World!', 'verbosity': 0}},
                         {'display': {'verbosity': 0}})
   result = action.run(tmp=None, task_vars=None)
   assert result['failed'] == False
   assert result['msg'] == 'Hello World!'
   assert result['skipped'] == False
   assert result['skipped_reason'] == None

   action = ActionModule({'args': {'msg': 'Hello World!', 'verbosity': 1}},
                         {'display': {'verbosity': 0}})
   result = action.run(tmp=None, task_vars=None)
   assert result['failed'] == False
   assert result['skipped'] == True
   assert result['skipped_reason'] == 'Verbosity threshold not met.'


# Generated at 2022-06-13 09:50:05.164455
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import json

    print("Testing ActionModule constructor...")
    action_task = dict()
    action_task['action'] = dict()
    action_task['action']['__ansible_module__'] = "debug"
    action_task['action']['__ansible_arguments__'] = dict()

    action_args = dict()
    action_args['msg'] = "Hello World!"
    action_task['action']['__ansible_arguments__'] = action_args

    # Test with msg argument
    action_module = ActionModule(action_task, dict(), True)
    assert action_module._task.action == 'debug'
    assert action_module._task.name == 'debug'

# Generated at 2022-06-13 09:50:18.824051
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import os
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager

    class AnsibleTask:
        def __init__(self, args):
            self.args = args

    class AnsibleModule:
        def __init__(self, args):
            self.params = args

    class AnsibleUndefinedVariable:
        def __init__(self):
            self.message = "undefined variable"

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = Inventory(loader=loader, variable_manager=variable_manager,  host_list=['my_host'])

    dbg_

# Generated at 2022-06-13 09:50:25.260522
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext

    module_args = {"msg":"Hello world!"}
    action_args = []

    t = Task()
    
    pc = PlayContext()
    pc.remote_addr = '127.0.0.1'
    pc.remote_user = 'root'
    t._play_context = pc

    am = ActionModule(t,module_args, action_args)



# Generated at 2022-06-13 09:50:38.080259
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Create a test instance of class ActionModule
    test_instance = ActionModule(load_config_file=False, module_name=None, task=dict(), connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

    # Set test attributes to the test instance of class ActionModule
    test_instance._display = dict()
    test_instance._display['verbosity'] = 2
    test_instance._task = dict()
    test_instance._task.args = dict()
    test_instance._task.args['verbosity'] = 1

    # Create expected result for test
    expected_result = dict()
    expected_result['failed'] = False
    expected_result['skipped_reason'] = "Verbosity threshold not met."
    expected_result['skipped'] = True

    #

# Generated at 2022-06-13 09:50:48.319634
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule(
        task=dict(action=dict(module_name='debug')),
        connection=dict(module_name='ssh'),
        play_context=dict(check_mode=False),
        loader=None,
        templar=None,
        shared_loader_obj=None,
    )

    assert action._task.action.module_name == 'debug'
    assert action._connection.module_name == 'ssh'
    assert action._play_context.check_mode is False

    # No assertion for these attributes/properties. We only want to run the Django code to exercise it.
    action.become
    action.become_method
    action.become_user
    action._config
    action._display
    action._templar
    assert action._loader is None
    assert action._shared_loader_

# Generated at 2022-06-13 09:50:49.232295
# Unit test for constructor of class ActionModule
def test_ActionModule():
    testActionModule = ActionModule(None, None)

# Generated at 2022-06-13 09:52:45.879078
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule is not None

# Generated at 2022-06-13 09:52:49.334927
# Unit test for constructor of class ActionModule
def test_ActionModule():
    a = ActionModule(None, None, None)
    assert a.TRANSFERS_FILES == False
    assert a._VALID_ARGS == frozenset(('msg', 'var', 'verbosity'))

# Generated at 2022-06-13 09:52:59.912808
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Example 1: msg is specified, var is not specified
    module = ActionModule(
        dict(msg="Hello world!"),
        dict(name="hello_world_module", action="pause",  verbosity=0),
        tuple(),
        "test_palybook_file.yml",
        1,
        dict(),
        dict(ANSIBLE_MODULE_ARGS=dict(msg="Hello world!"), ANSIBLE_MODULE_NAME='pause', ANSIBLE_MODULE_CONSTANTS=dict())
    )

    version_info = dict(
        ansible_version='2.8.0',
        ansible_facts=dict(),
        ansible_version_string='2.8.0',
        ansible_python_version='2.7.15'
    )
    module._templar = _

# Generated at 2022-06-13 09:53:01.001121
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass
    # TODO

# Generated at 2022-06-13 09:53:11.598581
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(None, None)
    assert __file__ == module._config._ansible_executable         # Ensure the config module is not None
    assert module._task == None                                    # Ensure the task module is not None
    assert module._connection == None                              # Ensure the connection module is not None
    assert module._shell == None                                   # Ensure the shell module is not None
    assert module._display.verbosity == 0                          # Ensure the display module is not None
    assert module._play_context.check_mode == False                # Ensure the play_context module is not None
    assert module._loader == None                                  # Ensure the loader module is not None
    assert module._templar == None                                 # Ensure the templar module is not None
    assert module._shared_loader_obj.plugin_filters == {}          # Ensure the shared_loader

# Generated at 2022-06-13 09:53:15.602756
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(None, {"test_task":"test_task", "tasks_action":"test_action","task_args":{},"task_vars":{}, "tmp":None, "play_context":None}, "test_connection")

# Generated at 2022-06-13 09:53:24.781487
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    file_dict = {'path': 'test_action_plugin.py'}
    task_vars = {'test_var':'test_val'}
    module_name = 'test_action_plugin'
    to_text = str
    task = dict(action=file_dict)
    play_context = dict(verbosity=0)
    loader = None
    templar = None
    shared_loader_obj = None
    # If the assert is false it returns a string containing the error message
    assert run_method(ActionModule, 'run', module_name, to_text, task, play_context, loader, templar, shared_loader_obj) == None


# Generated at 2022-06-13 09:53:30.548923
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import ansible.plugins.action

    my_module = ansible.plugins.action.ActionModule('/some/path', 'localhost')
    assert my_module is not None

    # Test the static method ActionBase.static_load_factory()
    my_class = my_module.static_load_factory(my_module.__module__, my_module.__name__)
    assert my_class is not None

# Generated at 2022-06-13 09:53:34.092301
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext

    # Constructor tests
    module = ActionModule(Task(), PlayContext())
    assert module._task.action == 'debug'
    assert module._task.args == dict()

# Generated at 2022-06-13 09:53:40.161147
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # initializing assert object
    assert_obj = Assert()

    # creating mock object of class ActionModule
    task_args_obj = {"msg": "Hello World"}
    module_obj = ActionModule(None, None, task_args=task_args_obj,
                              task_vars=None)

    # executing run method of module_obj
    msg = "Hello World"
    results = module_obj.run()

    # asserting expected and actual values