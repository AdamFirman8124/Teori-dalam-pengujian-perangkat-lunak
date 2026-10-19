

# Generated at 2022-06-13 11:03:26.830729
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # test with no arg
    action_module = ActionModule(None, dict(), False, '/tmp/ansible_vali_argspec_plugin.py', False, None)
    try:
        action_module.run()
    except Exception as e:
        assert isinstance(e, AnsibleError)

    # test with no argument_spec
    action_module = ActionModule(None, dict(provided_arguments={'name': 'h1'}), False, '/tmp/ansible_vali_argspec_plugin.py', False, None)
    try:
        action_module.run()
    except Exception as e:
        assert isinstance(e, AnsibleError)

    # test with argument_spec as string

# Generated at 2022-06-13 11:03:32.031017
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''Test ActionModule.run'''

    class mock_self:
        '''Mock of class ActionModule, used to test its run method'''
        def run(self, tmp=None, task_vars=None):
            '''Mock of ActionModule.run, used to test its run method'''
            res = {'failed': None, 'msg': None, 'changed': None}
            if 'argument_spec' not in self.args:
                res['failed'] = True
                res['msg'] = '\'argument_spec\' arg is required in args: %s' % self.args
                return res
            if not isinstance(self.args.get('argument_spec'), dict):
                res['failed'] = True

# Generated at 2022-06-13 11:03:44.505683
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ''' Unit test for method run of class ActionModule '''
    action_module = ActionModule()
    tmp = {}
    task_vars = {}

    result = action_module.run(tmp, task_vars)
    assert result['failed'] is True
    assert result['msg'] == "The task's `argument_spec` arg is required"

    task_vars['argument_spec'] = {}
    result = action_module.run(tmp, task_vars)
    assert result['failed'] is True
    assert result['msg'] == "The task's `provided_arguments` arg is required"

    task_vars['provided_arguments'] = 'invalid_provided_arguments'
    result = action_module.run(tmp, task_vars)
    assert result['failed'] is True
    assert result['msg']

# Generated at 2022-06-13 11:03:53.424601
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''Test action run'''

    # Linting: noqa: F821, E501
    class MockModule(object):
        ''' Mock of AnsibleModule'''
        def __init__(self, argument_spec, bypass_checks=False):
            self.argument_spec = argument_spec
            self.params = {}
            self.check_mode = False

        def exit_json(self, **kwargs):
            return kwargs

        def fail_json(self, **kwargs):
            return kwargs

    class MockTask(object):
        ''' Mock of AnsibleTask'''
        def __init__(self, args):
            self.args = args

    class MockPlayContext(object):
        ''' Mock of PlayContext'''
        def __init__(self):
            self.remote_addr

# Generated at 2022-06-13 11:03:59.993258
# Unit test for constructor of class ActionModule
def test_ActionModule():
    config = {
        'module_name': 'argument_spec_validation',
        'action': None,
        'action_args': {},
        'task_vars': {},
        'task_args': None,
        'default_vars': {},
    }
    action_module = ActionModule(config, 'argument_spec_validation.yaml', 'testmodule', 'testmodule', {})

    assert isinstance(action_module, ActionModule)


# Generated at 2022-06-13 11:04:07.209533
# Unit test for method get_args_from_task_vars of class ActionModule
def test_ActionModule_get_args_from_task_vars():
    target_object = ActionModule()
    arguments = {
        'required_arg': {
            'type': 'dict',
            'required': True,
        },
        'optional_arg': {
            'type': 'int',
            'required': False,
        }
    }
    task_vars = {
        'required_arg': {
            'key': 'value',
            'key2': '{{ var }}'
        },
        'optional_arg': 1,
        'var': 'test'
    }
    target_result = {
        'required_arg': {
            'key': 'value',
            'key2': 'test'
        },
        'optional_arg': 1
    }

    target_object._templar = Dictable()

    result = target_object.get_args_from

# Generated at 2022-06-13 11:04:12.080521
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Test with invalid args
    try:
        ActionModule({'invalid': 'args'}, 'dummy_connection')
        assert False  # should never get here
    except TypeError as exp:
        assert str(exp).startswith('__init__() takes exactly')

    # Test with valid args
    action = ActionModule({}, 'dummy_connection')
    assert action is not None
    assert isinstance(action, ActionModule)



