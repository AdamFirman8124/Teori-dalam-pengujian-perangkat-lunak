

# Generated at 2022-06-13 10:52:53.964180
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Create test ActionModule object.
    am = ActionModule()
    # Create test AnsiblePlugin object.
    ap = AnsiblePlugin()

    # Module is called locally.
    result = am.run(tmp = None, task_vars = None)
    print("ActionModule_run: {}".format(result))

    ## Test results:
    # Have not found an example of this method output. 


# Generated at 2022-06-13 10:52:55.764994
# Unit test for constructor of class ActionModule
def test_ActionModule():
    p = ActionModule()
    assert p is not None


# Generated at 2022-06-13 10:53:08.343709
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Needed to instantiate a class with an abstract method in it.
    class ConcreteModule(ActionModule):
        def run(self, tmp=None, task_vars=None):
            return super(ConcreteModule, self).run(tmp, task_vars)

    mod = ConcreteModule()
    mod.set_options(module_path='ansible.builtin.copy')
    mod.set_runner(object())
    mod.process_common_errors = lambda x, y: y
    mod.set_connection(object())

    mod._task.args = dict(
        args=dict(
            src='/a/b/c',
            dest='/x/y/z',
            decrypt=True,
        )
    )

# Generated at 2022-06-13 10:53:22.155923
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    try:
        import ansible.compat.six
    except (ImportError, SyntaxError):
        pass
    loader = DictDataLoader({})
    variable_manager = VariableManager()
    variable_manager.set_inventory(Inventory(loader))
    connection = None
    play_context = PlayContext()
    play_context.connection = "local"
    play_context.network_os = "default"
    play_context.remote_addr = "127.0.0.1"
    play_context.port = 22
    play_context.remote_user = "user"
    play_context.password = "password"
    play_context.private_key_file = "~/.ssh/id_rsa"
    play_context.become = False
    play_context.become_method = "sudo"
   

# Generated at 2022-06-13 10:53:24.140225
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    #
    # Unit test: ansible.plugins.action.unarchive.ActionModule.run
    #
    pass

# Generated at 2022-06-13 10:53:33.951600
# Unit test for constructor of class ActionModule
def test_ActionModule():
    host = 'testhost'
    connection = 'testconnection'
    runner_queue = 'testrunner_queue'
    loader = 'testloader'
    tmp = 'testtmp'
    shared_loader_obj = 'testshared_loader_obj'
    variable_manager = 'testvar_manager'
    action_base = ActionModule(host, connection, runner_queue, loader, tmp, shared_loader_obj, variable_manager)
    assert action_base._host == host
    assert action_base._connection == connection
    assert action_base._runner_queue == runner_queue
    assert action_base._loader == loader
    assert action_base._tmp == tmp
    assert action_base._shared_loader_obj == shared_loader_obj
    assert action_base._variable_manager == variable_manager
    assert action_base._task_vars

# Generated at 2022-06-13 10:53:39.340068
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule('test_name', 'test_args', 'test_inject')._task.name == 'test_name'
    assert ActionModule('test_name', 'test_args', 'test_inject')._task.args == 'test_args'
    assert ActionModule('test_name', 'test_args', 'test_inject')._task._had_task_run == False

# Generated at 2022-06-13 10:53:40.213542
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert isinstance(ActionModule(), ActionBase)

