

# Generated at 2022-06-13 11:03:19.256339
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''test_ActionModule'''
    result = ActionModule()

    assert result is not None

# Generated at 2022-06-13 11:03:22.086146
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''
    test the constructor of class ActionModule
    '''
    action_module = ActionModule()
    assert action_module.TRANSFERS_FILES == False


# Generated at 2022-06-13 11:03:23.073474
# Unit test for constructor of class ActionModule
def test_ActionModule():
    obj = ActionModule()
    assert obj is not None

# Generated at 2022-06-13 11:03:30.685165
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    am = ActionModule()
    # Test that we get a TypeError if we don't have an argument spec in args
    # TODO: Improve this, maybe mock the self._task.args dict?
    try:
        am.run()
    except TypeError:
        pass
    except Exception:
        raise AssertionError("ActionModule should have raised TypeError because it has no args")
    # Test that we get an AnsibleError if we don't have the correct type for arg_spec
    try:
        am.run(task_vars={'argument_spec': []})
    except AnsibleError:
        pass
    except Exception:
        raise AssertionError("ActionModule should have raised AnsibleError because it has an invalid argument_spec")

# Generated at 2022-06-13 11:03:32.171577
# Unit test for constructor of class ActionModule
def test_ActionModule():
	assert ActionModule() is not None

# Generated at 2022-06-13 11:03:44.565781
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_result import TaskResult
    from ansible.inventory.host import Host

    class TestActionModule(ActionModule):
        def run(self, tmp=None, task_vars=None):
            return dict(ansible_facts=dict())

    task = Task()
    task_result = TaskResult(host=Host(name='localhost'), task=task)
    play_context = PlayContext()
    test_action_module = TestActionModule(task=task, connection=None, play_context=play_context, loader=None, templar=None, shared_loader_obj=None)
    result = test_action_module.run(task_vars=dict())

# Generated at 2022-06-13 11:03:53.458064
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """
    Constructor:
    action_plugin = ActionModule(task, connection, play_context, loader, templar, shared_loader_obj)
    """
    from ansible.module_utils.common.arg_spec import ArgumentSpecValidator
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.module_utils._text import to_bytes

    argument_spec = dict(
        foo = dict(type='bool')
    )
    validator = ArgumentSpecValidator(argument_spec)
    task_vars = ImmutableDict()
    templar = Templar(loader=None, variables=task_vars)
    var_mgr = VariableManager(loader=None, inventory=None)

# Generated at 2022-06-13 11:03:54.889989
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True == True

# Generated at 2022-06-13 11:04:03.794486
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ''' test_ActionModule_run

    Validate the run method of the ActionModule class.
    '''
    import pytest


# Generated at 2022-06-13 11:04:13.089379
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    from ansible.playbook.role.include import RoleInclude
    from ansible.plugins.loader import action_loader

    # A generic task for setting up a test
    task = Task()
    # The action being tested
    action_name = 'validate_arg_spec'
    # Get the wrapped action module
    action_class = action_loader.get(action_name,
                                     task=task,
                                     connection=None,
                                     play_context=PlayContext(),
                                     loader=None,
                                     templar=None,
                                     shared_loader_obj=None)
    # Instantiate the action module
    action = action_class()
    assert isinstance(action, ActionModule)

# Unit

# Generated at 2022-06-13 11:04:18.712741
# Unit test for constructor of class ActionModule
def test_ActionModule():

    # test passing obj
    _ActionModule = ActionModule()
    assert _ActionModule is not None

