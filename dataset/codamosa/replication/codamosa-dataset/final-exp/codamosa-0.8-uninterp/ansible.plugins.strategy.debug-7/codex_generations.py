

# Generated at 2022-06-13 14:55:30.508682
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    print("---[START] test_constructor")
    assert(StrategyModule)
    print("---[END] test_constructor")


# Generated at 2022-06-13 14:55:33.009446
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # Arrange
    tqm = None # stub

    # Action
    strategy = StrategyModule(tqm)

    # Assert
    assert strategy.debugger_active == True


# Generated at 2022-06-13 14:55:35.150833
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    print('### In test_StrategyModule()')
    sm = StrategyModule(None)
    pprint.pprint(sm.__dict__)

test_StrategyModule()


# Generated at 2022-06-13 14:55:35.930612
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    StrategyModule(None)



# Generated at 2022-06-13 14:55:36.899694
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    StrategyModule(None)


# Generated at 2022-06-13 14:55:39.214156
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    result = StrategyModule(None)
    assert isinstance(result, LinearStrategyModule)
    assert isinstance(result, StrategyModule)


# Generated at 2022-06-13 14:55:41.725747
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    print("\n Constructor for class StrategyModule \n")
    strategy_module = StrategyModule(None)
    print(strategy_module.debugger_active)


# Generated at 2022-06-13 14:55:44.760610
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    args = {'_ansible_debug': True}
    tqm = FakeTQM(args)
    sm = StrategyModule(tqm)
    assert sm.debugger_active




# Generated at 2022-06-13 14:55:45.803304
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True

# Generated at 2022-06-13 14:55:49.866874
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    import mock
    import ansible.plugins.strategy.debug as debug

    tqm = mock.Mock()

    d = debug.StrategyModule(tqm)

    assert d.debugger_active is True
    assert d.tqm == tqm

# Generated at 2022-06-13 14:55:57.964560
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule.__doc__ == '''\
    Allows Ansible tasks to be run in an interactive debug session.\n\n    This is a very basic implementation of a debugger using python's cmd module.\n    '''
    assert StrategyModule.__init__.__doc__ == '''\
        Create a new instance of the StrategyModule.\n\n        :type tqm: TaskQueueManager\n        :param tqm: TaskQueueManager object\n        '''
    assert StrategyModule.__module__ == 'ansible.plugins.strategy.debug'
    assert StrategyModule.__name__ == 'StrategyModule'


# Generated at 2022-06-13 14:55:59.576238
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    _ = StrategyModule(tqm=None)


# Generated at 2022-06-13 14:56:01.488584
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    for k, v in StrategyModule.__dict__.items():
        print(k, v)



# Generated at 2022-06-13 14:56:02.424239
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True  # TODO: implement your test here

# Command line for debugger

# Generated at 2022-06-13 14:56:04.953579
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # Test StrategyModule class constuctor
    tqm = True
    sm = StrategyModule(tqm)
    assert sm.debugger_active == True



# Generated at 2022-06-13 14:56:07.259207
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    try:
        s = StrategyModule(None)
    except:
        assert False
    else:
        assert True



# Generated at 2022-06-13 14:56:08.849466
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = ''
    StrategyModule(tqm)



# Generated at 2022-06-13 14:56:10.340952
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert not StrategyModule(tqm=None).debugger_active



# Generated at 2022-06-13 14:56:17.730446
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True


    def get_host_var(self, host, varname):

        # First filter within groups
        all_host_vars = self.inventory.get_vars(host)
        if varname in all_host_vars:
            return all_host_vars[varname]

        # Second look in vars
        data = self.inventory.get_host(host)
        if data is not None:
            all_group_vars = self.inventory.get_vars(data, 'all')
            if varname in all_group_vars:
                return all_group_vars[varname]

        return None



# Generated at 2022-06-13 14:56:18.648610
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    test_tqm = {}
    StrategyModule(test_tqm)



# Generated at 2022-06-13 14:56:21.722783
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    #test_strategy = StrategyModule()
    pass



