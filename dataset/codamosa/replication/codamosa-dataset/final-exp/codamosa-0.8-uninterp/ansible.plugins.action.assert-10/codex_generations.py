

# Generated at 2022-06-13 09:34:18.863595
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.block import Block
    from ansible.playbook.play import Play
    from ansible.playbook.playbook import Playbook
    from ansible.playbook.role import Role
    from ansible.inventory.group import Group
    from ansible.inventory.host import Host
    from ansible.inventory.inventory import Inventory
    from ansible.vars.manager import VariableManager

    my_host = Host(name='my_host')
    my_host.set_variable('greeting', 'hello')
    my_host.set_variable('other_variable', 'goodbye')
    my_host.set_variable('my_fact', 'my_fact_value')

# Generated at 2022-06-13 09:34:23.596020
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule(loader=None, task=None, connection=None, play_context=None, loader_cache=None, templar=None, shared_loader_obj=None)
    assert module.run()



# Generated at 2022-06-13 09:34:26.946827
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule(action='test_action', task=dict(args=dict()), 
        play_context=dict(become_user='rw', become=False), 
        loader=None, templar=None, shared_loader_obj=None)


# Generated at 2022-06-13 09:34:38.372980
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """
    Test run method of class ActionModule
    """
    # test fail_msg
    fail_msg = "assertion failed"
    module = ActionModule()
    assert fail_msg == module._task.args.get(
        'fail_msg', module._task.args.get('msg'))

    # test success_msg
    success_msg = "All assertions passed"
    module = ActionModule()
    assert success_msg == module._task.args.get('success_msg')

    # test that not in task.args
    with pytest.raises(AnsibleError) as execinfo:
        module = ActionModule()
        module.run()
    assert "conditional required in 'that' string" in str(execinfo.value)

    # test non boolean value for param quiet

# Generated at 2022-06-13 09:34:50.266460
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import copy
    import types
    from six.moves import builtins

    class FakeVarsModule:
        def __init__(self):
            self.LIST = ['test1']

        def dict(self):
            return dict()

    class FakeTemplar:
        def __init__(self):
            self.vars = FakeVarsModule()
            self.template = 'template'

    class FakeLoader:
        def __init__(self):
            pass

        def load_from_file(self, filename, *args, **kwargs):
            return 'load_from_file'

        def path_dwim(self, path):
            return path

    class FakeSelf:
        def __init__(self):
            self.run = types.MethodType(ActionModule.run, self)
            self._loader = Fake

# Generated at 2022-06-13 09:35:04.808309
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = AnsibleModule(argument_spec=dict(
        fail_msg=dict(type='str', default=None),
        msg=dict(type='str', default=None),
        quiet=dict(type='bool', default=False),
        success_msg=dict(type='str', default=None),
        that=dict(required=True, type='list')
    ))

    action_module = ActionModule(module, {})

    # testing success message
    result = action_module.run(task_vars=dict(ansible_hostname='hostname'))
    assert result['msg'] == 'All assertions passed'
    assert '_ansible_verbose_always' not in result

    # testing success message with quiet parameter

# Generated at 2022-06-13 09:35:12.676846
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    #FAIL_MSG = "Assertion failed"
    TASK_VARS = {'A': 0, 'B': True, 'C': {'key': 'value'}, 'D': [3, 2, 1]}
    TEMPLAR = {}
    LOADER = None

    task = {'args': {'that': [
        'C.key == "value"'
    ]}}

    cond = Conditional(loader=LOADER)
    cond.when = [task['args']['that'][0]]

    assert(len(task['args']['that']) == 1)

    assert(cond.evaluate_conditional(templar=TEMPLAR, all_vars=TASK_VARS))

# Generated at 2022-06-13 09:35:22.168878
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(task={'args': {'that': [False, False]}}).run() == {
        'failed': True, 'msg': 'Assertion failed',
        'evaluated_to': False, 'assertion': False,
        '_ansible_no_log': False, '_ansible_verbose_always': True}

    assert ActionModule(task={'args': {'that': [True, False]}}).run() == {
        'failed': True, 'msg': 'Assertion failed',
        'evaluated_to': False, 'assertion': False,
        '_ansible_no_log': False, '_ansible_verbose_always': True}


