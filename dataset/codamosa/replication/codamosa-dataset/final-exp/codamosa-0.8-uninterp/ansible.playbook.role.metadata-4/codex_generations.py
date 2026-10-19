

# Generated at 2022-06-13 08:52:17.641719
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    ''' test_RoleMetadata_serialize()
    This unit test is to test serialize functionality of class RoleMetadata
    '''
    serialize_data = dict(
        allow_duplicates=False,
        dependencies=[]
    )
    assert RoleMetadata().serialize() == serialize_data

# Generated at 2022-06-13 08:52:22.975979
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    role_metadata = RoleMetadata()
    role_metadata.allow_duplicates = True
    role_metadata.dependencies = ['foo', 'bar']
    serialized = role_metadata.serialize()
    assert (serialized == {'allow_duplicates': True, 'dependencies': ['foo', 'bar']})

# Generated at 2022-06-13 08:52:28.787361
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    metadata = RoleMetadata()
    setattr(metadata, 'allow_duplicates', False)
    setattr(metadata, 'dependencies', [])
    result_dict = metadata.serialize()
    assert isinstance(result_dict, dict)
    assert result_dict['allow_duplicates'] is False
    assert result_dict['dependencies'] == []



# Generated at 2022-06-13 08:52:36.609496
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    class TestRole:
        def __init__(self):
            self._role_path = ""

        def set_path(self, path):
            self._role_path = path

    class TestGalaxyInfo:
        def __init__(self):
            self.author = ""
            self.description = ""
            self.license = ""
            self.min_ansible_version = ""
            self.platforms = []
            self.galaxy_tags = []
            self.issues_url = ""
            self.company = ""
            self.repository = ""
            self.website = ""

    role = TestRole()
    galaxy_info = TestGalaxyInfo()

# Generated at 2022-06-13 08:52:47.230958
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.playbook import Play
    from ansible.playbook.role.definition import RoleDefinition

    # create play
    play_ds = dict(
        name='test play',
        hosts=['all'],
    )
    play = Play.load(play_ds, variable_manager=None, loader=None)

    # create role
    role_ds = dict(name='test role', path='/path/to/test/role')
    role = RoleDefinition.load(role_ds, play, variable_manager=None, loader=None)

    # create RoleMetadata
    meta_ds = dict(
        dependencies=[
            'dependency1',
            'dependency2'
        ],
        allow_duplicates=True
    )

# Generated at 2022-06-13 08:52:50.803090
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    role = RoleMetadata()
    setattr(role,'_allow_duplicates',False)
    setattr(role,'_dependencies',['test1','test2','test3'])
    assert role.serialize() == dict(dependencies=['test1','test2','test3'], allow_duplicates=False)


# Generated at 2022-06-13 08:52:54.186877
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    INVALID_DS = dict()
    class FakeOwner:
        name = "fake"
        _play = None
    assert isinstance(RoleMetadata.load(INVALID_DS, FakeOwner()), AnsibleParserError)


# Generated at 2022-06-13 08:52:57.545307
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    test = RoleMetadata()
    assert test._allow_duplicates == False
    assert test._dependencies == []
    assert test._galaxy_info == None
    assert test._argument_specs == {}

# Generated at 2022-06-13 08:53:06.970238
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.hosts import Group
    from ansible.playbook.role.metadata import RoleMetadata

    play_context = PlayContext()
    fake_loader = lambda x: None

# Generated at 2022-06-13 08:53:09.687317
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    data = dict(dependencies=['foo', 'bar'])
    role = RoleMetadata()
    role.deserialize(data)
    assert role._dependencies == ['foo', 'bar']

# Generated at 2022-06-13 08:53:28.562863
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    import pytest
    class Owner:
        def __init__(self):
            self._play = 'play'
            self._role_collection = 'collection'
        def get_name(self):
            return 'name'
    variable_manager = 'variable_manager'
    loader = 'loader'
    owner = Owner()
    data = dict(
        dependencies='dependencies'
    )
    # initialize the class
    role_metadata = RoleMetadata(owner)
    # load the data
    role_metadata.load(data, owner, variable_manager, loader)

