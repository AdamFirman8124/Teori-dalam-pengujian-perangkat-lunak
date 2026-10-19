

# Generated at 2022-06-13 09:23:47.032010
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():

    from ansible.utils.display import Display
    from ansible.parsing.yaml.constructor import AnsibleConstructor

    ################################################################
    # Below we test the get_vars() method of class TaskInclude.
    # We need to make sure that:
    # - when 'apply' is present, the args are also added to the vars
    # - when 'apply' is not present, the args are not being added to
    #   the vars
    # - the 'tags' and the 'when' args are not being added to the vars
    # - the vars of the parent are being added to the vars
    # These tests cover the following methods:
    # - TaskInclude.build_parent_block()
    # - Task._get_parent_attribute()
    # - Task.get_vars()

# Generated at 2022-06-13 09:23:56.242345
# Unit test for method load of class TaskInclude
def test_TaskInclude_load():
    from ansible.playbook import Play
    from ansible.playbook.play import Play as Play_

    from ansible.playbook.play_context import PlayContext

    from ansible.executor.task_queue_manager import TaskQueueManager

    from ansible.vars.manager import VariableManager

    from ansible.utils.vars import combine_vars
    from ansible.parsing.dataloader import DataLoader

    from ansible.inventory.manager import InventoryManager

    # set some of attributes
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=["localhost", "other_hosts"])

    variable_manager = VariableManager(loader=loader, inventory=inventory)

    # create a new play

# Generated at 2022-06-13 09:24:11.477679
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext

    data = AnsibleLoader(None, '''
    - include: test_include.yml
      action: include_tasks
      name: test
      static: yes
      apply:
        tags:
          - test
    ''').get_single_data()
    data = dict((k, v) for k, v in data.items() if v is not None)
    data.pop('action', None)

    parent_block = Play()
    parent_block._play = Play()
    parent_block._play._context = PlayContext()


# Generated at 2022-06-13 09:24:21.817356
# Unit test for method load of class TaskInclude
def test_TaskInclude_load():
    '''
    Unit test for TaskInclude.load method.
    '''
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.block import Block
    from ansible.playbook.role.include import RoleInclude
    from ansible.playbook.play_context import PlayContext

    my_role = RoleDefinition.load("test_role")
    my_block = Block.load(dict(
        tasks=[
            dict(
                include="include setup",
                static="test static",
            ),
            dict(
                include="test include",
            ),
        ],
    ), parent_block=my_role)
    task_include = TaskInclude.load(dict(
        include="test include",
    ), block=my_block, role=my_role)

    assert task_include

# Generated at 2022-06-13 09:24:27.410891
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    ti = TaskInclude()
    ds = {'tasks': [{'action': 'include', 'name': 'some_name', 'one': 1, 'two': 2}]}
    new_ds = ti.preprocess_data(ds)
    assert 'two' not in new_ds['tasks'][0]


# Generated at 2022-06-13 09:24:34.773216
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    '''
    Unit test for method preprocess_data of class TaskInclude.
    Create an instance of TaskInclude, call the method with a dict
    containing valid and invalid keywords and check that it raises an
    exception for the invalid keywords, and return the dict otherwise.
    '''
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    task = TaskInclude(block=None, role=None, task_include=None)

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources='')
    variable_manager = VariableManager(loader=loader, inventory=inventory)


# Generated at 2022-06-13 09:24:42.744152
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    host_results_file = '/tmp/test_playbook_results.txt'
    if os.path.exists(host_results_file):
        os.remove(host_results_file)
    fd, path = tempfile.mkstemp()
    f = os.fdopen(fd,'w')
    f.write(u'---\n  - name: test-playbook')
    f.close()


