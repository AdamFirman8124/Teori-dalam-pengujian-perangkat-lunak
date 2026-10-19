

# Generated at 2022-06-13 08:52:20.459185
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    roleMetadata_object = RoleMetadata()
    assert roleMetadata_object.serialize() == {'allow_duplicates': False, 'dependencies': []}


# Generated at 2022-06-13 08:52:22.507358
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    meta = RoleMetadata()
    data = {}
    assert meta.load_data(data)

# Generated at 2022-06-13 08:52:24.347505
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    assert isinstance(RoleMetadata(), RoleMetadata)

# Generated at 2022-06-13 08:52:33.178232
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    import ansible.playbook
    import ansible.playbook.task
    m = RoleMetadata.load({
            'allow_duplicates': False },
        ansible.playbook.Play.load({
            'hosts': 'all',
            'tasks': [
                {'action': {
                    'module': 'echo',
                    'args': 'Hi!'
                }}]},
            variable_manager=ansible.vars.VariableManager(),
            loader=ansible.parsing.dataloader.DataLoader()))
    assert m.allow_duplicates == False

# Generated at 2022-06-13 08:52:37.593372
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    gi = RoleMetadata()
    gi.deserialize(data={'allow_duplicates':True, 'dependencies':"test"})
    assert gi.serialize() ==  {'allow_duplicates':True, 'dependencies':"test"}

# Generated at 2022-06-13 08:52:47.857831
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
  from ansible.playbook.role.definition import RoleDefinition
  from ansible.playbook.role.meta import RoleMetadata
  from ansible.playbook.role.requirement import RoleRequirement
  from ansible.utils.collection_loader import AnsibleCollectionLoader
  from ansible.utils.path import unfrackpath

  loader = AnsibleCollectionLoader()

# Generated at 2022-06-13 08:52:52.304265
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():

    meta = RoleMetadata()
    result = meta.deserialize(data=dict(allow_duplicates=True, dependencies=[{'role': 'b', 'tasks_from': 'main'}, {'role': 'c', 'something': 1}]))
    assert result == {'allow_duplicates': True, 'dependencies': [{'role': 'b', 'tasks_from': 'main'}, {'role': 'c', 'something': 1}]}

# Generated at 2022-06-13 08:52:58.529020
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    m = RoleMetadata()
    data = {"allow_duplicates": True,
            "dependencies": [{"role": "common"},
                             {"role": "webserver", "foo": "bar"}]
            }
    m.deserialize(data)
    assert m.allow_duplicates is True
    assert m.dependencies == [{"role": "common"},
                              {"role": "webserver", "foo": "bar"}]

# Generated at 2022-06-13 08:53:05.146000
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    test_data = dict(
        allow_duplicates=False,
        dependencies=['common', 'dev', 'prod'],
    )
    my_role_metadata = RoleMetadata()
    my_role_metadata.deserialize(data=test_data)
    test_serialize = my_role_metadata.serialize()
    assert test_data['allow_duplicates'] == test_serialize['allow_duplicates']
    assert test_data['dependencies'] == test_serialize['dependencies']


# Generated at 2022-06-13 08:53:06.086596
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    assert False, "Test not implemented"

# Generated at 2022-06-13 08:53:15.095741
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    role_metadata = RoleMetadata()
    role_metadata.allow_duplicates = True
    role_metadata.dependencies = ['test_role_a', 'test_role_b']
    assert role_metadata.serialize() == {'allow_duplicates': True, 'dependencies': ['test_role_a', 'test_role_b']}

# Generated at 2022-06-13 08:53:23.087466
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    role_info = RoleMetadata()
    result = role_info.deserialize({"dependencies": [{'role': 'test'}, {'role': 'test2'}],
                                    'allow_duplicates': False})
    assert role_info._allow_duplicates == False
    assert role_info._dependencies == [{'role': 'test'}, {'role': 'test2'}]
    result = role_info.deserialize({"dependencies": [{'role': 'test'}, {'role': 'test2'}],
                                    'allow_duplicates': True})
    assert role_info._allow_duplicates == True
    assert role_info._dependencies == [{'role': 'test'}, {'role': 'test2'}]

# Generated at 2022-06-13 08:53:30.969082
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    roleMetadata = RoleMetadata()
    roleMetadata._allow_duplicates = True
    roleMetadata._dependencies = [{'src': 'my.role', 'version': 'v1.0.0'}]

    ret = roleMetadata.serialize()

    assert ret['allow_duplicates'] == True
    assert ret['dependencies'] == [{'src': 'my.role', 'version': 'v1.0.0'}]


