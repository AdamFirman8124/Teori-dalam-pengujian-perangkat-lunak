

# Generated at 2022-06-13 08:52:20.137029
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    role_metadata = RoleMetadata()
    role_metadata.deserialize({'allow_duplicates': True, 'dependencies': []})
    assert role_metadata._allow_duplicates == True
    assert not role_metadata._dependencies

# Generated at 2022-06-13 08:52:28.085227
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    rmd = RoleMetadata.load({
                             'allow_duplicates': True,
                             'dependencies': [ 'B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z' ]
                            },None,None,None)
    data = rmd.serialize()
    assert isinstance(data, dict)
    assert data['allow_duplicates']
    assert 'dependencies' in data
    # Test all upper case letters to assure alphabetical order of dependency list

# Generated at 2022-06-13 08:52:32.045185
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    r = RoleMetadata()
    r.deserialize({'allow_duplicates':True})
    assert r.serialize() == {'allow_duplicates':True, 'dependencies':[]}

# Generated at 2022-06-13 08:52:43.384774
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    import ansible.constants as C

    # Return True if deserialize method set attributes 'allow_duplicates' and 'dependencies'
    # of data 'role_metadata' as True and []
    def isDeserializeCalled(role_metadata, data):
        return data.get('allow_duplicates', False) == getattr(role_metadata, 'allow_duplicates', False) and \
            data.get('dependencies', []) == getattr(role_metadata, 'dependencies', [])

    # Testcase to check whether deserialize method of class RoleMetadata
    # is called

# Generated at 2022-06-13 08:52:49.127333
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    data = { "allow_duplicates": True,
             "dependencies" : [{"role": "b",
                                "vars": {"x": "y"}},
                               {"role": "c"}]
        }
    m = RoleMetadata()
    m.deserialize(data)
    assert m.allow_duplicates is True
    assert len(m.dependencies) == 2
    assert m.dependencies[0]["role"] == "b"
    assert m.dependencies[1]["role"] == "c"



# Generated at 2022-06-13 08:53:00.422590
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    role_metadata = RoleMetadata()
    assert role_metadata.allow_duplicates == False
    assert role_metadata.dependencies == list()

    class MockRole(object):
        def __init__(self):
            self.name = "mock.role"

    class MockPlay(object):
        def __init__(self):
            self.name = "mockplay"
            self.roles = [MockRole()]

    mock_obj = MockRole()
    mock_obj.main_file = "./meta/main.yml"
    mock_obj._role_path = "./mock.role"
    mock_obj._play = MockPlay()
    mock_obj._role_collection = None

    # Constructor with owner
    role_metadata = RoleMetadata(owner=mock_obj)

# Generated at 2022-06-13 08:53:10.500640
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.role.include import RoleInclude

    data = {
        'allow_duplicates': False,
        'dependencies': [ 'role1', 'role2'],
        'galaxy_info': {}, # not implemented yet
        'allow_ansible_core_to_update': False
    }
    data_ds = {
        'allow_duplicates': False,
        'dependencies': [ 'role1', 'role2'],
        'galaxy_info': {}, # not implemented yet
        'allow_ansible_core_to_update': False
    }
    # create a RoleDefinition
    role_def = RoleDefinition()
    role_def.role_path = '/path/to/role'
    # test the method

# Generated at 2022-06-13 08:53:14.661394
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    # Test if correct serialized data is generated
    data = {}
    data['allow_duplicates'] = False
    data['dependencies'] = []
    m = RoleMetadata()
    m.deserialize(data)
    assert m.serialize() == data

if __name__ == "__main__":
    test_RoleMetadata_serialize()

# Generated at 2022-06-13 08:53:23.087728
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():

    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.role.include import RoleInclude
    from ansible.playbook.play import Play
    from ansible.playbook.role.sanity import RoleSanityException

    m = RoleMetadata()
    play = Play().load({
        'name': 'test play',
        'hosts': 'localhost',
        'roles': [
            {'name': 'test_role', 'role_path': 'test_role'},
        ],
    }, variable_manager=None, loader=None)
    role = None
    for role in play.get_roles():
        if role.get_name() == 'test_role':
            break

# Generated at 2022-06-13 08:53:33.850668
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    # Create an instance of a  RoleMetadata
    r = RoleMetadata()

    # Create an instance of a  Role
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.play_context import PlayContext
    playcontext = PlayContext(play=None)
    role = RoleDefinition.load(path='./tests/lib/ansible/playbook/units/metadata',
                               name='myrole',
                               play_context=playcontext,
                               variable_manager=None,
                               loader=None)
    # Create an instance of a  RoleRequirement
    from ansible.playbook.role.requirement import RoleRequirement

