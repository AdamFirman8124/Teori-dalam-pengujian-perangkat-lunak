

# Generated at 2022-06-13 15:06:27.223818
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    sm = StrategyModule(tqm="tqm")
    assert sm._host_pinned == True

# Generated at 2022-06-13 15:06:28.133147
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    StrategyModule("tqm")
    assert True

# Generated at 2022-06-13 15:06:32.604293
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    global display
    from ansible.plugins.strategy.free import StrategyModule as FreeStrategyModule
    from ansible.plugins.strategy.host_pinned import StrategyModule
    assert issubclass(StrategyModule, FreeStrategyModule)

    from ansible.utils.display import Display
    from ansible.plugins.strategy import StrategyBase
    from ansible.plugins.strategy.host_pinned import StrategyModule
    from ansible.executor.task_queue_manager import TaskQueueManager
    
    #constructor test
    display = Display()
    strategy = StrategyModule(TaskQueueManager())
    assert issubclass(type(strategy), StrategyBase)

# Generated at 2022-06-13 15:06:33.125335
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    StrategyModule(None)

# Generated at 2022-06-13 15:06:35.083521
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    S = StrategyModule(tqm=None)
    assert (type(S) is StrategyModule)

# Generated at 2022-06-13 15:06:38.197112
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    strategy=StrategyModule(tqm)
    assert strategy

if __name__ == '__main__':
    tqm = None
    strategy=StrategyModule(tqm)
    assert strategy

# Generated at 2022-06-13 15:06:39.497966
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert 'StrategyModule' == StrategyModule.__name__


# Generated at 2022-06-13 15:06:41.104899
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    sm = StrategyModule(tqm = "tqm")
    assert sm._host_pinned == True

# Generated at 2022-06-13 15:06:41.619357
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass

# Generated at 2022-06-13 15:06:43.077556
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = object()
    sm = StrategyModule(tqm)
    assert sm._host_pinned is True

# Generated at 2022-06-13 15:06:45.273678
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    a = StrategyModule(1)
    assert a != None

# Generated at 2022-06-13 15:06:47.025275
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    sm = StrategyModule(tqm)

    assert sm is not None

# Generated at 2022-06-13 15:06:48.353560
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    s = StrategyModule(tqm)
    assert s._host_pinned == True

# Generated at 2022-06-13 15:06:51.501067
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    host0 = {'ID': 0}
    host1 = {'ID': 1}
    host2 = {'ID': 2}
    tqm = {'hosts': [host0, host1, host2]}
    StrategyModule(tqm)

# Generated at 2022-06-13 15:06:53.147912
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    mod = StrategyModule(None)
    assert hasattr(mod, '_host_pinned') == True

# Generated at 2022-06-13 15:06:54.404044
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    StrategyModule(None)

# Generated at 2022-06-13 15:06:59.148492
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.inventory.host import Host

    inventory = ["testhost"]
    tqm = TaskQueueManager(
        inventory = inventory,
        variable_manager = object,
        loader = object,
        options = object,
        passwords = object,
        stdout_callback = object,
    )

    strategy_module = StrategyModule(tqm)

    assert strategy_module._host_pinned == True

# Generated at 2022-06-13 15:07:00.624617
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    strategy = StrategyModule(tqm)
    assert strategy._host_pinned == True


# Generated at 2022-06-13 15:07:01.636576
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    display = Display()
    display.display(strategy)

# Generated at 2022-06-13 15:07:04.111164
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    t = StrategyModule()
    assert t._host_pinned == True

# Generated at 2022-06-13 15:07:08.233361
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    strategy_obj = StrategyModule(tqm)
    assert strategy_obj._host_pinned is True

# Generated at 2022-06-13 15:07:12.096385
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule.__doc__ == """Executes tasks on each host without interruption"""
    assert StrategyModule.__init__.__doc__ == """Creates an instance of StrategyModule."""
    assert StrategyModule.run.__doc__ == """Runs the Ansible task queue manager."""
    assert StrategyModule.cleanup.__doc__ == """Clears layers of abstraction to reclaim memory"""

