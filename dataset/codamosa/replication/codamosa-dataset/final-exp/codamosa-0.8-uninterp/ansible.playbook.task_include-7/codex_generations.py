

# Generated at 2022-06-13 09:23:56.036336
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    # Helper method to create the TaskInclude instance
    def create_ti(data):
        ti = TaskInclude()
        return ti.check_options(ti.load_data(data), data)

    # Valid task attributes
    task = create_ti({'action': 'include', '_raw_params': 'example'})
    assert task.action == 'include', task.action
    assert task.args == {'_raw_params': 'example'}, task.args

    # Invalid task attributes raise an error
    data = {'action': 'include', '_raw_params': 'example', 'foo': 'bar'}
    try:
        create_ti(data)
    except AnsibleParserError as e:
        assert e.message == 'Invalid options for include: foo', e.message
    else:
        raise AssertionError

# Generated at 2022-06-13 09:24:11.408421
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    # These actions should be filtered
    actions_to_be_filtered = [
        'include', 'include_role', 'import_role', 'import_tasks',
        'include_tasks', 'import_playbook', 'include_playbook',
        'include_vars',
    ]

    # These actions should not be filtered
    actions_to_not_be_filtered = [
        'meta', 'runme'
    ]

    # These actions should error
    actions_to_error = [
        'include_vars',
    ]

    # Test dynamic include
    for action in actions_to_be_filtered:
        ti = TaskInclude(block=None, role=None, task_include=None)
        data = dict(action='include', file='blah')

# Generated at 2022-06-13 09:24:19.061780
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    from ansible.playbook.play_context import PlayContext

    ti = TaskInclude()
    ti._parent = PlayContext()
    ti._parent.vars = {'foo': 'bar'}

    ds = {'action': 'include', 'foo': 'bar', 'file': 'x.yml'}
    ds2 = ti.preprocess_data(ds)

    assert ds2 == {'action': 'include', 'file': 'x.yml', '_raw_params': 'x.yml'}



# Generated at 2022-06-13 09:24:29.131116
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    '''
    Test get_vars method of class TaskInclude
    '''
    task = TaskInclude()
    assert task.get_vars() == {}, "bad TaskInclude.get_vars()"

    # test with a TaskInclude with a parent. The parent has vars and args
    task_parent = Task()
    task_parent.vars = dict(a=1, b=2, c=3)
    task_parent.args = dict(d=4, e=5, f=6)
    task = TaskInclude(parent=task_parent)
    # for 'include' the vars and args of the parent are also included
    assert task.get_vars() == dict(a=1, b=2, c=3, d=4, e=5, f=6)

    # for

# Generated at 2022-06-13 09:24:34.766948
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    '''
    test_TaskInclude_check_options tests method 'check_options'
    of class 'TaskInclude'
    '''
    task = TaskInclude()

    # Test task with 'import_tasks' action and other arguments
    data = dict(action="import_tasks", file="main.yml", apply="test")
    task.check_options(task.load_data(data), data)

    # Test task with 'import_playbook' action and other arguments
    data = dict(action="import_playbook", file="main.yml", apply="test")
    task.check_options(task.load_data(data), data)

# Generated at 2022-06-13 09:24:42.742742
# Unit test for method load of class TaskInclude
def test_TaskInclude_load():
    data = {
        'action': 'include_role',
        'file': '/path/to/file',
        'apply': {},
    }

    a_block = object()
    a_role = object()
    a_ti = object()

    def load_data(data, variable_manager=None, loader=None):
        return data

    # For this test, we must overrid the load_data method to just return the input data.
    # Then, we can check that the only thing that was changed by the method
    # is the '_raw_params' arg.
    old_load_data = TaskInclude.load_data
    TaskInclude.load_data = load_data


# Generated at 2022-06-13 09:24:48.966347
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    ti = TaskInclude()
    ti.args['key1'] = 'value1'
    ti.args['key2'] = 'value2'
    ti.vars['key3'] = 'value3'
    ti_vars = ti.get_vars()
    assert 'key1' in ti_vars
    assert 'key2' in ti_vars
    assert 'key3' in ti_vars

# Generated at 2022-06-13 09:25:00.561137
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    '''
    Test TaskInclude.check_options
    '''
    from ansible.parsing.vault import VaultLib
    from ansible.playbook.play_context import PlayContext

    mock_VaultSecret = type('VaultSecret', (object,), {'load': lambda x, y=None: x})

    def mock_load_data(data, variable_manager=None, loader=None):
        loader.set_vault_secrets(dict())
        return TaskInclude(block=None, role=None, task_include=None).load_data(data, variable_manager=variable_manager, loader=loader)


# Generated at 2022-06-13 09:25:08.271698
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    parent_block = 'parent_block'
    ti = TaskInclude()
    ti._parent = parent_block
    ti.args = {
        'task_name': 'task_name',
        'apply': {
            'block': 'block',
            'sub1': 'sub1'
        },
        'sub2': 'sub2'
    }
    assert ti.build_parent_block() == parent_block

    ti.args = {
        'task_name': 'task_name',
        'sub1': 'sub1',
        'sub2': 'sub2'
    }
    assert ti.build_parent_block() == ti

# Generated at 2022-06-13 09:25:10.953053
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    task = Task()
    task.action = 'include_role'
    task.args = {'file': 'file_name'}

    ti = TaskInclude()
    task = ti.check_options(task, task.action)

    assert task.args['_raw_params'] == 'file_name'

# Generated at 2022-06-13 09:25:16.401934
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    pass
    # TODO: Add test for class TaskInclude and method build_parent_block

# Generated at 2022-06-13 09:25:18.993975
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    ti = TaskInclude()
    assert ti.get_vars() == {}, 'expected empty dict'

# Generated at 2022-06-13 09:25:31.449736
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    # Case 1: No args and no parents
    ti1 = TaskInclude(block=None, role=None, task_include=None)
    ti1.action = 'include'
    ti1.args = dict()
    ti1.args['include'] = 'some_task.yml'
    assert ti1.get_vars() == dict()

    # Case 2: Has args and no parents
    ti2 = TaskInclude(block=None, role=None, task_include=None)
    ti2.action = 'include'
    ti2.args = dict()
    ti2.args['include'] = 'some_task.yml'
    ti2.args['var1'] = 'val1'
    ti2.args['var2'] = 'val2'

# Generated at 2022-06-13 09:25:34.106174
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():

    task = TaskInclude.load(dict(action='include', args=dict(file='some_path', foo='bar')))

    all_vars = task.get_vars()

    assert isinstance(all_vars, dict)
    assert len(all_vars) == 1
    assert all_vars['foo'] == 'bar'

# Generated at 2022-06-13 09:25:44.890447
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    from ansible.playbook.play import Play
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task

    play = Play().load({
        'name': 'test',
        'hosts': 'localhost',
        'tasks': [
            {
                'include': 'include_file',
                'apply': {'block': []}
            }
        ]
    }, variable_manager={}, loader=None)
    block = play.tasks[0]
    task = block.block[0]

    assert isinstance(task, TaskInclude)
    assert isinstance(task.build_parent_block(), Block)

# Generated at 2022-06-13 09:25:54.131873
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    from ansible.playbook.play import Play

    p = Play().load({
        'name': 'myplay',
        'hosts': 'all',
        'gather_facts': False,
        'tasks': [
            {'include': 'roles/foo/tasks/bar.yml', 'when': 'uname == "debian"'}
        ]
    }, variable_manager=None, loader=None)
    # the play has a block, and the block has one task
    assert len(p.block) == 1
    assert isinstance(p.block[0], TaskInclude)
    # the task has a parent block
    assert p.block[0]._parent
    # and that block is the play
    assert p.block[0]._parent == p

    # test the TaskInclude's get_vars()

# Generated at 2022-06-13 09:26:00.174627
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    real_ds = dict(action='include_role', name='db', ignore_errors=True)
    real_ds = TaskInclude.preprocess_data(real_ds)
    assert 'name' in real_ds
    assert 'ignore_errors' in real_ds
    assert real_ds['name'] == 'db'
    assert real_ds['ignore_errors'] is True

    real_ds = dict(action='include_role', name='db', ignore_errors=True,
                   hello=42)
    real_ds = TaskInclude.preprocess_data(real_ds)
    assert 'name' in real_ds
    assert 'ignore_errors' in real_ds
    assert real_ds['name'] == 'db'
    assert real_ds['ignore_errors'] is True
    assert 'hello' not in real_ds



# Generated at 2022-06-13 09:26:06.542006
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    test = TaskInclude()
    test._parent = Block()
    test._parent.vars = {'k1': 'v1'}
    test.vars = {'k2': 'v2'}
    test.action = 'include'
    test.args = {'k3': 'v3'}
    assert test.get_vars() == {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}

    test.action = 'include_role'
    assert test.get_vars() == {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}

    test.action = 'import_playbook'

# Generated at 2022-06-13 09:26:15.366430
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    from ansible.playbook import Playbook
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.vars.manager import VariableManager

    # Ansible CLI does use file lookup plugin to load playbooks, so we will do the same in this unit test
    loader = 'file'

    # I'm going to be quite lazy and use the test/base_include.yml file as the input
    playbook_name = 'test/base_include.yml'
    play = Playbook.load(playbook_name, loader=loader)

    # Set up the VariableManager to be able to reference variables
    play_hosts = [host_name for host_name in play.hosts]
    play_variable_manager = VariableManager()

# Generated at 2022-06-13 09:26:25.308418
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    # create a task with options that must be rejected
    bad_opts = {
        "action": "include",
        "args": {
            "apply": "value",
            "bad_opt": "value"
        }
    }

    # make sure that 'bad_opt' is rejected
    try:
        task = TaskInclude(None, None, None)
        task.check_options(task.load(bad_opts), bad_opts)
        assert False, "'bad_opt' option should have been rejected."
    except AnsibleParserError:
        pass

    # make sure that 'apply' is accepted for an 'include' action
    task = TaskInclude(None, None, None)
    task = task.check_options(task.load(bad_opts), bad_opts)

# Generated at 2022-06-13 09:26:39.145166
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    class FakeBase:
        def __init__(self):
            self.fake_vars = {}
        def get_vars(self):
            return self.fake_vars

    ti = TaskInclude()

    ti._parent = FakeBase()
    ti._parent.fake_vars = {"parent_key": "parent_val"}
    ti.vars = {"self_key": "self_val"}

    ti.action = "include"

    ti.args = {"include_key": "include_val"}
    # get_vars should return the parent's vars and the include's args
    # but not the include's vars, since that's a different task
    assert ti.get_vars() == {"parent_key": "parent_val","include_key": "include_val"}


# Generated at 2022-06-13 09:26:42.940638
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    ti_instance = TaskInclude()
    ds = {'action': 'included_task'}
    result = ti_instance.preprocess_data(ds)
    assert result == ds

# Generated at 2022-06-13 09:26:54.093180
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    from ansible.playbook.play import Play
    from ansible.playbook.role.include import IncludeRole

    display = Display()
    play_context = dict()
    variable_manager = VariableManager()
    loader = DataLoader()
    play = Play().load({
        'name': 'any',
        'hosts': 'all',
        'gather_facts': 'no',
    }, variable_manager=variable_manager, loader=loader)


# Generated at 2022-06-13 09:27:04.559703
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    ti = TaskInclude()
    ti.action = 'include'
    ti.args['test_arg'] = 'test_value'
    ti.vars = {}
    assert ti.get_vars() == {'test_arg': 'test_value'}

    ti.action = 'include_role'
    assert ti.get_vars() == {'test_arg': 'test_value'}

    ti.action = 'import_role'
    assert ti.get_vars() == {}

    ti.action = 'import_tasks'
    assert ti.get_vars() == {}

    ti.args['tags'] = 'tag1'
    assert ti.get_vars() == {}

    ti.args['when'] = 'test_condition'
    assert ti.get_vars() == {}


# Generated at 2022-06-13 09:27:13.582770
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():

    # Empty apply_attrs
    task_attrs = dict(apply=dict(), block=dict(rescue=[], always=[]))
    task_block = TaskInclude.load(task_attrs)
    p_block = task_block.build_parent_block()
    assert p_block == task_block

    # apply_attrs with empty block
    task_attrs = dict(apply=dict(block=dict()), block=dict(rescue=[], always=[]))
    task_block = TaskInclude.load(task_attrs)
    p_block = task_block.build_parent_block()
    assert p_block != task_block
    assert isinstance(p_block, Block)
    assert p_block.block == p_block
    assert not p_block._parent
    assert not p_block._

# Generated at 2022-06-13 09:27:24.001195
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    task = TaskInclude()
    def _attr(attr):
        return FieldAttribute(
            parent=task, class_name='TaskInclude', name=attr,
            include_role=task._include_role,
            role=task._role,
            task_include=task,
            play=task._play,
            loader=task._loader,
            variable_manager=task._variable_manager,
            block=None,
        )


# Generated at 2022-06-13 09:27:38.246216
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    loader = DictDataLoader({
        "unit_test.yml": """
---
        - hosts: localhost
          gather_facts: False
          vars:
            var1: test1
          tasks:
            - import_tasks: unit_test_include.yml
              var2: test2
            - name: task2
              var3: test3
        """,
        "unit_test_include.yml": """
---
        - name: task1
          var4: test4
        """,
    })
    variable_manager = VariableManager()

# Generated at 2022-06-13 09:27:49.993913
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    task_include = TaskInclude()
    # validate valid args
    # skip static include only
    data = {'tasks': [{'include': 'main.yml', 'tags': 'test'}]}
    for action in C._ACTION_ALL_INCLUDE_ROLE_TASKS:
        task = Task()
        task.action = action
        task.args = {'file': 'test.yml', 'tags': 'test'}
        ti = task_include.check_options(task, data)
        assert 'tags' in ti.args
        assert 'test' in ti.args['tags']
        assert 'when' not in ti.args
        assert 'file' in ti.args['_raw_params']

        # with when
        task = Task()
        task.action = action

# Generated at 2022-06-13 09:27:57.466597
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    # Test 'include'
    ds = dict(
        name='foo',
        action='include',
        args=dict(one=1, two=2),
    )
    ti = TaskInclude.load(ds)
    assert ti.get_vars() == dict(one=1, two=2)
    # Test role
    ds = dict(
        name='foo',
        action='include_role',
        args=dict(one=1, two=2),
    )
    ti = TaskInclude.load(ds)
    assert ti.get_vars() == dict()
    # Test import
    ds = dict(
        name='foo',
        action='import_tasks',
        args=dict(one=1, two=2),
    )
    ti = TaskInclude.load(ds)

# Generated at 2022-06-13 09:28:05.564176
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    # test for 'include'
    ti_include = TaskInclude()
    ti_include.action = 'include'
    ti_include.vars = {'foo': 'bar'}
    ti_include.args = {'_raw_params': 'test/test_file.yml', 'a': 'b', 'c': 'd'}
    if ti_include.get_vars() != {'foo': 'bar', '_raw_params': 'test/test_file.yml', 'a': 'b', 'c': 'd'}:
        raise AssertionError

    # test for 'include_role'
    ti_include_role = TaskInclude()
    ti_include_role.action = 'include_role'
    ti_include_role.vars = {'foo': 'bar'}
    ti_

# Generated at 2022-06-13 09:28:21.977195
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    my_block = Block()
    my_block.vars = {'fruit': 'apple'}
    my_task = Task()
    my_task.vars = {'cat': 'garfield'}
    my_task._parent = my_block
    my_task.action = 'include'
    my_task.args = {'dog': 'odie', 'fruit': 'orange'}
    import collections
    my_task.vars = collections.chainMap({}, my_task.vars, my_task.args)
    assert my_task.get_vars() == {'fruit': 'orange', 'cat': 'garfield', 'dog': 'odie'}

# Generated at 2022-06-13 09:28:30.093856
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    from ansible.vars.manager import VariableManager
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    task_include = TaskInclude()
    task_include.vars = {'key1': 'value1'}
    task_include.args = {'key2': 'value2'}

    # Test case 1 (Playbook task):
    task_include.action = 'include'
    vars = task_include.get_vars()
    assert 'key1' in vars
    assert 'key2' in vars
    assert 'tags' not in vars
    assert 'when' not in vars
    assert vars['key1'] == 'value1'

# Generated at 2022-06-13 09:28:40.538844
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    # Test data
    data_1 = dict(
        apply=dict(
            block=dict(
                name='include_1_apply_block'
            )
        )
    )
    data_2 = dict(
        apply=dict(
            block=dict(
                name='include_2_apply_block'
            )
        )
    )
    data_3 = dict(
    )
    # Expected results
    block_0 = Block.load(
        dict(
            name='include_block'
        ),
        play=None,
        task_include=None,
        role=None,
        variable_manager=None,
        loader=None,
    )

# Generated at 2022-06-13 09:28:48.351107
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    from ansible.utils.vars import combine_vars

    testcases = dict()

    # Case 1: parent_block == None, and action not in C._ACTION_INCLUDE
    # Return empty dict
    testcases['case1a'] = dict(
        input=dict(
            args=dict(
                _raw_params='/some/include/file.yml',
                a='a',
                b='b'
                ),
            action='some_action',
            parent_block=None),
        expected=dict())

    # Case 2: parent_block is not None, and action not in C._ACTION_INCLUDE
    # Return combination of self.vars and parent_block.vars

# Generated at 2022-06-13 09:28:54.213595
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    test_class = TaskInclude()
    # Test with action=include
    task = Task()
    task.action = 'include'
    task.args = {'file': 'file1', 'other args': 'args1'}
    task = test_class.check_options(task, {})
    assert task.args['file'] == 'file1'
    assert 'other args' not in task.args
    assert task.args['_raw_params'] == 'file1'

    # Test with action=include_tasks
    task = Task()
    task.action = 'include_tasks'
    task.args = {'file': 'file1', 'other args': 'args1'}
    task = test_class.check_options(task, {})
    assert task.args['file'] == 'file1'

# Generated at 2022-06-13 09:29:04.087358
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    # Test 1:
    # Task is not 'include'
    TaskInclude.action = ''
    assert TaskInclude().get_vars() == {}

    # Test 2:
    # Task is 'include' and no other attrs are specified
    TaskInclude.action = 'include'
    TaskInclude.args = {}
    TaskInclude._parent = None
    TaskInclude.vars = {}
    assert TaskInclude().get_vars() == {}

    # Test 3:
    # Task is 'include' and other attrs are specified
    TaskInclude.action = 'include'
    TaskInclude.args = {'a': 1, 'b': 2}
    TaskInclude._parent = None
    TaskInclude.vars = {'c': 3}

# Generated at 2022-06-13 09:29:15.408276
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    from ansible.parsing.yaml.objects import AnsibleMapping
    ti = TaskInclude()
    ti.action = 'include'
    ti.vars = AnsibleMapping()
    ti.vars.update({'var1': 'value1'})
    ti.args = AnsibleMapping()
    ti.args.update({'arg1': 'value2'})
    ti.args.update({'arg2': 'value3'})
    assert(ti.get_vars() == {'var1': 'value1', 'arg1': 'value2', 'arg2': 'value3'})

# Generated at 2022-06-13 09:29:24.696874
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    from ansible.utils.vars import combine_vars

    data = {
        'action': 'include',
        'file': 'some_file.yml',
        'apply': 'some_apply.yml'
    }
    task = TaskInclude.load(data)
    assert task.args['apply'] == 'some_apply.yml'

    data = {
        'action': 'include_role',
        'file': 'some_file.yml',
        'apply': 'some_apply.yml'
    }
    task = TaskInclude.load(data)
    assert task.args['apply'] == 'some_apply.yml'


# Generated at 2022-06-13 09:29:31.897840
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    from ansible.playbook.play import Play
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task

    play_source =  dict(
        name = "Ansible Play",
        hosts = 'all',
        gather_facts = 'no',
        tasks = [
            dict(include="do_first"),
        ]
    )


# Generated at 2022-06-13 09:29:35.503817
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    # Test creation of the parent block with 'apply' configuration
    apply_config = {'block': 'test_block_apply'}
    task = TaskInclude()
    # Save the creation of the block in a variable to compare later
    expected_block = Block.load({'block': 'test_block_apply'})
    task.args['apply'] = apply_config
    assert task.build_parent_block() == expected_block
    # Check the deletion of the apply configuration from task.args
    assert 'apply' not in task.args
    # Test without the 'apply' configuration
    task.args['apply'] = None
    assert task.build_parent_block() == task


# Generated at 2022-06-13 09:29:59.629522
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    """
    Verify AnsibleTask.get_vars() method.
    """
    t = TaskInclude()
    t.action = 'include'
    t.args = dict(first="first-var", second="second-var", third="third-var")

    t._parent = Block()
    t._parent.vars = dict(parent_only1="parent_only1-var", parent_only2="parent_only2-var")
    t._parent._parent = Block()
    t._parent._parent.vars = dict(parent_parent_only="parent_parent_only-var")

    t.vars = dict(task_only1="task_only1-var", task_only2="task_only2-var")


# Generated at 2022-06-13 09:30:06.874391
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    task_include = TaskInclude()
    assert task_include.preprocess_data({
        'action': 'include_role',
        'file': 'some_file',
        'tasks': {},
        'handlers': {},
    }) == {
        'action': 'include_role',
        'file': 'some_file',
        'tasks': {},
        'handlers': {},
        '_raw_params': 'some_file',
    }


# Generated at 2022-06-13 09:30:13.213881
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    Block.datastructure_prefix = None
    Task.datastructure_prefix = None
    class TestVars1(object):
        def __init__(self, ds):
            self.vars = ds

    b1 = TestVars1({'a': 1, 'b': 2, 'c': 3})
    b2 = TestVars1({'a': 4, 'd': 5})
    b3 = TestVars1({'a': 6})

    b1.block = [b2, b3]

    b2.block = []
    b3.block = []
    b2._parent = b1
    b3._parent = b1

    b1.args = {'e': 7, 'f': 8}

# Generated at 2022-06-13 09:30:22.453936
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    display = Display()
    ti = TaskInclude()
    ti.action = 'include'
    ti.args = {'myvar': 'value'}
    ti.vars = {'othervar': 'anothervalue'}

    # This is the case the method should be tested for.
    result = ti.get_vars()

    display.display("Expected: %s" % {'othervar': 'anothervalue', 'myvar': 'value'})
    display.display("Result: %s" % result)

    if result == {'othervar': 'anothervalue', 'myvar': 'value'}:
        display.display("Test succeeded!")
    else:
        display.display("Test FAILED!")

# Generated at 2022-06-13 09:30:27.172151
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play

    variable_manager = VariableManager()
    loader = DataLoader()
    host = Host(name="test")
    group = Group(name="test")
    group.add_host(host)
    play = Play.load({}, variable_manager=variable_manager, loader=loader)
    block = Block(parent_block=play)
    task = TaskInclude()
    task._parent = block  # pylint: disable=protected-access
    task._role = "test"   # pylint: disable=protected-access
    task.name = "test"
   

# Generated at 2022-06-13 09:30:38.841551
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    '''
    Verify that the method TaskInclude.get_vars returns the expected dictionary
    '''
    t = TaskInclude()
    for action in C._ACTION_ALL_INCLUDE_ROLE_TASKS:
        t.action = action
        if action == 'include':
            # The result should contain the vars from the parent block
            t._parent = Block()
            t._parent.vars = dict(foo='bar')
            # The result should contain the task args
            t.args = dict(baz=42)
            # The result should not contain the "tags" and "when" args
            t.vars = dict(tags='always', when='yes', qux='quz')
            expected = dict(foo='bar', baz=42, qux='quz')

# Generated at 2022-06-13 09:30:48.268159
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():

    # We test preprocess_data() method when action is include_tasks or import_tasks
    for action in C._ACTION_INCLUDE_TASKS:
        data = dict(
            action=action,
            file=dict(a=1, b=2),
        )
        # We expect an exception for the file parameter
        try:
            ti = TaskInclude.load(data)
            ti.preprocess_data(data)
            assert(False)
        except AnsibleParserError:
            pass

        # The file parameter should be renamed _raw_params
        data = dict(
            action=action,
            file=dict(a=1, b=2),
        )
        ti = TaskInclude.load(data)
        ti.preprocess_data(data)

# Generated at 2022-06-13 09:30:56.869960
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    ti = TaskInclude()

    # No conversion if no 'include' in C.INVALID_TASK_ATTRIBUTE_FAILED
    try:
        C.INVALID_TASK_ATTRIBUTE_FAILED = ()
        ds = dict(action='include_role', name='myname', invalid_option='myoption')
        ti.preprocess_data(ds)
    except AnsibleParserError:
        assert False, 'Not expected to throw exception for invalid option'

    # Invalid option not included after preprocessing if 'include' in C.INVALID_TASK_ATTRIBUTE_FAILED
    C.INVALID_TASK_ATTRIBUTE_FAILED = ('include',)

# Generated at 2022-06-13 09:31:02.273967
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.block import Block

    def mock_get_vars(self):
        return {'hello': 'world'}

    def mock_copy(self, exclude_parent=False, exclude_tasks=False):
        return self

    TaskInclude._parent = 'parent'

    ti = TaskInclude(block=Block())
    ti.action = 'include'
    ti.get_vars = mock_get_vars.__get__(ti, TaskInclude)
    ti.args = {'this': 'that'}
    ti.copy = mock_copy.__get__(ti, TaskInclude)

    assert ti.get_vars() == {u'hello': u'world', u'this': u'that'}
   

# Generated at 2022-06-13 09:31:10.458762
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
        ti = TaskInclude()
        ti.args = {'debugger': 'a', 'tags': 'b'}
        task = ti.check_options(ti, {'debugger': 'a', 'tags': 'b'})
        assert task is ti
        assert ti.args == {'debugger': 'a'}

        ti = TaskInclude()
        ti.args = {'not_existent': 'a',}
        ti.action = 'include'
        try:
            task = ti.check_options(ti, {'not_existent': 'a',})
        except AnsibleParserError as e:
            assert str(e) == "Invalid options for include: not_existent"

        ti = TaskInclude()
        ti.args = {'debugger': 'a', 'tags': 'b'}

# Generated at 2022-06-13 09:31:38.077638
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.playbook.role_include import RoleInclude

    p_block = Block()
    p_block.vars.update({'x': 1})
    play_context = PlayContext()
    play_context.update(dict(x=2, y=3))
    play_context.set_task_and_variable_override(dict(x=3, z=4))
    play = Play().load({'name': 'play', 'connection': 'local', 'hosts': 'localhost', 'gather_facts': 'no'}, variable_manager=None, loader=None)
    play._play_context = play_context
    p_block._parent = play
    task_include = TaskInclude()
   

# Generated at 2022-06-13 09:31:39.108263
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    pass


# Generated at 2022-06-13 09:31:49.616556
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    _variable_manager = TaskQueueManager._variable_manager

    # test with action in C._ACTION_INCLUDE
    task_action = C._ACTION_INCLUDE[0]
    args = {'var1': 'value1'}
    vars = {'var2': 'value2'}

    task_params = {'action': task_action, 'args': args, 'vars': vars}

    play_context = PlayContext()
    play = Play().load(task_params, variable_manager=_variable_manager, loader=None)

# Generated at 2022-06-13 09:31:57.625736
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    def get_fake_ti(data):
        class FakeTaskInclude(TaskInclude):
            def __init__(self):
                self.action = 'include'
                self.args = {}
                self.parent = None
                self.name = ''
                self.tags = []
                self.when = []

            def check_options(self, task, data):
                super(FakeTaskInclude, self).check_options(task, data)
                return task

        return FakeTaskInclude()

    def get_fake_ti_action(action):
        class FakeTaskIncludeAction(TaskInclude):
            def __init__(self):
                self.action = action
                self.args = {}
                self.parent = None
                self.name = ''
                self.tags = []
                self.when = []


# Generated at 2022-06-13 09:32:05.814392
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    from collections import Mapping
    from ansible.playbook.attribute import FieldAttribute

    ti = TaskInclude()
    ti.action = 'include'
    task = Task()
    task.action = 'include'
    task.block = None
    task.role = None
    task.task_include = None
    task.args = dict()
    task.vars = dict()
    task.set_loader(None)

    # The following raises error, since 'action' is not a valid option
    # for 'include' tasks
    task.args['action'] = 'setup'
    try:
        ti.check_options(task, task)
    except AnsibleParserError as e:
        assert 'action' in str(e)

    # The following raises error, since 'debugger' is not a valid option for
    # 'include

# Generated at 2022-06-13 09:32:12.124698
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    from ansible.playbook.task import Task
    from ansible.playbook.role_include import IncludeRole
    test_incl_kwargs = {
        'action': 'include_role',
        '_raw_params': 'foo',
        'tasks': [],
        'file': 'foo.yml',
        'args': {
            'my_first_arg': 'bar',
            'my_second_arg': 'baz'
        }
    }

# Generated at 2022-06-13 09:32:16.946390
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    task = TaskInclude()
    apply_attrs={"when": "test", "loop": "test", "block": "test"}
    task.args['apply'] = apply_attrs
    p_block = task.build_parent_block()
    assert isinstance(p_block, Block)
    assert p_block.loop == apply_attrs['loop']
    assert p_block.when == apply_attrs['when']
    assert p_block.block == apply_attrs['block']

# Generated at 2022-06-13 09:32:26.874284
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    '''
    Test if it returns a parent block initialized with apply attributes
    '''
    with_apply = {
        'action': 'include',
        '_raw_params': 'test.yml',
        'apply': {
            'pause': 0,
        }
    }
    ti = TaskInclude.load(with_apply)
    p_block = ti.build_parent_block()
    expected = Block(pause=0, block=[], task_include=ti)
    assert p_block == expected

    no_apply = {
        'action': 'include',
        '_raw_params': 'test.yml',
    }
    ti = TaskInclude.load(no_apply)
    assert ti.build_parent_block() == ti

# Generated at 2022-06-13 09:32:36.658026
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    import ansible.playbook
    from ansible.playbook.play_context import PlayContext
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    tc = TaskInclude()
    tc._parent = ansible.playbook.Play()
    tc._parent._play = ansible.playbook.Play()
    tc._parent._play._context = PlayContext()
    tc._parent._play._variable_manager = VariableManager(loader=DataLoader())
    tc._role = None
    tc._variable_manager = tc._parent._play._variable_manager
    tc._loader = None

    # Example 1: no apply
    tc.args = {'_raw_params': None, 'file': 'name_file', 'action': 'include'}
    parent_block = tc

# Generated at 2022-06-13 09:32:48.559899
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    # import needed to run unit test
    import ansible.playbook.role_include as ri
    import ansible.playbook.play as play

    # create a dict that represents the task to be created
    task_data = {
       'apply': {
         'block': []
       }
    }

    # create the task object with our task_data
    task = TaskInclude.load(
        task_data,
        role=ri.RoleInclude.load(task_data, play=play.Play()),
    )

    # test returns a dictionary
    assert isinstance(task.build_parent_block().vars, dict)

# Generated at 2022-06-13 09:33:32.695821
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    from ansible.playbook.play import Play
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager

    ti = TaskInclude()
    ti._parent = Play().load(dict(name='test_play'))
    ti._role = None
    ti.vars = dict(test_var='test_value')
    ti.args = dict(apply=dict(tags=['test_tag'], when='test_task'))
    ti._variable_manager = VariableManager()

    p_block = ti.build_parent_block()
    assert isinstance(p_block, Block)
    assert isinstance(p_block._parent, Play)
    assert p_block.block  == []
    assert p_block.role == None
    assert p_block.tags == ['test_tag']
   

# Generated at 2022-06-13 09:33:42.805799
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    class _MockTask:
        def __init__(self, action):
            self.action = action
            self.args = {}

    class _MockTi:
        def __init__(self, action):
            self.action = action
            self.args = {}

    import pytest
    from ansible.errors import AnsibleParserError
    from ansible.parsing.yaml.objects import AnsibleUnicode

    ti = _MockTi('')
    task = _MockTask('')

    # empty dictionaries for task.args
    ti.check_options(task, '')

    # Adding a key that is not in the set of valid args
    task.args = {'somekey': ''}