

# Generated at 2022-06-13 09:23:53.070724
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():

    task_include = TaskInclude(block=None, role=None, task_include=None)

    # Test py3 compat
    assert isinstance(task_include.VALID_INCLUDE_KEYWORDS, frozenset)

    data = {'include': 'a'}
    res = task_include.preprocess_data(data)
    assert res == {'action': 'include', '_raw_params': 'a'}

    data = {'action': 'shell', 'include': {'no_log': True}}
    res = task_include.preprocess_data(data)
    assert res == {'action': 'shell', '_raw_params': {'no_log': True}}

    data = {'action': 'shell', 'include': {'no_log': True, 'not_valid_attribute': True}}

# Generated at 2022-06-13 09:24:04.344062
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.playbook.task_include import HandlerTaskInclude
    from ansible.collections.ansible.community.plugins.inventory.ini import InventoryModule

    play_context = PlayContext()
    play_context.inventory = InventoryModule()
    play_context.network_os = 'ios'
    play = Play().load({}, loader=None, variable_manager=None, play_context=play_context)
    task_include = TaskInclude(block=None, role=None, task_include=None)

# Generated at 2022-06-13 09:24:16.511490
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():

    import ansible.playbook.play
    import ansible.playbook.block
    import ansible.playbook.role

    task = ansible.playbook.task.Task()
    task.vars = dict()
    task.args = dict()
    task.action = 'include'
    play = ansible.playbook.play.Play()
    role = ansible.playbook.role.Role()

    task_include = TaskInclude(block=None, role=role, task_include=task)
    task_include.args = dict()
    task_include.args['apply'] = dict()
    task_include.args['apply']['block'] = list()

    parent_block = task_include.build_parent_block()

    assert isinstance(parent_block, ansible.playbook.block.Block)
   

# Generated at 2022-06-13 09:24:26.928643
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():

    # create TaskInclude instance
    taskinclude = TaskInclude()

    # add task to a new block
    block = Block(play=None)
    apply_task = Task()
    apply_task.action = 'include'
    apply_task.args = {'apply': '{"a": true}'}
    block.block = [apply_task]

    # check_options with a bad arg
    task = Task()
    task.action = 'include'
    task.args = {'bad_opt': 'true'}
    result = taskinclude.check_options(task, {'bad_opt': 'true'})
    assert result, "check_options should return the task"
    assert result.args['_raw_params'], "check_options should move the 'bad_opt' to _raw_params"

    # check_

# Generated at 2022-06-13 09:24:34.517305
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    ti = TaskInclude()
    data_set_1 = dict(action='include', file='admin.yml', vars=dict(foo=1), name='Admin tasks', debug=True)
    data_set_2 = dict(action='include', file='admin.yml', vars=dict(foo=1), name='Admin tasks', custom_attr=dict(foo=1))
    data_set_3 = dict(action='include', file='admin.yml', vars=dict(foo=1), name='Admin tasks', apply=dict(foo=1))
    data_set_4 = dict(action='include_role', file='admin.yml', vars=dict(foo=1), name='Admin tasks', tags=['bar'],
                      when='foo=1', apply=dict(foo=1))
    data_set_

# Generated at 2022-06-13 09:24:45.314524
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    tsk = TaskInclude()
    ds = {'file': 'test_include.yml', 'tags': ['tag1', 'tag2']}
    tsk.preprocess_data(ds)
    assert len(ds.keys()) == 2
    ds = {'file': 'test_include.yml', 'unknown_attr': 'invalid'}
    try:
        tsk.preprocess_data(ds)
    except AnsibleParserError as e:
        assert 'is not a valid attribute for TaskInclude' in str(e)
    else:
        assert False
    ds = {'file': 'test_include.yml', 'unknown_attr': 'invalid'}

# Generated at 2022-06-13 09:24:58.019774
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    '''
    Validates the check_options of TaskInclude returns an AnsibleParserError
    when an invalid option is provided and AnsibleParserError is raised when
    when a required option is not provided.
    '''

    import sys
    if sys.version_info[0] > 2:
        import mock

    if sys.version_info[0] > 2:
        my_mock = mock.Mock()
        my_mock.args = dict(file='file_name')
        my_mock.action = 'include_role'
    else:
        from mock import Mock
        my_mock = Mock()
        my_mock.args = dict(file='file_name')
        my_mock.action = 'include_role'


    import pytest

