

# Generated at 2022-06-13 09:23:47.622517
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    from ansible.playbook.play import Play

    pb = TaskInclude()
    pb.args = dict(
        apply=dict(
            block=[],
        ),
    )
    pb._variable_manager = 'fake_var_mgr'
    pb._loader = 'fake_loader'

    # No play so we should not pass the ``apply`` dict
    assert pb.build_parent_block() == pb
    # We should always pass a task_include
    assert pb.build_parent_block()._task_include == pb
    assert pb.build_parent_block()._role == pb._role
    assert pb.build_parent_block()._variable_manager == pb._variable_manager
    assert pb.build_parent_block()._loader == pb._loader

    #

# Generated at 2022-06-13 09:23:56.578361
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    from ansible.playbook.block import Block
    from ansible.playbook.task_include import TaskInclude
    import ansible.playbook.play
    import ansible.utils.display
    from ansible.plugins.loader import action_loader

    # Patch Display to display a warning
    def mock_display_warning(msg):
        print(msg)

    ansible.utils.display.Display.warning = mock_display_warning
    # Patch ActionLoader to return a dummy action
    def action_loader_mock(name, *args, **kwargs):
        def func_mock():
            pass

        class ActionModule:
            def __init__(self, *args, **kwargs):
                pass

            def run(self, *args, **kwargs):
                pass
        dummy_action = ActionModule()
        setattr

# Generated at 2022-06-13 09:24:06.144173
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    task_include = TaskInclude()
    task_include.action = 'include'
    task_include._parent = Block()
    task_include.vars = dict(a=1, b=2)
    task_include.args = dict(c=3, d=4)
    expected_result = dict(a=1, b=2, c=3, d=4)
    assert task_include.get_vars() == expected_result


# Generated at 2022-06-13 09:24:14.887452
# Unit test for method load of class TaskInclude
def test_TaskInclude_load():
    import ansible.utils.vars as vars_util
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    result = vars_util.TaskInclude.load({'_raw_params':'test_plugin.yml', 'a':'b'}, variable_manager=None, loader=None)

    # check class
    assert isinstance(result, vars_util.TaskInclude)

    # check parent class
    assert isinstance(result, Task)
    assert isinstance(result, AnsibleBaseYAMLObject)

    # check values
    assert result.action == 'include'
    assert result.args['_raw_params'] == 'test_plugin.yml'
    assert result.args['a'] == 'b'

# Generated at 2022-06-13 09:24:23.890001
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    my_task = TaskInclude()
    task_include_copy_dict = {'action': 'copy', 'args': {'src': '/home/src', 'dest':'/home/dest'}}
    task_include_copy = my_task.load(task_include_copy_dict, variable_manager=None, loader=None)

    # 1st test: args is not a dict
    task_include_copy.args = [1, 2, 3]
    with pytest.raises(AnsibleParserError) as excinfo:
        my_task.check_options(task_include_copy, task_include_copy_dict)
    assert 'Expected a dict for args' in str(excinfo.value)

    # 2nd test: bad args should raise an exception

# Generated at 2022-06-13 09:24:32.325550
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    # Create a fake task for the test
    task = Task()
    task.action = 'include'
    task.args = {
        'file': 'my_include.yml',
        'force': False
    }

    # Raise an error when invalid options are about to be set
    try:
        TaskInclude.check_options(task, {})
    except AnsibleParserError:
        pass

    # Raise an error when args is not a dict
    task.args = {}
    try:
        TaskInclude.check_options(task, {})
    except AnsibleParserError:
        pass

    # Raise an error when apply is defined with an invalid type
    task.args = {
        'file': 'my_include.yml',
        'apply': 'my_apply.yml',
    }

# Generated at 2022-06-13 09:24:36.788476
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    task_include = TaskInclude()
    ds = {'include': 'hello'}
    result = task_include.preprocess_data(ds)
    assert isinstance(result, dict)
    assert result['include'] == 'hello'

# Generated at 2022-06-13 09:24:47.568371
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    task_include = TaskInclude()
    task = {'action': 'include', 'file': 'file.yml'}
    valid_task = {'action': 'include', 'file': 'file.yml', '_raw_params': 'file.yml'}
    assert valid_task == task_include.preprocess_data(task)
    task = {'action': 'include', 'file': 'file.yml', 'unknown_key': True}
    valid_task = {'action': 'include', 'file': 'file.yml', '_raw_params': 'file.yml', 'unknown_key': True}
    assert valid_task == task_include.preprocess_data(task)
    task = {'action': 'include_role', 'name': 'myrole'}

