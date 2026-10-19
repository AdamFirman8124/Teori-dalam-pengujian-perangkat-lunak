

# Generated at 2022-06-13 09:55:40.087464
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.compat import StringIO

    am = ActionModule(None, None, None)
    am._play_context.check_mode = False
    am._task.args = dict()
    # Test no source
    am._task.args['dest'] = '/tmp/test'
    am._loader = None
    am._display = False
    am._connection = Mock()
    am._connection._shell = Mock()
    am._connection._shell.join_path = lambda x, y: x+'/'+y
    am._connection._shell._unquote = lambda x: x.replace('\\', '/')
    am._execute_module = lambda x, y, z: dict(failed=False)
    am._execute_remote_stat = lambda x, y, follow: dict(exists=True)
    am.run()

# Generated at 2022-06-13 09:55:41.297650
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule()
    assert am


# Generated at 2022-06-13 09:55:44.204902
# Unit test for constructor of class ActionModule
def test_ActionModule():
    print("Test for ActionModule class")

    module = ActionModule()

    # test for run method
    print('Test for run method')
    try:
        module.run()
    except Exception:
        print('Error in test_run_method')

# Generated at 2022-06-13 09:55:50.360815
# Unit test for constructor of class ActionModule
def test_ActionModule():
    config = dict( become = True, become_user = 'root', become_ask_pass = True)
    play_context = dict( remote_addr = 'localhost')
    task = dict(action = dict( module = 'copy', args = dict( src = '/tmp/1')))
    a = ActionModule(config, play_context, task)
    assert isinstance(a, ActionModule)

# Test for method _remove_tmp_path of class ActionModule

# Generated at 2022-06-13 09:56:01.245812
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook import PlaybookInclude

    play = PlaybookInclude()
    play.vars = {'a': '1', 'b': '2'}
    play.action = 'setup'
    play.priority = 0
    play.connection = 'paramiko'
    play.name = '$a=>$b'

    task = dict(action='setup')
    task_vars = dict()

    act = ActionModule(play, task, task_vars)
    assert act.action == 'setup'
    assert act.connection == 'paramiko'
    assert act.order == 0
    assert act.name == '$a=>$b'
    assert 'a' in act.play.vars
    assert 'b' in act.play.vars

# Generated at 2022-06-13 09:56:12.003705
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am  = ActionModule()
    assert am.ACTION_WARNINGS == ('deprecated',)
    assert am.ACTION_FLAGS == ('check_mode',)
    assert am.ACTION_VERSION == 1.1
    assert am.__doc__.startswith('handler for fetch operations')
    assert am.ACTION_USAGE.startswith('- src: Path on the remote server to fetch.')
    assert am.ACTION_EXAMPLES == (
        '- name: copy file from remote to local',
        '  fetch: src=/path/to/file.txt dest=/path/to/local_file.txt')
    assert am.super_action_module.__class__.__name__ == 'ActionBase'
    assert am._display.__class__.__name__ == 'Display'

# Generated at 2022-06-13 09:56:12.752630
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule()

# Generated at 2022-06-13 09:56:13.774096
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(ActionModule.run, {}).run()

# Generated at 2022-06-13 09:56:25.613312
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    host = dict(
        ansible_connection_plugins=dict(
            local='local_plugins',
        ),
    )


# Generated at 2022-06-13 09:56:28.192976
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import ansible.plugins.action.copy
    assert ansible.plugins.action.copy.ActionModule is not None

# Unit test to check the result of test_ActionModule()

# Generated at 2022-06-13 09:56:46.401921
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 09:56:48.135609
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    am = ActionModule({})
    assert am._execute(None, None) == {'changed': False, 'failed': True}

# Generated at 2022-06-13 09:56:58.285835
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule()
    # source = self._task.args.get('src', None)
    # original_dest = dest = self._task.args.get('dest', None)
    # flat = boolean(self._task.args.get('flat'), strict=False)
    # fail_on_missing = boolean(self._task.args.get('fail_on_missing', True), strict=False)
    # validate_checksum = boolean(self._task.args.get('validate_checksum', True), strict=False)
    #
    # msg = ''
    # # validate source and dest are strings FIXME: use basic.py and module specs
    # if not isinstance(source, string_types):
    #     msg = "Invalid type supplied for source option, it must be a string"
    #
    # if not isinstance

