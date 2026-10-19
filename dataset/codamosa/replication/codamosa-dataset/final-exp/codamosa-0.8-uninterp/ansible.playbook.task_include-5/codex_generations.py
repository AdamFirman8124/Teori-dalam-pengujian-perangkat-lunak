

# Generated at 2022-06-13 09:23:41.285160
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    t = TaskInclude()

# Generated at 2022-06-13 09:23:55.454238
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    import ansible.playbook as playbook
    import ansible.playbook.play_context as play_context

    ti = TaskInclude()
    ti._variable_manager = playbook.VariableManager()

# Generated at 2022-06-13 09:24:05.693042
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    ti = TaskInclude()
    assert ti.VALID_ARGS == frozenset(('file', '_raw_params', 'apply',))

    # check bad opts
    task1 = TaskInclude.load({'action': 'include', 'foo': 'bar'})
    try:
        ti.check_options(task1, task1)
        assert False, 'Invalid options for include should be raised'
    except AnsibleParserError as e:
        assert e.message == 'Invalid options for include: foo'
        assert e.obj == {'action': 'include', 'foo': 'bar'}

    task2 = TaskInclude.load({'action': 'import_tasks', 'foo': 'bar'})

# Generated at 2022-06-13 09:24:14.664349
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    ds1 = {'action': 'include', 'tags': ['foo'], 'blah': 'blah'}
    ds2 = {'action': 'import_playbook', 'tags': ['foo'], 'blah': 'blah'}
    task1 = TaskInclude(block=None, role=None, task_include=None)
    task2 = TaskInclude(block=None, role=None, task_include=None)
    new_ds1 = task1.preprocess_data(ds1)
    new_ds2 = task2.preprocess_data(ds2)
    expected_ds1 = {'action': 'include', 'tags': ['foo'], 'blah': 'blah'}
    expected_ds2 = {'action': 'import_playbook', 'tags': ['foo']}

# Generated at 2022-06-13 09:24:19.412697
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    '''
    This method is used to test the TaskInclude class
    '''

    test_TaskInclude = TaskInclude()
    args = dict()
    args['a'] = '1'
    args['b'] = '2'

    def mock_get_vars():
        return dict(x='1')

    test_TaskInclude.args = args
    test_TaskInclude._parent = MockTask
    test_TaskInclude.vars = dict(c='1', d='2')
    test_TaskInclude._parent.get_vars = mock_get_vars

    expected_result = dict(c='1', d='2', x='1', a='1', b='2')
    actual_result = test_TaskInclude.get_vars()

    assert actual_result == expected_result




# Generated at 2022-06-13 09:24:29.457635
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    task = TaskInclude()

    bad_actions = ['include_tasks', 'include_role', 'import_tasks', 'import_role']
    bad_actions_data = {'bad_action': 'bad_value'}
    for action in bad_actions:
        data = dict(bad_actions_data, action=action)
        try:
            task.check_options(task, data)
            assert False, "Invalid options for %s: check_options did not raise an error" % action
        except AnsibleParserError:
            pass

    bad_apply = dict(apply=['bad_value'])
    data = dict(bad_apply, action='include_role')

# Generated at 2022-06-13 09:24:39.175081
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    path_to_dummy_file = "./test/units/utils/ansible_module_fake.py"
    ti = TaskInclude()
    ti_copy = ti.copy()  # Needed for testing

    # test var_args
    task = TaskInclude.load({'action': 'include_tasks', 'file': path_to_dummy_file})
    test_data = {'action': 'include_tasks', 'vars': {'foo': 'bar'}}
    task_copy = task.copy()  # Needed so that we don't modify the actual data
    ti.check_options(task_copy, test_data)
    assert '_raw_params' in task_copy.args
    assert task_copy.args.get('_raw_params') == path_to_dummy_file

# Generated at 2022-06-13 09:24:50.497698
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    # Test that check_options raises when encountering bad_opts
    data = {"action": "meta: random", "this_is_bad": 123}
    ti = TaskInclude()
    try:
        ti.check_options(
            ti.load_data(data, variable_manager=None, loader=None),
            data
        )
    except AnsibleParserError as e:
        assert "Invalid options for meta: random: this_is_bad" in str(e)
        assert "this_is_bad: 123" in str(e)

    # Now validate that apply_attrs are validated
    data = {"action": "include_tasks", "file": "foo.yml", "apply": [1,2,3]}

