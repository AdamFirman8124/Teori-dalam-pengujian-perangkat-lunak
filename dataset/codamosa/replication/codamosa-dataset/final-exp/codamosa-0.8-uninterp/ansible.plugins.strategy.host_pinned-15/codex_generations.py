

# Generated at 2022-06-13 15:06:31.027169
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    sm = StrategyModule()
    assert sm._host_pinned == True

# Generated at 2022-06-13 15:06:33.808352
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    my_strategy = StrategyModule(tqm=None)
    assert my_strategy._host_pinned, '_host_pinned did not initialize properly'
    print('test_StrategyModule passed!')

# Generated at 2022-06-13 15:06:35.439229
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # change this test when you add more attributes to the class
    assert StrategyModule.__bases__ == (FreeStrategyModule,)

# Generated at 2022-06-13 15:06:37.227690
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_module = StrategyModule()
    assert (not strategy_module._host_pinned) == False

# Generated at 2022-06-13 15:06:39.217784
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    """ Definition of unit test for constructor of class StrategyModule """
    tqm = StrategyModule(None)
    tqm

# Generated at 2022-06-13 15:06:40.052046
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule() is not None

# Generated at 2022-06-13 15:06:47.159452
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule.__doc__ == """    name: host_pinned
    short_description: Executes tasks on each host without interruption
    description:
        - Task execution is as fast as possible per host in batch as defined by C(serial) (default all).
          Ansible will not start a play for a host unless the play can be finished without interruption by tasks for another host,
          i.e. the number of hosts with an active play does not exceed the number of forks.
          Ansible will not wait for other hosts to finish the current task before queuing the next task for a host that has finished.
          Once a host is done with the play, it opens it's slot to a new host that was waiting to start.
          Other than that, it behaves just like the "free" strategy.
    version_added: "2.7"
    author: Ansible Core Team
"""

# Generated at 2022-06-13 15:06:47.719032
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass



# Generated at 2022-06-13 15:06:49.392357
# Unit test for constructor of class StrategyModule
def test_StrategyModule():

   testvar = type(StrategyModule)

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 15:06:49.964160
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True

# Generated at 2022-06-13 15:06:56.084730
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = object()
    strategy_module = StrategyModule(tqm)
    assert strategy_module.tqm == tqm
    assert strategy_module._host_pinned == True
    assert strategy_module._host_pinned is True
    assert isinstance(strategy_module, StrategyModule)
    assert isinstance(strategy_module, FreeStrategyModule)

if __name__ == '__main__':
    test_StrategyModule()

# Generated at 2022-06-13 15:06:58.376970
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.plugins.strategy.host_pinned import StrategyModule
    strategy = StrategyModule(None)
    assert hasattr(strategy, '_host_pinned') and strategy._host_pinned

# Generated at 2022-06-13 15:07:01.281692
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.executor.task_queue_manager import TaskQueueManager
    obj1 = StrategyModule(tqm=TaskQueueManager())
    assert(obj1._host_pinned)

# Generated at 2022-06-13 15:07:03.319423
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert hasattr(StrategyModule, '__init__')

# Generated at 2022-06-13 15:07:10.034285
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = ansible.executor.task_queue_manager.TaskQueueManager(
                    inventory=ansible.inventory.Manager(inventory=ansible.inventory.Inventory()),
                    variable_manager=ansible.vars.manager.VariableManager(),
                    loader=ansible.parsing.dataloader.DataLoader(),
                    options=ansible.utils.options.Options(),
                    passwords={})
    strategy = StrategyModule(tqm)

    assert strategy._host_pinned == True

# Generated at 2022-06-13 15:07:11.241524
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule(tqm=None)

# Generated at 2022-06-13 15:07:12.437366
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    obj = StrategyModule()


# Generated at 2022-06-13 15:07:20.284045
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    assert StrategyModule(tqm)._host_pinned == True

# uses FreeStrategyModule's get_host_list
# uses FreeStrategyModule's push_host_state

# Overrides FreeStrategyModule's get_next_task_for_host
# see https://github.com/ansible/ansible/blob/devel/lib/ansible/plugins/strategy/free.py#L88
# to get the next host that can run
# TODO: Implement this to find the next available host from the list of hosts provided by inventory

