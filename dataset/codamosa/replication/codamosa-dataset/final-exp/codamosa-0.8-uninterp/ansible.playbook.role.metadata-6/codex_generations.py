

# Generated at 2022-06-13 08:52:24.211990
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    data_1 = dict()
    metadata = RoleMetadata()
    metadata.deserialize(data_1)
    assert metadata._allow_duplicates is False
    assert metadata._dependencies == []

    data_2 = dict(allow_duplicates=True, dependencies=[])
    metadata = RoleMetadata()
    metadata.deserialize(data_2)
    assert metadata._allow_duplicates
    assert metadata._dependencies == []

    #TODO: test for deserialize in error case

# Generated at 2022-06-13 08:52:33.483373
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    from ansible.playbook.role.metadata import RoleMetadata
    data = {}
    role_meta = RoleMetadata()
    role_meta.deserialize(data)
    assert role_meta._allow_duplicates is False
    assert role_meta._dependencies == []
    data = {
        "allow_duplicates": True,
        "dependencies": ['foo', 'bar']
    }
    role_meta = RoleMetadata()
    role_meta.deserialize(data)
    assert role_meta._allow_duplicates is True
    assert role_meta._dependencies == ['foo', 'bar']

# Generated at 2022-06-13 08:52:38.601833
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    record = {
        'allow_duplicates': False,
        'dependencies': []
    }
    rm = RoleMetadata().deserialize(record)

    assert rm.allow_duplicates == record['allow_duplicates']
    assert rm.dependencies == record['dependencies']

# Generated at 2022-06-13 08:52:41.735951
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    metadata = RoleMetadata.load(get_valid_metadata(), owner=None)
    assert metadata.serialize() == get_valid_metadata_serialized()


# Generated at 2022-06-13 08:52:49.625395
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():

    class MockRole(object):
        def __init__(self, name):
            self.name = name

        def get_name(self):
            return self.name

    meta_main = {
        'dependencies': [
            {'role': 'test'},
            {'role': 'test2'}
        ]
    }

    role = MockRole('test')
    role_meta = RoleMetadata.load(meta_main, owner=role)
    #print(role_meta.__dict__)
    assert role_meta._dependencies[0]._role_name == 'test'
    assert role_meta._dependencies[1]._role_name == 'test2'

    meta_main = {
        'dependencies': [
            'foo',
            'bar'
        ]
    }

    role = Mock

# Generated at 2022-06-13 08:53:00.539632
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():

    from ansible.utils.vars import combine_vars

    class VariableManagerMock(object):
        def get_vars(self, loader=None, play=None, host=None, task=None, include_hostvars=True):
            return {
                'foo': 'foo',
                'bar': 'bar',
            }

        def extra_vars_from_files(self, items):
            return {}

        def all_vars(self, loader=None, play=None, host=None, task=None, include_hostvars=True):
            return {}

        def get_host_variables(self, host):
            return {}

        def get_group_variables(self, group):
            return {}

        def get_group_vars(self, group, play=None):
            return {}

       

# Generated at 2022-06-13 08:53:01.213518
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    pass

# Generated at 2022-06-13 08:53:08.464661
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    r = RoleMetadata()
    # Test assign value to attr allow_duplicates
    setattr(r, '_allow_duplicates', False)
    # Test assign value to attr dependencies
    setattr(r, '_dependencies', [])
    j = r.serialize()
    # Test value of key 'allow_duplicates'
    assert j.get('allow_duplicates') == False
    # Test value of key 'dependencies'
    assert j.get('dependencies') == []


# Generated at 2022-06-13 08:53:10.343818
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    metadata = RoleMetadata()
    result = metadata.serialize()
    print(result)
    assert len(result) == 2


# Generated at 2022-06-13 08:53:14.310019
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    metadata = RoleMetadata()
    actual_result = metadata.deserialize({
        'allow_duplicates': True,
        'dependencies': ['role1', 'role2', 'role3']
    })
    assert metadata.allow_duplicates == True
    assert metadata.dependencies == ['role1', 'role2', 'role3']