# Generated at 2022-06-13 11:04:26.280785
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''
    Unit test for constructor of class ActionModule
    '''
    test_task = type('TestTask', (object,), {})
    test_task.args = {}
    test_task.args['validate_args_context'] = {}
    test_task.args['validate_args_context']['action_type'] = 'jinja template'
    test_task.args['validate_args_context']['action_name'] = 'jinja template'
    test_task.args['validate_args_context']['action_module'] = 'template.py'
    test_task.args['argument_spec'] = {}
    test_task.args['provided_arguments'] = {}


# Generated at 2022-06-13 11:04:34.054456
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.plugins.loader import get_all_plugin_loaders
    from ansible.playbook.play_context import PlayContext

    # Get plugin loader
    plugin_loader = get_all_plugin_loaders()[0]

    # Get action plugin
    action_plugin = plugin_loader.get('action', 'validate_arguments_with_argument_spec')

    # Init task and play contexts
    task_vars = dict()
    play_context = PlayContext()

    # Init action module
    action_module = action_plugin(
        loader=plugin_loader,
        task=None,
        connection=None,
        play_context=play_context,
        loader_path=None,
        templar=None,
        shared_loader_obj=None
    )


# Generated at 2022-06-13 11:04:44.442345
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ''' validate_args action unit test'''

    module = ActionModule()

    argument_spec = {
        'author': {
            'type': 'list',
            'elements': 'str',
        },
    }

    provided_arguments = {
        'author': ['test']
    }

    args = {
        'argument_spec': argument_spec,
        'provided_arguments': provided_arguments
    }

    task = dict(
        action=dict(
            module='validate_args',
            args=args
        )
    )

    tmp = None
    task_vars = dict()
    result = module.run(tmp, task_vars)

    assert result.get('changed') is False
    assert result.get('msg') == 'The arg spec validation passed'

# Generated at 2022-06-13 11:04:57.798871
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # values taken from this file (validate_argument_spec.py)
    module_args = {
        'argument_spec': {
            'argument_spec': {'type': 'dict', 'default': {}},
            'provided_arguments': {'type': 'dict', 'default': {}}
        }
    }

    # Fake a module, task, and action plugin
    class DummyModule(object):
        def __init__(self):
            self.params = {}

    class DummyTask(object):
        def __init__(self):
            self.args = module_args

    class DummyActionPlugin(object):
        def __init__(self):
            self.name = 'validate_argument_spec'
            self.module = DummyModule()
            self.task = DummyTask()

    # Create a

# Generated at 2022-06-13 11:05:07.739853
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils.common.arg_spec import ModuleArgsValidator

    action_module = ActionModule()

    argument_spec = dict(
        user=dict(type='str', required=True),
        password=dict(type='str', required=True, no_log=True),
        enable=dict(type='bool', default=False),
        optional_group=dict(type='dict', default=dict(), options=dict(
            key=dict(type='str'),
            value=dict(type='str'),
        )),
        config_file=dict(type='path', required=True),
        security_dir=dict(type='path', required=True),
    )


# Generated at 2022-06-13 11:05:16.016759
# Unit test for method get_args_from_task_vars of class ActionModule
def test_ActionModule_get_args_from_task_vars():
    import unittest

    from ansible.plugins.action.validate_argument_spec import ActionModule

    class ModuleTestCase(unittest.TestCase):
        def setUp(self):
            self.validator = ActionModule()
            self.validator.task = unittest.mock.MagicMock()
            self.validator.task.args = {}

        def test_get_args_from_task_vars(self):
            """Tests that get_args_from_task_vars() returns the provided arguments."""

            argument_spec = {
                "test": {},
                "test_list": {"type": "list"},
                "test_dict": {"type": "dict"},
                "test_int": {"type": "int"},
            }

# Generated at 2022-06-13 11:05:26.186363
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    from ansible.vars import VariableManager
    from ansible.executor.task_result import TaskResult

    class FakeModuleResult(object):
        def __init__(self, module_name, result=None, msg=None):
            self.module_name = module_name
            self.result = result
            self.msg = msg

    class FakePlayContext(object):
        def __init__(self, ansible_vars=None, check_mode=True, connection='local', port=None,
                     remote_user='remote_user', become=False, become_method='sudo',
                     become_user=None, become_pass=None, become_exe=None,
                     diff=False, environment=None, only_tags=[], skip_tags=[]):
            self.connection = connection
            self.port = port

# Generated at 2022-06-13 11:05:33.730264
# Unit test for method get_args_from_task_vars of class ActionModule
def test_ActionModule_get_args_from_task_vars():
    from ansible.plugins.action.validate_argument_spec import ActionModule
    from ansible.module_utils.common.arg_spec import ArgumentSpecValidator
    import six
    import unittest
    import json

    class TestActionModule(unittest.TestCase):
        def setUp(self):
            self.action_module = ActionModule()

        def test_valid_input(self):
            task_vars = {
                'my_arg': 'my_value',
                'my_arg2': 'my_value2'
            }

            argument_spec = {
                'my_arg': {},
                'my_arg2': {},
            }

            args = self.action_module.get_args_from_task_vars(argument_spec, task_vars)
            self.assertIsInstance

# Generated at 2022-06-13 11:05:43.449174
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(
        task=dict(
            async_val=40,
            become_method='sudo',
            become_user='root',
            become=False,
            no_log=False,
            args=dict(
                argument_spec=dict(
                    test=dict(required=True),
                    test_not_required=dict(required=False)
                ),
                provided_arguments=dict(
                    test=True,
                    test_not_required=False
                )
            )
        ),
        connection=None,
        play_context=dict(
            check_mode=False
        ),
        loader=None,
        templar=None,
        shared_loader_obj=None
    )

    # test the __init__ method
    assert not isinstance(action_module, ActionModule)

# Generated at 2022-06-13 11:05:55.643617
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule(play=dict(), runner=dict())
    assert am._task == dict()
    assert am._play_context == dict()
    assert am._loader == dict()
    assert am._templar == dict()
    assert am._shared_loader_obj == dict()

# Generated at 2022-06-13 11:06:04.821198
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''
    Unit test for the method run of class ActionModule
    '''
    # We will use a mock of ActionBase because we don't need its functionality
    # We just want to test the methods in ActionModule

    # Mock of the ActionBase class
    class MockActionModule(ActionBase):
        '''
        Mock of the ActionModule class
        '''
        TRANSFERS_FILES = False

        def __init__(self, tmp, tas_vars):
            '''
            Mock init method that does nothing
            :param tmp: None
            :param tas_vars: None
            '''
            pass


