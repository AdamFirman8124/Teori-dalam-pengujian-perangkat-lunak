

# Generated at 2022-06-13 10:52:48.046621
# Unit test for constructor of class ActionModule
def test_ActionModule():
    a = ActionModule()
    print(a)

# Generated at 2022-06-13 10:52:50.095141
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''
    Unit test for method run of class ActionModule
    '''
    pass


# Generated at 2022-06-13 10:52:53.620370
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule()
    assert module.__class__.__name__ == 'ActionModule'
    assert module.TRANSFERS_FILES is True


# Generated at 2022-06-13 10:53:06.813355
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    x = None  # TODO: Build testcase
    x = None  # TODO: Build testcase
    x = None  # TODO: Build testcase
    x = None  # TODO: Build testcase
    x = None  # TODO: Build testcase
    x = None  # TODO: Build testcase
    x = None  # TODO: Build testcase
    x = None  # TODO: Build testcase
    x = None  # TODO: Build testcase
    x = None  # TODO: Build testcase
    x = None  # TODO: Build testcase
    x = None  # TODO: Build testcase
    x = None  # TODO: Build testcase
    x = None  # TODO: Build testcase
    x = None  # TODO: Build testcase

# Generated at 2022-06-13 10:53:14.773522
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Create the object with required arguments
    action_module = ActionModule(task='test', connection='test', play_context='test', loader='test', templar='test', shared_loader_obj='test')
    # test the values of initialized variable
    assert action_module._connection == 'test'
    assert action_module._loader == 'test'
    assert action_module._play_context == 'test'
    assert action_module._shared_loader_obj == 'test'
    assert action_module._task == 'test'
    assert action_module._templar == 'test'
    assert action_module.action_buffers == {}
    assert action_module.action_results == []
    assert action_module.action_runners == {}
    assert action_module.DEFAULT_TRANSFER_STRATEGY == 'smart'

# Generated at 2022-06-13 10:53:26.431970
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_mod = ActionModule()
    action_mod._task.args = { 'src': 'src', 'dest': 'dest' }
    action_mod._task.action = 'unarchive'
    tmp_dir = 'tmp_dir'
    action_mod._remove_tmp_path = lambda a: None
    action_mod._fixup_perms2 = lambda a, b: None
    action_mod._transfer_file = lambda a, b: None
    action_mod._execute_remote_stat = lambda a, b, c: { 'exists': True, 'isdir': True }
    action_mod._connection = lambda: None
    action_mod._connection._ext_name = 'ext_name'
    action_mod._connection._shell = lambda: None
    action_mod._connection._shell.tmpdir = 'tmp_dir'

# Generated at 2022-06-13 10:53:33.788438
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Test the in-memory data.
    test_data = {
        'remote_src': False,
        'src': 'src',
        'dest': 'dest',
    }
    # Set up a class instance and run it.
    action = ActionModule()
    result = action.run(test_data)
    # The results come back as a dict ready for Ansible.
    #   There is an error in the results.
    assert result['changed'] is True
    assert result['rc'] == 1
    assert result['msg'] == "Unable to extract to dest, it must be a directory."

# Generated at 2022-06-13 10:53:35.754373
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """ Unit test for method run of class ActionModule """


# Generated at 2022-06-13 10:53:38.245676
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    arguments = {'dest': '/home/testUser/testDir/testDir2', 'src': 'src/file.tar.gz'}
    module = ActionModule(arguments)
    result = module.run()

# Generated at 2022-06-13 10:53:42.947576
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule(
        task=dict(args=dict()),
        connection=None,
        play_context=None,
        loader=None,
        templar=None,
        shared_loader_obj=None
    )
    assert am.TRANSFERS_FILES is True

# Generated at 2022-06-13 10:53:52.789094
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule is not None

# Generated at 2022-06-13 10:53:56.121088
# Unit test for constructor of class ActionModule
def test_ActionModule():
    a = ActionModule(1, 2, 3, 4)
    if not isinstance(a, ActionBase):
        raise AssertionError('ActionModule is not a subclass of ActionBase')
    if not isinstance(a, object):
        raise AssertionError('ActionModule is not a subclass of object')

# Generated at 2022-06-13 10:54:04.556783
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.action import ActionModule
    class TestActionModule(ActionModule):
        def run(self,tmp=None,task_vars=None):
            print("This is a test of ActionModule")
            pass

    t = TestActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    t.run()


# Generated at 2022-06-13 10:54:06.566450
# Unit test for constructor of class ActionModule
def test_ActionModule():
    m = ActionModule()
    assert m is not None


# Generated at 2022-06-13 10:54:10.030722
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    a = ActionModule()
    b = a._task
    c = AnsibleAction(None)
    d = c.result
    assert a.run() == d

# Generated at 2022-06-13 10:54:14.473075
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """Unit test the function ``ansible.plugins.action.unarchive.ActionModule.run``."""
    # get a mock object of class ActionModule and pass it test data.
    module = get_mock_action_module(data)
    result = module.run()
    # check the results against pre-defined results from test data.
    assert result == test_result


# Generated at 2022-06-13 10:54:26.807298
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Test action plugin class ActionModule
    module = ActionModule(None, None, {}, False, False, False)

    src = '/tmp/installer/ansible-test-installer-1.0-SNAPSHOT'
    dest = './'
    remote_src = True
    creates = None
    decrypt = True
    args = {
        'src': src,
        'dest': dest,
        'remote_src': remote_src,
        'creates': creates,
        'decrypt': decrypt
    }

    task_vars = {}

    # test result of run method
    result = module.run(None, task_vars)
    assert result == None


# Generated at 2022-06-13 10:54:38.812880
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    class Connection(object):
        def __init__(self):
            self.host = 'localhost'
            self.port = 22
            self.user = 'user'
            self.password = 'passwd'
            self.private_key_file = ''
            self.passphrase = ''
    class PlayContext(object):
        def __init__(self):
            self.network_os = 'linux'
            self.remote_addr = '127.0.0.1'
            self.remote_user = 'user'
            self.password = 'passwd'
            self.port = 22
            self.become = False
            self.become_method = 'sudo'
            self.become_user = None
            self.become_pass = None
            self.private_key_file = None

# Generated at 2022-06-13 10:54:40.169525
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''
    test the run method of ActionModule
    '''
    pass

