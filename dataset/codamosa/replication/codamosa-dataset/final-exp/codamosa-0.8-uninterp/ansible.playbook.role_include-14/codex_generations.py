

# Generated at 2022-06-13 09:02:51.017351
# Unit test for method get_include_params of class IncludeRole
def test_IncludeRole_get_include_params():
    task = IncludeRole(role=object())
    params = {
        'foo': 'bar',
    }
    task._parent_role = object()
    task._parent_role.get_role_params = lambda: params
    task._parent_role.get_name = lambda: 'xyzzy'
    task._parent_role._role_path = '/tmp'

    include_params = task.get_include_params()

    assert include_params == {
        'ansible_parent_role_names': ['xyzzy'],
        'ansible_parent_role_paths': ['/tmp'],
        'foo': 'bar',
    }



# Generated at 2022-06-13 09:03:01.793206
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    block = Block()
    role = Role()
    irc = IncludeRole(block, role)
    irc._role_name = 'test_role'
    irc._role_path = 'test_role_path'
    assert irc.get_name() == ' : test_role'
    assert irc._from_files == {}
    assert irc._parent_role == role

    block = Block()
    role = Role()
    irc = IncludeRole(block, role)
    irc._role_name = 'test_role'
    irc._role_path = 'test_role_path'
    assert irc.get_name() == ' : test_role'
    assert irc._from_files == {}
    assert irc._parent_role == role

    # testing attribute_public
    assert irc.get

# Generated at 2022-06-13 09:03:09.163532
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():
    display.verbosity = 3

    # Setup AnsibleParserError
    try:
        raise AnsibleParserError()
    except AnsibleParserError as e:
        pass

    fixture_include = {"__ansible_arguments__": "role",
                       "__ansible_module__": "include_role",
                       "__ansible_no_log__": False,
                       "__ansible_self__": {"action": "role"}}
    include_role = IncludeRole(role="dummy_role")
    include_role.load_data(fixture_include)

    assert include_role.get_name() == "role : dummy_role"

# Generated at 2022-06-13 09:03:20.075676
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    from ansible.utils.unit.compat import mock
    from ansible.utils.unit.mock import patch
    import ansible.playbook.role

    mock_parent_role = mock.Mock()
    mock_data = {'name': 'test'}
    mock_block = mock.Mock()
    mock_variable_manager = mock.Mock()
    mock_loader = mock.Mock()
    playbook_dir = '/playbook/dir'
    mock_variable_manager.get_vars.return_value = {'playbook_dir': playbook_dir}

    RoleInclude_obj = mock.Mock()
    mock_patch_target = 'ansible.playbook.role.RoleInclude'
    with patch(mock_patch_target, RoleInclude_obj):
        test_obj = IncludeRole

# Generated at 2022-06-13 09:03:31.209810
# Unit test for method get_include_params of class IncludeRole
def test_IncludeRole_get_include_params():
    # pylint: disable=unused-argument
    import os
    import tempfile
    from ansible.playbook.play_context import PlayContext
    
    vars = dict(
      foo = dict(
        bar = dict(
          baz = "hello",
        ),
      ),
    )

    def _create_tmp_dir(tmp_prefix=tempfile.template):
        tmp_dir = tempfile.mkdtemp(prefix=tmp_prefix)
        open(os.path.join(tmp_dir,"main.yml"),"w").close()
        sub_role_dir = os.path.join(tmp_dir,"subrole")
        os.mkdir(sub_role_dir)
        open(os.path.join(sub_role_dir,"main.yml"),"w").close()
        return

# Generated at 2022-06-13 09:03:42.539935
# Unit test for method get_include_params of class IncludeRole
def test_IncludeRole_get_include_params():
    import os
    import sys
    import unittest
    import unittest.mock as mock

    sys.modules['ansible'] = mock.Mock()
    sys.modules['ansible.utils'] = mock.Mock()
    sys.modules['ansible.utils.display'] = mock.Mock()

    with mock.patch.object(sys.modules['ansible.utils.display'], 'Display') as MockDisplay:
        display_instance = MockDisplay.return_value
        display_instance.warning.return_value = None

        from ansible.playbook.role import Role

        class TestRole(Role):
            _role_name = 'test-role'
            _role_path = '/test/role/path'
            _metadata_path = '/test/role/path/meta/main.yml'


