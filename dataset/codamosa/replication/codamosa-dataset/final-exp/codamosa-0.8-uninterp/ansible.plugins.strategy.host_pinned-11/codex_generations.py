

# Generated at 2022-06-13 15:06:30.082294
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True

# Generated at 2022-06-13 15:06:31.388182
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    StrategyModule(tqm) # no exception

# Generated at 2022-06-13 15:06:36.900584
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    def display_logs(msg):
        pass

    tqm.host_list = [host.name for host in inventory.get_hosts()]
    tqm.inventory = inventory
    tqm.variable_manager = variable_manager
    tqm.loader = loader
    tqm.options = options
    tqm.display = display_logs
    assert isinstance(StrategyModule(tqm), StrategyModule)

# Generated at 2022-06-13 15:06:45.055971
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    play = Play().load(dict(
        name = "Ansible Play 0",
        hosts = 'localhost',
        gather_facts = 'no',
        tasks = [
            dict(action=dict(module='debug', args=dict(msg='{{uname}}'))),
        ]
    ), variable_manager=dict(), loader=None)
    tqm = None

# Generated at 2022-06-13 15:06:46.731394
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    obj = StrategyModule(tqm)
    assert obj._host_pinned is True

# Generated at 2022-06-13 15:06:48.487172
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    m = StrategyModule(tqm = None)
    assert m._host_pinned == True

# Generated at 2022-06-13 15:06:56.280027
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    a = StrategyModule('tqm')
    print("print the value of the private attribute '_host_pinned' of class StrategyModule:", a._host_pinned)
    if a._host_pinned == True:
        print("correct")
    else:
        print("incorrect")

#test_StrategyModule()


if __name__ == '__main__':
    a = StrategyModule('tqm')
    print("print the value of the private attribute '_host_pinned' of class StrategyModule:", a._host_pinned)
    if a._host_pinned == True:
        print("correct")
    else:
        print("incorrect")

# Generated at 2022-06-13 15:06:57.738995
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule.__subclasses__() != FreeStrategyModule.__subclasses__()

# Generated at 2022-06-13 15:06:59.356960
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy = StrategyModule
    obj = strategy(tqm=None)
    assert obj is not None
    assert obj._host_pinned is True

# Generated at 2022-06-13 15:07:00.465306
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    StrategyModule("tqm")

# Generated at 2022-06-13 15:07:03.798107
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    mod = StrategyModule(None)
    assert mod._host_pinned is True

# Generated at 2022-06-13 15:07:04.445714
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule

# Generated at 2022-06-13 15:07:05.223247
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    strategyModule = StrategyModule(tqm)
    assert strategyModule._host_pinned

# Generated at 2022-06-13 15:07:06.291002
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule.__init__


# Generated at 2022-06-13 15:07:07.229548
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_module = StrategyModule(None)
    assert strategy_module is not None
    assert strategy_module._host_pinned ==True

# Generated at 2022-06-13 15:07:09.712184
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    SM = StrategyModule("a")
    assert SM._host_pinned == True
    assert SM._batch_count == 0
    assert SM._batch_size == 1

# Generated at 2022-06-13 15:07:14.703145
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert issubclass(StrategyModule, FreeStrategyModule)
    # Call the constructor of class StrategyModule
    tqm = {'tqm1': 'tqm1'}
    obj = StrategyModule(tqm)
    assert obj._host_pinned == True

# test_StrategyModule()

# Generated at 2022-06-13 15:07:17.685695
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    _tqm = None
    _strategy = StrategyModule(_tqm)
    assert _strategy is not None


# Generated at 2022-06-13 15:07:20.572540
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule.__name__ == 'StrategyModule'
    assert StrategyModule.__doc__ == 'Host-pinned strategy for handling hosts in order.'

# Generated at 2022-06-13 15:07:21.244245
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass

# Generated at 2022-06-13 15:07:23.593026
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule({})

