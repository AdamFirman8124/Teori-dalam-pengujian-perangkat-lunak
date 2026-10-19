

# Generated at 2024-05-31 22:11:46.445713
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():    # Setup
    block = Block()
    role = Role()
    task_include = TaskInclude()
    include_role = IncludeRole(block=block, role=role, task_include=task_include)
    play = None
    variable_manager = None
    loader = None

    # Mocking RoleInclude.load
    def mock_role_include_load(role_name, play, variable_manager, loader, collection_list):
        class MockRoleInclude:
            def __init__(self):
                self.vars = {}
        return MockRoleInclude()
    
    # Mocking Role.load
    def mock_role_load(ri, play, parent_role, from_files, from_include, validate):
        class MockRole:
            def __init__(self):
                self._role_path = "/mock/role/path"
                self._metadata = type('metadata', (object,), {'allow_duplicates': True})
                self.collections = []

# Generated at 2024-05-31 22:11:49.464598
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():    data = {
        'name': 'test_role',
        'apply': {'some_key': 'some_value'},
        'tasks_from': 'tasks/main.yml',
        'vars_from': 'vars/main.yml',
        'defaults_from': 'defaults/main.yml',
        'handlers_from': 'handlers/main.yml',
        'public': True,
        'allow_duplicates': False,
        'rolespec_validate': True
    }

# Generated at 2024-05-31 22:11:52.508980
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():    data = {
        'name': 'test_role',
        'apply': {'some_key': 'some_value'},
        'public': True,
        'tasks_from': 'tasks/main.yml'
    }

# Generated at 2024-05-31 22:11:56.913677
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():    data = {
        'name': 'test_role',
        'role': 'test_role',
        'tasks_from': 'tasks/main.yml',
        'vars_from': 'vars/main.yml',
        'defaults_from': 'defaults/main.yml',
        'handlers_from': 'handlers/main.yml',
        'apply': {'some_key': 'some_value'},
        'public': True,
        'allow_duplicates': False,
        'rolespec_validate': True
    }

# Generated at 2024-05-31 22:11:59.314800
# Unit test for method get_include_params of class IncludeRole
def test_IncludeRole_get_include_params():    parent_role = Role()

# Generated at 2024-05-31 22:12:00.887170
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():    block = Block()

# Generated at 2024-05-31 22:12:03.103572
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():    block = Block()

# Generated at 2024-05-31 22:12:06.022301
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():    data = {
        'name': 'test_role',
        'role': 'test_role',
        'tasks_from': 'tasks/main.yml',
        'vars_from': 'vars/main.yml',
        'defaults_from': 'defaults/main.yml',
        'handlers_from': 'handlers/main.yml',
        'apply': {'some_option': 'some_value'},
        'public': True,
        'allow_duplicates': False,
        'rolespec_validate': True
    }

# Generated at 2024-05-31 22:12:09.565923
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():    data = {
        'name': 'test_role',
        'apply': {'some_key': 'some_value'},
        'tasks_from': 'tasks/main.yml',
        'vars_from': 'vars/main.yml',
        'defaults_from': 'defaults/main.yml',
        'handlers_from': 'handlers/main.yml',
        'public': True,
        'allow_duplicates': False,
        'rolespec_validate': True
    }

# Generated at 2024-05-31 22:12:11.755069
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():    block = Block()

# Generated at 2024-05-31 22:12:20.547975
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():    data = {
        'name': 'test_role',
        'apply': {'some_key': 'some_value'},
        'public': True,
        'tasks_from': 'tasks/main.yml'
    }

# Generated at 2024-05-31 22:12:22.521827
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():    # Setup
    block = Block()
    role = Role()
    task_include = TaskInclude()
    include_role = IncludeRole(block=block, role=role, task_include=task_include)
    play = None
    variable_manager = None
    loader = None

    # Execute
    blocks, handlers = include_role.get_block_list(play=play, variable_manager=variable_manager, loader=loader)

    # Verify
    assert isinstance(blocks, list)
    assert isinstance(handlers, list)


# Generated at 2024-05-31 22:12:24.434489
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():    block = Block()

# Generated at 2024-05-31 22:12:26.080666
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():    block = Block()

# Generated at 2024-05-31 22:12:29.247360
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():    data = {
        'name': 'test_role',
        'role': 'test_role',
        'tasks_from': 'tasks/main.yml',
        'vars_from': 'vars/main.yml',
        'defaults_from': 'defaults/main.yml',
        'handlers_from': 'handlers/main.yml',
        'apply': {'some_option': 'some_value'},
        'public': True,
        'allow_duplicates': False,
        'rolespec_validate': True
    }

# Generated at 2024-05-31 22:12:30.988243
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():    block = Block()

# Generated at 2024-05-31 22:12:33.247332
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():    data = {
        'name': 'test_role',
        'apply': {'some_key': 'some_value'},
        'public': True,
        'tasks_from': 'tasks/main.yml'
    }

# Generated at 2024-05-31 22:12:34.998666
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():    block = Block()

# Generated at 2024-05-31 22:12:38.156798
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():    data = {
        'name': 'test_role',
        'role': 'test_role',
        'tasks_from': 'tasks/main.yml',
        'vars_from': 'vars/main.yml',
        'defaults_from': 'defaults/main.yml',
        'handlers_from': 'handlers/main.yml',
        'apply': {'some_key': 'some_value'},
        'public': True,
        'allow_duplicates': False,
        'rolespec_validate': True
    }

# Generated at 2024-05-31 22:12:40.075249
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():    block = Block()

# Generated at 2024-05-31 22:12:47.866253
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():    block = Block()

