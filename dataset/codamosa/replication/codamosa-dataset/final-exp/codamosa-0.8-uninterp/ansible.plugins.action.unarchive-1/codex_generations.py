

# Generated at 2022-06-13 10:52:59.401994
# Unit test for method run of class ActionModule

# Generated at 2022-06-13 10:53:06.611207
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    mod = ActionModule()
    mod._task.args = {'dest': '/home/ansible', 'src': '/home/ansible/foo.tgz', 'remote_src': False}
    mod._task.args['copy'] = False
    # CCTODO: Add test for Windows hosts.
    assert mod.run() == {'changed': 'changed'}

    mod._task.args['dest'] = '/home/ansible'
    mod._task.args['creates'] = '/home/ansible/foo.tgz'
    mod._task.args['remote_src'] = False
    mod._task.args['copy'] = False
    # CCTODO: Add test for Windows hosts.
    assert mod.run() == {'changed': 'changed'}


# Generated at 2022-06-13 10:53:12.960665
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import unittest
    import ansible.constants as C

    class TestActionModule(unittest.TestCase):
        def setUp(self):
            pass

        def tearDown(self):
            pass

        @unittest.skip("Needs to be implemented")
        def test_run(self):
            self.assertFalse(True)

    C.DEFAULT_HOST_LIST = 'localhost'
    C.DEFAULT_MODULE_PATH = 'library'
    C.DEFAULT_MODULE_NAME = 'debug'
    unittest.main()

# Generated at 2022-06-13 10:53:24.809006
# Unit test for constructor of class ActionModule
def test_ActionModule():
    fake_loader = object()
    fake_task = object()
    fake_connection = object()
    fake_play_context = object()

    # Ensure no arguments produces the expected initialized class
    action_module = ActionModule(fake_loader, fake_task, fake_connection, fake_play_context)

    # Ensure the properties are as expected
    assert action_module._loader == fake_loader
    assert action_module._task == fake_task
    assert action_module._connection == fake_connection
    assert action_module._play_context == fake_play_context

    # Ensure no arguments produces the expected initialized class
    action_module = ActionModule(fake_loader, fake_task, fake_connection, fake_play_context, task_vars=dict())

    # Ensure the properties are as expected
    assert action_module._loader == fake_loader


# Generated at 2022-06-13 10:53:34.898583
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # arrange
    _ActionBase = ActionBase()
    _ActionBase.runner_path = 'ansible.runner'
    _ActionBase._shared_loader_obj = 'ansible.parsing.dataloader.DataLoader'
    _ActionBase._task = "task_instance"
    _ActionBase.datastructure_filename = 'ansible/playbooks/playbooks'
    _ActionBase.playbook = 'playbook_instance'
    _ActionBase.play = 'play_instance'
    _ActionBase._play_context = 'play_context'

# Generated at 2022-06-13 10:53:45.515263
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """ Unit test for constructor of class ActionModule. """

    #
    # Test the constructor for class ActionModule, with valid parameters
    #
    try:
        obj = ActionModule(
            task=dict(args=dict(src="src_file", dest="dest_file")),
            connection=dict(),
            play_context=dict(),
            loader=None,
            templar=None,
            shared_loader_obj=None)
    except Exception as e:
        raise Exception(e)

    #
    # Test the constructor for class ActionModule, with invalid parameter
    #
    try:
        obj = ActionModule()
        raise Exception('Expected ValueError but none occurred!')
    except ValueError:
        pass

    #
    # Run test_ActionModule() to test the constructor of class ActionModule
    #
    test_

# Generated at 2022-06-13 10:53:46.342360
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True

# Generated at 2022-06-13 10:53:46.981718
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:53:49.126337
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Don't require any parameters passed to unarchive, so don't pass any.
    action_module = ActionModule()

    # Test that the constructor return the correct object type.
    assert isinstance(action_module, ActionModule)

# Generated at 2022-06-13 10:53:50.424596
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Create an instance of class ActionModule
    # CCTODO: write unit tests
    pass

# Generated at 2022-06-13 10:53:58.954472
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:54:06.464467
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.module_utils.common.removed import removed_module
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.vars.manager import VariableManager

    playbook = Play()
    inventory = playbook.inventory
    loader = DataLoader()
    tqm = TaskQueueManager(
        inventory=inventory,
        variable_manager=VariableManager(),
        loader=loader,
        passwords=dict(),
    )

    play_context = dict(
        remote_user='test_remote_user',
    )


