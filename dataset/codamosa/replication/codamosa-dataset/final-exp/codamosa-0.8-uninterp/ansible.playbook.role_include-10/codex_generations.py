

# Generated at 2022-06-13 09:02:52.395853
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():

    from ansible.playbook.role.include import RoleInclude
    from ansible.playbook.role.meta import RoleMetadata
    from ansible.parsing.dataloader import DataLoader

    variable_manager = VariableManager()
    variable_manager._extra_vars = {'some_var': 'foo'}
    loader = DataLoader()

    # include action
    data = {'include_role': 'some_role', 'public': True}
    ir = IncludeRole.load(data=data, variable_manager=variable_manager, loader=loader)
    assert ir.action == 'include_role'
    assert ir.statically_loaded == True
    assert isinstance(ir._parent_role, Role)
    assert isinstance(ir._parent_role._metadata, RoleMetadata)

# Generated at 2022-06-13 09:03:02.892464
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    def test_get_block_list():
        from ansible.playbook.play_context import PlayContext
        from ansible.plugins import module_loader
        from ansible.playbook.play import Play
        from ansible.inventory.manager import InventoryManager
        from ansible.parsing.dataloader import DataLoader
        from ansible.vars.manager import VariableManager

        dataloader = DataLoader()
        inventory = InventoryManager(loader=dataloader, sources=["localhost"])
        variable_manager = VariableManager(loader=dataloader, inventory=inventory)

        play_context = PlayContext()
        play_context.variable_manager = variable_manager
        play_context.CLIARGS = dict(tags=[])

        variable_manager.set_inventory(inventory)
        variable_manager.extra_v

# Generated at 2022-06-13 09:03:07.647075
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    '''Test the IncludeRole load method'''

    # Test
    block = Block()
    role_include = RoleInclude()
    role = Role()
    data = dict()
    data['name'] = 'my_fancy_name'
    data['role'] = 'my_fancy_role'
    data['apply'] = 'my_fancy_apply'

    role_include.load(data, block, role)

# Generated at 2022-06-13 09:03:14.207381
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    import ansible.utils.vars as vars
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.inventory.manager import InventoryManager
    from ansible.plugins.loader import plugin_loader

    loader = plugin_loader._find_plugins(('action_plugins', ))
    cache = dict()

    groups = {"all": {"vars": {"globalvar": "globalvalue"}}}
    hosts = {
        "example.com": {"vars": {"hostvar": "hostvalue"}},
        "example.org": {"vars": {"hostvar": "host2value"}},
        "example.net": {"vars": {"hostvar": "host3value"}},
    }
    inventory

# Generated at 2022-06-13 09:03:18.309863
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():
    '''
    In this test I call the method: get_name.
    The method should return the name of the task
    '''
    ir = IncludeRole()
    ir._role_name = 'roleName'
    assert ir.get_name() == "%s : roleName" % ir.action


# Generated at 2022-06-13 09:03:27.414368
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():
    display = Display()
    display.verbosity = 4

    data = dict(
        name = 'test1',
        role = 'test2',
    )
    irc = IncludeRole.load(data)
    assert(irc.get_name() == 'test1 : test2')

    data = dict(
        name = 'test1',
        tasks_from = 'main.yaml'
    )
    irc = IncludeRole.load(data)
    assert(irc.get_name() == 'test1')

    data = dict(
        name = 'test1',
    )
    irc = IncludeRole.load(data)
    assert(irc.get_name() == 'include_role : test1')

# Generated at 2022-06-13 09:03:38.700228
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    from ansible.playbook import Play, Role
    from ansible.playbook.block import Block
    from ansible.playbook.playbook import Playbook
    from ansible.playbook.task_include import TaskInclude
    from ansible.template import Templar
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.inventory.inventory import Inventory
    from ansible.inventory.manager import InventoryManager
    from ansible.utils.display import Display
    from ansible.parsing.dataloader import DataLoader
    import ansible.constants as C
    import json

    display = Display()

    # Prepare data

