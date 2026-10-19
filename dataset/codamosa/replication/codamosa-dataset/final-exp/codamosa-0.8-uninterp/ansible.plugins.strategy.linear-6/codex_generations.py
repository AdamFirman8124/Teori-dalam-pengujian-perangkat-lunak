

# Generated at 2022-06-13 15:18:10.673417
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.inventory.manager import InventoryManager
    from ansible import errors
    from ansible.task.manager import TaskManager
    from ansible.task.task import Task
    my_obj = StrategyModule(TaskManager('/etc/ansible/playbooks/playbook1.yml'))
    my_obj._tasks = []
    my_obj._tasks.append(Task())
    my_obj._tasks[0].action = 'copy'
    my_obj._tasks[0]._role = errors.AnsibleError()
    my_obj._tasks[0]._role.has_run = False


# Generated at 2022-06-13 15:18:16.938719
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    mock_results_q = MagicMock()
    module = StrategyModule(
        tqm=BasicTestQueueManager(
            inventory=BaseInventory(),
            variable_manager=BaseVariableManager(),
            loader=BaseLoader(),
            options=MagicMock(),
            passwords=None
        ),
        play=MagicMock(),
        options=MagicMock(),
        variable_manager=BaseVariableManager(),
        loader=BaseLoader(),
        passwords=None)

    module.run(iterator=MagicMock(), play_context=MagicMock())



# Generated at 2022-06-13 15:18:26.160426
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    module = StrategyModule()
    # assert hasattr(module, '_step')
    assert hasattr(module, '_name')
    assert hasattr(module, '_blocked_hosts')
    assert hasattr(module, '_hosts_cache')
    assert hasattr(module, '_hosts_cache_all')
    assert hasattr(module, '_hosts_queue')
    assert hasattr(module, '_conditional_tasks')
    assert hasattr(module, '_conditional')
    assert hasattr(module, '_pending_results')
    assert hasattr(module, '_active_connections')


# Generated at 2022-06-13 15:18:27.251886
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule is StrategyModule

# Generated at 2022-06-13 15:18:27.884338
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass


# Generated at 2022-06-13 15:18:34.753392
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    hosts_left = []
    iterator = []
    play_context = []
    result = []
    play_context = []
    play_context.append(['play_context'])
    iterator.append(['iterator'])
    hosts_left.append(['hosts_left'])
    result.append(['result'])
    assert True == StrategyModule.run(hosts_left, iterator, play_context, result)




# Generated at 2022-06-13 15:18:36.220030
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_module = StrategyModule()
    assert strategy_module._blocked_hosts is None

# Generated at 2022-06-13 15:18:37.311368
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    pass

# end class StrategyModule



# Generated at 2022-06-13 15:18:38.829435
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    print(StrategyModule())

# Unit test of method get_hosts_left of class StrategyModule

# Generated at 2022-06-13 15:18:46.021894
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    host=''
    display='display'
    options=''
    variable_manager='variable_manager'
    loader='loader'
    passwords='passwords'
    # Test 1
    strategy_module=StrategyModule(host, display, options, variable_manager, loader, passwords)
    iterator=''
    play_context=''
    result=strategy_module.run(iterator, play_context)
    assert result==strategy_module._tqm.RUN_UNKNOWN_ERROR


# from ansible.plugins.strategy import StrategyBase

# Generated at 2022-06-13 15:19:27.874740
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    '''
    Run method of class StrategyModule
    '''
    module = StrategyModule()

    assert type(module.run({},{})) == int


# Generated at 2022-06-13 15:19:28.975284
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass


# Generated at 2022-06-13 15:19:31.980699
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    '''
    Unit test for method run of class StrategyModule
    '''
    obj = StrategyModule()
    try:
        obj.run()
    except SystemExit:
        pass


# Generated at 2022-06-13 15:19:33.341002
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy = StrategyModule()
    assert strategy != None


# Generated at 2022-06-13 15:19:33.946243
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass


# Generated at 2022-06-13 15:19:35.612536
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    try:
        strategy = StrategyModule()
        assert False
    except Exception:
        assert True


# Generated at 2022-06-13 15:19:42.657721
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_module = StrategyModule(tqm, None, None, None, None)
    assert strategy_module is not None
    assert strategy_module._tqm is tqm
    assert strategy_module._inventory is None
    assert strategy_module._variable_manager is None
    assert strategy_module._loader is None
    assert strategy_module._options is None
    assert strategy_module._blocked_hosts == {}
    assert strategy_module._workers_left == 0
    assert strategy_module._pending_results == 0
    assert strategy_module._cur_workers == 10
    assert strategy_module._final_q is None
    assert strategy_module._failed_queue is None
    assert strategy_module._workers_queue is None


# Generated at 2022-06-13 15:19:46.914749
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    strategy_module = StrategyModule()
    assert isinstance(strategy_module, StrategyModule) == True
    assert strategy_module.run() == None


# Generated at 2022-06-13 15:19:49.228064
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    result = StrategyModule()
    assert(isinstance(result, StrategyModule))


# Generated at 2022-06-13 15:20:01.419341
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    args = dict(
        default_vars_files = '',
        debug = False,
        diff = False,
        inventory = '',
        listhosts = False,
        listtags = False,
        listtasks = False,
        vault_password_files = '',
        vault_identity_list = ''
    )

    variable_manager = VariableManager()
    variable_manager.extra_vars = {}
    variable_manager._extra_vars = {}

    loader = DataLoader()

    inventory = Inventory(loader, variable_manager)

    variable_manager.set_inventory(inventory)


# Generated at 2022-06-13 15:21:13.577118
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy = StrategyModule(tqm=None)
    assert(strategy is not None)


# Generated at 2022-06-13 15:21:14.709807
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
	pass

