

# Generated at 2022-06-13 09:34:28.323506
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    def get_test_task_vars(var_name='test_var', var_value=True):
        from ansible.plugins.loader import action_loader
        from ansible.vars.manager import VariableManager

        t = DummyTask(name='dummy_test_task', task_action='dummy_action')
        t.args = dict()
        t.action = 'debug'
        t._ansible_module_name = 'setup'

        t.register = MagicMock()

        t.notify = MagicMock()
        task_vars = dict()
        task_vars[var_name] = var_value
        t._variable_manager = VariableManager()
        t._variable_manager.set_nonpersistent_facts(task_vars)


# Generated at 2022-06-13 09:34:32.741183
# Unit test for constructor of class ActionModule
def test_ActionModule():
    mod = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert isinstance(mod._VALID_ARGS, frozenset)
    assert isinstance(mod.TRANSFERS_FILES, bool)

# Generated at 2022-06-13 09:34:37.935774
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(task=dict(), connection=dict(), play_context=dict(), new_stdin=dict())
    assert module.TRANSFERS_FILES is False
    assert module._VALID_ARGS == frozenset(('fail_msg', 'msg', 'quiet', 'success_msg', 'that'))


# Generated at 2022-06-13 09:34:44.090377
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """
    Test the run method of the ActionModule
    """

    # Test the run method with msg passed as string and fail_msg not passed
    def test_ActionModule_run_msg_string_fail_msg_not_passed():
        t = ActionModule()
        t.run(module_args={'msg': 'This is a test message'})
        assert t.result['msg'] == 'This is a test message'

    # Test the run method with msg passed as a list of strings and fail_msg
    # not passed
    def test_ActionModule_run_msg_list_fail_msg_not_passed():
        t = ActionModule()
        t.run(module_args={'msg': ['This is a test message', 'This is another test message']})

# Generated at 2022-06-13 09:34:44.740735
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert True

# Generated at 2022-06-13 09:34:53.326259
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    ###############
    #  Fail msg test
    ###############
    from ansible.playbook.task import Task
    from ansible.vars.manager import VariableManager

    # fail_msg test 1
    task_source = dict(action=dict(module='assert', fail_msg='fail_msg_test1'))
    task = Task.load(task_source, None, None, task_vars=dict())
    action = ActionModule(task, None)
    result = action.run(None, None)
    assert result['failed'], 'ActionModule.run fail_msg test1 - expected fail, got success'

# Generated at 2022-06-13 09:34:54.650246
# Unit test for constructor of class ActionModule
def test_ActionModule():
    ActionModule('Test').run()

# Generated at 2022-06-13 09:34:57.014939
# Unit test for constructor of class ActionModule
def test_ActionModule():
    act = ActionModule()
    print(act)

# Generated at 2022-06-13 09:35:08.480244
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Source file and class for this unit test
    src_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                 '..',
                                 '..',
                                 '..',
                                 'lib',
                                 'ansible',
                                 'playbook',
                                 'action',
                                 'assert.py')
    src_file = SourceFileLoader.load_module(src_file_path)
    # Dummy class name for this unit test
    src_file.ActionModule.__name__ = 'ActionModule'
    assert_obj = ModuleUtils.ArgumentSpec(src_file.ActionModule._VALID_ARGS)
    print('Unit test for method run of class ActionModule')
    print('Test with fail and msg options')
    fail_

# Generated at 2022-06-13 09:35:13.255712
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.block import Block
    from ansible.playbook.role.include import RoleInclude
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.plugins.loader import action_loader
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    import os

    context = PlayContext()
    play_

# Generated at 2022-06-13 09:35:21.630298
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    am = ActionModule(loader=None, variable_manager=None, templar=None)

# Generated at 2022-06-13 09:35:22.110118
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 09:35:34.022213
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import json

    mock_task_args_that_is_list_of_strings = {
        'fail_msg': 'Looks like something went wrong here'
    }
    mock_task_args_that_is_a_string = {
        'fail_msg': 'Looks like something went wrong here'
    }
    mock_task_args_msg_is_a_list_of_strings = {
        'msg': ['One', 'Two', 'Three']
    }
    mock_task_args_msg_is_a_string = {
        'msg': 'Looks like something went wrong here'
    }
    mock_task_args_msg_is_a_list_of_nonstrings = {
        'msg': [1, 2, 3]
    }
    mock_task_args_fail_msg_is_a_

