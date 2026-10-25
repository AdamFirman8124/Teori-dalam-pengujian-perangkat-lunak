

# Generated at 2026-10-25 02:49:02.881955
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 02:49:05.296662
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 02:49:07.711153
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 02:49:10.127644
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 02:49:12.551325
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 02:49:14.961863
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 02:49:17.377418
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 02:49:19.792411
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 02:49:22.539335
# Unit test for constructor of class ActionModule
def test_ActionModule():from unittest.mock import MagicMock

# Generated at 2026-10-25 02:49:32.052001
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
    assert isinstance(action, ActionBase)
    assert action._task is task
    assert action._connection is connection
    assert action._play_context is play_context
    assert action._loader is loader
    assert action._templar is templar
    assert action._shared_loader_obj is shared_loader_obj
    assert action.TRANSFERS_FILES is False

# Generated at 2026-10-25 02:49:41.384862
# Unit test for constructor of class ActionModule
def test_ActionModule():task = object()

# Generated at 2026-10-25 02:50:02.257980
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 02:50:04.674270
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 02:50:07.090121
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 02:50:09.505337
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-25 02:50:11.919006
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-25 02:50:14.333890
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-25 02:50:16.750070
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 02:50:19.164421
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 02:50:21.579393
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 02:50:23.994129
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-25 02:50:26.409755
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-25 02:50:28.825247
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-25 02:50:31.251887
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 02:50:33.666121
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 02:50:36.084780
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 02:50:47.524368
# Unit test for method get_args_from_task_vars of class ActionModule
def test_ActionModule_get_args_from_task_vars():
    argument_spec = {
        'username': {'type': 'str'},
        'password': {'type': 'str'},
    }
    task_vars = {
        'username': '{{ configured_username }}',
        'configured_username': 'admin',
        'unrelated_variable': 'ignored',
    }

    templar = MagicMock()
    templar.template.return_value = {'username': 'admin'}

    action = object.__new__(ActionModule)
    action._templar = templar

    result = action.get_args_from_task_vars(argument_spec, task_vars)

    templar.template.assert_called_once_with({
        'username': '{{ configured_username }}',
    })
    assert result == {'username': 'admin'}

# Generated at 2026-10-25 02:51:08.821052
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 02:51:11.915639
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 02:51:14.431456
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 02:51:16.847306
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-25 02:51:19.264750
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-25 02:51:21.683075
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-25 02:51:24.099906
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 02:51:26.515156
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 02:51:28.930042
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 02:51:31.344533
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 02:51:33.760050
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 02:51:36.174618
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 02:51:38.593026
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-25 02:51:41.004926
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-25 02:51:43.426014
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-25 02:51:45.836681
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 02:51:48.252197
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 02:51:50.668150
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 02:51:53.084154
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-25 02:51:55.498914
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-25 02:51:57.914070
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-25 02:52:00.329780
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 02:52:02.745419
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 02:52:05.158402
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 02:52:07.576230
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 02:52:09.990024
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 02:52:12.406230
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 02:52:14.818240
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 02:52:17.234363
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 02:52:19.661310
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 02:52:22.065103
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 02:52:24.479582
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 02:52:26.895118
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 02:52:29.309118
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 02:52:31.724439
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 02:52:34.138185
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 02:52:36.552515
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-25 02:52:38.966073
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-25 02:52:41.380364
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-25 02:52:43.795308
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 02:52:46.209546
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 02:52:48.624335
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 02:52:51.038737
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 02:52:53.452920
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 02:52:55.870123
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 02:52:58.630683
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 02:53:01.045381
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 02:53:03.462167
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 02:53:05.878042
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 02:53:08.292690
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 02:53:10.707723
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 02:53:13.122570
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 02:53:15.537624
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 02:53:17.952501
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 02:53:20.367987
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 02:53:22.783189
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 02:53:25.199696
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 02:53:27.613615
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 02:53:30.039322
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 02:53:32.455083
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 02:53:34.872321
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-25 02:53:37.289256
# Unit test for method get_args_from_task_vars of class ActionModule

