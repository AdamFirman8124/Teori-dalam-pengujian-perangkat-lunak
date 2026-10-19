

# Generated at 2022-06-13 09:02:52.698874
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager

    assert IncludeRole.get_block_list(play=PlayContext(), variable_manager=VariableManager())
    assert IncludeRole.get_block_list(play=PlayContext(), variable_manager=VariableManager(), loader=None)

# Generated at 2022-06-13 09:03:03.012180
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():
    from ansible.playbook.play_context import PlayContext
    # test for IncludeRole.get_name()
    # data for test (reduce cyclomatic complexity)
    class FakeParent():
        _play = None
    class FakePlay():
        def __init__(self, rolename, playname):
            self.rolename = rolename
            self.playname = playname
            self.roles = [self.rolename]
            self.handlers = [self.playname]
        parents = [FakeParent()]
        variable_manager = None
        loader = None
        collection_list = None
    class FakeRole():
        metadata = None
        def __init__(self, rolename, rolepath):
            self.rolename = rolename
            self.rolepath = rolepath

# Generated at 2022-06-13 09:03:04.243767
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    '''
    Test IncludeRole.get_block_list
    '''
    pass

# Generated at 2022-06-13 09:03:14.568988
# Unit test for method get_include_params of class IncludeRole
def test_IncludeRole_get_include_params():
    # Create a parent role with params
    parent_role = Role()
    parent_role.vars.update({'parent_role_var1': 'parent_role_value1'})

    # Create a IncludeRole task using the parent role
    block = Block.load(dict(tasks=[]), play=None)
    task_include = IncludeRole(block=block, role=parent_role)

    # Get the include parameters
    params = task_include.get_include_params()

    # Test the expected output
    expected = {'role_params': {}, 'ansible_parent_role_names': [], 'ansible_parent_role_paths': [], 'parent_role_var1': 'parent_role_value1'}
    assert expected == params

# Generated at 2022-06-13 09:03:26.228365
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    from ansible.playbook.play_context import PlayContext
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from collections import namedtuple
    import os

    Spec = namedtuple('Spec', ['role_name', 'imports'])

    THIS_DIR = os.path.dirname(__file__)
    ROLE_NAME = 'test-include-role'
    ROLE_DIR = os.path.join(THIS_DIR, 'fixtures', ROLE_NAME)
    DEFAULT_IMPORT_TASKS = ['main.yml']
    TASKS_IMPORT = 'sample_tasks.yml'
    SAMPLE_TASKS = ['file_exists.yml', 'file_does_not_exist.yml']
    DEFAULT_

# Generated at 2022-06-13 09:03:30.950973
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():

    # Setup
    variable_manager = None
    loader = None
    play = None
    variable_manager = None
    loader = None

    # Test
    block = Block()
    role = Role()
    role.get_name = lambda: "test-role"
    task_include = TaskInclude()
    task_include.action = "include_role"
    task_include.vars = {}
    role.get_dependencies = lambda x: None
    task_include.args = {
        "role": "test-role2"
    }
    test_obj = IncludeRole(
        block=block,
        role=role,
        task_include=task_include
    )

# Generated at 2022-06-13 09:03:36.367049
# Unit test for method get_include_params of class IncludeRole
def test_IncludeRole_get_include_params():
    # The goal is to check if `get_include_params` returns the right data
    # given that it's a recursive function.
    # More precisely, we want to check the value returned given a role
    # dependency chain.

    # To test this, we need to:
    # - Build a dependency chain of IncludeRole objects
    # - Build a dependency chain of Role objects
    # - Build an IncludeRole.get_include_params() call stack which returns
    #   the expected result.

    # Build a dependency chain of IncludeRole objects
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.role.include import RoleInclude

    role1_path = '/tmp/role1'
    role2_path = '/tmp/role2'

    # Build a dependency chain of Role objects

    # Role1
    role

# Generated at 2022-06-13 09:03:48.047049
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    from ansible.playbook.task import Task
    from ansible.playbook.play import Play
    from ansible.playbook.playbook import Playbook
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.template import Templar
    from collections import namedtuple
    from ansible.vars import VariableManager

    block1 = Block()
    block1._role_name = 'test'
    block1.vars.update({'name': 'test'})
    block1.vars.update({'role': 'test'})
    block1.block = ['block1']

    task = Task()
    task._role = block1
    task._role_name = 'test'
    task.action = 'include_role'
    task.args.update({'name': 'test'})

