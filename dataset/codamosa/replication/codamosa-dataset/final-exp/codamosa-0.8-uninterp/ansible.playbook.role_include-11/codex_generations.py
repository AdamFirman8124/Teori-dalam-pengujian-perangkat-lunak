

# Generated at 2022-06-13 09:02:52.223188
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    ''' unit testing for method load of class IncludeRole '''

    def _data_argument(name, value):
        return {name: {'args': {name: value}}}

    data = {'args': {'name': 'common', 'public': True}}

    # create IncludeRole object
    ir = IncludeRole()

    # try to load data of class IncludeRole
    ir.load_data(data, variable_manager=None, loader=None)

    assert ir.args == {'public': True, 'name': 'common'}
    assert ir._allow_duplicates
    assert ir._public
    assert ir._rolespec_validate
    assert ir._role_name == 'common'
    assert ir._from_files == {}

    # name is requried
    data = {'args': {}}

# Generated at 2022-06-13 09:02:56.201794
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    m = IncludeRole(block=None, role=None, task_include=None)
    m.load('role', block=None, role=None, task_include=None, variable_manager=None, loader=None)



# Generated at 2022-06-13 09:03:02.564383
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    # print(test_IncludeRole_load.__doc__)
    # load manually as we are not in a test environment
    import sys
    import os
    import ansible.release
    ansible_path = os.path.realpath(os.path.join(os.path.dirname(ansible.release.__file__), '..'))
    sys.path.append(ansible_path)
    import ansible.plugins.loader as loader
    loader._find_plugin_paths()

    from ansible.playbook.task_include import TaskInclude
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager

    data = dict(
        name='test_role',
        apply=dict(
            tags=['my_tag']
        )
    )

    block = Block()


# Generated at 2022-06-13 09:03:13.266333
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    from ansible.playbook.play import Play
    from ansible.playbook.play import PlayContext
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    import os
    import json
    import pytest


# Generated at 2022-06-13 09:03:22.319715
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():

    # check if error 'Invalid options for <action>' is raise
    # when bad_options is passed in
    data = dict(action='include_role', bad_options='bad_options')
    ir = IncludeRole()
    try:
        ir.load(data)
    except AnsibleParserError as e:
        assert 'Invalid options for include_role: bad_options' in str(e)

    # check if error 'Expected a str for <name> but got <type> instead' is raise
    # when empty value is passed in for name
    data = dict(name='')
    ir = IncludeRole()
    try:
        ir.load(data)
    except AnsibleParserError as e:
        assert 'Expected a string for name but got %s instead' % type('') in str(e)

    # check if

# Generated at 2022-06-13 09:03:31.838011
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task_include import TaskInclude
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    import ansible.constants as C
    import os


# Generated at 2022-06-13 09:03:33.799355
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    """
    Test load() method of class IncludeRole
    """
    pass



# Generated at 2022-06-13 09:03:45.290869
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():
    from ansible.playbook.play import Play
    from ansible.playbook.role.include import ROLE_INCLUDE_CACHE

    assert IncludeRole(None, role=None, task_include=None).get_name() == 'include_role : '

    play = Play.load(dict(
        name="test play",
        hosts=['all'],
        roles=[dict(role="foo")]
    ))
    ROLE_INCLUDE_CACHE[('foo', None)] = Role.load(dict(
        name="foo",
        tasks=dict(main=dict(include_role=dict(name="bar")))
    ), play=play, variable_manager={})

# Generated at 2022-06-13 09:03:48.656463
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():
    ir = IncludeRole(
        block=Block(),
        role='my_role',
        task_include='my_task'
    )
    assert ir.get_name() == "my_task : my_role"

# Generated at 2022-06-13 09:03:53.638185
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    block = Block()
    role = Role()
    task_include = TaskInclude()

    ir = IncludeRole(block, role, task_include)
    ir._role_name = 'test_role'

    myplay = None
    variable_manager = None
    loader = None

    # call get_block_list
    ir.get_block_list(play=myplay, variable_manager=variable_manager, loader=loader)

# Generated at 2022-06-13 09:04:11.301830
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    from ansible.playbook.block import Block
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.plugins.loader import add_all_plugin_dirs
    from ansible.collections import CollectionsLoader
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.playbook.play_context import PlayContext

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, sources=['localhost'])

