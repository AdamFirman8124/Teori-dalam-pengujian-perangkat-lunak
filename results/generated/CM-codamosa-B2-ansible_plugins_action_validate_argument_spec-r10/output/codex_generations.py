

# Generated at 2026-11-03 02:51:57.845508
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule(
        task=MagicMock(),
        connection=MagicMock(),
        play_context=MagicMock(),
        loader=MagicMock(),
        templar=MagicMock(),
        shared_loader_obj=MagicMock()
    )
    assert action is not None
    assert isinstance(action, ActionModule)
    assert action.TRANSFERS_FILES is False

# Generated at 2026-11-03 02:54:23.461900
# Unit test for constructor of class ActionModule
def test_ActionModule():action = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

# Generated at 2026-11-03 02:57:27.259829
# Unit test for method get_args_from_task_vars of class ActionModule
def test_ActionModule_get_args_from_task_vars():
    try:
        from unittest.mock import MagicMock
    except ImportError:
        from mock import MagicMock

    argument_spec = {
        'name': {'type': 'str', 'required': True},
        'age': {'type': 'int'},
        'not_in_vars': {'type': 'str'},
    }

    task_vars = {
        'name': 'bob',
        'age': 42,
        'unrelated': 'ignored',
    }

    am = ActionModule(task=MagicMock(), connection=MagicMock(),
                      play_context=MagicMock(), loader=MagicMock(),
                      templar=MagicMock(), shared_loader_obj=MagicMock())

    # Passthrough templar
    am._templar.template.side_effect = lambda value: value

    # Only arguments present in both argument_spec and task_vars are returned
    result = am.get_args_from_task_vars(argument_spec, task_vars)
    assert result == {'name': 'bob', 'age': 42}
    am._templar.template.assert_called_once_with({'name': 'bob', 'age': 42})

    # No matching task vars yields an empty dict
    assert am.get_args_from_task_vars(argument_spec, {}) == {}

    # Values are passed through the templar, simulating variable expansion
    def fake_template(value):
        if isinstance(value, dict):
            return dict((k, v.upper() if isinstance(v, string_types) else v)
                        for k, v in iteritems(value))
        return value

    am._templar.template.side_effect = fake_template

    templated_vars = {'name': '{{ user_name }}'}
    result = am.get_args_from_task_vars(argument_spec, templated_vars)
    assert result == {'name': '{{ USER_NAME }}'}

# Generated at 2026-11-03 02:59:41.202099
# Unit test for method get_args_from_task_vars of class ActionModule
def test_ActionModule_get_args_from_task_vars():
    from unittest.mock import MagicMock

    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
        'city': {'type': 'str', 'default': 'nyc'},
    }
    task_vars = {
        'name': 'bob',
        'age': 42,
        'city': 'chicago',
        'not_in_spec': 'ignored',
    }

    templar = MagicMock()
    templar.template.side_effect = lambda value: value

    am = ActionModule(
        task=dict(),
        connection=None,
        play_context=dict(),
        loader=None,
        templar=templar,
        shared_loader_obj=None,
    )

    result = am.get_args_from_task_vars(argument_spec, task_vars)

    # Only arguments present in both the arg spec and task_vars are returned
    assert result == {'name': 'bob', 'age': 42, 'city': 'chicago'}


def test_ActionModule_get_args_from_task_vars_templated():
    from unittest.mock import MagicMock

    argument_spec = {'name': {'type': 'str'}}
    task_vars = {'name': '{{ some_var }}'}

    templar = MagicMock()
    templar.template.return_value = {'name': 'resolved_value'}

    am = ActionModule(
        task=dict(),
        connection=None,
        play_context=dict(),
        loader=None,
        templar=templar,
        shared_loader_obj=None,
    )

    result = am.get_args_from_task_vars(argument_spec, task_vars)

    assert result == {'name': 'resolved_value'}
    templar.template.assert_called_once_with({'name': '{{ some_var }}'})


def test_ActionModule_get_args_from_task_vars_empty():
    from unittest.mock import MagicMock

    argument_spec = {'name': {'type': 'str'}}
    task_vars = {}

    templar = MagicMock()
    templar.template.side_effect = lambda value: value

    am = ActionModule(
        task=dict(),
        connection=None,
        play_context=dict(),
        loader=None,
        templar=templar,
        shared_loader_obj=None,
    )

    result = am.get_args_from_task_vars(argument_spec, task_vars)

    assert result == {}