

# Generated at 2022-06-13 08:10:03.797560
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    pass

# Generated at 2022-06-13 08:10:12.241408
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    data_load = {
        'listen': 'task:add_first_primary_database',
        'include': 'tasks/add_first_primary_database.yml',
        'name': 'Add a database for the first time'
    }

    assert HandlerTaskInclude.load(data_load) is not None

    data_check_options = {
        'listen': 'task:add_first_primary_database',
        'include': {
            'tasks': [
                'add_first_primary_database.yml',
                'additional_primary_database.yml'
            ]
        },
        'name': 'Add a database for the first time'
    }


# Generated at 2022-06-13 08:10:14.736511
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    data = {}
    block = {}
    role = {}
    task_include = {}
    variable_manager = {}
    loader = {}
    handler = HandlerTaskInclude.load(data, block, role, task_include, variable_manager, loader)

# Generated at 2022-06-13 08:10:16.883819
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    hti = HandlerTaskInclude()
    assert isinstance(hti, HandlerTaskInclude)
    assert isinstance(hti, Handler)
    assert isinstance(hti, TaskInclude)

# Generated at 2022-06-13 08:10:17.381749
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    assert False

# Generated at 2022-06-13 08:10:21.577301
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    data = dict(name='somename')
    block = 'block'
    role = 'role'
    task_include = 'task'
    variable_manager = 'vm'
    loader = 'ldr'

    handler = HandlerTaskInclude.load(data, block, role, task_include, variable_manager, loader)

    assert handler

# Generated at 2022-06-13 08:10:23.034532
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    test = HandlerTaskInclude()
    assert isinstance(test, TaskInclude)
    assert isinstance(test, Handler)

# Generated at 2022-06-13 08:10:23.379004
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    pass

# Generated at 2022-06-13 08:10:29.374712
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    print("Testing method load of class HandlerTaskInclude")
    hti = HandlerTaskInclude()
    data = dict()
    block = None
    role = None
    ti = None
    variable_manager = 4
    loader = 8
    res = hti.load(data,block,role,ti,variable_manager,loader)
    assert isinstance(res, HandlerTaskInclude)
    print("Success.")
    return


# Generated at 2022-06-13 08:10:43.799375
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    pass
#     from ansible.inventory.host import Host
#     from ansible.inventory.group import Group
#     from ansible.vars import VariableManager
#     from ansible.playbook.play_context import PlayContext

#     handler_task_include_load_1_variable_manager = VariableManager()
#     handler_task_include_load_1_play_context = PlayContext()
#     handler_task_include_load_1_loader = None

#     # host = Host()
#     # group = Group()
#     # group.name = 'test_hosts'
#     # handler_task_include_load_1_inventory.add_group(group)

#     handler_task_include_load_1_variable_manager.set_inventory(handler_task_include_load_1_inventory)


# Generated at 2022-06-13 08:10:54.823999
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    '''
    Unit test for method load of class HandlerTaskInclude
    '''
    # Create simple Ansible Playbook
    playbook_content = {
        'hosts': 'localhost',
        'name': 'Test playbook',
        'roles': [],
        'tasks': [
            {
                'name': 'A task',
                'include': 'tasks.yml',
                'remote_user': 'local',
                'connection': 'local'
            }
        ]
    }
    # Create a temporary directory for storing playbook content
    playbook_dir = tempfile.mkdtemp()
    # Create a playbook file in the temporary directory
    playbook_path = os.path.join(playbook_dir, 'test.yml')
    # Write content of playbook

# Generated at 2022-06-13 08:11:05.203353
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.plugins.loader import lookup_loader
    from ansible.plugins.loader import lookup_loader_private
    from ansible.plugins.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.inventory.host import Host
    inventory = InventoryManager(loader=lookup_loader, sources='localhost,')
    variable_manager = VariableManager()
    variable_manager._fact_cache = {}
    variable_manager._fact_cache_file = ''
    variable_manager._host_vars_files = {}
    variable_manager._host_vars_file_results = {}
    variable_manager._host_vars_files_timestamps = {}
    variable_manager._add_new_host(Host(name="localhost"))

# Generated at 2022-06-13 08:11:08.298506
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    # Test valid name
    h = HandlerTaskInclude(block=None, role=None, task_include=None)
    assert h.name == 'include'

