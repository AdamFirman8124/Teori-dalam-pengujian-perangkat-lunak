

# Generated at 2022-06-13 08:52:20.146115
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    role_metadata = RoleMetadata()
    role_metadata._allow_duplicates = True
    role_metadata._dependencies = ['dependency1', 'dependency2']
    serialized = role_metadata.serialize()

    assert(serialized['allow_duplicates'] == role_metadata.allow_duplicates)
    assert(serialized['dependencies'] == role_metadata.dependencies)



# Generated at 2022-06-13 08:52:28.106786
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():

    from ansible.playbook.play_context import PlayContext
    from ansible.parsing.vault import get_vault_secret
    from ansible.vars import VariableManager

    inventory = '''
    [r1]
    localhost
    '''

    variable_manager = VariableManager()
    variable_manager.extra_vars = {'a': '1', 'b': '2'}
    variable_manager.get_vault_secrets = lambda _: dict(vault_secret='secret')

    # constructor
    class Helper(object):
        def __init__(self, name):
            self._name = name

        def get_name(self):
            return self._name


# Generated at 2022-06-13 08:52:32.608136
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    role_meta = RoleMetadata().deserialize(
        dict(allow_duplicates=False, dependencies=list())
    )
    assert role_meta.allow_duplicates == False
    assert role_meta.dependencies == list()

# Generated at 2022-06-13 08:52:37.369541
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    metadata = RoleMetadata()
    data = {
        'allow_duplicates': False,
        'dependencies': []
    }
    serialize_data = metadata.serialize()
    assert serialize_data == data, "Unit test for method serialize of class RoleMetadata failed"


# Generated at 2022-06-13 08:52:39.198252
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    # Create a RoleMetadata object
    role_metadata = RoleMetadata()

# Generated at 2022-06-13 08:52:46.401761
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    class FakeRole:
        def __init__(self, name='test'):
            self.name = name
            self.ansible_version = None

    meta = RoleMetadata(owner=FakeRole())
    meta._dependencies = [{'name': 'test', 'src': 'test', 'path': 'test'}]
    meta.allow_duplicates = True

    assert meta.serialize() == {'dependencies': [{'name': 'test', 'src': 'test', 'path': 'test'}], 'allow_duplicates': True}

# Generated at 2022-06-13 08:52:51.607751
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.playbook import Play
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.parsing.loader import DataLoader
    from collections import namedtuple
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.inventory.host import Host

    class FakeTestPlaybook:
        def __init__(self):
            inventory = InventoryManager(loader=DataLoader(), sources='')
            self.hosts = 'localhost'
            self.inventory = inventory
            self.variable_manager = VariableManager()
            self.variable_manager.set_inventory(self.inventory)

    data_to_test = {}

# Generated at 2022-06-13 08:52:58.629629
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():

    # RoleMetadata.deserialize should set allow_duplicates and dependencies properly.
    class Role(object):
        def __init__(self):
            self.metadata = RoleMetadata()

    role = Role()

    data = dict(
        allow_duplicates=True,
        dependencies=['common']
    )

    role.metadata.deserialize(data)

    assert role.metadata.allow_duplicates == True
    assert role.metadata.dependencies == ['common']


# Generated at 2022-06-13 08:53:04.019044
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    data = { '_dependencies': [{'role': 'test'}, 'test2'], '_allow_duplicates': False, 'allow_duplicates': True, 'dependencies': ['test3'] }

    role_metadata = RoleMetadata()
    role_metadata.deserialize(data)

    assert role_metadata._allow_duplicates is True
    assert role_metadata._dependencies == ['test3']

# Generated at 2022-06-13 08:53:08.637932
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    role_metadata = RoleMetadata()
    role_metadata._allow_duplicates = 'True'
    role_metadata._dependencies = ['role1', 'role2']
    assert role_metadata.serialize() == {'allow_duplicates': 'True', 'dependencies': ['role1', 'role2']}, \
           "RoleMetadata.serialize() test failed"

# Generated at 2022-06-13 08:53:16.096058
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    pass  # TODO


# Generated at 2022-06-13 08:53:16.750952
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    pass

