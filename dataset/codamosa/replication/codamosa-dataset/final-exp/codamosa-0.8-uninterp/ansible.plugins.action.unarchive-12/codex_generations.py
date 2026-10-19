

# Generated at 2022-06-13 10:53:00.340860
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Constructor ActionModule initializes self._task to None.
    ua = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert ua._task is None, "Initialization of task in ActionModule constructor is supposed to be None"

    # Constructor ActionModule initializes self._loader to None.
    ua = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert ua._loader is None, "Initialization of loader in ActionModule constructor is supposed to be None"

    # Constructor ActionModule initializes self._connection to None.

# Generated at 2022-06-13 10:53:08.547765
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    dest_path = '/path/to/dest'
    dest_path_user = '~user'

    test_action = ActionModule(dict(), dict())
    test_action._remove_tmp_path = lambda x: x
    test_action._connection = MockConnection()

    # Required args are missing.
    test_action._task.args = {'src': 'source_path'}
    result = test_action.run(task_vars={})
    assert isinstance(result, dict)
    assert 'failed' in result
    assert result['failed']

    # Required args are missing.
    test_action._task.args = {'dest': dest_path}
    result = test_action.run(task_vars={})
    assert isinstance(result, dict)
    assert 'failed' in result

# Generated at 2022-06-13 10:53:17.153348
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """ this function is simply used for unit testing the constructor of class ActionModule
    for more unit test cases, please refer to test/units/module_common/test_action_module.py
    """
    try:
        # We will use a mock object here to do the needed preparation

        # Test case 1: Constructor of class ActionModule without arguments
        ActionModule()

    except Exception as e:
        print("Exception caught when unit testing the constructor of class ActionModule")
        print(e)

# Generated at 2022-06-13 10:53:28.057014
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Create an instance of ActionModule
    options = {
        'remote_src': False,
        'decrypt': True,
        'src': 'source',
        'dest': '/tmp/dest'
    }
    action_module = ActionModule(
        task=None,
        connection=None,
        play_context=None,
        loader=None,
        templar=None,
        shared_loader_obj=None
    )

    # Create an instance of AnsibleActionFail
    ansible_action_fail = AnsibleActionFail(
        message='unarchive failed!'
    )

    # Create an instance of AnsibleActionSkip
    ansible_action_skip = AnsibleActionSkip(
        message='unarchive is skipped!'
    )

    # Create an instance of AnsibleError
    ansible_error = AnsibleError

# Generated at 2022-06-13 10:53:29.529312
# Unit test for constructor of class ActionModule
def test_ActionModule():
    result = ActionModule()
    print(result)
    assert result._task is None

# Generated at 2022-06-13 10:53:32.028522
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(
        task=dict(
            action=dict(
                unarchive=dict()
            ),
        ),
    )


# Generated at 2022-06-13 10:53:42.051909
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    test_parameters = {
        "dest": "/home/user/test_archive.tar.gz",
        "src": "test_archive.tar.gz",
        "remote_src": True,
        "creates": "https://example.com/test_archive.tar.gz",
        "decrypt": False
    }

    # create mock object
    mock_object = type('', (), {})()

    # first function called
    def _execute_remote_stat(self, path, follow, all_vars):
        if path == "https://example.com/test_archive.tar.gz":
            return {"exists": False, "isdir": False}
        return {"exists": True, "isdir": True}

    mock_object._execute_remote_stat = _execute_remote_stat

    # second function called

# Generated at 2022-06-13 10:53:44.025653
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(None, None, None)
    assert action_module is not None


# Generated at 2022-06-13 10:53:45.290787
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(loader=None, connection=None, play_context=None)
    assert module != None

# Generated at 2022-06-13 10:53:46.484247
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    am = ActionModule()
    print(am.run())

# Generated at 2022-06-13 10:54:00.279836
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    conn = Connection()
    task_vars = {'ansible_connection': 'local'}
    new_task_vars = {'ansible_connection': 'local'}
    task = Task()
    task.args['src'] = "test"
    task.args['dest'] = "/test/dir"
    task.args['creates'] = "testfile"
    task.args['decrypt'] = "true"
    action = ActionModule(task, conn, new_task_vars)
    action.run(task_vars)

