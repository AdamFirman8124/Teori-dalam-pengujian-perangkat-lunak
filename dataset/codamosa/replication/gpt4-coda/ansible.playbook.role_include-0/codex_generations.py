

# Generated at 2024-03-18 03:00:14.085507
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():    # Setup the context for the test
    fake_loader = None
    fake_variable_manager = None
    fake_play = None

    # Create a fake IncludeRole object with minimal configuration
    include_role = IncludeRole()

    # Set the role name to a fake role
    include_role._role_name = 'fake_role'

    # Mock the Role.load method to return a fake Role object
    def mock_role_load(role_include, play, parent_role, from_files, from_include, validate):
        fake_role = Role()
        fake_role._role_path = '/path/to/fake_role'
        return fake_role

    # Patch the Role.load method
    original_role_load = Role.load
    Role.load = mock_role_load


# Generated at 2024-03-18 03:00:21.775526
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():    # Setup test data and mocks
    fake_loader = None
    fake_variable_manager = None
    fake_block = Block()
    fake_role = Role()
    fake_task_include = TaskInclude()

    # Test data for IncludeRole.load
    test_data = {
        'name': 'testrole',
        'tasks_from': 'main.yml',
        'vars_from': 'vars/main.yml',
        'defaults_from': 'defaults/main.yml',
        'handlers_from': 'handlers/main.yml',
        'apply': {'tags': ['test']},
        'public': True,
        'allow_duplicates': False,
        'rolespec_validate': True
    }

    # Call IncludeRole.load with test data
    include_role = IncludeRole.load(
        data=test_data,
        block=fake_block,
        role=fake_role,
        task_include=fake_task_include,
        variable_manager=fake_variable_manager,
        loader=fake_loader
    )

    # Assertions

# Generated at 2024-03-18 03:00:31.201672
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():    # Setup the context for the test
    fake_loader = None
    fake_variable_manager = None
    fake_block = Block()
    fake_role = Role()

    # Test data
    include_role_args = {
        'name': 'testrole',
        'tasks_from': 'main.yml',
        'vars_from': 'vars/main.yml',
        'defaults_from': 'defaults/main.yml',
        'handlers_from': 'handlers/main.yml',
        'public': True,
        'apply': {'tags': ['test']},
        'allow_duplicates': False,
        'rolespec_validate': True
    }

    # Expected results
    expected_role_name = 'testrole'
    expected_from_files = {
        'tasks': 'main.yml',
        'vars': 'vars/main.yml',
        'defaults': 'defaults/main.yml',
        'handlers': 'handlers/main.yml'
    }
    expected_public = True

# Generated at 2024-03-18 03:00:38.833053
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():    # Setup test data and mocks
    fake_loader = MagicMock()
    fake_variable_manager = MagicMock()
    fake_block = MagicMock()
    fake_role = MagicMock()
    fake_task_include = MagicMock()

    # Test data for IncludeRole.load
    test_data = {
        'name': 'testrole',
        'tasks_from': 'main.yml',
        'vars_from': 'vars/main.yml',
        'defaults_from': 'defaults/main.yml',
        'handlers_from': 'handlers/main.yml',
        'apply': {'delegate_to': 'localhost'},
        'public': True,
        'allow_duplicates': False,
        'rolespec_validate': True
    }

    # Expected results
    expected_from_files = {
        'tasks': 'main.yml',
        'vars': 'vars/main.yml',
        'defaults': 'defaults/main.yml',
        'handlers': 'handlers/main.yml'
    }

    # Call the method

# Generated at 2024-03-18 03:00:45.931461
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():    # Setup the test scenario
    block = Block()
    role = Role()
    include_role = IncludeRole(block=block, role=role)
    include_role.name = "test_include_role"
    include_role.action = "include_role"
    include_role._role_name = "test_role"

    # Call the method
    result = include_role.get_name()

    # Assert the expected output
    assert result == "test_include_role", "The name should be 'test_include_role'"

    # Test with no explicit name set
    include_role.name = None
    result = include_role.get_name()
    expected = "include_role : test_role"
    assert result == expected, f"The name should be '{expected}' when no explicit name is set"


# Generated at 2024-03-18 03:00:54.041122
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():    # Mock objects and data for testing
    mock_play = MagicMock()
    mock_variable_manager = MagicMock()
    mock_loader = MagicMock()
    mock_role = MagicMock()
    mock_block = MagicMock()
    mock_task_include = MagicMock()

    # Create an instance of IncludeRole
    include_role = IncludeRole(block=mock_block, role=mock_role, task_include=mock_task_include)

    # Set up the role name and path
    include_role._role_name = 'test_role'
    include_role._role_path = '/path/to/test_role'

    # Set up the from_files dictionary
    include_role._from_files = {
        'tasks': 'main.yml',
        'vars': 'main.yml',
        'defaults': 'main.yml',
        'handlers': 'main.yml'
    }

    # Set up the templar to return the same values as the from_files dictionary
    mock_templar = MagicMock()
    mock_templar.template.side