# Generated at 2022-06-13 09:04:21.725682
# Unit test for method load of class IncludeRole

# Generated at 2022-06-13 09:04:25.900678
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():
    block = Block()
    role = Role()
    task_include = TaskInclude()
    include_role = IncludeRole(block, role, task_include)
    include_role._role_name = "test_role"
    assert include_role.get_name() == "include_role : test_role"
    include_role.name = "test_role1"
    assert include_role.get_name() == "test_role1"

# Generated at 2022-06-13 09:04:37.286248
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():

    # testing dicts
    data1 = {u'role': u'myrole'}
    data2 = {u'name': u'myrole'}
    data3 = {u'name': u'myrole', u'tasks_from': 'tasks/main.yml'}

    # testing loading of a valid IncludeRole
    ir1 = IncludeRole.load(data1)
    assert isinstance(ir1, IncludeRole)
    assert ir1._role_name == u'myrole'
    assert not ir1._from_files

    # testing loading of a valid IncludeRole
    ir2 = IncludeRole.load(data2)
    assert isinstance(ir2, IncludeRole)
    assert ir2._role_name == u'myrole'
    assert not ir2._from_files

    # testing loading of a valid IncludeRole


# Generated at 2022-06-13 09:04:38.989837
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    display.display(u"TEST_INCLUDE_ROLE_LOAD")


# ===========================================

# Generated at 2022-06-13 09:04:49.813165
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    # test case 1
    block = Block()
    role = Role()
    task_include = TaskInclude()
    include_role = IncludeRole(block=block, role=role, task_include=task_include)
    data = dict(apply=dict(some_data="some data", some_other_data="some other data"))
    variable_manager = None
    loader = None
    ir = include_role.load(data=data, variable_manager=variable_manager, loader=loader)
    assert ir.apply == dict(some_data="some data", some_other_data="some other data")
    assert ir._role_name == None

    # test case 2
    block = Block()
    role = Role()
    task_include = TaskInclude()

# Generated at 2022-06-13 09:04:50.536420
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    pass

# Generated at 2022-06-13 09:05:00.001631
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.included_file import IncludedFile
    from ansible.playbook.handler import Handler

    def assert_task_inheritance(task, role_name=None, role_path=None, collection_name=None, collection_version=None):
        if role_name:
            assert task.role_name == role_name
        if role_path:
            assert task.role_path == role_path
        if collection_name:
            assert task.collections[0].name == collection_name
        if collection_version:
            assert task.collections[0].version[0] == collection_version

    loader, inventory, variable_manager = C.load_

# Generated at 2022-06-13 09:05:13.690449
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    # Test with valid args
    display.display("*** TEST: Valid args ***")
    # Load with valid args
    with open("test/units/parsing/data/include_role_1.yml", "rb") as f:
        include_role_dict = yaml.safe_load(f)
    # test role
    role = Role()

    ir = IncludeRole(block=Block(), role=role)
    ir.load(include_role_dict)

    assert ir.name == 'include role'
    assert ir.statically_loaded == True
    assert ir._allow_duplicates == False
    assert ir._from_files == {'defaults': 'defaults.yml', 'vars': 'vars.yml'}
    assert ir._public == True

# Generated at 2022-06-13 09:05:21.816650
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.play import Play
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.template import Templar

    loader = DataLoader()
    host = Host(name='localhost')
    group = Group(name='example')
    group.hosts.add(host)

# Generated at 2022-06-13 09:05:47.457248
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():

    data = dict(
        name = 'role1',
        tasks_from = 'main.yml',
        vars_from = 'vars.yml',
        defaults_from = 'defaults.yml',
        handlers_from = 'handlers.yml'
    )
    ir = IncludeRole.load(data)
    assert ir._role_name == 'role1'
    assert ir._from_files['tasks'] == 'main.yml'
    assert ir._from_files['vars'] == 'vars.yml'
    assert ir._from_files['defaults'] == 'defaults.yml'
    assert ir._from_files['handlers'] == 'handlers.yml'


