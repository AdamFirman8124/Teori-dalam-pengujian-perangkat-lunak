

# Generated at 2022-06-13 09:34:50.348294
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(task=dict(action=dict(module_name='action_module', args=dict())))
    assert module is not None

# Generated at 2022-06-13 09:34:51.183941
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert True

# Generated at 2022-06-13 09:35:04.954715
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.play_context import PlayContext

    play_context = PlayContext()
    action_module = ActionModule(play_context, dict())
    action_module._display._verbosity = 3
    action_module._display.verbosity = 3
    action_module._display.deprecated(
        'warning', 'hello', version='1.0', removed=False)

    assert type(action_module.setup) == FunctionType
    assert action_module.setup.__name__ == 'setup'
    assert type(action_module.run) == FunctionType
    assert action_module.run.__name__ == 'run'
    assert type(action_module.cleanup) == FunctionType
    assert action_module.cleanup.__name__ == 'cleanup'
    assert action_module.cleanup == ActionModule.cleanup

# Generated at 2022-06-13 09:35:12.846869
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    mock__connection = Mock(name='_connection')
    mock_find_needle = Mock(
        name='find_needle',
        return_value='/tmp/ansible_file_payload_pRPvaz/test.txt'
    )
    mock_remote_expand_user = Mock(
        name='_remote_expand_user',
        return_value='/home/david/test.txt'
    )
    mock__copy_file = Mock(
        name='_copy_file',
        return_value={'changed': False, 'failed': False}
    )
    mock__execute_module = Mock(
        name='_execute_module',
        return_value={'changed': False, 'failed': False}
    )

# Generated at 2022-06-13 09:35:15.149183
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule()
    assert module != None
    assert hasattr(module, 'run')

#
# Unit tests for _walk_dirs()
#


# Generated at 2022-06-13 09:35:17.645976
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # action_module.run(self, tmp=None, task_vars=None)
    pass

# Generated at 2022-06-13 09:35:21.542448
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert action_module.__class__ == ActionModule

# Generated at 2022-06-13 09:35:25.043405
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''Unit test for the ActionModule constructor'''
    action_module = ActionModule(ActionModule.get_action_name(),
                                 dict(),
                                 dict(),
                                 dict(),
                                 dict(),
                                 dict(),
                                 dict())

    assert isinstance(action_module, ActionModule)

# Generated at 2022-06-13 09:35:27.502022
# Unit test for constructor of class ActionModule
def test_ActionModule():  # noqa: N802
    am = ActionModule(task_vars=dict())
    assert isinstance(am, ActionModule)



# Generated at 2022-06-13 09:35:31.398992
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """Test function for ActionModule.run"""
    am = ActionModule('fake action', 'fake_action', {}, {'no_log': True})
    assert am.run() == {'failed': True, 'msg': 'src or content is required'}

# Generated at 2022-06-13 09:36:21.069281
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Instance of class ActionModule
    module = ActionModule("task", "connection", "play_context", "loader", "templar", "shared_loader_obj")
    assert("ActionModule" in str(type(module)))
    assert("task" in str(type(module._task)))
    assert("connection" in str(type(module._connection)))
    assert("play_context" in str(type(module._play_context)))
    assert("loader" in str(type(module._loader)))
    assert("templar" in str(type(module._templar)))


# Unit test to test _find_needle() of class ActionModule

# Generated at 2022-06-13 09:36:29.438843
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = ActionModule()
    action_module._task = Mock()
    action_module._task.args = dict()
    action_module._task.args['src']="test"
    action_module._task.args['dest']="test"
    action_module._task.args['remote_src']=False
    action_module._task.args['local_follow']=True

    action_module._connection = Mock()
    action_module._connection._shell = Mock(AnsibleShell)
    action_module._connection._shell.path_has_trailing_slash = lambda x:False
    action_module._connection._shell.join_path = lambda x,y:x+y
    action_module._connection._shell.tmpdir =None

# Generated at 2022-06-13 09:36:33.374806
# Unit test for constructor of class ActionModule
def test_ActionModule():
    global module_loader
    module_loader = AnsibleModuleLoader(None, None)
    global connection_loader
    connection_loader = ConnectionLoader(None, None)

# Generated at 2022-06-13 09:36:41.939823
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''Unit test of run() in ansible.plugins.action.copy.ActionModule'''

    # Imports

    # Variables
    # redefine
    module = None
    task = None
    tmp = None
    task_vars = None

    # Set up
    # mock

    module = ansible.plugins.action.copy.ActionModule(
        module._connection,
        module._task,
        module._loader,
        module._templar,
        module._shared_loader_obj
    )

    # Testing
    result = module.run(task_vars)

    # assert
    expected = None
    assert result == expected