# Generated at 2022-06-13 09:24:59.709528
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    task = TaskInclude()
    ds = {'name': 'bla', 'include': 'file.yaml', 'action': 'include', 'when': 'yes'}
    assert ds == task.preprocess_data(ds)
    ds = {'name': 'bla', 'include': 'file.yaml', 'action': 'include', 'when': 'yes', 'non_existent': 'yes'}
    assert 'non_existent' not in task.preprocess_data(ds)

    ds = {'name': 'bla', 'include_role': 'file.yaml', 'action': 'include_role', 'when': 'yes'}
    assert ds == task.preprocess_data(ds)

# Generated at 2022-06-13 09:25:06.358699
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    class MockTaskInclude(TaskInclude):
        _task_fields = ('action', 'args')

    # Check that the method returns an empty dict for the action ``include_tasks``
    # and only returns vars from the parent class for the action ``include_role``
    x = MockTaskInclude()
    for action in C._ACTION_ALL_INCLUDE_TASKS:
        x.action = action
        x.args = {}
        get_vars = x.get_vars()
        assert isinstance(get_vars, dict), "Expected dict, got %s" % type(get_vars)

        if action in C._ACTION_INCLUDE:
            assert len(get_vars) == 0, "Expected empty dict, got %s" % get_vars

# Generated at 2022-06-13 09:25:15.562943
# Unit test for method get_vars of class TaskInclude

# Generated at 2022-06-13 09:25:23.411801
# Unit test for method load of class TaskInclude
def test_TaskInclude_load():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.playbook import Playbook
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    import io
    from collections import namedtuple
    from ansible.playbook.block import Block

    # create dummy data

# Generated at 2022-06-13 09:25:33.719448
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    from ansible.playbook.play import Play
    from ansible.playbook.role_include import IncludeRole
    from ansible.playbook.task_include import TaskInclude


# Generated at 2022-06-13 09:25:46.007319
# Unit test for method load of class TaskInclude
def test_TaskInclude_load():
    """
    Unit test for method `load` of class `TaskInclude`.
    """
    # Check all valid keywords for 'include'

# Generated at 2022-06-13 09:25:55.130683
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    task_include = TaskInclude()
    task_include.vars = {'a': 'b'}
    task_include.args = {'c': 'd'}
    task_include.action = 'include_role'
    assert task_include.get_vars() == {'a': 'b', 'c': 'd'}
    task_include.action = 'include_tasks'
    assert task_include.get_vars() == {'a': 'b', 'c': 'd'}
    task_include.action = 'include'
    assert task_include.get_vars() == {'c': 'd'}
    task_include.action = 'import_playbook'
    assert task_include.get_vars() == {'a': 'b'}

# Generated at 2022-06-13 09:26:06.575007
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    task = TaskInclude.load_data({
        'meta': 'test_task_include_check_options',
        'action': 'include_tasks',
        'apply': {},  # 'apply' key is valid for 'include_tasks' and 'import_tasks'
        'debugger': True,
    }, variable_manager=None, loader=None)
    TaskInclude.check_options(task, task)

    task = TaskInclude.load_data({
        'meta': 'test_task_include_check_options',
        'action': 'include_role',
        'apply': {},  # 'apply' key is not valid for 'include_role'
        'debugger': True,
    }, variable_manager=None, loader=None)

# Generated at 2022-06-13 09:26:14.822251
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():

    data = dict(
        apply=dict(
            new_attr='new-attr',
            block=[]
        ),
        file='tests/test.yml',
        new_attr='new-attr'
    )

    data_action_include = dict(data.copy())
    data_action_include['action'] = 'include'

    data_action_import_tasks = dict(data.copy())
    data_action_import_tasks['action'] = 'import_tasks'

    data_action_include_role = dict(data.copy())
    data_action_include_role['action'] = 'include_role'

    data_action_import_role = dict(data.copy())
    data_action_import_role['action'] = 'import_role'


# Generated at 2022-06-13 09:26:17.177226
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    # TODO: implement the test for the method build_parent_block of class TaskInclude
    pass