# Generated at 2022-06-13 09:03:56.992257
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():

    # Initialize global Display
    Display._access_count = 0
    Display._use_stderr = True

    # Initialize global VariableManager
    VariableManager._vars_plugins = frozenset(C.DEFAULT_VARS_PLUGINS)

    # Initialize global Template
    Templar._fail_on_undefined_errors = frozenset(C.DEFAULT_UNDEFINED_VAR_BEHAVIOR)
    Templar._allow_unsafe_templating = False
    Templar._basedir = None
    Templar._j2_env = None
    Templar._allow_undefined = False

    # Initialize global Options
    Options._shell_executable = '/bin/sh'
    Options._verbosity = 0
    Options._roles_path = None
    Options._module_path = None
    Options._fact_path

# Generated at 2022-06-13 09:04:03.676142
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    from ansible.playbook.play import Play
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    play = Play.load({'name': 'test', 'hosts': ['testhost']}, variable_manager=VariableManager(), loader=DataLoader())

    task = IncludeRole.load(
        {'name': 'test_role', 'apply': {'tags': 'testrole'}},
        play=play,
        variable_manager=VariableManager(),
        loader=DataLoader()
    )
    assert task is not None
    assert task._role_name == 'test_role'
    assert task.get_block_list()[0][0].tags == ['testrole']
    assert task._from_files == {}

# Generated at 2022-06-13 09:04:22.478567
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins.loader import action_loader
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    variable_manager = VariableManager()
    loader = DataLoader()
    play_context = PlayContext()
    task_vars = variable_manager.get_vars(play=play_context, task=None)

    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.play import Play
    # TODO bug with task_vars and play, see https://github.com/ansible/ansible/issues/59053
    # task_vars =

# Generated at 2022-06-13 09:04:29.301635
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():

    ######################
    # prepare test data
    ######################

    # Create a test role
    def create_role_mock(path, role_name):
        r = Role()
        r._role_path = path
        r._role_name = role_name
        return r

    test_role_path = "/home/test/ansible/roles/test_role"
    test_role = create_role_mock(test_role_path, "test_role")

    # Create a test parent role
    test_parent_role = create_role_mock("/home/test/ansible/roles/parent", "parent")
    test_parent_role._parents = []

    # Create a Block object to represent a play:
    test_block = Block()
    test_block._role = test_parent_

# Generated at 2022-06-13 09:04:39.509443
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    from ansible.playbook.play import Play
    from ansible.playbook.role import Role
    from ansible.playbook.role.include import RoleInclude
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager

    # Test valid 'name'
    ir = IncludeRole.load({'name': 'role1', 'role': 'role1'}, variable_manager=VariableManager(), loader=None)
    assert ir.name == 'role1'
    assert ir.role == 'role1'

    # Test valid 'role'
    ir = IncludeRole.load({'role': 'role1'}, variable_manager=VariableManager(), loader=None)
    assert ir.name == 'role1'
    assert ir.role == 'role1'

    # Test missing 'name'

# Generated at 2022-06-13 09:04:50.410692
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    from ansible.vars.manager import VariableManager
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins.loader import action_loader
    from ansible.utils.plugins import action_loader as module_loader
    from ansible.parsing.dataloader import DataLoader

    play_context = PlayContext()
    variable_manager = VariableManager()
    loader = DataLoader()

    task_vars = {}
    role_name = 'test-role-name'

    ir = IncludeRole()
    ir.block = Block()
    ir.block._role = Role()

    ir._parent_role = None
    ir._role_name = role_name

    play_context.variable_manager = variable_manager
    variable_manager._extra_vars = task_vars


# Generated at 2022-06-13 09:04:54.473033
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():
    block = Block()
    role = Role()
    task_include = TaskInclude()
    include_role = IncludeRole(block, role, task_include)
    include_role.name = 'role-name'
    assert include_role.name == 'role-name'
    include_role.name = None
    assert include_role.get_name() == 'include_role : role-name'


# Generated at 2022-06-13 09:05:02.087725
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    class DummyVars:
        def update(self, arg):
            pass
    class DummyLoader:
        def __init__(self):
            self.task_blocks = []
            self.handler_blocks = []
        def load_from_file(self, filename):
            return self.task_blocks, self.handler_blocks
    class DummyTask:
        def __init__(self, block_list_tasks, block_list_handlers):
            self.block_list_tasks = block_list_tasks
            self.block_list_handlers = block_list_handlers
        def set_loader(self, loader):
            self.loader = loader
        def load_data(self, role_data, variable_manager=None, loader=None):
            self.loader.task_blocks = self.block_

