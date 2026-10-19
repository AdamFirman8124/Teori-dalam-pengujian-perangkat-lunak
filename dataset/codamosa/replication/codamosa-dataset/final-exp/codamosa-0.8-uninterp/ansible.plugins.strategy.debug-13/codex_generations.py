

# Generated at 2022-06-13 14:55:26.318564
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
   assert True


# execute is a method of class StrategyModule

# Generated at 2022-06-13 14:55:28.383046
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = ['tqm']
    assert StrategyModule(tqm)


# Generated at 2022-06-13 14:55:28.948595
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule


# Generated at 2022-06-13 14:55:29.822415
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    fail()


# Generated at 2022-06-13 14:55:31.708673
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    StrategyModule(tqm)

if __name__ == '__main__':
    test_StrategyModule()

# Generated at 2022-06-13 14:55:39.392204
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    import ansible.utils.vars
    import ansible.task
    import ansible.playbook.task_include
    import ansible.playbook
    import ansible.inventory
    import ansible.plugins.strategy.debug
    from ansible.plugins.strategy import StrategyBase
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group

    #pylint: disable=invalid-name
    class TestAttrDict(dict):
        _ansible_no_log = False
        def __getattr__(self, attr):
            return self.get(attr)
    #pylint: enable=invalid-name

    import ansible.executor
    import ansible.callbacks
    from ansible.executor.task_queue_manager import TaskQueueManager

# Generated at 2022-06-13 14:55:40.265399
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule


# Generated at 2022-06-13 14:55:42.312765
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    sm = StrategyModule(__name__)
    assert sm.tqm == __name__
    assert sm.debugger_active == True


# Generated at 2022-06-13 14:55:44.659982
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    strategy_module = StrategyModule(tqm)
    assert strategy_module.debugger_active == True



# Generated at 2022-06-13 14:55:47.076886
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_module = StrategyModule(1)
    assert strategy_module.debugger_active == True


# Generated at 2022-06-13 14:55:49.100970
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True


# Generated at 2022-06-13 14:55:51.046265
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    test_instance = StrategyModule(None)
    assert isinstance(test_instance, StrategyModule)
    assert test_instance.debugger_active == True


# Generated at 2022-06-13 14:55:52.540065
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
   assert callable(StrategyModule.__init__)


# Generated at 2022-06-13 14:56:02.814051
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    class DummyTQM(object):
        pass
    tqm = DummyTQM()
    tqm.stats = DummyTQM()
    tqm.inventory = DummyTQM()
    tqm.inventory.get_groups_dict = lambda: {}
    tqm.inventory.get_hosts = lambda: []
    tqm.stdout_callback = 'debug'
    tqm.options = DummyTQM()
    tqm.options.listhosts = True
    tqm.options.subset = None
    tqm.options.syntax = None
    tqm.options.connection = 'ssh'
    tqm.options.module_path = None
    tqm.options.forks = 5

# Generated at 2022-06-13 14:56:06.112915
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # Test case 1
    tqm.result_q = MagicMock()
    assert_that(StrategyModule(tqm).result_q, tqm.result_q)


# Generated at 2022-06-13 14:56:08.077512
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    testmoduleObj = StrategyModule(None)
    assert testmoduleObj.debugger_active == True


# Generated at 2022-06-13 14:56:17.329717
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.playbook.play_context       import PlayContext
    from ansible.playbook.task               import Task
    from ansible.vars.reserved               import Reserved
    from ansible.inventory.host              import Host
    from ansible.inventory.group             import Group
    from ansible.inventory.manager           import InventoryManager
    from ansible.plugins.strategy.linear     import StrategyModule
    from ansible.utils.display               import Display
    display = Display()
    def load_options(self):
        pass
    Task.load_options = load_options
    Reserved.__init__ = load_options
    PlayContext.__init__ = load_options
    StrategyModule.__init__ = load_options
    InventoryManager.__init__ = load_options

# Generated at 2022-06-13 14:56:18.383388
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
  try:
      StrategyModule('test')
  except:
      assert False

# Generated at 2022-06-13 14:56:19.593292
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule.__doc__
    assert StrategyModule.__init__.__doc__

