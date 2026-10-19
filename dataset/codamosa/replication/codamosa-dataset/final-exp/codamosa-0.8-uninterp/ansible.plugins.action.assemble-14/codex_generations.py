

# Generated at 2022-06-13 09:23:56.142876
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # setup mocks
    mock_loader = Mock()
    mock_play_context = Mock()
    #mock_play = Mock()
    mock_task = Mock()
    mock_task_args = Mock()
    mock_task_args.get = Mock()
    mock_task_args.get.side_effect = [None, None, None, None, None, None, None, None, None, None, None, None, None]
    mock_task.args = mock_task_args
    mock_connection = Mock()
    mock_connection._shell = Mock()
    example_path = '/usr/lib'
    test_path = '/home/vagrant/'
    mock_connection._shell.join_path = Mock()

# Generated at 2022-06-13 09:24:05.837341
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    path = tempfile.mkdtemp("ansible_test.%s" % str(time.time()))
    os.mkdir(os.path.join(path, 'frag_0'))
    os.mkdir(os.path.join(path, 'frag_1'))

    file0 = open(os.path.join(path, 'frag_0', 'file0.txt'), 'w+')
    file0.write("first file")
    file0.close()
    file1 = open(os.path.join(path, 'frag_1', 'file1.txt'), 'w+')
    file1.write("second file")
    file1.close()


# Generated at 2022-06-13 09:24:06.293795
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert True

# Generated at 2022-06-13 09:24:14.946090
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''Unit test for ActionModule.run
    '''

    import pprint
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    ################################################################################
    # Parse arguments from the caller
    ################################################################################

    inventory_path = 'inventory/hosts'
    playbook_path = 'playbook.yml'

    # create inventory and pass to var manager
    inventory = InventoryManager(loader=None, sources=inventory_path)
    variable_manager = VariableManager(loader=None, inventory=inventory)
    ################################################################################

    # Create the Task

# Generated at 2022-06-13 09:24:18.465409
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule(None, None, None, None, None, None)
    assert isinstance(am, object)

# Generated at 2022-06-13 09:24:26.375526
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule(loader=None, task=None, connection=None, play_context=None, loader_path='', shared_loader_obj=None,
                      final_loader=None)
    assert am._supports_check_mode == False
    assert am._task is None
    assert am._loader is None
    assert am._play_context is None
    assert am._shared_loader_obj is None
    assert am._final_loader is None
    assert am._connection is None
    assert am._tmp is None
    assert am._templar is None
    assert am._loader_path == ''


# Generated at 2022-06-13 09:24:27.814132
# Unit test for constructor of class ActionModule
def test_ActionModule():
    x = ActionModule(10,20,30)
    assert x != None

# Generated at 2022-06-13 09:24:29.734127
# Unit test for constructor of class ActionModule
def test_ActionModule():
    obj = ActionModule(task=dict(), connection=dict(), play_context=dict())
    assert obj.run() == dict()

# Generated at 2022-06-13 09:24:30.645372
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule.TRANSFERS_FILES

# Generated at 2022-06-13 09:24:32.014949
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule(None, {}, {}, None, None)
    assert action is not None

# Generated at 2022-06-13 09:24:43.121898
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule()

# Generated at 2022-06-13 09:24:48.298564
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # preparations
    import mock
    import shutil

    am = ActionModule()
    am._task = mock.Mock()
    am._task.args = mock.Mock()
    am._task.args.get = mock.Mock()
    am._task.args.get.return_value = None
    am._task.args.copy = mock.Mock()
    am._task.args.copy.return_value = mock.Mock()
    am._execute_module = mock.Mock()
    am._remote_expand_user = mock.Mock()
    am._remote_expand_user.return_value = u"/tmp/dest"
    am._find_needle = mock.Mock()
    am._find_needle.return_value = u'/tmp/src'

# Generated at 2022-06-13 09:24:50.148694
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert isinstance(ActionModule(None, None, None), ActionModule)

# Generated at 2022-06-13 09:24:50.834318
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 09:24:55.520912
# Unit test for constructor of class ActionModule
def test_ActionModule():
    task = dict(action=dict(__ansible_module__='file', dest='/tmp/file'))
    act = ActionModule(task, dict(), '/tmp/test_dir', 'fake_connection')
    assert act != None

# Generated at 2022-06-13 09:24:56.117260
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule()

# Generated at 2022-06-13 09:25:04.719474
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''
    Test ActionModule instantiation.
    :return:
    '''
    task = dict(
        name='Fetch file',
        action='get_url',
        delegate_to='xxx',
        args={'url': 'http://xxxx.com'}
    )
    actionbase = ActionBase()
    actionmodule = ActionModule(task, actionbase._connection, actionbase._play_context, actionbase._loader, actionbase._templar, actionbase._shared_loader_obj)
    # This class is an abstract class, we will test its instantiation
    assert actionmodule