# Generated at 2022-06-13 15:07:26.822349
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    sm = StrategyModule(tqm)
    assert sm._host_pinned == True
    assert sm._batch_size == 0
    assert sm._inventory == None
    assert sm._index_count == 0

# Generated at 2022-06-13 15:07:27.844978
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
  strategyModule = StrategyModule()

# Generated at 2022-06-13 15:07:31.460109
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_module = FreeStrategyModule('test_tqm')
    strategy_module.__init__('test_tqm')
    strategy_module = StrategyModule('test_tqm')
    strategy_module.__init__('test_tqm')


# Generated at 2022-06-13 15:07:32.964400
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy = StrategyModule([])
    assert strategy._host_pinned

# Generated at 2022-06-13 15:07:35.802773
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = ansible.executor.task_queue_manager.TaskQueueManager()
    sm = StrategyModule(tqm)
    print("StrategyModule: " + str(sm._host_pinned))

# Generated at 2022-06-13 15:07:37.105236
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule('tqm') is not None

# Generated at 2022-06-13 15:07:38.034183
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    StrategyModule(None)


# Generated at 2022-06-13 15:07:39.648272
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = 'default'
    StrategyModule(tqm)

# test case for class StrategyModule

# Generated at 2022-06-13 15:07:41.837904
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # Test with QueueManager object as parameter
    tqm = None
    obj = StrategyModule(tqm)
    assert obj is not None
    assert isinstance(obj, StrategyModule)

# Generated at 2022-06-13 15:07:46.692559
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True

# Generated at 2022-06-13 15:07:48.182568
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.plugins.strategy.host_pinned import StrategyModule
    assert hasattr(StrategyModule, '__init__')

# Generated at 2022-06-13 15:07:59.933150
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.plugins.strategy.host_pinned import StrategyModule
    from ansible.plugins.strategy import StrategyBase
    from ansible import context
    from ansible.executor.task_result import TaskResult
    from ansible.executor.result import Result
    import ansible.task
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play

    loader = DataLoader()
    variable_manager = VariableManager()
    variable_manager.extra_vars = {'ansible_connection': 'fake'}
    inventory = InventoryManager(loader=loader, sources='localhost,')
    variable_manager.set_inventory(inventory)
    play_source =  dict

# Generated at 2022-06-13 15:08:01.011429
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
   pass

# Generated at 2022-06-13 15:08:03.144088
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule is not None
    display.test('test_strategy_pinned construct complete')

test_StrategyModule()

# Generated at 2022-06-13 15:08:06.176420
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_module = StrategyModule(host=None,task_queue_manager=None)
    assert(strategy_module._host_pinned == True)

# Generated at 2022-06-13 15:08:07.443832
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    module = StrategyModule()
    assert module is not None

# Generated at 2022-06-13 15:08:08.535920
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule


# Generated at 2022-06-13 15:08:10.365016
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    s = StrategyModule(None)
    assert s._host_pinned == True

# tests for construction of StrategyModule objects

# Generated at 2022-06-13 15:08:14.756660
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    import ansible.plugins.strategy.host_pinned

    tm = ansible.plugins.strategy.host_pinned.StrategyModule('tm')
    assert tm._host_pinned == True
    assert tm._tqm is 'tm'

# Generated at 2022-06-13 15:08:22.632760
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass

# Generated at 2022-06-13 15:08:24.840222
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    module = StrategyModule(None)
    assert module._host_pinned == True

# Generated at 2022-06-13 15:08:26.889224
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule

if __name__ == "__main__":
    test_StrategyModule()

# Generated at 2022-06-13 15:08:28.764848
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert(StrategyModule)

# Generated at 2022-06-13 15:08:29.808832
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy = StrategyModule()
    assert strategy._host_pinned == True

# Unit test of inherited method

# Generated at 2022-06-13 15:08:32.048275
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    sm = StrategyModule(tqm=None)

    assert sm._host_pinned == True

