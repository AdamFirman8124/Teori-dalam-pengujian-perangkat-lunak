

# Generated at 2022-06-13 09:23:54.111962
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    # Uses valid args
    data = {'action': 'include', 'file': 'tasks.yaml', 'debugger': 'True'}
    task = TaskInclude(block=None, role=None, task_include=None)
    task = task.check_options(task.load_data(data), data)
    assert task.action == 'include'
    assert task.args['file'] == 'tasks.yaml'
    assert task.args['debugger'] is True

    # Uses 'apply' argument
    data = {'action': 'include', 'file': 'tasks.yaml', 'apply': {'debugger': 'True'}}
    task = TaskInclude(block=None, role=None, task_include=None)
    task = task.check_options(task.load_data(data), data)


# Generated at 2022-06-13 09:24:01.200509
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    '''
    Test method preprocess_data of class TaskInclude
    '''

    data = {'somearg': 'somearg_value1'}
    task = TaskInclude()
    preprocessed_data = task.preprocess_data(data)
    assert preprocessed_data == {}, "preprocess_data returns unexpected result."


if __name__ == '__main__':
    test_TaskInclude_preprocess_data()

# Generated at 2022-06-13 09:24:07.409898
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    t = TaskInclude()
    # Assumes Task class has a vars attribute
    t.vars = {'key1': 'value1', 'key2': 'value2'}
    assert t.get_vars() == {'key1': 'value1', 'key2': 'value2'}


# Generated at 2022-06-13 09:24:17.317743
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block

    play = Play()
    play.vars['pv'] = 'pv'

    block1 = Block.load(
        dict(name='block1',
             when='block1'),
        play=play,
        task_include=None,
        role=None,
        variable_manager=None,
        loader=None,
    )
    block1.vars['b1v'] = 'b1v'
    task1 = Task.load(
        dict(name='task1',
             when='task1'),
        block=block1,
        role=None,
        task_include=None,
        variable_manager=None,
        loader=None,
    )

# Generated at 2022-06-13 09:24:27.772056
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    # Build fake data
    data = {
        'block': [{
            'name': 'test_name',
            'args': {'arg': True},
            'tags': ['tag1'],
            'when': 'ansible_distribution=="Fedora"'
        }],
        'apply': {
            'name': 'test_parent_name',
            'tags': ['tag2'],
            'when': 'ansible_distribution=="Ubuntu"'
        }
    }

    # Load data
    ti = TaskInclude()
    ti.args.update(ti.load_data(data, variable_manager=None, loader=None).args)

    # Run method
    p_block = ti.build_parent_block()

    # Assert data

# Generated at 2022-06-13 09:24:34.991720
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    # import modules needed for testing
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group

    from ansible.module_utils._text import to_bytes

    from ansible.playbook.play import Play
    from ansible.playbook.role import Role
    from ansible.plugins import module_loader
    from ansible.template import Templar
    from units.mock.loader import DictDataLoader

    # setup the objects needed and populate it with data
    variable_manager = VariableManager()
    loader = DictDataLoader({})

    # setup the host objects
    hosts = [Host(name='192.168.0.1', port=22), Host(name="localhost", port=22)]
    group = Group('all')

    # setup play object

# Generated at 2022-06-13 09:24:39.079955
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    # set up objects
    ds = dict()
    ti = TaskInclude()

    ds['action'] = 'include'
    ds['foo'] = 'bar'

    ds = ti.preprocess_data(ds)
    assert 'action' in ds
    assert 'foo' not in ds

    ds['action'] = 'import_playbook'
    ds['foo'] = 'bar'

    ds = ti.preprocess_data(ds)
    assert 'action' in ds
    assert 'foo' not in ds

    ds['action'] = 'import_tasks'
    ds['foo'] = 'bar'

    ds = ti.preprocess_data(ds)
    assert 'action' in ds
    assert 'foo' not in ds


