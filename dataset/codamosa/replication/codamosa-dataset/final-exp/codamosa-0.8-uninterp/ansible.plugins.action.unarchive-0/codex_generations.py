

# Generated at 2022-06-13 10:52:47.174952
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:52:48.412523
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule.__name__ == "ActionModule"
    assert hasattr(ActionModule, "run")

# Generated at 2022-06-13 10:53:00.143141
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """
    Unit test for `ActionModule.run`.
    :return:
    """
    from ansible_collections.ansible.legacy.tests.unit.modules.utils import AnsibleExitJson
    from ansible_collections.ansible.legacy.tests.unit.modules.utils import AnsibleFailJson
    from ansible_collections.ansible.legacy.tests.unit.modules.utils import ModuleTestCase

    # Tested class.
    module = ActionModule

    # Create the test case.
    test_case = ModuleTestCase(module)

    # Create the module.
    test_case.module = module(name=None, kwargs=None, loader=None, templar=None, shared_loader_obj=None)

    # Test the run method.

    # Test the `_execute_remote

# Generated at 2022-06-13 10:53:06.157715
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ActionModule._connection = FakeConnection()
    source = "/home/user/x.y"
    dest = "/home/user"
    a = ActionModule(dict(src=source, dest=dest, remote_src=False, copy = False,
                          decrypt=True), FakeLoader(), FakePlayContext())
    test_result = a.run(FakeTask())
    assert test_result['failed'] is False
    assert test_result['dest'] == dest
    assert test_result['src'] == source
    assert test_result['remote_src'] is False
    assert test_result['copy'] is False
    assert test_result['decrypt'] is True


# Generated at 2022-06-13 10:53:07.036385
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Run the method with an invalid argument.
    assert False

# Generated at 2022-06-13 10:53:12.434211
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Create a ActionModule object
    action_module = ActionModule()

    # Create a test task
    task = dict(
        args = dict(
            src = 'a.zip',
            dest = 'files/unarchived',
            creates = None,
            decrypt = True
        )
    )
    # Test ActionModule.run()
    result = action_module.run(task)
    # Check if returned result is expected
    assert(result['msg'] == 'unarchived')

# Generated at 2022-06-13 10:53:25.721487
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # test with fresh variables.
    a = ActionModule()
    a.set_task_and_variables(task={'args': {'src': 'a/src/path', 'dest': 'a/dest/path', 'creates': 'some/file', 'remote_src': True}},
                             variables={'foo': 'bar'})
    a._transfer_file = lambda src, dest: print("TEST: Transferring from src: %s to dest: %s" % (src, dest))
    a._execute_remote_stat = lambda path, all_vars, follow: {'exists': True, 'isdir': True}
    a._remote_expand_user = lambda path: path
    a._remote_file_exists = lambda path: True
    a._fixup_perms2 = lambda paths: None
   

# Generated at 2022-06-13 10:53:27.122369
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(dict(src=None, dest=None), True)

# Generated at 2022-06-13 10:53:31.317583
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    test_module = AnsibleAction(None, None, None)
    test_module.set_task_vars(None, None)
    result = test_module.run()
    assert result.get('skipped', False) is True
    assert result.get('changed', False) is False

# Generated at 2022-06-13 10:53:36.860567
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from mock import Mock
    from mock import patch

    am = ActionModule()
    am.inject(
        {
            'connection': Mock(),
            'task': Mock(),
            '_task': Mock(),
        }
    )
    with patch('os.path.expanduser') as ope:
        ope.return_value = 'test'
        result = am.run(tmp='test', task_vars='test')
    assert result is not None

# Generated at 2022-06-13 10:53:46.384185
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass


# Generated at 2022-06-13 10:53:47.823164
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule('ActionModule', 'src', 'dest')

# Generated at 2022-06-13 10:53:56.444328
# Unit test for method run of class ActionModule

