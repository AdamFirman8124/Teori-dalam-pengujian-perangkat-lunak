

# Generated at 2022-06-13 09:23:47.118565
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    # AttributeError occurs when an object does not have an attribute.
    # So this exception is expected.
    def check_options_no_file(task):
        with pytest.raises(AttributeError):
            task.check_options({}, {})

    task = TaskInclude()

    # Valid include
    task.action = 'include'
    task.check_options({'_raw_params': 'include.yml'}, {})

    # Invalid include
    task.action = 'include'
    check_options_no_file(task)

    # Valid import_tasks
    task.action = 'import_tasks'
    task.check_options({'_raw_params': 'include.yml'}, {})

    # Invalid import_tasks
    task.action = 'import_tasks'
    check_options

# Generated at 2022-06-13 09:23:56.282856
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    display.warning = lambda msg: 'Warning: %s' % msg
    display.error = lambda msg: 'Error: %s' % msg

    # Create a TaskInclude without fail_on_invalid_task_attributes
    ti = TaskInclude()
    ti.action = 'include'
    ds = {'action': 'include', 'ignore_errors': True, 'new_attribute': 'True', 'file': 'file.yml'}

    # Check that new_attribute is deleted, warning is returned and action is changed
    assert ds['action'] == 'include'
    assert 'new_attribute' in ds.keys()
    assert display.warning.call_count == 0
    ds = ti.preprocess_data(ds)
    assert ds['action'] == 'include_tasks'

# Generated at 2022-06-13 09:24:01.373171
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():

    tasks_iterator = iter([
        {
            'include_role': {'name': 'rolename'},
        },
        {
            'include_tasks': {'name': 'tasksname'},
        },
        {
            'import_tasks': {'name': 'tasksname'},
        },
        {
            'import_playbook': {'name': 'tasksname'},
        },
    ])

    class FakeLoader:
        def __init__(self):
            self.task_cache = {}
            self.add_task('rolename', tasks_iterator)

        def add_task(self, name, task):
            if name not in self.task_cache:
                self.task_cache[name] = task


# Generated at 2022-06-13 09:24:08.836792
# Unit test for method load of class TaskInclude
def test_TaskInclude_load():
    # Import test data
    import os
    import tempfile
    import yaml
    _test_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../unit/test_data')
    with open(os.path.join(_test_dir, 'test_playbook_include_with_apply.yml'), 'r') as test_play:
        test_data = yaml.safe_load(test_play)
    test_playbook = Block.load(test_data)
    test_play = next(iter(test_playbook.get_plays().values()))
    test_tasks = test_play.compile()
    test_task = next(iter(test_tasks.values()))
    # End of import test data

    # Test with no apply attribute


# Generated at 2022-06-13 09:24:20.476379
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    import ansible.playbook.play
    from ansible.playbook.block import Block
    from ansible.playbook.role.include import RoleInclude
    from ansible.playbook.task import Task
    from ansible.plugins.loader import plugin_loader

    current_dir = './tests/'
    vars_file = "test_include_module_vars_file"
    include_file = "test_include_module_vars_file_include.yml"
    mock_loader, mock_inventory, mock_variable_manager = plugin_loader.load_plugins(playbook_basedir=current_dir)

# Generated at 2022-06-13 09:24:31.082583
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    import ansible.playbook.role
    import ansible.playbook.task
    import ansible.playbook.play
    import ansible.playbook.block

    my_task_block = ansible.playbook.block.Block()
    my_task_block._role = ansible.playbook.role.Role()
    my_task_block._play = ansible.playbook.play.Play()
    my_task_block._play.vars = {'various': 'vars'}

    my_task = ansible.playbook.task.Task()
    my_task._parent = my_task_block
    my_task.vars = {'task': 'vars'}

    my_ti = TaskInclude()
    my_ti.action = 'include'
    my_ti._parent = my_task

