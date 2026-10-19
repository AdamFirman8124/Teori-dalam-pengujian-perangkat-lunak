

# Generated at 2022-06-13 15:06:29.771631
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = ansible_test.get_tqm()
    strategy = StrategyModule(tqm)
    assert(strategy._host_pinned is True)

# Generated at 2022-06-13 15:06:31.063668
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    module = StrategyModule("This is a test")
    assert module._host_pinned == True

# Generated at 2022-06-13 15:06:32.234883
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.plugins.strategy.host_pinned import StrategyModule


# Generated at 2022-06-13 15:06:32.775434
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass

# Generated at 2022-06-13 15:06:35.359861
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.executor.task_queue_manager import TaskQueueManager
    tqm = TaskQueueManager(None, None)
    StrategyModule(tqm)

# Generated at 2022-06-13 15:06:36.741752
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = {}
    StrategyModule(tqm)

# Generated at 2022-06-13 15:06:40.823297
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # Here we are taking the object of class StrategyModule for unit testing
    strategy = StrategyModule(tqm=None)
    # This will return the object of a Display class
    display_obj = Display()
    # Asserting the test case if the object of Display class is returned or not
    assert isinstance(strategy._display, Display) == True

# Generated at 2022-06-13 15:06:47.620720
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy = StrategyModule(None)
    assert strategy is not None
    assert strategy._host_pinned == True
    assert strategy.tqm is None
    assert strategy._blocked is False
    assert strategy._display is not None
    assert strategy._done is False
    assert strategy._failed_hosts == dict()
    assert strategy._initial_queue is None
    assert strategy._inventory is None
    assert strategy._last_banner is None
    assert strategy._last_task_banner is None
    assert strategy._play is None
    assert strategy._play_context is None
    assert strategy._play_name is None
    assert strategy._play_view is None
    assert strategy._queue is None
    assert strategy._send_callback is None
    assert strategy._stats is not None
    assert strategy._var_cache is None
    assert strategy._vars_

# Generated at 2022-06-13 15:06:49.249665
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    s = StrategyModule(None)
    assert s._host_pinned is True, "_host_pinned is not True"

# Generated at 2022-06-13 15:06:51.073437
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    test_object = StrategyModule(tqm)
    assert test_object is not None
    assert test_object._host_pinned == True


# Generated at 2022-06-13 15:07:00.218357
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    h1 = Host('h1')
    h2 = Host('h2')
    p1 = Play(playbook=None, playbook_basedir='static/yaml', host_list=[h1, h2])
    t1 = Task(host=h1, play=p1)
    t2 = Task(host=h2, play=p1)
    tqm = TaskQueueManager(hosts=[h1, h2], tasks=[t1], tasks_done=[t2], queue=None, stats=None, stdout_callback=None, run_once=None)
    strategy_module = StrategyModule(tqm)
    assert(strategy_module._host_pinned == True)

# Generated at 2022-06-13 15:07:00.796651
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass

# Generated at 2022-06-13 15:07:03.580287
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
        strategy = StrategyModule(tqm="tqm1")
        assert strategy._host_pinned == True

# Generated at 2022-06-13 15:07:06.352495
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    '''
    Return a test suite for the host_pinned module
    '''
    import unittest
    test_loader = unittest.TestLoader()
    test_loader.testMethodPrefix = 'test'
    suite = unittest.TestSuite()

    suite.addTest(test_loader.loadTestsFromTestCase(StrategyModule))
    return suite



# Generated at 2022-06-13 15:07:06.975210
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule

# Generated at 2022-06-13 15:07:07.598491
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True

# Generated at 2022-06-13 15:07:09.344308
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = ''
    x = StrategyModule(tqm)
    assert x._host_pinned is True

# Generated at 2022-06-13 15:07:18.741933
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.playbook_executor import PlaybookExecutor
    class TestOptions(object):
        def __init__(self):
            self.module_path = None
            self.connection = None
            self.forks = 5
            self.become = None
            self.become_method = None
            self.become_user = None
            self.check = False
            self.listhosts = None
            self.listtasks = None

# Generated at 2022-06-13 15:07:19.948875
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    module = StrategyModule(tqm=None)
    assert module is not None

# Generated at 2022-06-13 15:07:21.943696
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = object()
    strategy = StrategyModule(tqm)

    assert strategy._host_pinned == True

# Generated at 2022-06-13 15:07:25.533417
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_module = StrategyModule('tqm')
    assert isinstance(strategy_module._host_pinned, bool)

# Generated at 2022-06-13 15:07:26.138954
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass

# Generated at 2022-06-13 15:07:28.141499
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule.__name__ == 'StrategyModule'
    assert issubclass(StrategyModule, FreeStrategyModule)

# Generated at 2022-06-13 15:07:29.830104
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
      tqm = TestQueueManagerInterface()
      assert StrategyModule(tqm)._host_pinned


# Generated at 2022-06-13 15:07:31.371762
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    display = Display()
    StrategyModule(display)

# end of StrategyModule

# Generated at 2022-06-13 15:07:38.330670
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    class TQM(object):
        def __init__(self):
            self.options = {'forks': 10}
            self.inventory = 'inventory'
            self.variable_manager = 'variable_manager'
            self.loader = 'loader'
            self.passwords = 'passwords'
            self.stdout_callback = 'stdout_callback'
            self.stats = 'stats'

    tqm_obj = TQM()

    strategy_obj = StrategyModule(tqm_obj)
    assert strategy_obj._host_pinned == True

# Generated at 2022-06-13 15:07:42.083953
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    print(StrategyModule)

# test case 1
test = StrategyModule(tqm="tqm")
if hasattr(test, '_host_pinned'):
    print("Success, class 'StrategyModule' has attribute '_host_pinned'")
else:
    print("Failed, class 'StrategyModule' does not have attribute '_host_pinned'")


# Generated at 2022-06-13 15:07:44.070737
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None # TODO: how to do the test?
    strategy = StrategyModule(tqm)
    assert strategy == None # just for test now
    return

# Generated at 2022-06-13 15:07:45.370581
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy = StrategyModule(tqm=None)
    assert strategy._host_pinned == True

# Generated at 2022-06-13 15:07:48.951966
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert issubclass(StrategyModule, FreeStrategyModule)
    assert StrategyModule.use_linear_chunks
    assert StrategyModule.should_partition_workers
    assert StrategyModule.should_disable_partial_callback
    assert StrategyModule.should_disable_action_warnings
    assert StrategyModule.worker_pool_size == 0
    assert StrategyModule.queue_has_task_limits


# Generated at 2022-06-13 15:07:54.735085
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    sm = StrategyModule({})
    assert sm._host_pinned == True

# Generated at 2022-06-13 15:08:04.474579
# Unit test for constructor of class StrategyModule

# Generated at 2022-06-13 15:08:05.907928
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    StrategyModule(tqm='tqm')

# Generated at 2022-06-13 15:08:10.415543
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    import ansible.plugins.strategy.host_pinned
    tqm = "Temp"
    strategy_module = StrategyModule(tqm)
    assert strategy_module._host_pinned == True
    assert strategy_module._tqm.__dict__ == tqm.__dict__

# Generated at 2022-06-13 15:08:20.049280
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.plugins.loader import strategy_loader
    from ansible.plugins.strategy.host_pinned import StrategyModule as test_StrategyModule
    import unittest

    class AnsibleExitJson(Exception):
        pass

    class AnsibleFailJson(Exception):
        pass

    class ExitJsonException(unittest.TestCase):
        def runTest(self):
            result = {'changed': False, 'failures': [], 'skipped': [], 'ok': ['localhost']}
            tqm = test_StrategyModule(result)
            self.assertEqual(tqm._tqm_stdout_callback._display._verbosity, 3)

    test_cases = [ExitJsonException()]
    for test in test_cases:
        suite = unittest.TestSuite()


# Generated at 2022-06-13 15:08:23.269367
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_module = StrategyModule(10)
    host_pinned_var = strategy_module._host_pinned
    assert host_pinned_var == True

"""
This method checks the time elapsed between the current time and the time when the first task of the host started.
If the time elapsed is more than 'seconds' then yield returns the current host, otherwise None.
"""

# Generated at 2022-06-13 15:08:24.538294
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    StrategyModule()
    pass


# Generated at 2022-06-13 15:08:26.099184
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    a = StrategyModule()
    print(a)

# Generated at 2022-06-13 15:08:29.888234
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_object = StrategyModule('tqm')
    strategy_data = strategy_object.__dict__
    assert strategy_data['_host_pinned'] == True

# Generated at 2022-06-13 15:08:30.508770
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
	return True

# Generated at 2022-06-13 15:08:42.109912
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    sm = StrategyModule(tqm)
    assert sm is not None
    print("StrategyModule passed")

# Here are some unit tests that can be run in python3.6
# python3.6 -m pytest Tests/test_host_pinned.py

