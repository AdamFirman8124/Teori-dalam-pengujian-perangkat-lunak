

# Generated at 2022-06-13 09:02:53.419702
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    # # Inclusion of a role fails without a name
    # data = dict(
    #     role = './tests/../../stubs/include_role',
    # )
    # ir = IncludeRole()
    # assert ir.load(data) != 'AnsibleParserError'
    
    # Inclusion of a role fails with an invalid option
    data = dict(
        name = 'my_role',
        invalid_option = 'bogus'
    )
    ir = IncludeRole()
    assert ir.load(data) != 'AnsibleParserError'
    
    # Inclusion of a role fails with an invalid apply attribute
    data = dict(
        name = 'my_role',
        apply = 'bogus'
    )
    ir = IncludeRole()

# Generated at 2022-06-13 09:03:00.384430
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    # unit test file
    data = dict(
        name='common',
        apply=dict(
            tags='commontag',
        )
    )

    # setup mock objects
    class RolespecValidator(object):
        def __init__(self):
            self.validated_roles = set()

        def validate(self, role):
            self.validated_roles.add(role)

    class Role(object):
        def __init__(self, role):
            self.role = role

    class Loader(object):
        def __init__(self):
            self.roles = dict()

        def get_basedir(self, role):
            return role

    class Play(object):
        def __init__(self, loader):
            self.loader = loader
            self.roles = list()

# Generated at 2022-06-13 09:03:10.810759
# Unit test for method get_include_params of class IncludeRole
def test_IncludeRole_get_include_params():
    from ansible.playbook.role import Role
    from ansible.playbook.task import Task
    from ansible.utils.vars import combine_vars

    # Create a Task object
    task = Task()
    task.vars = dict(foo='foo', bar='bar')

    # Create a parent role
    parent_role = Role()
    parent_role.name = 'parent'
    parent_role.vars = dict(foo='foo_role', bar='bar_role')
    parent_role.roles = list()
    parent_role.tasks = list()
    parent_role.handlers = list()
    parent_role._dependencies = list()
    parent_role._metadata = dict()

    # Create nested role
    role = Role()
    role.name = 'nested'

    # Create associated Include

# Generated at 2022-06-13 09:03:20.862944
# Unit test for method get_include_params of class IncludeRole
def test_IncludeRole_get_include_params():
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.play_context import PlayContext

    block = Block()
    task_include = IncludeRole.load(data={'name': 'name', 'tasks': 'tasks'}, block=block)

    role1 = RoleDefinition('role1', 'role1', 'role1', loader=None, variable_manager=None)
    role1._role_path = 'role_path'
    role1.get_vars.return_value = {}
    task_include._parent_role = role1
    task_include.vars = {}

    # dunder_ansible_parent_role_names = ['role1']

