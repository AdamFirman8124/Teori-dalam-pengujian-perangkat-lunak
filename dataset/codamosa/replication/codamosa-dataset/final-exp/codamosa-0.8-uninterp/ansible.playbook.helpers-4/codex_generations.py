

# Generated at 2022-06-13 08:21:24.514712
# Unit test for function load_list_of_tasks

# Generated at 2022-06-13 08:21:28.235892
# Unit test for function load_list_of_blocks
def test_load_list_of_blocks():
    import sys
    if sys.version_info < (2, 7):
        return True
    else:
        from ansible.compat.tests import unittest

        from units.mock.loader import DictDataLoader
        from ansible.vars import VariableManager
        from ansible.playbook.play import Play
        from ansible.playbook.task import Task
        from ansible.parsing.mod_args import ModuleArgsParser
        from ansible.parsing.yaml.objects import AnsibleUnicode
        from ansible.template import Templar

        class TestModule(object):
            def __init__(self, module_args, **kwargs):
                self.module_args = module_args


# Generated at 2022-06-13 08:21:32.702978
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    test_tasks = [{
        'name': 'First task',
        'action': 'shell',
        },
        {
        'block': [
            {
                'name': 'Task 1',
                'action': 'shell',
                },
            ],
        },
        {
        'name': 'Second task',
        'action': 'shell'
        },
        {
        'block': [
            {
                'name': 'Task 2',
                'action': 'shell'
                },
            ],
        },
    ]
    assert load_list_of_tasks(test_tasks) != [{'action': 'shell', 'block': None, 'name': 'First task'}, {'action': 'shell', 'block': None, 'name': 'Second task'}]


# Generated at 2022-06-13 08:21:38.709057
# Unit test for function load_list_of_roles
def test_load_list_of_roles():
    # skip test if we don't have pytest-ansible
    try:
        import pytest_ansible
    except ImportError:
        pytest = None
    else:
        pytest = pytest_ansible.plugin

    if pytest is None:
        pytest.skip()

    # load the test roles
    role_defs = [
        {'role': 'common'},
        {'role': 'web', 'when': 'ansible_os_family == "RedHat"'},
        {'role': 'web', 'tags': ['redhat', 'fedora'], 'when': 'ansible_os_family == "Debian"'},
    ]

    role_path = './test/units/modules/test_collection/test_roles'
    loader = Dataloader()
    loader.set_basedir

# Generated at 2022-06-13 08:21:44.910050
# Unit test for function load_list_of_blocks
def test_load_list_of_blocks():
    from ansible.playbook.play import Play
    play_ds = dict(
        name = "foobar",
        hosts = "s-east",
        gather_facts = "no"
    )

    task_ds = dict(
        name = "hello",
        debug = "msg='i am task 1'"
    )

    play = Play().load(play_ds, variable_manager=None, loader=None)

    result = load_list_of_blocks([task_ds], play, variable_manager=None, loader=None)

# Generated at 2022-06-13 08:21:46.759689
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    assert load_list_of_tasks(None, None, None, None, None, None, None) == []



# Generated at 2022-06-13 08:21:55.337729
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import HandlerTaskInclude
    from ansible.playbook.handler import Handler
    task_ds = {'action': 'test'}
    play = None
    block = None
    role = None
    task_include = None
    use_handlers = False
    variable_manager = None
    loader = None
    task_list = load_list_of_tasks(task_ds,play,block,role,task_include,use_handlers,variable_manager,loader)
    assert task_list[0].__class__ == Task
    task_ds = {'include_tasks': 'other_yml'}
    play = None
    block = None
    role

# Generated at 2022-06-13 08:21:57.418828
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    # Note - This unit test is a placeholder until load_list_of_tasks can be unit tested
    pass



# Generated at 2022-06-13 08:22:11.589814
# Unit test for function load_list_of_blocks
def test_load_list_of_blocks():
    ds = [{'include' : 'test_include.yml'}]
    play = 'test_play'
    parent_block = 'test_parent_block'
    role = 'test_role'
    task_include = 'test_task_include'
    use_handlers = False
    variable_manager = 'test_variable_manager'
    loader = 'test_loader'
    
    from ansible.playbook.block import Block

    class TestBlock(Block):
        pass

    Block.load = lambda *a, **kw: TestBlock()

    block_list = load_list_of_blocks(ds, play, parent_block, role, task_include, use_handlers, variable_manager, loader)

    assert len(block_list) == 1