# Generated at 2022-06-13 08:11:11.046620
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    handler = HandlerTaskInclude(
        block=None,
        role=None,
        task_include=None
    )

    assert handler is not None

# Generated at 2022-06-13 08:11:21.323118
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    from ansible.playbook import task as Task
    obj = HandlerTaskInclude(
        block=None,
        role=None,
        task_include=Task.TaskInclude(
            block=None,
            role=None,
            task_include=None,
            task_tags=None,
            when=None,
            _role=None,
            loop=None,
            loop_args=None,
            loop_with_items=[],
            delegate_to=None,
            loop_with_items_via="list"
        )
    )
    print(obj)


# Generated at 2022-06-13 08:11:23.840465
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    t = "---"
    role = "Test"
    handler = HandlerTaskInclude.load(t, role=role)
    assert handler.role == role
    assert handler.parent is None
    assert handler.static is False

# Generated at 2022-06-13 08:11:34.744364
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    # test case when the value of keywords is listen
    # create a class object
    t = HandlerTaskInclude()
    data = {u'listen': u'install_mysql', u'tags': [u'install_mysql']}
    handler = t.check_options(data, data)
    assert data == handler
    assert data == handler.get_vars()
    assert 'HandlerTaskInclude' == handler.__class__.__name__
    assert data['listen'] == handler.action

    # test case when the value of keywords is not listen
    data = {u'local_action': u'command /bin/echo hi', u'tags': [u'install_mysql']}
    handler = t.check_options(data, data)
    assert data == handler
    assert data == handler.get_vars()


# Generated at 2022-06-13 08:11:44.679132
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    data = dict(
        include = dict(
            tasks = 'new_tasks.yml'
        )
    )
    t = HandlerTaskInclude(block=dict(), role=None, task_include=None)
    handler = t.check_options(
        t.load_data(data, variable_manager=None, loader=None),
        data
    )
    assert isinstance(handler, Handler)
    assert handler.name == 'include'
    assert handler.static == True
    assert handler.loop is None
    assert handler.block is None
    assert handler.include == 'new_tasks.yml'
    assert handler.only_tags is None
    assert handler.run_once is None
    assert handler.notify is None
    assert handler.listen is None

# Generated at 2022-06-13 08:11:46.789797
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():

    # TODO: Mock the constructor, or refer to a real object in unit tests
    # TODO: Update the following to be in sync with the constructor
    h = HandlerTaskInclude()

# Generated at 2022-06-13 08:11:54.558310
# Unit test for method load of class HandlerTaskInclude

# Generated at 2022-06-13 08:12:05.388310
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    # passing host of type Host
    from ansible.inventory.host import Host
    from ansible.vars.manager import VariableManager
    from ansible.loader import DataLoader
    from ansible.playbook.task_include import TaskInclude

    h = Host('host_name')
    task_i = TaskInclude('p1')

    # passing data of type dict
    data = {}
    task_i_object = HandlerTaskInclude.load(data=data,
                                            block=None,
                                            role=None,
                                            task_include=task_i,
                                            variable_manager=VariableManager(),
                                            loader=DataLoader())

    assert task_i_object.__class__.__name__ == 'HandlerTaskInclude'
    assert task_i_object.static_vars == {}


# Generated at 2022-06-13 08:12:06.759250
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    assert HandlerTaskInclude() is not None


# Generated at 2022-06-13 08:12:07.245972
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    pass

# Generated at 2022-06-13 08:12:13.350834
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.parsing.dataloader import DataLoader

    yaml_data = '---\n- debug: msg="{{foo}}"\n  when: foo is defined\n'

    variable_manager = VariableManager()
    loader = DataLoader()
    inventory = Inventory(loader=loader, variable_manager=variable_manager)
    handler = HandlerTaskInclude.load(yaml_data, variable_manager=variable_manager, loader=loader)
    assert isinstance(handler, HandlerTaskInclude)

# Generated at 2022-06-13 08:12:22.192566
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    # Load data
    data = {
      'include': "main.yml",
      'listen': "something"
    }

    block = 0
    role = 0
    task_include = 0
    variable_manager = 0
    loader = 0

    # Try to call the method load
    try:
        ret = HandlerTaskInclude.load(data, block, role, task_include, variable_manager, loader)
    except:
        ret = None
    finally:
        assert ret != None