# Generated at 2022-06-13 09:24:48.861095
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():

    ti = TaskInclude()
    ti.action = 'include'
    ti.args = {
        '_raw_params': 'file.yml',
    }

    ti = ti.check_options(ti, {})
    assert ti.args == {
        '_raw_params': 'file.yml',
    }

    ti.action = 'include_tasks'
    ti.args = {
        '_raw_params': 'file.yml',
        'apply': {},
    }

    ti = ti.check_options(ti, {})
    assert ti.args == {
        '_raw_params': 'file.yml',
        'apply': {},
    }


# Generated at 2022-06-13 09:25:00.479695
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    check = TaskInclude.check_options

    # Assert TaskInclude action is not in the tuples of valid TaskInclude actions
    assert ('action_for_task_include' not in C._ACTION_ALL_PROPER_INCLUDE_IMPORT_TASKS and
            'action_for_task_include' not in C._ACTION_ALL_INCLUDE_ROLE_TASKS)

    # Assert options validation on 'include' task
    task = Task()
    task.action = 'include'
    task.args = {'file': 'fake.yml', 'other': 'value'}
    valid_task = check(task, {})
    assert task.args.get('_raw_params') == 'fake.yml'
    assert 'other' not in task.args

    # Assert options validation on

# Generated at 2022-06-13 09:25:06.740451
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    '''
    Ensure TaskInclude.preprocess_data() keeps expected values, drop the rest
    '''
    block = Block()

    current_data = dict(
        action='include_role',
        file='test.yml',
        name='some_play',
        tags=['foo'],
        ignore_errors=True,
        when='some_var is defined'
    )

    new_data = dict(
        action='include_role',
        file='test.yml',
        name='some_play',
        tags=['foo'],
        ignore_errors=True,
        when='some_var is defined',
        loop='some_loop_var'
    )

    ti = TaskInclude(block=block, role=None, task_include=None)

# Generated at 2022-06-13 09:25:23.169053
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    # Testing class TaskInclude
    # Unit tests for preprocess_data method
    #
    # Not much to test here, because this method only invokes
    # the same method of the super class and then do some checks
    # on the original `ds` object.
    # Since the super class is already tested, we are going to test
    # here only the checks of the ds object.
    #
    # First of all we create an instance of the class:

    task = TaskInclude()

    # Then we create a valid dataset for an include:

    ds = {
        'action': 'include',
        'file': 'some_file.yml',
        'vars': {},
        'tags': [],
        'when': [],
    }

    # It should return the same dataset. There is no need for preprocessing:

# Generated at 2022-06-13 09:25:35.487000
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    class Mock_TaskInclude(TaskInclude):
        def __init__(self, *args, **kwargs):
            super(TaskInclude, self).__init__(*args, **kwargs)

            # Simulate Attribute
            for name, value in self.args.items():
                setattr(self, name, FieldAttribute(self, name, value=value))

    # key: input data
    # value: expected data

# Generated at 2022-06-13 09:25:41.994689
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    from ansible.playbook.task import Task

    loader = 'dummy_loader'
    variable_manager = 'dummy_variable_manager'
    block = Block(loader=loader, variable_manager=variable_manager)
    role = 'dummy_role'
    task_include = 'dummy_task_include'

    class MockTaskInclude(TaskInclude):
        def load_data(self, ds, variable_manager=None, loader=None):
            assert ds == data_source
            assert variable_manager == 'dummy_variable_manager'
            assert loader == 'dummy_loader'
            return Task(block=self._block, role=self._role, task_include=self._task_include)


# Generated at 2022-06-13 09:25:52.154611
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():

    # -- Base case to cover all other ELSE cases
    # -- Action is 'include' but there is no parent. This is the case which gives
    #    empty VARS
    task = TaskInclude(dict(action = 'include'))
    assert task.get_vars() == {}, "Vars are returned as expected"

    # -- A base case to cover all ELSE cases in the IF
    # -- 'include' is called but there are no args to include
    fake_parent = TaskInclude(dict(action = 'include'))
    task = TaskInclude(dict(action = 'include', _parent = fake_parent))
    assert task.get_vars() == {}, "Vars are returned as expected"

    # -- Case to cover 'include' and args which has no parent

