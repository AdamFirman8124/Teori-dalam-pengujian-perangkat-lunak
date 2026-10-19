

# Generated at 2022-06-13 10:26:54.257912
# Unit test for constructor of class ActionModule
def test_ActionModule():
	mod = ActionModule()
	mod.run()

# Generated at 2022-06-13 10:27:02.465255
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    print("test_ActionModule_run")
    from ansible import context
    from ansible.utils.display import Display
    display = Display()
    context._init_global_context(display)
 
    config_manager = context.CLIARGS._get_config_manager()
    display.verbosity = config_manager.verbosity
    tasks = [ {'action': { '__ansible_module__': 'service', '__ansible_arguments__': {'name': 'httpd','state': 'stopped','sleep': 3,'enable': True},'__ansible_action_args__': {'delimiters': ('{{', '}}')}},'async': 0,'delegate_to': '127.0.0.1'}]
    task = tasks[0] #FIXME - should be a mock object instead

    #

# Generated at 2022-06-13 10:27:03.849955
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''
    Unit test for constructor of class ActionModule.
    '''

    module = ActionModule()
    assert module is not None

# Generated at 2022-06-13 10:27:05.634992
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = ActionModule()
    action_module.run()
test_ActionModule_run()

# Generated at 2022-06-13 10:27:07.815347
# Unit test for constructor of class ActionModule
def test_ActionModule():
    #assert isinstance(ActionModule(), ActionModule)
    print("Unit test for test_ActionModule")
    assert True == True

# Generated at 2022-06-13 10:27:11.058895
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(task={'args': {'test_arg': 'test_value'}}, connection={}, play_context={}, loader={}, templar={}, shared_loader_obj={})
    assert action_module

# Generated at 2022-06-13 10:27:11.809584
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:27:22.621681
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ''' Unit test for method run of class ActionModule '''

    my_task = Mock()
    my_task.args = {'use': 'auto'}

    my_connection = Mock()
    my_connection.shell = Mock()
    my_connection.shell.tmpdir = "dir"

    my_play_context = Mock()
    my_play_context.become = True
    my_play_context.become_method = "sudo"
    my_play_context.become_user = "root"

    module = ActionModule(my_task, my_connection, my_play_context, loader=None, templar=None, shared_loader_obj=None)

    my_task.delegate_to = "host"

    my_task.delegate_to = None

    my_task.delegate_to

# Generated at 2022-06-13 10:27:33.317792
# Unit test for constructor of class ActionModule

# Generated at 2022-06-13 10:27:35.097240
# Unit test for constructor of class ActionModule
def test_ActionModule():
    pass

# Generated at 2022-06-13 10:27:51.024873
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule()
    module._task.args = {}
    module._task.args["name"] = "mariadb"
    module._task.args["state"] = "started"

    # Testing the case of success
    module._templar.template = Mock(return_value="ansible.legacy.service")
    module._shared_loader_obj.module_loader.has_plugin = Mock(return_value=True)
    module._shared_loader_obj.module_loader.find_plugin_with_context = Mock(return_value=True)
    module._execute_module = Mock(return_value={'failed': True})
    result = module.run()
    assert(type(result) == dict)
    assert(result['failed'] == True)

    # Testing the case of failure

# Generated at 2022-06-13 10:27:59.082971
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task import Task
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.inventory.host import Host
    from ansible.parsing.dataloader import DataLoader
    from ansible.module_utils.facts import ModuleArgsParser
    from ansible_collections.ansible.builtin import plugins as ansible_builtin_plugins

    playbook_path = 'test_playbook.yml'
    hosts = ['host1', 'host2']
    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, variable_manager=variable_manager, sources=None)

# Generated at 2022-06-13 10:28:11.590297
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import sys
    from ansible.utils.path import unfrackpath
    from ansible.parsing.dataloader import DataLoader

    my_loader = DataLoader()
    my_loader.set_vault_secrets([])

    def get_action_module_with_args(task, args):
        global action_plugin_class
        return action_plugin_class(task, args, load=my_loader)

    class Task(object):
        def __init__(self):
            self._parent = '_parent'
            self.delegate_to = 'delegate_to'
            self.args = {'use': 'auto'}
            self.async_val = 'async_val'
            self.module_defaults = {}


# Generated at 2022-06-13 10:28:22.403908
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    class MockResult(object):
        def update(self, value):
            pass
    from ansible.plugins.action import ActionBase
    from ansible.plugins import action
    mock = MockResult()
    module = action.ActionModule()
    module._supports_async = True
    module._supports_check_mode = True
    module._task = {
        'delegate_to': None,
        'args': {},
        'collections': [],
        'async_val': False,
        'module_defaults': {}
    }
    module._execute_module = lambda x, y, z, a: {'ansible_facts': {'service_mgr': 'auto'}}

# Generated at 2022-06-13 10:28:24.033335
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:28:39.310768
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import json
    import pytest
    from ansible.plugins.action.service import ActionModule
    from ansible.plugins.loader import add_all_plugin_dirs, find_plugin
    add_all_plugin_dirs()
    with open("tests/test_service_module_unit_test.json") as jsonfp:
        test_data = json.load(jsonfp)
        for test_case in test_data.get("test_case"):
            task=test_case.get("task")
            ansible_facts=test_case.get("ansible_facts")
            test_hostvars=test_case.get("hostvars")
            expected_result=test_case.get("expected_result")
            host_name=test_case.get("host_name")

# Generated at 2022-06-13 10:28:43.554747
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Create an instance of ActionModule named am
    am = ActionModule()
    # Check if the attribute _supports_check_mode of am is True
    assert am._supports_check_mode == True
    # Check if the attribute _supports_async of am is True
    assert am._supports_async == True



# Generated at 2022-06-13 10:28:48.739631
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule(None, None, None, None)
    assert isinstance(am.BUILTIN_SVC_MGR_MODULES, set)
    assert isinstance(am.UNUSED_PARAMS, dict)
    assert am.TRANSFERS_FILES == False

# Generated at 2022-06-13 10:28:50.768206
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule('/tmp/ansible_service_payload', dict(), False, 10, 'debug')
    assert am is not None

# Generated at 2022-06-13 10:29:02.438680
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action1 = ActionModule()
    assert action1._task is None
    assert action1._connection is None
    assert action1._tmp is None
    assert action1._loader is None
    assert action1._play_context is None
    assert action1._shared_loader_obj is None
    assert action1._templar is None
    assert action1._task_vars is None

    action2 = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert action2._task is None
    assert action2._connection is None
    assert action2._play_context is None
    assert action2._loader is None
    assert action2._templar is None
    assert action2._shared_loader_obj is None
    assert action2._task

# Generated at 2022-06-13 10:29:16.652255
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(task=dict(action=dict(service=dict(use='auto'))))

# Generated at 2022-06-13 10:29:17.281768
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True

# Generated at 2022-06-13 10:29:26.963022
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # create two ActionModule objects
    p = ActionModule(None, dict(name='service', use='auto'),
                     'service', None, None)
    p1 = ActionModule(None, dict(name='service', use='ansible.legacy.service'),
                     'service', None, None)
    # get the class of the two objects
    assert p.__class__.__name__ == 'ActionModule'
    assert p1.__class__.__name__ == 'ActionModule'
    # get the attributes of the two objects
    assert p._shared_loader_obj.module_loader.has_plugin('auto')
    assert not p1._shared_loader_obj.module_loader.has_plugin('ansible.legacy.service')

# Generated at 2022-06-13 10:29:31.350022
# Unit test for constructor of class ActionModule
def test_ActionModule():
    connection = object()
    display = object()
    task = object()
    shared_loader_obj = object()
    templar = object()
    result = object()
    action_module = ActionModule(connection, display, task, shared_loader_obj, templar, result)
    assert action_module._supports_async is True
    assert action_module._supports_check_mode is True
    assert action_module is not None

# Generated at 2022-06-13 10:29:37.626763
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''
    Unit test for constructor of class ActionModule
    '''
    # Invalid instantiation
    action_module = ActionModule(task=dict(), connection=dict(), play_context=dict(), loader=dict(),
                                 templar=dict(), shared_loader_obj=dict())
    assert action_module is not None


