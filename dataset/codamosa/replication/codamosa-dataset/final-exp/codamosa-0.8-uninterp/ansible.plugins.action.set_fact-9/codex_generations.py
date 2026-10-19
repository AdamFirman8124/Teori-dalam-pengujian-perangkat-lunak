

# Generated at 2022-06-13 10:42:25.436553
# Unit test for constructor of class ActionModule
def test_ActionModule(): 
    # NOTE: this test requires ansible.cfg to be present in user's home directory
    # with ansible_managed=Ansible managed
    original_stdout = sys.stdout
    sys.stdout = StringIO()
    sys.stdout.close()
    sys._stdout = StringIO()
    a = ActionModule()
    result = a.run(tmp=None, task_vars=None)
    assert result['ansible_facts'] == {u'moduled_by': u'Ansible managed'}
    sys.stdout = original_stdout

# Generated at 2022-06-13 10:42:32.758142
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.executor import task_result
    from ansible.playbook import task

    init_args = 'test_playbook', 'test_play', 'non-file.yml'
    t = task.Task(*init_args)
    t.set_loader(None)
    t.action = 'set_fact'
    a = ActionModule(t, None)
    args = {
        "A": 5,
        "B": False,
        "C": "Hello",
    }

    a._task.action = "set_fact"
    a._task.args = args
    res = a.run(task_vars=dict())

# Generated at 2022-06-13 10:42:34.313696
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(None, None, None)
    assert(module is not None)

# Generated at 2022-06-13 10:42:41.578899
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import ansible.constants as C
    C.DEFAULT_JINJA2_NATIVE = True

    from ansible.plugins import action_loader
    from ansible.playbook.play_context import PlayContext

    am = action_loader._action_plugins.get('set_fact')
    am = am()
    am._task.args = {'ansible_facts':{'x':'y'}}
    am._shared_loader_obj = action_loader
    am._task.loop = 'item'
    am._task_vars = PlayContext()
    am._templar = am._shared_loader_obj.templar
    am._loader = am._shared_loader_obj.loader
    am.task_vars = {'item': 'item'}

# Generated at 2022-06-13 10:42:44.147442
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(None, None, load_args_from_file=False)
    print("Passed test for constructor of class ActionModule")


# Generated at 2022-06-13 10:42:44.909278
# Unit test for method run of class ActionModule
def test_ActionModule_run():
  # TODO: write test code
  return

# Generated at 2022-06-13 10:42:45.698340
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(dict(), dict())

# Generated at 2022-06-13 10:42:46.578680
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule


# Generated at 2022-06-13 10:42:47.066660
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert True

# Generated at 2022-06-13 10:42:53.218552
# Unit test for constructor of class ActionModule
def test_ActionModule():
    test_cases = (
        dict(
            action_args=dict(cacheable=True),
            expected_args=dict(cacheable=True),
            expected_dict=dict()
        ),
    )

    for test_case in test_cases:
        obj = ActionModule(**test_case.get('action_args'))
        assert obj._task.args == test_case.get('expected_args')
        for key, value in test_case.get('expected_dict').iteritems():
            assert obj.__dict__.get(key) == value

# Generated at 2022-06-13 10:43:06.123982
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.executor.task_queue_manager import TaskQueueManager

    tqm = TaskQueueManager('', [], [{}], None, None, None, None, None, None)
    cur_task = tqm._inventory.get_host('localhost').get_task('setup')
    cur_task._role._task_blocks = {}
    cur_task._role._role_path = '/etc/ansible/test'
    action = ActionModule(None, cur_task, tqm._loader, None, None)
    action.set_runner(tqm)

    action.run()

# Generated at 2022-06-13 10:43:13.515563
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import ansible.module_utils.facts.system.distribution
    import ansible.module_utils.facts.system.pkg_mgr

    actionModule = ansible.module_utils.facts.system.distribution.ActionModule()
    actionModule._task = ansible.module_utils.facts.system.pkg_mgr.ActionModule()
    actionModule._task.args = {"cacheable": False}
    actionModule._task.args = {"a": 1}
    actionModule._task.args = {"a": "b"}
    actionModule._task.args = {"a": "b"}
    actionModule._task.args = {"a": True}
    actionModule._task.args = {"a": "True"}


