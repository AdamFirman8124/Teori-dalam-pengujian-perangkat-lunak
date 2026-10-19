

# Generated at 2022-06-13 10:16:14.469355
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule()
    # move to aa test module
    module._supports_check_mode = True
    module._supports_async = True

    # First test - check results when skipped
    result = {'skipped': True}

    # call the code
    result = module.run(tmp=None, task_vars=None)

    # Did we get a success return?
    assert result == {}, 'ActionModule.run did not return a valid result for skipped'

    # Second test - check results when not skipped
    result = {'skipped': False, 'invocation': {'module_args': 'module_args_value'}}

    # call the code
    result = module.run(tmp=None, task_vars=None)

    # Did we get a success return?

# Generated at 2022-06-13 10:16:15.655829
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule(None, None)


# Generated at 2022-06-13 10:16:25.215883
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import ansible.plugins.loader
    import ansible.plugins.action

    l = ansible.plugins.loader.ActionModuleLoader()
    c = l.get('command')

    test_task_data = {
        'args': {'_raw_params': 'uptime'},
        'no_log': False,
        'register': 'shell_out'
    }

    test_task_data_no_log = {
        'args': {'_raw_params': 'uptime'},
        'no_log': True,
        'register': 'shell_out'
    }


# Generated at 2022-06-13 10:16:27.058096
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # instantiate ActionModule
    module = ActionModule()
    assert isinstance(module, ActionModule)

# Generated at 2022-06-13 10:16:37.241060
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.plugins.loader import action_loader
    import ansible.playbook.task as task
    import ansible.playbook.play as playbook
    import ansible.executor.task_queue_manager as executor
    import ansible.executor.playbook_executor as pl
    import ansible.inventory.manager as inventory
    import ansible.vars.manager as v
    
    MockModule = type('MockModule', (object,), {})
    
    action_module = action_loader.get('test')
    assert isinstance(action_module, ActionModule)
    assert action_module._supports_check_mode is True
    assert action_module._supports_async is True

    
    task = executor.TaskQueueManager()

# Generated at 2022-06-13 10:16:46.079458
# Unit test for constructor of class ActionModule
def test_ActionModule():
    print("testing ActionModule constructor")
    # create a test task object
    task = Task()
    # create test connection object
    connection = Connection()
    # create test action plugin object
    plugin = ActionModule(task,connection)
    # assert that the object we created is an instance of the ActionModule class
    assert isinstance(plugin,ActionModule)
    # assert that the object we created is an instance of the ActionBase class
    assert isinstance(plugin,ActionBase)


# test_ActionModule()


# Generated at 2022-06-13 10:16:47.068149
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action = ActionModule(None)

# Generated at 2022-06-13 10:16:53.222229
# Unit test for constructor of class ActionModule
def test_ActionModule():
    try:
        myaction = ActionModule()
        myaction._supports_check_mode = True
        myaction._supports_async = True
        myaction.connection._shell.tmpdir = 'mydir'
        myaction._execute_module(task_vars={})
        myaction.run(tmp={}, task_vars={})
        myaction._remove_tmp_path(myaction.connection._shell.tmpdir)

    except Exception as e:
        raise AssertionError('ActionModule exception: %s' % str(e))


if __name__ == '__main__':
    test_ActionModule()

# Generated at 2022-06-13 10:16:53.690590
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert(ActionModule)

# Generated at 2022-06-13 10:17:04.265290
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Create a fake task
    class Task:
        async_val = None
        action = 'setup'
    task = Task()

    # Create a fake connection and _shell object
    class FakeConnection:
        has_native_async = False
        def __init__(self):
            self._shell = FakeShell()
    connection = FakeConnection()

    # Create a fake shell and tmpdir object
    class FakeShell:
        tmpdir = '/tmp'

    # Create an _execute_module object
    task_vars = dict()
    wrap_async = False
    def _execute_module(self, task_vars, wrap_async):
        return task_vars
    setattr(ActionModule, '_execute_module', _execute_module)

    # Create a remove_tmp_path object

# Generated at 2022-06-13 10:17:15.372654
# Unit test for constructor of class ActionModule
def test_ActionModule():
    mock_task = dict(
        async_val=0,
        async_seconds=0,
        action='shell',
        register='shell_out'
    )
    mock_task['action'] = 'shell'
    mock_task['register'] = 'shell_out'
    mock_task['async'] = 0
    mock_task['async_seconds'] = 0
    mock_task['async_poll_interval'] = 1
    assert isinstance(mock_task, dict)
    assert 'async_val' in mock_task
    assert 'async_seconds' in mock_task
    assert 'action' in mock_task
    assert 'register' in mock_task
    assert 'async' in mock_task
    assert 'async_seconds' in mock_task

