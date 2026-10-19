

# Generated at 2022-06-13 09:23:52.203257
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    # Unit test for method preprocess_data of class TaskInclude

    def assert_task_invalid_option(task, option, data):
        with pytest.raises(AnsibleParserError) as exc:
            task.preprocess_data(data)
        assert "Invalid options for %s: %s" % (task.action, option) in str(exc.value)

    # Invalid options for action 'import_playbook'
    ti = TaskInclude()
    ti.action = 'import_playbook'
    data = dict(silly_option=42)
    assert_task_invalid_option(ti, 'silly_option', data)

    data = dict(apply='silly')
    assert_task_invalid_option(ti, 'apply', data)

    # Invalid options for action 'import_tasks'

# Generated at 2022-06-13 09:23:59.248246
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=['hosts'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    # Simple case
    task_include = TaskInclude.load(
        {
            'file': 'some_file',
            'another_attr': 'some_attr'
        },
        loader=loader,
        variable_manager=variable_manager
    )

    assert task_include.args == {
        '_raw_params': 'some_file'
    }

    # 'apply' is an attribute and not recognized as valid for an 'import_role' task
    task_include

# Generated at 2022-06-13 09:24:14.088190
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    import tempfile
    from ansible.galaxy.role import RoleRequirement

    ti = TaskInclude()
    ti.action = 'include'
    ti.args = {"test": "this"}
    ti.vars = {"test1": "that"}

    ti1 = TaskInclude()
    ti1.action = 'include_role'
    ti1.args = {"test": "this"}
    ti1.vars = {"test1": "that"}
    ti1.role = RoleRequirement("test_role")

    # This simulates a handler task include, but not the exact one
    # since HandlerTaskInclude derives from Task.
    ti2 = TaskInclude()
    ti2.action = 'notify'
    ti2.args = {"test": "this"}

# Generated at 2022-06-13 09:24:23.051296
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.role_include import IncludeRole
    from ansible.playbook.play import Play

    n_play = Play().load({
        'name': 'foobar',
        'hosts': 'localhost',
        'gather_facts': False,
        'tasks': [
            {
                'include_role': {
                    'name': 'bar',
                    'apply': {
                        'ignore_errors': True,
                        'collections': ['foo.bar'],
                        'when': True,
                        'tags': ['foo'],
                    }
                }
            }
        ]
    }, variable_manager=None, loader=None)

    n_play.post_validate(PlayContext())

    n_block = n_play.get_

# Generated at 2022-06-13 09:24:34.720957
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.unsafe_proxy import UnsafeProxy

    from ansible.playbook.play import Play

    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block

    variable_manager = VariableManager()
    loader = DataLoader()
    variable_manager.set_loader(loader)
    variable_manager.extra_vars = {'baz': 'foo'}


# Generated at 2022-06-13 09:24:45.468511
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    class MockBlock(object):
        def __init__(self, vars):
            self.vars = vars

        def get_vars(self):
            return self.vars

    class MockPlay(object):
        def __init__(self, vars):
            self.vars = vars

        def get_vars(self):
            return self.vars

    class MockRole(object):
        def __init__(self, vars):
            self.vars = vars

        def get_vars(self):
            return self.vars


# Generated at 2022-06-13 09:24:53.790467
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    task = TaskInclude()

    import yaml
    ds = yaml.full_load('''
    - include: tasks.yaml
      ignore_errors: true
      when: not skip
    ''')
    ds = ds[0]

    ds = task.preprocess_data(ds)

    assert ds['action'] == 'include'
    assert 'ignore_errors' in ds
    assert ds.get('when') == 'not skip'

# Generated at 2022-06-13 09:25:03.176814
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    display.verbosity = 3
    task_include = TaskInclude()
    task = Task()
    # Test that we get a KeyError when handling 'apply' and action is not in INCLUDE_TASKS
    task.action = 'action'
    task.args = {'apply': {}}
    try:
        # _validate_apply_vars() is not called because action is not in INCLUDE_TASKS
        task_include.check_options(task, {})
    except AnsibleParserError:
        pass
    # Test that we get an AnsibleParseError when a bad opt is used
    task.action = 'include'
    task.args = {'invalid_opt': 'blabla'}

# Generated at 2022-06-13 09:25:11.011717
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    task = TaskInclude()

    # This unit test only check for the changes made to the input dict.
    # It does not check for the transformations that are silently
    # applied to param 'include'.
    # It also doesn't check for the new attribute ``statically_loaded``

    # 'include' is a valid attribute only with the task `include`
    # while `role` and `import_role` are valid with other tasks.
    # This test ignores the 'include' attribute since it is handled by
    # the static tasks loader.
    d1 = dict(name='test1', include='test1', action='role')
    o1 = dict(name='test1', action='role')
    task.preprocess_data(d1)
    assert d1 == o1


# Generated at 2022-06-13 09:25:21.675918
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.role.requirement import RoleRequirement

    play_context = {
        'diff': False,
        'forks': 10,
        'become': False,
        'become_method': None,
        'become_user': None,
        'check_mode': False,
        'remote_addr': '127.0.0.1',
        'remote_user': 'ansiballz',
        'verbosity': 0,
    }
    block_vars = {'foo': 'bar', 'baz': 'qux'}

# Generated at 2022-06-13 09:25:36.677968
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    task = TaskInclude()
    task.action = 'include_role'
    task.set_loader(None)
    task.vars = dict(ansible_os_family='Windows')
    task.args = dict(name='Some_role')
    task.vars.update(task.args)
    assert(task.get_vars() == dict(ansible_os_family='Windows', name='Some_role'))
    task.action = 'import_role'
    task.args = dict(name='Some_role')
    task.vars.update(task.args)
    assert(task.get_vars() == dict(ansible_os_family='Windows', name='Some_role'))
    task.action = 'include'
    task.args = dict(name='Some_role')
    task.v

# Generated at 2022-06-13 09:25:45.144018
# Unit test for method load of class TaskInclude
def test_TaskInclude_load():
    """
    Unit test for method load of class TaskInclude
    """
    block = Block()
    role = None
    task_include = None
    data = {'action': 'include', 'file':'examples/test.yml'}
    variable_manager = None
    loader = None
    task = TaskInclude.load(data, block, role, task_include, variable_manager, loader)
    assert task.action == 'include'
    assert task._attributes.get('file').value == 'examples/test.yml'
    assert task.statically_loaded == False

# Generated at 2022-06-13 09:25:54.374927
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    ds_dict = {}
    task_include = TaskInclude()
    display.display(task_include.preprocess_data(ds_dict))
    ds_dict = {'name': 'test'}
    display.display(task_include.preprocess_data(ds_dict))
    ds_dict = {'action': 'include', 'name': 'test'}
    display.display(task_include.preprocess_data(ds_dict))
    ds_dict = {'action': 'import_tasks', 'name': 'test'}
    display.display(task_include.preprocess_data(ds_dict))
    ds_dict = {'any': 'test'}
    display.display(task_include.preprocess_data(ds_dict))

# Generated at 2022-06-13 09:25:58.963733
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    from ansible.parsing.yaml.objects import AnsibleUnicode

    ti = TaskInclude()
    ds = {'action':'include_role', 'name': 'my_role', 'INVALID':AnsibleUnicode('value')}

    assert ds['name'] == 'my_role'
    assert isinstance(ds['INVALID'], AnsibleUnicode)

    ds = ti.preprocess_data(ds)

    assert ds['name'] == 'my_role'
    assert 'INVALID' not in ds



# Generated at 2022-06-13 09:26:09.492465
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.role.include import RoleInclude
    from ansible.playbook.role.tasks import Task as RoleTask
    from ansible.utils.display import Display
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    display = Display()
    loader = DataLoader()
    variable_manager = VariableManager()
    play_context = PlayContext()
    variable_manager.extra_vars = {
        'inventory_hostname': 'localhost',
        'inventory_hostname_short': 'localhost'
    }

    task1

# Generated at 2022-06-13 09:26:13.761361
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    data = {'include': Sentinel(), 'action': 'include', 'tags': [], 'when': []}
    ti = TaskInclude()
    ds = ti.preprocess_data(data)
    # Make sure the original object is untouched
    assert data == {'include': Sentinel(), 'action': 'include', 'tags': [], 'when': []}


# Generated at 2022-06-13 09:26:25.068530
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    '''
    Test case for TaskInclude get_vars method.
    '''

    from ansible.playbook import Play
    from ansible.playbook.play import Play

    loader = DictDataLoader({
        "test_play.yaml": """
        - hosts: all
          block:
            - include: foo.yaml
        """
    })

    pb = Play.load(
        dict(
            name = "test_play",
            hosts = 'all',
            roles = [],
            tasks = [
                dict(
                    block = [
                        dict(
                            include = 'foo.yaml',
                        ),
                    ],
                ),
            ],
        ),
        variable_manager=VariableManager(),
        loader=loader,
    )


# Generated at 2022-06-13 09:26:35.966979
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    class Mock(object):
        def __init__(self):
            self.block = None
            self.name = 'some_name'
            self.apply = 'some_apply'
            self.vars = {'some_var': 'value'}
            self.unparsed_params = 'some_unparsed_params'
            self.args = {}
            self.action = 'some_action'

        def parse_args(self):
            pass

        def validate_base_args(self):
            pass

        def post_validate(self):
            pass

        def copy(self, exclude_parent=None, exclude_tasks=None):
            pass

        def get_vars(self):
            pass

        def build_parent_block(self):
            pass


# Generated at 2022-06-13 09:26:45.030820
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    class DummyTask:
        def __init__(self):
            self.vars = dict()

    t = DummyTask()
    ti = TaskInclude(t)
    ti.action = 'include'
    ti.args = dict(a=1, b=2)

    t.vars.update({'c': 2})

    ti.vars.update({'d': 3})

    assert ti.get_vars() == dict(a=1, b=2, c=2, d=3)

# Generated at 2022-06-13 09:26:46.080438
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    pass

# Generated at 2022-06-13 09:27:01.481237
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    from ansible.playbook.play import Play
    from ansible.playbook.block import Block
    from ansible.playbook.role import Role
    from ansible.playbook.role.include import IncludeRole
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.conditional import Conditional
    from ansible.template import Templar

    loader = DataLoader()
    variable_manager = VariableManager()

    play_ds = {'name': 'test', }
    play = Play.load(play_ds, variable_manager=variable_manager, loader=loader)

    my_block_ds = {'block': [], }

# Generated at 2022-06-13 09:27:11.418218
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    mock_play = Mock()

    task_include = TaskInclude(
        block=mock_play,
        role=None,
        task_include=None,
        args={'a':1,'b':2,'c':3}
    )

    # static include, action = 'include'
    task_include.action = 'include'
    v = task_include.get_vars()
    expected = {'a':1,'b':2,'c':3}
    if v != expected:
        print("ERROR: expected %s, found %s" % (expected,v))

    # static include, action = 'include_role'
    task_include.action = 'include_role'
    v = task_include.get_vars()
    expected = {}

# Generated at 2022-06-13 09:27:18.624325
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    from ansible.playbook.play_context import PlayContext
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.vars.manager import VariableManager
    from ansible.vars.hostvars import HostVars
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.plugins.task.include_tasks import ActionModule as IncludeTasks
    from ansible.plugins.task.include_role import ActionModule as IncludeRole
    from ansible.plugins.loader import PluginLoader

    # Construct a host
    host = Host(name="localhost")
    host.vars = HostVars(loader=None, hostname="localhost")

    # Construct a group
    group = Group("ungrouped")
    group.add_host(host)

   

# Generated at 2022-06-13 09:27:27.680078
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    ti = TaskInclude()
    ds = dict()

    ds = dict(
        action = "include_role",
        name = 'my role',
    )
    assert ti.preprocess_data(ds) == {'action': 'include_role', 'name': 'my role'}

    ds = dict(
        action = "include_role",
        name = 'my role',
        ignore_errors = True,
        tags = ['the_tag'],
        when = False,
    )
    assert ti.preprocess_data(ds) == {'action': 'include_role', 'name': 'my role', 'ignore_errors': True, 'tags': ['the_tag'], 'when': False}


# Generated at 2022-06-13 09:27:38.703776
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    # A dict describing an action different than any of the 'include' tasks.
    # For example, an action related to the 'import_tasks' task.
    data_dict = {
        'action': 'import_tasks',
        'debugger': 'no',
        'loop': 'yes',
        'run_once': 'no',
        'file': 'somedir/somefile.yml',
    }

    # Check if we are allowed to ignore invalid entries
    TaskInclude.load_data(data_dict, ignore_errors=True)
    assert 'debugger' not in TaskInclude.VALID_ARGS
    assert 'loop' not in TaskInclude.VALID_ARGS
    assert 'run_once' not in TaskInclude.VALID_ARGS

    # Check if we are not allowed to ignore invalid entries

# Generated at 2022-06-13 09:27:43.129874
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    task_include = TaskInclude.load({"action": "include", "apply": {"when": "1==1"}}, play=object(), task_include=object())
    p_block = task_include.build_parent_block()
    assert p_block.when == "1==1"



# Generated at 2022-06-13 09:27:58.568481
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    from ansible.playbook.play_context import PlayContext


    # Create a blocked task which includes another tasks
    play_context = PlayContext()

    host = dict(
        name='127.0.0.1',
        connection='ssh',
        port=22,
        #vars=dict(),
        vars={"a": "A"},
    )

    block = Block(
        parent_block=None,
        role=None,
        task_include=None,
        play=None,
        play_context=play_context,
        loader=None,
        variable_manager=None,
        use_handlers=False,
        role_params={}
    )

    task_include = TaskInclude(block=block, role=None, task_include=None)

    task_include.action = 'include'

# Generated at 2022-06-13 09:28:06.057361
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    # Setup vars
    playbook_dir = 'playbooks'
    inventory_filename = 'inventory'
    inventory = './test/units/inventory/inventory'

    # Create TaskInclude instance
    include_task = TaskInclude()

    # Test with include action
    data = {
        'action': 'include',
        'args': {
            'var1': 'foo',
            'var2': 'bar',
            'var3': 'baz',
        }
    }
    include_task.load_data(data)
    vars = include_task.get_vars()
    assert vars['var1'] == 'foo'
    assert vars['var2'] == 'bar'
    assert vars['var3'] == 'baz'

    # Test with import_tasks action

# Generated at 2022-06-13 09:28:14.872379
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    t = TaskInclude()
    t.action = 'include'
    t.vars = {'a': '1', 'b': '2'}
    t.args = {'c': '3', 'd': '4'}
    vars = t.get_vars()
    assert vars == {'a': '1', 'b': '2', 'c': '3', 'd': '4'}

    t.action = 'include_role'
    vars = t.get_vars()
    assert vars == {'a': '1', 'b': '2', 'c': '3', 'd': '4'}

# Generated at 2022-06-13 09:28:22.884216
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    block = Block()
    block.vars = dict(b_vars=True)
    block._parent = None
    block._play = None
    block._role = None
    block._loader = None
    block._variable_manager = None

    task_include = TaskInclude(block=block)
    task_include.vars = dict(ti_vars=True)
    task_include.args = dict(ti_args=True)

    res = task_include.get_vars()
    assert res == dict(ti_vars=True, ti_args=True), res

# Generated at 2022-06-13 09:28:36.326484
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    data = dict(file='test_file.yml', apply=dict(become=True, become_user='root'))

    # test it to work with the proper tasks
    for action in C._ACTION_ALL_PROPER_INCLUDE_IMPORT_TASKS:
        task1 = TaskInclude.load(action, data)
        assert task1.args == data
        assert not task1.args.get('apply')

    # test it to fail with the bad tasks
    for action in C._ACTION_ALL_INCLUDE_IMPORT_TASKS.difference(C._ACTION_ALL_PROPER_INCLUDE_IMPORT_TASKS):
        try:
            TaskInclude.load(action, data)
            assert False
        except AnsibleParserError:
            assert True


# Unit test

# Generated at 2022-06-13 09:28:44.765592
# Unit test for method build_parent_block of class TaskInclude

# Generated at 2022-06-13 09:28:51.024587
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager

    loader = DataLoader()
    variable_manager = VariableManager()

    # We're using the actual include module here, but it doesn't really matter which one we choose
    include_tasks_module = [
        {
            'action': 'include_tasks',
            'include_tasks': 'foobar.yml'
        },
        {
            'action': 'include_role',
            'include_role': 'foobar'
        },
        {
            'action': 'import_tasks',
            'import_tasks': 'foobar.yml'
        },
        {
            'action': 'import_role',
            'import_role': 'foobar'
        },
    ]


# Generated at 2022-06-13 09:29:01.942012
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():

    from ansible.playbook.play import Play
    from ansible.playbook.playbook_include import TaskInclude
    from ansible.playbook.role.include import TaskInclude
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.template import Templar


# Generated at 2022-06-13 09:29:16.423252
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    task_include = TaskInclude()
    data = {
        'action': 'some_include',
        'file': 'foobar',
        'some': 'invalid',
    }

    # test that no error is raised for valid data
    ti = task_include.load(data)
    assert ti.args.get('_raw_params') == 'foobar'
    assert not ti.args.get('some')

    # test that an error is raised for invalid data
    data['file'] = None
    data['some'] = 'invalid'
    try:
        ti = task_include.load(data)
    except AnsibleParserError as ae:
        assert 'Invalid options for some_include' in str(ae)
    else:
        assert False, 'AnsibleParserError not raised'

    # test that an error

# Generated at 2022-06-13 09:29:25.960870
# Unit test for method load of class TaskInclude
def test_TaskInclude_load():
    '''
    Unit test for method 'load' of class 'TaskInclude'
    '''
    ti = TaskInclude()
    data_source = {'action': 'include', 'file': 'foobar'}
    # no invalid options like 'foobar': 123
    task = ti.load(data_source, loader=None)
    assert task.args['_raw_params'] == 'foobar'
    assert task.action == 'include'
    # invalid options like 'foobar': 123
    data_source = {'action': 'include', 'foobar': 123}
    try:
        ti.load(data_source)
    except AnsibleParserError:
        pass
    else:
        raise AssertionError('Expected to call but it did not raise')
    # no file specified for include

# Generated at 2022-06-13 09:29:38.540140
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():

    # Arrange
    class MockVariableManager:
        def __init__(self):
            pass

        def get_vars(self):
            return {}

    class MockLoader:
        def __init__(self):
            pass

        def get_basedir(self):
            return ''

    class MockPlay:
        def __init__(self):
            pass

    class MockParentTask:
        def __init__(self):
            self.vars = {'inventory_hostname': 'my_hostname'}
            self.tags = ['tag1', 'tag2']
            self.when = 'inventory_hostname == my_hostname'

        def get_vars(self):
            return self.vars

        def get_tags(self):
            return self.tags

        def get_when(self):
            return

# Generated at 2022-06-13 09:29:47.848295
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    print("\n")
    root_block = Block()
    root_block.vars = {"test1_var" : "test1_value", "test2_var" : "test2_value"}

    block1 = Block()
    root_block.block = [block1]

    block1.vars = {"test3_var" : "test3_value", "test4_var" : "test4_value"}

    task1 = TaskInclude()
    block1.block = [task1]

    task1.vars = {"test5_var" : "test5_value", "test6_var" : "test6_value"}
    task1.args = {"test7_var" : "test7_value", "test8_var" : "test8_value"}

    #print(task1.get_

# Generated at 2022-06-13 09:29:57.991238
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    from ansible.playbook.block import Block
    from ansible.playbook.play import Play
    taskdata = {'action': 'include', 'file': 'dummy'}
    blockdata = {'name': 'dummy', 'tasks': [taskdata]}
    block = Block.load(blockdata, task_include=None, play=Play.load(blockdata, variable_manager=None, loader=None))
    tasks = block.compile()
    assert tasks[0].args.get('_raw_params') == 'dummy'
    assert not tasks[0].args.get('file')
    taskdata = {'action': 'include', 'file': 'dummy', 'non-existing': 'dummy'}
    blockdata = {'name': 'dummy', 'tasks': [taskdata]}
    block = Block

# Generated at 2022-06-13 09:30:05.577206
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    class FakeTaskInclude:
        def load_data(self, data, *args, **kwargs):
            # here we are in 'load_data' so the check is not done yet
            assert 'foo' in data
            assert 'bar' in data
            return data

        VALID_ARGS = frozenset(('foo', 'bar'))
        VALID_INCLUDE_KEYWORDS = frozenset(('action', 'file', 'bar'))

    ti = FakeTaskInclude()

    # 1. no foo and bar
    d = dict(action='include', debug='msg')
    ti.check_options(ti.load_data(d), d)

    # 2. no foo but bar
    d = dict(action='include', bar='baz', debug='msg')

# Generated at 2022-06-13 09:30:22.545324
# Unit test for method load of class TaskInclude
def test_TaskInclude_load():

    # Invalid option for 'include' action
    data = dict(
        action='include',
        apply={},
    )
    task = TaskInclude()
    try:
        task.check_options(task.load_data(data), data)
        assert False, "Expected exception on invalid option for 'include' action"
    except AnsibleParserError as e:
        assert "Invalid options for include: apply" in e.message

    # Missing file path for 'include' action
    data = dict(
        action='include',
        file='',
        _raw_params='',
    )
    task = TaskInclude()

# Generated at 2022-06-13 09:30:32.772466
# Unit test for method load of class TaskInclude
def test_TaskInclude_load():
    from ansible.parsing.yaml.objects import AnsibleUnicode

    # Test defaults
    c = TaskInclude.load(dict())
    assert c.action == 'include'
    assert '_raw_params' in c.args
    assert c.args['_raw_params'] is None
    assert not c.args.get('apply', None)

    # Test args
    c = TaskInclude.load(dict(file='foo.yml'))
    assert c.args['_raw_params'] == 'foo.yml'

    # Test apply
    c = TaskInclude.load(dict(file='foo.yml', apply=dict()))
    assert c.args['_raw_params'] == 'foo.yml'
    assert c.args['apply'] == dict()

    # Test with invalid apply (

# Generated at 2022-06-13 09:30:42.726057
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    task_include = TaskInclude()

    # Action not in C._ACTION_INCLUDE
    # return values:
    #    get_vars() of parent class Task()
    #    task include vars are NOT included as a parameter for the included tasks
    task_include.action = 'debug'
    task_include.vars = {'k': 'v'}
    task_include.args = {'var1': 'value1'}
    assert task_include.get_vars() == {'k': 'v'}, "1_1"

    # Action in C._ACTION_INCLUDE
    # return values:
    #    task include vars are included as a parameter for the included tasks
    task_include.action = 'include'
    task_include.vars = {'k': 'v'}
   

# Generated at 2022-06-13 09:30:53.106989
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.block import Block
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    myvar = dict(
        foo='bar',
        zoo='zar'
    )
    display = Display()
    variable_manager = VariableManager()
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources='localhost,')
    variable_manager.set_inventory(inventory)
    variable_manager.set_host_variable('localhost', myvar)
    playbook_vars = dict(
        fuz='biz'
    )
    variable_manager.extra_vars = playbook_vars