# Generated at 2022-06-13 09:25:11.934542
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils.basic import AnsibleModule

    from ansible.module_utils import basic

    module = AnsibleModule(
        argument_spec=dict(
            src=dict(required=True, type='str'),
            dest=dict(required=True, type='str'),
            regexp=dict(default=None, type='str'),
            remote_src=dict(default=True, type='bool'),
            delimiter=dict(default=None, type='str'),
            follow=dict(default=False, type='bool'),
            ignore_hidden=dict(default=False, type='bool'),
        ),
    )


# Generated at 2022-06-13 09:25:16.349092
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.plugins.action.assemble import ActionModule
    ActionModule('test_ActionModule', 'test/test_action_module.yml', 'test/test_action_module.py', {}, {})

# Generated at 2022-06-13 09:25:27.794028
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(None)
    assert action_module._task is None
    assert action_module._connection is None
    assert action_module._play_context is None
    assert action_module._loader is None
    assert action_module._templar is None
    assert action_module._shared_loader_obj is None

    # object has no attribute '_connection'
    result = action_module.run()
    assert 'invocation' in result
    assert 'module_args' in result['invocation']
    assert 'module_name' in result['invocation']
    assert result['invocation']['module_name'] == 'ansible.legacy.assemble'
    assert result['failed']

# Generated at 2022-06-13 09:25:53.783990
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''
    Unit test for constructor of class ActionModule
    :return:
    '''
    my_new_action_module = ActionModule()
    if not isinstance(my_new_action_module, ActionModule):
        raise Exception("Cannot create instance of ActionModule class.")

    try:
        my_new_action_module.run()
        raise Exception("ActionModule class does not throw exceptoin. It should.")
    except _AnsibleActionDone:
        pass

# Generated at 2022-06-13 09:25:56.355238
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    actionModule = ActionModule(play_context=None, new_stdin=None)
    result = actionModule.run(None, None)
    assert(result is not None)
    assert(type(result) is dict)


# Generated at 2022-06-13 09:25:57.842341
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass


# Generated at 2022-06-13 09:26:01.018057
# Unit test for constructor of class ActionModule
def test_ActionModule():
    testobject = ActionModule({'src': 'src', 'dest': 'dest'}, {}, False, False, {})
    assert testobject.TRANSFERS_FILES

# Generated at 2022-06-13 09:26:03.521721
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(load_context=True)
    assert module.TRANSFERS_FILES == True

# Generated at 2022-06-13 09:26:05.390741
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule(loader=None, task=None, connection=None, play_context=None, loader_cache=dict())
    assert am != None

# Generated at 2022-06-13 09:26:07.354899
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    a = ActionModule(None, None)
    assert a.run() == {}


# Generated at 2022-06-13 09:26:08.822501
# Unit test for constructor of class ActionModule
def test_ActionModule():

    # run test
    #assert(1 == 2)
    assert(1 == 1)

# Generated at 2022-06-13 09:26:12.265822
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # 
    fake_task = object()
    # 
    helper = ActionModule(fake_task)
    #
    assert helper.run()
    #
    assert helper.run(tmp='tmp', task_vars=dict())
    #
    assert helper.run(tmp='tmp', task_vars=None)

# Generated at 2022-06-13 09:26:13.844977
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule()
    assert(am.TRANSFERS_FILES == True)


# Generated at 2022-06-13 09:27:05.594867
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    def test_run_ActionModule_A():
        mock_task = MockTask()
        mock_task.action = 'assemble'
        mock_task.args = {}
        mock_task.args[u'src'] = u'path/to/src'
        mock_task.args[u'dest'] = u'path/to/dest'
        mock_task.args[u'remote_src'] = u'yes'
        mock_task.args[u'delimiter'] = None
        mock_task.args[u'regexp'] = None
        mock_task.args[u'follow'] = False
        mock_task.args[u'ignore_hidden'] = False
        mock_task.args[u'decrypt'] = True
        action_module = ActionModule()
        action_module._task = mock_task

# Generated at 2022-06-13 09:27:14.359606
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    with _tst_ActionModule_run() as e:
        e.mock_os_path_isdir.return_value = True
        e.mock_os_path.join.return_value = "test"
        e.mock_os_path.basename.return_value = "test"
        e.mock_os_path.isfile.return_value = True

        e.mock_checksum_s.return_value = 1
        e.mock_execute_remote_stat.return_value = {'checksum': 1}

        result = e.self.run(tmp="/tmp", task_vars={"any": "data"})

# Generated at 2022-06-13 09:27:22.322909
# Unit test for constructor of class ActionModule
def test_ActionModule():
    task_vars = dict()
    connection = None
    play_context = None
    loader = None
    task = None
    file_loader = None
    action_plugin = ActionModule(task, connection, play_context, loader, file_loader)
    assert isinstance(action_plugin, ActionModule)
    assert task == action_plugin._task
    assert connection == action_plugin._connection
    assert play_context == action_plugin._play_context
    assert loader == action_plugin._loader
    assert file_loader == action_plugin._file_loader

# Generated at 2022-06-13 09:27:22.837883
# Unit test for constructor of class ActionModule
def test_ActionModule():
    pass

# Generated at 2022-06-13 09:27:29.884203
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task import Task
    from ansible.playbook.play import Play

    obj = ActionModule(task=Task(), connection='local', play=Play().load(dict(name='Test', hosts='localhost', tasks=dict()), variable_manager='', loader='', options='', passwords='', stdout_callback=''))

    assert hasattr(obj, '_execute_module')
    assert hasattr(obj, '_execute_remote_stat')

# Generated at 2022-06-13 09:27:40.854770
# Unit test for constructor of class ActionModule
def test_ActionModule():
    class FakeTask:
        def __init__(self):
            self.args = dict()

    class FakePlayContext:
        def __init__(self):
            self.shell = 'shell'
            self.connection = 'connection'
            self.diff = True
            self.basedir = 'basedir'

    class FakeConnection:
        def __init__(self):
            self._shell = FakeShell()

    class FakeShell:
        def __init__(self):
            self.tmpdir = '/path/to/directory'
    args = dict()
    task = FakeTask()
    play_context = FakePlayContext()
    connection = FakeConnection()
    obj = ActionModule(task, connection, play_context, None, None)
    assert isinstance(obj, ActionBase)

# Generated at 2022-06-13 09:27:55.868216
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''
    Unit test for class ActionModule.run method.
    '''

    class Test(object):

        def __init__(self):
            self.supports_check_mode = False

            self.res = {'rc': 0, 'failed': False, 'changed': False}
            self.tmp = None
            self.tmp_path = None
            self.task = None
            self.task_vars = None
            self.play_context = None
            self.src = None
            self.dest = None
            self.delimiter = None
            self.remote_src = None
            self.regexp = None
            self.follow = None
            self.ignore_hidden = None
            self.decrypt = None
            self.check_mode = False
            self.assemble_from_fragments_called

