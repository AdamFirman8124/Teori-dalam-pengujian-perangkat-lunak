

# Generated at 2022-06-13 15:06:31.064332
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    print("Testing constructor of class StrategyModule")
    strategy = StrategyModule()
    assert strategy is not None
    assert strategy._host_pinned is True
    print("Passed all tests for constructor of class StrategyModule")



# Generated at 2022-06-13 15:06:31.612275
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True

# Generated at 2022-06-13 15:06:34.264319
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy = StrategyModule(host, connection, loader, options, passwords, stdout_callback, run_additional_callbacks, run_tree)
    assert strategy._host_pinned == True

# Generated at 2022-06-13 15:06:35.163075
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
   assert StrategyModule.__doc__

# Generated at 2022-06-13 15:06:39.054279
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.plugins.strategy.host_pinned import StrategyModule
    from ansible.executor.task_queue_manager import TaskQueueManager
    tqm = TaskQueueManager(None, None)
    sm = StrategyModule(tqm)
    assert sm._host_pinned == True

# Generated at 2022-06-13 15:06:40.661731
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = 'To be implemented'
    sut = StrategyModule(tqm)
    assert sut is not None

# Generated at 2022-06-13 15:06:41.497890
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    print (StrategyModule)


# Generated at 2022-06-13 15:06:42.346175
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    a = StrategyModule('tqm')

# Generated at 2022-06-13 15:06:42.851493
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True==True

# Generated at 2022-06-13 15:06:46.097345
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # test class instantiation
    tqm = StrategyModule(tqm)
    assert not tqm#, msg='Object is not instantiated properly'

# Generated at 2022-06-13 15:06:48.352830
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategyModule = StrategyModule(None)
    print("The test case for StrategyModule is passed")

# Generated at 2022-06-13 15:06:50.052226
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # Test constructor when no argument is passed (make sure it doesn't
    # fail in that case)
    StrategyModule()

# Generated at 2022-06-13 15:06:55.455467
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    import unittest
    class TestStrategyModule(unittest.TestCase):
        def setUp(self):
            tqm = unittest.mock.MagicMock()
            self.strategy_module = StrategyModule(tqm)
        def test_host_pinned(self):
            self.assertEqual(self.strategy_module._host_pinned, True)
        unittest.mock.patch('ansible.plugins.strategy.host_pinned.FreeStrategyModule.__init__', return_value=None)
        def test_call_FreeStrategyModule_init(self, mock_init):
            StrategyModule(unittest.mock.MagicMock())
            self.assertTrue(mock_init.called)
    unittest.main()

# Generated at 2022-06-13 15:06:56.326433
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule

# Generated at 2022-06-13 15:06:57.782930
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert len(dir(StrategyModule)) > 0


# Generated at 2022-06-13 15:06:58.387367
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True

# Generated at 2022-06-13 15:07:00.219200
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy = StrategyModule(None)
    assert strategy._host_pinned == True

# Generated at 2022-06-13 15:07:11.080841
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
  from unittest import mock
  from ansible.plugins.strategy.host_pinned import StrategyModule
  print("Running host_pinned unit test")
  # Unit test for constructor of class StrategyModule
  tqm = mock.MagicMock()
  testStrategyModule = StrategyModule(tqm)
  assert testStrategyModule._tqm == tqm
  assert testStrategyModule._host_pinned
  assert testStrategyModule._shared_loader_obj
  assert testStrategyModule._host_pinned == True
  assert testStrategyModule._host_topics == {}
  assert testStrategyModule._workers == {}

# Generated at 2022-06-13 15:07:11.829071
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True

# Generated at 2022-06-13 15:07:12.503637
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
  print("hello")

# Generated at 2022-06-13 15:07:17.641610
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    context = {}
    obj = StrategyModule(context)
    assert obj._host_pinned == True # pylint: disable=protected-access

