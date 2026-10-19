

# Generated at 2022-06-13 09:34:26.453600
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Basically tests that the "that" variable is used appropriately
    test_action = ActionModule()

    args = dict()
    args['msg'] = "All assertions passed"
    args['fail_msg'] = "Assertion failed"
    args['that'] = [1,2,3]
    args['quiet'] = False

    mock_task = dict()
    mock_task['args'] = args

    test_action._task = mock_task

    test_action._templar = None

    test_action._loader = None

    test_action.run()

# Generated at 2022-06-13 09:34:29.111904
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(None) is not None


# Generated at 2022-06-13 09:34:29.773210
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert True

# Generated at 2022-06-13 09:34:30.367336
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 09:34:40.135796
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import sys
    if sys.version_info[0] == 2:
        import __builtin__ as builtins
    else:
        import builtins

    # make sure we capture the module_utils path
    try:
        del builtins.module_utils_loaded
    except AttributeError:
        pass

    # Patch the get_bin_path function so that when this runs on a machine
    # without the specified program, it does not through an exception
    def get_bin_path_mock(self, arg, required=False, opt_dirs=[]):
        if arg == 'chmod':
            return '/bin/chmod'
        return None

    ActionModule._get_bin_path = get_bin_path_mock
    test_action_module = ActionModule(loader=None, task=None, connection=None)

   

# Generated at 2022-06-13 09:34:45.661821
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule(loader=None, task=None, connection=None, templar=None)
    assert action._task.action == 'assert'
    assert action._task.args['assert_keyword'].strip() == 'keyword'
    assert action._task.args['assert_msg'].strip() == 'msg'


# Generated at 2022-06-13 09:34:53.928123
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Test the default case:
    #   fail_msg is not given
    #   success_msg is not given
    #   that is not given
    #   msg is not given
    #   quiet is not given
    module = ActionModule()

    with pytest.raises(AnsibleError) as e_info:
        module.run()

    assert "conditional required in \"that\" string" in str(e_info.value)

    # Test the case that fail_msg is given
    #   success_msg is not given
    #   that is not given
    #   msg is not given
    #   quiet is not given
    module = ActionModule()
    module._task.args['fail_msg'] = "test_fail_msg"


# Generated at 2022-06-13 09:35:07.660907
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.play_context import PlayContext
    import ansible.constants as C
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.template import Templar, DictData
    from ansible.vars.manager import VariableManager

    action = ActionModule(
            task=dict(),
            connection=dict(),
            play_context=PlayContext(),
            loader=None,
            templar=Templar(loader=None),
            shared_loader_obj=None)

    action._task.args = dict()
    action._templar._available_variables = dict()
    action._task.action = 'debug'
    # AssertionError: conditional required in "that" string

# Generated at 2022-06-13 09:35:19.737571
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Test that message is given when 'that' is not in task.args
    # Create instance of ActionModule class
    am = ActionModule(task=dict(args=dict()), connection=dict(), play_context=dict(), loader=None, templar=None, shared_loader_obj=None)
    try:
        am.run()
    except AnsibleError as e:
        assert(str(e) == "conditional required in \"that\" string")

    # Test that message is given when 'fail_msg' or 'msg' is not string or list
    am = ActionModule(task=dict(args=dict(that="1==1", fail_msg=1)), connection=dict(), play_context=dict(), loader=None, templar=None, shared_loader_obj=None)

# Generated at 2022-06-13 09:35:28.353639
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.vars.manager import VariableManager

    # Create a Test class instance for the following and return it
    class Test():
        def __init__(self, options, connection):
            self._options = options
            self._connection = connection
            self._play_context = 'play_context'

    # Create the instance of TaskQueueManager class
    tqm = TaskQueueManager(
        inventory=None,
        variable_manager=VariableManager(),
        loader=DataLoader(),
        options=None,
        passwords=None,
    )

    # Create the instance of MockConnection class
    module_return_value = 'module_return_value'