# Generated at 2022-06-13 15:07:13.281785
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert(True)

# Generated at 2022-06-13 15:07:14.241258
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    sm = StrategyModule(None)
    assert sm._host_pinned is True
    assert sm._tqm is None



# Generated at 2022-06-13 15:07:16.076328
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule is not None


# Generated at 2022-06-13 15:07:17.413475
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule is not None

# Generated at 2022-06-13 15:07:18.136044
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True



# Generated at 2022-06-13 15:07:18.814687
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule

# Generated at 2022-06-13 15:07:22.184754
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    import ansible.plugins.strategy.host_pinned
    strategy_module = ansible.plugins.strategy.host_pinned.StrategyModule('')
    strategy_module._host_pinned
    assert strategy_module._host_pinned == True
    strategy_module.send_callback
    strategy_module.queue_task
    strategy_module.wait_on_pending_results

# Generated at 2022-06-13 15:07:25.788641
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from mock import MagicMock
    from ansible.plugins.strategy.host_pinned import StrategyModule
    from ansible.plugins.strategy.free import StrategyModule as FreeStrategyModule
    tqm = MagicMock()
    strategy = StrategyModule(tqm)
    assert(strategy is not None)
    assert(isinstance(strategy, FreeStrategyModule))
    assert(strategy._host_pinned == True)

# Generated at 2022-06-13 15:07:30.554525
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule(tqm=None)

# Generated at 2022-06-13 15:07:31.606508
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule(tqm)

# Generated at 2022-06-13 15:07:32.566838
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule(None)


# Generated at 2022-06-13 15:07:33.223940
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass

# Generated at 2022-06-13 15:07:33.791867
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule(tqm=None)

# Generated at 2022-06-13 15:07:42.697200
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule.__name__ == 'StrategyModule'
    assert StrategyModule.__mro__[1].__name__ == 'object'
    assert StrategyModule.__mro__[2].__name__ == 'FreeStrategyModule'
    assert StrategyModule.__mro__[3].__name__ == 'BaseStrategyModule'
    assert StrategyModule.__mro__[4].__name__ == 'object'
    assert StrategyModule.__mro__[5].__name__ == 'object'
    assert StrategyModule.__mro__[6].__name__ == 'object'
    assert StrategyModule.__mro__[7].__name__ == 'object'
    assert StrategyModule.__mro__[8].__name__ == 'object'

# Generated at 2022-06-13 15:07:44.344842
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    s = StrategyModule(None)
    assert s
    assert s._host_pinned
    assert s._tqm is None

# Generated at 2022-06-13 15:07:45.620425
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    obj=StrategyModule()
    assert obj is not None, 'StrategyModule object is None'

# Generated at 2022-06-13 15:07:47.811106
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    res=StrategyModule("tqm")
    assert res._host_pinned == True


# Generated at 2022-06-13 15:07:49.227145
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    s = StrategyModule()



# Generated at 2022-06-13 15:07:59.181349
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    StrategyModule()

# Generated at 2022-06-13 15:08:06.630290
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.plugins.strategy.host_pinned import StrategyModule
    from ansible.executor import task_queue_manager
    from ansible.playbook import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.vars import combine_vars
    from ansible.utils.vars import combine_hash
    from ansible.utils.vars import load_extra_vars

# Generated at 2022-06-13 15:08:08.619803
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    obj = StrategyModule(tqm='')
    assert obj._host_pinned == True

# Generated at 2022-06-13 15:08:17.797602
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.playbook.play import Play
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.inventory.inventory import Inventory
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    host = Host(name="example.org")
    group = Group(name="example_group")
    group.add_host(host)
    inventory = Inventory(loader=DataLoader(), groups=[group])
    variable_manager = VariableManager(loader=DataLoader(), inventory=inventory)

# Generated at 2022-06-13 15:08:18.971118
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    x = StrategyModule()
    print(x._host_pinned)

