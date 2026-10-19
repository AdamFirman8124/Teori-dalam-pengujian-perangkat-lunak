

# Generated at 2022-06-13 08:52:13.451402
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    data = {
        "allow_duplicates": False,
        "dependencies": [],
        "galaxy_info": {},
        "argument_specs": {}
    }
    owner = "owner"

    m = RoleMetadata(owner).load_data(data)
    assert m.serialize() == data
    m = RoleMetadata(owner).deserialize(data)

# Generated at 2022-06-13 08:52:16.723847
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    class RunOnce:
        run_once = True

    assert isinstance(RoleMetadata.load(dict(allow_duplicates=True), RunOnce), RoleMetadata)
    assert isinstance(RoleMetadata.load(dict(allow_duplicates=False), RunOnce), RoleMetadata)
    assert isinstance(RoleMetadata.load(dict(), RunOnce), RoleMetadata)


# Generated at 2022-06-13 08:52:22.321624
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    role_metadata = RoleMetadata()
    data = {
        'allow_duplicates': True,
        'dependencies': ['foo']
    }
    role_metadata.deserialize(data)

    assert role_metadata.allow_duplicates is True
    assert role_metadata.dependencies == ['foo']

# Generated at 2022-06-13 08:52:26.109318
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    # Verify that no name is specified
    role_metadata_1 = RoleMetadata.load(data=None, owner=None)
    assert role_metadata_1 == None

# Generated at 2022-06-13 08:52:32.662269
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    class Test(object):
        def get_name(self):
            return 'test'

    rm = RoleMetadata(owner=Test())
    setattr(rm, 'allow_duplicates', True)
    setattr(rm, 'dependencies', ['test'])

    assert rm.serialize() == dict(
        allow_duplicates=True,
        dependencies=['test']
    )

# Generated at 2022-06-13 08:52:37.026258
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    '''
    To check if serialize func return a dict
    '''
    collection = RoleMetadata()
    output = collection.serialize()
    assert isinstance(output, dict)
    assert 'allow_duplicates' in output
    assert 'dependencies' in output

# Generated at 2022-06-13 08:52:47.481564
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.task import Task
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject

    # initialize an instance of TaskInclude
    task_include = TaskInclude()

    # initialize an instance of Task
    task = Task()

    # initialize an instance of AnsibleBaseYAMLObject
    ansible_base_yaml_object = AnsibleBaseYAMLObject()

    # initialize an instance of RoleMetadata
    role_metadata = RoleMetadata()
    role_metadata.dependencies = [task, task_include, ansible_base_yaml_object]

    serialized_data = role_metadata.serialize()
    # validate the data with keys that are expected

# Generated at 2022-06-13 08:52:50.766765
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    r = RoleMetadata()
    data = {
        'allow_duplicates': True,
        'dependencies': ['test1', 'test2']
    }
    r.deserialize(data)
    assert r._allow_duplicates == True
    assert r._dependencies == ['test1', 'test2']

# Generated at 2022-06-13 08:52:58.132884
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    class FakeRole():
        def __init__(self):
            pass

        def get_name(self):
            return 'role-name'

    role_metadata = RoleMetadata(owner=FakeRole())
    role_metadata._allow_duplicates = True
    role_metadata._dependencies = ['dep_1', 'dep_2']
    result = role_metadata.serialize()
    print(result['allow_duplicates'])
    print(result['dependencies'][0])
    print(result['dependencies'][1])



# Generated at 2022-06-13 08:53:07.330159
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    metadata_yaml_str = """
    allow_duplicates: yes
    dependencies:
    - src: https://github.com/geerlingguy/ansible-role-apache
      name: geerlingguy.apache
      scm: git
      version: 1.0.0
    - src: https://github.com/geerlingguy/ansible-role-mysql
      name: geerlingguy.mysql
      scm: git
      version: 1.0.0
    """
    import yaml
    metadata_data = yaml.load(metadata_yaml_str)

    # verify construction
    metadata = RoleMetadata.load(metadata_data, None)
    assert metadata.allow_duplicates == True
    assert metadata.dependencies.__len__() == 2

# Generated at 2022-06-13 08:53:13.816329
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    assert RoleMetadata.__name__ == 'RoleMetadata'
    assert RoleMetadata.__doc__ is not None


