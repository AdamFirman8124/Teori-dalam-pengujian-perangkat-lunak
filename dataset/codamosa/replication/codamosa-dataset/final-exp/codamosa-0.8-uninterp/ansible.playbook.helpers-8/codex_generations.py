

# Generated at 2022-06-13 08:21:03.681768
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.task import Task
    # Test with good_data
    data = [{'arg1': 'val1'}, {'arg2': 'val2'}]
    task_list = load_list_of_tasks(data)
    assert(len(task_list)) == 2
    assert(all(isinstance(item, Task) for item in task_list))
    # Test with bad_data
    data = {'arg1': 'val1'}
    try:
        load_list_of_tasks(data)
    except AnsibleAssertionError as e:
        assert 'must be a list' in str(e)
    # Test with None

# Generated at 2022-06-13 08:21:10.905327
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    import os, sys, tempfile

    from ansible.errors import AnsibleParserError
    from ansible.playbook import Playbook
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.display import Display
    from ansible.utils.vars import combine_vars
    from ansible.utils.vars import merge_hash
    from ansible.vars import VariableManager

    display = Display()
    loader = DataLoader()
    variable_manager = VariableManager()
    merge_hash({'foo': 'bar'}, {'baz': 'bas', 'foo': 'not_bar'})

    playbook_path = tempfile.mkdtemp()
    extra_vars = {'debug': True}

# Generated at 2022-06-13 08:21:23.618819
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():

    from ansible.playbook.block import Block
    from ansible.playbook.handler import Handler
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.role_include import IncludeRole
    from ansible.playbook.handler_task_include import HandlerTaskInclude

    variable_manager = MagicMock()
    loader = MagicMock()

    # None input, should get empty list
    print("load_list_of_tasks(None, MagicMock(), MagicMock())")
    task_list = load_list_of_tasks(None, MagicMock(), MagicMock(), MagicMock(), MagicMock(), False, MagicMock(), MagicMock())
    assert(len(task_list) == 0)

    # List input,

# Generated at 2022-06-13 08:21:32.656516
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.play_context import PlayContext
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from collections import namedtuple

    Options = namedtuple('Options', ['connection', 'module_path', 'forks', 'become', 'become_method', 'become_user', 'check', 'diff'])
    options = Options(connection='paramiko', module_path=None, forks=100, become=None, become_method=None, become_user=None, check=False, diff=False)
    loader = DataLoader()
    passwords = {}
    inventory = InventoryManager(loader=loader, sources=["localhost"])

# Generated at 2022-06-13 08:21:43.121496
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    # test with a normal list of tasks
    ds = [{u'name': u'TASK_TEST_1'}, {u'name': u'TASK_TEST_2'}]
    task_list = load_list_of_tasks(ds, None, None, None, None, False, None, None)
    assert task_list[0].name == u'TASK_TEST_1'
    assert task_list[1].name == u'TASK_TEST_2'

    # test with a list that contains an include task
    ds = [{u'name': u'TASK_TEST_1'},
          {u'include': {u'name': u'TASK_TEST_INCLUDE'}}]
    task_list = load_list_of

# Generated at 2022-06-13 08:21:52.842118
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    for (test_input, expected) in load_list_of_tasks_cases:
        if isinstance(test_input, tuple):
            # We expect a tuple for broken cases
            try:
                load_list_of_tasks(test_input)
            except Exception as e:
                if type(e) != expected:
                    raise Exception(
                        'Unexpected exception type "{0}" while loading {1} '
                        'Expected "{2}"'.format(type(e), test_input, expected)
                    )
        else:
            actual = load_list_of_tasks(test_input)

# Generated at 2022-06-13 08:22:02.429215
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    """
    Unit test for load_list_of_tasks

    """
    import ansible.playbook.play
    from ansible.playbook.play_context import PlayContext
    import ansible.playbook.task
    import ansible.inventory.manager
    import ansible.parsing.dataloader
    import ansible.vars.manager
    import ansible.template.template
    import ansible.template.varsmodule
    import ansible.constants
    import ansible.inventory.host
    from ansible.parsing.yaml.objects import AnsibleMapping

    # mock _load_list_of_tasks