# Generated at 2022-06-13 09:25:01.487593
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    ds_module = dict(
        action='include_role',
        name='ami-roles.ami-role'
    )
    ds_include = dict(
        action='include',
        file='file1',
        tags='tag1'
    )
    ds_tasks = dict(data=[ds_module, ds_include])

    module = TaskInclude.load(ds_module, block=None)
    include = TaskInclude.load(ds_include, block=None)
    tasks = Block.load(ds_tasks, block=None)

    assert module.args.keys() == {'action', 'name'}
    assert ds_module['action'] == module.action
    assert ds_module['name'] == module.args['name']


# Generated at 2022-06-13 09:25:07.177468
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    import os, sys, tempfile
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible import context

    class MockPlay(Play):
        '''
        Mock of the Play class to allow the use of a private method
        '''
        def __init__(self, *args, **kwargs):
            super(MockPlay, self).__init__(*args, **kwargs)

        def _load_included_file(self, *args, **kwargs):
            # Override the load_included_file method to remove the cache
            pass

    # Setup context

# Generated at 2022-06-13 09:25:21.948284
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    import unittest

    class TestTaskInclude(unittest.TestCase):

        class MyTaskInclude(TaskInclude):

            def _validate_action(self, attr, value, var_name, display_name):
                return value

            def _validate_loop(self, attr, value, var_name, display_name):
                return value

            def _validate_loop_control(self, attr, value, var_name, display_name, play=None):
                return value

            def _validate_loop_with(self, attr, value, var_name, display_name):
                return value

            def _validate_args(self, attr, value, var_name, display_name):
                return value


# Generated at 2022-06-13 09:25:33.142481
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    import copy
    import yaml
    yaml_str1 = """
    - hosts: localhost
      gather_facts: no
      tasks:
        - name: include with apply
          include: tasks/main.yml apply:
            block:
              - debug:
                  msg: '{{ ansible_version }}'
                tags:
                  - always
                  - debug
          tags: []
          when: False
        - debug:
            msg: '{{ ansible_version }}'
          tags:
            - always
            - debug
    """
    playbook_data1 = yaml.safe_load(yaml_str1)

    # Method build_parent_block of class TaskInclude
    # should not change the structure of the data

# Generated at 2022-06-13 09:25:45.979756
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():

    t = TaskInclude(block=None, role=None, task_include=None)
    t.action = 'include'
    test_dict = dict(task_include_2={'name': 'hello'},
                     task_include_1={'name': 'world'},
                     task_include_3={'name': 'foo'})
    result_dict = dict(task_include_1={'name': 'world'},
                       task_include_2={'name': 'hello'},
                       task_include_3={'name': 'foo'})
    for name, items in test_dict.items():
        t.action = 'include'
        t.vars = {}
        t.args = items.copy()
        assert t.get_vars() == result_dict[name]

# Generated at 2022-06-13 09:25:50.062231
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    '''
        This method is used to test the get_vars method of the module.
    '''
    from ansible.playbook import Play
    from ansible.playbook.base import Base
    from ansible.playbook.block import Block
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    from ansible.vars.manager import VariableManager

    base_obj = Base()

# Generated at 2022-06-13 09:25:57.675502
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    from ansible.playbook.block import Block
    from ansible.playbook.play import Play
    from ansible.playbook.role.include import RoleInclude
    from ansible.vars.manager import VariableManager

    from ansible.module_utils._text import to_text

    ti = TaskInclude(block=Block(), role=RoleInclude(play=Play()))
    ti._variable_manager = VariableManager()

    apply_attrs = {
        'when': 'when',
        'loop': 'loop',
        'loop_with': 'loop_with',
        'name': 'name',
        'rescue': [],
        'always': [],
    }

    p_block = ti.build_parent_block()
    assert p_block == ti

    ti.args['apply'] = apply_attrs



# Generated at 2022-06-13 09:26:09.128097
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.task import Task
    my_ti = TaskInclude()

    # with 'include'
    my_task = Task()
    my_task.action = 'include'
    my_task.args = {'file': 'file_1', 'bad': 'opt', 'debugger': False}
    my_task = my_ti.check_options(my_task, {})
    assert my_task.action == 'include'
    assert my_task.args == {'file': 'file_1', '_raw_params': 'file_1'}

    # with 'include_role'
    my_task = Task()
    my_task.action = 'include_role'

