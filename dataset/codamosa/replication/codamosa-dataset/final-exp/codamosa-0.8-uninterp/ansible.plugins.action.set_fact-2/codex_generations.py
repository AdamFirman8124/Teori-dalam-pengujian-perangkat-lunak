

# Generated at 2022-06-13 10:42:27.416245
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action = ActionModule()
    action.connection = MockConnection()
    action.action = 'test'
    action.action_getval = lambda x: x
    action.module = MockModule()
    action.runner = MockRunner()

    # test with minimal options
    action.runner.task = action.runner.task_class()
    action.runner.task.action = 'test'

    result = action.run(task_vars={'ansible_facts': {}})
    # there should be a single result: ansible_facts
    assert len(result) == 1
    # it should have 2 entries
    assert len(result['ansible_facts']) == 2
    # make sure we have the correct entries
    assert result['ansible_facts']['yes'] is True
    assert result['ansible_facts']['no']

# Generated at 2022-06-13 10:42:39.697643
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from mock import Mock, patch
    from ansible.module_utils import basic
    from ansible.module_utils.six import BytesIO
    from ansible.module_utils.parsing.convert_bool import boolean

    # constructor

# Generated at 2022-06-13 10:42:48.579922
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.module_utils.parsing.convert_bool import boolean
    from ansible.plugins.loader import action_loader

    module_args = dict(
        a=dict(b=4, c='d'),
        e='f',
        g=True,
        cacheable=False,
    )
    task_vars = dict()
    action = action_loader.get('set_fact', task=dict(action=dict(name='set_fact', args=module_args), args=module_args), connection=None, play_context=dict(), loader=None, templar=None, shared_loader_obj=None)
    result = action.run(None, task_vars=task_vars)

# Generated at 2022-06-13 10:42:58.605017
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.executor.task_result import TaskResult

    class TestActionModule(ActionModule):
        def run(self, tmp=None, task_vars=None):
            if task_vars is None:
                task_vars = dict()
            result = super(ActionModule, self).run(tmp, task_vars)
            return result

    class TestExecutor(object):
        def __init__(self):
            self.tasks = []

        def queue_task(self, host, task, task_vars, play_context):
            self.tasks.append((host, task, task_vars, play_context))

    # NOTE: these are NOT the same as in test_convert_bool

# Generated at 2022-06-13 10:43:07.443101
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils.basic import AnsibleModule


# Generated at 2022-06-13 10:43:15.389877
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # initializing some test data
    action = ActionModule()
    action._templar = 'Not a tmplar'
    action._task = 'Not a task'
    action._task.args = 'Not a task arg'

    # begin of test_run_task_vars
    # assert TypeError is raised if task_vars is not a dict
    try:
        action.run(tmp='', task_vars='task_vars')
    except TypeError:
        pass
    else:
        assert False
    # end of test_run_task_vars

    # begin of test_run_tmp
    # assert __Call__ method of AnsibleActionFail is called if tmp is not empty
    try:
        action.run(tmp='tmp', task_vars={})
    except AnsibleActionFail:
        pass

# Generated at 2022-06-13 10:43:18.237934
# Unit test for constructor of class ActionModule
def test_ActionModule():
    print("Testing ActionModule constructor")
    a = ActionModule()
    print("%s" % a)
    print("")

# Testing if this module works as a standalone script
if __name__ == '__main__':
    test_ActionModule()

# Generated at 2022-06-13 10:43:28.370136
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager

    play_source = dict(
        name="Ansible Play",
        hosts='localhost',
        gather_facts='no',
        tasks=[
            dict(action=dict(module='dynamic_vars', args=dict(cacheable=True, foo='bar', baz=42, quux='{{ ansible_date_time.epoch }}'))),
            dict(action=dict(module='debug', args=dict(msg='{{ foo }} {{ baz }} {{ quux }}'))),
        ]
    )

    play = Play().load(play_source, variable_manager={}, loader=None)