# Generated at 2022-06-13 09:03:30.705606
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():

    # This is a hack so we can import the Ansible module in our tests
    # when running from a git clone that doesn't have a local site.
    import sys
    import os
    import yaml
    sys.path.insert(1, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

    from ansible.playbook.play_context import PlayContext
    from ansible.plugins.loader import role_loader

    ds = yaml.safe_load("""
- include_role:
    name: foo
""")

    pc = PlayContext()
    loader.all()
    ir = IncludeRole.load(ds[0], variable_manager=None, loader=loader, task_include=None)

    assert ir._role_name == 'foo'

# Generated at 2022-06-13 09:03:42.140682
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    from ansible.vars.manager import VariableManager
    from ansible.utils.vars import combine_vars
    from ansible.utils.vars import load_extra_vars
    from ansible.parsing.dataloader import DataLoader

    # Initialize vars and results dicts to be checked
    ds = dict()
    results = dict()

    # Create IncludeRole object and load data
    ir = IncludeRole()
    ir.load(ds)

    # Check the result of load method
    assert(ir.args == ds)
    assert(ir._from_files == dict())
    assert(ir._parent_role == None)
    assert(ir._role_name == None)
    assert(ir._role_path == None)
    assert(ir.task_include == None)

# Generated at 2022-06-13 09:03:49.303446
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    display.verbosity = 3

    # useful to generate a list of valid role parameters
    '''
    d = vars(IncludeRole()).keys() + vars(Role()).keys() + vars(Block()).keys()
    d = set(d) - set(['clean_copy', 'deprecated_play_vars', 'has_run', '_metadata'])
    print(', '.join(list(d)))
    '''
    assert IncludeRole.load({'name': 'name'})

# Generated at 2022-06-13 09:03:58.101170
# Unit test for method get_include_params of class IncludeRole
def test_IncludeRole_get_include_params():

    from ansible.playbook.play_context import PlayContext

    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    from ansible.playbook.role import Role
    from ansible_collections.community.general.tests.unit.compat import unittest
    from ansible_collections.community.general.tests.unit.compat.mock import patch

    class TestIncludeRole(unittest.TestCase):

        def setUp(self):
            self.loader = DataLoader()
            self.inventory = InventoryManager(loader=self.loader, sources=['localhost,'])
            self.variable_manager = VariableManager()
            self.variable_manager.set_inventory(self.inventory)

            # create a dummy

# Generated at 2022-06-13 09:04:09.200282
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():

    from ansible.playbook.task import Task

    # Create a task with an include_role
    include_role = {
        'include_role': {
            'name': 'test_role',
            'tasks_from': './test_role/tasks/main.yml',
            'handlers_from': './test_role/handlers/main.yml'
        }
    }

    # Convert the task with include role to an object
    t = Task()
    try:
        t_obj = t.load(include_role)
    except AnsibleParserError as e:
        t_obj = None

    # Create an include_role object
    include_role_obj = IncludeRole.load(include_role)

    assert isinstance(include_role_obj, IncludeRole)
    assert include_role_obj

# Generated at 2022-06-13 09:04:17.253174
# Unit test for method get_include_params of class IncludeRole
def test_IncludeRole_get_include_params():
    from ansible.playbook.play import Play
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.task_include import TaskInclude
    p = Play().load({'hosts': 'localhost', 'gather_facts': 'no', 'roles': [{'role': 'a_role'}, {'role': 'another_role'}]})
    role = RoleDefinition.load({'name': 'test_role'}, play=p, ds=dict())
    role._role_path = r'd:\fli\test'
    ri = TaskInclude.load({'include': 'a_task', 'role': 'a_role'}, block=Block(), role=role, task_include=None)
    # test_IncludeRole.get_include_params: 0

# Generated at 2022-06-13 09:04:29.591892
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():

    fd = open('../../../test/units/parsing/yaml/include_role_add_fields.yml')
    data = yaml.load(fd)
    fd.close()
    ir = IncludeRole.load(data)
    blocks, handlers = ir.get_block_list()
    assert len(blocks) == 5



# Generated at 2022-06-13 09:04:39.686387
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    import ansible.plugins.loader as loader
    import ansible.plugins.action as action_plugins
    from ansible.template import Templar
    import ansible.constants as constants
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.block import Block
    from ansible.playbook.play import Play
    import os
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.playbook.role import Role
    from ansible.playbook.task import Task
    from ansible.playbook.task.include import IncludeTask

    dummy_loader = DataLoader()
    dummy_passwords = dict()
    variable_manager = VariableManager()

    # Define variable manager to use variables
    variable_

# Generated at 2022-06-13 09:04:54.671335
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    # dict to represent a parent role block
    parent_block = dict(
        name='parent_block',
        roles=['role1', 'role2'],
        handlers=['handler1', 'handler2'],
    )
    # dict to represent a role block
    role_block = dict(
        name='role_block',
        tasks=['task1', 'task2'],
        handlers=['handler1', 'handler2'],
    )
    # dict to represent a task include
    task_include = dict(
        name='task_include',
        tasks=['task1', 'task2'],
        handlers=['handler1', 'handler2'],
    )
    # Data for the IncludeRole object

# Generated at 2022-06-13 09:05:02.174344
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    # Setup
    data = dict(
        name='someRoleName',
        default_vars=dict(
            somevar='somevarValue',
        ),
    )
    block = None
    role = None
    task_include = None
    variable_manager = None
    loader = None

    # Execute
    include_role = IncludeRole.load(data, block = block, role = role, task_include = task_include, variable_manager = variable_manager, loader = loader)

    # Assertions
    assert include_role.name == 'someRoleName'
    assert include_role.args == {'name': 'someRoleName', 'default_vars': {'somevar': 'somevarValue'}}
    assert include_role._parent_role == None
    assert include_role._role_name == 'someRoleName'

# Generated at 2022-06-13 09:05:15.417454
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    """
    define variables and create a RoleInclude
    """
    role = None
    task_include = None

    # test block with parent
    action = "ensure this is include_role"
    block = Block(parent_block=None)
    block.block  = [
        {'block': [
            {'local_action': {
                'include_role': {
                    'name': "test_role"
                }
            }}
        ]}
    ]
    ir = IncludeRole(block, role, task_include=task_include)
    ir.args = {
        'name': 'test_role'
    }
    ir.action = action
    ir._role_name = "test_role"
    block_list = ir.get_block_list()

# Generated at 2022-06-13 09:05:23.152563
# Unit test for method get_include_params of class IncludeRole
def test_IncludeRole_get_include_params():
    # setup
    class FakeRole(object):
        def get_name(self):
            return 'fake_role_name'

        def get_role_params(self):
            return {'a':'a','b':'b'}

    class FakeBlock(object):
        def __init__(self):
            self.vars = {'1':1,'2':2}

    fake_block = FakeBlock()
    fake_role = FakeRole()
    include_role = IncludeRole(block = fake_block, role = fake_role)
    assert include_role.args == {}
    assert include_role._from_files == {}
    assert include_role._parent_role == fake_role
    assert include_role._role_name == None
    assert include_role._role_path == None

    # execution
    result = include

# Generated at 2022-06-13 09:05:31.887592
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    import os
    import shutil
    from tempfile import mkdtemp
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.block import Block
    from ansible.playbook.role import Role
    from ansible.playbook.task import Task
    from ansible.module_utils.six import string_types

    # Create temporary directory
    tmpdir = mkdtemp()

    # Create fake role
    role_path = os.path.join(tmpdir, 'role')
    data_path = os.path.join(role_path, 'tasks')
    os.makedirs(data_path)

# Generated at 2022-06-13 09:05:37.042917
# Unit test for method get_include_params of class IncludeRole
def test_IncludeRole_get_include_params():
    """
    Test that get_include_params returns expected result
    """
    from ansible.playbook.handler import Handler

    # Case 1:
    # no parent role, no handlers
    expected = {'ansible_included_var_files': [], 'ansible_included_tasks': [], 'ansible_included_handlers': []}
    ir = IncludeRole()
    assert ir.get_include_params() == expected

    # Case 2:
    # with parent role and no handlers

# Generated at 2022-06-13 09:05:48.712862
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    from ansible.playbook.block import Block
    from ansible.playbook.role import Role
    from ansible.playbook.role.include import RoleInclude
    from ansible.template import Templar
    import os

    my_loader = None
    my_block = Block()
    my_role = Role()
    my_variable_manager = None
    data = {'name': 'name', 'role': 'role'}

    myobj = IncludeRole.load(data, my_block, my_role, task_include=None, variable_manager=my_variable_manager, loader=my_loader)
    assert myobj.action == 'include_role'
    assert myobj._role_name == 'name'
    assert (myobj.name, myobj.role) == ('name', 'role')
    assert myobj._from_

# Generated at 2022-06-13 09:06:02.459257
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    import pytest

    #
    # Make sure we raise errors on bad data
    #
    dataloader = DataLoader()
    inventory = {}
    variable_manager = VariableManager(loader=dataloader, inventory=inventory)
    play_context = PlayContext()
    args = ['name', 'role']
    t = IncludeRole(block=None, role=None, task_include=None)
    for arg in args:
        data = '''
            - role_test:
            -   %s: 'test_arguments'
            ''' % arg

# Generated at 2022-06-13 09:06:27.412315
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.included_file import IncludedFile
    import shutil
    import tempfile
    import ansible.playbook.play
    import ansible.playbook.task
    import ansible.playbook.block
    import ansible.playbook.role
    tmpdir = tempfile.mkdtemp(dir='/tmp/')
    srcdir = tmpdir + "/src"
    distdir = tmpdir + "/dist"
    myplay = Play().load({'name': 'myplay', 'hosts': 'localhost'})
    ansible.playbook.play.Play.ROLE_CACHE = {}
    ansible.playbook.task.Task.ROLE_CACHE = {}
    ansible.play

# Generated at 2022-06-13 09:06:39.569760
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():

    from ansible.playbook import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager

    loader = DataLoader()
    variable_manager = VariableManager()

# Generated at 2022-06-13 09:06:40.440324
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    pass

# Generated at 2022-06-13 09:06:44.770697
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():

    name = 'rolename'
    ir = IncludeRole()
    ir._role_name = name
    ir.action = 'include_role'
    expected_result = 'include_role : rolename'
    assert ir.get_name() == expected_result


# Generated at 2022-06-13 09:06:54.622232
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    import sys
    import os
    import shutil
    import tempfile

    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.utils.display import Display
    from ansible.plugins.callback import CallbackBase
    from ansible.template import Templar

    display = Display()
    display.verbosity = 4


# Generated at 2022-06-13 09:07:05.615774
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    from io import StringIO
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from units.mock.loader import DictDataLoader
    from units.mock.path import mock_unfrackpath_noop

# Generated at 2022-06-13 09:07:16.089197
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():

    from ansible.playbook.play import Play
    from ansible.playbook.role import Role
    from ansible.playbook.task import Task
    from ansible.plugins.loader import action_loader

    # Prepare test data
    play_data = dict(
        name='Test play',
        hosts='localhost',
        gather_facts='no',
        roles=['/home/user/project/roles/test'],
        tasks=[
            dict(
                include_role=dict(
                    tasks_from='main.yml',
                    role='test',
                ),
            ),
            dict(
                include_role=dict(
                    tasks_from='main.yml',
                    role='test',
                ),
            ),
        ],
    )

# Generated at 2022-06-13 09:07:27.180730
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    import os
    import ansible.constants as C
    import ansible.playbook.role.meta as meta
    import ansible.playbook.role.definition as definition
    # import ansible.executor.task_queue_manager as task_queue_manager
    # import ansible.executor.playbook_executor as playbook_executor
    # import ansible.executor.process.worker as worker
    # import ansible.executor.process.worker_manager as worker_manager
    # import ansible.playbook.play_context as play_context
    import ansible.inventory.manager as inventory_manager
    from ansible.plugins.loader import action_loader, module_loader
    from ansible.playbook.play import Play
    from ansible.playbook.playbook import Playbook

# Generated at 2022-06-13 09:07:36.117820
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():

    # load mock data
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.playbook_executor import PlaybookExecutor

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, sources=["hosts"])

