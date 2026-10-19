

# Generated at 2022-06-13 08:52:11.510866
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    assert False

# Generated at 2022-06-13 08:52:17.817286
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    # Empty role load
    try:
        role_load('')
        assert False # it should raise an exception
    except AnsibleParserError as e:
        pass

    # Load a role requirement with all fields set
    path = '../test/test_roles/test_role_1'
    data = {'role': 'test_role_1', 'when': 'test_task_1'}
    role = role_load(data, path)
    assert role.get_name() == 'test_role_1'
    assert role.get_path() == path
    assert role.get_role_params() == data

    # Load a role requirement with minimal fields
    path = '../test/test_roles/test_role_2'
    data = 'test_role_2'

# Generated at 2022-06-13 08:52:20.521757
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    print("----------- Unit test start for RoleInclude -----------")

    print("----------- Unit test end for RoleInclude -----------")

# Generated at 2022-06-13 08:52:22.149519
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    # TODO: implement test method load of class RoleInclude
    pass

# Generated at 2022-06-13 08:52:34.656033
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():

    import unittest

    class TestClass(unittest.TestCase):

        def test_normal(self):

            from ansible.playbook.role.definition import RoleDefinition
            from ansible.playbook.play_context import PlayContext
            from ansible.parsing.dataloader import DataLoader

            class Play(object):

                def __init__(self):
                    self.name = 'test'
                    self.connection = None
                    self.context = PlayContext()
                    self.loader = DataLoader()

            class Playbook(object):

                def __init__(self):
                    self.name = 'test'
                    self.connection = None
                    self.context = PlayContext()
                    self.loader = DataLoader()

            def get_loader(*args, **kwargs):
                return DataLoader()


# Generated at 2022-06-13 08:52:46.321861
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    
    myLoader = DataLoader()
    myInventory = InventoryManager(loader=myLoader, sources=[])
    myVariableMgr = VariableManager(loader=myLoader, inventory=myInventory)
    
    myPlay = Play().load({'name': 'test_play'}, variable_manager=myVariableMgr, loader=myLoader)
    myRoleDef = RoleDefinition.load({'name': 'test_role'}, play=myPlay, variable_manager=myVariableMgr, loader=myLoader)
    
    myRoleInc = RoleIn

# Generated at 2022-06-13 08:52:49.550000
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():

    ri=RoleInclude()
    ri.load(data=data, play=play, current_role_path=current_role_path, parent_role=parent_role, variable_manager=variable_manager, loader=loader, collection_list=collection_list)

# Generated at 2022-06-13 08:53:00.538378
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.parsing.yaml.objects import AnsibleUnicode
    
    # test string
    data = 'test1.role'
    play = None
    current_role_path = None
    parent_role = None
    variable_manager = None
    loader = None
    collection_list = None
    ri = RoleInclude.load(data, play, current_role_path, parent_role, variable_manager, loader, collection_list)
    assert ri._role_name is None
    assert ri._role_path is None
    assert ri._role_name is None
    assert ri.get_name() == 'test1.role'
    assert ri.get_role_path() == 'test1.role'
    
    # test dict

# Generated at 2022-06-13 08:53:09.232112
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    role_data = {'role_test_data': [{'name':'test_role_name'}]}
    variable_manager = 'test_variable_manager'
    loader = 'test_loader'
    play = 'test_play'
    current_role_path = 'test_current_role_path'
    parent_role = 'test_parent_role'
    role_include = RoleInclude.load(role_data, play, current_role_path, parent_role, variable_manager, loader)
    assert(role_include.name == 'test_role_name')
    assert(role_include.role_basedir == 'test_current_role_path')


# Generated at 2022-06-13 08:53:16.316491
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    # Test RoleInclude load with valid string and dict data
    the_dict = {
        "role": "test_role_name"
    }
    the_str = "test_role_name"
    assert(RoleInclude.load(the_dict,None,None,None,None,None) is not None)
    assert(RoleInclude.load(the_str,None,None,None,None,None) is not None)
    # Test RoleInclude load with invalid string data
    the_dict.update({"role": "test_role_name,other_role_name"})
    assert(RoleInclude.load(the_dict,None,None,None,None,None) is None)
    # Test RoleInclude load with valid dict data
    the_dict.update({"role": "test_role_name"})

