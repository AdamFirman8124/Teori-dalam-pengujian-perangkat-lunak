

# Generated at 2022-06-13 14:55:26.141429
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = 'tqm'
    assert StrategyModule(tqm)


# Generated at 2022-06-13 14:55:27.108247
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule.__name__


# Generated at 2022-06-13 14:55:29.699862
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = ''
    sm = StrategyModule(tqm)
    assert sm.tqm == ''
    assert sm.debugger_active

# Execute debugger

# Generated at 2022-06-13 14:55:30.230956
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass



# Generated at 2022-06-13 14:55:35.890567
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    '''
    Constructor of the class StrategyModule
    '''
    from ansible.executor.task_queue_manager import TaskQueueManager

    # Create task queue for test
    task_queue_manager = TaskQueueManager(
            inventory=None,
            variable_manager=None,
            loader=None,
            options=None,
            passwords=None
            )

    # Create StrategyModule object for test
    strategy_module = StrategyModule(task_queue_manager)

    # Return object which is StrategyModule
    return strategy_module


# Generated at 2022-06-13 14:55:36.734735
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    StrategyModule(tqm=None)



# Generated at 2022-06-13 14:55:40.821362
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    print('Testing StrategyModule')
    # Constructor of class StrategyModule
    strategy = StrategyModule(1)
    # Check attributes
    assert strategy.tqm == 1
    assert strategy.debugger_active == True
    # Check function inherited from superclass
    assert strategy.run() == True

# Test interactive debugger

# Generated at 2022-06-13 14:55:42.822663
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = dict()
    s = StrategyModule(tqm)
    assert s.debugger_active == True
    return s


# Generated at 2022-06-13 14:55:53.839764
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    mytask = StrategyModule('tqm')
    assert mytask.debugger_active is True


    class DebugCmd(cmd.Cmd):
        """Simple command processor example."""

        def __init__(self, *args, **kwargs):
            super(DebugCmd, self).__init__(*args, **kwargs)
            self.prompt = "debug> "

        def do_continue(self, line):
            "Switch the debugger to the 'continue' mode"
            self.debugger_active = False

        def do_pp(self, line):
            "Pretty-print the object on the command line"
            print(pprint.pformat(eval(line)))

        def do_EOF(self, line):
            "Quit the debugger"
            return True


# Generated at 2022-06-13 14:55:54.836099
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    print("Debugger constructed")


# Generated at 2022-06-13 14:55:58.391364
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    myStrategyModule = StrategyModule(tqm)
    assert myStrategyModule.debugger_active == True


# Generated at 2022-06-13 14:56:07.439482
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule(1).tqm == 1
    assert StrategyModule(1)._queue_name is None
    assert StrategyModule(1)._workers == 5
    assert StrategyModule(1)._inventory is None
    assert StrategyModule(1)._loader is None
    assert StrategyModule(1)._variable_manager is None
    assert StrategyModule(1)._host_state_callbacks == {}
    assert not StrategyModule(1)._failed_hosts
    assert not StrategyModule(1)._done
    assert not StrategyModule(1)._tqm_exit_gracefully
    assert not StrategyModule(1)._tqm_rebalance
    assert not StrategyModule(1)._tqm_rebalance_items
    assert StrategyModule(1)._job_events is None
    assert StrategyModule(1)._tqm_t

# Generated at 2022-06-13 14:56:08.600967
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True


# Generated at 2022-06-13 14:56:16.413235
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    try:
        import __main__ as main
    except ImportError:
        main = {}
    main.__file__ = 'debug'
    main.__name__ = 'debug'
    main.__package__ = None

    class TestTQM(object):
        class AnsibleTQM(object):
            def __init__(self):
                self.stats = {}

        def __init__(self):
            self.ansible_play = self.AnsibleTQM()

    tqm = TestTQM()
    try:
        strategy = StrategyModule(tqm)
        assert isinstance(strategy, StrategyModule)
    except:
        pass



# Generated at 2022-06-13 14:56:19.318586
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    print('# Unit test for constructor of class StrategyModule')
    sm = StrategyModule(None)
    if sm and sm.debugger_active:
        print('    Success')
    else:
        print('    Failed')



# Generated at 2022-06-13 14:56:19.886132
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    sm = StrategyModule(tqm)



