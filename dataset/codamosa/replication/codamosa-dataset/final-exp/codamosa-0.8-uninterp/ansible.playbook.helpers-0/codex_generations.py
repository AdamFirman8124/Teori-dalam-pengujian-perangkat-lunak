

# Generated at 2022-06-13 08:21:27.950252
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    # Create temporary directory to store file
    tmp_dir = tempfile.mkdtemp()
    tmp_file = tmp_dir + '/include.yml'
    print("Temp dir:" + tmp_dir)
    print("Temp file:" + tmp_file)
    # Write the include file
    with open(tmp_file, 'w') as f:
        f.write("""---
- hosts: all
  tasks:
  - include: include2.yml
        """)
    # Write the include file
    with open(tmp_dir + "/include2.yml", 'w') as f:
        f.write("""---
- hosts: all
  tasks:
  - debug:
      msg: hello
        """)
    inventory = InventoryManager(loader=DataLoader())

# Generated at 2022-06-13 08:21:35.537936
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    # Set up a fake configuration environment
    class Options:
        module_path = None
        fact_path = None
        forks = 32
        become = True
        become_method = None
        become_user = None
        check = True
        connection_user = None
        diff = False
        vault_password_files = None
        verbose = True
        roles_path = None

    cfg = C()
    cfg.DEFAULT_MODULE_PATH = './module'
    cfg.DEFAULT_ROLES_PATH = './role'
    cfg.DEFAULT_ROLES_PATH = './playbook/playbook'

    cfg.DEFAULT_PRIVATE_ROLE_VARS_PATH = './playbook/playbook/vars'


    class Taskds():
        pass

    taskds

# Generated at 2022-06-13 08:21:44.586412
# Unit test for function load_list_of_roles
def test_load_list_of_roles():
    from ansible.playbook.play import Play

    play = Play.load({'name': 'TEST', 'hosts': 'all'})

    role_list = load_list_of_roles([{'name': 'test', 'foo': 'bar'}, {'name': 'test2'}], play)
    assert len(role_list) == 2
    assert isinstance(role_list[0], RoleInclude)
    assert isinstance(role_list[1], RoleInclude)
    assert role_list[0].name == 'test'
    assert role_list[0]._role_params == {'name': 'test', 'foo': 'bar'}
    assert role_list[1].name == 'test2'

# Generated at 2022-06-13 08:21:53.982251
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.handler import Handler
    from ansible.template import Templar
    from ansible.plugins.loader import action_loader
    #Dummy class to return action instance, since action is imported in function
    class TestAction():
        def __init__(self):
            self._load_name = 'test'
    hostvars = {}
    variable_manager = VariableManager(loader=None, inventory=None, version_info=AnsibleInfo(gitinfo=None, ansible_version='2.7.13'), extra_vars={}, options=None)
    variable_manager._extra_vars = hostvars
    variable_manager._hostvars = hostvars
    variable_manager._options = Options

# Generated at 2022-06-13 08:22:01.281588
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.task import Task
    ds = [{'debug': {'msg': 'foo'}}, {'debug': {'msg': 'bar'}}]
    task_list = load_list_of_tasks(ds=ds, play=None, block=None, role=None, task_include=None, use_handlers=False, variable_manager=None, loader=None)
    assert(len(task_list)==2)
    for i in task_list:
        assert(isinstance(i, Task))


# Generated at 2022-06-13 08:22:16.131792
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    class DummyTask(object):
        def __init__(self, args):
            self.args = args
        def __getitem__(self, key):
            return self.args[key]
        def __setitem__(self, key, val):
            self.args[key] = val
    class DummyBlock(Block):
        def __init__(self, block):
            self._block = block
        def get_vars(self):
            return {}
        def get_block_list(self, variable_manager=None, loader=None):
            return self._block, None
        def dump(self):
            return ''
        def _load_module_data(self, ds):
            pass

# Generated at 2022-06-13 08:22:25.647445
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    '''
    Function to test pre- and post-conditions of the load_list_of_tasks() function.
    '''
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude

    task_list = []
    ds = [{'role': 'nop_role'}]

    for task_ds in ds:
        if 'block' in task_ds:
            t = Block.load(task_ds)
            task_list.append(t)
        else:
            t = TaskInclude.load(task_ds)

    assert(True)