# Generated at 2022-06-13 08:53:23.498808
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    role = RoleMetadata()
    assert role
    assert role._allow_duplicates == False
    assert role._dependencies == []

# Generated at 2022-06-13 08:53:35.183701
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.playbook.block import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.task import Task
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.playbook.play import Play

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = Inventory(loader=loader, variable_manager=variable_manager)
    play = Play()
    play.variable_manager = variable_manager
    play.inventory = inventory
    play.loader = loader

    task_include = TaskInclude()
    task_include._play = play

    role_metadata = RoleMetadata.load(dict(), task_include)
    assert role_metadata._dependencies

# Generated at 2022-06-13 08:53:39.470287
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    from ansible.playbook.role.definition import RoleDefinition
    role = RoleDefinition.load(dict(
        name="test",
        foo="bar"
    ), play=None)
    assert role.name == "test"
    assert role.foo == "bar"

# Generated at 2022-06-13 08:53:46.318170
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    rmd = RoleMetadata()
    rmd.allow_duplicates = False
    rmd.dependencies = ['ansible-role-patch_role', 'ansible-role-systemd']
    expected_result = {
        'allow_duplicates': False,
        'dependencies': ['ansible-role-patch_role', 'ansible-role-systemd']
    }
    assert rmd.serialize() == expected_result

# Generated at 2022-06-13 08:53:53.473570
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    assert RoleMetadata.load({}, object()).serialize() == dict(allow_duplicates=False, dependencies=[])
    assert RoleMetadata.load({'allow_duplicates': True}, object()).serialize() == dict(allow_duplicates=True, dependencies=[])
    assert RoleMetadata.load({'dependencies': ['A']}, object()).serialize() == dict(allow_duplicates=False, dependencies=['A'])


# Generated at 2022-06-13 08:54:00.971028
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    test_obj = RoleMetadata()
    test_obj.allow_duplicates = True
    test_obj.dependencies = [
        {'role': 'role1', 'name': 'test'},
        {'role': 'role2', 'name': 'test2'}
    ]
    test_obj.galaxy_info = {'author': 'test', 'company': 'test_company'}

    expected = dict(
        allow_duplicates=True,
        dependencies=[
            {'role': 'role1', 'name': 'test'},
            {'role': 'role2', 'name': 'test2'}
        ]
    )
    assert test_obj.serialize() == expected

# Generated at 2022-06-13 08:54:07.029975
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.playbook.play import Play
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.utils.vars import combine_vars
    from ansible.utils.vars import load_extra_vars
    from ansible.vars.manager import VariableManager

    # Create:
    # - tmp_dir/
    # |- test_role1/
    # | |- meta/
    # | | |- main.yml
    # | |- tasks/
    # | | |- main.yml
    # | |- vars/
    # | |- main.yml
    tmp_dir = os.path.dirname(__file__) + '/test_data/role/'

# Generated at 2022-06-13 08:54:10.256974
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    from ansible.playbook.role.definition import RoleDefinition
    rd = RoleDefinition(name="test_role_def")
    rm = RoleMetadata(owner=rd)
    assert isinstance(rm, RoleMetadata)

# Generated at 2022-06-13 08:54:14.496946
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    owner = "owner"
    data = dict(
        allow_duplicates=True,
        dependencies=[]
    )
    result = RoleMetadata(owner).serialize()
    assert result == data, "Was expecting %s but got %s" % (data, result)


# Generated at 2022-06-13 08:54:23.841831
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    # arrange
    alt_data = dict(
        allow_duplicates=True,
        dependencies=['testA,testB,testC']
    )
    from ansible.playbook.role.inc import RoleInclude

    m = RoleMetadata()
    setattr(m, 'allow_duplicates', True)
    setattr(m, 'dependencies', RoleInclude.load_list_of_roles(['testA,testB,testC'], play=None))

    # act
    role_metadata = m.serialize()

    # assert
    assert role_metadata == alt_data


# Generated at 2022-06-13 08:54:47.249483
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    import datetime

    # WARNING: this test is known to be broken, see comment above the unit test
    # also, this test is less than ideal as it should be located in a test module
    # outside of this file, but will have to work for now

    #from ansible.playbook import Playbook
    #yaml_file = "./test/sanity/inventory/hosts"
    #from ansible.inventory import Inventory
    #inventory = Inventory(yaml_file)

    #playbook = Playbook.load("./test/sanity/role-meta/deps/main.yml", variable_manager=variable_manager, inventory=inventory)
    #assert playbook.get_type() == "playbook"
    #roles = playbook.get_roles()
    #assert len(roles) == 1
    #metadata = roles

# Generated at 2022-06-13 08:54:57.697583
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.playbook.role import Role
    from ansible.playbook.role.include import RoleInclude
    from ansible.playbook.play import Play
    from ansible.playbook.playbook import Playbook
    from ansible.playbook.included_file import IncludedFile
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager


    role_name = "myrole"
    role_path = "mypath"

    # Load dummy playbook
    def load_dummy_file(filename):
        return IncludedFile(filename, 'role/meta/main.yml', [dict()])

    loader = DataLoader()
    loader.load_from_file = load_dummy_file


# Generated at 2022-06-13 08:55:02.511196
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    meta_data = {'allow_duplicates': True, 'dependencies': [{'name': 'ansible.builtin'}]}
    role_meta = RoleMetadata(owner=None).deserialize(meta_data)
    assert role_meta.allow_duplicates
    assert role_meta.dependencies


# Generated at 2022-06-13 08:55:13.831664
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    # make sure that we properly handle old style roles
    # this is a regression test for 2.1
    data = dict(dependencies=[{'role': 'foo'}, {'role': 'bar'}])
    role = RoleMetadata.load(data, None)
    assert role._dependencies[0]['role'] == 'foo'
    assert role._dependencies[1]['role'] == 'bar'

    # make sure that we properly handle old-style roles as well as facts
    # collected from the play and environment

# Generated at 2022-06-13 08:55:20.989761
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    host = 'localhost'
    hosts_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test_hosts')
    inventory = Inventory(loader=None, hosts=hosts_file, variable_manager=VariableManager())
    vm = VariableManager(loader=DataLoader(), inventory=inventory)

    # Test load function of class RoleMetadata when param data is not a dict
    test_data_not_a_dict = ''
    ret = RoleMetadata.load(test_data_not_a_dict, None)
    assert isinstance(ret, AnsibleParserError)

    # Test load function of class RoleMetadata when param data is a empty dict
    test_data_empty_dict = {}

# Generated at 2022-06-13 08:55:27.006377
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    # Create a RoleMetadata object
    role_metadata = RoleMetadata()

    # Test with just role name
    role_name = 'role1'
    role_data = {'dependencies': [{'role': role_name}]}
    role_metadata.deserialize(role_data)
    assert role_name in role_metadata._dependencies
    assert rol

# Generated at 2022-06-13 08:55:28.349727
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    pass



# Generated at 2022-06-13 08:55:38.662724
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.playbook.role import Role
    from ansible.playbook.collectionsearch import CollectionSearch
    from ansible.playbook.role.include import RoleInclude
    from ansible.utils.collection_loader import AnsibleCollectionLoader

    test_path = os.path.join(os.path.dirname(__file__), 'test_data')
    loader = AnsibleCollectionLoader(None, None)
    collection_search_list = ['ansible.legacy']
    collection_search_list.extend(CollectionSearch.get_collections_from_paths(loader, [os.path.join(test_path, 'collection_path')]))


