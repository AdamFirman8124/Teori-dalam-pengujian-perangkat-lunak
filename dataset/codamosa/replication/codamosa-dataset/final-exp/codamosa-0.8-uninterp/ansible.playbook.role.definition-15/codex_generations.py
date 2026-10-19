

# Generated at 2022-06-13 08:41:53.877057
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    from ansible.vars.unsafe_proxy import UnsafeProxy
    from ansible.inventory.host import Host
    import ansible.constants as C
    from ansible.vars.manager import VariableManager

    ds = dict(
        role='test_role',
        become_user='root',
        become=True,
    )
    templar = Templar(loader=None)
    variable_manager = VariableManager()
    variable_manager._vars_cache = dict(
        all=dict(
            ansible_ssh_pass='{{ vault_ssh_pass }}',
            vault_ssh_pass='pass',
        ),
    )
    play_context = PlayContext(become_pass='s3cr3t')

# Generated at 2022-06-13 08:41:58.102749
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    role = RoleDefinition.load({'role': 'test_role', 'with_items': ['a', 'b']})
    assert role._role_params == {u'with_items': ['a', 'b']}
    assert role.role == 'test_role'


# Generated at 2022-06-13 08:42:09.995503
# Unit test for method get_name of class RoleDefinition
def test_RoleDefinition_get_name():
    assert RoleDefinition(role_basedir=None).get_name(include_role_fqcn=True) == ''
    assert RoleDefinition(role_basedir=None).get_name(include_role_fqcn=False) == ''
    assert RoleDefinition(role_basedir='/roles/my_role').get_name(include_role_fqcn=True) == '/roles/my_role'
    assert RoleDefinition(role_basedir='/roles/my_role').get_name(include_role_fqcn=False) == 'my_role'
    assert RoleDefinition(role_basedir='/roles/my_role', role='other_role').get_name(include_role_fqcn=True) == 'other_role'

# Generated at 2022-06-13 08:42:21.338896
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():

    # Inject the role_path into the MethodResolver used by the
    # RoleDefinition class to return the desired role_path
    # when the _load_role_path method is invoked by the
    # preprocess_data method.
    def inject_role_path(self, role_name):
        return role_name, u'role_path'

    RoleDefinition._load_role_path = inject_role_path

    rd = RoleDefinition()

    data_structure = dict()
    data_structure['role'] = 'role_name'
    data_structure['role_param'] = 'role_param_value'

    result = rd.preprocess_data(data_structure)
    assert (result['role'] == 'role_name')
    assert (result['playbook_basedir'] == 'role_path')


# Generated at 2022-06-13 08:42:29.363579
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager

    play_context = PlayContext()
    variable_manager = VariableManager()
    test_play = Play().load({
        'name' : 'test_play',
        'hosts' : 'localhost',
        'gather_facts' : 'no',
        'roles' : [
            {
                'role' : 'test_role',
                'test_attribute' : 'test_attribute_value',
                'test_parameter' : 'test_parameter_value'
            }
        ]
    }, variable_manager=variable_manager, loader=None)


# Generated at 2022-06-13 08:42:44.161929
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.playbook.play import Play
    from ansible.playbook.role import Role
    from ansible.plugins.loader import find_plugin
    from ansible.template import Templar

    if not find_plugin(Play.__name__):
        raise AssertionError()
    if not find_plugin(Role.__name__):
        raise AssertionError()

    role = Role()
    role = role.load({'name': 'role-name-1'})
    result = role.preprocess_data({'name': 'role-name-1'})

    assert result['name'] == 'role-name-1'

    role = Role()
    role = role.load({'name': 'role-name-2'})
    result = role.preprocess_data({'name': 'role-name-2'})



# Generated at 2022-06-13 08:42:49.345563
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    # Given
    ds = dict(
        role='fake_role_name',
        any_key='any_value',
        )

    # When
    c = RoleDefinition()
    result = c.preprocess_data(ds)

    # Then
    assert result == dict(role='fake_role_name')


