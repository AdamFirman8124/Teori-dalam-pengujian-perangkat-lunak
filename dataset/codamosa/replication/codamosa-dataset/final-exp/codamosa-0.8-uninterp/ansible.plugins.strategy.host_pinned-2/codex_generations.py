

# Generated at 2022-06-13 15:06:30.411772
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    print("Testing creation of StrategyModule object")
    strategy_module_obj = StrategyModule(tqm = "tqm")
    assert strategy_module_obj._host_pinned == True

# Generated at 2022-06-13 15:06:31.727424
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    sm = StrategyModule(None)
    assert sm._host_pinned



# Generated at 2022-06-13 15:06:34.343497
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    import ansible.plugins.strategy.host_pinned
    a = ansible.plugins.strategy.host_pinned.StrategyModule()
    assert a._host_pinned == True

# Generated at 2022-06-13 15:06:35.557322
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    s = StrategyModule(tqm=None)
    assert s._host_pinned

# Generated at 2022-06-13 15:06:37.353497
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    q = StrategyModule(tqm='tqm')
    assert q._host_pinned==True

# Generated at 2022-06-13 15:06:37.916639
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True

# Generated at 2022-06-13 15:06:38.890921
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    StrategyModule(tqm=None)

# Generated at 2022-06-13 15:06:40.053126
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule("tqm") is not None


# Generated at 2022-06-13 15:06:41.707045
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # TODO : Complete this unit test
    return True
# ---------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------

# Generated at 2022-06-13 15:06:42.229508
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True

# Generated at 2022-06-13 15:06:45.647952
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule(None) is not None
    import ansible.plugins.strategy.host_pinned
    obj = ansible.plugins.strategy.host_pinned.StrategyModule(None)
    assert obj is not None

# Generated at 2022-06-13 15:06:48.127967
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    strategy_module = StrategyModule(tqm)
    assert strategy_module._host_pinned == True

# Generated at 2022-06-13 15:06:57.187494
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.config import defaults
    from ansible.executor.task_queue_manager import TaskQueueManager

    from ansible.utils import plugin_docs
    import os
    import sys

    sys.argv = ["ansible-playbook", "test.yml", "-i", "test/inventory", '--connection=local']
    os.environ['ANSIBLE_CONFIG'] = os.devnull
    plugin_docs._find_plugins(display)


# Generated at 2022-06-13 15:07:00.996856
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
   host = { "ip": "192.168.10.1" }
   tqm = { "host": host }
   strategy = StrategyModule(tqm)
   assert strategy != None
   assert strategy._host_pinned

# Generated at 2022-06-13 15:07:03.945149
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # Instantiating StrategyModule class
    module = StrategyModule(tqm)
    assert module._host_pinned

# Generated at 2022-06-13 15:07:05.459232
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = ''
    assert StrategyModule(tqm)._host_pinned

# Generated at 2022-06-13 15:07:13.946574
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # Set up a tqm object to test with.
    from threading import Thread
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.utils.vars import load_extra_vars
    from ansible.utils.vars import load_options_vars
    from ansible.vars.manager import VariableManager


# Generated at 2022-06-13 15:07:15.571793
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    mod = StrategyModule(1)
    assert mod._host_pinned == True


# Generated at 2022-06-13 15:07:20.729916
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = {}
    strategy_obj = StrategyModule(tqm)
    print(strategy_obj._host_pinned)
    assert strategy_obj._host_pinned == True, "The function returns a wrong information"

if __name__ == "__main__":
    test_StrategyModule()

# Generated at 2022-06-13 15:07:24.859200
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # Testing constructor class StrategyModule
    from ansible.plugins.strategy.host_pinned import display

    StrategyModule(tqm=display)


if __name__ == '__main__':
    # Unit test
    configure_logging()
    test_StrategyModule()

# Generated at 2022-06-13 15:07:36.591668
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule.__bases__[0].__name__ == 'FreeStrategyModule'

# Generated at 2022-06-13 15:07:38.577168
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    test_strategy_module = StrategyModule(tqm)
    assert test_strategy_module is not None



# Generated at 2022-06-13 15:07:40.150674
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    StrategyModule(None)
    display.display("Test default constructor")

