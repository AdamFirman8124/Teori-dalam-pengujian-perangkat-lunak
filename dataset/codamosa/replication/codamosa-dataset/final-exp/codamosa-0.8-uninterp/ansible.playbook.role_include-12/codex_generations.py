

# Generated at 2022-06-13 09:02:51.051695
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.play import Play
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.task import Task
    from ansible.inventory.manager import InventoryManager

    source = """
    - import_role:
        name: testrole
        tasks_from: file1
    """

    def _convert_to_task(data, role=None):
        block = Block.load(data, role=role, task_include=None, use_handlers=False,
                           variable_manager=variable_manager, loader=loader)
        task = Task()
        task._role = role
        task._block = block
        return task.copy()


# Generated at 2022-06-13 09:02:59.258478
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    data = {'include_role': {}}
    obj = IncludeRole.load(data=data)
    assert data['include_role'] is not None

    data = {'import_role': {'name': 'some_role'}}
    obj = IncludeRole.load(data=data)
    assert data['import_role'] is not None

    data = {'import_role': {'name': 'some_role', 'allow_duplicates': False}}
    obj = IncludeRole.load(data=data)
    assert data['import_role'] is not None
    assert obj._allow_duplicates is False

# Generated at 2022-06-13 09:03:10.346596
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    test_data = dict(
        action="include_role",
        args=dict(
            name="test",
        ),
    )
    display.verbosity = 4
    role = IncludeRole.load(test_data)
    assert role._role_name == test_data['args']['name']

    test_data = dict(
        action="include_role",
        args=dict(
            role="test",
        ),
    )
    role = IncludeRole.load(test_data)
    assert role._role_name == test_data['args']['role']

    test_data = dict(
        action="include_role",
        args=dict(
            name="test",
            unknown_val=True,
        ),
    )

# Generated at 2022-06-13 09:03:20.786921
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():
    class Block(object):
        def __init__(self):
            self.vars = {'a': '1'}
            self.role = None
            self.dep_chain = []

    class Role(object):
        def __init__(self, parent_role=None):
            self._role_path = 'role_path'
            self.vars = {'a': '0'}
            self._parents = []

# Generated at 2022-06-13 09:03:25.910537
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    """
    include_role:
      name: foo
    ---
    """
    import ansible.parsing.yaml.objects

    data = ansible.parsing.yaml.objects.AnsibleMapping()
    data['include_role'] = ansible.parsing.yaml.objects.AnsibleMapping()
    data['include_role']['name'] = 'foo'

    role = IncludeRole.load(data, block=Block(), role=Role(), task_include=TaskInclude())

    assert role._role_name == 'foo'
    assert role.name is None
    assert role._from_files == {}


# Generated at 2022-06-13 09:03:26.326559
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    pass

# Generated at 2022-06-13 09:03:37.022771
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    import ansible.playbook.play
    import ansible.playbook.block
    import ansible.playbook.role

    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.plugins.loader import role_loader

    class MockActionBase(object):
        def __init__(self):
            self.__name = 'my_action'

        @property
        def name(self):
            return self.__name

    class MockRole(ansible.playbook.role.Role):
        @property
        def _role_name(self):
            return self.__role_name


# Generated at 2022-06-13 09:03:48.568374
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    """
    Unit test for method load.
    """
    from ansible.playbook.task import Task

    # NOTE: loader and from_files are required to instantiate an IncludeRole
    loader = None
    from_files = {}

    # Test with C._ACTION_INCLUDE_ROLE
    ir = IncludeRole.load({'name': 'test', 'tasks_from': 'tasks.yml'}, task_include=Task.load({'name': 'test'}, loader=loader, from_files=from_files))

    assert ir._role_name == 'test'
    assert ir._from_files['tasks'] == 'tasks.yml'
    assert not ir.statically_loaded
    assert not ir.public
    assert not ir.allow_duplicates

    # Test with C._ACTION_IMPORT_

# Generated at 2022-06-13 09:03:55.488720
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():
    # Test 1: Verify the task name is returned with action and role name
    ir = IncludeRole()
    ir.action = 'include_role'
    ir._role_name = 'role_name'
    assert ir.get_name() == "include_role : role_name"

    # Test 2 : Verify the task name is returned with action, role name and name
    ir = IncludeRole()
    ir.action = 'include_role'
    ir._role_name = 'role_name'
    ir.name = 'name'
    assert ir.get_name() == "name"


