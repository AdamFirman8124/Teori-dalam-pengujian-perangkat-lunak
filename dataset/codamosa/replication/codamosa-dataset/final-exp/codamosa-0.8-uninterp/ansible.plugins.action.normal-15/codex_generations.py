

# Generated at 2022-06-13 10:16:10.636684
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    result = ActionModule.run(ActionModule, tmp=None, task_vars=None)
    assert result is not None, "There should be some results from the command."

# Generated at 2022-06-13 10:16:11.076835
# Unit test for constructor of class ActionModule
def test_ActionModule():

    pass

# Generated at 2022-06-13 10:16:19.473569
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task import Task
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.inventory.manager import InventoryManager
    my_host = Host(name='hostname')
    my_group = Group(name='groupname')
    group_name = my_group.name
    my_host.groups.add(group_name)
    my_host.groups.add("all")
    my_group.hosts.add(my_host)
    host_name = my_host.name
    my_inventory_manager = InventoryManager()
    my_inventory_manager.groups.add(my_group)
    my_inventory_manager.hosts.add(my_host)
    my_task = Task(action='test', name='test')
    my_task

# Generated at 2022-06-13 10:16:20.043588
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert True

# Generated at 2022-06-13 10:16:30.163620
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import copy
    import sys
    import types

    from units.mock.loader import DictDataLoader

    from ansible import constants as C
    from ansible.errors import AnsibleError
    from ansible.executor.play_context import PlayContext
    from ansible.plugins.action import ActionBase
    from ansible.inventory.manager import InventoryManager
    from ansible.vars import VariableManager
    from ansible.module_utils.six import PY3
    from ansible.module_utils.six.moves import builtins

    # Note: when testing, it's ok to use the C.config object here in the test since it is a singleton
    # and the other unit tests should not have modified it.
    if PY3:
        from ansible.module_utils.six import io as cStringIO
        from io import String

# Generated at 2022-06-13 10:16:31.276607
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule()

# Generated at 2022-06-13 10:16:36.024371
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.inventory import Host
    from ansible.playbook.task import Task
    from ansible.executor.task_result import TaskResult
    host = Host("localhost", None, None)
    task = Task()
    task_result = TaskResult(host=host, task=task)
    a = ActionModule(task_result)
    print(a)

# Generated at 2022-06-13 10:16:49.651992
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.action import ActionModule
    from ansible.plugins.loader import module_loader
    from ansible.playbook.task import Task
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.playbook.play import Play
    from ansible.playbook.block import Block
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.handler import Handler
    from ansible.module_utils._text import to_text
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.playbook_executor import Playbook

# Generated at 2022-06-13 10:16:50.697996
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule is ActionBase

# Generated at 2022-06-13 10:17:01.589002
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(
        task=dict(action=dict(module_name='test_module', module_args=dict(test_arg='test_arg'))),
        connection=dict(connection='connection'),
        play_context=dict(become_user='root')
    )

    assert module._task.action.module_name == 'test_module'
    assert module._task.action.module_args == 'test_arg'
    assert module._connection.connection == 'connection'
    assert module._play_context.become_user == 'root'
    assert module._supports_check_mode == True
    assert module._supports_async == True

# Generated at 2022-06-13 10:17:06.605816
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.plugins.action.normal import ActionModule
    assert ActionModule is not None, "Unable to import ActionModule class"

# Generated at 2022-06-13 10:17:15.002761
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    ####
    #### mock ActionBase
    ####

    def mock_SUPPORTS_DEFAULT(self):
        return True

    def mock_SUPPORTS_ASYNC(self):
        return True

    ####
    #### mock ActionBase._execute_module
    ####
    def mock_execute_module(task_vars, wrap_async=False):
        return {'result': 'result from execute_module'}

    ActionBase._execute_module = mock_execute_module

    ####
    #### mock ActionBase.run
    ####

    def mock_run_returns_result(tmp, task_vars):
        return {
            'skipped': False,
            'invocation': {'module_args': {'a': 1}},
            'result': 'result from run'
        }