# Generated at 2022-06-13 11:04:20.031504
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    spec = {
        "name": {"type": "str"},
        "pattern": {"type": "list", "elements": "str"},
        "recurse": {"type": "bool", "default": True},
    }

    # test with dicts of dicts
    data = {
        "name": {"type": "str"},
        "pattern": {"type": "list", "elements": "str"},
        "recurse": {"type": "bool", "default": True},
    }

    # test with list of dicts
    data1 = [
        {"name": {"type": "str"}},
        {"pattern": {"type": "list", "elements": "str"}},
        {"recurse": {"type": "bool", "default": True}},
    ]

    # test with list of strings

# Generated at 2022-06-13 11:04:21.543800
# Unit test for constructor of class ActionModule
def test_ActionModule():
    ''' Unit test to verify the ActionModule constructor.'''
    obj = ActionModule(None, None, None, None)
    assert isinstance(obj, ActionModule)



# Generated at 2022-06-13 11:04:23.060860
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    result = dict()
    module = ActionModule(None, None, None, None, None)
    result = module.run(None, None)
    assert not result

# Generated at 2022-06-13 11:04:38.331885
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.play import Play

    from ansible.playbook.task import Task

    from ansible.vars.manager import VariableManager

    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    options = dict(
        connection='local',
        forks=10,
        become=None,
        become_method=None,
        become_user=None,
        check=False,
        diff=False
    )

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=[])
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    task = Task()
    task.action = 'validate_argument_spec'

# Generated at 2022-06-13 11:04:40.571868
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''
    unit-test method for ActionModule
    '''
    action = ActionModule()
    assert isinstance(action, ActionModule)


# Generated at 2022-06-13 11:04:41.493336
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # TODO
    pass


# Generated at 2022-06-13 11:04:50.188939
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    import sys
    from ansible.errors import AnsibleError
    from ansible.module_utils.common.arg_spec import ArgumentSpecValidator
    from ansible.module_utils.errors import AnsibleValidationErrorMultiple
    from ansible.utils.vars import combine_vars
    from pytest_ansible.module_dispatcher.validate_args import ActionModule

    # Mock class objects
    mock_self = MagicMock()
    mock_self._task = MagicMock()

# Generated at 2022-06-13 11:04:52.308702
# Unit test for constructor of class ActionModule
def test_ActionModule():
    test_action_mod = ActionModule(
        _task=dict(args=dict()),
        connection='local',
        play_context=dict(),
        loader=dict(),
        templar=dict(),
        shared_loader_obj=None)
    assert test_action_mod

# Generated at 2022-06-13 11:04:54.776024
# Unit test for constructor of class ActionModule
def test_ActionModule():
    try:
        ActionModule()
    except:
        raise AssertionError('Constructor of class ActionModule failed')

# Generated at 2022-06-13 11:05:00.033264
# Unit test for constructor of class ActionModule
def test_ActionModule():
    actionModule = ActionModule(
        task=dict(
            action=dict(
                module_name='test_module',
                module_args=dict(
                    argument_spec=dict(
                        test_param=dict(type='str', required=True)
                    ),
                    provided_arguments=dict(test_param='test_value')
                )
            )
        ),
        connection=None,
        play_context=None,
        loader=None,
        templar=None,
        shared_loader_obj=None
    )
    assert isinstance(actionModule, ActionModule)
    assert actionModule._task.action.module_name == 'test_module'

# Generated at 2022-06-13 11:05:05.668804
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''Unit test for constructor of class ActionModule'''

    # pylint: disable=unused-argument
    def run(tmp=None, task_vars=None):
        '''
        Run the module.

        :param tmp: The path to a temporary directory.
        :param task_vars: A dict of task variables.
        :return: An action result dict.
        '''

    ActionModule(dict(), dict(), run)

# Generated at 2022-06-13 11:05:14.582267
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = ActionModule()
    #test run with failed condition
    with pytest.raises(AnsibleError) as execinfo:
        action_module.run()
    assert '"argument_spec" arg is required in args:' in str(execinfo.value)

    with pytest.raises(AnsibleError) as execinfo:
        action_module.run(tmp=None, task_vars={'argument_spec': None})
    assert 'Incorrect type for argument_spec, expected dict and got' in str(execinfo.value)

    with pytest.raises(AnsibleError) as execinfo:
        action_module.run(tmp=None, task_vars={'argument_spec': 'test_data', 'provided_arguments': None})

