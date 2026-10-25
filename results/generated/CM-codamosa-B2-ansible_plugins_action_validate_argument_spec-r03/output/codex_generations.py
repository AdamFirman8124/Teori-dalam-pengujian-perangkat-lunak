

# Generated at 2026-10-24 06:42:36.745544
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 06:42:39.163717
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 06:43:02.399827
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 06:43:35.136477
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 06:43:37.556626
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 06:43:39.972638
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 06:44:05.808271
# Unit test for method get_args_from_task_vars of class ActionModule
def test_ActionModule_get_args_from_task_vars():
    from unittest.mock import MagicMock

    task = MagicMock()
    connection = MagicMock()
    play_context = MagicMock()
    loader = MagicMock()
    templar = MagicMock()
    shared_loader_obj = MagicMock()

    action = ActionModule(task, connection, play_context, loader, templar, shared_loader_obj)

    argument_spec = {
        'name': {'type': 'str'},
        'age': {'type': 'int'},
        'missing': {'type': 'str'},
    }
    task_vars = {
        'name': 'Alice',
        'age': 30,
        'unrelated': 'ignored',
    }

    templated_result = {'name': 'Alice', 'age': 30}
    templar.template.return_value = templated_result

    result = action.get_args_from_task_vars(argument_spec, task_vars)

    assert result is templated_result
    templar.template.assert_called_once_with({'name': 'Alice', 'age': 30})

# Generated at 2026-10-24 06:44:22.352485
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert issubclass(ActionModule, ActionBase)

# Generated at 2026-10-24 06:44:24.771428
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 06:44:27.187971
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 06:44:29.608540
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 06:44:32.022788
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 06:44:34.439305
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 06:44:36.855154
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 06:44:39.271468
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 06:44:41.687117
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 06:44:44.100560
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 06:44:46.513164
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 06:44:48.931434
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 06:44:51.346845
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-24 06:44:53.758884
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-24 06:44:56.174268
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-24 06:44:58.592999
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-24 06:45:07.989552
# Unit test for method get_args_from_task_vars of class ActionModule
def test_ActionModule_get_args_from_task_vars():instance = ActionModule.__new__(ActionModule)

# Generated at 2026-10-24 06:45:29.837309
# Unit test for method get_args_from_task_vars of class ActionModule
def test_ActionModule_get_args_from_task_vars():from ansible.plugins.action.validate_argument_spec import ActionModule


# Generated at 2026-10-24 06:45:32.342980
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 06:45:34.762502
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 06:45:37.177542
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 06:45:39.592617
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 06:45:42.008742
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 06:45:44.424678
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 06:45:46.842656
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 06:45:49.256342
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 06:45:51.670876
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 06:45:54.085708
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-24 06:45:56.502578
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-24 06:45:58.913824
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-24 06:46:01.326572
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 06:46:03.739961
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 06:46:06.153312
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 06:46:08.566086
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 06:46:10.980233
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 06:46:13.397839
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 06:46:15.813137
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-24 06:46:18.226996
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-24 06:46:20.642719
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-24 06:46:23.054485
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 06:46:25.466156
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 06:46:27.878773
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 06:46:30.291045
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 06:46:32.703914
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 06:46:35.128494
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 06:46:37.530202
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-24 06:46:39.943616
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-24 06:46:42.356516
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-24 06:46:44.769611
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-24 06:46:47.185815
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-24 06:46:49.610073
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-24 06:46:52.026317
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-24 06:46:54.441297
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-24 06:46:56.856069
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-24 06:47:13.363531
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert issubclass(ActionModule, ActionBase)

# Generated at 2026-10-24 06:47:16.121723
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 06:47:18.885901
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 06:47:38.228067
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-24 06:47:40.726750
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-24 06:47:43.247311
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-24 06:47:45.669954
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 06:47:48.090490
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 06:47:50.512508
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 06:47:52.930720
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 06:47:55.362521
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 06:47:57.765524
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 06:48:00.177482
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 06:48:02.591764
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 06:48:36.471234
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 06:48:53.047870
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 06:48:55.469197
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 06:48:57.884902
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 06:49:00.299236
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 06:49:02.918337
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 06:49:05.334725
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 06:49:07.750122
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 06:49:10.167678
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 06:49:12.587141
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 06:49:15.000193
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 06:49:17.417803
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 06:49:19.834953
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 06:49:22.251611
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 06:49:24.654670
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 06:49:27.070262
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 06:49:29.485523
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 06:49:31.901201
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 06:49:49.720249
# Unit test for method run of class ActionModule
def test_ActionModule_run():from types import SimpleNamespace

# Generated at 2026-10-24 06:49:52.583632
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 06:50:26.522515
# Unit test for method run of class ActionModule
def test_ActionModule_run():from types import SimpleNamespace

# Generated at 2026-10-24 06:50:29.156383
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 06:50:31.575121
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 06:50:33.992088
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 06:50:36.405237
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 06:50:38.998706
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 06:50:41.746367
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 06:50:58.236760
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert issubclass(ActionModule, ActionBase)

# Generated at 2026-10-24 06:51:00.962668
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 06:51:03.817357
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 06:51:06.633774
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 06:51:24.536005
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 06:51:42.578758
# Unit test for method run of class ActionModule
def test_ActionModule_run():from types import SimpleNamespace

# Generated at 2026-10-24 06:51:59.166478
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert issubclass(ActionModule, ActionBase)

# Generated at 2026-10-24 06:52:02.027219
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 06:52:04.847005
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 06:52:21.488072
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert issubclass(ActionModule, ActionBase)

# Generated at 2026-10-24 06:52:24.138470
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 06:52:26.553473
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 06:52:28.970074
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 06:52:31.387967
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 06:52:33.803490
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 06:52:36.219556
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 06:52:38.633089
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 06:52:41.047894
# Unit test for method run of class ActionModule