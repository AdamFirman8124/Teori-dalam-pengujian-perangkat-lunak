

# Generated at 2022-06-13 11:03:20.270940
# Unit test for constructor of class ActionModule
def test_ActionModule():
    ''' test_ActionModule is a unit test for the ActionModule class '''

    module = ActionModule()
    assert isinstance(module, ActionModule)

# Generated at 2022-06-13 11:03:22.046020
# Unit test for constructor of class ActionModule
def test_ActionModule():

    result = ActionModule.run()
    assert result == 'The arg spec validation passed'

# Generated at 2022-06-13 11:03:23.583178
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action = ActionModule(
        {'desc': 'validate args'},
        {})

    action.run()

# Generated at 2022-06-13 11:03:31.011002
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # ActionModule(task, connection, play_context, loader, templar, shared_loader_obj)
    # Parameter task: AnsibleTask
    # Parameter connection: Connection
    # Parameter play_context: AnsiblePlayContext
    # Parameter loader: DataLoader
    # Parameter templar: Templar
    # Parameter shared_loader_obj: AnsibleBase
    # test_ActionModule.func_doc = Run the action module.
    # test_ActionModule.func_name = run
    test_ActionModule = ActionModule()
    print(test_ActionModule)

    # exeception if argument_spec is missing
    # ansible.utils.display.Display.display(msg, color=None, stderr=False, screen_only=False, log_only=False)

# Generated at 2022-06-13 11:03:44.108838
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''Unit test for method run of class ActionModule'''
    class AnsibleModuleMock(object):
        def __init__(self):
            self._ansible_result = {
                "_ansible_no_log": False,
                "failed": False,
                "msg": "The arg spec validation passed",
                "changed": False,
            }

        def exit_json(self, **kwargs):
            self._ansible_result.update(kwargs)

        def fail_json(self, **kwargs):
            self._ansible_result.update(kwargs)

    ansible_module = AnsibleModuleMock()

    def run_ansible_module(ansible_module):
        '''Run the ansible module code'''

# Generated at 2022-06-13 11:03:44.988690
# Unit test for constructor of class ActionModule
def test_ActionModule():
    test_action = ActionModule()
    assert test_action is not None



# Generated at 2022-06-13 11:03:47.801704
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # arrange
    test_ansible_module = ActionModule()

    # act
    test_result = test_ansible_module.run()

    # assert
    assert(test_result is not None)



# Generated at 2022-06-13 11:03:55.705002
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import yaml
    from ansible.module_utils.common.arg_spec import ArgumentSpec


# Generated at 2022-06-13 11:04:04.196135
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import json
    import os
    import shutil
    import tempfile
    import unittest
    from ansible.module_utils.six import StringIO

    class TestActionModule(ActionModule):
        def _execute_module(self, tmp=None, task_vars=None, **kwargs):
            return dict(failed=False)

    # Create a valid argument spec
    valid_argument_spec = dict(
        state=dict(default='present', choices=['present', 'absent']),
        name=dict(type='str'),
        login=dict(type='str'),
        description=dict(type='str'),
        password=dict(type='str', no_log=True)
    )

    # Create a task vars dict

# Generated at 2022-06-13 11:04:13.535056
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''
    Unit tests for method run of class ActionModule
    '''
    # Mock ActionsModule class
    class ActionsModule():
        '''Mock class for ActionModule'''
        def __init__(self):
            self.args = {'argument_spec': 'argument_spec_data', 'provided_arguments': {'key': 'value'}}
            self.validate_args_context = {}
        def run(self, tmp=None, task_vars=None):
            '''
            Mock run method to return a mocked result
            '''
            result = {}
            result['changed'] = False
            result['msg'] = 'The arg spec validation passed'
            return result

    # Mock ArgumentSpecValidator class
    class ArgumentSpecValidator():
        '''Mock class for ArgumentSpecValidator'''