# Generated at 2022-06-13 09:31:04.358617
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    display.verbosity = 3

    # Test1: call method preprocess_data when action is 'include'
    data = dict(action='include', file='/etc/hosts', args=dict(arg1=1), arg2='a')
    task_include = TaskInclude(task_include=None)
    result = task_include.preprocess_data(ds=data)
    assert result == dict(action='include', file='/etc/hosts', args=dict(arg1=1))

    # Test2: call method preprocess_data when action is 'import_playbook'
    data = dict(action='import_playbook', file='/etc/hosts', args=dict(arg1=1), arg2='a')
    task_include = TaskInclude(task_include=None)
    result = task_include.pre

# Generated at 2022-06-13 09:31:15.195149
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    loader = DataLoader()

    variable_manager = VariableManager()
    variable_manager.set_inventory(loader.load_inventory("localhost"))
    variable_manager.set_vault_password("secret")

    task = TaskInclude.load(
        dict(
            action="include_role",
            name="some_role",
            vars={
                "some_var": 1,
                "another_var": 2,
            }
        ),
        variable_manager=variable_manager,
        loader=loader
    )

    # With an 'include_role' task the get_vars() method should only return
    # variables set in the vars as they are not parameters to the role
    assert task.get

# Generated at 2022-06-13 09:31:30.302511
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    '''
    Unit tests for the method check_options of class TaskInclude.
    '''
    from ansible.playbook.task_include import TaskInclude

    # Test for the case that TaskInclude does not receive any options.
    data = dict(action='include', args=dict())
    task = TaskInclude(Task(), None, None)
    with pytest.raises(AnsibleParserError) as execinfo:
        task.check_options(task.load_data(data), data)
    assert "No file specified for include" in str(execinfo.value)

    # Test for the case that TaskInclude receives a file option.
    data = dict(action='include', args=dict(file='foo.yml'))
    task = TaskInclude(Task(), None, None)

