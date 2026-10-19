

# Generated at 2022-06-13 08:21:06.744335
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():

    from ansible.playbook.task import Task
    from ansible.playbook.role_include import IncludeRole
    from ansible.playbook.block import Block

    args_parser = ModuleArgsParser()
    ds = {'action': 'shell', 'args': 'echo hello'}
    try:
        (action, args, delegate_to) = args_parser.parse(skip_action_validation=True)
    except AnsibleParserError as e:
        # if the raises exception was created with obj=ds args, then it includes the detail
        # so we dont need to add it so we can just re raise.
        if e.obj:
            raise
        # But if it wasn't, we can add the yaml object now to get more detail

# Generated at 2022-06-13 08:21:15.941820
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play

    loader = DataLoader()
    inv_manager = InventoryManager(loader=loader, sources='localhost,')
    variable_manager = VariableManager(loader=loader, inventory=inv_manager)
    play = Play().load({'name': 'test_play', 'hosts': 'localhost', 'gather_facts': 'no'},
                       variable_manager=variable_manager, loader=loader)

    ds = [
        {
            'name': 'test_task'
        }
    ]


# Generated at 2022-06-13 08:21:19.434763
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    '''
    --------------------------------------------------------------------------------
    Purpose: test load_list_of_tasks()
    --------------------------------------------------------------------------------
    Parameters: none
    --------------------------------------------------------------------------------
    Returns: None
    --------------------------------------------------------------------------------
    '''
    pass


# Generated at 2022-06-13 08:21:30.133602
# Unit test for function load_list_of_roles
def test_load_list_of_roles():
    def get_variable_manager(value):
        '''This is a mock object for VariableManager.'''
        return {"foo": value}

    def get_loader(value):
        '''This is a mock object for DataLoader.'''
        return {"foo": value}

    play_object = get_play_for_load_list_of_roles()
    ds_list_of_roles = [{"role": "foo"}, {"role": "foo", "bar": "baz"}]
    get_variable_manager.ansible_version = 2.9
    get_loader.ansible_version = 2.9
    result = load_list_of_roles(ds_list_of_roles, play_object, get_variable_manager, get_loader)
    assert len(result) == 2

# Generated at 2022-06-13 08:21:41.911748
# Unit test for function load_list_of_roles
def test_load_list_of_roles():
    # Mock objects
    mock_play = mock.MagicMock()
    mock_vars = mock.MagicMock()
    mock_loader = mock.MagicMock()
    # List of roles
    ds = [{"role": "web"}, {"role": "db"}]
    # Call the function
    roles = load_list_of_roles(ds, mock_play, None, mock_vars, mock_loader)
    # Check if the call returns a list
    assert isinstance(roles, list)
    # Validate each role
    for role in roles:
        # Check the role name
        assert role.get_name() == role._role_name
        # Check if the role is a instance of RoleInclude
        assert isinstance(role, RoleInclude)
        # Check the role has default attributes

# Generated at 2022-06-13 08:21:52.256320
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    import os
    import sys
    import yaml
    # Load the playbook
    path = os.path.join(os.getcwd(), './playbook.yml')

    with open(path, 'r') as yml:
        yml_str = yml.read()
    yml_list = yaml.load(yml_str, Loader=yaml.FullLoader)
    # Load the data structure
    variable_manager = VariableManager()
    loader = DataLoader()

    # load inventory

# Generated at 2022-06-13 08:22:01.520195
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    '''
    This test case is a unit test to exercise all of the functions in
    load_list_of_tasks()
    '''

    list_of_tasks = [{'test': ['test', 'test']},
                     {'test': ['test2']}]

    # This should generate an assertion error
    try:
        load_list_of_tasks('ds', None)
        assert False
    except AnsibleAssertionError:
        assert True

    # This should generate an assertion error
    try:
        load_list_of_tasks(['ds'], None)
        assert False
    except AnsibleAssertionError:
        assert True

    # This should generate an assertion error

# Generated at 2022-06-13 08:22:06.266301
# Unit test for function load_list_of_roles
def test_load_list_of_roles():
    from ansible.playbook.play import Play
    from ansible.playbook.role.collection import RoleCollection
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.role import Role
    from ansible.playbook.role.include import RoleInclude
    from ansible.playbook.role_include import IncludeRole

    fake_loader = DictDataLoader(dict())
    fake_vars = dict(
        foo='foo',
        bar='bar',
        baz='baz',
        role_path='/tmp/doesnotexist',
        role_name='test_role',
        play_hosts=['localhost', 'otherhost'],
    )
    facts = dict(
        distribution='Fedora',
        version='28',
        somefact='somefact'
    )
   

