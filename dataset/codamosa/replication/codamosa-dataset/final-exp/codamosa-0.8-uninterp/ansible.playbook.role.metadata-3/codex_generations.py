

# Generated at 2022-06-13 08:52:23.554123
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    data = {"meta_data": "some_data"}
    assert isinstance(RoleMetadata(None), RoleMetadata)
    assert isinstance(RoleMetadata.load(data, None), RoleMetadata)
    assert isinstance(RoleMetadata.load(data, None)._load_dependencies("dependencies", None), list)
    assert isinstance(RoleMetadata.load(data, None)._load_galaxy_info("galaxy_info", None), dict)
    assert isinstance(RoleMetadata.load(data, None).serialize(), dict)

# Generated at 2022-06-13 08:52:27.851309
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    role = RoleMetadata()
    role.deserialize({'allow_duplicates': 'True', 'dependencies': ['a', 'b']})
    print(role.serialize())

if __name__ == '__main__':
    test_RoleMetadata_deserialize()

# Generated at 2022-06-13 08:52:29.947962
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():

    # Implicit test of load method of class RoleMetadata
    RoleMetadata.load(None, None, None, None)

# Generated at 2022-06-13 08:52:34.094570
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    rm = RoleMetadata()
    assert rm._owner == None
    assert rm._allow_duplicates == False
    assert rm._dependencies == []
    assert rm._galaxy_info == None
    assert rm._argument_specs == {}

# Generated at 2022-06-13 08:52:45.983287
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    from ansible.playbook.role import Role
    from ansible.galaxy import collections_loader
    from ansible.cli.galaxy import GalaxyCLI
    from ansible.galaxy.collection import CollectionRequirement

    loader = collections_loader.CollectionsLoader()

    roles1_path = os.path.join(os.path.dirname(__file__), '..', '..', 'test', 'unit', 'roles1')
    roles_path = os.path.join(os.path.dirname(__file__), '..', '..', 'test', 'integration', 'targets', 'test1')

    role_source = 'https://galaxy.server.com/api/v1/roles/namespace.rolename'
    test_role_req = CollectionRequirement.from_spec(role_source)

# Generated at 2022-06-13 08:52:51.515450
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    import sys
    import yaml

    meta = '''
    allow_duplicates: True
    dependencies:
      - {name: "role1"}
    '''

    role_metadata = RoleMetadata()
    role_metadata.deserialize(yaml.safe_load(meta))

    serialized_data = role_metadata.serialize()
    assert isinstance(serialized_data, dict)
    assert serialized_data.get('allow_duplicates')
    assert len(serialized_data.get('dependencies')) == 1

# Generated at 2022-06-13 08:52:56.366134
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    rm = RoleMetadata()
    assert rm.dependencies == [], "Initial RoleMetadata.dependencies should be an empty list"
    rm.deserialize({'dependencies': ['foo']})
    assert rm.dependencies == ['foo'], "After deserialize with dependencies=['foo'] expected RoleMetadata.dependencies to be ['foo']"

# Generated at 2022-06-13 08:53:02.435905
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    '''Unit test for method serialize of class RoleMetadata'''

    rolemetadata = RoleMetadata()
    rolemetadata.allow_duplicates = True
    rolemetadata.dependencies = [{ "role" : "role"}]

    data = rolemetadata.serialize()
    assert data.get("allow_duplicates") == True
    assert data.get("dependencies") == [{ "role" : "role"}]


# Generated at 2022-06-13 08:53:10.030482
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    meta_data = dict(
        allow_duplicates=True,
        dependencies=[
            dict(
                name='test',
                src='/path/to/role',
                version='1.0'
            ),
            dict(
                name='test',
                src='/path/to/role',
                version='1.0'
            ),
            dict(
                name='test',
                src='/path/to/role',
                version='1.0'
            ),
        ]
    )

    rm = RoleMetadata(owner=None)
    rm.deserialize(meta_data)

# Generated at 2022-06-13 08:53:16.750534
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.role.include import RoleInclude
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.handler import Handler
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.playbook.task_include import TaskInclude

# Generated at 2022-06-13 08:53:25.079632
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    # Create RoleMetadata object
    m = RoleMetadata()
    assert m.load({}, {})