# Generated at 2022-06-13 09:24:46.870789
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    # mock up all the external imports that build_parent_block depends on
    mock_Block_load = opaque_mock()
    mock_Block_load.return_value = opaque_mock()
    mock_Block_load.return_value._play = opaque_mock()
    mock_Block_load.return_value._role = opaque_mock()
    mock_Block_load.return_value._variable_manager = opaque_mock()
    mock_Block_load.return_value._loader = opaque_mock()
    mock_Block = opaque_mock()
    mock_Block.load = mock_Block_load
    orig_Block = Block
    Block = mock_Block

    # mock up all the external imports that __init__ of TaskInclude depends on
    mock_Display_warning = opaque_mock()
    display = opaque

# Generated at 2022-06-13 09:24:59.159156
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    # test that the get_vars() return vars from the play, role, block and task when self.action is not in C._ACTION_INCLUDE
    fake_task = TaskInclude(dict(name='fake task', action='fake action'))
    fake_task._parent = {}
    fake_task._parent.get_vars = lambda: dict(parent_vars=1)
    fake_task._role = {}
    fake_task._role.get_vars = lambda: dict(role_vars=2)
    fake_task._play = {}
    fake_task._play.get_vars = lambda: dict(play_vars=3)
    fake_task.vars = dict(task_vars=4)

    fake_task.action = 'fake action'
    assert fake_task.get_v

# Generated at 2022-06-13 09:25:08.817380
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    # Create a task include with a task which has args
    task = TaskInclude(task_include=Task(args={'arg1': 'value1'}))
    # Check args is included into task include's vars
    assert task.get_vars() == {'arg1': 'value1'}

    # Create task include with a task which has vars and args
    task = TaskInclude(task_include=Task(vars={'var1': 'value1'}, args={'arg1': 'value1'}))
    # Check vars and args are included into task include's vars
    assert task.get_vars() == {'arg1': 'value1', 'var1': 'value1'}

    # Create task include with a task which has vars and args and parent vars
    parent = Task()

# Generated at 2022-06-13 09:25:22.932945
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    ti = TaskInclude()
    assert ti.preprocess_data({}) == {}
    assert ti.preprocess_data({'action': 'include_role', 'foo': 'bar'}) == {'action': 'include_role', 'foo': 'bar'}
    assert ti.preprocess_data({'action': 'include_role', 'tags': 'baz', 'foo': 'bar'}) == {'action': 'include_role', 'foo': 'bar'}

    ti.action = 'include_role'

    assert ti.preprocess_data({}) == {}
    assert ti.preprocess_data({'action': 'include_role', 'foo': 'bar'}) == {'action': 'include_role', 'foo': 'bar'}

# Generated at 2022-06-13 09:25:35.387279
# Unit test for method load of class TaskInclude
def test_TaskInclude_load():
    '''
    Test method load of class TaskInclude. It generates a task with different kind of input
    and tests if the loaded task is as expected

    The test is executed only if INCLUDE_ROLE_TASKS is loaded
    '''
    from ansible.inventory.group import Group
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext


# Generated at 2022-06-13 09:25:41.926075
# Unit test for method load of class TaskInclude
def test_TaskInclude_load():
    '''
    Test if the load method of TaskInclude properly loads from data (dedicated to action)
    '''
    from ansible.playbook.included_file import IncludedFile

    # check load for 'include' action
    for action in C._ACTION_INCLUDE:
        task = TaskInclude.load(dict(action=action, file="repo/tasks/main.yml"))
        assert task.action == action
        assert task.args['_raw_params'] == "repo/tasks/main.yml"
        assert task._parent is None
        assert task._role is None
        assert task._play is None
        assert task._task_include is None
        assert task._loader is None
        assert task._variable_manager is None
        assert task.statically_loaded is False
        assert task._block

# Generated at 2022-06-13 09:25:52.071592
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.plugins.loader import add_all_plugin_dirs
    add_all_plugin_dirs()

    display.verbosity = 3
    fake_loader, inventory, variable_manager = C.TEST_DIRECTORY
    play_context = PlayContext()
    task = TaskInclude()
    def test_preprocess(ds, expected_action):
        ds = task.preprocess_data(ds)
        action = ds['action']
        assert action == expected_action, "Expected action is %s but got %s instead" % (expected_action, action)
        return ds

    # 1. Test the behavior of the action
    #   1.1 Action 'include_tasks'


