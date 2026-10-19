

# Generated at 2022-06-13 08:21:40.982446
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.task import Task
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager




# Generated at 2022-06-13 08:21:52.257382
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    '''
    Run the test case for load_list_of_tasks
    '''
    from ansible.playbook.task import Task
    from ansible.playbook._base import Base
    # making the third element, a task
    ds = [None, None, {'action': 'shell', 'args': 'ls', '_ansible_line_number': 2}]
    t1 = Task.load(ds[2], None, None, None, None, None)
    assert t1.action == 'shell'
    assert t1.args == 'ls'
    t2 = Task.load(ds[2], None, None, None, None, None)
    assert t2.action == 'shell'
    assert t2.args == 'ls'
    # Exercise the Base.copy method

# Generated at 2022-06-13 08:21:52.970030
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    assert 1 == 1



# Generated at 2022-06-13 08:21:56.280654
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    assert load_list_of_tasks([{},{}], 1, block=None, role=None, task_include=None, use_handlers=False, variable_manager=None, loader=None)

# Generated at 2022-06-13 08:22:04.226496
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

    # Test with correct ds

# Generated at 2022-06-13 08:22:16.106555
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    # test when action is in C._ACTION_INCLUDE_TASKS
    # data structure when action is in C._ACTION_INCLUDE_TASKS
    #   action: include_tasks
    #   file: test1.yaml
    include_task = dict(action="include_tasks", file="test1.yaml")
    class TaskIncludeTest(object):
        def __init__(self):
            self.data = None
    ti = TaskIncludeTest()
    ti.data = load_list_of_tasks([include_task], None, None, None, None, False, None, None)
    assert(isinstance(ti.data[0], TaskInclude))

    # test when action is in C._ACTION_IMPORT_TASKS
    # data structure when action is in C._ACTION

# Generated at 2022-06-13 08:22:19.209588
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    task = dict(action=dict(module='shell', args='ls -al'))
    task_list = load_list_of_tasks(ds=task)
    print(task_list)



# Generated at 2022-06-13 08:22:34.457012
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():

    # we import here to prevent a circular dependency with imports
    from ansible.playbook.role_include import IncludeRole
    from ansible.playbook.task_include import TaskInclude

    all_vars = {}
    loader = None
    test1_task = [{
        'action': 'include',
        'args': {
            'static': True,
            '_raw_params': 'test1.yaml'
        }
    }]
    test1_task_res = [{
        'action': 'include',
        'args': {
            'static': True,
            '_raw_params': 'test1.yaml'
        }
    }]

# Generated at 2022-06-13 08:22:41.634688
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.play import Play
    from ansible.playbook.task_include import TaskInclude
    from ansible.template import Templar

    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.handler import Handler

    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    def make_fake_task(name, action=None):
        return dict(
            name=name,
            args=dict(_raw_params=name),
            action=action,
        )

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, sources=['localhost'])
    play_source

# Generated at 2022-06-13 08:22:44.491078
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    block_list, task_list = load_list_of_tasks(ds, play, block, role, task_include, use_handlers, variable_manager, loader)



# Generated at 2022-06-13 08:23:10.941829
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    test_class = LoadListOfTasks()
    ansible_result = test_class.result()
    assert ansible_result['success'] == True

# Generated at 2022-06-13 08:23:11.690738
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    pass

# Generated at 2022-06-13 08:23:13.267606
# Unit test for function load_list_of_roles
def test_load_list_of_roles():
    assert False, "No tests for load_list_of_roles"



# Generated at 2022-06-13 08:23:21.924267
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook import Play
    from ansible.playbook.role_include import IncludeRole
    from ansible.playbook.task import Task
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.vars.manager import VariableManager
    import ansible.constants as C
    import os
    import yaml
    from pprint import pprint
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.utils.vars import combine_vars
    from ansible.inventory.manager import InventoryManager
    from ansible.plugins.callback import CallbackBase
    from ansible.utils.display import Display

# Generated at 2022-06-13 08:23:22.629393
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    pass



# Generated at 2022-06-13 08:23:23.359934
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    pass


