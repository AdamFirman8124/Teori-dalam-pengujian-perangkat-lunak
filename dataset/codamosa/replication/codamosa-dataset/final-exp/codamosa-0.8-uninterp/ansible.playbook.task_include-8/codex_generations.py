

# Generated at 2022-06-13 09:23:53.326534
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    task = TaskInclude()
    data = {"action": "include", "args": {}, "name": "this is a name"}

    expected_msg = "Unexpected key 'name', it should be one of: ['action', 'args', 'collections', 'debugger', 'ignore_errors', 'loop', 'loop_control', 'loop_with', 'no_log', 'register', 'run_once', 'tags', 'timeout', 'vars', 'when']"
    try:
        task.preprocess_data(data)
    except AnsibleParserError as e:
        assert expected_msg in str(e)
    else:
        raise Exception("Unexpected success, exception should have been raised")

    data.pop("name")
    data["action"] = "include_tasks"
    data["apply"] = {"not": "dict"}


# Generated at 2022-06-13 09:24:04.422353
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    task = TaskInclude()
    task.action = 'import_tasks'
    task.vars = {}
    task.args['name'] = '[OK]'
    task.args['age'] = '[OK]'
    assert task.get_vars() == {}

    task.action = 'include_tasks'
    task.vars = {}
    task.args['name'] = '[OK]'
    task.args['age'] = '[OK]'
    assert task.get_vars() == {'name': '[OK]', 'age': '[OK]'}

    task.action = 'include_role'
    task.vars = {}
    task.args['name'] = '[OK]'
    task.args['age'] = '[OK]'

# Generated at 2022-06-13 09:24:10.697246
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    from ansible.playbook.role import Role
    from ansible.playbook.play_context import PlayContext

    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader

    variable_manager = VariableManager()
    loader = DataLoader()
    variable_manager.set_loader(loader)
    variable_manager.set_inventory(loader.load_inventory('localhost'))

    play_context = PlayContext()
    variable_manager.set_play_context(play_context)

    block = Block.load(
        {
            'name': 'included_block',
        },
        variable_manager=variable_manager,
        loader=loader,
    )

# Generated at 2022-06-13 09:24:21.261202
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    class FakeTaskInclude(TaskInclude):
        valid_options_new_method = TaskInclude.VALID_ARGS
        valid_options_old_method = TaskInclude.BASE

    task_include = FakeTaskInclude()
    task = Task()
    task.action = 'include'

    # Check invalid options
    task.args['invalid_option'] = 'fake_option'
    with pytest.raises(AnsibleParserError):
        task_include.check_options(task, task.args)

    # Check valid options
    for option in task_include.valid_options_new_method:
        task.args.clear()
        task.args[option] = 'fake_option'
        task_include.check_options(task, task.args)

    # Check valid options for tasks with old method


# Generated at 2022-06-13 09:24:25.385674
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():

    # Scenario 1: Check action is not 'include'
    with pytest.raises(Exception):
        TaskInclude.get_vars()


    # Scenario 2: Check when action is 'include'
    with pytest.raises(Exception):
        TaskInclude.get_vars()

# Generated at 2022-06-13 09:24:29.212164
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    ti = TaskInclude()
    ds = dict(action='include_role', file='foo.yml', name='bar', not_allowed='baz')
    ds = ti.preprocess_data(ds)
    assert ds == dict(action='include_role', file='foo.yml', name='bar')

# Generated at 2022-06-13 09:24:34.065290
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    # Create TaskInclude object
    ti = TaskInclude()

    # Create data structure
    ds = { "action": "include_role", "name": "test_name" }

    # Convert data
    ds_result = ti.preprocess_data(ds)

    # Compare result
    assert ds_result == ds


# Generated at 2022-06-13 09:24:38.959299
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    from ansible.playbook.block import Block

    class MyTaskInclude(TaskInclude):
        _valid_attrs = frozenset(('action',))

    ds = dict(
        block=dict(
            tasks=[
                dict(
                    action='include',
                    apply=dict(
                    ),
                ),
            ]
        ),
    )

    block = Block.load(
        ds,
        task_include=MyTaskInclude(),
    )

    action, args, _ = block.block_args.pop(0)
    assert action == 'include'

    # Since apply is an invalid attribute for include, it should have been removed by preprocess_data
    assert 'apply' not in args

