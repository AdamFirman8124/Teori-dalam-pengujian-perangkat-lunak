

# Generated at 2022-06-13 09:02:56.613430
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    from ansible.playbook.play import Play
    from ansible.playbook.block import Block
    play = Play.load(dict(
        name="Play",
        hosts='all',
        gather_facts='no',
        roles=["my_role"]
    ), variable_manager=None, loader=None)
    block = play.get_roles()[0].get_default_block()
    include_role = IncludeRole.load(dict(
        name="name from host_var",
        apply=dict(debug=True)
    ), block=block, role=None)
    assert include_role._role_name == "name from host_var"
    assert include_role._from_files == dict(tasks=None, vars=None, defaults=None, handlers=None)



# Generated at 2022-06-13 09:03:02.878614
# Unit test for method get_include_params of class IncludeRole
def test_IncludeRole_get_include_params():
    # init the variable manager used to get the variables
    variable_manager = VariableManager()

    # init the datastructure that contains the data to build the tasks
    data = dict(
        name="my role",
        tasks=[{'name': 'task1'}]
    )

    # create the role based on the data
    my_role = Role().load(data, variable_manager=variable_manager)

    # init the datastructure that contains the data to build the include_tasks
    data = dict(
        name="my role",
        tasks=[{'include_role': {'name': 'my role'}}]
    )

    # create the role based on the data
    my_role = Role().load(data, variable_manager=variable_manager)

    # get the include role of the role
    include_role = my_

# Generated at 2022-06-13 09:03:03.576786
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    pass

# Generated at 2022-06-13 09:03:14.644796
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():

    # Test for empty data
    data = {}
    block, role = None, None
    res_expected = None
    task_obj = IncludeRole.load(data, block, role)
    assert task_obj is res_expected

    # Test for empty data when role is not None
    data = {}
    block, role = None, 'role'
    res_expected = None
    task_obj = IncludeRole.load(data, block, role)
    assert task_obj is res_expected

    # Test for empty data when block is not None
    data = {}
    block, role = Block(), None
    res_expected = None
    task_obj = IncludeRole.load(data, block, role)
    assert task_obj is res_expected

    # Test for empty data when block and role are not None
    data = {}
    block,

# Generated at 2022-06-13 09:03:16.397384
# Unit test for method get_include_params of class IncludeRole
def test_IncludeRole_get_include_params():
    pass

# Generated at 2022-06-13 09:03:18.242676
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    '''IncludeRole.load()'''
    raise NotImplementedError


# Generated at 2022-06-13 09:03:28.436580
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    loader = DataLoader()
    variable_manager = VariableManager()
    variable_manager.extra_vars = {'role_name': 'test_role'}
    block = Block()
    include_role = IncludeRole(block)
    playbook = {}
    include_role.load('- include_role: {{role_name}}', block=block, role=None, task_include=None, variable_manager=variable_manager)
    assert include_role._role_name == 'test_role'
    include_role.load('- include_role: test2', block=block, role=None, task_include=None, variable_manager=None)
    assert include_role._role_name == 'test2'

# Generated at 2022-06-13 09:03:39.793800
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    import ansible.playbook.block as block
    import ansible.playbook.task as task
    import ansible.playbook.role as role

    x = IncludeRole(block=block.Block())
    x._role_name = 'test_role'

    y = role.Role(name='test_role')
    y._metadata = role.RoleMetadata()
    y._metadata.allow_duplicates = True
    y._parent_role = None
    y._role_path = 'role_path'

    y.tasks = [
        task.Task(name='action', action='action', args=dict(a='a'))
    ]
    (role_blocks, role_handlers) = x.get_block_list(role=y)

    assert len(role_blocks) == 1

# Generated at 2022-06-13 09:03:50.482415
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    from ansible.playbook.role.definition import RoleDefinition

    from argparse import Namespace  # pylint: disable=unused-import
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager

    #pylint: disable=too-many-locals
    def _get_variable_manager(loader, play=None):
        # FIXME: this is more a hack than a clean method
        roledef = RoleDefinition()
        roledef._role_path = '/a/b/role'
        roledef._metadata = Namespace(allow_duplicates=True)

        context = PlayContext()
        if play is not None:
            context.loader = loader
            context._variables = play.get_variable_manager()


