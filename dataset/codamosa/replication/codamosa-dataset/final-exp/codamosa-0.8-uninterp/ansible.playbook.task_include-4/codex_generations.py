

# Generated at 2022-06-13 09:23:46.152085
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():

    ti_1 = TaskInclude(action='include_role')
    assert not ti_1.preprocess_data(dict(foo='bar'))

    ti_2 = TaskInclude(action='include')
    assert not ti_2.preprocess_data(dict(foo='bar'))

    ti_3 = TaskInclude(action='import_role')
    assert not ti_3.preprocess_data(dict(foo='bar'))

    ti_4 = TaskInclude(action='include_tasks')
    assert not ti_4.preprocess_data(dict(foo='bar'))



# Generated at 2022-06-13 09:23:55.857555
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    # role: foo
    #    baz.yml
    #    meta
    #       main.yml
    #       foo.yml
    #
    roles_path = [
        'tests/support/foo'
    ]
    # use first role in roles_path
    role_name = os.path.split(roles_path[0])[-1]
    # load 'meta/main.yml' as it imports 'foo.yml' that we want to test
    play_source = dict(
        name="Ansible Play",
        hosts='all',
        gather_facts='no',
        roles=[role_name, ],
        vars=dict(
            role_path=roles_path,
            playbook_dir='playbook',
            role_name=role_name,
        )
    )

# Generated at 2022-06-13 09:24:01.138870
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    class TestTaskInclude(TaskInclude):
        '''
        Subclass to override some methods with our mock so we can test
        the check_options method of the parent class
        '''

        def load_data(self, data, variable_manager=None, loader=None):
            return data

        def check_valid_tags(self, task_ds):
            pass

    ds = dict(action='import_role')
    task = TestTaskInclude(task_include=True)
    task = task.check_options(task, ds)
    assert task.args['apply'] == {}
    assert not task.args['_raw_params']

    ds = dict(action='include_role')
    task = TestTaskInclude(task_include=True)
    task = task.check_options(task, ds)


# Generated at 2022-06-13 09:24:15.537109
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, variable_manager=variable_manager, host_list=[])
    variable_manager.set_inventory(inventory)

    task = TaskInclude.check_options(TaskInclude(), {'action': 'inc_action', '_raw_params': 'raw_params'})
    assert task.action == 'inc_action'
    assert task.args['_raw_params'] == 'raw_params'

    task = TaskInclude.check_options(TaskInclude(), {'action': 'inc_action', 'file': 'raw_params'})

# Generated at 2022-06-13 09:24:26.846241
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    class TestTask(TaskInclude):

        def __init__(self, ds, block=None, role=None, task_include=None):
            self.action = 'include'
            self.vars = dict()
            self.args = dict()
            self.tags = None
            self._role = role
            self._parent = None

        def get_vars(self):
            return super(TestTask, self).get_vars()

    t1 = TestTask({'file': 'foo.yaml'})
    vars = t1.get_vars()
    assert vars == {'file': 'foo.yaml'}, vars

    t2 = TestTask({'include': 'foo.yaml'})
    vars = t2.get_vars()

# Generated at 2022-06-13 09:24:34.453643
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    display = Display()
    display.verbosity = 3
    task = TaskInclude(None)

    assert task.preprocess_data({'action': 'include_tasks'}) == {'action': 'include_tasks'}, 'Failed to include_tasks'
    assert task.preprocess_data({'action': 'include_role'}) == {'action': 'include_role'}, 'Failed to include_role'
    assert task.preprocess_data({'action': 'import_role'}) == {'action': 'import_role'}, 'Failed to import_role'
    assert task.preprocess_data({'action': 'import_tasks'}) == {'action': 'import_tasks'}, 'Failed to import_tasks'

    # static include

# Generated at 2022-06-13 09:24:45.203436
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    from ansible.playbook.role.task_include import TaskInclude
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.utils.sentinel import Sentinel

    # setup
    data = {
        'action': 'include_tasks',
        'file': 'test.yml',
        'tags': ['some'],
        'when': 'some'
    }
    variable_manager = None
    loader = None
    t_include = TaskInclude.load(
        data, variable_manager=variable_manager, loader=loader)

    # test
    task = TaskInclude.check_options(t_include, data)

    # assert
    assert task.action == 'include_tasks'
    # 'action' is not a valid attribute and it is among given keywords