# Generated at 2022-06-13 09:35:28.184556
# Unit test for constructor of class ActionModule
def test_ActionModule():
    class _ActionModule(object):
        _VALID_ARGS = frozenset(('fail_msg', 'msg', 'quiet', 'success_msg', 'that'))

    _action_module = _ActionModule()
    print('_action_module._VALID_ARGS: ', _action_module._VALID_ARGS)

# Generated at 2022-06-13 09:35:29.307678
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule()
    assert module != None

# Generated at 2022-06-13 09:35:41.423394
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule.ACTION_VERSION == 1.0
    assert not ActionModule.BYPASS_HOST_LOOP
    assert ActionModule.CACHEABLE is True
    assert ActionModule.CONNECTION == 'smart'
    assert not ActionModule.HAS_TEST_DATA
    assert ActionModule.TRANSFERS_FILES is False

    # Just test that _VALID_ARGS can be retrieved without an error
    assert ActionModule._VALID_ARGS

# Generated at 2022-06-13 09:35:43.529499
# Unit test for constructor of class ActionModule
def test_ActionModule():
	action = ActionModule()
	assert isinstance(action, ActionModule) == True

test_ActionModule()

# Generated at 2022-06-13 09:35:55.427429
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import os.path
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.inventory import Inventory
    from ansible.vars.manager import VariableManager
    from ansible.playbook.play_context import PlayContext
    from ansible.module_utils._text import to_bytes
    from ansible.parsing.dataloader import DataLoader
    from ansible.plugins.action import ActionBase
    from io import StringIO
    import pytest

    host = Host(name="myhost")
    group = Group(name="mygroup")
    group.add_host(host)
    inventory = Inventory(loader=None, variable_manager=None, host_list=[host])
    variable_manager = VariableManager(loader=None, inventory=inventory)
    play_context = PlayContext

# Generated at 2022-06-13 09:36:03.151626
# Unit test for constructor of class ActionModule
def test_ActionModule():
    loader = 'loader'
    play_context = 'play_context'
    new_stdin = 'new_stdin'
    task_uuid = 'task_uuid'

    a = ActionModule(loader=loader, play_context=play_context, new_stdin=new_stdin, task_uuid=task_uuid)

    print(a.loader)
    print(a.play_context)
    print(a.new_stdin)
    print(a.task_uuid)

# Generated at 2022-06-13 09:36:03.746202
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert False

# Generated at 2022-06-13 09:36:07.172513
# Unit test for constructor of class ActionModule
def test_ActionModule():
    m = ActionModule()
    assert m._VALID_ARGS == frozenset(('fail_msg', 'msg', 'quiet', 'success_msg', 'that'))


# Generated at 2022-06-13 09:36:15.300092
# Unit test for constructor of class ActionModule
def test_ActionModule():
    sample_task = {
        'action': {
            '__ansible_action__': 'fail',
            '__ansible_arguments__': {
                'fail_msg': 'assertion failed',
            }
        }
    }
    module = ActionModule(sample_task, {})
    assert module._VALID_ARGS == frozenset(('fail_msg', 'msg', 'quiet', 'that'))
    assert module.TRANSFERS_FILES == False
    assert module.DEFAULT_HASH_BEHAVIOUR == 'replace'
    assert module._matched_block == {}
    assert module._matched_host == {}


# Generated at 2022-06-13 09:36:21.564008
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # make sure that method run terminates in case a non iterable type is passed as arg thats
    task_args = {'fail_msg': 'Assertion failed', 'that': '2 > 1'}
    action_module = ActionModule(task_args=task_args)

    try:
        action_module.run()
    except TypeError as err:
        if str(err) == "'>' not supported between instances of 'int' and 'list'":
            assert True
        else:
            assert False
    except:
        assert False

    assert False

# Generated at 2022-06-13 09:36:27.733244
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # This is a pretty useless unit test. I'm only doing it to get some
    # 100% test coverage. The action module will only be tested by the
    # integration tests
    module = ActionModule(
        task=dict(args=dict(that=['foo'])),
        connection=None,
        play_context=None,
    )

    result = module.run(task_vars=dict(foo=True))
    assert result.get('failed') is False
    assert result.get('evaluated_to') is True
    assert result.get('changed') is False

    result = module.run(task_vars=dict(foo=False))
    assert result.get('failed') is True
    assert result.get('evaluated_to') is False
    assert result.get('changed') is False

