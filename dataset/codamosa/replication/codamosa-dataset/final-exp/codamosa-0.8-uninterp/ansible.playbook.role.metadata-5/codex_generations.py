

# Generated at 2022-06-13 08:52:18.127749
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    role = RoleMetadata()
    role.deserialize(dict(allow_duplicates=True, dependencies=['geerlingguy.repo-epel']))
    assert role._allow_duplicates
    assert role._dependencies[0].name == 'geerlingguy.repo-epel'
    assert role._dependencies[0].get('allow_duplicates') == False

# Generated at 2022-06-13 08:52:22.658799
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    setattr(_, 'allow_duplicates', [])
    setattr(_, 'dependencies', [])
    return dict(
        allow_duplicates=self._allow_duplicates,
        dependencies=self._dependencies
    )

# Generated at 2022-06-13 08:52:34.829299
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    from ansible.playbook.role import Role
    from ansible.playbook.role.include import RoleInclude
    test_role = Role()
    test_role_metadata = RoleMetadata(owner=test_role)

    # test for a RoleMetadata object
    assert isinstance(test_role_metadata, RoleMetadata)

    # test for a RoleMetadata object, loaded from a dictionary
    role_metadata = RoleMetadata.load({}, test_role)
    assert isinstance(role_metadata, RoleMetadata)
    assert role_metadata._allow_duplicates == False
    assert role_metadata._dependencies == []

    # test serialize
    test_role_metadata._dependencies.append(test_role)
    test_role_metadata._dependencies.append(RoleInclude())

# Generated at 2022-06-13 08:52:46.363080
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.playbook.role import Role
    from ansible.playbook.play_context import PlayContext
    from ansible.parsing.yaml.loader import AnsibleLoader
    import yaml

    input1 = """
    allow_duplicates: yes
    dependencies:
    - { role: other, vars: { a: b } }
    """

    input2 = """
    allow_duplicates: yes
    dependencies:
      - other
      - { role: other, vars: { a: b } }
    """


# Generated at 2022-06-13 08:52:48.250373
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    role_meta = RoleMetadata()
    data = {"allow_duplicates": False, "dependencies": []}
    role_meta.deserialize(data)
    assert role_meta.allow_duplicates == False
    assert role_meta.dependencies == []

# Generated at 2022-06-13 08:52:50.761080
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    # TODO: write some tests
    assert True

# Generated at 2022-06-13 08:52:53.626896
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    metadata = RoleMetadata(owner=None)
    assert metadata._allow_duplicates == False
    assert metadata._dependencies == []
    assert metadata._galaxy_info == None
    assert metadata._owner == None

# Generated at 2022-06-13 08:53:04.210695
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    '''
    Unit test for method load of class RoleMetadata
    '''
    import os,sys,inspect
    currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    parentdir = os.path.dirname(currentdir)
    sys.path.insert(0,parentdir)
    from role import Role
    from task import Task
    from play import Play
    from playbook_include import PlaybookInclude
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.playbook.block import Block

# Generated at 2022-06-13 08:53:08.096606
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    meta = "meta/main.yml"
    #specify a metafile
    meta_data = RoleMetadata(meta)
    Build_Role_Metadata = {
        "allow_duplicates": False,
        "dependencies": [],
    }
    assert meta_data == Build_Role_Metadata

# Generated at 2022-06-13 08:53:14.015583
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    '''
    This function tests the loading of RoleMetadata methods
    '''

    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.role.requirement import RoleRequirement
    from ansible.playbook.play_context import PlayContext
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager

    # Role Definition object
    role_definition = RoleDefinition()

    # Inventory
    inventory = InventoryManager(loader=None, sources=None, vault_secrets=None)

    # Variable manager
    variable_manager = VariableManager(loader=None, inventory=inventory)

    # PlayContext
    play_context = PlayContext()

    # Data structure to pass to the role metadata object