# Generated at 2024-03-18 03:01:00.276763
# Unit test for method get_include_params of class IncludeRole
def test_IncludeRole_get_include_params():    # Create a mock IncludeRole instance with necessary attributes
    include_role = IncludeRole()
    include_role._parent_role = Role()
    include_role._parent_role._role_name = "parent_role"
    include_role._parent_role._role_path = "/path/to/parent_role"
    include_role._role_name = "test_role"
    include_role._role_path = "/path/to/test_role"

    # Mock the get_role_params method of the parent role
    include_role._parent_role.get_role_params = lambda: {'role_param': 'value'}

    # Call the method under test
    include_params = include_role.get_include_params()

    # Assert expected values in the include_params
    assert include_params['role_param'] == 'value'
    assert include_params['ansible_parent_role_names'] == ['parent_role']
    assert include_params['ansible_parent_role_paths'] == ['/path/to/parent_role']


# Generated at 2024-03-18 03:01:06.186201
# Unit test for method get_include_params of class IncludeRole
def test_IncludeRole_get_include_params():    # Setup the context for the test
    fake_loader = None
    fake_variable_manager = None
    fake_block = Block()
    fake_role = Role()
    fake_task_include = TaskInclude()

    # Create an instance of IncludeRole
    include_role = IncludeRole(block=fake_block, role=fake_role, task_include=fake_task_include)

    # Set attributes for the IncludeRole instance
    include_role._parent_role = fake_role
    include_role._role_name = "test_role"
    include_role._role_path = "/path/to/test_role"

    # Mock the parent role's get_role_params and get_name methods
    fake_role.get_role_params = lambda: {'role_param_key': 'role_param_value'}
    fake_role.get_name = lambda: 'parent_role_name'

    # Call the method under test
    include_params = include_role.get_include_params()

    # Assertions to validate the behavior of get_include_params

# Generated at 2024-03-18 03:01:13.630326
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():    # Setup test data and mocks
    fake_loader = None
    fake_variable_manager = None
    fake_block = Block()
    fake_role = Role()
    fake_task_include = TaskInclude()

    # Test data for IncludeRole.load
    test_data = {
        'name': 'testrole',
        'tasks_from': 'main.yml',
        'vars_from': 'vars/main.yml',
        'defaults_from': 'defaults/main.yml',
        'handlers_from': 'handlers/main.yml',
        'apply': {'tags': ['test']},
        'public': True,
        'allow_duplicates': False,
        'rolespec_validate': True
    }

    # Call IncludeRole.load with test data
    include_role = IncludeRole.load(
        data=test_data,
        block=fake_block,
        role=fake_role,
        task_include=fake_task_include,
        variable_manager=fake_variable_manager,
        loader=fake_loader
    )

    # Assertions

# Generated at 2024-03-18 03:01:20.001884
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():    # Mock objects and data for testing
    mock_play = MagicMock()
    mock_variable_manager = MagicMock()
    mock_loader = MagicMock()
    mock_block = MagicMock()
    mock_role = MagicMock()
    mock_task_include = MagicMock()

    # Create an instance of IncludeRole
    include_role = IncludeRole(block=mock_block, role=mock_role, task_include=mock_task_include)

    # Set up the role name and path
    include_role._role_name = 'test_role'
    include_role._role_path = '/path/to/test_role'

    # Mock the RoleInclude.load method

# Generated at 2024-03-18 03:01:35.456127
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():    # Mock objects and data for testing
    mock_play = MagicMock()
    mock_variable_manager = MagicMock()
    mock_loader = MagicMock()
    mock_block = MagicMock()
    mock_role = MagicMock()
    mock_task_include = MagicMock()

    # Create an instance of IncludeRole
    include_role = IncludeRole(block=mock_block, role=mock_role, task_include=mock_task_include)

    # Set necessary attributes for the test
    include_role._role_name = 'test_role'
    include_role._from_files = {'tasks': 'main.yml'}
    include_role._parent_role = mock_role
    include_role.rolespec_validate = True
    include_role.allow_duplicates = True
    include_role.public = False
    include_role.statically_loaded = False

    # Mock the RoleInclude.load method

# Generated at 2024-03-18 03:01:43.829624
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():    # Setup test data and mocks
    fake_loader = MagicMock()
    fake_variable_manager = MagicMock()
    fake_block = MagicMock()
    fake_role = MagicMock()
    fake_task_include = MagicMock()

    # Test data for IncludeRole.load
    test_data = {
        'name': 'test_role',
        'tasks_from': 'main.yml',
        'vars_from': 'vars/main.yml',
        'defaults_from': 'defaults/main.yml',
        'handlers_from': 'handlers/main.yml',
        'apply': {'delegate_to': 'localhost'},
        'public': True,
        'allow_duplicates': False,
        'rolespec_validate': True
    }

    # Expected results
    expected_from_files = {
        'tasks': 'main.yml',
        'vars': 'vars/main.yml',
        'defaults': 'defaults/main.yml',
        'handlers': 'handlers/main.yml'
    }

    # Call the method

# Generated at 2024-03-18 03:01:50.942156
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():    # Mock objects and data for testing
    mock_play = MagicMock()
    mock_variable_manager = MagicMock()
    mock_loader = MagicMock()
    mock_role = MagicMock()
    mock_block = MagicMock()
    mock_task_include = MagicMock()

    # Create an instance of IncludeRole
    include_role = IncludeRole(block=mock_block, role=mock_role, task_include=mock_task_include)

    # Set up the role name and path
    include_role._role_name = 'test_role'
    include_role._role_path = '/path/to/test_role'

    # Set up the from_files
    include_role._from_files = {
        'tasks': 'main.yml',
        'vars': 'main.yml',
        'defaults': 'main.yml',
        'handlers': 'main.yml'
    }

    # Set up the role to return a list of blocks and handlers
    mock_role.compile.return_value = [mock_block]
    mock_role.get_handler_blocks.return_value