# Generated at 2022-06-13 11:05:24.699734
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    type_int = 'int'
    type_str = 'str'
    type_list = 'list'
    type_dict = 'dict'
    type_bool = 'bool'
    type_raw = 'raw'
    type_str_or_list = 'str_or_list'
    type_str_or_none = 'str_or_none'

    test_provide_arguments = {
        'arg1': 1,
        'arg2': 'value',
        'arg3': [1, 2, 3],
        'arg4': {'key': 'value'},
        'arg5': True,
        'arg6': ['a', 'b', 1],
        'arg7': None,
        'arg8': 'value',
        'arg9': False
    }


# Generated at 2022-06-13 11:05:30.951997
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True

# Generated at 2022-06-13 11:05:32.249640
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # action plugin does not accept any args nor kwargs
    assert not ActionModule.args

# Generated at 2022-06-13 11:05:34.599409
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule()
    assert(am.TRANSFERS_FILES == False)

# Unit tests for function get_args_from_task_vars

# Generated at 2022-06-13 11:05:35.476620
# Unit test for constructor of class ActionModule
def test_ActionModule():
    result = ActionModule()

# Generated at 2022-06-13 11:05:44.394773
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''Unit test for action plugin class method run

    :param self: An object of class ActionModule
    :param tmp: Deprecated. Do not use.
    :param task_vars: A dict of task variables.
    :return: An action result dict, including a 'argument_errors' key with a
        list of validation errors found.
    '''
    # Create a mock action_base object
    action_base_obj = ActionBase()

    # Create a mock task
    class Task(object):
        def __init__(self):
            self.args = {}

    # Create a mock module_utils.errors.AnsibleValidationErrorMultiple() object
    class Err_Multiple(object):
        def __init__(self):
            self.message = "Ansible Validation Error Multiple"

    # Create a mock module_utils.common

# Generated at 2022-06-13 11:05:49.796710
# Unit test for method get_args_from_task_vars of class ActionModule
def test_ActionModule_get_args_from_task_vars():
    spec = {
        'src': {},
        'dest': {},
        }

    task_vars = {
        'src': '/tmp/foo',
        }

    action = ActionModule(None, {})
    action.set_loader({})
    action._templar = {}
    action._templar.template = lambda x: x

    args = action.get_args_from_task_vars(spec, task_vars)

    if len(spec) != len(args):
        raise AssertionError("Number of arguments returned from task vars does not match length of argument spec.\nspec=%s\nargs=%s\ntask_vars=%s" % (spec, args, task_vars))


# Generated at 2022-06-13 11:05:54.578239
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext

    task = Task()
    task._role = 'test.role'
    task._parent = 'test.parent'

    result = ActionModule(task, PlayContext())
    assert result is not None



# Generated at 2022-06-13 11:06:03.350964
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils.common.validation import ArgumentSpec
    from ansible.modules.packaging.os import os_package
    from ansible.compat.tests.mock import MagicMock
    from ansible.compat.tests.mock import patch

    import pytest

    with patch('ansible_collections.ansible.community.tests.unit.compat.mock.MagicMock') as mock_constructor:
        with patch.object(ActionBase, 'run') as mbase_run:
            mbase_run.return_value = dict(failed=False, changed=False)
            mock_constructor.return_value = MagicMock()
            am = ActionModule()
            am.transfers_files = False
            # arg_spec from the os_package module

# Generated at 2022-06-13 11:06:08.558260
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Inject a mock action loader.
    action_loader = {'data': {'action_plugins': {}}}
    ansible_params = dict({'ANSIBLE_MODULE_ARGS': {}})

    am = ActionModule(action_loader, ansible_params)
    assert isinstance(am, ActionModule)


# Generated at 2022-06-13 11:06:10.931726
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(None, None, None)
    assert isinstance(action_module, ActionModule)

# Generated at 2022-06-13 11:06:31.820213
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Monkeypatch the task loaded by the action plugin
    real_load_task = ActionModule._load_task
    real_task_vars = ActionModule.task_vars
    real_get_vars = ActionModule.get_vars


# Generated at 2022-06-13 11:06:35.231015
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # First import the module_utils
    from ansible.module_utils.basic import AnsibleModule
    module_args = dict(argument_spec=dict(mandatory_name=dict(type='str', required=True)))
    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)
    action = ActionModule(module, module.params)
    action.run(task_vars=dict())

# Generated at 2022-06-13 11:06:36.570068
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule()
    assert isinstance(action_module, ActionModule)



# Generated at 2022-06-13 11:06:47.885377
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Validate that an argument without a default value raises an error
    argument_spec = {
        'first_name': {'required': True},
        'last_name': {'required': True},
        'age': {'required': False, 'default': 0, 'type': 'int'},
    }
    provided_args = {
        'first_name': 'John',
        'last_name': 'Smith',
    }
    args = {
        'argument_spec': argument_spec,
        'provided_arguments': provided_args,
    }
    task = {'args': args}
    action = ActionModule(task, dict())
    result = action.run(dict(), dict())
    assert result['failed']
    assert result['argument_errors'] == ['age is a required value']

# Generated at 2022-06-13 11:06:48.860783
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule()
    assert action is not None

# Generated at 2022-06-13 11:06:50.033062
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule()


# Generated at 2022-06-13 11:06:51.110253
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert False



# Generated at 2022-06-13 11:06:59.909404
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # This is the function that is tested.
    def action_module(args, tmp, task_vars):
        action = ActionModule(task=args.get('task', None),
                              connection=args.get('connection', None),
                              play_context=args.get('play_context', None),
                              loader=args.get('loader', None),
                              templar=args.get('templar', None),
                              shared_loader_obj=args.get('shared_loader_obj', None))
        return action.run(tmp, task_vars)

    import ansible.playbook.task
    from ansible.plugins.loader import module_loader
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.vars.manager import VariableManager

# Generated at 2022-06-13 11:07:01.086034
# Unit test for constructor of class ActionModule
def test_ActionModule():
    mod = ActionModule()
    assert mod is not None


# Generated at 2022-06-13 11:07:10.732067
# Unit test for method get_args_from_task_vars of class ActionModule
def test_ActionModule_get_args_from_task_vars():
    '''
    Unit test for method get_args_from_task_vars of class ActionModule.
    '''
    argument_spec = {
        "name": {
            "required": False,
            "type": "str"
        },
        "state": {
            "default": "present",
            "choices": [
                "present",
                "absent"
            ],
            "type": "str"
        },
        "uuid": {
            "required": False,
            "type": "str"
        }
    }
    task_vars = {
        "name": "test",
        "state": "present",
        "uuid": "2238dc00-4181-4b30-80b4-c5a5f5e5b36e"
    }

# Generated at 2022-06-13 11:07:33.468446
# Unit test for constructor of class ActionModule
def test_ActionModule():
    instance = ActionModule()
    assert instance


# Generated at 2022-06-13 11:07:42.981509
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import json
    import pprint
    import sys

    # get argument_spec data
    argument_spec_data = dict()

    argument_spec_data["argument1"] = {}
    argument_spec_data["argument1"]['type'] = 'dict'

    argument_spec_data["argument2"] = {}
    argument_spec_data["argument2"]['type'] = 'int'

    #get task variables
    task_vars = dict()
    task_vars["argument1"] = dict()
    task_vars["argument1"]["value"] = "text"
    task_vars["argument2"] = -1

    #get task arguments
    task = dict()
    task['args'] = dict()
    task['args']['validate_args_context'] = dict()

# Generated at 2022-06-13 11:07:43.545798
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 11:07:53.466228
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import json
    from ansible.module_utils.common.validation import check_type_dict


# Generated at 2022-06-13 11:08:00.259256
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Create an instance of class ActionModule and assign it to variable am
    am = ActionModule()
    # Set the tmp attribute of am to None
    am.tmp = None
    # Set the task_vars attribute of am to a dictionary
    am.task_vars = dict()
    # Set the _task attribute of am to a dictionary
    am._task = dict()
    # Set the args attribute of the _task attribute of am to a dictionary
    am._task['args'] = dict()
    # Set the argument_spec key of the args attribute of the _task attribute of am to a dictionary
    am._task['args']['argument_spec'] = dict()
    # Set the provided_arguments key of the args attribute of the _task attribute of am to a dictionary
    am._task['args']['provided_arguments'] = dict()
   

# Generated at 2022-06-13 11:08:02.103551
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Create a fake module
    module = ActionModule()
    if  module is not None:
        assert "ActionModule" == module.__class__.__name__

# Generated at 2022-06-13 11:08:10.285869
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ''' Unit test for method run of class ActionModule '''

    import ansible.utils.collection_loader

    class MockedActionBase():
        ''' Class to mock AnsibleActionBase class '''
        def __init__(self, main_file, task_vars):
            self._task = {}
            self._task['args'] = {}
            self._task['args']['argument_spec'] = argument_spec_data
            self._task['args']['validate_args_context'] = {'role_name': 'test_role', 'collection': 'test_collection'}
            self._task['args']['provided_arguments'] = provided_arguments

            self._task['action'] = 'action module'
            self._task['task'] = 'task name'


# Generated at 2022-06-13 11:08:14.737715
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    class ActionModuleTest(ActionModule):
        def __init__(self, args=None, _task=None):
            self._task = _task
            self.connection = None
        def run(self, tmp=None, task_vars=None):
            return super(ActionModuleTest, self).run(tmp, task_vars)
    obj = ActionModuleTest(None, None)
    obj.run()

# Generated at 2022-06-13 11:08:18.334637
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    arg = dict()
    arg['argument_spec'] = {}
    arg['provided_arguments'] = {}
    assert ActionModule(arg, None, './ansible_collections').run() == {'argument_spec_data': {}, 'argument_errors': [], 'changed': False, 'msg': 'The arg spec validation passed'}



# Generated at 2022-06-13 11:08:19.157088
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule()

# Generated at 2022-06-13 11:09:11.357898
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ''' Unit test for method run of class ActionModule '''

    # Note: the test_module argument is a AnsibleModule context object, which
    # we're not actually using in the test. This is ok.
    test_module = mock()

    # action_module_object is an instance of the ActionModule class, which
    # we can mock out as needed to get the results we want.
    action_module_object = ActionModule(test_module, task=dict())

    # Invalid argument specifications are caught
    action_module_object._task.args = {
        'argument_spec': {},
        'provided_arguments': {}
    }
    assert_raises(AnsibleError, action_module_object.run, tmp=None, task_vars=None)

    # Invalid argument specifications are caught
    action_module_object._

# Generated at 2022-06-13 11:09:12.529411
# Unit test for constructor of class ActionModule
def test_ActionModule():

    assert ActionModule is not None

# Generated at 2022-06-13 11:09:15.224984
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule()
    assert action.__class__.__name__ == 'ActionModule', 'object has wrong class name'
    assert hasattr(action, 'run'), 'object does not have run() method'

# Generated at 2022-06-13 11:09:23.690503
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule()
    action_result = {}
    action_result['failed'] = False
    action_result['changed'] = False
    action_result['msg'] = ""
    action_result['validate_args_context'] = {}
    tmp = None
    task_vars = {}
    
    # Test for below type of vaidation error
    # {'path': ['name', 'not', 'valid_data'], 'error': 'invalid_argument',
    # 'message': 'Invalid value for path/name/not/valid_data of type str: False'}


# Generated at 2022-06-13 11:09:30.404641
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    job = dict()
    job['argument_spec'] = {'argument1': {'type': 'str'}, 'argument2': {'type': 'str'}, 'argument3': {'type': 'int'}}
    job['validate_args_context'] = {'task': 'task1.yml', 'role': 'role1'}
    job['provided_arguments'] = {'argument1': 10, 'argument3': 1}
    j = dict()
    j['_ansible_diff'] = False
    j['_ansible_verbose_always'] = True
    j['_ansible_no_log'] = False
    j['task_vars'] = {'arg': 'value', 'var': 'value'}
    j['play_context'] = {'password': 'value'}
    j['play']

# Generated at 2022-06-13 11:09:39.295240
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils.ansible_release import __version__ as ANSIBLE_VERSION
    from ansible.module_utils.six.moves import StringIO
    import ansible.module_utils.connection

    # Mock an ansible.module_utils.basic.AnsibleModule object:

# Generated at 2022-06-13 11:09:41.238255
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''
    Unit test for ActionModule class.
    '''
    obj = ActionModule()
    assert obj

