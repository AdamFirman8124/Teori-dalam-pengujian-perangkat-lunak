

# Generated at 2022-06-13 10:42:17.011275
# Unit test for constructor of class ActionModule
def test_ActionModule():
   a = ActionModule(None, None)
   assert a is not None

# Generated at 2022-06-13 10:42:23.832729
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    ############################################################################
    #
    # Run test
    #
    ############################################################################
    from ansible.module_utils import basic

    actionModule = __import__('action_plugins.set_fact', globals(), locals(), ['ActionModule'])
    actionModule = getattr(actionModule, 'ActionModule')
    actionModule = actionModule()

    actionModule._task = object()
    actionModule._task.args = dict()
    actionModule._task.args['a'] = 'b'

    actionModule._templar = basic.AnsibleModule()

    actionModule.run(tmp=None, task_vars=None)

# Generated at 2022-06-13 10:42:30.396020
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    mock_self = {}
    mock_self.__dict__ = {'_task': {'args': {'cacheable': False, 'key1': 'value1', 'key2': 'value2'}}, '_templar': {}}
    mock_self._templar.template = lambda x: x

    result = ActionModule.run(mock_self)

    assert result['ansible_facts'] == {'key1': 'value1', 'key2': 'value2'}
    assert result['_ansible_facts_cacheable'] == False



# Generated at 2022-06-13 10:42:30.991627
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:42:42.855546
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Setup
    action_module = ActionModule()
    action_module._task = mock.Mock()
    action_module._task.args = {'test_key': 'test_value'}
    action_module._templar = mock.Mock()
    action_module._templar.template.return_value = 'test_key'
    action_module._templar.template.return_value = 'test_key'

    # Exercise
    result = action_module.run()

    # Verify
    assert result == {'ansible_facts': {'test_key': 'test_value'}, '_ansible_facts_cacheable': False}
    action_module._templar.template.assert_called_with('test_key')

# Generated at 2022-06-13 10:42:52.141667
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Construct a mock object to test method run
    class ActionModuleMock():
        def __init__(self):
            self.action = 'set_fact'
            self.name = 'set_fact'

    actionModuleMock = ActionModuleMock()

    # Construct a mock object to test with
    class TaskMock():
        def __init__(self):
            self.args = {'fact': 'value'}

    taskMock = TaskMock()

    # Set the return value of mocked get_task_vars.
    def get_task_vars_return():
        return {'fact': 'old_value'}

    # Construct a mock object to test with
    class RunnerMock():
        def __init__(self):
            self.get_task_vars = get_task_vars_return

   

# Generated at 2022-06-13 10:42:54.902925
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import ansible.plugins.action.set_fact as set_fact

    task_vars = dict()
    action = set_fact.ActionModule(task=dict(), connection=dict(), play_context=C.PlayContext(), loader=dict(), templar=C.Templar(variables=task_vars), shared_loader_obj=None)

    action.run(task_vars=dict())

# Generated at 2022-06-13 10:43:05.132901
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    task_vars = dict(ansible_facts=dict(oldvar='oldvalue', othervar='othervalue'))
    am = ActionModule(dict(myvar='myvalue', othervar='newvalue'), 
                      dict(name='foobar', action=dict(module='set_fact', args=dict(myvar='myvalue', othervar='newvalue'))))
    res = am.run(task_vars=task_vars)
    assert 'ansible_facts' in res, res
    assert res['ansible_facts']['myvar'] == 'myvalue', res
    assert '_ansible_facts_cacheable' in res, res
    assert res['_ansible_facts_cacheable'] == False, res



# Generated at 2022-06-13 10:43:07.754171
# Unit test for constructor of class ActionModule
def test_ActionModule():
    a = ActionModule(ActionModule, {})
    a.task = {}
    a.task_vars = {}
    a.tmp = {}

    assert a.TransfersFiles == False

# Generated at 2022-06-13 10:43:15.618546
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import os
    from ansible.played_role import PlayedRole
    from ansible.play import Play
    from ansible.task import Task
    from ansible.inventory.manager import InventoryManager
    from ansible.inventory.host import Host
    from ansible.vars.manager import VariableManager
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.parsing.dataloader import DataLoader
    hosts_path = os.path.dirname(__file__) + "/files/inventory"
    with open(hosts_path) as hosts_file:
        host_data = hosts_file.read()
    inventory = InventoryManager(loader=DataLoader(), sources=[hosts_path])
    variable_manager = Variable

