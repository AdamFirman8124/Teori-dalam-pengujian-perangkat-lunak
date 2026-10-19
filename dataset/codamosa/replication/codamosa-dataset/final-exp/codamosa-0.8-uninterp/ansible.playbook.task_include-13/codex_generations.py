

# Generated at 2022-06-13 09:23:52.165241
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():

    from ansible.playbook.block import Block
    from ansible.playbook.play import Play
    from ansible.playbook.role import Role
    from ansible.vars.manager import VariableManager
    from ansible.vars.loader import DataLoader
    from ansible.parsing.dataloader import DataLoader as ParsingDataLoader
    from ansible.inventory.manager import InventoryManager

    def fake_task_ds(action, apply = None):
        task = dict(action = action)
        if apply:
            task['apply'] = apply
        return dict(tasks = [task])

    loader = DataLoader()
    inventory = InventoryManager(loader = loader, sources = 'localhost,')
    variable_manager = VariableManager(loader=loader, inventory=inventory)


# Generated at 2022-06-13 09:23:53.775797
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    taskInclude = TaskInclude()
    assert taskInclude.get_vars() == dict()

# Generated at 2022-06-13 09:24:04.649591
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    class Fake(object):
        def load_data(self, data, variable_manager=None, loader=None):
            return data

        def preprocess_data_safe(self, data):
            if data.get('action') in ('include', 'include_role'):
                return data
            else:
                return {}

    ti = TaskInclude()
    ti.load= ti.check_options = ti.copy = lambda a, b, c, d, e: None
    ti.action = 'include'
    ti._loader = Fake()
    ti.parent = Block()
    ti.action = 'include'
    assert ti.preprocess_data({'include': 'foo'}) == {}
    assert ti.preprocess_data({'include': 'foo', 'tags': ['test']}) == {'tags': ['test']}

   

# Generated at 2022-06-13 09:24:15.508260
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():  # noqa
    # Preparing test case variables
    include_args = {'action': 'include', 'apply': {}}
    block_attr_args = {'name': 'example_1', 'block': []}
    task_args = {'block': block_attr_args}
    # Creation of TaskInclude object:
    ti = TaskInclude()
    ti.load_data(include_args)
    ti.load_data(task_args)
    # Assert that the parent block created matches the one
    p_block = ti.build_parent_block()
    assert p_block == ti.args['apply']

# Generated at 2022-06-13 09:24:25.463305
# Unit test for method load of class TaskInclude
def test_TaskInclude_load():
    # This test case has been written keeping in mind that it may break any time
    # if the internals of method load gets changed. So it is not at all recommended
    # to use this test case for refactoring method load.
    # The potential risk here is that the test case captures the side-effect of
    # method load. I am aware of this risk.
    task = TaskInclude()

    try:
        load = task.load
    except TypeError:
        load = task.load_data


# Generated at 2022-06-13 09:24:33.486116
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    '''
    Function to test method get_vars of class TaskInclude.
    '''
    # Test with include
    ti = TaskInclude()
    ti.action = 'include'
    ti.args = {'include': '1.yml', 'a': 'b', 'c': [1, 2, 3]}
    ti.vars = {'var_1': 1, 'var_2': 'a', 'var_3': None}
    ti.tags = ['tag1', 'tag2']
    ti.when = 'some_condition'
    ti.register = 'some_var'
    ti.statically_loaded = False


# Generated at 2022-06-13 09:24:44.148995
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    from ansible.vars.manager import VariableManager
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.utils.vars import combine_vars
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText

    vm = VariableManager()
    ti = TaskInclude()

    data = {
        'action': 'include',
        'args': {
            'file': 'test.yml',
            'foo': 'bar',
        },
    }
    task = TaskInclude.load(data, variable_manager=vm, loader=None)

    assert task.action == 'include'
    assert task.args['file'] == 'test.yml'

    data['action'] = 'import_playbook'

