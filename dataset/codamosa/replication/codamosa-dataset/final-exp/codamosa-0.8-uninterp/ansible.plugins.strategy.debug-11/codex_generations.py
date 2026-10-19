

# Generated at 2022-06-13 14:55:29.250228
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    assert True == StrategyModule(tqm).debugger_active, "Error - incorrect constructor"
    return True



# Generated at 2022-06-13 14:55:30.430128
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy = StrategyModule(None)
    assert strategy.debugger_active is True



# Generated at 2022-06-13 14:55:38.489699
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    import ansible.playbook.task
    import ansible.playbook.play
    import ansible.playbook.task_include
    import ansible.playbook.handler
    import ansible.vars.manager
    import ansible.inventory.host
    import ansible.inventory.group
    import ansible.executor.task_queue_manager
    import ansible.executor.process.worker
    import ansible.executor.action_result
    import ansible.playbook.play_context

    print("Unit test for constructor of class StrategyModule")

    task = ansible.playbook.task.Task()
    task._role = None
    task.action = 'setup'
    task_objects = [task]
    play_context = ansible.playbook.play_context.PlayContext()
    play = ansible.playbook

# Generated at 2022-06-13 14:55:43.049813
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # Unit test for constructor of class StrategyModule
    # Create mock object for class TaskQueueManager
    class TaskQueueManager:
        pass
    tqm = TaskQueueManager()
    sm = StrategyModule(tqm)
    assert sm.tqm == tqm
    assert sm.debugger_active == True

# An interactive shell for debugging

# Generated at 2022-06-13 14:55:50.186620
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # Generate a fake 'ansible' object
    ansible = type('ansible', (object,), {'debugger': {} })

    # Generate a fake 'TaskQueueManager' object
    tqm = type('tqm', (object,), {'ansible': ansible})

    # Instantiate StrategyModule
    strategy_module = StrategyModule(tqm)
    assert strategy_module.debugger_active is True

# Add on_file_diff callback to StrategyModule

# Generated at 2022-06-13 14:55:52.763062
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = object()
    mod = StrategyModule(tqm)
    assert isinstance(mod, LinearStrategyModule)
    assert not (mod.debugger_active)


# Generated at 2022-06-13 14:55:54.548873
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    sm = StrategyModule(None)
    return sm



# Generated at 2022-06-13 14:55:55.673828
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    module = StrategyModule()
    assert module.debugger_active == True


# Generated at 2022-06-13 14:55:56.568714
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass


# Generated at 2022-06-13 14:55:57.592278
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True


# Generated at 2022-06-13 14:56:07.516899
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    class FakeOptions(object):
        verbosity = 2
        inventory = './my-hosts.ini'
        vault_password_files = []
        forks = 99

    class FakeData:
        class LocalTaskTarget(object):
            def __init__(self, hostname):
                self.name = hostname

        class Task(object):
            def __init__(self, name):
                self.name = name
                self.action = '/bin/sleep'
                self.environment = {}

# Generated at 2022-06-13 14:56:16.912077
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.playbook.play import Play
    from ansible.plugins.strategy.linear import StrategyModule as LinearStrategyModule
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.utils.vars import load_extra_vars
    from ansible.utils.vars import load_options_vars
    from ansible.utils.vars import merge_hash
    from ansible.config.manager import load_config_file
    from ansible.errors import AnsibleError

    config = load_config_file()
    config_data

# Generated at 2022-06-13 14:56:19.439424
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # instatiate a class
    strategy_module = StrategyModule(tqm)
    # check if strategy_module.debugger_active is True
    assert strategy_module.debugger_active == True


# Generated at 2022-06-13 14:56:21.219487
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # Arrange - N/A
    # Act - N/A
    # Assert - N/A
    assert StrategyModule(tqm) == StrategyModule(tqm)


# Generated at 2022-06-13 14:56:22.876445
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    mod = StrategyModule(None)
    assert mod.debugger_active == True
    assert mod.tqm == None

# Generated at 2022-06-13 14:56:23.407835
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass



# Generated at 2022-06-13 14:56:25.172693
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule(tqm=None) is not None


# Generated at 2022-06-13 14:56:29.906691
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    print("test_StrategyModule")
    strategy_test = StrategyModule(tqm)
    print("debugger_active: " + str(strategy_test))
    assert strategy_test.debugger_active == True


# Generated at 2022-06-13 14:56:33.477533
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm._final_q = None
    tqm._failed_hosts = None
    tqm._stats = None
    StrategyModule.__init__(StrategyModule, tqm)
    assert True


# Generated at 2022-06-13 14:56:34.103235
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass


# Generated at 2022-06-13 14:56:47.399443
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
  # Define a test case in which the debugger_active should be initialized to True.
  debugger_active_test_case = {
    'debugger_active': True
  }

  # Create StrategyModule class object for the defined test case, and check if the
  # debugger_active is initialized properly.
  tqm = None
  strategy_module = StrategyModule(tqm)
  if strategy_module.debugger_active != debugger_active_test_case['debugger_active']:
    print('Test failed. Expected debugger_active to be initialized to %s, but got %s.' \
          % (debugger_active_test_case['debugger_active'], strategy_module.debugger_active))
    raise Exception

  print('All tests passed.')


# Generated at 2022-06-13 14:56:51.356862
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = null
    sm = StrategyModule(tqm)
    assert sm.debugger_active == True


# Generated at 2022-06-13 14:56:54.080897
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = mock.MagicMock()
    m = StrategyModule(tqm)
    assert not m.save_failed_hosts
    assert tqm == m._tqm
    assert not m.stats
    assert not m.failed_hosts
    assert m.get_hosts_remaining_to_run() == []
    assert m.strategy == 'debug'
# End of test case


# Generated at 2022-06-13 14:56:56.677418
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    sm = StrategyModule()
    assert sm.tqm
    assert sm.get_host_list
    assert sm.add_tasks
    assert sm.save_load_cache

# Generated at 2022-06-13 14:56:58.419040
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule.__doc__
    assert StrategyModule.__init__.__doc__


# Generated at 2022-06-13 14:56:59.702154
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert isinstance(strategy_module, StrategyModule)


# Generated at 2022-06-13 14:57:00.550068
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    StrategyModule()



# Generated at 2022-06-13 14:57:01.705103
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    sm = StrategyModule(None)
    assert(sm.debugger_active)


# Generated at 2022-06-13 14:57:03.402266
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    strategy = StrategyModule(tqm)
    assert strategy.debugger_active == True


# Generated at 2022-06-13 14:57:04.481200
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass
    # assert strategy_module.debugger_active == True



# Generated at 2022-06-13 14:57:13.183145
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    mock_tqm = object()
    assert isinstance(StrategyModule(mock_tqm), LinearStrategyModule)

tqm = object()
strategy_module = StrategyModule(tqm)
sys.modules[__name__] = strategy_module

# Generated at 2022-06-13 14:57:14.548005
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy = StrategyModule(None)
    assert strategy.debugger_active == True


# Generated at 2022-06-13 14:57:18.581513
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    action_plugin = object()
    display = object()
    loader = object()
    variable_manager = object()
    shared_loader_obj = object()
    inventory = object()
    task_queue_manager = MockTaskQueueManager(action_plugin, display, loader, variable_manager, shared_loader_obj, inventory)
    assert isinstance(task_queue_manager.strategy, StrategyModule)
    assert (task_queue_manager.strategy.tqm == task_queue_manager)


# Generated at 2022-06-13 14:57:20.422197
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    TASK_QUEUE_MANAGER = []
    strategy = StrategyModule(TASK_QUEUE_MANAGER)


# Generated at 2022-06-13 14:57:31.492258
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    
    #import needed class not found in current scope
    import ansible.plugins.loader
    import ansible.plugins.callback
    import ansible.utils.display
    import ansible.playbook
    import ansible.inventory.manager
    import ansible.parsing.dataloader
    
    #instantiate needed classes
    dataloader = ansible.parsing.dataloader.DataLoader()
    inventory = ansible.inventory.manager.InventoryManager(loader=dataloader, sources='localhost')
    variable_manager = ansible.playbook.variable_manager.VariableManager(loader=dataloader, inventory=inventory)
    loader = ansible.plugins.loader.PluginLoader(None)
    display = ansible.utils.display.Display()

# Generated at 2022-06-13 14:57:32.116789
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass



# Generated at 2022-06-13 14:57:44.102512
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    print("StrategyModule: __init__")
    import ansible.utils.shlex as shlex
    import ansible.plugins.loader as plugin_loader
    import ansible.parsing.dataloader as loader
    import ansible.vars as vars
    import ansible.vars.manager as vars_manager

    parser = option_parser()
    options, args = parser.parse_args()

    loader = loader.DataLoader()
    inventory = Inventory(loader=loader, variable_manager=variables, host_list='dummy_hosts_file')
    tqm = TaskQueueManager(model=inventory, loader=loader, options=options, passwords=None, stdout_callback=None)


# Generated at 2022-06-13 14:57:45.464163
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    command_module = StrategyModule(tqm)
    assert command_module



# Generated at 2022-06-13 14:57:46.863574
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    m = StrategyModule(tqm=None)
    assert m.debugger_active == True


# Generated at 2022-06-13 14:57:48.169592
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # TODO : Write unit test

    return True