# Generated at 2022-06-13 08:53:22.735899
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    def test_data(name, meta_data, dependencies):
        meta = RoleMetadata()
        meta.deserialize(meta_data)

        assert(meta._owner.name == name)
        assert(meta._allow_duplicates == meta_data['allow_duplicates'])
        assert(len(meta._dependencies) == dependencies)

    from .test_factory import TestRoleInclude

# Generated at 2022-06-13 08:53:28.850864
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    role_metadata = RoleMetadata(12)

    assert type(role_metadata) == RoleMetadata
    assert role_metadata._owner == 12
    assert role_metadata._allow_duplicates == False
    assert role_metadata._dependencies == []
    assert role_metadata._galaxy_info == None
    assert role_metadata._argument_specs == {}

# Generated at 2022-06-13 08:53:29.601047
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    assert RoleMetadata() is not None

# Generated at 2022-06-13 08:53:36.257072
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
  module_name = os.path.basename(__file__)
  header_string = module_name + ": test_RoleMetadata: "
  print('\n' + header_string + 'Starting' + '-' * 60)

  role_metadata = RoleMetadata()
  assert role_metadata.allow_duplicates == False, "role_metadata.allow_duplicates == False"
  assert role_metadata.dependencies == [], "role_metadata.dependencies == []"
  print('\n' + header_string + 'Ending' + '-' * 60)

if __name__ == "__main__":
  test_RoleMetadata()

# Generated at 2022-06-13 08:53:39.956996
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    r = RoleMetadata()
    d = {'allow_duplicates': False, 'dependencies': []}
    r.deserialize(d)
    assert r.allow_duplicates == False
    assert r.dependencies == []


# Generated at 2022-06-13 08:53:47.949680
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    role_metadata = RoleMetadata()
    allow_duplicates = True
    dependencies = [
        {'role': 'test_role_1', 'src': 'test_src_1' },
        {'role': 'test_role_2', 'src': 'test_src_2' },
    ]
    data = dict(allow_duplicates=allow_duplicates, dependencies=dependencies)

    role_metadata.deserialize(data)

    assert role_metadata._allow_duplicates == allow_duplicates
    assert role_metadata._dependencies == dependencies

# Generated at 2022-06-13 08:53:56.996681
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    metadata = RoleMetadata()
    data = metadata.serialize()
    assert data['allow_duplicates'] == False
    assert data['dependencies'] == []
    metadata = RoleMetadata()
    metadata._allow_duplicates = True
    data = metadata.serialize()
    assert data['allow_duplicates'] == True
    assert data['dependencies'] == []
    metadata = RoleMetadata()
    metadata._dependencies = [{'foo': 'bar'}]
    data = metadata.serialize()
    assert data['allow_duplicates'] == False
    assert data['dependencies'] == [{'foo': 'bar'}]

# Generated at 2022-06-13 08:54:00.652584
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    metadata = RoleMetadata()
    data = {'dependencies': ['common'], 'allow_duplicates': False}
    metadata.deserialize(data)
    assert metadata.dependencies == ['common']
    assert metadata.allow_duplicates == False


# Generated at 2022-06-13 08:54:08.804980
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    from ansible.playbook.role.definition import RoleDefinition
    m = RoleMetadata()
    r = RoleDefinition.load({'role': 'foo'}, [], {})

    # Test the default value
    assert m.allow_duplicates is False
    assert m.dependencies == []

    # Test the set value
    data = dict(allow_duplicates=True, dependencies=[r])
    m.deserialize(data)
    assert m.allow_duplicates is True
    assert m.dependencies == [r]

    # Test the set value with an unsuppoted key
    data = dict(allow_duplicates=True, dependencies=[r], blah=True)
    m.deserialize(data)
    assert m.allow_duplicates is True
    assert m.dependencies == [r]

#

# Generated at 2022-06-13 08:54:23.503944
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    """RoleMetadata - serialize"""

    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.role.include import RoleInclude

    role = RoleDefinition.load({'role': 'appserver'})
    role._role_path = "~/roles/appserver"
    role_include = RoleInclude.load("common")
    role_include.set_parent(role)
    metadata = RoleMetadata.load({}, owner=role_include)
    metadata.deserialize({'allow_duplicates': True, 'dependencies': ['galaxy.role,version,name']})
    data = metadata.serialize()
    assert 'allow_duplicates' in data
    assert 'dependencies' in data
    assert data['allow_duplicates'] is True

