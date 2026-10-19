

# Generated at 2022-06-13 08:21:07.504177
# Unit test for function load_list_of_roles
def test_load_list_of_roles():
    from units.mock.loader import DictDataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.plugins.loader import add_all_plugin_dirs

    add_all_plugin_dirs()
    inventory = InventoryManager(loader=DictDataLoader({'localhost': {}}), sources=[])
    var_manager = VariableManager(loader=DictDataLoader({}), inventory=inventory)

# Generated at 2022-06-13 08:21:16.037422
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    # Example of a list of mixed tasks and blocks
    example_ds = [
        {'name': 'first_task'},
        {'block': [{'name': 'some_block'}, {'name': 'some_other_block'}]},
        {'name': 'last_task'},
    ]
    task_list = load_list_of_tasks(example_ds, None)
    assert len(task_list) == 5

    # Example of a list of block with the first block including a task

# Generated at 2022-06-13 08:21:27.545179
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    test_yaml = """---
- name: foo
  loop:
    - item1
    - item2
  debug:
    msg: "{{ item }}"
- debug:
    msg: "bar"
- name: baz
  include_tasks:
    foo.yml
"""
    test_data = yaml.safe_load(test_yaml)
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.plugins.loader import action_loader
    from ansible.plugins.loader import callback_loader
    from ansible.plugins.loader import connection_loader


# Generated at 2022-06-13 08:21:28.186216
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    pass

# Generated at 2022-06-13 08:21:35.686164
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.handler_task_include import HandlerTaskInclude
    from ansible.playbook.block import Block
    from ansible.playbook.handler import Handler
    from ansible.playbook.play import Play
    from ansible.playbook.role import Role
    from ansible.playbook.play_context import PlayContext
    from ansible.parsing.vault import JsonVaultEncryptedUnicode
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.errors import AnsibleParserError
    from ansible.executor.task_queue_manager import TaskQueueManager

# Generated at 2022-06-13 08:21:40.655260
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    import ansible.constants as C
    ansible.constants.HOST_KEY_CHECKING = False
    #from ansible import constants
    #from ansible.plugins import module_loader
    #constants.HOST_KEY_CHECKING = False
    #module_loader.add_directory('./plugins/modules')
    #module_loader.add_directory('./plugins/action')


# Generated at 2022-06-13 08:21:52.214158
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    import json
    import tempfile
    import shutil
    from ansible.module_utils.six import StringIO
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.playbook.playbook import Playbook
    from ansible.playbook.playbook_include import PlaybookInclude
    from ansible.utils.sentinel import Sentinel
    from ansible.template import Templar
    from ansible.plugins.loader import action_loader
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.utils.vars import combine_vars


# Generated at 2022-06-13 08:22:01.519254
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    # 1. test a list of tasks
    # 2. test a list of includes
    # 3. test a list of imports
    # 4. test a list of roles
    # 4. test nested tasks
    # 5. test nested imports
    # 6. test nested imports with a loop
    ds_list = [{
        'name': 'test',
        'tags': ['test'],
        'action': 'shell',
        'args': 'ls'
    }]
    task_list = load_list_of_tasks(ds_list)
    assert len(task_list) == 1

    ds_list = [{
        'include': 'role.yml',
        'loop': [{'name': 'joe'}, {'name': 'jane'}]
    }]
    task_list = load_

# Generated at 2022-06-13 08:22:15.194052
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():

    import ansible.plugins.loader as plugin_loader
    import ansible.utils.context_objects as context_objects

    plugin_loader.add_directory(os.path.join(os.path.dirname(__file__), 'action_plugins'))

    # AnsibleModule is essentially a fake task in order to test load_list_of_tasks
    class AnsibleModule():

        def __init__(self, argument_spec, supports_check_mode=False):
            self.argument_spec = argument_spec
            self.supports_check_mode = supports_check_mode

    class FakeCallbacks(object):

        def on_any(self, *args, **kwargs):
            pass

    context_objects._CALLBACK_PLUGINS = FakeCallbacks()