# Generated at 2022-06-13 09:04:02.921239
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    # Create a parent role and add a task
    test_parent_role = Role()
    test_parent_role.tasks = [
        Block(
            task_include=IncludeRole(
                args={'role': 'test_role_1'}
            )
        )
    ]
    # Add a role to the parent role
    test_parent_role._dependencies = [
        Role.load(RoleInclude(role_name='test_role_1'))
    ]

    # Create a task include
    task_include = IncludeRole(
        role = test_parent_role,
        args = {'role': 'test_role_2'}
    )
    # Get the block list from the task include
    block_list = task_include.get_block_list()

    # Create a new role to compare with


# Generated at 2022-06-13 09:04:17.334176
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():

    # Test 1: correct results with sample role
    test_role = "sample_role"
    role = IncludeRole.load({}, role=test_role)

    assert len(role.get_block_list()[0]) == 1
    assert role.get_block_list()[0][0].name == "Sample task"

    # Test 2: correct results with invalid role
    test_role = "invalid_role"
    role = IncludeRole.load({}, role=test_role)
    assert role.get_block_list() == ([], [])

    # Test 3: correct results with non-existent role
    test_role = "non_existent_role"
    role = IncludeRole.load({}, role=test_role)
    assert role.get_block_list() == ([], [])

# Generated at 2022-06-13 09:04:25.985707
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():

    class t_object(object):
        pass

    class t_task(t_object):
        def __init__(self, a=None, name=None):
            self.args = a
            self.name = name
        # We need to define these properties to make the test pass
        def get_dep_chain(self):
            pass
        def get_name(self):
            pass
        def get_parent_block(self):
            pass

    class t_block(t_object):
        def get_name(self):
            return self.name
    class t_play(t_object):
        def __init__(self, name=None, roles=[]):
            self.name = name
            self.roles = roles

# Generated at 2022-06-13 09:04:37.287053
# Unit test for method get_include_params of class IncludeRole
def test_IncludeRole_get_include_params():
    loader = None
    variable_manager = None
    role = None
    role_name = 'test_role_name'
    role_path = 'test_role_path'
    parent_role = Role()
    parent_role._role_path = role_path
    parent_role._role_name = role_name
    static_params = {'name': 'testinclude',
                     'apply': {'var1': 'value1'},
                     'allow_duplicates': True,
                     'collections': ['test_collection', 'ansible_collections.name.space.collection'],
                     'public': False,
                     'rolespec_validate': True}

    # IncludeRole object not have attributes from_files and parent_role
    include_role = IncludeRole(role=parent_role)
    include_role.load_

# Generated at 2022-06-13 09:04:40.663961
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():
    """ Unit test for method get_name of class IncludeRole """
    ir = IncludeRole()
    ir.action = 'include_role'
    ir._role_name = 'test'
    assert ir.get_name() == 'include_role : test'

# Generated at 2022-06-13 09:04:49.260699
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    block = Block()
    task_include = TaskInclude()
    variable_manager = None
    loader = None

    # Test the case when 'name' is required 
    data = { 'include_role': { 'name' : 'test_role' } }
    actual_result = IncludeRole.load(data, block, variable_manager, loader)
    expected_result = None
    assert  actual_result == expected_result


# Generated at 2022-06-13 09:04:59.217875
# Unit test for method get_include_params of class IncludeRole
def test_IncludeRole_get_include_params():
    ir = IncludeRole()
    ir._parent_role = Role()
    assert ir.get_include_params() == {'ansible_parent_role_names': [''], 'ansible_parent_role_paths': ['']}
    #
    ir = IncludeRole()
    ir._parent_role = Role()
    ir._parent_role._name = 'test'
    assert ir.get_include_params() == {'ansible_parent_role_names': ['test'], 'ansible_parent_role_paths': ['']}
    #
    ir = IncludeRole()
    ir._parent_role = Role()
    ir._parent_role._role_path = 'test'