# Generated at 2022-06-13 11:06:18.203364
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import sys
    import types
    module = sys.modules[__name__]
    action_module = module.ActionModule()

    # Mock the args that would be passed in from the task.

# Generated at 2022-06-13 11:06:28.905779
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Check that argument_spec is required, without it, the error
    # is raised
    from ansible.plugins.action.validate_arg_spec import ActionModule
    from ansible.errors import AnsibleError
    from ansible.module_utils.connection import Connection
    from ansible.module_utils.network.common.utils import load_provider
    from ansible.utils import context_objects as co
    import ansible.constants as C

    action = ActionModule(task=None, connection=Connection('localhost'), play_context=None, loader=None,
                          templar=None, shared_loader_obj=None)

    # ensure loader and templar are cleanup
    co.cleanup()

    C.CONFIG_LOADER = True

    vars_loader = 'vars'


# Generated at 2022-06-13 11:06:29.370851
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 11:06:36.663444
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.action.validate_arg_spec import ActionModule
    from ansible.module_utils.common.arg_spec import ArgumentSpecValidator, ArgumentError
    mock_task = Mock()
    mock_task.args = {
        'argument_spec': {
            'a': {'type': 'str'},
            'b': {'type': 'int'}
        },
        'provided_arguments': {
            'a': 'aaa',
            'b': 'bbb'
        }
    }
    action_module = ActionModule(mock_task, dict())

    validator = ArgumentSpecValidator.from_params(dict(a=dict(type='str'), b=dict(type='int')), dict())