# Generated at 2022-06-13 09:25:08.049952
# Unit test for method preprocess_data of class TaskInclude

# Generated at 2022-06-13 09:25:16.844747
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    '''
    Unit tests for TaskInclude class method preprocess_data
    '''
    # Test case 1: check that invalid attributes raise errors
    ds = {
        'action': 'include',
        'no_such_attribute': None,
    }
    ti = TaskInclude()
    ti.preprocess_data(ds)
    assert ds['no_such_attribute'] is Sentinel, 'no_such_attribute should have been removed'
    del ds['no_such_attribute']

# Generated at 2022-06-13 09:25:29.757594
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.role import Role
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager


# Generated at 2022-06-13 09:25:46.141485
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    import json
    import os
    import tempfile
    from ansible.utils.path import unfrackpath

    # -------------------------------------------------------------------------------------------------
    # test case #1: apply provided
    # -------------------------------------------------------------------------------------------------
    #
    # test setup
    #
    data = {}
    data["action"] = "include_tasks"
    data["apply"] = {}
    data["apply"]["name"] = "Include tasks with apply provided"
    data["args"] = {}
    data["args"]["file"] = "test_include.yml"
    data["ignore_errors"] = False

    display.verbosity = 3
    temp_dir = tempfile.mkdtemp()
    current_path = os.getcwd()

    #
    # test steps
    #

# Generated at 2022-06-13 09:25:50.454935
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    from ansible.playbook.task_include import HandlerTaskInclude
    from ansible.parsing.yaml.objects import AnsibleUnicode

    data = dict(
        file='a',
        action='b',
        name='c',
        debug='d',
        rare_attr=dict(),
        apply=dict(
            line='e',
            loop='f'
        ),
        args=dict(),
    )
    task = TaskInclude.check_options(
        TaskInclude.load_data(data, variable_manager=None, loader=None), data
    )

# Generated at 2022-06-13 09:25:57.944190
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():

    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import HandlerTaskInclude

    # This check does not depend on anything, it only checks that the
    # method raises no exception for valid task_actions:
    for task_action in C._ACTION_ALL_PROPER_INCLUDE_IMPORT_TASKS:
        play = Play().load({'name': 'test_TaskInclude_check_options', 'hosts': 'localhost'},
                           variable_manager=None,
                           loader=None)
        ti = TaskInclude(block=play, role=None, task_include=None)

        result = ti.check_options(Task(), {'action': task_action})
        assert result.action == task_action

    # This

# Generated at 2022-06-13 09:26:03.316149
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    # Test for data containing a key for which TaskInclude has _validate_* method
    ds = dict(a=1, action='include', b=2, c=3, d=4, e=5, f=6)
    task = TaskInclude.load(ds, task_include=None)
    ds = task.preprocess_data(ds)
    assert ds['action'] == 'include'
    assert 'a' not in ds
    assert 'b' not in ds
    assert 'c' not in ds
    assert 'd' not in ds
    assert 'e' not in ds
    assert 'f' not in ds

    # Test for data containing a key for which action is include

# Generated at 2022-06-13 09:26:13.215838
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    def new_TaskInclude(args):
        # Create a fake task
        data = {}
        data['block'] = []
        data['action'] = 'include_role'
        data['args'] = args
        ti = TaskInclude.load(data)
        ti._parent = None
        return ti

    # task with apply
    task_args = {}
    task_args['apply'] = {}
    task_args['apply']['block'] = []
    ti = new_TaskInclude(task_args)
    # no apply, task = parent = self
    p_block = ti.build_parent_block()
    assert p_block == ti
    assert p_block != ti._parent
    assert p_block._parent != ti._parent
    # the task is not a block

# Generated at 2022-06-13 09:26:24.867305
# Unit test for method load of class TaskInclude
def test_TaskInclude_load():
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    play_context = PlayContext()
    variable_manager = VariableManager(
        loader=loader,
        play_context=play_context,
    )

    def create_include_task(task_action):
        test_task = dict(
            action=task_action,
            args=dict(
                static='yes',
                apply=dict(
                    block='yes you can apply this',
                    debug='should only be applied to task includes',
                )
            )
        )

        return TaskInclude.load(test_task, variable_manager=variable_manager, loader=loader)

    TaskInclude.BASE

