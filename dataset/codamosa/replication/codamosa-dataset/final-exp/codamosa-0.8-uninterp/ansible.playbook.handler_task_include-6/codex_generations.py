

# Generated at 2022-06-13 08:10:03.472869
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    handler = HandlerTaskInclude()
    assert isinstance(handler, HandlerTaskInclude)
    assert isinstance(handler, Handler)
    assert isinstance(handler, TaskInclude)

# Generated at 2022-06-13 08:10:07.472419
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    TaskInclude.VARIABLE_MANAGER = variable_manager
    HandlerTaskInclude.load(data, variable_manager=variable_manager)
    assert HandlerTaskInclude.VALID_INCLUDE_KEYWORDS == TaskInclude.VALID_INCLUDE_KEYWORDS.union(('listen',))


# Generated at 2022-06-13 08:10:13.004530
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    loader_mock = Mock()
    variable_manager_mock = Mock()
    block_mock = Mock()
    role_mock = Mock()

    t = HandlerTaskInclude(block=block_mock, role=role_mock)
    handler = t.load(dict(
        include_tasks='filename'
    ), block=block_mock, role=role_mock, variable_manager=variable_manager_mock, loader=loader_mock)

    assert handler.get_name() == 'filename'


# Generated at 2022-06-13 08:10:19.364114
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.inventory.group import Group
    from ansible.inventory.host import Host
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.hostvars import HostVars
    import ansible.constants as C
    import os

    file_name = 'handlertaskinclude_load.yml'
    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, sources=['localhost,'])

    print('+++> Begin of the unit test')
    print('--- Inventory ---')
    print(inventory.dump())

    print

# Generated at 2022-06-13 08:10:28.984927
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.inventory.host import Host
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    myhost = Host()
    myhost.name = "testhost"
    myhost.host_name = "testhost"

    loader = DataLoader()
    variable_manager = VariableManager()
    variable_manager.extra_vars = {'hostvars': {'testhost': {}}}

    # {"include": "task2.yml"}
    data = {
        'include': 'task2.yml'
    }
    result = HandlerTaskInclude.load(data, block=None, role=None, task_include=None, variable_manager=variable_manager, loader=loader)

    expected = HandlerTaskInclude()

# Generated at 2022-06-13 08:10:41.680784
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():

    data = {
        u'files': u'/path/to/files',
        u'name': u'handler_name',
        u'tags': [ u'tag1', u'tag2' ],
        u'notify': [ u'nginx' ]
    }

    handler = HandlerTaskInclude.load(data)

    assert handler.name == data[u'name']
    assert handler.tags == data.get(u'tags', [])
    assert handler.block == None
    assert handler.role == None
    assert handler.tasks == []

    expected_notifications = [('nginx', {'task_include': handler})]
    assert handler.notified_by == expected_notifications

# Generated at 2022-06-13 08:10:47.532394
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible import errors
    from ansible.inventory.host import Host

    from spec.utils import set_module_args

    obj = HandlerTaskInclude()

    def load_data(data, **kwargs):
        return data

    def check_options(self, data, data_copy):
        return data

    def get_listen_tasks(self, iterator):
        return []

    def add_tasks(self, tasks):
        pass

    def add_notify(self, task, handler):
        pass

    def _load_tasks(self, iterator):
        pass

    # No value for argument 'data'
    set_module_args({})
    with pytest.raises(errors.AnsibleError) as err:
        obj.load()

# Generated at 2022-06-13 08:10:51.809540
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    assert HandlerTaskInclude.load([])
    assert HandlerTaskInclude.load([], block=True)
    assert HandlerTaskInclude.load([], role=True)
    assert HandlerTaskInclude.load([], task_include=True)


# Generated at 2022-06-13 08:10:53.969694
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    # TODO: implement test
    pass

# Unit tests for class HandlerTaskInclude

# Generated at 2022-06-13 08:11:04.866417
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    '''
    This function tests the load function of the class HandlerTaskInclude
    '''

    # String for testing
    test_string = ''' 
- name: Standalone handlers
  notify: 
      - Restart Tomcat
      - Start Tomcat
'''

    # Create a Host object
    # host = Host()

    # Create a Handler object
    handler = Handler.load(data=yaml.load(test_string), block=block, role=role, task_include=task_include, variable_manager=variable_manager, loader=loader)

    # Create a HandlerTaskInclude object
    handler = HandlerTaskInclude.load(data=yaml.load(test_string), block=block, role=role, task_include=task_include, variable_manager=variable_manager, loader=loader)

    # Create a Handler