# Generated at 2022-06-13 14:58:04.601093
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    play = dict(
        name="foo.yml",
        hosts=["localhost"],
        roles=[],
        gather_facts=True,
        tasks=[]
    )


# Generated at 2022-06-13 14:58:08.014007
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert(strategy.__name__ == 'StrategyModule')
    assert(strategy.__module__ == 'ansible.plugins.strategy.debug')
    assert(isinstance(strategy.__doc__, str))


# Generated at 2022-06-13 14:58:10.334772
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_module = StrategyModule(tqm)
    assert strategy_module is not None
    assert strategy_module.debugger_active == True



# Generated at 2022-06-13 14:58:11.724609
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    test_object = StrategyModule()
    assert test_object is not None

# Generated at 2022-06-13 14:58:14.323818
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_module = StrategyModule(tqm={})
    assert strategy_module != None
    assert strategy_module.debugger_active == True
    assert strategy_module.display.verbosity == 4


# Generated at 2022-06-13 14:58:25.361891
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    class TestTqm:
        pass
    tqm = TestTqm()
    tqm.stats = Stats()
    tqm._failed_hosts = dict()
    tqm.inventory = dict()
    tqm.inventory.get_hosts = lambda pattern: ['localhost']
    strategyModule = StrategyModule(tqm)
    assert strategyModule.get_next_task_lockfile == '/tmp/ansible_%s.retry' % 'localhost'
    assert strategyModule.tqm is tqm
    assert strategyModule.host_state_map == {'localhost': HostState('localhost')}
    assert strategyModule.host_state_map['localhost'].task_vars == dict()
    assert strategyModule.host_state_map['localhost'].result is None
    assert strategyModule.host

# Generated at 2022-06-13 14:58:26.201602
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    sm = StrategyModule


# Generated at 2022-06-13 14:58:28.659473
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = 'test'
    strategy_module = StrategyModule(tqm)
    assert strategy_module.debugger_active == True

# Simple class to implement the cmd interface

# Generated at 2022-06-13 14:58:29.883920
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    s = StrategyModule(None)
    assert s.debugger_active


# Generated at 2022-06-13 14:58:30.815311
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule(None)


# Generated at 2022-06-13 14:58:48.389939
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    sm = StrategyModule(object)
    assert sm.debugger_active is True

# Test that isinstance(strategy_module, LinearStrategyModule)

# Generated at 2022-06-13 14:58:52.489383
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    test_tqm = pprint.pformat(['ansible_module_name', 'encoding', 'connection',
                               'module_args', 'module_compression', 'module_vars'])
    assert StrategyModule(test_tqm) is not None


# Generated at 2022-06-13 14:58:54.049761
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # test instantiation
    sm = StrategyModule(None)

    # test attributes of class StrategyModule
    assert sm.debugger_active


# Generated at 2022-06-13 14:58:54.940465
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    StrategyModule()


# Generated at 2022-06-13 14:58:56.111174
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    return StrategyModule(tqm)


# Generated at 2022-06-13 14:59:04.802857
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # Create a fake task manager for test.
    class FakeTaskQueueManager:
        class Callbacks:
            pass
        def __init__(self):
            self.callbacks = self.Callbacks()
            self.index = {}
            self.host_vars = []
    tqm = FakeTaskQueueManager()

    class FakeTask:
        def __init__(self, host):
            self.host = host

    # Create a fake inventory for test.
    class FakeInventory:
        class Host:
            def __init__(self, hostname):
                self.name = hostname

        def __init__(self):
            self.hosts = []
        def add_host(self, hostname):
            self.hosts.append(self.Host(hostname))

    fake_inventory = FakeInventory()
   

# Generated at 2022-06-13 14:59:12.720054
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.executor.task_queue_manager import TaskQueueManager
    tqm = TaskQueueManager(
            inventory=None,
            variable_manager=None,
            loader=None,
            options=None,
            passwords=None,
            stdout_callback=None,
            run_additional_callbacks=True,
            run_tree=False,
            )
    tqm._final_q = None

    sm = StrategyModule(tqm)
    assert sm.tqm == tqm
    assert sm.debugger_active


# Generated at 2022-06-13 14:59:13.772585
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule



# Generated at 2022-06-13 14:59:17.917982
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    global TASK_QUEUE_MANAGER
    global STR
    TASK_QUEUE_MANAGER = None
    STR = StrategyModule(TASK_QUEUE_MANAGER)
    print (STR)

# Generated at 2022-06-13 14:59:21.186955
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    my_strategy = StrategyModule(None)
    assert isinstance(my_strategy, LinearStrategyModule)
    assert my_strategy.debugger_active


# Generated at 2022-06-13 14:59:55.407590
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule(tqm = tqm)

# Test for method 'get_host_list'

