

# Generated at 2022-06-13 09:35:00.023399
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    my_path = os.path.abspath(os.path.dirname(__file__))
    empty_file = os.path.join(my_path, 'empty_file')
    assert os.path.exists(empty_file)

    module_constraint = {'delegate_to': 'delegate_to', 'src': empty_file, 'dest': 'dest' }
    module_name = 'copy'
    module_args = module_constraint
    module_class_name = 'ActionModule'
    module_loader = None
    task = Task(dict(action=dict(module=module_name, args=module_args)))
    connection = Connection(None)
    tmp = connection._shell.tmpdir
    display = Display()

    # Initialization

# Generated at 2022-06-13 09:35:05.938411
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """
    Constructor of class ActionModule
    :return:
    """
    am = ActionModule(task=dict(action=dict()), connection=None, play_context=None, loader=None, templar=None,
                      shared_loader_obj=None)

# Generated at 2022-06-13 09:35:09.389838
# Unit test for constructor of class ActionModule
def test_ActionModule():
    has_tmp_path = [True, False]
    for has_tmp in has_tmp_path:
        test_module(name='action',
                    path='ansible.legacy.actions.file.ActionModule',
                    has_tmp_path=has_tmp,
                    has_unsafe_context=False)

# Generated at 2022-06-13 09:35:18.148719
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Setup
    # Remove temporary content file if it exists
    if os.path.exists(content_tempfile):
        os.remove(content_tempfile)

    # Run
    try:
        # Define the class with some content
        action_module = ActionModule(dict(src='test_src', content='test_content', dest='test_dest', remote_src='test_remote_src', local_follow='test_local_follow'))
    except Exception:
        pass

    # Cleanup
    # Remove temporary content file if it exists
    if os.path.exists(content_tempfile):
        os.remove(content_tempfile)
 

# Generated at 2022-06-13 09:35:27.729385
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    tmp = tempfile.mkdtemp()
    task_vars = {"ansible_tmpdir_suffix": None}
    args = {
        "content": None,
        "dest": "/tmp/abc/ansible_file.txt",
        "remote_src": True,
        "local_follow": False,
        "src": "/tmp/abc/ansible_file.txt"
    }
    local_follow = False

# Generated at 2022-06-13 09:35:29.000106
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert (ActionModule is not None)



# Generated at 2022-06-13 09:35:34.548830
# Unit test for constructor of class ActionModule
def test_ActionModule():
    mock_connection = MagicMock()
    mock_connection._shell = MagicMock()
    mock_connection._shell.join_path = lambda *args: "/".join(args)
    mock_loader = MagicMock()
    mock_task = MagicMock()
    mock_task.args = {}
    action = ActionModule(mock_connection, mock_loader, mock_task, MagicMock())
    assert action

# Generated at 2022-06-13 09:35:45.634293
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    class mock_ActionModule():
        def __init__(self):
            return None

    action_module = mock_ActionModule()

# Generated at 2022-06-13 09:35:57.604446
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule.__name__ == 'ActionModule'
    assert ActionModule.__doc__ == '''Handler for copying files and directories'''
    am = ActionModule()
    assert isinstance(am, ActionModule)
    assert isinstance(am, ActionBase)
    assert am.DEFAULT_NEWLINE_SEQUENCE == '\n'
    assert am.CHECKSUM_ATTRIBUTES == ['checksum', 'sum']
    assert am.MODE_ARGUMENT_ERROR == "You can only use 'mode' for copying files and not for directories"
    assert am.MODE_TYPE_ERROR == "'mode' must be an octal mode specification in 4 digit format"

# Generated at 2022-06-13 09:35:58.743711
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(Task())
    assert action_module is not None


# Generated at 2022-06-13 09:36:50.923750
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    c = AnsibleConnector("ccc", "ddd", "eee", "fff")
    a = ActionModule(c._task, c._connection, c._templar, c._loader)
    resp = a.run(tmp="fff", task_vars=dict(a=1,b=2))
    assert resp

if __name__ == "__main__":
    test_ActionModule_run()

