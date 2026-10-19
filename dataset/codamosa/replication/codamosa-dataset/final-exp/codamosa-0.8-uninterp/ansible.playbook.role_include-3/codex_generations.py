

# Generated at 2022-06-13 09:02:56.916000
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    """Unit test for method load of class IncludeRole."""
    mytest = dict(
        action=dict(module='include_role', args=dict(name='test')),
    )
    myrole = dict(
        name='test',
        defaults=dict(),
        vars=dict(),
        tasks=dict()
    )
    myblock = Block(parent_block=None, task_include=mytest)
    myinclude = IncludeRole(block=myblock, role=myrole)
    assert myinclude.load(mytest, myblock, myrole) is not None

test_IncludeRole_load()

# Generated at 2022-06-13 09:03:06.594562
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    from ansible.playbook.included_file import IncludedFile

    # load some roles
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    import ansible.constants as C
    C.HOST_KEY_CHECKING = False
    C.RETRY_FILES_ENABLED = False
    C.DEFAULT_ROLES_PATH = ['https://github.com/roles-ansible']
    C.DEFAULT_ROLES_PATH = 'https://github.com/roles-ansible'
    
    from ansible.parsing.dataloader import DataLoader
    loader = DataLoader()
    inv_manager = InventoryManager(loader=loader, sources=['/home/brendon/Projects/Ansible/myhosts'])

   

# Generated at 2022-06-13 09:03:17.828373
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    import os
    import sys
    import unittest
    import ansible.plugins
    from ansible.module_utils.six import PY3
    from ansible.plugins import module_loader
    from ansible.template import Templar
    from ansible.vars import VariableManager
    if PY3:
        import unittest.mock as mock
    else:
        import mock

    class IncRoleTestCase(unittest.TestCase):

        def setUp(self):
            self.play = mock.MagicMock()
            self.play.roles = []
            self.play.block_list = []
            self.var_manager = VariableManager()
            self.loader = mock.MagicMock()
            self.loader.get_basedir.return_value = '.'


# Generated at 2022-06-13 09:03:24.949073
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    import ansible.plugins.loader as plugins

# Generated at 2022-06-13 09:03:28.898960
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():
    include = IncludeRole()
    include.name = 'Name'
    include._role_name = 'Role name'
    assert include.get_name() == 'Name : Role name'
    include.name = None
    assert include.get_name() == 'include_role : Role name'

# Generated at 2022-06-13 09:03:37.604957
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():

    # TODO: Also test the error-cases.

    # Create a role instance
    ir = IncludeRole()
    # Setup a fake module
    module = 'include_role'
    # Setup a fake module_args (data)
    data = {
        "name": "web",
        "apply": {
            "tags": ["foo"],
            "become": True
        },
        "allow_duplicates": True,
        "tasks_from": "foo.yml"
    }
    # Call load and return it
    return ir.load(data, module=module)


# Generated at 2022-06-13 09:03:48.789133
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    # Test without data and without variable_manager
    try:
        IncludeRole.load(None)
    except AnsibleParserError as e:
        assert str(e) == "'name' is a required field for include_role."
    except:
        assert False, 'Expected AnsibleParserError'

    # Test with data and variable_manager
    data = {'role': 'test', 'tasks_from': 'role_tasks/test.yml', 'vars_from': 'role_vars/test.yml', 'defaults_from': 'defaults/test.yml', 'handlers_from': 'handlers/test.yml', 'tags': ['test'], 'allow_duplicates': False, 'apply': {}}
    variable_manager = None
    loader = None
    block = None
    role = None


# Generated at 2022-06-13 09:03:57.635997
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    t_incl = IncludeRole()
    data = {}
    data['args'] = {'name': 'myrole'}
    t_incl.load(data=data, variable_manager=None, loader=None)
    assert t_incl._role_name == 'myrole'
    assert len(t_incl._from_files) == 0
    vars = t_incl.get_include_params()
    assert len(vars) == 0
    assert t_incl._parent_role is None

    data = {}
    data['args'] = {'name': 'myrole', 'allow_duplicates': True, 'apply': {}}
    t_incl.load(data=data, variable_manager=None, loader=None)
    assert t_incl._role_name == 'myrole'
   

