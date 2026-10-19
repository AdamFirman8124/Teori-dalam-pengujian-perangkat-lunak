

# Generated at 2022-06-13 10:16:09.974606
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    code = lambda code: ActionModule({}, code)
    assert code('a') == 'a'

# Generated at 2022-06-13 10:16:11.258879
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # test for ActionModule constructor
    action_module = ActionModule()
    assert action_module is not None

# Generated at 2022-06-13 10:16:16.029880
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # run method takes in task_vars and wraps it in a dict which 
    # contains a key called invocation which has module_args as one of the keys
    # the values for both are empty arrays
    # NOTE: _execute_module() does not seem to exist anymore
    from ansible.plugins.action import ActionModule
    import ansible.plugins.loader as plugins
    test_instance = ActionModule()

    assert(test_instance.run({}, []) == None)

# Generated at 2022-06-13 10:16:23.686291
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # define a class object ActionModule
    class ActionModule():
        def __init__(self):
            self._supports_check_mode = False

    # object of class ActionModule
    action_module = ActionModule()

    # test a new parameter added in this module
    # 
    # print(action_module.run({"tmp":True, "task_vars":{"test_task_var":"test_task_var_value"}}))
    print(action_module.run({"task_vars":{"test_task_var":"test_task_var_value"}}))


if __name__ == '__main__':
    test_ActionModule_run()

# Generated at 2022-06-13 10:16:31.419548
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import ansible.plugins.action
    action_plugins = ansible.plugins.action.ActionBase._load_action_plugins(C.DEFAULT_ACTION_PLUGIN_PATH)
    print(action_plugins)
    print(action_plugins.keys())
    assert 'auto' in action_plugins.keys()
    assert 'async' in action_plugins['auto'].keys()
    assert 'poll' in action_plugins['auto'].keys()
    assert 'pause' in action_plugins['auto'].keys()
    assert 'setup' in action_plugins['auto'].keys()

# Generated at 2022-06-13 10:16:33.986070
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # check object creation
    action_module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

# Generated at 2022-06-13 10:16:34.947858
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(dict(), 'localhost', 'test')

# Generated at 2022-06-13 10:16:38.764445
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(
        task=dict(action='fake_mod'),
        connection=dict(connection='connection_name'),
        play_context=dict(remote_addr='10.10.10.10')
    )

# Generated at 2022-06-13 10:16:49.867949
# Unit test for constructor of class ActionModule
def test_ActionModule():

    class MockTask():
        def __init__(self):
            self.action = "action_x"
            self.args = {}

    class MockPlayContext():
        def __init__(self):
            self.check_mode = True
            self.remote_addr = "127.0.0.1"

    class MockTaskVars():
        def __init__(self):
            self.task_vars = {}

    class MockConnection():
        def __init__(self):
            self.has_native_async = True

    class MockActionBase():

        def __init__(self):
            self._task = MockTask()
            self._play_context = MockPlayContext()
            self._task_vars = MockTaskVars()
            self._connection = MockConnection()

# Generated at 2022-06-13 10:16:53.469800
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    am = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert am.run(tmp=None, task_vars=None) == None

# Generated at 2022-06-13 10:17:05.721582
# Unit test for constructor of class ActionModule

# Generated at 2022-06-13 10:17:06.487306
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule()

# Generated at 2022-06-13 10:17:07.756061
# Unit test for constructor of class ActionModule
def test_ActionModule():
    a = ActionModule()
    assert isinstance(a, ActionModule)

# Generated at 2022-06-13 10:17:09.036762
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule();
    assert type(module).__name__ == 'ActionModule'

# Generated at 2022-06-13 10:17:17.083092
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    host_vars = dict()
    constants = dict()
    constants['DEFAULT_SUDO_PASS'] = 'default_sudo_pass'

    task_vars = {
        'hostvars': host_vars
    }

    tmp = None

    action_module = ActionModule(task=dict(action='test'), connection=dict(host='test_host', port=7999), play_context=dict(become=False, become_method='test_become_method', become_user='test_become_user'), loader=dict(), templar=dict(), shared_loader_obj=dict())
    action_module._remove_tmp_path = lambda a: True
    action_module._get_become_method = lambda a: 'test_become_method'

