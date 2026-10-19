

# Generated at 2022-06-13 08:21:15.742850
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    loader = DataLoader()
    variable_manager = VariableManager()
    play = Play_DS()
    role = None

    ds = {
        'hosts': 'localhost',
        'tasks': [
            {
                'name': 'test1',
                'debug': {'msg': 'This is task1'}
            },
            {
                'name': 'test2',
                'debug': {'msg': 'This is task2'}
            }
        ]
    }

    tasks = load_list_of_tasks(ds['tasks'], play, role=role, loader=loader, variable_manager=variable_manager)

    assert tasks[0].name == 'test1'
    assert tasks[1].name == 'test2'


# Generated at 2022-06-13 08:21:27.271388
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    import ansible.playbook.task
    ansible.playbook.task.Task = Mock()
    load_list_of_tasks(ds=[{'name': 'Test task 1'}, {'name': 'Test task 2'}], play=1, block=2, role=3, task_include=4, use_handlers=5, variable_manager=6, loader=7)
    assert ansible.playbook.task.Task.mock_calls == [call.load(ds={'name': 'Test task 1'}, block=2, role=3, task_include=4, variable_manager=6, loader=7), call.load(ds={'name': 'Test task 2'}, block=2, role=3, task_include=4, variable_manager=6, loader=7)]


# Generated at 2022-06-13 08:21:27.918088
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    assert True



# Generated at 2022-06-13 08:21:33.718358
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():

    ds = [{'block': [{'task': {'name': 'name'}}]}, {'task': {'name': 'name2'}}]

    play = Play()
    task_list = load_list_of_tasks(ds, play, block=None, role=None, task_include=None, use_handlers=False, variable_manager=None, loader=None)
    assert len(task_list) == 2
    assert task_list[0].get_name() == 'name'
    assert task_list[1].get_name() == 'name2'

# Generated at 2022-06-13 08:21:39.371923
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    class FakeContainer():
        pass
        
    class FakeRole():
        def __init__(self, role_path):
            self._role_path = role_path

        def get_path(self):
            return self._role_path

    class FakePlay():
        pass

    ds = [
        {
            'block': [
                {
                    'meta': {
                        'var1': 'value1'
                    }
                },
                {
                    'action': {
                        'module': 'debug',
                        'args': {
                            'msg': 'in block'
                        }
                    }
                }
            ]
        },
        {
            'action': {
                'module': 'debug',
                'args': {
                    'msg': 'after block'
                }
            }
        }
    ]



# Generated at 2022-06-13 08:21:41.913249
# Unit test for function load_list_of_blocks
def test_load_list_of_blocks():
     assert load_list_of_blocks(['task1','task2','block1','block2'], play=None) == '{}' #FIXME


# Generated at 2022-06-13 08:21:48.933479
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    # Test for comments in task list
    ds = [{'#':'Comment', 'action':{'module': 'ping','args': {}}}, {'action':{'module': 'ping','args': {}}}]
    play = Play()
    loader = DictDataLoader({})
    variable_manager = VariableManager()
    task_list = load_list_of_tasks(ds, play, None, None, None, False, variable_manager, None)
    assert isinstance(task_list, list)
    assert len(task_list) == 2
    assert task_list[0].action == 'ping'
    assert task_list[1].action == 'ping'

    # Test for empty task list
    ds = []

# Generated at 2022-06-13 08:21:59.983076
# Unit test for function load_list_of_blocks
def test_load_list_of_blocks():

    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.handler import Handler

    # test for bare task
    ds = dict(
        name="test block",
        hosts="test.com",
        connection="smart",
        gather_facts="no",
        tasks=[
            dict(action=dict(module="debug", args=dict(msg="test_msg"))),
        ]
    )

    # setup play
    play = Play()
    play.name = "test_play"
    play.hosts = "test.com"
    play.connection = "ssh"
    play.gather_facts = False
    play.vars = dict(foo='bar', bam='baz')

# Generated at 2022-06-13 08:22:03.273266
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    assert load_list_of_tasks(None, None, None, None, None, None, None, None) == []