# Generated at 2022-06-13 08:22:18.837045
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    loader = DataLoader()
    variable_manager = VariableManager()
    play = dict()
    ds = [
        dict(action='debug', msg="hello world")
    ]
    task_list = load_list_of_tasks(ds, play, None, None, None, None, variable_manager, loader)
    assert isinstance(task_list, list)
    assert len(task_list) == 1
    task = task_list[0]
    assert isinstance(task, Task)


# Generated at 2022-06-13 08:22:57.233138
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    # Mock ansible
    ds = mock_ansible_module(
        dict(
            name='Hello {{ ansible_env.USER }}',
            become_user='{{ ansible_env.USER }}',
            environment='USER={{ ansible_user.name }}',
            environment_dict='{"USER": "{{ ansible_user.name }}"}',
        )
    )
    play = mock_ansible_module(
        dict(
            name='test play',
            hosts='all',
            gather_facts='no',
            roles='foo'
        )
    )

# Generated at 2022-06-13 08:23:06.389148
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.handler_task_include import HandlerTaskInclude
    #from ansible.playbook.role_include import IncludeRole
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.parsing.dataloader import DataLoader
    class FakePlay(object):
        def get_variable_manager(self):
            variable_manager = VariableManager()
            variable_manager.set_inventory(Inventory(loader=loader, variable_manager=variable_manager, host_list=C.DEFAULT_HOST_LIST))
            return variable_manager
    loader = DataLoader()
    play = FakePlay()



# Generated at 2022-06-13 08:23:08.192220
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    assert load_list_of_tasks("ds", "play", "block", "role", "task_include", "use_handlers", "variable_manager", "loader") == NotImplemented


# Generated at 2022-06-13 08:23:18.532410
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    # FIXME: use a better approach to mock up the datastructures
    #        instead of using the actual python files.
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.role_include import IncludeRole
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from units.mock.loader import DictDataLoader
    from units.mock.path import mock_unfrackpath_noop


# Generated at 2022-06-13 08:23:30.492612
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    data = [
        {
            'include_tasks': 'xyz',
            'loops': '{{bla_bla_bla}}',
            'block': [
                {
                    'include_tasks': 'abc',
                }
            ]
        }
    ]
    play = {
        'hosts': 'localhost',
        'gather_facts': 'no',
        'tasks': data
    }

    pb = Playbook.load(play, variable_manager=None, loader=None)
    assert isinstance(pb, Playbook)

    pb._entries[0].associate_with_play(pb)
    assert pb._entries[0].get_vars() == dict()
    assert pb._entries[0].get_dep_chain() == list()


# Generated at 2022-06-13 08:23:31.193691
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    pass

# Generated at 2022-06-13 08:23:32.288996
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    # TODO : add some unit test
    pass

# Generated at 2022-06-13 08:23:41.666467
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.role_include import IncludeRole
    from ansible.playbook.role import Role
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.handler_task_include import HandlerTaskInclude
    from ansible.playbook.handler import Handler
    from ansible.playbook.task import Task

    variable_manager = VariableManager()
    loader = DataLoader()
    play = Play()
    play._variable_manager = variable_manager
    play._loader = loader

    include_task = dict(
        include="test_include_task"
    )

    import_task = dict(
        import_task="test_import_task"
    )

    include

# Generated at 2022-06-13 08:23:53.482232
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.play import Play
    from tests.unit.playbook.common import MockLoader

    # sample tasks
    task = {'name': 'task name', 'action': 'action name'}

    # sample role
    role = {
        'role': 'role name',
        'import_tasks': 'role_tasks.yml'
    }

    # sample nested block with two tasks
    block = {
        'block': [
            task,
            task
        ]
    }

    tasks = [role, block]

    mock_loader = MockLoader()


# Generated at 2022-06-13 08:24:09.609129
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from collections import namedtuple
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.role_include import IncludeRole
    from ansible.playbook.play import Play
    from ansible.module_utils._text import to_bytes
    from ansible.vars import VariableManager
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.dataloader import DataLoader

    TaskArgs = namedtuple('TaskArgs', ['action', 'args', 'delegate_to'])
    loader = DataLoader()
    variable_manager = VariableManager()
    play = Play()


# Generated at 2022-06-13 08:24:39.953571
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    class Object:
        pass
    t = Object()
    t.tags = []
    t.when = []
    t.name = 'test'
    t.args = []
    t.action = 'debug'
    t.register = []
    t.notify = []
    t.changed_when = []
    t.failed_when = []
    t.always_run = False
    t.delegate_to = []
    t.delegate_facts = False
    t.loop = []
    t.loop_args = {}
    t.loop_with_items = {}
    t.notified_by = []
    t.no_log = False
    t.run_once = False
    t.until = []
    t.retries = 0
    t.delay = 0
    t.first_available_