# Generated at 2022-06-13 09:25:58.842194
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():

    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext

    p = Play().load({
        'name': 'testplay',
        'hosts': 'testhost',
        'gather_facts': 'no',
        'tasks': [
            {
                'name': 'testtask',
                'include': {
                    'action': 'include',
                    'file': '/included_tasks',
                    'apply': {'loop': {'var': {'test': 'item'}}}
                }
            }
        ]
    }, variable_manager=None, loader=None)
    t = p.get_tasks()[0]
    p_block = t.build_parent_block()
    assert p_block.get_name() == 'testtask'

# Generated at 2022-06-13 09:26:09.365311
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():

    # Create variable_manager to pass it to build_parent_block method
    variable_manager = ansible.vars.Manager()
    variable_manager.extra_vars = {
        'o': 'my_own_var',
        'r': 'my_role_var',
        'p': 'my_play_var',
        'g': 'my_group_var',
        'h': 'my_host_var',
    }
    variable_manager._options = {
        'playbook_dir': '.',
        'force_handlers': False
    }

    # Create loader to pass it to build_parent_block method
    loader = DataLoader()

    # Create task for testing with no apply in args
    task_no_apply = TaskInclude(block=None, role=None, task_include=None)
   

# Generated at 2022-06-13 09:26:17.201789
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():

    task_include = TaskInclude()

    # Normal include => valid + no change
    task = Task()
    task.args = {'_raw_params': '{{some_var}}', 'tags': "abc", 'when': 'true'}
    task.action = 'include'
    task = task_include.check_options(task, {'action': 'include'})
    assert task.args['_raw_params'] == '{{some_var}}'
    assert task.action == 'include'

    # Include with missing include parameter => error
    task.args = {'tags': "abc", 'when': 'true'}
    task.action = 'include'

# Generated at 2022-06-13 09:26:22.049207
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():

    this_task = TaskInclude()

    # Check if not 'include'
    this_task.action = 'include_role'

    assert this_task.get_vars() == dict(), 'Should be empty dict'

    # Check if include
    this_task.action = 'include'
    this_task._parent = 'parent'

    # Check if include but no parent
    this_task._parent = None
    this_task.args = dict()
    this_task.vars = dict()

    assert this_task.get_vars() == dict(), 'Should be empty dict'

    # Check if include but parent
    this_task._parent = 'parent'
    this_task.args = dict(arg_one='one', arg_two='two')

# Generated at 2022-06-13 09:26:29.391517
# Unit test for method load of class TaskInclude
def test_TaskInclude_load():
    from ansible.playbook.play import Play
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    def _create_playbook_executor(loader):
        variable_manager = VariableManager()
        inventory = InventoryManager(loader=loader, sources=[''])
        variable_manager.set_inventory(inventory)
        return PlaybookExecutor(
            playbooks=[''],
            inventory=inventory,
            variable_manager=variable_manager,
            loader=loader,
            options='',
            passwords={},
        )

    # setup
    loader = DataLoader()
    pbe = _create_playbook_executor(loader)
   

# Generated at 2022-06-13 09:26:38.091764
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    '''Test for method preprocess_data of class TaskInclude'''
    import json

    # Testing with inputs from ../../../ansible/test/units/parsing/utils/fixtures/task_include_data_preprocess_data.json
    my_task_include = TaskInclude(task_include=None)


# Generated at 2022-06-13 09:26:50.961742
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    ds = dict(
        action='include_tasks',
        args=dict(
            bla=Sentinel,
            apply=dict(
                bla=1,
            ),
        ),
    )
    ti = TaskInclude()
    ds = ti.preprocess_data(ds)
    assert 'bla' not in ds['args']
    assert 'bla' in ds['args']['apply']
    assert ds['args']['apply']['bla'] == 1

