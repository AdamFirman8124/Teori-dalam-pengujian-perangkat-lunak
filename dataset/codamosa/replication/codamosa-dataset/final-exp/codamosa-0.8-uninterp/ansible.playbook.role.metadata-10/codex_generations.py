

# Generated at 2022-06-13 08:52:25.505210
# Unit test for constructor of class RoleMetadata

# Generated at 2022-06-13 08:52:31.995883
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    dependencies = [{'role': 'mysql'}, {'role': 'php'}]
    rolemetadata = RoleMetadata()
    rolemetadata._dependencies = dependencies
    rolemetadata._allow_duplicates = True
    rolemetadata_serialize = rolemetadata.serialize()
    assert rolemetadata_serialize['allow_duplicates'] == True
    assert rolemetadata_serialize['dependencies'] == dependencies


# Generated at 2022-06-13 08:52:32.886376
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    role_metadata = RoleMetadata()

# Generated at 2022-06-13 08:52:34.921783
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    data = RoleMetadata()
    assert data.allow_duplicates == False
    assert data.dependencies == []

# Generated at 2022-06-13 08:52:46.364935
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.parsing.mod_args import ModuleArgsParser
    from ansible.playbook.task import Task
    from ansible.playbook.play import Play
    from ansible.playbook.role import Role
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.role.include import RoleInclude
    from ansible.playbook.play_context import PlayContext
    from ansible.utils.display import Display
    from ansible.vars.manager import VariableManager

    display = Display()
    role_file_path = './test_roles/good_role/meta'
    role = Role.load(role_file_path)
    role_meta = role._metadata
    assert role_meta._allow_duplicates == True

# Generated at 2022-06-13 08:52:50.963841
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():

    result = RoleMetadata.load(data=dict(
        dependencies=[{'role': 'common', 'version': '1.0'}, 'prodsec'],
        allow_duplicates=True,
    ))

    assert len(result.dependencies) == 2
    assert result.dependencies[0].role == 'common' # Role include
    assert result.dependencies[0]._role_name == 'common'
    assert result.dependencies[0]._role_path is None
    assert result.dependencies[0]._role_search is None
    assert result.dependencies[1].role == 'prodsec' # Role name
    assert result.allow_duplicates == True

# Generated at 2022-06-13 08:52:53.145407
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    assert RoleMetadata().serialize() == {
        'allow_duplicates': False,
        'dependencies': list()
    }

# Generated at 2022-06-13 08:52:58.231554
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    role_metadata = RoleMetadata()
    setattr(role_metadata, 'allow_duplicates', True)
    setattr(role_metadata, 'dependencies', ['role1'])
    assert role_metadata.serialize() == dict(allow_duplicates = True,
                                             dependencies = ['role1'])


# Generated at 2022-06-13 08:52:59.691404
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    # This test ensures the creation of a RoleMetadata object is correctly done
    RoleMetadata()

# Generated at 2022-06-13 08:53:00.790239
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    RoleMetadata(owner=None)

# Generated at 2022-06-13 08:53:12.626692
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():

    role_metadata = RoleMetadata()
    setattr(role_metadata, 'allow_duplicates', False)
    setattr(role_metadata, 'dependencies', ['role1', 'role2'])

    # check serialized lists
    assert role_metadata.serialize() == {'allow_duplicates': False, 'dependencies': ['role1', 'role2']}


# Generated at 2022-06-13 08:53:16.917163
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    meta = RoleMetadata()
    data = dict(
        dependencies=dict(
            role='test',
            collections=['col']
        )
    )
    meta.deserialize(data)
    assert meta.dependencies[0] == dict(
        role='test',
        collections=['col']
    )

# Generated at 2022-06-13 08:53:30.105349
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    yaml_obj = '''
    allow_duplicates: false
    dependencies:
      - name: collection.namespace.role
        version: 2.2.1
      - name: community.general.role
        version: 1.0.0
      - { role: ansible.legacy.role, name: role_name }
    '''
    from ansible.parsing.yaml.dumper import AnsibleDumper
    from ansible.parsing.yaml.objects import AnsibleRole
    data = AnsibleDumper().parse_yaml_from_text(yaml_obj)
    r = RoleMetadata(owner=AnsibleRole())
    r.deserialize(data)
    assert not r._allow_duplicates
    assert len(r._dependencies) == 3