# Generated at 2022-06-13 09:03:49.674864
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    import sys
    if sys.version_info < (2, 7):
        import unittest2 as unittest
    else:
        import unittest

    def load(data, block, role, task_include=None, variable_manager=None, loader=None):
        return IncludeRole.load(data, block, role, task_include, variable_manager=variable_manager, loader=loader)

    class TestIncludeRoleLoad(unittest.TestCase):
        def test_public_option(self):
            # test with public option not allowed
            data = dict(action='ignore', include_role='test')
            self.assertRaises(AnsibleParserError, load, data, block=None, role=None)

            # test with public option allowed
            data = dict(action='include_role', include_role='test')

# Generated at 2022-06-13 09:03:50.610159
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    # TODO
    pass

# Generated at 2022-06-13 09:03:59.260677
# Unit test for method get_include_params of class IncludeRole
def test_IncludeRole_get_include_params():

    class Role(object):
        def __init__(self):
            self.name = 'test'
            self.path = 'foo'
            self.metadata = {}
            self._role_params = {'test': 'test1'}
        def get_name(self):
            return self.name
        def get_role_params(self):
            return self._role_params

    class Parent_Role(object):
        def __init__(self):
            self.name = 'test2'
            self.path = 'foo2'
            self.metadata = {}
            self._role_params = {'test2': 'test3'}
        def get_name(self):
            return self.name
        def get_role_params(self):
            return self._role_params


    test_role = Role()
   

# Generated at 2022-06-13 09:04:14.238546
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    def dummy_loader_mock(self):
        return None
    def dummy_variable_manager_mock(self):
        return None

    block = Block()

# Generated at 2022-06-13 09:04:24.079091
# Unit test for method get_include_params of class IncludeRole
def test_IncludeRole_get_include_params():
    i = IncludeRole()
    i._parent = Block()
    i._parent_role = Role()
    i._parent_role.get_name = lambda: 'base'
    i._parent_role._role_path = 'path'
    i._parent_role.get_role_params = lambda: { 'ansible_role_params': True }
    params = i.get_include_params()

    assert params.get('ansible_parent_role_names') == ['base']
    assert params.get('ansible_parent_role_paths') == ['path']
    assert params.get('ansible_role_params') == True

    new_parent = Block()
    new_parent.get_name = lambda: 'new'
    new_parent._role_path = 'new_path'
    new_parent.get_role

# Generated at 2022-06-13 09:04:35.692265
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    test_data = {
        'block': None,
        'role': None, 'task_include': None,
        'data': {
            'bar': 'foo',
            'name': 'test',
            'allow_duplicates': False,
            'apply': {
                'tags': ['test'],
            }
        }
    }
    ir = IncludeRole(**test_data)

    # test simple role include
    result = ir.load(test_data['data'])
    assert result._role_name == 'test'
    assert result.args['allow_duplicates'] == False
    assert result.apply == {'tags': ['test']}

    test_data['data']['apply']['tags'].append('include')
    test_data['data']['apply']['skip_tags']

# Generated at 2022-06-13 09:04:42.519115
# Unit test for method get_include_params of class IncludeRole
def test_IncludeRole_get_include_params():
    role_name = 'test_role'
    role_path = '/usr/share/ansible/test_role'
    roles = [{'name': role_name, 'path': role_path}]
    p_role = Role().load({'name': role_name, 'roles': roles, 'metadata': {'role_path': role_path}})
    i_role = IncludeRole(role_name, p_role)
    include_params = i_role.get_include_params()
    if include_params is None:
        raise AssertionError("Return value of get_include_params is None.")
    if len(include_params) != 2:
        raise AssertionError("Length of include_params is not 2.")

# Generated at 2022-06-13 09:04:57.613121
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    class Test_play(object):
        def __init__(self, name=None):
            self.name = name
            self.handlers = []
            self.roles = []

    class Test_block(object):
        def __init__(self, name=None):
            self._parent = None
            self.name = name
            self.exclude_tasks = []
            self.static_tasks = []
            self.rescue_tasks = []
            self.always_tasks = []
            self.block = None
            self.vars = {}

        def load_data(self, data, variable_manager=None, loader=None):
            self.name = data.get('name', None)
            self.exclude_tasks = data.get('exclude_tasks', [])
            self.static

