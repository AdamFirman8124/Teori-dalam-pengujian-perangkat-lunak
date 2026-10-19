

# Generated at 2022-06-13 08:52:18.119689
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    var_manager = VariableManager()
    var_manager.set_host_variable("host1", "hostname", "host1")
    var_manager.set_host_variable("host2", "hostname", "host2")
    var_manager.set_host_variable("host4", "hostname", "host4")

    var_manager.set_variable("test_var1", "var1")
    var_manager.set_variable("test_var2", "var2")

    var_manager.extra_vars = {"test_var": "value_extra_vars"}

    # basic
    data = "test_role1"

    loader = DataLoader()
    inventory = InventoryManager.construct_inventory(loader=loader, sources=["test/ansible/inventory/test_inventory.yaml"])

    # load data


# Generated at 2022-06-13 08:52:27.482276
# Unit test for method load of class RoleInclude

# Generated at 2022-06-13 08:52:37.667109
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    # Test for old style role requirement string
    test_data1 = 'jdoe.role'

    # Test for new style role requirement dict
    test_data2 = { 'role': 'jdoe.role', 'version': 'v1.0' }

    # Test for new style role requirement AnsibleBaseYAMLObject
    test_data3 = AnsibleBaseYAMLObject()
    test_data3.role = 'jdoe.role'
    test_data3.version = 'v1.0'

    # Test for invalid data type
    test_data4 = [ 'jdoe.role', 'v1.0' ]

    # Load old style role requirement string

# Generated at 2022-06-13 08:52:47.855353
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    class Play:
        pass
    play = Play()
    variable_manager = "variable_manager"
    loader = "loader"
    collection_list = "collection_list"
    role_basedir = "role_basedir"

    try:
        RoleInclude.load("string", play)
    except AnsibleParserError as e:
        assert e.message == "Invalid role definition: %s" % to_native("string")

    try:
        RoleInclude.load({'name': "name"}, play)
    except AnsibleParserError as e:
        assert e.message == "Invalid role definition: %s" % to_native({'name': "name"})


# Generated at 2022-06-13 08:52:56.070263
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    # GIVEN
    data = "test: test"
    loader = DictDataLoader({"test/test_RoleInclude.yml": data})
    variable_manager = VariableManager()

    # WHEN
    ri = RoleInclude()
    result = ri.load(data, variable_manager=variable_manager, loader=loader)

    # THEN
    assert result.get_name() == "test"
    assert result.get_tasks() == []



# Generated at 2022-06-13 08:53:05.848571
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook.play import Play

    variable_manager = None
    loader = None
    play = Play()
    data = "test"
    try:
        RoleInclude.load(data, play, variable_manager=variable_manager, loader=loader)
        assert False
    except AnsibleError as e:
        assert str(e) == "Invalid old style role requirement: test"

    data = 1
    try:
        RoleInclude.load(data, play, variable_manager=variable_manager, loader=loader)
        assert False
    except AnsibleParserError as e:
        assert str(e) == "Invalid role definition: 1"

    data = "test"

# Generated at 2022-06-13 08:53:14.604796
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():

    # case 1:
    # data is not either string nor dict
    data = ['role1', 'role2']
    play = dict()
    current_role_path = None
    parent_role = None
    variable_manager = None
    loader = None
    collection_list = None
    try:
        RoleInclude.load(data, play, current_role_path, parent_role, variable_manager, loader, collection_list)
    except Exception as e:
        assert type(e) is AnsibleParserError

    # case 2:
    # data is string and in the format of `role1,role2`
    data = "role1,role2"

# Generated at 2022-06-13 08:53:16.163620
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    # TODO: Add unit test for RoleInclude class load function
    pass

# Generated at 2022-06-13 08:53:28.868581
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    
    # Dummy role definition
    role_definition = {
        "name": "test-role", 
        "description": "This is a test role",
        "path": "/path/to/test-role", 
        "scm": "git",
        "src": "https://github.com/test/test-role",
        "version": "0.1"
    }
    # Dummy role requirement
    role_requirement = {
        "name": "test-role",
        "src": "https://github.com/test/test-role",
        "scm": "git",
        "version": "0.1",
        "path": "/path/to/test-role"
    }
    # Dummy host
    host = 'localhost'
    # Dummy inventory

# Generated at 2022-06-13 08:53:36.887190
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook.play import Play
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    loader = DataLoader()
    variable_manager = VariableManager()
    variable_manager.extra_vars = {'foo': 'bar'}