# Generated at 2022-06-13 09:36:58.334295
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play_context import PlayContext

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=['local_hosts'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    play_context = PlayContext()

    test_connection = Connection(module_name='test_connection')
    test_connection.connection = None

    # Test constructor of ActionModule()
    test_action = ActionModule(connection=test_connection,
                               play_context=play_context, loader=loader,
                               templar=None, shared_loader_obj=None)


# Generated at 2022-06-13 09:37:09.338461
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """Unit tests for remote_copy"""
    class DummyTask(object):
        def __init__(self, args):
            self.args = args
        def _remote_expand_user(self, dest):
            return dest

    # pylint: disable=unused-argument
    class DummyConnection(object):
        def __init__(self):
            pass
        def get_option(self, option):
            return 'local'
        def _shell_escape(self, arg):
            return '%s' % arg
        def _shell_expand_path(self, arg):
            return '%s' % arg
        def _fixup_perms2(self, cmd):
            return '%s' % cmd
        def _fixup_perms1(self, cmd):
            return '%s' % cmd

# Generated at 2022-06-13 09:37:10.657812
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert 'ActionModule' == type(ActionModule).__name__


# Generated at 2022-06-13 09:37:22.196726
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''
    Unit test for method run of class ActionModule
    '''

    storage = {}

    class MockTask(object):
        '''
        Class to mock a task object
        '''
        def __init__(self):
            self.args = dict()

        @staticmethod
        def _resolve_relative_path(original_path, original_basedir):
            '''
            Method to handle relative paths
            '''
            return original_path


    class MockModule(object):
        '''
        Class to mock module object
        '''
        def __init__(self, module_name, module_args='', task_vars=''):
            self._task = MockTask()
            self._connection = Connection(1)

# Generated at 2022-06-13 09:37:24.589888
# Unit test for method run of class ActionModule

# Generated at 2022-06-13 09:37:26.243905
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(load_ignored_vars=False)
    assert isinstance(type(module), ActionModule)


# Generated at 2022-06-13 09:37:41.654002
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    source_dir = "tests/unittests/module_utils/copy_data"
    local_follow = True
    remote_src = True

    # Set up a file on the source location
    source_file = os.path.join(source_dir,'testfile')
    with open(source_file, 'w') as f:
        f.write('hello world')

    # Create an ActionModule object with the above source file
    self = ActionModule(source_file, remote_src, local_follow)
    assert self == 'ansible.builtin.copy'

    # Test for optional src and dest variables
    task = dict(src = None, dest = None)
    self = ActionModule(task, remote_src, local_follow)

    tmp = "tests/unittests/module_utils/"

# Generated at 2022-06-13 09:37:53.557596
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    host = Mock()
    host.get_connection.return_value = SSHConnection(host, None)
    host._shell.join_path.return_value = '>|'
    host._shell.expand_user.return_value = '<~'
    host._shell.stat.return_value = dict(st_mode=0o7654)
    host._shell.is_executable.return_value = True
    host._shell.is_directory.return_value = True
    host._shell.is_fifo.return_value = True
    host._shell.is_file.return_value = True
    host._shell.is_block_device.return_value = True
    host._shell.is_socket.return_value = True
    host._shell.is_char_device.return_value = True
    host._

# Generated at 2022-06-13 09:37:55.487675
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    file = AnsibleFile()
    assert file.run() == None


# Generated at 2022-06-13 09:39:34.191969
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import ansible.playbook.play_context

    # Create a context which is initialized to values required by ActionModule
    connection = unittest.mock.Mock()
    connection._shell = unittest.mock.Mock()
    connection._shell.tmpdir = 'TEMP_DIR'
    connection._shell.join_path = os.path.join
    connection._shell.path_has_trailing_slash = lambda x: x.endswith('/')
    connection._shell._unquote = lambda x: x

    play_context = ansible.playbook.play_context.PlayContext()
    play_context.become = False
    play_context.become_user = ''
    play_context.remote_addr = 'REMOTE_ADDR'


# Generated at 2022-06-13 09:39:36.131763
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(None, None, None, None) is not None


# Generated at 2022-06-13 09:39:50.368739
# Unit test for constructor of class ActionModule

# Generated at 2022-06-13 09:39:57.812547
# Unit test for constructor of class ActionModule

# Generated at 2022-06-13 09:40:03.486871
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Create the object.
    x = ActionModule(task=dict(action=dict(module_name='async_status', args=dict())),
                     connection=MagicMock(),
                     only_if=True,
                     run_once=True,
                     no_log=True,
                     unless=True
                     )
    assert x is not None


# Generated at 2022-06-13 09:40:07.253355
# Unit test for constructor of class ActionModule
def test_ActionModule():
    def fill_args(args=None):
        if args is None:
            args = {}
        args['task'] = AnsibleTaskV2()
        return args
    action_module = ActionModule(**fill_args())
    assert isinstance(action_module, ActionModule)

# Generated at 2022-06-13 09:40:16.777528
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    mock_executor = MagicMock()
    mock_executor._shell.path_has_trailing_slash.return_value = False
    mock_executor._shell.join_path.return_value = "/tmp/test-src"
    mock_executor._shell.expand_user.return_value = "/tmp/test-dest"
    mock_loader = MagicMock()
    mock_loader.get_basedir.return_value = "/tmp/testdir"
    mock_task = MagicMock()
    mock_task.args = {'src': "test-src", 'dest': "test-dest"}
    mock_action_module = ActionModule(mock_task, mock_executor, mock_loader)
    non_recursive_result = mock_action_module.run(task_vars={})
   

# Generated at 2022-06-13 09:40:23.108799
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Test with different module_args
    # missing 'dest'
    module_args = {
        'src' : 'http://www.example.com/path/to/file.txt'
    }
    am = ActionModule(Task(), module_args)
    assert am._task.args.get('dest', None) is None
    assert am._task.args.get('src', None) == 'http://www.example.com/path/to/file.txt'

    # missing 'src'
    module_args = {
        'dest' : '/path/to/file.txt'
    }
    am = ActionModule(Task(), module_args)
    assert am._task.args.get('dest', None) == '/path/to/file.txt'
    assert am._task.args.get('src', None) is None



# Generated at 2022-06-13 09:40:30.503196
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    connection = ConnectionMock()
    module = ActionModuleMock(connection, {'path': 'tmp', 'other': 'things'})
    # TODO: Add a test for ActionModule.run()
    # assert module.run(tmp=None, task_vars=None) == {"invocation": {"module_args": {"path": "tmp", "other": "things"}}}


# Generated at 2022-06-13 09:40:38.505516
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(task=Mock(), connection=Mock(), play_context=Mock(), loader=Mock(), templar=Mock(), shared_loader_obj=Mock())

    assert action_module._task is not None
    assert action_module._connection is not None
    assert action_module._play_context is not None
    assert action_module._loader is not None
    assert action_module._templar is not None
    assert action_module._shared_loader_obj is not None
