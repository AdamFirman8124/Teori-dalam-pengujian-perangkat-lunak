

# Generated at 2022-06-13 08:20:55.746714
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    pass

# Generated at 2022-06-13 08:20:59.322643
# Unit test for function load_list_of_roles
def test_load_list_of_roles():
    ds = [{'name': 'apache'}]
    play = Play()
    current_role_path = None
    variable_manager = None
    loader = None
    collection_search_list = False
    a = load_list_of_roles(ds, play=play, current_role_path=current_role_path, variable_manager=variable_manager, loader=loader, collection_search_list=collection_search_list)
    print(a)


# Generated at 2022-06-13 08:21:00.448296
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    pass

# Generated at 2022-06-13 08:21:04.734916
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    ds = [{
        'block': [
            {'block': [
                {'debug': {'msg': '1'}},
                {'debug': {'msg': '2'}}
            ]},
            {'block': [
                {'debug': {'msg': '3'}},
                {'debug': {'msg': '4'}}
            ]}
        ]
    }]
    load_list_of_tasks(ds, None, None, None, None, None, None, None)



# Generated at 2022-06-13 08:21:11.975986
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    display.verbosity = 4

    # TESTS:
    #   1. Normal
    #
    #       1.1 Params
    #       1.2 No params
    #       1.3 Module args
    #       1.4 Modules args + params
    #
    #   2. Local
    #       2.1 Params
    #       2.2 No params
    #       2.3 Module args
    #       2.4 Modules args + params
    #
    #   3. Include
    #       3.1 Params
    #       3.2 No params
    #       3.3 Tags
    #       3.4 When
    #       3.5 With_items
    #       3.6 With_items with loop_control
    #
    #   4. Local + Include
    #       4.1

# Generated at 2022-06-13 08:21:24.661501
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.task import Task


# Generated at 2022-06-13 08:21:33.362703
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    # Unit: ansible.playbook.helpers
    import ansible.playbook.block

    # monkey patch this test method over to an empty
    # one that does nothing so we don't need to import all
    # the block stuff, which introduces too many other
    # dependencies for a simple test. This also avoids
    # the need for a real task and task_include, which means
    # we can avoid most of the other imports we would need
    # for this test.
    ansible.playbook.block.Block._load_parents = lambda self: None


# Generated at 2022-06-13 08:21:34.421730
# Unit test for function load_list_of_roles
def test_load_list_of_roles():
    pass


# Generated at 2022-06-13 08:21:44.227398
# Unit test for function load_list_of_roles
def test_load_list_of_roles():
    '''
    This test case checks the loading list of roles
    '''

    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from units.mock.loader import DictDataLoader

    vars_manager = VariableManager()
    loader = DictDataLoader(dict())

    test_role_def = [{"role": "test_role", "become": True, "become_user": "root"}]
    role_list = load_list_of_roles(test_role_def, None, variable_manager=vars_manager, loader=loader)
    assert len(role_list) == 1
    assert role_list[0]._role_name == "test_role"
    assert role_list[0].become == True
    assert role

# Generated at 2022-06-13 08:21:53.686975
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():

    from ansible.playbook.block import Block
    from ansible.playbook.handler import Handler
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.role_include import IncludeRole

    class Play():
        name = 'test_play'

    p = Play()


# Generated at 2022-06-13 08:22:35.690054
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.handler import Handler
    from ansible.playbook.handler_task_include import HandlerTaskInclude
    from ansible.playbook.block import Block
    from ansible.vars.manager import VariableManager
    from ansible.vars.hostvars import HostVars
    from ansible.executor.task_queue_manager import TaskQueueManager

    variable_manager = VariableManager()
    inventory = Inventory(loader=None, variable_manager=variable_manager, host_list=[])
    variable_manager.set_inventory(inventory)


# Generated at 2022-06-13 08:22:44.436997
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    task_1 = {"name": "action_1", "action": {"module": "copy", "args": "content=test1 dest=test1"}}
    task_2 = {"name": "action_2", "action": {"module": "copy", "args": "content=test2 dest=test2"}}
    task_list = [task_1, task_2]
    expected_task_list = [Task(ds=task_1), Task(ds=task_2)]
    assert load_list_of_tasks([task_1, task_2]) == expected_task_list

# Generated at 2022-06-13 08:22:45.697616
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    pass


# Generated at 2022-06-13 08:22:53.763073
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    import pytest

