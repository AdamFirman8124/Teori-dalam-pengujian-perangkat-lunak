

# Generated at 2022-06-13 14:55:26.618256
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    strategy = StrategyModule(tqm)
    assert strategy.debugger_active == True
    assert strategy.tasks_left_to_run == None
    assert strategy.current_task == None


# Generated at 2022-06-13 14:55:29.372463
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_module = StrategyModule()
    assert strategy_module.debugger_active == True
    print("Unit test for constructor of class StrategyModule is Passed")


# Generated at 2022-06-13 14:55:30.227944
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule


# Generated at 2022-06-13 14:55:31.480203
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule.debugger_active == True


# Generated at 2022-06-13 14:55:33.296535
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    try:
        s = StrategyModule(None)
    except Exception as e:
        print (str(e))


# Generated at 2022-06-13 14:55:37.987521
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    print("\n")
    print("Testing constructor for class StrategyModule")
    print("\n")
    test_strategymodule = StrategyModule(None)
    assert(test_strategymodule.debugger_active == True)
    print("Test Successful")
test_StrategyModule()


# Generated at 2022-06-13 14:55:40.371218
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    print('StrategyModule_test_StrategyModule()')
    strategy = StrategyModule()
    assert_equal(strategy.__class__.__name__, 'StrategyModule')


# Generated at 2022-06-13 14:55:51.408530
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    sys.argv.insert(1, '-vvvvv')
    sys.argv.insert(2, '--debugger')

    from ansible import constants as C
    from ansible.playbook import Playbook
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.inventory.manager import InventoryManager

    # For PlaybookExecutor
    playbook = Playbook.load('playbook/playbook-playbook', variable_manager=None, loader=None)

    # For TaskQueueManager
    inventory = InventoryManager(loader=None, sources='inventory/hosts-playbook')
    variable_manager = None
    loader = None

    play_context = Play

# Generated at 2022-06-13 14:55:52.539595
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    print('Test StrategyModule()')


# Generated at 2022-06-13 14:55:53.146635
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass



# Generated at 2022-06-13 14:55:55.604983
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    setattr(StrategyModule, '__init__', test_StrategyModule.__func__)


# Generated at 2022-06-13 14:55:57.741011
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    s = StrategyModule(tqm)
    assert not s is None
    assert s.debugger_active == True


# Generated at 2022-06-13 14:55:58.504376
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True

# Generated at 2022-06-13 14:56:07.517086
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    try:
        from __main__ import display
    except ImportError:
        from ansible.utils.display import Display
        display = Display()

    tqm = mock.Mock(ansible.executor.task_queue_manager.TaskQueueManager)
    tqm.display = display
    tqm._stats = mock.Mock(ansible.executor.task_queue_manager._Stats)
    tqm._loop = mock.Mock(asyncio.base_events.BaseEventLoop)
    tqm._final_q = mock.Mock(asyncio.queues.Queue)
    tqm._inventory = mock.Mock(ansible.inventory.manager.InventoryManager)
    tqm._workers = mock.Mock(ansible.executor.task_queue_manager._Workers)


# Generated at 2022-06-13 14:56:08.293100
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True


# Generated at 2022-06-13 14:56:09.360062
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    print(type(StrategyModule))


# Generated at 2022-06-13 14:56:10.453978
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass



# Generated at 2022-06-13 14:56:13.416554
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = 'not None'
    tqm.vars = {}

    strategy_module = StrategyModule(tqm)

    assert strategy_module.debugger_active == True



# Generated at 2022-06-13 14:56:17.119756
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    sModule = StrategyModule(tqm=None)
    assert sModule.debugger_active, 'StrategyModule.debugger_active is'\
            'not True'

    assert isinstance(sModule, LinearStrategyModule), 'Class StrategyModule is not inherited from'\
            ' class LinearStrategyModule'


# Generated at 2022-06-13 14:56:18.988939
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    '''
    Test Script to test the constructor of the class StrategyModule
    '''
    ctest = StrategyModule('TEST')
    assert ctest is not None


# Generated at 2022-06-13 14:56:21.770093
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    StrategyModule(tqm)