# Generated at 2022-06-13 09:24:51.281310
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    block = Block()
    ti = TaskInclude(block=block, role=None, task_include=None)
    data = {'static': 'here'}
    new_data = ti.preprocess_data(data)
    assert new_data is data
    data = { 'ignore_errors': True }
    new_data = ti.preprocess_data(data)
    assert new_data is not data
    assert 'ignore_errors' in new_data

# Generated at 2022-06-13 09:25:02.248741
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():

    host = "localhost"

# Generated at 2022-06-13 09:25:13.589816
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    display.verbosity = 3
    task_data = {
        'include': 'include_role_test.yml',
    }
    ti1 = TaskInclude()
    assert 'include' in ti1.VALID_INCLUDE_KEYWORDS
    assert ti1.preprocess_data(task_data) == task_data
    task_data['bad_attr'] = 'foo'
    assert ti1.preprocess_data(task_data) == task_data
    task_data = {
        'include_role': 'include_role_test.yml',
    }
    assert ti1.preprocess_data(task_data) == task_data
    task_data['bad_attr'] = 'foo'

# Generated at 2022-06-13 09:25:29.935827
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    class MockRole(object):
        # http://stackoverflow.com/a/28175701/879070
        def __init__(self):
            self._role_params = 'foo'
            self._role_path = 'bar'
        def get_params(self):
            return self._role_params
        def get_role_path(self):
            return self._role_path

    task_include = TaskInclude()
    task_include._role = MockRole()
    task_include._play = 'baz'
    task_include._loader = 'qux'
    task_include._variable_manager = 'quux'

    apply_attrs = {}
    block = task_include.build_parent_block()
    assert not block.name
    assert not block.action
    assert block._parent == task_

# Generated at 2022-06-13 09:25:38.589442
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    '''
    Ensures that TaskInclude.check_options properly validates args and raises an
    AnsibleParserError when needed.

    The test is composed of the following functions, which should all be called in this order:
    * _test_TaskInclude_check_options_init_helper: initializes the test
    * _test_TaskInclude_check_options_test_helper: test the check_options method with the specified args
    * _test_TaskInclude_check_options_teardown_helper: cleanups
    '''

    # ansible.playbook.task.TaskInclude.TaskInclude() initializes the object with
    # these values

# Generated at 2022-06-13 09:25:47.182369
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    # Create a minimal parent block
    p_block = Block(task_include=None)
    p_block._role = None
    p_block._play = None
    p_block._loader = None
    p_block._variable_manager = None

    # Create a minimal include block
    task_include = TaskInclude(block=p_block)
    apply_attrs = {
        'when': '',
        'fail_when': '',
        'always_run': '',
        'register': '',
        'ignore_errors': '',
        'block': [],
    }

    # Add the apply data
    task_include.args.update(apply_attrs)

    # Check if the parent block is well created
    p_block = task_include.build_parent_block()
    assert p_block._play

# Generated at 2022-06-13 09:25:56.002353
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from io import StringIO
    from ansible.parsing.yaml.objects import AnsibleUnicode

    class Args(object):
        def __init__(self, values):
            self.tags = None
            self.skip_tags = None
            self.limit = None
            self.inventory = values['inventory']
            self.listhosts = False
            self.subset = None
            self.extra_vars = values['extra_vars']
            self.forks = 100
            self.ask_v

# Generated at 2022-06-13 09:26:05.817376
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager

    play = Play().load(dict(
        name = "Ansible Play",
        hosts = 'all',
        gather_facts = 'no',
        roles = [
            dict(
                name = 'common',
                tasks = [
                    dict(action='include', file="tasks.yaml")
                ]
            )
        ]
    ), variable_manager=TaskQueueManager(play_context=PlayContext()).get_vars_manager())

# Generated at 2022-06-13 09:26:14.886523
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook import Play
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.parsing.vault import VaultLib
    #
    import os
    import tempfile


