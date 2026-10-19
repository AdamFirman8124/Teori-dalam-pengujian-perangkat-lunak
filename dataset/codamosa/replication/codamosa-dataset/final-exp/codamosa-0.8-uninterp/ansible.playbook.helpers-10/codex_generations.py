

# Generated at 2022-06-13 08:21:01.748448
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    test_ds = [
        {
            'include': 'test_include.yml',
            'static': True
        },
        {
            'block': [
                {
                    'action': {
                        'module': 'test_module'
                    }
                }
            ]
        }
    ]
    play = 'test'
    block = None
    role = None
    task_include = None
    use_handlers = False
    variable_manager = None
    loader = None

# Generated at 2022-06-13 08:21:02.262432
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    pass

# Generated at 2022-06-13 08:21:07.028872
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    import ansible.playbook
    pb = ansible.playbook.PlayBook()
    pb.host_list = "./hosts"
    pb.connection = 'local'
    pb.playbook_dir = "./"
    pb.callbacks = AnsibleCallbacks(verbose=utils.VERBOSITY)
    pb.runner.cwd = './'
    pb.basedir = './'
    task_ds = [{'block:': '', 'hosts': 'localhost'}]
    block = pb.load_list_of_tasks(task_ds)
    print(repr(block))

# Generated at 2022-06-13 08:21:15.216950
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.block import Block
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.vars import VariableManager

    connection = "local"
    transport = "local"
    port = None
    remote_user = "test"
    connection_user = "test"
    become = False
    become_method = None
    become_user = None
    verbosity = 0
    timeout = 10

# Generated at 2022-06-13 08:21:26.795341
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.play import Play
    from ansible.playbook.task_include import TaskInclude
    from test.units.mock.loader import DictDataLoader
    from ansible.vars.manager import VariableManager
    from test.units.compat import mock

    loader = DictDataLoader({})
    variable_manager = VariableManager()
    p = Play()
    ds = [dict(include='test'), dict(include='test')]
    task_list = load_list_of_tasks(ds, play=p, loader=loader, variable_manager=variable_manager)
    assert len(task_list) == 2
    assert isinstance(task_list[0], TaskInclude)
    assert isinstance(task_list[1], TaskInclude)
    assert task_list[0] is not task

# Generated at 2022-06-13 08:21:34.737700
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():

    def fake_task(s):
        t = Mock()
        name = Mock(return_value=s)
        t.get_name = name
        type = s[0]
        if type == 'i':
            t.name = 'include'
        elif type == 'r':
            t.name = 'include_role'
        elif type == 'p':
            t.name = 'pause'
        else:
            raise Exception('Bad test data')
        return t

    def gen_tasks(chars):
        for c in chars:
            yield fake_task(c)


# Generated at 2022-06-13 08:21:44.514904
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.play import Play
    from ansible.playbook.role import Role
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    loader = DataLoader()
    role = Role()
    play = Play()
    play._loader = loader
    play._variable_manager = VariableManager()
    block_ds = {'block':'some_block', 'tasks':list()}
    role_ds = dict(foo='bar')
    tasks_ds = list()

    tasks_ds.append(block_ds)
    for i in range(5):
        t = dict(block='some_block')
        tasks_ds.append(t)
    tasks_ds.append(role_ds)

    block_list = load_list_of_

# Generated at 2022-06-13 08:21:53.917245
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    display = Display()
    loader = DataLoader()
    variable_manager = VariableManager()
    #function load_list_of_tasks(ds, play, block=None, role=None, task_include=None, use_handlers=False, variable_manager=None, loader=None):
    ds = ['asd', 'asda', 'sadasd']
    play = 'play1'
    block = 'block1'
    role = 'role1'
    task_include = 'task_include1'
    use_handlers = 'use_handlers1'
    #variable_manager = 'variable_manager1'
    #loader = 'loader1'
    load_list_of_tasks(ds, play, block, role, task_include, use_handlers, variable_manager, loader)

# Generated at 2022-06-13 08:22:03.094162
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.play import Play
    from ansible.playbook.role import Role
    pb = Playbook()
    def get_dict():
        d = dict(
            name = 'test',
            hosts = 'all'
        )
        return d
    pb._entries.append(get_dict())
    pb.add_role(Role().load({}, pb._loader, pb))
    play_ds = pb.get_plays()[0]
    p = Play().load(play_ds, pb._loader, pb)
    loader = DataLoader()

# Generated at 2022-06-13 08:22:07.527028
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.handler_task_include import HandlerTaskInclude

    # test

