

# Generated at 2026-10-24 15:13:50.352574
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 15:13:52.761307
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 15:13:55.174425
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 15:13:57.586694
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-24 15:13:59.999953
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-24 15:14:02.418726
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-24 15:14:04.837833
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 15:14:07.250972
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 15:14:09.666682
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 15:14:12.079773
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-24 15:14:14.493989
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-24 15:14:16.908931
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-24 15:14:19.321020
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 15:14:21.734826
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 15:14:24.147316
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 15:14:26.559257
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 15:14:28.971854
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 15:14:31.386013
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 15:14:32.862484
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

# Generated at 2026-10-24 15:14:50.857504
# Unit test for constructor of class ActionModule
def test_ActionModule():from unittest.mock import MagicMock

# Generated at 2026-10-24 15:14:53.582576
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

# Generated at 2026-10-24 15:14:54.940924
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

# Generated at 2026-10-24 15:14:57.356263
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 15:14:59.771881
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 15:15:02.183875
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-24 15:15:04.598387
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-24 15:15:07.196029
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-24 15:15:09.750840
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 15:15:12.165349
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 15:15:14.581071
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 15:15:17.006283
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-24 15:15:19.426083
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-24 15:15:21.840343
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-24 15:15:24.249230
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 15:15:26.665784
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 15:15:29.080392
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 15:15:31.492560
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 15:15:33.906085
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 15:15:36.321727
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 15:15:38.732755
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 15:15:41.146627
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 15:15:43.560877
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 15:15:45.978189
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-24 15:15:48.389811
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-24 15:15:50.802525
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-24 15:15:53.216361
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 15:15:55.626539
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 15:15:58.038673
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 15:16:16.175177
# Unit test for method get_args_from_task_vars of class ActionModule
def test_ActionModule_get_args_from_task_vars():
    from unittest.mock import MagicMock
    from ansible.plugins.action.validate_argument_spec import ActionModule

    am = ActionModule()
    mock_templar = MagicMock()
    mock_templar.template.side_effect = lambda value: value
    am._templar = mock_templar

    # Only keys present in both the argument spec and task vars are returned.
    argument_spec = {
        'name': {'type': 'str'},
        'count': {'type': 'int'},
        'missing': {'type': 'str'},
    }
    task_vars = {
        'name': 'example',
        'count': 2,
        'unrelated': 'ignored',
    }

    result = am.get_args_from_task_vars(argument_spec, task_vars)

    assert result == {'name': 'example', 'count': 2}
    assert 'unrelated' not in result
    assert 'missing' not in result
    mock_templar.template.assert_called_once_with({'name': 'example', 'count': 2})

    # The filtered args are passed through the templar, and templated values
    # are what get returned.
    mock_templar.reset_mock()
    mock_templar.template.side_effect = lambda value: {
        key: ('expanded' if item == '{{ source }}' else item)
        for key, item in value.items()
    }
    task_vars = {'name': '{{ source }}'}

    result = am.get_args_from_task_vars({'name': {'type': 'str'}}, task_vars)

    assert result == {'name': 'expanded'}
    mock_templar.template.assert_called_once_with({'name': '{{ source }}'})

    # When no argument names match, an empty dict is still templated and returned.
    mock_templar.reset_mock()
    mock_templar.template.side_effect = lambda value: value

    result = am.get_args_from_task_vars({'name': {'type': 'str'}}, {'other': 'value'})

    assert result == {}
    mock_templar.template.assert_called_once_with({})

# Generated at 2026-10-24 15:16:34.097696
# Unit test for method get_args_from_task_vars of class ActionModule
def test_ActionModule_get_args_from_task_vars():
    from unittest.mock import MagicMock
    from ansible.plugins.action.validate_argument_spec import ActionModule

    am = ActionModule()
    mock_templar = MagicMock()
    mock_templar.template.side_effect = lambda value: value
    am._templar = mock_templar

    # Only keys present in both the argument spec and task vars are returned.
    argument_spec = {
        'name': {'type': 'str'},
        'count': {'type': 'int'},
        'missing': {'type': 'str'},
    }
    task_vars = {
        'name': 'example',
        'count': 2,
        'unrelated': 'ignored',
    }

    result = am.get_args_from_task_vars(argument_spec, task_vars)

    assert result == {'name': 'example', 'count': 2}
    assert 'unrelated' not in result
    assert 'missing' not in result
    mock_templar.template.assert_called_once_with({'name': 'example', 'count': 2})

    # The filtered args are passed through the templar, and templated values
    # are what get returned.
    mock_templar.reset_mock()
    mock_templar.template.side_effect = lambda value: {
        key: ('expanded' if item == '{{ source }}' else item)
        for key, item in value.items()
    }
    task_vars = {'name': '{{ source }}'}

    result = am.get_args_from_task_vars({'name': {'type': 'str'}}, task_vars)

    assert result == {'name': 'expanded'}
    mock_templar.template.assert_called_once_with({'name': '{{ source }}'})

    # When no argument names match, an empty dict is still templated and returned.
    mock_templar.reset_mock()
    mock_templar.template.side_effect = lambda value: value

    result = am.get_args_from_task_vars({'name': {'type': 'str'}}, {'other': 'value'})

    assert result == {}
    mock_templar.template.assert_called_once_with({})

