

# Generated at 2022-06-13 09:55:25.783610
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    from ansible.utils.vars import combine_hash

    # Create the class object for this test.
    action_obj = ActionModule(
        connection=None,
        task=None,
        executor=None,
        loader=None,
        templar=None,
        shared_loader_obj=None)

    assert action_obj is not None

# Generated at 2022-06-13 09:55:33.745095
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """
    :type tmp: Tempfile
    :type task_vars: dict
    """

    import tempfile

    tmp = tempfile.NamedTemporaryFile()
    task_vars = {}
    action_module = ActionModule()

    result = action_module.run(tmp=tmp, task_vars=task_vars)

    assert isinstance(result, dict)
    assert result.get('ansible_facts', dict()).get('_ansible_facts_gathered') is True



# Generated at 2022-06-13 09:55:35.520260
# Unit test for constructor of class ActionModule
def test_ActionModule():

    # Execute constructor
    am = ActionModule()
    assert am



# Generated at 2022-06-13 09:55:36.284148
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 09:55:45.030501
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Context for test dummy play
    module_args = {
        'test': 'test'
    }
    task_vars = {
        'ansible_facts': {}
    }

    # Dummy play
    play = dict(
        name="Test Play",
        gather_facts='smart',
        hosts=['all'],
        tasks=[
            dict(
                action=dict(
                    module="dummy",
                    args=module_args
                ),
                register="dummy"
            ),
            dict(
                action=dict(
                    module="setup",
                    args=module_args
                ),
                register="setup"
            )
        ]
    )

    pb = ActionModule(play, task_vars)

    # Playbook execution
    result = pb.run()
    assert not result.get

# Generated at 2022-06-13 09:55:55.815682
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    try:
        from ansible.module_utils._text import to_text
    except (ImportError, AttributeError):
        from ansible.utils.unicode import to_text

    from ansible.module_utils.facts import default_collectors

    class ModuleStub(object):
        def __init__(self):
            self.params = {}
            self._name = None
            self._task = {}
            self._args = {}
            self._module_name = 'setup'
            self._connection = 'local'

        def _execute_module(self, module_name, module_args, task_vars=None, wrap_async=False):
            module_name = module_name.replace('ansible.base_facts.BaseFactsCollector', 'ansible.base_facts.ActionModule')
            return module_name

# Generated at 2022-06-13 09:56:01.674608
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    import sys
    import unittest
    import argparse

    class MockConfig(object):
        class MockConfigParser(object):
            def __init__(self):
                self.f = ['none']

            @staticmethod
            def read(path, encoding='utf-8'):
                return

        class ConfigParser(object):
            def __init__(self):
                self.config = self.MockConfigParser()

        def get_config_value(self, a, variables=None):
            if a == 'FACTS_MODULES':
                return ['fake_fact']
            if a == 'CONNECTION_FACTS_MODULES':
                return {'ansible_connection': 'fake_fact'}
            if a == 'DEFAULT_EXECUTABLE':
                return 'echo %s'


# Generated at 2022-06-13 09:56:02.796910
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    print("Test ActionModule")
    print("Method run")

# Generated at 2022-06-13 09:56:04.540625
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(None, None, None, {})
    assert module

# Generated at 2022-06-13 09:56:13.944573
# Unit test for constructor of class ActionModule
def test_ActionModule():
    args = dict(
        ansible_facts_parallel=True,
        ansible_facts_module_name=['*'],
        ansible_facts_gather_subset='!all',
        ansible_facts_plugins='*',
        ansible_facts_gather_timeout=10
    )
    action = ActionModule(args, {})
    assert action.args['ansible_facts_parallel'] is True
    assert action.args['ansible_facts_module_name'] == ['*']
    assert action.args['ansible_facts_gather_subset'] == '!all'
    assert action.args['ansible_facts_plugins'] == '*'
    assert action.args['ansible_facts_gather_timeout'] == 10

# Generated at 2022-06-13 09:56:26.959575
# Unit test for constructor of class ActionModule
def test_ActionModule():
    my_mock = ActionModule()
    assert my_mock.my_action is True

# Generated at 2022-06-13 09:56:35.998790
# Unit test for constructor of class ActionModule
def test_ActionModule():
    try:
        loader = None
        templar = None
        shared_loader_obj = None
        action_base_obj = ActionBase()
        task = None
        connection = None
        play_context = None
        new_action_module_obj = ActionModule(loader, templar, shared_loader_obj, action_base_obj,
                                             task, connection, play_context, task_uuid='',
                                             final_q = action_base_obj._queue)
        print("Created ActionModule object successfully")
    except Exception as e:
        print("Failed to create ActionModule object due to exception:" + str(e))



