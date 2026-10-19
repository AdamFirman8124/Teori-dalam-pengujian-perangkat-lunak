

# Generated at 2022-06-13 08:21:18.084384
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    # simple test coverage of a type fail
    mylist = {}
    b = Block()
    with pytest.raises(AnsibleAssertionError):
        load_list_of_tasks(mylist, b)


# Generated at 2022-06-13 08:21:29.226847
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.utils.vars import combine_vars
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    import json
    import os
    import sys
    import copy

    class Options(object):
        """
        Options class to replace the Ansible OptParser
        """
        verbosity = 0
        connection = 'local'
        module_path = None
        forks = 10
        check = False
        diff = False
        inventory = None
        listhosts = None

# Generated at 2022-06-13 08:21:30.133323
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
  # TODO
  assert False

# Generated at 2022-06-13 08:21:37.295418
# Unit test for function load_list_of_blocks
def test_load_list_of_blocks():
    from ansible.playbook.block import Block
    from ansible.parsing.dataloader import DataLoader
    def loader_for_data(data):
        return DataLoader()
    def get_variable_manager(loader):
        from ansible.vars.manager import VariableManager
        return VariableManager()
    def get_play_context(variable_manager):
        from ansible.playbook.play_context import PlayContext
        return PlayContext()
    def get_playbook(loader_for_data, get_variable_manager, get_play_context):
        from ansible.playbook.play import Play
        return Play()
    def get_task(loader_for_data, get_variable_manager, get_play_context, get_playbook):
        from ansible.playbook.task import Task
        return Task()

# Generated at 2022-06-13 08:21:46.192548
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    assert load_list_of_tasks(ds=[], play=None, block=None, role=None, task_include=None, use_handlers=False, variable_manager=None, loader=None) == []
    assert load_list_of_tasks(ds=None, play=None, block=None, role=None, task_include=None, use_handlers=False, variable_manager=None, loader=None) == []
    assert load_list_of_tasks(ds='', play=None, block=None, role=None, task_include=None, use_handlers=False, variable_manager=None, loader=None) == []

# Generated at 2022-06-13 08:21:55.004502
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():

    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play

    # block = load_list_of_tasks(ds, play, block=None, variable_manager=variable_manager, loader=loader)
    variable_manager = VariableManager()
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=None)
    variable_manager.set_inventory(inventory)

    # initializes a play object

# Generated at 2022-06-13 08:21:56.432585
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    # TODO: implement
    pass



# Generated at 2022-06-13 08:22:04.278997
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    """
    Test loading of ds with dict and list
    """
    template_ds = {
        'name': 'Test',
        'description': 'Test description',
        'connection': 'local',
        'hosts': 'all',
        'gather_facts': 'no',
        'vars': {},
        'tasks': [
            {
                'name': 'Test'
            },
            {
                'name': 'Test'
            },
            [{
                'name': 'Test'
            }]
        ],
    }
    play = Play().load(template_ds, variable_manager=VariableManager(), loader=DictDataLoader())

# Generated at 2022-06-13 08:22:17.410315
# Unit test for function load_list_of_roles
def test_load_list_of_roles():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.role.include import RoleInclude
    from ansible.playbook import Play
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.vars import combine_vars
    from ansible import context
    from ansible.executor.task_queue_manager import TaskQueueManager


# Generated at 2022-06-13 08:22:29.194899
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    # test_data_structure = [{"test_task1":"t1"},{"test_task2":"t2"}]
    # result = load_list_of_tasks(test_data_structure, None)
    # assert result.__class__ == list
    test_data_structure = [{"test_task1":"t1"},{"test_task2":"t2"}]
    result = load_list_of_tasks(test_data_structure)
    assert result.__class__ == list
if __name__ == '__main__':
    test_load_list_of_tasks()

# Generated at 2022-06-13 08:22:56.698315
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.handler import Handler
    from ansible.playbook.block import Block
    from ansible.template import Templar
    from ansible.vars.unsafe_proxy import UnsafeProxy
    from ansible.utils.display import Display
    display = Display()

    global_loader = DictDataLoader({})
    global_loader.set_basedir('/foo/bar')
    global_loader._basedir = '/foo/bar'
    global_loader._command_data = {}

    variable_manager = VariableManager()
    variable_manager.extra_vars = {'hostvars': {'host-M': {'roles': ['app', 'web']}}}
    variable_manager._fact_