# Generated at 2022-06-13 14:56:22.220739
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = 1
    strategy_module = StrategyModule(tqm)
    assert strategy_module.tqm == tqm
    assert strategy_module.debugger_active == True


# Generated at 2022-06-13 14:56:24.143465
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule.__doc__, "No docstring for class StrategyModule"
    assert StrategyModule.__init__, "No constructor for class StrategyModule"


# Generated at 2022-06-13 14:56:36.091481
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    class mocked_self:
        self.tqm = None
        self.host_states = dict()
        self.noop_task_result = None
    mocked_self.tqm = mocked_self()
    mocked_self.tqm.results = []
    mocked_self.tqm.hosts = dict()
    mocked_self.tqm.loop = None
    mocked_self.tqm.inventory = None
    mocked_self.tqm.callbacks = None
    mocked_self.tqm.global_vars = dict()
    mocked_self.tqm.extra_vars = dict()
    mocked_self.tqm.options = None
    mocked_self.tqm.vars_cache = dict()
    mocked_self.tqm.playbook = None
   

# Generated at 2022-06-13 14:56:41.386733
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    print("Start test_StrategyModule()")
    sm = StrategyModule(None)
    assert sm.tqm == None
    assert sm.debugger_active == True

    print("End test_StrategyModule()")


# Generated at 2022-06-13 14:56:49.486530
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    class TestTaskQueueManager(object):
        def __init__(self, host_list):
            self.host_list = host_list

    class TestTask(object):
        def __init__(self, name):
            self.name = name

        def get_name(self):
            return self.name

    class TestHost(object):
        def __init__(self, name):
            self.name = name

        def get_name(self):
            return self.name
    
    class TestInventory(object):
        def __init__(self, inventory):
            self.inventory = inventory

        def get_hosts(self):
            return self.inventory
    
    class TestOptions(object):
        def __init__(self, host_list):
            self.forks = 1

# Generated at 2022-06-13 14:57:00.765406
# Unit test for constructor of class StrategyModule
def test_StrategyModule():

    class TestTqm(object):
        def __init__(self):
            self.stats = dict(
                ok         = 0,
                changed    = 0,
                failures   = 0,
                unreachable= 2,
                skipped    = 0,
                rescued    = 0,
                ignored    = 0,
                processed  = 0,
                dark       = 0,
            )
            self.inventory = dict(
                hosts = {
                    "test_host" : {}
                },
                groups = {
                    "test_group" : {}
                }
            )

    test_tqm = TestTqm()

    class TestInventory(object):
        def __init__(self):
            self.hosts = {
                "test_host" : {}
            }

# Generated at 2022-06-13 14:57:01.589342
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True
    return True



# Generated at 2022-06-13 14:57:02.272104
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule is not None


# Generated at 2022-06-13 14:57:04.111919
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    class TQM:
        class host_list:
            __len__ = lambda self: 1

    tqm = TQM()
    sm = StrategyModule(tqm)
    assert sm.debugger_active == True


# Generated at 2022-06-13 14:57:07.231379
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # Stub
    class tqm:
        variables = { 'limit': 'dummy' }
        stats = { 'dummy': 'stats' }
    assert StrategyModule(tqm) is not None


# Generated at 2022-06-13 14:57:09.850795
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    class tqm:
        def __init__(self):
            self.stats = {}

    obj = StrategyModule(tqm())
    assert obj.debugger_active


# Generated at 2022-06-13 14:57:12.825711
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy = StrategyModule({})
    assert strategy
    assert strategy.debugger_active


# Generated at 2022-06-13 14:57:16.768717
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    sm = StrategyModule()
    assert sm.debugger_active == True
    assert sm.tqm == None
    assert sm.stats == None
    assert sm.runners == []
    assert sm.hostvars == []
    assert sm.play_context == {}
    assert sm.get_host_vars is None


# Generated at 2022-06-13 14:57:17.912090
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    c=StrategyModule(None)
    assert(c.debugger_active==True)


# Generated at 2022-06-13 14:57:27.069250
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    if (not hasattr(StrategyModule, "__init__")
        or not callable(StrategyModule.__init__)):
        return False
    sm = StrategyModule(1)
    if (not hasattr(sm, "debugger_active")
        or not sm.debugger_active):
        return False
    return True


# Generated at 2022-06-13 14:57:28.609800
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = {}
    StrategyModule(tqm)