# Generated at 2022-06-13 08:53:31.407495
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    """
    Tests AnsibleRole.RoleMetadata.serialize
    """

    setattr(self, 'allow_duplicates', data.get('allow_duplicates', False))
    setattr(self, 'dependencies', data.get('dependencies', []))


# Generated at 2022-06-13 08:53:32.592831
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    RoleMetadata(owner=None)

# Generated at 2022-06-13 08:53:36.332758
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    m.deserialize(data={'allow_duplicates': True, 'dependencies': [{'role': 'thiagolucio.esxi'}]})
    assert m._allow_duplicates == True
    assert m._dependencies[0].get_name() == 'thiagolucio.esxi'


# Generated at 2022-06-13 08:53:47.531910
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    import sys, inspect
    data = """
    {
        'tools': {
            'OS': 'Ubuntu',
            'Server': 'Apache'
        },
        'dependencies': {
            'apache': '*',
            'role3': '1.0.0rc1'
        },
        'allow_duplicates': True,
        'galaxy_info': {}
    }
    """

    if sys.version_info[0] < 3:
        reload(sys)
        sys.setdefaultencoding('utf8')
    if sys.version_info[0] < 3:
        from io import BytesIO
        data = BytesIO(data)


# Generated at 2022-06-13 08:53:48.543203
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    assert RoleMetadata().deserialize([]) == []

# Generated at 2022-06-13 08:53:57.911225
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    role_metadata = RoleMetadata()
    role_metadata.allow_duplicates = False
    role_metadata.dependencies = ['hello', 'world']
    assert {'allow_duplicates': False, 'dependencies': ['hello', 'world']} == role_metadata.serialize()
#
#
# def test_RoleMetadata_deserialize():
#     role_metadata = RoleMetadata()
#     role_metadata.deserialize({'allow_duplicates': False, 'dependencies': ['hello', 'world']})
#     assert {'allow_duplicates': False, 'dependencies': ['hello', 'world']} == role_metadata.serialize()
#
#

# Generated at 2022-06-13 08:54:02.686734
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    role = RoleMetadata()
    role.deserialize(dict())
    assert role.allow_duplicates is False
    assert role.dependencies == []
    role.deserialize(dict(allow_duplicates=True, dependencies=['a','b','c']))
    assert role.allow_duplicates is True
    assert role.dependencies == ['a','b','c']

# Generated at 2022-06-13 08:54:05.293684
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    data = dict(
        allow_duplicates=False,
        dependencies=[]
    )
    m = RoleMetadata()
    m.deserialize(data)
    assert m.serialize() == data

# Generated at 2022-06-13 08:54:12.260135
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    d = dict(
        allow_duplicates=True,
        dependencies=dict(
            role="webservers",
            name="testrole",
            src="https://github.com/foo/bar.git",
            scm="git",
            version="v1.3",
        ),
    )
    m = RoleMetadata()
    m.deserialize(d)
    assert m._dependencies[0].get_name() == d['dependencies']['name']
    assert m._dependencies[0].get_scm() == d['dependencies']['scm']
    assert m._dependencies[0].get_src() == d['dependencies']['src']
    assert m._dependencies[0].get_version() == d['dependencies']['version']
    assert m._allow_du

# Generated at 2022-06-13 08:54:37.410599
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    import tempfile

    def test_fail(role_content, expected_serialize):
        with tempfile.TemporaryDirectory() as temp_dir:
            with open(os.path.join(temp_dir, 'meta', 'main.yml'), 'w') as meta_main:
                meta_main.write(role_content)
            from ansible.playbook.role_block import RoleBlock
            role_block = RoleBlock.load(loader=None, path_info=temp_dir, variable_manager=None, loader_cache=None)
            assert role_block.metadata.serialize() == expected_serialize

    test_fail('', {})
    test_fail('foo: 1', {'allow_duplicates': False, 'dependencies': []})

