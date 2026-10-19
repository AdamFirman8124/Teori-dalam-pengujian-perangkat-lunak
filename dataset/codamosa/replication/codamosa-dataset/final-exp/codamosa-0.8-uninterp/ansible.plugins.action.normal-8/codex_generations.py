

# Generated at 2022-06-13 10:16:23.263887
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Unit test for constructor of class ActionModule
    result = {}
    m_task_vars = {}
    m_shell = {}
    m_wrap_async = False
    m_connection = {}
    m_defer_results = False
    m_module_name = ''
    m_module_args = {}
    m_module_lang = ''
    m_module_common_arguments = ''
    m_task_uuid = ''
    m_task_uuid = ''
    m_task_uuid = ''
    m_task_uuid = ''

# Generated at 2022-06-13 10:16:25.436609
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Test case where wrap_async is True
    # action_plugin = ActionModule()
    # result = action_plugin.run()
    pass

# Generated at 2022-06-13 10:16:27.693936
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule()
    assert action._supports_check_mode == True
    assert action._supports_async == True

# Generated at 2022-06-13 10:16:28.592473
# Unit test for constructor of class ActionModule
def test_ActionModule():
    mod = ActionModule()
    assert mod is not None

# Generated at 2022-06-13 10:16:38.533453
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    class FakeRunner:
        def __init__(self):
            self.tmpdir = '/tmp'
    class FakeConn:
        def __init__(self):
            self.runner = FakeRunner()
            self.has_native_async = True
    class FakeTask:
        def __init__(self):
            self.action = 'setup'
            self.async_val = False
            self.connection = FakeConn()
    class FakeModule:
        def __init__(self):
            self._task = FakeTask()
            self._supports_check_mode = True
            self._supports_async = True
            self._connection = FakeConn()
            self._tmp_path = '/tmp'
            self.action = 'setup'
            self.action_plugins = {'setup': '/tmp'}

# Generated at 2022-06-13 10:16:39.923774
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule()
    assert module is not None

# Generated at 2022-06-13 10:16:45.635221
# Unit test for constructor of class ActionModule
def test_ActionModule():
    ansible_mock_action = dict(
        ANSIBLE_MODULE_ARGS=dict(),
        ANSIBLE_MODULE_CONSTANTS=dict(),
        ANSIBLE_MODULE_COMPLEX_ARGS=dict()
    )
    assert isinstance(ActionModule(ansible_mock_action, '/path/to/test'), ActionBase)

# Generated at 2022-06-13 10:16:48.693521
# Unit test for constructor of class ActionModule
def test_ActionModule():
    #All test case for constructor
    obj= ActionModule()
    print(obj)
    print("##############################")
if __name__ == '__main__':
    test_ActionModule()

# Generated at 2022-06-13 10:16:56.020217
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule('test_ActionModule', '_ansible_test', '_connection_test', 'become_test', 'become_user_test', 'no_log_test', 'verbosity_test', '_diff_test')
    assert ActionModule('test_ActionModule', '_ansible_test', '_connection_test', 'become_test', 'become_user_test', 'no_log_test', 'verbosity_test', '_diff_test')._task.action == 'test_ActionModule'
    assert ActionModule('test_ActionModule', '_ansible_test', '_connection_test', 'become_test', 'become_user_test', 'no_log_test', 'verbosity_test', '_diff_test')._task._ansible == '_ansible_test'
    assert ActionModule

# Generated at 2022-06-13 10:16:57.239932
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:17:06.783664
# Unit test for constructor of class ActionModule
def test_ActionModule():
    class Connection():
        def __init__(self):
            self.has_native_async = False

    connection = Connection()
    variable_manager = {}

    class Task():
        def __init__(self):
            self.async_val = False

    task = Task()

    am = ActionModule(connection=connection, variable_manager=variable_manager, task=task)
    assert am.run() == {}

if __name__ == "__main__":
    test_ActionModule()

# Generated at 2022-06-13 10:17:09.718038
# Unit test for constructor of class ActionModule
def test_ActionModule():
   # Check that the return of ActionModule object is an instance of ActionModule
   assert isinstance(ActionModule(), ActionModule)
   # Check that the return of ActionModule object is not an instance of plugins.action.Command
   assert not isinstance(ActionModule(), Command)

# Generated at 2022-06-13 10:17:17.616788
# Unit test for method run of class ActionModule

# Generated at 2022-06-13 10:17:23.283744
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    class MockActionModule(object):
        _supports_check_mode = False
        _supports_async = False
        invocation = {}
        _task = object()
        _connection = object()

        def run(self, tmp=None, task_vars=None):
            pass
        
        def _execute_module(self, task_vars=None, wrap_async=None,):
            pass

        def _remove_tmp_path(self, tmpdir):
            pass

    result = {
        "skipped": False
    }

    mock_task_vars = object()

    module = MockActionModule()
    
    assert module.run(
        tmp=None,
        task_vars=mock_task_vars
    ) == result

# Generated at 2022-06-13 10:17:33.231262
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Initilizing test data
    fake_loader = DictDataLoader({})
    fake_inventory = InventoryManager(loader=fake_loader, sources='localhost,')
    fake_variable_manager = VariableManager(loader=fake_loader, inventory=fake_inventory)
    play_context = PlayContext()
    play_source =  dict(
            name = "Ansible Play",
            hosts = 'localhost',
            gather_facts = 'no',
            tasks = [
                dict(action=dict(module='setup', args=dict()))
            ]
        )
    fake_play = Play().load(play_source, variable_manager=fake_variable_manager, loader=fake_loader)
    fake_task = Task().load(play_source['tasks'][0], play=fake_play)

    # Initializing test object
   

# Generated at 2022-06-13 10:17:33.790866
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert True

# Generated at 2022-06-13 10:17:34.624350
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:17:43.014399
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import ansible.plugins.action as action
    action_module = action.ActionModule()
    _task = dict(action = "This action")
    _play_context = dict(remote_addr = "This is remote address")
    _connection = dict(has_native_async = False)
    _play_context['connection'] = _connection
    action_module._task = _task
    action_module._play_context = _play_context
    action_module._task.async_val = False
    action_module._connection.has_native_async = False
    action_module._connection._shell.tmpdir = "This is a temporary path"
    action_module.run()


# Generated at 2022-06-13 10:17:52.110151
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Check results for run method
    def run_mock(self_param, tmp=None, task_vars=None):
        raise NotImplementedError()

    import mock
    import __builtin__

    with mock.patch.object(ActionModule, 'run', run_mock):
        with mock.patch.object(__builtin__, 'super', lambda x, y: None):
            with mock.patch.object(ActionBase, 'run', run_mock):
                assert(ActionModule().run()) == None

# Generated at 2022-06-13 10:17:58.225791
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Test with a simple module
    result = ActionModule(constants=C).run(tmp=None, task_vars=None)
    assert result.get('skipped') == False
    
    # Test with a module that doesn't exist
    result = ActionModule(constants=C).run(tmp=None, task_vars=None)
    assert result.get('skipped') == False

    # Test with a module that doesn't support check or async
    result = ActionModule(constants=C).run(tmp=None, task_vars=None)
    assert result.get('skipped') == False
    # Test with a module that supports check or async
    result = ActionModule(constants=C).run(tmp=None, task_vars=None)
    assert result.get('skipped') == False

# Generated at 2022-06-13 10:18:04.595303
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert False, "Test not implemented"

# Generated at 2022-06-13 10:18:15.776591
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ModuleRes = { "skipped": False, "invocation": { "module_args": "test" } }
    from ansible.plugins.action.normal import ActionModule
    from ansible.utils.vars import merge_hash

    def _execute_module(task_vars, wrap_async):
        return { "_execute_module": "test" }

    TestAction = ActionModule("test", "test", None, "test", False, False)
    TestAction.run("tmp", "task_vars")
    TestAction.run("tmp", ModuleRes)
    TestAction._execute_module = _execute_module
    print(TestAction.run("tmp", ModuleRes))

# Generated at 2022-06-13 10:18:24.709730
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # sample vars for the test (run in init)
    task_vars = {'ansible_connection': "local",
                 'rsync_src': "/my/files",
                 'rsync_dest': "/other/files",
                 'rsync_port': 22,
                 'rsync_archive': True,
                 'rsync_partial': True,
                 'rsync_progress': True}

    # mock the module loading mechanism.
    module_loader = ActionModule._shared_loader_obj
    ActionModule._shared_loader_obj = DictDataLoader()

    # create the action and the action plugin

# Generated at 2022-06-13 10:18:27.579265
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule is not None
    # Constructor requires a TaskQueueManager
    assert ActionModule(TaskQueueManager=None) is not None

# Generated at 2022-06-13 10:18:39.825446
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ActionModule._remove_tmp_path = lambda self, path: path
    ActionModule._execute_module = lambda self, *args, **kwargs: kwargs
    ActionModule._task = lambda self: {'action': 'setup'}
    ActionModule._connection = lambda self: object()
    ActionModule._connection._shell = lambda self: object()
    ActionModule._connection._shell.tmpdir = 'tmpdir'
    task_vars = {'k': 'v'}
    wrap_async = True