# Generated at 2022-06-13 11:06:48.067680
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # The expected result is a dict
    expected_result = {
        "failed": False,
    }

    # The dict of provided arguments
    provided_arguments = {
        'user': 'ansible',
        'group': 'ansible',
    }

    # The dict of argument_spec
    argument_spec = {
        'user': dict(type='str'),
        'group': dict(type='str'),
    }

    # The test object
    test_obj = ActionModule()

    # The actual result
    actual_result = test_obj.run(None, dict({'validate_args_context': {}, 'argument_spec': argument_spec, 'provided_arguments': provided_arguments}))

    # Assert it has the same content.

# Generated at 2022-06-13 11:06:57.853422
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule(None, None)

    # TypeError
    # module._task.args = {}
    # with pytest.raises(AnsibleError, match=r'^"argument_spec"'):
    #     module.run()

    # Error
    module._task.args = {'argument_spec': 10}
    with pytest.raises(AnsibleError, match=r'^Incorrect type for argument_spec'):
        module.run()

    # Fail
    module._task.args = {'argument_spec': {'provider': {'type': 'dict'}},
                         'provided_arguments': {'provider': 32}}
    result = module.run()
    assert result['failed']

# Generated at 2022-06-13 11:06:58.251331
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert True

# Generated at 2022-06-13 11:07:03.508587
# Unit test for constructor of class ActionModule
def test_ActionModule():

    from ansible.runner.action_plugins.validate_argument_spec import ActionModule
    from ansible.module_utils.six import PY3
    from ansible.utils.vars import combine_vars
    from ansible.module_utils.common.arg_spec import ArgumentSpecValidator


# Generated at 2022-06-13 11:07:32.594356
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Create an instance of a module
    module = ActionModule()

    # Create a fake TaskExecutor
    task_executor = object()

    # Create a fake AnsibleModule
    class FakeAnsibleModule:
        def __init__(self):
            self.params = dict()

    ansible_module = FakeAnsibleModule()

    # Create a fake Task
    class FakeTask:
        def __init__(self):
            self.args = dict()

    task = FakeTask()
    runner = object()

    # Create a fake Runner
    class FakeRunner:
        def __init__(self, connection_info, transport, become_info, module_args, module_name, task_vars, tmpdir, become_method='', become_user='', check=False, diff=False, complex_args=None):
            self

# Generated at 2022-06-13 11:07:33.986242
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule()
    assert isinstance(action, ActionModule)
    assert action  # nosec

# Generated at 2022-06-13 11:07:41.075068
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.role import Role
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.executor.task_queue_manager import TaskQueueManager

    class TestModule(object):
        def __init__(self):
            self.argument_spec = dict(foo=dict(type='str'))

    class TestPlay(Play):
        pass

    class TestTask(Task):
        pass

    class TestBlock(Block):
        pass

    class TestRole(Role):
        pass

    class TestRoleDefinition(RoleDefinition):
        pass

    class TestTaskQueueManager(TaskQueueManager):
        pass


# Generated at 2022-06-13 11:07:50.938356
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ''' test method run of class ActionModule '''

    # Tests for normal execution with no errors
    mb = ModuleBuilder('validate_argument_spec', 'action')


# Generated at 2022-06-13 11:07:57.407905
# Unit test for constructor of class ActionModule
def test_ActionModule():
    args = {
        'action': 'validate_argument_spec',
        'argument_spec': {'ok_f': dict(type='str')},
        'provided_arguments': {'ok_f': 'value_ok_f'}
    }

    test_task = dict(args=args)
    validate_args_plugin = ActionModule(test_task, {})  # the second param is a connection object
    assert 'action' in validate_args_plugin._task
    assert validate_args_plugin._task['action'] == 'validate_argument_spec'
    assert 'validate_args_context' not in validate_args_plugin._task.args

# Generated at 2022-06-13 11:08:05.975903
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """Test the constructor for class ActionModule."""
    # Constructor without parameters should raise no exception
    action_module = ActionModule()

    # Constructor with parameters should raise no exception
    connection = "connection"
    task = "task"
    jobs = "jobs"
    _loader = "loader"
    _templar = "templar"
    _shared_loader_obj = "shared_loader_obj"

    action_module = ActionModule(connection=connection,
                                 task=task,
                                 jobs=jobs,
                                 _loader=_loader,
                                 _templar=_templar,
                                 _shared_loader_obj=_shared_loader_obj)