# Generated at 2022-06-13 08:12:32.204049
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.inventory.manager import InventoryManager
    from ansible.inventory.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.playbook.role import Role
    from ansible.playbook.task import Task
    from ansible.vars.manager import VariableManager

    h0 = Host(name='h0')
    h1 = Host(name='h1')
    g0 = Group(name='g0')
    g0.add_host(h0)
    g0.add_host(h1)
    i0 = InventoryManager()
    i0.add_group(g0)
    d0 = DataLoader

# Generated at 2022-06-13 08:12:34.293543
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    data = dict()

    t = HandlerTaskInclude()
    obj = t.load(data)

    assert obj is not None



# Generated at 2022-06-13 08:12:37.753979
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    # test_data_for_HandlerTaskInclude
    data = {"hosts": "localhost", "tasks": {"- name": "test_handler", "include": {"role": "test_role"}}}
    assert HandlerTaskInclude.load(data) is not None



# Generated at 2022-06-13 08:12:45.372756
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.inventory.group import Group
    from ansible.inventory.host import Host
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.role_include import IncludeRole
    
    loader = DataLoader()
    variable_manager = VariableManager()
    block = Block()
    role = IncludeRole('test/roles/role_name', loader=loader, variable_manager=variable_manager, use_handlers=True)
    task_include = TaskInclude.load(dict(include='test/tasks/task_name', static='try', when='True'))

# Generated at 2022-06-13 08:12:55.789683
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.playbook.role import Role
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.inventory.host import Host
    from ansible.vars import VariableManager
    from ansible.parsing.yaml.objects import AnsibleUnicode

    vars = VariableManager()
    vars.extra_vars = {'my_var': {}}
    include_task = Task()
    include_task._role = Role()
    include_task._role._role_name = 'my_role'

    block = Block()
    block.block  = [include_task]

# Generated at 2022-06-13 08:13:09.677452
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    """
    This is a unit test for method load of class HandlerTaskInclude.
    """
    # set up
    data = \
"""
- name: include handler
  include_handler:
    name: local_action
  tags:
    - always
  listen:
    - foo
    - bar
  run_once: true
"""
    block = None
    role = None
    task_include = None
    variable_manager = None
    loader = None

    expected_result = \
"""
- name: include handler
  include_handler:
    name: local_action
  tags:
    - always
  listen:
    - foo
    - bar
  run_once: true
"""
    # test

# Generated at 2022-06-13 08:13:13.981110
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    result = HandlerTaskInclude.load({'include': 'handler1.yml'})
    assert result.__class__.__name__ == 'HandlerTaskInclude'
    assert result._role is None
    assert result._block is None
    assert result._task_include is None

# Generated at 2022-06-13 08:13:28.019426
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    data = dict(
        include='test_template',
        with_items=[1,2,3],
        with_file='test_file',
        with_dict={'key1':'value1', 'key2':'value2'},
        with_sequence=[1,2,3,4,5],
        loop_control={'label':'test_label'}
    )

    variable_manager = []
    loader = None

    handler = HandlerTaskInclude.load(
        data=data, variable_manager=variable_manager, loader=loader
    )

    assert handler.include == data.get('include')
    assert handler.include_role == data.get('include_role')
    assert handler.include_tasks == data.get('include_tasks')

# Generated at 2022-06-13 08:13:32.472616
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    data = {
        "tasks": "tasks.yml",
    }

    handler_task_include = HandlerTaskInclude.load(data)
    assert handler_task_include is not None


# vim: set noexpandtab:

# Generated at 2022-06-13 08:13:36.404699
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    data = {
        'include': '/path/to/handler.yml',
        'listen': 'test_event'
    }

    t = HandlerTaskInclude.load(data)

    assert isinstance(t, Handler)
    assert isinstance(t, TaskInclude)
    assert t._task_include.is_handler

# Generated at 2022-06-13 08:13:43.617566
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    object_data = dict(
        name='Ansible Handler Sample', 
        listen='Ansible_Handler', 
        tasks=[
            dict(
                name='Task Sample',
                shell="echo 'Ansible Handler Sample Task'"
            ),
            dict(
                name='Task Sample with notify',
                ping="PONG",
                notify=["Ansible_Handler"]
            )
        ]
    )