# Generated at 2022-06-13 08:53:49.744969
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    import os
    import sys
    import inspect
    import json
    import tempfile
    from ansible.playbook.block import Block
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.utils.vars import combine_vars
    from ansible.plugins.loader import action_loader
    from ansible.plugins.callback import CallbackBase
    from ansible.template import Templar
    from ansible.errors import AnsibleError
    from ansible.galaxy.role import Role

# Generated at 2022-06-13 08:53:54.337480
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    role_metadata = RoleMetadata()
    assert isinstance(role_metadata._allow_duplicates, bool)
    assert role_metadata._allow_duplicates is False
    assert isinstance(role_metadata._dependencies, list)
    assert role_metadata._dependencies == []

# Generated at 2022-06-13 08:53:57.498661
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    # Make sure that RoleMetadata.serialize returns the correct dict
    get_data = RoleMetadata(owner=None).serialize()
    data = dict(allow_duplicates=False, dependencies=[])
    assert get_data == data



# Generated at 2022-06-13 08:54:01.267004
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    t_RoleMetadata = RoleMetadata()
    t_RoleMetadata.allow_duplicates = True
    t_RoleMetadata.dependencies = []
    data = t_RoleMetadata.serialize()
    assert data == {'allow_duplicates': True, 'dependencies': []}


# Generated at 2022-06-13 08:54:02.806970
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    role_metadata = RoleMetadata()
    role_metadata.allow_duplicates = Fals

# Generated at 2022-06-13 08:54:10.669263
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    from ansible.executor.task_result import TaskResult
    from ansible.playbook.task import Task
    from ansible.playbook.play import Play
    from ansible.playbook.role.definition import RoleDefinition


# Generated at 2022-06-13 08:54:11.742489
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    pass


# Unit tests for class RoleMetadata

# Generated at 2022-06-13 08:54:18.465340
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    from ansible.playbook import Play
    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext

    myplay = Play().load({'name': 'myplay', 'hosts': 'all', 'gather_facts': 'no'})

    p = RoleMetadata(owner=myplay)
    assert p.serialize() == dict(allow_duplicates=False, dependencies=[])

# Generated at 2022-06-13 08:54:27.568099
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    from ansible.playbook.play_context import PlayContext
    variable_manager = VariableManager()
    variable_manager.extra_vars = {'hostvars':{}}
    variable_manager.hostvars = variable_manager.extra_vars['hostvars']
    role_context = PlayContext(variable_manager=variable_manager)

    with pytest.raises(AnsibleParserError) as excinfo:
        RoleMetadata.load({0:0}, None)
    excinfo.match(r"the 'meta/main.yml' for role .* is not a dictionary")

    data = {'a':1, 'b':2}
    r = RoleMetadata.load(data, None)
    assert r.a == 1
    assert r.b == 2

# Generated at 2022-06-13 08:54:37.457084
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    import pytest

    name = 'test_role'
    m = RoleMetadata(owner='owner')

    # test second argument is a list
    data = {name: 'var'}
    with pytest.raises(AnsibleParserError) as excinfo:
        m.deserialize(data)
    assert str(excinfo.value) == "Expected role dependencies to be a list."

    # test second argument is a not valid list
    data = {name: ['var1', 'var2']}
    with pytest.raises(AnsibleParserError) as excinfo:
        m.deserialize(data)
    assert str(excinfo.value) == (
        "A malformed list of role dependencies was encountered."
    )

# Generated at 2022-06-13 08:54:52.774086
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.playbook.role.definition import RoleDefinition
    data = {'allow_duplicates': True, 'dependencies': []}
    owner = RoleDefinition()
    r = RoleMetadata.load(data, owner)
    assert r.allow_duplicates == True
    assert r.dependencies == []


# Generated at 2022-06-13 08:54:57.504313
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    # Test serialize
    # Correct input
    input = dict(
        allow_duplicates=False,
        dependencies=[]
    )
    # Create a RoleMetadata object
    obj = RoleMetadata()
    # Call deserialize of class RoleMetadata to populate object data from input
    obj.deserialize(input)
    # Check object data
    assert obj.allow_duplicates == False
    assert obj.dependencies == []