# Generated at 2022-06-13 08:22:18.156233
# Unit test for function load_list_of_roles
def test_load_list_of_roles():
    '''
    load_list_of_roles function is called in load_list_of_blocks, need to patch the load_list_of_blocks
    in this test suite to test load_list_of_roles.
    :return:
    '''
    task_ds_with_role = [
         {
            'include_role': {
                'name': 'foo',
                'tasks': 'bar'
            }
        }
    ]
    task_ds_with_include_role = [
         {
            'include_role': {
                'name': 'foo',
                'tasks': 'bar'
            }
        }
    ]

    role_def_with_field = [
        {
            'name': 'foo'
        }
    ]

    role_def_with_field_and

# Generated at 2022-06-13 08:22:33.403464
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():

    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.playbook_executor import PlaybookExecutor


    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, sources=['localhost'])
    variable_manager.set_inventory(inventory)

    ds = [
            {'action': 'do', 'more': 'yep'},
            {'block': [
                    {'action': 'do', 'more': 'yep'}
                ]
            }
        ]

    task_list = load_list_of_tasks(ds, PlaybookExecutor, None, None, None, False, variable_manager, loader)



# Generated at 2022-06-13 08:23:48.282018
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    # Test Case 1
    ds = [{"block": [{"name": "Block1"}]}, {"name": "Task1"}, {"block": [{"name": "Block2"}]}]
    assert True == load_list_of_tasks(ds, None, None)
    # Test Case 2
    ds = {"block": [{"name": "Block1"}]}
    assert True == load_list_of_tasks(ds, None, None)
    # Test Case 3
    ds = {"name": "Task1"}
    assert True == load_list_of_tasks(ds, None, None)
    # Test Case 4
    ds = None
    assert True == load_list_of_tasks(ds, None, None)
    # Test Case 5
    ds = "WrongType"
    assert False == load

# Generated at 2022-06-13 08:23:57.830436
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():

    # we import here to prevent a circular dependency with imports
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude

    # Test a list of bare tasks, unparsed (implicit block)
    ds = [{'action': {'module': 'shell', 'args': 'ls -l'}},
          {'action': {'module': 'shell', 'args': 'ls -l'}}]
    task_list = load_list_of_tasks(ds, 'test_play', None, variable_manager=None, loader=None)
    assert len(task_list) == 2
    assert isinstance(task_list[0], Task)
    assert isinstance(task_list[1], Task)

# Generated at 2022-06-13 08:24:12.821438
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    ds = ['hello']
    play = None
    block = None
    role = None
    task_include = None
    use_handlers = False
    variable_manager = None
    loader = None
    result = load_list_of_tasks(ds, play, block, role, task_include, use_handlers, variable_manager, loader)
    assert isinstance(result, list)
    assert len(result) == 0
    assert isinstance(play, object)
    assert isinstance(block, object)
    assert isinstance(role, object)
    assert isinstance(task_include, object)
    assert isinstance(use_handlers, bool)
    assert isinstance(variable_manager, object)
    assert isinstance(loader, object)




# Generated at 2022-06-13 08:24:21.694489
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
	# starting with 1.8, all tasks are loaded in this order
	ds = [
		{
			'with_nested': [
				{'include': 'foofile'},
				{'shell': "echo 'included task list'"},
				{'include': 'barfile'}
			]
		},
		{'include': 'bazfile'},
		{'include': 'bizfile', 'static': True}
	]
	#assert load_list_of_tasks(ds) == expected

# Generated at 2022-06-13 08:24:32.117380
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    def test_tasks(ds, task_count, block_count):
        t_task = load_list_of_tasks(ds)
        assert(len(t_task) == task_count)
        assert(len(t_task[0].block) == block_count)

    # Case 1: list of tasks
    yaml_data = """
    - name: test1
      debug:
        msg: task 1
    - name: test1
      debug:
        msg: task 2
    - name: test1
      debug:
        msg: task 3
    """
    test_tasks(ds=yaml.load(yaml_data), task_count=3, block_count=0)

    # Case 2: list of blocks and tasks