# Generated at 2022-06-13 15:08:20.351594
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_module = StrategyModule(connection="connection", hosts="host")
    assert strategy_module._host_pinned == True

# Generated at 2022-06-13 15:08:21.605077
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = null
    acst = StrategyModule(tqm)

# Generated at 2022-06-13 15:08:22.286852
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule.__name__ == "StrategyModule"

# Generated at 2022-06-13 15:08:24.536937
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy = StrategyModule()
    assert strategy._host_pinned == True

# Generated at 2022-06-13 15:08:26.047980
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    host_pinned = StrategyModule()
    assert host_pinned is not None

# Generated at 2022-06-13 15:08:43.034509
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = object()
    assert StrategyModule(tqm).tqm == tqm

# Generated at 2022-06-13 15:08:44.948417
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    s = StrategyModule(None)
    assert s._host_pinned


# vim: et ts=4 sw=4 ft=python

# Generated at 2022-06-13 15:08:48.321696
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule.__name__ == 'StrategyModule'
    assert StrategyModule.__module__ == 'ansible.plugins.strategy.host_pinned'

# Generated at 2022-06-13 15:08:48.908050
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule({})

# Generated at 2022-06-13 15:08:58.248535
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.plugins.strategy.host_pinned import StrategyModule
    from ansible.plugins.strategy.free import StrategyModule as FreeStrategyModule
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    import ansible.constants as C

    class Options(object):
        controller = None
        forks = C.DEFAULT_FORKS
        check = False
        listhosts = None
        module_path = None
        module_name = None
        module_args = None
        pattern = None
        extra_vars = None
        subset = None
        inventory = None
        inventory_manager_class = InventoryManager
        variable_manager_class = VariableManager
        display = Display()
        verbosity

# Generated at 2022-06-13 15:09:05.067005
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = MagicMock(
        _initialize_processes=None,
        send_callback=None,
        get_vault_secrets=None,
        hosts=None,
        get_inventory=None,
        loader=None,
        display=None,
        variables=None,
        run_handlers=None,
        run_final_queue=None,
        run_unreachable_host_queue=None,
        stats=None,
        extra_vars=None,
    )

    strategy_module = StrategyModule(tqm)

    assert strategy_module._host_pinned

# Generated at 2022-06-13 15:09:12.377147
# Unit test for constructor of class StrategyModule
def test_StrategyModule():

    # Create a dict for a task.
    task = dict(name='test_task', action='test_action')

    # Create a dict for a result.
    result = dict(name='test_task', result='test_result')

    # Create a dict for a host.
    host = dict(name = 'test_host')

    # Create a dict for a play.
    play = dict(name = 'test_play')

    # Create a dict for a set of hosts.
    host_set = dict(name = 'test_host_set')

    # Create a dict for a variable.
    variable = dict(name = 'test_variable', value = 'test_value')

    # Create a dict for a variable manager.
    variable_manager = dict(name = 'test_variable_manager')

    # Create a dict for a task queue manager

# Generated at 2022-06-13 15:09:13.003320
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True

# Generated at 2022-06-13 15:09:14.849272
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    '''
    Test the StrategyModule class.
    '''
    strategy_module = StrategyModule({})
    assert strategy_module is not None

# Generated at 2022-06-13 15:09:15.742600
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert 1 == 1, "Test is OK"

# Generated at 2022-06-13 15:09:58.276661
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule.__doc__ == FreeStrategyModule.__doc__
    assert StrategyModule.__name__ == FreeStrategyModu

# Generated at 2022-06-13 15:09:59.817683
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    StrategyModule("tqm")

# Generated at 2022-06-13 15:10:00.838659
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    stg=StrategyModule(tqm)

# Generated at 2022-06-13 15:10:02.153004
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert hasattr(StrategyModule, '__init__') == True


# Generated at 2022-06-13 15:10:02.711877
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule

# Generated at 2022-06-13 15:10:04.653184
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.plugins.strategy import StrategyModule
    tqm = None
    assert isinstance(StrategyModule(tqm), StrategyModule)

