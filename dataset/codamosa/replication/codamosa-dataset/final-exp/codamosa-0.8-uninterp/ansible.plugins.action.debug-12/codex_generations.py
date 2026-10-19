

# Generated at 2022-06-13 09:44:40.562319
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(None, {}, None, None)
    assert module is not None

# Generated at 2022-06-13 09:44:43.350256
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # We do not have a sane way to unit test the print module yet.  The
    # code we have in place does not actually result in the module ever
    # being used from a unit test.
    pass

# Generated at 2022-06-13 09:44:44.260500
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # TODO
    return True

# Generated at 2022-06-13 09:44:52.097818
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """
    Test the method run of ActionModule
    """
    # pylint: disable=protected-access,too-many-locals
    # pylint: disable=too-many-arguments, too-many-branches, too-many-statements
    # set up arguments
    tmp = "ansible.tmp"
    task_vars = dict()
    task = DummyObject()
    task_vars["ansible_verbosity"] = 1

    # test with no msg and var in task.args
    # the following debug module should be skipped
    task_args = dict()
    task.args = task_args
    action_module = ActionModule(task, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    result = action_module._execute_

# Generated at 2022-06-13 09:44:53.933357
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule()
    assert action_module is not None

# Generated at 2022-06-13 09:44:56.470913
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # TODO: add failure test for 'msg' and 'var' are incompatible options
    # TODO: test display is not None
    pass

# Generated at 2022-06-13 09:45:04.449102
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.plugins import module_loader, callback_loader

    Options = namedtuple('Options', [
        'connection', 'module_path', 'forks', 'become', 'become_method', 'become_user',
        'check', 'listhosts', 'listtasks', 'listtags', 'syntax', 'sudo_user', 'sudo',
        'diff', 'remote_user', 'verbosity', 'timeout', 'private_key_file'
    ])

# Generated at 2022-06-13 09:45:08.642918
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """ Unit test for method run of class ActionModule """
    module = ActionModule(load_fixture('debug_test1.yml'), {})
    result = module.run(None, {})
    assert result['failed'] is False
    assert result['msg'] == 'Hello world!'

# Generated at 2022-06-13 09:45:09.682147
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule()
    assert action

# Generated at 2022-06-13 09:45:11.714777
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule(None, constuct_args={'task': None})
    print(am)


# Generated at 2022-06-13 09:45:31.346791
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager

    play_context = PlayContext()
    play_context.verbosity = 0
    play_context._set_task_and_variable_override(1, 1, 1, 1)
    task = dict(action=dict(module='debug', msg='foobar'))

    p = Play().load(dict(
        name='test play',
        hosts='all',
        gather_facts='no',
        tasks=[task]
    ), variable_manager=play_context.variable_manager, loader=play_context.loader)

    tqm = None

# Generated at 2022-06-13 09:45:34.539466
# Unit test for constructor of class ActionModule
def test_ActionModule():
    instance = ActionModule(None, dict(a='b', c='d'), None)
    assert instance._task.action == 'debug'
    assert instance._task.args == dict(a='b', c='d')

# Generated at 2022-06-13 09:45:35.152506
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    m = ActionModule()

# Generated at 2022-06-13 09:45:46.188519
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import os

    import ansible.compat.six as six

    from ansible.plugins.action import ActionModule
    from ansible.utils.vars import combine_vars

    from io import StringIO
    from ansible.module_utils.common._collections_compat import Mapping

    from units.mock.loader import DictDataLoader
    from units.mock.path import mock_unfrackpath_noop

    from ansible.playbook.task import Task
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    from ansible.template import Templar

    from ansible.parsing.dataloader import DataLoader


# Generated at 2022-06-13 09:45:47.359276
# Unit test for constructor of class ActionModule
def test_ActionModule():
    a = ActionModule(None, loader=None, templar=None, shared_loader_obj=None)

# Generated at 2022-06-13 09:45:51.320407
# Unit test for constructor of class ActionModule
def test_ActionModule():
    test_action = ActionModule()
    # check if class is instantiated.
    # assert_in() is only present in Python 2.7 and above
    assert 'ActionModule' in str(type(test_action))


# Generated at 2022-06-13 09:45:59.617154
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ''' Unit test for method run of class ActionModule
        This is a very simple test as calling out to the templating language is
        very difficult to test completely.
    '''
    from ansible.playbook import Play
    from ansible.playbook.task import Task
    from ansible.playbook.role.include import IncludeRole

    import ansible.plugins.action.debug as debuglib
    from ansible.template import Templar
    from ansible.utils.display import Display
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    display = Display()
    hostvars = dict()
    templar = Templar(loader=None, variables=VariableManager(loader=None, inventory=InventoryManager(loader=None)))
    task = Task()


# Generated at 2022-06-13 09:46:01.038866
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule()

# Generated at 2022-06-13 09:46:09.332272
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Load necessary class and data
    module = 'ansible.plugins.action.debug'
    action_module = 'ActionModule'
    data = {}
    tmp_path = None

    # Init
    ro = __import__(module, fromlist=[action_module])
    ActionModule = getattr(ro, action_module)
    action_module_obj = ActionModule()
    action_module_obj._task = mock()
    action_module_obj._task.args = data
    action_module_obj._display = mock()
    action_module_obj._display.verbosity = 0
    action_module_obj._templar = mock()
    action_module_obj._templar.template = mock()
    action_module_obj._templar.template.return_value = 'template content'

    # test 1
   

# Generated at 2022-06-13 09:46:10.212131
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 09:46:31.268361
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module_obj = ActionModule()
    action_module_obj._task.args = dict()
    action_module_obj._task.args['verbosity'] = 0
    action_module_obj._task.args['var'] = "test_var"
    action_module_obj._task.args['msg'] = "test_message"
    action_module_obj._task.args['verbosity'] = 1
    action_module_obj._display.verbosity = 1
    action_module_obj._templar.template = lambda template, convert_bare, fail_on_undefined: template
    action_module_obj._templar.template = lambda template, convert_bare, fail_on_undefined: template
    results_dict = action_module_obj.run()
    assert results_dict['msg'] == 'test_message'

# Generated at 2022-06-13 09:46:38.845799
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Test failed when msg and var are used together
    assert ActionModule(None, None).run(None, None)['failed'] == True
    assert ActionModule(None, {'var': 'VAR'}).run(None, None)['failed'] == False
    assert ActionModule(None, {'var': 'VAR', 'msg': 'MSG'})['failed'] == True

# Generated at 2022-06-13 09:46:49.469669
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.action.debug import ActionModule
    import ansible.module_utils.basic
    from ansible.module_utils.basic import AnsibleModule
    ansible.module_utils.basic._ANSIBLE_ARGS = None
    am = ActionModule(dict(
        ANSIBLE_MODULE_ARGS={
            'msg': 'Hello world!',
        },
        ANSIBLE_MODULE_NAME='foo',
        ANSIBLE_MODULE_CONSTANTS={
            'FOO': 'BAR',
        },
        ANSIBLE_MODULE_ARGS_FILE='/tmp/ansible-module-args.1234567890',
        ANSIBLE_MODULE_ARGS_FILE_CONTENT='FOO: BAR',
    ), object())
    result = am.run(None, None)

# Generated at 2022-06-13 09:46:50.057222
# Unit test for constructor of class ActionModule
def test_ActionModule():
    ActionModule()

# Generated at 2022-06-13 09:46:59.646706
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    print("Test for method run of class ActionModule")
    var_string="TestVar"
    var_string_result="Hello World"
    var_list=[1,2,3]
    var_list_result=[1,2,3]
    var_dict={"key":123,"value":456}
    var_dict_result={"key":123,"value":456}
    result={}
    class FakeTask:
        def __init__(self,args):
            self.args=args
    class FakeDisplay:
        def __init__(self):
            self.verbosity=0

    action_module=ActionModule()
    action_module._task=FakeTask({"verbosity":"0"})
    action_module._display=FakeDisplay()


# Generated at 2022-06-13 09:47:08.808724
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # create an instance of ActionModule to run the tests against
    test_action = ActionModule(dict(RUN_COMMAND='/usr/bin/ansible-test-action'))

    # create a dummy class to mimic the class ansible.module_utils.basic._AnsibleModule
    class DummyAnsibleModule:
        def __init__(self):
            self.params = dict(
                verbosity=2,
                msg='Hello world test 1!',
                )

    # create a dummy class to mimic the class ansible.utils.display.Display
    class DummyAnsibleDisplay:
        verbosity = 2

    # create a dummy class to mimic the class ansible.parsing.dataloader.DataLoader
    class DummyDataLoader:
        pass

    # create a dummy class to mimic the class ansible

# Generated at 2022-06-13 09:47:18.928199
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.playbook.play import Play
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    # Dummy arguments
    args = {}
    play_context = PlayContext()
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=['localhost,'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    # Task arguments to pass to ActionModule constructor

# Generated at 2022-06-13 09:47:19.459596
# Unit test for constructor of class ActionModule
def test_ActionModule():
    pass

# Generated at 2022-06-13 09:47:20.134195
# Unit test for constructor of class ActionModule
def test_ActionModule():
    pass

# Generated at 2022-06-13 09:47:30.077296
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Test for get dict from argument 'var'.
    var = dict(a=1, b=2, c=dict(d=3, e=4))
    task = dict(args=dict(var=var))
    _result = dict(failed=False, changed=False)
    _result[var] = 'a=1, b=2, c=d=3, e=4'
    assert ActionModule(task, dict())._execute_module() == _result

    # Test for get list from argument 'var'.
    var = list(range(6))
    task = dict(args=dict(var=var))
    _result = dict(failed=False, changed=False)
    _result[to_text(type(var))] = '0, 1, 2, 3, 4, 5'

# Generated at 2022-06-13 09:47:53.638175
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None,
                        shared_loader_obj=None).module_name == 'debug'

# Generated at 2022-06-13 09:48:02.352627
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    _task = {
        "action": {
            "__ansible_module__": "debug",
            "__ansible_arguments__": "msg='hello world'"
        },
        "args": {
            "msg": "hello world"
        },
        "delegate_to": None,
        "changed_when": True,
        "action_plugins": [],
        "name": "debug hello world",
        "when": True
    }

    _display = {
        "verbosity": 0
    }

    _templar = {
        "template": lambda var, convert_bare, fail_on_undefined: var
    }

    _task_vars = {
        "msg": "hello world"
    }


# Generated at 2022-06-13 09:48:03.129041
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    modobj = ActionModule()
    modobj.run()

# Generated at 2022-06-13 09:48:09.710870
# Unit test for constructor of class ActionModule
def test_ActionModule():
  # test __init__
  mod = ActionModule()
  print(type(mod))
  print(type(mod._VALID_ARGS))
  print('VALID_ARGS: ' + mod._VALID_ARGS.__str__())
  print('TRANSFERS_FILES: ' + mod.TRANSFERS_FILES.__str__())
  assert (type(mod) is ActionModule)
  assert (type(mod._VALID_ARGS) is frozenset)
  assert (mod._VALID_ARGS.__str__() == "frozenset({'verbosity', 'msg', 'var'})")
  assert (mod.TRANSFERS_FILES is False)

# Generated at 2022-06-13 09:48:16.845761
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(argument_spec=dict(msg=dict(type='str'), var=dict(type='str'), verbosity=dict(type='int')),
                           supports_check_mode=True)
    am = ActionModule(module, "task.yml")
    assert isinstance(am, ActionModule)

# Generated at 2022-06-13 09:48:18.362502
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(None, dict(), dict())


# Generated at 2022-06-13 09:48:28.586140
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Create test object
    am = get_class_instance(ActionModule, "ActionModule", path='ansible/plugins/action', args={'action_plugins': '.'})

    # Test when verbosity is not met
    am._task.args = {'verbosity': 2}
    result = am.run()
    assert result['msg'] == "Verbosity threshold not met."
    assert result['skipped'] is True

    # Test when verbosity is met but msg is not provided, var not provided and
    # var is not given
    am._task.args = {'verbosity': 0}
    result = am.run()
    assert result['msg'] == "Hello world!"
    assert result['failed'] is False

    # Test when verbosity is met but msg is not provided, var provided and var
    # is interpreted as string
    am

# Generated at 2022-06-13 09:48:29.736666
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert not ActionModule(None, {}, {})._task.args

# Generated at 2022-06-13 09:48:39.392944
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Initialize the test class
    test = ActionModule(name='test', task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    # Assert check with empty task args
    assert test.run() == {'failed': False}
    # Assert check with msg args
    assert test.run(task_vars={'verbosity': 1}) == {'msg': 'Hello world!', '_ansible_verbose_always': True}
    # Assert check with verbosity args
    assert test.run(
        task_vars={'verbosity': 0}) == {'skipped': True, 'skipped_reason': 'Verbosity threshold not met.', 'failed': False}
    # Assert check with var args

# Generated at 2022-06-13 09:48:39.992575
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(None)

# Generated at 2022-06-13 09:49:22.862732
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Test the success scenarios
    task_vars = {'msg': 'Testing ansible debug module'}
    results = dict()
    result = dict(failed=False, msg='Hello world!', _ansible_verbose_always=True)
    my_obj = ActionModule(None, None, task_vars, load_arg_spec=False)
    my_obj.run(None, task_vars)
    assert result == results

    # Test the failure scenarios
    results = {"failed": True, "msg": "'msg' and 'var' are incompatible options"}
    my_obj = ActionModule(None, None, task_vars, load_arg_spec=False)
    my_obj._task.args = {'msg': 'Testing ansible debug module', 'var': 'Testing ansible debug module'}

# Generated at 2022-06-13 09:49:23.959376
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule()
    assert isinstance(module, ActionModule)

# Generated at 2022-06-13 09:49:24.812462
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 09:49:34.571387
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """Create ActionModule object
    """
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes
    class FakeActionModule(ActionModule):
        def run(self, tmp=None, task_vars=None):
            del tmp, task_vars
            return {}

    task_vars = {'verbose': True}
    connection = 'local'
    play_context = {}

    # Execute constructor
    am = FakeActionModule(task=None, connection=connection, play_context=play_context, 
        loader=None, templar=basic.AnsibleTemplar(), shared_loader_obj=None)
    
    # Check if member variables are initialized
    assert am._play_context == play_context
    assert am._task == None
    assert am._connection

# Generated at 2022-06-13 09:49:42.222309
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    test_class = ActionModule('test', dict(msg="Hello world"))
    result = test_class.run()
    assert result['msg'] == 'Hello world'

    test_class = ActionModule('test', dict(var='foo'))
    result = test_class.run(task_vars={'foo': 'hello world'})
    assert result['foo'] == 'hello world'

    test_class = ActionModule('test', dict(var=['foo', 'bar']))
    result = test_class.run(task_vars={'foo': 'hello world', 'bar': 'hello world'})
    assert result['<type \'list\'>'] == ['hello world', 'hello world']

    test_class = ActionModule('test', dict(var=dict(foo='bar', bar='foo')))

# Generated at 2022-06-13 09:49:42.782942
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert True

# Generated at 2022-06-13 09:49:51.012898
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """
    This is a unittest for the module ActionModule, which is in the
    ActionModule.py file.
    """
    # create a empty argument
    arguments = {}

    # create a empty task
    task = {}

    # create a moduleloader
    my_loader = {}

    # create a connection
    connection = {}

    # create a variable manager
    variable_manager = {}

    # create a fake display
    display = {}

    # create the object and store it to the variable named test_object
    test_object = ActionModule(task, connection, my_loader, variable_manager, display)

    # test the constructor of the object
    assert isinstance(test_object, ActionModule)
    assert test_object.TRANSFERS_FILES == False
    assert test_object._VALID_ARGS == frozenset

# Generated at 2022-06-13 09:49:59.942643
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.facts.system.distribution import Distribution
    from ansible.module_utils.facts.system.distribution import LinuxDistribution
    from ansible.module_utils.facts.system.services import Services
    import ansible.module_utils.facts.system.distribution
    import ansible.module_utils.facts.system.services

    import datetime


# Generated at 2022-06-13 09:50:05.285964
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import ansible.plugins.loader as plugin_loader

    plugin_loader.add_directory('./plugins')
    action = plugin_loader.get('action', 'debug')
    action = action.ActionModule(None, None, None)
    assert action

    # Test constant _VALID_ARGS
    assert action._VALID_ARGS == frozenset(('msg', 'var', 'verbosity'))

    # Test constant TRANSFERS_FILES
    assert action.TRANSFERS_FILES == False

# Test method run() of class ActionModule

# Generated at 2022-06-13 09:50:18.808088
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible import context
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.playbook.play import Play
    from ansible.cli import CLI
    from ansible.plugins.loader import action_loader
    from ansible.inventory.manager import InventoryManager
    from ansible.executor.task_result import TaskResult
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.utils.shlex import shlex_split
    from ansible.utils.vars import load_extra_vars
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.group import Group
    from ansible.inventory.host import Host


# Generated at 2022-06-13 09:51:55.852920
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    am = ActionModule(loader=None, templar=None, shared_loader_obj=None)
    assert "Hello world!" == am._task.args.get('msg', None)
    assert am.run(task_vars=None)['msg'] == "Hello world!"

    am = ActionModule(loader=None, templar=None, shared_loader_obj=None)
    am._task.args['msg'] = "Hello Universe!"
    assert am.run(task_vars=None)['msg'] == "Hello Universe!"

    am = ActionModule(loader=None, templar=None, shared_loader_obj=None)
    am._task.args['msg'] = "Hello Earth!"
    am._task.args['verbosity'] = "3"

# Generated at 2022-06-13 09:52:05.349382
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import pytest
    from ansible.executor.play_iterator import PlayIterator
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.playbook.play import Play
    from ansible.inventory.manager import InventoryManager
    from ansible.inventory.host import Host
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.plugins.loader import action_loader

    # setup
    play_source =  dict(
            name = "Ansible Play",
            hosts = 'webservers',
            gather_facts = 'no',
            tasks = [
                dict(action=dict(module='debug', args=dict(msg='Hello World!')))
            ]
        )

# Generated at 2022-06-13 09:52:06.316998
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True

# Generated at 2022-06-13 09:52:07.793543
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule()
    assert am

# Generated at 2022-06-13 09:52:08.593679
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 09:52:20.442237
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Creating an instance of class ActionModule
    action_module_object = ActionModule()

    # Creating expected results
    expected_results = {
        "msg": "Hello world!",
        "_ansible_verbose_always": True,
        "failed": False
    }

    test_task = {}
    test_task["args"] = {}
    test_task["vars"] = {}
    test_task["vars"]["ansible_verbosity"] = 0

    assert action_module_object.run(tmp=None, task_vars=test_task["vars"]) == expected_results

# Generated at 2022-06-13 09:52:30.590567
# Unit test for constructor of class ActionModule
def test_ActionModule():

    msg = '{"ansible_facts": {"foo": "Task is running"}}'
    data = '{"_ansible_verbose_always": true, "changed": false, "msg": "Hello world!"}'
    obj = ActionModule(None)
    obj.set_task(msg)
    assert obj.run() == data

    msg = '{"ansible_facts": {"foo": "Task is running"}, "msg": "Hello world!"}'
    data = '{"_ansible_verbose_always": true, "changed": false, "msg": "Hello world!"}'
    obj = ActionModule(None)
    obj.set_task(msg)
    assert obj.run() == data

    msg = '{"ansible_facts": {"foo": "Task is running"}, "var": "Hello world!"}'

# Generated at 2022-06-13 09:52:31.657686
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule()
    assert isinstance(am, ActionModule)

# Generated at 2022-06-13 09:52:40.526226
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import ansible.plugins.action as action_lib
    import ansible.template as template_lib

    a = action_lib.ActionModule(dict(), dict())
    a._templar = template_lib.Templar(loader=None)
    a._display = action_lib.ActionBase._create_display()

    print(a.run(None, dict()))

    print(a.run(None, dict(msg="Hellow world")))

    print(a.run(None, dict(var="msg")))

    print(a.run(None, dict(var=dict(key="msg"))))

    print(a.run(None, dict(var=dict(key="msg", foo="bar"))))

    print(a.run(None, dict(var="{{" + "msg" + "}}")))

# Generated at 2022-06-13 09:52:42.687476
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(None, None, None).__class__.__bases__[0] == ActionBase