# Generated at 2022-06-13 10:43:21.927274
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule({},{})
    assert type(module) is ActionModule

# ***** Unit tests for run() *****


# Generated at 2022-06-13 10:43:25.711215
# Unit test for constructor of class ActionModule
def test_ActionModule():
    data = '{"_ansible_parsed": true, "invocation": {"module_args": {"cacheable": false, "test1": "value1", "test2": "value2"}}}'
    am = ActionModule(None, data, False, None)

# Generated at 2022-06-13 10:43:33.316375
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # setup test
    class_name = 'ActionModule'

    # create dummy ansible options for testing
    ansible_options = Bunch()
    ansible_options.module_name = 'AnsibleModule'
    ansible_options.module_path = 'ansible.modules.system.ping'
    ansible_options.remote_tmp = 'ansible'
    ansible_options.connection = 'local'
    ansible_options.verbosity = 1
    ansible_options.forks = 1
    ansible_options.check = True
    ansible_options.module_lang = 'py'

    # create test object
    class_object = ActionModule(ansible_options)

    # get method
    method = getattr(class_object, 'run')

    # create test data
    task_vars = dict()

# Generated at 2022-06-13 10:43:39.705412
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # create a dummy action
    am = ActionModule()
    am.datastructure = {}

    # template a valid var name
    v = am._templar.template('{{ this_is_ok }}')

    # check that a valid varname passes
    assert isidentifier(v) == True

    # template a invalid var name
    v = am._templar.template('{{ this-is-bad }}')

    # check that an invalid varname raises an error
    try:
        assert isidentifier(v) == True
        assert False
    except AssertionError as e:
        assert True
    except:
        assert False

# Generated at 2022-06-13 10:43:51.646383
# Unit test for constructor of class ActionModule

# Generated at 2022-06-13 10:44:05.781372
# Unit test for method run of class ActionModule
def test_ActionModule_run():
   action = ActionModule()
   action.name = "test"
   action._task = {"action":{"__ansible_module__":"setup"}}
   action._task.args = {"setup_filter":"ansible_date_time"}

# Generated at 2022-06-13 10:44:08.287506
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_mod = ActionModule(None, None, None, None, None)
    assert isinstance(action_mod, ActionModule)

# Generated at 2022-06-13 10:44:16.265402
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import sys
    import pytest
    # pytest is using sys.exit to signal that a test has failed
    # since the testcases may call sys.exit we first save the
    # previous value to restore it after the test has ran
    prev_sys_exit = sys.exit
    # mock all the imports done in the module under test
    mod_search_path = [ 'ansible.plugins.action.__main__' ]
    for mod in mod_search_path:
        sys.modules[mod] = pytest.Mock()

    # last but not least we need to mock that the module under test is
    # in the module search path
    sys.path.append('/home/travis/build/ansible/ansible/plugins/action')

    from ansible.plugins.action.__main__ import ActionModule

# Generated at 2022-06-13 10:44:26.092403
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import StringIO
    import sys
    import unittest
    sys.path.append('/path/to/ansible')
    import ansible.utils.vars
    from ansible.constants import DEFAULT_JINJA2_NATIVE
    from ansible.module_utils.parsing.convert_bool import boolean
    from ansible.module_utils.six import string_types
    import ansible.constants as C
    from ansible.plugins.action.set_fact import ActionModule
    
    # ActionBase.run returns a dictionary that gets returned by the ansible 'calling' module
    mock_ActionBase_run = {'ansible_facts':{}, '_ansible_facts_cacheable':False}
    # create mock ActionBase class

# Generated at 2022-06-13 10:44:35.399823
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes

    task_vars = {'foo': 'bar'}
    result = {}
    module = basic.AnsibleModule(argument_spec={})
    action = ActionModule(module)
    action.task_vars = task_vars

# Generated at 2022-06-13 10:44:43.675359
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule()
    assert module

# Generated at 2022-06-13 10:44:48.841043
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import ansible.playbook.play_context
    context = ansible.playbook.play_context.PlayContext()
    am = ActionModule(task=dict(args=dict()), connection=dict(), play_context=context, loader=None, templar=None, shared_loader_obj=None)
    assert am