# Generated at 2022-06-13 08:22:26.841588
# Unit test for function load_list_of_tasks

# Generated at 2022-06-13 08:22:54.086560
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    test_file_path = TEST_DIR + '/load_list_of_tasks.yml'
    with open(test_file_path, "r") as yaml_file:
        ds = yaml.safe_load_all(yaml_file)
    # I didn't find a way to get the iterator object of the yaml file
    # I have to iterate through the yaml file before testing
    for i in range(6):
        ds.__next__()
    task_list = load_list_of_tasks(ds, None, None, None, None, False)
    # <ansible.playbook.task.Task object at 0x7f99c8eb7d30>
    assert(type(task_list[0]) == Task)
    # <ansible.playbook.task_include.Task

# Generated at 2022-06-13 08:23:04.308740
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.play import Play
    from ansible.playbook.role_include import IncludeRole
    from ansible.playbook.task import Task
    pb = dict()
    pb['name'] = "test playbook"
    pb['hosts'] = 'localhost'
    pb['connection'] = 'local'
    pb['gather_facts'] = 'no'
    p = Play().load(pb, variable_manager=None, loader=None)
    t = dict()
    t['name'] = "get the time"
    t['local_action'] = 'command date'
    tasks = load_list_of_tasks(ds=[t], play=p, block=None, role=None, task_include=None, use_handlers=False, variable_manager=None, loader=None)
   

# Generated at 2022-06-13 08:23:15.428984
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    import_role = {'import_role': {'name': 'test'}}
    test_task = {'name': 'test', 'action': {'module': 'test'}}
    def test_load_list_of_tasks_import():
        loader = DictDataLoader({
            'tasks/main.yml': '- include_tasks: test.yml'})
        variable_manager = VariableManager()
        variable_manager.extra_vars = load_extra_vars({'test': True})
        variable_manager.options_vars = {'refresh_inventory': False}
        variable_manager.options_vars['connection'] = 'local'
        variable_manager.options_vars['defaults_file'] = './test/unit/vars/test_variables.yaml'
        variable_

# Generated at 2022-06-13 08:23:19.804781
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    p=Play()
    b=Block()
    p.load(b)
    t=Task()
    b.load(t)
    t1=Task()
    b.load(t1)

# Generated at 2022-06-13 08:23:27.212379
# Unit test for function load_list_of_roles
def test_load_list_of_roles():
    from ansible.parsing.yaml.objects import AnsibleSequence

    from ansible.playbook import Play
    from ansible.playbook.role.include import RoleInclude

    class FakeLoader(object):
        pass

    ds = AnsibleSequence([{'name': 'test', 'foo': 'bar'}])
    loader = FakeLoader()
    play = Play()
    assert isinstance(load_list_of_roles(ds, play, loader=loader)[0], RoleInclude)

# Generated at 2022-06-13 08:23:38.337447
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook import Play
    # we import here to prevent a circular dependency with imports
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.role_include import IncludeRole
    from ansible.playbook.handler_task_include import HandlerTaskInclude
    from ansible.template import Templar

    # there is a checksum check that happens in this method and it requires utf-8
    # we reload to get the default
    reload(sys)

    # test a basic task list
    tasks = [
        {'debug': {'msg': 'hello world'}},
        {'debug': {'msg': 'goodbye world'}}
    ]

# Generated at 2022-06-13 08:23:46.111030
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    assert isinstance(load_list_of_tasks([]), list)
    assert isinstance(load_list_of_tasks([{'include': 'test.yml'}])[0], TaskInclude)
    assert isinstance(load_list_of_tasks([{'import_playbook': 'test.yml'}])[0], TaskInclude)
    assert isinstance(load_list_of_tasks([{'include_tasks': 'test.yml'}])[0], TaskInclude)
    assert isinstance(load_list_of_tasks([{'import_tasks': 'test.yml'}])[0], TaskInclude)