# Generated at 2022-06-13 08:55:48.837527
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    data = {
        "allow_duplicates": True,
        "dependencies": [
            {
                "src": "https://github.com/larrycai/ansible-role-apache.git",
                "name": "ansible-role-apache",
                "version": "v1.0.0"
            }
        ]
    }
    role = RoleMetadata(owner=None)
    role.deserialize(data)
    assert role.allow_duplicates == True
    assert role.dependencies[0].name == "ansible-role-apache"
    assert role.dependencies[0].src == "https://github.com/larrycai/ansible-role-apache.git"
    assert role.dependencies[0].version == "v1.0.0"

# Generated at 2022-06-13 08:55:50.328901
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    role = RoleMetadata()

# Generated at 2022-06-13 08:56:17.654380
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    """
    Test the serialize method of RoleMetadata
    """

    mdata = RoleMetadata()
    mdata._allow_duplicates = False
    mdata._dependencies = ['foo', 'bar']

    assert isinstance(mdata.serialize(), dict)
    assert mdata.serialize()['allow_duplicates'] is False
    assert mdata.serialize()['dependencies'] == ['foo', 'bar']


# Generated at 2022-06-13 08:56:24.490348
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    # Test the case where the allow_duplicates is set and the dependencies
    # list is empty
    test_role_metadata = RoleMetadata()
    test_role_metadata.deserialize({'allow_duplicates': True})
    assert test_role_metadata.allow_duplicates == True
    assert test_role_metadata.dependencies == []

    # Test the case where allow_duplicates is not set and dependencies
    # list is not empty
    test_role_metadata = RoleMetadata()
    test_role_metadata.deserialize({'dependencies': ['foo', 'bar']})
    assert test_role_metadata.allow_duplicates == False
    assert test_role_metadata.dependencies == ['foo', 'bar']

# Generated at 2022-06-13 08:56:30.987487
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    '''
    Unit test for method serialize of class RoleMetadata
    '''
    base = Base()
    role_metadata = RoleMetadata()
    role_metadata.allow_duplicates = True
    role_metadata.dependencies = base.load_list_of_tasks([{'name': 'foo'}])
    assert role_metadata.serialize() == {'allow_duplicates': True, 'dependencies': [{'name': 'foo'}]}


# Generated at 2022-06-13 08:56:32.261336
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    role_metadata = RoleMetadata()
    assert role_metadata


# Generated at 2022-06-13 08:56:39.673433
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    from ansible.playbook import Play
    from ansible.playbook.role.include import RoleInclude
    from ansible.playbook.role.requirement import RoleRequirement
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor

    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.utils.vars import load_extra_vars
    from ansible.plugins import callback_loader


# Generated at 2022-06-13 08:56:49.372980
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    from ansible.playbook.role.meta import RoleMetadata
    from ansible.playbook.role.include import RoleInclude
    from ansible.playbook.role import Role
    from ansible.playbook.block import Block
    from ansible.playbook.play_context import PlayContext
    import ansible.constants as C

    role = Role()
    role._role_path = "test_role_path"

    role_include1 = RoleInclude()
    role_include1._role_name = "test_role_name1"
    role_include1._role_collection = "test_role_collection1"
    role_include1._role_path = "test_role_path1"

    role_include2 = RoleInclude()
    role_include2._role_name = "test_role_name2"

# Generated at 2022-06-13 08:57:06.084824
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    from ansible.playbook.role_include import IncludeRole
    from ansible.template import Template
    class TestRole:
        def __init__(self):
            self._role_name = 'test_role'
            self._role_path = '/test_role_path'
            self._play = Play()
            self._play.set_loader(TestPlay.loader)
    class TestPlay:
        def __init__(self):
            self._loader = Template.loader
            self._context = PlayContext()
        @staticmethod
        def get_loader():
            return TestPlay.loader