# Generated at 2022-06-13 08:54:28.497428
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    '''
    This is a test method for class RoleMetadata's method load
    '''
    from ansible.playbook.role.meta import RoleMetadata
    import json
    import os
    import tempfile

    dependencies = [
        {
            "src": "https://github.com/ansible/role-git.git",
            "name": "git"
        }
    ]

    data = {
        "dependencies": dependencies,
        "allow_duplicates": False
    }

    temp_dir = tempfile.gettempdir()
    file_path = os.path.join(temp_dir, 'role-meta-class-test')

    with open(file_path, 'w') as f:
        f.write(json.dumps(data))


# Generated at 2022-06-13 08:54:34.985114
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    role_metadata = RoleMetadata()
    role_metadata._load_data({
        'allow_duplicates': True,
        'dependencies': [
            'dep1',
            'dep2',
        ],
    })
    serialized = role_metadata.serialize()
    assert serialized == {
        'allow_duplicates': True,
        'dependencies': [
            'dep1',
            'dep2',
        ],
    }


# Generated at 2022-06-13 08:54:41.069556
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.role.requirement import RoleRequirement

    rdata = dict(name="test_role", galaxy_info=dict(), dependencies=[dict(role=dict(name="foo"))])
    role = RoleDefinition()
    role.load_data(rdata)
    role.deserialize()

    # Test deserializing using deserialize method
    ds = {
        'allow_duplicates': True,
        'dependencies': [dict(role=dict(name="foo"))]
    }
    obj = RoleMetadata.deserialize(ds)
    assert len(obj.dependencies) == len(ds['dependencies'])
    assert obj.allow_duplicates == True
    assert obj.dependencies[0].name == "foo"

# Generated at 2022-06-13 08:54:45.313059
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    try:
        RoleMetadata()
    except Exception as e:
        raise AssertionError("failed to create object RoleMetadata")
    return True

if __name__ == '__main__':
    test_RoleMetadata()

# Generated at 2022-06-13 08:54:54.616074
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    import pprint
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.role.requirement import RoleRequirement
    import ansible.constants as C

    default_playbook_basedir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
    C.DEFAULT_ROLES_PATH = os.path.join(default_playbook_basedir, 'test', 'roles')
    C.DEFAULT_ROLES_PATH = os.path.abspath(C.DEFAULT_ROLES_PATH)

    from ansible.playbook.play import Play

# Generated at 2022-06-13 08:54:55.572179
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    assert True

# Generated at 2022-06-13 08:54:56.759770
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    # returns nothing
    pass

# Generated at 2022-06-13 08:55:07.942671
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    ''' test that RoleMetadata doesn't raise on deserialize '''

    class MockLoader:
        def __init__(self):
            pass

    class MockVariableManager:
        def __init__(self):
            pass

    class MockRole:
        def __init__(self, name):
            self.name = name

        def get_name(self):
            return self.name

        def get_path(self):
            return self.name


# Generated at 2022-06-13 08:55:10.759505
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    role_meta = RoleMetadata()
    assert role_meta._allow_duplicates == False
    assert role_meta._dependencies == []

# Generated at 2022-06-13 08:55:20.594270
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    metadata = RoleMetadata()
    assert metadata.allow_duplicates == False
    assert metadata.dependencies == []


# Generated at 2022-06-13 08:55:21.830115
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    pass

# Generated at 2022-06-13 08:55:29.380323
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    # This test is just for coverage of load() in order to cover
    # the code paths to be able to access the local variables
    from ansible.playbook.role import Role
    from ansible.utils.vars import combine_vars

    role_name = "clowns"
    role = Role(role_name)

    # Load the role's meta/main.yml
    sample_path = os.path.join(os.path.dirname(__file__), '..', 'files', 'playbooks', 'meta', 'main.yml')
    meta_data = RoleMetadata.load(
        ds=dict(),
        owner=role,
        variable_manager=combine_vars({}),
        loader=None
    )
    meta_data.allow_duplicates = True

    # Test the deserial

# Generated at 2022-06-13 08:55:39.178105
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    import copy
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.includes.role import RoleInclude

    # Basic test
    attrs = dict()
    attrs['allow_duplicates'] = False
    attrs['dependencies'] = list()

    rm1 = RoleMetadata()
    for attr, val in attrs.items():
        setattr(rm1, attr, val)

    data1 = rm1.serialize()
    assert data1 == dict(allow_duplicates=False, dependencies=[])

    # More thorough test
    r1 = RoleDefinition()
    r1.name = 'testrole1'

    ri1 = RoleInclude()
    ri1._role = r1

    rm2 = RoleMetadata()
    rm2.allow_dupl

