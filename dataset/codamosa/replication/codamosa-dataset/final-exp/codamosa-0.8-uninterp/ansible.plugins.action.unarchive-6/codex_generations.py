

# Generated at 2022-06-13 10:52:59.690451
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.task import Task
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText

    basedir = os.path.abspath(os.path.dirname(__file__))
    task_vars = dict()
    tmp = '/tmp'
    task = Task()
    task.args = {
        'content': "foo",
        'dest': "bar",
        'remote_src': "True",
    }
    am = ActionModule(task, tmp, task_vars)
    am._execute_module = lambda module_name, module_args, task_vars: {'failed': False, 'changed': True}
    am._loader = lambda: None
    am._loader.path_dwim = lambda x: x

# Generated at 2022-06-13 10:53:00.292742
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:53:02.650434
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

# Generated at 2022-06-13 10:53:08.980017
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''Test function run of class ActionModule.
    '''

    task_vars = {}
    loader = None
    tmp = None
    source = None
    dest = None
    remote_src = None
    creates = None
    decrypt = None
    connection = None
    action = ActionModule(loader, connection, source, dest, remote_src, creates, decrypt, tmp, task_vars)

    result = action.run(tmp, task_vars)
    assert result['failed'] == True
    assert result['msg'] == "src (or content) and dest are required"
    assert result['unreachable'] == False

    action = ActionModule(loader, connection, source, dest, remote_src, creates, decrypt, tmp, task_vars)
    result = action.run(tmp, task_vars)

# Generated at 2022-06-13 10:53:22.609084
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    task_vars = dict()
    module_tmp = 'None'
    task_action = dict(_ansible_module_name='unarchive',
        src='/path/to/archive',
        dest='/path/to/deploy',
        creates='/path/to/deploy/file',
        remote_src='True')
    task_action_mocker = mock.patch('lib.action.ActionModule.run')
    with task_action_mocker:
        task_action_mocker = mock.patch('lib.action.ActionBase.run')
        with task_action_mocker:
            # test case 01: dest is a dir
            dest = '/path/to/deploy'
            task_vars['ansible_check_mode'] = False
            task = Task(task_action)
            action = ActionModule

# Generated at 2022-06-13 10:53:24.184513
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True # TODO: implement your test here


# Generated at 2022-06-13 10:53:26.949737
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # We need to create class instance, then call its run method
    ActionModule.run()
    # If we get here, it means that test passed, otherwise exception will be raised


# Generated at 2022-06-13 10:53:29.419064
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """This is a constructor test for ActionModule"""

    action = ActionModule(None, {}, {}, {})
    print(action)

# Generated at 2022-06-13 10:53:30.255863
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert True

# Generated at 2022-06-13 10:53:30.892717
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule()

# Generated at 2022-06-13 10:53:41.848890
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # No error if it works correctly
    ActionModule(None, None, None, None)
    pass

# Generated at 2022-06-13 10:53:52.417980
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Test a normal run.
    action = ActionModule({"module_name": "unarchive", "module_args": {'src': '/tmp/foo', 'dest': '/tmp/bar'}})
    res = action.run()
    assert('failed' in res and res['failed'] is False)
    assert('src' in res and res['src'] == '/tmp/bar/foo')

    # Test a run with remote_src=True.
    action = ActionModule({"module_name": "unarchive", "module_args": {'src': '/arbitrary/path/filename', 'dest': '/tmp/bar', 'remote_src': True}})
    res = action.run()
    assert('failed' in res and res['failed'] is False)

# Generated at 2022-06-13 10:53:57.284648
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Test this code by creating an instance of this class:
    am = ActionModule(
        task=None,
        connection=None,
        play_context=None,
        loader=None,
        templar=None,
        shared_loader_obj=None
    )
    # Execute the run() method of the instance:
    result = am.run(tmp=None, task_vars=None)
    # print(result)
    # Assert the result is what was expected:
    assert isinstance(result, dict)
    assert result == {'failed': True, 'msg': "parameters are mutually exclusive: ('copy', 'remote_src')"}

# Generated at 2022-06-13 10:54:11.052234
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """
    ActionModule.run() Test case
    """
    import unittest
    import mock
    from ansible.plugins.action import ActionModule

    connection = mock.MagicMock()
    connection.shell = mock.MagicMock()
    connection.shell.tmpdir = mock.MagicMock()
    connection.shell.join_path = mock.MagicMock(return_value="test_string")
    connection.shell.join_path("test_str1", "test_str2")
    connection._shell = mock.MagicMock()
    connection._shell.join_path = mock.MagicMock(return_value="test_string")
    connection._shell.join_path("test_str1", "test_str2")
    connection._shell.tmpdir = mock.MagicMock()

# Generated at 2022-06-13 10:54:12.611507
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Create an instance of ActionModule
    am = ActionModule()

    result = am.run()

    assert result is not None

# Generated at 2022-06-13 10:54:15.574319
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(load_paths=['/foo/bar'], task=dict(action=dict()))
    assert action_module._load_paths == ['/foo/bar']
    assert action_module._task == {'action': {}}

# Generated at 2022-06-13 10:54:16.424570
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:54:18.379861
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(None, None, None) is not None


# Generated at 2022-06-13 10:54:31.943514
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.compat.tests import unittest
    from ansible.compat.tests.mock import Mock, patch

    class TestActionModule(unittest.TestCase):
        def test_ActionModule_run_with_missing_src_and_dest(self):
            from ansible.plugins.action import ActionModule
            from ansible.module_utils.legacy import core as legacy_module_utils

            class MockTask():
                def __init__(self):
                    self.args = dict()
                    self.args['src'] = None
                    self.args['dest'] = None

            class MockPlayContext():
                def __init__(self):
                    self.check_mode = False
            class MockLoader():
                def get_real_file(self):
                    return '/path/to/file'

# Generated at 2022-06-13 10:54:32.690834
# Unit test for constructor of class ActionModule
def test_ActionModule():
    pass

# Generated at 2022-06-13 10:54:50.924293
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """ Unit tests for class ActionModule. """
    assert True

if __name__ == '__main__':
    test_ActionModule()

# Generated at 2022-06-13 10:54:52.304634
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """Work in progress"""
    actionmodule = ActionModule(None, None)

# Generated at 2022-06-13 10:55:02.004521
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = dict(action='copy')

    # Mock classes and objects that ActionModule will use.
    mock_action_base = create_autospec(ActionBase).return_value
    mock_connection = create_autospec(ConnectionBase).return_value
    mock_task = create_autospec(Task)
    mock_task.args = action
    mock_loader = create_autospec(DataLoader)
    mock_play_context = create_autospec(PlayContext)

    mock_task.action = action
    mock_task.async_val = None
    mock_task.notify = []
    mock_task.run_once = False
    mock_task.loop = None
    mock_task.until = None
    mock_task.loop_args = {'count': 1}
    mock_task.check_

# Generated at 2022-06-13 10:55:04.191609
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule(None, None, None, None, None)
    assert am


# Generated at 2022-06-13 10:55:05.529257
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(None, None, None, None)._task.name == 'unarchive'

# Generated at 2022-06-13 10:55:12.462912
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule('/tmp/test_action_unarchive_module', {'src': '/tmp/test_action_unarchive_module/src'}, False, False, 10)
    result = module.run(tmp='/tmp/test_action_unarchive_module/tmp', task_vars={'dest': '/tmp/test_action_unarchive_module/dest'})
    assert result.get('changed') is True
    assert result.get('msg') == 'unarchived'
    assert result.get('rc') == 0
    assert result.get('dest') == '/tmp/test_action_unarchive_module/dest/manifests'
    assert result.get('start') == 0
    assert result.get('delta') == 0
    assert result.get('stderr') == ''

# Generated at 2022-06-13 10:55:21.425646
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from UnitTest import UnitTest
    from ansible.plugins.action.unarchive import ActionModule
    from ansible.plugins.action import ActionBase
    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext

    task = Task()
    task._role = None
    task.args = {"src": "/tmp/myfile.txt", "dest": "/home/user/dest", "remote_src": False}
    test = UnitTest(action_plugin=ActionModule, task=task, connection=None, play_context=PlayContext(), loader=None, templar=None, shared_loader_obj=None)

    with test.test("test_ActionModule_run"):
        test.assert_equals(test.action_plugin.run(), {})



# Generated at 2022-06-13 10:55:22.842804
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule is not None


# Generated at 2022-06-13 10:55:25.932785
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import ansible.plugins.action.unarchive
    module = ansible.plugins.action.unarchive
    results = module.ActionModule()
    assert isinstance(results, module.ActionModule) is True, ('%s is an instance of' % type(results))

# Generated at 2022-06-13 10:55:26.530017
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule()

# Generated at 2022-06-13 10:55:57.588505
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    raise NotImplementedError("No tests for example.py")

# Generated at 2022-06-13 10:55:58.160069
# Unit test for constructor of class ActionModule
def test_ActionModule():
    pass



# Generated at 2022-06-13 10:56:08.305514
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Instantiating the class
    action_module_obj = ActionModule()

    # Mocking
    obj = action_module_obj
    obj._task.args = dict()
    obj._task.args['src'] = 'src'
    obj._task.args['dest'] = 'dest'
    obj._task.args['remote_src'] = 'remote_src'
    obj._task.args['creates'] = 'creates'
    obj._task.args['decrypt'] = 'decrypt'
    obj.run(None, None)

    # Mocking
    obj = action_module_obj
    obj._task.args = dict()
    obj._task.args['src'] = 'src'
    obj._task.args['dest'] = 'dest'

# Generated at 2022-06-13 10:56:09.643862
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass # Dummy for using module as library

# Generated at 2022-06-13 10:56:17.390771
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.task import Task
    import ansible.module_local_test_runner as runner

    context = PlayContext()
    connection = runner.FakeConnection(runner.get_pseudo_executor())
    tqm = TaskQueueManager(connection=connection)
    loader = tqm._loader
    task = Task()

    ex = runner.FakeActionModule(
        connection=connection,
        task=task,
        play_context=context,
        loader=loader,
    )

    print(type(ex))
    print(type(ex.run()))

# Generated at 2022-06-13 10:56:27.938592
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Setup test class
    test_module = AnsibleModule({}, {'src': 'test-source', 'dest': 'test-dest', 'remote_src': True}, {}, True, {})
    test_result = dict(changed=False)
    test_class = ActionModule(test_module, {}, {'role_path': 'test-role_path'}, task_vars={'role_path': 'test-role_path'}, result=test_result)

    # Test 1
    # test exception raised "src and dest are required"
    test_result = dict(changed=False)
    test_class = ActionModule(test_module, {}, {'role_path': 'test-role_path'}, task_vars={'role_path': 'test-role_path'}, result=test_result)
    test_class

# Generated at 2022-06-13 10:56:31.416167
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule('test', {'key': 'value'}, 'ansible_connection')
    assert module._task.args['key'] == 'value'
    assert module._connection._play_context.connection == 'ansible_connection'


# Generated at 2022-06-13 10:56:40.208595
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import ansible.executor.task_result
    result = ansible.executor.task_result.TaskResult(host=None, task=None)


# Generated at 2022-06-13 10:56:41.372805
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert(ActionModule(None, dict()).TRANSFERS_FILES)


# Generated at 2022-06-13 10:56:46.207104
# Unit test for constructor of class ActionModule
def test_ActionModule():
    fake_task = {'args': {'src': 'src', 'dest': 'dest'}}
    fake_connection = {'_shell': {'tmpdir': 0, 'join_path': lambda *a: a}}
    action_module = ActionModule(fake_task, fake_connection)

    assert action_module._task == fake_task
    assert action_module._connection == fake_connection
    assert action_module.cattr == {}



# Generated at 2022-06-13 10:57:49.026616
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:57:49.793471
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:57:51.736865
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule()
    assert (am.TRANSFERS_FILES == True)

# Generated at 2022-06-13 10:57:54.727077
# Unit test for constructor of class ActionModule
def test_ActionModule():
    print("ActionModule constructor: ")
    obj = ActionModule()
    assert isinstance(obj, ActionModule)


# Generated at 2022-06-13 10:57:56.678461
# Unit test for constructor of class ActionModule
def test_ActionModule():
    class FakeActionModule(ActionModule): pass

    assert isinstance(FakeActionModule(), ActionModule)

# The test_* functions below are not unit tests, but tests to check the functionality of the
# ActionModule class as a whole.


# Generated at 2022-06-13 10:57:58.585737
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''
    :return:
    '''
    pass