# Generated at 2022-06-13 11:09:51.368981
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = ActionModule(None, None, None, {})

    # empty args
    try:
        assert action_module.run(tmp=None, task_vars=None)
        assert False
    except AnsibleError as e:
        assert str(e) == '"argument_spec" arg is required in args: {}'
        assert True

    # missing argument_spec
    try:
        assert action_module.run(tmp=None, task_vars={'argument_spec': ''})
        assert False
    except AnsibleError as e:
        assert str(e) == '"argument_spec" arg is required in args: {}'
        assert True

    # incorrect argument_spec type

# Generated at 2022-06-13 11:09:58.922139
# Unit test for method get_args_from_task_vars of class ActionModule
def test_ActionModule_get_args_from_task_vars():
    actionbase = ActionBase()
    actionbase._templar = Templating()
    module = ActionModule()
    module._templar = Templating()
    module.action_loader = ActionLoader()
    module._connection = None
    module._task_vars = {}
    module._templar.available_variables = {}

    task_vars = {
        'test_var': 'a templated string: {{ test_var_2 }}',
        'test_var_2': '{{ test_var_3 }}',
        'test_var_3': 'a real value'
    }

    argument_spec = {
        'test_var': {'type': 'str'},
        'test_var_2': {'type': 'str'}
    }

    args = module.get_args_from_task