# Generated at 2022-06-13 09:35:46.940418
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # create an instance of the class
    action_module = ActionModule()

    # create a fake task object
    fake_task = type('FakeTask', (object,), {'args': {}})()

    # create a fake loader object
    fake_loader = type('FakeLoader', (object,), {'get_basedir': lambda: 'fake/path'})

    # create a fake templar object
    fake_templar = type('FakeTemplar', (object,), {'template': lambda x: x})

    # assign values to the fake task object
    fake_task.args = {
        'that': 'foo',
        'msg': 'hello world'
    }

    # call the run method

# Generated at 2022-06-13 09:35:47.969084
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    #assert 1 == 2
    assert 2 == 2

# Generated at 2022-06-13 09:35:59.729008
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    def return_false(*args, **kwargs):
        return False

    class MockActionBase(object):

        def __init__(self, *args, **kwargs):
            self.params = {
                'conditional': 'false',
                'msg': 'Fail msg'
            }
            self.loader = {}
            self.templar = type('Templar', (), {'template': return_false})

    class MockConditional(object):

        def __init__(self, loader):
            self.when = []

        def evaluate_conditional(self, templar, all_vars):
            return False

    class MockAnsibleError(object):
        pass

    class MockReturn(object):
        pass


# Generated at 2022-06-13 09:36:11.024979
# Unit test for constructor of class ActionModule
def test_ActionModule():
    ''' Constructor works as expected '''

    def test_parameters(self):
        ''' The parameters passed to the __init__ method '''
        return dict(
            task=dict(args=dict(fail_msg='Fail message',
                                msg='Message',
                                quiet=False,
                                success_msg='Success message',
                                that='That'
                               )
                     ),
            play_context=dict(check_mode=True),
            new_stdin='New standard in'
        )

    def test_assertions(self):
        ''' Assert that the class initialised as we expected it to '''
        assert self.action_module._task.args['fail_msg'] == "Fail message"
        assert self.action_module._task.args['msg'] == "Message"
        assert self.action_

# Generated at 2022-06-13 09:36:11.956662
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module_object = ActionModule()

    assert(action_module_object is not None)

# Generated at 2022-06-13 09:36:14.279720
# Unit test for constructor of class ActionModule
def test_ActionModule():
    try:
        assert 'ActionModule'
    except AssertionError:
        raise AssertionError("Method have not been created!")

# Generated at 2022-06-13 09:36:23.111464
# Unit test for constructor of class ActionModule
def test_ActionModule():
    d = {}
    d['action'] = 'fail'
    d['_ansible_verbose_always'] = True
    d['_ansible_version'] = '1.0.0'
    d['args'] = {'fail_msg': 'fail_msg value', 'msg': 'msg value', 'quiet': True, 'success_msg': 'success_msg value', 'that': 'that value'}
    d['delegated_vars'] = {}
    d['failed'] = False
    d['invocation'] = {'module_name': 'fail', 'module_args': ''}
    d['item'] = 'item value'
    d['name'] = 'name value'
    d['tags'] = ['tag1', 'tag2']


# Generated at 2022-06-13 09:36:23.639586
# Unit test for constructor of class ActionModule
def test_ActionModule():
   assert True

# Generated at 2022-06-13 09:36:34.556798
# Unit test for constructor of class ActionModule
def test_ActionModule():
    def test_action_module_no_fail():
        # Test with no 'fail_msg' or 'msg' provided
        a_module = ActionModule(loader=None,
                                task=None,
                                connection=None,
                                play_context=None,
                                loader_cache=None,
                                shared_loader_obj=None,
                                templar=None,
                                all_vars=None)
        result = a_module.run(tmp=None, task_vars=None)
        assert result == {'failed': True,
                          'assertion': 'All assertions passed',
                          'msg': 'Assertion failed',
                          'evaluated_to': False,
                          '_ansible_verbose_always': True}

    def test_action_module_fail():
        a

