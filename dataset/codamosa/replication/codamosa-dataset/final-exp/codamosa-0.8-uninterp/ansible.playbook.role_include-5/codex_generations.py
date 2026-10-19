

# Generated at 2022-06-13 09:02:51.701290
# Unit test for method get_include_params of class IncludeRole

# Generated at 2022-06-13 09:03:02.511281
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    """
    Unit test for method get_block_list of class IncludeRole
    """
    from ansible.playbook.role import Role
    from ansible.playbook.role.include import RoleInclude
    from ansible.playbook.block import Block

    # Define class attributes
    IncludeRole._parent = Block()
    IncludeRole._role_name = 'test_role'
    IncludeRole._role_path = 'test_path'
    IncludeRole._from_files = {'tasks': 'test_tasks', 'vars': 'test_vars'}

    # Define the original class
    class OriginalIncludeRole(IncludeRole):
        pass

    # Copy the class and its attributes
    IncludeRole = OriginalIncludeRole.copy()

    # Assert class attributes
    assert IncludeRole._parent.__class__ == Original

# Generated at 2022-06-13 09:03:13.217279
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    # GIVEN
    display = Display()
    display.verbosity = 3
    display.color = 'never'
    display.set_option('diff')

    # WHEN
    role_include1 = IncludeRole.load(
        {'name': 'test', 'allow_duplicates': True, 'public': True},
        task_include=True
    )
    role_include2 = IncludeRole.load(
        {'role': 'test', 'apply': {'tags': ['all']}, 'rolespec_validate': False},
        task_include=True
    )
    role_include3 = IncludeRole.load(
        {'name': 'test', 'tags': ['all'], 'tasks_from': 'tasks/tasks_all.yml'},
        task_include=True
    )
    #

# Generated at 2022-06-13 09:03:13.848945
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    pass

# Generated at 2022-06-13 09:03:15.117699
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    pass


# Generated at 2022-06-13 09:03:20.351727
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.role import Role
    from ansible.playbook.play import Play

    block = Block()
    role = Role()
    task_include = TaskInclude()
    task = IncludeRole(block, role, task_include)
    task._role_name = "role_name"
    assert task.get_name() == 'role_name'

# Generated at 2022-06-13 09:03:31.210061
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task_include import TaskInclude
    from ansible.template import Templar
    from ansible.vars.manager import VarManager


# Generated at 2022-06-13 09:03:42.538824
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    from ansible.module_utils._text import to_bytes
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    import ansible.constants as C
    import os
    loader = DataLoader()
    options = {'verbosity': 0}
    passwords = {}
    inventory = InventoryManager(loader=loader, sources=['tests/ansible/testdata/includerole/inventory'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)


# Generated at 2022-06-13 09:03:52.777355
# Unit test for method get_include_params of class IncludeRole
def test_IncludeRole_get_include_params():
    class FakeRole:
        def __init__(self, name, role_path):
            self.get_name = lambda : name
            self._role_path = role_path

        def get_role_params(self):
            return {'foo_test':'bar_test'}

    a = IncludeRole()
    assert a.get_include_params() == {}

    a._parent_role = FakeRole('test_name', 'test_path')
    assert a.get_include_params() == {
        'foo_test': 'bar_test',
        'ansible_parent_role_names': ['test_name'],
        'ansible_parent_role_paths': ['test_path'],
    }

    b = IncludeRole()

# Generated at 2022-06-13 09:04:01.059410
# Unit test for method get_include_params of class IncludeRole
def test_IncludeRole_get_include_params():
    r1 = Role()
    r1.name = "role1"
    r1._role_path = "/path/to/role1"

    r2 = Role()
    r2.name = "role2"
    r2._role_path = "/path/to/role2"

    r2._parents = [r1, ]

    ir = IncludeRole()
    ir._parent_role = r2

    v = ir.get_include_params()
    assert v['role_name'] == 'role2'
    assert v['role_path'] == '/path/to/role2'
    assert v['ansible_parent_role_names'] == ['role2', 'role1']
    assert v['ansible_parent_role_paths'] == ['/path/to/role2', '/path/to/role1']


# Generated at 2022-06-13 09:04:11.634465
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    pass

# Generated at 2022-06-13 09:04:22.201466
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():

    """

    :return:
    """

    # ------------------------------
    # include_role yaml file
    # ------------------------------

# Generated at 2022-06-13 09:04:29.044678
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    from ansible.playbook.play import Play
    from ansible.playbook.role import Role
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.config.manager import ConfigManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.playbook_executor import PlaybookExecutor
    import os
    import sys

    # initialize needed object
    options = PlaybookExecutor.default_options()
    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = Inventory(loader=loader, variable_manager=variable_manager,
                          host_list='/etc/ansible/hosts')
    variable_manager.set

# Generated at 2022-06-13 09:04:39.347519
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():

    import sys
    from ansible.playbook.block import Block
    from ansible.playbook.role import Role
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject

    if sys.version_info[0] == 2:
        from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    else:
        from ansible.utils.unsafe_proxy import AnsibleUnsafeBytes as AnsibleUnsafeText

    # Unit test for utility function load
    # pre-defined value
    class RoleObjTest(AnsibleBaseYAMLObject):
        def __init__(self):
            self.args = {}
            self.action = 'include_role'

    block_obj = Block()
    block_obj.apply_provider_options = {"role":{}}
    role_obj

# Generated at 2022-06-13 09:04:47.428654
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=["localhost"])
    play_context = PlayContext()
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    block_list = IncludeRole.load(dict(name='test'), variable_manager=variable_manager, loader=loader)

    assert len(block_list) == 1