# Generated at 2022-06-13 14:56:28.236262
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    sys.argv = ['ansible-playbook', 'test.yml']
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.parsing.dataloader import DataLoader

    playbook_path = 'test.yml'
    inventory = '/path/to/inventory'

    loader = DataLoader()

    passwords = {}

    pbex = PlaybookExecutor(playbooks=[playbook_path],
                            inventory=inventory,
                            loader=loader,
                            passwords=passwords)

    tqm = TaskQueueManager(
        inventory=inventory,
        variable_manager=pbex._variable_manager,
        loader=loader,
        passwords=passwords
    )


# Generated at 2022-06-13 14:56:33.101340
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.executor import task_queue_manager
    tqm = task_queue_manager.TaskQueueManager(
        inventory=None,
        variable_manager=None,
        loader=None,
        options=None,
        passwords=None,
    )
    s = StrategyModule(tqm)
    assert s is not None


# Generated at 2022-06-13 14:56:34.291891
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # Initialize instance of class StrategyModule
    sm = StrategyModule(None)
    # Assert initial value of property debugger_active
    assert sm.debugger_active



# Generated at 2022-06-13 14:56:35.249897
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    StrategyModule('tqm')



# Generated at 2022-06-13 14:56:37.238892
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    sm = StrategyModule(None)
    assert sm.debugger_active, 'Constructor of class StrategyModule is failed'


# Generated at 2022-06-13 14:56:38.866670
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = object()
    assert isinstance(StrategyModule(tqm), StrategyModule)


# Generated at 2022-06-13 14:56:44.763381
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    class FakeTQM(object):
        def __init__(self):
            self.hosts = dict()
            self.host_vars = dict()
            self.groups = dict()
    tqm = FakeTQM()
    strategy = StrategyModule(tqm)
    assert strategy.tqm == tqm
    assert strategy.debugger_active


# Generated at 2022-06-13 14:56:49.865192
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
  tqm = {'_unreachable_hosts': set([]),
         '_log_messages': [],
         'stats': {'failures': {}, 'skipped': {}, 'ok': {}, 'changed': {}}}
  strategy_module = StrategyModule(tqm)
  assert 'debugger_active' in strategy_module.__dict__
  assert strategy_module.__dict__['debugger_active'] == True


# Generated at 2022-06-13 14:56:54.219369
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    class MockTaskQueueManager:
        pass
    sm = StrategyModule(MockTaskQueueManager())
    assert sm.debugger_active
    assert isinstance(sm, LinearStrategyModule)



# Generated at 2022-06-13 14:57:02.315284
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    print("*** TEST: execute test_StrategyModule() ***")
    tqm = type("TaskQueueManager", (object,), {
        'execute_tasks': lambda self: None,
        'run': lambda self: None,
        'RUN_OK': 0,
    })
    strategy = StrategyModule(tqm)
    assert strategy.tqm is tqm


# Generated at 2022-06-13 14:57:03.164483
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # TODO: need to implement
    assert True



# Generated at 2022-06-13 14:57:07.970881
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    try:
        import ansible.plugins.action.debug_action as Plugin
    except ImportError:
        pass
    else:
        Plugin.StrategyModule('non-null')

try:
    from __main__ import display, CLI
except ImportError:
    from ansible.utils.display import Display
    display = Display()
    CLI = False


# Generated at 2022-06-13 14:57:18.237801
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    sm = StrategyModule(None)
    assert sm.debugger_active

# NOTE: this module does not handle the has_task_events support;
#       the module which uses this one for the execution of tasks,
#       will handle this.

    # This method returns two iterators. One is the task iterator, the other
    # is a state iterator. The advantage of this approach is that all hosts will
    # start executing their first task at the same time, rather than doing all
    # the hosts in one batch, then all the next tasks in another batch, etc.
    def run(self, iterator, play_context):
        state = 1
        task_iterator, state_iterator = self._get_iterator(iterator)

        #Play the states in order:
        all_vars = dict()

# Generated at 2022-06-13 14:57:19.991079
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = MagicMock()
    
    sm = StrategyModule(tqm)

    assert sm.debugger_active == True


# Generated at 2022-06-13 14:57:20.557192
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass



# Generated at 2022-06-13 14:57:29.530263
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    task_queue_manager = "hi"

    class TestStrategyModule:
        def test_init(self):
            test_StrategyModule = StrategyModule(task_queue_manager)
            assert test_StrategyModule.debugger_active == True
    
    test_StrategyModule_instance = TestStrategyModule()
    # run all the tests in class TestStrategyModule
    for name in dir(test_StrategyModule_instance):
        if name.startswith('test_'):
            print(name)
            test_StrategyModule_instance.__getattribute__(name)()


