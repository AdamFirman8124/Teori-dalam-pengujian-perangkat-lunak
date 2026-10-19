

# Generated at 2022-06-13 15:06:30.253534
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    FreeStrategyModule()

# Generated at 2022-06-13 15:06:32.967006
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.executor.task_queue_manager import TaskQueueManager
    tqm = TaskQueueManager(None)
    sm = StrategyModule(tqm)
    assert hasattr(sm, "_host_pinned")

# Generated at 2022-06-13 15:06:34.224323
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    """Unit test for constructor of class StrategyModule"""
    pass

# Generated at 2022-06-13 15:06:35.775954
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    my_strategy_module = StrategyModule(tqm={})
    assert my_strategy_module is not None

# Generated at 2022-06-13 15:06:36.432334
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True

# Generated at 2022-06-13 15:06:38.116193
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    sm = StrategyModule(tqm)
    assert sm._host_pinned == True

# Generated at 2022-06-13 15:06:40.051574
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule.__name__ == 'StrategyModule'
    assert StrategyModule.__doc__ == 'Host pinned strategy plugin, which runs tasks without interruption'

# Generated at 2022-06-13 15:06:40.414664
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    StrategyModule()

# Generated at 2022-06-13 15:06:45.023714
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    '''
    Unit test for constructor of class StrategyModule
    '''
    tqm = None
    strategy = StrategyModule(tqm)
    assert strategy is not None
    assert strategy._host_pinned is True
    assert strategy._inventory is None
    assert strategy._tqm is None
    assert strategy._runners is None
    assert strategy._final_q is None
    assert strategy._blocked_hosts is None
    assert strategy._blocker_hosts is None

# Generated at 2022-06-13 15:06:46.326113
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    obj = StrategyModule(True)
    assert obj._host_pinned == True

# Generated at 2022-06-13 15:06:49.247945
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule.__name__ == 'StrategyModule'
    assert StrategyModule.__doc__ == FreeStrategyModule.__doc__

# Generated at 2022-06-13 15:06:50.961040
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    value1 = StrategyModule(tqm='tqm')
    assert value1 is not None

# Generated at 2022-06-13 15:06:51.838572
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule



# Generated at 2022-06-13 15:06:54.446851
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    mock_tqm = []
    strategy_mod = StrategyModule(mock_tqm)
    assert strategy_mod is not None
    assert strategy_mod._host_pinned

# Generated at 2022-06-13 15:06:55.167292
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule(tqm)._host_pinned == True

# Generated at 2022-06-13 15:06:56.323204
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass


# Generated at 2022-06-13 15:06:59.199111
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = mock.Mock(name='tqm')
    assert isinstance(StrategyModule(tqm), FreeStrategyModule)



# Generated at 2022-06-13 15:07:00.012184
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass

# Generated at 2022-06-13 15:07:04.278043
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from units.mock.loader import DictDataLoader
    from units.mock.inventory import Host
    from units.mock.runner import Runner

    loader = DictDataLoader({
        "strategy_plugin/host_pinned.py": "",
        "host_pinned/hosts.yml": ""
    })
    host = Host("host_pinned")
    tqm = Runner(loader=loader, inventory=[host])
    strategy = StrategyModule(tqm)
    assert strategy._host_pinned == True

# Generated at 2022-06-13 15:07:04.928655
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule != None

# Generated at 2022-06-13 15:07:08.170928
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    s = StrategyModule(tqm)
    assert s is not None
    assert s._host_pinned is True
    assert s._tqm is None
    assert s._batch_size is None
    assert s._display is not None
    assert isinstance(s._display, Display)

# Generated at 2022-06-13 15:07:09.793544
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule(tqm="test")
    assert StrategyModule(tqm="test")._host_pinned

# Generated at 2022-06-13 15:07:12.613827
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    arg1 = object()
    strategy_module = StrategyModule(arg1)
    assert strategy_module._host_pinned == True

# Generated at 2022-06-13 15:07:13.686075
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # empty constructor
    StrategyModule()

# Generated at 2022-06-13 15:07:15.686736
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # Setup the StrategyModule object
    strategy = StrategyModule()
    # Check if it is created successfully
    assert strategy is not None


# Generated at 2022-06-13 15:07:18.206082
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_modules = StrategyModule(None)
    assert strategy_modules._host_pinned == True

