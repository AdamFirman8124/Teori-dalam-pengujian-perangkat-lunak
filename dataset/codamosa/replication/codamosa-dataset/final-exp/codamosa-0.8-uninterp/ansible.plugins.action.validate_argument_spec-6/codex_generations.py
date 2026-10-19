

# Generated at 2022-06-13 11:03:18.066112
# Unit test for constructor of class ActionModule
def test_ActionModule():
    a = ActionModule(
        task=dict(),
        connection=dict(),
        play_context=dict(),
        loader=dict(),
        templar=dict(),
        shared_loader_obj=dict()
    )
    # If a is not an instance of ActionModule, this would result in a TypeError
    a.run()

# Generated at 2022-06-13 11:03:21.557550
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    params = {
        'argument_spec': {},
        'provided_arguments': {'key': 'value'}
    }
    action_module = ActionModule(dict(), params)
    action_module.run()

# Generated at 2022-06-13 11:03:29.666694
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Disabling pylint because this is a test module, not an actual class and it's
    # not worth the effort to create a mock object for this.
    # pylint: disable=R0904
    import collections

    # import and instantiate module
    module = __import__('ansible.modules.network.system', fromlist=['system'])
    system_module = getattr(module, 'system')
    action_module = ActionModule(system_module, dict(), False, None, None, dict())

    # create mock data, objects and functions
    valid_value = {'type': 'str', 'required': True}
    valid_key = 'valid_key'
    error_message_1 = 'validation error 1'
    error_message_2 = 'validation error 2'

    validation_result = collections.namedtuple

