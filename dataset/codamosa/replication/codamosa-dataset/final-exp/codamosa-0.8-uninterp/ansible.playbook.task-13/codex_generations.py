

# Generated at 2022-06-13 09:13:55.520484
# Unit test for method preprocess_data of class Task
def test_Task_preprocess_data():
    import ansible.parsing.yaml.loader
    test_obj = Task()
    test_obj.get_validated_value = lambda a, b, c, d: c
    test_obj.action = 'copy'
    test_obj._valid_attrs = {}
    test_obj._attribute_overrides = {}
    test_obj._loader = ansible.parsing.yaml.loader.AnsibleLoader(None, None, None)
    test_obj._final_common_args = dict()
    test_obj._valid_attrs = dict()
    test_obj._variable_manager = None
    test_obj._loader = None
    test_obj._Role__role_name = ''
    test_obj._Role__role_path = ''
    test_obj._Role__role_args = dict()


# Generated at 2022-06-13 09:14:06.191864
# Unit test for method deserialize of class Task
def test_Task_deserialize():
    t = Task()

    # Test with parent and role

# Generated at 2022-06-13 09:14:16.589111
# Unit test for method post_validate of class Task
def test_Task_post_validate():
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.role_include import IncludeRole
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject

    task_ds = AnsibleBaseYAMLObject()
    task_ds.action='test'
    task_ds.name='test task'
    variabled_manager = VariableManager()
    variabled_manager._fact_cache = {}
    variabled_manager._options_vars = {}
    variable_manager = variabled_manager
    loader = None
    task_include = TaskInclude()
    task_include.deserialize(task_ds)

# Generated at 2022-06-13 09:14:25.337152
# Unit test for method post_validate of class Task
def test_Task_post_validate():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    ds = {'action': {'test': 'asd'}}
    loader = DataLoader()
    variable_manager = VariableManager()
    task = Task()
    task.post_validate(ds, loader=loader, templar=AnsibleTemplar(loader=loader, shared_loader_obj=loader, variables=variable_manager))


# Generated at 2022-06-13 09:14:30.250845
# Unit test for method deserialize of class Task
def test_Task_deserialize():
    task = Task()
    task.deserialize({"action": "shell", "args": {"chdir": "/tmp"}})
    assert task.action == "shell"
    assert task.args["chdir"] == "/tmp"


# Generated at 2022-06-13 09:14:33.298957
# Unit test for method post_validate of class Task
def test_Task_post_validate():
    t = Task(ds=None)
    t.post_validate(templar=None)
    return True


# Generated at 2022-06-13 09:14:38.668835
# Unit test for method get_first_parent_include of class Task
def test_Task_get_first_parent_include():
  task = Task()
  assert task.get_first_parent_include() is None
  mock_parent = MagicMock()
  task._parent = mock_parent
  assert task.get_first_parent_include() is mock_parent
  assert task.get_first_parent_include() is mock_parent
  mock_parent.get_first_parent_include.return_value = mock_parent
  assert task.get_first_parent_include() is mock_parent
  mock_parent.get_first_parent_include.assert_called_once()


# Generated at 2022-06-13 09:14:39.635639
# Unit test for method deserialize of class Task
def test_Task_deserialize():
    t = Task()
    t.deserialize({})

# Generated at 2022-06-13 09:14:44.384829
# Unit test for method __repr__ of class Task
def test_Task___repr__():
    task = Task()
    task._attributes = dict()
    # task._attributes = dict({'tags': ['tag']})
    task.action = 'the_test'
    assert task.__repr__() == 'the_test'



# Generated at 2022-06-13 09:14:54.418116
# Unit test for method serialize of class Task
def test_Task_serialize():
    data = dict(
        action='test',
        args=dict(
            _raw_params='test',
            _uses_shell=True,
        ),
        delegate_to='localhost',
        environment=dict(
            TEST=True,
        ),
        run_once=True,
        ignore_errors=False,
        no_log=True,
        register='test',
        retries=3,
        until=False,
        vars=dict(
            a='test',
            b=False,
            c=True,
        ),
        when='test',
        changed_when=False,
        failed_when='test',
        tags=['test']
    )

    task = Task()
    task.deserialize(data)

    assert task.serialize() == data