# Generated at 2022-06-13 09:03:59.090407
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    data = {
        'action': 'include_role',
        'name': 'myrole',
        'apply': {
            'some': 'other',
            'params': {
                'for': 'test',
                'this': 'thing'
            }
        },
        'allow_duplicates': True,
        'public': True,
        'rolespec_validate': True
    }
    ir = IncludeRole.load(data)
    assert ir.args == data
    assert ir._role_name == 'myrole'
    assert ir.apply == {
        'some': 'other',
        'params': {
            'for': 'test',
            'this': 'thing'
        }
    }
    assert ir.allow_duplicates is True
    assert ir.public is True
    assert ir.ro

# Generated at 2022-06-13 09:04:13.057339
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    pass

# Generated at 2022-06-13 09:04:23.128706
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():

    from ansible.playbook import Playbook
    from ansible.playbook.block import Block
    from ansible.playbook.play import Play
    from ansible.playbook.role import Role
    from ansible.playbook.task import Task
    from ansible.template import Templar
    import ansible.constants as C

    p = Play()
    p.load({
        "name": "test play",
        "hosts": "all",
        "gather_facts": "no",
        "tasks": [
            {
                'include_role': {
                   'name': 'test',
                   'public': True
                }
            }
        ]
    })

    r = Role()

# Generated at 2022-06-13 09:04:29.783365
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    # Test errors
    data = {'action': 'include_role'}
    ir = IncludeRole(None, None)
    try:
        ir.load_data(data)
        assert False, 'Should have raised an error'
    except AnsibleParserError as e:
        assert 'Expected a dict' in str(e)

    data = {'action': 'include_role', 'name': 'my_role'}
    try:
        ir.load_data(data)
    except AnsibleParserError as e:
        assert False, 'Should not have raised an error: %s' % str(e)

    # Test good case

# Generated at 2022-06-13 09:04:39.770701
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    from ansible.playbook.role_include import RoleInclude
    from ansible.playbook.role import Role

    # Initialize
    ir = IncludeRole()

    # Test case with invalid_args
    data = dict(name="test", invalid_args="something")
    with pytest.raises(AnsibleParserError):
        ir = IncludeRole.load(data, block=None, role=None, task_include=None, variable_manager=None, loader=None)

    # Test case with valid options
    data = dict(name="test", allow_duplicates=False, apply=dict(x="x"), public=False, rolespec_validate=True,
                defaults_from="defaults", handlers_from="handlers", tasks_from="tasks", vars_from="vars")
    ir = IncludeRole.load

