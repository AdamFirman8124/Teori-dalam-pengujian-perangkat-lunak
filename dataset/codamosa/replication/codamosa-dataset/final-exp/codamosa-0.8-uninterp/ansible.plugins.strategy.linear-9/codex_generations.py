

# Generated at 2022-06-13 15:18:05.623676
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_module = StrategyModule()
    assert(isinstance(strategy_module, StrategyModule))


# Generated at 2022-06-13 15:18:08.925190
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    test_strat = StrategyModule()
    assert isinstance(test_strat, StrategyModule)
    assert len(test_strat._blocked_hosts) == 0
    assert test_strat._pending_results == 0

if __name__ == "__main__":
    test_StrategyModule()

# Generated at 2022-06-13 15:18:12.856679
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    a = StrategyModule()
    assert isinstance(a, StrategyModule)
    print("Constructor test for StrategyModule passed.")
    assert isinstance(a, BaseStrategy)
    print("Constructor test for StrategyModule passed.")


# Generated at 2022-06-13 15:18:25.791102
# Unit test for constructor of class StrategyModule
def test_StrategyModule():

    # Create mock objects
    tqm = mock.Mock()

    # Instantiate the strategy module
    strategy_module = StrategyModule(tqm)

    # Make assertions
    assert isinstance(strategy_module, BaseStrategy)
    assert strategy_module._hosts_cache is None
    assert strategy_module._hosts_cache_all is None
    assert strategy_module._tqm == tqm
    assert strategy_module._workers_count == DEFAULT_FORKS
    assert strategy_module._notified_handlers == {}
    assert strategy_module._active_connections == {}
    assert strategy_module._blocked_hosts == {}
    assert strategy_module._pending_results == 0
    assert strategy_module._pipelining == False
    assert strategy_module._stats == tqm._stats

# Generated at 2022-06-13 15:18:36.949448
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    import mock
    load_options = LoadOptions()
    opts = mock.Mock()
    ansible_cfg = os.path.join(os.path.dirname(__file__), "ansible.cfg")
    playbook = os.path.join(os.path.dirname(__file__), "debug.yml")

    # build the config object -- this is independent of the strategy being used
    display.verbosity = 3
    variable_manager = VariableManager()
    loader = DataLoader()
    variable_manager.extra_vars = load_options.__dict__
    passwords = {}
    results_callback = ResultCallback()
    inventory = Inventory(loader=loader, variable_manager=variable_manager, host_list=['localhost', '127.0.0.1'])


# Generated at 2022-06-13 15:18:38.790162
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    test_result = run_test(StrategyModule)
    if test_result.wasSuccessful():
        return 0
    return 1


# Generated at 2022-06-13 15:18:43.033310
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    sm = StrategyModule(
        tqm=None,
        connection_info=None,
        loader=None,
        variable_manager=None,
        loader_cache=None)

    assert sm._tqm is None
    assert sm._inventory is None
    assert sm._variable_manager is None
    assert sm._loader is None
    assert sm._host_pinned is False

# Generated at 2022-06-13 15:18:54.137093
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    my_strategy_module = StrategyModule()
    my_strategy_module._tqm.RUN_OK = True
    my_strategy_module._hosts_cache = []
    my_strategy_module._hosts_cache_all = []
    my_strategy_module._variable_manager.get_vars = lambda play, host, task, _hosts, _hosts_all: []
    my_strategy_module.TASK_CACHE = {}
    my_strategy_module.TASK_CACHE['pre_tasks'] = False
    my_strategy_module.TASK_CACHE['tasks'] = False
    my_strategy_module.TASK_CACHE['post_tasks'] = False

    iterator = "my_iterator"
    play_

# Generated at 2022-06-13 15:18:55.223504
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    strategy_module = StrategyModule()
    print("Parameter name: ")
    strategy_module.run()
    return

# Generated at 2022-06-13 15:18:59.341376
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    module = StrategyModule()
    x = module.run(iterator=None, play_context=None)
    assert x == 0

# Generated at 2022-06-13 15:19:41.680645
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    StrategyModule(
        tqm=None,
        var_manager=None,
        loader=None,
        passwords=None,
        stdout_callback=None,
        run_additional_callbacks=True,
        run_tree=False,
        forks=None,
        timeout=None,
        display=None,
        step=None,
        use_contrib_script_wrapper=None,
        free_form=False,
    )