# Generated at 2022-06-13 08:54:49.018780
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    data = {
        'allow_duplicates': False,
        'dependencies': [
            {'role':'test1'},
            {'role':'test2', 'name':'test_name'},
            {'role':'test3', 'name':'test_name', 'scenario':'test_scenario', 'version':'test_version'},
            {'role':'test4', 'name':'test_name', 'scenario':'test_scenario', 'version':'test_version', 'collections':[{'namespace':'test_namespace', 'name':'test_name'}]}
        ]
    }
    a = RoleMetadata()
    a.deserialize(data)
    print(a._allow_duplicates)
    print(a._dependencies)


# Generated at 2022-06-13 08:54:59.079465
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():

    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.play import Play
    from ansible.playbook.playbook import Playbook
    from ansible.playbook.play_context import PlayContext
    from ansible.vars import VariableManager


# Generated at 2022-06-13 08:55:10.368578
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    test_obj = RoleMetadata()

# Generated at 2022-06-13 08:55:18.996929
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():

    # Test case #1:
    # Test the code when the data variable is not a dictionary
    try:
        data = 'Test'
        owner = None
        variable_manager = None
        loader = None
        result = RoleMetadata.load(data, owner, variable_manager, loader)
        assert False
    except AnsibleParserError as e:
        print(e.message)
        assert True

    # Test case #2:
    # Test the code when the role definition is a string (old style)
    data = { 'dependencies': ['roleA', 'roleB', 'roleC'] }
    owner = "roles"
    variable_manager = None
    loader = None
    result = RoleMetadata.load(data, owner, variable_manager, loader)
    assert result is not None
    assert result.dependencies is not None

# Generated at 2022-06-13 08:55:28.644712
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    # TestRoleMetadata is a fake owner
    test_owner = RoleMetadata()
    test_owner.get_name = lambda: 'TestRoleMetadata'
    test_owner._role_path = 'role_path'
    test_owner._play = 'test_owner_play'
    test_owner._role_collection = 'test_owner_role_collection'
    test_owner.collections = ['collection1', 'collection2']
    with open("test/unit/role/meta/main.yml", "r") as f:
        data = f.read()
    data = load_data(data)
    role_metadata = RoleMetadata.load(data, test_owner)
    assert role_metadata._owner == test_owner
    assert role_metadata._allow_duplicates == False

# Generated at 2022-06-13 08:55:34.052397
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    assert RoleMetadata().serialize() == {'allow_duplicates': False, 'dependencies': []}
    assert RoleMetadata(allow_duplicates=True, dependencies=['role1', 'role2']).serialize() == {'allow_duplicates': True, 'dependencies': ['role1', 'role2']}

# Generated at 2022-06-13 08:55:39.720735
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.playbook.play import Play
    from ansible.playbook.role import Role
    from ansible.playbook.task_include import TaskInclude

    role = Role()
    play = Play()
    play.roles= [role]
    variable_manager = 'variable_manager'

    data = {'dependencies': ["test"]}
    m = RoleMetadata.load(data, role, variable_manager)
    assert isinstance(m._dependencies[0], TaskInclude)

# Generated at 2022-06-13 08:55:43.354825
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    from ansible.playbook.role.definition import RoleDefinition

    role = RoleDefinition.load({'a': 'b'}, loader='foo', variable_manager='bar')

    role_metadata = RoleMetadata(
        owner=role
    )

    serialized = role_metadata.serialize()

    assert serialized == dict(
        allow_duplicates=False,
        dependencies=[]
    )

# Generated at 2022-06-13 08:55:54.886693
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    def_data = dict(
        allow_duplicates=False,
        dependencies=[]
    )
    test = RoleMetadata.deserialize(def_data)
    if test.allow_duplicates != def_data['allow_duplicates'] or test.dependencies != def_data['dependencies']:
        raise AssertionError("Deserialization failed. Test data was: \n" + str(def_data))
    test_data = dict(
        allow_duplicates=True,
        dependencies=[
            dict(role='dependency_role_1'),
            dict(role='dependency_role_2'),
            dict(role='dependency_role_3', name='dependency_role_3a')
        ]
    )
    test = RoleMetadata.deserialize(test_data)