# Generated at 2022-06-13 08:55:39.737559
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    pass

# Generated at 2022-06-13 08:55:43.718511
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    data = "test"
    owner = "test"
    variable_manager = "test"
    loader = "test"
    # RoleMetadata::load(data,owner,variable_manager,loader)
    assert False # TODO: implement your test here


# Generated at 2022-06-13 08:55:50.778993
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    role_metadata = RoleMetadata()
    role_metadata.load({'foo': 'bar'})
    assert role_metadata.deserialize({'foo': 'bar'}) == dict(foo='bar')
    assert role_metadata.serialize() == dict(allow_duplicates=False, dependencies=[])

    role_metadata_2 = RoleMetadata()
    role_metadata_2._load_galaxy_info('foo', None)
    assert role_metadata_2._galaxy_info == {}

# Generated at 2022-06-13 08:55:52.194336
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    role_metadata = RoleMetadata()

# Generated at 2022-06-13 08:55:53.096427
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    assert False, "Test not implemented"


# Generated at 2022-06-13 08:55:57.063512
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    role_metadata = RoleMetadata()
    role_metadata.allow_duplicates = False
    role_metadata.dependencies = ["test"]
    serialize_data = role_metadata.serialize()
    assert "allow_duplicates" in serialize_data


# Generated at 2022-06-13 08:56:19.512962
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    class Mock(object):
        def get_name(self):
            return "foo"

    role = RoleMetadata(owner=Mock())
    assert role.__class__.__name__ == "RoleMetadata"

# Generated at 2022-06-13 08:56:25.241606
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.utils.collection_loader import AnsibleCollectionRef
    role_name = 'test_role'
    role_def = RoleDefinition(role_name)
    role_def._role_collection = AnsibleCollectionRef.from_string('test_namespace.test_col')
    role_metadata = RoleMetadata(role_def)
    role_serialized = role_metadata.serialize()

    new_metadata = RoleMetadata(role_def)
    new_metadata.deserialize(role_serialized)
    new_serialized = new_metadata.serialize()

    assert new_serialized == role_serialized

# Generated at 2022-06-13 08:56:29.434124
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    data = dict(
        allow_duplicates=False,
        dependencies=[]
    )

    m = RoleMetadata()
    m.deserialize(data)

    assert m.allow_duplicates == False
    assert m.dependencies == []


# Generated at 2022-06-13 08:56:31.784311
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    '''
        unit test for constructor of class RoleMetadata
    '''
    m = RoleMetadata()
    assert m.__class__.__name__ == 'RoleMetadata'

# Generated at 2022-06-13 08:56:32.713686
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    assert RoleMetadata is RoleMetadata

# Generated at 2022-06-13 08:56:39.928497
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():

    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.block import Block
    from ansible.playbook.play import Play

    class RoleMock:
        def __init__(self, name):
            self.name = name
            self._role_path = '/roles'
            self._play = Play()

    data = dict(
      name='test1',
      allow_duplicates=False,
      dependencies=['localhost', 'test1', 'test2']
    )

    data2 = dict(
      name='test2',
      allow_duplicates=False,
      dependencies=['localhost', 'test2']
    )

    fake_play = Play()

# Generated at 2022-06-13 08:56:49.594995
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    def check_loaded_values(loaded_data, expected_data):
        assert loaded_data._ds == expected_data
        assert loaded_data.allow_duplicates == expected_data.get('allow_duplicates', False)
        assert loaded_data.dependencies == expected_data.get('dependencies', [])

    data = {}
    RoleMetadata.load(data, 'test_role')
    check_loaded_values(RoleMetadata.load(data, 'test_role'), data)

    data = {'allow_duplicates': True, 'dependencies': []}
    RoleMetadata.load(data, 'test_role')
    check_loaded_values(RoleMetadata.load(data, 'test_role'), data)


# Generated at 2022-06-13 08:57:06.239550
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    # import needed for testing
    import copy
    import os
    import sys
    import unittest
    from ansible.plugins.loader import find_plugin_file
    try:
        from yaml import CSafeLoader as SafeLoader, CSafeDumper as SafeDumper
    except ImportError:
        from yaml import SafeLoader, SafeDumper

    #################################################################
    # Definitions: state what we expect the class to do
    #################################################################
    def load_metadata_file(file_name, owner=None):
        if not owner:
            owner = MockRole()
            owner.name = "mock"
            owner.role_path = find_plugin_file(file_name, [os.path.join(os.path.dirname(__file__), '..')])

        role_meta = RoleMetadata.load_from_