# Generated at 2022-06-13 09:04:10.759637
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    import pytest
    from ansible.playbook.play import Play
    from ansible.playbook.role.include import RoleInclude
    from ansible.playbook.role import Role
    test_args = ['test_role']
    test_kwargs = dict(tasks_from='test_tasks',
                       vars_from='test_vars',
                       defaults_from='test_defaults',
                       handlers_from='test_handlers',
                       apply=dict(bob='jim'),
                       public=True,
                       allow_duplicates=True,
                       rolespec_validate=False)

# Generated at 2022-06-13 09:04:14.995947
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.conditional import Conditional
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.play import Play
    from ansible.playbook.role import Role

    loader = DataLoader()
    variable_manager = VariableManager()

# Generated at 2022-06-13 09:04:35.937910
# Unit test for method get_include_params of class IncludeRole
def test_IncludeRole_get_include_params():

    vars = {u'ansible_parent_role_names': [u'fake_role_1']}

    my_include_role = IncludeRole()
    my_include_role._parent_role = Role()
    my_include_role._parent_role.name = u'fake_role_1'
    my_include_role._parent_role._role_path = u'/fake/fake_role_1'

    my_include_role.vars = vars

    v = my_include_role.get_include_params()

    expected = {u'ansible_parent_role_names': [u'fake_role_1', u'fake_role_1'], u'ansible_parent_role_paths': [u'/fake/fake_role_1', u'/fake/fake_role_1']}


# Generated at 2022-06-13 09:04:45.629445
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():

    class FakeRole(object):
        def __init__(self, role_name=None, role_path=None):
            self._role_path = role_path
            self._role_name = role_name
            self._metadata = FakeRoleMetadata()

        def get_name(self):
            return self._role_name

        def get_handler_blocks(self, play):
            pass

        def compile(self, play):
            pass

    class FakeRoleMetadata(object):
        def __init__(self):
            self.allow_duplicates = True

    class FakePlay(object):
        def __init__(self):
            self.roles = []

    class FakeLoader(object):
        def __init__(self):
            self.paths = []


# Generated at 2022-06-13 09:04:59.704700
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():

    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.block import Block

    data = dict(
        name='foo',
        tasks_from='../bar.yml',
        vars_from='../baz.yml',
        defaults_from='../blam.yml',
        apply=dict(
            ignore_errors=True,
            tags='no-such-tag',
        ),
        public=True,
        allow_duplicates=False,
    )
    data_obj = Block.load(data, task_include=dict(action='frobnicate'))
    data_obj.basename = 'a-role'
    loader = DataLoader()


# Generated at 2022-06-13 09:05:00.777779
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    # This is a test
    return True

# Generated at 2022-06-13 09:05:14.154073
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.module_utils.common.process import get_bin_path

    # Ansible Config
    config = {
        'DEFAULT_ROLES_PATH': '../../../tests/units/module_utils/roles',
    }

    # Create a temporary directory
    import tempfile
    temp_dir = tempfile.TemporaryDirectory()

    # Ansible Inventory

# Generated at 2022-06-13 09:05:22.259934
# Unit test for method get_include_params of class IncludeRole
def test_IncludeRole_get_include_params():
    assert IncludeRole().get_include_params() == {
                            'ansible_include_role_params': {},
                            'ansible_playbook_python': '{{ ansible_playbook_python|default(ansible_python_interpreter) }}',
                            'ansible_python_interpreter': '{{ ansible_python_interpreter|default("python") }}'}

    assert IncludeRole(name='test').get_include_params() == {
                            'ansible_include_role_params': {'name': 'test'},
                            'ansible_playbook_python': '{{ ansible_playbook_python|default(ansible_python_interpreter) }}',
                            'ansible_python_interpreter': '{{ ansible_python_interpreter|default("python") }}'}

