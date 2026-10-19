

# Generated at 2022-06-13 09:02:56.692577
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    from ansible.playbook.play_context import PlayContext

    block = Block()
    role = Role()
    task_include = TaskInclude()

    # Test normal case
    data = dict(
        name='test_role',
        allow_duplicates=False,
        apply=dict(ignore_errors=True),
        public=True,
        rolespec_validate=True,
        tasks_from='task.yml',
        vars_from='vars.yml',
        defaults_from='defaults.yml',
        handlers_from='handlers.yml'
    )
    instance = IncludeRole.load(data, block, role, task_include)
    assert type(instance) == IncludeRole
    assert instance.name == 'test_role'
    assert instance.allow_duplicates == False


# Generated at 2022-06-13 09:03:06.400524
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    # test_IncludeRole_load_missing_name
    data = {
        'include_role': {
            'apply': None,
            'handlers_from': 'handlers.yml',
            'tasks_from': 'tasks.yml',
            'vars_from': 'vars.yml'
        }
    }
    with pytest.raises(AnsibleParserError):
        IncludeRole.load(data)

    # test_IncludeRole_load_bad_args

# Generated at 2022-06-13 09:03:13.702859
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():
    ir = IncludeRole(block=None, role=None, task_include=None)
    ir.name = "test"
    assert ir.get_name() == "test", "Should return test"
    ir.name = ""
    ir.action = "include_role"
    ir._role_name = "role_name"
    assert ir.get_name() == "include_role : role_name", "Should return include_role : role_name"


# Generated at 2022-06-13 09:03:22.594786
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    # pylint: disable=import-error
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.inventory.host import Host

    my_host = Host('test.host')
    my_block = Block(hosts=[my_host], task_list=[])
    my_task = Task(name='task_test')
    my_task._parent = my_block
    my_task.role = 'test_role'
    my_block.block = [my_task]

    my_task_include = IncludeRole()
    my_task_include._parent = my_task
    my_task_include.role = 'test_task_include'
    my_task.args = {'tasks_from': 'test.yml'}

    my_task_include

# Generated at 2022-06-13 09:03:33.493654
# Unit test for method get_include_params of class IncludeRole
def test_IncludeRole_get_include_params():
    from ansible.playbook.play import Play
    from ansible.template import templar

    play_context = dict(
        foo='foo',
        bar='bar',
        baz='baz'
    )

    # play context has precedence over role vars
    vars = dict(
        foo='bar',
        bar='baz',
        qux='qux',
        quxx='quxx'
    )

    # role context has precedence over parent role vars
    parent_vars = dict(
        foo='foo',
        bar='foo',
        baz='baz',
        qux='foo',
        parent='parent'
    )

    mock_loader = lambda *args: dict()

    play = Play.load(dict(
        name='play',
    ))


# Generated at 2022-06-13 09:03:39.343938
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():
    ir = IncludeRole()
    ir.name = 'foo'
    assert ir.name == 'foo'
    ir.name = None
    ir.args = {'role': 'bar'}
    assert ir.get_name() == 'include_role : bar'
    ir.action = 'include_tasks'
    assert ir.get_name() == 'include_tasks : bar'

# Generated at 2022-06-13 09:03:46.250898
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    block = Block([IncludeRole(action='include_role', args={'role': 'my_role'}, role=Role())])
    display_stderr = display.stderr
    display.stderr = lambda x: x  # I can't find a way to mock without doing this
    result = IncludeRole().get_block_list(play=None, variable_manager=None, loader=None)
    display.stderr = display_stderr
    return result

# Generated at 2022-06-13 09:03:55.655632
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    data = {
        'name': 'test-role',
        'role': None,
        'tasks_from': None,
        'vars_from': None,
        'handlers_from': None,
        'defaults_from': None,
        'apply': {},
        'allow_duplicates': True,
        'public': False,
        'rolespec_validate': True
    }
    ir = IncludeRole.load(data)
    assert ir.name == 'test-role'
    ir.rolespec_validate = False
    ir_new = IncludeRole.load(data)
    assert ir_new.rolespec_validate
    assert ir_new.args == data


# Generated at 2022-06-13 09:04:03.054238
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    from ansible.module_utils.six.moves import builtins
    import pytest
    from ansible.errors import AnsibleParserError
    from ansible.playbook.role_include import RoleInclude
    from ansible.playbook.role import Role
    import ansible.playbook.play
    import ansible.playbook.task_include
    import ansible.playbook.block

    ################################################################################################
    # test basic operation and attribute inheritance
    ################################################################################################
    yaml_data = """
    - include_role:
        name: foobar
        apply:
          tags: [ 'tag1', 'tag2' ]
    """

    p = ansible.playbook.play.Play().load(yaml_data, variable_manager=None, loader=None)

