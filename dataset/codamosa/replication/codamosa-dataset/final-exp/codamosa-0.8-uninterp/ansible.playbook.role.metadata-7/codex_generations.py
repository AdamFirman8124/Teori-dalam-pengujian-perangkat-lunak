

# Generated at 2022-06-13 08:52:24.728392
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.playbook.play_context import PlayContext
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.playbook.play import Play
    from ansible.playbook.role import Role

    context._init_global_context(load_plugins=False)

    def _get_base_vars():
        loader = DataLoader()
        vars_manager = VariableManager()
        play_context = PlayContext()
        play_context._set_loader(loader)
        base_vars = vars_manager.get_vars(play=Play(), loader=loader, play_context=play_context)
        play_context._set_vars(base_vars)

        return (loader, vars_manager, play_context)

   

# Generated at 2022-06-13 08:52:35.877369
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.plugins.loader import action_loader
    from ansible.plugins.loader import lookup_loader
    from ansible.plugins.loader import module_loader
    from ansible.plugins.loader import strategy_loader
    from ansible.plugins.loader import module_utils_loader
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager


# Generated at 2022-06-13 08:52:46.684942
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    import ansible.playbook.role.definition
    import ansible.playbook.role.include
    class Play:
        _entries = {}
        def get_entry_point(self):
            return os.path.join(os.path.dirname(__file__), 'testvars', 'roles')
    class Role:
        _role_path = 'rolepath'
    p = Play()
    r = Role()
    r._play = p
    r._variable_manager = None
    r._loader = None
    m = RoleMetadata.load(dict(), r)
    assert isinstance(m, RoleMetadata)
    assert not m._allow_duplicates
    assert isinstance(m._dependencies, list)
    assert m._dependencies == []
    assert m._owner == r
    m = RoleMet

# Generated at 2022-06-13 08:52:53.669525
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.playbook.block import Block
    from ansible.playbook.role import Role
    from ansible.playbook.task import Task
    # Create a PlayContext
    play_context = PlayContext()
    # Create a Play
    play = Play().load({'name': 'test', 'hosts': 'localhost'}, variable_manager=None, loader=None)
    # Create a Block
    block = Block().load({}, play=play, task_include=None, use_handlers=False)
    # Create a Role
    role = Role().load({'name': 'test'}, play=play)
    # Create a Task
    host = 'test'

# Generated at 2022-06-13 08:53:03.232430
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.playbook.role import Role

    role = Role.load('/path/to/role', loader=None, variable_manager=None, play=None)
    role_metadata = RoleMetadata.load({'allow_duplicates': True, 'dependencies': ['my.dependency', 'my.other_dependency']},
                                      owner=role, loader=None, variable_manager=None)

    assert role_metadata._allow_duplicates

    dependencies = role_metadata._dependencies
    assert len(dependencies) == 2
    assert dependencies[0].get_name() == 'my.dependency'
    assert dependencies[1].get_name() == 'my.other_dependency'

# Generated at 2022-06-13 08:53:04.034182
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    assert True

# Generated at 2022-06-13 08:53:04.571267
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    pass

# Generated at 2022-06-13 08:53:08.054197
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():

    with pytest.raises(AnsibleParserError):
        RoleMetadata.load([], None)

    with pytest.raises(AnsibleParserError):
        RoleMetadata.load({'dependencies':'asd'}, None)


# Generated at 2022-06-13 08:53:12.361260
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.playbook.role.definition import RoleDefinition

    rd = RoleDefinition.load(dict(name='test_role'))
    rmeta = RoleMetadata.load(dict(dependencies=[dict(src='a.b.c')]), rd, None, None)
    assert isinstance(rmeta, RoleMetadata)

# Generated at 2022-06-13 08:53:20.246457
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.block import Block
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.handler_task_include import HandlerTaskInclude
    from ansible.errors import AnsibleParserError
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group

    play_context = PlayContext()
    block = Block()
    hosts = [Host(name="localhost")]
    groups = [Group(name="localhost")]

# Generated at 2022-06-13 08:53:31.371828
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    x = RoleMetadata()
    x.deserialize(dict(allow_duplicates=True, dependencies=[{}]))
    assert x.allow_duplicates is True
    assert isinstance(x.dependencies, list)