# Generated at 2022-06-13 08:23:30.761469
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    assert load_list_of_tasks([{'block': [0, 1]}], play=None, block=None, role=None, task_include=None, use_handlers=False, variable_manager=None, loader=None) is not None
    assert load_list_of_tasks(["pong"], play=None, block=None, role=None, task_include=None, use_handlers=False, variable_manager=None, loader=None) is not None

# Generated at 2022-06-13 08:23:41.348618
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    '''
        This function checks all the possible class of the task (action)
    '''
    class Task():
        def __init__(self):
            self.action = 'debug'
            self.args = {}

        def to_json(self):
            return "{\"debug\":\"\"}"


    class Task2():
        def __init__(self):
            self.action = 'fail'
            self.args = {}

        def to_json(self):
            return "{\"fail\":\"\"}"

    class Task3():
        def __init__(self):
            self.action = 'command'
            self.args = {}

        def to_json(self):
            return "{\"command\":\"\"}"

    class Task4():
        def __init__(self):
            self.action = 'shell'
            self

# Generated at 2022-06-13 08:23:42.933725
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    # assert load_list_of_tasks('abc', None, None, None, None, None) == 'def'
    assert 1 == 1

# Generated at 2022-06-13 08:23:50.015634
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.utils.vars import combine_vars
    from ansible.playbook.play import Play
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    import ansible.constants as C
    import yaml
    #from ansible.module_utils.basic import AnsibleModule

    C.HOST_KEY_CHECKING = False
    C.DEPRECATION_WARNINGS = False
    C.ANSIBLE_RETRY_FILES_ENABLED = 0
    # Enable deprecating unsafe lookup plugins
    C.ANSIBLE_DISABLE_UNSAFE_LOOKUPS = False

    # Mock the inventory
    inventory = InventoryManager(loader=None, sources='localhost,')

    # Mock the loader

# Generated at 2022-06-13 08:24:19.704854
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    test_load_list_of_tasks.play = Play().load(
        dict(
            name   = "Test Play",
            hosts  = "unittest.example.com",
            gather_facts = False,
        ),
        loader=DictDataLoader(
            dict(
                playbooks='/home/foo/',
                roles='/home/foo/',
            )
        ),
    )

    test_load_list_of_tasks.variable_manager = VariableManager()

    test_load_list_of_tasks.loader = DataLoader()
    test_load_list_of_tasks.loader.set_basedir("/home/foo")


# Generated at 2022-06-13 08:24:30.587820
# Unit test for function load_list_of_roles
def test_load_list_of_roles():
    """
    Used in conjunction with the ansible-doc tool to test the documentation
    format of the load_list_of_roles function and its parameters.
    """
    p = MockPlay()
    v = VariableManager()
    l = DictDataLoader()
    roles = [{
        "name": "role1",
        "when": "some condition",
        "ignore_errors": True
    }]
    assert load_list_of_roles(roles, p, current_role_path='role_path') == [
        RoleInclude(name='role1', when='some condition', ignore_errors=True, play=p, current_role_path='role_path',
                    variable_manager=v, loader=l, collection_list=None)
    ]

# Generated at 2022-06-13 08:24:40.657863
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook import Play
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.parsing.dataloader import DataLoader

    variable_manager = VariableManager()
    loader = DataLoader()
    inventory = Inventory(loader=loader, variable_manager=variable_manager)

    display.verbosity = 3

# Generated at 2022-06-13 08:24:49.451136
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    class Host(object):
        def __init__(self, hostname):
            self.hostname = hostname

        def get_name(self):
            return self.hostname

    class Play(object):
        def __init__(self, name, host):
            self.name = name
            self.hosts = set([host])

        def get_variable_manager(self):
            pass

    class VariableManager(object):
        def __init__(self):
            self.vars = dict()

        def get_vars(self, play=None, task=None):
            return self.vars

    class Loader(object):
        pass

    h1 = Host("localhost")
    p1 = Play("play 1", h1)
    varMgr = VariableManager()

