

# Generated at 2026-10-24 20:28:05.138470
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 20:28:07.552761
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 20:28:09.970227
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 20:28:12.386540
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-24 20:28:14.802087
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-24 20:28:17.220537
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-24 20:28:19.636829
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 20:28:22.053717
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 20:28:24.472068
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 20:28:26.888373
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-24 20:28:29.306193
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-24 20:28:31.721686
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-24 20:28:34.139487
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 20:28:36.556229
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 20:28:38.982553
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 20:28:41.405652
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-24 20:28:43.817610
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-24 20:28:46.235060
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-24 20:28:48.650324
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 20:28:51.066701
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 20:28:53.482608
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 20:28:55.899407
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 20:28:58.315511
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 20:29:00.732928
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 20:29:03.149019
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 20:29:05.566853
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 20:29:07.981591
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 20:29:10.400279
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-24 20:29:12.816765
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-24 20:29:15.232568
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-24 20:29:17.648043
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-24 20:29:20.064333
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-24 20:29:26.989434
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-24 20:29:48.574710
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 20:30:15.602982
# Unit test for method run of class ActionModule
def test_ActionModule_run():from types import SimpleNamespace

# Generated at 2026-10-24 20:30:30.566185
# Unit test for method get_args_from_task_vars of class ActionModule
def test_ActionModule_get_args_from_task_vars():import pytest
from unittest.mock import MagicMock

# Adjust import path if this test lives next to the plugin instead of in ansible
from ansible.plugins.action.validate_argument_spec import ActionModule


@pytest.fixture
def action_mod():
    # Skip ActionBase.__init__ (it needs a real task/connection);
    # get_args_from_task_vars only uses self._templar
    am = ActionModule.__new__(ActionModule)
    am._templar = MagicMock()
    am._templar.template.side_effect = lambda x: x  # identity by default
    return am


def test_picks_only_args_present_in_task_vars(action_mod):
    spec = {'name': {'type': 'str'}, 'age': {'type': 'int'}}
    task_vars = {'name': 'bob', 'unrelated': 'x'}
    result = action_mod.get_args_from_task_vars(spec, task_vars)
    assert result == {'name': 'bob'}


def test_templar_called_with_collected_args(action_mod):
    spec = {'a': {'type': 'str'}, 'b': {'type': 'str'}}
    task_vars = {'a': 'x', 'c': 'y'}
    action_mod.get_args_from_task_vars(spec, task_vars)
    action_mod._templar.template.assert_called_once_with({'a': 'x'})


def test_templated_values_are_resolved(action_mod):
    spec = {'name': {'type': 'str'}}
    task_vars = {'name': '{{ first }}', 'first': 'bob'}
    # Simulate templating: {{ first }} -> bob
    action_mod._templar.template.side_effect = lambda d: {k: 'bob' for k in d}
    result = action_mod.get_args_from_task_vars(spec, task_vars)
    assert result == {'name': 'bob'}


def test_empty_argument_spec_returns_empty_dict(action_mod):
    assert action_mod.get_args_from_task_vars({}, {'a': 1}) == {}


def test_no_matching_task_vars_returns_empty_dict(action_mod):
    assert action_mod.get_args_from_task_vars({'a': {'type': 'str'}}, {}) == {}

# Generated at 2026-10-24 20:30:33.089476
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-24 20:30:35.507325
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-24 20:30:37.933049
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-24 20:30:40.344986
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-24 20:30:42.763367
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-24 20:30:45.183269
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-24 20:30:47.600339
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 20:30:50.016468
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 20:31:00.538582
# Unit test for method run of class ActionModule
def test_ActionModule_run():from types import SimpleNamespace

# Generated at 2026-10-24 20:31:03.331895
# Unit test for constructor of class ActionModule
def test_ActionModule():action_module = ActionModule(
        task=None,
        connection=None,
        play_context=None,
        loader=None,
        templar=None,
        shared_loader_obj=None,
    )

# Generated at 2026-10-24 20:31:06.096390
# Unit test for constructor of class ActionModule
def test_ActionModule():action_module = ActionModule(
        task=None,
        connection=None,
        play_context=None,
        loader=None,
        templar=None,
        shared_loader_obj=None,
    )

# Generated at 2026-10-24 20:31:08.868029
# Unit test for constructor of class ActionModule
def test_ActionModule():action_module = ActionModule(
        task=None,
        connection=None,
        play_context=None,
        loader=None,
        templar=None,
        shared_loader_obj=None,
    )

# Generated at 2026-10-24 20:31:10.211298
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 20:31:21.565619
# Unit test for method run of class ActionModule
def test_ActionModule_run():from types import SimpleNamespace

# Generated at 2026-10-24 20:31:24.222197
# Unit test for constructor of class ActionModule
def test_ActionModule():action_module = ActionModule(
        task=None,
        connection=None,
        play_context=None,
        loader=None,
        templar=None,
        shared_loader_obj=None,
    )

