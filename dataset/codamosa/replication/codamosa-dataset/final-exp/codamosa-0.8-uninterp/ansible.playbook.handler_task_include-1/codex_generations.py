

# Generated at 2022-06-13 08:10:08.168619
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    import os
    import sys
    import imp
    import mock
    import pytest

    # If a test module is not already loaded, then load it now.
    if 'nxos_version' not in sys.modules:
        nxos_version = imp.load_source('nxos_version', '../../../../nxos_version/library/nxos_version.py')

    # Create an instance of class HandlerTaskInclude using HandlerTaskInclude.load()
    mock_loader = mock.Mock()

    # Check constructor of class HandlerTaskInclude

# Generated at 2022-06-13 08:10:16.103801
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    data = {u'static': u'/tmp/ansible_xyz.log', u'files': u'/tmp/ansible_xyz*.log', u'ignore_missing': False, u'dest': u'/tmp/ansible_xyz.log', u'path': u'/tmp', u'dest_type': u'file', u'src': u'', u'listen': u'Test'}
    from ansible.parsing.utils.addresses import parse_address
    from ansible.playbook.play_context import PlayContext

    from ansible.vars.manager import VariableManager
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.inventory.manager import InventoryManager


    # dummy host, and a dummy inventory
    host = Host()

# Generated at 2022-06-13 08:10:20.450456
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    # Create a handler
    handler = HandlerTaskInclude.load(data = {'include':'{{ foo }}'}, block=None, role=None, task_include=None, variable_manager=None, loader=None)

    # Make sure that it is a instance of HandlerTaskInclude
    assert isinstance(handler,HandlerTaskInclude)

# Generated at 2022-06-13 08:10:21.361643
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    return


# Generated at 2022-06-13 08:10:22.514864
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    ansible.playbook.handler.Handler.load(arg1, arg2, arg3)

# Generated at 2022-06-13 08:10:32.866274
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    # Create an AnsibleHost object
    from ansible.inventory.host import Host
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    host = Host(name='localhost', port=22)

    # Create an InventoryManager object
    inventory = InventoryManager(loader=DataLoader())
    inventory.hosts = dict()
    inventory.hosts['localhost'] = host

    # Create a VariableManager object
    variable_manager = VariableManager(loader=DataLoader(), inventory=inventory)

    example_data = dict(
        include='name_of_playbook_to_include'
    )

    # Create a HandlerTaskInclude object

# Generated at 2022-06-13 08:10:39.652313
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    h = HandlerTaskInclude.load(
        data={
            'include': 'my_include.yml',
            'tags': ['tag1', 'tag2']
        },
        block=None,
        role=None,
        task_include=None,
        variable_manager=None,
        loader=None
    )

    assert h.tags == ['tag1', 'tag2']

# Generated at 2022-06-13 08:10:40.138637
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    assert True

# Generated at 2022-06-13 08:10:50.388782
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader

    handler = HandlerTaskInclude.load(data=dict(
        include='a',
        include_tasks='b',
        include_vars='c',
        include_role='d',
    ))

    # check that the handler has correctly been initialized
    assert handler is not None
    assert handler.include_tasks == 'a'
    assert handler.include_tasks == 'b'
    assert handler.include_vars == 'c'
    assert handler.include_role == 'd'

    # check that the action has correctly been initialized
    assert handler.action is not None

# Generated at 2022-06-13 08:10:52.406398
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    data = dict(
        name = 'test'
    )

    assert HandlerTaskInclude.load(data).get_name() == 'test'

# Generated at 2022-06-13 08:11:04.730078
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.inventory.host import Host
    from ansible.playbook.task import Task
    from ansible.parsing.yaml.objects import AnsibleUnicode, AnsibleSequence
    from ansible.vars.manager import VariableManager

    variable_manager = VariableManager()
    variable_manager._fact_cache = {'me': 'notme'}
    variable_manager._options = {'cache_type': 'memory'}

    host = Host('test')
    host.set_variable('me', 'notme')
    host.set_variable('mydict', {'foo': 'bar'})
    host.set_variable('mylist', ['foo', 'bar'])
    variable_manager.set_host_variable(host, 'myvar', 42)