# Generated at 2022-06-13 09:26:26.563324
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    ti = TaskInclude()
    ti.args = {
        'foo': 'test',
        'bar': 'test',
        'tags': ['test'],
        'when': 'test',
    }
    ti.action = 'include'
    ti.statically_loaded = False

    assert ti.get_vars() == {'foo': 'test', 'bar': 'test'}
    ti.action = 'include_role'

    assert ti.get_vars() == {'foo': 'test', 'bar': 'test', 'tags': ['test'], 'when': 'test'}
    ti.statically_loaded = True

    assert ti.get_vars() == {'foo': 'test', 'bar': 'test', 'tags': ['test'], 'when': 'test', 'name': 'include_role'}

# Generated at 2022-06-13 09:26:36.987638
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    def file_assign_test(file_arg, raw_params_arg):
        task = TaskInclude()
        assert file_arg
        assert raw_params_arg
        task_args = {'action': 'include',
                     'file': file_arg,
                     '_raw_params': raw_params_arg}
        task = task.check_options(task, task_args)
        assert task.args['file'] == file_arg
        assert task.args['_raw_params'] == raw_params_arg

    def raw_params_assign_test(file_arg, raw_params_arg):
        task = TaskInclude()
        assert file_arg
        assert raw_params_arg
        task_args = {'action': 'include',
                     '_raw_params': raw_params_arg}

# Generated at 2022-06-13 09:26:50.646065
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    from ansible.playbook import Play
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    # Creating some tasks, blocks and plays
    b1 = Block()
    b2 = Block()
    t1 = Task()
    t2 = Task()
    t3 = Task()
    ti1 = TaskInclude()

    # Setting the parents
    b1.set_parent(b2)
    b2.set_parent(t1)
    t1.set_parent(t3)
    t3.set_parent(ti1)

    # Setting the vars and args
    b1.vars = {'b1': 'b1'}
    b2.vars = {'b2': 'b2'}
    t1.vars

# Generated at 2022-06-13 09:27:00.580637
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    '''Unit test for method build_parent_block of class TaskInclude'''
    task_include = TaskInclude(block=None, role=None, task_include=None)
    task_include.action = 'include_tasks'
    task_include.statically_loaded = True
    task_include.args = dict(apply=dict(test='test_value'))
    parent_block = task_include.build_parent_block()

    assert parent_block.__class__.__name__ == 'Block'
    assert parent_block.parent == task_include
    assert parent_block.block == []
    assert parent_block.args['test'] == 'test_value'


# Generated at 2022-06-13 09:27:06.495804
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    playbook_path = '/etc/ansible/playbook.yml'
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources='/etc/ansible/hosts')
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    p_ti = PlayContext()


# Generated at 2022-06-13 09:27:15.072859
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager

    # Create a TaskInclude instance
    block = Block()
    task = TaskInclude(block)

    # Create the args for the TaskInclude instance
    task_args = dict()
    task_args['foo'] = 'bar'
    task_args['baz'] = 'faz'

    # Assign the args to the task
    task.vars = task_args

    # Create the task_vars for the VariableManager()
    task_vars = dict()
    task_vars['baz'] = 'buzz'
    task_vars['boo'] = 'far'

    # Create the variable manager
    variable_manager = VariableManager()
    variable_manager.set_nonpersistent_facts

# Generated at 2022-06-13 09:27:21.052569
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    # Create a simple task
    t1 = TaskInclude()
    assert t1.get_vars() == {}

    # Create a task with a parent
    t2 = TaskInclude()
    t2._parent = TaskInclude()
    t2._parent.vars = {'parent_var': 'val0'}
    t2.get_vars() == {'parent_var': 'val0'}

    # Create a task with a parent and args
    t3 = TaskInclude()
    t3.args = {'task_arg': 'val1'}
    t3._parent = TaskInclude()
    t3._parent.vars = {'parent_var': 'val0'}

# Generated at 2022-06-13 09:27:26.793909
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    # set up task
    # this is how _find_needle() returns data
    data = {
        'action': 'include_tasks',
        'loop_control': {'loop_var': 'ansible_distribution'},
        'name': '"Install {{ item }}"',
        'apply': {'when': 'inventory_hostname == "foohost"'},
        '_raw_params': 'test.yml',
    }

    TaskInclude.check_options(
        TaskInclude.load_data(data),
        data
    )