# Generated at 2022-06-13 09:07:43.656175
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():
    name = "some role name"

# Generated at 2022-06-13 09:08:17.205735
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    from ansible.playbook.block import Block
    from ansible.playbook.role import Role
    from ansible.playbook.task_include import TaskInclude
    from ansible.utils.vars import combine_vars

    # create a simple playbook with a role/task that has an include_tasks
    block = Block()
    role = Role()
    role._role_name = "myme"
    task = TaskInclude()
    task._role_name = "otherme"
    data = dict(
        name="otherme",
        rolespec_validate="false",
        allow_duplicates="False",
    )

    # call the include role load method
    result = IncludeRole.load(data, block, role, task)

    # assert that values are correct

# Generated at 2022-06-13 09:08:23.343964
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():

    from ansible.playbook.play_context import PlayContext
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.playbook_executor import PlaybookExecutor

    loader = DataLoader()
    inv_file = loader.load_from_file('/home/khasanov/git/ansible-modules-core/lib/ansible/modules/files/templates/ansible/inventory')
    inventory = InventoryManager(loader=loader, sources=inv_file)
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    # Create a role with a simple task

# Generated at 2022-06-13 09:08:28.369005
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():
    obj = IncludeRole()
    obj.name = 'IncludeRole'
    obj._role_name = 'role'
    assert obj.get_name() == 'IncludeRole : role'
    obj.name = None
    assert obj.get_name() == 'IncludeRole : role'