# Generated at 2022-06-13 09:24:57.876768
# Unit test for method load of class TaskInclude
def test_TaskInclude_load():
    # Test for load and check_options, fail on bad options
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play_context import PlayContext
    import os

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, sources=('localhost,'))
    variable_manager.set_inventory(inventory)
    play_context = PlayContext()

    # Bad options
    ti = TaskInclude(block='hello', role='world', task_include='!')

    data = {'action': 'include', 'bad_option': 'bad_value'}

# Generated at 2022-06-13 09:25:08.010551
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    class Fake1:
        class Fake2:
            def get_vars(self):
                return dict(x=2)

        def get_vars(self):
            return dict(y=1)

        def __init__(self):
            self._parent = self.Fake2()

    class Fake3:
        pass

    class Fake4(Fake3):
        def get_vars(self):
            return dict(x=2)

    # fake1 is a Block with a parent
    assert TaskInclude(block=Fake1()).get_vars() == dict(x=2, y=1)
    # fake3 is a child of Block
    assert TaskInclude(block=Fake3()).get_vars() == dict()
    # fake4 is a child of Block with a get_vars method defined
    assert Task

# Generated at 2022-06-13 09:25:17.208080
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    task_include = TaskInclude()
    task_include._action = "include"
    data = {'a': 'b', 'c': 'd'}
    data = task_include.preprocess_data(data)
    assert data == {'c': 'd'}

    task_include._action = "rescue"
    data = {'e': 'f', 'g': 'h'}
    data = task_include.preprocess_data(data)
    assert data == {'e': 'f', 'g': 'h'}

# Generated at 2022-06-13 09:25:33.920161
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    from collections import namedtuple
    from ansible.playbook.play import Play
    from ansible.playbook.role import Role
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.role_context import RoleContext

    # Build the following play:
    #
    # vars:
    # - a: 1
    #   b: 2
    #
    # pre_tasks:
    # - name: pre1
    #   block:
    #     - name: task1
    #       block:
    #         - name: task2
    #           include:
    #             - file: test_TaskInclude_get_vars.yaml
    #               variables:
   

# Generated at 2022-06-13 09:25:46.037759
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    task_include = TaskInclude()
    my_task = Task()
    my_task.action = 'include'
    # validate when everything is ok
    my_task.args = {'file': 'file-name.yml'}
    task = task_include.check_options(my_task, my_task.args)
    assert '_raw_params' in task.args.keys() and 'file' not in task.args.keys()
    assert task.args['_raw_params'] == 'file-name.yml'
    # raise an error when there is an unknown option
    my_task.args = {'file': 'file-name.yml', 'unknown_option': 'option_value'}

# Generated at 2022-06-13 09:25:55.091669
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    from ansible.playbook.block import Block
    from ansible.playbook.play import Play
    from ansible.plugins.loader import include_tasks_loader

    # Create a block which is required for the TaskInclude.load()
    pb = Play.load(dict(
        name = "test_TaskInclude_preprocess_data",
        hosts = 'all',
        gather_facts = 'no',
        tasks = []
    ))
    block = Block.load(dict(
        name = 'test_TaskInclude_preprocess_data',
        tasks = [],
    ), play=pb)

    # Test TaskInclude.load() with a single task include
    test_data1 = [{
        'include': 'my_tasks.yml',
        'myattr': 1
    }]
    tasks_

# Generated at 2022-06-13 09:26:06.537867
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block(): # FIXME: there should be a better way to organize unit-tests for this class
    from ansible.playbook.play import Play
    from ansible.playbook.playbook import TaskList, Playbook
    from ansible.playbook.role import Role
    from ansible.playbook.role.include import RoleInclude
    from ansible.playbook.role.task import Task as RoleTask
    from ansible.playbook.task_include import TaskInclude
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager


# Generated at 2022-06-13 09:26:15.366440
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    # In this test, we want to make sure that the args attribute of the
    # include are added to the vars before the vars of the parent task
    vars_file = {
        'a': 1,
        'b': 2,
        'c': 3,
    }
    vars_include = {
        'd': 4,
        'e': 5,
        'f': 6,
    }
    vars_parent = {
        'g': 7,
        'h': 8,
        'i': 9,
    }

    # _update_hash_vals() must be called on a dict or the keys will be
    # converted to unicode and won't match the strings in the get_vars() test
    FieldAttribute.ensure_not_local({}, 'foo')

    # Create a block (parent) and