# Generated at 2022-06-13 10:17:17.552880
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:17:18.144799
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert(True)

# Generated at 2022-06-13 10:17:28.361384
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import imp
    import sys
    import argparse
    import os
    import datetime
    import yaml

    test_dir = os.path.dirname(__file__) + '/..'
    sys.path.append(test_dir)
    test_lib_dir = test_dir + '/testlib_for_unit_tests'
    sys.path.append(test_lib_dir)

    # import Ansible action plugin module
    from ansible.plugins.action import ActionBase

    # import Ansible module_utils
    ansible_module_utils = test_lib_dir + '/ansible_modlib.zip'
    if ansible_module_utils.endswith('.zip'):
        mod_path = os.path.splitext(ansible_module_utils)[0]

# Generated at 2022-06-13 10:17:36.740744
# Unit test for constructor of class ActionModule
def test_ActionModule():
    host = "testHostname"
    connection = "testConnection"
    task = "testTask"
    play_context = "testPlayContext"
    loader = "testLoader"
    templar = "testTemplar"
    shared_loader_obj = "testSharedLoaderObj"
    am = ActionModule(host, connection, task, play_context, loader, templar, shared_loader_obj)
    assert am._task.action == "testTask"
    assert am._loader.path_exists("asdf") == False
    print('ActionModule constructor test passed')


# Generated at 2022-06-13 10:17:38.189653
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    print("HI")
    a = ActionModule()
    a.run()

# Generated at 2022-06-13 10:17:56.435388
# Unit test for constructor of class ActionModule
def test_ActionModule():
    working_direct = "."
    config = {}
    loader = None
    variable_manager = None
    shared_loader_obj = None
    task_vars = {}
    action = None
    task_vars = {}
    create_ds = {}
    create_ds["hosts"] = "hosts"
    create_ds["vars"] = "vars"
    create_ds["tasks"] = "tasks"
    create_ds["defaults"] = "defaults"
    create_ds["project_name"] = "project_name"
    create_ds["role_name"] = "role_name"
    create_ds["module_name"] = "module_name"
    create_ds["module_args"] = "module_args"
    create_ds["module_lang"] = "module_lang"
   

# Generated at 2022-06-13 10:18:11.521718
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """
    Runs any unit tests for the class ActionModule
    :return:
    """
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins.loader import module_loader
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.play_iterator import PlayIterator
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=[])
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    play_context = PlayContext()
    play_context.connection = 'local'
    play_context.remote_

# Generated at 2022-06-13 10:18:12.337168
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # TODO: create and destroy mocks
    return None

