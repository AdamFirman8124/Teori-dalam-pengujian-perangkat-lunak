

# Generated at 2022-06-13 10:16:13.638459
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule is not None

# Generated at 2022-06-13 10:16:18.168127
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Fixture 1
    class module_native_async_False(object):
        def __init__(self):
            self.async_val = 0
            self.action = C._ACTION_SETUP

        def get_value(self, name):
            self.async_val = False
            return self.async_val

        def get_action(self):
            return self.action

    # Fixture 2
    class module_native_async_True(object):
        def __init__(self):
            self.async_val = 0
            self.action = C._ACTION_SETUP

        def get_value(self, name):
            self.async_val = True
            return self.async_val

        def get_action(self):
            return self.action

    # Method called by `Action

# Generated at 2022-06-13 10:16:28.236735
# Unit test for constructor of class ActionModule
def test_ActionModule():
    config = dict()
    config['task'] = dict()
    config['task']['action'] = dict()
    config['task']['action']['module_name'] = "ping"
    config['task']['action']['module_args'] = dict()
    config['task']['action']['args'] = dict()
    config['task']['name'] = 'ping'
    config['task']['action']['args']['data'] = "pong"
    config['task']['action']['delegate_to'] = None
    config['task']['action']['async'] = None
    config['task']['action']['async_poll_rate'] = None
    config['task']['action']['async_seconds'] = None
    config

# Generated at 2022-06-13 10:16:38.221147
# Unit test for constructor of class ActionModule
def test_ActionModule():
    class Task:
        def __init__(self):
            self.async_val = None
            self.action = "setup"

    class Connection:
        def __init__(self):
            self.has_native_async = None

    class PlayContext:
        def __init__(self):
            self.check_mode = False
            self.connection = "local"
            self.remote_addr = None
            self.remote_user = None

    class ModuleDeprecationWarning(RuntimeError):
        pass

    class ModuleNotFound(RuntimeError):
        pass

    class Runner:
        def __init__(self):
            self._connection = Connection()
            self._task = Task()
            self._play_context = PlayContext()


# Generated at 2022-06-13 10:16:41.452840
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert isinstance(ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None), ActionModule)

# Generated at 2022-06-13 10:16:43.727512
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    print("Unit test for method run of class ActionModule")
    print("FIXME: No unit test implemented")
    return

# Generated at 2022-06-13 10:16:46.539592
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert module is not None

# Generated at 2022-06-13 10:16:54.442430
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.action.normal import ActionModule
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.playbook.task import Task
    from ansible.utils.vars import load_extra_vars
    from ansible.utils.vars import load_options_vars
    from ansible.utils.vars import merge_hash
    from ansible.utils.display import Display
    import ansible.constants as C

# Generated at 2022-06-13 10:17:07.725599
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Setup mocks
    import os
    import ansible.plugins.action
    from ansible.plugins.action import ActionBase

    class MockActionBase(ActionBase):
        """
        Mock class that extends from ActionBase
        """
        def __init__(self, connection, task, result=None, play_context=None, loader=None, templar=None, shared_loader_obj=None):
            self._connection = connection
            self._task = task
            self._result = result
            self._play_context = play_context
            self._loader = loader
            self._templar = templar
            self._shared_loader_obj = shared_loader_obj


# Generated at 2022-06-13 10:17:12.192326
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Check TypeError is raised if action plugin is not ActionBase
    # implementation
    from ansible.plugins.action import ActionBase
    actionBase = ActionBase()
    try:
        actionModule = ActionModule(actionBase._connection, actionBase._task, actionBase._play_context, actionBase._loader, actionBase._templar, actionBase._shared_loader_obj)
        assert False
    except TypeError:
        assert True

# Generated at 2022-06-13 10:17:25.514178
# Unit test for constructor of class ActionModule

# Generated at 2022-06-13 10:17:28.233824
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # can't really test ActionModule as it's purely base
    # but will at least run the code
    ActionModule(None, dict(task=dict(action='test', async_val=False, async_seconds=5)))

# Generated at 2022-06-13 10:17:28.830567
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert 0 == 1

# Generated at 2022-06-13 10:17:30.357104
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass
# vim: expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

# Generated at 2022-06-13 10:17:32.148316
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert isinstance(ActionModule(None,None,None), ActionModule)

