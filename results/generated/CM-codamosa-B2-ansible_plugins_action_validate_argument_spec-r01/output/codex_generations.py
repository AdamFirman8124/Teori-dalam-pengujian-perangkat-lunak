

# Generated at 2026-11-01 22:12:22.893074
# Unit test for method get_args_from_task_vars of class ActionModule
def test_ActionModule_get_args_from_task_vars():
    argument_spec = {
        'name': {'type': 'str', 'required': True},
        'age': {'type': 'int', 'default': 18},
        'city': {'type': 'str'},
    }
    task_vars = {
        'name': '{{ person_name }}',
        'age': 42,
        'city': 'Springfield',
        'unrelated_var': 'should_not_be_included',
    }

    am = ActionModule.__new__(ActionModule)
    templar = MagicMock()

    def fake_template(value):
        # Simulate templating: resolve simple '{{ var }}' strings
        if isinstance(value, dict):
            return dict((k, fake_template(v)) for k, v in iteritems(value))
        if isinstance(value, string_types) and value.startswith('{{') and value.endswith('}}'):
            return 'Alice'
        return value

    templar.template.side_effect = fake_template
    am._templar = templar

    # Only args present in both argument_spec and task_vars should be returned
    result = am.get_args_from_task_vars(argument_spec, task_vars)

    assert result == {'name': 'Alice', 'age': 42, 'city': 'Springfield'}

    # Templating must be applied exactly once to the filtered args dict
    templar.template.assert_called_once_with(
        {'name': '{{ person_name }}', 'age': 42, 'city': 'Springfield'}
    )

    # No overlapping variables between arg spec and task vars -> empty dict
    result_no_match = am.get_args_from_task_vars({'other_arg': {'type': 'str'}}, task_vars)
    assert result_no_match == {}

    # Empty task vars -> empty dict
    result_empty_vars = am.get_args_from_task_vars(argument_spec, {})
    assert result_empty_vars == {}

    # Empty argument spec -> empty dict
    result_empty_spec = am.get_args_from_task_vars({}, task_vars)
    assert result_empty_spec == {}

# Generated at 2026-11-01 22:13:04.673402
# Unit test for method get_args_from_task_vars of class ActionModule
def test_ActionModule_get_args_from_task_vars():
    from unittest.mock import MagicMock


# Generated at 2026-11-01 22:13:58.841359
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    task_args = {
        'validate_args_context': {'type': 'role', 'name': 'my_role'},
        'argument_spec': {
            'name': {'type': 'str', 'required': True},
            'age': {'type': 'int', 'default': 18},
        },
        'provided_arguments': {'name': 'bob'},
    }
    action = _get_action(task_args)

    with patch.object(ActionBase, 'run', autospec=True, return_value={}):
        result = action.run(tmp=None, task_vars={})


# Generated at 2026-11-01 22:15:04.377121
# Unit test for method get_args_from_task_vars of class ActionModule
def test_ActionModule_get_args_from_task_vars():
    '''
    Test that get_args_from_task_vars:
      * collects only argument names present in BOTH the argument spec and task_vars
      * runs the collected values through the templar before returning them
    '''
    argument_spec = {
        'name': {'type': 'str', 'required': True},
        'count': {'type': 'int', 'default': 1},
    }
    task_vars = {
        'name': '{{ some_name }}',
        'count': 42,
        'unrelated': 'should_be_ignored',
    }

    # Fake templar that simulates expanding '{{ some_name }}'
    templar = MagicMock()

    def fake_template(data):
        if isinstance(data, dict):
            return {k: fake_template(v) for k, v in data.items()}
        if isinstance(data, str) and data == '{{ some_name }}':
            return 'Alice'
        return data

    templar.template.side_effect = fake_template

    action_module = ActionModule(
        task=MagicMock(),
        connection=MagicMock(),
        play_context=MagicMock(),
        loader=MagicMock(),
        templar=templar,
        shared_loader_obj=MagicMock(),
    )

    result = action_module.get_args_from_task_vars(argument_spec, task_vars)

    # Only keys declared in the argument spec are pulled from task vars
    assert set(result.keys()) == {'name', 'count'}

    # Values were expanded through templar.template()
    assert result['name'] == 'Alice'
    assert result['count'] == 42

    # Templating was invoked exactly once with the collected raw args
    templar.template.assert_called_once_with({'name': '{{ some_name }}', 'count': 42})

# Generated at 2026-11-01 22:15:46.364006
# Unit test for method get_args_from_task_vars of class ActionModule
def test_ActionModule_get_args_from_task_vars():
    '''Only arguments present in both the arg spec and task_vars are returned, and are templated.'''
    argument_spec = {
        'name': {'type': 'str', 'required': True},
        'count': {'type': 'int'},
        'missing': {'type': 'str'},
    }
    task_vars = {
        'name': 'webserver',
        'count': 3,
        'unrelated': 'should not be picked up',
    }
    templar = MagicMock()
    templar.template.side_effect = lambda value: value

    action = _make_action_module(templar=templar)
    result = action.get_args_from_task_vars(argument_spec, task_vars)

    assert result == {'name': 'webserver', 'count': 3}
    templar.template.assert_called_once_with({'name': 'webserver', 'count': 3})