# Generated at 2022-06-13 09:05:10.126097
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    from ansible.playbook import Play

    # Define the block variable
    block = Block()

    # Define the variable_manager variable
    variable_manager = None

    # Define the loader variable
    loader = None

    # Define the role variable
    from ansible.playbook.role import Role

    role = Role()
    role._role_name = "web-server"
    role._role_path = "/path/to/roles/web-server"

    # Define the task_include variable
    task_include = None

    # Create the IncludeRole variable
    include_role = IncludeRole(block=block, role=role, task_include=task_include)
    include_role._from_files = {'tasks':'test-tasks.yml'}

    # Define the play variable

# Generated at 2022-06-13 09:05:20.467821
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    # Pass
    data = dict(role=dict(
        name = 'test_role'
    ))
    block = Block()
    role = Role()
    task_include = TaskInclude()
    variable_manager = dict()
    loader = dict()
    result = IncludeRole.load(data, block, role, task_include, variable_manager, loader)
    assert (result == None)

    # Pass

# Generated at 2022-06-13 09:05:21.098474
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    assert False

# Generated at 2022-06-13 09:05:29.930182
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    from ansible.plugins.loader import action_loader
    from ansible.utils.vars import merge_hash
    from ansible.vars.manager import VariableManager
    from ansible.parsing.metavar import parse_kv
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    import ansible.constants as C
    from ansible.playbook.task import Task
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.play_iterator import PlayIterator
    from ansible.inventory.manager import InventoryManager
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.errors import AnsibleParserError

# Generated at 2022-06-13 09:05:43.600804
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    variable_manager = VariableManager()
    loader = DataLoader()

    # Invalid options for include_tasks
    data = dict(
        name = 'fake_role',
        apply = dict(x=5),
    )
    ir = IncludeRole.load(data)
    assert ir.apply == dict(x=5)


# Generated at 2022-06-13 09:05:50.714547
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    from ansible.playbook.role_include import RoleInclude
    from ansible.playbook.play_context import PlayContext

    data = dict(
        name='role',
        public=True,
        task_from='foo/tasks/a.yaml',
    )

    block = Block()
    ir = IncludeRole.load(data, block=block)

    assert ir.name == data['name']
    assert ir.public == data['public']
    assert ir._from_files['task'] == data['task_from']



# Generated at 2022-06-13 09:05:58.743830
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():
    '''
    Test method get_name of class IncludeRole.
    Call get_name() on an empty instance of IncludeRole, which should return a
    string similar to "Role include 'name: role_name'".
    :return:
    '''
    ir = IncludeRole()
    assert ir.get_name() == "Role include 'name: role_name'"
    print("Success: test_get_name")



# Generated at 2022-06-13 09:06:08.511549
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    from ansible.template.vars import VarsModule
    from ansible.vars import VariableManager
    from ansible.playbook.play import Play
    from ansible.plugins.loader import action_loader, lookup_loader
    from ansible.plugins.loader import module_loader
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.executor.playbook_executor import PlaybookExecutor

    # Ansible vars
    loader = DataLoader()
    variable_manager = VariableManager()
    variable_manager.extra

# Generated at 2022-06-13 09:06:10.920186
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    ir = IncludeRole()

    (blocks, handlers) = ir.get_block_list(play=None, variable_manager=None, loader=None)

# Generated at 2022-06-13 09:06:19.248412
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    loader = DataLoader()
    variable_manager = VariableManager()
    play = Play.load({'name': 'test', 'hosts': 'localhost'}, variable_manager=variable_manager, loader=loader)
    role = Role()
    role._role_name = "test_role"
    role._role_path = "/tmp/ansible/roles"
    ir = IncludeRole.load({"name":"test_role"}, block=None, role=role, task_include=None, variable_manager=variable_manager, loader=loader)
    assert ir._role_name == "test_role"

# Generated at 2022-06-13 09:06:27.531391
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():

    from ansible.playbook.block import Block
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.role.definition import TaskDefinition
    import os

    # create a temporary directory to store the rolespec content
    test_dir = os.path.join(C.DEFAULT_LOCAL_TMP, 'ansible_IncludeRole_get_block_list_test')
    if not os.path.exists(test_dir):
        os.makedirs(test_dir)
    test_file = os.path.join(test_dir, 'test_file')

    # create a role 'foo' with a task that creates the file from above
    # using 'foo\main.yml'

