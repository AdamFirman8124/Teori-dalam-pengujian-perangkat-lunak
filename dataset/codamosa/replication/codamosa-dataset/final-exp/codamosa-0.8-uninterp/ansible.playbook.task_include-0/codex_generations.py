

# Generated at 2022-06-13 09:23:54.111988
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    from ansible.playbook.role.definition import Task as RoleTask
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins.loader import action_loader
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.executor.task_queue_manager import TaskQueueManager

    test_case_1 = {'_raw_params': 'xyz'}
    test_task = TaskInclude(block=None, task_include=None)
    assert test_task.check_options(test_task, test_case_1)


    from ansible.plugins.loader import filters_loader
    from ansible.plugins.loader import module_loader

# Generated at 2022-06-13 09:24:04.382607
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    class TestTaskInclude(TaskInclude):
        def __init__(self):
            self._parent = None
            self._role = None
            self._variable_manager = None
            self._loader = None

    def test_with_apply(self):
        ti = TestTaskInclude()
        ti.args = dict(apply=dict(loop='{{ test_loop }}'))
        blk = ti.build_parent_block()
        assert blk.loop == '{{ test_loop }}'
        assert isinstance(blk, Block)

    def test_without_apply(self):
        ti = TestTaskInclude()
        ti.args = dict()
        blk = ti.build_parent_block()
        assert blk is ti


# Generated at 2022-06-13 09:24:10.676837
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():

    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.vars.hostvars import HostVars
    from collections import namedtuple

    class FakeOptions:
        connection = 'local'
        module_path = None
        forks = 100
        remote_user = 'root'
        private_key_file = None
        ssh_common_args = None
        ssh_extra_args = None
        sftp_extra_args = None
        scp_extra_args = None
        become = False
        become_method = 'sudo'
        become_user = 'root'
        verbosity = False
        check = False

    # Setup Vars
    Options = FakeOptions()
    inventory = HostVars(loader=None, variable_manager=None)


# Generated at 2022-06-13 09:24:21.261877
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    '''
    Test that TaskInclude.get_vars returns the right values depending on the action and the existence of parent.
    '''
    #Create fake objects
    t = TaskInclude()
    #Test action different than 'include' and with parent
    t.action = 'not_include'
    t._parent = 'foo'
    assert t.get_vars() == 'foo'
    #Test action 'include' and with parent
    t.action = 'include'
    t.vars = {'vars': 'foo'}
    t.args = {'args': 'bar'}
    assert t.get_vars() == {'_parent': 'foo', 'args': 'bar', 'vars': 'foo'}
    #Test action 'include' and no parent
    t._parent = None
    assert t

# Generated at 2022-06-13 09:24:31.819356
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    import ansible.constants as C

    class TaskIncludeTest(TaskInclude):
        pass

    ds_old_style = dict(
        file='f2.yml',
        name='include example'
    )
    ds_new_style = dict(
        include='f2.yml',
        name='include example'
    )
    ds_old_style_with_unkown_key = dict(
        file='f2.yml',
        name='include example',
        unknownkey='somevalue'
    )
    ds_new_style_with_unkown_key = dict(
        include='f2.yml',
        name='include example',
        unknownkey='somevalue',
    )

# Generated at 2022-06-13 09:24:43.636422
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    # TaskInclude.preprocess_data({})
    assert TaskInclude.preprocess_data({}) == {}

    # TaskInclude.preprocess_data({'a': 'b'})
    assert TaskInclude.preprocess_data({'a': 'b'}) == {'a': 'b'}

    # TaskInclude.preprocess_data({'action': 'include', 'a': 'b'})
    assert TaskInclude.preprocess_data({'action': 'include', 'a': 'b'}) == {'action': 'include', 'a': 'b'}

    # TaskInclude.preprocess_data({'action': 'include_vars'})
    assert TaskInclude.preprocess_data({'action': 'include_vars'}) == {'action': 'include_vars'}

    # Task

# Generated at 2022-06-13 09:24:56.409469
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    # TaskInclude._validate_action will raise exception in case action is not in action list.
    # We mock the method to validate preprocess_data in case of static include ansible.cfg
    import ansible.playbook.task_include
    mock_validate_action = ansible.playbook.task_include.TaskInclude._validate_action
    ansible.playbook.task_include.TaskInclude._validate_action = lambda self: None

    class TestTaskInclude(TaskInclude):
        def __init__(self, ds):
            self.ds = ds
            self._parent = None
            self._attribute_plugins = None
            self._loader = None
            self._variable_manager = None
            self._role = None
            self._block = None
            self._task_include = None
            self._