# Generated at 2022-06-13 11:10:06.221369
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.plugins.action import ActionBase
    from ansible.plugins.action.debug import ActionModule
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    task = ActionBase()
    job_vars = VariableManager()
    loader = DataLoader()

    mod = ActionModule(task, job_vars, loader)
    assert mod is not None

# Generated at 2022-06-13 11:11:43.607661
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    task_vars = {}
    # Test showing that an empty list of provided_arguments is valid.
    action = ActionModule(dict(argument_spec={}), task_vars=task_vars)
    result = action.run(task_vars=task_vars)
    assert not result['failed']
    assert not result['changed']
    assert result['msg'] == 'The arg spec validation passed'

    # Test showing a list of provided_arguments that is valid.
    provided_arguments = {
        'arg1': 1,
        'arg2': '2',
        'arg3': ['thing1', 'thing2'],
        'arg4': [],
        'arg5': {'thing': '3'},
    }

# Generated at 2022-06-13 11:11:45.109178
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.modules.utilities.validate_argument_spec import ActionModule
    action = ActionModule()
    print(action)

# Generated at 2022-06-13 11:11:46.341979
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule({}, {})
    assert action_module is not None

# Generated at 2022-06-13 11:11:54.098966
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task import Task
    from ansible.playbook.role import Role
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory_manager = InventoryManager(loader=loader, sources=[])
    variable_manager.set_inventory(inventory_manager)

    play_context = PlayContext()