# Generated at 2022-06-13 08:53:38.182391
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play_context import PlayContext

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, sources=[])
    variable_manager.set_inventory(inventory)

    class FakePlay(object):
        def __init__(self):
            self._variable_manager = variable_manager
            self._tasks = []

        def get_variable_manager(self):
            return self._variable_manager

    fake_play = FakePlay()
    test_play_context = PlayContext(play=fake_play)


# Generated at 2022-06-13 08:53:46.098903
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.role.requirement import RoleRequirement
    rd = RoleDefinition()
    rm = RoleMetadata(rd)
    metadata_dict = {
        'allow_duplicates': False,
        'dependencies':[
            RoleRequirement(name='namelist1'),
            RoleRequirement(name='namelist2'),
        ]
    }
    rm.deserialize(metadata_dict)
    assert rm.serialize() == metadata_dict

# Generated at 2022-06-13 08:53:57.082142
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.utils.context_objects import Context

    meta_data = dict(
        allow_duplicates=True,
        dependencies=['ROLE1', 'ROLE2']
    )

    context = Context()
    context.CLIARGS = dict(
        connection='ssh',
        module_langage='python',
        forks=10,
        become=False,
        become_method='sudo',
        become_user='root',
        check=False,
        diff=True
    )

    rm = RoleMetadata.load(meta_data, None, context)
    assert rm
    assert rm.allow_duplicates

    rm_data = rm.serialize()
    assert rm_data

    assert rm_data.get('allow_duplicates') == meta_data.get('allow_duplicates')


# Generated at 2022-06-13 08:54:06.100137
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.playbook.role import Role
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.role.requirement import RoleRequirement

    # test 1, should succeed
    with open('../../test/units/support/meta/check') as f:
        meta = yaml.load(f)

    role_def = RoleDefinition(
        name='check',
        role_path='../../test/units/support/meta',
        collection_list=['ansible.legacy']
    )
    r = Role(name='check', role_definition=role_def)
    m = RoleMetadata.load(meta, r)

    assert len(m._dependencies) == 1
    assert m._dependencies[0].name == 'other'

    # test 2, should succeed

# Generated at 2022-06-13 08:54:10.956076
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.playbook.play import Play
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task

    metadata_data = {
        'dependencies': [{'role': 'geerlingguy.nginx'}]
    }

    variable_manager = VariableManager()
    loader = DataLoader()
    play = Play().load({}, variable_manager=variable_manager, loader=loader)
    block = Block()
    task = Task()
    block._parent = play
    task._parent = block
    task._role = dict(name='test')
    task._role_path = '/home/ansible/roles/test'
    task._loader = loader
    task._role_collection = None
    task._collections = [None]
    task._variable_manager = variable_manager


# Generated at 2022-06-13 08:54:22.625554
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():

    from ansible.playbook.role.definition import RoleDefinition

    def_1 = RoleDefinition()
    def_1._role_path = "ansible.galaxy.role.foo"
    def_1._name = "foo"

    def_2 = RoleDefinition()
    def_2._role_path = "ansible.galaxy.role.bar"
    def_2._name = "bar"

    def_3 = RoleDefinition()
    def_3._role_path = "ansible.galaxy.role.baz"
    def_3._name = "baz"

    # test with no definition
    rolemeta = RoleMetadata()
    rolemeta.serialize()

    # test with a dependency
    rolemeta = RoleMetadata()
    rolemeta._dependencies = [def_1]

# Generated at 2022-06-13 08:54:30.312153
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    import os
    import json
    import ansible.executor.module_common
    from ansible.executor.module_common import load_module_definition
    from ansible.module_utils.facts.system.distribution import Distribution

    ansible.executor.module_common.MODULE_COMMON_ARGSPEC = json.loads('''{
        "supports_check_mode": false,
        "supports_diff": false,
        "supports_private_key": false,
        "supports_no_log": false,
        "required_one_of": [],
        "mutually_exclusive": [],
        "required_together": [],
        "required_by": []
    }''')

    current_directory = os.path.dirname(__file__)

    module = load_module_definition

# Generated at 2022-06-13 08:54:42.151757
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    role_metadata = RoleMetadata()
    role_metadata.deserialize({"allow_duplicates": True, "dependencies": ["common"]})

    assert role_metadata.allow_duplicates == True
    assert role_metadata.dependencies == ["common"]