# Generated at 2022-06-13 08:43:03.060130
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    def _load_role_name(self, ds):
        return ds

    # The line numbers are important here. If you add, remove or change lines, you need to adjust accordingly
    role_defs_strings = [
        "role_name",
        "{ role: 'role_name'}",
        "{ name: 'role_name'}",
        "{ role: 'role_name', parameter1: 'value1', parameter2: 'value2'}",
        "{ name: 'role_name', parameter1: 'value1', parameter2: 'value2'}",
        #"{ role: 1 }"
    ]


# Generated at 2022-06-13 08:43:12.770587
# Unit test for method get_name of class RoleDefinition
def test_RoleDefinition_get_name():

    # Create two RoleDefinition objects to test
    roles_dir = '.'
    loader = None
    play = None
    vm = None

    test_cases = [
        # test_case 1
        {
            "name": "Test with valid role definition",
            "role_definition": {'role': 'test_role_name'},
            "expected": {
                "include_role_fqcn": True,
                "output": 'test_role_name',
            },
        },
        # test_case 2
        {
            "name": "Test with role path",
            "role_definition": 'test_role_path',
            "expected": {
                "include_role_fqcn": True,
                "output": 'test_role_path',
            },
        },
    ]


# Generated at 2022-06-13 08:43:20.451199
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    role_p_success = {'role': 'testrole'}
    role_p_success_alias = {'name': 'testrole'}
    role_n_success = 'testrole_name_only'
    role_n_success_quoted = "'testrole_name_only_quoted'"
    role_n_success_double_quote = '"testrole_name_only_double_quote"'
    role_n_success_template = '"{{ role_name }}"'
    role_n_success_template_single_quote = "'{{ role_name_single_quote }}'"
    role_n_success_dict = {'role': 'testrole_dict'}
    role_n_success_alias_dict = {'name': 'testrole_alias_dict'}

    role_n_fail = None
    role

# Generated at 2022-06-13 08:43:35.885947
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins.loader import action_loader
    from ansible.vars.manager import VariableManager

    variable_manager = VariableManager()
    loader = DataLoader()
    variable_manager.set_inventory(Inventory(loader=loader, variable_manager=variable_manager, host_list='localhost'))

    value_from_inventory = 'localhost'
    PC = PlayContext(variable_manager=variable_manager)
    variable_manager.set_loader(loader)

# Generated at 2022-06-13 08:43:48.675896
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.playbook import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.vars import VariableManager
    from ansible.utils.vars import combine_vars

    DATA = """
    ---
    - hosts: localhost
      roles:
        - role: testrole
          role_param: role_param_value
          role_param2:
            - role_param2_value
          role_param3:
            - role_param3_value
            - role_param3_value2
    """

    r = RoleDefinition()
    r._loader = None

    p = Play().load(DATA, variable_manager=VariableManager(), loader=None)
    p._variable_manager = VariableManager()
    p._tasks = []
    _ = p.get_tasks()

   

# Generated at 2022-06-13 08:43:58.844322
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    # Mocking objects
    class MockVariableManager:
        pass
    class MockDataLoader:
        pass
    class MockPlayContext:
        pass

    data_structures = [
        # Test with a dictionary
        {
            "role": "foo-role"
        },
        {
            "role": "foo-role",
            "bar": "baz"
        },
        {
            "role": "foo-role",
            "bar": "baz",
            "tags": "foo"
        },
        {
            "role": "foo-role",
            "bar": "baz",
            "when": "foo"
        },
        # Test with a simple string
        'foo-role',
        # Test with an integer
        42
    ]

# Generated at 2022-06-13 08:44:14.372333
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():

    # Ensure that valid input parameters are successfully parsed
    datastructure = dict(role='test-role')
    rd = RoleDefinition()
    new_ds = rd.preprocess_data(datastructure)
    assert new_ds['role'] == 'test-role'

    # Ensure that a role definition containing a role keyword is successfully parsed
    datastructure = dict(role='test-role', test='test-val')
    rd = RoleDefinition()
    new_ds = rd.preprocess_data(datastructure)
    assert new_ds['role'] == 'test-role'
    assert rd._role_params['test'] == 'test-val'

    # Ensure that a role definition containing a role keyword is successfully parsed
    datastructure = dict(name='test-role', test='test-val')