# Generated at 2022-06-13 09:04:58.058625
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.plugins.loader import PluginLoader
    from ansible.executor.playbook_executor import PlaybookExecutor

    from ansible.utils.display import Display
    display = Display()

# Generated at 2022-06-13 09:05:02.536547
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    ''' unit test for load method '''

    # Create a sample dict input data
    data = dict(
        apply=dict(
            tags=['tag1', 'tag2']
        ),
        include_tasks='tasks/main.yml',
        include_vars='vars/main.yml',
        include_defaults='defaults/main.yml',
        include_handlers='handlers/main.yml',
        name='my_role'
    )

    # Instantiate Block and Role classes
    bl = Block()
    r = Role()

    # Instantiate IncludeRole class
    i = IncludeRole(block=bl, role=r)

    # Create a sample dict for variable_manager
    variable_manager = dict()

    # Create a sample dict for loader
    loader = dict()

    # Test

# Generated at 2022-06-13 09:05:15.869240
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():

    # Test load with valid options
    data = {
        'include_role': {
            'name': 'test_role',
            'tasks_from': 'tasks/test.yml',
            'vars_from': 'vars/test.yml',
            'defaults_from': 'defaults/test.yml',
            'handlers_from': 'handlers/test.yml',
            'register': 'test',
            'allow_duplicates': True,
            'apply': {'a': '1'},
            'public': True,
            'block': {
                'name': 'test_block',
                'when': 'true'
            }
        }
    }
    ir = IncludeRole.load(data)
    assert isinstance(ir, IncludeRole)

    # Test load without name

# Generated at 2022-06-13 09:05:26.617623
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.playbook.play_context import PlayContext
    from ansible.inventory.manager import InventoryManager
    from ansible.executor.task_queue_manager import TaskQueueManager

    loader = DataLoader()
    variable_manager = VariableManager()
    play_context = PlayContext()
    inventory = InventoryManager(loader, variable_manager, play_context)
    play_context.become = True

    test_play = dict(
        name="Ansible Play",
        hosts='localhost',
        gather_facts='no',
        roles=['role1']
    )

    # create a task to include a role
    role_include = RoleInclude()

# Generated at 2022-06-13 09:05:32.854613
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    """
    Unit test for method load of class IncludeRole

    This is a regression test for the AnsibleParserError when a
    deprecation warning is raised during load.
    """
    display.display = lambda x, *args, **kwargs: x
    display.verbosity = 2

    data = dict(
        name="foo",
        role="{{ role }}",
    )
    block = Block()
    task_include = TaskInclude()
    task_include.action = "some-action"

    ir = IncludeRole.load(data, block, task_include=task_include)

    assert ir.name == "foo"
    assert ir.role == "{{ role }}"

# Generated at 2022-06-13 09:06:00.156523
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.template import Templar
    from ansible.errors import AnsibleParserError
    import os
    import tempfile
    import shutil

    # Create a temporary directory
    tmpdir = tempfile.mkdtemp()
    curdir = os.getcwd()


# Generated at 2022-06-13 09:06:08.770210
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    """Class IncludeRole: Method load_data function as expected
    """
    # This is the data to load
    data = {
        'include_role': 'toto',
        'name': 'toto',
        'apply': {
            "tags": [ "debug" ],
            "when": [ "debug" ]
        },
        'allow_duplicates': True,
        'public': True
    }

    # We create an empty IncludeRole object
    my_task = IncludeRole()

    # We load the data in it
    result = my_task.load_data(data)

    # We check that the good data has been loaded
    assert result.name == 'toto'
    assert result.action == 'include_role'
    assert result.allow_duplicates is True
    assert result.public is True

