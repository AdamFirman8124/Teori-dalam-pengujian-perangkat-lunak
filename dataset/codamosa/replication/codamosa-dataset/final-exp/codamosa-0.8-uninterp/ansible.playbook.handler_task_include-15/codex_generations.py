

# Generated at 2022-06-13 08:10:07.131775
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():

    data = {'listen': 'copy'}
    variable_manager = ""
    loader = ""
    handler = HandlerTaskInclude.load(data, variable_manager, loader)
    assert handler is not None, "Class HandlerTaskInclude method load returns None!"

# Generated at 2022-06-13 08:10:08.790044
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    handler_task_include = HandlerTaskInclude()
    assert isinstance(handler_task_include, HandlerTaskInclude) == True


# Generated at 2022-06-13 08:10:10.561791
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    '''handler
        handler_task_include
            HandlerTaskInclude
                load
    '''

    pass



# Generated at 2022-06-13 08:10:11.496024
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    assert HandlerTaskInclude.load is not None

# Generated at 2022-06-13 08:10:18.487968
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.inventory.group import Group
    from ansible.inventory.host import Host
    from ansible.vars.manager import VariableManager
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.block import Block
    import ansible.playbook.task
    import ansible.playbook.role
    import ansible.playbook.play
    import ansible.playbook.conditional
    import ansible.playbook.included_file
    import ansible.playbook.task_include
    import ansible.playbook.task_type
    import ansible.playbook.task_queue_manager
    import ansible.playbook.become

    group = Group(name='all')
    host = Host(name='localhost')

# Generated at 2022-06-13 08:10:27.884699
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible import constants
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.plugins import action_loader

    constants.HOST_KEY_CHECKING = False
    host = "127.0.0.1"
    block = Block()
    role = None
    task_include = Task()
    playbook_dir = '/usr/share/ansible/'
    variable_manager = VariableManager()
    loader = action_loader.ActionModuleLoader(playbook_dir, variable_manager)

    data = {'include': 'in_playbook_inc'}

# Generated at 2022-06-13 08:10:39.215600
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    play = {
            "hosts": "all",
            "gather_facts": "no",
            "handlers": [ {
                "include": {
                    "tasks": "tasks_file.yml",
                    "listen": "my_handler"
                }
            }]
    }

    import json
    import yaml

    print(json.dumps(play, default=lambda o: o.__dict__, sort_keys=True, indent=4))

    with open("play.yml", 'w') as outfile:
        yaml.dump(play, outfile, default_flow_style=False)

# Generated at 2022-06-13 08:10:45.950693
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    print("Testing load")
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.inventory.host import Host
    from ansible.inventory.host import Manager
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.vars import combine_vars

    host = Host(name="testserver.example.com")
    host.set_variable('ansible_python_interpreter', '/usr/bin/python')
    host.set_variable('variable1', 'value1')
    host.set_variable('variable2', 'value2')
    host.set_variable('variable3', 'value3')
    host.set_variable('variable4', 'value4')
    host.set

# Generated at 2022-06-13 08:10:48.023174
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    pass
# #
# #    HandlerTaskInclude.load(data)

# Generated at 2022-06-13 08:11:01.144621
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.role import Role
    from ansible.playbook.task_include import TaskInclude
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    play = Play()

# Generated at 2022-06-13 08:11:05.251774
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    """Tests the load() method of the HandlerTaskInclude class."""
    data = ['handler1', 'handler2']
    t = HandlerTaskInclude()
    # Call the method
    handler = t.load(data=data)
    assert handler.name == 'handler1'
    assert handler.get_htype()== 'handler'

# Generated at 2022-06-13 08:11:13.007760
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    data = {
        "include": {
            "foo": "bar",
            "listen": "my-handler"
        }
    }

    handler = HandlerTaskInclude.load(data)

    assert handler.include  == "foo=bar"
    assert handler.name     == "my-handler"
    assert handler.notify   == ["my-handler"]
    assert handler.rescue   == []
    assert handler.when     == []

# Generated at 2022-06-13 08:11:21.601780
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():

    from ansible.playbook.block import Block
    
    block = Block()
    task_include = HandlerTaskInclude(block=block)

    # Test for include_role
    data = {
        'include_role': {'name': 'Apache'}
    }

    handler = HandlerTaskInclude.load(data=data)
    assert handler.get_name() == 'include_role'
    assert handler.get_value() == {'name': 'Apache'}

    # Test for include_tasks
    data = {
        'include_tasks': {'name': 'Apache'}
    }

    handler = HandlerTaskInclude.load(data=data)
    assert handler.get_name() == 'include_tasks'
    assert handler.get_value() == {'name': 'Apache'}

