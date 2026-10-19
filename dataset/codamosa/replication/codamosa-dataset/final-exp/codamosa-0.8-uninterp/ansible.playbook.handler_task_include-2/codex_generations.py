

# Generated at 2022-06-13 08:10:08.717861
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.role import Role
    from ansible.playbook.role.include import RoleInclude
    from ansible.plugins.loader import add_all_plugin_dirs

    variable_manager = VariableManager()
    loader = DataLoader()
    variable_manager.set_loader(loader)
    
    add_all_plugin_dirs()

    task1 = Task()
    t = HandlerTaskInclude()
    HandlerTaskInclude.check_options(task1, {})
    task2 = TaskInclude()
    role = Role()
    role2 = RoleInclude()

    expected_result = {'tasks': [task1], 'meta': {}}


# Generated at 2022-06-13 08:10:16.591877
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    obj = HandlerTaskInclude()
    obj.load('- include: test.yml')
    obj.load('- include_tasks: test.yml')
    obj.load('- include_role: test.yml')
    obj.load('- import_role: test.yml')
    obj.load('- include: tasks/test.yml')
    obj.load('- include_tasks: tasks/test.yml')
    obj.load('- include_role: tasks/test.yml')
    obj.load('- import_role: tasks/test.yml')
    obj.load('- include: tasks/test.yml')
    obj.load('- include_tasks: tasks/test.yml')
    obj.load('- include_role: tasks/test.yml')

# Generated at 2022-06-13 08:10:25.336168
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    class AnsibleHost:
        def __init__(self, host_name):
            self.name = host_name
            self.groups = []

        def get_name(self):
            return self.name

    class MockVariableManager:
        def __init__(self):
            pass

    class MockLoader:
        def __init__(self):
            pass

    h = HandlerTaskInclude()
    data = {'action': {'handler': '/path/to/handler.yml'}, 'listen': 'test1'}
    h.load(data, block=None, role=None, task_include=None, variable_manager=MockVariableManager(), loader=MockLoader())
    assert h.loop is False
    assert h.name is None
    assert h.notify is None

# Generated at 2022-06-13 08:10:36.009561
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    def test_throws_warning(monkeypatch):
        def mock_load(self, data, block=None, role=None, task_include=None, variable_manager=None, loader=None):
            mock_load.call_count += 1
            return "test"
        mock_load.call_count = 0
        monkeypatch.setattr(HandlerTaskInclude, 'load', mock_load)

        import warnings
        from ansible.utils.warnings import AnsibleParserWarning
        from ansible.playbook.task_include import TaskInclude
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            HandlerTaskInclude.load(data, block=None, role=None, task_include=TaskInclude(), variable_manager=None, loader=None)

# Generated at 2022-06-13 08:10:37.113566
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    t = HandlerTaskInclude()
    assert t is not None

# Generated at 2022-06-13 08:10:40.137108
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    print('Executing test_HandlerTaskInclude')
    hti = HandlerTaskInclude()
    print('got here')
    assert hti is not None

# Unit test to load valid data

# Generated at 2022-06-13 08:10:50.389636
# Unit test for method load of class HandlerTaskInclude

# Generated at 2022-06-13 08:10:53.504574
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    h=HandlerTaskInclude()
    h.load({'include':'test.yml','tags':'test','listen':'test','other':'other'})

# Generated at 2022-06-13 08:11:03.970074
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.vars.manager import VariableManager

    block = Block(
        parent_block=None,
        role=None,
        task_include=None,
        use_handlers=False,
        block=None,
        role=None,
        task_include=None,
    )
    role = None
    task_include = Task(
        ''
    )

    data = '''
    - action: ping
      name: hello world
    '''

    handler = HandlerTaskInclude.load(data, block, role, task_include, VariableManager())
    assert isinstance(handler, HandlerTaskInclude)