# Generated at 2022-06-13 09:05:15.288976
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    """
    IncludeRole.load is a static method which take the following argument:
        - data: (dict) which describe the task
        - block: (Block) which is the parent of the task
        - role: (Role) which is the parent of the task
        - task_include: (TaskInclude) if the task was created as a child of a TaskInclude
        - variable_manager: (VariableManager) which is the variable manager
        - loader: (DataLoader) which is the dataloader
    """

    # Bootstrap a dummy class to test static method
    class Cls():
        def __init__(self):
            self.name = "Cls"
            self.action = "ClsAction"
            self.block = None
            self.role = None
            self.task_include = None

# Generated at 2022-06-13 09:05:23.069475
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    # Test with dynamically loaded role
    def mock_ansible_loader(self, path, class_name, valid_subdirs=None):
        # Check that the path is valid
        if valid_subdirs:
            for subdir in valid_subdirs:
                if subdir in path:
                    print(subdir + ": " + path)
                    return None
        raise Failed

    # Test with statically loaded role
    class MockAnsibleLoader:
        def __init__(self, path, class_name, valid_subdirs=None):
            return

        def load_from_file(self, name, path, is_pkg=False):
            return MockRoleMeta

    class MockRoleMeta:
        def __init__(self):
            self.ROLE_CACHE = {}

# Generated at 2022-06-13 09:05:31.818367
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():

    import sys
    import os
    import unittest

    # in the current directory, we need the roles directory
    # in the parent directory we need the test directory which contains the library
    module_loader = C.DEFAULT_MODULE_LOADER
    module_loader.add_directory(os.path.join(os.path.dirname(__file__), '..'))
    module_loader.add_directory(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'test', 'units', 'library'))
    sys.modules['ansible'] = type('FakeAnsibleModule', (object,), {'__file__': __file__})

    class TestIncludeRole(unittest.TestCase):
        def setUp(self):
            self.ir = dict()



# Generated at 2022-06-13 09:05:44.208221
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():

    import ansible.constants as C
    import ansible.module_utils.six as six

    block = Block()
    task_include = TaskInclude.load(dict(
        name = "i123",
        role = dict(
            name = "included-role"
        )
    ), block=block, role=None, task_include=None)
    role = Role.load(dict(
        name = "included-role",
        src = "roles/included-role",
    ), block=block, task_include=task_include)

    include_role = IncludeRole(block=block, role=role, task_include=task_include)

    t = Template()
    variable_manager = VariableManager(loader=FileSystemLoader(searchpath=C.DEFAULT_ROLES_PATH))
    variable_manager

# Generated at 2022-06-13 09:05:53.019522
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    pass

# Generated at 2022-06-13 09:06:04.234707
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    ''' test_IncludeRole_load will be called by unit test '''
    data = {'name': 'my_role', 'task-files': 'my_role.yml'}
    block = Block()
    role = Role()
    task_include = TaskInclude()
    variable_manager = None
    loader = None
    result = IncludeRole.load(data, block, role, task_include, variable_manager, loader)
    assert result._role_name == 'my_role'
    assert result._from_files == {'tasks': 'my_role.yml'}
    assert result._role_path is None

# Generated at 2022-06-13 09:06:19.004647
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.task_result import TaskResult
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()

# Generated at 2022-06-13 09:06:27.428524
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.playbook.block import Block
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.role.metadata import RoleMetadata
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.role.include import RoleInclude
    from ansible.vars.manager import VariableManager

    ir = IncludeRole()

    host = dict(name='localhost', port=22)

# Generated at 2022-06-13 09:06:35.711557
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():
    class TasksIncludeMock(object):
        pass

    class BlockMock(object):
        pass

    class RoleMock(object):
        pass

    t = TasksIncludeMock()
    t.get_name = IncludeRole.get_name

    t.action = 'include_role'
    t._role_name = 'gwen.siesta'

    assert t.get_name() == 'include_role' + ' : ' + 'gwen.siesta'

# Generated at 2022-06-13 09:06:43.912067
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    ''' Unit test for method IncludeRole._load
        test case:
            1. The method `task_include.load` should be called.
            2. The method `role_include.load` should be called.
        teardown:
            Nothing to do.
        result:
            Pass if this test case not failed.
    '''
    from ansible.playbook.task_include import TaskInclude

    class Mock_TaskInclude(TaskInclude):
        def __init__(self):
            self.task_include_load_called = False
            super(Mock_TaskInclude, self).__init__()

        def load(self, *args, **kwargs):
            self.task_include_load_called = True
            return super(Mock_TaskInclude, self).load(*args, **kwargs)

   