# Generated at 2022-06-13 08:23:52.489711
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    task = {'include': 'test.yaml',
            'loop': '{{loop}}'}
    task_list = load_list_of_tasks([task], None, None, None, False, None, None)
    assert len(task_list) == 1
    assert isinstance(task_list[0], TaskInclude)
    assert task_list[0].loop.get('name') == '{{loop}}'



# Generated at 2022-06-13 08:24:05.343329
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    play_context = PlayContext()
    variable_manager = VariableManager()
    loader = DataLoader()
    tasks = [
        {'connection': 'local'},
        {'include': 'test.yml'},
        {'import_role': 'test'},
        {'import_tasks': 'test.yml'},
        {'include_role': 'test'},
        {'include_tasks': 'test.yml'},
        {'role_name': 'test'}
    ]
    play = Play()
    load_list_of_tasks(tasks, play, variable_manager=variable_manager, loader=loader)

# Generated at 2022-06-13 08:24:12.829782
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    variable_manager = VariableManager()
    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, sources='localhost,')
    variable_manager.set_inventory(inventory)

# Generated at 2022-06-13 08:24:39.101275
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
  '''
  Load empty list of tasks
  '''
  from ansible.playbook.task import Task
  from ansible.playbook.block import Block
  from ansible.playbook.task_include import TaskInclude
  from ansible.playbook.play_context import PlayContext
  from ansible.playbook.variable_manager import VariableManager
  from ansible.vars.manager import VariableManager
  from ansible.vars.reserved import Reserved
  from ansible.inventory.manager import InventoryManager
  from ansible.parsing.dataloader import DataLoader
  from ansible.module_utils.common.collections import ImmutableDict
  from ansible.utils.display import Display
  from ansible.executor.task_queue_manager import TaskQueueManager

# Generated at 2022-06-13 08:24:39.841890
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    pass

# Generated at 2022-06-13 08:24:48.982912
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.parsing.yaml.objects import AnsibleMapping
    from ansible.parsing.yaml.dumper import AnsibleDumper
    from ansible.utils import context_objects as co
    from ansible.plugins.loader import role_loader

    c = co.GlobalCLIArgs()
    c.verbosity = 5
    v = co.GlobalVariables()
    l = co.GlobalLoader()
    r = co.GlobalRole()

    # Test load_list_of_tasks
    # test input
    ds = [{'block': [{'include_tasks': 'test1'}]}, {'block': [{'include_tasks': 'test2'}, {'include_tasks': 'test3'}]}]
    # output

# Generated at 2022-06-13 08:25:03.644505
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.role_include import IncludeRole
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.task import Task

    # test Task
    task_ds = {
        'action': 'run_molecule'
    }
    task_list = load_list_of_tasks([task_ds], None, None, None, None, False, None, None)
    assert len(task_list) == 1
    assert task_list[0].__class__ == Task

    # test TaskInclude
    include_ds = {
        'name': 'run_molecule',
        'include': 'molecule_common'
    }

# Generated at 2022-06-13 08:25:04.448713
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    assert 0

# Generated at 2022-06-13 08:25:14.766887
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    test_data = dict(
        action='myaction',
        otherkey=['somevalue', 'someothervalue'],
        delegate_to='localhost',
        until=dict(failed_when='True'),
        retries=3,
        retry_delay=30,
    )
    tasklist = load_list_of_tasks([test_data], play=None, block=None, role=None, task_include=None, use_handlers=False, variable_manager=None, loader=None)
    assert len(tasklist) == 1

# Generated at 2022-06-13 08:25:17.447417
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    '''
    Test module function load_list_of_tasks
    '''
    pass



# Generated at 2022-06-13 08:25:20.771413
# Unit test for function load_list_of_roles
def test_load_list_of_roles():
    '''
    Unit test for function load_list_of_roles
    :return:
    '''
    pass #TODO