# Generated at 2022-06-13 08:11:18.068269
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.inventory.host import Host
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude

    testhost = Host(name='testhost')
    testhost.set_variable('ansible_ssh_user', 'testuser')
    testhost.set_variable('ansible_ssh_pass', 'testpass')
    testhost.set_variable('ansible_python_interpreter', '/usr/bin/python3')
    testhost.set_variable('ansible_connection', 'ssh')
    testhost.set_variable('ansible_ssh_host', '192.168.1.2')
   

# Generated at 2022-06-13 08:11:30.211947
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    from ansible.playbook.play import Play
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    host = Host(name='testhost')
    group = Group(name='testgroup')
    group.add_hosts([host])
    play = Play()
    play.add_hosts([host])
    play.add_groups([group])
    variable_manager = VariableManager()
    variable_manager.set_inventory(play.get_inventory())

    data = dict(
        include='testtask',
        name='testhandler'
    )


# Generated at 2022-06-13 08:11:30.985873
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    pass

# Generated at 2022-06-13 08:11:36.976664
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    data = {
        "block": None,
        "role": None,
        "task_include": None,
        "listen": "MYSQL_WRITE",
        "name": "restart mysql",
        "notify": ["restart mysql"]
    }

    handler = HandlerTaskInclude.load(data)
    assert handler.name == 'restart mysql'
    assert handler.notify == ['restart mysql']



# Generated at 2022-06-13 08:11:43.352228
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    # Data
    data = {
        "include": ["my-tasks"],
        "listen": "myhandlers",
    }

    # create an instance of HandlerTaskInclude
    t = HandlerTaskInclude()
    print(t)

    # create an instance of HandlerTaskInclude
    t = HandlerTaskInclude(data=data)
    print(t)
    t.load(data, None, None, None, None, None)

# Generated at 2022-06-13 08:11:50.907715
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():

    from ansible.playbook.play import Play
    from ansible.playbook.block import Block
    from ansible.playbook.role import Role
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.task import Task
    from ansible.inventory.host import Host
    from ansible.vars.manager import VariableManager
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.plugins.loader import daemons
    from ansible.errors import AnsibleParserError

    host = Host(name="localhost", port=22)
    variable_manager = VariableManager()
    loader = AnsibleLoader(None, variable_manager)
    variable_manager.set_host_variable(host, "foo", "bar")

    # missing required attribute
    # missing required attribute

# Generated at 2022-06-13 08:11:55.640422
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    t = HandlerTaskInclude(block=None, role=None, task_include=None)
    # handler = t.check_options(t.load_data(data, variable_manager=variable_manager, loader=loader), data)
    handler = t.check_options(t.load_data('data', variable_manager=None, loader=None), 'data')
    assert handler == None

# Generated at 2022-06-13 08:12:08.352194
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.template import Templar
    from ansible import constants as C
    import sys
    import os

    if sys.version_info >= (2, 7):
        import unittest
    else:
        import unittest2 as unittest

    from units.mock.loader import DictDataLoader


    class TestHandlerTaskInclude(unittest.TestCase):

        def setUp(self):
            pass


        def tearDown(self):
            pass


        def test_load(self):
            templar = Templar(loader=None, variables={})


# Generated at 2022-06-13 08:12:09.197421
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    pass

# Generated at 2022-06-13 08:12:16.023677
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    host = Host(name='test')
    handler = HandlerTaskInclude.load(dict(hosts='test'), block=None)
    hosts = list(handler.get_hosts())
    assert hosts == [host]

    handler = HandlerTaskInclude.load(dict(hosts=['test']), block=None)
    hosts = list(handler.get_hosts())
    assert hosts == [host]

# Generated at 2022-06-13 08:12:26.755818
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():

    from ansible.playbook.task import Task 
    from ansible.inventory.host import Host
    from ansible.playbook.block import Block
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.template import Templar
    from ansible.inventory.group import Group
    from ansible.inventory.inventory import Inventory
    from io import StringIO
    import os

    thehost = Host(name="darkstar")
    thehost.set_variable('ansible_ssh_host', '10.0.0.1')
    thehost.set_variable('ansible_ssh_pass', 'changeme')
    thehost.set_variable('ansible_ssh_user', 'root')