# Generated at 2022-06-13 08:56:14.455158
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    """
    This test case is used to verify the deserialize method
    of RoleMetadata class
    """

    role_metadata = RoleMetadata()
    role_metadata.deserialize({'allow_duplicates': True, 'dependencies': ['test']})
    assert role_metadata.allow_duplicates == True
    assert role_metadata.dependencies == ['test']



# Generated at 2022-06-13 08:56:22.783783
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from .play_context import PlayContext
    from .playbook import Playbook
    from .task import Task

    playbook_yaml_str = """
- hosts: test_host_1
  tasks:
    - name: test task
      shell: echo "hello world"
    - include_role:
        name: test_role_1
"""
    yaml_result = Playbook.load(playbook_yaml_str)
    assert len(yaml_result) == 1
    assert isinstance(yaml_result[0], PlayContext)

    play = yaml_result[0]
    assert play.hosts[0] == 'test_host_1'
    assert len(play.tasks) == 2
    assert isinstance(play.tasks[0], Task)

# Generated at 2022-06-13 08:56:33.276771
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    """
    Test RoleMetadata.load
    """

    # initialize the data
    data = dict()
    data['allow_duplicates'] = True
    data['dependencies'] = ['web', 'mysql', 'common']

    # initialize the role
    owner = dict()
    owner['get_name'] = lambda: 'test.role'
    owner['_role_path'] = '~/roles/test.role/tasks/main.yml'
    owner['collections'] = ['ansible.builtin']

    variable_manager = None
    loader = None

    # load metadata
    meta = RoleMetadata.load(data, owner, variable_manager, loader)

    # check metadata
    assert meta._allow_duplicates == data['allow_duplicates']

# Generated at 2022-06-13 08:56:41.715781
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    import collections
    import copy

    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.role.requirement import RoleRequirement
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task

    role_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', 'test', 'units', 'playbooks', 'roles', 'test_role')
    r = RoleDefinition.load(name='test_role', role_path=role_path)

    # known value to compare against

# Generated at 2022-06-13 08:56:43.842904
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    role_metadata = RoleMetadata(owner='owner')
    assert role_metadata._owner == 'owner'

# Generated at 2022-06-13 08:56:44.960145
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    RoleMetadata('mock_owner_name')

# Generated at 2022-06-13 08:56:52.875345
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():


    role_meta_data = RoleMetadata()
    role_meta_data.deserialize({"allow_duplicates": "test_data_1"})
    assert role_meta_data.allow_duplicates == "test_data_1"
    role_meta_data.deserialize({"dependencies": "test_data_2"})
    assert role_meta_data.dependencies == "test_data_2"
    # Edge case test on unknown objects
    role_meta_data.deserialize({"allow_duplicates": "test_data_1", "dependencies": "test_data_2", "test_data_3": "test_data_3"})
    assert role_meta_data.allow_duplicates == "test_data_1"

# Generated at 2022-06-13 08:56:56.221045
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    m = RoleMetadata()
    result = m.serialize()
    assert result == dict(
        allow_duplicates=False,
        dependencies=[]
    )


# Generated at 2022-06-13 08:57:08.312118
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    # simple test by loading a dictionary
    data = {'some': 'data', 'dependencies': [{'role': 'test1'}, {'role': 'test2'}]}
    fake_play = {'collections': []}
    fake_role = {'_role_path': '/some/fake/path'}
    m = RoleMetadata.load(data, fake_role, loader=None)
    assert m._data == data

    # test loading dependency
    m = RoleMetadata.load(data, fake_role, loader=None)
    assert len(m._dependencies) == 2



