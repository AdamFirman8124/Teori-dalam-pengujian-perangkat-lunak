

# Generated at 2022-06-13 09:23:47.369339
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    from ansible.playbook.task import Task
    from ansible.parsing.yaml.loader import AnsibleLoader
    TaskInclude.VALID_ARGS = frozenset(('file', 'debugger', '_raw_params', 'hello'))
    TaskInclude.VALID_INCLUDE_KEYWORDS = frozenset(('action', 'file', 'debugger', '_raw_params', 'hello'))

    # No file specified at all, should raise AnsibleParserError
    ti = TaskInclude()
    ti.statically_loaded = True

    data = AnsibleLoader(None).load("""
---
- include:
""")[0]

# Generated at 2022-06-13 09:23:56.412865
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    class TestTaskInclude(TaskInclude):
        _ds = None

        def __init__(self, task_include=None):
            super(TestTaskInclude, self).__init__(task_include=task_include)

        def load_data(self, ds, variable_manager=None, loader=None):
            self._ds = ds
            return super(TestTaskInclude, self).load_data(ds, variable_manager=variable_manager, loader=loader)

    import ansible.plugins.loader

    original_get_all_plugin_loaders = ansible.plugins.loader.get_all_plugin_loaders
    original_vars_loader = None

    def _get_all_plugin_loaders():
        if original_vars_loader is None:
            original_vars_loader = original_get

# Generated at 2022-06-13 09:24:11.616704
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    task_include = TaskInclude.load({
        'action': 'include',
        'args': {
            'apply': {
                'name': 'Apply this',
                'tags': ['tag1', 'tag2'],
            },
        },
    })
    assert task_include.args == {'apply': {'name': 'Apply this', 'tags': ['tag1', 'tag2'], 'block': []}}
    assert task_include.args['apply']['block'] == []
    p_block = task_include.build_parent_block()
    assert task_include.args == {'apply': {'name': 'Apply this', 'tags': ['tag1', 'tag2'], 'block': []}}
    assert task_include.args['apply']['block'] == []

# Generated at 2022-06-13 09:24:18.382111
# Unit test for method load of class TaskInclude
def test_TaskInclude_load():
    import ansible.playbook
    import ansible.playbook.block
    import ansible.playbook.task

    tasks_dict_data = dict(
        name="include this",
        include=dict(
            file="common.yml",
            debug="{{ some_var }}",
            loop_with="{{ my_list }}",
        )
    )
    display = Display()
    t = ansible.playbook.task.Task.load(
            tasks_dict_data,
            block=ansible.playbook.block.Block(),
            role=None,
            variable_manager=None,
            loader=None,
        )
    assert isinstance(t, ansible.playbook.task_include.TaskInclude)
    assert t.name == tasks_dict_data['name']

# Generated at 2022-06-13 09:24:28.527066
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.utils.display import Display
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    loader = None
    variable_manager = VariableManager()
    inventory = InventoryManager()
    display = Display()
    role_def = RoleDefinition(loader=loader, play=None, collection_list=None, options={}, variable_manager=variable_manager,
                              loader_cache=None, display=display, inventory=inventory, default_vars={},
                              role_params={}, task_include=None, role=None, task_vars={})
    play = None
    block = [{"arg1": "val1"}, {"arg2": "val2"}, {"arg3": "val3"}]

# Generated at 2022-06-13 09:24:33.048187
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    import pytest
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    variable_manager = VariableManager()
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, variable_manager=variable_manager, host_list='localhost')
    variable_manager.set_inventory(inventory)

    # get_include_params
    ds = dict(action='include_tasks', one='1', two='2')
    ti = TaskInclude(block=None, role=None, task_include=None)
    ti_processed = ti.preprocess_data(ds)
    assert ti_processed.pop('action') == 'include_tasks'

# Generated at 2022-06-13 09:24:43.891389
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    ''' Test TaskInclude.get_vars(). Tested functions:
        - TaskInclude.get_vars()
        - Task.get_vars()
    '''
    # set up test data

