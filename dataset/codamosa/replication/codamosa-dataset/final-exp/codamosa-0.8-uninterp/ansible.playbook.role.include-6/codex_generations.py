

# Generated at 2022-06-13 08:52:02.754550
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    pass

# Generated at 2022-06-13 08:52:03.571627
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    pass

# Generated at 2022-06-13 08:52:04.370632
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    pass

# Generated at 2022-06-13 08:52:13.916129
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    ri = RoleInclude()
    assert ri.load(None, None, None, None, None, None) == {}
    assert ri.load('' , None, None, None, None, None) == {}
    assert ri.load([], None, None, None, None, None) == {}
    assert ri.load('role', None, None, None, None, None) == {}
    assert ri.load({'name': 'role'}, None, None, None, None, None) == {}


# Generated at 2022-06-13 08:52:15.579914
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    pass

    # old style
    #assert False, "TODO"
    

# Generated at 2022-06-13 08:52:21.275388
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    ##################################################################################################################
    #
    #   RoleInclude.load(data, play, current_role_path=None, parent_role=None, variable_manager=None, loader=None)
    #
    ##################################################################################################################

    # To Do:
    pass

# Generated at 2022-06-13 08:52:28.477942
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():

    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext

    from ansible.playbook.task import Task

    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.plugins.loader import load_callback_plugins
    from ansible.plugins.loader import load_connection_plugins

    from ansible.executor.playbook_executor import PlaybookExecutor

    class MyTask(Task):

        def __init__(self):
            super(MyTask, self).__init__()

        def _load_name_from_data(self, ds):
            pass

       

# Generated at 2022-06-13 08:52:38.186376
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    class Play(object):
        pass

    class VariableManager(object):
        def __init__(self):
            self.extra_vars = {}

    class Loader(object):
        def load_from_file(self, file_name, file_name2=None, tmp_dir=None):
            pass

    play = Play()
    play.use_task_filters = False
    play.use_role_filters = False
    play.role_debug = False
    vars = VariableManager()
    loader = Loader()
    role_basedir_one = os.getcwd()
    role_basedir_two = os.path.abspath('/')
    role_basedir_three = os.path.abspath('../')

# Generated at 2022-06-13 08:52:39.562327
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    assert False, "Test not implemented"

# Generated at 2022-06-13 08:52:41.951696
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    ri = RoleInclude()
    data = {"role": "elasticsearch"}
    ri.load(data, None)

# Generated at 2022-06-13 08:52:53.173930
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook.play import Play
    from ansible.playbook.role import Role
    from ansible.vars.manager import VariableManager
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.mod_args import ModuleArgsParser
    from ansible.utils.vars import combine_vars
    from ansible.utils.vars import combine_hash
    from ansible.inventory.manager import InventoryManager
    from ansible.utils.collection_loader import AnsibleCollectionConfig
    from ansible.module_utils._text import to_bytes

    module_parser = ModuleArgsParser(None, collection_list=AnsibleCollectionConfig.instance())

    # Define Inventory
    inventory = InventoryManager(loader=AnsibleLoader(None))

# Generated at 2022-06-13 08:53:03.798053
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.parsing.dataloader import DataLoader
    inventory = Inventory(loader=DataLoader(), variable_manager=VariableManager(),  host_list='/dev/null')

    # role definition with role name
    role_definition_with_name = '''
---
- name: test_role
  include:
    name: webservers
  become: yes
  become_method: sudo
  become_user: root
  check_mode: yes
  gather_facts: yes
  delegate_to: localhost
  delegate_facts: yes
'''

    # role definition with role path

# Generated at 2022-06-13 08:53:13.190955
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    import ansible.plugins.loader as plugin_loader
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.vars.manager import VariableManager
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group

    ansible_loader = DataLoader()
    host_vars = dict()
    host_vars['futurama'] = {
        'job': 'Delivery Boy',
        'species': 'Human',
    }
    host_vars['bender'] = {
        'job': 'Bending Unit',
        'species': 'Robot',
    }

    hosts = [Host(name='futurama')]

# Generated at 2022-06-13 08:53:21.071104
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():

    # Test string that should fail
    data_to_test = 'string'
    expected_result = "Invalid role definition"
    try:
        RoleInclude.load(data_to_test, None)
    except AnsibleError as e:
        assert expected_result in to_native(e)
    else:
        assert False

    # Test that should pass
    data_to_test = {
        'role': 'test',
        'vars': {'a': 'b'}
    }
    ri = RoleInclude.load(data_to_test, None)
    data_expected = 'test'
    assert data_expected == ri.get_name()

# Generated at 2022-06-13 08:53:21.790733
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    pass

# Generated at 2022-06-13 08:53:30.157070
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():

    ri = RoleInclude()
    data = {
            'role': 'test_role',
            'tasks': ['task1', 'task2']
           }
    new_ri = ri.load(data, {})

    assert new_ri.name == 'test_role'
    assert isinstance(new_ri.tasks, list) and len(new_ri.tasks) == 2 and new_ri.tasks[0] == 'task1'

# Generated at 2022-06-13 08:53:31.294110
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    RoleInclude.load("Vinay.Demo",None,None,None,None)

# Generated at 2022-06-13 08:53:39.281386
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.plugins.loader import collection_loader
    from ansible.playbook.play import Play
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.host import Host
    from ansible.vars import VariableManager
    from ansible.playbook.role.requirement import RoleRequirement

    my_playbook = Play.load(dict(
        name = "test playbook",
        hosts = "test",
        gather_facts = "no",
        roles = [
            "test_role",
        ],
    ), variable_manager=VariableManager(), loader=DataLoader())

    current_role_path = "path_to_currrent_role"


# Generated at 2022-06-13 08:53:49.184938
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.vars.manager import VariableManager

    pc = PlayContext()
    play = Play().load({}, variable_manager=VariableManager(), loader=None, play_context=pc)

    ri = RoleInclude(play=None, role_basedir=None, variable_manager=None, loader=None)
    assert(ri.load({}, None, None, None, None, None) is ri)
    ri = RoleInclude.load('foo', None, None, None, None, None)
    assert(isinstance(ri, RoleRequirement))
    assert(ri.get_name() == 'foo')
    assert(ri.get_role_path() is None)


# Generated at 2022-06-13 08:53:54.542262
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    _ri = RoleInclude()
    assert isinstance(_ri.load('name: test'), RoleInclude)
    assert isinstance(_ri.load({'name': 'test'}), RoleInclude)
    try:
        _ri.load(['name: test', 'name: test2'])
    except AnsibleParserError:
        pass

# Generated at 2022-06-13 08:54:06.069266
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    # valid
    assert isinstance(RoleInclude.load({}, "play_name"), RoleInclude)
    assert isinstance(RoleInclude.load("role_name", "play_name"), RoleInclude)
    assert isinstance(RoleInclude.load(RoleRequirement("role"), "play_name"), RoleInclude)

    # invalid
    raised = False
    try:
        RoleInclude.load([], "play_name")
    except AnsibleParserError:
        raised = True
    assert raised is True

    raised = False
    try:
        RoleInclude.load(1, "play_name")
    except AnsibleParserError:
        raised = True
    assert raised is True


# Generated at 2022-06-13 08:54:12.787024
# Unit test for method load of class RoleInclude

# Generated at 2022-06-13 08:54:24.070463
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():

    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    variable_manager = VariableManager()
    loader = DataLoader()
    play_context = PlayContext()
    playbook = Play().load({
        'name': 'myplay',
        'hosts': 'dummy',
        'gather_facts': 'no',
        'roles': [
            {
                'name': "myrole",
                'tasks': [
                    {
                        'name': 'mytask'
                    }
                ]
            }
        ]
    }, variable_manager=variable_manager, loader=loader)


# Generated at 2022-06-13 08:54:34.697769
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    
    role_path = '../../../../test/data/ansible_collections/ansible/collection_one'

    # Create a fake Ansible Playbook
    class StubPlaybook:
        pass
    fake_playbook = StubPlaybook()
    
    # Create a fake Variable Manager
    class StubVariableManager:
        pass
    fake_variable_manager = StubVariableManager()
    
    # Create a fake Collection List
    class StubCollectionList:
        pass
    fake_collection_list = StubCollectionList()

    # Create a valid role definition string
    valid_role_definition_string = 'test_role'

    # Create a valid role definition dict
    valid_role_definition_dict = dict()
    valid_role_definition_dict['name'] = 'test_role'

# Generated at 2022-06-13 08:54:35.154052
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    pass

