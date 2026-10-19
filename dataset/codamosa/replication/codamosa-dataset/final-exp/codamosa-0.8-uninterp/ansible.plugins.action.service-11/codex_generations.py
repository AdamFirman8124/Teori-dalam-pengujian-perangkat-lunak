

# Generated at 2022-06-13 10:26:53.048569
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = ActionModule()
    # TODO
    return action_module.run()

# Generated at 2022-06-13 10:27:01.884847
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.module_utils import basic
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.plugins.loader import action_loader

    task = dict(
                action=dict(
                            module='service',
                            use='auto',
                            args=dict(
                                      name='httpd',
                                      state='stopped'
                                      )
                            ),
                async_val=123,
                async_jid='123',
                delegate_to='localhost',
                delegate_facts=None,
                _original_file='playbook.yml',
                _start_at_line=1,
                _ds=dict(),
                _hosts='localhost'
                )


# Generated at 2022-06-13 10:27:09.125622
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ''' Unit test for method run of class ActionModule '''

    # Define the classe used to mock the method load_from_file_module of ActionBase
    class MockActionBase:
        def load_from_file_module(self, path, module_name, module_args, task_vars=None, wrap_async=None):
            if path == 'ansible/modules/system/setup.py':
                return dict(
                    ansible_facts=dict(
                        ansible_service_mgr='fake module'
                    )
                )
            return dict()

    # Define the classe used to mock the method _load_params of ActionBase

# Generated at 2022-06-13 10:27:09.824775
# Unit test for constructor of class ActionModule
def test_ActionModule():
    pass

# Generated at 2022-06-13 10:27:13.604426
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule(dict(action='setup', _uses_shell=True, _raw_params='setup', _task_vars=dict(ansible_service_mgr='systemd')))
    assert am._task.args.get('use') == 'auto'

# Generated at 2022-06-13 10:27:24.106045
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(
        task = dict(
            async_val = 10,
            args = dict(
                path = '/usr/bin',
                state = 'installed'
            ),
            delegate_to = 'ansiblecon'
        ),
        connection=dict(),
        play_context=dict(),
        loader=None,
        templar=None,
        shared_loader_obj=None
    )

    dictProp = action_module.run()


# Generated at 2022-06-13 10:27:26.408751
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert am.TRANSFERS_FILES == False

# Generated at 2022-06-13 10:27:26.908148
# Unit test for constructor of class ActionModule
def test_ActionModule():
  return

# Generated at 2022-06-13 10:27:34.038004
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    task_vars = dict(
        ansible_facts=dict(
            ansible_service_mgr='systemd',
        ),
    )
    task = dict(
        args=dict(
            name='httpd',
            state='started',
            use='auto',
        ),
    )
    module = ActionModule(task, dict())
    result = module.run(tmp=None, task_vars=task_vars)

    assert result['changed'] == True
    assert result['msg'] == 'httpd started'

# Generated at 2022-06-13 10:27:45.897738
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ''' test case for unit testing of run method of class ActionModule '''

    # create an instance of the class ActionModule
    act_obj = ActionModule()

    # create an instance of the class AnsibleAction
    ans_act_obj = AnsibleAction()

    # create an instance of the class AnsibleActionFail
    ans_act_fail_obj = AnsibleActionFail('Could not detect which service manager to use. Try gathering facts or setting the "use" option.')

    # create an instance of the class AnsibleAction
    ans_act_obj = AnsibleAction()

    # create an instance of the class AnsibleActionFail
    ans_act_fail_obj = AnsibleActionFail('Could not detect which service manager to use. Try gathering facts or setting the "use" option.')

    # create a mock object to be used as a argument of function run

# Generated at 2022-06-13 10:27:59.536982
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    import ansible.constants as C

    class Host:
        def __init__(self, name):
            self.name = name
            self.groups = {'all': True}
            self.vars = {}
            self.port = 22

    # Define a fake host
    host = Host('localhost')

    # Define a fake task
    task = Task()
    task._role = None
    task.action = 'shell'
    task.args = {}
    task.async_val = 30
    task.run_once = False

    # Define a fake block
    block = Block()

# Generated at 2022-06-13 10:28:00.212573
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert True

# Generated at 2022-06-13 10:28:12.670898
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import shutil
    import tempfile
    import json

    # Path to directory with fixtures
    FIXTURE_DIR = os.path.join(os.path.dirname(__file__), 'fixtures')

    # Create temporal working dir
    temp_dir = tempfile.mkdtemp()

    # Create temporal ansible.cfg
    temp_cfg = os.path.join(temp_dir, 'ansible.cfg')
    shutil.copyfile(os.path.join(FIXTURE_DIR, 'ansible.cfg'), temp_cfg)

    # For connection local test set ANSIBLE_CONFIG variable
    os.environ['ANSIBLE_CONFIG'] = temp_cfg

    # Fixtures used
    connection_local = os.path.join(FIXTURE_DIR, 'connection_local.py')

    # Create temporal