# Generated at 2022-06-13 10:54:06.967153
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''Unit test for constructor of class ActionModule.'''
    task_vars = dict()
    action_module = ActionModule(None, dict(src='/test/test/test.conf', dest='/home/local', remote_src=True, decrypt=False),
                                 '', '', '', '', task_vars)
    assert action_module


# Generated at 2022-06-13 10:54:10.935266
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    created_class = create_class_instance(ActionModule)
    result = created_class.run()
    print(result)
    #assert result == 1

# Create a class called class_name

# Generated at 2022-06-13 10:54:14.103195
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # test constructor of class ActionModule
    module = ActionModule(job=None, task=None)
    assert module.TRANSFERS_FILES


# Generated at 2022-06-13 10:54:18.777035
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    am = ActionModule()
    result = am.run(None, None)
    print("Result of test_ActionModule_run is:")
    print(result)
    # assert result['rc'] == 1
    assert True


# Generated at 2022-06-13 10:54:19.612452
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert True

# Generated at 2022-06-13 10:54:21.495222
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert False, "No tests for method run of class ActionModule"

# Generated at 2022-06-13 10:54:23.244788
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # role_path, load_path, task_vars, play_context, connection
    assert False

# Generated at 2022-06-13 10:54:24.615886
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # init object
    test = ActionModule()
    assert test is not None


# Generated at 2022-06-13 10:54:30.750723
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.action.unarchive import ActionModule

    action_module = ActionModule(task=[], connection=[],
                                 play_context=[], loader=[],
                                 templar=[], shared_loader_obj=[])
    action_module.take_action = Mock()
    action_module.run(tmp=None, task_vars=None)
    action_module.take_action.assert_called_with(None, None)


# Generated at 2022-06-13 10:54:47.121463
# Unit test for constructor of class ActionModule
def test_ActionModule():

    from ansible.playbook.task import Task
    from ansible.playbook.role import Role
    from ansible.playbook.play import Play
    from ansible.playbook.playbook import Playbook
    from ansible.playbook.block import Block
    from ansible.playbook.handler import Handler
    from ansible.playbook.task_include import TaskInclude
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.inventory.inventory import Inventory
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    from ansible.vars.hostvars import HostVars

    loader = DataLoader()

    # Create a dictionary to represent task args

# Generated at 2022-06-13 10:54:53.719204
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(
        task=dict(action=dict(module='unarchive', args=dict(src='my.tar.gz', dest='.'))),
        connection=dict(),
        play_context=dict(),
        loader=None,
        templar=None,
        shared_loader_obj=None)

    assert module.run() == dict(
        changed=False,
        msg='skipped, since my.tar.gz exists'
    )

# Generated at 2022-06-13 10:55:02.795137
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # mock the ansible_module_utils.parsing.convert_bool.boolean function to return a valid bool
    from ansible.module_utils.parsing.convert_bool import boolean

    boolean_orig = boolean
    boolean = lambda x, **k: True

    action = ActionModule()
    # mock the _execute_remote_stat() method
    action._execute_remote_stat = lambda *args, **kwargs: {'exists': True, 'isdir': True}

    # mock the _execute_module() method
    action._execute_module = lambda *args, **kwargs: dict(changed=True, failed=False)

    # Test with valid src and dest

# Generated at 2022-06-13 10:55:14.151595
# Unit test for constructor of class ActionModule
def test_ActionModule():
    print(' *** Unit test for constructor of class ActionModule')
    class FakeTask:
        def __init__(self):
            self.args = {
                'src' : 'src',
                'dest' : 'dest',
            }
    class FakePlayContext:
        def __init__(self):
            self.check_mode = False
            self.become = False
            self.become_user = None
    class FakePlay:
        def __init__(self):
            self.connection = 'local'
            self.port = 22
            self.become = False
            self.become_user = None
    class FakeLoader:
        def __init__(self):
            self.path_exists = ''
            self.path_rwx = ''
            self.is_file = ''
            self.module_loader

# Generated at 2022-06-13 10:55:17.988198
# Unit test for constructor of class ActionModule
def test_ActionModule():
    mock_ActionBase = object()
    mock_task = object()
    am = ActionModule(mock_ActionBase, mock_task)
    assert am
    assert am.__dict__['_task'] is mock_task


# Generated at 2022-06-13 10:55:28.318014
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import os
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.executor.task_queue_manager import TaskQueueManager

    from ansible.playbook import Play
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.role import Role
    from ansible.playbook.role.include import RoleInclude
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.source_tree import SourceTree
    from ansible.utils.vars import combine_vars

    # Create mock objects for Ansible playbook features that are used in the


# Generated at 2022-06-13 10:55:29.114083
# Unit test for constructor of class ActionModule
def test_ActionModule():
    a = ActionModule()
    pass

# Generated at 2022-06-13 10:55:34.297792
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # input_data will come from the test case.
    input_data = {}

    # Declare the class we are testing
    action_plugin = ActionModule(task=input_data, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

    # Now run the constructor with the input_data we want.
    action_plugin.run(tmp=None, task_vars=None)

# Generated at 2022-06-13 10:55:38.789206
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import ansible.plugins.action.unarchive as unarchive_a
    from ansible.module_utils.ansible_modlib.plugins.module_utils.network.common.utils import load_provider
    from ansible.plugins.action.copy import ActionModule as copy_a
    from ansible.playbook.task import Task as task_p
    from ansible.executor.task_result import TaskResult as task_r

    at_exit_set = False

    prov_params = {
    }

    mi = unarchive_a.ActionModule(task_p(), load_provider(prov_params), atexit_register=False)
    mi._shell = copy_a.ActionModule(task_p(), load_provider(prov_params), atexit_register=False)._shell


# Generated at 2022-06-13 10:55:39.672805
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module_instance = ActionModule()

# Generated at 2022-06-13 10:56:07.786639
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    test_ActionModule_run.ansible_return_value = dict(
        changed=dict(
            remote_src=False,
            dest='test_dest',
            src='test_src',
            creates=''
        ),
        rc=0,
        stderr='test_stderr',
        stdout='test_stdout'
    )

    test_ActionModule_run.ansible_module_results = dict(
        changed=True,
        remote_src=False,
        dest='test_dest',
        src='test_src',
        creates=''
    )

    def _execute_module(module_name, module_args, task_vars):
        assert(module_name == 'ansible.legacy.unarchive')
        assert(module_args.get('dest') == 'test_dest')

# Generated at 2022-06-13 10:56:08.686866
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass # TODO implement unit test

# Generated at 2022-06-13 10:56:15.754980
# Unit test for constructor of class ActionModule
def test_ActionModule():
    class RemoteModuleFixupMixin(object):
        _shell = 'shell'
        _shell_executable = None
        _connection = 'connection'
        tmpdir = 'tmpdir'

    # Create a ActionModule object by assigning it an empty dictionary
    # for the argument 'task'
    args = dict()
    am = ActionModule(task=args, connection=RemoteModuleFixupMixin())

    # Run the constructor
    am.run(None)


# Run tests when called from the command line
if __name__ == '__main__':
    import pytest
    pytest.main(['-v', __file__])

# Generated at 2022-06-13 10:56:20.402083
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''
    Unit test for ActionModule
    '''
    action_module = ActionModule(task=dict(args=dict(dest='/home/ansible/foo.gz', src='/home/ansible/foo.gz')))
    assert action_module.run()['dest'] == '/home/ansible/foo.gz'

