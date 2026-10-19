

# Generated at 2022-06-13 08:52:15.067907
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    loader = Mock()
    play = Mock()
    play._play = True
    role_meta = RoleMetadata(owner=play)
    role_meta.deserialize({'allow_duplicates': True, 'dependencies': []})
    assert role_meta._allow_duplicates is True
    assert role_meta._dependencies == []


# Generated at 2022-06-13 08:52:24.698732
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    role_metadata_obj = RoleMetadata()
    role_metadata_obj._allow_duplicates = False
    role_metadata_obj._dependencies = []
    role_metadata_obj_serialized = role_metadata_obj.serialize()
    assert isinstance(role_metadata_obj_serialized, dict)
    assert 'allow_duplicates' in role_metadata_obj_serialized
    assert 'dependencies' in role_metadata_obj_serialized
    assert role_metadata_obj_serialized['allow_duplicates'] == False
    assert role_metadata_obj_serialized['dependencies'] == []



# Generated at 2022-06-13 08:52:33.909537
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    test_role_path = "/Users/yuexiao.jiang/Documents/git-repo/automation-ansible/hd_example_roles/test_role"
    m = RoleMetadata(test_role_path)
    assert isinstance(m, RoleMetadata)
    assert m._ignore_errors is False
    assert m._owner == test_role_path
    assert m._variable_manager == None
    assert m._loader == None
    assert m._ds == None
    assert m._vars == None
    assert m._task_blocks == None
    assert m._role_blocks == None


# Generated at 2022-06-13 08:52:45.798016
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    # Instantiate a FakeGalaxyInfo object
    import sys
    import io
    import yaml
    fake = io.StringIO()

# Generated at 2022-06-13 08:52:48.492273
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    from ansible.playbook.role import Role

    role = Role()
    rm = RoleMetadata(owner=role)
    assert rm.allow_duplicates == False
    assert rm.dependencies == []

# Generated at 2022-06-13 08:52:54.390702
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    data = dict(
        allow_duplicates=False,
        dependencies=['role1']
    )
    role_metadata = RoleMetadata()
    role_metadata.deserialize(data)
    assert role_metadata._allow_duplicates == False
    assert role_metadata._dependencies == ['role1']

# Generated at 2022-06-13 08:52:58.180638
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    r = RoleMetadata()
    data = dict(
        allow_duplicates=True,
        dependencies=[]
    )
    r.deserialize(data)
    assert r.allow_duplicates == True
    assert r.dependencies == []

# Generated at 2022-06-13 08:53:01.294526
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    role_metadata = RoleMetadata()
    role_data = {'allow_duplicates': False, 'dependencies': []}
    assert (role_metadata.deserialize(role_data) == None)

# Generated at 2022-06-13 08:53:04.449035
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    # create a RoleMetadata object
    empty_role_metadata = RoleMetadata()
    assert empty_role_metadata.serialize() == {'allow_duplicates': False, 'dependencies': []}


# Generated at 2022-06-13 08:53:05.408083
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    RoleMetadata()
    assert True

# Generated at 2022-06-13 08:53:20.992356
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    class A:
        def get_name(self):
            return "test_name"

    r = RoleMetadata(owner=A())
    assert r._dependencies == [], "dependencies should be empty list"
    assert r._allow_duplicates == False, "allow_duplicates should be false"

    data = dict(
        allow_duplicates=True,
        dependencies=["galaxy.role", "galaxy.role2"]
    )

    r.deserialize(data)
    assert r._dependencies == ["galaxy.role", "galaxy.role2"], "dependencies should be filled"
    assert r._allow_duplicates == True, "allow_duplicates should be true"

# Generated at 2022-06-13 08:53:25.577692
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    data = dict(
        allow_duplicates=False,
        dependencies=None
    )

    metadata = RoleMetadata()
    metadata.deserialize(data)
    result = metadata.serialize()
    assert result == data

