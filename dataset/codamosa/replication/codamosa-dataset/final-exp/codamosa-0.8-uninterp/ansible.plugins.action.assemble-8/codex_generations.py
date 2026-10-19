

# Generated at 2022-06-13 09:23:51.625959
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import ansible.plugins.action.assemble

    module = ansible.plugins.action.assemble.ActionModule(load_arg_spec={}, templar=None, shared_loader_obj=None)
    assert module is not None

# Generated at 2022-06-13 09:23:52.058527
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True

# Generated at 2022-06-13 09:24:03.076276
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    module_path = "ansible.builtin.assemble"
    module_class = "ActionModule"

    task_vars = {
        'ansible_ssh_user': 'root',
        'ansible_ssh_pass': 'root',
        'ansible_connection': 'local',
        'ansible_playbook_python': '/usr/bin/python2.7',
    }

    tmp  = 'ansible_assemble_test'
    dest = '/tmp/dest'


    if not os.path.isdir(tmp):
        os.mkdir(tmp)

    def _mkdir(dir):
        if not os.path.isdir(dir):
            os.mkdir(dir)


# Generated at 2022-06-13 09:24:09.836339
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Testing with all parameters
    task = {"args": {'src': '/Users/usr/ansible/data',
                     'dest': '/Users/usr/ansible/data/payload',
                     'delimiter': 'EOF',
                     'remote_src': 'yes',
                     'regexp': '/^foo',
                     'follow': False,
                     'ignore_hidden': False,
                     'decrypt': True}}
    tmp = ''
    task_vars = {}

    action_obj = ActionModule(task, tmp, task_vars)
    # Testing without remote_src parameter

# Generated at 2022-06-13 09:24:15.277802
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # test for constructor
    am = ActionModule(None, None)
    assert am.TRANSFERS_FILES == True
    assert am._supports_check_mode == False


if __name__ == '__main__':
    # Unit test for constructor of class ActionModule
    test_ActionModule()

# Generated at 2022-06-13 09:24:26.571585
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.plugins.loader import connection_loader

    # Load action plugin
    a = connection_loader.get('local', class_only=True)()
    a.connection = connection_loader.get('local', class_only=True)()
    a._task = connection_loader.get('local', class_only=True)()
    a._loader = connection_loader.get('local', class_only=True)()
    a._templar = connection_loader.get('local', class_only=True)()
    a._shared_loader_obj = connection_loader.get('local', class_only=True)()
    a._connection = connection_loader.get('local', class_only=True)()
    a._play_context = connection_loader.get('local', class_only=True)()


# Generated at 2022-06-13 09:24:35.725791
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible import module_utils
    from ansible.module_utils.basic import AnsibleModule

    module_args = dict(
        src='/home/test/test_dir',
        dest='/home/test/test_dir2',
        remote_src=False
    )

    module = AnsibleModule(argument_spec=module_args)
    module_utils.basic.ASK_PASSWORD = False
    module_utils.HAS_PARAMIKO = False
    module_utils.HAS_CRYPTOGRAPHY = False
    module_utils.CRYPTOGRAPHY_FOUND = False
    module.connection = 'local'
    module.run()

# Generated at 2022-06-13 09:24:42.415450
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module_name = 'assemble'
    task_name = 'test_task'
    task_vars = {'dest': 'dest_var'}
    tmp = None
    play_context = 'play_context'
    loader = None
    shared_loader_obj = None

    action_module = ActionModule(module_name, task_name, task_vars, tmp, play_context, loader, shared_loader_obj)
    assert type(action_module).__name__ == 'ActionModule'

# Generated at 2022-06-13 09:24:44.061920
# Unit test for constructor of class ActionModule
def test_ActionModule():
    a = ActionModule(None,"/tmp")
    assert a is not None


# Generated at 2022-06-13 09:24:45.312654
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    raise NotImplementedError()



# Generated at 2022-06-13 09:24:58.532650
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''
    Test ActionModule run method
    '''

    # Set up object
    action = ActionModule()

# Generated at 2022-06-13 09:25:02.205024
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Test with no arguments
    assert ActionModule()

    # Test with arguments
    assert ActionModule(task=None, connection=None, play_context=None, loader=None,
                    templar=None, shared_loader_obj=None)

# Generated at 2022-06-13 09:25:03.441801
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''test class ActionModule'''
    module = ActionModule(None, None)
    assert(module is not None)