# Generated at 2022-06-13 08:54:47.147574
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    import os
    import tempfile
    from ansible.errors import AnsibleError
    from ansible.parsing.yaml.objects import AnsibleUnicode, AnsibleMapping
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.role.requirement import RoleRequirement
    from ansible.playbook.role.include import RoleInclude

    ri = RoleInclude()
    data_str = b'invalid yaml'
    try:
        ri.load_data(data_str)
    except AnsibleParserError as e:
        assert 'malformed data' in to_native(e)
    data_str = 'invalid_role'

# Generated at 2022-06-13 08:54:47.738877
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    pass

# Generated at 2022-06-13 08:54:57.346320
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    import unittest
    import ansible.playbook.role.include
    class MockPlay(object):
        pass
    class MockVariableManager(object):
        def __init__(self):
            self.data = {}
        def set_variable(self, name, value):
            self.data[name] = value
        def get_variable(self, name):
            return self.data.get(name)
    class MockLoader(object):
        pass
    class MockCollectionList(object):
        pass

    mock_play = MockPlay()
    mock_variable_manager = MockVariableManager()
    mock_loader = MockLoader()
    mock_collection_list = MockCollectionList()

    # Test load with invalid data type

# Generated at 2022-06-13 08:54:58.109716
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    assert True

# Generated at 2022-06-13 08:55:09.031947
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    try:
        ri = RoleInclude.load(data='foo')
    except AnsibleError as e:
        print('AnsibleError: %s' % e)

    try:
        ri = RoleInclude.load(data=',')
    except AnsibleError as e:
        print('AnsibleError: %s' % e)

    try:
        ri = RoleInclude.load(data=123)
    except AnsibleParserError as e:
        print('AnsibleParserError: %s' % e)

test_RoleInclude_load()


# class RoleInclude:
#
#     """
#     A derivative of RoleDefinition, used by playbook code when a role
#     is included for execution in a play.
#     """
#
#     __slots__ = [
#        

# Generated at 2022-06-13 08:55:29.932412
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    current_role_path = '/tmp/roles/test_role'
    data = dict(name='test_role', src='/tmp/roles/test_role')
    play = dict(
        hosts='localhost',
        gather_facts='no',
        become='no'
    )
    collection_list = None
    role = RoleInclude.load(data=data,
                            play=play,
                            current_role_path=current_role_path,
                            parent_role=None,
                            variable_manager=None,
                            loader=None,
                            collection_list=collection_list)
    assert role.get_name() == data.get('name')
    assert role.get_role_path() == data.get('src')


# Generated at 2022-06-13 08:55:39.685734
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook.play import Play
    from ansible.variable_manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.task import Task

    variable_manager = VariableManager()
    loader = DataLoader()
    play = Play.load(dict(
        name="test play",
        hosts='localhost',
        gather_facts='no',
        roles=[]
    ), variable_manager=variable_manager, loader=loader)

# Generated at 2022-06-13 08:55:45.680313
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    # Test Case 1: "load" method works with no params,
    # variable_manager and loader have default values

    role_basedir = './'
    var_mgr = None
    loader = None
    collection_list = None

# Generated at 2022-06-13 08:55:57.217126
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook.play_context import PlayContext

    # literal load
    ri = RoleInclude.load("my_role_name", None)
    assert isinstance(ri, RoleInclude)
    assert ri.role_name == "my_role_name"
    assert ri.role_path == "my_role_name"

    # literal load from parent role, using local path
    ri = RoleInclude.load("my_role_name", None, "/roles/parent_role")
    assert isinstance(ri, RoleInclude)
    assert ri.role_name == "my_role_name"
    assert ri.role_path == "my_role_name"

    # literal load from parent role, using full path

# Generated at 2022-06-13 08:56:12.952872
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    ri = RoleInclude()
    play_context = PlayContext()
    play_source =  dict(
        name = "Ansible Play",
        hosts = 'webservers',
        gather_facts = 'no',
        tasks = [
            dict(action=dict(module='ping', args=''), register='ping_results'),
        ]
    )
    play = Play().load(play_source, variable_manager=VariableManager(), loader=DataLoader())

# Generated at 2022-06-13 08:56:19.674018
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook import Play
    from ansible.playbook.play_context import PlayContext
    data = {'role': 'test_role'}
    play = Play.load(data, variable_manager=None, loader=None)
    ri = RoleInclude(play=play, role_basedir=None, variable_manager=None, loader=None, collection_list=None)
    ri.load(data, play, current_role_path=None, parent_role=None, variable_manager=None, loader=None, collection_list=None)
    assert ri.get_name() == 'test_role'

