

# Generated at 2022-06-13 08:52:14.724068
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    class RoleMetadata_test(RoleMetadata):
        pass

    result = RoleMetadata_test().serialize()
    assert result['allow_duplicates'] == False
    assert result['dependencies'] == []



# Generated at 2022-06-13 08:52:25.841688
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    data = {
        'allow_duplicates': True,
        'dependencies': [
            { "role": "geerlingguy.redis" },
            { "role": "geerlingguy.memcached" }
        ]
    }
    check_data = {
        'allow_duplicates': True,
        'dependencies': [
            { "role": "Ansible.geerlingguy.redis", "role_path": "/path/to/geerlingguy.redis" },
            { "role": "Ansible.geerlingguy.memcached", "role_path": "/path/to/geerlingguy.memcached" }
        ]
    }
    class Owner:
        def __init__(self):
            self.get_name = lambda: "OwnerName"


# Generated at 2022-06-13 08:52:29.998964
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    test_data = {'allow_duplicates': True, 'dependencies': ['ansible.legacy.mysql', 'ansible.builtin.yum']}
    actual_result = RoleMetadata().deserialize(test_data)
    assert actual_result == test_data

# Generated at 2022-06-13 08:52:30.874982
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    role_metadata = RoleMetadata()
    role_metadata.serialize()


# Generated at 2022-06-13 08:52:39.135218
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    data = dict(
        allow_duplicates = False,
        dependencies = [
            {
                'src': 'test.test_role',
                'version': '1.0.0',
                'name': 'test_role'
            },
            {
                'role': 'test_role',
                'foo': 'bar'
            },
            {
                'role': 'test_role'
            }
        ]
    )
    meta = RoleMetadata()
    meta.deserialize(data)
    assert meta.allow_duplicates == False
    assert len(meta.dependencies) == 3
    assert meta.dependencies[0].src == 'test.test_role'
    assert meta.dependencies[0].version == '1.0.0'

# Generated at 2022-06-13 08:52:40.528268
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    m = RoleMetadata()
    assert m is not None

# Generated at 2022-06-13 08:52:45.168018
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    data = {
        'allow_duplicates': True,
        'dependencies': [
            "geerlingguy.apache",
            "geerlingguy.mysql"
        ]
    }
    role_metadata = RoleMetadata().load(data)
    assert role_metadata.serialize() == data



# Generated at 2022-06-13 08:52:46.641538
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    role_meta=RoleMetadata()

# Generated at 2022-06-13 08:52:51.186316
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    '''
    Test for deserialize
    '''
    role_metadata = RoleMetadata()
    role_metadata.deserialize({'allow_duplicates': True, 'dependencies': ['roles/common', 'roles/webserver']})
    assert role_metadata.serialize() == {'allow_duplicates': True, 'dependencies': ['roles/common', 'roles/webserver']}


# Generated at 2022-06-13 08:52:54.644109
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    """
    Unit test for constructor of class RoleMetadata
    """
    role_metadata_test = RoleMetadata()
    role_metadata_test

if __name__ == '__main__':
    test_RoleMetadata()

# Generated at 2022-06-13 08:53:14.974322
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    # Create a new RoleMetadata
    rm = RoleMetadata()

    # Test 1: given a data for deserialize the attribute _allow_duplicates must be true
    rm.deserialize({'allow_duplicates': True})
    allow_duplicates = rm.allow_duplicates
    assert allow_duplicates == True

    # Test 2: given a data for deserialize the attribute _dependencies must be a non empty array
    rm.deserialize({'dependencies': ['ap']})
    dependencies = rm.dependencies
    assert dependencies == ['ap']

    # Test 3: given a data for deserialize the attributes _allow_duplicates and _dependencies must be true and a non empty array
    rm.deserialize({'allow_duplicates': True, 'dependencies': ['ap']})
    allow

# Generated at 2022-06-13 08:53:16.064829
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    pass


# Generated at 2022-06-13 08:53:17.381316
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    role_metadata = RoleMetadata
    role_metadata(owner=None)