# Generated at 2024-03-18 03:01:58.385276
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():    # Mock objects and data for testing
    mock_play = MagicMock()
    mock_variable_manager = MagicMock()
    mock_loader = MagicMock()
    mock_block = MagicMock()
    mock_role = MagicMock()
    mock_task_include = MagicMock()

    # Create an instance of IncludeRole
    include_role = IncludeRole(block=mock_block, role=mock_role, task_include=mock_task_include)

    # Set up the role name and path
    include_role._role_name = 'test_role'
    include_role._role_path = '/path/to/test_role'

    # Set up the _from_files to simulate `tasks_from`, `vars_from`, etc.
    include_role._from_files = {
        'tasks': 'main.yml',
        'vars': 'main.yml',
        'defaults': 'main.yml',
        'handlers': 'main.yml'
    }

    # Set up the return values for the mocked objects
    mock_play.roles = []
    mock_play.handlers

# Generated at 2024-03-18 03:02:05.174446
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():    # Setup test data and mocks
    fake_loader = MagicMock()
    fake_variable_manager = MagicMock()
    fake_block = MagicMock()
    fake_role = MagicMock()
    fake_task_include = MagicMock()

    # Test data for IncludeRole.load
    test_data = {
        'name': 'testrole',
        'tasks_from': 'main.yml',
        'vars_from': 'vars/main.yml',
        'defaults_from': 'defaults/main.yml',
        'handlers_from': 'handlers/main.yml',
        'apply': {'delegate_to': 'localhost'},
        'public': True,
        'allow_duplicates': False,
        'rolespec_validate': True
    }

    # Expected results
    expected_from_files = {
        'tasks': 'main.yml',
        'vars': 'vars/main.yml',
        'defaults': 'defaults/main.yml',
        'handlers': 'handlers/main.yml'
    }

    # Call the method

# Generated at 2024-03-18 03:02:11.633431
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():    # Mock objects and data for testing
    mock_play = MagicMock()
    mock_variable_manager = MagicMock()
    mock_loader = MagicMock()
    mock_role = MagicMock()
    mock_block = MagicMock()
    mock_task_include = MagicMock()

    # Create an instance of IncludeRole
    include_role = IncludeRole(block=mock_block, role=mock_role, task_include=mock_task_include)

    # Set necessary attributes for the test
    include_role._role_name = 'test_role'
    include_role._from_files = {'tasks': 'main.yml'}
    include_role._parent_role = mock_role
    include_role.rolespec_validate = True
    include_role.allow_duplicates = True
    include_role.public = False
    include_role.statically_loaded = False

    # Mock the Role and RoleInclude classes and their methods
    mock_role_include = MagicMock()
    mock_role_include.load.return_value = mock_role_include
    mock_role_include.vars = {}
    mock

# Generated at 2024-03-18 03:02:19.287404
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():    # Setup test data and mocks
    fake_loader = MagicMock()
    fake_variable_manager = MagicMock()
    fake_block = MagicMock()
    fake_role = MagicMock()
    fake_task_include = MagicMock()

    # Test data for IncludeRole.load
    test_data = {
        'name': 'testrole',
        'tasks_from': 'main.yml',
        'vars_from': 'vars/main.yml',
        'defaults_from': 'defaults/main.yml',
        'handlers_from': 'handlers/main.yml',
        'apply': {'delegate_to': 'localhost'},
        'public': True,
        'allow_duplicates': False,
        'rolespec_validate': True
    }

    # Expected results
    expected_from_files = {
        'tasks': 'main.yml',
        'vars': 'vars/main.yml',
        'defaults': 'defaults/main.yml',
        'handlers': 'handlers/main.yml'
    }

    # Call the method

# Generated at 2024-03-18 03:02:25.187940
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():    # Mock objects and data for testing
    mock_play = MagicMock()
    mock_variable_manager = MagicMock()
    mock_loader = MagicMock()
    mock_role = MagicMock()
    mock_block = MagicMock()
    mock_task_include = MagicMock()

    # Create an instance of IncludeRole
    include_role = IncludeRole(block=mock_block, role=mock_role, task_include=mock_task_include)

    # Set necessary attributes for the test
    include_role._role_name = 'test_role'
    include_role._from_files = {'tasks': 'main.yml'}
    include_role._parent_role = mock_role
    include_role.rolespec_validate = True
    include_role.allow_duplicates = True
    include_role.public = False
    include_role.statically_loaded = False

    # Mock the RoleInclude.load method
    mock_role_include = MagicMock()

# Generated at 2024-03-18 03:02:31.230168
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():    # Setup test data and mocks
    fake_loader = MagicMock()
    fake_variable_manager = MagicMock()
    fake_block = MagicMock()
    fake_role = MagicMock()
    fake_task_include = MagicMock()

    # Test data for IncludeRole.load
    test_data = {
        'name': 'testrole',
        'tasks_from': 'main.yml',
        'vars_from': 'vars/main.yml',
        'defaults_from': 'defaults/main.yml',
        'handlers_from': 'handlers/main.yml',
        'apply': {'delegate_to': 'localhost'},
        'public': True,
        'allow_duplicates': False,
        'rolespec_validate': True
    }

    # Expected results
    expected_from_files = {
        'tasks': 'main.yml',
        'vars': 'vars/main.yml',
        'defaults': 'defaults/main.yml',
        'handlers': 'handlers/main.yml'
    }

    # Call the method