# Generated at 2022-06-13 15:19:42.955635
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    module = StrategyModule()
    module.run(iterator=None, play_context=None)

# Generated at 2022-06-13 15:19:54.916973
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategyModule = StrategyModule(tqm=None, strategy='linear', host_list=[], module_vars=dict(), loader=None,
                                    options=dict(), passwords=dict())
    assert(strategyModule.GET_NEXT_TASK_LOCKSTEP_ITERATIONS == 100)
    assert(strategyModule._tqm == None)
    assert(strategyModule._inventory == None)
    assert(strategyModule._variable_manager == None)
    assert(strategyModule._loader == None)
    assert(strategyModule._play_context == None)
    assert(strategyModule._shared_loader_obj == None)
    assert(strategyModule._host_pinned == False)
    assert(strategyModule._host_pinned_msg == '')
    assert(strategyModule._task_queue == None)


# Generated at 2022-06-13 15:19:59.981530
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    try:
        # Test 1
        # Test with bad tqm value
        test_strategy_module = StrategyModule(None, "vars", "Runner", "Inventory", "Loader")
        assert test_strategy_module is None
    except:
        assert True
    else:
        assert False

    try:
        # Test 2
        # Test with bad variable_manager value
        test_strategy_module = StrategyModule("tqm", None, "Runner", "Inventory", "Loader")
        assert test_strategy_module is None
    except:
        assert True
    else:
        assert False


# Generated at 2022-06-13 15:20:00.719436
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    pass

# Generated at 2022-06-13 15:20:02.899351
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    result = StrategyModule(None, None, None, None, None)
    assert type(result) == StrategyModule


# Generated at 2022-06-13 15:20:12.766109
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    # multiprocessing.Process
    from ansible.executor.task_result import TaskResult

    from ansible.executor.process.worker import WorkerProcess
    from ansible.executor.process.worker import WorkerCallbacks
    from ansible.plugins.loader import get_all_plugin_loaders
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.template import Templar
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.role.include import RoleInclude
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.plugins.callback import CallbackBase
   

# Generated at 2022-06-13 15:20:20.014103
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    """
    Unit test for method run of class StrategyModule
    """
    # Create a StrategyModule object
    strategy_module = StrategyModule()
    # Create a dummy iterator
    iterator = MagicMock()
    # Create a play_context object
    play_context = MagicMock()
    # Define the return value of method get_hosts_left of class iterator
    iterator.get_hosts_left.return_value = ['localhost']
    # Create a host object
    host = MagicMock()
    # Define the return value of method get_name of class host
    host.get_name.return_value = 'localhost'
    # Define the return value of method hosts of class iterator
    iterator.hosts.return_value = [host]
    # Create a task object
    task = MagicMock()
    # Define the

# Generated at 2022-06-13 15:20:23.925053
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert isinstance(StrategyModule(task_queue_manager=None, inventory=None, variable_manager=None, loader=None, options=None, passwords=None), StrategyModule)


# Generated at 2022-06-13 15:20:26.249886
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    my_strategy = StrategyModule()
    my_strategy.run(iterator, play_context)
    print('Pass module test')



# Class RunnerBase
# Documentation: https://docs.ansible.com/ansible/devel/dev_guide/developing_api.html#runnerbase-api-class

# Generated at 2022-06-13 15:21:12.997574
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    """
    Unit test for constructor of class StrategyModule
    """
    # This is must be the first line of the test as it sets up the environment
    setup_test_environment()

    # Create instance of class StrategyBase
    step = True
    tqm = Mock()
    loader = Mock()
    variable_manager = Mock()
    shared_loader_obj = Mock()
    host_number = 1
    strategy = StrategyModule(tqm, step, host_number)

    assert strategy._tqm == tqm
    assert strategy._host_number == host_number
    assert strategy._step == step
    assert strategy._loader == loader
    assert strategy._variable_manager == variable_manager
    assert strategy._shared_loader_obj == shared_loader_obj
    assert len(strategy._connections) == 0

