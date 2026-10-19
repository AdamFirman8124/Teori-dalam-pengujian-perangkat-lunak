

# Generated at 2022-06-13 09:23:54.874559
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    class AnsibleModuleMock(object):
        class AnsibleModuleMock(object):
            ITEM = None
            MODULE_ARGS = {'action': 'include'}

        def __init__(self, module_name, **kwargs):
            for k,v in kwargs.items():
                self.MODULE_ARGS[k] = v

    class RoleMock(object):
        def __init__(self, **kwargs):
            for k,v in kwargs.items():
                setattr(self, k, v)

    # Test for issue #65771
    # Check that include_role and import_role don't accept the 'action' parameter
    ti = TaskInclude()
    incorrect_action = AnsibleModuleMock('include', action='a_bad_action')
    ti.preprocess_data

# Generated at 2022-06-13 09:24:05.247263
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    '''
    Test method for TaskInclude.check_options.
    '''

    task = TaskInclude()
    data = { 'action': 'include_role', 'file': 'test.yml' }
    task.check_options(task, data)
    assert ( 'file' not in task.args and '_raw_params' in task.args )
    assert ( task.args['_raw_params'] == 'test.yml' )

    data = { 'action': 'include_role', 'tags': ['test'] }
    task.check_options(task, data)
    assert ( 'tags' not in task.args)

    data = { 'action': 'include_role', 'no_log': True }
    task.check_options(task, data)

# Generated at 2022-06-13 09:24:09.509960
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    ti = TaskInclude()
    ds = dict(
        meta=dict(
            foo='bar'
        )
    )

    t = ti.preprocess_data(ds)
    assert 'meta' not in t

# Generated at 2022-06-13 09:24:20.644415
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    #Unit test for method get_vars of class TaskInclude

    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    class TaskIncludeForUnitTest(TaskInclude):

        def __init__(self, block=None, role=None, task_include=None, action='include'):
            super(TaskIncludeForUnitTest, self).__init__(block=block, role=role, task_include=task_include)
            self.action = action

        def get_parent(self):
            return self._parent

        def set_parent(self, parent):
            self._parent = parent


# Generated at 2022-06-13 09:24:30.109379
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    # Create a simple playbook task
    playbook_content = {
        'name': 'task_name',
        'action': 'include',
        'args': {
            'one': 1,
            'two': 2,
            'thre': [1, 2, 3],
            'four': [{'var': 5}]
        }
    }
    task = TaskInclude.load(playbook_content)
    vars = task.get_vars()
    assert vars == {'one': 1, 'two': 2, 'thre': [1, 2, 3], 'four': [{'var': 5}]}

    # Create a simple playbook task

# Generated at 2022-06-13 09:24:39.799593
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    ti = TaskInclude()

    # Option 'file' is valid for all actions
    assert ti.check_options({'action': 'include', 'args': {'file': 'test.yml'}}, {})
    assert ti.check_options({'action': 'import_role', 'args': {'file': 'test.yml'}}, {})
    assert ti.check_options({'action': 'include_role', 'args': {'file': 'test.yml'}}, {})
    assert ti.check_options({'action': 'import_playbook', 'args': {'file': 'test.yml'}}, {})

    # Option '_raw_params' is valid for all actions

# Generated at 2022-06-13 09:24:51.136445
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    from ansible.playbook.role.task_include import TaskInclude as TI
    from ansible.playbook.role.task_include import HandlerTaskInclude as HTI

    def assert_error(data, error):
        try:
            TaskInclude.load(data, block=None, role=None, task_include=None, variable_manager=None, loader=None)
        except AnsibleParserError as e:
            assert error in str(e)
        else:
            assert False, 'Expected AnsibleParserError'


