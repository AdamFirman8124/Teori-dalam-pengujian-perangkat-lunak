

# Generated at 2022-06-13 09:14:00.670058
# Unit test for method preprocess_data of class Task
def test_Task_preprocess_data():
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.block import Block
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.playbook.role_include import RoleInclude
    from ansible.template import Templar
    play = Play()
    play_context = PlayContext(play=play)
    templar = Templar(loader=None, variables={}, play_context=play_context)

    parent = RoleInclude()
    parent.vars = {'key1': 'val1'}
    parent.role = None
    parent._role = None
    parent.statically_loaded = True

    task = Task()
    task._parent = parent

# Generated at 2022-06-13 09:14:09.562325
# Unit test for method preprocess_data of class Task
def test_Task_preprocess_data():
    runner = unittest.TextTestRunner(resultclass=unittest.ResultNoDescription)
    test_case = unit_test.TestCase(unittest.TestCase, runner)
    ds = dict()
    ds['delegate_to'] = 'localhost'
    ds['action'] = 'setup'
    ds['key'] = 'value'
    task = Task()
    task.post_validate = MagicMock()
    task.get_validated_value = MagicMock(return_value='value')
    task._variable_manager = MagicMock()
    task._validate_attributes = MagicMock()
    task.post_validate = MagicMock()
    task._get_parent_attribute = MagicMock()
    new_ds = task.preprocess_data(ds)
    assert new

# Generated at 2022-06-13 09:14:18.955331
# Unit test for method get_vars of class Task
def test_Task_get_vars():
    '''
    Unit test for method get_vars of class Task
    '''

    # Init a Task object

# Generated at 2022-06-13 09:14:21.742490
# Unit test for method deserialize of class Task
def test_Task_deserialize():
    x = Task(loader=None, variable_manager=None, use_deprecated_imports=True)
    x.deserialize({})

# Generated at 2022-06-13 09:14:24.338333
# Unit test for method get_name of class Task
def test_Task_get_name():
    task = Task()
    task._attributes['name'] = "test_name"
    assert task.get_name() == "test_name"


# Generated at 2022-06-13 09:14:27.596209
# Unit test for method preprocess_data of class Task
def test_Task_preprocess_data():
    data = {'name': 'test', 'tags': 'test'}
    task_ds = Task(data=data, collection_list=[])
    
    assert task_ds.get_validated_value('tags') == ['test']


# Generated at 2022-06-13 09:14:31.358482
# Unit test for method __repr__ of class Task
def test_Task___repr__():
    # i = Task()
    # i.deserialize({'_uuid': '22d369c8-0e69-4c11-bddf-d6de5ed6ff5c', '__ansible_module__': 'setup', 'action': 'setup'})
    # assert repr(i) == "<Task: 'setup'>"
    pass

# Generated at 2022-06-13 09:14:38.658998
# Unit test for method get_include_params of class Task
def test_Task_get_include_params():
    host_manager = HostManager()
    loader = DataLoader()
    variable_manager = VariableManager()

    p = Play().load('test_play', loader=loader, variable_manager=variable_manager, loader_basedir='.', all_vars=dict(), all_tasks=dict())

    task = Task()
    task._attributes['vars'] = dict(a=1, c=3)

    task1 = Task()
    task1._attributes['vars'] = dict(a=2, d=4)

    task.load('test_task', loader=loader, play=p, variable_manager=variable_manager)
    task1.load('test_task1', loader=loader, parent=task, play=p, variable_manager=variable_manager)

# Generated at 2022-06-13 09:14:49.132401
# Unit test for method preprocess_data of class Task
def test_Task_preprocess_data():
    # Assert if file is not found
    #def test_file_not_found(self):
    test_task = Task()

    # test for preprocess_data for skip_missing action
    test_action_skip_missing_data = {'action': 'include_vars',
                                 'skip_missing': True}
    test_action_skip_missing_data_res = {'action': 'include_vars',
                                      'lookup_plugin': '',
                                      'args': {'skip_missing': True}}
    test_action_skip_missing_data_res_out = test_task.preprocess_data(test_action_skip_missing_data)
    assert test_action_skip_missing_data_res == test_action_skip_missing_data_res_out

    # test for preprocess_data for

# Generated at 2022-06-13 09:14:57.474308
# Unit test for method preprocess_data of class Task