# Generated at 2022-06-13 09:05:06.786357
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    from ansible.playbook.block import Block
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.handler import Handler
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task

    my_block = Block.load(dict(
        name="block 1",
        meta={"fs": "xfs"},
        tasks=[
            dict(action=dict(module='debug', args=dict(msg='block 1 task 1')),
                 when="x1",
                 loop="loop1"),
            dict(action=dict(module='debug', args=dict(msg='block 1 task 2')),
                 when="x2",
                 loop="loop1"),
        ]
    ), play=None, role=None, task_include=None)

    my_handler = Handler

# Generated at 2022-06-13 09:05:18.793472
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    data1 = dict(
        name='test_role',
    )
    assert IncludeRole.load(data1)._role_name == 'test_role'

    data2 = dict(
        role='test_role_alias',
    )
    assert IncludeRole.load(data2)._role_name == 'test_role_alias'

    # Default value for _rolespec_validate should be True
    assert IncludeRole.load(data1)._rolespec_validate == True

    data3 = dict(
        name='test_role_2',
        public=True,
        allow_duplicates=False,
        rolespec_validate=False,
    )
    assert IncludeRole.load(data3)._role_name == 'test_role_2'

# Generated at 2022-06-13 09:05:28.279183
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    from ansible.playbook.block import Block
    from ansible.playbook.play import Play
    from ansible.playbook.role import Role
    from ansible.template import Templar

    before = {'name': 'test_role',
              'vars_from': 'file.yml'}
    after = {'name': 'test_role',
             'vars': {'var': 'file.yml'},
             'tasks': []}

    # parameters initialization
    block = Block.load(before, play=Play().load({}),
                       task_include=IncludeRole.load(before, play=Play().load({}), role=Role()))
    templar = Templar(loader=None, variables={'var': 'file.yml'})
    loader = None
    variable_manager = None

    #

# Generated at 2022-06-13 09:05:34.731233
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():

    from ansible.playbook.conditional import Conditional
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.task_include import TaskInclude

    block = Block()
    role = RoleDefinition()
    task_include = TaskInclude(block=block, role=role)

    # test __init__
    ir = IncludeRole(block=block, role=role, task_include=task_include)
    assert isinstance(ir, IncludeRole)
    assert isinstance(ir, Conditional)
    #assert isinstance(ir, Include)
    assert isinstance(ir, TaskInclude)
    assert isinstance(ir, Block)
    assert isinstance(ir, Base)
    assert isinstance(ir, Role)
    assert isinstance(ir, RoleDefinition)

# Generated at 2022-06-13 09:05:47.250113
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():
    from ansible.playbook.role import Role
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.inventory.inventory import Inventory
    from ansible.parsing.dataloader import DataLoader
    from collections import namedtuple
    from ansible.executor.task_queue_manager import TaskQueueManager

    # initialize needed objects
    Options = namedtuple('Options', ['connection', 'module_path', 'forks', 'become', 'become_method', 'become_user', 'check', 'diff'])
    options = Options

# Generated at 2022-06-13 09:06:04.126224
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():
    task = IncludeRole()
    task.action = 'role'
    task._role_name = 'test_role_name'
    assert task.get_name() == "role : test_role_name"

    task._role_name = None
    assert task.get_name() == "role : None"

# Generated at 2022-06-13 09:06:11.766541
# Unit test for method get_include_params of class IncludeRole
def test_IncludeRole_get_include_params():
    from collections import namedtuple
    FakeRole = namedtuple('FakeRole', ['get_role_params', '_role_path'])
    ir = IncludeRole()
    # Case 1: No parent role
    assert ir.get_include_params() == {}
    
    # Case 2: With parent role
    fake_parent_role = FakeRole(
            get_role_params=lambda: {
                    'ansible_role_context': 'production',
                    'ansible_role_uuid': 'fake_uuid',
                    'ansible_role_name': 'fake_role_name'
                    },
            _role_path='/fake/path'
            )
    ir._parent_role = fake_parent_role