# Generated at 2022-06-13 08:57:12.096015
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    """Unit test for constructor of class RoleMetadata"""
    myRoleMetadata = RoleMetadata(owner=None)
    assert myRoleMetadata is not None

# Generated at 2022-06-13 08:57:43.744736
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    r = RoleMetadata()
    # test defaults
    assert r.allow_duplicates == False
    assert r.dependencies == []
    # test constructor args
    r = RoleMetadata(owner=None)
    assert r.allow_duplicates == False
    assert r.dependencies == []

# Generated at 2022-06-13 08:57:47.564611
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    rm_obj = RoleMetadata()
    data = {'allow_duplicates': False, 'dependencies': []}
    rm_obj.deserialize(data)
    assert  rm_obj.allow_duplicates == False and rm_obj.dependencies == []

# Generated at 2022-06-13 08:57:51.297098
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    data = {'allow_duplicates': False, 'dependencies': []}
    rm = RoleMetadata({})
    rm.deserialize(data)
    assert getattr(rm, 'dependencies') == []
    assert getattr(rm, 'allow_duplicates') == False


# Generated at 2022-06-13 08:57:55.945985
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block

    # Arrange
    data = dict(allow_duplicates=False, dependencies=[])
    meta = RoleMetadata(owner=RoleDefinition(name='my_role', play=None))

    # Act
    meta.deserialize(data)

    # Assert
    assert meta.allow_duplicates == False
    assert meta.dependencies == []
    assert meta._dependencies == []

# Generated at 2022-06-13 08:58:05.447576
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext

    play_context = PlayContext()
    play = Play().load(dict(
        name = "Ansible Play",
        hosts = 'webservers',
        gather_facts = 'no',
        tasks = [
            dict(action=dict(module='shell', args='ls'), register='shell_out'),
            dict(action=dict(module='debug', args=dict(msg='{{shell_out.stdout}}')))
         ]
        )
    )

    rmd = RoleMetadata()
    rmd.deserialize(dict(allow_duplicates=False, dependencies=['common', 'webtier']))
    assert rmd.allow_duplicates is False

# Generated at 2022-06-13 08:58:09.747564
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    data = {
        "allow_duplicates": True,
        "dependencies": [
            "test1", {
                "role": "test2",
                "test_var": "test_var_value"
            }
        ]
    }

    # TODO
    # A proper test of this method is needed here
    # see https://github.com/ansible/ansible/issues/41318
    assert RoleMetadata.load(data, None)

# Generated at 2022-06-13 08:58:13.502140
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    role_metadata = RoleMetadata()
    role_metadata.allow_duplicates = False
    role_metadata.dependencies = ['dependency1', 'dependency2']

    assert(role_metadata.serialize() == {'allow_duplicates': False, 'dependencies': ['dependency1', 'dependency2']})


# Generated at 2022-06-13 08:58:15.941079
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    rmd = RoleMetadata()
    d = dict()
    d['allow_duplicates'] = True
    d['dependencies'] = ['one']

    rmd.deserialize(d)
    assert rmd._allow_duplicates == True
    assert rmd._dependencies == ['one']

# Generated at 2022-06-13 08:58:21.699662
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    '''
    test_RoleMetadata_load:
    '''

    print('UNIT TEST start for: test_RoleMetadata_load')
    m = RoleMetadata(owner=None)
    m.load()
    print('UNIT TEST end for: test_RoleMetadata_load')


# Generated at 2022-06-13 08:58:25.664897
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    data = [{"src": "test", "name": "test", "version": "v1.0.0"}]
    role_metadata = RoleMetadata(owner="owner").load_data(data, variable_manager="variable_manager", loader="loader")
    assert isinstance(role_metadata, RoleMetadata)


