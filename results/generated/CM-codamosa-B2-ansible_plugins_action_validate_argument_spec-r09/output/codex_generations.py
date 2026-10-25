

# Generated at 2026-10-24 13:00:44.929865
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 13:00:47.348504
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 13:00:49.766158
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 13:00:52.184815
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 13:00:54.595922
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 13:00:57.008110
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 13:00:59.421748
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 13:01:01.835247
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 13:01:04.248305
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 13:01:06.662600
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 13:01:09.330298
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 13:02:00.126200
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 13:02:02.789664
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 13:02:05.313675
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 13:02:07.736724
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 13:02:10.573979
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 13:02:13.362029
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 13:02:35.449446
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 13:03:09.346857
# Unit test for method get_args_from_task_vars of class ActionModule
def test_ActionModule_get_args_from_task_vars():
    from unittest.mock import MagicMock
    action = ActionModule.__new__(ActionModule)
    mock_templar = MagicMock()
    action._templar = mock_templar
    mock_templar.template.side_effect = lambda v: v
    argument_spec = {'foo': {'type': 'str'}, 'bar': {'type': 'int'}}
    task_vars = {'foo': 'hello', 'bar': 42, 'extra': 'ignored'}
    result = action.get_args_from_task_vars(argument_spec, task_vars)
    assert result == {'foo': 'hello', 'bar': 42}
    mock_templar.template.assert_called_once_with({'foo': 'hello', 'bar': 42})
    mock_templar.reset_mock()
    result = action.get_args_from_task_vars(argument_spec, {'other': 1, 'extra': 2})
    assert result == {}
    mock_templar.template.assert_called_once_with({})
    mock_templar.reset_mock()
    result = action.get_args_from_task_vars({}, task_vars)
    assert result == {}
    mock_templar.template.assert_called_once_with({})
    mock_templar.reset_mock()
    mock_templar.template.side_effect = None
    mock_templar.template.return_value = {'foo': 'expanded'}
    result = action.get_args_from_task_vars(argument_spec, {'foo': '{{ var }}', 'unrelated': 'x'})
    assert result == {'foo': 'expanded'}
    mock_templar.template.assert_called_once_with({'foo': '{{ var }}'})

# Generated at 2026-10-24 13:03:11.766869
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-24 13:03:14.184124
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-24 13:03:16.601318
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-24 13:03:19.283978
# Unit test for method get_args_from_task_vars of class ActionModule
def test_ActionModule_get_args_from_task_vars():
    from unittest.mock import MagicMock
    action = ActionModule.__new__(ActionModule)
    mock_templar = MagicMock()
    action._templar = mock_templar
    mock_templar.template.side_effect = lambda v: v
    argument_spec = {'foo': {'type': 'str'}, 'bar': {'type': 'int'}}
    task_vars = {'foo': 'hello', 'bar': 42, 'extra': 'ignored'}
    result = action.get_args_from_task_vars(argument_spec, task_vars)
    assert result == {'foo': 'hello', 'bar': 42}
    mock_templar.template.assert_called_once_with({'foo': 'hello', 'bar': 42})
    mock_templar.reset_mock()
    result = action.get_args_from_task_vars(argument_spec, {'other': 1, 'extra': 2})
    assert result == {}
    mock_templar.template.assert_called_once_with({})
    mock_templar.reset_mock()
    result = action.get_args_from_task_vars({}, task_vars)
    assert result == {}
    mock_templar.template.assert_called_once_with({})
    mock_templar.reset_mock()
    mock_templar.template.side_effect = None
    mock_templar.template.return_value = {'foo': 'expanded'}
    result = action.get_args_from_task_vars(argument_spec, {'foo': '{{ var }}', 'unrelated': 'x'})
    assert result == {'foo': 'expanded'}
    mock_templar.template.assert_called_once_with({'foo': '{{ var }}'})

# Generated at 2026-10-24 13:03:20.752356
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from unittest.mock import MagicMock

    mock_task = MagicMock()
    mock_connection = MagicMock()
    mock_play_context = MagicMock()
    mock_loader = MagicMock()
    mock_templar = MagicMock()
    mock_shared_loader = MagicMock()

    instance = ActionModule(
        mock_task,
        mock_connection,
        mock_play_context,
        mock_loader,
        mock_templar,
        mock_shared_loader,
    )

    assert isinstance(instance, ActionBase)
    assert isinstance(instance, ActionModule)
    assert ActionModule.TRANSFERS_FILES is False
    assert instance._task is mock_task
    assert instance._connection is mock_connection
    assert instance._play_context is mock_play_context
    assert instance._loader is mock_loader