# Generated at 2022-06-13 09:05:28.194602
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    role = IncludeRole()
    role.args = { 'name' : 'serial', 'apply' : {}}
    role.statically_loaded = True
    role.allow_duplicates = True
    role.public = True
    role.rolespec_validate = True
    role.vars = {}
    role.collections = []

    try:
        block_list = role.get_block_list()
    except Exception as e:
        print(e)
        assert False

    assert True


# Generated at 2022-06-13 09:05:31.957279
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():
    block = Block(parent_block=None)
    role = Role(name='foo')
    task_include = TaskInclude(name='bar')

    ir = IncludeRole(block=block, role=role, task_include=task_include)

    assert ir.get_name() == 'bar'

    ir.name = 'baz'
    assert ir.get_name() == 'baz'

# Generated at 2022-06-13 09:05:44.441195
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.utils.vars import combine_vars
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    import sys
    import json
    import os

    class PlayStub:
        def __init__(self, inventory):
            self._play = Play()
            self.inventory = inventory

    # - ansible-playbook -i inventory/molecule_local.yml --limit localhost --tags "test_IncludeRole_get_block_list" playbooks/main.yml
   

# Generated at 2022-06-13 09:05:48.066469
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    ir = IncludeRole(block=None, role=None, task_include=None)
    print(ir.get_block_list(play=None, variable_manager=None, loader=None))


# Generated at 2022-06-13 09:06:08.856303
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    import pytest
    from ansible.playbook.role.include import RoleInclude

    # role=None, task_include=None
    assert isinstance(IncludeRole.load({'name': 'test'}), IncludeRole)
    assert isinstance(IncludeRole.load({'include': 'test'}), TaskInclude)
    assert isinstance(IncludeRole.load({'include_role': 'test'}), IncludeRole)

    # role=Role()
    assert isinstance(IncludeRole.load({'name': 'test'}, role=RoleInclude({})), IncludeRole)
    assert isinstance(IncludeRole.load({'include': 'test'}, role=RoleInclude({})), TaskInclude)

# Generated at 2022-06-13 09:06:17.194711
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    from ansible.playbook.play import Play
    from ansible.vars.manager import VariableManager
    import os

    cur_play_dir = os.path.dirname(os.path.realpath(__file__))
    test_play_dir = os.path.abspath(os.path.join(cur_play_dir, '..', '..', 'test', 'units', 'playbooks'))

    loader = RoleInclude.create_loader(None, play_basedir=test_play_dir)
    variable_manager = VariableManager()

    play = Play.load(name='test_play', variable_manager=variable_manager, loader=loader)

# Generated at 2022-06-13 09:06:21.422611
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    from ansible.playbook.play import Play
    from ansible.playbook.role.definition import RoleDefinition

    p = Play()
    p._loader = None
    p._variable_manager = None

    # non-existent role
    d = dict(
        name='fake.role',
        local_action='include_role',
    )
    r = RoleDefinition(play=p)
    result = IncludeRole.load(d, role=r)
    try:
        result.get_block_list(play=p)
        assert False, 'expected exception'
    except Exception as e:
        assert 'Specified role fake.role' in str(e), str(e)

    d = dict(
        name='fake.role',
        local_action='include_role',
    )

# Generated at 2022-06-13 09:06:29.901527
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():
    include_role = IncludeRole()
    include_role.action = 'include_role'
    include_role.name = 'myRole'
    assert include_role.get_name() == "include_role : myRole"
    include_role.name = None
    include_role.role = 'myRole'
    assert include_role.get_name() == "include_role : myRole"
    include_role.name = 'overridden_'
    assert include_role.get_name() == "include_role : overridden_"