# Generated at 2022-06-13 15:08:36.515267
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    s= StrategyModule("tqm")
    print("tqm: " + s.tqm)
    print("_host_pinned: " + str(s._host_pinned))
    print("_blocks: " + str(s._blocks))
    print("_ however, this is not the real test: " + str(True))

# Generated at 2022-06-13 15:08:38.159989
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert not StrategyModule(None)._host_pinned
    assert StrategyModule(None)._host_pinned



# Generated at 2022-06-13 15:08:40.235120
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
   strategy = StrategyModule(tqm)
   assert strategy is not None
   assert strategy.__init__(tqm)

# Generated at 2022-06-13 15:08:41.832986
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy = StrategyModule(tqm='dummy tqm')
    assert strategy._host_pinned == True

# Generated at 2022-06-13 15:08:58.821463
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule.__doc__ != None

# Generated at 2022-06-13 15:09:00.832059
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    my_StrategyModule = StrategyModule()
    # Test that _host_pinned is set to True; this is the only testable property
    assert my_StrategyModule._host_pinned is True

# Generated at 2022-06-13 15:09:03.796285
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.plugins.strategy.host_pinned import StrategyModule
    from ansible.plugins.strategy import ActionModule
    strategy_module = StrategyModule(None)
    assert strategy_module._host_pinned


# Generated at 2022-06-13 15:09:05.215967
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    host = StrategyModule(tqm)
    assert hasattr(host,'_host_pinned')

# Generated at 2022-06-13 15:09:12.476499
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.plugins.strategy.host_pinned import StrategyModule
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.utils.vars import load_extra_vars
    from collections import namedtuple

# Generated at 2022-06-13 15:09:19.686200
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible import plugins
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.block import Block

    class FakeTQM(object):
        def __init__(self):
            self.inventory = plugins.inventory.InventoryLoader()

    tqm = FakeTQM()
    strategy = StrategyModule(tqm)
    assert strategy.get_name() == 'host_pinned'
    #host_list = [host1, host2, host3, host4, host5]
    #host_list_results = strategy.get_host_list(host_list)
    #assert sorted(host_list_results) == sorted(host_list)
    #assert strategy.get_host_list_max_batch() is None
    #assert strategy.check_conditional_needs_

# Generated at 2022-06-13 15:09:20.617326
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    StrategyModule(tqm={})

# Generated at 2022-06-13 15:09:22.746633
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = "tqm"
    StrategyModule(tqm)


# Generated at 2022-06-13 15:09:23.237592
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass

# Generated at 2022-06-13 15:09:26.446777
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # first initialize StrategyModule object
    strategy_module = StrategyModule('')
    # then test if the constructor properly set the initial values
    # assertion to check if the field _host_pinned is not None
    assert strategy_module._host_pinned is not None

# Generated at 2022-06-13 15:10:06.642431
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from mock import Mock
    tqm = Mock()
    sm = StrategyModule(tqm)
    assert sm._host_pinned is True


# Generated at 2022-06-13 15:10:12.622843
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.playbook import Play
    import ansible.playbook.play
    import ansible.playbook.task
    import ansible.playbook.block
    import ansible.playbook.handler
    import ansible.playbook.role

    play_source =  dict(
            name = "Ansible Play 1",
            hosts = 'hosts',
            gather_facts = 'no',
            tasks = [
                dict(action=dict(module='shell', args='ls'), register='shell_out'),
                dict(action=dict(module='debug', args=dict(msg='{{shell_out.stdout}}')))
             ]
        )

    play = Play().load(play_source, variable_manager = None, loader = None)

    inventory = ansible.inventory.Inventory("localhost")

# Generated at 2022-06-13 15:10:13.161917
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule

# Generated at 2022-06-13 15:10:17.588177
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = 2
    strategyModule = StrategyModule(tqm)
    assert strategyModule._host_pinned


# Generated at 2022-06-13 15:10:19.074272
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    display.debug("In test_StrategyModule of host_pinned\n")