# Generated at 2022-06-13 10:43:16.139360
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import ansible.utils.template as template
    t = template.Templar()

    result = dict(ansible_facts=dict(foo=1, bar=2))
    am = ActionModule(t, dict(task_vars=dict(), args=dict(foo=1, bar=2)))
    assert result == am.run(task_vars=dict())


# Generated at 2022-06-13 10:43:17.817654
# Unit test for constructor of class ActionModule
def test_ActionModule():
    mod = ActionModule(task={}, connection={}, play_context={}, loader=None, templar=None, shared_loader_obj=None)
    assert mod is not None

# Generated at 2022-06-13 10:43:18.925931
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule({},{})
    assert isinstance(action, ActionModule)

# Generated at 2022-06-13 10:43:25.378870
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.executor.task_result import TaskResult

    task_args = dict(
        name="one",
        value=True,
        cacheable=True,
        name2="two",
        value2=False
    )

    fake_task = dict(
        args=task_args
    )

    action = ActionModule(task=fake_task, connection=dict(), play_context=dict(), loader=None, templar=None)
    res = action.run(tmp=None, task_vars=dict())

    assert isinstance(res, TaskResult)

    assert res._result['ansible_facts'] == dict(
        name="one",
        value=True,
        name2="two",
        value2=False
    )

    assert res._result['_ansible_facts_cacheable']

# Generated at 2022-06-13 10:43:25.779507
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule

# Generated at 2022-06-13 10:43:30.554539
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import sys
    import os
    import json
    import pytest
    import tempfile

    origin_directory = os.getcwd()
    os.chdir(tempfile.gettempdir())

    from ansible.plugins.action.setup import ActionModule

    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.role import Role
    from ansible.playbook.handler import Handler
    from ansible.inventory.group import Group
    from ansible.inventory.host import Host
    from ansible.inventory.inventory import Inventory

    class HostFake(Host):
        def __init__(self, name):
            super(HostFake, self).__init__(name, variable_manager=None)


# Generated at 2022-06-13 10:43:36.025764
# Unit test for constructor of class ActionModule
def test_ActionModule():
    dummy_executor = type('DummyExecutor', (object,), {})
    dummy_executor.__module__ = __name__
    dummy_executor.noop_task = False
    dummy_executor.config = C

    dummy_play_context = type('DummyPlayContext', (object,), {})
    dummy_play_context.__module__ = __name__
    dummy_play_context.noop_task = False
    dummy_play_context.config = C
    dummy_play_context.check_mode = False
    dummy_play_context.accelerate = False
    dummy_play_context.cur_uuid = 'fff'

    dummy_task = type('DummyTask', (object,), {})
    dummy_task.__module__ = __name__

# Generated at 2022-06-13 10:43:48.947162
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_result import TaskResult
    from ansible.executor.task_executor import ActionTaskExecutor
    import ansible.utils.vars
    import ansible.template
    import ansible.inventory
    import ansible.utils.vars

    class MyActionModule(ActionModule):
        def __init__(self, task, connection, play_context, loader, templar, shared_loader_obj):
            super(MyActionModule, self).__init__(task, connection, play_context, loader, templar, shared_loader_obj)

            self._loader = loader
            self._templar = templar


    # For UT, since this module is neither special nor part of a connection plugin,
    # we need to mock

# Generated at 2022-06-13 10:43:57.320168
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(None, None, {})

# Generated at 2022-06-13 10:43:58.088030
# Unit test for constructor of class ActionModule
def test_ActionModule():
    a = ActionModule()

# Generated at 2022-06-13 10:44:10.337577
# Unit test for method run of class ActionModule

# Generated at 2022-06-13 10:44:21.083134
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    a = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    # Test a valid run
    from ansible.template import Templar
    templar = Templar(loader=None, variables={})
    a._templar = templar
    a._task.args = {'a': 'b'}
    assert a.run(tmp=None, task_vars=None) == {'ansible_facts': {'a': 'b'}, '_ansible_facts_cacheable': False, 'changed': False}
    # Test with invalid k=v
    a._task.args = {'a': 'b', 'c': 'd', '1': True}

# Generated at 2022-06-13 10:44:21.798978
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(action_plugin=None)
    assert module is not None