# Generated at 2022-06-13 08:23:00.322063
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    # Load the list of tasks
    with open("../../examples/ansible-roles/roles/dev/tasks/main.yml", "r") as f:
        tasks = yaml.load(f.read())

    task_loader = TestTaskLoader()
    task_loader.set_task_key("tasks")

    # Build list of tasks
    task_list = load_list_of_tasks(tasks, task_loader)
    task_count = len(task_list)

    return task_count

if __name__ == "__main__":
    task_count = test_load_list_of_tasks()
    print("Task count: " + str(task_count))

# Generated at 2022-06-13 08:23:07.110530
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    pass
    #import yaml
    #from ansible.playbook.play import Play
    #from ansible.playbook.play_context import PlayContext
    #from ansible.template import Templar
    #from ansible.plugins.loader import add_all_plugin_dirs
    #
    ## Template the tasks to resolve any variables
    #add_all_plugin_dirs()
    #
    #task_list = [
    #    {
    #        'include': '{{ include_me }}',
    #        'include_tasks': '{{ include_me }}',
    #        'import_tasks': '{{ include_me }}',
    #        'include_role': '{{ include_me }}',
    #        'import_role': '{{ include_me }}',
    #        'static': True,
    #

# Generated at 2022-06-13 08:23:10.777723
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    # load_list_of_tasks(ds, play, block=None, role=None, task_include=None, use_handlers=False, variable_manager=None, loader=None):
    
    assert True


# Generated at 2022-06-13 08:23:20.352222
# Unit test for function load_list_of_blocks
def test_load_list_of_blocks():
    # Valid data
    data = [
        {'block': [
            {'task': [
                {'include': 'test1.yml'},
                {'include': 'test2.yml'}
            ]}]},
        {'block': [
            {'task': [
                {'include': 'test3.yml'},
                {'include': 'test4.yml'}
            ]}]},
        {'block': [
            {'task': [
                {'include': 'test5.yml'},
                {'include': 'test6.yml'}
            ]}]},
    ]
    # Call the function to test
    load_list_of_blocks(data, None)
    # Tests
    assert True


#--- end of test_load_list_of

# Generated at 2022-06-13 08:23:22.392958
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    assert False, "Need to write unit tests for load_list_of_tasks"


# Generated at 2022-06-13 08:23:33.757374
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.play_context import PlayContext

    from units.mock.loader import DictDataLoader
    from units.mock.path import mock_unfrackpath_noop

    loader = DictDataLoader({
        "test_include.yml": "",
        "test_include_static.yml": "",
        "test_include_dynamic.yml": "",
        "test_dynamic_include.yml": "",
        "handler_tasks/test_include.yml": "",
        "handler_tasks/test_include_static.yml": "",
        "handler_tasks/test_include_dynamic.yml": "",
    })
    variable_manager = MagicMock()

# Generated at 2022-06-13 08:23:44.031675
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    class Options():
        def __init__(self, tag_list=None, listtags=False, listtasks=False, listhosts=False, syntax=False, connection=None,
                     module_path=None, forks=100, remote_user=None,
                     private_key_file=None, ssh_common_args=None, ssh_extra_args=None, sftp_extra_args=None, scp_extra_args=None,
                     become=False, become_method=None, become_user=None, verbosity=False, check=False):
            self.tag_list=tag_list
            self.listtags=listtags
            self.listtasks=listtasks
            self.listhosts=listhosts
            self.syntax=syntax
            self.connection=connection
            self.module_path

# Generated at 2022-06-13 08:23:55.711609
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.block import Block
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.role_include import IncludeRole
    

# Generated at 2022-06-13 08:24:11.776661
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    module_loader=unittest_module_loader
    fake_play=play_for_rescue(module_loader)
    rescue_option={'rescue':'{{ rescue }}', 'rescue_async':'{{ rescue_async }}'}
    tasks=[{'name':'test1', 'action':'debug', 'rescue':'1', 'rescue_async':'2'},
           {'name':'test2', 'action':'debug', 'rescue':'3', 'rescue_async':'4'},
           {'name':'test3', 'action':'debug', 'rescue':'5', 'rescue_async':'6'}]
    variable_manager=VariableManager()
    variable_manager.set_nonpersistent_facts(inventory_for_rescue())
    task_

# Generated at 2022-06-13 08:24:39.576696
# Unit test for function load_list_of_roles
def test_load_list_of_roles():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.playbook.role.meta import RoleMetadata
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.role.requiremenets import RoleRequirement
    from ansible.playbook.role.include import RoleInclude
    from ansible.playbook.role.include import get_collections_to_search