# Generated at 2022-06-13 08:12:29.785562
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    pass

# Generated at 2022-06-13 08:12:31.545951
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    # Instantiate class
    newHandlerTaskInclude = HandlerTaskInclude()
    assert newHandlerTaskInclude is not None

# Generated at 2022-06-13 08:12:40.831515
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.block import Block

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = [Group('test_group')]
    variable_manager.set_inventory(inventory)

    data = {'include': 'test_include_01.yml'}
    t = HandlerTaskInclude(block=Block(), role=None, task_include=None)
    handler = t.load(data)

    assert handler.task_include.include
    assert handler.task_include.include_tasks

# Generated at 2022-06-13 08:12:47.309592
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
     from ansible.vars.manager import VariableManager
     from ansible.inventory.manager import InventoryManager
     from ansible.parsing.dataloader import DataLoader
     from ansible.playbook.role.definition import RoleDefinition
     from ansible.utils.vars import load_extra_vars
     from ansible.utils.vars import load_options_vars
     from ansible.utils.vars import load_params_vars
     from ansible.errors import AnsibleParserError, AnsibleUndefinedVariable
     from ansible.playbook.block import Block
     from ansible.playbook.play import Play
     from ansible.playbook.role import Role
     from ansible.playbook.task import Task
     from ansible import constants as C
     import os
     myloader = DataLoader()
     mypasswords

# Generated at 2022-06-13 08:12:57.051522
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    t = HandlerTaskInclude()

# Generated at 2022-06-13 08:13:05.245023
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    data = {'include': 'debug_output.yml'}
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
    assert handler is not None

# Generated at 2022-06-13 08:13:15.935438
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    from ansible.playbook.handler import Handler
    from ansible.inventory.host import Host

    from ansible.playbook.block import Block

    from ansible.playbook.role import Role

    from ansible.playbook.task import Task

    from ansible.playbook.task_include import TaskInclude

    from ansible.vars import VariableManager
    variable_manager = VariableManager

    from ansible.parsing.dataloader import DataLoader
    loader = DataLoader
    variable_manager.set_inventory(loader.load_inventory('localhost'))

    data = dict()
    data['name'] = 'test'
    data['local_action'] = dict()
    data['local_action']['module'] = 'shell'
    data['local_action']['args'] = 'date'

    i = Host

# Generated at 2022-06-13 08:13:16.784468
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    assert True

# Generated at 2022-06-13 08:13:29.945980
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    from ansible.inventory.host import Host
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    data = dict(
        name="nop test",
        action="nop",
    )
    host=Host("testhost")
    variable_manager = VariableManager()
    loader = DataLoader()

    handler = HandlerTaskInclude.load(data, block=None, role=None, task_include=None, variable_manager=variable_manager, loader=loader)
    assert isinstance(handler, HandlerTaskInclude)
    handler.evaluate_conditional_if_needed(host, variable_manager)

    assert handler._included_file is not None
    assert handler._included_file.get('module') == 'nop'



# Generated at 2022-06-13 08:13:32.142598
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    assert HandlerTaskInclude.load([])
    #assert HandlerTaskInclude.load(['', ''])

# Generated at 2022-06-13 08:13:37.946220
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    assert HandlerTaskInclude.load(data)

# Generated at 2022-06-13 08:13:44.481026
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():

    from ansible.playbook.block import Block
    from ansible.inventory.host import Host
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.template import Templar
    from ansible.utils.vars import combine_vars
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.inventory.group import Group
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.playbook.task_include import TaskInclude

    loader = DataLoader()

    class MockVariableManager(VariableManager):
        def __init__(self):
            self.vars = {}
            self.extra_vars = {}
            self.options

