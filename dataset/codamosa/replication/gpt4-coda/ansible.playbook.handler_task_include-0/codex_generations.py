

# Generated at 2024-03-18 02:49:49.516953
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():    # Given
    mock_block = None
    mock_role = None
    mock_task_include = None
    mock_variable_manager = None
    mock_loader = None

    # When
    handler_task_include = HandlerTaskInclude.load(
        data={},
        block=mock_block,
        role=mock_role,
        task_include=mock_task_include,
        variable_manager=mock_variable_manager,
        loader=mock_loader
    )

    # Then
    assert isinstance(handler_task_include, HandlerTaskInclude)
    assert handler_task_include.block is mock_block
    assert handler_task_include.role is mock_role
    assert handler_task_include.task_include is mock_task_include
    assert handler_task_include._variable_manager is mock_variable_manager
    assert handler_task_include._loader is mock_loader


# Generated at 2024-03-18 02:49:57.230547
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():    # Mocking the necessary objects and inputs
    mock_data = {'name': 'include_task', 'listen': 'event_name'}
    mock_block = None
    mock_role = None
    mock_task_include = None
    mock_variable_manager = None
    mock_loader = None

    # Call the method
    handler = HandlerTaskInclude.load(
        data=mock_data,
        block=mock_block,
        role=mock_role,
        task_include=mock_task_include,
        variable_manager=mock_variable_manager,
        loader=mock_loader
    )

    # Assertions to validate the behavior of the method
    assert isinstance(handler, HandlerTaskInclude), "The returned object should be an instance of HandlerTaskInclude"
    assert handler.name == 'include_task', "The name attribute should be set to 'include_task'"
    assert handler.listen == 'event_name', "The listen attribute should be set to 'event_name'"

# Generated at 2024-03-18 02:50:07.125208
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():    # Mocking the necessary components for the test
    mock_data = {'name': 'test_handler', 'listen': 'test_event'}
    mock_block = None
    mock_role = None
    mock_task_include = None
    mock_variable_manager = None
    mock_loader = None

    # Call the method we're testing
    handler = HandlerTaskInclude.load(
        data=mock_data,
        block=mock_block,
        role=mock_role,
        task_include=mock_task_include,
        variable_manager=mock_variable_manager,
        loader=mock_loader
    )

    # Assertions to validate the behavior of the method
    assert isinstance(handler, HandlerTaskInclude), "The returned object should be an instance of HandlerTaskInclude"
    assert handler.listen == 'test_event', "The 'listen' attribute should be set to 'test_event'"

# Generated at 2024-03-18 02:50:13.295311
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():    # Mocking the necessary components for the test
    mock_data = {'listen': 'my_event', 'name': 'include_task.yml'}
    mock_block = None
    mock_role = None
    mock_task_include = None
    mock_variable_manager = None
    mock_loader = None

    # Call the method we are testing
    handler = HandlerTaskInclude.load(
        data=mock_data,
        block=mock_block,
        role=mock_role,
        task_include=mock_task_include,
        variable_manager=mock_variable_manager,
        loader=mock_loader
    )

    # Assertions to validate the behavior of the method
    assert isinstance(handler, HandlerTaskInclude), "The returned object should be an instance of HandlerTaskInclude"
    assert handler.listen == 'my_event', "The 'listen' attribute should be set to 'my_event'"

# Generated at 2024-03-18 02:50:20.225462
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():    # Mocking the necessary objects and inputs for the test
    mock_data = {'listen': 'my_event', 'name': 'include_task.yml'}
    mock_block = None
    mock_role = None
    mock_task_include = None
    mock_variable_manager = None
    mock_loader = None

    # Call the method we are testing
    result = HandlerTaskInclude.load(
        data=mock_data,
        block=mock_block,
        role=mock_role,
        task_include=mock_task_include,
        variable_manager=mock_variable_manager,
        loader=mock_loader
    )

    # Assertions to validate the expected outcomes
    assert isinstance(result, HandlerTaskInclude), "Result should be an instance of HandlerTaskInclude"
    assert result.listen == 'my_event', "Handler should have 'listen' attribute set to 'my_event'"

# Generated at 2024-03-18 02:50:26.185711
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():    # Mocking the necessary components for the test
    mock_data = {'listen': 'my_event', 'name': 'include_task.yml'}
    mock_block = None
    mock_role = None
    mock_task_include = None
    mock_variable_manager = None
    mock_loader = None

    # Call the method we're testing
    handler = HandlerTaskInclude.load(
        data=mock_data,
        block=mock_block,
        role=mock_role,
        task_include=mock_task_include,
        variable_manager=mock_variable_manager,
        loader=mock_loader
    )

    # Assertions to validate the behavior of the method
    assert isinstance(handler, HandlerTaskInclude), "The returned object should be an instance of HandlerTaskInclude"
    assert handler.listen == 'my_event', "The 'listen' attribute should be set to 'my_event'"

# Generated at 2024-03-18 02:50:32.640226
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():    # Mocking the necessary components for the test
    mock_data = {'listen': 'my_event', 'name': 'include_task.yml'}
    mock_block = None
    mock_role = None
    mock_task_include = None
    mock_variable_manager = None
    mock_loader = None

    # Call the method we're testing
    handler = HandlerTaskInclude.load(
        data=mock_data,
        block=mock_block,
        role=mock_role,
        task_include=mock_task_include,
        variable_manager=mock_variable_manager,
        loader=mock_loader
    )

    # Assertions to validate the behavior of the method
    assert isinstance(handler, HandlerTaskInclude), "The returned object should be an instance of HandlerTaskInclude"
    assert handler.listen == 'my_event', "The 'listen' attribute should be set to 'my_event'"

