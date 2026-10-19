

# Generated at 2022-06-13 09:02:56.382364
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=None)
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    play_source =  dict(
            name = "Ansible Play",
            hosts = 'test',
            gather_facts = 'no',
            roles = [
                dict(
                    name = 'foo',
                    tasks = [
                        dict(name='test', action='include_role', args=dict(name='test'))
                    ]
                )
            ]
        )



# Generated at 2022-06-13 09:02:57.394104
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    # TODO: add a unit test for this class
    pass


# Generated at 2022-06-13 09:03:03.424748
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    from ansible.playbook.block import Block
    from ansible.playbook.handler import Handler
    from ansible.playbook.task import Task
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    # Create IncludeRole instance
    block = Block()
    # Create Role instance
    role = Role()
    # Create TaskInclude instance
    task_include = TaskInclude()
    # make IncludeRole instance
    include_role = IncludeRole(block=block, role=role, task_include=task_include)

    # set _role_name
    include_role._role_name = 'test_role'
    include_role._role_path = '/opt/ansible/roles/test_role'
    # Create Role instance
    role = Role()


# Generated at 2022-06-13 09:03:14.248331
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    import ansible.playbook.task_include
    import ansible.playbook.role
    display.verbosity = 3
    # Place for setup code for unit test of class IncludeRole
    yaml_obj0 = {'block': 'block0', 'action': 'action0', 'name': 'name0', 'role': 'role0', 'statically_loaded': True,
     'args': {'name': 'name1', 'role': 'role1'}, 'post_validate_data': {}}
    yaml_obj1 = {'block': 'block1', 'action': 'action1', 'name': 'name1', 'role': 'role1', 'statically_loaded': False,
     'args': {'name': 'name2', 'role': 'role2'}, 'post_validate_data': {}}
    role0

# Generated at 2022-06-13 09:03:25.265370
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():
    # Create an instance of IncludeRole class.
    ir = IncludeRole()
    # Check if get_name method return name of include_role task
    assert ir.get_name() == "include_role : No name given"

    # Create an instance of IncludeRole class.
    ir = IncludeRole(name="task_name")
    # Check if get_name method return name of include_role task
    assert ir.get_name() == "task_name : No name given"

    # Create an instance of IncludeRole class.
    ir = IncludeRole(name="task_name", role="role_name")
    # Check if get_name method return name of include_role task
    assert ir.get_name() == "task_name : role_name"


# Generated at 2022-06-13 09:03:28.124143
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():
    args = dict(name='test', role='test')
    include_role = IncludeRole(action='include_role', args=args)
    assert include_role.get_name() == 'include_role : test'

# Generated at 2022-06-13 09:03:39.495474
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    """
    Unit test for method load of class IncludeRole
    """

    data = {
        "name": "geerlingguy.jenkins",
    }

    include_role = IncludeRole.load(data)

    assert include_role._role_name == data["name"]
    assert include_role.from_files == {}
    assert include_role._role_path is None
    assert include_role._parent_role is None
    assert include_role.statically_loaded == False
    assert include_role.vars == {}

    assert include_role.static is False
    assert include_role.delegate_to is None
    assert include_role.loop is None


# Generated at 2022-06-13 09:03:49.216613
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():
    from ansible.playbook.task import Task
    from ansible.playbook.role import Role
    from ansible.playbook.play import Play

    play = Play.load({
        'name': 'test play',
        'hosts': 'localhost',
        'roles': [{'role': 'test_role'}]
    })

    role = Role.load(
        name='test_role',
        role_path='/path/to/test_role',
        play=play
    )
    task = Task.load(dict(include_role=dict(name='test_role')))
    task._role = role
    assert task.get_name() == "include_role : test_role"

# Generated at 2022-06-13 09:03:58.028165
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.play import Play
    from ansible.module_utils.six import iteritems

    p1 = Play()
    p1_vars = {'a': 1, 'b': 2, 'c': 3}

    p2 = Play()
    p2_vars = {'z': 26, 'y': 25, 'x': 24}

    r1 = RoleDefinition()
    r1.vars = {'a': 1, 'b': 1, 'c': 1}
    r1.name = 'r1'
    r1.parent_role = None
    r1._role_path = '/var/lib/ansible/roles/r1'

    r2 = RoleDefinition()

# Generated at 2022-06-13 09:04:00.046204
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    # @todo we have no unit test coverage for this class yet
    pass