# Generated at 2022-06-13 11:11:55.031542
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(task={})

# Generated at 2022-06-13 11:11:57.493806
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(task=dict(args=dict()), connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert action_module

# Generated at 2022-06-13 11:12:05.192734
# Unit test for method get_args_from_task_vars of class ActionModule
def test_ActionModule_get_args_from_task_vars():
    ''' Unit test helper for ActionModule.get_args_from_task_vars() '''
    from ansible.template import Templar
    from ansible.utils.vars import combine_vars

    templar = Templar(loader=None, variables={'t1': 't1_value'})
    action_module = ActionModule(args={}, task=None, connection=None, play_context=None, loader=None, templar=templar, shared_loader_obj=None)
    task_vars = {'dict_var': {'a': 'b'}, 'list_var': ['item 1', 'item 2', 'item 3'], 't1': 't1_value'}

# Generated at 2022-06-13 11:12:19.903304
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Test default constructor
    am = ActionModule()
    result = am.run(None, {'example_arg': 'value'})
    assert result['failed'] == True
    assert 'argument_spec' in result['msg']
    assert result['argument_spec_data'] == None

    # Test constructor with args
    task_args = {'argument_spec': {'example_arg': {'required': True}},
                 'provided_arguments': {'example_arg': 'value'}}
    am = ActionModule(task_args)
    result = am.run(None, {'example_arg': 'value'})
    assert result['failed'] == False

    # Test constructor with keyword args

# Generated at 2022-06-13 11:12:21.992993
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''Unit test for constructor of class ActionModule'''
    # pylint: disable=protected-access
    action_mod = ActionModule({}, {}, False, False)
    assert action_mod._templar is not None
    assert action_mod._loader is not None

# Generated at 2022-06-13 11:12:26.504568
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # construct the argument spec for short name
    short_name_argument_spec = dict(
        argument_spec=dict(required=True, type='dict'),
        provided_arguments=dict(required=True, type='dict')
    )

    # construct the argument spec for full name
    full_name_argument_spec = dict(
        validate_args=dict(
            argument_spec=dict(required=True, type='dict'),
            provided_arguments=dict(required=True, type='dict')
        )
    )

    # test constructor with short name
    provider = ActionModule(short_name_argument_spec, dict(argument_spec=dict(), provided_arguments=dict()))

    # test constructor with full name