# Generated at 2022-06-13 10:44:51.359377
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(None, 'testHost', 'testUser', 'testSudoPassword')

# Generated at 2022-06-13 10:44:55.622628
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(task=dict(), connection=None, play_context=dict(no_log=False), loader=None, templar=None, shared_loader_obj=None)
    assert isinstance(action_module, ActionBase)

# Generated at 2022-06-13 10:44:56.574256
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert 'ActionModule' in globals()

# Generated at 2022-06-13 10:44:57.529674
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule is not None


# Generated at 2022-06-13 10:45:08.025648
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    from ansible.utils.display import Display
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.task.manager import TaskManager
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.handler import Handler
    from ansible.playbook.role import Role
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    import sys


# Generated at 2022-06-13 10:45:09.481115
# Unit test for constructor of class ActionModule
def test_ActionModule():
    x = string_types()
    t = x()
    t.string_types()


# Generated at 2022-06-13 10:45:20.444033
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = ActionModule()

    def find_needle(result, needle):
        for key, value in result.items():
            if needle in key:
                return True
        for value in result.values():
            if type(value) is dict:
                if find_needle(value, needle):
                    return True
        return False

    test_result = dict()
    test_task = dict()
    test_task['args'] = dict()
    test_task['args']['ansible_os_family'] = 'CentOS'
    test_task['args']['ansible_distribution'] = 'CentOS'
    test_task['args']['ansible_distribution_version'] = '7'
    test_task['args']['ansible_hostname'] = 'localhost.localdomain'


# Generated at 2022-06-13 10:45:28.799618
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """
    Tests for the constructor of class ActionModule
    """
    test_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    # 1. Check that the ActionModule constructor sets self.count to a default of 0
    test1 = ActionModule(None, test_dict)
    assert test1.count == 0

    # 2. Check that the ActionModule constructor sets self.count to a different value
    test2 = ActionModule(None, test_dict, count=7)
    assert test2.count == 7

    # 3. Check that the ActionModule constructor sets self._templateto a default of None
    test3 = ActionModule(None, test_dict)
    assert test3._templar == None

    # 3. Check that the ActionModule constructor sets self._templateto a default of

# Generated at 2022-06-13 10:45:47.679753
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import sys
    # sys.modules['ansible'] = mock.Mock()
    # import ansible.plugins.action.set_fact
    a = ActionModule()
    print ("a.run", a.run)

# Generated at 2022-06-13 10:45:48.721966
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(None, None, {}) is not None

# Generated at 2022-06-13 10:45:56.282100
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action = ActionModule()

    from ansible.vars.hostvars import HostVars
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.utils.vars import combine_vars

    # test case 1 - no args
    result = action.run()
    assert result['failed'] == True
    assert result['msg'] == 'No key/value pairs provided, at least one is required for this action to succeed'

    # test case 2 - one non indentifier arg
    result = action.run(task_vars={}, tmp=None, args={'1a': '1b'})
    assert result['failed'] == True

# Generated at 2022-06-13 10:46:00.432791
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule(
        task=dict(action=dict(module_name='debug', args=dict(msg='bar'))),
        connection=dict(),
        play_context=dict(check_mode=False),
        loader=None,
        templar=None,
        shared_loader_obj=None)

# Generated at 2022-06-13 10:46:08.881981
# Unit test for constructor of class ActionModule
def test_ActionModule():
    template = dict(action=dict(module_name='set_fact', args=dict(new_fact='this is my value for new_fact')))
    action = ActionModule(None, template, {})
    assert action._task.args.get('new_fact') == 'this is my value for new_fact'

# Generated at 2022-06-13 10:46:10.001641
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert isinstance(ActionModule(None, None), ActionModule)


# Generated at 2022-06-13 10:46:11.172727
# Unit test for constructor of class ActionModule
def test_ActionModule():
    mod = ActionModule(None, None)
    assert mod is not None

# Generated at 2022-06-13 10:46:14.781538
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(
        task=dict(args=dict(key1=1, key2=True)),
        connection=dict(),
        play_context=dict(),
        loader=dict(),
        templar=dict(),
        shared_loader_obj=None)

    assert action_module._task == dict(args=dict(key1=1, key2=True))