# Generated at 2022-06-13 09:27:01.316625
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    from ansible.playbook.play import Play
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    variable_manager = VariableManager()
    play = Play.load(
        dict(
            name='test_play',
            hosts=['foo'],
            gather_facts='no',
            tasks=[dict(action='include', apply={'tags': 'a_tag'})]
        ),
        loader=loader,
        variable_manager=variable_manager
    )
    included_task = play.get_tasks()[0]
    assert isinstance(included_task._parent, Block)
    assert included_task._parent._name == 'a_tag'

# Generated at 2022-06-13 09:27:11.432689
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources='')
    variable_manager = VariableManager(loader=loader, inventory=inventory)

# Generated at 2022-06-13 09:27:20.452893
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    import ansible.plugins.action as action
    # Note that this test method wouldn't test if an invalid attribute is set,
    # but with a sentinel value.
    #
    # If a test with a non-sentinel value is needed, it can be added here.
    #
    # This test is to make sure that we don't return error if an invalid attribute is present
    # in a task.
    si = TaskInclude()
    ds = dict(action='include_role', name='test_role')
    assert si.preprocess_data(ds) == ds

    ds = dict(action='import_tasks', name='test_role')
    assert si.preprocess_data(ds) == ds

    ds = dict(action='include_tasks')
    assert si.preprocess_data(ds) == d

# Generated at 2022-06-13 09:27:29.193113
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    from ansible.playbook.play import Play
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.executor.task_queue_manager import TaskQueueManager

    # Load play and create TaskInclude
    pb_ex = PlaybookExecutor([], [], [], [], 'localhost', 0, None)
    loader = DataLoader()
    inv_mgr = InventoryManager(loader=loader, sources='localhost,')
    variable_manager = VariableManager(loader=loader, inventory=inv_mgr)


# Generated at 2022-06-13 09:27:39.472104
# Unit test for method load of class TaskInclude
def test_TaskInclude_load():
    from ansible.vars.manager import VariableManager
    from ansible.playbook.play import Play
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    # Playbook file
    yml_file = 'test_playbook.yml'

    # Create the play

# Generated at 2022-06-13 09:27:51.145112
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.parsing.yaml.loader import AnsibleLoader

    block = Block()
    data = {u'include': u'test_include.yml'}
    ti = TaskInclude(block=block)
    task = ti.load_data(data, variable_manager=None, loader=AnsibleLoader)

    # test case 1: data is correctly written
    ti.check_options(task, data)
    assert task.args['_raw_params'] == u'test_include.yml'

    # test case 2: no _raw_params specified
    data = {u'apply': {u'collect_facts': False}}

# Generated at 2022-06-13 09:28:04.089575
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    from ansible.vars import VariableManager
    from ansible.playbook.play import Play
    from ansible.parsing.dataloader import DataLoader
    from ansible.plugins.loader import action_loader

    task_include = TaskInclude()
    task_include._loader = DataLoader()
    task_include._variable_manager = VariableManager()


# Generated at 2022-06-13 09:28:09.108787
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    task_include = TaskInclude()
    task_include.action = 'include_role'
    task_include.vars = {
        'name': 'this is a name',
        'tags': 'include_role_tags',
    }
    task_include.args = {
        'file': 'include_role_file',
        'some_args': 'this is some_args',
    }

    # Check for 'some_args' in the result
    vars_result = task_include.get_vars()
    assert 'some_args' in vars_result

    task_include._parent = TaskInclude()
    task_include._parent.vars = {
        'name': 'this is a name',
        'tags': 'this is tags',
    }

    # Check for 'some_args' in the result