# Generated at 2022-06-13 09:24:56.683269
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    task = TaskInclude()

    #
    # Test mode include_role
    #

    # Valid values
    ds = {
        'action': 'include_role',
        'name': "Test",
        'ignore_errors': True,
        'vars': {
            'foo': 'bar',
        },
        'tags': ['tag1', 'tag2'],
        'when': 'always',
    }
    ds = task.preprocess_data(ds)
    assert ds['ignore_errors'] is True
    assert ds['vars'] == {'foo': 'bar'}
    assert ds['tags'] == ['tag1', 'tag2']
    assert ds['when'] == 'always'

    # Invalid values

# Generated at 2022-06-13 09:25:07.268197
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    from ansible.playbook import Play
    from ansible.playbook.play import Play as Play_obj
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.task_include import TaskInclude as TaskInclude_obj
    from ansible.utils.vars import combine_vars

    mock_loader = Mock()
    mock_variable_manager = Mock()

    # Test case: includes/tasks/main.yml

# Generated at 2022-06-13 09:25:19.572824
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    def test_check_options(action, valid=True, apply_enabled=False, raw_params='test_file'):
        '''
        Helper method to test TaskInclude.check_options with different options
        '''
        data = {'action': action, 'args': {'_raw_params': raw_params}}
        if apply_enabled:
            data['args']['apply'] = {}

        if not valid:
            from ansible.errors import AnsibleParserError
            try:
                task = TaskInclude.load(data)
                assert False, 'No error raised for %s with apply' % action
            except AnsibleParserError as e:
                assert 'Invalid options' in str(e)

        task = TaskInclude.load(data)
        assert '_raw_params' in task.args
        assert task

# Generated at 2022-06-13 09:25:35.486956
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.vars import TaskVars
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play

    inventory = InventoryManager(loader=DataLoader(), sources='')
    variable_manager = VariableManager(loader=DataLoader(), inventory=inventory, version_info=PlaybookVersionInfo())
    variable_manager.set_inventory(inventory)

    ti = TaskInclude()
    ti.name = 'task_include'
    ti.action = 'include_role'
    ti.args = {'task_name': 'foo', 'debugger': True, 'args': {}}

# Generated at 2022-06-13 09:25:41.994597
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    """
       Unit test for method get_vars of class TaskInclude
    """
    # test case: valid action 'include'
    task_include = TaskInclude()
    task_include.action = 'include'
    task_include._parent = 'parent'
    task_include.vars = dict(a='a', b='b')
    task_include.args = dict(c='c', d='d')
    assert task_include.get_vars() == dict(a='a', b='b', c='c', d='d')

    # test case: valid action 'include_role'
    task_include = TaskInclude()
    task_include.action = 'include_role'
    task_include._parent = 'parent'
    task_include.vars = dict(a='a', b='b')
   

# Generated at 2022-06-13 09:25:52.155855
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    """
    Unit test for method ``build_parent_block`` of class ``TaskInclude``
    """
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.role import Role
    from ansible.playbook.role_include import IncludeRole
    from ansible.playbook.task_include import TaskInclude
    from ansible.vars.manager import VariableManager
    from ansible.vars.unsafe_proxy import UnsafeProxy
    from ansible.utils.vars import combine_vars

    context = PlayContext(play=None)
    context._prompt = {}
    context.become = True
    context.become_method = 'sudo'
    context.become_user = 'root'
    context.remote_addr = '127.0.0.1'
    context

# Generated at 2022-06-13 09:25:58.871940
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():

    from units.mock.loader import DictDataLoader
    from units.mock.path import mock_unfrackpath_noop

    # Create TaskInclude object
    ds = dict(
        include='foo.yml',
        vars=dict(
            var_foo=True,
            var_bar=True
        ),
        bar='foo'
    )
    task = TaskInclude.load(
        ds,
        loader=DictDataLoader({}),
        variable_manager=None,
        use_handlers=False
    )

    # Get vars for task include
    vars = task.get_vars()

    assert set(vars.keys()) == {'var_foo', 'var_bar', 'include', 'bar'}