# Generated at 2022-06-13 10:54:43.005803
# Unit test for constructor of class ActionModule
def test_ActionModule():
    ''' Unit test for constructor of ActionModule
    '''
    action_module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert action_module

# Generated at 2022-06-13 10:54:53.050094
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:54:56.285595
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert (action.TRANSFERS_FILES == True)

# Generated at 2022-06-13 10:55:06.516978
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import collections, os.path, tempfile
    # Create an instance of the action plugin class
    action_plugin = ActionModule()

    # Mock an 'ansible.parsing.dataloader.DataLoader' object
    # DataLoader is needed to validate the tasks
    class DataLoader:
        def __init__(self, *args, **kwargs):
            self.path_exists = os.path.exists
            self.get_real_file = os.path.realpath
        def path_exists(self, path):
            return self.path_exists(path)
        def set_basedir(self, basedir):
            pass
        def get_real_file(self, filename, decrypt=False):
            return self.get_real_file(filename)
    action_plugin._loader = DataLoader()

   

# Generated at 2022-06-13 10:55:17.536380
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Constructor
    module = ActionModule(
        task=dict(action=dict(module='unarchive', args=dict(
            src='/tmp/src',
            dest='/tmp/dest'
        ))),
        connection=None,
        play_context=None,
        loader=None,
        templar=None,
        shared_loader_obj=None
    )
    # Check type
    assert type(module) == ActionModule
    # Check instance attributes
    assert hasattr(module, '_task')
    assert hasattr(module, '_connection')
    assert hasattr(module, '_play_context')
    assert hasattr(module, '_loader')
    assert hasattr(module, '_templar')
    assert hasattr(module, '_shared_loader_obj')

# Generated at 2022-06-13 10:55:27.900522
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action = ActionModule()

    # Test for method run.
    #
    # 1. Test when the src is not specified and dest is specified.

    assert(action.run(tmp=None, task_vars={})['failed'] == True)

    # Test for method run.
    #
    # 2. Test when the src is specified and dest is not specified.

    assert(action.run(tmp=None, task_vars={'src': 'src'})['failed'] == True)

    # Test for method run.
    #
    # 3. Test when the src is specified and dest is specified but creates is also specified.

    assert(action.run(tmp=None, task_vars={'src': 'src', 'dest': 'dest', 'creates': 'creates'})['skipped'] == True)

    # Test for method

# Generated at 2022-06-13 10:55:34.438275
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """
    Test the constructor of class ActionModule
    :return: None
    """
    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.module_utils.common.removed import removed
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.playbook import Playbook
    from ansible.plugins.callback import CallbackBase

    class AnsibleDummyModule(ActionModule):
        """
        Dummy class that inherits from ActionModule
        """

# Generated at 2022-06-13 10:55:40.065360
# Unit test for method run of class ActionModule
def test_ActionModule_run():
	"""
	ActionModule run method unit test stub.
	"""
	# Construct test object
	dummy_connection = object()
	dummy_play_context = object()
	obj = ActionModule(dummy_connection, dummy_play_context)

	# Invoke method
	result = obj.run(tmp=None, task_vars=None)

	# Check result
	assert result == None