# Generated at 2022-06-13 08:11:17.522367
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    from units.mock.loader import DictDataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    loader = DictDataLoader({
        "some_handler_file.yml": "{}",
    })

    variable_manager = VariableManager()
    inventory = InventoryManager(loader=DataLoader())
    variable_manager.set_inventory(inventory)

    handler = HandlerTaskInclude.load(dict(name='some_handler_file.yml'), loader=loader, variable_manager=variable_manager)
    assert isinstance(handler, Handler)

# Generated at 2022-06-13 08:11:19.573875
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.handler import Handler
    assert issubclass(HandlerTaskInclude,Handler)
    assert issubclass(HandlerTaskInclude,TaskInclude)
    t = HandlerTaskInclude()
    assert(t.load.__module__ == 'ansible.playbook.handler_task_include')



# Generated at 2022-06-13 08:11:27.531689
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    assert False, "TODO"
# (c) 2012-2014, Michael DeHaan <michael.dehaan@gmail.com>
#
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www

# Generated at 2022-06-13 08:11:31.359410
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    m = HandlerTaskInclude.load(
        data={
            "include": {
                "name": "test.yml"
            }
        }
    )
    assert m is not None
    assert m.static is True

# Generated at 2022-06-13 08:11:42.187082
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    # Define all parameters that are used to create the class
    # HandlerTaskInclude
    block = None
    role = None
    task_include = None
    data = dict(
        include='/foo/bar.yml',
        static=1,
        no_log=1
    )
    variable_manager = None
    loader = None

    # Create an instance of the class HandlerTaskInclude
    handler = HandlerTaskInclude.load(data, block, role, task_include, variable_manager, loader)

    # Check if all attributes of the object handler have the correct value
    assert handler._block == block
    assert handler._role == role
    assert handler._task_include == task_include
    assert handler.include_file == '/foo/bar.yml'
    assert handler.no_log == 1
    assert handler.static

# Generated at 2022-06-13 08:11:46.904402
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    data = {'include': 'myplay', 'hosts': 'localhost'}
    variable_manager = None
    loader = None
    obj = HandlerTaskInclude.load(data, variable_manager=variable_manager, loader=loader)
    assert obj is not None
    assert obj._role is None
    assert obj._block is None
    assert obj._task_include is None
    assert obj._include is not None

# Generated at 2022-06-13 08:11:55.928596
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    data = dict(
        name = 'test_handler_task_include',
        listen = 'test_listen',
        tasks = dict(
            file = '/etc/passwd'
        )
    )
    handler = HandlerTaskInclude.load(data)
    data1 = dict(
        name = 'test_handler_task_include_check',
        tasks = dict(
            file = '/etc/passwd'
        )
    )
    handler1 = HandlerTaskInclude.load(data1)
    assert handler.tasks[0]._role is None
    assert handler.tasks[0]._task_include is None
    assert handler1.tasks[0]._role is None
    assert handler1.tasks[0]._task_include is None

# Generated at 2022-06-13 08:11:56.863800
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    pass

# Generated at 2022-06-13 08:11:57.594514
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    pass

# Generated at 2022-06-13 08:12:02.255853
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    handlerTaskInclude = HandlerTaskInclude()
    assert handlerTaskInclude == {'listen': None, 'role': None, 'tasks': []}
    # assert handlerTaskInclude.listen == None
    # assert handlerTaskInclude.tasks == []



# Generated at 2022-06-13 08:12:13.415773
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    import ansible.playbook
    import ansible.inventory.host
    import ansible.playbook.task_include
    import ansible.playbook.task

    handler = HandlerTaskInclude.load({"name" : "hello",
                                       "include" : "some_role",
                                       "listen" : "some_event"}, block=None, role=None, task_include=None, variable_manager=None, loader=None)

    assert isinstance(handler, HandlerTaskInclude)
    assert handler.block == None
    assert handler.role == None
    assert handler.task_include == None
    assert handler._role_name == "some_role"
    assert handler._task_name == None
    assert handler._loop == None
    assert handler._loop_var == None
    assert handler._task_tags == []

# Generated at 2022-06-13 08:12:15.314354
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    print('test_HandlerTaskInclude_load')

    # TODO create a unit test

# Generated at 2022-06-13 08:12:26.514804
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    ht = HandlerTaskInclude(block=None, role=None, task_include=None)

    data_include_handlers = dict(
        include_handlers=dict(
            tasks=dict(
                action=dict(
                    module='debug',
                    args=dict(
                        msg='this is a test'
                    )
                )
            )
        )
    )

    from ansible.errors import AnsibleParserError
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