# Generated at 2022-06-13 10:18:43.350074
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    python_version = sys.version_info.major
    if python_version != 2:
        # This function has code which is only applicable to python2, so no point of testing it for other versions.
        return
    else:
        # TODO: Write appropriate test code.
        pass

# Generated at 2022-06-13 10:18:44.969390
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule()
    assert am.run_is_async is False

# Generated at 2022-06-13 10:18:52.559044
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    task_vars = dict()

    tmp = None
    result = dict(skipped=False)
    module = ActionModule(task_vars)
    module._connection = MagicMock()
    module._connection.has_native_async = False
    module._task = MagicMock()
    module._task.async_val = False
    module._remove_tmp_path = MagicMock()

    module.run(tmp, task_vars)

    module._connection._shell.tmpdir = None

    module.run(tmp, task_vars)
    module._connection._shell.tmpdir = None
    module._supports_async = False
    module.run(tmp, task_vars)

    result = dict(skipped=False)
    result['invocation'] = dict()

# Generated at 2022-06-13 10:18:57.640115
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Setting up the necessary parameters for testing constructor of class ActionModule
    module_name = 'test_module'
    task_vars = {'_ansible_no_log': 'ON_FAILURE'}
    connection = 'test_connection'
    play_context = 'test_play_context'
    loader = 'test_loader'

    # Testing ActionModule constructor
    actmod = ansible.plugins.action.ActionModule(
        module_name, task_vars, connection, play_context, loader
    )

    # Checking that the instance created is of type ActionModule
    assert(isinstance(actmod, ansible.plugins.action.ActionModule))

    # Ending testing for constructor of class ActionModule



# Generated at 2022-06-13 10:19:02.355282
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """
    Unit test for constructor of class ActionModule
    """
    my_action = ActionModule(loader=None, task=None, connection=None, play_context=None,
                             shared_loader_obj=None, loader_cache=None)
    assert my_action is not None


# Generated at 2022-06-13 10:19:19.392369
# Unit test for constructor of class ActionModule
def test_ActionModule():
    x = ActionModule()
    assert (x._supports_check_mode == True, "should be True")
    assert (x._supports_async == True, "should be True")
    assert (x.MAX_FAIL_PERCENTAGE == 1, "should be 1")


# Test: Test if the parent class has _supports_check_mode and _supports_async set to True.

# Generated at 2022-06-13 10:19:20.683999
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule({}, {})

# Generated at 2022-06-13 10:19:21.389438
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule()

# Generated at 2022-06-13 10:19:32.087656
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import os
    from ansible.playbook.play_context import PlayContext
    from ansible.executor import task_queue_manager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.plugins.action.normal import ActionModule

    # other test code
    context = PlayContext()
    inventory = InventoryManager(loader=DataLoader(), sources=["localhost"])
    variable_manager = VariableManager(loader=DataLoader(), inventory=inventory)
    loader = DataLoader()


# Generated at 2022-06-13 10:19:39.695916
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Constructor without argument
    task = {
        'action': 'copy',
        'module_name': 'copy',
        'module_args': '',
        'async': 1546278979.912062,
        'async_val': 1546278979.912062,
        'delegate_to': 'localhost',
        'register': 'result'
    }
    am = ActionModule(task, connection='local', play_context={}, loader=None, templar=None, shared_loader_obj=None,
                  variable_manager=None)


if __name__ == '__main__':
    # Unit test will go here
    test_ActionModule()

# Generated at 2022-06-13 10:19:40.169060
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert True

# Generated at 2022-06-13 10:19:41.309787
# Unit test for constructor of class ActionModule
def test_ActionModule():
    a = ActionModule()
    assert isinstance(a, ActionModule)

# Generated at 2022-06-13 10:19:53.451976
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule()
    module._supports_check_mode = True
    module._supports_async = True
    tmp = '/tmp'
    task_vars = {}
    result = {}

    # Test with supports check mode enabled
    result['skipped'] = False
    result['invocation'] = {'module_args': 'Hello'}
    result2 = module.run(tmp, task_vars)
    assert result2['invocation']['module_args'] == result['invocation']['module_args']

    # Test with supports check mode disabled
    module._supports_check_mode = False
    result2 = module.run(tmp, task_vars)
    assert result2['invocation']['module_args'] == result['invocation']['module_args']

    # Test with supports async

# Generated at 2022-06-13 10:19:54.391812
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule is not None

# Generated at 2022-06-13 10:20:03.947587
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # the fields expected to be present in the result
    keys = ['changed', 'warnings', 'skipped', 'stderr', 'stdout', 'stdout_lines', '_ansible_verbose_override']
    # set up the action module to use
    actionModule = ActionModule()

    # set up some dummy task_vars