# Generated at 2022-06-13 09:15:21.424086
# Unit test for method preprocess_data of class Task
def test_Task_preprocess_data():
    from ansible.playbook.block import Block
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.utils.display import Display
    import json
    import sys

    class Options(object):
        verbosity = 0
        listtags = False
        listtasks = False
        listhosts = False
        syntax = False
        connection = 'ssh'
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

# Generated at 2022-06-13 09:15:21.974145
# Unit test for method preprocess_data of class Task
def test_Task_preprocess_data():
    pass



# Generated at 2022-06-13 09:15:25.161757
# Unit test for method __repr__ of class Task
def test_Task___repr__():
    task = Task(
        action='test'
    )
    assert repr(task)  # TODO: We should check the output

# Generated at 2022-06-13 09:15:31.040825
# Unit test for method get_vars of class Task
def test_Task_get_vars():
    new_task = Task()
    print('Test 1')
    all_vars = new_task.get_vars()
    print(all_vars,type(all_vars))
    print('Test 2')
    all_vars = new_task.get_vars()
    print(all_vars,type(all_vars))
test_Task_get_vars()

# Generated at 2022-06-13 09:15:40.275261
# Unit test for method deserialize of class Task

# Generated at 2022-06-13 09:15:43.576237
# Unit test for method get_vars of class Task
def test_Task_get_vars():
    task = Task(None,dict(),loader = None)
    result = task.get_vars()
    assert  result == {}


# Generated at 2022-06-13 09:15:46.215806
# Unit test for method __repr__ of class Task
def test_Task___repr__():
    task = Task()
    repr_ = task.__repr__()
    assert repr_ == ""

# Generated at 2022-06-13 09:15:57.216989
# Unit test for method preprocess_data of class Task

# Generated at 2022-06-13 09:16:07.106721
# Unit test for method __repr__ of class Task
def test_Task___repr__():
  task = Task()
  task.name = 'name'
  task.action = 'action'
  task.args = 'args'
  task.delegate_to = 'delegate_to'
  task.always_run = True
  task.async_val = 100
  task.poll = 100
  task.tags = 'tags'
  task.transport = 'transport'
  task.until = 'until'
  task.retries = 'retries'
  task.first_available_file = 'first_available_file'
  task.vars = 'vars'
  task.run_once = True
  task.notify = 'notify'
  task.register = 'register'
  task.ignore_errors = True
  task.free_form = True
  task.no_log = True
 

# Generated at 2022-06-13 09:16:08.984942
# Unit test for method deserialize of class Task
def test_Task_deserialize():
    t = Task()
    t.deserialize([])


# Generated at 2022-06-13 09:16:28.113778
# Unit test for method get_first_parent_include of class Task
def test_Task_get_first_parent_include():
    # Create a role
    role_meta = {
        "name": "test-role",
        "collections": [{
            "name": "test-collection"
        }],
        "version": "1.0.0"
    }
    role = Role.load({
        "_role_meta": role_meta,
        "_search_paths": [
            "."
        ],
        "_collections": [
            "test-collection"
        ]
    })
    # Create a task
    task = Task()
    task.action = 'ansible.builtin.debug'
    task.args = {"msg": 'hello world'}
    task._role = role
    # Create a handler
    handler = Handler()
    handler.action = 'ansible.builtin.debug'

# Generated at 2022-06-13 09:16:41.533499
# Unit test for method deserialize of class Task
def test_Task_deserialize():
    # Sets up the context of the test
    # -- Set up mocks
    from ansible.playbook.role_include import RoleInclude
    
    r = RoleInclude()
    r.deserialize = MagicMock()
    m = {
        'data': {
            'some': 'data',
        },
        'parent': r,
    }
    
    # -- Set up fixture
    t = Task()
    
    # -- Run unit test
    t.deserialize(m['data'])
    
    # -- Check assertions
    assert t._attributes == {
        'some': 'data',
    }
    r.deserialize.assert_called_with(m['parent'])
    assert t._parent == r


# Generated at 2022-06-13 09:16:44.691409
# Unit test for method deserialize of class Task
def test_Task_deserialize():
    # Invalid inputs
    assert isinstance(None, Task)
    assert isinstance(0, Task)
    assert isinstance([], Task)
    assert isinstance({}, Task)
    assert isinstance(b'', Task)
    assert isinstance(u'', Task)