# Generated at 2022-06-13 10:54:10.924907
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """
    This is a constructor test of ActionModule using the built-in unittest module.

    """
    import unittest
    import mock
    class MyMock(object):
        def __init__(self):
            self.module_name = 'test'
            self.args = {'test': True}
    class MyMockContext(object):
        def __init__(self):
            self.task = MyMock()
    class MockTaskVars(dict):
        def __init__(self, data=None, **kwargs):
            super(MockTaskVars, self).__init__(data or {}, **kwargs)
            self.update(kwargs)
    # Create the object that we are testing
    test_object = ActionModule(MyMockContext())

    # Begin the unittest by testing

# Generated at 2022-06-13 10:54:14.889749
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_mod = ActionModule()
    assert(hasattr(action_mod, '_execute_remote_stat'))
    assert(hasattr(action_mod, '_execute_module'))
    assert(hasattr(action_mod, '_remove_tmp_path'))
    assert(hasattr(action_mod, 'run'))

# Generated at 2022-06-13 10:54:16.922747
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert isinstance(ActionModule, object)


# Generated at 2022-06-13 10:54:18.295289
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Tested in test_action.py.
    pass

# Generated at 2022-06-13 10:54:19.132824
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:54:21.028107
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Create a ActionModule object for testing.
    test_obj = ActionModule()

# Generated at 2022-06-13 10:54:21.837436
# Unit test for method run of class ActionModule
def test_ActionModule_run():   
    pass

# Generated at 2022-06-13 10:54:39.264412
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert True

# Generated at 2022-06-13 10:54:41.421477
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module_args = {'src': '/tmp/foo', 'dest': '/var/log'}
    action = ActionModule(None, module_args)
    assert action is not None

# Generated at 2022-06-13 10:54:51.383037
# Unit test for constructor of class ActionModule

# Generated at 2022-06-13 10:55:01.292105
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.action.unarchive import ActionModule

    # Mock the result for the execute_module method.
    ansible_result = {
        'rc': 0,
        'stdout': '',
        'stderr': '',
        'stdout_lines': []}

    # Mock the run method of the ActionBase class.
    def mock_run(tmp, task_vars):
        return {}

    # Mock the _execute_module method of the ActionBase class.
    def mock_method(module_name, module_args, task_vars):
        return ansible_result

    # Mock the _fixup_perms2 method of the ActionBase class.
    def mock_fixup_perms2(file_paths):
        self._fixup_perms2

    # Mock the _remove_tmp_

# Generated at 2022-06-13 10:55:10.646274
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import os
    import sys
    import unittest
    import shutil

    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_result import TaskResult
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.utils.vars import load_extra_vars
    from ansible.errors import AnsibleError
    from ansible import context
    import ansible.constants as C
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task

# Generated at 2022-06-13 10:55:12.529090
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule(None, None, None)
    assert action.run("tmp", "task_vars")

# Generated at 2022-06-13 10:55:14.980731
# Unit test for constructor of class ActionModule
def test_ActionModule():
    m = ActionModule()
    assert m is not None

if __name__ == '__main__':
    test_ActionModule()

# Generated at 2022-06-13 10:55:15.595375
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert True

# Generated at 2022-06-13 10:55:25.231366
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Set up mocks for testing this function.
    #
    # Source: https://github.com/ansible/ansible/blob/devel/test/units/plugins/actions/test_synchronize.py
    from ansible.plugins.action.synchronize import ActionModule
    from ansible.plugins.connection.ssh import Connection


# Generated at 2022-06-13 10:55:32.152085
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """ Test the run method of class ActionModule """

    tmp_path_expected = "/tmp"
    task_vars_expected = {
        'a': 1,
        'b': 2,
    }


# Generated at 2022-06-13 10:56:08.204000
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """Unit test for constructor of class ActionModule
    """
    assert ActionModule is not None