# Generated at 2022-06-13 09:28:19.472743
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    """Unit test for method preprocess_data of class TaskInclude.
    """
    import copy

    ti = TaskInclude()

    # Check VALID_INCLUDE_KEYWORDS
    assert isinstance(ti.VALID_INCLUDE_KEYWORDS, frozenset)

    data = {'action': 'include',
            'name': 'my_include_task',
            'file': 'my_include_file'}

    # Check no changes if no extra keys
    assert ti.preprocess_data(data) == data

    # Check with action that doesn't support extra keys
    # Check extra key is removed
    data_extra_key = copy.deepcopy(data)
    data_extra_key['foo_bar'] = 'baz'

# Generated at 2022-06-13 09:28:37.495293
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    from .test_task import ConstructableTask
    from .test_block import ConstructableBlock
    from .test_play import ConstructablePlay
    from ansible.vars.manager import VariableManager

    attrs = {
        '_loader': None,
        '_variable_manager': VariableManager(),
    }
    constructor_args = ('block', 'role', 'task_include')

    # Test without argument `apply`
    task_include = ConstructableTask(cls=TaskInclude, constructor_args=constructor_args, attrs=attrs)
    p_block = task_include.build_parent_block()
    assert isinstance(p_block, TaskInclude)
    assert p_block is task_include

    # Test with argument `apply`

# Generated at 2022-06-13 09:28:45.756008
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    from ansible.utils.display import Display
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    display = Display()
    loader = DataLoader()
    context_val = PlayContext(play=Play())
    context_val.variable_manager = VariableManager()

    test_data_1 = {"apply": {}, "args": {}, "block": [], "vars": {}}
    test_data_2 = {"apply": {"a": 1, "b": 2}, "args": {}, "block": [], "vars": {}}


# Generated at 2022-06-13 09:28:52.497525
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    from ansible.playbook.play_context import PlayContext

    # Setup test block
    from ansible.playbook.play import Play
    from ansible.playbook.role import Role
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.vars.manager import VariableManager

    def test_check_options(data, action, result):
        play = Play().load(dict(
            name="Ansible Play",
            hosts=['all'],
            gather_facts='no',
            tasks=[data],
        ), variable_manager=VariableManager(), loader=None)
        block = Block.load(data=dict(
            tasks=[data],
            rescue=[],
            always=[],
        ), parent_block=play, role=Role(), task_include=None)



# Generated at 2022-06-13 09:29:02.762183
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    from ansible.playbook.task import Task

    def test_options(data):
        for key, value in data.items():
            yield key, value

    args_apply_dict = {
        'action': 'include',
        'args': {},
        'apply': {'tags': ['include']},
        'file': 'file',
        'loop': [],
        'loop_control': {},
        'loop_with': {}
    }
    args_apply_list = {
        'action': 'include',
        'args': {},
        'apply': ['tags=include'],
        'file': 'file',
        'loop': [],
        'loop_control': {},
        'loop_with': {}
    }

# Generated at 2022-06-13 09:29:14.688520
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    from collections import namedtuple
    from ansible.playbook.play import Play
    from ansible.playbook.role_include import RoleInclude
    from ansible.playbook.block import Block
    from ansible.vars.manager import VariableManager

    task_include = TaskInclude()

    # Aliases to keep things simple
    args = task_include.args
    build_parent_block = task_include.build_parent_block

    # No parent, no apply
    args.clear()
    assert build_parent_block() is task_include

    # Parent, no apply
    role_include = RoleInclude()
    task_include._parent = role_include
    assert build_parent_block() is task_include

    # Parent and apply
    args.clear()

# Generated at 2022-06-13 09:29:20.388108
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    from ansible.vars import VariableManager
    from ansible.vars.reserved import Reserved

    Play = namedtuple('Play', ['vars'])
    play = Play(vars=dict())

    Task = namedtuple('Task', ['_play'])
    task = Task(_play=play)

    VariableManager = namedtuple('VariableManager', ['_reserved'])
    variable_manager = VariableManager(_reserved=Reserved(dict()))

    Block = namedtuple('Block', ['args'])
    block = Block(args=dict())

    # Case 1
    # apply_attrs is not empty
    apply_attrs = dict(
        any_key='any_value'
    )

    ti = TaskInclude(block=block, role=None, task_include=None)

