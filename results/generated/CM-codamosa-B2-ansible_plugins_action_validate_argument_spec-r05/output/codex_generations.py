

# Generated at 2026-10-24 02:43:12.378163
# Unit test for method get_args_from_task_vars of class ActionModule
def test_ActionModule_get_args_from_task_vars():
    action = ActionModule.__new__(ActionModule)
    action._templar = MagicMock()

    argument_spec = {
        'name': {'type': 'str'},
        'enabled': {'type': 'bool'},
    }
    task_vars = {
        'name': '{{ role_name }}',
        'enabled': True,
        'role_name': 'example',
        'unrelated': 'must not be included',
    }

    filtered_args = {
        'name': '{{ role_name }}',
        'enabled': True,
    }
    templated_args = {
        'name': 'example',
        'enabled': True,
    }
    action._templar.template.return_value = templated_args

    result = action.get_args_from_task_vars(argument_spec, task_vars)

    action._templar.template.assert_called_once_with(filtered_args)
    assert result == templated_args
    assert 'unrelated' not in result

# Generated at 2026-10-24 02:43:22.286524
# Unit test for method get_args_from_task_vars of class ActionModule
def test_ActionModule_get_args_from_task_vars():
    templar = MagicMock()
    templar.template.return_value = {
        'username': 'admin',
        'port': 443,
    }

    action = ActionModule(
        task=None,
        connection=None,
        play_context=None,
        loader=None,
        templar=templar,
        shared_loader_obj=None,
    )

    argument_spec = {
        'username': {'type': 'str'},
        'port': {'type': 'int'},
        'state': {'type': 'str'},
    }
    task_vars = {
        'username': '{{ configured_username }}',
        'port': 443,
        'unrelated_variable': 'ignored',
    }

    result = action.get_args_from_task_vars(argument_spec, task_vars)

    templar.template.assert_called_once_with({
        'username': '{{ configured_username }}',
        'port': 443,
    })
    assert result == {
        'username': 'admin',
        'port': 443,
    }

# Generated at 2026-10-24 02:43:36.909675
# Unit test for constructor of class ActionModule
def test_ActionModule():
    task = MagicMock()
    connection = MagicMock()
    play_context = MagicMock()
    loader = MagicMock()
    templar = MagicMock()
    shared_loader_obj = MagicMock()

    action = ActionModule(
        task,
        connection,
        play_context,
        loader,
        templar,
        shared_loader_obj,
    )

    assert action._task is task
    assert action._connection is connection
    assert action._play_context is play_context
    assert action._loader is loader
    assert action._templar is templar
    assert action._shared_loader_obj is shared_loader_obj
    assert action.TRANSFERS_FILES is False

# Generated at 2026-10-24 02:43:44.906991
# Unit test for constructor of class ActionModule
def test_ActionModule():action = ActionModule(None, None, None, None, None, None)

# Generated at 2026-10-24 02:44:38.145220
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 02:45:07.431037
# Unit test for method run of class ActionModule
def test_ActionModule_run():from types import SimpleNamespace

# Generated at 2026-10-24 02:45:21.563260
# Unit test for constructor of class ActionModule
def test_ActionModule():
    task = MagicMock()
    connection = MagicMock()
    play_context = MagicMock()
    loader = MagicMock()
    templar = MagicMock()
    shared_loader_obj = MagicMock()

    action = ActionModule(
        task,
        connection,
        play_context,
        loader,
        templar,
        shared_loader_obj,
    )

    assert isinstance(action, ActionModule)
    assert action._task is task
    assert action._connection is connection
    assert action._play_context is play_context
    assert action._loader is loader
    assert action._templar is templar
    assert action._shared_loader_obj is shared_loader_obj
    assert action.TRANSFERS_FILES is False

# Generated at 2026-10-24 02:45:29.086445
# Unit test for constructor of class ActionModule
def test_ActionModule():task = object()

# Generated at 2026-10-24 02:45:50.038951
# Unit test for method run of class ActionModule
def test_ActionModule_run():from types import SimpleNamespace