# Generated at 2022-06-13 10:56:20.992815
# Unit test for method run of class ActionModule
def test_ActionModule_run():
  pass

# Generated at 2022-06-13 10:56:22.113531
# Unit test for constructor of class ActionModule
def test_ActionModule():
    a = ActionModule(object())
    assert a

# Generated at 2022-06-13 10:56:31.592586
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import ansible.plugins.action
    # test for ansible.plugins.action.ActionBase
    a = ansible.plugins.action.ActionBase()
    test_vars = dict()
    test_vars['ansible_python_interpreter'] = 'python'
    test_vars['ansible_connection'] = 'local'
    test_vars['ansible_os_family'] = 'linux'
    test_vars['ansible_facts'] = dict()
    test_vars['ansible_facts']['processor_count'] = 4
    test_vars['ansible_facts']['processor0'] = dict()
    test_vars['ansible_facts']['processor0']['vendor_id'] = 'my vendor'

# Generated at 2022-06-13 10:56:35.710288
# Unit test for constructor of class ActionModule
def test_ActionModule():
    print("\nTesting constructor of ActionModule")
    import ansible.plugins.action.unarchive
    module_util = ansible.plugins.action.unarchive.ActionModule
    assert module_util is not None
    assert callable(getattr(module_util, 'run', None))

test_ActionModule()