# Generated at 2022-06-13 09:36:50.042782
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Make sure we test the local versions of modules.
    C.DEFAULT_MODULE_PATH = '../lib/ansible/modules'

    # Create the action module instance.
    action = ActionModule(dict())

    # Create a mock task with a few fields of interest.
    task = AnsibleTask()
    task._task.args = dict()
    task._task.action = 'ansible.builtin.copy'

    # Create a mock connection that we can use in the test.
    connection = MockConnection()
    connection._shell = MockShell()

    # Set the copy action module's connection to the mock connection.
    action._connection = connection

    # Create a mock taskvars with a few fields of interest.
    task_vars = dict()
    task_vars['ansible_connection'] = 'mock'

    # Create

# Generated at 2022-06-13 09:36:52.841726
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule().__module__ == 'ansible_collections.notstdlib.moveitallout.plugins.modules.copy'


# Generated at 2022-06-13 09:37:00.679166
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """
    This is just really a sanity test to make sure that the ActionModule
    class can be created, and an object of it can have methods called on it.

    The constructor for ActionModule does not accept any arguments, so this
    is about as good as we can do for a test.
    """
    am = ActionModule()
    try:
        am.run()
    except NotImplementedError:
        pass


# Generated at 2022-06-13 09:37:11.061781
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''
    Unit test for method run of class ActionModule
    '''
    # Configure mock for ActionModule.run()

# Generated at 2022-06-13 09:37:21.319575
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    @pytest.fixture(scope='module')
    def action_module():
        module_args = dict()
        module_args['src'] = 'src'
        action_module = ActionModule(dict(), module_args)
        return action_module

    def test_ActionModule_run_01(action_module):
        source = ''
        content = ''
        dest = ''
        task_vars = dict()
        res = action_module._run(source, content, dest, task_vars)
        assert 'failed' in res
        assert res['failed'] == True
        assert 'msg' in res
        assert res['msg'] == 'src (or content) is required'



# Generated at 2022-06-13 09:37:28.856710
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    conn = MagicMock()
    task = MagicMock()
    loader = MagicMock()
    templar = MagicMock()
    task_vars = {}
    tmp = {}
    sut = ActionModule(conn, task, loader, templar, task_vars, tmp)
    # no exception raised
    sut.run(tmp, task_vars)
    # verify
    conn.run.assert_called_once_with('/bin/sh -c "mkdir -p $HOME/.ansible/tmp/ansible-tmp-1463702517.83-157176338233771 && echo $HOME/.ansible/tmp/ansible-tmp-1463702517.83-157176338233771"', stdin=None)

# Generated at 2022-06-13 09:38:57.260985
# Unit test for method run of class ActionModule
def test_ActionModule_run():
  # TODO: implement
  return None

# Generated at 2022-06-13 09:38:59.244570
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(None, {})

    assert(isinstance(module, ActionModule))

# Generated at 2022-06-13 09:39:00.804672
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True


# Generated at 2022-06-13 09:39:13.334212
# Unit test for constructor of class ActionModule
def test_ActionModule():

    # Test ActionModule.__init__() with an explicitly given `task` argument.
    # It should be a Task() instance with no connection plugins.
    task = Task()
    task.connection = None
    action_module = ActionModule(task, connection='local')
    assert(action_module.task == task)
    assert(action_module._task == task)
    assert(action_module.connection == 'local')

    # Test Task.__init__() with no explicitly given `task` argument.
    # It should be a Task() instance with a connection plugin from `connection`.
    task = Task()
    task.connection = 'local'
    action_module = ActionModule(connection='local')
    assert(action_module.task == task)
    assert(action_module._task == task)

# Generated at 2022-06-13 09:39:28.736779
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    t = collections.namedtuple('Task', ['args', 'task_vars'])
    task = t(args = dict(
            src = "test/test_action_module/test_module_utils_basic/test_module_utils_urls.py", 
            content = "", 
            dest = "/Users/danshultz/project/ansiblepull/test/test_action_module/test_module_utils_basic/", 
            remote_src = "", 
            local_follow = "",
            checksum = ""
        ),
        task_vars = dict()
    )
    action_module = ActionModule(task)

    result = action_module.run(tmp=None, task_vars=None)

# Generated at 2022-06-13 09:39:36.004585
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule('test', 'test', 'test', 'test')

    assert hasattr(action, '_connection')
    assert hasattr(action, '_task')
    assert hasattr(action, '_loader')
    assert hasattr(action, '_templar')
    assert hasattr(action, '_shared_loader_obj')
    assert hasattr(action, '_connection_loader')
    assert hasattr(action, '_task_vars')
    assert hasattr(action, '_nonpersistent_fact_names')
    assert hasattr(action, '_play_context')
    assert hasattr(action, '_loader_cache')
    assert hasattr(action, '_task_fields')
    assert hasattr(action, '_play')
    assert hasattr(action, '_play_context')


# Generated at 2022-06-13 09:39:39.131903
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = AnsibleModule(argument_spec={})
    assert not isinstance(module.params, collections.Mapping)


# Generated at 2022-06-13 09:39:45.105317
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = ActionModule(task=None)
    result = action_module.run(tmp=None, task_vars={})
    assert 'msg' in result and result['msg'] == 'please use the copy module instead of copy.py'
    assert result['invocation'].get('module_name') == 'copy'

# Generated at 2022-06-13 09:39:51.334274
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # unittest requires method with test_ as prefix.  We can not just
    # create an instance of ActionModule, as we have to set _handle_filename
    # because _load_task_vars calls it.
    class TestActionModule(ActionModule):
        def _handle_filename(self, pathname):
            return pathname

    mock_connection = MockConnection()
    module = TestActionModule(mock_connection)
    module._task.args = dict()
    module._load_task_vars = lambda: dict()
    return module


# Generated at 2022-06-13 09:39:58.275177
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    error_msg = '''- hosts: localhost
  tasks:
    - name: test
      action:
      module: ansible.legacy.copy