# Generated at 2022-06-13 08:53:29.301734
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    data = dict(
        a=1,
        b=2,
        dependencies=['a', 'b']
    )
    test_obj = RoleMetadata()
    test_obj.deserialize(data)

    assert test_obj._dependencies == ['a', 'b']
    assert test_obj._allow_duplicates == False

# Generated at 2022-06-13 08:53:34.286981
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.playbook.role.definition import RoleDefinition
    data = {'dependencies': [{'role': 'one'}, {'role': 'two'}]}
    mock_owner = RoleDefinition()
    nm = RoleMetadata.load(data, mock_owner)
    assert len(nm._dependencies) == 2
    assert nm._dependencies[0]._role_name == 'one'
    assert nm._dependencies[1]._role_name == 'two'

# Generated at 2022-06-13 08:53:38.154341
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    r = RoleMetadata()
    r.allow_duplicates = True
    r.dependencies = ['role1', 'role2']
    assert r.serialize() == {'allow_duplicates': True, 'dependencies': ['role1', 'role2']}


# Generated at 2022-06-13 08:53:41.579608
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    metadata = RoleMetadata()
    metadata.dependencies = [{'role': 'common', 'foo': 'bar'}]
    metadata.allow_duplicates = True

    data = metadata.serialize()
    assert data['dependencies'][0]['role'] == 'common'
    assert data['dependencies'][0]['foo'] == 'bar'
    assert data['allow_duplicates']

# Generated at 2022-06-13 08:53:47.743849
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    m = RoleMetadata()
    assert m._allow_duplicates == False
    assert m._dependencies == []
    assert isinstance(m, Base)
    assert isinstance(m, CollectionSearch)
    assert isinstance(m, Block)
    assert isinstance(m, Task)
    assert not isinstance(m, type)
    assert m.__doc__

# Generated at 2022-06-13 08:53:48.303533
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    pass

# Generated at 2022-06-13 08:53:55.932808
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    meta_data = dict(allow_duplicates=False, dependencies=[{'role': 'galaxy.ansible.com,1.9.5-1,foo'}])
    mock_owner = MockRole()
    role_metadata = RoleMetadata.load(meta_data, mock_owner)
    assert role_metadata.allow_duplicates == meta_data['allow_duplicates']
    assert role_metadata.dependencies[0].role == meta_data['dependencies'][0]['role']


# Generated at 2022-06-13 08:54:04.805832
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    from ansible.playbook.collectionsearch import RoleInclude
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.role.role import Role

    ri = RoleInclude()
    ri.name="test_role1"
    ri.role=Role()
    ri.role.name="test_role1"
    ri.role.collection=None
    ri.role.role_path="<dir_of_playbook>/roles/test_role1"

    rd = RoleDefinition()
    rd.name = "test_role2"
    rd.role = None
    rd.role_path = "<dir_of_playbook>/roles/test_role2"
    rd.collection = None

    rd2 = RoleDefinition()
   

# Generated at 2022-06-13 08:54:14.406678
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.playbook.play import Play
    from ansible.playbook.role import Role

    play = Play()
    role = Role()
    role._role_path = './test/unit/lib/ansible/modules/files/'
    ds = dict(
        allow_duplicates=False,
        dependencies=[
            dict(
                name='test_role',
                src='test/test_role',
                scm='git',
                version='master',
                path='test/test_role',
            )
        ]
    )
    metadata = RoleMetadata.load(ds, owner=role)
    assert metadata.allow_duplicates == False
    assert len(metadata.dependencies) == 1
    assert metadata.dependencies[0].name == 'test_role'

# Generated at 2022-06-13 08:54:35.579551
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    '''
    In order to properly test the load function, a fake owner is created.
    We then create a fake variable_manager and loader.

    The loader is important to test whether the dependencies are properly
    created or not. Note that the dependencies are supposed to be list of
    RoleInclude, not a list of string.

    The variable_manager is important to test the role_yaml_parse functionality
    of RoleRequirement.
    '''

    import tempfile
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar

    # Fake owner
    class FakeOwner(object):
        def __init__(self):
            self._role_path = tempfile.mkdtemp()

    # Fake variable_manager
    class FakeVariableManager(object):
        def __init__(self):
            self.v