# Generated at 2024-03-18 02:50:38.698164
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():    # Mocking the necessary objects and inputs for the test
    mock_data = {'listen': 'my_event', 'name': 'include_task.yml'}
    mock_block = None
    mock_role = None
    mock_task_include = None
    mock_variable_manager = None
    mock_loader = None

    # Call the method we're testing
    handler = HandlerTaskInclude.load(
        data=mock_data,
        block=mock_block,
        role=mock_role,
        task_include=mock_task_include,
        variable_manager=mock_variable_manager,
        loader=mock_loader
    )

    # Assertions to validate the behavior of the method
    assert isinstance(handler, HandlerTaskInclude), "The returned object should be an instance of HandlerTaskInclude"
    assert handler.listen == 'my_event', "The 'listen' attribute should be set to 'my_event'"

# Generated at 2024-03-18 02:50:47.017436
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():    # Mocking the necessary objects and inputs for the test
    mock_data = {'name': 'include_tasks', 'listen': 'my_event'}
    mock_block = None
    mock_role = None
    mock_task_include = None
    mock_variable_manager = None
    mock_loader = None

    # Call the method we're testing
    handler = HandlerTaskInclude.load(
        data=mock_data,
        block=mock_block,
        role=mock_role,
        task_include=mock_task_include,
        variable_manager=mock_variable_manager,
        loader=mock_loader
    )

    # Assertions to validate the behavior of the method
    assert isinstance(handler, HandlerTaskInclude), "The returned object should be an instance of HandlerTaskInclude"
    assert handler.listen == 'my_event', "The 'listen' attribute should be set to 'my_event'"

# Generated at 2024-03-18 02:50:52.652223
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():    # Mocking the necessary objects and inputs
    mock_data = {'name': 'include_task', 'listen': 'event_name'}
    mock_block = None
    mock_role = None
    mock_task_include = None
    mock_variable_manager = None
    mock_loader = None

    # Call the method
    handler = HandlerTaskInclude.load(
        data=mock_data,
        block=mock_block,
        role=mock_role,
        task_include=mock_task_include,
        variable_manager=mock_variable_manager,
        loader=mock_loader
    )

    # Assertions to validate the behavior of the method
    assert isinstance(handler, HandlerTaskInclude), "The returned object should be an instance of HandlerTaskInclude"
    assert handler.name == 'include_task', "The name attribute should be set to 'include_task'"
    assert handler.listen == 'event_name', "The listen attribute should be set to 'event_name'"


# Generated at 2024-03-18 02:51:02.961034
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():    # Given
    mock_block = None
    mock_role = None
    mock_task_include = None
    mock_variable_manager = None
    mock_loader = None
    mock_data = {'listen': 'my_event', 'name': 'include_task.yml'}

    # When
    handler_task_include = HandlerTaskInclude.load(
        data=mock_data,
        block=mock_block,
        role=mock_role,
        task_include=mock_task_include,
        variable_manager=mock_variable_manager,
        loader=mock_loader
    )

    # Then
    assert isinstance(handler_task_include, HandlerTaskInclude)
    assert handler_task_include.listen == 'my_event'
    assert handler_task_include.get_name() == 'include_task.yml'


# Generated at 2024-03-18 02:51:09.582033
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():    # Mocking the necessary components for the test
    mock_data = {'listen': 'my_event', 'name': 'include_task.yml'}
    mock_block = None
    mock_role = None
    mock_task_include = None
    mock_variable_manager = None
    mock_loader = None

    # Call the method we're testing
    handler = HandlerTaskInclude.load(
        data=mock_data,
        block=mock_block,
        role=mock_role,
        task_include=mock_task_include,
        variable_manager=mock_variable_manager,
        loader=mock_loader
    )

    # Assertions to validate the behavior of the method
    assert isinstance(handler, HandlerTaskInclude), "The returned object should be an instance of HandlerTaskInclude"
    assert handler.listen == 'my_event', "The 'listen' attribute should be set to 'my_event'"

# Generated at 2024-03-18 02:51:17.157012
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():    # Mocking the necessary components for the test
    mock_data = {'name': 'include_task', 'listen': 'event_name'}
    mock_block = object()
    mock_role = object()
    mock_task_include = object()
    mock_variable_manager = object()
    mock_loader = object()

    # Call the method we are testing
    handler = HandlerTaskInclude.load(
        data=mock_data,
        block=mock_block,
        role=mock_role,
        task_include=mock_task_include,
        variable_manager=mock_variable_manager,
        loader=mock_loader
    )

    # Assertions to validate the behavior of the method
    assert isinstance(handler, HandlerTaskInclude), "The returned object should be an instance of HandlerTaskInclude"
    assert handler.listen == 'event_name', "The 'listen' attribute should be set to 'event_name'"

# Generated at 2024-03-18 02:51:22.109949
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():    # Given
    mock_block = None
    mock_role = None
    mock_task_include = None
    mock_variable_manager = None
    mock_loader = None
    mock_data = {'name': 'test_handler', 'listen': 'test_event'}

    # When
    handler_task_include = HandlerTaskInclude.load(
        data=mock_data,
        block=mock_block,
        role=mock_role,
        task_include=mock_task_include,
        variable_manager=mock_variable_manager,
        loader=mock_loader
    )

    # Then
    assert isinstance(handler_task_include, HandlerTaskInclude)
    assert handler_task_include.get_name() == 'test_handler'
    assert handler_task_include.listen == 'test_event'


# Generated at 2024-03-18 02:51:27.285809
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():    # Given
    mock_block = None
    mock_role = None
    mock_task_include = None
    mock_variable_manager = None
    mock_loader = None
    mock_data = {'listen': 'my_event', 'name': 'include_task.yml'}

    # When
    handler_task_include = HandlerTaskInclude.load(
        data=mock_data,
        block=mock_block,
        role=mock_role,
        task_include=mock_task_include,
        variable_manager=mock_variable_manager,
        loader=mock_loader
    )

    # Then
    assert isinstance(handler_task_include, HandlerTaskInclude)
    assert handler_task_include.listen == 'my_event'
    assert handler_task_include.get_name() == 'include_task.yml'