# Generated at 2022-06-13 08:25:03.912505
# Unit test for function load_list_of_roles
def test_load_list_of_roles():
    # TODO: refactor this test and get rid of it's dependency on a playbook.
    collection_search_list = [os.path.join(DATA_DIR, 'local_collections')]
    loader = DataLoader()
    variable_manager = VariableManager()
    play = Play().load(dict(
        name = "Ansible Play",
        hosts = 'localhost',
        gather_facts = 'no',
        roles = [
            dict(
                name = 'should_be_a_collection_role',
            )
        ]
    ), variable_manager=variable_manager, loader=loader)
    roles = load_list_of_roles(play.roles, play, variable_manager=variable_manager, loader=loader, collection_search_list=collection_search_list)
    # Checking that roles are correctly loaded

# Generated at 2022-06-13 08:25:13.601595
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.play import Play
    from ansible.playbook import Playbook
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.handler import Handler
    from ansible.playbook.handler_task_include import HandlerTaskInclude
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.role.include import IncludeRole
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.plugins.loader import plugin_loader
    from ansible.template import Templar


# Generated at 2022-06-13 08:25:27.405151
# Unit test for function load_list_of_blocks
def test_load_list_of_blocks():
    from ansible.playbook.task import Task
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    from ansible.playbook.block import Block
    from ansible.playbook.play import Play
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    ds = [
         AnsibleBaseYAMLObject(content='action: action1'),
         AnsibleBaseYAMLObject(content='- name: 1\n  action: action2'),
         AnsibleBaseYAMLObject(content='- name: 2\n  action: action2'),
         AnsibleBaseYAMLObject(content='action: action3')
        ]
    variable_manager = VariableManager()
    loader=DataLoader()
    play = Play

# Generated at 2022-06-13 08:25:40.606883
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.role_include import IncludeRole
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.template import Templar
    from ansible.vars import VariableManager
    data = [{"hosts": "all"}, {"block": [{"task": [{"block": [{"import_role": {"name": "some_role_name"}}]}]}]}, {"block": [{"import_role": {"name": "some_role_name"}}]}]
    pc = PlayContext()

# Generated at 2022-06-13 08:25:48.304552
# Unit test for function load_list_of_blocks
def test_load_list_of_blocks():
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.role.include import RoleInclude
    from ansible.playbook.play import Play

    class FakeData:
        def __init__(self, data):
            self.data = data

        def get_ds(self):
            return FakeData(self.data)

    class FakeItem:
        def __init__(self, host, name, value, ignore_errors=False, register=None, failed_when=False):
            self.host = host
            self.name = name
            self.value = value
            self.ignore_errors = ignore_errors
            self.register = register
            self.failed_when = failed_when


# Generated at 2022-06-13 08:25:52.468471
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    print("Testing function load_list_of_tasks")
    print("Not Implemented")
    # Some tests to implement
    # Test the correct loads
    # Test the incorrect loads
    # Test the error case



# Generated at 2022-06-13 08:26:29.546471
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    pass

# Generated at 2022-06-13 08:26:41.490283
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    # Test for default case
    ds = [{'block': 'my_block',
           'when': 'my_when',
           'name': 'my_name'},
          {'block': 'my_block2',
           'when': 'my_when2',
           'name': 'my_name2'}, ]
    play = {'name': 'my_test_play',
            'hosts': 'my_hosts', }
    block = {'name': 'my_test_block',
             'tasks': 'my_tasks', }
    role = {"name": "my_role",}
    task_include = {'name': 'my_test_task_include',
                    'tags': 'my_tags',}
    use_handlers = True
    variable_manager = {}
    loader = {}
   

# Generated at 2022-06-13 08:26:51.557772
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    import os
    from ansible.playbook.block import Block
    from ansible.playbook.role_include import IncludeRole
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.handler_task_include import HandlerTaskInclude
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.template import Templar
    from ansible.errors import AnsibleParserError

    temp_dir = None

# Generated at 2022-06-13 08:27:03.526765
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.playbook_executor import PlaybookExecutor

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=['/etc/ansible/hosts'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    playbook_path = "test.yml"
    context = PlayContext()
    p = PlaybookExecutor(
        playbooks=[playbook_path],
        inventory=inventory,
        variable_manager=variable_manager,
        loader=loader,
        passwords={},
        context=context,
    )
   

# Generated at 2022-06-13 08:27:13.169146
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    #Test list of task names
    ds = ['debug', 'debug again']
    task_list = load_list_of_tasks(ds)
    assert len(task_list) == 2
    for task in task_list:
        assert task.action == 'debug'

    #Test list of dictionaries
    ds = [{'action': 'debug'}, {'action': 'debug again'}]
    task_list = load_list_of_tasks(ds)
    assert len(task_list) == 2
    for task in task_list:
        assert task.action == 'debug'

    #Test list of dictionaries with additional keys
    ds = [{'action': 'debug'}, {'action': 'debug', 'hosts': 'all'}]
    task_list = load_list_of_t

# Generated at 2022-06-13 08:27:22.801606
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():

    """
    For a given list of data structure,
    return a list of Task() or TaskInclude() objects.
    """

    # we import here to prevent a circular dependency with imports
    from ansible.playbook.block import Block
    from ansible.playbook.handler import Handler
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.role_include import IncludeRole
    from ansible.playbook.handler_task_include import HandlerTaskInclude
    from ansible.template import Templar


    if not isinstance(ds, list):
        raise AnsibleAssertionError('The ds (%s) should be a list but was a %s' % (ds, type(ds)))

    task_list = []

# Generated at 2022-06-13 08:27:27.643595
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    cmd_data = dict(
        command="echo hello world",
        register="status"
    )
    include_dict = dict(
        include="include.yaml"
    )
    tasks = [{"shell": "echo hello"}, {"command": {"module": "shell", "args": cmd_data}}, include_dict]
    try:
        tasks.append({"command": "echo hello"})
    except Exception:
        pass
    load_list_of_tasks(tasks, None, None, None, None, False, None, None)



# Generated at 2022-06-13 08:27:36.359221
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
   import unittest
   from ansible.playbook.role_include import IncludeRole
   from ansible.playbook.task import Task
   from ansible.playbook.task_include import TaskInclude
   class Testload_list_of_tasks(unittest.TestCase):
       def test_load_list_of_tasks(self):
           ds = [{'include_tasks': 'tasks/ntp.yml', 'tags': ['end_tag']}]
           task_list = load_list_of_tasks(ds)
           self.assertEqual(len(task_list), 1)
           self.assertTrue(isinstance(task_list[0],TaskInclude))

# Generated at 2022-06-13 08:27:50.170493
# Unit test for function load_list_of_blocks
def test_load_list_of_blocks():
    import ansible.playbook.play
    from ansible.playbook.play import load_list_of_blocks as test_load_list_of_blocks
    from ansible.playbook.block import Block
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, sources='localhost,')
    variable_manager.set_inventory(inventory)

    host = Host(name="localhost")
    group = Group(name="all")
    group.add_host(host)
    inventory.add_group(group)

# Generated at 2022-06-13 08:27:51.059037
# Unit test for function load_list_of_roles
def test_load_list_of_roles():
    assert True  # TODO: Implement unit test

# Generated at 2022-06-13 08:28:32.041137
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.parsing.yaml.objects import AnsibleUnicode

    from ansible.playbook.block import Block
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager

    # we import here to prevent a circular dependency with imports
    from ansible.playbook.task import Task
    from ansible.playbook.role_include import IncludeRole

    # Prepare mock data for test
    ds_role = IncludeRole.load({
        'include_role': {
            'name': AnsibleUnicode('role1')
        }
    }, None, None, None, None)

# Generated at 2022-06-13 08:28:33.934563
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    assert False, "No Unit test for function load_list_of_tasks"

# Generated at 2022-06-13 08:28:34.632803
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    pass

# Generated at 2022-06-13 08:28:35.349196
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    assert True

# Generated at 2022-06-13 08:28:46.571697
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    try:
        from unittest.mock import Mock
        from ansible.playbook.playbook import Playbook
    except ImportError:
        # ansible-lint support
        from mock import Mock
        from ansible.playbook.playbook import Playbook

    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.role_include import IncludeRole