# Generated at 2022-06-13 08:23:04.071656
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.handler import Handler
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.block import Block

    display = Display()

    def handler_load(
        ds,
        block=None,
        role=None,
        task_include=None,
        use_handlers=False,
        variable_manager=None,
        loader=None,
    ):
        Handler.load(
            ds,
            block=block,
            role=role,
            task_include=task_include,
            variable_manager=variable_manager,
            loader=loader,
        )


# Generated at 2022-06-13 08:23:12.305244
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.task import Task
    from ansible.parsing.dataloader import DataLoader

    ds = [{'hosts': 'local'}]
    play = None
    block = None
    role = None
    task_include = None
    use_handlers = False
    variable_manager = None
    loader = DataLoader()
    task_list = load_list_of_tasks(ds, play, block, role, task_include, use_handlers, variable_manager, loader)
    assert isinstance(task_list[0], Task)

# Generated at 2022-06-13 08:23:23.983103
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    # pylint: disable=missing-docstring
    # pylint: disable=unexpected-keyword-arg
    def make_task(data):
        task = MagicMock()
        task.as_dict = Mock(return_value=data)
        return task

    def make_task_dict(data):
        ds = MagicMock()
        ds.as_dict = Mock(return_value=data)
        return ds
    # pylint: enable=missing-docstring
    # pylint: enable=unexpected-keyword-arg

    # test_empty_list
    data = []
    tasks = load_list_of_tasks(data, None)
    assert not tasks

    # test_list_with_one_task
    data = [{'foo': 'bar'}]
   

# Generated at 2022-06-13 08:23:24.626602
# Unit test for function load_list_of_blocks
def test_load_list_of_blocks():
   assert True

# Generated at 2022-06-13 08:23:36.289441
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    #
    # Tests that a single task can be parsed correctly. 
    # The same test is performed for a list of tasks.
    #
    from ansible.playbook.task import Task
    from ansible.playbook.handler import Handler
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.block import Block
    #TODO: This test should be broken up into smaller chunks

# Generated at 2022-06-13 08:23:45.834901
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    class FakeLoader():
        def __init__(self):
            self.vault_passwords = {}
            self.path_info = []
    # Loader object
    loader = FakeLoader()

    # VariableManager object
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, sources='localhost,')
    variable_manager.set_inventory(inventory)

    task_ds1 = {
        'block': '',
        'rescue': '',
        'always': '',
        'tags': [],
        'vars': {},
        'when': ''
    }


# Generated at 2022-06-13 08:24:11.924690
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    ds = [{'action': 'import_role', 'name': 'test'}, {'block': [{'action': 'import_role', 'name': 'test'}]}]
    play = {}
    block = None
    role = {}
    task_include = None
    use_handlers = False
    variable_manager = {}
    loader = {}
    task_list = load_list_of_tasks(ds, play, block, role, task_include, use_handlers, variable_manager, loader)
    assert_equal(3, len(task_list))

# Generated at 2022-06-13 08:24:24.306776
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.parsing.dataloader import DataLoader
    
    # Data structure of list of task
    # [
    #    {
    #        "action": {
    #            "module": "some_module",
    #            "args": "some_args"
    #        },
    #        "delegate_to": "some_delegate_to",
    #        "register": "some_register"
    #    },
    #    {
    #        "block": [
    #            {
    #                "action": {
    #                    "module": "some_module",
    #                    "args": "some_args"
    #                },
    #                "delegate_to

# Generated at 2022-06-13 08:24:33.908971
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.vars.manager import VariableManager
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.plugins.callback import CallbackBase
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.plugins.loader import action_loader
    from ansible.playbook.role import Role
    import json


# Generated at 2022-06-13 08:24:42.671915
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.base import Base
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block

    class FakePlay(Base):
        def __init__(self):
            self.playbook = 'playbook.yml'
            self.options = OptionsMock()
            self.hosts = ['localhost', '127.0.0.1']
            self.vars = dict()
            self.default_vars = dict()

    class FakeBlock(Block):
        def __init__(self):
            self.vars = dict()
            self.default_vars = dict()

    class FakeTask(Task):
        def __init__(self):
            self.action = 'notify'

    fake_play = FakePlay

# Generated at 2022-06-13 08:24:58.026695
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():

    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.template import Templar
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.vars.manager import VariableManager
    from ansible.utils.vars import combine_vars


# Generated at 2022-06-13 08:25:00.453054
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    assert False, "No test for function load_list_of_tasks"



# Generated at 2022-06-13 08:25:01.934453
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    pass #FIXME



# Generated at 2022-06-13 08:25:02.495987
# Unit test for function load_list_of_roles
def test_load_list_of_roles():
    pass

