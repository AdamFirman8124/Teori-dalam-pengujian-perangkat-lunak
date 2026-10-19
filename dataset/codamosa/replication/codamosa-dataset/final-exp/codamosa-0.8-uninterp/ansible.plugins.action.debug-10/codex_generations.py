

# Generated at 2022-06-13 09:44:41.893246
# Unit test for constructor of class ActionModule
def test_ActionModule():
	# set ansible.module_utils.basic.AnsibleModule
	module = ActionModule()
	assert module is not None

# Generated at 2022-06-13 09:44:50.876510
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Test the different kwargs that the constructor recognizes
    test_kwargs = [
            {'task': 'task_value'},
            {'connection': 'connection_value'},
            {'templar': 'templar_value'},
            {'loader': 'loader_value'},
            {'shared_loader_obj': 'shared_loader_obj_value'},
            {'play_context': 'play_context_value'},
            {'variable_manager': 'variable_manager_value'},
            ]
    for test_kwarg in test_kwargs:
        test_action_module = ActionModule(**test_kwarg)
        assert test_action_module.task == 'task_value'
        assert test_action_module.connection == 'connection_value'
        assert test_action_module.tem

# Generated at 2022-06-13 09:44:51.559791
# Unit test for constructor of class ActionModule
def test_ActionModule():
    pass

# Generated at 2022-06-13 09:44:52.198605
# Unit test for constructor of class ActionModule
def test_ActionModule():
    return True

# Generated at 2022-06-13 09:45:02.100052
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Create an instance of ActionModule
    actionmodule = ActionModule(
    )

    # Create an instance of AnsibleOptions

# Generated at 2022-06-13 09:45:13.492984
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    #TODO
    class ActionBaseTest(object):
        def __init__(self):
            self._templar = self
        def template(self, data, convert_bare=True, fail_on_undefined=True):
            return data
        def __getattr__(self, name):
            return name
    
    class ActionModuleTest(ActionModule):
        def __init__(self, *args, **kwargs):
            self._templar = ActionBaseTest()
            self._display = {'verbosity':0}
            self._task = {'args':kwargs['args']}
    
    # no msg, no var
    task_vars = dict()
    module_return = ActionModuleTest(args=dict(verbosity=0)).run(task_vars=task_vars)
    assert module

# Generated at 2022-06-13 09:45:18.295121
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # pylint: disable=too-many-function-args
    import ansible.plugins
    global_action_plugin_loader = ansible.plugins.action.get_loader()
    action_plugin = global_action_plugin_loader.get('debug')
    test_mod = type.__call__(action_plugin)
    assert test_mod is not None

# Generated at 2022-06-13 09:45:32.278829
# Unit test for method run of class ActionModule

# Generated at 2022-06-13 09:45:42.804062
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import os
    import tempfile
    ssh_options = os.environ.get("ANSIBLE_SSH_ARGS")
    if ssh_options is not None:
        del os.environ["ANSIBLE_SSH_ARGS"]

    import ansible.plugins.action.debug

    class Task:
        def __init__(self, args, module_name=''):
            self.args = args
            self.module_name = module_name

    class PlayContext:
        def __init__(self):
            self.prompt = None
            self.verbosity = 2

    class Connection:
        def __init__(self):
            self._shell = None

        def _new_shell(self, **kwargs):
            if self._shell is None:
                from ansible.plugins.connection.ssh import Connection as Connection_

# Generated at 2022-06-13 09:45:50.098911
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import pytest
    from ansible.executor.task_result import TaskResult
    from ansible.module_utils import basic
    from ansible.module_utils.six import StringIO

    args = {'verbosity': 0}
    task_vars = {'failed': False}

    # Testing for 'msg' in task.args
    task = _Task()
    task._task.args.update(args)
    task._task.args['msg'] = 'Hello world!'
    result = task.run(task_vars=task_vars)
    assert result['msg'] == 'Hello world!'

    # Testing for 'var' in task.args
    task = _Task()
    task._task.args.update(args)
    task._task.args['var'] = 'Hello world!'