# Generated at 2022-06-13 09:24:43.489911
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    display = Display()
    display.verbosity = 3
    ds = dict(action='include', args=dict(file='/tmp/file.yml'), rc=0, changed=False)
    task = TaskInclude()
    new_ds = task.preprocess_data(ds)
    assert 'args' in new_ds
    assert len(new_ds.keys()) == 3
    assert new_ds['action'] == 'include'
    assert new_ds['rc'] == 0
    assert new_ds['changed'] == False
    ds = dict(action='import_tasks', args=dict(file='/tmp/file.yml'), rc=0, changed=False)
    task = TaskInclude()
    new_ds = task.preprocess_data(ds)
    assert 'args' in new_ds

# Generated at 2022-06-13 09:24:56.264245
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    from ansible.playbook import Play
    from ansible.playbook.task import HandlerTaskInclude

    for action in C._ACTION_ALL_PROPER_INCLUDE_IMPORT_TASKS:
        task = TaskInclude()
        task.action = action
        task.args = {'_raw_params': ''}
        task.check_options(task, {})

    # Invalid options
    task = TaskInclude()
    task.action = 'include'
    task.args = {'_raw_params': '', 'bad_opt': ''}
    with pytest.raises(AnsibleParserError):
        task.check_options(task, {})

    # Valid options
    task = TaskInclude()
    task.action = 'include'

# Generated at 2022-06-13 09:25:07.030660
# Unit test for method check_options of class TaskInclude

# Generated at 2022-06-13 09:25:19.494307
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext

    class TaskIncludeForTest(TaskInclude):
        def __init__(self):
            self._role = None
            self._parent = Play()
            self._play = Play()
            self._loader = None
            self._variable_manager = None
            self.args = {}

    task_include = TaskInclude()
    task_include.args = {'apply': {'block': []}}
    parent_block = task_include.build_parent_block()
    assert parent_block.__class__.__name__ == 'Block'

    task_include = TaskInclude()
    parent_block = task_include.build_parent_block()

# Generated at 2022-06-13 09:25:33.498488
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    from ansible.playbook.handlertask import HandlerTaskInclude
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText

    # TaskInclude check_options
    # No issues
    ti = TaskInclude()
    task = dict(
        action="include",
        args=dict(
            file="../path/to/file.yml",
            _raw_params="../path/to/file.yml",
        ),
    )
    assert ti.check_options(task, dict()) is task
    assert task == dict(
        action="include",
        args=dict(
            _raw_params="../path/to/file.yml",
        ),
    )

    # No 'file' specified when action is include
    ti = TaskInclude()
    task = dict(action="include")
   

# Generated at 2022-06-13 09:25:43.723007
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    module = AnsibleModule(argument_spec={'content': dict(type='str', required=True)})
    result = module.run_command(['ansible-playbook', '--syntax-check', module.params['content']])
    if result[0] == 0:
        module.exit_json(changed=False)
    else:
        error_msg = result[1].split("\n")[0]
        module.fail_json(msg=error_msg, changed=False)

# Generated at 2022-06-13 09:25:53.077660
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    block = Block()
    task = TaskInclude(block=block)

    task.vars = {'abc': 'def'}
    if task.action in C._ACTION_INCLUDE:
        assert task.get_vars() == {'abc': 'def'}
    else:
        assert task.get_vars() == {}

    task.args = {'arg1': 'value1', 'arg2': 'value2'}
    if task.action in C._ACTION_INCLUDE:
        assert task.get_vars() == {'abc': 'def', 'arg1': 'value1', 'arg2': 'value2'}
    else:
        assert task.get_vars() == {'abc': 'def'}


# Generated at 2022-06-13 09:25:59.505572
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.playbook.block import Block

    # test without include
    preprocessed = TaskInclude.preprocess_data({'action': 'meta'})
    assert preprocessed == {'action': 'meta'}

    # test with action = include
    preprocessed = TaskInclude.preprocess_data({'action': 'include', 'include': 'foo.yml'})
    assert preprocessed == {'action': 'include', 'include': 'foo.yml'}

    # test with action = import_tasks
    preprocessed = TaskInclude.preprocess_data({'action': 'import_tasks', 'include': 'foo.yml'})