# Generated at 2022-06-13 08:53:26.479408
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    attribute = RoleInclude()
    role_name = attribute.load('name', play=None, current_role_path=None, parent_role=None, variable_manager=None, loader=None)
    assert role_name == 'name'
    role_name = attribute.load('name:role_name', play=None, current_role_path=None, parent_role=None, variable_manager=None, loader=None)
    assert role_name == 'role_name'

# Generated at 2022-06-13 08:53:33.037281
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.plugins.loader import collection_loader
    from ansible.vars.manager import VariableManager

    vm = VariableManager()

    role1 = RoleInclude.load("mynamespace.mycollection.myrole",
                             play=None,
                             current_role_path=None,
                             parent_role=None,
                             variable_manager=vm,
                             loader=collection_loader)

    print(role1)

    assert role1.role_name == "myrole"
    assert role1.role_path == "mynamespace/mycollection/myrole"

# Generated at 2022-06-13 08:53:36.235880
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    """
    Unit test for method load of class RoleInclude
    """
    data = "test_role"

    result = RoleInclude.load(data)

    assert isinstance(result, RoleInclude)

    data = {"test_role": {}}
    result = RoleInclude.load(data)
    assert isinstance(result, RoleInclude)

    data = {"role_name": {}}
    result = RoleInclude.load(data)
    assert isinstance(result, RoleInclude)



# Generated at 2022-06-13 08:53:42.734615
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    import yaml

    # Action: read yaml file
    with open(os.path.dirname(__file__) + '/test_data/test_RoleInclude_load.yml', 'r') as f:
        doc = yaml.safe_load(f)

        # Action: create a role include object
        role_include = RoleInclude()
        role_include.load_data(doc)

        # Assertion: the role include object's attributes (name, tasks, handlers, etc),
        #            is equal to the expected result.
        assert role_include.get_name() == 'test_role_include'
        assert role_include.get_default_vars() == {'key1': 'value1_overwrite'}

# Generated at 2022-06-13 08:53:50.472118
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    class TestPlaybook:
        pass

    playbook = TestPlaybook()
    playbook.vars = {}
    playbook.basedir = 'foo'

    class TestVariableManager:
        pass

    variable_manager = TestVariableManager()
    variable_manager.extra_vars = {'a': 1, 'b': 2}
    variable_manager._fact_cache = {'c': 3, 'd': 4}

    class TestLoader:
        pass

    loader = TestLoader()
    loader.get_basedir = lambda: 'ansible/playbooks'

    class TestCollectionLoader:
        pass

    collection_loader = TestCollectionLoader()
    collection_loader.collections = {'foo': 1, 'bar': 2}

    collection_list = [collection_loader]


# Generated at 2022-06-13 08:54:00.138327
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    import json
    from ansible.playbook.play import Play
    from ansible.playbook.role.requirement import RoleRequirement

    variable_manager = None
    loader = None
    collection_list = None

    play = Play().load(dict(
        name = "Ansible Play 1",
        hosts = 'localhost',
        tasks = [
        ]
    ), variable_manager=variable_manager, loader=loader, collection_list=collection_list)

    current_role_path = None
    parent_role = None


    if 1:
        # test string
        data = 'role1'

# Generated at 2022-06-13 08:54:08.360999
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook.play_context import PlayContext

    # RoleInclude without any fields
    data = ""
    play = PlayContext()
    ri = RoleInclude(play=play)
    assert isinstance(ri.load_data(data), RoleInclude)

    # RoleInclude with only meta/main.yml
    data = "meta/main.yml"
    play = PlayContext()
    ri = RoleInclude(play=play)
    assert isinstance(ri.load_data(data), RoleInclude)

    # RoleInclude with required fields
    data = "role: test\ndefine: meta/main.yml"
    play = PlayContext()
    ri = RoleInclude(play=play)
    assert isinstance(ri.load_data(data), RoleInclude)

   

# Generated at 2022-06-13 08:54:19.281257
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    import json
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins.loader import add_all_plugin_dirs
    from ansible.executor.task_queue_manager import TaskQueueManager
    add_all_plugin_dirs()