# Generated at 2022-06-13 09:29:35.472831
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():

    # TaskInclude with 'include' action
    t = TaskInclude.load({
        'action': 'include',
        'args': {'bla': 1, 'bla_bla': 2},
        'name': 'foo',
    })
    v = t.get_vars()
    assert v['bla'] == 1
    assert v['bla_bla'] == 2
    assert 'tags' not in v
    assert 'when' not in v

    # TaskInclude with any other action is the same as a Task
    t = TaskInclude.load({
        'action': 'meta',
        'args': {'bla': 1, 'bla_bla': 2},
        'when': True,
        'tags': ['t'],
        'name': 'foo',
    })
    v = t

# Generated at 2022-06-13 09:29:42.852445
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.vars.manager import VariableManager

    mytask = dict(action='include', file='fake.yml')
    myblock = dict(name='first_block')
    path_loader = None
    variable_manager = VariableManager()
    loader = None

    #1. Standard usage: no apply
    block = Block.load(myblock, play=Play().load({}, variable_manager=variable_manager, loader=loader), task_include=None, role=None)

# Generated at 2022-06-13 09:29:49.980331
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task

    block = Block()
    block.vars = {'blockvar': 'block'}
    block.parent_task = Task()
    block.parent_task.vars = {'parent_task': 'parent_task'}
    block.parent_task.block = block
    block.parent_task.loop = {'loopvar': 'loop'}

    ti1 = TaskInclude(block=block)
    ti1.vars = {'taskincludevar': 'taskinclude'}
    ti1.action = 'include'
    ti1.args = {'argvar': 'arg'}


# Generated at 2022-06-13 09:29:59.465290
# Unit test for method load of class TaskInclude
def test_TaskInclude_load():
    from ansible.playbook.play import Play
    from ansible.playbook.role import Role
    from ansible.vars.manager import VariableManager

    def build_task(filename, data, play=None, role=None):
        # construct a play_ds with expected structure
        play_ds = dict(
            name='test',
            hosts='none',
            become='false',
            become_method='sudo',
            tasks=[]
        )
        if play is None:
            play = Play().load(play_ds, variable_manager=VariableManager(), loader=None)

        # set the play context
        play._role_context = dict(name='test', filename=filename)

        # construct a task_ds with expected structure

# Generated at 2022-06-13 09:30:28.006376
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():

    def _task(action='include', args = { 'loop': '{{ my_vars }}', 'other': 'foo'}, parent=None):
        task_ds = {
            'action': action,
            'args': args,
            'name': 'included task',
        }
        task = TaskInclude()
        task.action = action
        task.args = args
        task.name = 'included task'
        task._parent = parent

        if parent:
            parent.block = [task]
        return task

    ds = {
        'hosts': 'localhost',
        'vars': {'my_vars': 'foobar'},
        'tasks': [
            _task(),
        ],
    }


# Generated at 2022-06-13 09:30:39.454057
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.playbook.block import Block
    from ansible.playbook.role import Role
    from ansible.playbook.task import Task
    from ansible.playbook.conditional import Conditional
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    # Setup the Fake Data Loader
    loader = DataLoader()
    loader.set_basedir(C.DEFAULT_MODULE_PATH)
    # Setup the Fake Play Context
    play_context = PlayContext()
    # Setup the Fake Play

# Generated at 2022-06-13 09:30:48.595405
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    '''
    Test if TaskInclude.preprocess_data() works as expected.
    '''
    class FakeTask:
        def __init__(self, action):
            self.action = action

    class FakeInclude:
        VALID_INCLUDE_KEYWORDS = frozenset(('foo', 'bar', 'baz'))

        def preprocess_data(self, ds):
            return ds

    fake_task = FakeTask('action_1')
    fake_task2 = FakeTask('action_2')

    fake_data = {
        'foo': 'foo',
        'bar': 'bar',
        'baz': 'baz',
        'unknown': 'unknown',
    }

    fake_include = FakeInclude()