# Generated at 2022-06-13 08:25:27.051169
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    fake_loader = DictDataLoader({
        'roles/somerole/tasks/main.yml': """
        - name: task 1
          action: test
          register: test_var
        - include: included.yml
        - name: task 3
          action: test
          when: not test_var.rc
        """,
        'roles/somerole/tasks/included.yml': """- name: included task 3
  action: test
  register: test_var
"""
        })

    fake_variable_manager=MagicMock()


# Generated at 2022-06-13 08:25:31.879822
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    # test_ds is a yaml list of yaml task dictionaries
    test_ds = [
        {'debug': {'msg': 'Hello'}},
        {'debug': {'msg': 'Goodbye'}}
    ]
    # initialize a fake play
    play = Play()
    # call function
    task_list = load_list_of_tasks(test_ds, play)
    # assert that task_list is a list
    assert isinstance(task_list, list)
    # assert that there are two tasks in the task_list
    assert len(task_list) == 2
    # assert that each item in task_list is an ansible.playbook.task.Task object
    assert isinstance(task_list[0], Task)
    assert isinstance(task_list[1], Task)
    # assert that

# Generated at 2022-06-13 08:25:56.957549
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    # It needs a Play
    #   - Play needs an inventory
    #   - Play needs a variable_manager
    #       - variable_manager needs a loader
    #   - Play needs a loader
    #   - Play needs a variable_manager
    #       - variable_manager needs a host_variable_manager
    #       - variable_manager needs a play_variable_manager

    # host_variable_manager just needs an inventory
    # play_variable_manager needs a loader

    #make a fake inventory
    inventory = InventoryManager.construct_inventory(hosts=[None])

    # make a fake loader
    loader = DataLoader()

    host_variable_manager = HostVariableManager(loader=loader, inventory=inventory)
    inventory.set_variable_manager(host_variable_manager)

    # make a play variable manager

# Generated at 2022-06-13 08:26:04.830147
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    task_ds = [{'name': 'echo boo'}]
    play = {}
    task_list = load_list_of_tasks(ds=task_ds, play=play, block=None, role=None, task_include=None, use_handlers=False, variable_manager=None, loader=None)
    # print('task_list', task_list)
    assert task_list
    assert len(task_list) == 1
    # import ipdb; ipdb.set_trace()
    assert task_list[0].name == 'echo boo'

# Generated at 2022-06-13 08:26:15.502765
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    # Testing
    import ansible
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.cli import CLI

    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager

    from ansible.utils.sentinel import Sentinel
    import json

    # CLI dummy
    cli = CLI(args=['1'])
    cli.options.tags = ['all']
    cli.options.listtags = None
    cli.options.listtasks = None
    cli.options.listhosts = None

# Generated at 2022-06-13 08:26:29.820032
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.vars.hostvars import HostVars

    loader = DictDataLoader({})
    variable_manager = VariableManager(loader=loader)
    hostvars = HostVars(loader=loader, variables=variable_manager)
    inventory = FakeInventory(loader=loader, variables=variable_manager, hostvars=hostvars)
    play_context = PlayContext(variable_manager=variable_manager)
    play = Play()
    play._included_file = dict(path='/foo', name='main.yml')
    play._role_names = dict()
    play._variable_manager = variable_manager
    play.name = 'test play'
    display = Display()
    import os

# Generated at 2022-06-13 08:26:31.102224
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    assert True

# Generated at 2022-06-13 08:26:32.490518
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    # FIXME
    pass


# Generated at 2022-06-13 08:26:43.414080
# Unit test for function load_list_of_blocks
def test_load_list_of_blocks():
    """Verify a list of blocks are created from a list"""
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.role_include import IncludeRole
    from ansible.playbook.role import Role
    from ansible.playbook.role_dependency import RoleDependency
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, variable_manager=variable_manager, host_list=C.DEFAULT_HOST_LIST)
    variable_manager.set_inventory(inventory)