# Generated at 2022-06-13 09:26:20.902088
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    print("Running test_TaskInclude_build_parent_block")

    class Field:
        def __init__(self, fieldname):
            self.name = fieldname

    class ParentTask:
        def __init__(self, **kwargs):
            for field in ('_variable_manager', '_loader'):
                setattr(self, field, kwargs.get(field))

            setattr(self, '_play', kwargs.get('play'))

        def get_vars(self):
            return {'parent_var': '...'}


    parent_task = ParentTask(
        _variable_manager=None,
        _loader=None,
        play=None,
    )


# Generated at 2022-06-13 09:26:28.745506
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    from ansible.playbook.play_context import PlayContext
    from ansible.utils.sentinel import Sentinel

    from ansible.playbook.block import Block

    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.role.include import RoleInclude

    from ansible.playbook.task.meta import MetaTask

    from ansible.playbook.handler.task_include import HandlerTaskInclude

    p_block = Block()
    p_block._play = Sentinel
    p_block.role = Sentinel
    p_block.vars = {}
    p_block.apply_defaults = None
    p_block.loop = None
    p_block.block = Block()
    p_block.loop_control = None
    p_block.always_run = []
    p_block.res

# Generated at 2022-06-13 09:26:37.757774
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    '''
    Test if the method build_parent_block creates the parent block
    when ``apply`` keyword is present in the data dict
    '''
    import unittest
    import ansible.playbook.play
    import ansible.playbook.block
    import ansible.playbook.task_include
    import ansible.playbook.role

    from ansible.playbook.task import Task

    class TestTaskInclude(unittest.TestCase):
        '''
        Unit test for TaskInclude class
        '''
        class TestPlay(ansible.playbook.play.Play):
            '''
            Play class for unit testing only.
            '''
            pass

        class TestBlock(ansible.playbook.block.Block):
            '''
            Block class for unit testing only.
            '''

# Generated at 2022-06-13 09:26:49.698570
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():

    def _preprocess_data(task, data):
        ti = TaskInclude()
        return ti.preprocess_data(data)

    data = dict(action='include_role', name='some_name')
    assert _preprocess_data(TaskInclude(), data) == data

    # invalid data should be discarded. The result should have exactly the same keys
    data = dict(action='include_role', name='some_name', invalid_key='some_value')
    assert _preprocess_data(TaskInclude(), data) == data.copy()

    data = dict(action='include_role', name='some_name', apply={})
    assert _preprocess_data(TaskInclude(), data) == data

    data = dict(action='include_role', name='some_name', apply=1)

# Generated at 2022-06-13 09:27:01.316032
# Unit test for method get_vars of class TaskInclude

# Generated at 2022-06-13 09:27:13.014559
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    # The TaskInclude class does not inherit from Task, so it has to be tested separately
    task = TaskInclude()

    # TaskInclude cannot be initialized directly, so we test the get_vars method
    # as it stands in the library
    # Look at line 2468 in library/ansible/playbook/task_include.py:
    #   new_me.args = self.args
    task.args = {
        '_raw_params': '',
        'file': 'foo.yml',
        'collections': [
            'foo-1.0.0',
            'bar-0.1.0'
        ],
        'x': 'foobar',
        'y': 'zap'
    }
    
    # The copied task is tested against the expected variables

# Generated at 2022-06-13 09:27:19.687358
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    task_include = TaskInclude()
    ds = dict(action='include', x=1, y=2)
    ds = task_include.preprocess_data(ds)
    assert ds.get('action') == 'include' and ds.get('x') == 1 and ds.get('y') == 2

    ds = dict(action='import_tasks', x=1, y=2)
    ds = task_include.preprocess_data(ds)
    assert ds.get('x') is None and ds.get('y') is None

    ds = dict(action='import_playbook', x=1, y=2)
    ds = task_include.preprocess_data(ds)
    assert ds.get('x') is None and ds.get('y') is None



# Generated at 2022-06-13 09:27:27.842498
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    import ast
    import json
    data = """
- name: include a task file
  include: stuff.yml
  tags:
    - debug
  when: combination[1]==1
  loop: "{{ query('url', 'http://localhost:9000') }}"
  loop_control:
    loop_var: combination
"""
    # Note that the list of vars is not filtered by include_vars and set_fact
    # tasks (yet)
    all_vars = {'inventory_hostname': 'webserver01'}
    ti = TaskInclude.load(ast.literal_eval(json.dumps(data)), variable_manager=all_vars)