# Generated at 2022-06-13 09:26:10.886642
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    task = TaskInclude(None)
    # raise error if both params 'file' and '_raw_params' are provided in args
    args = {'file': 'a', '_raw_params': 'b'}
    data = 'test'
    for action in ('include', 'include_role'):
        task.action = action
        try:
            task.check_options(task, data)
            assert False
        except AssertionError:
            raise
        except AnsibleParserError as ae:
            assert ae.message == 'Invalid options for include: _raw_params'
        task.args.clear()

    # raise error if apply is provided but task.action is not in C._ACTION_INCLUDE_TASKS
    task.action = 'import_tasks'

# Generated at 2022-06-13 09:26:18.314917
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    from ansible.playbook.task_include import TaskInclude


# Generated at 2022-06-13 09:26:27.184015
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    task = TaskInclude()
    task.args = {
        'other_args': 'other_args_value',
        'apply': {
            'other_attrs': 'other_attrs_value',
            'block': [],
        },
    }
    task._parent = '_parent_value'
    task._role = '_role_value'
    task._variable_manager = '_variable_manager_value'
    task._loader = '_loader_value'

    p_block = task.build_parent_block()
    # Validate the returned object is a Block and the object.args contains the 'apply' args
    assert isinstance(p_block, Block)
    assert p_block.args == {'other_attrs': 'other_attrs_value'}

    # Validate that the caller object is not

# Generated at 2022-06-13 09:26:37.336631
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
  # test case 01
  ds = dict(action='include', file='XXXX')
  dds = dict(action='include', file='XXXX')

  ti = TaskInclude()
  ti.args = ds
  ti.action = 'include'
  ti.vars = dds
  r = ti.get_vars()
  assert r == ds, 'TaskInclude.get_vars unit test failed.'


  # test case 02
  ds = dict(action='include', file='XXXX')
  dds = dict(action='include', file='XXXX')

  ti = TaskInclude()
  ti.args = ds
  ti.action = 'include'
  ti.vars = dds
  ti._parent = TaskInclude()

# Generated at 2022-06-13 09:26:51.071191
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    from ansible.playbook.play import Play
    from ansible.playbook.role import Role
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    import ansible.utils.vars as vars

    play_vars = vars(Play())
    loader_vars = vars(Role())
    variable_manager = vars(Block())

    play_ds = {'hosts': 'all'}
    loader_ds = {'include': 'include_file.yaml'}
    block_ds = {'hosts': 'all'}

    play = Play.load(
        play_ds,
        variable_manager=variable_manager,
        loader=loader_vars
    )


# Generated at 2022-06-13 09:26:54.890071
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    data = dict(
        apply = dict(
            block = dict(
                name = 'Build',
            ),
        )
    )
    t = TaskInclude()
    tb = t.build_parent_block()
    assert isinstance(tb, Block)
    assert tb.name == 'Build'
    assert tb.action == 'block'

# Generated at 2022-06-13 09:27:05.686743
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    from ansible.playbook.play import Play

    play = Play.load(dict(
        name="play",
        hosts=['abc'],
        gather_facts='no',
        connection='local',
        roles=["my_role"],
    ), variable_manager=None, loader=None)

    tasks = [{
        'include': './data/bar.yml',
        'vars': {
            'a': 1,
        },
    }]
    block = Block.load({'task': tasks}, play=play, variable_manager=None, loader=None)
    task = TaskInclude.load(tasks[0], block=block, variable_manager=None, loader=None)


# Generated at 2022-06-13 09:27:13.685072
# Unit test for method load of class TaskInclude
def test_TaskInclude_load():
    task = TaskInclude.load(
        dict(
            apply=dict(block=[]),
            file='/tmp/test.yml',
            name='test',
        )
    )
    assert task.get_name() == 'test'
    assert 'name' in task.vars
    assert task.args['apply'] == {}
    assert task.args['file'] == '/tmp/test.yml'
    assert task.action == 'include'

    task = TaskInclude.load(
        {'include': 'file=/tmp/test.yml'}
    )
    assert 'file' in task.args
    assert task.args['file'] == '/tmp/test.yml'
    assert task.action == 'include'


# Generated at 2022-06-13 09:27:18.630004
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    tih = TaskInclude()
    ds = dict(action='include_role')
    ds = tih.preprocess_data(ds)
    assert 'include_role' == ds['action']

    ds = dict(action='include_role', abc='xyz')
    ds = tih.preprocess_data(ds)
    assert 'xyz' != ds['abc']