# Generated at 2022-06-13 10:53:49.809835
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task import Task

    # Create a task that checks for the existence of a directory and executes
    # another task if the directory exists.
    test_task = Task()
    test_task.args['src'] = 'testdirectory'
    test_task.args['dest'] = 'C:\\Users\\admin\\uncrypt'

    action_plugin = ActionModule(task=test_task, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

    assert action_plugin._task.args['src'] == 'testdirectory'
    assert action_plugin._task.args['dest'] == 'C:\\Users\\admin\\uncrypt'

# Generated at 2022-06-13 10:53:55.977273
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task

    block = Block.load(
        None,
        [
            dict(
                action=dict(
                    __ansible_module__='unarchive',
                    dest='/usr/local/unarchive',
                    src='/path/to/src/file'
                ),
                module_vars=dict()
            )
        ],
        loader=None,
        variable_manager=None,
        parent_block=None
    )
    task = Task.load(
        None,
        block,
        None,
        variable_manager=None,
        loader=None
    )
    task.block = block


# Generated at 2022-06-13 10:54:15.693143
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Set up test fixture
    #
    # test that boolean() works for str, int, and bool types
    assert(boolean('yes') == True)
    assert(boolean('True') == True)
    assert(boolean('false') == False)
    assert(boolean('False') == False)
    assert(boolean('0') == False)
    assert(boolean('1') == True)
    assert(boolean(0) == False)
    assert(boolean(1) == True)
    assert(boolean(True) == True)
    assert(boolean(False) == False)

    # test that None is returned if file doesn't exist
    assert(boolean(os.path.join(os.path.dirname(__file__), 'test_file_does_not_exist')) == False)

   

# Generated at 2022-06-13 10:54:29.748312
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task import Task

    action_module = ActionModule(Task(), dict())
    assert (action_module._task is not None)

    action_module_with_args = ActionModule(Task(), dict(src='~/foo/bar.zip', dest='./', remote_src=True, creates='foobar.txt', decrypt=True))
    assert (action_module_with_args._task is not None)
    assert (action_module_with_args._task.args['src'] == '~/foo/bar.zip')
    assert (action_module_with_args._task.args['dest'] == './')
    assert (action_module_with_args._task.args['remote_src'] is True)

# Generated at 2022-06-13 10:54:30.446077
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert False

# Generated at 2022-06-13 10:54:36.950575
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule()
    print()
    print("This is a test of ActionModule class method run.")
    print()
    print("There is no output if the test passes.")
    print()
    print("If the test fails, an exception will be generated.")
    print()
    print("test_ActionModule_run.py has been executed")
    print()

# Execute the test when this file is run.
test_ActionModule_run()

# Generated at 2022-06-13 10:54:45.500132
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Setting up the mock objects
    mock_task = MagicMock()
    mock_connection = MagicMock()
    mock_task.args = {'src': "/data/files/file.txt", 'dest': "/data/files/destination",
                      'remote_src': False, 'creates': None, 'decrypt': True}
    mock_task.action = "UNARCHIVE"
    mock_task.action_loader = _MockActionLoader()
    mock_task.name = "UNARCHIVE"
    mock_task._ds = mock_task.args
    mock_task.async_val = 30
    mock_task._connection = mock_connection
    mock_task._unreachable_hosts = []

# Generated at 2022-06-13 10:54:56.687843
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''
    Unit test for method run of class ActionModule
    '''
    fake_loader = FakeLoader()
    fake_task_queue_manager = FakeTaskQueueManager()
    fake_variable_manager = FakeVariableManager()

    subject = ActionModule(
        task=FakeTask(),
        connection=FakeConnection(),
        play_context=FakePlayContext(),
        loader=fake_loader,
        shared_loader_obj=fake_loader,
        # runner_cache=fake_task_queue_manager._cache,
        variable_manager=fake_variable_manager,
        task_vars=dict(test_run=True),
    )


# Generated at 2022-06-13 10:54:59.739332
# Unit test for constructor of class ActionModule

# Generated at 2022-06-13 10:55:00.376842
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert True

# Generated at 2022-06-13 10:55:02.699624
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    #test_ActionModule_run() cannot be implemented because it requires additional mocked methods.
    assert True

# Generated at 2022-06-13 10:55:13.179628
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Create a dummy task.
    task = {
        'action': 'test',
        'args': {},
        'register': 'shell_out'
    }
    # Convert the task to a parameterized interface.
    ptask = ActionModule.load(task, {}, [])
    # Instantiate class ActionModule.
    am = ActionModule(task, {})
    # Test that variables are initialized correctly.
    assert am._task.action == 'test'
    assert am._task.args  == {}
    assert am._task.register == 'shell_out'
    assert ptask._task.action == 'test'
    assert ptask._task.args  == {}
    assert ptask._task.register == 'shell_out'


# Generated at 2022-06-13 10:55:31.825408
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule('{"src": "~/src", "dest": "~/dest"}', '/path/to/module', True, False, False)
    assert action._task.args['src'] == "~/src"
    assert action._task.args['dest'] == "~/dest"

# Generated at 2022-06-13 10:55:41.043579
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """
    Unit test for method run of class ActionModule
    :return:
    """
    import __main__
    from ansible.executor.task_queue_manager import TaskQueueManager

    class TestTaskQueueManager(TaskQueueManager):
        def __init__(self):
            pass

        def _queue_task(self, host, task, task_vars, play_context):
            return dict(failed=False, changed=True, rc=0, stdout='', stderr='')

    # Initializing test class
    module = __main__.__dict__.get('ActionModule')
    test_class = ActionModule(None, dict(), None, None)
    test_class.task = 'test'
    test_class._display = None
    test_class._connection = None
    test_class._loader = None


# Generated at 2022-06-13 10:55:42.777360
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    am = ActionModule()
    am.run()


# Generated at 2022-06-13 10:55:49.902258
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = 'unarchive'
    action_plugin = 'unarchive'
    task_vars = {}
    self_hostname = 'hostname'

    action = ActionModule(self_hostname, task_vars=task_vars, loader=None, templar=None, shared_loader_obj=None)
    action._connection = MockConnection(self_hostname)
    action._task = MockTask(module=module, action=action_plugin, args=dict(src='test.file', dest='/destination'))

    result = action.run(task_vars=task_vars)
    assert 'skipped' in result

# Generated at 2022-06-13 10:55:50.437433
# Unit test for constructor of class ActionModule
def test_ActionModule():
    ActionModule()

# Generated at 2022-06-13 10:55:52.468549
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = ActionModule()
    action_module.run()
#

# Generated at 2022-06-13 10:55:54.343058
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert 1 == 1
    # TODO: Implement test for method run of class ActionModule

# Generated at 2022-06-13 10:56:05.871397
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.parsing.yaml.loader import AnsibleLoader

    # Initialize AnsibleLoader
    loader = AnsibleLoader(None, True)
    # Load task content
    task_vars = {}
    data = '''
    - name: mytask
      action: unarchive
      '''
    task = loader.load(data)[0]

    # Initialize ActionModule
    module = AnsibleModule(argument_spec={})
    am = ActionModule(task, module.connection, module._task_vars)

    # TODO: Test run method
    raise NotImplementedError

# Generated at 2022-06-13 10:56:07.738951
# Unit test for constructor of class ActionModule
def test_ActionModule():
    print("Testing Existence of ActionModule")
    module = ActionModule()
    assert module is not None


# Generated at 2022-06-13 10:56:09.633175
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''
    Instantiates ActionModule
    '''
    actionmodule = ActionModule()
    assert actionmodule

# Generated at 2022-06-13 10:56:40.354055
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    print("ActionModule.run is tested in TestActionModule")

# Generated at 2022-06-13 10:56:43.262259
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule(dict(ANSIBLE_MODULE_ARGS=dict(src='test', dest='test')))
    assert action is not None, "Failed to prepare a valid ActionModule object!"

# Generated at 2022-06-13 10:56:52.597698
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    Shell = namedtuple('Shell', ['join_path', 'tmpdir'])
    shell = Shell(join_path=lambda a, b: os.path.join(a, b), tmpdir='/tmp')
    Connection = namedtuple('Connection', ['_shell'])
    connection = Connection(_shell=shell)
    Host = namedtuple('Host', ['name'])
    host = Host(name='test_host')
    Task = namedtuple('Task', ['args', 'action'])
    task = Task(action='ansible.legacy.unarchive', args={'src': 'src', 'dest': 'dest', 'decrypt': 'decrypt'})
    PlayContext = namedtuple('PlayContext', ['check_mode'])
    play_context = PlayContext(check_mode=False)

# Generated at 2022-06-13 10:56:54.606625
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert 'unarchive' == ActionModule.default_module_name(None)



# Generated at 2022-06-13 10:57:03.138184
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task import Task
    from ansible.executor.task_result import TaskResult
    def AnsibleAction(arg1, arg2):
        return

    setattr(ActionModule, '_remove_tmp_path', AnsibleAction)
    setattr(ActionModule, '_execute_module', AnsibleAction)
    setattr(ActionModule, 'run', AnsibleAction)
    global_vars = dict()
    global_vars['role_path'] = 'test'
    global_vars['role_path'] = 'test'
    global_vars['runner_cache'] = 'test'
    global_vars['role_path'] = 'test'
    global_vars['role_path'] = 'test'
    task_vars = dict()
    task_vars['role_path']

# Generated at 2022-06-13 10:57:14.366613
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # unit test needs an "inventory" to work against
    import ansible.parsing.dataloader
    import ansible.inventory.manager
    import ansible.vars.manager
    import ansible.playbook.play
    import ansible.constants as C

    # make sure we don't try and use any real ansible.cfg file
    C.CONFIG_FILE = "/tmp/ansible_ActionModule_unarchive_config"
    if os.path.exists(C.CONFIG_FILE):
        os.unlink(C.CONFIG_FILE)
    # make sure we don't try and talk to github public
    C.DEFAULT_GITHUB_API_URL = "https://example.org"

    loader = ansible.parsing.dataloader.DataLoader()
    # set basedir to

# Generated at 2022-06-13 10:57:21.835881
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """
        Testing of run method of ActionModule
    """
    # Create an instance of class ActionModule
    module = ActionModule()
    # Create a class containing a mock method
    class ActionModuleMock(object):
        def run(self, *args, **kwargs):
            return {'msg': 'result'}
    # Create an instance of class ActionModuleMock and make module.run to be equal to method run of class ActionModuleMock
    module.run = ActionModuleMock().run
    result = module.run()
    assert result['msg'] == 'result'

# Generated at 2022-06-13 10:57:23.163405
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule(None, None)
    assert type(action) == ActionModule

# Generated at 2022-06-13 10:57:28.703114
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''
    Takes a dictionary of options.
    # create an action plugin instance
    args = dict(remote_user='root')
    actionMod = unarchive_action.ActionModule(**args)
    '''
    args = dict()
    actionMod = ActionModule(**args)  # constructor of ActionModule
    assert actionMod != None

# Generated at 2022-06-13 10:57:37.879139
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins.loader import action_loader
    from ansible.executor.task_queue_manager import TaskQueueManager
    import ansible.config.manager as config_manager

    config_manager.set_config_file('tests/test_utils/ansible.cfg')
    my_ActionModule = ActionModule({'name': 'test', 'args': {'src': 'test/file.txt', 'dest': '/dest', 'remote_src': False}}, TaskQueueManager('test_host', play_context=PlayContext()))
    assert my_ActionModule.run() == {'failed': True, 'msg': 'src (or content) and dest are required'}

# Generated at 2022-06-13 10:58:52.942979
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Test constructor of class ActionModule
    # Test no arguments
    m = ActionModule()
    # Test attributes are set correctly
    assert m.TRANSFERS_FILES == True

# Generated at 2022-06-13 10:58:59.421779
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import datetime
    task = {}
    task['args'] = {}
    task['args']['src'] = 'source-path'
    task['args']['dest'] = 'dest-path'
    action_mod = ActionModule(task=task, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert action_mod._task == task
    assert action_mod._task_vars == 'undefined'
    assert action_mod._play_context == 'undefined'
    assert action_mod._shared_loader_obj == 'undefined'
    assert isinstance(action_mod._loader, 'undefined')
    assert action_mod.TRANSFERS_FILES == True
    assert action_mod._connection == 'undefined'
    assert action_mod

# Generated at 2022-06-13 10:59:01.290370
# Unit test for constructor of class ActionModule
def test_ActionModule():
    testobj = ActionModule()
    assert testobj.TRANSFERS_FILES == True

# Generated at 2022-06-13 10:59:10.717776
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task import Task
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.playbook_executor import PlaybookExecutor
    import ansible.constants as C

    # Create all required objects.
    # Create objects directly so that we can test everything.
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources='localhost,')
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    variable_manager.extra_vars = {'hosts': 'localhost'}
    # TODO: Make this work on Windows.

# Generated at 2022-06-13 10:59:20.464522
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Initilize required objects
    task = dict()
    task['args'] = {}
    task['vars'] = {}
    task_vars = dict()
    task_vars['ansible_connection'] = 'local'
    task_vars['ansible_inventory_sources'] = ['test/test_inventory.yml']
    tmp = tempfile.mkdtemp()
    connection = ConnectionLocal(task_vars['ansible_inventory_sources'])
    loader = DataLoader()

    # initilize object for ActionModule class
    am = ActionModule(task, connection, tmp, task_vars, loader)

    # Test __init__ method
    assert am.TRANSFERS_FILES == True
    assert am._task == task
    assert am._connection == connection
    assert am._tmp == tmp
   

# Generated at 2022-06-13 10:59:28.888211
# Unit test for constructor of class ActionModule
def test_ActionModule():
    host = dict(
        name='127.0.0.1',
        port=22,
        transport='local',
    )
    task_vars = dict()
    options = dict(connection='local')
    variables = dict() # test_play_context
    local_action = 'copy'
    loader = None
    tmp_path = None
    task_tmp_path = None
    ptr = None
    templar = None
    play_context = None

    # Test args
    module_name = 'unarchive'
    module_args = dict(
        content='file.txt',
        dest='/tmp',
        original_basename='foobar.txt',
        src='~/',
        creates='/tmp/foobar.txt',
        executable=True,
        strip_components=1,
    )

# Generated at 2022-06-13 10:59:36.087431
# Unit test for constructor of class ActionModule
def test_ActionModule():
    my_task = dict()
    my_task['action'] = 'unarchive'
    my_task['args'] = { 'remote_src' : False}
    a = ActionModule(my_task, None, None, None)
    assert a._task.args['remote_src'] == False
    print('Test Successful - Constructor')

test_ActionModule()

# Generated at 2022-06-13 10:59:44.757256
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Build args, tmp, and task_vars
    args = dict(src = 'source', dest = 'dest', remote_src = False)
    tmp = None
    task_vars = dict()
    action = ActionModule(task = dict(args = args), connection = None, play_context = None, loader = None, templar = None, shared_loader_obj = None)

    # Test case where creates is not defined
    action._remote_file_exists = lambda x: False
    action._remove_tmp_path = lambda x: None
    action._execute_remote_stat = lambda x, y, z: dict(exists=True, isdir=True)
    action._fixup_perms2 = lambda x: None

# Generated at 2022-06-13 10:59:52.881166
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import pytest
    import ansible.plugins.action.unarchive as na_unarchive
    
    # Testing without raises argument.
    with pytest.raises(Exception):
        na_unarchive.ActionModule.run(None, None)

    # Testing with raises to make sure it does not raise.
    na_unarchive.ActionModule.run(None, None, raises=False)
    

if __name__ == '__main__':
    pytest.main()

# Generated at 2022-06-13 10:59:55.933335
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """Method _transfer_file of ActionModule class just calls the transfer_file method of Connection class. This method
     is already tested, in the test_Connection_transfer_file unit test."""
    pass