# Generated at 2022-06-13 08:11:10.875416
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    test_data = {
        'listen': 'redis',
        'name': 'redis_cache',
        'notify': [
            'restart redis'
        ],
        'notify_with_items': True
    }
    handler = HandlerTaskInclude.load(test_data)
    # assert isinstance(host, Host)

# Generated at 2022-06-13 08:11:12.213745
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    assert HandlerTaskInclude


# Generated at 2022-06-13 08:11:16.299872
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    data = {
        'include': 'foo.yml',
        'static': 'yes'
    }

    handler = HandlerTaskInclude.load(data)
    assert handler.include == 'foo.yml'

# Generated at 2022-06-13 08:11:24.090491
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.inventory.host import Host
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.role import Role
    from ansible.playbook.role_include import RoleInclude
    import os
    import json

    # NOTE: Method load of class HandlerTaskInclude needs the following
    # parameters:
    #   data: A dictionary that contains the data to load into the object.
    #   block: The Block object on which this task resides.
    #   role:

# Generated at 2022-06-13 08:11:24.907937
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    HandlerTaskInclude(block="block", role="role")

# Generated at 2022-06-13 08:11:26.080587
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    pass


# Generated at 2022-06-13 08:11:31.222215
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    data = {
        'handlers': 'node-notify.yml'
    }
    handler = HandlerTaskInclude(
        None,
        None,
        task_include=None
    ).load(data)
    assert handler.get_name() == 'node-notify'
    assert handler.enabled == 'yes'

# Generated at 2022-06-13 08:11:41.958536
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.inventory.dir import InventoryDirectory
    from ansible.inventory.host import Host
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()

    inv_dir = InventoryDirectory('.')
    inv = dict(
        all = dict(
            children = dict(
                test = dict(
                    children = dict(
                        foo = dict(
                            hosts = dict(
                                host0 = dict(),
                            )
                        ),
                        bar = dict(
                            hosts = dict(
                                host1 = dict(),
                            )
                        ),
                    ),
                    hosts = dict()
                ),
            )
        )
    )

    inv_dir._populate_from_inventory(inv)


# Generated at 2022-06-13 08:11:50.256552
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.role import Role
    from ansible.playbook.play import Play

    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    test_task = Task()
    test_block = Block()
    test_play = Play()
    test_role = Role()
    test_variable_manager = VariableManager()
    test_loader = DataLoader()
    test_inventory = InventoryManager(loader=test_loader, sources=['/etc/ansible/hosts'])


# Generated at 2022-06-13 08:12:05.873341
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.inventory.host import Host
    from ansible.variables import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    import uuid
    subset_dir = 'file:///home/vagrant/myansible/default_inventory_plugins'
    host_list = ['localhost']
    host_obj = Host(name='localhost', port=22)
    inventory_manager = InventoryManager(loader=DataLoader(), sources=subset_dir)
    inventory_manager.add_host(host=host_obj)
    play_context = PlayContext()
    play_context.check_

# Generated at 2022-06-13 08:12:11.947621
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    data = dict(
        name='name',
        first_keyword='first_keyword',
        second_keyword='second_keyword'
        )
    block = 'block'
    role = 'role'
    task_include = 'task_include'
    variable_manager='variable_manager'
    loader='loader'

    handler = HandlerTaskInclude.load(data, block, role, task_include, variable_manager, loader)
    for key, value in handler.items():
        assert key in data.keys() and data[key] == value

# Generated at 2022-06-13 08:12:21.765290
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    data = dict(
        name = 'test',
        include = dict(
            src = 'role',
            private = 'foo',
            tasks = dict(
                task2 = dict(
                    action = dict(
                        module = 'ping',
                        args = 'pong'
                    )
                )
            ),
            variables = dict(
                a = 'b'
            )
        )
    )

    handler = HandlerTaskInclude.load(data=data)