# Generated at 2022-06-13 08:53:39.301758
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    import ansible_collections
    from ansible_collections.testns.testcoll.plugins.module_utils.test_module import AnsibleExitJson
    from ansible_collections.testns.testcoll.plugins.module_utils.test_module import AnsibleFailJson

    # test data for metadata file

# Generated at 2022-06-13 08:53:45.020049
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    RoleMetadata._serialize = RoleMetadata.serialize
    RoleMetadata.serialize = lambda x: dict(dep=x._dependencies)
    result = RoleMetadata().serialize()
    assert result["dep"] == []
    RoleMetadata.serialize = RoleMetadata._serialize
    del RoleMetadata._serialize


# Generated at 2022-06-13 08:53:51.708668
# Unit test for constructor of class RoleMetadata

# Generated at 2022-06-13 08:53:57.828848
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    metadata = RoleMetadata()
    tests = [
        [{'allow_duplicates': True, 'dependencies': ["foo"]},
         {'allow_duplicates': True, 'dependencies': ["foo"]}],

        [{},
         {'allow_duplicates': False, 'dependencies': []}],
    ]
    for test in tests:
        metadata.deserialize(test[0])
        assert metadata.serialize() == test[1]

# Generated at 2022-06-13 08:53:58.978767
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    roleMetadata = RoleMetadata()
    roleMetadata.serialize()
    assert True

# Generated at 2022-06-13 08:54:07.629454
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.playbook.helpers import load_list_of_roles
    from ansible.collections.ansible.legacy.plugins.action import ActionModule
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    loader = DataLoader()
    variable_manager = VariableManager()
    variable_manager.set_inventory(loader.load_from_file('test/units/inventory'))
    role_data = {'galaxy_info': {},
                 'dependencies': [{u'src': u'../other'}]}

# Generated at 2022-06-13 08:54:10.380213
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    data = dict(
        allow_duplicates=False,
        dependencies=list()
    )
    res = RoleMetadata.load(data, None).serialize()
    assert res == data

# Generated at 2022-06-13 08:54:21.858739
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins.loader import lookup_loader
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText

    variable_manager = VariableManager()
    variable_manager.extra_vars = dict(foo='bar')
    variable_manager.set_nonpersistent_facts(dict(lol='lol'))
    play_context = PlayContext(variables=variable_manager)
    loader = lookup_loader.get('file')
    templar = Templar(loader=loader, variables=variable_manager, playcontext=play_context)

    # set dependencies
    deps_path = '../deps'
    deps_path_abs = os.path.ab

# Generated at 2022-06-13 08:54:29.864151
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    data = {
        "allow_duplicates": True,
        "dependencies": [
            {
                "role": "geerlingguy.apache",
                "name": "geerlingguy.apache",
                "collections": [
                    "geerlingguy.collection"
                ]
            },
            {
                "role": "geerlingguy.apache",
                "name": "geerlingguy.apache",
                "collections": [
                    "geerlingguy.collection"
                ]
            }
        ],
    }
    variable_manager = Mock()
    variable_manager.extra_vars = dict()
    loader = Mock()
    owner = Mock()
    owner._play = Mock()
    owner.collections = ["geerlingguy.collection"]
    owner._role_collection = None



# Generated at 2022-06-13 08:54:46.041889
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    role_metadata = RoleMetadata(owner="test")
    assert role_metadata._owner == "test"
    assert isinstance(role_metadata._dependencies, list)
    assert isinstance(role_metadata._galaxy_info, dict)

# Generated at 2022-06-13 08:54:50.578789
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    rolemetadata = RoleMetadata()
    setattr(rolemetadata, 'allow_duplicates', True)
    setattr(rolemetadata, 'dependencies', ['apache','tomcat'])
    result=rolemetadata.serialize()
    assert result == {'allow_duplicates': True, 'dependencies': ['apache','tomcat']}


# Generated at 2022-06-13 08:54:54.621270
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    initial_data = dict(
        allow_duplicates=True,
        dependencies=['foo.bar']
    )

    serialized = RoleMetadata.serialize(initial_data)
    assert serialized == initial_data

# Generated at 2022-06-13 08:54:57.051869
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    '''
    Unit test for constructor of class RoleMetadata
    '''
    role = RoleMetadata()

# Generated at 2022-06-13 08:54:57.864469
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    pass

