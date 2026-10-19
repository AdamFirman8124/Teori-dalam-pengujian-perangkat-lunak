

# Generated at 2022-06-13 14:55:32.873649
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # Mock
    tqm = 1
    # Test
    strategy = StrategyModule(tqm)
    # Check
    assert strategy.debugger_active == True


# Generated at 2022-06-13 14:55:34.064081
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule(None).debugger_active


# Generated at 2022-06-13 14:55:34.566479
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True == True

# Generated at 2022-06-13 14:55:43.668598
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.utils.display import Display
    from ansible.plugins import strategy_loader
    from ansible.inventory import Inventory
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.executor.task_queue_manager import TaskQueueManager

    loader = DataLoader()
    display = Display()
    inventory = Inventory(loader=loader, variable_manager=VariableManager(loader=loader), host_list='localhost')
    variable_manager = VariableManager(loader=loader, inventory=inventory)


# Generated at 2022-06-13 14:55:46.048535
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule
    assert LinearStrategyModule
    assert StrategyModule.debugger_active


# Generated at 2022-06-13 14:55:48.417173
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass
#     debugger_active = True;
#     self.assertEqual(self.debugger_active, debugger_active)


# Generated at 2022-06-13 14:55:50.738808
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    import ansible.plugins.strategy.debug
    ansible.plugins.strategy.debug.StrategyModule(None)


# Generated at 2022-06-13 14:55:52.482453
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    st = StrategyModule(tqm=None)
    assert st.debugger_active



# Generated at 2022-06-13 14:55:58.120687
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.executor.task_queue_manager import TaskQueueManager
    tqm = TaskQueueManager( # pylint: disable=unexpected-keyword-arg
        inventory=None,
        variable_manager=None,
        loader=None,
        options=None,
        passwords=None,
    )
    s = StrategyModule(tqm)
    assert s.debugger_active is True


# Generated at 2022-06-13 14:56:02.227989
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    ms = StrategyModule(None)
    assert ms.run is not None
    assert ms.run_playbook is not None
    assert ms.run_async is not None
    assert ms.cleanup is not None
    assert ms.debugger_active is True


# Generated at 2022-06-13 14:56:04.093603
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule.debugger_active


# Generated at 2022-06-13 14:56:05.216160
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True


# Generated at 2022-06-13 14:56:06.208241
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert(str(StrategyModule))



# Generated at 2022-06-13 14:56:09.406196
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # Create a object of class StrategyModule
    test = StrategyModule(tqm=None)

    # Check if DEBUGGER_ACTIVE is set to True
    assert( test.debugger_active == True)
    

# Generated at 2022-06-13 14:56:18.275210
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    '''
    Test StrategyModule Class constructor
    '''
    import ansible.playbook.task.dynamic
    import ansible.playbook.task_include
    import ansible.playbook.handler
    import ansible.playbook.task
    task1 = ansible.playbook.task.dynamic.Task('init 1')
    strategy = StrategyModule(task1)
    assert strategy.tqm == task1
    task2 = ansible.playbook.task_include.TaskInclude('init 2')
    strategy = StrategyModule(task2)
    assert strategy.tqm == task2
    task3 = ansible.playbook.handler.Handler('init 3')
    strategy = StrategyModule(task3)
    assert strategy.tqm == task3

# Generated at 2022-06-13 14:56:25.793558
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible import context
    from ansible.utils.vars import merge_hash
    from ansible.parsing.dataloader import DataLoader


# Generated at 2022-06-13 14:56:27.126204
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    stragegy = StrategyModule(tqm)
    assert stragegy.debugger_active == True



# Generated at 2022-06-13 14:56:35.296653
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    class TestTqm:
        pass
    tqm = TestTqm()
    print("TEST: Create StrategyModule")
    sm = StrategyModule(tqm)
    if not isinstance(sm, LinearStrategyModule) or not isinstance(sm, StrategyModule):
        raise Exception("StrategyModule constructor failed")
    if not isinstance(sm.tqm, TestTqm):
        raise Exception("StrategyModule constructor failed: tqm")
    if sm.debugger_active != True:
        raise Exception("StrategyModule constructor failed: debugger_active")
    print("TEST PASSED")



# Generated at 2022-06-13 14:56:36.567533
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    sm = StrategyModule(tqm)


# Generated at 2022-06-13 14:56:38.081684
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    print("StrategyModule()")



# Generated at 2022-06-13 14:56:40.958626
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True

# Generated at 2022-06-13 14:56:41.499589
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass


# Generated at 2022-06-13 14:56:42.787549
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    m = StrategyModule(None)

