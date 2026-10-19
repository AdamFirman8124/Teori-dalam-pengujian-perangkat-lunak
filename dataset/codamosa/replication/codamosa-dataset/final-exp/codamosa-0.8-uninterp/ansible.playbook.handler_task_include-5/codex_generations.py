

# Generated at 2022-06-13 08:10:08.131262
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.inventory.group import Group
    from ansible.inventory.host import Host
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    data = dict(
        name='test',
        hosts=['all'],
        tasks=[{'name': 'debug', 'debug': 'msg="{{ item }}"'},
               {'name': 'debug', 'include': 'test'}]
    )
    data2 = dict(
        name='test',
        include='test'
    )
    play = Play().load(data, variable_manager=VariableManager(), loader=DataLoader())
    block = play.compile()

    # Create host, group and inventory.
    variable_manager = VariableManager()
   

# Generated at 2022-06-13 08:10:09.877291
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    task_include = HandlerTaskInclude.load(data={'tags': ['cust_tag']})
    assert task_include != None


# Generated at 2022-06-13 08:10:17.495697
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.inventory.host import Host
    from ansible.vars.manager import VariableManager
    from ansible.vars.hostvars import HostVars
    from ansible.vars.hostvars import HostVarsVars
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.block import Block
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.role import Role
    from ansible.playbook.play_context import PlayContext
    from ansible import context
    import unittest
    import sys
    import os


# Generated at 2022-06-13 08:10:18.829247
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    handler = HandlerTaskInclude()
    assert handler is not None

# Generated at 2022-06-13 08:10:28.319074
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    handler_task_include = HandlerTaskInclude()
    handler_task_include.task_include = None
    handler_task_include.block = None
    handler_task_include.role = None
    handler_task_include.name = 'test_handler_task_include'
    handler_task_include.tasks = None
    handler_task_include.loop = None
    handler_task_include.always = None
    handler_task_include.tags = None
    handler_task_include.register = None
    handler_task_include.run_once = None
    handler_task_include.include_role = None

    data = dict(
        name = "test_handler",
        tasks = None
    )


# Generated at 2022-06-13 08:10:35.832692
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    data = dict(
        name='test',
        listen='stop',
    )
    handler = HandlerTaskInclude(block=None,
                  role=None,
                  task_include=None)

    result = handler.load(data=data,
                          variable_manager=None,
                          loader=None)

    assert result.name == 'test'
    assert result.listen == 'stop'

# Generated at 2022-06-13 08:10:39.099975
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    data = dict(something=dict(a=1,b=2))
    handler = HandlerTaskInclude.load(data)
    assert handler.something.a == 1
    assert handler.something.b == 2


# Generated at 2022-06-13 08:10:40.486645
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    pass
HandlerTaskInclude.load = test_HandlerTaskInclude_load


# Generated at 2022-06-13 08:10:43.240326
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    handler = HandlerTaskInclude()
    assert handler.__class__.__name__ == 'HandlerTaskInclude'

# Generated at 2022-06-13 08:10:48.448258
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.errors import AnsibleParserError
    from ansible.inventory.host import Host
    from ansible.playbook.block import Block
    from ansible.playbook.role.include import RoleInclude
    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins.loader import get_all_plugin_loaders
    from ansible.utils.vars import combine_vars
    from ansible.vars.manager import VariableManager

    block = Block(
        parent_block=None,
        role=None,
        task_include=RoleInclude(),
        use_handlers=True,
        play_context=PlayContext()
    )
    loader, _, _ = get_all_plugin_loaders()
    variable_manager = VariableManager

# Generated at 2022-06-13 08:10:50.886576
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    pass


# Generated at 2022-06-13 08:10:51.718688
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    assert HandlerTaskInclude()

# Generated at 2022-06-13 08:10:54.346141
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    assert HandlerTaskInclude.VALID_INCLUDE_KEYWORDS == set(['tasks', 'block', 'listen'])