# Generated at 2022-06-13 09:57:05.006332
# Unit test for constructor of class ActionModule
def test_ActionModule():

    #pylint: disable=no-member,too-many-function-args
    assert ActionModule({}, {}, None, None, '').__class__.__name__ == "ActionModule"
    assert ActionModule({}, {}, None, None, '')._connection.__class__.__name__ == "Connection"

# Generated at 2022-06-13 09:57:08.320901
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # See if constructor works
    actionModuleObj = ActionModule(connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

    assert actionModuleObj is not None, "failed to instantiate ActionModule object"

    # Test error conditions in run()
    # TODO: Do this when we can figure out how to mock the run command

# Unit test
if __name__ == "__main__":
    test_ActionModule()

# Generated at 2022-06-13 09:57:11.161346
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert module is not None

# Generated at 2022-06-13 09:57:22.387144
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule(
        connection=None,
        play_context=dict(remote_user="some_user", remote_addr="some_host", password="some_pass"),
        loader=None,
        templar=None,
        shared_loader_obj=None
    )

    module._connection = MockConnection()
    module._remove_tmp_path = lambda x: None
    module._execute_remote_stat = lambda src, all_vars, follow: dict(exists=True, isdir=False, checksum=MockChecksum.CHECKSUM)
    module._execute_module = lambda module_name, module_args, task_vars: dict(failed=False, content="some_content", encoding="base64")

    # check mode not supported yet
    module._play_context.check_mode = True
    result

# Generated at 2022-06-13 09:57:33.336990
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Determine if the system is FIPS enabled. pycrypto is required for this test
    fips_enabled = False
    try:
        import Crypto.Hash
        if Crypto.Hash.algorithms_guaranteed.count('md5') == 0:
            fips_enabled = True
    except ImportError:
        # pycrypto was not installed. We can't validate if FIPS is enabled
        pass

    # Create an instance of class ActionModule to be tested
    test_action_module = ActionModule()

    # Create an instance of class ActionBase to be used as a mock object
    mock_action_base = ActionBase()

    # Create a dictionary to be used as task_vars
    test_task_vars = {}

    # Set the return value of mocked method _execute_remote_stat to a fixture
    mock_action_base

# Generated at 2022-06-13 09:57:33.889065
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert True

# Generated at 2022-06-13 09:57:41.449230
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''
    Constructor test: Instantiation of object of class ActionModule and its attributes
    '''
    
    src="path/to/remote/file"
    dest="path/to/local/file"
    flat=True
    fail_on_missing=True
    vm=ActionModule()
    assert src == vm._task.args.get('src',None)
    assert dest == vm._task.args.get('dest',None)
    assert flat == vm._task.args.get('flat',False)
    assert fail_on_missing == vm._task.args.get('fail_on_missing',False)
    return 0


# Generated at 2022-06-13 09:58:18.142556
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(name = 'ansible.builtin.fetch',
                          task = None,
                          connection = None,
                          play_context = None,
                          loader = None,
                          templar = None,
                          shared_loader_obj = None)
    return module.run()

# Generated at 2022-06-13 09:58:21.080804
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Constructor test:
    module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert module is not None

# Generated at 2022-06-13 09:58:26.812220
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # FIXME: action_plugin = module_loader.find_plugin(action)
    # FIXME: module_loader = ModuleLoader()
    action_plugin = ActionModule(connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    # FIXME: action_base = action_plugin(connection, play_context, loader, templar, shared_loader_obj)
    # FIXME: action_base.setup()
    # FIXME: return action_base.run(task_vars=tqsk_vars)
    return

# Generated at 2022-06-13 09:58:37.714297
# Unit test for constructor of class ActionModule
def test_ActionModule():
	# Test 1
	action_module = ActionModule(connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
	# Test 2
	action_module = ActionModule(connection='connection', play_context='play_context', loader='loader', templar='templar', shared_loader_obj='shared_loader_obj')
	# Test 3
	action_module = ActionModule(connection='connection', play_context='play_context', loader='loader', templar='templar', shared_loader_obj=None)
	# Test 4
	action_module = ActionModule(connection='connection', play_context='play_context', loader='loader', templar=None, shared_loader_obj=None)
	# Test 5

# Generated at 2022-06-13 09:58:46.537797
# Unit test for constructor of class ActionModule
def test_ActionModule():
    print("Testing ActionModule constructor:")
    obj = ActionModule()
    assert hasattr(obj, '_connection')
    assert hasattr(obj, '_task')
    assert hasattr(obj, '_loader')
    assert hasattr(obj, '_templar')
    assert hasattr(obj, '_shared_loader_obj')
    assert hasattr(obj, '_task_vars')
    assert hasattr(obj, '_play_context')
    assert hasattr(obj, '_loaded_from')
    assert hasattr(obj, '_cleanup_remote_tmp')
    assert hasattr(obj, '_async_poll_interval')
    assert hasattr(obj, '_async_seconds')
    assert hasattr(obj, '_async_seconds_remaining')

# Generated at 2022-06-13 09:58:48.675400
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule(None, None, None)
    assert isinstance(am, ActionModule)

# Generated at 2022-06-13 09:58:56.331520
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Create the module and source string
    module = ActionModule(connection=None, task=None, play_context=None)
    source = 'data'

    # Create a task
    task = dict()
    task['args'] = dict()
    task['args']['src'] = source

    # Test the fetch method with a fake task.
    result = module.run(task_vars=task)

    # Verify the file was downloaded
    assert result['changed'], "The file was not fetched"
    assert result['checksum'] == '35858f937e991a4954f35b7092c3e50a'
    assert result['md5sum'] == '2a58a68c8dde065f74b4a13169d98d60'

# Generated at 2022-06-13 09:58:58.186076
# Unit test for constructor of class ActionModule
def test_ActionModule():
    result = ActionModule()
    assert bool(result) is True
    assert result is not None
    assert isinstance(result, ActionModule)

# Generated at 2022-06-13 09:59:01.521933
# Unit test for constructor of class ActionModule
def test_ActionModule():

    assert ActionModule({'action': 'fetch', 'module_complex_args': {'src': 'foo', 'dest': 'bar'}},
                        task_vars={},
                        play_context={'remote_addr': 'test1', 'check_mode': False})

# Generated at 2022-06-13 09:59:09.863198
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Test behavior when host is None
    task = dict()
    task['action'] = dict()
    task['action']['module_name'] = ''
    task['action']['module_args'] = ''
    task['action']['args'] = ''
    # Test behavior when play_context is None
    play_context = dict()
    connection = dict()
    connection['play_context'] = play_context
    try:
        action_module_obj = ActionModule(task, connection, {})
        assert False
    except TypeError as e:
        assert e.message == "argument of type 'NoneType' is not iterable"

    # Test behavior when connection is None
    play_context = dict()
    play_context['host'] = 'host'
    task['action']['module_name'] = 'test'


# Generated at 2022-06-13 10:00:36.969578
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    am = ActionModule(None, {}, {}, {})
    result = am._execute_remote_stat('/tmp/test.log')
    assert 'exists' in result
    assert 'isdir' in result
    assert 'checksum' in result

# Generated at 2022-06-13 10:00:40.115101
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import ansible.plugins.action.fetch
    fetch = ansible.plugins.action.fetch.ActionModule(None, {}, {}, {})
    assert fetch is not None

# Generated at 2022-06-13 10:00:40.934354
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    return 0

# Generated at 2022-06-13 10:00:43.437758
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    print("\n***** test_ActionModule_run *****")

    # can't test this because it's mostly about fetching files
    # TODO: mock fetch_file method
    pass

# Generated at 2022-06-13 10:00:44.882435
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert isinstance(ActionModule(), ActionModule)


# Generated at 2022-06-13 10:00:54.815421
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_result import TaskResult
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.inventory.host import Host
    from ansible.vars.manager import VariableManager
    from ansible.executor.play_iterator import PlayIterator
    play_context = PlayContext()
    play_context.network_os = 'ios'
    play_context.become = False
    play_context.become_method = 'cli'
    play_context.become_user = None
    play_context.remote_addr = '1.1.1.1'
    connection = Connection('network_cli')
    connection.remote_addr = '1.1.1.1'
    connection._shell._become_

# Generated at 2022-06-13 10:01:04.346031
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    class MockRemoteStatResult():
        def __init__(self):
            self.exists = True
            self.isreg = True
            self.checksum = '123'

    class MockTask():
        def __init__(self):
            self.args = {'src': 'test.txt', 'dest': 'test.txt'}

    class MockConnection():
        def __init__(self):
            self.become = False
            self._shell = MockExecute()

        def fetch_file(self, src, dest):
            pass

    connection = MockConnection()

    class MockPlayContext():
        def __init__(self):
            self.check_mode = False
            self.remote_addr = '192.168.1.1'

    play_context = MockPlayContext()


# Generated at 2022-06-13 10:01:12.062486
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # test_ActionModule: create an object of the class ActionModule
    print('INFO: test_ActionModule')
    obj = ActionModule()
    print('INFO: type(obj): ' + str(type(obj)))
    print('INFO: obj._connection: ' + str(obj._connection))
    print('INFO: type(obj._connection): ' + str(type(obj._connection)))
    print('INFO: obj._play_context: ' + str(obj._play_context))
    print('INFO: type(obj._play_context): ' + str(type(obj._play_context)))
    print('INFO: obj._loader: ' + str(obj._loader))
    print('INFO: type(obj._loader): ' + str(type(obj._loader)))

# Generated at 2022-06-13 10:01:12.676880
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:01:24.290911
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import os
    import tempfile
    # Construct a task that executes the action module 
    task = TMPDummyTask()
    # Construct an action module using the task
    action = ActionModule(task, DummyConnection)
    # Extract "tmp" from the action module
    tmp = action._connection._shell.tmpdir
    # Try to remove the tmp directory with normal permissions
    action._remove_tmp_path(tmp)
    # Make the tmp directory read-only 
    os.chmod(tmp, 0o400)
    # Try to remove the tmp directory with limited permissions
    action._remove_tmp_path(tmp)
    # Construct the task again
    task = TMPDummyTask()
    # Construct the action module using the task
    action = ActionModule(task, DummyConnection)
    # Extract "tmp" from the action module
   

# Generated at 2022-06-13 10:04:30.762491
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    print("test_ActionModule_run")
    source = '/home/test/test_file.txt'
    dest = '/tmp/test_fetch/test_file.txt'
    flat = False
    fail_on_missing = True

    action_module = ActionModule()
    action_module._connection = MagicMock()
    action_module._play_context = MagicMock()
    action_module._task = MagicMock()
    action_module._task.args = MagicMock()
    action_module._task.args['src'] = source
    action_module._task.args['dest'] = dest
    action_module._task.args['flat'] = flat
    action_module._task.args['fail_on_missing'] = fail_on_missing
    action_module._connection._shell = MagicMock()

    action

# Generated at 2022-06-13 10:04:41.685602
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # test example from action_plugins/fetch.py
    module_args = dict(src='/home/testuser/testfile', dest='/etc/testfile')
    display.display = lambda x: x
    a = ActionModule(task=dict(args=module_args), connection=dict(conn_type='ssh'))
    dict_a = dict()

    display.verbosity = 5
    result = a.run(tmp=None, task_vars=dict_a)
    print("Result is: ")
    print(result)
    assert result == dict()

    dict_a['inventory_hostname'] = 'testhost'
    result = a.run(tmp=None, task_vars=dict_a)
    print("Result is: ")
    print(result)
    #assert result == dict()




# Generated at 2022-06-13 10:04:50.543673
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    print("Starting test_ActionModule_run")

    tmpdir = os.getcwd()
    subdir = os.path.join(tmpdir, "test_run")

# Generated at 2022-06-13 10:04:51.818841
# Unit test for constructor of class ActionModule
def test_ActionModule():
    print("TEST: class ActionModule")
    am = ActionModule()
    # TODO: more tests

# Generated at 2022-06-13 10:04:54.839537
# Unit test for constructor of class ActionModule
def test_ActionModule():
    connection = None
    play_context = None
    loader = None
    templar = None
    shared_loader_obj = None

    am = ActionModule(connection, play_context, loader, templar, shared_loader_obj)
    assert am is not None

if __name__ == '__main__':
    # Run unit test
    test_ActionModule()

# Generated at 2022-06-13 10:04:56.125290
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action = ActionModule()


# Generated at 2022-06-13 10:05:10.531041
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    class ActionModule_test(ActionModule):
        def _execute_remote_stat(self, source, all_vars=None, follow=True):
            return {"exists": True, "isdir": False, "checksum": "123456789"}

    action_module = ActionModule_test()
    task = object()
    task.args = {
        "src": "/home/foo",
        "dest": "/home/dest",
        "flat": "no",
        "validate_checksum": "no",
        "fail_on_missing": "yes",
    }
    task_vars = {"inventory_hostname": "localhost"}
    play_context = object()
    play_context.check_mode = True
    play_context.remote_addr = "localhost"
    runner = object()