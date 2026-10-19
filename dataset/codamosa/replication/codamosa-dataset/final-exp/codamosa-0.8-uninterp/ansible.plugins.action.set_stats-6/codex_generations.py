

# Generated at 2022-06-13 10:42:16.266661
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:42:18.551802
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    am = ActionModule(task=dict(args=None), connection=dict(host=None, port=None, user=None, password=None))
    assert am.run()

# Generated at 2022-06-13 10:42:29.101234
# Unit test for constructor of class ActionModule
def test_ActionModule():
   
    class MyActionModule(ActionModule):

        def run(self, tmp=None, task_vars=None):
            if task_vars is None:
                task_vars = dict()
            result = super(MyActionModule, self).run(tmp, task_vars)
            return result

    action_module = MyActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

    assert action_module.args == dict()
    assert action_module.connection == None
    assert action_module.loader == None
    assert action_module.play_context == None
    assert action_module.plugin_type == 'action'
    assert action_module.shared_loader_obj == None
    assert action_module.task == None

# Generated at 2022-06-13 10:42:41.630205
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils.ansible_modlib import DictObj
    from ansible.module_utils.six import string_types
    from ansible.template import Templar
    from ansible.vars import VariableManager

    from ansible.plugins.action.set_stats import ActionModule

    # create fake variables
    variable_manager = VariableManager()
    variable_manager.extra_vars = {'fake_var': 'hello'}

    # create fake loader
    loader_mock = DictObj()
    loader_mock.get_basedir.return_value = 'fake_basedir'

    # create fake play context
    play_context_mock = DictObj()
    play_context_mock.network_os = None
    play_context_mock.remote_addr = False
    play_context_m

# Generated at 2022-06-13 10:42:43.441764
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule(None, None, None, None, None, None)
    assert type(action) == ActionModule

# Generated at 2022-06-13 10:42:45.569117
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule(task=dict(action=dict(module_name="setup", args=dict(filter='ansible_distribution_version'))))
    print(am.run())


# Generated at 2022-06-13 10:42:55.065318
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.utils.vars import merge_hash
    from ansible.plugins.action.set_stats import ActionModule


# Generated at 2022-06-13 10:43:02.356912
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext

    task = Task()
    play_context = PlayContext()
    action_module = ActionModule(task, play_context)
    assert action_module._task == task
    assert action_module._play_context == play_context
    assert action_module._loader.get_basedir() == task._role._role_path
    assert action_module._templar == play_context.CLIARGS['module_compression']

# Generated at 2022-06-13 10:43:03.811151
# Unit test for constructor of class ActionModule
def test_ActionModule():
    foo = ActionModule()
    print(foo)
    assert False

# Generated at 2022-06-13 10:43:05.122037
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert 'action plugin' in ActionModule.__doc__

# Generated at 2022-06-13 10:43:10.965955
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule()

# Generated at 2022-06-13 10:43:11.510352
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule()

# Generated at 2022-06-13 10:43:14.022866
# Unit test for method run of class ActionModule
def test_ActionModule_run():
	m = ActionModule()
	res = m.run(tmp=None, task_vars=None)
	assert 'ansible_stats' in res

# Generated at 2022-06-13 10:43:17.336474
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # set_stats.py can't be run directly, as it's not a module, but an ActionModule.
    # However, it's possible to run ActionBase.run, which is implemented in
    # set_stats.py.
    # TODO: how to test?
    pass

# Generated at 2022-06-13 10:43:18.778069
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """ Unit test for run method"""

    # TODO: implement this
    raise NotImplementedError

# Generated at 2022-06-13 10:43:23.301949
# Unit test for constructor of class ActionModule
def test_ActionModule():
    #import sys
    #sys.path.append("/home/ceph-user/ceph-qa-suite/qas_lib")
    #from sanlock_client import SanlockClient
    #replica = '192.168.174.133'
    #client = SanlockClient(replica)
    #client.client.connect()
    #client.client.release()
    #client.client.disconnect()
    #import pdb
    #pdb.set_trace()
    pass