# Generated at 2022-06-13 14:57:32.677431
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    """
    test_StrategyModule
    This function tests instantiating of DebugStrategy class
    """
    tqm = LinearStrategyModule(None)
    strategy = StrategyModule(tqm)
    assert isinstance(strategy, StrategyModule)


# Generated at 2022-06-13 14:57:36.157436
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    try:
        tqm = "tqm"
        StrategyModule.__init__(tqm)
    except Exception as error:
        print(error)
        assert False



# Generated at 2022-06-13 14:57:43.269741
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    import inspect
    import pprint
    import sys

    class MockTqm:
        def __init__(self):
            self.hostvars = {}

    tqm = MockTqm()
    tqm.hostvars = {}
    sm = StrategyModule(tqm)
    sm.queue_task(None, None)

#
# Wrapper for handling callback function to send output to debugger
#

# Generated at 2022-06-13 14:57:55.557388
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    strategy = StrategyModule(tqm)
    assert hasattr(strategy, "debugger_active") == True
    assert strategy.debugger_active == True
    assert hasattr(strategy, "tqm") == True
    assert strategy.tqm == None



# Generated at 2022-06-13 14:57:57.770237
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = True
    obj = StrategyModule(tqm)
    assert tqm is obj._tqm



# Generated at 2022-06-13 14:57:59.993461
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    print("test_StrategyModule")
    # TODO: テスト実装
    print("test_StrategyModule: NG")


# Generated at 2022-06-13 14:58:00.824671
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass

    return True, None

# Generated at 2022-06-13 14:58:01.889057
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    s = StrategyModule(None)
    assert type(s) == StrategyModule


# Generated at 2022-06-13 14:58:02.875367
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass


# Generated at 2022-06-13 14:58:04.412209
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert 1 == 1


# Generated at 2022-06-13 14:58:08.685301
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # test
    # 1. class StrategyModule
    # 2. __init__ - constructor
    # 3. parameters
    #    self, tqm
    # 4. self - Instance of StrategyModule
    # 5. tqm - Instance of TaskQueueManager
    assert True


# Generated at 2022-06-13 14:58:10.936273
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    strategy = StrategyModule(tqm)
    assert strategy.debugger_active == True


# Generated at 2022-06-13 14:58:15.385543
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    print("Testing `__init__` of class StrategyModule")
    tqm = "tqm"
    strategy_module = StrategyModule(tqm)
    assert strategy_module.tqm == "tqm"
    assert strategy_module.debugger_active == True
    print("Successfully passed")


# Generated at 2022-06-13 14:58:34.065676
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # Setup test data
    taskq = TestTaskQueueManager()
    taskq.result_q = [1, 2, 3]
    taskq.host_q = {'host': TestHost}

    # Test constructor of debug module
    sm = StrategyModule(taskq)

    # Test init behavior
    assert isinstance(sm, StrategyModule)

    assert sm.tqm == taskq
    assert sm.debugger_active



# Generated at 2022-06-13 14:58:34.994802
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    sm = StrategyModule(tqm=None)
    assert sm.debugger_active


# Generated at 2022-06-13 14:58:46.766426
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    class Tqm(object):
        def __init__(self):
            self.inventory = ""
            self.extra_vars = ""
            self.passwords = ""
            self.iterator = ""
            self.play = ""
            self.loader = ""
            self.vars_cache = ""
            self.options = ""
            self.shared_loader_obj = ""

        def get_inventory(self):
            return self.inventory

        def get_extra_vars(self):
            return self.extra_vars

        def get_passwords(self):
            return self.passwords

        def get_iterator(self):
            return self.iterator

        def load_callbacks(self):
            return ""

        def host_stack_of_tasks(self, host):
            return ""


# Generated at 2022-06-13 14:58:47.737194
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = StrategyModule("test_tqm")
    return tqm

# Generated at 2022-06-13 14:58:54.335366
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    a = StrategyModule(None)
    assert a
# End of unit test

    def _initialize(self, iterator, play):
        self.play = play
        self.iterator = iterator
        self.inventory = play.inventory
        self.variable_manager = play.get_variable_manager()
        self.all_vars = self.variable_manager.get_vars(self.iterator._play, self.iterator._host, self.iterator)
        self.host_vars = self.variable_manager.get_vars(self.iterator._play, self.iterator._host, self.iterator, 'hostvars')
        self.play_vars = self.variable_manager.get_vars(self.iterator._play, self.iterator._host, self.iterator, 'playvars')
        play_context = play.get_variable