# Generated at 2022-06-13 08:57:16.021066
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    from ansible.playbook.role.include import RoleInclude
    from ansible.playbook.collection.collection_loader import AnsibleCollectionLoader

    loader = AnsibleCollectionLoader()
    search_paths = loader.get_collection_paths('./')
    data = loader.get_collection_artifact('tasks/main.yml', search_paths=search_paths)
    variable_manager = loader.variable_manager
    variable_manager._options = dict(
        role_paths=['./'],
        collection_paths='./'
    )
    ansible_version = dict(
        major=2,
        minor=0,
        patch=0,
        dirty='',
        stable=True,
        string='2.0.0'
    )


# Generated at 2022-06-13 08:57:21.599522
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    roleMetadata = RoleMetadata()
    serialize_result = roleMetadata.serialize()
    assert serialize_result["allow_duplicates"] == False
    assert serialize_result["dependencies"] == []


# Generated at 2022-06-13 08:57:56.614477
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    '''
    Tests load of RoleMetadata
    :return:
    '''
    from ansible.playbook.role.include import RoleInclude

    owner = mock()
    data = {
        'allow_duplicates': True,
        'dependencies': [{'some': 'role'}],
    }

    my_role_meta = RoleMetadata.load(data, owner)

    for attr, val in data.items():
        assert my_role_meta.__getattribute__(attr) == val
    assert isinstance(my_role_meta.dependencies[0], RoleInclude)
    assert owner == my_role_meta._owner

# Generated at 2022-06-13 08:58:02.106685
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    role_meta = RoleMetadata(owner='active_directory')

    # Dirty trick to bypass the __init__
    role_meta._allow_duplicates = True
    role_meta._dependencies = ['active_directory']

    result = role_meta.serialize()

    assert result['allow_duplicates'] == True
    assert result['dependencies'] == ['active_directory']



# Generated at 2022-06-13 08:58:09.688862
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    '''Test Ansible RoleMetadata serialize method'''
    # Create a data structure with nested GalaxyInfo object
    role = {
        'allow_duplicates': True,
        'dependencies': [
            {
                'role': 'role1'
            },
            {
                'role': 'role2',
                'ansible_facts_file': 'facts'
            },
            {
                'role': 'role3',
                'collections': [
                    'collections1',
                    'collections2'
                ]
            }
        ]
    }
    result = RoleMetadata.load(role, owner=None).serialize()

# Generated at 2022-06-13 08:58:13.970572
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    meta = RoleMetadata()

    # Test deserialize case where JSON data is a empty dictionary
    #assert meta.deserialize({}) == dict(allow_duplicates=False, dependencies=[])

    # Test deserialize case where JSON data has 'allow_duplicates' attribute
    #meta.deserialize({'allow_duplicates': True})
    #assert meta.allow_duplicates == True

    # Test deserialize case where JSON data has 'dependencies' attribute
    #meta.deserialize({'dependencies': [{'role': 'webserver'}]})
    #assert meta.dependencies == [{'role': 'webserver'}]

# Generated at 2022-06-13 08:58:18.820670
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    import ansible.playbook
    class TmpPlay(object):
        pass

    class TmpRole(object):

        def __init__(self):
            self.name = 'test'
            self.play = TmpPlay()
            self.play.collections = ['ansible.builtin']

    role = TmpRole()
    data = dict(
        allow_duplicates=True,
        dependencies=[dict(role='test_role')]
    )
    role_meta = RoleMetadata.load(data, role)
    assert role_meta.allow_duplicates == True
    assert role_meta.dependencies[0].get_name() == 'test_role'
    assert role_meta.dependencies[0].get_collections() == ['ansible.builtin']

# Generated at 2022-06-13 08:58:20.728105
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    # TODO: implement test_RoleMetadata_load
    pass



# Generated at 2022-06-13 08:58:28.322596
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    data = {'allow_duplicates': True, 'dependencies': [{'role': 'test_role1'}, {'role': 'test_role2'}, {'role': 'test_role3'}]}
    result = RoleMetadata(owner=None).load_data(data, None, None).serialize()
    assert result == data