# Generated at 2022-06-13 08:22:33.613000
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    assert load_list_of_tasks(list(), None, None, None, None, None, None) == list()
    assert load_list_of_tasks(list(dict()), None, None, None, None, None, None) == list()
    assert load_list_of_tasks(list(dict(block=dict())), None, None, None, None, None, None) == list()

# Generated at 2022-06-13 08:22:39.234253
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():

    d1={'block': [{'when': 'ansible_distribution == "CentOS"'}]}

    d2={'block': [{'when': 'ansible_distribution == "CentOS"'}]}

    d3={'name': 'Install NTP', 'action': {'module': 'yum', 'name': 'ntp', 'state': 'present'}}

    d4={'block': [{'when': 'ansible_distribution == "CentOS"'}]}

    test_list=[d1, d2, d3, d4]

    assert True == True

# Generated at 2022-06-13 08:22:50.593649
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.playbook.play import Play
    from ansible.executor.playbook_executor import PlaybookExecutor

    #from ansible.playbook.play import Play
    #from ansible.playbook.block import Block
    #from ansible.playbook.task import Task
    #from ansible.playbook.handler import Handler
    #from ansible.playbook.role import Role

    #from ansible.plugins.loader import add_all_plugin_dirs
    #from ansible.parsing.dataloader import DataLoader
    #

# Generated at 2022-06-13 08:23:15.722125
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    assert load_list_of_tasks([], None, None, None, None, False, None, None) == []

    assert load_list_of_tasks([{'block': [{'block': []}]}], None, None, None, None, False, None, None) == [Block]

    assert load_list_of_tasks([{}], None, None, None, None, False, None, None) == [Task]

    assert load_list_of_tasks([{'include': {}}], None, None, None, None, False, None, None) == [TaskInclude]

    assert load_list_of_tasks([{'include_role': {}}], None, None, None, None, False, None, None) == [IncludeRole]


# Generated at 2022-06-13 08:23:16.675636
# Unit test for function load_list_of_blocks
def test_load_list_of_blocks():
    pass



# Generated at 2022-06-13 08:23:29.214798
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():

    from ansible.playbook.block import Block
    from ansible.playbook.handler import Handler
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.role_include import IncludeRole
    from ansible.playbook.handler_task_include import HandlerTaskInclude
    from ansible.playbook.task import Task
    from ansible.vars.manager import VariableManager

    # we import here to prevent a circular dependency with imports
    from ansible.playbook.play_context import PlayContext

    loader = DictDataLoader({
        "hello": """
            - name: this is a task
            - debug:
                msg: Hello World!"""
        })
    variable_manager = VariableManager()
    play_context = PlayContext()
    play_context.new_stdin = "test"


# Generated at 2022-06-13 08:23:30.445264
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    # FIXME: write this
    assert False

# Generated at 2022-06-13 08:23:39.848394
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.vars import combine_vars
    
    loader = DataLoader()
    # IF NOT SET, many function will get this error:
    # ERROR! The field 'connection' has an invalid value, which includes an undefined variable. The error was: 'dict object' has no attribute 'local'

    group_vars = {}
    host_vars = {}
    inventory = InventoryManager(loader=loader, sources=['localhost'])

    # FIXME: are these enough?

# Generated at 2022-06-13 08:23:41.259248
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    # TODO: mock datastructures to test
    pass


# Generated at 2022-06-13 08:23:47.239352
# Unit test for function load_list_of_blocks
def test_load_list_of_blocks():
    from ansible.playbook.task import Task
    from ansible.playbook.role import Role
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.vars.manager import VariableManager

    ds = [
        {'include': 'test.yaml'},
        {'include': 'test2.yaml'},
        {'block': [{'include': 'test3.yaml'}, {'include': 'test4.yaml'}]},
        {'include': 'test5.yaml'},
        {'include': 'test6.yaml'},
        {'block': [{'include': 'test7.yaml'}]},
        {'include': 'test8.yaml'},
    ]

    play = Play()
    play

# Generated at 2022-06-13 08:23:57.274824
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.block import Block
    from ansible.playbook.handler import Handler
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.role_include import IncludeRole
    from ansible.playbook.handler_task_include import HandlerTaskInclude
    from ansible.template import Templar

    task_list = []
    task_ds = {}
    play = None
    block = None
    role = None
    task_include = None
    use_handlers = False
    variable_manager = None
    loader = None

    #test for block