# Generated at 2022-06-13 09:27:38.806289
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    # Scenario:
    # TaskInclude.check_options was called with valid parameters
    # It is expected that task object is returned
    from ansible.playbook.task_include import TaskInclude
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText

    data = {"action": "include_tasks", "file": "test.yml"}
    vm = VariableManager()
    loader = DataLoader()
    ti = TaskInclude()
    ti.action = "include_tasks"
    ti.args = {"file": AnsibleUnsafeText("test.yml"), "_raw_params": "test.yml"}
    assert ti.check_options(ti, data) == ti



# Generated at 2022-06-13 09:27:50.683023
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    # test with values
    task_include_with_apply = TaskInclude()
    task_include_with_apply.args = {
        'apply': {
            'apply': 'all',
            'when': 'cond1'
        },
        'file': 'test_file.yml'
    }
    parent_block1 = task_include_with_apply.build_parent_block()
    assert parent_block1.apply == 'all'
    assert parent_block1.when is 'cond1'
    assert parent_block1.block is []

    # test with apply attributes as null
    task_include_without_apply = TaskInclude()
    task_include_without_apply.args = {
        'apply': None,
        'file': 'test_file.yml'
    }

# Generated at 2022-06-13 09:28:03.837100
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    from ansible.playbook import Play
    from ansible.playbook.block import Block
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    variable_manager = VariableManager()
    loader = DataLoader()

    sample_play = {
        'hosts': [
            'localhost',
        ],
        'roles': [
            'database'
        ],
        'tasks': [
            {
                'block': [
                    {
                        'include': {
                            'apply': {
                                'when': 'ansible_os_family == "Debian"'
                            }
                        }
                    },
                ]
            }
        ]
    }
    # Overwrite actual play_source for test purpose
    Play.play_source = "localhost"

# Generated at 2022-06-13 09:28:15.007101
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    from ansible.playbook.play import Play
    from ansible.playbook.role.include import IncludeRole

    play_ds = dict(
        name = "Ansible Play",
        hosts = 'all',
        gather_facts = 'no',
        tasks = [
            dict(include='test.yml', apply=dict(freeform=True, some_test='test'))
        ]
    )

    play = Play.load(play_ds)
    play.load()

    # define _role and _parent
    role = IncludeRole.load(dict(name='test-include', tasks='test.yml'),
                            play=play)
    play._included_file = dict(path='test.yml')
    play._included_file['role'] = role

    role.load()

    taskds = dict

# Generated at 2022-06-13 09:28:25.443031
# Unit test for method load of class TaskInclude
def test_TaskInclude_load():

    from ansible.playbook import Playbook
    from ansible.playbook.helpers import load_list_of_tasks
    from ansible.playbook.play_context import PlayContext

    cls_path = 'ansible.parsing.dataloader.DataLoader'
    with patch(cls_path):

        def loader_mock_constructor(self, *args, **kwargs):
            pass

        def create_task(action, apply_dict, raw_params):
            # create task
            task = {}
            task['action'] = action
            task['apply'] = apply_dict
            task['file'] = raw_params

            return task


# Generated at 2022-06-13 09:28:35.198958
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.role.role import Role
    from ansible.playbook.handler.handler import Handler
    import ansible.constants as C
    import random
    import string

    C.DEFAULT_HANDLER_TASK_NAME = 'handler'
    C.DEFAULT_TASK_NAME = 'task'

    t = Task()
    r = Role()
    p = Play()

    a_dict = dict()
    a_dict['apply'] = dict()

    test_data = dict()
    test_data['block'] = a_dict['apply']

# Generated at 2022-06-13 09:28:43.808265
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    '''
    Unit test for method get_vars of class TaskInclude
    '''
    ## initialize for TaskInclude
    #   initialize for class Task
    #       initialize for class Block
    #       include for class Block
    #       include for class Block
    #       include for class Block
    #       include for class Block
    #       include for class Block
    #       include for class Block
    #       initialize for class Play
    #       include for class Play
    #   include for class Task
    #   include for class Task
    #   include for class Task
    #   include for class Task
    #   include for class Task
    #   include for class Task
    #   include for class Task
    #   include for class Task
    #   include for class Task
    #   include for class Task
    #   include for class Task


# Generated at 2022-06-13 09:28:54.307822
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    '''
    Test TaskInclude.preprocess_data with the following tasks:
        - include: ...
        - import_playbook: ...
        - include_role: ...
        - include_tasks: ...
        - include_vars: ...
    '''
    # Creating sample objects
    variable_manager = None
    loader = None
    block = None
    role = None
    task_include = None
    ds = None

    # Testing include
    ds = dict(action='include', file='/home/test.yml', ignore_errors=True)
    ti = TaskInclude(block=block, role=role, task_include=task_include)
    result = ti.preprocess_data(ds)
    assert result['file'] == '/home/test.yml'
    assert result['ignore_errors']

