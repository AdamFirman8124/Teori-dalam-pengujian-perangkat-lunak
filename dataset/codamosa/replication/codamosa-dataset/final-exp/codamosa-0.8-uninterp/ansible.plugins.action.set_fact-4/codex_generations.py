

# Generated at 2022-06-13 10:42:21.878809
# Unit test for constructor of class ActionModule
def test_ActionModule():
    class MockModule(object):
        def __init__(self):
            self.params = dict(
                cacheable=False,
                x=1,
                y=2
            )

    def get_task_vars(x):
        return dict()
    def templar(x):
        return x

    import ansible.plugins.action.set_fact
    a = ansible.plugins.action.set_fact.ActionModule(MockModule(), '', templar, '/tmp/', get_task_vars)
    assert a

# Generated at 2022-06-13 10:42:30.842279
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.parsing.dataloader import DataLoader

    from ansible.playbook.task import Task
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    from ansible.utils.vars import AnsibleVars

    from ansible.executor.task_queue_manager import TaskQueueManager

    loader = DataLoader()
    options = AnsibleVars(
        connection='local',
        module_path='/path/to/mymodules',
        forks=10,
        become=None,
        become_method=None,
        become_user=None,
        check=False,
        diff=False,
        timeout=10,
        remote_user='root',
        private_key_file='keys/mykey',
    )


# Generated at 2022-06-13 10:42:36.040412
# Unit test for constructor of class ActionModule
def test_ActionModule():
    instantiate_action = ActionModule(None, {}, {}, False, None, 'set_fact')
    assert instantiate_action is not None, 'Can instantiate ActionModule class'
    assert isinstance(instantiate_action, ActionModule), 'Can instantiate ActionModule class'

# Generated at 2022-06-13 10:42:46.215632
# Unit test for method run of class ActionModule
def test_ActionModule_run():
	# initialize
	am = ActionModule()

	# argument 'args' contain the key/value pairs, which are stored into facts
	# if args is empty, raise AnsibleActionFail, otherwise store the facts
	def _run(am, tmp, task_vars, args, cacheable):
		am._task = Object()
		am._task.args = args
		am._task.args['cacheable'] = cacheable
		am._templar = FakeTemplar()
		return am.run(tmp, task_vars)

	# test for empty args, error
	res = _run(am, None, None, {}, False)
	assert res['failed'] == True
	
	# test for non empty args, when name is a valid identifier, store facts

# Generated at 2022-06-13 10:42:55.381111
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    task_vars = {}
    module_args = { 'cacheable': False }
    argument_spec = {'cacheable': dict(type='bool', required=False)}
    tmp = None
    connection = None
    module_name = ''
    module = None
    task_path = ''
    wrap_async = None

    # test first place where raise is present
    for k in ['1','False','True','d','dd','$','@','_','_F','_False','_d','_dd','_$$','_@','_@d','_@dd','_1','_1d','_1dd','123','123d','123dd','123$','123$$','123$d','123@','123@d','123^','123^d','123^dd']:
        module_args.update({k:123})
        a

# Generated at 2022-06-13 10:43:06.570944
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    actionModule = ActionModule(
        task=dict(),
        connection=dict(),
        play_context=dict(),
        loader=dict(),
        templar=dict(),
        shared_loader_obj=dict(),
    )
    # create an example actionModule._task.args dictionary
    actionModule._task.args = {
        u'namespace_prefix': u'foo',
        u'testvar': True,
    }

    # create an empty actionModule._task.vars dictionary
    actionModule._task.vars = dict()

    facts = actionModule.run()

# Generated at 2022-06-13 10:43:13.830062
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # define test input
    sample_task_vars = { 'ansible_facts': { 'ansible_distribution': 'CentOS' } }
    sample_args = { 'cacheable': 'no', 'test_key_1': 'test_value_1', 'test_key_2': 'test_value_2' }
    # define and build a test ActionModule instance
    expected_result = { 'ansible_facts': { 'test_key_1': 'test_value_1', 'test_key_2': 'test_value_2',
                                           'ansible_distribution': 'CentOS' },
                        '_ansible_facts_cacheable': False }
    am = ActionModule(None, sample_args, None, None)
    # execute the method under test and verify results

