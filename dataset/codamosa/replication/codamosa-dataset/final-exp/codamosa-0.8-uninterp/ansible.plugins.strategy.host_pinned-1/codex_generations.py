

# Generated at 2022-06-13 15:06:36.092390
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    """
    Constructor for StrategyModule class
    """
    import Queue
    live_pool = Queue.Queue()
    new_tqm = Queue.Queue()
    newtqm = StrategyModule(new_tqm)
    assert newtqm is not None
    assert newtqm._host_pinned == True
    assert newtqm._tqm is not None
    assert newtqm._play is None
    assert newtqm._iterator is None
    assert newtqm._strategy is None
    assert newtqm._variables is None
    assert newtqm._host_state is None
    assert newtqm._pool is None
    assert newtqm._max_fail_pct is None
    assert newtqm._pending_results is None

# Generated at 2022-06-13 15:06:38.156137
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy = StrategyModule(tqm=None)
    assert strategy.display == Display()
    assert strategy._host_pinned == True

# Generated at 2022-06-13 15:06:41.815334
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    '''
    Constructor of class StrategyModule.
    :return:
    '''
    from ansible.executor.task_queue_manager import TaskQueueManager
    tqm = TaskQueueManager()
    strategy = StrategyModule(tqm)
    assert strategy._host_pinned == True

# Generated at 2022-06-13 15:06:42.859550
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = TaskQueueManager()
    test = StrategyModule(tqm)
    assert test._host_pinned == True

# Generated at 2022-06-13 15:06:45.364179
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule.__init__ != FreeStrategyModule.__init__

# Generated at 2022-06-13 15:06:46.325785
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert(StrategyModule)

# Generated at 2022-06-13 15:06:48.443175
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = 0
    strategy = StrategyModule(tqm)
    assert strategy
    assert strategy._host_pinned == True


# Generated at 2022-06-13 15:06:49.024346
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
  assert True

# Generated at 2022-06-13 15:06:50.741319
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    obj = StrategyModule(tqm = 'tqm')
    assert obj._host_pinned == True

# Generated at 2022-06-13 15:06:52.590841
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.plugins.strategy.host_pinned import StrategyModule
    tqm = ""
    v = StrategyModule(tqm)

# Generated at 2022-06-13 15:06:59.587816
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.plugins.strategy import strategy_loader
    from ansible.executor import task_queue_manager
    tqm = task_queue_manager.TaskQueueManager(
        inventory=None,
        variable_manager=None,
        loader=None,
        options=None,
        passwords=None,
        stdout_callback=None,
        run_additional_callbacks=False,
        run_tree=False,
    )
    strategy = strategy_loader.get(tqm, 'host_pinned')
    assert type(strategy) == StrategyModule
    assert strategy._host_pinned == True

# Generated at 2022-06-13 15:07:00.559796
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule(tqm=None)._host_pinned == True


# Generated at 2022-06-13 15:07:02.488139
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    x = StrategyModule(False)
    assert isinstance(x, FreeStrategyModule)
    if hasattr(x, '_host_pinned'):
        assert x._host_pinned == True

# Generated at 2022-06-13 15:07:03.559395
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    my_strategy_object=StrategyModule(None)
    assert my_strategy_object._host_pinned == True

# Generated at 2022-06-13 15:07:04.324084
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True

# Generated at 2022-06-13 15:07:05.774619
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert(StrategyModule.__name__ == 'StrategyModule')
    assert(StrategyModule.__doc__ == '\nHostPinnedStrategyModule\n')

# Generated at 2022-06-13 15:07:06.593927
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    stg = StrategyModule(1)
    assert stg._host_pinned == True

# Generated at 2022-06-13 15:07:10.787655
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.plugins.strategy.host_pinned import StrategyModule
    display = Display()
    tqm = Display()
    s = StrategyModule(tqm)
    if s._host_pinned:
        display.display("test_StrategyModule is passed")
    else:
        display.display("test_StrategyModule is failed")

# Generated at 2022-06-13 15:07:12.821040
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_module = StrategyModule('')
    assert strategy_module._host_pinned == True

# Generated at 2022-06-13 15:07:13.924526
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    StrategyModule()

# Generated at 2022-06-13 15:07:17.156755
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert type(StrategyModule) == type