# Generated at 2022-06-13 09:27:37.742832
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    # Arrange
    apply_attrs = {'action': 'parent_block'}
    Block.LOADED_FROM = 'test_block'

    # Act
    ti = TaskInclude()
    ti.args = {'apply': apply_attrs}
    p_block = ti.build_parent_block()

    # Assert
    assert p_block.block, 'Expected: %s . Actual: %s' % (apply_attrs, p_block.block)
    assert p_block.action == 'parent_block'
    assert p_block.block[0] is ti, 'Expected: %s . Actual: %s' % (ti, p_block.block[0])

    # Cleanup
    del Block.LOADED_FROM

# Generated at 2022-06-13 09:27:42.601064
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    data = {
        'include': 'foo.yml'
    }
    data['vars'] = {
        'B': {
            'C': 2
        }
    }

    task = TaskInclude.load(data)
    assert task.get_vars() == {'B': {'C': 2}}


# Generated at 2022-06-13 09:27:58.071744
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.plugins.loader import action_loader
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    variable_manager = VariableManager()
    host_list = ['127.0.0.1', 'localhost']
    inventory = Inventory(loader=loader, variable_manager=variable_manager, host_list=host_list)


# Generated at 2022-06-13 09:28:05.860227
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    '''
    Unit test of method build_parent_block of class TaskInclude.
    '''

    t1 = TaskInclude()
    t1.action = 'include'
    t1.args = {'apply': {'tags': ['test1'], 'when': 'test2'}, 'loop': 'test3'}
    t1.set_loader(None)

    # This is what build_parent_block() should return
    p_block = Block(task_include=t1)
    p_block.role = None
    p_block.tags = ['test1']
    p_block.block = []
    p_block.when = 'test2'
    p_block.post_validate(templar=None, shared_loader_obj=None)

    p_block_result = t1.build_

# Generated at 2022-06-13 09:28:23.356588
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    # Just check if parent block is created
    task = TaskInclude()
    task.action = "include"
    task.args = {'apply': {'tags': ["tag1"]}}
    p_block = task.build_parent_block()
    assert p_block.block, "Block should exist"
    assert p_block.block[0].tags == ['tag1'], "Block should have tag1"

    # Check that parent block is not created
    task.args = {'tags': ['tag1']}
    p_block = task.build_parent_block()
    assert not p_block.block, "Block should not exist"

    # Check that parent block is not created
    task.args = {'apply': {'tag1': "tag1"}}
    p_block = task.build_parent_block()
   

# Generated at 2022-06-13 09:28:30.981345
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    '''
    TaskInclude: Testing get_vars method.
    '''
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.playbook.block import Block
    from ansible.playbook.role.definition import RoleDefinition

    play_context = PlayContext()
    play = Play.load({'hosts': 'hosts'}, variable_manager=None, loader=None)
    role = RoleDefinition.load(None, None, None)
    block = Block.load({}, play=play, task_include=None, role=role, variable_manager=None, loader=None)
    block.block  = [Task()]
   

# Generated at 2022-06-13 09:28:41.185538
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():

    # Arrange
    include_file_path = 'include_file.yml'
    include_task = TaskInclude(block=None, role=None, task_include=None)
    include_task.statically_loaded = True
    include_task.action = 'include'
    include_task.args['apply'] = True
    include_task.args['tags'] = 'tag_value_in_args'
    include_task.args['file'] = include_file_path
    include_task.vars = {'var_key': 'var_value_in_vars'}

    # Arrange
    parent_task = Task()
    parent_task.vars = {'parent_var_key': 'parent_var_value'}
    include_task._parent = parent_task

    # Act
    all_v

# Generated at 2022-06-13 09:28:48.860360
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    from ansible.playbook.play import Play
    from ansible.plugins.loader import loader

    class DummyTaskInclude(TaskInclude):
        pass

    class DummyBlock:
        def __init__(self):
            self._play = None
            self._parent = None
            self._vars_files = None
            self._role = None
            self._variable_manager = None
            self._loader = None
            self.vars = dict()
            self.args = dict()
            self.action = None
            self.name = 'apply'

    sut = DummyTaskInclude()

    # Case 1: empty apply (just to make sure the test works)
    apply_attrs = {}
    sut.args.pop('apply', None)
    sut.args['apply'] = apply_attrs
   