# Generated at 2022-06-13 08:24:41.458428
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.errors import AnsibleParserError
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.role_include import IncludeRole
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.inventory.manager import InventoryManager
    import os

    loader = DataLoader()

    test_dir = os.path.dirname(os.path.realpath(__file__)) + os.sep + 'loader_fixtures'

    inventory = InventoryManager(loader=loader, sources=[test_dir + '/inventory'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)


# Generated at 2022-06-13 08:24:48.586746
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    # This is a unit test for load_list_of_tasks
    yaml_str = u'[{"include_tasks": "/etc/ansible/roles/sw_upgrade_tasks/tasks/import_cfg.yml"}, {"include_tasks": "/etc/ansible/roles/sw_upgrade_tasks/tasks/sw_upgrade.yml"}]'
    ds = yaml.load(yaml_str)

# Generated at 2022-06-13 08:24:51.152354
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    assert False, "This function cannot be tested as it has dependencies that are not loaded on test import"


# Generated at 2022-06-13 08:25:05.107189
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook import Playbook
    from ansible.playbook.role_include import IncludeRole

    task_ds = [
        {
            'include_role': {
                'name': 'name',
                'vars': {'name': 'role'},
                'static': False
            }
        }
    ]

    class Role:
        def __init__(self, name):
            self.name = name
            self.compiled_blocks = []
            self.metadata = {
                'dependencies': [],
                'collections': [],
                'status': 'stable',
            }

        def get_vars(self, include_params=True, include_files=False, use_defaults=False):
            return {'name': self.name}


# Generated at 2022-06-13 08:25:20.264980
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    def t_create_exception(msg, exception_class=None):
        if exception_class is None:
            exception_class = AnsibleAssertionError
        def t_exception(*args, **kwargs):
            raise exception_class(msg)
        return t_exception

    # exception can't be raised in mock, create a function to raise it instead
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.vars.clean import module_response_deepcopy

    module_response = module_response_deepcopy()

# Generated at 2022-06-13 08:25:46.253875
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():

    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    from ansible.utils.vars import combine_vars

    from ansible.tests.unit.mock.loader import DictDataLoader

    from ansible.plugins.loader import action_loader

    display.verbosity = 3

    inventory_manager = InventoryManager(loader=DictDataLoader({'host_list': ['localhost',]}))
    variable_manager = VariableManager(loader=DictDataLoader({}), inventory=inventory_manager, version_info=combine_vars(None, None))

    # Test with action in all include tasks
    data = [
        {'include': 'include_me.yml'},
    ]

# Generated at 2022-06-13 08:25:59.128353
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.handler_task_include import HandlerTaskInclude
    from ansible.playbook.role_include import IncludeRole
    ds = [
        dict(
            block=[]
        ),
        dict(
            action='include_tasks',
            args=dict(
                _raw_params='playbook.yaml',
            )
        ),
        dict(
            action='include_role',
            args=dict(
                _raw_params='playbook.yaml',
            )
        ),
    ]
    play = type('DummyPlayBook', (object,), {})
    dummy_role = type('DummyRole', (object,), {})

# Generated at 2022-06-13 08:26:00.429714
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    pass
# Unit test of class Base

# Generated at 2022-06-13 08:26:08.827956
# Unit test for function load_list_of_tasks

# Generated at 2022-06-13 08:26:19.352651
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.play import Play
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.task import Task
    from ansible.playbook.role_include import IncludeRole
    from ansible.playbook.handler import Handler
    from ansible.playbook.handler_task_include import HandlerTaskInclude
    from ansible.playbook.block import Block

    # Define the playbook structure

# Generated at 2022-06-13 08:26:22.790064
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    assert load_list_of_tasks(ds, play, block, role, task_include, use_handlers, variable_manager, loader)
    assert isinstance(load_list_of_tasks(ds, play, block, role, task_include, use_handlers, variable_manager, loader), list)
    

# Generated at 2022-06-13 08:26:23.411168
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    pass

# Generated at 2022-06-13 08:26:36.159533
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    # Test 1
    # Test case: Test with invalid ds
    # Test result: AnsibleAssertionError should be thrown with error message 'ds should be a list but was a str'
    ds = 'test'
    try:
        load_list_of_tasks(ds=ds)
    except AnsibleAssertionError as e:
        assert e.error == 'The ds (test) should be a list but was a str'

    # Test 2
    # Test case: Test with invalid ds
    # Test result: AnsibleAssertionError should be thrown with error message 'ds should be a dict but was a str'
    ds = ['test']

# Generated at 2022-06-13 08:26:47.112099
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.executor.playbook_executor import PlaybookExecutor

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=['/etc/ansible/hosts'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    print(variable_manager)

    pb_path = '/home/hyt/ansible/learn/ansible_learn/tasks/playbook.yml'
    pb = PlaybookExecutor(playbooks=[pb_path], inventory=inventory, variable_manager=variable_manager, loader=loader)
    pb._tqm._stdout_callback = results_callback_

# Generated at 2022-06-13 08:26:48.544597
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    # TODO: implement test_load_list_of_tasks
    pass



# Generated at 2022-06-13 08:27:43.416477
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    pass



# Generated at 2022-06-13 08:27:51.244328
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    ds = [
        {'action': 'debug', 'args':{'msg': 'test'}},
        {'block': [{'action': 'debug', 'args':{'msg': 'test'}}]}
        ]
    play = Play()
    loader = None
    variable_manager = None
    use_handlers = False
    task_list = load_list_of_tasks(ds, play, None, None, None, use_handlers, variable_manager, loader)
    assert (len(task_list) == 2)

# Generated at 2022-06-13 08:28:00.573786
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.block import Block
    from ansible.playbook.handler import Handler
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.role_include import IncludeRole
    from ansible.playbook.handler_task_include import HandlerTaskInclude
    from ansible.template import Templar

    play = mock.MagicMock()
    variable_manager=mock.MagicMock()
    loader=mock.MagicMock()

    task_list = load_list_of_tasks({'block': True}, play,role="role", task_include=None, use_handlers=True, variable_manager=variable_manager, loader=loader)
    assert len(task_list) == 1

# Generated at 2022-06-13 08:28:11.943868
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    ds = [{
        'name': '123',
        'action': 'shell',
        'register': 'r',
    }, {
        'name': '456',
        'action': 'raw',
        'register': 'r'
    }]
    play = None
    block = None
    role = None
    task_include = None
    use_handlers = False
    variable_manager = None
    loader = None
    rlt = load_list_of_tasks(ds, play, block, role, task_include, use_handlers, variable_manager, loader)

    assert len(rlt) == 2
    assert rlt[0].name == '123'
    assert rlt[0].action == 'shell'
    assert rlt[0].register == 'r'
    assert rlt[1].name

# Generated at 2022-06-13 08:28:26.354762
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    test_ds = [{'action': 'include_tasks', 'args': {'_raw_params': 'test.yml'}},
               {'action': 'command', 'args': {'_raw_params': 'rm /etc'}, 'delegate_to': 'localhost', 'register': 'r'},
               {'action': 'command', 'args': {'_raw_params': 'test'}, 'delegate_to': 'localhost', 'register': 'r'}]

    test_load_list_of_tasks = load_list_of_tasks(ds=test_ds)
    assert test_load_list_of_tasks[0].action == 'include_tasks'
    assert test_load_list_of_tasks[0].args['_raw_params'] == 'test.yml'
   

# Generated at 2022-06-13 08:28:37.063408
# Unit test for function load_list_of_blocks
def test_load_list_of_blocks():
    from ansible.playbook.block import Block
    from ansible.playbook.play import Play
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    ##############################################
    ## mock data
    ##############################################
    # ds

# Generated at 2022-06-13 08:28:44.336092
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from collections import namedtuple

    # To isolate variables
    os.environ['ANSIBLE_ROLES_PATH'] = '../../test/unit/play/roles/'

    # A dummy task
    task = namedtuple('task', ['module_name'])

    # A simple play
    play_ds = dict(
        name = 'Test Play',
        hosts = ['remote'],
        gather_facts = 'no',
        connection = 'local',
        become = 'yes',
        become_method = 'sudo',
        become_user = 'root',
        task_list = [
            dict(
                include_role = dict(
                    name = 'no_loop',
                    static = True
                )
            )
        ]
    )

    # Block object

# Generated at 2022-06-13 08:28:55.694299
# Unit test for function load_list_of_blocks
def test_load_list_of_blocks():
    import unittest
    from ansible.playbook.block import Block
    class TestPlaybookBlocks(unittest.TestCase):
        def test_load_list_of_blocks(self):
            from ansible.playbook import Playbook
            from ansible.vars import VariableManager
            from ansible.parsing.dataloader import DataLoader
            from ansible.inventory.manager import InventoryManager
            from ansible.playbook.play import Play

# Generated at 2022-06-13 08:29:04.417154
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude

    def test_load_task_loop(ds, loop_result):
        list_of_tasks = load_list_of_tasks(ds, None, None, None, None, None, None)
        assert len(list_of_tasks) == 1
        assert isinstance(list_of_tasks[0], Task)
        assert list_of_tasks[0].loop == loop_result
        assert list_of_tasks[0].loop_args == loop_result


# Generated at 2022-06-13 08:29:15.914264
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    # Local imports
    from ansible.playbook.task import Task
    from ansible.playbook.role_include import IncludeRole
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.playbook.play import Playbook
    from ansible.plugins.loader import action_loader
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.module_utils.six import string_types, text_type
    from ansible.errors import AnsibleParserError

    # Create the playbook
    loader = DataLoader()

# Generated at 2022-06-13 08:29:48.453004
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    # TODO: Implement tests for load_list_of_tasks
    pass


# Generated at 2022-06-13 08:29:55.996170
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.errors import AnsibleParserError
    ds = [
        {'action': 'include', 'params': 'foo'},
        {'action': 'include', 'params': 'foo1'},
        {'action': 'include', 'params': 'foo2'},
        {'action': 'command', 'params': 'echo "hello"'},
        {'action': 'include', 'params': 'foo3'},
    ]

    assert load_list_of_tasks(ds, None, None, None, None, False, None, None), list



# Generated at 2022-06-13 08:30:01.313534
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    # load_list_of_tasks()

    ds = [
        {"action": "included", "args": {}, "block": None, "changed_when": False, "delegate_to": "localhost", "failed_when": False, "loop": None, "name": "", "register": "", "retries": 3, "run_once": False, "until": None, "when": True},
        {"action": "included", "args": {}, "block": None, "changed_when": False, "delegate_to": "localhost", "failed_when": False, "loop": None, "name": "", "register": "", "retries": 3, "run_once": False, "until": None, "when": True},
    ]

    from ansible.playbook.task import Task


# Generated at 2022-06-13 08:30:12.176763
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    PLAYBOOK = """---
- name: test playbook
  hosts: all

  roles:
    - my_role

  tasks:
    - debug:
        msg: hello
    - include_role:
        name: my_role
        tasks_from: specific_tasks
"""
    from ansible.parsing.dataloader import DataLoader
    loader = DataLoader()
    results = loader.load(PLAYBOOK)
    assert isinstance(results, list)
    assert len(results) == 1
    assert 'name' in results[0]
    assert results[0].get('name') == "test playbook"
    assert 'tasks' in results[0]
    assert results[0]['tasks']
    assert isinstance(results[0]['tasks'], list)

# Generated at 2022-06-13 08:30:22.659971
# Unit test for function load_list_of_blocks
def test_load_list_of_blocks():
    assert load_list_of_blocks([]) == []
    assert load_list_of_blocks([
    {
        'block': [{
            'meta': 'test1'
        }],
        'tasks': []
    },
    {
        'block': [{
            'meta': 'test2'
        }],
        'tasks': []
    }
    ]) != load_list_of_blocks([{
        'block': [{
            'meta': 'test1'
        }],
        'tasks': []
    },{
        'block': [{
            'meta': 'test2'
        }],
        'tasks': []
    }])

# Generated at 2022-06-13 08:30:37.517243
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    # test with a regular task
    regular_task_1 = dict(action=dict(module='debug', args=dict()))
    regular_task_2 = dict(action=dict(module='shell', args=dict()))

    task_list = load_list_of_tasks([regular_task_1,regular_task_2])
    # two tasks loaded
    assert len(task_list) == 2

    # test with a task that has block
    task_with_block = dict(block=[dict(action=dict(module='debug', args=dict()))])

    task_list = load_list_of_tasks([task_with_block])
    # one block and one task loaded
    assert len(task_list) == 2
    assert 'block' in task_list[0]._attributes