# Generated at 2022-06-13 08:22:16.618289
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.play import Play
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(
        argument_spec={},
        supports_check_mode=True
    )
    play = Play().load(dict(
        name="Ansible Play",
        hosts='localhost',
        gather_facts='no',
        tasks=[
            dict(action=dict(module='shell', args='ls'), register='shell_out'),
            dict(action=dict(module='debug', args=dict(msg='{{shell_out.stdout}}')))
        ]
    ), variable_manager=module._variable_manager, loader=module._loader)

# Generated at 2022-06-13 08:22:32.091220
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    ansible_vars = {}
    ansible_inventory = {}
    ansible_playbook = {}
    ansible_playbook['hosts'] = ["localhost"]

    if 'foo' in ansible_playbook:
        ansible_playbook.pop('foo')

    # Ansible variables
    if 'foo' in ansible_vars:
        ansible_vars.pop('foo')

    # Ansible inventory
    ansible_inventory['localhost'] = {}
    ansible_inventory['localhost']["hostname"] = "localhost"
    ansible_inventory['localhost']["ansible_connection"] = "local"
    if 'foo' in ansible_inventory['localhost']:
        ansible_inventory['localhost'].pop('foo')

    # Ansible playbook

# Generated at 2022-06-13 08:22:38.281676
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():

    # Code to run here
    the_list = [
        {
            'name': 'print hello'
        },
        {
            'block': [
                {
                    'name': 'print hello'
                }
            ]
        },
        {
            'name': 'print hello'
        }
    ]

    results = load_list_of_tasks(the_list)
    assert len(results) == 3
    assert isinstance(results[0], Task)
    assert isinstance(results[1], Block)
    assert isinstance(results[2], Task)

# Generated at 2022-06-13 08:23:06.295156
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.play import Play


# Generated at 2022-06-13 08:23:17.057159
# Unit test for function load_list_of_roles
def test_load_list_of_roles():
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.role.include import RoleInclude
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.task_queue_manager import TaskQueueManager

    play_source = dict(
        name="Ansible Play",
        hosts='localhost',
        gather_facts='no',
        tasks=[
            dict(action=dict(module='setup', args=dict()))
        ]
    )

    # Create a temporary file on the local host, which will be used as a inventory file
    fd, inv_path = tempfile.mkstemp()

# Generated at 2022-06-13 08:23:24.041399
# Unit test for function load_list_of_tasks

# Generated at 2022-06-13 08:23:35.752900
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    # Unit tests to make sure we don't regress, to ensure that the
    # function works we do a static test, by mocking the return of
    # all functions that are called, and making sure that the right
    # objects are returned.

    # Mocked objects
    test_task_ds = {
        'include': 'foo'
    }

    test_task = [
        {
            'include': 'foo'
        },
        {
            'include': 'bar'
        }
    ]

    test_role = {
        'include': 'baz'
    }


# Generated at 2022-06-13 08:23:45.386203
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
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.playbook_executor import PlaybookExecutor
    import pytest
    # Create a mock play object
    loader = DataLoader()

# Generated at 2022-06-13 08:23:56.091532
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins.loader import action_loader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.playbook.play import Play
    from ansible.playbook.role.include import IncludeRole
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude

    # Get the action plugin object

# Generated at 2022-06-13 08:23:58.814238
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    # TODO: implement test_load_list_of_tasks
    assert(False)



# Generated at 2022-06-13 08:24:13.378596
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    import os
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.handler import Handler
    from ansible.playbook.handler_task_include import HandlerTaskInclude
    from ansible.playbook.role_include import IncludeRole
    data = [{}, {}]
    # Test load_list_of_tasks with an empty list
    assert load_list_of_tasks(data, None, None, False, None) == []
    # Test load_list_of_tasks with a list and a block
    play = {}
    block = {}
    task_list = []