# Generated at 2022-06-13 09:26:05.089382
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    # pylint: disable=unused-variable
    from ansible.playbook.play import Play

    my_block = Block()
    my_block.task_vars['foo'] = 'bar'
    my_block.vars = dict(one='1', two='2')
    my_block._parent = my_block

    my_task = TaskInclude(parent=my_block)
    my_task.vars = dict(three='3', four='4')
    my_task.args = dict(five='5', six='6')
    my_task.action = 'include'


# Generated at 2022-06-13 09:26:06.228918
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    pass


# Generated at 2022-06-13 09:26:15.113882
# Unit test for method load of class TaskInclude
def test_TaskInclude_load():
    '''
    Unit test for method load of class TaskInclude.
    '''
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.utils.sentinel import Sentinel
    from ansible.utils.display import Display
    import ansible.constants as C

    display = Display()
    display.verbosity = 3

    task = TaskInclude.load({'_raw_params': 'file', 'action': 'include'})
    assert isinstance(task, Task)
    assert isinstance(task, TaskInclude)
    assert isinstance(task, Block)
    assert task._role is None
    assert task._parent._play is None
    assert task.statically_loaded is False
    assert isinstance(task.vars, dict)

# Generated at 2022-06-13 09:26:20.727030
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.vars.reserved import RESERVED_VARS
    from ansible.plugins.loader import include_loader

    # Test with include action
    ti = TaskInclude(task_include=TaskInclude(task_include=TaskInclude()))
    ti.action = 'include'
    ti.args = dict(with_items=['1', '2'])
    ti.vars = dict(x=['a', 'b'])
    ti._loader = include_loader
    ti._block = Block(play=None)
    ti._block.vars = dict(y=['c', 'd'])
    ti._parent = ti._block
    ti._role = None
    ti._play

# Generated at 2022-06-13 09:26:28.665175
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    # Initialize parameters
    ds = dict(action='include_role', name='my_role', tasks_from='main')
    # Initialize test class
    ti = TaskInclude()
    ti.action = 'include_role'
    ti.vars = dict(my_var='my_value', my_var2=dict(my_var2_key='my_var2_value'))
    ti.args = dict(my_arg='my_arg_value', my_arg2=dict(my_arg2_key='my_arg2_value'))

    # Call get_vars method
    actual = ti.get_vars()

    # Verify test results

# Generated at 2022-06-13 09:26:36.819162
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    ti = TaskInclude({'include': 'vars.yml', 'tags': 'tag1,tag2'})
    # Test without parent Task()
    assert ti.get_vars() == {'include': 'vars.yml', 'tags': 'tag1,tag2'}

    # Test with parent Task()
    ti = TaskInclude({'include': 'vars.yml', 'tags': 'tag1,tag2'}, Block())
    ti._parent.vars = {'a':1}
    assert ti.get_vars() == {'a': 1, 'include': 'vars.yml', 'tags': 'tag1,tag2'}

# Generated at 2022-06-13 09:26:50.983848
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    # All fixtures are created in file test/units/test_tasks.py

    # build_parent_block() checks if apply is set, if yes it returns a Block.
    # apply is a Field attribute. This allows us to initialize apply by passing
    # a dictionary to the constructor of Field.
    # apply defaults to an empty dictionary.
    # apply is not a normal attribute of the TaskInclude class so we need to
    # create a class with a custom constructor that sets apply as a custom
    # attribute.
    class TaskIncludeWithApply(TaskInclude):
        apply = FieldAttribute(isa='dict')
        def __init__(self, block=None, role=None, task_include=None, apply=None):
            self.apply = apply

# Generated at 2022-06-13 09:27:00.819119
# Unit test for method load of class TaskInclude
def test_TaskInclude_load():
    from ansible.playbook.block import Block
    from ansible.playbook.play_context import PlayContext

    # Expected dict data
    test_data = {
        'file': 'test-vars-include.yml',
        'tags': ['test_include_tags'],
        'ignore_errors': True,
        'when': ['test_include_when'],
        'static': 2,
    }

    # Expected task dictionary
    task_data = dict(name='test-include', action='include', file='test-vars-include.yml')
    task_data.update(test_data)

    # Expected results
    task_args = dict()
    task_args.update(test_data)

