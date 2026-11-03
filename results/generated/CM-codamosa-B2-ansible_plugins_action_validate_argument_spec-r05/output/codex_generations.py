

# Generated at 2026-11-01 18:40:27.785969
# Unit test for method get_args_from_task_vars of class ActionModule
def test_ActionModule_get_args_from_task_vars():
    # Build an ActionModule instance without invoking ActionBase.__init__
    action = ActionModule.__new__(ActionModule)

    argument_spec = {
        'name': {'type': 'str', 'required': True},
        'age': {'type': 'int', 'default': 0},
    }
    task_vars = {
        'name': 'bob',
        'age': 42,
        'unrelated_var': 'should not be included',
    }

    # Mock the templar to pass values through unchanged
    templar = MagicMock()
    templar.template.side_effect = lambda value: value
    action._templar = templar


# Generated at 2026-11-01 18:40:32.341133
# Unit test for method get_args_from_task_vars of class ActionModule
def test_ActionModule_get_args_from_task_vars():
    from unittest.mock import MagicMock

    argument_spec = {
        'name': {'type': 'str', 'required': True},
        'path': {'type': 'str'},
    }
    task_vars = {
        'name': 'somename',
        'path': '/tmp/foo',
        'unrelated': 'not_in_spec',
    }

    action = ActionModule.__new__(ActionModule)
    action._templar = MagicMock()
    action._templar.template.side_effect = lambda x: x

    result = action.get_args_from_task_vars(argument_spec, task_vars)

    assert result == {'name': 'somename', 'path': '/tmp/foo'}
    assert 'unrelated' not in result
    action._templar.template.assert_called_once_with({'name': 'somename', 'path': '/tmp/foo'})


# Unit test for method get_args_from_task_vars with templated values
def test_ActionModule_get_args_from_task_vars_templating():
    from unittest.mock import MagicMock

    argument_spec = {
        'name': {'type': 'str'},
    }
    task_vars = {
        'name': 'myvalue',
    }

    action = ActionModule.__new__(ActionModule)
    action._templar = MagicMock()
    action._templar.template.return_value = {'name': 'templated_myvalue'}

    result = action.get_args_from_task_vars(argument_spec, task_vars)

    assert result == {'name': 'templated_myvalue'}


# Unit test for method get_args_from_task_vars with no matching task vars
def test_ActionModule_get_args_from_task_vars_no_matches():
    from unittest.mock import MagicMock

    argument_spec = {
        'name': {'type': 'str'},
    }
    task_vars = {
        'other_var': 'value',
    }

    action = ActionModule.__new__(ActionModule)
    action._templar = MagicMock()
    action._templar.template.side_effect = lambda x: x

    result = action.get_args_from_task_vars(argument_spec, task_vars)

    assert result == {}