# Generated at 2022-06-13 09:03:52.776772
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():

    import sys
    if sys.version < '3':
        from io import BytesIO as StringIO
    else:
        from io import StringIO

    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.block import Block
    from ansible.playbook.play import Play
    from ansible.playbook.role import Role
    from ansible.playbook.task import Task
    from ansible.template import Templar

    the_loader = DataLoader()
    the_loader.set_basedir('../../tests/')

    variable_manager = VariableManager()
    variable_manager.set_inventory(the_loader.load_inventory('../../tests/inventory'))


# Generated at 2022-06-13 09:04:06.767725
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():

    from ansible.playbook import Play
    import os

    BASE_DIR = os.path.dirname(__file__)
    FIXTURES_DIR = os.path.join(BASE_DIR, "fixtures")

    p = Play.load(path=FIXTURES_DIR + '/test_IncludeRole.yaml', variable_manager=None, loader=None)

    assert len(p.tasks) == 1

    ir = IncludeRole.load(p.tasks[0], block=None, role=None, task_include=None, variable_manager=None, loader=None)
    ir._parent_role = p.get_roles()[0]

    assert ir.get_block_list()

    assert len(ir._parent_role._dep_chain) == 1

# Generated at 2022-06-13 09:04:07.707100
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    raise NotImplementedError

# Generated at 2022-06-13 09:04:16.351403
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    # Role object only instantiated by `.load()`
    assert isinstance(IncludeRole.load(data={'name': 'myrole', 'tasks_from': 'main.yml'}), IncludeRole)

    # Assign valid args to properties
    # name property is the same as role
    for arg_name in IncludeRole.BASE:
        include_role = IncludeRole.load(data={arg_name: 'test'})
        assert getattr(include_role, arg_name) == 'test'

    # (tasks_from, vars_from, defaults_from, handlers_from)
    for arg_name in IncludeRole.FROM_ARGS:
        include_role = IncludeRole.load(data={arg_name: 'test'})

# Generated at 2022-06-13 09:04:35.206809
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play

    loader = DataLoader()
    variable_manager = VariableManager()
    play = Play.load({}, variable_manager=variable_manager, loader=loader)

    data = {
        'include_role': {
            'name': 'testrole',
        }
    }
    ir = IncludeRole.load(data, play=play, variable_manager=variable_manager, loader=loader)

    assert ir._role_name == 'testrole'
    assert ir.args == {'name': 'testrole'}
    assert ir._from_files == {}
    assert ir._parent_role == None
    assert ir._role_path == None

# Generated at 2022-06-13 09:04:38.990547
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():
    r2 = Block()
    r2._role_name = 'role2'
    ti = IncludeRole(r2)
    ti.name = 'include_role'
    ti._role_name = 'role1'
    assert ti.get_name() == 'include_role : role1'



# Generated at 2022-06-13 09:04:39.606780
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():
    return True

# Generated at 2022-06-13 09:04:44.838829
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():
    rname = "tstrole"
    r = Role.load(dict(name=rname))
    rb = r.get_block_list(play=None)[0]
    i = IncludeRole(block=rb, data=dict(name=rname), role=r)
    assert i.get_name() == "include_role : %s" % rname

# Generated at 2022-06-13 09:04:56.004163
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    # case 1
    print('IncludeRole_load case 1')
    class Mock_Block():
        def __init__(self, data):
            self.data = data
    class Mock_Role():
        def __init__(self, data):
            self.data = data
    class Mock_Task_Include():
        def __init__(self, data):
            self.data = data
    data = {
        "include_role": {
            "name": "web",
            "public": True
        }
    }
    block = Mock_Block(data)
    role = Mock_Role(data)
    task_include = Mock_Task_Include(data)
    m = IncludeRole.load(data, block=block, role=role, task_include=task_include)

# Generated at 2022-06-13 09:05:03.387890
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():
    data = {
        'block': None,
        'load_file_name': 'roles/role_name/tasks/main.yml',
        'args': {u'role': u'role_name'},
        'name': u'role_name',
        'action': u'include_role',
        'private': True,
        'playbook_filename': u'playbook.yml',
        'role': None
    }

    ir = IncludeRole().load_data(data)

    name = ir.get_name()
    assert name == 'role_name'