# Generated at 2022-06-13 09:25:07.027364
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    from ansible.vars import VariableManager
    from ansible.playbook.play import Play
    from ansible.playbook.role import Role
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.plugins.loader import get_all_plugin_loaders

    loader = get_all_plugin_loaders()[0]
    variable_manager = VariableManager()
    play = Play().load({'hosts': 'all'}, variable_manager=variable_manager, loader=loader)
    role = Role()
    task = Task()
    play.add_role(role)
    role.add_task(task)

    data = {'action': 'include', 'args': {'apply': {'a': 1}} }

# Generated at 2022-06-13 09:25:19.492468
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():

    from ansible.playbook.play import Play
    from ansible.playbook.role import Role
    from ansible.vars.manager import VariableManager

    # create tasks
    data = dict(
        action=dict(
            meta=dict(
                name="include task with args",
                args=dict(
                    _raw_params="{{include_file}}",  # sets 'file'
                    debug=Sentinel,
                    x=1,  # sets 'args'
                    y=2,  # sets 'args'
                    z=3,  # sets 'args'
                )
            ),
            main=dict()
        )
    )
    ti = TaskInclude()

    # simulate 'preprocess_data'
    data = ti.preprocess_data(data)
    task = data['action']

    # simulate 'load

# Generated at 2022-06-13 09:25:33.386631
# Unit test for method load of class TaskInclude
def test_TaskInclude_load():
    '''
    Test case to validate TaskInclude's method load by
    checking the attributes set by load.
    :return:
    '''
    # This will fail..as there should be no action in include
    data_from_task_include_task = {
        'action': 'include',
        'file': '../../../common.yml',
        'tags': ['include'],
        'when': 'include'
    }

    me = TaskInclude.load(data_from_task_include_task, block=None, role=None, task_include=None)

    # Check for the 'action' attribute
    assert hasattr(me, 'action')

    # Check for the 'file' attribute
    assert hasattr(me, 'file')

    # Check for the 'tags' attribute

# Generated at 2022-06-13 09:25:43.355821
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    task_include = TaskInclude()
    apply_attrs = {
        'block': []
    }
    task_include.args['apply'] = apply_attrs
    task_include.build_parent_block()
    assert task_include.args == {}

# Generated at 2022-06-13 09:25:52.969002
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    def check_options(task, data, options):
        '''
        Function to create a mock class to call check_options of class TaskInclude
        '''
        class TaskIncludeMock:
            '''
            Class to mock TaskInclude
            '''
            class ActionBase:
                '''
                Class to mock ActionBase
                '''
                def __init__(self):
                    '''
                    Function to initialize ActionBase
                    '''
                    self._ACTION_ALL_PROPER_INCLUDE_IMPORT_TASKS = options

            def __init__(self):
                '''
                Function to initialize the mock class
                '''
                self.VALID_ARGS = TaskInclude.VALID_ARGS
                self.VALID_INCLUDE_KEYWORDS = TaskInclude.VALID_

# Generated at 2022-06-13 09:25:55.648282
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    t = TaskInclude()
    data = {'action': 'include', 'vars': {'foo': 'bar'}}
    assert t.preprocess_data(data) == {'action': 'include', 'vars': {'foo': 'bar'}}



# Generated at 2022-06-13 09:26:06.957161
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    import ansible.playbook.block as block

    b = block.Block()

    # 'include'
    action = 'include'
    task = TaskInclude(block=b, task_include=None)

    # check 'action'
    data = dict(action = action)
    task = task.check_options(task.load_data(data), data)
    assert data.pop('action') == task.action

    # check 'file'
    data = dict(action = action, file = 'test')
    task = task.check_options(task.load_data(data), data)
    assert data.pop('file') == task.args['_raw_params']

    # check 'apply'
    data = dict(action = action, apply = dict(loop = '{{test_loop}}'))
    task = task.check

# Generated at 2022-06-13 09:26:15.641008
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    task1 = TaskInclude(block=None, role=None, task_include=None)
    task1.action = 'include_role'
    task1.args = {'name': 'foo'}
    task1.vars = {'var1': 1, 'var2': 2}
    task1._parent = None

    vars1 = task1.get_vars()
    assert len(vars1) == 2
    assert vars1['var1'] == 1
    assert vars1['var2'] == 2

    task2 = TaskInclude(block=None, role=None, task_include=None)
    task2.action = 'include'
    task2.args = {'name': 'foo'}
    task2.vars = {'var1': 1, 'var2': 2}
    task

