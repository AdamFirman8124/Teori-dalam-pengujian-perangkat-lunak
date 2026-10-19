

# Generated at 2022-06-13 15:06:51.419373
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    from ansible.plugins.strategy import StrategyBase
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    tqm = None
    iterator = None
    play_context = None
    strategyModule = StrategyModule(tqm)
    strategyModule.run(iterator, play_context)
    assert hasattr(strategyModule, '_hosts_cache') == True
    assert callable(strategyModule.run) == True
    assert issubclass(StrategyModule, StrategyBase) == True
    assert not hasattr(strategyModule, "beep")



# Generated at 2022-06-13 15:06:54.271963
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    tqm = MockTQM()
    iterator = MockIterator()
    play_context = MockPlayContext()
    strats = StrategyModule(tqm)
    strats.run(iterator, play_context)



# Generated at 2022-06-13 15:06:59.619186
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    
    print('\n=== Function: StrategyModule.__init__ ===')
    
    import mock
    tqm = mock.Mock()
    sm = StrategyModule(tqm)
    
    assert sm.run == StrategyModule.run
    assert sm.get_hosts_left == StrategyModule.get_hosts_left
    assert sm.get_failed_hosts == StrategyModule.get_failed_hosts
    assert sm.get_changed_hosts == StrategyModule.get_changed_hosts
    

# Generated at 2022-06-13 15:07:05.733642
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
  # NOTE: we do not test the queue_task method.
  # TODO: Check if we should test the queue task method.

  # TODO: Another part of the test should run the method of the base class run (which executes the cleanup function and runs any outstanding handlers which have been triggered)
  # We did not do this part, because we consider it less important than the part that is tested.

  # First we create a mock object for all objects that are used by the method
  tqm = MagicMock()
  iterator = MagicMock()
  play_context = MagicMock()
  host = MagicMock()
  worker = MagicMock()
  task = MagicMock()
  worker_task = MagicMock()
  ite = MagicMock()
  task_vars = MagicMock()
  templar = MagicMock()

# Generated at 2022-06-13 15:07:06.133600
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    assert True

# Generated at 2022-06-13 15:07:16.733091
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.vars.manager import VariableManager

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=["/Users/bobby/projects/ansible-2.9.10/test/inventory"])
    variable_manager = VariableManager(loader=loader, inventory=inventory)

# Generated at 2022-06-13 15:07:27.549282
# Unit test for method run of class StrategyModule

# Generated at 2022-06-13 15:07:37.321248
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    # in this test fixture, only job test_runner_playbook_runners_check_playbook_v2_playbook_on_stats_on_runner_on_unreachable
    play_context = {}
    action = None
    run_once = None

    # task.action = "setup"
    task = {}
    task.action = "setup"
    task.host = "host"
    task.task_deps = {}
    task.notify = {}
    task.run_once = False
    task.register = None
    task.when = None
    task.async_val = None
    task.async_seconds = None
    task.changed_when = None
    task.failed_when = None
    task.tags = []
    task.delegate_to = None
    task.until = None
   

# Generated at 2022-06-13 15:07:37.720504
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True

# Generated at 2022-06-13 15:07:38.102155
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    pass

# Generated at 2022-06-13 15:08:01.062381
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    pass



# Generated at 2022-06-13 15:08:12.747077
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    from ansible.playbook.play import Play
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.handler import Handler
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.vars.manager import VariableManager
    from ansible.plugins.strategy.linear import StrategyModule
    from ansible.plugins.loader import action_loader
    from ansible.utils.listify import listify_lookup_plugin_terms
    from ansible.executor.task_queue_manager import TaskQueueManager
    from units.mock.loader import DictDataLoader

    play = Play()
    play._variable_manager = VariableManager()

# Generated at 2022-06-13 15:08:14.345963
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert isinstance(StrategyModule, object)


# Generated at 2022-06-13 15:08:20.669057
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
	# Define variables
	iterator = None
	play_context = ''

	# Create object of class StrategyModule
	obj = StrategyModule()

	# Check if method 'run' exists
	if hasattr(obj,'run'):
		obj.run(iterator, play_context)
	else:
		print("Method 'run' does not exist")
		return

	# Check that run method does not return anything
	assert obj.run(iterator, play_context) is None, "Error, method 'run' returns not nothing"

	print("Method run of class StrategyModule - ok\n")


# Generated at 2022-06-13 15:08:25.983975
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    # create mock ansible runtime
    mock_ansible_runtime(None)
    # create mock ansible-runner runtime
    mock_ansible_runner_runtime()

    # Ansible results to tell what happened on the machine
    results = [
        {
            'host': 'host1',
            'port': 22,
            'result': {'results': {'status': 'SUCCESSFUL'}}
        },
        {
            'host': 'host2',
            'port': 22,
            'result': {'results': {'status': 'SUCCESSFUL'}}
        },
        {
            'host': 'host3',
            'port': 22,
            'result': {'results': {'status': 'FAILED'}}
        }
    ]

    # Mock ansible results