# Generated at 2022-06-13 09:05:16.700404
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():

    # Tests for _action_plugin loading
    #
    # Loader mock
    class LoaderMock():
        def get_basedir(self, *args):
            return 'some/path'

    # Data mock
    class DataMock():
        def __init__(self, *args):
            self.args = args

    # VariableManager mock
    class VariableManagerMock():
        pass

    # Block mock
    class BlockMock():
        pass

    # Role mock
    class RoleMock():
        def __init__(self, *args):
            self.args = args

    # Load IncludeRole
    lm = LoaderMock()
    vm = VariableManagerMock()
    dm = DataMock('include_role', 'name=myrole', 'become=yes', 'connection=local')
    b

# Generated at 2022-06-13 09:05:24.288933
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():

    from ansible.playbook.playbook import Playbook
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.playbook_executor import PlaybookExecutor

    class Options(object):
        become = False
        become_user = ''
        become_method = ''
        become_ask_pass = False
        check = False
        diff = False
        connection = 'local'
        module_path = None
        only_tags = []
        skip_tags = []
        start_at_task = None
        verbosity = 4
        private_key_file = None

    pb = Playbook

# Generated at 2022-06-13 09:05:32.761956
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():

    from ansible.module_utils._text import to_bytes
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.role import ROLE_CACHE
    from ansible.playbook.play import Play
    from ansible.plugins.loader import get_all_plugin_loaders, get_plugin_loader
    from ansible.executor.task_queue_manager import TaskQueueManager

    # name is None
    data = dict(name=None, role='foo')
    IncludeRole.load(data)

    # name and role
    data = dict(name='name', role=None)
    IncludeRole.load(data)

    # from_files

# Generated at 2022-06-13 09:05:44.972431
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    import os
    import copy
    import json
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText

    # python2 and python3 compatible way to get the path of this script
    test_case_path = os.path.dirname(os.path.abspath(__file__))

    localhost = None
    inventory = None
    loader = None
    variable_manager = None
    tqm = None

    # the path of the role, not the task
    role_path = os.path.join(test_case_path, 'roles/basicrole')

    # the task (playbook) that includes the role
    task_path = os.path.join(test_case_path, 'playbooks/include_role_task.yml')

    # the task (playbook) that the role includes
   

# Generated at 2022-06-13 09:06:08.898333
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    def include_role_load(data_dict):
        return IncludeRole.load(data_dict, block=None, role=None, task_include=None, variable_manager=None, loader=None)

    #
    # - role needs a name
    # - from_* values need to be strings
    # - any invalid options must be reported
    #
    data_dict = {'name': 'test', 'some_invalid_arg': 'some_invalid_value'}
    assert_raises(AnsibleParserError, include_role_load, data_dict)

    # data_dict = {'name': 'test', 'tasks_from': 'some_tasks_file'}
    # assert_raises(AnsibleParserError, include_role_load, data_dict)


# Generated at 2022-06-13 09:06:17.217774
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    # Scenario 1: name is not provided and role is not provided
    data = dict()
    try:
        # Expect AnsibleParserError
        IncludeRole.load(data)
    except AnsibleParserError as e:
        assert "Invalid options for include_role:" in str(e)

    # Scenario 2: invalid_keys is provided
    data = dict(
        name='new_role',
        invalid_keys=dict(anykey='anyvalue')
    )
    try:
        # Expect AnsibleParserError
        IncludeRole.load(data)
    except AnsibleParserError as e:
        assert "Invalid options for include_role: invalid_keys" in str(e)

    # Scenario 3: invalid_value for apply is provided

# Generated at 2022-06-13 09:06:26.030479
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    class FakeOptions(object):
        def __init__(self):
            self.roles = []

    class FakeRole(object):
        def __init__(self, name):
            self.name = name

    module_name = 'include_role'
    module_args = dict(name='role_name')
    block = Block.load(dict(
        _raw_params='',
        _role=FakeRole('foo'),
        _play=FakeOptions()
    ), loader=None, variable_manager=None, use_handlers=False)
    ir = IncludeRole.load(dict(
        action=module_name,
        args=module_args,
        block=block
    ), block=block, variable_manager=None, loader=None)
    assert ir.action == module_name

# Generated at 2022-06-13 09:06:28.471793
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
  ir = IncludeRole

  assert isinstance(ir, object)
  t = IncludeRole.load

