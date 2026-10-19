

# Generated at 2022-06-13 09:23:53.729907
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """
    constructor test for ActionModule
    """
    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play

    task = Task()
    play_context = PlayContext()
    play = Play()

    act = ActionModule(task, play_context, play)
    assert act._supports_check_mode == False

# Generated at 2022-06-13 09:24:04.649238
# Unit test for constructor of class ActionModule
def test_ActionModule():

    # Constructor sets variables
    # Unit test for ActionModule.run()
    # Case 1: dest=None
    # Case 2: dest is not directory
    # Case 3: local assemble
    # Case 4: remote assemble
    # Case 5: delimiter used
    # Case 6: regexp used
    # Case 7: follow=True
    # Case 8: ignore_hidden=True

    # Test cases are nested because they use the variables set by the
    # previous test cases.
    # TODO: refactor code to allow test cases to be independent

    # Test case 1: dest = None
    AM = ActionModule()
    AM.run(tmp=None, task_vars=dict())

    # Test case 2: dest is not directory
    os.mkdir("/tmp/test")
    os.mkdir("/tmp/test/src")

# Generated at 2022-06-13 09:24:07.859781
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(None, None, None)
    assert module.TRANSFERS_FILES == True

# Generated at 2022-06-13 09:24:15.573826
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    print ('Testing ActionModule.run')

    # stubbed task_vars, used in setting up mocks
    task_vars = {
        'ansible_default_ipv4': {'address': '192.168.1.100'},
        'ansible_connection': 'local',
        'ansible_diff_files': True,
        'ansible_python_interpreter': '/usr/bin/python3',
        'ansible_playbook_python': '/usr/bin/python3',
        'ansible_play_hosts_all': ['127.0.0.1'],
        'ansible_version': {'full': '2.99.0'},
    }

    # the return value for module_executor.run

# Generated at 2022-06-13 09:24:19.543208
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule(None, None, None, None, None, None)
    # Let's make sure the ActionModule isn't a no-op
    assert am.run(task_vars=None) == {}

# Generated at 2022-06-13 09:24:28.568596
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Set up the class object
    data = {
        'name': 'file',
        'args': {
            'dest':'/tmp/ansible_test.txt',
            'src':'/tmp/ansible_src',
            'regexp':'.*',
            'remote_src':'True',
            'delimiter':'','ignore_hidden':False
        },
        'delegate_to': None,
        'delegate_facts': False,
        'module_vars': {},
        'register': '',
        'run_once': False,
        'no_log': False
    }
    obj = ActionModule(data)
    obj._remove_tmp_path('random_dir')

# Generated at 2022-06-13 09:24:33.818059
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    msg = '''TASK [assemble] 
    **************************************************************************************************
    fatal: [localhost]: FAILED! => {"changed": false, "failed": true, "msg": "src and dest are required"}
    ...ignoring
    '''

    action_module = ActionModule()

    # test exception
    res = action_module.run()

    assert msg in res

# Generated at 2022-06-13 09:24:44.410987
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # pylint: disable=too-few-public-methods
    class ModuleResult(object):
        def __init__(self):
            self.changed = False
            self.msg = 'ok'

    class TaskResult(object):
        def __init__(self, result, changed=False):
            self.result = result
            self.changed = changed

    # pylint: disable=too-few-public-methods
    class Connection(object):
        def __init__(self):
            self.tmpdir = 'tmpdir'

        class _shell(object):
            @staticmethod
            def join_path(path1, path2):
                return '%s/%s' % (path1, path2)


# Generated at 2022-06-13 09:24:47.245878
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(task='set_fact', task_vars={}, stretch=False)._task.action == 'set_fact'

# Generated at 2022-06-13 09:24:59.461110
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    mock_connection = MockConnection()
    task_args = dict()
    action_module = ActionModule(mock_connection, task_args)
    task_vars = dict()
    result = action_module.run(None, task_vars)
    # Assertion
    assert result == dict(
        failed=True,
        msg='src and dest are required'
    )
    mock_connection.reset()

    task_args = dict(src=None)
    action_module = ActionModule(mock_connection, task_args)
    result = action_module.run(None, task_vars)
    # Assertion
    assert result == dict(
        failed=True,
        msg='src and dest are required'
    )
    mock_connection.reset()

    task_args = dict(dest=None)