# Generated at 2026-10-24 02:46:15.544594
# Unit test for method run of class ActionModule
def test_ActionModule_run():from unittest.mock import MagicMock, patch


# Generated at 2026-10-24 02:46:34.370771
# Unit test for method get_args_from_task_vars of class ActionModule
def test_ActionModule_get_args_from_task_vars():
    argument_spec = {
        'username': {'type': 'str'},
        'retries': {'type': 'int'},
    }
    task_vars = {
        'username': '{{ role_user }}',
        'role_user': 'alice',
        'retries': 3,
        'unrelated_variable': 'ignored',
    }

    templar = MagicMock()
    templar.template.return_value = {
        'username': 'alice',
        'retries': 3,
    }

    action = ActionModule.__new__(ActionModule)
    action._templar = templar

    result = action.get_args_from_task_vars(argument_spec, task_vars)

    templar.template.assert_called_once_with({
        'username': '{{ role_user }}',
        'retries': 3,
    })
    assert result == {
        'username': 'alice',
        'retries': 3,
    }

# Generated at 2026-10-24 02:46:44.404545
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

# Generated at 2026-10-24 02:46:51.472584
# Unit test for constructor of class ActionModule
def test_ActionModule():task = object()

# Generated at 2026-10-24 02:47:01.517389
# Unit test for method get_args_from_task_vars of class ActionModule
def test_ActionModule_get_args_from_task_vars():
    class FakeTemplar(object):
        def __init__(self):
            self.received = None

        def template(self, value):
            self.received = value
            return {
                'username': 'rendered-user',
                'port': 8080,
            }

    action = ActionModule.__new__(ActionModule)
    action._templar = FakeTemplar()

    argument_spec = {
        'username': {'type': 'str'},
        'port': {'type': 'int'},
        'missing': {'type': 'str'},
    }
    task_vars = {
        'username': '{{ user_name }}',
        'port': 8080,
        'unrelated_variable': 'must not be included',
    }

    result = action.get_args_from_task_vars(argument_spec, task_vars)

    assert action._templar.received == {
        'username': '{{ user_name }}',
        'port': 8080,
    }
    assert result == {
        'username': 'rendered-user',
        'port': 8080,
    }

# Generated at 2026-10-24 02:47:11.234805
# Unit test for constructor of class ActionModule
def test_ActionModule():
    task = MagicMock()
    connection = MagicMock()
    play_context = MagicMock()
    loader = MagicMock()
    templar = MagicMock()
    shared_loader_obj = MagicMock()

    action = ActionModule(
        task,
        connection,
        play_context,
        loader,
        templar,
        shared_loader_obj,
    )

    assert isinstance(action, ActionModule)
    assert action._task is task
    assert action._connection is connection
    assert action._play_context is play_context
    assert action._loader is loader
    assert action._templar is templar
    assert action._shared_loader_obj is shared_loader_obj
    assert action.TRANSFERS_FILES is False

# Generated at 2026-10-24 02:47:20.040798
# Unit test for constructor of class ActionModule
def test_ActionModule():task = object()

# Generated at 2026-10-24 02:47:30.281038
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

    assert isinstance(action, ActionBase)
    assert action._task is task
    assert action._connection is connection
    assert action._play_context is play_context
    assert action._loader is loader
    assert action._templar is templar
    assert action._shared_loader_obj is shared_loader_obj
    assert action.TRANSFERS_FILES is False

# Generated at 2026-10-24 02:47:38.062600
# Unit test for constructor of class ActionModule
def test_ActionModule():task = object()

# Generated at 2026-10-24 02:48:04.789051
# Unit test for method run of class ActionModule
def test_ActionModule_run():import sys

