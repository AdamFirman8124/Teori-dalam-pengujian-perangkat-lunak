

# Generated at 2024-05-31 22:32:43.207934
# Unit test for method preprocess_data of class Task
def test_Task_preprocess_data():    task = Task()

# Generated at 2024-05-31 22:32:46.431747
# Unit test for method deserialize of class Task
def test_Task_deserialize():    task_data = {
        'parent': {
            'parent_type': 'Block',
            'parent': None,
            'role': None,
            'implicit': False,
            'resolved_action': None
        },
        'role': {
            'name': 'test_role',
            'path': '/path/to/role'
        },
        'implicit': True,
        'resolved_action': 'test_action'
    }


# Generated at 2024-05-31 22:32:48.687264
# Unit test for method get_include_params of class Task
def test_Task_get_include_params():    task = Task()

# Generated at 2024-05-31 22:32:50.243198
# Unit test for method post_validate of class Task
def test_Task_post_validate():    templar = Mock()

# Generated at 2024-05-31 22:32:52.656960
# Unit test for method preprocess_data of class Task
def test_Task_preprocess_data():    task = Task()

# Generated at 2024-05-31 22:32:56.235146
# Unit test for method preprocess_data of class Task
def test_Task_preprocess_data():    task = Task()

# Generated at 2024-05-31 22:32:59.477787
# Unit test for method preprocess_data of class Task
def test_Task_preprocess_data():    task = Task()

# Generated at 2024-05-31 22:33:00.449025
# Unit test for method __repr__ of class Task
def test_Task___repr__():    task = Task()

# Generated at 2024-05-31 22:33:03.050887
# Unit test for method deserialize of class Task
def test_Task_deserialize():    task_data = {
        'parent': {
            'parent_type': 'Block',
            'parent': None,
            'role': None,
            'implicit': False,
            'resolved_action': None
        },
        'role': {
            'name': 'test_role',
            'path': '/path/to/role'
        },
        'implicit': True,
        'resolved_action': 'test_action'
    }


# Generated at 2024-05-31 22:33:05.649463
# Unit test for method preprocess_data of class Task
def test_Task_preprocess_data():    task = Task()

# Generated at 2024-05-31 22:33:38.018934
# Unit test for method get_name of class Task
def test_Task_get_name():    task = Task()

# Generated at 2024-05-31 22:33:41.790959
# Unit test for method preprocess_data of class Task
def test_Task_preprocess_data():    task = Task()

# Generated at 2024-05-31 22:33:45.494814
# Unit test for method serialize of class Task
def test_Task_serialize():    task = Task()

# Generated at 2024-05-31 22:33:49.232442
# Unit test for method get_first_parent_include of class Task
def test_Task_get_first_parent_include():    from ansible.playbook.task_include import TaskInclude

# Generated at 2024-05-31 22:33:52.599043
# Unit test for method preprocess_data of class Task
def test_Task_preprocess_data():    task = Task()

# Generated at 2024-05-31 22:33:56.742725
# Unit test for method preprocess_data of class Task
def test_Task_preprocess_data():    task = Task()

# Generated at 2024-05-31 22:34:00.058031
# Unit test for method deserialize of class Task
def test_Task_deserialize():    task_data = {
        'parent': {
            'parent_type': 'Block',
            'parent': None,
            'role': None,
            'implicit': False,
            'resolved_action': None
        },
        'role': {
            'name': 'test_role',
            'path': '/path/to/role'
        },
        'implicit': True,
        'resolved_action': 'test_action'
    }


# Generated at 2024-05-31 22:34:03.581388
# Unit test for method deserialize of class Task
def test_Task_deserialize():    task_data = {
        'parent': {
            'parent_type': 'Block',
            'parent': None,
            'role': None,
            'implicit': False,
            'resolved_action': None
        },
        'role': {
            'name': 'test_role',
            'path': '/path/to/role'
        },
        'implicit': True,
        'resolved_action': 'test_action'
    }


# Generated at 2024-05-31 22:34:05.869904
# Unit test for method post_validate of class Task
def test_Task_post_validate():    templar = Mock()

# Generated at 2024-05-31 22:34:08.334141
# Unit test for method get_vars of class Task
def test_Task_get_vars():    parent_task = Task()

# Generated at 2024-05-31 22:34:44.562612
# Unit test for method get_vars of class Task
def test_Task_get_vars():    task = Task()

# Generated at 2024-05-31 22:34:48.244414
# Unit test for method preprocess_data of class Task
def test_Task_preprocess_data():    task = Task()