# Generated at 2022-06-13 14:56:20.405917
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    exit(0)


# Generated at 2022-06-13 14:56:24.481363
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
  print("Unit test for StrategyModule class constructor")
  tqm = object
  strategy_module = StrategyModule(tqm)
  assert strategy_module.debugger_active == True

Sys_argv = []


# Generated at 2022-06-13 14:56:36.966427
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    sys.modules.pop('ansible.errors', None)
    sys.modules.pop('ansible.parsing.dataloader', None)
    sys.modules.pop('ansible.playbook.play', None)
    sys.modules.pop('ansible.playbook.play_context', None)
    sys.modules.pop('ansible.playbook.task_include', None)
    sys.modules.pop('ansible.vars.manager', None)
    sys.modules.pop('ansible.vars.host_variable_manager', None)
    sys.modules.pop('ansible.vars.task_variable_manager', None)

    from ansible.errors import AnsibleError
    from ansible.plugins.loader import strategy_loader, action_loader
    from ansible.playbook.play import Play

# Generated at 2022-06-13 14:56:37.918053
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True


# Generated at 2022-06-13 14:56:42.400247
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
  # Arrange
  tqm = "tqm"

  # Act
  actual = StrategyModule(tqm)
  debugger_active = actual.debugger_active

  # Assert
  assert debugger_active == True



# Generated at 2022-06-13 14:56:51.252580
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # Make sure StrategyModule is a subclass of LinearStrategyModule
    assert issubclass(StrategyModule, LinearStrategyModule)

    # The following is trying to test the method of constructor
    # It is really hard to do it, so just do some "intermediate" test
    # The following is to test whether __init__() can be successfully called in python
    class tqm_mock(object):
        def __init__(self):
            pass
    tqm = tqm_mock()
    strategy_module = StrategyModule(tqm)
    assert strategy_module.debugger_active == True

    # test the first statement in __init__
    strategy_module2 = LinearStrategyModule(tqm)
    assert strategy_module2.get_host_list() == []


# A mock class of Cmd

# Generated at 2022-06-13 14:56:53.128150
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule(object) is not None

# Executing StrategyModule unit test

# Generated at 2022-06-13 14:56:54.957403
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    ss = StrategyModule(None)
    assert(ss.debugger_active == True)


# Generated at 2022-06-13 14:56:57.840336
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    print("Test for the constructor of class StrategyModule")
    tqm = MockTQM()
    test_instance = StrategyModule(tqm)
    assert test_instance.debugger_active


# Generated at 2022-06-13 14:57:00.151798
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    sys.argv = ['ansible-playbook', 'debugger.yml', '-i', 'localhost,', '-c', 'local']
    tqm = AnsiblePlaybookDebugger()
    strategy_instance = StrategyModule(tqm)


# Generated at 2022-06-13 14:57:02.865606
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    import ansible.plugins.strategy.debug
    tqm = ansible.plugins.strategy.debug.StrategyModule(tqm=None)
    assert tqm.name == 'debug'
    assert tqm.tqm is None
    assert tqm.debugger_active



# Generated at 2022-06-13 14:57:13.180023
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    class TQM():
        def __init__(self):
            self.hostvars = [{'host': 'host', 'host_name': 'host_name'}]

    tqm = TQM()
    sm = StrategyModule(tqm)
    assert sm.tqm == tqm
    assert sm.debugger_active == True


# Generated at 2022-06-13 14:57:14.233631
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule.__doc__



# Generated at 2022-06-13 14:57:15.015814
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    StrategyModule(tqm=42)


# Generated at 2022-06-13 14:57:16.083342
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    st = StrategyModule(0)
    assert(st)



# Generated at 2022-06-13 14:57:16.858191
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    a = StrategyModule()
    assert a.debugger_active == True


# Generated at 2022-06-13 14:57:20.422887
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    import ansible.plugins.strategy.debug
    print('test_StrategyModule')
    
    # Test default constructor
    strategy_debug_obj = ansible.plugins.strategy.debug.StrategyModule('test_tqm')
    assert strategy_debug_obj.debugger_active, 'StrategyModule constructor initializes the debugger_active to True'

# test_StrategyModule()