# Generated at 2022-06-13 08:24:44.021802
# Unit test for function load_list_of_roles
def test_load_list_of_roles():
    ds = [{'role': 'role_name', 'vars': {}}]
    play = Play().load({'name': 'test_play', 'hosts': 'all', 'roles': ds}, variable_manager=None, loader=None)
    role_list = load_list_of_roles(ds, play, variable_manager=None, loader=None)
    assert len(role_list) == 1
    assert role_list[0]._role_name == ds[0]['role']



# Generated at 2022-06-13 08:24:45.606713
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    assert load_list_of_tasks is not None

# Generated at 2022-06-13 08:25:00.753548
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    ds = "- debug: msg='Hello world'\n"
    ds += "  with_dict: '{{ some_dict }}'\n"
    ds += "  loop_control:\n"
    ds += "    loop_var: '{{ item.key }}'\n"
    ds += "  tags: foo\n"
    ds += "  any_errors_fatal: True\n"
    ds += "  rescue:\n"
    ds += "  - debug: msg='We rescued something'"

    tasks = load_list_of_tasks(ds, dict(), dict())
    assert len(tasks) == 1
    t = tasks[0]
    assert t.any_errors_fatal == True
    assert t.loop_control == dict(loop_var='{{ item.key }}')

# Generated at 2022-06-13 08:25:12.032874
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    # modules_mapping
    modules_mapping = C.DEFAULT_MODULE_MAPPING
    # setup_cache
    setup_cache = dict()
    # defaults
    defaults = dict()
    # tasks
    tasks = []
    # task_vars
    task_vars = dict()
    # _variable_manager
    _variable_manager = VariableManager()

    _variable_manager.extra_vars = task_vars
    _variable_manager.options_vars = defaults
    # inventory
    inventory = Inventory()
    # play
    play = Play()
    play.filter_handler = []
    play.filter_loader = C.DEFAULT_FILTER_PLUGIN_LOADER
    # _loader
    _loader = DataLoader()

    # Set variable_manager to _variable_manager
    _variable

# Generated at 2022-06-13 08:25:19.723743
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    display.verbosity = 4
    loader = DataLoader()
    variable_manager = VariableManager()
    variable_manager.extra_vars = dict(foo='bar')
    variable_manager.options_vars = dict(ansible_foo='bar')
    variable_manager.set_inventory(Inventory(loader=loader, variable_manager=variable_manager, host_list=[Host()]))
    play = Play().load({
        'name': 'test',
        'hosts': 'all',
        'gather_facts': 'no',
        'tasks': [
            {'include': '{{ foo }}'}
        ]
    }, variable_manager=variable_manager, loader=loader)
    play._variable_manager = variable_manager
    play._loader = loader

# Generated at 2022-06-13 08:25:26.411484
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    global _load_list_of_tasks_PLAY
    global _load_list_of_tasks_EXTRAVARS
    # FIXME: duplicates of code from ansible-playbook
    from ansible.config.manager import ConfigManager
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.utils.vars import load_extra_vars
    from ansible.utils.vars import load_options_vars
    from ansible.utils.vars import combine_vars


# Generated at 2022-06-13 08:25:39.708551
# Unit test for function load_list_of_blocks
def test_load_list_of_blocks():
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    ds = [ {'include': 'test.yml'},{'tasks': [{'debug': 'msg={{testvar}}'}]}, {'include': 'test2.yml'}]
    blocks = load_list_of_blocks(ds, Play(), None)
    assert(len(blocks) == 2, "Should have 2 blocks")
    assert(isinstance(blocks[0], Task))
    assert(blocks[0].include is not None)
    assert(blocks[0].block is None)
    assert(blocks[0].role is None)
    assert(isinstance(blocks[1].block, Block))
    assert(len(blocks[1].block._entries) == 2)


# Generated at 2022-06-13 08:25:51.747749
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.role_include import IncludeRole
    from ansible.module_utils._text import to_bytes
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager

    templar = Templar(loader=None, variables={})
    varmgr = VariableManager()

    data = list()
    task = dict(
        include = dict(
            _raw_params='site.yml',
            static = False
        )
    )
    data.append(task)
    task = dict(
        import_playbook=dict(
            _raw_params='another_playbook.yml',
            static=False
        )
    )
    data.append(task)


