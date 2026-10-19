

# Generated at 2022-06-13 09:34:52.913077
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # mock the connection to get the class constructed
    class TestConnection(object):
        def __init__(self, tmpdir):
            self._shell = Shell()
            self._shell.tmpdir = tmpdir

        @contextmanager
        def _rab(self):
            yield self

        def _create_tmp_path(self):
            return tempfile.mkdtemp()
    class TestTask(object):
        def __init__(self, args):
            self.args = args
    # We have to patch the connection_loader class to make sure we get a
    # connection.
    with patch.object(connection_loader, 'get', return_value=TestConnection(None)):
        task = TestTask(dict(src='src', dest='dest'))

# Generated at 2022-06-13 09:35:06.403565
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Test that the run method of ActionModule calls the correct methods in the correct order and returns the expected result
    ## First test call for src and content being mutually exclusive
    result = {
        'failed': True,
        'msg': 'src and content are mutually exclusive'
    }

# Generated at 2022-06-13 09:35:13.872673
# Unit test for constructor of class ActionModule
def test_ActionModule():
    class Options(object):
        connection = 'ssh'
        module_path = '/path/to/mymodules'
        forks = 10
        become = False
        become_method = 'sudo'
        become_user = 'root'
        check = False
        diff = False

    # Load up options for an ssh connection
    options = Options()

    class Task(object):
        def __init__(self, args):
            self.args = args

    # Create a Transfer object with the ssh connection info
    xfer = ActionModule(
        task=Task(dict(action=dict(src='test', dest='foo', remote_src=False))),
        connection=ActionModule._create_connection(options),
        play_context=PlayContext(variables={'ansible_check_mode': False})
    )

    # Make sure we set up

# Generated at 2022-06-13 09:35:18.499725
# Unit test for constructor of class ActionModule
def test_ActionModule():
    ''' tests that the module can be created '''
    assert ActionModule is not None


# Generated at 2022-06-13 09:35:27.915855
# Unit test for method run of class ActionModule

# Generated at 2022-06-13 09:35:38.663529
# Unit test for method run of class ActionModule

# Generated at 2022-06-13 09:35:42.596351
# Unit test for constructor of class ActionModule
def test_ActionModule():
    ''' return an instance of ActionModule for testing '''
    module = ActionModule(task=dict(action=dict(module_name='copy', module_args=dict())))
    return module



# Generated at 2022-06-13 09:35:45.235989
# Unit test for constructor of class ActionModule
def test_ActionModule():
    for action_ in (Connection, ActionModule):
        action = action_()
        assert isinstance(action, object)


# Generated at 2022-06-13 09:35:57.349669
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Setup
    m = module_common._ANSIBLE_ARGS
    module = ActionModule(None, m, False, False)
    module._load_name_to_path_map()
    assert module._name_to_path_map
    module._task_vars = {}

    # Execute the unit under test
    module._connection = Connection(module, 'dummy', 'dummy')
    module._transfer_strategy = 'copy'
    result = module.run(tmp='/tmp', task_vars={})
    # Verify
    assert result['failed'] is True
    assert result['msg'] == 'src (or content) is required'
    # Teardown

    # Setup
    m = module_common._ANSIBLE_ARGS
    module = ActionModule(None, m, False, False)
    module._load_

# Generated at 2022-06-13 09:36:02.675510
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """
    ActionModule.run()
    """
    import os
    import sys
    import inspect
    import tempfile
    # Import the mocked modules that we are testing
    from ansible.module_utils.basic import AnsibleModule, AnsibleError
    from ansible.module_utils._text import to_bytes, to_text
    from ansible.module_utils.common._collections_compat import Mapping, MutableMapping
    from ansible.plugins.action import ActionBase
    from ansible.vars.hostvars import HostVars
    from ansible.vars.hostvars import VariableManager
    from ansible.vars.manager import VariableManager
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    import ansible.constants as C
    C.DEFAULT_LOC