# Generated at 2022-06-13 10:46:21.526327
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    test_dir = os.path.dirname(os.path.realpath(__file__))
    test_cases_dir = os.path.join(test_dir, 'test_cases')
    # 1. __init__
    # 2. run
    # 3. has_trasferred_files
    # 4. has_failed
    # 5. run_command_safe


# Generated at 2022-06-13 10:46:29.670018
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    am = ActionModule(
        task=dict(
            action=dict(
                module_name='set_fact',
            ),
            args=dict(
                foo='bar',
                other_fact='test'
            ),
            _ansible_version='2.6.1',
        ),
        connection=None,
        play_context=None,
        loader=None,
        templar=None,
        shared_loader_obj=None,
    )
    task_vars = dict(foo='bar')
    result = am.run(task_vars=task_vars)
    assert result['ansible_facts'] == dict(foo='bar', other_fact='test')

# Generated at 2022-06-13 10:47:02.212727
# Unit test for constructor of class ActionModule
def test_ActionModule():
    mod = ActionModule()
    assert mod is not None

# Generated at 2022-06-13 10:47:08.204323
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    temp_instance = ActionModule()
    Facts_store = dict()
    Facts_store['ansible_facts'] = dict()
    Facts_store['ansible_facts']['test_key'] = 'test_value'
    assert temp_instance.run(task_vars=Facts_store) == Facts_store


# Generated at 2022-06-13 10:47:18.328754
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Initialize the ActionModule class
    action = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

    # Convert Scalar values to a dictionary
    task_vars = {}

    # Check if run() returns a valid result
    result = action.run(tmp=None, task_vars=task_vars)

    # Test for Expected Exception
    # Expected Action Fail - test for invalid variable name
    task_vars = {'test': 123}
    with pytest.raises(AnsibleActionFail):
        action.run(tmp=None, task_vars=task_vars)

    # Test for Expected Exception
    # Expected Action Fail - test for invalid value type

# Generated at 2022-06-13 10:47:27.403715
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Get parameters
    # Not need any parameters

    # Target object
    _task = type('ActionModule_Instance', (object,), {})()

    # Ansible Options
    _ansible_options = type('AnsibleOptions_Instance', (object,), {})()
    _ansible_options.connection = None
    _ansible_options.module_path = None
    _ansible_options.forks = None
    _ansible_options.remote_user = None
    _ansible_options.private_key_file = None
    _ansible_options.ssh_common_args = None
    _ansible_options.ssh_extra_args = None
    _ansible_options.sftp_extra_args = None
    _ansible_options.scp_extra_args = None
    _ansible_options

# Generated at 2022-06-13 10:47:36.437732
# Unit test for constructor of class ActionModule
def test_ActionModule():

    import sys
    from ansible.playbook.task import Task
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.inventory.manager import InventoryManager

    variable_manager = VariableManager()
    variable_manager._fact_cache = {}
    variable_manager._host_vars = {}
    variable_manager._group_vars = {}
    variable_manager.extra_vars = {}
    variable_manager.options_vars = {}
    variable_manager._vars_cache = {}
    variable_manager._options = {
        'remoting': 'basic'
    }
    variable_manager.options_vars['ansible_python_interpreter'] = sys.executable
    variable_

# Generated at 2022-06-13 10:47:38.066819
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    AM = ActionModule(None, None)

    AM.run(None, {'_ansible_no_log': True})

# Generated at 2022-06-13 10:47:50.662195
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.action.set_fact import ActionModule
    import ansible.module_utils.parsing.convert_bool
    try:
        reload(ansible.module_utils.parsing.convert_bool)
    except NameError:
        from importlib import reload  # Python 3.4+ only.
        reload(ansible.module_utils.parsing.convert_bool)


# Generated at 2022-06-13 10:47:56.355043
# Unit test for constructor of class ActionModule
def test_ActionModule():
    actionmodule = ActionModule(None, dict(a=1, b=2), None, None, None)
    assert 'a' in actionmodule._task.args
    assert actionmodule._task.args['a'] == 1
    assert 'b' in actionmodule._task.args
    assert actionmodule._task.args['b'] == 2

# Generated at 2022-06-13 10:47:59.983667
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import mock
    import json

    # Constructor test
    module = ActionModule(mock.MagicMock(), mock.MagicMock(), {})
    assert isinstance(module, ActionModule)
    assert module.TRANSFERS_FILES is False

