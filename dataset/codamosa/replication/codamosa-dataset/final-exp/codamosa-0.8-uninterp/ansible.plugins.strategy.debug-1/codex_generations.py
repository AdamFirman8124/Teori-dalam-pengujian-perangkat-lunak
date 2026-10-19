

# Generated at 2022-06-13 14:55:29.543590
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    strategy = StrategyModule(tqm)
    assert strategy.debugger_active == True


# Generated at 2022-06-13 14:55:31.045083
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    Debugger(command=None, stdin=None, stdout=None).cmdloop()


# Generated at 2022-06-13 14:55:34.140979
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule.__doc__ == 'Documentation string for "debug" strategy.'
    assert LinearStrategyModule.__doc__ == 'Documentation string for "linear" strategy.'

    test_obj = StrategyModule('test_tqm')
    assert test_obj.debugger_active == True

# Generated at 2022-06-13 14:55:40.820783
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    import unittest
    class TestStrategyModule(unittest.TestCase):
        def test_StrategyModule(self):
            tqm = unittest.mock.Mock()
            strategy_module = StrategyModule(tqm)
            self.assertTrue(strategy_module)
            self.assertEqual(strategy_module.run, strategy_module.run_debug)
            self.assertTrue(strategy_module.debugger_active)
    unittest.main()


# Generated at 2022-06-13 14:55:42.437891
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = MockTQM()
    assert StrategyModule(tqm)


# Generated at 2022-06-13 14:55:43.400906
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule.__doc__



# Generated at 2022-06-13 14:55:45.340622
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = True
    StrategyModule(tqm)


# Generated at 2022-06-13 14:55:49.869132
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = object()
    strategy = StrategyModule(tqm)
    assert strategy.tqm == tqm
    assert strategy.step is None
    assert strategy.iterator is None
    assert strategy.display is None

    assert strategy.debugger_active is True

# Testing for cmd.Cmd class

# Generated at 2022-06-13 14:55:54.065778
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.executor.task_queue_manager import TaskQueueManager
    tqm = TaskQueueManager(None)
    s = StrategyModule(tqm)
    assert isinstance(s, StrategyModule)

if __name__ == "__main__":
    import nose
    nose.main()

# Generated at 2022-06-13 14:55:56.276391
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = object()
    strategy = StrategyModule(tqm)
    assert strategy.tqm == tqm
    assert strategy.debugger_active == True


# Generated at 2022-06-13 14:56:06.503881
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible import constants as C
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.inventory import Inventory


# Generated at 2022-06-13 14:56:10.536001
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    class Test:
        verbose = True

    fake_tqm = Test()
    sm = StrategyModule(fake_tqm)
    assert sm.get_host_list() is None
    assert sm.tqm == fake_tqm


# Generated at 2022-06-13 14:56:16.046813
# Unit test for constructor of class StrategyModule
def test_StrategyModule():

    # Create tqm object
    class TQM():
        pass
    tqm = TQM()

    # Create strategy object
    strategy_object = StrategyModule(tqm)

    # Verify
    expected_debugger_active = True
    actual_debugger_active = strategy_object.debugger_active
    assert expected_debugger_active == actual_debugger_active

    # Terminate
    sys.exit(0)


# Main class for controlling the strategy

# Generated at 2022-06-13 14:56:16.960040
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule("test")


# Generated at 2022-06-13 14:56:18.625255
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = object()
    obj = StrategyModule(tqm)
    assert obj.debugger_active == True


# Generated at 2022-06-13 14:56:22.857978
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = DummyTaskQueueManager()
    strategy = StrategyModule(tqm)
    assert type(strategy) is StrategyModule
    assert strategy.tqm == tqm
    assert strategy.debugger_active == True
    assert strategy.num_per_host == tqm.options.forks

###############################################################################
# TODO: move this class to a common test framework place.

# Generated at 2022-06-13 14:56:25.514556
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    print(StrategyModule.__doc__)
    assert (StrategyModule.__doc__) is not None


# Generated at 2022-06-13 14:56:27.409760
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule.__doc__ is not None



# Generated at 2022-06-13 14:56:31.907492
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    task  = None
    inventory = None
    variable_manager = None
    loader = None
    options = None
    passwords = None
    stdout_callback = None
    run_tree = None

    sm = StrategyModule(task)
    assert sm.debugger_active == True