# Generated at 2022-06-13 08:12:30.533691
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    # stub
    _data = {}
    # object
    _t = HandlerTaskInclude()
    # execute
    _actual_result = _t.load(_data)
    # verify
    assert _actual_result is not None

# Generated at 2022-06-13 08:12:40.086469
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.vars import VariableManager
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play

    hosts = [Host(name="test_inventory_host_1", variables={})]
    groups = [Group(name="test_inventory_group_1")]
    group = hosts[0].get_group()
    group.add_host(hosts[0])
    groups.append(group)
    inventory = InventoryManager(loader=DataLoader(), sources=None, groups=groups)

    vars_manager = VariableManager(loader=DataLoader(), inventory=inventory)


# Generated at 2022-06-13 08:12:46.839102
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.inventory.host import Host
    from ansible.playbook.handler import Handler
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    from ansible.vars.manager import VariableManager

    # Setup Mock Host
    mock_host = Host('localhost')

    # Setup Mock PlayContext
    mock_play_context = PlayContext(remote_user='root')

    # Setup Mock Task
    mock_task = Task()

    # Setup Mock VariableManager
    mock_variable_manager = VariableManager()
    mock_variable_manager._fact_cache['localhost'] = dict()

    # Test load
    test_instance = HandlerTaskInclude()

# Generated at 2022-06-13 08:12:56.702800
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():

    from ansible.playbook.block import Block
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.role import Role
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude

    #Prepare necessary arguments to create a HandlerTaskInclude object

# Generated at 2022-06-13 08:13:11.015398
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.inventory.host import Host
    from ansible.playbook.block import Block
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.template import Templar

    templar = Templar(loader=None, variables={})

# Generated at 2022-06-13 08:13:11.934192
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    pass

# Generated at 2022-06-13 08:13:21.264372
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    # Using a class variable VALID_INCLUDE_KEYWORDS to test the included one and optionally overwritten
    print('\ntest_HandlerTaskInclude_load: using class variable HandlerTaskInclude.VALID_INCLUDE_KEYWORDS: ',
          HandlerTaskInclude.VALID_INCLUDE_KEYWORDS)

# Generated at 2022-06-13 08:13:34.039803
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    import os
    import sys
    import yaml
    from ansible.inventory import Inventory
    from ansible import constants as C

    # Initialize local variables
    ansible_dir = '/home/vagrant/workspace/ansible'
    relative_path_test_file = 'lib/ansible/playbook/tests/files/playbooks/test_include.yml'
    test_file = os.path.join(ansible_dir, relative_path_test_file)
    stream = open(test_file, 'r').read()

    playbook_data = yaml.safe_load(stream)
    for playbook_datum in playbook_data:
        for parameter in playbook_datum:
            print(parameter)

    # Test constants

# Generated at 2022-06-13 08:13:34.995142
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    pass


# Generated at 2022-06-13 08:13:42.639500
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    class Handler:
        def __init__(self, block=None, role=None, task_include=None):
            self.block = block
            self.role = role
            self.task_include = task_include

        def _load_from_block(self, block, local_vars):
            pass

        def check_options(self, options, imported_file):
            return options

    class TaskInclude:
        VALID_INCLUDE_KEYWORDS = {'tasks'}

        def __init__(self, block=None, role=None, task_include=None):
            self.block = block
            self.role = role
            self.task_include = task_include

        def load_data(self, data, variable_manager=None, loader=None):
            return data

    hti = Handler

# Generated at 2022-06-13 08:13:44.081756
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    data = {
        'test': 'blank'
    }
    result = HandlerTaskInclude.load(data=data)
    assert result



# Generated at 2022-06-13 08:13:45.745704
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    '''
    test_HandlerTaskInclude_load:
    '''
    # Create a HandlerTaskInclude instance
    h = HandlerTaskInclude()

    # Execute the load method and check the result
    assert h.load(None) is None

# Generated at 2022-06-13 08:13:47.138303
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    assert False, "Test not implemented"


# Generated at 2022-06-13 08:13:51.098221
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.inventory import Inventory
    from ansible.vars import VariableManager

    host = Inventory("localhost")
    variable_manager = VariableManager()
    
    handler = HandlerTaskInclude.load("/tmp/notify.yml", variable_manager=variable_manager, loader=None)
    assert handler == None

