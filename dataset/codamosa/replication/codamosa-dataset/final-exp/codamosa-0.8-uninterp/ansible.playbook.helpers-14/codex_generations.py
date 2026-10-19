

# Generated at 2022-06-13 08:21:17.389446
# Unit test for function load_list_of_roles
def test_load_list_of_roles():

    def mock_play_loader_pathfinders():
        return 'pathfinders'

    def mock_variable_manager_get_vars():
        return 'vars'

    def mock_loader_get_basedir():
        return 'basedir'

    def mock_loader_path_dwim(file):
        return file
    
    def mock_task_load(ds, play, block, role, task_include, variable_manager, loader):
        return {
            'ds': ds,
            'play': play,
            'block': block,
            'role': role,
            'task_include': task_include,
            'variable_manager': variable_manager,
            'loader': loader,
        }


# Generated at 2022-06-13 08:21:28.749969
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.play import Play

    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    from ansible.utils.vars import combine_vars
    from ansible.template import Templar

    p = Play().load({
        'name': 'test play',
        'hosts': 'all',
        'tasks': [
            dict(include='/tmp/testme.yml', static=True),
        ]
    }, variable_manager=VariableManager(), loader=None)

    variable_manager = p.get_variable_manager()

# Generated at 2022-06-13 08:21:36.035891
# Unit test for function load_list_of_roles
def test_load_list_of_roles():
    # Test basic behavior
    res = load_list_of_roles(ds=[
            {'role': 'base'},
        ], play=None, current_role_path=None, variable_manager=None, loader=None, collection_search_list=None)
    assert isinstance(res, list)
    assert len(res) == 1
    assert isinstance(res[0], RoleInclude)
    assert res[0].role_name == 'base'
    assert res[0].collections == []

    # Test collection_search_list priority over role path

# Generated at 2022-06-13 08:21:45.481611
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    set_fake_assertions_made()
    ds = [{'include_tasks': '_tasks.yml'}]
    # play is a object only used to generate a fake attribute to fulfill the demands of the function
    play = FakeTask()
    block = None
    role = 'role_and_task_dir'
    task_include = None
    use_handlers = False
    variable_manager = FakeTask()
    loader = FakeTask()
    # test_data is a dict which contains the expected result of the function and the parameter used in the function

# Generated at 2022-06-13 08:21:48.799329
# Unit test for function load_list_of_roles
def test_load_list_of_roles():
    # we import here to prevent a circular dependency with imports
    import ansible.playbook.role.include
    assert hasattr(ansible.playbook.role.include, "RoleInclude")
    import ansible.playbook.block
    assert hasattr(ansible.playbook.block, "Block")
    import ansible.playbook.task
    assert hasattr(ansible.playbook.task, "Task")


# Generated at 2022-06-13 08:21:59.941243
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    def regex_match(pattern, text):
        regex = re.compile(pattern)
        return regex.match(text) is not None

    def assert_only_keys(dct, *keys):
        assert list(dct.keys()) == list(keys), 'Should be %s' % list(keys)

    ns = dict(
        regex_match=regex_match,
        assert_only_keys=assert_only_keys,
        Ansible=dict(
            MODULE_REQUIRE_ARGS=False,
            DEFAULT_FORKS=10,
            DEFAULT_REMOTE_PORT=22,
            DEFAULT_ASK_SUDO_PASS=False,
            DEFAULT_ASK_SU_PASS=False,
            DEFAULT_REMOTE_USER='root'
        ),
    )

    ns_copy

# Generated at 2022-06-13 08:22:14.848634
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.plugins.loader import action_loader
    from ansible.plugins.loader import module_loader

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, sources=['client.cfg'])
    variable_manager.set_inventory(inventory)

# Generated at 2022-06-13 08:22:26.671960
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.role_include import IncludeRole
    from ansible.playbook.handler import Handler
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude

    # Instantiate test variables

    block_ds = [dict(action='block')]
    task_ds = [dict(action='task')]
    inc_ds = [dict(action='include')]
    inc_role_ds = [dict(action='include_role')]

    # Test when action is block
    try:
        res = load_list_of_tasks(block_ds, play=True, block=True, role=True, task_include=True, use_handlers=True, variable_manager=True, loader=True)

    except AnsibleAssertionError:
        pass



# Generated at 2022-06-13 08:22:36.173631
# Unit test for function load_list_of_tasks

# Generated at 2022-06-13 08:22:36.863424
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    return

# Generated at 2022-06-13 08:23:07.629194
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    # make sure this function works when passing in a list of task ds
    assert load_list_of_tasks([
        {'name': 'test1', 'action': 'include', 'args': 'blah.yml'},
        {'name': 'test2', 'action': 'include', 'args': 'blah.yml'},
        {'name': 'test3', 'action': 'include', 'args': 'blah.yml'}
    ])

    # make sure this function works when passing in no ds
    assert load_list_of_tasks(None) is None

    # make sure this function raise for wrong ds type
    with pytest.raises(AnsibleAssertionError):
        assert load_list_of_tasks(dict())