# Generated at 2022-06-13 08:44:24.899165
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.playbook.play_context import PlayContext
    from ansible.parsing.yaml.objects import AnsibleUnicode, AnsibleSequence, AnsibleMapping
    from ansible.utils.collection_loader._collection_finder import CollectionFinder
    all_vars = dict()
    variable_manager = None
    play = None
    loader = None
    RoleDefinition(play, variable_manager=variable_manager, loader=loader, collection_list=CollectionFinder().find(".", "", "", "", "", "", all_vars))
    ds = AnsibleMapping()
    assert isinstance(RoleDefinition._load_role_name(ds), str)
    ds = {
        'role': 'role_name'
    }
    role_name, role_path = RoleDefinition._load_role_

# Generated at 2022-06-13 08:44:36.995727
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    '''
    Unit test for RoleDefinition.preprocess_data
    '''
    import json

    # Dependencies
    from ansible.parsing.yaml.loader import AnsibleLoader

    # Define objects to be used in the test

    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    class Playbook:
        def __init__(self):
            self.inventory = InventoryManager(loader=None, sources=[])

    class Host:
        def __init__(self, name=None):
            self.name = name
            self.vars = dict(
                roles=['test_role'],
            )

    test_playbook = Playbook()

    test_host = Host()

# Generated at 2022-06-13 08:44:48.810573
# Unit test for method get_name of class RoleDefinition
def test_RoleDefinition_get_name():
    role_name = 'test_role_name'
    role_path = '/tmp/roles'
    ds = dict(role=role_name)
    rd = RoleDefinition()
    rd._role_path = role_path

    # when include_role_fqcn == True
    # we expect that rd.get_name() returns a fully qualified collection name
    # containing the role name, path, and the collection name
    rd._role_collection = 'test_collection_name'
    assert rd.get_name() == '.'.join(x for x in (rd._role_collection, role_name, role_path) if x)

    # when include_role_fqcn == False
    # we expect that rd.get_name() returns only the role name

# Generated at 2022-06-13 08:44:59.489498
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.config.manager import ConfigManager
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.inventory.manager import InventoryManager
    from ansible.module_utils._text import to_text

    def load_config():
        return ConfigManager(
            [os.path.join(os.path.dirname(__file__), 'test_data/test.cfg')]
        )

    #
    # test_file_based_role_with_full_path
    #
    config = load_config()
    ds = dict(role="/tmp/test_role")
    play_context = PlayContext()
    variable

# Generated at 2022-06-13 08:45:04.564256
# Unit test for method get_name of class RoleDefinition
def test_RoleDefinition_get_name():
    rd = RoleDefinition()
    rd.role = 'role_a'
    assert rd.get_name() == 'role_a'

    rd._role_collection = 'ns_a.col_b'
    assert rd.get_name() == 'ns_a.col_b.role_a'
    assert rd.get_name(include_role_fqcn=False) == 'role_a'

# Generated at 2022-06-13 08:45:13.279818
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():

    rd = RoleDefinition()

    role_name_1 = 'role name 1'
    role_name_1_as_dict = {'role': role_name_1}
    assert role_name_1 == rd._load_role_name(role_name_1)
    assert role_name_1 == rd._load_role_name(role_name_1_as_dict)

    # The name parameter of a role definition is an alias for the role parameter
    role_name_2 = 'role name 2'
    role_name_2_as_dict = {'name': role_name_2}
    assert role_name_2 == rd._load_role_name(role_name_2_as_dict)

    role_name_3 = 'role name 2'

# Generated at 2022-06-13 08:45:25.532493
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    role_definition= RoleDefinition()
    role_name = role_definition.preprocess_data("test-role")
    assert role_name == "test-role"