# Returns the strategy class object

# Generated at 2022-06-13 14:56:44.071824
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # TODO: Need implementation
    return 0



# Generated at 2022-06-13 14:56:44.930471
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = ''
    sm = StrategyModule(tqm)
    assert sm.debugger_active == True




# Generated at 2022-06-13 14:56:47.056970
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # self.debugger_active = True
    # assert self.debugger_active == True
    print("test_StrategyModule: passed")



# Generated at 2022-06-13 14:56:52.586760
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    sys.modules["ansible.plugins.strategy.debug"] = sys.modules["__main__"]
    from ansible.plugins.strategy.debug import StrategyModule
    strategy = StrategyModule(tqm)
    assert strategy.debugger_active is True


# Generated at 2022-06-13 14:56:55.108376
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = 0
    strategy_module = StrategyModule(tqm)
    assert strategy_module.debugger_active == True


# Generated at 2022-06-13 14:56:55.707723
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True



# Generated at 2022-06-13 14:57:02.243681
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    import ansible.plugins.strategy.linear as linear
    class Fake_TQM(object):
        def __init__(self):
            self.hostvars = None
    tqm = Fake_TQM()
    x = StrategyModule(tqm)
    assert x.tqm.__class__ == tqm.__class__
    assert x.tqm.hostvars == tqm.hostvars
    assert x.get_host_list() == []
    assert x.get_failed_hosts() == []
    assert x.get_changed_hosts() == []
    assert x.run() is True
    assert x.strategy == 'debug'
    assert x.parallelism == 0
    assert x.can_start == 0
    assert x.rlimits == [[0,0]]

# Generated at 2022-06-13 14:57:07.627234
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True


# Generated at 2022-06-13 14:57:08.535459
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass


# Generated at 2022-06-13 14:57:14.064352
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = ''
    
    # Constructor for tqm
    strategy_module = StrategyModule(tqm)
    # Assert tqm
    assert strategy_module.tqm == tqm
    # Assert debugger_active
    assert strategy_module.debugger_active == True


# Generated at 2022-06-13 14:57:15.076796
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # TODO - write unit test after class StrategyModule is defined
    assert True


# Generated at 2022-06-13 14:57:15.790478
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass


# Generated at 2022-06-13 14:57:18.175505
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    sm = StrategyModule(tqm=None)
    if not sm:
        raise Exception("Failed to create object of class StrategyModule.")
    if sm.debugger_active != True:
        raise Exception("The value of property debugger_active is not correct.")

# Generated at 2022-06-13 14:57:19.674792
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy = StrategyModule(tqm)
    assert strategy != None
    assert strategy.debugger_active == True



# Generated at 2022-06-13 14:57:22.492238
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    print('Executing test_StrategyModule')
    # Arrange
    # TODO: Add code here

    # Act
    # TODO: Add code here

    # Assert
    # TODO: Add code here


# Generated at 2022-06-13 14:57:27.211103
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    obj = StrategyModule(tqm)
    assert obj.testModuleName == "debug"
    assert obj.testModuleType == "strategy"
    assert obj.debugger_active


# Generated at 2022-06-13 14:57:31.107519
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.playbook import PlayBook
    from ansible.inventory import Inventory
    from ansible.executor.task_queue_manager import TaskQueueManager
    playbook = PlayBook.load('test_playbook.yml', 'local')
    inventory = Inventory.load('test_inventory.yml', 'local')
    tqm = TaskQueueManager(playbook, inventory)
    StrategyModule(tqm)


# Generated at 2022-06-13 14:57:43.879439
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = object()
    strategy_module = StrategyModule(tqm)
    assert strategy_module.tqm == tqm
    assert not strategy_module.runner_queued
    assert not strategy_module.host_pinned
    assert strategy_module.debugger_active


# Generated at 2022-06-13 14:57:44.858995
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass


# Generated at 2022-06-13 14:57:53.390990
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.utils.unicode import to_unicode
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.vars.manager import VariableManager
    from ansible.executor import task_queue_manager

    # Setup
    inventory = InventoryManager(None, '/dev/null')
    play_context = PlayContext(remote_addr='127.0.0.1')
    play = Play().load({'name': 'play name', 'hosts': 'localhost', 'gather_facts': 'no', 'tasks': [{'action': 'debug'}]})
    variable_manager = VariableManager(loader=None)

