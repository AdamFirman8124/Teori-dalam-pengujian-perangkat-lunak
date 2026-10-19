

# Generated at 2022-06-13 15:06:32.887129
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    import random
    import string
    st = StrategyModule(random.choice(string.ascii_lowercase))
    assert st._host_pinned == True
    st._host_pinned = False
    assert st._host_pinned == False

# Generated at 2022-06-13 15:06:35.163770
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_module = StrategyModule(FakeTQM())
    assert strategy_module._host_pinned == True

# Unit test setup


# Generated at 2022-06-13 15:06:36.471415
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    StrategyModule(tqm="host_pinned")


# Generated at 2022-06-13 15:06:37.874706
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    module = StrategyModule()
    assert module._host_pinned == True

# Generated at 2022-06-13 15:06:39.813483
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    TQM = 'test_tqm'
    strategy = StrategyModule(TQM)
    assert strategy._host_pinned == True

# Generated at 2022-06-13 15:06:41.742703
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategyModule = StrategyModule(tqm=None)
    
    assert strategyModule._host_pinned == True



# Generated at 2022-06-13 15:06:42.576471
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule(None) is not None

# Generated at 2022-06-13 15:06:43.631720
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    t = StrategyModule('test')
    assert 'test' == t

# Generated at 2022-06-13 15:06:47.391181
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.executor.task_queue_manager import TaskQueueManager
    tqm = TaskQueueManager(None, None)

    sm = StrategyModule(tqm)

    assert sm._host_pinned == True


# Generated at 2022-06-13 15:06:49.828622
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule.name == 'host_pinned'

    # Check that the strategy name is correctly set in the super class constructor
    assert FreeStrategyModule.name == 'host_pinned'

# Generated at 2022-06-13 15:06:52.041295
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_module = StrategyModule(tqm = None)
    assert strategy_module._host_pinned

# Generated at 2022-06-13 15:06:53.924825
# Unit test for constructor of class StrategyModule
def test_StrategyModule():

    strategy_module = StrategyModule (None)
    assert isinstance(strategy_module, FreeStrategyModule)


# Generated at 2022-06-13 15:07:00.658366
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.playbook.task import Task
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.inventory.inventory import Inventory
    from ansible.plugins.loader import action_loader
    from ansible.vars.manager import VariableManager
    from ansible.executor import task_queue_manager
    inventory = Inventory(loader=None, variable_manager=VariableManager(), host_list=[])
    strategy = task_queue_manager.get_strategy(inventory, 'host_pinned')
    assert strategy._host_pinned == True

# Generated at 2022-06-13 15:07:02.310419
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
   strategy_module = StrategyModule("tqm")
   assert strategy_module != None

# Generated at 2022-06-13 15:07:02.906380
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    a = StrategyModule(tqm=None)
    a._host_pinned = True

# Generated at 2022-06-13 15:07:04.668399
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    a = StrategyModule(tqm)
    assert a._host_pinned == True

# Generated at 2022-06-13 15:07:13.196666
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule.__name__ == 'StrategyModule'

# Generated at 2022-06-13 15:07:13.916863
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass

# Generated at 2022-06-13 15:07:16.138961
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    class _tqm:
        def __init__(self):
            pass

    sut = StrategyModule(_tqm())

    assert True == sut._host_pinned

# Generated at 2022-06-13 15:07:27.298091
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule.__name__ == 'StrategyModule'

# Generated at 2022-06-13 15:07:32.427356
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_module = StrategyModule('tqm')
    assert strategy_module is not None
    assert strategy_module.get_host_pinned() is True
    assert strategy_module._host_pinned is True

# Generated at 2022-06-13 15:07:33.099077
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
  pass

# Generated at 2022-06-13 15:07:33.669186
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule

# Generated at 2022-06-13 15:07:34.044450
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule

# Generated at 2022-06-13 15:07:35.716589
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = ''
    strategy = StrategyModule(tqm)
    assert strategy is not None

# Generated at 2022-06-13 15:07:44.187307
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    import unittest
    from units.mock.loader import DictDataLoader
    from units.mock.inventory import MockInventory
    from ansible.vars.manager import VariableManager
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.task_result import TaskResult
    from ansible.executor.play_iterator import PlayIterator

    import ansible.constants as C
    # This instantiates our ResultCallback for processing the results of tasks
    results_callback = ResultCallback()

    class PlaybookExecutorTestCase(unittest.TestCase):
        def setUp(self):
            pass

        def tearDown(self):
            pass

        def test_constructor(self):
            loader = DictDataLoader

# Generated at 2022-06-13 15:07:45.207697
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    sm = StrategyModule("tqm")
    assert sm._host_pinned == True

# Generated at 2022-06-13 15:07:47.421732
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = 'tqm'
    assert StrategyModule(tqm)._host_pinned

# Generated at 2022-06-13 15:07:50.796018
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = {'one':1,'two':2}
    strategyModule = StrategyModule(tqm)
    print(strategyModule._host_pinned)

test_StrategyModule()

# Generated at 2022-06-13 15:07:53.152387
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy = StrategyModule(tqm='test')
    strategy_str = str(strategy)
    assert "StrategyModule()" in strategy_str

# Generated at 2022-06-13 15:08:01.312300
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.plugins.strategy.host_pinned import StrategyModule
    strategy = StrategyModule('TEST')
    assert strategy._host_pinned == True
    assert strategy._tqm == 'TEST'


# Generated at 2022-06-13 15:08:03.383546
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = 'test_tqm'
    strategy = StrategyModule(tqm)

    assert(strategy._host_pinned == True)

# Generated at 2022-06-13 15:08:06.451740
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    _tqm = MagicMock()
    strategy_module = StrategyModule(_tqm)
    assert strategy_module._host_pinned == True

# Generated at 2022-06-13 15:08:13.111812
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    sample_playbook = None
    sample_inventory = None
    sample_variable_manager = None
    sample_loader = None
    sample_options = None
    sample_tqm = None
    # Make a new instance of StrategyModule with the above variables
    sm = StrategyModule(sample_tqm)
    # Assert Truthy value
    assert sm
    # Assert True value
    assert sm._host_pinned == True

# Generated at 2022-06-13 15:08:16.145951
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_module = StrategyModule(None)
    assert strategy_module is not None
    assert strategy_module.get_name() == 'host_pinned'
    assert strategy_module._host_pinned is True


# Generated at 2022-06-13 15:08:23.268894
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    import time
    import json
    import os
    import sys
    from collections import namedtuple
    from ansible.plugins.strategy.host_pinned import StrategyModule
    from ansible.utils.display import Display
    from ansible.executor.task_queue_manager import TaskQueueManager

    display = Display()

# Generated at 2022-06-13 15:08:25.402180
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    strategy = StrategyModule(tqm)
    assert strategy is not None

# Generated at 2022-06-13 15:08:28.241861
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    mod_name = __name__
    mod = __import__(mod_name)
    StrategyModule()


# Generated at 2022-06-13 15:08:39.752256
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule.__name__ == 'StrategyModule'
    assert StrategyModule.__module__ == 'ansible.plugins.strategy'
    assert hasattr(StrategyModule, '_host_pinned')
    assert hasattr(StrategyModule, '__init__')
    assert callable(StrategyModule.__init__)
    assert hasattr(StrategyModule, 'display')
    assert StrategyModule.display == Display()
    assert hasattr(StrategyModule, 'run')
    assert callable(StrategyModule.run)
    assert hasattr(StrategyModule, 'get_next_task_lock')
    assert callable(StrategyModule.get_next_task_lock)
    assert hasattr(StrategyModule, '_wait_on_pending_results')

# Generated at 2022-06-13 15:08:40.330091
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    return True

# Generated at 2022-06-13 15:08:51.020712
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    print("Testing StrategyModule")
    print("Testing StrategyModule constructor")
    strategy = StrategyModule()
    assert strategy 
    print("Testing StrategyModule constructor....PASSED")

# Generated at 2022-06-13 15:08:51.880078
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    StrategyModule('tqm')

# Generated at 2022-06-13 15:08:53.653433
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.plugins.strategy import StrategyBase
    tqm = StrategyBase()
    assert StrategyModule(tqm)._host_pinned

# Generated at 2022-06-13 15:08:55.366776
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
  tqm = None
  sm = StrategyModule(tqm)

# Generated at 2022-06-13 15:08:57.625147
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    global display
    global StrategyModule
    display = Display()
    assert type(display) is Display
    StrategyModule = StrategyModule(display)
    assert type(StrategyModule) is StrategyModule

# Generated at 2022-06-13 15:08:58.910356
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_obj = StrategyModule(tqm=None)
    assert strategy_obj is not None

# Generated at 2022-06-13 15:09:06.531990
# Unit test for constructor of class StrategyModule
def test_StrategyModule():

    from queue import Queue
    from ansible.plugins.strategy import add_tqm_attribute
    from ansible.executor.task_queue_manager import TaskQueueManager

    display.display("test_StrategyModule", color='green')

    tqm = TaskQueueManager(
        inventory=None,
        variable_manager=None,
        loader=None,
        options=None,
        passwords=None,
        stdout_callback=None,
    )
    tqm._final_q = Queue()
    add_tqm_attribute(tqm)

    obj = StrategyModule(tqm)

    assert obj is not None
    assert obj._host_pinned is not None

# Generated at 2022-06-13 15:09:07.807553
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy = StrategyModule(None)
    assert True == strategy._host_pinned

# Generated at 2022-06-13 15:09:09.244970
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_module = StrategyModule(tqm = None)
    assert strategy_module._host_pinned == True

# Generated at 2022-06-13 15:09:10.022030
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass


# Generated at 2022-06-13 15:09:32.305436
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    display = Display()
    assert StrategyModule(display)

# Generated at 2022-06-13 15:09:32.753504
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass

# Generated at 2022-06-13 15:09:33.486432
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule.__init__

# Generated at 2022-06-13 15:09:34.666959
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule(tqm=None).__init__(tqm=None) == None

# Generated at 2022-06-13 15:09:37.242380
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    s = StrategyModule("tqm")
    print(s._host_pinned)


# Generated at 2022-06-13 15:09:39.471001
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # Testing __init__(tqm)
    strategy_module = StrategyModule(tqm)
    assert(strategy_module)

# Generated at 2022-06-13 15:09:40.983355
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    host_pinned = StrategyModule()
    assert host_pinned._host_pinned is True

# Generated at 2022-06-13 15:09:44.135541
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    #
    # Test1
    #
    print("Testing StrategyModule")
    assert True == True
    #
    # Test2
    #
    print("Testing StrategyModule")
    assert True == True

# Generated at 2022-06-13 15:09:45.507877
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = {}
    sm = StrategyModule(tqm)
    assert sm._host_pinned



# Generated at 2022-06-13 15:09:47.567497
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
   # This test will fail if there is any exception
   # In the constructor of the class
   strategy = StrategyModule(None)

# Generated at 2022-06-13 15:10:25.246626
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_module = StrategyModule(None)
    assert strategy_module._host_pinned == True

# Generated at 2022-06-13 15:10:26.376283
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True

# Generated at 2022-06-13 15:10:27.619221
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy = StrategyModule('')
    assert strategy._host_pinned


# Generated at 2022-06-13 15:10:28.628031
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule(None) is not None

# Generated at 2022-06-13 15:10:29.791977
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = mock.Mock()
    StrategyModule(tqm)

# Generated at 2022-06-13 15:10:32.440251
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    ''' The constructor of class StrategyModule '''

    # Create an instance of class StrategyModule
    strategy = StrategyModule(tqm)

    # Check that the constructed object has the properties required by
    # the class
    assert hasattr(strategy, 'display')

# Generated at 2022-06-13 15:10:36.272853
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
   # Unit test setup
   tqm = _task_queue_manager()

   # Execute strategy module constructor
   strategy_module = StrategyModule(tqm)

   # Assert strategy is of type 'free'
   assert strategy_module.__class__.__name__ == 'StrategyModule'

   # Assert hosts are pinned
   assert strategy_module._host_pinned == True


# Generated at 2022-06-13 15:10:37.414839
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True
#    assert host_pinned

# Generated at 2022-06-13 15:10:38.086349
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass

# Generated at 2022-06-13 15:10:46.806644
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.plugins.strategy.host_pinned import StrategyModule
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible_collections.nsbl.collab.plugins.module_utils.array import array

    play_context = PlayContext()
    task_queue_manager = TaskQueueManager(
      inventory=array(['all']),
      variable_manager=array(),
      loader=array(),
      options=array(),
      passwords=array(),
      stdout_callback=array(),
      run_additional_callbacks=array(),
      run_tree=array(False),
      timeout=array(10),
      play=array()
    )
    strategy_module = StrategyModule(task_queue_manager)

# Generated at 2022-06-13 15:12:31.572642
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.plugins.strategy.host_pinned import StrategyModule
    ansible_obj = Mock()
    class Obj(object):
        def __init__(self):
            self.host_pinned = True
    ansible_obj.display = Obj()
    t = Mock()
    s = StrategyModule(t)
    assert type(s) == StrategyModule
    #assert type(ansible_obj.display) == Obj
    #assert s._tqm == t



# Generated at 2022-06-13 15:12:33.274562
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = FreeStrategyModule()
    assert isinstance(tqm, FreeStrategyModule)

# Generated at 2022-06-13 15:12:35.356619
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    """Test if the constructor of StrategyModule is working properly"""
    module = StrategyModule(None)

    assert True == module._host_pinned

# Generated at 2022-06-13 15:12:37.214031
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    StrategyModule(tqm=tqm)

# Generated at 2022-06-13 15:12:38.430786
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule(None) != None


# Generated at 2022-06-13 15:12:48.168189
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.plugins.strategy.host_pinned import StrategyModule
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    import json
    import os
    import ansible.constants as C

    # TODO: create test inventory
    inventory = InventoryManager(loader=DataLoader(), sources='localhost,')
    variable_manager = VariableManager(loader=DataLoader(), inventory=inventory)

    playbook_path = 'test.yml'
    if not os.path.exists(playbook_path):
        print('[INFO] The playbook does not exist')
        sys.exit()


# Generated at 2022-06-13 15:12:49.179550
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    x = StrategyModule(True)
    assert x._display == Display()

# Generated at 2022-06-13 15:12:50.369064
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
  p = StrategyModule(None)
  assert p._host_pinned == True

# Generated at 2022-06-13 15:12:51.123863
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert(StrategyModule)

# Generated at 2022-06-13 15:12:51.627074
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass

# Generated at 2022-06-13 15:16:10.187290
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule.__bases__ == (FreeStrategyModule,)
#    assert StrategyModule.__doc__ == 'Default ansible StrategyModule'
    assert StrategyModule._host_pinned == True
#    assert type(StrategyModule._display) == Display
    
test_StrategyModule()

# Generated at 2022-06-13 15:16:11.062117
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass

# Generated at 2022-06-13 15:16:11.567218
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    StrategyModule(3)

# Generated at 2022-06-13 15:16:14.832807
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert issubclass(StrategyModule, FreeStrategyModule)
    strategy_module = StrategyModule(tqm='tqm_variable')
    assert strategy_module is not None


# Generated at 2022-06-13 15:16:16.298301
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = []
    strategy = StrategyModule(tqm)
    assert strategy._host_pinned == True

# Generated at 2022-06-13 15:16:18.749524
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = "local"
    strategy_obj = StrategyModule(tqm)
    assert strategy_obj
    assert strategy_obj._host_pinned == True

# Generated at 2022-06-13 15:16:19.270173
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass

# Generated at 2022-06-13 15:16:20.106354
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    m = StrategyModule()
    assert m

# Generated at 2022-06-13 15:16:20.619155
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True

# Generated at 2022-06-13 15:16:27.926400
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    print('\nChiamata a StrategyModule')
    print('SETUP')

    #-------------------------------------------------------------
    #        TEST: strategy_module_init
    #-------------------------------------------------------------
    #         from collections import namedtuple
    #         from ansible.plugins.strategy import StrategyBase
    #         from ansible.executor.task_queue_manager import TaskQueueManager
    #         from ansible.inventory.host import Host
    #         from ansible.inventory.group import Group
    #         from ansible.vars.manager import VariableManager
    #
    #         StrategyBase = namedtuple('StrategyBase', ['get_hosts_left'])
    #         StrategyBase.__str__ = lambda x: 'name'
    #
    #         # Test object initialization
    #         host_pinned_obj = StrategyModule(TaskQueueManager())