# Generated at 2022-06-13 09:06:40.496468
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    Block = type('Block', (object,), {})
    Role = type('Role', (object,), {'compile': lambda *args, **kwargs: [args, kwargs]})
    Play = type('Play', (object,), {'roles': []})
    RoleInclude = type('RoleInclude', (object,), {'load': lambda *args, **kwargs: Role()})
    IncludeRole.RoleInclude = RoleInclude

    play = Play()
    block = Block()
    role = Role()
    role.play = play
    ir = IncludeRole(block=block, role=role)
    ir.name = 'ir'
    ir.args = {'name': 'role'}
    ir.action = 'include_role'


# Generated at 2022-06-13 09:06:46.985354
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    block_mock = Block()
    block_mock.vars = {}
    ir = IncludeRole(block=block_mock)
    ir._role_name = "foo"
    play = None
    variable_manager = None
    loader = None
    block_list = ir.get_block_list(play=play, variable_manager=variable_manager, loader=loader)



# Generated at 2022-06-13 09:06:55.625775
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():

    import sys
    import pytest
    from ansible.errors import AnsibleError, AnsibleParserError
    from ansible.playbook.role import Role
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins.loader import action_loader
    from ansible.template import Templar
    class block:
        def get_name(self, play=None, variable_manager=None, loader=None):
            return self.name

        def get_block_list(self, play=None, variable_manager=None, loader=None):
            return (self.blocks, self.handlers)
    class raw:
        pass
    from ansible.vars.manager import VariableManager
    class variable_manager:
        def __init__(self):
            self.vars = {}


# Generated at 2022-06-13 09:07:18.377942
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    # simple test
    data = dict(name='apache', apply=dict(tags=['mytag1'], when='mywhen'))
    include_role = IncludeRole(None, None, None)
    include_role.load(data, block=None, task_include=None, variable_manager=None, loader=None)
    assert include_role.apply == dict(tags=['mytag1'], when='mywhen')
    assert include_role.name == 'apache'
    assert include_role.args == data
    assert include_role._role_name == 'apache'

    data = dict(name='apache', tasks_from='some_task.yaml')
    include_role = IncludeRole(None, None, None)

# Generated at 2022-06-13 09:07:27.800895
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    """
    In this test, we create an IncludeRole object and configure it to have
    the following parameters

        name: role_name
        role: role_name # this is the same as the name, so it will be ignored
        tasks_from: tasks/main.yml
        handlers_from: handlers/main.yml
        vars_from: vars/main.yml
        public: yes
        apply:
            prompt: "Do you want to apply this role? "
            when: apply_this_role

    Then we call get_block_list, and it should return a list of blocks
    that were loaded from the tasks/main.yml file.

    """
    pass

# Generated at 2022-06-13 09:07:38.067990
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    # Create a task_include
    task_include = IncludeRole()

    # Create a block
    block = Block()

    # Create a role
    role = Role()

    # Create the playbooks
    play = Play()


    # Link the include_role to the play
    include_role = IncludeRole(block, role, task_include=task_include)
    play.roles.append(include_role)
    # Test the method "get_block_list"
    blocks = include_role.get_block_list(play)

    # Test the attribute "role_path" of the role
    role_path = include_role._role_path

    # Test the attribute "role_name" of the role
    role_name = include_role._role_name

    # Test the attribute "_from_files" of the role

# Generated at 2022-06-13 09:07:48.751034
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    play = None
    variable_manager = None
    loader = None

    # SETUP FIXTURES
    # SETUP FIXTURES
    # CREATE FAKE OBJECTS/CLASSES/METHODS THAT WILL BE USED
    class DummyRole(object):

        def __init__(self):
            self.include = False
            self.include_tasks = []
            self.tags = []
            self.when = None

    class DummyRoleInclude(object):

        def __init__(self):
            self.include = False
            self.include_tasks = []
            self.tags = []
            self.when = None


# Generated at 2022-06-13 09:07:57.285058
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    from ansible.playbook.play import Play
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.task_queue_manager import TaskQueueManager

    # TODO: Ugly hack: Needs refactoring to make method testable
    # Fake inventory map
    class FakeInventory(object):
        def __init__(self, host_list):
            self.host_list = host_list
            self.list_hosts = lambda pattern="all": self.host_list

    inventory = InventoryManager(loader=DataLoader(), sources=[])
    inventory.add_host(host="dummyhost", group="test")
    inventory.hosts["dummyhost"].vars = {}

   

# Generated at 2022-06-13 09:08:04.936603
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():

    """
    IncludeRole:
        - load

    """

    action = 'include_role'
    module_name = 'include_role'
    args = dict(name='test_role_name')
    task_ds = dict(action=action, args=args)

    ir = IncludeRole.load(task_ds)

    assert ir.action == action
    assert ir._role_name == args['name']



# Generated at 2022-06-13 09:08:09.031253
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():

    # Create a test IncludeRole object
    include_role = IncludeRole()
    include_role.name = 'my_name'
    include_role._role_name = 'my_role_name'

    assert include_role.get_name() == 'my_name : my_role_name'

# Generated at 2022-06-13 09:08:16.484429
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    # normal include_role
    data = {
        'hosts': 'all',
        'roles': [
            {'name': 'role1'},
            {'name': 'role2', 'apply': {'a': '1'}},
            {'name': 'role3', 'ignore_errors': True},
        ],
    }
    pb = Playbook.load(data, variable_manager=variable_manager, loader=loader).get_plays()[0]
    r = pb.get_roles()[0]
    assert len(r.get_tasks()) == 3
    for ri in r.get_tasks():
        if ri.get_name() == 'role1':
            assert ri.action == 'include_role'

# Generated at 2022-06-13 09:08:22.638203
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    from ansible.playbook import Playbook
    from ansible.playbook.block import Block
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.plugins.loader import get_all_plugin_loaders
    from ansible.module_utils.six import string_types
    from ansible.template import Templar
    from ansible.config.manager import ConfigManager
    import os
    import shutil
    import tempfile

    for plugin_loader in get_all_plugin_loaders():
        plugin_loader.add_directory(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'test', 'lib', 'ansible', 'modules'))


# Generated at 2022-06-13 09:08:24.560561
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    pass

# Generated at 2022-06-13 09:09:02.727898
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():

    from ansible.playbook.role import Role
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.play import Play
    from ansible.plugins.loader import add_all_plugin_dirs
    import ansible.constants as C
    import os

    # Load plugins
    all_dirs = add_all_plugin_dirs()

    # Setup
    RoleDefinition._metadata_files = ['meta/main.yml', 'meta/main.json']
    role_name = 'test_role'

    # Execute method load
    # Case 1: missing name, role is not an alias
    data={}
    try:
        ir = IncludeRole.load(data)
        successful = False
    except AnsibleParserError:
        successful = True
    assert(successful)

    # Case

# Generated at 2022-06-13 09:09:07.548460
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    block = Block.load(None, task='debug', args={'msg': 'hello'}, action='debug')
    role = Role()
    role._role_name = 'role01'
    role._role_path = 'role01'
    task_include = TaskInclude()
    task_include.action = 'include_role'
    ir = IncludeRole(block, role, task_include=task_include)
    ir._role_name = 'role02'
    ir._role_path = 'role02'
    ir._from_files = {'tasks_from': 'tasks.yml'}

    class Play:
        def __init__(self):
            self.roles = [role]
        def get_vars(self):
            return {'message': 'hello'}
    play = Play()


# Generated at 2022-06-13 09:09:18.032440
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():

    # First test with no 'apply' option
    action_opts = {'name': 'role_name'}
    ir = IncludeRole.load(action_opts)
    # Test with empty 'apply' option
    action_opts = {'name': 'role_name', 'apply': {}}
    ir = IncludeRole.load(action_opts)

    # Test with common invalid options
    invalid_opts = [
        {'name': 'role_name', 'does_not_exist': 'foo'},
        {'name': 'role_name', 'apply': 'foo'},
        {'name': 'role_name', 'rolespec_validate': 'false'},
        {'name': 'role_name', 'statically_loaded': 'false'},
    ]