# Generated at 2022-06-13 08:23:18.073260
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    import ansible.errors as errors
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task

    # test when parameters are correct
    correct_ds = [{'action':{'module':'ping'}, 'name':'ping'}]
    assert isinstance(load_list_of_tasks(correct_ds, Block(), None, None)[0], Task)

    # test when parameters are incorrect
    incorrect_ds = [{'action':{'module':'ping'}, 'name':'ping'}, {'action':{'module':'ping'}}]
    assert isinstance(load_list_of_tasks(incorrect_ds, Block(), None, None)[0], Task)

    # test when parameters are incorrect

# Generated at 2022-06-13 08:23:19.528724
# Unit test for function load_list_of_blocks
def test_load_list_of_blocks():
    pass



# Generated at 2022-06-13 08:23:26.123981
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


# Generated at 2022-06-13 08:23:36.304271
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    '''
    For this test we need some resources.
    The tests expect these to be in the current directory
    '''
    from ansible.playbook.play import Play
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.task import Task
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.plugins.callback import CallbackBase
    import ansible.constants as C

    # Create the necessary objects (mocking as much as possible)
    loader = DataLoader()

# Generated at 2022-06-13 08:23:44.109272
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():

    from ansible.parsing.vault import VaultLib
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.role_include import IncludeRole
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.play_context import PlayContext
    from ansible.vars import VariableManager


    tasks_data = [
        {"block": [{"name": "task1"}]},
        {"block": [{"name": "task2"}]},
        {"shell": "echo 'task3'"},
        {"shell": "echo 'task4'"},
        {"include_role": {"name": "role1", "static": True}},
        {"import_role": {"name": "role2", "static": True}}
    ]

# Generated at 2022-06-13 08:23:55.799696
# Unit test for function load_list_of_roles
def test_load_list_of_roles():
    # we import here to prevent circular dependency with imports
    from ansible.playbook.role import Role
    from ansible.playbook.role.include import IncludeRole
    from ansible.playbook.role.definition import RoleDefinition

    mock_loader = unittest.mock.MagicMock()
    mock_loader.path_exists.return_value = True
    mock_loader.path_dwim.return_value = "/some/path/to/a/role.yml"
    mock_loader.list_directory.return_value = ["some_role1", "role_with_vars"]

    mock_var_manager = unittest.mock.MagicMock()

    mock_play = unittest.mock.MagicMock()

# Generated at 2022-06-13 08:23:57.914033
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    assert 1 == 1
test_load_list_of_tasks()


# Generated at 2022-06-13 08:23:59.273216
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    # TODO implement me
    return

# Generated at 2022-06-13 08:24:10.288609
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.play import Play
    from ansible.playbook.role import Role
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.role_include import IncludeRole
    from ansible.playbook.handler_task_include import HandlerTaskInclude
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    import ansible.constants as C
    import os
    import json

    # test load_list_of_tasks
    loader = DataLoader()
    variable_manager = VariableManager()

# Generated at 2022-06-13 08:24:54.826673
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    pass
# Unit tests for function load_list_of_blocks

# Generated at 2022-06-13 08:25:07.743571
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.playbook import Playbook
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.role_include import IncludeRole

    variable_manager = VariableManager()
    loader = DataLoader()
    variable_manager.set_loader(loader)

    result = loader.load_from_file('play.yml')

    play = Playbook.load(result, variable_manager=variable_manager, loader=loader)
    play = play.get_plays()[0]

    assert isinstance(play, PlayContext)

    assert isinstance(load_list_of_tasks(play.tasks, play=play, variable_manager=variable_manager, loader=loader), list)

# Generated at 2022-06-13 08:25:22.778731
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    # import needed inside method to prevent circular dependency with imports from
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.template import Templar
    from ansible.utils.vars import combine_vars

    groups = {
               'hosts1': {'hosts': ['127.0.0.1']},
               'hosts2': {'hosts': ['127.0.0.2']},
               'group_vars': {
                                'group_vars1': {'var1': 'val1'},
                                'group_vars2': {'var2': 'val2'}
                            },
             }
    host

# Generated at 2022-06-13 08:25:37.774412
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    # TODO: refactor the load_list_of_tasks function to make it testable
    # we import here to prevent a circular dependency with imports
    from ansible.playbook.block import Block
    from ansible.playbook.role_include import IncludeRole
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.handler_task_include import HandlerTaskInclude

    ds = [
        {
            'block': [
                {'debug': '{{ test }}'}
            ]
        },
        {
            'include_tasks': 'test.yml'
        },
        {
            'include_role': {'name': 'test'}
        },
    ]

    task_list = load_list_of_tasks(ds)


