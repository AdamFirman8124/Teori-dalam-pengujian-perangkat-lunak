

# Generated at 2022-06-13 08:09:59.969723
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    pass



# Generated at 2022-06-13 08:10:08.130888
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    import os
    import sys
    import unittest2 as unittest

    class TestHandlerTaskInclude_load(unittest.TestCase):
        def test_load(self):
            current_directory = os.path.dirname(__file__)
            parent_directory = os.path.dirname(current_directory)
            sys.path.append(parent_directory)
            from ansible.parsing import DataLoader
            from ansible.inventory.manager import InventoryManager
            from ansible.vars import VariableManager
            variable_manager = VariableManager()
            loader = DataLoader()
            variable_manager.set_loader(loader)
            variable_manager.set_inventory(InventoryManager(loader=loader, sources=current_directory + "/hosts"))

# Generated at 2022-06-13 08:10:12.776295
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    # Setup
    data = 'handler.yaml'
    block = None
    role = None
    task_include = None
    variable_manager = None
    loader = None

    # Exercise
    handler = HandlerTaskInclude.load(data, block, role, task_include, variable_manager, loader)

    # Verify
    assert handler.name == 'include' and handler.tags == ['include', 'task']


# Generated at 2022-06-13 08:10:19.230935
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():

    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.group import Group
    from ansible.inventory.host import Host
    from ansible.playbook.block import Block
    from ansible.playbook.play import Play

    variable_manager = VariableManager()
    loader = DataLoader()
    inventory = variable_manager.get_inventory()
    host = Host(name='host')
    group = Group(name='group')
    group.add_host(host)
    inventory.add_group(group)
    variable_manager.set_inventory(inventory)

    data = {"listen": "notify_change"}
    block = Block()
    block._parent = Play()


# Generated at 2022-06-13 08:10:20.139399
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    assert False, "TODO"

# Generated at 2022-06-13 08:10:20.814659
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    pass

# Generated at 2022-06-13 08:10:21.323624
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    assert False

# Generated at 2022-06-13 08:10:31.405407
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    data = {
        'tags': 'all,new-config',
        'name': 'Startup config synced to disk',
        'handler': 'meta:sync_config',
        'listen': 'new-config'
    }
    e = HandlerTaskInclude.load(data, block=None, role=None, task_include=None, variable_manager=None, loader=None)
    assert e.get_name() == 'Startup config synced to disk'

#     def __init__(self, block=None, role=None, task_include=None):
#         self.block = block
#         self.role  = role
#         TaskInclude.__init__(self, task_include, load_role=False)
#         self._role_name = role.get_name() if role is not None else None

# Generated at 2022-06-13 08:10:37.317957
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    test_data = [
        {
            "name": "test handler",
            "action": {
                "module": "test_module",
                "param1": "param1"
            }
        }
    ]
    handler = HandlerTaskInclude.load(test_data)
    assert handler.name == "test handler"
    assert handler.action["module"] == "test_module"
    assert handler.action["param1"] == "param1"
    assert handler.action["args"] == dict()

# Generated at 2022-06-13 08:10:40.270295
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    hti=HandlerTaskInclude()
    hti.load('handler.yml',block=None,role=None,task_include=None,variable_manager=None,loader=None)
    return hti

# Generated at 2022-06-13 08:10:45.712653
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    from ansible.playbook.block import Block
    from ansible.parsing.loader import DataLoader
    from ansible.vars.manager import VariableManager

    block = Block(None, 'test', [])
    data = dict(include='test')
    loader = DataLoader()
    variable_manager = VariableManager()
    obj = HandlerTaskInclude.load(data, block, task_include=True, loader=loader, variable_manager=variable_manager)
    assert isinstance(obj, HandlerTaskInclude)

# Generated at 2022-06-13 08:10:55.708069
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    import os
    import sys
    import unittest
    from ansible.errors import AnsibleError
    from ansible.module_utils.six import PY3, iteritems
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.role import Role
    from ansible.playbook.role_path import RolePath
    from ansible.playbook.block import Block
    from ansible.template import Templar
    from ansible.utils.vars import combine_vars

    test_dir = os.path.dirname(os.path.realpath(__file__))
    sys.path.append(test_dir + "/../")
    sys.path.append(test_dir + "/../ansible")
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group



# Generated at 2022-06-13 08:10:57.632817
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    print("Unit test for method load of class HandlerTaskInclude")
    print("Not implemented")

# Generated at 2022-06-13 08:11:01.083910
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    handler_task_include = HandlerTaskInclude()
    data = {'listen': "hello world"}
    handler = handler_task_include.load(data)

# Generated at 2022-06-13 08:11:06.100575
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.inventory.manager import InventoryManager
    from ansible.inventory.script import InventoryScript
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.role import Role
    from ansible.playbook.block import Block
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.template import Templar

    loader = DataLoader()
    results = Template.load({ "block": Block(), "role": Role() }, loader)

    assert isinstance(results, type(Block)) is True
    assert isinstance(results, Block) is True



# Generated at 2022-06-13 08:11:09.621992
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    # set input parameters
    block = None
    role = None
    task_include = None

    HandlerTaskInclude(block=block, role=role, task_include=task_include)

# Generated at 2022-06-13 08:11:11.944847
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    ut = HandlerTaskInclude()
    assert ut.__class__.__name__ == 'HandlerTaskInclude'

