

# Generated at 2024-05-31 20:08:38.436264
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    handler_task_include = HandlerTaskInclude()
    assert isinstance(handler_task_include, HandlerTaskInclude)
    assert isinstance(handler_task_include, Handler)
    assert isinstance(handler_task_include, TaskInclude)
    assert 'listen' in handler_task_include.VALID_INCLUDE_KEYWORDS

# Generated at 2024-05-31 20:08:39.683783
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    handler_task_include = HandlerTaskInclude()
    assert isinstance(handler_task_include, HandlerTaskInclude)
    assert isinstance(handler_task_include, Handler)
    assert isinstance(handler_task_include, TaskInclude)
    assert 'listen' in handler_task_include.VALID_INCLUDE_KEYWORDS

# Generated at 2024-05-31 20:08:41.392663
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    block = "test_block"
    role = "test_role"
    task_include = "test_task_include"
    handler_task_include = HandlerTaskInclude(block=block, role=role, task_include=task_include)
    
    assert handler_task_include.block == block
    assert handler_task_include.role == role
    assert handler_task_include.task_include == task_include

# Generated at 2024-05-31 20:08:44.847416
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    data = {
        'name': 'Test Handler',
        'listen': 'test_event',
        'action': 'debug',
        'args': {'msg': 'This is a test'}
    }
    block = None
    role = None
    task_include = None
    variable_manager = None
    loader = None

    handler = HandlerTaskInclude.load(data, block, role, task_include, variable_manager, loader)

    assert handler.get_name() == 'Test Handler'
    assert handler.listen == 'test_event'
    assert handler.action == 'debug'
    assert handler.args == {'msg': 'This is a test'}

# Generated at 2024-05-31 20:08:49.326880
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():    data = {
        'name': 'Test Handler',
        'listen': 'test_event',
        'action': 'debug',
        'args': {'msg': 'This is a test'}
    }

# Generated at 2024-05-31 20:08:52.501784
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():    data = {
        'name': 'Test Handler',
        'listen': 'test_event',
        'action': 'debug',
    }

# Generated at 2024-05-31 20:08:55.320212
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    handler_task_include = HandlerTaskInclude()
    assert isinstance(handler_task_include, HandlerTaskInclude)
    assert isinstance(handler_task_include, Handler)
    assert isinstance(handler_task_include, TaskInclude)
    assert 'listen' in handler_task_include.VALID_INCLUDE_KEYWORDS

# Generated at 2024-05-31 20:08:58.076187
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():    data = {
        'name': 'Test Handler',
        'listen': 'test_event'
    }

# Generated at 2024-05-31 20:09:00.049511
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():    data = {
        'name': 'Test Handler',
        'listen': 'test_event'
    }

# Generated at 2024-05-31 20:09:02.095852
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():    data = {
        'name': 'Test Handler',
        'listen': 'test_event'
    }

# Generated at 2024-05-31 20:09:08.939516
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():    data = {
        'name': 'Test Handler',
        'listen': 'test_event'
    }

# Generated at 2024-05-31 20:09:11.609832
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():    data = {
        'name': 'Test Handler',
        'listen': 'test_event'
    }

# Generated at 2024-05-31 20:09:12.937825
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    handler_task_include = HandlerTaskInclude()
    assert isinstance(handler_task_include, HandlerTaskInclude)
    assert isinstance(handler_task_include, Handler)
    assert isinstance(handler_task_include, TaskInclude)
    assert 'listen' in handler_task_include.VALID_INCLUDE_KEYWORDS

# Generated at 2024-05-31 20:09:14.805933
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():    block = "test_block"

# Generated at 2024-05-31 20:09:16.462848
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():    block = "test_block"

# Generated at 2024-05-31 20:09:19.350630
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():    data = {
        'name': 'Test Handler',
        'listen': 'test_event'
    }