# Generated at 2022-06-13 08:54:28.356603
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():

    def test_function(param):
        print(param)

    import ansible.utils.collection_loader
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.vars.manager import VariableManager

    collection_loader = ansible.utils.collection_loader.CollectionsLoader()
    dfv = DataLoader()
    p = Play()
    vm = VariableManager()

    ri = RoleInclude(play=p,
                     role_basedir='/home/drusso/ansible/test1/roles',
                     variable_manager=vm,
                     loader=dfv,
                     collection_list=collection_loader)

    # test load()
    data = 'test-role'

# Generated at 2022-06-13 08:54:39.512069
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    import ansible.playbook.play
    import ansible.playbook.role.definition
    import ansible.playbook.role.requiremen
    import ansible.vars.manager
    import ansible.parsing.vault

    sample_hosts = '''
    localhost ansible_connection=local ansible_python_interpreter="/usr/bin/env python"
    '''
    sample_data = '''
    - hosts: host1
      gather_facts: False
      roles:
        - role1
        - role2
    '''


# Generated at 2022-06-13 08:54:51.922429
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    variable_manager = DummyVariableManager()
    loader = DummyLoader()
    collection_list = DummyCollectionList()
    play = DummyPlay()
    # 1. Role name is just a string and it should be transformed into a role requirement
    data = "test-role"
    ri = RoleInclude.load(data, play, variable_manager=variable_manager, loader=loader, collection_list=collection_list)
    assert isinstance(ri, RoleRequirement)
    # 2. Role name is just a string and it should be transformed into a role requirement
    data = "test-role,test-version"
    ri = RoleInclude.load(data, play, variable_manager=variable_manager, loader=loader, collection_list=collection_list)
    assert isinstance(ri, RoleRequirement)
    # 3. Role

# Generated at 2022-06-13 08:54:59.824018
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins.loader import variable_manager_loader

    variable_manager = variable_manager_loader.variable_manager()
    variable_manager.set_nonpersistent_facts(dict(a=1, b=2, c=3))
    variable_manager.set_facts(dict(a=1, b=2, c=3))
    play_context = PlayContext()
    play_context.network_os = 'ios'

    ri = RoleInclude(play=play_context, role_basedir=None, variable_manager=variable_manager, loader=None, collection_list=None)

    ri.load_data("myrole")

    assert ri.get_name() == 'myrole'


# Generated at 2022-06-13 08:55:11.301341
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.parsing.yaml.objects import AnsibleMapping
    from ansible.playbook.play import Play
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.vars import combine_vars
    from ansible.errors import AnsibleError

    variable_manager = VariableManager()
    loader = DataLoader()
    variable_manager.extra_vars = {}

    variable_manager.set_inventory(loader.load_from_file('hosts'))

    play_dict = dict(
        name='test_play',
        hosts='all',
        gather_facts='no',
        roles=[]
    )
    play_no_roles = Play.load

# Generated at 2022-06-13 08:55:19.501875
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():

    class RoleInclude_load_Mock(RoleInclude):
        def __init__(self, play=None, role_basedir=None, variable_manager=None, loader=None, subdirs=None):
            self.variable_manager = variable_manager
            self.loader = loader
            self.subdirs = subdirs
            self.play = play
            self.roles = dict()
            self.role_basedir = role_basedir

    class Play(object):
        pass

    ri = RoleInclude_load_Mock(play=Play(), role_basedir='role_basedir', variable_manager={}, loader={}, subdirs={})
    assert True == isinstance(ri.load_data('data', variable_manager={}, loader={}), Attribute)



# Generated at 2022-06-13 08:55:29.869700
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.playbook.block import Block
    from ansible.playbook.play import Play
    from ansible.playbook.role import Role
    from ansible.parsing.yaml.loader import AnsibleLoader

    dataloader = DataLoader()

    variable_manager = VariableManager()
    inventory = InventoryManager(loader=dataloader, sources=[])
    variable_manager.set_inventory(inventory)

    play_

# Generated at 2022-06-13 08:55:39.609865
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook.role.meta import RoleMetadata
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    # init
    fake_loader = DictDataLoader({
      "/path/to/imported/roles": {
        "file1.yml": "",
        "file2.yml": "",
      },
    })
    fake_inventory = InventoryManager(loader=fake_loader, sources='')
    fake_variable_manager = VariableManager(loader=fake_loader, inventory=fake_inventory)
    fake_play_context = PlayContext()

# Generated at 2022-06-13 08:55:45.641762
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook.play import Play
    from ansible.playbook.role import Role
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.role.requirement import RoleRequirement

    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.plugins.loader import role_loader

    # Setup the test
    role_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '..', '..', 'test', 'units', 'playbook', 'load_role',
                             'dependencies', 'required_roles_1')
    vars_manager = RoleDefinition._get_variable_manager()
    play = Play()

    # Test the method load
    play.load()


# Generated at 2022-06-13 08:55:51.956770
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible import inventory
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play

    ri = RoleInclude()
    ri.load(data="geerlingguy.nginx", play=Play(), loader=DataLoader(), variable_manager=VariableManager(inventory=inventory.Inventory()))

# Generated at 2022-06-13 08:55:56.263127
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():

    data = '- role: test'
    f = RoleInclude.load(data,play=None, current_role_path=None, parent_role=None, variable_manager=None, loader=None, collection_list=None)
    assert f._role_name == 'test'

# Generated at 2022-06-13 08:56:11.830826
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    import os, sys
    import unittest
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    from ansible.module_utils.six import string_types
    from ansible.playbook.role.include import RoleInclude
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.mod_args import ModuleArgsParser
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    import ansible.constants as C
    from ansible.plugins import module_loader
    import ansible.errors as errors


# Generated at 2022-06-13 08:56:24.911308
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    current_role_path = os.path.dirname(__file__)
    loader = None
    variable_manager = None
    collection_list = None
    play_mock, play_objs = mock_play()

    ri = RoleInclude()
    role_name = 'test_name'
    role_data = { 'role': role_name }

    result = ri.load(role_data, play=play_objs,
                     current_role_path=current_role_path,
                     variable_manager=variable_manager,
                     loader=loader, collection_list=collection_list)
    assert result.get_name() == role_name

    role_data = { 'role': role_name, 'become': 'True' }

# Generated at 2022-06-13 08:56:34.743239
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    import copy
    from ansible.playbook.play import Play

    class MockVariableManager(object):
        def __init__(self):
            self.vars = {}
        def set_nonpersistent_facts(self, host, vars):
            pass
        def include_vars(self, host, include_path, is_handlers=False, args=None):
            return {}
        def add_group_vars(self, host, group_name, vars):
            pass
        def set_host_variable(self, host, varname, value):
            pass
        def add_host_vars(self, host, vars):
            pass
        def set_host_fact(self, host, varname, value):
            pass

# Generated at 2022-06-13 08:56:44.863517
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    # required by script
    class Play(object):
        def __init__(self, basedir):
            self.basedir = basedir
            self.default_vars = {}
        def get_variable_manager(self):
            return None
    def get_basedir(self):
        return 'test/test_data/test_ansible_module'

    # init the play, use get_basedir to get the basedir
    play = Play(basedir=get_basedir(Play))

    # init the role include
    role_include = RoleInclude(play=play)

    # test invalid role definition, pass a list
    data = ['nest_directory', 'role_tasks', 'tasks.yml']

# Generated at 2022-06-13 08:56:48.696469
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    data = 'git'
    play = None
    current_role_path = './role'
    parent_role = None
    variable_manager = None
    loader = None
    collection_list = None

    RoleInclude.load(data, play, current_role_path, parent_role, variable_manager, loader, collection_list)


# Generated at 2022-06-13 08:57:05.600248
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    def createAttribute(attr):
        return Attribute.load(attr, Attribute(), None, None)
    def createRoleInclude(data, play, current_role_path, parent_role, variable_manager, loader):
        return RoleInclude.load(data, play, current_role_path, parent_role, variable_manager, loader)
    data_str = [
        "",
        "a_role",
        "a_role,foo=test,bar=test2,baz=test3",
        "a_role,when: test",
    ]
    for data_item in data_str:
        try:
            ri = createRoleInclude(data_item, None, None, None, None, None)
        except AnsibleError:
            assert data_item in ['', 'a_role']