# Generated at 2022-06-13 08:26:52.675327
# Unit test for function load_list_of_blocks
def test_load_list_of_blocks():
    from ansible.vars import VariableManager
    from ansible.playbook import Play, PlayContext
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.vars import combine_vars

    loader = DataLoader()
    variable_manager = VariableManager()

# Generated at 2022-06-13 08:27:04.820866
# Unit test for function load_list_of_blocks
def test_load_list_of_blocks():
    import ansible.playbook.block
    import ansible.playbook.task
    import ansible.playbook.role.task_include
    import ansible.playbook.role

    ansible.playbook.block.Block = FakeBlock

    import ansible.playbook.play
    import ansible.playbook.role
    from ansible.vars.manager import VariableManager

    vars_manager = VariableManager()
    role = ansible.playbook.role.Role()

    ds = [{'task': 'fake'}, {'task': 'fake_2'}]


# Generated at 2022-06-13 08:27:11.315765
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.plugins.loader import module_loader
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.role_include import IncludeRole
    from ansible.playbook.role import Role

    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager

    from ansible.playbook.play import Play
    from ansible.playbook.playbook import Playbook
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager


# Generated at 2022-06-13 08:27:46.532887
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    ds = [
        {
            'name': 'List of tasks',
            'block': {
                'name': 'List of tasks',
                'rescue': [],
                'always': [],
                'ignore_errors': False,
                'block': [
                    {'name': 'One task'},
                    {'name': 'Another task'}
                ]
            },
            'rescue': [],
            'always': [],
            'ignore_errors': False
        },
        {'name': 'A task'}
    ]
    assert load_list_of_tasks(ds, None, None, None, None) == ds
# end of function test_load_list_of_tasks



# Generated at 2022-06-13 08:27:55.441429
# Unit test for function load_list_of_roles
def test_load_list_of_roles():
    test_playbook = '''
    - hosts: localhost
      connection: local
      gather_facts: false
      vars:
        foo: bar
      roles:
        - { role: foo }
    '''
    display.verbosity = 3
    playbook = Playbook.load(test_playbook, variable_manager=VariableManager(), loader=DataLoader())
    assert len(playbook.get_plays()) == 1
    play = playbook.get_plays()[0]
    assert len(play.get_roles()) == 1
    assert play.get_roles()[0].get_name() == 'foo'
    assert play.get_roles()[0]._role_path == 'foo'
    assert play.get_roles()[0].get_variable_manager() == play.get_variable_manager()


# Generated at 2022-06-13 08:27:58.499679
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    task_list = ['task_1','task_2']
    output = load_list_of_tasks(task_list, None, None, None, None)

    assert output == task_list
    assert type(output) == type(task_list)

# Generated at 2022-06-13 08:28:11.122142
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.play import Play
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.import_role import IncludeRole
    from ansible.vars.manager import VariableManager

    loader_mock = MagicMock()
    loader_mock.get_basedir.return_value = "/home/mock_user/project/tests/mock_path"
    loader_mock.path_dwim.return_value = "/home/mock_user/project/tests/mock_path/mock_include.yml"
    loader_mock.path_dwim_relative.return_value = "/home/mock_user/project/tests/mock_path/project/mock_include_relative.yml"

    variable_manager = VariableManager()



# Generated at 2022-06-13 08:28:25.191358
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    '''
    Unit test for function load_list_of_tasks
    :return: True if successful, otherwise False
    '''
    fake_ansible_module = collections.namedtuple('AnsibleModule', ['params'])

    fake_module_args = dict(
        name='Test Name',
        state='present',
        repositories=dict(
            repo1='http://repo1.com'
        )
    )

    fake_ansible_module.params = fake_module_args

    fake_loader = DictDataLoader({})

    fake_variable_manager = collections.namedtuple('VariableManager', ['get_vars'])

    def stdout_mocked(*args, **kwargs):
        print(args)

    fake_variable_manager.get_vars = stdout_mocked

    fake_