# Generated at 2024-03-18 03:02:37.634179
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():    # Setup test data and mocks
    fake_loader = MagicMock()
    fake_variable_manager = MagicMock()
    fake_block = MagicMock()
    fake_role = MagicMock()
    fake_task_include = MagicMock()

    # Test data for IncludeRole.load
    test_data = {
        'name': 'testrole',
        'tasks_from': 'main.yml',
        'vars_from': 'vars/main.yml',
        'defaults_from': 'defaults/main.yml',
        'handlers_from': 'handlers/main.yml',
        'apply': {'tags': ['test']},
        'public': True,
        'allow_duplicates': False,
        'rolespec_validate': True
    }

    # Call IncludeRole.load with test data
    include_role = IncludeRole.load(
        data=test_data,
        block=fake_block,
        role=fake_role,
        task_include=fake_task_include,
        variable_manager=fake_variable_manager,
        loader=fake_loader
    )

    # Assertions to

# Generated at 2024-03-18 03:03:03.667856
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():    # Mock objects and data for testing
    mock_play = MagicMock()
    mock_variable_manager = MagicMock()
    mock_loader = MagicMock()
    mock_role = MagicMock()
    mock_block = MagicMock()
    mock_task_include = MagicMock()

    # Create an instance of IncludeRole
    include_role = IncludeRole(block=mock_block, role=mock_role, task_include=mock_task_include)

    # Set necessary attributes for the IncludeRole instance
    include_role._role_name = 'test_role'
    include_role._from_files = {'tasks': 'main.yml'}
    include_role._parent_role = mock_role
    include_role.rolespec_validate = True
    include_role.allow_duplicates = True
    include_role.public = False
    include_role.statically_loaded = False

    # Mock the Role.load method to return a mock role

# Generated at 2024-03-18 03:03:08.654227
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():    # Setup the test scenario
    block = Block()
    role = Role()
    role._role_name = "test_role"
    include_role = IncludeRole(block=block, role=role)
    include_role.name = "include test_role"

    # Call the method
    result = include_role.get_name()

    # Assert the expected output
    assert result == "include test_role", "The name should be 'include test_role'"

    # Test with no explicit name set
    include_role.name = None
    result = include_role.get_name()
    assert result == "include_role : test_role", "The name should default to 'include_role : test_role' when no explicit name is set"

# Generated at 2024-03-18 03:03:15.804035
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():    # Setup test data and mocks
    fake_loader = MagicMock()
    fake_variable_manager = MagicMock()
    fake_block = MagicMock()
    fake_role = MagicMock()
    fake_task_include = MagicMock()

    # Test data for IncludeRole.load
    test_data = {
        'name': 'testrole',
        'tasks_from': 'main.yml',
        'vars_from': 'vars/main.yml',
        'defaults_from': 'defaults/main.yml',
        'handlers_from': 'handlers/main.yml',
        'apply': {'tags': ['test']},
        'public': True,
        'allow_duplicates': False,
        'rolespec_validate': True
    }

    # Expected results
    expected_from_files = {
        'tasks': 'main.yml',
        'vars': 'vars/main.yml',
        'defaults': 'defaults/main.yml',
        'handlers': 'handlers/main.yml'
    }

    # Call the method

# Generated at 2024-03-18 03:03:21.270844
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():    # Mock objects and data for testing
    mock_play = MagicMock()
    mock_variable_manager = MagicMock()
    mock_loader = MagicMock()
    mock_role = MagicMock()
    mock_block = MagicMock()
    mock_task_include = MagicMock()

    # Create an instance of IncludeRole
    include_role = IncludeRole(block=mock_block, role=mock_role, task_include=mock_task_include)

    # Set up the role name and from_files for the include_role instance
    include_role._role_name = 'test_role'
    include_role._from_files = {'tasks': 'main.yml'}

    # Mock the Role.load method to return a mock role object
    with patch('ansible.playbook.role.Role.load', return_value=mock_role) as mock_role_load:
        # Mock the Templar object and its template method
        mock_templar = MagicMock()
        mock_templar.template.return_value = include_role._from_files

# Generated at 2024-03-18 03:03:27.307459
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():    # Mock objects and data for testing
    mock_play = MagicMock()
    mock_variable_manager = MagicMock()
    mock_loader = MagicMock()
    mock_block = MagicMock()
    mock_role = MagicMock()
    mock_task_include = MagicMock()

    # Create an instance of IncludeRole
    include_role = IncludeRole(block=mock_block, role=mock_role, task_include=mock_task_include)

    # Set necessary attributes for the IncludeRole instance
    include_role._role_name = 'test_role'
    include_role._from_files = {'tasks': 'main.yml'}
    include_role._parent_role = mock_role
    include_role.rolespec_validate = True
    include_role.allow_duplicates = True
    include_role.public = False
    include_role.statically_loaded = False

    # Mock the RoleInclude.load method
    mock_role_include = MagicMock()

