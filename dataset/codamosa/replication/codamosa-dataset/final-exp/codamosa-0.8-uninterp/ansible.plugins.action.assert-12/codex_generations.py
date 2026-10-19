

# Generated at 2022-06-13 09:34:14.975027
# Unit test for constructor of class ActionModule
def test_ActionModule():
    a = ActionModule(None, None, None, None)

# Generated at 2022-06-13 09:34:19.880688
# Unit test for constructor of class ActionModule
def test_ActionModule():
    host = 'host'

    # Create a task object
    task_args = dict(
        fail_msg='fail_msg',
        msg='message',
        quiet=True,
        success_msg='success_msg',
        that='that'
    )
    task = dict(
        action=dict(module='assert'),
        _ansible_check_mode=True,
        _ansible_no_log=True,
        _ansible_verbosity=2,
        args=task_args
    )

    # Create a play object
    play = dict(
        name='test_play',
        hosts=host,
        gather_facts='yes',
        tasks=[task]
    )

    # Create a play context
    play_context = dict(
        play=play
    )

    # Create a test playbook object


# Generated at 2022-06-13 09:34:24.282638
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    testActionModule = ActionModule(None, None, None)

    assert_result = testActionModule.run(dict(), dict())

    assert assert_result['msg'] == 'All assertions passed'
    assert assert_result['changed'] == False

# Generated at 2022-06-13 09:34:31.728633
# Unit test for method run of class ActionModule
def test_ActionModule_run():
  
    # Setup the test action module
    task = dict(
        name='check',
        action='assert',
        args=dict()
    )

    # Setup the task variables
    task_vars = dict(
        ansible_version = dict(
            major = 2,
            minor = 6,
            revision = 1,
            string = '2.6.1'
        )
    )
    
    # Test with passed assert
    action = ActionModule(task, task_vars=task_vars)
    action.task_vars['that'] = ["ansible_version.major == 2"]
    result = action.run(task_vars=task_vars)

    assert result["assertion"] == "ansible_version.major == 2"
    assert result["evaluated_to"] == True
    assert result

# Generated at 2022-06-13 09:34:40.844010
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule(None, None, None)
    assert action is not None
    assert action._VALID_ARGS == frozenset(('fail_msg', 'msg', 'quiet', 'success_msg', 'that'))
    assert action.TRANSFERS_FILES == False

    # test_boolean_strict_false

# Generated at 2022-06-13 09:34:51.139860
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Test with simple string
    a = ActionModule(name='action_module_1', action='set_fact', args={'fail_msg':'fail_msg_1'}, loader=None, shared_loader_obj=None)
    assert a.name == 'action_module_1'
    assert a._task.action == 'set_fact'
    assert a._task.args['fail_msg'] == 'fail_msg_1'
    assert a._task.accepts_async

    # Test with list
    a = ActionModule(name='action_module_2', action='set_fact', args={'fail_msg':['fail_msg', 'fail_msg_2']}, loader=None, shared_loader_obj=None)
    assert a.name == 'action_module_2'

# Generated at 2022-06-13 09:35:04.850709
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # initialization
    a = ActionModule(None, {})

    # an AssertionError is raised if that is not specified
    try:
        a.run(None, None)
        assert False, 'AnsibleError expected'
    except AnsibleError as e:
        assert str(e) == 'conditional required in "that" string'

    # test for fail_msg is None
    # this is the first condition in the method run of class ActionModule
    try:
        a.run(None, {'that': [['2', '>', '1']]})
        assert False, 'AnsibleError expected'
    except AnsibleError as e:
        assert str(e) == 'Incorrect type for fail_msg or msg, expected a string or list and got <class \'NoneType\'>'

    # test for that is not

# Generated at 2022-06-13 09:35:10.111368
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import copy
    import sys
    sys.modules['_ansible_module_mymodule'] = None

    # testing object construction
    module = ActionModule()

    assert hasattr(module, '_VALID_ARGS'), \
        'ActionModule object is missing attribute "_VALID_ARGS"'
    assert hasattr(module, '_task'), \
        'ActionModule object is missing attribute "_task"'
    assert hasattr(module, '_connection'), \
        'ActionModule object is missing attribute "_connection"'
    assert hasattr(module, '_play_context'), \
        'ActionModule object is missing attribute "_play_context"'