# Generated at 2022-06-13 10:17:17.070382
# Unit test for constructor of class ActionModule
def test_ActionModule():
    actionModule = ActionModule()
    assert actionModule
    assert actionModule.action_type is 'normal'

# Generated at 2022-06-13 10:17:20.046405
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(ActionBase._shared_loader_obj, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert module is not None

# Generated at 2022-06-13 10:17:21.044719
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # TODO: Implement this unit test
    assert False

# Generated at 2022-06-13 10:17:30.640427
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(name='Task', connection=None, task=None, on_unreachable=None, on_no_log_passthru=None, on_localhost=None, runner_on_ok=None, runner_on_failed=None, runner_on_unreachable=None, runner_on_no_hosts=None, runner_on_async_poll=None, runner_on_async_ok=None, runner_on_async_failed=None, runner_on_file_diff=None, loader=None, variable_manager=None, loading_basedir=None)
    assert action_module._supports_check_mode == True
    assert action_module._supports_async == True
    assert action_module._incremental_results == False

# Generated at 2022-06-13 10:17:31.915871
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(task=None)

# Generated at 2022-06-13 10:17:36.542366
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Variables
    class Ansible():
        class Connection():
            has_native_async = True
        task = Ansible()
    ansible = Ansible()
    # Class instance
    x = ActionModule(ansible, '', '', '', '', 'setup')
    # Test return value
    assert x.run() == {}

# Generated at 2022-06-13 10:17:44.363413
# Unit test for constructor of class ActionModule
def test_ActionModule():
    task_vars = dict(
        ansible_ssh_host = "127.0.0.1",
    )
    tmp = "/tmp"
    module_name = "ping"
    module_args = dict(
        data = "pong",
    )
    class connection:
        def has_native_async(self):
            return False
    class task:
        async_val = 10
        action = "ping"
        def __init__(self):
            self.connection = connection()
    am = ActionModule(task, connection, tmp, module_name, module_args, task_vars)
    am.run(tmp, task_vars)

# Generated at 2022-06-13 10:17:56.768751
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    class MockActionPlugin:
        def __init__(self,task):
            self._task = task
            self._task.async_val = None
            self._task.action = 'setup'
            self._task.action_plugin = 'setup'
            self._task._connection = None
            self._task._queue_name = None
            self._task.noop_val = None
            self._task.notify = None
            self._task.task_include = None
            self._task.loop = None
            self._task.tags = None
            self._task.when = None

        def run(self,*args,**kwargs):
            return 'do run'

    class MockTask:
        def __init__(self):
            self.name = 'setup'
            self.async_val = None

# Generated at 2022-06-13 10:18:04.630315
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.play_context import PlayContext
    x = PlayContext()
    x._docker_host = True
    x._remote_uid = 22
    x._remote_user = 'root'
    x.network_os = 'ios'
    x.remote_addr = '127.0.0.1'
    x.connection = 'docker'
    y = ActionModule(x)
    assert y.get_view_name() == 'action'
    assert y.get_option('docker_host') == True
    assert y.get_option('remote_uid') == 22
    assert y.get_option('remote_user') == 'root'
    assert y.get_option('network_os') == 'ios'
    assert y.get_option('remote_addr') == '127.0.0.1'


# Generated at 2022-06-13 10:18:12.740127
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule(None, None)
    assert am._supports_check_mode == True
    assert am._supports_async == True

# Generated at 2022-06-13 10:18:21.697756
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Different values of _connection variable is tested.
    #
    # - if _connection.has_native_async == True, self._execute_module has wrap_async=False
    # - if _connection.has_native_async == False, self._execute_module has wrap_async=True
    #
    # Cases for each:
    #
    # async_val | has_native_async | wrap_async
    #       true|            true|      false
    #       true|           false|       true
    #      false|            true|      false
    #      false|           false|      false

    # setup
    class dummy_connection():
        def __init__(self, has_native_async):
            self.has_native_async = has_native_async

# Generated at 2022-06-13 10:18:25.831256
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins.loader import connection_loader
    module = ActionModule(
            task=PlayContext(),
            connection=connection_loader.get('local', PlayContext(), '/dev/null'),
            _shared_loader_obj=None
    )

    assert module is not None, "ActionModule() failed"

# Generated at 2022-06-13 10:18:30.467979
# Unit test for constructor of class ActionModule
def test_ActionModule():
    result = {"invocation" : {"module_args" : "test_module_args"}}

    action_plugin = ActionModule()
    updated_result = action_plugin.run(None, result)
    assert updated_result['invocation'] == {}
    assert updated_result['invocation'] != result["invocation"]

    action_plugin = ActionModule()
    updated_result = action_plugin.run(None, result)
    assert updated_result['invocation'] == {}
    assert updated_result['invocation'] != result["invocation"]

# Generated at 2022-06-13 10:18:36.188008
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.action.normal import ActionModule
    import pytest
    am = ActionModule(None, None, None)
    result = am.run(None, None)
    assert isinstance(result, dict)
    assert result.get('skipped') is None
    assert result.get('invocation') is None
    assert result == {}


# Generated at 2022-06-13 10:18:42.324978
# Unit test for constructor of class ActionModule
def test_ActionModule():
    mock_task = dict(action='test')
    mock_connection = dict(play_context=dict(remote_addr='3.3.3.3'))
    a = ActionModule(mock_task, mock_connection)
    assert a.task == mock_task
    assert a.connection == mock_connection
    assert a._supports_check_mode is True
    assert a.add_path == []

# Generated at 2022-06-13 10:18:48.581842
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Test an invalid module_name
    am1 = ActionModule()
    assert am1.run(None, None) == {'failed': True}

    # Test a valid module
    am2 = ActionModule()
    am2.name = 'ping'
    assert am2.run(None, {'inventory_hostname': '127.0.0.1'})['ping'] == 'pong'



# Generated at 2022-06-13 10:18:57.728876
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import pickle
    import ansible.plugins.action

    action_module = ansible.plugins.action.ActionModule(
        {},
        'test')

    action_module._remote_modname = 'fake'
    action_module._supports_check_mode = True
    pickled = pickle.dumps(action_module)
    del action_module

    action_module_new = pickle.loads(pickled)

    assert action_module_new._remote_modname == 'fake'
    assert action_module_new._supports_check_mode is True

# Generated at 2022-06-13 10:19:07.673639
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    m = ActionModule()
    m.task = 't'
    m._task = 'm._task'
    m.connection = 'c'
    m._connection = 'm._connection'
    m.tmp = 't'
    m.task_vars = 'tv'
    m._execute_module = lambda task_vars, wrap_async: {'wrap_async': wrap_async, 'task_vars': task_vars}

    m._connection._shell.tmpdir = 'tmpdir'
    m._connection.has_native_async = lambda: False

    m._task.async_val = 0
    assert m.run(tmp='t', task_vars='tv') == {'wrap_async': False, 'task_vars': 'tv'}

    m._task.async_

# Generated at 2022-06-13 10:19:15.099906
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import os
    import tempfile
    import shutil
    import sys
    import stat
    import signal
    import time
    import ansible.utils.template as template
    import ansible.utils.vars as vars
    import ansible.utils.module_docs as module_docs
    import ansible.utils.unicode as Unicode
    import json
    from ansible.plugins.action import ActionBase
    from ansible.compat import selectors

    t1 = tempfile.mkdtemp(dir='/tmp')
    t2 = tempfile.mkdtemp(dir='/tmp')


# Generated at 2022-06-13 10:19:29.504640
# Unit test for constructor of class ActionModule
def test_ActionModule():
    x = ActionModule(
        name='testaction',
        args={'test':'testarg'}
    )
    assert x.name == 'testaction'
    assert x.args['test'] == 'testarg'

# Generated at 2022-06-13 10:19:30.093499
# Unit test for method run of class ActionModule
def test_ActionModule_run():
	assert True

# Generated at 2022-06-13 10:19:39.098724
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module_name = "test_module"
    action_file = "../../plugins/actions/copy.py"

# Generated at 2022-06-13 10:19:40.657371
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    test_ActionModule = ActionModule()
    test_ActionModule.ActionModule()
    # test_ActionModule.run()


# Generated at 2022-06-13 10:19:45.389441
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.module_utils._text import to_bytes
    from ansible.plugins.action import ActionModule
    from ansible.plugins.action.normal import ActionModule as ActionModuleNormal
    from ansible.plugins import action_loader

    # Patch built-in open() with our own mock
    import __builtin__ as builtins
    real_open = builtins.open

    def test_open(name, mode='r'):
        if name == '/dev/null':
            raise OSError("mock open() failed")
        else:
            return real_open(name, mode)

    m = action_loader.get("setup", task=dict())
    assert type(m) == ActionModuleNormal

    m = action_loader.get("copy", task=dict(async_val=1))

# Generated at 2022-06-13 10:19:57.263911
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.task import Task
    from ansible.plugins.connection.local import Connection
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    task_vars = dict(ansible_facts=dict(distribution='Ubuntu'))
    result = dict(skipped=False)
    test_inv = InventoryManager(loader=DataLoader(), sources=[])
    test_var = VariableManager(loader=DataLoader(), inventory=test_inv)
    test_loader = DataLoader()

# Generated at 2022-06-13 10:20:04.041367
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    conn = AnsibleConnection(connection_local)  # This represents the connection to the target host.
    obj = ActionModule(task_local, connection_local, tmp=None, module_name=None, module_vars=[], task_vars=None, wrap_async=False, result=None)  # we seem to use this object to magicly know the result of running whatever we are calling
    obj.run(tmp=None, task_vars=None)
    #assert obj.run(tmp=None, task_vars=None) == expected
    raise Exception("Test not implemented")

# Generated at 2022-06-13 10:20:06.133146
# Unit test for constructor of class ActionModule
def test_ActionModule():
    c = ActionModule(None,None)

    assert c is not None

# Generated at 2022-06-13 10:20:12.599132
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Test a case with no parameters
    action = ActionModule()
    result = action.run()
    assert result == dict(
        _ansible_verbose_override=True,
        _ansible_no_log=False,
        _ansible_module_name='setup',
    )

# Test cases for run method of class ActionModule

# Generated at 2022-06-13 10:20:14.029297
# Unit test for constructor of class ActionModule
def test_ActionModule():
   assert ActionModule is not None

# Generated at 2022-06-13 10:20:46.661785
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible import constants as C
    from ansible.plugins.loader import action_loader
    from ansible.plugins.connections.ssh import Connection
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.host import Host, Group
    from units.mock.procenv import swap_stdin_and_argv

    loader = DataLoader()
    options = lambda: None
    options.connection = 'ssh'
    options.module_path = None

# Generated at 2022-06-13 10:20:56.859336
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Create an instance to test
    action = ActionModule({}, {
        'ASK_PASS': False,
        'HOST_KEY_CHECKING': True,
        'PARAMIKO_RECORD_HOST_KEYS': True,
        'REMOTE_USER': 'user',
    })

    # Set up some test data
    class TestModule:
        pass
    setattr(action, '_CHECK_ARGUMENT_TYPES_MAPPING', TestModule())
    setattr(action, '_COMPATIBLE_PLATFORMS', TestModule())
    setattr(action, '_CORE_MODULE_ARGS', TestModule())
    setattr(action, '_LOOKUP_PROMPTS', TestModule())

# Generated at 2022-06-13 10:21:01.304901
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule(task=MockTask(), connection=MockConnection(), play_context=MockPlayContext(),
                      loader=None, templar=None, shared_loader_obj=None)
    assert am is not None


# Generated at 2022-06-13 10:21:01.743702
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert True

# Generated at 2022-06-13 10:21:14.261626
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    from ansible.vars import VariableManager

    module_name = 'test_module'
    loader = 'some_loader'
    play_context = PlayContext()
    play_context.network_os = 'some_network_os'
    play_context.remote_addr = 'some_remote_addr'
    play_context.port = 1234

    task = Task()
    task.action = 'some_action'
    task.async_val = 20
    task.dep_chain = ['test1', 'test2']
    task.notified_by = ['test3', 'test4']
    task.tags = ['tag1', 'tag2']
    task.register = 'some_result'

# Generated at 2022-06-13 10:21:15.290549
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule


# Generated at 2022-06-13 10:21:15.832924
# Unit test for method run of class ActionModule
def test_ActionModule_run():
  pass

# Generated at 2022-06-13 10:21:17.832032
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    mod = ActionModule()
    mod.run(tmp=None, task_vars=None)

# Generated at 2022-06-13 10:21:20.280776
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule()
    assert action is not None
    assert action.__doc__ is not None

# Generated at 2022-06-13 10:21:21.318495
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ActionModule().run()

# Generated at 2022-06-13 10:22:21.339674
# Unit test for constructor of class ActionModule
def test_ActionModule():

    action_module = ActionModule()

    assert action_module is not None

# Generated at 2022-06-13 10:22:22.699475
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # TODO: Fill this in...
    pass

# Generated at 2022-06-13 10:22:34.140786
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    print('Starting test_ActionModule_run')
    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    import ansible.constants as C

    C.HOST_KEY_CHECKING = False
    C.DEFAULT_HOST_LIST = 'localhost'

    mytask = Task()
    mytask._role = None
    mytask.action = 'shell'
    mytask.async_val = 1
    mytask.name = 'test_ActionModule_run'
    mytask.args = dict(free_form='/bin/echo')

    # test executing a module with a return of rc=0
    play_context = PlayContext()

# Generated at 2022-06-13 10:22:34.691274
# Unit test for constructor of class ActionModule
def test_ActionModule():
    pass

# Generated at 2022-06-13 10:22:42.220150
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.task import Task
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_result import TaskResult

    t = Task()
    t._ds = dict(action='command', command='/bin/ls')
    p = Play()
    p._ds = dict(playbook='/tmp/playbook.yml', name='foo')
    p._tasks = [t]
    pc = PlayContext()
    pc._ds = dict(playbook='/tmp/playbook.yml')
    pc._tasks = [t]

    a = ActionModule()
    a._shared_loader_obj = None
    a._task = t
    a._tasks = [t]
    a._play_context = pc

# Generated at 2022-06-13 10:22:50.732065
# Unit test for constructor of class ActionModule
def test_ActionModule():
    def test_init_with_valid_args():
        conn_info = dict(host=dict(port=22))
        loader=dict(path=[])
        variable_manager=dict(host_vars=dict(hostvars=[]))
        temporary_path="test"
        module_name="ping"
        module_args={}
        task=dict(action=module_name, args=module_args, async_val=0)
        task_vars=dict(ansible_connection="local", ansible_ssh_private_key_file="/test/test")
        play_context=dict(become=False)
        action_plugin = ActionModule(conn_info, loader, variable_manager, temporary_path, task, task_vars, play_context)
        assert(action_plugin._conn_info == conn_info)

# Generated at 2022-06-13 10:22:52.741730
# Unit test for constructor of class ActionModule
def test_ActionModule():
    test_action_module = ActionModule()
    assert test_action_module is not None

# Generated at 2022-06-13 10:22:53.795478
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule()
    print()

# Generated at 2022-06-13 10:22:54.493360
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:22:55.106701
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:25:10.362804
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Create a new instance of class with implmented method _execute_module
    # this is based on run of class ActionModule
    action_module = object.__new__(ActionModule)

    # Create new instance of ActionBase class
    action_base = object.__new__(ActionBase)
    # set _task attribute 
    action_base._task = object.__new__(ActionBase)
    # set _task attribute of ActionBase 
    action_base.task = object.__new__(ActionBase)
    # set action attribute of _task to be setup
    action_base._task.action = "setup"

    # set _connection attribute
    action_base._connection = object.__new__(ActionBase)
    # set _shell attribute
    action_base._connection._shell = object.__new__(ActionBase)
    #

# Generated at 2022-06-13 10:25:18.377529
# Unit test for method run of class ActionModule

# Generated at 2022-06-13 10:25:18.994362
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    a = ActionModule()

# Generated at 2022-06-13 10:25:20.118769
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True

# Generated at 2022-06-13 10:25:21.981427
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.action import ActionModule
    m_ansible_action = ActionModule()
    assert True

# Generated at 2022-06-13 10:25:25.341401
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    m = ActionModule()

    result = m._execute_module(task_vars={}, wrap_async=False)
    assert result['rc'] == 0, 'rc should be 0'
    assert result['invocation'] == {'module_name': 'setup'}, 'module_name should be setup'

# Generated at 2022-06-13 10:25:27.290862
# Unit test for constructor of class ActionModule
def test_ActionModule():

        # create instance of ActionModule
    command = ActionModule()

    # Result should be of Class ActionModule
    assert isinstance(command, ActionModule), "Instance is not of type ActionModule"

# Generated at 2022-06-13 10:25:28.971364
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert isinstance(ActionModule(), ActionModule)

# Generated at 2022-06-13 10:25:33.691267
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import sys, ansible.runner.connection_plugins.ssh
    am = ActionModule({'become': True, 'async': 100}, ansible.runner.connection_plugins.ssh,
            '/usr/share/ansible', '', 'action_plugin')
    assert am._task.action == 'action_plugin'



# Generated at 2022-06-13 10:25:44.295503
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils.connection import Connection

    x_ActionModule_run = {
        'invocation': {
            'module_args': "hello world"
        },
        'skipped': False,
        'verbose_override': True,
        '_ansible_verbose_override': True,
        '_ansible_no_log': False,
        '_ansible_delegated_vars': {},
        'changed': True,
        'invocation': {
            'module_name': 'setup',
            'module_args': "hello world"
        },
        '_ansible_item_result': False,
        '_ansible_parsed': True
    }

    a = Connection(module_name='setup')