# Generated at 2026-10-25 02:53:44.484987
# Unit test for method get_args_from_task_vars of class ActionModule
def test_ActionModule_get_args_from_task_vars():action = ActionModule.__new__(ActionModule)


# Generated at 2026-10-25 02:53:53.906442
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

# Generated at 2026-10-25 02:54:01.181988
# Unit test for constructor of class ActionModule
def test_ActionModule():task = object()

# Generated at 2026-10-25 02:54:10.193508
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

# Generated at 2026-10-25 02:54:17.150596
# Unit test for constructor of class ActionModule
def test_ActionModule():task = object()

# Generated at 2026-10-25 02:54:20.174000
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 02:54:22.708947
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 02:54:25.447807
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 02:54:27.865804
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 02:54:30.282853
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 02:54:32.703600
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 02:54:35.275510
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 02:54:37.690789
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 02:54:40.105219
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 02:54:42.521105
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 02:54:44.934828
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 02:54:54.152293
# Unit test for constructor of class ActionModule
def test_ActionModule():task = object()

# Generated at 2026-10-25 02:55:08.149921
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

# Generated at 2026-10-25 02:55:15.040668
# Unit test for constructor of class ActionModule
def test_ActionModule():task = object()

# Generated at 2026-10-25 02:55:17.797357
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 02:55:38.886248
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 02:55:41.557508
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 02:55:43.973245
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 02:55:46.390162
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 02:55:48.807000
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 02:55:51.821542
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 02:55:54.545541
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 02:55:57.400651
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 02:56:00.371689
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 02:56:03.442505
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 02:56:06.310327
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 02:56:09.074941
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 02:56:11.832959
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 02:56:14.601417
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 02:56:23.001836
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

# Generated at 2026-10-25 02:56:25.418652
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 02:56:27.834551
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 02:56:30.251540
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 02:56:32.677987
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 02:56:35.081362
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 02:56:37.658644
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 02:56:40.073275
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 02:56:42.489206
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 02:56:44.905294
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 02:56:47.322535
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 02:56:49.737286
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 02:56:52.152585
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 02:56:54.567916
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 02:56:56.982785
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 02:56:59.398316
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 02:57:01.815863
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 02:57:04.229418
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 02:57:06.644695
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 02:57:09.060160
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 02:57:11.476586
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 02:57:13.893287
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 02:57:16.313138
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 02:57:26.101923
# Unit test for constructor of class ActionModule
def test_ActionModule():task = object()

# Generated at 2026-10-25 02:57:28.903735
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 02:57:31.605452
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 02:57:34.375896
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 02:57:37.446616
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 02:57:40.209995
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 02:57:42.977838
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 02:57:45.390308
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 02:57:47.807171
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 02:57:50.222274
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 02:57:52.798361
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 02:57:55.212189
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 02:57:57.629803
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 02:58:01.856990
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 02:58:04.275987
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 02:58:06.697806
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 02:58:09.114778
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 02:58:11.530766
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 02:58:13.945026
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 02:58:16.362799
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 02:58:18.777701
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 02:58:21.191799
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 02:58:23.607976
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 02:58:26.028284
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 02:58:28.442350
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 02:58:30.857755
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 02:58:33.272191
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 02:58:35.686307
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 02:58:38.101542
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 02:58:40.516073
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 02:58:42.932365
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 02:58:45.346972
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 02:58:47.761659
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 02:58:50.178599
# Unit test for method run of class ActionModule

# Generated at 2026-10-25 02:58:52.593594
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 02:58:55.007222
# Unit test for constructor of class ActionModule

# Generated at 2026-10-25 02:59:03.869344
# Unit test for constructor of class ActionModule
def test_ActionModule():from unittest.mock import MagicMock