# Generated at 2022-06-13 08:22:38.455046
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    import json
    # Initialize a Display() object to handle display control
    display = Display()
    # Set verbosity to 3 to suppress all outputs except for errors
    display.verbosity = 3
    # JUnit reports require STDOUT and STDERR to be returned.
    # So, we capture the output with a fake stream.
    class FakeStream(object):
        def __init__(self):
            self.content = ""
        def write(self, s):
            print("orig.out:\n%s" % s)
            self.content = self.content + s
        def read(self):
            return self.content
    fake_stdout = FakeStream()
    fake_stderr = FakeStream()
    save_stdout = sys.stdout
    save_stderr = sys.stderr

# Generated at 2022-06-13 08:22:39.634519
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    assert False, "Test is not implemented"

# Generated at 2022-06-13 08:22:50.778576
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.handler_task_include import HandlerTaskInclude
    ds_list = [
        {
            "set_fact": {
                "X": 1
            }
        },
        {
            "set_fact": {
                "X": 2
            }
        }
    ]

    tasks = load_list_of_tasks(
        ds_list,
        play=None,
        block=None,
        role=None,
        task_include=None,
        use_handlers=False,
        variable_manager=None,
        loader=None
    )

    assert all(map(lambda x: isinstance(x, Task), tasks))

# Generated at 2022-06-13 08:23:01.812690
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    # Test imports
    from collections import namedtuple
    from ansible.playbook.play import Play
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.plugins.filter import ipaddr, join, random
    from ansible.plugins.lookup import password

    # Test variables

# Generated at 2022-06-13 08:23:14.210388
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.play_context import PlayContext
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.playbook.play import Play
    from ansible.playbook import Playbook
    from ansible.plugins.test.test_task import TestTask
    from ansible.plugins.action import ActionBase
    from ansible.plugins.action.basic import ActionModule

    class TestActionModule(ActionModule):
        def run(self, tmp=None, task_vars=None):
            pass

    # Load the test task plugin
    TestTask.action_cls = TestActionModule

    # Define the fake

# Generated at 2022-06-13 08:23:22.541931
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    ds = [{'block': []}, {'debug': 'msg={{test_test1_var1}}'}, {}, {'include_tasks': 'test_test1_task1.yml'}, {'include_tasks': 'test_test2_task2.yml'}]
    task_list = load_list_of_tasks(ds)
    assert isinstance(task_list, list), 'Error test_load_list_of_tasks1'
    assert task_list[0].__class__.__name__ == 'Block', 'Error test_load_list_of_tasks2'
    assert task_list[1].__class__.__name__ == 'Task', 'Error test_load_list_of_tasks3'

# Generated at 2022-06-13 08:23:26.057058
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    # load_list_of_tasks(ds, play, block=None, role=None, task_include=None, use_handlers=False, variable_manager=None, loader=None):
    pass

# Generated at 2022-06-13 08:23:37.426575
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    # Create empty loader
    loader = DataLoader()
    # Create empty variable manager
    variable_manager = VariableManager()

    # Create mock play class
    class MockPlay(object):
        def __init__(self):
            self.hosts = 'host1'
            self.roles = []

    # Create mock block class
    class MockBlock(object):
        def __init__(self):
            self._parent = None
            self._play = MockPlay()
            self.use_handlers = False

    # Create mock task class
    class MockTask(object):
        def __init__(self):
            self._parent = None
            self._play = MockPlay()
            self.use_handlers = False
            self.block = None
            self.role = None
            self.task_include = None
            self.any

# Generated at 2022-06-13 08:23:46.705165
# Unit test for function load_list_of_roles
def test_load_list_of_roles():
    from ansible.playbook.play import Play
    from ansible.playbook import Playbook
    from ansible.vars.manager import VariableManager
    playbook = Playbook.load("./test/functional/playbooks/pb_with_roles.yml", loader=DataLoader())
    # Test play with roles
    pb_play = playbook.get_plays()[0]
    # Test load_list_of_roles with empty list
    assert load_list_of_roles([], pb_play) == []
    # Test load_list_of_roles with one role
    role_def = pb_play.roles_path[0]
    ds = [role_def]
    roles = load_list_of_roles(ds, pb_play)
    assert len(roles) == 1

# Generated at 2022-06-13 08:23:56.879035
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():

    from ansible.playbook.play import Play
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.task_queue_manager import TaskQueueManager
    loader = DataLoader()
    options = namedtuple('Options', ['connection', 'module_path', 'forks', 'become', 'become_method', 'become_user', 'check', 'listhosts', 'listtasks', 'listtags', 'syntax', 'sudo_user', 'sudo'])