# Generated at 2022-06-13 09:26:17.031852
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    '''
    TaskInclude: build_parent_block
    '''
    t = TaskInclude()
    t._parent = {'_variable_manager': 'foo',
                 '_loader': 'bar'}
    t.args = {'apply': {'name': 'baz'}}
    res = t.build_parent_block()
    assert '_play' in res
    assert '_role' in res
    assert 'block' in res
    assert '_parent' in res
    assert res['_variable_manager'] == 'foo'
    assert res['_loader'] == 'bar'
    assert res['block'] == []
    assert res['_role'] == t._role
    assert res['name'] == 'baz'

    t = TaskInclude()

# Generated at 2022-06-13 09:26:26.491952
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    from ansible.playbook.block import Block
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    from ansible.playbook.role_include import IncludeRole

    fake_play = Play().load({}, variable_manager=None, loader=None)
    fake_play._role = IncludeRole()
    fake_task = Task()
    fake_task._play = fake_play
    tc = TaskInclude()
    tc._parent = fake_task
    tc.args = {'apply': {'loop': '{{ test_var }}'}}

    p_block = tc.build_parent_block()
    assert isinstance(p_block, Block)


# Generated at 2022-06-13 09:26:36.957543
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    # Test for action which does not use 'apply'
    for action in C._ACTION_ALL_PROPER_INCLUDE_IMPORT_TASKS.difference(C._ACTION_INCLUDE_TASKS):
        task = TaskInclude()
        # Test without any option
        task.action = action
        task.args = {}
        res_task = task.check_options(task, dict(action=action, args={}))
        assert res_task.args == dict(_raw_params=None)
        # Test with option and option which is not 'file'
        task.args = dict(apply=dict(name='test_block_name'))

# Generated at 2022-06-13 09:26:50.876497
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    ti = TaskInclude(block=None, role=None, task_include=None)
    ti.args = {'apply': {'block': []}}
    ti._parent = 'parent'
    ti._play = 'play'
    ti._loader = 'loader'
    ti._variable_manager = 'variable_manager'
    ti._role = 'role'
    # Testing that the build_parent_block properly creates a Block object
    assert isinstance(ti.build_parent_block(), Block)


# This import is here because fields copy the instance's class in setup (top level),
# thus we need to import related classes before the fields.
from ansible.playbook.role.include import TaskInclude as RoleTaskInclude


# Generated at 2022-06-13 09:27:05.530074
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    from ansible.playbook.play_context import PlayContext

    data = {
        'include': 'test.yml',
    }

    task = TaskInclude.load(data, block=None, role=None, task_include=None, variable_manager=None, loader=None)

    assert task.action == 'include'
    assert task.args['_raw_params'] == 'test.yml'

    data = {
        'include_tasks': 'test.yml',
        'apply': 'test.yml',
    }

    with pytest.raises(AnsibleParserError):
        task = TaskInclude.load(data, block=None, role=None, task_include=None, variable_manager=None, loader=None)


# Generated at 2022-06-13 09:27:14.296522
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText

    # Create a TaskInclude object for testing
    ti = TaskInclude()
    ti._parent = Sentinel
    ti.task_include = Sentinel
    ti._role = Sentinel
    ti._block = Sentinel
    ti._play = Sentinel
    ti._loader = Sentinel
    ti._variable_manager = Sentinel
    ti.parent = Sentinel
    ti.context = PlayContext()

    # Sentinel
    sentinel = Sentinel()

    # Create a dict with all valid keywords for include tasks
    dict_data = dict()
    for k in TaskInclude.VALID_INCLUDE_KEYWORDS:
        dict_data[k] = sentinel

    # Verify that all keywords in dict_data are returned as

# Generated at 2022-06-13 09:27:24.713197
# Unit test for method load of class TaskInclude
def test_TaskInclude_load():
    from ansible.playbook.play import Play
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    inv_data = InventoryManager(loader=loader, sources=['localhost,'])
    play_source = dict(
        name = "Ansible Play",
        hosts = 'webservers',
        gather_facts = 'no',
        tasks = [
            dict(action=dict(module='shell', args='ls'), register='shell_out'),
            dict(action=dict(module='debug', args=dict(msg='{{shell_out.stdout}}')))
        ]
    )
    play = Play().load(play_source, variable_manager=None, loader=loader)