# Generated at 2022-06-13 08:13:49.994009
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    h = HandlerTaskInclude(block=None, role=None, task_include=None)
    assert h.static == False
    assert h.handler is None
    assert h._load_name is None
    assert h._role is None
    assert h._block is None
    assert h._parent is None
    assert h._shared_loader_obj is None
    assert h._include is None
    assert h._dep_chain == []

# Generated at 2022-06-13 08:13:51.353299
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
  handlerTaskInclude = HandlerTaskInclude()
  assert isinstance(handlerTaskInclude, HandlerTaskInclude)

# Generated at 2022-06-13 08:14:01.422880
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.inventory.host import Host
    from ansible.playbook.block import Block
    from ansible.playbook.task_include import TaskInclude
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    data = {
        'name': 'test',
        'listen': 'notify_test',
        'when': 'test',
        'remote_user': 'test',
        'sudo': 'test',
        'sudo_user': 'test',
        'environment': 'test',
        'register': 'test',
        'tags': ['test'],
        'hosts': 'test'
    }

    hosts = [Host(name='test')]
    variable_manager = VariableManager(loader=DataLoader())
    variable_manager.set

# Generated at 2022-06-13 08:14:07.536551
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    '''
    This method is not static, we need to instantiate the class before calling.
    The call is like
    HandlerTaskInclude.load(data, block=None, role=None, task_include=None,
                            variable_manager=None, loader=None):
    '''

# Generated at 2022-06-13 08:14:20.114943
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    def check_var(host, var, val):
        if var == "somevar":
            assert val == "somevalue"
        assert var in ('somevar', 'someothervar')

    def check_host(host):
        assert host in ('host1', 'host2')
        return [('somevar', 'somevalue'), ('someothervar', 'someothervalue')]

    class FakeVariableManager(object):
        def __init__(self):
            self.failed_conditions = []

        def set_failed_conditions(self, conds):
            self.failed_conditions = conds

        def get_vars(self, host):
            return check_host(host)

    class FakeTaskInclude(object):
        def __init__(self, variable_manager):
            self.variable_manager = variable_manager



# Generated at 2022-06-13 08:14:22.443343
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    handler_task_include = HandlerTaskInclude(block=None, role=None, task_include=None)
    handler_task_include.__class__

# Generated at 2022-06-13 08:14:30.064973
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    obj = HandlerTaskInclude()
    arg1 = {"include": "some_file"}
    arg2 = {"include": "some_file", "ignore_errors": True}
    arg3 = {"include": "some_file", "tags": ["A", "B"]}
    arg4 = {"include": "some_file", "listen": "A"}
    arg5 = {"include": "some_file", "vars": {"A": "B", "C": "D"}}
    arg6 = {"include": "some_file", "vars": {"A": "B", "C": "D"}, "listen": "A"}

# Generated at 2022-06-13 08:14:33.757174
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
   handler_example = HandlerTaskInclude(block = 'unit_test', role ='unit_test', task_include = 'unit_test')
   assert handler_example.__class__.__name__ == 'HandlerTaskInclude'

# Generated at 2022-06-13 08:14:50.302037
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    data   = dict(name="test")
    loader = dict()
    variable_manager = dict()

    result1 = HandlerTaskInclude.load(data, block=None, role=None, task_include=None, variable_manager=variable_manager, loader=loader)
    assert result1 == data
    assert result1.get('task') == None # added as a value

    data["task"] = "text"
    result2 = HandlerTaskInclude.load(data, block=None, role=None, task_include=None, variable_manager=variable_manager, loader=loader)
    assert result2.get('task') == "text"

    data["task"] = "{{ test }}"