# Generated at 2022-06-13 09:26:30.910983
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    # This is a dummy data to run 'check_options' with. The original data is
    # not really necessary as we only use '_data' in the method we're testing.
    data = {
        'action': 'include',
        'args': {
            '_raw_params': '/toto.yml',
        },
    }

    # Tasks that should be allowed with keywords 'args' and 'ignore_errors'
    valid_tasks = ('include', 'include_role', 'import_playbook', 'import_tasks')
    # Tasks that should only be allowed with keywords 'file', 'args' and 'ignore_errors'
    valid_tasks_with_file = ('include_tasks', 'include_vars', 'include_tasks')

    # Check that invalid keywords raise an exception.
    # This is used to

# Generated at 2022-06-13 09:26:38.812417
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    # Unit test: TaskInclude.check_options()
    #-----------------------------------------------------------------------
    # Illegal include arguments should raise an exception
    #-----------------------------------------------------------------------
    ti = TaskInclude()
    data = {'action': 'include', 'file': '/path/to/file', 'bad_arg': 'illegal value'}
    task = ti.check_options(TaskInclude.load_data(data, None, None), data)
    assert isinstance(task, TaskInclude)

    #-----------------------------------------------------------------------
    # Legal include arguments should not raise an exception
    #-----------------------------------------------------------------------
    ti = TaskInclude()
    data = {'action': 'include', 'file': '/path/to/file', 'tags': ['foo', 'bar']}
    task = ti.check_options(TaskInclude.load_data(data, None, None), data)

# Generated at 2022-06-13 09:26:51.941697
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    from ansible.playbook.play import Play
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.role.include import IncludeRole

    play = Play().load({
        'hosts': 'localhost',
        'tasks': [
            {
                'include_role': {
                    'name': 'include_role_test',
                    'apply': {
                        'when': 'always'
                    }
                }
            }
        ]
    }, variable_manager=None, loader=None)

    role = RoleDefinition()
    role._role_name = 'include_role_test'
    role._role_path = '/dev/null'
    role._role = role
    role.get_tasks = lambda: []


# Generated at 2022-06-13 09:27:02.767146
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.playbook.block import Block

# Generated at 2022-06-13 09:27:18.240109
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    from .test_play import TestPlay
    from .test_block import TestBlock
    from .test_task import TestTask
    import os

    test_play = TestPlay()
    test_play.load_data()
    test_play.post_validate()
    test_play.instantiate_vars()

    test_task = TestTask.load(dict(
        action='include_role',
        args=dict(
            apply=dict(
                meta=dict(
                    foo='bar'
                ),
                tasks=dict(
                    hello='world'
                )
            )
        )
    ), play=test_play, task_include=None, role=TestRole())

    test_task.preprocess_data()
    test_task.post_validate(test_task._play, test_task)

   

# Generated at 2022-06-13 09:27:27.641870
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    # Todo: fix namespace variables:
    #  - here we need to create a parent in order to have namespace variables
    #  - but in this case, it test the tests: we are not testing the method
    #    "get_vars" but the method "get_vars" and a lot of things around (ex:
    #    _build_parent_block())
    # We can make a class patching the method "get_vars" of class TaskInclude
    # but it seems complicated.
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.play import Play

    ti = TaskInclude(block = Block(play = Play()))

    ti.vars = {'a': 'b'}

# Generated at 2022-06-13 09:27:33.491078
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    # GIVEN
    my_apply = {
        'action': 'add_host',
        'block': []
    }

    # WHEN
    ti = TaskInclude()
    ti.args['apply'] = my_apply
    p_block = ti.build_parent_block()

    # THEN
    assert p_block._action == 'add_host'


# Generated at 2022-06-13 09:27:41.517545
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():

    # Test setup
    include_task = TaskInclude()

    # Test exception handler of method get_vars
    try:
        include_task.action = "include"
        include_task.args = {"_raw_params": "test_file.yml", "verbose": "yes"}
        include_task._parent = None
        include_task.vars = {"msg": "Hello World"}
        include_task.tags = ["test_tag"]
        include_task.when = "test_condition"

        result = include_task.get_vars()

        if "verbose" not in result:
            raise KeyError("A KeyError was not raised for the incorrect 'get_vars' test.")

    except KeyError:
        pass