# Generated at 2022-06-13 08:45:37.152691
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    # Mocking the data structure
    ds = {
        'name': 'test',
        'tasks': [
            'task1',
            'task2',
        ],
    }

    role_definition = RoleDefinition()

    # testing the preprocessed data structure
    preprocess_ds = role_definition.preprocess_data(ds)
    assert preprocess_ds.get('name') == 'test'

    # Mocking the data structure
    ds = {
        'role': 'test',
        'tasks': [
            'task1',
            'task2',
        ],
    }

    role_definition = RoleDefinition()

    # testing the preprocessed data structure
    preprocess_ds = role_definition.preprocess_data(ds)
    assert preprocess_ds.get('role') == 'test'

# Generated at 2022-06-13 08:45:50.814245
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    # Test for checking the role name which is simply a string without any quotes but
    # PyYAML has the capability of parsing it as an integer. Here the role name is
    # simply an integer.
    test_case1 = {'role': 4}
    # Test for checking the role name which is simply a string containing some special characters
    # such as quote, colon, hyphen, comma, etc.
    test_case2 = {'role': 'Username-1'}
    # Test for checking the role name which is simply a string containing some special characters
    # such as quote, colon, hyphen, comma, etc. and is quoted by single quotes.
    test_case3 = {'role': 'Username-1'}
    # Test for checking the role name which is simply a string containing some special characters
    # such as quote, colon, hyphen

# Generated at 2022-06-13 08:46:03.884787
# Unit test for method get_name of class RoleDefinition
def test_RoleDefinition_get_name():
    test_role = RoleDefinition()
    # Test with role collection set to "test" and role set to "test_role",
    # include_role_fqcn set to True
    test_role._role_collection = "test"
    test_role.role = "test_role"
    assert test_role.get_name(include_role_fqcn=True) == "test.test_role"
    # Test with role collection set to None and role set to "test_role",
    # include_role_fqcn set to True
    test_role._role_collection = None
    test_role.role = "test_role"
    assert test_role.get_name(include_role_fqcn=True) == "test_role"
    # Test with role collection set to "test" and role set to None,


# Generated at 2022-06-13 08:46:16.679531
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.playbook.play_context import PlayContext
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.template import Templar
    from ansible.utils.display import Display
    from ansible.plugins.loader import connection_loader, lookup_loader
    display = Display()
    options = dict(connection='local', module_path=['/to/mymodules'], forks=10, become=None,
                   become_method=None, become_user=None, check=False, diff=False, listhosts=None, listtasks=None,
                   listtags=None, syntax=None)
    loader = DataLoader()
    passwords = dict()

# Generated at 2022-06-13 08:46:29.881331
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.role.requirement import RoleRequirement

    parser = RoleDefinition.load({u'role': u'foo'}, loader=DataLoader(), variable_manager={})
    assert parser.role == 'foo'

    parser = RoleDefinition.load({u'name': u'foo'}, loader=DataLoader(), variable_manager={})
    assert parser.role == 'foo'

    parser = RoleDefinition.load(AnsibleMapping(mapping={u'role': u'foo'}), loader=DataLoader(), variable_manager={})
    assert parser.role == 'foo'
    assert parser.get_role_path() is None
    assert parser._role_basedir is None


# Generated at 2022-06-13 08:46:37.177560
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.playbook.play import Play
    from ansible.template import Templar
    from ansible.parsing.yaml.objects import AnsibleMapping

    play = Play().load({
        "name": "Ansible Play",
        "hosts": "localhost",
        "roles": ["role1"],
        "tasks": []
    }, variable_manager=None, loader=None)

    variable_manager = None
    loader = None
    collection_list = None

    playbook_base_path = os.path.join(os.path.dirname(__file__), '..', '..', 'test_data')

    templar = Templar(loader=loader, variables=dict())
    role_basedir = None

    # test: role path set to None (role path undefined)
    role_def = RoleDefinition

# Generated at 2022-06-13 08:46:38.543472
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    # FIXME: implement me!
    pass