# Generated at 2022-06-13 08:15:02.247448
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.inventory.host import Host
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.playbook.block import Block
    from ansible.playbook.play import Play

    host = Host('localhost', port=22, user='root')
    block = Block()
    role = None
    task_include = None
    variable_manager = VariableManager()
    loader = DataLoader()

    data = {
        'listen': 'Service started',
        'include': 'foo.yml'
    }

    handler = HandlerTaskInclude.load(data=data, block=block, role=role, task_include=task_include, variable_manager=variable_manager, loader=loader)
    assert handler is not None
    assert handler._name

# Generated at 2022-06-13 08:15:03.530969
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    # TODO
    pass

# Generated at 2022-06-13 08:15:11.496380
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.errors import AnsibleError
    from ansible.playbook.block import Block
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.vars.hostvars import HostVars
    from ansible.utils.vars import combine_vars

    # create a variable manager
    variable_manager = VariableManager()
    variable_manager.extra_vars = {
        "var1": "var1_value",
        "var2": "var2_value",
        "var3": "var3_value",
    }

    # create a fake loader
    loader = None

    # create a fake play context
    play_context = PlayContext()

    # create a fake host
    host = HostV

# Generated at 2022-06-13 08:15:12.847802
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    h = HandlerTaskInclude()
    assert h is not None

# Generated at 2022-06-13 08:15:18.945697
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    print("Unit test for constructor of class HandlerTaskInclude")
    t = HandlerTaskInclude()
    t_dir = dir(t)
    print(t_dir)
    assert 'VALID_INCLUDE_KEYWORDS' in t_dir
    # assert isinstance(t.VALID_INCLUDE_KEYWORDS, FrozenSet), "assert isinstance(t.VALID_INCLUDE_KEYWORDS, FrozenSet)"

# Generated at 2022-06-13 08:15:25.364101
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.playbook.role.include import IncludeRole
    from ansible.vars.manager import VariableManager

    data = {
        u'name': u'start services',
        u'when': [u'services_started'],
        u'tag': u'tags_here',
        u'include': u'roles/foo/tasks/main.yml',
        u'include_role': u'foo',
        u'include_tasks': u'roles/foo/tasks/main.yml',
        u'include_vars': u'roles/foo/vars/main.yml',
    }

    handler = HandlerTaskInclude.load(data)

    print(type(handler))
    print(dir(handler))
    print(handler._included_file)

# Generated at 2022-06-13 08:15:25.963736
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    HandlerTaskInclude()

# Generated at 2022-06-13 08:15:32.912293
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.inventory.host import Host
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    host = Host()
    loader = DataLoader()
    variable_manager = VariableManager()

    data = '''
    ---
    tasks:
      - debug:
          msg: Hello World!
    '''

    h = HandlerTaskInclude.load(data, loader=loader, variable_manager=variable_manager)
    assert(h is not None)
    assert(h._role is None)
    assert(h._block is None)
    assert(h._task_include is None)


# Generated at 2022-06-13 08:15:34.044725
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    h = HandlerTaskInclude()
    assert h is not None


# Generated at 2022-06-13 08:15:56.351844
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    # TODO: finish this test
    print("Hello, world!")

# Generated at 2022-06-13 08:15:57.500933
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    pass


# Generated at 2022-06-13 08:16:00.431120
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    print("testing method load of class HandlerTaskInclude")
    # TODO
    print("task_include.py:test_HandlerTaskInclude_load:TODO")



# Generated at 2022-06-13 08:16:11.887529
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.playbook.block import Block
    from ansible.playbook.role import Role
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.base import Base
    block = Block()
    role = Role()
    task_include = TaskInclude()
    data = dict(
        _raw=dict(
            handlers=dict(
                foo=dict(
                    tasks=dict(
                        bar=dict(
                            listen=dict(
                                when=dict(
                                    some_key=dict(
                                        equals=dict(
                                            some_value=""
                                        )
                                    )
                                )
                            )
                        )
                    )
                )
            )
        )
    )
    variable_manager = None
    loader = None
    handler = Handler