# Generated at 2022-06-13 10:43:38.657786
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    class TestActionModule(ActionModule):
        pass
    action_module = TestActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

    try:
        action_module.run(tmp=None, task_vars=None)
    except Exception as e:
        assert(type(e) == AnsibleActionFail)
        assert(str(e) == 'No key/value pairs provided, at least one is required for this action to succeed')

    try:
        action_module.run(tmp=None, task_vars=dict(test='test'))
    except Exception as e:
        assert(type(e) == AnsibleActionFail)
        assert(str(e) == 'Unable to create any variables with provided arguments')


# Generated at 2022-06-13 10:43:51.208914
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task

    task = Task()
    task._role = None
    task_ds = dict()

    pb_ds = dict()
    task_ds['vars'] = dict()
    pb_ds['vars'] = dict()

    pc = PlayContext()

    am = ActionModule(task, pc, task_ds, pb_ds)

    assert am._task.__class__.__name__ == 'Task'
    assert am._play_context.__class__.__name__ == 'PlayContext'
    assert am._loader.__class__.__name__ == 'DataLoader'
    assert am._templar.__class__.__name__ == 'Templar'

# Generated at 2022-06-13 10:44:08.975409
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Create mock objects

    # Create mock module
    module = AnsibleModule(
        argument_spec=dict(
            cacheable=dict(required=False, type='bool', default=False),
            key1=dict(required=False, type='str', default=None),
        ),
        supports_check_mode=True
    )

    # Create mock task
    task = AnsibleTask()

    # Create mock play context
    pc = AnsiblePlayContext()

    # Create mock loader
    loader = AnsibleLoader()

    # Create mock variable manager
    variable_manager = AnsibleVariableManager()
    variable_manager._fact_cache = dict()
    variable_manager._extra_vars = dict()
    variable_manager._options = dict()

    # Create mock templar
    templar = AnsibleTemplar()

   

# Generated at 2022-06-13 10:44:16.750537
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.task import Task

    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager

    from ansible.executor.playbook_executor import PlaybookExecutor

    from ansible.inventory.manager import InventoryManager

    from ansible.vars.manager import VariableManager

    from ansible.parsing.dataloader import DataLoader

    from ansible.utils.vars import load_extra_vars
    from ansible.errors import AnsibleActionFail

    # Create a test ActionModule with a mocked PlayContext.
    # This allows us to easily create hosts, and change the connection
    # method.
    class TestActionModule(ActionModule):
        def __init__(self, *args, **kwargs):
            self._play

# Generated at 2022-06-13 10:44:26.517793
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes
    DataLoader = basic.DataLoader
    OptionParser = basic.AnsibleOptionParser
    CommandLine = basic.AnsibleCommandLine
    # Create necessary objects
    (options, args) = OptionParser().parse_args()
    loader = DataLoader()
    cmdline = CommandLine(args)
    task = cmdline.get_task()
    # Set first argument to actions/set_fact
    args.insert(0, "set_fact")
    # Set action
    task.set_action(args[0])
    # Set module args

# Generated at 2022-06-13 10:44:33.117565
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = AnsibleAction()
    action._task.args   = dict(name='test')
    action._task.action = 'set_fact'
    action._task.no_log = True
    action._task.action = 'set_fact'
    result = action.run(tmp='/tmp/test', task_vars=dict(foo='bar'))
    assert result['ansible_facts']['name'] == 'test'
    assert result['_ansible_facts_cacheable'] == False

# Generated at 2022-06-13 10:44:34.584728
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule is not None, "Failed to import Ansible module."

# Generated at 2022-06-13 10:44:38.893053
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule(load_module_spec=False, task=dict(args=dict(ansible_facts=dict(test_value="test"))))
    result = module.run()
    assert result['changed'] is False
    assert result['ansible_facts']['test_value'] == "test"