# Generated at 2022-06-13 08:46:47.093774
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    import ansible.playbook.play_context
    import ansible.playbook.play
    import ansible.vars.manager
    import ansible.template.template

    play_context = ansible.playbook.play_context.PlayContext()
    play_context.network_os = 'ios'

    play = ansible.playbook.play.Play().load({
        'name': "Ansible Play",
        'hosts': '{{ inventory_hostname }}',
        'gather_facts': 'no',
        'connection': 'local',
    }, variable_manager=ansible.vars.manager.VariableManager(), loader=ansible.parsing.dataloader.DataLoader())


# Generated at 2022-06-13 08:46:59.170771
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    rd = RoleDefinition()
    yaml_ds = {
        'role': 'testrole',
        'tasks': {'include': 'print.yml'},
        'vars': {'var1': 'val1'},
        'handlers': {'include': 'handlers.yml'},
        'meta': {'meta1': 'meta1'}
    }
    assert rd.preprocess_data(yaml_ds) == {'role': 'testrole'}
    assert rd.get_role_path() == None

# Generated at 2022-06-13 08:47:15.038442
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play

    variable_manager = VariableManager()
    loader = DataLoader()
    variable_manager.set_inventory(Inventory(loader=loader, host_list=['localhost']))

    def get_role_definition(data):
        play = Play().load({}, variable_manager=variable_manager, loader=loader)
        return RoleDefinition(play=play, variable_manager=variable_manager, loader=loader, collection_list=[]).preprocess_data(data)

    role_name_string = 'test_role'
    assert get_role_definition(role_name_string) == role_name_string

    role_name_dict_0

# Generated at 2022-06-13 08:47:26.117017
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    '''
    This function is not a unittest. It's a function that demonstrates the usage
    of the class RoleDefinition and its method preprocess_data
    '''
    import ansible.plugins.loader as plugin_loader
    from ansible.parsing.plugin_docs import read_docstring

    # Declare the objects needed to instantiate a RoleDefinition:
    play = dict(
        name='Demo Play',
        hosts=['demo-host'],
        gather_facts='no',
        connection='local',
        # ...
    )
    role_basedir = '/path/to/playbook/roles'
    variable_manager = dict(
        # variables dict here
    )
    # We instantiate a Loader here, but the instance is not needed for anything

# Generated at 2022-06-13 08:47:35.357037
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():

    from units.mock.loader import DictDataLoader

    # test without variables
    role_name = DictDataLoader({
        "library/role_name.yml": """
        role: myrole
        """
    })

    rd = RoleDefinition.load({'role': 'role_name'}, loader=role_name)[0]
    rd.preprocess_data(rd._ds)

    assert rd._role_path == role_name.path_dwim("library/role_name")

# Generated at 2022-06-13 08:47:42.313598
# Unit test for method get_name of class RoleDefinition
def test_RoleDefinition_get_name():
    role_def = RoleDefinition.load(dict(name="myrole"), None, None)
    assert role_def.get_name() == "myrole"
    role_def = RoleDefinition.load(dict(name="myrole"), None, None, collection_list=["namespace.foo"])
    assert role_def.get_name() == "namespace.foo.myrole"

# Generated at 2022-06-13 08:47:51.660772
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    """
    Test RoleDefinition.preprocess_data method
    """

    import yaml
    yaml_str = """
    - hosts: localhost
      roles:
      - role: test
        role_param1: a
        role_param2: b
    """

    results = list(yaml.safe_load_all(yaml_str))
    loader = None
    variable_manager = None
    role_basedir = None
    role_def = RoleDefinition(play=results[0], loader=loader, variable_manager=variable_manager,
                              role_basedir=role_basedir, collection_list=None)

    ds = results[0]['roles'][0]
    new_ds = role_def.preprocess_data(ds)

    assert 'role' in new_ds

# Generated at 2022-06-13 08:48:04.515349
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    import yaml
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext
    from ansible.utils.vars import combine_vars
    from ansible.playbook.role_include import RoleInclude

    current_dir = os.path.dirname(__file__)
    fixtures_path = os.path.join(current_dir, '/fixtures/preprocess_data_role')
    parent_vars = combine_vars(loader=DataLoader(), variables=dict(foo='bar'))
    inventory = InventoryManager(loader=DataLoader(), sources='localhost,')