# Generated at 2022-06-13 09:06:49.594408
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    ''' Unit test for method load of class IncludeRole'''
    data = dict(
        name = 'bar',
        allow_duplicates = 'no',
        apply = dict(
            handlers = 'no',
        ),
        vars = dict(
            foo = 'bar',
        ),
        other = 'dont_load',
    )
    block = Block()
    role = Role()
    task_include = IncludeRole(block=block, role=role)
    include_role = IncludeRole.load(data, block=block, role=role, task_include=task_include)
    keys = include_role.args.keys()
    assert('name' in keys)
    assert('allow_duplicates' in keys)
    assert('apply' in keys)
    assert('vars' in keys)

# Generated at 2022-06-13 09:06:57.077515
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.block import Block
    from ansible.module_utils.six import string_types
    from ansible.template import Templar

    # Prepare empty objects
    block_obj = Block()
    block_obj.vars = dict()
    task_include_obj = TaskInclude()
    role_obj = Role()
    variable_manager = variable_manager = type('variable_manager', (object,), {})
    variable_manager.set_available_variables = lambda x: None
    loader = type('loader', (object,), {})

    # Test get_block_list function of IncludeRole object
    # Prepare test object
    ir = IncludeRole

# Generated at 2022-06-13 09:07:00.614683
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():

    # no name or role specified
    data = {"name": "foobar", "role": "foobar"}

    my_task = IncludeRole.load(data)

    assert my_task.get_name() == "foobar : foobar"

# Generated at 2022-06-13 09:07:10.137007
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    '''
    Unit test for method get_block_list of class IncludeRole
    '''
    import ansible.playbook.play
    import ansible.playbook.block
    import ansible.playbook.task

    from ansible.utils.display import Display
    from ansible.module_utils._text import to_text
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    display = Display()
    display.verbosity = 4

    loader = DataLoader()
    templar = Templar(loader=loader, variables={})

    role_name = 'test_role'

    task_include = ansible.playbook.task_include.TaskInclude()
    block = ansible.playbook.block.Block()


# Generated at 2022-06-13 09:07:35.589694
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.vars.manager import VariableManager

    fake_loader = DictDataLoader({})

    fake_variable_manager = VariableManager()

    # These files exists in tests/unit/data/roles-include-v6
    # They are completely fake, do not try to use them
    fake_files = {
        'task' : 'task.yml',
        'vars' : 'vars.yml',
        'handlers' : 'handlers/main.yml',
        'defaults' : 'defaults/main.yml',
        }

    # Add a fake role in the loader
    fake_role_name = 'fake_role'
    fake_role_path = '/path/to/roles/fake_role'
    fake_

# Generated at 2022-06-13 09:07:46.100575
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.role import Role
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from ansible.template import Templar
    from collections import namedtuple
    FakeData = namedtuple('FakeData', ['action', 'args'])
    task_data = dict(
        name=AnsibleUnsafeText('playbook.yml'), parent_uuid='12345'
    )
    block_data = dict(
        role=Role(name='test_role', play=None),
        tasks=[]
    )
    block_data['role']._role_path = '/path/to/roles'
    block = Block.load(block_data, [Task()], task_data)

# Generated at 2022-06-13 09:07:48.030862
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    """get_block_list() is tested (unit) by tests/test_role_include.yml"""
    pass

# Generated at 2022-06-13 09:07:57.531502
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.role import Role
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText

    # create an playbook with one of the roles in the playbook

# Generated at 2022-06-13 09:08:09.501891
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    import ansible.playbook
    import ansible.playbook.play
    import ansible.playbook.task
    v = ansible.constants.DEFAULT_VAULT_PASSWORD_FILE
    ansible.constants.DEFAULT_VAULT_PASSWORD_FILE = None

# Generated at 2022-06-13 09:08:15.784361
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    """
    Test load method:
    - when name is not provided
    - when role is provided
    - when name and role are provided
    - when name is not a string
    - when bad options are provided
    """

    # test 'name' not provided
    # noinspection PyUnusedLocal
    def missing_name(data, block=None, role=None, variable_manager=None, loader=None):
        task = IncludeRole.load(data, block=block, role=role, variable_manager=variable_manager, loader=loader)

    data = {'include_role': 'foo'}
    block = Block()
    role = Role()
    variable_manager = None
    loader = None