# Generated at 2022-06-13 09:06:17.150670
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():

    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.playbook.role.definition import RoleDefinition

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, sources=['127.0.0.1,'])
    play = Play().load(dict(
        name = "Ansible Play",
        hosts = 'all',
        gather_facts = 'no',
        tasks = [dict(action=dict(include_role=dict(name='foo')))]
    ), variable_manager=variable_manager, loader=loader)

    ir = play.get_tasks()[0]

    role_

# Generated at 2022-06-13 09:06:25.993894
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():

    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager

    from ansible_collections.notstdlib.moveitallout.tests.unit.mock.loader import DictDataLoader


# Generated at 2022-06-13 09:06:39.637927
# Unit test for method load of class IncludeRole

# Generated at 2022-06-13 09:06:51.285111
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():

    # block is Block
    # role is Role
    # task_include is TaskInclude
    # play is Play
    # variable_manager is VariableManager
    # loader is DataLoader
    # blocks is list of Block
    # handlers is list of Block

    # use a role to simulate an include_role
    role_name = 'database'
    role_path = 'roles/%s' % role_name
    role_path_full = '/home/mdelgado/Projects/ansible-roles-base/%s' % role_path
    handler_filename = 'handlers/main.yml'
    task_filename = 'tasks/main.yml'
    handler_filename_full = "%s/%s" % (role_path_full, handler_filename)

# Generated at 2022-06-13 09:07:02.429378
# Unit test for method get_include_params of class IncludeRole
def test_IncludeRole_get_include_params():
    import os
    import tempfile
    import unittest

    # ansible mocks
    display = Display()
    display.verbosity = 3
    display.columns = 80

    def fake_get_vars(play=None, task=None, host=None, othervars=None, use_cache=True):
        return dict()

    class FakeVarsManager(object):
        def get_vars(self, play=None, task=None, host=None, othervars=None, use_cache=True):
            return dict()

    # Test class
    class TestIncludeRole(unittest.TestCase):

        def setUp(self):
            self.varsManager = FakeVarsManager()
            self.tempPath = tempfile.mkdtemp()

# Generated at 2022-06-13 09:07:09.994232
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():

    context = dict(IncludeRole.VALID_ARGS)
    context['role'] = 'my_role'

    for key in context:
        # remove one argument at a time to test missing argument
        data = context.copy()
        del data[key]
        data['action'] = '- include_role'
        with pytest.raises(AnsibleParserError):
            IncludeRole.load(data)

    context['action'] = '- include_role'

    ir = IncludeRole.load(context)

    for key in context:
        # check if arguments are loaded correctly
        assert getattr(ir, key) == context[key]

# Generated at 2022-06-13 09:07:18.830670
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    display = Display()
    display.verbosity = 3

    # normal include_role
    data = dict(
        name="foo",
        tasks_from="../some_tasks.yml"
    )
    ir = IncludeRole.load(data)
    assert ir._from_files == dict(tasks="some_tasks.yml")
    assert ir.rolespec_validate
    assert ir._allow_duplicates

    # set apply
    data['apply'] = dict(bar="abc")
    ir = IncludeRole.load(data)
    assert ir._from_files == dict(tasks="some_tasks.yml")
    assert ir.rolespec_validate
    assert ir._allow_duplicates
    assert ir.apply == dict(bar="abc")

    # unknown option

# Generated at 2022-06-13 09:07:30.026693
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():

    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.vars.manager import VariableManager
    import sys
    import ansible.plugins.loader as module_loader

    # workaround to avoid failing on variable_manager in the host object
    variable_manager = VariableManager()
    variable_manager._fact_cache = {}
    variable_manager.set_fact_cache({"ansible_local": {"role_paths": ["roles/", "../"]}})
    variable_manager.set_fact_cache({"ansible_all_ipv4_addresses": ["1.2.3.4"]})

    play_context = PlayContext()


# Generated at 2022-06-13 09:08:18.849692
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    blocks = []
    this_block = Block.load(dict(
        tasks=[
            dict(action=dict(
                include_role=dict(name='foo')
            ))
        ]
    ))
    blocks.append(this_block)
    IncludeRole.load(
        data=dict(
            name='foo'
        ),
        block=this_block,
        task_include=this_block.block
    )