# Generated at 2022-06-13 09:29:04.177999
# Unit test for method load of class TaskInclude
def test_TaskInclude_load():
    task = TaskInclude()
    data = {'action': 'include', 'file': 'test.yml'}
    task.load(data, variable_manager=None, loader=None)

    assert('file' in task.args)
    assert(task.args['file'] == 'test.yml')
    assert('action' in task.actions)
    assert(task.actions['action'] == 'include')
    assert('include' in task.action)
    assert(task.action['include'] == 'test.yml')
    assert(task.action['include_action'] == 'include')
    assert(task.action['include_name'] == 'INCLUDE')
    assert(task.action['include_role'] is None)
    assert(task.action['include_tasks'] is None)


# Generated at 2022-06-13 09:29:15.155152
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins.loader import action_loader
    from ansible.executor.playbook_executor import PlaybookExecutor


# Generated at 2022-06-13 09:29:24.313759
# Unit test for method load of class TaskInclude
def test_TaskInclude_load():

    class TestTask(Task):
        def __init__(self, block=None, role=None, task_include=None):
            super(TestTask, self).__init__(block=block, role=role, task_include=task_include)

        @staticmethod
        def load(data, block=None, role=None, task_include=None, variable_manager=None, loader=None):
            return TestTask(block=block, role=role, task_include=task_include)

    TestInclude = TaskInclude.load(data={'action':'name', 'file':'tests/unit/test_task_include.py'}, task_include=TestTask())
    assert 'action' in TestInclude.args
    assert TestInclude.args['action'] == 'name'

# Generated at 2022-06-13 09:29:31.568467
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    ti = TaskInclude()
    assert ti.preprocess_data({'action': 'include_role'}) == {'action': 'include_role'}
    assert ti.preprocess_data({'action': 'include_role', 'x': 'y', 'z': 't'}) == {'action': 'include_role', 'x': 'y', 'z': 't'}
    assert ti.preprocess_data({'action': 'include_tasks'}) == {'action': 'include_tasks'}
    assert ti.preprocess_data({'action': 'import_role'}) == {'action': 'import_role'}
    assert ti.preprocess_data({'action': 'import_tasks'}) == {'action': 'import_tasks'}

# Generated at 2022-06-13 09:29:40.652055
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    import yaml
    from ansible.vars.manager import VariableManager
    from ansible.vars.hosting import HostVars
    from ansible.playbook.play_context import PlayContext
    from ansible.parsing.yaml.objects import AnsibleUnicode, AnsibleSequence
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.play_iterator import PlayIterator
    from ansible.inventory.manager import InventoryManager

    my_vars = dict(a=1, b=2)
    hvars = HostVars(
        "localhost",
        variables=my_vars
    )

    variable_manager = VariableManager()
    variable_manager.set_inventory(InventoryManager(loader=None, sources=''))
    variable_manager.add_

# Generated at 2022-06-13 09:29:46.805682
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    from collections import namedtuple
    TestArgs = namedtuple("TestArgs", ("action", "expected"))

    for test_args in TestArgs("include", True), TestArgs("import_tasks", True), TestArgs("import_role", True), TestArgs("include_role", True):
        ds = dict(static=Sentinel, action=test_args.action)
        ti = TaskInclude()
        result = ti.preprocess_data(ds)
        assert result.get("action") == test_args.action
        assert result.get("static") == test_args.expected

# Generated at 2022-06-13 09:29:57.081040
# Unit test for method load of class TaskInclude
def test_TaskInclude_load():
    import ansible.playbook.task_include
    task = ansible.playbook.task_include.TaskInclude.load(dict(action='include_tasks', file='roles/common/tasks/main.yml'), variable_manager=None, loader=None)
    assert str(task.action) == 'include_tasks'
    assert task.args.get('_raw_params') == 'roles/common/tasks/main.yml'
    assert task.args.get('file') is None

    task = ansible.playbook.task_include.TaskInclude.load(dict(action='include_tasks', file='roles/common/tasks/main.yml', loop_with='item'), variable_manager=None, loader=None)