# Generated at 2022-06-13 10:55:40.573916
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert True

# Generated at 2022-06-13 10:55:49.844551
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import json
    import mock

    # Mock task
    task = mock.Mock()
    task._role = None
    task.args = {'src': 'source'}
    # Mock connection
    connection = mock.Mock()
    connection.shell.tmpdir = 'tmp'
    connection.shell.join_path.return_value = 'tmp/source'
    connection.shell.exists.return_value = False
    connection.shell.isdir.return_value = False
    connection.join_path.return_value = '/home/test_user/test'
    connection.remote_file_exists.return_value = False
    connection.remote_expand_user.return_value = 'test_dir'
    connection.get_option.return_value = False
    # Mock inventory
    inventory = mock.Mock()

# Generated at 2022-06-13 10:55:51.249137
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule is not None


if __name__ == '__main__':
    test_ActionModule()

# Generated at 2022-06-13 10:56:11.467199
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule()

# Generated at 2022-06-13 10:56:13.260521
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ''' Test for method run of class ActionModule
    '''
    pass

# Generated at 2022-06-13 10:56:14.571661
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass


# Generated at 2022-06-13 10:56:16.356961
# Unit test for method run of class ActionModule

# Generated at 2022-06-13 10:56:16.930480
# Unit test for constructor of class ActionModule
def test_ActionModule():
    pass

# Generated at 2022-06-13 10:56:20.549678
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = ActionModule()
    return_data = action_module.run(tmp=None, task_vars=None)
    assert return_data

if __name__ == '__main__':
    test_ActionModule_run()

# Generated at 2022-06-13 10:56:23.958466
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    a = ActionModule(None, dict(), dict(), dict(), None, None)  # TODO: More parameters?
    try:
        a.run()
    except AnsibleActionFail:
        return True
    return False


# Generated at 2022-06-13 10:56:24.658938
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert True

# Generated at 2022-06-13 10:56:33.390587
# Unit test for constructor of class ActionModule
def test_ActionModule():
    host = 'localhost'
    port = 22
    user = 'vagrant'
    password = 'vagrant'
    playbook_basedir = '.'
    loader = None
    shared_loader_obj = None
    task_uuid = None
    tmpdir = None
    connection = 'smart'
    # Constructor ActionModule(task, connection, play_context, loader, templar, shared_loader_obj)
    # Instantiate task
    task = DummyTask()
    # Instantiate play_context
    play_context = DummyPlayContext()
    # Instantiate loader
    loader = DummyLoader()
    # Instantiate templar
    templar = DummyTemplar()
    shared_loader_obj = DummySharedLoaderObj()
    task_vars = None

# Generated at 2022-06-13 10:56:38.078515
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    test_args_1 = {
        'src': 'tests/test_files/test_unarchive_1.tar.gz',
        'dest': '/',
        'creates': 'test_file_1',
    }
    test_action_module_1 = ActionModule(None, test_args_1, None)
    test_action_module_1.run()

# Generated at 2022-06-13 10:57:18.514289
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert module.run() == None

# Generated at 2022-06-13 10:57:19.700638
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert True


# Generated at 2022-06-13 10:57:27.352060
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_result import TaskResult
    from ansible.executor.play_iterator import PlayIterator
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.utils.vars import load_extra_vars
    from ansible.utils.vars import load_options_vars
    from ansible.utils.vars import load_options_vars
    from ansible.utils.vars import load_options_vars
    from ansible.vars.reserved import Reserved
   

# Generated at 2022-06-13 10:57:28.750781
# Unit test for constructor of class ActionModule
def test_ActionModule():
    for ActionModule in [ActionModule, ActionModule]:
        assert ActionModule

# Generated at 2022-06-13 10:57:38.514276
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor

    task = Task()
    task._role = None
    task.args = dict()
    task.args['src'] = "path/to/source"
    task.args['dest'] = "path/to/destination"

    play_context = PlayContext()
    task_queue_manager = TaskQueueManager(play_context)
    task_queue_manager._pending_results = 5
    playbook_executor = PlaybookExecutor(play_context)

# Generated at 2022-06-13 10:57:45.923752
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """
    Unarchive module.

    Test the return from run() action plugin method.
    """
    module = AnsibleModule(
        argument_spec=dict(
            src=dict(type='str', required=True),
            dest=dict(type='str', required=True),
            creates=dict(type='str', required=False),
            copy=dict(type='bool', required=False),
            remote_src=dict(type='bool', required=False),
            decrypt=dict(type='bool', required=False),
        ),
        supports_check_mode=True
    )

    # NOTE: (devkulkarni1) This test is not working anymore. I just skipped it.
    #       This is not a easy test. We will have to mock out a lot of things to make it working.
    #       Please come back and