test_StrategyModule()

# Generated at 2022-06-13 14:56:34.205172
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy = StrategyModule(None)
    assert isinstance(strategy, StrategyModule)
    assert isinstance(strategy, LinearStrategyModule)



# Generated at 2022-06-13 14:56:40.668676
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    task_queue_manager = mock.MagicMock()
    strategy_module = StrategyModule(task_queue_manager)
    assert strategy_module.debugger_active == True


# Generated at 2022-06-13 14:56:50.042781
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    global_vars = {
        "playbook_basedir": "/path/to/playbook"
    }

# Generated at 2022-06-13 14:56:52.339073
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule(None).debugger_active == True


# Generated at 2022-06-13 14:56:54.421534
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    mod = StrategyModule('test_tqm')
    assert mod.debugger_active == True



# Generated at 2022-06-13 14:56:55.411566
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # TODO: Implement unit tests
    return



# Generated at 2022-06-13 14:56:56.289243
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # test_class_StrategyModule()
    return (1)


# Generated at 2022-06-13 14:56:59.839331
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    import ansible.plugins.strategy.debug as debug_module
    tqm = None
    strategy_module = debug_module.StrategyModule(tqm)
    assert strategy_module.tqm == None
    assert strategy_module.debugger_active


# Generated at 2022-06-13 14:57:01.617953
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule is not None

    tqm = None
    strategy = StrategyModule(tqm)
    assert strategy.debugger_active



# Generated at 2022-06-13 14:57:05.625305
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.plugins.strategy import StrategyModule
    from ansible.plugins.strategy.linear import StrategyModule as LinearStrategyModule
    import ansible.plugins.strategy.debug as debug

    inst = debug.StrategyModule(None)
    assert isinstance(inst, LinearStrategyModule)
    assert isinstance(inst, StrategyModule)
    assert inst.debugger_active is True



# Generated at 2022-06-13 14:57:16.693039
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.utils import module_docs
    from ansible.utils.sentinel import Sentinel
    from ansible.utils.display import Display
    from ansible.plugins.loader import strategy_loader
    from ansible.parsing.dataloader import DataLoader

    display = Display()
    display.verbosity = 0

    # Unit test for display._display() method
    display._display(dict(color='green', msg='test_StrategyModule'))

    # Unit test for display.display() method
    display.display(dict(color='green', msg='test_StrategyModule'))

    # Unit test for display.vv() method
    display.vv(dict(color='green', msg='test_StrategyModule'))

    # Unit test for display.vvv() method

# Generated at 2022-06-13 14:57:21.331281
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule


# Generated at 2022-06-13 14:57:26.112521
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = 'test tqm'
    sm = StrategyModule(tqm)
    assert sm.tqm == tqm, "strategy module is not initialized"
    assert sm.debugger_active is True, "debugger should be active"



# Generated at 2022-06-13 14:57:30.122367
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # test without tqm
    assert isinstance(StrategyModule(None), StrategyModule)
    # test with tqm
    class test_tqm(object):
        pass
    assert isinstance(StrategyModule(test_tqm()), StrategyModule)



# Generated at 2022-06-13 14:57:31.184571
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass


# Debugger class

# Generated at 2022-06-13 14:57:35.072612
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    print("Testing constructor of class StrategyModule")
    test_tqm = "test_tqm"
    test_strategy_module = StrategyModule(test_tqm)
    assert test_strategy_module.debugger_active == True


# Generated at 2022-06-13 14:57:39.764747
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    print("Unit test for constructor of class StrategyModule")
    sm = StrategyModule(None)
    if sm.debugger_active is False:
        print("Unit test fails. Expected 'True', passed '%s'" % sm.debugger_active)
    else:
        print("Unit test succeeds")


# Generated at 2022-06-13 14:57:41.128064
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert(StrategyModule)



# Generated at 2022-06-13 14:57:42.134017
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True

# Generated at 2022-06-13 14:57:46.406917
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    class MockTQM:
        verbosity = 2
        hosts = None
        iterable = None
        final_q = None
    tqm = MockTQM()
    strategy_module = StrategyModule(tqm)

    assert strategy_module.debugger_active == True


# Generated at 2022-06-13 14:57:54.447128
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_module = StrategyModule()
    assert strategy_module.debugger_active == True