# Generated at 2022-06-13 08:54:45.312875
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    r = RoleMetadata()
    data = dict(
            allow_duplicates=False,
            dependencies=[]
        )
    r.deserialize(data)

# Generated at 2022-06-13 08:54:54.611491
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.role.requirement import RoleRequirement
    owner = RoleDefinition()
    owner._role_path = "/usr/local/lib/role"
    owner._role_name = "test"

# Generated at 2022-06-13 08:55:06.023604
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():

    # Testing constructor for class RoleMetadata
    # ****************************************************************
    # ****************************************************************

    # ****************************************************************
    # TEST CASE: Constructor RoleMetadata without arguments
    # ****************************************************************

    # Test comment: Constructor with default arguments
    # Test name: T11
    # Test description: Constructor of class RoleMetadata with no arguments
    # Test expected result: Instance of class RoleMetadata is created
    my_role_metadata = RoleMetadata()
    assert isinstance(my_role_metadata, RoleMetadata)

    # ****************************************************************
    # TEST CASE: Constructor RoleMetadata with one argument
    # ****************************************************************

    # Test comment: Constructor with owner argument
    # Test name: T12
    # Test description: Constructor of class RoleMetadata with owner argument
    # Test expected result: Instance of class RoleMetadata is created
    my

# Generated at 2022-06-13 08:55:07.410421
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    # TODO
    pass

# Generated at 2022-06-13 08:55:18.653769
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    json_data = """
    {
        "allow_duplicates": false,
        "dependencies": []
    }
    """
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    ds = DataLoader().load(json_data)
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=DataLoader(), sources=[])
    role = RoleMetadata()
    role.deserialize(ds)



# Generated at 2022-06-13 08:55:26.586800
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():

    # test normal execution with data
    data = {
        'dependencies': [{'role': 'Common'}]
    }
    role_metadata = RoleMetadata()
    role_metadata.deserialize(data)
    assert role_metadata.dependencies == [{'role': 'Common'}]

    # test with empty data
    data = {}
    role_metadata = RoleMetadata()
    role_metadata.deserialize(data)
    assert role_metadata.dependencies == []



# Generated at 2022-06-13 08:55:30.973790
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    role_path = '/home/cesar/Documentos/infraestructura_como_codigo/ansible/generador_stack_ec2/roles/test/'
    obj = RoleMetadata(owner=role_path)
    assert isinstance(obj, RoleMetadata)

# Generated at 2022-06-13 08:55:36.310414
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    meta = RoleMetadata()
    data = {'dependencies': [{'name': 'foo', 'src': 'bar', 'version_requirement': '1.2.4'}]}
    meta.deserialize(data)
    assert meta._dependencies == data.get('dependencies')
    assert meta._allow_duplicates == data.get('allow_duplicates', False)

# Generated at 2022-06-13 08:55:37.414223
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    metadata = RoleMetadata()

# Generated at 2022-06-13 08:55:57.383431
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():

    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.role.requirement import RoleRequirement
    fake_store = ['fake_role1', 'fake_role2', 'fake_role3']
    fake_play = 'fake_play'

    # Test with a empty ds
    m = RoleMetadata.load({}, fake_play)
    assert isinstance(m, RoleMetadata)
    assert m._owner == fake_play
    assert m._dependencies == []

    # Test with a simple ds
    ds = dict(
        dependencies=['fake_role1', 'fake_role3']
    )
    m = RoleMetadata.load(ds, fake_play)
    assert isinstance(m, RoleMetadata)
    assert m._owner == fake_play

# Generated at 2022-06-13 08:56:13.164879
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():

    from ansible.playbook.role.definition import RoleDefinition
    
    data = dict(
            allow_duplicates=True,
            dependencies=[
                dict(
                    role='iam.role',
                    vars=dict(
                        a=1,
                        b=2
                    )
                ),
                dict(
                    role='iam.role2',
                    vars=dict(
                        a=3,
                        b=4
                    )
                )
            ]
        )
    meta = RoleMetadata()

    meta.deserialize(data)
    assert meta.allow_duplicates == True
    for i in range(len(meta.dependencies)):
        assert meta.dependencies[i].name == data['dependencies'][i]['role']

# Generated at 2022-06-13 08:56:14.963829
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    m = RoleMetadata(owner='')
    assert m._allow_duplicates == False
    assert m._dependencies == []

