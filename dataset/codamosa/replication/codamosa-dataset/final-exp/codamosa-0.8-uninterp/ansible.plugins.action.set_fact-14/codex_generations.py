

# Generated at 2022-06-13 10:42:22.825860
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import inspect
    
    filename = inspect.getfile(test_ActionModule_run)
    
    (args, kwargs) = ActionModule.run.__code__.co_varnames, ActionModule.run.__code__.co_argcount
    if args[:kwargs] == ('self', 'tmp', 'task_vars'):
        return True
    elif args[:kwargs] == ('self', 'task_vars', 'tmp'):
        return True
    else:
        raise ValueError('Invalid signature for {0}: {1}'.format(ActionModule.run.__name__, args[:kwargs]))

# Generated at 2022-06-13 10:42:23.462245
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:42:24.065045
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule()

# Generated at 2022-06-13 10:42:25.780366
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule()
    assert isinstance(module, ActionModule)

# Generated at 2022-06-13 10:42:26.811110
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass


# Generated at 2022-06-13 10:42:29.575769
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule({}, {}, {}, {})
    assert module.run(tmp=None, task_vars=None) == {
        'ansible_facts': {},
        '_ansible_facts_cacheable': False,
    }

# Generated at 2022-06-13 10:42:42.095713
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import sys

    # Python 2
    if sys.version_info[0] == 2:
        from ansible.module_utils.six import PY3
    # Python 3
    else:
        from ansible.module_utils.six import PY2

    from ansible.module_utils.parsing.convert_bool import boolean
    from ansible.module_utils.six import string_types

    # Python 3
    if not PY2:
        string_types = (str,)

    action_module = ActionModule()

    task_vars = dict()

    tmp = None

    # The following are not valid identifiers
    blacklist = [
        'a.b',
        'a/b',
        '-abc',
        'abc-',
        'abc:',
    ]

    # The following are valid identifiers


# Generated at 2022-06-13 10:42:44.178228
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule(None, None, task_vars=dict(foo='bar'))
    assert action.task_vars['foo'] == 'bar'

# Generated at 2022-06-13 10:42:44.945912
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule is not None

# Generated at 2022-06-13 10:42:45.718440
# Unit test for constructor of class ActionModule
def test_ActionModule():
    x = ActionModule()
    assert x is not None

# Generated at 2022-06-13 10:42:53.495941
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task import Task
    task = Task()
    task.args = {"test_name_1":"test_value_1","test_name_2":"test_value_2"}
    action_mod = ActionModule(task, {})
    assert action_mod is not None

# Generated at 2022-06-13 10:42:56.991611
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert am is not None
    assert isinstance(am, ActionBase)

# Generated at 2022-06-13 10:42:58.036475
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert False, "Test not implemented"

# Generated at 2022-06-13 10:43:03.475755
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(
        task=dict(action=dict(module='set_fact', args=dict(one=1, two=2, myname='fred'))))
    assert module._task == dict(action=dict(module='set_fact', args=dict(one=1, two=2, myname='fred')))
    assert module._templar == None

# Generated at 2022-06-13 10:43:10.888531
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils.ansible_modlib.test.test_runner_module import setup_and_run

    setup_and_run({
         'action': {
             '__ansible_module__': ActionModule,
         },
         'task': {
             'args': {
                 'hello': 'world',
                 'foo': 'bar',
                 'cacheable': False
             }
         }
     },
     """
     setup_action:
         args:
             hello: world
             foo: bar
             cacheable: False
     """,
     """
     {"changed": false, "ansible_facts": {"hello": "world", "foo": "bar"}, "_ansible_facts_cacheable": false}
     """)

# Generated at 2022-06-13 10:43:20.127833
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils import basic
    from ansible.module_utils.facts import is_fact
    from ansible.utils import vars

    host = basic.AnsibleHost('testhost')
    task = basic.AnsibleTask()
    task.hosts = [host]
    task._ds = dict(strategy='free', task=task)
    task.vars = vars.TaskVars(task, dict())

    action = ActionModule(task, dict())

    # Test case 1
    task.args = dict(facts_cacheable=True, foo='bar')
    results = action.run(tmp=None, task_vars=dict())

    assert 'ansible_facts' in results
    assert '_ansible_facts_cacheable' in results

# Generated at 2022-06-13 10:43:22.461324
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # create an instance of a class
    x = ActionModule()
    assert isinstance(x, ActionModule)


if __name__ == "__main__":
    x = ActionModule()
    x.run()
    x.transfer_files()