# Generated at 2022-06-13 10:48:07.617038
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # mock module_utils.parsing.convert_bool.boolean, so no connection is required
    # to do the boolean conversion
    def module_utils_parsing_convert_bool_boolean(value, strict=False):
        if value == 'true':
            return True
        else:
            return False

    module_utils_parsing_convert_bool_boolean_old = ActionModule.boolean
    ActionModule.boolean = module_utils_parsing_convert_bool_boolean

    # mock Ansible module class and exit_json method, so no connection is required
    # for testing the exit_json method call
    class AnsibleModule:
        def __init__(self):
            class ExitJson:
                def __init__(self):
                    self.called = False

# Generated at 2022-06-13 10:49:28.940835
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(
        task={
            'args': {'hostname': 'localhost'},
            'name': 'my task',
            'action': 'set_fact',
            'delegate_to': 'localhost'
        },
        connection=None,
        play_context=None,
        loader=None,
        templar=None,
        shared_loader_obj=None
    )
    assert action_module is not None

# Generated at 2022-06-13 10:49:30.304787
# Unit test for constructor of class ActionModule
def test_ActionModule():
    a = ActionModule (None, {})
    assert isinstance(a, object)

# Generated at 2022-06-13 10:49:40.365284
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.module_utils.facts import ansible_distribution
    from ansible.module_utils.facts import ansible_distribution_file_name
    from ansible.module_utils.facts import ansible_distribution_file_parsed
    from ansible.module_utils.facts import ansible_distribution_file_variety

    am = ActionModule({})

    # test with empty ansible_facts
    assert am.run(None, {}) == \
    {
        'changed': False,
        'ansible_facts': {},
        '_ansible_facts_cacheable': False,
    }

    # test with ansible_facts

# Generated at 2022-06-13 10:49:41.231500
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    a = ActionModule()
    print(a.run())

# Generated at 2022-06-13 10:49:46.270183
# Unit test for constructor of class ActionModule
def test_ActionModule():

    module = ActionModule(
        task=dict(action=dict(module='set_fact', args=dict(new_fact='one'))),
        connection=dict(),
        play_context=dict(),
        loader=None,
        templar=None,
        shared_loader_obj=None)

    assert module is not None

# Generated at 2022-06-13 10:49:53.978006
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    import sys
    import os
    import shutil

    lib_path = '/usr/share/ansible'
    if os.path.exists(lib_path):
        sys.path.insert(0, lib_path)

    module_file = os.path.join(os.path.dirname(__file__), '../../module_utils/basic.py')
    shutil.copy(module_file, '/tmp/basic.py')

    #This will create the playbook with the content.
    playbook = 'test_playbook.yml'
    with open(playbook, 'w') as f:
        f.write('---\n')
        f.write('- hosts: 127.0.0.1\n')
        f.write('  vars:\n')

# Generated at 2022-06-13 10:50:03.328754
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule()
    # Testing for no key/value pairs provided
    args = {}
    task = {'args': args}
    res = module.run(task_vars={}, tmp={}, task=task)
    assert_equals(res, {'failed': True, '_ansible_verbose_always': True,
        'msg': 'No key/value pairs provided, at least one is required for this action to succeed'})

    # Testing for no key/value pairs provided
    args = {}
    task = {'args': args}
    res = module.run(task_vars={}, tmp={}, task=task)

# Generated at 2022-06-13 10:50:05.206875
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule(None, None, None, None)
    assert isinstance(am, ActionModule)
    assert hasattr(am, 'run')

# Generated at 2022-06-13 10:50:10.780544
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils import basic
    from ansible.parsing.plugin_docs import read_docstring

    # Create mock module
    module_loader, module_name, path, module_args, loader, tmp, task_vars = basic.setup_module_loader_args('', '','')
    module = basic.AnsibleModule(argument_spec={}, supports_check_mode=True, no_log=True)

    action = AnsibleActionModule(module, None, None, None, '')

    action._task.args = {
        'cacheable': False,
        'valid_name_one': 'value_one',
        'valid_name_two': 'value_two',
        'invalid-name-three': 'value_three',
    }

    res = action.run()

# Generated at 2022-06-13 10:50:15.477703
# Unit test for constructor of class ActionModule
def test_ActionModule():
    a = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    a.add_clean_up_task = None
    a._execute_module = None
    a._add_tqm_variables = None
    a._post_validate_ds = None
    a.run()