

# Generated at 2022-06-13 08:52:16.697429
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    def compare(metadata_dict, expected_galaxy_info, expected_dependencies):

        data = {'galaxy_info': metadata_dict,
                'dependencies': expected_dependencies}

        role_metadata = RoleMetadata.load(data, owner)

        assert role_metadata._galaxy_info == expected_galaxy_info
        assert role_metadata._dependencies == expected_dependencies

        return role_metadata

    role_path = 'roles/test_role/'
    role_name = 'test_role'

    owner = type('Role', (object,), dict())()
    owner._role_path = role_path
    owner._role_name = role_name
    owner._role_collection = None
    owner._task_blocks = []
    owner._role_collections = []

    # Compare if galaxy_info

# Generated at 2022-06-13 08:52:26.833527
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.role.include import RoleInclude

    role_metadata = RoleMetadata(owner=None)

    # test with empty params
    try:
        role_metadata.load({}, None)
        assert False
    except:
        assert True

    # test that it returns RoleMetadata object
    role_definition = RoleDefinition(name='test')
    result = role_metadata.load({}, role_definition)
    assert isinstance(result, RoleMetadata)

    # test that it throws error with invalid metadata
    try:
        result = role_metadata.load('hello', role_definition)
        assert False
    except:
        assert True

    # test a valid role metadata

# Generated at 2022-06-13 08:52:37.252823
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():

    from ansible.playbook.play import Play
    from ansible.playbook.role import Role
    from ansible.playbook.task import Task


# Generated at 2022-06-13 08:52:46.152757
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    class Role():
        def __init__(self):
            self._role_path = "/path/to/role"

    class GalaxyInfo():
        def __init__(self):
            self._author = "test"

    data = dict(
        allow_duplicates=True,
        dependencies=["test"]
    )

    galaxy_data = dict(
        author="test"
    )

    role_metadata = RoleMetadata()
    role_metadata._owner = Role()
    role_metadata._galaxy_info = GalaxyInfo()
    role_metadata.deserialize(data)

    assert(role_metadata.serialize() == data)

# Generated at 2022-06-13 08:52:49.699468
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    role_metadata = RoleMetadata()
    data = dict(allow_duplicates=False, dependencies=[], galaxy_info=dict(), argument_specs=dict())
    role_metadata.deserialize(data)
    assert role_metadata.allow_duplicates == False
    assert role_metadata.dependencies == []

# Generated at 2022-06-13 08:53:00.538596
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    # It's necessary to create a fake class because the class AnsiblePlaybook is not serializable
    class FakeAnsiblePlaybook(object):
        def __init__(self, metadata):
            self.metadata = metadata

    # It's necessary to create a fake class because the class GalaxyInfo is not serializable
    class FakeGalaxyInfo(object):
        def __init__(self, platforms, issues_url):
            self.platforms = platforms
            self.issues_url = issues_url

    # create an object of class RoleMetadata to test
    role_metadata = RoleMetadata()

    # set dependencies property
    role_metadata._dependencies = ['role1', 'role2', 'role3']

    # set galaxy info property
    galaxy_info = FakeGalaxyInfo(platforms='all', issues_url='ansible.com')


# Generated at 2022-06-13 08:53:04.124237
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    role = RoleMetadata()
    role.deserialize({"dependencies": [], "allow_duplicates": False})
    assert role.dependencies == []
    assert role.allow_duplicates == False

# Generated at 2022-06-13 08:53:13.411278
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    from ansible.parsing.yaml.objects import AnsibleSequence
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.role.requirement import RoleRequirement

    role = RoleDefinition.load({'name': 'test_role'})
    role.metadata = RoleMetadata(owner=role)
    role.metadata._dependencies = AnsibleSequence()

# Generated at 2022-06-13 08:53:22.464214
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    # Create a simple main.yml
    from ansible.playbook.role import Role
    from ansible.playbook.role.definition import RoleDefinition
    myRole = Role(name='myRoleName')
    assert myRole is not None
    roleDefinition = RoleDefinition()
    roleDefinition._role_name = 'myRoleName'
    myRole.definition = roleDefinition

    # Define variables for testing RoleMetadata constructor