# Generated at 2022-06-13 09:27:05.634699
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    '''
    Unit test for method check_options of class TaskInclude
    '''
    from ansible.vars.unsafe_proxy import wrap_var
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    dummy_loader = DataLoader()
    variable_manager = VariableManager()

    def _prepare_task(data):
        '''
        We need to wrap _raw_params and file in a function, so that we can reset the vars later
        '''
        if 'apply' in data:
            data['apply'] = wrap_var(data['apply'])
        if 'file' in data:
            data['file'] = wrap_var(data['file'])

# Generated at 2022-06-13 09:27:13.684449
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():

    from ansible.playbook.play import Play

    mytask = TaskInclude()
    assert mytask.get_vars() == {}, "Tasks with no args should return empty dict as vars"

    mytask.action = 'include'
    assert mytask.get_vars() == {}, "Include without parent should return empty dict as vars"

    mytask.action = 'include_role'
    assert mytask.get_vars() == {}, "Include without parent should return empty dict as vars"

    mytask.action = 'include'
    mytask._parent = Play()
    mytask.vars = {'foo': 'bar'}
    mytask.args = {'foo': 'bar'}

# Generated at 2022-06-13 09:27:22.187608
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    bo = Block.load({})
    task = TaskInclude.load({'apply': {'block': []}, '_raw_params': "test.yml"})
    p_block = task.build_parent_block()
    assert p_block.get_vars() == {}
    assert p_block.parent is None
    assert p_block.block is []

    bo = Block.load({})
    task = TaskInclude.load({'apply': {}, '_raw_params': "test.yml"})
    p_block = task.build_parent_block()
    assert p_block is task

# Generated at 2022-06-13 09:27:33.868497
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    # This method is used to create the parent block for the included tasks
    # when ``apply`` is specified
    dummy_include1 = TaskInclude()
    dummy_include1.action = 'include'
    dummy_include1._parent = object()
    dummy_include1._parent.get_vars = lambda: {'var_from_parent': True}
    dummy_include1.vars = {'var_from_self': True}
    dummy_include1.args = {'var_from_args': True}

    assert dummy_include1.get_vars() == {'var_from_parent': True,
                                         'var_from_self': True,
                                         'var_from_args': True}

    dummy_include2 = TaskInclude()
    dummy_include2.action = 'include_role'
    dummy

# Generated at 2022-06-13 09:27:42.318718
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    from ansible.playbook.task_include import TaskInclude
    # test case: correct options, some of them will be put into "args"
    task = TaskInclude.load({'include': {'file': 'file_path', 'ignore_errors': False}})
    if task.args.get('file') is not None:
        raise AssertionError("Should be None")
    if task.args.get('_raw_params') is None:
        raise AssertionError("Should not be None")
    if task.args.get('_raw_params') != 'file_path':
        raise AssertionError("Should be 'file_path'")
    if task.ignore_errors is not False:
        raise AssertionError("Should be False")

    # test case: invalid options

# Generated at 2022-06-13 09:27:57.784846
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    def _check_options(data):
        from ansible.playbook.block import Block
        from ansible.playbook.role.definition import RoleDefinition

        b = Block()
        r = RoleDefinition()
        task_include = TaskInclude(block=b, role=r)

        task = task_include.check_options(task_include.load_data(data), data)

        return task

    test_data = {
        'action': 'include',
        'file': '/path/to/include',
        'ignore_errors': True,
        'bad-option': True,
        'apply': {'name': 'apply-block'},
    }
    task = _check_options(test_data)

# Generated at 2022-06-13 09:28:05.728391
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    task = TaskInclude()
    my_arg_names = frozenset(['action', 'args', 'name', 'debugger', 'tags', 'when', 'register', 'ignore_errors', 'loop_with',
                              'loop', 'init_file', '_raw_params', '_flag_debug', 'apply', 'collections', 'loop_control',
                              'no_log', 'run_once', 'timeout', 'vars', 'args'])

    # Test 1: Empty args
    task = task.check_options(task, {})
    assert task.args == {}

    # Test 2: args with invalid keys