# Generated at 2026-11-01 18:40:37.512888
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''
    Test the constructor of ActionModule.

    ActionModule does not define its own __init__, so it inherits from
    ActionBase. We patch ActionBase.__init__ to avoid needing real
    task/connection/play_context/loader/templar objects, instantiate the
    class, and verify it was initialized correctly.
    '''
    task = MagicMock()
    connection = MagicMock()
    play_context = MagicMock()
    loader = MagicMock()
    templar = MagicMock()
    shared_loader_obj = MagicMock()

    with patch.object(ActionBase, '__init__', return_value=None) as mock_init:
        action_module = ActionModule(
            task,
            connection,
            play_context,
            loader,
            templar,
            shared_loader_obj,
        )

        # Parent constructor should have been invoked with all args
        mock_init.assert_called_once_with(
            task, connection, play_context, loader, templar, shared_loader_obj
        )

    # Instance checks
    assert isinstance(action_module, ActionModule)
    assert isinstance(action_module, ActionBase)

    # Class attribute sanity checks
    assert ActionModule.TRANSFERS_FILES is False

# Generated at 2026-11-01 18:40:47.857488
# Unit test for method run of class ActionModule
def test_ActionModule_run():import pytest
from unittest.mock import MagicMock, patch

from ansible.errors import AnsibleError
from ansible.playbook.task import Task
from ansible.template import Templar
from ansible.module_utils.common.arg_spec import ArgumentSpecValidator

try:
    from plugins.action.validate import ActionModule
except ImportError:
    from ansible.plugins.action.validate import ActionModule


def _make_action(task_args=None, task_vars=None):
    """Build an ActionModule with mocked _task/_templar/play_context."""
    task = MagicMock()
    task.async_val = 0
    task.args = task_args if task_args is not None else {}
    task.diff = False
    task.check_mode = False
    task.action = 'validate_argument_spec'

    play_context = MagicMock()
    play_context.check_mode = False
    play_context.become = False
    play_context.become_user = None
    play_context.become_method = None
    play_context.shell = '/bin/sh'
    play_context.network_os = None

    connection = MagicMock()
    connection._shell = MagicMock()
    connection._shell.tmpdir = None
    connection._shell.path_prefix = None
    connection.become = None

    am = ActionModule(task, connection, play_context, loader=None,
                      templar=None, shared_loader_obj=None)
    am._templar = MagicMock()
    am._templar.template = lambda x: x
    return am


VALID_SPEC = {
    'name': {'type': 'str', 'required': True},
    'count': {'type': 'int', 'default': 1},
}


def test_run_success_with_provided_arguments():
    task_args = {
        'argument_spec': VALID_SPEC,
        'provided_arguments': {'name': 'foo', 'count': 2},
    }
    am = _make_action(task_args=task_args, task_vars={})
    result = am.run(task_vars={})

    assert result.get('failed') is not True
    assert result['changed'] is False
    assert result['msg'] == 'The arg spec validation passed'
    assert 'argument_errors' not in result


def test_run_success_defaults_applied():
    task_args = {
        'argument_spec': VALID_SPEC,
        'provided_arguments': {'name': 'foo'},
    }
    am = _make_action(task_args=task_args, task_vars={})
    result = am.run(task_vars={})

    assert result.get('failed') is not True
    assert result['changed'] is False


def test_run_validation_failure_returns_errors():
    task_args = {
        'argument_spec': VALID_SPEC,
        'provided_arguments': {'count': 'not-an-int'},
    }
    am = _make_action(task_args=task_args, task_vars={})
    result = am.run(task_vars={})

    assert result['failed'] is True
    assert 'Validation of arguments failed:' in result['msg']
    assert result['argument_spec_data'] == VALID_SPEC
    assert isinstance(result['argument_errors'], list)
    assert len(result['argument_errors']) > 0


def test_run_missing_required_argument_fails():
    task_args = {
        'argument_spec': VALID_SPEC,
        'provided_arguments': {'count': 1},  # missing required 'name'
    }
    am = _make_action(task_args=task_args, task_vars={})
    result = am.run(task_vars={})

    assert result['failed'] is True
    assert any('name' in err for err in result['argument_errors'])


def test_run_args_from_task_vars_merged():
    task_args = {
        'argument_spec': VALID_SPEC,
        'provided_arguments': {},
    }
    am = _make_action(task_args=task_args, task_vars={'name': 'from-vars'})
    result = am.run(task_vars={'name': 'from-vars'})

    assert result.get('failed') is not True
    assert result['changed'] is False


def test_run_validate_args_context_included():
    ctx = {'role': 'myrole', 'entry_point': 'main'}
    task_args = {
        'argument_spec': VALID_SPEC,
        'provided_arguments': {'name': 'x'},
        'validate_args_context': ctx,
    }
    am = _make_action(task_args=task_args, task_vars={})
    result = am.run(task_vars={})

    assert result['validate_args_context'] == ctx


def test_run_missing_argument_spec_raises():
    am = _make_action(task_args={}, task_vars={})
    with pytest.raises(AnsibleError) as excinfo:
        am.run(task_vars={})
    assert '"argument_spec" arg is required' in str(excinfo.value)


def test_run_bad_argument_spec_type_raises():
    task_args = {'argument_spec': ['not', 'a', 'dict']}
    am = _make_action(task_args=task_args, task_vars={})
    with pytest.raises(AnsibleError) as excinfo:
        am.run(task_vars={})
    assert 'Incorrect type for argument_spec' in str(excinfo.value)


def test_run_bad_provided_arguments_type_raises():
    task_args = {
        'argument_spec': VALID_SPEC,
        'provided_arguments': 'not-a-dict',
    }
    am = _make_action(task_args=task_args, task_vars={})
    with pytest.raises(AnsibleError) as excinfo:
        am.run(task_vars={})
    assert 'Incorrect type for provided_arguments' in str(excinfo.value)


def test_run_none_task_vars_defaults_to_empty_dict():
    task_args = {
        'argument_spec': VALID_SPEC,
        'provided_arguments': {'name': 'foo'},
    }
    am = _make_action(task_args=task_args, task_vars=None)
    result = am.run(task_vars=None)

    assert result['changed'] is False
    assert result['msg'] == 'The arg spec validation passed'


def test_run_templated_task_vars_are_resolved():
    task_args = {
        'argument_spec': VALID_SPEC,
        'provided_arguments': {},
    }
    am = _make_action(task_args=task_args, task_vars={'name': '{{ myvar }}'})
    # Simulate templating resolving the variable
    am._templar.template = lambda x: {k: 'resolved' for k in x}
    result = am.run(task_vars={'name': '{{ myvar }}', 'myvar': 'resolved'})

    assert result.get('failed') is not True
    assert result['changed'] is False

# Generated at 2026-11-01 18:41:08.740358
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from unittest.mock import MagicMock

    task = MagicMock()
    connection = MagicMock()
    play_context = MagicMock()
    loader = MagicMock()
    templar = MagicMock()
    shared_loader_obj = MagicMock()

    am = ActionModule(task=task, connection=connection, play_context=play_context,
                      loader=loader, templar=templar, shared_loader_obj=shared_loader_obj)

    assert isinstance(am, ActionModule)
    assert am._task is task
    assert am._connection is connection
    assert am._play_context is play_context
    assert am._loader is loader
    assert am._templar is templar
    assert am._shared_loader_obj is shared_loader_obj
    assert am.TRANSFERS_FILES is False

# Generated at 2026-11-01 18:41:29.021185
# Unit test for constructor of class ActionModule
def test_ActionModule():am = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

# Generated at 2026-11-01 18:41:45.974900
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Mock the required objects for ActionBase's constructor
    task = MagicMock()
    task.action = 'validate_argument_spec'
    task.args = {'argument_spec': {'my_opt': {'type': 'str'}}}

    connection = MagicMock()
    connection._shell.env = {}

    play_context = MagicMock()
    loader = MagicMock()
    templar = MagicMock()
    shared_loader_obj = MagicMock()

    # Instantiate the ActionModule
    action = ActionModule(
        task=task,
        connection=connection,
        play_context=play_context,
        loader=loader,
        templar=templar,
        shared_loader_obj=shared_loader_obj,
    )

    # Verify the instance was constructed correctly
    assert isinstance(action, ActionModule)
    assert action._task is task
    assert action._connection is connection
    assert action._play_context is play_context
    assert action._loader is loader
    assert action._templar is templar
    assert action._shared_loader_obj is shared_loader_obj
    assert action.TRANSFERS_FILES is False
    assert callable(action.run)
    assert callable(action.get_args_from_task_vars)

# Generated at 2026-11-01 18:42:05.372644
# Unit test for method get_args_from_task_vars of class ActionModule
def test_ActionModule_get_args_from_task_vars():
    class FakeTemplar(object):
        """Minimal templar stand-in; uppercases strings so we can verify templating occurred."""
        def template(self, data):
            if isinstance(data, dict):
                return dict((k, self.template(v)) for k, v in data.items())
            if isinstance(data, string_types):
                return data.upper()
            return data

    # Build instance without invoking the heavyweight ActionBase constructor;
    # get_args_from_task_vars only relies on self._templar.
    action_mod = ActionModule.__new__(ActionModule)
    action_mod._templar = FakeTemplar()

    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
    }

    task_vars = {
        'name': 'fred',
        'age': 42,
        'unrelated': 'should be ignored',
    }

    # Only keys present in both argument_spec and task_vars are collected,
    # and they are passed through the templar.
    result = action_mod.get_args_from_task_vars(argument_spec, task_vars)
    assert result == {'name': 'FRED', 'age': 42}

    # No overlapping vars yields an empty dict.
    result = action_mod.get_args_from_task_vars({'missing': {'type': 'str'}}, {})
    assert result == {}

    # Empty argument spec yields an empty dict even with vars present.
    result = action_mod.get_args_from_task_vars({}, {'name': 'fred'})
    assert result == {}

    # Non-string values pass through templating untouched.
    nested_spec = {'count': {'type': 'int'}}
    result = action_mod.get_args_from_task_vars(nested_spec, {'count': [1, 2, 3]})
    assert result == {'count': [1, 2, 3]}

# Generated at 2026-11-01 18:42:15.102663
# Unit test for constructor of class ActionModule
def test_ActionModule():
    ''' Test the constructor of ActionModule '''
    from unittest.mock import MagicMock

    task = MagicMock()
    connection = MagicMock()
    play_context = MagicMock()

    action_module = ActionModule(task, connection, play_context,
                                 loader=None, templar=None, shared_loader_obj=None)

    assert isinstance(action_module, ActionModule)
    assert action_module.TRANSFERS_FILES is False

# Generated at 2026-11-01 18:42:19.157040
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from unittest.mock import MagicMock

    task = MagicMock()
    connection = MagicMock()
    play_context = MagicMock()
    loader = MagicMock()
    templar = MagicMock()
    shared_loader_obj = MagicMock()

    action_module = ActionModule(
        task=task,
        connection=connection,
        play_context=play_context,
        loader=loader,
        templar=templar,
        shared_loader_obj=shared_loader_obj
    )

    assert isinstance(action_module, ActionModule)
    assert isinstance(action_module, ActionBase)
    assert action_module.TRANSFERS_FILES is False
    assert action_module._task is task

# Generated at 2026-11-01 18:42:35.339983
# Unit test for constructor of class ActionModule
def test_ActionModule():from unittest.mock import MagicMock


# Generated at 2026-11-01 18:42:57.805549
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-11-01 18:43:03.724550
# Unit test for method get_args_from_task_vars of class ActionModule
def test_ActionModule_get_args_from_task_vars():am = object.__new__(ActionModule)


# Generated at 2026-11-01 18:43:20.609393
# Unit test for method get_args_from_task_vars of class ActionModule
def test_ActionModule_get_args_from_task_vars():am = ActionModule.__new__(ActionModule)


# Generated at 2026-11-01 18:43:25.647050
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """
    Test that the ActionModule constructor properly initializes the object
    by passing mocked dependencies to ActionBase.
    """
    from unittest.mock import MagicMock

    fake_task = MagicMock()
    fake_connection = MagicMock()
    fake_play_context = MagicMock()
    fake_loader = MagicMock()
    fake_templar = MagicMock()
    fake_shared_loader_obj = MagicMock()

    action_module = ActionModule(
        task=fake_task,
        connection=fake_connection,
        play_context=fake_play_context,
        loader=fake_loader,
        templar=fake_templar,
        shared_loader_obj=fake_shared_loader_obj,
    )

    # Verify an instance of ActionModule was created successfully
    assert isinstance(action_module, ActionModule)

    # Verify inherited attributes from ActionBase were assigned correctly
    assert action_module._task is fake_task
    assert action_module._connection is fake_connection
    assert action_module._play_context is fake_play_context
    assert action_module._loader is fake_loader
    assert action_module._templar is fake_templar
    assert action_module._shared_loader_obj is fake_shared_loader_obj

    # Verify class-level attributes
    assert action_module.TRANSFERS_FILES is False

# Generated at 2026-11-01 18:44:04.797048
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-11-01 18:44:09.936979
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-11-01 18:44:18.181950
# Unit test for method get_args_from_task_vars of class ActionModule
def test_ActionModule_get_args_from_task_vars():from ansible.module_utils.six import string_types


# Generated at 2026-11-01 18:44:49.119086
# Unit test for method run of class ActionModule

# Generated at 2026-11-01 18:45:18.509001
# Unit test for method run of class ActionModule

# Generated at 2026-11-01 18:45:23.819016
# Unit test for method run of class ActionModule
def test_ActionModule_run():am = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

# Generated at 2026-11-01 18:45:36.006388
# Unit test for method get_args_from_task_vars of class ActionModule
def test_ActionModule_get_args_from_task_vars():
    '''
    Test that get_args_from_task_vars picks up only the arguments present in
    the argument spec from task_vars and returns them after templating.
    '''
    action = _make_action_module()

    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
    }
    task_vars = {
        'name': 'bob',
        'age': 42,
        'unrelated': 'not in spec',
    }

    templated_result = {'name': 'bob', 'age': 42}
    action._templar.template.return_value = templated_result

    result = action.get_args_from_task_vars(argument_spec, task_vars)

    assert result == {'name': 'bob', 'age': 42}
    action._templar.template.assert_called_once_with({'name': 'bob', 'age': 42})


def test_ActionModule_get_args_from_task_vars_no_matching_vars():
    '''
    Test that get_args_from_task_vars returns an empty dict when no task_vars
    match the argument spec names.
    '''
    action = _make_action_module()

    argument_spec = {'name': {'type': 'str'}}
    task_vars = {'other_var': 'value'}

    action._templar.template.return_value = {}

    result = action.get_args_from_task_vars(argument_spec, task_vars)

    assert result == {}
    action._templar.template.assert_called_once_with({})


def test_ActionModule_get_args_from_task_vars_templated_values():
    '''
    Test that templated task var values are expanded via the templar before
    being returned.
    '''
    action = _make_action_module()

    argument_spec = {'name': {'type': 'str'}}
    task_vars = {'name': '{{ my_var }}'}

    action._templar.template.return_value = {'name': 'resolved_value'}

    result = action.get_args_from_task_vars(argument_spec, task_vars)

    assert result == {'name': 'resolved_value'}

# Generated at 2026-11-01 18:45:44.810127
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from unittest.mock import MagicMock

    # Mock the dependencies required by ActionBase's constructor
    task = MagicMock()
    connection = MagicMock()
    play_context = MagicMock()
    loader = MagicMock()
    templar = MagicMock()
    shared_loader_obj = MagicMock()

    action_module = ActionModule(
        task=task,
        connection=connection,
        play_context=play_context,
        loader=loader,
        templar=templar,
        shared_loader_obj=shared_loader_obj
    )

    # Verify the instance was created and inherits from ActionBase
    assert isinstance(action_module, ActionModule)
    assert isinstance(action_module, ActionBase)

    # Verify class attributes and stored dependencies
    assert action_module.TRANSFERS_FILES is False
    assert action_module._task is task
    assert action_module._connection is connection
    assert action_module._play_context is play_context
    assert action_module._loader is loader
    assert action_module._templar is templar
    assert action_module._shared_loader_obj is shared_loader_obj

# Generated at 2026-11-01 18:46:14.199453
# Unit test for constructor of class ActionModule

# Generated at 2026-11-01 18:46:36.188507
# Unit test for constructor of class ActionModule
def test_ActionModule():from unittest.mock import MagicMock


# Generated at 2026-11-01 18:46:40.447675
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''
    Test the constructor of ActionModule.
    '''
    from unittest.mock import MagicMock

    task = MagicMock()
    connection = MagicMock()
    play_context = MagicMock()
    loader = MagicMock()
    templar = MagicMock()
    shared_loader_obj = MagicMock()

    action_module = ActionModule(
        task=task,
        connection=connection,
        play_context=play_context,
        loader=loader,
        templar=templar,
        shared_loader_obj=shared_loader_obj
    )

    # Verify the instance is created and inherits from ActionBase
    assert action_module is not None
    assert isinstance(action_module, ActionModule)
    assert isinstance(action_module, ActionBase)

    # Verify class attributes
    assert ActionModule.TRANSFERS_FILES is False

    # Verify the task was assigned
    assert action_module._task is task