# Generated at 2022-06-13 09:25:58.786623
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    class TestModule(object):
        _ANSIBLE_ARGS = frozenset(('action', 'args', 'collections', 'debugger', 'ignore_errors', 'loop', 'loop_control',
                                   'loop_with', 'name', 'no_log', 'register', 'run_once', 'tags', 'timeout', 'vars'))

        def __init__(self):
            self.args = {}

        def check_options(self, task, data):
            my_arg_names = frozenset(task.args.keys())
            bad_opts = my_arg_names.difference(self._ANSIBLE_ARGS)

# Generated at 2022-06-13 09:26:09.323911
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext

    loader = DataLoader()
    variable_manager = VariableManager()
    play_context = PlayContext()
    play_context.set_variable_manager(variable_manager)

    task = {'action': 'include',
            'file': 'playbook.yml',
            'apply': {
                'tags': ['all'],
                'when': '1 == 1'
            }}
    ti = TaskInclude()
    ti.name = 'task include with valid options'
    ti.set_loader(loader=loader)
    ti.set_variable_manager(variable_manager=variable_manager)

# Generated at 2022-06-13 09:26:17.184979
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    '''
    Test TaskInclude.check_options with different cases
    '''

    # Test when the task has a wrong key
    data = dict(file='/path/to/file', wrong_opt='foo', action='include')
    ti = TaskInclude()
    task = ti.load(data, variable_manager=None, loader=None)
    try:
        ti.check_options(task, data)
    except AnsibleParserError as e:
        assert "Invalid options for include: wrong_opt" in str(e)
    else:
        assert False, 'AnsibleParserError not raised'
    data.pop('wrong_opt')

    # Test when the task has the apply key
    data['apply'] = dict(playbook_variables='foo')

# Generated at 2022-06-13 09:26:26.596455
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    all_vars = dict()
    all_vars['first'] = 'var'
    all_vars['second'] = 'var'
    all_vars['third'] = 'var'
    all_vars['fourth'] = 'var'
    all_vars['fifth'] = 'var'

    module_args = dict()
    module_args['action'] = 'include'
    module_args['file'] = 'test.yml'
    module_args['first'] = 'changed var'
    module_args['sixth'] = 'var'
    module_args['tags'] = ['tag1', 'tag2', 'tag3']

    ti = TaskInclude(args=module_args)

    class Task:
        def get_vars(self):
            return all_vars

    ti._parent = Task()

# Generated at 2022-06-13 09:26:35.595408
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    from ansible.playbook import Play

    # TODO: There should be a more elegant way to test this.
    #       Maybe this can be done using mock objects.
    task = TaskInclude()
    play = Play().load({'hosts': 'all', 'vars': {'var1': 'value1'}})
    play.add_task(task)
    task.load({'action':'shell', 'args': {'var2': 'value2'}})
    task_res = task.get_vars()
    assert task_res == {'var1': 'value1', 'var2': 'value2'}

# Generated at 2022-06-13 09:26:49.452519
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.task import Task
    from ansible.parsing.yaml.objects import AnsibleUnicode, AnsibleMapping
    from ansible.utils.listify import listify_lookup_plugin_terms

    def make_task_object(action, data, file=None):
        task = Task()
        task.action = action
        task.args = dict()
        if file:
            task.args['file'] = file
        task.args.update(data)
        args = task.args
        args.update(task.vars)

        task._role = None
        task._parent = None
        task._block = None
        task._play = None
        task._loader = None
        task._variable_manager = None

       

# Generated at 2022-06-13 09:27:04.506834
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    '''
    Test that get_vars returns the right vars
    '''
    from ansible.playbook import Play
    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext

    p = Play().load({'name': 'foo', 'hosts': 'all'}, variable_manager=None, loader=None)
    pc = PlayContext()

    # test that 'include' in C._ACTION_ALL_INCLUDE_ROLE_TASKS is handled
    ti_include = TaskInclude().load({'action': 'include', 'name': 'test', 'var1': 'baz'}, block=p, role=None, task_include=None, variable_manager=None, loader=None)