# Generated at 2024-03-18 03:03:33.132333
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():    # Mock objects and data for testing
    mock_play = MagicMock()
    mock_variable_manager = MagicMock()
    mock_loader = MagicMock()
    mock_block = MagicMock()
    mock_role = MagicMock()
    mock_task_include = MagicMock()

    # Create an instance of IncludeRole
    include_role = IncludeRole(block=mock_block, role=mock_role, task_include=mock_task_include)

    # Set necessary attributes for the test
    include_role._role_name = 'test_role'
    include_role._from_files = {'tasks': 'main.yml'}
    include_role._parent_role = mock_role
    include_role.rolespec_validate = True
    include_role.allow_duplicates = True
    include_role.public = False
    include_role.statically_loaded = False

    # Mock the RoleInclude.load method

# Generated at 2024-03-18 03:03:40.067793
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():    # Setup test data and mocks
    fake_loader = None
    fake_variable_manager = None
    fake_block = Block()
    fake_role = Role()
    fake_task_include = TaskInclude()

    # Test data for IncludeRole.load
    test_data = {
        'name': 'testrole',
        'tasks_from': 'main.yml',
        'vars_from': 'vars/main.yml',
        'defaults_from': 'defaults/main.yml',
        'handlers_from': 'handlers/main.yml',
        'apply': {'delegate_to': 'localhost'},
        'public': True,
        'allow_duplicates': False,
        'rolespec_validate': True
    }

    # Call IncludeRole.load with test data
    include_role = IncludeRole.load(data=test_data, block=fake_block, role=fake_role, task_include=fake_task_include,
                                    variable_manager=fake_variable_manager, loader=fake_loader)

    # Assertions to validate the IncludeRole.load functionality

# Generated at 2024-03-18 03:03:50.365458
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():    # Setup test data and mocks
    fake_loader = MagicMock()
    fake_variable_manager = MagicMock()
    fake_block = MagicMock()
    fake_role = MagicMock()
    fake_task_include = MagicMock()

    # Test data for IncludeRole.load
    test_data = {
        'name': 'testrole',
        'tasks_from': 'main.yml',
        'vars_from': 'vars/main.yml',
        'defaults_from': 'defaults/main.yml',
        'handlers_from': 'handlers/main.yml',
        'apply': {'tags': ['test']},
        'public': True,
        'allow_duplicates': False,
        'rolespec_validate': True
    }

    # Expected results
    expected_from_files = {
        'tasks': 'main.yml',
        'vars': 'vars/main.yml',
        'defaults': 'defaults/main.yml',
        'handlers': 'handlers/main.yml'
    }

    # Call the method

# Generated at 2024-03-18 03:03:56.104509
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():    # Setup the test case
    fake_loader = None
    fake_variable_manager = None
    fake_block = Block()
    fake_role = Role()
    fake_task_include = TaskInclude()

    # Create an instance of IncludeRole
    include_role = IncludeRole(block=fake_block, role=fake_role, task_include=fake_task_include)

    # Set the action and role name for the IncludeRole instance
    include_role.action = 'include_role'
    include_role._role_name = 'test_role'

    # Call the get_name method
    name = include_role.get_name()

    # Assert the expected output
    assert name == 'include_role : test_role', "The name returned by get_name should be 'include_role : test_role'"

# Generated at 2024-03-18 03:04:02.398057
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():    # Mock objects and data for testing
    mock_play = MagicMock()
    mock_variable_manager = MagicMock()
    mock_loader = MagicMock()
    mock_block = MagicMock()
    mock_role = MagicMock()
    mock_task_include = MagicMock()

    # Create an instance of IncludeRole
    include_role = IncludeRole(block=mock_block, role=mock_role, task_include=mock_task_include)

    # Set up the role name and path
    include_role._role_name = 'test_role'
    include_role._role_path = '/path/to/test_role'

    # Mock the RoleInclude.load method

# Generated at 2024-03-18 03:04:46.985928
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():    # Setup test data and mocks
    fake_loader = None
    fake_variable_manager = None
    fake_block = Block()
    fake_role = Role()
    fake_task_include = TaskInclude()

    # Test data for IncludeRole.load
    test_data = {
        'name': 'testrole',
        'tasks_from': 'main.yml',
        'vars_from': 'vars/main.yml',
        'defaults_from': 'defaults/main.yml',
        'handlers_from': 'handlers/main.yml',
        'apply': {'tags': ['test']},
        'public': True,
        'allow_duplicates': False,
        'rolespec_validate': True
    }

    # Call IncludeRole.load with test data
    include_role = IncludeRole.load(
        data=test_data,
        block=fake_block,
        role=fake_role,
        task_include=fake_task_include,
        variable_manager=fake_variable_manager,
        loader=fake_loader
    )

    # Assertions

# Generated at 2024-03-18 03:04:52.659275
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():    # Setup test data and mocks
    fake_loader = None
    fake_variable_manager = None
    fake_block = Block()
    fake_role = Role()
    fake_task_include = TaskInclude()

    # Test data for IncludeRole.load
    test_data = {
        'name': 'testrole',
        'tasks_from': 'main.yml',
        'vars_from': 'vars/main.yml',
        'defaults_from': 'defaults/main.yml',
        'handlers_from': 'handlers/main.yml',
        'apply': {'tags': ['test']},
        'public': True,
        'allow_duplicates': False,
        'rolespec_validate': True
    }

    # Call IncludeRole.load with test data
    include_role = IncludeRole.load(
        data=test_data,
        block=fake_block,
        role=fake_role,
        task_include=fake_task_include,
        variable_manager=fake_variable_manager,
        loader=fake_loader
    )

    # Assertions