# Generated at 2022-06-13 08:56:25.778508
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    
    from ansible.playbook.play_context import PlayContext
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    
    
    import os
    import sys
    
    from collections import namedtuple
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.yaml.objects import AnsibleUnicode, AnsibleSequence, AnsibleMapping
    file_path = os.path.dirname(__file__)
    sys.path.insert(0, file_path)
    from ansible.module_utils._text import to_bytes, to_text
    
    
    
    loader = DataLoader()
    
    passwords = {}
    

# Generated at 2022-06-13 08:56:26.600647
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    # external usage of load function in RoleInclude class
    assert True

# Generated at 2022-06-13 08:56:32.604488
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():

    data = {
        'name': 'role',
        'tasks': [
            {'debug': {'var': 'hi'}},
        ],
    }

    test_role_include = RoleInclude()
    role_include_dict = test_role_include.load_data(data)
    assert role_include_dict['name'] == 'role'
    assert role_include_dict['tasks'][0]['debug']['var'] == 'hi'

# Generated at 2022-06-13 08:56:40.879244
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    variable_manager = VariableManager()
    loader = DataLoader()
    loader.set_basedir(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', '..'))
    inventory = InventoryManager(loader=loader, sources='localhost,')
    variable_manager.set_inventory(inventory)
    play_context = PlayContext()
    variable_manager.set_play_context(play_context)

    # Normal test

# Generated at 2022-06-13 08:57:07.925019
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    # test_role = RoleInclude(play='', role_basedir='', variable_manager=None, loader=None, collection_list=None)
    test_data = {}
    # test_role.load_data(data=test_data, variable_manager=None, loader=None)
    # TODO: Implement test_RoleInclude_load.
    pass


# Generated at 2022-06-13 08:57:18.973659
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook import Play
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    # Setup
    dataloader = DataLoader()

    variable_manager = VariableManager()
    variable_manager.extra_vars = {'inventory_dir': os.path.join(os.path.dirname(__file__), '..', '..', 'inventory'),
                                   'inventory_file': 'test_inventory'}
    inventory = InventoryManager(loader=dataloader, sources="{inventory_dir}/{inventory_file}".format(**variable_manager.extra_vars))
    variable_manager.set_inventory(inventory)


# Generated at 2022-06-13 08:57:22.993002
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():

    # data is a string
    data = 'role'

    # . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
    # Step 1: data is a string

    play = None
    current_role_path = None
    parent_role = None
    variable_manager = None
    loader = None
    collection_list = None

    # Method load is called
    results = RoleInclude.load(data=data, play=play, current_role_path=current_role_path, parent_role=parent_role, variable_manager=variable_manager, loader=loader, collection_list=collection_list)

    # Tests the results

# Generated at 2022-06-13 08:57:28.803806
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    # Sample data to load via classmethod
    data = {
        'name': 'apache',
    }

    # Call method load of class RoleInclude
    ri = RoleInclude.load(data, None, None, None, None, None, None)

    assert isinstance(ri, RoleInclude)
    assert ri._role_name == 'apache'

# Generated at 2022-06-13 08:57:35.516609
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook.play import Play
    from ansible.playbook.role.requirement import RoleRequirement

    my_play = Play().load({
        "name": "test play",
        "hosts": "all",
        "gather_facts": True,
        "roles": {
            "test": {
                "name": "role_name",
                "become": False,
                "vars": {
                    "a": 1,
                },
                "tasks": [
                    dict(action=dict(module="command", args="uname -a"), register="uname_output"),
                ]
            }
        }
    }, variable_manager={}, loader=None)


# Generated at 2022-06-13 08:57:36.388036
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    pass

# Generated at 2022-06-13 08:57:47.083736
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    '''
    unit test for method load of class RoleInclude
    '''
    from ansible.playbook.play import Play
    from ansible.playbook.role.include import RoleInclude
    from ansible.playbook.task.include import TaskInclude
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.playbook.block import Block
    loader, inventory, variable_manager = setup_loader()
    variable_manager.set_inventory(inventory)
    current_role_path = u'~/ansible-example/roles/common'

# Generated at 2022-06-13 08:57:54.512897
# Unit test for method load of class RoleInclude
def test_RoleInclude_load(): # lgtm [py/similar-function]
    # pylint: disable=unused-variable,invalid-name
    def _verify_function(role_name, role_path, expected_result, params, file_tree=None, loader=None, collection_list=None):
        if file_tree:
            loader.file_tree = file_tree
        if loader is None:
            # lgtm [py/unused-local-variable]
            loader = DictDataLoader({})
        if collection_list is None:
            collection_list = []

        base_role_path = os.getcwd() + os.sep + "roles"

        class MockPlay(object):
            _file_name = "mock_play.yml"
            _basedir = os.getcwd()


# Generated at 2022-06-13 08:58:04.653972
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook.play import Play
    from ansible.parsing.mod_args import ModuleArgsParser
    from ansible.vars import VariableManager

    module_args_parser = ModuleArgsParser()

    play_source = dict(
        name="Ansible Play",
        hosts='all',
        gather_facts='no',
        tasks=[
            dict(action=dict(module='shell', args='ls'), register='shell_out'),
            dict(action=dict(module='debug', args=dict(msg='{{shell_out.stdout}}')))
        ]
    )

    play = Play().load(play_source, variable_manager=VariableManager(), loader=None)

# Generated at 2022-06-13 08:58:11.303372
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    import ansible.constants as C
    from ansible.plugins.loader import role_loader

    # Using a playbook as role_basedir to test when role_basedir is a playbook file
    playbook_path = "/playbook/directory/playbook.yml"
    play_data = dict(
        name="Ansible Play",
        hosts='all',
        gather_facts='no',
        tasks=[
            dict(action=dict(module='setup', args=dict()))
        ]
    )

    # Using a directory as role_basedir to test when role_basedir is a directory
    role_basedir_path = os.path.join(C.DEFAULT_ROLES_PATH, "role_name")

    # A dictionary representing a role definition loaded from a play

# Generated at 2022-06-13 08:58:52.707341
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    '''
        RoleInclude:
            - test_role

        RoleInclude:
            role: test_role
    '''

    pass

# Generated at 2022-06-13 08:59:02.286079
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    """
    Load the role definition, role should be strict.
    """
    import os
    import pytest
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.role.requirement import RoleRequirement
    from ansible.parsing.dataloader import DataLoader

    data = {
        'name': 'test',
        'strict': True,
        'tasks': [
            {'debug': {'msg': 'hello world'}}
        ]
    }

    # Since we are only doing one test for method load of the class RoleInclude
    # We can use the same dummy play object for testing.
    PL = Play()
    # PL.load is also tested

# Generated at 2022-06-13 08:59:06.839677
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    '''
    (string) -> object

    :param data:
    :param play:
    :param current_role_path:
    :param parent_role:
    :param variable_manager:
    :param loader:
    :return:
    '''
    play = None
    current_role_path = None
    parent_role = None

    data = '[{"role_name": "myrole", "role_path": "../myrole", "role_action": ["install"]}]'
    RoleInclude.load(data, play, current_role_path, parent_role)
    #print(result)
    return

if __name__ == "__main__":
    test_RoleInclude_load()

# Generated at 2022-06-13 08:59:07.253554
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    pass

# Generated at 2022-06-13 08:59:14.120433
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    import ansible.constants as C

    loader = DataLoader()
    inventory = Inventory(loader=loader, variable_manager=VariableManager(), host_list=C.DEFAULT_HOST_LIST)
    datastr = '''
    - name: test.yml
      hosts: test
      roles:
        - rolea
        - roleb
    '''
    data = loader.load(datastr)
    data = data[0]
    play = data.get_children()[0]
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    loader.set_basedir('/tmp/ansible-test')

# Generated at 2022-06-13 08:59:31.334782
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    # Test for "Invalid role definition" exception
    # We need to mock on load_data method here, because method load_data
    # will be tested later
    from ansible.playbook.role.include import RoleInclude
    from ansible.playbook.role.definition import RoleDefinition
    RoleInclude.load_data = RoleDefinition.load_data
    data = [1, 2, 3]
    # Test for "Invalid role definition" exception
    play = dict(name='test')
    try:
        RoleInclude.load(data, play, current_role_path=None, parent_role=None, variable_manager=None, loader=None, collection_list=None)
        assert False
    except AnsibleParserError:
        pass
    # Test for "Invalid old style role requirement" exception

# Generated at 2022-06-13 08:59:35.423284
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    # test string
    s = 'test'
    data = RoleInclude.load(data=s)
    assert data
    assert isinstance(data, string_types) and ',' not in data

    # test dict
    s = 'test_old_style,test_new_style'
    data = RoleInclude.load(data=s)
    assert data
    assert isinstance(data, string_types) and ',' in data

# Generated at 2022-06-13 08:59:41.054884
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    # data input for method load
    data = "galaxy/collection/package"
    current_role_path = '/opt/ansible/roles'
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    play = Play.load(dict(playbooks=[]), variable_manager=VariableManager(), loader=None)
    variable_manager = VariableManager()
    variable_manager._fact_cache = dict()
    variable_manager._fact_cache["ansible_facts"] = dict()
    variable_manager._fact_cache["ansible_facts"]['ansible_os_family'] = 'Linux'
    variable_manager._fact_cache["ansible_facts"]['ansible_distribution'] = 'RedHat'
   

# Generated at 2022-06-13 08:59:52.251196
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook import Play
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    loader = DataLoader()
    variable_manager = VariableManager()

    # string type data
    data = 'name'
    play = Play().load(dict(
        name = "test play",
        hosts = 'localhost',
        gather_facts = 'no',
        roles = [data]
    ), variable_manager=variable_manager, loader=loader)

    # string type data and variable
    data = 'name, {{ variable }}'
    play = Play().load(dict(
        name = "test play",
        hosts = 'localhost',
        gather_facts = 'no',
        roles = [data]
    ), variable_manager=variable_manager, loader=loader)

# Generated at 2022-06-13 08:59:59.782367
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
   role_name = '/Users/yzhang/ansible_test_suite/vault_test/test_file'
   my_play = 'play'
   my_role_basedir = 'role_basedir'
   my_variable_manager = 'variable_manager'
   my_loader = 'loader'
   my_collection_list = 'collection_list'

   ri = RoleInclude.load(role_name, my_play, my_role_basedir, my_variable_manager, my_loader, my_collection_list)
   print (ri)

# Generated at 2022-06-13 09:01:25.790189
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    data = {
        'tasks': [
            { 'name': 'test task' }
        ]
    }

    ri = RoleInclude()
    ri.load_data(data=data)
    assert len(ri.get_tasks()) == 1

# Generated at 2022-06-13 09:01:31.193900
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():

    class Play(object):
        task_vars = dict()
        def get_vars(self):
            return self.task_vars
        def set_vars(self, vars):
            self.task_vars = vars
        def __init__(self):
            self.task_vars = {
                    'included_role_tasks': [],
                    'tasks': [{
                        'first_task': True
                    }]
                }

    class VariableManager(object):
        def __init__(self, host_c=None):
            if host_c is None:
                host_c = VariableManager
            self.host_c = host_c

# Generated at 2022-06-13 09:01:44.821966
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():

    import shutil
    import tempfile
    import filecmp

    cur_dir = os.getcwd()

    # Create the basedir
    basedir = tempfile.mkdtemp()

    # Create the role dir
    role_dir = os.path.join(basedir, 'test_roles')
    os.mkdir(role_dir)
    os.chdir(role_dir)

    (ret, out, err) = module.run_command('git init')
    assert (ret == 0)
    assert (out == '')
    assert (err == '')

    (ret, out, err) = module.run_command('git config user.email "you@example.com"')
    assert (ret == 0)
    assert (out == '')
    assert (err == '')


# Generated at 2022-06-13 09:01:56.086969
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook.role.requirement import RoleRequirement
    from ansible.template import Templar
    from copy import deepcopy

    def do_test(role_yaml, role_path, role_name, role_tasks_path, role_vars):
        ri = RoleInclude()
        vm = DummyVars()
        vm.set_variable("role_name", role_name)

        ri.role_basedir = role_path
        ri.load_data(role_yaml)
        role_files_path = os.path.join(role_path, 'files')
        role_tasks_path = os.path.join(role_path, role_tasks_path)
        role_templates_path = os.path.join(role_path, 'templates')
        role_

# Generated at 2022-06-13 09:02:03.087271
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():

    data = {
        u'name': u'foo',
        u'include': u'bar'
    }

    def load_data(self, data, variable_manager=None, loader=None):
        self._role_name = data['name']
        self._role_path = data['include']
        return self

    class RoleIncludeWithMethod(RoleInclude):
        load_data = load_data

    class Play(object):
        pass

    play = Play()
    play.roles_path = ['/path/to/role']

    class VariableManager(object):
        def __init__(self):
            self.extra_vars = {}
            self.vars_cache = {}