# Generated at 2022-06-13 09:26:20.043452
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    task = TaskInclude()
    ds = {}
    ds.update({
        'action': 'include_tasks',
        'file': 'test.yml',
        'test': 'test',
    })
    task.preprocess_data(ds)
    assert not ds.get('test')

# Generated at 2022-06-13 09:26:28.292778
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    variable_manager = DummyVariableManager()
    loader = DummyLoader()
    from ansible.playbook.play import Play
    from ansible.playbook import PlayContext
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.template import Templar
    play_ds = dict(
        name = "test play",
        hosts = "testhost",
        gather_facts = "no",
        connection = "local",
        roles = [
            "test_role",
        ],
        tasks = [
            dict(
                include = "test.yml",
                apply = dict(
                    block = [],
                ),
            )
        ],
    )

# Generated at 2022-06-13 09:26:37.584921
# Unit test for method load of class TaskInclude
def test_TaskInclude_load():
    '''
    Unit test to run test_TaskInclude_load
    ''

    Note: All other methods do not work without a defined task and are covered
    by load_data unit test in test_task.py: test_Task_load_data
    '''

    task_obj = TaskInclude(block=None, role=None, task_include=TaskInclude())
    yaml_object = {'action': 'include_tasks', 'file': 'post_op.yml'}
    task_action = 'include'
    task = task_obj.load(data=yaml_object, block=None, role=None, task_include=None, variable_manager=None, loader=None)
    assert task.args.get('_raw_params') == 'post_op.yml'
    assert task.action == task_

# Generated at 2022-06-13 09:26:49.643206
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    import unittest
    from ansible.parsing.dataloader import DataLoader

    from ansible.playbook import Play
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.block import Block

    class TaskIncludeTest(unittest.TestCase):
        def setUp(self):
            self._loader = DataLoader()
            self._variable_manager = VariableManager(loader=self._loader)

            self._host_pattern = 'all'
            self._hosts = 'localhost,'


# Generated at 2022-06-13 09:27:01.289080
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play

    play_context = PlayContext()
    play_context.extra_vars = dict(force='yes', max_log_size=10000000)
    play_context.prompt = ('Please enter a value for password: ', False)


# Generated at 2022-06-13 09:27:13.961973
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    from ansible.playbook.play import Play

    # create dummy Play
    play_ds = dict(
        name="some play",
        hosts='all',
        gather_facts='no'
    )
    pb = Play().load(play_ds, variable_manager=None, loader=None)

    # test for include
    task_ds = dict(
        file = "some_file.yml"
    )
    t = TaskInclude.load(task_ds, block=pb)
    assert t.args['_raw_params'] == 'some_file.yml'

    # test for action without apply
    task_ds = dict(
        file = "some_file.yml",
        action = "include_role"
    )
    t = TaskInclude.load(task_ds, block=pb)


# Generated at 2022-06-13 09:27:24.453885
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    from ansible.playbook.play import Play
    from ansible.playbook.block import Block
    from ansible.vars.manager import VariableManager
    from ansible.template.template import Templar

    data = {"include": {"apply": {"deprecated": "yes"}}, "deprecated": "ignored", "deprecated2": "ignored", "_role": None}

    p = Play.load(
        data,
        variable_manager=VariableManager(),
        loader=None,
    )

    ti = TaskInclude(block=Block(play=p, parent_block=None), role=None, task_include=None)
    ti.action = 'include'
    ti.vars = {'deprecated': 'no'}
    ti.vars['include'] = {'apply': {"deprecated": "yes"}}
    ti

# Generated at 2022-06-13 09:27:38.711354
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    # Load an include task, initialize it and verify validations
    ti = TaskInclude()
    # 1. HandlerTaskInclude task
    # load_data
    data = {'handler': 'main'}
    task = ti.load_data(data)
    task.post_validate(PlayContext(), DataLoader())
    # check_options
    assert ti.check_options(task, data) == task
    # 2. TaskInclude task
    # load_data
    data = {'include': 'main'}
    task = ti.load_data(data)
    task.post_validate(PlayContext(), DataLoader())
    #

