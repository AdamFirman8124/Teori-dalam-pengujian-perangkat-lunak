

# Generated at 2022-06-13 08:52:14.609364
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    role_metadata = RoleMetadata()
    role_metadata.deserialize(dict(allow_duplicates=True, dependencies=[]))
    assert role_metadata.allow_duplicates
    assert role_metadata.dependencies == []

# Generated at 2022-06-13 08:52:19.956800
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    assert RoleMetadata.__doc__ is not None
    obj = RoleMetadata()
    assert obj is not None
    assert obj._allow_duplicates is False
    assert obj._dependencies == []
    assert obj._galaxy_info is None
    assert obj._argument_specs == {}

# Generated at 2022-06-13 08:52:25.052417
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    data = {}
    data_2 = {
        'allow_duplicates': True,
        'dependencies': [],
    }
    r = RoleMetadata()
    r.deserialize(data)
    assert not r.allow_duplicates and not r.dependencies
    r.deserialize(data_2)
    assert r.allow_duplicates and not r.dependencies

# Generated at 2022-06-13 08:52:32.002520
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():

    # create an instance of RoleMetadata
    module = RoleMetadata()

    # set the properties of the instance
    module.allow_duplicates = False
    module.dependencies = []

    # serialize the instance
    data = module.serialize()

    # compare the serialized instance with a reference copy
    assert data == dict(
        allow_duplicates=False,
        dependencies=[]
    )


# Generated at 2022-06-13 08:52:33.955855
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    role_metadata = RoleMetadata()
    assert isinstance(role_metadata, RoleMetadata)

# Generated at 2022-06-13 08:52:45.796196
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    # Unit test function:
    # method serialize of class RoleMetadata

    # 1. Init role metadata
    role_metadata = RoleMetadata()

    # 2. Serialize
    serialized_data = role_metadata.serialize()

    # 3. Check data
    assert serialized_data['allow_duplicates'] == False
    assert serialized_data['dependencies'] == []

    # 4. Init role metadata
    role_metadata = RoleMetadata()
    role_metadata.allow_duplicates = False
    role_metadata.dependencies = ['nginx']

    # 5. Serialize
    serialized_data = role_metadata.serialize()

    # 6. Check data
    assert serialized_data['allow_duplicates'] == False
    assert serialized_data['dependencies'] == ['nginx']

#

# Generated at 2022-06-13 08:52:46.407872
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    assert 1 == 1

# Generated at 2022-06-13 08:52:48.295427
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    lm = RoleMetadata()
    setattr(lm, 'allow_duplicates', True)
    setattr(lm, 'dependencies', "dependency")
    assert lm.serialize() == dict(allow_duplicates=True, dependencies=["dependency"])

# Generated at 2022-06-13 08:52:56.974864
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    role_name = 'testrole'
    role = RoleRequirement()
    role.name = role_name
    role_metadata = RoleMetadata(owner=role)
    assert role_metadata._owner == role
    assert role_metadata._allow_duplicates == False
    assert role_metadata._dependencies == []
    assert isinstance(role_metadata._galaxy_info, type(None))
    assert role_metadata._argument_specs == {}

if __name__ == '__main__':
    test_RoleMetadata()

# Generated at 2022-06-13 08:53:06.379789
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    from ansible.playbook.role.definition import RoleDefinition
    from six import StringIO


# Generated at 2022-06-13 08:53:21.789332
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.playbook.role_include import RoleInclude
    from ansible.playbook.role import Role
    from ansible.playbook import Play
    from ansible.playbook.block import Block
    from ansible.playbook.task_include import TaskInclude
    from ansible.inventory import Inventory
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    # 1st test
    # empty data should raise an AnsibleParserError
    data = None
    owner = Role()
    owner._role_path = '/tmp'
    owner._role_collection = None
    result = data