# Generated at 2022-06-13 09:27:27.668569
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():

    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.block import Block
    from ansible.playbook.task_include import TaskInclude
    from ansible.plugins.loader import include_role_tasks_loader
    import ansible.constants as C

    # create a play context
    play_context = PlayContext()
    play_context._shell = None
    play_context._connection = None
    play_context._play = None
    play_context._loader = None
    play_context._variable_manager = None
    play_context._stdin_path = None
    play_context.network_os = None
    play_context.remote_addr = None
    play_context.password = None
    play_context.port = None
   

# Generated at 2022-06-13 09:27:38.669053
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    import random

    def gen_task():
        task = dict(action='random_action')

        rand_num = random.randint(0, 10)
        if rand_num == 0:
            task["apply"] = dict()
        elif rand_num == 1:
            task["apply"] = dict(action=['some_action'])
        else:
            task["apply"] = dict(action=['some_action'], arg1=random.randint(0, 10), arg2=random.randint(0, 10))

        # Random number of optional args
        for i in range(0, random.randint(0, 10)):
            key = "arg%d" % i
            task[key] = random.randint(0, 10)

        return task

    # Generate random number of tasks
    num_items

# Generated at 2022-06-13 09:27:50.519510
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():

    class loader(object):
        ''' fake loader class '''
        def __init__(self):
            self.path_finder = DummyPathFinder()

    class DummyPathFinder(object):
        ''' fake path_finder class '''
        def find_file_in_search_path(self, path, game):
            return True

    class DummyTask(object):
        ''' fake task class '''
        def __init__(self, args):
            self.args = args

    class DummyVariableManager(object):
        ''' fake variable_manager class '''
        def __init__(self):
            self.extra_vars = dict()
            self.options = dict()

    # Create a TaskInclude class object
    task_include = TaskInclude()

    # Create a loader class object
    loader

# Generated at 2022-06-13 09:28:03.531063
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    import datetime
    t1 = datetime.time()
    t2 = datetime.time()
    f1 = datetime.time()

    # Testing the default behavior
    ds = {
        "include": t1,
        "static": t2,
        "static_with_vars": t2,
        "include_tasks": t2,
        "import_tasks": t2,
        "import_role": t2
    }
    ti = TaskInclude(None)

    d = ti.preprocess_data(ds)
    assert d is ds
    assert 'include' in ds
    assert 'static' not in ds
    assert 'static_with_vars' not in ds
    assert 'include_tasks' not in ds
    assert 'import_tasks' not in d

# Generated at 2022-06-13 09:28:14.836928
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    from ansible.playbook.role import Role
    from ansible.playbook.play import Play
    from ansible.playbook.block import Block
    from ansible.utils.sentinel import Sentinel
    from ansible.executor.task_result import TaskResult
    from ansible.inventory.host import Host
    from ansible.vars.manager import VariableManager
    from collections import namedtuple

    class MockLoader:
        pass

    class MockDataLoader:
        pass

    class MockVariableManager:
        pass

    class MockPlay:
        def __init__(self, _hosts_pattern):
            self._hosts_pattern = _hosts_pattern
            self._variable_manager = MockVariableManager()
            self.notified_handlers = dict()
            self.tags = None
            self.post_validate = None

# Generated at 2022-06-13 09:28:25.278667
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    ds = {
        "action": "include",
        "file": "somefile",
        "args": {
            "foo": "bar",
            "apply": {},
            "baz": "foo",
        },
    }

    task = TaskInclude(block=None, role=None, task_include=None)
    task = task.check_options(task.load_data(ds), ds)

    # Action is fixed to 'include'
    assert task.action == 'include'
    # 'baz' is not a valid arg but it should not raise an exception because
    # 'include' is one of the valid action to accept invalid args
    assert 'baz' in task.args
    # 'apply' is a valid arg but it is not accepted by 'include'
    assert 'apply' not in task.args