# Generated at 2022-06-13 09:27:13.543970
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    from ansible.playbook.play import Play
    from ansible.playbook.role import Role
    from ansible.playbook.role.include import RoleInclude
    from ansible.playbook.role.tasks import Task as RoleTask
    from ansible.playbook.block import Block
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    role = Role()
    ri = RoleInclude()
    ri.load({'name': 'test', 'file': 'file.yaml'}, role=role)

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=None)
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    ti = TaskInclude

# Generated at 2022-06-13 09:27:20.001524
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    from ansible.playbook.block import Block
    test_data = dict(
        type='task_include',
        name='include_tasks',
        action='include_tasks',
        args=dict(_raw_params='foo.yml', apply={})
    )
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.vars.unsafe_proxy import UnsafeProxy
    from ansible.parsing.dataloader import DataLoader
    from ansible.plugins.loader import action_loader
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.executor.task_queue_manager import TaskQueueManager

# Generated at 2022-06-13 09:27:27.164337
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    # We mock the vars
    t = TaskInclude.load({'include_tasks': 'foo.yml', 'apply': {'name': 'test_TaskInclude_build_parent_block'}})
    assert t.args['_raw_params'] == 'foo.yml'
    assert t.args['apply'] == {'name': 'test_TaskInclude_build_parent_block'}
    p_block = t.build_parent_block()
    assert p_block.name == 'test_TaskInclude_build_parent_block'
    assert not p_block.has_tasks()
    assert p_block._parent is None


# Generated at 2022-06-13 09:27:38.332049
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    class TaskIncludeDummyParent(object):
        class TaskIncludeDummyGrandParent(object):
            vars = { "Parent_grandparent_var":"Parent_grandparent_val1" }

        vars = { "Parent_parent_var":"Parent_parent_val1" }
        parent = TaskIncludeDummyGrandParent()

    args = { "Parent_var":"Parent_val1", "var1":"val1" }
    vars = { "self_var":"self_val1", "var2":"val2" }
    task_include = TaskInclude()
    task_include.args = args
    task_include.vars = vars
    task_include._parent = TaskIncludeDummyParent()
    all_vars = task_include.get_vars()


# Generated at 2022-06-13 09:27:50.090410
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    from ansible.vars import VariableManager

    # Test a task include with no args or kwargs
    ti = TaskInclude(block=None, role=None, task_include=None)
    ds = {
        u'include': u'roles/common/tasks/main.yml',
        u'action': u'include',
    }
    templar = Templar(loader=None, variables=VariableManager())
    ti.load_data(ds, variable_manager=templar._available_variables)
    task = ti.check_options(
        ti,
        ds
    )
    assert isinstance(task, TaskInclude), 'task must be an instance of TaskInclude'

# Generated at 2022-06-13 09:28:02.428695
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    from ansible.playbook.play import Play
    from ansible.playbook.task_include import TaskInclude

    class MockPlaybook(object):
        def __init__(self, hosts, stats):
            self.hosts = hosts
            self.stats = stats

        def set_variable_manager(self, variable_manager):
            self.variable_manager = variable_manager

    class MockTaskInclude(TaskInclude):
        def __init__(self, action):
            TaskInclude.__init__(self, None)
            self.action = action
            self.args = dict()

        def add_parent_block(self, parent_block):
            self._parent = parent_block

    class MockBlock(object):
        def __init__(self, vars={}):
            self._vars = vars

       

# Generated at 2022-06-13 09:28:13.990830
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    # For example,
    # - include: some_module.yml apply:
    #       when: my_var == 1
    #       loop: my_var_loop
    #       loop_with_items:
    #           - a
    #           - b
    class MockParentTask:
        def __init__(self):
            self.action = "test_include"
            self.args = {'apply': {'when': 'my_var == 1',
                                   'loop': 'my_var_loop',
                                   'loop_with_items': ['a', 'b']}}
            self.tags = ['include_test']
            self._loader = None
            self._variable_manager = None
            self._role = None

    class MockTaskTag:
        def __init__(self, _parent=None):
            self