# Unit test to check value with no args passed

# Generated at 2022-06-13 15:07:41.645439
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # Create instance of class StrategyModule
    strategy_instance = StrategyModule('tqm')
    assert strategy_instance != None

# Generated at 2022-06-13 15:07:42.142849
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True == True

# Generated at 2022-06-13 15:07:43.183310
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    """
    Test function for module StrategyModule
    """
    pass

# Generated at 2022-06-13 15:07:52.192757
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    """
    This function is used to test the constructor of the class StrategyModule
    """

    import ansible.plugins.strategy.host_pinned
    from ansible.utils.display import Display
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.inventory.host import Host
    from ansible.parsing.dataloader import DataLoader

    strategy = ansible.plugins.strategy.host_pinned.StrategyModule(TaskQueueManager())
    assert(isinstance(strategy, Host))

# Generated at 2022-06-13 15:07:54.938236
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    module = StrategyModule(None)
    assert module is not None
    assert module._host_pinned is True


# Generated at 2022-06-13 15:07:55.938392
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    StrategyModule("test_tqm")

# Generated at 2022-06-13 15:07:56.638588
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass

# Generated at 2022-06-13 15:08:02.102156
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = dummy()
    StrategyModule(tqm)


# Generated at 2022-06-13 15:08:03.463775
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert hasattr(StrategyModule, '__init__')


# Generated at 2022-06-13 15:08:05.350330
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule is not None

# Generated at 2022-06-13 15:08:16.070909
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    obj = StrategyModule(tqm="tqm")
    assert(obj._host_pinned==True)
    assert(obj._display==Display())
    assert(obj._tqm=="tqm")
    assert(obj._inventory=="tqm.inventory")
    assert(obj._variable_manager=="tqm.variable_manager")
    assert(obj._loader=="tqm.loader")
    assert(obj._options=="tqm.options")
    assert(obj._stdout_callback=="tqm._stdout_callback")
    assert(obj._run_handlers=="tqm.run_handlers")
    assert(obj._run_tasks=="tqm.run_tasks")

# Generated at 2022-06-13 15:08:17.267105
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = object()
    StrategyModule(tqm)

# Generated at 2022-06-13 15:08:18.084362
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule.__name__ == 'StrategyModule'

# Generated at 2022-06-13 15:08:21.183155
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.plugins.strategy.host_pinned import StrategyModule
    assert issubclass(StrategyModule, FreeStrategyModule)
    strategymod = StrategyModule()
    assert isinstance(strategymod._host_pinned, bool)
    assert strategymod._host_pinned

# Generated at 2022-06-13 15:08:21.641636
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass

# Generated at 2022-06-13 15:08:22.065123
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True

# Generated at 2022-06-13 15:08:24.334261
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    """Unit test for constructor of class StrategyModule"""
    StrategyModule()

# Generated at 2022-06-13 15:08:34.054335
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    st = StrategyModule(tqm)
    assert st._host_pinned == True

# Generated at 2022-06-13 15:08:36.016332
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = object()
    strategy = StrategyModule(tqm)
    assert hasattr(strategy, '_host_pinned')

# Generated at 2022-06-13 15:08:37.692052
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    a = StrategyModule()
    assert a._host_pinned == True, 'StrategyModule: Test for constructor failed'

# Generated at 2022-06-13 15:08:39.380279
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    print (StrategyModule)

# Generated at 2022-06-13 15:08:40.008184
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass

# Generated at 2022-06-13 15:08:40.600097
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True

# Generated at 2022-06-13 15:08:41.832246
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
        strategy_module = StrategyModule(None)
        assert strategy_module is not None

# Generated at 2022-06-13 15:08:43.713553
# Unit test for constructor of class StrategyModule
def test_StrategyModule():

    strategy_module = StrategyModule('tqm')

    assert strategy_module._host_pinned == True

# Generated at 2022-06-13 15:08:44.253085
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule

# Generated at 2022-06-13 15:08:46.868037
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert isinstance(object.__new__(StrategyModule), FreeStrategyModule)