# Generated at 2022-06-13 10:54:15.492556
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Create an instance of class ActionModule to test.
    args = [
        'src="/tmp/example.tgz"',
        'dest="/tmp/"'
    ]
    task_vars = {}
    _task = dict(args=list(args))
    action = ActionModule(task=_task, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

    # Fake the _execute_remote_stat method to return a value that
    # indicates that the destination exists and is a directory.
    action._execute_remote_stat = lambda *args1: dict(exists=True, isdir=True)

    # Fake the _remote_file_exists method to return False so that
    # the test can avoid checking for an existent remote file.
    action._remote_file

# Generated at 2022-06-13 10:54:16.360686
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule()

# Generated at 2022-06-13 10:54:18.857005
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Patching the test execution
    # TODO: Add tests for the ActionModule class
    pass

# Generated at 2022-06-13 10:54:31.703883
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    errMsg = "success"
    try:
        # CCTODO: Figure out how to provide a mock_loader here.
        mock_actionBase = ActionBase(task=dict(), connection=dict(), play_context=dict(), loader=dict(), templar=dict(), shared_loader_obj=dict())
        result = ActionModule.run(mock_actionBase, tmp=None, task_vars=None)
        errMsg = "failed to raise AnsibleActionSkip('skipped, since %s exists')" % creates
        assert result.get('skipped', False)
    except AnsibleActionSkip as e:
        if e != "skipped, since %s exists" % creates:
            raise
    except Exception:
        raise Exception(errMsg)

# Generated at 2022-06-13 10:54:42.211345
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Create an instance of ActionModule that we can use to call the method run
    from ansible.plugins.action.copy import ActionModule
    from ansible.playbook.task import Task
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.executor.executor import PlaybookExecutor
    from ansible.plugins.loader import loader, action_loader
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.inventory.host import Host
    from ansible.playbook.play import Play
    from ansible.playbook import inline_data
    import json
    import io

# Generated at 2022-06-13 10:54:52.304806
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ActionModule = reload(ActionModule)
    print("Test ActionModule method run()")

    # arrange.
    task_args = {
        'arg1': 'arg1',
        'arg2': 'arg2'
    }
    task_vars = {
        'var1': 'var1',
        'var2': 'var2'
    }

    # act.
    action_module = ActionModule(task_args, {})
    result = action_module.run(task_vars)

    # assert.
    assert result['changed'] is False
    assert 'msg' in result
    assert 'failed' not in result
    assert 'invocation' in result
    assert 'rc' in result
    assert 'stderr' in result
    assert 'stdout' in result
    assert 'stdout_lines' in result

# Generated at 2022-06-13 10:54:58.089059
# Unit test for constructor of class ActionModule
def test_ActionModule():
    connection_mock = ConnectionMock()
    task_mock = TaskMock()
    task_vars = {}
    loader_mock = DataLoaderMock()
    templar_mock = TemplarMock()
    test_object = ActionModule(connection_mock, task_mock, task_vars, loader_mock, templar_mock)
    return test_object



# Generated at 2022-06-13 10:54:58.785093
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert True

# Generated at 2022-06-13 10:55:16.009066
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Unit test stub
    # No real test here, just making sure this compiles.
    am = ActionModule()

# Generated at 2022-06-13 10:55:17.105103
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert False

# Generated at 2022-06-13 10:55:21.414229
# Unit test for constructor of class ActionModule
def test_ActionModule():
    mod = ActionModule({'src': 'src'}, {'dest': 'dest'})
    assert mod.action_name == 'unarchive'
    assert mod._task.args['src'] == 'src'
    assert mod._task.args['dest'] == 'dest'

# Generated at 2022-06-13 10:55:30.344989
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(task=dict(action=dict(module_name='unarchive', src='/tmp/foo/archive.tar', dest='/tmp/bar')))
    assert module._task == {'action': {'module_name': 'unarchive'}, 'args': {'dest': '/tmp/bar', 'src': '/tmp/foo/archive.tar'}}
    assert module._task.action == {'module_name': 'unarchive'}
    assert module._task.action.module_name == 'unarchive'
    assert module._task.args == {'dest': '/tmp/bar', 'src': '/tmp/foo/archive.tar'}
    assert module._task.args.dest == '/tmp/bar'
    assert module._task.args.src == '/tmp/foo/archive.tar'
    # FIXME: test _

# Generated at 2022-06-13 10:55:33.005430
# Unit test for constructor of class ActionModule
def test_ActionModule():

    # Create an instance of the ActionModule class and test it
    actionModule = ActionModule(loader=None, task=None, connection=None)
    assert isinstance(actionModule, ActionModule)

# Generated at 2022-06-13 10:55:35.619270
# Unit test for method run of class ActionModule
def test_ActionModule_run():
  # Create an instance of class ActionModule
  action_module_obj = ActionModule()
  print("ActionModule_run()")

# Generated at 2022-06-13 10:55:49.483742
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    def create_loader(val):
        # Create a memory loader for unit testing.
        class MemLoader:
            def get_real_file(self, val, decrypt=True):
                fakefile = val
                return fakefile
        return MemLoader()

    class Connection:
        class Shell:
            def join_path(self, curr_path, filename):
                # Pretend path join.
                return os.path.join(curr_path, filename)
            def tmpdir(self):
                # Pretend tmp dir.
                return "/tmp"

        def _shell(self):
            # Pretend to return a shell.
            return self.Shell()


# Generated at 2022-06-13 10:55:50.244464
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ActionModule.run()


# Generated at 2022-06-13 10:55:50.951446
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:55:53.591236
# Unit test for constructor of class ActionModule
def test_ActionModule():
    ansible_action_module = ActionModule()
    assert ansible_action_module is not None

# Generated at 2022-06-13 10:56:26.774916
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """
    Unit test for constructor of class ActionModule
    """
    theActionModule = ActionModule()
    theActionModule.run()

# Generated at 2022-06-13 10:56:31.045300
# Unit test for constructor of class ActionModule
def test_ActionModule():
    ua = ActionModule(task=dict(args=dict(src='/my/ansible/path/source.file.zip', dest='/my/destination/')))

    assert ua.run(tmp='/my/ansible/path')
    assert ua.run(tmp='/my/ansible/path') == {}

# Generated at 2022-06-13 10:56:39.935075
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.errors import AnsibleError
    from ansible.inventory.manager import InventoryManager
    from ansible.inventory.host import Host
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.plugins.loader import action_loader
    #from ansible.executor.task_executor import TaskExecutor
    import os
    import tempfile
    import json
    import shutil
    loader = DataLoader()
    host = Host('127.0.0.1')
    vault_

# Generated at 2022-06-13 10:56:40.542750
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:56:41.436319
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = ActionModule()

# Generated at 2022-06-13 10:56:49.087911
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import sys
    import os
    import tempfile
    temp_dir = tempfile.mkdtemp()
    copy_file = os.path.join(temp_dir, 'testfile')
    with open(copy_file, 'w') as f:
        f.write('testfile')
    unarchived_file = os.path.join(temp_dir, 'testfile.tar.gz')
    if sys.version_info[0] < 3:
        import tarfile
    else:
        import tarfile
    with tarfile.open(unarchived_file, 'w:gz') as tf:
        tf.add(copy_file, arcname=os.path.basename(copy_file))
    copy_file = os.path.join(temp_dir, 'testfile.tar.gz')
    unarchived_

# Generated at 2022-06-13 10:56:51.761864
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Initialize class
    action = ActionModule()
    # Run constructor
    assert action is not None

test_ActionModule()

# Generated at 2022-06-13 10:56:53.923808
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule(None, None, None, None, None, None)
    assert action is not None


# Generated at 2022-06-13 10:56:55.787964
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import os
    assert os.path.exists("ansible/plugins/action/unarchive.py") == True

# Generated at 2022-06-13 10:56:56.525634
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True

# Generated at 2022-06-13 10:58:02.900261
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = 'unarchive'
    kwargs = dict()
    module_args = dict()
    module_args['src'] = '/tmp/test.tar'
    module_args['dest'] = '/tmp/test'
    module_args['creates'] = '/tmp/test/'
    kwargs['module_args'] = module_args
    obj = ActionModule(None, None, **kwargs)
    #print(obj.run())
    pass

if __name__ == '__main__':
    test_ActionModule_run()

# Generated at 2022-06-13 10:58:04.263557
# Unit test for constructor of class ActionModule
def test_ActionModule():
    print("Testing ActionModule constructor")


# Generated at 2022-06-13 10:58:09.645833
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert (module is not None)
    assert module.TRANSFERS_FILES
    assert module.display.__doc__
    assert module.run.__doc__

# Generated at 2022-06-13 10:58:17.804780
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Load test data from yaml file
    import yaml
    stream = open('./test/unarchive_test.yml', 'r')
    data = yaml.load(stream)

    # Create object and send test data to the object
    a = ActionModule()
    a._task.args = data['arguments']
    a._task.action = 'unarchive'

    # Create expected result
    expected = data['expected']

    # Execute method and compare result
    assert a.run() == expected

# Generated at 2022-06-13 10:58:32.442481
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task import Task
    from ansible.executor.task_queue_manager import TaskQueueManager

    # create a task
    task = Task()
    task._ds = dict()
    task.args = dict()
    task.args['src'] = 'file.txt'
    task.args['dest'] = 'tmp'
    task.args['remote_src'] = 'True'
    task.args['creates'] = 'tmp/file.txt'
    task.args['decrypt'] = 'True'

    # create the task queue manager object
    tqm = TaskQueueManager(None)

    # create the action module object
    action = ActionModule(task, tqm._loader, tqm._shared_loader_obj, None)

    # run the unit test on the action module
    action.run

# Generated at 2022-06-13 10:58:33.269140
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass


# Generated at 2022-06-13 10:58:33.766852
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True

# Generated at 2022-06-13 10:58:42.039169
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Construct a fake AnsibleModule object
    am = AnsibleModule({})

    # Create a FakeV2Connection object
    fvd = FakeV2Connection("/tmp")

    # Create a ActionModule object
    ami = ActionModule(am, fvd)
    ami._tmpdir = '/tmp'
    ami._connection = fvd

    # Create a FakeV2Loader object
    fvl = FakeV2Loader({})
    ami._loader = fvl

    # Create a FakeV2ActionModule object
    ami2 = FakeV2ActionModule(ami)

    # Run the unit test
    result = ami2.run()

    # Test if the result is not empty
    if result:
        print("PASS: test_ActionModule_run")

# Generated at 2022-06-13 10:58:51.859734
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins import action_loaders

    '''
    Setting up variables for tests.
    '''
    run_module_result = {
        'cmd': 'tar -xzf /tmp/source -C /home/dylan/test',
        'changed': True,
        'end': '2017-05-12 23:33:57.774179',
        'failed': False,
        'rc': 0,
        'start': '2017-05-12 23:33:57.774094',
        'stderr': '',
        'stdout': '',
        'stdout_lines': [],
        'warnings': [],
    }

    # This is a simplified command_args dictionary object like it would be created
    # in the y

# Generated at 2022-06-13 10:58:56.588124
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''
    For now we just test that the class can be constructed.
    TODO: add more tests
    '''
    assert 'ActionModule' in globals()
    assert callable(ActionModule)
    assert issubclass(ActionModule, ActionBase)
    action_module = ActionModule(None, dict())
    assert action_module is not None
    assert isinstance(action_module, ActionBase)

# Generated at 2022-06-13 11:01:43.256485
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 11:01:47.838931
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(
        task=dict(action=dict(module='unarchive', src='/a/b/c', dest='/x/y/z')),
        connection=dict(),
        play_context=dict(),
        loader=dict(),
        templar=dict(),
        shared_loader_obj=None
    )
    assert module.TRANSFERS_FILES is True

# Generated at 2022-06-13 11:01:54.067139
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(
        task=dict(args=dict(dest='/path/to/dest')),
        connection=dict(),
        play_context=dict(become_user='play_become_user', become_method='play_become'),
        loader=None,
        templar=None,
        shared_loader_obj=None
    )
    assert action_module.get_become_method() == 'play_become'
    assert action_module.get_become_user() == 'play_become_user'

# Generated at 2022-06-13 11:02:03.687310
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Create an instance of the action service that we can execute
    action_service = ActionModule(task=dict(action=dict(module_name='unarchive', src='/tmp/testfile.txt',
                                                        dest='/tmp/testfile2.txt', remote_src=False,
                                                        check_mode=False, diff=False, creates='/tmp/testfile2.txt')),
                                  connection=dict(module_name='local'),
                                  play_context=dict(check_mode=False, diff=False),
                                  loader=dict(module_utils_path='/tmp', filter_factory=None))

    # Create a mock of the module action to execute
    module_action = MockActionModule()


# Generated at 2022-06-13 11:02:07.302855
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert am.TRANSFERS_FILES == True


# Generated at 2022-06-13 11:02:08.874605
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(None, {}, {})



# Generated at 2022-06-13 11:02:12.232878
# Unit test for constructor of class ActionModule
def test_ActionModule():
    tmpdir = "/tmp/test_dir"
    mock_args = {'src': 'source', 'dest': 'dest'}
    mock_task = {'args': mock_args}
    act_mod = ActionModule(mock_task, tmpdir)
    assert act_mod

# unit test for method run of class ActionModule

# Generated at 2022-06-13 11:02:21.793403
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    class MockConnection:
        tmpdir = '/home/vagrant'
        def _shell(self):
            class MockShell:
                def tmpdir(self):
                    return '/home/vagrant'
                def join_path(self, l1, l2):
                    return os.path.join(l1, l2)
            return MockShell()
        def _exec_command(self, cmd, tmp_path, sudoable=False):
            out = ''
            err = ''
            rc = 0
            return out, err, rc


# Generated at 2022-06-13 11:02:23.441776
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert hasattr(ActionModule, 'run'), "ActionModule is missing required method run"

# Generated at 2022-06-13 11:02:34.886526
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Set up a test action module object.
    from ansible.plugins.loader import module_loader
    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.block import Block
    from ansible.plugins.connection.local import Connection
    from ansible.vars.manager import VariableManager

    module_loader.add_directory(os.path.join(os.path.dirname(__file__), '../../'))
    module_loader.add_directory(os.path.join(os.path.dirname(__file__), '../../ansible_collections/ansible/posix'))

    task = Task()
    task._role = None
    task.action = 'fetch'