# Generated at 2022-06-13 08:55:03.663597
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    role_metadata = RoleMetadata()

    # test valid data
    test_data = dict(allow_duplicates=True, dependencies=['role_a', 'role_b'])
    role_metadata._allow_duplicates = test_data['allow_duplicates']
    role_metadata._dependencies = test_data['dependencies']
    assert test_data == role_metadata.serialize()


# Generated at 2022-06-13 08:55:14.578178
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():

    valid_data = {
        "allow_duplicates": True,
        "dependencies": [
            { "role": "common", "some_parameter": "foo" },
            "other"
        ]
    }

    invalid_data = [
        { "dependencies": "hello" },
        { "dependencies": [ "hello" ] },
        { "dependencies": { "hello": "world" } }
    ]

    # Valid data
    m = RoleMetadata.load(valid_data, owner='owner')
    assert(type(m) == RoleMetadata)

    # Invalid data
    for d in invalid_data:
        try:
            _ = RoleMetadata.load(d, owner='owner')
            assert(False)
        except AssertionError:
            assert(True)

# Generated at 2022-06-13 08:55:16.346465
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    a = ansible.playbook.RoleMetadata()
    a.load()
    a.serialize()
    assert(True)


# Generated at 2022-06-13 08:55:22.580946
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    import ansible.playbook
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.role import Role
    from ansible.parsing.utils.addresses import parse_address
    from ansible.plugins.loader import add_all_plugin_dirs

    add_all_plugin_dirs()

    play_context = PlayContext()
    play_context.remote_addr = parse_address("localhost")
    play_context.network_os = 'default'
    play_context.remote_user = 'default'
    play_context.become = False
    play_context.become_method = None
    play_context.become_user = None
    play_context.port = None
    play_context.passwords = {}


# Generated at 2022-06-13 08:55:31.119390
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    """
    RoleMetadata: load()
    """

    # basic loading of a role from a path, no dependency parsing yet
    from ansible.playbook.role import Role
    from ansible.playbook.play import Play
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.inventory.inventory import Inventory
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.errors import AnsibleError

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = Inventory(loader=loader, variable_manager=variable_manager, host_list=[])


# Generated at 2022-06-13 08:56:01.894166
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.playbook.role import Role
    import sys
    from ansible.playbook.play_context import PlayContext

    # Create a fake role with fake meta/main.yml
    fake_role_name = 'fake_role_name'
    fake_role_path = 'fake_role_path'
    fake_meta_main_yml = """\
{
    "allow_duplicates": "true",
    "dependencies": [
        "role:fake_dependencies_1",
        "role:fake_dependencies_2"
    ]
}
"""
    fake_meta_main_yml_wrong_allow_duplicates = "{\n    \"allow_duplicates\": \"yes\"\n}\n"

# Generated at 2022-06-13 08:56:07.982204
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    data = {"allow_duplicates": True, "dependencies": []}
    dummy_owner = ""
    result = RoleMetadata.load(data, dummy_owner)

    assert data['allow_duplicates'] == result.allow_duplicates
    assert data['dependencies'] == result.dependencies

# Generated at 2022-06-13 08:56:16.108063
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    data = dict()
    data['allow_duplicates'] = "false"
    data['dependencies'] = list()
    data['dependencies'].append("geerlingguy.apache")
    data['dependencies'].append("geerlingguy.ntp")
    role_metadata = RoleMetadata()
    role_metadata.load(data)
    assert role_metadata.allow_duplicates == False
    assert role_metadata.dependencies[0].get_name() == "geerlingguy.apache"
    assert role_metadata.dependencies[1].get_name() == "geerlingguy.ntp"

# Generated at 2022-06-13 08:56:20.221736
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    # Testing if test passes with empty data
    m = RoleMetadata(owner=None)
    m.deserialize(data=dict())
    assert m.allow_duplicates == False
    assert m.dependencies == []
    assert m._galaxy_info is None
    assert m._argument_specs is None

    # Testing if test passes with filled data
    data = dict()
    data['allow_duplicates'] = True
    data['dependencies'] = ['test_role']
    m.deserialize(data=data)
    assert m.allow_duplicates == True
    assert m.dependencies == ['test_role']

# Generated at 2022-06-13 08:56:21.604106
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    obj = RoleMetadata(owner=None)

    assert obj is not None