# Generated at 2022-06-13 08:53:30.575100
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    data = {'dependencies': [
        {'name': 'foo', 'src': 'https://github.com/foo/foo'},
        {'role': 'bar', 'src': 'https://github.com/bar/bar'}
    ]}
    r = RoleMetadata(owner=None)
    r.deserialize(data)
    assert r.dependencies[0].get_name() == 'foo'
    assert r.dependencies[0].get_src() == 'https://github.com/foo/foo'
    assert r.dependencies[0].get_scm() == 'git'
    assert r.dependencies[0].get_scm_url() == 'https://github.com/foo/foo'
    assert r.dependencies[0].get_scm_branch() == 'master'
   

# Generated at 2022-06-13 08:53:33.468395
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    # Test normal case
    role_object = RoleMetadata().load({})
    assert role_object._allow_duplicates == False
    assert role_object._dependencies == []
    assert role_object._galaxy_info is None

# Generated at 2022-06-13 08:53:38.279130
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():

    from ansible.playbook.play import Play
    from ansible.playbook.task_include import TaskInclude

    rmd = RoleMetadata()
    rmd.deserialize(dict(allow_duplicates=False, dependencies=[]))
    assert rmd._allow_duplicates == False
    assert rmd._dependencies == []

    rmd = RoleMetadata()
    rmd.deserialize(dict(allow_duplicates=True, dependencies=['joe', 'bob']))
    assert rmd._allow_duplicates == True
    assert rmd._dependencies == ['joe', 'bob']

    data = {'allow_duplicates': False, 'dependencies': []}
    rmd = RoleMetadata()
    rmd.deserialize(data)
    assert rmd._allow_

# Generated at 2022-06-13 08:53:43.688677
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.playbook.role.definition import RoleDefinition
    m = RoleMetadata(owner=RoleDefinition(role_name='test'))
    metadata = {'dependencies': ['foo:bar', 'baz', 'qux:quux']}
    m.load(metadata, 'test:bar', 'test', 'foo')

# Generated at 2022-06-13 08:53:47.652574
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():

    class test_metadata(object):
        def __init__(self):
            self.allow_duplicates = 'testing'
            self.dependencies = 'testing'

    data = test_metadata()
    x = RoleMetadata()
    y = x.deserialize(data)
    assert y['allow_duplicates'] == 'testing'
    assert y['dependencies'] == 'testing'


# Generated at 2022-06-13 08:53:58.345258
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.playbook.attribute import FieldAttribute
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.utils.path import unfrackpath
    from ansible.parsing.yaml.loader import AnsibleLoader
    from unit.mock.loader import DictDataLoader


# Generated at 2022-06-13 08:53:58.897867
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    pass

# Generated at 2022-06-13 08:54:16.927909
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    from ansible.playbook.role.definition import RoleDefinition
    args = {'name': 'myrole', 'path': 'myrole'}
    role_owner = RoleDefinition.load(args)
    args = {'allow_duplicates': True, 'dependencies': 'myrole'}
    role_meta = RoleMetadata.load(args, role_owner)
    # FIXME
    #assert role_meta.dependencies.get_name() == role_owner.get_name()
    assert role_meta.allow_duplicates == True

# Generated at 2022-06-13 08:54:20.676876
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.task import Task

    role_a = RoleDefinition('role_a',
                            [Task()],
                            )

    print(RoleMetadata(role_a))

# Generated at 2022-06-13 08:54:27.879516
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    a = RoleMetadata.load({
        'allow_duplicates': True,
        'dependencies': [
            {'name': 'test-role', 'collections': ['common']},
            {'name': 'test-role', 'version': '1.0.0'},
        ],
    }, None)

    assert a.serialize() == {
        'allow_duplicates': True,
        'dependencies': [
            {'name': 'test-role', 'collections': ['common']},
            {'name': 'test-role', 'version': '1.0.0'},
        ],
    }

# Generated at 2022-06-13 08:54:28.429207
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    pass  # TODO

# Generated at 2022-06-13 08:54:33.726554
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    role = RoleMetadata()
    role.allow_duplicates = True
    role.dependencies = ["common", "web", "database"]

    result_expected = dict(
        allow_duplicates=True,
        dependencies=["common", "web", "database"]
    )
    assert role.serialize() == result_expected