# Generated at 2024-03-18 03:04:58.390975
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():    # Setup test data and mocks
    fake_loader = MagicMock()
    fake_variable_manager = MagicMock()
    fake_block = MagicMock()
    fake_role = MagicMock()
    fake_task_include = MagicMock()

    # Test data for IncludeRole.load
    test_data = {
        'name': 'testrole',
        'tasks_from': 'main.yml',
        'vars_from': 'vars/main.yml',
        'defaults_from': 'defaults/main.yml',
        'handlers_from': 'handlers/main.yml',
        'apply': {'delegate_to': 'localhost'},
        'public': True,
        'allow_duplicates': False,
        'rolespec_validate': True
    }

    # Expected results
    expected_from_files = {
        'tasks': 'main.yml',
        'vars': 'vars/main.yml',
        'defaults': 'defaults/main.yml',
        'handlers': 'handlers/main.yml'
    }

    # Call the method

# Generated at 2024-03-18 03:05:05.956490
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():    # Mock objects and data for testing
    mock_play = MagicMock()
    mock_variable_manager = MagicMock()
    mock_loader = MagicMock()
    mock_role = MagicMock()
    mock_block = MagicMock()
    mock_task_include = MagicMock()

    # Create an instance of IncludeRole
    include_role = IncludeRole(block=mock_block, role=mock_role, task_include=mock_task_include)

    # Set up the role name and from_files for the include_role instance
    include_role._role_name = 'test_role'
    include_role._from_files = {'tasks': 'main.yml'}

    # Mock the RoleInclude.load method

# Generated at 2024-03-18 03:05:13.025882
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():    # Setup test data and mocks
    fake_loader = MagicMock()
    fake_variable_manager = MagicMock()
    fake_block = MagicMock()
    fake_role = MagicMock()
    fake_task_include = MagicMock()

    # Test data for IncludeRole.load
    test_data = {
        'name': 'testrole',
        'tasks_from': 'main.yml',
        'vars_from': 'vars/main.yml',
        'defaults_from': 'defaults/main.yml',
        'handlers_from': 'handlers/main.yml',
        'apply': {'delegate_to': 'localhost'},
        'public': True,
        'allow_duplicates': False,
        'rolespec_validate': True
    }

    # Expected results
    expected_from_files = {
        'tasks': 'main.yml',
        'vars': 'vars/main.yml',
        'defaults': 'defaults/main.yml',
        'handlers': 'handlers/main.yml'
    }

    # Call the method

# Generated at 2024-03-18 03:05:18.715479
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():    # Setup test data and mocks
    fake_loader = None
    fake_variable_manager = None
    fake_block = Block()
    fake_role = Role()
    fake_task_include = TaskInclude()

    # Test data for IncludeRole.load
    test_data = {
        'name': 'testrole',
        'tasks_from': 'main.yml',
        'vars_from': 'vars/main.yml',
        'defaults_from': 'defaults/main.yml',
        'handlers_from': 'handlers/main.yml',
        'apply': {'tags': ['test']},
        'public': True,
        'allow_duplicates': False,
        'rolespec_validate': True
    }

    # Call IncludeRole.load with test data
    include_role = IncludeRole.load(
        data=test_data,
        block=fake_block,
        role=fake_role,
        task_include=fake_task_include,
        variable_manager=fake_variable_manager,
        loader=fake_loader
    )

    # Assertions

# Generated at 2024-03-18 03:05:24.013235
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():    # Mock objects and data for testing
    mock_play = MagicMock()
    mock_variable_manager = MagicMock()
    mock_loader = MagicMock()
    mock_block = MagicMock()
    mock_role = MagicMock()
    mock_task_include = MagicMock()

    # Create an instance of IncludeRole
    include_role = IncludeRole(block=mock_block, role=mock_role, task_include=mock_task_include)

    # Set necessary attributes for the test
    include_role._role_name = 'test_role'
    include_role._from_files = {'tasks': 'main.yml'}
    include_role._parent_role = mock_role
    include_role.rolespec_validate = True
    include_role.allow_duplicates = True
    include_role.public = False
    include_role.statically_loaded = False

    # Mock the RoleInclude.load method

# Generated at 2024-03-18 03:05:31.839012
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():    # Setup test data and mocks
    fake_loader = MagicMock()
    fake_variable_manager = MagicMock()
    fake_block = MagicMock()
    fake_role = MagicMock()
    fake_task_include = MagicMock()

    # Test data for IncludeRole.load
    test_data = {
        'name': 'testrole',
        'tasks_from': 'main.yml',
        'vars_from': 'vars/main.yml',
        'defaults_from': 'defaults/main.yml',
        'handlers_from': 'handlers/main.yml',
        'apply': {'tags': ['test']},
        'public': True,
        'allow_duplicates': False,
        'rolespec_validate': True
    }

    # Call IncludeRole.load with test data
    include_role = IncludeRole.load(
        data=test_data,
        block=fake_block,
        role=fake_role,
        task_include=fake_task_include,
        variable_manager=fake_variable_manager,
        loader=fake_loader
    )

    # Assertions to