# Generated at 2022-06-13 09:26:25.229834
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    import pytest

    ti = TaskInclude()

    data = dict(
        action = 'include_role',
        args = dict(
            name = 'testrole',
            tasks_from = 'some_file.yml',
        )
    )
    with pytest.raises(AnsibleParserError) as err:
        ti.preprocess_data(data)
    assert "'tasks_from' is not a valid attribute for a TaskInclude" in str(err)
    assert "include_role" in str(err)

    data = dict(
        action = 'import_role',
        args = dict(
            name = 'testrole',
            tasks = 'some_file.yml',
        )
    )
    with pytest.raises(AnsibleParserError) as err:
        ti.preprocess

# Generated at 2022-06-13 09:26:36.110086
# Unit test for method load of class TaskInclude
def test_TaskInclude_load():
    '''
    Most of the tests for the TaskInclude class are covered in the test_playbook.py
    test class. This unit test only covers the method load of the class.
    '''
    from ansible.playbook.play_context import PlayContext
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText


# Generated at 2022-06-13 09:26:47.988333
# Unit test for method load of class TaskInclude
def test_TaskInclude_load():
    t = TaskInclude()
    data = dict(action='include', file='foo.txt')
    t.load(data)
    assert t.args['_raw_params'] == 'foo.txt'

    data = dict(action='include', apply=dict(a='1'))
    t.load(data)
    assert t.args['apply'] == {'a': '1'}
    assert t.args['_raw_params'] is None

    data = dict(action='import_tasks', file='hello', debug='True')
    t.load(data)
    assert t.args['_raw_params'] == 'hello'
    assert 'debug' not in t.args

# Generated at 2022-06-13 09:26:59.279152
# Unit test for method load of class TaskInclude
def test_TaskInclude_load():
    TaskInclude.load({
        'include': 'something.yml',
        'something': 'value'
    })

    TaskInclude.load({
        'import_role': 'something',
        'something': 'value'
    })

    TaskInclude.load({
        'import_playbook': 'something.yml',
        'something': 'value'
    })

    # 'include' is not static, so it can have all options, so we can't check that here
    TaskInclude.load({
        'import_tasks': 'something.yml',
        'something': 'value'
    })

    TaskInclude.load({
        'apply': {'other': 'value'},
        'import_tasks': 'something.yml'
    })

# Generated at 2022-06-13 09:27:09.301819
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    kvps = {'action': 'include_role', 'file': 'foo', 'apply': Sentinel}
    ti = TaskInclude(task_include=Sentinel())
    result = ti.check_options(ti._load_data(kvps), kvps)
    assert isinstance(result, TaskInclude)
    assert result.action == 'include_role'
    assert result.args['_raw_params'] == 'foo'
    assert result.args['apply'] == Sentinel
    assert result.task_include == Sentinel()


# Generated at 2022-06-13 09:27:17.028004
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    # Statics for test_TaskInclude_preprocess_data:
    static_data = {'foo': 3,
                   'bar': 3,
                   'foobar': 3,
                   'baz': 42,
                   'buzz': 42
                   }
    static_valid_include_keywords = frozenset(['action', 'args', 'dynamic'])
    static_valid_args = frozenset(['_raw_params'])
    static_my_arg_names = frozenset(static_data.keys())
    static_bad_opts = static_my_arg_names.difference(static_valid_args)
    static_exclude_tasks = frozenset(['include'])

    # Tests follow:
    # create a TaskInclude object
    task = TaskInclude()
    # remove all keys

# Generated at 2022-06-13 09:27:26.986176
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    '''
    Test method build_parent_block of class TaskInclude.
    '''
    #
    # test without apply attr
    #
    block = dict(
        name='my_include',
        tasks=[
            dict(
                shell='echo test1',
                when='condition1',
                with_items='items1',
            ),
            dict(
                shell='echo test2',
                when='condition2',
                with_items='items2',
            )
        ],
        vars=dict(
            var1='test1',
            var2='test2',
        ),
    )
    include = TaskInclude.load(data=block, block=None, role=None, task_include=None, variable_manager=None, loader=None)
    p_block = include.build_parent_block