# Generated at 2022-06-13 15:21:24.123905
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    #initialization
    strategy_module = StrategyModule()
    class Iterator():
        def  __init__(self):
            self._play = None
            self._hosts = None
            self._hosts_all = None
            self._host_state_map = {} #stores the iterator state
            self.dump_me_later = None
            self.prev_host = None
            self.prev_task = None
        def get_next_task_for_host(self, host, peek=False):
            return self._host_state_map[host]
        def get_active_state(self, s):
            return s
        def mark_host_failed(self, host):
            pass
        
    class Play():
        def  __init__(self):
            self.max_fail_percentage = None

# Generated at 2022-06-13 15:21:24.797793
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    return

# Generated at 2022-06-13 15:21:30.124069
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    iterator = mock.Mock()
    play_context = mock.Mock()
    _tqm = mock.Mock()
    _variable_manager = mock.Mock()
    _loader = mock.Mock()
    strategies = ['linear', 'free', 'serial', 'smart', 'implicit']
    strategy = strategies[randint(0, len(strategies)-1)]
    c = StrategyModule(tqm=_tqm, variable_manager=_variable_manager, loader=_loader, strategy=strategy)
    assert c.run(iterator, play_context) == _tqm.RUN_OK



# Generated at 2022-06-13 15:21:31.890129
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    mod = StrategyModule(tqm=None)
    assert mod != None

if __name__ == '__main__':
    mod = StrategyModule(tqm=None)
    assert mod != None

# Generated at 2022-06-13 15:21:43.961232
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
  # mock
  mock_StrategyBase_run = MagicMock()
  mock_get_hosts_left = MagicMock()
  mock_set_hosts_cache = MagicMock()
  mock_get_next_task_lockstep = MagicMock()
  mock_check_pipelining_required = MagicMock()
  mock_take_step = MagicMock()
  mock__get_worker_processes = MagicMock()
  mock__get_workers = MagicMock()
  mock__load_included_file = MagicMock()
  mock__copy_included_file = MagicMock()
  mock_get_host_list_cache = MagicMock() 
  mock_get_hosts_from_pattern = MagicMock()

  # object under test
  strategy_module = StrategyModule()



# Generated at 2022-06-13 15:21:53.786697
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.plugins import callback_loader, module_loader
    from ansible.playbook.task import Task
    from ansible.plugins.callback import CallbackBase

    tqm=TaskQueueManager(
        inventory=InventoryManager(loader=DataLoader(), sources=[]),
        variable_manager=VariableManager(),
        loader=DataLoader(),
        options=None,
        passwords=None,
        stdout_callback='default',
    )
    iterator = Play().post_validate(None, None)
    iterator._iterator_

# Generated at 2022-06-13 15:22:02.031041
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    ''' unit test for StrategyModule'''

    variable_manager = VariableManager()
    loader = DataLoader()
    tqm = TaskQueueManager(
        inventory=None,
        variable_manager=variable_manager,
        loader=loader,
        passwords=None,
        stdout_callback=None,
        run_additional_callbacks=False,
        run_tree=False,
    )

    strategy = StrategyModule(tqm)
    assert strategy


# Generated at 2022-06-13 15:22:08.522199
# Unit test for method run of class StrategyModule

# Generated at 2022-06-13 15:24:54.388558
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    # create an instance of the class to be tested. Any parameters needed for the class
    # are put in a dictionary with the key being an identifier for the parameter.
    # The dictionary is passed to the constructor.
    strategymodule = StrategyModule()

    # create a mock TQM object.  The mock object will allow you to
    # stub out the methods the class you are testing actually uses
    # so you can control the data returned from those methods.  You
    # can also use the mock to make sure that the methods were
    # actually called.

    tqm_instance = MagicMock(name="QueueManager")
    tqm_instance.RUN_OK = 0
    tqm_instance.RUN_FAILED_BREAK_PLAY = 1
    tqm_instance.RUN_UNKNOWN_ERROR = 255
    tqm

# Generated at 2022-06-13 15:24:55.361542
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_module = StrategyModule()
    assert strategy_module



# Generated at 2022-06-13 15:25:01.968752
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    print("**** TEST ****")
    test_tqm = None
    test_iterator = None
    test_play_context = None
    test_strategy_module = StrategyModule(test_tqm, test_iterator, test_play_context)
    try:
        test_strategy_module.run(test_iterator, test_play_context)
    except Exception as e:
        print(e.args)


# Generated at 2022-06-13 15:25:11.729393
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    import random

# Generated at 2022-06-13 15:25:21.556407
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = Mock()
    tqm._failed_hosts = dict()
    tqm._unreachable_hosts = dict()
    tqm._stats = Collector()
    tqm._stdout_callback = Default(verbosity=4)
    tqm._terminated = False
    tqm._workers_lock = Lock()
    tqm.send_callback = Mock(return_value=None)
    tqm.RUN_OK = 2
    tqm.RUN_FAILED_BREAK_PLAY = 4
    tqm.RUN_UNKNOWN_ERROR = 16

    loader = Mock()
    loader.load_basedir = Mock(return_value=None)
    loader.path_dwim_relative = Mock(return_value=None)
    loader.path_d

# Generated at 2022-06-13 15:25:22.586495
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    s=StrategyModule()
    assert (s.run('',''))

# Generated at 2022-06-13 15:25:24.300331
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
	test_strategy_module = StrategyModule()

# Generated at 2022-06-13 15:25:26.225696
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    my_obj = StrategyModule()
    a = my_obj.run(iterator, play_context)
    assert a  

# Generated at 2022-06-13 15:25:27.797195
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_module = StrategyModule(None, None, None)
    assert strategy_module


# Generated at 2022-06-13 15:25:29.401639
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    # ansible.RunCmdLine.Options_initialize()
    return