# Generated at 2022-06-13 09:36:39.265883
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import os
    import sys
    import syslog
    import tempfile
    #import unittest2 as unittest
    import unittest
    class MockTask(object):
        def __init__(self):
            self.args = dict()
            #self.args['msg'] = 'Assertion failed'
            #self.args['that'] = 'ansible_eth0.speed == 10'

    class MockPlayContext(object):
        def __init__(self):
            self.remote_addr = '10.1.1.1'
            self.connection = 'local'
        def connection(self):
            return self.connection

    import ansible.plugins

# Generated at 2022-06-13 09:37:07.496875
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Create a mock TaskExecutor
    class TaskExecutorMock(TaskExecutor):

        def __init__(self, task_action, connection, play_context, loader, templar, shared_loader_obj):
            super(TaskExecutorMock, self).__init__(task_action, connection, play_context, loader, templar, shared_loader_obj)


# Generated at 2022-06-13 09:37:15.203554
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """Test method ActionModule.run()"""
    from .mock import patch, MagicMock, call
    from ansible.errors import AnsibleError
    from ansible.module_utils.six import string_types

    # Patch AnsibleError
    mock_AnsibleError = patch('ansible.errors.AnsibleError', autospec=True)
    mock_AnsibleError_class = mock_AnsibleError.start()
    mock_AnsibleError_class.side_effect = AnsibleError

    # Patch string_types
    mock_string_types = patch('ansible.module_utils.six.string_types', autospec=True)
    mock_string_types_class = mock_string_types.start()

    # Patch AnsibleModule

# Generated at 2022-06-13 09:37:25.589787
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    def run_ActionModule(module_name=None, fail_msg="Assertion failed", success_msg="All assertions passed",
                         quiet=False, that=[True], task_vars = dict(), kwargs = dict()):

        action_mod = ActionModule(name=module_name, task={"name": module_name, "args": {}})

        if "fail_msg" in kwargs:
            action_mod._task.args["fail_msg"] = kwargs["fail_msg"]

        if "success_msg" in kwargs:
            action_mod._task.args["success_msg"] = kwargs["success_msg"]

        if "quiet" in kwargs:
            action_mod._task.args["quiet"] = kwargs["quiet"]


# Generated at 2022-06-13 09:37:27.760198
# Unit test for constructor of class ActionModule
def test_ActionModule():
    actionmodule = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert actionmodule is not None

# Generated at 2022-06-13 09:37:33.042037
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert hasattr(ActionModule, 'TRANSFERS_FILES')
    assert ActionModule._VALID_ARGS == frozenset(('fail_msg', 'msg', 'quiet', 'success_msg', 'that'))

# Generated at 2022-06-13 09:37:46.401808
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    # test run method with valid arguments
    arg1 = tmp1 = task_vars1 = None
    result1 = module.run(tmp1, task_vars1)
    assert result1 is not None
    assert isinstance(result1, dict)
    assert 'failed' in result1
    assert not result1['failed']
    assert 'msg' in result1
    assert result1['msg'] == 'All assertions passed'

    # test run method with empty 'that' argument
    arg2 = tmp2 = task_vars2 = {'that': ()}
    result2 = module.run(tmp2, task_vars2)
    assert result2 is not None


# Generated at 2022-06-13 09:37:51.970283
# Unit test for constructor of class ActionModule
def test_ActionModule():

    #test 1: normal case with all parameters
    am = ActionModule(
        task=MockTask(),
        connection=None,
        play_context=None,
        loader=None,
        templar=None,
        shared_loader_obj=None
    )

    assert am.TRANSFERS_FILES == False



# Generated at 2022-06-13 09:38:06.033019
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    import ansible.constants as C

    class DummyDisplay:
        verbosity = True

        def display(self, msg, color=None, stderr=False, screen_only=False, log_only=False, runner=None):
            pass

    class MockVariableManager:
        def __init__(self):
            pass

        def set_host_variable(self, host, varname, value):
            pass

        def get_vars(self, loader, play, host, task):
            return {}

   

# Generated at 2022-06-13 09:38:12.681253
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task import Task

    constr = lambda: ActionModule(
        task=Task(),
        connection=None,
        play_context=None,
        loader=None,
        templar=None,
        shared_loader_obj=None
    )

    assert constr()
    assert constr()