# Generated at 2024-05-31 22:34:49.861223
# Unit test for method post_validate of class Task
def test_Task_post_validate():    templar = Mock()

# Generated at 2024-05-31 22:34:53.703464
# Unit test for method preprocess_data of class Task
def test_Task_preprocess_data():    task = Task()

# Generated at 2024-05-31 22:34:57.029980
# Unit test for method preprocess_data of class Task
def test_Task_preprocess_data():    task = Task()

# Generated at 2024-05-31 22:34:58.106163
# Unit test for method __repr__ of class Task
def test_Task___repr__():    task = Task()

# Generated at 2024-05-31 22:34:59.706478
# Unit test for method post_validate of class Task
def test_Task_post_validate():    templar = Mock()

# Generated at 2024-05-31 22:35:00.961857
# Unit test for method __repr__ of class Task
def test_Task___repr__():    task = Task()

# Generated at 2024-05-31 22:35:07.042040
# Unit test for method preprocess_data of class Task
def test_Task_preprocess_data():    task = Task()

# Generated at 2024-05-31 22:35:09.369671
# Unit test for method get_include_params of class Task
def test_Task_get_include_params():    task = Task()

# Generated at 2024-05-31 22:35:42.487435
# Unit test for method preprocess_data of class Task
def test_Task_preprocess_data():    task = Task()

# Generated at 2024-05-31 22:35:46.916707
# Unit test for method post_validate of class Task
def test_Task_post_validate():    # Create a mock templar object
    templar = Mock()

    # Create a Task object with a parent
    parent_task = Mock()
    task = Task()
    task._parent = parent_task

    # Call post_validate and check if parent's post_validate was called
    task.post_validate(templar)
    parent_task.post_validate.assert_called_once_with(templar)

    # Create a Task object without a parent
    task_no_parent = Task()

    # Call post_validate and check if it completes without errors
    try:
        task_no_parent.post_validate(templar)
        assert True
    except Exception as e:
        assert False, f"post_validate raised an exception: {e}"

    # Check if super's post_validate was called
    with patch.object(Task, 'post_validate', wraps=Task.post_validate) as mock_super_post_validate:
        task_no_parent.post_validate(templar)
        mock_super_post_validate.assert_called

# Generated at 2024-05-31 22:35:49.207541
# Unit test for method get_include_params of class Task
def test_Task_get_include_params():    parent_task = Task()

# Generated at 2024-05-31 22:35:51.963943
# Unit test for method deserialize of class Task
def test_Task_deserialize():    task_data = {
        'parent': {
            'parent_type': 'Block',
            'parent': None,
            'role': None,
            'implicit': False,
            'resolved_action': None
        },
        'role': {
            'name': 'test_role',
            'path': '/path/to/role'
        },
        'implicit': True,
        'resolved_action': 'test_action'
    }


# Generated at 2024-05-31 22:35:55.039691
# Unit test for method preprocess_data of class Task
def test_Task_preprocess_data():    task = Task()

# Generated at 2024-05-31 22:35:57.090451
# Unit test for method get_vars of class Task
def test_Task_get_vars():    parent_task = Task()

# Generated at 2024-05-31 22:36:00.608207
# Unit test for method deserialize of class Task
def test_Task_deserialize():    task_data = {
        'parent': {
            'parent_type': 'Block',
            'parent': None,
            'role': None,
            'implicit': False,
            'resolved_action': None
        },
        'role': {
            'name': 'test_role',
            'path': '/path/to/role'
        },
        'implicit': True,
        'resolved_action': 'test_action'
    }


# Generated at 2024-05-31 22:36:02.792134
# Unit test for method get_include_params of class Task
def test_Task_get_include_params():    parent_task = Task()

# Generated at 2024-05-31 22:36:04.438454
# Unit test for method post_validate of class Task
def test_Task_post_validate():    templar = Mock()

# Generated at 2024-05-31 22:36:05.319088
# Unit test for method get_name of class Task
def test_Task_get_name():    task = Task()

# Generated at 2024-05-31 22:37:15.236633
# Unit test for method preprocess_data of class Task
def test_Task_preprocess_data():    task = Task()

# Generated at 2024-05-31 22:37:21.302353
# Unit test for method preprocess_data of class Task
def test_Task_preprocess_data():    task = Task()

# Generated at 2024-05-31 22:37:24.867710
# Unit test for method preprocess_data of class Task
def test_Task_preprocess_data():    task = Task()

# Generated at 2024-05-31 22:37:26.106988
# Unit test for method __repr__ of class Task
def test_Task___repr__():    task = Task()