# Generated at 2022-06-13 10:17:16.162870
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule is not None


# Generated at 2022-06-13 10:17:18.142478
# Unit test for constructor of class ActionModule
def test_ActionModule():
	'''
	Unit test for constructor of class ActionModule
	'''
	action = ActionModule()
	assert action is not None

# Generated at 2022-06-13 10:17:19.631003
# Unit test for constructor of class ActionModule
def test_ActionModule():
    pass

if __name__ == '__main__':
    test_ActionModule()

# Generated at 2022-06-13 10:17:20.633409
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule()
    assert am

# Generated at 2022-06-13 10:17:22.446934
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """
    Test that the ActionModule.run() method
    """
    module = ActionModule()

# Generated at 2022-06-13 10:17:31.719738
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import ansible.playbook.play
    from ansible.playbook.task_include import TaskInclude
    from ansible.plugins import ActionBase
    from ansible.executor.task_queue_manager import TaskQueueManager
    import ansible.executor.task_result as task_result

    # Create a mock taskqueue
    mock_taskqueue = TaskQueueManager(inventory='ansible/inventory/hosts', variable_manager='ansible/inventory')
    mock_taskqueue._tqm_iterable = ['somehost']
    mock_taskqueue._failed_hosts = []
    mock_taskqueue._stats = {}

    # Create a mock task
    mock_task = TaskInclude()
    mock_task.action = 'someaction'
    mock_task.async_val = 0
    mock_task.delegate_to

# Generated at 2022-06-13 10:17:40.886111
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.utils.vars import combine_vars
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.utils.vars import load_extra_vars
    from ansible.utils.vars import load_options_vars
    from ansible.utils.vars import load_group_vars


# Generated at 2022-06-13 10:17:51.128965
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.action import ActionBase
    from ansible.utils.vars import merge_hash

    class ActionModule_Test(ActionModule):
        def run(self, tmp=None, task_vars=None):
            result = merge_hash(result, self._execute_module())
            return result

    tmp = '/tmp/ansible-tmp-1'
    task_vars = {}

    obj = ActionModule_Test(inject=None)
    res = obj.run(tmp=tmp, task_vars=task_vars)
    assert res == {}

# Generated at 2022-06-13 10:17:57.602632
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass


from ansible.plugins.action.action_plugins import ActionModule

# Generated at 2022-06-13 10:18:00.213772
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule()
    assert action_module is not None
    method_result = action_module.run(tmp="tmp", task_vars=None)
    assert method_result is not None

# Generated at 2022-06-13 10:18:08.441671
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    task = dict(action = dict(__ansible_module__='test_module'))
    tmp = '/tmp/ansible-test'
    task_vars = dict()
    self_ConnectionBase = dict()
    self_ResultBase = dict()

    result = dict(skipped=True)

    ActionModule(task, tmp, task_vars, self_ConnectionBase, self_ResultBase).run(tmp, task_vars)

# Generated at 2022-06-13 10:18:15.364918
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task import Task
    module_loader = None
    task = Task()
    connection = None

    action_plugin = ActionModule(task, connection, module_loader)
    assert action_plugin._task == task
    assert action_plugin._connection == connection
    assert action_plugin._loader == module_loader
    assert action_plugin._supports_check_mode == False
    assert action_plugin._supports_async == False

# Generated at 2022-06-13 10:18:18.556798
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """
    This unit test method is used to test the run method of ActionModule class.
    :return: It returns None
    """
    print("In ActionModule_run of Test Framework")
    assert True is True


# Generated at 2022-06-13 10:18:19.119529
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:18:22.709721
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Create a constructor for class ActionModule
    import ansible.plugins.action
    action_module = ansible.plugins.action.ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    # Check if the constructor return None
    assert isinstance(action_module, ansible.plugins.action.ActionModule)


