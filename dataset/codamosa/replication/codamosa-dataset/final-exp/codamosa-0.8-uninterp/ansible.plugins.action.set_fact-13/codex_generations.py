

# Generated at 2022-06-13 10:42:22.311969
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils.parsing.convert_bool import boolean
    ac = ActionModule(dict(ANSIBLE_MODULE_ARGS={}, ANSIBLE_MODULE_REQUIREMENTS=""), task_vars=[])
    assert boolean("false", strict=False) == False
    assert boolean("true", strict=False) == True
    assert boolean("yes", strict=False) == True
    assert boolean("no", strict=False) == False
    assert ac.run({}, {"foo":1})["ansible_facts"] == {}
    assert ac.run({}, {"foo":1})["_ansible_facts_cacheable"] == False
    assert ac.run({"foo": 1}, {})["ansible_facts"] == {"foo": 1}

# Generated at 2022-06-13 10:42:23.521346
# Unit test for constructor of class ActionModule
def test_ActionModule():

    assert ActionModule(dict(), load_module_spec_from_file=False, task_uuid=None)

# Generated at 2022-06-13 10:42:27.235825
# Unit test for constructor of class ActionModule
def test_ActionModule():
	task_vars = {'deployment': 'deploy_1'}
	task_args = {'cacheable': False}
	module = ActionModule(task=None, connection=None, play_context=None,
			loader=None, templar=None, shared_loader_obj=None)
	module.run(task_vars=task_vars, tmp=None)

# Generated at 2022-06-13 10:42:31.551742
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # set up required vars
    module_name = 'setup'
    tmp = ''
    task_vars = dict()
    task_vars['ansible_facts'] = dict()

    # create an instance of the ActionModule class
    action = ActionModule(module_name, tmp, task_vars)

    # create a test result
    result = {}

    # execute run method
    result = action.run(tmp, task_vars)

    # assert that the test did what it should have
    assert result['ansible_facts'] is not None
    assert result['_ansible_facts_cacheable'] is True
    assert result['changed'] is False

# Generated at 2022-06-13 10:42:35.989890
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action = ActionModule()
    print(action.run(tmp=None, task_vars=None))
    print(action.run(tmp=None, task_vars={'ansible_facts': {'a': 1}}))

# Generated at 2022-06-13 10:42:42.815986
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import mock
    import tempfile
    from ansible.vars import VariableManager
    from ansible.playbook.play_context import PlayContext
    from ansible.module_utils.parsing.convert_bool import boolean
    from ansible.plugins.action.set_fact import ActionModule

    v = VariableManager()
    fd, fname = tempfile.mkstemp()

    action = ActionModule(mock.Mock(), {'_ansible_no_log': False, '_ansible_verbosity': 3},
        mock.Mock(), task_vars=v.get_vars(play=mock.Mock()), loader=mock.Mock(), templar=mock.Mock())

    context = PlayContext()
    action._connection = mock.Mock()

# Generated at 2022-06-13 10:42:43.649728
# Unit test for constructor of class ActionModule
def test_ActionModule():
    obj = ActionModule({}, {}, {})
    assert isinstance(obj, ActionBase)

# Generated at 2022-06-13 10:42:53.316832
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    example_variables = {
        'ansible_local': {
            'test_facts': {
                'fact_one': 'abc'
            }
        }
    }
    class TestActionModule(ActionModule):
        '''Test class for testing run method of class ActionModule
        '''
        def run(self, tmp=None, task_vars=None):
            self.tmp = tmp
            self.task_vars = task_vars
            return super(TestActionModule, self).run(tmp, task_vars)
    test_module = TestActionModule()
    task_vars = {'ansible_local': {'test_facts': {'fact_one': 'abc'}}}

    arguments = {
        'cacheable': False,
        'fact_two': 'def'
    }
    test_