# Generated at 2022-06-13 08:23:57.946944
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    pass



# Generated at 2022-06-13 08:23:59.703955
# Unit test for function load_list_of_roles
def test_load_list_of_roles():
    pass
########################
# end - load_list_of_roles



# Generated at 2022-06-13 08:24:20.853538
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():

    ds = [
        {
            'block': [
                {
                    'debug': {'msg': 'This is a block'}
                }
            ]
        },
        {
            'debug': {'msg': 'This is an implicit block'}
        },
        {
            'debug': {'msg': 'This is an implicit block'}
        },
        {
            'block': [
                {
                    'debug': {'msg': 'This is a block'}
                }
            ]
        },
        {
            'block': [
                {
                    'debug': {'msg': 'This is a block'}
                }
            ]
        },
    ]

    class DummyVarsManager(object):
        def get_vars(self, play=None, task=None):
            return dict()

# Generated at 2022-06-13 08:24:24.275752
# Unit test for function load_list_of_roles
def test_load_list_of_roles():
    p = Play()
    variable_manager = VariableManager()
    loader = DataLoader()
    ds = load_list_of_roles(
        ds=None,
        play=p,
        variable_manager=variable_manager,
        loader=loader,
        collection_search_list=None,
    )
    assert ds is None



# Generated at 2022-06-13 08:24:33.586111
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    def assert_parser_exception(f, *args, **kwargs):
        with pytest.raises(AnsibleParserError, ) as excinfo:
            f(*args, **kwargs)
        return excinfo
    # Test arguments
    ds_1 = [
        {'include': 'test.yaml'},
        {'include': 'test.yaml'}
    ]
    play_1 = 'a'
    block_1 = 'b'
    role_1 = 'c'
    task_include_1 = 'd'
    use_handlers_1 = 'e'
    variable_manager_1 = 'f'
    loader_1 = 'g'
    # Test ptions

# Generated at 2022-06-13 08:24:42.458381
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    # This test is designed to check if the load_list_of_tasks
    # function correctly loads the given tasks
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task

    tasks = [
        {'host': 'host1', 'action': {'module': 'ping', 'args': ''}},
        {'host': 'host2', 'action': {'module': 'ping', 'args': ''}}
    ]
    play = Play.load(
        dict(
            name="test play",
            hosts=['127.0.0.1', '127.0.0.2'],
            gather_facts='no',
            tasks=tasks
        ),
        loader=None,
    )
    tasks = load_list_of_tasks(tasks, play)

# Generated at 2022-06-13 08:24:47.085732
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    copy_args = [{'k': 'v'}]
    task = Mock()
    task.exists.return_value = True

    with patch('ansible.executor.task_result.TaskResult') as mocked_TaskResult:
        t = load_list_of_tasks(copy_args, task)
        assert t == [mocked_TaskResult.return_value]



# Generated at 2022-06-13 08:24:48.460616
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():

    assert(False), "Test not implemented"

# Generated at 2022-06-13 08:25:00.518743
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook import Play
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block

    play = Play().load({
        'name': 'test',
        'hosts': 'all',
        'gather_facts': 'no',
        'tasks': [
            {'debug': {'msg': 'hello world'}},
            {'block': [
                {'debug': {'msg': 'inner block'}},
            ]},
            {'debug': {'msg': 'hello world again'}},
        ]
    }, variable_manager={}, loader=None)


# Generated at 2022-06-13 08:25:04.598244
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    ds_list=[{"hosts": "host1", "task1": "task1"}, {"hosts": "host2", "task2": "task2"}]
    task_list = load_list_of_tasks(ds_list)
    assert len(task_list) == 2


# Generated at 2022-06-13 08:25:14.078748
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.vars.manager import VariableManager
    import ansible.constants as C
    import ansible.utils.display as display
    from ansible.inventory.manager import InventoryManager
    from ansible.plugins.loader import action_loader
    from ansible.plugins.loader import connection_loader
    from ansible.plugins.loader import module_loader
    from ansible.inventory.host import Host
    from ansible.vars import VariableManager
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader

    # source:https://github.com/ansible/ansible/blob/devel/test/units/plugins/test_loader.py

# Generated at 2022-06-13 08:25:15.071124
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    pass

# Generated at 2022-06-13 08:25:38.962117
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    task_ds = [{'a': 'b'}]

    ansible.playbook.play.Play()