# Generated at 2022-06-13 08:11:22.817167
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    import sys
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    
    if sys.version_info.major == 2:
        import __builtin__ as builtins
    else:
        import builtins

    myhost = Host()
    myhost.set_variable('foo', 'bar')
    group = Group()
    group.add_host(myhost)
    inventory = InventoryManager(loader=DataLoader(), groups={"group": group})
    variable_manager = VariableManager(loader=DataLoader(), inventory=inventory)
    data = {"include": "role", "name": "foobar"}
    handler = HandlerTask

# Generated at 2022-06-13 08:11:29.757575
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    # Check the constructor without any params
    handler_task_include = HandlerTaskInclude()
    assert handler_task_include.block is None
    assert handler_task_include.role is None
    assert handler_task_include.task_include is None

    handler_task_include = HandlerTaskInclude(block='block', role='role', task_include='task_include')
    assert handler_task_include.block == 'block'
    assert handler_task_include.role == 'role'
    assert handler_task_include.task_include == 'task_include'

# Generated at 2022-06-13 08:11:31.649118
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    data = {'include': 'test.yml'}
    return HandlerTaskInclude.load(data)

# Generated at 2022-06-13 08:11:44.562423
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    h = HandlerTaskInclude()
    assert isinstance(h, Handler)
    assert isinstance(h, TaskInclude)
    assert hasattr(h, 'static')
    assert not hasattr(h, 'STATIC')
    assert hasattr(h, 'static_add')
    assert not hasattr(h, 'STATIC_ADD')
    assert not hasattr(h, 'static_remove')
    assert not hasattr(h, 'STATIC_REMOVE')
    assert not hasattr(h, 'static_exact')
    assert not hasattr(h, 'STATIC_EXACT')
    assert hasattr(h, '_run')
    assert hasattr(h, '_load_role_vars')
    assert hasattr(h, 'check_options')

# Generated at 2022-06-13 08:11:50.164587
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    hti = HandlerTaskInclude()
    data = {
        "include": "my_playbook.yml",
        "tags": "all",
        "listen": "task_notify"
    }
    result = hti.load(data)
    assert result == {
        "tags": {"all": ["all"]},
        "listen": [{"task_notify": {"task_notify": "task_notify"}}],
        "include": [{"include": "my_playbook.yml"}],
        "when": []
    }

# Generated at 2022-06-13 08:11:59.259015
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    results = []
    VALID_INCLUDE_KEYWORDS = TaskInclude.VALID_INCLUDE_KEYWORDS
    assert results.append(VALID_INCLUDE_KEYWORDS.union(('listen',)))

    VALID_INCLUDE_KEYWORDS = TaskInclude.VALID_INCLUDE_KEYWORDS.union(('listen',))
    results.append(VALID_INCLUDE_KEYWORDS)

    assert results[-1] == {'static', 'tasks', 'meta', 'role', 'listen'}
    assert results[-2] == {'static', 'tasks', 'meta', 'role', 'listen'}

    def load_data(data, variable_manager, loader):
        return variable_manager, loader, data

    assert load

# Generated at 2022-06-13 08:12:00.604707
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    # Create the object HandlerTaskInclude without arg
    HandlerTaskInclude()

# Generated at 2022-06-13 08:12:06.699018
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.playbook.task import Task
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.role import Role
    from ansible.playbook.block import Block
    from ansible.playbook.play import Play
    from ansible.utils.vars import combine_vars
    from ansible.utils.vars import load_extra_vars

    block = Block()
    host = Host(name='localhost')
    group = Group(name=None, hosts=[host])
    task = Task(name='tasks')
    role = Role()
    loader = DataLoader()
    variable_manager = VariableManager()
    play = Play()


# Generated at 2022-06-13 08:12:10.441291
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    test_data = {
        "include": {"file": "ansible/test/handler_include_test"},
        "listen": "notify_test"
    }
    
    result = Handler.load(test_data)
    assert isinstance(result, Handler)
    assert isinstance(result, HandlerTaskInclude)

# Generated at 2022-06-13 08:12:11.670189
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    pass


# Generated at 2022-06-13 08:12:15.571555
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    # Constructor method for class HandlerTaskInclude
    HandlerTaskInclude.load(data=None, block=None, role=None, task_include=None, variable_manager=None, loader=None)

# Generated at 2022-06-13 08:12:26.603763
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    data = dict(
        name='ndn_init',
        events='on-failure',
        handlers='include ndn_handlers.yml'
    )

    handler = Handler.load(data, block=None, role=None, task_include=None)

    assert handler.__class__.__name__ == 'Handler'
    assert handler._attrs == dict(
        handlers='include ndn_handlers.yml',
        events='on-failure',
        name='ndn_init'
    )

    # test that include_tasks is converted to a handler with include
    data = dict(
        handlers='include_tasks ndn_handlers.yml'
    )
    handler = Handler.load(data, block=None, role=None, task_include=None)
    assert handler.__class__

# Generated at 2022-06-13 08:12:37.026295
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    """
    Test HandlerTaskInclude.load() method
    """

    # Load a HandlerTaskInclude object from the given data
    def load_handler_task_include(data):
        # Create a mock Block object
        class MockBlock(object):
            pass
        block = MockBlock()

        # Create a mock Role object
        class MockRole(object):
            pass
        role = MockRole()

        # Create a mock TaskInclude object
        class MockTaskInclude(object):
            pass
        task_include = MockTaskInclude()

        handler = HandlerTaskInclude.load(data, block=block, role=role, task_include=task_include)
        return handler

    # Test the data