# Generated at 2022-06-13 10:18:23.489215
# Unit test for constructor of class ActionModule
def test_ActionModule():
	assert ActionModule(task=task)

# Generated at 2022-06-13 10:18:24.009295
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert 1 == 1

# Generated at 2022-06-13 10:18:36.291931
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # setup mock for ansible.plugins.action.ActionBase._execute_module
    mock_self = type('', (object,), {'_execute_module': lambda *args, **kwargs: {'completed': True},
                                     '_task': type('', (object,), {'async_val': True, 'action': 'setup',
                                                                   'async_jid': '12345', 'name': 'ping host'}),
                                     '_connection': type('', (object,), {'has_native_async': True})})()
    # stubbed method call
    result = ActionModule.run(mock_self, tmp='/path/to/temp/dir', task_vars='task_vars')
    # test

# Generated at 2022-06-13 10:18:52.514843
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_base = ActionBase()
    action_module = ActionModule(action_base.connection, action_base.play_context, action_base.loader, action_base.templar, action_base._shared_loader_obj)
    assert action_module


# Generated at 2022-06-13 10:18:57.113297
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import random, os
    from ansible import constants as C
    from ansible.module_utils.basic import AnsibleModule

    connection = AnsibleModule(argument_spec={})

    # create a temporary action plugin path
    plugin_path = '/tmp/lib/action_plugins/'
    try:
        os.makedirs(plugin_path)
    except OSError:
        pass

    # setup a very basic action plugin

# Generated at 2022-06-13 10:18:58.486661
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule({}, {})
    print(module)

# Generated at 2022-06-13 10:19:00.356538
# Unit test for constructor of class ActionModule
def test_ActionModule():
    actionmodule = ActionModule()
    assert actionmodule is not None

# Generated at 2022-06-13 10:19:01.589923
# Unit test for constructor of class ActionModule
def test_ActionModule():
    a = ActionModule()
    assert a.async_timeout == 10

# Generated at 2022-06-13 10:19:10.398030
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """
    ActionModule.run() Test Plan:
     - setup:
       - tmp = None
       - task_vars = None

     - Check it will not skip
     - Check it will use module_args from result
     - Check it will use wrap_async from self._task.async_val and not self._connection.has_native_async

     - Check it will use _execute_module to calculate internally?
     - Check it will use merge_hash to result and what _execute_module returns

     - Check it will remove a temporary path
    """

    # setup
    a = ActionModule(action_plugin._task, action_plugin._connection, action_plugin._play_context, action_plugin._loader, action_plugin._templar, action_plugin._shared_loader_obj)
    a._task.async_val = True


# Generated at 2022-06-13 10:19:19.912488
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.plugins.action import ActionModule
    from ansible.module_utils._text import to_text
    from ansible.vars import VariableManager

    variable_manager = VariableManager()
    variable_manager.extra_vars = {'var1': 2}
    variable_manager.options_vars = {'opt1': 1}
    variable_manager.options_vars = {'opt2': 2}

    parent_task = {}

    task = {
        'action': {'module': 'ping', 'args': '-c1 -W1 -y', 'name': 'all'},
        'async': 300,
        'delegate_to': 'remote',
        'until': 'all',
        'retries': 3,
        'register': 'reg',
    }

    pipeline = None

# Generated at 2022-06-13 10:19:20.685338
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:19:24.922550
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import os

    import ansible
    from ansible.cli import CLI
    from ansible.cli.playbook import PlaybookCLI
    import ansible.plugins.action
    import ansible.plugins.action.normal
    import ansible.playbook.play
    import ansible.playbook.task

    # Current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Instance
    cli = PlaybookCLI(['ansible-playbook', '--forks', '1', os.path.join(current_dir, '../module_utils/test_module_args.yml')])
    cli.parse()

    # Play