# Generated at 2022-06-13 08:24:49.017399
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible import constants as C
    from ansible.utils.display import Display
    display = Display()

    ds = [{'include_tasks': {'name': 'test1', 'host': 'host2'}},
          {'import_tasks': {'name': 'test1', 'host': 'host2'}}
          ]
    block = None
    role = None
    task_include = None
    use_handlers = False
    variable_manager = None
    loader = None
    result = load_list_of_tasks(ds, block, role, task_include, use_handlers)
    assert len(result) == 1

    ds = [{'include': {'name': 'test1', 'host': 'host2'}}]
    block = None
    role = None
    task_include

# Generated at 2022-06-13 08:24:50.553952
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    # Intentionally fails for now
    assert False

# Generated at 2022-06-13 08:25:04.651840
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    task_ds = []
    play = 1
    block = 2
    role = 3
    task_include = 4
    use_handlers = 5
    variable_manager = 6
    loader = 7
    list_task_obj = load_list_of_tasks(task_ds, play, block, role, task_include, use_handlers, variable_manager, loader)
    assert isinstance(list_task_obj, list)
    assert not list_task_obj
    task_ds = [{}]
    list_task_obj = load_list_of_tasks(task_ds, play, block, role, task_include, use_handlers, variable_manager, loader)
    assert isinstance(list_task_obj, list)
    assert not list_task_obj

# Generated at 2022-06-13 08:25:15.639587
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    # test parent block import
    pb = Mock()
    pb.vars = dict()
    # test role passed in
    r = Mock()
    r.name = "test_role"
    r.tasks_path = "roles/test_role/tasks/"
    # test task include passed in
    ti = Mock()
    ti.args = dict()
    # test variable manager
    v = Mock()
    vars = dict()
    vars[u'a'] = u'b'
    vars[u'c'] = u'd'
    vars[u'e'] = [u'f', u'g']
    v.get_vars.return_value = vars
    c = Mock()
    c.DEFAULT_HANDLERS_PATH = "default/handlers/"

# Generated at 2022-06-13 08:25:29.189402
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.parsing.mod_args import ModuleArgsParser


# Generated at 2022-06-13 08:25:36.831607
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    variable_manager = VariableManager() # FIXME: Make a fake vars manager?
    loader = DataLoader()
    play = Play()
    t = load_list_of_tasks(ds=[{'include_tasks': 'foobar.yml'}], play=play, variable_manager=variable_manager, loader=loader)
    assert len(t) == 1
    assert t[0].args['_raw_params'] == 'foobar.yml'

# Generated at 2022-06-13 08:25:37.712714
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    assert True

# Generated at 2022-06-13 08:25:42.619966
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
  # In this test, we are testing that the function will return a list of tasks,
  # each of which have a name and a module
  task_list = load_list_of_tasks([{'include_role': {'name': 'some_role', 'static': False, 'tasks_from': 'main'}},
                                  {'include_tasks': 'super_playbook.yml'}], None, None, None, False, None, None)
  assert task_list[0].name == 'some_role'
  assert task_list[0].module == 'include_role'
  assert task_list[1].name == 'super_playbook.yml'
  assert task_list[1].module == 'include_tasks'
  # Also want to test that it raises an error if you pass in a task that


# Generated at 2022-06-13 08:25:55.513913
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():

    from ansible.playbook.playbook_include import PlaybookInclude
    from ansible.playbook.play import Play

    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    inv_obj = InventoryManager(loader=loader, sources=[])
    variable_manager = VariableManager(loader=loader, inventory=inv_obj)