# Generated at 2022-06-13 09:28:32.035726
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    '''
    Method get_vars of class TaskInclude is used to return the variables to
    use as arguments when a role/import_playbook/etc is included.
    This unit test validates the behaviour of get_vars.
    :return:
    '''
    from ansible.playbook.base import Base

    class TaskInclude2(TaskInclude):
        _base_class = Base

    import ansible.playbook.base as base

    class Block2(Block):
        _task_class = TaskInclude2

    import ansible.template as template
    from ansible.vars.manager import VariableManager

    class Play2(base.Base):
        _ROLE_CACHE = template.role_cache

        def __init__(self):
            pass


# Generated at 2022-06-13 09:28:43.959871
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    task_ds = {
        'include': 'df.yml',
    }
    task = TaskInclude.load(data=task_ds)
    assert task.args['_raw_params'] == 'df.yml'
    assert not task.args.get('apply')

    task_ds = {
        'include_tasks': 'df.yml',
        'apply': '{"a": 1}',
    }
    task = TaskInclude.load(data=task_ds)
    assert task.args['_raw_params'] == 'df.yml'
    assert not task.args.get('apply')

    task_ds = {
        'import_playbook': 'df.yml'
    }
    task = TaskInclude.load(data=task_ds)

# Generated at 2022-06-13 09:28:50.447449
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    '''Test the method check_options of class TaskInclude. The validations performed in
    the method are necessary but since they can change over time due to the inclusion
    of new options, it is necessary to unit test them to avoid regressions.'''
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.block import Block
    ti = TaskInclude(block=Block())
    # Test invalid options for include tasks
    task = ti.check_options(
        {'action': 'include', 'foo': 'bar', 'args': {'_raw_params': 'foo'}},
        {'action': 'include', 'foo': 'bar'}
    )
    assert task == {'action': 'include', 'args': {'_raw_params': 'foo'}}
    task = ti.check_options

# Generated at 2022-06-13 09:29:01.424597
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():

    class MockTask(object):
        def __init__(self, vars):
            self.vars = vars

        def get_vars(self):
            return self.vars

    class MockBlock(object):
        def __init__(self, vars):
            self.vars = vars
            self._parent = None

        def get_vars(self):
            return self.vars

    class MockRole(object):
        def __init__(self, vars):
            self.vars = vars
            self.name = 'role'

        def get_vars(self):
            return self.vars


    # test get_vars for action 'include'
    # include_tasks: my_task
    # parent_block.vars:
    #   - 'foo': 'bar'

# Generated at 2022-06-13 09:29:15.337837
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins.loader import get_all_plugin_loaders

    loader, ps = get_all_plugin_loaders()

    ti = TaskInclude()
    ti._parent = Block()
    ti._parent._play = {}  # play object is required
    ti._variable_manager = PlayContext()

    res = ti.build_parent_block()
    assert(res == ti)

    ti.args['apply'] = {'other': 'arg'}
    res = ti.build_parent_block()
    assert(res != ti)
    assert(isinstance(res, Block))
    assert(res._parent._role == res)
    assert(res.other == 'arg')

# Generated at 2022-06-13 09:29:24.599533
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    my_task_include = TaskInclude()

    # Case of "Empty apply data"
    apply_attrs = {}
    my_task_include.args['apply'] = apply_attrs
    try:
        my_task_include.build_parent_block()
        assert True, "Should not raise an exception"
    except:
        assert False, "Should not raise an exception"

    # Case of "Non empty apply data"
    apply_attrs = {
        'block': [],
        'name': 'my_task_include',
        'other_apply_attr': 'other_apply_attr',
        'tags': ['other_apply_attr'],
        'when': 'other_apply_attr'
    }
    my_task_include.args['apply'] = apply_attrs

# Generated at 2022-06-13 09:29:31.846917
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    '''
    Unit test for method TaskInclude.check_options
    '''
    # setup
    class TestOptions:
        def __init__(self, **kwds):
            self.__dict__.update(kwds)
    task_include = TaskInclude()
    test_data = dict()

    # test -- action not in C._ACTION_ALL_PROPER_INCLUDE_IMPORT_TASKS
    test_task = TestOptions(action='test', args=dict(test1='one', test2='two'))
    result_task = task_include.check_options(test_task, test_data)
    assert test_task == result_task

    # test -- action in C._ACTION_ALL_PROPER_INCLUDE_IMPORT_TASKS

