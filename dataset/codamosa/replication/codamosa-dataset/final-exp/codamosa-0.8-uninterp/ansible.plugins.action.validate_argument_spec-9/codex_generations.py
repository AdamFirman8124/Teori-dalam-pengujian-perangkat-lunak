

# Generated at 2022-06-13 11:03:20.434867
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    module = ActionModule()

    class FakeTask(object):
        def __init__(self, args):
            self.args = args

    # Test that "argument_spec" is required
    task = FakeTask({})
    module._task = task
    with pytest.raises(AnsibleError):
        module.run()

    # Test that "argument_spec" must be a dict
    task = FakeTask({'argument_spec': 'not a dict'})
    module._task = task
    with pytest.raises(AnsibleError):
        module.run()

    # Test that "provided_arguments" must be a dict
    task = FakeTask({'argument_spec': {}, 'provided_arguments': 'not a dict'})
    module._task = task

# Generated at 2022-06-13 11:03:27.926842
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    print('test_ActionModule_run')
    action_module_obj = ActionModule()
    action_module_obj._task = {'args': {'argument_spec': {'a': {'type': 'int'},
                                                          'b': {'type': 'list', 'elements': 'int'}},
                                        'provided_arguments': {'a': '10', 'b': ['1', '2', '3']}
                                        }
                                }
    result = action_module_obj.run()
    import json
    print(json.dumps(result, indent=4))
    assert result['msg'] == 'The arg spec validation passed'



# Generated at 2022-06-13 11:03:30.252855
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_plugin = ActionModule()
    assert isinstance(action_plugin, ActionModule)

# Generated at 2022-06-13 11:03:43.800909
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import json

    # Initialize test variables
    argument_spec = {
        'name': dict(type='str'),
        'field1': dict(type='dict'),
        'field2': dict(type='list'),
        'field3': dict(type='str', choices=['first', 'second']),
    }

    provided_arguments = {
        'name': 'foo',
        'field1': {'a': 'b'},
        'field2': ['a', 'b', 'c'],
        'field3': 'first',
    }

    task_vars = {'name': 'fred'}

    # Initialize ActionModule
    import ansible.plugins.action
    from ansible.playbook.task import Task

    # this is a dictionary, not a task

# Generated at 2022-06-13 11:03:44.236732
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True

# Generated at 2022-06-13 11:03:53.140260
# Unit test for method get_args_from_task_vars of class ActionModule
def test_ActionModule_get_args_from_task_vars():
    action_module = ActionModule(None, None, None, None)

    # Test 1: Check for correct processing of get_args_from_task_vars method
    # Given
    argument_spec = { "fakearg1": {"type": "str"}}
    task_vars = { "fakearg1" : "fakevalue"}

    # When
    args = action_module.get_args_from_task_vars(argument_spec, task_vars)

    # Then
    assert args == {'fakearg1': 'fakevalue'}

    # Test 2: Check for correct processing of get_args_from_task_vars method when argument is a list
    # Given
    argument_spec = { "fakearg1": {"type": "list"}}

# Generated at 2022-06-13 11:03:58.608723
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import unittest
    import os
    import sys

    # base class
    class TestBase(unittest.TestCase):
        def setUp(self):
            from ansible.errors import AnsibleError

            # general mocks
            self.MockAnsibleError = AnsibleError
            self.mock_general_dict = {}
            # modify the `what_it_does` list to make the test more readable
            self.mock_general_dict['validate_args_context'] = {'what_it_does': 'Unit testing'}
            self.mock_general_dict['failed'] = False
            self.mock_general_dict['msg'] = None
            self.mock_general_dict['changed'] = False

            # action base mocks

# Generated at 2022-06-13 11:04:02.534223
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import sys
    # Below adds the directory to the path to resolve the `test.unit.plugins.modules.test_validate_argument_spec` import
    if __name__ == '__main__':
        sys.path.append('.')
    from test.unit.plugins.modules import test_validate_argument_spec
    test_validate_argument_spec.test_ActionModule_run()

