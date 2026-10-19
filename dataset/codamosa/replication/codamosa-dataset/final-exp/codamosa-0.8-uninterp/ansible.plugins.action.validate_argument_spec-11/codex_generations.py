

# Generated at 2022-06-13 11:03:28.817022
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = ActionModule(dict(path='/path/to/file'), dict(connection='local', play_context=dict(become=False, become_method=None, become_user=None, become_pass=None, remote_addr=None, remote_user=None, password=None, private_key_file=None, connection=None)))
    # Test case 1 - without argument_spec arg
    with pytest.raises(AnsibleError) as excinfo:
        action_module.run()
    assert '"argument_spec" arg is required in args' in str(excinfo.value)
    # Test case 2 - with argument_spec arg as list

# Generated at 2022-06-13 11:03:31.645262
# Unit test for constructor of class ActionModule
def test_ActionModule():
    test_name = 'test_action_module'
    test_args = {'argument_spec': {'test_arg': {'type': 'string'}}, 'provided_arguments': {'test_arg': 'hello'}}
    am = ActionModule(None, test_name, test_args)

    assert test_name == am._task.name
    assert test_args == am._task.args

# Generated at 2022-06-13 11:03:32.868717
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule()
    assert isinstance(action, ActionModule)

# Generated at 2022-06-13 11:03:38.232846
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # unit test for validate_argument_spec action plugin.

    '''
    The following is an example of how this method might be called
    ArgumentSpecValidator.

    The `validate_argument_spec` action will receive the following in the
    task dict:
    {
        'validate_args_context': {
            'context_key': 'context_value'
        },
        'name': 'validate_arg_spec',
        'argument_spec': {
            'valid_arg_name': {
                'type': 'str',
                'required': True
            }
        }
        'provided_arguments': {
            'valid_arg_name': 'value'
        }
    }
    '''
    from ansible_collections.ansible.netcommon.tests.unit.compat import unittest
   

# Generated at 2022-06-13 11:03:40.744538
# Unit test for constructor of class ActionModule
def test_ActionModule():
    ''' Unit test for the constructor of ActionModule class '''
    action_module = ActionModule()
    assert action_module

# Generated at 2022-06-13 11:03:43.419832
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule(dict(), dict(), False, role_name='test', module_name='test_module')
    assert action.role_name == 'test'
    assert action.module_name == 'test_module'

# Generated at 2022-06-13 11:03:44.221276
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Do nothing for now
    pass

# Generated at 2022-06-13 11:03:46.175004
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Test that the constructor of class ActionModule raises a
    # NotImplementedError exception
    if not isinstance(ActionModule(), ActionModule):
        raise Exception('test_ActionModule(): constructor of ActionModule failed to raise NotImplementedError exception')

# Generated at 2022-06-13 11:03:52.809710
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.plugins import module_utils
    import ansible.plugins.action.validate_argument_spec as action_validate_argument_spec

    # create a module object, with params built from the test object.
    am = ActionModule(
        {'argument_spec': dict(), 'provided_arguments': dict()},
        module_utils.basic.AnsibleModule(
            argument_spec={},
            supports_check_mode=True
        )
    )
    assert isinstance(am, action_validate_argument_spec.ActionModule)



# Generated at 2022-06-13 11:03:55.975052
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Tests that correct initialized object is created
    obj = ActionModule()
    assert type(obj).__name__ == 'ActionModule'