# Generated at 2022-06-13 14:57:23.407797
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    mock_tqm = 'mock_tqm'
    assert mock_tqm
    strategy = StrategyModule(mock_tqm)
    assert strategy.debugger_active is True


# Generated at 2022-06-13 14:57:24.261042
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule


# Generated at 2022-06-13 14:57:26.199164
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # Do not call __init__() directly
    # StrategyModule(tqm)
    pass


# Generated at 2022-06-13 14:57:29.430918
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule is not None
    assert StrategyModule is not LinearStrategyModule
    strategy_module = StrategyModule()
    assert strategy_module is not None
    assert strategy_module.debugger_active is True


# Generated at 2022-06-13 14:57:41.003344
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # TODO: should be changed to create a class mocker
    tqm = MockTqm()
    m = StrategyModule(tqm)
    assert(isinstance(m, LinearStrategyModule))
    assert(m.tqm == tqm)


# Generated at 2022-06-13 14:57:42.998988
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule(tqm=None)
    return True



# Generated at 2022-06-13 14:57:45.879852
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule.__doc__ == LinearStrategyModule.__doc__

if __name__ == '__main__':
    import pytest
    pytest.main([__file__])

# Generated at 2022-06-13 14:57:47.204950
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule(None).debugger_active == True



# Generated at 2022-06-13 14:57:48.812992
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    str_m = StrategyModule(1)
    assert str_m.debugger_active


# Generated at 2022-06-13 14:57:50.458191
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    sys.argv.append("")
    t = Strategies.StrategyModule()


# Generated at 2022-06-13 14:57:51.689153
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule(None)


# Generated at 2022-06-13 14:58:02.042573
# Unit test for constructor of class StrategyModule

# Generated at 2022-06-13 14:58:03.296219
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass

    # assert class StrategyModule(..)



# Generated at 2022-06-13 14:58:04.883591
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule


# Generated at 2022-06-13 14:58:23.572588
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    print("Testing constructor of class StrategyModule...")
    assert StrategyModule.__name__ == 'StrategyModule'
    assert isinstance(StrategyModule(None), LinearStrategyModule)
    print("Done!")


# Generated at 2022-06-13 14:58:25.796956
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = {}
    strategy = StrategyModule(tqm)
    assert strategy.debugger_active == True

####################
# Interactive debugger
####################


# Generated at 2022-06-13 14:58:29.597898
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    class DummyTQM(object):
        def __init__(self):
            self.stats = dict()
            self.hostvars = dict()
            self.host_list = dict()
    tqm = DummyTQM()
    StrategyModule(tqm)


# Generated at 2022-06-13 14:58:30.135384
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True



# Generated at 2022-06-13 14:58:33.066686
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.plugins.strategy.linear import StrategyModule
    assert issubclass(StrategyModule, object)
    assert StrategyModule.__module__ == StrategyModule.__module__
    assert StrategyModule.__doc__ == StrategyModule.__doc__



# Generated at 2022-06-13 14:58:39.258665
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    tqm = TaskQueueManager(inventory=InventoryManager(loader=None, sources=[]))
    tqm._final_q = None
    tqm._inventory = None
    tqm._variable_manager = VariableManager(loader=None, inventory=tqm.inventory)
    tqm._loader = None
    tqm._stats = None
    strategy_module = StrategyModule(tqm)
    assert isinstance(strategy_module, StrategyModule)


# Generated at 2022-06-13 14:58:42.226657
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert isinstance(StrategyModule(None), LinearStrategyModule)
    assert StrategyModule(None).debugger_active == True


# Generated at 2022-06-13 14:58:45.048352
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # Test constructor with null data
    strategyModule = StrategyModule(None)

    # Test created object
    assert strategyModule



# Generated at 2022-06-13 14:58:51.985048
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    class test_tqm:
        def __init__(self):
            self.stats = {}
            self.hosts = {}
    class test_inventory:
        def __init__(self):
            self.hosts = []
    class test_play:
        def __init__(self):
            self.name = 'test play'
            self.hosts = []
    # Main
    tqm = test_tqm()
    tqm.inventory = test_inventory()
    tqm.play = test_play()
    strategy = StrategyModule(tqm)
    assert strategy
    assert strategy.debugger_active is True