# Generated at 2022-06-13 09:30:04.919495
# Unit test for method load of class TaskInclude
def test_TaskInclude_load():
    from ansible.playbook.play import Play
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    variable_manager = VariableManager()
    loader = None
    play = Play().load({
        'name': 'testplay',
        'hosts': 'all',
        'gather_facts': 'no'
    }, variable_manager=variable_manager, loader=loader)
    inventory = InventoryManager(loader=loader, sources='localhost')
    variable_manager.set_inventory(inventory)
    templar = Templar(loader=loader, variables=variable_manager.get_vars(play=play))


# Generated at 2022-06-13 09:30:16.383088
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    import json
    def print_vars(var_set):
        print(json.dumps(var_set, indent=4))

    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory

    variable_manager = VariableManager()
    loader = DataLoader()
    inventory = Inventory(loader=loader, variable_manager=variable_manager, host_list='localhost')
    variable_manager.set_inventory(inventory)

    # ## include
    ds = {'name': 'include',
          'action': 'include',
          'args': {'x': 3}}
    ti = TaskInclude.load(ds, variable_manager=variable_manager)
    ti.vars = {'x': 1}

# Generated at 2022-06-13 09:30:26.841096
# Unit test for method load of class TaskInclude
def test_TaskInclude_load():
    from ansible.playbook.play_context import PlayContext
    from ansible.vars import VariableManager
    from ansible.template.safe_eval import safe_eval
    from ansible.parsing.dataloader import DataLoader

    context = PlayContext()
    context.set_options(default_vars=dict(a=1))
    context.set_options(apply=dict(b=2))
    context.user_variables.update(dict(a=3, c=dict(d=4)))

    a_loader = DataLoader()
    a_loader.set_basedir(C.DEFAULT_VAULT_IDENTITY_LIST[0])
    var_manager = VariableManager(loader=a_loader)
    var_manager.set_inventory(None)


# Generated at 2022-06-13 09:30:38.341133
# Unit test for method load of class TaskInclude
def test_TaskInclude_load():
    """
    Test the method TaskInclude.load

    :return:
    """
    from ansible.vars.manager import VariableManager
    import ansible.playbook.play as pb_play
    from ansible.playbook.play_context import PlayContext

    # import the config
    from ansible.config.manager import ConfigManager
    config_manager = ConfigManager()
    config_manager.load()

    # import the loader
    from ansible.loader.loader import DataLoader
    loader = DataLoader()

    # import the inventory
    from ansible.inventory.manager import InventoryManager
    inventory = InventoryManager(loader=loader, sources=[])

    # import the variable manager
    variable_manager = VariableManager(
        loader=loader,
        inventory=inventory)

    play_context = PlayContext()

    # import the play


# Generated at 2022-06-13 09:30:45.686424
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    # when 'apply' is specified
    ti = TaskInclude(block=None, role=None, task_include=None)
    ti.args = {'apply': {'block': []}}
    p_block = ti.build_parent_block()
    assert p_block.args == {'block': []}

    # when 'apply' is not specified
    ti = TaskInclude(block=None, role=None, task_include=None)
    p_block = ti.build_parent_block()
    assert p_block == ti


# Generated at 2022-06-13 09:30:55.216341
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    test_inc = TaskInclude()
    test_inc.args = {}
    test_inc.vars = {}
    test_inc.action = 'include_tasks'
    test_inc._parent = None
    assert test_inc.get_vars() == {}

    test_inc.args = {'x': 'y'}
    test_inc.vars = {'a': 'b'}
    test_inc.action = 'include_tasks'
    assert test_inc.get_vars() == {'a': 'b', 'x': 'y'}

    test_inc.args = {'x': 'y'}
    test_inc.vars = {'a': 'b'}
    test_inc.action = 'include_role'
    test_inc._parent = FieldAttribute(Sentinel())

# Generated at 2022-06-13 09:31:06.356912
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    # Test to check the values returned by the get_vars method of TaskInclude
    # as they are different from the Task class:

    # Variable memoization is disabled
    C.DEFAULT_CACHE_PLUGIN = None

    # Creating a Mock object for the class FieldAttribute.
    mock_obj = FieldAttribute.FieldAttribute(sentinel=None, default='test_val')

    # Creating a Mock object for the class Play.
    mock_play_obj = MagicMock()
    mock_play_obj.get_vars = Mock(return_value = mock_obj)

    # Creating a Mock object for the class Role.
    mock_role_obj = MagicMock()
    mock_role_obj.get_vars = Mock(return_value = mock_obj)

    # Creating a Mock object for the class Loader.