# Generated at 2024-03-18 02:51:33.261602
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():    # Given
    fake_block = None
    fake_role = None
    fake_task_include = None
    fake_variable_manager = None
    fake_loader = None

    # When
    handler_task_include = HandlerTaskInclude.load(
        data={},
        block=fake_block,
        role=fake_role,
        task_include=fake_task_include,
        variable_manager=fake_variable_manager,
        loader=fake_loader
    )

    # Then
    assert isinstance(handler_task_include, HandlerTaskInclude)
    assert handler_task_include._block is fake_block
    assert handler_task_include._role is fake_role
    assert handler_task_include._task_include is fake_task_include
    assert handler_task_include._variable_manager is fake_variable_manager
    assert handler_task_include._loader is fake_loader


# Generated at 2024-03-18 02:51:37.964038
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():    # Given
    mock_block = None
    mock_role = None
    mock_task_include = None
    mock_variable_manager = None
    mock_loader = None
    mock_data = {'listen': 'event_name'}

    # When
    handler_task_include = HandlerTaskInclude.load(
        data=mock_data,
        block=mock_block,
        role=mock_role,
        task_include=mock_task_include,
        variable_manager=mock_variable_manager,
        loader=mock_loader
    )

    # Then
    assert isinstance(handler_task_include, HandlerTaskInclude)
    assert handler_task_include.listen == 'event_name'

# Generated at 2024-03-18 02:51:55.565024
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():    # Mocking the necessary objects and inputs
    mock_data = {'listen': 'my_event', 'name': 'include_task.yml'}
    mock_block = None
    mock_role = None
    mock_task_include = None
    mock_variable_manager = None
    mock_loader = None

    # Call the method
    handler = HandlerTaskInclude.load(
        data=mock_data,
        block=mock_block,
        role=mock_role,
        task_include=mock_task_include,
        variable_manager=mock_variable_manager,
        loader=mock_loader
    )

    # Assertions to validate the behavior of the method
    assert isinstance(handler, HandlerTaskInclude), "The returned object should be an instance of HandlerTaskInclude"
    assert handler.listen == 'my_event', "The 'listen' attribute should be set to 'my_event'"

# Generated at 2024-03-18 02:51:59.396325
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():    # Given
    mock_block = None
    mock_role = None
    mock_task_include = None
    mock_variable_manager = None
    mock_loader = None
    mock_data = {'listen': 'event_name'}

    # When
    handler_task_include = HandlerTaskInclude.load(
        data=mock_data,
        block=mock_block,
        role=mock_role,
        task_include=mock_task_include,
        variable_manager=mock_variable_manager,
        loader=mock_loader
    )

    # Then
    assert isinstance(handler_task_include, HandlerTaskInclude)
    assert handler_task_include.listen == 'event_name'


# Generated at 2024-03-18 02:52:11.055392
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():    # Mocking the necessary objects and inputs for the test
    mock_data = {'name': 'test_handler', 'listen': 'test_event'}
    mock_block = None
    mock_role = None
    mock_task_include = None
    mock_variable_manager = None
    mock_loader = None

    # Call the method we're testing
    handler = HandlerTaskInclude.load(
        data=mock_data,
        block=mock_block,
        role=mock_role,
        task_include=mock_task_include,
        variable_manager=mock_variable_manager,
        loader=mock_loader
    )

    # Assertions to validate the behavior of the method
    assert isinstance(handler, HandlerTaskInclude), "The returned object should be an instance of HandlerTaskInclude"
    assert handler.name == 'test_handler', "The handler name should be set to 'test_handler'"
    assert handler.listen == 'test_event', "The handler should listen to 'test_event'"


# Generated at 2024-03-18 02:52:26.581634
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():    # Create a mock block, role, task_include, variable_manager, and loader
    mock_block = None
    mock_role = None
    mock_task_include = None
    mock_variable_manager = None
    mock_loader = None

    # Create a sample data dictionary to simulate input
    sample_data = {
        'name': 'Include a task list',
        'include': 'some_task_file.yml',
        'listen': 'my_custom_event'
    }

    # Call the load method with the sample data and mocks
    handler = HandlerTaskInclude.load(
        data=sample_data,
        block=mock_block,
        role=mock_role,
        task_include=mock_task_include,
        variable_manager=mock_variable_manager,
        loader=mock_loader
    )

    # Assertions to check if the handler is correctly instantiated
    assert isinstance(handler, HandlerTaskInclude), "HandlerTaskInclude instance not created"

# Generated at 2024-03-18 02:52:33.025235
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():    # Mocking the necessary components for the test
    mock_data = {'name': 'include_task', 'listen': 'my_event'}
    mock_block = None
    mock_role = None
    mock_task_include = None
    mock_variable_manager = None
    mock_loader = None

    # Call the method we are testing
    handler = HandlerTaskInclude.load(
        mock_data,
        block=mock_block,
        role=mock_role,
        task_include=mock_task_include,
        variable_manager=mock_variable_manager,
        loader=mock_loader
    )

    # Assertions to validate the behavior of the method
    assert isinstance(handler, HandlerTaskInclude), "The returned object should be an instance of HandlerTaskInclude"
    assert handler.listen == 'my_event', "The 'listen' attribute should be set to 'my_event'"
    assert handler.name == 'include_task', "The 'name' attribute should be set to 'include_task'"


# Generated at 2024-03-18 02:52:41.772197
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():    # Given
    fake_loader = None
    fake_variable_manager = None
    fake_data = {'listen': 'my_event', 'name': 'Include Task'}
    fake_block = None
    fake_role = None
    fake_task_include = None

    # When
    handler_task_include = HandlerTaskInclude.load(
        data=fake_data,
        block=fake_block,
        role=fake_role,
        task_include=fake_task_include,
        variable_manager=fake_variable_manager,
        loader=fake_loader
    )

    # Then
    assert isinstance(handler_task_include, HandlerTaskInclude)
    assert handler_task_include.listen == 'my_event'
    assert handler_task_include.get_name() == 'Include Task'