# Generated at 2022-06-13 09:31:37.044742
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    from ansible.playbook.role import Role
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.errors import AnsibleParserError
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    import os

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=[])
    variable_manager = VariableManager(loader=loader, inventory=inventory)

# Generated at 2022-06-13 09:31:43.385759
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():

    # TEST BLOCK 1: file, _raw_params, apply
    data = dict(
        action='include',
        file=dict(
            dest='/tmp/dest',
            content='content'
        ),
        apply=dict(
            meta=dict(
                key1='value1',
                key2='value2'
            )
        )
    )
    task = TaskInclude.load(data, variable_manager=None, loader=None)
    assert task.action == 'include'
    assert task.args['file'] == data['file']
    assert task.args['apply'] == data['apply']
    assert task.args['_raw_params'] is None
    assert task.apply == data['apply']

    # TEST BLOCK 2: _raw_params, apply, no file

# Generated at 2022-06-13 09:31:52.571916
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    ti = TaskInclude()
    assert ti.check_options(TaskInclude.load({'action': 'include_tasks', 'file': 'foo'}), {})
    assert ti.check_options(TaskInclude.load({'action': 'include_role', 'file': 'foo'}), {})
    assert ti.check_options(TaskInclude.load({'action': 'import_playbook', 'file': 'foo'}), {})

    assert ti.check_options(TaskInclude.load({'action': 'include_tasks', 'apply': 'foo', 'file': 'foo'}), {})
    assert ti.check_options(TaskInclude.load({'action': 'import_playbook', 'apply': 'foo', 'file': 'foo'}), {})