# Generated at 2022-06-13 15:07:17.856101
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    modul = StrategyModule(tqm)

# Generated at 2022-06-13 15:07:20.386013
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.plugins.strategy.host_pinned import StrategyModule
    from ansible.executor.task_queue_manager import TaskQueueManager
    tqm = TaskQueueManager()
    StrategyModule(tqm)


# Generated at 2022-06-13 15:07:23.408260
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # pylint: disable=protected-access
    tqm = MagicMock()
    strategy = StrategyModule(tqm)
    assert strategy._host_pinned is True

# Generated at 2022-06-13 15:07:25.128105
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = 'test'
    testStrategyModule = StrategyModule(tqm)
    assert testStrategyModule._host_pinned == True


# Generated at 2022-06-13 15:07:25.533766
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule

# Generated at 2022-06-13 15:07:25.930959
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True

# Generated at 2022-06-13 15:07:26.512114
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule

# Generated at 2022-06-13 15:07:29.034055
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    strategy_module = StrategyModule(tqm)
    assert strategy_module._host_pinned == True
    assert strategy_module._display == Display()

# Generated at 2022-06-13 15:07:30.509648
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_module = StrategyModule(None)
    assert strategy_module is not None

# Generated at 2022-06-13 15:07:35.130953
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule.__doc__ is not None

# Generated at 2022-06-13 15:07:36.013437
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert(StrategyModule(1) is not None)

# Generated at 2022-06-13 15:07:37.332543
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    FreeStrategyModule.__init__(FreeStrategyModule)

# Generated at 2022-06-13 15:07:39.932183
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    """ Unit test for constructor of class StrategyModule
    """
    strategy = StrategyModule(None)
    assert strategy._host_pinned


if __name__ == '__main__':
    test_StrategyModule()

# Generated at 2022-06-13 15:07:40.565257
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
  assert StrategyModule


# Generated at 2022-06-13 15:07:42.036646
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = {'send_cli_msg': 'test'}
    StrategyModule(tqm)

# Generated at 2022-06-13 15:07:43.455494
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_module = StrategyModule(None)
    assert strategy_module._host_pinned is True

# Generated at 2022-06-13 15:07:45.888905
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True

# Generated at 2022-06-13 15:07:50.670015
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.playbook.task_include import TaskInclude
    strategy = StrategyModule("test_tqm")
    assert isinstance(strategy,FreeStrategyModule)
    assert strategy._host_pinned == True

# Create a basic TaskResult to test get_host_result()

# Generated at 2022-06-13 15:07:54.084689
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from __main__ import display

    strategy_Obj = StrategyModule(display)

    print(strategy_Obj._host_pinned)

if __name__ == '__main__':
    test_StrategyModule()

# Generated at 2022-06-13 15:08:04.434781
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True

if __name__ == '__main__':
    test_StrategyModule()

# Generated at 2022-06-13 15:08:07.701713
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.plugins.strategy.host_pinned import StrategyModule
    from ansible.utils.connection import Connection
    a = StrategyModule()
    assert (a)

# Generated at 2022-06-13 15:08:08.312108
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
	pass

# Generated at 2022-06-13 15:08:10.136936
# Unit test for constructor of class StrategyModule
def test_StrategyModule():

    tqm = None
    strategy = StrategyModule(tqm)

    assert strategy._host_pinned

# Generated at 2022-06-13 15:08:13.310984
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.plugins.strategy.host_pinned import StrategyModule
    sm = StrategyModule(None)
    assert sm._host_pinned == True
    return True

# Generated at 2022-06-13 15:08:15.452107
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = object()
    sm = StrategyModule(tqm)
    assert sm._tqm == tqm
    assert sm._host_pinned == True

# Generated at 2022-06-13 15:08:21.178712
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    test_tqm = [
        'ansible.plugins.strategy.host_pinned.StrategyModule',
        'ansible.plugins.strategy.host_pinned.FreeStrategyModule'
    ]
    test_obj = StrategyModule('test_tqm')
    assert test_obj._host_pinned == True
    assert test_obj.__doc__ != None
    assert StrategyModule.__module__ == 'ansible.plugins.strategy.host_pinned'
    assert StrategyModule.__doc__ != None