# Generated at 2022-06-13 09:04:12.864351
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    task_include_data = dict(
        action='include_role',
        args=dict(
            name='a_role',
            tasks_from='a_tasks.yml',
            handlers_from='a_handlers.yml',
            vars_from='a_vars.yml',
            defaults_from='a_defaults.yml',
            apply=dict(
                a='a',
                b=5,
                c=True,
            ),
            public=True,
            allow_duplicates=False,
        ),
    )
    ir = IncludeRole.load(task_include_data)
    assert ir._role_name == 'a_role'
    assert 'a_tasks' in ir._from_files
    assert 'a_handlers' in ir._from_files

# Generated at 2022-06-13 09:04:36.116290
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():
    import ansible.playbook.role
    import ansible.playbook.task_include

    # construct role
    role = ansible.playbook.role.Role()
    role.name = 'role_name'

    # construct task_include
    task_include = ansible.playbook.task_include.TaskInclude()
    task_include.action = 'action'

    # construct include_role
    include_role = IncludeRole(role=role, task_include=task_include)
    display.display("include_role: %s" % include_role.get_name())



# Generated at 2022-06-13 09:04:41.532614
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    data = {'name': 'somerole'}
    ir = IncludeRole.load(data)
    assert isinstance(ir, IncludeRole)
    assert ir._role_name == 'somerole'

    data = {'role': 'somerole'}
    ir = IncludeRole.load(data)
    assert isinstance(ir, IncludeRole)
    assert ir._role_name == 'somerole'
    assert str(ir) == 'include_role somerole'

    data = {}
    try:
        IncludeRole.load(data)
        assert False
    except AnsibleParserError:
        assert True

# Generated at 2022-06-13 09:04:56.372976
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    # 1.
    # Test the case that the 'name' is not given and the 'role' is not given
    # The method should raise an error since the 'name' value is required
    ir = IncludeRole()
    data = {"role": None}
    try:
        ir.load_data(data)
    except AnsibleParserError:
        pass
    try:
        ir.load(data)
    except AnsibleParserError:
        pass
    # 2.
    # Test the case that the 'name' is given
    # The method should not raise any exception
    ir = IncludeRole()
    data = {"name": "test"}
    try:
        ir.load_data(data)
    except AnsibleParserError:
        assert False

# Generated at 2022-06-13 09:05:05.924375
# Unit test for method get_include_params of class IncludeRole
def test_IncludeRole_get_include_params():
    # test for empty len of ansible_role_name, ansible_role_path, ansible_parent_role_names and ansible_parent_role_paths
    block = Block([]).load(dict(
        roles=['role1', 'role2'], vars=dict(role_var="role_var_value"),
        tasks=dict(include="role_include.yml", var1="val1")))
    role = Role()
    role._role_path = 'test.yml'
    role._role_name = 'test_role_name'
    ir = IncludeRole(block=block, role=role)
    ir.vars["role_var"] = "role_var_value"
    ir._from_files = dict(tasks="role_include.yml")

# Generated at 2022-06-13 09:05:15.028224
# Unit test for method get_include_params of class IncludeRole
def test_IncludeRole_get_include_params():

    q_task = IncludeRole()
    q_task._parent_role = Role()
    q_task._parent_role.name = 'parent_role'
    q_task._parent_role._role_path = '/foo/bar'

    # unit test
    task_params = q_task.get_include_params()
    assert task_params == {
        'ansible_parent_role_names': ['parent_role'],
        'ansible_parent_role_paths': ['/foo/bar']
    }

# Generated at 2022-06-13 09:05:15.639950
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    pass

# Generated at 2022-06-13 09:05:20.706670
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    # Specification of expected values

    # Initialization of the object to be tested
    ir = IncludeRole()

    # Test executions
    ir.load(['- name: role_name'])

    # Get the result of the test
    assert ir._role_name == 'role_name'

# Generated at 2022-06-13 09:05:29.593793
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    import os
    import sys
    import unittest
    from unittest.mock import patch
    from ansible.cli import CLI
    from ansible.playbook.block import Block
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.role import Role
    from ansible.template import Templar