# Generated at 2022-06-13 08:53:34.245134
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    from ansible.playbook.role.meta import RoleMetadata
    import types
    import sys

    sys.modules['ansible'] = types.ModuleType('ansible')
    sys.modules['ansible.playbook'] = types.ModuleType('ansible.playbook')
    sys.modules['ansible.playbook.role'] = types.ModuleType('ansible.playbook.role')
    sys.modules['ansible.playbook.role.meta'] = types.ModuleType('ansible.playbook.role.meta')
    sys.modules['ansible.playbook.role.meta'].RoleMetadata = RoleMetadata

    data = dict(allow_duplicates=True, dependencies=[])

    rolemetadata = RoleMetadata()
    rolemetadata.deserialize(data)

    assert rolemetadata._allow_duplicates == True

# Generated at 2022-06-13 08:53:38.942318
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    from ansible.playbook import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block

    play_context = PlayContext()
    play_source = dict(
        name = "Ansible Play",
        hosts = 'webservers',
        vars = dict(
            var1 = "this is a variable",
            var2 = "this is another variable",
        ),
        roles = [
        ],
    )
    play = Play().load(play_source, variable_manager=play_context.variable_manager, loader=play_context.loader)

# Generated at 2022-06-13 08:53:48.971613
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    test_data = {
        'allow_duplicates': True,
        'dependencies': [
             "role1",
             "role2",
             {'name': "role3", 'version': "master"},
             {'name': "role4", 'src': "https://www.example.com/role-4.tar.gz"}
        ]
    }
    rm = RoleMetadata.load(test_data, owner=None)
    assert rm._allow_duplicates is True
    assert len(rm._dependencies) == 4
    assert rm._dependencies[0] == "role1"
    assert rm._dependencies[1] == "role2"
    assert rm._dependencies[2] == {'name': "role3", 'version': "master"}

# Generated at 2022-06-13 08:53:59.334463
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.role.requirement import RoleRequirement
    from ansible.playbook.role.include import RoleInclude

    test_role_md = RoleMetadata()
    assert test_role_md._allow_duplicates is False
    assert test_role_md._dependencies == []
    assert test_role_md._galaxy_info is None
    assert test_role_md._argument_specs == dict()
    assert test_role_md._loader is None
    assert test_role_md._variable_manager is None
    assert test_role_md._owner is None

    # Test _load_dependencies() with a simple string requirement

# Generated at 2022-06-13 08:54:00.814215
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    testMeta = RoleMetadata()
    assert testMeta.allow_duplicates == False

# Generated at 2022-06-13 08:54:08.932344
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.playbook.play_context import PlayContext

    data = dict(
        allow_duplicates=True,
        dependencies=[
            {
                'role': 'mysql',
                'version': '1.0',
                'name': 'foo'  # this should be ignored
            },
            dict(role='xyz'),
            dict(src='https://example.com/repo/roles/foo')
        ],
        argument_specs={
            'foo': dict(type='str', default='bar')
        }
    )

    pm = RoleMetadata()
    pm.load_data(data)

    assert pm.allow_duplicates is True
    assert len(pm.dependencies) == 3

    loader, inventory, variable_manager = (None, None, None)
    pm.post_valid

# Generated at 2022-06-13 08:54:14.538136
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.playbook import Play
    from ansible.playbook.role.metadata import RoleMetadata
    from ansible.playbook.role.definition import RoleDefinition

    class BaseRoleDefinition(Base, RoleDefinition):
        _role_path = FieldAttribute(isa='string', default='', required=True)

        def __init__(self, role_name, data=None, parent_role=None, role_path=None, collection_names=None, collection_search_list=None):
            super(BaseRoleDefinition, self).__init__()
            self._role_name = role_name
            self._role_path = role_path
            self._role_collection = None
            self._role_collections = []
            self._collections = collection_search_list
            self._collection_names = collection_names or []
            self

# Generated at 2022-06-13 08:54:15.187952
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    assert RoleMetadata()

# Generated at 2022-06-13 08:54:22.480411
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    # Test all the parameters
    assert RoleMetadata()
    assert RoleMetadata().load_data({'allow_duplicates': 'True', 'dependencies': {'name': 'apache', 'src': 'foo/bar'}})

# Generated at 2022-06-13 08:54:27.878624
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    data = {"allow_duplicates": True,
            "dependencies": ["role1", "role2"]}
    role_metadata = RoleMetadata()
    role_metadata.deserialize(data)
    assert(role_metadata.allow_duplicates)
    assert(len(role_metadata.dependencies) == 2)
    first_role = role_metadata.dependencies[0]
    assert(first_role.role == "role1")
    assert(first_role.collections == [])