# Generated at 2022-06-13 09:08:30.394327
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():
    data = dict(
        name='foo',
        role='bar',
        tasks_from='tasks.yml',
        vars_from='vars.yml',
        defaults_from='defaults.yml',
        handlers_from='handlers.yml',
        apply=dict(
            foo='bar'
        ),
        public=True,
        allow_duplicates=True,
        rolespec_validate=False
    )
    block = Block()
    role = Role()
    task_include = IncludeRole(block, role, 'foo')
    loaded = IncludeRole.load(data, block=block, role=None, task_include=task_include)
    assert 'foo : bar' == loaded.get_name()

# Generated at 2022-06-13 09:08:43.830753
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.executor.task_queue_manager import TaskQueueManager

    def load_ansible_roles(role_name, play=None, variable_manager=None, loader=None, collection_list=None):
        role_definition = RoleDefinition.load(role_name, play=play, variable_manager=variable_manager, loader=loader, collection_list=collection_list)
        return role_definition

    # Patch RoleDefinition.load method
    RoleDefinition.load = load_ansible_roles

    # Patch TaskInclude.load method
    TaskInclude.load = load_ansible_roles


# Generated at 2022-06-13 09:08:52.940496
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    class MockRole:
        def __init__(self):
            self.vars = {'a':1}

    class MockTaskInclude:
        def __init__(self):
            self.task = {'vars': {'b':2}}
    data = {'name':'name_role', 'static':True, 'tasks_from':'task_from', 'apply':{'x':1}, 'public': False, 'allow_duplicates':True, 'rolespec_validate':True}
    data2 = {'name':'name_role', 'static':True, 'tasks_from':'task_from', 'apply':{'x':1}, 'public': False, 'allow_duplicates':True, 'rolespec_validate':True, 'not_exists':'True'}
    role

# Generated at 2022-06-13 09:09:04.836639
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager

    from ansible.parsing.dataloader import DataLoader
    from ansible.parsing.mod_args import ModuleArgsParser
    from ansible import context

    from ansible.playbook.role.definition import RoleDefinition
    # TODO: need to mock objects


# Generated at 2022-06-13 09:09:13.082771
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():
    task = IncludeRole(role=None, task_include=None)
    task._role_name = 'test_role'
    task.name = 'given_name'
    assert task.get_name() == 'given_name : test_role'

    task = IncludeRole(role=None, task_include=None)
    task._role_name = 'test_role'
    assert task.get_name() == 'include_role : test_role'


# Generated at 2022-06-13 09:09:20.600224
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    display.display('test_IncludeRole_load - Start')
    # The following data should be passed to the load method
    data = {
        'action': 'include_role',
        'args': {
            'private': True,
            'name': 'bar',
            'allow_duplicates': True,
            'tasks_from': '../../tasks/baz.yml',
            'apply': {'ignore_errors': True, 'serial': 1},
            'rolespec_validate': True,
        }
    }

    role = Role()
    # Load the data into an IncludeRole object
    include_role_obj = IncludeRole.load(data=data, role=role)
    # Check if the include_role_obj is instance of IncludeRole class

# Generated at 2022-06-13 09:09:34.877036
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    '''
        include_role:
          name: include_role_sample
          tasks_from: "{{ inventory_dir }}/tasks/main.yml"
          vars_from: "{{ inventory_dir }}/vars/main.yml"
          vars:
            custom_var:
          defaults_from: "{{ inventory_dir }}/defaults/main.yml"
          handlers_from: "{{ inventory_dir }}/handlers/main.yml"
    '''

# Generated at 2022-06-13 09:09:42.838833
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    ansible_play_path = "test/support/ansible/play.yaml"
    variable_manager = VariableManager()
    variable_manager.extra_vars = utils.load_extra_vars(loader, variable_manager, ansible_play_path)
    variable_manager.options_vars = utils.load_options_vars(loader, ansible_play_path)

    ansible_task = """
    - name: "IncludeRole test"
      include_role:
        name: "common"
        apply:
          tags:
            - test
    """
    data = load_yaml(ansible_task)
    IncludeRole.load(data, variable_manager=variable_manager, loader=loader)

# Generated at 2022-06-13 09:09:54.631133
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    block = Block()
    role = Role()
    role.name = "role_load_name"
    task_include = TaskInclude()
    task_include.name = "task_include_load_name"
    # case 1: no valid name.
    data = {"not_name": "not_name", "action": "include_role"}
    try:
        IncludeRole.load(data=data, block=block, role=role, task_include=task_include)
    except AnsibleParserError as e:
        assert 'name' in str(e)
    # case 2: public should not be a part of action other than include_role
    data = {"name": "role_load_name", "action": "include_tasks", "public": True}