# Generated at 2022-06-13 08:53:17.527541
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    pass

# Generated at 2022-06-13 08:53:24.835399
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    role_meta = RoleMetadata(owner="owner")
    role_meta.allow_duplicates = True
    role_meta.dependencies = [{'name': 'foo'}, {'name': 'bar'}]
    assert(role_meta.serialize() ==
           {'allow_duplicates': True, 'dependencies': [{'name': 'foo'}, {'name': 'bar'}]})

# Generated at 2022-06-13 08:53:29.232581
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    dependencies=['foo', {'role': 'bar'}]
    data=dict(
        allow_duplicates=True,
        dependencies=dependencies
    )
    metadata=RoleMetadata()
    metadata.deserialize(data)
    assert metadata.allow_duplicates == True
    assert metadata.dependencies == dependencies


# Generated at 2022-06-13 08:53:35.159233
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    j = RoleMetadata()
    j.deserialize({'allow_duplicates': False, 'dependencies': []})
    assert j._allow_duplicates == False
    assert j._dependencies == []
    j.deserialize({'dependencies': []})
    assert j._allow_duplicates == False
    assert j._dependencies == []
    j.deserialize({'allow_duplicates': True, 'dependencies': []})
    assert j._allow_duplicates == True
    assert j._dependencies == []


# Generated at 2022-06-13 08:53:39.754744
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    m = RoleMetadata()
    m.allow_duplicates = True
    m.dependencies = ["dep1", "dep2"]
    m.serialize()
    assert m._dependencies == ["dep1","dep2"]
    assert m._allow_duplicates == True



# Generated at 2022-06-13 08:53:43.408439
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    data = {}
    owner = {}
    variable_manager = {}
    loader = {}
    assert RoleMetadata.load(data, owner, variable_manager, loader) is not None

# Generated at 2022-06-13 08:53:46.418356
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    rm = RoleMetadata()
    setattr(rm, 'allow_duplicates', True)
    setattr(rm, 'dependencies', [1,2,3])
    assert(rm.serialize() == {'allow_duplicates': True, 'dependencies': [1,2,3]})


# Generated at 2022-06-13 08:53:47.717395
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():

    assert(RoleMetadata(owner=None))
    assert(not RoleMetadata(owner=" "))

# Generated at 2022-06-13 08:54:01.508556
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    data = {'allow_duplicates': False, 'dependencies': []}
    role_metada_serialize_data = RoleMetadata.serialize(data)
    assert role_metada_serialize_data == data

# Generated at 2022-06-13 08:54:05.135855
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    info = RoleMetadata()
    data = {'allow_duplicates': True, 'dependencies': ['r1', 'r2']}
    info.deserialize(data)
    assert info._allow_duplicates == True
    assert info._dependencies == ['r1', 'r2']

# Generated at 2022-06-13 08:54:11.018620
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    data = {
        'allow_duplicates': True,
        'dependencies': [{'role': 'tests.collections.ansible_collections.acme.sample'},
                         {'role': 'tests.collections.ansible_collections.acme.another'}]
    }
    obj = RoleMetadata(owner=None).deserialize(data)
    ds = obj.serialize()
    assert data == ds, "Serialize result fails to restore original data structure"

# Generated at 2022-06-13 08:54:22.671846
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    data = {
        "dependencies": [
            { "src": "geerlingguy.docker" },
            { "src": "geerlingguy.java" }
        ]
    }
    role = RoleMetadata()
    assert role._load_dependencies(None, data['dependencies'])[0].get_info() == {
        "scm": "https",
        "scm_url": "github.com/geerlingguy/ansible-role-java",
        "src": "geerlingguy.java",
        "version": "v1.7.0"
    }

# Generated at 2022-06-13 08:54:29.614069
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():

    a = RoleMetadata()
    a.allow_duplicates = True
    a.dependencies = "test"
    a.vars = "test"

    b = a.serialize()

    assert b['allow_duplicates'] == True
    assert b['dependencies'] == "test"
    assert 'vars' not in b

    # Test with an empty dictionary
    a = RoleMetadata()
    a.vars = "test"
    b = a.serialize()
    
    assert 'allow_duplicates' not in b
    assert 'dependencies' not in b
    assert 'vars' not in b