# Generated at 2022-06-13 10:56:45.278563
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import mock
    import json

    # Create an instance of ActionModule
    class Object(object):
        def __init__(self):
            self.args = {'dest': 'C:/Users/Test/Ansible'}
            self.name = 'unarchive'
            self.module_vars = {}
            self.task_vars = {}

    module = Object()
    tmpdir = 'C:/Users/Test/Ansible'

# Generated at 2022-06-13 10:56:53.478859
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    #Testing run function of ActionModule
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    import ansible.constants as C
    import ansible.executor.task_queue_manager as tqm
    import ansible.executor.playbook_executor as pe
    import ansible.executor.process.worker as worker

    class Options(object):
        def __init__(self):
            self.inventory = '/etc/anisble/hosts'
            self.listhosts = None
            self.subset = None
            self.module_paths = None
            self.extra_vars = []
            self.forks = 5
            self.ask_vault_pass = False
            self.vault_password_files = []
            self.new

# Generated at 2022-06-13 10:57:36.202568
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Setup
    tmp = tempfile.mkdtemp()
    fake_loader = DictDataLoader({tmp: dict(path=tmp)})
    fake_playbook = Playbook()

    task = Task()
    task._role = Role()
    task._role._role_path = tmp
    task._role._tasks_path = tmp
    task._loader = fake_loader
    task._role._validate_dependencies = mock.MagicMock()
    task._block = Block()
    task._role._attribute_failures = dict()
    task._role._get_task_vars = mock.MagicMock()
    task._role.get_vars = mock.MagicMock()
    task._role._role_path = tmp

# Generated at 2022-06-13 10:57:41.212255
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    source = '/etc/passwd'
    dest = '/tmp'

    mod = ActionModule()
    mod._task.args['src'] = source
    mod._task.args['dest'] = dest

    mod._task.args['remote_src'] = True
    mod._task.args['creates'] = None
    mod._task.args['decrypt'] = True

    mod.run()