# Generated at 2022-06-13 14:57:36.124348
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    class TestCls:
        pass

    tqm_test = TestCls()
    tqm_test.options = TestCls()
    tqm_test.options.forks = 4
    tqm_test.options.become_method = "sudo"
    tqm_test.options.become_user = "root"
    tqm_test.options.become_ask_pass = False
    tqm_test.options.become_pass = "test"
    tqm_test.options.remote_user = "test"
    tqm_test.stats = TestCls()
    tqm_test.stats.total_tasks = 0
    srm = StrategyModule(tqm_test)
    # checks

# Generated at 2022-06-13 14:57:38.380529
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    print('start')
    test = StrategyModule()
    print('end')
    return test


# Generated at 2022-06-13 14:57:38.981858
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass



# Generated at 2022-06-13 14:57:43.200091
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    class TQM:
        pass
    tqm = TQM()
    result = StrategyModule(tqm)
    assert result.tqm == tqm
    assert result.debugger_active is True


# Generated at 2022-06-13 14:57:52.217854
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    class Bunch(object):
        def __init__(self, **kwds):
            self.__dict__.update(kwds)


# Generated at 2022-06-13 14:57:53.629031
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    sm = StrategyModule(tqm)
    assert sm.debugger_active == True

# Dummy test for cmd.cmd

# Generated at 2022-06-13 14:57:54.268848
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule()

# Generated at 2022-06-13 14:57:55.020417
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass


# Generated at 2022-06-13 14:58:04.451073
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    StrategyModule(None)

#
# Debugger for Ansible's Tasks.
#

# Generated at 2022-06-13 14:58:05.842326
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    StrategyModule(tqm)


# Generated at 2022-06-13 14:58:07.621413
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_instance = StrategyModule(tqm=None)
    assert strategy_instance.debugger_active == True


# Generated at 2022-06-13 14:58:09.971232
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    x = StrategyModule(1)
    assert x.tqm == 1
    assert x.debugger_active == True


# Generated at 2022-06-13 14:58:10.584765
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass


# Generated at 2022-06-13 14:58:11.294007
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass


# Generated at 2022-06-13 14:58:11.980269
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert(StrategyModule(None))


# Generated at 2022-06-13 14:58:19.746506
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    import unittest
    import ansible.plugins.strategy.debug

    class TestStrategyModule(unittest.TestCase):
        def test_init(self):
            s = StrategyModule('test')
            self.assertEqual(s.debugger_active, True)

    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestStrategyModule))
    unittest.TextTestRunner(verbosity=2).run(suite)


# Generated at 2022-06-13 14:58:28.714193
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    try:
        import __builtin__ as builtins
    except ImportError:
        import builtins

    class Host(object):
        pass

    class Play(object):
        pass

    class PlayContext(object):
        pass

    class Task(object):
        def __init__(self):
            self.name = 'test_task'
            self.action = 'shell'
            self.args = dict()
            self.args['_raw_params'] = 'uptime'

    class TaskQueueManager(object):
        def __init__(self):
            self.hostvars = dict()
            self.hostvars['vagrant'] = 'vagrant_host'
            self.hostvars['server'] = 'server'

            self.hosts = dict()
            self.hosts['vagrant'] = Host()
           

# Generated at 2022-06-13 14:58:30.984455
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # Currently invalid test, just to make syntax checker happy
    from ansible.executor.task_queue_manager import TaskQueueManager
    assert StrategyModule(TaskQueueManager())



# Generated at 2022-06-13 14:58:48.753474
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = "sqm"
    strategy = StrategyModule(tqm)
    assert(strategy.tqm == tqm)
    assert(strategy.debugger_active == True)


# Generated at 2022-06-13 14:58:59.220915
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    config = {}
    config['ansible_verbosity'] = 2
    config['ansible_log_path'] = None
    config['ansible_diff'] = False
    config['ansible_forks'] = 5

    from ansible.playbook import Playbook
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.inventory import Inventory
    from ansible.inventory.host import Host
    from ansible.parsing import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.play_iterator import PlayIterator

    loader = DataLoader()
    inventory = Inventory(loader=loader)
    variable_manager = VariableManager()

    play_source =  dict

# Generated at 2022-06-13 14:59:00.881433
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    print("Testing constructor of StrategyModule")
    strategy = StrategyModule(None)
    assert strategy