test_RoleMetadata_serialize()


# Generated at 2022-06-13 08:54:40.618574
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    filename = str(os.path.join(os.getcwd(), 'test/repos/roles/test_role/meta/main.yml'))
    information = {}
    with open(filename, 'r') as content_file:
        content = content_file.read()
        content_list = content.split('\n')
        for line in content_list:
            if ':' in line:
                split_line = line.split(':')
                if split_line[0][0] != '#' and '#' in line:
                    try:
                        information[split_line[0]] = line[line.index('#')+1:]
                    except:
                        information[split_line[0]] = split_line[1]

# Generated at 2022-06-13 08:54:51.235960
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    from ansible.playbook.role.required_by import RoleRequirement
    from ansible.playbook.role.metadata import RoleMetadata
    from ansible.playbook.role import Role
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext

    # test for missing dependencies
    data = {"allow_duplicates": True}
    meta = RoleMetadata()
    meta.deserialize(data)
    assert meta._allow_duplicates == True
    assert meta._dependencies == []

    # test for different version of dependencies
    data = {"dependencies": [{"role": "my.role", "version": "0.1"}, {"role": "my.role", "version": "0.2"}]}
    meta = RoleMetadata()

# Generated at 2022-06-13 08:54:55.874302
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    data = dict(
        allow_duplicates=True,
        dependencies=['role1', 'role2']
    )
    # RoleMetadata.deserialize(data)
    data['foo'] = 'bar'
    assert data.get('foo') == 'bar'


# Generated at 2022-06-13 08:55:06.716987
# Unit test for method load of class RoleMetadata

# Generated at 2022-06-13 08:55:07.728921
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    assert True

# Generated at 2022-06-13 08:55:19.817056
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    data = dict()

    data['allow_duplicates'] = False
    data['dependencies'] = []

    test_metadata = RoleMetadata().deserialize(data)

    test_output = test_metadata.serialize()

    assert test_output == data


# Generated at 2022-06-13 08:55:25.642957
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    expected = dict(
        allow_duplicates=False,
        dependencies=[{'src': '../roles/geerlingguy.apache'}]
    )
    obj = RoleMetadata()
    obj.deserialize(expected)
    assert expected == obj.serialize()


# Generated at 2022-06-13 08:55:30.537896
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    r = RoleMetadata()
    data = dict()
    data['allow_duplicates'] = False
    data['dependencies'] = []
    r.deserialize(data)
    assert r.allow_duplicates == data['allow_duplicates']
    assert r.dependencies == data['dependencies']

# Generated at 2022-06-13 08:55:32.787069
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    assert RoleMetadata().deserialize({}).__dict__ == RoleMetadata().__dict__

# Generated at 2022-06-13 08:55:37.374689
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():

    # Create the object
    obj = RoleMetadata()

    # Test with no argument
    obj.deserialize({})

    # Test with data
    obj.deserialize(dict(allow_duplicates=True, dependencies=["foo", "bar"]))

    # Test bad argument
    try:
        obj.deserialize([])
    except AnsibleParserError:
        pass

# Generated at 2022-06-13 08:55:41.752342
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    """
    Test deserialize method of class RoleMetadata
    """
    print()
    metadata=RoleMetadata.load(dict(allow_duplicates=False, dependencies=[],), None)
    data=dict(allow_duplicates=True, dependencies=[],)
    metadata.deserialize(data)
    assert metadata.allow_duplicates==True
    print('OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK OK')

# Generated at 2022-06-13 08:55:47.294973
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    metadata = RoleMetadata()
    data = dict(allow_duplicates=True, dependencies=['galaxy.role,version,name'])
    metadata.deserialize(data)
    assert metadata.allow_duplicates == True
    assert len(metadata.dependencies) == 1
    assert isinstance(metadata.dependencies[0], dict)

# unit test for create RoleMetadata obj by method load of class RoleMetadata