# Generated at 2022-06-13 14:58:00.408572
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_module = StrategyModule({"foo": "bar"})
    assert strategy_module.tqm == {"foo": "bar"}
    assert strategy_module.queue_name == 'debug_queue'
    assert strategy_module.results_queue_name == 'debug_results_queue'
    assert strategy_module.queue_terms == {}
    assert strategy_module.variable_manager == None
    assert strategy_module.current_task == None
    assert strategy_module.debugger_active == True

# class Cmd method to execute the command
import pprint

# Generated at 2022-06-13 14:58:01.190170
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    StrategyModule(None)


# Generated at 2022-06-13 14:58:01.960750
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert(StrategyModule)


# Generated at 2022-06-13 14:58:12.747771
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    import ansible.utils.vars as ansible_vars
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.inventory import Inventory
    from ansible.vars.manager import VariableManager
    from ansible.vars.hostvars import HostVars

    ansible_vars.__OPTIONS = []
    ansible_vars.__OPTIONS.append('inventory=./tests/unit/module_utils/inventory/debug_inventory')

# Generated at 2022-06-13 14:58:23.536849
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    print("Unit test for constructor of class StrategyModule")
    # Note1: When calling the constructor of class 'linear.StrategyModule'
    # directly, an exception occurs such as "TypeError: Error when calling the
    # metaclass bases module.__init__() takes at most 2 arguments (3 given)".
    # Note2: The following statements work fine.
    #        from ansible.plugins.strategy.linear import StrategyModule
    #        strategy = StrategyModule()
    from ansible.plugins.strategy.debug import StrategyModule as LinearStrategyModule
    task_queue_manager = object()
    strategy = LinearStrategyModule(task_queue_manager)
    pprint.pprint(vars(strategy))
    print()


# Generated at 2022-06-13 14:58:32.440904
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert 'StrategyModule' == StrategyModule.__name__


# unit test for execute_nowait_iterable
# TODO


# unit test for wait_for_event
# TODO


# unit test for run
# TODO


# unit test for run_handlers
# TODO


# unit test for cleanup_tasks
# TODO


# unit test for execute_tasks
# TODO


# unit test for start_debugger
# TODO


# unit test for get_vars
# TODO


# unit test for get_host_vars
# TODO


# unit test for get_host_vars
# TODO


# unit test for get_play_vars
# TODO


# unit test for get_task_vars
# TODO


# unit test for _cmd

# Generated at 2022-06-13 14:58:36.029563
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # Test 1: Constructor of class StrategyModule
    tqm = None
    strategy_module = StrategyModule(tqm)

    assert strategy_module is not None, \
        'StrategyModule constructor UnitTest failed'


# Generated at 2022-06-13 14:58:53.653572
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # pylint: disable=no-member
    assert isinstance(StrategyModule(), LinearStrategyModule)



# Generated at 2022-06-13 14:58:54.559053
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule(None).debugger_active


# Generated at 2022-06-13 14:58:55.500804
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True


# Class Debugger

# Generated at 2022-06-13 14:58:56.912545
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert (StrategyModule)

# Generated at 2022-06-13 14:59:03.367523
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    """
    Unit test for constructor of class StrategyModule
    """
    tqm = 'tqm'
    sm = StrategyModule(tqm)

    assert sm.tqm == tqm, \
        'Constructor of class StrategyModule should set tqm to value passed'

    assert type(sm.debugger_active) is bool, \
        'Constructor of class StrategyModule should set debugger_active to bool'

    assert sm.debugger_active == True, \
        'Constructor of class StrategyModule should set debugger_active to True'


# Generated at 2022-06-13 14:59:04.584373
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    StrategyModule(tqm)



# Generated at 2022-06-13 14:59:14.462061
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.play_iterator import PlayIterator
    from ansible.plugins import action_loader
    from ansible.playbook.play import Play
    from ansible.vars.manager import InventoryManager
    import ansible.constants as C

    loader = action_loader.ActionModuleLoader()

    hosts = ['localhost']
    inventory = InventoryManager(loader=loader, sources=['localhost,'])
    inventory.add_group('local')
    inventory.add_host(host=hosts[0], group='local')
    inventory.reconcile_inventory()


# Generated at 2022-06-13 14:59:19.935759
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = "abc"
    strategy_module = StrategyModule(tqm)
    assert strategy_module.name == 'debug'
    assert strategy_module.display == 'debug'
    assert isinstance(strategy_module.debugger_active, bool)
    assert strategy_module.debugger_active == True


# Generated at 2022-06-13 14:59:29.147170
# Unit test for constructor of class StrategyModule

# Generated at 2022-06-13 14:59:31.508275
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = DummyTQM()
    strategy = StrategyModule(tqm)
    assert strategy.debugger_active is True, "%r != %r" % (strategy.debugger_active, True)