# Generated at 2022-06-13 08:56:23.154012
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    import os
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    loader = DataLoader()
    variable_manager = VariableManager()
    role_path = os.path.join(loader.get_basedir(), '../test/support/roles/valid_role_names')
    rd = RoleDefinition.load(role_path, loader=loader, variable_manager=variable_manager)
    RoleMetadata_load = RoleMetadata.load(rd._metadata._data, rd, variable_manager=variable_manager, loader=loader)
    assert(RoleMetadata_load._owner == rd)
    assert(RoleMetadata_load.dependencies == [])

# Generated at 2022-06-13 08:56:25.772688
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    role_metadata = RoleMetadata()
    assert role_metadata.__class__.__name__ == 'RoleMetadata'
    assert isinstance(role_metadata, Base)

# Generated at 2022-06-13 08:56:30.702653
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():

    test_metadata = {
        'allow_duplicates': True,
        'dependencies': [
            {'role': 'foo'},
            {'role': 'bar', 'name': 'baz'}
        ]
    }

    assert RoleMetadata.load(data=test_metadata, owner=None) is not None

# Generated at 2022-06-13 08:56:38.588471
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    import os
    import shutil
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.playbook.playbook import Playbook

    def cleanup_tree(root_dir, is_playbook=False):
        dirs = [root_dir, '%s/roles' % root_dir]
        file_paths = ['meta/main.yml']
        if is_playbook:
            dirs.append('%s/group_vars' % root_dir)
            dirs.append('%s/host_vars' % root_dir)
            file_paths.append('site.yml')
            file_paths.append('hosts')

# Generated at 2022-06-13 08:56:42.414823
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    role = RoleMetadata()
    role.deserialize(dict(
        allow_duplicates = False,
        dependencies = []
    ))
    assert role.allow_duplicates == False
    assert role.dependencies == []

# Generated at 2022-06-13 08:56:46.628975
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    role = dict(
        allow_duplicates=True,
        dependencies=['test']
    )
    rm = RoleMetadata()
    rm.deserialize(role)
    rm.serialize()
    assert rm.allow_duplicates == True
    assert rm.dependencies == ['test']

# Generated at 2022-06-13 08:56:53.930681
# Unit test for constructor of class RoleMetadata

# Generated at 2022-06-13 08:57:17.841386
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    meta1 = RoleMetadata.load({}, None)
    assert meta1.dependencies == []
    assert meta1.allow_duplicates is False

    meta2 = RoleMetadata.load(dict(
        allow_duplicates=True,
        dependencies=['role1']), None)
    assert meta2.allow_duplicates is True
    assert meta2.dependencies == ['role1']

# Generated at 2022-06-13 08:57:25.945617
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    from ansible.playbook.role.collection import RoleCollection
    from ansible.galaxy import Galaxy
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars import VariableManager
    from ansible.galaxy.role import GalaxyRole
    from ansible.playbook.play import Play
    loader = DataLoader()
    galaxy = Galaxy(loader=loader, variable_manager=VariableManager())
    galaxy.init_roles_paths()


# Generated at 2022-06-13 08:57:27.671186
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    assert RoleMetadata().load({'allow_duplicates': False, 'dependencies': []}) is not None

# Generated at 2022-06-13 08:57:32.393996
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    from ansible.playbook import role

    role_name = 'test_role'

    role_data = {
        'allow_duplicates': False,
        'dependencies': ['role1', 'role2']
    }

    role_meta = role.RoleMetadata(role_name)
    role_meta._deserialize_data(role_data)

    assert role_meta.serialize() == role_data

# Generated at 2022-06-13 08:57:47.880537
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.play import Play
    from collections import namedtuple

    FakeVars = namedtuple('FakeVars', ['hostvars', 'host'])
    fake_vars = FakeVars({}, {})
    fake_play = Play().load({'name': 'fakeplay', 'hosts': 'all'})
    fake_play.ROLE_CACHE = {}
    fake_role = RoleDefinition()
    fake_role._role_path = 'fake/path'
    fake_role._role_name = 'fake_name'
    fake_role._role_collections = []

    # no need to instantiate self._owner,because it is None
    serialize_test_obj = RoleMetadata(None)

    serialize_test_