# Generated at 2022-06-13 08:54:38.117703
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    new_obj = RoleMetadata()
    assert new_obj.deserialize({"arg1": 1}) == {"arg1": 1}

# Generated at 2022-06-13 08:54:47.878877
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    from ..role.definition import RoleDefinition
    from ansible.playbook.play_context import PlayContext

    role_path = "./tests/sanity/roles/foobar_baz/meta"
    role_metadata = RoleMetadata()
    role_metadata._owner = RoleDefinition()
    role_metadata._owner._role_path = role_path
    data = dict(
        allow_duplicates=True,
        dependencies=["foobar", "barbaz"]
    )
    role_metadata.deserialize(data)
    print(role_metadata.allow_duplicates)
    print(role_metadata.dependencies)



# Generated at 2022-06-13 08:54:57.759732
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    from unittest import TestCase
    from ansiblelint import Runner
    from ansiblelint.rules import RulesCollection
    from ansiblelint.rules.RoleDeprecatedVariablesRule import RoleDeprecatedVariablesRule

    class Test(TestCase):
        collection = RulesCollection()
        collection.register(RoleDeprecatedVariablesRule())

        def setUp(self):
            self.loader = Runner(self.collection, 'test')._loader

        def test_serialize(self):
            meta = RoleMetadata.load(data={'allow_duplicates': True, 'dependencies': [{'role': 'test.meta_main'}]},
                        owner=self, variable_manager=None, loader=self.loader)

# Generated at 2022-06-13 08:54:58.486365
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    pass

# Generated at 2022-06-13 08:55:00.292363
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    m = RoleMetadata()
    assert m.serialize() == dict(allow_duplicates=False, dependencies=[])

# Generated at 2022-06-13 08:55:11.694796
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    r = RoleMetadata()
    s = r.serialize()
    assert s == {'allow_duplicates': False, 'dependencies': []}
    r.dependencies = []
    s = r.serialize()
    assert s == {'allow_duplicates': False, 'dependencies': []}
    r.allow_duplicates = True
    s = r.serialize()
    assert s == {'allow_duplicates': True, 'dependencies': []}
    r.dependencies = 'xxx'
    s = r.serialize()
    assert s == {'allow_duplicates': True, 'dependencies': 'xxx'}
    r.dependencies = [1,2,3]
    s = r.serialize()

# Generated at 2022-06-13 08:55:12.896842
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    this_role = RoleMetadata()
    assert this_role is not None

# Generated at 2022-06-13 08:55:20.297211
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    m = RoleMetadata()
    m._allow_duplicates = True
    m._dependencies = [{'name': 'test', 'scm': 'git', 'website': 'test.com', 'scm_path': 'git@github.com:test/test,1.0.0,test'}]
    m._galaxy_info = {'name': 'test', 'scm': 'git', 'website': 'test.com', 'scm_path': 'git@github.com:test/test,1.0.0,test'}
    m._argument_specs = {'test': 'test'}

    data = m.serialize()

    assert 'allow_duplicates' in data
    assert 'dependencies' in data



# Generated at 2022-06-13 08:55:26.131745
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    roleMetadata_obj = RoleMetadata(owner=None)
    data_dict = dict(allow_duplicates=True, dependencies=[])
    roleMetadata_obj.deserialize(data_dict)

    assert roleMetadata_obj._allow_duplicates == True
    assert roleMetadata_obj._dependencies == []

# Generated at 2022-06-13 08:55:59.055669
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    import sys
    import os
    import json
    import unittest
    from ansible.module_utils import basic

    # Create test object
    module_args = dict(
        name='test-role',
        src='git://example.org/foo.git',
        version='v1.2.3',
    )
    tmp = basic.AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )
    owner = tmp.params['name']
    data = tmp.params
    m = RoleMetadata(owner)
    m.load_data(data, loader=None, variable_manager=None)

    # Check if RoleMetadata object is created as expected
    assert isinstance(m.galaxy_info, dict)

# Generated at 2022-06-13 08:56:05.513710
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    data = dict(
        allow_duplicates=True,
        dependencies=['role1', 'role2', 'role3'],
    )
    role_metadata = RoleMetadata()
    role_metadata.deserialize(data)
    result = role_metadata.serialize()
    assert result == data