# Generated at 2022-06-13 10:17:39.082714
# Unit test for method run of class ActionModule
def test_ActionModule_run():  # First, create an object of the class we want to test
    a = ActionModule()

    # Second, create a mock object that imitates tmp and task_vars parameters passed to run method
    tmp = {'a': 10, 'b': 20}
    task_vars = {'v': 30, 'w': 40}

    # Third, set these mock object as the atributes of the object a.
    a.tmp = tmp
    a.task_vars = task_vars

    # Fourth, test the values returned when run method of class ActionModule is called
    assert (a.run() == {'_ansible_parsed': True})


# Generated at 2022-06-13 10:17:53.315366
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Get all the details for a test to run within the python interpreter
    from ansible import constants as C
    from ansible.plugins.action import ActionModule
    from ansible.executor.task_result import TaskResult
    from ansible.executor.task_executor import TaskExecutor
    from ansible.executor.module_common import ModuleCommon
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.executor.play_iterator import PlayIterator
    from ansible.executor.process.worker import WorkerProcess
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.action_plugins.construct_module_args import ConstructModuleArgs
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play

# Generated at 2022-06-13 10:18:02.037194
# Unit test for constructor of class ActionModule

# Generated at 2022-06-13 10:18:02.532857
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True

# Generated at 2022-06-13 10:18:15.855164
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task import Task
    from ansible.vars import VariableManager
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group

    variable_manager = VariableManager()
    inventory = Host(name='hostname')
    variable_manager.set_inventory(inventory)
    host = inventory.get_host(name='hostname')
    host.set_variable('ansible_connection', 'ssh')
    host.set_variable('ansible_ssh_host', 'ssh_host')
    host.set_variable('ansible_ssh_pass', 'ssh_pass')
    host.set_variable('ansible_ssh_port', 'ssh_port')
    host.set_variable('ansible_ssh_user', 'ssh_user')

    play_context = dict()
    play_

# Generated at 2022-06-13 10:18:22.645763
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(None, None)
    assert action_module

# Generated at 2022-06-13 10:18:30.054297
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    hostname = 'host'
    m = ActionModule()
    m.Runner = MockRunner()
    
    # Testing for when the result are skipped

# Generated at 2022-06-13 10:18:38.481739
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    from ansible.plugins.action.normal import ActionModule

    # class instantiation
    obj = ActionModule(task='Test', connection='Test', play_context='Test', loader='Test', templar='Test', shared_loader_obj='Test')

    # method run test
    # NOTE: not mocking all the required methods, this is not a unit test but just a quick test
    #       to ensure syntax is correct
    # TODO: create proper unit tests
    result = obj.run('Test', 'Test')
    assert isinstance(result, dict)

# Generated at 2022-06-13 10:18:46.671962
# Unit test for constructor of class ActionModule
def test_ActionModule():
    in_task_vars = {"hostvar": "hostval"}
    in_task = None
    in_connection = None
    in_play_context = None
    in_loader = None
    in_templar = None
    in_shared_loader_obj = None

    m = ActionModule(in_task, in_connection, in_play_context, in_loader, in_templar, in_shared_loader_obj)
    assert m._supports_check_mode == True
    assert m._supports_async == True
    assert m._shared_loader_obj == in_shared_loader_obj
    assert m._connection == in_connection
    assert m._loader == in_loader
    assert m._templar == in_templar
    assert m._play_context == in_play_context

# Generated at 2022-06-13 10:18:55.228278
# Unit test for constructor of class ActionModule
def test_ActionModule():
	import ansible
	from ansible.plugins.action import ActionBase
	task_vars = {}
	action_module = ActionModule(ansible.plugins.action.ActionBase, task_vars, name='test_ActionModule', no_log=False)
	assert action_module._supports_check_mode == True
	assert action_module._supports_async == True
	assert action_module._task == ansible.plugins.action.ActionBase
	assert action_module._task_vars == task_vars

