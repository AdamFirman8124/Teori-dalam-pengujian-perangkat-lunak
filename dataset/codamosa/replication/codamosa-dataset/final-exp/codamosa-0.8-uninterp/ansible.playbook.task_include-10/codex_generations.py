

# Generated at 2022-06-13 09:23:52.727264
# Unit test for method load of class TaskInclude
def test_TaskInclude_load():
    '''
    If it is loaded from a role file, the role is the parent of the include.
    The loaded task is added to the list of children of the parent block.
    The parent block is populated from the 'apply' keyword.
    '''
    from ansible.playbook.role_include import IncludeRole
    from ansible.playbook.role_context import RoleContext

    class Parent(object):

        _tasks = []

        def __init__(self):
            self._blocks = []
            self._vars = dict()
            self._parent = None

        def add_block(self, block):
            self._blocks.append(block)

        def block(self, role_context):
            return self._blocks[0]

        def get_vars(self):
            return self._vars


# Generated at 2022-06-13 09:23:59.390630
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    from ansible.playbook.play import Play
    from ansible.parsing.utils.addresses import parse_address
    from ansible.vars.manager import VariableManager

    playbook_vars = [
        'ansible_python_interpreter',
        'ansible_connection',
        'inventory_hostname',
        'inventory_hostname_short',
        'group_names',
        'groups',
    ]

    p = Play().load({
        'hosts': 'localhost',
        'gather_facts': False,
        'tasks': [
            {'action': 'include', 'args': {'file': 'tests/playbook_include_vars/main.yml'}},
        ],
    }, variable_manager=VariableManager(), loader=None)

# Generated at 2022-06-13 09:24:11.447959
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    data, ignore_errors = ('include_tasks',     {'file': 'somefile', 'ignore_errors': True, 'tags': 'test'}), True
    data = TaskInclude.preprocess_data(data)
    assert 'ignore_errors' in data and isinstance(data['ignore_errors'], bool) and data['ignore_errors'] == ignore_errors
    assert 'tags' not in data
    assert isinstance(data, tuple)

    # ignored_attributes is empty and failed=True
    data = ('include_tasks', {'file': 'somefile', 'tags': 'test'})
    data = TaskInclude.preprocess_data(data)
    assert not data

    # ignored_attributes is empty and failed=False

# Generated at 2022-06-13 09:24:21.817720
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    from ansible.playbook.play import Play
    from ansible.plugins.loader import action_loader
    import ansible.playbook.task
    import ansible.playbook.block

    # Create a TaskInclude object
    my_task = ansible.playbook.task.TaskInclude()

    # Create a Play object

# Generated at 2022-06-13 09:24:30.940888
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    '''
    task:
      include:
        file: foo.yml
        apply:
          loop: "{{ myvar.results }}"
          ignore_errors: True
      tags: never
    '''
    data = {'action': 'include', 'file': 'foo.yml', 'apply': {'loop': '{{ myvar.results }}', 'ignore_errors': True, 'block': []}}
    task = TaskInclude.load(data)
    assert task.action == data['action'], "Action is not %s. Got %s" % (data['action'], task.action)
    assert 'ignore_errors' not in task.args, "Key 'ignore_errors' found in %s" % task.args
    assert 'block' not in task.args['apply'], "Key 'block' found in %s"

# Generated at 2022-06-13 09:24:43.375818
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():

    import pytest
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    my_block = Block()
    my_block._vars = dict(
        block_var1 = 'bar',
        block_var2 = 'baz',
    )

    my_play = Play()
    my_play._vars = dict(
        play_var1 = 'foo',
        play_var2 = 'bar',
    )

    my_task_include = TaskInclude()
    my_task_include._parent = my_block
    my_task_include._play = my_play
    my_task_

# Generated at 2022-06-13 09:24:56.106621
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins.loader import cli_conf_loader
    class Dim:
        def __init__(self, file=None, when=None, action=None):
            self.file=file
            self.when=when
            self.action=action
            self.args={}
            self.tasks=[]
            self.vars={}
    ds1=Dim("./test/test_whatever1.yml", "whatever", "include_role")
    ds2=Dim("./test/test_whatever1.yml", "whatever", "include_tasks")
    ds3=Dim("./test/test_whatever1.yml", "whatever", "import_role")