# Generated at 2022-06-13 10:44:40.961680
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule(None, None, None)

    assert isinstance(am, ActionBase)
    assert hasattr(am, 'run')


# Generated at 2022-06-13 10:44:54.531982
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.task import Task
    from ansible.plugins.strategy import StrategyBase
    from ansible.utils.listify import listify_lookup_plugin_terms
    from ansible.template import Templar
    from ansible.utils.vars import merge_hash

    loader = DataLoader()
    variable_manager = VariableManager()
    variable_manager.extra_vars = {
    }
    variable_manager.options

# Generated at 2022-06-13 10:45:05.347499
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import ansible.errors
    import ansible.module_utils.parsing.convert_bool
    import ansible.module_utils.six
    import ansible.template
    import ansible.utils.vars
    import sys
    import unittest

    # Syntax sugar

# Generated at 2022-06-13 10:45:14.421099
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task import Task
    from ansible.playbook.role import Role
    from ansible.playbook.block import Block
    from ansible.playbook.play import Play
    from ansible.playbook.playbook import Playbook
    from ansible.module_utils.parsing.convert_bool import boolean

    role = Role().load({
        'name': 'test',
        'tasks': [{
            'action': 'set_fact',
            'name': {'var': 'var'},
            'value': {'val': 'val'}
        }]
    }, loader=None, variable_manager=None)


# Generated at 2022-06-13 10:45:29.205219
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Initializing ActionModule class
    actionModule = ActionModule(
        task=dict(args=dict(myvar=True, myothervar=False, mystring='mystring', mynumber='12345')),
        connection=None,
        play_context=None,
        loader=None,
        templar=None,
        shared_loader_obj=None
    )

    # Starting tests
    assert len(actionModule.run()['ansible_facts']) == 4

# Generated at 2022-06-13 10:45:40.337851
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.utils.vars import combine_vars
    args = {'pattern': 'hostvars'}
    action = ActionModule(None, args, {})
    mock_task_vars = {
        'hostvars': {},
        'group_names': [],
        'groups': {},
        'omit': 'omitted_vars',
    }
    combine_vars(action._task.vars, action._templar._available_variables)
    ret = action.run(None, mock_task_vars)
    assert ret['ansible_facts'] == {'hostvars': {}}

# Generated at 2022-06-13 10:45:43.842067
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Create an instance of class ActionModule
    am = ActionModule(
        task=dict(),
        connection=dict(),
        play_context=dict(),
        loader=None,
        templar=None,
        shared_loader_obj=None)

    assert isinstance(am, ActionModule)
    assert isinstance(am, ActionBase)


# Generated at 2022-06-13 10:45:50.027471
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Testing the import of ActionBase
    from ansible.plugins.action import ActionBase
    from ansible.plugins.action.set_fact import ActionModule
    from ansible.module_utils.six import string_types

    action_base = ActionBase()
    action_set_fact = ActionModule()

    # Testing the presence of function 'run' and its existence.
    assert action_set_fact.run()

# Generated at 2022-06-13 10:45:55.334709
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action = ActionModule()
    module_args = {
        'ansible_facts': {
            'custom_var': True
        }
    }

    # TODO: Use real objects instead of possibly brittle hard-coded strings for these tests
    # Subclass instead of mocks
    action._task.args = module_args
    action.run(task_vars={})

    # TODO: Assert that this looks like the thing we wanted
    print(action.result)


if __name__ == '__main__':
    test_ActionModule_run()

# Generated at 2022-06-13 10:46:04.179367
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import json
    import sys
    import ansible.utils.module_docs as mod_docs

    import ansible.modules.system.set_fact

    # Create the class to test
    ActionModuleTest = ActionModule(
        ansible.modules.system.set_fact.ActionModule.__name__,
        ansible.modules.system.set_fact.ActionModule.argspec,
        ansible.modules.system.set_fact.ActionModule.supports_check_mode,
        ansible.modules.system.set_fact.ActionModule.deprecated,
        ansible.modules.system.set_fact.ActionModule.no_log,
        ansible.modules.system.set_fact.ActionModule.__doc__,
        ansible.modules.system.set_fact.ActionModule.__dict__,
    )

    #