# Generated at 2022-06-13 08:25:38.668224
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    pass



# Generated at 2022-06-13 08:25:47.199235
# Unit test for function load_list_of_roles
def test_load_list_of_roles():
    ansible_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
    data = [
        {
            'role': 'somerole'
        },
        {
            'role': 'somerole2'
        }
    ]

    play = Play()
    play_ds = {}
    loader = DataLoader()
    variable_manager = VariableManager()
    collection_search_list = []

    roles = load_list_of_roles(data, play, current_role_path=ansible_path + "/test/test_data/test_roles/", loader=loader,
                               variable_manager=variable_manager, collection_search_list=collection_search_list)
    print("Roles: %s" % roles)
   

# Generated at 2022-06-13 08:26:00.036967
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    # This one is not very good.
    
    g = AnsibleCollectionLoader()
    g.update_collection_folders(['/Users/martin/projets/ansible_collections/ansible_collections/ansible/netcommon'])
    g.add_directory('/Users/martin/projets/ansible_collections/ansible_collections/ansible/netcommon')
    init_config = dict()
    init_config['collect_ignore'] = []
    init_config['roles_path'] = "/Users/martin/projets/ansible_collections/ansible_collections/ansible/netcommon"
    g.add_directory('/Users/martin/projets/ansible_collections/ansible_collections/ansible/netcommon', init_config)
    

# Generated at 2022-06-13 08:26:07.260661
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    variable_manager = VariableManager()
    variable_manager._fact_cache = {'ansible_facts': {'testvar': 'testvalue'}}


# Generated at 2022-06-13 08:26:18.093109
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude

    # Test for load_list_of_tasks
    # Invalid datastructure test
    ds = {}
    try:
        load_list_of_tasks(ds, None)
    except AnsibleAssertionError:
        pass
    else:
        raise AssertionError("Expect AnsibleAssertionError")

    # Invalid task datastructure test
    ds = ['t', 'ttt']
    try:
        load_list_of_tasks(ds, None)
    except AnsibleAssertionError:
        pass
    else:
        raise AssertionError("Expect AnsibleAssertionError")

    # Invalid task datastructure test 2

# Generated at 2022-06-13 08:26:25.391528
# Unit test for function load_list_of_blocks
def test_load_list_of_blocks():
    from ansible.playbook.block import Block

    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.dataloader import DataLoader

    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    from ansible.playbook.play import Play

    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.executor.process.factory import Factory
    factory = Factory()
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=[
            'localhost,'
        ])

# Generated at 2022-06-13 08:27:26.782083
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    assert load_list_of_tasks({
        "foo": "bar"
    }, play='play', block='block', role='role', task_include='task_include', use_handlers='use_handlers', variable_manager='variable_manager', loader='loader') == []

# Generated at 2022-06-13 08:27:35.854877
# Unit test for function load_list_of_blocks
def test_load_list_of_blocks():
    from ansible.playbook.play import Play
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.vars import VariableManager
    import ansible.constants as C
    import os

    fake_ds = [
        {
            'block': [
                {'task': {'name': 'foo', 'action': 'shell echo hi'}},
                {'task': {'name': 'bar', 'action': 'shell echo hi'}},
            ],
        },
        {'task': {'action': 'command echo hi'}},
    ]


# Generated at 2022-06-13 08:27:49.943131
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():


    class FakeVars():
        def get_vars(self,play=None,task=None):
            return {
                "disk_size": 1,
                "disk_dev_list": [
                    "/dev/sdb"
                ],
                "disk_model_list": [
                    "SATA_SSD_b"
                ],
                "disk_dev_name_list": [
                    "sdb"
                ]
            }

    class FakePlay():
        def __init__(self):
            self.vars = FakeVars()


# Generated at 2022-06-13 08:27:59.614765
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible import constants as C
    from ansible.errors import AnsibleParserError
    from ansible.playbook.block import Block
    from ansible.playbook.handler import Handler
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager

    # defined in 't.yml'

# Generated at 2022-06-13 08:28:11.553982
# Unit test for function load_list_of_blocks
def test_load_list_of_blocks():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    from ansible.utils.vars import combine_vars
    from ansible.vars import VariableManager
    from ansible.utils.vars import load_extra_vars
    from ansible.vars import VariableManager, TemplateVars

    vars_loader = VariableManager()
    parent_vars = load_extra_vars(loader=vars_loader, options=None)
    vars_loader.set_inventory(parent_vars)
    variable_manager = VariableManager()

    variable_manager.add_group_vars_files(
        variable_manager.get_group_variables(group='all'),
    )

    variable_manager.set_nonpersistent_facts(dict())
    variable_