# Generated at 2022-06-13 11:04:11.185627
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Dummy class for passing in as the task's arguments
    class Args(object):
        def __init__(self, arg_dict):
            self._dict = arg_dict

        def __getitem__(self, key):
            return self._dict[key]

    test_task = Args({})

    # Create an instance of the action module class
    action_module = ActionModule(task=test_task, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

    task_vars = {}
    tmp = None

    # Call the run method
    results = action_module._execute_module(module_name='validate_argument_spec', module_args=dict(), task_vars=task_vars, tmp=tmp)


# Generated at 2022-06-13 11:04:12.077422
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule()

    assert module is not None

# Generated at 2022-06-13 11:04:20.031379
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ''' unittest for run method of class ActionModule.
    '''
    action_module = ActionModule()

    # error case: no argument_spec provided
    try:
        action_module.run(tmp=None,
                          task_vars={'a': 'b'})
    except Exception as ex:
        assert '"argument_spec" arg is required in args:' in str(ex)

    # error case: argument_spec is not a dict
    argument_spec = 'not a dict'
    try:
        action_module.run(tmp=None,
                          task_vars={'argument_spec': argument_spec})
    except Exception as ex:
        assert 'Incorrect type for argument_spec, expected dict and got' in str(ex)

    # error case: provided_arguments is not a dict
    provided

# Generated at 2022-06-13 11:04:27.337465
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule()
    assert module.TRANSFERS_FILES == False

    #If no arguments are passed to run, an exception must be thrown
    try:
        module.run()
        assert False
    except Exception as ex:
        assert True

    #If any required arguments are not passed to run, an exception must be thrown
    try:
        module.run(None, {})
        assert False
    except Exception as ex:
        assert True

    #If argument_spec argument is expected to be a dictionary, ActionModule
    #must throw an exception
    try:
        module.run(None, {'argument_spec': 'abc'})
        assert False
    except Exception as ex:
        assert True

    #If provided_arguments argument is expected to be a dictionary,
    #ActionModule must throw an exception

# Generated at 2022-06-13 11:04:28.313891
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert isinstance(ActionModule(), ActionModule)

# Generated at 2022-06-13 11:04:34.050331
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # import modules that are needed
    import ansible.plugins.action
    from ansible.plugins.action.argspec import ActionModule
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText

    args = {
        'argument_spec':{
            'arg1': {'type':'str', 'required':True},
            'arg2': {'type':'int'},
            'arg3': {'type':'dict', 'required':True}
        },
        'provided_arguments':{
            'arg1': 'val_str',
            'arg2': 'val_int'
        }
    }

    # make an instance of the ActionModule class

# Generated at 2022-06-13 11:04:42.413192
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule(dict(), dict())
    assert action._shared_loader_obj == None
    assert action._task == None
    assert action._play_context == None
    assert action._loader == None
    assert action._templar == None
    assert action._connection == None
    assert action._task_vars == None
    assert action._play_context == None
    assert action._registered_variables == None
    assert action._templar._available_variables == None
    assert action._task._role == None
    assert action._task._block == None
    assert action._task._when == None
    assert action._task._delegate_to == None

# Generated at 2022-06-13 11:04:49.187245
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule()
    action = {
        "name": "validate_arg_spec",
        "argument_spec": {
            "argument_spec": {
                "type": "dict",
                "required": True,
                "elements": "dict",
            },
            "provided_arguments": {
                "type": "dict",
                "required": True,
                "elements": "dict",
                "default": {},
            },
        },
    }
    task = {"action": action}

# Generated at 2022-06-13 11:05:01.070903
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Set up the mocks
    class MockErrors(object):

        def __init__(self):
            self.error_messages = ['There was a problem']

    class MockActionModule(ActionModule):
        ''' ActionModule mock '''

        def __init__(self):
            self._task = MockTask()

        def get_args_from_task_vars(self, argument_spec, task_vars):
            '''
            get_args_from_task_vars mock

            :param argument_spec: A dict of the argument spec.
            :param task_vars: A dict of task variables.

            :returns: A dict of values that can be validated against the arg spec.
            '''
            return {'arg_name': 'arg_value'}


# Generated at 2022-06-13 11:05:10.924472
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Init ActionModule class variables
    result = {}
    tmp = None
    task_vars = {}

    # Create a dumb class
    class TestActionModule(object):
        def run(self, tmp, task_vars):
            return result

    # Arrange
    action_module = ActionModule()
    action_module._task = TestActionModule()
    action_module._task.args = {
        'argument_spec': {},
        'provided_arguments': {},
    }

    # Act
    actual = action_module.run(tmp, task_vars)

    # Assert
    assert len(actual) == 2
    assert actual['changed'] == False

    # Arrange

# Generated at 2022-06-13 11:05:28.219565
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    result = ActionModule({}).run({}, {'argument_spec': {'name': {'type': 'str'}, 'state': {'type': 'str', 'default': 'present'}}, 'provided_arguments': {'name': 'ff'}})
    assert result.get('msg') == 'The arg spec validation passed'
    assert not result.get('failed')
    assert not result.get('changed')


# Generated at 2022-06-13 11:05:37.233977
# Unit test for constructor of class ActionModule

# Generated at 2022-06-13 11:05:45.852490
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils.common.validation import SupportedTypes
    from ansible.plugins.action.validate_arg_spec import ActionModule
    from ansible.utils.collection_loader import AnsibleCollectionLoader
    from ansible.vars.manager import VariableManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.task_result import TaskResult
    from ansible.executor.play_iterator import PlayIterator
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.role.include import RoleInclude

# Generated at 2022-06-13 11:05:56.566582
# Unit test for method run of class ActionModule

# Generated at 2022-06-13 11:06:01.692287
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = ActionModule()
    tmp = None
    my_test_vars = dict()
    my_test_vars['my_var'] = 'my_value'
    result = action_module.run(tmp, task_vars=my_test_vars)
    result['failed'] = False
    assert result == {
        'failed': False,
        'changed': False,
        'msg': 'The arg spec validation passed',
        'validate_args_context': {}
    }

# Generated at 2022-06-13 11:06:12.949106
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Create a class with mock attributes for testing
    class Class(object):
        module = None
        _role = None
        _task = None

    # Create mock attributes for the above class with required attributes
    class MockTask(object):
        def __init__(self, args=None):
            self.args = args or {}

    # Valid input
    in1 = {
        "argument_spec": {
            "a": {
                "type": "str",
            },
            "b": {
                "type": "list",
            },
        },
        "provided_arguments": {
            "a": "1",
            "b": ["1", "2", "3"],
        }
    }
    c1 = Class()
    c1._task = MockTask(in1)

# Generated at 2022-06-13 11:06:14.937888
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule()
    assert module is not None
    assert module.TRANSFERS_FILES is False


# Generated at 2022-06-13 11:06:22.341153
# Unit test for method get_args_from_task_vars of class ActionModule
def test_ActionModule_get_args_from_task_vars():
    from ansible.modules.conftest import validate_arg

    spec = dict(argument_spec=dict(name=dict(type='str'), enabled=dict(type='bool')))
    vars = dict(name='foo', enabled=True)

    task_vars = dict(argument_spec=spec)

    action = ActionModule(None, task_vars, None)
    action.connection = None
    action.datastore = None
    action.play = None
    action.playbook = None

    args = action.get_args_from_task_vars(spec['argument_spec'], vars)

    assert args == {'name': 'foo', 'enabled': True}



# Generated at 2022-06-13 11:06:31.949252
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''
    Unit test for the run method of ActionModule class.
    '''
    action = ActionModule()
    result = action.run(tmp={}, task_vars={'argument_spec': {'t': {'required': True}}})
    assert result['failed'] == True
    assert result['msg'] == '"argument_spec" arg is required in args: {}'
    assert result['validate_args_context'] == {}

    result = action.run(tmp={}, task_vars={'argument_spec': {'t': {'required': True}}, 'provided_arguments': 't'})
    assert result['msg'] == 'Incorrect type for argument_spec, expected dict and got <class \'str\'>'


# Generated at 2022-06-13 11:06:40.320111
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Default values
    tmp = None
    task_vars = dict()

    # Make a test case dict
    test_case = dict(
        # add in any default arguments here
        argument_spec=dict(
            test_error=dict(type='list', elements='str', required=True),
            test_default=dict(type='list', elements='str', required=False),
        ),
        provided_arguments=dict(
            # provided arguments
            test_error='this is a string',
            test_default='this is a string',
        ),
    )

    # Make a deep copy of the test_case
    test_case2 = test_case.copy()
    test_case2['provided_arguments'] = test_case2['provided_arguments'].copy()

# Generated at 2022-06-13 11:07:05.901356
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''
    action plugin object testing
    '''
    assert isinstance(ActionModule(), ActionModule)

# Generated at 2022-06-13 11:07:16.023657
# Unit test for constructor of class ActionModule
def test_ActionModule():
    hostvars = {
        'is_valid': True,
        'valid_value': 'valid',
        'valid_nested': ['valid_1', 'valid_2'],
        'valid_nested_dict': {
            'nested_valid_key_1': 'valid_1',
            'nested_valid_key_2': 'valid_2',
        }
    }


# Generated at 2022-06-13 11:07:19.073484
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action = ActionModule()
    action_result = action.run()
    assert isinstance(action_result, dict)
    assert action_result['failed']
    assert action_result['msg'] == '"argument_spec" arg is required in args: {}'

# Generated at 2022-06-13 11:07:26.101328
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.plugins.loader import add_all_plugin_dirs
    from ansible.plugins.action.normal import ActionModule as NormalActionModule

    add_all_plugin_dirs()

    am = ActionModule()
    assert am is not None
    assert isinstance(am, ActionModule)
    assert isinstance(am, NormalActionModule)


# Generated at 2022-06-13 11:07:28.317324
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Unit test for constructor of class ActionModule
    # Returns:
    #     None

    am = ActionModule()
    assert am is not None


# Generated at 2022-06-13 11:07:36.137044
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    spec = {'age': {'type': 'int'}}
    provided_args = {'age': 'four'}
    options = {'task_vars': {}}

    action = ActionModule()
    action.args = {'validate_args_context': {'path': 'foo/bar.yaml'},
                   'argument_spec': spec,
                   'provided_arguments': provided_args}

    result = action.run(tmp=None, task_vars=options['task_vars'])
    assert result['failed'] is True
    assert result['msg'] == 'Validation of arguments failed:\nfoo/bar.yaml:age is expected to be of type int'

    provided_args = {'age': 7}

# Generated at 2022-06-13 11:07:36.543495
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True

# Generated at 2022-06-13 11:07:39.825989
# Unit test for constructor of class ActionModule
def test_ActionModule():
    args = dict(validate_args_context='validate_args_context')
    task = dict(args=args)
    validate_args = ActionModule(task, None)
    assert dict(validate_args_context='validate_args_context') == validate_args._task.args

# Generated at 2022-06-13 11:07:41.697301
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''validate argument spec.'''


# Generated at 2022-06-13 11:07:51.652583
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Test validation success
    action_module = ActionModule({}, {}, {})
    argument_spec_data = {'my_argument': {'type': 'str', 'required': True}}
    provided_arguments = {'my_argument': 'my_argument_value'}
    task_vars = {}
    assert action_module.run(task_vars=task_vars, argument_spec=argument_spec_data, provided_arguments=provided_arguments) == {
        'changed': False,
        'msg': 'The arg spec validation passed'
    }

    # Test validation error
    argument_spec_data = {'my_argument': {'type': 'str', 'required': True}}
    provided_arguments = {'my_argument': 123}

# Generated at 2022-06-13 11:08:53.429838
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.utils.vars import combine_vars
    from ansible.module_utils.common.arg_spec import ArgumentSpecValidator
    from ansible.module_utils.errors import AnsibleValidationErrorMultiple

    module_args = {}
    '''
    {
        "argument_spec": {
            "arg_name": {
                "description": "description",
                "required": true,
                "type": "bool"
            }
        },
        "provided_arguments": {
            "arg_name": "true"
        }
    }
    '''

    # Successful validation
    argument_spec_data = {
        'arg_name': {
            'description': 'description',
            'required': True,
            'type': 'bool'
        }
    }

# Generated at 2022-06-13 11:08:54.715906
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(None, None, None, None)
    assert action_module is not None

# Generated at 2022-06-13 11:09:00.657863
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule()
    # Test 1: If dict key 'argument_spec' is not present in `task.args`, raise AnsibleError
    with module._task.args.update({'argument_spec': None}):
        try:
            assert module.run()
        except AnsibleError:
            pass
    # Test 2: If dict key 'provided_arguments' is not present in `task.args`, it should return a dict with default values

# Generated at 2022-06-13 11:09:09.975895
# Unit test for constructor of class ActionModule
def test_ActionModule():
    ansible_dict = {
        'validate_args_context': {
            'task': 'validate_args',
            'task_path': 'validate_args.yaml',
            'action': 'validate_args_action'
        }
    }

    # Check if all the required attributes are initialized
    actionmodule = ActionModule(dict(), ansible_dict)

    assert isinstance(actionmodule._task, dict)
    assert actionmodule.TRANSFERS_FILES is False
    assert actionmodule._shared_loader_obj is not None
    assert actionmodule._templar is not None
    assert actionmodule._task_vars is not None
    assert actionmodule._loader is not None
    assert actionmodule._templar is not None
    assert actionmodule._filters is not None

# Generated at 2022-06-13 11:09:15.604367
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Create a action module instance
    action_module_instance = ActionModule(load_dl=None, pattern_dl=None,
                                          shared_loader_obj=None, task=None, connection=None, play_context=None,
                                          loader=None, templar=None, shared_module_loader=None)

    # Create a valid argument spec containing only one argument
    argument_spec = dict(test_argument=dict(type='bool', required=True))

    # Create a dict containing the argument to be tested
    provided_arguments = dict(test_argument=True)

    # Setup a mocked task_vars to use in run
    # This mimics a role passing in the arg spec and the arg to be tested to validate_args module

# Generated at 2022-06-13 11:09:18.921354
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # action_module = ActionModule()
    # results = action_module.run(tmp=None, task_vars=None)
    # assert results['failed'] is False
    # assert results['changed'] is False
    # assert results['msg'] is 'The arg spec validation passed'

    pass

# Generated at 2022-06-13 11:09:20.172791
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert issubclass(ActionModule, ActionBase)


# Generated at 2022-06-13 11:09:21.988688
# Unit test for constructor of class ActionModule
def test_ActionModule():
    ''' Unit test for constructor of class ActionModule '''
    action = ActionModule(load_plugins=False)
    assert action is not None


# Generated at 2022-06-13 11:09:29.302313
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor import module_common, play_context
    from ansible.utils.display import Display
    from ansible_collections.sensu.sensu_go.plugins.action import ActionModule

    display = Display()
    display.verbosity = 2

    results_callback = module_common.ResultsCollector()

    task_queue_manager = TaskQueueManager(
        inventory=None,
        variable_manager=None,
        loader=None,
        options=None,
        passwords=None,
        stdout_callback=results_callback,
        run_additional_callbacks=None,
        run_tree=False,
    )


# Generated at 2022-06-13 11:09:35.604138
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ''' Test for method run in class ActionModule '''

    # Test 1: Test a dict of non-required arguments, with a dict of provided arguments
    result = ActionModule.run(ActionModule(), None, {'argument_spec': {'required_to_be_false': {'required': False, 'type': 'bool'},
                                                                        'required_to_be_true': {'required': True, 'type': 'bool'}},
                                                      'provided_arguments': {'required_to_be_false': False, 'required_to_be_true': False}})


# Generated at 2022-06-13 11:11:13.987176
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(None, None)

# Generated at 2022-06-13 11:11:19.406606
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.module_utils.common.arg_spec import ArgumentSpecValidator

    argument_spec_data = {'test1': {'type': 'dict'}, 'test2': {'type': 'str'}}
    validator = ArgumentSpecValidator(argument_spec_data)
    assert validator.argument_spec_data == argument_spec_data

# Generated at 2022-06-13 11:11:23.760124
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.plugins.action.validate_argument_spec import ActionModule

    action_module = ActionModule(None, None, None, None, None)

    assert isinstance(action_module, ActionModule)  # verify the object created is an instance of ActionModule
    #print("test ActionModule: " + str(action_module.__class__.__name__))

# Generated at 2022-06-13 11:11:26.247657
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''This function will perform unit test for constructor of class ActionModule'''
    action_module = ActionModule()
    assert action_module is not None

# Generated at 2022-06-13 11:11:33.057645
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import unittest
    import ansible
    import ansible.plugins.action
    import os

    # The unit test has some magic variables, so let's do some definitions like the code
    # would do
    class AnsibleError(Exception):
        pass

    class AnsibleValidationErrorMultiple(Exception):
        pass

    # Create an instance of the unit tested class
    actionModule = ansible.plugins.action.ActionModule(dict(), dict(), dict())

    # Create a class that will be used to mock the Ansible module behavior
    class ActionBaseMock(object):
        def __init__(self):
            self.results = dict()
            self.results['msg'] = None
            self.results['changed'] = False
            self.results['failed'] = False

        def run(self, tmp, task_vars):
            return self

# Generated at 2022-06-13 11:11:43.078000
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    import unittest
    from ansible.errors import AnsibleError

    class _ActionModule(ActionModule):
        ACTION_WARNINGS = []
        ACTION_DEPRECATIONS = []

        def __init__(self):
            self._task = _Task()

    class _Task():
        def __init__(self):
            self.args = _Args()


# Generated at 2022-06-13 11:11:45.508842
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module_name = 'validate_argument_spec'
    module_path = 'ansible.plugins.action.validate_argument_spec'
    module = ActionModule(module_name, module_path)
    return module

# Generated at 2022-06-13 11:11:53.164223
# Unit test for method get_args_from_task_vars of class ActionModule
def test_ActionModule_get_args_from_task_vars():
    from ansible.module_utils.six import BytesIO
    from ansible.module_utils.six.moves import builtins
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.module_utils._text import to_bytes

    mock_container = builtins.__dict__

    class FileHandle(BytesIO):
        def write(self, arg):
            return BytesIO.write(self, to_bytes(arg, errors='surrogate_or_strict'))

    # Create a 'open' function that behaves like a file
    # We simulate that we are inside a function
    mock_container['open'] = lambda *args, **kwargs: FileHandle()

# Generated at 2022-06-13 11:12:00.293088
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module_args = {}
    module_args['argument_spec'] = {
        'foo': {
            'type': 'str',
            'choices': ['1', '2', '3'],
            'default': '1',
            'required': False
        },
        'bar': {
            'type': 'str',
            'default': '1',
            'required': False
        }
    }
    module_args['provided_arguments'] = {
        'foo': '2',
        'bar': '1'
    }
    result = ActionModule(module_args)
    assert result.run(None, None) is not None


# Generated at 2022-06-13 11:12:00.702735
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule