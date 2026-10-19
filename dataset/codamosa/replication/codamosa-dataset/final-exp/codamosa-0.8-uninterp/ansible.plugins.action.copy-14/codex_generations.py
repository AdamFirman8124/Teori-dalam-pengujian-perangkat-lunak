

# Generated at 2022-06-13 09:34:55.823614
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    arguments = dict(
        dest='',
        remote_src=False,
        local_follow=True,
        follow=False,
        content='',
        src=''
    )
    task_vars = dict()
    tmpdir = os.path.abspath('/tmp')

    m = ActionModule(tmp=tmpdir, task_vars=task_vars, **arguments)
    m._execute_module = mock.Mock()
    m._copy_file = mock.Mock()
    m._find_needle = mock.Mock()
    m._loader = mock.Mock()
    m._remove_tmp_path = mock.Mock()
    m._execute_remote_stat = mock.Mock()
    m._remote_expand_user = mock.Mock()
    m._remove_

# Generated at 2022-06-13 09:34:58.880110
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule({}, {}, '/home', False, False, None)
    assert isinstance(action_module, ActionModule)
    action_module = ActionModule({}, {}, '/home', False, False, None)
    assert isinstance(action_module, ActionModule)

# Generated at 2022-06-13 09:35:09.959539
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Build a fake task
    task = Task()

    # Build a fake play context
    play_context = PlayContext()
    play_context.remote_addr = 'remote_addr'
    play_context.port = 'port'
    play_context.remote_user = 'remote_user'
    play_context.password = 'password'
    play_context.connection = 'connection'
    play_context.timeout = 'timeout'
    play_context.shell = 'shell'
    play_context.become = 'become'
    play_context.become_method = 'become_method'
    play_context.become_user = 'become_user'
    play_context.become_pass = 'become_pass'
    play_context.no_log = 'no_log'

# Generated at 2022-06-13 09:35:10.628180
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 09:35:20.462828
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''Unit test for method run of class ActionModule'''
    task = Mock()
    task.args = dict()
    # _transfer_str should equal to "ansible.legacy.copy"
    task._transfer_str = "ansible.legacy.copy"

    tmp = None
    task_vars = dict()

    action_module = ActionModule(task, tmp, task_vars)
    result = action_module.run(tmp, task_vars)
    assert result.get('failed')
    assert result['msg'] == 'src (or content) is required'

    action_module = ActionModule(task, tmp, task_vars)
    result = action_module.run(tmp, task_vars)
    assert result.get('failed')

# Generated at 2022-06-13 09:35:24.624323
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Testing action module
    mod = ActionModule(dict(ANSIBLE_MODULE_ARGS=dict(dest="", src="", content="")))
    result = mod.run(None, dict(localhost=dict()))
    assert result['invocation']['module_args']['dest'] == ""
    assert result['invocation']['module_args']['src'] == ""
    assert result['invocation']['module_args']['content'] == ""
    assert result['failed'] == True

# Generated at 2022-06-13 09:35:35.551535
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.action.copy import ActionModule
    from ansible.errors import AnsibleError
    from ansible.module_utils._text import to_bytes
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.executor.task_result import TaskResult
    from ansible.executor.process.worker import WorkerProcess
    from ansible.executor.process.result import ResultProcess

    loader = DataLoader()
    host = Host(name="foo")

# Generated at 2022-06-13 09:35:46.683815
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''
    Unit test for method run of class ActionModule.
    '''
    tmp = tempfile.mktemp()
    task_vars = {}

    # Initialize a ActionModule object for testing
    obj = ActionModule()
    obj._task = dict(args=dict(src='test_src', remote_src=True))
    obj._initialize_module_arguments()
    obj._task.args.update(dict(remote_user='test', module_name='test'))

    # If a task does not have a "name" attribute, the result should be failed
    result = obj.run(task_vars=task_vars, tmp=tmp)
    assert 'failed' in result

    # If a task does not have a "args" attribute, the result should be failed
    obj._task = dict(name='test')


# Generated at 2022-06-13 09:35:51.821529
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(None, None)
    assert module._task is None
    assert module._connection is None
    assert isinstance(module._loader, DataLoader)
    assert isinstance(module._templar, Templar)
    assert isinstance(module._shared_loader_obj, SharedPluginLoaderObj)