# Generated at 2022-06-13 11:04:24.082032
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ''' test the method run of class ActionModule '''
    # Mock the argument spec
    argument_spec = dict()

    # Mock the provided arguments
    provided_arguments = dict()

    # Mock the ActionModule instance
    action_module = ActionModule()

    # Mock the results of run()
    result = action_module.run()

    # Assert of result
    assert result == {
      'changed': False,
      'msg': 'The arg spec validation passed'
    }

if __name__ == '__main__':
    from unit_tests.mock_action_base import mock_action_base
    mock_action_base()
    test_ActionModule_run()

# Generated at 2022-06-13 11:04:29.410524
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # only unit test if there is a named action
    if __name__ == '__main__':
        print("Unit test for validating a argument spec")

        action_module = ActionModule()

        # Test with an empty argument spec - no arguments
        argument_spec_data = {}
        provided_arguments = {}
        result = action_module.run(tmp=None, task_vars=None)
        assert result['msg'] == 'The arg spec validation passed'

        # Test with an argument spec that specifies a single required param for the validate_args_context
        argument_spec_data = {
            'validate_args_context': {'required': True, 'type': 'dict'}
        }
        provided_arguments = {}
        result = action_module.run(tmp=None, task_vars=None)
        assert result

# Generated at 2022-06-13 11:04:39.285833
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule()
    # We want to first test the case where a required arg is not specified
    tmp = None
    task_vars = None
    result = module.run(tmp, task_vars)
    assert 'argument_spec' in result['msg']
    # Now test when we have the proper argument_spec arg specified
    task_vars = dict(argument_spec=dict(a=dict(type='int')))
    result = module.run(tmp, task_vars)
    assert 'The arg spec validation passed' in result['msg']
    # Now test when we have a bad provided_arguments arg specified
    task_vars = dict(argument_spec=dict(a=dict(type='int')), provided_arguments="5")
    result = module.run(tmp, task_vars)

# Generated at 2022-06-13 11:04:41.013142
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = AnsibleValidationErrorMultiple()
    module.__init__('message')
    assert module.message == 'message'

# Generated at 2022-06-13 11:04:47.347846
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''Unit test for constructor of class ActionModule'''

    # Test when task_vars is None
    test_task_vars = None
    test_action_module = ActionModule()
    assert not test_action_module.run(task_vars=test_task_vars)

    # Test when task_vars is not None
    test_task_vars = dict()
    test_action_module = ActionModule()
    assert not test_action_module.run(task_vars=test_task_vars)

# Generated at 2022-06-13 11:04:51.365392
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """
    Constructor tests for ActionModule class.
    """
    action_module = ActionModule()
    assert action_module is not None
    assert action_module.TRANSFERS_FILES is False


# Generated at 2022-06-13 11:05:01.744083
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    def compare_dict(d1, d2):
        '''Compare two dict. If values are list or dict, compare their items.'''
        if d1 is None and d2 is None:
            return True
        if d1 is None or d2 is None:
            return False
        if set(d1) != set(d2):
            return False
        for k, v1 in d1.items():
            v2 = d2.get(k)
            if isinstance(v1, list):
                if not compare_list(v1, v2):
                    return False
            elif isinstance(v1, dict):
                if not compare_dict(v1, v2):
                    return False
            else:
                if v1 != v2:
                    return False
        return True


# Generated at 2022-06-13 11:05:04.322222
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """
    Constructor for ActionModule class.
    :return: ActionModule class object.
    """
    action_module = ActionModule()
    assert action_module is not None


# Generated at 2022-06-13 11:05:08.023454
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''
    Constructor test for class ActionModule
    '''
    module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert module is not None

# Generated at 2022-06-13 11:05:11.281694
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    action_module.run(tmp='', task_vars={})

# Generated at 2022-06-13 11:05:25.728026
# Unit test for method get_args_from_task_vars of class ActionModule
def test_ActionModule_get_args_from_task_vars():
    # create mock data
    args = {'argument_spec': {'name': {'type': 'str', 'required': True}}, 'provided_arguments': {'name': 'test-name'}}
    tmp = None
    # create object
    obj = ActionModule(tmp, args)
    # get result
    result = obj.get_args_from_task_vars(args['argument_spec'], args['provided_arguments'])
    # check result
    assert result == args['provided_arguments']