# Generated at 2022-06-13 09:28:54.686739
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    '''
    Since we do not have a loader in this test, we have to mock the types to use when creating the
    class fields.
    '''
    class Field(FieldAttribute):
        def __init__(self, default=None, fallback=(), type_func=None, always_post_validate=False):
            self._default = default
            self._fallback = fallback
            self._always_post_validate = always_post_validate
            if type_func is not None:
                self._type = type_func
            else:
                self._type = lambda x, v=None: x

            if not callable(self._type):
                raise ValueError('self._type must be a callable function/lambda')


# Generated at 2022-06-13 09:29:04.410208
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    task = TaskInclude()
    task.action = 'include'
    task.args = {'a': 'b'}
    # task's _parent is None. test will pass
    assert task.get_vars() == {'a': 'b'}

    role = Block()
    role.vars = {'role_var': 'role_val'}

    task = TaskInclude()
    task.action = 'include'
    task.args = {'a': 'b'}
    task._parent = role
    assert task.get_vars() == {'role_var': 'role_val', 'a': 'b'}

    task = TaskInclude()
    task.action = 'include_role'
    task.args = {'a': 'b'}
    task._parent = role

# Generated at 2022-06-13 09:29:15.268802
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    def _check_options(task, data, expected):
        '''
        Helper method used to exercise the method check_options of the TaskInclude class and
        verify the result
        '''
        task = TaskInclude.check_options(task, data)
        for k, v in expected.items():
            if isinstance(v, set):
                assert v == set(task.args.get(k))
            else:
                assert v == task.args.get(k)

    # User assigns a different file or _raw_params key
    task = TaskInclude()
    task.args = {
        # We use a set here so that the order doesn't matter
        'extra': set(['param1', 'param2']),
    }
    data = {'extra': 'foo'}

# Generated at 2022-06-13 09:29:24.532523
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    import ansible.playbook
    import ansible.playbook.play
    import ansible.playbook.role
    import ansible.playbook.task

    my_play = ansible.playbook.Play()
    my_play.vars.update({
        'var1': 'value1',
        'var2': 'value2',
        'var3': 'value3'
    })

    my_role = ansible.playbook.Role()
    my_role.vars.update({
        'rvar1': 'rvalue1',
        'rvar2': 'rvalue2'
    })

    my_include = ansible.playbook.TaskInclude()
    my_include._block = my_play
    my_include._role = my_role
    my_include.action = 'include'
    my