# Generated at 2022-06-13 09:35:56.930323
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Test with valid invocation
    task_vars = dict(
        ansible_connection="local",
        ansible_python_interpreter="/usr/bin/python"
    )
    action_mod = ActionModule(dict(), task_vars=task_vars)

    # Test with invalid invocation
    action_mod = ActionModule(dict(), task_vars={})


# Generated at 2022-06-13 09:36:44.585921
# Unit test for constructor of class ActionModule
def test_ActionModule():
    connection = Connection(None)
    tmp = connection._shell.tmpdir
    task = Task()
    action = ActionModule(task, connection, tmp, {})
    assert isinstance(action, ActionModule)


# Generated at 2022-06-13 09:36:50.447609
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module_return = dict(failed=True, changed=False)

    module_return['stdout'] = '''
        An error occurred
        '''

    module_return['stdout_lines'] = [
        'An error occurred',
    ]


    module_return['stderr'] = ''

    module_return['stderr_lines'] = ''

    module_return['rc'] = 1

    action_module_run = ActionModule(
        task=dict(role='test'),
        connection=None,
        play_context=None,
        loader=None,
        templar=None,
        shared_loader_obj=None
    )
    result = dict()

    result['dest'] = 'test'

    result['failed'] = False

    result['fetched'] = None

    result['src'] = 'test'

# Generated at 2022-06-13 09:36:52.168477
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule()
    assert action_module

# Generated at 2022-06-13 09:36:53.233128
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 09:36:53.870563
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True

# Generated at 2022-06-13 09:37:06.365816
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """
    Unit test for method run of class ActionModule
    """
    # Initialize mock task
    task = Task()
    task.args = dict()
    task.args['remote_src'] = True
    task.args['src'] = '/tmp'
    task.args['dest'] = '/tmp'

    # Create a mock inventory
    inventory = Inventory()

    # Create a mock variable manager
    variableManager = VariableManager()
    variableManager.extra_vars = dict()
    variableManager.extra_vars['foo'] = 'bar'
    variableManager.extra_vars['foo1'] = 'bar1'

    # Create a mock loader
    loader = DataLoader()

    # Create a mock connection
    connection = Connection()

    # Initialize action
    action = ActionModule(task, connection, variableManager, loader)

   

# Generated at 2022-06-13 09:37:09.177999
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Setup mock
    ActionModule(task=dict(args=dict(src='foo', dest='bar', mode='preserve'),
                   task_vars={'role_path': '/test/path'}))


# Generated at 2022-06-13 09:37:21.134841
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils.basic import AnsibleModule, AnsibleFallbackNotFound, AnsibleFileNotFound, AnsibleError
    from ansible.utils.path import unfrackpath
    from copy import copy

    def _walk_dirs(path, local_follow=True, trailing_slash_detector=None):
        result = {'files': [], 'directories': [], 'symlinks': []}
        for root, dirs, files in os.walk(path):
            relative_root = unfrackpath(root, path)
            if relative_root:
                dest_root = relative_root
            else:
                dest_root = ''
            # do not descend into symlinks


# Generated at 2022-06-13 09:37:28.103530
# Unit test for constructor of class ActionModule
def test_ActionModule():
    conn = Mock(spec=Connection)
    tmp = tempfile.mkdtemp(dir=C.DEFAULT_LOCAL_TMP, prefix='ansible-tmp')
    tmp_shell = tempfile.mkdtemp(dir=C.DEFAULT_LOCAL_TMP, prefix='ansible-tmp')

    c = AnsibleConnection(conn)
    c._shell = Mock(spec=ShellModule)
    c._shell.path_has_trailing_slash = Mock(return_value=True)
    c._shell.join_path = Mock(return_value=os.path.sep.join(['test_result', 'new_path']))
    c._shell.tempdir = tmp_shell
    c._shell.env_prefix = None