# Generated at 2022-06-13 09:25:14.046980
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # create mock task_vars
    task_vars = dict()
    # create mock AnsiblePlugin
    action_plugin = AnsiblePlugin()
    # create object of ActionModule
    action_module = ActionModule(task=action_plugin, connection=action_plugin, play_context=action_plugin, loader=action_plugin, templar=action_plugin, shared_loader_obj=action_plugin)
    # run method of class ActionModule
    result = action_module.run(task_vars=task_vars)
    # assert result
    assert result is not None

# Generated at 2022-06-13 09:25:16.773642
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule()
    assert action._supports_check_mode is False


# Generated at 2022-06-13 09:25:20.381984
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule()
    print(action_module)
    print('ok')

if __name__ == "__main__":
    test_ActionModule()

# Generated at 2022-06-13 09:25:21.109976
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 09:25:34.254740
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import inspect
    import tempfile

    # create a test repo with a file
    repo_path = tempfile.mkdtemp()
    file_path = os.path.join(repo_path, "file")
    with open(file_path, "w") as f:
        f.write("some content")
    repo_path_remote = repo_path.replace(os.path.sep, os.path.altsep)

    # create an assembly dir in the test repo
    assembly_dir = os.path.join(repo_path, "_assembly")
    os.makedirs(assembly_dir)
    assembly_dir_remote = assembly_dir.replace(os.path.sep, os.path.altsep)

    # create a tmpdir
    tmpdir = tempfile.mkdtemp()
    tmpdir

# Generated at 2022-06-13 09:25:46.142660
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Test with bad task_vars and all_vars arguments
    action_module = ActionModule(
        task=None,
        connection=None,
        play_context=None,
        loader=None,
        templar=None,
        shared_loader_obj=None,
    )
    assert action_module.task is None
    assert action_module.connection is None
    assert action_module.play_context is None
    assert action_module.loader is None
    assert action_module.templar is None
    assert action_module.shared_loader_obj is None


# Generated at 2022-06-13 09:25:46.720275
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action = ActionModule()

# Generated at 2022-06-13 09:25:55.634620
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # dest is None
    actionmodule = ActionModule(load_fixture('test_module.py', 'action_plugins'), 'test_module', {}, load_fixture('test_runner.py', 'lib'))
    res = actionmodule.run(tmp='.', task_vars={})
    assert 'dest is required' in res.get('msg')
    assert 'skipped' in res.get('skipped')
    assert not 'failed' in res.get('skipped')
    assert not res.get('tmp')
    assert not 'rc' in res

    # src is None
    actionmodule = ActionModule(load_fixture('test_module.py', 'action_plugins'), 'test_module', {}, load_fixture('test_runner.py', 'lib'))

# Generated at 2022-06-13 09:25:56.362247
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert False


# Generated at 2022-06-13 09:25:59.855484
# Unit test for constructor of class ActionModule
def test_ActionModule():
    tmp=None
    task_vars = None
    action_module=ActionModule(tmp, task_vars)
    print(action_module)

# Generated at 2022-06-13 09:26:25.615619
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert action.supports_check_mode is False
    assert action.supports_async is False
    assert action.async_seconds == 0
    assert action.async_poll_interval == 1
    assert action.TRANSFERS_FILES


# Generated at 2022-06-13 09:26:26.763599
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert False, 'Need to write unit tests for ActionModule'