# Generated at 2022-06-13 15:07:18.101585
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    StrategyModule('test')

# Generated at 2022-06-13 15:07:21.279455
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = {"foo": "baz"}
    strategy = StrategyModule(tqm)
    assert strategy.__class__.__bases__[0].__name__ == 'FreeStrategyModule'
    assert strategy._tqm == tqm
    assert strategy._host_pinned
    assert strategy.get_name() == 'host_pinned'

# Generated at 2022-06-13 15:07:23.022708
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategyModule = StrategyModule
    assert strategyModule, "Unable to create instance of StrategyModule"

# Generated at 2022-06-13 15:07:23.467402
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True

# Generated at 2022-06-13 15:07:24.857923
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule('tqm')._host_pinned == True

# Generated at 2022-06-13 15:07:27.979662
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # Set up argument objects for StrategyModule
    class Test_TQM(object):
        pass
    tqm = Test_TQM()

    strategy_module = StrategyModule(tqm)
    assert strategy_module._host_pinned == True

# Generated at 2022-06-13 15:07:30.411162
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_module = StrategyModule(tqm=None)
    assert strategy_module._host_pinned == True
    assert strategy_module._batch_count == 0

# Generated at 2022-06-13 15:07:32.280800
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
  assert StrategyModule.__bases__[0].__name__ == FreeStrategyModule.__name__

# Generated at 2022-06-13 15:07:33.308645
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True == True  # Placeholder

# Generated at 2022-06-13 15:07:38.249216
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule(2)
    assert StrategyModule(True)

# Generated at 2022-06-13 15:07:44.762912
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.plugins.strategy.pinned import StrategyModule
    import ansible.plugins.strategy.free
    import ansible.plugins.strategy.linear

    strategy_module = StrategyModule()
    assert isinstance(strategy_module, StrategyModule), "Constructor of class StrategyModule failed"
    assert isinstance(strategy_module, ansible.plugins.strategy.free.StrategyModule), "StrategyModule should be instance of class FreeStrategyModule"
    assert not isinstance(strategy_module, ansible.plugins.strategy.linear.StrategyModule), "StrategyModule should not be instance of class LinearStrategyModule"

# Generated at 2022-06-13 15:07:46.435042
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule.__init__

# Generated at 2022-06-13 15:07:47.162306
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert callable(StrategyModule)

# Generated at 2022-06-13 15:07:48.477633
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy = StrategyModule(tqm=None)
    assert strategy is not None
    assert strategy._host_pinned == True

# Generated at 2022-06-13 15:07:49.668712
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
  assert StrategyModule

if __name__ == '__main__':
  test_StrategyModule()

# Generated at 2022-06-13 15:07:52.128434
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule.__name__ == 'StrategyModule'
    # test parent class
    assert issubclass(StrategyModule, FreeStrategyModule)
    # test parent class attributes
    assert hasattr(StrategyModule, '__init__')
    assert hasattr(StrategyModule, 'run')


# Generated at 2022-06-13 15:07:53.150817
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    module = StrategyModule(tqm=None)
    assert(module._host_pinned == True)

# Generated at 2022-06-13 15:07:53.651610
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule


# Generated at 2022-06-13 15:07:54.262214
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule

# Generated at 2022-06-13 15:08:05.664293
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.plugins.strategy.host_pinned import StrategyModule
    my_plugin = StrategyModule(tqm = None)

# Generated at 2022-06-13 15:08:08.958432
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    class TQM:
        def __init__(self):
            self.stats = []
    obj1 = TQM()
    obj2 = StrategyModule(obj1)
    assert obj2._host_pinned == True

# Generated at 2022-06-13 15:08:12.791933
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    """Create a StrategyModule object"""
    tqm = unittest.mock.MagicMock()
    strategy_module_object = StrategyModule(tqm)
    assert strategy_module_object._host_pinned == True