# Generated at 2024-03-18 02:52:48.128437
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():    # Mocking the necessary components for the test
    mock_data = {'listen': 'my_event', 'name': 'include_task.yml'}
    mock_block = None
    mock_role = None
    mock_task_include = None
    mock_variable_manager = None
    mock_loader = None

    # Call the method we are testing
    handler = HandlerTaskInclude.load(
        data=mock_data,
        block=mock_block,
        role=mock_role,
        task_include=mock_task_include,
        variable_manager=mock_variable_manager,
        loader=mock_loader
    )

    # Assertions to validate the behavior of the method
    assert isinstance(handler, HandlerTaskInclude), "The returned object should be an instance of HandlerTaskInclude"
    assert handler.listen == 'my_event', "The 'listen' attribute should be set to 'my_event'"

# Generated at 2024-03-18 02:52:52.206086
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():    # Given
    mock_block = None
    mock_role = None
    mock_task_include = None
    mock_variable_manager = None
    mock_loader = None
    mock_data = {'listen': 'event_name'}

    # When
    handler_task_include = HandlerTaskInclude.load(
        data=mock_data,
        block=mock_block,
        role=mock_role,
        task_include=mock_task_include,
        variable_manager=mock_variable_manager,
        loader=mock_loader
    )

    # Then
    assert isinstance(handler_task_include, HandlerTaskInclude)
    assert handler_task_include.listen == 'event_name'


# Generated at 2024-03-18 02:52:59.379831
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():    # Mocking the necessary components for the test
    mock_data = {'listen': 'my_event', 'name': 'include_task.yml'}
    mock_block = None
    mock_role = None
    mock_task_include = None
    mock_variable_manager = None
    mock_loader = None

    # Call the method we're testing
    handler = HandlerTaskInclude.load(
        data=mock_data,
        block=mock_block,
        role=mock_role,
        task_include=mock_task_include,
        variable_manager=mock_variable_manager,
        loader=mock_loader
    )

    # Assertions to validate the behavior of the method
    assert isinstance(handler, HandlerTaskInclude), "The returned object should be an instance of HandlerTaskInclude"
    assert handler.listen == 'my_event', "The 'listen' attribute should be set to 'my_event'"

# Generated at 2024-03-18 02:53:04.266157
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():    # Given
    mock_block = None
    mock_role = None
    mock_task_include = None
    mock_variable_manager = None
    mock_loader = None
    mock_data = {'listen': 'my_event', 'name': 'include_task.yml'}

    # When
    handler_task_include = HandlerTaskInclude.load(
        data=mock_data,
        block=mock_block,
        role=mock_role,
        task_include=mock_task_include,
        variable_manager=mock_variable_manager,
        loader=mock_loader
    )

    # Then
    assert isinstance(handler_task_include, HandlerTaskInclude)
    assert handler_task_include.listen == 'my_event'
    assert handler_task_include.get_name() == 'include_task.yml'


# Generated at 2024-03-18 02:53:13.009048
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():    # Mocking the necessary objects and inputs for the test
    mock_data = {'name': 'include_task', 'listen': 'event_name'}
    mock_block = None
    mock_role = None
    mock_task_include = None
    mock_variable_manager = None
    mock_loader = None

    # Call the method we're testing
    result = HandlerTaskInclude.load(
        data=mock_data,
        block=mock_block,
        role=mock_role,
        task_include=mock_task_include,
        variable_manager=mock_variable_manager,
        loader=mock_loader
    )

    # Assertions to validate the behavior of the method
    assert isinstance(result, HandlerTaskInclude), "Result should be an instance of HandlerTaskInclude"
    assert result.listen == 'event_name', "Handler should have the correct 'listen' attribute set"
    assert result.name == 'include_task', "Handler should have the correct 'name' attribute set"


# Generated at 2024-03-18 02:53:19.838072
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():    # Mocking the necessary components for the test
    mock_data = {'name': 'include_task', 'listen': 'my_event'}
    mock_block = None
    mock_role = None
    mock_task_include = None
    mock_variable_manager = None
    mock_loader = None

    # Call the method we are testing
    handler = HandlerTaskInclude.load(
        data=mock_data,
        block=mock_block,
        role=mock_role,
        task_include=mock_task_include,
        variable_manager=mock_variable_manager,
        loader=mock_loader
    )

    # Assertions to validate the behavior of the method
    assert isinstance(handler, HandlerTaskInclude), "The returned object should be an instance of HandlerTaskInclude"
    assert handler.name == 'include_task', "The name attribute should be set to 'include_task'"
    assert handler.listen == 'my_event', "The listen attribute should be set to 'my_event'"


# Generated at 2024-03-18 02:53:27.425543
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():    # Given
    mock_block = None
    mock_role = None
    mock_task_include = None
    mock_variable_manager = None
    mock_loader = None
    mock_data = {'listen': 'event_name'}

    # When
    handler_task_include = HandlerTaskInclude.load(
        data=mock_data,
        block=mock_block,
        role=mock_role,
        task_include=mock_task_include,
        variable_manager=mock_variable_manager,
        loader=mock_loader
    )

    # Then
    assert isinstance(handler_task_include, HandlerTaskInclude)
    assert handler_task_include.listen == 'event_name'

# Generated at 2024-03-18 02:53:50.681269
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():    # Mocking the necessary components for the test
    mock_data = {'listen': 'my_event', 'name': 'include_task.yml'}
    mock_block = None
    mock_role = None
    mock_task_include = None
    mock_variable_manager = None
    mock_loader = None

    # Call the method we're testing
    handler = HandlerTaskInclude.load(
        data=mock_data,
        block=mock_block,
        role=mock_role,
        task_include=mock_task_include,
        variable_manager=mock_variable_manager,
        loader=mock_loader
    )

    # Assertions to validate the behavior of the method
    assert isinstance(handler, HandlerTaskInclude), "The returned object should be an instance of HandlerTaskInclude"
    assert handler.listen == 'my_event', "The 'listen' attribute should be set to 'my_event'"