# Generated at 2022-06-13 09:25:06.902381
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    from ansible.plugins.loader import include_role_tasks_apply_task_include
    from ansible.plugins.loader import include_tasks_apply_task_include
    from ansible.utils.vars import combine_vars
    ti = TaskInclude()
    ti._parent = Block()
    ti.vars = {'a': 1, 'b': 2}
    ti.args = {'b': 3, 'c': 4}
    assert ti.get_vars() == {'a': 1, 'b': 3, 'c': 4}
    ti.action = 'include_role'
    ti._parent._play = include_role_tasks_apply_task_include
    ti._parent.get_vars = lambda: {'a': 1, 'b': 2, 'tags': 3, 'when': 4}

# Generated at 2022-06-13 09:25:19.368400
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():

    task = TaskInclude()
    task._parent = type('Mock', (object,), {'get_vars': lambda: {}, '_play': 'test_play', '_role': 'test_role'})
    task._variable_manager = type('Mock', (object,), {'get_vars': lambda x: {}})
    task._loader = type('Mock', (object,), {'get_basedir': lambda: '', 'path_dwim': lambda x, y: x})

# Generated at 2022-06-13 09:25:31.733135
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    data = {
        'action': 'include_role',
        'name': 'foo',
        'file': 'bar',
        'asdf': '1234'
    }

    with Display().unregister_display():
        ti = TaskInclude()
        ti.preprocess_data(data)

    assert data == {
        'action': 'include_role',
        'name': 'foo',
        'file': 'bar',
        'asdf': '1234'
    }

    with Display().unregister_display():
        ti = TaskInclude()
        ti.preprocess_data(data)

    assert data == {
        'action': 'include_role',
        'name': 'foo',
        '_raw_params': 'bar',
        'asdf': '1234'
    }

# Generated at 2022-06-13 09:25:47.556525
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    # Test with valid 'action' and 'args'
    my_task = TaskInclude()
    data = {
        'action': 'include_tasks',
        'file': 'valid_file'
    }
    result = my_task.check_options(my_task.load_data(data), data)
    assert result is not None
    assert 'file' not in result.args
    assert '_raw_params' in result.args
    assert result.args['_raw_params'] == 'valid_file'

    # Test with valid 'action', 'args' and 'apply'
    my_task = TaskInclude()
    data = {
        'action': 'include_tasks',
        'file': 'valid_file',
        'apply': {}
    }

# Generated at 2022-06-13 09:25:56.258913
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    """
    Test the get_vars of class TaskInclude and make sure that the variable of
    class TaskInclude are valid.
    """
    block = None
    role = None
    task_include = None
    ti = TaskInclude(block, role, task_include)

    #Validation of 'args' in the TaskInclude when 'action' is not 'include'
    args = {}
    ti.args = args
    ti.action = "shell"
    all_vars = ti.get_vars()
    assert all_vars == args

    #Validation of 'args' in the TaskInclude when 'action' is 'include'
    args = {"include_test": "include_test"}
    ti.args = args
    ti.action = "include"

    all_vars = ti.get_vars

# Generated at 2022-06-13 09:26:07.416496
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    ds = {'a': 1, 'b': 2, 'c': 3}
    ti = TaskInclude()
    ds1 = ti.preprocess_data(ds)
    assert ds1 == ds

    ds = {'action': 'include', 'a': 1, 'b': 2}
    ti = TaskInclude()
    ds1 = ti.preprocess_data(ds)
    assert ds1 == {'action': 'include', 'b': 2}

    ds = {'action': 'include', 'a': 1, 'b': 2}
    ti = TaskInclude()
    ds1 = ti.preprocess_data(ds)
    assert ds1 == {'action': 'include', 'b': 2}


# Generated at 2022-06-13 09:26:15.953724
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    from ansible.playbook.task_include import HandlerTaskInclude
    task_include_class = TaskInclude
    for action in task_include_class.VALID_INCLUDE_KEYWORDS:
        # regular task
        data = {'action': action, 'args': {'file': 'foo'}}
        task = task_include_class.load(data)
        task_include_class.check_options(task, data)  # no error

        # include
        data = {'include': {'action': action, 'args': {'file': 'foo'}}}
        task = task_include_class.load(data)
        task_include_class.check_options(task, data)  # no error

        # include_tasks