# Generated at 2022-06-13 08:22:16.981513
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    #   test when ds is not None
    #   test when ds is None
    #   test when ds is not of type list
    #   test when an element of ds is not of type dict

    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader


    # empty list
    ds = []
    play = None
    block = None
    role = None
    task_include = None
    use_handlers = False
    variable_manager = VariableManager()
    loader = DataLoader()


# Generated at 2022-06-13 08:22:41.746922
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources='localhost,')
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    play_source = dict(
        name="Ansible Play",
        hosts='localhost',
        gather_facts='no',
        tasks=[
            dict(action=dict(module='shell', args='ls'), register='shell_out'),
            dict(action=dict(module='debug', args=dict(msg='{{shell_out.stdout}}')))
        ]
    )

# Generated at 2022-06-13 08:22:45.916123
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    ds = '''
    - name: task 1
      ping:
    '''
    print(yaml.load(ds, Loader=yaml.FullLoader))
    return



# Generated at 2022-06-13 08:22:48.079522
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    assert False, "No tests for function load_list_of_tasks"

# Generated at 2022-06-13 08:23:00.058268
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    # Test if we get a task object from the datastructure
    from ansible.plugins.action.normal import ActionModule as _ActionModule
    from ansible.plugins.action import ActionBase
    module = _ActionModule(task=MagicMock())
    module._shared_loader_obj = datastructure_loader
    task = Task()
    task._role = MagicMock()
    task.evaluate_conditional = MagicMock(return_value=True)
    task._parent = MagicMock()
    task.evaluate_tags = MagicMock(return_value=True)
    task.notify_handler = MagicMock()
    task.run = MagicMock()
    task.rescue = MagicMock()
    task.always = MagicMock()


# Generated at 2022-06-13 08:23:07.849222
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.playbook.block import Block
    
    C = AnsibleModuleBuilder(ignore_warnings=True)
    variable_manager = VariableManager()
    variable_manager.extra_vars = load_extra_vars(loader=None, options=None, variable_manager=None)
    variable_manager.options_vars = load_options_vars(loader=None, options=None, variable_manager=variable_manager)
    play_context = PlayContext()
    play_context.port = 22
    play_context.remote_addr = 'localhost'
    play_context.connection = 'ssh'
    play_context.network_os = 'linux'
    play_context.become = False
    play

# Generated at 2022-06-13 08:23:18.242195
# Unit test for function load_list_of_roles
def test_load_list_of_roles():
    import os
    import sys
    import yaml
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.plugins.loader import collection_loader

    # keep track of original paths
    orig_sys_path = sys.path

    # create a dummy plugins path in our test dir
    plugin_path = os.path.join(os.path.dirname(__file__), 'test_role_loader_plugin_path')
    if not os.path.exists(plugin_path):
        os.mkdir(plugin_path)
    # add dummy plugins dir to system path
    sys.path.append(plugin_path)

    # create a test role

# Generated at 2022-06-13 08:23:30.438677
# Unit test for function load_list_of_roles
def test_load_list_of_roles():
    from ansible.playbook.block import Block
    from ansible.playbook.role.include import RoleInclude

    fake_play = Play()
    fake_play.hosts = FakeHost()
    fake_play.hosts.get_name.return_value = 'fakehost'
    fake_play.hosts.get_vars.return_value = {'ansible_connection': 'local'}
    fake_play.hosts.get_variables.return_value = {'ansible_connection': 'local'}

    fake_variable_manager = FakeVariableManager()

    fake_loader = DictDataLoader()
    fake_loader.set_basedir('/fakebasedir')

    fake_block = Block()
    fake_block._role = FakeRole()

    fake_role = FakeRole()


# Generated at 2022-06-13 08:23:41.041365
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():

    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.role_include import IncludeRole
    from ansible.playbook.handler_task_include import HandlerTaskInclude

    # Create a list of task datastructures (parsed from YAML),
    # return a list of Task() or TaskInclude() objects.

    loader = DictDataLoader({})
    variable_manager = VariableManager(loader=loader)
    ds = [dict(block=dict(name="block", tasks=[]))]
    task_list = load_list_of_tasks(ds, None, None, None, None, False, variable_manager, loader)

