

# Generated at 2022-06-13 09:34:15.785855
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass



# Generated at 2022-06-13 09:34:16.754463
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert True

# Generated at 2022-06-13 09:34:27.977152
# Unit test for method run of class ActionModule

# Generated at 2022-06-13 09:34:32.308947
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.utils.pytest_runner import run_module_as_unit_test

    module_args = dict(
        that='{{ foo == bar }}',
        fail_msg='{{ foo }} and {{ bar }} are not equal',
        msg='{{ foo }} and {{ bar }} are equal',
    )

    results = run_module_as_unit_test('assert', **module_args)
    assert not results.get('failed', False)

    results = run_module_as_unit_test('assert', **dict(module_args, foo='apple', bar='orange'))
    assert results.get('failed', False)
    assert results.get('msg') == 'apple and orange are not equal'

    results = run_module_as_unit_test('assert', **dict(module_args, foo='apple', bar='apple'))

# Generated at 2022-06-13 09:34:41.248453
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.six import StringIO
    from ansible.parsing.yaml.objects import AnsibleSequence
    from ansible.plugins.action import ActionBase
    from ansible.playbook.conditional import Conditional
    from ansible.playbook.task import Task
    from ansible.template import Templar
    from ansible.utils.vars import merge_hash
    from ansible.vars.manager import VariableManager
    import yaml

    class TestActionModule(ActionModule):
        def _execute_module(self, tmp=None, task_vars=None):
            assert task_vars is not None
            assert tmp is not None

# Generated at 2022-06-13 09:34:42.446524
# Unit test for constructor of class ActionModule
def test_ActionModule():
    pass

# Generated at 2022-06-13 09:34:47.246793
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook import Play
    from ansible.playbook.play import PlayContext
    from ansible.playbook.task import Task
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    # Create dummy variables
    fake_loader = DummyLoader()
    fake_inventory = InventoryManager(loader=fake_loader, sources='localhost,')
    variable_manager = VariableManager(loader=fake_loader, inventory=fake_inventory)

    # Create fake play context
    play_context = PlayContext()
    play_context._queue_control_from_worker = None

    # Create fake play

# Generated at 2022-06-13 09:34:59.227423
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ''' Unit test for method run of class ActionModule'''

    # Create a temporary directory to use as a stub
    tmpdir = tempfile.mkdtemp()
    # Create a simple ansible task to test method fail of class ActionModule
    playbook_path = os.path.join(tmpdir, 'test_ActionModule_run.yml')
    with open(playbook_path, 'wb') as f:
        f.write(b'''---
- hosts: localhost
  gather_facts: false
  tasks:
  - name: test conditional
    fail:
      msg: "condition is false"
    when: false


''')
    # Create the TaskExecutor that will be used to execute the task
    task_vars = dict()
    loader = DataLoader()

# Generated at 2022-06-13 09:35:09.228128
# Unit test for constructor of class ActionModule
def test_ActionModule():
    ''' fail: fail_msg=I\'m a teapot '''
    task_vars = dict()

    result = ActionModule._execute_module(dict(fail_msg='I\'m a teapot'), task_vars=task_vars)
    assert result.get('msg') == 'I\'m a teapot'
    assert result.get('changed') is False

    result = ActionModule._execute_module(dict(fail_msg=['foo','bar','baz']), task_vars=task_vars)
    assert result.get('msg') == ['foo','bar','baz']
    assert result.get('changed') is False

    result = ActionModule._execute_module(dict(fail_msg=['foo',None,'baz']), task_vars=task_vars)
    assert 'foo'

# Generated at 2022-06-13 09:35:15.665612
# Unit test for method run of class ActionModule

# Generated at 2022-06-13 09:35:31.646763
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    from ansible.module_utils._text import to_text
    from ansible.utils.display import Display
    from ansible.parsing.dataloader import DataLoader

    display = Display()
    loader = DataLoader()

    # Initialize required objects
    task = AnsibleTask()

    # Initialize required variables
    task_vars = dict()

    # Defined varable settings
    task_vars['ansible_verbosity'] = 3

    # Instantiating class object
    am = ActionModule(task, loader, display, task_vars)

# Generated at 2022-06-13 09:35:34.507659
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(task=object(), connection=object(), play_context=object(), loader=object(), templar=object(), shared_loader_obj=object())
    assert(action_module is not None)