# Generated at 2022-06-13 08:56:32.304524
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.playbook.block import Block
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.playbook.playbook import Playbook
    from ansible.playbook.task import Task
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from collections import namedtuple
    from ansible.utils.vars import combine_vars

    myloader = DataLoader()
    myinventory = InventoryManager(loader=myloader, sources='localhost,')

    # fake play, task and role

# Generated at 2022-06-13 08:56:33.612788
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    print("Testing constructor of RoleMetadata")


# Generated at 2022-06-13 08:56:35.925338
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():

    # create instance of class
    rm = RoleMetadata()

    # deserialize
    rm.deserialize({})

    # test for value of allow_duplicates
    assert rm._allow_duplicates == False


# Generated at 2022-06-13 08:56:40.966971
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    data = dict(
            allow_duplicates=True,
            dependencies=[dict(name='foo'), dict(name='bar')]
    )
    m = RoleMetadata()
    m.deserialize(data)
    res = m.serialize()
    assert data['allow_duplicates'] == res['allow_duplicates']
    assert data['dependencies'] == res['dependencies']

# Generated at 2022-06-13 08:56:50.368654
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    from ansible.playbook.play import Play
    from ansible.playbook.play import PlayContext
    from ansible.playbook.task import Task
    from ansible.playbook.task import TaskInclude
    from ansible.playbook.block import Block

    context = PlayContext()
    play_source = dict(
        name="Ansible Play",
        hosts='localhost',
        gather_facts='no',
        tasks=[
            dict(action=dict(module='setup', args='')),
        ]
    )

    play = Play().load(play_source, variable_manager=None, loader=None)

# Generated at 2022-06-13 08:57:35.829192
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    main = {"_galaxy_info": {}}
    role = RoleMetadata(owner=True)
    role.load_data(main)

# Generated at 2022-06-13 08:57:41.314269
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    role_metadata_data = dict(
        allow_duplicates=False,
        dependencies=[]
    )
    role_metadata = RoleMetadata().deserialize(role_metadata_data)
    assert role_metadata.allow_duplicates == False
    assert not role_metadata.dependencies

# Generated at 2022-06-13 08:57:45.979726
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    data = dict(
        allow_duplicates=True,
        dependencies=[
            dict(src='other_role', scm='git', version='1.2.3')
        ]
    )
    metadata = RoleMetadata()
    metadata.deserialize(data)
    assert data == metadata.serialize()



# Generated at 2022-06-13 08:57:52.156740
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    roleMetadata = RoleMetadata()
    roleMetadata.dependencies = ["role1", "role2"]
    roleMetadata.allow_duplicates = False
    result = roleMetadata.serialize()
    assert result == {'dependencies': ['role1', 'role2'], 'allow_duplicates': False}
    roleMetadata.allow_duplicates = True
    result = roleMetadata.serialize()
    assert result == {'dependencies': ['role1', 'role2'], 'allow_duplicates': True}

# Generated at 2022-06-13 08:57:56.203737
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    test_data = {}
    test_data['allow_duplicates'] = False
    test_data['dependencies'] = []
    obj = RoleMetadata()
    obj.deserialize(test_data)
    assert obj.serialize() == test_data

# Generated at 2022-06-13 08:58:05.670773
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.playbook.role_include import RoleInclude

    # Assert successful load

# Generated at 2022-06-13 08:58:11.409678
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    from ansible.playbook.role.definition import RoleDefinition

    rdef = RoleDefinition()
    rdef.name = 'test_role'
    role = RoleMetadata(rdef)
    role.deserialize({'allow_duplicates': True, 'dependencies': [{'role': 'test_depended_role'}, {'role': 'test_depended_role1'}]})
    assert role.allow_duplicates == True
    assert role.dependencies[0].role == 'test_depended_role'
    assert role.dependencies[1].role == 'test_depended_role1'

# Generated at 2022-06-13 08:58:16.976463
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.role.requirement import RoleRequirement


# Generated at 2022-06-13 08:58:27.028566
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():

    test_RoleMetadata = RoleMetadata()
    test_data = {
        'allow_duplicates': True,
        'dependencies': [
            'my_role',
            {
                'src': 'https://github.com/example/another_role',
                'version': '1.0',
                'name': 'another_role',
                'scm': 'git',
                'path': '.',
                'other_vars': {
                    'whatever': 'something'
                }
            }
        ]
    }
    assert test_RoleMetadata.deserialize(test_data) == None
    assert test_RoleMetadata.allow_duplicates == True