# Generated at 2022-06-13 08:54:34.288139
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():

    from ansible.playbook.role_include import RoleInclude

    data = {
        # galaxy_info is no longer used - ensure we don't break if it shows up in a
        # meta/main.yml
        'galaxy_info': 'junk',
        # allow_duplicates is no longer used - ensure we don't break if it shows up in a
        # meta/main.yml
        'allow_duplicates': 'junk',
        'dependencies': [
            {'role': 'test.dependency'},
            {'role': 'test.dependency2'},
        ]
    }

    m = RoleMetadata(owner='role').load(data, variable_manager=None, loader=None)
    assert m.dependencies[0].role == 'test.dependency'
    assert m.depend

# Generated at 2022-06-13 08:54:38.996373
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    from ansible.playbook.role.requirement import RoleRequirement
    from ansible.module_utils.six import BytesIO
    res1 = b'---\ndependencies:\n- src: ../roles/test/\n'

    test_info = {'dependencies': [RoleRequirement("../roles/test/")]}
    test_parser = RoleMetadata()

    test_parser.deserialize(test_info)
    io = BytesIO()
    test_parser.serialize(io=io)

    assert res1 == io.getvalue()

# Generated at 2022-06-13 08:54:44.869265
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    role_metadata = RoleMetadata()
    data = dict(
        allow_duplicates=True,
        dependencies=["other-role-1"],
    )
    role_metadata.deserialize(data)
    assert role_metadata.allow_duplicates == True
    assert role_metadata.dependencies == ["other-role-1"]


# Generated at 2022-06-13 08:54:48.848767
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    role = RoleMetadata()
    role._allow_duplicates = True
    role._dependencies = ['foo', 'bar']
    assert {'allow_duplicates': True, 'dependencies': ['foo', 'bar']} == role.serialize()



# Generated at 2022-06-13 08:54:51.732647
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    data = {
        'allow_duplicates': True,
        'dependencies': [],
    }
    metadata = RoleMetadata()
    metadata.deserialize(data)

    assert metadata._allow_duplicates == True
    assert metadata._dependencies == []

# Generated at 2022-06-13 08:54:57.915101
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    class MockRoleMetadata():
        def __init__(self, _allow_duplicates, _dependencies):
            self._allow_duplicates = _allow_duplicates
            self._dependencies = _dependencies

    test_input = {'allow_duplicates': True, 'dependencies': ["test_role1", "test_role2"]}
    test_output = MockRoleMetadata(True, ["test_role1", "test_role2"])
    assert RoleMetadata.deserialize(test_input) == test_output

# Generated at 2022-06-13 08:55:03.711778
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    my_role = RoleMetadata()
    my_role_data = {
        'allow_duplicates': True,
        'dependencies': ['test1', 'test2']
    }
    my_role.load(my_role_data)

    assert my_role.allow_duplicates == True
    assert my_role.dependencies == ['test1', 'test2']



# Generated at 2022-06-13 08:55:08.333428
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    meta = RoleMetadata()
    meta_data = dict(
        allow_duplicates=True,
        dependencies=['common','webserver'])
    meta.deserialize(meta_data)
    assert meta.allow_duplicates
    assert meta.dependencies == ['common','webserver']

# Generated at 2022-06-13 08:55:19.027338
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    roleMetadata_obj = RoleMetadata()
    assert roleMetadata_obj


if __name__ == "__main__":
    test_RoleMetadata()

# Generated at 2022-06-13 08:55:26.277870
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():

    class Role:
        def __init__(self, name):
            self._name = name

        def get_name(self):
            return self._name

    rmt = RoleMetadata()
    rmt._owner = Role('meta_unittest')
    rmt.deserialize({'allow_duplicates': False, 'dependencies': []})
    assert rmt.allow_duplicates == False
    assert rmt.dependencies == []

# Generated at 2022-06-13 08:55:27.550126
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    role = RoleMetadata()
    assert role.dependencies == []

# Generated at 2022-06-13 08:55:35.226816
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    owner = type('',(),{})
    owner.get_name = lambda: 'test_role'
    owner._role_path = './'

    r = RoleMetadata(owner=owner)
    assert r.serialize() == {'allow_duplicates': False, 'dependencies': []}

    r.allow_duplicates = True
    r.dependencies = ['foo', 'bar']
    assert r.serialize() == {'allow_duplicates': True, 'dependencies': ['foo', 'bar']}