# Generated at 2022-06-13 09:06:41.625020
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():

    display.verbosity = 3
    # FIXME: there's a warning logged here
    with parser.load_from_file(os.path.join(DATA_PATH, 'playbooks', 'include_role.yml')) as playbook:
        display.verbosity = 3
        play = playbook.get_plays()[0]
        variable_manager = VariableManager()
        variable_manager.extra_vars = load_fixture('include_role_vars.yml')
        loader = DataLoader()

        tasks = play.compile()
        host = Host(name="localhost")
        task_vars = variable_manager.get_vars(loader=loader, play=play, host=host)
        play_context = PlayContext()
        play_context._task_vars = task_vars

        # test calling the method with empty

# Generated at 2022-06-13 09:06:42.689427
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    assert False

# Generated at 2022-06-13 09:06:53.219687
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    assert IncludeRole.load({"role":"myrole"})
    assert IncludeRole.load({"name":"myrole"})
    assert IncludeRole.load({"role":"myrole", "tasks_from":"main.yml"})
    assert IncludeRole.load({"name":"myrole", "tasks_from":"main.yml"})
    assert IncludeRole.load({"role":"myrole", "no_log":True})
    assert IncludeRole.load({"name":"myrole", "no_log":True})
    assert not IncludeRole.load({"role":None})
    assert not IncludeRole.load({"role":[]})
    assert not IncludeRole.load({"role":{}})
    assert not IncludeRole.load({"role":1})
    assert not IncludeRole.load({"name":None})
    assert not Include

# Generated at 2022-06-13 09:06:54.813842
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():

    # TODO
    pass

# Generated at 2022-06-13 09:06:59.858192
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    display.verbosity = 0
    # We create a Block with its parent set to None because the parent
    # is not used by get_block_list
    block = Block(parent=None)
    ir = IncludeRole(block=block)

    # Check that an error is raised when a task contains none of the
    # options name or role
    data = {'foo': 'bar'}
    ir = ir.load(data=data, variable_manager=None, loader=None)
    with pytest.raises(AnsibleParserError) as excinfo:
        (blocks, handlers) = ir.get_block_list()
    assert 'name' in str(excinfo.value)
    assert 'role' in str(excinfo.value)

# Generated at 2022-06-13 09:07:05.759800
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    '''
    Tests IncludeRole load method
    '''
    sample_include_role = {
        'include_role': {
            'name': 'sample_role',
            'vars': {'a': 'b'}
        }
    }
    try:
        IncludeRole.load(sample_include_role)
    except AnsibleParserError:
        print('IncludeRole load method test failed')

# Generated at 2022-06-13 09:07:36.768308
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():
    task_include, role, data = None, None, {'name': 'role_name'}
    l_include_role = IncludeRole(task_include=task_include, role=role)
    l_include_role.args = data
    l_include_role.action = 'include_role'
    result = l_include_role.get_name()
    assert result == 'include_role : role_name'


# Generated at 2022-06-13 09:07:47.277618
# Unit test for method get_include_params of class IncludeRole
def test_IncludeRole_get_include_params():

    from ansible.playbook import Play
    from ansible.playbook.play import PlayContext
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.role_include import RoleInclude
    from ansible.playbook.role import Role

    play = Play()
    play_context = PlayContext(play=play)
    play._defaults = {
        'roles_path': C.DEFAULT_ROLES_PATH
    }
    loader = play._loader

    # Use default default_vars
    block = Block(parent_block=play)
    block.vars.update({'role_name': 'test_role', 'role_path': 'test_role.yml', "role_tasks_path": 'test_role/tasks/main.yml'})

    # Create

# Generated at 2022-06-13 09:07:56.955008
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    from ansible.playbook.play_context import PlayContext

    role = Role.load('test_include_role')
    ir = IncludeRole.load('test_include_role')
    ir.vars = dict(a=1, b='2')
    blocks, handlers = ir.get_block_list(play=role._play, loader=role._loader, variable_manager=role._variable_manager)

    assert len(blocks) == 1
    assert isinstance(blocks[0], Block)
    assert blocks[0].block  == [
        dict(
            register=dict(result='var_a'),
            set_fact=dict(
                var_a=dict(a=1, b='2'),
                var_b=dict(c=2, d='4')
            )
        )
    ]