# Generated at 2022-06-13 10:43:00.343711
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Setup fake objects
    ansible_variables = {"test_var_name" : "test_var_value" }
    task_vars = {'vars': ansible_variables }
    action = ActionModule(dict(test_arg_name="test_arg_value"), dict(), False)
    # Call method
    result = action.run(None, task_vars)
    # Verify results
    assert result['ansible_facts'] == {"test_var_name" : "test_var_value"}

# Generated at 2022-06-13 10:43:08.851412
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import sys
    import inspect
    from ansible.errors import AnsibleActionFail
    from ansible.module_utils._text import to_text
    from ansible.module_utils.common._collections_compat import Mapping, MutableMapping, Sequence, Set

    # Fixture 1
    #
    # action = ActionModule({'module_name': 'debug', 'module_args': {'msg': 'Hello World', 'verbosity': 0, '_ansible_verbosity': 0, '_ansible_check_mode': False, 'ANSIBLE_MODULE_ARGS': {'msg': 'Hello World', 'verbosity': 0}}}, [])

    # action_module = ActionModule(action, [])
    # assert isinstance(action_module.run(), dict)

    # Fixture 2
    #
    # action = Action

# Generated at 2022-06-13 10:43:19.713664
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    args = {}
    args['key1'] = 'value1'
    args['key2'] = None
    args['key3'] = 'value3'
    args['key4'] = 'value4'
    args['key5'] = 'value5'
    args['key6'] = 'value6'
    args['key7'] = 'value7'

    module_args = {}
    module_args.update(args)

    tmp = None

    task_name = 'test_ActionModule_run'

    # Not actually necessary since we verify the arguments before calling ActionBase.run(), but just in case...
    task_vars = {}

    action = ActionModule(task_name, task_vars=task_vars)

# Generated at 2022-06-13 10:43:29.098998
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    #
    # Define test `action_module` object for unit tests to use
    #
    class ActionModule_obj:
        def __init__(self, args=None):
            self.args = args

    #
    # Define test `task_vars` object for unit tests to use
    #
    class task_vars_obj:
        def __init__(self, facts=None, cacheable=False):
            self.facts = facts

    #
    # Define test `action_base` object for unit tests to use
    #
    class action_base_obj:
        def __init__(self, result=None):
            self.result = result

    #
    # Define test `templar` object for unit tests to use
    #


# Generated at 2022-06-13 10:43:36.688768
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Only to be run automatically by nose on one test class or one test case level
    if os.getenv('NOSE_WITHOUT_ACTIONMODULE_RUN_'):
        return

    module_args = dict(
        ansible_facts = dict(
            a_fact = 'test',
        )
    )
    module_return = dict(
        ansible_facts = dict(
            a_fact = 'test',
        )
    )
    module = ActionModule(dict(), module_args)
    assert module.run() == module_return

# Generated at 2022-06-13 10:43:50.667949
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook import Play

    task = dict(action=dict(module='setup', args=dict(cacheable=True)))
    play_context = dict(become=True, become_method='sudo', become_user='root')
    task_include = TaskInclude(task)
    play = Play().load(task, play_context, variable_manager=None, loader=None)
    new_task = task_include.get_task_copy()

    action_plugin = ActionModule(new_task, play_context, None, loader=None, templar=None, shared_loader_obj=None)
    assert action_plugin is not None

    assert action_plugin._task is not None
    assert action_plugin._task.action['module'] == 'setup'

# Generated at 2022-06-13 10:43:52.953151
# Unit test for constructor of class ActionModule
def test_ActionModule():
    a = ActionModule(None, None, None, None)
    assert not a.TRANSFERS_FILES