# Generated at 2026-10-24 02:48:16.739468
# Unit test for method get_args_from_task_vars of class ActionModule
def test_ActionModule_get_args_from_task_vars():
    action = ActionModule.__new__(ActionModule)
    action._templar = Mock()
    action._templar.template.return_value = {
        'username': 'alice',
        'enabled': True,
    }

    argument_spec = {
        'username': {'type': 'str'},
        'enabled': {'type': 'bool'},
        'missing': {'type': 'str'},
    }
    task_vars = {
        'username': '{{ role_username }}',
        'enabled': True,
        'role_username': 'alice',
        'unrelated': 'ignored',
    }

    result = action.get_args_from_task_vars(argument_spec, task_vars)

    action._templar.template.assert_called_once_with({
        'username': '{{ role_username }}',
        'enabled': True,
    })
    assert result == {
        'username': 'alice',
        'enabled': True,
    }

# Generated at 2026-10-24 02:48:35.759081
# Unit test for method get_args_from_task_vars of class ActionModule
def test_ActionModule_get_args_from_task_vars():
    action = ActionModule.__new__(ActionModule)
    action._templar = MagicMock()

    argument_spec = {
        'username': {'type': 'str'},
        'enabled': {'type': 'bool'},
        'missing': {'type': 'str'},
    }
    task_vars = {
        'username': '{{ account_name }}',
        'enabled': False,
        'account_name': 'alice',
        'unrelated': 'ignored',
    }

    templated_args = {
        'username': 'alice',
        'enabled': False,
    }
    action._templar.template.return_value = templated_args

    result = action.get_args_from_task_vars(argument_spec, task_vars)

    action._templar.template.assert_called_once_with({
        'username': '{{ account_name }}',
        'enabled': False,
    })
    assert result == templated_args

# Generated at 2026-10-24 02:48:46.374476
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

# Generated at 2026-10-24 02:48:55.275928
# Unit test for constructor of class ActionModule
def test_ActionModule():task = object()

# Generated at 2026-10-24 02:49:10.236554
# Unit test for method get_args_from_task_vars of class ActionModule
def test_ActionModule_get_args_from_task_vars():
    action = object.__new__(ActionModule)
    action._templar = MagicMock()
    action._templar.template.return_value = {
        'username': 'alice',
        'retries': 3,
    }

    argument_spec = {
        'username': {'type': 'str'},
        'retries': {'type': 'int'},
        'missing': {'type': 'bool'},
    }
    task_vars = {
        'username': '{{ role_username }}',
        'role_username': 'alice',
        'retries': 3,
        'unrelated': 'ignored',
    }

    result = action.get_args_from_task_vars(argument_spec, task_vars)

    action._templar.template.assert_called_once_with({
        'username': '{{ role_username }}',
        'retries': 3,
    })
    assert result == {
        'username': 'alice',
        'retries': 3,
    }

# Generated at 2026-10-24 02:49:48.624926
# Unit test for method get_args_from_task_vars of class ActionModule
def test_ActionModule_get_args_from_task_vars():
    argument_spec = {
        'name': {'type': 'str', 'required': True},
        'port': {'type': 'int', 'required': False},
        'extra': {'type': 'str', 'required': False},
    }
    task_vars = {
        'name': 'web01',
        'port': '{{ http_port }}',   # templated value must be resolved
        'not_in_spec': 'ignored',    # task var not in spec must be dropped
    }

    templar = MagicMock()

    def fake_template(data):
        return {k: (9090 if v == '{{ http_port }}' else v) for k, v in data.items()}

    templar.template.side_effect = fake_template

    am = _make_action(templar)
    result = am.get_args_from_task_vars(argument_spec, task_vars)

    # Only spec-defined args kept, templated value resolved
    assert result == {'name': 'web01', 'port': 9090}
    templar.template.assert_called_once_with({'name': 'web01', 'port': '{{ http_port }}'})


def test_ActionModule_get_args_from_task_vars_empty_task_vars():
    argument_spec = {'name': {'type': 'str'}}
    templar = MagicMock()
    templar.template.side_effect = lambda data: data

    am = _make_action(templar)
    result = am.get_args_from_task_vars(argument_spec, {})

    assert result == {}
    templar.template.assert_called_once_with({})


def test_ActionModule_get_args_from_task_vars_no_matching_vars():
    argument_spec = {'name': {'type': 'str'}, 'port': {'type': 'int'}}
    task_vars = {'something_else': 'x'}
    templar = MagicMock()
    templar.template.side_effect = lambda data: data

    am = _make_action(templar)
    result = am.get_args_from_task_vars(argument_spec, task_vars)

    assert result == {}