# Generated at 2022-06-13 15:09:07.076242
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.plugins.strategy.host_pinned import StrategyModule as HPStrategyModule
    from ansible.plugins.strategy import StrategyBase
    hpstrategy = HPStrategyModule(None)
    assert issubclass(HPStrategyModule, StrategyBase)
    assert isinstance(hpstrategy, StrategyBase)
    assert isinstance(hpstrategy, HPStrategyModule)
    assert hpstrategy._host_pinned

# Generated at 2022-06-13 15:09:10.387223
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    _tqm = ['StrategyModule', 'tqm'] #TODO
    test_StrategyModule = StrategyModule(_tqm)
    assert(test_StrategyModule.tqm == _tqm)
    assert(test_StrategyModule._host_pinned == True)

# Generated at 2022-06-13 15:09:18.024480
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.executor.task_queue_manager import TaskQueueManager
    tqm = TaskQueueManager('1', '2', '3', '4', '5')
    strategy_module = StrategyModule(tqm)
    assert strategy_module._host_pinned == True

# Test for class StrategyModule
# def test_StrategyModule():
#     from ansible.executor.task_queue_manager import TaskQueueManager
#     tqm = TaskQueueManager('1', '2', '3', '4', '5')
#     strategy_module = StrategyModule(tqm)
#     assert strategy_module.get_host_list() == ['1', '2', '3', '4', '5']

# Generated at 2022-06-13 15:09:20.324270
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    t = FreeStrategyModule()
    assert t._host_pinned is True, "_host_pinned should be True"

# Generated at 2022-06-13 15:09:22.474049
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert isinstance(StrategyModule, FreeStrategyModule), "It's not StrategyModule"


# Generated at 2022-06-13 15:09:26.028275
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    print("Running unit test for StrategyModule class constructor")
    obj = StrategyModule("tqm_obj")
    if obj is not None:
        print("Successfully instantiated StrategyModule class")
    else:
        print("Failed to instantiate StrategyModule class")


# Generated at 2022-06-13 15:09:28.932797
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_module = StrategyModule("test_tqm")
    display.display("test_tqm")
    assert strategy_module._host_pinned
    assert strategy_module._tqm == "test_tqm"

# Generated at 2022-06-13 15:09:35.677839
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    t = test_tqm = 1
    strategy = StrategyModule(t)
    assert strategy._tqm == t
    assert strategy._display == display
    assert strategy._watcher is None
    assert strategy._inventory
    assert strategy._variables
    assert strategy._loader
    assert strategy._shared_loader_obj
    assert strategy._play_context
    assert strategy._all_vars
    assert strategy._templar
    assert strategy._fail_queue
    assert strategy._new_stdin is sys.stdin
    assert strategy._runners
    assert strategy._host_pinned is True
    assert strategy._final_q
    assert strategy._last_hosts
    assert strategy._show_custom_stats
    assert strategy._host_name_map
    assert strategy._hit_counter is 0
    assert strategy._host_pinned_count is 0

# Generated at 2022-06-13 15:09:39.202376
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    module = StrategyModule(None)
    assert module is not None
    assert module._host_pinned == True
    assert module._tqm is None

# Unit test to check the minimum version of Ansible required

# Generated at 2022-06-13 15:09:40.008088
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass


# Generated at 2022-06-13 15:10:19.282116
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = object()
    s = StrategyModule(tqm)
    assert s._host_pinned



# Generated at 2022-06-13 15:10:21.028618
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    obj = StrategyModule(tqm=None)
    assert obj._host_pinned == True

# Generated at 2022-06-13 15:10:21.761954
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True

# Generated at 2022-06-13 15:10:23.067973
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_module = StrategyModule(None)
    assert strategy_module._host_pinned == True
    assert strategy_module.get_host_list(None) == None

# Generated at 2022-06-13 15:10:24.788640
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.plugins.strategy.host_pinned import StrategyModule
    tqm = TaskQueueManager()
    strategy = StrategyModule(tqm)
    assert strategy._host_pinned == True

# Generated at 2022-06-13 15:10:26.333537
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule.__init__.__doc__

# Generated at 2022-06-13 15:10:28.707839
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.plugins.strategy.free import StrategyModule as FreeStrategyModule
    print("test for StrategyModule")
    FreeStrategyModule()