# Generated at 2022-06-13 08:12:22.183756
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    assert True

# Generated at 2022-06-13 08:12:22.797467
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    assert True

# Generated at 2022-06-13 08:12:29.365780
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    
    variable_manager = VariableManager()

    inventory = InventoryManager(['./tests/inventory/inventory'])
    variable_manager.set_inventory(inventory)

    data = {'name': 'start'}

    handler = HandlerTaskInclude.load(data, variable_manager=variable_manager)
    print(handler)


if __name__ == '__main__':
    test_HandlerTaskInclude()

# Generated at 2022-06-13 08:12:38.842269
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.vault import VaultLib
    from ansible.vars.manager import VariableManager

    # Initialize the VaultLib
    vault_pass = "123"
    vault_lib = VaultLib(vault_pass)

    # Initialize the inventory
    inventory_manager = InventoryManager(loader=None, sources=None)

    # Set a custom source to the inventory
    custom_host = dict(
        aHostName="aHostName",
        aCustomField="some value",
        aCustomGroup="all",
        aCustomVariable="aCustomVariableValue"
    )
    inventory_manager.add_host(custom_host, "all", "aHostName")

    # Initialize a variable_manager

# Generated at 2022-06-13 08:12:46.151808
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():

    import __builtin__
    from ansible.inventory.host import Host
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    from ansible.plugins.callback.default import CallbackModule
    from ansible.vars.manager import VariableManager

    __builtin__.__dict__['__opts__'] = {
        '__role_opts__': {},
        '__play_context__': PlayContext(),
        'default_inventory': 'localhost'
    }

    setattr(CallbackModule, '_display', lambda x:x)

    results = []

    def get_host_results(host, task_name):
        return results

    def get_group_results(group, task_name):
        return results


# Generated at 2022-06-13 08:12:46.994670
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    pass

# Generated at 2022-06-13 08:12:48.396880
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    # Initialize the class
    obj = HandlerTaskInclude()
    # Execute the method
    obj.load()

# Generated at 2022-06-13 08:12:54.569561
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    pass

# Generated at 2022-06-13 08:13:04.606689
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    # load is a staticmethod
    # load = staticmethod(HandlerTaskInclude.load)
    # load = HandlerTaskInclude.load

    data = dict(
        name = 'test_HandlerTaskInclude_load'
    )

    # args = (data, block, role, task_include, variable_manager, loader)
    # handler = load(*args)
    handler = HandlerTaskInclude.load(data)

    assert handler.__class__.__name__ == 'HandlerTaskInclude'
    assert handler.get_name() == 'test_HandlerTaskInclude_load'
    assert handler.loop is None

# Generated at 2022-06-13 08:13:06.627913
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    assert HandlerTaskInclude({'include': 'my-handlers.yml'}, block=None, role=None, task_include=None)

# Generated at 2022-06-13 08:13:11.886477
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    data = {'block': {'attributes': ['attributes'], 'name': 'block name', 'handler': 'handler'}, 'role': {'name': 'role name'}, 'task_include': {'name': 'task include name'}, 'listen': 'listen', 'include': {'tasks': 'tasks'}, 'import_playbook': 'import_playbook', 'import_role': 'import_role'}
    variable_manager = 'variable manager'
    loader = 'loader'
    handler = HandlerTaskInclude.load(data, variable_manager=variable_manager, loader=loader)

    assert handler.block == data['block']
    assert handler.role == data['role']
    assert handler.task_include == data['task_include']
    assert handler._include == data['include']
    assert handler._import_

# Generated at 2022-06-13 08:13:13.158490
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    HandlerTaskInclude.load(data=None)
    assert 1 == 1

# Generated at 2022-06-13 08:13:14.793724
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():

    # create an instance
    HandlerTaskInclude = HandlerTaskInclude()

    # pass self test
    return