# Generated at 2022-06-13 08:13:52.979718
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    # check if ansible.cfg is loaded
    config_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../source-code-analysis/ansible.cfg')
    assert os.path.isfile(config_file_path)
    # get config file
    config_file = open(config_file_path, "r")
    # read config file
    config_file_content = config_file.read()
    # close config file
    config_file.close()
    # get config file content
    # config_file_content = pytest.fixtures.config_file_content
    # get config data
    config_data = configparser.ConfigParser()
    config_data.read_string(config_file_content)
    # get config data from DEFAULT

# Generated at 2022-06-13 08:14:02.648356
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    import os
    import sys
    import yaml
    import json
    import pytest
    import types
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.block import Block
    from ansible.utils.vars import load_extra_vars
    from ansible.utils.vars import load_options_vars
    from ansible.errors import AnsibleParserError
    from ansible.plugins.loader import action_loader

    # Preparamos los parámetros para cargar los datos de la tarea
    parent_dir = os.path.abspath(os.path.join(__file__, '../..'))

# Generated at 2022-06-13 08:14:03.889461
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    pass


# Generated at 2022-06-13 08:14:08.373204
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    t = HandlerTaskInclude()
    obj = t.load( {"name": "test_task" }, block = Block(), role = Role(), task_include = TaskInclude(), variable_manager = VariableManager(), loader = None)
    return obj


# Generated at 2022-06-13 08:14:21.593316
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    print("Test of HandlerTaskInclude")
    t = HandlerTaskInclude(block=None, role=None, task_include=None, args=None)
    print("test_task_include: " + repr(t))

# Generated at 2022-06-13 08:14:23.826202
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    '''
    Test for instantiation of class HandlerTaskInclude.
    '''
    return HandlerTaskInclude()

# Generated at 2022-06-13 08:14:28.105169
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    handler = HandlerTaskInclude.load({
        'include': "dir1/dir2/file.yml",
        'listen': 'myhandler'})
    print('handler:', handler)

    handler = HandlerTaskInclude.load({
        'include': "dir1/dir2/file.yml",
        'listen': "myhandler"})
    print('handler:', handler)

# Generated at 2022-06-13 08:14:28.516222
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    HandlerTaskInclude()

# Generated at 2022-06-13 08:14:33.277114
# Unit test for method load of class HandlerTaskInclude

# Generated at 2022-06-13 08:14:36.824794
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    test_task_include = TaskInclude()
    test_handler_task_include = HandlerTaskInclude()
    print(test_handler_task_include)



# Generated at 2022-06-13 08:14:43.225393
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    data = dict(
        name = 'include_role',
        include = dict(
            name = 'role_name'
        )
    )
    block = None
    role = None
    task_include = None

    handler = HandlerTaskInclude.load(data, block=block, role=role, task_include=task_include)

    assert handler.name == data['name']

    assert type(handler.include) == dict
    assert handler.include == data['include']


# Test to validate args passed to __init__ method

# Generated at 2022-06-13 08:14:46.214837
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    """Unit test for method load of class HandlerTaskInclude"""
    # print('')
    # print('Test for method load of class HandlerTaskInclude')
    # print('Test for method load of class HandlerTaskInclude')
    handler_task_include = HandlerTaskInclude()
    # TODO



# Generated at 2022-06-13 08:14:57.094370
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.task import Task
    from ansible.playbook.included_file import IncludedFile
    from ansible.playbook.block import Block
    from ansible.playbook import Play
    from ansible.inventory.host import Host

    block = Block()
    task = Task()
    handler = Handler()
    task_include = TaskInclude()

    # test for 'block' type
    block_res = HandlerTaskInclude.load(data={'block': 'Test'}, block=block, task_include=task_include)
    assert(type(block_res) is IncludedFile)

    # test for 'task' type