# Generated at 2024-03-18 02:53:56.431398
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():    # Given
    mock_block = None
    mock_role = None
    mock_task_include = None
    mock_variable_manager = None
    mock_loader = None
    mock_data = {'name': 'include_task', 'listen': 'my_event'}

    # When
    handler_task_include = HandlerTaskInclude.load(
        data=mock_data,
        block=mock_block,
        role=mock_role,
        task_include=mock_task_include,
        variable_manager=mock_variable_manager,
        loader=mock_loader
    )

    # Then
    assert isinstance(handler_task_include, HandlerTaskInclude)
    assert handler_task_include.listen == 'my_event'
    assert handler_task_include.name == 'include_task'


# Generated at 2024-03-18 02:54:03.775760
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():    # Mocking the necessary components for the test
    mock_data = {'name': 'include_task', 'listen': 'event_name'}
    mock_block = object()
    mock_role = object()
    mock_task_include = object()
    mock_variable_manager = object()
    mock_loader = object()

    # Call the method we are testing
    handler = HandlerTaskInclude.load(
        data=mock_data,
        block=mock_block,
        role=mock_role,
        task_include=mock_task_include,
        variable_manager=mock_variable_manager,
        loader=mock_loader
    )

    # Assertions to validate the behavior of the method
    assert isinstance(handler, HandlerTaskInclude)
    assert handler.listen == 'event_name'
    assert handler.name == 'include_task'
    assert handler.block is mock_block
    assert handler.role is mock_role
    assert handler.task_include is mock_task_include
    assert handler._variable_manager is mock_variable_manager

# Generated at 2024-03-18 02:54:09.808424
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():    # Given
    mock_block = None
    mock_role = None
    mock_task_include = None
    mock_variable_manager = None
    mock_loader = None
    mock_data = {'listen': 'my_event', 'name': 'include_task.yml'}

    # When
    handler_task_include = HandlerTaskInclude.load(
        data=mock_data,
        block=mock_block,
        role=mock_role,
        task_include=mock_task_include,
        variable_manager=mock_variable_manager,
        loader=mock_loader
    )

    # Then
    assert isinstance(handler_task_include, HandlerTaskInclude)
    assert handler_task_include.listen == 'my_event'
    assert handler_task_include.get_name() == 'include_task.yml'


# Generated at 2024-03-18 02:54:17.959360
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():    # Mocking the necessary objects and inputs
    mock_data = {'name': 'include_task', 'listen': 'event_name'}
    mock_block = object()
    mock_role = object()
    mock_task_include = object()
    mock_variable_manager = object()
    mock_loader = object()

    # Call the method
    handler = HandlerTaskInclude.load(
        data=mock_data,
        block=mock_block,
        role=mock_role,
        task_include=mock_task_include,
        variable_manager=mock_variable_manager,
        loader=mock_loader
    )

    # Assertions to validate the returned handler object
    assert isinstance(handler, HandlerTaskInclude)
    assert handler.listen == 'event_name'
    assert handler.name == 'include_task'
    assert handler.block == mock_block
    assert handler.role == mock_role
    assert handler.task_include == mock_task_include


# Generated at 2024-03-18 02:54:25.664124
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():    # Mocking the necessary objects and inputs for the test
    mock_data = {'name': 'test_handler', 'listen': 'test_event'}
    mock_block = None
    mock_role = None
    mock_task_include = None
    mock_variable_manager = None
    mock_loader = None

    # Call the method we are testing
    handler = HandlerTaskInclude.load(
        data=mock_data,
        block=mock_block,
        role=mock_role,
        task_include=mock_task_include,
        variable_manager=mock_variable_manager,
        loader=mock_loader
    )

    # Assertions to validate the behavior of the method
    assert isinstance(handler, HandlerTaskInclude), "The returned object should be an instance of HandlerTaskInclude"
    assert handler.name == 'test_handler', "The handler name should be set to 'test_handler'"
    assert handler.listen == 'test_event', "The handler should listen to 'test_event'"


# Generated at 2024-03-18 02:54:32.510579
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():    # Mocking the necessary objects and inputs for the test
    mock_data = {'name': 'test_handler', 'listen': 'test_event'}
    mock_block = None
    mock_role = None
    mock_task_include = None
    mock_variable_manager = None
    mock_loader = None

    # Call the method we are testing
    handler = HandlerTaskInclude.load(
        data=mock_data,
        block=mock_block,
        role=mock_role,
        task_include=mock_task_include,
        variable_manager=mock_variable_manager,
        loader=mock_loader
    )

    # Assertions to validate the behavior of the method
    assert isinstance(handler, HandlerTaskInclude), "The returned object should be an instance of HandlerTaskInclude"
    assert handler.name == 'test_handler', "The name attribute should be set to 'test_handler'"
    assert handler.listen == 'test_event', "The listen attribute should be set to 'test_event'"


# Generated at 2024-03-18 02:54:40.180761
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():    # Create a mock block, role, task_include, variable_manager, and loader
    mock_block = None
    mock_role = None
    mock_task_include = None
    mock_variable_manager = None
    mock_loader = None

    # Create a data dictionary to simulate input data
    data = {
        'name': 'include_tasks.yml',
        'listen': 'my_event'
    }

    # Call the load method with the mock objects and data
    handler = HandlerTaskInclude.load(data, block=mock_block, role=mock_role, task_include=mock_task_include, variable_manager=mock_variable_manager, loader=mock_loader)

    # Assertions to check if the handler is correctly instantiated
    assert isinstance(handler, HandlerTaskInclude), "HandlerTaskInclude instance is not created"
    assert handler.listen == 'my_event', "HandlerTaskInclude 'listen' attribute not set correctly"