# Generated at 2022-06-13 08:55:43.101163
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.role.requirement import RoleRequirement
    from ansible.playbook.play_context import PlayContext

    role_path = '/home/dennyzhang/github/ansible-playbook/myroles/myrole'
    var_manager = VariableManager()
    var_manager.extra_vars = load_extra_vars(loader=None, options=None, passed_args=None)

    myroles = RoleMetadata()
    # role_name = RoleDefinition(None, role_path, role_path, False, False, None, None).get_name()
    # myroles._owner = RoleRequirement(role_name, role_name)
    # myroles._variable_manager = var_manager
    # myroles

# Generated at 2022-06-13 08:55:54.515069
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    from ansible.playbook.role_include import RoleInclude
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.play import Play

    metadata = {
        'allow_duplicates': True,
        'dependencies': [{
            'role': 'some-role',
            'name': 'some-role',
            'scm': None,
            'src': '/some/path/some-role',
            'version': None,
            'path': 'meta/main.yml',
        }]
    }

    role_metadata = RoleMetadata().load(metadata, None)
    serialized_data = role_metadata.serialize()
    assert 'dependencies' in serialized_data

# Generated at 2022-06-13 08:55:57.370878
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    my_role = RoleMetadata()
    assert my_role._allow_duplicates == False
    assert my_role._dependencies == []

# Generated at 2022-06-13 08:56:04.150833
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    role_name = "test"
    role_path = "/Users/admin/Ansible/ansible/playbooks/roles/"
    play = "playbook"
    metadata = dict()

    owner = None
    r = RoleMetadata(owner)
    assert owner == r._owner

# Generated at 2022-06-13 08:56:11.751303
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    metadata_content= {'allow_duplicates': True, 'dependencies': ['role1', 'role2']}
    role_metadata = RoleMetadata.load(metadata_content, None)
    assert role_metadata is not None
    assert role_metadata.allow_duplicates is True
    assert role_metadata.dependencies is not None
    assert len(role_metadata.dependencies) == 2

# Generated at 2022-06-13 08:56:16.223741
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    data = dict()
    data['allow_duplicates'] = True
    data['dependencies'] = ["role1", "role2"]

    role_metadata = RoleMetadata()
    role_metadata.deserialize(data)

    assert role_metadata.allow_duplicates == True
    assert role_metadata.dependencies == ["role1", "role2"]

# Generated at 2022-06-13 08:56:31.386130
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.role import Role

    role_data = dict(
        name='test_role',
        tasks=dict(
            main=dict(
                block=dict(
                    tasks=[dict(action=dict(module='test'))]
                )
            )
        ),
        meta=dict(
            dependencies=['test_role1'],
        )
    )

    role = Role.load(role_data)
    assert role.get_dependencies()[0].get_name() == 'test_role1'

# Generated at 2022-06-13 08:56:35.007696
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    data = {'dependencies': [{'role': 'web-server'}, {'role': 'other-role', 'become':True}]}
    role_metadata = RoleMetadata()
    role_metadata.deserialize(data)
    assert role_metadata.dependencies == data['dependencies']

# Generated at 2022-06-13 08:56:39.779920
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    role_metadata = RoleMetadata()
    setattr(role_metadata, 'dependencies', "dependencies")
    setattr(role_metadata, 'allow_duplicates', "allow_duplicates")
    serialize = role_metadata.serialize()
    assert serialize['dependencies'] == "dependencies"
    assert serialize['allow_duplicates'] == "allow_duplicates"


# Generated at 2022-06-13 08:56:45.186674
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    from ansible.playbook.role.definition import RoleDefinition
    variable_manager = DummyVariableManager()
    loader = DummyLoader()
    obj = RoleMetadata(owner=RoleDefinition.load(data={'name': 'myrole'}, variable_manager=variable_manager, loader=loader))
    obj.load_data({}, variable_manager=variable_manager, loader=loader)