# Generated at 2022-06-13 08:53:28.177482
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.playbook.play import Play
    from ansible.playbook.base import Base
    r = RoleMetadata()
    assert r._ds is None
    assert r._metadata is None
    data = dict()
    r = RoleMetadata.load(data = data)
    assert data == r.get_ds()

# Generated at 2022-06-13 08:53:45.157946
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    assert(RoleMetadata.load(data={"allow_duplicates": False}, owner="owner"))
    assert(RoleMetadata.load(data={"dependencies": ["foo", "bar"]}, owner="owner"))
    assert(RoleMetadata.load(data={"galaxy_info": {"author": "foo", "description": "bar"}}, owner="owner"))
    assert(RoleMetadata.load(data={"keywords": ["foo", "bar"]}, owner="owner"))
    assert(RoleMetadata.load(data={"min_ansible_version": "2.5"}, owner="owner"))
    assert(RoleMetadata.load(data={"min_ansible_version": {"foo": "2.5", "bar": "2.6"}}, owner="owner"))

# Generated at 2022-06-13 08:53:47.101833
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    # Test with valid role path
    role_metadata = RoleMetadata.load(data=dict(), owner=dict(), variable_manager=object(), loader=object())

# Generated at 2022-06-13 08:53:52.970751
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():

    import ansible.playbook.role
    import ansible.playbook.role.meta
    import ansible.playbook.play
    from ansible.playbook.play import Play
    from ansible.playbook.role.requirement import RoleRequirement

    p = Play()
    p._variable_manager = ansible.playbook.play.VariableManager()
    p._loader = ansible.playbook.play.RoleLoader()

    r = ansible.playbook.role.Role()
    r._play = p
    r._role_path = '.'

    # Test case for error handling.
    # ds is not a dictionary.
    ds = "test"

    try:
        m = RoleMetadata.load(ds, owner=r)
        assert False
    except AnsibleParserError:
        pass

    # Test

# Generated at 2022-06-13 08:54:01.545086
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.role.requirement import RoleRequirement
    # Stub AnsibleModule object
    class ModuleStub(object):
        def __init__(self):
            self.params = {}
        def fail_json(self, *args, **kwargs):
            raise AssertionError("fail_json was called unexpectedly with args: %s and kwargs: %s" % (args, kwargs))
    # Stub Role object
    class RoleStub(object):
        def __init__(self):
            self._name = "test_role"
            self._role_path = "/dev/null"
            self._role_collection = None
            self._role_definition = RoleDefinition(name="test_role")
            self._variable_manager = None


# Generated at 2022-06-13 08:54:05.647600
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    yaml_str = """
    dependencies:
    - role: galaxy.ansible.com,1.0,myrole
      other_vars: foo
    - galaxy.ansible.com,1.0,anotherrole
    """
    ds = yaml.safe_load(yaml_str)
    from ansible.playbook.role.definition import RoleDefinition
    rd = RoleDefinition.load(ds=ds, play=None, collection_list=['ansible.legacy'])
    assert len(rd.dependencies) == 2

# Generated at 2022-06-13 08:54:08.804722
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    data = {'allow_duplicates': True, 'dependencies': ['role1', 'role2']}
    result = RoleMetadata().deserialize(data)
    assert result._allow_duplicates == True
    assert result._dependencies == ['role1', 'role2']


# Generated at 2022-06-13 08:54:11.202292
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    # test constructor
    rolemetadatatest = RoleMetadata("rolem.yml")
    assert(rolemetadatatest.allow_duplicates == False)
    assert(rolemetadatatest.dependencies == [])

# Generated at 2022-06-13 08:54:13.206427
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    role_metadata = RoleMetadata()
    assert role_metadata is not None


# Generated at 2022-06-13 08:54:22.717028
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    owner = None
    data = {"dependencies": [{"role": "geerlingguy.ntp", "name": "geerlingguy.ntp", "collections": [], "scm": None, "src": None, "version": None, "use_role_def": False}], "allow_duplicates": False}
    m = RoleMetadata.load(data, owner)
    m_data = m.serialize()
    assert m_data == data
    assert m_data["allow_duplicates"] == data["allow_duplicates"]
    assert m_data["dependencies"] == data["dependencies"]