# Generated at 2022-06-13 08:14:01.148106
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    data=dict(
        include='task1.yml',
        listeners=10,
        name='task1'
    )
    block=None
    role=None
    task_include=None
    variable_manager=None
    loader=None
    handler=HandlerTaskInclude.load(data,
                                    block,
                                    role,
                                    task_include,
                                    variable_manager,
                                    loader)
    handlers=[]
    handlers.append(handler)
    # Testing when include is a string
    assert len(handlers) == 1
    assert handlers[0].get_name() == 'task1'
    assert handlers[0].listeners == 10
    assert handlers[0]._role == role


# Generated at 2022-06-13 08:14:06.446769
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins.loader import variable_manager
    from ansible.template import Templar
    from ansible.vars import VariableManager

    block = None
    role = None
    task_include = None
    variable_manager = VariableManager()
    variable_manager.extra_vars = dict(a=1)
    variable_manager._fact_cache = dict(a=1)

    tags = None
    listen_list = []
    listen = None
    max_fail_percentage = 0
    run_once = True
    use_handlers = True
    remote_user = 'root'
    become_user = None
    verbosity = 0


# Generated at 2022-06-13 08:14:09.815108
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    handler = HandlerTaskInclude()
    assert isinstance(handler,Handler)
    assert isinstance(handler,TaskInclude)
    assert isinstance(handler,HandlerTaskInclude)

# Generated at 2022-06-13 08:14:28.292351
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    ############################################
    # Basic test of load method of HandlerTaskInclude class
    ############################################
    plugin = 'handler_task_include'

# Generated at 2022-06-13 08:14:29.004892
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    pass;


# Generated at 2022-06-13 08:14:40.302983
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.playbook.task_include import TaskInclude
    import ansible.playbook.task as task
    import ansible.inventory.host as host
    import ansible.inventory.group as group
    import ansible.vars.manager as var_manager
    import ansible.vars.hostvars as hostvars
    import ansible.vars.groupvars as groupvars
    import ansible.inventory.manager as inventory_manager

    variable_manager = var_manager.VariableManager() 
    variable_manager._fact_cache = dict()
    my_host = host.Host(name='test_host')
    my_group = group.Group(name='test_group')
    my_inventory = inventory_manager.InventoryManager()
    my_inventory.add_group(my_group)
    my_inventory

# Generated at 2022-06-13 08:14:41.228324
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    handler = HandlerTaskInclude()
    assert(handler)

# Generated at 2022-06-13 08:14:43.260720
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    hti = HandlerTaskInclude()
    hti.load({
        'include': 'test',
        'listen': 'test'
    })

# Generated at 2022-06-13 08:14:44.296893
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    handler_task_include = HandlerTaskInclude()

# Generated at 2022-06-13 08:14:51.476333
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    import ansible.playbook.task
    from ansible.parsing.yaml.objects import AnsibleUnicode
    
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.inventory.host import Host
    from ansible.parsing.dataloader import DataLoader

    vars = VariableManager()
    loader = DataLoader()
    i = InventoryManager(loader=loader, sources=["/path/to/hosts"])
    h = Host(name="test", inventory=i)
    t = ansible.playbook.task.Task()
    h.set_variable('hostvars', {})
    h.set_variable('groups', {'test_group': {'hosts': ['test']}})

# Generated at 2022-06-13 08:14:56.297343
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    with mock.patch.object(Handler, 'load_data', return_value={}):
        with mock.patch.object(HandlerTaskInclude, 'check_options', return_value={}):
            HandlerTaskInclude.load(data={}, block={}, role={}, task_include={}, variable_manager={}, loader={})

# Generated at 2022-06-13 08:15:06.679494
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():

    print("In test_HandlerTaskInclude_load")
    print("Load the class")

    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    ########################################################
    # Create a host
    print("Create a host")
    host = Host(name='testserver')
    host.set_variable('ansible_ssh_port','22')
    host.set_variable('ansible_ssh_host','1.1.1.1')
    host.set_variable('ansible_ssh_user','testuser')
    host.set_variable('ansible_ssh_pass','testpass')
    host.set_

# Generated at 2022-06-13 08:15:14.190635
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    handler = HandlerTaskInclude(block=None, role=None, task_include=None)
    task_include = TaskInclude(block=None, role=None, task_include=None)
    data = {}
    data2 = {}
    data3 = {}
    data4 = {}
    data['name'] = 'test_HandlerTaskInclude'
    data2['name'] = 'test_HandlerTaskInclude'
    data3['name'] = 'test_HandlerTaskInclude'
    data4['name'] = 'test_HandlerTaskInclude'
    handler.check_option_value(data, data2, data3)
    handler.check_options(data, data2)
    handler.load_data(data4, variable_manager=None, loader=None)
    handler.add_path(loader=None)
    handler