# Unit test: END


# Generated at 2022-06-13 08:54:35.153206
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    t = RoleMetadata()
    if t is not None:
        pass

# Generated at 2022-06-13 08:54:39.476152
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    yaml_str='''
    allow_duplicates: 1
    dependencies: x
    '''

    ds = yaml.safe_load(yaml_str)

    metadata = RoleMetadata.load(ds, owner=None)

    result = metadata.serialize()

    expected_result = dict(
        allow_duplicates=True,
        dependencies=['x']
    )
    assert result == expected_result, \
        "The result of the serialize method of class RoleMetadata is not correctly returned"


# Generated at 2022-06-13 08:54:45.739084
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    from ansible.module_utils.six import iteritems
    d = {
        'allow_duplicates': False,
        'dependencies': [
            {
                'role': 'common',
                'version': '1.0'
            }
        ]
    }
    m = RoleMetadata()
    m.deserialize(d)
    assert m.serialize() == d



# Generated at 2022-06-13 08:54:49.306019
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    testinstance = RoleMetadata()
    assert testinstance._allow_duplicates == False
    assert testinstance._dependencies == []
    assert testinstance._galaxy_info == {}
    assert testinstance._argument_specs == {}

# Generated at 2022-06-13 08:54:53.726946
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    r = RoleMetadata()
    result = r.serialize()
    assert isinstance(result, dict)
    assert result['allow_duplicates'] == False
    assert result['dependencies'] == []

# Generated at 2022-06-13 08:55:25.630659
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():

    # Test the case that RoleMetadata object returned successfully and value of _allow_duplicates is True
    owner = MockOwner()
    data = {
        "allow_duplicates": True
    }
    role_metadata = RoleMetadata.load(data, owner, None, None)
    assert isinstance(role_metadata, RoleMetadata)
    assert role_metadata._allow_duplicates is True

    # Test the case that RoleMetadata object returned successfully and value of _allow_duplicates is False
    owner = MockOwner()
    data = {
        "allow_duplicates": False
    }
    role_metadata = RoleMetadata.load(data, owner, None, None)
    assert isinstance(role_metadata, RoleMetadata)
    assert role_metadata._allow_duplicates is False

    # Test the case

# Generated at 2022-06-13 08:55:35.116236
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    from ansible.playbook.role.definition import RoleDefinition
    test_data = {
        'foo': 'bar',
        'boo': 'far',
        'allow_duplicates': False,
        'dependencies': {'role1': {'version': '3.0.0'}, 'role2': None},
    }
    rd = RoleDefinition(name='test', path='not/used')
    meta = RoleMetadata(owner=rd).load_data(test_data)
    assert meta._allow_duplicates == False
    assert len(meta._dependencies) == 2
    assert meta.data == test_data

# Test loading of role dependencies

# Generated at 2022-06-13 08:55:40.902430
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    import ansible.playbook.role

    t = Task()
    p = Play()
    # create an empty role
    role = ansible.playbook.role.Role()
    p._included_roles.append(role)
    # test the constructor of RoleMetadata
    assert not RoleMetadata(owner=None)
    # This is not a function that return a RoleMetadata object
    assert not RoleMetadata(owner=role)

# Generated at 2022-06-13 08:55:51.780570
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():

    from ansible.module_utils._text import to_bytes
    from ansible.playbook.role.definition import RoleDefinition

    yaml_to_load = """
    ---
    allow_duplicates: True
    dependencies:
    - role: galaxy.role
      other_vars: "here"
    galaxy_info:
      description: fake desc
      company: fake_company
      author: brandon_philips
      license: MIT
      min_ansible_version: fake_min_ansible_ver
    arguments:
      - name: repo_name
        default: galaxy_repo
        description: fake_description
    """

# Generated at 2022-06-13 08:55:56.062692
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    role_metadata = RoleMetadata()
    role_metadata.allow_duplicates = False
    role_metadata.dependencies = []
    assert {'allow_duplicates': False, 'dependencies': []} == role_metadata.serialize()