# Generated at 2022-06-13 08:57:50.671545
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from .test_role import TestRole

    test_role = TestRole()
    role_metadata = RoleMetadata.load(test_role.metadata_legacy(), owner=test_role.get_role())

# Generated at 2022-06-13 08:57:54.076558
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    metadata = RoleMetadata(owner="testOwner")
    assert metadata._allow_duplicates == False
    assert metadata._dependencies == []
    assert metadata._galaxy_info is None
    assert metadata._argument_specs == {}
    assert metadata._owner == "testOwner"

if __name__ == "__main__":
    test_RoleMetadata()

# Generated at 2022-06-13 08:57:59.584673
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    data = {'dependencies': ['test1', 'test2'], 'allow_duplicates': True}
    test_meta_data = RoleMetadata().deserialize(data)
    assert data['dependencies'] == test_meta_data.get('dependencies')
    assert data['allow_duplicates'] == test_meta_data.get('allow_duplicates')

# Generated at 2022-06-13 08:58:05.708895
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
  data = {}
  data['allow_duplicates'] = True
  data['dependencies'] = [
    {'role': 'common', 'version': '> 2.0'},
    {'role': 'geerlingguy.java', 'version': '> 1.0'},
  ]
  r = RoleMetadata()
  r.deserialize(data)
  print(r.serialize())
  r.allow_duplicates = False
  r.dependencies = []
  print(r.serialize())


# Generated at 2022-06-13 08:58:06.989200
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    roleMetaData = RoleMetadata()
    assert roleMetaData is not None

# Generated at 2022-06-13 08:58:44.065857
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    from ansible.playbook.role import Role
    from ansible.parsing.mod_args import ModuleArgsParser

    role = Role()

    # test init with no args
    role_metadata = RoleMetadata()
    assert role_metadata.__class__.__name__ == 'RoleMetadata'

    # test init with args
    role_metadata = RoleMetadata(owner=role)
    assert role_metadata.__class__.__name__ == 'RoleMetadata'

    # test load
    data = { 'dependencies': [ {'role': 'role1'}, {'role': 'role2'} ] }
    role_metadata = RoleMetadata(owner=role)
    role_metadata.load(data=data, variable_manager=None, loader=None)
    assert role_metadata.allow_duplicates == False


# Generated at 2022-06-13 08:58:50.823548
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.playbook.play import Play

    p = Play().load({
        'name': 'test',
        'hosts': 'localhost',
        'roles': [{
            'name': 'testrole',
            'tasks': [{
                'meta': {
                    'allow_duplicates': False,
                    'dependencies': [
                        'http://github.com/test/test-external-role',
                        'role_name',
                        {'role': 'role2', 'version': '1.2.3'},
                        {'role': 'role3', 'other_vars': 'here'}
                    ],
                    'galaxy_info': None
                }
            }]
        }]
    }, variable_manager=None, loader=None)

    assert p is not None

# Generated at 2022-06-13 08:58:56.883801
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    '''
    This function tests the deserialize function of RoleMetadata.
    Since deserialize calls serialize, it is tested in this context.
    '''

    obj = RoleMetadata()
    obj.deserialize( {'allow_duplicates': True, 'dependencies': ['dependency']} )
    assert(obj.serialize() == {'allow_duplicates': True, 'dependencies': ['dependency']})


# Generated at 2022-06-13 08:59:03.952520
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    # create a class with this test
    class Example(RoleMetadata):
        def __init__(self, data):
            self.data = data

        def deserialize(self, data):
            return data

    # check that deserialize has returned the same dict
    test = Example({'a': 'b'})
    assert test.deserialize({'a': 'b'}) == {'a': 'b'}

    # check that deserialize has returned a dict different from the one we have passed
    test2 = Example({'a': 5})
    assert test.deserialize({'a': 5}) == {'a': 5}

# Generated at 2022-06-13 08:59:07.055152
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    r = RoleMetadata()
    assert r.dependencies == []
    assert not r.galaxy_info

    r2 = RoleMetadata()
    assert r.dependencies == r2.dependencies
    assert r.galaxy_info == r2.galaxy_info

if __name__ == "__main__":
    test_RoleMetadata()