# Generated at 2022-06-13 09:08:09.292624
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    from ansible.plugins.loader import action_loader

    # Setup loader
    action_plugin_loader = action_loader.ActionModuleLoader(None, '/dev/null')
    action_plugin_loader._module_cache.clear()
    action_plugin_loader._directory_cache.clear()

    # Setup play
    play = {
        'name': 'test_play',
        'hosts': 'localhost',
        'gather_facts': 'no',
        'tasks': [
            {
                'name': 'test_task',
                'action': 'include_role',
                'arguments': {
                    'name': 'test_role'
                }
            }
        ]
    }

    # Setup role

# Generated at 2022-06-13 09:08:19.319986
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    from ansible.playbook import Play
    from ansible.module_utils._text import to_bytes
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    class FakeLoader():
        def get_basedir(self):
            return '.'

    loader = FakeLoader()
    variable_manager = VariableManager(loader=loader)
    play_source = dict(
        name = "Ansible Play",
        hosts = "localhost",
        gather_facts = 'no',
        tasks = [{
            'include_role': {
                'name': 'foobar',
            }
        }]
    )
    play = Play.load(play_source, variable_manager=variable_manager, loader=loader)


# Generated at 2022-06-13 09:08:26.610250
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager

    loader = None
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, sources="127.0.0.1", variable_manager=variable_manager)
    variable_manager.set_inventory(inventory)

    play_context = PlayContext()

    # case 1: simple include_role
    block = Block()
    ir = IncludeRole()
    ir.load_data({'role': 'somesuite.someproject'})
    ir.post_validate(play_context)
    blocks, handlers = ir.get_block_list()

    # case 2: include_role with apply

# Generated at 2022-06-13 09:08:39.897285
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.utils.vars import load_extra_vars

    loader = DataLoader()
    variable_manager = VariableManager()
    variable_manager._extra_vars = load_extra_vars('v', 'tasks/files/playbook.yml')
    variable_manager.set_inventory(InventoryManager(loader=loader, sources=['tasks/files/playbook.yml']))

    play_context = PlayContext()


# Generated at 2022-06-13 09:08:50.907398
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    role = Role()
    role.ROLE_CACHE = {}
    ir = IncludeRole(role=role)
    ir.vars = {}
    ir._role_name = "foo"
    ir._from_files = {}
    ir._parent_role = role
    ir._parent_role._metadata = type('', (), {})()
    ir._parent_role._metadata.role_name = "parent"
    play = type('', (), {})()
    play.roles = []
    play.handlers = []
    variable_manager = type('', (), {})()
    variable_manager.get_vars = lambda: {}
    loader = None
    blocks, handlers = ir.get_block_list(play=play, variable_manager=variable_manager, loader=loader)
    assert len(blocks) == 2
   

# Generated at 2022-06-13 09:09:03.040154
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    import ansible.playbook
    import ansible.playbook.role
    import ansible.template
    import ansible.vars
    import ansible.errors
    import ansible.module_utils.six
    import ansible.plugins.loader
    import ansible.playbook.play
    import ansible.playbook.block

    ansible.playbook.ZERO_COMPLEXITY_REACHED = False
    ansible.playbook.COMPLEXITY_LIMIT = None
    ansible.playbook.INCLUDE_ROLE_DEPTH = 0


# Generated at 2022-06-13 09:09:14.663290
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():

    """
    Test to ensure IncludeRole._get_block_list() returns expected results.
    When there is a _parent, then return parent's blocks.
    When there are tasks in _tasks, then returns their blocks.
    """

    from ansible.playbook import Play
    from ansible.playbook.play import PlayContext
    from ansible.playbook.included_file import IncludedFile
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.block import Block