# Generated at 2022-06-13 08:58:36.208058
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.playbook.play import Play

    owner = Play().load(dict(
        name = "foo",
        hosts = 'all',
    ))


# Generated at 2022-06-13 09:00:06.333722
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.role_include import RoleInclude
    from ansible.utils.collection_loader import AnsibleCollectionConfig
    from ansible.vars.manager import VariableManager

    # Create the objects needed in the test
    owner = RoleDefinition()
    owner._role_path = '/path/to/role'
    owner._role_collection = AnsibleCollectionConfig('namespace.collection')
    owner._play = None
    owner.collections = ['ansible.legacy']
    variable_manager = VariableManager()

    # Test when the meta/main.yml file is missing
    data = None
    m = RoleMetadata(owner=owner).load(data, owner, variable_manager=None, loader=None)
    assert m.dependencies is not None

   

# Generated at 2022-06-13 09:00:11.972782
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    '''
    Test function for the serialize method of class RoleMetadata
    '''

    #########################
    # With required args
    #########################
    # Creating RoleMetadata object
    role_metadata_obj = RoleMetadata()
    role_metadata_obj.allow_duplicates = False
    role_metadata_obj.dependencies = []

    # Serialize the object
    result = role_metadata_obj.serialize()

    # Check the result
    assert result == {
        'allow_duplicates': False,
        'dependencies': [],
    }

# Generated at 2022-06-13 09:00:17.221881
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    '''
    This function tests the method load of class RoleMetadata
    '''

    # testing RoleMetadata()
    md = RoleMetadata()
    assert md is not None

    # testing RoleMetadata.load()
    md = RoleMetadata.load({}, None, variable_manager=None, loader=None)
    assert md is not None

# Generated at 2022-06-13 09:00:21.203265
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    role_meta=RoleMetadata()
    role_meta.allow_duplicates=True
    role_meta.dependencies=[]
    result=role_meta.serialize()
    assert result=={'allow_duplicates': True, 'dependencies': []}


# Generated at 2022-06-13 09:00:23.868928
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    '''
    This is a test method for testing the constructor
    of the RoleMetadata class.
    '''
    role_metadata = RoleMetadata()
    assert(role_metadata is not None)

# Generated at 2022-06-13 09:00:30.801776
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    import json
    import os

    # given
    src_dir = os.path.dirname(__file__)
    test_data_src_file = os.path.join(src_dir, '../../../test/unit/lib/ansible/playbook/test_data/role_meta_data.json')
    with open(test_data_src_file) as f:
        test_data = json.load(f)

    # when

    # we need a valid owner for a RoleMetadata object,
    # so we construct one
    owner = _owner_for_test()

    role_meta_data = RoleMetadata(owner=owner).load_data(test_data)

    # then
    assert role_meta_data._galaxy_info == test_data['galaxy_info']
    assert role_meta_

# Generated at 2022-06-13 09:00:40.585629
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    import os
    import json
    import sys
    import ansible.playbook
    import ansible.inventory
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.plugins.callback import CallbackBase
    from ansible.executor.playbook_executor import PlaybookExecutor

    from ansible.playbook.play import Play
    from ansible.playbook.playbook import Playbook


# Generated at 2022-06-13 09:00:48.384606
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.vars.manager import VariableManager

    data = dict(
        allow_duplicates=False,
        dependencies=[
            {'role': '../some_other_role'},
            '../another_role'
        ]
    )

    metad = RoleMetadata()
    metad.deserialize(data)
    assert metad.allow_duplicates == False
    assert metad.dependencies == [
        {'role': '../some_other_role'},
        '../another_role'
    ]

    play = Play()
    play.post_validate()
    play_context = PlayContext()

    role

# Generated at 2022-06-13 09:00:52.445531
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    metadata = RoleMetadata()
    data = dict()
    data.setdefault('allow_duplicates', False)
    data.setdefault('dependencies', [])
    assert metadata.deserialize(data) == None


# Generated at 2022-06-13 09:00:55.667761
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    data = {'dependencies':[{'role': 'test'}]}
    owner = RoleRequirement.load(data)
    m = RoleMetadata.load(data, owner)
    assert m.dependencies[0].role == 'test'