# Generated at 2022-06-13 09:25:11.182027
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # fake class for ActionModule unit test
    class FakeActionModule():
        def __init__(self, task, connection, play_context, loader, templar, shared_loader_obj):
            self._task = task
            self._connection = connection
            self._play_context = play_context
            self._loader = loader
            self._templar = templar
            self._shared_loader_obj = shared_loader_obj
            self.runner_path = 'ansible.runner'

        def _execute_module(self, module_name, module_args=None, task_vars=None, wrap_async=None):
            if module_args is None:
                module_args = dict()
            if task_vars is None:
                task_vars = dict()

# Generated at 2022-06-13 09:25:12.898031
# Unit test for constructor of class ActionModule
def test_ActionModule():
    mod = ActionModule()

    assert mod is not None


# Generated at 2022-06-13 09:25:15.800335
# Unit test for constructor of class ActionModule
def test_ActionModule():
    global constants
    global module_loader
    am = ActionModule(constants=constants, module_loader=module_loader)

# Generated at 2022-06-13 09:25:16.946476
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 09:25:29.757518
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    print('Testing class ActionModule for method run')
    # From /usr/lib/python3.5/inspect.py:
    # def getargspec(func):
    #    """Get the names and default values of a function's arguments.
    #
    #    A tuple of four things is returned: (args, varargs, varkw, defaults).
    #    'args' is a list of the argument names (it may contain nested lists).
    #    'varargs' and 'varkw' are the names of the * and ** arguments or None.
    #    'defaults' is an n-tuple of the default values of the last n arguments.
    #    """
    try:
        from inspect import getargspec
    except ImportError:
        from py3compat import getargspec


# Generated at 2022-06-13 09:25:38.536862
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.module_utils.facts.system.distribution import Distribution
    from ansible.module_utils.facts.system.linux import Linux
    from ansible.module_utils.facts.system.bsd import BSD
    linux = Linux()
    bsd = BSD()
    dist = Distribution()

# Generated at 2022-06-13 09:25:40.584362
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # create ActionModule object
    obj = ActionModule()
    result = obj.run()
    assert result['_ansible_verbose_always'] == False
    assert result['_ansible_no_log'] == False

# Generated at 2022-06-13 09:26:11.610664
# Unit test for constructor of class ActionModule
def test_ActionModule():
    c = dict(
        ansible_connection='local',
        ansible_python_interpreter='/usr/bin/env python'
    )
    t = dict(
        action=dict(
            module_name='assemble',
            module_args={'src': 'tests/unit/module_utils/test_assemble/fragments', 'dest': '/tmp/hello'}
        ),
        task=dict(
            args={'src': 'tests/unit/module_utils/test_assemble/fragments', 'dest': '/tmp/hello'},
            delegate_to='localhost'
        ),
        play=dict(
            remote_user='root',
            hosts='localhost'
        )
    )

# Generated at 2022-06-13 09:26:13.258899
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(None, None, None, None)
    assert isinstance(action_module, ActionModule)

# Generated at 2022-06-13 09:26:19.063775
# Unit test for constructor of class ActionModule
def test_ActionModule():

    # Check the class can be instantiated.
    task_vars = {'ansible_python_interpreter': '/usr/bin/python'}
    action_module_object = ActionModule(dict(), task_vars)
    assert action_module_object is not None



# Generated at 2022-06-13 09:26:27.674136
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    def _setup_action_module_for_testing(mocker):
        task_args = dict(src='/tmp', dest='/tmp/dest')
        task_vars = dict(ansible_verbosity=0)
        test_action = ActionModule(mocker.Mock(), task_args, task_vars)

        mocker.patch('ansible.module_utils.basic.AnsibleModule.exit_json')
        mocker.patch('ansible.module_utils.basic.AnsibleModule.fail_json')
        mocker.patch('ansible.utils.hashing.checksum_s').return_value = 'foo'
        mocker.patch('ansible.plugins.action.ActionBase._execute_remote_stat').return_value = dict(checksum='foo')

        return test_action


# Generated at 2022-06-13 09:26:29.960283
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(None, None, None)
    assert action_module is not None

# Generated at 2022-06-13 09:26:33.411920
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module_instance = ActionModule()
    # To avoid error in unit test
    action_module_instance._remove_tmp_path("test")
    assert not isinstance(action_module_instance, ActionModule)

# Generated at 2022-06-13 09:26:47.741440
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # run() parameters
    tmp = None
    task_vars = {}

    # create a dummy class to test run()
    class ActionModule_test(ActionModule):

        def _assemble_from_fragments(self, src_path, delimiter=None, compiled_regexp=None, ignore_hidden=False, decrypt=True):
            return '/tmp/test'

        def _remote_expand_user(self, dest):
            return dest

        def _execute_remote_stat(self, dest, all_vars=dict(), follow=False):
            return { 'checksum': 'e45678' }

        def _transfer_file(self, path, remote_path):
            return remote_path

        def _fixup_perms2(self, file):
            return