# Generated at 2024-05-31 22:12:50.102333
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():    data = {
        'name': 'test_role',
        'apply': {'some_key': 'some_value'},
        'public': True,
        'tasks_from': 'tasks/main.yml'
    }

# Generated at 2024-05-31 22:12:52.552444
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():    data = {
        'name': 'test_role',
        'apply': {'some_key': 'some_value'},
        'public': True,
        'tasks_from': 'tasks/main.yml'
    }

# Generated at 2024-05-31 22:12:56.863446
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():    # Setup
    block = Block()
    role = Role()
    task_include = TaskInclude()
    include_role = IncludeRole(block=block, role=role, task_include=task_include)
    play = None
    variable_manager = None
    loader = None

    # Mock methods and attributes
    include_role._parent = type('obj', (object,), {'_play': 'mock_play'})
    include_role._role_name = 'mock_role_name'
    include_role.vars = {}
    include_role.collections = []
    include_role.statically_loaded = False
    include_role.public = False
    include_role.allow_duplicates = True
    include_role.rolespec_validate = True

    RoleInclude.load = lambda *args, **kwargs: type('obj', (object,), {'vars': {}})

# Generated at 2024-05-31 22:12:59.995478
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():    data = {
        'name': 'test_role',
        'role': 'test_role',
        'tasks_from': 'tasks/main.yml',
        'vars_from': 'vars/main.yml',
        'defaults_from': 'defaults/main.yml',
        'handlers_from': 'handlers/main.yml',
        'apply': {'some_option': 'some_value'},
        'public': True,
        'allow_duplicates': False,
        'rolespec_validate': True
    }

# Generated at 2024-05-31 22:13:02.563147
# Unit test for method get_include_params of class IncludeRole
def test_IncludeRole_get_include_params():    parent_role = Role()

# Generated at 2024-05-31 22:13:05.113864
# Unit test for method get_include_params of class IncludeRole
def test_IncludeRole_get_include_params():    parent_role = Role()

# Generated at 2024-05-31 22:13:07.336773
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():    data = {
        'name': 'test_role',
        'apply': {'some_key': 'some_value'},
        'public': True,
        'tasks_from': 'tasks/main.yml'
    }

# Generated at 2024-05-31 22:13:09.873109
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():    block = Block()

# Generated at 2024-05-31 22:13:12.715086
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():    data = {
        'name': 'test_role',
        'role': 'test_role',
        'tasks_from': 'tasks/main.yml',
        'vars_from': 'vars/main.yml',
        'defaults_from': 'defaults/main.yml',
        'handlers_from': 'handlers/main.yml',
        'apply': {'some_option': 'some_value'},
        'public': True,
        'allow_duplicates': False,
        'rolespec_validate': True
    }

# Generated at 2024-05-31 22:13:21.662926
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():    data = {
        'name': 'test_role',
        'apply': {'some_key': 'some_value'},
        'public': True,
        'tasks_from': 'tasks/main.yml'
    }

# Generated at 2024-05-31 22:13:24.052192
# Unit test for method get_include_params of class IncludeRole
def test_IncludeRole_get_include_params():    parent_role = Role()

# Generated at 2024-05-31 22:13:26.073879
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():    block = Block()

# Generated at 2024-05-31 22:13:28.933030
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():    data = {
        'name': 'test_role',
        'role': 'test_role',
        'tasks_from': 'tasks/main.yml',
        'vars_from': 'vars/main.yml',
        'defaults_from': 'defaults/main.yml',
        'handlers_from': 'handlers/main.yml',
        'apply': {'some_option': 'some_value'},
        'public': True,
        'allow_duplicates': False,
        'rolespec_validate': True
    }

# Generated at 2024-05-31 22:13:31.454712
# Unit test for method get_include_params of class IncludeRole
def test_IncludeRole_get_include_params():    parent_role = Role()

# Generated at 2024-05-31 22:13:35.035396
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():    data = {
        'name': 'test_role',
        'role': 'test_role',
        'tasks_from': 'tasks/main.yml',
        'vars_from': 'vars/main.yml',
        'defaults_from': 'defaults/main.yml',
        'handlers_from': 'handlers/main.yml',
        'apply': {'some_option': 'some_value'},
        'public': True,
        'allow_duplicates': False,
        'rolespec_validate': True
    }

# Generated at 2024-05-31 22:13:37.146294
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():    data = {
        'name': 'test_role',
        'apply': {'some_key': 'some_value'},
        'public': True,
        'tasks_from': 'tasks/main.yml'
    }

# Generated at 2024-05-31 22:13:40.163378
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():    data = {
        'name': 'test_role',
        'role': 'test_role',
        'tasks_from': 'tasks/main.yml',
        'vars_from': 'vars/main.yml',
        'defaults_from': 'defaults/main.yml',
        'handlers_from': 'handlers/main.yml',
        'apply': {'some_option': 'some_value'},
        'public': True,
        'allow_duplicates': False,
        'rolespec_validate': True
    }

# Generated at 2024-05-31 22:13:41.936778
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():    block = Block()

# Generated at 2024-05-31 22:13:48.477312
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():    data = {
        'name': 'test_role',
        'role': 'test_role',
        'tasks_from': 'tasks/main.yml',
        'vars_from': 'vars/main.yml',
        'defaults_from': 'defaults/main.yml',
        'handlers_from': 'handlers/main.yml',
        'apply': {'some_option': 'some_value'},
        'public': True,
        'allow_duplicates': False,
        'rolespec_validate': True
    }

# Generated at 2024-05-31 22:13:56.203812
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():    block = Block()