# Generated at 2022-06-13 09:29:31.766743
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    from ansible.playbook.play import Play
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins.loader import get_all_plugin_loaders

    loader = DataLoader()
    all_plugins = get_all_plugin_loaders()
    inventory = InventoryManager(loader=loader, sources=['localhost,'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    play_context = PlayContext()

# Generated at 2022-06-13 09:29:40.778669
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager

    task = TaskInclude(block=Block.load({'block': []}))
    role = RoleDefinition(
        'role',
        play_context=PlayContext(
            connection_lock=None,
            remote_addr='localhost',
            remote_user='root',
            become_method='sudo',
            verbosity=0,
            check_mode=False,
            diff=False,
            runtime=300),
        loader=None,
        variable_manager=VariableManager(),
        parent_role=None,
        task_blocks=[],
        _role_path=None,
        _dep_chain=None
    )
    task.set_loader

# Generated at 2022-06-13 09:30:04.114432
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    '''
    Tests method check_options of class TaskInclude
    '''

    def _data_from_action(action, data=None):
        if not data:
            data = {}
        data['action'] = action
        return data

    # Valid arguments for an include with apply:
    data = {
        'file': 'test.yml',
        'apply': {
            '_raw_params': 'test.yml',
            'block': [],
        },
    }

    assert TaskInclude.check_options(TaskInclude.load_data(_data_from_action('include')), _data_from_action('include')) == TaskInclude.load_data(_data_from_action('include'))

# Generated at 2022-06-13 09:30:10.295858
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.block import Block
    from ansible.playbook.play import Play
    from ansible.vars.manager import VariableManager
    from ansible.parsing.yaml.objects import AnsibleMapping
    from ansible.utils.sentinel import Sentinel
    from ansible.playbook.base import Base
    import ansible.plugins.loader as plugin_loader

    from ansible.plugins.loader import ModuleLoader
    from ansible.vars import VariableManager

    class MockBase(Base):
        def __init__(self):
            self.task_includes = []

    class MockPlay(Play):
        def __init__(self):
            self.blocks = []


# Generated at 2022-06-13 09:30:25.629200
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    # For test we need a task with a parent play
    attr = FieldAttribute(names=['test_attr'], private=True)
    attr.load(dict(a_test_attr='test_val'))
    task = Task()
    task.add_attribute(attr)
    play = Block()
    play.add_child(task)

    ti = TaskInclude(parent=play)
    ti.args = {'addr': '192.168.1.1', 'port': '4444'}
    ti.action = 'include'
    ti.name = 'test_task'
    ti.vars = {'a_local_var': 'local_val'}

    # We expect to get the vars from the parent block, the task and the args
    # without 'tags' and 'when'
    assert ti

# Generated at 2022-06-13 09:30:32.583821
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    '''
    Test for method get_vars() of class TaskInclude
    '''

    from ansible.playbook.play import Play

    from ansible.playbook.role_include import IncludeRole
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task


# Generated at 2022-06-13 09:30:42.628344
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.vars import VariableManager
    from ansible.utils.vars import load_extra_vars
    from ansible.parsing.dataloader import DataLoader
    import os
    import yaml
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

    ROLE_NAME = 'test-role'
    PLAY_NAME = 'test-play'
    PLAY_PATH = 'test-play-path'
    PLAYBOOK_NAME = 'test-playbook'
    PLAYBOOK_PATH = 'test-playbook-path'
    HOST_NAME = 'test-host'
    TAS

# Generated at 2022-06-13 09:30:52.980244
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    # Arrange
    playbook = ['---',
                '- hosts: all',
                '  gather_facts: false',
                '  tasks:',
                '    - include_tasks: test.yml',
                '      apply:',
                '        block:',
                '        - debug:',
                '            msg: "From the block"',
                '    - debug:',
                '        msg: "From the main file"']

    # Act
    loader, inventory, variable_manager = C.setup_loader()
    play = C.load_playbook(playbook, loader, variable_manager, inventory)
    play.post_validate(variable_manager, loader)

    # Assert
    assert len(play.block) == 2
    assert play.block[0].block

# Generated at 2022-06-13 09:31:04.359798
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task_include import TaskInclude
    from ansible.template import Templar

    task = TaskInclude(dict(action='include', args=dict(file='/tmp/testfile')))
    setattr(task, '_variable_manager', Templar(loader=None, variables=dict()))

    task_vars = task.get_vars()
    assert task_vars == dict(file='/tmp/testfile')

    task = TaskInclude(dict(action='import_playbook', args=dict(file='/tmp/testfile')))
    setattr(task, '_variable_manager', Templar(loader=None, variables=dict()))

    task_vars = task.get_vars()
    assert task_vars == dict

# Generated at 2022-06-13 09:31:15.236254
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    loader = DictDataLoader({
        "dir1/dir2/tasks.yaml": """
- name: task1
  include: task_include_file.yaml apply={"when": "foo==bar"}
""",
        "dir1/dir2/task_include_file.yaml": """
- name: task1_1
""",
    })
    inventory = Inventory(loader=loader, variable_manager=VariableManager())
    variable_manager = VariableManager()
    variable_manager.set_inventory(inventory)
    play_source =  dict(
            name = "Ansible Play",
            hosts = 'my_hosts',
            gather_facts = 'no',
            tasks = [
                dict(include=dict(file='dir1/dir2/tasks.yaml'))
            ]
        )


# Generated at 2022-06-13 09:31:21.759145
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager

    import os
    import yaml

    # Setup
    action = 'include_role'
    filename = os.path.join('test/sanity/code', action, 'main.yml')
    with open(filename, 'r') as stream:
        data = yaml.safe_load(stream)
    ti = TaskInclude()
    ti.action = action
    ti.vars = data.get('vars')
    ti.args = data.get('args')
    ti.static_loader = False
    ti.set_loader({})

    # Test
    pc = PlayContext()
    vm = VariableManager()
    ti.load()
    vm.set_known_hosts('localhost')
    result

# Generated at 2022-06-13 09:31:35.709030
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    from collections import namedtuple
    from ansible.playbook.taggable import Taggable
    from ansible.playbook.attribute import FieldAttribute
    from ansible.playbook.task_include import TaskInclude

    ti = TaskInclude()
    ti.action = 'include'
    ti.args = dict()

    # test valid file
    task = namedtuple('Task', ['args'])({'file': 'file.yml', '_raw_params': 'file.yml'})
    check_task = ti.check_options(task, 'include')
    assert check_task.args['file'] == 'file.yml'
    assert check_task.args['_raw_params'] == 'file.yml'

    # test valid _raw_params

# Generated at 2022-06-13 09:32:26.661460
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    # Test get_vars() of TaskInclude
    # Test case with include action
    task = TaskInclude()
    task.action = 'include'
    task.args = {'a': 1, 'b': 2}
    task.vars = {'c': 3, 'd': 4}
    _parent = Block()
    _parent.vars = {'e': 5, 'f': 6}
    task._parent = _parent
    assert task.get_vars() == {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}

    # Test case with import_tasks action
    task.action = 'import_tasks'

# Generated at 2022-06-13 09:32:32.811244
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():

    def get_vars_assert(task_action, inline_args, **args):
        pb = Block(parent_block=None)
        pb.vars.update(**args)
        ti = TaskInclude(pb, task_include=None)

        # Mock task_action and inline_args
        ti.action = task_action
        ti.args['_raw_params'] = ''.join(inline_args)

        # Test
        got = ti.get_vars()
        assert got == vars_values

    # Test get_vars in action = 'include' with inline_args
    vars_values = {'arg1': 'baz', 'arg2': 'qux'}
    inline_args = (' {arg1: baz} {arg2: qux}',)
    get_vars_

# Generated at 2022-06-13 09:32:40.415944
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    '''
    Unit test for method TaskInclude.get_vars
    '''
    from ansible.playbook.block import Block

    task_ds1 = {
        'args': {
            'foo': 'bar',
        },
        'action': 'include_some',
    }
    task1 = TaskInclude(block=Block(), task_include=None)
    task1.load_data(task_ds1)

    all_vars = task1.get_vars()

    task_ds2 = {
        'args': {
            'foo': 'bar',
        },
        'action': 'include_some_other',
    }
    task2 = TaskInclude(block=Block(), task_include=None)
    task2.load_data(task_ds2)

    all_vars_

# Generated at 2022-06-13 09:32:53.541079
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    task = TaskInclude()
    # check when action is 'include'
    data1 = {'action': 'include', 'file': 'a.yml', 'apply': {'a': 'b'}, 'when': False}
    task1 = task.check_options(task.load_data(data1), data1)
    assert isinstance(task1, TaskInclude)
    assert task1.action == 'include'
    assert task1.args['_raw_params'] == 'a.yml'
    assert task1.args['apply'] == {'a': 'b'}
    assert 'when' not in task1.args
    # check when action is 'include_with_items'
    # check invalid apply option

# Generated at 2022-06-13 09:33:08.273008
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():

    '''
    This method is to demonstrate that parent Block is created when 'apply' option
    is specified and that Block(parent=self) is returned when 'apply' is not specified.
    '''

    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.block import Block
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, variable_manager=variable_manager, sources=[])
    play_context = PlayContext(variable_manager=variable_manager)


# Generated at 2022-06-13 09:33:20.197212
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    from ansible.playbook.play import Play

    t = TaskInclude()

    # Invalid tasks must raise exception when invalid options are specified.
    for task_action in C.INVALID_TASK_ARGS_TASKS:
        with pytest.raises(AnsibleParserError):
            t.check_options({'_raw_params': 'file', 'action': task_action, 'args': 'blah', 'apply': 'blah'}, {'action': 'action', 'args': 'args', 'apply': 'apply'})


# Generated at 2022-06-13 09:33:26.329449
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    ti = TaskInclude()
    ti.add_block(Block())
    ti._parent = Task()
    ti._parent.add_block(Block())
    ti._parent.get_vars = lambda: {'foo': 'bar'}
    ti._parent._parent = Task()
    ti._parent._parent.add_block(Block())
    ti._parent._parent.get_vars = lambda: {'fooo': 'barr'}
    ti.vars = {'foooo': 'barrr'}
    ti.args = {'fooooo': 'bar'}
    ti.action = 'include'
    assert ti.get_vars() == {'foo': 'bar', 'fooo': 'barr', 'foooo': 'barrr', 'fooooo': 'bar'}

# Generated at 2022-06-13 09:33:36.976741
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    from ansible.playbook.role.include import RoleInclude
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.play import Play
    from ansible.playbook.role import Role
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.task_queue_manager import TaskQueueManager
    import json

    variable_manager = VariableManager()
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=[])