# Generated at 2022-06-13 08:23:48.925613
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

    # Test1: ds should be a list
    ds = 0
    task_list = []
    try:
        task_list = load_list_of_tasks(ds, '', None, None, None, False, None, None)
    except AnsibleAssertionError as e:
        pass
    assert_equals(task_list, [])

    # Test

# Generated at 2022-06-13 08:23:58.154416
# Unit test for function load_list_of_blocks
def test_load_list_of_blocks():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.inventory.manager import InventoryManager

    test_block = {
        "block": [
            {"block": [
                {"hosts": "testhost"}
            ]}
        ]
    }

    test_listofblocks = [
        {"hosts": "testhost"},
        {"block": [
            {"hosts": "testhost"}
        ]}
    ]

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, sources=[])
    play_context = PlayContext(play=Play(), variable_manager=variable_manager, loader=loader)

# Generated at 2022-06-13 08:24:32.040476
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    debug = False
    ds = [{'action': {'module': 'shell', 'args': 'ls', 'register': 'result'}},
          {'action': {'module': 'shell', 'args': 'cat /etc/hosts', 'register': 'hosts'}},
          {'action': {'module': 'debug', 'msg': '{{ result.stdout }}'}}
          ]
    task_list = load_list_of_tasks(ds)
    if debug:
    #   for t in task_list:
    #      print(t)
        print(task_list)
    assert len(task_list) == 3



# Generated at 2022-06-13 08:24:32.747127
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    assert True

# Generated at 2022-06-13 08:24:41.899731
# Unit test for function load_list_of_tasks

# Generated at 2022-06-13 08:24:42.849107
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    assert callable(load_list_of_tasks)

# Generated at 2022-06-13 08:24:58.093772
# Unit test for function load_list_of_blocks
def test_load_list_of_blocks():
    # https://github.com/ansible/ansible/pull/26015
    import sys
    if sys.version_info >= (2, 7):
        from ansible.playbook.handler import Handler

        from ansible.playbook.block import Block
        from ansible.playbook.role_block import RoleBlock
        from ansible.playbook.task_include import TaskInclude
        from ansible.playbook.task import Task
        from ansible.playbook.role import Role

        from ansible.playbook.play_context import PlayContext
        from ansible.playbook.play import Play

        import ansible.playbook.play
        import ansible.playbook.block
        import ansible.parsing.mod_args

        import ansible.inventory.manager
        from ansible.inventory.group import Group

# Generated at 2022-06-13 08:25:00.452374
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    pass
###############################################################################
# END
###############################################################################

# Generated at 2022-06-13 08:25:00.859363
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    pass

# Generated at 2022-06-13 08:25:10.928407
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    import tempfile, shutil, os

    file_name = 'load_list_of_tasks'
    # Write out a tempfile that we can then read back in
    fd, temp_path = tempfile.mkstemp(prefix=file_name)

# Generated at 2022-06-13 08:25:13.252050
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    assert callable(load_list_of_tasks)




# Generated at 2022-06-13 08:25:20.739432
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    from ansible.playbook.play import Play
    from ansible.playbook.task import Task, TaskInclude
    from ansible.playbook.block import Block

    test_dir_path = os.path.dirname(os.path.realpath(__file__))

    inventory_path = os.path.join(test_dir_path, 'data/hosts')
    task_ds = [{'debug': {'msg': 'hello world'}, 'block': 'test'}]

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=inventory_path)

# Generated at 2022-06-13 08:28:30.821100
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    # we import here to prevent a circular dependency with imports
    from ansible.playbook.role_include import IncludeRole
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.task import Task
    # Create fixture objects
    # FIXME: do we need all of these?
    #      - test_loader
    #      - test_variable_manager
    #      - test_play
    #      - test_block
    #      - test_task_include
    #      - test_role
    test_variable_manager = VariableManager()
    test_loader = DictDataLoader({})
    test_play = Play()
    test_block = Block()
    test_task_include = TaskInclude()
    test_role = Role()
    # Create list of dictionary objects to be converted to tasks


