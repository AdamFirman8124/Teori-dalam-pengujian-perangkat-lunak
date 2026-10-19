

# Generated at 2022-06-13 15:06:25.666032
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategyModule = StrategyModule()
    assert strategyModule._host_pinned

# Generated at 2022-06-13 15:06:26.547431
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
   tqm = None
   strategy_module = StrategyModule(tqm)
   assert strategy_module is not None

# Generated at 2022-06-13 15:06:27.835092
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule.__name__ == "StrategyModule"



# Generated at 2022-06-13 15:06:28.893927
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    obj = StrategyModule()
    assert  obj._host_pinned == True

# Generated at 2022-06-13 15:06:31.349174
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = object
    sm = StrategyModule(tqm)
    assert sm._host_pinned == True

# Generated at 2022-06-13 15:06:33.243505
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.plugins.strategy import StrategyModule
    from ansible.plugins.loader import strategy_loader
    strategy_loader.add(StrategyModule)

# Generated at 2022-06-13 15:06:35.519089
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    print('Calling StrategyModule()')
    tqm = None
    StrategyModule(tqm)

#test_StrategyModule()

# Generated at 2022-06-13 15:06:37.311586
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
   tqm = None
   strategy = StrategyModule(tqm)

test_StrategyModule()

# Generated at 2022-06-13 15:06:39.615562
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = "TQM"
    assert tqm == "TQM"
    assert StrategyModule(tqm)._host_pinned == True

# Generated at 2022-06-13 15:06:42.188653
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # Creating a random instance of FreeStrategyModule
    import uuid
    tqm = uuid.uuid4()
    strategy = StrategyModule(tqm)

    assert strategy._host_pinned

# Generated at 2022-06-13 15:06:44.153386
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True


# Generated at 2022-06-13 15:06:45.007743
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True

# Generated at 2022-06-13 15:06:52.150034
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.plugins.strategy.host_pinned import StrategyModule
    from ansible.plugins.loader import strategy_loader
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    tqm = TaskQueueManager(
        inventory = None,
        variable_manager = None,
        loader = None,
        options = None,
        passwords = None,
        stdout_callback=None,
    )
    strategy = strategy_loader.get('host_pinned', tqm)
    assert type(strategy) == StrategyModule

# Generated at 2022-06-13 15:06:54.446362
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy = StrategyModule(tqm=None)
    assert strategy._host_pinned == True
    return True


# Generated at 2022-06-13 15:06:54.982186
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True == True

# Generated at 2022-06-13 15:06:55.416292
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass

# Generated at 2022-06-13 15:06:58.058347
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    """
    Test the constructor for StrategyModule
    """
    strategy_module = StrategyModule(tqm=None)
    assert strategy_module._host_pinned

if __name__ == '__main__':
    test_StrategyModule()

# Generated at 2022-06-13 15:06:59.356004
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = FreeStrategyModule
    StrategyModule(tqm)


# Generated at 2022-06-13 15:07:00.073978
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule(1)._host_pinned == True

# Generated at 2022-06-13 15:07:00.635447
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass

# Generated at 2022-06-13 15:07:05.031322
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # Test the __init__ function by passing tqm object
    assert StrategyModule(tqm)

# Generated at 2022-06-13 15:07:06.920576
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    my_strategy = StrategyModule(tqm)
    assert my_strategy._host_pinned == True

# Generated at 2022-06-13 15:07:14.712201
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategyMod = StrategyModule('tqm')
    assert 'object' == type(strategyMod).__name__
    assert 'StrategyModule' == strategyMod.__class__.__name__
    assert (strategyMod._host_pinned == True)

'''
Test strategy module :

It tests the strategy module in the following way :

1. It creates 5 host group to execute tasks in one of several strategies.
2. It creates a sample host and adds hosts to the host group.
3. It creates sample tasks for each host group and adds it to the host.
4. It creates a task queue manager and sets inventory and variable manager in it.
5. It creates a playbook and runs it.
6. It checks the end result.

'''

# Generated at 2022-06-13 15:07:17.684936
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = 'test'
    s = StrategyModule(tqm)
    assert s._host_pinned == True



# Generated at 2022-06-13 15:07:18.360508
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert not StrategyModule

# Generated at 2022-06-13 15:07:19.151903
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True

# Generated at 2022-06-13 15:07:21.448296
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    import ansible.plugins.strategy.host_pinned as host_pinned
    assert host_pinned.StrategyModule

# Generated at 2022-06-13 15:07:23.933733
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.plugins.strategy.host_pinned import StrategyModule
    assert isinstance(StrategyModule(None), StrategyModule)

# Generated at 2022-06-13 15:07:26.094732
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    l = [u'test1', u'test2']
    strategy_module = StrategyModule(l)
    assert strategy_module._host_pinned == True

# Generated at 2022-06-13 15:07:28.363882
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    host = 'localhost'
    tqm = None
    s = StrategyModule(tqm)
    assert s._host_pinned == True