# Generated at 2022-06-13 08:53:26.489619
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    rm = RoleMetadata()
    data = dict(
        allow_duplicates=True,
        dependencies=["geerlingguy.postgresql"]
    )
    rm.deserialize(data)
    assert getattr(rm, 'allow_duplicates') is True
    assert getattr(rm, 'dependencies') == ["geerlingguy.postgresql"]

# Generated at 2022-06-13 08:53:36.563716
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    # This is the ansible role definition in the role's meta/main.yml file
    data = {
        'allow_duplicates': False,
        'dependencies': [
            {'role': 'geerlingguy.java'},
            {'role': 'geerlingguy.mysql'},
            {'role': 'geerlingguy.apache'},
            {'role': 'geerlingguy.elasticsearch'}
        ]
    }
    # This is the role object under test
    role = RoleMetadata(owner=None)
    role.load(data=data, owner=None, variable_manager=None, loader=None)
    # This is the assert statement comparing the actual and expected data
    assert role

# Generated at 2022-06-13 08:53:43.357153
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    from ansible.playbook.role.definition import RoleDefinition

    r = RoleDefinition.load({
        'name': 'test-role',
        'tasks': {'main.yml': 'test123'}
    })
    m = RoleMetadata(owner=r)

    assert m._owner == r
    assert m._dependencies == []
    assert m._allow_duplicates == False



# Generated at 2022-06-13 08:53:50.300354
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.playbook.role.definition import RoleDefinition


# Generated at 2022-06-13 08:53:51.859513
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    assert False, "No test for RoleMetadata load implemented"

# Generated at 2022-06-13 08:53:54.288419
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    role = RoleMetadata(owner=None)
    assert role.allow_duplicates == False
    assert role.dependencies == []

# Generated at 2022-06-13 08:54:02.282608
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    print()
    print("test RoleMetadata.load method")
    print()

    class MockRole(object):
        def __init__(self, name, role_path=None, role_collection=None, collection_search_list=None):
            self.name = name
            self.collections = collection_search_list or []
            self.is_role_collection = (role_collection is not None)
            self._role_collection = role_collection
            self._play = None
            self._role_path = role_path

    class MockPlay(object):
        def __init__(self, variable_manager=None, loader=None):
            self._variable_manager = variable_manager
            self._loader = loader


# Generated at 2022-06-13 08:54:04.891935
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    role_metadata = RoleMetadata()
    role_metadata._allow_duplicates = True
    role_metadata._dependencies = ['role_1', 'role_2']

    assert role_metadata.serialize() == {'allow_duplicates': True, 'dependencies': ['role_1', 'role_2']}

# Generated at 2022-06-13 08:54:14.462038
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.playbook.role import Role
    from ansible.inventory.host import Host

    role_path = os.path.join(os.path.dirname(__file__), '../../../test/support/test_roles/role_include')
    role = Role.load(role_path)
    host = Host()

    assert role.get_dependencies() == [{'role': 'test_role_x'}, {'role': 'test_role_y'}]

    role_included_x = role.get_initial_role_dependencies().pop()
    assert role_included_x.get_name() == 'test_role_x'

# Generated at 2022-06-13 08:54:22.370638
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    print('Test: serialize of class RoleMetadata')

    # Create a RoleMetadata object
    roleMetadata = RoleMetadata()

    # Create expected data
    expected_data = dict(
        allow_duplicates=False,
        dependencies=list()
    )

    # Serialize the RoleMetadata
    data = roleMetadata.serialize()

    # Verify serialized data is as expected
    assert data == expected_data

    print('Test: serialize of class RoleMetadata: Success')


# Generated at 2022-06-13 08:54:30.475010
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.playbook.role.definition import RoleDefinition
    rd = RoleDefinition()
    rm = RoleMetadata(owner=rd)
    d = dict()
    rm.load(d, rd)

# Generated at 2022-06-13 08:54:41.160748
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.block import Block
    import yaml
    yaml_data = """
    - hosts: localhost
      tasks:
      - name: This is a task
        ping:
"""
    play_ds = yaml.safe_load(yaml_data)
    play = Play().load(play_ds, variable_manager=None, loader=None)
    play_context = PlayContext()
    role_ds = dict(
        dependencies=['path/to/the/dependencies/file']
    )

    role_metadata = RoleMetadata().load(role_ds, owner=play)
    role_metadata.serialize()