# Generated at 2022-06-13 10:19:35.567030
# Unit test for constructor of class ActionModule
def test_ActionModule():
    task_vars = dict(
        ansible_verbosity=4
    )

    my_task = dict(
        async_val=False,
        action='test_action',
        module_name='test_module',
        module_args='test_args',
        module_vars=['test_vars'],
        module_import_name='test_import_name'
    )

    tmp = 'test_str'
    result = dict(
        skipped=False,
        invocation={'module_args': 'test_args'},
        ansible_facts={},
        ansible_module_args=None
    )

    action_module = ActionModule(my_task, tmp, task_vars)
    action_module._execute_module = lambda **kwargs: dict(changed=True, failed=False)
   

# Generated at 2022-06-13 10:19:58.132670
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:20:06.042602
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Initialize a new AnsibleModule with required parameters
    #
    # (params: module_class, task_vars, file_vars, connection, module_name,
    #          loader, templar, shared_loader_obj)
    #
    # Args of params will be created for test
    #
    # Note: the following params has no meaning for the test itself,
    #       and are just simple examples, not the real usecases

    import ansible.plugins.action as action
    class AnsibleModuleFake:
        def __init__(self, module_class, task_vars, file_vars, connection, module_name,
                     loader, templar, shared_loader_obj):
            self.module_class = module_class
            self.task_vars = task_vars
            self.file_v