# Generated at 2022-06-13 09:11:02.779777
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    import pytest
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.utils.display import Display

    display = Display()
    import os
    import sys
    import io
    import shutil
    import tempfile


    # Create a temporary directory
    dirpath = tempfile.mkdtemp(dir='.')
    # print('Created temporary directory: ', dirpath)

    # Create a temporary file in the above temporary directory
    file_name = "myfile.yaml"
    fh, fh_path = tempfile.mkstemp(dir=dirpath, suffix=".yaml")

# Generated at 2022-06-13 09:11:13.374722
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    class FakeRole:
        def __init__(self, name):
            self.name = name
            self.collections = ['bar']
    class FakePlay:
        def __init__(self):
            self.roles = []
            self.handlers = []
    class FakeBlock(Block):
        def __init__(self):
            pass
    class FakeVariableManager:
        def __init__(self):
            pass
        def get_vars(self, play, task):
            return dict(foo='baz')

    include_role = IncludeRole(block=FakeBlock(), role=FakeRole('foo'), task_include=TaskInclude())
    include_role._role_name = 'bar'
    include_role._from_files = dict(foo='baz')
    include_role.statically_loaded = True


# Generated at 2022-06-13 09:11:23.879579
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    from ansible.playbook.play_context import PlayContext
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    import ansible.constants as C
    import tempfile
    import os
    import shutil
    import ansible.module_utils.six as six

    fixtures_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fixtures')
    src_path = os.path.join(fixtures_path, 'rolespec', 'test_include_role_1')

    # create temp dir for test
    temp_path = tempfile.mkdtemp()
    for role_name in (src_path,):
        shutil.copy

# Generated at 2022-06-13 09:11:27.117857
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():
    i = IncludeRole()
    i._role_name = "test_name"
    i.action = "include_role"
    name = i.get_name()
    assert name == "include_role : test_name"


# Generated at 2022-06-13 09:11:34.240013
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():
    class IncludeRoleExt(IncludeRole):
        def __init__(self):
            block = Block()
            role = Role()
            task_include = TaskInclude()

            IncludeRole.__init__(self, block, role, task_include)
            self.name = 'test'

            self._role_name = 'test_role'

    ir = IncludeRoleExt()
    assert ir.get_name() == 'test'
    ir.name = None
    assert ir.get_name() == "include_role : test_role"

# Generated at 2022-06-13 09:11:43.879802
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():

    import ansible.constants as C
    import ansible.parsing.dataloader as DataLoader
    from ansible.playbook.role import role_include_attribute
    from ansible.template import Templar

    def load_role_include(data, play, parent_role=None, loader=None, templar=None, **kwargs):
        attr = role_include_attribute(data, play=play, parent_role=parent_role)
        if attr:
            attr.args.update(kwargs)
            return attr.load(data, play=play, parent_role=parent_role, loader=loader, templar=templar)
        return None


# Generated at 2022-06-13 09:11:57.915897
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    # Test case 1: Base case with invalid action
    data = dict()
    data['action'] = 'include_bad'
    data['name'] = 'role'
    data['public'] = True
    data['allow_duplicates'] = False
    data['rolespec_validate'] = False
    try:
        IncludeRole.load(data)
    except AnsibleParserError as e:
        assert str(e) == 'Invalid options for include_bad: public'

    # Test case 2: Base case with invalid argument public
    data = dict()
    data['action'] = 'include_role'
    data['name'] = 'role'
    data['public'] = 'true'
    data['allow_duplicates'] = False
    data['rolespec_validate'] = False

# Generated at 2022-06-13 09:12:01.867591
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    data = { 'name': 'foo', 'role': 'bar', 'apply': 'stuff' }
    ir = IncludeRole()
    result = ir.load(data)
    assert result._role_name == 'bar'
    assert result._from_files == {'tasks': 'main.yml'}

# Generated at 2022-06-13 09:12:02.280466
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    pass

# Generated at 2022-06-13 09:12:09.233038
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.play_context import PlayContext
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.task_include import TaskInclude

    loader = DataLoader()
    options = dict(connection='local', become=True, new_vault_password_file=None,
                   forks=100, become_method='sudo', module_path=None, become_user='root',
                   check=False, diff=False, syntax=None, start_at_task=None)

    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, sources=['localhost,'])