# Generated at 2022-06-13 09:35:44.240003
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.role import Role
    class TestActionModule(ActionModule):
        pass

    module = TestActionModule(task=Task(), connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    module._task = Task()
    module._task.args = {'msg': None, 'that': None}
    module._task.action = 'conditional'
    module._task.args.update(module.clean_args())

    module._task.block = Block(role=Role())

    result = module.run(tmp=None, task_vars={})
    assert result['failed'] == True
    assert result['assertion'] == None

# Generated at 2022-06-13 09:35:48.889326
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule(None,dict(),'localhost','/tmp')
    assert action._VALID_ARGS == frozenset(('fail_msg', 'msg', 'quiet', 'success_msg', 'that'))
    assert action.TRANSFERS_FILES == False


# Generated at 2022-06-13 09:35:54.050438
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule()
    assert(action.TRANSFERS_FILES == False)
    assert(action._VALID_ARGS == frozenset(('fail_msg', 'msg', 'quiet', 'success_msg', 'that')))
    assert(action.__class__.__name__ == "ActionModule")

# Generated at 2022-06-13 09:36:06.275885
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ''' Tests the method run'''
    import os
    import sys
    import unittest

    from ansible.playbook.play_context import PlayContext
    from ansible.utils.display import Display
    from ansible.vars.manager import VariableManager

    class ActionModule_run_TestCase(unittest.TestCase):
        ''' Test the method run for class ActionModule '''

        def runTest(self):
            pass

    from ansible import context
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.playbook.block import Block

    #

# Generated at 2022-06-13 09:36:16.025372
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """ Unit test for method run of class ActionModule. """

    # make sure that invalid types for fail_msg or msg raise an exception
    try:
        m = {'fail_msg': 1}
        am = ActionModule(t=None, a=m, i='test_host', ds='test_ds')
        r = am.run(task_vars=dict())
    except AnsibleError:
        pass

    try:
        m = {'fail_msg': {'test': 'test'}}
        am = ActionModule(t=None, a=m, i='test_host', ds='test_ds')
        r = am.run(task_vars=dict())
    except AnsibleError:
        pass


# Generated at 2022-06-13 09:36:19.716499
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Check it is an instance of the correct class
    actionmodule = ActionModule(task=None, connection=None,
                                play_context=None, loader=None,
                                templar=None, shared_loader_obj=None)
    assert isinstance(actionmodule, ActionModule)

# Generated at 2022-06-13 09:36:22.206274
# Unit test for constructor of class ActionModule
def test_ActionModule():
    a = ActionModule('/tmp/foo', 'somehost', 'someuser', '/some/path/ansible.cfg', '/tmp/some/file', False, 'some_passwd')
    assert a


# Generated at 2022-06-13 09:36:39.513743
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule()
    assert isinstance(action, ActionModule)

# Generated at 2022-06-13 09:36:40.692139
# Unit test for constructor of class ActionModule
def test_ActionModule():
    pass

if __name__ == '__main__':
    test_ActionModule()

# Generated at 2022-06-13 09:36:44.072108
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """
    Test the run method of class ActionModule
    """
    assert 'module_utils.parsing.convert_bool.boolean' in globals()

# Generated at 2022-06-13 09:36:55.496194
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Test variables
    test_vars = dict()
    test_vars['test_quiet_false'] = dict()
    test_vars['test_quiet_false']['that'] = 'fail_msg'
    test_vars['test_quiet_false']['quiet'] = False
    test_vars['test_quiet_false']['success_msg'] = 'All assertions passed'
    test_vars['test_quiet_false']['fail_msg'] = 'Assertion failed'
    test_vars['test_quiet_false']['_ansible_verbose_always'] = True
    test_vars['test_quiet_false']['failed'] = False
    test_vars['test_quiet_false']['evaluated_to'] = False

# Generated at 2022-06-13 09:37:02.114792
# Unit test for constructor of class ActionModule
def test_ActionModule():
    a = ActionModule()
    assert a.ACTION_VERSION == '2.0'
    assert a.SKIP_BYPASS is True
    assert a.action_type is None
    assert a.action_loader is None
    assert a._task is None
    assert a.shared_loader_obj is None
    assert a.DEFAULT_TRANS_UTILS is True

# Generated at 2022-06-13 09:37:03.219751
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = ActionModule()
    assert True == False

# Generated at 2022-06-13 09:37:03.782773
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 09:37:12.374173
# Unit test for constructor of class ActionModule
def test_ActionModule():
    host = 'dummy'
    args = {
        'fail_msg': 'Test',
        'msg': ['Test']
    }
    task = {
        'args': args,
        'delegate_to': 'localhost'
    }
    play = {
        'hosts': host
    }
    try:
        action_module = ActionModule(task=task, connection=None, play_context=play, loader=None, templar=None, shared_loader_obj=None)
    except Exception as e:
        # AssertionError: Incorrect type for fail_msg, expected a string or list and got <class 'bool'>
        assert isinstance(e, AssertionError)
    else:
        # Should have raised Exception
        assert False

# Generated at 2022-06-13 09:37:19.230474
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    actionModule = ActionModule()
    actionModule._task = MagicMock()

    fail_msg = "Assertion failed"
    success_msg = "Success"
    actionModule._task.args = ({
        'msg': fail_msg,
        'success_msg': success_msg,
        'fail_msg': fail_msg
    })

    test_result = actionModule.run()
    assert test_result['msg'] == fail_msg

# Generated at 2022-06-13 09:37:27.651827
# Unit test for constructor of class ActionModule
def test_ActionModule():

    # Create a test fixture
    loader = DictDataLoader({})
    variable_manager = VariableManager()
    variable_manager.extra_vars = {'test_var': 'test_value'}
    variable_manager._unparsed_cache = {"test_host": {'omit': {'omit_this_host'}}}
    variable_manager._vars_cache = {"test_host": {'omit': {'omit_this_host'}}}
    variable_manager._host_vars_plugins = {}

# Generated at 2022-06-13 09:38:07.558693
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task import Task
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.vars import combine_vars
    from ansible.playbook.play import Play

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, sources='localhost,')
    variable_manager.set_inventory(inventory)

    # Add extra vars
    variable_manager._extra_vars = {
        'ansible_connection': 'local',
        'ansible_playbook_python': '/usr/bin/python',
    }
    variable_manager.clear_pattern_cache()