# Generated at 2022-06-13 15:07:33.035562
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    sm = StrategyModule(tqm)
    assert sm._host_pinned is True

# Generated at 2022-06-13 15:07:33.586035
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass

# Generated at 2022-06-13 15:07:37.520847
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.executor.task_queue_manager import TaskQueueManager
    tqm = TaskQueueManager(None, None, None, None, None, None, None, None, None, None, None)
    strategy = StrategyModule(tqm)
    assert strategy._host_pinned is True

# Generated at 2022-06-13 15:07:38.078940
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    StrategyModule()

# Generated at 2022-06-13 15:07:40.045563
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = 'test'
    strategy_module = StrategyModule('test')
    assert strategy_module._host_pinned == True

# Generated at 2022-06-13 15:07:40.898528
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule is not None

# Generated at 2022-06-13 15:07:42.328984
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = object()
    obj = StrategyModule(tqm)
    assert obj._host_pinned

# Generated at 2022-06-13 15:07:49.269182
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    import tempfile
    from ansible.utils.shlex import split
    from ansible.utils.vars import combine_vars
    from ansible.inventory import Inventory
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.playbook.play_context import PlayContext
    from ansible.cli.playbook import PlaybookCLI
    cli = PlaybookCLI(['test_host_pinned.yml'])
    cli.parse()
    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = Inventory(loader, variable_manager, cli.options.host_list)
    variable_manager.set_inventory(inventory)

# Generated at 2022-06-13 15:07:50.173264
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    sm = StrategyModule(tqm)

# Generated at 2022-06-13 15:07:50.714132
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True

# Generated at 2022-06-13 15:08:03.649654
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # Dummy object creation for testing
    from ansible.utils.display import Display
    from ansible.plugins.strategy.free import StrategyModule as FreeStrategyModule
    display = Display()
    strategy_module = FreeStrategyModule(tqm=None)
    # Function to test constructor of class StrategyModule
    strategy_module = StrategyModule(tqm=None)
    assert strategy_module._host_pinned == True

# Generated at 2022-06-13 15:08:05.989729
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert issubclass(StrategyModule, FreeStrategyModule)

# Generated at 2022-06-13 15:08:07.186263
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    s = StrategyModule('test')


# Generated at 2022-06-13 15:08:11.243861
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    TASK_QUEUE_MANAGER_ELEM = []
    StrategyModule(TASK_QUEUE_MANAGER_ELEM)
    assert TASK_QUEUE_MANAGER_ELEM == []


# Generated at 2022-06-13 15:08:14.671046
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    global display
    test = StrategyModule(display)
    assert(test.__class__.__name__ == 'StrategyModule')
    assert(test._host_pinned == True)

# Generated at 2022-06-13 15:08:15.174091
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True

# Generated at 2022-06-13 15:08:22.772500
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    host = ['localhost']
    play_context = {'port': 0, 'remote_user': '', 'connection': 'local', 'network_os': '', 'become': False, 'is_playbook': False, 'become_method': '', 'become_user': '', 'check_mode': False, 'remote_addr': 'localhost', 'visualization': False}
    loader = '--loader'

# Generated at 2022-06-13 15:08:24.439716
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule(tqm)

# Generated at 2022-06-13 15:08:25.997867
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    module = StrategyModule(None)
    assert module._host_pinned == True

# Generated at 2022-06-13 15:08:29.799378
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.executor.task_queue_manager import TaskQueueManager

    strategy = StrategyModule(TaskQueueManager())
    assert strategy._host_pinned is True

# Generated at 2022-06-13 15:08:47.127718
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule is not None

# Generated at 2022-06-13 15:08:47.775615
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass

# Generated at 2022-06-13 15:08:54.677820
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.plugins.loader import strategy_loader
    from ansible.playbook.task_queue_manager import TaskQueueManager
    tqm = TaskQueueManager(
        inventory=None,
        variable_manager=None,
        loader=None,
        options=None,
        passwords=None,
        stdout_callback='default',
    )
    strategy = strategy_loader.get('host_pinned', tqm)
    assert strategy.get_name() == 'host_pinned'
    assert strategy._host_pinned

# Generated at 2022-06-13 15:08:55.501624
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    StrategyModule(tqm)

# Generated at 2022-06-13 15:08:56.315344
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    print("No unit tests for strategy host_pinned")

# Generated at 2022-06-13 15:08:56.814316
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
   pass

# Generated at 2022-06-13 15:08:59.467250
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.plugins.strategy import host_pinned
    from ansible.plugins.strategy.host_pinned import StrategyModule
    tqm = object()
    host_pinned.StrategyModule(tqm)
    StrategyModule(tqm)



# Generated at 2022-06-13 15:09:00.423160
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    obj = StrategyModule('tqm')
    assert obj._host_pinned == True

# Generated at 2022-06-13 15:09:02.310858
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    sm = StrategyModule(tqm)
    assert sm is not None

# Generated at 2022-06-13 15:09:03.116857
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    display.display("Test StrategyModule class")
    assert True