# Generated at 2022-06-13 08:13:19.546218
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    hti = HandlerTaskInclude()
    assert hti.VALID_INCLUDE_KEYWORDS == {'block', 'block:rescue', 'block:always', 'block:always:rescue', 'listen'}

# Generated at 2022-06-13 08:13:20.723968
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    pass


# Generated at 2022-06-13 08:13:21.465576
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
	pass

# Generated at 2022-06-13 08:13:26.981964
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    data = {u'name': u'Test handler', u'listen': u'Test Condition'}
    try:
        hti = HandlerTaskInclude.load(data=data)
    except Exception as e:
        assert False
    else:
        assert isinstance(hti, HandlerTaskInclude)

# Generated at 2022-06-13 08:13:43.924037
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.inventory import Inventory
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext

    # Create inventory
    host = Host(name="localhost")
    group = Group(name="ungrouped")
    group.add_host(host)
    inventory = Inventory()
    inventory.add_host(host)
    inventory.add_group(group)
    inventory.subset("all")

    # Create task data
    data = {}

    # Create task

# Generated at 2022-06-13 08:13:49.372290
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    valid_data = dict(
        include='some_file',
        new_field='value_of_new_field'
    )
    invalid_data = dict(
        var='some_file',
        new_field='value_of_new_field'
    )
    assert HandlerTaskInclude.load(valid_data) is not None
    assert HandlerTaskInclude.load(invalid_data) is None

# Generated at 2022-06-13 08:13:49.917536
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
	pass

# Generated at 2022-06-13 08:13:59.806076
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.parsing.yaml.objects import AnsibleMapping
    from ansible.inventory.host import Host
    from ansible.vars.manager import VariableManager
    from ansible.vars.include_vars import IncludeVars
    from ansible.playbook.play_context import PlayContext

    host = Host('h1')
    playbook_context = PlayContext()
    variable_manager = VariableManager(loader=None, hosts=host, playbook_context=playbook_context)

    data = AnsibleMapping({
        u'include': u'included_handler',
        u'listen': u'reboot'
    })

    handler = HandlerTaskInclude.load(data, task_include=IncludeVars(loader=None, variable_manager=variable_manager))
    assert handler._block == None

# Generated at 2022-06-13 08:14:05.880965
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.plugins.loader import action_loader
    from ansible.inventory.group import Group
    from ansible.inventory.host import Host
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    # create loader, inventory and variable_manager
    loader = DataLoader()
    inventory = Group()
    variable_manager = VariableManager()

    # create host, set its vars and add it to inventory
    host = Host(name='foohost')
    host.vars = {'ansible_connection': 'local'}
    inventory.add_host(host)

    # create play
    play = Play()

    # create task
    task = Task()
    play.add_task(task)

    # create handler

# Generated at 2022-06-13 08:14:11.443208
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    handlerTaskInclude = HandlerTaskInclude()
    assert handlerTaskInclude
    assert handlerTaskInclude.VALID_INCLUDE_KEYWORDS == {
                                                          'tasks_from',
                                                          'handlers_from',
                                                          'listen'
                                                         }

# Generated at 2022-06-13 08:14:21.565043
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    # Create new handler call to load
    HandlerTaskInclude_load = HandlerTaskInclude()

    # Load test data
    data = dict(
        include = dict(
            name = "my include tasks",
            static = [ "1", "2" ]
        )
    )

    # Check that load method raises exception for empty include data
    def empty_include():
        HandlerTaskInclude_load.load(dict(include = dict()))
    expect(empty_include).to(raise_error(Exception, 'This task/handler does not have a valid `include` directive'))

    # Check that load method raises exception when include data doesn't have name
    def no_name():
        HandlerTaskInclude_load.load(dict(include = dict(static = ["1"])))

# Generated at 2022-06-13 08:14:26.063503
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    """
    Call the load method of HandlerTaskInclude with a example 'include'
    """
    data = {
        'include': 'hello.yml'
    }
    handler = HandlerTaskInclude.load(data)
    assert handler.include_file == 'hello.yml'
    assert handler.block is None