# Generated at 2022-06-13 08:58:35.685768
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    o = RoleMetadata()

    o.allow_duplicates = True
    o.dependencies = ['role1', 'role2']

    # serialize to dict
    data = o.serialize()
    assert data['allow_duplicates'] == True
    assert data['dependencies'] == ['role1', 'role2']

# Generated at 2022-06-13 08:58:38.273374
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    roleMetadata = RoleMetadata()
    roleMetadata.deserialize({'allow_duplicates':False, 'dependencies': []})
    assert roleMetadata.allow_duplicates is False
    assert roleMetadata.dependencies == []

# Generated at 2022-06-13 08:58:41.211040
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    role_metadata = RoleMetadata()
    #role_metadata._dependencies = ['a']
    dependencies = ['a']
    data = {'dependencies': dependencies}
    role_metadata.deserialize(data)
    assert role_metadata.dependencies == dependencies

# Generated at 2022-06-13 08:59:10.497405
# Unit test for method deserialize of class RoleMetadata

# Generated at 2022-06-13 08:59:16.561189
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.role_include import RoleInclude
    from ansible.playbook.role.definition import RoleDefinition

    # Test the constructor
    #
    # 1. No owner
    # 2. Owner is not a RoleDefinition
    # 3. Ownwer is a RoleDefinition

    # Test __init__
    #  1. No owner
    try:
        role = RoleMetadata()
    except Exception as e:
        assert(isinstance(e, AnsibleParserError) and (str(e) == "RoleMetadata() missing 1 required positional argument: 'owner'"))
    else:
        assert(False)

    # Test __init__
    #  2. Owner is not a RoleDefinition

# Generated at 2022-06-13 08:59:34.065793
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    # Expected results
    expected_allow_duplicates = False
    expected_dependencies = []
    # create a test RoleMetadata object
    test_RoleMetadata = RoleMetadata()
    # verify empty values of RoleMetadata on start
    assert test_RoleMetadata._allow_duplicates == expected_allow_duplicates
    assert test_RoleMetadata._dependencies == expected_dependencies
    # test missing dependency entries
    data = dict(
        allow_duplicates=True,
    )
    test_RoleMetadata.deserialize(data)
    assert test_RoleMetadata._allow_duplicates == True
    assert test_RoleMetadata._dependencies == expected_dependencies
    # test missing allow_duplicates entry
    data = dict(
        dependencies=[],
    )
    test_RoleMet

# Generated at 2022-06-13 08:59:35.081968
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    #TODO: Write unit tests
    pass


# Generated at 2022-06-13 08:59:37.653553
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    data = dict(
        allow_duplicates=False,
        dependencies=list()
    )

    test_obj = RoleMetadata()
    test_obj.deserialize(data)
    assert test_obj.allow_duplicates == False
    assert test_obj.dependencies == list()

# Generated at 2022-06-13 08:59:48.599583
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.plugins.loader import load_plugin

    role_definition = RoleDefinition('/etc/ansible/roles/my_role', scm='git', version='1.0.0', name='my_role')
    role_definition_loader = load_plugin('role/role_definition_loader')
    role_definition._loader = role_definition_loader
    main_role = RoleMetadata(owner=role_definition)
    main_role._dependencies = [{'role': 'remcolle'}]
    main_role._allow_duplicates = True
    assert main_role.serialize() == {'allow_duplicates': True, 'dependencies': [{'role': 'remcolle'}]}

# Generated at 2022-06-13 08:59:59.240526
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.playbook.task_include import TaskInclude
    
    from ansible.playbook.role import Role
    from ansible.playbook.role_include import RoleInclude
    from ansible.playbook.task import Task
    from ansible.vars.hostvars import HostVars
    from ansible.vars.manager import VariableManager
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    
    # load role with unknown dependencies, role is not exist
    role_metadata = RoleMetadata()
    play = Play()
    play.default_vars = {'foo': 'bar'}
    variable_manager = VariableManager()
    variable_manager.set_play_context(play=play)

# Generated at 2022-06-13 09:00:07.553670
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.playbook import Play
    from ansible.playbook.role import Role
    from ansible.vars import VariableManager

    yaml_data = """
    galaxy_info:
      author: john
    dependencies:
    - src: git+https://github.com/user/ansible-role-foo.git
      scm: git
      version: v1.0
    """

    variable_manager = VariableManager()
    loader = None
    play = Play()
    role = Role()
    role._role_path = './test_role/meta'
    role._play = play

    role_metadata = RoleMetadata.load(yaml_data, role, variable_manager, loader)
    assert role_metadata._allow_duplicates == False