# Generated at 2022-06-13 09:31:13.222697
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():

    class MyTaskInclude(TaskInclude):
        def __getattr__(self, name):
            return []

    ti = MyTaskInclude(block=None, task_include=None)
    ti._parent = MyTaskInclude(block=None, task_include=None)
    ti.vars = {'a': '1'}
    ti._parent.vars = {'b': '2'}
    ti.args = {'c': '3'}

    # We should not have 'tags' and 'when' in the returned vars
    ti.vars['tags'] = '4'
    ti.vars['when'] = '5'
    ti.args['tags'] = '6'
    ti.args['when'] = '7'
    vars = ti.get_vars().keys()

# Generated at 2022-06-13 09:31:20.622595
# Unit test for method load of class TaskInclude
def test_TaskInclude_load():
    def apply(x):
        return x

    def check_options(task, data):
        return task

    class TaskIncludeMock(TaskInclude):
        def __init__(self, *args):
            pass

        @staticmethod
        def load_data(data, *args):
            return data

        @staticmethod
        def check_options(task, data):
            return task

    # NOTE: The file to include can be specified in the form of an absolute
    # path, relative to the location of the executing playbook, or as a
    # literal in the format of yaml.
    #
    # TaskInclude settings:
    #     file:
    #         literal: '---\n- name: test\n  command: /bin/true\n'
    #     ignore_errors: True
    #     static: yes

# Generated at 2022-06-13 09:31:22.144865
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    assert TaskInclude().build_parent_block()



# Generated at 2022-06-13 09:31:35.905286
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    class MockTaskInclude(TaskInclude):
        VALID_ARGS = frozenset(('file', 'arg1', 'arg2',))

        def __init__(self, block=None, role=None, task_include=None):
            super(MockTaskInclude, self).__init__(block=block, role=role, task_include=task_include)
            self.statically_loaded = False

    # test valid arguments
    data = dict(
        action='import_playbook',
        file='/not/a/real/file',
        arg1='value1',
        arg2='value2',
    )
    task = MockTaskInclude.load(data, loader=None)

# Generated at 2022-06-13 09:31:42.706066
# Unit test for method load of class TaskInclude
def test_TaskInclude_load():
    '''
    Test for method load of class TaskInclude
    '''
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.block import Block
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    loader = DataLoader()
    variable_manager = VariableManager()
    variable_manager.extra_vars = {'var1': 'value1'}
    inventory = InventoryManager(loader=loader, sources=['localhost'])
    variable_manager.set_inventory(inventory)

# Generated at 2022-06-13 09:31:50.603372
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    pass

# Generated at 2022-06-13 09:31:58.351960
# Unit test for method load of class TaskInclude
def test_TaskInclude_load():
    import ansible.playbook.task_include
    r = ansible.playbook.task_include.TaskInclude.load(
        {
            'action': 'include_tasks',
            'file': 'my_file_with_tasks_and_handlers.yml',
            'apply': {
                'free_form': 'my_free_form_data'
            },
        },
        variable_manager='ansible.vars.manager.VariableManager',
        loader='ansible.parsing.dataloader.DataLoader',
    )
    assert isinstance(r, ansible.playbook.task_include.TaskInclude)
    assert r.action == 'include_tasks'
    assert r.args['file'] == 'my_file_with_tasks_and_handlers.yml'


# Generated at 2022-06-13 09:32:06.948640
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    '''
    Tests build parent block creation, when ``apply`` is specified.
    '''
    apply_attrs = {}
    apply_attrs['block'] = []
    apply_attrs['name'] = None
    apply_attrs['always_run'] = False
    apply_attrs['any_errors_fatal'] = False
    apply_attrs['auto_resolve'] = None
    apply_attrs['collections'] = None
    apply_attrs['connector'] = None
    apply_attrs['delegate_to'] = None
    apply_attrs['loop'] = None
    apply_attrs['loop_control'] = None
    apply_attrs['loop_with'] = None
    apply_attrs['max_fail_percentage'] = None
    apply_attrs['notify'] = None


# Generated at 2022-06-13 09:32:14.838253
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.block import Block
    from ansible.template import Templar
    from ansible.vars.cleaner import ValueData
    import ansible.constants as C
    import ansible.playbook.role.include as role_include
    import ansible.playbook.included_file as included_file
    from units.mock.loader import DictDataLoader
    from units.mock.path import mock_unfrackpath_noop
    from units.mock.vars import mock_get_vars