# Generated at 2022-06-13 09:24:50.264619
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    from ansible.vars.manager import VariableManager
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils import context_objects as co

    vault_pass = 'dummypass'
    variable_manager = VariableManager()
    loader = DataLoader()
    vault_secrets = VaultLib(vault_pass).secrets.get('secret_1', vault_pass)
    variable_manager.extra_vars = {'vaulted_var': vault_secrets, 'plain_var': 'plain value of var'}
    variable_manager.set_nonpersistent_facts(dict(foo='bar'))
    co.global_vars.vault._set_variable_manager(variable_manager)

    # Single path (different forms

# Generated at 2022-06-13 09:25:01.371729
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    import pytest
    from ansible.playbook.task import Task
    ti = TaskInclude()
    task_data = 'included_task'
    # When parmeters are ok, 'check_options' not change the task
    task = ti.check_options(task_data, data={'action': 'include_tasks', 'file': 'tasks.yml'})
    assert task == task_data
    # When action is not an action which can have 'apply' as parameter
    with pytest.raises(AnsibleParserError):
        task = ti.check_options(task_data, data={'action': 'include_role', 'file': 'tasks.yml', 'apply': {}})
    # When file is not specified
    with pytest.raises(AnsibleParserError):
        task = ti

# Generated at 2022-06-13 09:25:12.562544
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    from ansible.playbook.block import Block
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task

    my_vars = dict(a='foo', b='bar')
    my_block = Block()
    my_block.vars = my_vars

    my_task = Task()
    my_task.action = 'include'
    my_task.args = dict(x='y')
    my_task._parent = my_block

    assert my_task.get_vars() == dict(a='foo', b='bar', x='y')

    # test 'include_role'
    my_task.action = 'include_role'
    assert my_task.get_vars() == dict(a='foo', b='bar')

    # test 'include_

# Generated at 2022-06-13 09:25:22.577097
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    # TaskInclude._validate_and_set_args should not raise for valid options
    for valid_options in [('file',), ('_raw_params',), ('_raw_params', 'apply')]:
        task = TaskInclude._validate_and_set_args(dict.fromkeys(valid_options))
        assert len(task.args) == len(valid_options)

    # TaskInclude._validate_and_set_args should raise for invalid options
    for invalid_options in [('file', 'bad_option'), ('_raw_params', 'bad_option')]:
        with pytest.raises(AnsibleParserError):
            task = TaskInclude._validate_and_set_args(dict.fromkeys(invalid_options))

    # TaskInclude._validate_and_set_args should raise if

# Generated at 2022-06-13 09:25:32.101688
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    # TaskInclude.get_vars no longer needs to retrieve the variables from its parents
    # as it is done in Task.get_vars but only for include tasks
    t = TaskInclude()
    assert t.get_vars() == dict()

    t.vars = dict(foo="bar")
    t.args = dict(hello="world")
    assert t.get_vars() == dict(foo="bar", hello="world")

    t.action = 'include_role'
    assert t.get_vars() == dict(foo="bar")

# Generated at 2022-06-13 09:25:39.685973
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    # Initialize the test object
    from ansible.playbook.play import Play
    from ansible.playbook.role import Role
    from ansible.playbook.task_include import TaskInclude
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText

    ti = TaskInclude()
    ti._role = Role()
    ti._parent = Play()
    ti._parent._play = Play()
    ti._parent._play._entries = []
    ti._loader = DataLoader()
    ti._variable_manager = VariableManager(loader=ti._loader, inventory=InventoryManager())

    # Test 1: 
    # input data:

# Generated at 2022-06-13 09:25:47.766181
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    # TaskInclude.check_options() should raise exception on invalid options
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager

    loader = DataLoader()
    variable_manager = VariableManager(loader=loader)
    inventory = InventoryManager(loader=loader, sources='localhost,')
    variable_manager.set_inventory(inventory)

    good_action = 'include'
    good_args = {'file': '/some/file'}
    good_data = {'action': good_action, 'args': good_args}

    # Everything that is allowed with regular tasks is allowed with an
    # include task
    bad_action = 'include'