# Generated at 2022-06-13 09:56:38.218122
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    am = ActionModule()
    result = am.run(task_vars={})
    assert result['ansible_facts'] != {}

# Generated at 2022-06-13 09:56:48.075523
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Note about this test:
    # 1. It's just to check the class method
    # 2. It does not cover all possible cases
    # 3. it does not work in a real env as it needs to mock call to ActionBase.run,


    # Create an instance of class ActionModule
    this = ActionModule({}, {}, {}, [])

    # Create a mocked instance of class AnsibleModule
    ansible_module = AnsibleModule(argument_spec={})
    # Create a mocked instance of class Play
    play = Play(name='test', hosts=[])
    # Create a mocked instance of class Task
    task = Task(name='test', play=play, action='action_plugin', args={})
    # Create a mocked instance of class PlayContext
    context = PlayContext()
    # Set connection for context

# Generated at 2022-06-13 09:56:58.249610
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule()
    module._display.verbosity = 4
    module._play_context = PlayContext()
    module._task = Task()
    module._task.action = 'setup'
    module._task.name = 'gather facts'
    module._task.args = dict(filter='ansible_distribution')
    module._shared_loader_obj = SharedPluginLoaderObj()
    module._shared_loader_obj.action_loader = SharedPluginLoaderObj()
    module._shared_loader_obj.action_loader.module_loader = ModuleLoader()
    module._shared_loader_obj.action_loader.module_loader.add_directory(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'playbook'))

# Generated at 2022-06-13 09:57:12.184087
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.executor.playbook_executor import PlayContext
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.vars import FailedVarsFilter
    from ansible.utils.display import Display
    loader = DataLoader()
    variable_manager = VariableManager()
    display = Display()

# Generated at 2022-06-13 09:57:15.276212
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # ActionModule.run(self, tmp=None, task_vars=None):
    # TODO: Write a unit test for this method
    pass

# Generated at 2022-06-13 09:57:15.895139
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 09:57:17.442712
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(task=dict(), connection=dict(), play_context=dict(), loader=dict(), templar=dict(), shared_loader_obj=dict()) is not None

# Generated at 2022-06-13 09:57:18.744076
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 09:57:46.554113
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Initialize objects for module run method
    action_module = ActionModule()
    action_module._shared_loader_obj = globals()['SharedLoaderObj']()
    action_module._connection = globals()['connection_data']()
    action_module._task = globals()['task_data']()
    action_module._loader = globals()['loader_obj']()
    action_module._templar = globals()['TemplarObj']()
    action_module._display = globals()['DisplayObj']()

    # Return value of method run
    result = action_module.run()

    # Assertion check for method run
    assert result['ansible_facts'] == {}
    assert result['_ansible_verbose_override'] == True

    # Return value of method _combine_task_result


# Generated at 2022-06-13 09:57:59.602495
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module_name = 'setup'
    module_args = {'filter': 'ansible_all_ipv4_addresses'}

    executor = None
    loader = None
    play = None
    action = None
    task = None
    task_vars = None
    tmp = None
    # If executor, loader, play, action, task and task_vars are not given they
    # are taken from the caller.
    # If tmp is not given, it is taken from 'C.DEFAULT_LOCAL_TMP'
    action_obj = ActionModule(
        executor=executor,
        loader=loader,
        play=play,
        action=action,
        task=task,
        task_vars=task_vars,
        tmp=tmp
    )


# Generated at 2022-06-13 09:58:05.857659
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    tmp = None
    task_vars = {}
    assert action_module.run(tmp, task_vars) == {
        '_ansible_verbose_override': True,
        'ansible_facts': {
            '_ansible_facts_gathered': True,
        },
        'failed': True,
        'failed_modules': {},
        'msg': 'The following modules failed to execute: \n',
        'skipped_modules': {},
    }

# Generated at 2022-06-13 09:58:16.667236
# Unit test for method run of class ActionModule

# Generated at 2022-06-13 09:58:18.267684
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # test instantiation
    am = ActionModule('local', {}, {}, {}, {})
    assert am

# Generated at 2022-06-13 09:58:19.278254
# Unit test for constructor of class ActionModule
def test_ActionModule():
    pass