# Generated at 2026-10-24 13:03:40.068381
# Unit test for constructor of class ActionModule
def test_ActionModule():from unittest.mock import MagicMock

# Generated at 2026-10-24 13:03:45.906884
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 13:04:17.952580
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 13:04:20.368893
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 13:04:22.782165
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-24 13:04:25.229633
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-24 13:04:41.831386
# Unit test for method get_args_from_task_vars of class ActionModule
def test_ActionModule_get_args_from_task_vars():from unittest.mock import MagicMock

# Generated at 2026-10-24 13:04:44.601494
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 13:04:47.444048
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 13:05:10.401200
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 13:05:13.122747
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-24 13:05:15.631348
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-24 13:05:18.043828
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-24 13:05:20.597803
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 13:05:23.006741
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 13:05:25.504711
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 13:05:27.917766
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 13:05:30.737266
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 13:06:04.232636
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 13:06:07.018120
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 13:06:24.930252
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 13:06:27.356745
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 13:06:45.511927
# Unit test for method get_args_from_task_vars of class ActionModule
def test_ActionModule_get_args_from_task_vars():
    from unittest.mock import MagicMock
    action = ActionModule.__new__(ActionModule)
    mock_templar = MagicMock()
    action._templar = mock_templar
    mock_templar.template.side_effect = lambda v: v
    argument_spec = {'foo': {'type': 'str'}, 'bar': {'type': 'int'}}
    task_vars = {'foo': 'hello', 'bar': 42, 'extra': 'ignored'}
    result = action.get_args_from_task_vars(argument_spec, task_vars)
    assert result == {'foo': 'hello', 'bar': 42}
    mock_templar.template.assert_called_once_with({'foo': 'hello', 'bar': 42})
    mock_templar.reset_mock()
    result = action.get_args_from_task_vars(argument_spec, {'other': 1, 'extra': 2})
    assert result == {}
    mock_templar.template.assert_called_once_with({})
    mock_templar.reset_mock()
    result = action.get_args_from_task_vars({}, task_vars)
    assert result == {}
    mock_templar.template.assert_called_once_with({})
    mock_templar.reset_mock()
    mock_templar.template.side_effect = None
    mock_templar.template.return_value = {'foo': 'expanded'}
    result = action.get_args_from_task_vars(argument_spec, {'foo': '{{ var }}', 'unrelated': 'x'})
    assert result == {'foo': 'expanded'}
    mock_templar.template.assert_called_once_with({'foo': '{{ var }}'})

# Generated at 2026-10-24 13:06:50.417955
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 13:06:54.215528
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 13:06:57.083047
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 13:07:00.360185
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 13:08:06.513504
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 13:08:28.628769
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 13:08:32.699656
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 13:09:20.692417
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 13:10:10.622315
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 13:10:13.590062
# Unit test for method get_args_from_task_vars of class ActionModule
def test_ActionModule_get_args_from_task_vars():
    from unittest.mock import MagicMock
    action = ActionModule.__new__(ActionModule)
    mock_templar = MagicMock()
    action._templar = mock_templar
    mock_templar.template.side_effect = lambda v: v
    argument_spec = {'foo': {'type': 'str'}, 'bar': {'type': 'int'}}
    task_vars = {'foo': 'hello', 'bar': 42, 'extra': 'ignored'}
    result = action.get_args_from_task_vars(argument_spec, task_vars)
    assert result == {'foo': 'hello', 'bar': 42}
    mock_templar.template.assert_called_once_with({'foo': 'hello', 'bar': 42})
    mock_templar.reset_mock()
    result = action.get_args_from_task_vars(argument_spec, {'other': 1, 'extra': 2})
    assert result == {}
    mock_templar.template.assert_called_once_with({})
    mock_templar.reset_mock()
    result = action.get_args_from_task_vars({}, task_vars)
    assert result == {}
    mock_templar.template.assert_called_once_with({})
    mock_templar.reset_mock()
    mock_templar.template.side_effect = None
    mock_templar.template.return_value = {'foo': 'expanded'}
    result = action.get_args_from_task_vars(argument_spec, {'foo': '{{ var }}', 'unrelated': 'x'})
    assert result == {'foo': 'expanded'}
    mock_templar.template.assert_called_once_with({'foo': '{{ var }}'})