# Generated at 2022-06-13 09:15:09.542705
# Unit test for method get_include_params of class Task
def test_Task_get_include_params():
    '''
    test_Task_get_include_params ansible.parsing.yaml.objects.Task
    '''
    assert True == isinstance(Task().get_include_params(), dict)


# Generated at 2022-06-13 09:15:21.332138
# Unit test for method post_validate of class Task

# Generated at 2022-06-13 09:15:26.501220
# Unit test for method preprocess_data of class Task
def test_Task_preprocess_data():
  import json
  from ansible.parsing.dataloader import DataLoader
  from ansible.vars.manager import VariableManager
  from ansible.inventory.manager import InventoryManager
  from ansible.playbook.play import Play
  from ansible.playbook.role import Role
  from ansible.playbook.task import Task
  def test_json(json_obj,pretty=False):
    if pretty:
        print(json.dumps(json_obj, sort_keys=True, indent=4, separators=(',', ': ')))
    else:
        print(json.dumps(json_obj))
  loader=DataLoader()
  inventory = InventoryManager(loader=loader, sources=['localhost,'])
  variable_manager = VariableManager(loader=loader, inventory=inventory)
  play_source =  dict

# Generated at 2022-06-13 09:15:36.975405
# Unit test for method deserialize of class Task
def test_Task_deserialize():
    data = {
        'block': False,
        'action': 'gather_facts',
        'args': {}}
    task = Task()
    task.deserialize(data)
    assert task.action == 'gather_facts', "Expected: %s \n Got: %s" % ("gather_facts", task.action)
    assert task.args == {}, "Expected: %s \n Got: %s" % ("{}", task.args)
    assert (isinstance(task._parent, ansible.playbook.task_include.TaskInclude) or task._parent == None), "Expected: %s \n Got: %s" % ("ansible.playbook.task_include.TaskInclude", type(task._parent))

# Generated at 2022-06-13 09:15:52.468644
# Unit test for method deserialize of class Task
def test_Task_deserialize():

    # Initialize required class attributes
    yaml_data = {'action': 'shell', '_ansible_parsed': True, 'ignore_errors': False, 'resolved_action': 'shell', 'always_run': False, 'args': {'_raw_params': 'ping 127.0.0.1'}, 'delegate_to': '', 'register': '', '_ansible_no_log': False, 'name': '', '_ansible_item_label': '', 'when': '', 'notify': [], 'async_val': '', '_ansible_verbosity': 0, 'run_once': True}

    # Initialize obj with yaml data
    obj  = Task(yaml_data)

    # Task attribute 'action' is read-only and cannot be deserialized
    expected_output = False

# Generated at 2022-06-13 09:15:56.753201
# Unit test for method get_vars of class Task
def test_Task_get_vars():
    '''
    Test function for method get_vars of class Task
    '''
    all_vars = {'op1': 0}
    # Test initialize
    fixture = Task('task', all_vars)

    # Test get_vars
    output = fixture.get_vars()
    assert output == all_vars


# Generated at 2022-06-13 09:15:58.705211
# Unit test for method post_validate of class Task
def test_Task_post_validate():
    #Since there is no test for this module, just checking for proper doc string
    assert True == True

# Generated at 2022-06-13 09:16:08.274563
# Unit test for method preprocess_data of class Task
def test_Task_preprocess_data():
    print("******* Task *********")
    test_play = {}
    test_play['vars'] = {}
    test_play['vars']['some_var'] = 'some_value'
    test_play['vars']['some_var2'] = 'some_value2'
    test_play['vars']['some_var3'] = 'some_value3'
    test_play['vars']['some_var4'] = 'some_value4'
    test_play['vars']['some_var5'] = 'some_value5'
    test_play['vars']['some_var6'] = 'some_value6'
    test_play['vars']['some_var7'] = 'some_value7'

# Generated at 2022-06-13 09:16:16.053526
# Unit test for method __repr__ of class Task
def test_Task___repr__():
    # in this case, the Subclassed Task will not use the parent class's __repr__ method
    # while the Subclassed Task itself has to implement its own __repr__ method
    # so actually we do not test Task.__repr__ method, instead of testing the TaskHelper method
    class SubclassedTaskHelper(TaskHelper):
        def __init__(self):
            super(SubclassedTaskHelper, self).__init__()
    
    class SubclassedTask(Task):
        def __init__(self):
            super(SubclassedTask, self).__init__()
            self.task_helper = SubclassedTaskHelper()
    
    task = SubclassedTask()
    assert 'TaskHelper' in task.__repr__()