# Generated at 2022-06-13 09:08:40.146005
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    """
     - name: include role
       include_role:
         name: IncludeRole_load_role_name
       register: include_role_res
    """

    result = {
        "include_role_res": {
            "include_variables": {}
        }
    }
    role = {'role_name': 'IncludeRole_load_role_name'}
    block = Block.load(
        dict(
            block=dict(
                tasks=list(),
                roles=[role]
            )
        )
    )

    ir = IncludeRole.load(role, block=block)
    assert ir._role_name == 'IncludeRole_load_role_name'
    assert ir.get_name() == 'include_role : IncludeRole_load_role_name'

# Generated at 2022-06-13 09:08:51.085186
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():

    data = dict(
        role="cowsay"
    )
    block = Block()
    role = Role()

    ir = IncludeRole(block, role)
    ir.load(data)

    assert ir.args == data
    assert ir._role_name == "cowsay"
    assert ir._from_files == {}
    assert ir._parent_role == role

    data = dict(
        name="cowsay",
        allow_duplicates=False,
        vars_from="vars/main.yml",
        handlers_from="handlers/main.yml",
        apply=dict(
            delegate_to="127.0.0.1",
            serial=True,
            tags=list(["first", "second"])
        )
    )
    ir = IncludeRole(block, role)


# Generated at 2022-06-13 09:09:03.224946
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    from ansible.playbook.play import Play
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    import os
    import sys

    loader = DataLoader()

    play = Play()
    play._variable_manager = VariableManager()
    play._variable_manager._extra_vars = {}
    play._loader = loader

    IncludeRole._parent = play
    spawn_loader = DataLoader()
    inventory = spawn_loader.load_from_file(os.path.join(os.getcwd(), 'tests/test_roles/include_role_inventory.yaml'))
    pb_dir = os.path.join(os.getcwd(), 'tests/test_roles')
    # test_include_role_inventory.yaml
    # [