# Generated at 2022-06-13 15:00:14.305653
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    import datetime
    from ansible import constants as C
    from ansible.inventory.manager import InventoryManager
    from ansible.task_queue_manager import TaskQueueManager
    from ansible.vars.manager import VariableManager

    # Create dummy inventory
    inv_path = '/home/kishin/git/ansible/ansible/test/integration/inventory'
    inventory = InventoryManager(loader=None, sources=inv_path)

    # Create dummy variable manager
    variable_manager = VariableManager(
        loader=None,
        inventory=inventory,
        version_info=C.ansible_version_info
    )

    # Create dummy task queue manager

# Generated at 2022-06-13 15:00:18.121405
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    s = StrategyModule(None)
    assert s.debugger_active == True, 'value of debugger_active is not True'

    s.debugger_active = False
    assert s.debugger_active == False, 'value of debugger_active is not False'

    s.debugger_active = True
    assert s.debugger_active == True, 'value of debugger_active is not True'


# Generated at 2022-06-13 15:00:21.074165
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    parser_mock = 'parser_mock'
    tqm = 'tqm'
    assert StrategyModule(tqm) == StrategyModule(tqm)


# Generated at 2022-06-13 15:00:21.958026
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True


# Generated at 2022-06-13 15:00:25.082648
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = '''
        TaskQueueManager for play #1 (test)
        '''
    strategy = StrategyModule(tqm)

    assert strategy.debugger_active

# Generated at 2022-06-13 15:00:25.774262
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass


# Generated at 2022-06-13 15:00:35.047976
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    config = {
        'host_list': ['localhost'],
        'module_path': None,
        'pattern': 'test',
        'remote_pass': None,
        'remote_user': 'ansible',
        'roles_path': [],
        'become': False,
        'become_method': 'sudo',
        'become_user': None,
        'verbosity': 3,
    }

    host_list = ['localhost']

    task_queue_manager = type('TaskQueueManager', (object,), {})
    task_queue_manager.config = config
    task_queue_manager.host_list = host_list
    task_queue_manager.stats = type('Stats', (object,), {})

# Generated at 2022-06-13 15:00:37.323978
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None

    strategy = StrategyModule(tqm)

    assert strategy.debugger_active is True


# Generated at 2022-06-13 15:00:38.098745
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass



# Generated at 2022-06-13 15:00:38.645920
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True



# Generated at 2022-06-13 15:02:01.766449
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = 'tqm'
    strategy_module = StrategyModule(tqm)
    assert strategy_module.debugger_active == True


# Generated at 2022-06-13 15:02:10.100188
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # Dummy TaskQueueManager
    tqm = None
    # Invoke the constructor
    strategy = StrategyModule(tqm)
    # Verify initial values
    assert strategy.debugger_active == True
    assert strategy.inventory == None
    assert strategy.play is None
    assert strategy.all_hosts is None
    assert strategy.unreachable_hosts == dict()
    assert strategy.stats is None
    assert strategy.variable_manager is None
    assert strategy.loader is None
    assert strategy.tqm_failed is False
    assert strategy.tqm_unreachable is False
    assert strategy.tqm_failed_hosts == dict()
    assert strategy.tqm_unreachable_hosts == dict()
    assert strategy.tqm_changed_hosts == dict()
    assert strategy.tq

# Generated at 2022-06-13 15:02:17.565105
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = object()
    s = StrategyModule(tqm)
    assert s.runner_queue == []
    assert s.tqm == tqm
    assert s.host_consumed_results == {}
    assert s.host_status_results == {}
    assert s.host_skipped_results == {}
    assert s.host_failure_results == {}
    assert s.host_unreachable_results == {}


# Generated at 2022-06-13 15:02:21.901355
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # Test that new class object instantiated correctly
    test_object = StrategyModule()
    assert hasattr(test_object, "get_host_list")
    assert hasattr(test_object, "add_tasks")
    assert hasattr(test_object, "run_tasks")




# Generated at 2022-06-13 15:02:23.401643
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy = StrategyModule('test_TQM')
    assert strategy is not None


# Generated at 2022-06-13 15:02:24.537300
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    assert StrategyModule(tqm)


# Generated at 2022-06-13 15:02:25.349946
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True


# Generated at 2022-06-13 15:02:34.487079
# Unit test for constructor of class StrategyModule

# Generated at 2022-06-13 15:02:37.796452
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # test constructor
    s = StrategyModule(tqm=None)
    assert s.debugger_active == True


# Generated at 2022-06-13 15:02:38.740069
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
  assert True