# Generated at 2022-06-13 10:18:13.554296
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''Create an instance of the class'''
    module = ActionModule()
    assert module

# Generated at 2022-06-13 10:18:22.136834
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import ansible.plugins.loader
    import ansible.playbook.task
    import ansible.vars.manager
    import ansible.utils.vars

    # create a task with a simple action
    task_vars = ansible.vars.manager.VarManager()
    task = ansible.playbook.task.Task()
    task._role = None
    task.action = dict(module='ping', args=dict())

    # create a fake connection to pass to the plugin
    class FakeConnection():
        class _shell():
            tmpdir = '/does_not_exist'
        has_native_async = False
        def exec_command(self, cmd, tmp_path, sudoable=False, in_data=None, su=False, su_user=None):
            return 0, '', ''

# Generated at 2022-06-13 10:18:24.986269
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # test that ActionModule initializer is not erroring on valid module
    assert ActionModule('setup', {'setup': {'filter': 'ansible_local'}}, False, None, None)



# Generated at 2022-06-13 10:18:25.663890
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:18:26.471219
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:18:29.071272
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule()
    assert isinstance(module, ActionModule)

if __name__ == '__main__':
    test_ActionModule()

# Generated at 2022-06-13 10:18:31.682324
# Unit test for constructor of class ActionModule
def test_ActionModule():

    from ansible.plugins.action import ActionModule
    from ansible.utils.sentinel import Sentinel
    assert ActionModule.__doc__

# Generated at 2022-06-13 10:18:51.690719
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.plugins.action.normal import ActionModule
    action = ActionModule()
    # Ensure we correctly set all required instance attributes
    assert hasattr(action, 'action_loader')
    assert hasattr(action, '_templar')
    assert hasattr(action, '_play_context')
    assert hasattr(action, '_loader')
    assert hasattr(action, '_task')
    assert hasattr(action, '_shared_loader_obj')
    assert hasattr(action, '_connection')
    assert hasattr(action, '_task_vars')
    assert hasattr(action, '_start_at_done')
    assert hasattr(action, '_block')
    assert hasattr(action, '_play')
    assert hasattr(action, '_included_filenames')

# Generated at 2022-06-13 10:19:01.247361
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import ansible.plugins.action
    ActionModule = ansible.plugins.action.ActionModule
    mod = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    import ansible.vars
    import ansible.module_utils
    mytask_vars = ansible.vars.TaskVars(play=None, task=None)
    mytask_vars.update(dict(foo='bar'))
    mytask_vars.update(ansible.module_utils.basic.HUDict(bar='baz'))
    result = mod.run(task_vars=mytask_vars)
    assert result == {}, result

# Generated at 2022-06-13 10:19:10.209956
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block

    from ansible.inventory.manager import InventoryManager

    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.play_iterator import PlayIterator

    from ansible.plugins.loader import find_plugin, action_loader, connection_loader
    from ansible.plugins.action import ActionBase

    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.host import Host, Group

    from ansible.utils.vars import combine_vars

    class ArgParse:
        def __init__(self):
            self.syntax = None
            self.connection = 'local'
            self.module_path

# Generated at 2022-06-13 10:19:12.430438
# Unit test for constructor of class ActionModule
def test_ActionModule():
    try:
        my_action_module = ActionModule()
    except:
        assert False, "Exception when instantiating ActionModule object"
    else:
        assert True


# Generated at 2022-06-13 10:19:12.906645
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert True

# Generated at 2022-06-13 10:19:14.905961
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(None, None)
    assert action_module is not None
    assert action_module._supports_check_mode is True
    assert action_module._supports_async is True

# Generated at 2022-06-13 10:19:21.682947
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.play_context import PlayContext

    module = ActionModule(task=Task(), connection='local', play_context=PlayContext())
    assert isinstance(module, ActionModule)
    assert isinstance(module.block, Block)
    assert isinstance(module.task, Task)
    assert isinstance(module._play_context, PlayContext)

# Generated at 2022-06-13 10:19:22.710808
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """
    Unit test for method run of class ActionModule.
    :return:
    """
    pass

# Generated at 2022-06-13 10:19:23.861761
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.plugins.action.normal import ActionModule
    a = ActionModule()


# Generated at 2022-06-13 10:19:27.543725
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.plugins.action import ActionModule
    from ansible.playbook.task import Task

    t = Task()
    t._role = None
    c = ActionModule(t)
    assert isinstance(c,ActionModule)

# Generated at 2022-06-13 10:19:58.976634
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Define a mock task which is used to test the constructor's behaviour.
    class MockTask:
        async_val = False
        action = 'setup'
    class MockConnection:
        has_native_async = False
    class MockPlayContext:
        def __init__(self):
            self.check_mode = False
            self.diff = False
    class MockModule:
        attr = 'some value'
    act = ActionModule('test','test', MockTask(), MockConnection(), MockPlayContext(), MockModule())
    assert act.task == 'test'
    assert act.connection == 'test'
    assert act._task == MockTask()
    assert act._connection == MockConnection()
    assert act._display.verbosity == 2
    assert act._supports_check_mode == False

# Generated at 2022-06-13 10:19:59.431835
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:20:09.194538
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.plugins.action import ActionBase
    from ansible.plugins.cache.memory import ActionModule as ActionModule_impl
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.executor.task_result import TaskResult
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.playbook.play_context import PlayContext
    #from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.executor.process.worker import WorkerProcess

# Generated at 2022-06-13 10:20:16.914966
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import actionplugin
    from ansible.plugins.loader import action_loader
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext

    action_loader.add_directory(actionplugin.__path__._path[0])

    # Initializing resources
    loader = DataLoader()
    variable_manager = VariableManager()
    inventory_manager = InventoryManager(loader=loader, sources='unittest_hosts')
    variable_manager.set_inventory(inventory_manager)
    play_context = PlayContext()


# Generated at 2022-06-13 10:20:24.723530
# Unit test for constructor of class ActionModule
def test_ActionModule():

    class ShellModule:

        def __init__(self, arg1, arg2, arg3=None, **kwargs):
            self.arg1 = arg1
            self.arg2 = arg2
            self.arg3 = arg3

    class ConnectionModule:

        def close(self):
            return

        def exec_command(self, cmd, tmp_path, sudo_user=None, sudoable=False):
            raise Exception("I have not implemented this method")

        def put_file(self, in_path, out_path):
            raise Exception("I have not implemented this method")

        def fetch_file(self, in_path, out_path):
            raise Exception("I have not implemented this method")


# Generated at 2022-06-13 10:20:25.337613
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:20:28.062692
# Unit test for constructor of class ActionModule
def test_ActionModule():
    x = ActionModule(connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert x is not None

# Generated at 2022-06-13 10:20:36.805091
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """Check if we can get a result when we call method run of class ActionModule"""
    # Set up the class
    mock_connection = MagicMock()
    mock_connection._shell = MagicMock()
    mock_connection._shell.tmpdir = 'FAKE_TMP_PATH'
    mock_task = MagicMock()
    mock_task.async_val = False
    mock_task.action = 'FAKE_ACTION'
    action_module = ActionModule(mock_connection, mock_task, tmp_path='FAKE_TMP_PATH')

    # mock return value from method _execute_module(task_vars={'failed': False, 'changed': False, 'skipped': False})

# Generated at 2022-06-13 10:20:37.611205
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule()
    assert module is not None

# Generated at 2022-06-13 10:20:38.738811
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule is not None

# Generated at 2022-06-13 10:21:23.520111
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule is not None

# Generated at 2022-06-13 10:21:32.639906
# Unit test for constructor of class ActionModule
def test_ActionModule():
    mytask = dict(
        action=dict(
            module="shell",
            args="echo hello world"
        )
    )

    mock_connection = unittest.mock.MagicMock()
    mock_loader = unittest.mock.MagicMock()
    mock_templar = unittest.mock.MagicMock()

    action = ActionModule(mock_connection, mytask, mock_loader, mock_templar)

    assert action._task == mytask
    assert action._connection == mock_connection
    assert action._loader == mock_loader
    assert action._templar == mock_templar
    assert action._task_vars == dict()

# Generated at 2022-06-13 10:21:33.745837
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # TODO:
    pass

# Generated at 2022-06-13 10:21:38.667524
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''
    Test the run method of class ActionModule
    '''

    result = dict(
        changed=False,
        failed=False,
        _ansible_verbose_override=True,
        msg=''
    )

    action_module = ActionModule()
    action_module._task.async_val = 0
    action_module._task.action = 'setup'

    assert action_module.run() == result, "run method have value error"

# Generated at 2022-06-13 10:21:39.257238
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:21:44.990293
# Unit test for constructor of class ActionModule
def test_ActionModule():
    test_class = ActionModule('setup', {}, False, False, '/path/to/ansible/modules')
    assert hasattr(test_class, '_supports_check_mode')
    assert hasattr(test_class, '_supports_async')

# Generated at 2022-06-13 10:21:51.855684
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import types
    import sys
    tmp = 'test_ActionModule_run'
    task_vars = 'test_ActionModule_run'
    res = ActionModule.run(ActionModule, tmp, task_vars)
    # check that return type is types.DictType
    assert(isinstance(res, types.DictType))


# Generated at 2022-06-13 10:21:58.661820
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.plugins.connection.local import Connection
    from ansible.playbook.task import Task
    from ansible import module_loader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    import ansible.constants as C
    from ansible.playbook.play_context import PlayContext

    C.HOST_KEY_CHECKING = False
    C.DEFAULT_HASH_BEHAVIOUR = 'merge'
    loader = module_loader.ActionModuleLoader(None, './lib/ansible/modules', './lib/ansible/modules/extras')
    connection = Connection(loader)
    module_name = 'shell'
    task = Task()
    task.all_vars = {}
    task.name = 'shell'

# Generated at 2022-06-13 10:22:00.838294
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import ansible.plugins.action.normal as action
    module = action.ActionModule()
    assert module is not None