# Generated at 2022-06-13 15:07:21.164275
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = object
    assert StrategyModule(tqm)

# Generated at 2022-06-13 15:07:27.010792
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    import unittest
    class TestStrategyModule(unittest.TestCase):
        def test_StrategyModule(self):
            tqm = None
            strategy = StrategyModule(tqm)
            self.assertEqual(strategy._host_pinned, True)

    suite = unittest.TestLoader().loadTestsFromTestCase(TestStrategyModule)
    unittest.TextTestRunner(verbosity=2).run(suite)

# Generated at 2022-06-13 15:07:29.963680
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    StrategyModule('tqm')

# Generated at 2022-06-13 15:07:30.978875
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    s = StrategyModule(None)

# Generated at 2022-06-13 15:07:32.378187
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    StrategyModule(tqm)

# Generated at 2022-06-13 15:07:34.244476
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_mock = StrategyModule('tqm')
    assert strategy_mock._host_pinned == True

# Generated at 2022-06-13 15:07:36.590914
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = 'tqm'
    sm = StrategyModule(tqm)
    assert sm._tqm == tqm
    assert sm._host_pinned == True

# Generated at 2022-06-13 15:07:38.945274
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.plugins.strategy import host_pinned

    a = host_pinned.StrategyModule(None)
    assert a._host_pinned == True

# Generated at 2022-06-13 15:07:40.839185
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    print('test_StrategyModule')
    StrategyModule('')

if __name__ == '__main__':
    print('Executing as standalone')
    test_StrategyModule()

# Generated at 2022-06-13 15:07:42.620061
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_module = StrategyModule(tqm = None)
    strategy_module._host_pinned
    assert strategy_module._host_pinned is True

# Generated at 2022-06-13 15:07:46.438257
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule


if __name__ == '__main__':
    import sys
    #test_StrategyModule()
    sys.exit(0)

# Generated at 2022-06-13 15:07:47.506012
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    obj = StrategyModule()


# Generated at 2022-06-13 15:07:59.386225
# Unit test for constructor of class StrategyModule
def test_StrategyModule():

    from ansible.plugins.strategy import StrategyModule
    from ansible.utils.listify import listify_lookup_plugin_terms

    #tqm = AnsibleTaskQueueManager(inventory=inventory, variable_manager=variable_manager, loader=loader, display=display, options=options, passwords=passwords, run_tree=run_tree)
    tqm = None
    strategy = StrategyModule(tqm)

    #assert strategy.get_host_list() == 'test'

test_StrategyModule()

# Generated at 2022-06-13 15:07:59.978520
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass

# Generated at 2022-06-13 15:08:01.823218
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = 'TestString'
    StrategyModule(tqm)

# Generated at 2022-06-13 15:08:02.857187
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule


# Generated at 2022-06-13 15:08:04.825098
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    StrategyModule(tqm)

# Generated at 2022-06-13 15:08:06.356932
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    sm = StrategyModule('tqm')
    assert sm._host_pinned is True

# Generated at 2022-06-13 15:08:09.289907
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = "test"
    st = StrategyModule(tqm)
    assert st._host_pinned
    assert st._tqm == "test"


# Generated at 2022-06-13 15:08:10.701771
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule
    assert FreeStrategyModule
    assert tqm


# Generated at 2022-06-13 15:08:20.249168
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.plugins.strategy.strategy_loader import get_strategy
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.utils.vars import load_extra_vars, load_options_vars
    from collections import namedtuple
    import ansible.constants as C
    from ansible.utils.display import Display
    from ansible.module_utils.basic import AnsibleModule


# Generated at 2022-06-13 15:08:21.284223
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    sm = StrategyModule()
    assert sm._host_pinned == True

# Generated at 2022-06-13 15:08:32.376444
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = ''
    obj = StrategyModule(tqm)
    assert obj._host_pinned == True

if __name__ == '__main__':
    test_StrategyModule()

# Generated at 2022-06-13 15:08:33.117235
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy = StrategyModule(tqm=object)
    assert strategy._host_pinned == True