# Generated at 2022-06-13 09:06:00.983217
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    import ansible.playbook.block
    import ansible.playbook
    from ansible.plugins import module_loader
    from ansible.template import Templar

    from ansible.vars.unsafe_proxy import UnsafeProxy

    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor

    from ansible.playbook.role.meta import RoleMetadata

    from ansible.utils.display import Display
    from ansible.plugins.loader import action_loader

    my_display = Display()
    my_display.verbosity = 3

    loader = DataLoader()


# Generated at 2022-06-13 09:06:08.545726
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():

    class task(object):

        def __init__(self):
            self.args = {
                'tasks_from': 'some_tasks_from_args',
                'vars_from': 'some_vars_from_args',
                'defaults_from': 'some_defaults_from_args',
                'handlers_from': 'some_handlers_from_args',
            }

    class role(object):

        def __init__(self):
            self.args = {
                'tasks_from': 'some_tasks_from_args',
                'vars_from': 'some_vars_from_args',
                'defaults_from': 'some_defaults_from_args',
                'handlers_from': 'some_handlers_from_args',
            }


# Generated at 2022-06-13 09:06:22.818859
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    from ansible.playbook import Playbook
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager

    from ansible.parsing.dataloader import DataLoader

    variable_manager = VariableManager()
    loader = DataLoader()

    play_source =  dict(
        name = "Ansible Play",
        hosts = 'localhost',
        gather_facts = 'no',
        roles = [dict(role_name="bob"), dict(role_name="alice")],
        # roles = [{'role_name':"bob"}, {'role_name':"alice"}],
        tasks = [dict(action='include_role', name='bob'), dict(action='include_role', name='alice')],
    )

    play = Play().load

# Generated at 2022-06-13 09:06:35.709187
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.block import Block
    from ansible.playbook.play import Play
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.parsing.dataloader import DataLoader

    variable_manager = VariableManager()
    variable_manager.extra_vars = {
        'shared_simple_var': 'shared_simple_var_value',
        'shared_complex_var': {
            'k1': 2,
            'k2': True,
            'k3': ['a', 'b']
        }
    }

    loader = DataLoader()

    parent_block = Block()

# Generated at 2022-06-13 09:06:45.663585
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.inventory.manager import InventoryManager
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText
    from ansible.module_utils.six import PY3

    import ansible.constants as C
    # Get RoleInclude

# Generated at 2022-06-13 09:06:55.058494
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    import ansible.plugins.loader
    from ansible.plugins.loader import role_loader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.playbook.play import Play
    import io
    import sys
    import pytest

    basenames = ["playbook", "play", "task", "role"]
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=[])
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    display.verbosity = 0
    roles_path = ["/etc/ansible/roles/"]


# Generated at 2022-06-13 09:07:06.004065
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    from ansible.playbook.role import ROLE_CACHE, Role
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.utils.display import Display
    from ansible.playbook.play import Play
    import os
    import tempfile

    # Setup temp directory
    tempdir = tempfile.mkdtemp()

    # Create file to check processing of variables
    path = os.path.join(tempdir, "test_j2.yml")
    with open(path, "a") as f:
        f.write("param: '{{ par }}'")
    test_dict = {"action": "include_role", "args": {"name": "test_role"}}
    display = Display()
    play_context = PlayContext()
    variable

# Generated at 2022-06-13 09:07:16.408641
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    """ test get_block_list """
    from collections import namedtuple
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.playbook.block import TaskBlock
    from ansible.playbook.play_context import PlayContext

    MockRole = namedtuple('MockRole', 'compile')

    mock_role = MockRole(compile=lambda p, r: [])

    variable_manager = VariableManager()
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, variable_manager=variable_manager)
    play_context = PlayContext()

# Generated at 2022-06-13 09:07:19.375603
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():
    ir = IncludeRole()
    ir._role_name = 'test-role'

    assert ir.get_name() == 'include_role : test-role'



# Generated at 2022-06-13 09:07:57.267199
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    #
    #
    ##############################################################################################################################################
    ##############################################################################################################################################
    #
    # Test for method get_block_list of class IncludeRole
    #
    #
    ##############################################################################################################################################
    ##############################################################################################################################################

    from ansible.playbook.block import Block
    display = Display()

    role = 'roles/apache'