# Generated at 2022-06-13 08:28:25.634330
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    test_string = """---
- include_tasks: ./test.yml
"- import_tasks: ./test.yml"
""".strip()

    raw_ds = yaml.safe_load(test_string)

    # We don't need to load a full playbook, and we want to test the block
    # loading, so we'll just call the internal load_list_of_tasks method
    # directly.
    task_list = load_list_of_tasks(
        ds=raw_ds,
        play=None,
        block=None,
        role=None,
        task_include=None,
        use_handlers=False,
        variable_manager=None,
        loader=None,
    )

    # We should have a task include and an import task

# Generated at 2022-06-13 08:28:36.722208
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    test_task=dict(
        block=dict(
            tasks=dict(
                block1=dict(
                    tasks=['action1'],
                    rescue='action2'
                ),
                block2=dict(
                    block=dict(
                        tasks=['action3'],
                        rescue='action4'
                    ),
                    rescue=['action5'],
                    always=['action6']
                )
            ),
            rescue=['action7'],
            always=['action8']
        ),
        rescue=['action9'],
        always=['action10']
    )
    display.deprecated = lambda x, y: None

# Generated at 2022-06-13 08:28:47.420213
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.play import Play
    from ansible.playbook.block import Block
    from ansible.playbook.role_include import IncludeRole
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.task import Task

    fake_play = Play().load(
        dict(
            name = 'fakeplay',
            hosts = 'fakehosts',
            gather_facts = 'no',
            vars = {},
            roles = [],
        ),
        variable_manager=None,
        loader=None
    )
    fake_block = Block(parent_block=None, role=None, task_include=None, use_handlers=False, variable_manager=None, loader=None, play=fake_play)
    fake_block._parent = fake_block

    #

# Generated at 2022-06-13 08:28:59.480951
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    # Incomplete unit test
    fake_play = type('Play', (object,), {})
    fake_block = type('Block', (object,), {})
    fake_role = type('Role', (object,), {})
    fake_task_include = type('TaskInclude', (object,), {})

    playbook_dir = os.path.dirname(os.path.dirname(__file__))
    playbook = os.path.join(playbook_dir, 'test_playbook.yml')
    playbook_loader = DataLoader()

# Generated at 2022-06-13 08:29:09.159842
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():

    ds = [{'local_action': 'module'},
          {'local_action': 'module'},
          {'local_action': 'module'}]

    task_list = load_list_of_tasks(ds, play=None, block=None, role=None, task_include=None, use_handlers=False, variable_manager=None, loader=None)
    if len(task_list) != 3:
        print ("Test load_list_of_tasks: FAILED")
    else:
        print ("Test load_list_of_tasks: PASSED")

if __name__ == '__main__':
    test_load_list_of_tasks()

# Generated at 2022-06-13 08:30:11.783477
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    ds = [dict(action=dict(module='debug', args=dict(msg='hello world'))),
          dict(action=dict(module='include_tasks', args=dict(static=True), include=dict(file='foo.yml')))]

    play = Play()
    block=None
    task_include=None
    role=None
    var_manager = VariableManager()
    loader = DataLoader()
    use_handlers=False

    task = load_list_of_tasks(ds, play, block, role, task_include, use_handlers, var_manager, loader)
    assert isinstance(task[0], Task)
    assert isinstance(task[1], TaskInclude)



# Generated at 2022-06-13 08:30:21.278332
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
  from ansible.vars import VariableManager
  from ansible.inventory import Inventory
  from ansible.playbook.play import Play
  from ansible.executor.task_queue_manager import TaskQueueManager
  from ansible.plugins.callback import CallbackBase

  class ResultCallback(CallbackBase):
      """A sample callback plugin used for performing an action as results come in

      If you want to collect all results into a single object for processing at
      the end of the execution, look into utilizing the ``json`` callback plugin
      or writing your own custom callback plugin
      """
      def v2_runner_on_ok(self, result, **kwargs):
          """Print a json representation of the result

          This method could store the result in an instance attribute for retrieval later
          """
          host = result._host
          print(result.task_name)
         

# Generated at 2022-06-13 08:30:36.306443
# Unit test for function load_list_of_blocks
def test_load_list_of_blocks():
    '''
    Test load_list_of_blocks with a list of tasks. Create an implicit block.
    '''
    # Create a tasklist
    ds = [
        {'include': 'some_task'},
        {'include': 'some_other_task'},
        'a_bare_task',
        [
            {'include': 'some_block_task'},
            {'include': 'some_other_block_task'}
        ]
    ]
    # We need some objects to avoid errors when creating the block
    play = 'my_play'
    role = 'my_role'
    task_include = 'my_task_include'
    use_handlers = True
    variable_manager = 'my_variable_manager'
    loader = 'my_loader'
    # Create the blocks
    block