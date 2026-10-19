

# Generated at 2022-06-13 08:10:07.909124
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    data = dict(static='/etc/ansible/static.yml',
                dynamic='/etc/ansible/dynamic/{{ inventory_hostname }}.yml')
    block = []
    t = HandlerTaskInclude(block=block)
    handler = t.check_options(t.load_data(data))
    assert handler == t

# Generated at 2022-06-13 08:10:15.788394
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.inventory.host import Host
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    loader = DataLoader()
    host = Host(name="foo")
    variable_manager = VariableManager()

    handler = HandlerTaskInclude.load(
        {
            'name': 'test',
            'include_tasks': 'tasks/main.yaml',
            'tags': ['debug']
        },
        block=None,
        role=None,
        task_include=None,
        loader=loader,
        variable_manager=variable_manager,
    )
    assert handler.name == 'test'
    assert handler.block is None
    assert handler.has_triggered() is False
    assert handler.notified_by() == []


# Generated at 2022-06-13 08:10:17.521664
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    t = HandlerTaskInclude()
    assert t.VALID_INCLUDE_KEYWORDS == HandlerTaskInclude.VALID_INCLUDE_KEYWORDS

# Generated at 2022-06-13 08:10:18.326802
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    # Write a test
    pass

# Generated at 2022-06-13 08:10:27.882836
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():

    from ansible.playbook.block import Block

    host = Host("localhost")
    handler = Handler("test handler", host)

    variable_manager = VariableManager()
    variable_manager.set_inventory(Inventory(hosts=[host]))

    variable_manager.set_extra_vars(
        dict(
            # Test for required keys.
            name="test handler load",
            block=Block("test handler load block", handler),
            role=Role("test handler load role"),
            task_include=TaskInclude("test handler load task include"),
            variable_manager=variable_manager,
            loader=None,
        )
    )

    # Test for missing required keys.
    assert_raises(AnsibleParserError, HandlerTaskInclude.load, data=dict(), variable_manager=variable_manager)

    # Test for

# Generated at 2022-06-13 08:10:28.697760
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    HandlerTaskInclude()

# Generated at 2022-06-13 08:10:43.104470
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    # pylint: disable=protected-access
    # unit test for method load of class HandlerTaskInclude
    # simple function definition with default argument
    handler = HandlerTaskInclude.load(
        data=dict(
            include=dict(
                tasks="tasks.yml",
            ),
            listen="my_event",
        ),
        variable_manager=None,
        loader=None
    )

    assert handler == {
        '_block': None,
        '_role': None,
        'listen': 'my_event',
        '_attributes': {
            'free-form': []
        },
        '_task_include': None,
        'static': False,
        'include': {
            'tasks': 'tasks.yml'
        },
        '_parent': None
    }

# Generated at 2022-06-13 08:10:46.457888
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    _block = None
    _role = None
    _task_include = None
    data = {'listen': 'tomcat'}
    t = HandlerTaskInclude(block=_block, role=_role, task_include=_task_include)
    handler = t.check_options(
        t.load_data(data, variable_manager=None, loader=None),
        data
    )
    assert handler is not None


# Generated at 2022-06-13 08:10:48.871049
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    a = HandlerTaskInclude()
    assert a.__class__.__name__ == "HandlerTaskInclude"

# Generated at 2022-06-13 08:11:01.917547
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.handler import Handler
    from ansible.inventory.host import Host
    from ansible.playbook.role import Role
    from ansible.playbook.block import Block

    # host create
    host1 = Host()
    # role create
    role1 = Role()
    block1 = Block()

    data = {
        "include": "name:{{item}}",
        "loop": {"x": "range(5)"},
        "loop_control": {"name": "item"},
    }
    data = HandlerTaskInclude.load(data, block=block1, role=role1, task_include=TaskInclude.load(data,block=block1, role=role1), variable_manager=None, loader=None)