# Generated at 2022-06-13 10:43:27.477530
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """
    Test for method run of class ActionModule
    """
    # Test for full argument types
    test_instance = ActionModule(action=None, task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert test_instance.run(tmp=None, task_vars=None) == None

    # Test for no argument types
    test_instance = ActionModule(action=None, task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert test_instance.run(None, None) == None

# Generated at 2022-06-13 10:43:28.655502
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(None, None).run() == ActionModule.run(None, None)

# Generated at 2022-06-13 10:43:33.172609
# Unit test for constructor of class ActionModule
def test_ActionModule():

    # Execute constructor with no arguments
    plugin = ActionModule()

    # Check if data member is an instance of the correct type
    assert isinstance(plugin.runner, object)
    assert isinstance(plugin.data, object)
    assert isinstance(plugin.runner_queue, object)
    assert isinstance(plugin.playbook, object)
    assert isinstance(plugin._connection, object)
    assert isinstance(plugin._play_context, object)
    assert isinstance(plugin._loader, object)
    assert isinstance(plugin._templar, object)
    assert isinstance(plugin._shared_loader_obj, object)
    assert isinstance(plugin._task, object)
    assert isinstance(plugin._task_vars, object)
    assert isinstance(plugin._tmp, object)

    # Create a fake task argument
    task_

# Generated at 2022-06-13 10:43:37.315627
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule(dict(task=dict(args=dict(data=dict(a=1, b=2)))))
    assert action._valid_args == action._VALID_ARGS
    assert not action.TRANSFERS_FILES
    assert action._task.args.get('data', None) == dict(a=1, b=2)

# Generated at 2022-06-13 10:43:54.521403
# Unit test for constructor of class ActionModule
def test_ActionModule():
    class Task:
        args = dict()

    class Module:
        pass

    class Play:
        pass

    class PlayContext:
        pass

    class TaskQueueManager:
        pass

    class DataLoader:
        pass

    class Variables:
        pass

    class Runner:
        pass

    class Connection:
        def __init__(self):
            self.transport = 'local'

    class Inventory:
        def __init__(self):
            self.hosts = dict()
            self.hosts['localhost'] = {'vars': dict()}

    class AdHoc:
        pass

    class Playbook:
        pass

    class Set:
        pass

    action_task = Task()
    action_task.args = dict()
    action_task.action = 'setup'
    action_task.name

# Generated at 2022-06-13 10:43:57.466368
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''
    Test constructor of class ActionModule
    :return:
    '''
    action_module = ActionModule()
    assert action_module is not None, 'Failed to create object'

# Generated at 2022-06-13 10:44:05.845844
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule(task=dict(args=dict(data={ "log_level": 5 }, per_host=True, aggregate=True)))
    result = module.run(task_vars=dict())
    wanted = {
        'changed': False,
        'ansible_stats': {
            'data': {
                'log_level': 5,
            },
            'per_host': True,
            'aggregate': True
        }
    }
    assert result == wanted, result

# Generated at 2022-06-13 10:44:14.921649
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import ansible.plugins.loader as plugin_loader
    import ansible.plugins.action as action_plugins
    import ansible.utils.vars as vars

    action_plugin = plugin_loader.get('action', 'set_stats')

    action_init = action_plugin(task={"action": "set_stats", "args": {"data": {"foo1": "bar1", "foo2": "bar2"}, "aggregate": False, "per_host": True}},
                                     connection=None,
                                     play_context=None,
                                     loader=None,
                                     templar=vars.AnsibleVars,
                                     shared_loader_obj=None)

    assert isinstance(action_init, action_plugins.ActionModule)

    assert action_init.TRANSFERS_FILES == False

# Generated at 2022-06-13 10:44:20.113548
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """
    Unit test for ActionModule.
    """
    # Test constructor
    am = ActionModule(None, None)
    if hasattr(am, "_VALID_ARGS"):
        print("Attribute ActionModule._VALID_ARGS exists.")

    if am.TRANSFERS_FILES:
        print("Attribute ActionModule.TRANSFERS_FILES is true.")

# Generated at 2022-06-13 10:44:22.328473
# Unit test for constructor of class ActionModule
def test_ActionModule():
    aa = ActionModule()
    assert aa.VALID_ARGS == frozenset(('aggregate', 'data', 'per_host'))

# Generated at 2022-06-13 10:44:27.324415
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # create a fake task
    task = object()

    # create a fake temp name
    temp_name = 'temp_name'

    # create a fake task vars
    task_vars = {'ansible_verbosity': 0}

    # instantiate an instance of ActionModule
    action_mod = ActionModule(task, temp_name, task_vars)

    # checking the return value of run method
    assert action_mod.run(temp_name, task_vars) is not None

# Generated at 2022-06-13 10:44:30.614855
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # TODO: create unit test to verify functionality of the method run of class ActionModule
    #res = action.run(tmp=None, task_vars=None)
    pass

# Generated at 2022-06-13 10:44:37.949235
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """
    Unit test for constructor of class ActionModule.
    """
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    loader = DataLoader()
    variable_manager = {}
    _taskqmgr = TaskQueueManager(loader=loader, variable_manager=variable_manager, passwords=None)

# Generated at 2022-06-13 10:44:43.270429
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    am = ActionModule(
        task=dict(action=dict(module_name='set_stats', arguments=dict(data=dict(debug="{{ debug }}"))))
    )

    # test that the variable 'debug' is correctly set and the variable name is
    # correctly rendered
    assert am.run(task_vars=dict(debug='true'))['ansible_stats'] == {'data': {'debug': 'true'}, 'aggregate': True, 'per_host': False}

# Generated at 2022-06-13 10:45:02.975212
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(None, None) is not None

# Generated at 2022-06-13 10:45:11.695958
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.task import Task
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    class Fake:
        def __init__(self, **kwargs):
            self.__dict__ = kwargs
    class FakeDS:
        def __init__(self, **kwargs):
            self.__dict__ = kwargs
        def get_vars(self, hostname=None):
            return dict(test_var = "test_val", fail_var = "{{ var_not_defined }}")
        def get_host_vars(self, hostname):
            return dict(test_var = "test_val", fail_var = "{{ var_not_defined }}")

# Generated at 2022-06-13 10:45:17.360292
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.utils.vars import combine_vars
    from ansible.playbook.task import Task

    AnsibleModule = ActionModule(Task(), dict())
    assert isinstance(AnsibleModule, ActionModule)
    assert isinstance(AnsibleModule._VALID_ARGS, frozenset)
    assert AnsibleModule.TRANSFERS_FILES == False



# Generated at 2022-06-13 10:45:23.983517
# Unit test for constructor of class ActionModule
def test_ActionModule():
    ActionModule(
        task=dict(args=dict(
            data=dict(
                key1="value1",
                key2="value2",
             ),
            per_host=True,
            aggregate=False,
        )),
        connection=None,
        play_context=dict(
            # Run on localhost, no variables
            inventory=dict(
                hosts=["localhost"],
                vars={}
            )
        ),
        loader=None,
        templar=None,
        shared_loader_obj=None
    ).run()

# Generated at 2022-06-13 10:45:26.187402
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # If module fails, return None
    # Pass for now
    pass

# Generated at 2022-06-13 10:45:33.017653
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    args = {'data': {'some_var': '{{ foo }}', 'some_other_var': '{{ bar }}'}}

    action = ActionModule(dict(ACTIONS=dict(set_stats=args)), None)
    action.task = dict(args=args)
    action.task_vars = dict(foo='foo', bar='bar')

    res = action.run()

    assert res['changed'] == False
    assert res['ansible_stats'] == {'data': {'some_var': 'foo', 'some_other_var': 'bar'}, 'aggregate': True, 'per_host': False}

# Generated at 2022-06-13 10:45:46.101892
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import ansible.plugins.action
    p = ansible.plugins.action.ActionModule(None, {}, None, None, None, "", "", "", "", "", "", "")
    p._templar = ansible.template.Templar(None)
    p._task = ansible.task.Task(
        None, None,
        {"args": {
            "data": {
                "var1": "value1",
                "var2": "value2",
            },
            "per_host": False,
            "aggregate": True,
        }
        },
        None)
    res = p.run(None, None)

# Generated at 2022-06-13 10:45:48.672688
# Unit test for constructor of class ActionModule
def test_ActionModule():
    ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

# Generated at 2022-06-13 10:45:51.985226
# Unit test for constructor of class ActionModule
def test_ActionModule():
    print("Testing ActionModule")
    assert ActionModule(None, None, None)._task.args == {}, "ActionModule object is created with empty args"
    print("PASSED")

if __name__ == '__main__':
    test_ActionModule()

# Generated at 2022-06-13 10:45:53.779415
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # TODO: rewrite this with AnsibleModule based on set_stats.py module
    assert ActionModule()

# Generated at 2022-06-13 10:46:39.466310
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Passing
    args = dict()
    # Result of templating is expected to be a dict
    args['data'] = """
    {
        "test1": {{ test1 }},
        "test2": {{ test2 }},
    }
    """
    data = dict()
    data['test1'] = 'test'
    data['test2'] = 'test'

    fail_msg1 = "The variable name 'test1' is not valid. Variables must start with a letter or underscore character, and contain only letters, numbers and underscores."
    fail_msg2 = "The 'data' option needs to be a dictionary/hash"

    # Case 1: Passing with all required args
    expected_result = dict()
    expected_result['changed'] = False
    expected_result['ansible_stats'] = dict()

# Generated at 2022-06-13 10:46:50.814922
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    test_result = {'changed': None}
    test_result_expected = {'changed': False, 'ansible_stats': {'data': {'test_result': 'mytest'}, 'per_host': False, 'aggregate': True}}
    # import
    import sys
    sys.path.append('/home/user/ansible/lib/ansible/modules/action')
    # create dummy class
    class Dummy(object):
        """This is a dummy class for unittesting"""
        def __init__(self):
            self._task = {}
            self.args = {}
            self.run_command_environ_update = {}
            self._templar = {}
            self._templar.template = {}
    # create dummy object
    dummy = Dummy()
    # set args
    dummy._task

# Generated at 2022-06-13 10:46:59.106130
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    mod = ActionModule()
    mod._task.args = {}
    mod.run()
    assert (mod.run()['ansible_stats']['data'] == {})
    mod._task.args = {'data': 'testdata'}
    mod.run()
    assert (mod.run()['ansible_stats']['data'] == {})
    mod._task.args = {'data': {'testkey': 'testvalue'}}
    assert (mod.run()['ansible_stats']['data'] == {'testkey': 'testvalue'})
    mod.run()
    mod._task.args = {'aggregate': 10}
    assert (mod.run()['ansible_stats']['aggregate'] == True)
    mod._task.args = {'aggregate': 0}

# Generated at 2022-06-13 10:47:10.062511
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Fake ansible module object
    class FakeAnsibleModule:

        class FakeModule:

            def __init__(self, args):
                self.args = args

        def __init__(self, task_vars):
            self._task = FakeAnsibleModule.FakeModule(task_vars)

    # Fake ansible module action plugin object
    class FakeAnsibleActionModule(ActionModule):

        def __init__(self, task_vars):
            AnsibleModule = FakeAnsibleModule(task_vars)
            self._task_vars = task_vars
            super(FakeAnsibleActionModule, self).__init__(AnsibleModule)

    # Instantiate fake ansible module action plugin
    fake_task_vars = {}

# Generated at 2022-06-13 10:47:20.751971
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.utils.vars import AnsibleVars
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext

    play_context = PlayContext()
    play_context.remote_user = 'test'
    play_context.remote_addr = 'test'
    play_context.connection = 'test'
    play_context.port = 'test'

    loader = DataLoader()

    variables = AnsibleVars(loader=loader, play_context=play_context)
    variable_manager = VariableManager(loader=loader, variables=variables)

    actionmodule = ActionModule(loader=loader, play_context=play_context, variable_manager=variable_manager)
    

# Generated at 2022-06-13 10:47:23.922150
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    instance = ActionModule()
    with pytest.raises(AnsibleParserError):
        instance.run(tmp=None, task_vars=dict())

# Generated at 2022-06-13 10:47:33.920304
# Unit test for constructor of class ActionModule
def test_ActionModule():

    results = {"failed": False, "ansible_stats": {"data": {}, "per_host": False, "aggregate": True}}

    # test no args
    action_module = ActionModule(dict(action=dict()), dict(task_name='set_stats'), False, False)
    assert results == action_module._execute_module(task_vars=dict(ansible_check_mode=False))

    # test incorrect args
    action_module = ActionModule(dict(action=dict(foo='bar')), dict(task_name='set_stats'), False, False)
    results["failed"] = True
    results["msg"] = "Invalid options for set_stats: ('foo',)"
    assert results == action_module._execute_module(task_vars=dict(ansible_check_mode=False))

    # test incorrect args

# Generated at 2022-06-13 10:47:36.947836
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(task=dict(), connection=dict(), play_context=dict(), loader=dict(),
            templar=dict(), shared_loader_obj=dict())

# Generated at 2022-06-13 10:47:47.266954
# Unit test for method run of class ActionModule
def test_ActionModule_run():
  import datetime
  module = ActionModule({}, {})
  utctime = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
  ret = module.run(task_vars={'a': 'A'})
  assert(ret == {'_ansible_verbose_always': False, '_ansible_no_log': False, 'ansible_stats': {'per_host': False, 'data': {u'a': u'A', u'time': utctime}, 'aggregate': False}, 'failed': False, 'changed': False})

# Generated at 2022-06-13 10:47:58.805306
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Create a dummy task that will be passed to test object
    class Task:
        def __init__(self):
            self._ds = None
            self._ds = {'args' : {'data' : {'var1' : 'val1'}, 'per_host' : 'yes', 'aggregate' : 'no'}}
            self._ds['action'] = {'name' : 'set_stats'}

    class PluginLoader:
        def __init__(self, base_class):
            self.base_class = base_class

        def get(self, name, *args):
            return getattr(self.base_class, name)(*args)

    import ansible.plugins.action.set_stats

# Generated at 2022-06-13 10:49:45.618105
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor

    loopback = "localhost"
    transport = "local"
    context = PlayContext()
    context._hostvars = {loopback: {}}
    context._host = loopback
    context._connection = transport
    context._play_context = context

    # set up a minimal "playbook"
    task_queue_manager = TaskQueueManager(
        inventory=None,
        variable_manager=None,
        loader=None,
        context=context,
        passwords=None,
        stdout_callback=None
    )

# Generated at 2022-06-13 10:49:53.538190
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # create an action module from the class
    am = ActionModule(None, None)

    # create a task result to store the results
    result = {}

    # set a task with an args hash containing some valid yml data
    args = {'data': {
                'my_users': ['Alice', 'Bob', 'Charlie'],
                'my_numbers': [1, 2, 3, 4, 5]
            },
            'per_host': True
        }
    class Task:
        def __init__(self, args): self.args = args
    am._task = Task(args)

    # call the run method to generate stats
    am.run(None, None)

    # compare the stats data to what we expect

# Generated at 2022-06-13 10:49:54.426489
# Unit test for constructor of class ActionModule
def test_ActionModule():
    my_action_module = ActionModule()

# Generated at 2022-06-13 10:50:03.824440
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.action.set_stats import ActionModule
    from ansible.parsing.vault import VaultLib

    task_vars = {}
    tmp = None
    result = {}

    # Test with aggregate and per_host set to True
    args = {'aggregate': 'True', 'per_host': 'True', 'data': {'test_var': 'test_value'}}
    task = MockTask(args)
    set_mod = ActionModule(task, tmp, task_vars, result)

    set_mod._templar.template = MockTemplar(task_vars, vault_password=None)
    set_mod._templar.template.vars = task_vars

    set_mod.run(tmp, task_vars)

    assert set_mod.TRANSFERS_

# Generated at 2022-06-13 10:50:04.734583
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # TODO: test code
    pass

# Generated at 2022-06-13 10:50:10.513386
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.vars.unsafe_proxy import UnsafeProxy
    from ansible.vars.hostvars import HostVars
    from ansible.executor.play_iterator import PlayIterator
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    from ansible.plugins.loader import add_all_plugin_dirs
    from ansible.plugins.action.set_stats import ActionModule
    from ansible.plugins import module_loader
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.inventory.host import Host


# Generated at 2022-06-13 10:50:19.573079
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    def execute_task(args=None, blocks=None, task_vars=None, loader=None, templar=None, shared_loader_obj=None):
        action = ActionModule(task=None, connection=None, play_context=None, loader=loader, templar=templar,
                              shared_loader_obj=shared_loader_obj)
        action._task = MockTask(args=args, blocks=blocks, task_vars=task_vars)
        return action.run(task_vars=task_vars)

    class MockLoaderObj:
        def get_basedir(self, conn=None, task=None, variables=None, **kwargs):
            return 'fake-basedir'


# Generated at 2022-06-13 10:50:23.313146
# Unit test for constructor of class ActionModule
def test_ActionModule():
    try:
        from ansible.plugins.loader import action_loader
    except:
        action_loader = None

    a = action_loader.get('set_stats', task=dict(action='set_stats'), connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert(type(a).__name__ == 'ActionModule')

# Generated at 2022-06-13 10:50:29.820331
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Expected: ansible.plugins.action.set_stats.ActionModule()
    mod = ActionModule()
    assert mod._task.action == 'set_stats'
    assert mod.TRANSFERS_FILES is False
    assert mod._VALID_ARGS == frozenset(('aggregate', 'data', 'per_host'))


# Generated at 2022-06-13 10:50:38.748510
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import collections
    import pytest

    test_args = {'data':{}}

    # empty test case
    def empty():
        a = ActionModule({})

        # empty test case
        def empty():
            a = ActionModule({'_ansible_no_log': False})
            assert a.run(None, None)['ansible_stats'] == {'data': {}, 'per_host': False, 'aggregate': True}

        # test case with good data
        def good():
            a = ActionModule({'_ansible_no_log': False})
            assert a.run(None, None, test_args)['ansible_stats'] == {'data': {}, 'per_host': False, 'aggregate': True}