# Generated at 2022-06-13 10:29:38.497121
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:29:51.343105
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    task_vars = {'ansible_facts': {'service_mgr': 'systemd'}}
    task = MagicMock()
    task.async_val = False
    task.args = {'name': 'foo', 'state': 'started', 'use': 'auto'}
    task.delegate_to = None
    task._parent = MagicMock()
    task._play = MagicMock()
    task._play._action_groups = {'all': [[]]}
    action = ActionModule(task, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    action._execute_module = mock.Mock(return_value={'changed': False, 'rc': 0, 'module_executed': 'unit_test'})
    action._remove_tmp

# Generated at 2022-06-13 10:30:05.058225
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import ansible.utils.module_docs as module_docs

    # Initialize Ansible's context singleton
    from ansible.context import CLIContext
    from ansible.cli import CLI
    from ansible.utils.display import Display
    from ansible.errors import AnsibleError
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.inventory.manager import InventoryManager
    from ansible.plugins.loader import action_loader
    from ansible.plugins.connection import ConnectionBase
    from ansible.vars.manager import VariableManager
    C = CLIContext()

    # Initialize Ansible's context singleton
    display = Display()
    connection = ConnectionBase()

# Generated at 2022-06-13 10:30:19.838792
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    "Tests run() of class ActionModule"

    # Initialization of local variables for test
    loader = DictDataLoader({})
    variable_manager = VariableManager()
    inventory = Inventory(loader, variable_manager, host_list=[])
    variable_manager.set_inventory(inventory)

    # Initialization of class object to test

# Generated at 2022-06-13 10:30:29.048887
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.play_iterator import PlayIterator
    from ansible.inventory import Inventory

    from ansible.vars.manager import VariableManager
    from ansible.playbook.play import Play
    from ansible.plugins.strategy.linear import StrategyModule

    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.vars import merge_hash

    from ansible.playbook.block import Task
    from ansible.playbook.block import Block

    loader = DataLoader()
    inventory = Inventory(loader=loader, variable_manager=VariableManager(), host_list=[])
    variable_manager = VariableManager(loader=loader, inventory=inventory)


# Generated at 2022-06-13 10:31:14.458070
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import ansible.module_utils.facts

# Generated at 2022-06-13 10:31:24.271375
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.module_utils.basic import AnsibleModule
    import ansible.plugins.action
    import ansible.playbook.play_context
    import ansible.playbook.task_include
    import ansible.template
    import ansible.vars.manager

    module_loader, md = ansible.plugins.action.resolve_action_plugin("service", "", "", "", "", "", None, None, ansible.plugins.action._shared_loader_obj)

    assert md.__class__.__name__ == 'ActionModule'
    assert md.run.__class__.__name__ == 'function'

    # construct object with all None values
    md = ActionModule(None, None, None, None, None, None, None, None, None, None)

    # construct object

# Generated at 2022-06-13 10:31:24.609493
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule()

# Generated at 2022-06-13 10:31:33.375994
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''unit test for method run of class ActionModule'''
    from ansible.module_utils.six import StringIO, PY3
    from ansible.module_utils._text import to_text
    from ansible.module_utils.pycompat24 import get_exception
    #from ansible.module_utils.basic import AnsibleModule, set_module_args
    from ansible.plugins.action.service import ActionModule


# Generated at 2022-06-13 10:31:42.980779
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    actionModule_obj = ActionModule()

# Generated at 2022-06-13 10:31:44.469425
# Unit test for constructor of class ActionModule
def test_ActionModule():
    mod = ActionModule(None, None)


# Generated at 2022-06-13 10:31:54.560624
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ############################################################
    # Test:
    ############################################################
    # Case 1.1
    ############################################################
    module = ActionModule()
    module._shared_loader_obj = 'dummy'
    task = FakeTask()
    task._parent = 'dummy'
    task._play = 'dummy'
    module._task = task
    module._templar = 'dummy'
    module._supports_check_mode = True
    module._supports_async = True
    task_vars = 'dummy'
    result = module.run(tmp=None, task_vars=task_vars)
    assert result['failed']
    assert result['msg']
    assert not result['invocation']['module_args'].get('use')

# Mock class for FakeTask

# Generated at 2022-06-13 10:31:56.118598
# Unit test for constructor of class ActionModule
def test_ActionModule():
    ab = ActionBase()
    assert ab._supports_check_mode is False

# Generated at 2022-06-13 10:32:01.201302
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Example code for run method of class ActionModule
    # Note: this code is just a dummy example.
    # action = ActionModule(task=task, connection=connection, play_context=play_context, loader=loader, templar=templar, shared_loader_obj=shared_loader_obj)
    # result = action.run(task_vars=task_vars)
    pass


# Generated at 2022-06-13 10:32:02.091438
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:33:01.103934
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Constructor test
    # action = ActionModule({}, {}, "localhost", "test", "")
    assert False is True

# Generated at 2022-06-13 10:33:10.477389
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.action.service import ActionModule
    from ansible.executor import module_common
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.utils.collection_loader import AnsibleCollectionLoader
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.module_utils.common.removed import removed_module, removed_class

    assert removed_module('ansible.parsing.yaml.objects') is not None, \
            "ActionModule unit tests require 'ansible.parsing.yaml.objects' removed to be imported"

# Generated at 2022-06-13 10:33:12.112013
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible import context
    context._init_global_context(['ansible-playbook'])
    assert isinstance(ActionModule(None, None, None, None), ActionModule)

# Generated at 2022-06-13 10:33:18.770400
# Unit test for method run of class ActionModule

# Generated at 2022-06-13 10:33:26.415703
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """
    Print the functions/methods in this class
    """
    action = ActionModule(connection=None, task=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    print(action.run(tmp=None, task_vars=None))


if __name__ == '__main__':
    # Unit test
    config_args = dict()

    # Provided callbacks
    def on_start(host):
        print('Starting... {}'.format(host))

    def on_notify(host, handler):
        print('Notify... {} {}'.format(host, handler))

    test_ActionModule_run()

# Generated at 2022-06-13 10:33:30.702794
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task import Task
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.executor.playbook_executor import PlaybookExecutor
    import os
    from ansible.inventory.manager import InventoryManager

    inventory_manager = InventoryManager(loader=None, sources=None)
    test_host = inventory_manager.add_host('test_host','127.0.0.1')
    test_host.vars['ansible_host'] = '127.0.0.1'
    test_host.vars['ansible_user'] = 'root'
    test_host.vars['ansible_connection'] = 'local'


# Generated at 2022-06-13 10:33:40.365277
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.loader import action_loader
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    import ansible.constants as C
    import sys
    import json
    print("#############test_ActionModule_run()###################")
    if len(sys.argv) < 2:
        print("Usage: %s playbooks/test.yml" % sys.argv[0])

# Generated at 2022-06-13 10:33:53.807968
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Mock Objects
    task = mock.Mock()
    task.args = {}
    task.delegate_to = 'test'
    task._parent = mock.Mock()
    task._parent._play = mock.Mock()
    task._parent._play._action_groups = ['post_tasks']
    task.module_defaults = {}
    task.async_val = 'test'

    connection = mock.Mock()
    tmpdir = 'tmpdir'
    connection._shell.tmpdir = tmpdir

    display = mock.Mock()

    module_loader = mock.Mock()
    plugin_finder = mock.Mock()
    finder_res = mock.Mock()
    finder_res.resolved_fqcn = 'test_fqcn'
    plugin_finder.find_plugin_

# Generated at 2022-06-13 10:34:00.921476
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    task_ds = dict(
        delegate_to='127.0.0.1',
        use='auto'
    )

    task_obj = ActionModule(task_ds, dict(connection='local'))
    result = task_obj.run(None, dict(ansible_facts= dict(service_mgr='auto')))
    pass

# Generated at 2022-06-13 10:34:13.508367
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils.facts.system import get_distribution

    test_action = ActionModule()
    test_action._shared_loader_obj.module_loader.has_plugin = lambda x: True

    # Test with module = auto
    test_action._templar.template = lambda x: 'systemd'
    test_action._task.args = {'use': 'auto'}
    test_action._task.delegate_to = 'delegate'
    test_action.hostvars = {'delegate': {'ansible_facts': {'service_mgr': 'test_service_mgr'}}}
    test_action.test_service_mgr = 'test_service_mgr'
    test_action._execute_module = lambda x, y, z: 'test_get_defaults'
    os

# Generated at 2022-06-13 10:36:23.625267
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.executor.module_common import MODULE_ARGS_SPEC, get_action_args_with_defaults, get_action_args_with_defaults
    from ansible.plugins.action import ActionBase
    from ansible.parsing import plugin_loader
    import ansible.plugins.action.service as service

    # ActionBase._execute_module() return None
    def _execute_module(self, module_name=None, module_args=None, task_vars=None, wrap_async=False):
        return [{}, None]

    # ORIGINAL METHOD:
    # return super(ActionModule, self).run(tmp, task_vars)

# Generated at 2022-06-13 10:36:25.560922
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule()
    assert action_module is not None

# Generated at 2022-06-13 10:36:34.846808
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.task import Task
    from ansible.playbook.role import Role
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    import json

    loader = DataLoader()
    inventories = InventoryManager(loader=loader, sources=['hosts'])
    variable_manager = VariableManager(loader=loader, inventory=inventories)

# Generated at 2022-06-13 10:36:45.174798
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # action module instance
    module = ActionModule()

    # arguments for the above module
    arg1 = {
        'name': 'redis-server',
        'state': 'started',
        'use': 'auto'
    }

    # dictionary containing hostvars of delegate_to host
    hostvars = {
        'host1': {
            'ansible_facts': {
                'service_mgr': 'systemd'}
        }
    }

    # shared loader object
    shared_loader_obj = None

    # task object
    task_obj = {
        'delegate_to': 'host1',
        'async_val': 0,
        'args': arg1,
        'module_defaults': "",
        '_parent': "",
        'collections': ''
    }

    #