# Generated at 2022-06-13 11:04:08.121739
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''
    :returns: dict -- the result of the module execution
    '''
    test_host = {'hostname': 'localhost'}
    runner = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    task_vars = dict()
    result = runner.run(task_vars=task_vars)
    assert result['failed']

# Generated at 2022-06-13 11:04:08.715951
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True

# Generated at 2022-06-13 11:04:18.748724
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Create an instance of ActionModule
    module = ActionModule()
    assert module
    assert isinstance(module, ActionModule)

# Generated at 2022-06-13 11:04:24.582715
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task import Task
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    import json

    playbook = 'test_action_plugin_validate_argument_spec.yml'
    inventory = InventoryManager(loader=None, sources='localhost,')
    variable_manager = VariableManager()
    loader = DataLoader()

    pbex = PlaybookExecutor(playbooks=[playbook], inventory=inventory, variable_manager=variable_manager, loader=loader, passwords={})
    tqm = None

# Generated at 2022-06-13 11:04:31.559241
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module_utils = AnsibleModule(
        argument_spec=dict(
            argument_spec=dict(type='dict'),
            provided_arguments=dict(type='dict'),
            validate_args_context=dict(type='dict'),
        ),
    )
    set_module_args(dict(
        argument_spec={'test': {'required': False}},
        provided_arguments={'test': 'test'},
        validate_args_context={'context': 'context'},
    ))

    action_module = ActionModule(module_utils._task, {})
    result = action_module.run(task_vars={'test': 'test'})


# Generated at 2022-06-13 11:04:41.750246
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import ansible.utils.vars

    spec_data = dict(
        prop1=dict(required=True, type='str'),
        prop2=dict(required=True, type='dict')
    )
    provided_data = dict(
        prop1='value 1',
        prop2=dict(
            nested1='value1',
            nested2='value2',
        )
    )

    module = ActionModule(dict(name='validate_argument_spec', module_args=dict(argument_spec=spec_data, provided_arguments=provided_data)), dict(connection='network_cli'))
    result = module.run(task_vars=dict(prop1='value 1 from vars', prop2=dict(nested1='value from vars')))
    assert not result['failed']
    assert result['changed']

# Generated at 2022-06-13 11:04:50.394620
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # create object in order to test method
    obj = ActionModule()
    # testing function run of class ActionModule
    tmp = None
    task_vars = None
    obj.run(tmp=None, task_vars=None)
    task_vars = {"validate_args_context": {"validate_args_task": {"name": "test"}, "validate_args_role": {"name": "test"},
                                           "validate_args_plugin": {"name": "test"}, "validate_args_connection": {"name": "test"},
                                           "validate_args_module_name": "test", "validate_args_module_path": "test"},
                 "provide_arguments": {"test": "test"}}
    obj.run(tmp=None, task_vars=task_vars)
   

# Generated at 2022-06-13 11:04:52.220055
# Unit test for constructor of class ActionModule
def test_ActionModule():
    ActionModule()

# Generated at 2022-06-13 11:04:54.716258
# Unit test for constructor of class ActionModule
def test_ActionModule():
    if __name__ == '__main__':
        # Creating ActionModule object
        actionmodule = ActionModule()

# Generated at 2022-06-13 11:04:55.511835
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 11:05:05.131774
# Unit test for method get_args_from_task_vars of class ActionModule
def test_ActionModule_get_args_from_task_vars():
    ''' unit test for get_args_from_task_vars method '''
    action_module = ActionModule()
    action_module._templar = FakeTemplar()
    argument_spec = dict(
        key1=dict(required=True, type='str'),
        key2=dict(required=True, type='str'),
    )

    task_vars = dict(key1="{{ 'value1' }}", key2="{{ 'value2' }}")
    args = action_module.get_args_from_task_vars(argument_spec, task_vars)
    assert len(args) == 2
    assert args['key1'] == 'value1'
    assert args['key2'] == 'value2'
    return


# Generated at 2022-06-13 11:05:07.097499
# Unit test for constructor of class ActionModule
def test_ActionModule():
    class_ = ActionModule()
    assert isinstance(class_, ActionBase)



# Generated at 2022-06-13 11:05:16.141676
# Unit test for constructor of class ActionModule
def test_ActionModule():
    return ActionModule()

# Generated at 2022-06-13 11:05:26.349885
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils.common.arg_spec import ArgumentSpecValidator
    from ansible.utils.vars import combine_vars

    ansible_module = ActionModule()
    class test_ActionBase():
        args = {'argument_spec': {'user': {'type': 'str'}}, 'provided_arguments': {'user': 'test'}}
        def _get_worker_privilege(self):
            return True

    ansible_module._task = test_ActionBase()
    ansible_module._templar = test_ActionBase()
    ansible_module._templar.template = lambda x: x
    ArgumentSpecValidator.validate = lambda self, args: self
    ArgumentSpecValidator.error_messages = []

# Generated at 2022-06-13 11:05:27.395596
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule is ActionModule

# Generated at 2022-06-13 11:05:28.188041
# Unit test for constructor of class ActionModule
def test_ActionModule():
    test_instance = ActionModule()
    print("hello")


# Generated at 2022-06-13 11:05:37.191049
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils import basic
    import copy

    # create an instance of the class under test
    module_args = {'argument_spec': {'arg': {'type': 'dict', 'required': True},
                                     'arg2': {'type': 'dict', 'required': True, 'default': {'test': 'default_value'}},
                                     'arg3': {'type': 'dict', 'required': True, 'default': {'test': 'default_value'}}},
                   'provided_arguments': {'arg': {'test': 'value'}, 'arg2': {'test': 'value'}, 'arg3': {'test': 'value'}},
                   'validate_args_context': {'entry_point': 'main', 'role_name': 'test_role'}}
    action_module

# Generated at 2022-06-13 11:05:45.814827
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import tempfile
    tmpdir = tempfile.mkdtemp(prefix='ansible-test-validate_argument_spec-')

    from ansible.module_utils.common.validation import ErrorData

    class MockActionBase:
        def run(self, tmp, task_vars):
            return {'tmp': tmp, 'task_vars': task_vars, 'changed': False}

    class MockTask:
        def __init__(self, args):
            self.args = args

    with open('test_validate_argument_spec_file', 'w+') as f:
        f.write('foo')

    action_base_instance = MockActionBase()


# Generated at 2022-06-13 11:05:56.564705
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import unittest.mock as mock
    import json
    import os
    import sys

    import ansible_collections.community.general.plugins.action.validate_argument_spec as validate_argument_spec
    import ansible.plugins.loader as plugins_loader

    from ansible.plugins.action import ActionBase
    from ansible.module_utils.six import iteritems
    from ansible.module_utils.common.arg_spec import ArgumentSpecValidator
    from ansible.module_utils.errors import AnsibleValidationErrorMultiple
    from ansible.utils.vars import combine_vars

    # Mock imports to run some of the functions in this file.
    sys.modules['ansible.plugins.loader'] = mock.Mock()
    sys.modules['ansible.plugins.loader.ActionModuleLoader'] = mock.Mock

# Generated at 2022-06-13 11:05:57.298614
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule()

# Generated at 2022-06-13 11:05:58.307427
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Create an instance of ActionModule
    module = ActionModule()
    assert module.TRANSFERS_FILES == False

# Generated at 2022-06-13 11:06:09.702713
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_base_path = 'ansible.plugins.action.ActionBase'
    action_module_path = 'ansible.plugins.action.ActionModule'
    fake_action_base = FakeActionBase(action_base_path)
    action_module = ActionModule(
        task=FakeTask(),
        connection=FakeConnection(),
        play_context=FakePlayContext(),
        loader=FakeLoader(),
        templar=FakeTemplar(),
        shared_loader_obj=FakeLoader(),
    )
    action_module._shared_loader_obj = action_module.loader
    action_module._connection = action_module.connection
    action_module._task = action_module.task
    action_module._loader = action_module.loader
    action_module._templar = action_module.templar
    action_module._

# Generated at 2022-06-13 11:06:30.473788
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Test with no args passed
    action_module = ActionModule(None, None)
    assert action_module is not None

    # Test with arguments passed
    action_module = ActionModule(None, None, 'test')
    assert action_module is not None


# Generated at 2022-06-13 11:06:38.223455
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(loader=None,
                                 tempdir=None,
                                 task_vars=None,
                                 connection=None,
                                 play_context=None,
                                 loader_cache=None,
                                 shared_loader_obj=None,
                                 termination_plugin=None,
                                 module_vars=None,
                                 task_uuid=None,
                                 task_path=None,
                                 task_path_depth=None,
                                 role_names=None,
                                 role_params=None,
                                 role_update=None,
                                 role_args=None,
                                 main_task_path=None,
                                 diff=None,
                                 task=None,
                                 defs=None)
    assert action_module is not None


# Generated at 2022-06-13 11:06:49.126064
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """Unit test for method run of class ActionModule"""

    # Create a fake task that does not have argument_spec data (which should
    # cause an exception in the run method)
    task = MagicMock(args=dict())

    # Run the validation. Should throw an exception.
    # If it does not then the test has failed.
    acm = ActionModule(task, {})
    with pytest.raises(AnsibleError):
        acm.run()

    # Create a fake task that does not have provided_arguments data (which should
    # cause an exception in the run method)
    task = MagicMock(args=dict(argument_spec=dict(foo='bar')))

    # Run the validation. Should throw an exception.
    # If it does not then the test has failed.

# Generated at 2022-06-13 11:06:58.775602
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''
    Test call to run, with properly formatted values.
    '''
    # Mock out modules
    modules = {
        'ansible.plugins.action.ActionBase': ActionBase
    }
    module_mocks = {}
    for module_name, cls in iteritems(modules):
        module_mocks[module_name] = MagicMock(
            return_value=MagicMock(
                module_name=module_name,
                __bases__=cls
            )
        )

    # Mock out classes
    classes = {
        'AnsibleError': AnsibleError,
        'AnsibleValidationErrorMultiple': AnsibleValidationErrorMultiple,
        'ArgumentSpecValidator': ArgumentSpecValidator,
    }
    class_mocks = {}