# Generated at 2022-06-13 08:16:12.659586
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    handler = HandlerTaskInclude()
    assert handler

# Generated at 2022-06-13 08:16:16.059987
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    # unit test start
    testHandlerTaskInclude = HandlerTaskInclude()
    assert testHandlerTaskInclude is not None, "Failed to create testHandlerTaskInclude"
    # unit test ends

if __name__ == "__main__":
    test_HandlerTaskInclude()

# Generated at 2022-06-13 08:16:18.253041
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    hti = HandlerTaskInclude('name', 'file', 'action')
    assert (hti.action == 'action')


# Generated at 2022-06-13 08:16:19.013606
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    # HandlerTaskInclude()
    pass

# Generated at 2022-06-13 08:16:28.138980
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
  import sys
  import os
  import unittest
  #sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

  class HandlerTaskInclude_load_TestCase(unittest.TestCase):
    def setUp(self):
      self.instance = None

    def tearDown(self):
      if self.instance is not None:
        del self.instance

    #TODO: test here
    def test_load(self):
      print("No test for method load of class HandlerTaskInclude")
      return
      self.assertEqual(True, True)

  #unittest.main()
  suite = unittest.TestLoader().loadTestsFromTestCase(HandlerTaskInclude_load_TestCase)

# Generated at 2022-06-13 08:16:34.421825
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    # init variable
    data = dict()
    data['include'] = 'test.yml'
    data['when'] = 'shutdown'
    variable_manager = dict()
    variable_manager['variable_manager'] = 'test'
    loader = dict()
    loader['loader'] = 'test'

    # init class
    t = HandlerTaskInclude()
    handler = t.check_options(t.load_data(data, variable_manager=variable_manager, loader=loader), data)

    assert handler.block == None
    assert handler.role == None
    assert handler.task_include == None
    assert handler._uuid == handler.uuid
    assert handler.when == 'shutdown'
    assert handler.include == 'test.yml'
    assert handler.name == 'test.yml'
    assert handler.handler

# Generated at 2022-06-13 08:17:15.377070
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    h = HandlerTaskInclude()
    print(h)

# Generated at 2022-06-13 08:17:27.617614
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.vars.manager import VariableManager

    tasks = [
        dict(name='test task 1', action=dict(module='shell', args='ls'))
    ]

    block = Block(
        tasks=tasks,
        rescue=None,
        always=None,
        role=None,
        loop=None,
    )

    role = dict(
        tasks=dict(
            main=block
        )
    )

    play_context = PlayContext()
    play_context.remote_addr = '10.10.10.10'

    task_include = Task()

    handler = HandlerTaskInclude()

# Generated at 2022-06-13 08:17:35.489792
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    print("test_HandlerTaskInclude")
    data = { "include": "test_playbook.yml" }
    import os
    data['include'] = os.path.abspath("test_playbook.yml")
    variable_manager = None
    loader = None
    test_HandlerTaskInclude = HandlerTaskInclude(None, None, None)
    for dirpath, dirnames, filenames in os.walk("."):
        for filename in [f for f in filenames if f.endswith(".py")]:
            print(os.path.join(dirpath, filename))
    task_include = TaskInclude.load(data, variable_manager=variable_manager, loader=loader)
    assert task_include.filename == "test_playbook.yml"

# Generated at 2022-06-13 08:17:45.873466
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    # Arrange
    from ansible.inventory.host import Host
    from ansible.playbook.block import Block

    class TestTask:
        # to check object against
        def __init__(self, block, role=None, task_include=None):
            self.block = block
            self.role = role
            self.task_include = task_include

    # Act with all paramaters

# Generated at 2022-06-13 08:17:52.420536
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    print()

    from ansible.inventory.host import Host
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task

    from ansible.vars.manager import VariableManager

    block = Block()
    msg   = "Hello"
    task  = Task()
    task.vars.update({"msg" : msg})
    handlers = [{"name" : "main", "tasks" : [task], "when" : "not localhost"}]
    block.handlers = handlers
    varm = VariableManager()

    hosts = [Host('localhost')]
    varm.set_inventory(hosts)

    # This is a basic test, with no changed state.