# Generated at 2022-06-13 14:58:53.583722
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    tsm = StrategyModule(tqm)
    assert tsm.debugger_active is True


# Generated at 2022-06-13 14:59:31.238100
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    class TestStrategyModule(object):
        hosts = ['localhost']
        DEBUG = True
    test = TestStrategyModule()
    class TestTQM(object):
        def __init__(self, **kwargs):
            pass
    test_tqm = TestTQM(**dict(inventory=test, variable_manager=test, loader=test, options=test))
    mod_debug = StrategyModule(test_tqm)
    assert(mod_debug.debugger_active == True)



# Generated at 2022-06-13 14:59:32.444787
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
  print("Testing argument constructor")
  print("Testing StrategyModule")


# Generated at 2022-06-13 14:59:34.523094
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_module = StrategyModule(None)
    assert strategy_module.debugger_active == True

# ----
# This is the cli used to interact with the debugger.
# ----

# Generated at 2022-06-13 14:59:37.603166
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    sys.argv = [sys.argv[0]]
    tqm = StrategyModule()
    assert(tqm.debugger_active)

# Basic unit test for check_conditional_result

# Generated at 2022-06-13 14:59:38.241534
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # This function should pass without exception
    StrategyModule(tqm)


# Generated at 2022-06-13 14:59:40.899891
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    module = StrategyModule(tqm=None)
    assert module.debugger_active == True


# Generated at 2022-06-13 14:59:44.182882
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pp = pprint.PrettyPrinter()
    str_module = StrategyModule(None)
    pp.pprint(str_module)
    assert str_module.debugger_active
    assert str_module.host_pinned is None


# Generated at 2022-06-13 14:59:45.304493
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    StrategyModule(None)


# Generated at 2022-06-13 14:59:46.889547
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    #raise NotImplementedError()
    pass


# Generated at 2022-06-13 14:59:48.376416
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule(1).debugger_active == True


# Generated at 2022-06-13 15:00:58.844934
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    StrategyModule('test_StrategyModule')

# Generated at 2022-06-13 15:01:01.043691
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    import mock
    tqm = mock.MagicMock()
    StrategyModule(tqm)
    assert 'StrategyModule' == StrategyModule.__name__


# Generated at 2022-06-13 15:01:01.898559
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert(True)


# Generated at 2022-06-13 15:01:06.447146
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = ['tqm']
    strategy = StrategyModule(tqm)
    assert 'debug' == strategy.get_name()
    assert tqm == strategy._tqm
    assert strategy.debugger_active == True



# Generated at 2022-06-13 15:01:09.423954
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule
    assert type(StrategyModule) == type
    assert issubclass(StrategyModule, LinearStrategyModule)
    assert StrategyModule.__module__ == __name__

# Generated at 2022-06-13 15:01:14.445690
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    class Dummy(object):
        def __init__(self):
            self.run_callbacks = []
            self.stats = None
            self.results_callback = None
    tqm = Dummy()

    strategy = StrategyModule(tqm)
    assert strategy.get_host_list(tasks=[]) == set()
    assert strategy.get_next_task_lockfn(play=None) == None


# Generated at 2022-06-13 15:01:18.710048
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.plugins.loader import strategy_loader
    from ansible.utils.debug import debug

    strategy = strategy_loader.all(class_only=True)['debug']

    # Set the debug flag True
    debug.set_debug_value(True)
    # tqm is None
    strategy_obj = strategy(None)
    # Show strategy_obj
    pprint.pprint(vars(strategy_obj))
    


# Generated at 2022-06-13 15:01:19.715104
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True


# Generated at 2022-06-13 15:01:22.764191
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    s = StrategyModule(None)
    assert s._tqm == None
    assert s.debugger_active == True


# Generated at 2022-06-13 15:01:23.662099
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    StrategyModule(None)


# Generated at 2022-06-13 15:04:06.499004
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    try:
        from collections import namedtuple
        TaskQueueManager = namedtuple('TaskQueueManager', ['_final_q'])

        tasks = []
        taskQueueManager = TaskQueueManager(tasks)
        strategyModule = StrategyModule(taskQueueManager)
    except Exception as e:
        assert False