# Generated at 2022-06-13 09:26:32.857099
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''
    Unit test for constructor of class ActionModule
    '''

    a = ActionModule(loader=None, task=None, connection=None,
                     play_context=None, loader_path=None,
                     shared_loader_obj=None, final_q=None,
                     no_log=False, options=None, variable_manager=None)
    assert a is not None

# Generated at 2022-06-13 09:26:33.512436
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 09:26:37.210059
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(connection=None, runner_connection=None, task=None, play_context=None, loader=None, shared_loader_obj=None, final_q=None)

# Generated at 2022-06-13 09:26:51.010106
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # pylint: disable=protected-access
    # mock
    from ansible.module_utils.basic import AnsibleModule

    am = ActionModule(AnsibleModule, 'copy', {}, fixed_tmp_path='a', _ansible_selinux_special_fs=True, _ansible_tmpdir='b')

    am._task = 'c'
    am._task.args = {'src': 'd', 'dest': 'e', 'remote_src':'f', 'regexp':'g', 'delimiter':'h', 'ignore_hidden':'i', 'decrypt':'j'}
    am._supports_check_mode = False
    am._connection = 'k'
    am._connection.shell = 'l'
    am._connection.shell.tmpdir = 'm'
    am._loader

# Generated at 2022-06-13 09:27:00.853548
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Create a temporary directory
    temp_dir = tempfile.mkdtemp()
    # Create file1 in temporary directory
    file1 = tempfile.NamedTemporaryFile(dir=temp_dir, delete=False)
    # Create file2 in temporary directory
    file2 = tempfile.NamedTemporaryFile(dir=temp_dir, delete=False)
    # Write data to file1
    file1.write(b"""abc\n""")
    file1.close()
    # Write data to file2
    file2.write(b"""def\n""")
    file2.close()

    # Create a temporary directory
    temp_dir2 = tempfile.mkdtemp()
    # Create file3 in temporary directory

# Generated at 2022-06-13 09:27:01.386652
# Unit test for method run of class ActionModule
def test_ActionModule_run():
	assert True == 1

# Generated at 2022-06-13 09:27:04.996324
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    instance = ActionModule(task=dict(), connection=dict(), play_context=dict(), loader=dict(), templar=dict(), shared_loader_obj=None)
    assert isinstance(instance.run(), dict)

# Generated at 2022-06-13 09:27:06.630230
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = ActionModule()
    return True

# Generated at 2022-06-13 09:27:46.871591
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule()
    assert not action_module is None

# Generated at 2022-06-13 09:27:48.995667
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert_equals = 'assert_equals'
    assert_equals(type(ActionModule), type)

# Generated at 2022-06-13 09:27:53.088225
# Unit test for constructor of class ActionModule
def test_ActionModule():
    dest = 'dest'
    host = 'host'
    taskVars = 'taskVars'
    tmp = 'tmp'

    action = ActionModule(dest, host, taskVars, tmp)

    assert action.name == 'A'
    assert action.action_type == 'A'
    assert action._task.args['dest'] == 'dest'
    assert action._task.args['host'] == 'host'
    assert action._task.args['taskVars'] == 'taskVars'
    assert action._task.args['tmp'] == 'tmp'
    assert action._supports_async == False
    assert action._supports_check_mode == True
    assert action._supports_static_basic_auth == False
    assert action._supports_sub_tasks == False

# Generated at 2022-06-13 09:27:59.161882
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.play_context import PlayContext
    from ansible.utils.vars import combine_vars
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText
    from ansible.vars.unsafe_proxy import AnsibleUnsafeBytes
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    import ansible.constants as C

    C.DEFAULT_HASH_BEHAVIOUR = "md5"
    C.DEFAULT_HASH_VERIFY = True


# Generated at 2022-06-13 09:28:02.479149
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Case1: Constructing an ActionModule with all the right params
    action_module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert action_module is not None

# Generated at 2022-06-13 09:28:03.051527
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 09:28:14.533072
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # This is a very simple test to exercise the code paths.
    # A better test would be to compare the output from the module
    # against the actual contents of the files and the assembled file.

    # Set up a fake task and action module.
    task_vars = dict()
    task = dict(action=dict(module_name='assemble', args=dict(src='/doesnotexist', dest='/doesnotexist')))

    # Set up a fake connection and play context to exercise the code path
    # that deals with remote_src=no.
    connection = dict(name='local')
    pc = dict(connection=connection, remote_addr='localhost', remote_user='test', diff=True)

    # Set up a fake action module with an empty _execute_module method.

# Generated at 2022-06-13 09:28:15.960680
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass


# Generated at 2022-06-13 09:28:25.775864
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # This unit test covers patch from PR #34244
    from ansible.module_utils.connection import Connection
    from ansible.module_utils.six import StringIO as sixStringIO
    from ansible.plugins.action.assemble import ActionModule as AssembleActionModule
    from ansible.utils.path import unfrackpath
    from ansible.utils.display import Display
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.utils.vars import combine_vars

# Generated at 2022-06-13 09:28:26.207399
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 09:29:50.179430
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule(None, None, None, None)
    assert module
    assert module.run()    # if no exception thrown we assume it's all good

# Generated at 2022-06-13 09:29:54.313628
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager

    pc = PlayContext()
    var_manager = VariableManager()
    test_module = ActionModule(pc, var_manager)

    assert test_module is not None

# Generated at 2022-06-13 09:29:56.903288
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule()
    assert action_module.TRANSFERS_FILES is True
    assert hasattr(action_module, 'run')
    assert hasattr(action_module, '_assemble_from_fragments')

# Generated at 2022-06-13 09:30:01.002950
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.module_utils.basic import AnsibleModule
    am = ActionModule(AnsibleModule({'src':'/home/ansiball/src','dest':'/home/ansiball/dest','delimiter':'','regexp':'','follow':False,'ignore_hidden':False,'decrypt':True}))
    print (am.run(None,None))

# Generated at 2022-06-13 09:30:05.169758
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule({'src': 'src', 'dest': 'dest'})
    assert am._task.args['src'] == 'src'
    assert am._task.args['dest'] == 'dest'
    assert am._name == 'assemble'

# Unit tests for _assemble_from_fragments method of class ActionModule

# Generated at 2022-06-13 09:30:05.694641
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 09:30:06.300645
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 09:30:06.812503
# Unit test for constructor of class ActionModule
def test_ActionModule():
    ActionModule()

# Generated at 2022-06-13 09:30:07.317544
# Unit test for constructor of class ActionModule
def test_ActionModule():
    pass

# Generated at 2022-06-13 09:30:10.078964
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule()


if __name__ == '__main__':
    import sys
    test_ActionModule()
    sys.exit(0)

# Generated at 2022-06-13 09:33:21.482688
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''
    Test case:
    '''
    os.environ['HOME'] = '/home/fakeuser'
    am = ActionModule(dict(
        _task=None,
        _connection=None,
        _play_context=None,
        _loader=None,
        _templar=None,
        _shared_loader_obj=None
    ), 'ansible.legacy.assemble')
    assert am is not None
    assert am._task is None
    assert am._connection is None
    assert am._play_context is None
    assert am._loader is None
    assert am._templar is None
    assert am._shared_loader_obj is None