# Generated at 2022-06-13 09:35:13.411824
# Unit test for constructor of class ActionModule
def test_ActionModule():
    ''' action_fail: Test the ActionModule constructor '''
    from ansible.playbook.task import Task
    from ansible.playbook.role import Role
    from ansible.playbook.block import Block
    from ansible.playbook.play import Play

    # Setup the class
    module = None
    action = ActionModule(module, task=Task())

# Generated at 2022-06-13 09:35:13.737129
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert False

# Generated at 2022-06-13 09:35:26.190229
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    p = {"fail_msg": "Failure message"}
    task = {"args": p, "register": "result"}
    e = {"loader": "loader_mock_obj", "templar": "templar_mock_obj"}
    a = ActionModule(task, e)

    p["that"] = ["that_mock_obj_1"]
    p["quiet"] = "false"
    result = a.run()
    assert result["msg"] == "Assertion failed"
    assert result["failed"] is True
    assert result["evaluated_to"] is False
    assert result["assertion"] == "that_mock_obj_1"
    assert result["_ansible_verbose_always"] is True

    p["that"] = ["that_mock_obj_2"]

# Generated at 2022-06-13 09:35:30.424969
# Unit test for constructor of class ActionModule
def test_ActionModule():
	print()
	print("Unit test for constructor of class ActionModule")
	print("-----------------------------------------------")
	action_module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)


# Generated at 2022-06-13 09:35:41.062104
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.plugins.action import ActionModule
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    import ansible.constants as C

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources='localhost,')
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    play_context = PlayContext()
    play_context.network_os = 'ios'

    task = Task()


# Generated at 2022-06-13 09:35:42.026911
# Unit test for constructor of class ActionModule
def test_ActionModule():
    try:
        action = ActionModule()
    except:
        assert False
    assert True

# Generated at 2022-06-13 09:35:50.740961
# Unit test for constructor of class ActionModule
def test_ActionModule():
    class AnsibleModuleMock():

        def __init__(self):
            self.fail_json = dict()

        def fail_json(self, *args, **kwargs):
            print("In fail_json")
            self.fail_json = kwargs

    class AnsibleTaskMock():

        def __init__(self, task_args):
            self.args = task_args

    class AnsiblePlayContextMock():
        def __init__(self):
            self.action = 'assert'
            self.connection = 'local'
            self.network_os = 'default'
            self.remote_addr = 'default'
            self.remote_user = 'default'
            self.port = None
            self.play_uuid = 'default'

# Generated at 2022-06-13 09:35:53.955278
# Unit test for constructor of class ActionModule
def test_ActionModule():
    a1 = ActionModule()
    expected_result = ['fail_msg', 'msg', 'quiet', 'success_msg', 'that']
    assert a1._VALID_ARGS == frozenset(expected_result)

# Generated at 2022-06-13 09:35:54.659181
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass


# Generated at 2022-06-13 09:35:58.876335
# Unit test for constructor of class ActionModule
def test_ActionModule():
    mod = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert mod._task.action == 'assert'
    assert mod._task.action == 'assert'


# Generated at 2022-06-13 09:35:59.580020
# Unit test for constructor of class ActionModule
def test_ActionModule():
    pass

# Generated at 2022-06-13 09:36:01.010909
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert isinstance(ActionModule(None, None, None, None), ActionModule)

# Generated at 2022-06-13 09:36:15.543416
# Unit test for constructor of class ActionModule
def test_ActionModule():
  action = ActionModule()
  assert type(action) == ActionModule

# Generated at 2022-06-13 09:36:22.502144
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.action import ActionBase
    from ansible.playbook.conditional import Conditional
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText

    # Create an instance of ActionBase for testing
    action_base = ActionBase()

    # Create an instance of Conditional for testing
    cond = Conditional()

    # Check if the result is correct when ansible verbose is enabled
    action_base.C.config.verbosity = 10
    result = action_base.run(task_vars={"a": 1, "b": "2", "c": 3})
    assert result["msg"] == "No content found"

    # Check if the result is correct when ansible verbose is disabled
    action_base.C.config.verbosity = 0