# Generated at 2022-06-13 08:14:31.707429
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    from ansible.template import Templar

    data = {
        'name': 'test',
        'include': 'test.yml',
        'listen': 'all'
    }

    class MockRole(object):
        def __init__(self):
            self.name= 'test'

    class MockVariableManager:
        class MockLoader:
            vars_files=['test']

            def get(self, key, default=None):
                return {
                    'test.yml': 'test'
                }.get(key, default)

        def __init__(self):
            self.loader= self.MockLoader()

    class MockBlock:
        def __init__(self):
            self.role= MockRole()



# Generated at 2022-06-13 08:14:42.539866
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    # test with an include task
    hti = HandlerTaskInclude.load({
        'include': 'foo.yml',
        'static': 'yes'
    })
    assert hti is not None
    assert hti.tasks is None
    assert hti.static is True
    assert hti.path == 'foo.yml'

    # test with an include task with name
    hti = HandlerTaskInclude.load({
        'include': 'foo.yml',
        'name': 'Foobar foo',
    })
    assert hti is not None
    assert hti.tasks is None
    assert hti.static is False
    assert hti.path == 'foo.yml'
    assert hti.role is None
    assert hti.get_name() == 'Foobar foo'

    #

# Generated at 2022-06-13 08:15:08.722753
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    print("Testing HandlerTaskInclude class")
    # Test 6
    """
    Test object creation and attribute assignment
    """
    # data = {'include': 'tasks/common.yml'}
    # block = None
    # role = None
    # task_include = None
    # loader = None
    # variable_manager = None
    # handler = HandlerTaskInclude.load(data=data, block=block, role=role, task_include=task_include, variable_manager=variable_manager, loader=loader)
    # assert handler.include == 'tasks/common.yml'


test_HandlerTaskInclude_load()

# Generated at 2022-06-13 08:15:15.779965
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.playbook.block import Block
    from ansible.playbook.role import Role
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook import PlayBook
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.inventory.inventory import Inventory
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    block = Block()
    role = Role()
    task_include = TaskInclude()

    data = dict(
        name="",
        src="",
        tasks=[],
        handlers=[],
        vars=[],
        default_vars=[],
        meta=[],
    )


# Generated at 2022-06-13 08:15:22.920892
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group

    host_1 = Host(name="localhost")
    host_2 = Host(name="localhost")
    host_3 = Host(name="localhost")

    host_1.set_variable('ansible_connection', 'local')
    host_2.set_variable('ansible_connection', 'local')
    host_3.set_variable('ansible_connection', 'local')

    group_1 = Group('group_1')
    group_2 = Group('group_2')


# Generated at 2022-06-13 08:15:23.415483
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    # TODO
    pass

# Generated at 2022-06-13 08:15:25.479807
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    pass

# Generated at 2022-06-13 08:15:28.445786
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    obj = HandlerTaskInclude(block=None, role=None, task_include=None)

# Load constructor data and check it's attributes
# if it's correctly loaded

# Generated at 2022-06-13 08:15:30.158624
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    handler = HandlerTaskInclude(block=None, role=None, task_include=None)

    assert handler is not None

# Generated at 2022-06-13 08:15:30.918498
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    pass


# Generated at 2022-06-13 08:15:37.461740
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():

    data={
        'include':'',
        'name':''
    }

    variable_manager=None
    loader=None
    role=None
    block=None

    t = HandlerTaskInclude(block=block, role=role, task_include=None)
    handler = t.load(data,block=block, role=role, task_include=t, variable_manager=variable_manager, loader=loader)
    assert handler.include == data['include']


# Generated at 2022-06-13 08:15:41.698090
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    def __init__(self, block=None, task_include=None, role=None):
        Role()
        Block()
        TaskInclude()