# Generated at 2022-06-13 09:06:20.102994
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():

    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.role.include import RoleInclude
    from ansible.playbook.role import Role

    from ansible import constants as C

    from ansible.module_utils.six import PY2

    import pytest
    from ansible.module_utils._text import to_bytes, to_text
    from ansible.module_utils.parsing.convert_bool import boolean


# Generated at 2022-06-13 09:06:27.950841
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    import sys
    import os

    # Setting the current path to ansible source
    ansible_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    sys.path.append(ansible_path)
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play

    play_context = PlayContext()
    play_source = dict(hosts='all', gather_facts='no', roles=['role0', 'role1'], vars=dict(role_var='role_var_value'))
    # Test get_block_list with play context and play source
    play = Play().load(play_source, None, variable_manager=None, loader=None)
    parent_role = play

# Generated at 2022-06-13 09:06:40.716431
# Unit test for method get_include_params of class IncludeRole
def test_IncludeRole_get_include_params():
    from ansible.playbook.play_context import PlayContext

    context = PlayContext()
    context.CLIARGS = {'connection': 'local',
                       'module_path': None,
                       'forks': 10,
                       'remote_user': 'root',
                       'private_key_file': None,
                       'ssh_common_args': '',
                       'ssh_extra_args': '',
                       'sftp_extra_args': '',
                       'scp_extra_args': '',
                       'become': False,
                       'become_method': 'sudo',
                       'become_user': 'root',
                       'verbosity': 0,
                       'check': False}

    include_block = Block(role=Role(name='test_Role'))

# Generated at 2022-06-13 09:06:45.151045
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    data = {'action': 'include_role', 'name': 'test'}
    include_role = IncludeRole.load(data)
    assert include_role._role_name == 'test'
    assert 'test' in include_role._parent._play._role_names

# Generated at 2022-06-13 09:06:54.822883
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    import unittest
    import ansible.playbook
    import ansible.inventory
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    class TestIncludeRoleGetBlockList(unittest.TestCase):

        def setUp(self):
            pass

        def tearDown(self):
            pass

        def test__get_block_list(self):
            loader = DataLoader()
            variable_manager = VariableManager()
            inventory = ansible.inventory.Inventory(loader=loader, variable_manager=variable_manager, host_list=[])

# Generated at 2022-06-13 09:07:05.808758
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    from ansible.module_utils.six import iteritems
    from ansible.vars import VariableManager
    from ansible.parsing.plugin_docs import read_docstring
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.role_include import RoleInclude

    # Load data
    role_include_data = {
        'include_role': {
            'name': 'foo',
            'tasks_from': 'main.yml'
        }
    }

    # Use fake loader to load data by using DataLoader
    class FakeLoader:
        def load_from_file(self, path):
            return role_include_data

    # Initialize objects for IncludeRole class
    variable_manager = VariableManager()
    loader = DataLoader()
    fake_loader = FakeLoader

# Generated at 2022-06-13 09:07:09.164027
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():
    ir = IncludeRole()
    ir.name = "test"
    ir._role_name = "role_name"
    assert ir.get_name() == "test : role_name"

# Generated at 2022-06-13 09:07:18.310899
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    from ansible.playbook.block import Block
    from ansible.playbook.play import Play
    from ansible.playbook.role import Role

    data = dict(
        name='galaxy.nginx',
        foo='bar',
    )
    # Missing required field 'name'
    try:
        IncludeRole.load(data)
    except AnsibleParserError:
        pass
    else:
        raise Exception('test failed')

    # field 'name' can be an alias of 'role'
    data = dict(
        role='galaxy.nginx',
        foo='bar',
    )
    include_role = IncludeRole.load(data)
    assert include_role._role_name == 'galaxy.nginx'

    # should raise AnsibleParserError when field 'public' exists

# Generated at 2022-06-13 09:07:51.369535
# Unit test for method get_include_params of class IncludeRole
def test_IncludeRole_get_include_params():
    ir = IncludeRole()
    ir._parent_role = None
    assert ir.get_include_params() == {}

    class MockRole(object):

        def get_role_params(self):
            return {'foo': 'bar'}

        def get_name(self):
            return 'baz'

    ir = IncludeRole()
    ir._parent_role = MockRole()
    ir._parent_role._role_path = 'qaz'
    result = ir.get_include_params()
    assert result == {
        'ansible_parent_role_names': ['baz'],
        'ansible_parent_role_paths': ['qaz'],
        'foo': 'bar',
    }