# Generated at 2022-06-13 09:28:24.327290
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    import mock
    import json
    import sys

    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.task import Task
    class MockedTask(TaskInclude):
        def __init__(self, args, action):
            self.args = args
            self.action = action

    def call(*args, **kwargs):
        if 'variable_manager' in kwargs and kwargs['variable_manager'] is None:
            del kwargs['variable_manager']
        return TaskInclude.load(*args, **kwargs)

    from ansible.utils.vars import combine_vars

    test_facts = dict(ansible_all_ipv4_addresses=['192.0.2.1'])

# Generated at 2022-06-13 09:28:28.158353
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    # this comes from the 'include' parsing
    data = dict(args=dict(file='/path/to/file', foo='bar'))

    task = TaskInclude()
    task.check_options(task, data)

    assert task.args == dict(_raw_params='/path/to/file')


# Generated at 2022-06-13 09:28:38.634655
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    class TestTask(TaskInclude):
        VALID_INCLUDE_KEYWORDS = TaskInclude.VALID_INCLUDE_KEYWORDS.union(('new_attr',))
        _validate_new_attr = lambda self, attr: False

    t = TestTask({'action': 'include', 'new_attr': {}, 'thats_unsupported': {'bar': 'baz'}})
    t.preprocess_data({'action': 'include', 'new_attr': {}, 'thats_unsupported': {'bar': 'baz'}})
    try:
        t.preprocess_data({'action': 'import_tasks', 'new_attr': {}, 'thats_unsupported': {'bar': 'baz'}})
    except AnsibleParserError:
        pass




# Generated at 2022-06-13 09:28:46.706245
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():

    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.role import Role
    from ansible.vars.manager import VariableManager

    # Play
    play = Play().load({
        'name': 'test',
        'hosts': 'localhost',
        'connection': 'local',
        'gather_facts': 'no',
        'tasks': [
            {
                'include': {
                    'file': 'test.yml',
                    'apply': {
                        'name': 'test',
                        'loop': [1,2,3]
                    }
                }
            }
        ]
    }, variable_manager=VariableManager(), loader=None)

    # Role

# Generated at 2022-06-13 09:28:53.132097
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins.loader import action_loader
    display = Display()

    # Basic test
    test_task_name = 'test_TaskInclude_get_vars'
    test_task_args = {'var1': 'value1', 'var2': 'value2'}

    data = {'action': 'include', 'args': test_task_args}
    test_task = TaskInclude.load(
        data,
        block=None,
        role=None,
        task_include=None,
        variable_manager=VariableManager(),
        loader=DataLoader(),
    )

# Generated at 2022-06-13 09:29:03.255223
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    '''
    Ensure that we get the proper parent block with apply attributes
    '''
    from ansible.playbook.task_include import TaskInclude
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    ti = TaskInclude.load({'include': 'test.yml'}, variable_manager=VariableManager(), loader=DataLoader(), inventory=InventoryManager())
    block = ti.build_parent_block()

    # No apply parameter should return the instance itself
    assert block == ti


# Generated at 2022-06-13 09:29:17.754156
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    # Create a mock object to test this method
    class FakeBlock:

        def __init__(self, vars):
            self.vars = vars

        def get_vars(self):
            return self.vars

    fb = FakeBlock({'a': 'A'})
    # We expect the vars dict of the task to be the vars dict of the parent block
    assert TaskInclude(block=fb, role=None, task_include=None).get_vars() == {'a': 'A'}

    # We expect the vars dict of the task to be the vars dict of the parent block,
    # and will be extended by vars dict of the task
    assert TaskInclude(block=fb, role=None, task_include=None,
                       vars={'b': 'B'}).get_