# Generated at 2022-06-13 09:58:27.415703
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # FIXME : this test mostly check that it doesn't crash
    from ansible.plugins.loader import action_loader

    t = action_loader.get('setup', class_only=True)()

    t._initialize_sub_tasks()

    args = dict(
        gather_subset=['all'],
    )
    t._task_vars = dict(ansible_facts_parallel=False)

    result = t.run(tmp=None, task_vars=t._task_vars)
    assert result.get('ansible_facts')
    assert result.get('ansible_facts').get('_ansible_facts_gathered') is True

    t._task_vars = dict(ansible_facts_parallel=True)


# Generated at 2022-06-13 09:58:28.576329
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert callable(ActionModule)

# Generated at 2022-06-13 09:58:38.877552
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.executor.task_result import TaskResult
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.plugins.loader import connection_loader
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    import collections
    from ansible.vars.hostvars import HostVars
    from ansible.vars.hostvars import HostVarsVars
    import yaml


# Generated at 2022-06-13 09:58:42.459211
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''
    the run of class ActionModule
    '''
    module = ActionModule('test.yml')
    result = module.run(None, {"FACTS_MODULES": ["fact1", "fact2"]})
    print(result)

# Generated at 2022-06-13 09:59:37.214380
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.executor.task_executor import TaskExecutor
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.handler import Handler
    from ansible.playbook.play_context import PlayContext
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.utils.vars import combine_vars
    from ansible.utils.vars import combine_facts
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.vars import load_extra_vars
    from ansible.utils.vars import load_options_vars

# Generated at 2022-06-13 09:59:52.262982
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action = ActionModule()
    action._supports_check_mode = True
    task_vars = {"ansible_facts_parallel": True, "ansible_facts": {}, "connection": "local", "ansible_network_os": "ios"}
    modules = ["setup"]
    result = action.run(tmp=None, task_vars=task_vars)
    failed = {}
    skipped = {}
    for fact_module in modules:
        mod_args = action._get_module_args(fact_module, task_vars)
        res = action._execute_module(module_name=fact_module, module_args=mod_args, task_vars=task_vars, wrap_async=False)
        if res.get('failed', False):
            failed[fact_module] = res
            


# Generated at 2022-06-13 09:59:57.124622
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    mod = ActionModule()
    assert mod.run() == {
        'ansible_facts': {
            '_ansible_facts_gathered': True
        },
        'changed': False,
        'failed': False,
        'warnings': [
            'Using fallback module for \'ansible.legacy.setup\' as the requested '
            'module (ansible.legacy.setup) is not available.  This typically '
            'happens when this module is executed on a host that is expected to '
            'be managed by another Ansible control host.'
        ]
    }

# Generated at 2022-06-13 10:00:04.571719
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    list_modules = ['smart', 'ansible_network.legacy.ios', 'ansible_network.legacy.ios_facts']
    collection_list = ['ansible_network.network_plugins.ios',
                       'ansible_network.network_plugins.ios_facts'
                       'ansible_network.network_plugins.ios_config']
    class_ActionModule = ActionModule()
    class_ActionModule._task = 'setup'
    class_ActionModule._task.args = ['network_os', 'ios']
    class_ActionModule._task.collections = collection_list

# Generated at 2022-06-13 10:00:05.308683
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule is not None

# Generated at 2022-06-13 10:00:12.450867
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import ansible.plugins.action.setup as A
    tmp = None
    task_vars = dict(FACTS_MODULES=['ansible.legacy.setup', 'ansible.legacy.setup'])
    action_module = A.ActionModule(tmp, task_vars=task_vars)
    res = action_module.run(tmp, task_vars=task_vars)
    assert res['ansible_facts']['_ansible_facts_gathered'] == True
    assert res['failed'] == False
    assert res['msg'] == 'All items completed\n'
    task_vars = dict(FACTS_MODULES=['ansible.legacy.setup', 'ansible.legacy.setup'], parallel=True)

# Generated at 2022-06-13 10:00:22.691987
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    acm = ActionModule(None, dict(ansible_facts_parallel=None, parallel=None), False)
    acm.run(None, dict(config_value=["FACTS_MODULES", ["test_value1", "test_value2"]]))
    acm.run(None, dict(config_value=["FACTS_MODULES", ["test_value1", "test_value2"]], ansible_facts_parallel=True, parallel=False))
    acm.run(None, dict(config_value=["FACTS_MODULES", ["test_value1", "test_value2"]], ansible_facts_parallel=False, parallel=True))

# Generated at 2022-06-13 10:00:23.325003
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:00:30.600725
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # See https://github.com/ansible/ansible/blob/devel/lib/ansible/plugins/action/setup.py
    action_module = ActionModule()

    assert action_module._supports_check_mode is True
    assert action_module.argument_spec == dict()
    assert action_module.no_log is False
    assert action_module.mutually_exclusive is set()
    assert action_module.required_one_of is set()
    assert action_module.required_together is set()

# Generated at 2022-06-13 10:00:37.984307
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    task_vars = dict()
    tmp = None
    task_vars['ansible_connection'] = 'local'
    task_vars['ansible_bash_type'] = 'bash'
    task_vars['ansible_version']['full'] = 'v2.10'
    task_vars['ansible_version']['major'] = 2
    task_vars['ansible_version']['minor'] = 0
    task_vars['ansible_version']['revision'] = 1
    task_vars['ansible_version']['string'] = u'v2.10'
    task_vars['ansible_version']['timestamp'] = '2020-08-25 23:23:49.694803'

# Generated at 2022-06-13 10:02:35.820347
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.loader import connection_loader
    import ansible

    fact_modules = ['ansible.legacy.setup', 'ansible.legacy.extra_facts']
    # Test the execution of the method _get_module_args
    with open('test_ActionModule_run_out.txt', 'w') as f:
        f.write('Connection: localhost\n')
        f.write('Create a dict with the args to be passed to the module.\n')
        f.write('List of fact modules to be executed:\n')
        f.write(str(fact_modules))
        f.write('\n')
        for fact_module in fact_modules:
            f.write('Execute module: ')
            f.write(fact_module)
            f.write('\n')
            f.write

# Generated at 2022-06-13 10:02:40.792336
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import tempfile
    import ansible.plugins.action as action
    loader = ansible.loader.ActionLoader()
    env_vars = {}
    p = tempfile.mkdtemp()
    env_vars.update(dict(ANSIBLE_LIBRARY=p))
    env_vars.update(dict(ANSIBLE_MODULE_UTILS=p))
    #TODO: Add test for this class
    pass

# Generated at 2022-06-13 10:02:49.292850
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Dummy class for class ActionModule unit test
    class DummyActionModule:
        def __init__(self, tmp=None, task_vars=None):
            self.__dict__ = dict(tmp=None, task_vars=None)
            self.__dict__.update(tmp=tmp, task_vars=task_vars)

    # Dummy class for module ansible.plugins.action.setup
    class DummyModule:
        def __init__(self, module_name, module_args, task_vars, wrap_async, connection):
            self.__dict__ = dict(module_name=None, module_args=None, task_vars=None, wrap_async=None, connection=None)

# Generated at 2022-06-13 10:02:49.833822
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass # nothing to test

# Generated at 2022-06-13 10:02:51.142538
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule()
    assert(am is not None)

# Generated at 2022-06-13 10:03:00.561619
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils import basic
    from ansible.parsing.splitter import parse_kv
    from ansible.plugins.action import ActionBase
    from ansible.utils.vars import combine_vars

    class ModuleMock(object):
        def __init__(self, *args, **kwargs):
            self.args = args
            self.params = kwargs

    class TaskMock(object):
        def __init__(self, *args, **kwargs):
            self.args = args
            self.module = args[0]
            self.module_vars = args[1]
            self.no_log = False
            self.async_val = 10
            self.async_seconds = 1
            self.module_defaults = {}


# Generated at 2022-06-13 10:03:10.031410
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # print "test_Command run"
    #print "C.config", C.config
    #print "dir(C.config)", dir(C.config)
    C.config.set_config_value('FACTS_MODULES', ['ansible.legacy.setup'], '__ansible_builtin__')
    C.config.set_config_value('CONNECTION_FACTS_MODULES', {'network_cli': 'ansible.legacy.setup'}, '__ansible_builtin__')
    #print "C.config", C.config
    #print "dir(C.config)", dir(C.config)
    #print "C.config.get_config_value('FACTS_MODULES')", C.config.get_config_value('FACTS_MODULES')
   

# Generated at 2022-06-13 10:03:10.423152
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:03:10.788306
# Unit test for constructor of class ActionModule
def test_ActionModule():
    pass

# Generated at 2022-06-13 10:03:15.841295
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """Unit test for :class:`ActionModule` using internal functions and classes.

    :class:`ActionModule` is tested in ``test/integration/default/targets/test_setup_module.py``.
    """
    action_module = ActionModule(
        task=Task(),
        connection=Connection(),
        play_context=PlayContext(),
        loader=None,
        templar=None,
        shared_loader_obj=None
    )