# Generated at 2022-06-13 08:11:25.283132
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    # TODO Check if 'self' is needed --> Pass or no pass?
    H = HandlerTaskInclude
    HandlerTaskInclude.load(
        H,
        data=None,
        block=None,
        role=None,
        task_include=None,
        variable_manager=None,
        loader=None
    )

# Generated at 2022-06-13 08:11:32.462078
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    hti = HandlerTaskInclude()
    hti.listen = "listen"
    hti.block = "block"
    hti.role = "role"
    hti.tags = "tags"
    hti.run_once = "run_once"
    hti.name = "name"
    hti.delegate_to = "delegate_to"
    hti.handler = "handler"
    hti.transport = "transport"
    return hti


# Generated at 2022-06-13 08:11:43.600450
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.template import Templar
    from ansible.playbook.play import Play

    # Create a Dictionary to mimic 'data' in method load of class HandlerTaskInclude
    data = {}
    data['listen'] = 'test'
    data['name'] = 'test name'
    data['include'] = 'test include'
    data['tags'] = ['tag1', 'tag2']

    # Create a Templar object
    variable_manager = VariableManager()
    loader = DataLoader()
    inventory = InventoryManager(loader, variable_manager, sources='localhost,')
    variable_manager.set_inventory(inventory)

# Generated at 2022-06-13 08:11:51.055499
# Unit test for method load of class HandlerTaskInclude

# Generated at 2022-06-13 08:11:59.669207
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    """
    For this test to work, the following elements have to be set up:
    - inventory file with content:
        [test_group]
        test_machine ansible_connection=local
    - playbook test_playbook.yml with content:
        - hosts:
            - test_group
          tasks:
            - name: Test task
              debug:
                msg: This is a test task
            - include: test_task_include
            - include: test_handlers_include.yml

    - file with tasks called test_task_include with content
        - name: Test task include
          debug:
            msg: This is a task test include

    - file with handlers called test_handlers_include.yml with content
        - name: Test handlers include
          debug:
            msg: This is a handlers test include
    """
   

# Generated at 2022-06-13 08:12:00.888603
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    hti = HandlerTaskInclude()

# Generated at 2022-06-13 08:12:10.518000
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.inventory.host import Host
    hosts = [Host("hostname")]
    host = Host("hostname")

    from ansible.inventory.group import Group
    groups = [Group("groupname")]
    group = Group("groupname")

    from ansible.inventory.inventory import Inventory
    inventory = Inventory(hosts)

    from ansible.vars.manager import VariableManager
    variable_manager = VariableManager(inventory=inventory)

    from ansible.playbook.play import Play
    play = Play()

    from ansible.playbook.block import Block
    block = Block(play=play, role=None)

    from ansible.playbook.role import Role
    role = Role()

    from ansible.template.template import AnsibleTemplate
    task_include = AnsibleTemplate(dict())


# Generated at 2022-06-13 08:12:25.631685
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.inventory.host import Host
    from ansible.vars.manager import VariableManager
    from ansible.module_utils.facts import Facts
    import os

    my_loader = DataLoader()
    my_inventory = InventoryManager(loader=my_loader, sources=['/etc/ansible/hosts'])
    my_variable_manager = VariableManager(loader=my_loader, inventory=my_inventory)

# Generated at 2022-06-13 08:12:36.364158
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.inventory.host import Host
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.vars.manager import VariableManager
    from collections import namedtuple
    from ansible.parsing.dataloader import DataLoader

    Options = namedtuple('Options', ['connection', 'module_path', 'forks', 'become', 'become_method', 'become_user', 'check', 'diff'])
    options = Options(connection='ssh', module_path=None, forks=10, become=None, become_method=None, become_user=None, check=False, diff=False)

    data = {
        'name': 'test',
        'listen': 'notify_test'
    }

    loader = DataLoader()
    variable

# Generated at 2022-06-13 08:12:43.165846
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    # Check for required parameters for object creation
    try:
        t = HandlerTaskInclude()
    except Exception as e:
        assert '__init__() missing 2 required positional arguments: \'task_include\' and \'block\'' in str(e)

    # Check for correct initialization and parameter passing to base class
    try:
        t = HandlerTaskInclude(block='block', role='role', task_include='task_include')
    except Exception as e:
        assert False
    else:
        assert t._parent_block == 'block'
        assert t._role == 'role'
        assert t._task_include == 'task_include'


# Generated at 2022-06-13 08:12:43.684188
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    HandlerTaskInclude()


# Generated at 2022-06-13 08:12:44.418936
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    # Setup

    # Execute

    # Assert

    pass