# Generated at 2022-06-13 09:28:16.872909
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    from ansible.playbook.play_context import PlayContext
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook import Play
    from ansible.playbook.block import Block
    variable_manager = VariableManager()
    loader = DataLoader()
    inventory = Inventory(loader=loader, variable_manager=variable_manager, host_list='/dev/null')
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    play_context = PlayContext()
    play = Play().load({}, variable_manager=variable_manager, loader=loader, play_context=play_context)
    block = Block()
    block._play = play
    block.role = None

    task_include = TaskIn

# Generated at 2022-06-13 09:28:28.464190
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    import ansible.playbook.play
    block_data = {'block': ['first_task', 'second_task']}
    p_block = Block.load(
                block_data,
                play=ansible.playbook.play.Play,
                task_include=None,
                role=None,
                variable_manager=None,
                loader=None,
            )
    assert p_block._entries == ['first_task', 'second_task']


# Generated at 2022-06-13 09:28:38.678512
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    task = TaskInclude.load({
        'apply': {
            'when': ['unix'],
            'become': True,
            'become_user': 'root',
            'block': [],
        },
        '_raw_params': 'unix.yml',
    })

    assert task.args['apply']['become'] is True
    assert task.args['apply']['become_user'] == 'root'

    # build_parent_block() should remove apply from task.args
    parent_block = task.build_parent_block()
    assert 'apply' not in task.args

    assert isinstance(parent_block, Block)
    assert parent_block.become is True
    assert parent_block.become_user == 'root'

# Generated at 2022-06-13 09:28:46.738299
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    '''
    Test get_vars of TaskInclude.
    '''
    TaskInclude._match_hostname = lambda self, hostname: True

    # define common test variables
    fake_loader = DummyLoader()
    fake_play = DummyPlay()
    fake_play.variable_manager = DummyVariableManager()
    fake_play.variable_manager._extra_vars = dict()
    fake_play.variable_manager.extra_vars = dict()
    fake_play._included_file_local_search_paths = []
    fake_play.included_file_local_search_paths = []

    # define values for testing TaskInclude.get_vars()
    # Note that we can't really use the real tasks.include
    # here as it will attempt to actually load the includes
    test_

# Generated at 2022-06-13 09:28:53.155900
# Unit test for method load of class TaskInclude
def test_TaskInclude_load():
    # Setup
    task = {
        'include': 'statictasks.yml',
        'args': {
            'action': 'include',
            'apply': {
                'tags': ['task_include_test', 'task_include_delegate_test'],
            },
        }
    }

    ti = TaskInclude()
    ti.VALID_ARGS = frozenset(['file', 'copy', 'delegate_to', 'register'])
    ti.BASE = frozenset(['file', 'copy', 'delegate_to', 'register'])

# Generated at 2022-06-13 09:29:00.030819
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    # create inner task
    inner_task = Task()
    inner_task.vars = dict(x=1)
    # create outer task
    outer_task = TaskInclude(task_include=inner_task)
    outer_task.action = 'include'
    outer_task.vars = dict(y=2)
    outer_task.args = dict(x=3, z=4)
    assert outer_task.get_vars() == dict(x=3, y=2, z=4)

# Generated at 2022-06-13 09:29:09.773217
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():

    task_data = {
        'action': 'include',
        'args': {
            'file': 'some-file'
        },
        'ignore_errors': True,
    }

    fake_block = 'fake-block'

    ti = TaskInclude(block=fake_block)

    task = ti.check_options(ti.load_data(task_data))

    assert task.action == task_data['action']
    assert task.ignore_errors == task_data['ignore_errors']
    assert task.args['_raw_params'] == task_data['args']['file']

# Generated at 2022-06-13 09:29:17.648420
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    from ansible.playbook.play import Play

    t_block = Block()
    t_block.vars = dict()
    t_block.vars = {'foo': 'bar'}
    t_block.args = dict()
    t_block.args = {'_raw_params': 'somefile'}

    t_include = TaskInclude(t_block)
    t_include.vars = dict()
    t_include.vars = {'baz': 'boo'}

    t_play = Play()
    t_play.vars = dict()
    t_play.vars = {'top': 'level'}
    t_block.set_parent(t_play)

    list_vars = dict()
    list_vars = t_include.get_vars()