# Generated at 2022-06-13 09:27:57.085517
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 09:27:59.746479
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''
    Unit test for method run of class ActionModule
    '''
    print("ActionModule_run")
    # TODO: write unit test
    #assert(False)

# Generated at 2022-06-13 09:28:09.742578
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.plugins.action import ActionModule

    path = '../module_utils/assemble.py'
    options = {'src': 'src', 'dest': 'dest', 'remote_src': 'yes', 'regexp': 'regexp', 'delimiter': 'delimiter', 'ignore_hidden': 'ignore_hidden', 'decrypt': 'decrypt'}
    name = 'test_name'
    args = {'test_arg': 'test_value'}
    loader = 'test_loader'

    test = ActionModule(path, options, name, args, loader)
    assert test._name == 'test_name'

# Generated at 2022-06-13 09:29:34.077258
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True

# Generated at 2022-06-13 09:29:36.543360
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(loader=None, play_context=None, new_stdin=None)
    assert action_module.TRANSFERS_FILES == True

# Generated at 2022-06-13 09:29:40.178764
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """
    Make the action
    """
    action_mod = ActionModule()

    """
    Make the complex args for the module's run
    """
    # Run the module
    test_run = action_mod.run(None, {'TMP_PATH': '/tmp'})

    """
    Write some test
    """
    assert True

# Generated at 2022-06-13 09:29:41.924679
# Unit test for constructor of class ActionModule
def test_ActionModule():
    clazz = ActionModule()
    assert len(clazz.ActionModule.__dict__.keys()) > 0

# Generated at 2022-06-13 09:29:46.579267
# Unit test for constructor of class ActionModule
def test_ActionModule():
    host = 'some_host'
    path = 'some_path'
    args = 'some_args'
    tmp = 'some_tmp'
    task_vars = dict()
    inject = dict()
    shared_loader_obj = dict()
    variable_manager_obj = dict()

    connection = object
    play_context = object
    action_base = ActionModule(connection=connection, play_context=play_context,
                               new_stdin=None, loader=None, shared_loader_obj=shared_loader_obj,
                               variable_manager=variable_manager_obj, task_vars=task_vars,
                               tmp=tmp, inject=inject)
    assert action_base.task_vars == task_vars
    assert action_base.variable_manager == variable_manager_obj

# Generated at 2022-06-13 09:29:51.105882
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    print('Test ActionModule.run')
    parser = argparse.ArgumentParser()
    parser.add_argument('--separator', dest='separator', default='.',
                            help='separator in hostname')
    args, unk = parser.parse_known_args()
    am = ActionModule(task=dict(), connection=dict(), play_context=dict(), loader=dict(), templar=dict(), shared_loader_obj=None)
    am.run(tmp='', task_vars=dict())

if __name__ == '__main__':
    test_ActionModule_run()

# Generated at 2022-06-13 09:30:00.384026
# Unit test for constructor of class ActionModule
def test_ActionModule():
    #
    # initial test to see how the module and ActionBase work together.
    #

    # TODO: add tests to the ActionBase class, note that it will require other
    #       sections of the code to be abstracted out, such as vars, loader, tmp
    #       etc, so that they can be mocked and won't fail if not present.

    action = ActionModule()

    # example of injecting data into the action
    action._task = {
        'action': 'test',
        'args': {'src': 'test.txt', 'dest': 'test2.txt'},
    }

    # example of what a client would pass into an execute method
    tmp = '/tmp/foo'
    task_vars = {'test_var': 'foo'}

    result = action.run(tmp, task_vars)

   

# Generated at 2022-06-13 09:30:08.535631
# Unit test for constructor of class ActionModule
def test_ActionModule():
    filename = "./test/unit/mockups/fake_object_with_methods.py"
    loader = DictLoader(filename)
    def _get_real_file(path, decrypt=True):
        return path
    loader._get_real_file = _get_real_file
    task_vars = {"task1": {
        "args": {
            "src": "../test/data/test_file_with_content",
            "dest": "/tmp/test_file_with_content",
            "deploy_data": "yes"
            },
        "action": {
            "__ansible_module__": "copy",
            "__ansible_arguments__": "src=/home/user/file, dest=/tmp/file"
            }
        }
    }

# Generated at 2022-06-13 09:30:13.489496
# Unit test for constructor of class ActionModule
def test_ActionModule():
    a = ActionModule(dict(action=dict({'__ansible_module__': 'ansible.legacy.assemble'})))
    assert a._task.action['__ansible_module__'] == 'ansible.legacy.assemble'

# Generated at 2022-06-13 09:30:14.933532
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # pylint: disable=redefined-outer-name
    assert ActionModule is ActionBase

# Generated at 2022-06-13 09:33:23.552459
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.runner.connection_plugins.local import Connection
    from ansible.inventory import Host, Inventory
    from ansible.module_utils import basic
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.vars.manager import VariableManager
    from ansible.utils.vars import combine_vars
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    inv = Inventory(loader=loader, variable_manager=VariableManager(), host_list=[])
    variable_manager = VariableManager()

# Generated at 2022-06-13 09:33:24.394735
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # unit-test-empty-result
    assert True

# Generated at 2022-06-13 09:33:29.036421
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    hostname = "www.example.com"
    task_vars = {"my_var": "11"}
    spec = {
        "src": "{{ var_dir }}",
        "remote_src": "True",
        "dest": "{{ log_dir }}",
        "regexp": "\*.log",
        "delimiter": "",
        "ignore_hidden": False,
        "decrypt": False,
    }
    module_executor = ActionModule(hostname, spec)

    class MockRunner(object):
        def run(self, task_vars, tmp=None, task_args=None, *args, **kwargs):
            self.run_called_with = dict(task_args=task_args)
            return dict()

    module_executor._execute_module = MockRunner().run

   

# Generated at 2022-06-13 09:33:29.838658
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 09:33:40.806840
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Initialization of the ActionModule class
    action_module = ActionModule(
        task=dict(args=dict(src="files", dest="temp", remote_src="yes", regexp="reg file", delimiter="del",
                            ignore_hidden="False", decrypt="True")),
        connection=Connection(),
        play_context=PlayContext(),
        loader=None,
        templar=None,
        shared_loader_obj=None
    )

    # Test case when src is None
    action_module.connection = Connection()
    action_module.task = dict(args=dict(src=None, dest="temp", remote_src="yes", regexp="reg file", delimiter="del",
                                        ignore_hidden="False", decrypt="True"))