# Generated at 2022-06-13 08:54:30.370311
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.playbook.role import Role
    import ansible.constants as C
    import sys

    C.DEFAULT_ROLES_PATH = './lib/ansible/roles'

    role = Role.load('./lib/ansible/roles/test_role', None, True)

    assert isinstance(role.metadata, RoleMetadata)
    assert role.metadata.allow_duplicates == False
    assert len(role.metadata.dependencies) == 1
    assert role.metadata.dependencies[0].name == 'test_role_dependency_5'
    assert role.metadata.dependencies[0].get_path() == os.path.abspath('./lib/ansible/roles/test_role_dependency_5')

# Generated at 2022-06-13 08:54:51.869257
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    from ansible.playbook.role.definition import RoleDefinition

    x = RoleMetadata()
    data = dict(allow_duplicates=False, dependencies=[])
    x.deserialize(data)
    assert x._dependencies == []
    assert x._allow_duplicates == False

    data = dict(allow_duplicates=False, dependencies=[RoleDefinition()])
    x.deserialize(data)
    assert x._dependencies == [RoleDefinition()]
    assert x._allow_duplicates == False

    data = dict(allow_duplicates=False, dependencies=[RoleDefinition(), RoleDefinition()])
    x.deserialize(data)
    assert x._dependencies == [RoleDefinition(), RoleDefinition()]
    assert x._allow_duplicates == False


# Generated at 2022-06-13 08:54:52.933558
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    pass

# Generated at 2022-06-13 08:55:00.114590
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    import sys
    import os
    import textwrap

    # The role_dir should be a directory created so that it exists when we
    # load the role into RoleMetadata.
    role_dir = './test_RoleMetadata_load'
    if not os.path.exists(role_dir):
        os.makedirs(role_dir)

    # Create a temporary file that we can use to test with.
    from tempfile import NamedTemporaryFile
    main_yml = NamedTemporaryFile(mode='w+t', dir=role_dir, delete=False)

    main_yml.write(textwrap.dedent('''\
        ---
        dependencies:
          - role: test_dependency
            test_tag:
            - test_tag_value
    '''))
    main_yml.flush()

# Generated at 2022-06-13 08:55:11.559940
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    import ansible.playbook.role
    from ansible.playbook.role.requirement import RoleRequirement

    role_metadata_obj = RoleMetadata(owner=None)

    data = dict(
        allow_duplicates=False,
        dependencies=[]
    )
    role_metadata_obj.deserialize(data)

    # Test with minimal data

# Generated at 2022-06-13 08:55:13.240976
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    m = RoleMetadata()
    assert m.deserialize({}) is None


# Generated at 2022-06-13 08:55:19.193063
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    data = {
        'dependencies': [
            'geerlingguy.apache',
            'geerlingguy.php',
            'geerlingguy.mysql',
            {'role': 'geerlingguy.php', 'version': '1.0', 'name': 'test_name'},
            {'role': 'test-2', 'version': '1.0'},
            {'role': 'test-3'}
        ],
        'allow_duplicates': True
    }

    role = None
    variable_manager = None
    loader = None
    m = RoleMetadata.load(data, role, variable_manager, loader)

    assert m.allow_duplicates
    assert isinstance(m.dependencies, list)
    assert len(m.dependencies) == 5

# Generated at 2022-06-13 08:55:24.441223
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    from ansible.playbook.role import Role
    # Check that RoleMetadata.serialize works as expected
    r = Role()
    m = RoleMetadata()
    assert m.serialize() == {'allow_duplicates': False, 'dependencies': []}

# Generated at 2022-06-13 08:55:31.773320
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    m = RoleMetadata(owner=None)
    m.deserialize(None)
    assert m.allow_duplicates is False
    assert len(m.dependencies) == 0
    m.deserialize("")
    assert m.allow_duplicates is False
    assert len(m.dependencies) == 0
    m.deserialize("a string")
    assert m.allow_duplicates is False
    assert len(m.dependencies) == 0
    m.deserialize(3)
    assert m.allow_duplicates is False
    assert len(m.dependencies) == 0
    m.deserialize(5.5)
    assert m.allow_duplicates is False
    assert len(m.dependencies) == 0
    m.deserialize(True)
    assert m.allow