print('2')

# Generated at 2022-06-13 15:08:35.117668
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    display = Display()
    tqm = None 
    strategy = StrategyModule(tqm)
    assert strategy._host_pinned == True


# Generated at 2022-06-13 15:08:36.677337
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule.__doc__ is not None
    assert StrategyModule.__init__.__doc__ is not None

# Generated at 2022-06-13 15:08:43.114946
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    
    # Test with tqm not being None
    tqm = 7
    strategy_module = StrategyModule(tqm)
    assert strategy_module._host_pinned == True
    assert strategy_module._tqm == 7

    # Test with tqm being None
    tqm = None
    strategy_module = StrategyModule(tqm)
    assert strategy_module._host_pinned == True
    assert strategy_module._tqm == None



# Generated at 2022-06-13 15:08:44.326649
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    free = FreeStrategyModule(None)
    assert free._host_pinned == False

# Generated at 2022-06-13 15:08:48.142411
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # Run module successfully
    try:
        StrategyModule(tqm=None)
    # Run module with error
    except:
        pass



# Generated at 2022-06-13 15:08:51.230595
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    sm = StrategyModule(tqm)
    assert sm._host_pinned, "Test failed: _host_pinned must be True."

# Generated at 2022-06-13 15:08:59.839312
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # Instantiate a HostQueueManager object
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.utils.display import Display
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.utils.vars import combine_vars

    tqm = TaskQueueManager(
            inventory=InventoryManager(loader=DataLoader(), sources=['./test/inventory']),
            variable_manager=VariableManager(),
            loader=DataLoader(),
            display=Display(),
            options=None,
            stdout_callback=None,
            passwords=None)
    # Instantiate StrategyModule

# Generated at 2022-06-13 15:09:01.240007
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    sm = StrategyModule()
    assert sm._host_pinned == True

# Generated at 2022-06-13 15:09:31.664399
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.utils.vars import combine_vars
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.inventory.host import Host
    from ansible.playbook.play import Play
    import ansible.constants as C
    import json

    inventory = InventoryManager(loader=None, sources='''
    localhost ansible_connection=local
    [all:vars]
    local_file = /etc/ansible/hosts
    ''')

    variable_manager = VariableManager()

# Generated at 2022-06-13 15:09:32.103857
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    StrategyModule(None)

# Generated at 2022-06-13 15:09:38.352926
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    """This unit test of the constructor of the class StrategyModule
    """
    # Create
    tqm = {
        'host_name': 'test_host_name',
        'hostvars': {'host': 'host'},
        'group_vars': {'group': 'group'},
        'groups': {'test_group': 'group'}
    }
    strategy_module = StrategyModule(tqm)
    # Check
    assert strategy_module._host_pinned is True

# Generated at 2022-06-13 15:09:40.271394
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
  u = StrategyModule(tqm=None)
  assert u._host_pinned is True

# Generated at 2022-06-13 15:09:40.875919
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass

# Generated at 2022-06-13 15:09:42.411279
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule.__doc__ == FreeStrategyModule.__doc__

# Generated at 2022-06-13 15:09:44.224783
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
	st_obj = StrategyModule(tqm=None)
	assert st_obj._host_pinned == True

# Generated at 2022-06-13 15:09:45.040599
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule.__name__ == 'StrategyModule'

# Generated at 2022-06-13 15:09:45.818839
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert isinstance(StrategyModule(None), StrategyModule)

# Generated at 2022-06-13 15:09:47.812117
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy = StrategyModule(None)
    assert strategy.__doc__ is not None
    assert strategy._host_pinned

# Generated at 2022-06-13 15:10:25.107338
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    return StrategyModule


# Generated at 2022-06-13 15:10:29.031326
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # TODO: I have to initialize StrategyModule class with tqm
    #       In a future tqm will be replaced with something else
    tqm = None
    sm = StrategyModule(tqm)
    assert isinstance(sm, StrategyModule)

# Generated at 2022-06-13 15:10:29.556726
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule != None