# Generated at 2022-06-13 09:46:04.770574
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Test for method run(self, tmp=None, task_vars=None)....
    print()
    print('#' * 20, "unit test for run of class ActionModule", '#' * 20)
    print()
    print('## Test for run when var is not in self._task.args ##')
    print()
    print('# Test for run when verbosity is less than or equal to self._display.verbosity #')
    print()
    print('# result should be: Hello world! #')
    print()
    # test data
    var = 'msg'
    verbosity = 0
    msg = 'Hello world!'
    # build test data
    tmp = None
    task_vars = None
    result = {}

# Generated at 2022-06-13 09:46:17.023603
# Unit test for constructor of class ActionModule
def test_ActionModule(): 
    # This is a hack to avoid getting a deprecation warning.
    # In Ansible 2.5+ the module_utils.basic import was deprecated and the ActionModule class was moved to the action
    # plugin.
    import ansible.plugins.action
    ActionModule = getattr(ansible.plugins.action, 'ActionModule') 
    action_module = ActionModule("test_task", dict(msg="Hello world!", verbosity=1))
    action_module.templar = Template("test") 
    action_module.display = Display("verbosity")
    result = action_module.run()
    assert result["msg"] == "Hello world!"
    assert not result["failed"]


# Generated at 2022-06-13 09:46:24.111406
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import mock
    from ansible.plugins.action.debug import ActionModule

    def dummy_path_dwim(self, something):
        return 'dummy'

    # Create module fixture
    module_mock = mock.MagicMock(path_dwim=mock.MagicMock(side_effect=dummy_path_dwim))

    # Create display fixture
    display_mock = mock.MagicMock()
    display_mock.verbosity = 2

    # Create task fixture
    task_mock = mock.MagicMock()
    task_mock.args = dict()

    task_executor = ActionModule(task_mock, display_mock, module_mock)
    assert task_executor is not None
    return


# Generated at 2022-06-13 09:46:25.189113
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule

# Generated at 2022-06-13 09:46:36.342748
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Set up modules that are stubbed out
    import ansible.plugins.action.debug
    ansible.plugins.action.debug.ActionModule = ActionModule
    import ansible.plugins
    ansible.plugins.action_loader = ansible.plugins.ActionModule
    import ansible.playbook.play_context
    playbook_context = ansible.playbook.play_context.PlayContext()
    # Set up a fake inventory
    import ansible.inventory.manager
    inventory = ansible.inventory.manager.InventoryManager(loader=None, sources=None)
    # Create fake task_vars
    task_vars = {}
    # Create fake loader
    import ansible.parsing.dataloader
    loader = ansible.parsing.dataloader.DataLoader()
    # Create fake variables
    import ans

# Generated at 2022-06-13 09:46:36.973622
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert True