# Generated at 2022-06-13 15:08:47.342221
# Unit test for constructor of class StrategyModule
def test_StrategyModule():

    # mock class for tqm object
    class _test_tqm():
        def __init__(self):
            self.stats = {}

    _tqm = _test_tqm()
    result = StrategyModule(_tqm)

    assert (result._host_pinned == True)

# Generated at 2022-06-13 15:08:53.771674
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    module = StrategyModule(1)
    assert module

# Lesson 3:
#   - write some code here that uses the constructor
#   - either use unit test or main section
#   - if you need some hints check out the test or the other lessons
#   - if you need more info check out the python documentation
#   - share your solution on github and add the link here

# share your solution on github and add the link here:
# https://github.com/tik42/ansible-reverse-engineering

# Generated at 2022-06-13 15:08:54.677182
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True

# Generated at 2022-06-13 15:08:55.828092
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = AnsiblePlaybook()
    StrategyModule(tqm)

# Generated at 2022-06-13 15:08:57.767532
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy = StrategyModule(tqm=None)
    assert strategy._host_pinned


if __name__ == '__main__':
    test_StrategyModule()

# Generated at 2022-06-13 15:08:59.579538
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    import ansible.plugins.strategy.host_pinned
    strategyModule = ansible.plugins.strategy.host_pinned.StrategyModule()
    assert strategyModule != None

# Generated at 2022-06-13 15:09:00.971985
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    s = StrategyModule(None)
    assert s._host_pinned == True

# Generated at 2022-06-13 15:09:02.698209
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule.__name__ == 'StrategyModule'
    assert StrategyModule._host_pinned == True

# Generated at 2022-06-13 15:09:04.838917
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    sm = StrategyModule("tqm")
    assert sm._host_pinned

if __name__ == '__main__':
    test_StrategyModule()

# Generated at 2022-06-13 15:09:28.714972
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_module = StrategyModule
    assert strategy_module.__module__ == 'ansible.plugins.strategy.host_pinned'
    assert strategy_module.__name__ == 'StrategyModule'

# Generated at 2022-06-13 15:09:29.778915
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule.__doc__ is not None



# Generated at 2022-06-13 15:09:31.133002
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    smtest = StrategyModule(tqm=None)
    assert smtest._host_pinned == True

# Generated at 2022-06-13 15:09:31.597983
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    StrategyModule(None)

# Generated at 2022-06-13 15:09:32.378779
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    StrategyModule(tqm)

# Generated at 2022-06-13 15:09:38.329897
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    import piston
    import ansible.plugins.loader as plugin_loader
    import ansible.plugins.strategy.host_pinned as strategy_host_pinned
    import ansible.utils.display as display
    plugin = plugin_loader.get_plugin_loader().get('strategy')
    display = display.Display()
    strat = plugin.load_strategy_module('host_pinned')
    print("\n!!Unit test for constructor of class StrategyModule")
    print("\n!!StrategyModule class object = ", strat)
    print("\n!!StrategyModule class object = ", strat.__class__)
    print("\n!!StrategyModule class object = ", strat.__class__.__name__)
    print("\n!!StrategyModule str variable = ", strat.__str__())

# Generated at 2022-06-13 15:09:40.656620
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_module = StrategyModule(None)
    global display
    assert strategy_module.__str__() is not None

# Generated at 2022-06-13 15:09:41.404678
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert (StrategyModule(tqm) != None)

# Generated at 2022-06-13 15:09:46.445386
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    hostname = []
    hostname.append("host")
    hosts = dict()
    hosts['host'] = dict()
    hosts['host']['hostname'] = 'host'
    tqm = dict()
    tqm['hosts'] = hosts
    tqm['hostname'] = hostname
    st = StrategyModule(tqm)
    assert st.__class__.__name__ == 'StrategyModule'

# Generated at 2022-06-13 15:09:47.852992
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_module = StrategyModule('tqm')
    assert(strategy_module)

# Generated at 2022-06-13 15:10:24.505209
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    obj = StrategyModule(tqm)
    assert obj._host_pinned == True

# Generated at 2022-06-13 15:10:26.463440
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
        assert StrategyModule.__init__ is not FreeStrategyModule.__init__

# Generated at 2022-06-13 15:10:28.509748
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_module = StrategyModule("tqm")
    assert(strategy_module._host_pinned == True)


# Generated at 2022-06-13 15:10:30.934170
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # Testing constructor of class StrategyModule
    # Assume ExampleStrategy is the name of the strategy class
    tqm = ''
    strategy_instance = StrategyModule(tqm)
    return strategy_instance


# Generated at 2022-06-13 15:10:32.034821
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy = StrategyModule('testqm')
    assert strategy._host_pinned == True