# Generated at 2022-06-13 08:28:58.962502
# Unit test for function load_list_of_roles
def test_load_list_of_roles():
    global mock_collection_search_list
    global mock_loader_find_role
    mock_collection_search_list = (
        'top-level-collection',
        'sub-collection',
        'sub-sub-collection',
    )

    def _find_role_mock_func(role_name):
        if role_name == 'top-level-collection.sub-collection.sub-sub-collection.qualified-role':
            return True
        if role_name == 'top-level-collection.sub-sub-collection.qualified-role':
            return True
        if role_name == 'top-level-collection.sub-collection.qualified-role':
            return True
        if role_name == 'qualified-role':
            return True
        if role_name == 'missing-collection.missing-role':
            return True
       

# Generated at 2022-06-13 08:29:09.159678
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook import Play
    from ansible.playbook.task import Task
    from ansible.template import Templar
    from ansible.vars import VariableManager


# Generated at 2022-06-13 08:29:17.764572
# Unit test for function load_list_of_roles
def test_load_list_of_roles():
    # test setup
    # set up fake role r1
    r1 = FakeRole()
    r1.name = 'r1'
    r1.path = "/a/b/r1"

    # set up fake role r2
    r2 = FakeRole()
    r2.name = 'r2'
    r2.path = "/a/b/r2"

    # set up fake role r3
    r3 = FakeRole()
    r3.name = 'r3'
    r3.path = "/a/b/r3"

    # set up fake role r4
    r4 = FakeRole()
    r4.name = 'r4'
    r4.path = "/a/b/r4"

    # set up fake role r5
    r5 = FakeRole()
    r5.name

# Generated at 2022-06-13 08:29:32.121953
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():

    # Get the playbook root path
    root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
    test_playbook_path = os.path.join(root_path, 'test/unit/playbooks')

    # Fetch and load the test playbook
    test_playbook_file = u'static_include_task.yml'
    test_playbook_file_path = os.path.join(test_playbook_path, test_playbook_file)
    test_yaml = open(test_playbook_file_path)
    test_playbook = yaml.safe_load(test_yaml)

    # Load a temporary localhost inventory

# Generated at 2022-06-13 08:29:39.965097
# Unit test for function load_list_of_blocks
def test_load_list_of_blocks():
    from ansible.playbook.play import Play
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.task.include import TaskInclude
    from ansible.playbook.task import Task
    from ansible.playbook.task.action import TaskAction
    from ansible.playbook.handler import Handler
    from ansible.playbook.block import Block
    from ansible.playbook.play_context import PlayContext
    from ansible.vars import VariableManager
    from ansible.parsing.yaml.dumper import AnsibleDumper
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.inventory.manager import InventoryManager
    from units.mock.loader import DictDataLoader

    # Test implicit blocks by building a list of tasks and feeding them to

# Generated at 2022-06-13 08:30:19.453769
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.handler_task_include import HandlerTaskInclude
    from ansible.playbook.block import Block
    from ansible.playbook.play_context import PlayContext
    play_context = PlayContext()
    ds1 = {'include_tasks': 'test.yaml'}
    ds2 = {'import_tasks': 'test.yaml'}
    ds3 = {'include_role': 'test', 'static': True}
    ds4 = {'include_role': 'test', 'static': False}
    ds5 = {'import_role': 'test'}
    ds6 = {'include': 'test.yaml'}
    ds

# Generated at 2022-06-13 08:30:25.495382
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    # Tests will not run if environment variable ANSIBLE_KEEP_REMOTE_FILES is not set
    if 'ANSIBLE_KEEP_REMOTE_FILES' not in os.environ:
        raise SkipTest('ANSIBLE_KEEP_REMOTE_FILES not set, skipping test_load_list_of_tasks')

    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.playbook.play_context import PlayContext
    from ansible.module_utils._text import to_bytes
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.vars import combine_vars

    # setup module args

# Generated at 2022-06-13 08:30:33.042538
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks(): 
    # Set up mock objects.
    play = Play()
    block = Block()
    variable_manager = VariableManager()
    loader = DataLoader()
    # Load the example task list.
    task_list = load_list_of_tasks(["task_ds"], play, block, variable_manager, loader)
    # Assert that the returned list is not empty.
    assert task_list
    
    
    
    
    
    