# Generated at 2022-06-13 08:56:11.476488
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    class MockRole(object):
        def __init__(self):
            self._role_collection = 'ansible_test.test_collection'
            self._role_path = '/some/path'
            self.collections = ['ansible_test.test_collection', 'ansible.legacy']

    parent_role = MockRole()
    assert len(parent_role.collections) == 2

    metadata = {
        'allow_duplicates': True,
        'dependencies': [
            'test_collection.test_role',
        ]
    }

    rm = RoleMetadata(owner=parent_role)
    rm.load(metadata)
    assert rm.allow_duplicates is True
    assert len(rm.dependencies) == 1
    assert rm.dependencies[0].role_name == 'test_role'

# Generated at 2022-06-13 08:56:12.806304
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    return "TODO"

# Generated at 2022-06-13 08:56:17.694813
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    import json
    from operator import eq

    r = RoleMetadata()
    r.deserialize(json.loads('{"allow_duplicates": false, "dependencies": []}'))

    # Tests
    assert isinstance(r.allow_duplicates, type(False))
    assert isinstance(r.dependencies, type([]))

    assert eq(r.allow_duplicates, False)
    assert eq(r.dependencies, [])


# Generated at 2022-06-13 08:56:24.937487
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.playbook.role import Role
    from ansible.playbook.role.include import RoleInclude
    from ansible.playbook.role.requirement import RoleRequirement
    data = {'allow_duplicates': True,
            'dependencies': [{'role': 'common'}]
            }
    role = Role()
    role._role_path = '/etc/ansible/roles/foo'
    role_metadata = RoleMetadata.load(data, owner=role)
    assert role_metadata
    assert role_metadata.allow_duplicates == data['allow_duplicates']
    assert len(role_metadata.dependencies) == 1
    dependency = role_metadata.dependencies[0]
    assert dependency
    assert dependency.role == data['dependencies'][0]['role']

# Generated at 2022-06-13 08:56:34.782467
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    from ansible.parsing.yaml.manager import InventoryLoader
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.playbook.play_context import PlayContext

    my_loader = InventoryLoader(DataLoader())
    variable_manager = VariableManager(loader=my_loader, inventory=my_loader.inventory, variable_manager=None, loader_basedir=None)
    variable_manager.set_inventory_sources("test/test_role_include/hosts")
    variable_manager._extra_vars = {"foo": "bar"}

    play_context = PlayContext(variable_manager=variable_manager)
    variable_manager.set_play_context(play_context)


# Generated at 2022-06-13 08:57:19.084483
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.role.requirement import RoleRequirement
    data = {
        'dependencies': [
            {
                'role': 'foo',
                'name': 'foo',
                'collections': []
             },
            'bar'
        ]
     }
    owner = RoleDefinition.load(path='./tests/units/playbooks/roles/test_role')
    meta = RoleMetadata.load(data=data, owner=owner)
    assert(isinstance(meta, RoleMetadata))
    assert(len(meta.dependencies)==2)
    assert(isinstance(meta.dependencies[0], RoleRequirement))
    assert(isinstance(meta.dependencies[1], RoleRequirement))

# Generated at 2022-06-13 08:57:30.532647
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    test_roles_path = 'test/ansible/lib/galaxy/test_data/test-roles/'
    test_roles_path = os.path.join(os.getcwd(), test_roles_path)
    assert os.path.exists(test_roles_path) and os.path.isdir(test_roles_path), 'test_roles_path does not exist'

    deserialized = RoleMetadata(owner=None).deserialize({'dependencies': [{'role': 'test1'}], 'allow_duplicates': False})
    assert isinstance(deserialized, RoleMetadata)
    assert isinstance(deserialized._dependencies, list)

    deserialized._owner = None

# Generated at 2022-06-13 08:57:34.959212
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    role_meta_data = RoleMetadata()
    role_meta_data.deserialize({"dependencies": ["common"]})
    assert role_meta_data._dependencies == ["common"]

# Generated at 2022-06-13 08:57:39.494196
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    role_metadata = RoleMetadata()
    assert role_metadata._dependencies == []
    assert role_metadata._allow_duplicates == False
    assert role_metadata._galaxy_info == None