# Generated at 2022-06-13 09:16:19.899899
# Unit test for method deserialize of class Task
def test_Task_deserialize():
    class AnsibleReturn(object):
        def __init__(self, *args, **kwargs):
            self.args = args
    ansible_return = AnsibleReturn(*[1, 2, 3], **dict(a=1, b=2))
    obj = Task()
    obj.deserialize(ansible_return)
    assert isinstance(ansible_return, AnsibleReturn)

# Generated at 2022-06-13 09:16:34.063345
# Unit test for method get_name of class Task
def test_Task_get_name():
    task = Task()
    task._attributes['name'] = 'name'
    task._task_name = 'task_name'
    assert task.get_name() == 'task_name'

# Generated at 2022-06-13 09:16:45.219867
# Unit test for method deserialize of class Task
def test_Task_deserialize():
  '''
  Unit test for method deserialize of class Task
  '''

  t = Task()

# Generated at 2022-06-13 09:16:49.921044
# Unit test for method get_name of class Task
def test_Task_get_name():
    task = Task()
    task._attributes["name"] = "a"
    # Call method
    result = task.get_name()
    # assert result
    assert result == "a"


# Generated at 2022-06-13 09:17:00.803207
# Unit test for method __repr__ of class Task
def test_Task___repr__():
    task1 = Task()
    task1.action = 'shell'
    task1.args = {'free_form': '/usr/bin/example'}
    task1.name = 'Example Task'
    assert repr(task1) == '<Task name=Example Task action=shell free_form=/usr/bin/example>'

    task2 = Task()
    task2.action = 'yum'
    task2.args = {'name': 'vim'}
    task2.name = 'Install vim'
    assert repr(task2) == '<Task name=Install vim action=yum name=vim>'


# Generated at 2022-06-13 09:17:02.109764
# Unit test for method __repr__ of class Task
def test_Task___repr__():

    task = Task()
    task._attributes['name'] = 'test_name'
    assert task.__repr__() == "<Task name='test_name'>"



# Generated at 2022-06-13 09:17:06.373527
# Unit test for method post_validate of class Task
def test_Task_post_validate():
    Task(play=dict(), loader=dict(), variable_manager=dict(),
         task_vars=dict(), _role=dict(), shared_loader_obj=dict())
    pass

# Generated at 2022-06-13 09:17:19.757241
# Unit test for method get_include_params of class Task
def test_Task_get_include_params():
    from ansible.playbook.connection import Connection
    from ansible.utils.vars import combine_vars
    from ansible.template import Templar
    from ansible.parsing.yaml.objects import AnsibleUnicode, AnsibleSequence

    class Role(object):
        def serialize(self):
            return dict()

    class Block(object):
        def serialize(self):
            return dict()

    class MyTest(object):
        # task = Task()
        # task._variable_manager = dict()
        # task._loader = dict()
        task = Task()
        task._parent = None
        task._insert_parent = Block()
        task.role = Role()
        task.implicit = False
        task.resolved_action = None
        task.action = "action"

# Generated at 2022-06-13 09:17:30.108682
# Unit test for method post_validate of class Task

# Generated at 2022-06-13 09:17:40.031813
# Unit test for method deserialize of class Task
def test_Task_deserialize():
    task = Task()
    task.deserialize({"action": {}, "any_errors_fatal": False, "changed_when": False, "connection": "local", "delegate_to": {}, "delay": 0, "failed_when": False, "ignore_errors": False, "loop": "", "loop_control": {}, "name": "", "notify": {}, "register": "", "retries": 0, "until": False, "vars": {}})
    assert {} == task.action
    assert task.any_errors_fatal == False
    assert task.changed_when == False
    assert task.connection == "local"
    assert {} == task.delegate_to
    assert task.delay == 0
    assert task.failed_when == False
    assert task.ignore_errors == False

# Generated at 2022-06-13 09:17:41.646930
# Unit test for method preprocess_data of class Task
def test_Task_preprocess_data():
    task = Task()
    task.preprocess_data()