# Generated at 2022-06-13 09:08:03.736402
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    # Test the case where args is neither a string nor a dict
    yaml_tag = 'tag:yaml.org,2002:include'
    args = [1,2,3]
    data = {'__ansible_module__': 'include_role', '__ansible_arguments__': args, '__ansible_action__': 'include_role'}
    assert IncludeRole.load(data).args == data
    data = {'__ansible_module__': 'import_role', '__ansible_arguments__': args, '__ansible_action__': 'import_role'}
    assert IncludeRole.load(data).args == data

    # Test the case where args is a string
    args = 'username'

# Generated at 2022-06-13 09:08:07.417307
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    module = IncludeRole()
    role_data = {'name': 'test'}
    role_data_parser = module.load(role_data)
    assert role_data_parser._role_name == 'test'

# Generated at 2022-06-13 09:08:17.682955
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    from ansible.playbook.role import Role
    from ansible.playbook.play import Play
    from ansible.playbook.role.include import RoleInclude
    from ansible.inventory.group import Group

    loader, inventory, variable_manager = C.make_test_playbook()

    # create an empty block
    block1 = Block()

    # create an empty role object
    role1 = Role()

    data = dict(
        name='test_role',
        role='test_role',
        public=True,
        rolespec_validate=True,
        apply=dict(a=10),
    )

    # create an include_role object
    include_role1 = IncludeRole.load(data=data, block=block1, role=role1, variable_manager=variable_manager, loader=loader)

    #

# Generated at 2022-06-13 09:08:30.395278
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    '''
    Returns:
        bool: True if all unit tests passed, False otherwise
    '''
    ret = True

    def _get_block_list(self, play=None, variable_manager=None, loader=None):
        return self.get_block_list(play, variable_manager, loader)

    def _get_block_list_mock(self, play=None, variable_manager=None, loader=None):
        return ([], [])

    # parameter play can be None
    args_list = [
        # play, loader, blocks, handlers
        (None, None, ([], []), ([], [])),
    ]

    for args in args_list:
        play, loader, expected_results, expected_results_mock = args
        obj = IncludeRole()

# Generated at 2022-06-13 09:08:42.817459
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    """Unit tests for IncludeRole loading"""

    from ansible.vars.manager import VariableManager
    from ansible.playbook.play_context import PlayContext
    from ansible.parsing.loader import DataLoader
    from ansible.inventory.manager import InventoryManager

    variable_manager = VariableManager()
    loader = DataLoader()
    inventory = InventoryManager(loader, variable_manager, loader.get_basedir())
    variable_manager.set_inventory(inventory)
    task = {
        'name': 'include a role',
        'include_role': 'local_role',
    }

    ir = IncludeRole.load(task)

    assert ir.name == 'include a role'
    assert ir._role_name == 'local_role'
    assert ir.statically_loaded is False  # defaults to False


# Generated at 2022-06-13 09:08:52.535010
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    from ansible.vars.manager import VariableManager
    from ansible.inventory.host import Host
    from ansible.inventory.manager import InventoryManager
    from ansible.module_utils.six import StringIO

    blocks = []
    for i in range(9):
        block = Block()
        block.name = "test block %d" % i
        block.block = [ {'task':{}, 'name': "test task %d" % i} ]
        blocks.append(block)

    handlers = []
    for i in range(3):
        block = Block()
        block.name = "test handler %d" % i
        block.block = [ {'task':{}, 'name': "test task %d" % i} ]
        handlers.append(block)

    task_include = IncludeRole()
    task_include

# Generated at 2022-06-13 09:09:04.453957
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    data = {"action": "someaction",
            "name": "somefile.yml",
            "tasks_from": "somefile.yml",
            "rolespec_validate": True,
            "allow_duplicates": True,
            "public": True,
            "apply": False}
    variable_manager = None
    loader = None
    role = None
    from ansible.playbook.task_include import TaskInclude
    include = TaskInclude.load(data, variable_manager=variable_manager, loader=loader)
    ir = IncludeRole(role=role, task_include=include)
    ir._role_name = "somefile.yml"

    blocks = [{"tasks": [{"name": "some task"}]}]
    ir._blocks = blocks

    p_block = ir.build_

# Generated at 2022-06-13 09:09:16.822538
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    from ansible.playbook.play_context import PlayContext
    p = Play()