# Generated at 2022-06-13 15:21:17.564545
# Unit test for constructor of class StrategyModule
def test_StrategyModule():

    tqm = None
    hosts = [{
                "name": "c1n01",
                "vars": {
                   "test_var": "some_variable"
                }
            },
            {
                "name": "c1n02",
                "vars": {
                   "test_var": "some_variable"
                }
            }]
    module_name = "some_module"
    module_args = "some_module_args"
    task_queue_manager = TaskQueueManager(hosts, tqm)
    strategy_module = StrategyModule(task_queue_manager)
    assert_equals(strategy_module.__class__.__name__, "StrategyModule")
    strategy_module._set_hosts_cache(hosts)

# Generated at 2022-06-13 15:21:26.020528
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    '''
    Unit test for method run of class StrategyModule
    '''

    # Create avar manager for test
    varmgr = VariableManager()

    # Create a play for test
    newPlay = Play().load(get_fixture_path('v2_playbook.yml'), varmgr=varmgr, loader=None)

    # Create an inventory for test
    newInv = Inventory(loader=None, variable_manager=varmgr, host_list=get_fixture_path('hosts'))
    newInv.parse_inventory(newInv)

    # Create a task queue manager for test
    newTQM = TaskQueueManager(inventory=newInv, variable_manager=varmgr, loader=None)

    # Create a basic strategy module for test
    strategy = StrategyModule(tqm=newTQM)

# Generated at 2022-06-13 15:21:27.249472
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    t = StrategyModule()
    t.run()


# Generated at 2022-06-13 15:21:30.532554
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    strategy_module = StrategyModule(tqm=None,
                                     inventory=None,
                                     variable_manager=None,
                                     loader=None,
                                     options=None,
                                     shared_loader_obj=None,
                                     default_vars=None)


# Generated at 2022-06-13 15:21:31.142714
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    module = StrategyModule()

# Generated at 2022-06-13 15:21:33.045600
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    try:
        tqm = TaskQueueManager(None, None, None, None)
        sm = StrategyModule(tqm)
        assert sm is not None
    except Exception:
        assert False


# Generated at 2022-06-13 15:21:33.685893
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    pass