# Generated at 2022-06-13 08:56:16.675490
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    r = RoleMetadata()
    assert r.serialize() == {
        'allow_duplicates': False,
        'dependencies': []
    }

    r.allow_duplicates = True
    r.dependencies = [
        {'src': 'some_role', 'version': '1.0'},
        {'src': 'some_role', 'version': '1.0'},
        {'src': 'some_role', 'version': '1.0'},
    ]


# Generated at 2022-06-13 08:56:24.350573
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():

    # Test with invalid meta/main.yml
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.play import Play
    rd = RoleDefinition(); rd._role_path = "path/"
    play = Play(); play._loader = None
    try:
        RoleMetadata().load(None, owner=rd)
    except AnsibleParserError as e:
        assert "the 'meta/main.yml' for role" in to_native(e)
    else:
        assert False, "AnsibleParserError not raised"

    # Test with valid meta/main.yml
    try:
        RoleMetadata().load(dict(), owner=rd)
    except AnsibleParserError as e:
        assert False, "AnsibleParserError raised: %s" % to_native(e)

# Generated at 2022-06-13 08:56:26.932544
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    role_metadata = RoleMetadata()
    assert role_metadata._allow_duplicates == False
    assert role_metadata._dependencies == []

# Generated at 2022-06-13 08:56:34.265353
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    # TODO: Currently, the only way to access a RoleMetadata class is to create a Role,
    #       then access it's metadata. This will be improved in future...
    from ansible.playbook.role.role import Role
    role = Role.load('/tmp/not-existing-role')
    metadata = RoleMetadata.load(
        data=dict(
            allow_duplicates=False,
            dependencies=['role1', 'role2']
        ),
        owner=role
    )

    assert metadata._allow_duplicates == False
    assert len(metadata._dependencies) == 2

# Generated at 2022-06-13 08:56:40.934511
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.role.meta import RoleMetadata
    from ansible.plugins.loader import role_loader
    from ansible.plugins.loader import module_loader
    
    # set up args
    path = 'ansible/plugins/roles/test_role'
    role = RoleDefinition('test_role', None, path, None)
    data = {'allow_duplicates': True, 'dependencies': []}
    variable_manager = None
    loader = role_loader

    # test and assert
    role_meta = RoleMetadata.load(data, role, variable_manager, loader)
    assert role_meta.allow_duplicates == data.get('allow_duplicates', False)

# Generated at 2022-06-13 08:56:49.178041
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():

    data = """
    allow_duplicates: false
    dependencies:
    """

    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.playbook import PlayBook
    from ansible.playbook.play import Play

    loader = AnsibleLoader(data, '', play=Play())
    d = loader.get_single_data()

    p = Playbook()

    metadata = RoleMetadata(owner=p)

    metadata._load_allow_duplicates(None, d['allow_duplicates'])

    assert metadata.allow_duplicates is False

    metadata._load_dependencies(None, d['dependencies'])

# Generated at 2022-06-13 08:57:03.891884
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    # test a standard metadata
    data = dict(
        allow_duplicates=True,
        dependencies=['role1', 'role2'],
    )
    metadata = RoleMetadata()
    metadata.deserialize(data)
    serialized = metadata.serialize()

    assert serialized['dependencies'] == ['role1', 'role2']
    assert serialized['allow_duplicates'] is True

    # test a empty metadata
    data = dict()
    metadata = RoleMetadata()
    metadata.deserialize(data)
    serialized = metadata.serialize()

    assert serialized['dependencies'] == []
    assert serialized['allow_duplicates'] is False



# Generated at 2022-06-13 08:57:11.432008
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    r = RoleMetadata()
    data = {}
    r.deserialize(data)
    assert r.allow_duplicates == False
    assert r.dependencies == []
    data = {'allow_duplicates': 'false', 'dependencies': []}
    r.deserialize(data)
    assert r.allow_duplicates == False
    assert r.dependencies == []
    data = {'allow_duplicates': 'true', 'dependencies': ['role1', 'role2']}
    r.deserialize(data)
    assert r.allow_duplicates == True
    assert r.dependencies == ['role1', 'role2']