# Generated at 2022-06-13 09:08:25.131191
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():

    data = dict(
        name='myRole',
        public=True,
        allow_duplicates=False
    )

    ir = IncludeRole.load(data)

    assert ir._name == 'myRole', "test_IncludeRole_load failed to set _name"
    assert ir._public == True, "test_IncludeRole_load failed to set _public"
    assert ir._allow_duplicates == False, "test_IncludeRole_load failed to set _allow_duplicates"



# Generated at 2022-06-13 09:08:38.017925
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.inventory.manager import InventoryManager
    import os
    
    my_block = Block.load(
        dict(
            name='test',
            tasks=[
                dict(action='debug', msg='hello')
            ]
        ), 
        play=None, variable_manager=None, loader=None
    )

    parent_role = Role()
    

# Generated at 2022-06-13 09:08:49.724819
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.vars.manager import VariableManager
    from ansible.template import Templar
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.executor.task_result import TaskResult
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.inventory.manager import InventoryManager
    from ansible.loader.manager import LoaderManager
    from ansible.utils.color import stringc
    from ansible.plugins.loader import action_loader

# Generated at 2022-06-13 09:09:01.793733
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    from ansible.playbook.play import Play
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.plugins.loader import action_loader
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.parsing.dataloader import DataLoader
    #from ansible.playbook.play_context import PlayContext
    from ansible.playbook.block import Block
    from ansible.utils.sentinel import Sentinel
    from ansible.utils.shlex import shlex_split

    class StubVarsModule(object):
        def vars(self):
            return dict(
                a=dict(b=dict(c=[1, 2, 3]))
            )

    action_loader.add('test', StubVarsModule)

# Generated at 2022-06-13 09:09:41.307395
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    from ansible.playbook.play import Play
    import yaml
    from ansible.parsing.yaml.loader import AnsibleLoader
    action = '- include_role: name=test_role'
    role = 'test_role'
    data = AnsibleLoader(yaml.load(action), yaml.SafeLoader).get_single_data()
    play = Play().load(dict(
        name = 'test_play',
        hosts = 'all',
        gather_facts = 'no',
        roles=[role],
    ), variable_manager=None, loader=None)
    task = IncludeRole.load(data, block=None, role=None, task_include=None, variable_manager=None, loader=None)

# Generated at 2022-06-13 09:09:52.899804
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():

    import unittest
    import ansible.parsing.mod_args as mod_args
    import ansible.parsing.yaml.objects as objects
    import ansible.plugins.loader as plugin_loader

    from ansible.playbook.block import Block
    from ansible.playbook.play import Play
    from ansible.playbook.role_include import RoleInclude
    from ansible.playbook.role import Role
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.handler import Handler

    from collections import namedtuple
    from ansible.utils.vars import combine_vars

    from ansible.template import Templar


# Generated at 2022-06-13 09:10:00.422075
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    '''
    Unit test to verify that IncludeRole.load is implemented correctly.
    '''

    # load data
    data = {}
    block = None
    variable_manager = None
    loader = None
    task_include = None
    role = None

    # function to test
    from ansible.playbook.role.include import IncludeRole
    ir = IncludeRole.load(data, block, role, task_include, variable_manager, loader)

    # assert that the results of the function are correct
    assert isinstance(ir, IncludeRole)

# Generated at 2022-06-13 09:10:10.751606
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    import os
    import tempfile
    import unittest

    from ansible.vars import VariableManager
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.inventory import Inventory
    from ansible.executor import playbook_executor
    from ansible.plugins.loader import action_loader

    class TestIncludeRole(unittest.TestCase):

        def setUp(self):
            pass

        def tearDown(self):
            pass

        def test_include_role(self):

            # Create a temporary directory to store the included role
            temp_dir = tempfile.mkdtemp(dir='/tmp')

            # Create a temporary file to store the main task list

# Generated at 2022-06-13 09:10:24.305888
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    # Setup:
    import ansible.plugins.loader as module_loader
    from ansible.playbook.play import Play

    loader = module_loader._find_plugin_loader('action')
    play = Play().load({}, variable_manager=None, loader=loader)
    play._loader = loader

    path = '../example/roles/test_role'
    from_files = {'tasks': '../example/main.yml'}

    # Action:
    ir = IncludeRole(play=play, role_name='test_role', from_files=from_files)
    blocks, handlers = ir.get_block_list(play=play, loader=loader)

    # Assert:
    assert len(blocks) == 1
    assert isinstance(blocks[0], Block)
    assert len(blocks[0].block)