# Generated at 2022-06-13 08:53:28.238669
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    ds = dict(
        allow_duplicates=True,
        dependencies=[],
    )
    role_metadata = RoleMetadata()
    role_metadata.deserialize(data=ds)

    assert role_metadata.allow_duplicates == ds['allow_duplicates']
    assert role_metadata.dependencies == ds['dependencies']

# Generated at 2022-06-13 08:53:36.311077
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.role.include import RoleInclude

    role_def = RoleDefinition()
    role_def.name = 'test-role'
    role_def.path = '/tmp/galaxyr/roles/test-role'
    ri = RoleInclude()
    print("role directory is: " + str(role_def._role_path))
    print("role_def.name is: " + str(role_def.name))

    role_meta = RoleMetadata(owner=role_def)
    print("role_meta is: " + str(role_meta))


######################################################################
# main - for testing only
######################################################################
if __name__ == '__main__':
    test_RoleMetadata()

# Generated at 2022-06-13 08:53:46.951046
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    # Create a data dictionary
    data = { 'allow_duplicates': True, 'dependencies': ['test1', 'test2'] }
    # Create a RoleMetadata object
    rm = RoleMetadata()
    # Update the allow_duplicates and dependencies attributes based on data dictionary
    rm.deserialize(data)
    # Assert allow_duplicates is equal to True
    assert rm.allow_duplicates == True
    # Assert dependencies is equal to ['test1', 'test2']
    assert rm.dependencies == ['test1', 'test2']

if __name__ == '__main__':
    # Unit test for method deserialize of class RoleMetadata
    test_RoleMetadata_deserialize()

# Generated at 2022-06-13 08:53:54.388879
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    from ansible.playbook.play_context import PlayContext

    attrs = {
        'allow_duplicates': False,
        'dependencies': ['test1', 'test2']
    }

    import yaml
    yaml_data = yaml.dump(attrs, default_flow_style=False)

    obj = RoleMetadata(owner=PlayContext())
    obj.load_data(yaml_data)

    assert obj.serialize() == attrs

# Generated at 2022-06-13 08:53:58.190124
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    obj = RoleMetadata()
    obj._allow_duplicates = True
    obj._dependencies = ['a','b','c']
    ret = obj.serialize()
    assert ret == {'allow_duplicates':True,'dependencies':['a','b','c']}
    assert True


# Generated at 2022-06-13 08:54:04.360525
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    from ansible.playbook.role import Role
    role = Role.load('../../../test/units/metadata/role_meta_main/', name='foo', was_loaded=True)
    rolé = RoleMetadata(owner=role).load(role.metadata, owner=role)
    assert rolé.serialize()['dependencies'] == [{u'role': u'geerlingguy.pip', u'version': u'1.4.1'}]
    assert rolé.serialize()['allow_duplicates'] == True

# Generated at 2022-06-13 08:54:07.638459
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    rm = RoleMetadata()
    rm.deserialize({})
    assert rm.allow_duplicates == False
    assert rm.dependencies == []
    rm.deserialize({'allow_duplicates':True, 'dependencies':['test', 'test2']})
    assert rm.allow_duplicates == True
    assert rm.dependencies == ['test', 'test2']

# Generated at 2022-06-13 08:54:18.411750
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    body_str = '''
    - src: test_src
      version: 1.0
    '''
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.role.include import RoleInclude
    from ansible.plugins.loader import role_loader

# Generated at 2022-06-13 08:54:27.840712
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    from ansible.playbook.role import ROLE_CACHE
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.play_context import PlayContext

    rd = RoleDefinition()
    rd._role_name = 'foo'
    rd._role_path = '/path/to/foo'
    rd._play = object()
    rd._play_context = PlayContext()
    rd._loader = object()
    rd._variable_manager = object()

    ROLE_CACHE['foo'] = rd

    m = RoleMetadata()
    m.deserialize({'allow_duplicates': True, 'dependencies': [{'role': 'foo'}]})
    assert (m.allow_duplicates == True and m.dependencies != [])