# Generated at 2022-06-13 09:05:41.512089
# Unit test for method get_include_params of class IncludeRole
def test_IncludeRole_get_include_params():

    import pytest

    from ansible.playbook.role import ROLE_CACHE
    from ansible.playbook.role.include import RoleInclude

    from ansible.plugins.loader import plugin_loaders

    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.inventory.inventory import Inventory
    from ansible.playbook.play import Play

    class DataLoader(object):
        def __init__(self):
            pass

    class VariableManager(object):
        def __init__(self):
            self.extra_vars = {}

    class Tqm(object):
        def __init__(self):
            self.loader = DataLoader()
            self.inventory = Inventory()
            self.variable_manager = VariableManager()


# Generated at 2022-06-13 09:05:50.486817
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():

    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task_include import TaskInclude
    from ansible.template import Templar

    task = TaskInclude()
    task.args = dict(
        name='mock',
        apply=dict(
            collect_facts=True,
        )
    )

    task._loader = None
    task._variable_manager = None
    task._parent = Block()

    try:
        task.get_block_list()
    except KeyError as e:
        if '_parent' not in str(e):
            print(e)
        assert '_parent' in str(e)

# Generated at 2022-06-13 09:06:05.558733
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    assert 1 == 1

# Generated at 2022-06-13 09:06:20.126781
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():

    import os
    import sys
    import tempfile
    import unittest

    from ansible.utils.display import Display
    from ansible.playbook.play_context import PlayContext

    from ansible.playbook import Play
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.role import Role
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.role.include import RoleInclude
    from ansible.playbook.handler import Handler
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.errors import AnsibleParserError

    # The ansible.constants.DEFAULT

# Generated at 2022-06-13 09:06:26.270442
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():
    data = dict(
        name='include_role_test',
        role='test_role',
    )
    include_role = IncludeRole.load(dict(
        args=data,
        action='include_role',
    ))
    assert include_role.get_name() == 'include_role_test : test_role'

    data.pop('name', None)
    include_role = IncludeRole.load(dict(
        args=data,
        action='include_role',
    ))
    assert include_role.get_name() == 'include_role : test_role'

# Generated at 2022-06-13 09:06:39.887725
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    from ansible.playbook.play_context import PlayContext

    loader = 'loader'
    variable_manager = 'variable_manager'
    data = 'data'
    block = 'block'
    role = 'role'
    display = 'display'
    task_include = 'task_include'

    ##############################################################################################################
    # Invalid options for action
    print('Invalid options for action')
    ir = IncludeRole(block, role, task_include=task_include)

    data1 = {'name': 'name', 'static': 'static'}
    ir.load(data=data1, block=block, role=role, task_include=task_include, variable_manager=variable_manager, loader=loader)

    ##############################################################################################################
    # 'name' is a required field for action

# Generated at 2022-06-13 09:06:51.417263
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    from units.mock.loader import DictDataLoader
    from units.mock.path import MockVarsModulePath
    from ansible.vars.manager import VariableManager
    from ansible.playbook.play import Play
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play_context import PlayContext


# Generated at 2022-06-13 09:07:02.548195
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    from ansible.playbook.play import Play
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.plugins.loader import get_all_plugin_loaders, get_loader

    PLUGIN_LOADERS = get_all_plugin_loaders()
    action_loader = get_loader(PLUGIN_LOADERS, 'action')

    inventory = InventoryManager(loader=None, sources=[])
    variable_manager = VariableManager()
    play_source = {
        'name': 'IncludeRole Test',
        'hosts': 'all',
        'gather_facts': 'no',
        'tasks': [
            {'include_role': {'name': 'ciscoucs.ucs_data_center'}}
        ]
    }
    play

# Generated at 2022-06-13 09:07:11.363459
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():

    # test cases
    test_defs = []

    # test case (1)
    tc1_args = {'name': 'role_name'}
    tc1_results = {
        '_role_name':'role_name',
        '_role_path':None,
        '_from_files':{},
        '_parent_role':None,
        '_allow_duplicates':True,
        '_public':False,
        '_rolespec_validate':True,
    }
    test_defs.append((tc1_args, tc1_results))

    # test case (2)
    tc2_args = {'role': 'role_name'}

# Generated at 2022-06-13 09:07:11.981995
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    pass

# Generated at 2022-06-13 09:07:21.999319
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    '''
    This is to test syntax of the IncludeRole load method.
    '''
    item = {}
    item["name"] = 'myrole'
    item["apply"] = {"when": "not running_myrole"}
    data = '''
            - include_role:
                name: myrole
                apply:
                    when: not running_myrole
            '''

    block = Block()
    task_include = TaskInclude()
    task_include.action = "include_role"
    _ = IncludeRole.load(data, block=block, task_include=task_include)

    assert _.args == item