# Generated at 2022-06-13 10:46:05.735947
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule({},{}).run({},{}) == {}

# Generated at 2022-06-13 10:46:08.114673
# Unit test for constructor of class ActionModule
def test_ActionModule():
    try:
        myplugin = ActionModule()
    except Exception as e:
        print('ActionModule: exception: %s' % repr(e))
        assert False



# Generated at 2022-06-13 10:46:15.562896
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """Unit test for method run of class ActionModule"""
    import ansible.constants as C
    import ansible.plugins.action as action # Module under test
    import ansible.module_utils.parsing.convert_bool as convert_bool # Mocked for testing
    import sys # Mocked for testing
    import os # Mocked for testing
    import re # Mocked for testing
    from ansible.utils.vars import isidentifier # Mocked for testing
    from ansible.utils.unicode import to_unicode # Mocked for testing
    from ansible.context import CLIContext # Mocked for testing
    from ansible.template import Templar # Mocked for testing
    from ansible.executor.task_queue_manager import TaskQueueManager # Mocked for testing
    from ansible.executor.process.worker import WorkerProcess

# Generated at 2022-06-13 10:46:20.981790
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.handler import Handler
    from ansible.playbook.role import Role
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_result import TaskResult


# Generated at 2022-06-13 10:46:38.716143
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(None, {}, {}, 'debug')
    assert action_module


# Generated at 2022-06-13 10:46:49.914870
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import ansible.config.manager
    from ansible.utils.vars import combine_vars

    def _load_plugins(directory):
        ansible.config.manager._PLUGIN_PATH = directory
        ansible.config.manager.C.DEFAULT_MODULE_PATH = directory
        ansible.config.manager.C.DEFAULT_ACTION_PLUGIN_PATH = directory
        ansible.config.manager.C.DEFAULT_CACHE_PLUGIN_PATH = directory
        ansible.config.manager.C.DEFAULT_CALLBACK_PLUGIN_PATH = directory
        ansible.config.manager.C.DEFAULT_CONNECTION_PLUGIN_PATH = directory
        ansible.config.manager.C.DEFAULT_LOOKUP_PLUGIN_PATH = directory

# Generated at 2022-06-13 10:46:58.518078
# Unit test for constructor of class ActionModule
def test_ActionModule():
    class MockTask:
        def __init__(self, args):
            self.args = args
    class MockTemplar:
        def __init__(self):
            pass
        def template(self, value):
            return value
    class MockPlayContext:
        def __init__(self):
            self.check_mode = False
            self.prompt = None
            self.become = None
            self.become_user = None
            self.set_fact = {}
            self.set_uid = None
            self.set_gid = None
            self.set_env = False

    with pytest.raises(AnsibleActionFail) as excinfo:
        # No task args
        args = {}
        templar = MockTemplar()
        play_context = MockPlayContext()

# Generated at 2022-06-13 10:47:08.860472
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.executor.task_queue_manager import TaskQueueManager

    # All these should be true, may as well put them here
    assert isidentifier('foo')
    assert isidentifier('_foo')
    assert isidentifier('foo2')
    assert isidentifier('_foo2')

    # These should fail, may as well put them here
    assert not isidentifier('')
    assert not isidentifier('2foo')
    assert not isidentifier('Foo')
    assert not isidentifier('2')
    assert not isidentifier('foo-bar')
    assert not isidentifier('foo bar')
    assert not isidentifier('foo....bar')
    assert not isidentifier('foo.bar')

# Generated at 2022-06-13 10:47:09.742160
# Unit test for constructor of class ActionModule
def test_ActionModule():
    ActionModule(1,2,3, None)

# Generated at 2022-06-13 10:47:12.679714
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert False is boolean("false")
    assert False is boolean("0")
    assert True is boolean("true")
    assert True is boolean("1")