# Generated at 2022-06-13 08:57:15.869193
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    from ansible.playbook.role import Role
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.role.include import RoleInclude
    from ansible.parsing.mod_args import ModuleArgsParser

    m = ModuleArgsParser.parse_from_file('test_role/meta/main.yml')
    r = Role(name='test_role')
    r._metadata = RoleMetadata.load(m, r)
    m = RoleMetadata(owner=r)
    assert m.allow_duplicates == False
    assert m.dependencies == ['test_role_a', 'test_role_b'] # includes
    assert m.get_collections() == []

    m = ModuleArgsParser.parse_from_file('test_role_2/meta/main.yml')

# Generated at 2022-06-13 08:57:16.749264
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    assert True

# Generated at 2022-06-13 08:57:22.946753
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    obj = RoleMetadata(owner=None)
    obj._allow_duplicates = False
    obj._dependencies = []
    expected = {
        'allow_duplicates': False,
        'dependencies': []
    }
    assert obj.serialize() == expected

# Generated at 2022-06-13 08:58:13.086291
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    role_metadata = RoleMetadata()

    data = dict()
    data["allow_duplicates"] = True
    data["dependencies"] = ["role1"]
    role_metadata.deserialize(data)
    assert role_metadata.allow_duplicates == True
    assert role_metadata.dependencies == ["role1"]
    assert role_metadata.galaxy_info is None
    assert role_metadata.argument_specs is None
    assert role_metadata._owner is None


# Generated at 2022-06-13 08:58:18.102061
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    r = RoleMetadata()
    result = r.deserialize({"allow_duplicates": False, "dependencies": []})
    assert result is None
    assert isinstance(r, RoleMetadata)
    assert not r.allow_duplicates
    assert isinstance(r.dependencies, list)
    assert not r.dependencies

# Generated at 2022-06-13 08:58:23.765298
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    m = RoleMetadata.load({'dependencies': ['role1', {'src':'path/to/role2', 'name':'role2'}]}, owner='an owner')
    assert m._dependencies[0] == 'role1'
    assert m._dependencies[1].get('src') == 'path/to/role2'
    assert m._dependencies[1].get('name') == 'role2'

# Generated at 2022-06-13 08:58:31.149293
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    r = RoleMetadata()
    r.deserialize(data=dict(allow_duplicates=True, dependencies=[dict(role='test_role')]))
    assert r.allow_duplicates is True
    assert len(r.dependencies) == 1
    assert r.dependencies[0]['role']=='test_role'

# Generated at 2022-06-13 08:58:37.792994
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    my_metadata = RoleMetadata()
    assert isinstance(my_metadata, RoleMetadata)
    assert my_metadata._allow_duplicates == False
    assert my_metadata._dependencies == []
    assert my_metadata._galaxy_info == None
    assert my_metadata._argument_specs == dict()

# Generated at 2022-06-13 08:58:41.566824
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    # ---- Fixtures ----

    # ---- Test code ----
    m = RoleMetadata()
    serialize_m = m.serialize()
    # ---- Assertions ----
    # callable: RoleMetadata.serialize
    assert callable(RoleMetadata.serialize)
    # type: RoleMetadata.serialize -> dict
    assert isinstance(serialize_m, dict)

# Generated at 2022-06-13 08:58:45.228171
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    """
    tests if the serialize method works as expected.
    """
    from ansible.playbook.role.definition import RoleDefinition

    test_role = RoleDefinition.load({}, play=None, variable_manager=None, loader=None)
    role_metadata = RoleMetadata(owner=test_role).load({})
    assert role_metadata.serialize() == {u'allow_duplicates': False, u'dependencies': []}

# Generated at 2022-06-13 08:58:51.248130
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    import os
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.utils.collection_loader import AnsibleCollectionLoader
    from ansible.vars.manager import VariableManager
    from ansible.vars.unsafe_proxy import UnsafeProxy

    collection_path = os.path.join(os.path.dirname(__file__), '../collections')
    collection_loader = AnsibleCollectionLoader()
    collection_loader.set_collection_paths(collection_path)

    v = VariableManager(loader=collection_loader)

    def test_play_role_load():
        fake_loader = collection_loader._loader
        fake_loader.path_matches = {}
        fake_loader