# Generated at 2022-06-13 09:38:22.113178
# Unit test for method run of class ActionModule
def test_ActionModule_run():
  # init
  task = dict()
  task["name"] = "TestRun"
  task["action"] = dict()
  task["action"]["module"] = "assert"
  task["args"] = dict()
  task["args"]["that"] = "isempty(var_b)"
  task["args"]["success_msg"] = "Test Success"
  task["args"]["fail_msg"] = "Test Fail"

  # init
  tmp = None
  task_vars = dict()
  task_vars["var_a"] = "test1"
  task_vars["var_b"] = None

  # run
  action = ActionModule()
  result = action.run(tmp, task_vars)
  print(result)


# Generated at 2022-06-13 09:38:28.626798
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block

    action = dict(module="fail")
    action.update(dict(msg="foo", fail_msg="bar", quiet=True))
    action.update(dict(that=["1==1", "2==2"]))
    task = Task()
    task._role = None
    task.action = action
    block = Block()
    block._parent = task
    my_action = ActionModule(task, block._parent, '/dev/null/foobar', '/dev/null/foobar', loader=None, templar=None)

    my_action._VALID_ARGS = frozenset(('fail_msg', 'msg', 'quiet', 'success_msg', 'that'))


# Generated at 2022-06-13 09:38:38.783939
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """ Unit test for method run of class ActionModule """

    from ansible.playbook.role.include import IncludeRole
    from ansible.playbook.role.task_include import TaskInclude
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.play import Play
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.vars import combine_vars
    from units.mock.loader import DictDataLoader
    from units.mock.path import mock_unfrackpath_noop

    loader = DataLoader()
    variable_manager = VariableManager()
    variable_manager.extra_vars = {'foo': 'bar'}
    fake_loader = D

# Generated at 2022-06-13 09:38:48.224512
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Fixture to feed params required by the module
    module_params = {
        '_ansible_socket': None,
        '_ansible_check_mode': False,
        '_ansible_no_log': False,
        '_ansible_diff': False,
        'ansible_verbosity': 1,
        'ansible_version': '2.7.14',
        'ansible_module_name': 'assert',
        'ansible_module_args': {
            'msg': 'Test the output',
            'that': ['var1 == 1', 'var2 == 1', 'var3 == 1']
        },
        'warnings': []
    }

    # Fixture to feed the task parameters to the module

# Generated at 2022-06-13 09:38:56.394673
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    hostname = 'fake_host'

    class FakeActionModule(ActionModule):
        pass

    class FakePlayContext(object):

        def __init__(self):
            self.answered_prompts = {}
            self.become_passwords = {}

    class FakeTask(object):

        def __init__(self):
            self._role = None
            self._parent = None
            self._block = None
            self._loader = None
            self.action = 'assert'
            self.when = ['always']
            self.args = {'that': ['always']}

    class FakeLoader(object):

        def __init__(self):
            pass

        def get_basedir(self, path):
            return path


# Generated at 2022-06-13 09:38:59.116667
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert isinstance(ActionModule(None, None, None, None, None, None, None), ActionModule)



# Generated at 2022-06-13 09:39:00.005047
# Unit test for constructor of class ActionModule
def test_ActionModule():
    pass

# Generated at 2022-06-13 09:39:12.926730
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # this set of values is what the python file under test uses in
    # function run to build module_args
    tmp = None
    task_vars = dict()
    # the python file under test is getting the current working directory
    # which is where it will find the python file under test.
    # So that is the only 'playbook_dir' we need
    # the python file used by the python file under test has element
    # 'v2_playbook_item' and that is the value for it.
    play_context = dict(
        playbook_dir='/home/travis/build/ansible/ansible/test/functional/targets',
        v2_playbook_item={
            'task': {'when': 'False'}
        }
    )
    # the python file under test checks the type of this parameter and