# Generated at 2024-05-31 22:37:28.744550
# Unit test for method preprocess_data of class Task
def test_Task_preprocess_data():    task = Task()

# Generated at 2024-05-31 22:37:31.621876
# Unit test for method get_first_parent_include of class Task
def test_Task_get_first_parent_include():    from ansible.playbook.task_include import TaskInclude

# Generated at 2024-05-31 22:37:35.296940
# Unit test for method preprocess_data of class Task
def test_Task_preprocess_data():    task = Task()

# Generated at 2024-05-31 22:37:36.190721
# Unit test for method __repr__ of class Task
def test_Task___repr__():    task = Task()

# Generated at 2024-05-31 22:37:38.083074
# Unit test for method serialize of class Task
def test_Task_serialize():    task = Task()

# Generated at 2024-05-31 22:37:41.024530
# Unit test for method deserialize of class Task
def test_Task_deserialize():    task_data = {
        'parent': {
            'parent_type': 'Block',
            'parent': None,
            'role': None,
            'implicit': False,
            'resolved_action': None
        },
        'role': {
            'name': 'test_role',
            'path': '/path/to/role'
        },
        'implicit': True,
        'resolved_action': 'test_action'
    }


# Generated at 2024-05-31 22:39:57.726254
# Unit test for method get_name of class Task
def test_Task_get_name():    task = Task()

# Generated at 2024-05-31 22:39:59.554649
# Unit test for method get_vars of class Task
def test_Task_get_vars():    parent_task = Task()

# Generated at 2024-05-31 22:40:03.190794
# Unit test for method deserialize of class Task
def test_Task_deserialize():    task_data = {
        'parent': {
            'parent_type': 'Block',
            'parent': None,
            'role': None,
            'implicit': False,
            'resolved_action': None
        },
        'role': {
            'name': 'test_role',
            'path': '/path/to/role'
        },
        'implicit': True,
        'resolved_action': 'test_action'
    }


# Generated at 2024-05-31 22:40:04.302712
# Unit test for method __repr__ of class Task
def test_Task___repr__():    task = Task()

# Generated at 2024-05-31 22:40:07.872683
# Unit test for method preprocess_data of class Task
def test_Task_preprocess_data():    task = Task()

# Generated at 2024-05-31 22:40:09.248408
# Unit test for method get_name of class Task
def test_Task_get_name():    task = Task()

# Generated at 2024-05-31 22:40:10.148937
# Unit test for method get_name of class Task
def test_Task_get_name():    task = Task()

# Generated at 2024-05-31 22:40:12.730038
# Unit test for method preprocess_data of class Task
def test_Task_preprocess_data():    task = Task()

# Generated at 2024-05-31 22:40:17.660669
# Unit test for method post_validate of class Task
def test_Task_post_validate():    task = Task()

# Generated at 2024-05-31 22:40:20.506023
# Unit test for method deserialize of class Task
def test_Task_deserialize():    task_data = {
        'parent': {
            'parent_type': 'Block',
            'parent': None,
            'role': None,
            'implicit': False,
            'resolved_action': None
        },
        'role': {
            'name': 'test_role',
            'path': '/path/to/role'
        },
        'implicit': True,
        'resolved_action': 'test_action'
    }


# Generated at 2024-05-31 22:42:15.121194
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():    task_include = TaskInclude()

# Generated at 2024-05-31 22:42:18.736633
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():    task_include = TaskInclude()

# Generated at 2024-05-31 22:42:21.257633
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():    # Create a TaskInclude instance with mock arguments
    task_include = TaskInclude(block=None, role=None, task_include=None)
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


# Generated at 2024-05-31 22:42:26.283760
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


# Generated at 2024-05-31 22:42:28.803120
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():    task_include = TaskInclude()

# Generated at 2024-05-31 22:42:31.986788
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():    task_include = TaskInclude()

# Generated at 2024-05-31 22:42:35.060141
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():    task_include = TaskInclude()

# Generated at 2024-05-31 22:42:38.420656
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():    task_include = TaskInclude()

# Generated at 2024-05-31 22:42:41.144848
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():    task_include = TaskInclude()

# Generated at 2024-05-31 22:42:44.055572
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


# Generated at 2024-05-31 22:42:56.563562
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


# Generated at 2024-05-31 22:42:59.582355
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():    task_include = TaskInclude()

# Generated at 2024-05-31 22:43:01.322660
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():    task_include = TaskInclude()

# Generated at 2024-05-31 22:43:04.692327
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():    task_include = TaskInclude()