# Generated at 2022-06-13 11:03:43.548600
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''
    Unit test - use the same role to get the argument spec and to run the validation.
    This test is run when called as the main function of this file.
    :return:
    '''
    import shutil
    import tempfile
    import unittest
    from ansible.compat.tests.mock import patch
    from ansible.compat.tests.mock import Mock

    from ansible.compat.tests import unittest
    from ansible.compat.tests import skipIf
    from ansible.playbook.play_context import PlayContext

    from ansible.modules.network.nxos import validate_argument_spec
    from ansible.errors import AnsibleError

    # The module only works for Ansible 2.6 and higher

# Generated at 2022-06-13 11:03:48.782652
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    fixture_result = dict(failed=False, changed=False, msg='The arg spec validation passed', _ansible_verbose_always=True)

    fixture_task_vars = dict()

    def check_result(actual_result, expected_result):
        assert actual_result == expected_result

    import copy
    action_base = copy.deepcopy(ActionModule(None, dict(argument_spec=dict(), provided_arguments=dict()), 'test_template'))
    action_base._templar = 'test_templar'
    action_base._task = 'test_task'
    action_base._loader = 'test_loader'
    action_base._connection = 'test_connection'
    action_base._play_context = 'test_play_context'


# Generated at 2022-06-13 11:03:50.533110
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = ActionModule()
    result = action_module.run(None, None)
    assert result['msg'] == 'The arg spec validation passed'

# Generated at 2022-06-13 11:03:51.682421
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule is not None

# Generated at 2022-06-13 11:03:59.646774
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action = ActionModule(
        task=dict(
            args=dict(
                argument_spec=dict(
                    interface_name=dict(type='str', required=True)
                ),
                provided_arguments=dict(interface_name='lo'),
                validate_args_context=dict(resource_name='some_resource', task_name='some_task_name')
            )
        )
    )

    result = action.run(task_vars=dict())
    assert not result['failed']
    assert result['msg'] == 'The arg spec validation passed'



# Generated at 2022-06-13 11:04:02.308438
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule(dict(), dict())
    assert isinstance(action, ActionModule)
    assert hasattr(action, 'run')
    assert hasattr(action, 'get_args_from_task_vars')


# Generated at 2022-06-13 11:04:03.384289
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(None, None)
    assert action_module is not None

# Generated at 2022-06-13 11:04:14.931991
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # test run
    act_mod_obj = ActionModule()
    act_mod_obj.transfers_files = False
    argument_spec_data = {'x': {'type': 'list'}, 'y': {'type': 'int'}}
    provided_arguments = {'x': [1, 2], 'y': '5'}
    act_mod_obj.task_vars = {'x': [1, 2], 'y': '5'}
    act_mod_obj._task.args = {'argument_spec': argument_spec_data,
                              'provided_arguments': provided_arguments}

# Generated at 2022-06-13 11:04:20.225505
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible import context
    from ansible.module_utils._text import to_bytes

    exec_mode = context.CLIARGS['executable']
    exec_mode = to_bytes(exec_mode, errors='strict')

    obj = ActionModule(None, None)
    obj._connection = None
    obj._task = None
    obj._low_level_runner_after_trans = None
    obj._shared_loader_obj = None
    obj._play_context = None
    obj._loader = None
    obj._templar = None
    obj._task_vars = None
    obj._start_at_task = None
    obj._task_ds = None
    obj._task_ds['name'] = 'test_case'
    obj._task_ds['action'] = 'test_case'
    obj._task

# Generated at 2022-06-13 11:04:23.756227
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # mock task class
    class FakeTask():
        args = {"validate_args_context": {}}

    # mock task
    task = FakeTask()

    # These attributes are expected by ActionModule
    action = ActionModule(task, {}, {}, [])

    assert action.TRANSFERS_FILES is False


# Generated at 2022-06-13 11:04:29.164460
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    argument_spec = {
        'test_arg': {'type': 'str'},
        'test_arg2': {'type': 'list'},
    }

    provided_arguments = {
        'test_arg': 'good argument'
    }

    # Expected result of validation
    validation_result = {
        'validation_result': {
            'failed': False,
            'msg': 'The arg spec validation passed',
            'validate_args_context': {},
        }
    }

# ansible/test/units/plugins/action/validate_argument_spec.py
    task_vars = dict()

    # Create instance of class ActionModule and call method run
    action_module = ActionModule()
    result = action_module.run(task_vars=task_vars)
    #

# Generated at 2022-06-13 11:04:38.990268
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''
    Unit test for method run of class ActionModule
    '''

    # Construct a mock object of class ActionBase
    action_base = ActionBase()

    # Construct a mock object of class ActionModule
    action_module = ActionModule()

    # Construct a mock object of class Task
    task_obj = MagicMock()
    task_obj.action = action_module
    task_obj.async_val = 0
    task_obj.notify = []
    task_obj.noop_val = False
    task_obj.run_once = False

    def mock_run_once():
        '''
        Mock method run_once of class Task
        '''
        task_obj.run_once = True

    task_obj.run_once = mock_run_once

    # Construct a mock object of class TaskExecutor

# Generated at 2022-06-13 11:04:47.604585
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = ActionModule()

    module_input = dict(
        argument_spec=dict(
            argument_name=dict(
                required=True,
                aliases=['alias for name_of_arg'],
                type='bool'
            )
        ),
        provided_arguments=dict(
            argument_name='not true'
        ),
        validate_args_context=dict(
            role_name='test_role',
            entry_point_name='test_entry_point'
        )
    )

    # test run() method if provided_arguments dict has a key that is not defined in argument_spec dict
    action_module.run(module_input, task_vars={'argument_name': 'test_name_of_arg'})

# Generated at 2022-06-13 11:05:00.531028
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    task_vars = dict()
    global_args = dict()
    args = dict()
    spec_args = dict()

    class MockTask(object):
        def __init__(self):
            self.args = args

    class MockPlayContext(object):
        def __init__(self):
            self.global_vars = global_args

    class MockUtils(object):
        def __init__(self):
            self.Template = None

    class MockModuleUtils(object):
        def __init__(self):
            self.template = MockTemplate()
            self.basic = MockBasic()

    class MockTemplate(object):
        def __init__(self):
            self.template = None

        def template(self, args):
            return args


# Generated at 2022-06-13 11:05:10.361988
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ''' Unit test for method ActionModule.run
    '''

    # Since ActionModule is an abstract class, we need to create a subclass
    class ConcreteActionModule(ActionModule):
        def get_args_from_task_vars(self, argument_spec, task_vars):
            return {}


# Generated at 2022-06-13 11:05:17.669546
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Creating the arguments for the mocked module
    argument_spec = {
        "argument_spec": {
            "required": True,
            "type": "dict"
        },
        "provided_arguments": {
            "required": True,
            "type": "dict"
        }
    }

    # Assign test_module to the mocked module
    test_module = ActionModule()

    # Mock the task argument and set the argument_spec argument to an empty
    # dict
    test_module._task.args = {}
    test_module._task.args['argument_spec'] = {}

    # Create a dict with name and key value and set the provided_arguments
    # argument to it
    args = {}
    args['name'] = "test"
    test_module._task.args['provided_arguments'] = args

   

# Generated at 2022-06-13 11:05:21.030529
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(dict(), dict(), False,
                        connection=dict(),
                        play_context=dict(),
                        loader=None,
                        templar=None,
                        shared_loader_obj=None)

# Generated at 2022-06-13 11:05:28.251407
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # action_module = ActionModule()
    # assert action_module
    pass

# Generated at 2022-06-13 11:05:37.274126
# Unit test for method get_args_from_task_vars of class ActionModule
def test_ActionModule_get_args_from_task_vars():
    class Object(object):
        def __init__(self):
            self.action = ActionModule()

    c = Object()
    # test empty argument spec
    assert c.action.get_args_from_task_vars({}) == {}
    # test one argument
    assert c.action.get_args_from_task_vars({'toto': {}}) == {}
    # test one argument with a value
    assert c.action.get_args_from_task_vars({'toto': {}}, {'toto': 'value'}) == {'toto': 'value'}
    # test one argument with a value but task_vars is None
    assert c.action.get_args_from_task_vars({'toto': {}}, task_vars=None) == {}
    # test multiple arguments


# Generated at 2022-06-13 11:05:44.041681
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Setup mock arguments
    mock_task = {'args': {'argument_spec': 'test_argument_spec', 'provided_arguments': 'test_provided_arguments'}}
    mock_loader = 'test_loader'
    mock_templar = 'test_templar'

    # Construct our ActionModule to be tested
    am = ActionModule(mock_task, mock_loader, mock_templar)

    # Check our results
    # TODO: Add more asserts?
    assert am._task.args['argument_spec'] is mock_task['args']['argument_spec']


# Generated at 2022-06-13 11:05:45.123458
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action = ActionModule()
    assert type(action) == ActionModule
    print('Tested method run of class ActionModule')

# Generated at 2022-06-13 11:05:50.100868
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    result = dict(
        _ansible_verbosity=2,
        ansible_verbosity=2,
        ansible_check_mode=False,
        _ansible_check_mode=False,
        ansible_diff=False,
        _ansible_diff=False,
        _ansible_no_log=False,
        exception=AnsibleValidationErrorMultiple({'msg': 'A message', 'errors': ['error1', 'error2']}),
        changed=False,
        original_message='The arg spec validation failed'
    )

    assert result is not None

# Generated at 2022-06-13 11:05:59.725592
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.module_utils.common.arg_spec import ArgumentSpec
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play

    host = 'helloworld'
    hostname = 'hostname'
    port = 1023
    remote_user = 'root'

    play_context = PlayContext()
    play_context.network_os = hostname
    play_context.remote_addr = host
    play_context.port = port
    play_context.remote_user = remote_user
    play_context.become = None
    play_context.become_method = None
    play_context.become_user = None
    play_context.check_mode = False

    task_v

# Generated at 2022-06-13 11:06:10.221650
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = ActionModule(load_arg_spec=ActionModule._load_arg_spec)
    temp_task_vars = {
        'argument_spec': {
            'foo': {
                'type': 'str'
            }
        }
    }
    temp_args = {
        'provided_arguments': {
            'foo': 'bar'
        }
    }
    action_module._task.args = temp_args
    assert action_module.run(task_vars=temp_task_vars) == {
        'changed': False,
        'validate_args_context': {},
        'msg': 'The arg spec validation passed',
    }


# Generated at 2022-06-13 11:06:13.196663
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule(dict(argument_spec=dict(), provided_arguments=dict()),{})
    module.run(task_vars=dict())

# Generated at 2022-06-13 11:06:15.420466
# Unit test for constructor of class ActionModule
def test_ActionModule():
    spec = {'name': {'type': 'str'}}
    validator = ArgumentSpecValidator(spec)
    assert validator.argument_spec == spec



# Generated at 2022-06-13 11:06:23.277689
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module_run = ActionModule()
    setattr(module_run, '_task', {})
    setattr(module_run, '_templar', {})
    setattr(module_run._task, 'args', {})
    setattr(module_run._task.args, 'argument_spec', {})
    setattr(module_run._task.args, 'provided_arguments', {})

    class AnsibleError_mock(Exception):
        pass

    with pytest.raises(AnsibleError_mock):
        with mock.patch.object(module_run, 'run') as mocked_run:
            mocked_run.side_effect = AnsibleError_mock
            module_run.run()

# Generated at 2022-06-13 11:06:42.378873
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Get an instance of ActionModule
    am = ActionModule()
    assert am is not None

    try:
        # Test the run method to ensure that it throws an error
        # if argument_spec is not given.
        am.run(tmp=None, task_vars=None)
    except AnsibleError as ae:
        assert 'argument_spec' in str(ae)

    # Create a dummy ActionModule instance
    class FooActionModule(ActionModule):
        def run(self, tmp=None, task_vars=None):
            pass
    fooam = FooActionModule()

    # Give the dummy ActionModule instance our get_args_from_task_vars method
    # for testing purposes
    fooam.get_args_from_task_vars = am.get_args_from_task_vars

    # Create

# Generated at 2022-06-13 11:06:53.225153
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Create a Mock instance of a task
    # (see https://docs.python.org/2/library/unittest.mock.html#quick-guide)
    _task = mock.Mock()

    # Create a mock instance of the ansible context.
    _connection = mock.Mock()
    _play_context = mock.Mock()
    _loader = mock.Mock()
    _templar = mock.Mock()

    # Create a mock instance of ansible task result
    _result = mock.Mock()
    _result.__dict__ = {}

    # Create a mock instance of AnsibleVars
    _ansible_vars = mock.Mock()
    _ansible_vars.__dict__ = {}

    # Create a instance of ActionModule

# Generated at 2022-06-13 11:07:01.057091
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Setup the mock
    action = ActionModule()
    action._task = {}
    action._task.args = {'argument_spec': {},'provided_arguments': {}}
    action.get_args_from_task_vars = lambda argument_spec, task_vars: {}
    action.validate_args_context = {}
    action.validate_args_context['kind'] = {}
    action.validate_args_context['kind']['type'] = {}
    action.validate_args_context['kind']['type'] = 'action'
    action.validate_args_context['kind']['name'] = {}
    action.validate_args_context['kind']['name'] = 'action_name'
    action.validate_args_context['version'] = {}
    action.validate_

# Generated at 2022-06-13 11:07:10.733535
# Unit test for method get_args_from_task_vars of class ActionModule
def test_ActionModule_get_args_from_task_vars():
    from ansible.context import CLIContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.vars.manager import VariableManager
    from ansible.module_utils.common.arg_spec import ArgumentSpec

    valid_argument_spec = dict(
        sample1=dict(required=True, type='bool'),
        sample2=dict(required=True, type='str'),
        sample3=dict(required=True, type='list', elements='str'),
        sample4=dict(required=True, type='dict'),
    )


# Generated at 2022-06-13 11:07:11.704200
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule.TRANSFERS_FILES == False

# Generated at 2022-06-13 11:07:18.330608
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ''' Unit test for method run of class ActionModule '''
    task_vars = dict()
    action_module_obj = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    task_vars['ansible_facts.processor'] = 'x86_64'
    action_module_obj._task.args = {
        'argument_spec': {'length': {'required': False, 'type': 'int'}, 'state': {'required': True, 'choices': ['present', 'absent'], 'type': 'str'}},
        'provided_arguments': {'length': 10, 'state': 'absent'}
    }
    with pytest.raises(AnsibleError) as obj:
        action_