# Generated at 2022-06-13 09:46:44.072227
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''Unit test for method run of class ActionModule'''
    import os
    import sys
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes

    # initialize module_args: ansible.module_utils.basic.AnsibleModule
    module_args = dict(verbosity = 0)
    module_args = basic.AnsibleModule(argument_spec = module_args, supports_check_mode = False)

    # initialize self.args: ansible.module_utils.basic.AnsibleModule
    # TODO:
    # The class of arguments should be changed to the format below.
    # self.args = {'var': '{{ AnsibleHelloWorld }}', 'verbosity': '0', 'assertion': 'equals'}
    # If the format below is used, some

# Generated at 2022-06-13 09:46:54.657465
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.vars import load_extra_vars
    from ansible.vars import VariableManager
    from ansible.utils.vars import load_options_vars
    from ansible.errors import AnsibleUndefinedVariable
    import mock

    class Opts(mock.MagicMock):
        connection = 'local'


# Generated at 2022-06-13 09:47:04.587295
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action = ActionModule(
        {
            "name": "test",
            "verbosity": 0,
            "args": {
                "var": "foo"
            },
            "task": {
                "args": {
                    "verbosity": 0,
                    "var": "foo"
                }
            }
        },
        loader=None,
        templar=None,
        shared_loader_obj=None)

    action._templar.available_variables = {
        "foo": "bar"
    }

    assert action.run() == {
        "failed": False,
        "bar": "bar",
        "_ansible_verbose_always": True
    }

# Generated at 2022-06-13 09:47:07.773610
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.plugins.loader import action_loader
    action = action_loader.get('debug', class_only=True)
    assert True
    assert action._task.action == 'debug'
    assert action.plugin_name == 'debug'


# Generated at 2022-06-13 09:47:25.909186
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils._text import to_bytes
    from ansible.plugins.action import ActionBase
    from ansible.utils.vars import combine_vars
    from ansible.parsing.dataloader import DataLoader

    # Preparing variables for unit test
    class Task:
        def __init__(self, action_args):
            self.args = action_args

    class Display:
        def __init__(self, verbosity):
            self.verbosity = verbosity
    class Connection:
        def __init__(self, remote_user, host_list=list()):
            self.remote_user = remote_user
            self.host_list = host_list
        def get_host_list(self):
            return self.host_list

# Generated at 2022-06-13 09:47:30.391856
# Unit test for method run of class ActionModule

# Generated at 2022-06-13 09:47:40.323276
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    print('Testing for method run of class ActionModule')

    class MyActionModule(ActionModule):
        def run(self, tmp=None, task_vars=None):
            # Get the results from original ActionModule
            result = super(MyActionModule, self).run(tmp, task_vars)
            # Create a sample task_vars
            task_vars = {"var_name": "value"}
            # Assert value of result returned
            assert(result['failed'] == False)
            assert(result['skipped'] == False)
            assert(result['msg'] == 'Hello world!')
            # Assert that task_vars is passed in parameters
            assert(task_vars != None)
    # Create a sample task
    task = {'args': {}}
    # Create a instance of MyActionModule
    action_module

# Generated at 2022-06-13 09:47:43.166680
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Testing non-existent values
    with pytest.raises(KeyError):
        ActionModule()

# Generated at 2022-06-13 09:47:43.998516
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 09:47:58.855297
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # test all_actions
    class Mock_ActionBase(ActionBase):
        def run(self, tmp=None, task_vars=None):
            return "Run"
    # test all_actions
    actionModule = ActionModule(Mock_ActionBase(), dict(msg='test_msg'))
    assert actionModule.run() == {'changed': False, 'failed': False, 'msg': 'test_msg', '_ansible_verbose_always': True}

    class Mock_ActionBase_run_func1(ActionBase):
        def run(self, tmp=None, task_vars=None):
            return "Run"
    # test all_actions
    actionModule = ActionModule(Mock_ActionBase_run_func1(), dict(var='test_var'))

# Generated at 2022-06-13 09:48:04.239169
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # create instance of ActionModule
    module_run = ActionModule()

    # create a super simple task with module parameters
    task_args = {
        'var': {
            'msg': 'Hello world!'
        },
        'verbosity': 0
    }
    task = {
        'args': task_args
    }
    # create a super simple task_vars
    task_vars = {}

    # execute method run of class ActionModule
    # check if we get a result
    assert module_run.run(task_vars=task_vars, tmp='/tmp', task=task), "ActionModule.run() didn't return a result"

# Generated at 2022-06-13 09:48:15.238142
# Unit test for constructor of class ActionModule
def test_ActionModule():
    class AnsibleModule():
        def __init__(self, argument_spec={}, bypass_checks=False, no_log=False,
        check_invalid_arguments=True, mutually_exclusive=[], required_together=[],
        required_one_of=[], add_file_common_args=False, supports_check_mode=False,
        required_if=None):
            self.argument_spec = argument_spec
            self.bypass_checks = bypass_checks
            self.no_log = no_log
            self.check_invalid_arguments = check_invalid_arguments
            self.mutually_exclusive = mutually_exclusive
            self.required_together = required_together
            self.required_one_of = required_one_of
            self.add_file_common_args = add_file_common_args

# Generated at 2022-06-13 09:48:16.408081
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert('Hello world' in ActionModule.run())

# Generated at 2022-06-13 09:48:26.545205
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.basic import AnsibleModule
    from ansible.template import Templar
    from ansible.parsing.vault import VaultLib
    from ansible.plugins.loader import action_loader
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager

    context = dict(TASK_ID='TESTTASKID', PLAY_ID='TESTPLAYID', PLAYBOOK='testplaybook')
    play_context = PlayContext()
    module = AnsibleModule(argument_spec=dict())
    templar = Templar(loader=None, variables=dict(var1='foo', var2='bar'))

# Generated at 2022-06-13 09:48:55.332763
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Initialize required module and class arguments.
    dict_args = dict()
    dict_args['msg'] = 'Hello world!'
    action = ActionModule('name', dict_args)
    task_vars = dict()

    # Initialize required class variables.
    action._task_vars = task_vars
    action._task = ActionModule('name', dict_args)
    action._task.args = dict_args
    action._display = ActionModule('name', dict_args)
    action._display.verbosity = 0

    # Mock function to prevent exit due to a failed module.
    def mock_run_fail(tmp=None, task_vars=None):
        return (tmp, task_vars)

    action.run_fail = mock_run_fail

    # Execute method and verify.

# Generated at 2022-06-13 09:49:05.489200
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """
    Test method run of class ActionModule
    """
    import json
    # Run command without any options
    am = ActionModule()
    am._display = MockDisplay()
    am._task = {'args':{'verbosity': 0}}
    am.run()
    assert am._result == {'failed': False, 'msg': 'Hello world!', '_ansible_verbose_always': True}
    # Run command with msg in args 
    am = ActionModule()
    am._display = MockDisplay()
    am._task = {'args':{'verbosity': 0, 'msg': 'Hello world!'}}
    am.run()
    assert am._result == {'failed': False, 'msg': 'Hello world!', '_ansible_verbose_always': True}
    # Run command with verbosity in args 

# Generated at 2022-06-13 09:49:08.954216
# Unit test for constructor of class ActionModule
def test_ActionModule():
    task_args = {'var':'hostvars[inventory_hostname]'}
    am = ActionModule(None, task_args, {'verbosity': 0}, None, None)
    assert am.run(task_vars={'inventory_hostname':'localhost', 'hostvars': {'localhost':{'ansible_os_family': 'Debian'}}}) == {"msg": "localhost", "ansible_os_family": "Debian"}

# Generated at 2022-06-13 09:49:12.248077
# Unit test for constructor of class ActionModule
def test_ActionModule():
    value = ActionModule(None, None, "debug", None, None, None, None)
    assert value is not None

# Generated at 2022-06-13 09:49:22.653740
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # mock the task_vars
    task_vars = {'ansible_verbosity': 0}
    # mock the task
    task =  {'action': 'debug','args': {'msg': 'Hello world!'}}
    # mock the self._display
    display = {}
    display['verbosity'] = 0
    # mock the self._templar
    templar = {}
    templar['template'] = lambda a,b,c: a 
    # mock the self object
    self = {}
    self['_task'] = task
    self['_display'] = display
    self['_templar'] = templar
    # create a new instance of the ActionModule
    actionModule = ActionModule()
    for key, value in vars(actionModule).items():
        setattr(self, key, value)

# Generated at 2022-06-13 09:49:28.455144
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader

    class PlayContext(object):
        def __init__(self):
            self.verbosity = 0

    class Task(object):
        def __init__(self):
            self.args = {}
            self.action = 'debug'
            self.name = 'debug'
            self.loop = []
            self.notify = []
            self.run_once = False
            self.delegate_to = False
            self.when = []
            self.transport = 'ssh'

    class TaskExecutor(object):
        def __init__(self):
            self.play_context = PlayContext()


# Generated at 2022-06-13 09:49:37.707264
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import copy
    import pytest

    task = {'_ansible_verbosity': 0, '_ansible_no_log': False, 'args': {'var': 'var_name', 'verbosity': '0'}, 'loop_args': {'headers': {'Content-Length': '100', 'Content-Type': 'application/json'}, 'json': {'url': 'http://localhost:8888', 'username': 'admin', 'password': 'admin'}}, 'loop': '{{ output }}', 'register': 'result'}

    loader_mock = Mock()
    templar_mock = Mock()
    display_mock = Mock()
    connection_mock = Mock()
    ansible_mock = Mock()


# Generated at 2022-06-13 09:49:44.576660
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.utils.display import Display
    import os
    import sys

    class Options:
        module_path = ''
        remote_tmp = ''
        connection = ''

        def __init__(self):
            self.verbosity = 0
            self.no_log = False

    class PlayContext:
        def __init__(self):
            self.remote_addr = None
            self.remote_user = None
            self.password = None
            self.port = None
            self.become = False
            self.become_method = None
            self.become_user = None
            self.become_pass = None
            self.become_exe = None
            self.no_log = False
            self.verbosity = 0

    class ActionBase:
        _task = None


# Generated at 2022-06-13 09:49:45.990627
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert isinstance(ActionModule(None, None, None, None), ActionModule)

# Generated at 2022-06-13 09:49:47.056946
# Unit test for constructor of class ActionModule
def test_ActionModule():
    constructor = ActionModule()
    assert constructor is not None

# Generated at 2022-06-13 09:50:42.535530
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # private method _get_task_vars returns a dict object
    task_vars = ActionModule._get_task_vars(dict())
    # initialize object at module level
    action_module = ActionModule(dict(), dict(), False, task_vars, None)

    # Test default values when both 'msg' and 'var' are not present
    args = dict()
    result = action_module.run(None, task_vars, args)
    assert (result.get('msg') == "Hello world!")

    # Test value of msg when msg option is present
    args = dict({'msg': "foo"})
    result = action_module.run(None, task_vars, args)
    assert (result.get('msg') == "foo")

    # Test value of var when var option is present

# Generated at 2022-06-13 09:50:46.330072
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''
    Unit test for constructor of class ActionModule
    '''
    actionmodule = ActionModule()
    assert actionmodule._VALID_ARGS == frozenset(('msg', 'var', 'verbosity'))