# Generated at 2022-06-13 09:27:38.924004
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    from ansible.parsing.dataloader import DataLoader

# Generated at 2022-06-13 09:27:50.673080
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.module_utils.common.collections import is_sequence

    # no result
    assert TaskInclude.preprocess_data({'foo':'bar'}) == {}

    # test all possible valid options
    d = {
        'file': 'foobar',
        'apply': {'a': 1, 'b': 2}
    }
    assert TaskInclude.preprocess_data(dict(d, action='include')) == d
    assert TaskInclude.preprocess_data(dict(d, action='include_role')) == d

    # test invalid options

# Generated at 2022-06-13 09:28:03.789935
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    ds1 = dict(action="include_role", name="role_to_include")
    assert TaskInclude.preprocess_data(ds1) == ds1

    ds2 = dict(action="include_role", name="role_to_include", ignore_errors=True)
    assert TaskInclude.preprocess_data(ds2) == ds2

    ds3 = dict(action="include", file="path/to/file")
    assert TaskInclude.preprocess_data(ds3) == ds3

    ds4 = dict(action="include", file="path/to/file", when="some condition")
    assert TaskInclude.preprocess_data(ds4) == ds4

    ds5 = dict(action="include", file="path/to/file", ignore_errors=True)

# Generated at 2022-06-13 09:28:14.976471
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    import ansible.playbook.role.include as role_include
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    # valid option
    task = TaskInclude()
    data = dict(
        action='include',
        file='foo.yml',
    )
    task.check_options(task.load_data(data), data)

    # valid option
    task = TaskInclude()
    data = dict(
        action='include_role',
        _raw_params='role_name',
    )
    task.check_options(task.load_data(data), data)

    # valid option
    task = TaskInclude()
    data

# Generated at 2022-06-13 09:28:25.404854
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    from ansible.playbook.play_context import PlayContext

    test_apply_attrs = {'block': [], 'always': [], 'rescue': [], 'when': 'always', 'ignore_errors': False, 'register': 'ansible_module_result', 'delegate_to': '127.0.0.1', 'delegate_facts': True}

    # Test with apply_attrs is not empty
    test_task = TaskInclude()
    test_task.args = {'apply': test_apply_attrs}
    result = test_task.build_parent_block()
    assert isinstance(result, Block)
    assert result._parent is test_task
    assert result._play is PlayContext()
    assert result._task_include is test_task
    assert result._role is None

# Generated at 2022-06-13 09:28:30.564822
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    '''
    Test for check_options method of class TaskInclude
    '''

    display.verbosity = 3

    # test for invalid option 'unknown'
    data = {'action': 'include_tasks', 'unknown': {'key': 'value'}}
    ti = TaskInclude()
    task = ti.check_options(
        ti.load_data(data),
        data
    )

    assert len(task._load_errors) == 1
    assert 'is not a valid attribute' in task._load_errors[0]



# Generated at 2022-06-13 09:28:40.853136
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    '''
    Test that TaskInclude's build_parent_block() method creates a Block object
    with the same attributes as the ones passed in 'args.apply'
    '''
    task_include = TaskInclude()
    task_include.args = {
        'apply': {
            'name': 'Apply test',
            'tags': 'test'
        }
    }
    expected_p_block = Block()
    expected_p_block.name = 'Apply test'
    expected_p_block.tags = 'test'
    assert task_include.build_parent_block() == expected_p_block

    task_include = TaskInclude()
    task_include.args = {
        'apply': {
            'name': 'Apply test 2',
        }
    }
    expected_p_block = Block()
   

# Generated at 2022-06-13 09:29:00.885865
# Unit test for method load of class TaskInclude
def test_TaskInclude_load():
    '''
    This test method is used to test the load method of class TaskInclude
    '''
    # Invoke load method with invalid 'file' value
    task_include = TaskInclude()
    data = {'action': 'include', 'file': ''}
    try:
        task_include.load(data)
        assert False
    except AnsibleParserError:
        pass

    # Invoke load method with invalid option
    task_include = TaskInclude()
    data = {'action': 'include', 'file': 'test.yml', 'invalid_option': 'test_value'}
    try:
        task_include.load(data)
        assert False
    except AnsibleParserError:
        pass

    # Invoke load method with invalid option
    task_include = TaskInclude()