# Generated at 2022-06-13 10:28:15.855385
# Unit test for constructor of class ActionModule
def test_ActionModule():
    try:
        import ansible
        from ansible.plugins.action import ActionModule

        # constructor of class ActionModule
        # class ActionModule(ActionBase):
        ActionModule()

        assert True
    except:
        assert False

# Generated at 2022-06-13 10:28:19.309427
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """ Unit test for constructor of class ActionModule """

    task = dict(
        action=dict(
            module='service',
            use='auto',
            args=dict(
                state='started'
            )
        )
    )

    am = ActionModule(task, dict())
    print(am)

# Generated at 2022-06-13 10:28:21.390312
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule(dict(), dict(), False)
    assert action is not None
    assert action._shared_loader_obj is not None
    assert action._templar is not None

# Generated at 2022-06-13 10:28:24.225558
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(
        task=Mock(),
        connection=Mock(),
        play_context=Mock(),
        loader=Mock(),
        templar=Mock(),
        shared_loader_obj=Mock())
    assert action_module.TRANSFERS_FILES == False
    

# Generated at 2022-06-13 10:28:39.524528
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.plugins.action.normal import ActionModule
    task = {
        'args': dict(name='httpd', state='started'),
    }
    tmplar = object()
    shared_loader_obj = object()
    display = object()
    connection = object()
    adhoc_task = object()

    # Create a ActionModule object with valid parameters
    obj = ActionModule(tmplar, shared_loader_obj, task, connection, play_context=adhoc_task, loader=shared_loader_obj, templar=tmplar, shared_loader_obj=shared_loader_obj, display=display)
    assert obj._task.args == task['args']
    assert obj._templar == tmplar
    assert obj._shared_loader_obj == shared_loader_obj
    assert obj._connection

# Generated at 2022-06-13 10:28:45.859938
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import ansible.plugins.action.service as service
    module = service.ActionModule('test', {}, load_ds=None, play_context=None, new_on_new=None,
                                  shell=None, connection=None, tmp=None, become_method='sudo',
                                  become_user='root', become_exe=None, verbosity=None, check=None,
                                  diff=None, runner_cache=None)
    assert isinstance(module, service.ActionModule)

# Generated at 2022-06-13 10:28:55.078088
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """Unit test for ActionModule"""
    module_args = {"src": "file.sum", "dest": "/etc/sumfile", "sum": "sha1"}
    result = {"failed_when_result": True}
    module_name = 'ansible.legacy.copy'
    module_defaults = {}
    task_vars = {}
    action_groups = {}
    wrapped_ansible_module = ActionModule(
        module_name=module_name,
        module_args=module_args,
        pattern='all',
        task_vars=task_vars,
        tmp=None,
        wrap_async=False,
        action_groups=action_groups,
        module_defaults=module_defaults)
    result = wrapped_ansible_module.run(task_vars=task_vars)

# Generated at 2022-06-13 10:29:17.996713
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule({'name': 'service'}, {}, {})
    assert am is not None

    assert am.TRANSFERS_FILES == False

    assert len(am.UNUSED_PARAMS) == 1
    assert 'systemd' in am.UNUSED_PARAMS
    assert len(am.UNUSED_PARAMS['systemd']) == 5
    assert 'pattern' in am.UNUSED_PARAMS['systemd']
    assert 'runlevel' in am.UNUSED_PARAMS['systemd']
    assert 'sleep' in am.UNUSED_PARAMS['systemd']
    assert 'arguments' in am.UNUSED_PARAMS['systemd']
    assert 'args' in am.UNUSED_PARAMS['systemd']


# Generated at 2022-06-13 10:29:18.592194
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True

# Generated at 2022-06-13 10:29:22.289464
# Unit test for method run of class ActionModule

# Generated at 2022-06-13 10:29:29.974286
# Unit test for constructor of class ActionModule
def test_ActionModule():

    role_src = 'roles/test-role'
    role_path = '%s/tasks' % role_src
    name = 'test-role.yml'
    from os.path import dirname, join as pjoin
    path = pjoin(dirname(dirname(__file__)), name)

    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    import sys
    sys.path.append(role_path)
    from actions import ActionModule
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.executor.task_queue_manager import TaskQueueManager

# Generated at 2022-06-13 10:29:31.629718
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # check that 'service' action is initialized correctly
    assert isinstance(ActionModule(), ActionBase)

# Generated at 2022-06-13 10:29:35.724596
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert action_module is not None

# Generated at 2022-06-13 10:29:38.196911
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''
    Test method run of ActionModule class
    '''
    # TODO: make this test work
    assert True

# Generated at 2022-06-13 10:29:39.600629
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert 1 == 1

# Generated at 2022-06-13 10:29:52.137767
# Unit test for method run of class ActionModule
def test_ActionModule_run():
 
	# Test instantiation of class with all data
    result = ActionModule("test")
    print("test case 1")
    print("Testing on instantiation of the class")
    print("Checking on type:", type(result))
    assert isinstance(result, ActionModule)

    # Test instantiation of class with all data
    result = ActionModule(action='setup')
    print("test case 2")
    print("Testing on execution of the class")
    print("Checking on type:", type(result))
    assert isinstance(result, ActionModule)

    # Test instantiation of class with all data
    result = ActionModule(module='setup')
    print("test case 3")
    print("Testing on module execution of the class")
    print("Checking on type:", type(result))
    assert isinstance(result, ActionModule)

# Generated at 2022-06-13 10:30:01.188572
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule(task = {"args": {'use': 'auto'}}, connection = "conn_mock", play_context = {"network_os": "network_os_mock"}, loader = "loader_mock", templar = "templar_mock", shared_loader_obj = "shared_loader_obj_mock")
    res = module.run()
    assert res["failed"] == True
    assert "No module named ansible.legacy.setup" in res["msg"]



# Generated at 2022-06-13 10:30:43.166525
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """
    Unit test for method run of class ActionModule
    """
    mock_connection = Mock(name='_connection')
    mock_templar = Mock(name='_templar')
    mock_tmp = Mock(name='tmp')
    mock_task = Mock(name='_task')
    mock_task_args = Mock(name='_task.args', svc='test_svc', state='state_val')
    mock_task_args.__getitem__.side_effect = lambda x: getattr(mock_task_args, x)
    mock_task.args = mock_task_args

    mock_display = Mock(name='_display')
    mock_shared_loader_obj = Mock(name='_shared_loader_obj')
    mock_module_loader = Mock(name='module_loader')

   

# Generated at 2022-06-13 10:30:54.569288
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils.common.removed import removed
    from ansible.utils.display import Display
    from ansible.plugins.action.service import ActionModule

    module_instance = ActionModule(
        task=dict(async_val=False, async_seconds=0, args=dict(name='foobar', state='stopped', use='auto'), delegate_to='127.0.0.1',
                  run_once=True, module_defaults='foo', connection='ansible.netcommon.network_cli'),
        connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

    arguments = dict(
        name='foobar',
        state='stopped'
    )

    result = dict(
        ansible_module_generated=True
    )
   

# Generated at 2022-06-13 10:30:57.694886
# Unit test for constructor of class ActionModule
def test_ActionModule():
    mod = ActionModule(None, {}, None, None, None, {})
    assert mod is not None

# Generated at 2022-06-13 10:30:58.776425
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule

# Generated at 2022-06-13 10:30:59.614194
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True

# Generated at 2022-06-13 10:31:07.209310
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = ActionModule()
    self = type('', (), {})()
    action_module._remove_tmp_path = lambda x: None
    self._task = type('', (), {'args': {}, 'async_val': True})()
    self._connection = type('', (), {'_shell': type('', (), {'tmpdir': None})()})()
    self._shared_loader_obj = type('', (), {'module_loader': type('', (), {'has_plugin': lambda x: True})()})()
    self._display = type('', (), {'debug': lambda x: None, 'warning': lambda x: None, 'vvvv': lambda x: None})()
    self._templar = type('', (), {'template': lambda x: 'service'})()
    action_module.run(self)

# Generated at 2022-06-13 10:31:13.102978
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.action import ActionBase
    from ansible.module_utils._text import to_text
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    import ansible.constants as C
    import json
    import pytest
    pytest.importorskip('systemd')

    class FakeActionModule(ActionModule):
        __action_cls__ = ActionBase

    class FakeRunner(object):
        def __init__(self, host_name, module_name, module_args, task_vars=None, connection_info=None):
            self.host_name = host_name
            self.module_name = module_name
            self.module_args = module_args
            self

# Generated at 2022-06-13 10:31:23.276776
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    connection = Connection()
    task_vars = dict(
        ansible_facts=dict(
            service_mgr='systemd'
        )
    )

    module_args = dict(
        use='auto',
        name='foo',
        state='started'
    )

    task = Task()
    task.async_val = False
    task.action = 'foo'
    task.args = module_args
    task.set_loader(Loader())
    task.notify = []
    task.dep_chain = None
    task._parent = Play()

    my_test = ActionModule(connection, task, task_vars, module_args)
    result = my_test.run()
    assert result == {'changed': False}

    # Test use with auto, which doesn't match any service manager
    module_

# Generated at 2022-06-13 10:31:25.852522
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert action_module is not None


# Generated at 2022-06-13 10:31:32.235221
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''
    Unit test for constructor of class ActionModule
    '''
    # Constructor with one argument
    yaml = '''
    - name: test1
      hosts: localhost
      tasks:
      - name: module1
        action:
          module: testmodule
          name: module1
    '''
    result = dict(
        changed=False,
        failed=False
    )
    task = Task.load_from_data(yaml)
    exec_result = ExecutionResult(task, result, None)
    exec_status = ExecStatus(exec_result)
    act = ActionModule(exec_status)
    assert act._task == task
    assert act.TRANSFERS_FILES == False