# Generated at 2022-06-13 15:08:22.508999
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    global strategy_obj

    strategy_obj = StrategyModule(None)
    assert strategy_obj._host_pinned is True

# Generated at 2022-06-13 15:08:25.259663
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    StrategyModule(tqm)
    assert StrategyModule(tqm)

# Generated at 2022-06-13 15:08:32.914546
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.errors import AnsibleError
    from ansible.executor.task_queue_manager import TaskQueueManager
    try:
        tqm = TaskQueueManager(None, None, None, None, None, None, None, None)
        free = StrategyModule(tqm)
        assert free._host_pinned == True
    except AnsibleError:
        raise AnsibleError("Unit test for constructor of class StrategyModule failed")


# Generated at 2022-06-13 15:08:52.554864
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
  import mock
  import ansible.plugins.strategy.host_pinned
  mock_tqm = mock.MagicMock()
  sm = ansible.plugins.strategy.host_pinned.StrategyModule(mock_tqm)
  assert sm._host_pinned is True

# Generated at 2022-06-13 15:08:54.374381
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    t = StrategyModule.__init__('self', 'tqm')
    assert t is not None


# Generated at 2022-06-13 15:08:56.240252
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    display.verbosity = 5
    tqm = None
    strategy = StrategyModule(tqm)
    assert strategy._host_pinned is True

# Generated at 2022-06-13 15:08:59.699064
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.executor.task_queue_manager import TaskQueueManager
    tqm = TaskQueueManager(None, None)
    strategy_module = StrategyModule(tqm)
    assert strategy_module is not None
    assert isinstance(strategy_module, StrategyModule)
    assert strategy_module._host_pinned, 'expected host_pinned not True'

# Generated at 2022-06-13 15:09:08.466811
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    d = {'name': 'host_pinned', '_host_pinned': True}
    # class FakeOptions(object):
    #     forks = 5
    #     step = 5
    #     start_at_task = None
    #     pattern = 'all'
    #     subset = None
    #     serial = 'all'
    #     inventory = '/home/vagrant/ansible/inventory'
    #     module_path = '/tmp'
    #     extra_vars = None
    #     module_vars = None
    #     listhosts = None
    #     listtasks = None
    #     listtags = None
    #     syntax = None
    #     diff = False
    #     connection = 'smart'
    #     timeout = 10
    #     poll_interval = 15
    #    

# Generated at 2022-06-13 15:09:09.584117
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    StrategyModule(tqm)

# Generated at 2022-06-13 15:09:12.014006
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    result = StrategyModule(tqm)
    assert result._host_pinned == True

# Generated at 2022-06-13 15:09:13.935835
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    sm = StrategyModule(tqm)
    assert sm._host_pinned == True



# Generated at 2022-06-13 15:09:16.597660
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
  tqm = object()
  strategy_module = StrategyModule(tqm)
  # test for __init__
  assert strategy_module._host_pinned == True

from ansible.plugins.strategy.host_pinned import StrategyModule
from ansible.utils.display import Display
strategy_module = StrategyModule(tqm)
strategy_module.main()

# Generated at 2022-06-13 15:09:18.885760
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_module = StrategyModule()
    assert strategy_module is not None

# Generated at 2022-06-13 15:10:01.547187
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    SM = StrategyModule()
    assert hasattr(StrategyModule, 'get_host_list')



# Generated at 2022-06-13 15:10:03.261846
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    global display
    strategy = StrategyModule(display)
    assert strategy._host_pinned == True

# Generated at 2022-06-13 15:10:09.955280
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.plugins.strategy.host_pinned import StrategyModule
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.executor.task_executor import TaskExecutor
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.executor.task_result import TaskResult
    from ansible.executor.stats import AggregateStats
    from ansible.playbook.handler import Handler

# Generated at 2022-06-13 15:10:10.993409
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategyModule = StrategyModule(tqm)
    assert strategyModule._host_pinned == True

# Generated at 2022-06-13 15:10:12.452391
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # this should pass silently
    StrategyModule(None)

# Generated at 2022-06-13 15:10:13.003608
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True

# Generated at 2022-06-13 15:10:18.717147
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    msg = "Testing constructor of class StrategyModule..."
    print(msg)
    tqm = None
    s = StrategyModule(tqm)
    if s:
        print(msg + "OK")
    else:
        print(msg + "KO")