# Generated at 2022-06-13 09:29:15.339202
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    class FakeParentBlock(object):
        def __init__(self, vars_dict):
            self.vars = vars_dict

        def get_vars(self):
            return self.vars

    class FakeBlock(object):
        def __init__(self, vars_dict):
            self.vars = vars_dict

        def get_vars(self):
            return self.vars

    class FakeRole(object):
        def __init__(self, vars_dict):
            self.vars = vars_dict

        def get_vars(self):
            return self.vars

    class FakePlay(object):
        @staticmethod
        def get_vars():
            return dict()


# Generated at 2022-06-13 09:29:23.998840
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    from ansible.playbook.play import Play

    task_include = TaskInclude()
    task_include.role = None
    task_include._parent = Play()

    # Check when no apply options exist
    assert task_include.build_parent_block() is task_include

    # Check when apply options exist
    task_include.args['apply'] = { 'ignore_errors': False, 'loop_control': False }
    parent_block = task_include.build_parent_block()
    assert isinstance(parent_block, Block)
    assert task_include in parent_block._block
    assert task_include._parent == parent_block._parent
    assert parent_block.ignore_errors is False
    assert parent_block.loop_control is False

# Generated at 2022-06-13 09:29:37.986486
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    task = TaskInclude(
        block=Block(
            Block(
                task_include=TaskInclude(
                    block=Block()
                )
            ),
            play=None,
        ),
    )

    expected = {}
    actual = task.get_vars()
    assert expected == actual

    task.action = 'include'
    task.vars = {'var_foo': 'foo', 'var_bar': 'bar'}
    task.args = {'_raw_params': 'params', 'arg_foo': 'foo', 'arg_bar': 'bar'}
    expected = {
        'arg_foo': 'foo',
        'arg_bar': 'bar',
        'var_foo': 'foo',
        'var_bar': 'bar',
    }
    actual = task.get_vars()

# Generated at 2022-06-13 09:29:43.729550
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    block1 = dict(
        block=dict(
            name="foobar",
            rescue=["tasks3", "tasks4"],
            always=["tasks5"],
        )
    )

    def _assert(**kwargs):
        task = TaskInclude(**kwargs)

        # No apply attributes
        result = task.build_parent_block()
        assert result == task

        # With apply attributes
        task.args.update(apply=block1['block'])
        result = task.build_parent_block()
        assert result is not task
        assert "block" in result.vars
        assert result.vars['block'] == []


# Generated at 2022-06-13 09:29:50.568815
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    # Note that this test has to be run directly and not through pytest otherwise
    # the module AnsibleParserError will not be known resulting in a
    # NameError: name 'AnsibleParserError' is not defined
    from ansible.playbook import Playbook
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins.loader import load_plugin_manager
    from ansible.template import Templar
    from ansible.utils.vars import combine_vars
    # We need to load the plugin manager to be able to load the ansible lookup
    # plugin
    load_plugin_manager()
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    # We need to create a context to be able to create the task include

# Generated at 2022-06-13 09:29:55.819509
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    vars = dict(x=10, y=20)
    args = dict(a=1, b=2)
    block, parent_block = None, None
    ti = TaskInclude(block=block, task_include=parent_block)
    ti.action = 'include'
    ti.vars = vars
    ti.args = args
    assert vars == ti.get_vars()



# Generated at 2022-06-13 09:30:03.696378
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    from ansible.playbook.play_context import PlayContext
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.template import Templar

    class TestObject(AnsibleBaseYAMLObject):
        yaml_loader = None
        yaml_dumper = None
        _parent = None

    class TestLoader(BaseLoader):

        def __init__(self):
            self._basedir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
            self.variables = {}
            self.checked = []

        def get_basedir(self, host=None):
            return self

# Generated at 2022-06-13 09:30:08.922651
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    task = TaskInclude()
    task.vars = {
        'a': 1,
        'b': 2
    }
    task.args = {
        'c': 3,
        'd': 4,
    }
    task.action = 'include'
    task._parent = Task()
    task._parent.vars = {
        'e': 5,
        'f': 6
    }
    assert task.get_vars() == {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4
    }