# Generated at 2022-06-13 09:50:55.339632
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import ansible.plugins.action.debug as debug

    # Create a task object
    task = dict()
    task['args'] = dict()
    task['args']['msg'] = 'Hello world!'
    task['args']['verbosity'] = 0
    task_vars = dict()
    class FakeClass:
        pass
    connection = FakeClass()
    # Play context is required by the debug plugin
    class FakeClass2:
        def __init__(self):
            self.play_context = FakeClass()
    play_context = FakeClass2()

    # Create action module
    action = debug.ActionModule(task, connection, play_context, loader=None, templar=None, shared_loader_obj=None)

    # Run method

# Generated at 2022-06-13 09:51:05.666367
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """
    Constructor of ActionModule:
    1. ActionBase(self,task,connection,play_context,loader,templar,shared_loader_obj)
    2. ActionModule(self,task,connection,play_context,loader,templar,shared_loader_obj):
    """
    task = None
    connection = None
    play_context = None
    loader = None
    templar = None
    shared_loader_obj = None

    action_base = ActionBase(task,connection,play_context,loader,templar,shared_loader_obj)
    action_module = ActionModule(task,connection,play_context,loader,templar,shared_loader_obj)

# Generated at 2022-06-13 09:51:14.331962
# Unit test for constructor of class ActionModule
def test_ActionModule():
    for key in ['msg', 'var']:
        class FakeTask():
            def __init__(self, args):
                self.args = args
        class FakeDisplay:
            def __init__(self, verbosity):
                self.verbosity = verbosity
        class FakePlayContext:
            def __init__(self, check_mode, verbosity):
                self.check_mode = check_mode
                self.verbosity = verbosity
        task_vars = {
            'msg' : 'msg test',
            'var' : 'var test',
            'verbosity' : 3,
            'test' : 'test'
            }

        test_args = dict()
        test_args[key] = task_vars[key]
        test_result = dict()
        test_result[key] = task_vars

