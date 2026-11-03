

# Generated at 2026-11-03 01:03:49.405157
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''Test the ActionModule constructor.'''
    from unittest.mock import MagicMock

    task = MagicMock()
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

# Generated at 2026-11-03 01:05:47.206052
# Unit test for method get_args_from_task_vars of class ActionModule
def test_ActionModule_get_args_from_task_vars():
    action_module = _make_action_module()

    argument_spec = {
        'name': {'type': 'str', 'required': True},
        'port': {'type': 'int'},
        'state': {'type': 'str', 'choices': ['present', 'absent']},
    }
    task_vars = {
        'name': 'web01',
        'port': 8080,
        'not_in_spec': 'should be ignored',
    }

    result = action_module.get_args_from_task_vars(argument_spec, task_vars)

    # Only argument names declared in the spec and present in task_vars
    # should be returned; unrelated task vars must be excluded.
    assert result == {'name': 'web01', 'port': 8080}
    action_module._templar.template.assert_called_once_with({'name': 'web01', 'port': 8080})


def test_ActionModule_get_args_from_task_vars_empty_task_vars():
    action_module = _make_action_module()

    argument_spec = {'name': {'type': 'str'}}

    assert action_module.get_args_from_task_vars(argument_spec, {}) == {}


def test_ActionModule_get_args_from_task_vars_empty_argument_spec():
    action_module = _make_action_module()

    assert action_module.get_args_from_task_vars({}, {'name': 'web01'}) == {}


def test_ActionModule_get_args_from_task_vars_templated_values():
    # Simulate a templar that expands the values it is given
    templar = MagicMock()

    def fake_template(data):
        return dict((k, 'expanded:%s' % v) for k, v in data.items())

    templar.template.side_effect = fake_template
    action_module = _make_action_module(templar=templar)

    argument_spec = {'name': {'type': 'str'}}
    task_vars = {'name': '{{ hostvars["host1"].name }}'}

    result = action_module.get_args_from_task_vars(argument_spec, task_vars)

    assert result == {'name': 'expanded:{{ hostvars["host1"].name }}'}
    templar.template.assert_called_once_with({'name': '{{ hostvars["host1"].name }}'})

# Generated at 2026-11-03 01:11:11.777469
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''
    Unit test for the run method of ActionModule covering the success path,
    the validation-failure path, and the AnsibleError paths.
    '''
    from unittest.mock import MagicMock

    def _build_action(task_args):
        mock_task = MagicMock()
        mock_task.args = task_args
        action = ActionModule(
            mock_task,
            MagicMock(),  # connection
            MagicMock(),  # play_context
            MagicMock(),  # loader
            MagicMock(),  # templar
            MagicMock(),  # shared_loader_obj
        )
        action._templar = MagicMock()
        action._templar.template.side_effect = lambda x: x
        return action

    argument_spec = {
        'name': {'type': 'str', 'required': True},
        'count': {'type': 'int', 'default': 1},
    }

    # 1. Successful validation using provided_arguments
    action = _build_action({
        'argument_spec': argument_spec,
        'provided_arguments': {'name': 'foo', 'count': 5},
key: ae76b65d    })
    result = action.run(task_vars={})
    assert result.get('failed', False) is False
    assert result['changed'] is False
    assert result['msg'] == 'The arg spec validation passed'
    assert result['validate_args_context'] == {}

    # 2. Successful validation with args pulled from task_vars (templated)
    action = _build_action({'argument_spec': argument_spec, 'provided_arguments': {}})
    result = action.run(task_vars={'name': 'from_vars', 'count': 2, 'unrelated': 'x'})
    assert result.get('failed', False) is False
    assert result['changed'] is False
    assert result['msg'] == 'The arg spec validation passed'

    # 3. Failed validation returns failure details
    action = _build_action({
        'argument_spec': argument_spec,
        'provided_arguments': {'name': 'foo', 'count': 'not-an-int'},
    })
    result = action.run(task_vars={})
    assert result['failed'] is True
    assert result['msg'].startswith('Validation of arguments failed:')
    assert result['argument_errors']
    assert result['argument_spec_data'] == argument_spec

    # 4. Missing argument_spec raises AnsibleError
    action = _build_action({})
    try:
        action.run(task_vars={})
    except AnsibleError as e:
        assert '"argument_spec" arg is required' in str(e)
    else:
        raise AssertionError('AnsibleError not raised for missing argument_spec')

    # 5. Non-dict argument_spec raises AnsibleError
    action = _build_action({'argument_spec': ['not', 'a', 'dict']})
    try:
        action.run(task_vars={})
    except AnsibleError as e:
        assert 'Incorrect type for argument_spec' in str(e)
    else:
        raise AssertionError('AnsibleError not raised for invalid argument_spec type')

    # 6. Non-dict provided_arguments raises AnsibleError
    action = _build_action({'argument_spec': argument_spec, 'provided_arguments': 'nope'})
    try:
        action.run(task_vars={})
    except AnsibleError as e:
        assert 'Incorrect type for provided_arguments' in str(e)