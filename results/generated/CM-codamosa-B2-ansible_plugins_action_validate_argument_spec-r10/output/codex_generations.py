

# Generated at 2026-10-24 12:45:39.332757
# Unit test for constructor of class ActionModule
def test_ActionModule():
    task = MagicMock()
    connection = MagicMock()
    play_context = MagicMock()
    loader = MagicMock()
    templar = MagicMock()
    shared_loader_obj = MagicMock()

    action = ActionModule(
        task=task,
        connection=connection,
        play_context=play_context,
        loader=loader,
        templar=templar,
        shared_loader_obj=shared_loader_obj,
    )

    assert isinstance(action, ActionModule)
    assert action._task is task
    assert action._connection is connection
    assert action._play_context is play_context
    assert action._loader is loader
    assert action._templar is templar
    assert action._shared_loader_obj is shared_loader_obj
    assert action.TRANSFERS_FILES is False

# Generated at 2026-10-24 12:46:34.737306
# Unit test for constructor of class ActionModule
def test_ActionModule():from unittest.mock import MagicMock

# Generated at 2026-10-24 12:47:51.121824
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

# Generated at 2026-10-24 12:48:09.040451
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

# Generated at 2026-10-24 12:48:26.279366
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

# Generated at 2026-10-24 12:48:44.983586
# Unit test for constructor of class ActionModule
def test_ActionModule():from unittest.mock import MagicMock

# Generated at 2026-10-24 12:49:22.053129
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 12:49:58.610132
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 12:50:01.188233
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 12:50:03.608538
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-24 12:50:06.021962
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-24 12:50:08.439765
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-24 12:50:10.854640
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-24 12:50:13.271702
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-24 12:50:15.685504
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-24 12:50:18.099052
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-24 12:50:20.517119
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-24 12:50:22.926796
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-24 12:50:25.340844
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-24 12:50:27.754219
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-24 12:50:37.114696
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-24 12:50:39.978231
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

# Generated at 2026-10-24 12:50:42.948645
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 12:51:01.379290
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 12:51:04.440266
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 12:51:05.820754
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

# Generated at 2026-10-24 12:51:24.593663
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 12:51:27.010254
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 12:51:29.424685
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 12:51:31.982137
# Unit test for constructor of class ActionModule
def test_ActionModule():from unittest.mock import MagicMock

# Generated at 2026-10-24 12:51:33.431516
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

# Generated at 2026-10-24 12:51:36.235447
# Unit test for constructor of class ActionModule
def test_ActionModule():from unittest.mock import MagicMock

# Generated at 2026-10-24 12:51:38.965119
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 12:51:45.413366
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 12:52:09.284080
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 12:52:12.138113
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 12:52:15.006376
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 12:52:17.800521
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 12:52:20.506558
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 12:52:22.920609
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 12:52:25.334150
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 12:52:27.747339
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 12:52:30.160866
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 12:52:32.575975
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 12:52:35.392957
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 12:52:38.250848
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 12:52:41.116803
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 12:52:42.551037
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

# Generated at 2026-10-24 12:52:45.521040
# Unit test for constructor of class ActionModule
def test_ActionModule():from unittest.mock import MagicMock

# Generated at 2026-10-24 12:52:48.388644
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 12:53:06.308371
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 12:53:08.845110
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 12:53:11.264763
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 12:53:13.684460
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 12:53:16.103255
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 12:53:18.517019
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 12:53:21.024455
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 12:53:23.439022
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 12:53:25.851944
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 12:53:28.266732
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 12:53:30.684784
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 12:53:33.105298
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 12:53:35.525440
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 12:53:37.954028
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 12:53:40.364059
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 12:53:42.779641
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 12:53:45.755767
# Unit test for constructor of class ActionModule
def test_ActionModule():from unittest.mock import MagicMock

# Generated at 2026-10-24 12:53:47.162539
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

# Generated at 2026-10-24 12:53:50.009654
# Unit test for constructor of class ActionModule
def test_ActionModule():from unittest.mock import MagicMock

# Generated at 2026-10-24 12:53:51.370094
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

# Generated at 2026-10-24 12:53:54.204407
# Unit test for constructor of class ActionModule
def test_ActionModule():from unittest.mock import MagicMock

# Generated at 2026-10-24 12:53:55.618472
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

# Generated at 2026-10-24 12:54:20.958731
# Unit test for constructor of class ActionModule
def test_ActionModule():from unittest.mock import MagicMock

# Generated at 2026-10-24 12:54:26.081078
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 12:54:28.945157
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 12:54:31.817172
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 12:54:34.463863
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 12:54:36.882012
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 12:54:39.299066
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 12:54:41.716673
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 12:54:44.262147
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 12:54:46.679880
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 12:54:49.094273
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 12:54:51.512659
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 12:54:53.928615
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 12:54:56.575236
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 12:55:28.758361
# Unit test for method run of class ActionModule