# Generated at 2022-06-13 08:54:50.274607
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play

    def return_ansible_play(playbook, play_ds, variable_manager=None, loader=None):
        pc = PlayContext()
        playbook.set_loader(loader)
        pc._variable_manager = variable_manager

        p = Play().load(play_ds, variable_manager=variable_manager, loader=loader)
        p._play_context = pc
        p._variable_manager = variable_manager
        return p

    def return_role(parent, role_ds):
        role_path = "/path/to/roles/%s" % role_ds.get('name', 'role')
        return RoleMetadata(owner=parent).load(role_ds, parent, loader=loader)

    # test empty

# Generated at 2022-06-13 08:54:55.473434
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    role_metadata = RoleMetadata()
    data = {'allow_duplicates': True, 'dependencies': ['name', 7]}
    role_metadata.deserialize(data)
    assert role_metadata.allow_duplicates == True
    assert role_metadata.dependencies == ['name', 7]

# Generated at 2022-06-13 08:55:06.462823
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    from ansible.playbook.role import Role
    from ansible.playbook.role.include import RoleInclude
    from ansible.playbook.play import Play

    myplay = Play().load({
        'name': 'someplay',
        'hosts': 'somehosts',
        'roles': [{
            'role': 'some_role',
        }],
    }, variable_manager={}, loader=None)
    myrole = Role().load(
        data={
            'name': 'some_role',
        },
        play=myplay,
        variable_manager={},
        loader=None,
    )

# Generated at 2022-06-13 08:55:11.301820
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    role_metadata = RoleMetadata()
    role_metadata.allow_duplicates = False
    role_metadata.dependencies = 'test'
    assert role_metadata.serialize() == { 'allow_duplicates': False, 'dependencies': 'test' }

# Generated at 2022-06-13 08:55:18.158684
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.playbook.role import Role
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task_include import TaskInclude
    from units.mock.loader import DictDataLoader
    from units.mock.path import mock_unfrackpath_noop as mock_unfrackpath
    from ansible.vars.manager import VariableManager
    import ansible.constants as C


# Generated at 2022-06-13 08:55:28.916393
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    """
    Test if deserialize() method of class RoleMetadata returns an object of class RoleMetadata
    """
    import unittest
    import sys
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.role_include import RoleInclude
    from ansible.playbook.role_compatibility import RoleCompatibility
    from ansible.playbook.base import Base
    from collections import namedtuple

    MockObject = namedtuple('MockObject', ['serialize'])
    mock_object = MockObject(serialize=lambda: None)
    mock_role_definition = RoleDefinition(role_path='path')
    mock_object._role_definition = mock_role_definition

    mock_role_compatibility = RoleCompatibility(requirements_file='file')
    mock_object._role_

# Generated at 2022-06-13 08:55:38.951239
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.playbook import Playbook
    from ansible.playbook.role import Role
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from io import StringIO
    
    test_role_metadata=dict(
    allow_duplicates=False,
    dependencies=[]
    )

    # test passing in a dict
    s=StringIO(u'''---
- hosts: all
- roles:
    - role1
    - role2
    ''')
    
    play_ds=yaml.safe_load(s)

    templar = Templar(loader=None, variables={})
    pb = Playbook.load(play_ds, loader=None, variable_manager=VariableManager())

# Generated at 2022-06-13 08:55:41.752279
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    role = RoleMetadata()
    role.deserialize({"allow_duplicates": True, "dependencies": ["role1", "role2"]})
    assert role.allow_duplicates == True
    assert role.dependencies == ["role1", "role2"]

# Generated at 2022-06-13 08:55:48.605814
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    print("\n=== test_RoleMetadata_serialize ===")
    a = RoleMetadata(owner=None)
    a.dependencies = [1,2,3,4,5]
    a.allow_duplicates = True
    serialize_dict = a.serialize()
    print("serialize_dict = ", serialize_dict)
    assert serialize_dict['allow_duplicates'] == True
    assert serialize_dict['dependencies'] == [1,2,3,4,5]