# Generated at 2022-06-13 08:54:46.467693
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    role_metadata = RoleMetadata()

    role_metadata._allow_duplicates = True
    role_metadata._dependencies = []
    serialized_metadata = role_metadata.serialize()
    assert serialized_metadata.get('allow_duplicates')
    assert serialized_metadata.get('dependencies') == []


# Generated at 2022-06-13 08:54:57.569342
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    data = {
        'allow_duplicates' : True,
        'dependencies' : [
            {
                'role'        : 'foo',
                'scm'         : 'git',
                'src'         : 'git://forge.example.com/path/to/role',
                'version'     : 'v1.2',
                'name'        : 'role_name',
                'private'     : True,
                'path'        : 'roles/foo',
                'force'       : True,
                'environment' : {
                    'FOO' : 'bar'
                },
            }
        ]
    }

    m = RoleMetadata()
    m.load(data)
    assert m._allow_duplicates == data['allow_duplicates']
    assert m._dependencies == data

# Generated at 2022-06-13 08:55:01.234977
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    data = dict(
        dependencies=['foo', 'bar'],
        allow_duplicates=True
    )

    result = RoleMetadata().deserialize(data).serialize()

    assert result == data


# Generated at 2022-06-13 08:55:01.989627
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    pass

# Generated at 2022-06-13 08:55:02.976165
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    pass



# Generated at 2022-06-13 08:55:05.434753
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    obj = RoleMetadata()
    actual = obj.serialize()
    assert actual == {'allow_duplicates': False, 'dependencies': []}, actual

# Generated at 2022-06-13 08:55:20.964404
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.play import Play
    from ansible.playbook.role.requirement import RoleRequirement
    from ansible.playbook.role.include import RoleInclude
    from ansible.playbook.base import Base
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    import collections

    # dependence is not a list
    data = dict(
        allow_duplicates=True,
        dependencies=dict())

    try:
        RoleMetadata.load(data, owner=None)
    except AnsibleParserError as e:
        assert str(e) == 'Expected role dependencies to be a list.'

    # dependence is not a dict

# Generated at 2022-06-13 08:55:23.417736
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    rd = RoleMetadata(owner=None)
    assert rd is not None

# Generated at 2022-06-13 08:55:38.663089
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.playbook.role.definition import RoleDefinition
    import ansible.playbook.play_context

    class Dummy(object):
        def __init__(self):
            self._role_path = '/foo/bar'
            self._play = ansible.playbook.play_context.PlayContext()
            self._role = ansible.playbook.role.definition.RoleDefinition(
                None,
                '/foo/bar'
            )
            self._parent = None
            self.get_name = lambda: 'test'

    data = dict(
        allow_duplicates=False,
        dependencies=[],
        galaxy_info=dict(),
    )
    metadata = RoleMetadata.load(data, Dummy())
    assert isinstance(metadata, RoleMetadata)

# Generated at 2022-06-13 08:55:41.752315
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    m = RoleMetadata()
    mf = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'test_role_metadata.yml')
    data = m._loader.load_from_file(mf)
    m.load(data)

# Generated at 2022-06-13 08:55:45.838616
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    m = RoleMetadata(None)
    m.allow_duplicates = True
    m.dependencies = ['apache', 'nginx']
    assert m.serialize() == {
        'allow_duplicates': True,
        'dependencies': ['apache', 'nginx'],
    }

# Generated at 2022-06-13 08:55:57.278796
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    # test_data is a dictionary with key as the attributes of class RoleMetadata
    # and value as the corresponding value.
    test_data = {
        'dependencies': ['role1', 'role2'],
        'allow_duplicates': True
    }
    # create a new RoleMetadata object
    r = RoleMetadata()
    # set the value of all the attributes of RoleMetadata object
    # with the values from test_data
    r.deserialize(test_data)
    # test if the values of attributes in RoleMetadata object is
    # equal to the values in test_data