# Generated at 2022-06-13 08:56:53.005563
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():

    class TestRole(object):
        '''
        This is fake class to mimic a role class. If the role metadata is empty or deny_duplicates exists, allow_duplicates is False. If deny_duplicates does not exist, allow_duplicates is True.
        The TestRole should have two attributes, _metadata and allow_duplicates.
        The _metadat should be an instance of class RoleMetadata.
        '''

        def __init__(self, metadata):
            self._metadata = RoleMetadata(owner=self)
            self._metadata.deserialize(metadata)

    role = TestRole(metadata={'deny_duplicates': {}, 'dependencies': []})
    assert role.allow_duplicates == False

    role = TestRole(metadata={'dependencies': []})
    assert role.allow_

# Generated at 2022-06-13 08:57:04.544356
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():

    # The fixture for creating the test RoleMetadata object
    fixture = dict(
        allow_duplicates=False,
        dependencies=['dependency1', 'dependency2']
    )

    # The example output of the serialize method
    output = dict(
        allow_duplicates=False,
        dependencies=['dependency1', 'dependency2']
    )

    # Create the test object
    m = RoleMetadata()
    m.deserialize(fixture)

    # Check the output
    assert m.serialize() == output

# Generated at 2022-06-13 08:57:06.736132
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
  data = dict(
    allow_duplicates=False,
    dependencies=[]
  )
  RoleMetadata.deserialize(data)

# Generated at 2022-06-13 08:57:17.244329
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    # pylint: disable=too-many-locals
    """ test RoleMetadata.load """

    import data.tst_metadata.meta as test_meta

    from ansible.errors import AnsibleParserError

    from ansible.playbook import Playbook
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.block import Block
    from ansible.playbook.play_context import PlayContext

    from ansible.utils.collection_loader import AnsibleCollectionRef
    from ansible.utils.collection_loader._collection_finder import AnsibleCollectionFinder
    from ansible.utils.display import Display
    from ansible.utils.plugin_docs import read_docstring
    from ansible.utils.vars import combine_vars

    #

# Generated at 2022-06-13 08:57:20.934593
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    assert RoleMetadata(owner=None).deserialize({'allow_duplicates': False, 'dependencies': []}) is not None

# Generated at 2022-06-13 08:57:27.264093
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    role_metadata = RoleMetadata()
    role_metadata._allow_duplicates = True

# Generated at 2022-06-13 08:57:36.828515
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.playbook.role.definition import RoleDefinition
    RoleMetadata.load(dict(dependencies=list()), RoleDefinition())

# Unit test function

# Generated at 2022-06-13 08:57:37.696315
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    pass

# Generated at 2022-06-13 08:57:43.746198
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    data = {
        'authors': ['bob'],
        'dependencies': ['roles/alpha', 'roles/beta', 'roles/gamma'],
        'platforms': ['linux'],
        'galaxy_info': {
            'author': 'bob',
            'description': 'hello'
        }
    }

    c = RoleMetadata()

# Generated at 2022-06-13 08:57:51.666883
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    from ansible.playbook.block import Block
    from ansible.playbook.play import Play
    from ansible.playbook.role import Role
    from ansible.playbook.task import Task
    from ansible.playbook.tests.unit.test_play import TestPlay

    myblock = Block()
    myblock.block = [ Task() ]
    myplay = Play().load(
        dict(
            name = "myplay",
            hosts = 'localhost',
            gather_facts = 'no',
            roles = [ "testrole" ],
            tasks = [
                dict(action=dict(module='setup', args=dict())),
                dict(action=dict(module='debug', args=dict(msg='{{foo}}'))),
            ]
        )
    )
    myplay.post_validate()

    my

# Generated at 2022-06-13 08:57:52.197048
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    pass

# Generated at 2022-06-13 08:57:55.279284
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    roleMetadata = RoleMetadata()
    roleMetadata.deserialize(dict(allow_duplicates=False, dependencies=['common', 'webservers']))
    assert roleMetadata.allow_duplicates is False
    assert roleMetadata.dependencies == ['common', 'webservers']


# Generated at 2022-06-13 08:57:56.204913
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    RoleMetadata.load({}, [])
    assert True

# Generated at 2022-06-13 08:57:56.763957
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    pass

# Generated at 2022-06-13 08:58:01.523227
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    obj = RoleMetadata()
    obj.allow_duplicates = False
    obj.dependencies = ['role1', 'role2']
    expected_dict = {
        'allow_duplicates': False,
        'dependencies': ['role1', 'role2']
    }
    assert obj.serialize() == expected_dict

