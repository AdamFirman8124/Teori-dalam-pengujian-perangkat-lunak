

# Generated at 2022-06-13 09:34:51.645408
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    class Task(object):
        def __init__(self):
            self.args = dict()

    class TaskVars(object):
        def __init__(self):
            self.vars = dict()
            self.vars['ansible_check_mode'] = False

    class PlayContext(object):
        def __init__(self):
            self.connection = None
            self.port = None
            self.remote_addr = None
            self.remote_user = None

            self.become = None
            self.become_method = None
            self.become_user = None
            self.become_pass = None

    class Loader(object):
        def __init__(self):
            self.path_exists = lambda x: False


# Generated at 2022-06-13 09:34:58.637020
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    fake_ansible_module = 'test'
    fake_connection = 'test'
    fake_task = 'test'
    fake_tmp = 'test'
    fake_task_vars = {}
    action_module = ActionModule(fake_ansible_module, fake_connection, fake_task, fake_tmp, task_vars=fake_task_vars)

    # FIXME: What should we test?


# Generated at 2022-06-13 09:35:09.837693
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    class DummyConnection(object):
        def __init__(self, tmpdir):
            self.tmpdir = tmpdir
            self.transport = 'test'
        def _execute_module(self, conn, tmp, module_name, module_args, inject, complex_args=None, **kwargs):
            return dict(changed=True)
        def _exec_command(self, cmd):
            return (0, '', '')
        def _shell_out_compress(self, param, cmd, exec_cmd, environ, cwd, executable, stdin, stdout, stderr, shell, sudoable, executable_override=None):
            return (0, '', '')
        def join_shell_cmd(self, cmdlist):
            return ''.join(cmdlist)

# Generated at 2022-06-13 09:35:19.906310
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Arrange
    task_vars = dict()
    inject = dict()
    task_vars['inventory_hostname'] = 'test-host'
    executor = None
    loader = None
    task = Mock()

    task.args = dict()
    task.action = 'test-action-module'
    task.async_val = None
    task.environment = dict()

    # Act
    transfer = ActionModule(task, inject, loader, executor)

    # Assert
    assert transfer._task.args is not None
    assert len(transfer._task.args.keys()) == 0
    assert transfer._task.action == 'test-action-module'
    assert transfer._task.environment == dict()
    assert transfer._task.async_val == None
    assert transfer._task.args == dict()

# Unit

# Generated at 2022-06-13 09:35:28.493480
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    tmp = None
    task_vars = dict()
    module = ActionModule()
    result = module.run(tmp, task_vars)
    assert result['failed'] == True
    assert result['msg'] == 'src (or content) is required'
    module._task.args['dest'] = 'dest'
    result = module.run(tmp, task_vars)
    assert result['failed'] == True
    assert result['msg'] == 'src (or content) is required'
    module._task.args['src'] = 'src'
    module._task.args['content'] = 'content'
    result = module.run(tmp, task_vars)
    assert result['failed'] == True
    assert result['msg'] == 'src and content are mutually exclusive'
    module._task.args['src'] = 'src'


# Generated at 2022-06-13 09:35:39.158536
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    import ansible.compat.network_common
    from ansible.module_utils._text import to_bytes
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.utils.display import Display
    import ansible.utils.path
    import ansible.plugins.action
    import ansible.plugins.action.copy
    import ansible.playbook.task
    import ansible.executor.task_queue_manager
    import ansible.inventory.manager
    import ansible.executor.process.worker
    from ansible.vars.manager import set_var
    from ansible.vars.manager import VariableManager



# Generated at 2022-06-13 09:35:41.208171
# Unit test for constructor of class ActionModule
def test_ActionModule():
    a = ActionModule(None, dict(foo="bar"), dict(foo="bar"))
    assert a is not None

# Generated at 2022-06-13 09:35:50.588968
# Unit test for constructor of class ActionModule
def test_ActionModule():
    host = "localhost"
    port = 22
    user = "foo"
    passwd = "****"
    remote_pass = "****"
    name = "cat"
    args = dict(
        src="/tmp/src",
        dest="/tmp/dest"
    )
    task_args = dict(
        _raw_params="cat /tmp/src",
        _uses_shell=False,
        _uses_delegate=False,
        _task=Play().task
    )

    play_context = PlayContext()
    play_context.network_os = "linux"
    play_context.remote_addr = host
    play_context.remote_port = port
    play_context.password = passwd
    play_context.connection = "ssh"
    play_context.remote_user = user
    play_context