# Generated at 2022-06-13 10:20:34.241733
# Unit test for method run of class ActionModule

# Generated at 2022-06-13 10:20:39.528906
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # set up the class
    def run(self, tmp=None, task_vars=None):
        return True
    from ansible.plugins.action import ActionBase
    from ansible.plugins.action.normal import ActionModule
    test_class = ActionModule(ActionBase, 'ActionModule', 'normal', 'yaml', None, True)
    test_class.run = run
    assert test_class.run() == True

# Generated at 2022-06-13 10:20:40.424575
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert hasattr(ActionModule, 'run')

# Generated at 2022-06-13 10:20:45.591063
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule()
    module.test_result = {'test_result': 'test_result'}
    result = {'test_result_1': 'test_result_1'}
    tmp = None
    task_vars = {
        'test_task_vars': 'test_task_vars'
    }
    module.run(tmp, task_vars)
    assert result == module.test_result

# Generated at 2022-06-13 10:20:55.609755
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import sys, os
    sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
    import lib.connection as connection
    import lib.action.module_common as module_common

    conn = connection.Connection(module_name='ping')
    action_module = ActionModule(connection=conn, task=None)

    tmp = None
    task_vars = {
        'hostvars': {
            'testhost': {
                'vars': {
                    'test': 'test'
                }
            }
        }
    }

    result = action_module.run(tmp, task_vars)
    # assert result['invocation']['module_name'] == 'ping'
    assert result['_ansible_verbose_override'] is True

# Generated at 2022-06-13 10:20:57.004275
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(None, None, None)

# Generated at 2022-06-13 10:20:59.576790
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """Test ActionModule class"""
    module = ActionModule(task=None)

    # check if module is an instance of ActionBase
    assert isinstance(module, ActionBase)

# Generated at 2022-06-13 10:21:06.507441
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # this is not an actual unit test but is used by the functional tests
    module = ActionModule()
    import os
    class FakeTask(object):
        async_val = False
        action = os.path.basename(__file__)
    class FakeConnection(object):
        def has_native_async(self):
            return False
    class FakeLoader(object):
        pass

    module._remove_tmp_path = lambda x: None
    module._execute_module = lambda x, y: {"foo": "bar"}

    module._task = FakeTask()

    module._loader = FakeLoader()

    module._connection = FakeConnection()


# Generated at 2022-06-13 10:21:07.487595
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert True

# Generated at 2022-06-13 10:21:11.678243
# Unit test for constructor of class ActionModule
def test_ActionModule():
    def _do_test(action_module):
        assert action_module.task_vars == {}
        assert action_module.tmp == {}
        assert action_module.play_context != None


# Generated at 2022-06-13 10:22:20.828646
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.loader import action_loader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.inventory.host import Host
    from ansible.parsing.dataloader import DataLoader
    my_vars = dict(
    )
    inventory = InventoryManager(loader=DataLoader())
    host = Host(name="localhost")
    host.set_variable('ansible_connection', 'local')
    inventory.add_host(host)
    variable_manager = VariableManager(loader=DataLoader(), inventory=inventory)
    variable_manager.extra_vars = my_vars


# Generated at 2022-06-13 10:22:26.055887
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert(callable(ActionModule))

    # No arguments
    try:
        am = ActionModule()
    except:
        assert(False)

    # No arguments
    try:
        am = ActionModule("/tmp")
    except:
        assert(False)


# Generated at 2022-06-13 10:22:29.673984
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    task = Task()
    task.async_val = True
    task.action = 'asdf'
    task.task_vars = {'asdf':1}
    action = ActionModule(task, Connection('localhost'))
    action_result = action.run(tmp='/tmp', task_vars={'asdf':2})
    assert action_result['asdf'] == 2


# Generated at 2022-06-13 10:22:38.568219
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.plugins.loader import connection_loader, action_loader
    from ansible.inventory.host import Host
    from ansible.vars.manager import VariableManager
    from ansible.playbook.task import Task

    host = Host(name="test.example.org")
    t = Task()
    t.action = 'command'
    t._role = None
    m = VariableManager()
    connection = connection_loader.get('local',variables=m)
    am = action_loader.get(t.action, connection=connection, task=t, play_context=None, loader=None, templar=None, shared_loader_obj=None)

    assert am is not None
    assert isinstance(am, ActionModule)

# Generated at 2022-06-13 10:22:41.917110
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule.__name__ == 'ActionModule'

    class ActionModule(ActionModule):
        pass

    assert ActionModule.__name__ == 'ActionModule'