# Generated at 2022-06-13 15:10:22.103298
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    print("------------------ test_StrategyModule start ------------------")
    strategy_module = StrategyModule(tqm = "")
    assert strategy_module._host_pinned == True
    print("------------------ test_StrategyModule end ------------------")

# Generated at 2022-06-13 15:10:23.303801
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    StrategyModule(tqm=None)

if __name__ == '__main__':
    test_StrategyModule()

# Generated at 2022-06-13 15:10:26.382410
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    import ansible.plugins.strategy.unit_test
    ansible.plugins.strategy.unit_test.StrategyModuleTestCase.test_StrategyModule()

# Generated at 2022-06-13 15:10:31.921994
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # Given
    tqm = 'something'

    # When
    strategy_module = StrategyModule(tqm)

    # Then
    assert strategy_module._tqm == tqm
    assert strategy_module._display == display
    assert strategy_module._inventory == None
    assert strategy_module._play == None
    assert strategy_module._variables == None
    assert strategy_module._loader == None
    assert strategy_module._variable_manager == None
    assert strategy_module._block_list == []

# Generated at 2022-06-13 15:10:33.156224
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    sm = StrategyModule(tqm)
    assert sm is not None

# Generated at 2022-06-13 15:12:10.435890
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass

# Generated at 2022-06-13 15:12:10.950485
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass

# Generated at 2022-06-13 15:12:12.523208
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert isinstance(StrategyModule(None), StrategyModule)

# Generated at 2022-06-13 15:12:13.970146
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    test=StrategyModule(tqm)
    assert test._host_pinned==True

# Generated at 2022-06-13 15:12:15.125019
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    module = StrategyModule(None)
    assert callable(module)

# Generated at 2022-06-13 15:12:16.157512
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = AnsibleTaskQueueManager([])
    StrategyModule(tqm)

# Generated at 2022-06-13 15:12:19.844211
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    sm = StrategyModule(tqm=None)
    assert sm._host_pinned == True

# Generated at 2022-06-13 15:12:22.873630
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    ansi_display = Display()
    ansi_display.display("strategy_host_pinned.StrategyModule")
    assert ansi_display.event == "strategy_host_pinned.StrategyModule"

# Generated at 2022-06-13 15:12:24.232462
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule(test_tqm) is not None


# Generated at 2022-06-13 15:12:26.488363
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = 'tqm'
    strategy = StrategyModule(tqm)
    assert hasattr(strategy, '_host_pinned')

# Generated at 2022-06-13 15:15:34.606274
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_module = StrategyModule('tqm')
    assert strategy_module._host_pinned == True

# Generated at 2022-06-13 15:15:35.786854
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    s = StrategyModule(None)
    assert s._host_pinned

# Generated at 2022-06-13 15:15:37.184899
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    sm = StrategyModule('tqm')
    assert sm._host_pinned is True

# Generated at 2022-06-13 15:15:37.684217
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
	pass

# Generated at 2022-06-13 15:15:38.236886
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True

# Generated at 2022-06-13 15:15:39.593880
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # Test constructor and class variables
    s = StrategyModule(None)
    assert s._batch_size == 0

# Generated at 2022-06-13 15:15:40.538189
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule(None)._host_pinned == True

# Generated at 2022-06-13 15:15:41.743902
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass

# vim: ai ts=4 sw=4 et sts=4 ft=python

# Generated at 2022-06-13 15:15:42.690188
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy = StrategyModule('tqm')
    assert strategy._host_pinned == True

# Generated at 2022-06-13 15:15:46.859799
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    import ansible.plugins
    import ansible.plugins.loader
    from ansible.plugins.strategy import StrategyModule

    ansible.plugins.loader.add_directory('./ansible/plugins')
    strategy = ansible.plugins.strategy_loader.get('host_pinned', None)
    assert isinstance(strategy, StrategyModule)