# Generated at 2022-06-13 09:04:54.738226
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.task_queue_manager import TaskQueueManager

    from ansible.playbook.play import Play

    loader = DataLoader()

    myplay = Play()

    inventory = InventoryManager(loader=loader, sources=['localhost,'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)

# Generated at 2022-06-13 09:05:05.004775
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():

    # create a mock object to test IncludeRole.load method
    # it is defined in test/units/include/test_IncludeRole.py
    print("Invoking test_IncludeRole_load(): ")
    mock_obj = AnsibleParserError("This_is_mock")
    assert(hasattr(mock_obj, 'message'))
    assert(mock_obj.message == "This_is_mock")

    # Test for the following scenarios:
    # 1. role_name is None
    # 2. Invalid options for include_role: public
    # 3. Invalid options for include_role: fake
    # 4. args_value is not a string

    mock_data = {}

    # Test for scenario 1
    # Test for args = {'name': None, 'role': None}
    mock_data['args']

# Generated at 2022-06-13 09:05:17.775095
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    # Test variables
    from_file = "test/test/test.yaml"
    from_file2 = "test2/test2/test2.yaml"
    from_file3 = "test3/test3/test3.yaml"
    from_file4 = "test4/test4/test4.yaml"
    name = "test.yaml"
    fake_file = "fake/fake/file.yaml"

    # Test case - missing required 'name' option

# Generated at 2022-06-13 09:05:27.398090
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    my_block = Block()
    my_role = Role()
    data = dict(
        action='include_role',
        name='my_role_name',
        tasks_from='~/roles/my_role/tasks/main.yml',
        vars_from='~/roles/my_role/vars/main.yml',
        defaults_from='~/roles/my_role/defaults/main.yml',
        handlers_from='~/roles/my_role/handlers/main.yml',
        public=True,
        apply=dict(),
    )
    ir = IncludeRole.load(data, block=my_block, role=my_role)
    assert isinstance(ir, IncludeRole)
    assert isinstance(ir._parent, Role)
    assert ir._role

# Generated at 2022-06-13 09:05:34.814642
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():
    assert IncludeRole().get_name() == "include_role : "
    assert IncludeRole(name="name").get_name() == "name : "
    assert IncludeRole(name="name", role="role").get_name() == "name : role"
    assert IncludeRole(role="role").get_name() == "include_role : role"

    # Test with Block attribute
    from ansible.playbook.block import Block
    assert IncludeRole(block=Block()).get_name() == "include_role : "
    assert IncludeRole(block=Block(name="name")).get_name() == "name : "
    assert IncludeRole(block=Block(name="name"), role="role").get_name() == "name : role"

# Generated at 2022-06-13 09:05:47.249431
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():

    from ansible.vars import VariableManager
    from ansible.utils.display import Display
    display = Display()
    loader = None

    role_name = 'test_IncludeRole_get_block_list'

    def create_role_path(role_name):
        import tempfile
        from ansible.parsing.dataloader import DataLoader
        from ansible.playbook.play_context import PlayContext
        from ansible.playbook.task_include import TaskInclude
        # Create and return a temporary directory
        tmpdir = tempfile.mkdtemp()
        b_role = '''
            - name: test task
              include_role:
                name: "{{ role_name }}"
        '''
        role_path = os.path.join(tmpdir, role_name)
        os.mkdir

# Generated at 2022-06-13 09:06:08.688420
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.collections.loader._yaml_loader import AnsibleFileLoader
    from ansible.utils.vars import combine_vars
    from ansible.utils.display import Display
    import ansible.constants as C
    import ansible.context
    display = Display()

    basedir = 'tests/functional/targets/galaxy/test-galaxy'
    collection_paths = [basedir]


# Generated at 2022-06-13 09:06:09.290167
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    pass

# Generated at 2022-06-13 09:06:14.713613
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    import json
    with open('test/units/parsing/playbooks/IncludeRole.json', 'r') as result:
        data = json.load(result)
        parsed_data = IncludeRole.load(data)
        assert parsed_data._parent_role.name is None
        assert parsed_data._rolespec_validate
        assert parsed_data.args.get('name') == 'ntp'
        assert parsed_data.vars == {'foo': 'bar'}

# Generated at 2022-06-13 09:06:23.382967
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    from collections import namedtuple
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    import sys

    TestOptions = namedtuple('TestOptions', ['roles_path', 'force_handlers', 'start_at_task'])
    TestOptions.roles_path = ['./tests/fixtures/roles/include_role_test', './tests/fixtures/roles/role']


# Generated at 2022-06-13 09:06:36.213920
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    import ansible.playbook.role.definition
    import ansible.playbook.play
    import ansible.playbook.block
    import ansible.utils.display
    import os
    import shutil

    def clean_directory(directory):
        if os.path.exists(directory):
            shutil.rmtree(directory)
        os.makedirs(directory)

    def create_test_role_definition(name, directory='test_get_block_list', role=None, contents="fake_task_contents", handlers=None):
        directory = os.path.realpath(directory)
        main_role_path = os.path.join(directory, 'roles', name)
        os.makedirs(main_role_path)

# Generated at 2022-06-13 09:06:42.877955
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.inventory.inventory import Inventory
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    play_source = dict(
        name="Ansible Play",
        hosts='localhost',
        gather_facts='no',
        roles=['common'],
        vars=dict(
            ansible_connection='local'
        )
    )

    # create objects for UNIT test
    loader = DataLoader()
    variable_manager = VariableManager()

# Generated at 2022-06-13 09:06:48.568578
# Unit test for method get_include_params of class IncludeRole
def test_IncludeRole_get_include_params():
    """
    Test method IncludeRole.get_include_params
    """
    import ansible.utils.vars
    import ansible.constants as C
    import collections
    import copy
    import os
    import tempfile
    import yaml
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.template import Templar
    from unit.mock.loader import DictDataLoader
    from ansible.vars.manager import VariableManager
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.block import Block
    from ansible.playbook.role import Role
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.task_include import IncludeTask

# Generated at 2022-06-13 09:06:51.256531
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play


# Generated at 2022-06-13 09:07:02.427826
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():

    import ansible.playbook
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext

    host = ansible.inventory.host.Host(name="fake")
    my_loader = DataLoader()

    my_inventory = InventoryManager(loader=my_loader, sources='localhost,')
    my_inventory.add_host(host, group='all')
    my_inventory.add_group('fungroup')
    my_inventory.add_child('fungroup', 'all')
    my_inventory.reconcile_inventory()

    myplay = ansible.playbook.Play.load({'name': 'myplay', 'hosts': 'all'}, loader=my_loader)
    ir = IncludeRole

# Generated at 2022-06-13 09:07:11.274880
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():

    from ansible.playbook.block import Block
    # from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.vars.manager import VariableManager

    blk = Block()
    play = Play.load(dict(
        name="test play",
        hosts="localhost",
        roles=[],
    ))

    ir = IncludeRole(block=blk, role=None, task_include=None)

    # define role definition
    rd = RoleDefinition()
    # define role definition play
    rd._play = play
    rd.role_name = 'common'
    rd.role_path = '~/common'


# Generated at 2022-06-13 09:07:49.677210
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    from collections import namedtuple
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader


# Generated at 2022-06-13 09:07:58.753783
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():

    # test with 'name' option
    data = {'name': 'foo'}
    role = IncludeRole.load(data)
    assert role._role_name == 'foo'
    assert role.name is None

    # test with 'role' option
    data = {'role': 'foo'}
    role = IncludeRole.load(data)
    assert role._role_name == 'foo'
    assert role.name is None

    # test with both options
    data = {'name': 'foo', 'role': 'bar'}
    role = IncludeRole.load(data)
    assert role._role_name == 'foo'
    assert role.name is None

    # test with invalid options
    data = {'foo': 'foo', 'bar': 'bar'}
    role = IncludeRole.load(data)
    assert role

# Generated at 2022-06-13 09:08:09.871581
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    from ansible.playbook.block import Block
    from ansible.playbook.role.definition import RoleDefinition

    block = Block()
    block.vars = {'test_var': 'value'}
    block.roles = [RoleDefinition()]
    block.roles[0]._role_path = 'path/to/included/role'

    ir = IncludeRole()
    ir._parent = block
    ir._role_name = 'included_role_name'

    # Mock instance variables
    loader_mock = MagicMock()
    loader_mock.path_dwim.return_value = 'path/to/included/role'
    variable_manager_mock = MagicMock()

# Generated at 2022-06-13 09:08:17.066755
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    # set up role to import
    role_name = 'role_to_include'
    role_path = '../roles_to_include/role_to_include/'
    my_args = {
        'name': role_name,
        'tasks_from': '%s/tasks/main.yml' % role_path,
        'vars_from': '%s/defaults/main.yml' % role_path,
        'handlers_from': '%s/handlers/main.yml' % role_path,
    }
    my_block = Block()

    # build up a role that includes
    parent_role_name = 'parent_role'

# Generated at 2022-06-13 09:08:23.182262
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = "localhost"

    data = {
        "name": "common",
    }

    with pytest.raises(AnsibleParserError):
        IncludeRole.load(data, variable_manager=variable_manager, loader=loader)

    data = {
        "name": "common",
        "allow_duplicates": False,
        "apply": {
          "collect_facts": False
        },
        "public": False,
        "rolespec_validate": True,
    }


# Generated at 2022-06-13 09:08:33.703801
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    # test for IncludeRole
    from ansible.playbook.role_include import RoleInclude
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.block import Block
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    # Define role
    role = RoleDefinition()
    role._role_name = "bar"
    role._role_path = "/tmp/bar"

# Generated at 2022-06-13 09:08:46.873128
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    from ansible.playbook.playbook_include import PlaybookInclude
    from ansible.plugins.loader import lookup_loader
    import ansible.constants as C
    import os

    C.DEFAULT_ROLES_PATH = '../../../test/units/module_utils/include_role_units/'

    my_file_loader = lookup_loader()
    my_file_loader.set_basedir('../../../test/units/module_utils/include_role_units/')
    my_file_loader._basedir = u'../../../test/units/module_utils/include_role_units/'
    def __init__(self, block=None, role=None, task_include=None, use_handlers=False,
                 ignore_errors=False, data=None):
        pass

# Generated at 2022-06-13 09:08:54.199846
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    '''Test IncludeRole.get_block_list'''

    import ansible.constants as C
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.playbook.block import Block

    from ansible.playbook.task import Task
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.handler.task_handler import TaskHandler
    from ansible.executor.task_queue_manager import TaskQueueManager

    from ansible.utils.collection_loader import AnsibleCollectionConfig
    from ansible.utils.collection_loader._collection_finder import AnsibleCollectionFinder


# Generated at 2022-06-13 09:09:05.622035
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():

    class TestIncludeRole:
        pass

    # data = {'include_role': {'name': 'role1', 'public': True}}
    # data = {'include_role': {'name': 'role2.role3'}}
    # data = {'include_role': {'name': 'role3', 'tasks_from': 'tasks/main.yml'}}
    # data = {'include_role': {'name': 'role4', 'weird': 'weird'}}
    data = {'include_role': {'name': 'role4', 'tasks_from': [123, 'main.yml']}}
    
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.parsing.dataloader import DataLoader

# Generated at 2022-06-13 09:09:17.085074
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():

    class MockRole(object):
        def __init__(self, role_path):
            self._role_path = role_path

    class MockPlay(object):
        def __init__(self, roles):
            self.roles = roles

    class MockIncludeRole(TaskInclude):
        def __init__(self, **kwargs):
            self.args = kwargs

        def load_data(self, data, **kwargs):
            return self

    class MockBlock(Block):
        def __init__(self, role):
            self._role = role

    def myloader(path, **kwargs):
        available_vars = kwargs.get('available_vars')

# Generated at 2022-06-13 09:10:21.234430
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    from units.mock.loader import DictDataLoader
    from ansible.vars import VariableManager

    test_block = Block()
    test_hosts = 'testhost'
    test_vars = dict()
    test_options = dict()
    test_loader = DictDataLoader({ 'test': 'include_role', 'test2': 'include_role' })
    test_variable_manager = VariableManager()
    test_variable_manager.set_inventory(test_loader.inventory)

    test_inv_source = '{"test": {"name": "test", "hosts": ["testhost"]}}'
    test_inventory = test_loader.load_from_source(test_inv_source)[0]


# Generated at 2022-06-13 09:10:32.368948
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    import ansible.playbook.role.include
    loader = ansible.parsing.dataloader.DataLoader()
    variable_manager = ansible.utils.vars.VariableManager()
    include_role = ansible.playbook.role.include.IncludeRole.load(dict(name = 'name', role = 'role'), loader = loader, variable_manager = variable_manager)
    if include_role.name is None or include_role.name != 'name':
        raise AssertionError('IncludeRole.load should set the attribute name')
    if include_role._role_name is None or include_role._role_name != 'role':
        raise AssertionError('IncludeRole.load should set the attribute _role_name')


# Generated at 2022-06-13 09:10:40.423362
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    from ansible.playbook.role.include import RoleInclude

    class DummyRoleInclude(RoleInclude):
        GET_ROLE_PATH_CALLED = False
        GET_ROLE_NAME_CALLED = False

        def get_role_path(self):
            DummyRoleInclude.GET_ROLE_PATH_CALLED = True
            return "/home/user/roles"

        def get_role_name(self):
            DummyRoleInclude.GET_ROLE_NAME_CALLED = True
            return "mocked role"

    class DummyBlock(Block):
        def __init__(self, parent=None):
            self._parent = parent

    class DummyRole(Role):
        def get_handler_blocks(self):
            return []


# Generated at 2022-06-13 09:10:51.123194
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    import ansible.playbook
    import ansible.playbook.role
    import ansible.playbook.task
    from units.mock.loader import DictDataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    test_block = ansible.playbook.Block()
    test_play = ansible.playbook.Play().load({'name': 'test_play'}, variable_manager=VariableManager(), loader=DataLoader())
    r = ansible.playbook.role.Role()

    # test tasks_from
    a = 'tasks_from'
    data = {a: 'foo.yml'}

# Generated at 2022-06-13 09:10:59.973874
# Unit test for method get_include_params of class IncludeRole
def test_IncludeRole_get_include_params():
    from ansible.playbook.role_include import RoleInclude
    from ansible.playbook.role import Role
    from ansible.playbook.role_path import RolePath

    class FakeParentRole(Role):
        def __init__(self):
            super(FakeParentRole, self).__init__()
            self._metadata = {'name': 'parent_role'}
            self._role_path = RolePath(name='parent_role')

    p = FakeParentRole()

    ir = IncludeRole()
    ir.args = dict(role=dict(name='child_role'))

    assert ir.get_include_params() == dict(ansible_role_name='child_role')

    ir._parent_role = p

# Generated at 2022-06-13 09:11:13.675750
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    from ansible.playbook.play_context import PlayContext
    import ansible.plugins.loader as plugin_loader

    # TODO: this should mock the role loading and use actual role data
    r = IncludeRole()
    r._parent = 'parent'
    r._role_name = 'role_name'
    r._from_files = {'tasks': 'tasks/main.yml'}

    vars = {'a': 'b'}
    vars_templated = {'a': 'c'}

    mock_templar = type('mock_templar', (object,), {'template': lambda self, data: data})
    mock_loader = type('mock_loader', (object,), {'load_from_file': lambda self, path, basedir=None: ({}, '')})


# Generated at 2022-06-13 09:11:21.550285
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():

    from ansible.playbook.helpers import load_list_of_blocks

    data = dict(
        name='foo',
        allow_duplicates=False,
        rolespec_validate=False,
        apply={'serial': 1},
        public=True,
        tasks_from='/path/to/file.yml',
        vars_from='/path/to/file.yml',
        defaults_from='/path/to/file.yml',
        handlers_from='/path/to/file.yml',
    )

    res = load_list_of_blocks(
        [data],
        play=None,
        variable_manager=None,
        loader=None,
        parent_block=None,
    )
    assert res == (None, None)

# Generated at 2022-06-13 09:11:32.464711
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():

    Includerole = IncludeRole()
    Includerole._role_name = 'test_role_name'
    Includerole.public = 'test_public'
    Includerole._parent_role = 'test_parent_role'
    Includerole._allow_duplicates = 'test_allow_duplicates'
    Includerole.statically_loaded = 'test_statically_loaded'
    Includerole._role_path = 'test_role_path'
    Includerole._from_files = {'tasks':'main.yml', 'vars':'vars/main.yml', 'handlers':'handlers/main.yml'}


# Generated at 2022-06-13 09:11:40.047875
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():

    import tempfile
    import random
    import shutil
    import os
    import errno
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.errors import AnsibleParserError

    # create a temporary directory structure
    topdir = tempfile.mkdtemp()
    for role, subdir in (('test', 'tasks'), ('test2', 'tasks'), ('test3', 'tasks')):
        newdir = os.path.join(topdir, role, subdir)
        os.makedirs(newdir)

# Generated at 2022-06-13 09:11:51.427044
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    # set up the env
    import ansible.plugins.loader
    import ansible.plugins.action
    from ansible import context
    from ansible.utils.display import Display
    display = Display()
    display.verbosity = 3
    context.CLIARGS = {'verbosity': 3}

    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.playbook import Playbook
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    class Options(object):

        def __init__(self):
            self.connection = None
            self.forks = 0
            self.become = False