# Generated at 2022-06-13 08:57:15.249583
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook.play_context import PlayContext
    class TestRoleInclude(RoleInclude):
        def __init__(self, play=None, role_basedir=None, variable_manager=None, loader=None, collection_list=None):
            super(TestRoleInclude, self).__init__(play=play, role_basedir=role_basedir, variable_manager=variable_manager, loader=loader, collection_list=collection_list)

    test_variable_manager = PlayContext()
    test_loader = None
    test_collection_list = []
    test_hosts = [{'hostname': 'SampleHost1'}, {'hostname': 'SampleHost2'}]
    test_name = 'Test Play'

# Generated at 2022-06-13 08:57:29.616267
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():

    from units.mock.loader import DictDataLoader
    from units.mock.path import mock_unfrackpath_noop

    from ansible.parsing.vault import VaultLib
    from ansible.vars.manager import VariableManager

    loader = DictDataLoader({})
    collection_list = []
    play = None
    current_role_path = None
    parent_role = None

    # test_RoleInclude_load_with_string
    data = 'geerlingguy.java'
    loader.mock_add_directory({}, '/etc/ansible/roles/geerlingguy.java')
    variable_manager = VariableManager()

# Generated at 2022-06-13 08:57:45.877980
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    """
    Test load method of class RoleInclude
    """
    # Test instantiation of class RoleInclude
    role_include = RoleInclude()

    # Test raise AnsibleError when load data is invalid
    args = ['2.4.0', [], {}, True, 'Test data' , False]
    for arg in args:
        try:
            RoleInclude.load(arg, None)
        except AnsibleError:
            continue
        raise Exception("Expected exception AnsibleError did not occur.")

    # Test raise AnsibleParserError when load data is invalid
    args = ['2.4.0, 1.4.0', {'role': '2.4.0, 1.4.0', 'name': 'Test name'}, '2.4.0, 1.4.0']

# Generated at 2022-06-13 08:57:53.987768
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook.play import Play
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    from ansible.utils.vars import combine_vars
    import os

    yaml_data = """
- hosts: testing
  roles:
    - { role: webservers, foo: '{{bar}}', other: '{{baz}}' }
    - { role: dataservers, another: '{{foo}}', bar: '{{baz}}' }
    - { role: monitoring }
    - { role: '{{foo}}' }
    - { role: baz, include_role: sub }
"""
    inv_data = {}
    results = {}

# Generated at 2022-06-13 08:57:54.523286
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    pass

# Generated at 2022-06-13 08:58:14.684446
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    data = {
        "name": 'testname',
        "role_path": 'testrolepath',
        "scenario": {'tags': ['testscenario']},
        "become_user": 'testbecomeuser'
    }
    play = Mock()
    variable_manager = Mock()
    loader = Mock()
    play.get_variable_manager.return_value = variable_manager
    variable_manager.get_vars.return_value = data
    ri = RoleInclude.load(data, play, variable_manager=variable_manager, loader=loader)
    assert ri._role_name == 'testname'
    assert ri._role_path == 'testrolepath'
    assert ri.scenario._tags == ['testscenario']

# Generated at 2022-06-13 08:58:15.153513
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    assert True

# Generated at 2022-06-13 08:58:21.031310
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    ri = RoleInclude()
    data = 'role1'
    role_basedir = '/example/roles'
    play = AnsiblePlaybook()
    res = ri.load(data, play, role_basedir)
    assert isinstance(res, RoleInclude)


# Generated at 2022-06-13 08:58:37.561476
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.role.metadata import RoleMetadata
    from ansible.vars.manager import VariableManager

    data = {}
    role_path = 'test/any'
    loader = DataLoader()
    role_cls = RoleInclude(role_basedir=role_path, loader=loader)
    role_cls.__class__._valid_attrs += ('tasks',)
    role_cls.__class__.tasks = FieldAttribute(isa='list')

    # Test with dict value
    data['tasks'] = [{'meta': 'dummy', 'name': 'task1'}]
    role_cls = role_cls.load(data=data, loader=loader)

    assert role_cls.tasks