# Generated at 2022-06-13 14:56:25.273972
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    class DummyTqm(object):
        def get_play(self):
            return False

    dTqm = DummyTqm()
    sm = StrategyModule(dTqm)
    sm.debugger_active = False
    assert sm.debugger_active is False

test_StrategyModule()

# Ansible command line debugger

# Generated at 2022-06-13 14:56:26.014840
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass



# Generated at 2022-06-13 14:56:28.344301
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_module = StrategyModule(tqm)



# Generated at 2022-06-13 14:56:31.958171
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    print (StrategyModule)
    print (type(StrategyModule))

# TODO:
# '''
#   ansible localhost -m ping -M test/integration/test_module_data
# '''



# Generated at 2022-06-13 14:56:33.098790
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = StrategyModule('tqm')
    assert tqm.debugger_active is True
    assert tqm.tqm == 'tqm'



# Generated at 2022-06-13 14:56:40.866664
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    try:
        import __main__ as main
    except ImportError:
        main = sys.modules['__main__']
    setattr(main, '__file__', 'debug')
    from ansible.utils.vars import TaskVars
    from ansible.plugins import strategy_loader
    from ansible.playbook.task import Task
    from ansible.vars.hostvars import HostVars
    class MockTqm(object):
        def __init__(self, hostvars):
            self._hostvars = hostvars
        def get_host(self, hostname):
            host = HostVars(vars={})
            host.name = hostname
            return host
        def run(self, *args, **kwargs):
            pass

# Generated at 2022-06-13 14:56:44.656857
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    #constructor of class StrategyModule
    #asserts that constructor actually succeeded
    assert(test1.debugger_active == True)
    #asserts that constructor actually failed
    #assert(test1.debugger_active == False)

test1 = StrategyModule()



# Generated at 2022-06-13 14:56:49.185444
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.plugins.strategy.debug import StrategyModule
    # create a mock tqm
    class MockTqm(object):
        def __init__(self):
            self.hostvars = {}
    tqm = MockTqm()
    sm = StrategyModule(tqm)
    assert sm.debugger_active == True


# Generated at 2022-06-13 14:56:51.628318
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    StrategyModule(tqm)



# Generated at 2022-06-13 14:56:57.150508
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    module = StrategyModule(None)
    assert module
    assert isinstance(module, StrategyModule)


# Generated at 2022-06-13 14:56:58.110895
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass


# Generated at 2022-06-13 14:57:00.788719
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    stm = StrategyModule(tqm)
    if not stm.debugger_active:
        raise Exception("test_StrategyModule failed")


# Generated at 2022-06-13 14:57:02.155687
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_obj = StrategyModule()
    assert strategy_obj.debugger_active == True


# Generated at 2022-06-13 14:57:03.830629
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    for name in dir(StrategyModule):
        #if name.startswith("_"):
        #    continue
        print(name, getattr(StrategyModule, name))


# Generated at 2022-06-13 14:57:04.579258
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert False


# Generated at 2022-06-13 14:57:15.919513
# Unit test for constructor of class StrategyModule

# Generated at 2022-06-13 14:57:17.204074
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule.__name__ == 'StrategyModule'

# Unit test of first command in debugger


# Generated at 2022-06-13 14:57:17.886658
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    StrategyModule(None)


# Generated at 2022-06-13 14:57:22.385846
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    class TestTqm:
        def __init__(self):
            self.terminated = False
    
    tqm = TestTqm()
    strategy_module = StrategyModule(tqm)

    assert strategy_module.tqm == tqm
    assert strategy_module.get_host_list() == []
    assert strategy_module.get_host_keys_sorted() == []
    assert strategy_module.host_state == {}
    assert strategy_module.debugger_active == True
# Units tests for methods of class StrategyModule

# Generated at 2022-06-13 14:57:30.864810
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # TODO:
    pass


