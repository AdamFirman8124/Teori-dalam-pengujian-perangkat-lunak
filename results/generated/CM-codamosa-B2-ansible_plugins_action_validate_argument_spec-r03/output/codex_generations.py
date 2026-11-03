

# Generated at 2026-11-02 23:30:50.301050
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

    assert isinstance(action_module, ActionModule)
    assert action_module._task is task
    assert action_module._connection is connection
    assert action_module.TRANSFERS_FILES is False

# Generated at 2026-11-02 23:31:48.529346
# Unit test for constructor of class ActionModule

# Generated at 2026-11-02 23:32:59.729951
# Unit test for constructor of class ActionModule
def test_ActionModule():from unittest.mock import MagicMock


# Generated at 2026-11-02 23:34:02.917604
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''Test the constructor of class ActionModule.'''
    from unittest.mock import MagicMock

    mock_task = MagicMock()
    mock_task.async_val = False
    mock_task.args = {}

    action_module = ActionModule(
        task=mock_task,
        connection=MagicMock(),
        play_context=MagicMock(),
        loader=MagicMock(),
        templar=MagicMock(),
        shared_loader_obj=MagicMock(),
    )

    assert action_module is not None
    assert isinstance(action_module, ActionBase)
    assert action_module.TRANSFERS_FILES is False
    assert action_module._task is mock_task

# Generated at 2026-11-02 23:35:40.298897
# Unit test for method get_args_from_task_vars of class ActionModule
def test_ActionModule_get_args_from_task_vars():
    from unittest.mock import MagicMock

    argument_spec = {
        'name': {'type': 'str'},
        'count': {'type': 'int'},
    }

    am = ActionModule.__new__(ActionModule)
    am._templar = MagicMock()
    am._templar.template.side_effect = lambda value: value

    # Values present in task_vars for names in the argument spec are collected
    task_vars = {'name': 'web1', 'count': 3, 'unrelated': 'ignored'}
    args = am.get_args_from_task_vars(argument_spec, task_vars)
    assert args == {'name': 'web1', 'count': 3}

    # Templar is invoked with the collected args
    am._templar.template.assert_called_once_with({'name': 'web1', 'count': 3})

    # No matching task vars yields an empty dict
    args = am.get_args_from_task_vars(argument_spec, {})
    assert args == {}

    # Templated values in task_vars are expanded via the templar
    am._templar = MagicMock()
    am._templar.template.side_effect = lambda value: dict((k, v + '-expanded') for k, v in value.items())
    args = am.get_args_from_task_vars(argument_spec, {'name': 'web1'})
    assert args == {'name': 'web1-expanded'}

# Generated at 2026-11-02 23:38:26.600278
# Unit test for method get_args_from_task_vars of class ActionModule
def test_ActionModule_get_args_from_task_vars():
    try:
        from unittest.mock import MagicMock
    except ImportError:
        from mock import MagicMock

    argument_spec = {
        'name': {'type': 'str', 'required': True},
        'age': {'type': 'int', 'default': 18},
        'color': {'type': 'str'},
    }
    task_vars = {
        'name': 'bob',
        'age': 30,
        'color': 'red',
        'not_in_spec': 'ignored',
    }

    action_module = ActionModule(
        task=MagicMock(),
        connection=MagicMock(),
        play_context=MagicMock(),
        loader=MagicMock(),
        templar=MagicMock(),
        shared_loader_obj=MagicMock(),
    )

    # Simulate templating: '{{ ... }}' strings get expanded to a concrete value