# Generated at 2022-06-13 09:10:35.626995
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():

    from ansible.playbook.play import Play
    from ansible.playbook.task_include.role import IncludeRole
    from ansible.playbook.role_include import RoleInclude
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.role import Role
    from ansible.vars.manager import VariableManager
    from ansible.vars.hostvars import HostVars
    from ansible.parsing.dataloader import DataLoader


# Generated at 2022-06-13 09:10:42.576668
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.block import Block
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.template import Templar
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.vars.manager import VariableManager
    from ansible.vars.hostvars import HostVars
    from ansible.vars.reserved import RESERVED_VARS
    from ansible.parsing.dataloader import DataLoader
    from ansible.plugins.loader import variable_loader, action_loader

    host_list = []

# Generated at 2022-06-13 09:10:48.751455
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    """
    This function is the test for the method load() in class IncludeRole.
    
    The test combines input and output and test if the test result match the expected result.

    All possible types of input are tested.

    The test result and the expected result are both dictionaries.

    The test is passed if and only if the test result is the same as the expected result.    

    The test is implemented as following:
    Given a method
    When the method receive the input
    Then the method returns the output

    :return:
    """

    def get_action(ir):
        return ir.action

    def get_args(ir):
        return ir.args

    def get_allow_duplicates(ir):
        return ir._allow_duplicates

    def get_allow_duplicates(ir):
        return ir._allow_dupl

# Generated at 2022-06-13 09:10:49.425944
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    pass

# Generated at 2022-06-13 09:10:50.952559
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():
    ir = IncludeRole()
    assert ir.get_name() == 'include_role : None'

# Generated at 2022-06-13 09:12:00.283301
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():
    role = IncludeRole()
    role.name = 'test'
    role._role_name = 'test'
    assert 'test : test' == role.get_name()
    role.name = 'test1'
    assert 'test1 : test' == role.get_name()
    role.name = None
    role._role_name = 'test2'
    assert 'include_role : test2' == role.get_name()

# vim: expandtab:tabstop=4:shiftwidth=4

# Generated at 2022-06-13 09:12:01.441202
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    # TODO: Add a better unit test for get_block_list
    assert False

# Generated at 2022-06-13 09:12:02.414766
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    assert IncludeRole.load(dict(name='test_IncludeRole_load'), loader=None) is not None

# Generated at 2022-06-13 09:12:09.278907
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins import module_loader
    from ansible.vars import VariableManager

    # Setup
    loader = module_loader._find_plugin()
    variable_manager = VariableManager()
    variable_manager.extra_vars["test_parent_role"] = "test_parent_role_var"
    variable_manager.extra_vars["test_child_role"] = "test_child_role_var"
    variable_manager.extra_vars["test_grandchild_role"] = "test_grandchild_role_var"

    # Test

# Generated at 2022-06-13 09:12:20.547323
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():

    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.playbook.playbook import PlayBook
    from ansible.vars.hostvars import HostVars
    from ansible.vars.manager import VariableManager
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.inventory.manager import InventoryManager
    from ansible.executor.playbook_executor import PlaybookExecutor

    sqs = TaskQueueManager()

    loader = sqs._loader
    variable_manager = VariableManager()

    vars = HostVars({})
    variable_manager.extra_vars = vars

    inv = InventoryManager(loader=loader, sources=["127.0.0.1", "localhost"])

# Generated at 2022-06-13 09:12:26.996349
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():

    import ansible.playbook
    ir = ansible.playbook.IncludeRole

    assert ir.load(dict(a='1'), block=None, role=None).args.get('a') == '1'

    try:
        ir.load(dict(a='1'), block=None, role='myrole')
        assert False
    except AnsibleParserError:
        pass

    try:
        ir.load(dict(a='1', name='role1'), block=None, role='role2')
        assert False
    except AnsibleParserError:
        pass

    assert ir.load(dict(name='role1'), block=None, role='role2').args.get('name') == 'role1'


# Generated at 2022-06-13 09:12:36.022350
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    import ansible.playbook.role
    import ansible.playbook.role.include
    import ansible.playbook.task_include
    root_dir = "../../../../"
    role_dir = root_dir+"/lib/ansible/modules/cloud/amazon"
    include_dir = root_dir+"/lib/ansible/modules/cloud/amazon"
    # test is with load method
    ir = IncludeRole(role=ansible.playbook.role.Role(), task_include=ansible.playbook.task_include)
    include_role = ansible.playbook.role.include.RoleInclude()
    playbook_dir = root_dir+"/lib/ansible/playbook"
    available_variables = {}