# test_StrategyModule()

# Generated at 2022-06-13 15:07:20.785849
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_module = StrategyModule(tqm)
    assert(strategy_module._host_pinned);

# Generated at 2022-06-13 15:07:25.277063
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    import ansible.plugins
    import ansible.plugins.loader
    module = ansible.plugins.loader.get_strategy_plugin('host_pinned')
    strategy = module(None)
    assert hasattr(strategy, '_host_pinned') and strategy._host_pinned == True

# Generated at 2022-06-13 15:07:25.922923
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass

# Generated at 2022-06-13 15:07:27.368735
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    x = StrategyModule(tqm = tqm)
    assert x._host_pinned == True

# Generated at 2022-06-13 15:07:32.378135
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule.__init__(StrategyModule, tqm) == None

# Generated at 2022-06-13 15:07:33.389336
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass


# Generated at 2022-06-13 15:07:34.502674
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    StrategyModule(tqm=None)

# Generated at 2022-06-13 15:07:40.639082
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible_collections.ansible.community.plugins.strategy.host_pinned.strategy_module import StrategyModule
    # TQM object is required
    tqm1 = None
    # TQM initialized in constructor of FreeStrategyModule
    tqm2 = object()
    assert StrategyModule(tqm1) is not None, "'tqm' parameter is not required"
    assert StrategyModule(tqm2) is not None, "object initialized correctly when 'tqm' is given"
test_StrategyModule()

# Generated at 2022-06-13 15:07:42.101340
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    _tqm = 0
    _StrategyModule = StrategyModule(_tqm)


# Generated at 2022-06-13 15:07:48.594172
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # Tests for the StrategyModule constructor

    def test_empty_task_queue_manager():
        strategy_module = StrategyModule(tqm={})
        assert strategy_module._host_pinned

    def test_task_queue_manager():
        tqm = {'_inventory': {},
               '_final_q': {},
               '_host_pinned': True,
               '_load_callbacks': {},
               '_start_at_done': [],
               '_play': {'_itervalues': []}}
        strategy_module = StrategyModule(tqm=tqm)
        assert strategy_module._host_pinned

if __name__ == "__main__":
    test_StrategyModule()

# Generated at 2022-06-13 15:07:49.696249
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    m_module = StrategyModule(tqm)

# Generated at 2022-06-13 15:08:00.935417
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.plugins.strategy.host_pinned import StrategyModule
    from ansible.plugins.strategy import debug
    from ansible.utils.display import Display
    display = Display()

# Generated at 2022-06-13 15:08:03.424551
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    print('Testing for constructor of class StrategyModule')
    strategy_module = StrategyModule('tqm')
    assert strategy_module._host_pinned == True



# Generated at 2022-06-13 15:08:15.255367
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    s = StrategyModule(None)
    # instance = StrategyModule(tqm)
    # instance.add_tqm_variables(variables, play)
    # instance.get_next_task_lockfds(host)
    # instance.get_next_task_for_host(host, peek=False)
    # instance.get_variables(play, host, task)
    # instance.on_file_diff(host, res)
    # instance.on_any_file_diff(host, res)
    # instance.on_failed(host, res, ignore_errors=False)
    # instance.on_ok(host, host_result)
    # instance.on_skipped(host, host_result)
    # instance.on_unreachable(host, res)
    # instance.save_load_

# Generated at 2022-06-13 15:08:24.385948
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule



# Generated at 2022-06-13 15:08:25.094650
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass

# Generated at 2022-06-13 15:08:31.380302
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass
    # /usr/local/lib/python2.7/dist-packages/ansible/plugins/strategy/host_pinned.py:29:
    # def __init__(self, tqm):
    #     super(StrategyModule, self).__init__(tqm)
    #     self._host_pinned = True

# Generated at 2022-06-13 15:08:35.345468
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.playbook.task_queue_manager import TaskQueueManager
    tqm = TaskQueueManager(None, None)
    sm = StrategyModule(tqm)
    assert sm._host_pinned == True

# Generated at 2022-06-13 15:08:36.225874
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    StrategyModule(tqm = None)

# Generated at 2022-06-13 15:08:37.155878
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule.__init__