# Generated at 2022-06-13 09:27:38.219294
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    object = TaskInclude()
    object.args = {'file': '/tmp/ansible-list.yml', 'apply': {'block': [], 'conditional': 'xxx'}}
    object.name = 'Including into: single-list'
    object.action = 'include'
    object._role = None
    object._loader = None
    object._variable_manager = None
    object._parent = object
    apply_attrs = object.args.pop('apply', {})
    if apply_attrs:
        apply_attrs['block'] = []

# Generated at 2022-06-13 09:27:49.992752
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    class MyTask(TaskInclude):
        def __init__(self, blocks):
            super(MyTask, self).__init__()
            self._blocks = list(blocks)

        def _get_parent_attribute(self, attr, extend=False):
            pass

    my_task = MyTask([Block([Task()])])
    my_task.action = 'include'
    my_task.vars = {'a': 'my_a', 'b': 'my_b'}
    my_task.args = {'c': 'my_c', 'd': 'my_d', 'tags': 'never'}

    # no parent block, no parent task
    result = my_task.get_vars()

# Generated at 2022-06-13 09:28:00.479206
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    pb1=Playbook().load('site.yml',variable_manager='',loader='',options='',md5sum_check='off')
    task_inlcude=pb1.data[0]._entries[0]._entries[0]._entries[0]
    assert isinstance(task_inlcude,TaskInclude)
    assert task_inlcude.action == 'include'
    assert set(task_inlcude.get_vars().keys()) == {'inventory', 'playbook_dir', 'playbook_dirs', 'playbook_name'}

# Generated at 2022-06-13 09:28:12.354185
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    from ansible.playbook.task import Task
    from ansible.playbook.handler import HandlerTask
    from ansible.parsing.yaml.objects import AnsibleMapping
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager

    import pytest
    from ansible.executor.task_queue_manager import TaskQueueManager

    example = AnsibleMapping(dict(
        name='example',
        action='include',
        when='True',
        args=dict(
            _raw_params='example.yml',
            tags='tag',
        )
    ))

    ti = TaskInclude()
    ti.action = 'include_tasks'
    ti.check_options(ti.load_data(example), example)

# Generated at 2022-06-13 09:28:22.714089
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():

    from ansible.playbook.block import Block

    # Test a valid 'file' option
    data = {'action': 'include', 'file': 'foo'}
    task = TaskInclude.load(data)
    assert task.check_options(task, data) is None

    # Test an invalid option
    data['file'] = 'foo'
    data['foo'] = 'bar'
    task = TaskInclude.load(data)
    with pytest.raises(AnsibleParserError) as exc:
        task.check_options(task, data)
    assert exc.value.message == 'Invalid options for include: foo'

    # Test an invalid 'apply' option
    data = {'action': 'include', 'file': 'foo', 'apply': {'foo': 'bar'}}
    task = TaskInclude.load

# Generated at 2022-06-13 09:28:30.593990
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    import unittest
    import ansible.playbook

    class TestTaskIncludeGetVars(unittest.TestCase):

        def setUp(self):
            self.playbook = ansible.playbook.PlayBook()

        def test_get_vars_from_role(self):
            # Build the following structure
            # - play
            # -- role
            # --- include_tasks
            # ---- include_tasks
            main_task = TaskInclude(
                {'name': 'include_tasks'},
                role=self.playbook.roles[0],
                task_include=self.playbook.roles[0].tasks[0],
            )
            main_task.action = 'include_role'

# Generated at 2022-06-13 09:28:40.894261
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    import sys
    import ansible.playbook.role
    from collections import namedtuple

    mock_self = namedtuple('task', 'args action _parent vars')
    mock_self.args = dict()
    mock_self._parent = object
    mock_self.vars = dict()

    # non-include action should just return the vars
    mock_self.action = 'something'
    vars = TaskInclude.get_vars(mock_self)
    assert mock_self.vars is vars

    # include action should merge the args and vars
    mock_self.action = 'include'
    mock_self.vars = dict(x=1, y=2)
    mock_self.args = dict(a=3, b=4)
    vars = TaskInclude.get_vars