# Generated at 2022-06-13 08:53:38.966454
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    from ansible.playbook.role_include import RoleInclude

    meta = RoleMetadata()
    assert meta._dependencies == list()

    meta = RoleMetadata()
    meta.load({'dependencies' : [{'role':'common', 'foo':'bar'}]})
    assert meta._dependencies, [RoleInclude(name="common", play=None, foo="bar")]

    meta = RoleMetadata()
    meta.load({'dependencies' : [{'name':'common', 'foo':'bar'}]})
    assert meta._dependencies, [RoleInclude(name="common", play=None, foo="bar")]

    meta = RoleMetadata()
    meta.load({'dependencies' : [{'role':'common', 'vars':{'foo':'bar'}}]})


# Generated at 2022-06-13 08:53:47.102571
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    role = RoleMetadata(owner=None)
    role._allow_duplicates = True
    role._dependencies = [{"name": "test_role1"}, {"name": "test_role2"}]

    role_data = role.serialize()

    assert role_data['allow_duplicates'] is True
    assert len(role_data['dependencies']) == 2
    assert role_data['dependencies'][0]['name'] == "test_role1"
    assert role_data['dependencies'][1]['name'] == "test_role2"

# Generated at 2022-06-13 08:53:55.449987
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    _m = RoleMetadata()
    _m.deserialize({'allow_duplicates':True,
                    'dependencies':['geerlingguy.jenkins',
                                    {'src':'zilla.my-role',
                                     'some_var':'some_value'}]})
    assert _m._allow_duplicates == True
    assert _m._dependencies == ['geerlingguy.jenkins',
                                {'src':'zilla.my-role',
                                 'some_var':'some_value'}]

# Generated at 2022-06-13 08:53:57.284838
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    r = RoleMetadata()
    assert r._allow_duplicates == False
    assert r._dependencies == []
    pass

# Generated at 2022-06-13 08:53:58.640560
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    role_meta_obj = RoleMetadata()
    assert role_meta_obj is not None

# Generated at 2022-06-13 08:54:05.490131
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    import json
    m = RoleMetadata()
    m._allow_duplicates = True
    m._dependencies = ['foo', 'bar']
    data = m.serialize()
    assert data == {'allow_duplicates': True, 'dependencies': ['foo', 'bar']}

    assert json.loads(m.to_json()) == {'allow_duplicates': True, 'dependencies': ['foo', 'bar']}

    assert json.loads(m.to_json(indent=4)) == {'allow_duplicates': True, 'dependencies': ['foo', 'bar']}


# Generated at 2022-06-13 08:54:08.189554
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    role_meta = RoleMetadatas()

    # Method deserialize of class RoleMetadata
    data = {'allow_duplicates': True, 'dependencies': [1, 2, 3]}
    role_meta.deserialize(data)
    assert role_meta.allow_duplicates == True
    assert role_meta.dependencies == [1, 2, 3]

# Generated at 2022-06-13 08:54:24.517328
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    m = RoleMetadata()
    setattr(m, 'allow_duplicates', True)
    setattr(m, 'dependencies', ['test.testrole'])
    assert m.serialize() == {'allow_duplicates': True, 'dependencies': ['test.testrole']}
    assert m.serialize() == {'allow_duplicates': True, 'dependencies': ['test.testrole']}

# Generated at 2022-06-13 08:54:31.105341
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    m = RoleMetadata.load(dict(dependencies=[]), owner=None)
    assert isinstance(m, RoleMetadata)
    assert m._dependencies == []

    try:
        RoleMetadata.load([], owner='')
        assert False
    except AnsibleParserError as e:
        assert str(e) == "the 'meta/main.yml' for role  is not a dictionary"

    data = dict(dependencies=[
        dict(role='role1'),
        dict(src='role2', version='1.0')
    ])
    m = RoleMetadata.load(data, owner='')
    assert isinstance(m._dependencies, list)
    assert len(m._dependencies) == 2

# Generated at 2022-06-13 08:54:35.152463
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    obj = RoleMetadata()
    obj._allow_duplicates = True
    obj._dependencies = ['foo']

    obj.deserialize({})
    assert obj.allow_duplicates is False
    assert obj.dependencies == []

    obj.deserialize({'allow_duplicates': True,
                     'dependencies': ['foo', 'bar']})
    assert obj.allow_duplicates is True
    assert obj.dependencies == ['foo', 'bar']

# Generated at 2022-06-13 08:54:47.148489
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    """
    Test cases for method load() of class RoleMetadata
    """
    import copy
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.plugins.loader import role_loader