# Generated at 2022-06-13 09:26:23.332359
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    class MockTask(TaskInclude):
        def __init__(self, *args, **kwargs):
            super(MockTask, self).__init__(*args, **kwargs)
            self.action = 'include_role'

    data = {
        'include_role': {
            'name': 'test',
            'tasks_from': 'main',
            'test': 'main',  # this should be ignored
        }
    }

    task = MockTask.load(data)
    assert task.action == 'include_role'
    assert 'test' not in task.args

# Generated at 2022-06-13 09:26:30.109784
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.playbook.playbook import Playbook
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.included_file import IncludedFile
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.plugins.loader import add_all_plugin_dirs
    from ansible.template import Templar
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.inventory.inventory import Inventory
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.task_result import TaskResult

# Generated at 2022-06-13 09:26:38.455317
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.playbook.play import Play
    from ansible.plugins import module_loader

    loader = DataLoader()
    inventory = Inventory(loader=loader, variable_manager=VariableManager(), host_list=['test'])
    play_source =  dict(
        name = "Ansible Play",
        hosts = 'all',
        gather_facts = 'no',
        tasks = [
            dict(action=dict(module='setup', args='')),
            dict(action=dict(module='fail', args=dict(msg='failure message')))
        ]
    )
    play = Play().load(play_source, variable_manager=VariableManager(), loader=loader)

# Generated at 2022-06-13 09:26:49.913013
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    from ansible.playbook.block import Block
    from ansible.playbook.play import Play
    from ansible.playbook.role import Role
    from ansible.vars.manager import VariableManager

    apply_attrs = {
      "attributes": {
        "when": "test"
      },
      "block": None,
      "name": "test"
    }

# Generated at 2022-06-13 09:27:01.481111
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    import ansible.constants as C

    task = Task()
    task.args = dict(file='hosts')
    task.action = 'include'
    task.args['apply'] = dict(serial='10')

    # Without action
    try:
        TaskInclude.check_options(task, {})
        assert(False)
    except AnsibleParserError as e:
        pass

    # With a wrong action
    task.action = 'task'
    try:
        TaskInclude.check_options(task, {})
        assert(False)
    except AnsibleParserError as e:
        pass

    # With a known action, without apply
    task.action = 'include'

# Generated at 2022-06-13 09:27:05.984503
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    from ansible.playbook import Play
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, sources=[])
    variable_manager.set_inventory(inventory)

    play_source =  dict(
        name = "Ansible Play",
        hosts = '',
        gather_facts = 'no',
        tasks = [
            dict(action=dict(
                __ansible_action__ = 'include',
                __ansible_module__ = 'include',
                apply = dict(free_form=['no_log']),
                file = 'test.yml'
            ))
        ]
    )

   

# Generated at 2022-06-13 09:27:19.899588
# Unit test for method load of class TaskInclude
def test_TaskInclude_load():
    task = TaskInclude()
    # invalid options
    data = dict(
        action='include',
        args=dict(
            invalid_opt1='invalid',
            invalid_opt2='invalid',
        )
    )
    with pytest.raises(AnsibleParserError) as exc:
        task.check_options(task.load_data(data), data)
    assert "Invalid options for include" in str(exc.value)
    assert "invalid_opt1,invalid_opt2" in str(exc.value)

    # no file specified
    data = dict(
        action='include',
        args=dict(
        )
    )
    with pytest.raises(AnsibleParserError) as exc:
        task.check_options(task.load_data(data), data)
   

# Generated at 2022-06-13 09:27:27.966231
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    import collections
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext

    # Test for preprocess_data for a 'static' include
    playbook = [{'hosts': 'all', 'tasks': [{'include': 'my_static_file'}]}]
    play = Play().load(playbook, variable_manager=None, loader=None)
    play.post_validate(PlayContext())
    ti = play
    ds = ti.tasks[0].preprocess_data(collections.OrderedDict(ti.tasks[0]._task_fields))
    assert collections.OrderedDict([('name', 'include'), ('include', 'my_static_file')]) == ds

    # Test for preprocess_data for a 'dynamic' include