# Generated at 2022-06-13 15:00:03.796846
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.executor.task_queue_manager import TaskQueueManager
    def _task_executor(self, host, task, task_vars, play_context):
        return None
    TaskQueueManager._task_executor = _task_executor
    tqm = TaskQueueManager(
        inventory=None,
        variable_manager=None,
        loader=None,
        options=None,
        passwords=None,
        stdout_callback=None,
    )
    sm = StrategyModule(tqm=tqm)
    assert type(sm) == StrategyModule
# END unit test


# Generated at 2022-06-13 15:00:05.328362
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True
# ---------------------------------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------------------------------

# Generated at 2022-06-13 15:00:08.026703
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    print("\nTest constructor of class StrategyModule:")
    # TODO: How to instantiate class StrategyModule
    # strategy_module = StrategyModule()


# Generated at 2022-06-13 15:00:08.608410
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass



# Generated at 2022-06-13 15:00:09.175843
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True


# Generated at 2022-06-13 15:00:09.700972
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True



# Generated at 2022-06-13 15:00:10.431113
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass



# Generated at 2022-06-13 15:00:11.431581
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    StrategyModule._test_instance()

    Debugger._test_instance()



# Generated at 2022-06-13 15:00:12.036149
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True


# Generated at 2022-06-13 15:01:26.012678
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True



# Generated at 2022-06-13 15:01:26.866689
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule("test")

# Generated at 2022-06-13 15:01:27.470844
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True


# Generated at 2022-06-13 15:01:28.986177
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = object
    assert (StrategyModule(tqm) is not None)


# Generated at 2022-06-13 15:01:32.702691
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    '''Test function for creating StrategyModule class'''
    test_tqm = 'Not-None'
    strategy_module = StrategyModule(test_tqm)
    assert strategy_module.debugger_active == True


# Generated at 2022-06-13 15:01:33.685640
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True


# Generated at 2022-06-13 15:01:41.934458
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = mock_class()
    strategy_module = StrategyModule(tqm)
    assert strategy_module.tqm == tqm
    assert strategy_module.display is None
    assert strategy_module.host_pinned is False
    assert strategy_module.hostname_pinned is False
    assert strategy_module.debugger_active is True
    assert strategy_module.step is False
    assert strategy_module.breakpoints == []
    assert strategy_module.breakpoints_set == []
    assert type(strategy_module.debugger) == Debugger
    assert strategy_module.debugger.prompt == ''


# Generated at 2022-06-13 15:01:42.303730
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True



# Generated at 2022-06-13 15:01:43.673945
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    class TestTaskQueueManager():
        pass
    tqm = TestTaskQueueManager()
    strategy = StrategyModule(tqm)
    assert strategy.debugger_active == True


# Generated at 2022-06-13 15:01:44.695277
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    sm = StrategyModule(None)
    assert sm.debugger_active == True


# Generated at 2022-06-13 15:04:18.208010
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    sm = StrategyModule(None)
    assert sm.debugger_active


# Generated at 2022-06-13 15:04:19.418925
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = StrategyModule(None)
    assert tqm is not None


# Generated at 2022-06-13 15:04:20.646749
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    m = StrategyModule(None)
    assert m.debugger_active is True


# Generated at 2022-06-13 15:04:21.836040
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    print ("test_StrategyModule")
    assert StrategyModule



# Generated at 2022-06-13 15:04:22.435712
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule
    assert LinearStrategyModule



# Generated at 2022-06-13 15:04:32.377404
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    task_queue_manager = cmd.Cmd()
    # Bypass try-except
    setattr(task_queue_manager, 'loader', 'loader')
    setattr(task_queue_manager, 'variable_manager', 'variable_manager')
    setattr(task_queue_manager, 'shared_loader_obj', 'shared_loader_obj')

    # Stack trace shows the memory address of task_queue_manager.
    print('task_queue_manager: ', task_queue_manager, file=sys.stderr)

    strategy_module = StrategyModule(task_queue_manager)

    print(strategy_module.debugger_active, file=sys.stderr) # True
    print(strategy_module.tqm, file=sys.stderr) # <ansible.plugins.strategy.debug.StrategyModule object

# Generated at 2022-06-13 15:04:40.075443
# Unit test for constructor of class StrategyModule

# Generated at 2022-06-13 15:04:40.861242
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    obj = StrategyModule
    assert obj



# Generated at 2022-06-13 15:04:42.973096
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = 'tqm'
    s = StrategyModule(tqm)
    assert s.debugger_active == True
    assert s.tqm == 'tqm'



# Generated at 2022-06-13 15:04:45.190441
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = object()
    try:
        strategy_module = StrategyModule(tqm)
        assert strategy_module.debugger_active is True
    except:
        assert False