# Generated at 2026-10-24 20:31:26.640311
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-24 20:31:29.060577
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-24 20:31:31.477411
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-24 20:31:33.894078
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 20:31:36.469428
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 20:31:38.884858
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 20:31:41.301701
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 20:31:43.718317
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 20:31:46.134655
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 20:31:48.550745
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 20:31:50.969623
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 20:31:53.385633
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 20:31:55.806663
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 20:31:58.228324
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 20:32:00.644936
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 20:32:03.061851
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 20:32:05.482948
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 20:32:07.896137
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 20:32:10.313185
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 20:32:12.732888
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 20:32:15.147891
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 20:32:17.567138
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 20:32:19.982381
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 20:32:22.399651
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 20:32:24.818800
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 20:32:27.237123
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 20:32:29.654099
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 20:32:32.070364
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 20:32:34.486839
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 20:32:36.903212
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 20:32:39.319542
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-24 20:32:41.734308
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-24 20:32:44.150188
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-24 20:32:46.567498
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 20:32:48.985823
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 20:32:51.405019
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 20:32:53.821815
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 20:32:56.239566
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 20:32:58.657907
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 20:33:01.071636
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 20:33:03.490434
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 20:33:05.905891
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 20:33:08.321110
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 20:33:10.740037
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 20:33:13.155213
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 20:33:15.571950
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 20:33:17.990560
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 20:33:20.407752
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 20:33:22.826287
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 20:33:25.242530
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 20:33:27.658348
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 20:33:30.074366
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 20:33:32.492302
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 20:33:34.909505
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 20:33:37.324538
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 20:33:39.740720
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 20:33:42.159292
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 20:33:44.578322
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 20:33:46.995142
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 20:33:49.410518
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 20:33:51.829400
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 20:34:00.982144
# Unit test for method run of class ActionModule
def test_ActionModule_run():from types import SimpleNamespace

# Generated at 2026-10-24 20:34:03.636194
# Unit test for constructor of class ActionModule
def test_ActionModule():action_module = ActionModule(
        task=None,
        connection=None,
        play_context=None,
        loader=None,
        templar=None,
        shared_loader_obj=None,
    )

# Generated at 2026-10-24 20:34:04.993838
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 20:34:15.946837
# Unit test for method run of class ActionModule
def test_ActionModule_run():from types import SimpleNamespace

# Generated at 2026-10-24 20:34:18.583740
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 20:34:21.099279
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 20:34:23.518239
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 20:34:26.507542
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 20:34:28.927343
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 20:34:31.343922
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 20:34:33.762042
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 20:34:36.178469
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 20:34:38.597773
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 20:34:41.015351
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 20:34:43.430605
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 20:34:45.847719
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 20:34:48.265150
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 20:34:50.682865
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 20:34:53.100614
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 20:34:55.518625
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 20:34:57.934199
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 20:35:00.351549
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 20:35:02.770077
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 20:35:05.187131
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 20:35:07.609180
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 20:35:10.029477
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 20:35:12.444797
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 20:35:14.862410
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 20:35:17.278857
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 20:35:19.696334
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 20:35:22.112381
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 20:35:24.528545
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 20:35:26.945409
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 20:35:29.361439
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 20:35:31.782094
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 20:35:34.193061
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 20:35:36.608487
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 20:35:40.168589
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 20:35:52.409330
# Unit test for method run of class ActionModule
def test_ActionModule_run():from types import SimpleNamespace

# Generated at 2026-10-24 20:35:53.820933
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 20:36:03.058752
# Unit test for method run of class ActionModule
def test_ActionModule_run():from types import SimpleNamespace

# Generated at 2026-10-24 20:36:05.823901
# Unit test for constructor of class ActionModule
def test_ActionModule():action_module = ActionModule(
        task=None,
        connection=None,
        play_context=None,
        loader=None,
        templar=None,
        shared_loader_obj=None,
    )

# Generated at 2026-10-24 20:36:08.243160
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 20:36:10.810453
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 20:36:13.228628
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 20:36:15.749763
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 20:36:18.270495
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 20:36:20.692405
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 20:36:23.107668
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 20:36:25.523869
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 20:36:28.130933
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 20:36:30.543117
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 20:36:33.119664
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 20:36:35.536403
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 20:36:37.954963
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 20:36:40.370409
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 20:36:42.791862
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 20:36:45.204963
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 20:36:47.621171
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 20:37:12.485559
# Unit test for constructor of class ActionModule
def test_ActionModule():task = object()

# Generated at 2026-10-24 20:37:14.125324
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 20:37:23.749899
# Unit test for method run of class ActionModule
def test_ActionModule_run():from types import SimpleNamespace

# Generated at 2026-10-24 20:37:30.471952
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 20:37:43.921529
# Unit test for method run of class ActionModule
def test_ActionModule_run():from types import SimpleNamespace

# Generated at 2026-10-24 20:37:46.437608
# Unit test for constructor of class ActionModule