# Generated at 2022-06-13 08:54:54.079416
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins.loader import module_loader

    m = RoleMetadata(owner=PlayContext())
    assert m._allow_duplicates is False
    assert m._dependencies == []
    assert m._loader is None
    assert m._name is None
    assert m._owner == PlayContext()
    assert m._variable_manager is None

# Generated at 2022-06-13 08:54:56.598373
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    x = RoleMetadata()
    assert x._allow_duplicates == False
    assert x._dependencies == []

# Generated at 2022-06-13 08:55:07.673328
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    # role_path: test/data/playbooks/roles/collection1.tests.test_collections_nonamespace
    meta_source = """
allow_duplicates: False
dependencies:
  - src: 'ns1.tests.test_collections_namespace1'
    path: 'bar/baz'
    scm: 'git'
    version: 'master'
  - src: 'ns2.tests.test_collections_namespace2'
    version: '1.2.3'
  - src: 'ns1.tests.test_collections_namespace1'
    name: 'foo.bar'
"""
    import yaml
    yaml_meta = yaml.safe_load(meta_source)
    from ansible.playbook.role import Role
    role = Role()
    role

# Generated at 2022-06-13 08:55:15.930769
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    from ansible.playbook.role.definition import RoleDefinition

    role_definition = RoleDefinition('/somewhere')
    role_metadata = RoleMetadata(owner=role_definition)
    role_metadata.deserialize({'allow_duplicates': True, 'dependencies': [{'name': 'nginx'}, {'role': 'common'}]})

    assert role_metadata.allow_duplicates == True
    assert len(role_metadata.dependencies) == 2
    assert role_metadata.dependencies[0].get_name() == 'nginx'
    assert role_metadata.dependencies[1].get_name() == 'common'

# Generated at 2022-06-13 08:55:21.008446
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    r = RoleMetadata(owner=None)
    r.dependencies = [{'role': 'foo'}, 'bar', 'baz']
    assert r.serialize() == {'allow_duplicates': False, 'dependencies': [{'role': 'foo'}, 'bar', 'baz']}


# Generated at 2022-06-13 08:55:30.511015
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    data1 = dict(allow_duplicates=True, dependencies=[])
    data2 = dict(allow_duplicates=False, dependencies=['a.b.c', 'x.y.z'])
    data3 = dict(allow_duplicates=True, dependencies=['a-b-c', 'x-y-z'])
    data4 = dict(allow_duplicates=False, dependencies=['a$b$c', 'x$y$z'])

# Generated at 2022-06-13 08:56:01.548139
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    import json
    import tempfile
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.block import Block

    from ansible.playbook.role_context import RoleContext

    from ansible.executor.task_queue_manager import TaskQueueManager

    from io import StringIO

    def _get_loader():
        loader = DataLoader()

# Generated at 2022-06-13 08:56:06.471281
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    '''test_RoleMetadata_load'''

    role_metadata = RoleMetadata()
    data = {'allow_duplicates': True}
    role_metadata.load(data)

    assert role_metadata.allow_duplicates is True

# Generated at 2022-06-13 08:56:13.100892
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    data = {}
    role = AnsibleRole('dummy')
    role_metadata = RoleMetadata(owner=role)
    role_metadata._load_dependencies = Mock(return_value=None)
    ret = role_metadata.load(data, owner=role)
    assert ret.allow_duplicates == False
    assert ret.dependencies == []

# Generated at 2022-06-13 08:56:14.571106
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    meta = RoleMetadata()
    assert meta.allow_duplicates is False
    assert meta.dependencies == []

# Generated at 2022-06-13 08:56:17.454818
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    RoleMetadata.load({'allow_duplicates': False, 'dependencies': []}, None)
    RoleMetadata.load({'allow_duplicates': False, 'dependencies': [{'name': 'test_name', 'src': 'test_src'}]}, None)

# Generated at 2022-06-13 08:56:21.641725
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    config=dict(
        galaxy_info=None,
        allow_duplicates=False,
        dependencies=list(),
        argument_specs={}
    )
    role=RoleMetadata(config)
    assert role.allow_duplicates is config["allow_duplicates"]
    assert role.dependencies == config["dependencies"]

# Generated at 2022-06-13 08:56:22.167637
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    pass

# Generated at 2022-06-13 08:56:26.833720
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():

    metadata = RoleMetadata(owner=None)

    setattr(metadata, 'allow_duplicates', False)
    setattr(metadata, 'dependencies', [])

    assert metadata.serialize() == {'allow_duplicates': False, 'dependencies': []}