# Generated at 2022-06-13 09:10:23.384288
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    from ansible.playbook.play import Play
    from ansible.playbook.block import Block
    from ansible.playbook.task_include import TaskInclude
    from ansible.plugins import module_loader
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.template import Templar
    from ansible.utils.vars import combine_vars

    data = {'name': 'test', 'task': Block(module='include_role', tasks=[IncludeRole(Block(msg='Test'))])}
    data['tasks'] = [data['task']]

    loader = DataLoader()
    play = Play().load(data=data, variable_manager=VariableManager(), loader=loader)

   

# Generated at 2022-06-13 09:10:24.121319
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    pass

# Generated at 2022-06-13 09:10:35.502275
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    '''
    test for method get_block_list of class IncludeRole
    '''

    # Test setup
    from ansible.playbook.play_context import PlayContext
    from ansible.utils.vars import combine_vars
    from ansible.utils.path import unfrackpath

    class TestOptions(object):
        verbosity = 0
        extra_vars = []
        extra_vars_files = []
        vault_password = None
        vault_password_files = []
        tags = ['all']
        skip_tags = []
        force_handlers = False
        start_at_task = None
        step = None
        subset = None

    class TestPlay(object):
        tasks = []
        role_names = []
        role_paths = []
        handlers = []


# Generated at 2022-06-13 09:10:42.565879
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    from ansible.playbook import Playbook
    from ansible.inventory import Inventory
    from ansible.vars import VariableManager

    my_play = Playbook()
    my_inv = Inventory()
    my_vm = VariableManager()

    # test first use case
    data = {'name': 'test_name'}
    ir = IncludeRole.load(data, 'block', 'role')
    assert isinstance(ir, IncludeRole)
    assert ir._role_name == 'test_name'

    # test second use case
    data = {'role': 'test_role'}
    ir = IncludeRole.load(data, 'block', 'role')
    assert isinstance(ir, IncludeRole)
    assert ir._role_name == 'test_role'

    # test third use case

# Generated at 2022-06-13 09:10:52.736022
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    # set up role with some variables, handlers, and tasks
    import os, sys
    import yaml, ansible.utils.unsafe_proxy
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject

    class TestBaseYAMLObject(AnsibleBaseYAMLObject):
        # https://github.com/ansible/ansible/issues/23637
        # this is a copy of the original base object class, including the offending __setattr__
        def __init__(self, data):
            self._data = data

        def __getattr__(self, name):
            #print >>sys.stderr,"   calling __getattr__ with %s" % name
            return getattr(self._data, name)


# Generated at 2022-06-13 09:11:03.231331
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    # this test is to check if the get_block_list method of the IncludeRole class returns
    # a sorted list of list of blocks

    # role with simple tasks
    block = Block()
    role = Role()
    task_include = TaskInclude()
    task_include.tasks = [
        {'name': 'task 1'},
        {'name': 'task 2'}
    ]

    # calling the get_block_list method by passing a role
    include_role1 = IncludeRole(block, role, task_include=task_include)
    result1 = include_role1.get_block_list()

    # converting the result of the get_block_list method to a sorted list of list of blocks
    block_list1 = []

# Generated at 2022-06-13 09:11:13.849178
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    # Unit test:
    #   given:
    #     - include_role:
    #         name: test_role
    #   when:
    #     - IncludeRole.load()
    #   then:
    #     - _role_name is set to the value of name (test_role)
    #     - return object is an instance of IncludeRole class
    include_role_data = {'name': 'test_role'}
    include_role = IncludeRole.load(include_role_data)
    assert include_role._role_name == 'test_role'
    assert isinstance(include_role, IncludeRole)



# Generated at 2022-06-13 09:11:15.680022
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():
    ir = IncludeRole()
    ir._role_name = 'myrole'
    assert ir.get_name() == "include_role : myrole"

# Generated at 2022-06-13 09:11:24.652377
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    import ansible.utils.template as template
    from ansible.module_utils._text import to_bytes
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.errors import AnsibleParserError

    # Initialise test data
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager()
    play_context = Play

# Generated at 2022-06-13 09:11:25.390809
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    pass