# Generated at 2022-06-13 08:25:12.618691
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():

    #######  DATASTRUCTURE FOR load_list_of_tasks() #######

    # All proper tasks
    proper_task_list = [
        {'action': 'demo1'},
        {'action': 'demo2'},
        {'action': 'demo3'},
    ]

    # All Tasks that include
    task_include_list = [
        {'include': 'demo1.yml'},
        {'action': 'demo2'},
        {'action': 'demo3'},
    ]

    # Some tasks and some tasks that include
    mixed_task_list = [
        {'include': 'demo1.yml'},
        {'action': 'demo2'},
        {'include': 'demo3.yml'},
    ]

# Generated at 2022-06-13 08:25:13.633826
# Unit test for function load_list_of_blocks
def test_load_list_of_blocks():
    pass

# Generated at 2022-06-13 08:25:27.618570
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    # TODO: write unit test here
    pass



# Generated at 2022-06-13 08:25:40.788373
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    print('Testing load_list_of_tasks')
    assert 'ERROR' not in load_list_of_tasks(0, 'play')
    assert load_list_of_tasks(None, 'play') is None
    assert load_list_of_tasks([], 'play') == []
    assert 'ERROR' in load_list_of_tasks(1, 'play')
    assert 'ERROR' in load_list_of_tasks([0], 'play')
    assert 'ERROR' in load_list_of_tasks([1], 'play')
    assert load_list_of_tasks([{'block': [], 'name': 'test'}], 'play') == ['task: test']

# Generated at 2022-06-13 08:25:48.391946
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    # TODO: This test is incomplete. We should validate that the output of the function is what we expect

    from ansible.playbook import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.role import Role
    from ansible.playbook.role_context import RoleContext
    from ansible.playbook.task_include import TaskInclude


# Generated at 2022-06-13 08:26:01.271106
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    # This is a unit test for function load_list_of_tasks.
    # This function creates a list of task objects from a list of task dictionaries.

    # Create list of task dictionaries.
    task1_dict = dict()
    task1_dict['action'] = 'A'
    task1_dict['args'] = 'B'
    task1_dict['async'] = 'C'
    task1_dict['async_poll_interval'] = 'D'
    task1_dict['async_status_file'] = 'E'
    task1_dict['become'] = 'F'
    task1_dict['become_method'] = 'G'
    task1_dict['become_user'] = 'H'
    task1_dict['check_mode'] = 'I'
    task1_

# Generated at 2022-06-13 08:26:05.212183
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task

    task_list = load_list_of_tasks([{}, {}])

    assert(isinstance(task_list[0], Block))
    assert(isinstance(task_list[1], Block))

# Generated at 2022-06-13 08:26:16.104445
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.play import Play
    from ansible.plugins.loader import action_loader, module_loader
    from ansible.playbook.role_include import IncludeRole

    module_loader.add_directory(DATA_PATH)
    action_loader.add_directory(DATA_PATH, with_subdir=True, with_files=True)

    ds = []
    task_ds = dict()
    task_ds["include"] = "somefile"
    task_ds["block"] = "someblock"
    ds.append(task_ds)

    ds.append(dict(name="another"))

    play = Play()
    task_list = []
    task_list = load_list_of_tasks(ds, play=play)
    assert len(task_list) == 3



# Generated at 2022-06-13 08:26:24.095548
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.role import Role
    
    # (1) Test a list of tasks
    ds = [
       {
         "action": "set_fact",
         "args": {
           "ansible_all_ipv4_addresses": "['10.0.0.7', '172.16.0.3']"
         }
       }
    ]
    task_list = load_list_of_tasks(ds=ds, play=None, block=None, role=None, task_include=None, use_handlers=False, variable_manager=None, loader=None)
    assert isinstance(task_list[0], Task)
    assert task_list[0].action == 'set_fact'

# Generated at 2022-06-13 08:26:34.968748
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
  from ansible.playbook.play import Play
  from ansible.vars import VariableManager
  from ansible.inventory import Inventory
  from ansible.parsing.dataloader import DataLoader
  from ansible.executor import playbook_executor

  display = Display()

  loader = DataLoader()
  variable_manager = VariableManager()
  playbook = Play.load(loader=loader, variable_manager=variable_manager, file_name='tasks.yml', play=None, task_include=None, use_handlers=False, role=None)
  playbook.post_validate(inventory=None)




# Generated at 2022-06-13 08:26:41.750467
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.task import Task
    for task_ds in [{'action': 'ping', 'name': 'p'}, {'block': 'block', 'name': 'n1'}]:
        if not isinstance(task_ds, dict):
            raise AnsibleAssertionError('The ds (%s) should be a dict but was a %s' % (ds, type(ds)))
    for t in [Task(), Block()]:
        assert type(t) is not None