# Generated at 2022-06-13 09:30:57.100643
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    # Test with default apply attributes
    test_data = {
        'block': [],
        'apply': {}
    }
    my_task = TaskInclude.load(test_data)
    block = my_task.build_parent_block()
    assert block.block == []
    assert block.apply == {}

    # Test with custom apply attributes
    test_data = {
        'block': [],
        'apply': {
            'loop': '{{ my_list }}',
            'name': 'loop with my_list',
            'with_items': '{{ my_list }}',
        }
    }
    my_task = TaskInclude.load(test_data)
    block = my_task.build_parent_block()
    assert block.block == []

# Generated at 2022-06-13 09:31:06.892286
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():

    import sys
    if not sys.version_info[:2] == (2, 6):
        return

    # Test for valid data
    TaskInclude.VALID_INCLUDE_KEYWORDS = TaskInclude.VALID_INCLUDE_KEYWORDS.union(set(["include_valid_attr"]))
    include_data = {'action': 'name', 'include_valid_attr': 'value'}
    include_data_preprocessed = TaskInclude.preprocess_data(include_data)
    assert include_data_preprocessed == {'action': 'name', 'include_valid_attr': 'value'}

    # Test for invalid data
    include_data = {'action': 'name', 'include_invalid_attr': 'value'}
    include_data_preprocessed = TaskInclude

# Generated at 2022-06-13 09:31:17.238522
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    """
    Unit test for method check_options of class TaskInclude.
    """
    test_cases = [
        'include_role',
        'include_tasks',
        'import_tasks',
        'import_role'
    ]
    for test_case in test_cases:
        data = {'action': test_case}
        ti = TaskInclude(block=None, role=None, task_include=None)
        task = ti.check_options(ti.load_data(data), data)
        assert task.args['_raw_params'] == None
        assert task.args['apply'] == {}

        data = {'action': test_case, 'file': 'somefile'}
        ti = TaskInclude(block=None, role=None, task_include=None)
        task = ti.check

# Generated at 2022-06-13 09:31:32.424461
# Unit test for method load of class TaskInclude
def test_TaskInclude_load():
    from ansible.playbook.role import Role

    class TestVariableManager:
        def __init__(self):
            self.extra_vars = dict()

    class TestLoader:
        def __init__(self):
            self.paths = ['/etc/ansible/roles']
            self.cwd = '/etc/ansible/playbooks'

    class TestPlay:
        def __init__(self):
            self.variable_manager = TestVariableManager()
            self.loader = TestLoader()

    class TestRole:
        def __init__(self):
            self.name = 'my-role'
            self.parent_role = None
            self.path = '/etc/ansible/roles/my-role'

# Generated at 2022-06-13 09:31:41.119209
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    from ansible.playbook.play_context import PlayContext

    ti = TaskInclude()
    ti.name = "test get_vars"
    ti.action = 'include'

    # Create an empty block to serve as parent
    b = Block()
    b.vars = dict(p_var='p_value')
    ti._parent = b

    # Set some self.vars
    ti.vars = dict(s_var="s_value")
    ti.args = dict(a_var="a_value")

    # Test var merging
    assert ti.get_vars() == {'p_var': 'p_value', 's_var': 's_value', 'a_var': 'a_value'}

    # Test 'include*' restrictions on ``args``

# Generated at 2022-06-13 09:31:51.363309
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():

    # Unit test for method build_parent_block of class TaskInclude
    def test_TaskInclude_build_parent_block():
        # We use dummy loader and variable manager
        loader = DummyLoader()
        variable_manager = DummyVariableManager()
        # We need a play to instantiate task include
        play_ds = dict(
            name="test-play",
            hosts=['all'],
            gather_facts='no',
            tasks=[]
        )
        play = Play().load(play_ds, variable_manager=variable_manager, loader=loader)
        # We need block to be parent block
        p_block = Block(play=play)
        # Create test data for task include