# Generated at 2022-06-13 08:55:58.555422
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    import collections, sys
    if sys.version_info[0] < 3:
        import __builtin__ as builtins
    else:
        import builtins
    metadata = dict(
            allow_duplicates=True,
            dependencies=[
                dict(
                    src="https://github.com/myuser/myrole",
                    scm="git",
                    version="v1.0",
                    name="newrole"),
                dict(
                    src="https://github.com/myuser/myotherrole",
                    scm="git",
                    name="myotherrole"
                )
            ]
    )
    module = RoleMetadata()
    module.load_data(metadata)
    assert module._allow_duplicates == True
    assert isinstance(module._dependencies[0], RoleInclude)
    assert module._depend

# Generated at 2022-06-13 08:56:14.391481
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.playbook.role_include import RoleInclude
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.utils.collection_loader import AnsibleCollectionLoader
    from ansible.utils.collection_loader.data import DataLoader

    acl = AnsibleCollectionLoader()
    collection_name = 'ansible.posix'
    role_name = 'common'
    collection_ident = collection_name + '.z' + role_name
    collection = acl.load_collection(collection_ident)

    dl = DataLoader()
    ds = dl.load_from_file(collection.get_role_path(role_name))

    RoleMetadata.load(ds, current_role_path=collection.get_role_path(role_name))


# Generated at 2022-06-13 08:56:16.485870
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    role_metadata = RoleMetadata()
    serialize_result = role_metadata.serialize()
    assert isinstance(serialize_result, dict)


# Generated at 2022-06-13 08:56:33.612638
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.playbook.role.definition import RoleDefinition
    # create a role definition
    role_def = {
        'name': 'test',
        'allow_duplicates': True,
    }
    rd = RoleDefinition.load('test', role_def, None, None)
    # create a RoleMetadata object
    ds = {'dependencies': {}}

    md = RoleMetadata.load(ds, rd)
    assert md.load_data(ds) == md
    assert md._owner == rd
    assert md._dependencies == {}
    assert md._allow_duplicates == False

# Generated at 2022-06-13 08:56:42.502830
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    # Test deserialization RoleMetadata works with and without the allow_duplicates option.
    # This test requires a RoleMetadata object in which to run the deserialization method.
    # The need to create and assign an owner to the RoleMetadata is somehow not part of the
    # API of this class, but it is needed to run the deserialization process, thus it is
    # created below and assigned.
    owner = "test_owner"
    role_metadata = RoleMetadata(owner=owner)

    # This is the data the the deserialization is run on.
    data_duplicates_on = dict(allow_duplicates=True)
    data_duplicates_off = dict(allow_duplicates=False)

    # Run and test deserialization without the allow_duplicates option.
    role_metadata.des

# Generated at 2022-06-13 08:56:51.480488
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    '''
    Unit test for method serialize of class RoleMetadata
    '''
    class C(object):
        def __init__(self, name):
            self.name = name
        def get_name(self):
            return self.name

    # create the object
    o = RoleMetadata(owner=C(name='test'))
    o._allow_duplicates = False
    o._dependencies = ['test']
    o._galaxy_info = 'galaxy_info'
    o._argument_specs = 'argument_specs'
    o._ds = 'ds'

    # test serialize
    res_serialize = o.serialize()

# Generated at 2022-06-13 08:56:56.635170
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    meta = RoleMetadata(None)
    assert meta is not None, "RoleMetadata object not initialized!"
    assert meta.allow_duplicates == False, "RoleMetadata: allow_duplicates not False!"
    assert meta.dependencies == [], "RoleMetadata: dependencies not [], but: %s" % meta.dependencies

# Generated at 2022-06-13 08:57:06.882874
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    # Create the object RoleMetadata
    role_metadata = RoleMetadata()
    # Call the method deserialize
    role_metadata.deserialize(dict(
            allow_duplicates=True,
            dependencies=[{'role': 'b'}]
        )
    )
    assert getattr(role_metadata, 'allow_duplicates') == True
    assert getattr(role_metadata, 'dependencies') == [{'role': 'b'}]


# Generated at 2022-06-13 08:57:07.781024
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    m = RoleMetadata()
    m.serialize()