# Generated at 2022-06-13 08:55:50.073832
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    RoleMetadata(owner="a")

# Generated at 2022-06-13 08:56:16.485988
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    owner = "owner"
    # Load empty data
    m = RoleMetadata.load(data={}, owner=owner)
    assert owner == m._owner
    assert isinstance(m, RoleMetadata)
    assert m.variables == {}
    assert m.attribute_overrides == {}
    assert m._ds == {}



# Generated at 2022-06-13 08:56:24.117717
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    data = {
        "_metadata": {
            "dependencies": [],
            "allow_duplicates": False
        }
    }
    role_metadata = RoleMetadata()
    role_metadata.deserialize(data)
    assert role_metadata.serialize() == {
        "dependencies": [],
        "allow_duplicates": False
    }

    data = {
        "_metadata": {
            "dependencies": [
                {
                    "role": "rolename"
                }
            ],
            "allow_duplicates": True
        }
    }
    role_metadata = RoleMetadata()
    role_metadata.deserialize(data)

# Generated at 2022-06-13 08:56:24.877611
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    pass

# Generated at 2022-06-13 08:56:25.868283
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    r = RoleMetadata()
    assert r

# Generated at 2022-06-13 08:56:28.706689
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():

    # Initialize data for RoleMetadata
    data = dict(
        allow_duplicates=True,
        dependencies=['test','test2']
    )

    # Deserialize data and get attributes
    rolemetadata = RoleMetadata()
    rolemetadata.deserialize(data)
    al_dupli = rolemetadata.allow_duplicates
    depend = rolemetadata.dependencies

    assert al_dupli == True
    assert depend == ['test','test2']

# Generated at 2022-06-13 08:56:31.163534
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():

    r = RoleMetadata(None)
    r.allow_duplicates = True
    r.dependencies = [1, 2, 3]
    r.serialize()

# Generated at 2022-06-13 08:56:38.428525
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    from ansible.playbook.role import Role
    from ansible.playbook.role.requirement import RoleRequirement
    owner = Role()
    role_meta = RoleMetadata(owner)

    role_meta_dict = {'allow_duplicates': True, 'dependencies': [
        {'role': 'my-requirements'},
        {'name': 'my-requirements'}]}

    setattr(owner, 'allow_duplicates', True)
    setattr(owner, 'dependencies', [RoleRequirement(owner, {'role': 'my-requirements'}), RoleRequirement(owner, {'name': 'my-requirements'})])

    assert role_meta.serialize() == role_meta_dict


# Generated at 2022-06-13 08:56:42.239194
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    r = RoleMetadata()
    r._allow_duplicates = False
    r._dependencies = []
    assert r.serialize() == {'allow_duplicates': False, 'dependencies': []}


# Generated at 2022-06-13 08:56:46.753582
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    RoleMetadata._allow_duplicates = False
    RoleMetadata._dependencies = []
    assert RoleMetadata.serialize() == dict(allow_duplicates=False,dependencies=[])
    RoleMetadata._allow_duplicates = True
    assert RoleMetadata.serialize() == dict(allow_duplicates=True,dependencies=[])

# Generated at 2022-06-13 08:56:49.543905
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    RoleMetadata.load(dict(a=1, b=2), None)

# Generated at 2022-06-13 08:58:11.856681
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    m = RoleMetadata(owner=None)
    ds = dict(
        allow_duplicates=False,
        dependencies=[]
    )
    assert ds == m.serialize()
    ds = dict(
        allow_duplicates=True,
        dependencies=[
            dict(role="role1"),
            dict(role="role2")
            ]
    )
    m.allow_duplicates = ds.get("allow_duplicates")
    m.dependencies = ds.get("dependencies")
    assert ds == m.serialize()

# Generated at 2022-06-13 08:58:17.224893
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    meta = RoleMetadata()