# Generated at 2022-06-13 09:33:30.377339
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule(None, dict())

    test_src = "test_src"
    test_dest = "test_dest"
    test_delimiter = None
    test_remote_src = "yes"
    test_regexp = None
    test_follow = False
    test_ignore_hidden = False
    test_decrypt = True
    test_args = dict()
    test_args['src'] = test_src
    test_args['dest'] = test_dest
    test_args['delimiter'] = test_delimiter
    test_args['remote_src'] = test_remote_src
    test_args['regexp'] = test_regexp
    test_args['follow'] = test_follow
    test_args['ignore_hidden'] = test_ignore_hidden

# Generated at 2022-06-13 09:33:41.332282
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    import copy
    import lib.action_plugins.action_assemble as assemble_mod

    def test_action_given_non_None_tmp_dir_return_non_None_result(_tmpdir):
        _action = assemble_mod.ActionModule(None, None)
        _action._task = None
        _result = _action.run(_tmpdir)

        assert _result is not None
        assert 'failed' in _result
        assert _result['failed']

        assert 'rc' in _result
        assert _result['rc'] == 1

        assert 'msg' in _result
        assert isinstance(_result['msg'], assemble_mod.unicode)

    def test_action_given_None_tmp_dir_return_non_None_result():
        _action = assemble_mod.ActionModule(None, None)
        _action