# Generated at 2022-06-13 08:57:48.665593
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    role_metadata = RoleMetadata()
    data = {
        'allow_duplicates': True,
        'dependencies': [
            {'role': 'geerlingguy.docker', 'version': 'v1.1.0'},
            'username.role2',
            'username.role3'
        ]
    }
    role_metadata.deserialize(data)

    assert role_metadata.allow_duplicates is True
    assert isinstance(role_metadata.dependencies, list)
    assert isinstance(role_metadata.dependencies[0], RoleRequirement) and \
           role_metadata.dependencies[0].get_name() == 'geerlingguy.docker' and \
           role_metadata.dependencies[0].get_version() == 'v1.1.0'

# Generated at 2022-06-13 08:57:51.664915
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    test_data = dict(
        allow_duplicates=True,
        dependencies=['foo', 'bar']
    )
    data = RoleMetadata().deserialize(test_data)
    assert data['allow_duplicates'] is True

# Generated at 2022-06-13 08:58:02.226607
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.role.collection_loader import RoleCollectionLoader
    from ansible.playbook.play_context import PlayContext
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    class TestRoleDefinition(RoleDefinition):
        _metadata = FieldAttribute(isa='RoleMetadata')
        _role_collection = FieldAttribute(isa='str')
        _role_path = FieldAttribute(isa='str')
        _collections = FieldAttribute(isa='list', default=list)
        _play = FieldAttribute(isa='Play')
        _role_name = FieldAttribute(isa='str')


# Generated at 2022-06-13 08:58:04.234325
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    r = RoleMetadata()
    assert r is not None
    assert isinstance(r, RoleMetadata)


# Generated at 2022-06-13 08:58:09.953586
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():

    # Create test data
    data = {
        "allow_duplicates": False,
        "dependencies": []
    }
    # Create instance of class RoleMetadata
    metadata = RoleMetadata()
    assert getattr(metadata, '_allow_duplicates') == False
    assert getattr(metadata, '_dependencies') == []
    metadata.deserialize(data)
    # Verfiy if deserialized value are different from the data
    assert getattr(metadata, '_allow_duplicates') == data["allow_duplicates"]
    assert getattr(metadata, '_dependencies') == data["dependencies"]

# Generated at 2022-06-13 08:58:11.690290
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    role_metadata=RoleMetadata()
    role_metadata.allow_duplicates = False
    serialized_data = role_metadata.serialize()
    assert serialized_data == {'allow_duplicates': False, 'dependencies': []}


# Generated at 2022-06-13 08:59:26.184107
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.inventory.host import Host
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.task_queue_manager import TaskQueueManager

    class TestRole():
        def __init__(self):
            self._role_path = '/you/are/right'
            self._role_name = 'test_role'
            self._role_collection = None
            self._collections = ['/tmp/role_data/roles']
            self._play = Play()

    test_role = TestRole()


# Generated at 2022-06-13 08:59:31.936844
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    '''
    Unit test for constructor of class RoleMetadata
    '''
    role_metadata = RoleMetadata()
    role_metadata._owner = 'test'
    assert(role_metadata.serialize() == dict(allow_duplicates=False,dependencies=[]))
    #print("role_metadata._allow_duplicates =%s" % role_metadata._allow_duplicates)
    #print("role_metadata._dependencies =%s" % role_metadata._dependencies)
    #print("role_metadata.serialize() =%s" % role_metadata.serialize())


# Generated at 2022-06-13 08:59:34.133315
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    m = RoleMetadata()
    ser_dict = m.serialize()
    assert ser_dict['allow_duplicates'] == False
    assert ser_dict['dependencies'] == []


# Generated at 2022-06-13 08:59:34.624424
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    pass