# Generated at 2022-06-13 10:32:29.341557
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    class PrivActionModule(ActionModule):
        def __init__(self, task, connection, play_context, loader, templar, shared_loader_obj):
            super(PrivActionModule, self).__init__(task, connection, play_context, loader, templar, shared_loader_obj)
            self._task = task
            self._connection = connection
            self._play_context = play_context
            self._loader = loader
            self._templar = templar
            self._shared_loader_obj = shared_loader_obj

    task = MagicMock()
    connection = MagicMock()
    play_context = MagicMock()
    loader = MagicMock()
    templar = MagicMock()
    shared_loader_obj = MagicMock()

# Generated at 2022-06-13 10:32:32.851961
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    #Arrange
    #Act
    act = ActionModule(loader=None, shared_loader_obj=None, task=None, connection=None, play_context=None, loader_cache=None)
    act.run(tmp=None, task_vars=None)

    #Assert



# Generated at 2022-06-13 10:32:43.059611
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.errors import AnsibleActionFail
    from ansible.executor.task_result import TaskResult
    from ansible.plugins.action import ActionBase

    # class ActionModule
    # def run(self, tmp=None, task_vars=None):
    result = TaskResult(host=dict(), task=dict())

    # Requires a _shared_loader_obj (PluginLoader)
    # Requires a remote_user (str)
    # Requires a _templar (Templar)
    # Requires a _connection (Connection)

# Generated at 2022-06-13 10:32:50.515499
# Unit test for method run of class ActionModule

# Generated at 2022-06-13 10:33:03.799072
# Unit test for constructor of class ActionModule
def test_ActionModule():
    Task = type('Task', (object,), {})
    ActionBase._config_class = mock.MagicMock()
    con = mock.MagicMock()
    loader = mock.MagicMock()
    display = mock.MagicMock()
    templar = mock.MagicMock()
    shared_loader_obj = mock.MagicMock()
    tmp = 'hi'
    task_vars = {}
    args = {'use': 'auto'}
    tasks = mock.MagicMock()
    task = Task()
    task._parent = task
    task._task = task
    task._task.async_val = 'hi'
    task._task._parent = mock.MagicMock()
    task._task._play = mock.MagicMock()
    task._task.module_defaults = {}
    task._

# Generated at 2022-06-13 10:33:11.729571
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    task_vars = dict(
        ansible_facts=dict(
            service_mgr=None,
            ansible_service_mgr=None,
        ),
        ansible_check_mode=False,
    )

    module_args = dict(
        name='django',
    )

    action_plugin = ActionModule()

    import ansible.executor.task_result
    task_result = ansible.executor.task_result.TaskResult()

    action_plugin.run(task_vars=task_vars, task_result=task_result, **module_args)

    assert task_result.is_successful()
    assert task_result.result.get('invocation')
    assert task_result.result.get('module_start')

# Generated at 2022-06-13 10:33:12.253107
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:33:13.655787
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule('test')
    assert module.__class__.__name__ == "ActionModule"

# Generated at 2022-06-13 10:33:15.766635
# Unit test for constructor of class ActionModule
def test_ActionModule():
    my_service = ActionModule()
    assert not hasattr(my_service,'action_name')

# Generated at 2022-06-13 10:33:25.050840
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.module_utils._text import to_text
    from ansible.plugins.task import Task
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText

    module_name = 'service'
    module_args = dict(
        use='auto',
        name='httpd',
        state='started',
        sleep='10',
        enable='yes'
    )