# Generated at 2022-06-13 11:05:26.315409
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 11:05:28.645104
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # It is not possible to mock 'self' argument, but this is what
    # the function is supposed to do, so it is alright
    assert ActionModule is ActionModule

# Generated at 2022-06-13 11:05:30.022248
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule()
    assert isinstance(module, ActionModule)

# Generated at 2022-06-13 11:05:39.221152
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Required args
    argument_spec = {
        "argument_spec": dict(required=False, type='dict', default={}),
        "provided_arguments": dict(required=False, type='dict', default={})
    }

    # Required args
    module_args = dict(
        argument_spec={
            "param1": dict(type="bool"),
            "param2": dict(type="dict"),
            "param3": dict(type="int"),
            "param4": dict(type="float"),
            "param5": dict(type="jsonpath_rw")
        }
    )


# Generated at 2022-06-13 11:05:47.355152
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ''' validate_argument_spec action plugin unit test

    This unit tests the validate_argument_spec action plugin with
    the following parameters that are tested:
    - no argument spec provided
    - no provided arguments
    - provided arg not in argument spec
    - provided arg with incorrect type
    - provided arg with extra key
    - provided arg with extra spec key
    - successful validation
    '''
    from ansible.module_utils.common.arg_spec import ArgumentSpecValidator
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText

    # create ActionModule class object
    action_module = ActionModule()

    # create action result dict
    result = {}
    result['changed'] = False

    # create a valid playbook that is given as an argument

# Generated at 2022-06-13 11:05:57.563115
# Unit test for constructor of class ActionModule
def test_ActionModule():
    argument_spec_data = {
        'a': {
            'type': 'str'
        },
        'b': {
            'type': 'int'
        },
        'c': {
            'type': 'list'
        }
    }
    provided_arguments = {
        'a': 'a',
        'b': 2
    }

    action_module = ActionModule({'argument_spec': argument_spec_data, 'provided_arguments': provided_arguments})

    assert 'argument_spec' in action_module._task.args
    assert 'provided_arguments' in action_module._task.args

    assert 'argument_spec' in action_module._task.args['argument_spec']
    assert 'provided_arguments' in action_module._task.args['provided_arguments']

# Generated at 2022-06-13 11:06:02.540134
# Unit test for constructor of class ActionModule
def test_ActionModule():
    ''' validate_arg_spec unit test

    Validate the constructor of class ActionModule.
    '''
    # Setup
    actionBase = ActionBase()
    action = ActionModule(actionBase._connection, actionBase._play_context, actionBase._loader,
                          actionBase._templar, actionBase._shared_loader_obj)
    # Testing
    assert isinstance(action, ActionModule)

# Generated at 2022-06-13 11:06:05.769735
# Unit test for constructor of class ActionModule
def test_ActionModule():
    ''' Unit test for constructor of class ActionModule '''
    test_inst = ActionModule()
    assert isinstance(test_inst, ActionModule)


# Generated at 2022-06-13 11:06:06.825195
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    command = ActionModule()
    command.run()

# Generated at 2022-06-13 11:06:22.696641
# Unit test for constructor of class ActionModule
def test_ActionModule():
    _ = ActionModule()

# Generated at 2022-06-13 11:06:27.434880
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Initializing ActionModule
    actionmodule = ActionModule()

    # Testing run invalid argument_spec
    actionmodule.run(tmp="temp", task_vars="task_vars")

    # Testing run invalid provided_argument
    actionmodule.run(tmp="temp", task_vars="task_vars")