# Generated at 2022-06-13 11:07:07.049145
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    def __init__(self):
        self.run_ok = {}
    task_vars = {}
    result = {}
    # test response 1
    task_vars = {"one": "hello", "two": "hi"}
    argument_spec = {"arg": {"type": "str"}}
    provided_arguments = {"arg": "hello"}
    tmp_obj = __init__(self)
    tmp_obj.run(tmp=None, task_vars=task_vars)
    assert tmp_obj.run(tmp=None, task_vars=task_vars) == result
    # test response 2
    task_vars = {"one": "hello", "two": "hi"}
    tmp_obj = __init__(self)

# Generated at 2022-06-13 11:07:16.765923
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Arrange
    action_mod = ActionModule()
    action_mod._task.args = {
        'validate_args_context': 'network_cli',
        'argument_spec': {
            'host': {'required': True, 'type': 'str'},
            'opt1': {'required': True, 'type': 'str'},
            'opt2': {'required': True, 'type': 'int'},
            'port': {'required': False, 'type': 'int', 'default': 22}
        },
        'provided_arguments': {
            'host': '{{ host }}',
            'port': 22,
            'opt1': '{{ opt1 }}',
            'opt2': '{{ opt2 }}'
        }
    }
    action_mod._templar = None
    action_

# Generated at 2022-06-13 11:07:22.655467
# Unit test for method get_args_from_task_vars of class ActionModule
def test_ActionModule_get_args_from_task_vars():
    action_module = ActionModule()

    assert {} == action_module.get_args_from_task_vars({}, {})
    assert {'foo': 'bar'} == action_module.get_args_from_task_vars([{'name': 'foo'}], {'foo': 'bar', 'baz': 'qux'})
    assert {'foo': 'bar'} == action_module.get_args_from_task_vars([{'name': 'foo', 'required': True}], {'foo': 'bar'})

# Generated at 2022-06-13 11:07:24.517180
# Unit test for constructor of class ActionModule
def test_ActionModule():
    ''' The test case for testing the constructor'''

    module = ActionModule()

    assert module is not None

# Generated at 2022-06-13 11:07:32.839267
# Unit test for constructor of class ActionModule
def test_ActionModule():

    argument_spec = dict(
        action=dict(type='str', required=True, choices=['validate']),
        argument_spec=dict(type='dict', required=True),
        provided_arguments=dict(type='dict', required=True),
        validate_args_context=dict(type='dict', required=False),
    )


# Generated at 2022-06-13 11:07:35.405356
# Unit test for constructor of class ActionModule
def test_ActionModule():
    actionmodule = ActionModule()
    assert actionmodule is not None

# Generated at 2022-06-13 11:08:14.982766
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ''' Unit test for method run of class ActionModule '''
    args = dict()
    args_data = dict()
    args['argument_spec'] = args_data
    args['provided_arguments'] = dict()
    # Constructing the object of class ActionModule
    obj = ActionModule()
    # Calling the run method with args as parameters
    result = obj.run(args)
    assert result['failed'] is True


# Generated at 2022-06-13 11:08:15.660564
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule()

# Generated at 2022-06-13 11:08:22.549343
# Unit test for method run of class ActionModule