# Generated at 2022-06-13 14:59:04.364755
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    TQM_Mock = 'TQM_Mock'
    StrategyModule(TQM_Mock)

# Wrapper class to get access to protected variables

# Generated at 2022-06-13 14:59:10.648533
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # StrategyModule is inner class.
    # So test for constructor only by use.
    sys.argv.append("--help")
    sys.argv.append("--list-tasks")
    sys.argv.append("--list-tags")
    sys.argv.append("--version")
    sys.argv.append("--forks")
    sys.argv.append("--check")
    sys.argv.append("--diff")
    sys.argv.append("--connection")
    sys.argv.append("--inventory-file")
    sys.argv.append("--list-hosts")
    sys.argv.append("--module-path")
    sys.argv.append("--module-name")
    sys.argv.append("--limit")

# Generated at 2022-06-13 14:59:11.642320
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True


# Generated at 2022-06-13 14:59:16.479185
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    class MockTqm(object):
        pass
    my_tqm = MockTqm()
    my_strategy = StrategyModule(my_tqm)
    assert my_strategy.tqm == my_tqm, "test_StrategyModule: constructor for StrategyModule failed"

test_StrategyModule()


# Generated at 2022-06-13 14:59:18.376682
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # TODO: Add tests
    import unittest
    unittest.TestCase()


# Generated at 2022-06-13 14:59:19.775019
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule


# Generated at 2022-06-13 14:59:22.253490
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    mocker = mock.MagicMock()
    module = StrategyModule(mocker)
    assert module.debugger_active



# Generated at 2022-06-13 14:59:58.168951
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = object()
    debugger_active = True
    sm = StrategyModule(tqm)
    assert sm.tqm == tqm
    assert sm.debugger_active == debugger_active


# Generated at 2022-06-13 15:00:01.564125
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = 'use list of hosts'
    sm = StrategyModule(tqm)
    assert sm.tqm == tqm
    assert not sm.debugger_active


# Generated at 2022-06-13 15:00:02.213518
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass


# Generated at 2022-06-13 15:00:05.172504
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = 'tqm'
    try:
        StrategyModule(tqm)
    except NameError:
        assert False


# Class to execute interactive debug session

# Generated at 2022-06-13 15:00:10.659784
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    class TQM(object):
        nothing = False
    tqm = TQM()
    strategy = StrategyModule(tqm)
    assert tqm == strategy.tqm
    assert strategy.debugger_active == True
    assert strategy.should_debug_task == False
    assert strategy.should_interrupt_handler == False
    assert strategy.breakpoints == []


# Generated at 2022-06-13 15:00:12.939055
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass

    # Create a test object
    # tqm =
    test_obj = StrategyModule(tqm)

    # Can't test private methods


# Generated at 2022-06-13 15:00:19.975390
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    class tqm:
        def __init__(self):
            self.inventory = None
            self.variable_manager = None
            self.loader = None
            self.options = 'debug'
            self.passwords = {}
            self.stdout_callback = 'default'
            self.callback = None
            self.task_queue = None
            self.notified_handlers = {}
            self.stats = None
            self.failed_hosts = 'hosts'
            self.unreachable_hosts = 'hosts'
            self.blocked_hosts = 'hosts'
            self.tqm_rc = 0
            self.cur_worker = 'worker'

    tqm = tqm()
    pprint.pprint(tqm.__dict__)
    
    s = StrategyModule

# Generated at 2022-06-13 15:00:21.585699
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # TODO: Add unit test for constructor of class StrategyModule.
    pass


# Generated at 2022-06-13 15:00:23.739403
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    quick_start = StrategyModule(None)
    assert quick_start.debugger_active == True


# Generated at 2022-06-13 15:00:25.565082
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # We do not want to test StrategyModule in this file
    pass



# Generated at 2022-06-13 15:01:41.357920
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule.debugger_active == True



# Generated at 2022-06-13 15:01:43.127044
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # Test Case 1
    #         Test case for this class is not implemented yet. So, here we just
    #         write one line to cover the init function.
    #         Expected result:
    #             - The class name should be StrategyModule.
    assert "StrategyModule" in str(type(StrategyModule))


# Generated at 2022-06-13 15:01:43.939019
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    StrategyModule(None)


# Subclass of cmd.Cmd that allows multiple task debugging

# Generated at 2022-06-13 15:01:47.617069
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    test_tqm = None
    print('Testing constructor of class StrategyModule')
    sm = StrategyModule(test_tqm)
    print(sm.debugger_active)
    print('Testing done')