# Generated at 2022-06-13 09:25:56.388385
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    class Task(TaskInclude):
        _task_fields = dict(
            file = FieldAttribute(isa='string'),
            apply = FieldAttribute(isa='dict'),
            when = FieldAttribute(isa='string'),
        )

    class ParentTask(Task):
        _task_fields = dict(
            name = FieldAttribute(isa='string'),
        )

    class Play:
        def __init__(self, name):
            self._name = name

        def get_name(self):
            return self._name

    dat1 = dict(
        apply = dict(
            block = dict(
                name = 'foo',
            ),
            tags = ['atag'],
        ),
        when = 'when foo',
        file = 'foo.yml',
    )


# Generated at 2022-06-13 09:26:07.451299
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    t = TaskInclude()

    # Test parent block
    t.vars = dict(a=1,b=2)
    t._parent = Block()
    t._parent.vars = dict(c=3,d=4)
    assert t.get_vars() == dict(a=1, b=2, c=3, d=4)

    # Test action 'include' with exclude tags and when
    t._parent = None
    t.action = 'include'
    t.args = dict(a=10, b=20, tags=1, when=1)
    assert t.get_vars() == dict(a=10, b=20)

    # Test action 'import_playbook'
    t.args = dict(a=10, b=20, d=5, e=6)

# Generated at 2022-06-13 09:26:15.987614
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    def assert_vars(task_include, expected_vars):
        actual_vars = task_include.get_vars()
        assert actual_vars == expected_vars, 'Expected: %s\nActual: %s' % (expected_vars, actual_vars)

    # Test for 'include' action
    block = Block()
    # args get merged into vars so the order is important to test
    block.vars = {'kwargs': {'key1': 'value1'}}
    block.args = {'key2': 'value2'}
    task_include = TaskInclude(action='include', block=block)
    assert_vars(task_include, {'key2': 'value2', 'kwargs': {'key1': 'value1'}})

    # Test for other

# Generated at 2022-06-13 09:26:25.729907
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    class TestTaskIncludeTask(TaskInclude):
        def __init__(self, name=None, load_name=None):
            super(TestTaskIncludeTask, self).__init__()
            self.name = name
            self.load_name = load_name

        def __hash__(self):
            return self.__repr__().__hash__()

        def __eq__(self, other):
            return self.__repr__() == other.__repr__()

    task = TestTaskIncludeTask(name='task', load_name='task_load')

    class TestTaskInclude(TaskInclude):
        def __init__(self, name='', paramdict=None, load_name='', load_paramdict=None):
            if paramdict is None:
                paramdict = dict()

# Generated at 2022-06-13 09:26:36.428923
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    '''test_TaskInclude_build_parent_block
    Test TaskInclude._build_parent_block
    '''
    from ansible.playbook.play import Play
    from ansible.playbook.role.meta import RoleMeta
    from ansible.utils import context_objects as co
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    test_loader = DataLoader()
    test_inv = InventoryManager(loader=test_loader, sources='')
    test_passwords = dict()
    test_vars_manager = VariableManager(loader=test_loader, inventory=test_inv)

# Generated at 2022-06-13 09:26:50.359664
# Unit test for method load of class TaskInclude
def test_TaskInclude_load():
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar

    from units.mock.loader import DictDataLoader

    data = dict(
        action=dict(
            meta='include',
            args=dict(
                file='include_foo.yml',
                apply=dict(
                    block=list(),
                ),
            ),
        ),
        name='include_foo',
    )

    play_context = PlayContext()
    templar = Templar(loader=DictDataLoader({}), variables={}, fail_on_undefined=True)

    task = TaskInclude.load(data, variable_manager=None, loader=None)
    task.post_validate(templar)
    task.preprocess_data()
    task.post_validate(templar)

# Generated at 2022-06-13 09:26:54.179549
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    task_include = TaskInclude()
    task_include.action = 'include'
    task_include.vars = {'a': 'a'}
    task_include.args = {'b': 'b'}

    result = task_include.get_vars()
    assert result['a'] == 'a'
    assert result['b'] == 'b'