# Generated at 2022-06-13 15:10:05.181705
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule()

# Generated at 2022-06-13 15:10:06.008178
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy = StrategyModule(tqm)

# Generated at 2022-06-13 15:10:06.855506
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy = StrategyModule(None)
    assert strategy._host_pinned



# Generated at 2022-06-13 15:10:07.800504
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # Test for correct creation of object
    assert StrategyModule(None)

# Generated at 2022-06-13 15:11:31.345515
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert 1

# Generated at 2022-06-13 15:11:36.267389
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.utils.display import Display
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.inventory.manager import InventoryManager

#   # set up tqm
#   display = Display()
#   tqm = TaskQueueManager(inventory = InventoryManager(host_list='/etc/ansible/hosts'), variable_manager = None, loader = loader, options = None, passwords = None, stdout_callback = display.display, run_additional_callbacks = None, run_tree = False, )

#   # Process test Strategy module
#   my_strategy_module = StrategyModule(tqm = tqm)
#   my_strategy_module.run()

# Generated at 2022-06-13 15:11:38.993822
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    test_tqm = type('TQM', (object,), {'stats': {'dark': {}}})
    test_strategyModule = StrategyModule(test_tqm)

    assert test_strategyModule is not None

# Generated at 2022-06-13 15:11:42.709472
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    import unittest
    import ansible.plugins.strategy.host_pinned

    tqm = ansible.plugins.strategy.host_pinned.TaskQueueManager(None,None)
    assert isinstance(tqm,ansible.plugins.strategy.host_pinned.TaskQueueManager)
    #assert(tqm.is_strategy_plugin())

# Generated at 2022-06-13 15:11:43.522713
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule(None) is not None

# Generated at 2022-06-13 15:11:44.517703
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert(StrategyModule.__name__ == 'StrategyModule')

# Generated at 2022-06-13 15:11:47.962698
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    test_tmq = "test"
    result = StrategyModule(test_tmq)
    expected_result = "host_pinned"
    if result._host_pinned != expected_result:
        raise RuntimeError("Test with construction of class StrategyModule failed")

if __name__ == '__main__':
    test_StrategyModule()

# Generated at 2022-06-13 15:11:48.825186
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass

# Generated at 2022-06-13 15:11:58.619106
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule.__base__ == FreeStrategyModule

# Generated at 2022-06-13 15:11:59.483121
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass


# Generated at 2022-06-13 15:15:04.862334
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from pprint import pprint as pp
    from ansible.utils.display import Display
    display = Display()
    strategy = StrategyModule('test')
    host_pinned = getattr(strategy, '_host_pinned', False)
    assert host_pinned

# Generated at 2022-06-13 15:15:08.172733
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    mod_strategy = StrategyModule(tqm="tqm")
    print(mod_strategy._host_pinned)  # noqa
    assert(mod_strategy._host_pinned == True)

# Generated at 2022-06-13 15:15:09.637734
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_module = StrategyModule("Module name")
    # goal is to not get an exception
    assert strategy_module

# Generated at 2022-06-13 15:15:12.200469
# Unit test for constructor of class StrategyModule
def test_StrategyModule():

    # Test values
    s = StrategyModule('tqm')
    assert s._host_pinned == True
    display.display('Test StrategyModule: Constructor')

# Generated at 2022-06-13 15:15:12.746485
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass

# Generated at 2022-06-13 15:15:13.690068
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert isinstance(StrategyModule, object)

# Generated at 2022-06-13 15:15:14.223861
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    StrategyModule(1)

# Generated at 2022-06-13 15:15:16.054580
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    global StrategyModule
    assert( callable(StrategyModule))
    #StrategyModule = StrategyModule()
    assert( StrategyModule.__class__.__name__ == "StrategyModule")


# Generated at 2022-06-13 15:15:16.553436
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule

# Generated at 2022-06-13 15:15:18.021644
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule(mock.sentinel.tqm).__init__(mock.sentinel.tqm), 'Strategy module constructor failed'