# Generated at 2024-03-18 03:05:39.750992
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():    # Mock objects and data for testing
    mock_play = MagicMock()
    mock_variable_manager = MagicMock()
    mock_loader = MagicMock()
    mock_block = MagicMock()
    mock_role = MagicMock()
    mock_task_include = MagicMock()

    # Create an instance of IncludeRole
    include_role = IncludeRole(block=mock_block, role=mock_role, task_include=mock_task_include)

    # Set up the role name and path
    include_role._role_name = 'test_role'
    include_role._role_path = '/path/to/test_role'

    # Set up the _from_files to simulate `tasks_from` and other attributes
    include_role._from_files = {
        'tasks': 'main.yml',
        'vars': 'vars/main.yml',
        'defaults': 'defaults/main.yml',
        'handlers': 'handlers/main.yml'
    }

    # Set up the role to return a list of blocks and handlers
    mock_role.compile.return_value

# Generated at 2024-03-18 03:05:45.335839
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():    # Setup test data and mocks
    fake_loader = MagicMock()
    fake_variable_manager = MagicMock()
    fake_block = MagicMock()
    fake_role = MagicMock()
    fake_task_include = MagicMock()

    # Test data for IncludeRole.load
    test_data = {
        'name': 'testrole',
        'tasks_from': 'main.yml',
        'vars_from': 'vars/main.yml',
        'defaults_from': 'defaults/main.yml',
        'handlers_from': 'handlers/main.yml',
        'apply': {'delegate_to': 'localhost'},
        'public': True,
        'allow_duplicates': False,
        'rolespec_validate': True
    }

    # Expected results
    expected_from_files = {
        'tasks': 'main.yml',
        'vars': 'vars/main.yml',
        'defaults': 'defaults/main.yml',
        'handlers': 'handlers/main.yml'
    }

    # Call the method

# Generated at 2024-03-18 03:07:03.654719
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():    # Setup test data and mocks
    fake_loader = MagicMock()
    fake_variable_manager = MagicMock()
    fake_block = MagicMock()
    fake_role = MagicMock()
    fake_task_include = MagicMock()

    # Test data for IncludeRole.load
    test_data = {
        'name': 'testrole',
        'tasks_from': 'main.yml',
        'vars_from': 'vars/main.yml',
        'defaults_from': 'defaults/main.yml',
        'handlers_from': 'handlers/main.yml',
        'apply': {'delegate_to': 'localhost'},
        'public': True,
        'allow_duplicates': False,
        'rolespec_validate': True
    }

    # Expected results
    expected_from_files = {
        'tasks': 'main.yml',
        'vars': 'vars/main.yml',
        'defaults': 'defaults/main.yml',
        'handlers': 'handlers/main.yml'
    }

    # Call the method

# Generated at 2024-03-18 03:07:10.657161
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():    # Mock objects and data for testing
    mock_play = MagicMock()
    mock_variable_manager = MagicMock()
    mock_loader = MagicMock()
    mock_block = MagicMock()
    mock_role = MagicMock()
    mock_task_include = MagicMock()

    # Create an instance of IncludeRole
    include_role = IncludeRole(block=mock_block, role=mock_role, task_include=mock_task_include)

    # Set up the role name and path
    include_role._role_name = 'test_role'
    include_role._role_path = '/path/to/test_role'

    # Mock the RoleInclude.load method

# Generated at 2024-03-18 03:07:19.097837
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():    # Setup test data and mocks
    fake_loader = None
    fake_variable_manager = None
    fake_block = Block()
    fake_role = Role()
    fake_task_include = TaskInclude()

    # Test data for IncludeRole.load
    test_data = {
        'name': 'testrole',
        'tasks_from': 'main.yml',
        'vars_from': 'vars/main.yml',
        'defaults_from': 'defaults/main.yml',
        'handlers_from': 'handlers/main.yml',
        'apply': {'tags': ['test']},
        'public': True,
        'allow_duplicates': False,
        'rolespec_validate': True
    }

    # Call IncludeRole.load with test data
    include_role = IncludeRole.load(
        data=test_data,
        block=fake_block,
        role=fake_role,
        task_include=fake_task_include,
        variable_manager=fake_variable_manager,
        loader=fake_loader
    )

    # Assertions

# Generated at 2024-03-18 03:07:25.531939
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():    # Mock objects and data for testing
    mock_play = MagicMock()
    mock_variable_manager = MagicMock()
    mock_loader = MagicMock()
    mock_block = MagicMock()
    mock_role = MagicMock()
    mock_task_include = MagicMock()

    # Create an instance of IncludeRole
    include_role = IncludeRole(block=mock_block, role=mock_role, task_include=mock_task_include)

    # Set up the role name and path
    include_role._role_name = 'test_role'
    include_role._role_path = '/path/to/test_role'

    # Set up the _from_files to simulate `tasks_from`, `vars_from`, etc.
    include_role._from_files = {
        'tasks': 'main.yml',
        'vars': 'main.yml',
        'defaults': 'main.yml',
        'handlers': 'main.yml'
    }

    # Set up the return values for the mocked objects
    mock_play.handlers = []
    mock_role.compile