# Generated at 2022-06-13 15:10:37.869595
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from units.mock.loader import DictDataLoader
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.parsing.dataloader import DataLoader

    data_loader = DictDataLoader({})
    variable_manager = VariableManager()
    inventory = Inventory(loader=data_loader, variable_manager=variable_manager)
    tqm = TaskQueueManager(inventory=inventory, variable_manager=variable_manager, loader=data_loader)

    ret = StrategyModule(tqm)
    assert ret._host_pinned
    assert ret._tqm == tqm
    assert ret._display == display

# Generated at 2022-06-13 15:10:40.961986
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.plugins.strategy import StrategyModule
    sm = StrategyModule(None)
    # Test that the constructor for StrategyModule works
    assert sm is not None

# Generated at 2022-06-13 15:10:44.052367
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.plugins.strategy.host_pinned import StrategyModule

    strategy = StrategyModule(None)
    assert strategy != None
    assert strategy._host_pinned

# Test the module by testing it's super-class

# Generated at 2022-06-13 15:10:48.177571
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    class TQM:
        def __init__(self):
            self._host_pinned = True

    tqm = TQM()
    sm = StrategyModule(tqm)
    assert(sm._host_pinned)


# Generated at 2022-06-13 15:10:53.778009
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    module = StrategyModule(tqm = None)
    assert module._host_pinned == True
    assert module._cleanup_queue_size == 1
    assert module._task_result_q == None
    assert module._play_hosts == None
    assert module._play_context == None
    assert module._iterator == None
    assert module._optimize_deferring == None
    assert module._max_loop == 5000000


# Generated at 2022-06-13 15:12:37.422001
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from mock import MagicMock
    tqm = MagicMock()
    sm = StrategyModule(tqm)
    assert sm._display.__class__.__name__ == 'Display'
    assert sm._tqm == tqm
    assert sm._host_pinned == True

# Generated at 2022-06-13 15:12:39.251760
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule._host_pinned == True
#Unit test for constructor of super class

# Generated at 2022-06-13 15:12:45.089496
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from mock import create_autospec
    from ansible.plugins.strategy.host_pinned import StrategyModule

    tqm = create_autospec(ansible.executor.task_queue_manager.TaskQueueManager)
    s = StrategyModule(tqm)

    assert isinstance(s, ansible.plugins.strategy.free.StrategyModule)
    assert isinstance(s, StrategyModule)

    assert s._host_pinned == True

# Generated at 2022-06-13 15:12:48.637935
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    """
    This function is used to test the constructor of class StrategyModule
    :return: None
    """
    out = StrategyModule('')
    assert out.__class__.__name__ == "StrategyModule", "Failed to create a object of class StrategyModule"

# Generated at 2022-06-13 15:12:50.445605
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    strategy_module = StrategyModule(tqm)
    assert strategy_module._host_pinned == True

# Generated at 2022-06-13 15:12:51.772255
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    m = StrategyModule(tqm=None)
    assert(m._host_pinned)

# Generated at 2022-06-13 15:12:54.530658
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    strategy = StrategyModule(tqm)
    assert strategy_host_pinned is True
    strategy = StrategyModule()
    assert strategy_host_pinned is True

# Generated at 2022-06-13 15:12:56.008309
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    sm = StrategyModule(tqm)

# Generated at 2022-06-13 15:12:58.074889
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    import ansible.plugins.strategy.host_pinned
    strategy_module = ansible.plugins.strategy.host_pinned.StrategyModule(None)
    assert strategy_module

# Generated at 2022-06-13 15:12:59.605874
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    assert StrategyModule(tqm)._host_pinned == True

# Generated at 2022-06-13 15:16:13.769607
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass

# Generated at 2022-06-13 15:16:22.915913
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.handler import Handler
    from ansible.playbook.block import Block
    from ansible.playbook.task_include import TaskInclude
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.inventory.host import Host
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    variable_manager = VariableManager()
    host1 = Host(name="host1")
    host2 = Host(name="host2")
    host1.vars = dict()
    host2.vars = dict()
    play_context = dict()

# Generated at 2022-06-13 15:16:25.079302
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    strategy_module = StrategyModule(tqm)
    # The _host_pinned value should be True
    assert strategy_module._host_pinned == True

# Generated at 2022-06-13 15:16:28.868008
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.executor.task_queue_manager import TaskQueueManager

    manager = TaskQueueManager()
    tqm = StrategyModule(manager)
    print(tqm.__class__.__name__)

if __name__ == '__main__':
    test_StrategyModule()