

# Generated at 2024-05-31 22:52:22.503522
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():    task_include = TaskInclude()

# Generated at 2024-05-31 22:52:26.363578
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():    task_include = TaskInclude()

# Generated at 2024-05-31 22:52:32.008774
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():    # Create a TaskInclude instance with mock arguments
    task_include = TaskInclude()
    task_include.args = {'apply': {'some_key': 'some_value'}}
    task_include._parent = None
    task_include._role = None
    task_include._variable_manager = None
    task_include._loader = None

    # Call the method
    parent_block = task_include.build_parent_block()

    # Assertions to verify the behavior
    assert isinstance(parent_block, Block)
    assert 'some_key' in parent_block.args
    assert parent_block.args['some_key'] == 'some_value'
    assert 'block' in parent_block.args
    assert isinstance(parent_block.args['block'], list)


# Generated at 2024-05-31 22:52:36.931945
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():    task_include = TaskInclude()

# Generated at 2024-05-31 22:52:40.686819
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():    task_include = TaskInclude()

# Generated at 2024-05-31 22:52:43.638649
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():    # Create a TaskInclude instance with mock arguments
    task_include = TaskInclude()
    task_include.args = {'apply': {'some_key': 'some_value'}}
    task_include._parent = None
    task_include._role = None
    task_include._variable_manager = None
    task_include._loader = None

    # Call the method
    parent_block = task_include.build_parent_block()

    # Assertions to verify the behavior
    assert isinstance(parent_block, Block)
    assert 'some_key' in parent_block.args
    assert parent_block.args['some_key'] == 'some_value'
    assert 'block' in parent_block.args
    assert isinstance(parent_block.args['block'], list)


# Generated at 2024-05-31 22:52:46.058938
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():    task_include = TaskInclude()

# Generated at 2024-05-31 22:52:51.014805
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():    task_include = TaskInclude()

# Generated at 2024-05-31 22:52:53.862114
# Unit test for method load of class TaskInclude
def test_TaskInclude_load():    data = {
        'action': 'include',
        'file': 'some_file.yml',
        'apply': {'some_key': 'some_value'}
    }

# Generated at 2024-05-31 22:52:55.925447
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():    task_include = TaskInclude()

# Generated at 2024-05-31 22:53:02.845536
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():    task_include = TaskInclude()

# Generated at 2024-05-31 22:53:07.976199
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():    task_include = TaskInclude()

# Generated at 2024-05-31 22:53:09.828663
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():    task_include = TaskInclude()

# Generated at 2024-05-31 22:53:13.788220
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():    task_include = TaskInclude()

# Generated at 2024-05-31 22:53:16.409000
# Unit test for method load of class TaskInclude
def test_TaskInclude_load():
    data = {
        'action': 'include',
        'args': {
            'file': 'test_file.yml'
        }
    }
    block = Block()
    role = None
    task_include = None
    variable_manager = None
    loader = None

    task = TaskInclude.load(data, block=block, role=role, task_include=task_include, variable_manager=variable_manager, loader=loader)

    assert task.action == 'include'
    assert task.args['_raw_params'] == 'test_file.yml'
    assert task.args.get('file') is None

# Generated at 2024-05-31 22:53:22.412557
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():    task_data = {
        'action': 'include',
        'args': {
            'file': 'some_file.yml',
            'apply': {'some_key': 'some_value'}
        }
    }

# Generated at 2024-05-31 22:53:24.803347
# Unit test for method load of class TaskInclude
def test_TaskInclude_load():    data = {
        'action': 'include',
        'args': {
            'file': 'test_file.yml'
        }
    }

# Generated at 2024-05-31 22:53:27.040275
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():    task_include = TaskInclude()

# Generated at 2024-05-31 22:53:30.283729
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():    # Create a TaskInclude instance with mock arguments
    task_include = TaskInclude()
    task_include.args = {'apply': {'some_key': 'some_value'}}
    task_include._parent = None
    task_include._role = None
    task_include._variable_manager = None
    task_include._loader = None

    # Call the method
    parent_block = task_include.build_parent_block()

    # Assertions to verify the behavior
    assert isinstance(parent_block, Block)
    assert 'some_key' in parent_block.args
    assert parent_block.args['some_key'] == 'some_value'
    assert 'block' in parent_block.args
    assert isinstance(parent_block.args['block'], list)


# Generated at 2024-05-31 22:53:35.741064
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():    task_data = {
        'action': 'include',
        'args': {
            'file': 'some_file.yml',
            'apply': {'some_key': 'some_value'}
        }
    }