# Generated at 2022-06-13 09:37:05.820398
# Unit test for constructor of class ActionModule
def test_ActionModule():
    ''' constructor for class ActionModule '''
    runner_internal = Runner(
        module_name='copy',
        module_args={'src': 'src', 'dest': 'dest'},
        config={},
        connection=Connection('local'),
        task_uuid=None,
        loader=None,
        templar=None,
    )
    file_copy = ActionModule(runner_internal)
    if file_copy and isinstance(file_copy, basestring):
        raise AssertionError("ActionModule is string instead of object")
    if not isinstance(file_copy, ActionModule):
        raise AssertionError("ActionModule does not inherit from object ActionModule")

# Generated at 2022-06-13 09:37:08.578512
# Unit test for constructor of class ActionModule
def test_ActionModule():
    with patch.object(os, 'path', new=MockPath):
        action_module = ActionModule(task=Mock(module_args={}))
        assert action_module is not None

# Generated at 2022-06-13 09:37:15.813294
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import tempfile

    from ansible.compat.tests.mock import patch, MagicMock
    from ansible.module_utils.basic import AnsibleModule

    from ansible_collections.community.general.plugins.modules.files import _create_remote_file_args
    from ansible_collections.community.general.plugins.modules.files import _create_remote_copy_args

    # Instantiate a task
    task0 = AnsibleTask()
    task1 = AnsibleTask()

    # Create a temp file and close it.
    temp_file0 = tempfile.NamedTemporaryFile(mode='w', delete=False)
    temp_file0.close()

    # Create a temp file and close it.
    temp_file1 = tempfile.NamedTemporaryFile(mode='w', delete=False)
    temp