# Generated at 2022-06-13 08:58:05.998551
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.role.requirement import RoleRequirement

    role_defs = RoleMetadata.load({ 'dependencies': [ 'foo', { 'role': 'bar', 'src': 'geerlingguy.foo' } ] }, owner=RoleDefinition())
    assert isinstance(role_defs[0], RoleRequirement)


# Generated at 2022-06-13 08:58:15.093428
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    data = {
        "dependencies": [
            "other.rolename",
            "another.rolename",
            "yet-another.role"
        ]
    }
    role = RoleMetadata(owner=None).load(data, owner=None)
    assert role._dependencies[0]['role'] == 'other.rolename'

# Generated at 2022-06-13 08:58:19.673687
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    data = {
        'allow_duplicates': False,
        'dependencies': []
    }
    target = RoleMetadata(owner=None)
    target.deserialize(data)
    assert target.serialize() == data

# Generated at 2022-06-13 08:58:28.908158
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.playbook.play import Play
    from ansible.playbook.role import Role
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.executor.task_queue_manager import TaskQueueManager

    # Mock in the play object
    # TODO: some of this mocking might be better or possible using
    # the @patch decorator.  However, I'm not clear on how I would
    # do this for the nested task_queue_manager

    play = Play().load({
        'hosts': 'localhost',
        'tasks': [
            {'action': {'module': 'debug', 'args': {'msg': 'test role metadata'}}}
        ]})
    play._variable_manager = None

# Generated at 2022-06-13 08:58:34.266443
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    role_meta = RoleMetadata(None)
    assert role_meta.dependencies == []
    assert role_meta.allow_duplicates == False
    assert role_meta.galaxy_info == None
    assert role_meta.argument_specs == {}

# Generated at 2022-06-13 08:58:36.631746
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    m = RoleMetadata()

    data = dict(
        allow_duplicates=False,
        dependencies=[]
    )

    assert m.serialize() == data


# Generated at 2022-06-13 08:58:43.925807
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    variables = dict()
    variable_manager = VariableManager(loader=None, variables=variables)
    file = '../resources/playbooks/playbooks/play_test.yml'
    playbook = Playbook.load(file, variable_manager=variable_manager, loader=None)
    assert playbook.get_plays()[0]._role_name == 'test_role'
    assert playbook.get_plays()[1]._role_name == 'test_role'
    assert playbook.get_plays()[0]._role_path is not None
    assert playbook.get_plays()[1]._role_path is not None
    assert playbook.get_plays()[1]._role_path != playbook.get_plays()[0]._role_path

    # test deserializing
    role_meta = RoleMetadata()
    role

# Generated at 2022-06-13 08:58:50.396763
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    # Raw data
    data = dict(
        allow_duplicates=False,
        dependencies=[{'name': 'your-organization.your-role', 'version': 'dev'}]
        )
    rolemetadata = RoleMetadata()
    rolemetadata.deserialize(data)

    # Validation
    assert not rolemetadata.allow_duplicates
    assert len(rolemetadata.dependencies) == 1
    assert rolemetadata.dependencies[0].role == 'your-organization.your-role'
    assert rolemetadata.dependencies[0].version == 'dev'

# Generated at 2022-06-13 08:58:51.573999
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    r = RoleMetadata()
    d = r.serialize()
    assert 'allow_duplicates' in d
    assert 'dependencies' in d

# Generated at 2022-06-13 08:58:55.389465
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    role_metadata_object = RoleMetadata()
    role_metadata_object.allow_duplicates = False
    role_metadata_object.dependencies = []
    assert not role_metadata_object.allow_duplicates
    assert not role_metadata_object.dependencies

# Generated at 2022-06-13 08:58:57.454932
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    '''
    This function tests the serialize method.
    It needs to be improved to include a test with a valid datastructure.
    '''
    pass