# Generated at 2022-06-13 08:11:05.028168
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    import sys
    import os
    import unittest

    elementPath = os.path.join(os.path.dirname(__file__), '../../../../lib/ansible/playbook/task_include.py')
    sys.path.append(os.path.dirname(elementPath))

    task_includePath = os.path.join(os.path.dirname(__file__), '../../../../lib/ansible/playbook/task_include.py')
    sys.path.append(os.path.dirname(task_includePath))

    from task_include import TaskInclude

    # hack for unit test
    class FakeTaskInclude:

        @staticmethod
        def load(data, block=None, role=None, task_include=None, variable_manager=None, loader=None):
            t

# Generated at 2022-06-13 08:11:19.018400
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():

    try:
        from ansible.inventory.host import Host
    except:
        from collections import namedtuple
        Host = namedtuple("Host", "name port")

    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.block import Block
    from ansible.template import Templar
    from ansible.plugins.loader import HandlerLoader
    from ansible.plugins.connection import ConnectionLoader

    def get_loader(data=None):
        if data is None:
            data = dict()
        loader = DataLoader()
        if data is not None:
            if 'host_vars' in data:
                loader.set_basedir(data['host_vars'])
            if 'group_vars' in data:
                loader.set_

# Generated at 2022-06-13 08:11:21.382037
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    h = HandlerTaskInclude()


if __name__ == '__main__':
    test_HandlerTaskInclude_load()

# Generated at 2022-06-13 08:11:21.934452
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    pass

# Generated at 2022-06-13 08:11:32.074359
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    data = {
        "include": "test",
        "static": {
            "hosts": ["all"]
        },
        "tags": [
            "a", "b"
        ]
    }
    handler = HandlerTaskInclude.load(data)
    assert handler.include == "test"
    assert handler.static == {'hosts': ['all']}
    assert handler.tags == set(['a', 'b'])


    data = {
        "include": "test",
        "async_status_poll": {}
    }
    handler = HandlerTaskInclude.load(data)
    assert handler.include == "test"
    assert handler.async_status_poll == {}

    # this data would result from yaml parsing

# Generated at 2022-06-13 08:11:36.227612
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    try:
        block = None
        role = None
        task_include = None
        ansib_test = HandlerTaskInclude(block, role, task_include)
    except:
        print("Failed")

test_HandlerTaskInclude()

# Generated at 2022-06-13 08:11:43.393833
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    # test to load the data
    def test_load1():
        data = {
            'name':'Name For Handler',
            'local_action': 'fail'
        }
        handler = HandlerTaskInclude.load(data)
        assert handler.name == 'Name For Handler'

    # test to load the data without name
    def test_load2():
        data = {
            'local_action': 'fail'
        }
        handler = HandlerTaskInclude.load(data)
        assert handler.name is None

# Generated at 2022-06-13 08:11:53.125577
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    """
    This is a unit test for the load method of class HandlerTaskInclude
    """
    data = {
        'listen': 'task_1',
        'module_name': 'shell',
        'module_args': 'echo "This is task 1"'
    }
    block = None
    role = None
    task_include = None
    variable_manager = None
    loader = None
    handler = HandlerTaskInclude.load(
        data=data,
        block=block,
        role=role,
        task_include=task_include,
        variable_manager=variable_manager,
        loader=loader
    )
    assert handler.listen == 'task_1'

# Generated at 2022-06-13 08:11:59.237679
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    """Unit test for class HandlerTaskInclude method load

    A test case that load method of HandlerTaskInclude class
    will pass the test.

    """

    # TODO: Pass a complex `data` object here and make sure the `return`ed object isn't modified
    # TODO: Test that `handler` is a valid object
    pass

# Generated at 2022-06-13 08:11:59.977304
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    pass

# Generated at 2022-06-13 08:12:10.485767
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():

    from ansible.errors import AnsibleParserError

    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.task_elem import TaskElement
    from ansible.playbook.task_helpers import TaskResult

    from ansible.playbook.role import Role

    from ansible.plugins.action.debug import ActionModule

    block = Block(
        parent_block=None,
        role=None,
        task_include=None,
        use_role=None,
        use_task_include=None,
    )

    role = Role(
        _role_name='env-prod',
        _role_path='roles/env-prod',
        _task_blocks=[],
    )