# Generated at 2022-06-13 09:06:41.002073
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    import ansible.playbook.block
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.play import Play
    from ansible.playbook.playbook import Playbook
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    # Setup the play
    play_source = dict(
        name="test-role-load",
        hosts="test-server",
        gather_facts="no",
        roles=[
            dict(
                role="test_role",
                tags=["test_role"],
            )
        ]
    )
    play = Play().load(play_source, variable_manager=VariableManager(), loader=DataLoader())
   

# Generated at 2022-06-13 09:06:52.226811
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    class FakeBlock(object):
        def __init__(self, parent, role):
            self._parent = parent
            self._role = role
            self.action = 'include_role'
            self.vars = {}

        def get_role_params(self):
            return {}

    class FakeRole(object):
        def __init__(self, parents):
            self._parents = parents

        def get_role_params(self):
            return {}

    class FakePlay(object):
        def __init__(self):
            self.roles = []
            self.handlers = []

    class FakeVariableManager(object):
        def get_vars(self, play=None, task=None):
            return {}

    class FakeLoader(object):
        def __init__(self):
            self._basedir = '.'

# Generated at 2022-06-13 09:06:59.069288
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():
    ir = IncludeRole()
    ir.name = "foo"
    assert ir.get_name() == "foo"
    ir.name = None
    ir._action = "foo"
    ir._role_name = "bar"
    assert ir.get_name() == "foo : bar"
    ir._action = "foo"
    ir._role_name = None
    assert ir.get_name() == "foo : %s" % ir._role_name

# Generated at 2022-06-13 09:07:09.007711
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    block = Block()
    ir = IncludeRole.load({'name': 'test'}, block=block)
    assert isinstance(ir, IncludeRole)

    ir = IncludeRole.load({'name': 'test', 'tasks_file': 'test.yml', 'vars_from': 'test.yml'}, block=block)
    assert isinstance(ir, IncludeRole)
    assert isinstance(ir._from_files, dict)
    assert ir._from_files == {'tasks': 'test.yml', 'vars': 'test.yml'}
    ir = IncludeRole.load({'name': 'test', 'tasks_file': 'test.yml', 'vars_from': 'test.yml', 'apply': {'foo': 'bar'}}, block=block)

# Generated at 2022-06-13 09:07:09.596946
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    pass

# Generated at 2022-06-13 09:07:18.582047
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    def assert_block_chain(block, chain):
        assert block._role_name == chain[0]
        if len(chain) > 1:
            assert_block_chain(block._parent, chain[1:])

    ify = IncludeRole.load(dict(name='foo'))
    ify._from_files = dict(tasks='tasks/main.yml')
    ify._role_name = 'foo'

    role_a = Role(name="foo")
    role_a._metadata.collections = {"collections": [], "collection_names": set()}
    role_a._role_path = "/abc/def/foo"
    role_a._tasks = [IncludeRole.load(dict(name='bar'), role=role_a)]

    role_b = Role(name="bar")
   

# Generated at 2022-06-13 09:07:58.033667
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.plugins.loader import vars_loader, lookup_loader, strategy_loader, action_loader
    from ansible.config.manager import ConfigManager
    from ansible.constants import DEFAULT_ROLES_PATH
    from ansible.utils.context_objects import AnsibleContext

    # needed to reload callback plugins when running tests
    strategy_loader._strategy_plugins = {}
    strategy_loader._strategy_paths = []
    action_loader._action