# Generated at 2022-06-13 09:31:53.457910
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    # use a mock object to simulate a task
    # use a mock object to simulate a play
    # use a mock object to simulate a block
    pass

# Generated at 2022-06-13 09:32:42.146877
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    t = TaskInclude(block=None)

    t.action = 'include_role'
    t.vars = {'var_a': 'a', 'var_b': 'b'}
    t.args = {'var_c': 'c', 'var_d': 'd'}
    t._parent = {'var_e': 'e', 'var_f': 'f'}

    assert t.get_vars() == {'var_a': 'a', 'var_b': 'b', 'var_c': 'c', 'var_d': 'd', 'var_e': 'e', 'var_f': 'f'}

    t.action = 'include_tasks'
    t.tags = ['test_tag']
    t.when = 'test_when'

    assert t.get_vars

# Generated at 2022-06-13 09:32:54.348570
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    t = TaskInclude()

    # Simple test with no parent
    assert t.get_vars() == dict()

    # Test with parent play
    p = Play().load(dict(
        name = "myplay",
        hosts = 'all',
        gather_facts = 'no',
        vars = {'a': 'b'}
    ), variable_manager=VariableManager(), loader=DataLoader())

    # Test with no include_tasks
    t = TaskInclude(block=p._block)
    assert t.get_vars() == dict(a='b')

    # Test with include_tasks
    t = TaskInclude(block=p._block)
    t.load_data(dict(action="include_tasks", file="file.yml"))

# Generated at 2022-06-13 09:33:09.056462
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():

    # test class
    class myClass(TaskInclude):
        # redefine the get_vars method
        def get_vars(self):
            return self.args.copy()

    # create a list of dicts
    ds = dict()
    ds['file'] = 'testfile'
    ds['_raw_params'] = 'testrawparams'
    ds['apply'] = {'var1': 'apply_var1', 'var2': 'apply_var2'}
    ds['tags'] = ['tag1', 'tag2']
    ds['when'] = 'test when'
    ds['args'] = {'var1': 'args_var1', 'var2': 'args_var2'}

# Generated at 2022-06-13 09:33:20.777797
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    ds = dict()
    ds['action'] = 'include_role'
    ds['name'] = "webserver"
    ti = TaskInclude.load(ds)
    ti_ds = ti.preprocess_data(ds)
    assert isinstance(ti_ds, dict)
    assert 'tags' not in ti_ds.keys()
    assert 'when' not in ti_ds.keys()
    ds['tags'] = 'test'
    ti_ds = ti.preprocess_data(ds)
    assert isinstance(ti_ds, dict)
    assert 'tags' in ti_ds.keys()
    assert 'when' not in ti_ds.keys()
    ds['when'] = 'test'
    ti_ds = ti.preprocess_data(ds)

# Generated at 2022-06-13 09:33:29.748836
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    ti = TaskInclude()
    ti.args = {'file': 'somewhere'}

    # Test the success case
    ti.check_options(ti, ti.args)

    # Test the failure cases
    with pytest.raises(AnsibleParserError) as err:
        ti.args = {'file': 'somewhere', 'bad': 'options'}
        ti.check_options(ti, ti.args)
    assert str(err.value) == "Invalid options for include: bad"

    # Test the failure cases for HandlerTaskInclude
    hti = TaskInclude()
    hti.action = 'meta: refresh_inventory'

# Generated at 2022-06-13 09:33:30.973783
# Unit test for method load of class TaskInclude
def test_TaskInclude_load():  # pylint: disable=unused-variable
    assert False

# Generated at 2022-06-13 09:33:41.788905
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():

    from ansible.playbook.play import Play

    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.handler_task_include import HandlerTaskInclude
    from ansible.playbook.role.definition import TaskDefinition
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    class FakePlay(Play):
        def __init__(self):
            self.context = PlayContext()
            self.become = False

    class FakeTask(Task):
        def __init__(self, parent, attrs):
            self._parent = parent
            self._