# Generated at 2022-06-13 08:59:15.782044
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    # For testing purposes, we use a static method load, which is used to assign
    # the owner of this instance
    class object:
        pass
    fakeOwner = object()
    data = dict(
        allow_duplicates=True,
        dependencies=[
            {
                'role': 'roleA',
                'name': 'path/to/role'
            },
            {
                'role': 'roleB',
                'name': 'path/to/role'
            }
        ]
    )
    RoleMetadata.load = staticmethod(RoleMetadata.load)
    m = RoleMetadata.load(data, fakeOwner)

    m.deserialize(data)
    assert m.allow_duplicates == data['allow_duplicates']
    assert m.dependencies == data['dependencies']

# Generated at 2022-06-13 08:59:33.354719
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    from ansible.playbook.play import Play
    import yaml

    yaml_str="""
    allow_duplicates: False
    dependencies:
    - src: git+https://github.com/geerlingguy/ansible-role-firewall.git
      version: "1.1.0"
    - role: testrole
    """
    yaml_data = yaml.safe_load(yaml_str)
    p = Play().load(yaml_data)
    assert(p.allow_duplicates == False)
    assert(len(p.dependencies) == 2)
    assert(p.dependencies[0].get_info()['name'] == 'src')
    assert(p.dependencies[1].get_info()['role'] == 'testrole')

# Generated at 2022-06-13 08:59:39.518586
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():

    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.playbook.role import Role

    loader = None

    play = Play.load({}, loader=loader, variable_manager=None)

    context = PlayContext()

    arg_spec = {
        'src': dict(required=True, aliases=['name']),
        'version': dict(),
        'scm': dict(),
        'path': dict(),
        'private': dict(default=False, type='bool'),
    }


# Generated at 2022-06-13 08:59:50.578004
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    # pylint: disable=line-too-long, protected-access
    # Test enabled / disabled
    assert RoleMetadata.load({}, None)._allow_duplicates is False
    assert RoleMetadata.load({}, None)._dependencies == []
    assert RoleMetadata.load({'allow_duplicates': True}, None)._allow_duplicates is True
    assert RoleMetadata.load({'allow_duplicates': 1}, None)._allow_duplicates is True

    # Test dependencies
    assert RoleMetadata.load({'dependencies': [{'role': 'foo'}]}, None)._dependencies[0].get_name() == 'foo'
    assert RoleMetadata.load({'dependencies': ['foo']}, None)._dependencies[0].get_name() == 'foo'
    assert Role

# Generated at 2022-06-13 08:59:55.594901
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    data = dict(
        allow_duplicates=False,
        dependencies=[]
    )
    role_meta = RoleMetadata()
    role_meta.deserialize(data)
    assert role_meta.allow_duplicates == data['allow_duplicates']
    assert role_meta.dependencies == data['dependencies']

# Generated at 2022-06-13 08:59:57.926527
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    meta = RoleMetadata()
    result = meta.serialize()
    assert result == {
        'allow_duplicates': False,
        'dependencies': []
    }

# Generated at 2022-06-13 09:00:00.649749
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    role_meta = RoleMetadata(owner='test')
    role_meta.serialize()
    assert role_meta.serialize() == {'allow_duplicates': False, 'dependencies': []}

# Generated at 2022-06-13 09:00:05.274049
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    ''' Unit test of method deserialize of class RoleMetadata '''
    # Instantiate an empty RoleMetadata object
    role_metadata = RoleMetadata()
    # Serialize it
    data = role_metadata.serialize()
    # Assert that it is the expected serialization
    assert data == {
        'allow_duplicates': False,
        'dependencies': []
    }
    # Deserialize it
    role_metadata.deserialize(data)
    # Assert that it is the expected deserialized copy
    assert data == role_metadata.serialize()
    # Serialize and deserialize the expected serialized data
    new_role_metadata = RoleMetadata()
    new_role_metadata.deserialize(RoleMetadata().serialize())
    # Assert that the serialized result is the same
   

# Generated at 2022-06-13 09:00:05.691697
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    assert RoleMetadata()

# Generated at 2022-06-13 09:00:13.168222
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    '''
    Test the serialize method of the RoleMetadata class.

    Note: The results are almost the same. Some differences are in white spaces and order.
    That's expected and python can handle that.
    '''

    m = RoleMetadata()
    setattr(m, 'allow_duplicates', False)
    setattr(m, 'dependencies', [])
    m_serialized = m.serialize()
    assert m_serialized == {
        'allow_duplicates': False,
        'dependencies': []
    }

    m2 = RoleMetadata()
    setattr(m2, 'allow_duplicates', False)
    setattr(m2, 'dependencies', [])
    m2_serialized = m2.serialize()