# Generated at 2022-06-13 09:32:09.354176
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    '''
    This method tests the check_options method of TaskInclude class
    '''
    block = None
    role = None
    task_include = None
    ti = TaskInclude(block=block, role=role, task_include=task_include)
    data = Sentinel  # for testing errors it can be any object
    task = Task()
    opts = task.args

    opts.update({'file': Sentinel, '_raw_params': Sentinel})
    ti.check_options(task, data)
    assert('file' not in opts)
    assert('_raw_params' in opts)
    assert(opts['_raw_params'] is Sentinel)

    opts.update({'_raw_params': Sentinel})
    ti.check_options(task, data)

# Generated at 2022-06-13 09:32:16.976276
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    from ansible.playbook.included_file import IncludedFile
    from ansible.playbook.block import Block
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.plugins.loader import action_loader
    import pytest

    class Mockvariable_manager(VariableManager):
        def __init__(self, *args, **kwargs):
            self._vars_cache = {'inventory_hostname': 'testhost', 'group_names': ['all']}
            self._hostvars = {}
           

# Generated at 2022-06-13 09:32:27.516005
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():

    # Note that 'load_data' is not getting called in this test and other methods
    # like 'validate_vars' are not needed and not called.

    from ansible.playbook.block import Block
    from ansible.playbook.role.includes import TaskInclude

    task_include = TaskInclude(block=Block())

    # A dict with a key that is not an action is not allowed
    ds1 = dict(nonsense=dict())
    with pytest.raises(AnsibleParserError):
        task = task_include.check_options(task_include.load_data(ds1), ds1)

    # A dict with an action key that is not an 'include' action is not allowed
    ds2 = dict(action='nonsense', file='myinclude.yml')