# Generated at 2022-06-13 08:57:18.303352
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():

    # test empty dictionary
    md = RoleMetadata(owner='owner')
    ds = {'allow_duplicates': False, 'dependencies': []}
    md.load(data=ds, owner='owner')
    assert md.serialize() == ds

    # test allow_duplicates = True
    ds = {'allow_duplicates': True, 'dependencies': []}
    md.load(data=ds, owner='owner')
    assert md.serialize() == ds

    # test dependencies
    ds = {'allow_duplicates': False, 'dependencies': ['role_dependency_1', 'role_dependency_2']}
    md.load(data=ds, owner='owner')
    assert md.serialize() == ds

# Generated at 2022-06-13 08:57:20.573229
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    from ansible.playbook.role.definition import RoleDefinition
    rd1 = RoleDefinition()

    rm1 = RoleMetadata()
    assert rm1.owner is None

    rm2 = RoleMetadata(owner=rd1)
    assert id(rm2.owner) == id(rd1)

    rm3 = RoleMetadata(owner=rd1)
    assert id(rm3.owner) == id(rd1)

# Generated at 2022-06-13 08:57:25.922896
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    role = RoleMetadata()
    data = dict(
        allow_duplicates=True,
        dependencies=['common']
    )
    role.deserialize(data)
    assert role.serialize() == data


# Generated at 2022-06-13 08:57:31.153259
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    role_metadata = RoleMetadata()
    role_metadata.deserialize({'galaxy_info': {'author': 'Test author', 'description': 'Desc'}, 'dependencies': []})

    # test attribute values
    assert role_metadata._galaxy_info['author'] == 'Test author'
    assert role_metadata._galaxy_info['description'] == 'Desc'
    assert role_metadata._dependencies == []

# Generated at 2022-06-13 08:57:38.190482
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    RoleMetadata()
    return True

# Generated at 2022-06-13 08:57:41.539108
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    inst = RoleMetadata(owner=None)
    inst.allow_duplicates = True
    inst.dependencies = []
    assert isinstance(inst.serialize(), dict)

# Generated at 2022-06-13 08:57:44.337941
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    role_name = 'testRole' # name of the role
    role = MockRole(role_name) # role object
    role_metadata = RoleMetadata(role) # role metadata object

# Generated at 2022-06-13 08:57:52.193360
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.playbook.role_include import RoleInclude
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.vars import merge_hash

    # set up some variables to pass into the task queue manager
    inventory = Inventory("/dev/null")
    loader = DataLoader()
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    # set up the TaskQueueManager
    hostvars = {}

# Generated at 2022-06-13 08:57:52.827376
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    pass

# Generated at 2022-06-13 08:58:03.006122
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.playbook.collectionsearch import CollectionSearchImp
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.role import Role
    import os

    metadata = RoleMetadata(owner=Role(name='geerlingguy.ntp'))
    metadata.load({},'geerlingguy.ntp')
    metadata.load({'dependencies':['nickjj.custom-motd']},'geerlingguy.ntp')
    metadata.load({'allow_duplicates':True,'dependencies':['nickjj.custom-motd']},'geerlingguy.ntp')

    def test():
        metadata.load({'allow_duplicates':'bob'},'geerlingguy.ntp')

# Generated at 2022-06-13 08:58:11.281589
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    '''
    Test the `RoleMetadata.load` method. Returns True if tests passed
    '''
    from ansible.playbook import Play
    from ansible.playbook.role import Role

    test_play = Play.load(
        dict(
            name="test play",
            hosts=['localhost'],
            gather_facts=False,
            roles=['test_role'],
        ),
        variable_manager=None,
        loader=None,
    )
    test_role = Role.load(
        dict(
            name="test_role",
            tasks=[
                dict(action=dict(module='ping', args='foo=bar'))
            ]
        ),
        play=test_play,
        parent_role=None,
        loader=None,
    )


# Generated at 2022-06-13 08:58:14.132116
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    role_meta = RoleMetadata()

    assert role_meta._dependencies == []
    assert role_meta._allow_duplicates == False
    assert role_meta._argument_specs == {}

    print("RoleMetadata: OK")

if __name__ == '__main__':
    test_RoleMetadata()