# Generated at 2022-06-13 10:47:18.279062
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    tmp = None
    task_vars = {'ansible_forks': 10}
    result = action_module.run(tmp, task_vars)
    assert result == {'ansible_facts': {}, '_ansible_facts_cacheable': False, 'failed': True}

# Generated at 2022-06-13 10:47:18.943451
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True

# Generated at 2022-06-13 10:47:32.638987
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils._text import to_bytes
    from ansible.plugins.loader import action_loader
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    # Replace the get_action_classmethod with a method providing our test class
    # This obviously only works if the method is not already patched
    try:
        action_class_getter = action_loader.get_action_class
        action_loader.get_action_class = lambda *args, **kwargs: ActionModule
    except AttributeError:
        pass

    module_name = 'test_ActionModule'
    loader = DataLoader()
    variable_manager = VariableManager()

# Generated at 2022-06-13 10:47:40.859538
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # function create_task is used to avoid circular reference problem with module_utils.facts
    # This function is available from module_utils.facts
    def create_task(values):
        task = AnsibleTask()
        task.args = values
        task._task.action = 'set_fact'

        return task

    # ActionModule object
    test_obj = ActionModule()

    # Empty args
    result = test_obj.run(tmp=None, task_vars=None)
    assert result['failed']
    assert result['msg'] == 'No key/value pairs provided, at least one is required for this action to succeed'

    # valid
    result = test_obj.run(tmp=None, task_vars=None, args={'a': 'b', 'c': 'd'})
    assert not result['failed']

# Generated at 2022-06-13 10:48:18.139134
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert isinstance(module, ActionBase)

# Generated at 2022-06-13 10:48:22.687805
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # will fail because no valid module
    data = dict(ANSIBLE_MODULES='ansible.modules.test_module')
    a = ActionModule(data, dict(module_name=['test_module']))

# Generated at 2022-06-13 10:48:25.260212
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert issubclass(ActionModule, ActionBase)
    action_mod = ActionModule(None, None, None, None)
    assert action_mod is not None

    assert action_mod._supports_async == False


# Generated at 2022-06-13 10:48:29.447612
# Unit test for constructor of class ActionModule
def test_ActionModule():
    a = ActionModule(None, None, task_vars={})
    assert a.plugin_type == 'action'
    assert a.name == 'set_fact'
    assert a.short_desc == 'set host facts from a task'
    assert a.version == '1.0'
    assert a.TRANSFERS_FILES is False
    assert a._task.args == {}


# Generated at 2022-06-13 10:48:31.486989
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule(None, None, None, None, None)
    assert action is not None

# Generated at 2022-06-13 10:48:33.531116
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule(None, None)
    assert action.TRANSFERS_FILES is False

# Generated at 2022-06-13 10:48:35.539198
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """Unit test for constructor of class ActionModule"""
    action = ActionModule(None)
    assert action is not None

# Generated at 2022-06-13 10:48:42.921308
# Unit test for constructor of class ActionModule
def test_ActionModule():
    class TestModule:
        def __init__(self):
            self.args = None
            self.tmp = None
            self.task_vars = None

    class TestTemplar:
        def __init__(self):
            self.template = None

    class TestTask:
        def __init__(self):
            self.args = None

    tm = TestModule()
    tm.args = {'a': 1, 'cacheable': False}

    ts = TestTemplar()
    tt = TestTask()

    am = ActionModule(tm, ts, tt, 'setup')
    res = am.run(tmp=1, task_vars=2)

    assert 'ansible_facts' in res
    assert res['ansible_facts'] == {'a': 1}