# Generated at 2022-06-13 08:59:13.903340
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():

    data = {
        "dependencies": [
            "role1",
            "role2",
            "role3",
            {
                "role": "role1",
                "scm": "git"
            }
        ]
    }
    m = RoleMetadata()
    load_list_of_roles = m.load(data, m)
    assert load_list_of_roles is not None
    assert len(load_list_of_roles) == 3
    assert isinstance(load_list_of_roles[0], RoleRequirement)
    assert isinstance(load_list_of_roles[1], RoleRequirement)
    assert isinstance(load_list_of_roles[2], RoleRequirement)
    assert load_list_of_roles[0].role == 'role1'

# Generated at 2022-06-13 08:59:31.098106
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext

    m = RoleMetadata()
    p = Play().load({
        'name': 'test play',
        'hosts': 'all',
        'roles': [
            {'role': 'geerlingguy.java', 'java_packages': ['foo', 'bar']},
            {'role': 'geerlingguy.mysql', 'mysql_root_password': 'baz'},
        ]
    }, variable_manager=None, loader=None)


# Generated at 2022-06-13 08:59:36.861276
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    assert RoleMetadata.deserialize({}) == dict(allow_duplicates=False)
    assert RoleMetadata.deserialize({'allow_duplicates': True}) == dict(allow_duplicates=True)
    assert RoleMetadata.deserialize({'dependencies': []}) == dict(dependencies=[])
    assert RoleMetadata.deserialize({'dependencies': [{'role': 'role1'}]}) == dict(dependencies=[{'role': 'role1'}])
    assert RoleMetadata.deserialize({'dependencies': [{'role': 'role1'}]}) == dict(dependencies=[{'role': 'role1'}])

# Generated at 2022-06-13 08:59:38.661140
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    obj = RoleMetadata()
    obj.allow_duplicates = False
    obj.dependencies = []
    assert obj.serialize() == {'allow_duplicates': False, 'dependencies': []}

# Generated at 2022-06-13 08:59:43.726586
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.playbook.helpers import load_list_of_roles
    from ansible.utils.vars import combine_vars
    from ansible.vars.manager import VariableManager
    from ansible.vars.hostvars import HostVarsVars
    from ansible.vars.reserved import DEFAULT_HASH_BEHAVIOUR
    import ansible.playbook.play_context

    class RoleInclude:
        def __init__(self, role_name, role_path, play_context, role_args=None, role_vars=None):
            self._role_name = role_name
            self._role_path = role_path
            self.vars = role_vars
            self._play_context = play_context
            self._role_args = role_args


# Generated at 2022-06-13 09:00:00.453168
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    m = RoleMetadata()
    m.deserialize({'allow_duplicates': True, 'dependencies': ['role1', 'role2']})
    assert m.allow_duplicates is True
    assert m.dependencies == ['role1', 'role2']

# Generated at 2022-06-13 09:00:02.742037
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    _x = {
        'allow_duplicates': False,
        'dependencies': []
    }
    assert RoleMetadata().serialize() == _x


# Generated at 2022-06-13 09:00:09.508597
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    temp_dependencies = [{
      "role": "myrole",
      "scm": "git",
      "src": "http://github.com/foo/bar.git"
    }, {
      "role": "myrole2",
      "src": "./"
    }, {
      "src": "/path/to/roles/role3"
    }, "role4", "role5"
    ]
    data = dict(
            allow_duplicates=False,
            dependencies=temp_dependencies
        )
    r = RoleMetadata()
    r.deserialize(data)
    assert r.allow_duplicates == data.get('allow_duplicates', False)
    assert r.dependencies == temp_dependencies

# Generated at 2022-06-13 09:00:12.673618
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    data = {
        'allow_duplicates': False,
        'dependencies': []
    }
    meta = RoleMetadata()
    meta.deserialize(data)
    assert meta._allow_duplicates is False
    assert len(meta._dependencies) is 0



# Generated at 2022-06-13 09:00:14.101276
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    m = RoleMetadata()

# Generated at 2022-06-13 09:00:24.263261
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.play import Play
    import ansible.playbook.role
    from ansible.playbook.role_context import RoleContext
    from ansible.executor.task_queue_manager import TaskQueueManager

    r = ansible.playbook.role.definition.RoleDefinition()
    p = ansible.playbook.play.Play().load({})
    r._play = p

    rc = ansible.playbook.role_context.RoleContext()
    rc.ROLE_CACHE = {}

    tqm = ansible.executor.task_queue_manager.TaskQueueManager()

    # init vars
    RoleDefinition.__init__(r)
    RoleContext.__init__(rc)