# Generated at 2022-06-13 08:57:59.791006
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():

    # Test the default empty constructor
    r = RoleMetadata()
    assert r._allow_duplicates is False
    assert r._dependencies == []

    # Test the actual constructor with arguments
    r = RoleMetadata(owner='owner')
    assert r._allow_duplicates is False
    assert r._dependencies == []
    assert r._owner == 'owner'

# Generated at 2022-06-13 08:58:02.929280
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    data = dict(
        allow_duplicates=True,
        dependencies=[]
    )
    m = RoleMetadata()
    m.deserialize(data)
    assert m.allow_duplicates == True
    assert m.dependencies == []

# Generated at 2022-06-13 08:58:06.071330
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    dependencies = list()

    data = { 
        'allow_duplicates': False, 
        'dependencies': dependencies 
    }

    role_metadata_class = RoleMetadata()
    assert role_metadata_class.serialize() == data


# Generated at 2022-06-13 08:58:14.773512
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    from ansible.playbook.role.requirement import RoleRequirement
    from ansible.playbook.role_resource import RoleResource

    # Test minimal metadata
    metadata = RoleMetadata().deserialize({})
    assert metadata._allow_duplicates is False
    assert metadata._dependencies == []

    # Test full metadata
    role_deps = [
        RoleRequirement(dict(role="foo", scm='git', src='git@github.com:foo/bar.git', version='v1.0.0')),
        RoleResource('myrole', scm='git', src='git@github.com:foo/bar.git', version='v1.0.0')
    ]
    metadata.deserialize(dict(
        allow_duplicates=True,
        dependencies=role_deps
    ))

# Generated at 2022-06-13 08:58:19.527577
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    inv_dir = '/tmp/test_RoleMetadata_load/inv'
    playbooks_dir = '/tmp/test_RoleMetadata_load/playbooks'
    os.makedirs(inv_dir)
    os.makedirs(playbooks_dir)
    os.makedirs(playbooks_dir + '/roles/test_role/')

    context = PlayContext()
    inventory = InventoryManager

# Generated at 2022-06-13 08:58:28.809186
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():

    class TestRole():
        name = "test-role"
        _role_path = "/path/to/roles/test-role"
        _role_collection = "test.collection"
        collections = ["test.collection"]

    test_data = {
        'allow_duplicates': True,
        'dependencies': [
            'geerlingguy.apache',
            {
                'name': 'geerlingguy.php',
                'apply': False,
                'src': 'file:///path/to/roles/geerlingguy/php',
                'version': 'v1.7.0',
            },
        ],
    }

    meta = RoleMetadata.load(test_data, TestRole())
    assert meta.allow_duplicates is True
    assert len(meta.dependencies) == 2


# Generated at 2022-06-13 08:58:44.510395
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    """
    This test case will test the method load of the RoleMetadata class.
    In which it will try to see if the method can load the data.
    """

    from ansible.playbook.task import Task
    from ansible.playbook.role import Role

    # Create a task for the role, so that we can pass it to RoleMetadata.load
    task = Task()

    # Create an object of the Role class
    role = Role()

    # Set the role_path of the role,
    # so that it can be used later in the RoleMetadata.load
    role.role_path = "../../../ansible/test/units/modules/test_meta_main/"

    # Create a dictionary of data to be loaded

# Generated at 2022-06-13 08:58:45.877058
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    pass


# Generated at 2022-06-13 08:58:46.945273
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    # TODO: Add test for method load of class RoleMetadata
    pass

# Generated at 2022-06-13 08:58:50.074424
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    # We must create a RoleMetadata object with a valid owner object
    role_metadata = RoleMetadata(owner=None)
    assert role_metadata.allow_duplicates == False
    assert role_metadata.dependencies == []

# Generated at 2022-06-13 09:00:19.442897
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    a = RoleMetadata()
    print(a.__dict__)

# Generated at 2022-06-13 09:00:27.694960
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    meta = RoleMetadata()
    assert meta.allow_duplicates == False
    assert meta.dependencies == []

    # Construct from an empty dict
    meta = RoleMetadata()
    meta.load({})
    assert meta.allow_duplicates == False
    assert meta.dependencies == []

    # Construct from a dict with an empty dependencies key
    meta = RoleMetadata()
    meta.load({'dependencies': []})
    assert meta.allow_duplicates == False
    assert meta.dependencies == []

    # Construct from a dict with a dependencies key containing a list
    meta = RoleMetadata()
    meta.load({'dependencies': [{'name': 'geerlingguy.firewall'}]})
    assert meta.allow_duplicates == False
    assert len(meta.dependencies) == 1