# Generated at 2024-05-31 22:53:49.067741
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():    task_include = TaskInclude()

# Generated at 2024-05-31 22:53:52.075261
# Unit test for method load of class TaskInclude
def test_TaskInclude_load():
    data = {
        'action': 'include',
        'file': 'test_file.yml'
    }
    block = Block()
    role = None
    task_include = None
    variable_manager = None
    loader = None

    task = TaskInclude.load(data, block=block, role=role, task_include=task_include, variable_manager=variable_manager, loader=loader)

    assert task.args['_raw_params'] == 'test_file.yml'
    assert task.action == 'include'
    assert isinstance(task, TaskInclude)

# Generated at 2024-05-31 22:53:57.207095
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():    task_include = TaskInclude()

# Generated at 2024-05-31 22:53:59.543392
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():    task_include = TaskInclude()

# Generated at 2024-05-31 22:54:03.462336
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():    task_include = TaskInclude()

# Generated at 2024-05-31 22:54:09.966776
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():    task_data = {
        'action': 'include',
        'args': {
            'file': 'some_file.yml',
            'apply': {'some_key': 'some_value'}
        }
    }

# Generated at 2024-05-31 22:54:13.333610
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():    task_include = TaskInclude()

# Generated at 2024-05-31 22:54:17.315270
# Unit test for method load of class TaskInclude
def test_TaskInclude_load():    data = {
        'action': 'include',
        'file': 'some_file.yml',
        'apply': {'some_key': 'some_value'}
    }

# Generated at 2024-05-31 22:54:19.999413
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():    # Create a TaskInclude instance with mock data
    task_include = TaskInclude()
    task_include.args = {'apply': {'some_key': 'some_value'}}
    task_include._parent = None
    task_include._role = None
    task_include._variable_manager = None
    task_include._loader = None

    # Call the method
    parent_block = task_include.build_parent_block()

    # Assertions to verify the behavior
    assert isinstance(parent_block, Block)
    assert 'some_key' in parent_block.args
    assert parent_block.args['some_key'] == 'some_value'
    assert 'block' in parent_block.args
    assert isinstance(parent_block.args['block'], list)


# Generated at 2024-05-31 22:54:22.575325
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():    task_include = TaskInclude()

# Generated at 2024-05-31 22:54:46.351308
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():    task_include = TaskInclude()

# Generated at 2024-05-31 22:54:49.534788
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():    task_include = TaskInclude()

# Generated at 2024-05-31 22:54:51.467793
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():    task_include = TaskInclude()

# Generated at 2024-05-31 22:54:53.485637
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():    task_include = TaskInclude()

# Generated at 2024-05-31 22:54:57.701495
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():    task_data = {
        'action': 'include',
        'args': {
            'file': 'some_file.yml',
            'apply': {'some_key': 'some_value'}
        }
    }

# Generated at 2024-05-31 22:55:01.343291
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():    task_include = TaskInclude()

# Generated at 2024-05-31 22:55:04.245164
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():    task_include = TaskInclude()

# Generated at 2024-05-31 22:55:05.998404
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():    task_include = TaskInclude()

# Generated at 2024-05-31 22:55:08.379267
# Unit test for method load of class TaskInclude
def test_TaskInclude_load():
    data = {
        'action': 'include',
        'file': 'test_file.yml',
        'apply': {'some_key': 'some_value'}
    }
    block = Block()
    role = None
    task_include = None
    variable_manager = None
    loader = None

    task = TaskInclude.load(data, block=block, role=role, task_include=task_include, variable_manager=variable_manager, loader=loader)

    assert task.action == 'include'
    assert task.args['_raw_params'] == 'test_file.yml'
    assert task.args['apply'] == {'some_key': 'some_value'}
    assert isinstance(task, TaskInclude)

# Generated at 2024-05-31 22:55:12.338279
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():    task_include = TaskInclude()

# Generated at 2024-05-31 22:55:33.422523
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():    task_include = TaskInclude()

# Generated at 2024-05-31 22:55:36.663065
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():    task_include = TaskInclude()

# Generated at 2024-05-31 22:55:39.424688
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():    task_include = TaskInclude()

# Generated at 2024-05-31 22:55:42.329207
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():    task_include = TaskInclude()

# Generated at 2024-05-31 22:55:48.605125
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():    task_include = TaskInclude()

# Generated at 2024-05-31 22:55:52.043687
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():    task_include = TaskInclude()

# Generated at 2024-05-31 22:55:53.979103
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():    task_include = TaskInclude()

# Generated at 2024-05-31 22:55:56.502191
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():    task_include = TaskInclude()