# Generated at 2022-06-13 09:18:04.892321
# Unit test for method deserialize of class Task
def test_Task_deserialize():
    # Make sure we are working with original classes and functions
    save_task_actions = copy.deepcopy(Task._task_actions)
    save_action_write_locks = copy.deepcopy(Task._action_write_locks)
    save_action_loader = copy.deepcopy(Task._action_loader)
    save_action_loader_fact_cache = copy.deepcopy(Task._action_loader_fact_cache)

    # Initialize some test data
    block_hierarchy = []
    task_no_block_hierarchy = []
    role_paths = []

    # Change globals for unit test
    Task._task_actions = dict()
    Task._action_write_locks = dict()
    Task._action_loader = None
    Task._action_loader_fact_cache = None

    # Initialize Task class members

# Generated at 2022-06-13 09:18:11.175997
# Unit test for method get_first_parent_include of class Task
def test_Task_get_first_parent_include():
    print("running ")
    play = Play.load(dict(
        name="test play",
        hosts="localhost",
        gather_facts=False,
        tasks=[
        dict(name="hostname task",
            action="hostname"
        ),
        dict(include="main",
            static=True
        )
        ],
        handlers=[dict(
            include="list"
        )]
    )
        )
    play.load()
    task = play.get_tasks()[0]
    task.all_parents_static()


# Generated at 2022-06-13 09:18:18.449025
# Unit test for method deserialize of class Task
def test_Task_deserialize():
    t = Task()
    assert t.deserialize({
  "action": "dummy",
  "delegate_to": "localhost",
  "register": "test",
    })
    assert hasattr(t, '_attributes')
    assert hasattr(t, '_loader')
    assert hasattr(t, '_role')
    assert hasattr(t, '_parent')
    assert hasattr(t, '_task_deps')
    assert hasattr(t, '_blocks')
    assert hasattr(t, '_always_run')
    assert hasattr(t, '_loop')
    assert hasattr(t, '_delegate_to')
    assert hasattr(t, '_environment')
    assert hasattr(t, '_no_log')

# Generated at 2022-06-13 09:18:22.472719
# Unit test for method preprocess_data of class Task
def test_Task_preprocess_data():
    task = {'action': {'module': 'shell', 'args': 'ls'}}
    t = Task()
    t._load_name(task)



# Generated at 2022-06-13 09:18:31.919621
# Unit test for method get_include_params of class Task
def test_Task_get_include_params():
  import os
  import sys
  import unittest

  test_dir = os.path.dirname(os.path.realpath(__file__))

  ansible_dir = os.path.realpath(os.path.join(test_dir, '../../'))
  collections_dir = os.path.realpath(os.path.join(test_dir, '../../../../'))

  sys.path.insert(0, ansible_dir)

  from ansible.module_utils.common.text.converters import to_text
  from ansible.module_utils.six import PY3
  from ansible.module_utils.six.moves import builtins
  from ansible.module_utils._text import to_bytes
  from ansible.vars import VariableManager


# Generated at 2022-06-13 09:18:33.815444
# Unit test for method deserialize of class Task
def test_Task_deserialize():
    Task_instance = Task()

    Task_instance.deserialize(data)



# <<INCLUDE_CALLS>>

# <<TEST_CALLS>>

# Generated at 2022-06-13 09:18:46.115574
# Unit test for method deserialize of class Task
def test_Task_deserialize():
    # test `deserialize` method of `Task` class
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.handler_task_include import HandlerTaskInclude
    from ansible.playbook.role_include import RoleInclude
    from ansible.playbook.block import Block
    from ansible.playbook.role_block import BlockRole

    # instantiating object
    task = Task()

    # deserializing

# Generated at 2022-06-13 09:18:46.742568
# Unit test for method post_validate of class Task
def test_Task_post_validate():
    pass

# Generated at 2022-06-13 09:18:57.663172
# Unit test for method get_vars of class Task
def test_Task_get_vars():
    '''
    [ansible-project] AnsibleTower-project-6247 :: Add test case for method get_vars of class Task 
    '''
    from collections import namedtuple
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.module_utils.six import PY3
    from io import StringIO, BytesIO
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    import ansible.constants as C
    import ansible.utils.vars as ans_vars
    import ansible.parsing.yaml.objects
    import pytest

    # This is used to setup the fake environment
    Inventory = namedtuple('Inventory', ['basedir'])