# Generated at 2022-06-13 09:28:54.900588
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    def check_vars_for_task(test_task, task_instance, expected_vars):
        '''
        Helper method to check if the task returns the expected vars
        '''
        vars_obtained = task_instance.get_vars()
        assert vars_obtained == expected_vars,\
        "Vars obtained for %s is %s, but it should be %s" % (test_task, vars_obtained, expected_vars)

    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.vars.manager import VariableManager
    from ansible.vars.hostvars import HostVars

    # Create a play-context to use in the task-includes
    play_context_instance = PlayContext()


# Generated at 2022-06-13 09:29:04.322497
# Unit test for method load of class TaskInclude
def test_TaskInclude_load():
    task = TaskInclude()
    data = {'action': 'include', 'file': 'mytask.yml'}
    task.load(data=data)
    assert(task.args.get('_raw_params') == data.get('file'))
    data = {'action': 'include_tasks', 'apply': {'environment': 'myenv'}, 'file': 'mytask.yml'}
    task.load(data=data)
    assert(task.args.get('apply') == data.get('apply'))
    data = {'action': 'import_role', 'name': 'example', 'file': 'mytask.yml'}
    task.load(data=data)
    assert(data.get('name') == 'example')

# Generated at 2022-06-13 09:29:15.267269
# Unit test for method load of class TaskInclude
def test_TaskInclude_load():
    from ansible.playbook import Play
    from ansible.playbook.play import Play as Play_obj
    from ansible.playbook.task import Task as Task_obj
    from ansible.playbook.block import Block as Block_obj
    from ansible.playbook.handler import Handler as Handler_obj

    class loader(object):
        def load_from_file(self, filename):
            return {'data': 'some_data'}

    class dummy_variable_manager(object):
        def get_vars(self, loader=None, play=None, host=None, task=None):
            return {}

        def get_host_vars(self, host):
            return {}

        def get_group_vars(self, group):
            return {}


# Generated at 2022-06-13 09:29:24.532221
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    task_include = TaskInclude()

    ds = {'action': 'include_role', 'args': {'x': "{{ lookup('file', 'a.txt') }}"}}
    assert id(task_include.preprocess_data(ds)) == id(ds)
    assert ds['action'] == 'include_role'
    assert ds['args']['x'] == "{{ lookup('file', 'a.txt') }}"

    ds = {'action': 'import_role', 'args': {'x': "{{ lookup('file', 'a.txt') }}"}}
    assert id(task_include.preprocess_data(ds)) == id(ds)
    assert ds['action'] == 'import_role'

# Generated at 2022-06-13 09:29:31.767239
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    import itertools
    from ansible.plugins.loader import fragment_loader
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.utils.vars import combine_vars

    data = {
        'action': 'include_tasks',
        'file': 'a.yml',
        'apply': 'foo_bar',
        'baz': 'some_value',
    }

    # iterate over valid and bad apply values
    # the variable manager is only needed to properly handle the 'apply' value
    variable_manager = fragment_loader.variable_manager
    variable_manager.data = variable_manager.get_vars(loader=fragment_loader, play=None)
    # compute the config variables

# Generated at 2022-06-13 09:29:36.903379
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    task = TaskInclude()
    data = {'action': 'include_role', 'file': 'role.yml'}
    task = task.check_options(task, data)
    assert task.action == 'include_role'
    assert 'file' not in task.args.keys()
    assert '_raw_params' in task.args.keys()

    data = {'action': 'include_role', 'file': 'role.yml', 'apply': {}}
    task = task.check_options(task, data)
    assert task.action == 'include_role'
    assert 'file' not in task.args.keys()
    assert '_raw_params' in task.args.keys()

    data = {'action': 'include_role', 'file': 'role.yml', 'apply': True}
    task

# Generated at 2022-06-13 09:29:43.831913
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():

    # Without apply
    # No parent task or block
    t = TaskInclude.load({
        'include': 'tests/tasks/include-vars.yaml',
    }, play=None, role=None, task_include=None)

    assert t.get_vars() == {}

    # With parent task or block
    p_block = Block()
    t = TaskInclude.load({
        'include': 'tests/tasks/include-vars.yaml',
        'vars': {'var_parent_block': True},
        'args': {'var_task_include': True}
    }, block=p_block, role=None, task_include=None)

    p_block.vars = {'var_parent_block': True}
    p_block.block = []
    assert t.get

# Generated at 2022-06-13 09:29:50.615992
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():

    class N(object):
        pass

    class TestTaskInclude(TaskInclude):

        def __init__(self):
            self._parent = None
            self.vars = dict()
            self.action = None
            self.args = dict()

    # class N represents the play
    play = N()
    play.get_vars = lambda: dict()

    # class N represents the block
    block = N()
    block.get_vars = lambda: dict(block_vars=True)

    # class N represents the role
    role = N()
    role.get_vars = lambda: dict(role_vars=True)

    # create the test instance
    task_include = TestTaskInclude()
    task_include._play = play
    task_include._parent = block
    task_include._role

# Generated at 2022-06-13 09:30:00.031256
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    class FakeRole:
        def __init__(self):
            self._role_path = '.'

    class FakePlay:
        def __init__(self):
            self._ds = []

    class FakeVariableManager:
        def __init__(self):
            self._fact_cache = {}
            self._vars_cache = {}

    class FakeLoader:
        def __init__(self):
            self._basedir = '.'

    class FakeHost:
        def __init__(self):
            self.get_name.return_value = '127.0.0.1'

    task_incl_non_static = TaskInclude()
    task_incl_non_static._parent = Block(play=FakePlay(), task_include=None, role=FakeRole())
    task_incl_non_static._variable

# Generated at 2022-06-13 09:30:08.258118
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    import pytest
    from .test_playbook_objects import TestPlaybookObjects
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    variable_manager = TestPlaybookObjects.MyVarsManager()
    task_include = TaskInclude.load({'action': 'include', 'file': 'test.yml'}, variable_manager=variable_manager, loader=loader)

    # Test invalid attributes
    data = {'action': 'include', 'file': 'test.yml', 'test_attr': ''}
    with pytest.raises(AnsibleParserError):
        task_include.preprocess_data(data)
    data['test_attr'] = None

# Generated at 2022-06-13 09:30:30.663810
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    from ansible.playbook.block import Block
    from ansible.utils.listify import listify_lookup_plugin_terms

    block = Block()
    block.vars = {"a": "b"}
    task = TaskInclude(block = block)
    task.action = "include"
    task.args = {"x": "y", "_raw_params": "z"}
    assert task.get_vars() == {"a": "b", "x": "y", "_raw_params": "z"}

    block = Block()
    block.vars = {"a": "b"}
    task = TaskInclude(block = block)
    task.action = "include_tasks"
    task.args = {"x": "y", "_raw_params": "z"}

# Generated at 2022-06-13 09:30:41.846129
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.plugins.loader import action_loader
    from ansible.playbook.block import Block
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.role import Role
    from ansible.vars.manager import VariableManager

    # Load fake play and play context
    p_block = PlayContext()
    p_block._play = Play().load({
        'name': 'test play',
        'hosts': 'localhost',
        'connection': 'local',
        'gather_facts': 'no',
        'roles': [{'role': 'fake_role'}]
    }, variable_manager=VariableManager(), loader=action_loader)

    # Load fake_

# Generated at 2022-06-13 09:30:49.663080
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    from ansible.playbook.play import Play
    from ansible.playbook.task import (Task, HandlerTask, TaskInclude)
    from ansible.playbook.block import Block
    from units.mock.loader import DictDataLoader
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