# Generated at 2022-06-13 08:24:31.473302
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook import Playbook
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    import os

    p = Playbook()
    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, sources=['tests/test_inventory.ini'])
    variable_manager.set_inventory(inventory)

# Generated at 2022-06-13 08:24:38.939605
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():

    from ansible.playbook.task import Task
    from ansible.playbook.role_include import IncludeRole
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.handler import Handler

    ds = [{'action': b'name'}, {'action': b'name2'}]
    assert isinstance(load_list_of_tasks(ds, None, None, None, None, False, None, None)[0], Task)
    assert isinstance(load_list_of_tasks(ds, None, None, None, None, False, None, None)[1], Task)

    ds = [{'action': b'name'}, {'block': b'name2'}]

# Generated at 2022-06-13 08:24:48.376791
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():

    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    # Set-up test context
    loader = DictDataLoader({})
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, sources=[])
    play_context = PlayContext()

    # Create dummy task-list to test with
    # Task-list contains: 3 blocks, 2 tasks, and 2 tasks which include (import/include)

# Generated at 2022-06-13 08:25:03.145713
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    import types
    import random
    import tempfile
    import shutil

    from ansible.playbook.block import Block
    from ansible.playbook.handler import Handler
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.role_include import IncludeRole
    from ansible.playbook.handler_task_include import HandlerTaskInclude
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.plugins.loader import PluginLoader

# Generated at 2022-06-13 08:25:18.534444
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    #  assert load_list_of_tasks('foo') == 'foo'
    assert load_list_of_tasks(None) == []
    assert load_list_of_tasks('') == []
    assert load_list_of_tasks('', None) == []
    assert load_list_of_tasks(False) == []
    assert load_list_of_tasks([]) == []
    assert load_list_of_tasks(None, None, None, None, None, None, None, None) == []

# Generated at 2022-06-13 08:25:24.892291
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    import ansible.config.manager
    config_manager = ansible.config.manager.ConfigManager()
    config_manager.set_options('/Users/fred/ansible_core/lib/ansible/config/ansible.cfg')
    config_manager.options['host_key_checking'] = False
    config_manager.options['inventory'] = '/Users/fred/ansible_core/lib/ansible/inventory/hosts'
    config_manager.options['library'] = '/Users/fred/ansible_core/lib/ansible/modules/'
    config_manager.options['roles_path'] = '/Users/fred/ansible_core/lib/ansible/playbooks/roles'

# Generated at 2022-06-13 08:25:30.170022
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    '''
    Unit test for function load_list_of_tasks
    '''
    import os
    import sys
    import tempfile
    import shutil
    import subprocess

    import ansible.utils.template as template
    import ansible.utils.vars as ansible_vars
    import ansible.parsing.vault as vault
    import ansible.parsing.yaml as yaml
    import ansible.utils.shlex as shlex
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.handler_task_include import HandlerTaskInclude
    from ansible.playbook.role_include import IncludeRole

# Generated at 2022-06-13 08:25:42.657950
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    # 1.name is empty
    block = [{
        "name": "",
        "action": {
            "module": "shell",
            "args": "echo 1",
        }
    }]
    try:
        load_list_of_tasks(block)
    except AnsibleParserError as e:
        assert e.message != ""
        assert e.error != ""
    else:
        assert False, "AnsibleParserError should be raise"

    # 2.action is empty
    block = [{
        "name": "hey",
    }]
    try:
        load_list_of_tasks(block)
    except AnsibleParserError as e:
        assert e.message != ""
        assert e.error != ""

# Generated at 2022-06-13 08:25:55.613153
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    import ansible.playbook.role
    import ansible.playbook.task
    import ansible.playbook.task_include
    import ansible.playbook.block
    import ansible.playbook.handler
    import ansible.playbook.role_include
    import ansible.playbook.play
    import ansible.vars.manager
    import ansible.template

    vars_manager = ansible.vars.manager.VariableManager()
    data = [
        {
            'block': [
                {'local_action': dict(shell='echo')},
            ]
        },
        {'local_action': dict(shell='echo')}
    ]
    play = ansible.playbook.play.Play().load({}, variable_manager=vars_manager)
    task_list = load_list_of_

# Generated at 2022-06-13 08:26:00.861380
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    class FakePlay:
        pass

    class FakeRole:
        pass

    class FakeVarMgr:
        def get_vars(self, play, task):
            return {}

    class FakeLoader:
        pass

    class FakeHandler:
        pass

    # Create a test play
    play = FakePlay()
    # Create a test role
    role = FakeRole()
    # Create a fake variable manager
    var_mgr = FakeVarMgr()
    # Create a fake loader
    loader = FakeLoader()
    # Create a test handler
    handler = FakeHandler()

    # Create a ds for a block and for a task.
    block_ds = {'block': 'foo'}
    task_ds = {'task': 'bar'}
    # Create a test ds (ds = data structure)
    test_ds