# Generated at 2022-06-13 09:29:40.837610
# Unit test for method load of class TaskInclude
def test_TaskInclude_load():
    from ansible.plugins.loader import action_loader
    import ansible.playbook.task
    import ansible.playbook.role
    loader  = action_loader.ActionModuleLoader()
    task_include = TaskInclude()

    # test for valid data
    data = dict(
        action = 'include_role',
        name   = 'name',
        apply  = dict(first = 1),
    )
    task = task_include.load(data, task_include=task_include, loader=loader)
    assert isinstance(task, ansible.playbook.task.TaskInclude)
    assert 'name' == task.name
    assert 'apply' in task.args
    assert isinstance(task.args['apply'], dict)
    assert 'first' in task.args['apply']
    assert 1 == task.args

# Generated at 2022-06-13 09:29:48.836779
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():

    from ansible.playbook.play_context import PlayContext

    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    variable_manager = VariableManager()
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=['localhost'])
    variable_manager.set_inventory(inventory)

    variable_manager._fact_cache['ansible_system'] = 'Linux'
    variable_manager._fact_cache['ansible_foo'] = 5

    t_include = TaskInclude()

    # Validation of 'file' attribute
    data_1 = TaskInclude.load({'action': 'include', 'file': 'foo_group.yml'}, variable_manager=variable_manager, loader=loader)

# Generated at 2022-06-13 09:29:58.581333
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    # Create root task
    root_task = TaskInclude(block=Block(), role=None, task_include=None)
    # prepare vars for root task
    root_task._parent = root_task
    root_task.vars = dict(
        a="a",
        b="b"
    )
    root_task.args = dict()

    # Create regular task
    task = TaskInclude(block=Block(), role=None, task_include=None)
    # Prepare vars for regular task
    task._parent = root_task
    task.vars = dict(
        c="c",
        d="d"
    )
    task.args = dict()

    assert task.get_vars() == dict(a='a', b='b', c='c', d='d')

    # Create include task


# Generated at 2022-06-13 09:30:07.344930
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    import ansible.playbook.block as block
    import ansible.playbook.role.include as role_include

    # Helper function for populating the task's args
    def populate_task(task_args):
        task_args["_raw_params"] = task_args.pop("file", None)
        task_args["apply"] = task_args.pop("apply", {})
        return task_args

    # Testcase 1: apply not specified
    test_args = {"file":"test.yml"}
    my_include = TaskInclude()
    my_include.args = populate_task(test_args)
    assert my_include.build_parent_block() == my_include

    # Testcase 2: apply specified. checking the attrs are set properly on the returned parent block

# Generated at 2022-06-13 09:30:28.213896
# Unit test for method check_options of class TaskInclude

# Generated at 2022-06-13 09:30:39.656955
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    class TaskLoader:
        @staticmethod
        def load_from_file(*args, **kwargs):
            raise AnsibleParserError('This is a test')

    class HandlerTaskInclude(TaskInclude):
        def __init__(self, *args, **kwargs):
            super(HandlerTaskInclude, self).__init__(*args, **kwargs)

        def _load_task_from_file(self, ds, task_ds, parent_block, play=None, variable_manager=None, loader=None):
            return Task.load(ds, block=parent_block, play=play, variable_manager=variable_manager, loader=loader)

        def load_data(self, ds, variable_manager=None, loader=None):
            task_ds = self._load_task_ds(ds, loader)
           

# Generated at 2022-06-13 09:30:48.688679
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    from ansible.playbook.play import Play
    from ansible.playbook.role import Role
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.vars.manager import VariableManager

    # Create a play

# Generated at 2022-06-13 09:30:57.160270
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    # pylint: disable=R0915

    # test 'load' method
    taskvars = dict(foo='bar')
    def get_variable_manager(hostvars={}, *args, **kwargs):
        return namedtuple('MockVariableManager', 'extra_vars')(taskvars)

    def get_loader(*args, **kwargs):
        return namedtuple('MockLoader', 'get_real_file')('loader')

    def get_block(name='block'):
        return namedtuple('MockBlock', 'name')(name)

    def get_role(name='role', collection='collection'):
        return namedtuple('MockRole', 'name, collection')(name, collection)