# Generated at 2022-06-13 08:59:45.074018
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    meta = RoleMetadata(owner={'_role_path': '.'})

    required_keys = ('role', 'name')
    for required_key in required_keys:
        data = {required_key: '.'}
        role = meta.load(data=data, owner={'_role_path': '.'})
        assert role.dependencies[0][required_key] == '.'
        assert role._dependencies[0]['role'] == '.'

    # Test deserialize
    data = {'allow_duplicates': True, 'dependencies': ['.']}
    role = RoleMetadata(owner={'_role_path': '.'})
    role.deserialize(data=data)
    assert role.allow_duplicates is True
    assert role.dependencies == ['.']

# Generated at 2022-06-13 08:59:48.513130
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    r = RoleMetadata(owner=None)
    assert r.deserialize(
        {'allow_duplicates': False,
         'dependencies': []}
    ) == {'allow_duplicates': False,
          'dependencies': []}

# Generated at 2022-06-13 08:59:51.385970
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    m = RoleMetadata()
    assert m._allow_duplicates is False
    assert m._dependencies == []
    assert m._argument_specs == {}



# Generated at 2022-06-13 08:59:56.564250
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    '''
    constructor for class RoleMetadata
    '''
    test_metadata = {'allow_duplicates': False, 'dependencies': []}
    obj = RoleMetadata(1)
    obj.load_data(test_metadata)
    assert obj._owner == 1
    assert obj._allow_duplicates == False
    assert obj._dependencies == []

# Generated at 2022-06-13 09:00:00.526247
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    """
    Test method deserialize of class RoleMetadata
    """
    role_metdata = RoleMetadata()
    role_metdata.deserialize({})
    assert role_metdata.allow_duplicates == False
    assert role_metdata.dependencies == []


# Generated at 2022-06-13 09:00:08.533774
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    """Tests the load method of RoleMetadata."""
    class Role(object):
        def __init__(self, role_name, role_path, role_collection=None):
            self._role_name = role_name
            self._role_path = role_path
            self._role_collection = role_collection
            self.collections = []

        @property
        def _play(self):
            return None

        def get_name(self):
            return self._role_name

    def _load_list_of_roles(roles, play=None, current_role_path=None, variable_manager=None, loader=None, collection_search_list=None):
        return "MOCK__LOAD_LIST_OF_ROLES"

    # When: main.yml is not a dict
    # Then: Ans

# Generated at 2022-06-13 09:01:39.808351
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    role_meta = RoleMetadata({"dependencies": [{"role": "common", "tags": ['common']}]})
    assert role_meta.dependencies[0]['role'] == "common"

# Generated at 2022-06-13 09:01:48.845166
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    # test valid RoleMetadata initialization
    test_GalaxyInfo = dict(author='foo_author', description='foo_description',
                           company='foo_company', license='foo_license',
                           min_ansible_version='foo_min_ansible_version',
                           platforms='foo_platforms', galaxy_tags='foo_galaxy_tags',
                           galaxy_install_date='foo_galaxy_install_date',
                           galaxy_install_by='foo_galaxy_install_by',
                           galaxy_install_ip='foo_galaxy_install_ip',
                           supported_by='foo_supported_by')

# Generated at 2022-06-13 09:01:53.500554
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    role_metadata = RoleMetadata()
    setattr(role_metadata, '_allow_duplicates', None)
    setattr(role_metadata, '_dependencies', None)
    assert role_metadata.serialize() == {'allow_duplicates': False, 'dependencies': []}


# Generated at 2022-06-13 09:01:54.408841
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    pass


# Generated at 2022-06-13 09:02:01.964065
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.playbook.role.definition import RoleDefinition

    d = dict(
        allow_duplicates = False,
        dependencies = [
            dict(
                role = "foo",
                tasks_from = "*"
            ),
            dict(
                role = "bar"
            )
        ]
    )

    r = RoleMetadata()
    r.load(d)

    assert r._allow_duplicates is False
    assert len(r._dependencies) == 2
    assert isinstance(r._dependencies[0], RoleDefinition)
    assert isinstance(r._dependencies[1], RoleDefinition)

    assert r._dependencies[0]._role_name == 'foo'
    assert r._dependencies[0]._task_tags == '*'
    assert r._dependencies[1]._role_

# Generated at 2022-06-13 09:02:11.382489
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.parsing.yaml.objects import AnsibleUnicode

    from units.mock.loader import DictDataLoader