# Generated at 2022-06-13 09:09:03.816411
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    pass

# Generated at 2022-06-13 09:09:16.000576
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    '''
    The load method is the main way to create a IncludeRole object. This unit test
    ensures that the right object is created in different scenario.

    :return:
    '''

    # Test if argument 'data' is not a dict
    data1 = {'test': 'test'}
    data2 = 'test'
    block = 'block'
    role = 'role'
    task_include = 'task_include'
    variable_manager = 'variable_manager'
    loader = 'loader'
    myResult = None
    expectedResult = AnsibleParserError

    try:
        myResult = IncludeRole.load(data1, block, role, task_include,
                                    variable_manager, loader)
    except (AnsibleParserError, ValueError):
        pass


# Generated at 2022-06-13 09:09:24.532130
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    # Test with a valid dictionary
    data = '''
---
- include_role:
    name: apache
    tasks_from: ./main.yml
    apply:
      tags:
        - foo
    allow_duplicates: False
    rolespec_validate: False
'''
    print("\n")
    print("#####")
    print("TEST: IncludeRole load with a valid dictionary")
    print("#####")
    print("\n")
    result = IncludeRole.load(data)
    assert result is not False
    assert result._from_files['tasks'] is not None
    assert result.apply is not None
    assert result.allow_duplicates is False
    assert result.rolespec_validate is False
    print("\n")
    print("#####")

# Generated at 2022-06-13 09:09:34.824126
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    '''Unit test for method load of class IncludeRole'''
    results = {'failed': False, 'msg': []}

    from ansible.playbook.role_include import RoleInclude
    test_case = {
        'include_role': {'name': 'test_role_name'},
        'include': {'name': 'test_name'}
    }
    for action in test_case.keys():
        result = IncludeRole.load({'action': action, 'args': test_case[action]})
        if result._role_name != 'test_role_name':
            results['failed'] = True

# Generated at 2022-06-13 09:10:38.148509
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    from ansible.playbook.role.meta import RoleMetadata
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins.loader import filter_loader, lookup_loader
    from ansible.plugins.action import ActionBase
    from ansible.vars import VariableManager

    class DummyModule(ActionBase):
        def run(self, tmp=None, task_vars=None):
            return super(DummyModule, self).run(tmp, task_vars)

    class DummyChild(AnsibleBaseYAMLObject):
        pass

    mock_loader_mgr = DummyModule()
    filter_loader.mgr = mock_loader_mgr
    lookup_loader.mgr = mock_loader