# Generated at 2022-06-13 08:26:29.589432
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    #TODO: get this working
    pass



# Generated at 2022-06-13 08:26:41.492633
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.handler import Handler
    from ansible.playbook.task import Task

    task_list = load_list_of_tasks(['name: task1', 'name: task2'], None, None, None, False, None, None)
    assert len(task_list) == 2
    assert len(task_list) == 2
    assert task_list[0].name == 'task1'
    assert task_list[1].name == 'task2'
    assert isinstance(task_list[0], Task)
    assert isinstance(task_list[1], Task)


# Generated at 2022-06-13 08:26:51.558229
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    # These are the only imports needed for this function to unit test
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.role_include import IncludeRole
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.module_utils.common._collections_compat import Mapping

    # Create Needed objects
    t1 = Task()
    t2 = Task()
    t3 = Task()
    ti = TaskInclude()
    ir = IncludeRole()
    ir._parent = t2
    host = Host()


# Generated at 2022-06-13 08:26:59.300764
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    file_name = os.path.join(os.path.dirname(__file__),"../../playbooks/test_playbooks/hello_world.yaml")
    with open(file_name, 'r') as f:
        data = yaml.safe_load(f.read())
    t = load_list_of_tasks(data,None,None,None,None,False,None,None)
    assert t[0].action == 'debug'
    assert t[0].args == {'msg': 'Hello World!'}

# Generated at 2022-06-13 08:27:09.094757
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    # we import here to prevent a circular dependency with imports
    from ansible.playbook.block import Block
    from ansible.playbook.handler import Handler
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.role_include import IncludeRole
    from ansible.playbook.handler_task_include import HandlerTaskInclude
    from ansible.template import Templar

    # Test for explicit blocks.
    for block in load_list_of_tasks([{
        'block': [{
            'name': 'task1'
        }]
    }], None):
        assert isinstance(block, Block)
        assert block._is_subblock == block._parent is None


# Generated at 2022-06-13 08:27:20.411216
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.parsing.mod_args import ModuleArgsParser
    from ansible.template import Templar

    ds = []
    with pytest.raises(AnsibleAssertionError):
        load_list_of_tasks(ds, play=None, block=None, role=None, task_include=None, use_handlers=False, variable_manager=None, loader=None)

    ds = [ "a" ]
    with pytest.raises(AnsibleAssertionError):
        load_list_of_tasks(ds, play=None, block=None, role=None, task_include=None, use_handlers=False, variable_manager=None, loader=None)

    ds = [ { "a": {} } ]

# Generated at 2022-06-13 08:27:25.995800
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    # Call function
    a = load_list_of_tasks(ds, play, block, role, task_include, use_handlers, variable_manager, loader)
    print(a)

if __name__ == '__main__':
    test_load_list_of_tasks()

# Generated at 2022-06-13 08:27:35.455164
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    # We don't want to test the entire load_list_of_tasks() function here, as
    # that would be testing a lot of internal ansible code. We only want to
    # test the function's interface with code that we have written.

    # First, the function should take a list of task dictionaries. Since
    # load_tasks() is what calls load_list_of_tasks(), we can get a list of
    # task dictionaries from load_tasks().
    #
    # We need a Playbook object to call load_tasks()
    from ansible.playbook.play import Play
    from ansible.playbook.playbook import Playbook
    from ansible.playbook.role import Role

    pb = Playbook()

# Generated at 2022-06-13 08:27:48.392124
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    '''
    Basic tests for function load_list_of_tasks,
    does not test the backend functions called.
    '''
    # FIXME: we should improve load_list_of_tasks so that we don't need to create fake objects like this
    fake_play = object()
    fake_block = object()
    fake_role = object()
    fake_task_include = object()
    fake_use_handlers = object()
    fake_variable_manager = object()
    fake_loader = object()

    # Make sure ds is a list, otherwise we'll get an AssertionError
    ds = [{'local_action': 'supertest hello'}]

# Generated at 2022-06-13 08:27:51.264076
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    # FIXME: it is hard to unit test function load_list_of_tasks since it has so many dependencies
    pass

# Generated at 2022-06-13 08:28:31.962696
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.play_context import PlayContext
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.display import Display
    from ansible.utils.vars import combine_vars
    from ansible.vars.unsafe_proxy import wrap_var
    import ansible.constants as C

    display = Display()
    loader = DataLoader()
    inventory = InventoryManager(loader=loader,   sources="localhost,")
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    play_context = PlayContext()