# Generated at 2022-06-13 08:55:35.711118
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    a_dict = dict(
        allow_duplicates=True,
        dependencies=[
            dict(src='michael', name='michael-role')
        ]
    )
    role_meta = RoleMetadata().load(a_dict)
    assert role_meta.serialize() == a_dict


# Generated at 2022-06-13 08:55:43.436643
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.playbook import Play
    from ansible.playbook.play import Play as CreatePlay
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.utils.display import Display
    display = Display()
    display.verbosity = 3
    role_data = dict(
        # metadata = dict(
            allow_duplicates = False,
            dependencies = [
                dict(
                    src = 'example.com',
                    name = 'test-role'
                ),
                dict(
                    src = 'test-role',
                    path = '/home/user/ansible/roles/'
                ),
            ]
        # )
    )
    role = CreatePlay().load_data(
        data=role_data,
        variable_manager={},
        loader={},
    )

# Generated at 2022-06-13 08:56:16.010226
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    # Assign
    data = dict(
        allow_duplicates=True,
        dependencies=dict(role=dict(name='test'))
    )

    # Act
    role_metadata = RoleMetadata.load(data, owner=None)
    serialized_dict = role_metadata.serialize()

    # Assert
    assert type(serialized_dict) is dict
    assert serialized_dict['allow_duplicates'] is True
    assert serialized_dict['dependencies'] is not None
    assert type(serialized_dict['dependencies']) is list
    assert serialized_dict['dependencies'] == [dict(role=dict(name='test'))]


# Generated at 2022-06-13 08:56:19.552487
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    role_meta = RoleMetadata()

    data = {'allow_duplicates': True, 'dependencies': ['test_role']}

    role_meta.deserialize(data)

    assert role_meta.allow_duplicates
    assert role_meta.dependencies == ['test_role']

# Generated at 2022-06-13 08:56:25.082623
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    '''
    This function is called to test serialize function in class RoleMetadata
    '''
    role_metadata = RoleMetadata()
    role_metadata._allow_duplicates = True
    role_metadata._dependencies = ['role1', 'role2']
    data = role_metadata.serialize()
    assert data is not None
    assert data.get('allow_duplicates') is True
    assert 'dependencies' in data
    assert len(data.get('dependencies')) == 2
    assert data.get('dependencies')[0] == 'role1'
    assert data.get('dependencies')[1] == 'role2'


# Generated at 2022-06-13 08:56:34.898948
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.playbook.role.definition import RoleDefinition

    def load_data_impl(self, ds, variable_manager=None, loader=None):
        return ds

    RoleMetadata._load_data = load_data_impl

    role_metadata = RoleMetadata()
    data = {
        'allow_duplicates': True,
        'dependencies': [
            'test.role1',
            'test.role2',
            'test.role3',
            {'role': 'test.role4'},
            {'name': 'test.role5'}
        ]
    }

    result = role_metadata.load(data, role_metadata, None, None)
    assert result['allow_duplicates'] == data['allow_duplicates']

    dependencies = result['dependencies']

# Generated at 2022-06-13 08:56:39.335590
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    r_m_d = {
        'allow_duplicates': True,
        'dependencies': [],
    }

    role_metadata = RoleMetadata()
    role_metadata.deserialize(r_m_d)

    assert getattr(role_metadata, 'allow_duplicates', None)
    assert getattr(role_metadata, 'dependencies', None)

# Generated at 2022-06-13 08:56:45.188437
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    '''
    This function is used to test the serialize function of RoleMetadata.
    '''
    role_metadata = RoleMetadata()
    role_metadata.allow_duplicates = True
    role_metadata.dependencies = ['sample']
    data = role_metadata.serialize()
    assert data == {'allow_duplicates': True, 'dependencies': ['sample']}


# Generated at 2022-06-13 08:56:53.004995
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.role_include import RoleInclude
    from ansible.playbook.role import Role
    from ansible.playbook.block import Block
    from ansible.vars.manager import VariableManager

    # Create a RoleMetadata
    rm = RoleMetadata(owner=None)
    rm.allow_duplicates = True