# Generated at 2022-06-13 15:04:12.743741
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    def mocked_TaskQueueManager(connection_info, passwords):
        class MockedTaskQueueManager:
            def __init__(self, connection_info, passwords):
                self.stats = dict(processed=dict(ok=0, failures=0, dark=0),
                                  dark=dict(ok=0, failures=0, skipped=0))
                self._pending_results = 42
                self._non_local_exit_result = 42
                self.worker_responses = None
                self.patched_terminate_workers = None
                self.patched_terminate_loaders = None
        return MockedTaskQueueManager(connection_info, passwords)

    tqm = mocked_TaskQueueManager(None, None)
    strategy_module = StrategyModule(tqm)
    assert strategy_module.debugger_active
   

# Generated at 2022-06-13 15:04:17.045656
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert isinstance(StrategyModule, object)
    assert issubclass(StrategyModule, LinearStrategyModule)
    assert StrategyModule.__name__ == "StrategyModule"
    assert StrategyModule.__doc__ == None
    assert StrategyModule.debugger_active == True



# Generated at 2022-06-13 15:04:25.019108
# Unit test for constructor of class StrategyModule
def test_StrategyModule():

    try:
        # import is needed to get a reference to the BaseTaskExecutor class
        # that is defined in the base_executor.py file.
        from ansible.plugins.loader import action_loader
    except Exception as e:
        raise Exception("Failed to import ansible.plugins.loader.action_loader: {0}".format(e))

    # Check if ansible.plugins.action.debug exists.
    # If so, import it and find the class name.
    module_name = "ansible.plugins.action.debug"
    module_meta = __import__(module_name)
    class_name = None
    for part in module_name.split(".")[1:]:
        if not hasattr(module_meta, part):
            break
        module_meta = getattr(module_meta, part)
   

# Generated at 2022-06-13 15:04:34.950636
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    class Top(cmd.Cmd):
        def do_exec(self, arg):
            return True
    tqm = Top()
    tqm.callbacks = Top()
    tqm.stdout = sys.stdout
    tqm.stdin = sys.stdin
    tqm.vars = dict(x='x', y='y')
    tqm.inventory = 'inventory.yml'
    tqm.play = dict(name='k', hosts='localhost')
    tqm.playbook = pprint.pformat(dict(
        playbook='playbooks/debug.yml',
        play_uuid='e9dba4ea-6f4c-4e4d-8d6e-be84000a17b9'
    ))
    StrategyModule(tqm)

# Generated at 2022-06-13 15:04:44.093601
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    class FakeTqm(object):
        def __init__(self, host_list, module_vars, ansible_opts):
            self.host_list = host_list
            self.module_vars = module_vars
            self.ansible_opts = ansible_opts

    tqm = FakeTqm(
        host_list = "fake_host_list",
        module_vars = "fake_module_vars",
        ansible_opts = "fake_ansible_opts"
    )

    strategy = StrategyModule(tqm)

    assert strategy.tqm == tqm
    assert strategy.host_list == "fake_host_list"
    assert strategy.module_vars == "fake_module_vars"

# Generated at 2022-06-13 15:04:49.665570
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ConfigParser import SafeConfigParser
    from ansible import constants as C
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.inventory import Inventory
    from ansible.vars import VariableManager

    def get_config(config_file):
        config = SafeConfigParser()
        config.read(config_file)
        return config

    config_file = '/path/to/ansible.cfg'
    config = get_config(config_file)
    options = []
    passwords = {}
    inventory = Inventory(loader=None, host_list="localhost")
    variable_manager = VariableManager(loader=None, inventory=inventory)

# Generated at 2022-06-13 15:04:50.952293
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # call constructor function
    ansible.plugins.strategy.debug.StrategyModule(None)
    # did it execute without errors?
    assert True


# Generated at 2022-06-13 15:04:52.594956
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule.__init__
    assert LinearStrategyModule.__init__


# Generated at 2022-06-13 15:04:54.078713
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    t_StrategyModule = StrategyModule("tqm")
    return t_StrategyModule.debugger_active