# Generated at 2022-06-13 09:29:26.641322
# Unit test for method load of class TaskInclude
def test_TaskInclude_load():
    play = dict(
        name = "Ansible Play",
        hosts = 'localhost',
        gather_facts = 'no',
        tasks = [
            dict(action=dict(include="{{ lookup('file','test.yml') }}", args=dict(a="b")))
        ]
    )
    from ansible.playbook import Play
    import ansible.inventory
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.utils.display import Display
    from ansible.plugins.loader import action_loader
    from ansible.plugins.loader import module_loader

    display = Display()
    options = dict(
        connect_timeout=10,
    )

# Generated at 2022-06-13 09:29:33.071322
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    # Include should add include args as vars
    t = TaskInclude()
    t.block = Block(play=None, parent_block=None, role=None)
    t.action = 'include'
    t.args = dict(x=1, y=2, z=3)
    t._parent = None
    t.vars = dict()
    assert t.get_vars() == dict(x=1, y=2, z=3)
    # Include should not add include args as vars if parent is present
    t2 = TaskInclude()
    t2.block = Block(play=None, parent_block=None, role=None)
    t2.action = 'include'
    t2.args = dict(x=1, y=2, z=3)
    t2._parent = t
   

# Generated at 2022-06-13 09:29:38.160966
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.play import Play
    from ansible.playbook import Playbook
    from ansible.vars.manager import VariableManager
    from ansible.inventory import Inventory
    from ansible.parsing.dataloader import DataLoader

    # Setup
    dl = DataLoader()
    inventory = Inventory(loader=dl, variable_manager=VariableManager(), host_list=['localhost', 'otherhost'])

    ti = TaskInclude()

    block_args = dict()
    block = Block.load(block_args, play=Play(), task_include=Task(), role=None, variable_manager=None, loader=dl)


# Generated at 2022-06-13 09:30:01.152064
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    # Arguments for play and its context
    play_ds = dict()
    play_context = PlayContext()

    # Arguments for play's variable manager
    vars_loader = DataLoader()

    # Arguments for TaskInclude's self.load_data
    ti_ds = dict()
    role = None
    block = None

    # Inclusion of static import tasks do not require (file, _raw_params)
    static_import_tasks = ('import_playbook', 'import_tasks')