# Generated at 2026-11-01 18:47:13.078761
# Unit test for method run of class ActionModule

# Generated at 2026-11-01 18:47:42.979133
# Unit test for method run of class ActionModule

# Generated at 2026-11-01 18:47:50.351105
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from unittest.mock import MagicMock, patch

    argument_spec = {
        'name': {'type': 'str', 'required': True},
        'count': {'type': 'int', 'required': False, 'default': 1},
    }

    provided_arguments = {'name': 'hello', 'count': 42}

    mock_task = MagicMock()
    mock_task.args = {
        'argument_spec': argument_spec,
        'provided_arguments': provided_arguments,
        'validate_args_context': {'role': 'my_role'},
    }

    mock_templar = MagicMock()
    mock_templar.template.side_effect = lambda x: x

    am = ActionModule(
        task=mock_task,
        connection=MagicMock(),
        play_context=MagicMock(),
        loader=MagicMock(),
        templar=mock_templar,
        shared_loader_obj=MagicMock()
    )

    with patch.object(ActionBase, 'run', return_value={}):
        result = am.run(task_vars={})

    assert result['changed'] is False
    assert result['msg'] == 'The arg spec validation passed'
    assert 'failed' not in result
    assert result['validate_args_context'] == {'role': 'my_role'}

# Generated at 2026-11-01 18:48:19.739440
# Unit test for method run of class ActionModule

# Generated at 2026-11-01 18:48:48.104134
# Unit test for method run of class ActionModule

# Generated at 2026-11-01 18:49:00.600377
# Unit test for method run of class ActionModule
def test_ActionModule_run():from unittest.mock import MagicMock, patch

    # Success case: provided arguments match the argument spec

# Generated at 2026-11-01 18:49:10.673602
# Unit test for method run of class ActionModule

# Generated at 2026-11-01 18:49:48.184820
# Unit test for method run of class ActionModule

# Generated at 2026-11-01 18:50:01.725817
# Unit test for method run of class ActionModule
def test_ActionModule_run():am = ActionModule.__new__(ActionModule)

# Generated at 2026-11-01 18:50:26.561817
# Unit test for method run of class ActionModule

# Generated at 2026-11-01 18:50:55.078134
# Unit test for method run of class ActionModule
def test_ActionModule_run():from unittest.mock import patch, MagicMock