# Generated at 2022-06-13 09:16:48.493017
# Unit test for method __repr__ of class Task
def test_Task___repr__():
    task1 = Task()
    task1.name = 'task1'
    assert repr(task1) == '<Task name=task1>'



# Generated at 2022-06-13 09:16:58.487039
# Unit test for method get_include_params of class Task
def test_Task_get_include_params():
    yaml = """
    - action: include_tasks
      file: include_tasks.yml
      vars:
        foo: bar
    """
    data = yaml_loads(yaml)
    ds = prepare_for_serialization(data, play_context=PlayContext())
    t = Task.load(ds[0], play=None, variable_manager=None, loader=None)
    assert isinstance(t, Task)
    assert t.include_params == {'foo': 'bar'}


# Generated at 2022-06-13 09:17:09.409285
# Unit test for method serialize of class Task
def test_Task_serialize():
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.parsing.yaml.dumper import AnsibleDumper
    from ansible.plugins.loader import task_loader, lookup_loader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.block import Block
    task = Task()
    task._loader = task_loader
    task._variable_manager = VariableManager()
    task._inventory_manager = InventoryManager()
    task._play_context = PlayContext()
    task._task_vars = dict()
    task._nonpersistent_facts = dict()
    task._role

# Generated at 2022-06-13 09:17:10.433423
# Unit test for method deserialize of class Task
def test_Task_deserialize():
    data = {}
    Task().deserialize(data)
    assert data == {}


# Generated at 2022-06-13 09:17:22.005559
# Unit test for method deserialize of class Task
def test_Task_deserialize():
    t = Task()

# Generated at 2022-06-13 09:17:31.322042
# Unit test for method preprocess_data of class Task
def test_Task_preprocess_data():
    ds = dict()
    #
    # test case 1
    #

    #
    # test case 2
    #

    #
    # test case 3
    #

    #
    # test case 4
    #

    #
    # test case 5
    #

    #
    # test case 6
    #

    #
    # test case 7
    #

    #
    # test case 8
    #

    #
    # test case 9
    #

    #
    # test case 10
    #

    #
    # test case 11
    #

    #
    # test case 12
    #

    #
    # test case 13
    #

    #
    # test case 14
    #

    #
    # test case 15
    #

    #
    # test case 16
    #



# Generated at 2022-06-13 09:17:34.923585
# Unit test for method get_first_parent_include of class Task
def test_Task_get_first_parent_include():
    myTask = Task()
    myTask._parent = TaskInclude()
    assert hasattr(myTask, 'get_first_parent_include')
    assert myTask.get_first_parent_include() == myTask._parent


# Generated at 2022-06-13 09:18:26.594234
# Unit test for method preprocess_data of class Task
def test_Task_preprocess_data():
    task = Task()
    task._variable_manager = Mock()
    task._loader = Mock()
    task._loader.get_real_file.return_value = 'path.yml'
    task.when = 'a_when_value'
    task.tags = 'a_tags_value'
    task.action = 'a_action_value'
    task.local_action = 'a_local_action_value'
    task.args = 'a_args_value'
    task.delegate_to = 'a_delegate_to_value'
    task.environment = 'a_environment_value'
    task.register = 'a_register_value'
    task.run_once = 'a_run_once_value'
    task.ignore_errors = 'a_ignore_error_value'
    task.first_

# Generated at 2022-06-13 09:18:28.252280
# Unit test for method post_validate of class Task
def test_Task_post_validate():
    task = Task()
    task.post_validate('templar')


# Generated at 2022-06-13 09:18:32.944082
# Unit test for method __repr__ of class Task
def test_Task___repr__():
    task = Task()
    task.action = 'action'
    task.args = {}
    task.name = 'name'
    task.tags = ['tags']
    task.when = 'when'
    expected_result = "Task(action='action',name='name',args={},tags=['tags'],when='when')"
    result = task.__repr__()
    assert result == expected_result, result



# Generated at 2022-06-13 09:18:34.242648
# Unit test for method deserialize of class Task
def test_Task_deserialize():
    task = Task()
    task.deserialize({})