# Generated at 2022-06-13 08:11:17.398312
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():

    # Create a HandlerTaskInclude object
    # "handler": {
    #     "include": {
    #         "tasks": "tasks_dir/test.yaml"
    #     }
    # }
    #
    # => tasks: tasks_dir/test.yaml
    data = {
        "include": {
            "tasks": "tasks_dir/test.yaml"
        }
    }
    handler = HandlerTaskInclude.load(data)

    # Check type of object to be sure it is a HandlerTaskInclude object
    assert isinstance(handler, HandlerTaskInclude)

    # Check type of attribute handler.task_include to be sure it is a TaskInclude object
    assert isinstance(handler.task_include, TaskInclude)

    # Check value of attribute handler.task_include
   

# Generated at 2022-06-13 08:11:21.292905
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    t = HandlerTaskInclude(block=None, role=None, task_include=None)
    assert t._block == None
    assert t._load_role == None
    assert t._task_include == None

# Generated at 2022-06-13 08:11:25.320300
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():

    data = """
    - include: add_host.yml
      name: webhosts
      listen:
        - webtier
    """
    handlers = HandlerTaskInclude.load(data)
    assert handlers == {'webtier': {'tasks': [{'include': {'include': 'add_host.yml', 'name': 'webhosts'}}]}}

# Generated at 2022-06-13 08:11:30.515960
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    h = HandlerTaskInclude(
        block=None,
        role=None,
        task_include=None,
        exclude_hosts=None,
        only_hosts=None,
        name=None,
        include_paths=None,
        loop=None,
        loop_args=None
    )

    return h


# Generated at 2022-06-13 08:11:31.925447
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    pass
# vim: set expandtab ts=4 sw=4 ai :

# Generated at 2022-06-13 08:11:42.763553
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    class TaskInclude:
        VALID_INCLUDE_KEYWORDS = set()

    class VariableManager:
        def __init__(self):
            pass

    class Loader:
        def __init__(self):
            pass

    handler = HandlerTaskInclude()
    handler.VALID_INCLUDE_KEYWORDS = set()
    handler_data = dict()
    handler_data["name"] = "test_HandlerTaskInclude_load"
    handler_data["notification"] = "test_HandlerTaskInclude_load"
    handler_data["include"] = "test_HandlerTaskInclude_load"

    handler_task_include = HandlerTaskInclude()
    handler_task_include_data = dict()
    handler_task_include_data = handler_data

    handler_task_include.TaskIn

# Generated at 2022-06-13 08:11:43.874683
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    pass



# Generated at 2022-06-13 08:11:51.218290
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.role import Role

    # Create a simple task for test purpose
    task_test = Task()
    task_test._role = Role()
    block = Block()

    # define a set of options for test purpose
    # Expected result: an instance of HandlerTaskInclude
    task_include_data1 = {
        u"handler": {
            "include": "test_handler_include.yml"
        }
    }
    result_load1 = HandlerTaskInclude.load(
        task_include_data1, block=block, role=task_test._role, task_include=task_test
    )
    assert isinstance(result_load1, HandlerTaskInclude)

    # define a set

# Generated at 2022-06-13 08:11:51.831905
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    assert True

# Generated at 2022-06-13 08:11:52.547295
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    pass



# Generated at 2022-06-13 08:12:07.922627
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    print("test_HandlerTaskInclude()")
    data = dict(something=1, something_else=2, something_more=3)
    h = HandlerTaskInclude(None, None, data)
    assert data == h.copy(), "copy() did not retain all data"
    assert h.get_vars() == data, "get_vars() did not return all data"
    assert h.is_handler()  # it's a handler
    assert not h.is_import_role()  # it's not import role
    assert not h.is_notify()  # it's not notify
    assert not h.is_include()  # it's not include
    assert not h.is_poll_async()  # it's not poll async
    assert not h.any_errors_fatal()  # it's not poll async


# Generated at 2022-06-13 08:12:12.727547
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    """
    unit test for method HandlerTaskInclude
    """

    for loop in range(100):
        test_data = {}
        HandlerTaskInclude(
            block=test_data,
            role=test_data,
            task_include=test_data
        )