# Generated at 2022-06-13 14:58:57.896413
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = 'tqm' # Doesn't have to be defined
    sm = StrategyModule(tqm)
    assert sm.tqm == 'tqm'
    assert sm.debugger_active == True


# Generated at 2022-06-13 14:58:59.630764
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    test_tqm = None
    assert StrategyModule(test_tqm)


# Generated at 2022-06-13 14:59:01.624987
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = {}
    assert 'debugger_active' in vars(StrategyModule(tqm).__init__)



# Generated at 2022-06-13 14:59:04.364368
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    sm = StrategyModule(None)
    assert type(sm) is StrategyModule
    assert type(sm.debugger_active) is bool
    assert sm.debugger_active


# Generated at 2022-06-13 14:59:05.626712
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    sm = StrategyModule(None)
    assert sm.debugger_active == True


# Generated at 2022-06-13 14:59:40.531872
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    class TaskQueueManager():
        pass
    tqm = TaskQueueManager()
    sm = StrategyModule(tqm)
    assert sm.debugger_active == True


# Generated at 2022-06-13 14:59:42.353060
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    si = StrategyModule(None)
    assert si.debugger_active == True


# Generated at 2022-06-13 14:59:43.708797
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    StrategyModule(tqm)


# Generated at 2022-06-13 14:59:46.941097
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule.__doc__ == '''
    Debugging strategy module.
    '''
    assert StrategyModule.__init__.__doc__ == LinearStrategyModule.__init__.__doc__


# Generated at 2022-06-13 14:59:48.591580
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    class DummyTQM:
        pass
    dummy_tqm = DummyTQM()
    dummy_strategy_module = StrategyModule(dummy_tqm)
    assert dummy_strategy_module.debugger_active



# Generated at 2022-06-13 14:59:50.626040
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = "test"
    strategy_module = StrategyModule(tqm)
    assert strategy_module.debugger_active == True


# Generated at 2022-06-13 14:59:58.683364
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    import os
    import tempfile
    import collections

    class FakeAnsibleActionResult(object):
        def __init__(self, result=None):
            self.hostname = 'hostname'
            self.result = result

    class FakeAnsibleTaskResult(object):
        def __init__(self, hosts=None, hostlist=None):
            self.__hostlist = hostlist
            self.__hosts = hosts or {}
            self.__is_untouched = True

        def __getitem__(self, item):
            if self.__is_untouched:
                self.__is_untouched = False
                return self
            else:
                return FakeAnsibleTaskResult(self.__hosts, self.__hostlist)


# Generated at 2022-06-13 15:00:01.793093
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = 0
    strategy = StrategyModule(tqm)
    assert strategy.debugger_active == True

# end-of-line

# Generated at 2022-06-13 15:00:06.549294
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    class TestStrategyModule(StrategyModule):
        def __init__(self, tqm):
            super(StrategyModule, self).__init__(tqm)
            self.debugger_active = True
    assert TestStrategyModule.__name__ == 'StrategyModule'



# Generated at 2022-06-13 15:00:07.949431
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    StrategyModule('ansible-playbook')



# Generated at 2022-06-13 15:01:19.752269
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # test set up
    tqm = 'not necessary'
    assert StrategyModule(tqm).debugger_active == True


# Generated at 2022-06-13 15:01:21.223255
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    sm = StrategyModule()
    assert sm.debugger_active == True


# Generated at 2022-06-13 15:01:24.110745
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    strategy_module = StrategyModule(tqm)
    assert strategy_module.debugger_active is True


# Generated at 2022-06-13 15:01:32.053296
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    test_task = {
        "hosts": "all",
        "tasks": [{
            "debug": "msg=my first debug"
        }]
    }

    # run ansible with debug option
    import ansible.playbook
    import ansible.utils
    import ansible.constants
    from ansible.callbacks import DefaultRunnerCallbacks

    ansible.constants.DEFAULT_DEBUG = True

    # it seems that ansible.utils.parse_kv() is not necessary since
    # ansible.constants.DEFAULT_DEBUG is True
    # However without this parse_kv(), ansible module in the next task
    # will not work as expected.
    ansible.utils.parse_kv(sys.argv)