# Generated at 2022-06-13 10:44:03.868136
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''
    Unit test for constructor of class ActionModule
    '''
    module_name = 'test_module'
    task_name = 'test_task'
    play_context = {}
    new_stdin = 'test'

    test_action_module = ActionModule(module_name, task_name, play_context, new_stdin)

    assert test_action_module.name == module_name
    assert test_action_module.action == task_name
    assert test_action_module._play_context == play_context
    assert test_action_module._connection == None

# Generated at 2022-06-13 10:44:05.673470
# Unit test for constructor of class ActionModule
def test_ActionModule():
    x = ActionModule(None, {}, {})
    assert x is not None

# Generated at 2022-06-13 10:44:14.673093
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.module_utils.facts import ansible_facts
    from ansible.module_utils._text import to_native

    # Mock task object
    class MockTask(object):
        def __init__(self):
            self.action = 'myaction'
            self.name = 'Test Action'
            self.args = dict()

    # Mock runner object
    class MockRunner(object):
        def __init__(self):
            self.action_plugins = dict()
            self.module_name = 'mymodule'
            self.cwd = 'ansible'
            self._config_module = 'mod'
            self._config_data = dict()
            self._shared_loader_obj = None
            self._task = MockTask()

    myaction = ActionModule(MockRunner())

    # Test if constructor raises an error

# Generated at 2022-06-13 10:44:19.008362
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule({'module_name': 'test'})
    assert action._task is not None
    assert action._connection is None
    assert action._play_context is not None
    assert action._loader is not None
    assert action._templar is not None
    assert action._shared_loader_obj is not None

# Generated at 2022-06-13 10:44:24.536877
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """
    Run a minimal test of the ActionModule constructor with a known set of inputs and outputs
    """
    test_dict = {'test_key': 'test_val'}

    mod = ActionModule({'test_key': 'test_val'},{},{})
    assert mod.run(None, {"ansible_facts":{}}) == {"ansible_facts":test_dict, "_ansible_facts_cacheable":False}

# Generated at 2022-06-13 10:44:41.959721
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """
    Unit test for method run of class ActionModule
    :return:
    """
    # NOTE the API for ansible is not stable yet ... so we might need to change this test ...
    # test_data = [
    #     {
    #         'inputs': {
    #             '_task': {
    #                 'args': {
    #                     'cache': True,
    #                     'test1': 'test1',
    #                     'test1v': 'test1v',
    #                 },
    #             },
    #         },
    #         'expected': {
    #             'ansible_facts': {
    #                 'test1': 'test1',
    #                 'test1v': 'test1v',
    #             },
    #             'changed': False,
    #         }
   

# Generated at 2022-06-13 10:44:43.211525
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass  # TODO: implement this unit test

# Generated at 2022-06-13 10:44:56.169596
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.parsing.convert_bool import boolean

    module = AnsibleModule(argument_spec=dict(test_key=dict(type='str', default='test_value'), test_key2=dict(type='bool', default=True), test_key3=dict(type='bool', default=False)))
    action_obj = ActionModule(module, dict(name='test_facts'))

    # Test a dictionary of valid key/value pairs
    result = action_obj.run(task_vars={'ansible_facts': dict()})
    assert result['ansible_facts']['test_key'] == 'test_value'
    assert result['ansible_facts']['test_key2'] is True

# Generated at 2022-06-13 10:45:01.495507
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # HACK: using globals() to access the module member to set this
    # attribute so call to the constructor can be tested.
    globals()['_DEFAULT_ARGS'] = dict(
        cacheable=False
    )
    action_plugin = ActionModule()
    assert isinstance(action_plugin, ActionModule)
    assert action_plugin
    assert action_plugin._task.args.get('cacheable') == False

# Generated at 2022-06-13 10:45:04.072648
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Test creating an ActionModule without arguments
    assert ActionModule(None, {}, None) is not None, "Failed to create an ActionModule"

# Generated at 2022-06-13 10:45:12.405007
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    class TmpActionModule(ActionModule):

        class Task:
            args = dict(a="b", c="d")

        class AnsibleVars:
            def __init__(self):
                self.data = dict(e="f", g="h")

        class AnsibleTask:
            def __init__(self, vars):
                self.vars = vars

        class AnsiblePlay:
            def __init__(self, task):
                self.task = task

        class AnsibleRunner:
            def __init__(self, play):
                self.runner = dict()
                self.runner['play'] = play

        class AnsibleModule:
            def __init__(self, runner, task):
                self.runner = runner
                self.task = task


# Generated at 2022-06-13 10:45:13.266554
# Unit test for constructor of class ActionModule
def test_ActionModule():
    ActionModule()

# Generated at 2022-06-13 10:45:15.182439
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Constructor test.
    action_plugin_class = ActionModule()
    assert action_plugin_class is not None

# Generated at 2022-06-13 10:45:16.801697
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    print("Testing ActionModule.run")
    ActionModule.run()

# Generated at 2022-06-13 10:45:21.761084
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    actionModule = ActionModule(task=dict(action=dict(module_name='set_fact', args=dict(a=dict(b=1, c=2), d=3))))
    assert actionModule.run() == dict(ansible_facts=dict(a=dict(b=1, c=2), d=3), _ansible_facts_cacheable=False)

# Generated at 2022-06-13 10:45:48.056060
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import json
    import mock
    import os

    C.DEFAULT_HASH_BEHAVIOUR = 'replace'

    def _remove_tmp_path(path):
        if os.path.exists(path):
            os.unlink(path)

    class FakeTask(object):
        def __init__(self):
            self.action = 'fakeaction'
            self.name = 'fakeaction'

    class FakeModule(object):
        def __init__(self):
            self.params = {
                '_ansible_tmpdir': '/tmp/ansible-tmp'
            }
            self.tmpdir = '/tmp/ansible-tmp'
            self.task_vars = {'test_var': 'A'}


# Generated at 2022-06-13 10:45:49.642745
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule()
    assert isinstance(am, ActionBase)

# Generated at 2022-06-13 10:45:55.108459
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert isidentifier('_single_underscore')
    assert isidentifier('singleLetter')
    assert isidentifier('multipleLetters')
    assert isidentifier('multiple123')
    assert isidentifier('multiple_123')
    assert isidentifier('_multiple_123')

    assert not isidentifier('123startNumber')
    assert not isidentifier('123')
    assert not isidentifier('has spaces')
    assert not isidentifier('!bang')
    assert not isidentifier('@at')
    assert not isidentifier('#hash')

# Generated at 2022-06-13 10:45:57.064633
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """
    Unit test for method run of class ActionModule
    """

    pass

# Generated at 2022-06-13 10:45:57.658352
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True

# Generated at 2022-06-13 10:46:05.328601
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import os
    import tempfile

    from ansible.playbook.task import Task

    from ansible.utils.display import Display
    display = Display()

    current_dir = os.path.dirname(__file__)
    datadir = os.path.join(current_dir, '..', '..', '..', 'lib', 'ansible', 'modules', 'extras', 'test', 'unit', 'data')

    yaml_path = os.path.join(datadir, 'test_set_fact_constructor.yaml')

# Generated at 2022-06-13 10:46:07.523870
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # TODO create a unit test for method 'run' of class ActionModule
    print('ActionModule.run() unit test not implemented')

# Generated at 2022-06-13 10:46:15.160542
# Unit test for constructor of class ActionModule
def test_ActionModule():
    class FakeModule:
        def __init__(self):
            self.params = {}
            self.tmpdir = 'tmpdir'
            self.task_vars = {}
            self.args = ['foo=bar']

    class FakeLoader():
        pass

    class FakeTemplar():
        def __init__(self):
            self.available_variables = {}
            self.template = lambda data: data

    class FakePlayContext():
        pass

    class FakeTask():
        def __init__(self):
            self._role = None
            self._task_fields = {}
            self._clears_facts = None

    action = ActionModule(FakeLoader(), FakeTask(), FakePlayContext())
    action._task = FakeTask()
    action._task.args = {}
    action._templar = FakeTemplar()


# Generated at 2022-06-13 10:46:21.759461
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import pytest
    from ansible.module_utils.six import PY2
    from ansible.module_utils.parsing.convert_bool import boolean

    mock_self = type('TestActionModule', (object,), {
        '_task': type('TestTask', (object,), {'args': {}}),
        '_templar': type('TestTemplar', (object,), {'template': str})
    })
    mock_self._task.args['cacheable'] = 'no'
    mock_self._task.args['one'] = '1'
    mock_self._task.args['two'] = '2'

    # No args are provided when calling ActionModule.run
    # This is not a valid action, so we expect an ActionFail exception

# Generated at 2022-06-13 10:46:31.839882
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Given:
    module_name = 'test_module'
    task = dict(action=dict(module=module_name))
    dummy_connection = dict()
    play_context = dict()

    # When:
    module = ActionModule(task, dummy_connection, play_context, loader=None, templar=None, shared_loader_obj=None)

    # Then:
    assert module.task == task
    assert module._task == task
    assert module.connection == dummy_connection
    assert module._connection == dummy_connection
    assert module.play_context == play_context
    assert module._play_context == play_context
    assert module._loader is None
    assert module._templar is None
    assert module._shared_loader_obj is None

    assert module.name == module_name
    assert module.deprecated

# Generated at 2022-06-13 10:47:08.147403
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = ActionModule(None, None)
    result = action_module._execute_module('action_module')
    assert result['ansible_facts']=={'foo': 'bar', 'baz': 3}
    assert result['changed'] == False

# Generated at 2022-06-13 10:47:18.230694
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # executed with not arguments
    args = {}
    action = ActionModule(None, args, load_callback_plugins=False, runner_callback=None,
                          connection_callbacks=[], runner_callbacks=[], action_callbacks=[], always_run=False,
                          task_vars=None, shared_loader_obj=None)
    result = action.run(tmp=None, task_vars=None)
    assert(result['failed'])
    # executed with invalid arguments
    args = {
        '0': 'test',
        '1': 'test',
        'a[b]': 'test',
        'a.b': 'test',
    }

# Generated at 2022-06-13 10:47:29.525660
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import ast
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--foo', '-f', action='store_true')
    options, args = parser.parse_known_args(['--foo'])
    task = type('', (), dict(module_args=ast.literal_eval(str(options))))

    module = type('', (), dict(_templar=None, _task=task, _connection=None))
    module = module()

    result = module.run()

    assert result['ansible_facts'] == {'foo': True}
    assert result['_ansible_facts_cacheable'] == False

# Generated at 2022-06-13 10:47:38.504934
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = "test_action"
    tmp = "/tmp"
    task_vars = dict()
    args = dict()
    datastructure = dict(args=args,
                         name=module,
                         action='test_action')
    task = ActionModule(datastructure=datastructure,
                        connection=None,
                        play_context=None,
                        loader=None,
                        templar=None,
                        shared_loader_obj=None)

    assert task.name == module
    assert task.action == 'test_action'
    assert task.args == args
    assert task.async_val == 0
    assert task.poll == 0
    assert task.delegate_to is None
    assert task.notify == []
    assert task.notified_by == []
    assert task.run_once is False
   

# Generated at 2022-06-13 10:47:51.333423
# Unit test for constructor of class ActionModule

# Generated at 2022-06-13 10:47:54.778146
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Without the class on python 3, it seems to get confused and
    # uses the older version of this class (I think)
    obj1 = ActionModule()
    assert obj1

# Generated at 2022-06-13 10:48:04.931692
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # this test is a mock of the _execute_module function, so we can check what the result of our __call__ would be
    # but this approach lacks the checks if e.g. a valid module was found - these are done in _execute_module
    import json
    from ansible.playbook.play_context import PlayContext
    from ansible.collections import defaultdict
    from ansible.vars.hostvars import HostVars
    from ansible.vars.manager import VariableManager
    from ansible.template import Templar
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    import six
    import sys


# Generated at 2022-06-13 10:48:06.521106
# Unit test for constructor of class ActionModule
def test_ActionModule():
    actionModule = ActionModule()
    assert not actionModule.TRANSFERS_FILES

# Generated at 2022-06-13 10:48:20.000311
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # mock task input
    module_args = {
        'python_version': '2.7.12',
        'uname_result': 'Linux foo.example.com 3.10.0-327.el7.x86_64 #1 SMP Thu Nov 19 22:10:57 UTC 2015 x86_64 x86_64 x86_64 GNU/Linux'
    }
    # mock AnsibleTask
    mock_AnsibleTask = Mock()
    mock_AnsibleTask._task = {
        'args': module_args
    }
    # mock AnsibleModule
    mock_AnsibleModule = Mock()
    mock_AnsibleModule.run = Mock(return_value=module_args)
    # mock AnsibleTemplate
    mock_AnsibleTemplate = Mock()
    mock_AnsibleTemplate.template = Mock

# Generated at 2022-06-13 10:48:20.701867
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule({}, {})

# Generated at 2022-06-13 10:49:51.826337
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils import basic

    class MockModule:
        def __init__(self, *args, **kwargs):
            self.params = kwargs

        def fail_json(self, *args, **kwargs):
            raise Exception('fail_json')

    class MockTask:
        def __init__(self, *args, **kwargs):
            self.args = kwargs

    class MockPlay:
        def __init__(self, *args, **kwargs):
            self.tasks = [MockTask(*args, **kwargs)]

        def get_variable_manager(self):
            return Basic.VariableManager()

    class MockPlaybook:
        def __init__(self, *args, **kwargs):
            self.plays = [MockPlay(*args, **kwargs)]


# Generated at 2022-06-13 10:49:52.399174
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:49:53.095358
# Unit test for constructor of class ActionModule
def test_ActionModule():
	pass

# Generated at 2022-06-13 10:50:02.837493
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Setup for test_ActionModule_run
    task_vars = {
        'somekey': 'somevalue',
    }

    tmp = None

    class _MessageStore(object):

        def __init__(self):
            self.args = []
            self.kwargs = []

        def __call__(self, *args, **kwargs):
            self.args.append(args)
            self.kwargs.append(kwargs)

    message_func = _MessageStore()

    am = ActionModule(message_func, 'somehost', task_vars)

    am._task = {'args': {
        'ansible_facts': {
            'foo': 'bar',
        },
    }}

    # Execute test_ActionModule_run
    result = am.run()

# Generated at 2022-06-13 10:50:03.414690
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:50:06.828260
# Unit test for constructor of class ActionModule
def test_ActionModule():
    loader = 'noop'
    templar = 'noop'
    shared_loader_obj = 'noop'

    am = ActionModule(loader=loader, templar=templar, shared_loader_obj=shared_loader_obj)
    assert am.TRANSFERS_FILES is False

# Generated at 2022-06-13 10:50:07.778068
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert False, "Test not implemented"

# Generated at 2022-06-13 10:50:08.449022
# Unit test for constructor of class ActionModule
def test_ActionModule():
    return None

# Generated at 2022-06-13 10:50:15.410005
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action = ActionModule()

    task = dict(
        name = 'echo',
        args = dict(
            a = 'b',
            c = 'd',
            e = 'f',
        )
    )

    result = action.run(task_vars = dict(), task = task)

    assert 'ansible_facts' in result
    assert 'a' in result['ansible_facts']
    assert 'c' in result['ansible_facts']
    assert 'e' in result['ansible_facts']


# Generated at 2022-06-13 10:50:23.187258
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import json
    from os.path import dirname, join, abspath
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.plugins.loader import action_loader

    class TestTaskQueueManager(TaskQueueManager):
        def __init__(self, *args, **kwargs):
            super(TestTaskQueueManager, self).__init__(*args, **kwargs)
            self.stats = dict(ok=0, changed=0, failed=0, unreachable=0, skipped=0)