# Generated at 2022-06-13 09:38:13.527736
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 09:38:56.465419
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """test_ActionModule_run.py

    Test the function `run` of the class `ActionModule`

    :platform: Mac OS X
    :copyright: (c) 2019 by Devintelle Consulting Services Pvt.Ltd.
    :license: Apache 2.0, see LICENSE for more details.
    """
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_result import TaskResult
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task

# Generated at 2022-06-13 09:39:07.449107
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    from ansible.playbook.task import Task
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.playbook_executor import PlaybookExecutor
    import ansible.constants as C

    class AnsibleTask(Task):

        def __init__(self, action):
            self.action = action

    import io
    import sys


# Generated at 2022-06-13 09:39:13.737456
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    import pytest
    from ansible.plugins.action import ActionBase
    from ansible.errors import AnsibleError

    # Test fixture for class ActionModule
    class ActionModule(ActionBase):
        ''' Fail with custom message '''

        TRANSFERS_FILES = False
        _VALID_ARGS = frozenset(('fail_msg', 'msg', 'quiet', 'success_msg', 'that'))

    task_vars = dict(a=1, b=2, c=3)
    test_ActionModule = ActionModule(None, dict(module_name='debug', module_args=dict(msg='hello world')))
    test_ActionModule._templar = FakeTemplar()
    test_ActionModule._templar.available_variables = task_vars

    # Test case: with 'when' condition ==