# Generated at 2022-06-13 10:56:17.297241
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import tempfile
    import shutil
    import json
    import unittest
    import ansible.plugins.action.unarchive as unarchive

    # CCTODO: Create a suitable mock object to use instead of a real task object.
    class Task():
        def __init__(self, args):
            self.args = args

    # CCTODO: Create a suitable mock object to use instead of a real connection.
    class Connection():
        def __init__(self, tmpdir):
            self._shell = ConnectionShell(tmpdir)

        def _remote_expand_user(self, path):
            return self._shell.expanduser(path)

        def _remote_file_exists(self, path):
            return os.path.exists(path)


# Generated at 2022-06-13 10:56:27.950739
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import os
    import mock
    import ansible.plugins.action.unarchive

    # mock the task object
    mock_task = mock.MagicMock()
    mock_task._task = mock.MagicMock()
    mock_task._task.args = dict(src='src', dest='dest', remote_src=False, creates='creates', decrypt='decrypt')
    mock_task._connection = mock.MagicMock()
    mock_task._connection._shell = mock.MagicMock()
    mock_task._connection._shell.join_path = lambda x, y: y

    # test for constructor of class ActionModule
    print("Testing the constructor of class ActionModule")
    action = ansible.plugins.action.unarchive.ActionModule(mock_task, mock.MagicMock)
    assert action is not None

# Unit

# Generated at 2022-06-13 10:56:34.632466
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    params = {
        'dest': '.',
        'src': '/mnt/c/foo.zip',
        'remote_src': True,
    }
    my_am = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

    # CCTODO: Remove test when method is implemented.
    with pytest.raises(NotImplementedError):
        my_am.run(params)

# Generated at 2022-06-13 10:56:35.457028
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(None, None) is not None

# Generated at 2022-06-13 10:56:36.105914
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule

# Generated at 2022-06-13 10:56:36.777553
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ActionModule().run()

# Generated at 2022-06-13 10:56:40.802748
# Unit test for constructor of class ActionModule
def test_ActionModule():
    task = dict(action=dict(module='archive', args=dict(src='archive', dest='/var/lib/test')))
    task_vars = dict(ansible_ssh_user='user')
    tmp = '/tmp'

    action_plugin = ActionModule(task, tmp, task_vars)

# Generated at 2022-06-13 10:56:48.634800
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    am = ActionModule('/tmp/ansible_tmp_dir/', dict(src='/path/to/source', dest='/path/to/dest'), False, None, None)
    assert am.run(dict(ANSIBLE_REMOTE_TMP='/tmp/ansible_pip_dir/')) == {'failed': True, 'msg': "src (or content) and dest are required"}
    am = ActionModule('/tmp/ansible_tmp_dir/', dict(src='/path/to/source', dest='/path/to/dest'), False, None, None)
    task_vars = dict()
    task_vars['ansible_no_log'] = dict()
    task_vars['ansible_no_log']['files'] = dict()

# Generated at 2022-06-13 10:56:49.325477
# Unit test for constructor of class ActionModule
def test_ActionModule():
  am = ActionModule()
  assert am

# Generated at 2022-06-13 10:58:04.597602
# Unit test for method run of class ActionModule

# Generated at 2022-06-13 10:58:09.567075
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(
        {'dest': '/ansible/test', 'src': '/ansible/test/test.zip'},
        connection=None,
        task=None,
        loader=None,
        templar=None,
        shared_loader_obj=None
    )

    assert module is not None
    assert module.run() is not None
    assert module.run({'ansible_check_mode': True}) is not None

# Generated at 2022-06-13 10:58:20.184130
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # We need to make a fake class for these tests.
    module = ActionModule(None, None, None, None)

    # 1st test: when any of the parameters is None.
    # Result: must raise an exception.
    try:
        module = ActionModule(None, None, None, None)
    except ValueError as e:
        assert True, 'ActionModule constructor failed. Caught an exception: {0}'.format(e.message)
    else:
        assert False, 'ActionModule constructor failed. Not caught an exception.'

    # 2nd test: when the parameters are correct.
    # Result: must not raise an exception.