def test_ActionModule_get_args_from_task_vars_templates_values():
    '''Values pulled from task_vars are passed through the templar for expansion.'''
    argument_spec = {'url': {'type': 'str'}}
    task_vars = {'url': 'https://{{ host }}/'}
    templar = MagicMock()
    templar.template.side_effect = lambda value: value.replace('{{ host }}', 'example.com')

    action = _make_action_module(templar=templar)
    result = action.get_args_from_task_vars(argument_spec, task_vars)

    assert result == {'url': 'https://example.com/'}


def test_ActionModule_get_args_from_task_vars_no_matching_vars():
    '''Arguments in the spec that are absent from task_vars are omitted from the result.'''
    argument_spec = {'missing': {'type': 'str'}}
    task_vars = {'other': 'value'}
    templar = MagicMock()
    templar.template.side_effect = lambda value: value

    action = _make_action_module(templar=templar)
    result = action.get_args_from_task_vars(argument_spec, task_vars)

    assert result == {}
    templar.template.assert_called_once_with({})


def test_ActionModule_get_args_from_task_vars_empty_spec():
    '''An empty argument spec yields an empty result even with task_vars present.'''
    templar = MagicMock()
    templar.template.side_effect = lambda value: value

    action = _make_action_module(templar=templar)
    assert action.get_args_from_task_vars({}, {'foo': 'bar'}) == {}


def test_ActionModule_get_args_from_task_vars_empty_task_vars():
    '''Empty task_vars yields an empty result even with a populated arg spec.'''
    argument_spec = {'foo': {'type': 'str'}}
    templar = MagicMock()
    templar.template.side_effect = lambda value: value

    action = _make_action_module(templar=templar)
    assert action.get_args_from_task_vars(argument_spec, {}) == {}

# Generated at 2026-11-01 22:16:58.453935
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''Test the constructor of ActionModule.'''
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
        shared_loader_obj=shared_loader_obj,
    )

    assert isinstance(action_module, ActionModule)
    assert action_module.TRANSFERS_FILES is False
    assert action_module._task is task
    assert action_module._connection is connection
    assert action_module._play_context is play_context
    assert action_module._loader is loader
    assert action_module._templar is templar
    assert action_module._shared_loader_obj is shared_loader_obj

# Generated at 2026-11-01 22:17:28.662157
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''
    Test that the ActionModule constructor properly initializes the object.
    '''
    mock_task = MagicMock()
    mock_task.action = 'validate_argument_spec'
    mock_task.async_val = 0
    mock_task.args = {'argument_spec': {}}

    action_module = ActionModule(
        task=mock_task,
        connection=MagicMock(),
        play_context=MagicMock(),
        loader=MagicMock(),
        templar=MagicMock(),
        shared_loader_obj=MagicMock()
    )

    assert isinstance(action_module, ActionModule)
    assert action_module.TRANSFERS_FILES is False
    assert action_module._task == mock_task

# Generated at 2026-11-01 22:18:53.243060
# Unit test for method get_args_from_task_vars of class ActionModule
def test_ActionModule_get_args_from_task_vars():
    '''
    Test that get_args_from_task_vars collects only arguments present in both
    the argument spec and task vars, and that the collected values are
    passed through the templar before being returned.
    '''
    from unittest.mock import Mock
    from ansible.plugins.action.validate_argument_spec import ActionModule

    argument_spec = {
        'name': {'type': 'str', 'required': True},
        'count': {'type': 'int'},
        'not_in_vars': {'type': 'str'},
    }

    task_vars = {
        'name': '{{ default_name }}',
        'count': 3,
        'extra_var': 'should not be included',
    }

    action = ActionModule.__new__(ActionModule)

    def fake_template(value):
        # Simulate templating: resolve templated string values recursively
        if isinstance(value, dict):
            return dict((k, fake_template(v)) for k, v in value.items())
        if isinstance(value, str) and '{{' in value:
            return value.replace('{{ default_name }}', 'resolved_name')
        return value

    action._templar = Mock()
    action._templar.template.side_effect = fake_template

    result = action.get_args_from_task_vars(argument_spec, task_vars)

    # Only keys present in the argument spec are picked up from task_vars
    assert 'name' in result
    assert 'count' in result
    assert 'extra_var' not in result
    assert 'not_in_vars' not in result

    # Values were passed through the templar
    assert result['name'] == 'resolved_name'
    assert result['count'] == 3

    # No matching task vars -> empty result
    action._templar.template.side_effect = lambda v: v
    assert action.get_args_from_task_vars(argument_spec, {}) == {}