# Generated at 2022-06-13 09:27:03.706944
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    '''
    TaskInclude: get_vars
    '''
    parent = TaskInclude()
    parent.action = 'include_role'
    parent._parent = TaskInclude()
    parent.vars = {'foo': 'bar'}
    parent.args = {'tags': [], 'when': 'True'}
    parent._parent.vars = {'fiz': 'buzz'}
    assert parent.get_vars() == {'fiz': 'buzz', 'foo': 'bar'}
    assert parent.get_vars() == parent._get_parent_attribute('get_vars', False)()

    parent = TaskInclude()
    parent.action = 'import_tasks'
    parent._parent = TaskInclude()
    parent.vars = {'foo': 'bar'}


# Generated at 2022-06-13 09:27:12.853413
# Unit test for method load of class TaskInclude
def test_TaskInclude_load():
    ''' test for TaskInclude class load() method
    '''
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.playbook_executor import PlaybookExecutor

    variable_manager = VariableManager()
    loader = DataLoader()

    inventory = InventoryManager(loader=loader, sources='localhost,')
    variable_manager.set_inventory(inventory)


# Generated at 2022-06-13 09:27:17.438436
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    loader = None
    blocks = list()
    role = None
    play = None
    inventory = InventoryManager(loader=loader)
    task = TaskInclude()
    tqm = None
    variable_manager = VariableManager(loader=loader, inventory=inventory, version_info=ansible_version_info)
    task._variable_manager = variable_manager
    task._tqm = tqm
    task.action = 'include_role'
    task.vars = dict(name='test_role', include_tasks=['test_task'])
    task.args = dict(name='test_role', include_tasks=['test_task'])

# Generated at 2022-06-13 09:27:27.194717
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    from ansible.playbook.play import Play
    from ansible.plugins.loader import get_all_plugin_loaders
    from ansible.template import Templar
    from ansible.vars import VariableManager

    assert TaskInclude().build_parent_block() is None
    task_include = TaskInclude()
    assert task_include.build_parent_block() is task_include

    task_include = TaskInclude(task_include=task_include)
    assert task_include.build_parent_block() is task_include

    TaskInclude.BASE = frozenset(('_raw_params',))
    task_include = TaskInclude(task_include=task_include)
    task_include.register = 'y'
    task_include.name = 'test'
    assert task_include.build_parent_block()

# Generated at 2022-06-13 09:27:34.764984
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    '''
    test case for method build_parent_block of class TaskInclude
    '''
    mytask = TaskInclude()
    mytask.args = {'apply': {'ignore_errors':True}}
    new_parent = mytask.build_parent_block()
    assert new_parent.ignore_errors is True
    new_parent.ignore_errors = False
    mytask.args = {}
    new_parent1 = mytask.build_parent_block()
    assert new_parent1.ignore_errors is False

# Generated at 2022-06-13 09:27:42.546524
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    from ansible.playbook import Play
    from ansible.playbook.play import Play as Play_obj
    from ansible.playbook.role.include import RoleInclude
    from ansible.playbook.task.include import IncludeTasks
    from ansible.vars import VariableManager
    from ansible.utils.vars import combine_vars

    variable_manager = VariableManager()
    loader = None

    pb = {
        "roles": [
            {
                "name": "foo",
                "role": "foobar"
            },
        ],
        "playbook_dir": ".",
    }

    p = Play.load(pb, variable_manager=variable_manager, loader=loader)
    play_obj = Play_obj.load(p, variable_manager=variable_manager, loader=loader)

   

# Generated at 2022-06-13 09:27:57.999284
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    import pytest

    block = None
    role = None
    task_include = None
    variable_manager = None
    loader = None
    data = dict(action='include', args=dict(_raw_params=None))
    ti = TaskInclude(block, role, task_include)

    with pytest.raises(AnsibleParserError):
        task = ti.check_options(ti.load_data(data, variable_manager=variable_manager, loader=loader), data)

    data = dict(action='include', args=dict(_raw_params='my-file'))
    task = ti.check_options(ti.load_data(data, variable_manager=variable_manager, loader=loader), data)

    assert task.action == 'include'
    assert isinstance(task, TaskInclude)


# Generated at 2022-06-13 09:28:05.834282
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    import copy
    import unittest

    from ansible.playbook.block import Block
    from ansible.playbook.task import Task

    class TaskIncludeUnitTest(unittest.TestCase):

        def test_build_parent_block_01(self):
            '''
            No apply attrs
            '''
            data = dict(action='include', file='foo')
            task = TaskInclude.load(
                data,
                task_include=Task(),
            )
            task.args['apply'] = None

            task.build_parent_block()
            self.assertEqual(task, task._parent)

        def test_build_parent_block_02(self):
            '''
            Apply attrs, no block
            '''
            data = dict(action='include', file='foo')
            task