# Generated at 2022-06-13 08:12:55.090820
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.task_executor import TaskExecutor
    from ansible.playbook.task_include import TaskInclude

    # Create a dummy inventory
    host = Host(name='dummy')
    group = Group(name='group')
    group.add_host(host)
    inventory = InventoryManager(loader=DataLoader())
    inventory.add_group(group)
    inventory.add_host(host)

    # Create a dummy play

# Generated at 2022-06-13 08:13:04.687409
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():

    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.vars.reserved import reserved

    ds = dict(
        name='myHandler',
        listen='myEvent'
    )
    ds = DataLoader().load_from_dict(ds)

    variable_manager = VariableManager()
    variable_manager.set_inventory(reserved)

    handler = HandlerTaskInclude.load(ds, variable_manager=variable_manager)
    assert handler._name == 'myHandler'
    assert handler._listen == 'myEvent'

# Generated at 2022-06-13 08:13:12.984829
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.inventory.host import Host
    from ansible.playbook.play import Play
    from ansible.playbook.block import Block

    host = Host(name='host')
    play = Play.load(dict(name='test play', hosts='host'), variable_manager=None, loader=None)

    task = dict(
        name='task 1',
        include=dict(
            tasks='a.yml'
        )
    )
    data = play.load_block_list(task, play=play)

    handler = HandlerTaskInclude.load(data)
    assert handler.name == 'notify'
    assert handler.action == 'a.yml'
    assert handler.listen is None

# Generated at 2022-06-13 08:13:13.549877
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    pass

# Generated at 2022-06-13 08:13:21.893538
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    """Test load method of module HandlerTaskInclude."""
    data = {}
    block = None
    role = None
    task_include = None
    variable_manager = None
    loader = None
    handler = HandlerTaskInclude.load(data, block, role, task_include, variable_manager, loader)
    assert handler == None


if __name__ == "__main__":

    test_HandlerTaskInclude_load()
    print("Test success")

# Generated at 2022-06-13 08:13:28.581381
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    '''
    Test the method HandlerTaskInclude.load()
    '''
    pass

# Generated at 2022-06-13 08:13:38.599400
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.playbook.play import Play
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.role import Role
    register_module= {'action': {'__ansible_arguments__': ['sleuth', '0.0.1', 'result', 'stdout_lines']}}

    variables = dict()
    variables['a_var'] = 'a_value'
    variables['b_var'] = 'b_value'

    data = dict(a_var='{{ a_var }}', b_var='{{ b_var }}', register='{{ "sleuth" }}')
    data['ignore_errors'] = False
    data['listen'] = 'all_good'
    data['name'] = 'write_sleuth_version'

# Generated at 2022-06-13 08:13:39.918661
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    h = HandlerTaskInclude()
    assert h

# Generated at 2022-06-13 08:13:48.173504
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    data = {
        'listen': 'main'
    }
    block = 'no block'
    role = 'no role'
    task_include = 'no task include'
    variable_manager = 'no variable manager'
    loader = 'no loader'
    handler = HandlerTaskInclude.load(
        data, block, role, task_include, variable_manager, loader
    )
    print('handler being created', handler)
    assert handler.listen == 'main'
    assert handler.block == 'no block'
    assert handler.role == 'no role'
    assert handler.task_include == 'no task include'

# Generated at 2022-06-13 08:13:49.862064
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    # handler = HandlerTaskInclude.load(data, block=None)
    assert False

# Generated at 2022-06-13 08:13:59.764215
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    '''
    Test load() method of the HandlerTaskInclude class
    '''

    fake_loader = None
    fake_variable_manager = None
    fake_play = None

    fake_options = dict(
        tasks_path='/etc/ansible/tasks',
        handlers_path='/etc/ansible/handlers',
        roles_path='/etc/ansible/roles:~',
        force=False,
        role=None,
        task_include=None,
        step=None,
        start_at=None,
        verbosity=3,
        ignore_errors=False,
        listhosts=None,
        listtasks=None,
        listtags=None,
        syntax=None,
    )


# Generated at 2022-06-13 08:14:02.743437
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    test_HandlerTaskInclude = HandlerTaskInclude()
    assert isinstance(test_HandlerTaskInclude, HandlerTaskInclude)
    assert isinstance(test_HandlerTaskInclude, Handler)
    assert isinstance(test_HandlerTaskInclude, TaskInclude)

# Generated at 2022-06-13 08:14:03.465182
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    pass

# Generated at 2022-06-13 08:14:04.206163
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
	pass

# Generated at 2022-06-13 08:14:11.357671
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    #Data to test method load of class HandlerTaskInclude
    data = {'include': 'tasks/test.yml', 'tags': ['import', 'test']}

    #HandlerTaskInclude to test
    action = HandlerTaskInclude()

    #test load
    result = action.load(data)

    assert result.tags == ['import', 'test']
    assert result.include == 'tasks/test.yml'