# Generated at 2022-06-13 08:24:25.787269
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, sources=["/etc/ansible/hosts"])
    variable_manager.set_inventory(inventory)
    context = PlayContext()


# Generated at 2022-06-13 08:24:34.365598
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    '''Test loads a list of tasks from a text file'''
    loader = DictDataLoader({
        'tasks.yml': '''
        - debug:
            msg: "hello"
        - debug:
            msg: "goodbye"
        ''',
        'handlers/main.yml': '''
        - debug:
            msg: "hello"
        - debug:
            msg: "goodbye"
        '''
    })
    variable_manager = VariableManager()
    # see play.py for the play object
    play1 = None
    play2 = None
    display = Display()
    display.verbosity = 2
    # instantiate a test host
    host = Host('h1')
    # load the yaml file

# Generated at 2022-06-13 08:24:44.642193
# Unit test for function load_list_of_roles
def test_load_list_of_roles():
    assert load_list_of_roles([], None) == list()



# Generated at 2022-06-13 08:24:59.862093
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    arg = [{'block': [], 'name': 'include_vars'}]
    import ansible.parsing.vault
    from ansible.parsing.vault import VaultLib
    from ansible.plugins.loader import inventory_loader, module_loader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor

    inventory = InventoryManager(play_context, loader, sources=None)

    variable_manager = VariableManager(loader=loader, inventory=inventory)
    loader = DataLoader()
    vault_

# Generated at 2022-06-13 08:25:09.786508
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.play_context import PlayContext

    def _load_list_of_tasks_role_mock(loader, role_name, role_relative_path):
        return 'role_name'

    def _load_list_of_tasks_role_mock_raise(loader, role_name, role_relative_path):
        raise AnsibleError('role %s not found' % role_name)

    def _load_list_of_tasks_find_file_mock(filename):
        if filename == 'roles/role_name/tasks/main.yml':
            return filename
        else:
            raise AnsibleFileNotFound('file not found')


# Generated at 2022-06-13 08:25:10.628665
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    pass


# Generated at 2022-06-13 08:25:19.070793
# Unit test for function load_list_of_blocks
def test_load_list_of_blocks():
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.role import Role
    from ansible.playbook.role_context import RoleContext
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.vars.manager import VariableManager
    from ansible.vars.hostvars import HostVars


# Generated at 2022-06-13 08:25:19.880868
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    # TODO
    pass

# Generated at 2022-06-13 08:25:26.489273
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    # In the test, we don't want to get too much in the real
    # ansible code, so we will fake the module.
    # But we need some other part of the code to continue,
    # so we just import some of the basic classes that
    # we need in the test.
    #
    # We only need the main object Task to have the right type
    # so we can instanciate a fake.
    #
    # We also need the main object VariableManager and DataLoader
    # with a limited method set so that we can build a fake
    # instance of them.
    from ansible.utils.display import Display
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.task import Task

# Generated at 2022-06-13 08:25:39.871447
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    import ansible.config
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    import ansible.inventory.manager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.playbook.role_include import IncludeRole
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.handler_task_include import HandlerTaskInclude
    from ansible.playbook.task import Task
    from ansible.playbook.handler import Handler
    from ansible.playbook.block import Block
    from ansible.playbook.playbook_include import PlaybookInclude

    args_parser = ModuleArgsParser({"foo": 3})

# Generated at 2022-06-13 08:25:40.895725
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    # TODO
    pass


# Generated at 2022-06-13 08:25:48.416476
# Unit test for function load_list_of_blocks
def test_load_list_of_blocks():
    from ansible.playbook.play import Play
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.handler import Handler
    from ansible.playbook.role import Role
    from ansible.parsing.dataloader import DataLoader

    play_ds = {}
    play = Play.load(
        play_ds,
        variable_manager=None,
        loader=DataLoader(),
    )

    parent_block = None
    role = Role()
    task_include = None
    use_handlers = False
    variable_manager = None
    loader = DataLoader()