# Generated at 2022-06-13 09:35:44.702064
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = None
    result = {}
    tmp = None
    task_vars = {'test': 'test'}

    # If there is no fail_msg in the ansible_args, display a default msg
    ansible_args = {'that':['test']}
    action_module = ActionModule(module, tmp, task_vars=task_vars, **ansible_args)
    res = action_module.run(module=module, tmp=tmp, task_vars=task_vars)
    assert res['msg'] == 'Assertion failed'

    # If there is a fail_msg in the ansible_args, display this msg
    ansible_args = {'that':['test'], 'fail_msg':'fail msg'}

# Generated at 2022-06-13 09:35:47.970139
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert action

# Generated at 2022-06-13 09:35:52.195280
# Unit test for constructor of class ActionModule
def test_ActionModule():
    ans = ActionModule(None, None, None, {})
    assert ans._VALID_ARGS == frozenset(('fail_msg', 'msg', 'quiet', 'success_msg', 'that'))
    assert not ans.TRANSFERS_FILES

# Generated at 2022-06-13 09:35:52.874343
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule

# Generated at 2022-06-13 09:35:53.542231
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 09:36:05.244493
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Test when fail_msg is provided and it is a string
    action_module = ActionModule()
    action_module._task = mock_task = MockTask()
    mock_task.args = {'that': ['{{ var1 == var2 }}', '{{ var1 == var3 }}'], 'fail_msg': 'Failed message'}
    mock_task_vars = {'var1': 1, 'var2': 1, 'var3': '3'}
    assert action_module.run(task_vars=mock_task_vars) == {'evaluated_to': False, 'assertion': '{{ var1 == var3 }}', 'failed': True, 'msg': 'Failed message'}

    # Test when fail_msg is provided and it is a list
    action_module = ActionModule()
    action_module._

# Generated at 2022-06-13 09:36:09.187994
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # pass
    action = ActionModule()
    if action is None:
        print("Failed")
    else:
        print("Test action module passed")

if __name__ == '__main__':
    test_ActionModule()

# Generated at 2022-06-13 09:36:09.810845
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 09:36:35.467486
# Unit test for constructor of class ActionModule
def test_ActionModule():
    mock_task = {}
    mock_task['action'] = 'debug'
    mock_task['version_added'] = '2.0'
    mock_task['args'] = {}
    mock_task['args']['that'] = ['groups.foo | length > 3', 'groups.bar | length > 3']
    mock_task['args']['msg'] = ['foo error message', 'bar error message']

    print("Test ActionModule class")
    
    result = ActionModule(task=mock_task).run(tmp=None, task_vars=None)
    assert len(result['msg']) == len(mock_task['args']['that'])

# Generated at 2022-06-13 09:36:44.489988
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext
    from ansible.utils.sentinel import Sentinel
    from ansible.vars.manager import VariableManager

    test_task = Task()
    test_task_vars = dict()

    play_context = PlayContext()
    variable_manager = VariableManager()

    am = ActionModule(
        task=test_task,
        connection=None,
        play_context=play_context,
        loader=None,
        templar=None,
        shared_loader_obj=None
    )

    assert am is not None
    if am is not None:
        assert am._task == test_task
        assert am._connection == None
        assert am._play_context == play_context
        assert am._loader == None


# Generated at 2022-06-13 09:36:55.564459
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # This test checks the return of a string based conditional
    # The unit test is using a mocked self._task.args.
    # It also mocks Conditional and self._loader.
    import ansible.plugins.action as action

    class MockedConditional():
        # This class mocks the Conditional class
        def __init__(self, loader):
            self.when = None
            self.loader = loader

        def evaluate_conditional(self, templar, all_vars):
            # This function mocks the evaluate_conditional function
            return self.when

    class MockedLoader():
        # This class mocks the loader class
        def get_basedir(self, *args, **kwargs):
            return '/foo/bar'


# Generated at 2022-06-13 09:37:07.907388
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.task import Task
    from ansible.playbook.play import Play
    from ansible.playbook import Playbook
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    results_callback = lambda self: None
    inventory = PlaybookExecutor(loader=loader, inventory=None, variable_manager=None, loader_cache=False, results_callback=results_callback).inventory

    task = Task()
    task.action = 'assert'
    task.args = {'that': ['var1 == var2', 'var3 == 1'], 'fail_msg': 'Something failed'}
    play = Play().load