# Generated at 2022-06-13 08:57:01.849489
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():

    from ansible.playbook.play import Play
    from ansible.playbook.role import Role
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.handler import Handler
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.handler_task_include import HandlerTaskInclude

    class MyVarsModule():
        def get_vars(self, loader, path, entities, cache=True):
            return {'role_name': 'test_role'}

    class MyLoader():
        def __init__(self):
            pass

        def get_basedir(self, path):
            return path

        def path_dwim_relative(self, basedir, given, no_incl=False):
            return

# Generated at 2022-06-13 08:57:11.410910
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    """
    load return object RoleMetadata
    """
    from ansible.playbook.role import Role
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.play import Play
    from ansible.playbook.block import Block
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.plugins.loader import collection_loader

    loader = DataLoader()
    role_path = '../../tests/test_vars/roles/test_role_meta1'
    collection_path = '../../tests/test_collections/ansible_collections/my_namespace/ntp'

# Generated at 2022-06-13 08:57:12.329931
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    assert True

# Generated at 2022-06-13 08:57:33.284226
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    from ansible.playbook.role.definition import RoleDefinition
    from copy import copy

# Generated at 2022-06-13 08:57:38.241842
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    
    role_metadata = RoleMetadata()
    role_metadata.deserialize({"dependencies": [{"role": "common", "name": "common", "src": "../common"}]})

    assert role_metadata._dependencies[0].role == "common"

# Generated at 2022-06-13 08:57:39.370297
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    m = RoleMetadata()
    assert m is not None

# Generated at 2022-06-13 08:57:48.639695
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.role.requirement import RoleRequirement
    r = RoleDefinition.load(dict(
        name='test',
        collections=['test_collection'],
    ))
    m = RoleMetadata(r).load(dict(
        allow_duplicates=True,
        dependencies=[
            dict(role='test', version='1.1.2'),
            dict(collections=['test_collection'], name='test2'),
        ],
        galaxy_info=dict(id='foo.bar-1.1.1'),
    ))
    assert m._allow_duplicates
    assert len(m._dependencies) == 2
    assert isinstance(m._dependencies[0], RoleRequirement)

# Generated at 2022-06-13 08:57:51.189413
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    args = dict(
        allow_duplicates=False,
        dependencies=[]
    )

    rm = RoleMetadata()
    rm.deserialize(args)

    assert args == rm.serialize()

# Generated at 2022-06-13 08:57:54.950041
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    # set up test parameters
    data = dict()
    data['dependencies'] = ['geerlingguy.java', 'geerlingguy.postgresql']
    metadata = RoleMetadata()
    metadata.deserialize(data)

    # check expectations
    assert metadata._allow_duplicates is False
    assert metadata._dependencies == ['geerlingguy.java', 'geerlingguy.postgresql']

# Generated at 2022-06-13 08:57:59.418708
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    data = dict(allow_duplicates=True, dependencies=['something'])
    r = RoleMetadata()
    r.deserialize(data)

    assert r.allow_duplicates == data.get('allow_duplicates')
    assert r.dependencies == data.get('dependencies')

# Generated at 2022-06-13 08:58:07.920014
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    # Test for empty data
    data = dict()
    m = RoleMetadata().load_data(data)
    res = m.serialize()
    assert(res['allow_duplicates'] == False)
    assert(res['dependencies'] == [])

    # Test for absent items
    data = dict(author='1', dependencies=[dict(name='2', role='3')])
    m = RoleMetadata().load_data(data)
    res = m.serialize()
    assert(res['allow_duplicates'] == False)
    assert(res['dependencies'] == [dict(name='2', role='3')])

    # Test for present items
    data = dict(author='1', allow_duplicates=True, dependencies=[dict(name='2', role='3')])
    m = RoleMetadata().load

# Generated at 2022-06-13 08:58:10.590541
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    role_metadata = RoleMetadata()
    role_metadata.deserialize({'allow_duplicates': True})
    assert role_metadata.serialize() == {
        'allow_duplicates': True,
        'dependencies': []
    }


# Generated at 2022-06-13 08:58:13.411600
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    r = RoleMetadata()
    data = {
        "allow_duplicates": True,
        "dependencies": []
    }
    r.deserialize(data)
    assert r.allow_duplicates is True
    assert r.dependencies == []