# Generated at 2022-06-13 10:44:32.843992
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import sys
    import os
    sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_text
    from ansible.module_utils.common._collections_compat import Mapping, MutableMapping

    # redefine to_text so we don't have to load module_utils/basic
    to_text = lambda x: x
    # redefine isidentifier so we don't have to load module_utils/basic
    isidentifier = lambda x: x

    class TestTask(object):
        def __init__(self):
            self.args = dict()

    # Test normal conversion


# Generated at 2022-06-13 10:44:37.802042
# Unit test for constructor of class ActionModule
def test_ActionModule():
    result = ActionModule.run(ActionModule,
                              "test_ActionModule",
                              tmp="/tmp",
                              task_vars={'foo': 'bar'})

    assert result is not None
    assert result['failed']
    assert result['msg'] == 'No key/value pairs provided, at least one is required for this action to succeed'

# Generated at 2022-06-13 10:44:45.397807
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    actionModule = ActionModule(
      task=dict(action=dict(module_name='set_fact', module_args=dict(package_state='present', ansible_python_interpreter='/usr/bin/python3'))),
      connection=None,
      play_context=dict(become=False, become_method=None, become_user=None, check_mode=False, diff=False),
      loader=None,
      templar=None,
      shared_loader_obj=None
    )

    # without cacheable key
    tmp = None
    task_vars = dict()
    result = actionModule.run(tmp, task_vars)
    assert result['ansible_facts']['package_state'] == 'present'

    # with cacheable key
    tmp = None

# Generated at 2022-06-13 10:44:57.765974
# Unit test for constructor of class ActionModule
def test_ActionModule():
    class ConstructorTest(object):

        def __init__(self, task):
            self._task = task

    # Test that an empty dict raises AnsibleActionFail...
    try:
        action_module = ActionModule(ConstructorTest({'args': {}}))
        assert False
    except AnsibleActionFail as e:
        assert 'No key/value pairs provided, at least one is required for this action to succeed' in str(e)

    # Test that a non '_' prefixed variable name raises AnsibleActionFail...

# Generated at 2022-06-13 10:44:58.345079
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule

# Generated at 2022-06-13 10:45:24.111024
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Get a method of the class ActionModule
    method = getattr(ActionModule, "run")

    # Get the number of arguments required by the method run
    numArgs = len(method.__code__.co_varnames)

    # Get the class instance
    actionModule = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

    # Create an arguments list
    args = []

    # Create an arguments keyword
    kwargs = {"tmp": None, "task_vars": None}

    # Call the method run of the class ActionModule
    result = method(actionModule, *args, **kwargs)

    assert(result is not None)
    assert(type(result) is dict)



# Generated at 2022-06-13 10:45:30.279591
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    data = {'dest': '/tmp'}
    action = ActionModule(data, dict(action_plugins='/dev/null'))
    args = dict()
    action._task.args = args
    assert not action.run(task_vars=dict())
    args = dict(Foo='Bar')
    action._task.args = args
    assert action.run(task_vars=dict())['ansible_facts'] == args

# Generated at 2022-06-13 10:45:31.480141
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # FIXME: This test needs to be updated to run in non-local mode
    pass

# Generated at 2022-06-13 10:45:45.393162
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils._text import to_bytes
    from ansible.playbook.play import play
    from ansible.playbook.task import Task

    play_context = play.PlayContext()
    loader = None
    templar = None
    shared_loader_obj = None
    task_vars = dict()

    # Test with existing valid facts
    task_to_run = Task()
    task_to_run.action = 'setup'
    am = ActionModule(task_to_run, play_context, loader, templar, shared_loader_obj)

    am.setup(task_vars=task_vars)
    am._task.args['name'] = 'ansible_distribution'
    result_obj = am.run(task_vars=task_vars)
    assert result_obj

# Generated at 2022-06-13 10:45:54.770508
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # create mock objects
    task = DummyTask()
    action = DummyAction()

    # setup test data
    task.args = {
        'key1': 'value1',
        'key2': 'value2',
        'cacheable': True,
    }

    # run test
    action.run(task.args, task.vars)

    # assertion for test result
    assert task.tmp is None
    assert 'ansible_facts' in action.result
    assert action.result['ansible_facts']['key1'] == 'value1'
    assert action.result['ansible_facts']['key2'] == 'value2'
    assert action.result['_ansible_facts_cacheable'] is True