# Generated at 2022-06-13 08:25:57.891625
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    pass



# Generated at 2022-06-13 08:26:07.340633
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():

    ds = [{'action': 'ping'}]
    task_list = load_list_of_tasks(ds, None, None, None, None, False, None, None)
    assert isinstance(task_list[0], Task)
    assert task_list[0].action == 'ping'
    assert len(task_list) == 1

    ds = [{'include': 'foobar.yaml'}]
    task_list = load_list_of_tasks(ds, None, None, None, None, False, None, None)
    assert isinstance(task_list[0], TaskInclude)
    assert task_list[0]._role is None
    assert task_list[0].construct_include_params() == {'_raw_params': 'foobar.yaml'}

    role = Role

# Generated at 2022-06-13 08:26:18.177735
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.block import Block
    from ansible.playbook.handler import Handler
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.role_include import IncludeRole
    from ansible.playbook.handler_task_include import HandlerTaskInclude
    from ansible.template import Templar
    def assert_task_list(task_list):
        assert isinstance(task_list, list)
        assert len(task_list) == 1
        assert isinstance(task_list[0], Block)
        assert len(task_list[0].block) == 1
        assert isinstance(task_list[0].block[0], Task)

# Generated at 2022-06-13 08:26:18.855501
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    pass

# Generated at 2022-06-13 08:26:19.508852
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    pass

# Generated at 2022-06-13 08:26:25.993413
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():

    import pytest

    with pytest.raises(AnsibleAssertionError):
        load_list_of_tasks({}, None)

    with pytest.raises(AnsibleAssertionError):
        load_list_of_tasks(['a'], None)

    with pytest.raises(AnsibleAssertionError):
        load_list_of_tasks([{'block': None}], None)

    with pytest.raises(AnsibleAssertionError):
        load_list_of_tasks([{'block': 'a'}], None)

    with pytest.raises(AnsibleParserError):
        load_list_of_tasks([{'block': {'tasks': []}}], None)


# Generated at 2022-06-13 08:26:38.741395
# Unit test for function load_list_of_blocks
def test_load_list_of_blocks():

    from ansible.playbook.block import Block

    blocks = [1, 2, 3]
    blocks_ds  = [2, 3, 4, 5]
    play = {'hosts': 'all'}
    parent_block = 1
    role = 2
    task_include = [1, 2]
    use_handlers = True
    variable_manager = 1
    loader = 1

    load_list_of_blocks(blocks_ds, play, parent_block, role, task_include,
                        use_handlers, variable_manager, loader)

    # check that Block.load is called and that load_list_of_blocks return
    # loaded blocks
    assert Block.load.call_count == len(blocks_ds)
    # check if load return it's instance and if it's instance of Block

# Generated at 2022-06-13 08:26:49.285232
# Unit test for function load_list_of_tasks

# Generated at 2022-06-13 08:26:50.366118
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    pass
    # FIXME

# Generated at 2022-06-13 08:27:02.495564
# Unit test for function load_list_of_roles
def test_load_list_of_roles():
    from ansible.playbook.play_context import PlayContext
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.tasks import TASK_CACHE
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.template import Templar

    loader = DataLoader()

    inventory = InventoryManager(loader=loader, sources=['/etc/ansible/hosts'])
    print(inventory.get_hosts())

    vars_manager = VariableManager(loader=loader, inventory=inventory)
    print(vars_manager.get_vars(play=None))


# Generated at 2022-06-13 08:27:26.359971
# Unit test for function load_list_of_blocks
def test_load_list_of_blocks():
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.playbook import PlayContext

    variable_manager = VariableManager()
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources='')
    variable_manager.set_inventory(inventory)

    play_context = PlayContext()
    play_context.network_os = 'junos' # Dummy value