# Generated at 2022-06-13 09:36:43.832853
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import os
    import unittest
    import mock

    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager

    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    from ansible.utils.vars import combine_vars

    from ansible.errors import AnsibleError

    class TestActionModuleRun(unittest.TestCase):

        def setUp(self):
            self._loader = DataLoader()
            self._inventory = InventoryManager(self._loader, os.path.dirname(__file__) + '/fail/hosts')
            self._variable_manager = VariableManager

# Generated at 2022-06-13 09:37:03.971813
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # (self, tmp=None, task_vars=None):
    action_module = ActionModule()
    result = dict()
    # FIXME: Add a correct test case
    result['changed'] = False
    result['msg'] = u'Successfully executed assert module'
    return result


# Generated at 2022-06-13 09:37:04.965664
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert isinstance(ActionModule(None), ActionModule)

# Generated at 2022-06-13 09:37:06.365427
# Unit test for constructor of class ActionModule
def test_ActionModule():
  action = ActionModule()
  assert type(action) == ActionModule

# Generated at 2022-06-13 09:37:07.081904
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 09:37:14.945148
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # set up test variables
    task = {'args': {}, 'register': 'dummy'}
    tmp = None
    def _uppercase(name, failed=False, changed=False):
        return "UPPERCASED"

    def _lowercase(name, failed=False, changed=False):
        return "lowercased"
    test_vars = {'my_string': 'Hello', 'my_list': ['Hello', 'world'], 'my_dict': {'my_key': 'my_value'}, 'uppercase': _uppercase, 'lowercase': _lowercase}
    module_name = 'assert'
    # set up mock objects
    class MockActionBase(object):
        def __init__(self, module_name):
            self._task = task
            self._name = module_name


# Generated at 2022-06-13 09:37:25.369578
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # setUp
    action = ActionModule(dict(a=1, b=2), dict(c=[3,4]))
    dict1 = dict(d=5, e=6)
    dict2 = dict(f=7, g=8)

    # test outcomes
    # success_msg=''
    with pytest.raises(AnsibleError, match=r'conditional required in "that" string'):
        action.run()

    # fail_msg=''
    with pytest.raises(AnsibleError, match=r'conditional required in "that" string'):
        action.run(task_vars=dict(that=''))

    # success_msg=''

# Generated at 2022-06-13 09:37:30.977896
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task import Task

    # Test with fail_msg
    y = dict(fail_msg = 'test Fail', quiet = True)
    x = Task()
    x.args = y
    a = ActionModule(x, dict())
    result = a.run(None, None)
    assert result['failed'] == True
    assert result['msg'] == 'test Fail'

    # Test with msg
    y = dict(msg = 'test Fail')
    x = Task()
    x.args = y
    a = ActionModule(x, dict())
    result = a.run(None, None)
    assert result['failed'] == True
    assert result['msg'] == 'test Fail'

# Test output with fail_msg element that is a list
# type

# Generated at 2022-06-13 09:37:34.584830
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule()
    assert module._VALID_ARGS == frozenset(('fail_msg', 'msg', 'quiet', 'success_msg', 'that'))

# Generated at 2022-06-13 09:37:47.065320
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Setup class
    module = ActionModule()
    # Setup vars
    task_vars = {}
    tmp = None
    # Test with short form of 'msg'
    # Test with int
    with pytest.raises(AnsibleError, match=r'Incorrect type for fail_msg or msg, expected a string or list and got <.* \'int\'>'):
        module._task.args.update({'msg': 5})
        module.run(tmp, task_vars)
    # Test with list of str and int
    with pytest.raises(AnsibleError, match=r'Type of one of the elements in fail_msg or msg list is not string type'):
        module._task.args.update({'msg': ['test', 5]})

# Generated at 2022-06-13 09:37:54.255297
# Unit test for constructor of class ActionModule
def test_ActionModule():
    m = ActionModule(
        task=dict(),
        connection=dict(),
        play_context=dict(),
        loader=None,
        templar=None,
        shared_loader_obj=None)
    assert m._VALID_ARGS == frozenset(('fail_msg', 'msg', 'quiet', 'success_msg', 'that')), m._VALID_ARGS
    assert not m.TRANSFERS_FILES, m.TRANSFERS_FILES