# Generated at 2022-06-13 08:58:57.196458
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    
    print("\n === Begin Test for constructor of class RoleMetadata === \n")
    from ansible.playbook.role import Role
    role = Role()
    role_metadata = RoleMetadata(owner = role)
    assert role_metadata
    if role_metadata:
        print("Test for constructor of class RoleMetadata --- Pass\n")
    else:
        print("Test for constructor of class RoleMetadata --- Fail\n")


# Generated at 2022-06-13 08:59:05.372561
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    from ansible.playbook.role import Role
    from ansible.module_utils.six import StringIO

    a = StringIO("""
    allow_duplicates: yes
    dependencies:
      - { role: webserver, some_variables: foo }
      - { name: common }
      - database
      - { src: git+https://github.com/geerlingguy/ansible-role-firewall@master }
    galaxy_info: { description: "Common role for monitoring servers." }
    """)

    data = yaml.safe_load(a)
    role = Role()

    metadata = RoleMetadata(owner=role)

    metadata.load(data, variable_manager=None, loader=None)
    import pdb; pdb.set_trace()

# Generated at 2022-06-13 09:01:26.019454
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    role_list=list()
    owner=None
    role_meta_data=RoleMetadata(owner=owner)
    # Test __init__() and load()
    role_meta_data._load_dependencies(role_list, False)
    role_meta_data.deserialize(dict())
    role_meta_data.serialize()

# Generated at 2022-06-13 09:01:28.888301
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    data = {
        'allow_duplicates': True,
        'dependencies': [
            {'name': 'sample', 'src': 'git@example.com:sample.git'}
        ]
    }

    role = RoleMetadata()
    role.load_data(data)
    assert role.serialize() == data

# Generated at 2022-06-13 09:01:40.485360
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.playbook.play import Play
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.tests.unit.test_play import TestPlay
    from ansible.playbook.tests.unit.mock.loader import DictDataLoader


# Generated at 2022-06-13 09:01:49.134360
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.playbook.role.definition import RoleDefinition
    meta_main_dict = dict(
        allow_duplicates=False,
        dependencies=[
            dict(role=RoleDefinition("test_role1")),
            dict(role=RoleDefinition("test_role2")),
            'test_role3'
        ],
    )
    def_role1 = RoleDefinition("test_role1")
    def_role2 = RoleDefinition("test_role2")
    role_meta = RoleMetadata.load(meta_main_dict, owner=def_role1)

    assert role_meta.allow_duplicates == False
    assert len(role_meta.dependencies) == 3

# Generated at 2022-06-13 09:01:58.568649
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from collections import namedtuple
    from ansible.playbook.role import definition

    Role = namedtuple('Role', ['_role_name'])
    Role._role_path = None
    Role._role_collection = None
    Role._collections = None
    Role._play = None

    host_var = dict(name='foo')

    Role.get_name = lambda self: self._role_name

    role_def1 = definition.RoleInclude()
    role_def1.role_name = host_var

    role_def2 = definition.RoleInclude()
    role_def2.role_name = host_var

    role_def3 = definition.RoleInclude()
    role_def3.role_name = 'foo'


# Generated at 2022-06-13 09:02:08.660033
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    # test generation of RoleMetadata object by passing metadata in dict format
    from ansible.playbook.role import Role

    my_dependencies = [{'role': 'ansible.legacy.role'}]
    metadata = {'dependencies': my_dependencies}
    my_role = Role()
    my_role._role_path = os.path.join(os.path.dirname(__file__), '../test_data/test_meta')
    my_metadata = RoleMetadata.load(metadata, my_role)
    assert my_metadata._dependencies == my_dependencies

    # test generation of RoleMetadata object by passing metadata in list format
    metadata = [{'role': 'ansible.legacy.role'}]
    my_metadata = RoleMetadata.load(metadata, my_role)
    assert my