# Generated at 2022-06-13 09:36:23.672470
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert ActionModule.run(ActionModule(None, None, None), None, None)

# Generated at 2022-06-13 09:36:34.602680
# Unit test for constructor of class ActionModule
def test_ActionModule():
    success_msg = 'All assertions passed'
    fail_msg = 'Assertion failed'
    msg = 'Assertion failed'
    quiet = False
    that = ['item1 == 1', 'item2 == 1', 'item3 == 1']
    that2 = ['item1 == 1', 'item2 == 2', 'item3 == 1']

    args = dict(that = that, fail_msg = fail_msg, quiet = quiet)
    args2 = dict(that = that2, fail_msg = fail_msg, quiet = quiet)
    action = ActionModule(None, dict(assertion = args))
    action2 = ActionModule(None, dict(assertion = args2))

    assert success_msg == action.run(None, dict(item1 = 1, item2 = 1, item3 = 1))['msg']
    assert fail

# Generated at 2022-06-13 09:36:43.870432
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    task_vars = {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4,
        'e': 5,
        'f': 6,
        'g': None,
        'h': '',
        'i': '0',
        'j': 0,
        'k': 'a',
        'l': 'a',
        'm': 'b',
        'n': ['a', 'b'],
        'o': ['a', 'b'],
        'p': 'a',
        'q': 'a'
    }


# Generated at 2022-06-13 09:36:55.407197
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import sys
    import os
    from ansible.dispatch.dispatcher import TaskDispatcher
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.vars import VariableManager
    from io import StringIO
    from ansible.playbook.play_context import PlayContext
    # Python3 rename raw_input to input
    if sys.version_info[:2] <= (2, 7):
        get_input = 'raw_input'
    else:
        get_input = 'input'

    try:
        input = raw_input
    except NameError:
        input = input

    class VarsModule:
        """Mock AnsibleModule class"""
        def __init__(self, **kwargs):
            self.params = kw

# Generated at 2022-06-13 09:36:59.392472
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule(loader=None, path=None, task=None, shared_loader_obj=None, play_context=None, new_stdin=None)
    assert action is not None

# Generated at 2022-06-13 09:37:00.193980
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 09:37:10.616261
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    
    # test context setup
    module_args = {
        'that': [
            'is_flannel_enabled|success',
            'is_etcd_enabled|success',
            'is_master_node|success',
            'is_master_node|success',
            'is_worker_node|success',
            'is_docker_ready|success',
            ],
        'fail_msg': 'some message'
    }
    task_vars = {
        'is_master_node': True
    }

    fake_loader = 'fake_loader'
    fake_templar = 'fake_templar'
    fake_play_context = 'fake_play_context'

    # test execution

# Generated at 2022-06-13 09:37:12.638045
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule('setup', dict(), persist_files=False)
    assert action_module is not None

# Generated at 2022-06-13 09:37:42.704902
# Unit test for constructor of class ActionModule
def test_ActionModule():
    the_module = 'assert'
    the_task = dict()
    the_task['async'] = 0
    the_task['args'] = dict()
    the_task['args']['that'] = 'error==0'
    the_task['delegate_to'] = 'localhost'
    the_task['failed'] = None
    the_task['failed_when_result'] = None
    the_task['id'] = 1
    the_task['name'] = 'assert first'
    the_task['run_once'] = False
    the_task['tags'] = ['always']
    the_task['when'] = True
    the_task['when_result'] = True
    the_task['action'] = dict()
    the_task['action']['__ansible_module__'] = the_module

    action