# Generated at 2022-06-13 09:29:26.709703
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    '''
    Unit test for method get_vars of class TaskInclude.

    :return: 
    '''
    task_include = TaskInclude()
    task_include.action = 'include'
    task_include.vars = {
        "a": 1
    }
    task_include.args = {
        "b": 2,
        "c": 3
    }
    print(task_include.get_vars())
    # {'b': 2, 'c': 3}

    task_include.action = 'include_role'
    print(task_include.get_vars())
    # {'a': 1, 'b': 2, 'c': 3},
    # the action is not in C._ACTION_INCLUDE, so it returns parent Task() classes get_vars() here



# Generated at 2022-06-13 09:29:32.124078
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    b = Block()
    ti = TaskInclude(block=b)
    ti.args = {'param1': "value1",
               'param2': "value2",
               'tags': ["tag1", "tag2"],
               'when': "true"}
    ti._parent = b
    assert (ti.get_vars() == {'param1': "value1",
                              'param2': "value2"})
    assert (ti.args == {'param1': "value1",
                        'param2': "value2",
                        'tags': ["tag1", "tag2"],
                        'when': "true"})



# Generated at 2022-06-13 09:29:40.986539
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.play import Play
    from ansible.yaml.objects import AnsibleBaseYAMLObject
    from ansible.parsing.plugin_docs import read_docstring
    from ansible.parsing.yaml.loader import AnsibleLoader

    my_block = Block()
    my_block._role = None
    my_block._play = Play()
    my_load_data = read_docstring(TaskInclude._load_data)
    my_load_data['action'] = 'include'

    raw_data = my_load_data
    raw_data.pop('block', None)
    my_obj = AnsibleBaseYAMLObject(None, raw_data)

    my_play

# Generated at 2022-06-13 09:29:48.947814
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    '''
    Unit test for method check_options of class TaskInclude
    '''
    # Calling check_options as a static method of TaskInclude
    # -------------------------------------------------------
    # pylint: disable=unused-argument
    # pylint complains about the signature of the init method of TaskInclude which is called
    # by the check_options method but this is not the case since we are calling check_options
    # statically and the data object used is not the same as that used in the init method for TaskInclude
    # This is the reason for the disable-msg
    class DummyTaskInclude(TaskInclude):
        '''
        Dummy class that inherits from TaskInclude just to test the static method check_options
        '''

# Generated at 2022-06-13 09:29:58.663932
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    variable_manager = VariableManager()
    variable_manager.extra_vars = {'test_var': 'foo'}
    variable_manager.options_vars = {'test_option': 'bar'}
    variable_manager.set_inventory(loader.load_from_file('tests/inventory'))
    variable_manager.set_play_context(PlayContext())

    templar = Templar(loader=loader, variables=variable_manager)

    # Ok

# Generated at 2022-06-13 09:30:23.285747
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    '''
    Test for method get_vars of class TaskInclude
    '''
    data = dict(
        name='test_TaskInclude_get_vars',
        action='include',
        file='ansible/modules/system/ping.yml',
        bar='baz',
        tags=['include_tag'],
        when='include_when',
        args=dict(
            foo='baz',
            qux='quux',
        )
    )

    task = TaskInclude.load(
        data,
    )
    task.tags = data.get('tags')
    task.when = data.get('when')

    result = task.get_vars()

# Generated at 2022-06-13 09:30:31.903266
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():

    # Test data
    data = dict(
        action         = 'include_role',
        loop           = ['item1', 'item2'],
        loop_with_dict = dict(key1 = 'value1')
    )

    # Test variables
    task = TaskInclude.load(data)
    task.vars = dict(
        key1 = 'value1'
    )
    task.args = dict(
        loop_control = 'loop_control:loop_var=my_loop_var',
        loop_with_dict = 'loop_with_dict',
        _raw_params = 'test.yml'
    )

    # Unit test
    var_list = sorted(task.get_vars().keys())

# Generated at 2022-06-13 09:30:42.319944
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.task import Task

    # Note that for this test, we assume we are using the legacy vars option
    # and that it does not need to be validated
    def mock_load_data(data, variable_manager=None, loader=None):
        '''
        Mock class to return the passed data
        '''
        task = Task()
        task.args = data

        return task

    # Setup the class
    ti = TaskInclude()
    ti.load_data = mock_load_data

    # Test invalid options
    data = dict(action='include', file='playbooks/something.yml', invalid_option=True)