# Generated at 2024-05-31 20:09:21.523478
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():    data = {
        'name': 'Test Handler',
        'listen': 'test_event'
    }

# Generated at 2024-05-31 20:09:23.562507
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():    data = {
        'name': 'Test Handler',
        'listen': 'test_event'
    }

# Generated at 2024-05-31 20:09:25.674852
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():    block = "test_block"

# Generated at 2024-05-31 20:09:28.861606
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():    data = {
        'name': 'Test Handler',
        'listen': 'test_event'
    }

# Generated at 2024-05-31 20:09:38.939832
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    data = {
        'name': 'Test Handler',
        'listen': 'test_event',
        'action': 'debug',
        'args': {'msg': 'This is a test'}
    }
    block = None
    role = None
    task_include = None
    variable_manager = None
    loader = None

    handler = HandlerTaskInclude.load(data, block, role, task_include, variable_manager, loader)

    assert handler is not None
    assert handler.get_name() == 'Test Handler'
    assert handler.listen == 'test_event'
    assert handler.action == 'debug'
    assert handler.args == {'msg': 'This is a test'}

# Generated at 2024-05-31 20:09:41.637882
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():    data = {
        'name': 'Test Handler',
        'listen': 'test_event'
    }

# Generated at 2024-05-31 20:09:44.261278
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():    data = {'name': 'Test Handler', 'listen': 'test_event'}

# Generated at 2024-05-31 20:09:46.201510
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():    block = "test_block"

# Generated at 2024-05-31 20:09:50.493707
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():    data = {
        'name': 'Test Handler',
        'listen': 'test_event',
        'action': 'debug',
    }

# Generated at 2024-05-31 20:09:52.767396
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():    data = {
        'name': 'Test Handler',
        'listen': 'test_event'
    }

# Generated at 2024-05-31 20:09:54.698215
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():    data = {
        'name': 'Test Handler',
        'listen': 'test_event'
    }

# Generated at 2024-05-31 20:09:58.316028
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():    data = {
        'name': 'Test Handler',
        'listen': 'test_event'
    }

# Generated at 2024-05-31 20:10:02.104511
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():    data = {
        'name': 'Test Handler',
        'listen': 'test_event'
    }

# Generated at 2024-05-31 20:10:04.781743
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():    block = "test_block"

# Generated at 2024-05-31 20:10:16.601172
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():    data = {
        'name': 'Test Handler',
        'listen': 'test_event'
    }

# Generated at 2024-05-31 20:10:19.093522
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():    data = {
        'name': 'Test Handler',
        'listen': 'test_event'
    }

# Generated at 2024-05-31 20:10:22.267126
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():    data = {
        'name': 'Test Handler',
        'listen': 'test_event'
    }

# Generated at 2024-05-31 20:10:25.258575
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():    data = {
        'name': 'Test Handler',
        'listen': 'test_event'
    }

# Generated at 2024-05-31 20:10:26.517430
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    handler_task_include = HandlerTaskInclude()
    assert isinstance(handler_task_include, HandlerTaskInclude)
    assert isinstance(handler_task_include, Handler)
    assert isinstance(handler_task_include, TaskInclude)
    assert 'listen' in handler_task_include.VALID_INCLUDE_KEYWORDS

# Generated at 2024-05-31 20:10:28.705613
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():    block = "test_block"

# Generated at 2024-05-31 20:10:30.514264
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():    block = "test_block"

# Generated at 2024-05-31 20:10:32.495477
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():    block = "test_block"

# Generated at 2024-05-31 20:10:35.557685
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():    data = {'name': 'Test Handler', 'listen': 'test_event'}

# Generated at 2024-05-31 20:10:38.286040
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():    data = {
        'name': 'Test Handler',
        'listen': 'test_event',
        'action': 'debug',
        'args': {'msg': 'This is a test'}
    }

# Generated at 2024-05-31 20:10:58.010419
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():    block = "test_block"