# Generated at 2022-06-13 08:12:12.519143
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    data = {'listen': 'task_result'}
    handler = HandlerTaskInclude.load(data=data)
    assert handler.notify is ['task_result']

# Generated at 2022-06-13 08:12:15.066765
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    handler = HandlerTaskInclude(block=None, role=None, task_include=None)
    assert handler.__class__.__name__ == 'HandlerTaskInclude'

# Generated at 2022-06-13 08:12:26.421226
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():

    from ansible.playbook.play import Play

    # Incomplete data
    data = {}
    try:
        HandlerTaskInclude.load(data)
        raise Exception("Expected exception was not raised")
    except Exception as e:
        assert(str(e) == "Include tasks require more than just a name be defined")

    # Invalid data
    data = {'name': 'something', 'invalid_task_include_option': 'something'}
    try:
        HandlerTaskInclude.load(data)
        raise Exception("Expected exception was not raised")
    except Exception as e:
        assert(str(e) == "invalid task include option: invalid_task_include_option")

    # Valid data
    data = {'name': 'something'}

# Generated at 2022-06-13 08:12:28.978425
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    handler1 = TaskInclude()
    handler2 = HandlerTaskInclude(handler1)


# Generated at 2022-06-13 08:12:30.659152
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    constructor = HandlerTaskInclude()
    assert constructor.VALID_INCLUDE_KEYWORDS is not None

# Generated at 2022-06-13 08:12:31.205508
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    HandlerTaskInclude()

# Generated at 2022-06-13 08:12:44.197580
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    # Test with "handler" keyword
    data = {
        "tasks": [
            {
                "name": "Test Task",
                "include": "my_handler"
            }
        ],
        "handlers": [
            {
                "name": "Test Handler",
                "tasks": [
                    {
                        "name": "Test Subhandler"
                    }
                ]
            },
            {
                "name": "my_handler",
                "tasks": [
                    {
                        "name": "Test Subhandler"
                    }
                ]
            }
        ]
    }

    # HandlerTaskInclude.load(data)
    # Test without "handler" keyword

# Generated at 2022-06-13 08:12:51.015076
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    """
    Test:
        def load(data, block=None, role=None, task_include=None, variable_manager=None, loader=None)
    """

    data = {'listen': 'test1', 'block': 'someblock', 'include': 'test2'}
    block = 'someblock'

    t = HandlerTaskInclude(block=block)
    handler = t.check_options(data, data)
    assert handler.block == block
    assert handler.listen == 'test1'
    assert handler.include == 'test2'

# Generated at 2022-06-13 08:12:54.613175
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    data = '''
    - include: test.yml
      vars:
        var1: "val1"
    '''

    handler = HandlerTaskInclude.load({}, data)
    print(handler)

# Generated at 2022-06-13 08:13:06.787035
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():

    # Testing Invalid "include" keyword
    data = {'include': 'somefile'}
    h = HandlerTaskInclude(block=None, role=None, task_include=None)
    h1 = HandlerTaskInclude.load(data)
    assert h.load_data(data) == h1.load_data(data)

    data = {'include': 'somefile'}
    h = HandlerTaskInclude(block=None, role=None, task_include=None)
    h1 = HandlerTaskInclude.load(data)
    assert h.load_data(data) == h1.load_data(data)

    # Testing Invalid "include_vars" keyword
    data = {'include_vars': 'somefile'}

# Generated at 2022-06-13 08:13:16.701560
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    """Test the load method of class HandlerTaskInclude"""
    import ansible.playbook.handler
    import ansible.playbook.task_include

    def mock_TaskInclude_load(self, data, block=None, role=None, task_include=None, variable_manager=None, loader=None):
        pass
    ansible.playbook.task_include.TaskInclude.load = mock_TaskInclude_load

    def mock_Handler_load(self, data, block=None, role=None, task_include=None, variable_manager=None, loader=None):
        pass
    ansible.playbook.handler.Handler.load = mock_Handler_load

    # We need to set block, role and task_include