# Generated at 2022-06-13 08:28:36.599878
# Unit test for function load_list_of_blocks
def test_load_list_of_blocks():
    from ansible.playbook.block import Block
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    class Play:
        pass


# Generated at 2022-06-13 08:28:47.339030
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from unittest.mock import Mock
    
    task_ds = [
        {
            # Implicit block
            'debug': 'msg="I am implicit block task"'
        },
        {
            'block': [
                {
                    # Implicit block
                    'debug': 'msg="I am implicit block task"'
                },
                {
                    # Implicit block
                    'debug': 'msg="I am implicit block task"'
                },
            ]
        },
        {
            # Implicit block
            'debug': 'msg="I am implicit block task"'
        }
    ]
    
    play = Mock()
    block = Mock()
    role = Mock()
    task_include = Mock()
    use_handlers = False
    variable_manager = Mock()
    loader = Mock()
    

# Generated at 2022-06-13 08:28:49.453022
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    print(load_list_of_tasks('', ''))

test_load_list_of_tasks()

# Generated at 2022-06-13 08:28:50.128531
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    pass

# Generated at 2022-06-13 08:29:01.632958
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    # we need the top level parser to make Registry objects, which
    # the Task objects will use in their tests. We'll create a fake
    # one that just gives us an emtpy set of parsers
    parser = PlaybookParser(loader=DictDataLoader({}))

    # we only need to load ansible to get our constants
    C._load_constants()

    # now create our fake variable manager
    variable_manager = VariableManager()

    # fake loader, to use

# Generated at 2022-06-13 08:29:51.236933
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    #  Check when ds is a list
    ds = ['test']
    play = 'play'
    block = 'block'
    role = 'role'
    task_include = 'task_include'
    use_handlers = 'use_handler'
    variable_manager = 'variable_manager'
    loader = 'loader'
    try:
        load_list_of_tasks(ds, play, block=block, role=role, task_include=task_include, use_handlers=use_handlers, variable_manager=variable_manager, loader=loader)
    except AnsibleAssertionError:
        pass

    #  Check when ds is not a list
    ds = 'test'

# Generated at 2022-06-13 08:30:01.379486
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.role_include import IncludeRole
    from ansible.playbook.handler_task_include import HandlerTaskInclude


# Generated at 2022-06-13 08:30:12.259379
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():

    # import here to prevent circular problems
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.template import Templar

    ds_1 = dict(action='name', args=dict(a=1, b=2))
    ds_2 = dict(action='name2', args=dict(a=1, b=2))
    ds_3 = dict(block=dict(name='foo', tasks=[dict(action='name3', args=dict(a=1, b=2))]))
    ds = [ds_1, ds_2, ds_3]

    loader = DictDataLoader({})

    def find_vars_files(basedir, **kwargs):
        pass



# Generated at 2022-06-13 08:30:21.918904
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    ds = [{
        'action': 'include_tasks',
        'static': True,
        'tags': ['include-task'],
        '_raw_params': '../tasks/task2.yml'
    }]
    play = None
    block = None
    role = None
    task_include = None
    use_handlers = False
    variable_manager = None
    loader = None
    load_list_of_tasks(ds, play, block, role, task_include, use_handlers, variable_manager, loader)



# Generated at 2022-06-13 08:30:24.805192
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    assert callable(load_list_of_tasks)

# Test import of include_role

# Generated at 2022-06-13 08:30:39.649426
# Unit test for function load_list_of_blocks
def test_load_list_of_blocks():
    from ansible.playbook import Play
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.vars.manager import VariableManager
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText
    from ansible.inventory.manager import InventoryManager
    from ansible.executor.task_queue_manager import TaskQueueManager

    results = []
    results.append({'host': 'fakehost', 'unreachable': False, 'msg': 'fakehost'})
    results.append({'host': 'fakehost2', 'unreachable': False, 'msg': 'fakehost2'})
    results.append({'host': 'fakehost3', 'unreachable': False, 'msg': 'fakehost3'})