# Generated at 2024-05-31 20:10:59.386139
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    handler_task_include = HandlerTaskInclude()
    assert isinstance(handler_task_include, HandlerTaskInclude)
    assert isinstance(handler_task_include, Handler)
    assert isinstance(handler_task_include, TaskInclude)
    assert 'listen' in handler_task_include.VALID_INCLUDE_KEYWORDS

# Generated at 2024-05-31 20:11:01.452089
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    handler_task_include = HandlerTaskInclude()
    assert isinstance(handler_task_include, HandlerTaskInclude)
    assert isinstance(handler_task_include, Handler)
    assert isinstance(handler_task_include, TaskInclude)
    assert 'listen' in handler_task_include.VALID_INCLUDE_KEYWORDS

# Generated at 2024-05-31 20:11:04.201209
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():    data = {
        'name': 'Test Handler',
        'listen': 'test_event'
    }

# Generated at 2024-05-31 20:11:06.464171
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():    block = "test_block"

# Generated at 2024-05-31 20:11:08.030766
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():    block = "test_block"

# Generated at 2024-05-31 20:11:10.777688
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():    data = {
        'name': 'Test Handler',
        'listen': 'test_event'
    }

# Generated at 2024-05-31 20:11:14.820730
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():    data = {
        'name': 'Test Handler',
        'listen': 'test_event'
    }

# Generated at 2024-05-31 20:11:17.622966
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():    data = {
        'name': 'Test Handler',
        'listen': 'test_event'
    }

# Generated at 2024-05-31 20:11:21.643975
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():    data = {
        'name': 'Test Handler',
        'listen': 'test_event'
    }

# Generated at 2024-05-31 20:11:59.597849
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():    data = {'name': 'Test Handler', 'listen': 'test_event'}

# Generated at 2024-05-31 20:12:01.983665
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():    data = {
        'name': 'Test Handler',
        'listen': 'test_event'
    }

# Generated at 2024-05-31 20:12:04.077705
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    block = "test_block"
    role = "test_role"
    task_include = "test_task_include"
    handler_task_include = HandlerTaskInclude(block=block, role=role, task_include=task_include)
    
    assert handler_task_include.block == block
    assert handler_task_include.role == role
    assert handler_task_include.task_include == task_include

# Generated at 2024-05-31 20:12:07.525574
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():    data = {
        'name': 'Test Handler',
        'listen': 'test_event'
    }

# Generated at 2024-05-31 20:12:09.820965
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():    data = {
        'name': 'Test Handler',
        'listen': 'test_event'
    }

# Generated at 2024-05-31 20:12:12.310645
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():    block = "test_block"

# Generated at 2024-05-31 20:12:14.802741
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():    block = "test_block"

# Generated at 2024-05-31 20:12:16.836555
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():    block = "test_block"

# Generated at 2024-05-31 20:12:19.155813
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():    data = {
        'name': 'Test Handler',
        'listen': 'test_event'
    }

# Generated at 2024-05-31 20:12:20.867528
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():    block = "test_block"

# Generated at 2024-05-31 20:13:31.482005
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():    data = {
        'name': 'Test Handler',
        'listen': 'test_event'
    }

# Generated at 2024-05-31 20:13:32.861547
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    handler_task_include = HandlerTaskInclude()
    assert isinstance(handler_task_include, HandlerTaskInclude)
    assert isinstance(handler_task_include, Handler)
    assert isinstance(handler_task_include, TaskInclude)
    assert 'listen' in handler_task_include.VALID_INCLUDE_KEYWORDS

# Generated at 2024-05-31 20:13:34.671399
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():    data = {
        'name': 'Test Handler',
        'listen': 'test_event'
    }

# Generated at 2024-05-31 20:13:36.653542
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():    data = {
        'name': 'Test Handler',
        'listen': 'test_event'
    }