# Generated at 2022-06-13 08:13:18.624166
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    handler = HandlerTaskInclude()
    assert handler is not None

# Generated at 2022-06-13 08:13:31.228916
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.playbook import Playbook
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    # Test case 1 for constructor of class HandlerTaskInclude
    # Test 'listen' is set to None    
    handler = HandlerTaskInclude(block=None, role=None, task_include=None)
    assert handler.listen is None

    # Test case 2 for constructor of class HandlerTaskInclude
    # Test 'listen' is set to listen
    listen = 'restarted'
    handler = HandlerTaskInclude(block=None, role=None, task_include=None, listen=listen)
    assert handler.listen is listen


# Generated at 2022-06-13 08:13:32.179715
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    return 0


# Generated at 2022-06-13 08:13:36.478025
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    handler_data = {
            'name': 'foo'
    }

    global_vars = {
            'foo': 'bar'
    }

    handler = HandlerTaskInclude.load(
        handler_data,
        variable_manager=variable_manager.VariableManager(),
        loader=DataLoader()
    )
    assert handler is not None, "Failed to create HandlerTaskInclude"

# Generated at 2022-06-13 08:13:37.716162
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    # test no error
    # test no error but with handler
    pass


# Generated at 2022-06-13 08:13:51.200560
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.role import Role
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    block = Block()
    role = Role()
    task_include = TaskInclude()
    variable_manager = VariableManager()
    loader = DataLoader()


# Generated at 2022-06-13 08:14:00.235062
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins.loader import action_loader

    from ansible.plugins.loader import connection_loader
    from ansible.vars import VariableManager

    conn = connection_loader.get('local', {})


    # data={'include': u'../tasks/main.yml'}
    data = {'include': u'../tasks/main.yml'}
    play_context = PlayContext()
    variable_manager = VariableManager()
    loader = None
    handler = HandlerTaskInclude.load(data, None, None, None, variable_manager, loader)
    print(handler.include)
    print(data)



# Generated at 2022-06-13 08:14:01.460892
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    result = HandlerTaskInclude()
    assert result.__class__ == HandlerTaskInclude

# Generated at 2022-06-13 08:14:10.670790
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    # t = HandlerTaskInclude(block=None, role=None, task_include=None)
    # print(t)
    # print(type(t))
    # print(type(t) == HandlerTaskInclude)
    # print(isinstance(t, HandlerTaskInclude))
    assert HandlerTaskInclude(block=None, role=None, task_include=None)
    assert isinstance(HandlerTaskInclude(block=None, role=None, task_include=None), HandlerTaskInclude)

# Generated at 2022-06-13 08:14:15.040139
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    handler_task_include=HandlerTaskInclude()
    print(handler_task_include.skipped_conditions)

if __name__ == "__main__":
    test_HandlerTaskInclude()

# Generated at 2022-06-13 08:14:19.011406
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    host = "Test Host"
    handler_task_include = HandlerTaskInclude(block=None, role=None, task_include=None)
    assert host == handler_task_include.host



# Generated at 2022-06-13 08:14:28.236958
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.compat.tests import unittest
    from ansible.vars.manager import VariableManager

    class AnsibleModuleMock:
        def __init__(self, data):
            self.params = data
    class TestHandlerTaskInclude(unittest.TestCase):
        def setUp(self):
            self.variable_manager = VariableManager()

        def test_handler_task_include_load(self):
            self.assertEqual(HandlerTaskInclude.load(AnsibleModuleMock({ 'include': 'main' }),
                                             variable_manager=self.variable_manager).get_name(), 'include')

# Generated at 2022-06-13 08:14:34.236368
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    data = {
        "include_tasks": "../common/tasks.yml",
    }
    block = None
    role = None
    task_include = None
    variable_manager = None
    loader = None
    handler = HandlerTaskInclude.load(data, block, role, task_include, variable_manager, loader)

    assert handler is not None
    assert handler.task_include is not None
    assert handler.task_include.static