# Generated at 2022-06-13 08:28:33.245599
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    assert load_list_of_tasks(ds=None, play={}, block={}, role={}) == None

# Generated at 2022-06-13 08:28:44.847556
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.block import Block

    play = {
            'hosts': 'all',
            'roles': ['test']
            }
    block = Block()
    role = None
    use_handlers = False
    task_include = None
    variable_manager = DictData({}, {})
    loader = DictData({}, {})

    ds = [
        {'debug': 'msg=hello'},
        {'debug': 'msg=hello'},
        {'block': 'block1',
            'block1': [
                {'block': 'block2',
                    'block2': [
                        {'debug': 'msg=hello'}
                    ]
                }
            ]
        },
        {'debug': 'msg=hello'},
    ]

    res = load_list_of

# Generated at 2022-06-13 08:28:50.804718
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    try:
        load_list_of_tasks('not a list')
    except AssertionError:
        pass
    else:
        raise AssertionError('expected load_list_of_tasks to fail when argument is not a list')

    # load_list_of_tasks should return empty list when called with a empty list
    assert [] == load_list_of_tasks([])

    # load_list_of_tasks should return singleton when called with single list
    try:
        load_list_of_tasks([{'name': 'good task'}])
    except AssertionError:
        pass
    else:
        raise AssertionError('expected load_list_of_tasks to fail when argument is not a dict')

    # load_list_of_tasks should return singleton when called with

# Generated at 2022-06-13 08:29:02.166133
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    # Initialize
    test_str = '{"block": "test"}'
    task_ds = yaml.load(test_str)
    play = AnsiblePlay()
    block = None
    role = None
    task_include = None
    variable_manager = VariableManager()
    loader = DictDataLoader({})

    try:
        load_list_of_tasks(None, play, block, role, task_include, variable_manager, loader)
        assert False
    except AnsibleAssertionError as e:
        assert True

    try:
        load_list_of_tasks(1, play, block, role, task_include, variable_manager, loader)
        assert False
    except AnsibleAssertionError as e:
        assert True


# Generated at 2022-06-13 08:29:14.389574
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.role import Role
    from ansible.playbook.task import Task
    from ansible.playbook.play import Play
    from ansible.playbook.playbook import Playbook
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.handler import Handler

    task_ds_0 = {
        'name': 'test task 1',
        'action': {'module': 'test', 'args': 'test args'},
        'loop': '{{ var }}',
        'when': 'when_test',
        'async': 10,
        'delegate_to': 'localhost'
    }

    task_ds_1 = {
        'include': '{{ var }}',
        'loop': '{{ var }}'
    }


# Generated at 2022-06-13 08:29:15.250718
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    pass

# Generated at 2022-06-13 08:29:17.194052
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    assert load_list_of_tasks([1]) == []



# Generated at 2022-06-13 08:29:27.528821
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.yaml.reader import AnsibleReader
    from ansible.vars.manager import VariableManager
    '''
    Given a list of task datastructures (parsed from YAML),
    return a list of Task() or TaskInclude() objects.
    '''

    # we import here to prevent a circular dependency with imports
    from ansible.playbook.block import Block
    from ansible.playbook.handler import Handler
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.role_include import IncludeRole

# Generated at 2022-06-13 08:29:37.252767
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    # the tests in this function exist to cover the load_list_of_tasks function
    # in ansible.parsing.dataloader in the ansible repo.

    # setting up some data_structures
    ds1 = dict(name='test_statment_1', shell='echo "hello world"')
    ds2 = dict(name='test_statment_2', shell='echo "goodbye world"')
    ds3 = dict(name='test_statment_3', shell='echo "foo bar"')
    ds4 = dict(
        name='test_statment_4',
        block=dict(tasks=[ds2,ds3]))
    ds5 = dict(
        name='test_statment_5',
        include='test_file')