

# Generated at 2022-06-13 15:06:46.731558
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    class Test_StrategyModule(StrategyModule):
        pass
    strategyModule = Test_StrategyModule()
    assert strategyModule.run() == ''



# Generated at 2022-06-13 15:06:50.392304
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
   strategy = StrategyModule(tqm)
   iterator = iterator
   play_context = play_context
   #test_StrategyModule_run
   strategy = StrategyModule(tqm)
   iterator = iterator
   strategy.run(iterator, play_context)


# Generated at 2022-06-13 15:06:52.311607
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    tqm = AnsibleQueueManager()
    strategy_module = StrategyModule(tqm)
    strategy_module.run(iterator,play_context)

# Generated at 2022-06-13 15:06:55.021224
# Unit test for constructor of class StrategyModule
def test_StrategyModule():

	# check the class attribute is the same as the one in the super class
    assert StrategyModule.ALLOW_BASE_THROTTLING == False

test_StrategyModule()

# Generated at 2022-06-13 15:07:06.973507
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    playbook_path = 'tests/fixtures/test_playbooks/playbook_with_tasks_and_roles.yaml'
    stats = callbacks.AggregateStats()
    playbook_cb = callbacks.PlaybookCallbacks(verbose=utils.VERBOSITY)
    runner_cb = callbacks.PlaybookRunnerCallbacks(stats, verbose=utils.VERBOSITY)
    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = Inventory(loader=loader, variable_manager=variable_manager)
    variable_manager.set_inventory(inventory)
    inventory.add_host(host='localhost', port='22', ansible_connection='local')
    passwords = {}
    playbooks = [playbook_path]

# Generated at 2022-06-13 15:07:10.228083
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
#     Scenario:
#         Given an instance of class StrategyModule
#         When run is called with an iterator and a play_context
#         Then the result is not none
    strategy = StrategyModule();
    assert(strategy.run('','','') != None)

# Generated at 2022-06-13 15:07:16.100500
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():

        import pytest
        strategyModule = StrategyModule()

        # Attempt to make play iterator out of list and dict objects
        # Make sure errors thrown
        with pytest.raises(AnsibleError):
            strategyModule.run([], {})
        with pytest.raises(AnsibleError):
            strategyModule.run({}, {})
        with pytest.raises(AnsibleError):
            strategyModule.run({}, [])

# Generated at 2022-06-13 15:07:20.518293
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    #One of these tests should be deleted.
    #Check arguments
    test_module = StrategyModule(tqm=None)
    assert test_module.run(iterator=None, play_context=None)
    #Check method functionality

# Generated at 2022-06-13 15:07:21.251744
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    pass

# Generated at 2022-06-13 15:07:22.433767
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    pass  # noqa: WPS501

# Generated at 2022-06-13 15:07:41.735704
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():

    assert False

# Generated at 2022-06-13 15:07:46.186063
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    from ansible.executor.task_queue_manager import TaskQueueManager
    class TaskQueueManagerTest(TaskQueueManager):
        def __init__(self):
            self.RUN_OK = 1
            self.run_ok = 1
            self.host_result_cache = {}
            self.host_results = {}
            self.host_unreachable = {}
            self.host_failed = {}
            self.host_ignored = {}
            self.host_ok = {}
            self.task_result_cache = {}
            self.omit_hosts = {}
            self._terminated = False
#            self._executors = None
            self._inventory = None
            self._playbook = None
            self._loader = None


# Generated at 2022-06-13 15:07:46.748128
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    pass

# Generated at 2022-06-13 15:07:47.444482
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    pass

# Generated at 2022-06-13 15:07:48.183411
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    print("test")

# Generated at 2022-06-13 15:07:59.933230
# Unit test for method run of class StrategyModule

# Generated at 2022-06-13 15:08:01.023013
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
  pass

# Generated at 2022-06-13 15:08:01.654304
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    pass

# Generated at 2022-06-13 15:08:13.446004
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    from ansible.playbook import Playbook
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    import os
    import tempfile
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.playbook_executor import PlaybookExecutor


# Generated at 2022-06-13 15:08:14.955467
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    l = [1, 2, 3]
    StrategyModule(tqm=l)

# Generated at 2022-06-13 15:09:00.040016
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    # create a mocked inventory
    from ansible.plugins.loader import inventory_loader
    from ansible.parsing.dataloader import DataLoader

    def get_hosts(pattern="all"):
        return {'host1': {'host_name': 'host1', 'hostvars': {'foo': 'bar'}},
                'host2': {'host_name': 'host2', 'hostvars': {'foo': 'bar'}}}

    inventory = inventory_loader.get(constants.DEFAULT_INVENTORY_UNPARSED_PATTERN)
    inventory.hosts = get_hosts
    inventory.groups = {}
    inventory.pattern = "all"

    # create a mocked strategy
    from ansible.lib.hashcompat import md5_constructor

# Generated at 2022-06-13 15:09:00.945506
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    pass

# Generated at 2022-06-13 15:09:09.472596
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    TASK_QUEUE_MANAGER = 'TASK_QUEUE_MANAGER'
    strategy_module = StrategyModule(TASK_QUEUE_MANAGER)
    assert strategy_module.run(TASK_QUEUE_MANAGER, TASK_QUEUE_MANAGER) == 2
    assert strategy_module.get_hosts_left(TASK_QUEUE_MANAGER)
    assert strategy_module._blocked_hosts == {}
    assert strategy_module._tqm == TASK_QUEUE_MANAGER
    assert strategy_module._flushed_hosts == {}
    assert strategy_module.ALLOW_BASE_THROTTLING
    assert strategy_module._host_pinned == False

# Generated at 2022-06-13 15:09:12.636993
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    tqm = mock.MagicMock()
    StrategyModule.run(tqm, iterator, play_context)
    assert True