# Generated at 2022-06-13 09:37:08.843564
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule is not None

# Generated at 2022-06-13 09:37:09.445018
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 09:37:09.966267
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 09:37:14.299988
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule(task=None, connection=None,
            play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert isinstance(action, ActionModule)


# Generated at 2022-06-13 09:37:18.866832
# Unit test for constructor of class ActionModule
def test_ActionModule():
    mock = {
            '_task': {
                'args': {
                    'fail_msg': 'This is a failure',
                    'msg': 'This is a message',
                    'quiet': False,
                    'success_msg': 'You are a success',
                    'that': ['These is a that'],
                }
            }
        }
    mock['_task']['action'] = 'assert'
    test = ActionModule(**mock)
    assert test is not None

# Generated at 2022-06-13 09:37:27.431996
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action = ActionModule()
    action._task.args = dict()
    action._task.args['that'] = dict()
    action._task.args['fail_msg'] = "Test message"
    result = action.run()
    assert result['failed'] == True
    assert result['assertion'] == dict()
    assert result['evaluated_to'] == False
    assert result['msg'] == 'Test message'
    action._task.args['fail_msg'] = ["Test message"]
    result = action.run()
    assert result['failed'] == True
    assert result['assertion'] == dict()
    assert result['evaluated_to'] == False
    assert result['msg'] == 'Test message'
    action._task.args['fail_msg'] = "Test message"

# Generated at 2022-06-13 09:38:00.957040
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = ActionModule()


    # Unit test for functionality of `run` method
    # If fail_msg is not specified then msg should be returned as default 'Assertion failed'
    #
    # Input data:
    #       fail_msg: None
    #       that: test that
    #
    # Expected results:
    #       failed: True
    #       evaluated_to: False
    #       assertion: test that
    #       msg: Assertion failed
    @patch('ansible.plugins.action.assert.Conditional')
    @patch('ansible.plugins.action.assert.ActionBase.run')
    def test_ActionModule_run_case_1(self, mock_ActionBase_run, mock_Conditional):
        action_module = ActionModule()

        load_data = dict()
        load_

# Generated at 2022-06-13 09:38:09.307573
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    name = "test_ActionModule_run"
    action = ActionModule(task=dict(), connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    action._task.args = {'that': '{{ false }}'}
    result = action.run(tmp=None, task_vars=None)
    assert result['failed'] == True
    assert result['assertion'] == '{{ false }}'

    action._task.args['fail_msg'] = '{{ false }}'
    result = action.run(tmp=None, task_vars=None)
    assert result['failed'] == True
    assert result['assertion'] == '{{ false }}'
    assert result['msg'] == '{{ false }}'

    action._task.args['fail_msg'] = 'false'

# Generated at 2022-06-13 09:38:17.183390
# Unit test for constructor of class ActionModule
def test_ActionModule():

    class dummy_loader:
        ''' Dummy class for class TestActionModule '''
        def __init__(self):
            self.vars_loader = 'test1'

    class dummy_templar:
        ''' Dummy class for class TestActionModule '''
        def __init__(self):
            self.vars_templar = 'test2'

    class dummy_task:
        ''' Dummy class for class TestActionModule '''
        def __init__(self):
            self.args = {'that': ['foo'], 'msg': 'failed'}

    class dummy_play_context:
        ''' Dummy class for class TestActionModule '''
        def __init__(self):
            self.become_method = 'sudo'

    dl = dummy_loader()
    dt = dummy

# Generated at 2022-06-13 09:38:27.056966
# Unit test for constructor of class ActionModule
def test_ActionModule():
    ''' Unit test for the constructor of class ActionModule '''
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.template import Templar

    module = ActionModule()
    assert module._VALID_ARGS == frozenset(("quiet", "fail_msg", "msg", "success_msg", "that"))

    # Make sure that module.run() raises exception if fail_msg is not a string or a list
    module = ActionModule()
    module._task.args = {'fail_msg': 3, 'that': '1==1'}
    module._loader = None
    module._templar = Templar(loader=module._loader, variables=dict())
    module._task.action = 'fail'
    module._task.action = 'fail'
    module._task.args

# Generated at 2022-06-13 09:38:38.162099
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.module_utils.six import PY3
    if not PY3:
        from ansible.module_utils.six import iteritems
    else:
        from ansible.module_utils.six import items

    action = ActionModule()

    assert action._VALID_ARGS == frozenset(('fail_msg', 'msg', 'quiet', 'success_msg', 'that'))
    assert action.TRANSFERS_FILES == False
    assert "fails" in action.BYPASS_HOST_LOOP
    assert "msg" in action.BYPASS_HOST_LOOP
    assert "quiet" in action.BYPASS_HOST_LOOP
    assert "success_msg" in action.BYPASS_HOST_LOOP
    assert "that" in action.BYPASS_HOST_LOOP

   

# Generated at 2022-06-13 09:38:47.913660
# Unit test for constructor of class ActionModule
def test_ActionModule():

    loader = 'loader'
    templar = 'templar'
    shared_loader_obj = 'shared_loader_obj'

    class_ = ActionModule(loader=loader,templar=templar, shared_loader_obj=shared_loader_obj)

    assert class_._loader == loader
    assert class_._templar == templar
    assert class_._shared_loader_obj == shared_loader_obj
    assert class_._task_vars == dict()
    assert class_._task.action == 'fail'
    assert class_._task.args == dict()
    assert class_._task.delegate_to == None
    assert class_._task.loop is None
    assert class_._task.notify is None
    assert class_._task.run_once == False

# Generated at 2022-06-13 09:38:51.297983
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert action_module is not None

# Generated at 2022-06-13 09:38:57.504745
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import unittest

    # Unit test for method run of class ActionModule
    class test_ActionModule_run(unittest.TestCase):

        def _mock_ActionBase(self):
            return ActionBase(task=self._mock_task(), connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

        class _mock_task:
            args = dict()

        def _mock_task(self):
            return self._mock_task()

        def test_ActionModule_run_success_msg_is_expected_string(self):
            result = dict()
            result['failed'] = False
            result['changed'] = False

# Generated at 2022-06-13 09:39:11.397383
# Unit test for constructor of class ActionModule
def test_ActionModule():
    class FakeActionModule(ActionModule):
        def __init__(self, *args, **kwargs):
            self.task = args[0]
            super(FakeActionModule, self).__init__(*args, **kwargs)

    action = FakeActionModule({'args': {'fail_msg': 'This is fail message', 'success_msg': 'This is success message', 'that': 'this is a test string'}})
    result = action.run()
    assert(result['msg'] == 'This is fail message')
    assert(result['evaluated_to'] is False)
    assert(result['assertion'] == 'this is a test string')
    assert(result['changed'] is False)
    assert(result['failed'] is True)


# Generated at 2022-06-13 09:39:20.566702
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Test for whether custom message is applied correctly 
    # when the assertion fails
    class FakeTask(object):
        def __init__(self, args_dict):
            self.args = args_dict
    class FakeTemplar(object):
        def __init__(self, template):
            self.template = template
        def template(self):
            return self.template
    class FakeLoader(object):
        pass
    class FakePlayContext(object):
        pass
    class FakePlay(object):
        def __init__(self, play_context):
            self.play_context = play_context
    class FakeRole(object):
        def __init__(self, tasks):
            self.tasks = tasks
        def get_tasks(self):
            return self.tasks


# Generated at 2022-06-13 09:40:20.434253
# Unit test for constructor of class ActionModule
def test_ActionModule():
    test = dict(
        fail_msg = 'Assertion failed',
        success_msg = 'All assertions passed',
        that = ["{{ansible_facts['os_family']}} == 'RedHat' or {{ansible_facts['os_family']}} == 'Debian'"],
        quiet = True
    )

    # test object constructor
    am = ActionModule(task=dict(action='assert', args=test), connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    # test object attributes
    assert am.task == dict(action='assert', args=test)
    assert am.connection == None
    assert am.play_context == None
    assert am.loader == None
    assert am.templar == None
    assert am.shared_loader_obj == None

# Generated at 2022-06-13 09:40:27.245628
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    FAIL_MSG = "Assertion failed"
    SUCCESS_MSG = "All assertions passed"
    THATS = [
        'foo is defined',
        "bar is not none"
    ]
    TASK_VARS = {
        'foo': 'foo',
        'bar': 'bar'
    }

    action_mod = ActionModule()

    # Simple test to see if run returns a valid result
    res = action_mod.run(None, None)
    assert res['failed'] == False

    # Now a simple test to see if a failed assertion throws the right exception
    action_mod = ActionModule()
    res = action_mod.run(None, None)
    assert res['failed'] == False

    # Test all asserts pass
    action_mod = ActionModule()
    action_mod.set_loader

# Generated at 2022-06-13 09:40:39.120533
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.six import string_types
    from ansible.module_utils.six import PY3

    import json

    if PY3:
        unicode = str

        def to_native(x):
            return to_bytes(x)

        def assert_equal(x, y):
            assert x == y
    else:
        to_native = to_bytes

        def assert_equal(x, y):
            assert x == y, "%r != %r" % (x, y)

    # Create a mock templar for evaluating conditionals
    from ansible.template import Templar
    templar = Templar(loader=None, variables={})

    # Create a mock module loader for loading modules

# Generated at 2022-06-13 09:40:45.140913
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    class MockTask(object):
        def __init__(self):
            self.args = {'that':'that','fail_msg': 'fail_msg','msg': 'msg','quiet': 'quiet','success_msg': 'success_msg'}
    mock_task = MockTask()
    class MockTemplar(object):
        def __init__(self):
            pass
        def template(self, template, preserve_trailing_newlines=True, escape_backslashes=True, fail_on_undefined=True, override_vars=None):
            return template
    class MockLoader(object):
        def __init__(self):
            pass
        def path_dwim(self, path):
            return path
    mock_loader = MockLoader()

# Generated at 2022-06-13 09:40:58.495683
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # create instance of class
    actionModule = ActionModule()
    # create instance of AnsibleTemplar
    from ansible.template import Templar
    templar = Templar(loader=None, variables={})
    # end create instance of AnsibleTemplar
    # create instance of AnsibleLoader
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, sources=['localhost,'])
    variable_manager.set_inventory(inventory)

# Generated at 2022-06-13 09:41:04.615550
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # test with fail_msg, with that
    # fail_msg is a string and that is a string
    fail_msg = 'Assertion failed'
    that = 'item1'
    quiet = False
    success_msg = 'All assertions passed'
    tmp = {'that': that}
    task = {'args':{'fail_msg': fail_msg, 'that': that, 'quiet': quiet, 'success_msg': success_msg}}
    result = {'changed':False, 'msg':success_msg}

    test_case = TestCaseActionModule(fail_msg, that, quiet, success_msg, tmp, task)
    assert test_case.run() == result

    # test with msg, with that
    # msg is a string and that is a string
    msg = 'Assertion failed'

# Generated at 2022-06-13 09:41:12.382140
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # arrange
    mock_action = unittest_helper.MockActionModule()
    mock_action._task.args = {'that': 'myvar'}

    # act
    result = mock_action.run(tmp=None, task_vars={'myvar': 'myval'})

    # assert
    assert result['changed'] == False
    assert result['msg'] == 'All assertions passed'


# Generated at 2022-06-13 09:41:18.296821
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.inventory.manager import InventoryManager

    class MockTask():
        def __init__(self, args):
            self.args = args

    # Initial values for testing
    tasks = [MockTask({'that': ['foo == bar', 'baz == foo']})]
    play_context = PlayContext()
    inventory = InventoryManager()
    variable_manager = TaskQueueManager()

    # Get action plugin
    action_plugin = ActionModule()

    # Run method
    result = action_plugin.run(None, None, tasks, play_context, [], variable_manager, None, inventory)
    assert result['_ansible_verbose_always'] == True
    assert result['changed']

# Generated at 2022-06-13 09:41:20.236641
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule(None, {}, None, None, None)
    assert type(action) == ActionModule


# Generated at 2022-06-13 09:41:30.454210
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.module_utils._text import to_text

    def to_native(x):
        return to_text(x, errors='surrogate_then_replace')

    action_module_class = ActionModule(None, dict())

    # test run method
    result = action_module_class.run(None, dict())
    assert result.get('msg') == 'Assertion failed'

    arguments = dict(
        fail_msg='Failed',
        success_msg=['Success1', 'Success2'],
        that="{{ test }} and {{ test1 }}"
    )
    result = action_module_class.run(None, dict(test=True, test1=True), arguments=arguments)
    assert to_native(result.get('msg')) in ['Success1', 'Success2']

    result = action