# Generated at 2022-06-13 09:07:59.760716
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    '''
    Basic include role test
    '''

    #
    # Invalid options
    #

    # bad option name
    test_dict = dict(name="my_role", bad_option="bad")
    try:
        IncludeRole.load(test_dict)
        assert False, "Unexpected success"
    except AnsibleParserError:
        pass

    #
    # name and role
    #

    # name is required
    test_dict = dict(not_name="my_role")
    try:
        IncludeRole.load(test_dict)
        assert False, "Unexpected success"
    except AnsibleParserError:
        pass

    # name is required
    test_dict = dict()

# Generated at 2022-06-13 09:08:10.769617
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar

    # setup
    display = Display()
    play_context = PlayContext(verbosity=0)

    # list of valid options/values to check
    # -- from_task_options
    # -- from_vars_options
    # -- from_handler_options
    # -- from_task_from
    # -- from_vars_from
    # -- from_handler_from
    # -- apply
    # -- static_include
    # -- allow_duplicates
    # -- public
    # -- rolespec_validate
    # -- strict
    # -- ignore_errors
    # -- when
    # -- always_run
    # -- register
    # -- delegate_to
    # -- delegate_facts
    # -- until
   

# Generated at 2022-06-13 09:08:25.202794
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    data = dict(action='include_role', name='mongo', apply=dict(), vars=dict(name='mongo'),
                when=dict(test='test'), static_vars=dict(name='static_vars'), static_vars_from='static_vars.yml')
    include_role = IncludeRole.load(data)
    assert include_role.name == 'mongo'
    assert include_role.action == 'include_role'
    assert include_role.apply == dict()
    assert include_role.vars == dict(name='mongo')
    assert include_role.when == dict(test='test')
    assert include_role.static_vars == dict(name='static_vars')
    assert include_role._from_files == dict(static_vars='static_vars.yml')

# Generated at 2022-06-13 09:08:38.061102
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    from ansible.playbook.play import Play
    from ansible.playbook.block import Block
    from ansible.playbook.role.include import TaskInclude
    from ansible.template import Templar


# Generated at 2022-06-13 09:08:49.767483
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():

    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.play_iterator import PlayIterator
    from ansible.executor.task_queue_manager import TaskQueueManager

    import ansible.executor.task_result as task_result
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    import sys
    import json

    play_source = dict(
        name = "Compile",
        hosts = 'all',
        gather_facts = 'no',
        roles = ['role1']
    )


# Generated at 2022-06-13 09:08:50.312205
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    pass

# Generated at 2022-06-13 09:08:50.957388
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    pass

# Generated at 2022-06-13 09:08:52.035452
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    pass


# Generated at 2022-06-13 09:09:03.983688
# Unit test for method get_include_params of class IncludeRole
def test_IncludeRole_get_include_params():
    print("Testing IncludeRole get_include_params")

    # get_include_params, no parent role.
    ir = IncludeRole()
    v = ir.get_include_params()
    assert v == {'ansible_version': {'full': '', 'major': 0, 'minor': 0}, 'ansible_playbook_python': ''}

    # get_include_params, with parent role
    pr = Role()
    pr.name = 'parent_role'
    pr._role_path = './'
    pr._role_params = {'role': 'param_value'}
    ir._parent_role = pr
    v = ir.get_include_params()
    assert v['role'] == 'param_value'
    assert v['ansible_parent_role_names'] == ['parent_role']

# Generated at 2022-06-13 09:09:58.797406
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():

    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.block import Block

    block = Block()
    task_include = TaskInclude()
    data = { 'name': 'foo' }

    ir = IncludeRole.load(data, block, task_include=task_include)
    assert ir._role_name == 'foo'
    assert ir.args['name'] == 'foo'
    assert ir._from_files == {}

    ir = IncludeRole.load({ 'role': 'bar' }, block, task_include=task_include)
    assert ir._role_name == 'bar'
    assert ir.args['role'] == 'bar'