# Generated at 2022-06-13 10:20:12.460155
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.inventory.host import Host
    from ansible.playbook.task import Task
    host = Host(name="test_host")
    task = Task()
    actionModule = ActionModule(task, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert actionModule is not None

# Generated at 2022-06-13 10:20:21.817260
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    m = ActionModule(connection=dict())
    m.connection._shell = dict()
    m.connection._shell.tmpdir = '/tmp/ansible'
    m.connection.has_native_async = False
    m._task = dict()
    m._task.async_val = None
    m._task.action = None
    r1 = m.run()  # test for no_log, which throws error
    m.connection._shell.tmpdir = ''
    r2 = m.run()  # test for tmp_path
    return r1, r2


# Generated at 2022-06-13 10:20:23.914500
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert False, 'No unit test written for method run of class ActionModule'



# Generated at 2022-06-13 10:20:28.675451
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """
    Test case for method run of class ActionModule.
    """
    # Create an instance of class ActionModule
    print ("Create the instance of class ActionModule")
    action_module = ActionModule()

    # Execute method run of class ActionModule
    print ("Execute the method run of class ActionModule")
    action_module.run()

# Generated at 2022-06-13 10:20:30.032960
# Unit test for constructor of class ActionModule
def test_ActionModule():
    a = ActionModule(None, None, None, None)
    assert a is not None

# Generated at 2022-06-13 10:20:38.086428
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    dst_name='/tmp/test_run'
    tmp = None
    task_vars = {}
    module_name = 'test_module_name'

# Generated at 2022-06-13 10:20:39.306450
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # this is a hard test to write
    pass

# Generated at 2022-06-13 10:20:41.554822
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule(None, None, None, None, None)
    assert len(action._task.action) > 0

# Generated at 2022-06-13 10:21:38.932544
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    print("TESTING TESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTEST")
    raise

# Generated at 2022-06-13 10:21:49.055382
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import ansible.plugins.action
    import ansible.playbook.role.task
    import ansible.playbook.task_include
    import ansible.template
    import ansible.utils.vars
    action_module = ansible.plugins.action.ActionModule(
        task=ansible.playbook.role.task.Task(),
        connection=None,
        play_context=None,
        loader=None,
        shared_loader_obj=None,
        templar=ansible.template.Templar(loader=None),
        task_vars=ansible.utils.vars.VariableManager(),
        default_vars=ansible.utils.vars.VariableManager())
    result = action_module.run(tmp=None, task_vars=None)
    assert result.get('skipped') == False

# Generated at 2022-06-13 10:21:53.205724
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_plugin = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert action_plugin is not None

# Generated at 2022-06-13 10:21:53.630158
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:21:54.579359
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # creation
    a = ActionModule(None)
    assert a is not None

# Generated at 2022-06-13 10:21:55.202071
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    pass

# Generated at 2022-06-13 10:21:58.957004
# Unit test for constructor of class ActionModule
def test_ActionModule():

    # Create an instance of class ActionModule
    uut = ActionModule()

    # Make sure it's an instance of the right class
    assert isinstance(uut, ActionModule)

    # TODO: Implement unit tests

# Generated at 2022-06-13 10:22:12.083178
# Unit test for constructor of class ActionModule

# Generated at 2022-06-13 10:22:13.437672
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    res = ActionModule.run()
    assert res == True

# Generated at 2022-06-13 10:22:18.818862
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # create the class object using constructor
    action_module = ActionModule()
    # print("%s" % action_module)

    # create the class object using test_default_args
    # test_class = ActionModule.test_default_args()
    # print("%s" % test_class)

    # create the class object using test_default_args
    test_class = ActionModule()
    print("%s" % test_class)

# call the function test_class_inheritance()
test_ActionModule()

# Generated at 2022-06-13 10:24:24.248084
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    task_vars = dict(
        ansible_check_mode=True
    )
    tmp_path = 'tmp_path'
    wrap_async = False
    module_name = 'module_name'
    module_args = 'module_args'
    task_vars = dict(
        module_name=module_name,
        module_args=module_args
    )
    tmp = 'tmp'
    task_vars = {'foo': 'bar'}
    module = ActionModule(task_vars)
    module.action = 'action'
    module.connection = 'connection'
    module.async_val = 'async_val'
    result = module.run(tmp, task_vars)
    assert(result == None)

    module = ActionModule(task_vars)

# Generated at 2022-06-13 10:24:27.221478
# Unit test for constructor of class ActionModule
def test_ActionModule():
    actionObj = ActionModule(
        task=dict(), connection=dict(), play_context=dict(), loader=dict(), templar=dict(), shared_loader_obj=dict())
    assert actionObj is not None

# Generated at 2022-06-13 10:24:37.932704
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Test case
    # Test for calling the run method with a module_name of 'shell' and a module_args of
    # 'echo Hello World' and checking for the expected result.

    # Arrange
    from ansible.playbook.task import Task
    import ansible.constants as C
    import ansible.modules.system.ping as ping
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager

    variable_manager = VariableManager()
    loader = variable_manager.loader

    # Set up required players
    task = Task()
    task.action = 'ping'
    task.async_val = 0
    task.async_seconds = 0
    task.args = ping.ARGS_SPEC

    # Create a fake inventory

# Generated at 2022-06-13 10:24:38.770778
# Unit test for constructor of class ActionModule
def test_ActionModule():

    import lib.action_plugins.action.norm

# Generated at 2022-06-13 10:24:40.411993
# Unit test for constructor of class ActionModule
def test_ActionModule():
  test_module = ActionModule()
  assert test_module is not None

# Generated at 2022-06-13 10:24:49.045223
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import __main__
    import sys
    setattr(__main__, '__file__', sys.argv[0])
    import ansible.utils.template
    t = ansible.utils.template.AnsibleTemplate
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    class ActionModule_run_Task():
        def __init__(self):
            self.name = None
            self.action = None
            self.async_val = None
            self.async_seconds = None
            self.run_once = None
            self.notify = None
            self.register

# Generated at 2022-06-13 10:24:59.290252
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.action.normal import ActionModule
    from ansible.vars.hostvars import HostVars
    import ansible.vars
    ansible.vars.hostvars = HostVars

# Generated at 2022-06-13 10:25:01.438493
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert am

# Generated at 2022-06-13 10:25:02.810224
# Unit test for constructor of class ActionModule
def test_ActionModule():

    actionmodule = ActionModule('test_label')

    assert actionmodule is not None, "Failed to make ActionModule"

# Generated at 2022-06-13 10:25:04.181280
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(dict(tmp='test', task_vars='test_task_vars'))