# Generated at 2022-06-13 09:51:27.910692
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    
    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = Inventory(loader=loader, variable_manager=variable_manager)

    play_source = dict(
        name = "Ansible Play",
        hosts = 'localhost',
        gather_facts = 'no',
        tasks = [
            dict(action=dict(module='debug', args=dict(msg='Hello world!')))
        ]
    )

    play = Play().load(play_source, variable_manager=variable_manager, loader=loader)


# Generated at 2022-06-13 09:51:35.496686
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Test __init__() method of ActionModule class
    action_module = ActionModule(dict(), dict())

    assert action_module.TRANSFERS_FILES == False
    assert action_module._VALID_ARGS == frozenset(('msg', 'var', 'verbosity'))
    assert action_module._templar == None
    assert action_module._shared_loader_obj == None
    assert action_module._task == None
    assert action_module._connection == None
    assert action_module._play_context == None
    assert action_module._loader == None
    assert action_module._display == None

# Generated at 2022-06-13 09:51:41.678172
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # class ComplexActionBase(ActionBase):
    from ansible.plugins.action.debug import ActionModule
    from ansible.playbook.task import Task

    # class Task(object):
    #     def __init__(self, *args, **kwargs):
    #         super(Task, self).__init__()
    # class Connection(object):
    #     def __init__(self, *args, **kwargs):
    #         super(Connection, self).__init__()

    am = ActionModule(Task(), Connection())