# Generated at 2022-06-13 11:08:30.681907
# Unit test for constructor of class ActionModule
def test_ActionModule():
    ''' create an instance of the class'''

    # To validate arg spec we need an actual argument spec, so use the one for the openconfig module
    with open('../../../library/openconfig.py') as f:
        mod_data = f.read()

    exec(compile(mod_data, 'openconfig.py', 'exec'), globals())
    actual_arg_spec = main.argument_spec

    # Fake the context to test what happens with different values of the 'validate_args_context'
    task_context = {
        'validate_args_context': {
            'role': 'openconfig',
            '_entry_point': 'main',
            'task': 'validate_arg_spec'
        }
    }

    # Create the runner object, and call the action plugin
    task_runner = ActionModule

# Generated at 2022-06-13 11:08:32.109902
# Unit test for constructor of class ActionModule
def test_ActionModule():
    result = ActionModule()
    assert not result.run({}, {})['msg']

# Generated at 2022-06-13 11:08:35.490576
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(
        task=dict(),
        connection=dict(),
        play_context=dict(),
        loader=dict(),
        templar=dict(),
        shared_loader_obj=dict()
    )
    assert isinstance(action_module, ActionModule)

# Generated at 2022-06-13 11:08:36.048034
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 11:08:40.067887
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''
    Test the constructor of the ActionModule class.  The constructor
    should set some default values when created.
    '''
    action_module = ActionModule()
    assert action_module.display.verbosity == 1, 'Invalid default verbosity'
    assert action_module.connection is not None, 'Connection not set'
    assert action_module.noop_on_check_mode is False, 'Invalid noop on check mode'


# Generated at 2022-06-13 11:08:41.372484
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule()
    assert module

# Generated at 2022-06-13 11:08:42.438682
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert isinstance(ActionModule, object)

# Generated at 2022-06-13 11:09:59.621332
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils.network.common.utils import load_provider
    from ansible.module_utils.connection import Connection

    from ansible.plugins.loader import connection_loader
    from ansible.plugins.loader import action_loader

    adapter = connection_loader.get('local', class_only=True)
    connection = Connection(adapter)

    task_args = dict(argument_spec=dict(test_arg=dict(type='list')), provided_arguments=dict(test_arg=['']))
    action = action_loader.get('validate_argument_spec', class_only=True)
    ac = action(connection, task_args=task_args, play_context=None, loader=None, templar=None, shared_loader_obj=None)


# Generated at 2022-06-13 11:10:04.943536
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Setup
    action = ActionModule(None, None)
    action._task = {'args': {'argument_spec': {}, 'provided_arguments': {}}}
    action._templar = None
    action._loader = None
    action._connection = None
    action._play_context = None
    action._task.args = {'argument_spec': {'key1': 'value1'}, 'provided_arguments': {},
                         'validate_args_context': {'role':'test', 'entry_point': 'main.yml'}}

    # Run
    result = action.run(None, None)

    # Verify
    assert result['changed'] == False
    assert result['failed'] == False



# Generated at 2022-06-13 11:10:14.898008
# Unit test for method get_args_from_task_vars of class ActionModule
def test_ActionModule_get_args_from_task_vars():
    '''
    Function to test class ActionModule method get_args_from_task_vars
    '''
    module = ActionModule({}, {}, {}, None)

    # Check module.get_args_from_task_vars return type is dict
    assert type(module.get_args_from_task_vars({}, {})) == dict

    # Check module.get_args_from_task_vars return dict is empty if no elements in
    # task_vars
    assert not module.get_args_from_task_vars({'a': {'type': 'str'}}, {})

    # Check for non-empty dict, and dict.keys equal provided_arguments dict

# Generated at 2022-06-13 11:10:21.984935
# Unit test for constructor of class ActionModule
def test_ActionModule():
    params = {'argument_spec': {'required': True, 'type': 'str'},
              'provided_arguments': {'required': 42}}
    task = {'args': params}

    action = ActionModule({}, task, {})

    assert not action.TRANSFERS_FILES
    assert action.run({}, {}) == {'changed': False,
                                  'msg': 'The arg spec validation passed',
                                  'validate_args_context': {}}



# Generated at 2022-06-13 11:10:30.005486
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''
    Test to validate an argument specification against a provided set of data
    '''
    argument_spec = {'state': {'experiment': {'type':'str', 'default': 'abcd', 'choices': ['abcd', 'efgh']}, 'type':'str', 'required': True, 'choices': ['present', 'absent']}}
    parameters = {'state': 'present'}
    provided_arguments = {'state': 'present', 'experiment': 'efgh'}
    action_module = ActionModule(dict(), dict())
    results = action_module.run(argument_spec, parameters, provided_arguments)
    assert 'changed' in results and results['changed'] == False