# Generated at 2022-06-13 10:58:01.126237
# Unit test for constructor of class ActionModule
def test_ActionModule():
    if ActionModule is not None:
        am = ActionModule()
        if am is not None:
            pass
    else:
        raise Exception("Unable to create ActionModule")

# Generated at 2022-06-13 10:58:01.784919
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:58:03.543840
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert isinstance(ActionModule, object)


# Generated at 2022-06-13 10:58:05.246886
# Unit test for constructor of class ActionModule
def test_ActionModule():
	# Creating new object of a class
	myObj = ActionModule()

# Generated at 2022-06-13 11:00:39.032763
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """
    Unit test for method run of class ActionModule.
    """
    pass

# Generated at 2022-06-13 11:00:43.716198
# Unit test for constructor of class ActionModule
def test_ActionModule():
    task_vars = dict()
    am = ActionModule(task=dict(args=dict(src='/tmp/absolute', dest='/tmp/dest', remote_src=False)), connection='connection', play_context=dict(become=False))
    assert am.run(task_vars=task_vars)['_ansible_verbose_always'] == True

# Generated at 2022-06-13 11:00:52.022054
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import sys
    import unittest
    import lib.action.unarchive
    reload(lib.action.unarchive)
    sys.modules['ActionModule'] = lib.action.unarchive.ActionModule
    unittest.installHandler()

    import ansible.modules.files.unarchive
    m_unarchive = ansible.modules.files.unarchive.Unarchive(
        action=None,
        task=None,
        connection=None,
        play_context=None,
        loader=None,
        templar=None,
        shared_loader_obj=None,
    )

