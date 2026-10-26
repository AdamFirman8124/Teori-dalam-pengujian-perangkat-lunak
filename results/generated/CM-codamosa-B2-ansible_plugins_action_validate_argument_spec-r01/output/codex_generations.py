

# Generated at 2026-10-25 12:37:58.230976
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-25 12:38:00.645442
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-25 12:38:03.059960
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-25 12:38:29.371348
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 12:38:55.873539
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 12:38:58.509134
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 12:39:00.925944
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-25 12:39:03.336647
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-25 12:39:05.751075
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-25 12:39:08.165145
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 12:39:10.599765
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 12:39:13.014917
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 12:39:41.256001
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = _make_action_module()
    assert isinstance(am, ActionBase)
    assert isinstance(am, ActionModule)
    assert am.TRANSFERS_FILES is False

# Generated at 2026-10-25 12:39:43.672281
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 12:39:46.086050
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 12:39:48.500350
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-25 12:39:50.915144
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-25 12:39:53.330364
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-25 12:39:55.744602
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-25 12:39:58.161110
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-25 12:40:00.572242
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-25 12:40:02.989316
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 12:40:05.403625
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 12:40:07.816266
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 12:40:10.231753
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-25 12:40:12.645759
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-25 12:40:15.059044
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-25 12:40:17.473945
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-25 12:40:37.371261
# Unit test for method get_args_from_task_vars of class ActionModule
def test_ActionModule_get_args_from_task_vars():from unittest.mock import MagicMock

# Generated at 2026-10-25 12:40:38.889700
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 12:41:06.966589
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 12:41:09.383628
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 12:41:11.819159
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 12:41:14.233588
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 12:41:16.648600
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 12:41:19.063949
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-25 12:41:21.476009
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-25 12:41:23.889878
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-25 12:41:26.303983
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 12:41:28.716757
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 12:41:31.132826
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 12:41:33.547641
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 12:41:35.962146
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 12:41:38.375262
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 12:41:52.125729
# Unit test for method get_args_from_task_vars of class ActionModule
def test_ActionModule_get_args_from_task_vars():
    from unittest.mock import MagicMock
    from ansible.plugins.action.validate_argument_spec import ActionModule

    action = object.__new__(ActionModule)
    action._templar = MagicMock()
    action._templar.template.side_effect = lambda value: value

    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
    }
    task_vars = {
        'name': 'alice',
        'age': 30,
        'not_in_spec': 'ignored',
    }

    result = action.get_args_from_task_vars(argument_spec, task_vars)

    assert result == {'name': 'alice', 'age': 30}
    action._templar.template.assert_called_once_with({'name': 'alice', 'age': 30})

    action._templar.reset_mock()
    action._templar.template.side_effect = lambda value: {
        key: ('expanded' if key == 'name' else val) for key, val in value.items()
    }

    result = action.get_args_from_task_vars(argument_spec, {'name': '{{ first_name }}', 'age': 30})

    assert result == {'name': 'expanded', 'age': 30}
    action._templar.template.assert_called_once_with({'name': '{{ first_name }}', 'age': 30})

# Generated at 2026-10-25 12:41:53.667294
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 12:41:58.912582
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 12:42:01.650249
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 12:42:04.066958
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-25 12:42:06.820439
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-25 12:42:09.469197
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-25 12:42:11.884295
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-25 12:42:14.657341
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-25 12:42:17.075034
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-25 12:42:19.492174
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 12:42:21.906187
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 12:42:24.321824
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 12:42:26.764399
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 12:42:29.156944
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 12:42:31.570590
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 12:42:33.989423
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 12:42:36.402262
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 12:42:38.817287
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 12:42:41.231508
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 12:43:07.901219
# Unit test for constructor of class ActionModule
def test_ActionModule():from unittest.mock import MagicMock

# Generated at 2026-10-25 12:43:37.578399
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-25 12:43:39.991812
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-25 12:43:42.405535
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-25 12:43:44.823882
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 12:44:03.219230
# Unit test for constructor of class ActionModule
def test_ActionModule():from unittest.mock import MagicMock

# Generated at 2026-10-25 12:44:04.835822
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 12:44:07.827384
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 12:44:10.739379
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 12:44:13.153431
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 12:44:15.743773
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 12:44:18.163011
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 12:44:20.796578
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 12:44:23.212148
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 12:44:25.629787
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 12:44:28.044720
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 12:44:30.462356
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 12:44:32.990389
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 12:44:35.403115
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 12:44:37.818355
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 12:44:40.232945
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 12:44:42.647545
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 12:44:45.060787
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 12:44:47.475291
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 12:44:49.891844
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 12:44:52.306052
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 12:44:54.720649
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 12:44:57.134670
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 12:44:59.549002
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 12:45:01.963926
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 12:45:16.821512
# Unit test for constructor of class ActionModule
def test_ActionModule():from unittest.mock import MagicMock

# Generated at 2026-10-25 12:45:33.308953
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = _make_action_module()
    assert isinstance(am, ActionBase)
    assert isinstance(am, ActionModule)
    assert am.TRANSFERS_FILES is False

# Generated at 2026-10-25 12:45:38.736947
# Unit test for constructor of class ActionModule
def test_ActionModule():from unittest.mock import MagicMock

# Generated at 2026-10-25 12:45:40.171933
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 12:45:43.139457
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 12:45:46.212007
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 12:45:47.665276
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 12:45:50.516855
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 12:45:52.933896
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 12:45:55.350547
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 12:45:57.764519
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 12:46:00.177620
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 12:46:02.614454
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 12:46:05.028498
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 12:46:07.767099
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 12:46:09.273100
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 12:46:16.231073
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 12:46:35.858736
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 12:46:38.273075
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 12:46:40.686790
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 12:46:43.101046
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 12:46:45.518921
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 12:46:47.934924
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 12:46:50.438924
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 12:46:52.851199
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 12:46:55.265906
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 12:46:57.679534
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 12:47:00.094163
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 12:47:02.812274
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 12:47:05.227815
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 12:47:07.642157
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 12:47:10.055669
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 12:47:26.872106
# Unit test for constructor of class ActionModule
def test_ActionModule():from unittest.mock import MagicMock

# Generated at 2026-10-25 12:47:28.325413
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 12:47:31.376743
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 12:47:49.174175
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 12:47:51.941499
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 12:47:54.354759
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 12:47:56.769418
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 12:47:59.184126
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 12:48:01.597969
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 12:48:04.012531
# Unit test for constructor of class ActionModule