# Generated at 2022-06-13 09:04:07.582046
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    pass

# Generated at 2022-06-13 09:04:16.256122
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    from ansible.playbook.play import Play
    from ansible.playbook.role import Role

    from ansible.vars.manager import VariableManager
    from ansible.inventory import Inventory

    from io import StringIO

    from ansible.parsing.dataloader import DataLoader

    # Create a block for the test class
    block = Block()

    # Create a play for the test class
    play = Play.load(dict(name="Dummy play", hosts=['all']), variable_manager=VariableManager(), loader=DataLoader())

    # Create a role for the test class
    role = Role.load(dict(name="Dummy role"), play=play, variable_manager=VariableManager(), loader=DataLoader())

    # Initialize a IncludeRole test object, a TaskInclude object is the first argument
    # of the constructor.


# Generated at 2022-06-13 09:04:25.145549
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():
    print("Test get_name")
    ir = IncludeRole()
    # set name, will be returned
    ir.name = 'role-name'
    name = ir.get_name()
    assert name == 'role-name'
    # no name, but role_name is set
    ir.name = None
    ir._role_name = 'role-name'
    name = ir.get_name()
    assert name == 'include_role : role-name'
    # no name, no role_name
    ir.name = None
    ir._role_name = None
    name = ir.get_name()
    assert name == 'include_role : None'


if __name__ == "__main__":
    test_IncludeRole_get_name()

# Generated at 2022-06-13 09:04:36.626055
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():

    data = dict(name='foo', tags=['bar'], when='baz')
    # role is not defined
    try:
        IncludeRole.load(data)
    except AnsibleParserError:
        pass
    else:
        assert False, "role is not defined: unexpected pass"

    data['role'] = 'foo'
    # name is not defined
    try:
        IncludeRole.load(data)
    except AnsibleParserError:
        pass
    else:
        assert False, "name is not defined: unexpected pass"

    # name is defined
    data['name'] = 'foo'
    IncludeRole.load(data)

    data['bad_opts'] = 'bar'
    try:
        IncludeRole.load(data)
    except AnsibleParserError:
        pass

# Generated at 2022-06-13 09:04:47.064360
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():

    # Unit test for method load of class IncludeRole
    # Positive Cases
    # Case 1: include_role as action with basic arguments
    data = {"include_role": {"name": "test"}}
    role, role_include = IncludeRole.load(data)
    assert role.name == "test"
    assert role.action == "include_role"
    assert not role.allow_duplicates
    assert not role.tasks_from
    assert not role.vars_from
    assert not role.defaults_from
    assert not role.handlers_from
    assert not role.apply
    assert not role.public
    assert role._from_files == {}
    assert role._parent_role is None

    # Case 2: include_role as action with basic arguments and with_items

# Generated at 2022-06-13 09:04:57.742042
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.template import Templar
    from ansible.utils.display import Display
    from ansible.vars.manager import VariableManager
    from ansible.vars.unsafe_proxy import UnsafeProxy

    display = Display()
    loader = 'ansible.parsing.dataloader.DataLoader'
    templar = Templar(loader=loader)
    variable_manager = VariableManager()
    role_definition = RoleDefinition(
        'test_role_definition',
        loader=loader
    )

    # create a role

# Generated at 2022-06-13 09:05:06.871849
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    # data is a dict
    data = dict(
        name="test",
        tasks_from="test_tasks",
        vars_from="test_vars",
        defaults_from="test_defaults",
        handlers_from="test_handlers",
        apply={
            "test_apply_key": "test_apply_value"
        },
        public="test_public",
        allow_duplicates="test_allow_duplicates"
    )
    # block is a Block
    block = Block()
    block.vars.update(dict(ansible_version="test_ansible_version"))
    block.role = Role()

    # test IncludeRole.load
    ir = IncludeRole.load(data, block=block)

    # check ir
    assert isinstance(ir, IncludeRole)

# Generated at 2022-06-13 09:05:07.685372
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    pass

# Generated at 2022-06-13 09:05:19.219785
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():

    # test for IncludeRole._get_block_list to make sure it's loading in the blocks from the role correctly
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.role import Role
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.role.meta import RoleMetadata