'''
    simple_playbook_path = os.path.join(os.getcwd(), 'test_action_module.yml')
    open(simple_playbook_path, 'w').write(error_msg)


# Generated at 2022-06-13 09:43:52.768971
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Case when source is a directory
    _task = namedtuple('_task', ['args'])
    _task.args = {'backup': False, 'content': None, 'dest': 'dest', 'mode': None, 'regexp': None, 'remote_src': False, 'selevel': None, 'serole': None, 'setype': None, 'seuser': None, 'src': 'src', 'unsafe_writes': False, 'validate': None}
    _task = _task()

# Generated at 2022-06-13 09:44:02.994496
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = ActionModule()
    action_module.connection = Mock()
    action_module.connection._shell = Mock()
    action_module.connection._shell.tmpdir = Mock()
    action_module.connection._shell.path_has_trailing_slash = Mock()
    action_module.connection._shell.join_path = Mock()
    action_module.connection._shell.join_path.return_value = (
        '/Users/sudheer/Downloads/playbook/ansible-playbook --diff '
        '-v -i /Users/sudheer/Downloads/playbook/inventory '
        '/Users/sudheer/Downloads/ansible-test/test.yml')
    action_module.env = dict()
    action_module._task = Mock()
    action_module._task

# Generated at 2022-06-13 09:44:09.964235
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Define a host to test against
    host, port = _load_mock_data().items()[0]

    # Create an action module
    action = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

    # Create and load a task for this action module to work with
    task = Task()
    task.args = dict(
        src=None,
        dest=None,
        content=None,
        remote_src=False,
        local_follow=True
    )
    task_vars = dict(
        ansible_python_interpreter='/usr/bin/python'
    )
    action._task = task
    action._shared_loader_obj = None
    action._loader = DataLoader()
    action