# Generated at 2022-06-13 15:10:28.184502
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule(None) is not None


# Testing of StrategyModule class

# def test_class_StrategyModule():
#     pass
#
# def test_init_of_StrategyModule():
#     pass
#
# def test_extract_inventory_with_play_of_StrategyModule():
#     pass
#
# def test_run_of_StrategyModule():
#     pass
#
# def test_get_host_list_with_play_of_StrategyModule():
#     pass
#
# def test_add_tqm_variables_of_StrategyModule():
#     pass
#
# def test_get_hosts_remaining_in_play_of_StrategyModule():
#     pass
#
# def test_teardown_of_StrategyModule():
#

# Generated at 2022-06-13 15:10:28.503524
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass

# Generated at 2022-06-13 15:10:29.032558
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule

# Generated at 2022-06-13 15:12:06.096584
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True

# Generated at 2022-06-13 15:12:08.271415
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert not StrategyModule(None)._host_pinned

# Generated at 2022-06-13 15:12:09.606316
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    myModule = StrategyModule()
    assert myModule._host_pinned

# Generated at 2022-06-13 15:12:10.148976
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass

# Generated at 2022-06-13 15:12:11.272101
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    mod = StrategyModule
    x = mod.__init__
    assert x is not None

# Generated at 2022-06-13 15:12:12.669868
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass

# Generated at 2022-06-13 15:12:14.456949
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule is not None
    s = StrategyModule(None)
    assert s._host_pinned is True

# Generated at 2022-06-13 15:12:15.382188
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule(1).host_pinned


# Generated at 2022-06-13 15:12:16.157512
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    module = StrategyModule(None)
    assert module != None

# Generated at 2022-06-13 15:12:19.276582
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    a = StrategyModule({})
    print('StrategyModule a = ' + str(a))

# Generated at 2022-06-13 15:15:30.710849
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule(tqm=None)

# Generated at 2022-06-13 15:15:31.246935
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass

# Generated at 2022-06-13 15:15:35.077157
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext

    from ansible.utils.sentinel import Sentinel
    from ansible.plugins.loader import action_loader
    from ansible.plugins.loader import cache_loader

    from ansible.executor.task_result import TaskResult

    from ansible.executor.process.factory import ProcessFactory

    from ansible.executor.play_iterator import PlayIterator

    from ansible.executor.task_queue_manager import TaskQueueManager

    from ansible.utils.display import Display

    from ansible.plugins.strategy import StrategyModule
    import unittest

    Play = PlayIterator.Play

    class FakeHost:
        def __init__(self, name):
            self.name = name
            self.host_name = name

# Generated at 2022-06-13 15:15:37.454361
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    """Test StrategyModule constructor
    """
    tqm = None
    s = StrategyModule(tqm)
    assert s.name == 'host_pinned'

# Generated at 2022-06-13 15:15:38.908025
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    obj = StrategyModule(tqm = None)
    assert(obj._host_pinned == True)

# Generated at 2022-06-13 15:15:40.682357
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    sm = StrategyModule('test')
    assert sm._get_host_queue_item() == FreeStrategyModule.add_host_to_queue('test')

# Generated at 2022-06-13 15:15:44.472803
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = TaskQueueManager(
        inventory=inventory,
        variable_manager=variable_manager,
        loader=loader,
        options=options,
        passwords=passwords,
        stdout_callback=results_callback,  # Use our custom callback instead of the ``default`` callback plugin, which prints to stdout
    )
    sm = StrategyModule(tqm)
    assert sm is not None

# Generated at 2022-06-13 15:15:46.278815
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    sm = StrategyModule(None)
    assert sm._host_pinned == True

# Generated at 2022-06-13 15:15:47.832608
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
   tqm = object
   result = StrategyModule(tqm)
   display.display(result._host_pinned)

# Generated at 2022-06-13 15:15:53.541115
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    import sys
    import ansible
    from ansible.plugins.strategy.host_pinned import StrategyModule
    # Set up all the required params
    tqm = FakeTQM()
    # Create an object of class StrategyModule
    sm = StrategyModule(tqm)
    # Test the behavior of class StrategyModule
    assert(sm._host_pinned is True)


# Test class of TestQueueManager that is in charge of initializing and running the strategy plugins