# Generated at 2022-06-13 15:09:13.248094
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule

# Generated at 2022-06-13 15:09:17.507764
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
   hosts = [hosts_list]
   iterator = None
   play_context = None
   try:
      l = StrategyModule(None)
      l.run(iterator, play_context)
   except Exception as e:
      print("Exception in user code:")
      print("-"*60)
      traceback.print_exc(file=sys.stdout)
      print("-"*60)
      raise

# Generated at 2022-06-13 15:09:18.770942
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    pass

# Generated at 2022-06-13 15:09:28.714574
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    module = AnsibleModule(
        argument_spec=dict(
            dynamic=dict(type='bool', required=False, default=False)
        )
    )

    if not HAS_PYTEST:
        module.fail_json(msg='pytest is required for this module')

    if not module.params['dynamic']:
        # Use the static test variables
        host = "localhost"
        test_strategy = "free"

        # Generate the static test variables
        test_loader = DataLoader()
        results_callback = ResultCallback()
        test_inventory = InventoryManager(loader=test_loader, sources=host)
        variable_manager = VariableManager(loader=test_loader, inventory=test_inventory)

        # Setup the test objects

# Generated at 2022-06-13 15:09:35.129210
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    tqm = MagicMock()
    tqm.result_q = MagicMock()
    tqm.result_q.qsize.return_value = 1
    tqm.send_callback = MagicMock()
    tqm.RUN_OK = 0
    tqm._terminated = False
    play = MagicMock()
    play.max_fail_percentage = 3
    iterator = MagicMock()
    iterator._play = play
    iterator.is_failed.return_value = False
    play_context = MagicMock()
    nonlocal_strategy = StrategyModule(tqm)
    nonlocal_strategy._set_hosts_cache = MagicMock()
    nonlocal_strategy.get_hosts_left = MagicMock()
    nonlocal_strategy.get_host

# Generated at 2022-06-13 15:09:36.583766
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    # Pass empty objects to function
    assert() == None

if __name__ == "__main__":
    test_StrategyModule_run()

# Generated at 2022-06-13 15:11:17.430815
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.playbook.play import Play
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    import yaml
    import os
    import tempfile
    import sys
    import pytest
    # define a play with multiple tasks

# Generated at 2022-06-13 15:11:18.054340
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    pass

# Generated at 2022-06-13 15:11:18.714170
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    pass

# Generated at 2022-06-13 15:11:19.498150
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    pass

# Generated at 2022-06-13 15:11:20.591267
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    strategy_module = StrategyModule(tqm)
    strategy_module.run(iterator, play_context)

# Generated at 2022-06-13 15:11:21.330973
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    assert False

# Generated at 2022-06-13 15:11:22.288789
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    pass



# Generated at 2022-06-13 15:11:32.799683
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.handler import Handler
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.executor.task_result import TaskResult
    from ansible.utils.display import Display
    from ansible.plugins.callback import CallbackBase
    import json
    display = Display()

# Generated at 2022-06-13 15:11:41.028613
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible import context
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    import os
    from units.mock.loader import DictDataLoader
    from units.mock.path import mock_unfrackpath_noop
    from units.mock.plugins import MockPluginManager
    from units.mock.collections import MockCollectionsLoader

    context.CLIARGS = lambda: None
    context.CLIARGS.verbosity = 4
    context.CLIARGS.connection

# Generated at 2022-06-13 15:11:43.720297
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    try:
        # Test when given no input
        strategy = StrategyModule()
    except TypeError as err:
        assert err.__str__() == "__init__() missing 1 required positional argument: 'tqm'"


# Generated at 2022-06-13 15:16:02.977605
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    # Defining some dummy instances of classes that StrategyModule depends on
    class dummy_Display:
        def debug(self, *args, **kwargs):
            return None
        def warning(self, *args, **kwargs):
            return None
    display = dummy_Display()
    class dummy_StrategyBase(StrategyBase):
        def __init__(self, tqm):
            pass
        def _execute_meta(self, *args, **kwargs):
            return None
        def _wait_on_pending_results(self, *args, **kwargs):
            return True
        def _process_pending_results(self, *args, **kwargs):
            return True
        def _queue_task(self, *args, **kwargs):
            return None

# Generated at 2022-06-13 15:16:03.609576
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
  pass

# Generated at 2022-06-13 15:16:04.104567
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    pass

# Generated at 2022-06-13 15:16:04.780606
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule.__doc__

# Generated at 2022-06-13 15:16:14.110152
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.playbook.play_context import PlayContext
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.plugins.loader import action_loader

    context = PlayContext()
    context.connection = 'local'
    context.remote_addr = None
    context.port = None
    inv_object = InventoryManager(loader=None, sources=[])
    var_manager = VariableManager()

# Generated at 2022-06-13 15:16:15.262672
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    print("TEST:Run StrategyModule(tqm)")


# Generated at 2022-06-13 15:16:24.229343
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    print("\n---test StrategyModule run---")
    import unittest
    import mock
    import ansible.plugins.strategy
    import ansible.utils.display
    from ansible.plugins.strategy import StrategyModule
    from collections import namedtuple

    my_task = namedtuple("my_task", ["action", "collections", "when", "register"])
    my_meta = namedtuple("my_meta", ["action", "collections", "when", "register"])
    my_handler = namedtuple("my_handler", ["_role"])

    class FakeTask(object):
        def __init__(self):
            self.action = "fake"
            self.collections = "fake"

    class FakeMeta(object):
        def __init__(self):
            self.action = "fake"

# Generated at 2022-06-13 15:16:26.053663
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    '''
    Unit test for method run
    '''
    pass
StrategyModule.test_StrategyModule_run = test_StrategyModule_run