# Generated at 2022-06-13 09:28:23.220660
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    # 1. Task with no args should raise an exception
    data = {'include': None}
    target = TaskInclude()
    raised_error = False
    try:
        target.check_options(target.load_data(data), data)
    except AnsibleParserError:
        raised_error = True

    assert raised_error, 'Task with no args should raise an exception'

    # 2. Task 'include' with file should not raise exception
    data = {'include': 'test_play.yml'}
    target = TaskInclude()
    raised_error = False
    try:
        target.check_options(target.load_data(data), data)
    except AnsibleParserError:
        raised_error = True

    assert not raised_error, 'Task with file should not raise exception'

    # 3. Task '

# Generated at 2022-06-13 09:28:24.452426
# Unit test for method load of class TaskInclude
def test_TaskInclude_load():
    pass

# Method build_parent_block of class TaskInclude

# Generated at 2022-06-13 09:28:31.597305
# Unit test for method check_options of class TaskInclude

# Generated at 2022-06-13 09:28:41.772948
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.playbook.role.definition import RoleDefinition

    p = Play().load({
        'name': 'aplay',
        'hosts': 'all',
        'gather_facts': 'no',
        'tasks': [
            {'action': 'include', 'args': {'file': 'file.yml', 'foo': 'bar'}},
        ],
    }, variable_manager=None, loader=None)

    include_task = p.get_task_by_name('include')
    assert isinstance(include_task, TaskInclude)

# Generated at 2022-06-13 09:28:48.415684
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    from ansible.playbook.role.definition import RoleDefinition

    class MockRole(RoleDefinition):
        def __init__(self, name):
            self.name = name

        def get_path(self):
            return '/dev/null'
    task = TaskInclude()

    # Check the case where the action is 'include'
    data = {'apply': dict(foo='bar'), '_raw_params': 'tasks/foo.yml', 'action': 'include'}
    task.check_options(task, data)

    # Check the case where the action is 'import_tasks'
    data = {'_raw_params': 'tasks/foo.yml', 'action': 'import_tasks'}
    task.check_options(task, data)

    # Check the case where the action is 'import_role

# Generated at 2022-06-13 09:28:54.285587
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    from ansible.parsing.dataloader import DataLoader
    loader = DataLoader()
    variable_manager = VariableManager()

    play_source = dict(
        name = "Ansible Play",
        hosts = 'all',
        gather_facts = 'no',
        vars = {},
    )
    play = Play().load(play_source, variable_manager=variable_manager, loader=loader)

# Generated at 2022-06-13 09:29:04.149052
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    action = 'include'
    data_loaded = {
        'action': action,
        'args': {
            'other_args': 'other_args_value'
        }
    }
    task_include = TaskInclude()
    task = task_include.load(data_loaded)
    task_loaded = task.check_options(task, data_loaded)
    assert isinstance(task_loaded, TaskInclude)
    assert task_loaded.action == action

    action = 'import_tasks'
    data_loaded = {
        'action': action,
        'args': {
            'file': 'file_value',
            'other_args': 'other_args_value'
        }
    }
    task_include = TaskInclude()
    task = task_include.load(data_loaded)
    task

# Generated at 2022-06-13 09:29:15.157614
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    import ansible.parsing.yaml.objects
    import ansible.playbook.helper
    import ansible.playbook.play
    import ansible.playbook.play_context
    import ansible.playbook.role
    import ansible.playbook.task

    from ansible.errors import AnsibleParserError
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude

    # Dummy variables for test
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    dummy_loader = DataLoader()
    dummy_variable_manager = VariableManager()

    # 1. Test with all valid keys and options
    # 1.1. with status=success

# Generated at 2022-06-13 09:29:24.313198
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    ti = TaskInclude()
    ti.args = {'foo': 'bar'}

    task = ti.check_options(ti, task_ds=None)
    assert task.args == {'foo': 'bar'}

    ti.args = {'action': 'include', 'file': 'xx'}
    task = ti.check_options(ti, task_ds=None)
    assert task.args == {'_raw_params': 'xx'}

    ti.args = {'action': 'include', 'file': 'xx', 'apply': {'a': 'b'}}
    task = ti.check_options(ti, task_ds=None)
    assert task.args['apply'] == {'a': 'b'}
    assert task.args['_raw_params'] == 'xx'