# Generated at 2022-06-13 08:25:45.474600
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    loader = DictDataLoader({})
    variable_manager = VariableManager()
    variable_manager.extra_vars = {'firstname': 'foo'}

    ds = [ {'debug': 'msg="{{ firstname }}"', 'loop': 'item in [1,2,3]'} ]
    task_list = load_list_of_tasks(ds, variable_manager=variable_manager, loader=loader)

    assert(task_list[0].args['msg'] == 'foo' and task_list[0].loop.items == [1,2,3])

# Generated at 2022-06-13 08:25:48.056367
# Unit test for function load_list_of_roles
def test_load_list_of_roles():
    # Testing for no errors during the loading of a role list
    assert load_list_of_roles(ds=None, play=None, current_role_path=None, variable_manager=None, loader=None, collection_search_list=None) == []



# Generated at 2022-06-13 08:25:58.835687
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.parsing.dataloader import DataLoader

    task_list = load_list_of_tasks([
        {
            'name': 'foo',
            'any_errors_fatal': 'yes',
            'block': [
                {
                    'name': 'inner foo',
                    'action': 'include',
                }
            ],
        }
    ],
    play=None,
    block=None,
    role=None,
    task_include=None,
    use_handlers=None,
    variable_manager=None,
    loader=DataLoader(paths=['/data']))



# Generated at 2022-06-13 08:26:07.951165
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    import os
    import json
    from io import StringIO
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.role_include import IncludeRole
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.executor.playbook_executor import PlaybookExecutor

    basedir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test_playbook_executor')

# Generated at 2022-06-13 08:26:18.805115
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    context = PlayContext()
    inventory = InventoryManager(loader=None, sources=None)

    # load_list_of_tasks([ds], play, block=None, role=None, task_include=None, use_handlers=False, variable_manager=None, loader=None)
    # ds : list of task datastructures (parsed from YAML)
    # play : play object
    # block : Block object
    # role : Role object
    # task_include : TaskInclude object
    # use_handlers : bool
    # variable_manager : VariableManager object
    # loader: DataLoader object

    # initialize a variable_manager and Data

# Generated at 2022-06-13 08:26:25.869294
# Unit test for function load_list_of_tasks

# Generated at 2022-06-13 08:26:38.694644
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.block import Block
    from ansible.playbook.role_include import IncludeRole
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.task import Task
    from ansible.playbook.handler import Handler
    from ansible.playbook.handler_task_include import HandlerTaskInclude

# Generated at 2022-06-13 08:26:49.244434
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    '''
    Test the functionality of the load_list_of_tasks function
    '''

    class FakeRole(object):
        '''
        Fake AnsibleRole object
        '''
        def __init__(self, name):
            self._role_name = name

    class FakePlay(object):
        '''
        Fake AnsiblePlay object
        '''
        def __init__(self):
            self.namespace = ''

    class FakeVarManager(object):
        '''
        Fake Ansible Variable Manager
        '''

        def __init__(self):
            self._fact_cache = {}
            self._vars_cache = {}


# Generated at 2022-06-13 08:26:55.934135
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    #Create the dummy ansible.cfg file required for these tests
    os.mkdir('./ansible')
    #Create a valid config file
    config_file_fd = open("./ansible/ansible.cfg", 'w')
    config_file_fd.write("[defaults]")
    config_file_fd.close()

    #Create a loader object
    loader = DataLoader()
    #Create a variable manager object
    variable_manager = VariableManager()
    #Create a Dummy Inventory object and add a group
    inventory = Inventory("localhost")
    group = Group("localhost")
    inventory.add_group(group)
    #Create a playbook object
    playbook = Playbook.load("./../test/test_playbook.yaml", loader=loader, variable_manager=variable_manager, inventory=inventory)
   

# Generated at 2022-06-13 08:27:53.617685
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.block import Block
    from ansible.playbook.handler import Handler
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.role_include import IncludeRole
    from ansible.playbook.handler_task_include import HandlerTaskInclude
    from ansible.template import Templar

    # test Invalid input
    # var: ds = list
    # var: play = object
    # var: block = object
    # var: role = object
    # var: task_include = object
    # var: use_handlers = bool
    # var: variable_manager = object
    # var: loader = object
    ds = []
    play = Block()
    block = Block()
    role = Block()
    task