# Generated at 2022-06-13 09:30:56.077016
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    # prepare the data for the test
    data = dict(
        tags=['include_task_apply'],
        include='tests/include_task_apply.yml',
        apply=dict(
            block=dict(
                name='parent task block'
            )
        )
    )
    # load the data with TaskInclude.load
    ti = TaskInclude.load(data)
    # call the tested method
    p_block = ti.build_parent_block()
    # verify the results
    assert p_block.name == 'parent task block'

# Generated at 2022-06-13 09:31:06.528907
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    def return_local_vars(task):
        return task.get_local_vars()

    task = TaskInclude()
    task.action = 'export'
    task.vars = {'var1': 'value1', 'var2': 'value2'}
    task.args = {'var3': 'value3', 'var4': 'value4'}
    task._parent = Task()
    task._parent.get_vars = return_local_vars
    task._parent.get_local_vars = return_local_vars
    task._parent.vars = {'parent_var1': 'parent_value1', 'parent_var2': 'parent_value2'}

# Generated at 2022-06-13 09:31:16.988660
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    class MockBlock(object):
        def __getitem__(self, key):
            return self

        def __hasattr__(self, name):
            return self.__getattribute__(name)

    mock = MockBlock()
    task = TaskInclude(block=mock)
    task.args = {}
    task.args['apply'] = {"block": []}

    class MockBlock2(Block):
        def __init__(self, parent=None, play=None):
            self._parent = parent
            self._play = play

        def _load_vars(self, ds):
            self.vars = ds

        def _load_role_vars(self, ds):
            self._role_vars = ds

    block = MockBlock2(parent=mock, play=mock)
    task

# Generated at 2022-06-13 09:31:25.555932
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play

    play_context = PlayContext()
    play = Play().load({}, variable_manager={}, loader=None)

    task = TaskInclude.load({'file': 'foo'}, block=play, variable_manager={}, loader=None)
    play.block = [task]
    play_context.set_play(play)

    assert {'file': 'foo'} == task.get_vars()

# Generated at 2022-06-13 09:31:37.839462
# Unit test for method load of class TaskInclude
def test_TaskInclude_load():
    import io
    from ansible.parsing.yaml.objects import AnsibleUnicode, AnsibleSequence
    from ansible.template import Templar
    from ansible.playbook.play import Play
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    ds = AnsibleUnicode(u"- name: mytask\n  shell: /bin/foo\n  tags: [ 'always' ]\n  when: false\n")
    ds = AnsibleSequence([ds])
    play_source = dict(
        name = "Ansible Play",
        hosts = 'all',
        gather_facts = 'no',
        tasks = ds
    )


# Generated at 2022-06-13 09:31:48.304930
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    from ansible.playbook.play_context import PlayContext

    data = dict(
        import_playbook='bar.yml',
        include_tasks='foo.yml',
        include_vars='bar.yml',
    )

    ti = TaskInclude()
    with PlayContext(ti):
        for action, d in data.items():
            ti.action = action
            assert ti.preprocess_data(dict(import_playbook=d, random_junk='foo')) == dict(action=action, import_file='bar.yml', _raw_params=d)
            assert ti.preprocess_data(dict(import_playbook=d, args='foo=bar')) == dict(action=action, import_file='bar.yml', _raw_params=d, args='foo=bar')


# Generated at 2022-06-13 09:31:56.968412
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    # Test get_vars() when action is import_playbook
    task = TaskInclude(block=None, role=None, task_include=None)
    task.action = 'import_playbook'
    task.vars = dict()
    task.args = dict(a=1, b=2, c=3)
    task._parent = None
    assert isinstance(task.get_vars(), dict)
    assert task.get_vars() == dict()

    # Test get_vars() when action is include
    task = TaskInclude(block=None, role=None, task_include=None)
    task.action = 'include'
    task.vars = dict()
    task.args = dict(a=1, b=2, c=3)
    task._parent = None