# Generated at 2022-06-13 09:27:38.871177
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():

    # Use a mock to isolate the test
    from ansible.module_utils.six import PY3

    FieldAttribute_mock = FieldAttribute
    FieldAttribute_mock.is_normal_attribute = False
    FieldAttribute_mock.is_special_attribute = False

    if PY3:
        Task_mock_mro = Task
        TaskInclude_mock = TaskInclude
    else:
        Task_mock_mro = Task.__mro__[0]
        TaskInclude_mock = TaskInclude.__mro__[0]

    # Mock static and class attributes

# Generated at 2022-06-13 09:27:50.673662
# Unit test for method load of class TaskInclude
def test_TaskInclude_load():
    # Create an empty TaskInclude object
    ti = TaskInclude()

    # For each task action in the list
    for action in C._ACTION_ALL_INCLUDE_IMPORT_TASKS:
        # Build a data structure and validate it with TaskInclude to get a TaskInclude object
        data = {'action': action, 'args': {'file': 'something'}}
        ti = TaskInclude.load(data)

        # Check some properties of the TaskInclude object
        assert ti.action == action
        assert ti.args.get('_raw_params') == 'something'
        assert ti.block

        # Changed attributes for 'meta' tasks
        if action in C._ACTION_ALL_INCLUDE_IMPORT_TASKS:
            assert len(ti.block.block) == 0

# Generated at 2022-06-13 09:27:55.348318
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    from ansible.playbook.block import Block
    from ansible.playbook.role import Role

    task = TaskInclude()
    task._loader = None
    task._variable_manager = None
    task._task_include = None
    task._parent = Block()
    task._role = Role()
    task._play = None
    task._role = None

    result = task.build_parent_block()
    assert result == task

# Generated at 2022-06-13 09:28:04.846667
# Unit test for method load of class TaskInclude
def test_TaskInclude_load():
    data = {
        'action': 'include',
        'file': 'myinclude.yaml',
        'apply': {
            'tags': ['tag1'],
            'set_fact': {
                'test': 'test'
            }
        }
    }

    task_inc = TaskInclude.load(data)
    assert isinstance(task_inc, TaskInclude)
    assert isinstance(task_inc.args, dict)
    assert task_inc.action == 'include'
    assert task_inc.args['_raw_params'] == 'myinclude.yaml'
    assert 'set_fact' in task_inc.args.get('apply')
    assert task_inc.args.get('apply').get('tags') == ['tag1']

# Generated at 2022-06-13 09:28:15.513451
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    from ansible.playbook.play import Play
    from ansible.playbook.role_include import IncludeRole
    from ansible.playbook.role import Role

    # check play (without parent block)
    TaskInclude.include_role = TaskInclude.include
    task = TaskInclude.load(dict(action='include_role', name='foo'))
    pb = Play.load(dict(name='test', hosts=['all'], roles=['bar']), variable_manager=None, loader=None)
    pb.post_validate(pb.vars, [])
    task._play = pb
    assert task.get_vars() == dict(name='foo')

    # check play (with parent block)
    TaskInclude.include_role = TaskInclude.include
    task = TaskInclude.load

# Generated at 2022-06-13 09:28:25.560954
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    '''
    This method is used to test the preprocess_data method of class TaskInclude
    '''
    # Create a taskInclude object
    test_task = TaskInclude()
    # Verify that a 'name' key is added
    ds1 = {
        'action': 'import_role',
        'other_arg': 'test',
        'collections': ['test1'],
    }
    expected1 = {
        'name': 'test',
        'action': 'import_role',
        'other_arg': 'test',
        'collections': ['test1'],
    }
    # this will not modify the original ds
    res1 = test_task.preprocess_data(ds1)
    assert expected1 == res1

    # Verify any other key that is not in VALID_INCLU

# Generated at 2022-06-13 09:28:35.418366
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    import os
    import pytest

    class Options:
        connection = 'local'
        module_path = None
        forks = 10
        become = None
        become_method = None
        become_user = None
        check = False
        diff = False
        verbosity = 1
        timeout = 10

    options = Options()
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=['localhost,'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)

# Generated at 2022-06-13 09:28:44.036635
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():

    input_data = dict(key1='value1', key2='value2')
    # Object for testing method that doesn't extend TaskInclude
    class DummyClass(object):
        pass
    dummy_class = DummyClass()

    # Object for testing method that extends TaskInclude
    class DummyClass2(TaskInclude):
        def __init__(self):
            self._parent = None
            self._role = None
    dummy_class2 = DummyClass2()

    # Test when the action is not in the dict of allowed actions
    input_data['action'] = 'not_included_action'
    actual_data = dummy_class.preprocess_data(input_data)
    expected_data = dict(key1='value1', key2='value2', action='not_included_action')
    assert actual_