# Generated at 2022-06-13 08:12:25.551273
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.inventory.host import Host
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    data = '''
       - include_tasks: some_file.yml
         listen:
           - name: foo
             connection: local
             when: "'foo' in ansible_play_name"
           - name: bar
             connection: local
             when: "'bar' in ansible_play_name"
         when: "'abc' in ansible_play_name"
    '''
    data = '\n'.join([x.strip() for x in data.split()])

    loader = DataLoader()
    host = Host("127.0.0.1")
    variable_manager = VariableManager([], loader=loader)

    handler = HandlerTaskIn

# Generated at 2022-06-13 08:12:31.831623
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    data = {'hosts': 'hosts/hosts.yaml', 'tasks': 'tasks/tasks.yaml'}
    t = HandlerTaskInclude(block=None, role=None, task_include=None)
    handler = t.check_options(
        t.load_data(data, variable_manager=None, loader=None),
        data
    )
    assert handler

# Generated at 2022-06-13 08:12:36.165459
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    data = {'block': ['', ''], 'role': '', 'task_include': ''}
    HandlerTaskInclude.load(data, block=None, role=None, task_include=None, variable_manager=None, loader=None)
    assert data == {'block': ['', ''], 'role': '', 'task_include': ''}

# Generated at 2022-06-13 08:12:42.978206
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
	from ansible.inventory.host import Host
	from ansible.playbook.handler import Handler
	data = {'include': './playbook.include.yml'}
	block = None
	role = None
	task_include = [ TaskInclude.load(data, play=None, variable_manager=None, loader=None) ]
	variable_manager = None
	loader = None
	t = HandlerTaskInclude(block=block, role=role, task_include=task_include)
	assert isinstance(t, HandlerTaskInclude)
	assert isinstance(t, Handler)
	assert isinstance(t, TaskInclude)


# Generated at 2022-06-13 08:12:43.661399
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    # GIVEN
    # WHEN
    # THEN
    pass

# Generated at 2022-06-13 08:12:44.405556
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    HandlerTaskInclude.load()
    return 0



# Generated at 2022-06-13 08:12:45.497331
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    handler = HandlerTaskInclude()
    assert handler

# Generated at 2022-06-13 08:12:47.569729
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    assert issubclass(HandlerTaskInclude, Handler)
    assert issubclass(HandlerTaskInclude, TaskInclude)


# Generated at 2022-06-13 08:12:57.471431
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.inventory.host import Host
    from ansible.playbook.block import Block
    from ansible.playbook.role import Role
    t = HandlerTaskInclude()
    host = Host(name='localhost')
    block = Block()
    role = Role()

    handler = t.load(dict(
        name='test',
        include=dict(
            module='test_test'
        )
    ), block, role, t, host)
    assert handler is not None

# Generated at 2022-06-13 08:13:04.260233
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    data = {}
    block = 'block'
    role = 'role'
    task_include = 'task_include'
    variable_manager = 'variable_manager'
    loader = 'loader'
    test = HandlerTaskInclude.load(
        data,
        block,
        role,
        task_include,
        variable_manager,
        loader
    )
    print(test)
    assert isinstance(test, HandlerTaskInclude)



# Generated at 2022-06-13 08:13:05.773395
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    handler_task_include = HandlerTaskInclude()
    assert handler_task_include is not None

# Generated at 2022-06-13 08:13:10.946220
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    yamlstr = \
"""
- name: test handler
  include: test_handler.yaml
"""
    handler = Handler.load(data=yamlstr, variable_manager=None, loader=None)
    assert isinstance(handler, HandlerTaskInclude)

# Generated at 2022-06-13 08:13:13.651760
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    assert HandlerTaskInclude.load(data={}, block=None, role=None, task_include=None, variable_manager=None, loader=None) is not None

# Generated at 2022-06-13 08:13:15.792505
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    pass


