

# Generated at 2026-10-25 03:06:21.192299
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:06:23.605786
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:06:26.022224
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:06:37.519079
# Unit test for method get_args_from_task_vars of class ActionModule
def test_ActionModule_get_args_from_task_vars():
    class FakeTemplar(object):
        def __init__(self):
            self.received = None

        def template(self, value):
            self.received = value
            return {
                'username': 'alice',
                'port': 8080,
            }

    action = ActionModule.__new__(ActionModule)
    action._templar = FakeTemplar()

    argument_spec = {
        'username': {'type': 'str'},
        'port': {'type': 'int'},
        'enabled': {'type': 'bool'},
    }
    task_vars = {
        'username': '{{ role_username }}',
        'port': '{{ role_port }}',
        'role_username': 'alice',
        'role_port': 8080,
        'unrelated_variable': 'ignored',
    }

    result = action.get_args_from_task_vars(argument_spec, task_vars)

    # Only variables named in the argument specification are passed for
    # templating. Missing and unrelated variables must not be included.
    assert action._templar.received == {
        'username': '{{ role_username }}',
        'port': '{{ role_port }}',
    }
    assert result == {
        'username': 'alice',
        'port': 8080,
    }

# Generated at 2026-10-25 03:06:46.726545
# Unit test for method get_args_from_task_vars of class ActionModule
def test_ActionModule_get_args_from_task_vars():
    class FakeTemplar:
        def __init__(self):
            self.received = None

        def template(self, value):
            self.received = value
            return {
                'name': 'expanded value',
                'count': 3,
            }

    action = object.__new__(ActionModule)
    action._templar = FakeTemplar()

    argument_spec = {
        'name': {'type': 'str'},
        'count': {'type': 'int'},
    }
    task_vars = {
        'name': '{{ variable }}',
        'count': 3,
        'unrelated_variable': 'ignored',
    }

    result = action.get_args_from_task_vars(argument_spec, task_vars)

    assert action._templar.received == {
        'name': '{{ variable }}',
        'count': 3,
    }
    assert result == {
        'name': 'expanded value',
        'count': 3,
    }

# Generated at 2026-10-25 03:06:57.349532
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-25 03:07:04.709227
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-25 03:07:07.235192
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-25 03:07:09.651652
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:07:12.250575
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:07:14.664928
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:07:17.079896
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-25 03:07:19.496598
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-25 03:07:21.910498
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-25 03:07:24.325777
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:07:26.740173
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:07:29.355314
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:07:32.116671
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:07:34.967898
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:07:37.824527
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:07:40.694323
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:07:43.584155
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:07:46.346145
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:07:55.440165
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

# Generated at 2026-10-25 03:07:57.973992
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 03:08:00.388268
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 03:08:02.991034
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 03:08:05.405811
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 03:08:07.825314
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 03:08:10.241467
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 03:08:12.656299
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 03:08:15.073837
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 03:08:17.491362
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:08:19.908625
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:08:22.323625
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:08:24.739572
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:08:27.156246
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:08:29.571750
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:08:31.986166
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-25 03:08:34.400001
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-25 03:08:36.815838
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-25 03:08:39.230318
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 03:08:41.644734
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 03:08:44.059709
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 03:08:46.474198
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 03:08:48.889514
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 03:08:51.309409
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 03:08:53.728211
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 03:08:56.143049
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 03:08:58.557814
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 03:09:00.971834
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:09:03.385226
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:09:05.800071
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:09:08.215592
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:09:10.631050
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:09:13.045816
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:09:15.460227
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:09:17.876574
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:09:20.292305
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:09:22.705660
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:09:25.120000
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:09:27.536195
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:09:29.951021
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-25 03:09:32.365939
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-25 03:09:34.782099
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-25 03:09:37.199376
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:09:39.614398
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:09:42.029069
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:09:44.445219
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:09:46.865033
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:09:49.285069
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:09:51.702467
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 03:09:54.117752
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 03:09:56.533352
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 03:09:58.947419
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:10:01.362279
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:10:03.777100
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:10:06.191964
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 03:10:08.607044
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 03:10:11.022677
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 03:10:13.438338
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 03:10:15.852751
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 03:10:18.267731
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 03:10:21.052237
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:10:23.913492
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:10:26.643357
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:10:36.917892
# Unit test for constructor of class ActionModule
def test_ActionModule():
    task = object()
    connection = object()
    play_context = object()
    loader = object()
    templar = object()
    shared_loader_obj = object()

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