# TODO: Implement tests

# Generated at 2022-06-13 09:51:42.490235
# Unit test for constructor of class ActionModule
def test_ActionModule():
    a=ActionModule()


# Generated at 2022-06-13 09:51:44.411575
# Unit test for constructor of class ActionModule
def test_ActionModule():
    result = ActionModule.run(tmp=None, task_vars=None)
    assert result['msg'] == 'Hello world!'
    assert False

# Generated at 2022-06-13 09:53:39.743795
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import ansible.plugins
    t = ansible.plugins.action.ActionModule('setup', 'test', 'test', 'test')
    assert t.name == 'setup'
    assert t.action == 'test'
    assert t.task == 'test'
    assert t.args == 'test'
    assert t.loader is not None
    assert t.templar is not None
    assert t.shared_loader_obj is not None

# Generated at 2022-06-13 09:53:47.531724
# Unit test for constructor of class ActionModule
def test_ActionModule():

    class FakeTask():
        def __init__(self):
            self._args = {'verbosity': 1 }
        def get_args(self):
            return self._args

    class FakeDisplay():
        def __init__(self):
            self._verbosity = 1
        def set_verbosity(self, verbosity):
            self._verbosity = verbosity

    class FakeActionBase():
        def __init__(self):
            self._task = FakeTask()
            self._display = FakeDisplay()
        def run(self, tmp, task_vars):
            return {'foo': 'bar'}
        def get_task(self):
            return self._task
        def get_display(self):
            return self._display

    # Create object ActionModule without arg msg and verbosity=0, result['skipped'] should be

# Generated at 2022-06-13 09:53:56.557030
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """
    Testing of ActionModule()
    This is an unittest for ActionModule(), using pytest and mocker
    """

    from ansible.plugins.action import ActionModule
    from ansible.errors import AnsibleUndefinedVariable
    from ansible.module_utils._text import to_text
    # Test 1:
    # action argument 'msg' is defined
    # expected result: output = 'Hello world!'
    ACTION = {'msg': 'Hello world!'}
    TASK = None
    ACTION_BASE = None
    DISPLAY = None
    TEMPLAR = None
    # Creating an instance of class ActionModule
    TEST_ACTION = ActionModule(TASK, ACTION, DISPLAY, ACTION_BASE, TEMPLAR)
    # Unittest for run()
    TASK_VARS = None
   

# Generated at 2022-06-13 09:53:59.517986
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert module._VALID_ARGS is not None

# Generated at 2022-06-13 09:54:12.389743
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """ Tests the run method of ActionModule
    This tests that the variables msg and var are mutually exclusive, and also
    tests that both return the expected data.
    """
    import ansible.plugins.action.debug
    import ansible.playbook.task
    import ansible.utils.template
    import ansible.vars.manager
    t = ansible.playbook.task.Task()
    t.action = 'debug'
    t_vars = ansible.vars.manager.VarsManager()
    a = ansible.plugins.action.debug.ActionModule(t, t_vars)
    d = {}
    
    #Test that msg and var cannot be used together
    t.args = {'msg': 'ABCDE', 'var': ['var1', 'var2']}

# Generated at 2022-06-13 09:54:15.630015
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)


# Generated at 2022-06-13 09:54:17.497894
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule()
    assert module.__class__.__name__ == 'ActionModule'

# Generated at 2022-06-13 09:54:18.002685
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 09:54:28.422693
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    context = 5
    task_vars = {'ansible_verbosity': 5}
    args = {'msg': "This is a test", 'verbosity': context}

    am = ActionModule(None, task_vars, args)

    assert am.run()['msg'] == "This is a test"
    assert am.run()['failed'] == False

    del args['verbosity']
    am = ActionModule(None, task_vars, args)

    assert am.run()['msg'] == "This is a test"
    assert am.run()['failed'] == False

    task_vars = {'ansible_verbosity': 6}
    am = ActionModule(None, task_vars, args)

    assert am.run()['skipped_reason'] == "Verbosity threshold not met."

# Generated at 2022-06-13 09:54:36.613807
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.plugins.action import ActionModule
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.play import Play
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.utils.vars import combine_vars
    loader = DataLoader()
    inventory = InventoryManager(loader, sources='')
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    # Create a block for testing