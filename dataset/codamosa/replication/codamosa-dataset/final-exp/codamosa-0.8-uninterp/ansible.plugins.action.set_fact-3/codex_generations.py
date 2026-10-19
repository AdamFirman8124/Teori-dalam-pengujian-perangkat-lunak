

# Generated at 2022-06-13 10:42:27.716804
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # AnsibleActionFail is raised because for every key in args we must have a corresponding value.
    a = dict(type='dummy', module='set_fact', args=dict(a=None))
    a = ActionModule(a, dict())
    try:
        a.run(None, dict())
    except AnsibleActionFail as e:
        assert 'must have' in str(e)
    else:
        assert False
    # AnsibleActionFail is raised because variable name is not valid

# Generated at 2022-06-13 10:42:30.853135
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule('test', dict(a='a', b='b', c=1, d=2), False, 'localhost')
    module.run()

# Generated at 2022-06-13 10:42:43.161524
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils.parsing.convert_bool import boolean
    from ansible.utils.vars import isidentifier

    # Test 'cacheable' argument
    assert ActionModule._task.args['cacheable'] == False
    ActionModule._task.args['cacheable'] = 'true'
    assert boolean(ActionModule._task.args['cacheable']) == True
    assert ActionModule._task.args['cacheable'] == 'true'

    # Test other argument
    ActionModule._task.args['foo'] = 'bar'
    assert ActionModule._task.args['foo'] == 'bar'
    ActionModule._task.args['foo'] = 'bar'
    assert ActionModule._task.args['foo'] == 'bar'
    ActionModule._task.args['foo'] = 'true'

# Generated at 2022-06-13 10:42:44.715628
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert isidentifier('hello') == True
    assert isidentifier('$hello') == False
    assert isidentifier('!hello') == False

# Generated at 2022-06-13 10:42:54.341850
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # We will use the following task with args.
    task = {
        "args": {
            "override_ansible_facts": {
                "ansible_test_override": "test_override"
            },
            "set_ansible_facts": {
                "ansible_test_setting": "test_setting"
            }
        }
    }

    # We will use ansible global variables as task vars.
    #     'ansible_facts': { "ansible_test_default": "test_default" }
    task_vars = {
        'ansible_facts': { "ansible_test_default": "test_default" }
    }

    module = ActionModule(task, task_vars=task_vars)

# Generated at 2022-06-13 10:42:54.973967
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:43:04.416363
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action = ActionModule()

    # Testing method run of class ActionModule
    #
    # The run() method should handle the following args:
    #     - cacheable: true
    #     - foo: bar
    #
    arg_cacheable = True
    arg_foo = 'bar'
    tmp = None
    task_vars = { 'my_var': 'my_value' }
    # Executing method run of class ActionModule with above specified args.
    result = action.run(tmp, task_vars)
    assert result['_ansible_facts_cacheable'] == arg_cacheable
    assert result['ansible_facts']['foo'] == arg_foo
    return



# Generated at 2022-06-13 10:43:12.170123
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    delemiter = '.'
    new_fact = 'new_fact.9.9.9.9'
    new_fact_value = 'new_fact_value'

    # create instance of ActionModule

    action_module = ActionModule()

    # create task

    class task:
        def __init__(self):
            self.tmp = None
            self.task_vars = None

        def pop(self):
            pass

    task = task()

    # create task args

    class task_args:
        def __init__(self):
            self.cacheable = False

    task_args = task_args()

    task_args[new_fact] = new_fact_value
    task.args = task_args
    result = action_module.run(task_vars=task_vars)

# Generated at 2022-06-13 10:43:16.154150
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule('vars', dict(a=1, b=2), False, dict(), False, None)
    assert action.runner_on_ok() == dict(ansible_facts = dict(a = 1, b = 2), _ansible_facts_cacheable = False)