# Generated at 2022-06-13 09:31:06.971746
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    test_task_include = TaskInclude()
    test_task_include.args = { "arg1": "val1", "arg2": "val2" }
    assert test_task_include.get_vars() == { "arg1": "val1", "arg2": "val2" }, "Unexpected get_vars result"

    test_task_include.action = "import_tasks"
    assert test_task_include.get_vars() == { "arg1": "val1", "arg2": "val2" }, "Unexpected get_vars result"

    test_task_include.action = "include_role"
    test_task_include.vars = { "var1": "val1", "var2": "val2" }

# Generated at 2022-06-13 09:31:17.271324
# Unit test for method load of class TaskInclude
def test_TaskInclude_load():
    # Setup
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.task import Task

    # Test 1
    # Inputs
    data = {'action': 'include', 'file': 'test.yaml'}
    block = 'not None'
    role = None
    task_include = None
    variable_manager = None
    loader = None
    # Return value
    test_1_result = TaskInclude(block='not None', task_include=None, role=None)
    test_1_result.statically_loaded = False
    test_1_result.action = 'include'
    test_1_result.args = {'file': 'test.yaml', '_raw_params': 'test.yaml'}

    # Test 2
    # Inputs
    data

# Generated at 2022-06-13 09:31:29.308176
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from ansible.vars.unsafe_proxy import AnsibleUnsafeVars
    from ansible.vars.hostvars import HostVars
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task

    # initialize
    play = Play().load(dict(
        name = "Ansible Play",
        hosts = 'all',
        roles = [],
        tasks = [dict(
            include='foo.yml',
        )]
    ))

    play._variable_manager = VariableManager()
    play.post_validate(play._ds, play)
    play._variable_manager.set_

# Generated at 2022-06-13 09:31:36.247174
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    # Basic
    ti = TaskInclude(None)
    ti.args = {"apply": {}}
    p_block = ti.build_parent_block()
    assert ti is not p_block
    assert p_block.block == []

    # Advanced with assign
    ti = TaskInclude(None)
    ti.args = {"apply": {"block": []}}
    p_block = ti.build_parent_block()
    assert ti is not p_block
    assert p_block.block == []
    assert p_block.always == []
    assert p_block.rescue == []
    assert p_block.when == []
    assert p_block.anything_else == []

    # Advanced with attribute
    ti = TaskInclude(None)
    ti.args = {"apply": {"when": "some_when"}}
   

# Generated at 2022-06-13 09:31:41.027284
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    # Example 1: Build a parent block for a task without 'apply'
    play_data = {
        'name': 'no apply',
        'hosts': 'all',
        'serial': '1',
        'tasks': [
            {'name': 'task with no parent block'},
        ],
    }

    play = Play.load(play_data)
    block = play._get_block_list()[0]
    task = block._get_task_list()[0]
    p_block = task.build_parent_block()
    assert p_block == task
    assert p_block.parent is None
    assert p_block.block is None

    # Example 2: Build a parent block for a task with 'apply' but without tasks

# Generated at 2022-06-13 09:31:49.405774
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    ti = TaskInclude()
    ds_test_1 = {'action': 'include'}
    ds_test_2 = {'action': 'include', 'x': 1}

    # Normal execution without exception
    ds = ti.preprocess_data(ds_test_1)
    assert ds == {'action': 'include'}

    # Exception for unknown attribut for specific action in 'include'
    try:
        ds = ti.preprocess_data(ds_test_2)
    except AnsibleParserError:
        assert True
    else:
        assert False


# Generated at 2022-06-13 09:32:16.248287
# Unit test for method load of class TaskInclude
def test_TaskInclude_load():
    from ansible.playbook.play_context import PlayContext
    import ansible.playbook.block as block
    import ansible.playbook.task as task

    ctx = PlayContext()
    ctx._role = block.Role()
    ctx._task = task.Task()
    ctx._task._role = ctx._role
    my_task = TaskInclude.load({'include': 'some_file.yaml'}, block=ctx, task_include=ctx._task)
    assert my_task._parent.block is ctx
    assert my_task.block is ctx

    my_task = TaskInclude.load({'include': 'some_file.yaml', 'name': 'my name', 'when': 'true'}, block=ctx, task_include=ctx._task)