# Generated at 2022-06-13 09:27:56.817597
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    # Shared variables to use in tests
    class MyMergedOptions:
        def __init__(self, dict_):
            self.dict = dict_

        def __getitem__(self, k):
            return self.dict[k]

        def __setitem__(self, k, v):
            self.dict[k] = v

        def __contains__(self, k):
            return k == 'objects' or k in self.dict

        def keys(self):
            return self.dict.keys()

    variable_manager = None
    loader = None
    task = TaskInclude(variable_manager=variable_manager, loader=loader)
    data = dict()

    # TEST 1: include with no action
    # Continue on exception to ensure that all cases are covered

# Generated at 2022-06-13 09:28:04.546423
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    task = TaskInclude()
    with pytest.raises(AnsibleParserError):
        task.check_options(task, {})
    task = TaskInclude()
    task.action = 'action_test'
    task.args = {'apply': None}
    with pytest.raises(AnsibleParserError):
        task.check_options(task, {})
    task = TaskInclude()
    task.action = 'action_test'
    task.args = {'apply': {}}
    task.check_options(task, {})
    task = TaskInclude()
    task.args['_raw_params'] = 'test'
    task.check_options(task, {})

# Generated at 2022-06-13 09:28:08.671056
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    from ansible.playbook.play import Play
    from ansible.playbook.role_include import IncludeRole
    from ansible.playbook.handler import Handler
    from ansible.vars.hostvars import HostVars
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.module_utils._text import to_bytes, to_native

    fake_loader = DataLoader()
    inv_manager = InventoryManager(loader=fake_loader, sources=C.DEFAULT_HOST_LIST)
    var_manager = VariableManager(loader=fake_loader, inventory=inv_manager)

    my_host

# Generated at 2022-06-13 09:28:18.588411
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    ti = TaskInclude()

    # option file and _raw_params are mutually exclusive
    task = {}
    task['args'] = {}
    task['args']['file'] = 'test.yml'
    task['args']['_raw_params'] = 'test.yml'
    task['action'] = 'include'
    assert 'file' in task['args'].keys()
    assert '_raw_params' in task['args'].keys()
    ti.check_options(task, {})
    assert '_raw_params' in task['args'].keys()
    assert 'file' not in task['args'].keys()

    # option file is required
    task = {}
    task['args'] = {}
    task['args']['_raw_params'] = None

# Generated at 2022-06-13 09:28:21.157552
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    ti = TaskInclude()
    ti.args = {'apply': {'some_param': 'some_value'}}
    assert isinstance(ti.build_parent_block(), Block)

# Generated at 2022-06-13 09:28:29.518364
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    from ansible.playbook.play_context import PlayContext

    # Setup a class instance
    ti = TaskInclude()
    ti._loader = None
    ti._variable_manager = None
    ti._parent = None
    ti._parent._play = None
    ti._parent._play.context = PlayContext(remote_user='test', connection='tcp')
    ti._parent._play._loader = None
    ti._parent._play._variable_manager = None

    # Create a fake task to simulate include values

# Generated at 2022-06-13 09:28:51.978709
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext

    fake_play = Play.load({
        'name': 'fake_play',
        'hosts': 'all',
        'tasks': [
            dict(
                include=dict(
                    file='fake_file',
                    other_attr=dict(a='a', b='b'),
                )
            )
        ]
    })
    fake_play.PLAY_CONTEXT = PlayContext()

    fake_task_include = fake_play.tasks[0]
    assert isinstance(fake_task_include, TaskInclude)


# Generated at 2022-06-13 09:29:02.306629
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    from ansible.playbook.play_context import PlayContext
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    pc = PlayContext()
    im = InventoryManager(loader=DataLoader(), sources=[])
    vm = VariableManager(loader=DataLoader(), inventory=im)

    task = TaskInclude.load(dict(include='test', tags=['always']), variable_manager=vm, loader=DataLoader())
    task.action = 'include'
    assert task.get_vars() == {'include': 'test'}
    
    task.action = 'import_tasks'
    assert task.get_vars() == {'include': 'test'}
    

# Generated at 2022-06-13 09:29:14.382538
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play_context import PlayContext

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, variable_manager=variable_manager, sources=(__file__,))
    variable_manager.set_inventory(inventory)
    play_context = PlayContext()

    data = {'block': [{'action': 'include_role', 'name': 'common', 'collections': ['community.general'], 'tasks': []}]}

    ti = TaskInclude()
    result = ti.preprocess_data(data['block'][0])
    assert result['collections'] == ['community.general']