# Generated at 2022-06-13 09:18:46.461065
# Unit test for method preprocess_data of class Task
def test_Task_preprocess_data():
    def mock_getattr(self, name):
        if name == 'vars':
            return {'foo': 'bar'}
        return None

    class MockedTask(Task):
        _valid_attrs = {
            'any_key': Attribute(isa='dict', default={}),
        }

        def getattr(self, key):
            return getattr(self, key)

    task = MockedTask()
    task.role = None
    task.vars = {"test": "hello world"}
    # use a variable to mock __getattribute__
    task.__getattribute__ = MethodType(mock_getattr, task)

    # any_key defined in _valid_attrs

# Generated at 2022-06-13 09:18:54.053881
# Unit test for method deserialize of class Task

# Generated at 2022-06-13 09:19:03.678178
# Unit test for method deserialize of class Task
def test_Task_deserialize():
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.handler_task_include import HandlerTaskInclude

    parent_data = data.get('parent', None)
    if parent_data:
        parent_type = data.get('parent_type')
        if parent_type == 'Block':
            p = Block()
        elif parent_type == 'TaskInclude':
            p = TaskInclude()
        elif parent_type == 'HandlerTaskInclude':
            p = HandlerTaskInclude()
        p.deserialize(parent_data)
        self._parent = p
        del data['parent']

    role_data = data.get('role')
    if role_data:
        r = Role()
        r.deserialize(role_data)
        self._role = r

# Generated at 2022-06-13 09:19:14.472533
# Unit test for method serialize of class Task
def test_Task_serialize():
    task = Task()
    task.action = "action"
    task.changed_when = "changed_when"
    task.always_run = "always_run"
    task.async_val = "async_val"
    task.async_seconds = "async_seconds"
    task.first_available_file = "first_available_file"
    task.delay = "delay"
    task.environment = "environment"
    task.local_action = "local_action"
    task.notify = "notify"
    task.poll = "poll"
    task.retries = "retries"
    task.run_once = "run_once"
    task.until = "until"
    task.tags = "tags"
    task.when = "when"
    task.register = "register"


# Generated at 2022-06-13 09:19:27.749048
# Unit test for method get_include_params of class Task
def test_Task_get_include_params():
    task = Task()
    # test with empty task
    params = task.get_include_params()
    assert params == dict()
    # test with a task having include action
    task = Task()
    task.action = 'include'
    task.vars = dict(foo='bar')
    params = task.get_include_params()
    assert params == dict(foo='bar')
    # test with a task not having include action
    task = Task()
    task.action = 'notinclude'
    task.vars = dict(foo='bar')
    params = task.get_include_params()
    assert params == dict()
    # test with a task with parent
    task = Task()
    task.action = 'notinclude'
    task.vars = dict(foo='bar')
    # test with a task having include action

# Generated at 2022-06-13 09:19:32.691686
# Unit test for method __repr__ of class Task
def test_Task___repr__():
    '''
    Unit test for method __repr__ of class Task
    '''
    t = Task()

    # check for exception
    try:
        t.__repr__()
    except:
        raise AssertionError('Could not get repr of Task instance')

# Generated at 2022-06-13 09:19:54.785593
# Unit test for method deserialize of class Task
def test_Task_deserialize():
    import StringIO
    task = Task(loader=DictDataLoader({}))
    task.deserialize({'name': 'task name', 'tags': {'key': 'value'}, 'metadata': {'test_metakey': 'test_metavalue'}})
    assert task._attributes['name'] == 'task name'
    assert task._attributes['tags'] == {'key': 'value'}
    assert task._metadata['test_metakey'] == 'test_metavalue'


# Generated at 2022-06-13 09:20:05.149149
# Unit test for method __repr__ of class Task

# Generated at 2022-06-13 09:20:06.331847
# Unit test for method deserialize of class Task
def test_Task_deserialize():
    assert isinstance(Task().deserialize(""), Task)


# Generated at 2022-06-13 09:20:07.170651
# Unit test for method __repr__ of class Task
def test_Task___repr__():
  assert False, "No implemented"

# Generated at 2022-06-13 09:20:18.641455
# Unit test for method get_first_parent_include of class Task
def test_Task_get_first_parent_include():
    import ansible.playbook.task_include
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.task import Task

    # Task is the first recursion level
    task = Task()
    task_include = TaskInclude()
    task_include_2 = TaskInclude()

    task_include_2._parent = task_include
    task_include._parent = task

    assert task.get_first_parent_include() == task_include
    assert task_include.get_first_parent_include() == task_include
    assert task_include_2.get_first_parent_include() == task_include

    # Task is the second recursion level
    task_2 = Task()
    task_2._parent = task