# Generated at 2022-06-13 08:13:29.069908
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    yaml = """
---
- include: test.yml
  when: 1==2
"""
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.playbook_executor import PlaybookExecutor
    import os
    currentdir = os.path.dirname(os.path.realpath(__file__))
    parentdir = os.path.dirname(currentdir)
    yamlfile = parentdir + "/data/test.yml"
    #loader = DataLoader(yaml)
    #VariableManager(loader=loader)
    loader = DataLoader()
    play_context = PlayContext()
   

# Generated at 2022-06-13 08:13:38.922350
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    from ansible.template import Templar
    from ansible.inventory.host import Host
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    test_handler_task_include_data = {
    'block': None,
    'listen': None,
    'role': None,
    'task_include': None,
    'tags': None,
    'when': None,
    'include': './test_data/test_statements_handler.yml',
    'include_tasks': None,
    'static': False,
    'register': None,
    }
    variable_manager = VariableManager()


# Generated at 2022-06-13 08:13:42.907674
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    hti = HandlerTaskInclude.load(
        dict(
            include="test.yml"
        ),
        variable_manager=None,
        loader=None,
        task_include=TaskInclude(block=None, role=None, task_include=None)
    )
    assert hti.static_handler is True
    assert hti.handler_name == "test.yml"
    assert hti.handler_block == None

# Generated at 2022-06-13 08:13:44.127243
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    data = {'name':'test', 'listen':'blah'}
    handler = HandlerTaskInclude.load(data)

# Generated at 2022-06-13 08:13:56.139087
# Unit test for method load of class HandlerTaskInclude

# Generated at 2022-06-13 08:13:58.053739
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    assert HandlerTaskInclude(block=None, role=None, task_include=None) is not None

# Generated at 2022-06-13 08:14:05.112765
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.plugins.loader import action_loader
    import ansible.playbook.role.task
    from ansible.playbook.block import Block
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.loader.manager import LoaderManager
    from ansible.compat.tests import unittest
    import os

    class TestHandlerTaskInclude(unittest.TestCase):

        def setUp(self):
            current_dir = os.path.dirname(__file__)
            self.current_dir = current_dir

# Generated at 2022-06-13 08:14:18.955015
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.playbook.task import Task
    from ansible.playbook.role_include import RoleInclude
    from ansible.playbook.block import Block
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.group import Group
    from ansible.inventory.host import Host
    from ansible.template import Templar

    data = [{'debug': 'msg={{ var.value }}'}, {'debug': 'msg={{ var.value }}'}]
    block = Block(None)
    role = RoleInclude()
    role._role_name = 'role1'
    task_include = TaskInclude()
    task_include._include_name = 'task_include1'
    task = Task()
    task._role

# Generated at 2022-06-13 08:14:28.236350
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    data = """
    - handler:
        name: test_handler
        tags: test
        listen: test
    """
    # VariableManager, Loader object
    variable_manager = 'variable_manager'
    loader = 'loader'

    # Call load method of class HandlerTaskInclude
    obj = HandlerTaskInclude.load(data, variable_manager=variable_manager, loader=loader)

    # Check the class of object
    assert isinstance(obj, HandlerTaskInclude) == True

    # Check the values of attributes
    assert obj.get_name() == 'test_handler'
    assert obj.get_tags() == ['test']
    assert obj._metadata == None

    # Check the class of attributes
    assert isinstance(obj.get_name(), str) == True

# Generated at 2022-06-13 08:14:36.373906
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    ts_task_include = TaskInclude.load(data={"include_tasks": "/path/to/some/file.yaml"}, block=None, role=None, task_include=None)
    assert ts_task_include.include_tasks == ['/path/to/some/file.yaml']
    assert ts_task_include.include_role == []
    assert ts_task_include.include_vars == []
    assert ts_task_include.include_lines == []
    assert ts_task_include.loop_control == {}

# Generated at 2022-06-13 08:14:37.397591
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    handler = HandlerTaskInclude()