# Generated at 2022-06-13 09:30:10.208340
# Unit test for method load of class TaskInclude
def test_TaskInclude_load():
    raise Exception('Not Implemented')


# Generated at 2022-06-13 09:30:40.551725
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    '''
    The method get_vars() of class TaskInclude is a wrapper
    around the get_vars() method of a Task.
    The method get_vars() of a Task returns a dictionary
    containing all the variables available to that task.
    If the dictionary returned by get_vars() of a Task
    contains the variables 'tags' and/or 'when', the
    TaskInclude.get_vars() method deletes these variables
    from the dictionary.
    '''

    global display
    display = Display()
    display.display = lambda x, y, z: None

    ti = TaskInclude()

    class MockParent():
        def __init__(self, parent_vars=None):
            self._vars = parent_vars

        def get_vars(self):
            return self._vars



# Generated at 2022-06-13 09:30:48.089971
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    token = dict(action='include', name='everything')
    ti = TaskInclude.load(token)
    assert ti.get_vars() == {}

    token = dict(action='include_role', name='everything')
    ti = TaskInclude.load(token)
    assert ti.get_vars() == {}

    token = dict(action='include_tasks', name='everything')
    ti = TaskInclude.load(token)
    assert ti.get_vars() == {}

    token = dict(action='include', name='everything', two=2)
    ti = TaskInclude.load(token)
    assert ti.get_vars() == {'two': 2}

# Generated at 2022-06-13 09:30:56.750017
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    main_arg_names = frozenset(('file', '_raw_params'))
    task_block = Block(play=None, role=None)
    task = TaskInclude(block=task_block, role=None)

    data = {'include': 'file', 'action': 'include'}
    task = task.check_options(task.load_data(data, variable_manager=None, loader=None), data)
    assert task.args.keys() == main_arg_names

    data = {'include': 'file', 'action': 'include'}
    for attr in TaskInclude.VALID_INCLUDE_KEYWORDS.difference(TaskInclude.VALID_ARGS):
        data[attr] = 'foo'

# Generated at 2022-06-13 09:31:06.810116
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    from ansible.playbook.handler import HandlerTaskInclude
    task_data = dict(action='include_tasks')
    # Test for an empty dict for task data
    ti = TaskInclude()
    task = ti.check_options(TaskInclude.load(task_data), task_data)

    assert task.args == dict(_raw_params=None)

    # Test for a dict with file specified by relative path
    task_data['file'] = 'test.yml'
    ti = TaskInclude()
    task = ti.check_options(TaskInclude.load(task_data), task_data)

    assert task.args == dict(_raw_params='test.yml')

    # Test for a dict with file specified by absolute path
    task_data['file'] = '/path/to/test.yml'
   

# Generated at 2022-06-13 09:31:17.166411
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    from ansible.playbook.block import Block
    from ansible.playbook.play import Play

    play_datastructure = {'hosts': 'all', 'roles': [{'name': 'testrole'}], 'tasks': [{'include_tasks': {'file': 'test.yaml'}, 'name': 'test task'}]}
    play = Play().load(play_datastructure, variable_manager=None, loader=None)
    include_task = play.get_blocks()[0].block[0]
    assert include_task.get_vars() == {}

    # The below test is to check if the include action is not in C._ACTION_INCLUDE as it should not return the vars
    # from the args as part of get_vars()

# Generated at 2022-06-13 09:31:32.292961
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play

    dummy_loader = DataLoader()
    dummy_inventory = None
    dummy_variable_manager = VariableManager(loader=dummy_loader, inventory=dummy_inventory)
    dummy_play = Play()
    dummy_play_context = PlayContext(variable_manager=dummy_variable_manager)

    ti = TaskInclude()
    ti.vars = dict(cats='dogs')
    ti.args = dict(file='file')
    ti.action = 'include'
    ti._parent = dummy_play
    ti._role = None
    ti

# Generated at 2022-06-13 09:31:36.770810
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    mock_task = TaskInclude()
    mock_task.vars = dict(a=1, b=2)
    mock_task.args = dict(c=3, d=4)

    assert mock_task.get_vars() == dict(a=1, b=2, c=3, d=4)