# Generated at 2022-06-13 10:57:53.294211
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''
    Create an instance of the class ActionModule and assert that it
    is an instance of ActionBase.
    '''

    # Create instance of class ActionModule and retrieve its type
    act_mod = ActionModule()
    act_mod_type = type(act_mod)

    # Assert that type of instance of class ActionModule is ActionBase
    assert issubclass(act_mod_type, ActionModule) == True

# Generated at 2022-06-13 10:57:56.348849
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    sources = ['files/archive.tar.gz', 'files/archive.tar', 'files/archive.zip']


# Generated at 2022-06-13 10:57:58.350677
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule(None, None)
    # CCTODO: Implement this.

# Generated at 2022-06-13 10:57:59.011114
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:59:33.547574
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(
        task_vars='test_task_vars',
        connection='test_connection',
        play_context='test_play_context',
        loader='test_loader',
        templar='test_templar',
        shared_loader_obj='test_shared_loader_obj'
    )

    print(action_module)


# Generated at 2022-06-13 10:59:43.198172
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.module_utils.connection import Connection
    from ansible.module_utils.parsing.convert_bool import boolean
    from ansible.module_utils.parsing.splitter import parse_kv
    from ansible.plugins.action.unarchive import ActionModule as unarchive

    my_args = parse_kv('src=/home/admin/test_dir dest=/home/admin/dest_dir remote_src=False')


# Generated at 2022-06-13 10:59:47.742606
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # myActionModule = ActionModule(connection=None, task=None, task_vars=None, templar=None)
    # check to ensure that myActionModule is of type ActionModule
    assert type(myActionModule) is ActionModule


# Generated at 2022-06-13 10:59:52.757122
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    print('Unit test for method run of class ActionModule...')
    # Test action module run.
    result = ActionModule().run()
    print('result: %s' % result)
    return

# Add unit tests to test the method run of class ActionModule.
test_ActionModule_run()

# Generated at 2022-06-13 11:00:00.340504
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import unittest

    class testActionModule_run(unittest.TestCase):
        def setUp(self):
            def call_run(self, tmp, task_vars=None):
                return {'rc': 0}
            self.am = ActionModule()
            self.am.get_real_file = lambda x: x
            self.am.run = lambda x, task_vars=None: x
            self.am.runBackup = lambda x: x
            self.am.runAction = lambda x: x
            self.am.runConn = lambda x, y, z, d=True: {'rc': 0}
            self.am.set_action = lambda: None
            self.am.run = call_run.__get__(self.am)

# Generated at 2022-06-13 11:00:07.027067
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(
        task=dict(action=dict(module_name='', module_args='', remote_user='', user='',
                              connection='', args='', tmp='', debug=''),
                  args=dict(src='/path/to/src',
                            dest='/path/to/dest',
                            creates=None,
                            copy=None,
                            decrypt=True)))
    print(action_module)

# Generated at 2022-06-13 11:00:15.603780
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import ansible.plugins.action.unarchive as m_unarchive
    import ansible.plugins.action as m_action
    import ansible.plugins as m_plugins
    import ansible.plugins.connection as m_connection
    import ansible.plugins.loader as m_loader
    import ansible.vars as m_vars
    import ansible.template as m_template
    import ansible.errors as m_errors


# Generated at 2022-06-13 11:00:22.245042
# Unit test for constructor of class ActionModule
def test_ActionModule():
  unarchive_task = dict(action=dict(module='unarchive', args=dict(src='myfile.tgz', dest='/dest')))
  action_module = ActionModule(unarchive_task, {})
  assert action_module.run()['skip_reason'] == "skipped, since ./myfile.tgz exists"

# Generated at 2022-06-13 11:00:33.013818
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible import context
    from ansible.plugins.action import ActionBase
    from ansible.utils.path import unfrackpath
    import pytest

    context.CLIARGS = pytest.CLIARGS

    task_vars = {
        'ansible_check_mode': False,
        'ansible_verbosity': 2,
        'verbosity': 2,
    }

    action_base = ActionBase()
    action_base._loader = pytest.mocks.mock_loader()
    action_base._connection = pytest.mocks.mock_connection()

    # Test when source is None
    action_module = ActionModule()
    action_module.__dict__ = action_base.__dict__.copy()
    action_module._task = pytest.mocks.mock_task()
   

# Generated at 2022-06-13 11:00:35.401213
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """
    # -------------------------------------------------------------------------------------------------
    # Test that run method of class ActionModule works as expected
    # -------------------------------------------------------------------------------------------------
    """
    pass