# Generated at 2022-06-13 09:00:37.325141
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    '''
    make sure that the load function instantiates the correct object type
    '''
    from ansible.playbook.role import Role
    sample_role_metadata = {
        "galaxy_info": "test",
        "dependencies": [ {"role": "common"} ]
    }

    role = Role(name="my_role", collection=None, data=sample_role_metadata)
    role_meta = RoleMetadata.load(sample_role_metadata, role)

    # this test is basically dead code as the load method always returns a
    # RoleMetadata object. If a non-RoleMetadata object is returned this test
    # will fail.
    assert isinstance(role_meta, RoleMetadata)
    assert role_meta._dependencies[0].role == "common"



# Generated at 2022-06-13 09:00:43.270406
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    print ("test_RoleMetadata")
    test_host_1 = {'hostname': 'aa', 'ip': '127.0.0.1', 'port': 22}
    host_1 = ansible.inventory.host.Host(test_host_1)
    from ansible.playbook import Play
    play_1 = Play()
    m = RoleMetadata(owner=play_1)
    print (m.serialize())

if __name__ == '__main__':
    test_RoleMetadata()

# Generated at 2022-06-13 09:00:48.720862
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    # Create an object
    m = RoleMetadata()

    # Serialize the object and compare to expected
    expected = {
        'allow_duplicates': False,
        'dependencies': [],
    }

    assert m.serialize() == expected

    # Serialize the object with changes and compare to expected
    expected = {
        'allow_duplicates': True,
        'dependencies': ['role1', 'role2'],
    }

    m.allow_duplicates = True
    m.dependencies = ['role1', 'role2']
    assert m.serialize() == expected

# Generated at 2022-06-13 09:00:56.604617
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    from ansible.playbook.role.definition import RoleDefinition
    role = RoleDefinition.load(dict(name="foo"))
    role_metadata = RoleMetadata(owner=role)

    data = dict(
        allow_duplicates=False,
        dependencies=[dict(name="bar")]
    )

    role_metadata.load_data(data, variable_manager=None, loader=None)
    serialized = role_metadata.serialize()
    assert serialized["allow_duplicates"] == False
    assert (serialized["dependencies"][0] == {'name': 'bar'})

# Generated at 2022-06-13 09:01:03.794127
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():

    # Empty RoleMetadata, tests dict conversion
    data = dict()

    # Use a simple dict as variable manager
    variable_manager = {
        'user': 'root'
    }

    role_metadata = RoleMetadata.load(data, variable_manager)
    assert role_metadata._allow_duplicates == False

    # Missing dependencies dict, tests dict conversion
    data = dict()
    role_metadata = RoleMetadata.load(data, variable_manager)
    assert role_metadata._allow_duplicates == False
    assert len(role_metadata._dependencies) == 0

    # Simple dependencies dict
    data = dict()
    data['dependencies'] = dict()
    role_metadata = RoleMetadata.load(data, variable_manager)

    assert role_metadata._allow_duplicates == False

# Generated at 2022-06-13 09:01:08.301306
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    md = RoleMetadata()
    assert md.allow_duplicates is False
    assert md.dependencies == list()
    assert md.galaxy_info is None
    assert md.argument_specs == dict()

# Generated at 2022-06-13 09:01:12.527322
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    role_metadata = RoleMetadata()
    assert role_metadata is not None
    assert role_metadata.allow_duplicates is False
    assert role_metadata.dependencies == []

# Generated at 2022-06-13 09:01:27.610827
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():

    class FakeRole(object):
        def __init__(self, name):
            self.name = name

        def get_name(self):
            return self.name

    import collections

    # Mocked metadata - role_name
    role_metadata_dict = collections.namedtuple('role_metadata_dict', ['role_name'])

    # Mocked role name - name
    role_name_dict = collections.namedtuple('role_name_dict', ['name'])

    # Mocked role definition - src
    role_definition = collections.namedtuple('role_definition', ['src'])

    # Mocked dependency list - dependency
    dependency_list = collections.namedtuple('dependency_list', ['dependency'])

    # Mocked name - name