# Generated at 2022-06-13 09:10:49.217454
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    """
    This function is used to unit test the method load of class IncludeRole
    """
    # Case 1:
    #   This case is used to test load with data, block, role, task_include and loader being None
    #   Expected: Raise AnsibleParserError
    try:
        IncludeRole.load(None, None, None, None, None)
    except AnsibleParserError as e:
        pass
    else:
        raise AssertionError('The case 1 in test_IncludeRole_load is failed.')

    # Case 2:
    #   This case is used to test load with data, role, task_include and loader being None
    #   Expected: Raise AnsibleParserError

# Generated at 2022-06-13 09:10:51.484943
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():
  include_role = IncludeRole()
  include_role._role_name = "testrole"

  assert include_role.get_name() == "include_role : testrole"

# Generated at 2022-06-13 09:11:02.693664
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():

    from units.mock.loader import DictDataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    import ansible.constants as C
    import os

    # read role
    variable_manager = VariableManager()

# Generated at 2022-06-13 09:11:14.667545
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    import os
    import sys
    #import pytest
    from ansible.parsing.dataloader import DataLoader
    import ansible.utils.plugin_docs as plugin_docs

    my_loader = DataLoader()

    if getattr(sys, 'frozen', False):
        mock_base_path = os.path.join(os.getcwd(), 'ansible', 'modules')
    else:
        mock_base_path = os.path.join(os.getcwd(), 'lib', 'ansible', 'modules')

    mock_paths = plugin_docs.find_files(mock_base_path, '', ['.ps1'])
    plugin_docs.document_plugins(mock_paths, my_loader, mock_base_path)


# Generated at 2022-06-13 09:11:24.558049
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    import pytest
    from ansible.playbook.role.include import IncludeRole
    from ansible.playbook.role.requirement import RoleRequirement
    from ansible.playbook.role import Role

    # load a role with two requirements
    role = Role.load(dict(name="test-role",
                          tasks=[dict(action=dict(module="fail", args=dict(msg="xyz")))]),
                    variable_manager=None,
                    loader=None,
                    collection_list=[])
    role.dependencies = [RoleRequirement.load(dict(name="test-role-1", src="test-role-1")),
                         RoleRequirement.load(dict(name="test-role-2", src="test-role-2"))]

    # load an include_role task w/o parents 
    include_role

# Generated at 2022-06-13 09:11:34.762106
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    import sys
    import os
    # Make sure the current ansible doesn't interfere with the testing
    sys.path.pop(0)

    import json
    import unittest
    from ansible.playbook.block import Block
    from ansible.utils.display import Display
    from ansible.utils.vars import combine_vars

    #
    #   - include_role:
    #     name: ssl-certs
    #     apply:
    #       tags: ["letsencrypt_certs"]
    #       limit: "{{ ansible_fqdn }}:&{{ ansible_fqdn }}"
    #

# Generated at 2022-06-13 09:11:44.274906
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    #initialize variables
    loader, variable_manager, inventory = (None, None, None)
    host = 'somehost'
    connection = 'someconn'
    loader = 'some_loader'
    variable_manager = 'somevarman'
    hostvars = {}

    # create IncludeRole
    include_block = IncludeRole(loader=loader, variable_manager=variable_manager)

    # test data for Include_role.load()

# Generated at 2022-06-13 09:11:57.969871
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    class FakeVariableManager:
        def __init__(self, data):
            self.data = data
        def get_vars(self, *args, **kwargs):
            return self.data
    class FakeLoader:
        def __init__(self, data):
            self.data = data
        def get_basedir(self, *args, **kwargs):
            return self.data
    class FakeRole:
        pass
    class FakeBlock:
        pass
    class FakeTaskInclude:
        pass
    # Normal use
    data = {
        'name': 'myrole',
        'tasks_from': 'main.yml'
    }
    include_role = IncludeRole.load(data)
    assert include_role.name == 'include_role'

# Generated at 2022-06-13 09:12:04.860840
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    import ansible.playbook.block
    import ansible.playbook.play
    import ansible.playbook.role
    import ansible.playbook.task
    import ansible.playbook.task_include

    def _get_play():
        p = ansible.playbook.play.Play()
        p._basedir = '/path/to/playbook'
        return p

    def _get_block(name='block'):
        b = ansible.playbook.block.Block(parent=_get_play())
        b.role = ansible.playbook.role.Role(name='role')
        b.role._role_path = '/path/to/role'
        b.role._metadata = ansible.playbook.role.RoleMetadata()
        b.role._metadata.allow_duplicates = True