# Generated at 2022-06-13 10:43:25.568383
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ActionModule.run(tmp='/tmp', task_vars=dict())
    ActionModule.run(tmp=None, task_vars=dict())
    ActionModule.run(tmp=None, task_vars=None)

# Generated at 2022-06-13 10:43:27.240804
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """
    ActionModule.run()
    """
    obj = ActionModule()
    assert True

# Generated at 2022-06-13 10:43:34.870571
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """
    #Read variables from file "test/file_test.yml"
    arguments:
        file: "test/file_test.yml"
    """
    module = ActionModule()
    assert module.run() == {
        'failed': False,
        '_ansible_facts_cacheable': False,
        'ansible_facts': {
            'arguments': {
                'file': 'test/file_test.yml'
            }
        }
    }

# Generated at 2022-06-13 10:43:46.752312
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task import Task
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    inventory = InventoryManager(loader=DataLoader(), sources=None)
    variable_manager = VariableManager(loader=DataLoader(), inventory=inventory)
    loader = DataLoader()
    task = Task()
    actionModule = ActionModule(task, variable_manager=variable_manager, loader=loader)

    assert actionModule._task == task
    assert actionModule._templar == task._role._role_path._loader

# Generated at 2022-06-13 10:43:48.025713
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert isinstance(ActionModule(), ActionBase)

# Generated at 2022-06-13 10:43:49.242882
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(None, {})
    assert module

# Generated at 2022-06-13 10:43:51.173242
# Unit test for constructor of class ActionModule
def test_ActionModule():
    m = ActionModule(None, None, None)

    assert m.run(None, {})

# Generated at 2022-06-13 10:43:53.131307
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule()
    assert type(action) == ActionModule

# Generated at 2022-06-13 10:44:02.601662
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # create a ActionModule object
    am = ActionModule()

    # create a ActionBase object
    ab = ActionBase()

    # set the required attributes of a ActionModule object
    am._task = ab

    am._templar = ab

    # Call the run method of ActionModule and check the result
    #assert am.run() == {'ansible_facts': {}, '_ansible_facts_cacheable': False, 'changed': False}

    am._task_vars = {'ansible_check_mode': 'False'}
    assert am.run() == {'ansible_facts': {}, '_ansible_facts_cacheable': False, 'changed': False}