# Generated at 2022-06-13 08:16:30.697854
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.inventory.host import Host
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.vars.manager import VariableManager

    h = Host('127.0.0.1')
    t = Task()
    b = Block(t)
    v = VariableManager()

    data = {}
    handler = HandlerTaskInclude.load(data, block=b, variable_manager=v)
    assert handler._block == b
    assert handler._role is None
    assert handler._task_include is None
    assert handler._attributes['listen'] is None
    assert handler._attributes['tasks'] == []
    assert handler._attributes['handlers'] == []
    assert handler._attributes['vars'] == {}


    # from ansible.playbook.

# Generated at 2022-06-13 08:16:36.456649
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.role import Role
    from ansible.inventory.host import Host
    from ansible.vars.manager import VariableManager

    block = Block(parent_block=Task())

    host = Host('127.0.0.1')
    group = Group(name='test_group')
    group.add_host(host)
    host.get_vars()
    host.groups.append(group)

    inventory = Inventory(host_list=[host.name])
    inventory.add_group(group)
    inventory.add_host(host)

    variable_manager = VariableManager(loader=None, inventory=inventory)

    role = Role()


# Generated at 2022-06-13 08:16:37.611857
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    assert isinstance(HandlerTaskInclude(), HandlerTaskInclude)


# Generated at 2022-06-13 08:16:44.566114
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():

    from ansible.inventory.host import Host
    from ansible.vars.manager import VariableManager

    h1 = Host(name="h1")
    h2 = Host(name="h2")

    vm = VariableManager()

    data = dict(
        include = "tasks/main.yml",
        include_tasks = "tasks/main.yml",
        include_role = dict(name='test'),
        include_vars = "vars/main.yml",
        name = "test",
        hosts = [h1, h2],
        when = "True"
    )

    assert not HandlerTaskInclude.load(data, variable_manager=vm)

# Generated at 2022-06-13 08:16:48.355124
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources='localhost,')
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    handler_task_include = HandlerTaskInclude()
    data = dict(include='playbook.yml')
    result = handler_task_include.check_options(handler_task_include.load_data(data, variable_manager=variable_manager, loader=loader), data)
    assert result._role is None
    assert result._block is None
    assert result._task_include is None

# Generated at 2022-06-13 08:16:53.762375
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.play_context import PlayContext

    from units.mock.loader import DictDataLoader
    from units.mock.path import mock_unfrackpath_noop

    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    from units.compat.mock import MagicMock, patch

    loader = DictDataLoader({})

    variable_manager = VariableManager()
    variable_manager._fact_cache = dict()
    variable_manager.set_inventory(InventoryManager(loader=loader))

    playcontext = PlayContext()
    playcontext._play = None

    # test 1 - 'name' keyword

# Generated at 2022-06-13 08:17:02.811945
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    data = {'handlers': [{'include': 'tasks_role2_include.yml'},
                         {'include': 'handlers.yml'},
                         {'include': 'tasks_role3_include.yml'},
                         {'include': 'tasks_role4_include.yml'}]}
    #from ansible.parsing.dataloader import DataLoader
    #from ansible.vars.manager import VariableManager
    #from ansible.inventory.manager import InventoryManager
    #from ansible.playbook.play_context import PlayContext

    #variable_manager = VariableManager()
    #loader = DataLoader()
    #inventory = InventoryManager(loader=loader, sources=['localhost,'])
    #variable_manager.set_inventory(inventory)
    #print(inventory.get_host

# Generated at 2022-06-13 08:17:03.204125
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    pass

# Generated at 2022-06-13 08:17:03.698144
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    pass

# Generated at 2022-06-13 08:17:12.096968
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.block import Block
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.inventory.manager import InventoryManager

    variable_manager = VariableManager()
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, variable_manager=variable_manager)
    play_context = PlayContext(play=Play(), variable_manager=variable_manager, loader=loader)
    block = Block()
    task = HandlerTaskInclude(block=block, play_context=play_context)

    assert task