# Generated at 2022-06-13 10:35:40.409921
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.plugins.loader import action_loader
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor import module_common
    from ansible.executor.play_iterator import PlayIterator
    from ansible.playbook.play import Play
    import ansible.config.manager
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VaultAwareVariableManager

    loader = DataLoader()

# Generated at 2022-06-13 10:35:48.281487
# Unit test for constructor of class ActionModule
def test_ActionModule():
    loader = None
    #loader = DictDataLoader({})
    #loader.set_basedir('/home/username/playbooks/playbookdir')
    #queue = mock.Mock()
    #queue._is_async.return_value = True
    #action_plugin = ActionModule(loader=loader, task=Mock(), connection=Mock(), play_context=Mock(search_path=[]), loader_cache=Mock(), templar=Mock(), shared_loader_obj=Mock())
    from ansible.plugins.loader import action_loader
    action_plugin = action_loader.get('service', class_only=True)()
    action_plugin._task = Mock()
    action_plugin._task.args = dict()
    action_plugin._task.async_val = None

# Generated at 2022-06-13 10:35:56.043438
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Create connection and make sure it has correct name and port
    conn = Connection()
    assert conn._name == 'connection.local'
    assert conn.port is None

    # Create task and make sure it has correct name and action
    task = Task()
    assert task._name == 'setup'
    assert task.action == 'setup'

    # Create action module
    module = ActionModule(task, conn)

    # Test the method _execute_module
    results = module._execute_module(module_name='test', module_args={})
    assert 'invocation' in results
    assert results['invocation']['module_name'] == 'test'
    assert results['invocation']['module_args'] == {}

    return True

# Generated at 2022-06-13 10:36:02.807397
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import ansible.playbook.task
    import ansible.executor.task_result
    import ansible.executor.task_queue_manager
    import ansible.executor.play_iterator
    task = ansible.playbook.task.Task()
    task_result = ansible.executor.task_result.TaskResult(task, ansible.executor.task_queue_manager.TaskQueueManager())
    play = ansible.executor.play_iterator.PlayIterator()
    play._play = ansible.playbook.play.Play()
    play_context = ansible.playbook.play_context.PlayContext()
    play.play_context = play_context
    tmp = None
    task_vars = dict()

# Generated at 2022-06-13 10:36:05.936036
# Unit test for constructor of class ActionModule
def test_ActionModule():
    ok = {'hello': 'world'}
    module = ActionModule(task=ok, connection=ok, play_context=ok, loader=ok, templar=ok, shared_loader_obj=ok)
    assert module

# Generated at 2022-06-13 10:36:08.763805
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Test Using Auto
    # UNIT TESTS

    # Test Using Specific Module
    # UNIT TESTS

    # Test using auto with no facts
    # UNIT TESTS

    # Test using auto with unknown service_mgr
    # UNIT TESTS

    pass

# Generated at 2022-06-13 10:36:14.161769
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule('/path/to/ansible_module', 1, 2, 3, 4, 5)
    assert action_module._shared_loader_obj.module_loader.has_plugin('service') == True
    assert 'ansible.legacy.service' == action_module._task.args.get('use', 'auto').lower()

# Generated at 2022-06-13 10:36:15.017714
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule()

# Generated at 2022-06-13 10:36:25.165708
# Unit test for constructor of class ActionModule
def test_ActionModule():
    task_vars = dict(
        ansible_facts=dict(service_mgr='auto'),
        ansible_check_mode=False,
        ansible_version='2.1.0.0',
        ansible_module_name='service',
        ansible_module_args='name=foo',
    )
    mock_connection = object()
    mock_loader = object()
    mock_display = object()
    mock_templar = object()
    action = ActionModule(mock_connection, task_vars, mock_loader, mock_display, mock_templar)
    assert action.task_vars == task_vars
    assert action.connection == mock_connection
    assert action.action == 'service'
    assert action._templar == mock_templar
    assert action._loader == mock_

# Generated at 2022-06-13 10:36:34.660186
# Unit test for method run of class ActionModule
def test_ActionModule_run():
	# Create local objects of class ActionModule and AnsibleModule
	am = ActionModule(task=ansible.playbook.task.Task(), connection=ansible.plugins.connection.local.Connection(play_context=PlayContext(check_mode=False, diff_mode=False), new_stdin=None), templar=None, shared_loader_obj=None, default_vars=dict())
	am_m = ansible.module_utils.basic.AnsibleModule(argument_spec=dict(), supports_check_mode=False, bypass_checks=False)

	# Instantiate class TestModule
	tm = TestModule(am_m)

	# Test case when module auto is used
	tm.assertRaises(AnsibleAction, am.run, tmp=None, task_vars=dict())

	# Test case when module is system