# Generated at 2022-06-13 10:44:12.964596
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    task_vars = dict()
    tmp = None
    task_action = dict()

    action_plugin = ActionModule(task=task_action, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    result = action_plugin.run(tmp, task_vars)

    assert result.get('failed')


    task_action = dict(task_vars=dict(cacheable='False'))
    action_plugin = ActionModule(task=task_action, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    result = action_plugin.run(tmp, task_vars)

    assert not result.get('failed')
    assert not result.get('ansible_facts')

# Generated at 2022-06-13 10:44:23.402385
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from unittest import TestCase
    from unittest.mock import Mock, MagicMock, patch

    module = MagicMock()
    module.NAME = 'setup'

    task = Mock()
    task.args = {}

    method = ActionModule(module, task)

    with TestCase.assertRaises(AnsibleActionFail):
        method.run(tmp=None, task_vars=None)

    task.args = {'foo': 'bar'}
    with TestCase.assertRaises(AnsibleActionFail):
        method.run(tmp=None, task_vars=None)

    task_vars = {'foo': 'bar'}
    result = method.run(tmp=None, task_vars=task_vars)

# Generated at 2022-06-13 10:44:33.539845
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils import simplejson as json
    from ansible.module_utils._text import to_bytes, to_text
    from ansible.utils import plugin_docs
    from ansible.module_utils.six.moves import StringIO
    import os

    # Setup mocks

# Generated at 2022-06-13 10:44:42.721657
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import ansible.module_utils.basic
    import ansible.module_utils.common.dicts
    import ansible.utils.vars

    result = dict(
        ansible_facts=dict(
            name='ansible'
        ),
        ansible_module_name='setup',
        ansible_module_args=dict(
        ),
    )

    # test without any module parameters
    instance0 = ActionModule(dict(
        action=dict(
            args=dict(
            )
        ),
        module_name='setup',
        module_args=dict(
        ),
    ))

    task_vars = dict()
    instance0.run(task_vars=task_vars)

# Generated at 2022-06-13 10:44:58.535131
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:44:59.580540
# Unit test for constructor of class ActionModule
def test_ActionModule():
    m = ActionModule()
    assert m is not None

# Generated at 2022-06-13 10:45:09.578587
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    def test_module(self, tmp=None, task_vars=None):
        self._templar = {}
        self._templar['template'] = lambda x: '%s_templatized' % x
        self._task = {}
        self._task['action'] = 'action_module'
        self._task['args'] = dict()
        self._task['args']['cacheable'] = False
        self._task['args']['key1'] = 'value1'
        self._task['args']['key2'] = 'value2'
        return self.run(tmp, task_vars)
    module = ActionModule()
    module.run = test_module
    result = module.run()
    assert result['ansible_facts']['key1'] == 'value1_templatized'

# Generated at 2022-06-13 10:45:13.360693
# Unit test for constructor of class ActionModule
def test_ActionModule():
    
    # Test a RoleIncludeAction
    task_result = ActionModule(dict(task=dict(action=dict(module_name='include_role', name='some_role', tasks_from='some_task'))))
    
    print(task_result)

# Generated at 2022-06-13 10:45:18.320710
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task import Task
    from ansible.playbook.role import Role
    task = Task()
    role = Role()
    task._role = role
    am = ActionModule(task=task, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)


# Generated at 2022-06-13 10:45:20.933898
# Unit test for constructor of class ActionModule

# Generated at 2022-06-13 10:45:29.342104
# Unit test for constructor of class ActionModule
def test_ActionModule():
  module_args = dict(
    data1=1,
    data2=2,
  )

  arguments = dict(
    r='nada',
    s='nada',
    template='nada',
  )

  action_module = ActionModule(dict_to_pass_to_constructor=dict())

  assert action_module.run(task_vars=dict())['failed']
  assert 'No key/value pairs provided' in action_module.run(task_vars=dict())['msg']

  # Testing with valid values
  valid_values = dict(
    data1=1,
    data2=2,
  )
  arguments.update(valid_values)
  tmp_action_module = ActionModule(dict_to_pass_to_constructor=dict())


# Generated at 2022-06-13 10:45:38.661735
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Mock methods
    class MockActionBase(ActionBase):
        def run(self, tmp=None, task_vars=None):
            if task_vars is None:
                task_vars = dict()
            result = super(MockActionBase, self).run(tmp, task_vars)
            return result
    # Create instance of class ActionModule
    instance = ActionModule(task=dict(), connection=dict(), play_context=dict(), loader=dict(), templar=dict(), shared_loader_obj=dict())
    # Set methods
    instance.run = MockActionBase.run
    # Test function get_tmp_path
    assert instance.run(None, None) == {'_ansible_verbose_always': True}

# Generated at 2022-06-13 10:45:39.582689
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    pass

# Generated at 2022-06-13 10:45:46.564798
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    def test_module(*args, **kwargs):
        return 0, '{"foo": "bar"}', {}

    my_obj = object()
    my_obj.module_name = 'my_module'
    my_obj._templar = 'my_templar'
    my_obj.task_vars = {'my_vars': 'my_val'}

    my_class = type('ActionModule', (ActionModule,), {'check_mode': False})
    my_class._shared_loader_obj = None
    my_class._task = my_obj
    my_class.run_command = lambda x,y: 0
    my_class._low_level_execute_command = test_module

    # test with a minimal set of parameters
    res = my_class.run()


# Generated at 2022-06-13 10:46:18.190768
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule is not None

# Generated at 2022-06-13 10:46:20.127361
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    m = ActionModule()
    m.run = lambda: {'ansible_facts': {'test': 'success'}}
    assert m.run() == {"ansible_facts": {"test": "success"}}


# Generated at 2022-06-13 10:46:29.299676
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ActionBase._configure_module()
    actionplugin = ActionModule(None, None, None, None, None, None, None)

    assert actionplugin.run({'test': True}) == {
        'failed': True,
        'msg': 'No key/value pairs provided, at least one is required for this action to succeed'
    }

    assert actionplugin.run({'test': True}, {'ansible_verbosity': 1}) == {
        'failed': True,
        'msg': 'No key/value pairs provided, at least one is required for this action to succeed',
        'verbosity': 1
    }


# Generated at 2022-06-13 10:46:34.940740
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    mock_ansible_module = ActionModule(
        dict(), dict(
            test_var='test_val'
        )
    )

    res = mock_ansible_module.run(dict(), dict())
    assert res == dict(
        ansible_facts={ 'test_var': 'test_val' },
        _ansible_facts_cacheable=False
    )



# Generated at 2022-06-13 10:46:35.947258
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert isidentifier("_Test_identifier") == True

# Generated at 2022-06-13 10:46:37.026519
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''Unit test for constructor of class ActionModule'''
    ActionModule('test', {})

# Generated at 2022-06-13 10:46:47.969569
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import json
    import unittest
    import ansible.constants as C


# Generated at 2022-06-13 10:46:57.041814
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # import all modules needed for ActionModule class
    import os
    import sys
    import unittest
    import ansible.plugins
    
    import ansible.playbook
    import ansible.playbook.task
    import ansible.utils.vars

    class TestActionModule(unittest.TestCase):

        def setUp(self):
            """ setup """
            pass

        def tearDown(self):
            """ teardown """
            pass
    
        def test_run(self):
            # Test the method run of class ActionModule
            # Mock playbook
            class MockTask(object):
                def __init__(self, args):
                    self.args = args
        
            # Mock PlayContext
            class MockPlayContext(object):
                pass
    
            # Mock Play

# Generated at 2022-06-13 10:47:08.231002
# Unit test for constructor of class ActionModule
def test_ActionModule():
    print("Tests for constructor of class ActionModule")

    import ansible.playbook.action
    global_vars =  {}
    global_vars["hostvars"] = {}
    global_vars["hostvars"]['localhost'] = {}
    data = {}
    data["test_one"] = "test_one"
    data["test_two"] = "test_two"
    data["test_three"] = 3

    test = ansible.playbook.action.Task()
    test._task_fields['args'] = data

    am = ActionModule()
    am._task = test

    print("Testing render_args for ActionModule")
    result = am.run(None, global_vars)
    print("Is this the result we are expecting?")

# Generated at 2022-06-13 10:47:10.613599
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert module is not None

# Generated at 2022-06-13 10:48:17.459742
# Unit test for constructor of class ActionModule
def test_ActionModule():
    pass

# Generated at 2022-06-13 10:48:27.838580
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import json

    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.vars.manager import VariableManager
    from ansible.utils.vars import load_extra_vars
    from ansible.utils.vars import load_options_vars

    class ModelData(object):
        ''' mock class to replace AnsibleModule '''

        def __init__(self, params):
            self.params = params

        def dump(self):
            return self.params


# Generated at 2022-06-13 10:48:29.482470
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule(None)
    assert am.TRANSFERS_FILES == False

# Generated at 2022-06-13 10:48:31.082086
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Unit test for method run of class ActionModule
    pass



# Generated at 2022-06-13 10:48:32.253617
# Unit test for constructor of class ActionModule
def test_ActionModule():
    obj = ActionModule()


# Generated at 2022-06-13 10:48:32.880937
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule

# Generated at 2022-06-13 10:48:41.280656
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Mock the Task class and its args attribute
    Task = type('Task', (object,), {})
    task_args = {'jinja2_native': True, 'cacheable': False,
                 'foo': 'bar', 'baz': 'qux', 'quux': 'quuz',
                 'corge': 'grault'}
    Task.args = task_args

    # Create a 'fake' task
    task = Task()
    task.args = task_args

    # Create the action plugin
    action = ActionModule(task, None, None, None)

    # Assert that the 'foo' key in args is an identifier
    assert isidentifier(task.args['foo'])

    # Assert that the action plugin will have a result
    assert action.run()

# Generated at 2022-06-13 10:48:42.456359
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule is not None

# Generated at 2022-06-13 10:48:51.682634
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.vars.manager import VariableManager
    from ansible.playbook.task import Task

    mock_loader = 'ansible.plugins.action.test_moduletest'

    task = Task()
    task.args = {'testvar': 'testval'}
    tqm = None

    moduletest_instance = ActionModule(loader=mock_loader, task=task, connection=None, play_context=None, loader_cache=dict(), templar=None, shared_loader_obj=None)

    assert moduletest_instance.TRANSFERS_FILES == False

    variable_manager = VariableManager()
    variable_manager.extra_vars = {'test_variable_manager': 'test_value'}

    result = moduletest_instance.run(task_vars=variable_manager)


# Generated at 2022-06-13 10:48:54.294674
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(None, None, None, None)
    assert action_module is not None

# Generated at 2022-06-13 10:52:05.481723
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module_args = dict(
        a=dict(
            required=True,
            type='dict',
            aliasses=['b']
        ),
        b=dict(
            required=True,
            type='dict',
            aliasses=['a']
        )
    )
    am = ActionModule(dict(a=1, b=2, c=3), dict(module_args=module_args))
    assert am.update_task_args(dict(a=4)) == dict(a=4, b=2, c=3)

# Generated at 2022-06-13 10:52:12.607299
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.role import Role
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager

    from units.mock.loader import DictDataLoader

    play_context = {}
    play_context.update({"become": True})
    play_context.update({"become_method": "sudo"})
    play_context.update({"tags": []})

    def dummy_loader(self, path):
        return {"foo": "bar"}

    mock_loader = DictDataLoader({"hello": "world"})
    mock_loader.load_from_file = dummy_loader