# Generated at 2022-06-13 09:27:50.571245
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    '''
    Unit test for method check_options of class TaskInclude
    '''
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.task import Task

    data = {'action':'include', 'args':{'file':'tasks.yml', 'apply':{'a':1, 'b':2}}}

    task = Task(action='include')
    task.load_data(data)
    task = TaskInclude.check_options(task, data)

    assert task.args.get('_raw_params') == 'tasks.yml'
    assert task.args.get('apply') == {'a': 1, 'b': 2}

    data = {'action':'import_tasks', 'args':{'file':'tasks.yml'}}



# Generated at 2022-06-13 09:28:03.575659
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    # initialize a task include
    ti = TaskInclude()
    # create a dict of data to test with

# Generated at 2022-06-13 09:28:09.004277
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    from ansible.playbook.role.include import IncludeRole


# Generated at 2022-06-13 09:28:17.923172
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    '''
    Test that a valid parent block is created when the apply attribute is
    specified but not when apply is not specified
    '''
    # Create the TaskInclude instance
    ti = TaskInclude()
    ti.action = 'include_tasks'
    ti.args = {'apply': {'some': 'apply_attr'}}

    # Test if a Block is returned when apply is specified
    p_block = ti.build_parent_block()
    assert type(p_block) is Block

    # Test if a TaskInclude is returned when apply is not specified
    ti.args.pop('apply')
    p_block = ti.build_parent_block()
    assert type(p_block) is TaskInclude

# Generated at 2022-06-13 09:28:26.685026
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():

    yaml_data = dict(
        include = dict(
            file = 'foo.yml',
            vars = dict(
                a = 1,
                b = 2,
            ),
        )
    )

    PLAYBOOK_PATH = '/a_playbook_path'
    DATA_PATH = '/a_data_path'
    loader = None
    variable_manager = None

    task = TaskInclude.load(yaml_data['include'], loader=loader, variable_manager=variable_manager)
    assert task.get_vars()['file'] == 'foo.yml'
    assert task.get_vars()['vars'] == dict(a = 1, b = 2)
    assert task.get_vars().get('include') is None

# Generated at 2022-06-13 09:28:37.076562
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    import os

    role_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '..', 'test', 'units', 'support', 'roles', 'test_role')

    # The role has a role dependency, which contains a tasks/include_resources.yml file
    display.verbosity = 3

    ti = TaskInclude.load({'action': 'include', 'tasks': 'tasks/include_resources.yml', 'tags': ['include']})
    assert 'include' not in ti.get_vars()

    ti = TaskInclude.load({'action': 'include_role', 'name': 'test_role', 'tags': ['include_role']})
    assert 'include_role' not in ti.get_vars()

# Generated at 2022-06-13 09:28:45.384204
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    '''
    Testing build_parent_block of TaskInclude.

    This function test the following;
    - If apply is not specified, it will return the current task

    - If apply is specified, it will create a new Block with apply_attrs and
      return that block

    '''
    def create_block(fake_play, fake_role, fake_parent, fake_ti):
        '''
        Create new block with fake_play, fake_role, fake_parent and fake_ti.
        '''
        block = Block(fake_play, fake_role, fake_parent)
        block.name = "fake_block"
        block.parent = fake_parent
        block.role = fake_role
        block.task_include = fake_ti
        block.vars = fake_ti.args.pop('apply', {})


# Generated at 2022-06-13 09:29:05.766818
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.playbook.role_context import RoleContext

    block = Block()
    role_context = RoleContext(name='role1')
    play_context = PlayContext()
    play = Play().load({
        'name': 'test play',
        'hosts': 'all',
        'vars': {
            'test': 'play',
        },
    }, variable_manager=None, loader=None)
    block._play = play
    block._role = role_context
    block._parent = play_context
    # apply is specified
    apply_attrs = {
        'name': 'test',
        'do_something': 'test',
    }
    ret = block.build_parent_block()

# Generated at 2022-06-13 09:29:19.163367
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    # pylint: disable=unused-variable
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, sources=['localhost'])
    play_context = PlayContext()

    ti = TaskInclude.load({"apply": {"tags": "whitelisted", "when": "false"}}, variable_manager=variable_manager, loader=loader)
    p_block = ti.build_parent_block()
    assert p_block.tags == "whitelisted" # When should be ignored.