# Generated at 2022-06-13 09:09:30.783115
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():

    # Define Block and Role objects
    class Block(object):
        pass


    class Role(object):
        pass


    # Create IncludeRole and Block objects
    my_IncludeRole = IncludeRole()
    my_Block = Block()

    # Assign values to attributes
    my_IncludeRole._allow_duplicates = False
    my_IncludeRole._from_files = {'handler': 'main.yml', 'meta': 'main.yml', 'task': 'main.yml', 'vars': 'main.yml'}
    my_IncludeRole._parent_block = my_Block
    my_IncludeRole._parent_role = Role()
    my_IncludeRole._public = False
    my_IncludeRole._rolespec_validate = True
    my_IncludeRole._role_name

# Generated at 2022-06-13 09:09:40.123817
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    import ansible.plugins
    from ansible.plugins.strategy import StrategyBase

    class TestStrategy(StrategyBase):
        def _load_included_file(self, included_file, iterator, is_handler=False, parent_block=None):
            pass

    test_loader = ansible.plugins.loader.action_loader.ActionModuleLoader()
    test_play = ansible.playbook.play.Play().load({
        'hosts': '127.0.0.1',
        'gather_facts': 'no',
        'tasks': [
            {'include_role': {'name': 'test_role',
                              'tasks_from': 'test_tasks'}}
        ]
    }, loader=test_loader, variable_manager=None)

# Generated at 2022-06-13 09:09:51.856967
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.plugins.loader import become_loader, connection_loader, callback_loader, module_loader, lookup_loader

    from ansible.utils.display import Display
    from ansible.utils.vars import combine_vars

    import os
    import json
    
    TEST_DIR = os.path.join(os.path.dirname(__file__), '..', 'unit', 'utils', 'plugins', 'strategy')
    display = Display()


# Generated at 2022-06-13 09:10:02.294709
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    """Test IncludeRole.load()"""

    field_attributes = ('name', 'private', 'isa', 'default', 'inherited')
    expected_field_config = {
        '_allow_duplicates': {
            'default': True,
            'inherited': True,
            'isa': 'bool',
            'private': True,
        },
        '_public': {
            'default': False,
            'inherited': True,
            'isa': 'bool',
            'private': True,
        },
        '_rolespec_validate': {
            'default': True,
            'inherited': True,
            'isa': 'bool',
        },
    }

    # Test field attributes

# Generated at 2022-06-13 09:10:11.403212
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    from ansible.playbook.play import Play
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.vars.clean import merge_hash
    from ansible.vars.manager import VariableManager
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    from ansible.template import Templar
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play_context import PlayContext

    def get_variables(t_vars, ds):
        vars_prompt = {}
        vars_files = {}
        vars_params = {}
        merge_hash(vars_prompt, ds.get('vars', {}))
        merge

# Generated at 2022-06-13 09:10:20.490550
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():

    mock_block = Block()
    mock_role = Role()

    # Normal task
    data = dict(
        apply='apply',
        allow_duplicates='allow_duplicates',
        name='name',
        public='public',
        rolespec_validate='rolespec_validate',
        tasks_from='tasks_from',
        vars_from='vars_from',
        defaults_from='defaults_from',
        handlers_from='handlers_from',
    )
    t = IncludeRole.load(data, mock_block, mock_role)
    assert isinstance(t, IncludeRole)
    assert t.action == 'include_role'
    assert t.allow_duplicates == True
    assert t.apply == 'apply'
    assert t.private == False
    assert t._role

# Generated at 2022-06-13 09:10:32.048657
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():

    # test with minimal requirements (action=include_role, name=some_role_name)
    data = dict(
        action=dict(include_role=dict(name='some_role_name')),
    )
    ir = IncludeRole.load(data)
    assert ir.action == 'include_role'
    assert ir.tags == []
    assert ir._role_name == 'some_role_name'
    assert ir._from_files == {}
    assert ir.allow_duplicates is True
    assert ir.public is False
    assert isinstance(ir, IncludeRole)

    # test with additional values