# Generated at 2024-05-31 22:13:57.923665
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():    block = Block()

# Generated at 2024-05-31 22:14:01.060019
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():    data = {
        'name': 'test_role',
        'role': 'test_role',
        'tasks_from': 'tasks/main.yml',
        'vars_from': 'vars/main.yml',
        'defaults_from': 'defaults/main.yml',
        'handlers_from': 'handlers/main.yml',
        'apply': {'some_option': 'some_value'},
        'public': True,
        'allow_duplicates': False,
        'rolespec_validate': True
    }

# Generated at 2024-05-31 22:14:03.677011
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():    block = Block()

# Generated at 2024-05-31 22:14:05.430629
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():    block = Block()

# Generated at 2024-05-31 22:14:08.426675
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():    data = {
        'name': 'test_role',
        'role': 'test_role',
        'tasks_from': 'tasks/main.yml',
        'vars_from': 'vars/main.yml',
        'defaults_from': 'defaults/main.yml',
        'handlers_from': 'handlers/main.yml',
        'apply': {'some_option': 'some_value'},
        'public': True,
        'allow_duplicates': False,
        'rolespec_validate': True
    }

# Generated at 2024-05-31 22:14:10.990426
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():    data = {
        'name': 'test_role',
        'role': 'test_role',
        'tasks_from': 'tasks/main.yml',
        'vars_from': 'vars/main.yml',
        'defaults_from': 'defaults/main.yml',
        'handlers_from': 'handlers/main.yml',
        'apply': {'some_option': 'some_value'},
        'public': True,
        'allow_duplicates': False,
        'rolespec_validate': True
    }

# Generated at 2024-05-31 22:14:13.266606
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():    data = {
        'name': 'test_role',
        'apply': {'some_key': 'some_value'},
        'public': True,
        'tasks_from': 'tasks/main.yml'
    }

# Generated at 2024-05-31 22:14:16.383706
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():    data = {
        'name': 'test_role',
        'role': 'test_role',
        'tasks_from': 'tasks/main.yml',
        'vars_from': 'vars/main.yml',
        'defaults_from': 'defaults/main.yml',
        'handlers_from': 'handlers/main.yml',
        'apply': {'some_option': 'some_value'},
        'public': True,
        'allow_duplicates': False,
        'rolespec_validate': True
    }

# Generated at 2024-05-31 22:14:23.029221
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():    data = {
        'name': 'test_role',
        'role': 'test_role',
        'tasks_from': 'tasks/main.yml',
        'vars_from': 'vars/main.yml',
        'defaults_from': 'defaults/main.yml',
        'handlers_from': 'handlers/main.yml',
        'apply': {'some_option': 'some_value'},
        'public': True,
        'allow_duplicates': False,
        'rolespec_validate': True
    }

# Generated at 2024-05-31 22:14:32.585938
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():    data = {
        'name': 'test_role',
        'role': 'test_role',
        'tasks_from': 'tasks/main.yml',
        'vars_from': 'vars/main.yml',
        'defaults_from': 'defaults/main.yml',
        'handlers_from': 'handlers/main.yml',
        'apply': {'some_option': 'some_value'},
        'public': True,
        'allow_duplicates': False,
        'rolespec_validate': True
    }

# Generated at 2024-05-31 22:14:36.540599
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():    data = {
        'name': 'test_role',
        'role': 'test_role',
        'tasks_from': 'tasks/main.yml',
        'vars_from': 'vars/main.yml',
        'defaults_from': 'defaults/main.yml',
        'handlers_from': 'handlers/main.yml',
        'apply': {'some_option': 'some_value'},
        'public': True,
        'allow_duplicates': False,
        'rolespec_validate': True
    }

# Generated at 2024-05-31 22:14:39.829343
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():    # Setup
    block = Block()
    role = Role()
    task_include = TaskInclude()
    include_role = IncludeRole(block=block, role=role, task_include=task_include)
    play = None
    variable_manager = None
    loader = None

    # Mocking RoleInclude.load
    def mock_role_include_load(role_name, play, variable_manager, loader, collection_list):
        class MockRoleInclude:
            def __init__(self):
                self.vars = {}
        return MockRoleInclude()
    
    # Mocking Role.load
    def mock_role_load(ri, play, parent_role, from_files, from_include, validate):
        class MockRole:
            def __init__(self):
                self._role_path = "/mock/role/path"
                self._metadata = type('metadata', (object,), {'allow_duplicates': True})
                self.collections = []

# Generated at 2024-05-31 22:14:44.216068
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():    # Setup
    block = Block()
    role = Role()
    task_include = TaskInclude()
    include_role = IncludeRole(block=block, role=role, task_include=task_include)
    play = None
    variable_manager = None
    loader = None

    # Mocking RoleInclude.load
    def mock_role_include_load(role_name, play, variable_manager, loader, collection_list):
        class MockRoleInclude:
            def __init__(self):
                self.vars = {}
        return MockRoleInclude()
    RoleInclude.load = mock_role_include_load

    # Mocking Role.load
    def mock_role_load(ri, play, parent_role, from_files, from_include, validate):
        class MockRole:
            def __init__(self):
                self._role_path = "/mock/role/path"
                self._metadata = type('obj', (object,), {'allow_duplicates': True})
                self.collections = []

# Generated at 2024-05-31 22:14:48.860783
# Unit test for method get_include_params of class IncludeRole
def test_IncludeRole_get_include_params():    parent_role = Role()