# Generated at 2022-06-13 09:09:59.463946
# Unit test for method get_include_params of class IncludeRole
def test_IncludeRole_get_include_params():
    pass

# Generated at 2022-06-13 09:10:10.121530
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    ''' import and instantiate IncludeRole class and test:
          load
    '''
    #
    # Import module(s) under test
    #
    from ansible.playbook.role.include import IncludeRole

    #
    # Setup the IncludeRole test object
    #
    data1 = dict(
        include="role1"
    )
    #
    # Exercise the IncludeRole.load method
    #
    try:
        IncludeRole.load(data1)
    except Exception as e:
        assert e.message == "'name' is a required field for include_role."

    data2 = dict(
        name="role1"
    )
    my_ir = IncludeRole.load(data2)
    assert my_ir.action == 'include_role'
    assert my_ir.block is None
    assert my_

# Generated at 2022-06-13 09:10:10.908272
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    pass

# Generated at 2022-06-13 09:10:24.371050
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    my_block = Block(parent_block=None)
    test_data = {'apply': '', 'defaults_from': '', 'handlers_from': '', 'include_tasks': '', 'name': '', 'role': '', 'tasks_from': '', 'tags': '', 'vars_from': ''}
    my_role = Role()
    my_include_task = include_task.IncludeTask()
    my_variable_manager = variable_manager.VariableManager()
    my_loader = loader.Loader()
    test_IncludeRole_load = IncludeRole.load(test_data, block=my_block, role=my_role, task_include=my_include_task, variable_manager=my_variable_manager, loader=my_loader)
    assert test_IncludeRole_load._from_

# Generated at 2022-06-13 09:10:35.707388
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    display.verbosity = 4
    play = dict(
        name = "blah",
        hosts = "all",
        gather_facts = "no",
        connection = "local",
        roles = [],
        tasks = [
            dict(action=dict(module="shell", args="ls"), name="dummy task")
        ]
    )

    def check_tasks(tasks):
        assert len(tasks) == 1, tasks
        first_task = tasks[0]
        assert first_task._role.get_name() == 'zoo', first_task._role.get_name()

    def test_no_rolespec_validate(ir):
        ir.rolespec_validate = False

        test_role = 'zoo'
        ir._role_name = test_role

# Generated at 2022-06-13 09:10:47.386903
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():

    # Arrange
    loader = DictDataLoader({
        "test/unittest.yml": """
- include_role: name=role2 apply=other_task_print
  vars:
    testvar_1: someval
    testvar_2: someval
""",
        "role2/tasks/main.yml": """
tasks:
  - debug: msg={{ testvar_2 }}
""",
    })

    # Act
    role_include = RoleInclude.load(name='role2', play=Play(), loader=loader)

    # Assert
    assert len(role_include._parent_role._role_blocks) == 1

    block = role_include._parent_role._role_blocks[0]

# Generated at 2022-06-13 09:10:48.499446
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    pass


# Generated at 2022-06-13 09:10:54.724543
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():
    block = Block(parent=None, role=None, task_include=None, use_handlers=False, connection='test_connection', network_os='test_network_os', name='test_block', until=None, retries=0, rescue=None, always=None, delegate_to='127.0.0.1')
    role = Role()
    task_include = TaskInclude()
    obj = IncludeRole(block=block, role=role, task_include=task_include)
    assert obj.get_name() == "include_role : None"

# Generated at 2022-06-13 09:11:09.402773
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    my_hosts = ["localhost"]
    my_variable_manager = "my_variable_manager"
    my_loader = "my_loader"
    my_play = "my_play"

    # check when len(from_files) == 0
    my_block = "my_block"
    my_role = "my_role"
    my_task_include = "my_task_include"
    my_from_files = {}
    my_args = {"role": "my_role_name"}
    my_parent_role = "my_parent_role"
    my_annotation = "my_annotation"
    my_expanded_from = "my_expanded_from"
    my_action = "my_action"
    my_collections = "my_collections"