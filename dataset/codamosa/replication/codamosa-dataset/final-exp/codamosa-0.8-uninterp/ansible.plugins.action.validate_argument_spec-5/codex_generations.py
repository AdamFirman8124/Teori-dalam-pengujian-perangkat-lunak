

# Generated at 2022-06-13 11:03:20.575286
# Unit test for constructor of class ActionModule
def test_ActionModule():
    mod = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

    assert mod is not None

# Generated at 2022-06-13 11:03:21.970531
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule()
    assert action

# Generated at 2022-06-13 11:03:26.140764
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ''' This function tests the run method of class ActionModule '''
    try:
        my_obj = ActionModule()
        my_obj.run()
    except TypeError as err:
        assert 'run() takes at least 2 arguments (1 given)' in str(err)
    except KeyError as err:
        assert 'argument_spec' in str(err)



# Generated at 2022-06-13 11:03:27.135288
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert(True)

# Generated at 2022-06-13 11:03:32.286328
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import unit_tests.utils as utils
    options = {'validate_args_context': {'context': 'some_value'},
               'argument_spec': '<arg_spec>',
               'provided_arguments': '<args>'}
    runner = utils.get_runner(options)

    # Test without argument_spec in args
    runner._task.args.pop('argument_spec')
    result = utils.run_task(runner)
    assert(result['failed'])
    assert(result['msg'] == '"argument_spec" arg is required in args: {}'.format(result['validate_args_context']))

    # Test with wrong argument_spec type
    runner._task.args['argument_spec'] = 1
    result = utils.run_task(runner)

# Generated at 2022-06-13 11:03:36.681655
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ''' Unit test for method run of class ActionModule. '''

    module = get_action_module(validate_arg_spec)

    # Does not raise exception if called without argument_spec set
    result = module.run()
    assert result.get('msg') == 'The arg spec validation passed'
    assert result.get('failed') is False
    assert result.get('changed') is False

    # Does not raise exception if called without argument_spec in vars
    result = module.run(task_vars={'foo': 'bar'})
    assert result.get('msg') == 'The arg spec validation passed'
    assert result.get('failed') is False
    assert result.get('changed') is False

    # Raise exception if argument_spec is not a dict

# Generated at 2022-06-13 11:03:45.849565
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import copy
    import pytest
    from ansible.module_utils.ansible_collections.paloaltonetworks.panos.plugins.action.validate import ActionModule

    action_module = ActionModule(None, None)
    action_module._templar = None     # pylint: disable=protected-access
    # Mock the _templar property as it will be created in the constructor
    class _mock_templar():
        def __init__(self):
            self.template = lambda x: x
    action_module._templar = _mock_templar()   # pylint: disable=protected-access

    # Test the following arguments:
    #  'argument_spec': The argument specification for the entry point of a role
    #  'provided_arguments': The arguments provided by the user.

# Generated at 2022-06-13 11:03:47.030961
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_mod = ActionModule()
    action_mod.run()

# Generated at 2022-06-13 11:03:55.185898
# Unit test for constructor of class ActionModule
def test_ActionModule():
    spec = {'foo': {'type': 'list'}}
    provided = {'foo': 'not a list'}
    valid_name = 'validate_argument_spec'
    module_name = 'example'
    args = {'argument_spec': spec, 'provided_arguments': provided, 'validate_args_context': module_name}

    task = {'action': {'__name': valid_name, '__salt__': {'test.ping': lambda: None}, 'args': args}}
    task_copy = task.copy()
    task_vars = {}
    tmp_path = '/tmp'

    valid = ActionModule(task, task_vars, tmp_path, become_method='', become_user='', become_password='', check_mode=True)

# Generated at 2022-06-13 11:03:55.978300
# Unit test for method get_args_from_task_vars of class ActionModule
def test_ActionModule_get_args_from_task_vars():
    pass

# Generated at 2022-06-13 11:04:07.466063
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''
    This is the unit test for class ActionModule and for the method run of this class.
    '''
    action_module = ActionModule()

# Generated at 2022-06-13 11:04:15.801264
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils import basic


# Generated at 2022-06-13 11:04:18.132255
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''
    :raises AnsibleError: raises if an error
    '''
    am = ActionModule()
    if am is None:
        raise AnsibleError("Failed to instantiate ActionModule")


# Generated at 2022-06-13 11:04:22.586739
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''
    Unit test for method run of class ActionModule
    :return:
    '''
    # unit test for the ActionModule class
    # the ActionModule class has a run method which is the entry point
    # for the ansible action.
    # The run method accepts two arguments:
    #   - tmp: deprecated, do not use
    #   - task_vars: dict of task variables
    #
    # The run method gets the argument_spec as an argument to the ansible
    # action, as well as the provided_arguments (these are the arguments a user
    # provides to the ansible action).
    # The run method then calls the ArgumentSpecValidator.validate method to
    # validate the provided arguments against the argument spec.
    # The validate method returns an ArgumentValidationResult instance, which
    # exposes error_messages,

# Generated at 2022-06-13 11:04:23.692724
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(dict(), dict())

    assert isinstance(action_module, ActionModule)


# Generated at 2022-06-13 11:04:30.963472
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = ActionModule()

    # test empty value
    argument_spec = {'state': {'required': True, 'type': 'str'}, 'vlan_id': {'required': True, 'type': 'str'}}
    task_args = {'argument_spec': argument_spec, 'required_together': [], 'provided_arguments': {'state': 'present', 'vlan_id': '100'}}
    task_vars = dict(state='present', vlan_id='100')
    result = action_module.run(None, task_vars)
    assert result['changed'] == False
    assert result['msg'] == 'The arg spec validation passed'

    # test empty value

# Generated at 2022-06-13 11:04:41.185469
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import pytest
    # Setup the test environment
    utils.run_command_mock = MagicMock()

    specs = dict()
    specs['spec_name'] = dict()
    specs['spec_name']['choices'] = "test"

    args = dict()
    args['spec_name'] = "test"

    # Creation of the instance of the class ActionModule we are going to test
    args_array = dict()
    args_array['argument_spec'] = specs
    args_array['provided_arguments'] = args
    action_module_instance = ActionModule('', args_array, '')

    # Call run method
    try:
        action_module_instance.run()
    except SystemExit:
        pass

    # Test that run method call the run command with the right params
    assert 'run_command'

# Generated at 2022-06-13 11:04:41.752961
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 11:04:50.387987
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import unittest

    class TestActionModule(unittest.TestCase):
        def test_when_args_provided_are_valid_it_should_pass(self):
            import ansible.module_utils.common.arg_spec as arg_spec

            action_module = ActionModule()

            argument_spec = {
                'required_option': dict(type=arg_spec.int_type),
                'other_option': dict(type=arg_spec.str_type, required=False),
                'example_option': dict(required=False, type=arg_spec.bool_type),
            }

            task_vars = {
                'required_option': 4,
                'other_option': 'some string',
                'example_option': True,
            }


# Generated at 2022-06-13 11:05:02.504519
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''Unit test to test run method of class ActionModule
    '''

    # import class and create an object
    action_mod = ActionModule()

    # create tmp, task_vars and try to run the method
    tmp = None
    task_vars = {}
    try:
        res = action_mod.run(tmp=tmp, task_vars=task_vars)
    except AnsibleError as err:
        assert "argument_spec" in str(err)

    # create empty argument_spec
    argument_spec = {}
    task_vars = {'argument_spec': argument_spec}

    # create empty provided arguments
    provided_arguments = {}
    task_vars['provided_arguments'] = provided_arguments

# Generated at 2022-06-13 11:05:18.266133
# Unit test for constructor of class ActionModule
def test_ActionModule():
    argument_spec_data = {
        "X": {"type": "dict"},
        "Y": {"type": "dict"},
        "Z": {"type": "dict"},
        "W": {"type": "dict"}
    }

    provided_arguments = {
        "X": {"a": 1},
        "Y": {"b": 2}
    }

    args = {
        "argument_spec": argument_spec_data,
        "provided_arguments": provided_arguments
    }

    # Test Multiple validation error

# Generated at 2022-06-13 11:05:28.337260
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    act = ActionModule(dict(), dict())

    validation_result = AnsibleValidationErrorMultiple()
    validation_result.error_messages.append("This is a problem")

    # Should fail because argument spec is not a dict, but a string
    argument_spec_data = "this is a string"
    provided_arguments = dict()
    temp = dict()
    temp['validate_args_context'] = dict()
    result = act.run(dict(), temp)
    assert result['failed']

    # Should fail because provided arguments is not a dict, but a string
    argument_spec_data = dict()
    provided_arguments = "this is a string"
    temp = dict()
    temp['argument_spec'] = argument_spec_data
    temp['provided_arguments'] = provided_arguments

# Generated at 2022-06-13 11:05:37.392291
# Unit test for method run of class ActionModule

# Generated at 2022-06-13 11:05:40.246004
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ''' Unit test for method run of class ActionModule '''
    action_module = ActionModule()
    # TODO: unit test for run of class ActionModule
    raise NotImplementedError


# Generated at 2022-06-13 11:05:48.061526
# Unit test for method get_args_from_task_vars of class ActionModule
def test_ActionModule_get_args_from_task_vars():
    from ansible.template import Templar

    am = ActionModule(None, None, None)
    am._templar = Templar(loader=None, shared_loader_obj=None, variables={})

    data = {
        "argument_spec": {
            "name": {"required": True},
            "state": {"choices": ["present", "absent"], "default": "present"}
        },
        "validate_args_context": {
            "object_type": "role_defaults",
            "object_name": "role1"
        }
    }

    # Test get_args_from_task_vars
    result = am.get_args_from_task_vars(data['argument_spec'], {'name': 'foo', 'state': 'present'})

# Generated at 2022-06-13 11:05:58.072748
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import collections
    import yaml

    # load the testcases.yml file as dict
    test = yaml.load(open('./test/unittest/testcases.yml'), Loader=yaml.BaseLoader)

    # loop through all the testcases
    for tc in test['testcases']:
        # init argspecvalidator class
        actmod = ActionModule(None, collections.namedtuple('connection', 'shell')(None))
        actmod._templar = templar.Templar(loader=None)
        actmod._task = collections.namedtuple('task', 'args')(None)

        # set _task.args
        actmod._task.args = tc['task']['args']

# Generated at 2022-06-13 11:06:09.125784
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ''' Unit test for method run of class ActionModule'''

    argument_spec_data = {
        "state": {"required": True, "choices": ["present", "absent"], "type": "str"},
        "name": {"required": True, "type": "str"}
    }

    provided_arguments = {
        "state":  "present",
        "name": "if1"
    }

    task_vars = {
        "ansible_net_hostname": "n9k1",
        "ansible_net_username": "admin",
        "ansible_net_password": "cisco123"
    }


# Generated at 2022-06-13 11:06:19.807083
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    import random
    import string
    import os

    # mock ActionBase
    class ActionBase(object):
        def __init__(self):
            self.module_args = dict()

        # mock for run method
        def run(self, tmp=None, task_vars=None):
            self.module_args = dict()
            self.module_args['tmp'] = tmp
            self.module_args['task_vars'] = task_vars
            mock_result = dict()
            mock_result['tmp'] = tmp
            mock_result['task_vars'] = task_vars
            return mock_result

    # mock module_utils.common.arg_spec

# Generated at 2022-06-13 11:06:30.368544
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """ Unit test for method run of class ActionModule """
    # Create an instance of class ActionModule
    action_module_obj = ActionModule(load_data=dict(), templar=None, shared_loader_obj=None)

    # Create an instance of class TaskExecutor to set the default values for attributes
    # of class ActionModule
    task_executor_obj = TaskExecutor()

    # Set the default values for the attributes of class ActionModule
    action_module_obj._task = task_executor_obj
    action_module_obj._templar = None
    action_module_obj._loader = None
    action_module_obj._shared_loader_obj = None
    action_module_obj._connection = None
    action_module_obj._play_context = PlayContext()


# Generated at 2022-06-13 11:06:31.201146
# Unit test for constructor of class ActionModule
def test_ActionModule():
    test_action = ActionModule()

# Generated at 2022-06-13 11:06:58.668046
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # mock the class
    action_module = ActionModule(load_args=dict())
    action_module._task = MagicMock()
    action_module._task.args = {
        'argument_spec': {
            'name': {
                'required': True,
                'type': 'str'
            }
        },
        'provided_arguments': {
            'name': 'test'
        }
    }

    # mock return value
    action_module.run = MagicMock(return_value=dict())

# Generated at 2022-06-13 11:07:04.459322
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    class MockTemplar(object):

        def __init__(self, args):
            self.args = args

        def template(self, args):
            return args

    class MockModuleBase(object):

        def __init__(self, task_vars=None):
            self.task_vars = task_vars

        def get_vars(self):
            return self.task_vars

    class MockTask(object):

        def __init__(self, argument_spec):
            self.args = {
                'argument_spec': argument_spec,
                'validate_args_context': {},
            }


# Generated at 2022-06-13 11:07:14.919197
# Unit test for method get_args_from_task_vars of class ActionModule
def test_ActionModule_get_args_from_task_vars():
    ''' Unit test for get_args_from_task_vars '''
    action_mock = ActionModule({}, {}, shared_loader_obj=None, connection_loader_obj=None)
    action_mock.shared_loader_obj = None
    action_mock.connection_loader_obj = None
    action_mock.results = {}
    action_mock._templar = TemplatedVarMock({'variable_one': {'attr_1': 'value_1'},
                                             'variable_two': 'value_2'})

    argument_spec = {'variable_one': {'type': 'dict',
                                      'options': {'attr_1': {'type': 'str'}}
                                      },
                     'variable_two': {'type': 'str'}}

# Generated at 2022-06-13 11:07:24.591264
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action = ActionModule(dict(), dict(validate_args_context='blah'))
    result = action.run(task_vars=dict())
    assert result['msg'] == '"argument_spec" arg is required in args: {}'
    assert result['failed'] is True

    args = dict(
        argument_spec={'name': {'type': 'str'}},
        provided_arguments={'name': 'foo'},
    )
    action = ActionModule(dict(), args)
    assert action.run(task_vars=dict())['msg'] == 'The arg spec validation passed'
    assert action.run(task_vars=dict(name='bar'))['msg'] == 'The arg spec validation passed'


# Generated at 2022-06-13 11:07:26.580634
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module_obj = ActionModule()
    # TODO, other checks?
    assert action_module_obj.run(None, None)

# Generated at 2022-06-13 11:07:31.196659
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Create a new instance of class ActionModule
    action_module = ActionModule(
        task=None,
        connection=None,
        play_context=None,
        loader=None,
        templar=None,
        shared_loader_obj=None
    )

    print(type(action_module))
    assert isinstance(action_module, ActionModule)
    assert action_module.TRANSFERS_FILES is False


# Generated at 2022-06-13 11:07:38.732105
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''test_ActionModule_run'''
    action = ActionModule()
    # no tmp directory is set
    tmp = None
    # task_vars is not set
    task_vars = dict()
    # argument spec and the args need to be passed in
    task_vars['argument_spec'] = dict()
    task_vars['provided_arguments'] = dict()
    # the action should run successfully with no error thrown
    try:
        action.run(tmp, task_vars)
    except Exception as exception:
        assert False
        print(exception)
        print('test fail failed')
    # the argument spec should be a dict for this test to pass
    task_vars['argument_spec'] = ''

# Generated at 2022-06-13 11:07:48.283403
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import mock
    import ansible.plugins.loader as plugin_loader
    from ansible.action import ActionModule
    # from ansible.plugins.action import ActionModule

    # varibles to create a mock class
    mock_loader, mock_action_base, mock_argument_validator, \
        mock_action_module, str_ansible_action_base = plugin_loader, ActionBase, ArgumentSpecValidator, ActionModule, 'ansible.plugins.action.ActionBase'

    # mock the class ansible_action_base, in this case, the class is named str_ansible_action_base
    ansible_action_base = mock.Mock(spec_set=str_ansible_action_base)

    # mock the class ArgumentSpecValidator

# Generated at 2022-06-13 11:07:50.938386
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(task=dict(), connection=dict(), play_context=dict(), loader=dict(), templar=dict(), shared_loader_obj=dict())
    assert ActionModule()

# Generated at 2022-06-13 11:07:58.482249
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Create an instance of the ValidateArgumentSpec action
    action = ActionModule()

    # Set the module_name for mocks as for ansible inventory
    action._connection = 'local'
    # Set the host for mocks as for ansible inventory
    action._host = 'localhost'
    action.NO_TARGET_SYSTEM_DEPRECATION_WARNING = True


# Generated at 2022-06-13 11:08:35.088503
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule
    assert isinstance(am, type)

# Generated at 2022-06-13 11:08:35.600260
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert True

# Generated at 2022-06-13 11:08:42.359363
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = ActionModule()
    action_module._task = MockTask()

# Generated at 2022-06-13 11:08:45.448846
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(load_plugins=False)
    assert(isinstance(action_module, ActionModule))


# Generated at 2022-06-13 11:08:47.436470
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert isinstance(ActionModule(), ActionModule)


# Generated at 2022-06-13 11:08:57.987341
# Unit test for constructor of class ActionModule
def test_ActionModule():
    argument_spec = {
        "argument_spec": {"type": "dict"},
        "provided_arguments": {"type": "dict"},
        "validate_args_context": {"type": "dict"}
    }

# Generated at 2022-06-13 11:08:58.535776
# Unit test for method run of class ActionModule

# Generated at 2022-06-13 11:09:00.364793
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule(dict(), dict())
    assert isinstance(action, ActionBase)
    assert action.TRANSFERS_FILES is False

# Generated at 2022-06-13 11:09:09.656477
# Unit test for constructor of class ActionModule
def test_ActionModule():
    class A(object):
        pass

    a = A()
    a.args = None
    a.module_name = 'meta'
    a.task = A()
    a.task.action = 'meta'
    a.loader = None
    a.task_vars = {
        'test': 'test'
    }
    a.tmp = None
    a.task_path = ""
    a.playbook_dir = ""
    action_module = ActionModule(a, a.task, a.connection, a.play_context, a.loader, a.templar, a.shared_loader_obj)
    assert action_module is not None, 'Instance should not be None.'
    assert action_module._connection == a.connection, 'Should have expected connection object.'
    assert action_module.task_vars == a

# Generated at 2022-06-13 11:09:18.643860
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Test Helper class
    class TestArgSpecValidator(ArgumentSpecValidator):

        def __init__(self, argument_spec):
            self.argument_spec = argument_spec
            self.error_messages = []

        def validate(self, provided_arguments):
            return self

    # Mock
    class MockActionBase(ActionBase):
        def __init__(self, action_name, action_task_vars=None):
            self.failed = False
            self.msg = ''
            self.changed = False
            self.action_name = action_name
            self.action_task_vars = action_task_vars

        def run(self, tmp=None, task_vars=None):
            if task_vars is None:
                task_vars = dict()


# Generated at 2022-06-13 11:10:36.024078
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Inputs
    module_args = {
                  "argument_spec":{
                      "argument1":{"type":"int", "default":100},
                      "argument2":{"type":"dict", "required":True},
                      "argument3":{"type":"list", "required":True},
                      "argument4":{"type":"str", "required":True},
                      "argument5":{"type":"bool", "required":True, "default":False},
                      "argument6":{"type":"dict", "required":False, "default":"default"},
                  },
                  "provided_arguments":{
                      "argument1":100,
                      "argument2":{"key1":"value1"},
                      "argument3":["value1","value2"],
                      "argument4":"value1",
                      "argument5":True,
                      "argument6":"default"
                  }
                  }
    action = Action

# Generated at 2022-06-13 11:10:37.180634
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert(ActionModule(None, {}) is not None)



# Generated at 2022-06-13 11:10:37.782067
# Unit test for constructor of class ActionModule
def test_ActionModule():
    ActionModule()

# Generated at 2022-06-13 11:10:43.818742
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """Test ActionModule"""
    action_module = ActionModule(
        task=dict(args=dict(validate_args_context=dict())),
        connection=None,
        play_context=None,
        loader=None,
        templar=None,
        shared_loader_obj=None
    )

    assert action_module._task.args['validate_args_context'] == {}



# Generated at 2022-06-13 11:10:48.692596
# Unit test for constructor of class ActionModule
def test_ActionModule():
    def test_args(*args, **kwargs):
        ''' Mock for ansible.plugins.action.ActionBase.run '''

    am = ActionModule()
    am.run = test_args
    # create a class with a faked _task. It is required to not be None
    class Class:
        def __init__(self):
            self._task = 'a_string'
    am.__init__(Class)
    # call test on an empty dict
    assert am.run(None, {})



# Generated at 2022-06-13 11:11:01.249747
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import json

# Generated at 2022-06-13 11:11:09.763970
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''Unit test for method run of class ActionModule'''

    # The mock and patch needed for this test
    mocks = {
        'AnsibleError': AnsibleError,
        'super': ActionBase,
        'AnsibleValidationErrorMultiple': AnsibleValidationErrorMultiple,
        'iteritems': dict,
    }

    def my_super(self, tmp, task_vars):
        '''Super'''

        return {'changed': False, 'msg': 'NO ARGS'}

    # Create an instance of the class
    action_module = ActionModule(task=None, connection=None, play_context=None, loader=None,
                                 templar=None, shared_loader_obj=None)

    # Patch the classes, objects and functions needed
    # Patch of class AnsibleError

# Generated at 2022-06-13 11:11:16.330989
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Works only for Ansible 2.6.x
    from ansible.executor.task_result import TaskResult

    argument_spec = {
        "name": {
            "default": None,
            "required": True,
            "type": "str"
        },
        "foo": {
            "default": None,
            "required": False,
            "type": "str"
        },
        "bar": {
            "default": None,
            "required": False,
            "type": "str"
        }
    }

    argument_spec_data = {
        "argument_spec": argument_spec
    }

    provided_arguments = {
        "foo": "foo",
        "bar": "bar"
    }


# Generated at 2022-06-13 11:11:18.402498
# Unit test for constructor of class ActionModule
def test_ActionModule():
    ''' test_ActionModule(None, None) '''
    module = ActionModule(None, None)
    assert module is not None

# Generated at 2022-06-13 11:11:18.833446
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule