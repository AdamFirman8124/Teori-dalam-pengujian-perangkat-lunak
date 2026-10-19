

# Generated at 2022-06-13 15:06:26.525954
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
  # Creating an instance of class StrategyModule
    obj = StrategyModule()
    # Checking if the object is an instance of class StrategyModule
    assert isinstance(obj, StrategyModule)

# Generated at 2022-06-13 15:06:26.987583
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True

# Generated at 2022-06-13 15:06:28.600531
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    print("Begin StrategyModule Test")
    str_mod = StrategyModule("tqm")
    print("End StrategyModule Test")

# Generated at 2022-06-13 15:06:30.087696
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass

# Generated at 2022-06-13 15:06:30.624840
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass

# Generated at 2022-06-13 15:06:33.808885
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule.__name__=='StrategyModule'
    import ansible.plugins.loader as pl
    tqm=pl.get('tqm')
    StrategyModule(tqm)._host_pinned==True

# Generated at 2022-06-13 15:06:37.354781
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = ''
    StratMod = StrategyModule(tqm)
    #assert_is_instance(StratMod.display, Display)
    #assert_is_instance(StratMod._tqm, '')
    assert StratMod._host_pinned

# Generated at 2022-06-13 15:06:40.438155
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
  a = FreeStrategyModule(object())
  assert a._host_pinned == False
  b = StrategyModule(object())
  assert b._host_pinned == True

# Generated at 2022-06-13 15:06:40.795702
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule

# Generated at 2022-06-13 15:06:41.932637
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    result = StrategyModule()
    assert result._host_pinned == True

# Generated at 2022-06-13 15:06:45.838023
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    """
    Constructor test
    """
    strategy = StrategyModule(None)
    assert strategy._host_pinned == True

# Generated at 2022-06-13 15:06:46.418648
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    StrategyModule(None)

# Generated at 2022-06-13 15:06:48.176908
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
   strategyModuleTest = StrategyModule()
   assert (strategyModuleTest is not None), "There should be a valid StrategyModule"

# Generated at 2022-06-13 15:06:48.754101
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass

# Generated at 2022-06-13 15:06:49.339015
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass

# Generated at 2022-06-13 15:06:51.044515
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule

if __name__ == "__main__":
    test_StrategyModule()

# Generated at 2022-06-13 15:06:51.906558
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule(1) != None

# Generated at 2022-06-13 15:06:53.245929
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    module = StrategyModule(None)
    assert module._host_pinned == True

# Generated at 2022-06-13 15:06:55.020509
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_module = StrategyModule("tqm")
    assert strategy_module._host_pinned is True

# Generated at 2022-06-13 15:06:56.471873
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategyObject = StrategyModule('tqm')
    assert strategyObject._host_pinned == True

# Generated at 2022-06-13 15:06:59.749089
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    s = StrategyModule('tqm')
    assert s._host_pinned == True
    assert s._sliceable_tasks == True

# Generated at 2022-06-13 15:07:10.680717
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    import json
    import os
    constant_path = os.path.dirname(os.path.abspath(__file__))+'/../../constants/'
    host_vars = json.load(open(constant_path+'all_vars.json'))
    Options = {'connection': 'ssh', 'remote_user': 'root', 'private_key_file': '~/.ssh/id_rsa', 'host_key_checking': False, 'become': False,
               'become_method': 'sudo', 'become_user': 'root', 'verbosity': 0, 'module_lang': 'C', 'timeout': 10}

# Generated at 2022-06-13 15:07:19.171360
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # dummy task queue manager
    class _tqm():
        stats = None
        send_callback = None
        done_callback = None
        queue_callback = None
        run_handlers = None
        run_tasks = None
        variable_manager = None
        inventory = None
        timeout = None
        basedir = None

    tqm = _tqm()
    tm = StrategyModule(tqm)

    assert tm.tqm.stats == tqm.stats
    assert tm.tqm.send_callback == tqm.send_callback
    assert tm.tqm.done_callback == tqm.done_callback
    assert tm.tqm.queue_callback == tqm.queue_callback
    assert tm.tqm.run_handlers == tq

# Generated at 2022-06-13 15:07:24.184470
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    """Generates a mock task queue manager to pass to the StrategyModule constructor.
    Then tests the constructor to ensure it sets the correct initial values
    """
    from mock import Mock
    tqm = Mock()
    test_strategy = StrategyModule(tqm)
    assert test_strategy._host_pinned == True

# Generated at 2022-06-13 15:07:26.307810
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    mock_tqm = MagicMock()
    strategy = StrategyModule(mock_tqm)
    assert strategy._host_pinned

# Generated at 2022-06-13 15:07:36.479410
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy = StrategyModule
    assert strategy.__module__ == 'ansible.plugins.strategy.host_pinned'
    assert strategy.__name__ == 'StrategyModule'

# Generated at 2022-06-13 15:07:37.737298
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule._host_pinned == True



# Generated at 2022-06-13 15:07:38.691956
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule(tqm=None)

# Generated at 2022-06-13 15:07:39.315588
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule(tqm=None)

# Generated at 2022-06-13 15:07:40.236455
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule(tqm=1)

# Generated at 2022-06-13 15:07:56.418865
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    host = 'localhost'
    host_vars = {"ansible_connection": "local"}
    callback_plugins=[]
    display_callback_plugin = None
    connection_cache=None
    variables={}
    loader=None
    variable_manager=None
    stdout_callback=None
    run_additional_callbacks=True
    run_tree=False
    forks=5
    become=False
    become_user=None
    become_method=None
    become_pass=None
    become_exe=None
    become_flags=None
    check=False
    syntax=None
    diff=False
    private_key_file=None
    remote_user=None
    remote_pass=None
    remote_port=None
    specific_host=None
    subset=None
    inventory=None

# Generated at 2022-06-13 15:07:57.762174
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass


# Generated at 2022-06-13 15:07:58.664530
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert callable

# Generated at 2022-06-13 15:08:00.550791
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert type(StrategyModule(None)) == StrategyModule
    assert StrategyModule(None)._host_pinned == True

# Generated at 2022-06-13 15:08:01.904417
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    StrategyModule(tqm)

# Generated at 2022-06-13 15:08:03.272854
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    a = StrategyModule()
    assert a._host_pinned == True

# Generated at 2022-06-13 15:08:06.912181
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    strategy_module = StrategyModule(tqm)
    assert strategy_module._host_pinned == True,"Test constructor of class StrategyModule"

# Generated at 2022-06-13 15:08:08.415289
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy = StrategyModule()
    assert strategy._host_pinned is True


# Generated at 2022-06-13 15:08:09.043960
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule

# Generated at 2022-06-13 15:08:10.837966
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy = StrategyModule(tqm=None)
    assert strategy._host_pinned == True

# Generated at 2022-06-13 15:08:18.451184
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True

# Generated at 2022-06-13 15:08:19.846931
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    TaskQueueManager = object
    obj = StrategyModule(TaskQueueManager)
    assert obj is not None

# Generated at 2022-06-13 15:08:26.613035
# Unit test for constructor of class StrategyModule

# Generated at 2022-06-13 15:08:28.617217
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    StrategyModule.__init__(tqm)

# Generated at 2022-06-13 15:08:30.260306
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    # test with a none
    sm = StrategyModule(tqm)
    assert sm._host_pinned, "didn't get expected value for _host_pinned"

# Generated at 2022-06-13 15:08:32.101923
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert hasattr(StrategyModule, "__init__")


# Generated at 2022-06-13 15:08:33.808832
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    s = StrategyModule(tqm)

# Generated at 2022-06-13 15:08:35.431011
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
  """
  Test constructor of class StrategyModule
  """
  assert StrategyModule(None)._host_pinned

# Generated at 2022-06-13 15:08:35.976096
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    StrategyModule()

# Generated at 2022-06-13 15:08:38.620929
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    obj = StrategyModule(None)
    assert isinstance(obj, StrategyModule)
    assert hasattr(obj, '_host_pinned')

# Generated at 2022-06-13 15:08:55.509121
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = MockTQM()
    strategy_module = StrategyModule(tqm)



# Generated at 2022-06-13 15:08:56.587914
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    StrategyModule(tqm)

# Generated at 2022-06-13 15:09:01.460644
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    import unittest
    import mock
    import ansible.plugins.strategy.host_pinned
    from ansible.plugins.strategy import host_pinned

    class TestHostPinned(unittest.TestCase):
        def test_HostPinned(self):
            ansible.plugins.strategy.host_pinned.display = mock.MagicMock()
            strategy_module = host_pinned.StrategyModule(mock.MagicMock())
            self.assertTrue(strategy_module._host_pinned)

    unittest.main()

# Generated at 2022-06-13 15:09:02.849879
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy = StrategyModule(tqm=None)
    assert strategy._host_pinned

# Generated at 2022-06-13 15:09:04.023309
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy = StrategyModule(tqm)
    assert strategy._host_pinned

# Generated at 2022-06-13 15:09:05.141164
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
   strategic_module = StrategyModule([])
   assert strategic_module._host_pinned == True

# Generated at 2022-06-13 15:09:12.430609
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.plugins.strategy.host_pinned import StrategyModule
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.inventory.host import Host
    options = lambda x: None
    options.module_path = None
    options.connection = 'ssh'
    options.forks = 100
    options.remote_user = 'root'
    options.private_key_file = None
    options.ssh_common_args = None
    options.ssh_extra_args = None
    options.sftp_extra_args = None
    options.scp_extra

# Generated at 2022-06-13 15:09:13.005926
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True

# Generated at 2022-06-13 15:09:13.881895
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule.__init__ is not None

# Generated at 2022-06-13 15:09:15.273605
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = {}
    strategy = StrategyModule(tqm)
    assert strategy._host_pinned is True

# Generated at 2022-06-13 15:09:56.735397
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule(0)._host_pinned

# Generated at 2022-06-13 15:10:02.988534
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    class TestClass(StrategyModule):
        def __init__(self, tqm):
            super(StrategyModule, self).__init__(tqm)
    print(StrategyModule)
    print(TestClass)
    obj = TestClass('tqm')
    print(obj)
# Unit testing for execution of module.
# Run this script to execute these test.
# 'python3 test_host_pinned.py'

# Generated at 2022-06-13 15:10:03.901928
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule(tqm) == None

# Generated at 2022-06-13 15:10:05.733853
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    import ansible.plugins.strategy.host_pinned as host_pinned
    strategy = host_pinned.StrategyModule
    assert strategy

# Generated at 2022-06-13 15:10:08.170982
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule.__doc__ == '''Executes tasks on each host without interruption'''
    assert StrategyModule.__init__.__doc__ == '''initialization of hosts'''
    assert StrategyModule.run.__doc__ == '''executes task list'''

# Generated at 2022-06-13 15:10:09.346466
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy = StrategyModule(tqm=None)
    assert strategy._host_pinned == True

# Generated at 2022-06-13 15:10:11.093059
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # Test that constructors are called
    strategy = StrategyModule("tqm")
    assert strategy._host_pinned == True
    assert strategy._display.verbosity == 3


# Generated at 2022-06-13 15:10:13.122076
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = StrategyModule('tqm')
    assert(tqm._host_pinned == True)

# Generated at 2022-06-13 15:10:18.404005
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert len(StrategyModule.__bases__) == 1
    assert StrategyModule.__bases__[0].__name__ == 'FreeStrategyModule'
    assert callable(StrategyModule)

# Generated at 2022-06-13 15:10:21.621111
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    """ Create object of StrategyModule class and check it's inheritance
    """
    tqm = True
    strategy = StrategyModule(tqm)
    assert isinstance(strategy, FreeStrategyModule)
    assert strategy._host_pinned


# Generated at 2022-06-13 15:11:52.801324
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True



# Generated at 2022-06-13 15:11:53.987611
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass

# ======
#  MAIN
# ======


# Generated at 2022-06-13 15:11:54.757444
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    s=StrategyModule(tqm)

# Generated at 2022-06-13 15:11:57.106163
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    display = Display()
    assert display.verbosity == 2

    tqm = 'tqm'
    sw = StrategyModule(tqm)
    assert sw.tqm == 'tqm'

# Generated at 2022-06-13 15:12:03.882559
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.plugins.strategy import StrategyModule
    from ansible.plugins.strategy import pinned_hosts
    from ansible.plugins.strategy import free_hosts
    test_args = {'tqm': pinned_hosts}
    pinned_strategy = StrategyModule(**test_args)
    assert isinstance(pinned_strategy, StrategyModule)
    assert pinned_strategy._host_pinned is True
    assert pinned_strategy._host_free is False
    assert pinned_strategy._host_workers is None
    assert pinned_strategy.run() == 'pinned_hosts'
    test_args = {'tqm': free_hosts}
    free_strategy = StrategyModule(**test_args)
    assert isinstance(free_strategy, StrategyModule)
    assert free_str

# Generated at 2022-06-13 15:12:04.836001
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule(None) is not None

# Generated at 2022-06-13 15:12:05.790178
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule is not None

# Generated at 2022-06-13 15:12:08.946003
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy = StrategyModule(1)
    print(strategy._host_pinned)
    assert strategy._host_pinned == True

# Generated at 2022-06-13 15:12:09.608366
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    StrategyModule(None)

# Generated at 2022-06-13 15:12:12.953147
# Unit test for constructor of class StrategyModule
def test_StrategyModule():

  import ansible.plugins.strategy.host_pinned
  tqm = ansible.plugins.strategy.host_pinned.StrategyModule(None)

  assert tqm._host_pinned == True

# Generated at 2022-06-13 15:15:19.728556
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = 'abc'
    obj = StrategyModule(tqm)
    assert obj is not None

# Generated at 2022-06-13 15:15:21.168986
# Unit test for constructor of class StrategyModule
def test_StrategyModule():

    tqm = mock.Mock()
    strategy = StrategyModule()

    assert strategy is not None

# Generated at 2022-06-13 15:15:23.877510
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
      tqm = object()
      StrategyModule(tqm)

# Generated at 2022-06-13 15:15:25.354118
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule


# Generated at 2022-06-13 15:15:27.806870
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True

# code to execute if this script is called directly
if __name__ == '__main__':
    # In case someone runs this as a script, print out some information
    print('This is the free Module class')

# Generated at 2022-06-13 15:15:29.779753
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_module = StrategyModule("tqm")
    assert strategy_module._host_pinned == True

# Generated at 2022-06-13 15:15:31.997035
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
   strategy = StrategyModule(tqm=None)
   assert strategy.get_host_pinned()

# Generated at 2022-06-13 15:15:32.657523
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy = StrategyModule(tqm=None)
    assert strategy._host_pinned

# Generated at 2022-06-13 15:15:34.568877
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    task_queue_manager= None
    m = StrategyModule(task_queue_manager)
    assert isinstance(m,StrategyModule)

# Generated at 2022-06-13 15:15:35.342680
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule.__init__