# Generated at 2022-06-13 08:14:42.247988
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    data = {'include': 'a/b/c.yml'}
    handler = HandlerTaskInclude.load(data, block=None, role=None, task_include=None, variable_manager=None, loader=None)
    assert handler is not None

    data = {'include': 'a/b/c.yml', 'tags': ['a', 'b', 'c']}
    handler = HandlerTaskInclude.load(data, block=None, role=None, task_include=None, variable_manager=None, loader=None)
    assert handler is not None

# Generated at 2022-06-13 08:14:49.057038
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.inventory import Inventory
    from ansible.vars import VariableManager
    from ansible.inventory.host import Host
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.role import Role
    from ansible.playbook.role.include import IncludeRole
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.template import Templar

    def fake_loader(self, path):
        return file(path, 'r').read()

    def fake_get_basedir(self, path):
        pass

    def fake_get_real_file(self, path):
        pass

    def fake_filter_tasks(self, tasks):
        return (tasks, [])


# Generated at 2022-06-13 08:15:15.321867
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.inventory.host import Host
    from ansible.playbook.handler import Handler
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.vars.hostvars import HostVars
    from ansible.vars.hostvars import HostVarsVars
    from ansible.vars.groupvars import GroupVars
    from ansible.vars.groupvars import GroupVarsVars
    from ansible.vars.fact_cache import FactCache

    loader = DataLoader()

    variable_manager = VariableManager(loader=loader, inventory=None)

    variable_manager.extra_vars = {}


# Generated at 2022-06-13 08:15:17.128171
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    a = HandlerTaskInclude()
    data = {}
    assert a.load(data) is None
    data = dict(a=1)
    assert a.load(data) is None

# Generated at 2022-06-13 08:15:24.111797
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    # setup
    block = "_block"
    role = "role"
    task_include = "_task_include"
    data = "data"
    variable_manager = "variable_manager"
    loader = "loader"
    handler_task_include = HandlerTaskInclude(block=block, role=role, task_include=task_include)

    # check
    assert handler_task_include.block == block
    assert handler_task_include.role == role
    assert handler_task_include.task_include == task_include
    assert handler_task_include.VALID_INCLUDE_KEYWORDS == HandlerTaskInclude.VALID_INCLUDE_KEYWORDS
    assert handler_task_include.load(data, block, role, task_include, variable_manager, loader)



# Generated at 2022-06-13 08:15:31.768883
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.inventory.host import Host
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager

    data = {
        "name": "test_handler",
    }
    T = HandlerTaskInclude(block=None, role=None, task_include=None)
    result = T.load(data)
    assert(type(result) == HandlerTaskInclude)
    assert(result.get_name() == "test_handler")



# Generated at 2022-06-13 08:15:41.129293
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.inventory import Inventory
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.role import Role
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play

    inventory = Inventory("")
    variable_manager = VariableManager()
    loader = DataLoader()
    play_context = PlayContext()
    play = Play()

    data = {
        "name": "handler",
        "listen": "test",
        "block": "Test"
    }

    t = Task()

# Generated at 2022-06-13 08:15:54.585829
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():

    # Create object HandlerTaskInclude
    handler_task_include = HandlerTaskInclude()

    # Create object Block
    block = Block()

    # Create object Role
    role = Role()

    # Create object TaskInclude
    task_include = TaskInclude()

    # Create object VariableManager
    variable_manager = VariableManager()

    # Create object Loader
    loader = Loader()

    # Create data for test
    data = {}

    # Test with normal data
    handler_task_include.VALID_INCLUDE_KEYWORDS = handler_task_include.VALID_INCLUDE_KEYWORDS.union(('vars',))

# Generated at 2022-06-13 08:15:57.050646
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    # print('----- TEST: Constructor of class HandlerTaskInclude -----')
    print(HandlerTaskInclude())