# Generated at 2022-06-13 09:20:19.483024
# Unit test for method get_vars of class Task
def test_Task_get_vars():
    pass



# Generated at 2022-06-13 09:20:30.577050
# Unit test for method post_validate of class Task
def test_Task_post_validate():
    from ansible.template import Templar
    test_data = dict(
        name="test",
        environment={'test_key': '{{test_value}}'},
        action="shell",
        args=dict(foo="{{ bar }}", bar="test"),
        vars={'test_value': 'test_value'}
    )
    mocked_tmplar = mock.MagicMock(spec=Templar)
    mocked_tmplar.template = mock.MagicMock(return_value="test_value")
    mocked_tmplar.config = dict()
    t = Task()
    t.post_validate(mocked_tmplar)
    t._load_data(data=test_data)
    t.post_validate(mocked_tmplar)

# Generated at 2022-06-13 09:20:42.323744
# Unit test for method get_vars of class Task
def test_Task_get_vars():
    # test_Task_get_vars_1
    task_1 = Task()
    expected_1 = dict()
    actual_1 = task_1.get_vars()
    assert expected_1 == actual_1

    # test_Task_get_vars_2
    def _mock_get_vars():
        return dict(a=1, b=2)

    task_2 = Task()
    task_2.get_vars = _mock_get_vars
    expected_2 = dict(a=1, b=2)
    actual_2 = task_2.get_vars()
    assert expected_2 == actual_2

    # test_Task_get_vars_3
    def _mock_parent_get_vars():
        return dict(a=1, b=2)

# Generated at 2022-06-13 09:20:53.656060
# Unit test for method deserialize of class Task
def test_Task_deserialize():
    """
    Test that serialization/deserialization preserves the important parts of a Task object
    """
    # FIXME: this will fail if tests are run with options such as --diff
    display.verbosity = 0

    task = Task()
    task.action = 'ping'
    parent = Block()
    parent.block = ['ping']
    parent.rescue = ['ping']
    parent.always = ['ping']
    parent.any_errors_fatal = True
    parent.connection = 'ssh'
    parent.delegate_to = 'local'
    parent.ignore_errors = True
    parent.loop = '{{ host }}'
    parent.loop_control = {'loop_var': 'host', 'label': 'host'}
    parent.name = 'ping'
    parent.retries = 2

# Generated at 2022-06-13 09:21:04.290900
# Unit test for method deserialize of class Task
def test_Task_deserialize():
    task_obj = Task()
    assert isinstance(task_obj, Task) is True
    # deserialize call with data
    with pytest.raises(AnsibleParserError) as excinfo:
        task_obj.deserialize({})
    assert 'object has no attribute \'implicit\'' in str(excinfo.value)
    # Set value for object attribute role
    task_obj._role = False
    # Get value of object attribute role
    assert isinstance(task_obj._role, bool) is True
    # Set value for object attribute _parent
    task_obj._parent = False
    # Get value of object attribute _parent
    assert isinstance(task_obj._parent, bool) is True
    # deserialize call with data
    task_obj.deserialize({'implicit': True})
    # Get value

# Generated at 2022-06-13 09:21:29.550285
# Unit test for method deserialize of class Task
def test_Task_deserialize():
    
    # Initialize an instance of the Task class
    task = Task()
    parent_data = {}
    parent_type = "Block"
    role_data = {}
    data = {"parent": parent_data,
            "parent_type": parent_type,
            "role": role_data}
    
    # Call the deserialize method of class Task with the data
    task.deserialize(data)

    # Check if the correct parent is set
    assert task._parent is not None

    # Check if the role is correctly set
    assert task._role is not None

    # Check the value of implicit
    assert isinstance(task.implicit, bool)

    # Check the value of resolved_action
    assert isinstance(task.resolved_action, str)


# Generated at 2022-06-13 09:21:31.763598
# Unit test for method deserialize of class Task
def test_Task_deserialize():
    testcase = Task()
    assert testcase.deserialize({}) == None



# Generated at 2022-06-13 09:21:40.523454
# Unit test for method post_validate of class Task
def test_Task_post_validate():
    host = Mock()
    task = Task()
    task._play = Mock()
    task._play._play = Mock()
    task._play._play.host = host
    task._play._play.host.get_variable = Mock(return_value=None)
    task.get_vars = Mock(return_value=None)
    task.get_include_params = Mock(return_value=None)

    task.post_validate(None)