# Generated at 2026-10-25 03:10:39.701407
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:10:42.586964
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:10:45.728600
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:10:56.374651
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

# Generated at 2026-10-25 03:10:58.791152
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 03:11:01.207032
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 03:11:03.619937
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:11:06.204772
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:11:08.619551
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:11:11.035606
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 03:11:13.450665
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 03:11:15.863989
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 03:11:18.279066
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:11:20.693922
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:11:23.111238
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:11:25.527090
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 03:11:27.943726
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 03:11:30.359684
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 03:11:32.775443
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 03:11:41.302197
# Unit test for constructor of class ActionModule
def test_ActionModule():task = object()

# Generated at 2026-10-25 03:11:44.283052
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:11:46.989296
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:11:49.715055
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:11:52.457643
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:11:55.165139
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:11:57.877724
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:12:00.507152
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 03:12:02.923264
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 03:12:05.338306
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 03:12:07.753392
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:12:10.167044
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:12:12.582931
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:12:14.997882
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:12:17.412107
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:12:19.826273
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:12:22.253967
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:12:24.661299
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:12:27.075314
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:12:29.490702
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:12:31.908851
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:12:34.322405
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:12:36.737568
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 03:12:39.153644
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 03:12:41.568971
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 03:12:43.982453
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:12:46.399460
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:12:48.815109
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:12:51.476885
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:12:54.256104
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:12:57.011510
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:12:59.744341
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:13:02.478651
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:13:05.204012
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:13:07.976949
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:13:10.498540
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:13:13.020580
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:13:15.435503
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:13:17.852254
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:13:20.424774
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:13:22.842577
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 03:13:25.255481
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 03:13:27.675776
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 03:13:30.101995
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:13:32.506358
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:13:34.922276
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:13:37.335701
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:13:39.750676
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:13:42.168414
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:13:44.584976
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:13:46.999810
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:13:49.415096
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:13:51.829761
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:13:54.755101
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:13:57.526276
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:14:06.019381
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

# Generated at 2026-10-25 03:14:14.006612
# Unit test for constructor of class ActionModule
def test_ActionModule():task = object()

# Generated at 2026-10-25 03:14:22.813061
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

# Generated at 2026-10-25 03:14:25.228332
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 03:14:27.643423
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 03:14:30.060456
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:14:32.475130
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:14:34.890122
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:14:37.306379
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:14:39.720387
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:14:42.135408
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:14:44.550049
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:14:46.964631
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:14:49.378882
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:14:51.793019
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:14:54.210113
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:14:56.624757
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:14:59.038862
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:15:01.453275
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:15:03.867603
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:15:06.281923
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:15:08.695829
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:15:11.110153
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:15:13.526465
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 03:15:15.945756
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 03:15:18.364794
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 03:15:21.861601
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:15:24.276251
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:15:26.690550
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:15:29.106397
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 03:15:31.521326
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 03:15:33.934895
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 03:15:36.543982
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:15:39.388800
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:15:42.288888
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:16:05.984678
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from unittest.mock import MagicMock
    try:
        cls = ActionModule
    except NameError:
        from ansible.plugins.action.validate_argument_spec import ActionModule as cls
    task = MagicMock()
    connection = MagicMock()
    play_context = MagicMock()
    loader = MagicMock()
    templar = MagicMock()
    shared_loader_obj = MagicMock()
    obj = cls(task, connection, play_context, loader, templar, shared_loader_obj)
    assert isinstance(obj, cls)
    assert obj._task is task
    assert obj._connection is connection
    assert obj._play_context is play_context
    assert obj._loader is loader
    assert obj._templar is templar
    assert obj._shared_loader_obj is shared_loader_obj
    assert obj.TRANSFERS_FILES is False

# Generated at 2026-10-25 03:16:13.916986
# Unit test for constructor of class ActionModule
def test_ActionModule():from unittest.mock import MagicMock


# Generated at 2026-10-25 03:16:16.612467
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:16:19.461667
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 03:16:22.302427
# Unit test for method run of class ActionModule