# Generated at 2022-06-13 09:29:33.848788
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    # set up test data
    task_data = dict(
        action='include_role',
        file='test_path',
        apply={'a': 'b'},
        v=1,
        loop=2,
        loop_control={'loop_var': 'item'},
    )

    # set up expected result
    expected_task_data = dict(
        action='include_role',
        file='test_path',
        v=1,
        loop=2,
        loop_control={'loop_var': 'item'},
    )
    expected_block_data = dict(
        block=list(),
        a='b',
    )
    expected_task_data_after_run = expected_task_data.copy()
    expected_task_data_after_run.pop('apply')

    # run

# Generated at 2022-06-13 09:29:41.958663
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    task = TaskInclude({})
    assert task.preprocess_data({'action': 'include', 'file': 'file.yml'}) == \
        {'action': 'include', 'file': 'file.yml'}
    assert task.preprocess_data({'action': 'include_tasks', 'file': 'file.yml'}) == \
        {'action': 'include_tasks', 'file': 'file.yml'}
    assert task.preprocess_data({'action': 'include_role', 'file': 'file.yml'}) == \
        {'action': 'include_role', 'file': 'file.yml'}

# Generated at 2022-06-13 09:29:49.520493
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.block import Block
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.task import Task

    loader = DataLoader()
    variable_manager = VariableManager()
    play_context = PlayContext()

# Generated at 2022-06-13 09:29:59.130919
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    from ansible.playbook.play import Play
    from ansible.playbook.role import Role
    from ansible.vars.manager import VariableManager

    variable_manager = VariableManager()
    play_ds = dict(
        name="Ansible Play",
        hosts='all',
        roles=[],
        tasks=[],
        vars_prompt=[],
        gather_facts='no',
    )

    role_ds = dict(
        name="role_x",
        tasks=[],
    )

    include_ds = dict(
        include='some_file',
        apply=dict(
            block=[]
        )
    )

    play = Play.load(
        play_ds,
        variable_manager=variable_manager,
        loader=None,
    )


# Generated at 2022-06-13 09:30:07.760135
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    task = TaskInclude.load(data={
                'action': 'include',
                'file': 'test_include.yaml',
                'loop': '{{ host_set }}',
                'debugger': '{{ debugger }}',
                'args': '{{ include_params }}',
                # The apply is a valid option for include only
                'apply': {'loop': '{{ apply_loop }}'}
            },
            variable_manager=None,
            loader=None
    )
    assert task.action == 'include'
    # There should be no tasks in parent block
    assert len(task.block._parent.block) == 0
    # The task should be in the block of the apply section of the task_include
    assert len(task.block.block) == 1
    # This should not raise any error
    task = TaskInclude

# Generated at 2022-06-13 09:30:19.260955
# Unit test for method load of class TaskInclude
def test_TaskInclude_load():
    ti = TaskInclude()
    data = {
        'apply': {
            'name': 'test apply',
            'debugger': 'test',
            'async': 10,
            'poll': 20
        },
        'file': 'test/file/path.yml',
        'include': 'test/include/path.yml'
    }

    task = ti.check_options(ti.load_data(data), data)

    # check the attributes set in method load
    assert task.action == 'include'
    assert task.args['_raw_params'] == 'test/include/path.yml'
    assert 'name' in task.args['apply']
    assert 'debugger' in task.args['apply']
    assert task.args['apply']['async'] == 10

# Generated at 2022-06-13 09:30:30.463384
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    """
    Test TaskInclude.preprocess_data()
    """

    test_play = dict(
        action=dict(
            meta=dict(
                type='include'
            ),
            args=dict(
                ignore_errors=True
            ),
            unknown_key='unknown_value',
            other_unknown_key='other_unknown_value'
        )
    )

    task_include = TaskInclude()
    included_play = task_include.preprocess_data(test_play)

    assert included_play.get('ignore_errors') is True
    assert included_play.get('unknown_key') is not Sentinel
    assert included_play.get('other_unknown_key') is not Sentinel
    assert included_play.get('unknown_key') == 'unknown_value'

# Generated at 2022-06-13 09:30:41.574521
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task_include import TaskInclude
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    # Dictionary to be used as input in the test, it contains the
    # raw data of a playbook and the value of _raw_params must be the
    # file name of a task included in the test_task_include_playbook.yml
    # file which has the same directory as this test
    test_data = dict(
        action='include',
        name='task include',
        file='/test_task_include_playbook.yml'
    )

    # Dictionary to be used as input in the test, it contains the