# Generated at 2022-06-13 09:36:02.501744
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import os
    import shutil
    from tempfile import mkdtemp
    from ansible.errors import AnsibleError
    # Create temporary directory
    test_dir = mkdtemp()
    os.chdir(test_dir)
    # Create ansible.cfg and playbook.yml
    shutil.copy('/etc/ansible/ansible.cfg', '.')
    shutil.copy('/usr/share/ansible/openshift-ansible/playbooks/prerequisites.yml', 'playbook.yml')
    # Create Hosts file
    with open("hosts", "wt") as f:
        f.write("localhost ansible_connection=local\n")
    # Create a module/action

# Generated at 2022-06-13 09:36:07.762529
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''
    Unit test for method run of class ActionModule
    '''
    # create a mock connection object
    connection = Connection()
    
    # create a mock module
    module = File(connection)

    # create a mock task with arguments for the file module
    arguments = dict(src="/path/to/src",dest="/path/to/dest")
    task = dict(action=dict(module='file',args=arguments))

    # create a mock ansible object
    ansibleobj = Ansible()
    ansibleobj.connection = connection
    ansibleobj.fail_json = MagicMock()

    # set the ansible object in the module object
    module.set_connection(connection)
    module.set_task(task)
    module.set_ansible(ansibleobj)

    # define return values of mock objects    

# Generated at 2022-06-13 09:36:55.167087
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule()
    assert action_module._supports_check_mode == True

# Generated at 2022-06-13 09:37:07.543257
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    task_vars = dict()

    am = ActionModule(None, task_vars=task_vars)

    assert am.run() == {'changed':False, 'invocation':{'module_args':{}}, '_ansible_verbose_always': True}
    assert am.run(tmp="notNone") == {'changed':False, 'invocation':{'module_args':{}}, '_ansible_verbose_always': True}
    assert am.run(tmp="notNone", task_vars=None) == {'changed':False, 'invocation':{'module_args':{}}, '_ansible_verbose_always': True}

    # Testing src
    task_vars['src'] = 'test_src'

# Generated at 2022-06-13 09:37:15.258634
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import unittest
    class TestArgs(object):
        def __init__(self, arguments_dict):
            self.__dict__.update(arguments_dict)

    def mock_ApiModuleFactory_create_argspec(self, command=None):
        argspec = MagicMock()
        argspec.parameters = {'path': {'type': 'string', 'aliases':['dest', 'dst']}, 'src':{'type': 'string'}, 'mode':{'type': 'string'}}
        return argspec
    
    
    class TestActionModule(unittest.TestCase):
        def setUp(self):
            self.stdout_utils_patch = _patch_stdout_utils()
            self.stdout_utils_patch.start()
            self.mock_datastore = Magic

# Generated at 2022-06-13 09:37:25.662078
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    print("Testing action module copy")
    yaml_file = 'test-copy/test.yaml'
    content = "test_content"
    dest = "test-copy/sub1"
    file_path = "test-copy/sub2"
    link_path = "test-copy/sub3"
    # src is not set
    print("case 1")
    test_args = dict(dest=dest)
    result = dict(msg="src (or content) is required")
    assert (ActionModule.run(ActionModule(), result, test_args) == result)
    # content is not set
    print("case 2")
    test_args = dict(src=file_path)
    result = dict(msg="dest is required")
    assert (ActionModule.run(ActionModule(), result, test_args) == result)


# Generated at 2022-06-13 09:37:41.210242
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    host = Mock()
    task = Mock()
    loader = Mock()
    tmp = Mock()
    play_context = Mock()
    connection = Mock()
    connection._shell.join_path.return_value = 'test'
    connection._shell.path_has_trailing_slash.side_effect = [False, True]
    play_context.become = False
    play_context.become_user = None

# Generated at 2022-06-13 09:37:47.110270
# Unit test for constructor of class ActionModule
def test_ActionModule():

    class TaskSrc(object):
        def __init__(self, args=dict()):
            self.args = args

    class Task(object):
        def __init__(self, src):
            self.args = src.args

    class Connection(object):
        def __init__(self):
            self._shell = None

    class PlayContext(object):
        def __init__(self):
            self.become = False
            self.become_user = 'root'
            self.connection = Connection()

    class AnsibleModuleSrc(object):
        def __init__(self, task_vars=dict()):
            self.task_vars = task_vars

    class AnsibleModule(object):
        def __init__(self, src):
            self.args = {}
            self.task_v

# Generated at 2022-06-13 09:37:57.486753
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from itertools import chain
    from ansible_collections.ansible.community.general.tests.unit.compat import unittest
    from ansible_collections.ansible.community.general.tests.unit.compat.mock import patch

    from ansible_collections.ansible.community.general.plugins.action import ActionModule
    from ansible_collections.ansible.community.general.plugins.action.copy import ActionModule as CopyModule

    from ansible.utils.path import unfrackpath

    from ansible.module_utils._text import to_bytes
    from ansible.module_utils._text import to_text

    from ansible.module_utils.common.collections import Mapping
    from ansible.errors import AnsibleError

    from copy import deepcopy


# Generated at 2022-06-13 09:38:09.806831
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    
    # Setup mock for _load_params
    with patch.object(ActionModule, '_load_params') as mock_load_params:
        # Setup variables
        tmp = None
        task_vars = dict()
        
        # Instantiate class
        actionModule = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
        
        # Mock return values
        mock_load_params.return_value = dict(src=None, content=None, dest=None, remote_src=False, local_follow=True)
        
        # Call method
        result = actionModule.run(tmp, task_vars)
        
        # Assertions
        assert result['failed'] == True

# Generated at 2022-06-13 09:38:11.423132
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    file_transfer = FileTransfer()
    source_files = {'files': [], 'directories': [], 'symlinks': []}

# Generated at 2022-06-13 09:38:14.113691
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Unit tests for method run of class ActionModule

    # TODO: write or generate tests for this module

    # temporary code to facilitate manual testing outside of unit tests

    module = ActionModule()

    # TODO: run this method as if it were being called from within a task

    args = dict(
        content="Hello World!",
        dest="/tmp/myfile",
    )

    module.run(**args)

# Generated at 2022-06-13 09:39:42.844167
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass



# Generated at 2022-06-13 09:39:44.531751
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action = ActionModule(None, None)
    assert action.run() == None

# Generated at 2022-06-13 09:39:47.523870
# Unit test for constructor of class ActionModule
def test_ActionModule():
    conn = Connection(None)
    task = Task()
    task.args = dict()
    am = ActionModule(conn, task, play_context=PlayContext())
    assert isinstance(am, object)


# Generated at 2022-06-13 09:39:54.338805
# Unit test for constructor of class ActionModule
def test_ActionModule():
    init_args = dict(
        task=MagicMock(),
        connection=MagicMock(),
        play_context=MagicMock(),
        loader=MagicMock(),
        templar=MagicMock(),
        shared_loader_obj=None
    )
    action = ActionModule(**init_args)
    assert action._task == init_args['task']
    assert action._connection == init_args['connection']
    assert action._play_context == init_args['play_context']
    assert action._loader == init_args['loader']
    assert action._templar == init_args['templar']
    assert action._shared_loader_obj is None

# Generated at 2022-06-13 09:40:05.028669
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import ansible.constants as C

    # Simulating the object that the Task class would give the ActionModule
    class FakeTask(object):
        def __init__(self):
            self.args = {'src': 'test_src', 'dest': 'test_dest', 'checksum': 'test_checksum', 'content': 'test_content', 'state': 'test_state',
                         'remote_src': True}

    class FakeShellModule(object):
        def __init__(self, tmpdir):
            self.tmpdir = tmpdir
            self.join_path = os.path.join

    class FakeConnection(object):
        def __init__(self):
            self.shell = FakeShellModule(C.DEFAULT_REMOTE_TMP)

    test_connection = FakeConnection()
    test_task = FakeTask()

# Generated at 2022-06-13 09:40:06.974644
# Unit test for constructor of class ActionModule
def test_ActionModule():
    ActionModule(task=dict(action=dict(module_name='a', module_args=dict())))


# Generated at 2022-06-13 09:40:16.561016
# Unit test for constructor of class ActionModule
def test_ActionModule():
    connection = MagicMock()
    task = MagicMock()
    loader = MagicMock()
    shared_loader_obj = MagicMock()
    connection.shared_loader_obj = shared_loader_obj
    tmp = os.path.join('/tmp','ansible_test',''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8)))
    os.makedirs(tmp)
    os.chdir(tmp)
    ac = ActionModule(loader=loader, task=task, connection=connection)
    assert ac._task == task
    assert ac._loader == loader
    assert ac._connection == connection
    assert ac._templar == shared_loader_obj._templar
    assert ac._shared_loader_obj == shared_loader_obj
    assert ac._play

# Generated at 2022-06-13 09:40:23.936878
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''
    :type: assert_equal
    '''
    # Constructor arguments.
    task = dict()
    connection = dict()
    play_context = dict()
    loader = dict()
    templar = dict()
    shared_loader_obj = dict()

    # Create instance of ActionModule.
    action_module = ActionModule(
            task,
            connection,
            play_context,
            loader,
            templar,
            shared_loader_obj)
    assert_equal(action_module.__class__.__name__, 'ActionModule')

# Generated at 2022-06-13 09:40:25.720874
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    a = ActionModule()
    return a

# Generated at 2022-06-13 09:40:26.542620
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass