

# Generated at 2022-06-13 09:23:47.970229
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    class Fake_Block(object):
        class Fake_Parent(object):
            def get_vars(self):
                return {"a": 1}
        def get_vars(self):
            return {"b": 1}
        parent = Fake_Parent()
    class Fake_Task(object):
        args = {"a": 1}
        vars = {"b": 1}
        _parent = Fake_Block()
    assert TaskInclude.get_vars(Fake_Task()) == {"a": 1, "b": 1}

# Generated at 2022-06-13 09:23:56.800276
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():

    from ansible.playbook.play import Play
    from ansible.playbook.role_include import IncludeRole
    from ansible.playbook.role_task import Task as RoleTask

    p = Play()
    ir = IncludeRole()
    ir.load({'name': 'foo'}, p)

    data = {'action': 'include_tasks',
            'file': '/path/to/tasks.yml',
            'apply': {
                'tags': 'tag1',
                'when': 'ansible_os_family == "RedHat"',
                'block': [
                    {
                        'action': 'foo',
                        'tags': 'tag2',
                        'when': 'ansible_os_family == "Debian"'
                    },
                ]
            }}

    ti = TaskInclude()
    ti.args

# Generated at 2022-06-13 09:24:11.956360
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    '''
    This test checks TaskInclude.preprocess_data() against various cases.
    It does not cover cases for C._ACTION_INCLUDE_TASKS, since each of those
    cases is checked in its respective method.
    '''
    from ansible.playbook.role_include import RoleInclude
    from ansible.playbook.handler_task_include import HandlerTaskInclude

    def _load_data(data, action='include', task_include_class=TaskInclude):
        ti = task_include_class(action=action)
        task = ti.check_options(
            ti.load_data(data),
            data
        )
        task = ti.preprocess_data(task)

        return task

    # Static Cases
    # shows that we don't modify anything if action is 'include' and we

# Generated at 2022-06-13 09:24:21.850951
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    ti = TaskInclude()

    # valid args
    data = dict(
        _raw_params = 'tasks/foo.yml',
    )
    task = ti.load_data(data)
    task = ti.check_options(task, data)

    data = dict(
        file = 'tasks/foo.yml',
    )
    task = ti.load_data(data)
    task = ti.check_options(task, data)
    assert task.args['_raw_params'] == 'tasks/foo.yml'

    data = dict(
        _raw_params = 'tasks/foo.yml',
        apply = dict(),
    )
    task = ti.load_data(data)
    task = ti.check_options(task, data)
    assert task.args['apply']

# Generated at 2022-06-13 09:24:32.362926
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    # Parametrized test to check that errors are thrown for the given arguments and no errors for the others
    vars_param = {'key1': 'value1', 'key2': 'value2'}

    # Empty task that includes file
    base_task = { 'action': 'include', 'args': {'file': 'file_name' } }

    # Task that includes file with an apply
    task_with_apply = {'action': 'include', 'args': {'file': 'file_name', 'apply': { } } }

    # Task that includes file with a non-empty apply
    task_with_non_empty_apply = {'action': 'include', 'args': {'file': 'file_name', 'apply': { 'key1': 'value1' } } }

    # Task that includes file with some other option
   

# Generated at 2022-06-13 09:24:43.721683
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    display = Display()
    display.verbosity = 3

    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, sources=['local_hosts'])
    variable_manager.set_inventory(inventory)

    play_context = PlayContext()


# Generated at 2022-06-13 09:24:56.501759
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    from ansible.playbook.task import Task
    import ansible.constants as C
    # Test without include
    task = Task.load({'name': 'Test Task', 'action': 'shell', 'args': {'creates': '/home/user.txt'}})
    assert task.get_vars() == {}

    # Test with include
    task = Task.load({'include': 'other.yml', 'action': 'include'})
    assert task.get_vars() == {}

    # Test with include + args
    task = Task.load({'include': 'other.yml', 'action': 'include', 'args': {'tags': ['x'], 'args': {'a': 1}}})
    assert task.get_vars() == {'a': 1}

    # Test with include + vars
   

# Generated at 2022-06-13 09:25:00.479306
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    task = TaskInclude()
    ds = {'action': 'include', 'unknown_var': 1}
    ds = task.preprocess_data(ds)
    assert ds.get('unknown_var', False) is False

# Generated at 2022-06-13 09:25:09.936317
# Unit test for method load of class TaskInclude
def test_TaskInclude_load():
    import pytest
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.role import Role
    from ansible.errors import AnsibleParserError
    from .test_conditional import load_fixture

    # test load() raises AnsibleParserError on invalid action
    data = {'action': 'bad_module_name'}
    data.update(load_fixture('include_vars'))
    with pytest.raises(AnsibleParserError):
        TaskInclude.load(data)

    # test load() raises AnsibleParserError on invalid keyword
    data = {'action': 'include'}
    with pytest.raises(AnsibleParserError):
        TaskInclude.load(data)

    # test load() returns a TaskInclude object
    block1 = Role()

# Generated at 2022-06-13 09:25:15.202187
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():

    # -- prepration
    # create fake variables
    fact_vars = dict()
    fact_vars['facts'] = dict()
    fact_vars['facts']['var1'] = 7
    fact_vars['facts']['var2'] = 'test'

    playbook_vars = dict()
    playbook_vars['var3'] = 'test2'
    playbook_vars['var4'] = 'test3'
    playbook_vars['var5'] = 'test4'

    # create fake task with facts
    action = 'include'
    args = dict()
    args['file'] = 'playbook.yaml'
    args['role'] = 'app'
    args['var1'] = 'test1'
    args['var2'] = 'test2'

# Generated at 2022-06-13 09:25:22.728418
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    ti = TaskInclude()
    ti.action = 'include'
    ti.args = {'x': 1, 'y': 2}
    ti.vars = {'a': 3, 'b': 4}
    ti.get_vars()

# Generated at 2022-06-13 09:25:23.908406
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    # Not implemented yet
    pass

# Generated at 2022-06-13 09:25:27.608247
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    task_include = TaskInclude()
    task_include.args = {'apply': {'name': 'foo'}}
    assert task_include.build_parent_block().name == 'foo'

# Generated at 2022-06-13 09:25:36.550115
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    # Setup
    task = TaskInclude(block=None, role=None, task_include=None)

    # Execute
    result = task.preprocess_data({'when': 'yes', 'debug': 'yes', 'action': 'include_role'})

    # Check result
    assert 'when' in result
    assert 'debug' not in result
    assert 'action' in result

    # Execute
    result = task.preprocess_data({'when': 'yes', 'debug': 'yes', 'action': 'include_tasks'})

    # Check result
    assert 'when' in result
    assert 'debug' in result
    assert 'action' in result

# Generated at 2022-06-13 09:25:46.632419
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():

    fake_loader     = "fake_loader"
    fake_ds         = dict(action = "fake_action",
                           imported_from = "fake_imported_from",
                           args = dict(file = "fake_file",
                                       _raw_params = "fake_raw_params"))
    fake_block      = "fake_block"
    fake_task_include = "fake_task_include"
    fake_variable_manager = "fake_variable_manager"

    ti = TaskInclude(block=fake_block, task_include=fake_task_include)
    ti._loader = fake_loader
    received = ti.preprocess_data(fake_ds)

    assert received           == fake_ds
    assert received['action'] == "fake_action"

# Generated at 2022-06-13 09:25:54.463159
# Unit test for method get_vars of class TaskInclude

# Generated at 2022-06-13 09:26:00.160999
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    yaml = """
    - block:
        - include: foo.yml x=y
    """
    rval = Task.load(yaml)
    assert 'x' in rval.get_vars()

    include = rval.block.block[0]
    assert 'x' in include.get_vars()



# Generated at 2022-06-13 09:26:11.533751
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    class MockParent:
        _play = 'play'
        _role = 'role'
        _variable_manager = 'vm'
        _loader = 'loader'
    class MockBlock:
        _parent = MockParent()
        _role = 'role'
        _variable_manager = 'vm'
        _loader = 'loader'
        def __init__(self, name):
            self.name = name
            self.block = []
            self.args = {}
        def load(self, data, play=None, role=None, task_include=None, variable_manager=None, loader=None):
            return self
    mock_block = MockBlock('block')
    mock_task = MockBlock('task')
    mock_include = TaskInclude()
    mock_include._role = 'role'
    mock_include._variable_

# Generated at 2022-06-13 09:26:18.109441
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    task_name = 'test_module'
    include_task = TaskInclude()
    include_task.action = 'include_role'
    include_task.args = {'_raw_params': 'role_name'}
    incorrect_args = {'environ': {'path': '/usr/bin'}}
    include_task.check_options(include_task, data={
        'action': include_task.action,
        'name': task_name,
        **incorrect_args
    })

    assert 'environ' not in include_task.args
    assert '_raw_params' in include_task.args
    assert include_task.args['_raw_params'] == 'role_name'


# Generated at 2022-06-13 09:26:24.948352
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    name = "test-task"
    action = "include_tasks"
    args = {"a":"1", "b":"2", "c":3}
    data = {name: name, action: action, "args": args }

    task = TaskInclude.load(data)  #This is equivalent to: TaskInclude(name=name, action=action, args=args)
    task.action = "include_role"
    vars = task.get_vars()
    for key in args.keys():
        assert key in vars and vars[key] == args[key]

# Generated at 2022-06-13 09:26:37.561025
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    # TODO: IMO it should be replaced with a py.test fixture
    dummy_play = {'name': 'test_play', 'hosts': 'test_hosts'}
    dummy_task_incl = TaskInclude(block=None, role=None, task_include=None)
    dummy_task_incl._role = None
    dummy_task_incl._play = dummy_play
    dummy_task_incl._loader = None
    dummy_task_incl._templar = None
    dummy_task_incl._parent = None
    dummy_task_incl.vars = {}
    dummy_task_incl.args = {'foo': 'bar', 'baz': 'quux'}
    dummy_task_incl.action = 'include'
    dummy_task_incl.statically

# Generated at 2022-06-13 09:26:51.164216
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():

    # We define a fake class and a fake method that returns a dict
    class fake_class:
        def get_vars(self):
            data = dict()
            data['name'] = 'fake_name'
            data['age'] = 'fake_age'
            data['job'] = 'fake_job'
            data['tags'] = 'fake_tags'
            return data

    # We define a fake task
    class fake_task(TaskInclude):
        pass

    fake_task._parent = fake_class()
    fake_task.vars = dict()
    fake_task.action = 'fake_action'
    fake_task.args = dict()
    fake_task.args['name'] = 'fake_name'
    fake_task.args['age'] = 'fake_age'

# Generated at 2022-06-13 09:26:55.415113
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    from ansible.parsing.dataloader import DataLoader

    ti = TaskInclude()
    ti.args = {'apply': {}}
    result = ti.build_parent_block()
    assert result == ti, result


# Generated at 2022-06-13 09:27:05.765537
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    data = {'action': 'include_role',
            'name': 'some_name',
            'apply': {'a': 'b'},
            'args': 'some_args',
            'bogus_arg': 'bogus_value',
            'no_log': False,
            'tags': ['sometag'],
            'when': False
            }

    # Test warning when C.INVALID_TASK_ATTRIBUTE_FAILED == False
    ti = TaskInclude()
    ti.preprocess_data(data)

    # Test exception when C.INVALID_TASK_ATTRIBUTE_FAILED == True
    C.INVALID_TASK_ATTRIBUTE_FAILED = True
    ti = TaskInclude()

# Generated at 2022-06-13 09:27:14.467346
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task

    # Init task include
    task_include = TaskInclude(block=None, task_include=None, role=None)

    # Init variables
    loader = None
    variable_manager = None
    play_context = PlayContext()

# Generated at 2022-06-13 09:27:24.823410
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    ti = TaskInclude()

    # Test invalid combinations
    with pytest.raises(AnsibleParserError):
        task = dict(action='include', file='foo')
        ti.check_options(task, None)

    with pytest.raises(AnsibleParserError):
        task = dict(action='include', file='foo', debug=True)
        ti.check_options(task, None)

    with pytest.raises(AnsibleParserError):
        task = dict(action='import_playbook', file='foo')
        ti.check_options(task, None)

    with pytest.raises(AnsibleParserError):
        task = dict(action='import_tasks', file='foo')
        ti.check_options(task, None)


# Generated at 2022-06-13 09:27:37.336000
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    # FIXME: TaskInclude.VALID_ARGS should ideally be tested in unit test
    my_ti = TaskInclude()
    my_task = Task()
    my_task.action = 'include'
    my_task.args = {'file': 'xxxxxx.yml'}
    # Only valid args
    assert my_ti.check_options({}, {}) == {}
    # Bad opts
    bad_opts = 'bad_opt1,bad_opt2,bad_opt3,bad_opt4'.split(',')
    bad_opts = dict((o, o) for o in bad_opts)
    bad_opts.update(dict(file='xxxxxx.yml'))
    my_task.args = bad_opts

# Generated at 2022-06-13 09:27:43.600312
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    attrs = {'action': 'include', 'args': {'file': '/path/to/file.yaml'}}
    data = dict(name='test', include=attrs)
    task_include = TaskInclude.load(data)
    assert task_include.args['_raw_params'] == task_include.args.pop('file')
    assert task_include.args == {'_raw_params': '/path/to/file.yaml'}

# Generated at 2022-06-13 09:27:58.977101
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    # Initialize task
    class Play:
        def get_vars(self):
            return {'ansible_python_interpreter': 'test_interpreter'}
    play = Play()
    task = TaskInclude(play)
    task.args = {'include_role': 'test_include_role', 'include_tasks': 'test_include_tasks',
                  'import_role': 'test_import_role', 'import_tasks': 'test_import_tasks'}
    # Test method

    python_interpreter = task.get_vars()['ansible_python_interpreter']
    assert python_interpreter == 'test_interpreter'
    # Test method for include_role
    include_role = task.get_vars()['include_role']
    assert include_role

# Generated at 2022-06-13 09:28:05.229809
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():

    # Test if the method build_parent_block of the class TaskInclude creates parents dynamically
    # when apply is specified
    block = Block()

    test_block = dict(
        apply=dict(block=[]),
    )

    task_include = TaskInclude(block=block)

    task_include.args['apply'] = test_block['apply']
    parent_block = task_include.build_parent_block()

    # Test if the parent block of apply is being created dynamically
    assert parent_block is not None
    assert parent_block != task_include

    # Test if the method build_parent_block of the class TaskInclude returns the parent block as
    # itself when apply is not specified.
    block = Block()

    test_block = dict(
        apply=dict(block=[]),
    )

    task_include

# Generated at 2022-06-13 09:28:21.935458
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    pplay = {
        'name': 'play1'
    }
    ptask = {
        'name': 'task1',
        'when': {'var1': 'ok'},
        'vars': {'var1': 'ok'}
    }

    def get_block_vars(block):
        return block.get_vars()

    def get_task_vars(task):
        return task.get_vars()

    ###################################################################
    # get_vars for a TaskInclude included (via include_tasks) from a Block
    ###################################################################
    # If a Block includes some included tasks, get_vars for the included
    # Block should return the variables defined for that Block. For example,
    # Block:
    #   - name: myblock
    #     when: always


# Generated at 2022-06-13 09:28:28.022149
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():

    # This is the default behaviour
    task = TaskInclude(task_include=None, role=None, block=None)
    assert task.get_vars() == {}

    # This is the default behaviour
    task = TaskInclude(task_include=None, role=None, block=Block(parent=None))
    assert task.get_vars() == {}

    # This is the default behaviour
    task = TaskInclude(task_include=None, role=None, block=Block(parent=Block()))
    assert task.get_vars() == {}

    # This is the default behaviour
    task = TaskInclude(task_include=None, role=None, block=Block(parent=Block(), vars=dict(a="a")))
    assert task.get_vars() == {'a': "a"}

    #

# Generated at 2022-06-13 09:28:38.803003
# Unit test for method load of class TaskInclude
def test_TaskInclude_load():
    def _check_arg(value, expected_value, loader=None, variable_manager=None, block=None, role=None, task_include=None):
        data = {
            'file': value,
        }
        task = TaskInclude.load(
            data,
            block=block,
            role=role,
            task_include=task_include,
            variable_manager=variable_manager,
            loader=loader,
        )

        assert task.args['_raw_params'] == expected_value
        assert task.statically_loaded
        assert task.args['file'] == expected_value  # alias is assigned

    # When a string is provided
    _check_arg('foo', 'foo')

    # When a 'file' is provided
    _check_arg({'file': 'foo'}, 'foo')

   

# Generated at 2022-06-13 09:28:46.836606
# Unit test for method build_parent_block of class TaskInclude

# Generated at 2022-06-13 09:28:53.221652
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.role_context import RoleContext
    from ansible.vars.manager import VariableManager

    try:
        from ansible.parsing.dataloader import DataLoader
        from ansible.executor.task_queue_manager import TaskQueueManager
    except ImportError:
        from ansible.utils.loader import DataLoader
        from ansible.executor.task_queue_manager import TaskQueueManager

    from ansible.playbook.block import Block

    class MockIncludeTask:
        def __init__(self):
            self.args = dict()
            self._play = PlayContext()
            self._role = RoleContext()
            self._variable_manager = VariableManager()
            self._loader = DataLoader()
            self._task_v

# Generated at 2022-06-13 09:29:03.321673
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar

    mock_variable_manager = dict(vars=dict(a=1))

    task_data = dict(
        action='include',
        args=dict(_raw_params='foo', apply=dict(task_implicit=dict(a=2))),
        blocks=[],
        post_validate=True,
        name="test_TaskInclude_build_parent_block",
        loop_control={},
        ignore_errors=False,
        any_errors_fatal=False,
        no_log=False,
        run_once=False,
        delegate_to='localhost',
        register='test_task_register',
        when=[],
        vars=[],
        tags=[],
    )

    task = TaskIn

# Generated at 2022-06-13 09:29:17.819271
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    class MockParent(object):
        def get_vars(self):
            return {'parent_key': 'parent_value', 'parent_key_dup': 'parent_value_dup', 'key': 'value'}

    class MockRole(object):
        def __init__(self, tas):
            self.tasks = tas

    class MockPlay(object):
        def __init__(self):
            self.roles = [MockRole([t]) for t in tasks]

    parent = MockParent()
    play = MockPlay()


# Generated at 2022-06-13 09:29:26.744032
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    # Tests that the method 'get_vars()' returns the expected variables.
    # Expects a TaskInclude object as input.

    # The 'args' variable of the TaskInclude class is used to store the
    # arguments of the include tasks.
    # The following code illustrates initialization of 'args' variable:
    #   args = self.load_data(data, variable_manager=variable_manager, loader=loader)
    def load_data(data, variable_manager=None, loader=None):
        return {'hello': 'world'}

    # Initialization of action variable of the TaskInclude class
    action = 'include'
    # Initialization of TaskInclude class object
    my_task_include = TaskInclude()
    # Initialization of 'vars' variable of the TaskInclude class
    my_task_include.v

# Generated at 2022-06-13 09:29:29.577665
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    my_class = TaskInclude()
    my_class.args = {}
    assert(my_class.build_parent_block() == my_class)
    my_class.args = {'apply':{}}
    assert(my_class.build_parent_block() != my_class)

# Generated at 2022-06-13 09:29:39.693860
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    from ansible.playbook.conditional import Conditional
    from ansible.playbook.play import Play
    from ansible.playbook.block import Block
    from ansible.playbook.role.include import RoleInclude
    from ansible.playbook.handler_task_include import HandlerTaskInclude

    apply_data = {
        'when': 'failed',
        'ignore_errors': True,
        'block': [
            {
                'name': 'hello',
                'debug': {'var': 'myvar'}
            }
        ]
    }
    data = {
        'action': 'include',
        'apply': apply_data
    }
    dummy_host = "hostname"
    play = Play().load({'name': 'test play', 'hosts': dummy_host})

# Generated at 2022-06-13 09:29:54.821824
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    pass

_NO_VALUE = Sentinel("No Value", var_name="_NO_VALUE")  # Not used anywhere else in this file


# Generated at 2022-06-13 09:30:02.838413
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    task = TaskInclude()

    task.vars = {
        'A': '1',
        'B': '2'
    }

    task.args = {
        'C': '3',
        'D': '4'
    }

    parent = Task()
    parent.vars = {
        'A': '11',
        'E': '5'
    }

    task._parent = parent

    assert set(task.get_vars()) == set(task.args.keys() + task.vars.keys() + parent.vars.keys())
    assert task.get_vars()['A'] == '1'
    assert task.get_vars()['B'] == '2'
    assert task.get_vars()['C'] == '3'

# Generated at 2022-06-13 09:30:09.641432
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    '''
    Test the method get_vars from class TaskInclude
    '''
    import ansible.playbook.block
    import ansible.playbook.role
    import ansible.playbook.play
    from ansible.vars.manager import VariableManager

    pb = ansible.playbook.play.Play()
    pb.name = "Test Playbook"
    pb.hosts = ["all"]

    role = ansible.playbook.role.Role()
    role._role_name = "Test Role"

    block = ansible.playbook.block.Block()
    block._play = pb
    block._role = role

    task = TaskInclude(block=block)
    task.action = 'include'
    task.args = dict()
    task.vars = dict()

# Generated at 2022-06-13 09:30:24.785308
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    # For now, we just verify that the method doesn't raise any exceptions
    # This method is pretty static, so we don't test its own behaviour. It
    # doesn't have its own tests, but is visible in the test TaskInclude.load
    # and is indirectly tested by tests using TaskInclude.load
    import ansible.playbook.role as role

    # We use the class TaskInclude, not the instance, because we need a parent
    # object to build the Block, so we have to use the TaskInclude.load method
    my_task = TaskInclude.load(
        data={'action': 'include_role', 'apply': {'block': 'my_block'}},
        task_include=TaskInclude(),
        role=role.Role(),
        variable_manager=None,
        loader=None,
    )
   

# Generated at 2022-06-13 09:30:27.110980
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    """
    Test confirmed that it fails when the key is not in the specified set and succeeds when it is
    """
    task = TaskInclude()
    data = '''
- include: /test
  other: 123
'''
    task.load(data)

# Generated at 2022-06-13 09:30:38.734963
# Unit test for method load of class TaskInclude
def test_TaskInclude_load():
    from ansible.playbook.block import Block
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    host_list = [
        "127.0.0.1",
        "127.0.0.2",
        "127.0.0.3",
        "127.0.0.4"
    ]

    hosts = []

    inventory = InventoryManager(loader=loader, sources=host_list)

    for host in inventory.list_hosts():
        # set some hosts to not be available
        if host.name in host_list[:2]:
            host.set_variable('ansible_connection', 'local')

# Generated at 2022-06-13 09:30:48.200353
# Unit test for method load of class TaskInclude
def test_TaskInclude_load():
    ai = TaskInclude()
    ti = ai.load({'action': 'include', 'file': 'f1'})
    assert ti.action == 'include'
    assert ti.args['_raw_params'] == 'f1'
    assert ti.args['file'] == 'f1'

    ti = ai.load({'action': 'import_playbook', 'file': 'f1'})
    assert ti.action == 'import_playbook'
    assert ti.args['file'] == 'f1'

    ti = ai.load({'action': 'import_role', 'name': 'my_role'})
    assert ti.action == 'import_role'
    assert ti.args['name'] == 'my_role'


# Generated at 2022-06-13 09:30:55.554243
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    class MyPlay(object):
        def __init__(self):
            # fake the variable manager
            self.vars = dict()

        def get_variable_manager(self):
            return self
    # test that get_vars() raise a AnsibleError when the task's action is 'include' and the parent task var's still empty
    play = MyPlay()

# Generated at 2022-06-13 09:31:06.401056
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    task = TaskInclude()
    task.vars['key1'] = 'value1'
    task.block = Block()
    task.block._parent = Block()
    task.block._parent.vars = {'key2': 'value2'}
    task.args = {'key3': 'value3'}

    for action in C._ACTION_ALL_INCLUDE_ROLE_TASKS:
        task.action = action
        vars_ = task.get_vars()

        assert isinstance(vars_, dict)
        assert len(vars_) == 3
        assert vars_.get('key1') == 'value1'
        assert vars_.get('key2') == 'value2'
        assert vars_.get('key3') == 'value3'


# Generated at 2022-06-13 09:31:16.872939
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    import ansible.playbook.role.task as task_module

    task = task_module.TaskInclude(block=None, role=None, task_include=None)

    # No action
    data = dict(a='a', b='b', c='c')
    try:
        task.check_options(task.load_data(data), data)
    except AnsibleParserError as e:
        assert 'No file specified' in str(e)
    else:
        assert False, 'No exception raised'

    # No file
    data = dict(action='include', b='b', c='c')
    try:
        task.check_options(task.load_data(data), data)
    except AnsibleParserError as e:
        assert 'No file specified' in str(e)
    else:
        assert False

# Generated at 2022-06-13 09:31:57.032066
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    from ansible.playbook.play_context import PlayContext

    class TestPlay(object):
        def __init__(self):
            self.default_vars = {}

    class TestRole(object):
        def __init__(self):
            self.vars = {}
            self.task_blocks = [
                ['block1'],
                ['block2']
            ]

    test_play = TestPlay()
    test_role = TestRole()

    test_task = TaskInclude()
    test_task._role = test_role
    test_task._parent = test_play
    test_task.action = 'include'
    test_task.vars = {'var1': 'val1'}
    test_task.args = {'arg1': 'val1'}

    # action is 'include', vars

# Generated at 2022-06-13 09:32:05.316356
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    from ansible.playbook.block import Block

    ti = TaskInclude(block=Block())
    ti.args['_raw_params'] = 'test_file'

    task = {'action': 'include', 'args': {'_raw_params': 'test_file'}}
    test_1 = ti.check_options(task=task, data=None)
    assert test_1['args']['_raw_params'] == 'test_file'

    task = {'action': 'import_playbook', 'args': {'_raw_params': 'test_file'}}
    test_2 = ti.check_options(task=task, data=None)
    assert test_2['args']['_raw_params'] == 'test_file'


# Generated at 2022-06-13 09:32:13.985246
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    ti = TaskInclude()
    ti.action = 'include'
    ti.args = {'apply': {'name': 'the-name', 'with_items': []}}
    parent = ti.build_parent_block()
    assert isinstance(parent, Block)
    assert isinstance(parent, TaskInclude)
    assert parent.action == 'the-name'
    assert parent.loop.loop_with == 'with_items'
    assert parent.loop.item_name == []

    ti.args = {'apply': {'name': 'the-name', 'with_dict': []}}
    parent = ti.build_parent_block()
    assert isinstance(parent, Block)
    assert isinstance(parent, TaskInclude)
    assert parent.action == 'the-name'

# Generated at 2022-06-13 09:32:20.403712
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    from ansible.playbook.play_context import PlayContext
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.task_result import TaskResult
    from ansible.plugins.loader import module_loader

    tasks = [
        dict(action=dict(module='debug', args=dict(msg='{{ file }}'))),
    ]
    loader = DataLoader()
    variable_manager = VariableManager()
    variable_manager.extra_vars = dict(file='test')
    play_context = PlayContext()


# Generated at 2022-06-13 09:32:23.476244
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    t = TaskInclude()
    t.args['apply'] = {'when': 'test'}
    p_block = t.build_parent_block()
    assert p_block.args['when'] == 'test'


# Generated at 2022-06-13 09:32:30.725912
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    block = Block(play=None)
    role = None
    task_include = None
    ti = TaskInclude(block=block, role=role, task_include=task_include)
    ti.action = 'not-include'
    ti.args['test_arg'] = 'test_val'
    ti.vars['test_var'] = 'test_val'
    all_vars = ti.get_vars()
    assert 'test_arg' not in all_vars
    assert 'test_var' in all_vars
    assert all_vars['test_var'] == 'test_val'
    ti.action = 'include'
    all_vars = ti.get_vars()
    assert 'test_arg' in all_vars
    assert 'test_var' in all_vars
   

# Generated at 2022-06-13 09:32:36.903889
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    from ansible.playbook.play import Play
    from ansible.playbook.role import Role
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.errors import AnsibleOptionsError
    import pytest

    display = Display()
    loader = DataLoader()
    variable_manager = VariableManager()
    variable_manager.extra_vars = {'foo': 'bar', 'listvar': ['a', 'b'], 'tvars': {'a': 'b'}}

# Generated at 2022-06-13 09:32:51.700877
# Unit test for method load of class TaskInclude
def test_TaskInclude_load():
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.playbook.task_include import TaskInclude

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = Inventory(loader, variable_manager, host_list=[])
    play_source = dict(
        name="Ansible Play",
        hosts='localhost',
        gather_facts='no',
        tasks=[
            dict(action=dict(include='a_file.yaml', b=1)),
            dict(action=dict(include='a_file.yaml', b=1, apply='invalid_type'))
        ]
    )


# Generated at 2022-06-13 09:33:00.386174
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task

    # The test case for the method TaskInclude.check_options.
    #
    # NOTE:
    # The TaskInclude class does not need any test case for the method load.
    # The method load(...) is a factory method for the method `load_data(...)`
    # of the superclass Task and the method `check_options(...)` of the current
    # class, which are tested in the classes TestTaskInPlay and TestTaskInRole
    # of the test file test_tasks.
    def tc_TaskInclude_check_options(action, data, expected_obj, expected_exc_tp, expected_exc_msg):
        # Make a TaskInclude object
        t = TaskInclude(Block())
        t.action

# Generated at 2022-06-13 09:33:06.381052
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    from ansible.playbook.play import Play
    from ansible.playbook.role import Role
    from ansible.playbook.block import Block
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    host_list = InventoryManager(loader=DataLoader())
    variable_manager = VariableManager(loader=DataLoader(), inventory=host_list)