# Generated at 2022-06-13 15:01:33.727358
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_module = StrategyModule(None)
    assert strategy_module.debugger_active is True


# Generated at 2022-06-13 15:01:35.817656
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    obj = StrategyModule
    assert(obj.__class__.__name__ == "type")


# Generated at 2022-06-13 15:01:38.540879
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = 'test_tqm'
    strategy_instance = StrategyModule(tqm)
    assert strategy_instance
    assert strategy_instance.debugger_active


# Generated at 2022-06-13 15:01:39.234329
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True


# Generated at 2022-06-13 15:01:39.765552
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass



# Generated at 2022-06-13 15:01:40.683585
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule(None)


# Generated at 2022-06-13 15:04:12.307420
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule.debugger_active == True


# Generated at 2022-06-13 15:04:22.077667
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.playbook import Playbook
    from ansible.plugins.loader import strategy_loader
    from ansible.plugins.strategy import debug
    from ansible.executor.task_queue_manager import TaskQueueManager

    pb = Playbook()
    pb.strategy = 'debug'

    tqm = TaskQueueManager(
            inventory=pb.inventory,
            variable_manager=pb.get_variable_manager(),
            loader=pb.loader,
            passwords=dict(),
            stdout_callback=pb.callback,
            run_additional_callbacks=False,
            run_tree=False,
            transport=pb.get_transport(),
    )

    strategy = strategy_loader.get('debug', tqm)

    assert isinstance(strategy, tqm.strategy)

# Generated at 2022-06-13 15:04:26.113992
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    class task_queue_manager():
        def __init__(self):
            self.stats = dict()
    tqm = task_queue_manager()
    sm = StrategyModule(tqm)
    assert sm.debugger_active == True
    assert isinstance(sm, LinearStrategyModule)



# Generated at 2022-06-13 15:04:29.174273
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = {'foo': 'bar'}
    strategy_module = StrategyModule(tqm)
    assert strategy_module.tqm == {'foo': 'bar'}
    assert strategy_module.debugger_active == True

# Generated at 2022-06-13 15:04:29.867478
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    module = StrategyModule(None)
    assert module.debugger_active


# Generated at 2022-06-13 15:04:38.405984
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.playbook.task import Task
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.role import Role
    from ansible.playbook.role_context import RoleContext
    from ansible.playbook.block import Block
    from ansible.playbook.task_include import TaskInclude
    from ansible.executor.task_queue_manager import TaskQueueManager
    play_context = PlayContext(play=Play().load({'hosts': 'all', 'gather_facts': 'no'}))
    play_context._set_roles([Role(name='test_role', play_context=play_context)])
    role_context = RoleContext(play_context=play_context)

# Generated at 2022-06-13 15:04:45.460321
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    class TestException(Exception):
        pass

    class DummyTQM():
        def __init__(self):
            self.stats = {}

    class DummyResults():
        def __init__(self):
            self.hosts = {}

        @staticmethod
        def _get_host_records():
            return {}

    class DummyPlay():
        def __init__(self):
            self._included_roles = []

    class DummyInventory():
        def __init__(self):
            self.hosts = {}

    class DummyRunner():
        def __init__(self):
            pass

    class DummyVariableMgr():
        def __init__(self):
            pass

    class DummyAllStats():
        def __init__(self):
            self.failures = {}
            self

# Generated at 2022-06-13 15:04:47.209552
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    test_obj = StrategyModule(None) 
    assert test_obj.debugger_active == True



# Generated at 2022-06-13 15:04:53.873230
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    class my_tqm:
        def __init__(self):
            self.result_q = {0: {'_ansible_ignore_errors': False,
                                 '_ansible_no_log': False}}
            self._final_q = []

        def __repr__(self):
            return "my_tqm"

    my_tqm1 = my_tqm()
    test_sm = StrategyModule(my_tqm1)
    assert test_sm.debugger_active


# A subclass of Cmd, the framework of interactive command interpreter

# Generated at 2022-06-13 15:04:58.855848
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    class TestObjStruct(object):
        '''
        Robot Framework requires a class but the class doesn't have to have any particular
        attributes.

        So here we make class instead of dict just to show off.
        '''
        def __init__(self, **kwargs):
            self.__dict__.update(kwargs)

    tqm = TestObjStruct(something='whatever')
    sm = StrategyModule(tqm)
    assert sm.runner_queue == []
    assert sm.debugger_active == True