# Generated at 2022-06-13 09:00:31.066191
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    # Test case 1
    test_case_1 = RoleMetadata()
    assert test_case_1.serialize() == {'allow_duplicates': False, 'dependencies': []}

    # Test case 2
    test_case_2 = RoleMetadata()
    test_case_2.allow_duplicates = True
    test_case_2.dependencies = [{'src': 'test.test.test1', 'version': '1.0.0'}]
    assert test_case_2.serialize() == {'allow_duplicates': True, 'dependencies': [{'src': 'test.test.test1', 'version': '1.0.0'}]}

    # Test case 3
    test_case_3 = RoleMetadata()

# Generated at 2022-06-13 09:00:36.291919
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    # Fixtures
    data = {'dependencies': ['role1', 'role2']}
    owner = "AnsiblePlaybook"
    
    # Test
    obj = RoleMetadata(owner=owner)
    obj.load_data(data)

    # assert
    assert obj._dependencies == data.get('dependencies')
    assert obj._owner == owner

# Generated at 2022-06-13 09:00:37.147061
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    assert(False), "FIXME"


# Generated at 2022-06-13 09:00:45.880451
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    # If method load of class RoleMetadata is called with no parameters in its default values, an exception is raised
    try:
        RoleMetadata.load()
    except TypeError as e:
        assert str(e) == "load() missing 1 required positional argument: 'data'"
    # If method load of class RoleMetadata is called with incorrect parameters, an exception is raised
    try:
        RoleMetadata.load(42)
    except TypeError as e:
        assert str(e) == "load() takes at most 3 positional arguments (4 given)"
    try:
        RoleMetadata.load(42, 43, 44, 45)
    except TypeError as e:
        assert str(e) == "load() takes at most 3 positional arguments (4 given)"

# Generated at 2022-06-13 09:01:12.016034
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    role_metadata = RoleMetadata()
    assert role_metadata is not None


# Generated at 2022-06-13 09:01:12.993773
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    assert True

# Generated at 2022-06-13 09:01:27.795108
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    import unittest

    try:
        from unittest.mock import Mock
    except ImportError:
        from mock import Mock

    from ansible.playbook.role.meta import GalaxyInfo
    from ansible.playbook.role.requirement import RoleRequirement

    class TestRoleMetadata(unittest.TestCase):

        def setUp(self):
            self.mock_variable_manager = Mock()
            self.mock_loader = Mock()
            self.mock_owner = Mock()

        def tearDown(self):
            pass

        def test__load_dependencies_string(self):
            role_def = ['parent_role_name']

# Generated at 2022-06-13 09:01:31.106812
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    role = RoleMetadata()
    result = role.serialize()
    assert result['allow_duplicates'] == False
    assert result['dependencies'] == []


# Generated at 2022-06-13 09:01:44.786231
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    import mock
    import sys
    import __builtin__ as builtins

    mock_open_function = mock.Mock()
    open_name = '{0}.open'.format(__name__)
    setattr(builtins, open_name, mock_open_function)

    role_path = '/home/vagrant/ansible/roles/my_role'
    role_name = 'my_role'

# Generated at 2022-06-13 09:01:56.008156
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    meta_file = dict(
        galaxy_info=dict(
            author='Ansible',
            description='This is a noop role for testing some changes.',
            galaxy_tags=['test', 'noop'],
            platform='Debian',
            min_ansible_version='1.7',
            company='Ansible',
            license='GPL',
            roles_path='../'
        ),
        allow_duplicates=True,
        dependencies=[dict(name='geerlingguy.apache',
                           collections=[collect_name],
                           requirements_file='apache.yml')],
        )
    # Create an instance of class RoleMetadata
    role_meta = RoleMetadata()
    # Deserialize a role and play.

# Generated at 2022-06-13 09:02:03.059759
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.role.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.template import Templar

    fake_role_path = '/fake/path/to/role'
    fake_role = RoleDefinition.load('role1', fake_role_path, None, None, None, None)
    fake_task = Task.load(dict(
        action=dict(
            module='fake_module',
            args=dict(
                arg1='arg1',
                arg2='arg2',
            )
        )
    ), templar=Templar(loader=None, variables=dict()), play=fake_role._play)

    fake_role.tasks = [fake_task]
    fake_role