# Generated at 2022-06-13 09:29:12.044423
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    ti = TaskInclude()

    # Test when task is include
    ds = {'name': 'test_preprocess_data', 'include': ''}
    ds = ti.preprocess_data(ds)
    assert ds['name'] == 'test_preprocess_data'
    assert 'include' in ds

    # Test when task is static include
    ds = {'name': 'test_preprocess_data', 'include': '', 'static': ''}
    ds = ti.preprocess_data(ds)
    assert ds['name'] == 'test_preprocess_data'
    assert 'include' in ds
    assert 'static' in ds

    # Test when task is import_playbook
    ds = {'name': 'test_preprocess_data', 'import_playbook': ''}


# Generated at 2022-06-13 09:29:22.096826
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():

    # Create fake include task with args
    apply_attrs = {}
    apply_attrs['block'] = []
    apply_attrs['when'] = 'condition'
    apply_attrs['loop'] = '{{ item }}'
    apply_attrs['name'] = 'block name'
    apply_attrs['ignore_errors'] = True
    apply_attrs['tags'] = ['tag1', 'tag2']
    apply_attrs['run_once'] = True
    ti = TaskInclude()
    ti.args = {'apply': apply_attrs}

    # Build the parent block and check the result
    pb = ti.build_parent_block()
    assert pb.when == 'condition'
    assert pb.loop == '{{ item }}'
    assert pb.name == 'block name'

# Generated at 2022-06-13 09:29:27.187981
# Unit test for method preprocess_data of class TaskInclude
def test_TaskInclude_preprocess_data():
    data = {'some_attr': 'some_value', 'action': 'include_role'}
    task_include = TaskInclude()
    assert repr(task_include.preprocess_data(data)) == "{'action': 'include_role'}"

# Generated at 2022-06-13 09:29:29.255857
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    vars = dict()
    test_obj = TaskInclude()
    res = test_obj.get_vars()
    expected = vars
    assert res == expected



# Generated at 2022-06-13 09:29:37.719156
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    data = {
        'apply': 'my_apply',
        'file': 'my_file',
        'my_arg': 'my_arg'
    }

    ti = TaskInclude()
    task = ti.check_options(
        data,
        data
    )

    assert task['_raw_params'] == 'my_file'
    assert task['apply'] == 'my_apply'
    assert 'file' not in task
    assert 'my_arg' not in task

# Generated at 2022-06-13 09:29:40.655797
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    # Arrange
    options = { '_raw_params': './some/path', 'apply': 'some_value' }
    data = { '_raw_params': './some/path', 'apply': 'some_value' }
    ti = TaskInclude()

    # Act
    ti.check_options(options, data)

    # Assert
    assert 'file' in options
    assert '_raw_params' in options
    assert 'apply' in options

# Generated at 2022-06-13 09:29:46.051063
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    import unittest
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.play import Play
    from ansible.playbook.role import Role
    from ansible.playbook.role.include import RoleInclude
    from ansible.vars.manager import VariableManager

    mock_loader = lambda self, *args, **kwargs: True

    class TestRole(Role):
        pass

    class TestPlay(Play):
        pass

    class TestBlock(Block):
        pass

    class TestTask(Task):
        pass

    variabes_dict={'app1_url': 'https://app.example.com', 'app2_url': 'https://app.example.com'}

    # No apply
    task_include_no_apply = TaskIn

# Generated at 2022-06-13 09:29:50.225203
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    class Fake_Task():
        def __init__(self, tasks):
            self.tasks = tasks
            self._parent = self

        def _get_role(self):
            return None

        def _get_play(self):
            return None

        def _get_variable_manager(self):
            return None

        def _get_loader(self):
            return None

    class Fake_Manager():
        def get_vars(self, load_vars=True):
            return {}

    class Fake_Role():
        def __init__(self, name):
            self.name = name

    class Fake_Play():
        def __init__(self):
            self.roles = [Fake_Role('fake_role')]

    my_task = Fake_Task([])
    my_task._variable_manager = Fake_