# Generated at 2022-06-13 10:43:23.507320
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    task = dict()
    task["args"] = dict()
    task["args"]["foo"] = "bar"
    task["args"]["baz"] = "True"
    action = dict()
    action["name"] = "set_fact"
    action["action"] = "set_fact"
    module = ActionModule(task, action, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

    tmp = None
    task_vars = dict()
    result = module.run(tmp, task_vars)


# Generated at 2022-06-13 10:43:38.133327
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule(
        task=dict(action=dict(module_name='setup', args={'name': 'modulename'})),
        connection=dict(user='user', host='host', port='port'),
        play_context=dict(become=True, become_method='sudo', become_user='root'),
        loader=None,
        templar=None,
        shared_loader_obj=None)
    assert am.task == dict(action=dict(module_name='setup', args={'name': 'modulename'}))
    assert am.connection == dict(user='user', host='host', port='port')
    assert am.play_context == dict(become=True, become_method='sudo', become_user='root')
    assert am.loader == None
    assert am.templar == None

# Generated at 2022-06-13 10:43:50.947514
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils import basic
    from ansible.plugins.loader import action_loader

    # Mock basic.AnsibleModule
    basic.AnsibleModule = basic.AnsibleBase
    am = basic.AnsibleModule(
        argument_spec={'cacheable': {'type': 'bool', 'default': False, 'required': False},
                       'name': {'type': 'str', 'required': True},
                       'value': {'type': 'str', 'required': True}
                       },
        add_file_common_args=False
    )
    am._ansible_tmpdir = ''
    am.params = {'name': 'ANSIBLE_TEST',
                 'value': 'Test'}

    action_module = action_loader.get('set_fact', am)
    result = action_module

# Generated at 2022-06-13 10:44:02.551574
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task_include import TaskInclude
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.vars.hostvars import HostVars
    from ansible.vars.unsafe_proxy import UnsafeProxy
    from ansible.module_utils.six import string_types

    # Test arguments
    my_fact_module = AnsibleUnicode('setup')
    my_play_context = PlayContext()
    my_play_context._attributes = {'forks': 10, 'host_key_checking': False, 'name': 'DummyPlay'}
    my_task_vars = {}


# Generated at 2022-06-13 10:44:12.924329
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = ActionModule(None, None, None)

    task_args = dict()
    task_args['task_vars'] = dict()

    # Unsupported cacheable value
    task_args['args'] = dict(key1="value1", cacheable="")
    result = action_module._execute_module(task_args=task_args, tmp=None, task_vars=task_args['task_vars'])
    assert not result['ansible_facts']['key1']

    # Unsupported value type
    task_args['args'] = dict(key1=["value1"], cacheable=False)
    result = action_module._execute_module(task_args=task_args, tmp=None, task_vars=task_args['task_vars'])

# Generated at 2022-06-13 10:44:23.401871
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.play import Play
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.role import Role
    from ansible.playbook.handler import Handler
    from ansible.playbook.conditional import Conditional

    # Create the host
    host = "testhost"

    # Create the task
    task = Task()

    # Create the play context

# Generated at 2022-06-13 10:44:26.540032
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action = ActionModule({'some_var': 'foobar'})
    assert action.run() == {'ansible_facts': {'some_var': True}, '_ansible_facts_cacheable': False}

# Generated at 2022-06-13 10:44:35.432155
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    class MyActionBase(ActionBase):
        def run(self, tmp=None, task_vars=None):
            return { 'foo' : 'bar' }
    my_action = MyActionBase()
    my_action.templar = type('MyTemplar', (), {'template': lambda s: s})
    my_action.task = type('MyTask', (), {'args' : {'foo':'1', 'bar':'!', 'baz':'3'}})
    result = my_action.run(tmp=None, task_vars=None)
    assert result == {'foo': 'bar', 'ansible_facts': {'foo': '1', 'bar': '!', 'baz': '3'}, '_ansible_facts_cacheable': False}

# Generated at 2022-06-13 10:44:39.687261
# Unit test for constructor of class ActionModule
def test_ActionModule():
    try:
        action_module = ActionModule(
            task=dict(),
            connection=dict(),
            play_context=dict(),
            loader=dict(),
            templar=dict(),
            shared_loader_obj=dict()
        )
        assert action_module is not None
    except TypeError as e:
        assert False

# Generated at 2022-06-13 10:44:42.451619
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Create an instance of class ActionModule
    am = ActionModule()

# Generated at 2022-06-13 10:44:47.923453
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Create an instance of the class ActionModule
    action_module = ActionModule()
    # Verify that the instance of class ActionModule is correctly created
    assert isinstance(action_module.__dict__['runner'], ActionBase)
    assert isinstance(action_module.__dict__['_templar'], ActionBase)

# Generated at 2022-06-13 10:45:06.475775
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Dict: task_vars
    task_vars = {
        'ansible_user': 'user',
        'ansible_port': '22',
        'ansible_host': 'host',
        'ansible_password': '123456',
        'ansible_ssh_private_key_file': 'app/ssh-key.pem',
        'ansible_become': 'root',
        'ansible_become_method': 'su',
        'ansible_become_user': 'root',
        'ansible_become_pass': '123456',
        'ansible_is_active': True,
        'ansible_is_reachable': True,
    }

    # Set of temp object
    tmp = 'null'

    # Dict: self._task.args
    self_task

# Generated at 2022-06-13 10:45:16.287019
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    from ansible.playbook.play_context import PlayContext

    # create a mock task and task_vars
    mock_task = {
        'action': 'set_fact',
        'args': {
            'tmp': '{{tmp}}',
            'cacheable': 'yes',
            'x': '{{x}}',
        },
        'delegate_to': None,
        'tags': []
    }

    mock_task_vars = {
        'ansible_facts': {},
        'tmp': '/path/to/jeff',
        'x': 'y',
    }

    # create a mock context
    mock_context = PlayContext()
    mock_context.become = False
    mock_context.become_user = ''
    mock_context.remote_addr = ''

# Generated at 2022-06-13 10:45:16.960361
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:45:26.105278
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager

    yaml_data = dict(
        a = 1,
        b = 2,
        c = 3,
    )
    playbook_context = PlayContext()
    task_queue_manager = TaskQueueManager(inventory=None, variable_manager=None, loader=None, passwords=None, stdout_callback=None )
    action_module = ActionModule(task=yaml_data, connection=None, play_context=playbook_context, loader=None, templar=None, shared_loader_obj=None)
    result = action_module.run(None, dict())
    assert ('ansible_facts' in result)
    assert ('_ansible_facts_cacheable' in result)

# Generated at 2022-06-13 10:45:34.962068
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    am = ActionModule(ActionBase(), dict(jinja2_native=True))
    am.module_args = { 'cacheable': False }

    # Case 1: check = True
    result = am.run(None, None)
    assert result['failed'] == True
    assert result['msg'] == 'No key/value pairs provided, at least one is required for this action to succeed'

    # Case 2: check = None
    am = ActionModule(ActionBase(), dict(jinja2_native=True))
    am.module_args = { '_test-key': '_test-value', 'cacheable': False }
    result = am.run(None, None)
    assert result['ansible_facts']['_test_key'] == '_test-value'
    assert result['_ansible_facts_cacheable'] == False

# Generated at 2022-06-13 10:45:45.448300
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Sample task that we would like to run
    test_task = {
        "action": {
            "__ansible_module__": "my_action",
            "__ansible_arguments__": {
                "testkey1": "testvalue1",
                "testkey2": "testvalue2"
            },
            "__ansible_action_wrapper__": "foo-bar"
        }
    }

    # Create an instance of ActionModule
    action_module = ActionModule({}, task=test_task)

    # Run the task on the action module
    action_module.run()


# Generated at 2022-06-13 10:45:47.288594
# Unit test for constructor of class ActionModule
def test_ActionModule():
    m = ActionModule(None, {}, {}, None, None)
    assert isinstance(m, ActionModule)

# Generated at 2022-06-13 10:45:51.001590
# Unit test for constructor of class ActionModule
def test_ActionModule():

    ansible_module = ActionModule(task='dag')
    assert ansible_module.task == 'dag'
    assert ansible_module.task_vars == {}
    assert ansible_module.play_context == {}

# Generated at 2022-06-13 10:45:57.219573
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    args = {
        "test": "param",
        "test_int": 1,
        "test_dict": { "test": 1 },
        "test_list": [ "test", 1 ],
        "test_bool": "false",
        "test_bool_upper": "FALSE",
        "test_cacheable": True,
    }

    result = dict(
        ansible_facts=dict(
            test=args["test"],
            test_dict=args["test_dict"],
            test_list=args["test_list"],
            test_bool=bool(args["test_bool"]),
            test_bool_upper=bool(args["test_bool_upper"]),
        ),
        _ansible_facts_cacheable=True,
    )

    module = ActionModule()
    actual_result = module.run

# Generated at 2022-06-13 10:46:05.325199
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Test with no arguments
    am = ActionModule()
    am._task = {'args': {}}
    result = am.run()
    assert result['failed']
    assert result['msg'] == 'No key/value pairs provided, at least one is required for this action to succeed'

    # Test with single argument
    am = ActionModule()
    am._task = {'args': {'A': 'a'}}
    result = am.run()
    assert 'ansible_facts' in result
    assert result['ansible_facts'] == {'A': 'a'}
    assert result['_ansible_facts_cacheable']

    # Test with multiple arguments
    am = ActionModule()
    am._task = {'args': {'A': 'a', 'B': 'b'}}
    result = am.run()
   

# Generated at 2022-06-13 10:46:28.608432
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Generate a mock task for the test
    task = dict(
        action=dict(
            module_name="set_fact",
            module_args=dict(
                x=1,
                y=2,
                cacheable=False,
            )
        )
    )
    # Generate a mock context for the test
    context = dict(
        tmp=None,
        task_vars=dict()
    )

    # Create an instance of the module
    module = ActionModule()
    # Execute the run method of the set_fact module and assert that the action succeeded
    assert module.run(**context)['changed'] is False

# Generated at 2022-06-13 10:46:29.622645
# Unit test for constructor of class ActionModule
def test_ActionModule():
    x = ActionModule()
    assert x

# Generated at 2022-06-13 10:46:38.401290
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Test without "key/value" pairs
    module = ActionModule(None)
    module.muterun = lambda *args, **kwargs: {"stdout": "", "rc": 0, "stdout_lines": [], "start": "", "end": "", "delta": "", "cmd": "", "stderr": "", "changed": False,}
    module._templar = 10
    module._task = {"args": {}}
    result = module.run("tmp", "task_vars")
    assert result["failed"] == True

    # Test with "key/value" pairs
    module = ActionModule(None)

# Generated at 2022-06-13 10:46:38.921518
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:46:39.814265
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule()
    assert module.run()

# Generated at 2022-06-13 10:46:51.036642
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext

    from ansible.vars.manager import VariableManager
    from ansible.utils.vars import combine_vars

    from ansible.utils.sentinel import Sentinel

    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader

    # setup
    Sent = Sentinel()

    context = PlayContext()
    context._vars = VariableManager()
    context.reset()
    context._vars.extra_vars = {'foo': 'bar'}
    context._vars.update_vars({'foo': 'bar'})

    loader = DataLoader()
    templar = Templar(loader=loader, variables=context._vars)


# Generated at 2022-06-13 10:46:55.952209
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.play_context import PlayContext
    # neeeded for this fake test, but not any real ActionModule
    import ansible.module_utils.parsing.convert_bool
    # this is a mock class to run the method
    class _ActionModule(ActionModule):
        def run(self, tmp=None, task_vars=None):
            self.task_vars = task_vars
            return super(_ActionModule, self).run(tmp, task_vars)
    # these tests need:
    #   _task.args, with supplied key=value pairs
    #   _task.action, with supplied action to perform
    #   _task.action_args, with supplied list of args to action
    # the following variables are created during run
    #   result, dict of task results

# Generated at 2022-06-13 10:46:56.343496
# Unit test for constructor of class ActionModule
def test_ActionModule():
  assert ActionModule()

# Generated at 2022-06-13 10:46:56.888907
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass


# Generated at 2022-06-13 10:46:57.268639
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:47:32.191042
# Unit test for constructor of class ActionModule
def test_ActionModule():
    ActionModule(None, None)

# Generated at 2022-06-13 10:47:40.715256
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Create a mocking task object
    # _task object is a special object that Ansible uses to
    # track variables and information regarding a task.
    # The mock task object being constructed here is a dummy object
    # that only implements enough properties to pass the checks.
    class MockTask(object):
        def __init__(self):
            self.args = {}
    task = MockTask()

    # Create a mocking _templar object
    # _templar object is a special object that Ansible uses to
    # collect variables for templates via the 'template' method.
    # The mock _templar object being constructed here is a dummy object
    # that only implements enough methods to pass the checks.
    class MockTemplar(object):
        def __init__(self):
            pass

        # The 'template' method is what Ansible uses to

# Generated at 2022-06-13 10:47:41.434945
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True

# Generated at 2022-06-13 10:47:47.125350
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # ----------------------------------------------------------------------------------------------------
    # Test the constructor of class ActionModule
    # ----------------------------------------------------------------------------------------------------
    my_action = ActionModule()
    # ----------------------------------------------------------------------------------------------------
    # Test the constructor of class ActionModule
    # ----------------------------------------------------------------------------------------------------
    my_action = ActionModule()
    my_action.run()
    assert True

# Generated at 2022-06-13 10:47:56.968535
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.role_include import IncludeRole

    t = Task()
    assert t.action._attributes['_name'] == 'meta'
    assert t.action._attributes['_parent'] == t

    t = TaskInclude()
    assert t.action._attributes['_name'] == 'include'
    assert t.action._attributes['_parent'] == t

    t = IncludeRole()
    assert t.action._attributes['_name'] == 'include_role'
    assert t.action._attributes['_parent'] == t

# Generated at 2022-06-13 10:47:58.543856
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Fails if the constructor can not be called
    ActionModule()

# Generated at 2022-06-13 10:48:09.799278
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Constructor test
    # Ensures that the module takes in the necessary parameters
    # and sets them as attributes of the module
    module = ActionModule(
        task=dict(action=dict()),
        connection=dict(),
        play_context=dict(),
        loader=dict(),
        templar=None,
        shared_loader_obj=None
    )

    assert getattr(module, '_task')
    assert getattr(module, '_connection')
    assert getattr(module, '_play_context')
    assert getattr(module, '_loader')
    assert getattr(module, '_templar')
    assert getattr(module, '_shared_loader_obj')

# Generated at 2022-06-13 10:48:22.233716
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Testing method run of class ActionModule
    #
    # setup test variables:
    module_name = 'os_server'

    # Construct args:
    args = {'a': 1, 'b': 'some_var'}
    tmp = None
    task_vars = None

    # Setup mocks:
    tmp_module_name = 'ansible.plugins.action.' + module_name
    mocked_tmp_module = mock.MagicMock()
    mocked_tmp_module.run.return_value = {'ansible_facts': args,
                                          '_ansible_facts_cacheable': True}

    mocked_module_loader = mock.MagicMock()
    mocked_module_loader.get_all_plugin_loaders.return_value = [mock.MagicMock()]

    # setup loader module


# Generated at 2022-06-13 10:48:23.595428
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Arrange
    # Act
    # Assert
    pass


# Generated at 2022-06-13 10:48:31.002710
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import json
    import os
    import sys

    from ansible.plugins.action.set_fact import ActionModule

    # Setup a fake display
    class Display:
        verbosity = 0
        _display = {}

        def display(self, msg, *args, **kwargs):
            self._display[msg] = kwargs

    # Create a fake task
    class Task:
        def __init__(self):
            self._ds = {
                'args': {},
                '_raw_params': 'facts:',
            }

        def __getitem__(self, k):
            return self._ds[k]

        def __setitem__(self, k, v):
            self._ds[k] = v

        def __contains__(self, k):
            return k in self._ds

    # Create a

# Generated at 2022-06-13 10:50:06.733141
# Unit test for constructor of class ActionModule
def test_ActionModule():
    sets = {}
    sets['results'] = []
    sets['results'].append(dict(ansible_facts=dict(sample_fact=dict(value='sample_value')), _ansible_facts_cacheable=True))
    sets['results'].append(dict(ansible_facts=dict(constant_fact=dict(value='constant_value')), _ansible_facts_cacheable=False))

    for result in sets['results']:
        assert result['ansible_facts'] == dict(sample_fact=dict(value='sample_value'), constant_fact=dict(value='constant_value'))

# Generated at 2022-06-13 10:50:16.465615
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # make it work on both python2 and python3
    try:
        from cStringIO import StringIO
    except ImportError:
        from io import StringIO
    import sys
    stdout = sys.stdout
    sys.stdout = mystdout = StringIO()

    # set default args
    args = {}
    args['cacheable'] = False
    args['ansible_facts'] = {'age': '26', 'sex': 'female'}
    args['_ansible_facts_cacheable'] = False

    # call method run from class ActionModule
    result = {}
    result = ActionModule.run(None, args)

    # check what we get from method run
    assert result.has_key('ansible_facts')
    assert result.has_key('_ansible_facts_cacheable')

    del args


# Generated at 2022-06-13 10:50:19.983688
# Unit test for constructor of class ActionModule
def test_ActionModule():
    def test_eq(a, b):
        assert a == b, "%r==%r" % (a, b)

    test_eq(ActionModule, ActionModule)
    test_eq(ActionModule.__class__, ActionBase)
    test_eq(ActionModule.__class__.__class__, type)

# Generated at 2022-06-13 10:50:26.404050
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # test creation of an object
    action = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    ansible_facts = dict()
    ansible_facts['ansible_os_family'] = "Darwin"
    ansible_facts['ansible_distribution'] = "Mac OS X"
    ansible_facts['ansible_machine'] = "x86_64"
    task_vars = dict()
    task_vars['ansible_facts'] = ansible_facts
    # execute method run with valid parameters
    result = action.run(tmp=None, task_vars=task_vars)
    assert result['ansible_facts']['ansible_os_family'] == "Darwin"

# Generated at 2022-06-13 10:50:31.682810
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    args = {'cacheable': False, 'test': 't'}
    action = ActionModule()
    action.templar = {}
    action._task = {}
    action._task.args = args
    result = action.run()
    assert result['ansible_facts'] == {'test': 't'}

# Generated at 2022-06-13 10:50:34.135340
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule(None, None, '/tmp/', None, None, None, dictionary=dict(foo='bar'))
    assert am is not None

#

# Generated at 2022-06-13 10:50:35.598359
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert issubclass(ActionModule, ActionBase)

# Generated at 2022-06-13 10:50:40.916371
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule(None, {}, {}, '/home/brady/ansible/action_plugins/systemd.py', 'systemd', {}, {}, {})
    assert am.run(tmp = None, task_vars = None) != None

# Generated at 2022-06-13 10:50:48.210046
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # let's create an action module instance to test
    am = ActionModule(task=dict(args=dict()), connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    # invoke run method with valid arguments
    am.run(task_vars=dict(test="test"))
    # now transition to fail a test
    am = ActionModule(task=dict(), connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    am.run(task_vars=dict(test="test"))

# Generated at 2022-06-13 10:50:57.123167
# Unit test for constructor of class ActionModule
def test_ActionModule():
    inv = '''
[test]
localhost ansible_connection=local
'''

    task = {'tasks':
          {'test': {
            'action': {
                    '__ansible_module__': 'debug',
                    '__ansible_action__': 'action',
                    '__ansible_arguments__': 'var=foo',
              },
            },
          }
        }

    task_copy = task.copy()

    # Initialize the task and args
    action_mod = ActionModule(task, inv, 'ansible.cfg')
    action_mod.task_copy = task_copy

    # Test that the constructor sets these variables correctly
    assert action_mod.inject == {}
    assert action_mod.task_copy == task_copy
    assert action_mod._inject == {}
    assert action_