# Generated at 2022-06-13 08:55:02.835302
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    # Test acceptable input
    result = RoleMetadata.load({'test': {'test':'test'}}, 'test')
    assert isinstance(result, RoleMetadata)
    # Test unacceptable input
    try:
        result = RoleMetadata.load('test', 'test')
    except AnsibleParserError:
        pass
    else:
        raise AssertionError()

# Generated at 2022-06-13 08:55:11.008304
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    rm1 = RoleMetadata()
    rm1.deserialize({'allow_duplicates': True, 'dependencies': ['test_role1', 'test_role2']})
    assert rm1.allow_duplicates is True and rm1.dependencies == ['test_role1', 'test_role2']
    rm2 = RoleMetadata()
    rm2.deserialize({'dependencies': ['test_role3']})
    assert rm2.allow_duplicates is False and rm2.dependencies == ['test_role3']

# Generated at 2022-06-13 08:55:12.351814
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    metadata = RoleMetadata(owner=None)
    assert metadata is not None

# Generated at 2022-06-13 08:55:15.339498
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    metadata = RoleMetadata()
    data = dict()
    setattr(metadata, 'allow_duplicates', data.get('allow_duplicates', False))
    assert metadata._allow_duplicates == False
    assert metadata._dependencies == []

# Generated at 2022-06-13 08:55:27.243465
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    # https://github.com/ansible/ansible/issues/48227
    # https://github.com/ansible/ansible/issues/56750
    # https://github.com/ansible/ansible/pull/56762

    # public API so it shouldn't be changed
    from ansible.playbook.play_context import PlayContext

    from ansible.playbook.play import Play

    from ansible.playbook.role_include import RoleInclude

    from ansible.playbook.conditional import Conditional

    from ansible.template import Templar

    # this enforces the rule that RoleInclude objects are always loaded with a parent Play
    play = Play.load({
        'name': 'test',
        'hosts': 'localhost'
    }, variable_manager=None, loader=None)

# Generated at 2022-06-13 08:55:33.785367
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    metadata = RoleMetadata(owner=None)
    data = dict()
    metadata.deserialize(data)
    assert metadata.allow_duplicates == False
    assert metadata.dependencies == []
    data = dict(allow_duplicates=True, dependencies=['a'])
    metadata.deserialize(data)
    assert metadata.allow_duplicates == True
    assert metadata.dependencies == ['a']

# Generated at 2022-06-13 08:55:41.692722
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    from ansible.playbook.role_include import RoleInclude

    m = RoleMetadata()
    data = dict(
        allow_duplicates=False,
        dependencies=[
            dict(
                name='apache',
                src='/path/to/apache/folder',
                scm='git',
                version='v1.0',
                paths=['tasks', 'handlers'],
            )
        ],
    )
    m.deserialize(data)

    assert m._dependencies[0]._role_name == 'apache'
    assert m._dependencies[0]._role_path == '/path/to/apache/folder'
    assert m._dependencies[0]._role_scm == 'git'
    assert m._dependencies[0]._role_version == 'v1.0'

# Generated at 2022-06-13 08:55:45.793611
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    r = RoleMetadata()
    data = dict(
        allow_duplicates = False,
        dependencies = []
    )
    r.deserialize(data)
    assert r.get_allow_duplicates() == False
    assert r.get_dependencies() == []


# Generated at 2022-06-13 08:56:19.552463
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.playbook import Playbook
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.role_context import RoleContext

    # A basic Role
    fake_play = Playbook().load(dict(
        name='Test Play 01',
        hosts=[],
        roles=[dict(
            name='TestRole01',
            tasks=[dict(action='setup')]
        )],
        vars=dict(
            foo='bar'
        )
    ), variable_manager=PlayContext())
    fake_role = fake_play.get_roles('TestRole01')[0]

    # Test
    fake_metadata = dict(
        allow_duplicates=True,
        dependencies=[dict(name='TestRole02')]
    )

# Generated at 2022-06-13 08:56:20.326630
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    RoleMetadata(owner=None)

# Generated at 2022-06-13 08:56:26.676099
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    import collections
    from ansible.playbook.block import Block
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.role import RoleRequirement
    from ansible.playbook.role import Role

    host = "127.0.0.1"
    block = Block()
    playcontext = collections.namedtuple('PlayContext', 'remote_addr')
    play_context = playcontext(remote_addr=host)
    play = Play().load({
        'name': "Ansible Play",
        'hosts': 'localhost',
        'gather_facts': 'no',
        'tasks': [
        ]
    }, variable_manager=None, loader=None)
    play.set_loader(loader=None)
    play.set_variable