# Generated at 2024-03-18 02:54:45.056757
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():    # Given
    mock_block = None
    mock_role = None
    mock_task_include = None
    mock_variable_manager = None
    mock_loader = None
    mock_data = {'listen': 'my_event', 'name': 'include_task.yml'}

    # When
    handler_task_include = HandlerTaskInclude.load(
        data=mock_data,
        block=mock_block,
        role=mock_role,
        task_include=mock_task_include,
        variable_manager=mock_variable_manager,
        loader=mock_loader
    )

    # Then
    assert isinstance(handler_task_include, HandlerTaskInclude)
    assert handler_task_include.listen == 'my_event'
    assert handler_task_include.get_name() == 'include_task.yml'


# Generated at 2024-03-18 02:54:57.040237
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():    # Given
    mock_block = None
    mock_role = None
    mock_task_include = None
    mock_variable_manager = None
    mock_loader = None
    mock_data = {'listen': 'event_name'}

    # When
    handler_task_include = HandlerTaskInclude.load(
        data=mock_data,
        block=mock_block,
        role=mock_role,
        task_include=mock_task_include,
        variable_manager=mock_variable_manager,
        loader=mock_loader
    )

    # Then
    assert isinstance(handler_task_include, HandlerTaskInclude)
    assert handler_task_include.listen == 'event_name'

# Generated at 2024-03-18 02:55:33.739495
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():    # Given
    mock_block = None
    mock_role = None
    mock_task_include = None
    mock_variable_manager = None
    mock_loader = None
    mock_data = {'listen': 'my_event', 'name': 'include_task.yml'}

    # When
    handler_task_include = HandlerTaskInclude.load(
        data=mock_data,
        block=mock_block,
        role=mock_role,
        task_include=mock_task_include,
        variable_manager=mock_variable_manager,
        loader=mock_loader
    )

    # Then
    assert isinstance(handler_task_include, HandlerTaskInclude)
    assert handler_task_include.listen == 'my_event'
    assert handler_task_include.get_name() == 'include_task.yml'


# Generated at 2024-03-18 02:55:38.684158
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():    # Given
    mock_block = None
    mock_role = None
    mock_task_include = None
    mock_variable_manager = None
    mock_loader = None
    mock_data = {'listen': 'my_event', 'name': 'include_task.yml'}

    # When
    handler_task_include = HandlerTaskInclude.load(
        data=mock_data,
        block=mock_block,
        role=mock_role,
        task_include=mock_task_include,
        variable_manager=mock_variable_manager,
        loader=mock_loader
    )

    # Then
    assert isinstance(handler_task_include, HandlerTaskInclude)
    assert handler_task_include.listen == 'my_event'
    assert handler_task_include.get_name() == 'include_task.yml'


# Generated at 2024-03-18 02:55:47.085294
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():    # Mocking the necessary objects and inputs
    mock_data = {'name': 'include_task', 'listen': 'event_name'}
    mock_block = None
    mock_role = None
    mock_task_include = None
    mock_variable_manager = None
    mock_loader = None

    # Call the method
    handler = HandlerTaskInclude.load(
        data=mock_data,
        block=mock_block,
        role=mock_role,
        task_include=mock_task_include,
        variable_manager=mock_variable_manager,
        loader=mock_loader
    )

    # Assertions to validate the behavior of the method
    assert isinstance(handler, HandlerTaskInclude), "The returned object should be an instance of HandlerTaskInclude"
    assert handler.listen == 'event_name', "The 'listen' attribute should be set to 'event_name'"
    assert handler.name == 'include_task', "The 'name' attribute should be set to 'include_task'"


# Generated at 2024-03-18 02:55:55.091965
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():    # Mocking the necessary objects and inputs for the test
    mock_data = {'name': 'test_handler', 'listen': 'test_event'}
    mock_block = None
    mock_role = None
    mock_task_include = None
    mock_variable_manager = None
    mock_loader = None

    # Call the method we are testing
    handler = HandlerTaskInclude.load(
        data=mock_data,
        block=mock_block,
        role=mock_role,
        task_include=mock_task_include,
        variable_manager=mock_variable_manager,
        loader=mock_loader
    )

    # Assertions to validate the behavior of the method
    assert isinstance(handler, HandlerTaskInclude), "The returned object should be an instance of HandlerTaskInclude"
    assert handler.name == 'test_handler', "The name attribute should be set to 'test_handler'"
    assert handler.listen == 'test_event', "The listen attribute should be set to 'test_event'"


# Generated at 2024-03-18 02:56:01.718923
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():    # Mocking the necessary components for the test
    mock_data = {'name': 'test_handler', 'listen': 'test_event'}
    mock_block = None
    mock_role = None
    mock_task_include = None
    mock_variable_manager = None
    mock_loader = None

    # Call the method we are testing
    handler = HandlerTaskInclude.load(
        data=mock_data,
        block=mock_block,
        role=mock_role,
        task_include=mock_task_include,
        variable_manager=mock_variable_manager,
        loader=mock_loader
    )

    # Assertions to validate the behavior of the method
    assert isinstance(handler, HandlerTaskInclude), "The returned object should be an instance of HandlerTaskInclude"
    assert handler.name == 'test_handler', "The name attribute should be set to 'test_handler'"
    assert handler.listen == 'test_event', "The listen attribute should be set to 'test_event'"


# Generated at 2024-03-18 02:56:08.350022
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():    # Mocking the necessary objects and inputs for the test
    mock_data = {'name': 'test_handler', 'listen': 'test_event'}
    mock_block = None
    mock_role = None
    mock_task_include = None
    mock_variable_manager = None
    mock_loader = None

    # Call the method we are testing
    handler = HandlerTaskInclude.load(
        data=mock_data,
        block=mock_block,
        role=mock_role,
        task_include=mock_task_include,
        variable_manager=mock_variable_manager,
        loader=mock_loader
    )

    # Assertions to validate the behavior of the method
    assert isinstance(handler, HandlerTaskInclude), "The returned object should be an instance of HandlerTaskInclude"
    assert handler.name == 'test_handler', "The handler name should be set correctly"
    assert handler.listen == 'test_event', "The handler should listen to the correct event"