# Generated at 2022-06-13 09:09:31.390424
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    class TestTaskInclude(TaskInclude):
        pass

    block1 = Block(role=None, parent_block=None, use_handlers=False, role_name='role1', role_path='/path/to/role1')
    role1 = Role(name='role1', play=None, parents=[], default_vars=[], collection_list=None)
    task_include1 = TestTaskInclude(block=block1, role=role1, task_include=None)

    task_include1.vars = {
        'a': 'aaa',
        'b': 'bbb',
        'c': 'ccc',
        '_ansible_parent_role': 'role1'
    }


# Generated at 2022-06-13 09:10:37.933869
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    import os
    import imp
    import tempfile
    from ansible.playbook.play_context import PlayContext
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    # Define a test dir
    test_dir = tempfile.mkdtemp()
    # Include a variable in the roles dir
    vars_file_content = "var1: v1"
    with open(os.path.join(test_dir, 'vars', 'main.yaml'), 'wt') as vars_file:
        vars_file.write(vars_file_content)
    # Include a task in the tasks dir
    tasks_file_content = '- name: test_include_role\n  ping: '

# Generated at 2022-06-13 09:10:49.124194
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    display.verbosity = 3
    pb = '''
    - hosts: localhost
      name: "just a localhost test"
      tasks:
      - import_tasks: tasks/main.yml
      - include_role:
          name: myrole
          - import_tasks: tasks/a.yml
          - import_tasks: tasks/b.yml
    '''
    pb = pb.replace('    ', ' ')

    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.plugins.strategy.linear import Strategy

# Generated at 2022-06-13 09:10:58.339773
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():

    from ansible.playbook.play import Play

    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task

    from ansible.vars.unsafe_proxy import AnsibleUnsafeText


    # role directory for test
    TEST_DIR = os.path.join(os.path.dirname(__file__),
                            'data', 'roles', 'test_include_role_get_block_list')

    # Create a fake play
    play_context = PlayContext()
    play = Play().load({'name': 'testPlay', 'hosts': 'all', 'gather_facts': 'no'},
                       variable_manager=None, loader=None)

    # Create a fake task
    task = Task()
    play._dep_chain = [task._uuid]


# Generated at 2022-06-13 09:11:05.898741
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    # Some tests refer to constants which don't exist in the global-scope
    C._TASK_INCLUDE_ACTION = 'include'
    C._TASK_INCLUDE_ROLE_ACTION = 'import_role'
    # 1) Load a role specification, verify that everything is loaded correctly
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play

    file_name = "./test_IncludeRole_load.yml"
    options = {}
    loader = DataLoader()
    passwords = {}
    inventory = InventoryManager(loader=loader, sources=[file_name])
    variable_

# Generated at 2022-06-13 09:11:15.836499
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    from ansible.playbook.role_include import RoleInclude
    from ansible.playbook.role import Role
    from ansible.playbook.play import Play
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    path_to_playbook = ''
    loader = None

    test_data = dict(
        name="test_role",
        role=None,
        apply={},
        public=False,
        allow_duplicates=False,
    )

    test_data_no_name = dict(
        role="test_role",
        apply={},
        public=False,
        allow_duplicates=False,
    )


# Generated at 2022-06-13 09:11:16.442458
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    pass

# Generated at 2022-06-13 09:11:17.118880
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    pass

# Generated at 2022-06-13 09:11:19.868727
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():
    ir = IncludeRole(block=Block(), role=Role())
    ir._role_name = "test_role_name"
    assert ir.get_name() == "include_role : test_role_name"

# Generated at 2022-06-13 09:11:26.941833
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    from ansible.playbook.play import Play
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.role import Role
    from ansible.playbook.role.include import RoleInclude
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager

    options = [{
        'name': 'test_include_role',
        'tasks_from': 'main.yml',
        'defaults_from': 'defaults/main.yml',
        'vars_from': 'vars/main.yml',
        'handlers_from': 'handlers/main.yml',
    }]


# Generated at 2022-06-13 09:11:30.988188
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():
    role = Role('test_role', 'test_playbook')
    include_role = IncludeRole(block=Block(role=role), role=role)
    include_role._role_name = 'test_role'
    assert include_role.get_name() == 'include_role : test_role'