# Generated at 2022-06-13 15:08:28.954339
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    obj = StrategyModule(tqm)
    result = obj.run(iterator, play_context)
    return result

# Generated at 2022-06-13 15:08:32.740670
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    tqm = TaskQueueManager(None, None, None)
    iterator = PlayIterator(None, None, None)
    result = StrategyModule(tqm)
    result.run(iterator, None)



# Generated at 2022-06-13 15:08:35.843974
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_module = StrategyModule(tqm=None)
    # check if the object is instance of class StrategyBase
    assert isinstance(strategy_module, StrategyBase)
    # check if the object is instance of class StrategyModule
    assert isinstance(strategy_module, StrategyModule)


# Generated at 2022-06-13 15:08:45.207250
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    # Create a dummy object of class StrategyModule
    strategy = StrategyModule(None)

    # Create a dummy object of class TaskResult for testing
    task_result = TaskResult(None, None, None, None)
    # Make host_name of the result successful
    task_result.host = "host_name"
    task_result.task_name = "task_name"
    task_result.task_action = "task_action"
    task_result.result._result = {'invocation': {'module_name': 'setup'}, 'ansible_facts': {'ansible_hostname': 'host_name'}}

    # Create a dummy object of class TaskResult
    task_result1 = TaskResult(None, None, None, None)
    task_result1.host = "host_name1"

# Generated at 2022-06-13 15:08:48.680850
# Unit test for constructor of class StrategyModule
def test_StrategyModule():

    tqm = None # TODO: Test for StrategyModule -> tqm
    strategy_module = StrategyModule(tqm)

    assert strategy_module._host_pinned == False

# Generated at 2022-06-13 15:09:47.019326
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    ''' StratgyModule.run()'''

    iterator = None
    play_context = None

    strategy = StrategyModule(tqm)

    # test with valid args
    assert strategy.run(iterator, play_context)



# Generated at 2022-06-13 15:09:53.477830
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.block import Block
    from ansible.playbook.handler import Handler
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.helpers import load_list_of_blocks
    from ansible.playbook.conditional import Conditional
    from ansible.playbook._play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.utils.vars import combine_vars
    from ansible.inventory.host import Host

   

# Generated at 2022-06-13 15:10:04.529543
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    # Create a mocked ConfigManager
    mock_config = create_autospec(ConfigManager)
    mock_config.debug = False

    # Create a mocked TerminalBase
    mock_terminal = create_autospec(TerminalBase)
    mock_terminal.host = 'localhost'

    # Create a mocked TaskQueueManager
    mock_manager = create_autospec(TaskQueueManager)
    mock_manager._initialize_processes = None
    mock_manager.config = mock_config
    mock_manager.terminal = mock_terminal
    mock_manager.log_lock = None
    mock_manager.log_path = None
    mock_manager.run_handlers = None
    mock_manager.run_final_q = None
    mock_manager._final_q_workers = None
    mock_manager._notified_

# Generated at 2022-06-13 15:10:11.861088
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    from ansible.playbook.included_file import IncludedFile
    from ansible.template import Templar
    from ansible import constants as C
    class mock_playbook_on_task_start:
        def __init__(self):
            pass
        def update(self,task,is_conditional=False):
            return 0
    class mock_playbook_on_no_hosts_remaining:
        def __init__(self):
            pass
        def update(self):
            return 0
    class mock_Display:
        def __init__(self):
            pass
        def debug(self,msg,host=None):
            return 0
        def warning(self,msg,wrap_text=None):
            return 0
    display=mock_Display()

# Generated at 2022-06-13 15:10:23.430819
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.plugins.strategy import StrategyModule
    from ansible.plugins.strategy.linear import StrategyModule as linear

    class FakeOptions(object):
        verbosity = 0
        ascii = False
        step = False
        diff = False

    class FakeLoader(object):
        ''' mock dataloader '''

    options = FakeOptions()
    loader = FakeLoader()
    play = Play()

# Generated at 2022-06-13 15:10:24.117512
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    assert False

# Generated at 2022-06-13 15:10:33.254736
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    th = AnsibleTaskHost(name = 'test_host', port = 22, groups = ['group1', 'group2'])
    tqm = TaskQueueManager(terminated = False, inventory = AnsibleInventory([th]), variable_manager = AnsibleVariableManager())
    ac = AnsibleConnection('local')
    sm = StrategyModule(tqm)
    pl = AnsiblePlay()
    pl.hosts = 'all'
    th1 = AnsibleTaskHost(name = 'test_host1', port = 22, groups = ['group1', 'group2'])
    th2 = AnsibleTaskHost(name = 'test_host2', port = 22, groups = ['group1', 'group2'])
    sm._hosts_cache[th.name] = th 