# Generated at 2022-06-13 09:29:31.598383
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    # module_defaults
    from ansible.module_utils._text import to_text, to_bytes
    from ansible.executor.task_result import TaskResult
    from ansible.executor.task_queue_manager import TaskQueueManager

    # test var
    test_var = {
        'a': {
            'b': 1,
            'c': True,
            'd': 'foo'
        },
        'e': ['a', 'b', 'c'],
        'f': ['d', 'e', 'f'],
        'g': {
            'h': 'foo',
            'i': 123,
            'j': 'bar'
        }
    }

    # test task
    test_task = TaskInclude()
    test_task.vars = test_var

# Generated at 2022-06-13 09:29:48.237413
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    '''
    Unit test function
    '''
    task_loader = TaskInclude()
    task_loader.vars = {'var1': 'var1'}                                             # No need of variable_manager
    task_loader.args = {'apply': {'when': 'when'}, 'var3': 'var3', 'var4': 'var4'}  # No need of loader
    block = task_loader.build_parent_block()
    assert len(block._attributes) == 2
    assert block.args.get('var3') == None
    assert block.args.get('var4') == None
    block_vars = block.get_vars()
    for key in ('var1', 'when'):
        assert block_vars.get(key) is not None

# Generated at 2022-06-13 09:29:58.263369
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    dict_data = dict(action='include_tasks', file='/tmp/test', apply=dict(tags=['test']))
    ti0 = TaskInclude.load(dict_data, block=None, role=None, task_include=None, variable_manager=None, loader=None)
    pbl0 = ti0.build_parent_block()
    assert not ti0.args.get('apply')
    assert isinstance(pbl0, Block)
    assert pbl0.block == []

    dict_data = dict(action='include_tasks', file='/tmp/test')
    ti0 = TaskInclude.load(dict_data, block=None, role=None, task_include=None, variable_manager=None, loader=None)
    pbl0 = ti0.build_parent_block()

# Generated at 2022-06-13 09:30:04.600973
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    # Import the class here to avoid circular imports
    from ansible.playbook.handler import HandlerTaskInclude

    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.utils.vars import merge_hash

    for test_class in (TaskInclude, HandlerTaskInclude):
        # Test case: no action
        data = {'x': 'y'}
        task = test_class()
        try:
            task = test_class.check_options(task, data)
            assert False, "An exception should have been raised"
        except AnsibleParserError as e:
            assert "Invalid options for " in to_text(e)

        # Test case: nothing to validate
        data = {'action': 'include_role'}
        task = test_class()
        task = test_

# Generated at 2022-06-13 09:30:15.873185
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    # Setup
    from ansible.playbook.block import Block
    from ansible.playbook.play_context import PlayContext

    task = TaskInclude.load({
        'apply': dict(
            block=dict(
                block=dict(
                    block=dict(
                        block=dict(),
                    ),
                ),
            ),
        ),
    })

    fake_play = dict(
        connection='local',
        gather_facts='no',
        hosts=[
            dict(name='127.0.0.1'),
        ],
    )
    context = PlayContext(play=fake_play)
    task._play = dict(
        name='null',
        play_context=context,
    )

    # Operation
    rv = task.build_parent_block()

    # Verification

# Generated at 2022-06-13 09:30:24.313125
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    '''
    Test preprocess_data method of class TaskInclude.
    '''
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    import unittest

    class TestPlaybookVars(unittest.TestCase):

        def setUp(self):
            pass

        def tearDown(self):
            pass

        def test_TaskInclude_preprocess_data(self):
            # Test static include
            static_data = dict(
                name="include task",
                action="include",
                file="static_file",
                args=dict(_raw_params="static_file"),
                static="static",
            )
            pv = PlayContext(variable_manager=VariableManager())
            ti = TaskInclude()

            p_data = ti.pre

# Generated at 2022-06-13 09:30:32.201534
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, sources='localhost')
    variable_manager.set_inventory(inventory)