# Generated at 2022-06-13 08:58:44.660311
# Unit test for method load of class RoleInclude

# Generated at 2022-06-13 08:58:46.606630
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    ri = RoleInclude.load('role1', play=None, current_role_path=None, parent_role=None, variable_manager=None, loader=None, collection_list=None)
    assert isinstance(ri, RoleInclude)


# Generated at 2022-06-13 08:58:49.612039
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    play = dict()
    data = dict()
    ri = RoleInclude(play=play);
    r = ri.load(data=data)
    assert(r is None)

# Generated at 2022-06-13 08:59:00.328430
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():

    from ansible.playbook.role.definition import RoleDefinition
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.plugins.loader import module_loader
    from ansible.plugins import module_loader

    data = "TestRole"
    play = "Test Play"
    current_role_path = "/home/ansible/playbooks/roles/"
    parent_role = ""
    variable_manager = "Test Variable Manager"
    loader = AnsibleLoader("", module_loader, variable_manager=variable_manager)

    # Test with valid string data
    role = RoleInclude.load(data, play, current_role_path, parent_role, variable_manager, loader)
    assert role.get_name() == data

    # Test with dictionary data

# Generated at 2022-06-13 08:59:07.615015
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    # create a RoleInclude instance with default parameters
    ri = RoleInclude()
    # test that an exception is raised when an invalid type of data is passed as a parameter
    with pytest.raises(AnsibleParserError) as exc:
        ri.load(data=object(), variable_manager=object(), loader=object())
    assert "Invalid role definition: " in to_native(exc.value)
    # test that an exception is raised when an old style role requirement is passed as a parameter
    with pytest.raises(AnsibleError) as exc:
        ri.load(data="role1,role2", variable_manager=object(), loader=object())
    assert "Invalid old style role requirement: " in to_native(exc.value)
    # test that an exception is raised when an invalid type of data is passed as a parameter

# Generated at 2022-06-13 08:59:14.381589
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    '''
    Testcase for method load of class RoleInclude
    '''
    from ansible.playbook.role.definition import RoleDefinition
    import os
    import sys
    import tempfile
    try:
        from ansible.module_utils.six.moves import configparser
    except Exception:
        from six.moves import configparser
    from ansible.module_utils.parsing.convert_bool import boolean
    from ansible.module_utils._text import to_text
    from ansible.module_utils.six import iteritems
    from ansible.module_utils.six import string_types
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    from ansible.playbook.attribute import FieldAttribute
    from ansible.playbook.play_context import PlayContext
   

# Generated at 2022-06-13 08:59:44.008118
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    import ansible.playbook.role.definition
    ri = ansible.playbook.role.definition.RoleInclude()
    ri.load()
    assert True

# Generated at 2022-06-13 08:59:55.150946
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():

    from ansible import errors
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    from ansible.parsing.yaml.parser import AnsibleParser
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins import module_loader, callback_loader
    from ansible.plugins.callback import CallbackBase, callbacks

    from units.mock.loader import DictDataLoader
    from units.mock.path import mock_unfrackpath_noop

    mock_unfrackpath_noop()

    variable_manager = mock.MagicMock()
    variable_manager.extra_vars = {}

    loader = DictDataLoader({})
    callbacks.default = CallbackModule()

    play_context = PlayContext()
    play_context.network_

# Generated at 2022-06-13 09:00:04.275994
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    import tempfile
    import shutil
    from ansible.playbook.play import Play


# Generated at 2022-06-13 09:00:04.774711
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    pass



# Generated at 2022-06-13 09:00:10.912709
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook.play import Play
    from ansible.playbook.role.definition import RoleDefinition

    test_play = Play()
    test_play.vars = dict()
    test_play.vars['ansible_ssh_user'] = "ansibleuser"
    test_play.vars['ansible_ssh_host'] = "ansiblehost"
    test_play.vars['ansible_become_user'] = "ansibleuser"
    test_play.vars['ansible_become_pass'] = "ansiblepwd"

    test_role_include = RoleInclude(play=test_play)
    test_role_include.vars = dict()
    test_role_include.vars['ansible_ssh_user'] = "ansibleuser"