# Generated at 2022-06-13 09:21:49.199126
# Unit test for method deserialize of class Task
def test_Task_deserialize():
    import collections
    import ansible.playbook.task
    import ansible.playbook.block
    import ansible.playbook.handler
    import ansible.playbook.role
    import ansible.playbook.task_include
    import ansible.playbook.handler_task_include
    from ansible.playbook.task import Action, Task
    from ansible.playbook.block import Block
    from ansible.playbook.handler import Handler
    from ansible.playbook.role import Role
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.handler_task_include import HandlerTaskInclude

    task = Task()

    assert isinstance(task, collections.MutableMapping)
    assert isinstance(task, Task)

    # task.deserialize()

    #unit test

# Generated at 2022-06-13 09:21:54.316502
# Unit test for method deserialize of class Task
def test_Task_deserialize():
    task = Task()
    assert task.deserialize({"action": "test", "args": {"arg1": "test_arg1", "arg2": "test_arg2"}, "delegate_to": "test_delegate",
                             "name": "test_task", "parents": [{"action": "test_parent", "implicit": False}],
                             "parent_type": "TaskInclude", "role": {"action": "test_role", "implicit": False},
                             "task_type": "test_type", "vars": {"var1": "test_var1", "var2": "test_var2"}})

# Generated at 2022-06-13 09:21:58.493684
# Unit test for method post_validate of class Task
def test_Task_post_validate():
    t = Task()
    templar = Templar(loader=None, variables={})
    t.post_validate(templar=templar)

# Generated at 2022-06-13 09:22:01.224062
# Unit test for method __repr__ of class Task
def test_Task___repr__():
    from ansible.errors import AnsibleError
    from ansible.playbook.task import Task
    from ansible.utils.display import Display
    display = Display()

# Generated at 2022-06-13 09:22:03.984048
# Unit test for method deserialize of class Task
def test_Task_deserialize():
    test_instance = Task()
    test_instance.deserialize({})

# Generated at 2022-06-13 09:22:07.456121
# Unit test for method get_name of class Task
def test_Task_get_name():
    task = Task()
    task.name = 'test_task'
    assert task.get_name() == 'test_task'


# Generated at 2022-06-13 09:22:19.515452
# Unit test for method deserialize of class Task
def test_Task_deserialize():
    from ansible.playbook.handler_task_include import HandlerTaskInclude
    from ansible.playbook.task_include import TaskInclude
    t = Task()
    parent = TaskInclude()

# Generated at 2022-06-13 09:22:39.352214
# Unit test for method post_validate of class Task
def test_Task_post_validate():
    class AnsibleTemplar:
        def __init__(self):
            self.variable_manager = VariableManager()
    task_scheduled = Task()
    task_scheduled.task_action = 'setup'
    print("Passed: test_Task_post_validate")


# Generated at 2022-06-13 09:22:50.022303
# Unit test for method get_vars of class Task
def test_Task_get_vars():
    task = Task()
    task._parent = None
    task._loader = None
    task._variable_manager = None
    task._block = None
    task._role = None
    task._loop_eval_var = False
    task._delegate_to = None
    task._run_once = False
    task._loop = 'test_Task_get_vars.loop'
    task._ignore_errors = False
    task._always_run = True
    task._changed_when = None

    task.register_as_template_attribute("test_Task_get_vars_1.attr")

    task.implicit = True
    task.resolved_action = 'test_Task_get_vars_2.resolved_action'
    task.deprecated_vars = None
    task.deprecated_tags = None
   

# Generated at 2022-06-13 09:22:57.687835
# Unit test for method get_first_parent_include of class Task

# Generated at 2022-06-13 09:23:05.586039
# Unit test for method deserialize of class Task
def test_Task_deserialize():
    from ansible.playbook.block import Block
    from ansible.playbook.handler_task_include import HandlerTaskInclude
    from ansible.playbook.task_include import TaskInclude


    task = Task()
    task_data = {
        'action': 'setup',
        'loop': 'localhost',
        '__ansible_arguments__': [u'localhost'],
        '__ansible_version__': 2,
        'register': 'ansible_facts',
        'tags': ['always', 'module']
    }
    task.deserialize(task_data)
    assert task.action == 'setup'
    assert task.loop == 'localhost'