# Generated at 2022-06-13 08:26:27.537965
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    ds = [{
        'action': 'include_tasks',
        'static': 'yes'},
        {
        'action': 'shell',
        'args': 'cat foo'}
        ]
    variable_manager = VariableManager()
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=['localhost'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    variable_manager.set_inventory(inventory)
    play_context = PlayContext(variable_manager=variable_manager)

# Generated at 2022-06-13 08:26:39.798981
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.block import Block
    from ansible.playbook.handler import Handler
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.role_include import IncludeRole
    from ansible.playbook.handler_task_include import HandlerTaskInclude
    from ansible.template import Templar
    # we import here to prevent a circular dependency with imports
    import ansible.playbook
    import ansible.playbook.play
    import ansible.playbook.role


# Generated at 2022-06-13 08:26:48.099935
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    '''
    Here we test the load_list_of_tasks function.
    We are going to use a static include and ensure it is loaded statically
    We are going to use a role include and ensure it is loaded statically because
    there is no loop.
    We are also going to use an include_role with a loop, and ensure that it is not
    loaded statically
    '''

    # for testing, it is we are using the base_type
    class TestObject(object):
        def __init__(self, **kwargs):
            self.__dict__.update(kwargs)
            self.tasks = []

        def __setattr__(self, name, value):
            '''
            When we set an attr, we are also going to put it
            in the __dict__ so it is returned in the future
            '''


# Generated at 2022-06-13 08:26:55.223418
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.play import Play
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.playbook_executor import PlaybookExecutor

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = Inventory(loader=loader, variable_manager=variable_manager)
    variable_manager.set_inventory(inventory)

# Generated at 2022-06-13 08:27:07.017071
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():

    from ansible.playbook.play import Play

    class MockLoader():

        def path_dwim_relative(self, basedir, dir_path, filepath):
            return dir_path + '/' + filepath

        def path_dwim(self, filepath):
            return filepath

        def get_basedir(self):
            return './'

        def load_from_file(self, filepath):
            return [{'i_am': 'the_template'}]

    class MockVariableManager():

        def get_vars(self, play=None, task=None):
            return {}

    class MockInclude():

        def __init__(self, args):
            self.args = args
            self.statically_loaded = False

    loader = MockLoader()
    variable_manager = MockVariableManager()

# Generated at 2022-06-13 08:27:19.189922
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    if not os.path.exists(os.path.join(os.path.dirname(__file__), '../lib/ansible/playbook/play_context.py')):
        pytest.skip("not a full checkout, unable to run")
    import ansible.playbook.play_context
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    dl = DataLoader()
    inventory = InventoryManager(loader=dl, sources=['localhost,'])
    variable_manager = VariableManager(loader=dl, inventory=inventory)
    example_data = [{"name": "Test Playbook"}, {'block': 3}]
    # Test that type exists, and accesses the private method
    # Test fails as it

# Generated at 2022-06-13 08:27:26.749800
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    ds = [
        {'action': 'include_tasks', 'args': {}},
        {'action': 'set_fact', 'args': {'bar': '1'}},
        {'action': 'import_tasks', 'args': {}}
    ]
    play = Mock()
    block = Mock()
    role = Mock()
    task_include = Mock()
    use_handlers = Mock()
    variable_manager = Mock()
    loader = Mock()

    assert len(load_list_of_tasks(ds, play=play, block=block, role=role, task_include=task_include, use_handlers=use_handlers, variable_manager=variable_manager, loader=loader)) == 3

# Generated at 2022-06-13 08:27:35.913232
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude

    # Generate a single task
    ds = dict(action=dict(module='testmodule'))
    task_list = load_list_of_tasks([ds], play=None, block=None, role=None, task_include=None, use_handlers=False, variable_manager=None, loader=None)
    assert task_list[0].action == 'testmodule'

    # Generate a block of tasks
    ds = [
        dict(action=dict(module='testmodule')),
        dict(action=dict(module='testmodule'))
    ]

# Generated at 2022-06-13 08:27:50.023731
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.role_include import IncludeRole
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude

    ds = [
        {
            'import_role': {
                'name': 'webapp'
            }
        },
        {
            'include_role': {
                'name': 'webservers',
                'static': True
            }
        }
    ]
    task_list = load_list_of_tasks(ds)
    assert len(task_list) == 2
    assert isinstance(task_list[0], IncludeRole)
    assert isinstance(task_list[1], TaskInclude)
    assert task_list[0].static is False
    assert task_list[1].static is True

    task_list

# Generated at 2022-06-13 08:28:00.984822
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    # test_ds is an object of class Play
    test_ds = Play()
    test_ds.append(Task())
    test_ds.append(Task())
    test_ds[0].args['name'] = 'test task'
    fun_load_list_of_tasks = load_list_of_tasks(test_ds)
    assert fun_load_list_of_tasks[0].args['name'] == 'test task'
    assert fun_load_list_of_tasks[1].args['name'] == 'no_name'
    print("Load list of tasks passed")

# Generated at 2022-06-13 08:28:34.767794
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.task import Task
    from ansible.utils.vars import combine_vars
    from ansible.vars.manager import VariableManager
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins.loader import add_all_plugin_dirs

    add_all_plugin_dirs()

    my_play_context = PlayContext()

    my_vars_manager = VariableManager()


# Generated at 2022-06-13 08:28:43.113621
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    assert load_list_of_tasks({'foo': 'bar'}, None, None, None, None, None, None) == []
    assert load_list_of_tasks([{'foo': 'bar'}], None, None, None, None, None, None) == []
    assert load_list_of_tasks(None, None, None, None, None, None, None) == []


__ALL__ = [
    'load_list_of_blocks',
    'load_list_of_tasks',
]

# Generated at 2022-06-13 08:28:52.758830
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    """
    load_list_of_tasks unit test
    """

    def check_task_list(task_list, expected_classes):
        """
        Check that all the tasks in the list are of the expected type
        """

        for task, expected_class in zip(task_list, expected_classes):
            assert isinstance(task, expected_class)

    # Test 1
    test_data = """
    - name: test1
      debug: var=foo
      delegate_to: localhost

    - include: other_tasks.yml
      static: yes
    """

    test_list = yaml.load(test_data, Loader=AnsibleLoader)
    assert test_list is not None

    test_task_list = load_list_of_tasks(test_list, None)
    check_

# Generated at 2022-06-13 08:29:02.866666
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.play import Play
    from ansible.playbook.playbook import Playbook
    from ansible.playbook.role import ROLE_CACHE

    # Get the playbook object
    file_path = CONFIG.get_config_value('DEFAULT', 'role_path')
    playbook = Playbook.load(file_path + "/../test/test_playbook.yml")
    play = Play.load(playbook._entries[0], variable_manager=playbook.get_variable_manager(), loader=playbook._loader)
    loader = DataLoader()

    # Ensure that the single 'file' exists
    assert os.path.exists(file_path + "/../test/test_playbook.yml")

    # Ensure that the 'role' cache is populated

# Generated at 2022-06-13 08:29:15.063280
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.play import Play
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.handler_task_include import HandlerTaskInclude
    from ansible.vars.manager import VariableManager
    import ansible.constants as C
    from ansible.template import Templar
    from ansible.errors import AnsibleParserError
    import pytest

    hosts = dict(localhost=dict(host_name="localhost", port=22))
    play_source = dict(name="test play", hosts=["localhost"], gather_facts="no")
    play = Play().load(play_source, variable_manager=VariableManager(), loader=None)

# Generated at 2022-06-13 08:29:29.602848
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook import Play
    from ansible.playbook.block import Block
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.role import Role

    play_ds = dict(
        name = 'Test Play',
        hosts = 'all',
    )

    play = Play().load(play_ds, loader=DictDataLoader(), variable_manager=VariableManager())
    play.post_validate(templar=None)
    block_ds = dict(
        block = dict(
            tasks = [
                dict(debug=dict(msg='hello world')),
                dict(debug=dict(msg='hello world')),
                dict(debug=dict(msg='hello world')),
            ]
        )
    )


# Generated at 2022-06-13 08:29:30.309554
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    pass



# Generated at 2022-06-13 08:29:38.822994
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    ''' Test load_list_of_tasks function '''

    ###############
    # Register dict
    ###############
    register_dict = dict(
        register_name='register_test_1'
    )

    ################
    # Debug dict
    ################
    debug_dict = dict(
        debug_var_1='debug_test_1',
    )

    ################
    # Block dict
    ################
    block_dict = dict(
        block='block_dict',
        tasks=[
            dict(
                debug=debug_dict
            )
        ]
    )

    ################
    # When dict
    ################
    when_dict = dict(
            when_var='when_test'
    )

    ################


# Generated at 2022-06-13 08:29:47.849040
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.inventory import Inventory
    from ansible.vars import VariableManager
    from ansible.inventory.host import Host
    host = Host(name="test")
    ds = []
    ds.append({'action': 'setup'})
    ds.append({'action': 'debug', 'msg': '{{var1}} {{var2}}', 'var1': 'var1', 'var2': 'var2'})
    ds.append({'action': 'include', 'include': 'file1.yml'})
    ds.append({'action': 'include_role', 'name': 'role1', 'tasks_from': 'main'})

# Generated at 2022-06-13 08:29:57.361558
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.task import Task
    from ansible.playbook import Playbook
    from ansible.playbook.play_context import PlayContext
    from ansible.inventory import Inventory
    from ansible.vars import VariableManager

    yaml_data = '''
    - name: echo hello
      debug:
        msg: hello
        verbosity: 2
    - name: include_tasks
      include_tasks: ./static_include.yml
    - name: import_tasks
      import_tasks: ./static_include.yml
    - name: include_role
      include_role:
         name: some_role
    - name: import_role
      import_role:
         name: some_role
    '''
    #