# Generated at 2022-06-13 08:25:55.708619
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    '''
    This tests that the function load_list_of_tasks()
    works.
    '''

    # TODO:
    raise NotImplementedError()


# Generated at 2022-06-13 08:26:16.304730
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    pass


# Generated at 2022-06-13 08:26:30.504028
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    # Testing load_list_of_tasks function.
    import tempfile
    import yaml

    from ansible.playbook.play import Play
    from ansible.playbook.block import Block
    from ansible.playbook.handler import Handler
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.role_include import IncludeRole
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    # Creating play objects
    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, sources=['localhost,'])
    variable_manager.set_inventory(inventory)

    fakevu = Magic

# Generated at 2022-06-13 08:26:42.016541
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    test_file = {
        'block':
        [
            {
                'block':
                [
                    {
                        'block': [
                            {'local_action': 'shell echo A',
                            },
                            {'local_action': 'shell echo B',
                            },
                            {'local_action':
                                {'module': 'shell', 'args': 'echo C'},
                            },
                        ]
                    },
                ],
            },
            {
                'block':
                [
                    {'local_action': 'shell echo D',
                    },
                    {'local_action': 'shell echo E',
                    },
                ],
            },
        ]
    }
    actual = load_list_of_tasks(test_file, None, None, None, None, False, None, None)

# Generated at 2022-06-13 08:26:51.969318
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.play_context import PlayContext
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources='')

    play_context = PlayContext()
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    ds = [
        {'local_action': 'ping'},
        {'local_action': 'ping'},
    ]


# Generated at 2022-06-13 08:27:04.319192
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    loader = DictDataLoader({
        "/etc/ansible/my_include_tasks_file.yml": """
        - name: "do some task that I'm no good at"
          action: include_tasks "{{ tasks_file }}"
          tags: ["always"]
          register: foo

        - block:

            - name: "do a thing"
              action: ping

            - name: "do another thing"
              action: ping
          rescue:
            - name: "panic"
              action: ping
          always:
            - name: "clean up"
              action: ping
        """
    })

    fake_inventory = InventoryManager(loader=loader, sources=[])
    variable_manager = VariableManager(loader=loader, inventory=fake_inventory)


# Generated at 2022-06-13 08:27:14.493268
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    import ansible.playbook.play
    from ansible.playbook.role_include import IncludeRole
    from ansible.playbook.task import Task
    class FakePlaybook:
        def __init__(self):
            self.host_list = ['localhost']
    class FakeTaskInclude:
        def __init__(self, args_raw_params):
            self.args = {'_raw_params': args_raw_params}
            self.statically_loaded = True
    def fake_path_dwim_relative(*args, **kwargs):
        return args[0] + '/../tasks/' + args[1] + '/main.yml'
    def fake_load_from_file(*args, **kwargs):
        return [{'name': 'first'}, {'name': 'second'}]


# Generated at 2022-06-13 08:27:22.908486
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    # check for load_list_of_tasks function
    global load_list_of_tasks
    try:
        # open ansible/playbook/__init__.py to load the function
        f = open("/entrypoint/ansible/playbook/__init__.py")
        # read ansible/playbook/__init__.py
        content = f.read()
        # compile ansible/playbook/__init__.py code
        co = compile(content, "", 'exec')
        # execute ansible/playbook/__init__.py code
        exec(co)
        # close ansible/playbook/__init__.py
        f.close()
    except Exception as e:
        print(e)
        print("Error loading load_list_of_tasks function of ansible")
        sys

# Generated at 2022-06-13 08:27:29.126439
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    '''
    Returns a testcase dictionary for the `load_list_of_tasks` function.

    Args:
        None.

    Returns:
        A dictionary of data for testing the `load_list_of_tasks` function.
    '''

# Generated at 2022-06-13 08:27:36.881620
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.play_context import PlayContext

    test_play_context = PlayContext()
    test_play_context.remote_addr = '127.0.0.1'
    test_play_context.connection = 'local'
    test_play_context.port = 22

    self = Mock()
    self.play = Mock()
    self.play.play_context = test_play_context
    self.play_context = test_play_context

    ds = [
        dict(task=dict(name="test task 1")),
        dict(task=dict(name="test task 2")),
    ]

    loaded_tasks = load_list_of_tasks(ds, self.play)
    assert len(loaded_tasks) == 2