# Generated at 2022-06-13 10:58:30.313538
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''
    Test function for class ActionModule
    '''

    import ansible.plugins.action.unarchive

    # Construct test object

# Generated at 2022-06-13 10:58:31.936262
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule # constrcutor is found

# Generated at 2022-06-13 10:58:44.921026
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils import basic
    from ansible.module_utils.common.process import get_bin_path
    import ansible.plugins.action as action
    import ansible.plugins.action.unarchive as unarchive
    import ansible.module_utils.connection as connection
    import ansible.errors as errors

    class TestModule(basic.AnsibleModule):
        pass

    # Create an instance of the ActionModule class.

# Generated at 2022-06-13 10:58:46.439773
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass


# Generated at 2022-06-13 10:58:53.974454
# Unit test for constructor of class ActionModule
def test_ActionModule():
    yaml = '{"a": "b", "c": "d"}'
    p = ActionModule(yaml, dict(a=1, b=2), dict(), False, '/tmp', False)
    assert p._task.args['a'] == 'b'
    assert p._task.args['c'] == 'd'
    assert p._task_vars['a'] == 1
    assert p._task_vars['b'] == 2
    assert p._connection is None
    assert p._play_context is None
    assert p._loader is None
    assert p._templar is None
    assert p._shared_loader_obj is None
    assert p._action is None
    assert p._shell is None

# Generated at 2022-06-13 10:58:56.145955
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(None, None)
    assert isinstance(module, ActionModule), "Creating ActionModule object failed"

# Generated at 2022-06-13 10:59:07.053164
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action = ActionModule()
    mock_loader = MockLoader()
    tmp = '/a/b/c'
    source = '/source/file'
    dest = 'dest/dir'
    remote_src = False
    creates = 'dest/creates/dir'
    decrypt = True
    ansible_dir = '/a/mock/ansible/dir'
    mock_connection = MockConnection(ansible_dir)
    mock_task = MockTask()
    mock_task.args = {'src': source,
                      'dest': dest,
                      'remote_src': remote_src,
                      'creates': creates,
                      'decrypt': decrypt}


# Generated at 2022-06-13 11:02:15.708176
# Unit test for constructor of class ActionModule
def test_ActionModule():
    global actionModule
    actionModule = ActionModule(connection=None, play_context=dict(), loader=None, templar=None, shared_loader_obj=None)

# Test for run method of class ActionModule

# Generated at 2022-06-13 11:02:23.547219
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action = ActionModule()

    class connection:
        _shell = connection
        tmpdir = '/tmp/taw4'
        def join_path(self, a, b):
            return '{}/{}'.format(a, b)

    class module:
        args = {}

    class play:
        class strategy:
            name = 'mitchellh'

    class task:
        args = {'src': '/tmp/taw4/taw4', 'dest': '/tmp/taw4/taw4'}
        def __init__(self):
            self.action = 'unarchive'
            self.play = play

    action._play_context = connection
    action._connection = connection
    action._task = task
    action._remove_tmp_path = lambda x: None
    action._loader = connection
    action

# Generated at 2022-06-13 11:02:24.603408
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # TODO: write test for this class
    return True

# Generated at 2022-06-13 11:02:26.940398
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(None, None, None)
    # test if the object is an instance of ActionModule
    action_module.run('', '')

# Generated at 2022-06-13 11:02:38.484183
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import ansible.modules.packaging.os
    from ansible.playbook.play_context import PlayContext
    from ansible.executor import task_result
    from ansible.module_utils.facts.system.distribution import Distribution

    result = task_result.TaskResult(host=ansible.modules.packaging.os.Distribution(), task=object())
    play_context = PlayContext()
    unarchive = ansible.plugins.action.ActionModule(
        task=object(), 
        connection=ansible.plugins.connection.Connection(play_context=play_context),
        play_context=play_context,
        loader=ansible.parsing.dataloader.DataLoader(),
        templar=ansible.parsing.templar.Templar(),
        shared_loader_obj=None)