# Generated at 2024-05-31 20:13:39.818930
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    data = {
        'name': 'Test Handler',
        'listen': 'test_event',
        'action': 'debug',
    }
    block = None
    role = None
    task_include = None
    variable_manager = None
    loader = None

    handler = HandlerTaskInclude.load(data, block, role, task_include, variable_manager, loader)

    assert handler is not None
    assert handler.get_name() == 'Test Handler'
    assert handler.listen == 'test_event'
    assert handler.action == 'debug'

# Generated at 2024-05-31 20:13:42.589009
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():    data = {
        'name': 'Test Handler',
        'listen': 'test_event'
    }

# Generated at 2024-05-31 20:13:44.910631
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():    data = {'name': 'Test Handler', 'listen': 'test_event'}

# Generated at 2024-05-31 20:13:48.561582
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():    data = {
        'name': 'Test Handler',
        'listen': 'test_event'
    }

# Generated at 2024-05-31 20:13:50.487495
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():    data = {
        'name': 'Test Handler',
        'listen': 'test_event'
    }

# Generated at 2024-05-31 20:13:52.756081
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():    data = {'name': 'Test Handler', 'listen': 'test_event'}

# Generated at 2024-05-31 20:16:17.857964
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():    block = "test_block"

# Generated at 2024-05-31 20:16:19.601541
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    block = "test_block"
    role = "test_role"
    task_include = "test_task_include"
    handler_task_include = HandlerTaskInclude(block=block, role=role, task_include=task_include)
    
    assert handler_task_include.block == block
    assert handler_task_include.role == role
    assert handler_task_include.task_include == task_include

# Generated at 2024-05-31 20:16:22.550518
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():    data = {
        'name': 'Test Handler',
        'listen': 'test_event',
        'action': 'debug',
    }

# Generated at 2024-05-31 20:16:25.130871
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    data = {
        'name': 'Test Handler',
        'listen': 'test_event',
        'action': 'debug',
        'args': {'msg': 'This is a test'}
    }
    block = None
    role = None
    task_include = None
    variable_manager = None
    loader = None

    handler = HandlerTaskInclude.load(data, block, role, task_include, variable_manager, loader)

    assert handler.name == 'Test Handler'
    assert handler.listen == 'test_event'
    assert handler.action == 'debug'
    assert handler.args == {'msg': 'This is a test'}

# Generated at 2024-05-31 20:16:27.540512
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    data = {
        'name': 'Test Handler',
        'listen': 'test_event',
        'action': 'debug',
    }
    block = None
    role = None
    task_include = None
    variable_manager = None
    loader = None

    handler = HandlerTaskInclude.load(data, block, role, task_include, variable_manager, loader)

    assert handler is not None
    assert handler.get_name() == 'Test Handler'
    assert handler.listen == 'test_event'
    assert handler.action == 'debug'

# Generated at 2024-05-31 20:16:29.685158
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():    data = {'name': 'Test Handler', 'listen': 'test_event'}

# Generated at 2024-05-31 20:16:31.169141
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    handler_task_include = HandlerTaskInclude()
    assert isinstance(handler_task_include, HandlerTaskInclude)
    assert isinstance(handler_task_include, Handler)
    assert isinstance(handler_task_include, TaskInclude)
    assert 'listen' in handler_task_include.VALID_INCLUDE_KEYWORDS

# Generated at 2024-05-31 20:16:33.684770
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():    data = {
        'name': 'Test Handler',
        'listen': 'test_event'
    }

# Generated at 2024-05-31 20:16:35.204215
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    block = "test_block"
    role = "test_role"
    task_include = "test_task_include"
    handler_task_include = HandlerTaskInclude(block=block, role=role, task_include=task_include)
    
    assert handler_task_include.block == block
    assert handler_task_include.role == role
    assert handler_task_include.task_include == task_include

# Generated at 2024-05-31 20:16:38.285478
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():    data = {'name': 'Test Handler', 'listen': 'test_event'}