# Generated at 2022-06-13 08:56:04.078345
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    ''' constructor '''

    # (name, path, task_include)
    mock_role = MockRoleObj('name', '/path/')

    meta = RoleMetadata(owner=mock_role)
    assert meta._owner.name == 'name'
    assert meta._owner.path == '/path/'

# Generated at 2022-06-13 08:56:16.010033
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    # test invalid yaml
    yaml_data_1 = ['1']
    yaml_data_2 = {'name':'role'}
    yaml_data_3 = {'name':'role', 'dependencies':'2'}
    try:
        RoleMetadata.load(yaml_data_1, None)
        assert False
    except AnsibleParserError as err:
        assert err.message == "the 'meta/main.yml' for role None is not a dictionary"

    try:
        RoleMetadata.load(yaml_data_2, None)
        assert False
    except AnsibleParserError as err:
        assert err.message == "the 'meta/main.yml' for role None is not a dictionary"

    # test 'dependencies' is a list

# Generated at 2022-06-13 08:56:20.005184
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    rmd = RoleMetadata()
    rmd.allow_duplicates = True
    rmd.dependencies = ["role", "role2"]
    data_ser = rmd.serialize()
    assert data_ser["allow_duplicates"] == True
    assert data_ser["dependencies"] == ["role", "role2"]


# Generated at 2022-06-13 08:56:22.806308
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    role_metadata = RoleMetadata(owner=None)
    assert role_metadata._allow_duplicates == False
    assert role_metadata._dependencies == []
    assert role_metadata._galaxy_info == None
    assert role_metadata._argument_specs == {}

# Generated at 2022-06-13 08:56:25.300156
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    RoleMetadata.deserialize({ 'allow_duplicates': True, 'dependencies': ['role1', 'role2', 'role3'] })

# Generated at 2022-06-13 08:56:35.081393
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.playbook.role.definition import RoleDefinition

    current_role_path = '../'

    def mock_load_list_of_roles(roles, play, current_role_path, variable_manager, loader, collection_search_list):
        return [RoleDefinition.load_from_file('abc', current_role_path, variable_manager, loader)]

    RoleMetadata.load_list_of_roles = mock_load_list_of_roles

    m = RoleMetadata.load([{'src':'galaxy.role,version,name', 'other_vars':"here"}, 'xyz'], current_role_path)

    assert m._dependencies == [{'src':'galaxy.role,version,name', 'other_vars':"here"}, 'xyz']

# Generated at 2022-06-13 08:56:58.127731
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    # setup
    galaxy_info = dict(author='joe', name='foobar')
    data = dict(
        allow_duplicates=True,
        dependencies=galaxy_info
    )

    # test
    role_metadata = RoleMetadata()
    role_metadata.deserialize(data)

    # assert
    assert role_metadata.allow_duplicates
    assert role_metadata.dependencies['author'] == 'joe'
    assert role_metadata.dependencies['name'] == 'foobar'

# Generated at 2022-06-13 08:57:03.810196
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():

    # Test with no dependencies
    dependencies = []
    data = dict(
        dependencies = dependencies,
    )

    m = RoleMetadata()
    m.deserialize(data)

    assert dependencies == m.dependencies


# Generated at 2022-06-13 08:57:11.946418
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    from ansible.playbook.role.include import RoleInclude
    from ansible.playbook.role.definition import RoleDefinition

    data = dict(
        allow_duplicates=True,
        dependencies=[
          { "src": "testRole", "name": "testRole" },
          { "src": "testRole2", "name": "testRole2" },
        ],
    )

    role_meta = RoleMetadata().deserialize(data)
    assert role_meta.allow_duplicates == True

    # Test dependencies
    assert isinstance(role_meta.dependencies[0], RoleInclude)
    assert isinstance(role_meta.dependencies[1], RoleInclude)
    assert isinstance(role_meta.dependencies[0]._role_definition, RoleDefinition)