# Generated at 2026-10-24 15:16:36.617205
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 15:16:39.029604
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 15:16:41.441934
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 15:16:43.981465
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-24 15:16:46.393900
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-24 15:16:48.806704
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-24 15:16:51.220648
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 15:16:53.635919
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 15:16:56.051370
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 15:16:58.674575
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 15:17:01.087813
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 15:17:03.500919
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 15:17:05.914064
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 15:17:08.326896
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 15:17:10.740160
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 15:17:13.155826
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 15:17:15.569201
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 15:17:17.982241
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 15:17:20.394724
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 15:17:22.811091
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 15:17:25.225007
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 15:17:27.637973
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-24 15:18:03.695354
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-24 15:18:06.114288
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-24 15:18:08.527326
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 15:18:10.939772
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 15:18:13.352705
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 15:18:15.770261
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 15:18:18.177778
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 15:18:20.595316
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 15:18:23.002870
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 15:18:25.415404
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 15:18:27.828118
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 15:18:30.241915
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 15:18:32.654875
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 15:18:35.068416
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 15:18:37.481196
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-24 15:18:39.894957
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-24 15:18:42.307070
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-24 15:18:44.721894
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 15:18:47.134048
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 15:18:49.548625
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 15:18:51.960867
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 15:18:54.372505
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 15:19:12.078331
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 15:19:14.583216
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 15:19:16.996269
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 15:19:19.409929
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 15:19:21.821852
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 15:19:24.377609
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 15:19:26.792616
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 15:19:29.205796
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 15:19:31.618339
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 15:19:34.032093
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 15:19:36.446291
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 15:19:38.859486
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 15:19:41.272458
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 15:19:43.686025
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 15:19:46.099589
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 15:19:48.511810
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 15:19:50.924154
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-24 15:19:53.337291
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-24 15:19:55.750143
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-24 15:19:58.163227
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 15:20:00.576283
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 15:20:02.988762
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 15:20:05.400792
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 15:20:07.813327
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 15:20:10.228886
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 15:20:12.641512
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 15:20:15.055598
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 15:20:17.468745
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 15:20:19.882143
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 15:20:22.297250
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 15:20:24.713583
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 15:20:27.126695
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 15:20:29.538660
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 15:20:31.951511
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 15:20:34.364923
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-24 15:20:36.777313
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-24 15:20:39.190711
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-24 15:20:41.603278
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 15:20:44.015441
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 15:20:46.428992
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 15:20:48.841652
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-24 15:20:51.259202
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-24 15:21:03.311983
# Unit test for method get_args_from_task_vars of class ActionModule
def test_ActionModule_get_args_from_task_vars():import ansible.plugins.action.validate_argument_spec as mod


# Generated at 2026-10-24 15:21:21.164453
# Unit test for method get_args_from_task_vars of class ActionModule
def test_ActionModule_get_args_from_task_vars():
    from unittest.mock import MagicMock
    from ansible.plugins.action.validate_argument_spec import ActionModule

    am = ActionModule()
    mock_templar = MagicMock()
    mock_templar.template.side_effect = lambda value: value
    am._templar = mock_templar

    # Only keys present in both the argument spec and task vars are returned.
    argument_spec = {
        'name': {'type': 'str'},
        'count': {'type': 'int'},
        'missing': {'type': 'str'},
    }
    task_vars = {
        'name': 'example',
        'count': 2,
        'unrelated': 'ignored',
    }

    result = am.get_args_from_task_vars(argument_spec, task_vars)

    assert result == {'name': 'example', 'count': 2}
    assert 'unrelated' not in result
    assert 'missing' not in result
    mock_templar.template.assert_called_once_with({'name': 'example', 'count': 2})

    # The filtered args are passed through the templar, and templated values
    # are what get returned.
    mock_templar.reset_mock()
    mock_templar.template.side_effect = lambda value: {
        key: ('expanded' if item == '{{ source }}' else item)
        for key, item in value.items()
    }
    task_vars = {'name': '{{ source }}'}

    result = am.get_args_from_task_vars({'name': {'type': 'str'}}, task_vars)

    assert result == {'name': 'expanded'}
    mock_templar.template.assert_called_once_with({'name': '{{ source }}'})

    # When no argument names match, an empty dict is still templated and returned.
    mock_templar.reset_mock()
    mock_templar.template.side_effect = lambda value: value

    result = am.get_args_from_task_vars({'name': {'type': 'str'}}, {'other': 'value'})

    assert result == {}
    mock_templar.template.assert_called_once_with({})

# Generated at 2026-10-24 15:21:23.761148
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 15:21:26.399112
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 15:21:28.812313
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 15:21:31.225428
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 15:21:33.639156
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 15:21:36.051623
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 15:21:38.465825
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-24 15:21:40.879262
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-24 15:21:43.292143
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-24 15:21:45.705231
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-24 15:21:48.118491
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-24 15:21:50.532230
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-24 15:21:52.947723
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-24 15:21:55.360901
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-24 15:21:57.776669
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-24 15:22:00.189004
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 15:22:02.600024
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 15:22:05.017988
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 15:22:08.866727
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 15:22:11.278886
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 15:22:29.066119
# Unit test for constructor of class ActionModule
def test_ActionModule():from unittest.mock import MagicMock

# Generated at 2026-10-24 15:22:30.417330
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

# Generated at 2026-10-24 15:22:33.084539
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 15:22:35.499607
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 15:22:37.913533
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 15:22:40.327152
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 15:22:42.740993
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 15:22:45.341091
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 15:22:47.756974
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 15:22:50.169166
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 15:22:52.580387
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 15:22:54.996817
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 15:22:57.415243
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 15:22:59.826384
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 15:23:02.241367
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 15:23:04.654571
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 15:23:07.067504
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 15:23:09.478175
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 15:23:11.890819
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 15:23:14.307792
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 15:23:31.992631
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 15:23:50.014660
# Unit test for method run of class ActionModule