# Generated at 2022-06-13 08:58:24.327195
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    m = RoleMetadata()
    data = m.serialize()

    assert isinstance(data, dict)
    assert len(data) == 2

    dependency_list = [{'role': 'role1'}, {'role': 'role2'}]
    allow_duplicates = True

    m = RoleMetadata()
    setattr(m, 'dependencies', dependency_list)
    setattr(m, 'allow_duplicates', allow_duplicates)
    data = m.serialize()

    assert isinstance(data, dict)
    assert len(data) == 2
    assert data['dependencies'] == dependency_list
    assert data['allow_duplicates'] == allow_duplicates


# Generated at 2022-06-13 08:58:28.061932
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    role_meta = RoleMetadata()
    deserialized_data = {'allow_duplicates': False, 'dependencies': []}
    role_meta.deserialize(deserialized_data)
    assert role_meta._allow_duplicates == False
    assert role_meta._dependencies == []

# Generated at 2022-06-13 08:58:45.468448
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():

    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.block import Block

    from ansible.utils.vars import combine_vars

    from units.mock.loader import DictDataLoader

    from ansible.utils.display import Display
    Display().verbosity = 4

    rpath = dict(
        basedir='/etc/ansible/roles/a_role',
    )
    loader = DictDataLoader({
        "meta/main.yml": """
name: A Role
description: Mocked test role
dependencies:
- { role: b_role, src: https://github.com/user/b_role.git }
"""
    })


# Generated at 2022-06-13 08:58:49.050084
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    from ansible.playbook.role import Role
    from ansible.playbook.block import Task
    role = Role()
    print(role._metadata)

    task = Task()
    task._attributes = { "b": "b" }
    print(task.b)
    print(task._attributes)
    task.b = 3
    print(task.b)
    print(task._attributes)
    print(task.serialize())
    print(task.deserialize({ "b": "B" }))

if __name__ == '__main__':
    test_RoleMetadata()

# Generated at 2022-06-13 08:58:51.824248
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    data = dict(
        allow_duplicates=True,
        dependencies=[]
    )
    assert RoleMetadata().deserialize(data) == data

# Generated at 2022-06-13 08:58:56.482950
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    obj = RoleMetadata()
    data = dict(allow_duplicates=False, dependencies = [])
    obj.deserialize(data)
    assert obj.allow_duplicates == data.get('allow_duplicates', False)
    assert obj.dependencies == data.get('dependencies', [])


# Generated at 2022-06-13 08:59:01.479884
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.playbook.role import Role
    role = Role.load('/path/to/a/role', None, None, None)
    role_metadata_1 = RoleMetadata(owner=role).load_data({}, variable_manager=None, loader=None)
    assert isinstance(role_metadata_1, RoleMetadata)
    assert not hasattr(role_metadata_1, 'galaxy_info')

# Generated at 2022-06-13 08:59:04.397620
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    role_metadata = RoleMetadata()
    role_metadata.deserialize({'allow_duplicates': True, 'dependencies': ['role1']})
    assert role_metadata._dependencies == ['role1']
    assert role_metadata._allow_duplicates == True

# Generated at 2022-06-13 08:59:11.189686
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    from ansible.playbook import Playbook
    from ansible.playbook.role import Role
    from ansible.playbook.play_context import PlayContext

    # Basic constructor test
    test_1 = RoleMetadata()
    assert isinstance(test_1, RoleMetadata)

    # create an owner to test load()'s handling of owner
    pb = Playbook.load(dict(hosts=[]), variable_manager=None, loader=None)
    pb.ROLE_CACHE = {}
    role = Role.load(dict(hosts=[], tasks=[]), pb, _role_path="fake_dir")
    role.load_context(variable_manager=None, loader=None)

    # Test that load() returns a RoleMetadata

# Generated at 2022-06-13 08:59:20.531847
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    from ansible.playbook.role import RoleInclude
    from ansible.playbook.helpers import load_list_of_roles
    from ansible.playbook.play_context import PlayContext

    role = RoleMetadata()
    role._owner = RoleInclude()
    role._owner._play = PlayContext()
    role_dependency_list = []
    role_dependency_list.append("http://github.com/github_user/ansible-role-repo.git,v1.9.1,new_name")
    role._dependencies = role_dependency_list
    role._owner._role_collection = 'ansible_namespace.collection_name'
    roles = []
    roles.append(role)

    # Process the role dependency list
    processed_roles = load_list_of_roles