# Generated at 2022-06-13 08:57:22.859143
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    from ansible.playbook.role.definition import RoleDefinition
    import os

    role = RoleDefinition.load('/roles/test', None, None, None, parent_role=None, role_path='/roles')
    meta_file = '/roles/test/meta/main.yml'
    ds = {'allow_duplicates': False, 'dependencies': []}
    RoleMetadata.deserialize(ds)
    assert 'allow_duplicates' in ds
    assert 'dependencies' in ds

    role.deserialize(ds)
    assert role._allow_duplicates == False
    assert role._dependencies == []

    # Test that galaxy_info doesn't get defined when it
    # is not in the role's meta file

# Generated at 2022-06-13 08:57:33.227125
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.plugins.loader import role_loader

    # create an instance of the RoleMetadata whose _load_dependencies() we're going to test
    role_dir = os.path.dirname(os.path.dirname(__file__))
    role_dir = os.path.join(role_dir, 'data', 'test_role_metadata')

    # create a RoleDefinition associated with the test_role_metadata
    rd = RoleDefinition()
    rd._role_path = os.path.join(role_dir, 'meta', 'main.yml')

    # load the test_role_metadata
    rm = RoleMetadata(owner=rd)

# Generated at 2022-06-13 08:57:39.062458
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    role_file = 'test/unit/plugins/meta/thinkup.subdir/meta/main.yml'
    from ansible.playbook.role import Role
    test_role = Role.load(role_file)
    assert test_role.metadata.serialize() == {'allow_duplicates': False, 'dependencies': ['common']}

# Generated at 2022-06-13 08:57:48.504671
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.playbook import Playbook, Play
    from ansible.inventory.manager import InventoryManager

    inv_path = '/tmp/inventory'
    groupvars_path = '/tmp/inventory_group_vars'
    hostvars_path = '/tmp/inventory_host_vars'
    inv_data = {
        "all": {
            "children": ["ungrouped"]
        },
        "ungrouped": {}
    }

    # write data to yaml files
    for path in [inv_path, groupvars_path, hostvars_path]:
        with open(path, 'w') as yaml_file:
            yaml_file.write('{}\n')

    # Init inventory object
    inventory = InventoryManager(loader=None, sources=inv_path)

    # Init variable manager object


# Generated at 2022-06-13 08:57:55.214418
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    import pytest
    from ansible.playbook.deprecated import DeprecatedRole
    from ansible.playbook.role.include import RoleInclude
    from ansible.playbook.role.metadata import RoleMetadata
    from ansible.playbook.role.requirement import RoleRequirement
    r = RoleMetadata()

# Generated at 2022-06-13 08:58:00.654437
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    role_metadata = RoleMetadata()
    role_metadata._allow_duplicates = "true"
    role_metadata._dependencies = ['ansible_role1', 'ansible_role2']
    result = role_metadata.serialize()
    assert result['allow_duplicates'] == "true"
    assert result['dependencies'] == ['ansible_role1', 'ansible_role2']

# Generated at 2022-06-13 08:58:04.996619
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    # GIVEN
    data = dict()
    data['allow_duplicates'] = True
    data['dependencies'] = ['test1', 'test2']
    rm = RoleMetadata()

    # WHEN
    rm.deserialize(data)

    # THEN
    assert rm._allow_duplicates is True
    assert rm._dependencies == ['test1', 'test2']

# Generated at 2022-06-13 08:58:38.409100
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    m = RoleMetadata()
    m.deserialize({
        'allow_duplicates': True
    })
    assert m.allow_duplicates is True

    m.deserialize({
        'dependencies': [
            'name',
            'src',
            'role1',
            'role2',
            'role3'
        ]
    })
    assert m.dependencies == ['name', 'src', 'role1', 'role2', 'role3']


# Generated at 2022-06-13 08:58:42.107951
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    filepath = './ansible/playbook/__init__.py'
    role = RoleMetadata(filepath)
    role._load_dependencies()