# Generated at 2022-06-13 08:58:23.339828
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    m = RoleMetadata()
    data = dict(
        allow_duplicates=True,
        dependencies=[{'role': 'bob.deploy'}],
    )
    m.deserialize(data)
    assert m._allow_duplicates
    assert m.allow_duplicates
    assert len(m.dependencies) == 1
    assert m.dependencies[0].get_name() == 'bob.deploy'

# Generated at 2022-06-13 08:58:40.053358
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    from ansible.playbook.role import Role
    from ansible.playbook.role.include import RoleInclude
    from ansible.playbook.role.requirement import RoleRequirement
    import os

    role = Role()
    role.name = 'myrole'
    role.role_path = os.path.abspath(os.path.join(os.getcwd(), './'))

    # test empty meta
    meta = RoleMetadata(owner=role)
    serialized_meta = meta.serialize()
    assert isinstance(serialized_meta, dict)
    assert 'allow_duplicates' not in serialized_meta
    assert 'dependencies' not in serialized_meta
    assert 'galaxy_info' not in serialized_meta

    # test with info on allow_duplicates and dependencies
   

# Generated at 2022-06-13 08:58:46.881562
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    roleMetadata = RoleMetadata()
    roleMetadata.allow_duplicates = 'true'
    roleMetadata.dependencies = ['roles/test.role', 'roles/test2.role']
    expected_result = {'allow_duplicates': 'true', 'dependencies': ['roles/test.role', 'roles/test2.role']}
    assert roleMetadata.serialize() == expected_result


# Generated at 2022-06-13 08:58:57.704546
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    from ansible.playbook.role import Role
    from ansible.plugins.loader import add_all_plugin_dirs
    from ansible.utils.collection_loader import AnsibleCollectionLoader
    from ansible.module_utils.collections.ansible_collections.ansible.builtin import ansible_builtin_collection_loader

    test_dir = os.path.join(os.path.dirname(__file__), 'test_data')

    # create a test role
    role = Role.load(os.path.join(test_dir, 'test_role_1'), None, None, None)

    # by default, Ansible doesn't find this collection
    assert 'ansible_test' not in ansible_builtin_collection_loader.collections

    # add this test directory to the plugins dir list so we can find the collection

# Generated at 2022-06-13 08:59:00.078773
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    r = RoleMetadata(owner=None)
    assert r.serialize() == {'allow_duplicates': False, 'dependencies': []}

# Generated at 2022-06-13 08:59:07.363811
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.module_utils.facts.system.distribution import Distribution
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.plugins import module_loader
    from ansible.template import Templar
    from ansible.utils.listify import listify_lookup_plugin_terms

    import yaml

    # Note: this is a basic test, only the bare minimum to get
    #       RoleMetadata.load() to return without error.
    #       It could be expanded to test more of the logic,
    #       but many of the methods (including load_data) have
    #       there own unit tests.

# Generated at 2022-06-13 08:59:14.212188
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.playbook.play import Play
    class DB(object):
        pass
    db = DB()
    db.playbook = DB()
    db.playbook.basedir = '.'
    db.loader = None
    db.variable_manager = None

    play = {}
    play['name'] = 'Test'
    play['hosts'] = 'all'
    play['roles'] = []
    play['vars'] = []

    # new style
    data = {"dependencies": [{"name": "role-src", "src": "git+http://github.com/some/role"}]}
    p = Play.load(data, db, play['name'], loader=db.loader, variable_manager=db.variable_manager)
    m = RoleMetadata.load(data, p)

# Generated at 2022-06-13 08:59:21.476938
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    m = RoleMetadata(owner=None)

    data = dict()
    setattr(data, 'allow_duplicates', True)
    setattr(data, 'dependencies', [])

    role_metadata = m.deserialize(data)

    assert True == role_metadata.allow_duplicates