# Generated at 2022-06-13 08:26:51.770364
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.base import Base
    class Play(Base):
        def __init__(self):
            Base.__init__(self)
            self._entries = []
            self._handlers = []
            self.hosts = ['localhost']
            self.default_vars = dict()

    class Task(Base):
        __slots__ = Base.__slots__ + ('_parent',
                                      'action', 'args', 'async_val', 'delegate_to',
                                      'delegate_facts', 'environment', 'ignore_errors', 'loop',
                                      'loop_args', 'loop_control', 'notify', 'register',
                                      'retries', 'run_once', 'until', 'tags', 'when', 'with_items', '_role')

# Generated at 2022-06-13 08:27:32.639838
# Unit test for function load_list_of_blocks
def test_load_list_of_blocks():
    from ansible.playbook.task import Task
    tasks = [
        {'name': 'test1', 'action': {'module': 'shell', 'args': 'ls'}},
        {'name': 'test2', 'action': {'module': 'shell', 'args': 'ls'}},
        {'name': 'test3', 'action': {'module': 'shell', 'args': 'ls'}},
        ]
    blocks = load_list_of_blocks(tasks, play=None, parent_block=None, role=None, task_include=None, use_handlers=False, variable_manager=None, loader=None)
    assert len(blocks) == 1
    assert len(blocks[0].block) == 3
    assert isinstance(blocks[0].block[0], Task)

# Generated at 2022-06-13 08:27:42.770303
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    # First test: normal case
    display.deprecated("Using 'ansible.parsing.dataloader.load_list_of_tasks' directly is deprecated", version='2.9')
    ds = [
        {'action': 'test', 'register': 'test'},
        {'include': 'test.yml', 'static': False}
    ]
    assert len(load_list_of_tasks(ds, None, None, None, None, False, None, None)) == 2
    # FIxme: Add more unit tests for edge cases


# Generated at 2022-06-13 08:27:51.218596
# Unit test for function load_list_of_roles
def test_load_list_of_roles():
    '''
      ansible.playbook.play_context.PlayContext test cases
    '''
    ds_list = ['first_role','second_role','third_role']
    current_role_path = '/root'
    play = {'hosts': 'localhost'}
    variable_manager = {'host_list': 'localhost'}
    loader = {'host_list': 'localhost'}
    expected_result = []
    assert load_list_of_roles(ds_list, play, current_role_path, variable_manager, loader) == expected_result



# Generated at 2022-06-13 08:28:00.542490
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources='localhost,')
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    # The type of task_ds is [dict]
    task_ds = [{
        'action': 'copy',
        'copy': 'src=template dest=/etc/nginx.conf owner=root group=root mode=0644'
    }]
    play = None
    block = None
    role = None
    task_include = None
    use_handlers = False
    loader = None
    # task_list should be [<ansible.playbook.task.Task object at 0

# Generated at 2022-06-13 08:28:09.917586
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    ds = [{'block:' : {'block_tasks' : 'abc'}, 'abc' : 'def'}]
    task_list = load_list_of_tasks(ds)
    assert(isinstance(task_list[0], Block))
    assert(isinstance(task_list[0].block[0], TaskInclude))
    
    
    
    

# Generated at 2022-06-13 08:28:24.112639
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from collections import namedtuple
    from ansible.vars.clean import module_response_deepcopy

    # This function creates a YAML file with a list of a few tasks that
    # can be used for testing load_list_of_tasks. This is the contents of
    # this YAML file.
    #
    # - import_tasks: tasks1.yaml
    #
    # - name: task2
    #   local_action: foo
    #   register: x
    #
    #
    # - name: task3
    #   local_action: foo
    #   register: x
    # - debug: var=x
    #
    # - name: task4
    #   local_action: foo
    #   register: x
    # - debug: var=x
    #
    #

# Generated at 2022-06-13 08:28:35.529662
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():

    from ansible.playbook import Play
    from ansible.playbook.block import Block
    from ansible.playbook.block_include import BlockInclude
    from ansible.playbook.handler_task_include import HandlerTaskInclude
    from ansible.playbook.task import Task

    # we import here to prevent a circular dependency with imports
    from ansible.playbook.role_include import IncludeRole

    ds = [
        {'include': 'foo'},
        {'block': {'hosts': 'foo', 'tasks': [{'name': 'bar'}]}},
        {'include': 'bar'},
    ]

    play = Play().load({}, variable_manager=dict(), loader=dict())
    # for now we need to mockup an object which looks like a block
    block = Block()
    role