# Generated at 2022-06-13 15:21:46.592933
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    # Init some data
    loader = DataLoader()
    inventory = Inventory(loader=loader, variable_manager=VariableManager(), host_list=['localhost'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    play_context = PlayContext()
    play_source = dict(
        name="Ansible Play",
        hosts='local',
        gather_facts='no',
        tasks=[
            dict(action=dict(module='shell', args='ls'), register='shell_out'),
            dict(action=dict(module='debug', args=dict(msg='{{shell_out.stdout}}')))
         ]
    )

    # Init the strategy module with the given data
    tqm = None
    sm = StrategyModule(tqm, loader=loader, inventory=inventory, variable_manager=variable_manager)

# Generated at 2022-06-13 15:21:55.085995
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    inventory = '''
    [target]
    dev-vip-001 ansible_host=192.0.2.3 ansible_user=root
    '''
    play = dict(
        name = "Ansible Play",
        hosts = "target",
        gather_facts = 'no',
        tasks = [
            dict(action=dict(module='shell', args='id root'), register='shell_out'),
            dict(action=dict(module='debug', args=dict(msg='{{shell_out.stdout}}')))
         ]
    )
    tqm = None

# Generated at 2022-06-13 15:23:22.198270
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    testobj = StrategyModule()
    testobj.run('', '')
    

# Generated at 2022-06-13 15:23:27.500682
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    iterator = MagicMock()
    play_context = MagicMock()
    result = MagicMock()
    hosts_left = MagicMock()
    self_tqm_terminated = MagicMock()
    display_debug = MagicMock()
    self_set_hosts_cache = MagicMock()
    self_get_hosts_left = MagicMock()
    host_tasks = MagicMock()
    choose_step = MagicMock()
    any_errors_fatal = MagicMock()
    results = MagicMock()
    self_execute_meta = MagicMock()
    self_take_step = MagicMock()
    self_blocked_hosts = MagicMock()
    self_queue_task = MagicMock()
    self_process_pending_results = MagicMock()
   

# Generated at 2022-06-13 15:23:38.199205
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
  fake_iterator = 'fake_iterator'
  fake_iterator._play = 'fake_iterator._play'
  fake_iterator.get_failed_hosts = MagicMock(return_value=[])
  fake_iterator.mark_host_failed = MagicMock()
  fake_iterator.is_failed = MagicMock(return_value=False)

  fake__get_next_task_lockstep = MagicMock(return_value=[])
  fake__get_next_task_lockstep.__name__ = "fake__get_next_task_lockstep"
  fake__get_next_task_lockstep.return_value = None
  fake__process_pending_results = MagicMock()
  fake__process_pending_results.return_value = []
  fake__queue_task = MagicMock()
  fake__

# Generated at 2022-06-13 15:23:48.450048
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    # Create an instance of class StrategyModule
    strategy_module_instance = StrategyModule()

# Generated at 2022-06-13 15:23:57.781944
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText
    from ansible.vars.manager import VariableManager
    from ansible.vars.loader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.module_utils.common._collections_compat import MutableMapping
    from ansible.plugins.loader import callback_loader
    from ansible.template import Templar
    from ansible.errors import AnsibleError
    from ansible.executor.task_result import TaskResult
    from ansible.executor.stats import AggregateStats
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.path import unfrackpath
   

# Generated at 2022-06-13 15:23:59.336679
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
     strategy = StrategyModule(Tqm(),None, None, None, None, None, None, None)
     assert strategy


# Generated at 2022-06-13 15:24:01.356421
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert(str(StrategyModule.__init__) ==
           "StrategyModule.__init__(self, tqm, variables)")

# Generated at 2022-06-13 15:24:02.782005
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategymodule = StrategyModule(None, None, None, None)
    assert strategymodule is not None

# Generated at 2022-06-13 15:24:05.884390
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    mock_iterator = MagicMock()
    mock_play_context = MagicMock()
    strategy_module = StrategyModule(loader=None, tqm=None, strategy='linear')
    strategy_module.run(iterator=mock_iterator, play_context=mock_play_context)


# Generated at 2022-06-13 15:24:08.953253
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy = StrategyModule( tqm = Tqm(), connection_info = {}, loader = None, variable_manager = None, shared_loader_obj = None )
    assert strategy is not None

# Load the strategy plugin, run the test case
strategies.add( 'linear', StrategyModule )

test_StrategyModule()

# Generated at 2022-06-13 15:27:11.053846
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    # Initalizing required objects
    fake_loader = DictDataLoader({})
    fake_inventory = Inventory(loader=fake_loader, variable_manager=VariableManager(), host_list=[])
    fake_variable_manager = VariableManager()
    fake_variable_manager.set_inventory(fake_inventory)
    fake_tqm = TaskQueueManager(
        inventory=fake_inventory,
        variable_manager=fake_variable_manager,
        loader=fake_loader,
        options=Options(),
        passwords=dict(),
    )
    # Declaring required objects
    strategy_module = StrategyModule(fake_tqm)
    
    # Preparing fake objects
    fake_play = Play()
    fake_play._play_context = PlayContext()
    fake_play._play_context.remote_addr = None
    fake_play

# Generated at 2022-06-13 15:27:19.892623
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy = StrategyModule()

    callback_sent = False
    any_errors_fatal = False
    def send_callback(msg, task, is_conditional=False):
        global callback_sent
        global any_errors_fatal
        callback_sent = True
        any_errors_fatal = True

    strategy._tqm.send_callback = send_callback

    task = {'any_errors_fatal': True}
    iterator = None

    host = 'test_host'
    play_context = {}
    _hosts_cache = {}
    _hosts_cache_all = {}

    strategy.run(iterator, play_context)

# Generated at 2022-06-13 15:27:23.485117
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_module = StrategyModule(
        tqm = None,
        variant = 'linear',
        all_vars = dict(),
        options = dict(),
        loader = None,
        variable_manager = None,
        host_list = None
    )
    assert strategy_module is not None

# Generated at 2022-06-13 15:27:25.137828
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    strategymodule = StrategyModule()
    assert strategymodule != None
    strategymodule.run(iterator, play_context)

# Generated at 2022-06-13 15:27:30.396050
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    strategy_module = StrategyModule(tqm)
    # host = None
    # iterator = None
    # play_context = None
    result = strategy_module.run(iterator, play_context)
    assert result == tqm.RUN_UNKNOWN_ERROR
'''
# Execute class IncludedFile
'''

# included_file.py