# Generated at 2022-06-13 09:30:52.896114
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    task = TaskInclude()
    
    #Test 1 (minimal task)
    ds = {}
    task.preprocess_data(ds)
    assert ds == {}

    #Test2 (a full task)
    ds = {
        'action': 'include_role',
        'name': 'role_name',
        'dummy_test': 'dummy_test'
    }
    expected_ds = {
        'action': 'include_role',
        'name': 'role_name',
    }
    task.preprocess_data(ds)
    assert ds == expected_ds

    #Test3 (a full task with an invalid attribute)

# Generated at 2022-06-13 09:31:04.316894
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    '''
    This method is testing the build_parent_block of class TaskInclude
    '''
    # Please, don't change the following variables.
    # They are used for testing.
    # Modify 'apply_attributes' below if you want to test the method
    original_apply_attributes = {
        "when": "false",
        "block": [
            {
                "name": "test task 1",
                "when": "true"
            },
            {
                "name": "test task 2",
                "when": "false"
            }
        ]
    }

    # Change 'apply-attributes' below according to your need and run the test
    apply_attributes = original_apply_attributes

    # Uncomment the line below to simulate a TaskInclude object
    #included_object = TaskIn

# Generated at 2022-06-13 09:31:11.964446
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    from ansible.parsing.dataloader import DataLoader

    # test_TaskInclude_get_vars: test for 'include' action
    loader = DataLoader()
    t = TaskInclude.load(dict(action='include', src='foo.yaml'), loader=loader)
    # src will be in task.args as 'file' not 'src'
    t.args['file'] = 'foo.yaml'
    t.args['foo'] = 'bar'
    t.vars['baz'] = 'qux'
    x = t.get_vars()
    assert('foo' in x and x['foo'] == 'bar')
    assert('baz' in x and x['baz'] == 'qux')
    assert('tags' not in x)

    # test_TaskInclude_get_

# Generated at 2022-06-13 09:31:19.982499
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    from ansible.playbook.play import Play
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    options = {'verbosity': 0}
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources='')
    variable_manager = VariableManager(loader=loader, inventory=inventory)

# Generated at 2022-06-13 09:31:24.371955
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    task_include = TaskInclude()

    # empty task
    task = dict()
    task = task_include.check_options(task, task)
    assert set(task.keys()) == frozenset(('_raw_params',))  # static defaults

    task = {'action': 'include_role', 'file': 'foo'}

    # valid task, just apply is not yet a dict
    task = task_include.check_options(task, task)
    assert set(task.keys()) == frozenset(('file', '_raw_params', 'apply'))

    # apply is not a dict
    task['apply'] = "foo"
    try:
        task_include.check_options(task, task)
        assert False
    except AnsibleParserError:
        assert True

    # apply is a dict
    task

# Generated at 2022-06-13 09:31:37.219958
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    from unittest import TestCase, main
    from ansible.playbook.play import Play
    from ansible.playbook.role_include import RoleInclude
    from ansible.playbook.task_include import TaskInclude
    import ansible.playbook.task as task
    import ansible.playbook.block as block
    import ansible.playbook.role as role
    import ansible.inventory.group as group
    import ansible.inventory.host as host
    import ansible.vars.manager as varmanager
    import ansible.template as template
    import copy
    from units.mock.loader import DictDataLoader
    from units.mock.path import mock_unfrackpath_noop
    from units.mock.path import mock_unfrackpath_fail_on_frack_paths
   

# Generated at 2022-06-13 09:31:47.538548
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    # Simple action without any keyword
    check_preprocess_data(ds={}, exp={'action': 'include'})
    # With file
    check_preprocess_data(ds={'file': 'toto'}, exp={'action': 'include', 'file': 'toto'})
    # With _raw_params
    check_preprocess_data(ds={'_raw_params': 'toto'}, exp={'action': 'include', '_raw_params': 'toto'})
    # With file and _raw_params
    check_preprocess_data(ds={'file': 'toto', '_raw_params': 'titi'}, exp={'action': 'include', '_raw_params': 'titi'})

    # With file and a bunch of keywords (ignored)