# Generated at 2022-06-13 08:56:31.025235
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.playbook.role._role_include import RoleInclude
    from ansible.playbook.role._role_path import RolePath
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.task.include import TaskInclude

    # Test with just the name of the role
    RoleMetadata.load({'dependencies': ['role']}, owner=RoleDefinition())
    # Test with name of the role and the version
    RoleMetadata.load({'dependencies': ['role,1.0']}, owner=RoleDefinition())
    # Test with just the name of the role
    RoleMetadata.load({'dependencies': ['role']}, owner=RoleDefinition())
    # Test with name of the role, the version and allow_duplicates

# Generated at 2022-06-13 08:56:38.837517
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from ansible.playbook.role import Role
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.block import Block
    from ansible.parsing.yaml.objects import AnsibleSequence, AnsibleMapping
    from ansible.playbook.play_context import PlayContext

    variable_manager = dict()
    loader = dict()
    variable_manager['vars'] = dict()
    variable_manager['extra_vars'] = dict()
    variable_manager['options'] = dict()

    context = PlayContext()

    data = dict()
    data['defaults'] = dict()
    data['defaults']['tests'] = dict()
    data

# Generated at 2022-06-13 08:57:26.820583
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    role_metadata = RoleMetadata()
    data = dict(allow_duplicates=False, dependencies=['role1'])
    role_metadata.deserialize(data)
    assert role_metadata.serialize() == data

# Generated at 2022-06-13 08:57:34.694855
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    from ansible.playbook.role.definition import RoleDefinition

    from ansible.playbook.role.metadata import RoleMetadata
    role1 = RoleDefinition.load("webserver", ".", None, None, None)
    role1.metadata = RoleMetadata.load({
        "allow_duplicates": True,
        "dependencies": [
            "foo",
            "bar",
            {
                "role": "baz",
                "x": "y"
            }
        ]
    }, role1)

    test_data = {
        'allow_duplicates': True,
        'dependencies': ['foo', 'bar', {'role': 'baz', 'x': 'y'}]
    }

    assert role1.metadata.serialize() == test_data


# Generated at 2022-06-13 08:57:42.406760
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    '''
    Test function for deserialize method of class RoleMetadata.
    '''

    dObj = RoleMetadata()
    data = {'allow_duplicates': True, 'dependencies': 'test'}
    dObj.deserialize(data)
    assert dObj._dependencies == data.get('dependencies', [])
    assert dObj._allow_duplicates == data.get('allow_duplicates', False)



# Generated at 2022-06-13 08:57:46.949446
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    json_data = {
        "dependencies": [
            {
                "role": "foo"
            },
            {
                "role": "bar"
            }
        ],
        "allow_duplicates": False
    }

    test_dict = RoleMetadata().load(json_data).serialize()
    assert test_dict == json_data


# Generated at 2022-06-13 08:57:50.150933
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    role_metadata = RoleMetadata()
    assert role_metadata._allow_duplicates == False
    assert role_metadata._dependencies == []
    assert role_metadata._galaxy_info is None
    assert role_metadata._argument_specs == {}

# Generated at 2022-06-13 08:57:56.874872
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    import yaml
    from collections import namedtuple
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.play import Play

    # load a sample play definition

# Generated at 2022-06-13 08:58:03.697941
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    import ansible.playbook.role.meta
    import ansible.playbook.role.definition
    import ansible.playbook.role.include

    m = RoleMetadata()
    m.deserialize({'allow_duplicates': True, 'dependencies': ['baz']})

    assert m._allow_duplicates == True
    assert isinstance(m._dependencies[0], ansible.playbook.role.include.RoleInclude) == True
    assert m._dependencies[0]._role == 'baz'


# Generated at 2022-06-13 08:58:10.647462
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    '''
    In this test, we check that the `deserialize` method of class `RoleMetadata` correctly sets the value of the
    attributes.

    We also check that the method raises the right kind of error if the argument passed is not of the right type.
    '''
    # Make sure it raises the right error if passed an argument that is not a dictionary
    try:
        RoleMetadata.deserialize(1)
        assert False
    except AssertionError:
        pass

    class TestRoleMetadata(RoleMetadata):
        '''
        Test class for RoleMetadata, used for testing the deserialize method
        '''
        def __init__(self):
            self.value_1 = None
            self.value_2 = None

            super(TestRoleMetadata, self).__init__()

    # make sure

# Generated at 2022-06-13 08:58:13.472780
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    role_metadata = RoleMetadata()
    role_metadata.deserialize({'allow_duplicates': True, 'dependencies': None})
    assert role_metadata.allow_duplicates == True
    assert role_metadata.dependencies == []