# Generated at 2022-06-13 09:29:23.376089
# Unit test for method load of class TaskInclude
def test_TaskInclude_load():
    from ansible.inventory.host import Host
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.playbook.play import Play

    def _create_task(action, data, loader, variable_manager, block=None, role=None, task_include=None, static=False):
        data['action'] = action
        task = TaskInclude.load(
            data,
            block=block,
            role=role,
            task_include=task_include,
            variable_manager=variable_manager,
            loader=loader)
        task.static = static

        return task

    #########
    # Tests #
    #########

    # Loader
    loader = DataLoader()

    # Variable manager
    variable_manager = VariableManager()


# Generated at 2022-06-13 09:29:37.747187
# Unit test for method get_vars of class TaskInclude

# Generated at 2022-06-13 09:29:44.342035
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    task_data = {}
    task_data['block'] = [{'block': [{'key1': 'value1'}]}]
    block = Block.load(task_data)
    # Check if the block is created or not
    assert block is not None
    # Check if block is an instance of class Block
    assert isinstance(block, Block)

    task_data = {}
    task_data['task_include'] = Block(parent=block, role=block._role)
    task = TaskInclude.load(task_data, block=block, role=block._role)
    # Check if the task is created or not
    assert task is not None
    # Check if task and task_data are an instance of class TaskInclude
    assert isinstance(task, TaskInclude)

    task_data = {}
    task_data

# Generated at 2022-06-13 09:29:50.912695
# Unit test for method load of class TaskInclude
def test_TaskInclude_load():

    import pytest
    from ansible.playbook.attribute import FieldAttribute
    from ansible.playbook.play_context import PlayContext

    file_path = 'tests/unit/playbooks/block/task_include.yml'
    pb = Playbook.load(file_path)
    play = pb.get_plays()[0]
    variable_manager = VariableManager()
    variable_manager._fact_cache = {}
    play._variable_manager = variable_manager
    play.post_validate(play._play_context, variable_manager)

    for task_block in play.compile():
        for task in task_block.block:
            task.post_validate(play._play_context, variable_manager)
            if task.action == 'include':
                assert task.statically_loaded == False

# Generated at 2022-06-13 09:29:57.297156
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    from ansible.playbook.task import Task

    TASK_DS = dict(
        action='include',
        args=dict(
            file='file name'
        )
    )

    task = TaskInclude.load(TASK_DS)
    vars = task.get_vars()
    assert set(vars.keys()) == set(['file'])

    task = Task.load(TASK_DS)
    vars = task.get_vars()
    assert set(vars.keys()) == set(['file'])

# Generated at 2022-06-13 09:30:05.080273
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    from ansible.playbook.role.include import RoleInclude
    from ansible.playbook.role import Role
    from ansible.playbook.play import Play
    from ansible.playbook.block import Block
    from ansible.inventory.host import Host
    from ansible.vars import VariableManager

    # create a basic host
    host = Host(name="test_host")

    # create a basic play
    play = Play().load({'name': 'fakeplay'}, variable_manager=VariableManager(), loader=None)

    # create a basic block
    block = Block().load({'name': 'fakeblock'}, play=play, task_include=None, role=None, variable_manager=VariableManager(), loader=None)

    # create a basic include

# Generated at 2022-06-13 09:30:14.687157
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    import ansible.playbook
    import ansible.playbook.play
    import ansible.playbook.handler
    import ansible.playbook.task

    p = ansible.playbook.Play()
    role = ansible.playbook.role.Role()
    MockParent = ansible.playbook.task.Task.make_subclass('MockParent', {'action': FieldAttribute(isa='string'), 'block': FieldAttribute(isa='list')})
    parent = MockParent(dict(action='mock', block=[]), p)
    ti = TaskInclude(parent, role=role)
    ti.action = 'include'
    assert ti.build_parent_block() == ti

# Generated at 2022-06-13 09:30:40.969846
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    from ansible.playbook.play import Play

    play1 = Play()
    play1_name = 'Test Play 1'
    play1.name = play1_name

    task1 = TaskInclude(play=play1)
    task1_name = 'Test Task 1'
    task1.name = task1_name

    block1 = Block()
    block1_name = 'Test Block 1'
    block1.name = block1_name
    block1.add(task1)

    task2 = TaskInclude(block=block1, play=play1)
    task2_name = 'Test Task 2'
    task2_args = {'foo': 'bar'}
    task2_with_items = 'test with items'
    task2_loop_control = {'label': 'test label'}
    task