# Generated at 2022-06-13 14:57:39.628947
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert len(sys.argv) == 4
    plugin_name = sys.argv[0]
    config_file = sys.argv[1]
    color = sys.argv[2]
    log_path = sys.argv[3]

    # Create an instance of debugger
    so = StrategyModule(None)
    # Check if the debugger is active
    assert so.debugger_active
    # TODO: Check if below lines are necessary
    # Show the result of debug.
    #dir(so)
    #dir(so.tqm)
    #assert False


# Generated at 2022-06-13 14:57:40.936460
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule is not None


# Generated at 2022-06-13 14:57:44.148000
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    task_queue_manager = None
    strategy_module = StrategyModule(task_queue_manager)
    assert strategy_module.debugger_active


# Generated at 2022-06-13 14:57:46.004890
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = object
    strategy_module = StrategyModule(tqm)
    assert hasattr(strategy_module, 'debugger_active')
    assert strategy_module.debugger_active == True


# Generated at 2022-06-13 14:57:54.200290
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    import ansible.utils.collection_loader
    tests = ansible.utils.collection_loader.AllCollections('')
    paths = []
    results = tests.collect_files(paths, 'test_plugins')
    collection = ansible.utils.collection_loader.all_collection_paths(tests)
    assert collection == results
    print("\n" + pprint.pformat(collection) + "\n")
    sys.path.extend(collection)
    print("\n" + pprint.pformat(sys.path) + "\n")
    import ansible.plugins
    plugins = [ x for x in ansible.plugins.__dict__.values() if type(x) == type and issubclass(x, ansible.plugins.ActionBase) ]

# Generated at 2022-06-13 14:57:56.650268
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # When
    s = StrategyModule('tqm')
    # Then
    assert s.debugger_active == True


# Generated at 2022-06-13 14:57:57.617081
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass


# Generated at 2022-06-13 14:57:59.779737
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = TaskQueueManager()
    sm = StrategyModule(tqm)
    assert sm.debugger_active == True


# Generated at 2022-06-13 14:58:08.686628
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule.__name__ == 'StrategyModule'
    
    # Test that the constructor for StrategyModule exits if tqm is not provided
    try:
        StrategyModule(tqm=None)
        assert False, "StrategyModule constructor did not exit when tqm was not provided"
    except SystemExit as e:
        assert e.code == 10, "StrategyModule exited with expected error code when tqm was not provided"

    # Test that the constructor for StrategyModule does not exit if tqm is provided
    try:
        StrategyModule(tqm={})
        assert True
    except SystemExit:
        assert False, "StrategyModule constructor exited when tqm was provided"



# Generated at 2022-06-13 14:58:26.936189
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.executor.task_queue_manager import TaskQueueManager
    myStrat = StrategyModule(TaskQueueManager())
    assert myStrat.name == 'debug'
    assert myStrat.debugger_active is True


# Generated at 2022-06-13 14:58:29.388479
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = 'tqm'
    my_StrategyModule = StrategyModule(tqm)
    assert my_StrategyModule.tqm == tqm
    assert my_StrategyModule.debugger_active is True


# Generated at 2022-06-13 14:58:30.022632
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule(None)



# Generated at 2022-06-13 14:58:32.280825
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_module = StrategyModule("tqm")
    strategy_module.debugger_active = False
    assert not strategy_module.debugger_active


# Generated at 2022-06-13 14:58:36.495130
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # Dummy task queue manager.
    tqm = object()
    ret = StrategyModule(tqm)

    assert ret.debugger_active
    assert not ret.get_next_task_lock()
    assert not ret.job_queue
    assert ret.tqm == tqm


# Generated at 2022-06-13 14:58:38.770685
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule is not LinearStrategyModule
    assert isinstance(StrategyModule, type(LinearStrategyModule))



# Generated at 2022-06-13 14:58:44.140793
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # create dummy task queue manager
    class task_queue_manager:
        def __init__(self):
            self.host_result_callback = None
    tqm = task_queue_manager()
    strategy = StrategyModule(tqm)
    assert strategy
    assert strategy.debugger_active

# Generated at 2022-06-13 14:58:44.779269
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert False


# Generated at 2022-06-13 14:58:45.600239
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    stgy = StrategyModule(None)
    assert stgy.debugger_active is True


# Generated at 2022-06-13 14:58:53.167394
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.plugins.strategy import debug
    from ansible.playbook.task import Task
    from ansible.playbook.play_iterator import PlayIterator
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.stats import AggregateStats
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

# Generated at 2022-06-13 14:59:27.472798
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_module = StrategyModule(None)
    assert strategy_module.debugger_active
# End of unit test for constructor of class StrategyModule




# Generated at 2022-06-13 14:59:31.437701
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    import ansible.plugins.loader as plugin_loader
    tqm = plugin_loader.load_callback_plugins('action')
    strategy = StrategyModule(tqm)
    assert isinstance(strategy, StrategyModule)


# Generated at 2022-06-13 14:59:37.068137
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from units.mock.loader import DictDataLoader
    from units.mock.inventory import MockInventory
    from ansible.vars import VariableManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.playbook import Playbook

    variable_manager = VariableManager()
    loader = DictDataLoader({})
    inventory = MockInventory(loader)
    playbook = Playbook.load("./test/playbook/playbook_debug.yml", loader, variable_manager, inventory)
    executor = PlaybookExecutor(playbooks=[playbook], inventory=inventory, variable_manager=variable_manager, loader=loader, options=None, passwords={})
    ret = executor.run()
    assert ret == 0

if __name__ == '__main__':
    import sys


# Generated at 2022-06-13 14:59:42.167133
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    import ansible.plugins.strategy.debug

    tqm = ansible.plugins.strategy.debug.StrategyModule.test_tqm()

    strategy = ansible.plugins.strategy.debug.StrategyModule(tqm)
    assert strategy.debugger_active == True


# Generated at 2022-06-13 14:59:43.845802
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    StrategyModule(None)

# -------------------------------
# Debugger interface
# -------------------------------


# Generated at 2022-06-13 14:59:45.717364
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_module = StrategyModule(None)
    assert strategy_module.debugger_active == True


# Generated at 2022-06-13 14:59:46.889104
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert callable(StrategyModule)


# Generated at 2022-06-13 14:59:52.339416
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # Try to connect to terminal to confirm that
    # batch mode is not active
    try:
        import termios, tty
        isatty = sys.stdin.isatty()
    except ImportError:
        isatty = False

    # Only continue if connected to terminal
    if isatty:
        sm = StrategyModule(None)
        assert(True)
    else:
        assert(False)



# Generated at 2022-06-13 14:59:55.456375
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    print("StrategyModule")
    tqm = {"_dump_results": False,
           "_stats": {},
           "_tqm_variables": {},
           }
    assert hasattr(StrategyModule(tqm), "tqm")



# Generated at 2022-06-13 14:59:56.918988
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass

    # TASK cannot be tested



# Generated at 2022-06-13 15:01:16.709588
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    TASK_QUEUE_MANAGER = None
    strategy_module = StrategyModule(TASK_QUEUE_MANAGER)
    assert strategy_module.debugger_active
    
    assert strategy_module.name == "linear"
    assert strategy_module._queue is not None
    assert strategy_module._final_q is not None
    assert strategy_module._failed_hosts is not None
    assert strategy_module._tqm is not None
    assert strategy_module._strategy is not None
    assert strategy_module._host_pin_set is not None
    assert strategy_module._stats is not None
    assert strategy_module._display is not None
    assert strategy_module._display._display is not None
    assert strategy_module._callback_plugins == []
    assert strategy_module._stats_queue is not None


# Generated at 2022-06-13 15:01:17.402179
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True

# Generated at 2022-06-13 15:01:25.740601
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    import ansible.constants as C
    C.DEFAULT_INVENTORY = u'/Users/kishin/repos/ansible/test/inventory'
    C.DEFAULT_HOST_LIST = u'/Users/kishin/repos/ansible/test/inventories/hosts'
    C.INVENTORY = u'/Users/kishin/repos/ansible/test/inventory'
    C.HOST_LIST = u'/Users/kishin/repos/ansible/test/inventories/hosts'
    print(StrategyModule)