# Generated at 2022-06-13 09:32:20.968068
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    class MyTaskInclude(TaskInclude):
        VALID_ARGS = TaskInclude.VALID_ARGS.union({'valid_arg'})
        OTHER_ARGS = TaskInclude.OTHER_ARGS.union({'other_arg'})

    my_data = dict(action='my_action', file='my_file', invalid_arg='invalid_value', other_arg='other_value', valid_arg='valid_value')

    task = TaskInclude(block=None, role=None, task_include=None).check_options(TaskInclude.load_data(my_data), my_data)
    assert task.action == my_data['action']
    assert 'invalid_arg' not in task.args

    task = MyTaskInclude(block=None, role=None, task_include=None).check

# Generated at 2022-06-13 09:32:29.198950
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    from ansible.playbook.play_context import PlayContext

    ti = TaskInclude()
    ti.args = dict(
        foo='bar',
    )
    ti.action = 'include'

    assert ti.get_vars() == dict(foo='bar')

    ti2 = TaskInclude()
    ti2.vars = dict(
        bar='foo',
    )
    ti2.action = 'include_role'
    ti.block = ti2
    ti2.block = ti

    assert ti2.get_vars() == dict(foo='bar', bar='foo')

    ti3 = TaskInclude()
    ti3.args = dict(
        foo='bar',
        bar='foo',
        tags='all',
    )
    ti3.action = 'import_role'

    assert ti3

# Generated at 2022-06-13 09:32:38.269858
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    from ansible.playbook.play_context import PlayContext
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager

    loader = DataLoader()
    variable_manager = VariableManager()
    variable_manager.extra_vars = {'var1': 'myvar1', 'var2': 'myvar2', 'var3': 'myvar3'}
    play_context = PlayContext()
    block = Block()

    # case 1
    data = dict()
    data['action'] = 'include_role'
    data['name'] = 'myrole'
    data['file'] = 'myrole.yml'
    ti = TaskInclude(block=block, task_include=None)

# Generated at 2022-06-13 09:32:52.490808
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    args = dict(file='/my/include/file')

    # Test that 'include' action includes args to parent vars
    task = TaskInclude()
    task.action = 'include'
    task.args = args
    assert task.get_vars() == args

    # Test that 'include_tasks' action includes args to parent vars
    task = TaskInclude()
    task.action = 'include_tasks'
    task.args = args
    assert task.get_vars() == args

    # Test that 'include_role' action does not include args to parent vars
    task = TaskInclude()
    task.action = 'include_role'
    task.args = args
    assert task.get_vars() == {}

    # Test that 'include_vars' action does not include args to parent vars

# Generated at 2022-06-13 09:33:07.144419
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    # Initialise some dummy objects
    variable_manager = None
    loader = None

    # Test with action='include', should behave like any other action
    test_data = {'action': 'include', 'test_attr': 'test_attr_value', 'test_attr2': 'test_attr2_value'}
    task = TaskInclude.load(test_data, variable_manager=variable_manager, loader=loader)
    assert task.action == 'include'
    assert task.args == {'action': 'include', 'test_attr': 'test_attr_value', 'test_attr2': 'test_attr2_value'}
    assert task.args['action'] == 'include'
    assert 'test_attr' in task.args
    assert 'test_attr2' in task.args

# Generated at 2022-06-13 09:33:14.562383
# Unit test for method load of class TaskInclude
def test_TaskInclude_load():
    '''
    Here we only test the situations in which exceptions are expected.
    For the others, we use the original tests.
    To run this test:
    1. Install Ansible and its dependencies (https://docs.ansible.com/ansible/latest/intro_installation.html)
    2. Call from the root directory of Ansible:
       python -m pytest test/units/test_playbook.py::test_TaskInclude::test_TaskInclude_load
    '''
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.vars.collection_loader import AnsibleCollectionLoader

    from ansible.utils.vars import combine_vars
    from ansible.utils.vars import merge_hash

    play_context = PlayContext

# Generated at 2022-06-13 09:33:40.479604
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    from ansible.playbook.play_context import PlayContext

    for task_action in C._ACTION_ALL_PROPER_INCLUDE_IMPORT_TASKS:
        # do not test include as it has a different implementation
        if task_action != 'include':
            task_dict = {task_action: {'src': 'some_file'}}
            parent_block = Block()
            task = TaskInclude.load(data=task_dict, block=parent_block, variable_manager=None, loader=None)

            # test valid args
            assert task.check_options(task, task_dict)
            assert task.args.get('_raw_params') == 'some_file'

            # test invalid args
            task.args['invalid'] = "somevalue"