# Generated at 2022-06-13 08:58:59.401149
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    name = 'my_role'
    my_role = RoleMetadata()
    my_role._owner = name
    assert isinstance(my_role._owner, str)
    assert isinstance(my_role._allow_duplicates, bool)
    assert isinstance(my_role._dependencies, list)

    # Test of load() method
    data = {'name': 'my_role'}
    assert isinstance(data, dict)
    test_data = RoleMetadata.load(data, owner=name)
    assert isinstance(test_data, RoleMetadata)

    # Test of load_data() method
    my_role_2 = RoleMetadata()
    my_role_2.load_data(data)
    assert isinstance(my_role_2, RoleMetadata)

    # Test of _load_depend

# Generated at 2022-06-13 08:59:06.951591
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.errors import AnsibleParserError
    from ansible.module_utils._text import to_bytes
    from ansible.playbook.role import Role
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.template import Templar

    # Testing the parsing of a role metadata
    sample_role_metadata = '''
---
dependencies:
  - role1
  - role2
  - { role: role3, some_var: "some_value" }
allow_duplicates: yes
'''

    # Create a Role object to pass to the RoleMetadata.load function
    pb = Role()
    pb.name = 'test_role'
    pb.main_file_path = 'test_role/meta/main.yml'
    pb.role_path = os.path

# Generated at 2022-06-13 08:59:09.520913
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    ''' unit tests for RoleMetadata.deserialize '''
    rm = RoleMetadata()
    role_data = {}

    rm.deserialize(role_data)
    assert rm.allow_duplicates == False
    assert rm.dependencies == []


# Generated at 2022-06-13 08:59:14.650572
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    # Create test fixture
    role_metadata = RoleMetadata(owner=None)
    role_metadata.allow_duplicates=True
    role_metadata_test = RoleMetadata(owner=None)
    role_metadata_test.allow_duplicates=False
    # Perform the test
    serialize_result_test=role_metadata_test.serialize()
    assert (role_metadata.serialize() == {'allow_duplicates': True, 'dependencies': []})
    assert (serialize_result_test == {'allow_duplicates': False, 'dependencies': []})


# Generated at 2022-06-13 08:59:18.301189
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    a = RoleMetadata()
    assert not a.allow_duplicates
    assert not a.dependencies
    assert not a.galaxy_info

# Generated at 2022-06-13 08:59:25.688397
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    result_metadata={
        'allow_duplicates': False,
        'dependencies': [{'role': 'role1'}]
    }
    role_metadata=RoleMetadata()
    role_metadata.deserialize(result_metadata)
    assert(role_metadata.serialize() == result_metadata)

# Generated at 2022-06-13 08:59:33.142916
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    from ansible.playbook.role import Role
    role = Role()
    role._role_path = "/tmp"
    ds = dict(dependencies=dict(role_a=dict(role="role_a"),
                                role_b=dict(role="role_b")))

    rm = RoleMetadata(owner=role)
    print(rm)
    rm.load_data(ds)
    print(rm)
    print(rm.serialize())
    print(rm.deserialize(rm.serialize()))
    print(rm.serialize())

    # unit test for _load_dependencies

# Generated at 2022-06-13 08:59:43.218437
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():

    from ansible.playbook.role.metadata import RoleMetadata
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.play_context import PlayContext

    my_play_context = PlayContext()
    my_play_context._play = mock.Mock()


    # test role meta/main.yml file not a dict
    fake_data1 = "This is a fake role meta/main.yml file, which is not a dict"
    fake_data2 = "---\n- host: all\n\tremote_user: root\n\ttasks:\n\t\t- debug: var=hostvars[inventory_hostname]"

# Generated at 2022-06-13 08:59:50.447806
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    from ansible.playbook.role.definition import RoleDefinition
    data = dict(
        allow_duplicates=False,
        dependencies=[
          {'role': 'geerlingguy.redis'},
          {'role': 'geerlingguy.apache2'},
        ],
    )
    owner = RoleDefinition()
    role_metadata = RoleMetadata(owner)
    role_metadata.deserialize(data)
    role_metadata.deserialize = RoleMetadata.deserialize