# Generated at 2024-05-31 22:14:52.668643
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():    data = {
        'name': 'test_role',
        'apply': {'some_key': 'some_value'},
        'tasks_from': 'tasks/main.yml',
        'vars_from': 'vars/main.yml',
        'defaults_from': 'defaults/main.yml',
        'handlers_from': 'handlers/main.yml',
        'public': True,
        'allow_duplicates': False,
        'rolespec_validate': True
    }

# Generated at 2024-05-31 22:14:54.934308
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():    block = Block()

# Generated at 2024-05-31 22:14:57.993378
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():    block = Block()

# Generated at 2024-05-31 22:15:00.461014
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():    block = Block()

# Generated at 2024-05-31 22:15:03.016976
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():    block = Block()

# Generated at 2024-05-31 22:15:12.169183
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():    data = {
        'name': 'test_role',
        'role': 'test_role',
        'tasks_from': 'tasks/main.yml',
        'vars_from': 'vars/main.yml',
        'defaults_from': 'defaults/main.yml',
        'handlers_from': 'handlers/main.yml',
        'apply': {'some_key': 'some_value'},
        'public': True,
        'allow_duplicates': False,
        'rolespec_validate': True
    }

# Generated at 2024-05-31 22:15:15.137029
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():    block = Block()

# Generated at 2024-05-31 22:15:17.047167
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():    block = Block()

# Generated at 2024-05-31 22:15:19.907281
# Unit test for method get_include_params of class IncludeRole
def test_IncludeRole_get_include_params():    parent_role = Role()

# Generated at 2024-05-31 22:15:21.723052
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():    block = Block()

# Generated at 2024-05-31 22:15:23.745278
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():    block = Block()

# Generated at 2024-05-31 22:15:26.945844
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():    data = {
        'name': 'test_role',
        'role': 'test_role',
        'tasks_from': 'tasks/main.yml',
        'vars_from': 'vars/main.yml',
        'defaults_from': 'defaults/main.yml',
        'handlers_from': 'handlers/main.yml',
        'apply': {'some_option': 'some_value'},
        'public': True,
        'allow_duplicates': False,
        'rolespec_validate': True
    }

# Generated at 2024-05-31 22:15:28.649330
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():    block = Block()

# Generated at 2024-05-31 22:15:32.475223
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():    data = {
        'name': 'test_role',
        'apply': {'some_key': 'some_value'},
        'tasks_from': 'tasks/main.yml',
        'vars_from': 'vars/main.yml',
        'defaults_from': 'defaults/main.yml',
        'handlers_from': 'handlers/main.yml',
        'public': True,
        'allow_duplicates': False,
        'rolespec_validate': True
    }

# Generated at 2024-05-31 22:15:34.531159
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():    block = Block()

# Generated at 2024-05-31 22:15:44.360711
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():    block = Block()

# Generated at 2024-05-31 22:15:46.781151
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():    data = {
        'name': 'test_role',
        'apply': {'some_key': 'some_value'},
        'public': True,
        'tasks_from': 'tasks/main.yml'
    }

# Generated at 2024-05-31 22:15:49.427669
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():    data = {
        'name': 'test_role',
        'apply': {'some_key': 'some_value'},
        'public': True,
        'tasks_from': 'tasks/main.yml'
    }

# Generated at 2024-05-31 22:15:51.193687
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():    block = Block()

# Generated at 2024-05-31 22:15:54.224412
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():    # Setup
    block = Block()
    role = Role()
    task_include = TaskInclude()
    include_role = IncludeRole(block=block, role=role, task_include=task_include)
    play = None
    variable_manager = None
    loader = None

    # Mocking RoleInclude.load
    def mock_role_include_load(role_name, play, variable_manager, loader, collection_list):
        class MockRoleInclude:
            def __init__(self):
                self.vars = {}
        return MockRoleInclude()
    
    # Mocking Role.load
    def mock_role_load(ri, play, parent_role, from_files, from_include, validate):
        class MockRole:
            def __init__(self):
                self._role_path = "/mock/role/path"
                self._metadata = type('metadata', (object,), {'allow_duplicates': True})
                self.collections = []

# Generated at 2024-05-31 22:15:57.171466
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():    data = {
        'name': 'test_role',
        'role': 'test_role',
        'tasks_from': 'tasks/main.yml',
        'vars_from': 'vars/main.yml',
        'defaults_from': 'defaults/main.yml',
        'handlers_from': 'handlers/main.yml',
        'apply': {'some_option': 'some_value'},
        'public': True,
        'allow_duplicates': False,
        'rolespec_validate': True
    }

# Generated at 2024-05-31 22:16:07.744711
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():    data = {
        'name': 'test_role',
        'role': 'test_role',
        'tasks_from': 'tasks/main.yml',
        'vars_from': 'vars/main.yml',
        'defaults_from': 'defaults/main.yml',
        'handlers_from': 'handlers/main.yml',
        'apply': {'some_option': 'some_value'},
        'public': True,
        'allow_duplicates': False,
        'rolespec_validate': True
    }

# Generated at 2024-05-31 22:16:11.084831
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():    data = {
        'name': 'test_role',
        'apply': {'some_key': 'some_value'},
        'public': True,
        'tasks_from': 'tasks/main.yml'
    }

# Generated at 2024-05-31 22:16:14.052814
# Unit test for method get_include_params of class IncludeRole
def test_IncludeRole_get_include_params():    parent_role = Role()

# Generated at 2024-05-31 22:16:21.509202
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():    data = {
        'name': 'test_role',
        'role': 'test_role',
        'tasks_from': 'tasks/main.yml',
        'vars_from': 'vars/main.yml',
        'defaults_from': 'defaults/main.yml',
        'handlers_from': 'handlers/main.yml',
        'apply': {'some_option': 'some_value'},
        'public': True,
        'allow_duplicates': False,
        'rolespec_validate': True
    }

# Generated at 2024-05-31 22:16:29.893496
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():    block = Block()

# Generated at 2024-05-31 22:16:33.162842
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():    data = {
        'name': 'test_role',
        'role': 'test_role',
        'tasks_from': 'tasks/main.yml',
        'vars_from': 'vars/main.yml',
        'defaults_from': 'defaults/main.yml',
        'handlers_from': 'handlers/main.yml',
        'apply': {'some_option': 'some_value'},
        'public': True,
        'allow_duplicates': False,
        'rolespec_validate': True
    }

# Generated at 2024-05-31 22:16:38.429708
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():    # Setup
    block = Block()
    role = Role()
    task_include = TaskInclude()
    include_role = IncludeRole(block=block, role=role, task_include=task_include)
    play = None
    variable_manager = None
    loader = None

    # Mock RoleInclude.load
    def mock_role_include_load(role_name, play, variable_manager, loader, collection_list):
        class MockRoleInclude:
            def __init__(self):
                self.vars = {}
        return MockRoleInclude()
    RoleInclude.load = mock_role_include_load

    # Mock Role.load
    def mock_role_load(ri, play, parent_role, from_files, from_include, validate):
        class MockRole:
            def __init__(self):
                self._role_path = "/mock/role/path"
                self._metadata = type('metadata', (object,), {'allow_duplicates': True})
                self.collections = []

# Generated at 2024-05-31 22:16:40.921113
# Unit test for method get_include_params of class IncludeRole
def test_IncludeRole_get_include_params():    parent_role = Role()

# Generated at 2024-05-31 22:16:44.260783
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():    data = {
        'name': 'test_role',
        'role': 'test_role',
        'tasks_from': 'tasks/main.yml',
        'vars_from': 'vars/main.yml',
        'defaults_from': 'defaults/main.yml',
        'handlers_from': 'handlers/main.yml',
        'apply': {'some_option': 'some_value'},
        'public': True,
        'allow_duplicates': False,
        'rolespec_validate': True
    }

# Generated at 2024-05-31 22:16:46.227762
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():    block = Block()

# Generated at 2024-05-31 22:16:49.453520
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():    data = {
        'name': 'test_role',
        'role': 'test_role',
        'tasks_from': 'tasks/main.yml',
        'vars_from': 'vars/main.yml',
        'defaults_from': 'defaults/main.yml',
        'handlers_from': 'handlers/main.yml',
        'apply': {'some_option': 'some_value'},
        'public': True,
        'allow_duplicates': False,
        'rolespec_validate': True
    }

# Generated at 2024-05-31 22:16:52.661160
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():    data = {
        'name': 'test_role',
        'apply': {'some_key': 'some_value'},
        'tasks_from': 'tasks/main.yml',
        'vars_from': 'vars/main.yml',
        'defaults_from': 'defaults/main.yml',
        'handlers_from': 'handlers/main.yml',
        'public': True,
        'allow_duplicates': False,
        'rolespec_validate': True
    }

# Generated at 2024-05-31 22:16:54.553708
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():    block = Block()

# Generated at 2024-05-31 22:16:56.831035
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():    data = {
        'name': 'test_role',
        'apply': {'some_key': 'some_value'},
        'public': True,
        'tasks_from': 'tasks/main.yml'
    }

# Generated at 2024-05-31 22:17:04.931670
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():    block = Block()

# Generated at 2024-05-31 22:17:07.937625
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():    data = {
        'name': 'test_role',
        'role': 'test_role',
        'tasks_from': 'tasks/main.yml',
        'vars_from': 'vars/main.yml',
        'defaults_from': 'defaults/main.yml',
        'handlers_from': 'handlers/main.yml',
        'apply': {'some_option': 'some_value'},
        'public': True,
        'allow_duplicates': False,
        'rolespec_validate': True
    }

# Generated at 2024-05-31 22:17:11.230880
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():    block = Block()

# Generated at 2024-05-31 22:17:13.786686
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():    data = {
        'name': 'test_role',
        'apply': {'some_key': 'some_value'},
        'public': True,
        'tasks_from': 'tasks/main.yml'
    }

# Generated at 2024-05-31 22:17:16.995322
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():    block = Block()

# Generated at 2024-05-31 22:17:21.644285
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():    data = {
        'name': 'test_role',
        'apply': {'some_key': 'some_value'},
        'tasks_from': 'tasks/main.yml',
        'vars_from': 'vars/main.yml',
        'defaults_from': 'defaults/main.yml',
        'handlers_from': 'handlers/main.yml',
        'public': True,
        'allow_duplicates': False,
        'rolespec_validate': True
    }

# Generated at 2024-05-31 22:17:29.877989
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():    # Setup
    block = Block()
    role = Role()
    task_include = TaskInclude()
    include_role = IncludeRole(block=block, role=role, task_include=task_include)
    play = None
    variable_manager = None
    loader = None

    # Mock RoleInclude.load
    def mock_role_include_load(role_name, play, variable_manager, loader, collection_list):
        class MockRoleInclude:
            def __init__(self):
                self.vars = {}
        return MockRoleInclude()
    RoleInclude.load = mock_role_include_load

    # Mock Role.load
    def mock_role_load(ri, play, parent_role, from_files, from_include, validate):
        class MockRole:
            def __init__(self):
                self._role_path = "/mock/role/path"
                self._metadata = type('obj', (object,), {'allow_duplicates': True})
                self.collections = []

# Generated at 2024-05-31 22:17:32.240839
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():    block = Block()

# Generated at 2024-05-31 22:17:35.014065
# Unit test for method get_include_params of class IncludeRole
def test_IncludeRole_get_include_params():    parent_role = Role()

# Generated at 2024-05-31 22:17:37.270143
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():    data = {
        'name': 'test_role',
        'apply': {'some_key': 'some_value'},
        'public': True,
        'tasks_from': 'tasks/main.yml'
    }

# Generated at 2024-05-31 22:17:46.264128
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():    data = {
        'name': 'test_role',
        'role': 'test_role',
        'tasks_from': 'tasks/main.yml',
        'vars_from': 'vars/main.yml',
        'defaults_from': 'defaults/main.yml',
        'handlers_from': 'handlers/main.yml',
        'apply': {'some_key': 'some_value'},
        'public': True,
        'allow_duplicates': False,
        'rolespec_validate': True
    }

# Generated at 2024-05-31 22:17:49.618717
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():    data = {
        'name': 'test_role',
        'apply': {'some_key': 'some_value'},
        'tasks_from': 'tasks/main.yml',
        'vars_from': 'vars/main.yml',
        'defaults_from': 'defaults/main.yml',
        'handlers_from': 'handlers/main.yml',
        'public': True,
        'allow_duplicates': False,
        'rolespec_validate': True
    }

# Generated at 2024-05-31 22:17:51.440726
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():    block = Block()

# Generated at 2024-05-31 22:17:56.559796
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():    data = {
        'name': 'test_role',
        'apply': {'some_key': 'some_value'},
        'tasks_from': 'tasks/main.yml',
        'vars_from': 'vars/main.yml',
        'defaults_from': 'defaults/main.yml',
        'handlers_from': 'handlers/main.yml',
        'public': True,
        'allow_duplicates': False,
        'rolespec_validate': True
    }

# Generated at 2024-05-31 22:17:58.204477
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():    block = Block()

# Generated at 2024-05-31 22:18:01.665632
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():    data = {
        'name': 'test_role',
        'role': 'test_role',
        'tasks_from': 'tasks/main.yml',
        'vars_from': 'vars/main.yml',
        'defaults_from': 'defaults/main.yml',
        'handlers_from': 'handlers/main.yml',
        'apply': {'some_option': 'some_value'},
        'public': True,
        'allow_duplicates': False,
        'rolespec_validate': True
    }

# Generated at 2024-05-31 22:18:03.419746
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():    block = Block()

# Generated at 2024-05-31 22:18:05.141193
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():    block = Block()

# Generated at 2024-05-31 22:18:06.799923
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():    block = Block()

# Generated at 2024-05-31 22:18:10.059284
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():    data = {
        'name': 'test_role',
        'apply': {'some_key': 'some_value'},
        'tasks_from': 'tasks/main.yml',
        'vars_from': 'vars/main.yml',
        'defaults_from': 'defaults/main.yml',
        'handlers_from': 'handlers/main.yml',
        'public': True,
        'allow_duplicates': False,
        'rolespec_validate': True
    }

# Generated at 2024-05-31 22:18:18.726326
# Unit test for method get_include_params of class IncludeRole
def test_IncludeRole_get_include_params():    parent_role = Role()

# Generated at 2024-05-31 22:18:20.399663
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():    block = Block()

# Generated at 2024-05-31 22:18:22.136334
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():    block = Block()

# Generated at 2024-05-31 22:18:24.594956
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():    data = {
        'name': 'test_role',
        'apply': {'some_key': 'some_value'},
        'public': True,
        'tasks_from': 'tasks/main.yml'
    }

# Generated at 2024-05-31 22:18:27.781724
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():    data = {
        'name': 'test_role',
        'apply': {'some_key': 'some_value'},
        'public': True,
        'tasks_from': 'tasks/main.yml'
    }

# Generated at 2024-05-31 22:18:32.801423
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():    # Setup
    block = Block()
    role = Role()
    task_include = TaskInclude()
    include_role = IncludeRole(block=block, role=role, task_include=task_include)
    play = None
    variable_manager = None
    loader = None

    # Mocking RoleInclude.load
    def mock_role_include_load(role_name, play, variable_manager, loader, collection_list):
        class MockRoleInclude:
            def __init__(self):
                self.vars = {}
        return MockRoleInclude()
    RoleInclude.load = mock_role_include_load

    # Mocking Role.load
    def mock_role_load(ri, play, parent_role, from_files, from_include, validate):
        class MockRole:
            def __init__(self):
                self._role_path = "/mock/role/path"
                self._metadata = type('metadata', (object,), {'allow_duplicates': True})
                self.collections = []

# Generated at 2024-05-31 22:18:36.880800
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():    # Setup
    block = Block()
    role = Role()
    task_include = TaskInclude()
    include_role = IncludeRole(block=block, role=role, task_include=task_include)
    play = None
    variable_manager = None
    loader = None

    # Mocking RoleInclude.load
    def mock_role_include_load(role_name, play, variable_manager, loader, collection_list):
        class MockRoleInclude:
            def __init__(self):
                self.vars = {}
        return MockRoleInclude()
    
    RoleInclude.load = mock_role_include_load

    # Mocking Role.load
    def mock_role_load(ri, play, parent_role, from_files, from_include, validate):
        class MockRole:
            def __init__(self):
                self._role_path = "/mock/role/path"
                self._metadata = type('obj', (object,), {'allow_duplicates': True})
                self.collections = []

# Generated at 2024-05-31 22:18:39.764720
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():    data = {
        'name': 'test_role',
        'apply': {'some_key': 'some_value'},
        'public': True,
        'tasks_from': 'tasks/main.yml'
    }

# Generated at 2024-05-31 22:18:42.909039
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():    data = {
        'name': 'test_role',
        'apply': {'some_key': 'some_value'},
        'tasks_from': 'tasks/main.yml',
        'vars_from': 'vars/main.yml',
        'defaults_from': 'defaults/main.yml',
        'handlers_from': 'handlers/main.yml',
        'public': True,
        'allow_duplicates': False,
        'rolespec_validate': True
    }

# Generated at 2024-05-31 22:18:46.434236
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():    data = {
        'name': 'test_role',
        'role': 'test_role',
        'tasks_from': 'tasks/main.yml',
        'vars_from': 'vars/main.yml',
        'defaults_from': 'defaults/main.yml',
        'handlers_from': 'handlers/main.yml',
        'apply': {'some_key': 'some_value'},
        'public': True,
        'allow_duplicates': False,
        'rolespec_validate': True
    }

# Generated at 2024-05-31 22:18:58.269243
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():    block = Block()

# Generated at 2024-05-31 22:19:03.412639
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():    # Setup
    block = Block()
    role = Role()
    task_include = TaskInclude()
    include_role = IncludeRole(block=block, role=role, task_include=task_include)
    play = None
    variable_manager = None
    loader = None

    # Mock RoleInclude.load
    def mock_role_include_load(role_name, play, variable_manager, loader, collection_list):
        class MockRoleInclude:
            def __init__(self):
                self.vars = {}
        return MockRoleInclude()
    RoleInclude.load = mock_role_include_load

    # Mock Role.load
    def mock_role_load(ri, play, parent_role, from_files, from_include, validate):
        class MockRole:
            def __init__(self):
                self._role_path = "/mock/role/path"
                self._metadata = type('obj', (object,), {'allow_duplicates': True})
                self.collections = []

# Generated at 2024-05-31 22:19:07.053135
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():    data = {
        'name': 'test_role',
        'apply': {'some_key': 'some_value'},
        'public': True,
        'tasks_from': 'tasks/main.yml'
    }

# Generated at 2024-05-31 22:19:09.545062
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():    data = {
        'name': 'test_role',
        'apply': {'some_option': 'value'},
        'public': True,
        'tasks_from': 'tasks/main.yml'
    }

# Generated at 2024-05-31 22:19:11.596491
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():    block = Block()

# Generated at 2024-05-31 22:19:15.833358
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():    data = {
        'name': 'test_role',
        'apply': {'some_key': 'some_value'},
        'tasks_from': 'tasks/main.yml',
        'vars_from': 'vars/main.yml',
        'defaults_from': 'defaults/main.yml',
        'handlers_from': 'handlers/main.yml',
        'public': True,
        'allow_duplicates': False,
        'rolespec_validate': True
    }

# Generated at 2024-05-31 22:19:18.076590
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():    block = Block()

# Generated at 2024-05-31 22:19:20.047030
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():    block = Block()

# Generated at 2024-05-31 22:19:22.743026
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():    data = {
        'name': 'test_role',
        'apply': {'some_key': 'some_value'},
        'public': True,
        'tasks_from': 'tasks/main.yml'
    }

# Generated at 2024-05-31 22:19:26.602313
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():    data = {
        'name': 'test_role',
        'role': 'test_role',
        'tasks_from': 'tasks/main.yml',
        'vars_from': 'vars/main.yml',
        'defaults_from': 'defaults/main.yml',
        'handlers_from': 'handlers/main.yml',
        'apply': {'some_option': 'some_value'},
        'public': True,
        'allow_duplicates': False,
        'rolespec_validate': True
    }

# Generated at 2024-05-31 22:19:36.210542
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():    block = Block()

# Generated at 2024-05-31 22:19:43.494061
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():    data = {
        'name': 'test_role',
        'apply': {'some_key': 'some_value'},
        'tasks_from': 'tasks/main.yml',
        'vars_from': 'vars/main.yml',
        'defaults_from': 'defaults/main.yml',
        'handlers_from': 'handlers/main.yml',
        'public': True,
        'allow_duplicates': False,
        'rolespec_validate': True
    }

# Generated at 2024-05-31 22:19:46.044744
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():    block = Block()

# Generated at 2024-05-31 22:19:48.465582
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():    data = {
        'name': 'test_role',
        'apply': {'some_key': 'some_value'},
        'public': True,
        'tasks_from': 'tasks/main.yml'
    }

# Generated at 2024-05-31 22:19:51.554992
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():    data = {
        'name': 'test_role',
        'role': 'test_role',
        'tasks_from': 'tasks/main.yml',
        'vars_from': 'vars/main.yml',
        'defaults_from': 'defaults/main.yml',
        'handlers_from': 'handlers/main.yml',
        'apply': {'some_option': 'some_value'},
        'public': True,
        'allow_duplicates': False,
        'rolespec_validate': True
    }

# Generated at 2024-05-31 22:19:53.933987
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():    block = Block()

# Generated at 2024-05-31 22:19:56.282869
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():    data = {
        'name': 'test_role',
        'apply': {'some_key': 'some_value'},
        'public': True,
        'tasks_from': 'tasks/main.yml'
    }

# Generated at 2024-05-31 22:19:59.647038
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():    data = {
        'name': 'test_role',
        'role': 'test_role',
        'tasks_from': 'tasks/main.yml',
        'vars_from': 'vars/main.yml',
        'defaults_from': 'defaults/main.yml',
        'handlers_from': 'handlers/main.yml',
        'apply': {'some_option': 'some_value'},
        'public': True,
        'allow_duplicates': False,
        'rolespec_validate': True
    }