# Generated at 2022-06-13 08:15:57.732567
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    pass

# Generated at 2022-06-13 08:15:59.335085
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    instance = HandlerTaskInclude()
    assert instance is not None


# Generated at 2022-06-13 08:16:05.927407
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    assert HandlerTaskInclude.load({'hosts': 'testhost', 'tasks': []}) is not None
    assert HandlerTaskInclude.load({'hosts': 'testhost', 'tasks': [], 'name': 'test'}) is not None
    assert HandlerTaskInclude.load({'hosts': 'testhost', 'tasks': [], 'name': 'test', 'listen': 'my_handlers'}) is not None


# Generated at 2022-06-13 08:16:45.969349
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    pass
# TODO



# Generated at 2022-06-13 08:16:51.641417
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.utils.display import Display
    from ansible.vars.manager import VariableManager

    class Host:
        def __init__(self, host_name):
            self.name = host_name

    display = Display()
    play_context = PlayContext(play=Play().load("test.yml", variable_manager=VariableManager(), loader=None))

# Generated at 2022-06-13 08:16:52.717578
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    pass

# Generated at 2022-06-13 08:16:53.732336
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    pass

# Generated at 2022-06-13 08:17:02.782659
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.playbook.play import Play
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    import ansible.constants as C

    # Load test playbook
    pb = Play.load(dict(
        name="test",
        hosts='all',
        gather_facts='no',
        tasks=[
            dict(action=dict(module="command", args="whoami"), register="shell_out"),
            dict(action=dict(module="debug", args=dict(msg="{{shell_out.stdout}} is the owner")))
        ]
    ), variable_manager=VariableManager(), loader=C.DEFAULT_LOADER)

    # Load inventory
    inventory = InventoryManager(loader=C.DEFAULT_LOADER, sources=pb.get_hosts())


# Generated at 2022-06-13 08:17:11.958864
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    from ansible.playbook.block import Block
    from ansible.playbook.block import BlockInclude
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.role.include import RoleInclude
    from ansible.playbook.handler import Handler
    from ansible.inventory.host import Host

    handler_task_include = HandlerTaskInclude(block=BlockInclude(), role=RoleInclude(), task_include=TaskInclude())

    assert handler_task_include.__class__.__name__ == 'HandlerTaskInclude'
    assert (isinstance(handler_task_include, Handler))
    assert (isinstance(handler_task_include, Task))
    assert (isinstance(handler_task_include, TaskInclude))

# Generated at 2022-06-13 08:17:23.760241
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    data = dict(
        listen=dict(
            foo=dict(
                bar='baz'
            )
        )
    )
    t = HandlerTaskInclude(block=None, role=None, task_include=None)
    h = t.load_data(data, variable_manager=None, loader=None)
    print("HandlerTaskInclude_load:")
    print("h = ", h)
    assert h['action'] == 'include'
    assert h['role'] == None
    assert h['include'] == 'foo.bar.yml'
    assert h['static'] == True

if __name__ == '__main__':
    test_HandlerTaskInclude_load()

# Generated at 2022-06-13 08:17:30.542480
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    data = {
        "name": "example.yml",
        "src": "example.yml",
        "listen": "http_ok"
    }

    result = HandlerTaskInclude.load(data, block=None, role=None,
                                     task_include=None, variable_manager=None, loader=None)
    expected = {
        "name": "example.yml",
        "src": "example.yml",
        "listen": "http_ok"
    }

    assert expected == result

# Generated at 2022-06-13 08:17:36.450862
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    t = HandlerTaskInclude()
    data = dict(
        include=dict(
            tasks="some_tasks.yml",
            handler="some_handler.yml",
        )
    )

    t.VALID_INCLUDE_KEYWORDS = set(('tasks', 'handler'))

    handler = t.check_options(
        t.load_data(data, variable_manager=None, loader=None),
        data
    )

    assert handler.static is False
    assert handler.loop is None
    assert handler.listen is None
    assert "some_tasks.yml" in handler._handlers