# Generated at 2022-06-13 14:58:06.032576
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    sm = StrategyModule('tqm')
    msg = "Should have set debugger_active to True"
    assert sm.debugger_active == True, msg

if __name__ == '__main__':
    # Unit test for StrategyModule class
    test_StrategyModule()

# Generated at 2022-06-13 14:58:12.891595
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    import ansible.plugins.strategy.debug
    import ansible.plugins.strategy.linear
    tqm = 0
    sm = ansible.plugins.strategy.debug.StrategyModule(tqm)
    assert isinstance(sm, ansible.plugins.strategy.linear.StrategyModule)

# Note: for some reason the method _validate_playbooks in class StrategyModule
# is overridden.
# (The code in the method _validate_playbooks in class StrategyModule is the 
# same as that in class StrategyModule of ansible.plugins.strategy.linear 
# except for one line: super(StrategyModule, self).__init__(tqm)).
# I didn't find any difference in the effect. You can also see the same pattern
# in the constructor of class FreeStrategyModule of ansible.plugins

# Generated at 2022-06-13 14:58:16.329963
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # Create an instance of class StrategyModule
    strategy = StrategyModule(tqm)
    # Verify that debugger_active is true (unused)
    assert strategy.debugger_active == True



# Generated at 2022-06-13 14:58:18.715428
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass
    # stm = StrategyModule()
    # assert type(stm) is StrategyModule


# Generated at 2022-06-13 14:58:21.060005
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    a_StrategyModule = StrategyModule(None)
    assert isinstance(a_StrategyModule, StrategyModule)
    


# Generated at 2022-06-13 14:58:23.102792
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy = StrategyModule(tqm)
    assert strategy.debugger_active == True


# Generated at 2022-06-13 14:58:24.694222
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_module = StrategyModule(None)
    assert strategy_module.debugger_active


# Generated at 2022-06-13 14:58:25.520223
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass


# Generated at 2022-06-13 14:58:28.661428
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    class T:
        class hosts(object):
            iteritems = lambda self: [('h1', {}), ('h2', {})]
    t = T()
    sm = StrategyModule(t)
    assert sm.debugger_active


# Generated at 2022-06-13 14:58:31.549600
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    data = []
    host = []
    iterator = []
    variable_manager = []
    loader = []

    def fin():
        try:
            pass
        except:
            pass
    request.addfinalizer(fin)

    sm = StrategyModule(data, host, iterator, variable_manager, loader)
    assert True


# Generated at 2022-06-13 14:58:51.186621
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None

    # setup
    test_arg = StrategyModule(tqm)

    # assert
    assert test_arg.tqm is None
    assert test_arg.play_patterns_based is None
    assert test_arg.play_context is None
    assert test_arg.display is None
    assert test_arg.debugger_active is True


# Generated at 2022-06-13 14:58:53.018957
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    class FakeTqm(object):
        pass
    fake_tqm = FakeTqm()
    strategy_module = StrategyModule(fake_tqm)


# Generated at 2022-06-13 14:58:54.557044
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    try:
        pass
    except CommandError as e:
        pass


# Generated at 2022-06-13 14:58:57.046441
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # TODO: Add test of super class constructor
    # TODO: Add test of member debugger_active
    pass

    return # True



# Generated at 2022-06-13 14:58:58.352687
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    sm = StrategyModule()
    assert sm.debugger_active


# Generated at 2022-06-13 14:59:00.746677
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_module = StrategyModule(tqm='tqm')
    assert isinstance(strategy_module, StrategyModule)
# End of test for constructor of class StrategyModule

# Generated at 2022-06-13 14:59:02.920654
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = 'tqm'
    strategy_module = StrategyModule(tqm)
    assert strategy_module.debugger_active == True
    return


# Generated at 2022-06-13 14:59:03.740022
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule(None)
    


# Generated at 2022-06-13 14:59:06.747637
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_module = StrategyModule('Test')
    assert strategy_module is not None
    assert hasattr(strategy_module, 'tqm')


# Generated at 2022-06-13 14:59:15.429140
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.playbook.task import Task
    from ansible.executor import action_write_locks
    from ansible.executor.task_queue_manager import TaskQueueManager

    tqm = TaskQueueManager(
        inventory = None,
        variable_manager = None,
        loader = None,
        options = None,
        passwords = None,
        stdout_callback = None,
        run_additional_callbacks = True,
        run_tree = False,
    )
    sm = StrategyModule(tqm)
    assert isinstance(sm, LinearStrategyModule)
    assert sm.tqm == tqm
    assert sm.step == 0
    assert sm.topmost == {}
    assert sm.topmost_task is None
    assert sm.debugger_active