# Generated at 2022-06-13 09:39:28.228238
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Create a mock object which we can use to test this method of class ActionModule
    mock_ActionModule = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    # Create unit test for method run of class ActionModule
    # If the 'that' argument is not already present in the task's arguments, then raise an AnsibleError
    mock_task_vars_1 = {}
    mock_ActionModule.task.args = {}
    assert mock_ActionModule.run(tmp=None, task_vars=mock_task_vars_1) == {'failed': True, 'evaluated_to': None, 'assertion': None, 'msg': 'conditional required in "that" string'}
    # If the 'fail_msg' argument is not

# Generated at 2022-06-13 09:40:38.157548
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_task_result = {'assertion': '', 'failed': False, 'evaluated_to': False, 'msg': ''}
    action_tmp = ''
    action_task_vars = dict()
    action_module = ActionModule(
        task=dict(args=dict()),
        connection=dict(),
        play_context=dict(),
        loader=dict(),
        templar=dict(),
        shared_loader_obj=None
    )

    # Test with incorrect type of fail_msg and msg
    # Case 1: fail_msg with int
    action_task_result['assertion'] = 'fail_msg with int'
    action_module.task = dict(args=dict(fail_msg=1, that=True))

# Generated at 2022-06-13 09:40:38.745644
# Unit test for constructor of class ActionModule
def test_ActionModule():
    pass

# Generated at 2022-06-13 09:40:45.311506
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # test imports
    import ansible.plugins.action.assertion

    # test variables
    temp_task = dict()
    temp_task['args'] = dict()

    temp_task['args']['that'] = ['{{ one == 2 }}', '{{ two == 3 }}']

    temp_task['args']['fail_msg'] = 'Fail msg'

    temp_task['args']['success_msg'] = 'Success msg'

    temp_task['args']['quiet'] = True

    temp_task_vars = dict()
    temp_task_vars['one'] = 2
    temp_task_vars['two'] = 4


    # test action
    action = ansible.plugins.action.assertion.ActionModule(None, None, None)
    action._task = temp_task


    assert action

# Generated at 2022-06-13 09:40:46.942218
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    result = ActionModule.run(None,None)
    assert True

# Generated at 2022-06-13 09:40:50.436460
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    AnsibleModule = module_class.ActionModule
    assert AnsibleModule.run() == ''

if __name__ == '__main__':
    test_ActionModule_run()

# Generated at 2022-06-13 09:40:50.790849
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True

# Generated at 2022-06-13 09:40:55.668518
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import sys

    import ansible.plugins.action
    from ansible.parsing.vault import VaultLib
    from ansible.plugins.strategy import ActionModule
    am = ansible.plugins.action.ActionModule(None, None, task_vars=dict())
    am.vars = dict()
    am.templar = VaultLib(None, am.vars)
    am.runner = None
    am.task = None
    am.templar._fail_on_undefined = False
    am.templar._available_variables = dict()

    print('Assert test 1.1 (a): Fail when no msg is given but fail_msg is given')
    task_args = {'that': 'some_condition', 'fail_msg': 'Failed because the condition was not met'}
    am.task

# Generated at 2022-06-13 09:41:03.972487
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.facts import Facts
    from ansible.module_utils._text import to_text

    module = AnsibleModule(
        argument_spec = dict(
            fail_msg = dict(default=None, type='str'),
            msg = dict(default=None, type='str'),
            quiet = dict(default=False, type='bool'),
            success_msg = dict(default=None, type='str'),
            that = dict(default=None, type='list')
        ),
    supports_check_mode=True)

    module.run_command = lambda *args, **kwargs: (0, '', '')
    module.exit_json = lambda **kwargs: True
    module.fail_json = lambda **kwargs: True

    module

# Generated at 2022-06-13 09:41:04.753018
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ActionModule.run()

# Generated at 2022-06-13 09:41:17.428056
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # src/ansible/plugins/action/assert.py
    # Executed with:
    # ansible localhost -a 'assert expr=foo == "bar"
    #     fail_msg="Foo and Bar are not equal"'

    # Invalid msg type
    with pytest.raises(AnsibleError) as excinfo:
        class FakeActionModule():
            class FakeLoader():
                def __init__(self):
                    return

            class FakeTask():
                def __init__(self):
                    return

                args = {'msg': 10}

            class FakeTemplar():
                def __init__(self):
                    return

                def template(self, test):
                    return 'ok'

            class FakeConditional():
                def __init__(self):
                    return

                def when(self):
                    return 'ok'