# Generated at 2022-06-13 08:28:44.033901
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    import sys, os
    sys.path.append('../')
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.role_include import IncludeRole
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.module_utils.common.collections import is_sequence


    ds_list = [
        {
            'include_role': {
                'name': 'test'
            }
        }
    ]

    ds_list_2 = [
        {
            'include_tasks': {
                'name': 'test'
            }
        }
    ]


# Generated at 2022-06-13 08:28:50.208465
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.role.include import IncludeRole
    from ansible.plugins.loader import action_loader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()

    host_list = [{"hostname": "test.example.com", "port": 22}]
    inventory = InventoryManager(loader=loader, sources=host_list)
    variable_manager = VariableManager(loader=loader, inventory=inventory)


# Generated at 2022-06-13 08:29:01.673532
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    import os
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils._text import to_text
    from ansible.playbook.task import Task
    task_ds = [{'action':'File', 'module':'file', 'args':{'dest':'/tmp/asdfasdf'}}]
    #task_ds.append({'action':'template', 'module':'template', 'args':{'src':'/tmp/asdfasdf'}})
    #task_ds.append({'action':'include', 'module':'include', 'args':{'src':'/tmp/asdfasdf'}})
    #task_ds.append({'action':'copy', 'module':'copy', 'args':{'src':'/tmp/asdfasdf'}})
    #

# Generated at 2022-06-13 08:29:11.952740
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    import pytest

    with pytest.raises(AssertionError):
        load_list_of_tasks("abc", None, None, None)

    with pytest.raises(AnsibleAssertionError):
        load_list_of_tasks([{'name': 'a'}, {'name': 'b', 'block': 'xxx'}], None, None, None, task_include=None)

    with pytest.raises(AnsibleParserError):
        load_list_of_tasks([{'name': 'a'}, {'name': 'b'}], None, None, None, task_include=None)

# Generated at 2022-06-13 08:29:22.413889
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from config import C
    for action in C._ACTION_ALL_INCLUDE_IMPORT_TASKS:
        task_ds = dict(action=action, M_FOO=dict(BAR=dict(BAZ=1), BAR1=dict(BAZ1=2)))
        args_parser = ModuleArgsParser(task_ds)
        (action, args, delegate_to) = args_parser.parse(skip_action_validation=True)
        assert action == 'include_tasks'
        assert args == dict(BAR=dict(BAZ=1), BAR1=dict(BAZ1=2))
        assert delegate_to is None


# Generated at 2022-06-13 08:29:32.114479
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    # we import here to prevent a circular dependency with imports
    from ansible.playbook.play import Play
    from ansible.playbook.block import Block
    from ansible.playbook.role_include import IncludeRole
    from ansible.vars.manager import VariableManager
    from ansible.vars.hostvars import HostVars

    m_args = dict(
        delegate_to='foobar',
        tags=['tagssssss'],
    )

    m_ds = dict(
        action='ping',
        args=m_args,
        loop='localhost',
        loop_args=dict(
            _raw_params=['a', 'b', 'c'],
        ),
    )


# Generated at 2022-06-13 08:29:39.993919
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    # we import here to prevent a circular dependency with imports
    from ansible.playbook.task import Task, TaskInclude
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.role_include import IncludeRole
    from ansible.playbook.play import Play
    from ansible.playbook.role import Role
    from ansible.playbook.handler import Handler

    hostvars = dict(
        ansible_all_ipv4_addresses=['1.1.1.1', '2.2.2.2'],
        ansible_hostname='fakehost',
        ansible_default_ipv4=dict(address='1.1.1.1'),
    )
    LOADER = DataLoader()
    VARS_MANAGER = VariableManager()
    VARS_

# Generated at 2022-06-13 08:29:48.763176
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    # create a mock loader object and set it up with a simple inventory
    mock_loader = DictDataLoader({
        "gather_facts_example.yaml": """
---
tasks:
  - name: gather facts
    setup:
""",
        "debug_example.yaml": """
---
tasks:
  - name: debug example
    debug:
      msg: "This is a debug message"
""",
        "handler_example.yaml": """
---
handlers:
  - name: restart apache
    service:
      name: apache2
      state: restarted
""",
    })

    # generate the list of tasks

# Generated at 2022-06-13 08:29:51.473812
# Unit test for function load_list_of_blocks
def test_load_list_of_blocks():
    ds = [
        {'block': 'test1'},
        {'block': 'test2'},
    ]
    load_list_of_blocks(ds)