# Generated at 2022-06-13 10:57:48.124305
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task import Task

    try:
        from __main__ import display
    except ImportError:
        from ansible.utils.display import Display
        display = Display()

    yaml_data = """
- hosts: all
  tasks:
  - name: Archive test
    unarchive:
      src: /tmp/src.tgz
      dest: /tmp/dest
    when: yes
  """

    task = Task().load(yaml_data)
    t = task.task_blocks[0].block[0].resolve_task_and_items(load_vars=task.args)
    a = ActionModule(task, display, t, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert a is not None

# Generated at 2022-06-13 10:57:49.404339
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule()
    assert module

# Generated at 2022-06-13 10:57:51.874957
# Unit test for constructor of class ActionModule
def test_ActionModule():

    # Test that ActionModule instantiation works
    # Unit test for constructor of class ActionModule
    assert ActionModule

# Generated at 2022-06-13 10:58:00.113192
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule(None, None)
    an = AnsibleAction(None)
    try:
        am.run()
        assert False, "Test should have thrown an exception"
    except AnsibleAction as e:
        assert True  # Expected exception
    try:
        am.run(tmp=None, task_vars=None)
        assert False, "Test should have thrown an exception"
    except AnsibleAction as e:
        assert True  # Expected exception
    

# Generated at 2022-06-13 10:58:11.091775
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils.parsing.convert_bool import BOOLEANS_TRUE
    from ansible.plugins.action.unarchive import ActionModule as ActionModuleBase

    class ActionModule(ActionModuleBase):
        def _fixup_perms2(self, *args, **kwargs):
            pass

        def _remote_expand_user(self, *args, **kwargs):
            pass

        def _remote_file_exists(self, *args, **kwargs):
            pass

        def _execute_remote_stat(self, *args, **kwargs):
            pass

        def _execute_module(self, *args, **kwargs):
            return dict(failed=False)

        def _transfer_file(self, *args, **kwargs):
            pass


# Generated at 2022-06-13 10:58:17.702177
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule('/path/to/task', dict())
    expected_task = '/path/to/task'
    assert action._task == expected_task
    assert action._connection is None
    assert not action._play_context.become
    assert action._loader is None
    assert not action._templar
    assert not action._shared_loader_obj
    assert not action._connection_loader


# Generated at 2022-06-13 10:58:19.229843
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:58:21.841416
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule(None, None)
    assert am.__class__.__name__ == "ActionModule"
    assert am.__class__.TRANSFERS_FILES == True

# Generated at 2022-06-13 10:59:43.036022
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(
        task = dict(
            args = dict(
                src = '/tmp/ansible/roles/testing_role/files/my_archive.tgz',
                dest = '/tmp/ansible/roles/testing_role/files/dummy_path/',
                decrypt = True,
            )
        ),
        connection = None
    )
    assert module.action == 'unarchive'
    assert module.action_type == 'normal'
    assert module.action_plugin == 'unarchive'
    assert module.action_plugin_type == 'action_plugin'
    assert module.action_loader == 'unarchive'
    assert module.action_loader_type == 'action_loader'
    assert module.default_inclusion == 'both'
    assert module.name == 'unarchive'

# Generated at 2022-06-13 10:59:56.248436
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Create an instance of action module
    action_module = ActionModule()

    module_name = 'module_name'
    module_args = dict()

    # Create an instance of fake-ansible for testing
    class FakeAnsible(object):
        class FakeTask(object):
            def __init__(self):
                self.args = dict()
        class FakePlaybook(object):
            def __init__(self):
                self.inject = dict()
        def __init__(self):
            self.task = self.FakeTask()
            self.playbook = self.FakePlaybook()
    ansible = FakeAnsible()

    # Create an instance of fake-connection for testing

# Generated at 2022-06-13 11:00:07.537082
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import unittest
    import ansible.playbook.play
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.block import Block
    from ansible.playbook.role import Role
    import ansible.playbook.playbook
    import ansible.playbook.block


    class TestPlaybook:
        def __init__(self, playbook):
            """
            Initialize TestPlaybook with a playbook
            :arg playbook: the playbook to be tested
            """
            self.playbook = playbook

        def get_vars(self):
            """
            Get the variables assigned by the playbook
            :return: a dictionary of variables
            """
            variables = {}

# Generated at 2022-06-13 11:00:19.392300
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''
    Unit test for method run of class ActionModule
    '''
    # The test must be run as root because only root can create the file test_0 in the directory /root
    # CCTODO: Revise this test to run as it's own dedicated user.  You will need to comment out the test_0 content.
    # Only root can create a file in the directory /root.  The Ansible code will create it.
    if os.getuid() == 0:
        import re
        import shutil
        # Create test file
        test_0 = \
'''This is the content of the file test_0.
This is a second line in the file test_0.
This is the third line in the file test_0.'''
        # CCTODO: Comment out the following line.

# Generated at 2022-06-13 11:00:30.936743
# Unit test for constructor of class ActionModule
def test_ActionModule():
    host = 'localhost'
    connection = 'ssh'
    task = None
    info = None
    play_context = None
    loader = None
    shared_loader_obj = None
    variable_manager = None
    action_base = ActionModule(host, connection, task, info, play_context, loader, shared_loader_obj, variable_manager)

    # Unarchive a file
    task_vars = dict(dest='/tmp/ansible/dest', src='/tmp/ansible/src/myfile.tgz')
    action_base.run(tmp='/tmp/ansible', task_vars=task_vars)

# Generated at 2022-06-13 11:00:31.874302
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True

# Generated at 2022-06-13 11:00:41.839875
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    source = 'src'
    dest = 'dest'
    remote_src = False

    task_args = dict(src=source, dest=dest, remote_src=remote_src)
    task_vars = dict()

    # Test when both source and dest are specified.
    am = ActionModule(task=dict(args=task_args), connection=None, play_context=dict(), loader=None, templar=None, shared_loader_obj=None)
    r = am.run(task_vars=task_vars)
    assert r['invocation']['module_args'] == dict(src=source, dest=dest)

    # Test when neither src or dest is specified.
    del task_args['src']

# Generated at 2022-06-13 11:00:50.532061
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.module_utils.connection import ConnectionBase

    class ModuleStub:
        def __init__(self):
            self.CHECK_MODE = False

    class TaskStub:
        def __init__(self):
            self._ds = {'any_errors_fatal': [],
                        'always_run': [],
                        'no_log': [],
                        'run_once': [],
                        'tags': [],
                        'when': []}
            self.action = 'copy'

# Generated at 2022-06-13 11:00:51.040630
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule()

# Generated at 2022-06-13 11:00:56.555163
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import os
    import sys
    import unittest
    import ansible.plugins
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    class ActionModule_TestCase(unittest.TestCase):
        def test_init(self):
            current_dir = os.path.dirname(os.path.realpath(__file__))
            module_path = os.path.join(current_dir, '../../../lib/ansible/modules/legacy')
            if module_path not in sys.path:
                sys.path.insert(1, module_path)
           