# Generated at 2022-06-13 08:14:39.050240
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    #Test load with no arguments passed to it.
    test_instance = HandlerTaskInclude()


# Generated at 2022-06-13 08:14:47.112283
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():

    from ansible.inventory.group import Group
    from ansible.inventory.host import Host
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    # Create host, group and inventory
    myhost = Host(name="myhost")
    mygroup = Group(name="mygroup")
    mygroup.add_host(myhost)
    inventory = mygroup.get_inventory()
    variable_manager = VariableManager(loader=DataLoader())
    variable_manager.set_inventory(inventory)

    # Create data for constructor
    data = {
        "include": "do_something.yml",
        "vars": {"var1": "var1"},
        "vars_files": ["/file1", "/file2"],
    }

    # Test constructor
   

# Generated at 2022-06-13 08:14:55.556436
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    #Test with no arguments
    try:
        t = HandlerTaskInclude(block=None, role=None, task_include=None)
    except:
        raise
        assert False
    
    #Test with arguments
    try:
        block = [{"action": {"module": "shell", "args": "uptime"}}]
        role = "test role"
        task_include = {"name": "test"}
        t = HandlerTaskInclude(block=block, role=role, task_include=task_include)
    except:
        raise
        assert False



# Generated at 2022-06-13 08:15:17.712268
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    handler = HandlerTaskInclude()
    assert isinstance(handler, HandlerTaskInclude)


# Generated at 2022-06-13 08:15:18.784949
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    handler = HandlerTaskInclude()

    assert handler is not None

# Generated at 2022-06-13 08:15:19.264667
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    pass

# Generated at 2022-06-13 08:15:25.563335
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    host_list = [{
        "hostname": "test1",
        "ip": "192.168.5.129",
        "port": 22,
        "username": "root",
        "password": "toor",
        "private_key": "/root/.ssh/id_rsa"
        # "host_keys":"/etc/ssh/ssh_host_rsa_key",
        # "host_keys_vim":"/etc/ssh/ssh_host_rsa_key.pub"
    }]

    # host = Host(host_list[0])
    # variable_manager = VariableManager()
    # variable_manager.set_inventory(inventory)
    # variable_manager.extra_vars = {'': 'my_private_key', '': False, '':
    # 'cc7-LZ01-os.

# Generated at 2022-06-13 08:15:31.412707
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    # given
    data = {'include': 'some/path.yaml', 'listen': 'some_task'}
    block = None
    role = None
    task_include = None
    variable_manager = None
    loader = None

    # when
    handler = HandlerTaskInclude.load(data, block, role, task_include, variable_manager, loader)

    # then
    assert handler.static_vars['listen'] == 'some_task'

# Generated at 2022-06-13 08:15:32.910723
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    handler = HandlerTaskInclude()
    assert handler is not None

# Generated at 2022-06-13 08:15:37.312749
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    data = {'hosts': 'host_name_one'}
    block = {}
    role = {}
    task_include = {}
    variable_manager = {}
    loader = {}
    assert HandlerTaskInclude.load(data, block, role, task_include, variable_manager, loader)


# Generated at 2022-06-13 08:15:43.202095
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    data = {u'listen': u'compute_remove', 'include': 'os-compute.yml'}
    handler = HandlerTaskInclude.load(data)
    assert handler._block == None
    assert handler._role == None
    assert handler._task_include == ""

# Generated at 2022-06-13 08:15:48.496522
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    data = {'name': 'test', 'listen': 'x', 'include': 'z'}
    obj = HandlerTaskInclude()
    handler = obj.load(data)

    assert obj.__class__ == HandlerTaskInclude
    assert handler.__class__ == HandlerTaskInclude

# Generated at 2022-06-13 08:15:53.156314
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    data = {}
    block = {}
    role = {}
    task_include = {}
    variable_manager = {}
    loader = {}

    handler = HandlerTaskInclude.load(data, block, role, task_include, variable_manager, loader)