# Generated at 2022-06-13 08:15:07.102575
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.parsing.mod_args import ModuleArgsParser

    # Load method of class HandlerTaskInclude should return Handler
    # instance for below dictionary.
    data = {
        'debug': 'msg="{{ myvar }} is the value"',
        'when': 'myvar is defined'
    }
    assert isinstance(HandlerTaskInclude.load(data), Handler)

    # HandlerTaskInclude.check_options should raise AnsibleParserError
    # if any of the valid keywords is not defined.
    data = {
        'include': 'some play'
    }
    bad_data = {
        'debug': 'msg="{{ myvar }} is the value"',
        'when': 'myvar is defined'
    }


# Generated at 2022-06-13 08:15:28.530010
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    assert False, "Unit test for method load of class HandlerTaskInclude not implemented"

# Generated at 2022-06-13 08:15:34.456512
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.playbook.block import Block
    from ansible.parsing.dataloader import DataLoader

    # Create a data loader
    loader = DataLoader()

    # Create a variable manager
    variable_manager = VariableManager()

    # Create a block
    block = Block()
    block._role = "common"
    block.vars = { 'listen_group_name' : 'web' }

    # Create a handler
    handler = HandlerTaskInclude.load({
        'block': 'common',
        'listen': '{{ listen_group_name }}',
        'from': 'common/handlers'},
        block=block, variable_manager=variable_manager, loader=loader)

    # Check handler
    assert handler.block == block
    assert handler._role == block._role
    assert handler.t

# Generated at 2022-06-13 08:15:44.149697
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    import unittest
    from ansible.inventory.host import Host
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.role import Role
    from units.mock.loader import DictDataLoader
    from units.mock.path import mock_unfrackpath_noop as mock_unfrackpath
    from ansible.vars.manager import VariableManager

    class TestHandlerTaskInclude(unittest.TestCase):

        def setUp(self):
            pass

        def tearDown(self):
            pass

        #def test_HandlerTaskInclude_load(self):
        #    import os
        #    from ansible.inventory.host import Host
        #    from ansible.playbook.block import Block
        #    from ansible.

# Generated at 2022-06-13 08:15:44.680352
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    pass

# Generated at 2022-06-13 08:15:46.102569
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    HandlerTaskInclude.load(data=None, block=None, role=None, task_include=None, variable_manager=None, loader=None)

# Generated at 2022-06-13 08:15:57.413184
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.inventory.host import Host
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.role import Role
    from ansible.playbook.play import Play
    from ansible.template import Templar

    host = Host(name='some_host.example.com')
    variable_manager = VariableManager()
    loader = DataLoader()
    play = Play().load({}, variable_manager=variable_manager, loader=loader)
    templar = Templar(loader=loader, variables=variable_manager)


# Generated at 2022-06-13 08:16:09.501908
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.block import Block
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.vars.manager import VariableManager
    import ansible.constants as C
    import os
    import sys

    thisdir = os.path.dirname(__file__)
    # inventory_dir = os.path.dirname(thisdir)

    # Stub inventory objects

# Generated at 2022-06-13 08:16:18.475765
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    class Object(object):

        def __init__(self):
            self.variable_manager = 1
            self.loader = 1
            self.handler_task_include = HandlerTaskInclude

    class MockLoader:
        def load_from_file(self, filename, attr):
            return filename + attr

    class MockVar:
        def add_task_include(self, filename):
            return filename

    mock_var = MockVar()
    mock_loader = MockLoader()
    obj = Object()
    # Valid include key
    obj.variable_manager = mock_var
    obj.loader = mock_loader
    data = {'include': 'filename', 'with_items': 'item'}

# Generated at 2022-06-13 08:16:19.550114
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    # TODO: need to make a real test here
    pass

# Generated at 2022-06-13 08:16:28.678765
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    data = {
        "listen": "GOOD",
        "include": ["/path/to/handler","other/handler"],
        "ignore_errors": True,
        "when": "sup"
    }

    # Setup task
    h = HandlerTaskInclude()

    # loadHandler
    result = h.load(data, "TEST", "TEST", "TEST", None, None)
    assert result["listen"] == "GOOD"

    assert result["name"] == "TEST-TEST"

    # Test for url type
    data = {
        "listen": "GOOD",
        "include": ["http://localhost:8080"],
        "ignore_errors": True,
        "when": "sup"
    }
    # Setup task
    h = HandlerTaskInclude()

    # loadHandler