# Generated at 2022-06-13 15:10:33.753727
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    pass




# Generated at 2022-06-13 15:10:44.893594
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    """Test class StrategyModule and method run"""
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.plugins.strategy import StrategyModule
    from io import StringIO
    import json
    options = namedtuple("Options", ["connection", "module_path", "forks", "become", "become_method", "become_user", "check", "diff"])

# Generated at 2022-06-13 15:10:45.620537
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    pass

# Generated at 2022-06-13 15:13:11.115190
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    host = "host"
    include_host = "include_host"
    host_name = "host_name"
    include_host_name = "include_host_name"
    tqm = "tqm"
    path = "path"
    action = "action"
    iterator = "iterator"
    play_context = "play_context"

    strategy_module = StrategyModule(tqm)

    def get_hosts_left(iterator):
        return [host]

    strategy_module.get_hosts_left = get_hosts_left

    def get_hosts_left(iterator):
        return [include_host]

    strategy_module.get_hosts_left = get_hosts_left

    def get_hosts_left(iterator):
        return []

    strategy_module.get_

# Generated at 2022-06-13 15:13:17.258859
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    fake_tqm = object()
    fake_iterator = object()
    fake_play_context = object()

    actual = StrategyModule(fake_tqm)
    actual._tqm = FakeTqm()

    actual.run(fake_iterator, fake_play_context)
    assert actual._tqm.run() == True
    assert actual._tqm.call_count == 1



# Generated at 2022-06-13 15:13:20.819844
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    tqm = mock.Mock()
    strategy = StrategyModule(tqm)
    iterator = mock.Mock()
    play_context = mock.Mock()
    strategy.run(iterator, play_context)

# Generated at 2022-06-13 15:13:21.473233
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    pass

# Generated at 2022-06-13 15:13:22.467117
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    pass

# unit test for method add_tqm_variables of class StrategyModule

# Generated at 2022-06-13 15:13:31.885635
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    # set up objects needed for StrategyModule.run method to function
    # assumption: no error should occur
    strategy_module = StrategyModule(object)
    strategy_module.get_hosts_left = StrategyModule.get_hosts_left
    strategy_module.add_tqm_variables = StrategyModule.add_tqm_variables
    strategy_module._execute_meta = StrategyModule._execute_meta
    strategy_module._queue_task = StrategyModule._queue_task
    strategy_module._host_pinned = False
    strategy_module.update_active_connections = StrategyModule.update_active_connections
    strategy_module._process_pending_results = StrategyModule._process_pending_results
    strategy_module._wait_on_pending_results = StrategyModule._wait_on_pending_results
    strategy

# Generated at 2022-06-13 15:13:40.529903
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    try:
        from ansible import context
        from ansible.template import Templar
        from ansible.executor.task_queue_manager import TaskQueueManager
        from ansible.executor.playbook_executor import PlaybookExecutor
        from ansible.vars.manager import VariableManager
        from ansible.playbook.play import Play
        from ansible.inventory.manager import InventoryManager
    except ImportError:
        print('Failed to import ansible modules')
        return False

    templar = Templar(loader=None)
    tqm = TaskQueueManager(
        inventory=InventoryManager(loader=None, sources=''),
        variable_manager=VariableManager(loader=None),
        loader=None,
        options=context.CLIARGS,
        passwords=None,
    )


# Generated at 2022-06-13 15:13:44.801583
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_module = StrategyModule(1)
    result = strategy_module.__class__.__name__
    assert 'StrategyModule' == result, "Expected: %s, Actual: %s" % ('StrategyModule', result)

# Generated at 2022-06-13 15:13:47.846673
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    class Tqm:
        RUN_OK = True
    class Play:
        max_fail_percentage = None
    class PlayContext:
        pass
    iterator = StrategyModule(Tqm())
    result = iterator.run(Play(), PlayContext())
    assert result is True

# Generated at 2022-06-13 15:13:56.911059
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    import unittest
    import tempfile
    import os
    import pytest
    import ansible.module_utils.basic
    import ansible.module_utils.six
    import ansible.utils.jinja
    import ansible.utils.template
    import ansible.vars
    import ansible.plugins
    import ansible.plugins.strategy
    import ansible.plugins.strategy.linear
    import ansible.plugins.strategy.free
    import ansible.plugins.strategy.debug
    import ansible.plugins.strategy.debug2
    import ansible.playbook.play_context
    import ansible.playbook.play
    import ansible.playbook.task
    import ansible.playbook.role
    import ansible.playbook.block
    import ansible.playbook.handler