# Generated at 2022-06-13 09:37:54.625512
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.task import Task

    class FakeLoader(object):
        def __init__(self):
            pass

        def load_from_file(self, path):
            return []

    class FakeTask(Task):
        def __init__(self):
            self.name = 'fake'
            self.has_loop_control = False

    class FakePlay(object):
        def __init__(self):
            self.name = 'fake'
            self.hostvars = {'localhost': {'ansible_all_ipv4_addresses': ['192.168.0.100', '192.168.0.101']}}

    class FakeCond(object):
        class FakeTemplar(object):
            def __init__(self, variables):
                self.variables = variables


# Generated at 2022-06-13 09:37:56.711554
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """
    Unit test for method run of class ActionModule
    """
    pass

# Generated at 2022-06-13 09:38:09.301734
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import mock
    import unittest
    import re
    import os

    # setting up the mock objects
    class MockTemplar:
        def __init__(self):
            pass

        def template(self, data):
            return data

        def is_template(self,data):
            if isinstance(data, list) or isinstance(data, dict):
                return False
            return True

    class MockConditional:
        def __init__(self):
            pass

        def evaluate_conditional(self, templar, all_vars):
            return True

    class MockTask:
        def __init__(self):
            self.args = {}

    class MockPlayContext:
        pass

    # testing when msg is not provided

# Generated at 2022-06-13 09:38:19.754541
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(
        task={
            'action': 'fail',
            'args': {
                'that': 'item1',
                'fail_msg': 'test_fail_msg',
                'success_msg': 'test_success_msg',
                'quiet': False,
            },
        },
        connection=None,
        play_context=None,
        loader=None,
        templar=None,
        shared_loader_obj=None
    )
    assert isinstance(module, ActionModule)



# Generated at 2022-06-13 09:38:23.278797
# Unit test for constructor of class ActionModule
def test_ActionModule():
    x = ActionModule('setup',{'msg':'hello'},['localhost'])
    assert x._task.args['fail_msg'] == 'hello'

# Generated at 2022-06-13 09:38:34.129182
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Create an instance of the class under test
    assert ActionModule(DummyTask(args={'that': 'foo=="bar"'}), DummyPlayContext(),
            DummyLoader()).run(DummyTask(), DummyTaskVars())['failed']

    assert not ActionModule(DummyTask(args={'that': 'foo=="foo"'}), DummyPlayContext(),
            DummyLoader()).run(DummyTask(), DummyTaskVars())['failed']

    assert ActionModule(DummyTask(args={'that': 'foo in a'}), DummyPlayContext(),
            DummyLoader()).run(DummyTask(), DummyTaskVars())['failed']


# Generated at 2022-06-13 09:38:44.994364
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = get_action_module()

    task_not_quiet = dict(fail_msg="Error!")
    task_quiet = dict(fail_msg="Error!", quiet=True)


# Generated at 2022-06-13 09:38:53.753291
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.plugins.action import ActionBase
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.inventory.manager import InventoryManager

    ActionModule(None, dict(hosts=['127.0.0.1'],
                            vars=dict(test=True),
                            group_vars=dict(test=False),
                            _ansible_no_log=True
                            ),
                 InventoryManager([Host(name='127.0.0.1')],
                                  [Group(name='test')])
                 )

# Generated at 2022-06-13 09:39:08.814573
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.role import Role
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.inventory.manager import Inventorymanager
    from ansible.plugins.loader import action_loader
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.executor.playbook_executor import PlaybookExecutor

    # Create a task and a play
    task = Task()
    play = Play()
    play.hosts = 'local'
    play.tasks = [task]
    # Generate a block
    block = Block()
    block.parent_

# Generated at 2022-06-13 09:40:12.351147
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task import Task
    from ansible.playbook.role import Role
    from ansible.playbook.play import Play
    from ansible.playbook.block import Block
    from ansible.utils import context_objects as co
    from ansible.vars.manager import VariableManager

    task = Task()
    block = Block()
    task._block = block
    play_context = co.PlayContext()
    play_context.network_os = 'default'
    play_context.remote_addr = '192.0.2.1'
    task_vars = dict(foo='bar')
    inventory = dict(
        _meta=dict(
            hostvars=dict(),
        ),
        all=dict(
            hosts=dict(),
        ),
    )