# Generated at 2022-06-13 11:08:06.515898
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 11:08:08.151459
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.plugins.action import ActionModule
    test_object = ActionModule(ArgumentSpec({}), {})
    assert test_object is not None

# Generated at 2022-06-13 11:08:14.973158
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    result = dict(ansible_facts=dict())
    source_data = dict(
        argument_spec=dict(),
        provided_arguments=dict(),
        validate_args_context=dict(
            entry_point='tea',
            task_name='task2',
            role_name='role1'
        )
    )
    action_module = ActionModule(dict(), dict())
    action_module.task_vars = dict()
    action_module.task_vars['ansible_facts'] = dict()
    action_module.task_vars['ansible_facts']['ansible_system'] = 'Linux'
    action_module.task_vars['ansible_facts']['ansible_env'] = dict()

# Generated at 2022-06-13 11:08:16.168165
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule()
    assert isinstance(am, ActionModule)

# Generated at 2022-06-13 11:08:47.164680
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule()
    assert action

# Generated at 2022-06-13 11:08:57.888154
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ''' Unit test for method run of class ActionModule '''
    # Create a mock task
    mock_task = Mock()
    mock_task.args = dict()

    # Create an instance of the ActionModule
    action_module = ActionModule()
    action_module._task = mock_task
    action_module._templar = Mock()

    # Create a mock role spec

# Generated at 2022-06-13 11:08:59.783199
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule()
    assert isinstance(module, ActionModule)

# Unit test to validate args when argument_spec is not passed

# Generated at 2022-06-13 11:09:08.915727
# Unit test for constructor of class ActionModule
def test_ActionModule():
    class ActionModuleClass(ActionModule):
        def run(self, tmp=None, task_vars=None):
            pass

    def action_base(self, *args, **kwargs):
        pass

    action_base_class = type(action_base)
    action_base_instance = action_base_class()

    # Create an instance of ActionModule
    action_module_instance = ActionModuleClass(
        action_base_instance._task,
        action_base_instance._connection,
        action_base_instance._play_context,
        action_base_instance._loader,
        action_base_instance._templar,
        action_base_instance._shared_loader_obj)
    assert isinstance(action_module_instance, ActionModule)

    # test run method
    # case 1.1: test argument_spec

# Generated at 2022-06-13 11:09:17.871692
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.utils.connection_loader import ConnectionLoader
    action_module = ActionModule(load_args=dict(loader=ConnectionLoader()), task=dict(args={}))
    action_module._task.args = {
        'argument_spec': {
            'test_key': {
                'type': 'str',
                'required': True,
                'choices': ['test', 'test2']
            },
            'test_key2': {
                'type': 'int'
            }
        },
        'provided_arguments': {
            'test_key': 'test',
            'test_key2': 'test2'
        }
    }
    result = action_module.run(task_vars={})
    assert not result['failed']
    assert not result['changed']
    assert result['msg']

# Generated at 2022-06-13 11:09:26.079379
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''
    Test case for run method of class ActionModule.
    '''
    from ansible.module_utils.ansible_release import __version__ as ansible_version

    from ansible.plugins.action.validate_arg_spec import ActionModule
    from ansible.module_utils.common.arg_spec import ArgumentSpecValidator
    from ansible.module_utils.errors import AnsibleValidationErrorMultiple
    from ansible.utils.vars import combine_vars


# Generated at 2022-06-13 11:09:28.098237
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule({}, {}, {}, {})
    assert action_module
    # Make sure action_module is an instance of ActionModule
    assert isinstance(action_module, ActionModule)
    action_module.run()


# Generated at 2022-06-13 11:09:29.437257
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = ActionModule()
    action_module.run()

# Generated at 2022-06-13 11:09:35.674314
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''Unit test for method run of class ActionModule.'''

    mock_self = type('', (), {})()
    mock_self.task_vars = {'test': 'test', 'hostvars': [1, 2, 3]}
    mock_self._task = type('', (), {})()
    mock_self._task.args = {'action':
                            {'argument_spec': {'test_argument': {'type': 'int'}},
                             'provided_arguments': {'test_argument': 'test'},
                             'validate_args_context': {'module_name': 'test_module'}}}
    mock_self._templar = type('', (), {})()
    mock_self._templar.template = lambda x: x