# Generated at 2022-06-13 08:48:16.302344
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    '''
    Unit test for method preprocess_data of class RoleDefinition
    '''
    #
    # RoleDefinition.preprocess_data() gets a dictionary and returns a dictionary.
    #

    from ansible.playbook.role.definition import RoleDefinition
    assert (isinstance(RoleDefinition().preprocess_data({}), dict))

    #
    # If the role definition is not a string or a dict, raise an exception.
    #
    from ansible.playbook.role.definition import RoleDefinition
    try:
        RoleDefinition().preprocess_data(1)
        assert False, 'Unexpected behavior: no exception is raised'
    except Exception:
        pass

    #
    # The role name can be either the "role:" entry, or the "name:" entry,
    #

# Generated at 2022-06-13 08:48:28.565095
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.vars.manager import VariableManager
    from ansible.playbook.play import Play

    VariableManager._fact_cache = {'ansible_distribution': 'CentOS', 'ansible_distribution_version': '7.3.1611'}
    play = Play.load('test/units/playbookexpl2/groups.yaml', variable_manager=VariableManager(loader=None), loader=None)

    if not play._variable_manager:
        assert False, "VariableManager is empty"


    assert play.tags == [u'all'],   "expected tags 'all', got %s" % play.tags
    assert play.tasks[0].name == u'count me', "expected task name 'count me', got %s" % play.tasks[0].name

# Generated at 2022-06-13 08:48:36.839408
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.vars.manager import VariableManager
    from ansible.utils.vars import combine_vars

    fake_variable_manager = VariableManager()
    data = dict(
        role="test_role",
        some_variable="value1",
        some_other_variable="value2"
    )

    # First test without any variables
    rd = RoleDefinition()
    rd.variable_manager = fake_variable_manager

    new_data = rd.preprocess_data(data)

    assert(isinstance(new_data, AnsibleMapping))
    assert(type(new_data) is dict)
    assert('role' in new_data)
    assert('some_variable' not in new_data)
    assert('some_other_variable' not in new_data)


# Generated at 2022-06-13 08:48:43.088884
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    rd = RoleDefinition()

    # Special YAML dict
    data = AnsibleMapping()
    data.ansible_pos = ("test_RoleDefinition_preprocess_data", 3, 1, "simple.yaml")
    data['role'] = "name"
    assert rd.preprocess_data(data) == {'role': 'name'}
    assert rd._role_path is None
    assert rd._role_params == {}

    # Very simple dict
    data = { 'role': "name" }
    assert rd.preprocess_data(data) == {'role': 'name'}
    assert rd._role_path is None
    assert rd._role_params == {}

    # Invalid dict
    data = { 'role1': "name" }

# Generated at 2022-06-13 08:48:57.477133
# Unit test for method get_name of class RoleDefinition
def test_RoleDefinition_get_name():
    # __main__.Attribute = <class 'ansible.playbook.attribute.Attribute'>
    # __main__.Base = <class 'ansible.playbook.base.Base'>
    # __main__.RoleDefinition = <class 'ansible.playbook.role_definition.RoleDefinition'>
    def mock_name_repr(obj):
        if isinstance(obj, Attribute):
            return 'ansible.playbook.attribute.Attribute'
        elif isinstance(obj, Base):
            return 'ansible.playbook.base.Base'
        elif isinstance(obj, RoleDefinition):
            return 'ansible.playbook.role_definition.RoleDefinition'
        raise NotImplementedError()

    import types

# Generated at 2022-06-13 08:49:12.138152
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from collections import namedtuple
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.inventory import Inventory
    from ansible.vars.manager import VariableManager

    RoleDefinition_init = namedtuple('RoleDefinition_init', ['play', 'role_basedir', 'variable_manager', 'loader'])
    RoleDefinition_init.play = None
    RoleDefinition_init.role_basedir = None
    RoleDefinition_init.variable_manager = None
    RoleDefinition_init.loader = None
    RoleDefinition_init.collection_list = None

    # create RoleDefinition object to test
    role_definition_object = RoleDefinition(**RoleDefinition_init._asdict())

    # set some attributes to test