# Generated at 2022-06-13 10:43:15.094857
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """
    This function tests the constructor
    """
    # Create an instance of the class
    action = ActionModule()
    assert action._shared_loader_obj is not None

# Generated at 2022-06-13 10:43:15.982159
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert hasattr(ActionModule, 'run')

# Generated at 2022-06-13 10:43:16.884950
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert isinstance(ActionModule(), ActionModule)

# Generated at 2022-06-13 10:43:22.342283
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule is not None

# Generated at 2022-06-13 10:43:30.130939
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    am = ActionModule(None, None)
    am._task = type('Task', (object,), {})
    am._task.args = {
        'k1': 'v1',
        'k2': 'v2',
    }

    am._templar = type('Templar', (object,), {})
    am._templar.template = lambda x: x

    expected_result = {
        'ansible_facts': {
            'k1': 'v1',
            'k2': 'v2',
        },
        '_ansible_facts_cacheable': False,
    }

    assert expected_result == am.run()

# Generated at 2022-06-13 10:43:36.613014
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import tempfile
    with tempfile.TemporaryDirectory() as tmp:
        # Prepare the test data
        data = {'ansible_facts': {'legacy': True}}
        # Prepare the test ActionModule instance
        a = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
        # Run the test
        a.run(tmp, data)

# Generated at 2022-06-13 10:43:38.774062
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert True

# Generated at 2022-06-13 10:43:42.977842
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ar = ActionModule(dict(name='add_host',ds='hosts'),dict(hosts=dict(hostname='localhost',sip='1.2.3.4')))
    ar.run()
    print(ar)

# Generated at 2022-06-13 10:43:53.007428
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import sys
    from ansible.module_utils.urls import open_url
    from ansible.module_utils._text import to_bytes

    try:
        from __main__ import display
    except ImportError:
        from ansible.utils.display import Display
        display = Display()

    # Make sure that the display object is available
    display.verbosity = 3

    # Create a dummy task object to be used in this test
    task = CustomTask()

    # Create a new ActionModule object to be used in this test
    my_am = ActionModule(task, connection=None, play_context=PlayContext())

    # Test with no argument
    my_am.run()

# Generated at 2022-06-13 10:43:55.936286
# Unit test for constructor of class ActionModule
def test_ActionModule():
    pm = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert pm is not None

# Generated at 2022-06-13 10:43:56.695078
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    raise NotImplementedError

# Generated at 2022-06-13 10:44:09.650630
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # create instance of ActionModule
    action_module = ActionModule()

    # create needed stubs
    action_module._task_vars = dict()
    class ActionModule_Task:
        def __init__(self):
            self.args = dict()
    action_module._task = ActionModule_Task()

    # Set to False, ActionModule.run() should set True for cacheable
    action_module._task.args['cacheable'] = False

    # Call method
    ret = action_module._run()

    # Check that the method returned 'ansible_facts' and a key 'cacheable'
    assert 'ansible_facts' in ret
    assert '_ansible_facts_cacheable' in ret

    # Check that the method returned '_ansible_facts_cacheable' with value True

# Generated at 2022-06-13 10:44:16.395967
# Unit test for method run of class ActionModule
def test_ActionModule_run():
  from ansible.runner.return_data import ReturnData
  from ansible.playbook.task import Task
  from ansible.playbook.task_include import TaskInclude
  from ansible.playbook.block import Block
  from ansible.playbook import Play
  import ansible.constants as C

  action_module = ActionModule(task = Task(), connection = None, play_context = None, loader = None, templar = None, shared_loader_obj = None)

  #test that raises exception if no key/value pairs provided
  with pytest.raises(AnsibleActionFail):
    action_module.run()

  # test for non cacheable
  task1 = Task()
  task1._role = None
  task1._block = Block()

# Generated at 2022-06-13 10:44:29.368411
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import ansible.constants as C

    try:
        from __main__ import display
    except ImportError:
        from ansible.utils.display import Display
        display = Display()

    display.verbosity = 3

    import ansible.plugins.action.set_fact
    import ansible.playbook.task
    import ansible.module_utils.parsing.convert_bool


    play_context = ansible.playbook.play_context.PlayContext()
    play_context._timeout = 10
    play_context._shell = '/bin/sh -c'
    play_context._raw_shell = False
    play_context._shell_executable = '/bin/sh'
    play_context._shell_args = None
    play_context.become = True
    play_context.become_method = 'sudo'