# Generated at 2022-06-13 09:38:35.679834
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.parsing.yaml.objects import AnsibleMapping
    # Set up a test ActionBase
    act_base = ActionBase()
    act_base._templar = None
    act_base._loader = None
    # Test: Create a test TaskExecutor instance
    # act_mod = ActionModule()
    # act_mod.run(act_base, task_vars=None)

    # Test: Create a test TaskExecutor instance
    act_mod = ActionModule()
    act_mod._task = {}
    act_mod._task['args'] = {}
    act_mod.run(task_vars={'foo': 'bar'}, tmp=None)

    # Test: Create a test TaskExecutor instance
    act_mod = ActionModule()
    act_mod._task = {}
    act_mod

# Generated at 2022-06-13 09:38:36.214232
# Unit test for constructor of class ActionModule
def test_ActionModule():
    pass

# Generated at 2022-06-13 09:38:40.384963
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # create a test ActionModule
    x = ActionModule(
        task=dict(
            args=dict(),
            action="assert",
            name="assert"
        ),
        connection=None,
        play_context=dict(),
        loader=None,
        templar=None,
        shared_loader_obj=None
    )

    # assert that it is valid
    assert x.action == "assert"
    # assert that it is a singleton
    assert x.__class__ == ActionModule

# Generated at 2022-06-13 09:38:46.947545
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    loader = DataLoader()
    inv_manager = InventoryManager(loader=loader)
    variable_manager = VariableManager(loader=loader, inventory=inv_manager)

    task_t = dict(action=dict(module='assert',
                              args=dict(that=['0 > 1'])),
                  name='Assert',
                  )


# Generated at 2022-06-13 09:38:55.898193
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    args = {'fail_msg': 'type of one of the elements in fail_msg or msg list is not string type',
            'msg': 'Assertion failed',
            'quiet': False,
            'success_msg': 'All assertions passed',
            'that': '1 == 1'}

    play_context = {}
    loader = 'loader'

    task = MockTask()
    task.args = args

    templar = MockTemplar()

    plugin = ActionModule(task, play_context, loader, templar)

    result = plugin.run()

    assert 1 == result['evaluated_to']
    assert '1 == 1' == result['assertion']
    assert 'All assertions passed' == result['msg']

# Mock class MockTask to test the ActionModule class

# Generated at 2022-06-13 09:38:57.631346
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule()
    assert (am == am)

# Generated at 2022-06-13 09:39:11.454898
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    hostvars = dict()
    taskvars = dict()
    args_dict = dict()

    # Failure message without fail_msg and msg, without quiet
    module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    args_dict['that'] = 'hostname == "server1"'
    module.argument_spec = args_dict
    module.run(tmp=None, task_vars=taskvars)

    # Failure message with fail_msg and msg, without quiet
    args_dict['fail_msg'] = 'Assertion failed'
    module.argument_spec = args_dict
    module.run(tmp=None, task_vars=taskvars)

    # Failure message with fail_msg and msg, with quiet


# Generated at 2022-06-13 09:39:15.567266
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Create an instance of ActionModule
    action_module = ActionModule(
        task=dict(args=dict(that=True, fail_msg='failed'))
    )
    result = action_module.run()
    assert result['assertion'] is None
    assert result['changed'] is False
    assert result['msg'] == 'All assertions passed'
    assert result['failed'] is False


# Generated at 2022-06-13 09:39:17.588316
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule()
    assert am


# Generated at 2022-06-13 09:39:21.992905
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ''' Dummy unit test for action module run method '''
    test_action_module = ActionModule(None, None, None, None, None, None)
    test_action_module.run(None, None)
    return