# Generated at 2022-06-13 08:58:45.838312
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    data = { 'allow_duplicates': True, 'dependencies': ['roles/x.y'] }
    m = RoleMetadata()
    assert m.deserialize(data) == data

# Generated at 2022-06-13 08:58:49.737858
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():

    class Role():
        name = "test_role"

    role = Role()

    from units.mock.loader import DictDataLoader
    loader = DictDataLoader({
        './test_role/meta/main.yml': 'dependencies:\n - { role: "test_role1" }\n',
    })

    role_metadata = RoleMetadata.load({}, owner=role, loader=loader)

    assert role_metadata._dependencies == [{'role': 'test_role1'}]

# Generated at 2022-06-13 08:58:51.222189
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    RoleMetadata(owner="1")

# Generated at 2022-06-13 08:58:55.162622
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    main = {'allow_duplicates': True, 'dependencies': ['geerlingguy.apache', 'geerlingguy.mysql']}
    m = RoleMetadata()
    m.load_data(main)
    assert m.serialize() == main


# Generated at 2022-06-13 08:59:04.178705
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    import json
    import os
    import pytest
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.role.requirement import RoleRequirement
    from ansible.playbook.role.include import RoleInclude

    fixture_path = os.path.join(os.path.dirname(__file__), '../fixtures/role_meta_include.yml')
    with open(fixture_path, 'r') as f:
        test_data = json.load(f)

    for data in test_data:
        role_meta = RoleMetadata()
        role_meta.deserialize(data['deserialize'])
        assert getattr(role_meta, 'allow_duplicates') == data['allow_duplicates']

# Generated at 2022-06-13 08:59:04.804096
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    role_metadata = RoleMetadata()

# Generated at 2022-06-13 08:59:08.205211
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    data = {'allow_duplicates': False,
            'dependencies': []}
    m_r_m = RoleMetadata()
    m_r_m.deserialize(data)
    assert m_r_m.allow_duplicates == data.get('allow_duplicates', False)
    assert m_r_m.dependencies == data.get('dependencies', [])

# Generated at 2022-06-13 08:59:14.241366
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.playbook.role import Role
    from ansible.playbook.role.definition import RoleDefinition
    role_name = 'test_role'
    collection_name = 'test.collection'
    role_path = '/test/role/path'
    role = Role.load(role_name, role_path, {}, False, collection_name=collection_name)
    parent_role = RoleDefinition.load(
        role_name, role_path, {}, False, collection_name=collection_name, parent_role=role)
    loaded_role_metadata = RoleMetadata.load({'dependencies': 'test_role'}, parent_role)
    assert len(loaded_role_metadata.dependencies) == 1

# Generated at 2022-06-13 09:00:04.534892
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    from ansible.playbook.role.definition import RoleDefinition

    m = RoleMetadata()
    m.deserialize({'dependencies': []})
    assert m.dependencies == []

    m = RoleMetadata()
    m.deserialize({'dependencies': [
        RoleDefinition({
            'name': 'apache'
        })
    ]})
    assert str(m.dependencies[0]) == 'Role(apache,None,None)'

    m = RoleMetadata()
    m.deserialize({'allow_duplicates': True})
    assert m.allow_duplicates == True

# Generated at 2022-06-13 09:00:10.777561
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    "Unit test for method serialize of class RoleMetadata"

    def test_RoleMetadata_serialize_temp_data():
        "temp data for RoleMetadata.serialize"

        from ansible.playbook.helpers import load_list_of_roles

        owner = "owner"
        variable_manager = "variable_manager"
        loader = "loader"
        data = {
            "allow_duplicates": True,
        }
        roles = [{
            "name": "geerlingguy.ntp",
        }]
        context = {
            "play": "play",
            "current_role_path": "current_role_path",
            "variable_manager": variable_manager,
            "loader": loader,
            "collection_search_list": ["ansible.legacy"],
        }

       

# Generated at 2022-06-13 09:00:15.581257
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    owner = None
    data = dict(
        allow_duplicates=False,
        dependencies=[]
    )
    result = RoleMetadata.load(data, owner)
    expected_result = dict(
        allow_duplicates=False,
        dependencies=[]
    )
    assert result.serialize() == expected_result