# Generated at 2022-06-13 10:44:35.921234
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # We need to create a mock task here, later we can replace this with a real task
    mock_task = type('MockTask', (), { 'args' : { 'cacheable' : True, 'b': 'c', 'd': 'e'}})
    test = ActionModule(mock_task, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert test.TRANSFERS_FILES is False
    assert test._task.args['b'] == 'c'
    assert test._task.args['d'] == 'e'
    assert test._task.args['cacheable'] is True

# Generated at 2022-06-13 10:44:39.857406
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Create the module object with test arguments.
    test_args = dict()
    test_args['cacheable'] = 'True'
    test_args['testvar1'] = 'val1'
    test_args['testvar2'] = 'val2'
    module = ActionModule(test_args)
    # Assert that the module object is created properly.
    assert module

# Generated at 2022-06-13 10:44:53.801730
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # get a list of all of the classes in the module
    classes = [cls for name, cls in list(iteritems(locals())) if isinstance(cls, type) and name != 'ActionModule']
    # get a list of what type they are
    types = [cls.__name__ for name, cls in list(iteritems(locals())) if isinstance(cls, type) and name != 'ActionModule']
    # now build a dictionary out of this so we can look them up
    types_dict = dict(zip(classes, types))

    #import cStringIO as StringIO
    #import StringIO as StringIO
    from io import StringIO

    # now we want to create a fake environment and test the constructor
    # of ActionModule and make sure that it returns the correct class
    # to instantiate

    sample

# Generated at 2022-06-13 10:44:55.181206
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import ansible.plugins.action.set_fact as module
    assert issubclass(module.ActionModule, ActionBase)

# Generated at 2022-06-13 10:44:57.958743
# Unit test for constructor of class ActionModule
def test_ActionModule():
    d = dict(a='1', b='2')
    m = ActionModule(d, '/dev/null')
    assert m.name == 'set_fact'
    assert m._templar == d

# Generated at 2022-06-13 10:45:08.309420
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    class Task:
        def __init__(self):
            self.args = {'cacheable':'True'}

    class Play:
        def __init__(self):
            self.tasks = [Task()]

    class PlayContext:
        def __init__(self):
            self.play = Play()

    class Options:
        def __init__(self):
            self.connection = 'local'
            self.module_path = None
            self.forks = None
            self.become = None
            self.become_method = None
            self.become_user = None
            self.check = None
            self.diff = None

    class VariableManager:
        def __init__(self):
            self.extra_vars = dict()
            self.options_vars = dict()


# Generated at 2022-06-13 10:45:18.940321
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Create instance of ActionModule
    am = ActionModule('test_name', 'test_action', {})

    # Test when task_var is None
    am._task.args = {'k1': 'v1', 'k2': 'v2'}
    result = am.run(task_vars=None)
    # result['ansible_facts']['k1'] should be 'v1'
    assert result['ansible_facts']['k1'] == 'v1'
    # result['ansible_facts']['k2'] should be 'v2'
    assert result['ansible_facts']['k2'] == 'v2'

    # Test when task_var is not None
    # result['ansible_facts']['k1'] should be 'v1'

# Generated at 2022-06-13 10:45:22.137846
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # type: () -> None
    action_module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert action_module

# Generated at 2022-06-13 10:45:26.443729
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Try passing a non-identifier in the arguments
    test_args = {
        'foo bar': 'baz'
    }

    # Instantiate test class
    am = ActionModule(None, test_args)
    try:
        am.run()
        assert False
    except AnsibleActionFail:
        assert True

    # Try passing an identifier in the arguments
    test_args = {
        'foo_bar': 'baz'
    }

    # Instantiate test class
    am = ActionModule(None, test_args)
    try:
        am.run()
        assert True
    except AnsibleActionFail:
        assert False

# Generated at 2022-06-13 10:45:37.405197
# Unit test for constructor of class ActionModule
def test_ActionModule():
    mod = ActionModule()


# Generated at 2022-06-13 10:45:38.220145
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule()

# Generated at 2022-06-13 10:45:48.247908
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import ansible.playbook.task
    import ansible.runner.return_data
    import ansible.utils.template
    import ansible.vars.hostvars
    import ansible.vars.unsafe_proxy
    import ansible.template

    host = ansible.vars.hostvars.HostVars(
        hostname='localhost',
        vars={'foo': False},
        groups=['all', 'ungrouped'],
        connection='local',
    )
    si = ansible.template.template.VariableManager()
    tk = ansible.playbook.task.Task()
    tk._role = None
    tk._block = None
    tk._parent = None
    tk._loader = None
    tk._variable_manager = si
    tk._always_run = False

# Generated at 2022-06-13 10:45:55.106495
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    mock_loader, mock_templar, mock_task = create_mock_for_class_under_test()

    action = ActionModule(mock_loader, mock_templar, mock_task)

    mock_task.args = {'cacheable': False, 'foo': 'bar', 'baz': 'quux', 'one': 'two'}
    expected_result = {'ansible_facts': {'foo': 'bar', 'baz': 'quux', 'one': 'two'}, '_ansible_facts_cacheable': False}
    result = action.run(None, None)
    assert result == expected_result



# Generated at 2022-06-13 10:45:57.065007
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(None, None, None, None) is not None

# Generated at 2022-06-13 10:46:03.022623
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    print("test_ActionModule_run ...")

    action_module = ActionModule()
    print("action_module = ", action_module)

    task_vars = {}
    tmp = None
    ansible_.constants.DEFAULT_JINJA2_NATIVE = True
    result = action_module.run(tmp, task_vars)
    print("result = ", result)
    assert result['ansible_facts']['test_fact'] == 'test_value'
    assert result['_ansible_facts_cacheable'] == False

if __name__ == "__main__":
    test_ActionModule_run()

# Generated at 2022-06-13 10:46:04.388217
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(None, dict(a=1, b=2))


# Generated at 2022-06-13 10:46:06.307550
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule(None, {}, {}, {})
    assert am is not None


# Generated at 2022-06-13 10:46:09.358521
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert C.DEFAULT_JINJA2_NATIVE is True

# Unit: Test the Action base class
# NOTE: This unit test only tests the constructor of the class.
# TODO: Add unit testing for the 'run' method

# Generated at 2022-06-13 10:46:11.428175
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert module

# Generated at 2022-06-13 10:46:38.707806
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Create a mock task to run test on
    class MockVarsModule(object):
        def __init__(self):
            self._task = MockTask()

    # Create a mock task to run test on
    class MockTask(object):
        def __init__(self):
            self.args = dict()

    # Create a mock templar to run test on
    class MockTemplar(object):
        def __init__(self):
            pass

        def template(self, key):
            return key

    # Create a mock actionbase to run test on
    class MockActionBase(ActionBase):
        def __init__(self):
            self._templar = MockTemplar()

    # Create a mock ansible to run test on

# Generated at 2022-06-13 10:46:49.241814
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Create object
    action_module = ActionModule(None, None)
    assert(action_module is not None)

    # Set object attributes
    action_module._connection = None
    action_module._templar = None
    action_module._task_vars = None
    action_module._loader = None
    action_module._templar = None
    action_module._shared_loader_obj = None
    action_module._connection = None
    action_module.runner_on_failed = None
    action_module._task = None

    # Test get_hook_impl method
    assert(action_module.get_hook_impl() is None)

    # Test get_name method
    assert(action_module.get_name() is None)

# Generated at 2022-06-13 10:46:57.983430
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    #Define the values used in the unit tests

    # No key/value pairs provided
    test_no_key_value_pairs = dict()

    # Cacheable key/value pairs provided
    test_cacheable_key_value_pairs = dict(ansible_os_family='RedHat', ansible_distribution='CentOS')

    # Non-cacheable key/value pairs provided
    test_non_cacheable_key_value_pairs = dict(ansible_os_family='RedHat', ansible_distribution='CentOS')

    # Key/value pairs provided with invalid variable name

# Generated at 2022-06-13 10:46:58.485571
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule()


# Generated at 2022-06-13 10:46:58.844455
# Unit test for constructor of class ActionModule
def test_ActionModule():
    pass

# Generated at 2022-06-13 10:47:00.298734
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(None, None).run() is not None

# Generated at 2022-06-13 10:47:10.624925
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    my_action_module = ActionModule()
    my_action_module._task = dict()
    my_action_module._task["action"] = "set_fact"
    my_action_module._task["args"] = {"ansible_facts": {"key": "value"}}
    result = my_action_module.run()
    assert result["ansible_facts"]["key"] == "value"
    assert result["_ansible_facts_cacheable"] == False

    # setting it with cacheable
    my_action_module._task["args"] = {"ansible_facts": {"key": "another value", "cacheable": True}}
    result = my_action_module.run()
    assert result["ansible_facts"]["key"] == "another value"
    assert result["_ansible_facts_cacheable"] == True

# Generated at 2022-06-13 10:47:11.780908
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule()
    assert module

# Generated at 2022-06-13 10:47:20.484548
# Unit test for constructor of class ActionModule
def test_ActionModule():
    text = '''
        - one: two
          three: four
    '''
    task_vars = dict(v1='version_one')
    task_vars['v2'] = 'version_two'

    am = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    result = am.run(task_vars=task_vars)
    assert result['ansible_facts'] == dict(one='two', three='four')
    assert result['_ansible_facts_cacheable'] is True
    assert 'failed' not in result

# Generated at 2022-06-13 10:47:34.184447
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import json

    # Construct an instance of ActionModule using mock import path
    action_module = ActionModule({}, mock_import_path)

    # sanity check
    assert action_module._connection is None

    # prepare the action run arguments

# Generated at 2022-06-13 10:48:23.734347
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import sys
    import os
    import json
    import pytest
    from ansible.module_utils.six import PY3

    if not PY3:
        reload(sys)
        sys.setdefaultencoding('utf8')

    dp = dict()
    dp["action"] = "set_fact"
    dp["task"] = {
        "id": "set_fact",
        "role": "role1",
        "tags": ["tag1", "tag2"],
        "vars": {},
        "args": { "my_var":"my_value" },
        "ignore_errors": False,
        "delegate_to": "127.0.0.1"
        }


# Generated at 2022-06-13 10:48:25.751371
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """ Unit tests for constructor of ActionModule.
    """
    data = {}
    action_module = ActionModule(data, {})
    assert isinstance(action_module, object)

# Generated at 2022-06-13 10:48:33.001719
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    host = type('Host', (), {})()
    host.get_name = lambda: 'localhost'
    module_name = 'setup'
    task = type('Task', (), {
        'args': {},
        'action': 'setup',
        '_host': host,
        'tags': ['always', 'collect-facts']
    })()
    try:
        ActionModule(task, {}).run(task_vars={'inventory_hostname': 'localhost'})
    except AnsibleActionFail as e:
        assert e.result['msg'] == 'No key/value pairs provided, at least one is required for this action to succeed'
    else:
        assert False, 'AnsibleActionFail was not raised'
    task.args = {'name1': 'value1', 'name2': 'value2'}

# Generated at 2022-06-13 10:48:40.368770
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # create object
    module_args = dict(
        key1='value1',
        key2=2,
        key3=False,
    )
    task = dict(
        action=dict(
            module='set_fact',
            args=module_args
        )
    )
    am = ActionModule(task, dict())

    # run
    tmp = None
    task_vars = dict()
    result = am.run(tmp, task_vars)

    # verify
    assert result['ansible_facts'] == dict(
        key1='value1',
        key2=2,
        key3=False,
    )

# Generated at 2022-06-13 10:48:42.850275
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Test class instantiation
    action = ActionModule(None, None, None, None, None)
    assert action.TRANSFERS_FILES == False

# Generated at 2022-06-13 10:48:51.958313
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import os
    import sys
    sys.path.append(os.getcwd())
    from ansible.errors import AnsibleActionFail
    from ansible.module_utils.six import string_types
    from ansible.module_utils.parsing.convert_bool import boolean
    from ansible.plugins.action.set_fact import ActionModule
    # Constructor test
    actionModule = ActionModule(loader=None, task=None, connection=None)
    # load_entry_point test
    entry_point = {}
    entry_point['action'] = 'action_plugins.set_fact'
    load_entry_point = actionModule._load_entry_point('action', entry_point)
    # _get_tmp_path test

# Generated at 2022-06-13 10:49:01.926213
# Unit test for constructor of class ActionModule
def test_ActionModule():
    host_vars = dict()
    host_vars['a'] = 1
    task_vars = dict()
    task_vars['a'] = 1

    task_name = 'test_action_module'
    task_action  = dict(a=1)


# Generated at 2022-06-13 10:49:11.744957
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task import Task

    DATA = {}

    def get(key, default=None):
        return DATA.get(key, default)

    def set(key, value):
        DATA[key] = value

    class PlayContext:
        def __init__(self):
            self.prompt = None

    class Host:
        def __init__(self):
            self.name = 'host-name'

    class Play:
        def __init__(self):
            self.hostvars = dict()

    class Task:
        def __init__(self):
            self.name = 'task-name'
            self.action = 'debug'
            self._role = None
            self._task_fields = dict()

    class VariableManager:
        def __init__(self):
            self.vars

# Generated at 2022-06-13 10:49:18.572697
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import os
    import sys

    source_folder = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(source_folder + "/../../..")

    from AnsibleModuleHelper import example_action_module, AnsibleModuleHelper

    tmp, task_vars = AnsibleModuleHelper.init_test(
        source_folder,
        source_folder + "/../../fixtures/test_vars/facts_module_fixtures.yaml"
    )

    action_module = example_action_module.ActionModule(
        task=None,
        connection=None,
        _play_context=None,
        loader=None,
        templar=None,
        shared_loader_obj=None
    )


# Generated at 2022-06-13 10:49:20.515013
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule.__name__ == "ActionModule"
    assert ActionModule.TRANSFERS_FILES == False

# Generated at 2022-06-13 10:51:10.232332
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule()
    assert isinstance(module, ActionModule)

# Generated at 2022-06-13 10:51:16.285767
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(ActionBase._shared_loader_obj,
                         "/home/gchen1/ansible/lib/ansible/plugins/action",
                         'set_fact',
                         {"test1": "test1"},
                         "gchen1",
                         "123",
                         "",
                         "",
                         "",
                         "",
                         "",
                         "",
                         "",
                         "",
                         "")
    return module

# Generated at 2022-06-13 10:51:16.772121
# Unit test for constructor of class ActionModule
def test_ActionModule():
    return True

# Generated at 2022-06-13 10:51:18.197577
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(None, {}, None, "set_fact", None, None) is not None

# Generated at 2022-06-13 10:51:25.974604
# Unit test for method run of class ActionModule
def test_ActionModule_run():
  from ansible.module_utils.parsing.convert_bool import boolean
  from ansible.plugins.action.set_fact import ActionModule
  from ansible.utils.vars import merge_hash

  host = 'localhost'
  conn = 'ssh'
  tmp = '/tmp'
  args = {'k': 'v'}
  task_vars = {'facts': {'original': 'fact'}}

  action = ActionModule(dict(host=host, connection=conn), tmp, task_vars, args)
  result = action.run(tmp, task_vars)

  assert len(result.keys()) == 2
  assert result['ansible_facts']['original'] == 'fact'
  assert result['ansible_facts']['k'] == 'v'

# Generated at 2022-06-13 10:51:27.387001
# Unit test for method run of class ActionModule

# Generated at 2022-06-13 10:51:28.573366
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule is not None
    actionModule = ActionModule()
    assert actionModule._shared_loader_obj is not None

# Generated at 2022-06-13 10:51:33.420080
# Unit test for constructor of class ActionModule
def test_ActionModule():
    should_result = {
        u'ansible_facts': {
            u'a': 1,
            u'b': 2,
            u'c': u'{{ an }}{{ sib }}le'
        },
        u'_ansible_facts_cacheable': True
    }
    assert ActionModule({}, {'a': 1, 'b': 2, 'c': '{{ an }}{{ sib }}le', 'cacheable': u'yes'}) == should_result
    assert ActionModule({}, {'a': 1, 'b': 2, 'c': '{{ an }}{{ sib }}le', 'cacheable': True}) == should_result
    assert ActionModule({}, {'a': 1, 'b': 2, 'c': '{{ an }}{{ sib }}le'}) == should_result
    assert ActionModule

# Generated at 2022-06-13 10:51:34.912663
# Unit test for constructor of class ActionModule
def test_ActionModule():
    a = ActionModule()
    assert a is not None

# Generated at 2022-06-13 10:51:38.295728
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import ansible.plugins.action.set_fact as action
    assert hasattr(action.ActionModule, 'run')