# Generated at 2022-06-13 08:27:35.675340
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.play import Play
    from ansible.playbook.included_file import IncludedFile
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.vars.unsafe_proxy import wrap_var
    from ansible.parsing.dataloader import DataLoader
    import tempfile
    import shutil
    import os
    from ansible.vars.hostvars import HostVars
    from ansible.vars.unsafe_proxy import wrap_var


# Generated at 2022-06-13 08:27:49.864643
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.block import Block
    from ansible.playbook.role.include import IncludeRole
    from ansible.playbook.task.include import TaskInclude
    from ansible.playbook.task import Task
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.handler import Handler
    from ansible.plugins.loader import get_all_plugin_loaders
    from ansible.template import Templar
    from ansible.vars import VariableManager

    class FakeRole:
        def __init__(self):
            self._role_path = "/dev/null"

    class FakeTaskInclude:
        def __init__(self):
            self._role = FakeRole()

    # Test loading list of tasks with empty list
    load

# Generated at 2022-06-13 08:27:59.578319
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    """ This is a unit test for load_list_of_tasks, it uses the test data
        in the 'data' directory to test against the behavior of the function.
        The tests are intended to fail so that any updates to the
        load_list_of_tasks function will be tested.
    """
    data_dir = os.path.join(os.path.dirname(__file__), 'data/load_list_of_tasks')
    failed = 0
    # list of files to check
    # file_list = ['basic.yml'] # , 'fail1.yml', 'fail2.yml']
    file_list = ['included_role_static.yml']
    # file_list = [f for f in os.listdir(data_dir) if f.endswith('.yml')]


# Generated at 2022-06-13 08:28:11.556404
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.module_utils.common._collections_compat import Mapping, MutableSequence
    from ansible.playbook.play import Play
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.handler import Handler
    from ansible.playbook.role_include import IncludeRole
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.handler_task_include import HandlerTaskInclude
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.vars.resolver import Failer
    failer = Failer()
    variable_manager = VariableManager(resolver=failer)

# Generated at 2022-06-13 08:28:25.668856
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    """
    Test load_list_of_tasks method
    """
    import os
    from yaml.dumper import Dumper
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.vars.hostvars import HostVars

    loader = DictDataLoader({"": {"hosts": ["localhost"], "vars": {"foo": "bar"}}})

# Generated at 2022-06-13 08:28:38.851788
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    # Unit test for function load_list_of_tasks
    def test_dummy_function():
        pass
    display = test_dummy_function
    loader = test_dummy_function
    class Test_Task(object):
        def __init__(self, action):
            self.action = action
        def load(self, yaml_obj, loader=loader, templar=test_dummy_function):
            return Test_Task(yaml_obj['name'])
        def copy(self, exclude_parent=True):
            return Test_Task(self.action)
    class Test_Role(object):
        def __init__(self, name):
            self.name = name
    class Test_Play(object):
        def __init__(self, name):
            self.name = name

# Generated at 2022-06-13 08:28:48.495005
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.block import Block
    from ansible.playbook.handler import Handler
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.role_include import IncludeRole
    from ansible.playbook.handler_task_include import HandlerTaskInclude
    from ansible.template import Templar
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.plugins.loader import fragment_loader, action_loader, cache_loader

# Generated at 2022-06-13 08:28:49.654054
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    # TODO
    assert True

# Generated at 2022-06-13 08:28:56.437255
# Unit test for function load_list_of_roles
def test_load_list_of_roles():
    def create_ds_for_role(r):
        m = dict(role=r)
        return m

    ds = [create_ds_for_role('foo'), create_ds_for_role('bar')]
    assert load_list_of_roles(ds, None) == [RoleInclude(role='foo'), RoleInclude(role='bar')]

# Generated at 2022-06-13 08:29:16.017934
# Unit test for function load_list_of_roles
def test_load_list_of_roles():
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager

    loader = DataLoader()
    play_context = PlayContext()
    inventory = InventoryManager(loader=loader, sources='localhost,')
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    roledef = RoleDefinition()
    roledefs = load_list_of_roles([roledef], play_context, current_role_path='/etc',
                                  variable_manager=variable_manager, loader=loader)
    assert isinstance(roledefs, list)