# Generated at 2022-06-13 09:30:08.895218
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    # Case 1. Valid args
    yaml_data = """
    - include: file_included.yml
      loop: "{{ list_of_items }}"
      apply:
        ignore_errors: True
    """
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=['localhost'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    task = TaskInclude.load(yaml_data, variable_manager=variable_manager, loader=loader)
    assert task.statically_loaded == False
    assert task.args['_raw_params'] == 'file_included.yml'
   

# Generated at 2022-06-13 09:30:15.062635
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    t = TaskInclude()
    t.vars = dict(one=1,two=2,three=3)
    t.args = dict(four=4,five=5)
    assert t.get_vars() == dict(one=1,two=2,three=3,four=4,five=5)

# Generated at 2022-06-13 09:30:28.728898
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    # Test class TaskInclude get_vars.
    # Test without apply with self.action in not in C._ACTION_INCLUDE
    ti = TaskInclude()
    ti.action = 'include'

    assert(ti._parent is None)
    assert(ti.vars == {})
    assert(ti.args == {})

    assert(ti.get_vars() == {})

    # Test with self.action in not in C._ACTION_INCLUDE
    ti = TaskInclude()
    ti.action = 'include'
    ti._parent = TaskInclude()
    ti._parent.get_vars = lambda: {'a': 'foo', 'c': 'bar'}
    ti.vars = {'b': 'foo'}
    ti.args = {'d': 'foo'}

   

# Generated at 2022-06-13 09:30:40.119404
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    import ansible.playbook.play_context as play_context
    import ansible.playbook.play as play
    import random
    from ansible.inventory import Inventory
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader

    yaml_data = """
    - name: test include
      hosts: localhost
      tasks:
        - include: test.yml
          vars:
              foo: bar
          apply:
              when: 1
              block:
                - debug: msg="this is the block"
                  tags:
                    - test
    """
    # Setting up fake objects for the TaskInclude object.
    p = play.Play().load(yaml_data, variable_manager=VariableManager(), loader=DataLoader())
    i = Inventory("localhost")
   

# Generated at 2022-06-13 09:30:48.965462
# Unit test for method load of class TaskInclude
def test_TaskInclude_load():
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.plugins.loader import action_loader
    from ansible.parsing.dataloader import DataLoader

    context = PlayContext()

    variable_manager = VariableManager()
    loader = DataLoader()
    variable_manager.set_loader(loader)

    test_include = '''
- include: playbook.yml
  apply:
    name: "task block name"
    tags: tag1
    when: x is y
'''

    def task_loader(name, task, block=None, role=None, task_include=None, play_context=None, loader=None, variable_manager=None, **kwargs):
        if name == 'include':
            action = action_loader.get

# Generated at 2022-06-13 09:30:57.273762
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    # The method is tested in a loop. The scores are updated with the number of
    # failed tests per loop
    scores = [0, 0, 0]
    for tests in range(3):
        for i in range(3):
            task_include = TaskInclude()
            if tests == 0:
                task_include.action = C._ACTION_INCLUDE[0]
            elif tests == 1:
                task_include.action = C._ACTION_INCLUDE_ROLE[0]
            else:
                task_include.action = C._ACTION_IMPORT_ROLE[0]

            task_include.vars = dict(
                a=1,
                b=2,
                c=3
            )


# Generated at 2022-06-13 09:31:02.548327
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    from ansible.playbook.play import Play
    from ansible.playbook.role import Role
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor

    # Create a fake task with apply dict as a dict with 'block' key
    # This mirrors the task that would be created in Ansible 2.1.0.0
    task = {"action": "include", "apply": {"block": [], "name": "engine_configuration", "when": "app_engine_configuration_needed"}}

    # Create a fake role

# Generated at 2022-06-13 09:31:10.655775
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.playbook import Playbook
    from ansible.playbook.play_iterator import PlayIterator
    import ansible.playbook.included_file as included_file
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.handler import Handler

    vars_dict = dict(
        foo='bar',
        bam='boom',
        current_file='main.yml',
    )
    vars_manager = FakeVarsManager(vars_dict)
    config = FakeConfig()
    loader = FakeLoader(vars_dict)
    play_context = PlayContext()
    play = FakePlay(vars_manager, loader, play_context, config)


# Generated at 2022-06-13 09:31:13.229995
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    test_task = TaskInclude()
    assert test_task.build_parent_block() == test_task


# Generated at 2022-06-13 09:31:50.394385
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    task = TaskInclude()
    # test check_options with no file
    options = {'debugger': 'on'}
    data = {'action': 'include_role'}
    with pytest.raises(AnsibleParserError):
        task.check_options(task.load_data(data, options), data)
    # test check_options with no action
    options = {'file': 'test.yml'}
    data = {}
    task.check_options(task.load_data(data, options), data)

# Generated at 2022-06-13 09:31:58.212750
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook import Play
    from ansible.playbook.block import Block

    test_data = {'action': 'include', 'file': 'test.yml'}

    # check for bad options for include. Should raise exception
    test_task = TaskInclude()
    test_task.args = test_data
    test_task = task_check_options(test_task)

    test_task = TaskInclude()
    test_task.args = test_data.copy()
    test_task.action = 'import_playbook'
    test_task = task_check_options(test_task)

    # check for bad options for import_playbook. Should raise exception
    test_task = TaskInclude()
    test_task.args = test

# Generated at 2022-06-13 09:31:59.869239
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():  # pylint: disable=invalid-name
    pass  # TODO: Write unit test


# Generated at 2022-06-13 09:32:08.017684
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    # Setup
    playbook_data = {
        'name': 'test playbook',
        'hosts': 'localhost',
        'gather_facts': 'no',
        'roles': [
            {
                'name': 'test_role',
                'tasks': [
                    {
                        'name': 'test task',
                        'include': 'include_file.yml',
                        'apply': {
                            'block': []
                        }
                    }
                ]
            }
        ]
    }

    ti = TaskInclude()
    block_mock =  {
        'name': 'test task',
        'include': 'include_file.yml',
        'apply': {
            'block': []
        }
    }
    ti.block = block_mock

# Generated at 2022-06-13 09:32:15.856184
# Unit test for method load of class TaskInclude
def test_TaskInclude_load():
    from ansible.playbook.block import Block
    from ansible.playbook.play import Play
    from ansible.playbook.role import Role
    from ansible.playbook.task import Task
    from ansible.playbook.role.include import IncludeRole
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.vars import combine_vars
    from ansible.config.manager import ConfigManager
    from ansible.inventory.manager import InventoryManager
    from ansible.utils.sentinel import Sentinel
    from ansible.context import context
    from io import StringIO

    context.CLIARGS = lambda: {'module_path': 'fake_module_path'}


# Generated at 2022-06-13 09:32:26.313704
# Unit test for method load of class TaskInclude
def test_TaskInclude_load():
    from ansible.playbook.role_include import RoleInclude
    from ansible.playbook.block import Block
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.handler_task_include import HandlerTaskInclude
    from ansible.playbook.helpers import load_list_of_blocks

    '''
    tests:
    1. validate_options
    2. check_options
    3. preprocess_data
    4. copy
    5. get_vars
    6. build_parent_block
    '''

    # case 1: no options
    try:
        TaskInclude.load({'action':'include_tasks'})
    except Exception as e:
        assert e.message == 'No file specified for include_tasks'
    # all other tests
   

# Generated at 2022-06-13 09:32:32.483989
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    import ansible.playbook
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.block import Block
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    import ansible.constants as C

    loader = DataLoader()
    variable_manager = VariableManager()

    task_include = TaskInclude.load(dict(
        apply=dict(
            load_vars=dict(
                key1='val1',
                key2='val2',
            ),
            when='False',
        ),
        action='include',
        file='test.yml',
        key3='val3',
    ), VariableManager=variable_manager, loader=loader)


# Generated at 2022-06-13 09:32:38.576909
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    from ansible.playbook.block import Block
    from ansible.playbook.play import Play
    from ansible.playbook.task_include import TaskInclude
    from ansible.template import Templar

    # reset
    display.verbosity = 3

    ################################################################################
    #                           base attributes
    ################################################################################
    # fake play context
    fake_pb = Play()
    fake_pb._role_blocks = []
    fake_pb._play_ds = dict(
        name="fake",
    )

    # fake base task ds
    task_ds = dict(
        name='fake_task',
        action='include',
        ignore_errors=True,
        apply=dict(
            block=[]
        )
    )

    ################################################################################
    #                           test data

# Generated at 2022-06-13 09:32:52.701432
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    from ansible.playbook.play import Play
    from ansible.playbook.role import Role
    from ansible.playbook.task import Task

    play_ds = dict(
        name="Ansible Play",
        hosts='all',
        gather_facts='no',
        tasks=[
            dict(action='include', args=dict(file='/path/to/included/file.yml', tags='tag1'))
        ]
    )

    play = Play().load(play_ds, variable_manager=None, loader=None)
    role = Role()
    task = Task().load(play_ds['tasks'][0], block=play, role=role, task_include=None, variable_manager=None, loader=None)


# Generated at 2022-06-13 09:33:07.266045
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    task = TaskInclude()

    simple_data = { 'include' : 'foo.yml' }
    assert simple_data == task.preprocess_data(simple_data)

    simple_data = { 'include' : 'foo.yml', 'tags' : ['tag1'] }
    assert simple_data == task.preprocess_data(simple_data)

    simple_data = { 'include' : 'foo.yml', 'tags' : ['tag1', 'tag2'] }
    assert simple_data == task.preprocess_data(simple_data)

    simple_data = { 'include' : 'foo.yml', 'with_items' : 'bar' }
    expected_data = { 'include' : 'foo.yml' }
    assert expected_data == task.preprocess_data(simple_data)