# Generated at 2024-05-31 22:55:58.941635
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():    task_include = TaskInclude()

# Generated at 2024-05-31 22:56:00.560831
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():    task_include = TaskInclude()

# Generated at 2024-05-31 22:56:41.041349
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():    task_include = TaskInclude()

# Generated at 2024-05-31 22:56:43.715021
# Unit test for method load of class TaskInclude
def test_TaskInclude_load():
    data = {
        'action': 'include',
        'file': 'test_file.yml'
    }
    block = Block()
    role = None
    task_include = None
    variable_manager = None
    loader = None

    task = TaskInclude.load(data, block=block, role=role, task_include=task_include, variable_manager=variable_manager, loader=loader)

    assert task.args['_raw_params'] == 'test_file.yml'
    assert task.action == 'include'
    assert isinstance(task, TaskInclude)

# Generated at 2024-05-31 22:56:46.676952
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():    task_include = TaskInclude()

# Generated at 2024-05-31 22:56:49.018043
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():    task_include = TaskInclude()

# Generated at 2024-05-31 22:56:52.275297
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():    task_include = TaskInclude()

# Generated at 2024-05-31 22:56:54.550535
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():    task_include = TaskInclude()

# Generated at 2024-05-31 22:56:56.261998
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():    task_include = TaskInclude()

# Generated at 2024-05-31 22:56:58.063302
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():    task_include = TaskInclude()

# Generated at 2024-05-31 22:57:00.606199
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():    task_include = TaskInclude()

# Generated at 2024-05-31 22:57:04.383162
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():    task_include = TaskInclude()

# Generated at 2024-05-31 22:58:18.653363
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():    task_include = TaskInclude()

# Generated at 2024-05-31 22:58:22.059595
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():    task_include = TaskInclude()

# Generated at 2024-05-31 22:58:23.872642
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():    task_include = TaskInclude()

# Generated at 2024-05-31 22:58:27.004673
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():    task_include = TaskInclude()

# Generated at 2024-05-31 22:58:31.335199
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():    task_include = TaskInclude()

# Generated at 2024-05-31 22:58:36.251892
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():    task_include = TaskInclude()

# Generated at 2024-05-31 22:58:38.522486
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():    task_include = TaskInclude()

# Generated at 2024-05-31 22:58:40.663856
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():    task_include = TaskInclude()

# Generated at 2024-05-31 22:58:42.595495
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():    task_include = TaskInclude()

# Generated at 2024-05-31 22:58:44.991793
# Unit test for method load of class TaskInclude
def test_TaskInclude_load():
    data = {
        'action': 'include',
        'file': 'test_file.yml',
        'apply': {'some_key': 'some_value'}
    }
    block = Block()
    role = None
    task_include = None
    variable_manager = None
    loader = None

    task = TaskInclude.load(data, block=block, role=role, task_include=task_include, variable_manager=variable_manager, loader=loader)

    assert task.args['_raw_params'] == 'test_file.yml'
    assert task.args['apply'] == {'some_key': 'some_value'}
    assert task.action == 'include'

# Generated at 2024-05-31 23:01:12.060722
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():    task_include = TaskInclude()

# Generated at 2024-05-31 23:01:14.901034
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():    task_include = TaskInclude()

# Generated at 2024-05-31 23:01:21.009209
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():    task_include = TaskInclude()

# Generated at 2024-05-31 23:01:23.676383
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():    task_include = TaskInclude()

# Generated at 2024-05-31 23:01:25.618573
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():    task_include = TaskInclude()

# Generated at 2024-05-31 23:01:28.700487
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():    task_include = TaskInclude()

# Generated at 2024-05-31 23:01:30.340835
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():    task_include = TaskInclude()

# Generated at 2024-05-31 23:01:32.312601
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():    task_include = TaskInclude()

# Generated at 2024-05-31 23:01:34.854695
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():    # Create a TaskInclude instance with mock data
    task_include = TaskInclude()
    task_include.args = {'apply': {'some_key': 'some_value'}}
    task_include._parent = None
    task_include._role = None
    task_include._variable_manager = None
    task_include._loader = None

    # Call the method
    parent_block = task_include.build_parent_block()

    # Assertions to verify the behavior
    assert isinstance(parent_block, Block)
    assert 'some_key' in parent_block.args
    assert parent_block.args['some_key'] == 'some_value'
    assert 'block' in parent_block.args
    assert isinstance(parent_block.args['block'], list)


# Generated at 2024-05-31 23:01:36.886046
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():    task_include = TaskInclude()