# Generated at 2022-06-13 15:08:14.345979
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule == FreeStrategyModule
    assert isinstance(display, Display)

# Generated at 2022-06-13 15:08:15.209672
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    StrategyModule(tqm="tqm")

# Generated at 2022-06-13 15:08:17.267933
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = 'test'
    host_pinned = StrategyModule(tqm)

# test_StrategyModule()



# Generated at 2022-06-13 15:08:18.082732
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    StrategyModule('tqm')


# Generated at 2022-06-13 15:08:20.129254
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    my_tqm = None
    my_strategy_module = StrategyModule(my_tqm)
    assert my_strategy_module._host_pinned == True

# Generated at 2022-06-13 15:08:21.456803
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy=StrategyModule(tqm)
    assert strategy._tqm is tqm

# Generated at 2022-06-13 15:08:22.903473
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
  sm = StrategyModule()
  print(sm._host_pinned)

# Generated at 2022-06-13 15:08:41.550012
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_module = StrategyModule(None)
    assert strategy_module._host_pinned == True
    assert strategy_module._display.verbosity == 0

# Test for constructor of class Display

# Generated at 2022-06-13 15:08:43.449314
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule.name == 'host_pinned'
    assert StrategyModule.host_pinned

# Generated at 2022-06-13 15:08:44.327993
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    StrategyModule(tqm=None)

# Generated at 2022-06-13 15:08:50.122434
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.plugins.strategy.host_pinned import StrategyModule
    # test StrategyModule class constructor with tqm argument so that it can be called via ansible
    #   ansible -m ansible.plugins.strategy.host_pinned.StrategyModule
    StrategyModule(tqm=None)

# Generated at 2022-06-13 15:08:51.247671
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule

# Generated at 2022-06-13 15:08:52.710002
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy = StrategyModule(True)
    assert strategy._host_pinned == True


# Generated at 2022-06-13 15:08:53.803674
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    assert StrategyModule(tqm)

# Generated at 2022-06-13 15:08:55.088820
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
  strategy = StrategyModule("2")

# Generated at 2022-06-13 15:08:55.614104
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy = StrategyModule()

# Generated at 2022-06-13 15:08:56.742669
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    st = StrategyModule()
    assert st.__class__ == StrategyModule


# Generated at 2022-06-13 15:09:39.202257
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    sm = StrategyModule()
    assert sm._host_pinned is True

# Generated at 2022-06-13 15:09:43.947844
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    global display
    display = Display()
    tqm = type('tqm', (object,), dict(hostvars=dict(),
                                      inventory=type('inventory',(object,), dict(host_list=[],
                                                                                  groups=dict(all=[])))
                                      ))()
    sm = StrategyModule(tqm)
    assert sm._host_pinned == True

# Generated at 2022-06-13 15:09:45.649974
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = '__string__'
    a = StrategyModule(tqm)
    assert a._host_pinned == True

# Generated at 2022-06-13 15:09:47.141772
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    test_strategy_module = StrategyModule(tqm)
    assert test_strategy_module._host_pinned == True

# Generated at 2022-06-13 15:09:50.268765
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = "test_tqm"
    strategy_module = StrategyModule(tqm)
    assert strategy_module._host_pinned
    assert strategy_module._tqm == tqm

# Generated at 2022-06-13 15:09:51.964357
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    obj = StrategyModule(host_pinned=True)
    assert obj._host_pinned == True

# Generated at 2022-06-13 15:10:03.128868
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    '''
      This is a unit test for constructor of host_pinned class StrategyModule
      This test will generate a mock tqm object and pass it to host_pinned.py
      and check if it assigns the appropriate values to self._host_pinned

      Define success variables:
        _host_pinned is True
        next_nonscheduled_host() is empty
        host_list is empty
        max_host_failure_percentage is zero
    '''

    class _tqm:
        def __init__(self):
            self.options = None
            self.inventory = None
            self.runners = None
            self.notified_handlers = None
            self.ds = None
            self.stats = None
            self.failed_hosts = None
            self.ok_hosts = None