# Generated at 2022-06-13 09:37:26.118182
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''Unit test for method run of class ActionModule'''
    ############################################################################
    # Lets mock these out
    self = mock.MagicMock()
    tmp = mock.MagicMock()
    task_vars = mock.MagicMock()
    ############################################################################
    # Lets stub out this first if
    source = mock.MagicMock()
    source.endswith.return_value = True
    mocked_args = {'src': source}
    self._task.args = mocked_args
    result = ActionModule.run(self=self, tmp=tmp, task_vars=task_vars)
    assert result is not None
    assert 'src' in result and result['src'] == mocked_args['src']
    ############################################################################
    # Now lets stub out the else statement
    source.end

# Generated at 2022-06-13 09:37:32.669254
# Unit test for constructor of class ActionModule
def test_ActionModule():
    source = None
    content = None
    dest = None
    remote_src = None
    local_follow = None
    task_vars = {}
    # pylint: disable=unused-variable
    action_module = ActionModule(source, content, dest, remote_src, local_follow, task_vars)

# Generated at 2022-06-13 09:37:46.240454
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # create a fake ActionModule instance
    fake_args = dict(
        A_SPECIAL_ARG_KEY='special_arg_value',
        A_SPECIAL_ARG_LIST_KEY=['el1', 'el2'],
        A_SPECIAL_ARG_DICT_KEY=dict(d_key1='d_value1', d_key2=['d_el1', 'd_el2'])
    )

    # create a fake module
    module_mock = mock.MagicMock()

    # create a fake connection
    connection_mock = mock.MagicMock()

    # create a fake task
    task_mock = mock.MagicMock()
    task_mock.args = fake_args

    # create the testee

# Generated at 2022-06-13 09:37:47.981050
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert isinstance(ActionModule(), ActionModule)

# Generated at 2022-06-13 09:37:58.032155
# Unit test for method run of class ActionModule

# Generated at 2022-06-13 09:38:00.143719
# Unit test for constructor of class ActionModule
def test_ActionModule():
    obj = ActionModule(None, None)
    assert obj


# Generated at 2022-06-13 09:38:07.271959
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Get value from module ansible.modules.system.copy
    result = dict()
    source = None
    content = None
    dest = None
    remote_src = None
    local_follow = None
    source = source
    content = content
    dest = dest
    remote_src = remote_src
    local_follow = local_follow
    tmp = None
    tmp = tmp
    task_vars = None
    task_vars = task_vars
    copy = copy
    copy("test_value")
    # Assert result
    assert(result == result)

# Generated at 2022-06-13 09:39:13.545954
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """
    Unit test for constructor of class ActionModule
    """
    manager = mock.Mock()
    data = mock.Mock()
    task = mock.Mock()
    connection = mock.Mock()
    loader = mock.Mock()
    templar = mock.Mock()
    shared_loader_obj = mock.Mock()
    action = ActionModule(manager=manager, task=task, connection=connection, play_context=mock.Mock(), loader=loader, templar=templar, shared_loader_obj=shared_loader_obj)

    assert action.task == task
    assert action._task == task
    assert action._connection == connection
    assert action._loader == loader
    assert action._templar == templar
    assert action._shared_loader_obj == shared_loader_obj
   

# Generated at 2022-06-13 09:39:29.022115
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = ActionModule(task=dict(args=dict(src="src", dest="dest", content="content", remote_src="remote_src", local_follow="local_follow")))
    action_module._execute_module = Mock()
    action_module._task.args["files"] = list()
    action_module._connection = Mock()
    action_module._connection._shell = Mock()
    action_module._connection._shell.tmpdir = None
    action_module._loader = Mock()
    action_module._remove_tmp_path = Mock()
    action_module._ensure_invocation = Mock()

    result = action_module.run()
    assert result == action_module._ensure_invocation.return_value
    
    assert action_module._ensure_invocation.call_count == 1
    assert action_

# Generated at 2022-06-13 09:39:30.056049
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ActionModule_run()

# Generated at 2022-06-13 09:39:35.398672
# Unit test for constructor of class ActionModule
def test_ActionModule():
    connection = dict(user='test', host='testhost')
    task = dict(action=dict(module_name='async_wrapper', module_args=dict(module_name='test')))

    a_module = ActionModule(task, connection, play_context=PlayContext(remote_addr='192.168.1.1'))

    assert a_module.task is task
    assert a_module.connection is connection


# Generated at 2022-06-13 09:39:49.759096
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Test case 1: normal case
    task = Task()
    task.args = {
        'src': '/home/user/src',
        'dest': '/home/user/dest',
        'mode': 'copy'
    }
    assert ActionModule(task, connection=None, play_context=PlayContext(), loader=None, templar=None, shared_loader_obj=None).task.args == task.args

    # Test case 2: empty args
    task = Task()
    task.args = {}
    assert ActionModule(task, connection=None, play_context=PlayContext(), loader=None, templar=None, shared_loader_obj=None).task.args == task.args

    # Test case 3: args is None
    task = Task()
    task.args = None

# Generated at 2022-06-13 09:39:58.493854
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    #
    # run() takes an argument tmp that's usually the path to a temporary directory
    # that it uses to store results from previous tasks. In this test we're going to
    # run the module with a tmpdir that we can easily test
    #
    tmpdir = '/tmp/testtmpdir'
    #
    # Create a fake ActionModule with a mock for the run method
    #
    class MockActionModule(ActionModule):
        def run(self, tmp, task_vars=None):
            return super(MockActionModule, self).run(tmpdir, task_vars)

    #
    # Create a mock task we can use
    #
    task = AnsibleTask()
    task.args['content'] = 'some content'
    task.args['src'] = 'some source'

# Generated at 2022-06-13 09:40:05.113538
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''
    Unit test for constructor of class ActionModule
    '''
    connection = Connection()
    task = Task()
    result = 'result'
    action_module = ActionModule(connection=connection, task=task, result=result)
    assert action_module.task == task
    assert action_module.result == result
    assert action_module.task_vars == {}
    assert action_module.tmp == C.DEFAULT_REMOTE_TMP


# Generated at 2022-06-13 09:40:16.965453
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    host = '127.0.0.1'
    port = 22
    transport = 'paramiko'
    user = 'ansible_user'
    password = 'ansible_pass'
    connect_timeout = 10
    ssh_executable = None
    sock = None
    become = True
    become_method = 'sudo'
    become_user = 'root'
    become_pass = None
    _paramiko = None
    _ssh = None
    pty = True
    sudoable = True
    no_log = False
    remote_tmp = None
    local_tmp = None
    shell = '/bin/sh'
    has_pipelining = True
    supports_persistence = False
    timeout = 30
    persistent_connect_interval = 30
    persistent_command_interval = 0.01
    persistent_port

