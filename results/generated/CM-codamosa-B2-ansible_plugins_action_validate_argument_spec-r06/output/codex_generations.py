

# Generated at 2026-11-02 21:21:29.537878
# Unit test for method get_args_from_task_vars of class ActionModule
def test_ActionModule_get_args_from_task_vars():
    from unittest.mock import MagicMock

    argument_spec = {
        'name': {'type': 'str', 'required': True},
        'count': {'type': 'int'},
        'items': {'type': 'list'},
    }

    task_vars = {
        'name': 'some_name',
        'count': 3,
        'items': ['a', 'b'],
        'extra_var': 'not in the spec',
    }

    action_module = ActionModule.__new__(ActionModule)
    action_module._templar = MagicMock()
    action_module._templar.template.side_effect = lambda value: value

    # Only keys present in both the arg spec and task vars are collected,
    # and the collected values are run through the templar.
    result = action_module.get_args_from_task_vars(argument_spec, task_vars)
    assert result == {'name': 'some_name', 'count': 3, 'items': ['a', 'b']}
    action_module._templar.template.assert_called_once_with(
        {'name': 'some_name', 'count': 3, 'items': ['a', 'b']}
    )

    # Templated values are what get returned
    action_module._templar = MagicMock()
    action_module._templar.template.return_value = {'name': 'TEMPLATED'}
    result = action_module.get_args_from_task_vars(
        {'name': {'type': 'str'}}, {'name': '{{ some_var }}'}
    )
    assert result == {'name': 'TEMPLATED'}

    # No task vars matching the spec results in an empty dict being templated
    action_module._templar = MagicMock()
    action_module._templar.template.return_value = {}
    result = action_module.get_args_from_task_vars(argument_spec, {'unrelated': 'var'})
    assert result == {}
    action_module._templar.template.assert_called_once_with({})

# Generated at 2026-11-02 21:22:30.269870
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = _get_action(task_args={'argument_spec': {}})

    assert action is not None
    assert isinstance(action, ActionModule)
    assert action.TRANSFERS_FILES is False
    assert hasattr(action, 'run')
    assert hasattr(action, 'get_args_from_task_vars')
    assert callable(action.run)
    assert callable(action.get_args_from_task_vars)

# Generated at 2026-11-02 21:24:44.492772
# Unit test for constructor of class ActionModule
def test_ActionModule():
    task = MagicMock()
    connection = MagicMock()
    play_context = MagicMock()
    loader = MagicMock()
    templar = MagicMock()
    shared_loader_obj = MagicMock()

    action_module = ActionModule(task, connection, play_context, loader, templar, shared_loader_obj)

    assert isinstance(action_module, ActionModule)
    assert action_module._task is task
    assert action_module._connection is connection
    assert action_module._play_context is play_context
    assert action_module._loader is loader
    assert action_module._templar is templar
    assert action_module._shared_loader_obj is shared_loader_obj
    assert action_module.TRANSFERS_FILES is False

# Generated at 2026-11-02 21:26:53.975735
# Unit test for constructor of class ActionModule
def test_ActionModule():from unittest.mock import MagicMock

# Generated at 2026-11-02 21:28:39.509910
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from unittest.mock import MagicMock

    task = MagicMock()
    task.args = {}
    connection = MagicMock()
    play_context = MagicMock()
    loader = MagicMock()
    templar = MagicMock()
    shared_loader_obj = MagicMock()

    action_module = ActionModule(task, connection, play_context, loader, templar, shared_loader_obj)

    assert action_module._task == task
    assert action_module._connection == connection
    assert action_module._play_context == play_context
    assert action_module._loader == loader
    assert action_module._templar == templar
    assert action_module._shared_loader_obj == shared_loader_obj
    assert action_module.TRANSFERS_FILES is False

# Generated at 2026-11-02 21:29:37.666881
# Unit test for constructor of class ActionModule
def test_ActionModule():task = {"name": "test task"}