# Generated at 2022-06-13 15:10:30.820277
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategymodule_object = StrategyModule("tqm")
    assert strategymodule_object._task_queue_manager == "tqm"
    assert strategymodule_object._host_pinned

# Generated at 2022-06-13 15:10:31.921624
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule(tqm=None)._host_pinned == True

# Generated at 2022-06-13 15:10:32.351713
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass

# Generated at 2022-06-13 15:12:13.925781
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    ans_obj = None
    obj = StrategyModule(ans_obj)
    assert obj is not None

# Generated at 2022-06-13 15:12:14.459476
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass

# Generated at 2022-06-13 15:12:25.592654
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from unit.mock.loader import DictDataLoader
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.playbook import Playbook
    from collections import namedtuple

    variable_manager = VariableManager()
    loader = DictDataLoader({})

    inventory = Inventory(loader=loader, variable_manager=variable_manager, host_list=['localhost'])
    variable_manager.set_inventory(inventory)


# Generated at 2022-06-13 15:12:27.390663
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    module = StrategyModule('test')
    assert(module.get_host_pinned() == True)

# Generated at 2022-06-13 15:12:28.516495
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule.__init__(StrategyModule)

# Generated at 2022-06-13 15:12:29.061374
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule

# Generated at 2022-06-13 15:12:30.287290
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    strat = StrategyModule(tqm)
    assert (strat._host_pinned)

# Generated at 2022-06-13 15:12:32.437316
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    print("In strategy_host_pinned unit test")
    obj = StrategyModule(tqm="tqm")
    assert obj._host_pinned == True

# Generated at 2022-06-13 15:12:34.085937
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert issubclass(StrategyModule, FreeStrategyModule) == True

# test that the strategy key exists

# Generated at 2022-06-13 15:12:35.850149
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy = StrategyModule("test")
    assert strategy._host_pinned is True

# Generated at 2022-06-13 15:15:50.177819
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    class Tqm():
        def __init__(self):
            self.hostvars = {}

    tqm = Tqm()
    strategy_module = StrategyModule(tqm)
    isinstance(strategy_module, StrategyModule)

# Generated at 2022-06-13 15:15:51.989794
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    strategyModule = StrategyModule(tqm)
    assert strategyModule is not None
    assert strategyModule._host_pinned

# Generated at 2022-06-13 15:15:54.086488
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    '''Unit test for constructor of class StrategyModule'''

    strategy_module_obj = StrategyModule('tqm')
    assert True == strategy_module_obj._host_pinned

# Generated at 2022-06-13 15:15:56.070135
# Unit test for constructor of class StrategyModule
def test_StrategyModule():

    # Create a strategy object
    strategy_obj = StrategyModule()

    # Assert various arguments of strategy_obj
    assert strategy_obj._host_pinned == True

# Generated at 2022-06-13 15:15:56.526023
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule

# Generated at 2022-06-13 15:15:57.749419
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    module = StrategyModule(None)
    assert module._host_pinned == True


# Generated at 2022-06-13 15:15:58.677660
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    s = StrategyModule(None)
    assert(s is not None)

# Generated at 2022-06-13 15:16:04.288258
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    import pdb
    import mock
    import tempfile
    import filecmp
    import os
    import shutil

    sandbox_file = tempfile.NamedTemporaryFile(mode="a", delete=False)
    sandbox_file.write("sandbox")
    sandbox_file.close()
    sandbox_dir = tempfile.mkdtemp(prefix="ansible_test_")
    module_utils = os.path.join(os.path.realpath(os.path.dirname(__file__)), "../../../../lib/ansible/module_utils")
    shutil.copytree(module_utils, sandbox_dir + "/lib/ansible/module_utils")
    os.remove(sandbox_dir + "/lib/ansible/module_utils/__init__.py")

    tqm = mock.MagicMock()

# Generated at 2022-06-13 15:16:05.586305
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_module = StrategyModule(None)
    assert strategy_module._host_pinned

# Generated at 2022-06-13 15:16:07.063304
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    s = StrategyModule(tqm={})
    assert s._host_pinned == True