# Generated at 2022-06-13 15:08:38.457285
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass

# Generated at 2022-06-13 15:08:44.781423
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # Setup
    from ansible.playbook.play import Play
    from ansible.inventory.manager import InventoryManager
    from ansible.executor.task_queue_manager import TaskQueueManager

    tqm = TaskQueueManager(
        None,
        inventory=InventoryManager(None, ['localhost']),
        variable_manager=None,
        loader=None,
        options=None,
        passwords=None,
        stdout_callback='default',
    )

    # Act
    strategy = StrategyModule(tqm)

    # Assert
    assert strategy._host_pinned is True

# Generated at 2022-06-13 15:08:47.420988
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy = StrategyModule(True)
    assert strategy._host_pinned == True

# Generated at 2022-06-13 15:08:48.007722
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    StrategyModule(None)

# Generated at 2022-06-13 15:09:06.292397
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert issubclass(StrategyModule, FreeStrategyModule)

# Generated at 2022-06-13 15:09:07.242213
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule(tqm = None)

# Generated at 2022-06-13 15:09:08.751999
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_module = StrategyModule(None)
    assert strategy_module._host_pinned == True

# Generated at 2022-06-13 15:09:09.840462
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert issubclass(StrategyModule, FreeStrategyModule)

# Generated at 2022-06-13 15:09:13.959500
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from lib.ansible.executor.task_queue_manager import TaskQueueManager
    tqm = TaskQueueManager('root', [], None, None, None, None, None, None)
    sm = StrategyModule(tqm)
    assert sm._host_pinned == True

# Generated at 2022-06-13 15:09:15.168411
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_module = StrategyModule(tqm='tqm')
    assert strategy_module._host_pinned is True

# Generated at 2022-06-13 15:09:18.136903
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # Instantiate the test object
    obj = StrategyModule("tqm")
    # Return the result
    return True

# Generated at 2022-06-13 15:09:28.423805
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    global display
    display = Display()
    tqm = dict()
    tqm['args'] = dict()
    tqm['args']['private_key_file'] = '~/.ssh/id_rsa'
    tqm['args']['host_list'] = 'hosts'
    tqm['args']['forks'] = 10
    tqm['args']['timeout'] = 10
    tqm['args']['connection'] = 'ssh'
    tqm['args']['module_path'] = '/usr/lib/python2.6/site-packages/ansible/modules/'
    tqm['args']['subset'] = None
    tqm['args']['check'] = False
    tqm['args']['syntax'] = False


# Generated at 2022-06-13 15:09:33.232703
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    old_stdout, old_stderr = sys.stdout, sys.stderr
    output_stdout = io.StringIO()
    output_stderr = io.StringIO()
    try:
        sys.stdout, sys.stderr = output_stdout, output_stderr
        sm = StrategyModule(None)
        assert hasattr(sm, '_host_pinned')
    finally:
        sys.stdout, sys.stderr = old_stdout, old_stderr

# Generated at 2022-06-13 15:09:35.519431
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None

    T = StrategyModule(tqm)
    assert T
    assert T._host_pinned == True

# Generated at 2022-06-13 15:10:15.648971
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    host_pinned_strategy_plugin = StrategyModule(tqm='tqm')
    assert host_pinned_strategy_plugin._host_pinned == True

# Generated at 2022-06-13 15:10:18.821160
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    host = StrategyModule()
    assert host.name == "host_pinned"


# Generated at 2022-06-13 15:10:19.455203
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass

# Generated at 2022-06-13 15:10:20.820267
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
   tqm = []
   StrategyModule(tqm)

# Generated at 2022-06-13 15:10:26.685481
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.plugins.strategy.host_pinned import StrategyModule
    from ansible.plugins.strategy.host_pinned import test_StrategyModule as test_host_pinned
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.playbook.play import Play
    from ansible.inventory.host import Host, Inventory
    from ansible.inventory.group import Group
    from ansible.vars import VariableManager

    def test_task_queue_manager(loop):
        group = Group('all')
        group.add_host(Host('host1'))
        group.add_host(Host('host2'))
        group.add_host(Host('host3'))

        inventory = Inventory()
        inventory.add_group(group)
        variable_manager = VariableManager()


# Generated at 2022-06-13 15:10:27.252795
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule

# Generated at 2022-06-13 15:10:27.782902
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule

# Generated at 2022-06-13 15:10:28.789070
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule.__name__ == 'StrategyModule'

# Generated at 2022-06-13 15:10:30.430346
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    """
    Create StrategyModule object
    """
    strategy = StrategyModule({})
    assert strategy._host_pinned is True

# Generated at 2022-06-13 15:10:37.580811
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule
    strategy_module = StrategyModule
    assert strategy_module
    assert strategy_module.__init__
    assert callable(strategy_module.__init__)
    assert strategy_module.__init__.__class__ == MethodType
    assert_equal(strategy_module.__init__.__code__.co_argcount,2)
    assert hasattr(strategy_module, '__init__')
    assert hasattr(strategy_module.__init__, '__call__')
    assert hasattr(strategy_module.__init__, '__code__')
    assert hasattr(strategy_module.__init__, '__defaults__')
    assert hasattr(strategy_module.__init__, '__globals__')

# Generated at 2022-06-13 15:12:14.347066
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass

# Generated at 2022-06-13 15:12:14.755905
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass

# Generated at 2022-06-13 15:12:26.166666
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    host_pinned = True
    serial = None
    limit = None
    pattern = None
    forks = 100
    enabled = True
    run_tree = True
    module_path = None
    display = Display()
    inventory = None
    loader = None
    variable_manager = None
    shared_loader_obj = None
    strategy = StrategyModule(host_pinned, serial, limit, pattern, forks, enabled, run_tree, display, inventory, loader, variable_manager, shared_loader_obj, module_path)
    assert strategy._host_pinned == True
    assert strategy._have_pending_result == False
    assert strategy._have_task_result == False
    assert strategy._pending_results == {}
    assert strategy._result_prune_count == 100
    assert strategy._tqm._stats is not None
   

# Generated at 2022-06-13 15:12:30.004861
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    import ansible.plugins
    obj = ansible.plugins.strategy.host_pinned.StrategyModule(tqm)
    obj.__init__(tqm)
    assert obj._host_pinned == True
    assert type(obj) == ansible.plugins.strategy.host_pinned.StrategyModule

# Generated at 2022-06-13 15:12:31.477542
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    test_StrategyModule = StrategyModule('')
    assert test_StrategyModule is not None


# Generated at 2022-06-13 15:12:33.810986
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # Call constructor of class StrategyModule
    strategy_module = StrategyModule("tqm")
    # Check value of variable _host_pinned after initialize
    assert strategy_module._host_pinned

# Generated at 2022-06-13 15:12:35.901286
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    module = StrategyModule(tqm)
    assert module == 'StrategyModule'


# Generated at 2022-06-13 15:12:46.572826
# Unit test for constructor of class StrategyModule

# Generated at 2022-06-13 15:12:48.754291
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # Test for constructor
    tqm = 'test'
    strategy_module = StrategyModule(tqm)
    assert strategy_module._host_pinned == True

# Generated at 2022-06-13 15:12:49.276493
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass

# Generated at 2022-06-13 15:16:00.017371
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule

# Generated at 2022-06-13 15:16:01.865004
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_module = StrategyModule(tqm=None)
    assert strategy_module._host_pinned



# Generated at 2022-06-13 15:16:04.285824
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.plugins.strategy.host_pinned import StrategyModule as host_pinned_StrategyModule
    def __init__(self, tqm):
        self.__init__(tqm)
        self._host_pinned = True

    assert host_pinned_StrategyModule.__init__ == __init__


# Generated at 2022-06-13 15:16:04.987036
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True

# Generated at 2022-06-13 15:16:06.344990
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule == StrategyModule

# Unit test to check the check if the variable _host_pinned = true

# Generated at 2022-06-13 15:16:07.294637
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert isinstance(StrategyModule, object)

# Generated at 2022-06-13 15:16:08.180917
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True, "This test is ok"

# Generated at 2022-06-13 15:16:09.359697
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    mod = StrategyModule(None)
    assert mod._host_pinned == True

# Generated at 2022-06-13 15:16:11.822486
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = object()
    strategy = StrategyModule(tqm)
    assert strategy._host_pinned == True
    assert strategy._tqm == tqm

# Generated at 2022-06-13 15:16:13.507429
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule != None
    return True