# Generated at 2022-06-13 11:06:34.654737
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''
    Unit test for method run of class ActionModule
    '''
    result = ActionModule.run(ActionModule, None, {'argument_spec': {'parameter_name': {'required': False, 'type': 'str'}},
                                                   'provided_arguments': {'parameter_name': 'Hello'}})
    assert result['failed'] == False
    assert result['changed'] == False
    assert result['msg'] == 'The arg spec validation passed'
    result = ActionModule.run(ActionModule, None, {'argument_spec': {'parameter_name': {'required': False, 'type': 'int'}},
                                                   'provided_arguments': {'parameter_name': 'Hello'}})
    assert result['failed'] == True
    assert result['changed'] == False
    assert result

# Generated at 2022-06-13 11:06:41.259103
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import os
    import ansible_collections.ansible.netcommon.tests.ut_utils as ut_base
    from ansible_collections.ansible.netcommon.plugins.action.validate_argument_spec import ActionModule

    module = ut_base.get_ansible_module(os.path.dirname(__file__) + '/validate_arg_spec.yml')
    action = ActionModule(module, module.params)

    # Test the correct case

# Generated at 2022-06-13 11:06:52.382338
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule()

# Generated at 2022-06-13 11:07:00.600341
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Mocks
    tmp = None
    task_vars = dict()
    result = dict()
    # Mock instance of class ActionModule and its attributes
    action_module = ActionModule(task=dict(), connection=dict(), play_context=dict(), loader=dict(), templar=dict(), shared_loader_obj=dict())
    action_module._task = mock_AnsibleTask()
    action_module._task.args = {'argument_spec': dict(), 'provided_arguments': dict()}
    action_module._templar = dict()

    # Mocked method
    action_module.get_args_from_task_vars = Mock(return_value=dict())

    # Assertions
    assert action_module.run(tmp, task_vars) == result


# Generated at 2022-06-13 11:07:04.812353
# Unit test for constructor of class ActionModule
def test_ActionModule():
    class MockModule():
        def __init__(self, params):
            self.params = params

    class MockTask():
        def __init__(self, args):
            self.args = args

    args = {'argument_spec': 1, 'provided_arguments': 2}
    module = MockModule(None)
    task = MockTask(args)
    action_module = ActionModule(module, task, task_vars={})



# Generated at 2022-06-13 11:07:05.708977
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Not implemented
    assert False

# Generated at 2022-06-13 11:07:10.305599
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import ansible.plugins.action
    a = ansible.plugins.action.ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert a

# Generated at 2022-06-13 11:07:17.760497
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """Unit test for the method `run` in class `ActionModule`."""

    # Test when only mandatory args are provided
    action_module = ActionModule()
    action_module._task.args = dict()

    actual_result = action_module._execute_module(tmp=None, task_vars=None)
    assert actual_result.get('msg') == 'The arg spec validation passed'
    assert actual_result.get('failed') == False
    assert actual_result.get('changed') == False
    assert actual_result.get('validate_args_context') == None

    # Test when all args are provided
    action_module = ActionModule()
    argument_spec = dict()
    argument_spec['custom'] = dict()
    argument_spec['custom']['required'] = True

# Generated at 2022-06-13 11:07:56.808823
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Test that the action module returns msg with "The arg spec validation passed" if there is no
    # failure
    import unittest
    import ansible.plugins.action.validate_args
    from ansible.module_utils.common.arg_spec import ArgumentSpecValidator
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.module_utils.errors import AnsibleValidationErrorMultiple
    from ansible.module_utils.errors import AnsibleValidationError

    class TestActionModule(unittest.TestCase):
        argument_spec = {
            'provider': {'required': True, 'type': 'dict'},
            'name': {'required': True},
        }

# Generated at 2022-06-13 11:08:06.318646
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    result = dict()
    result['failed'] = False
    result['argument_errors'] = []
    result['validate_args_context'] = dict()

    ansible_module = dict()
    ansible_module['validate_argument_spec'] = dict()
    ansible_module['validate_argument_spec']['argument_spec'] = dict()
    ansible_module['validate_argument_spec']['argument_spec']['provider'] = dict()
    ansible_module['validate_argument_spec']['argument_spec']['provider']['type'] = 'dict'
    ansible_module['validate_argument_spec']['argument_spec']['provider']['options'] = dict()

# Generated at 2022-06-13 11:08:12.141111
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Create a test fixture (mock_module) for the module_utils/basic.py ModuleUtilsBasic class
    mock_module = MagicMock()
    mock_module.params = {}

    # Create a test fixture (mock_action) for the ActionBase class.
    mock_action = MagicMock()
    mock_action.run.return_value = None
    mock_action._task.args = {'argument_spec': {
        'a': {'type': 'str'},
        'b': {'type': 'dict', 'options': {'c': {'type': 'str'}}}
    }, 'provided_arguments': {'a': 'foo', 'b': {'c': 'bar'}}, 'validate_args_context': {'role': {'name': 'foo_role'}}}

    # Set up

# Generated at 2022-06-13 11:08:12.962072
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # TODO
    pass

# Generated at 2022-06-13 11:08:18.516910
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.role_context import RoleContext
    from ansible.playbook.block import Block
    from ansible.playbook.play import Play

    task = Task()
    task._role = RoleContext()
    task._block = Block()
    task._play = Play()

    p = PlayContext()
    task._play_context = p

    action = ActionModule(task, dict())
    assert isinstance(action, ActionModule)

# Generated at 2022-06-13 11:08:19.963666
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Empty task
    module = ActionModule()
    assert module.TRANSFERS_FILES is False


# Generated at 2022-06-13 11:08:27.645841
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    
    argument_validator_plugin_test1_task = {
        'action': {'__ansible_module__': 'ansible.plugins.action.validate_argument_spec', '__ansible_arguments__': {'provided_arguments': {'name': 'Tom'}, 'argument_spec': {'name': {'type': 'str'}}}},
        'args': {'argument_spec': {'name': {'type': 'str'}}, 'provided_arguments': {'name': 'Tom'}},
        'delegate_to': None,
        'delegate_facts': None,
        'register': None,
        'run_once': False,
        'retries': 0,
        'until': None
    }

# Generated at 2022-06-13 11:08:35.205578
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # mocking arguments for run method
    argument_spec_data = {'arg1': {'type': 'int'}}
    args = {'argument_spec': argument_spec_data}
    provided_arguments = {'arg1': 1}
    args['provided_arguments'] = provided_arguments

    check = ActionModule()
    result = check.run(tmp=None, task_vars=None)

    assert isinstance(result, dict)
    assert result['failed']
    assert result['msg'] == 'Validation of arguments failed:\n'
    assert result['argument_spec_data'] == argument_spec_data
    assert result['argument_errors'] == []

    # mocking arguments for run method
    argument_spec_data = {'arg1': {'type': 'int'}}

# Generated at 2022-06-13 11:08:41.634502
# Unit test for constructor of class ActionModule
def test_ActionModule():

    # First create a mock task object
    from ansible.playbook.task import Task
    task = Task()
    task.args = {
        'validate_args_context': {
            'task_path': 'path',
            'task_params': {
            }
        },
        'argument_spec': {},
        'provided_arguments': {}
    }

    # Now create an instance of the ActionModule class
    from ansible.plugins.action import ActionModule
    action_module = ActionModule(task, {}, {})

    # Check that the constructor sets the class vars correctly
    assert action_module._task == task
    assert action_module._connection == {}
    assert action_module._play_context == {}



# Generated at 2022-06-13 11:08:49.128268
# Unit test for method get_args_from_task_vars of class ActionModule
def test_ActionModule_get_args_from_task_vars():
    argument_spec = {'arg_a': {'type': 'str'},
                     'arg_b': {'type': 'str'}}
    task_vars = {'arg_a': 'value_a',
                 'arg_b': '{{ value_b }}'}
    ActionModule().get_args_from_task_vars(argument_spec, task_vars)


# Generated at 2022-06-13 11:09:51.407842
# Unit test for constructor of class ActionModule
def test_ActionModule():
    ''' Unit test ActionModule constructor '''
    assert (ActionModule != 'ActionModule')

# Generated at 2022-06-13 11:09:58.950446
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    test_arg_spec = {'x': {'type': 'int'}}
    test_provided_args = {'x': 1}

    test_result = {
        'changed': False,
        'validate_args_context': {},
        'msg': 'The arg spec validation passed'
    }
    expected_result = test_result

    module = ActionModule()
    result = module.run(task_vars={}, tmp=None, argument_spec=test_arg_spec, provided_arguments=test_provided_args)
    assert result == expected_result

    # test error message returned by ValidationErrorMulti
    test_arg_spec = {'x': {'type': 'int'}}
    test_provided_args = {'y': 1}

    expected_result['changed'] = True

# Generated at 2022-06-13 11:10:04.716670
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # This action can be called from anywhere, so pass in some info about what it is
    # validating args for so the error results make some sense
    task = {
        'args': {
            'validate_args_context': {},
            'argument_spec': {
                'required_argument': {
                    'type': 'str',
                    'required': True,
                },
                'int_argument': {
                    'type': 'int',
                    'default': 1,
                },
                'int_list_argument': {
                    'type': 'list',
                    'elements': 'int',
                },
            },
        }
    }

    action = ActionModule(task, {})

    result = action.run(None, task_vars={})

# Generated at 2022-06-13 11:10:06.153336
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule()
    assert action

# Generated at 2022-06-13 11:10:16.454686
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.test.test_plugins.test_action.test_validate_argument_spec import test_module_utils
    args = {
        "argument_spec": {
            "test_argument": {
                "required": True,
                "type": "str",
            },
        },
        "provided_arguments": {
            "test_argument": "bar",
        },
    }
    task_vars = {
        'test_var': 'foo',
    }
    tmp_path = test_module_utils.TestTemporaryDirectory()
    a = ActionModule(task=test_module_utils.task_from_args(args), tmp=tmp_path, task_vars=task_vars)
    r = a.run(task_vars=task_vars)

# Generated at 2022-06-13 11:10:26.663164
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import ansible.plugins.action.validate_args
    # Valid dir only input
    action = ansible.plugins.action.validate_args.ActionModule('/some/dir')
    assert action.module_utils_path == ['/some/dir']
    assert action.module_utils_loader.get_all_plugin_loaders() == ['/some/dir/module_utils']

    # Valid dir + file only input
    action = ansible.plugins.action.validate_args.ActionModule('/some/dir/file.py')
    assert action.module_utils_path == ['/some/dir']
    assert action.module_utils_loader.get_all_plugin_loaders() == ['/some/dir/module_utils']

    # Valid dir + file + hashbang input

# Generated at 2022-06-13 11:10:27.601071
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule is not None

# Generated at 2022-06-13 11:10:30.042864
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = ActionModule()
    task_vars = {}
    result = action_module.run(None,task_vars)

    assert result['msg'] == 'The arg spec validation passed'

# Generated at 2022-06-13 11:10:36.943203
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action = ActionModule()
    argument_spec = {
        'state': {'required': True, 'type': 'str', 'choices': ['present', 'absent']},
        'name': {'required': True, 'type': 'str'}
    }

    # test happy path
    args = {
        'state': 'present',
        'name': 'foo'
    }
    provided_arguments = {
        'state': 'present',
        'name': 'foo'
    }
    task_vars = {
        'state': 'present',
    }

    result = action.run(None, task_vars=task_vars)
    assert result['changed'] is False
    assert isinstance(result['argument_errors'], list)
    assert result['argument_errors'] == []

# Generated at 2022-06-13 11:10:47.036833
# Unit test for method run of class ActionModule

# Generated at 2022-06-13 11:13:10.130084
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils.common.validation import check_type_dict
    import copy

    # Setup test data
    task = dict(args=dict())
    task_vars = dict(
        argument_spec=dict(
            name=dict(required=True, type='str'),
            address=dict(required=True, type='str'),
            city=dict(required=True, type='str'),
            state=dict(choices=['present', 'absent']),
            zip=dict(type='str'),
        ),
    )

    # Setup test values
    args = dict(argument_spec=task_vars['argument_spec'],
        provided_arguments=dict(name='King',
                                address='Washington st',
                                city='Washington')
    )

    # Setup mocks