# Generated at 2022-06-13 08:28:46.693843
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    #
    # Prepare a task list
    #
    play = Play()

    task1 = dict(name='foo', action=dict(module='command', args='ls'))
    task2 = dict(name='bar', action=dict(module='command', args='date'))
    tasks = [task1, task2]

    #
    # Execute the function
    #
    task_list = load_list_of_tasks(ds=tasks, play=play, block=None, role=None, task_include=None, use_handlers=False, variable_manager=None, loader=None)

    #
    # Validate the result
    #
    assert len(task_list) == 2
    assert task_list[0].name == 'foo'
    assert task_list[0].args == 'ls'
   

# Generated at 2022-06-13 08:28:49.031405
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    """
    Test load_list_of_tasks function
    """
    assert False, 'Test not implemented'

# Generated at 2022-06-13 08:29:00.730991
# Unit test for function load_list_of_blocks
def test_load_list_of_blocks():
    from ansible.playbook import Play
    import ansible.constants as C
    from ansible.inventory import Inventory
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = Inventory(loader=loader, variable_manager=variable_manager)
    variable_manager.set_inventory(inventory)
    variable_manager.extra_vars = {}
    play_context = PlayContext()
    play = Play.load(None, variable_manager=variable_manager, loader=loader, play_context=play_context)

# Generated at 2022-06-13 08:29:30.216508
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    pass



# Generated at 2022-06-13 08:29:38.730663
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.role_include import IncludeRole
    from ansible.playbook.handler import Handler
    from ansible.playbook.handler_task_include import HandlerTaskInclude
    from ansible.playbook.block import Block
    from ansible.playbook.play import Play
    from ansible.playbook.playbook_include import PlaybookInclude
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    # Test: check that bare task is converted to implicit block

# Generated at 2022-06-13 08:29:42.479449
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    # Test load_list_of_tasks

    # Load a list of tasks
    args_parser = ModuleArgsParser({'name': 'test_name'})
    args = args_parser.parse()
    assert args == ('test_name', {}, None)



# Generated at 2022-06-13 08:29:50.298424
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    loader, variable_manager, all_vars = mock_loader()
    # print ("<test_load_list_of_tasks> loader = %s"%loader)
    # print ("<test_load_list_of_tasks> variable_manager = %s"%variable_manager)
    # print ("<test_load_list_of_tasks> all_vars = %s"%all_vars)
    ds_list = [{'name': 'test', 'action': 'test'}]
    task_list = load_list_of_tasks(ds_list, None, None, None, None, False, variable_manager, loader)
    assert bool(task_list)
    assert task_list[0].action == 'test'

# Construct "hostvars" cache to be used in role/task

# Generated at 2022-06-13 08:29:55.792811
# Unit test for function load_list_of_tasks

# Generated at 2022-06-13 08:30:01.053993
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.role_include import IncludeRole
    from ansible.playbook.task import Task
    from ansible.template import Templar
    from ansible.playbook.task_include import TaskInclude

# Generated at 2022-06-13 08:30:01.701465
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    assert True

# Generated at 2022-06-13 08:30:12.577666
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.role.requirement import RoleRequirement
    from ansible.playbook.play import Play
    from ansible.playbook.playbook import Playbook
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.handlers.handler import Handler
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.task_result import TaskResult
    from ansible.module_utils import basic
    from ansible.module_utils.six import PY3
    if not PY3:
        import __builtin__ as builtins
    else:
        import builtins
    # patch stdout/err so we don't get them in nose output

# Generated at 2022-06-13 08:30:23.691458
# Unit test for function load_list_of_roles
def test_load_list_of_roles():

    # Provide all the arguments needed by load_list_of_roles
    ds = {
      "name": "test_role",
      "role_path": "/tmp/test_role",
      "tags": "test_tags",
      "when": "test_when",
      "defaults": "test_defaults",
      "vars": "test_vars",
      "meta": "test_meta",
      "handlers": "test_handlers",
      "dependencies": "test_dependencies",
      "allow_duplicates": False
    }
    # load_list_of_roles expects all the arguments as a list
    ds = [ds]

    # Mocking all the arguments needed by load_list_of_roles function

# Generated at 2022-06-13 08:30:34.282078
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    with pytest.raises(AnsibleAssertionError):
        load_list_of_tasks()
    with pytest.raises(AnsibleAssertionError):
        load_list_of_tasks("not a list")
    with pytest.raises(AnsibleAssertionError):
        load_list_of_tasks([{}])
    with pytest.raises(AnsibleParserError):
        load_list_of_tasks([{'block': 'not_a_dict'}])
    load_list_of_tasks([{'block': {}}])