# Generated at 2022-06-13 09:05:28.600495
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    import pytest
    data = {'chdir': '/home/user', 'include': 'role'}
    block = Block('test')
    role = Role()
    ir = IncludeRole.load(data, block, role)
    # METHOD: load
    assert isinstance(ir, IncludeRole)
    with pytest.raises(AnsibleParserError) as e:
        ir._role_name is None
    data = {'name': 'role1'}
    ir = IncludeRole.load(data, block, role)
    with pytest.raises(AnsibleParserError) as e:
        ir._role_name is None
    data = {'role': 'role1'}
    ir = IncludeRole.load(data, block, role)
    assert ir._role_name == 'role1'



# Generated at 2022-06-13 09:05:54.952535
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    """
    include_role:
      name: test-role
    """
    # TODO: Write this unit test
    pass

# Generated at 2022-06-13 09:05:58.073525
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():
    ir = IncludeRole()
    ir._role_name = 'test'
    assert ir.get_name() == 'include_role : test'


# Generated at 2022-06-13 09:06:07.736741
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    """
    Test the load method of IncludeRole.
    """

    task = dict(
        name='test_include_role',
        action='include_role',
        args=dict(
            name='test_role',
            allow_duplicates=True,
            public=False,
            rolespec_validate=True
        )
    )

    # create an instance of IncludeRole with an action always present in C._ACTION_INCLUDE_ROLE
    ir = IncludeRole.load(task, task_include=task)

    assert ir.name == 'test_include_role'
    assert ir.action == 'include_role'
    assert ir._parent_role is None
    assert ir._role_name == 'test_role'
    assert isinstance(ir._from_files, dict)
    assert ir._from_files

# Generated at 2022-06-13 09:06:22.155269
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.playbook.block import Block

    loader = DataLoader()
    inventory = InventoryManager(loader=loader)
    var_manager = VariableManager()
    pbex = PlaybookExecutor(playbooks=['./test_include_role.yml'], inventory=inventory, variable_manager=var_manager, loader=loader, options={})
    actual_play = pbex._entries[0]
    block_name = "include_role_test"

# Generated at 2022-06-13 09:06:34.574573
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    from ansible.playbook.play_context import PlayContext
    import ansible.cli.playbook
    cli = ansible.cli.playbook.CLI()
    opts = cli.base_parser(None).parse_args([])[0]
    play_context = PlayContext(opts)

# Generated at 2022-06-13 09:06:42.360601
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager

    block = Block()
    block.vars = dict(a=1, b=2)
    ir = IncludeRole(block=block, role=None, task_include=None)
    ir.vars = dict(a=3, d=4)

    ir.args = dict()
    ir.action = 'include_role'
    ir.name = 'test-role'
    ir.rolespec_validate = False
    ir.statically_loaded = True

    loader = DataLoader()
    variable_manager = VariableManager()
    variable_

# Generated at 2022-06-13 09:06:53.069025
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    data = dict(
        name='role_2',
        tasks_from='role_1/tasks.yml',
        vars_from='vars/main.yml',
        allow_duplicates=False,
        rolespec_validate=True,
        apply=dict(
            when="is_precise",
            tags='precise')
    )
    ir = IncludeRole.load(data)
    assert ir._from_files == dict(
        tasks='tasks.yml',
        vars='main.yml'
    )
    assert ir.allow_duplicates is False
    assert ir.rolespec_validate is True
    assert ir.apply == dict(
            when="is_precise",
            tags='precise')
    assert ir._role_name == 'role_2'



# Generated at 2022-06-13 09:07:04.604818
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar

    class Role_load:
        def __init__(self, role_name):
            self._role_name = role_name
            self._metadata = dict(
                collections=[],
            )

    class Role(Role_load):
        def get_handler_blocks(self, *args, **kwargs):
            return []

        def compile(self, *args, **kwargs):
            return []

    class IncludeRole(IncludeRole_load):
        def __init__(self, allow_duplicates=True, public=False, rolespec_validate=True):
            self.allow_duplicates = allow_duplicates
            self.public = public
            self.rolespec_validate = rolespec_validate


# Generated at 2022-06-13 09:07:15.639593
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    import ansible.playbook
    import ansible.plugins.loader
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    loader = DataLoader()
    play = ansible.playbook.Play.load(dict(name='test play', hosts=['localhost'], roles=[], gather_facts=False), loader=loader, variables=dict())
    role = ansible.plugins.loader.role_loader.get(dict(name='test role'), play=play)
    block = Block.load(dict(name='test block', tasks=[]), play=play)

    # Empty block
    ir = IncludeRole.load(dict(name='test role'), block=block, role=role)
    blocks = ir.get_block_list()[0]
    assert not blocks

   