# Generated at 2026-10-24 02:50:09.105691
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 02:51:09.171486
# Unit test for method run of class ActionModule
def test_ActionModule_run():from types import SimpleNamespace

# Generated at 2026-10-24 02:51:12.080358
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 02:51:14.848598
# Unit test for method run of class ActionModule
def test_ActionModule_run():from types import SimpleNamespace

# Generated at 2026-10-24 02:51:23.957910
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert issubclass(ActionModule, ActionBase)

# Generated at 2026-10-24 02:51:57.965670
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 02:52:00.923636
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 02:52:17.461964
# Unit test for method get_args_from_task_vars of class ActionModule
def test_ActionModule_get_args_from_task_vars():
    argument_spec = {
        'name': {'type': 'str', 'required': True},
        'port': {'type': 'int', 'required': False},
        'extra': {'type': 'str', 'required': False},
    }
    task_vars = {
        'name': 'web01',
        'port': '{{ http_port }}',   # templated value must be resolved
        'not_in_spec': 'ignored',    # task var not in spec must be dropped
    }

    templar = MagicMock()

    def fake_template(data):
        return {k: (9090 if v == '{{ http_port }}' else v) for k, v in data.items()}

    templar.template.side_effect = fake_template

    am = _make_action(templar)
    result = am.get_args_from_task_vars(argument_spec, task_vars)

    # Only spec-defined args kept, templated value resolved
    assert result == {'name': 'web01', 'port': 9090}
    templar.template.assert_called_once_with({'name': 'web01', 'port': '{{ http_port }}'})


def test_ActionModule_get_args_from_task_vars_empty_task_vars():
    argument_spec = {'name': {'type': 'str'}}
    templar = MagicMock()
    templar.template.side_effect = lambda data: data

    am = _make_action(templar)
    result = am.get_args_from_task_vars(argument_spec, {})

    assert result == {}
    templar.template.assert_called_once_with({})


def test_ActionModule_get_args_from_task_vars_no_matching_vars():
    argument_spec = {'name': {'type': 'str'}, 'port': {'type': 'int'}}
    task_vars = {'something_else': 'x'}
    templar = MagicMock()
    templar.template.side_effect = lambda data: data

    am = _make_action(templar)
    result = am.get_args_from_task_vars(argument_spec, task_vars)

    assert result == {}

# Generated at 2026-10-24 02:52:20.298078
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 02:52:23.353417
# Unit test for method run of class ActionModule
def test_ActionModule_run():from types import SimpleNamespace

# Generated at 2026-10-24 02:52:26.222385
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 02:52:28.930593
# Unit test for method run of class ActionModule
def test_ActionModule_run():from types import SimpleNamespace

# Generated at 2026-10-24 02:52:30.312394
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert issubclass(ActionModule, ActionBase)

# Generated at 2026-10-24 02:52:33.384619
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 02:52:36.251067
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 02:52:37.686452
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert issubclass(ActionModule, ActionBase)

# Generated at 2026-10-24 02:52:40.758231
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 02:52:43.733762
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 02:52:46.821833
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 02:52:49.687223
# Unit test for method run of class ActionModule
def test_ActionModule_run():from types import SimpleNamespace

# Generated at 2026-10-24 02:52:52.427584
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 02:52:55.310346
# Unit test for method run of class ActionModule
def test_ActionModule_run():from types import SimpleNamespace

# Generated at 2026-10-24 02:52:58.165685
# Unit test for method run of class ActionModule

# Generated at 2026-10-24 02:53:01.027982
# Unit test for method run of class ActionModule
def test_ActionModule_run():from types import SimpleNamespace

# Generated at 2026-10-24 02:53:02.466923
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert issubclass(ActionModule, ActionBase)

# Generated at 2026-10-24 02:53:05.435807
# Unit test for constructor of class ActionModule

# Generated at 2026-10-24 02:53:08.405249
# Unit test for constructor of class ActionModule