# Generated at 2022-06-13 09:31:43.264899
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    '''
    make sure var inheritance work
    '''
    # make a small Play to represent the include
    class Play(object):
        vars = dict(
            aa='aa_play',
            bb='bb_play'
        )

        def get_variable_manager(self):
            class Vars:
                _fact_cache = {}
                _hostvars = {}
                _extra_vars = dict(
                    aa='aa_extra_vars',
                    cc='cc_extra_vars'
                )

            return Vars

    # make a small Block to represent the include
    class Block(object):
        def __init__(self, vars):
            self.vars = vars

    # make a role
    class Role:
        def __init__(self, vars):
            self

# Generated at 2022-06-13 09:31:49.943581
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    class TestFieldAttribute(FieldAttribute):
        def __init__(self, field_name, name):
            self._parent = None
            self._play = None
            self.blocks = None
            self.action = 'include'
            self.name = name
            self.task_include = Sentinel()
            self.args = {}
            self.vars = {}

        def __repr__(self):
            return self.name

    task = TestFieldAttribute('field_name', 'name')

    assert task.get_vars() == {'name': 'name'}

# Generated at 2022-06-13 09:31:57.876004
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    task_vars = {"x": "1"}
    loader = None
    variable_manager = None
    section_data = {"tasks": {
                        "task": "a"
                    }
                  }
    block = Block.load(section_data,
                    play=None,
                    task_include=None,
                    role=None,
                    variable_manager=variable_manager,
                    loader=loader
                )
    include_data = {
                "apply": {
                    "hosts": "host1",
                    "block": [
                        {
                            "task": "b"
                        },
                        {
                            "task": "c"
                        }
                    ]
                },
                "block": [
                    {
                        "task": "d"
                    }
                ]
            }
    task_include = TaskInclude

# Generated at 2022-06-13 09:33:06.850625
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():

    def assert_vars(action, args, expected, parent_vars=None):
        '''
        Utility to test the vars returned by the TaskInclude.get_vars()
        method. It creates an include task with the given action and args
        (preprocessed), then runs the get_vars method and compares the
        result with the expected dictionary. The optional parent_vars can
        be set to the vars that the parent block of the task should have.
        '''
        task_include = TaskInclude({'action': action})
        task_include.args = args
        block = Block()
        block.vars.update(parent_vars or {})
        task_include._parent = block
        assert task_include.get_vars() == expected

    # test include task with no parent vars
    assert_v

# Generated at 2022-06-13 09:33:14.226530
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.task import Task
    from ansible.vars.manager import VariableManager

    # Test invalid options
    task_test = TaskInclude(block=None, role=None, task_include=None)
    task_test.action = 'include'
    task_test.args = {'file': 'file', 'foo': 'bar'}
    with pytest.raises(AnsibleParserError):
        task_test.check_options(task_test, data={})
    # Test invalid options for import_* task
    task_test.action = 'import_tasks'
    task_test.args = {'file': 'file', 'apply': 'foo'}

# Generated at 2022-06-13 09:33:21.829933
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    # block with apply attributes
    task_inc = TaskInclude()
    task_inc.args = dict(apply=dict(loop_with='{{item}}', ignore_errors=True))
    task_inc.build_parent_block()
    assert isinstance(task_inc, Block)
    assert task_inc.args == dict(loop_with='{{item}}', ignore_errors=True)

    # block without apply attributes
    task_inc = TaskInclude()
    task_inc.build_parent_block()
    assert isinstance(task_inc, TaskInclude)

# Generated at 2022-06-13 09:33:30.294217
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    play_context = {}
    block = Block(play_context, parent=None)
    action = 'include'
    file = 'test_file'
    apply_attrs = {'a': 1, 'b': 2, 'c': 3}
    args = {'_raw_params': file, 'apply': apply_attrs}
    ti = TaskInclude(block, action=action, args=args)
    p_block = ti.build_parent_block()
    assert isinstance(p_block, Block)
    assert p_block._parent == block
    assert p_block.block == []
    assert p_block.apply == apply_attrs
    assert p_block.a == 1
    assert p_block.b == 2
    assert p_block.c == 3

# Generated at 2022-06-13 09:33:36.241709
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    '''
    This test validates whether attribute apply
    is processed correctly.
    '''
    # Test with no apply attribute
    # Test with empty apply attribute
    # Test with apply attribute with invalid block attribute
    # Test with apply attribute with invalid block attribute
    # Test with apply attribute with empty block attribute
    # Test with apply attribute with non-empty block attribute
    pass