# Generated at 2022-06-13 09:00:22.169788
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    print("RoleMetadata.deserialize")
    test_obj_deserialize = RoleMetadata()
    test_obj_deserialize.deserialize(dict(
        allow_duplicates=True,
        dependencies=['test1', 'test2'],
    ))
    assert test_obj_deserialize._allow_duplicates is True
    assert test_obj_deserialize._dependencies == ['test1', 'test2']


# Generated at 2022-06-13 09:00:29.086261
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    import ansible.playbook
    from ansible.playbook.role.definition import RoleDefinition

    def _create_role_definition(name, path):
        rd = RoleDefinition()
        rd._role_name = name
        rd._role_path = path
        return rd

    rd = _create_role_definition("name", "path")

    md = RoleMetadata.load({}, rd)
    assert(isinstance(md, RoleMetadata))
    assert(md.dependencies is not None)
    assert(md.allow_duplicates is False)
    assert(md._owner == rd)
    assert(md.galaxy_info is None)
    assert(md.argument_specs is None)


# Generated at 2022-06-13 09:00:38.938098
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():

    from ansible.playbook.role import ROLE_CACHE
    for r in ROLE_CACHE.values():
        if r.get_name() == 'test_role':
            assert r.metadata.allow_duplicates == False

    # assert that we get an error for the not-a-dictionary case
    from ansible.playbook import Play
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager

    loader = DataLoader()
    variable_manager = VariableManager()
    play = Play()

    meta_path = os.path.join(os.path.dirname(__file__), 'data', 'meta', 'not-a-dict.yml')
    meta_data = loader.load_from_file(meta_path)

    r = Role

# Generated at 2022-06-13 09:00:46.972316
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():

    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.role.include import RoleInclude

    rd = RoleDefinition()
    rd.load(dict(name="some_role", role_path="/some/path"))

    # if a non-dictionary data structure is passed, should get error
    # if no role is passed, should get error
    # if role doesn't have a name, should get error
    # if role has a name and no path, should get error

    ri = RoleInclude()

    # if a non-dictionary data structure is passed, should get error
    # if no role is passed, should get error
    # if role doesn't have a name, should get error
    # if role has a name and no path, should get error

# Generated at 2022-06-13 09:00:57.694818
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():

    # Init owner
    from ansible.playbook.role import Role
    owner = Role()
    owner._role_path = 'ansible/playbook'

    # Empty meta/main.yml
    data = {}
    try:
        m = RoleMetadata.load(data, owner, variable_manager=None, loader=None)
        assert 0
    except AnsibleParserError as e:
        print(e)
        assert 1

    # meta/main.yml with invalid data
    data = {'version': '1.0'}
    try:
        m = RoleMetadata.load(data, owner, variable_manager=None, loader=None)
        assert 0
    except AnsibleParserError as e:
        print(e)
        assert 1

    # meta/main.yml with valid data

# Generated at 2022-06-13 09:01:03.488067
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    from ansible.playbook.play import Play
    play = Play.load(dict(name='my play'), variable_manager=None, loader=None)
    from ansible.playbook.role_include import RoleInclude
    role_dependencies = [RoleInclude.load(dict(role=dict(name='my role')), play=play)]
    role_metadata = RoleMetadata.load(dict(
        allow_duplicates=False,
        dependencies=role_dependencies))
    assert role_metadata.serialize() == dict(
        allow_duplicates=False,
        dependencies=role_dependencies)


# Generated at 2022-06-13 09:01:13.123990
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    role_metadata = RoleMetadata.load('playbook/roles/test/meta/main.yml', None)
    assert role_metadata
    assert role_metadata.dependencies == [{'role': 'role1', 'collection': 'collection1',
                                           'name': 'role1', 'version_requirement': 'v1.0.0'},
                                          {'role': 'role2', 'collection': 'collection2',
                                           'name': 'role2', 'version_requirement': 'v2.0.0'}]