# Generated at 2022-06-13 08:59:29.665370
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    # initialize arguments
    role = None

    # create RoleMetadata object
    role_metadata = RoleMetadata(owner=role)

    # verify class fields
    assert role_metadata._allow_duplicates == False
    assert role_metadata._dependencies == list()
    assert role_metadata._owner == None
    assert role_metadata._argument_specs == dict()
    assert role_metadata._galaxy_info == None

# Generated at 2022-06-13 08:59:32.535916
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    data = dict(
        allow_duplicates=True,
        dependencies=[{'role': 'common', 'version': '1.0'}]
    )
    role_metadata = RoleMetadata.load(data, {})
    assert role_metadata.serialize() == data

# Generated at 2022-06-13 09:00:04.026214
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    class MockRole(object):
        name = 'test'
        role_path = '/some/path/test'
        _play = None
        _loader = None
        _variable_manager = None

    m = RoleMetadata(owner=MockRole())
    m.deserialize(dict(allow_duplicates=True,
                       dependencies=[dict(role='foo', tasks_from='main.yaml'),
                                     dict(role='bar', tasks_from='main.yaml')]))
    assert m._allow_duplicates is True
    assert m._dependencies == [dict(role='foo', tasks_from='main.yaml'),
                               dict(role='bar', tasks_from='main.yaml')]


# Generated at 2022-06-13 09:00:05.977842
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    """
    @Test: Test serializing a RoleMetadata object
    @Feature: RoleMetadata Class
    @Assert: Returns a dictionary
    """
    metadata = RoleMetadata()
    serialized = metadata.serialize()

    assert isinstance(serialized, dict)

# Generated at 2022-06-13 09:00:11.861383
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    RoleMetadata_Obj = RoleMetadata()
    RoleMetadata_Obj.allow_duplicates = True
    RoleMetadata_Obj.dependencies = "test"

    assert RoleMetadata_Obj.serialize() == {
        'allow_duplicates': True,
        'dependencies': "test"
    }

    RoleMetadata_Obj.allow_duplicates = False
    RoleMetadata_Obj.dependencies = "test"

    assert RoleMetadata_Obj.serialize() == {
        'allow_duplicates': False,
        'dependencies': "test"
    }


# Generated at 2022-06-13 09:00:16.045375
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    data = {'allow_duplicates': False, 'dependencies': []}
    role_metadata = RoleMetadata()
    role_metadata.deserialize(data)
    assert role_metadata.allow_duplicates == False
    assert role_metadata.dependencies == []

# Generated at 2022-06-13 09:00:19.942082
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    from ansible.playbook.role.definition import RoleDefinition
    rd = RoleDefinition()
    rm = RoleMetadata(rd)
    assert rm._owner is rd
    assert rm.allow_duplicates is False



# Generated at 2022-06-13 09:00:21.617645
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    # TODO: check if all the fields of class RoleMetadata contains correct values after initialization
    role_metadata = RoleMetadata()