# Generated at 2022-06-13 15:01:26.599879
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule
    st = StrategyModule('tqm')
    assert st.debugger_active == True


# Generated at 2022-06-13 15:01:27.512834
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule is not None


# Generated at 2022-06-13 15:01:33.604458
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    try:
        import ansible.playbook.play
        import ansible.playbook.task
        import ansible.playbook.task_include
    except ImportError:
        sys.exit("Failed to import imports in debugger plugin.")

    # Test StrategyModule
    try:
        tqm = object()
        module = StrategyModule(tqm)
        if not module.tqm == tqm:
            sys.exit("Failed to set tqm in debugger plugin.")
        if not module.debugger_active:
            sys.exit("Failed to set debugger_active in debugger plugin.")
    except Exception as ex:
        sys.exit("Test for StrategyModule failed with exception: " + str(ex))



# Generated at 2022-06-13 15:01:36.932262
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    print(StrategyModule.__mro__)
    assert StrategyModule.__name__ == 'StrategyModule'
    assert StrategyModule.__bases__ == (LinearStrategyModule,)
    return StrategyModule



# Generated at 2022-06-13 15:01:40.644717
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    class TestTaskQueueManager:
        def __init__(self):
            pass
        pass

    class TestLogger:
        def __init__(self, level):
            pass
        pass

    strategy_module = StrategyModule(TestTaskQueueManager())
    assert strategy_module



# Generated at 2022-06-13 15:01:43.164508
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    try:
        StrategyModule()
        assert False
    except Exception as e:
        assert str(e) == 'This interface must be implemented by a subclass'
        assert True
    except:
        assert False


# Generated at 2022-06-13 15:01:47.714819
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    """ Test StrategyModule class """
    import pdb
    import unittest
    import ansible
    class TestStrategyModule(unittest.TestCase):
        def test_strategy_module(self):
            """ Tests StrategyModule class constructor """
            self.assertRaises(Exception, StrategyModule, ansible)
    StrategyModule(ansible)


# Generated at 2022-06-13 15:04:40.127530
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass
# TODO define assert instance(StrategyModule(???), type(StrategyModule))

_debug_msgs = ['CS', 'ES', 'RUN', 'SETUP', 'TASK', 'CLEANUP']

# monkeypatch the StrategyModule class
StrategyModule.__name__ = 'StrategyModule'



# Generated at 2022-06-13 15:04:40.933952
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    print(__file__)



# Generated at 2022-06-13 15:04:42.008355
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule(tqm=None)


# Generated at 2022-06-13 15:04:43.608242
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    module = StrategyModule()
    assert module.debugger_active == True


# Generated at 2022-06-13 15:04:44.053077
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass


# Generated at 2022-06-13 15:04:45.556678
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    some_tqm = 0
    try:
        StrategyModule(some_tqm)
    except:
        assert False
    finally:
        pass

# Generated at 2022-06-13 15:04:46.135455
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass


# Generated at 2022-06-13 15:04:55.612787
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    try:
        import __builtin__
        __builtin__.__dict__.get('_') or __builtin__.__dict__.__setitem__('_', lambda *msg, **kwargs: msg[0])
    except ImportError:
        pass
    try:
        import __builtin__
        __builtin__.__dict__.get('N_') or __builtin__.__dict__.__setitem__('N_', lambda *msg, **kwargs: msg[0])
    except ImportError:
        pass
    try:
        import __builtin__
        __builtin__.__dict__.get('C_') or __builtin__.__dict__.__setitem__('C_', lambda *msg, **kwargs: msg[0])
    except ImportError:
        pass
    import ans

# Generated at 2022-06-13 15:04:56.112821
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass


# Generated at 2022-06-13 15:04:57.828132
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pp = pprint.PrettyPrinter(indent=1)
    pp.pprint(test_StrategyModule)