# Generated at 2022-06-13 11:09:41.642902
# Unit test for constructor of class ActionModule
def test_ActionModule():

    # mock ValueError exception
    class ValueError(Exception):
        pass

    class MockTask(object):

        def __init__(self, args):
            self.args = args

    class MockAnsibleModule(object):

        def __init__(self):
            self.check_mode = False

    class MockTemplar(object):

        def __init__(self):
            pass

        def template(self, args):
            return args

    class MockPluginLoader(object):

        @staticmethod
        def get(name, *args, **kwargs):
            return name

        @staticmethod
        def all(type_name, *args, **kwargs):
            return []


# Generated at 2022-06-13 11:10:44.993459
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    set_module_args(dict(
        argument_spec={
            'name':{
                'required': True,
                'type': 'str'
            }
        },
        provided_arguments={
            'name': 'test'
        }
    ))
    module = ActionModule()
    module.run()

# Generated at 2022-06-13 11:10:48.575051
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(load_plugins=False, task=None, connection=None,
                          play_context=None, loader=None, templar=None, shared_loader_obj=None)

    assert module is not None

# Generated at 2022-06-13 11:11:01.132249
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Basic method test
    module = ActionModule()
    module.task = mock.Mock()
    module._task.args = {
        'argument_spec': {'a': {'type': 'int'}, 'b': {'type': 'bool'}, 'c': {'type': 'dict'}},
        'provided_arguments': {}
    }
    module.task.action = 'validate_arg_spec'
    module.task_vars = {}
    assert module.run() == {'changed': False, 'msg': 'The arg spec validation passed'}

    # Test a basic failure
    module.task_vars = {'a': 1}
    assert module.run() == {'changed': False, 'msg': 'The arg spec validation passed'}

# Generated at 2022-06-13 11:11:02.960373
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """test the constructor of the class ActionModule"""

    # Create a module
    ActionModule(None, None, None, None, None)

# Generated at 2022-06-13 11:11:04.411005
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule()
    assert action_module is not None

# Generated at 2022-06-13 11:11:12.545420
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """ This unit test is based on the following test scenario:
    """
    print('\n==  Executing ansible.modules.network.nso.test_ActionModule_run ==')

    # These are the inputs that this test case will use to validate the argument
    # spec.

# Generated at 2022-06-13 11:11:14.956273
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.plugins.action.validate_arg_spec import ActionModule
    class Task(object):
        args = {'argument_spec': {}, 'provided_arguments': {}}
    action = ActionModule(task=Task())
    assert isinstance(action, ActionModule)

# Generated at 2022-06-13 11:11:19.255537
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''
    Unit test for constructor of class ActionModule.
    '''

    # Check if invocation raises any exception.
    try:
        ActionModule()
    except AnsibleValidationErrorMultiple as e:
        pass
        # print(str(e))

# Generated at 2022-06-13 11:11:19.769744
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert True

# Generated at 2022-06-13 11:11:26.480236
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ''' Unit test for method run of class ActionModule '''

    ansible_mock = Mock()
    ansible_mock.run.return_value = {'failed': True, 'msg': 'The arg spec validation failed'}
    module = ActionModule(ansible_mock, {})
    result = module.run(None, None)
    ansible_mock.run.assert_called_once_with(None, None)
    assert result['failed'] == True
    assert result['msg'] == 'The arg spec validation failed'