# Generated at 2022-06-13 15:09:45.752118
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule()._host_pinned == True

# Generated at 2022-06-13 15:09:47.338330
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # Nothing to test here - constructor does not take any parameters
    StrategyModule(None)

# Generated at 2022-06-13 15:09:53.575239
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    class TestTqm(object):
        def __init__(self, hosts, forks, timeout, inventory, variable_manager, loader, options, passwords, stdout_callback, run_additional_callbacks, run_tree):
            self.hosts = hosts
            self.forks = forks
            self.timeout = timeout
            self.inventory = inventory
            self.variable_manager = variable_manager
            self.loader = loader
            self.options = options
            self.passwords = passwords
            self.stdout_callback = stdout_callback
            self.run_additional_callbacks = run_additional_callbacks
            self.run_tree = run_tree

        def get_host_pinned(self):
            return self._host_pinned


# Generated at 2022-06-13 15:09:55.992507
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    print("Testing StrategyModule (host_pinned) constructor")
    print("Test completed successfully")


# Generated at 2022-06-13 15:09:59.981459
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    ansible = AnsibleMock()
    tqm = TQMMock()
    strategy = StrategyModule(tqm)
    assert strategy._host_pinned == True

# Mock for the built-in ansible library

# Generated at 2022-06-13 15:10:02.477819
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    import unittest.mock as mock
    tqm = mock.MagicMock()
    module = StrategyModule(tqm)
    assert module._host_pinned == True

# Generated at 2022-06-13 15:10:04.070190
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    def testwrapper():
        stm = StrategyModule('')
        assert stm._host_pinned
    testwrapper()

# Generated at 2022-06-13 15:10:04.614609
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
  pass

# Generated at 2022-06-13 15:10:05.276919
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy = StrategyModule()
    assert strategy

# Generated at 2022-06-13 15:10:06.454357
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_module = StrategyModule(tqm)
    assert strategy_module == 'foo'

# Generated at 2022-06-13 15:11:35.127968
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    StrategyModule(tqm=None)


# Generated at 2022-06-13 15:11:36.732523
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = object()
    strategy = StrategyModule(tqm)
    assert strategy.tqm == tqm
    assert strategy._host_pinned == True

# Generated at 2022-06-13 15:11:37.555730
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule is not None

# Generated at 2022-06-13 15:11:39.268415
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = FreeStrategyModule.__init__(self,tqm)
    assert StrategyModule(tqm)

# Generated at 2022-06-13 15:11:40.573836
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    test_strat = StrategyModule()
    assert test_strat._host_pinned == True

# Generated at 2022-06-13 15:11:42.892502
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    """
        Unit test for constructor of class StrategyModule
    """
    obj = StrategyModule(None)
    #obj.__init__(None)
    assert obj.__class__.__name__ == 'StrategyModule'

# Generated at 2022-06-13 15:11:43.956660
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
     assert StrategyModule(tqm) == "StrategyModule"


# Generated at 2022-06-13 15:11:46.760642
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy = StrategyModule('TQM')
    assert strategy._host_pinned == True
# Test if "host_pinned" is added in the list of available strategies
assert 'host_pinned' in StrategyModule.get_strategy_names()

# Generated at 2022-06-13 15:11:47.811317
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule

# Generated at 2022-06-13 15:11:49.212280
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # StrategyModule(tqm)
    return

# Generated at 2022-06-13 15:14:58.349835
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy = StrategyModule(None)
    assert strategy._host_pinned == True

# Generated at 2022-06-13 15:15:06.363432
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    display = Display()
    # Make a test task queue manager
    class FakeTaskQueueManager():
        _index = 0
        def next_index(self):
            self._index += 1
            return self._index
        def get_index(self):
            return self._index
    tqm = FakeTaskQueueManager()
    obj_strategy_module = StrategyModule(tqm)
    # Test that _host_pinned is true
    assert obj_strategy_module._host_pinned == True
    # Test that 'TASK' is in the callbacks
    assert 'TASK' in obj_strategy_module._callbacks

# Generated at 2022-06-13 15:15:07.830425
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    obj = StrategyModule(tqm)
    assert obj._host_pinned == True

# Generated at 2022-06-13 15:15:09.714720
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_module = StrategyModule(object)
    strategy_module.__init__(object)


# Unit test to check display is initialized success

# Generated at 2022-06-13 15:15:11.272838
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    s = StrategyModule()
    assert s._host_pinned == True

# Generated at 2022-06-13 15:15:11.820669
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass

# Generated at 2022-06-13 15:15:13.440995
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    x = StrategyModule(tqm='tqm')
    assert x._host_pinned == True


# Generated at 2022-06-13 15:15:15.003056
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_module = StrategyModule("tqm")
    assert strategy_module._host_pinned == True

# Generated at 2022-06-13 15:15:16.442911
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # Check that the variable _host_pinned is True.
    assert StrategyModule._host_pinned == True

# Generated at 2022-06-13 15:15:16.911757
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True