# Generated at 2024-03-18 03:07:31.361886
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():    # Setup test data and mocks
    fake_loader = MagicMock()
    fake_variable_manager = MagicMock()
    fake_block = MagicMock()
    fake_role = MagicMock()
    fake_task_include = MagicMock()

    # Test data for IncludeRole.load
    test_data = {
        'name': 'testrole',
        'tasks_from': 'main.yml',
        'vars_from': 'vars/main.yml',
        'defaults_from': 'defaults/main.yml',
        'handlers_from': 'handlers/main.yml',
        'apply': {'delegate_to': 'localhost'},
        'public': True,
        'allow_duplicates': False,
        'rolespec_validate': True
    }

    # Call IncludeRole.load with test data
    include_role = IncludeRole.load(
        data=test_data,
        block=fake_block,
        role=fake_role,
        task_include=fake_task_include,
        variable_manager=fake_variable_manager,
        loader=fake_loader
    )

    # Assertions

# Generated at 2024-03-18 03:07:37.653230
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():    # Setup the context for the test
    fake_loader = None
    fake_variable_manager = None
    fake_block = Block()
    fake_role = Role()
    fake_task_include = TaskInclude()

    # Test data
    test_data = {
        'name': 'testrole',
        'tasks_from': 'main.yml',
        'vars_from': 'vars/main.yml',
        'defaults_from': 'defaults/main.yml',
        'handlers_from': 'handlers/main.yml',
        'apply': {'tags': ['test']},
        'public': True,
        'allow_duplicates': False,
        'rolespec_validate': True
    }

    # Expected results
    expected_role_name = 'testrole'
    expected_from_files = {
        'tasks': 'main.yml',
        'vars': 'vars/main.yml',
        'defaults': 'defaults/main.yml',
        'handlers': 'handlers/main.yml'
    }

# Generated at 2024-03-18 03:07:43.861225
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():    # Setup test data and mocks
    fake_loader = MagicMock()
    fake_variable_manager = MagicMock()
    fake_block = MagicMock()
    fake_role = MagicMock()
    fake_task_include = MagicMock()

    # Test data for IncludeRole.load
    test_data = {
        'name': 'testrole',
        'tasks_from': 'main.yml',
        'vars_from': 'vars/main.yml',
        'defaults_from': 'defaults/main.yml',
        'handlers_from': 'handlers/main.yml',
        'apply': {'delegate_to': 'localhost'},
        'public': True,
        'allow_duplicates': False,
        'rolespec_validate': True
    }

    # Expected results
    expected_from_files = {
        'tasks': 'main.yml',
        'vars': 'vars/main.yml',
        'defaults': 'defaults/main.yml',
        'handlers': 'handlers/main.yml'
    }

    # Call the method

# Generated at 2024-03-18 03:07:52.034564
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():    # Setup test data and mocks
    fake_loader = MagicMock()
    fake_variable_manager = MagicMock()
    fake_block = MagicMock()
    fake_role = MagicMock()
    fake_task_include = MagicMock()

    # Test data for IncludeRole.load
    test_data = {
        'name': 'testrole',
        'tasks_from': 'main.yml',
        'vars_from': 'vars/main.yml',
        'defaults_from': 'defaults/main.yml',
        'handlers_from': 'handlers/main.yml',
        'apply': {'tags': ['test']},
        'public': True,
        'allow_duplicates': False,
        'rolespec_validate': True
    }

    # Call IncludeRole.load with test data
    include_role = IncludeRole.load(
        data=test_data,
        block=fake_block,
        role=fake_role,
        task_include=fake_task_include,
        variable_manager=fake_variable_manager,
        loader=fake_loader
    )

    # Assertions to

# Generated at 2024-03-18 03:07:58.483551
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():    # Mock objects and data for testing
    mock_play = MagicMock()
    mock_variable_manager = MagicMock()
    mock_loader = MagicMock()
    mock_block = MagicMock()
    mock_role = MagicMock()
    mock_task_include = MagicMock()

    # Create an instance of IncludeRole
    include_role = IncludeRole(block=mock_block, role=mock_role, task_include=mock_task_include)

    # Set necessary attributes for the IncludeRole instance
    include_role._role_name = 'test_role'
    include_role._from_files = {'tasks': 'main.yml'}
    include_role._parent_role = mock_role
    include_role.rolespec_validate = True
    include_role.allow_duplicates = True
    include_role.public = False
    include_role.statically_loaded = False

    # Mock the Role.load method to return a mock role object
    mock_loaded_role = MagicMock()
    mock_loaded_role.compile.return_value = [mock_block]
    mock_loaded_role.get_handler

# Generated at 2024-03-18 03:08:07.875150
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():    # Mock objects and data for testing
    mock_play = MagicMock()
    mock_variable_manager = MagicMock()
    mock_loader = MagicMock()
    mock_role = MagicMock()
    mock_block = MagicMock()
    mock_task_include = MagicMock()

    # Create an instance of IncludeRole
    include_role = IncludeRole(block=mock_block, role=mock_role, task_include=mock_task_include)

    # Set up the role name and from_files for the include_role instance
    include_role._role_name = 'test_role'
    include_role._from_files = {'tasks': 'main.yml'}

    # Mock the RoleInclude.load method