# Generated at 2022-06-13 08:56:31.966261
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    m = RoleMetadata()
    m.deserialize({'allow_duplicates': True, 'dependencies': ['foo.bar,v1.0', 'baz.qux,v1.0']})
    assert m.allow_duplicates == True
    assert m.dependencies == ['foo.bar,v1.0', 'baz.qux,v1.0']


# Generated at 2022-06-13 08:56:33.611746
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    role_metadata = RoleMetadata()

    assert isinstance(role_metadata, RoleMetadata)

# Generated at 2022-06-13 08:56:34.151736
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    assert False

# Generated at 2022-06-13 08:56:35.007385
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    role = RoleMetadata()
    assert role is not None

# Generated at 2022-06-13 08:56:35.558096
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    assert True

# Generated at 2022-06-13 08:56:39.020426
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    meta = RoleMetadata(owner=False)
    meta.deserialize({'allow_duplicates': True,
                      'dependencies': [{'src': 'jdoe.foo'}]})
    assert not meta._owner
    assert meta.allow_duplicates
    assert meta.dependencies == [{'src': 'jdoe.foo'}]

# Generated at 2022-06-13 08:56:41.755285
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    # test must instantiate class RoleMetadata
    r = RoleMetadata()
    assert r is not None

if __name__ == '__main__':
    test_RoleMetadata()

# Generated at 2022-06-13 08:57:31.672625
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    data = dict(
        allow_duplicates=True,
        dependencies=[]
    )
    roleMetadata = RoleMetadata()
    roleMetadata.deserialize(data)
    assert roleMetadata._allow_duplicates == True
    assert roleMetadata._dependencies == []

# Generated at 2022-06-13 08:57:47.580126
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.inventory.host import Host
    from ansible.vars.manager import VariableManager
    from ansible.vars.hostvars import HostVars

    vars_data = HostVars(Host(name='test_host'), dict(test_var=True))
    variable_manager = VariableManager(loader=None, inventory=None, version_info=None, host_vars=vars_data)


# Generated at 2022-06-13 08:57:54.180692
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    class A:
        def __init__(self):
            self._variable_manager = None
            self._loader = None
            self._play = None
            self._collections = []

    b = A()
    role_metadata = RoleMetadata(b)
    data = {'allow_duplicates': False, 'dependencies': []}
    exp_data = {'allow_duplicates': False, 'dependencies': []}

    role_metadata.deserialize(data)

    assert getattr(role_metadata, '_allow_duplicates', None) == exp_data['allow_duplicates']
    assert getattr(role_metadata, '_dependencies', None) == exp_data['dependencies']

# Generated at 2022-06-13 08:58:01.305011
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    class Owner(Base):
        _role_path = '/home/demo/roles/demo'

    test_data = {
        "allow_duplicates": True,
        "dependencies": ["demo1", "demo2"]
    }
    role_metadata = RoleMetadata.load(test_data, owner=Owner())
    assert role_metadata.allow_duplicates == test_data["allow_duplicates"]
    assert role_metadata.dependencies == test_data["dependencies"]

# Generated at 2022-06-13 08:58:08.904554
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    data = {
        'allow_duplicates': False,
        'dependencies': [
            {'role': 'test1', 'version': '1.0'},
            {'role': 'test2'},
            'test3'
        ]
    }
    role_metadata = RoleMetadata().load_data(data)
    assert role_metadata._dependencies[0].role == 'test1'
    assert role_metadata._dependencies[0].version == '1.0'
    assert role_metadata._dependencies[1].role == 'test2'
    assert role_metadata._dependencies[1].version == None
    assert role_metadata._dependencies[2].role == 'test3'
    assert role_metadata._dependencies[2].version == None

# Generated at 2022-06-13 08:58:11.796853
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    v = RoleMetadata()
    setattr(v, 'allow_duplicates', True)
    setattr(v, 'dependencies', [{'a':1}])
    assert v.serialize() == {'allow_duplicates':True, 'dependencies': [{'a':1}]}

# Generated at 2022-06-13 08:58:17.752953
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.playbook.role import Role
    from ansible.playbook.role.include import RoleInclude
    from ansible.utils.collection_loader import AnsibleCollectionConfig
    from ansible.parsing.yaml.loader import AnsibleLoader

    data = open('test/units/metadata.yml', 'rb').read()
    data = to_native(data)
    data = AnsibleLoader(data, file_name='/etc/ansible/foo').get_single_data()
    data = data['meta']
    role = Role.load({'name': 'test'})

    md = RoleMetadata.load(data, owner=role)
    assert md._allow_duplicates
    assert len(md._dependencies) == 2
    assert isinstance(md._dependencies[0], RoleInclude)
   