# Generated at 2022-06-13 08:59:34.461302
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    m = RoleMetadata.load({
        'allow_duplicates': True,
        'dependencies': ['foo', 'bar'],
        'galaxy_info': {
            'author': 'test',
            'description': 'test',
            'company': 'test',
            'license': 'test',
            'min_ansible_version': '2.0',
            'platforms': [
                {
                    'name': 'Ubuntu',
                    'versions': ['12.04', '14.04']
                }
            ],
        }
    }, owner=None)
    assert m.dependencies[0].name == 'foo'
    assert m.dependencies[1].name == 'bar'
    assert m.allow_duplicates
    assert m.galaxy_info.author == 'test'

# Generated at 2022-06-13 08:59:45.031900
# Unit test for method deserialize of class RoleMetadata

# Generated at 2022-06-13 08:59:55.798269
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    # Happy path test
    import sys
    import ansible
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.role.requirement import RoleRequirement

    sys.path.insert(0, ansible.__path__[0] + '/lib/ansible/playbooks')
    from ansible.playbook.play_context import PlayContext

    data = dict(
        allow_duplicates=False,
        dependencies=["geerlingguy.java",
                      dict(role="geerlingguy.mysql",
                           when="mysql_managed",
                           tags=['galaxy', 'role'])]
    )

    rd = RoleDefinition.load(data, play=None)
    play_context = PlayContext()

# Generated at 2022-06-13 09:00:00.771957
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    deserialize_data = dict()
    deserialize_data['allow_duplicates'] = True
    deserialize_data['dependencies'] = []

    m = RoleMetadata()
    m.deserialize(deserialize_data)

    assert m._allow_duplicates == deserialize_data['allow_duplicates']
    assert m._dependencies == deserialize_data['dependencies']

# Generated at 2022-06-13 09:00:05.339862
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.collections.ansible.community.plugins.module_utils.common.collections import AnsibleCollectionLoader
    from ansible.playbook.play_context import PlayContext

    loader = AnsibleCollectionLoader()
    pc = PlayContext()
    pc.CLIARGS = dict(ignore_collection_errors=True)
    inventory = 'invalid'

    # test setting of defaults
    meta = RoleMetadata.load(dict(), None)

    assert(not meta._allow_duplicates)
    assert(len(meta._dependencies) == 0)

    # test setting of explicit values
    meta = RoleMetadata.load(dict(allow_duplicates=True), None)
    assert(meta._allow_duplicates)

# Generated at 2022-06-13 09:00:06.829434
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    role = RoleMetadata()
    assert(role.allow_duplicates() is False)
    assert(role.dependencies() == [])

# Generated at 2022-06-13 09:00:13.519799
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.role.meta import RoleMetadata

    role_def = RoleDefinition.load({'name': 'test', 'dependencies': ['foo', 'bar']}, 'test')

    met = RoleMetadata(role_def)
    met._loader = None

    data = met.serialize()
    assert type(data) == dict
    assert data['allow_duplicates'] == False
    assert type(data['dependencies']) == list
    assert len(data['dependencies']) == 2
    assert data['dependencies'][0]['name'] == 'foo'
    assert data['dependencies'][1]['name'] == 'bar'

# Generated at 2022-06-13 09:00:14.660854
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    assert isinstance(RoleMetadata(), RoleMetadata)

# Generated at 2022-06-13 09:00:15.663180
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    roledef = RoleMetadata()

# Generated at 2022-06-13 09:00:25.428584
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    # a dependency with the old style of declaring a role
    dependency = {'role': 'mycol.myrole', 'version': '1.0.0'}

    # a dependency with the new style of declaring a role
    dependency2 = {'src': 'mycol.myrole,1.0.0', 'name': 'test'}

    # test the complete version
    data = {'allow_duplicates': True, 'dependencies': [dependency, dependency2]}
    m = RoleMetadata.load(data, None, None)

    assert m.allow_duplicates == True
    assert len(m.dependencies) == 2
    assert m.dependencies[0].collection == 'mycol'
    assert m.dependencies[0].name == 'myrole'

# Generated at 2022-06-13 09:02:09.023964
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    role_metadata = RoleMetadata()
    role_metadata = RoleMetadata(owner = "test123")