# Generated at 2022-06-13 09:32:36.350381
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    apply_attrs = {'hosts': '127.0.0.1', 'dynamic': 'all'}
    p_block = TaskInclude().build_parent_block(apply_attrs)
    assert p_block.name == '127.0.0.1'
    assert p_block.hosts == ['127.0.0.1']
    assert p_block.dynamic == ['all']
    assert not p_block.block
    assert not p_block.include
    assert p_block.ignore_errors is None
    assert p_block.until is None
    assert p_block.retries is None
    assert p_block.register is None
    assert p_block.delay is None


TaskInclude.register_lookup()

# Generated at 2022-06-13 09:32:51.124479
# Unit test for method load of class TaskInclude
def test_TaskInclude_load():  # type: () -> None
    class DummyVariableManager(object):
        def __init__(self):
            pass

        def get_vars(self, loader=None, play=None, host=None, task=None, include_hostvars=True, include_delegate_to=True):
            pass

        def get_inventory_vars(self, host):
            pass

    class DummyLoader(object):
        class DummyFile(object):
            def __init__(self):
                self.path = "./unit.test.file"

        def __init__(self):
            pass

        def path_dwim_relative(self, basedir, path, section_name, vault_password=None):
            return './unit.test.file'


# Generated at 2022-06-13 09:32:59.924426
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    task_include = TaskInclude()

    dataloader = DataLoader()
    variable_manager = VariableManager()
    display.verbosity = 3
    context = PlayContext()

    data = dict(
        file=dict(
            path = "/dev/null",
            mode = '0644',
        ),
        invalid = "should fail",
        action = "include_role",
    )
    task_include.preprocess_data(data)
    assert not task_include.args.get('invalid')