# Generated at 2024-05-31 22:43:06.882011
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():    task_include = TaskInclude()

# Generated at 2024-05-31 22:43:09.311808
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

# Generated at 2024-05-31 22:43:12.283538
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():    task_include = TaskInclude()

# Generated at 2024-05-31 22:43:15.706331
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():    task_include = TaskInclude()

# Generated at 2024-05-31 22:43:19.057552
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():    task_include = TaskInclude()

# Generated at 2024-05-31 22:43:22.624970
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():    task_include = TaskInclude()

# Generated at 2024-05-31 22:43:45.313959
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():    task_include = TaskInclude()

# Generated at 2024-05-31 22:43:50.036390
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():    task_include = TaskInclude()

# Generated at 2024-05-31 22:43:52.874668
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():    task_include = TaskInclude()

# Generated at 2024-05-31 22:43:55.234047
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

# Generated at 2024-05-31 22:43:59.075329
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():    task_include = TaskInclude()

# Generated at 2024-05-31 22:44:01.818041
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():    task_include = TaskInclude()

# Generated at 2024-05-31 22:44:03.941090
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():    task_include = TaskInclude()

# Generated at 2024-05-31 22:44:07.191975
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():    task_include = TaskInclude()

# Generated at 2024-05-31 22:44:09.752328
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():    task_include = TaskInclude()

# Generated at 2024-05-31 22:44:14.049176
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():    task_include = TaskInclude()

# Generated at 2024-05-31 22:44:55.985826
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():    # Create a TaskInclude instance with mock arguments
    task_include = TaskInclude(block=None, role=None, task_include=None)
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


# Generated at 2024-05-31 22:44:58.847142
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():    task_include = TaskInclude()

# Generated at 2024-05-31 22:45:01.687713
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


# Generated at 2024-05-31 22:45:03.977449
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():    task_include = TaskInclude()

# Generated at 2024-05-31 22:45:06.774834
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


# Generated at 2024-05-31 22:45:09.065674
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():    task_include = TaskInclude()

# Generated at 2024-05-31 22:45:11.157163
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

# Generated at 2024-05-31 22:45:14.092254
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():    task_include = TaskInclude()

# Generated at 2024-05-31 22:45:17.618026
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():    task_include = TaskInclude()

# Generated at 2024-05-31 22:45:19.562717
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():    task_include = TaskInclude()

# Generated at 2024-05-31 22:46:41.370960
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():    task_data = {
        'action': 'include',
        'args': {
            'file': 'some_file.yml',
            'apply': {'some_key': 'some_value'}
        }
    }

# Generated at 2024-05-31 22:46:43.545627
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():    task_include = TaskInclude()

# Generated at 2024-05-31 22:46:47.093479
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():    task_include = TaskInclude()

# Generated at 2024-05-31 22:46:50.795144
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():    task_include = TaskInclude()

# Generated at 2024-05-31 22:46:54.707104
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():    task_include = TaskInclude()

# Generated at 2024-05-31 22:46:57.945503
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():    task_include = TaskInclude()

# Generated at 2024-05-31 22:47:03.723755
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():    task_include = TaskInclude()

# Generated at 2024-05-31 22:47:07.095199
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():    task_include = TaskInclude()

# Generated at 2024-05-31 22:47:10.807558
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():    task_include = TaskInclude()

# Generated at 2024-05-31 22:47:14.133556
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():    task_include = TaskInclude()

# Generated at 2024-05-31 22:49:53.134979
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():    task_include = TaskInclude()

# Generated at 2024-05-31 22:49:56.580222
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():    task_include = TaskInclude()

# Generated at 2024-05-31 22:49:59.409871
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


# Generated at 2024-05-31 22:50:02.558991
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

    assert task.action == 'include'
    assert task.args['_raw_params'] == 'test_file.yml'
    assert task.block == block
    assert task.role == role
    assert task.task_include == task_include

# Generated at 2024-05-31 22:50:06.109101
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

    assert task.action == 'include'
    assert task.args['_raw_params'] == 'test_file.yml'
    assert task.block == block
    assert task.role == role
    assert task.task_include == task_include

# Generated at 2024-05-31 22:50:08.445407
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():    task_include = TaskInclude()

# Generated at 2024-05-31 22:50:10.392220
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():    task_include = TaskInclude()

# Generated at 2024-05-31 22:50:14.101578
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():    task_include = TaskInclude()

# Generated at 2024-05-31 22:50:17.938524
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():    task_include = TaskInclude()

# Generated at 2024-05-31 22:50:20.684343
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