# Generated at 2022-06-13 11:07:24.035893
# Unit test for constructor of class ActionModule
def test_ActionModule():
    argument_spec = dict(
        argument_spec=dict(required=True, type='dict'),
        provided_arguments=dict(required=False, type='dict')
    )
    action = ActionModule(argument_spec, dict())
    assert action


# Generated at 2022-06-13 11:07:32.368721
# Unit test for method get_args_from_task_vars of class ActionModule
def test_ActionModule_get_args_from_task_vars():
    ''' Unit test for get_args_from_task_vars method '''

    class ActionModule_for_test(ActionModule):
        ''' Dummy class for testing get_args_from_task_vars '''
        def __init__(self):
            p_type = string_types
            self._templar = Templar()
            self._templar.set_available_variables(dict(
                test_var="name",
                test_var2="name2",
            ))
            self._task = Task(dict(
                args=dict(
                    argument_spec=dict(
                        test_var=dict(type=p_type),
                        test_var2=dict(type=p_type),
                    ),
                ),
            ))

    class Task:
        ''' Dummy class '''

# Generated at 2022-06-13 11:07:40.363054
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.play_context import PlayContext
    from ansible.module_utils.common.validation import check_type_bool
    from ansible.module_utils.common.validation import check_type_dict
    from ansible.module_utils.common.validation import check_type_str
    from ansible.module_utils.common.validation import check_type_list

    play_context = PlayContext()
    play_context.become = False
    action_module = ActionModule(
        None,
        task_vars={'ansible_become_pass': 'pass'},
        task_uuid = 'task_uuid',
        loader = None,
        connection = None,
        play_context = play_context,
        new_stdin = None,
    )

# Generated at 2022-06-13 11:07:50.488294
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Test data
    argument_spec_data = {"arg1": {"required": True,
                                   "type": "dict",
                                   "options": {"opt1": {"required": True, "type": "str"},
                                               "opt2": {"required": False, "type": "str"}}},
                         "arg2": {"required": False, "type": "dict"}}

    provided_arguments = {"arg2": 3}

    # Message to display if the test case fails
    test_failed_message = "ArgumentSpecValidator validation failed"

    # Setup a mock action plugin with a stubbed run()
    class MockActionModule(object):

        @staticmethod
        def run():
            return {"validate_args_context": {"role": "my_role", "entry_point": "my_task"}}

    # Create a

# Generated at 2022-06-13 11:08:18.504252
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Testing run without any arguments
    with pytest.raises(Exception):
        test_action = ActionModule()
        test_action.run()


# Generated at 2022-06-13 11:08:25.559031
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import unittest

    from ansible.module_utils.common.arg_spec import ArgumentSpec
    from ansible.module_utils.six import PY2

    class FakeTask(object):
        def __init__(self):
            self.args = None

    class FakeTemplar(object):
        def __init__(self, task_vars):
            self.task_vars = task_vars
            self.collection_vars = {}

        def template(self, data):
            if isinstance(data, dict):
                for (k, v) in iteritems(data):
                    data[k] = self.template(v)
            elif isinstance(data, list):
                for i in range(len(data)):
                    data[i] = self.template(data[i])

# Generated at 2022-06-13 11:08:26.117139
# Unit test for constructor of class ActionModule
def test_ActionModule():
    pass