# Generated at 2022-06-13 08:18:43.612389
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    import ansible.vars.manager
    import ansible.inventory.manager
    import ansible.playbook.task
    import ansible.playbook.play
    import ansible.playbook.block
    import ansible.playbook.role
    import ansible.template

    vm   = ansible.vars.manager.VariableManager()
    im   = ansible.inventory.manager.InventoryManager(vm)
    play = ansible.playbook.play.Play().load({'hosts': 'all', 'gather_facts': 'no'}, vm, im)
    t    = ansible.playbook.task.Task()
    blk  = ansible.playbook.block.Block(play=play, role=ansible.playbook.role.Role())

# Generated at 2022-06-13 08:18:47.077803
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.module_utils.common.collections import ImmutableDict

    pc = PlayContext()
    vm = VariableManager()

    h = HandlerTaskInclude.load(
        dict(
            include='include.yml',
        ),
        variable_manager=vm,
        loader=DataLoader(),
    )

    assert h is not None

# Generated at 2022-06-13 08:18:49.912906
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    obj = HandlerTaskInclude()
    import ansible.playbook.task_include
    assert(obj._block == None)
    assert(type(obj._block) == ansible.playbook.task_include.Block)
    assert(obj._role == None)
    assert(type(obj._role) == ansible.playbook.task_include.Role)
    assert(obj._task_include == None)
    assert(type(obj._task_include) == ansible.playbook.task_include.TaskInclude)


# Generated at 2022-06-13 08:18:58.852042
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play

    variable_manager = VariableManager()
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=['test/inventory'])
    play = Play.load(dict(
        name = "Ansible Play",
        hosts = 'webservers',
        gather_facts = 'no',
        tasks = [
            dict(action=dict(module='shell', args='ls'), register='shell_out'),
            dict(action=dict(module='debug', args=dict(msg='{{shell_out.stdout}}')))
         ]
        ), variable_manager=variable_manager, loader=loader)



# Generated at 2022-06-13 08:19:09.363891
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.inventory.host import Host
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task

    def queue_task(host, task, task_vars=None, play_context=None, new_stdin=None, tmp=None):
        print("queue task method")

        assert host == "host1"
        assert task == "task1"
        assert task_vars == {"var1": "val1"}
        assert play_context == {"name": "play1"}
        assert new_stdin == "stdin"
        assert tmp == "tmp"


# Generated at 2022-06-13 08:19:11.157922
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    handler = HandlerTaskInclude()
    assert handler
    assert isinstance(handler, TaskInclude)

# Generated at 2022-06-13 08:19:18.474910
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    test_object = HandlerTaskInclude()
    data = "test_value"
    block = "TEST_BLOCK"
    #role = "TEST_ROLE"
    #task_include = "TEST_TASK"
    variable_manager = "TEST_VAR_MANAGER"
    loader = "TEST_LOADER"
    # For info on the following assert, see
    # https://stackoverflow.com/questions/46902497/python-assertionerror-when-testing-a-method-that-returns-a-value
    assert test_object.load(data,block,role=None,task_include=None,variable_manager=variable_manager,loader=loader)



# Generated at 2022-06-13 08:19:21.597494
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    handler_task_include = HandlerTaskInclude()
    assert isinstance(handler_task_include, HandlerTaskInclude)


# Generated at 2022-06-13 08:19:26.574834
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    print("Test load")
    t = HandlerTaskInclude()
    t.load(
        {
            "when": "success",
            "include": "foobar.yml"
        }
    )
    assert t.when == "success"
    assert t.include == "foobar.yml"

# Generated at 2022-06-13 08:19:34.977162
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    import ansible
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group

    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader

    from ansible.playbook.role import Role
    from ansible.playbook.block import Block
    from ansible.playbook.play import Play

    # Create a host and a group
    host1 = Host("test_host")
    group1 = Group("test_group")

    # Create a variable manager
    variable_manager = VariableManager()
    variable_manager.set_inventory(
        ansible.inventory.Inventory(
            loader=DataLoader(),
            variable_manager=variable_manager
        )
    )

    # Create a play