# Generated at 2022-06-13 09:29:57.191065
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    class AnsibleTaskInclude(TaskInclude):
        '''
        Mock class for testing get_vars method of TaskInclude
        '''
        def __init__(self):
            super(AnsibleTaskInclude, self).__init__()
            self.parent_vars = {}
            self.vars = {}
            self.args = {}
            self.action = 'include'

        def get_vars(self):
            return super(AnsibleTaskInclude, self).get_vars()

    class AnsibleBlock():
        def __init__(self):
            self.vars = {'block_vars': "block_vars"}
            self.parent = AnsibleBlockParent()


# Generated at 2022-06-13 09:30:05.015679
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    from ansible.playbook.play_context import PlayContext
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group

    loader = DataLoader()

    # Fake inventory for testing
    hosts = [Host(name='server'), Host(name='worker')]
    host_vars = loader.load_from_file('%s/../../../test/units/vars/host_vars.yml' % os.path.dirname(__file__))
    host_group = Group('ungrouped')
    host_group.add_host(hosts[0])
    host_group.add_host(hosts[1])
    host_group.set_variable('g_var', 'value_g_var')
    hosts

# Generated at 2022-06-13 09:30:22.484764
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():

    # Create a dummy block in which we will include that has apply to make a parent block
    block_with_apply = Block()
    block_with_apply.vars = dict(name=dict(keys=['key1', 'key2'], value='value_of_{key}'))

    # Create TaskInclude with apply
    task_include_with_apply = TaskInclude()
    task_include_with_apply.action = 'include'
    task_include_with_apply.args = dict(apply=dict(env=dict(key2='test_env_value')))
    task_include_with_apply._parent = block_with_apply

    # Create TaskInclude without apply
    task_include_without_apply = TaskInclude()
    task_include_without_apply.action = 'include'
    task_include_without

# Generated at 2022-06-13 09:30:32.667497
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():

    class FakeParent:
        def __init__(self, vars):
            self.vars = vars

        def get_vars(self):
            return self.vars

    class FakeBlock:
        def __init__(self, vars):
            self.vars = vars

    class FakeTaskInclude(TaskInclude):
        def __init__(self, action, args, parent, vars, block, role=None, task_include=None):
            self.action = action
            self.args = args
            self._parent = parent
            self.vars = vars
            self._block = block
            self._role = role
            self._task_include = task_include

    def assert_vars(action, args, parent, vars, block, expected, msg=None):
        ti = FakeTaskIn

# Generated at 2022-06-13 09:30:42.673514
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    p = Play()

    # For `include` task
    t = TaskInclude.load(dict(action='include', _raw_params='foobar'), block=p)
    assert t.args == dict(_raw_params='foobar')

    # For `when` use case
    t = TaskInclude.load(dict(action='include', _raw_params='foobar', when='true'), block=p)
    assert t.args == dict(_raw_params='foobar', when='true')

    # For `include_tasks` task
    t = TaskInclude.load(dict(action='include_tasks', _raw_params='foobar'), block=p)
    assert t.args == dict(_raw_params='foobar')

    # For `include_role` task

# Generated at 2022-06-13 09:30:53.022713
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    """
    Test that the method build_parent_block for the class TaskInclude
    works as expected.
    """
    from ansible.playbook.play_context import PlayContext
    from ansible.utils.sentinel import Sentinel

    from ansible.playbook.task import Task
    from ansible.playbook.play import Play

    from ansible.playbook.block import Block
    from ansible.playbook.role import Role

    from ansible.playbook.role.include import IncludeRole

    from ansible.playbook.handler import HandlerTaskInclude

    class MockPlayContext(PlayContext):

        def __init__(self):
            self.remote_addr = None
            self.remote_user = 'test_remote_user'

    # create a mock role and play, which are needed for creating a task
    r = Role()

# Generated at 2022-06-13 09:31:04.359026
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    ti = TaskInclude()

    # check options for a valid TaskInclude
    apply_attrs = dict(block='a_block')
    data = dict(action='a_action', _raw_params='an_include', apply=apply_attrs)
    task = dict(action='a_action', _raw_params='an_include', apply=apply_attrs)
    task = ti.check_options(task, data)
    assert task == dict(action='a_action', _raw_params='an_include', apply=apply_attrs)

    # check options for an invalid TaskInclude
    apply_attrs = dict(block='a_block')
    data = dict(action='a_action', _raw_params='an_include', foo='a_foo', apply=apply_attrs)