# Generated at 2022-06-13 08:28:02.266183
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.handler import Handler
    from ansible.playbook.handler_task_include import HandlerTaskInclude

    mock_loader = DictDataLoader({
        '/etc/ansible/roles/role_include/tasks/main.yml': '',
        'role_include/tasks/main.yml': '',
        'tasks/main.yml': '',
        'foo.yml': '',
        'bar.yml': '',
    })

    mock_variable_manager = MagicMock()
    loader = DataLoader
    options = Options()

    # Basic

# Generated at 2022-06-13 08:28:07.753169
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    import sys
    import tempfile
    import textwrap
    import unittest
    from ansible.errors import AnsibleParserError
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play

    class BaseTest(unittest.TestCase):
        def setUp(self):
            self.loader = DictDataLoader({})

            # create a play and associated objects for test
            self.play = Play.load(dict(
                name='test',
                hosts='all',
                gather_facts='no',
                tasks=[],
                vars_files=None,
                vars_prompt=None,
                vars=dict(),
                roles=[]),
            variable_manager=VariableManager(), loader=self.loader)
            self.play_context = PlayContext()

   

# Generated at 2022-06-13 08:28:12.726744
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    """
    Tests if the load_list_of_tasks method returns a tasklist consisting of task1
    :return: Success if true
    """
    from ansible.playbook.play import Play
    from ansible.playbook.task_include import TaskInclude
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager

    play_ds = dict(
        name="Ansible Play",
        hosts='all',
        gather_facts='no',
        tasks=[
            dict(action=dict(module='shell', args='ls'), register='shell_out'),
            dict(action=dict(module='debug', args=dict(msg='{{shell_out.stdout}}')))
        ]
    )
    loader = DictDataLoader({})

# Generated at 2022-06-13 08:28:27.212806
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.block import Block
    from ansible.playbook.handler import Handler
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.role_include import IncludeRole
    from ansible.playbook.handler_task_include import HandlerTaskInclude
    from ansible.template import Templar

    # Test dicts passed in
    assert load_list_of_tasks({}, None, None, None) == []
    assert load_list_of_tasks([{'block': []}], None, None, None) == [Block(None, [], [], None, None)]

# Generated at 2022-06-13 08:28:33.775173
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    '''
    Test load_list_of_tasks function
    '''

    ds = [{'action': 'shell', 'args': {'_raw_params': 'echo hello'}}]
    play = dict()
    task_list = load_list_of_tasks(ds, play)
    assert len(task_list) == 1

# Generated at 2022-06-13 08:28:45.285832
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.play_context import PlayContext
    from ansible.vars import VariableManager
    from ansible.utils import context_objects as co
    from ansible.plugins.loader import callback_loader, module_loader
    from ansible.plugins.callback import CallbackBase
    from ansible.template import Templar
    co.GlobalCLIArgs._store = dict(
        connection='local', forks=10, become=False, become_method=None, become_user=None, check=False, diff=False, roles_path="./tests/unit/modules/library/", get_user_facts=False, verbosity=4, inventory="./tests/unit/inventory/hosts")
    co.GlobalCLIArgs._in_task = False

# Generated at 2022-06-13 08:28:45.865284
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    pass

# Generated at 2022-06-13 08:28:51.634837
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.play import Play
    from ansible.parsing.dataloader import DataLoader

    ds = [
        {'include': 'role1'},
        {'import_role': 'role2'},
        {'include_role': 'role3'},
    ]
    play = Play().load({
        'name': 'test',
        'hosts': 'all',
        'gather_facts': 'no',
        'tasks': ds,
    })
    variable_manager = VariableManager()
    loader = DataLoader()

    tasks = load_list_of_tasks(ds, play, variable_manager=variable_manager, loader=loader)

    assert(len(tasks) == 3)
    assert(tasks[0].static)

# Generated at 2022-06-13 08:29:02.380162
# Unit test for function load_list_of_roles
def test_load_list_of_roles():
    from ansible.plugins.loader import role_loader
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText

    pb = Playbook.load('test_playbooks/playbook_syntax_ok.yml', loader=DataLoader(), variable_manager=VariableManager())
    role_paths = role_loader._get_role_paths()
    ds1 = [{u'role': u'adjunct.datadog.datadog-agent', u'name': u'Install datadog-agent'}]