# Generated at 2022-06-13 08:29:30.497508
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.role_include import IncludeRole
    from ansible.template import Templar
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from ansible.module_utils._text import to_text
    from ansible.playbook.play_context import PlayContext
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    #import ansible.constants as C
    from ansible.playbook.play import Play
    #import ansible.playbook.playbook as playbook
    #import ansible.playbook.block as block
    play_source =  dict

# Generated at 2022-06-13 08:29:38.914139
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    import os
    loader = DictDataLoader({
        os.path.join('test', 'a.yml'): """
        - a
        """,
        os.path.join('test', 'b.yml'): """
        - b
        """,
        os.path.join('test', 'c.yml'): """
        - c
        """,
        os.path.join('test', 'd.yml'): """
        - d
        """
    })
    variable_manager = VariableManager()
    variable_manager.set_inventory(Inventory(loader=loader, variable_manager=variable_manager))

# Generated at 2022-06-13 08:29:44.921613
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    #pylint: disable=invalid-name
    schema = '''
        action: import_tasks
        static: yes
        file: /playbooks/vars/ssh_def.yml
    '''
    results = load_list_of_tasks(schema)
    assert len(results) == 1, results
    assert 'static' in results[0].args, results[0].args
    #pylint: enable=invalid-name


# Generated at 2022-06-13 08:29:50.360400
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    def _load_list_of_tasks(ds):
        class Play:
            pass
        return load_list_of_tasks(ds, Play)
    assert len(_load_list_of_tasks([])) == 0
    assert len(_load_list_of_tasks([{'include': 'foo'}])) == 1
    assert len(_load_list_of_tasks([{'block': [{'debug': 'foo'}]}])) == 1
    # This is an example of list of blocks
    assert len(_load_list_of_tasks([{'debug': 'foo'}, {'debug': 'bar'}])) == 1
    # This is an example of 2 implicit blocks

# Generated at 2022-06-13 08:30:00.660231
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.play_context import PlayContext
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    variable_manager = VariableManager()
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=["localhost,"],)
    variable_manager.set_inventory(inventory)

    host = inventory.get_host(u'localhost')

    play_context = PlayContext()
    play_context._hostvars = dict()
    play_context._hostvars[host] = dict()
    play_context.remote_addr = "127.0.0.1"
    play_context.network_os = "linux"

    host.set_variable_manager(variable_manager)
    host

# Generated at 2022-06-13 08:30:01.306725
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    pass

# Generated at 2022-06-13 08:30:12.175402
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
  args_parser = ModuleArgsParser({u'include_vars': {u'name': u'my.var'}})
  (action, args, delegate_to) = args_parser.parse(skip_action_validation=True)
  assert action == u'include_vars'
  assert args == {u'name': u'my.var'}
  assert delegate_to == None

  args_parser = ModuleArgsParser({u'include': [u'file1.yml', {u'name': u'file2.yml'}, u'file3.yml']})
  (action, args, delegate_to) = args_parser.parse(skip_action_validation=True)
  assert action == u'include'

# Generated at 2022-06-13 08:30:23.567787
# Unit test for function load_list_of_tasks
def test_load_list_of_tasks():
    from ansible.playbook.task import Task
    from ansible.playbook.play import Play
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.utils.vars import combine_vars
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    variable_manager = VariableManager()
    variable_manager._extra_vars = combine_vars(loader=loader, variables=None, include_prior=True)
    variable_manager._options_vars = variable_manager._extra_vars.copy()
    templar = Templar(loader, variable_manager)

# Generated at 2022-06-13 08:30:36.517177
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



    block = Block.load(
            [{'block': {}}],
            play=None,
            parent_block=None,
            role=None,
            task_include=None,
            use_handlers=False,
            variable_manager=None,
            loader=None,
        )



    task_ds = {'block': {}}