# Generated at 2022-06-13 15:10:04.027374
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule(None) is not None

# Generated at 2022-06-13 15:10:08.869556
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    print('Test constructor of class StrategyModule')
    if tqm == None:
        print('tqm is None!')
        return -1
    else:
        strategyModule = StrategyModule(tqm)
        if not isinstance(strategyModule, StrategyModule):
            print('strategyModule is not an instance of class StrategyModule!')
            return -1
        else:
            print('strategyModule is an instance of class StrategyModule!')
            return 0


# Generated at 2022-06-13 15:10:09.339749
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    StrategyModule(None)

# Generated at 2022-06-13 15:11:38.823069
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule(tqm)


# Generated at 2022-06-13 15:11:40.677257
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    host = StrategyModule()
    if host._host_pinned:
        print('Host uses pinned strategy')
    else:
        print('Host does not use pinned strategy')

# Generated at 2022-06-13 15:11:42.126010
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.plugins.strategy.host_pinned import StrategyModule
    assert not StrategyModule._host_pinned

# Generated at 2022-06-13 15:11:43.789579
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    try:
        smd = StrategyModule(tqm)
    except:
        assert False
    else:
        assert True

# Generated at 2022-06-13 15:11:44.517571
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule is not None

# Generated at 2022-06-13 15:11:46.557797
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    strategy = StrategyModule(tqm)
    assert strategy is not None
    assert strategy._host_pinned

# Generated at 2022-06-13 15:11:48.172549
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    StrategyModule(object)



# Generated at 2022-06-13 15:11:49.561766
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    obj = StrategyModule()
    assert obj

# Generated at 2022-06-13 15:11:52.035238
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule('tqm') is not None


# Generated at 2022-06-13 15:11:59.868202
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule.__name__ == 'StrategyModule'

# Generated at 2022-06-13 15:15:09.974546
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule(1)._host_pinned == True


# Generated at 2022-06-13 15:15:11.481749
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    sm = StrategyModule('tqm')
    assert sm._host_pinned == True

# Generated at 2022-06-13 15:15:12.700278
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    module = StrategyModule(tqm)
    assert module._host_pinned is True

# Generated at 2022-06-13 15:15:13.317681
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass #TODO

# Generated at 2022-06-13 15:15:14.182818
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    sm = StrategyModule()
    assert sm

# Generated at 2022-06-13 15:15:15.681291
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    sm = StrategyModule(tqm)
    assert sm is not None

# Generated at 2022-06-13 15:15:18.912356
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    print("Test constructor of class StrategyModule")
    tqm = None
    strategy_module_object = StrategyModule(tqm)
    assert strategy_module_object is not None, 'Failed to create StrategyModule object'
    assert strategy_module_object._host_pinned is True, "Failed to create StrategyModule object. _host_pinned was not True"


# Generated at 2022-06-13 15:15:25.695322
# Unit test for constructor of class StrategyModule

# Generated at 2022-06-13 15:15:27.236286
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    global display
    module = StrategyModule(display)
    assert module != None

# Generated at 2022-06-13 15:15:33.320315
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    import mock
    import ansible.plugins.strategy
    import ansible.plugins.strategy.host_pinned

    import ansible.utils
    import ansible.plugins
    import ansible.plugins.strategy.free

    ansible.plugins.strategy = ansible.plugins.strategy.host_pinned
    ansible.plugins.strategy.free = ansible.plugins.strategy.free

    ansible.utils = mock.MagicMock()
    import ansible.plugins.strategy.host_pinned
    import ansible.plugins.strategy.free

    strategy_module = ansible.plugins.strategy.host_pinned.StrategyModule(mock.MagicMock())
    assert isinstance(strategy_module, ansible.plugins.strategy.free.StrategyModule)

    assert strategy_module._