# Generated at 2022-06-13 08:59:59.240911
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    #This method serialize needs a object of RoleMetadata.
    #So we need to create a object of RoleMetadata.
    #This RoleMetadata object is created by passing the data role_data,
    #from unit test "test_validate_metadata_from_main()" in file test/unit/playbook/test_playbook.py
    role_data = dict(
        allow_duplicates=True,
        dependencies=List(),
    )
    m = RoleMetadata(owner=None).load_data(role_data)
    try:
        assert m.serialize() is not None
    except AssertionError:
        print(m.serialize())
        raise

# Generated at 2022-06-13 09:00:57.325720
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    class MockRole(object):
        def __init__(self, name, **kwargs):
            self.name = name
            for k,v in kwargs.items():
                setattr(self, k, v)

    m = RoleMetadata()
    m.deserialize(
        dict(
            allow_duplicates=True,
            dependencies=
                [dict(
                    role='foo',
                    version='1.0.1'
                ),
                dict(
                    role='bar',
                    version='2.0.1'
                )
                ]
        )
    )

    # make sure we get the correct dependencies back
    assert type(m.dependencies) == list
    assert len(m.dependencies) == 2

    assert type(m.dependencies[0]) == MockRole
    assert m.depend

# Generated at 2022-06-13 09:01:02.035266
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task

    p = Play.load({'name': 'test', 'hosts': ['testhost'], 'roles': []})
    t = Task.load({'name': 'test', 'action': {'module': 'test'}})

    assert t._role is None

    rm = RoleMetadata(owner=t)

    assert rm._owner == t
    assert t._role == rm

# Generated at 2022-06-13 09:01:02.916066
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    new_RoleMetadata = RoleMetadata()

# Generated at 2022-06-13 09:01:05.308230
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    RoleMetadata.load(data=dict(), owner=[], variable_manager=dict())

# Generated at 2022-06-13 09:01:17.471536
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    '''
    Test the RoleMetaData class deserialize method when loading a
    dictionary that has the allow_duplicates field set to true and
    the dependency field set to a list of role dependencies
    '''
    datastruct = {'allow_duplicates': True, 'dependencies': ['role1', 'role2']}
    rmd = RoleMetadata()
    rmd.deserialize(datastruct)

    assert rmd._allow_duplicates is True
    assert rmd._dependencies == ['role1', 'role2']


# Generated at 2022-06-13 09:01:23.470456
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    role_metadata = RoleMetadata()
    data = {'allow_duplicates': True,
            'dependencies': [1, 2, 3]}
    role_metadata.deserialize(data)
    assert role_metadata.serialize() == data


# Generated at 2022-06-13 09:01:26.376299
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    role_path = os.path.join(os.getcwd(), '../../lib/ansible/playbook/role')
    role_metadata = RoleMetada

# Generated at 2022-06-13 09:01:40.178579
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():

    class SimpleOwner(object):
        def __init__(self, role_path, role_collection=None, collections=None):
            self._role_path = role_path
            self._role_collection = role_collection
            self._play = None
            self.collections = collections or []

    # test dict
    dict_input = dict(
        allow_duplicates=True,
        dependencies=[],
        galaxy_info=None
    )

    # init
    owner = SimpleOwner(role_path="/home/test/roles/test1")
    role_metadata_1 = RoleMetadata.load(dict_input, owner)

    assert role_metadata_1.allow_duplicates
    assert role_metadata_1.dependencies == []
    assert role_metadata_1.galaxy_info is None
    assert role_

# Generated at 2022-06-13 09:01:40.994761
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    pass

# Generated at 2022-06-13 09:01:48.164275
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    # Define role path location to test that it is correctly set
    role_path = "./tests/integration/roles/test_role"

    # Load tests/integration/roles/test_role/meta/main.yml
    metadata = RoleMetadata.load(
        data={
            "allow_duplicates": False,
            "dependencies": ['geerlingguy.apache', 'geerlingguy.php']
        },
        owner=role_path
    )

    # Make sure that metadata is loaded correctly from meta/main.yml
    assert metadata.allow_duplicates == False
    assert len(metadata.dependencies) == 2