# Generated at 2022-06-13 08:18:00.058741
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    # Create inventory
    myGroup = Group("my-group")
    myHost = Host("my-host", port=2222)
    myGroup.add_host(myHost)
    inventory = InventoryManager(loader = DataLoader(), sources = 'localhost,')
    inventory.add_group(myGroup)
    variable_manager = VariableManager()
    variable_manager.set_inventory(inventory)

    # Create AnsibleTaskInclude object
    handler_task_include = HandlerTaskInclude()

    # Create data for HandlerTaskInclude object

# Generated at 2022-06-13 08:18:06.193107
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():

    # call without task_include
    try:
        data = dict(include='test.yml')
        task_include = HandlerTaskInclude.load(data)
        assert task_include is None
    except:
        assert False

    # call with task_include
    try:
        data = dict(include='test.yml')
        task_include = HandlerTaskInclude.load(data, task_include='test_task_include')
        assert task_include is None
    except:
        assert False

# Generated at 2022-06-13 08:18:07.804933
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    hti = HandlerTaskInclude()
    assert hti.block is None
    assert hti.role is None
    assert hti.task_include is None

# Generated at 2022-06-13 08:18:08.936778
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    assert HandlerTaskInclude('block', 'role', 'task_include')

# Test for check_options()

# Generated at 2022-06-13 08:18:14.369022
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.errors import AnsibleParserError
    from ansible.playbook.task_include import TaskInclude

    from ansible.playbook.block import Block
    from ansible.playbook.role import Role
    from ansible.playbook.task import Task
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext

    import os
    import yaml

    # Load sample data
    current_dir = os.path.dirname(os.path.realpath(__file__))
    data = yaml.load(open(os.path.join(current_dir, 'sample_handler_task_include.yaml')))[0]

    # Create block, role, task and play
    block = Block()
    role = Role()
    task = Task()

# Generated at 2022-06-13 08:19:48.869128
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.playbook.play_context import PlayContext
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    play_context = PlayContext()
    inventory = InventoryManager()
    variable_manager = VariableManager(loader=None, inventory=inventory)

    # ここではansible 2系と3系で引数が異なる。
    # これによりplaybook.ymlの変更が必要となるかもしれない。
    # handlerの値が変わった場合、playbook.ymlの値も変更する。

# Generated at 2022-06-13 08:19:57.170777
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    import datetime
    from ansible.playbook.task_include import TaskInclude
    ti = TaskInclude()
    ti.name = 'foobar'
    ti.filename = 'foobar.yaml'
    ti.line_number = 3
    ti.action = 'foobar'
    ti._role_name = 'foobar'
    ti._role_path = 'foobar'
    ti._role_params = 'foobar'
    ti.handlers = []
    ti.meta = 'foobar'
    ti.previous = [1,2,3]
    ti.tags = ['foo', 'bar']
    ti.when = 'foobar'
    ti.__ansible_module__ = 'foobar'

    # make a copy of the settings, they'll be modified in load()
    ti2 = TaskIn

# Generated at 2022-06-13 08:20:02.917364
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.playbook.block import Block

    import json

    data = {
        'include': 'tasks/main.yml',
        'static': 'yes',
        'name': 'foo'
    }

    variable_manager = MockVariableManager()
    variable_manager.get_vars.return_value = {'foo': 'bar'}

    block = Block()
    block.vars = {'foo': 'bar'}
    block.hosts = ['host1']

    handler = HandlerTaskInclude.load(
        data=data,
        block=block,
        variable_manager=variable_manager
    )

    assert handler.__class__ == HandlerTaskInclude, handler.__class__
    assert handler.static == True, handler.static
    assert handler.include is not None, handler.include
   