# Generated at 2022-06-13 09:33:11.698401
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    ti = TaskInclude()
    ti._loader = DummyLoader()
    ti._variable_manager = DummyVariableManager()
    ti._block = DummyBlock()

    # Throw error on invalid options
    data = {'action': 'include_tasks', 'file': 'dummy', 'foo': 'bar'}
    with pytest.raises(AnsibleParserError) as excinfo:
        ti.check_options(ti.load_data(data, ti._variable_manager, ti._loader), data)
    assert 'Invalid options for include_tasks: foo' in str(excinfo.value)

    # Throw error on invalid apply options for non-include_tasks
    data = {'action': 'include_role', 'file': 'dummy', 'apply': {'foo': 'bar'}}

# Generated at 2022-06-13 09:33:22.156560
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    from ansible.playbook.base import Base
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.play import Play
    b = Base(dict(
        apply=dict(block=[]))
    )
    task = TaskInclude({}, block=b, role=None, task_include=None)
    apply_attrs = task.args.get('apply')
    task._loader = None
    task._variable_manager = None
    task._parent = Play()
    p_block = task.build_parent_block()
    from ansible.playbook.block import Block
    assert(isinstance(p_block, Block))
    assert(p_block.block is apply_attrs['block'])

# Generated at 2022-06-13 09:33:27.072096
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    class FakeVariableManager(object):
        pass

    class FakeLoader(object):
        pass

    class FakeRole(object):
        pass

    class FakePlay(object):
        pass

    class FakeParent(object):
        pass

    fake_parent = FakeParent()
    fake_parent2 = FakeParent()
    fake_parent3 = FakeParent()
    fake_parent4 = FakeParent()
    fake_parent5 = FakeParent()

    fake_vars = dict()
    fake_vars2 = dict()
    fake_vars3 = dict()
    fake_vars4 = dict()
    fake_vars5 = dict()

    fake_vars['a'] = 'a'
    fake_vars2['c'] = 'c'
    fake_vars3['d'] = 'd'
    fake_v

# Generated at 2022-06-13 09:33:37.835120
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    '''Test for method build_parent_block in class TaskInclude'''
    from ansible.playbook import Play
    from ansible.playbook.block import Block,\
        BlockInclude
    from ansible.playbook.role import Role
    from ansible.playbook.role.include import RoleInclude
    from ansible.playbook.role.tasks import Task as RoleTask,\
        TaskInclude as RoleTaskInclude
    from ansible.playbook.task import Task
    from ansible.playbook.task.include import TaskInclude
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