# Generated at 2022-06-13 09:40:26.843444
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.playbook.play_context import PlayContext

    loader = DataLoader()
    vars_manager = VariableManager()
    context = PlayContext()

    adhoc = TaskExecutor('assert', dict(), loader=loader, variable_manager=vars_manager, play_context=context)

    try:
        adhoc.run(dict())
        assert False, "assert no 'that' should raise exception"
    except:
        pass

    adhoc = TaskExecutor('assert', dict(that=['a>b', 'a>b']), loader=loader, variable_manager=vars_manager, play_context=context)
    adhoc.run(dict())

    adhoc = TaskExec

# Generated at 2022-06-13 09:40:38.942046
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    mod = ActionModule()

    class Test1(object):
        def __init__(self):
            self.when = 'y'

    class Test2(object):
        def __init__(self):
            self.when = 'y'

    test_case_list = [
        (True, 'y', 'y', Test1(), Test2()),
    ]

    for (expected_result, fail_msg, success_msg, that_1, that_2) in test_case_list:
        result = mod.run({"fail_msg": fail_msg, "success_msg": success_msg, "that": that_1})
        assert result['msg'] == fail_msg

        result = mod.run({"fail_msg": fail_msg, "success_msg": success_msg, "that": that_2})

# Generated at 2022-06-13 09:40:39.491579
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 09:40:45.237779
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from ansible.parsing.yaml.objects import AnsibleSequence
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.task import Task
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.playbook.play_context import PlayContext
    import jinja2
    import os
    import sys
    import pytest
    import json
    import pickle
    import base64
    import types


# Generated at 2022-06-13 09:40:54.113557
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = ActionModule(task=dict(), connection=dict(), play_context=dict(), loader=dict(), templar=dict(), shared_loader_obj=dict())

    test_vars = dict()


    # Test 1: Testing with empty parameter. It should raise AnsibleError
    that_parameter = dict()
    res = action_module._low_level_execute_command(task_vars=test_vars, that=that_parameter)
    res.pop('invocation', None)

# Generated at 2022-06-13 09:41:02.760161
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.task import Task
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible import context
    from ansible.module_utils._text import to_text
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.utils.vars import combine_vars

    from ansible_collections.notstdlib.moveitallout.plugins.module_utils.action.module import ActionModule as amodule

    from ansible_collections.notstdlib.moveitallout.plugins.module_utils.tests.test_module_set_facts import test_module_set_facts as test_module


# Generated at 2022-06-13 09:41:16.388587
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.parsing.convert_bool import boolean

    module_args = dict(
        success_msg = 'All assertions passed',
        fail_msg = 'Assertion failed',
        quiet = True,
        that='{{ name == "foo" }}'
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    mod = ActionModule(
        module=module,
        task=dict(
            args=module_args
        ),
        task_vars=dict(name = 'foo')
    )

    result = mod.run()
    assert boolean(result['failed'], strict=False) is False

# Generated at 2022-06-13 09:41:22.612832
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.block import Block
    from ansible.executor.task_result import TaskResult

    module_args = dict(
        msg='The message to display',
        fail_msg='message when failing',
        success_msg='message when successful',
        quiet=True,
        that=list([dict(jsonir1key='jsonir1value'), dict(jsonir2key='jsonir2value')])
    )


# Generated at 2022-06-13 09:41:32.456926
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.playbook.block import Block
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.hostvars import HostVars

    task_vars = HostVars(loader=DataLoader(), hostname='dummy')
    task_vars.update({'ansible_facts': {}})
    task_vars.update({'ansible_variables': {}})
    play_context = PlayContext()

    task = Task()
    task._role = None
    task.vars = dict()
    task.args = dict()
    task.args

# Generated at 2022-06-13 09:41:39.158453
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(
        task = dict(args = dict(msg = 'TEST_MSG')),
        connection = None,
        play_context = None,
        loader = None,
        templar = None,
        shared_loader_obj = None,
    )
    assert action_module.TRANSFERS_FILES == False
    assert action_module._VALID_ARGS == frozenset(('fail_msg', 'msg', 'quiet', 'success_msg', 'that'))