# Generated at 2022-06-13 09:00:21.661292
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    """
    AnsibleRoleDefinition: load(data, play, current_role_path=None, parent_role=None, variable_manager=None, loader=None)

    We intentionally test loading of different data types instead of
    testing methods in multiple test functions.
    """
    from ansible.playbook.play import Play
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.vars.manager import VariableManager

    play = Play.load({'name': 'test_play'}, variable_manager=VariableManager(), loader=None)
    variable_manager = VariableManager()
    variable_manager.set_nonpersistent_facts({'role_path': '/test'})
    loader = None

    # Testing a role definition

# Generated at 2022-06-13 09:00:25.977019
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():

    class fake_data(object):
        def __init__(self, name, path):
            self.name = name
            self.path = path

        def _load(self):
            pass

        def __ne__(self, other):
            return not self.__eq__(other)

        def __eq__(self, other):
            return self.name == other.name and self.path == other.path

    class fake_roledefinition(object):

        def __init__(self, name, path, parent_role=None, filename=None,
                     _role=None, role_paths=[], search_paths=[]):
            self.name = name
            self.filename = filename
            self.path = path
            self.parent_role = parent_role
            self._role = _role
            self.role_

# Generated at 2022-06-13 09:00:35.809710
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    """
    This method tests load method of class RoleInclude.
    """
    from ansible.playbook import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.roles import RoleRequirement
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = None
    play_context = PlayContext()
    play = Play().load(dict(
        name="Ansible Play",
        hosts=['all'],
        gather_facts='no',
        tasks=[dict(action=dict(module='setup', args=''))]
    ), loader=loader, variable_manager=variable_manager)

# Generated at 2022-06-13 09:00:44.758394
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    data_member = "---\n- name: test me\n"
    data_dict = {"name" : "test me"}
    data_unknown = ""

    play = None
    role_basedir = None
    current_role_path = None
    parent_role = None
    variable_manager = None
    loader = None
    collection_list = None

    ri_member = RoleInclude.load(data_member, play, current_role_path, parent_role, variable_manager, loader, collection_list)
    ri_dict = RoleInclude.load(data_dict, play, current_role_path, parent_role, variable_manager, loader, collection_list)

# Generated at 2022-06-13 09:00:54.934231
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():

    from ansible.utils.display import Display
    from ansible.parsing.dataloader import DataLoader

    display = Display()
    loader = DataLoader()
    parser = AnsibleParser(loader=loader)
    current_role_path = "/home/username/playbook/roles/test-role"
    variable_manager = VariableManager()
    variable_manager.extra_vars = {'hostname': 'host1'}

    # Load String data with one role
    data = 'geerlingguy.apache'
    role_include = RoleInclude.load(data, play=None, current_role_path=current_role_path, parent_role=None, variable_manager=variable_manager, loader=loader)
    assert type(role_include) == RoleInclude

# Generated at 2022-06-13 09:01:58.951166
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():

    class FakeVariableManager(object):
        def __init__(self):
            self.truevar = True
            self.falsevar = False

    class FakeLoader(object):
        def __init__(self):
            pass

        def load_from_file(self, *args, **kwargs):
            pass

    fake_variable_manager = FakeVariableManager()
    fake_loader = FakeLoader()

    ri = RoleInclude()

    data = ''
    ri.load(data, variable_manager=fake_variable_manager, loader=fake_loader)

    data = {}
    ri.load(data, variable_manager=fake_variable_manager, loader=fake_loader)

    data = []
    ri.load(data, variable_manager=fake_variable_manager, loader=fake_loader)

    data = ''

# Generated at 2022-06-13 09:02:09.286275
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():

    from ansible.playbook import Play
    from ansible.vars import VariableManager

    import os
    import sys
    import unittest2 as unittest

    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.parsing.yaml.loader import AnsibleLoader

    class TestRoleInclude(unittest.TestCase):

        def setUp(self):
            self.variable_manager = VariableManager()
            self.loader = AnsibleLoader(None, variable_manager=self.variable_manager)

        def tearDown(self):
            pass