# Generated at 2022-06-13 08:17:45.181849
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    
    variable_manager = VariableManager()
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, variable_manager=variable_manager, host_list=[])
    variable_manager.set_inventory(inventory)
    task = {
        'include': 'setup.yml',
        'listen': 'setup'
    }

    handler = HandlerTaskInclude.load(task, variable_manager=variable_manager, loader=loader)
    assert handler.get_path() == 'setup.yml'

# Generated at 2022-06-13 08:19:10.905229
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    data = {
        'name': 'include_a_var',
        'include': 'tasks/{{ a_var }}',
        'static': 'tasks/{{ a_var }}',
    }
    handler = HandlerTaskInclude.load(data)
    assert handler._load_name == 'include_a_var'
    assert handler._uses_include == True
    assert handler._include == 'tasks/{{ a_var }}'
    assert handler._static_include is None

# Generated at 2022-06-13 08:19:18.734193
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    test_HandlerTaskInclude = HandlerTaskInclude()
    print("***** Test of method load of class HandlerTaskInclude *****")
    print("=================================================================================================================")
    print("***** Good parameters *****")
    print("=================================================================================================================")
    try:
        print(">>>>> Test when both block and role are None")
        test_HandlerTaskInclude.load({}, None, None, None, None, None)
    except:
        assert False, "It should work with these good parameters"
    print("=================================================================================================================")
    print("***** Bad parameters *****")
    print("=================================================================================================================")
    print(">>>>> Test when block is empty")

# Generated at 2022-06-13 08:19:31.752875
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.block import Block
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.vars import load_extra_vars
    from ansible.utils.vars import load_options_vars
    from ansible.utils.vars import load_tasks_vars
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play

    # create the variable manager
    variable_manager = VariableManager()
    loader = DataLoader()

    # create the inventory, and feed the variable manager with options / extra vars

# Generated at 2022-06-13 08:19:34.024862
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    # data = dict(include='my-include.yml')
    # t = HandlerTaskInclude.load(data)
    # assert t is not None
    # assert t.include_tasks
    pass


# Generated at 2022-06-13 08:19:47.961560
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    class _ModuleLoader:
        @staticmethod
        def load_role_definitions(a, b=None):
            return {'tasks': {'main': ['test']}}

        @staticmethod
        def has_plugin(a):
            return False

    class _DataLoader:
        @staticmethod
        def load_from_file(file_name):
            return '{"tasks": [{"debug": "msg=Hello World"}]}'

        @staticmethod
        def list_directory(file_name):
            return [{'path': '/tmp/test.yml'}]

    class _VariableManager:
        def __init__(self):
            self.extra_vars = {}

        @property
        def variable_manager(self):
            return self


# Generated at 2022-06-13 08:19:56.376569
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.template import Templar
    from ansible.inventory.host import Host
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    import mock
    ht = HandlerTaskInclude()

    # Test valid include
    handler_data = """
    - name: test handler
      include: test_handler.yml
    """
    handler_data = yaml.load(handler_data)
    host = Host(name='test')
    variable_manager = VariableManager()
    variable_manager.set_host_variable(host, 'test_var', 'test_value')
    dataloader = DataLoader()
    t = Templar(loader=dataloader, variables=variable_manager, fail_on_undefined=True)

    # Test for successful load

# Generated at 2022-06-13 08:19:56.807602
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    assert HandlerTaskInclude

# Generated at 2022-06-13 08:20:02.617511
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    # import the required class and function
    from ansible.playbook.block import Block
    from ansible.playbook.role import Role

    # create objects and store them in a list
    block = Block()
    role = Role()
    data = dict()
    variable_manager = object()
    loader = object()

    # Call constructor
    h = HandlerTaskInclude(block=block, role=role)

    # Test the instantiating
    assert h.VALID_INCLUDE_KEYWORDS == frozenset(('vars', 'tasks', 'defaults', 'handlers', 'pre_tasks', 'post_tasks', 'listen'))
    assert h.block == block
    assert h.role == role

    # Test the load method
    data['content'] = 'line1'