# Generated at 2022-06-13 09:00:13.548598
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    assert RoleMetadata().deserialize({}) == {'allow_duplicates': False, 'dependencies': []}
    assert RoleMetadata().deserialize(dict(dependencies=[1, 2], allow_duplicates=True)) == {'allow_duplicates': True, 'dependencies': [1, 2]}
    assert RoleMetadata().deserialize(dict(dependencies=[1, 2])) == {'allow_duplicates': False, 'dependencies': [1, 2]}
    assert RoleMetadata().deserialize(dict(allow_duplicates=True)) == {'allow_duplicates': True, 'dependencies': []}

# Generated at 2022-06-13 09:00:19.645624
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():

    from ansible.playbook.role import Role

    r = Role()
    r._role_path = 'test_path'

    m = RoleMetadata(owner=r)

    d = dict(
        allow_duplicates=False,
        dependencies=list()
    )

    m.deserialize(d)

    assert not m.allow_duplicates
    assert m.dependencies == d['dependencies']

# Generated at 2022-06-13 09:01:13.391113
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    test_metadata = dict(
        allow_duplicates=False,
        dependencies=["foo"]
    )
    obj = RoleMetadata()
    obj.deserialize(test_metadata)
    assert getattr(obj, 'allow_duplicates') == False
    assert getattr(obj, 'dependencies') == ["foo"]

# Generated at 2022-06-13 09:01:18.354301
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    field_test=RoleMetadata()
    assert field_test.serialize() == dict(
            allow_duplicates=field_test._allow_duplicates,
            dependencies=field_test._dependencies)

# Generated at 2022-06-13 09:01:30.022568
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    # Initialize
    variable_manager = None
    loader = None
    role_name = 'some_name'
    role_path = 'some_path'

    # File not exist
    try:
        data = RoleMetadata.load({'some_key': 'some_value'}, None, variable_manager=variable_manager, loader=loader)
        assert False
    except AnsibleParserError:
        assert True
    # Correct file path and data
    file_path = 'tests/test_collections/ansible_collections/ansible/some_collection/roles/some_role/meta/main.yml'
    data = RoleMetadata(owner=role_name, role_path=role_path, variable_manager=variable_manager, loader=loader)
    assert data._allow_duplicates is None
    assert data._

# Generated at 2022-06-13 09:01:44.152021
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.playbook.play import Play
    from ansible.playbook.role import Role
    from ansible.vars.manager import VariableManager

    class DataLoader:
        pass

    class Playbook:
        def __init__(self):
            self._loader = DataLoader()

    pb = Playbook()
    play = Play.load({
        'name': 'test play'
    }, loader=pb._loader)
    role = Role.load({
        'name': 'test role'
    }, play=play, loader=pb._loader)

    meta_data = RoleMetadata(owner=role)
    meta_data.load_data({
        'dependencies': {
            '- role: test role 1'
        }
    }, variable_manager=VariableManager(), loader=pb._loader)

    assert meta_data

# Generated at 2022-06-13 09:01:44.642359
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    pass

# Generated at 2022-06-13 09:01:46.323537
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    """
    This function is used to test the deserialize() method of class RoleMetadata
    """
    assert True, 'No test implemented yet.'

# Generated at 2022-06-13 09:01:53.225867
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    m = RoleMetadata()
    assert m.serialize() == dict()

    m._allow_duplicates = True
    m._dependencies = ['foo', 'bar', 'a', 'b']
    assert m.serialize() == dict(
        allow_duplicates=True,
        dependencies=['foo', 'bar', 'a', 'b']
    )

# Generated at 2022-06-13 09:01:55.013556
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    roleMetadata_obj = RoleMetadata()
    roleMetadata_obj.allow_duplicates = False
    roleMetadata_obj.dependencies = []
    response = roleMetadata_obj.serialize()
    assert response['allow_duplicates'] == False
    assert response['dependencies'] == []

# Generated at 2022-06-13 09:02:02.391519
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    '''
    This is a test method to check load method of class RoleMetadata
    '''
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.role.requirement import RoleRequirement
    from ansible.playbook import Play
    from ansible.utils.collection_loader import AnsibleCollectionConfig
    from ansible.vars.manager import VariableManager