# Generated at 2022-06-13 09:07:30.333349
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():

    fake_data = {
        '__ansible_rolespec_validate': True,
        '__ansible_allow_duplicates': True,
        '__ansible_public': False,
        '__ansible_apply': {},
        '__ansible_role_name': 'test1'
    }

    ir = IncludeRole.load(fake_data)

    assert ir.rolespec_validate == True
    assert ir._allow_duplicates == True
    assert ir._public == False
    assert ir._role_name == 'test1'

# Generated at 2022-06-13 09:08:15.969838
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():

    # Generate a fake yaml data to test get_block_list()
    data = {'include_role':{'name':'fake_role'}}
    yaml_data = {}
    yaml_data['include_role'] = data['include_role']

    # Generate a fake block
    block = Block()
    block._play = None
    ir = IncludeRole(block=block)
    ir.args = data['include_role']

    # The role does not exist in the roles path
    try:
        ir.get_block_list()
    except AnsibleParserError:
        print("The role is not exist.")

    # The role exists in the roles path
    # Generate a fake role
    ir._role_name = 'fake_role'
    ir._parent_role = block
    ir._parent_role._

# Generated at 2022-06-13 09:08:29.530931
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    block = Block()
    task = IncludeRole(block, role=None)
    variable_manager = None
    loader = None

    # Test with incorrect syntax
    data = {'role': 'role.name', 'public': True, 'tasks': []}

    try:
        task.load(data, block, variable_manager=variable_manager, loader=loader)
    except AnsibleParserError as e:
        assert str(e) == "'name' is a required field for - include_role:"

    # Test with correct syntax
    data = {'name': 'role.name', 'tasks': []}
    task.load(data, block, variable_manager=variable_manager, loader=loader)

    # Test with incorrect syntax

# Generated at 2022-06-13 09:08:42.130818
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():

    import os
    import sys
    import tempfile

    sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'lib'))
    from ansible.module_utils.common.collections import AnsibleCollectionRef

    from ansible.utils.display import Display
    display = Display()

    from ansible.playbook.play_context import PlayContext
    from ansible.plugins.loader import fragment_loader

    ##########################
    # Setup
    ##########################

    fd, playbook = tempfile.mkstemp()
    filename = os.path.basename(playbook)
    display.vvvv("Generated playbook: %s" % playbook)

    ##########################
    # Test (1)
    ##########################

    # Inputs

# Generated at 2022-06-13 09:08:52.136400
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    from ansible.playbook.play_context import PlayContext
    from ansible.context import CLIContext
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.utils.vars import combine_vars
    import ansible.constants as C
    import os


# Generated at 2022-06-13 09:08:52.745878
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    pass

# Generated at 2022-06-13 09:09:04.710435
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():
    from ansible.playbook.play import Play
    from ansible.playbook.role.meta import RoleMetadata
    p = Play().load({}, variable_manager=None, loader=None)
    r = IncludeRole(play=p).load({'name': 'test', 'role': 'test'}, variable_manager=None, loader=None)
    assert r.get_name() == 'test'
    r = IncludeRole(play=p).load({'role': 'test'}, variable_manager=None, loader=None)
    assert r.get_name() == 'include_role : test'
    r = IncludeRole(play=p).load({}, variable_manager=None, loader=None)
    try:
        r.get_name()
    except AnsibleParserError:
        pass
    else:
        assert False



# Generated at 2022-06-13 09:09:16.811184
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():

    from ansible.playbook.role_include import RoleInclude
    from ansible.playbook.role import Role
    from ansible.playbook.play import Play
    from ansible.template import Templar
    from ansible.vars import VariableManager

    variable_manager = VariableManager()
    variable_manager.extra_vars = {'role_name': 'myrole', 'tasks_from': 'main.yml'}
    loader = None

# Generated at 2022-06-13 09:09:31.391663
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.plugins import role_finder

    from ansible.vars.manager import VariableManager

    # set up the basics
    loader = DataLoader()
    variable_manager = VariableManager()

    play = Play.load(dict(
        name="play",
        hosts='localhost',
        gather_facts='no',
        roles=[],
        tasks=[],
    ), loader, variable_manager)

    # create some roles
    role_paths = ['test_role1', 'test_role2']

    role_finder._create_empty_dirs(role_paths)


# Generated at 2022-06-13 09:09:40.654319
# Unit test for method load of class IncludeRole

# Generated at 2022-06-13 09:09:41.248563
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    pass

# Generated at 2022-06-13 09:10:47.632637
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    loader = DataLoader()
    variable_manager = VariableManager()