# Generated at 2022-06-13 09:08:09.593529
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    class FakeRole:
        def __init__(self):
            self.name = 'role1'
            self.path = 'roles/role1'

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=['localhost'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    block = Block()
    block.root_block = True

    role1 = FakeRole()
    role2 = FakeRole()
    role2.name = 'role2'
    role2.path = 'roles/role2'


# Generated at 2022-06-13 09:08:16.837195
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():

    def check_result(i_role, data):
        for key, value in data.items():
            if key == 'name':
                assert getattr(i_role, 'name') == value
            if key == 'tags':
                assert getattr(i_role, 'tags') == value
            if key == 'when':
                assert getattr(i_role, 'when') == value
            if key == 'any_errors_fatal':
                assert getattr(i_role, 'any_errors_fatal') == value
            if key == 'action':
                assert getattr(i_role, 'action') == value
            if key == 'public':
                assert getattr(i_role, 'public') == value

# Generated at 2022-06-13 09:08:20.126176
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    # Setup test
    block = Block(None, None)
    role = Role()
    task_include = TaskInclude(None, None)
    task = IncludeRole(block=block, role=role, task_include=task_include)
    task._role_name = 'some-role'
    result = task.get_block_list()

    # Check results
    assert result == ([], [])

# Generated at 2022-06-13 09:08:25.651155
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    """
    IncludeRole: Test method get_block_list
    """

    block = Block(
        role="include_role_unit_test_role",
        task_includes=[],
        always_post_tasks=[],
    )

    include_role = IncludeRole()
    include_role.action = 'include_role'
    include_role.args = {'name': 'include_role_unit_test_role'}
    include_role._parent = block

    block.task_includes.append(include_role)

    from ansible.playbook.play import Play
    from ansible.playbook.role.meta import RoleMetadata
    from ansible.playbook.role.definition import RoleDefinition

    import os
    import sys


# Generated at 2022-06-13 09:08:32.584533
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():
    include_role = IncludeRole()
    assert include_role.get_name() == 'include_role'
    include_role.name = 'name-of-task'
    assert include_role.get_name() == 'name-of-task'
    include_role.name = None
    include_role._role_name = 'some_role'
    assert include_role.get_name() == 'include_role : some_role'


# Generated at 2022-06-13 09:08:45.860855
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.vars.unsafe_proxy import UnsafeProxy

    # Test with an empty dictionary
    results = {
        'args': {},
        'unsafe_proxy_args': UnsafeProxy({})
    }
    block = Block(
        role=Role(),
        parent=ImmutableDict([('name', 'test_load')]),
        loader=None,
        variable_manager=None
    )
    assert IncludeRole.load({}, block=block)._role_name is None

    # Test with null values

# Generated at 2022-06-13 09:08:53.775055
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():

    def get_fake_loader(name):
        return name

    def get_fake_variable_manager(name):
        return name

    def get_fake_parent_role():
        return name

    def get_fake_block(name):
        return name

    @staticmethod
    def get_fake_play(name):
        return name

    role_name = "some_fake_name"
    fake_variable_manager = get_fake_variable_manager("fake_variable_manager")
    fake_loader = get_fake_loader("fake_loader")
    fake_parent_role = get_fake_parent_role("fake_parent_role")
    fake_block = get_fake_block("fake_block")
    fake_play = get_fake_play("fake_play")


# Generated at 2022-06-13 09:09:05.421951
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():

    # Test load() function with invalid action
    def test_load_invalid_action():
        data = dict(
            include_tasks='fake_include_tasks.yml',
            apply='""',
            public='true',
            allow_duplicates='false',
            rolespec_validate='false'
        )
        block = Block()
        role = Role()
        variable_manager=None
        loader=None

        ir = IncludeRole.load(data, block, role, variable_manager, loader)

        assert ir.include_tasks == 'fake_include_tasks.yml'
        assert ir.statically_loaded is False
        assert ir._public is True
        assert ir._allow_duplicates is False
        assert ir._rolespec_validate is False

    # Test load() function with invalid options

# Generated at 2022-06-13 09:09:17.013859
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():

    # Test case 1
    # Test with no given data
    data = dict()
    block = None
    role = None
    task_include = None
    variable_manager = None
    loader = None
    result = IncludeRole.load(data, block, role, task_include, variable_manager, loader)
    assert result is None

    # Test case 2
    # Test when name is not provided
    data = dict(role='test')
    block = None
    role = None
    task_include = None
    variable_manager = None
    loader = None
    result = IncludeRole.load(data, block, role, task_include, variable_manager, loader)
    assert result is None

    # Test case 3
    # Test when name is provided
    data = dict(name='test')
    block = None
    role = None


# Generated at 2022-06-13 09:10:22.542426
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    import os
    import tempfile
    import shutil

    from ansible.errors import AnsibleError
    from ansible.plugins.loader import role_loader

    ROLE_DIR = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'roles',
    )

    def _create_copy(role_name, copy_path):
        try:
            role_path = role_loader._find_role_path_with_deprecated(role_name, ROLE_DIR)
        except AnsibleError:
            # if we can't find the role, just ignore this test
            return False

        if copy_path is not None:
            # Create a copy of the role and return the path to the copied role
            shutil.copytree(role_path, copy_path)