# Generated at 2022-06-13 11:08:34.167727
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''
    :return:
    '''
    # create an instance of class ActionModule
    action_module_obj = ActionModule(connection='local', module_name='test_name', task_vars=dict(),
                                     loader=None, templar=None, shared_loader_obj=None,
                                     collection_loader=None,
                                     action_defaults=dict())

    # test method run of class ActionModule with argument_spec and valid data for argument spec validation
    argument_spec = {
        "test_arg_name": {"required": True, "type": "int"}
    }
    provided_arguments = {
        "test_arg_name": "12"
    }
    action_module_obj._task.args = dict()
    action_module_obj._task.args['argument_spec'] = argument_

# Generated at 2022-06-13 11:08:35.346018
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule()
    assert isinstance(module, ActionModule)

# Generated at 2022-06-13 11:08:36.131993
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule.__name__ == "ActionModule"

# Generated at 2022-06-13 11:08:41.476798
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Now, give it some dummy data.
    argument_spec = {'valid_argument': {'type': 'str'},
                     'valid_argument_with_default': {'type': 'str', 'default': 'some value'}}

    provided_arguments = {'valid_argument': 'some value'}

    task_vars = {'valid_argument': 'some value'}

    action = ActionModule({'validate_args_context': 'some info about the args being validated'}, {'validate_args_context': 'some info about the args being validated'}, task_vars, {})

    action.run(None, task_vars)


# Generated at 2022-06-13 11:08:47.798987
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """Test the constructor of class ActionModule"""
    from ansible.plugins.action.validate_arg_spec import ActionModule

    action_module = ActionModule(
        task=dict(),
        connection=dict(),
        play_context=dict(),
        loader=dict(),
        templar=dict(),
        shared_loader_obj=dict()
    )
    return action_module

# Generated at 2022-06-13 11:08:58.106649
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''
    Unit test method run

    :returns: TODO
    '''
    # Create the unit test object
    action_module = ActionModule()

    # Create a dict for the unit test of arguments provided to the method run,
    # and for the return value it is expected to have.
    #
    # TODO: How to handle "result" from module?  Maybe a patched return value
    #       from self._execute_module()?
    task_vars = {'argument_spec': {'test_key': {'type': 'str'}},
                 'provided_arguments': {'test_key': 'test_value'},
                 'validate_args_context': {'role': 'testrole'}}

# Generated at 2022-06-13 11:09:07.143902
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    class ActionModuleMock(ActionModule):
        def __init__(self):
            self.actions = {}
            self.results = {}

        def run(self, tmp=None, task_vars=None):
            return super(ActionModuleMock, self).run(tmp, task_vars)

    # Test 1
    args = dict(
        argument_spec=dict(
            test_argument='dict',
        ),
        provided_arguments=dict(
            test_argument='dict',
        ),
    )

    action_module_mock = ActionModuleMock()
    action_module_mock._task.args = args
    result = action_module_mock.run(None, task_vars=dict())
    assert result['failed'] is False
    assert result['changed'] is False

# Generated at 2022-06-13 11:10:11.759524
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils.common.validation import ArgumentSpec, ValidationError
    from ansible_collections.netapp.ontap.plugins.module_utils.netapp_module import NetAppModule as post_validate_module

    obj = ActionModule()
    obj._task = dict()
    obj._task['args'] = dict()
    obj._task['args']['argument_spec'] = dict()

    # Test exception: argument_spec not in '_task.args'
    try:
        obj.run()
    except AnsibleError as e:
        assert isinstance(e, AnsibleError)
    else:
        raise AssertionError(
            'Expected AnsibleError, got no exception')

    obj._task['args']['argument_spec'] = dict()

    # Test exception: argument_spec not

# Generated at 2022-06-13 11:10:16.117520
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module_obj = ActionModule(load_fixture('validate_args_playbook.yml'), dict(), dict(play=None), loader=None, templar=None, shared_loader_obj=None)
    results = dict()
    results['msg'] = 'test'
    results['changed'] = False
    assert action_module_obj.run(tmp=None, task_vars=None) == results


# Generated at 2022-06-13 11:10:26.396340
# Unit test for method get_args_from_task_vars of class ActionModule
def test_ActionModule_get_args_from_task_vars():

    # This is a mock for the class ActionModule
    class ActionModuleStub(ActionModule):
        def get_args_from_task_vars(argument_spec, task_vars):
            return argument_spec, task_vars

    # As `run` calls `get_args_from_task_vars()` we use it to test this method
    result = ActionModuleStub.run(ActionModule, None, {'argument_spec': {'arg': {'required': True, 'type': 'dict'}},
                                                       'provided_arguments': {'arg': {'key': 'value'}}})

    # Validate the result is as expected
    assert result.get('failed', False) is False
    assert result.get('msg') == 'The arg spec validation passed'