# Generated at 2022-06-13 09:19:07.198045
# Unit test for method get_include_params of class Task
def test_Task_get_include_params():
    from ansible.playbook.task_include import TaskInclude
    t = Task()
    t.vars = {'var1': 'value1'}
    t2 = TaskInclude()
    t2.vars = {'var2': 'value2'}
    t2.action = 'include'
    t.add_parent(t2)
    t3 = TaskInclude()
    t3.vars = {'var3': 'value3'}
    t3.action = 'include'
    t2.add_parent(t3)
    assert t.get_include_params() == {'var1': 'value1', 'var2': 'value2', 'var3': 'value3'}
    t.action = 'include'

# Generated at 2022-06-13 09:19:19.679515
# Unit test for method preprocess_data of class Task
def test_Task_preprocess_data():
    # https://github.com/ansible/ansible/blob/devel/test/units/playbook/test_playbook.py#L1452
    assert False



# Generated at 2022-06-13 09:19:27.861490
# Unit test for method preprocess_data of class Task
def test_Task_preprocess_data():
    # pass
    # actions: [identity]
    # args: {u'one': "1", u'two': 2}
    # delegate_to: ''
    # vars: {u'var1': 'foo'}
    t = Task()
    t.preprocess_data({'action': 'identity', 'args': {'one': "1", 'two': 2}, 'delegate_to': '', 'vars': {'var1': 'foo'}})
    assert (t.action == 'identity')
    assert (t.args == {'one': "1", 'two': 2})
    assert (t.delegate_to == '')
    assert (t.vars == {'var1': 'foo'})
    # actions: [identity]
    # args: {u'one': "1",

# Generated at 2022-06-13 09:19:28.623878
# Unit test for method preprocess_data of class Task
def test_Task_preprocess_data():
    pass

# Generated at 2022-06-13 09:19:40.579532
# Unit test for method preprocess_data of class Task
def test_Task_preprocess_data():
    c1 = dict(
        action=dict(),
        when=dict(),
        async_val=dict(),
        async_seconds=dict(),
        environment=dict(),
        poll=dict(),
        register=dict(),
        until=dict(),
        retries=dict()
    )
    task = Task()
    task.add_field(['action'], task.resolve_field, c1)
    task.add_field(['when'], task.resolve_field, c1)
    task.add_field(['async_val'], task.resolve_field, c1)
    task.add_field(['async_seconds'], task.resolve_field, c1)
    task.add_field(['environment'], task.resolve_field, c1)

# Generated at 2022-06-13 09:19:45.181527
# Unit test for method preprocess_data of class Task
def test_Task_preprocess_data():
    my_task = Task()
    my_dict = {'name':'vars', 'vars':[{'name':'test'}]}
    my_task.preprocess_data(my_dict)

if __name__ == '__main__':
    test_Task_preprocess_data()

# Generated at 2022-06-13 09:19:51.012097
# Unit test for method deserialize of class Task
def test_Task_deserialize():
    data = dict(
        action='setup',
        args={'filter': 'ansible_virtualization_type'},
        delegate_to='localhost',
        loop='setup_ansible_facts',
        name='Gather Facts'
    )

    task = Task()
    # testing a valid output
    assert isinstance(task.deserialize(data), Task)


# Generated at 2022-06-13 09:20:00.776346
# Unit test for method preprocess_data of class Task
def test_Task_preprocess_data():
    import tempfile
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.vars.manager import VariableManager
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText
    from ansible.errors import AnsibleParserError
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.playbook.playbook_context import PlaybookContext
    from ansible.playbook.block import Block
    from ansible.playbook.handler import Handler
    from ansible.template import Templar
    from ansible.parsing.yaml.objects import AnsibleSequence
    from ansible.utils.vars import combine_vars
    from ansible.plugins import action