# Generated at 2022-06-13 09:32:38.186089
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    from ansible.utils.sentinel import Sentinel

    # Mocked object
    class MockedTask:
        def __init__(self):
            self.args = dict()
            self.action = ''
    mock_task = MockedTask()

    # Mocked default attributes that are expected to be defined
    mock_action = 'import_tasks'
    mock_args = dict()
    mock_args['apply'] = dict()

    # Create mocked object
    mock_task.action = mock_action
    mock_task.args = mock_args

    # Create the object to be tested
    ti = TaskInclude()

    # Check that method returns the same object if no errors are found
    returned = ti.check_options(mock_task, None)
    assert mock_task is returned

    # Check for an error with an invalid option


# Generated at 2022-06-13 09:32:52.458159
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    '''
    Test for method preprocess_data of class TaskInclude
    '''
    # Test 1: action=include, no include_tasks keyword specifed
    # expected result: no change
    test_ds = dict(name="test",
                   action="include",
                   args=dict(a=1, b=2))
    task = TaskInclude()
    new_ds = task.preprocess_data(test_ds)
    assert new_ds == test_ds

    # Test 2: action=include, include_tasks keyword specified,
    # expected result: additional task added with include_tasks value
    test_ds = dict(name="test",
                   action="include",
                   include_tasks="somefile",
                   args=dict(a=1, b=2))
    task = TaskInclude()
   

# Generated at 2022-06-13 09:33:07.083865
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():

    class FakeBlock(object):
        def __init__(self):
            self.action = 'include_role'
        def _get_parent_attribute(self, attr, extend=False):
            if attr == '_role':
                return FakeRole()
    class FakeRole(object):
        def __init__(self):
            self.task_blocks = {'main': FakeBlock()}
    class FakePlay(object):
        def __init__(self):
            self.roles = []

    task = TaskInclude(block=FakeBlock())
    data = {'name': 'test', 'include': "{{ a }}"}

# Generated at 2022-06-13 09:33:10.741110
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    block = Block(task_include=None, parent_block=None)
    t = TaskInclude(block=block, role=None, task_include=None)
    t.vars = {'a': 'a'}
    t.args = {'b': 'b'}
    assert t.get_vars() == {'a': 'a', 'b': 'b'}



# Generated at 2022-06-13 09:33:22.340959
# Unit test for method load of class TaskInclude
def test_TaskInclude_load():
    # validate bad args
    ds = dict(action='include', args=dict(file='/foo/bar', foobar='baz'))
    ti = TaskInclude()
    try:
        ti.check_options(ti.load_data(ds), ds)
        assert False, 'TaskInclude.load() had not raised AnsibleParserError'
    except AnsibleParserError as e:
        assert str(e) == 'Invalid options for include: foobar'

    # validate that 'args' can be used for 'include'
    ds = dict(action='include', args=dict(file='/foo/bar', apply=dict(args=dict(a=1, b=2))))
    ti.check_options(ti.load_data(ds), ds)

    # validate that 'args' cannot be used otherwise
    d

# Generated at 2022-06-13 09:33:31.171627
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():

    # Create a dummy task and dummy block
    task = TaskInclude()
    block = Block()

    # Create the parent block
    parent_block = task.build_parent_block()
    # We should obtain a parent_block of class Block
    assert isinstance(parent_block, Block)

    # Add the parent block to the dummy task
    dummy_task = Task()
    with dummy_task.set_parent_block(parent_block):
        # If the parent block is set correctly, the dummy task should have a parent block
        assert dummy_task._parent == parent_block
        # and the dummy task should be part of it
        assert dummy_task in parent_block.block

    # Check if the parent block is correctly returned if there is no apply attribute
    task = TaskInclude(block=block)
    assert task.build_parent_block