# Generated at 2026-10-24 13:10:16.646621
# Unit test for method get_args_from_task_vars of class ActionModule
def test_ActionModule_get_args_from_task_vars():
    from unittest.mock import MagicMock
    action = ActionModule.__new__(ActionModule)
    mock_templar = MagicMock()
    action._templar = mock_templar
    mock_templar.template.side_effect = lambda v: v
    argument_spec = {'foo': {'type': 'str'}, 'bar': {'type': 'int'}}
    task_vars = {'foo': 'hello', 'bar': 42, 'extra': 'ignored'}
    result = action.get_args_from_task_vars(argument_spec, task_vars)
    assert result == {'foo': 'hello', 'bar': 42}
    mock_templar.template.assert_called_once_with({'foo': 'hello', 'bar': 42})
    mock_templar.reset_mock()
    result = action.get_args_from_task_vars(argument_spec, {'other': 1, 'extra': 2})
    assert result == {}
    mock_templar.template.assert_called_once_with({})
    mock_templar.reset_mock()
    result = action.get_args_from_task_vars({}, task_vars)
    assert result == {}
    mock_templar.template.assert_called_once_with({})
    mock_templar.reset_mock()
    mock_templar.template.side_effect = None
    mock_templar.template.return_value = {'foo': 'expanded'}
    result = action.get_args_from_task_vars(argument_spec, {'foo': '{{ var }}', 'unrelated': 'x'})
    assert result == {'foo': 'expanded'}
    mock_templar.template.assert_called_once_with({'foo': '{{ var }}'})

# Generated at 2026-10-24 13:10:18.014293
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from unittest.mock import MagicMock

    mock_task = MagicMock()
    mock_connection = MagicMock()
    mock_play_context = MagicMock()
    mock_loader = MagicMock()
    mock_templar = MagicMock()
    mock_shared_loader = MagicMock()

    instance = ActionModule(
        mock_task,
        mock_connection,
        mock_play_context,
        mock_loader,
        mock_templar,
        mock_shared_loader,
    )

    assert isinstance(instance, ActionBase)
    assert isinstance(instance, ActionModule)
    assert ActionModule.TRANSFERS_FILES is False
    assert instance._task is mock_task
    assert instance._connection is mock_connection
    assert instance._play_context is mock_play_context
    assert instance._loader is mock_loader

# Generated at 2026-10-24 13:10:20.962622
# Unit test for constructor of class ActionModule
def test_ActionModule():from unittest.mock import MagicMock

# Generated at 2026-10-24 13:10:53.150545
# Unit test for method get_args_from_task_vars of class ActionModule
def test_ActionModule_get_args_from_task_vars():
    from unittest.mock import MagicMock
    action = ActionModule.__new__(ActionModule)
    mock_templar = MagicMock()
    action._templar = mock_templar
    mock_templar.template.side_effect = lambda v: v
    argument_spec = {'foo': {'type': 'str'}, 'bar': {'type': 'int'}}
    task_vars = {'foo': 'hello', 'bar': 42, 'extra': 'ignored'}
    result = action.get_args_from_task_vars(argument_spec, task_vars)
    assert result == {'foo': 'hello', 'bar': 42}
    mock_templar.template.assert_called_once_with({'foo': 'hello', 'bar': 42})
    mock_templar.reset_mock()
    result = action.get_args_from_task_vars(argument_spec, {'other': 1, 'extra': 2})
    assert result == {}
    mock_templar.template.assert_called_once_with({})
    mock_templar.reset_mock()
    result = action.get_args_from_task_vars({}, task_vars)
    assert result == {}
    mock_templar.template.assert_called_once_with({})
    mock_templar.reset_mock()
    mock_templar.template.side_effect = None
    mock_templar.template.return_value = {'foo': 'expanded'}
    result = action.get_args_from_task_vars(argument_spec, {'foo': '{{ var }}', 'unrelated': 'x'})
    assert result == {'foo': 'expanded'}
    mock_templar.template.assert_called_once_with({'foo': '{{ var }}'})