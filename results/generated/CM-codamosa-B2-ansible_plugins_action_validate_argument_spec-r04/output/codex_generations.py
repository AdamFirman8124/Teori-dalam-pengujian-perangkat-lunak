

# Generated at 2026-11-02 00:01:27.644502
# Unit test for constructor of class ActionModule
def test_ActionModule():
    task = MagicMock()
    connection = MagicMock()
    play_context = MagicMock()
    loader = MagicMock()
    templar = MagicMock()
    shared_loader_obj = MagicMock()

    action_module = ActionModule(
        task, connection, play_context, loader, templar, shared_loader_obj
    )

    assert isinstance(action_module, ActionModule)
    assert action_module.TRANSFERS_FILES is False
    assert action_module._task is task

# Generated at 2026-11-02 00:02:06.456743
# Unit test for constructor of class ActionModule
def test_ActionModule():from unittest.mock import MagicMock


# Generated at 2026-11-02 00:02:45.412217
# Unit test for method get_args_from_task_vars of class ActionModule
def test_ActionModule_get_args_from_task_vars():
    from unittest.mock import MagicMock

    # Build an ActionModule instance without invoking ActionBase.__init__
    action_module = ActionModule.__new__(ActionModule)
    action_module._templar = MagicMock()
    action_module._templar.template.side_effect = lambda args: args

    argument_spec = {
        'name': {'type': 'str', 'required': True},
        'age': {'type': 'int'},
    }
    task_vars = {
        'name': 'bob',
        'age': 42,
        'unrelated': 'not in the arg spec',
    }

    result = action_module.get_args_from_task_vars(argument_spec, task_vars)

    # Only args present in both the spec and task vars are returned
    assert result == {'name': 'bob', 'age': 42}
    assert 'unrelated' not in result

    # The gathered args are passed through the templar
    action_module._templar.template.assert_called_once_with({'name': 'bob', 'age': 42})


def test_ActionModule_get_args_from_task_vars_no_matches():
    from unittest.mock import MagicMock

    action_module = ActionModule.__new__(ActionModule)
    action_module._templar = MagicMock()
    action_module._templar.template.side_effect = lambda args: args

    result = action_module.get_args_from_task_vars({'name': {'type': 'str'}}, {'other': 'value'})
    assert result == {}


def test_ActionModule_get_args_from_task_vars_empty():
    from unittest.mock import MagicMock

    action_module = ActionModule.__new__(ActionModule)
    action_module._templar = MagicMock()
    action_module._templar.template.side_effect = lambda args: args

    assert action_module.get_args_from_task_vars({}, {}) == {}


def test_ActionModule_get_args_from_task_vars_templates_values():
    from unittest.mock import MagicMock

    action_module = ActionModule.__new__(ActionModule)
    action_module._templar = MagicMock()
    action_module._templar.template.return_value = {'name': 'templated_value'}

    argument_spec = {'name': {'type': 'str'}}
    task_vars = {'name': '{{ some_var }}'}

    result = action_module.get_args_from_task_vars(argument_spec, task_vars)

    # Templated values are expanded via the templar

# Generated at 2026-11-02 00:04:30.228790
# Unit test for method run of class ActionModule

# Generated at 2026-11-02 00:06:02.962381
# Unit test for method run of class ActionModule

# Generated at 2026-11-02 00:08:07.622829
# Unit test for method run of class ActionModule

# Generated at 2026-11-02 00:09:19.714421
# Unit test for method get_args_from_task_vars of class ActionModule
def test_ActionModule_get_args_from_task_vars():
    try:
        from unittest.mock import MagicMock
    except ImportError:
        from mock import MagicMock

    argument_spec = {
        'first_name': {'type': 'str', 'required': True},
        'last_name': {'type': 'str'},
        'age': {'type': 'int'},
    }

    action_module = ActionModule(
        task=MagicMock(),
        connection=MagicMock(),
        play_context=MagicMock(),
        loader=MagicMock(),
        templar=MagicMock(),
        shared_loader_obj=MagicMock(),
    )

    # Case 1: all arguments in the spec exist in task_vars; extras are ignored
    task_vars = {
        'first_name': 'Fred',
        'last_name': 'Smith',
        'age': 30,
        'not_in_spec': 'should be ignored',
    }

    templated_values = {'first_name': 'FRED', 'last_name': 'SMITH', 'age': 30}
    action_module._templar = MagicMock()
    action_module._templar.template.return_value = templated_values

    result = action_module.get_args_from_task_vars(argument_spec, task_vars)

    assert result == templated_values
    action_module._templar.template.assert_called_once_with(
        {'first_name': 'Fred', 'last_name': 'Smith', 'age': 30}
    )

    # Case 2: only some of the spec arguments exist in task_vars
    partial_task_vars = {'first_name': 'Barney'}
    action_module._templar = MagicMock()
    action_module._templar.template.return_value = {'first_name': 'BARNEY'}

    result = action_module.get_args_from_task_vars(argument_spec, partial_task_vars)

    assert result == {'first_name': 'BARNEY'}
    action_module._templar.template.assert_called_once_with({'first_name': 'Barney'})

    # Case 3: none of the spec arguments exist in task_vars
    action_module._templar = MagicMock()
    action_module._templar.template.return_value = {}

    result = action_module.get_args_from_task_vars(argument_spec, {'other_var': 1})

    assert result == {}
    action_module._templar.template.assert_called_once_with({})

# Generated at 2026-11-02 00:10:13.383190
# Unit test for constructor of class ActionModule
def test_ActionModule():
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
        shared_loader_obj=shared_loader_obj,
    )

    assert isinstance(action_module, ActionModule)
    assert action_module.TRANSFERS_FILES is False
    assert hasattr(action_module, 'get_args_from_task_vars')
    assert hasattr(action_module, 'run')