# Generated at 2022-06-13 09:32:46.548700
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = Inventory(loader=loader, variable_manager=variable_manager)

    def test_action(action, data, expected_error=False):
        task = TaskInclude.load({'include': data}, variable_manager=variable_manager, loader=loader)
        task.action = action
        if expected_error:
            with pytest.raises(AnsibleParserError):
                TaskInclude.check_options(task, data)
        else:
            TaskInclude.check_options(task, data)


# Generated at 2022-06-13 09:32:52.576065
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():

    class DummyTaskInclude(TaskInclude):
        _apply = FieldAttribute(isa='dict', allow_include=True)

    # test static
    static_ti = DummyTaskInclude()
    static_ti.vars = {'foo': 'bar'}
    static_ti.args = {'foo': 'bar'}
    static_ti.action = 'include'
    assert static_ti.get_vars() == {'foo': 'bar'}

    # test dynamic
    dynamic_ti = DummyTaskInclude()
    dynamic_ti.vars = {'foo': 'bar'}
    dynamic_ti.args = {'foo': 'bar'}
    dynamic_ti.action = 'include_role'
    assert dynamic_ti.get_vars() == {'foo': 'bar'}

    #

# Generated at 2022-06-13 09:33:01.905430
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():

    # build a dummy self object that has the required attributes
    self = TaskInclude()
    self.args = {'apply': {'fake':'attributes'}}
    self._parent = lambda: None
    self._parent._play = lambda: None
    self._role = lambda: None
    self._variable_manager = lambda: None
    self._loader = lambda: None

    p_block = self.build_parent_block()
    assert type(p_block) is Block

# Generated at 2022-06-13 09:33:12.257221
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    block = Block()
    block.vars = {'foo': 'bar', 'baz': 'xyzzy'}
    block.parent_vars = {'foo': 'bar', 'baz': 'xyzzy'}

    for action in C._ACTION_INCLUDE:
        task = TaskInclude()
        task.args = {'_raw_params': 'include1.yml', 'foo': 'bax'}
        task.vars = {'foo': 'bax'}
        task.action = action
        # Implicit parent block
        task.set_loader(MockLoader({}))
        task.post_validate(MockDataLoader())
        assert task.get_vars() == {'foo': 'bax'}
        # Explicit parent block
        task._parent = block

# Generated at 2022-06-13 09:33:23.124885
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    task_include_task = TaskInclude()

    data = {
        "include": "foo",
        "_raw_params": "foo"
    }

    res = task_include_task.check_options(task_include_task.load_data(data), data)
    assert '_raw_params' in res.args
    assert 'file' not in res.args

    data = {
        "include": "foo",
        "_raw_params": "foo",
        "apply": {
            "attribute": "test"
        }
    }

    try:
        res = task_include_task.check_options(task_include_task.load_data(data), data)
    except AnsibleParserError:
        pass


# Generated at 2022-06-13 09:33:32.530458
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():

    """
        We test the method get_vars of class TaskInclude
    """

    from ansible.playbook.play import Play
    from ansible.inventory import Host, Inventory
    from ansible.vars import VariableManager

    block_vm = VariableManager()
    block_vm.extra_vars = dict()
    block_vm.extra_vars['block_var'] = 'block_var'
    block_vm.extra_vars['file_var'] = 'file_var'
    block_vm.extra_vars['_raw_params'] = '_raw_params'
    all_vars = dict()
    all_vars['block_var'] = 'block_var'
    all_vars['file_var'] = 'file_var'

# Generated at 2022-06-13 09:33:42.714070
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    # Test default options
    task = TaskInclude(block=None, role=None, task_include=None)
    task = task.check_options(task.load_data({}, variable_manager=None, loader=None), "")

    # Test no file specified
    with pytest.raises(AnsibleParserError) as exc:
        task = task.check_options(task.load_data({"no_file_specified": "helloworld"}, variable_manager=None, loader=None), "")
    assert exc.value.args[0] == 'No file specified for include'

    # Test invalid option
    task = TaskInclude(block=None, role=None, task_include=None)