# Generated at 2022-06-13 09:31:05.211196
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    from ansible.playbook.play import Play
    from ansible.playbook.task_include import TaskInclude

    task_data = {}
    task_data['action'] = 'include'
    task_data['file'] = 'test.yml'
    task_data['_raw_params'] = 'test.yml'

    task = TaskInclude.load(task_data, play=Play().load(dict(
        name = "test play",
        hosts = 'webservers',
        gather_facts = 'no',
        tasks = [task_data]
    ), variable_manager=None, loader=None))
    ti = TaskInclude()

    # Wrong action
    task_data['action'] = 'included'
    task = ti.check_options(task, task_data)

# Generated at 2022-06-13 09:31:11.524502
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    TaskInclude.VALID_INCLUDE_KEYWORDS = TaskInclude.VALID_INCLUDE_KEYWORDS.union(('preprocessed',))
    t = TaskInclude(dict(preprocessed='true'))
    assert t.preprocessed == 'true'
    t = TaskInclude(dict(preprocessed='{{not_a_variable}}'))
    assert t.preprocessed == dict(preprocessed='{{not_a_variable}}')
    TaskInclude.VALID_INCLUDE_KEYWORDS = TaskInclude.VALID_INCLUDE_KEYWORDS.difference(('preprocessed',))

# Generated at 2022-06-13 09:31:19.784205
# Unit test for method load of class TaskInclude
def test_TaskInclude_load():
    # Setup the test
    data = {"action": "include_tasks", "file": "./test.yml"}
    ti = TaskInclude.load(data)

    assert ti.action == "include_tasks"
    assert ti._raw_params == "./test.yml"

    # test with bad file name
    data = {"action": "include_tasks"}
    try:
        TaskInclude.load(data)
    except AnsibleParserError as e:
        assert "No file specified" in e.message

    # test with bad args
    data = {"action": "include_tasks", "file": "./test.yml", "bad_arg": "bad"}

# Generated at 2022-06-13 09:31:30.510165
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():

    import ansible.plugins.loader as plugin_loader

    TaskInclude = plugin_loader.get_plugin('tasks', 'include')

    action = 'include'
    file = 'some_file'
    loop = 'with_items'
    loop_with = 'localhost'
    ds1 = dict({
        'action': action,
        'file': file,
        'loop': loop,
        'loop_with': loop_with,
        'bad_attr': 'some_attr',
    })

    ti = TaskInclude(block=None, role=None, task_include=None)
    ds2 = ti.preprocess_data(ds1)

    assert ds2['action'] == action
    assert ds2['file'] == file
    assert ds2['loop'] == loop

# Generated at 2022-06-13 09:31:37.180241
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():

    from ansible.playbook.task import Task

    ti = TaskInclude()

    # Load valid data
    valid_data = {
        'file': 'some_file.yml',
        'with_items': ['some_item'],
        'when': 'some_condition',
    }
    task = Task.load(valid_data)
    ti.check_options(task, valid_data)

    # Load invalid data
    invalid_data = {
        'some_param': 'some_value',
        'file': 'some_file.yml',
    }
    task = Task.load(invalid_data)
    try:
        ti.check_options(task, invalid_data)
    except AnsibleParserError:
        pass

# Generated at 2022-06-13 09:31:43.476493
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():

    # Test: validate_options for 'include'
    assert TaskInclude.VALID_ARGS == frozenset(['file', '_raw_params', 'apply'])
    task = TaskInclude()
    task_data = {'action': 'include', 'ignore_errors': True}
    task = task.check_options(task.load_data(task_data), task_data)
    assert task.args == {'_raw_params': None, 'ignore_errors': True}

    # Test: validate_options for 'include_tasks'
    assert TaskInclude.VALID_ARGS == frozenset(['file', '_raw_params', 'apply'])
    task = TaskInclude()
    task_data = {'action': 'include_tasks'}

# Generated at 2022-06-13 09:31:52.653378
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext

    mock_loader = DataLoader()
    mock_inventory = InventoryManager(loader=mock_loader, sources=[])
    mock_variable_manager = VariableManager(loader=mock_loader, inventory=mock_inventory)
    mock_context = PlayContext()