# Generated at 2022-06-13 08:58:27.626104
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    import ansible.playbook
    import ansible.playbook.role
    import ansible.playbook.role.metadata
    import ansible.playbook.role.always
    from ansible.utils.collection_loader import AnsibleCollectionLoader
    from ansible.vars import VariableManager

    # Prepare test data
    test_variable_manager = VariableManager()
    test_loader = AnsibleCollectionLoader()
    test_metadata = {
        'dependencies': [
            {
                'name': 'test_role',
                'version': '1.0'
            }
        ]
    }

    # Test

# Generated at 2022-06-13 08:58:30.436413
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    ansible_mocking.mock()
    configuration = setup_config()
    loader = set

# Generated at 2022-06-13 08:58:34.499821
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    roleMetadata_instance = RoleMetadata()

if __name__ == '__main__':
    # Unit test for constructor of class RoleMetadata
    test_RoleMetadata()

# Generated at 2022-06-13 08:59:08.313538
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.playbook.role_include import RoleInclude
    from ansible.playbook.role import Role
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext

    vars = dict()


# Generated at 2022-06-13 08:59:13.612369
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    from ansible.playbook.role.include import RoleInclude
    meta_data = {
        'allow_duplicates': False,
        'dependencies': [
            {'role': 'a'},
            {'role': 'b'},
            {'role': 'c'}
        ]
    }
    loaded = RoleMetadata().load(meta_data)
    data = loaded.serialize()
    assert(type(data['dependencies']) == list)
    assert([isinstance(x, RoleInclude) for x in data['dependencies']] == [True]*len(data['dependencies']))

# Generated at 2022-06-13 08:59:30.790222
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.playbook.play import Play
    from ansible.playbook.role import Role
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.task import Task
    from ansible.playbook.task.include import TaskInclude
    from ansible.utils.vars import combine_vars

    # Construct test case variables
    role_dependencies_data = [{'role': 'test_role'}, {'name': 'test_role'}, {'role': 'test_role', 'version': '1.1.1'}, {'name': 'test_role', 'version': '1.1.1'}]
    role_metadata_data = dict(dependencies=role_dependencies_data)
    role_data = dict(name='test_role', tasks=[])

    #

# Generated at 2022-06-13 08:59:33.511773
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    r = RoleMetadata()
    data = {
        'allow_duplicates': False,
        'dependencies': []
    }
    r.deserialize(data)
    assert r.allow_duplicates == False
    assert r.dependencies == []

# Generated at 2022-06-13 08:59:37.020738
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    data = dict(
        allow_duplicates=True,
        dependencies=["rolea", "roleb"]
    )

    rm = RoleMetadata()
    rm.deserialize(data)

    assert rm.serialize() == data

# Generated at 2022-06-13 08:59:43.727007
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    dependencies = [{'role': 'foo'}, {'role': 'bar'}]
    allow_duplicates = True

    test_object = RoleMetadata()
    test_object.allow_duplicates = allow_duplicates
    test_object.dependencies = dependencies

    serialized_object = test_object.serialize()
    assert serialized_object.get("allow_duplicates") == allow_duplicates
    assert serialized_object.get("dependencies") == dependencies

# Generated at 2022-06-13 08:59:54.901873
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    dependency_list = [
            dict(role=dict(name='common-tasks', src="source")),
            dict(role=dict(name='foo', src="source"))
      ]
    dependency_list2 = [
            dict(name='common-tasks', src="source"),
            dict(name='foo', src="source"),
      ]
    role_metadata = RoleMetadata()
    role_metadata.dependencies = dependency_list
    role_metadata.dependencies = dependency_list2
    dependency_list3 = [
            dict(another="source"),
            dict(name='common-tasks', src="source"),
            dict(name='foo', src="source")
      ]

# Generated at 2022-06-13 08:59:56.897917
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    print("Test RoleMetadata")
    rm = RoleMetadata(owner='owner')
    print("Test RoleMetadata Pass")