# Generated at 2022-06-13 15:01:49.748878
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    s = StrategyModule("test")
    assert(s.debugger_active == True)
    return



# Generated at 2022-06-13 15:01:53.747128
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = "tqm"
    test_object = StrategyModule(tqm)
    assert test_object.debugger_active is True
    assert test_object.tqm == tqm


# This class will implement a terminal interface for the debug module

# Generated at 2022-06-13 15:01:56.883574
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # Declare local variables
    class tqm:
        pass
    # Initialize class
    x = StrategyModule(tqm)
    # Check initialization of class
    assert(x.debugger_active == True)



# Generated at 2022-06-13 15:01:59.014537
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    StrategyModule(None)



# Generated at 2022-06-13 15:02:01.767527
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule.__name__ == 'StrategyModule'
    assert StrategyModule.__mro__ == (StrategyModule, LinearStrategyModule, object)



# Generated at 2022-06-13 15:02:05.746575
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    module = StrategyModule('')
    assert(module.debugger_active == True)

##########################################################
#                                                        #
#   Module for debugging                                 #
#                                                        #
##########################################################

##########################################################
#   cmd.Cmd is defined in                                #
#   http://docs.python.org/2/library/cmd.html            #
##########################################################


# Generated at 2022-06-13 15:04:48.835537
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    test1 = StrategyModule(1)
    assert(test1.name == 'debug')
    assert(test1.debugger_active == True)


# Generated at 2022-06-13 15:04:57.779568
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    import imp
    import tempfile
    import os
    import shutil

    def _mock_terminate(self, result=True, repl='', status='successful'):
        return (repl, status)

    def _mock_run_playbook(self, hosts, playbook_path, play, condition,
                           module_path, start_at_task=None,
                           verbosity=0, extra_vars=None, private_key_file=None,
                           tags=None, skip_tags=None,
                           checkpoint=None, checkpoint_condition=None):
        return (0, '')

    def _mock_get_extra_vars(self):
        return {}

    def _mock_get_var(self, varname):
        return {}


# Generated at 2022-06-13 15:05:00.079305
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    test_tqm = dict()
    strategy_module = StrategyModule(test_tqm)
    assert strategy_module.tqm == test_tqm
    assert strategy_module.debugger_active == True


# Generated at 2022-06-13 15:05:02.499128
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    print('Test: start')
    tqm = 0
    sm = StrategyModule(tqm)
    assert sm.debugger_active == True
    print('Test: completed')


# Generated at 2022-06-13 15:05:04.193650
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    try:
        sm = StrategyModule(None)
    except:
        assert False, "StrategyModule constructor should not raise an exception"
    assert True


# Generated at 2022-06-13 15:05:07.246585
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    print("Unit test for constructor of class StrategyModule")
    # Constructor of class StrategyModule should set debugger_active = True
    strategyModule = StrategyModule(None)
    if strategyModule.debugger_active == True:
        print ("Pass")
    else:
        print ("Fail")

if __name__ == '__main__':
    test_StrategyModule()

# Generated at 2022-06-13 15:05:18.635573
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    global_vars = {"ansible_check_mode": False}
    callback = None
    runner = None
# Unit test only implemented for ansible v2.2.1.0(gate commit:a475d076b53c)
    class Tqm():
        def __init__(self, inventory, variable_manager, loader, options, passwords, stdout_callback=callback, run_additional_callbacks=callback, run_tree=False, stdout_callback_whitelist=runner, stdout_callback_blacklist=runner):
            self.inventory = inventory
            self.variable_manager = variable_manager
            self.loader = loader
            self.options = options
            self.passwords = passwords
            self.stdout_callback = stdout_callback
            self.run_additional_callbacks = run_additional_call

# Generated at 2022-06-13 15:05:20.356758
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pdb = StrategyModule(None)
    assert pdb.debugger_active



# Generated at 2022-06-13 15:05:21.685830
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    obj = StrategyModule()
    assert obj.debugger_active == True


# Generated at 2022-06-13 15:05:25.336833
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    try:
        sm = StrategyModule('tqm')
        if sm.debugger_active == True:
            print('Test 1 passed')
        else:
            print('Test 1 failed')
    except:
        print('Test 1 failed')

# Simple test cases for unit test with fake arguments