# Generated at 2022-06-13 09:31:59.500928
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    data = {
        'action': 'include_role',
        'tags': ['foo', 'bar'],
        'tasks': [
            {'action': 'copy', 'dest': '/tmp'},
        ],
    }

    ti = TaskInclude()
    block = Block.load(data, task_include=ti)
    assert isinstance(block, Block)
    assert len(block._block) == 1
    t = block._block[0]
    assert isinstance(t, Task)
    assert t.action == 'copy'

    data['apply'] = {'tags': ['foo']}
    block = Block.load(data, task_include=ti)
    assert isinstance(block, Block)
    assert len(block._block) == 1
    assert block.tags == ['foo']


# Generated at 2022-06-13 09:32:07.724131
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    t = TaskInclude()
    assert not t.get_vars()
    t.action = 'include'
    assert not t.get_vars()
    t.action = 'include_role'
    assert not t.get_vars()
    t.action = 'import_tasks'
    assert not t.get_vars()
    t.action = 'include_tasks'
    assert not t.get_vars()
    t.action = 'set_fact'
    assert not t.get_vars()
    t.vars = {'a': 'b'}
    assert t.get_vars() == {'a': 'b'}
    t.action = 'include'
    assert t.get_vars() == {'a': 'b'}

# Generated at 2022-06-13 09:32:15.571110
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    ti = TaskInclude()
    ds = ti.preprocess_data({'action': 'include_role', 'name': 'myrole'})
    assert 'name' in ds
    assert ds['name'] == 'myrole'
    assert 'file' not in ds
    assert 'apply' not in ds

    ds = ti.preprocess_data({'action': 'include', 'file': '/tmp/foo'})
    assert 'file' not in ds
    assert 'apply' not in ds
    assert '_raw_params' in ds
    assert ds['_raw_params'] == '/tmp/foo'

    ds = ti.preprocess_data({'action': 'include', 'apply': {'ignore_errors': True}})
    assert 'file' not in ds

# Generated at 2022-06-13 09:32:53.284770
# Unit test for method load of class TaskInclude
def test_TaskInclude_load():
    '''
    Unit test to verify that the TaskInclude class will raise an exception
    when calling load with the wrong args and action.
    '''
    try:
        ti = TaskInclude()
        ti.load({'action': 'script', 'args': {'file': 'some_file', 'bad_arg': 'some_value'}})
    except AnsibleParserError as exception:
        assert exception.message == 'Invalid options for script: bad_arg'
    else:
        assert False, "Expected AnsibleParserError to be raised"



# Generated at 2022-06-13 09:33:08.213592
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    from ansible.playbook.handlertaskinclude import HandlerTaskInclude

    # data for TaskInclude
    data = dict(action='include', file='/tmp/test')
    data_ = data.copy()
    data_['apply'] = {}
    data__ = data_.copy()
    data__['test'] = 'test'
    data___ = data.copy()
    data___['test'] = 'test'

    # test TaskInclude
    ti = TaskInclude()
    ti.check_options(ti.load_data(data, variable_manager=None, loader=None), data)
    ti.check_options(ti.load_data(data_, variable_manager=None, loader=None), data_)

# Generated at 2022-06-13 09:33:20.197849
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.role.definition import RoleDefinition

    def _get_task(action):
        play = Play().load({'name': 'test play', 'hosts': 'all'}, variable_manager=None, loader=None)
        role_definition = RoleDefinition(name='test role', play=play)
        task = TaskInclude(block=role_definition, task_include=None)
        task.action = action
        return task

    def _get_data(file_name=None, **kwargs):
        if file_name is None:
            file_name = 'test.yaml'
        raw_params = 'test_params'
        if file_name:
            kwargs['file'] = file_name

# Generated at 2022-06-13 09:33:28.883491
# Unit test for method load of class TaskInclude
def test_TaskInclude_load():

    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.inventory.inventory import Inventory
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    # Fake inventory for passing to the constructor
    group = Group('test group')
    group.vars['test_var'] = 'test_var_value'
    host = Host('test_host')
    host.vars['host_var'] = 'host_var_value'
    group.add_host(host)
    inv = Inventory(loader=DataLoader())
    inv.add_group(group)
    inv.add_host(host)

    # Vars manager
    var_manager = VariableManager(loader=DataLoader(), inventory=inv)


    #################################

# Generated at 2022-06-13 09:33:40.090691
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play

    from ansible.playbook.block import Block
    from ansible.playbook.role.task_include import TaskInclude
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.task_queue_manager import TaskQueueManager

    import pytest

    context = PlayContext()