# Generated at 2022-06-13 08:49:20.392409
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    import ansible.playbook
    fake_play = ansible.playbook.Play()
    fake_loader = ansible.loader.Loader()
    fake_variable_manager = ansible.vars.VariableManager()

    role_definition = RoleDefinition(play=fake_play, role_basedir='/tmp/ansible_test/role_basedir', variable_manager=fake_variable_manager, loader=fake_loader)

    ds = {
        'role': 'nginx-servers',
        'other_config': 'foo'
    }
    processed_ds = role_definition.preprocess_data(ds)
    assert processed_ds["role"] == "nginx-servers"
    assert processed_ds["other_config"] == "foo"
    assert role_definition._role_params["other_config"] == "foo"

# Generated at 2022-06-13 08:49:26.641779
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.playbook.play_context import PlayContext

    # Setup for testing
    role_path="roles/test"
    role_basedir="roles"
    variable_manager=None
    loader=None
    collection_list=None

    # expected result
    expected_result = 'test'
    role_ds = [{'role': 'test'}, {'name': 'test'}]

    # test with role:
    rd = RoleDefinition(role_basedir=role_basedir, variable_manager=variable_manager, loader=loader, collection_list=collection_list)
    result = rd.preprocess_data(role_ds[0])
    assert(result['role'] == expected_result)

    # test with name:

# Generated at 2022-06-13 08:49:31.870990
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    for ds in ROLE_DEFINITIONS:
        role_definition = RoleDefinition()
        role_definition.preprocess_data(ds)
        actual_ds = role_definition._ds
        expected_ds = ROLE_DEFINITIONS[ds]
        assert actual_ds == expected_ds


# TODO: remove these test cases after issue #29876 has been fixed

# Generated at 2022-06-13 08:49:43.361536
# Unit test for method get_name of class RoleDefinition
def test_RoleDefinition_get_name():
    rd = RoleDefinition()
    rd._role_basedir = None

    # Testing without role_basedir
    rd._role_collection = 'collection'
    rd.role = 'role_name'

    assert rd.get_name() == 'collection.role_name'
    assert rd.get_name(include_role_fqcn=False) == 'role_name'

    # Testing with role_basedir
    rd._role_basedir = '/etc'
    rd._role_collection = None
    rd.role = 'role_name'

    assert rd.get_name() == 'role_name'
    assert rd.get_name(include_role_fqcn=False) == 'role_name'

# Generated at 2022-06-13 08:49:49.397861
# Unit test for method get_name of class RoleDefinition
def test_RoleDefinition_get_name():
    role_definition = RoleDefinition()
    with pytest.raises(AnsibleError):
        assert role_definition.get_name()
    role_definition.role = 'foo'
    assert role_definition.get_name() == 'foo'
    role_definition._role_collection = 'ansible.builtin'
    assert role_definition.get_name() == 'ansible.builtin.foo'

# Generated at 2022-06-13 08:49:53.565365
# Unit test for method get_name of class RoleDefinition
def test_RoleDefinition_get_name():
    role_def = RoleDefinition()
    role_def._role_collection = "c1"
    role_def._role = "r1"
    assert role_def.get_name() == "c1.r1"
    assert role_def.get_name(include_role_fqcn=False) == "r1"
    role_def._role_collection = None
    role_def._role = "r1"
    assert role_def.get_name() == "r1"
    assert role_def.get_name(include_role_fqcn=False) == "r1"

# Generated at 2022-06-13 08:50:02.964553
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    class FakeVariableManager:
        def __init__(self):
            self.vars = dict(test_dict=dict(test_key='test_value'))
        def get_vars(self, play=None):
            return self.vars
    variable_manager = FakeVariableManager()
    role_basedir = 'role_basedir'
    loader = FakeLoader()
    collection_list = list()
    rd = RoleDefinition(play=None,
                        role_basedir=role_basedir,
                        variable_manager=variable_manager,
                        loader=loader,
                        collection_list=collection_list)

    def assert_rd(ds, role, role_path, role_params):
        ds = rd.preprocess_data(ds)
        assert role_path == rd._role_path
        assert role