# Generated at 2022-06-13 09:30:49.283296
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    from ansible.playbook.play import Play
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=['localhost'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    # Create a dummy play
    play = Play.load({}, variable_manager=variable_manager, loader=loader)

    ti = TaskInclude(block=play)

    ti.args = {'_raw_params': "include_vars: '{{ foo }}'", 'apply': {'tags': ['all']}}
    p_block = ti.build_parent_block()
    assert p_block.parent == play

# Generated at 2022-06-13 09:30:53.527600
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    taskin = TaskInclude()
    taskin.args = {
        'include': 'dummy',
        'x': 'y'
    }
    taskin.vars = {
        'a': 'b'
    }
    assert 'x' in taskin.get_vars()

# Generated at 2022-06-13 09:31:04.516598
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    from ansible.playbook.play_context import PlayContext
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    vm = VariableManager()
    loader = DataLoader()
    pb = PlayContext(play=None)
    pb.CONNECTION_PLUGIN_PATH = '.'
    pb.variable_manager = vm
    pb.inventory = InventoryManager("localhost", pb, loader)
    t = TaskInclude()
    t.action = 'include'
    t.args = {'_raw_params': 'test', 'a': 'a', 'b': 'b'}
    t.vars = {'c': 'c', 'd': 'd'}
    t._parent = pb

# Generated at 2022-06-13 09:31:11.590220
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    ti = TaskInclude()
    ti.vars = dict(
        one=1,
        two=2,
    )
    ti.args = dict(
        three=3,
        four=4,
    )
    ti._parent = Block()
    ti._parent.get_vars = lambda: dict(
        parent_one=1,
    )

    for action in C._ACTION_INCLUDE:
        ti.action = action
        ti.get_vars()

    for action in C._ACTION_ALL_PROPER_INCLUDE_IMPORT_TASKS:
        if action not in C._ACTION_INCLUDE:
            ti.action = action
            ti.get_vars()

# Generated at 2022-06-13 09:31:19.813948
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    data = {'action': 'include', 'apply': 'yes', 'debug': 'yes', 'file': 'some_file.yml'}
    block = Block.load(
        {'action': 'include', 'apply': 'yes', 'debug': 'yes', 'file': 'some_file.yml'},
        play=None,
        task_include=None,
        role=None,
        variable_manager=None,
        loader=None
    )
    ti = TaskInclude.load(
        data,
        block=block,
        role=None,
        task_include=None,
        variable_manager=None,
        loader=None
    )

    # There is no real data to preprocess here, so we want to simply check if the method
    # runs without raising an exception.
    assert ti.preprocess

# Generated at 2022-06-13 09:31:28.316089
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    # Scenario: There is a TaskInclude with a apply argument
    task_include_json = {
        'apply': {
            'serial': 2
        }
    }
    result = TaskInclude.load(task_include_json).build_parent_block()
    assert result._parent_block.serial == 2
    # Scenario: There is a TaskInclude without a apply argument
    task_include_json = {}
    result = TaskInclude.load(task_include_json).build_parent_block()
    assert result == TaskInclude.load(task_include_json)

# Generated at 2022-06-13 09:31:35.643477
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.play import Play

    task_include_dict = {'apply': {'when': 'true'}, 'block': [{'name': 'task name'}], '_lineage': [], '_role': None,
                         '_play': Play.load({'name': 'play name'}), '_loader': None, '_variable_manager': None,
                         'args': {'apply': {}}, 'action': 'include'}

    task_include = TaskInclude.load(task_include_dict)
    result = task_include.build_parent_block().__dict__
    assert result['block'][0].__dict__ == task_include_dict['block'][0]

# Generated at 2022-06-13 09:31:42.558461
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    from ansible.playbook.block import Block
    from ansible.playbook.role.definition import RoleDefinition

    block = Block()
    role = RoleDefinition()
    task_include = TaskInclude(block=block, role=role)
    # A single valid argument
    assert task_include.check_options(task_include, {'include': {'file': 'test_file'}}) == task_include
    # Two valid arguments
    assert task_include.check_options(task_include, {'include': {'file': 'test_file', 'apply': {'some': 'vars'}}}) == task_include
    # No file argument
    assert task_include.check_options(task_include, {'include': {'task': 'debug', 'apply': {'some': 'vars'}}}) == task_include


# Generated at 2022-06-13 09:31:52.242551
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    from ansible.playbook.play_context import PlayContext

    task = TaskInclude()
    task._parent = Block()
    task._parent.vars = dict(
        ansible_connection='local',
        ansible_ssh_user='root',
    )
    task.action = 'include'
    task.args = dict(
        file='/tmp/tasks.yml',
        user='root',
    )
    task.vars = dict(
        this='is a var',
    )
    task.when = 'True'
    task.tags = ['always']


# Generated at 2022-06-13 09:32:41.692374
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    tasks = {
        'meta': {},
        'tasks': [{
            'include': 'somefile.yml',
            'no_log': True,
            'tags': ['foo', 'bar'],
        }, {
            'include': 'somefile.yml',
            'apply': {'block': 'foo'},
        }, {
            'include': 'somefile.yml',
            'apply': {'block': 'foo', 'store_result': True},
        },{
            'include': 'somefile.yml',
            'apply': 'bar',
        }],
    }
    data = tasks['tasks'][0]
    task = TaskInclude.load_data(data, variable_manager=None, loader=None)
    task = task.check_options(task, data)
   

# Generated at 2022-06-13 09:32:54.150328
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    task_include = TaskInclude()
    task = Task()
    task.action = 'include_role'
    task.args['collections'] = 'col'
    task.args['file'] = 'file'
    task.args['apply'] = 'apply'
    task.args['apply_async'] = 'apply_async'
    task.args['no_log'] = 'no_log'
    task.args['ignore_errors'] = 'ignore_errors'
    task.args['ignore_unreachable'] = 'ignore_unreachable'
    task.args['name'] = 'name'
    task.args['run_once'] = 'run_once'
    task.args['tags'] = 'tags'
    task.args['vars'] = 'vars'
    task.args['when'] = 'when'

# Generated at 2022-06-13 09:33:08.933540
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    '''
    Unit test for method get_vars of class TaskInclude.
    '''
    # - include: my_task.yml
    my_task_include = TaskInclude()
    my_task_include.action = 'include'
    my_task_include._parent = None
    my_task_include.vars = {}
    my_task_include.args = dict()
    my_task_include.args['_raw_params'] = 'my_task.yml'
    my_task_include.args['tags'] = ['1']
    my_task_include.args['when'] = ['2']
    my_vars = my_task_include.get_vars()
    assert(my_vars == dict())

    # - include_role:
    my_include_role = TaskInclude

# Generated at 2022-06-13 09:33:20.658167
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():

    # Create a simple task
    from ansible.playbook import Play
    from ansible.playbook.task_include import TaskInclude
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.utils.vars import combine_vars
    from ansible.utils.display import Display
    from ansible.utils.sentinel import Sentinel
    from ansible.plugins.loader import action_loader

    loader = DataLoader()
    inv_manager = InventoryManager(loader=loader, sources='localhost,')
    variable_manager = VariableManager(loader=loader, inventory=inv_manager)

# Generated at 2022-06-13 09:33:26.761443
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    import copy
    import sys

    from ansible.vars import VariableManager
    from ansible.playbook.play_context import PlayContext

    # Setup module_utils and ansible.module_utils.common
    class MockModuleUtils:
        def __init__(self):
            self.files = []

        def __getattr__(self, name):
            if name == "files" and not self.files:
                class MockFile:
                    def __init__(self, name):
                        self.name = name

                    def __call__(self, *args, **kwargs):
                        self.args = copy.copy(args)
                        self.kwargs = copy.copy(kwargs)

                        self.files.append(self)
                        return self


# Generated at 2022-06-13 09:33:33.312892
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    # Prepare a dummy TaskInclude object
    task_dummy = TaskInclude()
    # Prepare an apply argument
    apply_attrs = {}
    apply_attrs['block'] = []
    # Call the method with the apply argument
    p_block = task_dummy.build_parent_block()
    # Assert that a Block was created and that its parent is the TaskInclude object
    assert p_block._parent == task_dummy
    assert isinstance(p_block, Block)


# Generated at 2022-06-13 09:33:40.809274
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    # Create a simple task include
    task_include = TaskInclude(task_include=None, role=None, block=None)
    task_include.vars = dict()
    task_include.args = dict()

    # Set name, action, and tags for the task
    task_include.name = 'include tags'
    task_include.action = 'include'
    task_include.args['tags'] = ['test']

    # Test it!
    assert task_include.get_vars() == {'tags': ['test']}