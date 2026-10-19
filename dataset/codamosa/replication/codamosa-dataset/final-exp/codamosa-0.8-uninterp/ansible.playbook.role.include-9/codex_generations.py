

# Generated at 2022-06-13 08:52:16.563132
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook.play import Play
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.playbook_executor import PlaybookExecutor

    variable_manager = VariableManager()
    loader = DataLoader()
    play = Play()
    variable_manager = variable_manager
    loader = loader
    play = play

    assert RoleInclude.load(data=dict(role="web", tags=['dev', 'deploy']), play=play, current_role_path=None, parent_role=None, variable_manager=variable_manager, loader=loader)


# Generated at 2022-06-13 08:52:26.832925
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():

    from ansible.collections.ansible.community.plugins.module_utils.ansible_playbook import Playbook
    from ansible.parsing.yaml.objects import AnsibleUnicode

    play = Playbook()
    current_role_path = './'
    variable_manager = None
    loader = None
    collection_list = None

    try:
        RoleInclude.load(1, play, current_role_path, variable_manager=variable_manager, loader=loader, collection_list=collection_list)
        assert False
    except AnsibleParserError:
        pass

    try:
        RoleInclude.load('1,2', play, current_role_path, variable_manager=variable_manager, loader=loader, collection_list=collection_list)
        assert False
    except AnsibleError:
        pass

# Generated at 2022-06-13 08:52:27.481878
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    pass

# Generated at 2022-06-13 08:52:37.666899
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():

    # Tests load method with empty dictionary, invalid dictionary, and a valid dictionary
    # All other branches in this method are handled in test_RoleInclude_load_data

    import ansible.playbook.role.meta
    import ansible.playbook.role.include
    import ansible.constants as C
    import ansible.errors as errors
    import ansible.playbook.play
    import ansible.playbook.role.definition
    import ansible.playbook.role.requirement
    import ansible.plugins.loader as plugin_loader


    # Mock the loader module
    mock_loader = plugin_loader.PluginLoader(
        'ansible.plugins.loader',
        'LoaderModule',
        '',
        'loader'
    )

    # If a dictionary is empty, test will pass
    rd = {}
    ri

# Generated at 2022-06-13 08:52:47.855840
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook.role.include import RoleInclude
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    loader = DataLoader()
    variable_manager = VariableManager()
    variable_manager.set_available_variables(loader.load_from_file(os.path.join(os.path.dirname(__file__), '../../../playbooks/vars/main.yml')))
    variable_manager.extra_vars = variable_manager.get_vars(loader=loader, play=None)
    variable_manager.options_vars = variable_manager.get_vars(loader=loader, play=None)

    data = {'name': 'myrole', 'tasks': ['firsttask']}
    ri = RoleIn

# Generated at 2022-06-13 08:52:51.397158
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    data = "apache"
    RoleInclude.load(data, None)


# Generated at 2022-06-13 08:53:02.087432
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    attr = dict(name="test",
                tasks=[{"debug": {"msg": "hello world"}}],
                handlers=[{"debug": {"msg": "hello world"}}],
                vars={'test_var': 'value'},
                default_vars={'default_test_var': 'value'})

    role_req = RoleRequirement("test", "test_version", "/tmp/test")
    attr['dependencies'] = [role_req]

    (data, current_role_path) = get_file_info(attr)
    (role, current_role_path) = RoleInclude.load(data, play=None, current_role_path=current_role_path)
    assert_equal_role(role, attr)

# Generated at 2022-06-13 08:53:04.623613
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
        roleInclude_Obj=RoleInclude()
        roleInclude_Obj.load('role')

# Generated at 2022-06-13 08:53:13.750144
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():

    def get_ansible_error(value):
        try:
            RoleInclude.load(value, None)
            return None
        except AnsibleError as e:
            #print(value, e)
            return e

    def get_ansible_parser_error(value):
        try:
            RoleInclude.load(value, None)
            return None
        except AnsibleParserError as e:
            #print(value, e)
            return e

    # Test passing valid types for 'data' argument
    assert RoleInclude.load('geerlingguy.java', None)
    assert RoleInclude.load({'role': 'geerlingguy.java'}, None)
    assert RoleInclude.load(AnsibleBaseYAMLObject({'role': 'geerlingguy.java'}), None)

    #

# Generated at 2022-06-13 08:53:22.669247
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    return
    #
    # loader = DictDataLoader({})
    # variable_manager = VariableManager()
    # variable_manager.extra_vars = {'aaa': 'bbb'}
    #
    # play = Play().load({'name': 'test_play', 'connection': 'test_connection'}, variable_manager, loader)
    #
    # # Load RoleInclude with list of vars
    # ri = RoleInclude()
    # ri.load({'role': 'name', 'vars': [{'var1': 'value1'}, {'var2': 'value2'}]}, play, variable_manager=variable_manager, loader=loader)
    # assert ri.get_vars() == {'var1': 'value1', 'var2': 'value2'}
    #
   