# Generated at 2024-03-18 02:56:15.200602
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():    # Mocking the necessary objects and inputs
    mock_data = {'listen': 'my_event', 'name': 'include_task.yml'}
    mock_block = None
    mock_role = None
    mock_task_include = None
    mock_variable_manager = None
    mock_loader = None

    # Call the method
    handler = HandlerTaskInclude.load(
        data=mock_data,
        block=mock_block,
        role=mock_role,
        task_include=mock_task_include,
        variable_manager=mock_variable_manager,
        loader=mock_loader
    )

    # Assertions to validate the behavior of the method
    assert isinstance(handler, HandlerTaskInclude), "The returned object should be an instance of HandlerTaskInclude"
    assert handler.listen == 'my_event', "The 'listen' attribute should be set to 'my_event'"

# Generated at 2024-03-18 02:56:21.979695
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():    # Mocking the necessary objects and inputs
    mock_data = {'name': 'test_handler', 'listen': 'test_event'}
    mock_block = None
    mock_role = None
    mock_task_include = None
    mock_variable_manager = None
    mock_loader = None

    # Call the method
    handler = HandlerTaskInclude.load(
        data=mock_data,
        block=mock_block,
        role=mock_role,
        task_include=mock_task_include,
        variable_manager=mock_variable_manager,
        loader=mock_loader
    )

    # Assertions to validate the behavior of the method
    assert isinstance(handler, HandlerTaskInclude), "The returned object should be an instance of HandlerTaskInclude"
    assert handler.name == 'test_handler', "The name attribute should be set to 'test_handler'"
    assert handler.listen == 'test_event', "The listen attribute should be set to 'test_event'"


# Generated at 2024-03-18 02:56:28.067569
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():    # Mocking the necessary objects and inputs for the test
    mock_data = {'listen': 'my_event', 'name': 'include_task.yml'}
    mock_block = None
    mock_role = None
    mock_task_include = None
    mock_variable_manager = None
    mock_loader = None

    # Call the method we are testing
    result = HandlerTaskInclude.load(
        data=mock_data,
        block=mock_block,
        role=mock_role,
        task_include=mock_task_include,
        variable_manager=mock_variable_manager,
        loader=mock_loader
    )

    # Assertions to validate the behavior of the method
    assert isinstance(result, HandlerTaskInclude), "Result should be an instance of HandlerTaskInclude"
    assert result.listen == 'my_event', "Handler should have 'listen' attribute set to 'my_event'"

# Generated at 2024-03-18 02:56:34.495366
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():    # Mocking the necessary components for the test
    mock_data = {'listen': 'my_event', 'name': 'include_task.yml'}
    mock_block = None
    mock_role = None
    mock_task_include = None
    mock_variable_manager = None
    mock_loader = None

    # Call the method we're testing
    handler = HandlerTaskInclude.load(
        data=mock_data,
        block=mock_block,
        role=mock_role,
        task_include=mock_task_include,
        variable_manager=mock_variable_manager,
        loader=mock_loader
    )

    # Assertions to validate the behavior of the method
    assert isinstance(handler, HandlerTaskInclude), "The returned object should be an instance of HandlerTaskInclude"
    assert handler.listen == 'my_event', "The 'listen' attribute should be set to 'my_event'"

# Generated at 2024-03-18 02:57:45.199887
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():    # Mocking the necessary components for the test
    mock_block = Mock()
    mock_role = Mock()
    mock_task_include = Mock()
    mock_variable_manager = Mock()
    mock_loader = Mock()
    mock_data = {'listen': 'my_event', 'name': 'include_task.yml'}

    # Call the method we're testing
    handler = HandlerTaskInclude.load(
        data=mock_data,
        block=mock_block,
        role=mock_role,
        task_include=mock_task_include,
        variable_manager=mock_variable_manager,
        loader=mock_loader
    )

    # Assertions to validate the behavior of the method
    assert isinstance(handler, HandlerTaskInclude)
    assert handler.listen == 'my_event'
    assert handler.get_name() == 'include_task.yml'
    assert handler.block == mock_block
    assert handler.role == mock_role
    assert handler.task_include == mock_task_include
    assert handler.variable_manager == mock_variable_manager

# Generated at 2024-03-18 02:57:53.781872
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():    # Mocking the necessary components for the test
    mock_data = {'listen': 'my_event', 'name': 'include_task.yml'}
    mock_block = None
    mock_role = None
    mock_task_include = None
    mock_variable_manager = None
    mock_loader = None

    # Call the method we're testing
    handler = HandlerTaskInclude.load(
        data=mock_data,
        block=mock_block,
        role=mock_role,
        task_include=mock_task_include,
        variable_manager=mock_variable_manager,
        loader=mock_loader
    )

    # Assertions to validate the behavior of the method
    assert isinstance(handler, HandlerTaskInclude), "The returned object should be an instance of HandlerTaskInclude"
    assert handler.listen == 'my_event', "The 'listen' attribute should be set to 'my_event'"

# Generated at 2024-03-18 02:58:00.173545
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():    # Mocking the necessary objects and inputs for the test
    mock_data = {'listen': 'my_event', 'name': 'include_task.yml'}
    mock_block = None
    mock_role = None
    mock_task_include = None
    mock_variable_manager = None
    mock_loader = None

    # Call the method we're testing
    handler = HandlerTaskInclude.load(
        data=mock_data,
        block=mock_block,
        role=mock_role,
        task_include=mock_task_include,
        variable_manager=mock_variable_manager,
        loader=mock_loader
    )

    # Assertions to validate the behavior of the method
    assert isinstance(handler, HandlerTaskInclude), "The returned object should be an instance of HandlerTaskInclude"
    assert handler.listen == 'my_event', "The 'listen' attribute should be set to 'my_event'"