# Generated at 2022-06-13 10:22:42.575612
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert True

# Generated at 2022-06-13 10:22:48.100148
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import mock
    import json

    m = mock.MagicMock()
    m.run.return_value = {"ansible_facts":{}}

    p = mock.MagicMock()
    p.run.return_value = {"changed":True}

    m1 = mock.MagicMock()

    c = mock.MagicMock()
    c._shell = mock.MagicMock()
    c._shell.tmpdir = "/tmp/dir"

    module = ActionModule(m, c, p, task_vars={'var':{'key':'value'}})
    result = module.run()

    json_result = json.dumps(result)
    assert result['invocation'] == {'module_args':{'var':{'key':'value'}}}, json_result

# Generated at 2022-06-13 10:22:59.554649
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    ansible= Ansible()
    parser = CliRunner()
    inventory = InventoryManager(loader=ansible.loader,sources=['/etc/ansible/hosts'])
    variable_manager = VariableManager(loader=ansible.loader, inventory=inventory)

    module = DummyModule()
    module._shared_loader_obj = ansible.loader
    module._shared_loader_obj.set_basedir('./')
    module._shared_loader_obj.module_loader = ansible.loader

    module._task = DummyTask()
    module._task.become = 'true'
    module._task.connection = 'local'
    module._task.action = "ping"
    module._task.play = DummyPlay()
    module._task.async_val = '1'

    module._connection = Connection()

# Generated at 2022-06-13 10:23:01.060241
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # How to test a method run of class ActionModule when it has local import modules above?
    assert True

# Generated at 2022-06-13 10:23:05.756108
# Unit test for constructor of class ActionModule

# Generated at 2022-06-13 10:25:28.063573
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.task_result import TaskResult
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    play_context = PlayContext()
    play_context._ssh_executable = '/bin/ssh'
    play_context._become_method = 'sudo'
    play_context._become_user = 'root'
    play_context._become_password = 'test'
    play_context._become_exe = '/bin/become'
    play_context._become_flags = '-f'
   

# Generated at 2022-06-13 10:25:29.072330
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:25:29.669345
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:25:37.560035
# Unit test for constructor of class ActionModule
def test_ActionModule():
    class FakeModule:
        def __init__(self):
            self.argument_spec = dict()
    class FakeTask:
        def __init__(self):
            self.action = 'fake'
            self.name = 'fake'
            self.args = dict()
            self.async_val = False
    class FakeConnection:
        def __init__(self):
            self.has_native_async = False
    class FakePlayContext:
        def __init__(self):
            self.remote_addr = '127.0.0.1'
            self.become = False
            self.become_method = None
            self.become_user = None
            self.become_pass = None
            self.port = 22

# Generated at 2022-06-13 10:25:47.900254
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    am = ActionModule()
    am._remove_tmp_path = lambda x: None
    am._task = ActionModule.Task()
    am._task.async_val = None
    am._task.action = C.DEFAULT_ACTION_PLUGIN
    am._task.action_plugin = C.DEFAULT_ACTION_PLUGIN
    am._task.async_jid = "test_ActionModule_run"
    am._task.loop = "test_ActionModule_run"
    am._connection = ActionModule.Connection()
    am._connection._new_stdin = None
    am._connection._shell = ActionModule.Shell()
    am._connection._shell.tmpdir = "/tmp"
    am._connection._shell.can_control_stdin = False
    am._connection._shell.executable = "/bin/sh"

# Generated at 2022-06-13 10:25:57.807700
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # mock task and module args
    task_vars = {
        'ansible_version': {'full': '2.3.0.0'},
        'ansible_python_interpreter': '/usr/bin/python'
    }
    args = {'_ansible_no_log': False, '_ansible_syslog_facility': 'LOG_USER'}
    # mock action module
    action_module = ActionModule(None, args, task_vars=task_vars)
    # call method run of class ActionModule
    action_module.run()

# Generated at 2022-06-13 10:26:00.224258
# Unit test for method run of class ActionModule

# Generated at 2022-06-13 10:26:04.404855
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """
    Verify basic constructor of class ActionModule
    """
    c = ActionModule(None, None, None,None, None, None)
    assert c is not None

# Generated at 2022-06-13 10:26:14.915909
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import unittest

    # Dummy data for class constructor
    connection = {}
    datastructure = {}
    connection_loader = {}
    play_context = {}
    loader = {}
    templar = {}
    shared_loader_obj = {}
    finalize_callback = lambda: True

    # Initalizing class object with data provided
    test_obj = ActionModule(connection, datastructure, connection_loader, play_context, loader, templar, shared_loader_obj, finalize_callback)
    assert test_obj is not None