# Generated at 2022-06-13 09:00:05.533912
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    from ansible.playbook.role.definition import RoleDefinition
    serialized_data = {'allow_duplicates': False, 'dependencies': [{'name': 'test_dep'}]}

    data = RoleDefinition.deserialize(serialized_data)
    assert data.allow_duplicates == False
    for dep in data.dependencies:
        assert dep.metadata.name == "test_dep"

    serialized_data = {'allow_duplicates': True, 'dependencies': [{'name': 'test_dep'}]}
    data = RoleDefinition.deserialize(serialized_data)
    assert data.allow_duplicates == True
    for dep in data.dependencies:
        assert dep.metadata.name == "test_dep"


# Generated at 2022-06-13 09:00:08.279529
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    rmd = RoleMetadata()
    data = dict(
        allow_duplicates=True,
        dependencies=['test']
    )
    rmd.deserialize(data)
    assert rmd.allow_duplicates == True
    assert rmd.dependencies == ['test']

# Generated at 2022-06-13 09:01:26.649840
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    # create role
    role = RoleMetadata()

    # set attributes
    role.allow_duplicates = True
    role.dependencies = ['common', 'webserver']

    # test serialize
    as_dict = role.serialize()
    assert(as_dict == dict(allow_duplicates=True, dependencies=['common', 'webserver']))


# Generated at 2022-06-13 09:01:39.500734
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.parsing.dataloader import DataLoader

    ds = dict(
        allow_duplicates = True,
        dependencies = [ 'role1', {'name': 'role2'} ]
        )
    l = DataLoader()
    v = dict()

    # load method of class RoleMetadata takes 4 arguments
    # 1. data as dict
    # 2. owner (Role)
    # 3. variable_manager (VariableManager)
    # 4. loader (DataLoader)
    m = RoleMetadata.load(ds, None, v, l)
    assert(m._dependencies[0]._role_name == 'role1')
    assert(m._dependencies[1]._role_name == 'role2')

# Generated at 2022-06-13 09:01:48.698682
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.playbook.role import Role
    # test 'meta/main.yml' is not a dictionary
    role_content = open('tests/test_file/variablesTest/test_role_dependencies/role1/meta/main.yml', 'r')
    r = Role()
    try:
        RoleMetadata.load(role_content, r)
    except Exception as e:
        assert type(e) == AnsibleParserError
        assert str(e) == "the 'meta/main.yml' for role role1 is not a dictionary"
    role_content.close()

    # test role_def is new style
    role_content = open('tests/test_file/variablesTest/test_role_dependencies/role1/meta/main.yml', 'r')
    r = Role()
   

# Generated at 2022-06-13 09:01:50.153328
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    pass


# Generated at 2022-06-13 09:01:56.632867
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    role_metadata = RoleMetadata()
    role_metadata.deserialize({
        'allow_duplicates': True,
        'dependencies': ["common"]
    })
    try:
        assert role_metadata.allow_duplicates is True and role_metadata.dependencies == ["common"]
        print("Unit test success: %s" % "RoleMetadata.deserialize")
    except AssertionError:
        print("Unit test failed: %s" % "RoleMetadata.deserialize")

test_RoleMetadata_deserialize()

# Generated at 2022-06-13 09:02:00.557713
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    import os
    import ansible.playbook.role.definition
    import ansible.playbook.play
    import ansible.playbook.task

    p = ansible.playbook.play.Play.load(dict(
        name = "test play",
        hosts = 'some_hosts',
        gather_facts = 'no',
        roles = [
            dict(name = 'rolename', foo = 'bar'),
            dict(name = 'rolename2'),
        ]
    ), variable_manager=ansible.playbook.task.variable_manager.VariableManager(), loader=None)
    r = p.get_roles()[0]

# Generated at 2022-06-13 09:02:04.549487
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    role_metadata = RoleMetadata()
    role_metadata.deserialize({'dependencies': ['role1', 'role2'], 'allow_duplicates': True})
    assert role_metadata.dependencies == ['role1', 'role2']
    assert role_metadata.allow_duplicates is True

# Generated at 2022-06-13 09:02:05.718284
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    """
    Validate the basic constructor of RoleMetadata.
    """
    role_metadata = RoleMetadata()
    assert isinstance(role_metadata, RoleMetadata)

# Generated at 2022-06-13 09:02:10.885241
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    testdata  = {'name': 'testrole'}
    owner = RoleMetadata(testdata)

    # Load the data into a RoleMetadata object
    m = RoleMetadata.load(None, owner)

    assert m._owner == owner
    assert m._allow_duplicates == False
    assert m._dependencies == []
    assert m._galaxy_info == None
    assert m._argument_specs == {}