# Generated at 2022-06-13 09:00:29.219883
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.playbook.role import Role
    from ansible.playbook.role.meta import RoleMetadata
    from ansible.playbook.task import Task
    from ansible.plugins.loader import role_loader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.template import Templar
    from ansible.plugins.filter.core import FilterModule

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=['hosts'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    tasks = [Task()]
    role_meta = role_loader.get('meta', 'main.yml')

# Generated at 2022-06-13 09:00:39.106210
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():

    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.roles.include import RoleInclude

    meta = {
        "dependencies": [
            {
                "role": "common",
            },
            "geerlingguy.java",
            "geerlingguy.pip",
            "geerlingguy.composer",
            "geerlingguy.drush",
            {
                "role": "geerlingguy.apache",
            }
        ]
    }
    t = RoleMetadata().load_data(meta)
    assert type(t.dependencies) == list
    assert type(t.dependencies[0]) == RoleInclude
    assert type(t.dependencies[0]._role) == TaskInclude

# Generated at 2022-06-13 09:00:43.312262
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    data = {'allow_duplicates': 'no', 'dependencies': [{'role': 'foo.bar'}]}
    owner = None
    variable_manager = None
    loader = None

    test = RoleMetadata.load(data, owner, variable_manager=variable_manager, loader=loader)
    assert test.deserialize(data)

# Generated at 2022-06-13 09:00:49.624345
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    # Test default values
    r = RoleMetadata()
    r.deserialize({})
    assert r.allow_duplicates == False
    assert r.dependencies == []
    # Test specific values
    r.deserialize({'allow_duplicates': True, 'dependencies': [{'role': 'b'}, {'role': 'c'}]})
    assert r.allow_duplicates
    assert r.dependencies == [{'role': 'b'}, {'role': 'c'}]
    # Test invalid attributes
    failed = False
    try:
        r.deserialize({'invalid_attr': 'invalid_attr'})
    except:
        failed = True
    assert failed


# Generated at 2022-06-13 09:01:18.869767
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    pass

# Generated at 2022-06-13 09:01:28.014175
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    """
    Serialize object RoleMetadata
    """
    Base._initialize()
    expected_result = {"allow_duplicates": False, "dependencies": []}

    owner = Base()
    owner.set_loader(None)
    owner.set_variable_manager(None)

    role_metada = RoleMetadata()
    role_metada._owner = owner
    role_metada._allow_duplicates = False
    role_metada._dependencies = []

    assert expected_result == role_metada.serialize()

# Generated at 2022-06-13 09:01:28.776998
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    assert RoleMetadata()

# Generated at 2022-06-13 09:01:34.738685
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    role_metadata = RoleMetadata()
    dependencies = ["geerlingguy.ntp", "geerlingguy.apache"]
    setattr(role_metadata, 'allow_duplicates', False)
    setattr(role_metadata, 'dependencies', dependencies)
    d = role_metadata.serialize()
    assert d['dependencies'] == dependencies
    assert d['allow_duplicates'] == False

# Generated at 2022-06-13 09:01:46.429256
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    data = dict()

    # Test the case when allow_duplicates is not passed.
    data['allow_duplicates'] = None
    data['dependencies'] = "somevalue"
    obj = RoleMetadata()
    obj.deserialize(data)
    obj_serialized = obj.serialize()
    assert obj_serialized['allow_duplicates'] == False
    assert obj_serialized['dependencies'] == "somevalue"

    # Test the case when allow_duplicates is passed as a boolean value.
    data['allow_duplicates'] = True
    data['dependencies'] = "someothervalue"
    obj = RoleMetadata()
    obj.deserialize(data)
    obj_serialized = obj.serialize()
    assert obj_serialized['allow_duplicates'] == True
   

# Generated at 2022-06-13 09:01:57.568163
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    from ansible.parsing.mod_args import ModuleArgsParser
    from ansible.vars import VariableManager
    from ansible.playbook.helpers import load_list_of_roles
    from ansible.playbook.role import Role
    import json
    import os

    current_dir = os.path.dirname(__file__)
    fixtures_path = os.path.join(current_dir, 'fixtures', 'role_data')
    valid_meta_data = {}
    with open(os.path.join(fixtures_path, "valid_meta_data.json"), 'r') as valid_meta_f:
        valid_meta_data = json.loads(valid_meta_f.read())
    valid_meta_data_expected = {}

# Generated at 2022-06-13 09:02:03.687016
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    m = RoleMetadata.load(dict(
        galaxy_info=dict(
            author='mdehaan',
            description='An awesome role.',
            company='Mozilla',
            license='MPLv2',
            min_ansible_version='1.2',
            platforms=['Debian', 'RedHat', 'BSD'],
            dependencies=[
                {'role': 'webserver', 'version_requirement': '>= 0.1'},
                'database'
            ]
        ),
        allow_duplicates=True,
        dependencies=['foo', 'bar'],
        test_collection=dict(
            meta=dict(
                description="A collection for testing metadata"
            )
        )
    ), owner=None)