# Generated at 2024-05-31 22:20:01.379022
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():    block = Block()

# Generated at 2024-05-31 22:20:06.389575
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():    data = {
        'name': 'test_role',
        'role': 'test_role',
        'tasks_from': 'tasks/main.yml',
        'vars_from': 'vars/main.yml',
        'defaults_from': 'defaults/main.yml',
        'handlers_from': 'handlers/main.yml',
        'apply': {'some_option': 'some_value'},
        'public': True,
        'allow_duplicates': False,
        'rolespec_validate': True
    }

# Generated at 2024-05-31 22:20:14.507345
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():    data = {
        'name': 'test_role',
        'apply': {'some_key': 'some_value'},
        'public': True,
        'tasks_from': 'tasks/main.yml'
    }

# Generated at 2024-05-31 22:20:17.191049
# Unit test for method get_include_params of class IncludeRole
def test_IncludeRole_get_include_params():    parent_role = Role()

# Generated at 2024-05-31 22:20:19.189800
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():    block = Block()

# Generated at 2024-05-31 22:20:21.453615
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():    block = Block()

# Generated at 2024-05-31 22:20:25.033408
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():    data = {
        'name': 'test_role',
        'role': 'test_role',
        'tasks_from': 'tasks/main.yml',
        'vars_from': 'vars/main.yml',
        'defaults_from': 'defaults/main.yml',
        'handlers_from': 'handlers/main.yml',
        'apply': {'some_option': 'some_value'},
        'public': True,
        'allow_duplicates': False,
        'rolespec_validate': True
    }

# Generated at 2024-05-31 22:20:30.024169
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():    data = {
        'name': 'test_role',
        'role': 'test_role',
        'tasks_from': 'tasks/main.yml',
        'vars_from': 'vars/main.yml',
        'defaults_from': 'defaults/main.yml',
        'handlers_from': 'handlers/main.yml',
        'apply': {'some_option': 'some_value'},
        'public': True,
        'allow_duplicates': False,
        'rolespec_validate': True
    }

# Generated at 2024-05-31 22:20:31.861596
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():    block = Block()

# Generated at 2024-05-31 22:20:35.756580
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():    data = {
        'name': 'test_role',
        'apply': {'some_key': 'some_value'},
        'public': True,
        'tasks_from': 'tasks/main.yml'
    }

# Generated at 2024-05-31 22:20:37.942720
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():    block = Block()

# Generated at 2024-05-31 22:20:41.197129
# Unit test for method get_include_params of class IncludeRole
def test_IncludeRole_get_include_params():    parent_role = Role()

# Generated at 2024-05-31 22:20:50.078198
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():    data = {
        'name': 'test_role',
        'apply': {'some_key': 'some_value'},
        'public': True,
        'tasks_from': 'tasks/main.yml'
    }

# Generated at 2024-05-31 22:20:54.471737
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():    data = {
        'name': 'test_role',
        'role': 'test_role',
        'tasks_from': 'tasks/main.yml',
        'vars_from': 'vars/main.yml',
        'defaults_from': 'defaults/main.yml',
        'handlers_from': 'handlers/main.yml',
        'apply': {'some_option': 'some_value'},
        'public': True,
        'allow_duplicates': False,
        'rolespec_validate': True
    }

# Generated at 2024-05-31 22:20:57.186523
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():    data = {
        'name': 'test_role',
        'apply': {'some_key': 'some_value'},
        'public': True,
        'tasks_from': 'tasks/main.yml'
    }

# Generated at 2024-05-31 22:21:00.771003
# Unit test for method get_include_params of class IncludeRole
def test_IncludeRole_get_include_params():    parent_role = Role()

# Generated at 2024-05-31 22:21:03.693819
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():    data = {
        'name': 'test_role',
        'role': 'test_role',
        'tasks_from': 'tasks/main.yml',
        'vars_from': 'vars/main.yml',
        'defaults_from': 'defaults/main.yml',
        'handlers_from': 'handlers/main.yml',
        'apply': {'some_option': 'some_value'},
        'public': True,
        'allow_duplicates': False,
        'rolespec_validate': True
    }

# Generated at 2024-05-31 22:21:06.074571
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():    data = {
        'name': 'test_role',
        'apply': {'some_key': 'some_value'},
        'public': True,
        'tasks_from': 'tasks/main.yml'
    }

# Generated at 2024-05-31 22:21:09.257671
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():    block = Block()

# Generated at 2024-05-31 22:21:12.097655
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():    block = Block()

# Generated at 2024-05-31 22:21:14.964343
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():    data = {
        'name': 'test_role',
        'apply': {'some_key': 'some_value'},
        'public': True,
        'tasks_from': 'tasks/main.yml'
    }

# Generated at 2024-05-31 22:21:17.629673
# Unit test for method get_include_params of class IncludeRole
def test_IncludeRole_get_include_params():    parent_role = Role()

# Generated at 2024-05-31 22:21:25.868359
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():    block = Block()

# Generated at 2024-05-31 22:21:30.732880
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():    data = {
        'name': 'test_role',
        'role': 'test_role',
        'tasks_from': 'tasks/main.yml',
        'vars_from': 'vars/main.yml',
        'defaults_from': 'defaults/main.yml',
        'handlers_from': 'handlers/main.yml',
        'apply': {'some_option': 'some_value'},
        'public': True,
        'allow_duplicates': False,
        'rolespec_validate': True
    }

# Generated at 2024-05-31 22:21:33.154283
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():    data = {
        'name': 'test_role',
        'apply': {'some_key': 'some_value'},
        'public': True,
        'tasks_from': 'tasks/main.yml'
    }