# Generated at 2022-06-13 10:48:52.011189
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action = ActionModule()
    action._task.args = dict(testvalue="test")
    action._task.action = "testaction"
    action._task.action_args = "testactionargs"
    action._task.action_stack = []
    action._task.action_show_args = True
    action._task.args = dict(testvalue="test")
    action._task.args = dict(testvalue="test")
    action._task.async_val = 0
    action._task.async_poll_interval = 1
    action._task.async_seconds = 0
    action._task.cleanup = False
    action._task.cleanup_default_handler = False
    action._task.connection = "testconnection"
    action._task.connection_port = 22
    action._task.created_at = 0

# Generated at 2022-06-13 10:49:01.964832
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import unittest

    from ansible.playbook.task import Task

    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager

    from ansible.utils.vars import combine_vars

    from ansible.plugins.action.set_fact import ActionModule

    class TestActionModule(unittest.TestCase):

        def setUp(self):
            task = Task()
            task.args = {}
            self.task = task

        def tearDown(self):
            pass

        def test_ActionModule(self):

            action = ActionModule(None, task=self.task, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

# Generated at 2022-06-13 10:50:44.047707
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import json
    import bigpackage.bigmodule
    from ansible.plugins.action import ActionModule
    from ansible.plugins.action.set import ActionModule as SetActionModule
    from ansible.utils.vars import HackyLoader

    fake_tas = bigpackage.bigmodule.ActionModule
    fake_tas.run = ActionModule.run
    args = dict(
        ANSIBLE_MODULE_ARGS={
            'name': 'one',
            'state': 'present',
            'quorum': True,
            'non_identifier': 'foo.bar'
        },
        ANSIBLE_MODULE_CONSTANTS={
        },
        MODULE_NAME='bigip_pool',
        DEFAULT_VAULT_ID='abcd1234'
    )

# Generated at 2022-06-13 10:50:53.500089
# Unit test for constructor of class ActionModule
def test_ActionModule():
    mock_task = MockTask()
    mock_task.action = 'set_fact'
    mock_task_vars = {}

    mock_ansible_mod = MockAnsibleModule()
    mock_ansible_mod._ansible_module = mock_ansible_mod
    mock_ansible_mod._ansible_module._ansible_module = mock_ansible_mod
    mock_ansible_mod.no_log = False

    action_plugin = ActionModule(mock_ansible_mod, mock_task, mock_task_vars)

    assert issubclass(action_plugin.__class__, ActionBase)
    assert action_plugin.TEMP_PATH == '/tmp'
    assert action_plugin.TRANSFERS_FILES == False



# Generated at 2022-06-13 10:50:54.013617
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule

# Generated at 2022-06-13 10:50:54.818076
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule()
    del am

# Generated at 2022-06-13 10:51:01.245989
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import unittest2 as unittest

    class TestActionModule(unittest.TestCase):

        def setUp(self):
            import ansible.utils.vars
            self.variables = ansible.utils.vars.VarsModule()

        def tearDown(self):
            self.variables = None

        def test_ActionModule_run_missing_key_value(self):
            from ansible.plugins.action import ActionModule
            # no key/value arguments provided

# Generated at 2022-06-13 10:51:13.202475
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.utils.vars import merge_hash
    import ansible.module_utils.facts as ansible_facts
    from ansible.plugins.action import ActionModule
    from ansible import context

    # test with parameters
    context.CLIARGS = {'_ansible_cache': False}
    test = ActionModule(dict(ANSIBLE_MODULE_ARGS={'name1': 'value1', 'name2': 'value2'}), playbook=None)
    test.run()
    assert (test._task.args == {'name1': 'value1', 'name2': 'value2'})

    # test with 1 parameter
    context.CLIARGS = {'_ansible_cache': False}

# Generated at 2022-06-13 10:51:14.833021
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # test the constructor of ActionModule
    am = ActionModule( {}, {})
    assert isinstance(am, ActionModule)

# Generated at 2022-06-13 10:51:15.322877
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass # TODO

# Generated at 2022-06-13 10:51:15.831230
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert False

# Generated at 2022-06-13 10:51:17.061982
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule()
    assert am is not None