# Generated at 2022-06-13 08:58:17.465997
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    each = RoleMetadata()
    each.allow_duplicates = True
    each.dependencies = [
        {'role': 'foobar1'},
        {'role': 'foobar2'},
    ]
    data = each.serialize()

    assert data is not None
    assert data['allow_duplicates'] is True
    assert len(data['dependencies']) == 2
    assert data['dependencies'][0]['role'] == 'foobar1'
    assert data['dependencies'][1]['role'] == 'foobar2'

# Generated at 2022-06-13 08:59:50.680367
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    print("test_RoleMetadata_deserialize START")
    obj = RoleMetadata()
    #obj.load(None)
    #obj.deserialize(None)
    print("test_RoleMetadata_deserialize END")

# Generated at 2022-06-13 09:00:00.733317
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    import sys
    import yaml

    # 1. Tests with errors
    #  1.1 Empty metadata
    assert yaml.load("") == {}
    with pytest.raises(AnsibleParserError):
        RoleMetadata.load({}, None)

    # 2. Tests without errors
    # 2.1 Test the correct parsing of a metadata
    # Create the metadata file

# Generated at 2022-06-13 09:00:08.683107
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    data = dict(
        galaxy_info = dict(
            description = 'Role description',
            author = 'Role author',
            min_ansible_version = '1.0',
            platforms = dict(
                platform = dict(
                    platform = 'some_platform',
                    versions = ['1','2']
                ),
            ),
            galaxy_tags = ['tag', 'tag2'],
            galaxy_links = [dict(name='Link name', url='example.com')],
            dependencies = [],
            license = 'GPLv3',
            company = 'Role Company',
            issues_url = 'www.example.com',
            min_python_version = '3.4',
        ),
        allow_duplicates = True,
        dependencies = []
    )

    from ansible.playbook.role import Role
   

# Generated at 2022-06-13 09:00:12.674293
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    role_metadata = RoleMetadata()
    role_metadata._allow_duplicates = True
    role_metadata._dependencies = ['/some/path/some_other_role']
    serialize_result = {
        'allow_duplicates': True,
        'dependencies': ['/some/path/some_other_role'],
    }
    assert role_metadata.serialize() == serialize_result

# Generated at 2022-06-13 09:00:23.423714
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.playbook.role.definition import RoleDefinition
    # Load a role dependency
    rd = RoleMetadata.load({'dependencies': [{"role": "foobar.com", "name": "foobar.com"}]}, RoleDefinition())
    assert rd._dependencies[0]._role_name == "foobar.com"
    assert rd._dependencies[0]._role_name_set_explicitly is True
    assert rd._dependencies[0]._role_collection is None
    # Load a role from a collection
    rd = RoleMetadata.load({'dependencies': [{"role": "foobar.com", "name": "foobar.com", "collections": ["collections"]}]}, RoleDefinition())

# Generated at 2022-06-13 09:00:26.061622
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    data = {'dependencies': ['role1', 'role2']}
    assert RoleMetadata().deserialize(data) == {'dependencies': ['role1', 'role2'], 'allow_duplicates': False}

# Generated at 2022-06-13 09:00:32.042391
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    from ansible.playbook.role.meta import RoleMetadata
    meta = RoleMetadata()
    meta._allow_duplicates = False
    meta._dependencies = []

    expected = {'allow_duplicates': False, 'dependencies': []}
    assert meta.serialize() == expected

# This test is needed to be able to import RoleMetadata from here,
# since it is also imported from ansible.playbook.role.meta when the
# latter is imported by ansible.playbook.role.definition

# Generated at 2022-06-13 09:00:35.264886
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    data = {'allow_duplicates': False, 'dependencies': []}
    role = RoleMetadata()
    role.deserialize(data)
    assert role.serialize() == data

# Generated at 2022-06-13 09:00:44.279899
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.play import Play
    from ansible.playbook.role_include import RoleInclude

    def mock_role_definition(**kwargs):
        role_definition = RoleDefinition()
        for attr in kwargs:
            setattr(role_definition, attr, kwargs[attr])
        return role_definition

    # Set up RoleDefinition objects
    rdt_a = mock_role_definition(
        name='package_installer',
        get_collections='ansible.legacy')
    rdt_b = mock_role_definition(
        name='yum_package',
        get_collections='ansible.legacy')

    # Set up RoleInclude objects

# Generated at 2022-06-13 09:00:50.919785
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    role_metadata = RoleMetadata(None)
    role_metadata.allow_duplicates = True
    role_metadata.dependencies = [{}, {}]
    role_metadata.galaxy_info = {}
    role_metadata.argument_specs = {}
    serialized = role_metadata.serialize()
    expected_serialized = {
        u'allow_duplicates': True,
        u'dependencies': [{}, {}]
    }
    assert serialized == expected_serialized