# Generated at 2022-06-13 09:20:15.187078
# Unit test for method preprocess_data of class Task
def test_Task_preprocess_data():
    t = Task()
    t._load_vars = mock.Mock()
    t._validate_loop_with_items = mock.Mock()
    t.post_validate = mock.Mock()
    t.action = None
    t._role = False
    t._ancestor_play = None
    t.args = None
    t.delegate_to = None
    t._parent = None
    t.implicit = None
    t.resolved_action = None
    t.vars = None
    t._variable_manager = 'variable_manager'

# Generated at 2022-06-13 09:20:27.181424
# Unit test for method post_validate of class Task
def test_Task_post_validate():
    args = dict(
        action='action',
        args='args',
        delegate_to='delegate_to',
        changed_when='changed_when',
        environment='environment',
        failed_when='failed_when',
        loop='loop',
        loop_control='loop_control',
        #name='name',
        ignore_errors='ignore_errors',
        until='until',
        pause_before='pause_before',
        register='register',
        retries='retries',
        run_once='run_once',
        tags='tags',
        timeout='timeout',
        try_loops='try_loops',
        vars='vars',
        when='when',
        with_=dict(str_dict=dict(str_str='str_str'))
    )

# Generated at 2022-06-13 09:20:34.586312
# Unit test for method preprocess_data of class Task

# Generated at 2022-06-13 09:20:51.689351
# Unit test for method __repr__ of class Task
def test_Task___repr__():
    task = Task({})
    ret = task.__repr__()
    assert type(ret) is str
    assert ret == "<Task tasks/name=None (not imported)>"


# Generated at 2022-06-13 09:20:54.158175
# Unit test for method deserialize of class Task
def test_Task_deserialize():
    task1 = Task()
    task2 = Task()
    task2.deserialize({'name': 'task1'})
    assert task1 is not task2
    assert not task1.get_name() and task2.get_name() == 'task1'

# Generated at 2022-06-13 09:20:58.170930
# Unit test for method get_name of class Task
def test_Task_get_name():
    ds = {}
    task = Task()
    task.load(ds, {}, {})
    assert task.get_name() == 'meta'



# Generated at 2022-06-13 09:21:02.281205
# Unit test for method deserialize of class Task
def test_Task_deserialize():
    # get_attr__ returns the '_attr' value of a Task instance
    #
    # AssertionError: '_attr' is not present
    t = Task()
    assert (t.deserialize(dict(a=1))._get_parent_attribute("a") == 1)


# Generated at 2022-06-13 09:21:12.578875
# Unit test for method deserialize of class Task

# Generated at 2022-06-13 09:21:24.141327
# Unit test for method get_first_parent_include of class Task
def test_Task_get_first_parent_include():
    #task_obj1 = Task(play=play_obj)
    #task_obj2 = Task(play=play_obj)
    #task_obj1.include_tasks(task_obj2)
    #task_obj3 = Task(play=play_obj)
    #task_obj1.include_tasks(task_obj3)
    pass
Task.test_Task_get_first_parent_include = test_Task_get_first_parent_include


# Generated at 2022-06-13 09:21:38.659242
# Unit test for method deserialize of class Task

# Generated at 2022-06-13 09:21:42.652072
# Unit test for method get_vars of class Task
def test_Task_get_vars():
    # In actual implementation, Ansible-based class objects are constructed
    # in the runtime, by loading yaml files with Ansible's own yaml serializer.
    # This test case is just a brief demo of the result.
    # Note that the actual implementation may have different results.
    task = Task()
    task.vars = {'name': 'jack'}
    result = task.get_vars()
    assert result == {'name': 'jack'}

# Generated at 2022-06-13 09:21:51.577971
# Unit test for method __repr__ of class Task
def test_Task___repr__():
    obj = Task()
    repr = repr(obj)
    repr = repr.strip()
    assert repr.startswith('%s(' % obj.__class__.__name__)
    assert repr.endswith(')')
    # Ensure repr() can be successfully executed
    # assert eval(repr) == obj
    try:
        eval(repr)
    except Exception as e:
        logger.exception('repr(%s) raised exception: %s', obj, e)
        assert False