# Class to mock object `module_utils.basic.AnsibleModule`

# Generated at 2022-06-13 10:45:56.883911
# Unit test for constructor of class ActionModule
def test_ActionModule():
    print('Testing action module:')
    # a sample action module
    am = ActionModule()

# Generated at 2022-06-13 10:45:58.196113
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert isinstance(ActionModule(None, None, {}), ActionModule)



# Generated at 2022-06-13 10:46:06.036281
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """
    Test the behaviour of Ansible's _set_fact module
    """

    # create a valid action
    action = ActionModule({u'task_vars': dict()})

    # test for tasks with no arguments
    action._task = dict(args=dict())
    assert action.run()['_ansible_verbose_override'] == False
    assert action.run()['failed'] == True
    assert action.run()['msg'] == 'No key/value pairs provided, at least one is required for this action to succeed'

    # test for tasks with arguments
    arg1 = 'spiderman'
    arg2 = 'peterparker'

    # test for tasks with invalid arguments
    action._task = dict(args=dict(arg1=arg1, arg2=arg2))

# Generated at 2022-06-13 10:46:08.468997
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''
    Test constructor of class ActionModule with empty args parameter.
    '''
    module = ActionModule(dict())
    assert isinstance(module, ActionModule)

# Generated at 2022-06-13 10:46:16.189876
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.utils.vars import combine_vars
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.handler import Handler
    from ansible.playbook.role import Role
    from ansible.playbook.include import Include
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.inventory.group import Group
    from ansible.inventory.host import Host
    from ansible.plugins.loader import add_

# Generated at 2022-06-13 10:46:57.431496
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """
    Test case that verifies the correct behaviour of _run_action_module method of ActionModule class
    """
    # Creating a dummy task.
    new_task = dict(action=dict(module='add_host', args=dict()), async_val=10, delegate_to='tests', poll=15,
                    run_once=False, until=None, retries=5, delay=10, ignore_errors=False)

    action_module = ActionModule(task=new_task, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

    # Given: I create the following arguments for method _run_action_module
    new_task_vars = dict()

    # When: I call run

# Generated at 2022-06-13 10:47:08.862445
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.plugins.action import ActionModule
    from ansible.utils.vars import AnsibleVars
    import sys

    # Arrange
    task_vars = AnsibleVars()
    tmp = None
    module_args = dict()
    module_args['name'] = 'myvar'
    module_args['value'] = 'myvalue'
    module_args['cacheable'] = False
    set_fact = ActionModule(task=dict(action=dict(args=module_args)), connection=dict(module_implementation_preferences='python'), task_vars=task_vars)

    # Act
    result = set_fact.run()

    # Assert
    assert result.get('ansible_facts') is not None

# Generated at 2022-06-13 10:47:19.428102
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task import Task
    from ansible.playbook.role import Role
    from ansible.playbook.block import Block
    from ansible.playbook.play_context import PlayContext

    fake_ds = dict(
        connection='network_cli',
        interpreter='python',
        network_os='junos',
    )
    fake_tqm = None
    fake_loader = None
    fake_play_context = PlayContext()

    t = Task()
    t._role = Role()
    t.block = Block()
    t._role.name = 'test-role'

    fake_ds = dict(
        connection='network_cli',
        interpreter='python',
        network_os='junos',
    )

# Generated at 2022-06-13 10:47:27.896031
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    print("A test for method run of class ActionModule")

    from ansible.playbook.task import Task
    from ansible.vars import VariableManager
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader

    variable_manager = VariableManager()
    loader = DataLoader()
    variable_manager.set_loader(loader)
    templar = Templar(loader=loader, variables=variable_manager)
    module = ActionModule(templar=templar)

    print("Test 1: No key/value pairs provided")
    assert module.run()['failed']

    print("Test 2: Empty key/value pairs provided")
    assert module.run(task_vars={})['failed']

    print("Test 3: Valid key/value pairs provided")

# Generated at 2022-06-13 10:47:29.931401
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """
    This is a unit test for the constructor of class ActionModule.
    """
    action_module = ActionModule()
    assert action_module is not None

# Generated at 2022-06-13 10:47:32.795875
# Unit test for constructor of class ActionModule
def test_ActionModule():
    a = ActionModule(fake_loader, dict(a=1, b=2))
    assert a.loader == fake_loader
    assert a._task.args['a'] == 1
    assert a._task.args['b'] == 2

# Generated at 2022-06-13 10:47:34.507545
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule('setup', 'localhost', {})
    assert isinstance(action_module, ActionModule)

# Generated at 2022-06-13 10:47:47.699854
# Unit test for constructor of class ActionModule
def test_ActionModule():
    mod = ActionModule(
        task=dict(
            action=dict(
                module_name='set_fact',
                module_args=dict(
                    a='a',
                    b='b',
                    c='c',
                    cacheable=True,
                )
            )
        ),
        connection=dict(
            transport='dummy'
        ),
        play_context=dict(
            # We need this to test the trashing of temporary directories.
            remote_user='test',
        ),
        loader=None,
        templar=None,
        shared_loader_obj=None)
    # Returns a dictionary with the module results
    res = mod.run()
    # Assert that the results of the module match the expected results

# Generated at 2022-06-13 10:47:56.754449
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.block import Block
    from ansible.playbook.role import Role

    role = Role()
    role.name = "some_role"
    role.role_path = "/foo/bar"
    role._role_path = "/bar/foo"
    role.task_blocks = [Block([TaskInclude()], role=role)]
    action = ActionModule(role=role)
    assert action.name == "some_role"
    assert action._role_name == "some_role"
    assert action._role is role

# Generated at 2022-06-13 10:47:57.812306
# Unit test for constructor of class ActionModule
def test_ActionModule():
    ActionModule(None, None)

# Generated at 2022-06-13 10:49:17.424573
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ActionModule.run(None, None)

# Generated at 2022-06-13 10:49:18.044250
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert False

# Generated at 2022-06-13 10:49:27.709044
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(
        dict(
            name=dict(type='str', required=True),
            new=dict(type='bool', required=False),
            cacheable=dict(type='bool', required=False)
        )
    )

# Generated at 2022-06-13 10:49:30.065394
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """
    This is a dummy unit test to keep pytest from reporting error for having 0 tests
    in the unit test file of the module.
    """
    pass

# Generated at 2022-06-13 10:49:36.362279
# Unit test for constructor of class ActionModule
def test_ActionModule():
    act_obj = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    result = act_obj.run(tmp='/tmp', task_vars=None)
    result.pop('invocation', None)
    assert result == {'changed': False, 'msg': 'Unable to create any variables with provided arguments'}


# Generated at 2022-06-13 10:49:42.327135
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    class FakeTask():
        def __init__(self, args):
            self.args = args

    class FakeCallbacks():
        def __init__(self, stdout):
            self.stdout = stdout

    class FakeRunner():
        def __init__(self):
            self.callbacks = FakeCallbacks("")
        def run(self, tmp=None, task_vars=None):
            return {}

    am = ActionModule({})
    am.runner = FakeRunner()

    # test success with key and value
    fake_task = FakeTask({'foo': 'bar'})
    am.task = fake_task
    action_result = am.run()
    assert action_result['ansible_facts'] == {'foo': 'bar'}

# Generated at 2022-06-13 10:49:42.920580
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:49:45.452874
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule(None, None, None, None, None, None)
    assert am
    assert am.TRANSFERS_FILES == False

# Generated at 2022-06-13 10:49:50.977242
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    class TaskMock(object):
        def __init__(self, args):
            self.args = args

    task = TaskMock(args = {'my_variable': 'my_value'})
    action = ActionModule(task, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

    result = action.run(tmp='tmp', task_vars={})

    assert result['ansible_facts'] == {'my_variable': 'my_value'}

# Generated at 2022-06-13 10:49:56.078242
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import unittest
    import copy
    import sys, os
    import ansible.constants as C
    import ansible.utils as utils
    import ansible.runner as runner
    import ansible.playbook as playbook
    import ansible.inventory as inventory
    import ansible.callbacks as callbacks
    from ansible.runner_utils import DataLoader