# Generated at 2022-06-13 11:10:34.263087
# Unit test for method get_args_from_task_vars of class ActionModule
def test_ActionModule_get_args_from_task_vars():
    from ansible.plugins.action.validate_arg_spec import ActionModule
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager


# Generated at 2022-06-13 11:10:42.162854
# Unit test for method get_args_from_task_vars of class ActionModule
def test_ActionModule_get_args_from_task_vars():

    argument_spec = {
        'arg1': {'type': 'str'}
    }

    task_vars = {
        'arg1': 'this arg came from task_vars'
    }

    result = ActionModule.get_args_from_task_vars(None, argument_spec, task_vars)

    # The value that came from task_vars should be in the validation args, and
    # the value should be a string
    assert result['arg1'] == 'this arg came from task_vars'
    assert isinstance(result['arg1'], string_types)



# Generated at 2022-06-13 11:10:45.044797
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(None, {}, {}, None, None, None)
    assert action_module
    assert action_module.TRANSFERS_FILES == False


# Generated at 2022-06-13 11:10:55.915911
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Mock imports
    # None

    # Mock an AnsibleError
    mock_AnsibleError = MagicMock()

    # Mock an ArgumentSpecValidator
    mock_ArgumentSpecValidator = MagicMock()
    mock_ArgumentSpecValidator_instance = MagicMock()
    mock_ArgumentSpecValidator.return_value = mock_ArgumentSpecValidator_instance
    mock_validation_result = MagicMock()
    mock_validation_result.error_messages = ['error 1', 'error 2']
    mock_ArgumentSpecValidator_instance.validate.return_value = mock_validation_result

    # Mock an ActionBase
    mock_ActionBase = MagicMock()
    # Mock the ActionBase._task
    mock_ActionBase._task = MagicMock()
    # Mock the ActionBase._

# Generated at 2022-06-13 11:11:00.643976
# Unit test for constructor of class ActionModule
def test_ActionModule():
    doc = {'ANSIBLE_MODULE_ARGS': {'argument_spec': {'arg1': {'type': 'str'}},
                                   'validate_args_context': {'name': 'foo'},
                                   'provided_arguments': '{{{foo}}}'}
           }
    module = ActionModule(doc, {})
    assert module

# Generated at 2022-06-13 11:11:09.300476
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ''' Unit test for method run of class ActionModule '''
    # Ensure that the module fails if there is no argument_spec provided
    args = {}
    # instantiate the task
    action_module = ActionModule()
    # run the method
    action_result = action_module.run(task_vars=args)
    # validate that the result is as expected
    assert action_result['failed'] == True
    assert action_result['msg'] == '"argument_spec" arg is required in args: {}'

    # Ensure that the module fails if argument_spec is not a dict
    args = {'argument_spec': 'test'}
    # instantiate the task
    action_module = ActionModule()
    # run the method
    action_result = action_module.run(task_vars=args)
    # validate that the result

# Generated at 2022-06-13 11:11:10.017462
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert False


# Generated at 2022-06-13 11:13:10.803564
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    original_namespace = AnsibleValidationErrorMultiple.__name__
    AnsibleValidationErrorMultiple.__name__ = 'AnsibleValidationErrorMultiple'

    mock_ansible_module = AnsibleMock()

    tmp = None
    task_vars = dict()

    action_module = ActionModule(None, mock_ansible_module)
    action_module._templar.template = lambda x: x

    #  1. test fail with no args
    try:
        action_module.run(tmp, task_vars)
    except Exception as e:
        assert 'The arg spec validation passed' not in str(e), '1. No error message expected'
        assert '"argument_spec" arg is required in args: {}' in str(e), '1. Error message expected'

    #  2. test fail with