# Generated at 2022-06-13 09:00:44.972489
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.role import Role
    from ansible.playbook.role.include import RoleInclude

    role = Role()
    role._role_path = os.path.join('/my/path', 'roles', 'my_role')
    metadata = RoleMetadata()
    args = {'dependencies': [{'role': 'foo'}]}
    meta = RoleMetadata.load(args, owner=role, loader=role._loader)
    assert len(meta._dependencies) == 1
    assert isinstance(meta._dependencies[0], RoleInclude)
    assert meta._dependencies[0]._role_name == 'foo'

# Generated at 2022-06-13 09:00:51.997298
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    role_metadata_object = RoleMetadata()
    data = dict(
        allow_duplicates=True,
        dependencies=[dict(src="role1", name="role1_name")],
    )
    # pylint: disable=protected-access
    role_metadata_object.deserialize(data)
    assert role_metadata_object._allow_duplicates == True
    assert role_metadata_object._dependencies == [dict(src="role1", name="role1_name")]

# Generated at 2022-06-13 09:00:55.752230
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    role_metadata = RoleMetadata()
    role_metadata.deserialize(dict(allow_duplicates=False, dependencies=[]))
    assert role_metadata.allow_duplicates == False
    assert role_metadata.dependencies == []


# Generated at 2022-06-13 09:01:00.709948
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    # If the constructor has no parameter, it should raise an exception
    try:
        RoleMetadata()
    except TypeError as exc:
        print('RoleMetadata has no parameter')
    try:
        RoleMetadata('')
    except TypeError as exc:
        print('RoleMetadata has no parameter')
    RoleMetadata('a')

# test the constructor of RoleMetadata
if __name__ == '__main__':
    test_RoleMetadata()

# Generated at 2022-06-13 09:01:03.170563
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    r = RoleMetadata()
    data = dict(
        allow_duplicates=False,
        dependencies=[]
    )
    r.deserialize(data)
    print(r.allow_duplicates)
    print(r.dependencies)


# Generated at 2022-06-13 09:01:03.919411
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    assert True

# Generated at 2022-06-13 09:01:12.765145
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    dependencies = [{'src': './test/test-role'}, {'src': 'test/test-role2'}]
    allow_duplicates = False
    meta = RoleMetadata()
    meta.deserialize({'dependencies': dependencies, 'allow_duplicates': allow_duplicates})
    serialized_meta = meta.serialize()
    assert(serialized_meta['dependencies'] == dependencies)
    assert(serialized_meta['allow_duplicates'] == allow_duplicates)

# Generated at 2022-06-13 09:01:20.504493
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from collections import namedtuple
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.play_context import PlayContext

    roledef1 = RoleDefinition(name='test1')
    rolepath = '/some/path'
    roledef1._role_path = rolepath
    roledef1._role_collection = 'test.collection'
    roledef1.collections = ['test.collection', 'test.other']

    mock_loader = namedtuple('MockLoader', ['path_dwim'])
    mock_loader.path_dwim = lambda path: path

    mock_vars = namedtuple('MockVars', ['get_vars', 'get_vars_files'])
    mock_vars.get_vars = lambda: {}
    mock_

# Generated at 2022-06-13 09:01:29.023470
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    from ansible.playbook.role.meta import RoleMetadata
    from ansible.playbook.role.include import RoleInclude
    class Role(object):
        def __init__(self, role_path, role_name, role_collection=None, play=None):
            self._role_path = role_path
            self._role_name = role_name
            self._role_collection = role_collection
            self._play = play
            self.collections = []

        @property
        def _role_requested_name(self):
            return self.get_name()

        def get_name(self):
            return self._role_name

    def test_serialize(role_name):
        role = Role('/some/path', role_name)
        role_meta = RoleMetadata(role)

        role_

# Generated at 2022-06-13 09:01:34.547482
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    roleMetadata = RoleMetadata(owner=None)
    data = dict()
    data['allow_duplicates'] = True
    data['dependencies'] = ['a', 'b']
    roleMetadata.deserialize(data)
    assert roleMetadata.dependencies == ['a', 'b']
    assert roleMetadata.allow_duplicates == True