# Generated at 2022-06-13 09:07:26.628409
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    import ansible.playbook.task
    import ansible.playbook.play
    import ansible.playbook.block
    import ansible.playbook.role

    # create the Play
    play_ds = dict(
        name="foobar",
        hosts='all',
        gather_facts='no'
    )
    play = ansible.playbook.play.Play().load(play_ds, variable_manager=None, loader=None)

    # create the Role
    role = ansible.playbook.role.Role()
    role._role_path = "/home/username/ansible_dir/roles/dummy"

    # create the IncludeRole
    include_role_ds = dict(
        name="dummy",
        role="web",
        tasks_from="main.yml"
    )
    include_

# Generated at 2022-06-13 09:08:00.459070
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.inventory import Inventory
    from ansible.vars.manager import VariableManager
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.process.worker import WorkerProcess

    class TestIncludeRole(IncludeRole):
        def __init__(self):
            super(TestIncludeRole, self).__init__()

    # Create Mock objects
    kwargs = {'_initial_variables': {}}
    host = FakeHost()
    task_vars = TaskVars(host, kwargs['_initial_variables'])
    play_context = PlayContext()
    play_context._play = Play()
    play_context._play._included

# Generated at 2022-06-13 09:08:11.421971
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():

    # 1. include_role, get_block_list
    # Just need to make sure that the method doesn't raise any exception, even in the absence of play, variable_manager and loader.
    from ansible.playbook.play import Play
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.role import Role
    from ansible.playbook.play_context import PlayContext

# Generated at 2022-06-13 09:08:13.266693
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    display.display('test_IncludeRole_load')
    assert True

# Generated at 2022-06-13 09:08:27.664615
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():

    # Test requires all options provided to load
    # Test requires all playbooks and roles in playbook path
    playbook_path = '/etc/ansible/roles'

    # Create mock data (dict) to pass to load of class IncludeRole

# Generated at 2022-06-13 09:08:41.169398
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    import pytest

    data = {
        'action': 'include_role',
        'args': {
            'name': 'foo',
            'public': True,
            'tasks_from': 'foo',
            'vars_from': 'bar',
            'defaults_from': 'baz',
            'handlers_from': 'qux',
            'allow_duplicates': False,
            'apply': { 'metadata': None },
            'rolespec_validate': True,
        },
        'loop': 'all',
        'loop_control': { 'loop_var': 'item' },
        'when': 'ansible_distribution',
    }

    with pytest.raises(AnsibleParserError, match='Invalid options for include_role'):
        IncludeRole.load(data)

   

# Generated at 2022-06-13 09:08:43.037964
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    # TODO: write unit test for method get_block_list of class IncludeRole
    pass

# Generated at 2022-06-13 09:08:52.615991
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    inv_data = {
        'all': {
            'vars': {
                'foo': 'bar'
            }
        },
        'ungrouped': {
            'vars': {
                'foo': 'baz'
            }
        }
    }
    inventory = InventoryManager(loader=loader, sources=inv_data)
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    def _parse_playbook(d):
        from ansible.playbook.play import Play

# Generated at 2022-06-13 09:09:04.546724
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():

    import yaml

    # only need play passed in when dynamic
    myplay = None

    # set up a temporary file/path for testing with
    import tempfile
    (fh1, task_vars) = tempfile.mkstemp()

    # define variables for testing

# Generated at 2022-06-13 09:09:12.461637
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():
    task = IncludeRole()
    task.name = 'foo'
    task.action = 'bar'
    task._role_name = 'baz'
    assert task.get_name() == 'foo : baz'

    task.name = None
    assert task.get_name() == 'bar : baz'

    task.name = 'foo'
    assert task.get_name() == 'foo : baz'


# Generated at 2022-06-13 09:09:20.381550
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    from six import PY2
    import sys
    import mock

    if PY2:
        builtin_open = '__builtin__.open'
    else:
        builtin_open = 'builtins.open'

    display_patch = mock.patch.object(Display, 'debug')
    display_patch.start()

    # BUILD TEST DATA
    #
    # | note: we're not currently testing Templar, so we're feeding in a very simplified version of a
    # |       real loader, which will work if the files being referenced do exist, but is no more than
    # |       that.
    # v

    loader_mock = mock.MagicMock()
    loader_mock.path_dwim = lambda x: x