# Generated at 2022-06-13 09:22:01.869819
# Unit test for method get_vars of class Task
def test_Task_get_vars():

    task = Task(block=dict(tasks=dict(vars=dict(test=1))),
                delegate_to='localhost')

    result = task.get_vars()
    assert result == {}

    task = Task(block=dict(tasks=dict(vars=dict(test=1))),
                vars=dict(test=0), delegate_to='localhost')

    result = task.get_vars()
    assert result == {'test': 0}

    task2 = Task(block=dict(tasks=dict(vars=dict(test=1))),
                 vars=dict(test=0), delegate_to='localhost')
    task2._parent = task

    result = task2.get_vars()
    assert result == {'test': 0}


# Generated at 2022-06-13 09:22:20.914777
# Unit test for method get_include_params of class Task
def test_Task_get_include_params():
    loader = DictDataLoader({
        'test_playbook.yaml': '''
        ---
        - hosts: localhost
          tasks:
            - include_tasks: test_include.yaml
              vars:
                var1: yes
              tags: tag1
              delegate_to: localhost
        ''',
        'test_include.yaml': '''
        ---
        - name: test include task 1
          ping:
        - name: test include task 2
          ping:
        '''
    })
    inv_data = InventoryData(loader=loader, variable_manager=VariableManager())
    tqm = TaskQueueManager()
    pb = Playbook.load(loader.path_dwim('test_playbook.yaml'), variable_manager=VariableManager(), loader=loader)
    pb._t

# Generated at 2022-06-13 09:22:35.579968
# Unit test for method __repr__ of class Task
def test_Task___repr__():
    """
    When task.__repr__() is called
    If Task has a name
    Then it should return the name
    """
    task = Task()
    task.name = 'do this task'
    assert 'do this task' == task.__repr__()

    """
    When task.__repr__() is called
    Else If the action is a string
    Then it should return the action
    """
    task = Task()
    task.action = 'do that task'
    assert 'do that task' == task.__repr__()

    """
    When task.__repr__() is called
    Else If the action is a module name
    Then it should return the module name
    """
    task = Task()
    task.action = 'command'
    assert 'command' == task.__repr__()

# Generated at 2022-06-13 09:22:42.203435
# Unit test for method deserialize of class Task
def test_Task_deserialize():
    fake_loader_obj = FakeLoader()
    t = Task()

# Generated at 2022-06-13 09:22:43.408630
# Unit test for method deserialize of class Task
def test_Task_deserialize():
    pass


# Generated at 2022-06-13 09:22:52.443371
# Unit test for method get_include_params of class Task
def test_Task_get_include_params():
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.handler import Handler
    from ansible.playbook.block import Block
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.role_include import RoleInclude
    from ansible.playbook.role import Role
    from ansible.playbook.handler_task_include import HandlerTaskInclude

    # Case 1
    # Test implicit variable inside the task
    # create Task
    t = Task()
    # create variables
    t.vars = {"foo": "bar"}
    # expect
    assert t.get_include_params() == {}

    # Case 2
    # Test implicit variable inside the handler
    # create Task
    t = Task()
    # create Handler
    h = Handler()
   

# Generated at 2022-06-13 09:22:53.338460
# Unit test for method __repr__ of class Task
def test_Task___repr__():
    assert Task.__repr__



# Generated at 2022-06-13 09:22:56.690056
# Unit test for method deserialize of class Task
def test_Task_deserialize():
    task = Task()
    task.deserialize(dict(action="setup", register="myhost"))

    assert task.action == "setup"
    assert task.register == "myhost"

    assert task.has_task_include() == False
    assert task.get_include_params() == {}
    assert task.role is None

# Generated at 2022-06-13 09:22:58.560819
# Unit test for method __repr__ of class Task
def test_Task___repr__():
    # setUp
    task = Task()
    task._attributes = wrap_dict_with_AttrDict({'name': 'test'})

    # assert
    assert task.__repr__() == 'TASK "test"'


# Generated at 2022-06-13 09:23:06.173537
# Unit test for method post_validate of class Task
def test_Task_post_validate():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    # Setup arguments and create new Task instance to call post_validate on
    task_ds = dict(
        loop=None,
        when=None,
        tags=None,
        register=None,
        ignore_errors=None,
        delegate_to=None,
        run_once=None,
        local_action=None,
        environment=None,
        action=None,
        args=None,
        _preprocessed_vars=None,
        vars=None,
        _role=None,
        _has_vars=False,
        _has_include_vars=False,
        _has_block=False
    )
    loader = DataLoader()
    variable_manager