# Generated at 2022-06-13 09:37:43.366316
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''
    ActionModule.run()
    '''
    module = ActionModule(
        task=dict(
            args=dict(
                dest='/root/test.txt',
                src='/etc/hosts',
            )
        ),
        connection=dict(
            _shell=dict(
                path_has_trailing_slash=path_has_trailing_slash,
                join_path=join_path
            )
        ),
        task_vars=dict(
            ansible_user_id='root'
        ),
    )
    module.run()
    assert not module._result.get('failed')

# Generated at 2022-06-13 09:39:27.299944
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Test if run will return the correct value
    inventory = InventoryManager(Loader(), sources='localhost,')
    variable_manager = VariableManager(inventory)
    loader = DataLoader()
    options = Options(connection='local', module_path=['./library'], forks=100, become=False, become_method=None, become_user=None, check=False, diff=False)
    passwords = dict()

# Generated at 2022-06-13 09:39:35.415678
# Unit test for constructor of class ActionModule
def test_ActionModule():
    loader = DictDataLoader({
        "test_host": {
            "hosts": ["test_host"],
            "vars": {
                "test_var": "test_value",
                "src": "test_src_value",
            }
        }
    })
    inventory = Inventory(loader=loader)
    task = Task.load(dict(
        name="test_task",
        action="test_action",
        become=False,
        connection="local",
        delegate_to="test_host",
        args=dict(
            test_args="test_args_value",
            src="{{ src }}",
        )
    ))
    host = inventory.get_host("test_host")
    # Initialize a connection
    connection = Connection(host, task)

    # Test simple constructor
    test_action

# Generated at 2022-06-13 09:39:36.025457
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 09:39:48.436947
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Create an instance
    action_module_instance = ActionModule()
    # Initialize mock
    action_module_instance._remote_user = 'ansible'
    action_module_instance._task = dict()
    action_module_instance._task.args = dict()
    action_module_instance._task.args = {'content': '(Content)', 'dest': '/home/ansible/testdir/testdir/'}
    action_module_instance._task.action = 'copy'
    action_module_instance._task.tags = ['role_tests', 'test_copy_module']
    action_module_instance._task.role = 'files'

    action_module_instance._connection = mock.MagicMock()
    action_module_instance._execute_module = mock.MagicMock()
    action_module_instance._remove_

# Generated at 2022-06-13 09:39:58.064483
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    source = "/home/ansible/test.txt"
    source_rel = "test.txt"
    content = "test"
    dest = "/home/ansible/test2.txt"

    class Task(object):
        def __init__(self):
            self.args = {
                'src': source,
                'dest': dest
            }

    class ModuleUtils(object):
        def __init__(self):
            self.tmp = None
            self.tmpdir = "/tmp/ansible"

    class Connection(object):
        def __init__(self):
            self.shell = ModuleUtils()

    class Runner(object):
        def __init__(self):
            self._connection = Connection()


# Generated at 2022-06-13 09:40:08.885171
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import os
    import tempfile
    import filecmp
    import shutil
    import stat
    import subprocess

    # make a tmp dir to store a file to move
    src_dir = tempfile.mkdtemp()
    dest_dir = tempfile.mkdtemp()

    data_to_write = "a" * 1024 * 1024 * 2  # 2 MB
    # create a file with 2 MB of data
    src_path = os.path.join(src_dir, "file")
    with open(src_path, 'wb') as f:
        f.write(data_to_write)

    # create a tmp file for ansible to write src_path to
    # and put it in the same dir as src_path to avoid
    # a copy

# Generated at 2022-06-13 09:40:17.861753
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ''' Test method run of class ActionModule. '''
    action_module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    action_module._create_content_tempfile = Mock()
    action_module._remove_tempfile_if_content_defined = Mock()
    action_module._execute_module = Mock()
    action_module._execute_module.return_value = {}
    action_module._find_needle = Mock()
    action_module._find_needle.side_effect = mock_find_needle
    action_module._walk_dirs = Mock()
    action_module._walk_dirs.side_effect = mock_walk_dirs
    action_module._remote_expand_user = Mock()


# Generated at 2022-06-13 09:40:18.461311
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 09:40:22.397520
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # test 200 OK
    response = requests.get('http://127.0.0.1:8000/api/hello_world/?name=wangbin')

# Generated at 2022-06-13 09:40:37.441198
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''
    Unit test for constructor of class ActionModule
    '''
    action_module = ActionModule()
    assert action_module._supports_check_mode is True
    assert action_module._supports_async is True
    assert action_module._supports_diff is True
    # The following line will fail if you have unpinned ansible installed
    # assert action_module._action_version == 2
    assert action_module._action_version == 1
    assert action_module._action_name == 'copy'
    assert action_module._action_name == action_module.name
    assert action_module._action_name == action_module.short_name
    assert action_module.action == 'copy'
    assert action_module.module_name == 'ansible.legacy.copy'
    assert action_module.module_