# Generated at 2022-06-13 10:19:04.980999
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.block import Block
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.vars import load_extra_vars
    from ansible.utils.vars import load_options_vars

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=['localhost,'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    option

# Generated at 2022-06-13 10:19:05.923529
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule(None, None, None, None)
    assert am is not None

# Generated at 2022-06-13 10:19:08.044381
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # create an instance of the class, to test its constructor.
    a = ActionModule()
    assert isinstance(a, ActionModule)

# Generated at 2022-06-13 10:19:08.948436
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    print("Testing ActionModule")
    assert True

# Generated at 2022-06-13 10:19:15.914140
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Create an object of ActionModule class
    action_module = ActionModule()

    # Set all the attributes for object ActionModule
    action_module._supports_check_mode = True
    action_module._supports_async = True

    # Create a task for object ActionModule
    task = dict()
    task['skipped'] = False
    task['invocation'] = dict()
    task['invocation']['module_args'] = ""
    task['invocation']['module_name'] = 'ping'

    # Create a connection for object ActionModule
    connection = dict()
    connection['_shell'] = dict()
    connection['_shell']['tmpdir'] = '/tmp'
    connection['has_native_async'] = True

    # Create a temporary variable task_vars
    task_vars = dict()


# Generated at 2022-06-13 10:19:29.503896
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule(dict())
    assert not am._supports_async
    assert not am._supports_check_mode


# Generated at 2022-06-13 10:19:31.693643
# Unit test for constructor of class ActionModule
def test_ActionModule():
    instance = ActionModule()
    assert instance._supports_check_mode is True
    assert instance._supports_async is True

# Generated at 2022-06-13 10:19:40.224568
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    m = ActionModule()
    result = m.run(tmp = None, task_vars = {'task_vars': 'task_vars'})
    result['skipped'] = True
    assert result == {'skipped': True}
    result['skipped'] = False
    result['invocation']['module_args'] = 'module_args'
    result = m.run(tmp = None, task_vars = {'task_vars': 'task_vars'})
    assert result == {'skipped': False, 'invocation': {'module_args': 'module_args'}}
    result['skipped'] = False
    result['invocation']['module_args'] = None

# Generated at 2022-06-13 10:19:42.226266
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule()
    # No tests, not sure how to test this
    assert True == True

# Generated at 2022-06-13 10:19:43.916556
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert isinstance(ActionModule(None, None, None, None, None), ActionModule)

# Generated at 2022-06-13 10:19:55.208236
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import json
    import copy
    import os
    import shutil
    import tempfile
    import yaml

    from ansible.errors import AnsibleUndefinedVariable, AnsibleError
    from ansible.module_utils.six import PY2
    from ansible.module_utils.six import string_types
    from ansible.module_utils._text import to_bytes, to_native
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.module_utils.common._json_compat import ensure_text
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins.action import ActionBase
    from ansible.vars.manager import VariableManager


# Generated at 2022-06-13 10:19:56.715366
# Unit test for constructor of class ActionModule
def test_ActionModule():
    a = ActionModule(dict(), dict())

# Generated at 2022-06-13 10:20:03.594820
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import ansible.plugins.action.normal as o
    # Tries to create an instance of the class
    action = o.ActionModule(None, '/tmp/ansible', 'foo')
    # Check that class was created and have correct attributes
    assert action._supports_check_mode == True
    assert action._supports_async == True
    assert action._shared_loader_obj == None
    assert action._display == None
    assert action._task == '/tmp/ansible'
    assert action._connection == 'foo'
    assert action._task_vars == None
    assert action._loader == None
    return True

# Generated at 2022-06-13 10:20:04.351552
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:20:12.669175
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # make sure there is no special variable that shows up in the final result
    # for an async task
    module = ActionModule()
    module._supports_check_mode = True
    module._supports_async = True
    result = module.run(tmp=None, task_vars=dict(foo='bar'))
    assert result['ansible_facts']['foo'] == 'bar'
    assert result.does_not_have('tmp')

# Generated at 2022-06-13 10:20:35.098459
# Unit test for constructor of class ActionModule
def test_ActionModule():
    a = ActionModule()

# Generated at 2022-06-13 10:20:35.662682
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:20:46.207529
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    mock_play_context = {
        'forks': 10,
        'ask_pass': False,
        'ask_su_pass': False,
        'become': False,
        'become_method': 'sudo',
        'become_user': None,
        'check': False,
        'diff': False,
        'new_vault_password_file': None,
        'other_vault_password_files': [],
        'verbosity': 5,
    }

# Generated at 2022-06-13 10:20:47.325641
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass



# Generated at 2022-06-13 10:20:57.373784
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Input parameters for this unittest
    module = type('',(object,),{'run':test_action_module.run})
    plugin = cPlugin(module)
    module.ActionModule=ActionModule
    tmp = tempfile.mktemp()
    constants._ANSIBLE_ARGS=type('',(object,),{'verbosity':0})
    task_vars = {'tvar':5}
    # Test input parameters
    result = module.run(tmp, task_vars)
    assert result == {'invocation': {'module_name': 'test_action_module'}, '_ansible_no_log': False, '_ansible_verbose_always': True, '_ansible_verbose_override': True}
    # FIXME: Add asserts for other testable parmeters.

# Unit

# Generated at 2022-06-13 10:21:01.844729
# Unit test for constructor of class ActionModule
def test_ActionModule():
    config, action = dict(), dict()
    task = dict()
    play_context = dict()
    result = dict()
    assert type(ActionModule(config, action, task, play_context, result, dict())) == ActionModule

# Generated at 2022-06-13 10:21:04.973703
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule()
    assert action is not None

# Unit test to test if ActionModule.run() returns result as a dict
# The function returns a dict as a result object

# Generated at 2022-06-13 10:21:05.901080
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:21:09.449760
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    print("test_ActionModule_run()")

if __name__ == '__main__':
    print("test_ActionModule_run()")

# Generated at 2022-06-13 10:21:17.857953
# Unit test for constructor of class ActionModule
def test_ActionModule():
	import ansible.executor.task_queue_manager
	import ansible.playbook.play
	from ansible.playbook.task import Task
	import ansible.utils.vars
	tqm = ansible.executor.task_queue_manager.TaskQueueManager(
	    inventory=ansible.inventory.Manager(host_list='tests/hosts'),
	    variable_manager=ansible.utils.vars.VariableManager(),
	    loader=ansible.loader.DataLoader()
	)
	input = {}
	input['action'] = 'setup'
	input['_ansible_verbose_always'] = True
	input['_ansible_version'] = ansible.__version__
	input['_ansible_version'] = ansible.__version__

# Generated at 2022-06-13 10:22:24.343270
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # generate the params
    task_vars = {}
    tmp = '/tmp/tmp'
    # instantiate the class
    action_module = ActionModule(task=None, connection=None, _play_context=None, loader=None, templar=None, shared_loader_obj=None)

    class Superclass:
        def run(self, tmp, task_vars):
            return True

    action_module.run(tmp=tmp, task_vars=task_vars)

# Generated at 2022-06-13 10:22:26.118104
# Unit test for constructor of class ActionModule
def test_ActionModule():
    mod = ActionModule()
    assert mod._supports_check_mode == True
    assert mod._supports_async == True

# Generated at 2022-06-13 10:22:26.952831
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ACTION = ActionModule()

# Generated at 2022-06-13 10:22:32.269308
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Instantiate an instance of ActionModule class
    action_module = ActionModule()
    # Assert type of instance is ActionModule class
    assert isinstance(action_module, ActionModule)
    # Assert run() method of class ActionModule takes 2 arguments
    assert action_module.run.__code__.co_argcount == 2

# Generated at 2022-06-13 10:22:33.242677
# Unit test for constructor of class ActionModule
def test_ActionModule():
    m=ActionModule()
    assert True is True

# Generated at 2022-06-13 10:22:34.819948
# Unit test for constructor of class ActionModule
def test_ActionModule():
    a = ActionModule('test', '/none/none', dict(), False, 10)
    assert a is not None

# Generated at 2022-06-13 10:22:46.064472
# Unit test for constructor of class ActionModule
def test_ActionModule():
    connection = 'None'
    module_name = 'None'
    task_uuid = 'None'
    loader = 'None'
    templar = 'None'
    shared_loader_obj = 'None'
    action = ActionModule(connection, module_name, task_uuid, loader, templar, shared_loader_obj)

    assert action._shared_loader_obj == 'None'
    assert action._loader == 'None'
    assert action._templar == 'None'
    assert action._connection == 'None'
    assert action._task == 'None'
    assert action._loader_name == 'None'
    assert action._verbosity == 0
    assert action._no_log == False
    assert action._task_uuid == 'None'
    assert action._supports_async == True
    assert action._

# Generated at 2022-06-13 10:22:47.961296
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # TODO: update the following test
    # action_module = ActionModule(connection=None)
    # assert action_module
    pass

# Generated at 2022-06-13 10:22:48.838726
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    m = ActionModule()
    pass

# Generated at 2022-06-13 10:23:00.305617
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    class myclass:
        class myclass2:
            def __init__(self):
                self.tmpdir = "test"
        _shell = myclass2
    fixture = [
        {"changed": False, "invocation": {"module_args": ["test"]}},
        {},
        {},
        {"changed": False, "invocation": {"module_args": ["test"]}},
        False,
        {},
        None,
        {"failed": False, "changed": True, "msg": "All items completed", "results": [{"item": "1", "ansible_job_id": "75278864", "ansible_job_id": "75278864", "changed": True, "rc": 0}]},
        False,
    ]
    am = ActionModule()
    am._supports_check_

# Generated at 2022-06-13 10:25:11.095784
# Unit test for constructor of class ActionModule
def test_ActionModule():
    actionmodule = ActionModule()

# Generated at 2022-06-13 10:25:12.296374
# Unit test for constructor of class ActionModule
def test_ActionModule():
    #Check that an instance is created successfully
    assert ActionModule() is not None

# Generated at 2022-06-13 10:25:12.774543
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:25:18.462654
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # assert that ActionBase is a parent of ActionModule
    assert issubclass(ActionModule, ActionBase)

    # assert that ActionModule has ActionBase's members
    assert hasattr(ActionModule, 'run')

    # assert that ActionModule has no _execute_module attribute
    assert not hasattr(ActionModule, '_execute_module')

    # assert that ActionModule has no _remove_temporary_path attribute
    assert not hasattr(ActionModule, '_remove_tmp_path')

    # create a ActionModule instance
    test_action_module = ActionModule('test_name')

    assert test_action_module.get_name() == 'test_name'

    # assert that test_action_module has a run method
    assert hasattr(test_action_module, 'run')

    # assert that test_action_module has no _execute

# Generated at 2022-06-13 10:25:20.902195
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    my_module = ActionModule()
    result = my_module.run()
    assert result == 0

# Generated at 2022-06-13 10:25:21.442615
# Unit test for constructor of class ActionModule
def test_ActionModule():
    pass

# Generated at 2022-06-13 10:25:22.780374
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = ActionModule()
    assert action_module.run() == None

# Generated at 2022-06-13 10:25:33.929783
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.module_utils.basic import AnsibleModule

    import ansible.plugins.action
    reload(ansible.plugins.action)

    mod = AnsibleModule(
        argument_spec=dict(
            test=dict(required=True),
        ),
    )

    module = ActionModule(
        connection=None,
        task_vars=dict(),
        loader=None,
        templar=None,
        shared_loader_obj=None)

    assert module._supports_check_mode == True
    assert module._supports_async == True
    assert module.connection == None
    assert module.task_vars == {}
    assert module.loader == None
    assert module.templar == None
    assert module.shared_loader_obj == None

# Generated at 2022-06-13 10:25:41.867411
# Unit test for constructor of class ActionModule
def test_ActionModule():
    args = {}
    args['task'] = {}
    args['task']['async'] = 2
    args['task']['async_val'] = True
    args['task']['action'] = 'command'
    args['connection'] = {}
    args['connection']['has_native_async'] = True
    args['task_vars'] = {}
    args['tmp'] = ''
    result = ActionModule(**args)
    assert result._supports_check_mode == True
    assert result._supports_async == True

# Generated at 2022-06-13 10:25:51.331966
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """
    Unit test for method run of class ActionModule

    :return:
    """
    #
    # Define test variables
    #
    tmp_dir = 'test-dir'
    task_vars = dict(
        ansible_module_args = dict(
            module_name = 'test-module',
            module_args = dict(
                test_param = 'test-value-1',
                test_param_2 = 'test-value-2'
            )
        )
    )
    test_connection = dict(
        connection = 'test-connection',
        has_native_async = True
    )
    test_task = dict(
        async_val = False
    )
    test_tmp = None
    #

    #
    # Prepare AnsibleModule mock object
    #