# Generated at 2024-03-18 02:58:07.748322
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():    # Mocking the necessary components for the test
    mock_data = {'name': 'include_task', 'listen': 'event_name'}
    mock_block = object()
    mock_role = object()
    mock_task_include = object()
    mock_variable_manager = object()
    mock_loader = object()

    # Call the method we're testing
    handler = HandlerTaskInclude.load(
        data=mock_data,
        block=mock_block,
        role=mock_role,
        task_include=mock_task_include,
        variable_manager=mock_variable_manager,
        loader=mock_loader
    )

    # Assertions to validate the behavior of the method
    assert isinstance(handler, HandlerTaskInclude)
    assert handler.listen == 'event_name'
    assert handler.name == 'include_task'
    assert handler.block is mock_block
    assert handler.role is mock_role
    assert handler.task_include is mock_task_include
    assert handler._variable_manager is mock_variable_manager

# Generated at 2024-03-18 02:58:16.516942
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():    # Mocking the necessary objects and inputs
    mock_data = {'name': 'include_tasks', 'listen': 'my_event'}
    mock_block = None
    mock_role = None
    mock_task_include = None
    mock_variable_manager = None
    mock_loader = None

    # Call the method
    handler = HandlerTaskInclude.load(
        data=mock_data,
        block=mock_block,
        role=mock_role,
        task_include=mock_task_include,
        variable_manager=mock_variable_manager,
        loader=mock_loader
    )

    # Assertions to validate the behavior of the method
    assert isinstance(handler, HandlerTaskInclude), "The returned object should be an instance of HandlerTaskInclude"
    assert handler.listen == 'my_event', "The 'listen' attribute should be set to 'my_event'"
    assert handler.name == 'include_tasks', "The 'name' attribute should be set to 'include_tasks'"


# Generated at 2024-03-18 02:58:23.422708
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():    # Given
    mock_block = None
    mock_role = None
    mock_task_include = None
    mock_variable_manager = None
    mock_loader = None

    # When
    handler_task_include = HandlerTaskInclude.load(
        data={},
        block=mock_block,
        role=mock_role,
        task_include=mock_task_include,
        variable_manager=mock_variable_manager,
        loader=mock_loader
    )

    # Then
    assert isinstance(handler_task_include, HandlerTaskInclude)
    assert handler_task_include.block is mock_block
    assert handler_task_include.role is mock_role
    assert handler_task_include.task_include is mock_task_include
    assert handler_task_include._variable_manager is mock_variable_manager
    assert handler_task_include._loader is mock_loader


# Generated at 2024-03-18 02:58:30.148165
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():    # Mocking the necessary objects and inputs for the test
    mock_data = {'name': 'test_handler', 'listen': 'test_event'}
    mock_block = None
    mock_role = None
    mock_task_include = None
    mock_variable_manager = None
    mock_loader = None

    # Call the method we are testing
    result = HandlerTaskInclude.load(
        data=mock_data,
        block=mock_block,
        role=mock_role,
        task_include=mock_task_include,
        variable_manager=mock_variable_manager,
        loader=mock_loader
    )

    # Assertions to validate the behavior of the method
    assert isinstance(result, HandlerTaskInclude), "Result should be an instance of HandlerTaskInclude"
    assert result.name == 'test_handler', "Handler name should be set correctly"
    assert result.listen == 'test_event', "Handler should listen to the correct event"


# Generated at 2024-03-18 02:58:36.645955
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():    # Create a mock block, role, task_include, variable_manager, and loader
    mock_block = None
    mock_role = None
    mock_task_include = None
    mock_variable_manager = None
    mock_loader = None

    # Create a sample data dictionary to simulate input
    sample_data = {
        'name': 'Include a task list',
        'include': 'some_task_file.yml',
        'listen': 'my_custom_event'
    }

    # Instantiate HandlerTaskInclude using the load method
    handler_task_include = HandlerTaskInclude.load(
        data=sample_data,
        block=mock_block,
        role=mock_role,
        task_include=mock_task_include,
        variable_manager=mock_variable_manager,
        loader=mock_loader
    )

    # Assertions to check if the object is created correctly
    assert isinstance(handler_task_include, HandlerTaskInclude), "Object is not an instance of HandlerTaskInclude"
    assert handler

# Generated at 2024-03-18 02:58:44.603832
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():    # Mocking the necessary components for the test
    mock_data = {'name': 'test_handler', 'listen': 'test_event'}
    mock_block = None
    mock_role = None
    mock_task_include = None
    mock_variable_manager = None
    mock_loader = None

    # Call the method we're testing
    handler = HandlerTaskInclude.load(
        data=mock_data,
        block=mock_block,
        role=mock_role,
        task_include=mock_task_include,
        variable_manager=mock_variable_manager,
        loader=mock_loader
    )

    # Assertions to validate the behavior of the method
    assert isinstance(handler, HandlerTaskInclude), "The returned object should be an instance of HandlerTaskInclude"
    assert handler.name == 'test_handler', "The handler name should be set to 'test_handler'"
    assert handler.listen == 'test_event', "The handler should listen to 'test_event'"


# Generated at 2024-03-18 02:58:52.501148
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():    # Given
    mock_block = None
    mock_role = None
    mock_task_include = None
    mock_variable_manager = None
    mock_loader = None
    mock_data = {'listen': 'my_event', 'name': 'include_task.yml'}

    # When
    handler_task_include = HandlerTaskInclude.load(
        data=mock_data,
        block=mock_block,
        role=mock_role,
        task_include=mock_task_include,
        variable_manager=mock_variable_manager,
        loader=mock_loader
    )

    # Then
    assert isinstance(handler_task_include, HandlerTaskInclude)
    assert handler_task_include.listen == 'my_event'
    assert handler_task_include.get_name() == 'include_task.yml'
