

# Generated at 2022-06-13 09:34:53.515621
# Unit test for constructor of class ActionModule
def test_ActionModule():
    temp_dir = tempfile.mkdtemp()
    test_host = FakeHost(temp_dir, temp_dir)

    test_task = Task()
    test_task._ds = dict(action=dict(name='remote'))
    test_task.args = dict(src='_test_src', dest='_test_dest')

    test_play = Play()
    test_play._ds = dict(hosts='test_host')
    _task_ds = dict(action=dict(name='remote', args=test_task.args))
    test_play.add_task(test_task, _task_ds)

    test_loader = DataLoader()

    test_variable_manager = VariableManager()
    test_variable_manager._extra_vars = dict()

    # Construct a mock remote_user
    test_remote_

# Generated at 2022-06-13 09:35:04.913623
# Unit test for constructor of class ActionModule
def test_ActionModule():
    filename = 'file.txt'
    filepath = os.path.join(C.DEFAULT_LOCAL_TMP, filename)
    testVars = {'file': filepath}
    task = dict(action={'module': 'copy', 'args': {'src': 'dummy', 'dest': filepath}})
    task_ds = Task(task)
    am = ActionModule(task_ds, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert os.path.exists(filepath)


if __name__ == '__main__':
    test_ActionModule()

# Generated at 2022-06-13 09:35:12.777779
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import chardet
    import copy
    import os
    import ansible.playbook.play_context

    # Mock the task module.
    class MockTaskModule(object):
        def __init__(self):
            self.args = {}

    task_module = MockTaskModule()
    set_module_args(dict(_original_basename='a', src='b', content=None, dest='c', directory_mode=None, remote_src=False, local_follow=False, follow=False, checksum=None, mode='preserve', owner=None, group=None, selevel=None, serole=None, setype=None, seuser=None, unsafe_writes=False))

# Generated at 2022-06-13 09:35:22.265066
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import ansible
    import ansible.playbook.play
    import ansible.playbook.task
    import ansible.playbook.role
    import ansible.playbook.block
    import ansible.playbook.handler
    import ansible.inventory.host
    import ansible.inventory.group
    import ansible.inventory.inventory
    import ansible.utils.template
    import ansible.utils.vars
    import ansible.executor.task_queue_manager
    import ansible.plugins
    import ansible.plugins.loader
    import ansible.plugins.action

    # Create a setup with valid options
    host = ansible.inventory.host.Host("localhost")
    group = ansible.inventory.group.Group("localhost")
    group.add_host(host)

# Generated at 2022-06-13 09:35:30.318384
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # NOTE: the tests are not run in the order they are defined here
    import ansible

    # Create a fake AnsibleModule object
    module = ansible.module_utils.basic.AnsibleModule(
            argument_spec={},
            supports_check_mode=True)
    # Create a fake loader with a mock inventory
    loader = ansible.parsing.dataloader.DataLoader()
    loader.set_inventory(ansible.inventory.Inventory(loader=loader))
    # Create a fake connection and shell
    host = ansible.inventory.host.Host(name='localhost')
    connection = ansible.connection.connection.Connection(host=host,
            port=22,
            loader=loader,
            module_class='copy',
            transport='local')
    connection._shell = Mock()

    # Create an Action

# Generated at 2022-06-13 09:35:40.997056
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''
    Unit tests for method run of class ActionModule
    '''

    # Clear out the member variables.
    module_args = {}
    module_args['dest'] = '/tmp/ansible_wOqe3j/test_dir'
    module_args['local_follow'] = True
    module_args['remote_src'] = False
    module_args['src'] = 'test_dir'
    module_args['src_dir'] = '/tmp/ansible_wOqe3j'
    module_args['src_path'] = '/tmp/ansible_wOqe3j'
    module_args['src_user'] = None
    module_args['src_groups'] = None
    module_args['_ansible_syspath'] = None
    module_args['_ansible_module_name']

# Generated at 2022-06-13 09:35:50.505279
# Unit test for constructor of class ActionModule
def test_ActionModule():
    host = Mock()
    task = Mock()
    connection = Mock()
    task_vars = dict()
    def setitem(name, item):
        task_vars[name] = item
    def get(name):
        return task_vars[name]
    def exists(name):
        return name in task_vars
    def get_bin_path(name):
        return '/bin/%s' % name
    setattr(task, 'args', dict())
    setattr(task, 'environment', dict())
    setattr(connection, '_shell', Mock())
    setattr(connection._shell, 'tmpdir', '/tmp')
    setattr(host, 'get_vars', Mock())
    setattr(host.get_vars, 'side_effect', get)

# Generated at 2022-06-13 09:36:02.455001
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Create an instance of ActionModule with a mock DefaultRunner
    action_module = ActionModule(mock.Mock())

    # Set default values on our mock
    action_module.runner = mock.Mock()
    action_module._remote_expand_user = mock.Mock(return_value='/mock_path')
    action_module._execute_module = mock.Mock(return_value={'changed': False})

    # Set default values on runner
    action_module.runner.get_remote_filename.return_value = '/mock_path'
    action_module.runner._create_content_tempfile = mock.Mock(return_value='/tmp/mock_content_tempfile')
    action_module.runner._remove_tmp_path = mock.Mock()

    # Set default values on module
    source

# Generated at 2022-06-13 09:36:07.682519
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Create a connection for the module to use
    test_connection = Connection('http://localhost')

    # Create a module for the plugin manager to handle
    test_module = ActionModule(test_connection)

    test_module.NO_TARGET_SYSTEM_WARNING = False

    # Create a task for the plugin manager to handle
    test_task = Task()

    test_task.args = dict(dest='/opt/test_copy.txt', src='test_copy.txt')

    test_task.args = dict(dest='/opt/test_copy.txt', content='random_string')

    test_task.args = dict(src='/opt/test_copy.txt', content='random_string')

    test_module._remove_tmp_path = MagicMock()

    test_module._create_content_tempfile = MagicMock

# Generated at 2022-06-13 09:36:17.071687
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule({'shell': ['/bin/false']})
    tmp = module._make_tmp_path()
    task_vars = {'ansible_check_mode': False}
    result = module.run(tmp, task_vars)
    assert result == {'failed': True, 'msg': 'src (or content) is required'}

    module = ActionModule({'shell': ['/bin/false'], 'src': 'file.txt'})
    tmp = module._make_tmp_path()
    task_vars = {'ansible_check_mode': False}
    result = module.run(tmp, task_vars)
    assert result == {'failed': True, 'msg': 'dest is required'}


# Generated at 2022-06-13 09:37:12.303112
# Unit test for constructor of class ActionModule
def test_ActionModule():
    ''' test_ActionModule
    This is a unit test for the constructor of the class ActionModule.
    '''

    # Inject needed modules
    inject_mock = MagicMock()
    inject_mock.return_value = dict()

    module_mock = MagicMock()
    module_mock.params = dict()

    task_mock = MagicMock()
    task_mock.args = dict()

    action_module = ActionModule(inject=inject_mock, module=module_mock, task=task_mock)

    assert action_module._task == task_mock
    assert action_module._loader == inject_mock.return_value
    assert action_module._shared_loader_obj == inject_mock.return_value


# Generated at 2022-06-13 09:37:23.419969
# Unit test for constructor of class ActionModule
def test_ActionModule():

    # Create fake application
    application = Application()
    application._connection = Connection(object())

    # Create fake task
    action_module = ActionModule(
        task = Task(
            play = Play(),
            connection = Connection(object())
        ),
        connection = Connection(object())
    )
    action_module._connection = Connection(object())
    task = Task(
        play = Play(),
        connection = Connection(object())
    )
    task._connection = Connection(object())
    task_vars = {}

    # Execute test
    action_module.run()
    action_module.run(tmp = application._connection._shell.tmpdir, task_vars = task_vars)
    action_module._task.args = {'src': None, 'content': None, 'dest': None}
    action_module.run

# Generated at 2022-06-13 09:37:35.540761
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText


# Generated at 2022-06-13 09:37:38.219749
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True # action module can't be tested directly


# Generated at 2022-06-13 09:37:42.387593
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Check if the AnsibleAction._loader is set to self._loader
    action = ActionModule(task=MagicMock(), connection=MagicMock(), play_context=MagicMock(), loader=MagicMock(), templar=MagicMock(), shared_loader_obj=None)
    assert action._loader == action.loader


# Generated at 2022-06-13 09:37:54.355343
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    #
    # When remote_src=True
    #
    # Setup
    import os
    fixture_path = os.path.join(os.path.dirname(__file__), 'fixtures')
    content='dummy_content'
    task_path=os.path.join(fixture_path, 'action_module_test_task.yml')
    playbook_path=os.path.join(fixture_path, 'action_module_test_playbook.yml')
    local_file_path=os.path.join(fixture_path, 'action_module_test.txt')
    remote_file_path_absolute=os.path.join(fixture_path, 'action_module_test_remote.txt')
    remote_file_path_relative='./action_module_test_remote.txt'

# Generated at 2022-06-13 09:38:01.684969
# Unit test for constructor of class ActionModule
def test_ActionModule():
    ''' unit test for class ActionModule '''
    # create a mock objects of class Connection
    connection = Connection()

    # create a mock object of class Task
    task = Task()

    # create an object of class ActionModule
    am = ActionModule(connection, task)

    # assert if the object is instance of class ActionModule
    assert isinstance(am, ActionModule)


# Generated at 2022-06-13 09:38:09.589714
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import tempfile
    content = 'foobar'
    dest_dir = tempfile.mkdtemp()
    dest_file = dest_dir + '/foo.txt'
    action_module = ActionModule()
    source_file = content_tempfile = action_module._create_content_tempfile(content)
    source_rel = os.path.basename(source_file)
    dest = dest_file
    task_vars = {}

    result = action_module._copy_file(source_file, source_rel, content, content_tempfile, dest, task_vars, False)
    assert result['changed'] is True
    assert(filecmp.cmp(source_file, dest_file))
    os.remove(source_file)
    os.remove(dest_file)
    os.rmdir(dest_dir)

# Generated at 2022-06-13 09:38:16.786439
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''
    Unit test for ActionModule
    '''
    task = MockTask()
    action_plugin = ActionModule(task=task, connection=MockConnection())

    assert action_plugin._task == task
    assert action_plugin._connection == task._connection



# Generated at 2022-06-13 09:38:18.871378
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule(None, None, None, None)
    assert am._connection is None
    assert am._task is None
    assert am._shared_loader_obj is None
    assert am._loader is None
    assert not am._task_vars


# Generated at 2022-06-13 09:39:20.326026
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Test parameters
    tmp = 'tmp'
    task_vars = dict()

    # Instantiate object of class ActionModule
    am = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

    # Test execution of method run of class ActionModule
    am.run(tmp, task_vars)

# Generated at 2022-06-13 09:39:32.055156
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """Unit test for construction of class and basic checks."""
    # Create dummy object that will result in a fake connection
    class module_executor_dummy(object):
        def __init__(self, task, connection, tmp, module_compression):
            pass

    # Create a dummy task
    class task_dummy(object):
        def __init__(self, args):
            self.args = args

    # Create fake connection plugin
    class connection_dummy(object):
        def __init__(self, play_context, new_stdin):
            pass

        def info(self):
            return dict()

        def connect(self):
            return False

    # Instantiate a dummy class to run with, just so we have something to run.

# Generated at 2022-06-13 09:39:47.514141
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    from ansible.plugins.action.copy import ActionModule
    import ansible.constants as C


# Generated at 2022-06-13 09:39:52.312184
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Create an instance of our class
    am = ActionModule(connection=None, task_vars={})
    print(am)

if __name__ == '__main__':
    test_ActionModule_run()

# Generated at 2022-06-13 09:39:53.420255
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule is ActionModule

# Generated at 2022-06-13 09:39:59.326338
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Create a fake Ansible Task object
    Task = collections.namedtuple('Task', 'args')
    task = Task(args={'dest': 'test_dest', 'src': 'test_src'})

    # Create a fake Ansible Connection object
    Connection = collections.namedtuple('Connection', '_shell _shell_executable')
    connection = Connection(_shell=None, _shell_executable=None)

    # Create a fake Ansible PlayContext object
    PlayContext = collections.namedtuple('PlayContext', 'prompt check_mode')
    play_context = PlayContext(prompt=None, check_mode=None)

    # Create a fake Ansible Loader object
    BaseLoader = collections.namedtuple('BaseLoader', '_get_basedir')
    _get_basedir = lambda x: 'test_basedir'

# Generated at 2022-06-13 09:40:05.562320
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule(
        task=dict(
            action=dict(
                module_name="copy",
                module_args=dict(
                    src="source_file_or_dir",
                    dest="destination_dir"
                )
            )
        ),
        connection=dict(
            transport="ssh"
        ),
        play_context=dict()
    )
    assert am.connection==dict(
        transport="ssh"
    )

# Generated at 2022-06-13 09:40:17.373137
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    dest_dir = tempfile.mkdtemp()

# Generated at 2022-06-13 09:40:26.346084
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import ansible.plugins.action.copy as copy
    # insantiate a copy object
    copy_action = copy.ActionModule(dict(ANSIBLE_MODULE_ARGS={}), {})
    # it should have the right clsss name
    assert copy_action.__class__.__name__ == "ActionModule"
    # set some attributes
    copy_action.set_task(dict(action="copy", src="/path/to/src", dest="/path/to/dest"))
    copy_action.set_connection("connection")
    # it should have a correct task attribute
    assert copy_action._task == dict(action="copy", src="/path/to/src", dest="/path/to/dest")
    # it should have a correct connection attribute
    assert copy_action._connection == "connection"
    # it should have a correct

# Generated at 2022-06-13 09:40:38.729775
# Unit test for method run of class ActionModule

# Generated at 2022-06-13 09:42:40.661219
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    tmp = tempfile.mkdtemp()
    file_0 = tempfile.NamedTemporaryFile(dir=tmp)
    file_1 = tempfile.NamedTemporaryFile(dir=tmp)
    dirs  = [file.name for file in os.scandir(tmp) if file.is_dir()]
    results = []
    for dir in dirs:
        module = ActionModule(task=dict(action=dict(args=dict(src=dir, dest=file_0.name, checksum='sha1'), module_args='', module_name='copy')))
        results.append(module.run(task_vars=dict()))
    assert results[0] == results[1]

# Generated at 2022-06-13 09:42:42.957771
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert hasattr(ActionModule, 'run')

if __name__ == '__main__':
    test_ActionModule()

# Generated at 2022-06-13 09:42:43.973798
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 09:42:48.014910
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''Unit test for method run of class ActionModule'''
    # Set up the input parameters
    tmp = None
    task_vars = None

    # initialize class
    actionmodule = ActionModule(None, None)
    # call method run of class ActionModule
    result = actionmodule.run(tmp, task_vars)
    # assert result



# Generated at 2022-06-13 09:42:49.011062
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 09:43:03.845908
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import ansible.utils.unsafe_proxy
    import ansible.utils.template

    am = ActionModule(dict(ANSIBLE_MODULE_ARGS=dict()), task_vars=dict(ansible_connection='local'))
    assert am is not None
    assert isinstance(am.action_args, dict)
    assert isinstance(am.task_vars, dict)
    assert am.task_vars.get('ansible_connection') == 'local'
    assert isinstance(am._loader, ansible.parsing.dataloader.DataLoader)
    assert isinstance(am._task, ansible.playbook.task.Task)
    assert isinstance(am._play, ansible.playbook.play.Play)

# Generated at 2022-06-13 09:43:04.462216
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 09:43:12.033641
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """Unit test for method `ActionModule::run`
    """
    import json
    import tempfile
    import os
    import os.path
    import shutil
    import traceback
    import stat
    import ansible.errors
    import ansible.module_utils.remote_management.shell.powershell

    class TestActionModule(ActionModule):
        def run(self, tmp=None, task_vars=None):
            self._task_vars = task_vars
            return super(TestActionModule, self).run(tmp, task_vars)
        def _remote_expand_user(self, path):
            return path.replace('~', 'TEST_HOME')

# Generated at 2022-06-13 09:43:19.573415
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Test invalid action
    action = ActionModule(dict(action='unknown', src='/my/input', dest='/my/output'))
    assert not action.is_valid()

    # Test action is not 'copy'
    action = ActionModule(dict(action='get_url', src='/my/input', dest='/my/output'))
    assert action.is_valid()

    # Test invalid source
    action = ActionModule(dict(action='copy', src=None, dest='/my/output'))
    assert not action.is_valid()

    # Test invalid destination
    action = ActionModule(dict(action='copy', src='/my/input', dest=None))
    assert not action.is_valid()

    # Test valid copy

# Generated at 2022-06-13 09:43:26.067065
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task import Task
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.playbook.play_context import PlayContext

    mygroup = Group('mygroup')
    myhost = Host('myhost')
    myhost.set_variable('ansible_ssh_user', 'testuser')
    myhost.set_variable('ansible_ssh_pass', 'testpassword')
    # testhost.set_variable('ansible_ssh_port', 2222)
    mygroup.add_host(myhost)

    task = Task()
    task._role = None
    task.context = PlayContext()
    task.context._connection = 'smart'
    task.context._play_context.remote_addr = "myhost"
    task.context._play_