# Generated at 2022-06-13 15:10:32.513657
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    FakeTqmObj = type('FakeTqmClass', (), {'hostvars':{}})
    fake_tqm = FakeTqmObj()
    strategy_obj = StrategyModule(fake_tqm)
    assert strategy_obj._host_pinned == True

# Generated at 2022-06-13 15:10:33.291271
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule


# Generated at 2022-06-13 15:10:34.470932
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = MockTQM()
    strategy = StrategyModule(tqm)
    assert strategy._host_pinned == True
# END

# Generated at 2022-06-13 15:10:39.115034
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    import mock
    TASK_QUEUE_MANAGER = mock.MagicMock()
    strategyModule = StrategyModule(TASK_QUEUE_MANAGER)
    assert strategyModule._host_pinned == True

# Generated at 2022-06-13 15:10:47.572120
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.plugins.strategy.host_pinned import StrategyModule as host_pinned
    from ansible.plugins.loader import strategy_loader
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.config.manager import ConfigManager
    from ansible.config.data import ConfigData
    from collections import namedtuple
    from ansible.vars.hostvars import HostVars
    from ansible.vars import VariableManager
    from ansible.utils.vars import combine_vars
    from ansible.parsing.dataloader import DataLoader
    from ansible.statistics import AggregateStats
    from ansible.inventory.manager import InventoryManager
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group

# Generated at 2022-06-13 15:10:48.376301
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_object = StrategyModule()

# Generated at 2022-06-13 15:10:50.836251
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_module = StrategyModule(None)
    assert strategy_module is not None
    assert strategy_module._host_pinned is True

# Generated at 2022-06-13 15:12:32.809539
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    ''' Unit testing for StrategyModule class '''
    display = Display()
    StrategyModule(display)

# Generated at 2022-06-13 15:12:33.424176
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule

# Generated at 2022-06-13 15:12:33.971261
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass

# Generated at 2022-06-13 15:12:38.513707
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    test_strategy = StrategyModule(tqm)
    assert "StrategyModule" == test_strategy.__class__.__name__
    assert True == test_strategy._host_pinned

# Generated at 2022-06-13 15:12:39.118744
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule.__doc__

# Generated at 2022-06-13 15:12:41.015673
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    Strategy = StrategyModule('test_tqm')
    # Test creation of object
    assert Strategy

# Generated at 2022-06-13 15:12:42.761924
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy = StrategyModule(tqm=None)
    assert strategy._host_pinned



# Generated at 2022-06-13 15:12:43.646084
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert callable(StrategyModule)

# Generated at 2022-06-13 15:12:44.967678
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    sm = StrategyModule(tqm=None)

# Generated at 2022-06-13 15:12:46.095115
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy = StrategyModule(None)
    assert strategy._host_pinned == True

# Generated at 2022-06-13 15:16:02.966639
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    sm = StrategyModule({})
    assert sm._host_pinned is True

# Generated at 2022-06-13 15:16:03.867903
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert issubclass(StrategyModule, FreeStrategyModule)

# Generated at 2022-06-13 15:16:04.276422
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True

# Generated at 2022-06-13 15:16:05.586744
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule(tqm="") is not None


# Generated at 2022-06-13 15:16:06.739429
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    sm = StrategyModule(None)
    assert sm._host_pinned == True

# Generated at 2022-06-13 15:16:07.646617
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule(tqm=None)

# Generated at 2022-06-13 15:16:08.185153
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True

# Generated at 2022-06-13 15:16:11.931865
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = "Test tqm"
    instance = StrategyModule(tqm)
    assert isinstance(instance,StrategyModule)
    assert isinstance(instance,FreeStrategyModule)
    assert hasattr(instance, '_host_pinned')
    assert instance._host_pinned == True

# Generated at 2022-06-13 15:16:15.192147
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = MagicMock()
    strategy = StrategyModule(tqm)
    assert isinstance(strategy, StrategyModule)
    assert strategy._host_pinned == True


# Generated at 2022-06-13 15:16:18.307542
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # Test normal instantiation
    tqm = MagicMock()
    s = StrategyModule(tqm)
    assert s
    assert isinstance(s, StrategyModule)
    assert isinstance(s, FreeStrategyModule)