# Generated at 2022-06-13 08:27:48.443379
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    import ansible.constants as C
    import unittest

    # Create a class that inherits unittest.TestCase
    class TestTaskList(unittest.TestCase):
        """docstring for TestTaskList"""

        def setUp(self):
            # do something before every test
            pass

        def tearDown(self):
            # do something after every test

            # do this so teardown runs even if test fails
            try:
                pass
            finally:
                pass

        def test_list_of_tasks(self):
            # You may want to call assertEquals(a, b) instead of just assert a==b
            assert False

    # Run the unit tests
    unittest.main()



# Generated at 2022-06-13 08:28:35.907707
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    # This unit test covers load_list_of_tasks()
    import yaml


# Generated at 2022-06-13 08:28:46.937749
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    print("test_load_list_of_tasks")

    # initial setup
    ds = dict()
    play = object
    block = object
    role = object
    task_include = object
    use_handlers = False
    variable_manager = None
    loader = None

    # we import here to prevent a circular dependency with imports
    from ansible.playbook.block import Block
    from ansible.playbook.handler import Handler
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.role_include import IncludeRole
    from ansible.playbook.handler_task_include import HandlerTaskInclude

    # we need to catch the AnsibleAssertionError exceptions
    # which were added by our own code in load_list_of_

# Generated at 2022-06-13 08:28:47.970524
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    pass



# Generated at 2022-06-13 08:28:59.985009
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    # We need a dummy loader
    loader = DictDataLoader({
        "file1.yml": """
        - block:
            - debug: msg="hello"
        """,
        "file2.yml": """
        - debug: msg="hello"
        - block:
            - include_tasks: file1.yml
        """,
    })

    # Define a dummy inventory
    inventory = InventoryManager(loader=loader, sources='localhost')

    # Define a dummy variable manager
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    # Define a dummy display
    display = Display()

    # Define a dummy options
    options = Options()

    # We need a dummy fake play

# Generated at 2022-06-13 08:29:07.103366
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    set_module_args({
        '_raw_params': 'test',
        'action': 'debug',
        'when': True
    })
    set_loader_modules({
        '_raw_params': 'test',
        'action': 'debug',
        'when': True
    })
    ds = dict([('_raw_params', 'test'), ('action', 'debug'), ('when', True)])
    assert load_list_of_tasks([ds]) is not None
    unset_module_args()
    unset_loader_modules()
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.role_include import IncludeRole
    from ansible.playbook.task_include import TaskInclude

# Generated at 2022-06-13 08:29:16.597852
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    print('testing...')
    from ansible import constants as C
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.utils.display import Display
    from ansible.vars.manager import VariableManager
    display = Display()
    loader = DataLoader()
    # play_source = dict(
    #     name="Ansible Play",
    #     hosts='localhost',
    #     gather_facts='no',
    #     tasks=[
    #         dict(action=dict(module='shell', args='ls'), register='shell_out'),
    #         dict(action=dict(module='debug', args=dict(msg='

# Generated at 2022-06-13 08:29:18.091197
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    # TODO: write unit tests
    pass



# Generated at 2022-06-13 08:29:30.361237
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    '''
    This is just a sanity check, json parsing is tested in test_load_list_of_blocks
    '''
    ds = '''
- include_tasks: home-server.yaml
- name: setup
  apt: name={{item}}
  with_items:
    - dnsmasq
    - hostapd
'''
    loader = DictDataLoader({})
    variable_manager = VariableManager()
    play = Play().load(ds, variable_manager=variable_manager, loader=loader)
    tasks = load_list_of_tasks(play.get_tasks(), play)
    assert len(tasks) == 1

# Generated at 2022-06-13 08:29:38.853495
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.play import Play
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.handler import Handler
    from ansible.playbook.role.include import IncludeRole
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.handler_task_include import HandlerTaskInclude
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.plugins.loader import action_loader, cache_loader

    variable_manager = VariableManager()
    loader = DataLoader

# Generated at 2022-06-13 08:29:47.887927
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    # We are loading this into a task list, so we have to have a task
    # to start with.
    # We make a task (dict) for this purpose.
    task = dict(action=dict(module='foobar', args=dict(one=1)))

    # We have to have a play to load the task list into
    # This can be a play associated with a task or a play associated with a
    # block. It doesn't mattter at this point
    # Since we want to test load_list_of_tasks, we will use a play associated
    # with a task.
    # We make a play (dict) for this purpose
    play = dict(tasks=[])

    # Simulate an AnsiblePlay.
    # We want to be able to test load_list_of_tasks without having to import
    # AnsiblePlay