# Generated at 2022-06-13 09:10:18.533744
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():
    ir = IncludeRole()
    ir.name = "example"
    ir._role_name = "example_role"
    assert ir.get_name() == "example : example_role"
    ir.name = None
    assert ir.get_name() == "include_role : example_role"

# Generated at 2022-06-13 09:10:30.470229
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():
    display.verbosity = 3
    # Ensure name of IncludeRole is set
    task = Block()
    task = IncludeRole(task)
    task.name = 'test_IncludeRole_get_name'
    task.role = 'test_IncludeRole_get_name'
    assert task.get_name() == 'test_IncludeRole_get_name : ' \
            'test_IncludeRole_get_name'
    # Ensure name of IncludeRole is set to action
    task = Block()
    task = IncludeRole(task)
    task.role = 'test_IncludeRole_get_name'
    assert task.get_name() == 'test_IncludeRole_get_name'

    # Ensure name of IncludeRole is set to role
    task = Block()
    task = IncludeRole(task)
    task.name

# Generated at 2022-06-13 09:10:31.548904
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    pass

# Generated at 2022-06-13 09:10:39.931263
# Unit test for method load of class IncludeRole

# Generated at 2022-06-13 09:10:50.777008
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.vars.manager import VariableManager
    from ansible.vars.unsafe_proxy import UnsafeProxy
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.vars import combine_vars

    # Setup
    block = Block()
    role = RoleDefinition.load(dict(
        name='foo',
        tasks=[{'include_role': {'name': 'bar'}}, {'include_role': {'name': 'baz'}}],
        defaults=dict(defaults='defaults'),
        handlers=dict(handlers='handlers'),
        vars=dict(vars='vars'),
        metadata=dict(metadata='metadata')
    ))
    variable_manager = VariableManager()
   

# Generated at 2022-06-13 09:10:59.150088
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():
    task_data = dict(
        name='name_1',
        include='include_1'
    )
    task_include = TaskInclude()
    task_include.load(task_data)
    include_role = IncludeRole(task_include=task_include)
    include_role._role_name = 'test_role'
    include_role._role_path = 'role_path'
    include_role.action = 'include'
    assert_true('include_1' in include_role.get_name())



# Generated at 2022-06-13 09:11:13.354368
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    fake_play = type('FakePlay', (object, ), {'_entries': {}, '_basedir': '.'})()
    fake_play._entries['tasks'] = [Block()]

    fake_role = type('FakeRole', (object, ), {'_metadata': {}, '_parents': ['parent1', 'parent2'], '_role_path': '/Users/user/ansible/roles/fake-role'})()
    fake_role._rolespec_validate = True
    fake_role.vars = {'var1': 'val1'}
    fake_role.get_handler_blocks = lambda: ['fake handler block']
    fake_role.get_role_params = lambda: {'fake param': 'fake value'}


# Generated at 2022-06-13 09:11:21.320128
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    from ansible.playbook.role.include import RoleInclude
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    variable_manager = VariableManager()
    variable_manager.set_loader(loader=loader)
    templar = Templar(loader=loader, variables=variable_manager.get_vars(play=None, task=None))

    include_role_1 = IncludeRole(None, None, None)


# Generated at 2022-06-13 09:11:24.709370
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    data = {'apply': {'ignore_errors': True}, 'public': False, 'rolespec_validate': False, 'name': 'include_role_test'}

    ir = IncludeRole.load(data, block=None, role=None, task_include=None, variable_manager=None, loader=None)

# Generated at 2022-06-13 09:11:34.933266
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    data = {
        'name': 'test_role',
    }

    ir = IncludeRole.load(data)
    assert ir._role_name == 'test_role'
    assert ir._from_files == {'tasks': 'tasks.yml', 'vars': 'vars.yml', 'defaults': 'defaults.yml', 'handlers': 'handlers.yml'}

    # Validate options
    my_arg_names = frozenset(ir.args.keys())
    bad_opts = my_arg_names.difference(IncludeRole.VALID_ARGS)
    assert not bad_opts, bad_opts

    # role is required, name can be used as alias
    data = {}
    with pytest.raises(AnsibleParserError):
        ir = IncludeRole