# Generated at 2022-06-13 09:10:56.584283
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():

    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.role.definition import RoleDefinition, ROLE_CACHE
    from ansible.playbook.play_context import PlayContext

    # mocking member of ansible.playbook.task_include.TaskInclude()
    # to get actual behavior of load() without having to
    # create a full object hierarchy
    _TASK_INCLUDE_LOAD = TaskInclude.load

    # mocking load method of ansible.playbook.role.definition.RoleDefinition
    # to get actual behavior of load() without having to
    # create a full object hierarchy
    ROLE_DEFINITION_LOAD = RoleDefinition.load

    # define templar, needed for the test
    from ansible.template import Templar

# Generated at 2022-06-13 09:11:05.148951
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():

    import os
    import tempfile
    import shutil
    import ansible.playbook.block
    import ansible.playbook.role.definition
    import ansible.playbook.role.meta
    import ansible.inventory.host

    playbook_base_path = "tests/test_playbooks"
    base_path = "tests/test_roles"
    collection_base_path = "tests/ansible_collections/ns/collection1/plugins/roles"

    # construct a dummy host, needed as a placeholder as a host is required by the
    # objects that are constructed later
    host = ansible.inventory.host.Host('localhost')

    # create a temporary directory
    temp_dir = tempfile.mkdtemp()

    # copy the entire test_playbooks directory to the temporary directory

# Generated at 2022-06-13 09:11:15.081699
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    display.display("Test test_IncludeRole_load()")

    # create a mock result and task
    file_name = './test/include_role/test_include_role.json'
    with open(file_name, 'r') as f:
        result = json.load(f)
    task = result['tasks'][0]
    block = result['tasks'][1]

    # create a mock variable manager, which is used to get variable value
    # with variable name
    variables = dict()
    variable_manager = VariableManager(loader=None, inventory=None, variables=variables)

    # create a mock loader, which is used to get value of a file with an given
    # path

# Generated at 2022-06-13 09:11:24.591117
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.template import Templar

    play_context = PlayContext()
    templar = Templar(loader=None, variables=dict())
    a_play = Play.load({'name': 'foo', 'hosts': 'all', 'connection': 'local'}, variable_manager=None, loader=None)
    a_play._ds = [{'name': 'fred', 'action': 'include_role', 'args': {'name': 'rolename', 'rolespec_validate': False}}]
    a_play._variable_manager = None
    role = RoleDefinition.load(role_data=dict(name='rolename'))
    task = a_

# Generated at 2022-06-13 09:11:34.802766
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():

    # setup given
    collection_list = [
        {
            'name': 'rolespec.test',
            'version': '1.0.0',
            'role': {
                'name': 'test_role_1',
                'metadata': {
                    'dependencies': [
                        {'name': 'test_role_2'}
                    ]
                }
            }
        }
    ]

    task_incl = IncludeRole(collections=collection_list, role_name='test_role_1')

    # test: include_role: task should have a name 'include_role : test_role_1'
    assert task_incl.get_name() == 'include_role : test_role_1'

    # test: include_role: task should have task 'Checkout'

# Generated at 2022-06-13 09:11:44.307382
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.playbook.playbook import Playbook
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.task import Task

    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    pb = Playbook.load()
    pb.set_variable_manager(VariableManager())


# Generated at 2022-06-13 09:11:55.717945
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    ''' Get a task data structure. '''
    data = dict(
        name='myrole',
        tasks_from='task-file',
        vars_from='vars-file',
        handlers_from='handlers-file',
        defaults_from='defaults-file',
        apply=dict(
            serial=2
        )
    )

    # Create a new object for this test, then use the object's load() method to feed in the task data.
    IncludeRole.load(data=data)

    # TODO: Fix this test.
    # assert "<class 'ansible.parsing.yaml.objects.AnsibleSequence'>" == str(t.tags.__class__)
    # assert True == t.public
    # assert True == t.apply_implied_vars
    # assert True ==

# Generated at 2022-06-13 09:11:58.499765
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():
    ir = IncludeRole(block=None, role=None, task_include=None)
    ir._role_name = 'nginx'
    assert ir.get_name() == 'meta : nginx'

# Generated at 2022-06-13 09:12:06.384808
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    from ansible.parsing.dataloader import DataLoader
    from ansible.parsing.vault import VaultLib
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    # create mock data
    my_role = 'APIR'
    my_play = Play()
    my_play._play = my_play
    my_play._included_files = set()
    my_play._included_files.add(my_role)
    my_play._base_vars = {}
    my_play._vars = {}
    my_play._role_names = set()
    my_play._role_names.add(my_role)
    vault_secrets = '$ANSIBLE_VAULT;1.1;AES256\n'
    block