# Generated at 2022-06-13 09:26:51.778557
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # construct ActionModule
    am = ActionModule()
    # check params
    assert am._supports_check_mode == False
    assert am.TRANSFERS_FILES == True



# Generated at 2022-06-13 09:26:52.487264
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 09:27:03.202239
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import mock

    connection_mock = mock.Mock()
    connection_mock.host = magic_host_name
    connection_mock.port = magic_port_number

    task_mock = mock.Mock()
    task_mock.args = {
        'src': magic_file_name,
        'dest': magic_dir_name,
        'delimiter': '',
        'regexp': r'.*',
        'ignore_hidden': False,
        'decrypt': True,
    }
    task_mock.async_val = 1
    task_mock.notify.return_value = None

    display_mock = mock.Mock()
    display_mock.display.return_value = None

    plugin_options_mock = mock.Mock()
    loader_

# Generated at 2022-06-13 09:27:58.914243
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.executor.task_result import TaskResult


# Generated at 2022-06-13 09:28:06.265438
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Create a FakeLoader instance
    fake_loader = DictDataLoader({})
    # Create a FakePlayContext instance
    fake_play_context = PlayContext()
    # Create a FakeTask instance
    fake_task = Task()

    # Create a ActionModule instance
    action_module = ActionModule(fake_loader, fake_play_context, fake_task)

    # Test get_tmp_path()
    action_module.get_tmp_path('/tmp/test.sh')
    # Test _prefix_login_path()
    action_module._prefix_login_path('/root')
    # Test _remote_expand_user()
    action_module._remote_expand_user('/etc/passwd')
    # Test _execute_module()

# Generated at 2022-06-13 09:28:07.303915
# Unit test for method run of class ActionModule
def test_ActionModule_run():
   pass

# Generated at 2022-06-13 09:28:17.849459
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import os
    import shutil
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_result import TaskResult
    from ansible.executor.process.result import ResultProcess
    from ansible.executor.process.worker import WorkerProcess
    from ansible.executor.task_executor import TaskExecutor
    from ansible.vars.manager import VariableManager
    from ansible.vars.hostvars import HostVars
    from ansible.vars.unsafe_proxy import UnsafeProxy
    from ansible.utils.vars import combine_vars
    from ansible.utils.vars import load_extra_vars
    from ansible.utils.vars import load_options_vars

# Generated at 2022-06-13 09:28:20.852442
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    action_module.run()


# Generated at 2022-06-13 09:28:29.022784
# Unit test for method run of class ActionModule
def test_ActionModule_run():
	# Test 1: test_data1.yml
	module = ActionModule()
	module._task.args['src'] = u"/home/ranjan/Ansible/ansible-git/ansible/lib/ansible/modules/files/"
	module._task.args['dest'] = u"/etc/ansible/ansible.cfg"
	module._task.args['remote_src'] = u"yes"
	task_vars = None
	result = module.run(None, task_vars)
	assert result == {u'failed': True, u'rc': 0, u'msg': u'invalid value for remote_src', u'stderr': u"ERROR! all values for remote_src must be 'yes' or 'no'"}
	return
	

# Generated at 2022-06-13 09:28:39.593522
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Set up necessary mocks

    # Mock object of class class AnsibleFileResult
    class MockAnsibleFileResult():
        def __init__(self):
            self.path = None
            self.stat = None

    # Mock object of class class AnsibleFileResult
    class MockAnsibleFileResult():
        def __init__(self):
            self.path = None
            self.stat = None
            self.module_stdout = None
            self.msg = None
            self.exception = None
            self.module_name = None

    # Mock object of class class AnsibleConnection
    class MockAnsibleConnection():
        def __init__(self):
            self._shell = None

    # Mock object of class class ActionBase
    class MockActionBase():
        def __init__(self):
            self._play_

# Generated at 2022-06-13 09:28:43.411249
# Unit test for constructor of class ActionModule
def test_ActionModule():

    class TestActionModule:
        ''' Test class to make sure static methods get copied to new class '''
        class TestActionBase:
            pass

    action_module = ActionModule(loader=None, task=None, connection=None)
    assert action_module.fixup_perms2 == TestActionModule.TestActionBase.fixup_perms2

# Generated at 2022-06-13 09:28:50.638522
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.block import Block
    from ansible.playbook.role.include import RoleInclude
    from ansible.executor.task_result import TaskResult
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.plugins.loader import action_loader

    #create dummy playcontext object
    play_context = PlayContext()
    play_context.become = True