# Generated at 2022-06-13 09:40:20.571577
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule(task=dict(action=dict(module_name='copy', module_args=dict(src='/tmp/source', dest='/tmp/dest'))))
    assert am is not None


# Generated at 2022-06-13 09:40:21.833719
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(None, None, None)

# Generated at 2022-06-13 09:41:28.726434
# Unit test for constructor of class ActionModule
def test_ActionModule():

    # Create an instance of the class
    obj = ActionModule(dict(action=dict(module_args=dict(dest='DEST', src='SRC'))))

    assert obj._task.action == 'copy'
    assert obj._task.args == {'dest': 'DEST', 'src': 'SRC'}
    assert obj._task.delegate_to is None


# Generated at 2022-06-13 09:41:36.302324
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Test the constructor of class ActionModule
    def _test(description, expected_result, *args, **kwargs):
        result = ActionModule(*args, **kwargs)
        assert result == expected_result, description

    # Create a task object.
    task_obj = dict(action=dict(module_compression='gzip'),
                    args=dict(src='/tmp/src.zip', dest='/tmp/dest.zip', mode='0600'))
    task = Task._load(task_obj)
    # Test 1

# Generated at 2022-06-13 09:41:45.707199
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Test action module setup
    t = ActionModule(task=dict(), connection=dict(), play_context=dict(), loader=dict(), templar=dict(), shared_loader_obj=dict())

    # Test _create_content_tempfile
    try:
        content = 'This is the content'
        tmp_file = t._create_content_tempfile(content)
        assert os.path.isfile(tmp_file)

        f = open(tmp_file, 'rb')
        tmp_content = f.read()
        f.close()

        os.remove(tmp_file)
        assert content == tmp_content
    except Exception as e:
        assert False, 'ActionModule._create_content_tempfile failed' % e

    # Test _remove_tempfile_if_content_defined

# Generated at 2022-06-13 09:41:50.573584
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # 
    # test __init__
    # 
    module_copy = ActionModule(task=None)

    # 
    # test _get_checksum
    # 
    # test _get_checksum failure
    try:
        module_copy._get_checksum(path='/tmp')

    except AnsibleActionFail as e:
        assert e.exception.args[0] == 'file (/tmp) is absent or not accessible'

    # test _get_checksum for file with sha256sum
    assert module_copy._get_checksum(path='/usr/bin/ansible-doc') == '05a9fd9c7fdc404b00c7cfe5597f1f61c12268f26d22b7a1457b1eac7acbb3b3'

    # test

# Generated at 2022-06-13 09:41:58.226566
# Unit test for method run of class ActionModule

# Generated at 2022-06-13 09:42:04.387017
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''
    Unit test for constructor of ActionModule
    '''
    class MockTask():
        def __init__(self, args):
            self.args = args

    def test_defaults():
        '''
        Test setting all the defaults and checking them
        '''
        task = MockTask(dict())
        action = ActionModule(task, dict())

        assert action.DEFAULT_NEWLINE == '\n'
        assert action._task is task
        assert action._connection is None
        assert action._play_context is None
        assert action._loader is None
        assert action._templar is None
        assert action._shared_loader_obj is None

    def test_boolean_args():
        '''
        Test setting all the defaults and checking them
        '''

# Generated at 2022-06-13 09:42:05.639506
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule()



# Generated at 2022-06-13 09:42:06.975359
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # TODO: implement test
    pass
# Class ActionModule

# Generated at 2022-06-13 09:42:07.628779
# Unit test for constructor of class ActionModule
def test_ActionModule():
    pass

# Generated at 2022-06-13 09:42:18.065457
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    m = AnsibleModule(
        argument_spec=dict(
            src=dict(required=True, type='path'),
            dest=dict(required=True, type='path'),
            follow=dict(required=False, type='bool', default=False),
            recurse=dict(required=False, type='bool', default=False),
            force=dict(required=False, type='bool', default=False),
            remote_src=dict(required=False, type='bool', default=False),
            local_follow=dict(required=False, type='bool', default=False),
            validate_certs=dict(required=False, type='bool', default=False),
        ),
        supports_check_mode=False
    )

    # create an ActionModule object with given parameters