# Generated at 2022-06-13 09:30:32.897511
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    pass

# Generated at 2022-06-13 09:30:42.725728
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    class MockPlaybook:
        def __init__(self):
            self.vars = {}

    class MockRole:
        def __init__(self):
            self.vars = {}

    class MockBlock:
        def __init__(self):
            self.vars = {}
            self._play = MockPlaybook()
            self._role = MockRole()

    task = TaskInclude()
    block = MockBlock()
    task._parent = block
    task.vars = {'C': 'D'}

    # basic test
    task.args = {'A': 'B'}
    all_vars = task.get_vars()
    assert({'A': 'B', 'C': 'D'} == all_vars)

    # 'include' action gets a little special treatment

# Generated at 2022-06-13 09:30:53.107045
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    task = TaskInclude()

    # test args validation with bad args
    data = {u'when': u'stuff', u'action': u'include_role', u'args': {u'file': u'common.yml', u'apply': u'stuff'}}

# Generated at 2022-06-13 09:31:04.358644
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    ti = TaskInclude()
    task = {'action': 'include', 'args': {'file': 't.yml', 'x': 1, 'y': 2, 'apply': {'a': 1, 'b': 2}}}
    invalid_task = {'action': 'include', 'args': {'file': 't.yml', 'x': 1, 'y': 2, 'apply': 'b'}}
    good_task = {'action': 'include', 'args': {'file': 't.yml', 'x': 1, 'y': 2}}
    res_task = {'action': 'include', 'args': {'_raw_params': 't.yml', 'x': 1, 'y': 2}}
    assert(res_task == ti.check_options(task, 'some data'))

# Generated at 2022-06-13 09:31:21.267148
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    '''
    Here we are checking the parent block created when ``apply`` is specified
    '''
    # pylint: disable=unused-import,import-error
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins import filter_loader
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.inventory.group import Group
    from ansible.inventory.host import Host
    from ansible.parsing.dataloader import DataLoader
    # pylint: enable=unused-import,import-error

    # create a dummy inventory
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=['localhost,'])
    host = Host('dummy')
    group = Group('dummy')
    group.add

# Generated at 2022-06-13 09:31:35.433766
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    #pylint: disable=R0903,R0904

    # ***** Test case: "apply" is specified *****
    class T1(TaskInclude):
        def __init__(self):
            self._parent = MockPlay()
            self._role = MockRole()
            self._variable_manager = MockVariableManager()
            self._loader = MockLoader()
            self.args = {'apply': {'name': 'test_TaskInclude_build_parent_block'}}

    ti = T1()
    assert ti.build_parent_block() is not ti

    # ***** Test case: "apply" is not specified *****
    class T2(TaskInclude):
        def __init__(self):
            self._parent = MockPlay()
            self._role = MockRole()
            self._variable_manager = Mock

# Generated at 2022-06-13 09:31:38.944275
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    task = TaskInclude()
    task.args = {'apply': {'ignore_errors': True}}
    block = task.build_parent_block()
    assert isinstance(block, Block), 'The method should return a Block instance'
    assert block.ignore_errors, 'The property should be True'


# Generated at 2022-06-13 09:31:49.448075
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.role_include import RoleInclude
    from ansible.playbook.role import Role
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.vars.hostvars import HostVars
    from ansible.vars.unsafe_proxy import UnsafeProxy

    templar = Templar(loader=None, variables=None)

    # load up a task

# Generated at 2022-06-13 09:31:57.502890
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    # Setup
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    play_context = PlayContext()
    variable_manager = VariableManager()
    loader = DataLoader()

    display.verbosity = 3

    # no param
    task_include = TaskInclude()
    task_include.check_options({'action': 'include'}, 'data')
    # no file
    task_include = TaskInclude()
    task_include.check_options({'action': 'include', '_raw_params': None}, 'data')
    # apply attr with non-dict value
    task_include = TaskInclude()

# Generated at 2022-06-13 09:32:05.715861
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    ti = TaskInclude()
    ti.validate_loop_controls = lambda task: task
    ti.validate_loop = lambda task: task
    ti.validate_tags = lambda task: task
    ti.validate_when = lambda task: task

    task_data = {
        'name': 'test',
        'action': 'include',
        'ignore_errors': True,
        'file': 'file.yml',
    }
    task = ti.check_options(ti.load_data(task_data), task_data)
    assert task.name == 'test'
    assert task.action == 'include'
    assert task.ignore_errors is True
    assert task.file is None
    assert task.args['_raw_params'] == 'file.yml'