# Generated at 2022-06-13 11:10:30.748554
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert issubclass(ActionModule, ActionBase)

# Generated at 2022-06-13 11:10:37.519244
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import os
    import sys
    import unittest

    from ansible.module_utils.six import PY3
    from ansible.modules.network.nxos import validate_argument_spec
    from ansible.utils.vars import combine_vars

    class TestActionModule(unittest.TestCase):
        '''
        a class for testing the action module
        '''

        def setUp(self):
            self._task = validate_argument_spec.ActionModule('TestActionModule.py')
            self._validate_argument_spec = validate_argument_spec.ActionModule('TestActionModule.py')

# Generated at 2022-06-13 11:10:47.385361
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''
    Unit test for method run of class ActionModule.

    :return: None
    '''
    # Check if argument_spec is not passed in
    # Expected output:
    #   raise AnsibleError('"argument_spec" arg is required in args: %s' % self._task.args)
    try:
        assert False
        instance = ActionModule()
        instance._task.args = {}
        instance.run(tmp="string", task_vars=dict())
    except AnsibleError:
        assert True
    else:
        assert False

    # Check if argument_spec is passed in and is a list
    # Expected output:
    #   raise AnsibleError('Incorrect type for argument_spec, expected dict and got %s' % type(argument_spec_data))

# Generated at 2022-06-13 11:10:54.008939
# Unit test for constructor of class ActionModule
def test_ActionModule():
    task = dict(name='test_task_name',
                args={'validate_args_context': {'path': 'some/path/to/module'},
                      'argument_spec': {},
                      'provided_arguments': {}
                      },
                )
    result = ActionModule(task, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None).run(tmp=None, task_vars=None)
    assert result

# Generated at 2022-06-13 11:11:03.907211
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''Unit test for run method of class ActionModule'''
    #the actual argument spec
    argument_spec = dict(
        param1 = dict(type='str', default='val1'),
        param2 = dict(type='str', default='val2'),
    )

    #the provided arguments
    provided_arguments = dict(
        param1 = 'provided value',
        param2 = 'provided value',
    )

    action_module = ActionModule(
        dict(
            args=dict(argument_spec=argument_spec, provided_arguments=provided_arguments),
            task=dict(args=dict(argument_spec=argument_spec, provided_arguments=provided_arguments)),
            task_vars=dict(argument_name='val')
        )
    )