# Generated at 2022-06-13 09:31:11.994421
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():

    # Since the method is not static and it is not named 'validate_options' on purpose,
    # 'validate_options' is a dummy variable
    def validate_options(arg_names, valid_args, action, bad_args, raw_params, obj, apply_attrs):
        ti = TaskInclude()
        ti.args = {
            '_raw_params': raw_params,
            'apply': apply_attrs,
        }
        if bad_args:
            ti.args.update(bad_args)
            with pytest.raises(AnsibleParserError, match='^Invalid options for {}: {}$'.format(action, ','.join(list(bad_args)))):
                ti.check_options(ti, obj)
        ti.action = action

# Generated at 2022-06-13 09:31:20.022180
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    # test invalid apply attribute
    data = dict(action='include_role', apply='1')
    task = TaskInclude(task_include=False)
    task.load_data(data)
    try:
        task.build_parent_block()
        assert False, 'apply must be a dict'
    except AnsibleParserError:
        pass

    # test apply attribute with empty block
    data = dict(action='include_role', apply=dict(block=[]))
    task = TaskInclude(task_include=False)
    task.load_data(data)
    task.build_parent_block()

    # test apply attribute with block
    data = dict(action='include_role', apply=dict(block=[dict(action='action1')]))
    task = TaskInclude(task_include=False)

# Generated at 2022-06-13 09:31:34.131127
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader

    variable_manager = VariableManager()
    loader = DataLoader()

    data = dict(
        name='TaskName',
        action='include_role',
        apply=dict(
            block='main',
            rescue=[dict(name='Rescue1'), dict(name='Rescue2')],
        ),
    )

    ti = TaskInclude.load(data, variable_manager=variable_manager, loader=loader)

    # Check if the method build_parent_block created the expected parent block

# Generated at 2022-06-13 09:31:41.936318
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    from ansible.playbook.play_context import PlayContext

    play_context = PlayContext()
    play_context.remote_addr = '127.0.0.1'
    play_context.connection = 'mock'
    play_context.network_os = 'default'
    play_context.remote_user = 'remote_user'
    play_context.become = False
    play_context.become_method = 'sudo'
    play_context.become_user = 'root'

    block_data = dict(
        block=[]
    )

    # Create a Block instance to test TaskInclude.build_parent_block with:
    # - no apply in args (f.e. default args when task.apply is not specified)
    # - apply with an empty dict in args (f.e. task.apply is

# Generated at 2022-06-13 09:31:52.017456
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.variable_manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.utils.vars import load_extra_vars
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.utils.path import unfrackpath
    from unit.mock.loader import DictDataLoader


# Generated at 2022-06-13 09:32:09.065850
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    from ansible.playbook import Play
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.executor.playbook_executor import PlaybookExecutor

    ansible.constants._init_global_vars()

    def build_playbook(playbook):
        mgr = InventoryManager(loader=DataLoader())
        playbooks = [ playbook ]
        variable_manager = VariableManager(loader=DataLoader(), inventory=mgr)
        pbex = PlaybookExecutor(playbooks=playbooks, inventory=mgr, variable_manager=variable_manager, loader=DataLoader())
        return pbex


# Generated at 2022-06-13 09:32:16.695340
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    from ansible.playbook.play_context import PlayContext

    t = TaskInclude()
    t.load({'name': ''})
    t.vars = dict(a=1, b=2)
    t.args = dict(c=3, d=4)
    t.action = 'include'

    # when action is 'include', the result is a dict that merges the vars, args and the parent vars
    vars = t.get_vars()
    assert vars == dict(a=1, b=2, c=3, d=4)

    # while when action is not 'include', the result is a dict that merges the vars and the parent vars
    t.action = 'include_role'
    vars = t.get_vars()

# Generated at 2022-06-13 09:32:27.269543
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():
    # setup
    fake_play = dict()
    fake_play['vars'] = dict()
    fake_play['vars']['fake_play_var'] = "fake_play_value"

    fake_block = dict()
    fake_block['vars'] = dict()
    fake_block['vars']['fake_block_var'] = "fake_block_value"

    fake_task_include = dict()
    fake_task_include['vars'] = dict()
    fake_task_include['vars']['fake_task_include_var'] = "fake_task_include_value"
    fake_task_include['vars']['fake_play_var'] = "override"
    fake_task_include['vars']['fake_block_var'] = "override"

    #