# Generated at 2022-06-13 09:25:02.151469
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    from ansible.playbook.play import Play
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.utils.vars import combine_vars

    loader = DataLoader()

    inventory = InventoryManager(loader=loader, sources=['localhost'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    loader.set_basedir('/')


# Generated at 2022-06-13 09:25:10.444741
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    import sys
    import os
    import tempfile
    import shutil

    cur_dir = os.path.dirname(os.path.realpath(__file__))
    test_dir = os.path.join(cur_dir, 'test_data')
    test_input_dir = os.path.join(test_dir, "include_params")
    test_output = os.path.join(tempfile.mkdtemp())
    sys.path.append(test_input_dir)
    from include_task_with_args import TaskIncludeWithArgs

    # Testing with include
    for data in TaskIncludeWithArgs.load():
        # Create TaskInclude object
        test_task_include_obj = TaskInclude(task_include=None)

        # Modify data to pass to test_task_include_obj.pre

# Generated at 2022-06-13 09:25:18.017910
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    # Given a `- import_tasks:` task with a `with_items` loop
    action = 'import_tasks'
    data = {'action': action, 'with_items': [], 'tags': []}

    # When I validate it
    ti = TaskInclude()
    data = ti.preprocess_data(data)

    # Then it should have the `loop` attribute
    assert data['action'] == action
    assert 'loop' in data.keys()

# Generated at 2022-06-13 09:25:35.286666
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():

    display.verbosity = 0
    play_context = {}
    setattr(play_context, 'foobar_test_test', 'bar')
    block = Block(play=None, parent_block=None, role=None, task_include=None)
    ti = TaskInclude(block=block, role=None, task_include=None)
    ti.vars = {'foobar_test': 'baz'}
    ti.args = {'foo': 'bar'}
    ti.action = 'include'

    # Check the inclusion of args
    assert ti.get_vars() == {'foobar_test': 'baz', 'foo': 'bar'}

    # Check the exclusion of tags
    ti.args = {'tags': 'baz'}

# Generated at 2022-06-13 09:25:46.296915
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    task_data = {
        "action": "include",
        "args": {"file": "some_file"},
        "test": "test",
    }

    task = TaskInclude.load(
        task_data,
        block=None,
        role=None,
        task_include=None,
        variable_manager=None,
        loader=None,
    )
    task = task.preprocess_data(task_data)

    assert task["test"] is Sentinel, "Preprocess data should remove unknown attribute 'test'"
    assert "test" not in task_data, "Preprocess data should remove unknown attribute 'test' from original dictionary"

    task_data["action"] = "role"


# Generated at 2022-06-13 09:25:55.315276
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    # define sample data
    ds = dict(
        action='include_role',
        static='yes',
        name='test',
        tasks='tasks.yml'
    )
    # build class to test
    ti = TaskInclude()
    # call method to test
    preprocessed_ds = ti.preprocess_data(ds)
    # assert preprocess_data does not touch static
    assert 'static' in preprocessed_ds
    # assert preprocess_data does not touch name
    assert 'name' in preprocessed_ds
    # assert preprocess_data does not touch tasks
    assert 'tasks' in preprocessed_ds
    # assert preprocess_data removes static
    assert 'static' not in preprocessed_ds
    # assert preprocess_data removes name
    assert 'name' not in pre

# Generated at 2022-06-13 09:26:06.751213
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    # setup
    my_block = Block()
    my_play = Play()
    my_play.block = my_block
    my_task = TaskInclude()
    my_task._parent = my_block
    my_task._play = my_play

    # test
    task_block = my_task.build_parent_block()
    # assert the identity of the returned block
    assert task_block is my_task

    # setup
    my_task_with_apply = TaskInclude()
    my_task_with_apply._parent = my_block
    my_task_with_apply._play = my_play
    my_task_with_apply.args['apply'] = {}

    # test
    task_block = my_task_with_apply.build_parent_block()
    # assert the identity of the returned

# Generated at 2022-06-13 09:26:15.502257
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    block1 = Block()
    block1.vars = dict(foo='1', bar='1')

    t2 = TaskInclude()
    t2.args = dict(foo='2', bar='2')
    t2.action = 'include'
    t2.set_loader(None)
    t2._parent = block1
    t2.vars = dict(foo='3', bar='3')

    t3 = TaskInclude()
    t3.args = dict(foo='4', bar='4')
    t3.action = 'include_role'
    t3.set_loader(None)
    t3._parent = block1
    t3.vars = dict(foo='5', bar='5')

    t4 = TaskInclude()

# Generated at 2022-06-13 09:26:25.426017
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    from ansible.module_utils._text import to_text
    from ansible.playbook.play_context import PlayContext


# Generated at 2022-06-13 09:26:36.360471
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    from ansible.playbook.base import Base

    class DummyInclude(Base):
        def __init__(self):
            self.args = {}

    dummy_task = DummyInclude()

    # Test '- include: ...'
    TaskInclude.check_options(dummy_task, None)
    dummy_task.args['file'] = '/path/to/file'
    with pytest.raises(AnsibleParserError):
        dummy_task.args['not_valid_arg'] = ''
        TaskInclude.check_options(dummy_task, None)

    # Test '- include_tasks: ...'
    dummy_task.action = 'include_tasks'
    TaskInclude.check_options(dummy_task, None)

# Generated at 2022-06-13 09:26:50.349067
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    task_include = TaskInclude()
    # non-existing attribute
    data = {'non_existing': 1}
    with pytest.raises(AnsibleParserError) as excinfo:
        task_include.check_options({}, data)
    assert 'Invalid options for include' in str(excinfo.value)

    # no file
    data = {}
    with pytest.raises(AnsibleParserError) as excinfo:
        task_include.check_options({}, data)
    assert 'No file specified for include' in str(excinfo.value)

    # 'apply' used for an action different from 'include'
    data = {'action': 'include_role', 'apply': {}}

# Generated at 2022-06-13 09:27:01.935925
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    import pytest
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.play import Play
    from ansible.playbook.block import Block
    from ansible.vars.manager import VariableManager

    from units.mock.loader import DictDataLoader

    def _test_check_options(data, data_no_action=None, expected_exception=None, valid_action=None):
        data_no_action = data if data_no_action is None else data_no_action

        if valid_action is None:
            if expected_exception is None:
                pytest.fail('Test case requires valid_action or expected_exception')
            valid_action = list(C._ACTION_INCLUDE.keys())[0]

# Generated at 2022-06-13 09:27:11.457922
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    task = {'action': 'include_role', 'name': 'role'}
    ti = TaskInclude()
    display.warning = lambda msg: msg
    assert ti.preprocess_data(task) == {'action': 'include_role', 'name': 'role'}

    task = {'action': 'include_role', 'name': 'role', 'foo': 'bar'}
    C.INVALID_TASK_ATTRIBUTE_FAILED = False
    assert ti.preprocess_data(task) == {'action': 'include_role', 'name': 'role'}
    C.INVALID_TASK_ATTRIBUTE_FAILED = True

# Generated at 2022-06-13 09:27:26.363250
# Unit test for method load of class TaskInclude
def test_TaskInclude_load():

    class DummyVarManager(object):
        def __init__(self):
            self.data = {'hostvars': {}, 'groups': {}}
        def add_group_vars_file(self, f):
            pass
        def add_extra_file(self, f):
            pass
        def set_variable_manager(self, f):
            pass
        def get_vars(self, loader, play, host, task, include_hostvars=True, include_delegate_to=True):
            return self.data


# Generated at 2022-06-13 09:27:35.669929
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager

    loader = DataLoader()
    variable_manager = VariableManager()
    apply_attrs = {}
    apply_attrs['block'] = []
    p_block = Block.load(
        apply_attrs,
        play=play,
        task_include=self,
        role=self._role,
        variable_manager=self._variable_manager,
        loader=self._loader,
    )
    assert(isinstance(TaskInclude.build_parent_block, TaskInclude))

# Generated at 2022-06-13 09:27:42.388879
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.utils.vars import combine_vars

    # Some utility function to create the task object and test
    def opt_is_dict(ti, opt, value):
        return isinstance(ti.args[opt], dict) and ti.args[opt] == value
    def opt_is(ti, opt, value):
        return ti.args[opt] == value
    def opt_is_dynamic(ti, opt):
        return not isinstance(ti.args[opt], dict)
    def opt_is_sentinel(ti, opt):
        return ti.args[opt] is Sentinel
    def check_includes(opt):
        task = TaskInclude({'include': opt})
        task.check_options(task, {})
        return

# Generated at 2022-06-13 09:27:57.782478
# Unit test for method load of class TaskInclude
def test_TaskInclude_load():

    import ansible.playbook
    import ansible.template
    import ansible.vars
    import ansible.utils.vars
    import ansible.utils.plugin_docs
    from ansible.template import Templar

    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()

    # Ansible's playbook.py file uses absolute imports to prevent circular
    # imports, but Ansible's module_utils directory uses relative imports.
    # The relative imports don't work when importing module_utils as a
    # package (from ansible import module_utils).  The following code should
    # allows both styles of import to work.

# Generated at 2022-06-13 09:28:05.281056
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    # Setup the test
    import ansible.playbook.test
    ti = ansible.playbook.TaskInclude(block=None, role=None)
    ti.action = 'include'
    ti.args = dict(a=1,b=2,c=3)
    ti._parent = type('Parent', (object,), {'get_vars': lambda: dict(d=4,e=5)})()

    # The test
    x = ti.get_vars()

    # Check the result
    assert x == dict(a=1,b=2,c=3,d=4,e=5), '''TaskInclude.get_vars returned unexpected value when action is 'include' '''



# Generated at 2022-06-13 09:28:16.532405
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    '''
    This is just the part of the unit test for the method 'check_options'
    of class TaskInclude. The method 'check_options' is tested in each
    sub-class since each sub-class is different.
    '''
    # test with no action
    task_data = dict(file='/my/include/file.yml')
    task = TaskInclude().check_options(TaskInclude().load_data(task_data), task_data)
    assert task.args.get('_raw_params') == '/my/include/file.yml'
    assert task.args.get('apply') is None

    # test with non-include action

# Generated at 2022-06-13 09:28:24.241164
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    task_include_instance = TaskInclude()
    task_include_instance.action = 'include'
    task_include_instance.args = {'a': 'yes', 'b': 'no'}
    task_include_instance.vars = {'c': 'maybe', 'd': 'so'}
    parent_block = Block()
    parent_block.vars = {'e': 'ok', 'f': 'cool'}
    task_include_instance._parent = parent_block
    assert task_include_instance.get_vars() == {'a': 'yes', 'b': 'no', 'c': 'maybe', 'd': 'so', 'e': 'ok', 'f': 'cool'}

    # This is the old case
    task_include_instance.action = 'import_role'
    task_include_

# Generated at 2022-06-13 09:28:31.483762
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    import ansible.plugins.loader as loader_module
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.playbook.play import Play
    from ansible.template import Templar

    class Loader():
        # Dummy loader class for unit test
        def __init__(self):
            self.templar = Templar()

        def load_from_file(self, path):
            return '''
                - include: test_include_file.yml
                    apply:
                        when: should_include
                        tags: include_tags

                - include_role:
                    name: test_include_role
                    apply:
                        when: should_include
                        tags: include_tags
            '''


# Generated at 2022-06-13 09:28:41.682167
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():

    from ansible.playbook.play_context import PlayContext
    import ansible.plugins.loader as plugins

    data = {'action':'include', 'remote_user': 'local'}
    ti = TaskInclude()
    ti.action = 'include'
    ti.vars = {'name': 'test'}
    ds = ti.preprocess_data(data)

    #no changes are expected
    assert(ds == data)

    data = {'action':'import_role', 'remote_user': 'local'}
    ti.action = 'import_role'
    ti.vars = {'name': 'test'}
    ds = ti.preprocess_data(data)

    #no changes are expected
    assert(ds == data)


# Generated at 2022-06-13 09:28:45.255909
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    assert TaskInclude.preprocess_data({'action': 'include', 'file': 'vars.yml'}) == {
        'action': 'include',
        'args': {'file': 'vars.yml'},
        'file': 'vars.yml',
        '_raw_params': 'vars.yml',
    }

# Generated at 2022-06-13 09:29:02.109015
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    '''
    This unit test verifies the proper behavior of the method 'get_vars'
    of class TaskInclude.
    '''

    # Create some test variables.
    include_args = dict(a=2, x=dict(b=7, c=8), e=98)
    include_vars = dict(d=4, x=dict(b=9, c=0))
    block_vars = dict(x=dict(b=3, c=4))
    block_action = 'test_TaskInclude_get_vars'

    # The task should not have access to its own vars dictionary
    # and to its own block vars.
    included_vars = include_args.copy()
    included_vars.update(include_vars)

# Generated at 2022-06-13 09:29:16.621278
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    '''
    Test for TaskInclude and HandlerTaskInclude
    '''
    from ansible.playbook.task_include import HandlerTaskInclude
    from ansible.playbook.task import Task
    import datetime
    class MockTask(Task):
        def __init__(self, action):
            self.action = action
            self.args = {}
    task_include = TaskInclude()
    handler_task_include = HandlerTaskInclude()
    # action with 'include'
    # apply is not in VALID_ARGS
    task = MockTask('include')
    task.args['apply'] = 'apply_value'
    task_include.check_options(task, {'action': 'include', 'apply': 'apply_value'})
    assert not task.args.get('apply')

    # action with 'include

# Generated at 2022-06-13 09:29:26.150693
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    t_i = TaskInclude()

    # test validation of any other args
    ti = type('task_include', (object,), {})()
    ti.args = {'foo': 'bar'}
    ti.action = t_i.action
    ti = t_i.check_options(ti, {})
    assert ti.args == {'_raw_params': 'bar'}, ti.args

    # test validation of other args if we are dealing with static include
    ti = type('task_include', (object,), {})()
    ti.args = {'foo': 'bar'}
    ti.action = 'include'
    ti = t_i.check_options(ti, {})
    assert ti.args == {'foo': 'bar', '_raw_params': 'bar'}, ti.args

    # test

# Generated at 2022-06-13 09:29:32.364212
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    block = Block()
    block.vars.update({'a': 1})

    task_a = TaskInclude(block=block)
    task_a.args.update({'a': 2})

    task_b = TaskInclude(block=task_a)
    task_b.args.update({'a': 3})

    res = task_b.get_vars()
    assert(res['a'] == 3)
    assert('a' in task_b.get_vars())

    task_a.action = 'include'
    res = task_b.get_vars()
    assert(res['a'] == 3)
    assert('a' in task_b.get_vars())



# Generated at 2022-06-13 09:29:41.133033
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.role import Role
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.errors import AnsibleParserError

    data = {'action': 'include', 'args': {'file': 'somefile.yml'}}
    variable_manager = VariableManager()
    loader = DataLoader()

    task = TaskInclude.load(data, variable_manager=variable_manager, loader=loader)

    assert task.check_options(task, data) == task
    assert task.args['file'] == None

# Generated at 2022-06-13 09:29:49.028578
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    from ansible.playbook.block import Block
    from ansible.playbook.task import HandlerTaskInclude

    block = Block()

    for action in C._ACTION_ALL_INCLUDE_TASKS:
        data = {'action': action}
        task = TaskInclude.load(data, block=block)
        assert task.action == action
        check_options_result = TaskInclude.check_options(task, data)
        assert check_options_result.action == action

    with pytest.raises(AnsibleParserError, match=r'[\s\S]*No file specified for include[\s\S]*'):
        TaskInclude.check_options(TaskInclude(block=block), {'action': 'include'})


# Generated at 2022-06-13 09:29:58.740662
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    #
    # 1. Valid options
    #
    #    a) _raw_params
    #
    task1 = TaskInclude.load({'_raw_params': 'include1.yml'}, block=None, task_include=None)
    assert task1.args['_raw_params'] == 'include1.yml'
    assert 'file' not in task1.args, "Unexpected 'file' key in args of %s" % task1
    assert 'apply' not in task1.args, "Unexpected 'apply' key in args of %s" % task1
    #
    #    b) file
    #
    task2 = TaskInclude.load({'file': 'include2.yml'}, block=None, task_include=None)

# Generated at 2022-06-13 09:30:07.427166
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.role_include import IncludeRole


# Generated at 2022-06-13 09:30:13.186889
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    from ansible.playbook.block import Block

    # In this test we just verify that the method returns a Block
    task_include = TaskInclude()
    task_include.args['apply'] = {'block': []}
    result = task_include.build_parent_block()

    assert isinstance(result, Block)


# Generated at 2022-06-13 09:30:23.124935
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    class MyVarsModule(object):
        def __init__(self, vars):
            self.vars = vars
        def get_vars(self, loader=None, path=None, dependencies=None,
                     overrides_loader=None,
                     context=None,
                    ):
            return self.vars
    class MyPlaybook(object):
        def __nonzero__(self):
            return False
    class MyParentBlock(object):
        def __init__(self, play):
            self._play = play
        def get_vars(self):
            return {'var1': 'var1_value', 'var2': 'var2_value'}
    class MyTaskInclude(TaskInclude):
        def __init__(self):
            self.vars = {}
            self.args = {}


# Generated at 2022-06-13 09:30:37.981513
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    task = TaskInclude.load({'include': 'test1.yml'})
    assert(task.get_vars() == {})
    task = TaskInclude.load({'file': 'test1.yml'})
    assert(task.get_vars() == {})
    task = TaskInclude.load({'include': 'test1.yml', 'tags': 'test1'})
    assert(task.get_vars() == {})
    task = TaskInclude.load({'include': 'test1.yml', 'vars': {'test1': 'test1'}})
    assert(task.get_vars() == {'test1': 'test1'})

# Generated at 2022-06-13 09:30:47.568341
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    # Test 1: Test when apply is not specified
    taskinclude_obj = TaskInclude()
    parent_block_obj = taskinclude_obj.build_parent_block()
    assert type(parent_block_obj) is not Block
    assert parent_block_obj == taskinclude_obj

    # Test 2: Test when apply is specified. There could be more tests
    # that could be added here, depending on the kind of apply_attrs
    # specified.
    taskinclude_obj.args = {'apply': {}}
    parent_block_obj = taskinclude_obj.build_parent_block()
    assert type(parent_block_obj) is Block
    assert parent_block_obj.parent == taskinclude_obj

Task.register_type('include', TaskInclude)

# Generated at 2022-06-13 09:30:56.328921
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    package_parts = __name__.split('.')[:-1]
    package_parts.append('mock')
    mock_mod_name = '.'.join(package_parts)

    try:
        # importlib was introduced in python 2.7
        from importlib import import_module
    except ImportError:
        # Mock import_module instead
        def import_module(module_name):
            if module_name == mock_mod_name:
                return MockModule()
            else:
                raise ImportError

    task = TaskInclude()
    my_arg_names = frozenset([])
    bad_opts = my_arg_names.difference(task.VALID_ARGS)
    assert not bad_opts

    assert task.check_options(task, None) is task

    task.action = 'include'

# Generated at 2022-06-13 09:31:06.526239
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    # We cannot simply use the 'load' method here as it calls 'load_data' which will read a file (if it exists)
    # So we call 'load_data' with dummy data and apply the 'check_options' method on the result
    task_include = TaskInclude()
    task_data = {
        u'action': u'include',
        u'apply': {u'foo': u'bar'},
        u'file': u'foo',
    }
    variables = {
        'foo': 'bar',  # dummy variable
    }
    # 'apply' should be accepted for the default action (when no attribute 'action' is specified)
    task = task_include.check_options(task_include.load_data(task_data, variable_manager=variables), task_data)
    assert task.args['apply']

# Generated at 2022-06-13 09:31:16.989324
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    ''' Test TaskInclude.build_parent_block() '''
    # initialize
    data = dict(
        name = "name-in-play",
        action = "action-in-play",
        when = "when-in-play",
        tags = "tags-in-play",
        apply = dict(
            name = "name-in-block",
            action = "action-in-block",
            when = "when-in-block",
            tags = "tags-in-block",
        ),
    )
    ti = TaskInclude()
    ti_block = ti.build_parent_block()
    for k,v in data.items():
        if k != 'apply':
            setattr(ti, k, v)


# Generated at 2022-06-13 09:31:32.151687
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    obj = TaskInclude()
    obj.role = None
    obj.vars = {}
    obj.args = {}
    obj.parent = None
    res = obj.get_vars()
    assert (res == {})

    obj = TaskInclude()
    obj.role = None
    obj.vars = {}
    obj.args = {'one': 1, 'two': 2}
    obj.parent = None
    obj.action = 'include'
    res = obj.get_vars()
    assert (res == {'one': 1, 'two': 2})

    obj = TaskInclude()
    obj.role = None
    obj.vars = {'one': 1, 'two': 2}
    obj.args = {'three': 3, 'four': 4}
    obj.parent = None
    obj

# Generated at 2022-06-13 09:31:38.336155
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    from ansible.playbook.block import Block
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    my_task = TaskInclude()
    my_task.action = 'include'
    my_task.args = {'hello': 'world'}
    my_task.vars = {'hello': 'world'}
    assert my_task.get_vars() == {'hello': 'world'}
    my_task.action = 'import_role'
    assert my_task.get_vars() == {'hello': 'world'}
    my_task.action = 'include'
    p_block = my_task.build_parent_block()
    assert isinstance(p_block, Block)
    my_task.action = 'include_role'
    my

# Generated at 2022-06-13 09:31:46.618167
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.playbook.play import Play

    task = TaskInclude()
    pb = Play()

    task._parent = pb
    task.args = dict(one=AnsibleUnicode(u'1'), two=AnsibleUnicode(u'2'))

    got_vars = task.get_vars()

    assert dict(one=AnsibleUnicode(u'1'), two=AnsibleUnicode(u'2')) == got_vars



# Generated at 2022-06-13 09:31:54.532298
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    from ansible.playbook.play_context import PlayContext

    task = TaskInclude()
    # Reset the arguments of the task
    task.args = {}
    # load_data uses check_options to validate the args, so we use this
    # to test it.
    data = {'include': 'myrole.yml'}
    # Copy the attributes of the task to test them later
    prev_args = task.args.copy()
    task = task.load_data(data, variable_manager=None, loader=None)

    # Check the attributes
    assert task.args == prev_args
    assert task.args.get('_raw_params') == 'myrole.yml'



# Generated at 2022-06-13 09:32:03.278902
# Unit test for method load of class TaskInclude
def test_TaskInclude_load():
    # Test the case when the task L{TaskInclude} is instantiated from a block
    from ansible.playbook.block import Block
    from ansible.playbook.play_context import PlayContext
    from ansible.vars import VariableManager
    from ansible.utils.vars import combine_vars


# Generated at 2022-06-13 09:32:27.342719
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    # action "include"
    display.verbosity = 3

    task_include_1 = TaskInclude()
    task_include_1.action = "include"
    task_include_1.args = dict(
        a=dict(
            b=2,
            c=3,
        ),
        d=5,
    )
    task_include_1.vars = dict(
        # just to make sure we do not leak Task vars into TaskInclude
        t=dict(
            u=6,
            v=7,
        ),
        w=8,
    )

# Generated at 2022-06-13 09:32:36.839192
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():

    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.task_include import TaskInclude

    a_role = RoleDefinition()

    b = TaskInclude(block=a_role, role=a_role)
    c = TaskInclude(block=b, role=a_role)
    d = TaskInclude(block=c, role=a_role)
    f = TaskInclude(block=d, role=a_role)

    assert f._block == d
    assert f._parent == c

    apply_attrs = {'when': 'puppies'}
    g = TaskInclude(block=f, role=a_role, task_include=f)
    g.args['apply'] = apply_attrs
    assert g.build_parent_block() != f

# Generated at 2022-06-13 09:32:51.629806
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    task = TaskInclude()
    assert task
    with pytest.raises(AnsibleParserError):
        task.check_options({'action': 'include', 'BAD_ATTR': True}, data={'action': 'include', 'BAD_ATTR': True})
    with pytest.raises(AnsibleParserError):
        task.check_options({'action': 'include', 'file': 'MY_FILE'}, data={'action': 'include', 'file': 'MY_FILE'})
    with pytest.raises(AnsibleParserError):
        task.check_options({'action': 'import_role', 'apply': {'a': 'b'}}, data={'action': 'import_role', 'apply': {'a': 'b'}})

# Generated at 2022-06-13 09:33:00.386007
# Unit test for method load of class TaskInclude

# Generated at 2022-06-13 09:33:11.845512
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    #get_vars should return all variables set in the TaskInclude
    task = TaskInclude()

    #action is not include, should return all_vars of the super class
    task.action = 'include_role'
    assert task.get_vars() == task.all_vars

    #action is include, should return all_vars of the super class
    task.action = 'include'
    assert task.get_vars() == task.all_vars

    #action is include, should return all_vars of the super class + the vars
    task.vars = {'test_var': 'test'}
    assert task.get_vars() == {'test_var': 'test'}

    #action is include, should return all_vars of the super class + the vars + the args
    task

# Generated at 2022-06-13 09:33:22.968949
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    # given
    task_include = TaskInclude()
    task_include.args = {
        'apply': {
            'notify': [
                'inform the law',
                {
                    'inform': {
                        'msg': 'The law is informed about ...'
                    }
                }
            ]
        },
        'ignore_errors': False,
        'debugger': 'python'
    }

    # when
    p_block = task_include.build_parent_block()

    # then
    assert 'apply' not in task_include.args, 'build_parent_block should remove \'apply\' from args'
    assert isinstance(p_block, Block), 'build_parent_block should return a Block instance'

# Generated at 2022-06-13 09:33:31.702542
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    from ansible.vars.manager import VariableManager
    import ansible.constants as C

    p = Play().load({'name':'test play', 'hosts': [], 'gather_facts':'yes'}, variable_manager=VariableManager(), loader=None)
    p.post_validate(play_context=PlayContext())

    # will produce an empty block
    empty_block = TaskInclude.load({'action': 'include'},
                                   play=p,
                                   task_include=Task(),
                                   variable_manager=VariableManager(),
                                   loader=None)
    assert empty_block._parent is None

# Generated at 2022-06-13 09:33:41.550061
# Unit test for method load of class TaskInclude
def test_TaskInclude_load():
    test_file_name = 'test_file.yml'
    test_other_option = 'other_option'
    data_dict = {
        'action': 'include',
        'args': {
            'file': test_file_name,
            'apply': {'key': 'value'},
            test_other_option: 'some value',
        }
    }
    task = TaskInclude.load(data_dict)
    assert task.action == 'include'
    assert task.args['_raw_params'] == test_file_name
    assert task.args['apply'] == {'key': 'value'}
    assert task.args[test_other_option] == 'some value'