# Generated at 2022-06-13 09:32:23.286933
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    ti = TaskInclude()
    ti.vars = dict(a=1)
    ti.args = dict(b=2)
    assert ti.get_vars() == dict(a=1, b=2)

    ti = TaskInclude()
    ti.vars = dict(a=1)
    ti.args = dict(b=2, tags=['a'])
    assert ti.get_vars() == dict(a=1, b=2)

# Generated at 2022-06-13 09:32:30.598524
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    from ansible.playbook import Play
    from ansible.playbook.play import Play as PlayObject
    from ansible.playbook.helpers import load_list_of_blocks

    loader = object()
    variable_manager = object()
    play = Play()

# Generated at 2022-06-13 09:32:36.800973
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    from ansible.playbook.role_include import IncludeRole
    import ansible.playbook.role

    ir = IncludeRole([])
    ir.args = {
        'file': '',
        'vars': {
            'myvar': 'myval'
        }
    }

    my_role = ansible.playbook.role.Role()
    my_role.get_vars = lambda: {
        'myivar': 'myival'
    }

    ir.post_validate(caller=my_role)

    ansible.playbook.role._Role = my_role

    assert ir.get_vars() == {
        'myvar': 'myval',
        'myivar': 'myival'
    }

    ir.action = 'import_role'

    assert ir.get_v

# Generated at 2022-06-13 09:32:43.467594
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():

    import ansible.playbook.block
    from copy import copy
    from ansible.utils.display import Display

    display = Display()

    class FakeTask():
        def __init__(self, args=None, parent=None, role=None, play=None, loader=None):
            self._parent = parent
            self.args = args
            self._play = play
            self._role = role
            self._loader = loader
            self._variable_manager = None

            display.display("Created fake task: %s" % self)
        
        def __repr__(self):
            return "<FakeTask(args=%s, parent=%s)" % (self.args, self._parent)


# Generated at 2022-06-13 09:32:54.883280
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    import ansible.playbook
    import ansible.playbook.play
    import ansible.playbook.task

    playbook_name = 'task_include_playbook'
    playbook_path = 'task_include_playbook.yml'
    extra_vars = {
        'var1': 'value1',
        'var2': 'value2',
        'var3': 'value3',
    }
    connection = 'local'

# Generated at 2022-06-13 09:33:09.301325
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():

    class FakeTask(TaskInclude):
        def __init__(self, ti):
            super(FakeTask, self).__init__(block=None, role=None, task_include=ti)

    from ansible.vars import VariableManager
    from ansible.utils.vars import combine_vars
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext
    from ansible.inventory.manager import InventoryManager

    loader = DataLoader()
    variable_manager = VariableManager()
    variable_manager._fact_cache = {'_ansible_no_log': True}
    inventory = InventoryManager(loader=loader, sources=None)

    class FakeOptions(object):
        forks = 10
        become_user = None
        become_method = None
       

# Generated at 2022-06-13 09:33:20.966619
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    def do_test(data, expected):
        task = TaskInclude()
        task = task.check_options(task.load_data(data), data)
        for key in expected:
            assert task.args[key] == expected[key], "'%s' differs from expected" % key


# Generated at 2022-06-13 09:33:29.912798
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    # Create TaskInclude object
    task_include = TaskInclude()
    task_include.action = 'include'
    task_include.args = {'tags': 'tag1', 'when': 'when1', 'include_var1': 'value1'}
    # Test TaskInclude.get_vars
    vars = task_include.get_vars()
    assert vars == {'tags': 'tag1', 'when': 'when1', 'include_var1': 'value1'}, 'TaskInclude.get_vars: TaskInclude.get_vars return value does not match expectation'
    # Create TaskInclude object
    task_include = TaskInclude()
    task_include.action = 'include_role'

# Generated at 2022-06-13 09:33:32.484951
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    task = {'apply': {'when': 'test'}}
    ti = TaskInclude(task=task)
    assert ti.build_parent_block() is task