# Generated at 2022-06-13 09:11:34.196635
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    display.verbosity = 3
    role_block = Block()
    role_block.block  = [dict(name="role_action_1", action=dict(module='debug', args=dict(msg='role action 1')))]
    role_block.resolve_block()

    subdir_block = Block()
    subdir_block.block  = [dict(name="role_action_2", action=dict(module='debug', args=dict(msg='role action 2')))]
    subdir_block.resolve_block()

    subdir_block.name = 'role_subdir'
    subdir_block.add_children([role_block])

    role = Role()
    role.get_path = lambda: '/path/to/role'

# Generated at 2022-06-13 09:11:41.081550
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():

    from ansible.module_utils.six import PY3

    if PY3:
        # TODO: fix for Python 3
        return

    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.vars import merge_hash
    from ansible.playbook.play_context import PlayContext
    from ansible.vars import VariableManager

    blocks = None

# Generated at 2022-06-13 09:11:43.540449
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():
    block = Block()
    ir = IncludeRole(block=block)
    ir._role_name = "test_role"
    assert ir.get_name() == "include_role : test_role"



# Generated at 2022-06-13 09:11:49.562754
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    ir = IncludeRole(task_include=TaskInclude())
    ir.load({"name":"foo", "role":"test"},block=Block())
    assert ir.get_name() == "include_role : foo"
    assert ir._role_name == "test"

# Generated at 2022-06-13 09:12:01.379722
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():

    # Define test data
    data = {'include_role': {'name': 'test1'}, 'include': {'name': 'test2'}, 'import_role': {'name': 'test3'} }

    # Define expected results
    expected_result = ['test1 : test1', 'test2 : test2', 'test3 : test3']

    # Initialise test object
    ir = IncludeRole()

    # Loop over test data
    results = []
    for key in data.keys():
        # Set up test object
        ir._load_data(data[key])
        results.append(ir.get_name())

    # Check results against expected results
    assert results == expected_result

# Generated at 2022-06-13 09:12:06.910817
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    include_role = IncludeRole()
    block = Block()
    include_role.load({'name': 'httpd'}, block=block)
    vars_loader, vars_manager = AnsibleVarsLoader(), AnsibleVarsManager()

    (blocks, handlers) = include_role.get_block_list(variable_manager=vars_manager, loader=vars_loader)

    assert type(blocks) is list
    assert type(blocks[0]) is Block
    assert len(blocks) == 6
    assert type(handlers) is list
    assert len(handlers) == 1
    assert type(handlers[0]) is Block

# Generated at 2022-06-13 09:12:19.397407
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    from units.mock.loader import DictDataLoader

    block = Block()
    role = Role()
    loader = DictDataLoader({})
    variable_manager = None

    try:
        IncludeRole.load(dict(role="my_role"), block, role, task_include=None, variable_manager=variable_manager, loader=loader)
    except AnsibleParserError:
        assert False
    else:
        assert True

    try:
        IncludeRole.load(dict(name="my_role"), block, role, task_include=None, variable_manager=variable_manager, loader=loader)
    except AnsibleParserError:
        assert False
    else:
        assert True


# Generated at 2022-06-13 09:12:25.873743
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    '''
    Constructor test: checks exports of a task
    '''

    def _validate(results, objects):
        '''
        Validate the results
        '''

        for key in objects:
            assert (results[key] == objects[key])

    # Test good arguments
    data = dict(
        name='foo',
        apply={'vars': {'x': 'y'}},
        allow_duplicates=True,
        public=False,
        rolespec_validate=True,
    )
    ir = IncludeRole.load(data)
    validate = dict(
        name='foo',
        allow_duplicates=True,
        public=False,
        rolespec_validate=True,
    )
    _validate(ir.args, data)

# Generated at 2022-06-13 09:12:35.347383
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    # Create include block to get blocks
    include_block = Block(role=None, task_include=TaskInclude(role=None))
    include_block.block += [
        {
            'name': 'task 1',
            'action': {
                'module': 'ping',
            }
        },
        {
            'name': 'task 2',
            'action': {
                'module': 'ping',
            }
        }
    ]

    # Create dependent role to get blocks
    dependent_role = Role(name='test_dependent_role',
                          task_include=TaskInclude(role=None))