# Generated at 2022-06-13 08:50:06.000245
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    assert RoleDefinition.load({
        'role': 'test',
        'foo': 'bar'
    }) == RoleDefinition.load({
        'role': {'role': 'test', 'foo': 'bar'}
    })

# Generated at 2022-06-13 08:50:29.604585
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    class TestAnsibleMapping:
        ansible_pos = 'test_file:12:34'

        def __init__(self):
            self.test_dict = dict()

        def __setitem__(self, key, value):
            self.test_dict[key] = value

        def __getitem__(self, key):
            return self.test_dict[key]

    # test role definition with role: or name:
    role_nameless = dict(
        role='nameless_role',
        many_fields=dict(
            foo=True,
            bar=False,
            baz=True,
            name=False,
            role=False,
            connection=True,
            gather_facts=True,
            ignore_errors=True,
            listeners=True,
        ),
    )
    role

# Generated at 2022-06-13 08:50:40.626949
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.parsing.yaml.loader import AnsibleLoader

    data = '''
- role:
    role: role1
  vars:
    var1: value1
  tags:
    - tag1
    - tag2
- role:
    name: role2
  vars:
    var2: value2
  become: true
  become_user: root
  become_method: sudo
'''

    yaml_obj = AnsibleLoader(data, 'test.yaml').get_single_data()
    print(yaml_obj)
    role_defs = []
    for ds in yaml_obj:
        role_def = RoleDefinition()
        role_defs.append(role_def)
        role_def.preprocess_data(ds)


# Generated at 2022-06-13 08:50:50.373211
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    with open(os.path.join(os.path.dirname(__file__), 'dependencies.yml')) as f:
        contents = f.read()
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.playbook.play import Play
    role_definition = AnsibleLoader(contents, 'test_file_name.yml').get_single_data()
    play = Play().load(role_definition[0], variable_manager=None, loader=None)
    # Test that when a simple string is passed in, then the string is returned
    if play.dependencies[0].preprocess_data('test_role') != b'test_role':
        print("test fail - RoleDefinition.preprocess_data: a simple string as input returned a non string value as output")

# Generated at 2022-06-13 08:51:03.611639
# Unit test for method get_name of class RoleDefinition

# Generated at 2022-06-13 08:51:16.365254
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():

    from ansible.parsing.yaml.dumper import AnsibleDumper
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.utils.collection_loader import AnsibleCollectionRef

    # test loading via a dictionary
    ds = {
        'role': 'foo',
        'role_basedir': 'my_role_basedir',
        'name': 'bar',
        'other': 'baz',
    }

    # create the role definition instance
    role_def = RoleDefinition(role_basedir=ds['role_basedir'])
    role_def.load_data(ds)

    # update the data structure and make sure it's as we expect
    ds = role_def.preprocess_data(ds)


# Generated at 2022-06-13 08:51:28.123869
# Unit test for method get_name of class RoleDefinition
def test_RoleDefinition_get_name():
    role_def = RoleDefinition()

    role_def._role_collection = 'test_collection'
    role_def.role = 'test_role'
    assert role_def.get_name() == 'test_collection.test_role'
    assert role_def.get_name(include_role_fqcn=False) == 'test_role'

    role_def._role_collection = 'test_collection'
    role_def.role = None
    with pytest.raises(AnsibleError) as excinfo:
        role_def.get_name()
    assert 'role definitions must contain a role name' in str(excinfo.value)
    assert role_def.get_name(include_role_fqcn=False) == ''

    role_def._role_collection = ''

# Generated at 2022-06-13 08:51:39.626204
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    # These are the tests which were run manually in the past
    # and now converted to automatic unit tests
    # This test is a bit complex, it tests the following:
    #   role: name: test inputs:
    #   role: name: test connections:
    #   role: name: test vars:
    #   role: name: test tasks:
    #   task: name: test
    from ansible.playbook.role import Role
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.play_context import PlayContext
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    # Setup DataLoader
    loader = DataLoader()