# Generated at 2022-06-13 10:22:12.986669
# Unit test for constructor of class ActionModule
def test_ActionModule():
    host = 'host1'
    task = 'task1'
    connection = 'connection1'
    play_context = 'play_context1'
    loader = 'loader1'
    templar = 'templar1'
    shared_loader_obj = 'shared_loader_obj1'

    am = ActionModule(host, task, connection, play_context, loader, templar, shared_loader_obj)
    assert am.host == host
    assert am.task == task
    assert am.connection == connection
    assert am.play_context == play_context
    assert am.loader == loader
    assert am.templar == templar
    assert am.shared_loader_obj == shared_loader_obj

# Generated at 2022-06-13 10:24:02.894441
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    print("Testing ActionModule run()")


    # The next section is how to setup a fake ansible module.
    # We need to create a fake environment, with a fake module that has the
    # struture of an AnsibleModule.
    from ansible.module_utils.basic import AnsibleModule
    import ansible.module_utils.basic

    class FakeAnsibleModule(object):
        def __init__(self, *args, **kwargs):
            #args[0] should be the first argument of the ansible module called
            self.args = args[0]
            self.params = kwargs

        def fail_json(self, **kwargs):
            # nothing to do here,
            # this method is tested in the test_basic.py test_basic.py
            self.exit_args = kwargs


   

# Generated at 2022-06-13 10:24:04.045569
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """This includes the basic tests for the constructor of the class"""
    test = ActionModule()
    assert test

# Generated at 2022-06-13 10:24:05.731269
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import ansible
    assert(ansible)

# Generated at 2022-06-13 10:24:13.685664
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Test: Test ActionModule class run method without async
    module = ActionModule()
    module._supports_check_mode = True
    module._supports_async = True


# Generated at 2022-06-13 10:24:14.655656
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(None, None, None, None)

# Generated at 2022-06-13 10:24:15.454030
# Unit test for constructor of class ActionModule
def test_ActionModule():
    actionModule = ActionModule()
    assert actionModule != None

# Generated at 2022-06-13 10:24:25.889232
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.module_utils.basic import AnsibleModule
    from ansible.parsing.dataloader import DataLoader
    import sys

    if sys.version_info >= (3, 0):
        sys.exit()

    variable_manager = VariableManager()
    loader = DataLoader()

    host1 = Inventory(loader=loader, variable_manager=variable_manager, host_list='tests/inventory/hosts')
    variable_manager.set_inventory(host1)

    variable_manager._extra_vars = {'ansible_connection': 'local'}

    play_context = PlayContext()


# Generated at 2022-06-13 10:24:37.122211
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task import Task

    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext

    from ansible.executor.play_iterator import PlayIterator

    from ansible.executor.task_queue_manager import TaskQueueManager

    from ansible.parsing.dataloader import DataLoader

    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    from ansible.inventory.host import Host
    from ansible.inventory.group import Group

    play_context = PlayContext()
    play_context.network_os = 'ios'
    play_context.become = 'no'
    play_context.become_method = ''

    loader = DataLoader()

    inventory = InventoryManager(loader=loader)

# Generated at 2022-06-13 10:24:39.155449
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule()
    assert module._supports_check_mode == True and module._supports_async == True

# Generated at 2022-06-13 10:24:40.363225
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # TODO
    print("ActionModule()")