# Generated at 2022-06-13 09:00:40.801815
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    class AnsibleRole:
        def __init__(self, name, role_path, play, collection=None):
            self._name = name
            self._role_path = role_path
            self._play = play
            self._role_collection = collection

    # Define the a role with name 'role_name' at path '/path/to/role/' within a play
    role = AnsibleRole('role_name', '/path/to/role', 'play')

    # Role metadata of the role 'role_name'
    metadata = {'allow_duplicates': True, 'dependencies': [{'role': 'common', 'some_parameter': 23}]}

    # Instance of the class RoleMetadata
    metadata_ob = RoleMetadata.load(metadata, role)

    # Serialize the class RoleMetadata
    serial

# Generated at 2022-06-13 09:00:47.037737
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():

    owner = object()
    m = RoleMetadata(owner=owner)
    assert m.serialize() == {
        'allow_duplicates': False,
        'dependencies': [],
    }

    m.allow_duplicates = True
    m.dependencies = [{'role': 'example.role1'}, {'role': 'example.role2'}]
    assert m.serialize() == {
        'allow_duplicates': True,
        'dependencies': [{'role': 'example.role1'}, {'role': 'example.role2'}],
    }


# Generated at 2022-06-13 09:00:49.641521
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    data_serialize = RoleMetadata(owner=None).serialize()
    assert isinstance(data_serialize, dict) == True


# Generated at 2022-06-13 09:00:59.264438
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():

    # Test 1: metadata without dependencies
    import re
    import os
    import sys
    import ansible.playbook
    import ansible.inventory
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.module_utils.common._collections_compat import Mapping

    loader = DataLoader()
    inventory = ansible.inventory.Inventory(loader=loader, variable_manager=VariableManager(), host_list=None)
    variable_manager = ansible.vars.manager.VariableManager(loader=loader, inventory=inventory)
    play_source = {}
    play = ansible.playbook.Play().load(play_source, variable_manager=variable_manager, loader=loader)
    role = ansible.playbook.Role()
    role._

# Generated at 2022-06-13 09:01:05.611596
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.playbook.play_context import PlayContext

    r = RoleMetadata.load(_METADATA_SAMPLE_1, None)
    assert r.allow_duplicates == True
    assert r.name == 'some_role'
    assert r.description == 'the description'
    assert len(r.dependencies) == 2
    dep1 = r.dependencies[0]
    assert dep1.get_name() == 'common'
    assert dep1.get_scm_url() is None
    dep2 = r.dependencies[1]
    assert dep2.get_name() == 'other_role'
    assert dep2.get_scm_url() == 'git://example.com/other_role.git'
    assert r.license == 'GPLv2'
    assert r.galaxy_

# Generated at 2022-06-13 09:01:22.362604
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.vars import combine_vars

    from ansible.module_utils.common._collections_compat import namedtuple
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText

# Generated at 2022-06-13 09:01:26.308289
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    role_meta_data = RoleMetadata()
    role_meta_data.allow_duplicates = True
    role_meta_data.dependencies = ['dependency-1', 'dependency-2']
    role_meta_data.serialize()



# Generated at 2022-06-13 09:01:33.632231
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    owner = None
    variable_manager = None
    loader = None
    data = {
        "allow_duplicates": True,
        "dependencies": [
        ]
    }
    role_metadata = RoleMetadata.load(data=data, owner=owner, variable_manager=variable_manager, loader=loader)
    result = role_metadata.serialize()
    assert result == data



# Generated at 2022-06-13 09:01:38.885554
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():

    # Basic usage
    role_metadata = RoleMetadata(owner=None)
    assert role_metadata._allow_duplicates is True
    assert role_metadata._dependencies == list()
    assert role_metadata.allow_duplicates == False
    assert role_metadata.dependencies == list()

# Generated at 2022-06-13 09:01:44.032949
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    data = {'allow_duplicates': False,
            'dependencies': []}
    m = RoleMetadata().load_data(data)
    assert m.allow_duplicates is False
    assert m.dependencies is not None
    assert len(m.dependencies) == 0