# Generated at 2022-06-13 09:10:34.256244
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    # Test initialization of class IncludeRole
    data = dict(
        name="galaxy.role.name",
        tasks_from="internal.yml",
        vars_from="internal.yml",
        defaults_from="internal.yml",
        handlers_from="internal.yml",
        public=True,
        allow_duplicates=False,
    )
    include_role = IncludeRole.load(data)

    assert include_role._role_name == "galaxy.role.name"
    assert include_role._from_files == {
        "tasks": "internal.yml",
        "vars": "internal.yml",
        "defaults": "internal.yml",
        "handlers": "internal.yml",
    }
    assert include_role._public is True
    assert include_

# Generated at 2022-06-13 09:10:45.509194
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    import json
    from ansible.module_utils._text import to_text

    # Test case #1: 'name' is a required field for action
    # Parse json data for object IncludeRole
    data = {
        "role": "example_include_role",
        "tasks_from": "../tasks/main.yml"
    }
    data = json.loads(to_text(json.dumps(data)))
    data = {"include_role": data}

    # Test case #1.1: Raise AnsibleParserError

# Generated at 2022-06-13 09:10:54.627757
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    # initialize data structure
    block = Block()
    block.set_role_params(dict(name='role1'))
    block.set_play_params(dict(play_name='play1'))
    block.add_parent(Block())

    role = Role()
    role.set_play_params(dict(play_name='play1'))

    task_include = TaskInclude()

    # create object
    ir = IncludeRole(block, role, task_include)
    loader = DataLoader()
    variable_manager = VariableManager()
    play = role._play

    # assign valid values
    ir.name = 'include-role'

# Generated at 2022-06-13 09:11:09.244714
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.template import Templar

    p = Play().load({'name': 'test1', 'hosts': 'localhost', 'gather_facts': 'no'}, variable_manager=None, loader=None)
    # build simple block that might be from a role
    myblock = Block()
    myblock.name = 'test1'
    # add a find task to the block
    t = Task()
    t.action = 'find'
    t.args = dict(path='/')
    myblock.block = [t]
    # Now create an IncludeRole object
    role = 'ansible.builtin.find'
    ir = IncludeRole()
    ir.name = role
    ir._parent_role = None
    ir

# Generated at 2022-06-13 09:11:18.646186
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    from ansible.playbook.play_context import PlayContext

    # create play
    mock_loader, mock_inventory, mock_variable_manager = cli.setup_loader()
    mock_play = play.Play().load('', variable_manager=mock_variable_manager, loader=mock_loader)

    # create play context
    mock_variable_manager.set_nonpersistent_facts(dict(env='test'))
    mock_play_context = PlayContext()
    mock_play_context.network_os = 'ios'
    mock_variable_manager.set_nonpersistent_facts(mock_play_context.serialize())

    # create role include
    mock_loader, mock_inventory, mock_variable_manager = cli.setup_loader()


# Generated at 2022-06-13 09:11:22.012487
# Unit test for method get_name of class IncludeRole
def test_IncludeRole_get_name():
    task = IncludeRole()
    assert task.get_name() == 'include_role : None'
    task = IncludeRole(task_include=dict(name='task1'))
    assert task.get_name() == 'include_role : task1'


# Generated at 2022-06-13 09:11:28.276263
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    """
    test function - method get_block_list

    ansible-playbook -i inventory test.yaml

    test.yaml contents:

    - hosts: localhost

      roles:
        - first-role

      tasks:
      - include_role:
          name: include-role
    """

    # Setup
    options = {'connection': 'local', 'module_path': '', 'forks': 1, 'become': None, 'become_method': None,
               'become_user': None, 'check': False, 'diff': False, 'listhosts': None, 'listtasks': None,
               'listtags': None, 'syntax': None, 'vault_password': None, 'verbosity': 3, 'start_at_task': None,
               'private_key_file': None}

   

# Generated at 2022-06-13 09:11:37.526564
# Unit test for method get_block_list of class IncludeRole
def test_IncludeRole_get_block_list():
    """Unit test for method get_block_list of class IncludeRole"""

    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.executor.task_result import TaskResult
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.block import Default


    #pylint: disable=unused-argument
    def _create_task(self, task):
        pass


# Generated at 2022-06-13 09:11:38.210398
# Unit test for method load of class IncludeRole
def test_IncludeRole_load():
    pass