# Generated at 2022-06-13 09:39:29.090481
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''
    Unit test for constructor of ActionModule class.
    '''
    my_task = dict(name='test', action='assert')
    my_task['args'] = dict(fail_msg='fail_msg', success_msg='success_msg')

    result = dict(failed=False, msg='success_msg')
    fake_loader = dict()
    am = ActionModule(my_task, fake_loader)
    assert result == am.run(None, dict())

    my_task['args'] = dict(fail_msg='fail_msg', success_msg='success_msg', msg='fail_msg')
    result = dict(failed=False, msg='success_msg')
    am = ActionModule(my_task, fake_loader)
    assert result == am.run(None, dict())


# Generated at 2022-06-13 09:39:37.655319
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Test when fail_msg is provided
    action_module = ActionModule({}, {}, {}, {})
    action_module._task = {'args' : {'that':'{{ 1 + 1 == 2 }}', 'msg':'Assertion failed.'},
                           'module_args' : {'fail_msg' : 'Assertion failed.'}}
    task_vars = dict(ansible_ssh_host='host1', ansible_ssh_pass='password')
    result = action_module.run(None, task_vars)
    assert result['changed'] == False, 'Assertion test is pass and should not set changed value to True'
    assert result['failed'] == False, 'Assertion test is pass and should not set failed value to True'

# Generated at 2022-06-13 09:39:44.767697
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Set expected values
    pass

    # Construct the object to test
    action_module = ActionModule(None, None, None, None, None, None, None, None)

    # Try to call method run of ActionModule
    # NotImplementedError should be raised
    try:
        action_module.run()
        assert False
    except NotImplementedError as ex:
        assert True

# Generated at 2022-06-13 09:39:52.312474
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Test with no parameter
    action = ActionModule()
    result = action.run()
    assert not 'task_vars' in result
    assert not 'tmp' in result

    # Test with valid parameters
    action = ActionModule()
    result = action.run(tmp='/tmp', task_vars={'var_1': 'foo', 'var_2': 'bar'})
    assert 'task_vars' in result
    assert 'tmp' in result

    # Test with invalid parameter
    action = ActionModule()
    result = action.run(tmp='/tmp', task_vars=0)
    assert not 'task_vars' in result
    assert not 'tmp' in result

# Generated at 2022-06-13 09:39:55.683933
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    task_vars = {}
    tmp = None
    action = ActionModule(loader=None, task=None, connection=None)
    result = action.run(tmp=tmp, task_vars=task_vars)
    assert result['failed'] is True
    assert isinstance(result['msg'], string_types)


# Generated at 2022-06-13 09:39:57.115897
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Pending - write test case for method run of class ActionModule
    assert False == True


# Generated at 2022-06-13 09:40:08.324945
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # We don't know what this data structure looks like in detail, so we use
    # the build_module method of the ActionBase class to build a data
    # structure that looks a bit like a task object. The method needs a task
    # name, a list of arguments that make up the task, and a data dictionary
    # to pass to the method. We then use the run() method of the action
    # module to get the result of the run().
    import os
    import json
    test_dir = os.path.dirname(__file__)
    test_playbook = os.path.join(test_dir, 'data/playbook.yml')
    with open(test_playbook) as f:
        test_play = f.read()
    test_task = json.loads(test_play)['tasks'][0]


# Generated at 2022-06-13 09:41:16.166915
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Test with missing 'that' in args
    module = ActionModule(loader=None, task=None, connection=None, play_context=None, loader_cache=None, templar=None, shared_loader_obj=None)
    try:
        module.run()
    except AnsibleError as e:
        assert e.message == 'conditional required in "that" string'

    # Test with incorrect type for fail_msg or msg
    from ansible.playbook.task import Task
    task = Task()
    task._role = None
    task._block = None
    task.args = {'fail_msg': 1, 'that': 'failed'}

# Generated at 2022-06-13 09:41:18.075884
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert not ActionModule(None, None, None)._shared_loader_obj

# Generated at 2022-06-13 09:41:21.584970
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Constructor #1
    try:
        am = _ActionModule()
        assert False, 'Expected exception is not raised'
    except Exception as e:
        assert e.args[0] == 'action_plugins should not be instantiated directly'

    # Constructor #2
    am = _ActionModule({})
    assert isinstance(am, _ActionModule)



# Generated at 2022-06-13 09:41:31.492452
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import os
    import sys
    import unittest
    from ansible.playbook.task_include import TaskInclude

    class TestActionModule(unittest.TestCase):
        def setUp(self):
            pass

        def tearDown(self):
            pass

        def test_run(self):
            try:
                os.remove('/tmp/test_ActionModule.log')
            except:
                pass
            fd = os.open('/tmp/test_ActionModule.log', os.O_RDWR|os.O_CREAT)
            self.old_stdout = os.dup(1)
            os.dup2(fd, 1)
            task = TaskInclude()
            task.action = 'test'
            task._role_name = 'test'

# Generated at 2022-06-13 09:41:31.994975
# Unit test for constructor of class ActionModule
def test_ActionModule():
    ActionModule()

# Generated at 2022-06-13 09:41:34.237642
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Arrange
    module = ActionModule("my_path", "my_connection", "my_action_plugin_loader")

    # Assert
    assert module._task.action == "my_path"

# Generated at 2022-06-13 09:41:40.821049
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # some fake data that would show in the _task.args
    args = { 'fail_msg' : 'All assertions failed',
             'success_msg': 'All assertions passed',
             'quiet': 'False',
             'that': ['test_this', 'test_that']
        }
    assert ActionModule(dict(), dict(), args)

    # Test that fail_msg and msg are not both set, fail_msg should take precedence
    args = { 'fail_msg' : 'All assertions failed',
             'msg' : 'This should fail',
             'success_msg': 'All assertions passed',
             'quiet': 'False',
             'that': ['test_this', 'test_that']
        }
    assert ActionModule(dict(), dict(), args)

    # Test if list type of msg/fail_msg and success_msg is passed
   

# Generated at 2022-06-13 09:41:44.812355
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.plugins.loader import  get_all_plugin_loaders
    from ansible.plugins import action_loader
    action_loader.add_directory('./test/test_action_plugins')
    a = ActionModule({}, task_vars={}, loader=get_all_plugin_loaders()[0])
    return a

# Generated at 2022-06-13 09:41:45.805348
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''Unit test for method run of class ActionModule'''
    print('ActionModule: unit test for Method run')
    print('TODO')

# Generated at 2022-06-13 09:41:53.501989
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # test assertions with default message
    module = AnsibleModuleStub({})
    action_mod = ActionModule(module, {}, {})

    try:
        action_mod.run(task_vars={})
        assert False
    except AnsibleError as e:
        assert e.message == 'conditional required in "that" string'

    try:
        action_mod.run(task_vars={'that': [{'==': [10, 10]}]})
        assert False
    except AnsibleError as e:
        assert e.message == 'Incorrect type for fail_msg or msg, expected a string or list and got <class \'NoneType\'>'