# Generated at 2022-06-13 09:28:51.329848
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 09:30:15.627333
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    m = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert m.run() == {}

# Generated at 2022-06-13 09:30:28.948559
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # create instance
    options = {
        'connection': 'local',
        'forks': 10,
        'remote_user': 'ubuntu',
        'ask_pass': False,
        'private_key_file': '',
        'ssh_common_args': '',
        'sftp_extra_args': '',
        'scp_extra_args': '',
        'ssh_extra_args': '',
        'become': False,
        'become_method': 'sudo',
        'become_user': 'root',
        'verbosity': 0,
        'check': False,
        'listhosts': None,
        'listtasks': None,
        'listtags': None,
        'syntax': None,
        'diff': False
    }

    # create instance of PlayContext


# Generated at 2022-06-13 09:30:34.875256
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # test with passing non-zero argument to constructor
    res = ActionModule(1)
    # test with passing zero argument to constructor
    res = ActionModule(0)
    # test with passing no argument to constructor
    res = ActionModule()
    # test with passing argv type argument to constructor
    argv = [""]
    res = ActionModule(argv)
    assert res.__class__.__name__ == "ActionModule"

# Generated at 2022-06-13 09:30:35.925368
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert not ActionModule(loader=None, action=None)

# Generated at 2022-06-13 09:30:46.648882
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ActionModule_obj = ActionModule()
    ActionModule_obj._supports_check_mode = False
    src = 'test.src'
    dest = 'test.dest'
    remote_src = 'test.remote_src'
    regexp = 'test.regexp'
    follow = False
    ignore_hidden = False
    decrypt = True
    tmp = None
    task_vars = dict()
    assert isinstance(ActionModule_obj.run(tmp, task_vars), dict)
    remote_src = 'no'
    ActionModule_obj._task.args = dict(src=src, dest=dest, remote_src=remote_src, regexp=regexp, follow=follow, ignore_hidden=ignore_hidden, decrypt=decrypt)
    task_vars = dict()

# Generated at 2022-06-13 09:30:54.543402
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # test_ActionModule_without_args
    assert ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

    # test_ActionModule_with_args
    assert ActionModule(
        task=dict(
            args=dict(
                src=None, dest=None, delimiter=None, remote_src='yes', regexp=None, follow=False, ignore_hidden=False
            )
        ),
        connection=None,
        play_context=None,
        loader=None,
        templar=None,
        shared_loader_obj=None
    )

# Generated at 2022-06-13 09:31:00.752634
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.plugins.action import ActionModule
    import ansible.playbook
    import ansible.playbook.task
    import ansible.utils.template

    ansible.playbook.SETUP_CACHE['foo'] = 1
    playbook = ansible.playbook.PlayBook()
    variable_manager = ansible.playbook.task.variable_manager
    loader = ansible.playbook.task.loader

    variable_manager.set_inventory(ansible.inventory.Inventory("localhost"))
    task = ansible.playbook.task.Task()
    task.args = {'src': 'test', 'dest': 'test'}

    assert 'foo' in ansible.playbook.SETUP_CACHE
    action = ActionModule(playbook, task, variable_manager, loader)

# Generated at 2022-06-13 09:31:04.438468
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule(None, {}, None, {}) # No need for a task here
    assert action.uses_shell is False
    assert action.supports_check_mode is False
    assert action.always_run is True
    assert action.connection._shell is not None


# Generated at 2022-06-13 09:31:12.022281
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    c = dict(foo='bar')
    task = dict(args=dict(src=None, dest=None))
    try:
        ActionModule(task, c).run()
    except AnsibleActionFail as e:
        assert(e.result['msg'] == 'src and dest are required')
    task = dict(args=dict(src=None, dest='foo'))
    try:
        ActionModule(task, c).run()
    except AnsibleActionFail as e:
        assert(e.result['msg'] == 'src and dest are required')
    task = dict(args=dict(src='foo', dest=None))
    try:
        ActionModule(task, c).run()
    except AnsibleActionFail as e:
        assert(e.result['msg'] == 'src and dest are required')

# Generated at 2022-06-13 09:31:15.402533
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.module_utils.actions import AnsibleModule
    module_args = {
        'src': 'source',
        'dest': 'destination'
    }
    module_obj = AnsibleModule(argument_spec={
        'src': {'required': True},
        'dest': {'required': True},
    }, argument_spec=module_args)
    action_obj = ActionModule(module_obj)
    assert isinstance(action_obj, ActionBase)