# Generated at 2022-06-13 09:40:23.265854
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''Unit test for ActionModule constructor'''

    loader_mock = 'loader_mock'
    templar_mock = 'templar_mock'
    mock_task = {'args': {'fail_msg': 'value', 'msg': 'value2', 'quiet': True, 'success_msg': 'value3', 'that': 'value4'}}

    test_case_instance_ActionModule = ActionModule(loader=loader_mock, 
    templar=templar_mock, task=mock_task)

    assert test_case_instance_ActionModule._VALID_ARGS == frozenset(('fail_msg', 'msg', 'quiet', 'success_msg', 'that'))
    assert test_case_instance_ActionModule.TRANSFERS_FILES == False
    assert test_

# Generated at 2022-06-13 09:40:38.096507
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # create an object of the class
    obj = globals()['ActionModule']()

    # create an object of the ansible class to pass as self
    loader = 'fake'
    templar = 'fake'
    shared_loader_obj = None
    action_base_obj = ActionBase(loader, templar, shared_loader_obj)
    cond = Conditional(loader='fake')

    # execute the method with required args - 2
    # assert the result
    try:
        results = obj.run(None, None)
    except Exception as e:
        assert (type(e) == AnsibleError)

    # execute the method with required args - 1
    # assert the result

# Generated at 2022-06-13 09:40:43.100208
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Test with no args
    obj = ActionModule()
    assert isinstance(obj, ActionModule)

    # Test with correct args
    # Test with correct args
    obj = ActionModule(action_plugins_path='/foo/bar',
                       task='test_task',
                       connection='test_connection',
                       play_context='test_play_context',
                       loader='test_loader',
                       templar='test_templar',
                       shared_loader_obj='test_shared_loader_obj')
    assert isinstance(obj, ActionModule)

# Generated at 2022-06-13 09:40:57.048747
# Unit test for constructor of class ActionModule
def test_ActionModule():
    a = ActionModule(None, None, None, None, None)
    action_module_class_args = vars(a)

    # Assert that all the class members are initialized
    assert action_module_class_args['_task_vars'] == None
    assert action_module_class_args['_loader'] == None
    assert action_module_class_args['_templar'] == None
    assert action_module_class_args['_shared_loader_obj'] == None
    assert action_module_class_args['_connection'] == None
    assert action_module_class_args['_play_context'] == None
    assert action_module_class_args['_task'] == None
    assert action_module_class_args['_loader_cache'] == None
    assert action_module_class_args['_adapter']

# Generated at 2022-06-13 09:41:04.139698
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Initializing
    am = ActionModule()

    # Failing when that is not a key in task_args
    task_args = {'foo': 'bar'}
    task_vars = {}
    try:
        am.run(task_args=task_args, task_vars=task_vars)
        assert False, "Should have thrown AnsibleError when that not a key in task_args"
    except AnsibleError as e:
        pass

    # Failing when that is not of correct type
    task_args = {'that': {'foo': 'bar'}}
    task_vars = {}

# Generated at 2022-06-13 09:41:17.159290
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    loader = DictDataLoader({})
    templar = Templar(loader=loader, variables={})
    task = Task()
    task.args = {'that': 'foo == bar', 'quiet': False}
    am = ActionModule(task, loader=loader, templar=templar)

    result = am.run(task_vars={'foo': 'bar'})
    assert(result['failed'] == False)
    assert(result['evaluated_to'] == True)
    assert(result['assertion'] == 'foo == bar')
    assert(result['msg'] == 'All assertions passed')

    result = am.run(task_vars={'foo': 'baz'})
    assert(result['failed'] == True)
    assert(result['evaluated_to'] == False)

# Generated at 2022-06-13 09:41:19.762568
# Unit test for constructor of class ActionModule
def test_ActionModule():
    test_action_module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert test_action_module._VALID_ARGS == frozenset(('fail_msg', 'msg', 'quiet', 'success_msg', 'that')) and test_action_module.TRANSFERS_FILES == False

# Generated at 2022-06-13 09:41:20.239675
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 09:41:20.811566
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert(True)