# Generated at 2022-06-13 14:59:54.312545
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    import unittest
    import mock

    class MyTest(unittest.TestCase):
        @mock.patch('ansible.plugins.strategy.linear.StrategyModule')
        def test_StrategyModule(self, strategy_module):
            StrategyModule(strategy_module)
            self.assertEqual(strategy_module.debugger_active, True)

    mytest = MyTest()
    mytest.test_StrategyModule()


# Generated at 2022-06-13 14:59:56.743451
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    try:
        sm = StrategyModule(None)
    except:
        assert(False)
    assert(True)



# Generated at 2022-06-13 15:00:00.346436
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = 'any value'
    strategy_module = StrategyModule(tqm)
    strategy_module.debugger_active = True
    assert tqm == strategy_module.tqm
    assert True == strategy_module.debugger_active



# Generated at 2022-06-13 15:00:04.968279
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # Generally dummy args
    tqm = "tqm"
    obj = StrategyModule(tqm)
    assert isinstance(obj, StrategyModule)
    assert obj._tqm == tqm
    assert obj.debugger_active == True


# Generated at 2022-06-13 15:00:08.848002
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    stub_tqm = type('stub_tqm', (object,), {})
    obj = StrategyModule(stub_tqm)
    assert hasattr(obj, 'debugger_active') and isinstance(obj.debugger_active, bool) and obj.debugger_active is True, 'Fail to initialize debugger_active'



# Generated at 2022-06-13 15:00:15.905783
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    file = open('hosts.test')
    list = file.readlines()
    list = list[0].strip().split(',')
    file.close()

    import ansible.utils.module_docs
    TQM = ansible.utils.module_docs.AnsibleModuleDocs('hosts.test', 'debug', '', [], module_docs_fragment='', verbose=True)
    module = StrategyModule(TQM)
    assert module.tqm.get_inventory().get_hosts() == list
    assert module.debugger_active is True
    
    
# Test for run method of class StrategyModule

# Generated at 2022-06-13 15:00:20.204325
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy = StrategyModule("tqm")
    assert strategy.debugger_active


    def __init__(self, tqm):
        super(StrategyModule, self).__init__(tqm)
        self.debugger_active = True


# Generated at 2022-06-13 15:00:22.837210
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = cmd.Cmd()
    sm = StrategyModule(tqm)
    assert sm.debugger_active == True


# Generated at 2022-06-13 15:00:23.965638
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # pending
    return



# Generated at 2022-06-13 15:00:28.058999
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    sm = StrategyModule(tqm)
    assert sm.debugger_active == True


##############################################################################
#
#  play_debugger
#
##############################################################################



# Generated at 2022-06-13 15:01:53.656497
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    module = StrategyModule
    #TODO: assert something here


#TODO: add unit tests for all public methods of class StrategyModule


# Generated at 2022-06-13 15:01:55.814401
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    strategy = StrategyModule(tqm)
    assert strategy.debugger_active == True


# Generated at 2022-06-13 15:02:00.872175
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass
#    if(StrategyModule('tqm') == None):
#        raise Exception("Failed to instantiate StrategyModule")

ValueError = None


# Generated at 2022-06-13 15:02:01.351438
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True

# Generated at 2022-06-13 15:02:02.275488
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True


# Run when invoked as a command

# Generated at 2022-06-13 15:02:05.364115
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # Create a test_StrategyModule
    test_StrategyModule = StrategyModule(None)
    # Assert that debugger_active is true
    assert test_StrategyModule.debugger_active == True


# Generated at 2022-06-13 15:02:06.544342
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    sm = StrategyModule(None)
    assert sm.debugger_active == True


# Generated at 2022-06-13 15:02:07.173580
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True


# Generated at 2022-06-13 15:02:09.159773
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    class StubTaskQueueManager(object):
        pass
    tqm = StubTaskQueueManager()
    sm = StrategyModule(tqm)
    assert sm.debugger_active == True


# Generated at 2022-06-13 15:02:13.459560
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    test_tqm = object()
    strategy_module = StrategyModule(test_tqm)
    assert strategy_module.debugger_active is True