# Generated at 2022-06-13 09:32:36.776055
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():

    from units.mock.loader import DictDataLoader
    from units.mock.path import mock_unfrackpath_noop
    from units.mock.vars import mock_get_vars
    from ansible.vars import VariableManager
    from ansible.playbook import Playbook
    from ansible.playbook.play_context import PlayContext

    def _validate(task, block_args, task_vars):
        '''
        Helper function to validate result of build_parent_block method
        '''
        # Build parent block using build_parent_block method
        p_block = task.build_parent_block()

        # Check that the parent block is a Block object
        assert isinstance(p_block, Block)

        # Check that the arguments used to build block have been removed from the task args

# Generated at 2022-06-13 09:32:51.556616
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    def _load_task_from_data(data, block=None):
        from ansible.playbook.play import Play
        from ansible.vars.manager import VariableManager
        from ansible.config.manager import ConfigManager
        from ansible.parsing.dataloader import DataLoader

        config_mgr = ConfigManager(
            defaults=dict(),
            env_vars={},
            parser=None
        )

        play_context = PlayContext()
        play_context._set_config_manager(config_mgr)

        loader = DataLoader()
        variable_manager = VariableManager()
        play = Play.load(
            data,
            variable_manager=variable_manager,
            loader=loader
        )


# Generated at 2022-06-13 09:32:56.889267
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.role_include import TaskIncludeRole
    from ansible.vars.manager import VariableManager
    from ansible.vars.hostvars import HostVars
    from ansible.vars.hostvars import HostVarsVars
    import ansible.constants as C
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.module_utils._text import to_bytes


    # Dummy task data

# Generated at 2022-06-13 09:33:10.827424
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.plugins.loader import action_loader

    class ActionModule(object):
        TRANSFERS_FILES = False

        def __init__(self, *args, **kwargs):
            pass

    action_loader.add('task_include_build_parent_block', ActionModule)

    # Create a Play, PlayContext and add TaskInclude under a Block
    host_name = "test_TaskInclude_build_parent_block"
    play_context = PlayContext(remote_addr=host_name)
    play_context.network_os = 'ios'

# Generated at 2022-06-13 09:33:19.897829
# Unit test for method build_parent_block of class TaskInclude
def test_TaskInclude_build_parent_block():
    test_block = []
    test_loader = None
    test_result = None
    test = TaskInclude()
    test.args = {}
    test._parent = None
    test._role = None
    test._variable_manager = None
    test._loader = None
    test.args['apply'] = {'block': test_block}
    test_result = test.build_parent_block()
    assert test_result.block == test_block
    test.args['apply'] = {}
    test_result = test.build_parent_block()
    assert test_result == test

# Generated at 2022-06-13 09:33:26.048197
# Unit test for method check_options of class TaskInclude
def test_TaskInclude_check_options():
    # create a task with only valid options
    ti = TaskInclude()
    data = dict(
        _raw_params='/etc/ansible/foobar',  # file will be converted to _raw_params in load_data
    )
    task = ti.check_options(
        ti.load_data(data, variable_manager=None, loader=None),
        data
    )

    # create a task with invalid options (two)
    data = dict(
        _raw_params='/etc/ansible/foobar',
        key_a='value_a',
        key_b='value_b',
    )
    with pytest.raises(AnsibleParserError):
        ti.check_options(
            ti.load_data(data, variable_manager=None, loader=None),
            data
        )

# Generated at 2022-06-13 09:33:36.585606
# Unit test for method get_vars of class TaskInclude
def test_TaskInclude_get_vars():  # pylint: disable=unused-argument
    from ansible.plugins.loader import action_loader
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    from ansible.inventory.host import Host
    from collections import namedtuple
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()

    # Mock task_vars
    task_vars = dict()
    # Mock play context
    play_context = dict()

    # Mock the task
    task = TaskInclude()
    task._role = None
    task.action = 'include'
    task.args['param1'] = 'value1'
    task.args['param2'] = 'value2'

    # Mock the play
    play = namedtuple('play', ['tasks'])