# Generated at 2022-06-13 09:32:14.126352
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    import ansible.playbook.task_include
    import ansible.playbook.role
    from ansible.playbook.base import Base

    ti = ansible.playbook.task_include.TaskInclude()
    ti._parent = Base()
    ti._parent.add_role(ansible.playbook.role.Role())
    ti.vars = dict(a=1)
    ti.args = dict(b=2)

    # test get_vars() with no parent
    ti._parent = None
    ti._role = None
    assert ti.get_vars() == ti.vars

    # test with a parent, but not one we descended from
    ti._parent = Base()
    ti._role = None
    assert ti.get_vars() == ti.vars

    # test with a parent and a task

# Generated at 2022-06-13 09:32:16.120853
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    result = TaskInclude().build_parent_block()
    assert result.__class__.__name__ == 'TaskInclude'

# Generated at 2022-06-13 09:32:26.660989
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():

    import json
    import os
    import sys

    import yaml

    file_dir = os.path.dirname(__file__)
    file_dir = os.path.abspath(file_dir)

    role_dir = os.path.join(file_dir, '../examples/roles/test-restart')

    # use the actual yaml if possible, but fallback to the python version

# Generated at 2022-06-13 09:32:36.516051
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext

    ti = TaskInclude()
    p_block = Play()
    task = Task()

    # valid option
    task.action = 'include_tasks'
    task.args = {'file': 'foo.yaml'}
    ti.check_options(task, {})
    assert task.args['_raw_params'] == 'foo.yaml'

    # valid option
    task.args = {'_raw_params': 'foo.yaml'}
    ti.check_options(task, {})
    assert task.args['_raw_params'] == 'foo.yaml'

    # wrong keyword
    task.args = {'command': 'foo.yaml'}

# Generated at 2022-06-13 09:33:10.710128
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.base import Base
    from ansible.playbook.block import Block
    from ansible.playbook.handler import Handler
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.plugins.loader import remote_plugin_loader

    mock_loader = DataLoader()
    mock_var_manager = VariableManager()
    mock_var_manager._fact_cache = dict()  # type: ignore
    mock_all_blocks = list()
    mock_tasks = list()
    mock_handlers

# Generated at 2022-06-13 09:33:22.340246
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    from ansible.playbook.role_include import IncludeRole
    from ansible.playbook.task import Task
    from ansible.playbook.play import Play
    from ansible.playbook.playbook_include import IncludePlaybook

    p = Play()
    t = Task()

    pb = IncludePlaybook()
    ir = IncludeRole()

    p_d = {
        'block': [{
            'task': {
                'loop': 'test',
                'with_items': 'test'
            }
        }]
    }

    result = pb.check_options(pb.load_data(p_d, variable_manager=None, loader=None), p_d)
    p_block = result.build_parent_block()
    t_block = p_block.block[0]
    t_block

# Generated at 2022-06-13 09:33:31.212870
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    from ansible.playbook.play import Play
    from ansible.playbook.block import Block
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    variable_manager = VariableManager()
    play = Play().load(dict(name="t1", hosts=['localhost']), loader=loader, variable_manager=variable_manager)
    host = Host(name="localhost")
    group = Group(name="all")
    group.add_host(host)
    play.set_loader(loader)
    play.set_variable_manager(variable_manager)
    play.set_hosts([host])

    # When parent block is not provided


# Generated at 2022-06-13 09:33:42.035185
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    test_data = '''
- include: remote.yml
  vars:
    a: b
  when: c
  tags: [d, e]'''

    # test for 'include'
    for action in C._ACTION_ALL_INCLUDE_ROLE_TASKS:
        task = TaskInclude.load({'action': action, '_raw_params': 'foo.yml', 'vars': {'b': 'c'}})
        assert task.get_vars() == {'b': 'c', '_raw_params': 'foo.yml'}

    # test for 'import_playbook'
    task = TaskInclude.load({'action': 'import_playbook', '_raw_params': 'foo.yml', 'vars': {'b': 'c'}})