# Generated at 2022-06-13 11:00:55.003316
# Unit test for constructor of class ActionModule
def test_ActionModule():
    class ActionModuleTest(ActionModule):
        def _execute_module(self, *args, **kwargs):
            return {'test': args[0]}
    action_module = ActionModuleTest(None, None)
    print(action_module._execute_module('test'))

# Generated at 2022-06-13 11:00:55.363821
# Unit test for constructor of class ActionModule
def test_ActionModule():
    pass

# Generated at 2022-06-13 11:00:56.203203
# Unit test for constructor of class ActionModule
def test_ActionModule():
    mock = ActionModule()
    assert mock is not None

# Generated at 2022-06-13 11:00:57.442417
# Unit test for constructor of class ActionModule
def test_ActionModule():
    m = ActionModule()
    assert m.TRANSFERS_FILES == True

# Generated at 2022-06-13 11:01:03.591176
# Unit test for constructor of class ActionModule
def test_ActionModule():
    ''' test_ActionModule.py: Unit test for ActionModule class '''
    # Create the arguments needed to create an instance of class ActionModule
    module_name = 'unarchive'
    task = dict()
    task_vars = dict()
    play_context = dict()
    action_plugin = dict()
    connection = dict()
    play_context['check_mode'] = False
    play_context['remote_addr'] = 'remote_addr'
    play_context['remote_user'] = 'remote_user'
    play_context['port'] = 123

    # Create an instance of class ActionModule

# Generated at 2022-06-13 11:01:07.364524
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule()
    module._task.args = {"src": "/src", "dest": "/dest", "remote_src": True}
    try:
        ret = module.run(None, {})
    except AnsibleActionFail:
        pass
    assert ret is None

# Generated at 2022-06-13 11:01:20.065111
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    imp_logging = None
    try:
        from logging import getLogger
        imp_logging = 'getLogger'
    except ImportError:
        try:
            from logging import Logger
            imp_logging = 'Logger'
        except ImportError:
            print('Could not import logging.getLogger')
            return None
    if imp_logging is 'getLogger':
        log = getLogger('test_ActionModule_run')
    else:
        log = Logger('test_ActionModule_run')

    log.debug('test_ActionModule_run')

    ###############################################################
    # We need to test the following parameters:
    # 1. src/content -  with/without remote_src
    # 2. dest
    # 3. creates
    # 4. copy/remote_src
