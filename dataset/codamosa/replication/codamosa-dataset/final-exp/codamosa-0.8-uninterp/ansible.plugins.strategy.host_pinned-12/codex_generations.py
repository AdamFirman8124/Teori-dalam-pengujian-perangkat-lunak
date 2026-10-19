

# Generated at 2022-06-13 15:06:39.258285
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    import ansible
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.plugins.strategy import StrategyBase
    from ansible.utils.display import Display
    from ansible.parsing.dataloader import DataLoader

    display = Display()
    loader = DataLoader()
    tqm = TaskQueueManager(
        inventory=None,
        variable_manager=None,
        loader=loader,
        display=display,
        options=None,
        passwords=None,
        stdout_callback=None,
        run_additional_callbacks=True,
        run_tree=False,
        all_vars=dict(),
        subset=None,
    )
    sm = StrategyModule(tqm)

# Generated at 2022-06-13 15:06:41.184312
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    s = StrategyModule(None)
    assert not s._host_pinned


# pylint: disable=unused-argument

# Generated at 2022-06-13 15:06:42.960168
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.utils.display import Display
    from ansible.plugins.strategy.free import StrategyModule as FreeStrategyModule

    assert True

# Generated at 2022-06-13 15:06:44.675759
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass

# Generated at 2022-06-13 15:06:45.628563
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule.__init__ is not None

# Generated at 2022-06-13 15:06:47.718144
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = mock.Mock()
    sm = StrategyModule(tqm)
    assert sm._host_pinned == True

# Generated at 2022-06-13 15:06:48.310848
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass

# Generated at 2022-06-13 15:06:50.785974
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    import __builtin__
    from ansible.plugins.strategy.host_pinned import StrategyModule
    sm = StrategyModule(None)
    assert sm._host_pinned == True

# Generated at 2022-06-13 15:06:52.313346
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    new_strategy_module = StrategyModule("tqm")
    assert new_strategy_module._host_pinned

# Generated at 2022-06-13 15:06:53.923876
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    str = StrategyModule(None)
    assert str._host_pinned

# Generated at 2022-06-13 15:06:56.966224
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert hasattr(StrategyModule, '__init__')
    assert callable(StrategyModule.__init__)

# Test for method _start_task_in_queue

# Generated at 2022-06-13 15:07:00.095103
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = TQM(inventory, variable_manager, loader, options, passwords, stdout_callback=None)
    strategy = StrategyModule(tqm)
    assert strategy is not None

# Generated at 2022-06-13 15:07:04.559034
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    a = StrategyModule("tqm")
    print("type of a is %s" % type(a))
    print("value of a._host_pinned is %s" % a._host_pinned)

test_StrategyModule()

# Generated at 2022-06-13 15:07:05.613042
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule(tqm=None)

# Generated at 2022-06-13 15:07:06.656441
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule('tqm')

# Generated at 2022-06-13 15:07:07.661254
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
   strategy_module = StrategyModule(1)
# Checking the initialized variable to the expected value.
   assert strategy_module._host_pinned == True

# Generated at 2022-06-13 15:07:11.342817
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule
    assert StrategyModule.__doc__

if __name__ == '__main__':
    test_StrategyModule()

# Generated at 2022-06-13 15:07:12.926313
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy = StrategyModule(tqm)
    assert strategy is not None

# Generated at 2022-06-13 15:07:14.791631
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    s= StrategyModule(tqm)
    assert s.get_host_pinned() == True


# Generated at 2022-06-13 15:07:15.786996
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True

# Generated at 2022-06-13 15:07:19.048640
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = {}
    sm = StrategyModule(tqm)
    assert sm._host_pinned == True
    return sm



# Generated at 2022-06-13 15:07:20.899277
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    sm = StrategyModule(None)
    assert sm is not None

# Generated at 2022-06-13 15:07:22.250681
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert(StrategyModule(None))

# Test if StrategyModule is a child of FreeStrategyModule (which has a constructor)

# Generated at 2022-06-13 15:07:22.916613
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    StrategyModule(tqm = None)

# Generated at 2022-06-13 15:07:23.682072
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
   assert StrategyModule.__init__

# Generated at 2022-06-13 15:07:24.286219
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True

# Generated at 2022-06-13 15:07:25.648076
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = "test_queue"
    sm = StrategyModule(tqm)
    assert sm._host_pinned == True

# Generated at 2022-06-13 15:07:26.714501
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule.__name__ == 'StrategyModule'

# Unit test to check name of StrategyModule

# Generated at 2022-06-13 15:07:28.801045
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # Create a StrategyModule object
    strategy_module = StrategyModule(1)
    assert strategy_module._host_pinned == True

# Generated at 2022-06-13 15:07:31.852806
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    class Tqm():
        def __init__(self):
            self.host_pinned = True
    tqm = Tqm()
    strategy_module = StrategyModule(tqm)

# Generated at 2022-06-13 15:07:35.971022
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule

# Generated at 2022-06-13 15:07:38.330710
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
  assert StrategyModule.__name__ == "StrategyModule", "Expected StrategyModule.__name__ to be StrategyModule, got : " + str(StrategyModule.__name__)

# Generated at 2022-06-13 15:07:39.564204
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy = StrategyModule(None)
    assert strategy._host_pinned == True

# Generated at 2022-06-13 15:07:41.775148
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
  from ansible.utils.display import Display
  
  display = Display()
  display.display("Hello World!")
  display.display(dir(display))


# Generated at 2022-06-13 15:07:42.292641
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True

# Generated at 2022-06-13 15:07:46.509793
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    obj_strat_mod = StrategyModule()
    assert type(obj_strat_mod) == StrategyModule
    assert obj_strat_mod._host_pinned == True

# Generated at 2022-06-13 15:07:48.893286
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    free = StrategyModule()
    strategy = StrategyModule()
    assert strategy is not None
    assert strategy != free

# Generated at 2022-06-13 15:07:49.333086
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True

# Generated at 2022-06-13 15:07:50.669921
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    a = StrategyModule("test")
    assert a._host_pinned == True

# Generated at 2022-06-13 15:07:53.002240
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    strategy_module = StrategyModule(tqm)
    strategy_module.__init__(tqm)

# Generated at 2022-06-13 15:08:06.452858
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.plugins.strategy.host_pinned import StrategyModule
    from ansible.executor.task_queue_manager import TaskQueueManager
    tqm = TaskQueueManager(None, None)
    strategy_module = StrategyModule(tqm)
    assert strategy_module._host_pinned == True

# Generated at 2022-06-13 15:08:08.570163
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert hasattr(StrategyModule, '__init__')

# test public methods

# Generated at 2022-06-13 15:08:10.792514
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    s = StrategyModule(tqm)
    assert s._host_pinned == True

# ---- END ----

# Generated at 2022-06-13 15:08:12.598770
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    strategy_m = StrategyModule(tqm)
    print("Strategy Module: " + strategy_m.__class__.__name__)


# Generated at 2022-06-13 15:08:15.217366
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule.__module__ == "ansible.plugins.strategy.host_pinned"
    assert StrategyModule.__name__ == "StrategyModule"


# Generated at 2022-06-13 15:08:17.850400
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    display.verbosity = 3
    obj = StrategyModule(None)
    assert isinstance(obj, StrategyModule)
    assert isinstance(obj._host_pinned, bool)
    assert obj._host_pinned is True

# Generated at 2022-06-13 15:08:18.702355
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    mod = StrategyModule("test")

# Generated at 2022-06-13 15:08:19.513227
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule

# Generated at 2022-06-13 15:08:20.012099
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True

# Generated at 2022-06-13 15:08:21.125852
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    test = StrategyModule("test")
    assert(test._host_pinned == True)

# Generated at 2022-06-13 15:08:39.075137
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule(None)._host_pinned 
    

# Generated at 2022-06-13 15:08:40.816108
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    st = StrategyModule(tqm="tqm")
    assert st._host_pinned is True

# Generated at 2022-06-13 15:08:52.158568
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.plugins.strategy.host_pinned import StrategyModule
    from ansible.plugins.strategy import ActionModule
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.vars.manager import VariableManager

    tqm = TaskQueueManager(
        inventory=dict(hosts={}),
        variable_manager=VariableManager(loader=dict(host_vars={})),
        loader=dict(playbooks=[], host_vars={})
    )
    strategy = StrategyModule(tqm)
    assert strategy.__class__.__name__ == 'StrategyModule'
    assert issubclass(StrategyModule, ActionModule)
    assert isinstance(strategy, ActionModule)
    assert strategy._tqm == tqm

# Generated at 2022-06-13 15:08:56.778031
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    object1 = dict()
    object2 = dict()
    object2['tqm'] = object1

    strategy_module = StrategyModule(object1)
    assert strategy_module.tqm == object2['tqm']
    assert strategy_module._current_serial_failure_count == {}
    assert strategy_module._current_serial_ok_count == {}
    assert strategy_module._display is not None

# Generated at 2022-06-13 15:08:58.076003
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    sm = StrategyModule(tqm=None)
    assert sm._host_pinned == False

# Generated at 2022-06-13 15:08:59.075699
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    '''
    Unit test for StrategyModule
    '''
    pass
# Test StrategyModule

# Generated at 2022-06-13 15:09:00.547512
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert issubclass(StrategyModule, FreeStrategyModule)
    x = StrategyModule(None)
    assert x._host_pinned == True

# Generated at 2022-06-13 15:09:02.926540
# Unit test for constructor of class StrategyModule

# Generated at 2022-06-13 15:09:04.099917
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    assert StrategyModule(tqm)

# Generated at 2022-06-13 15:09:08.198205
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.plugins.strategy import StrategyModule
    from ansible.plugins.strategy.host_pinned import StrategyModule as HostPinnedStrategyModule
    tqm = None
    sm = StrategyModule(tqm)
    assert sm._host_pinned is False
    sm = HostPinnedStrategyModule(tqm)
    assert sm._host_pinned is True

# Generated at 2022-06-13 15:09:52.669809
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule

if __name__ == '__main__':
    test_StrategyModule()

# Generated at 2022-06-13 15:09:53.227376
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass

# Generated at 2022-06-13 15:09:56.783300
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    print("Testing constructor of class StrategyModule")
    tqm = object
    strategy = StrategyModule(tqm)
    print("Constructor of class StrategyModule successfull")

# Unit test of function of class StrategyModule

# Generated at 2022-06-13 15:09:57.897582
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule


# Generated at 2022-06-13 15:10:03.561895
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # Use a fake task queue manager
    tqm = 'fake_tqm'
    # Instantiate the strategy module
    strategy = StrategyModule(tqm)
    # Test the strategy module (expected outcome)
    expected = True
    # Test the strategy module (actual outcome)
    actual = isinstance(strategy, StrategyModule)
    # Test the equality of the expected and actual outcomes
    assert expected == actual

# Generated at 2022-06-13 15:10:07.905971
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    display.verbosity = 3
    tqm = MagicMock()
    tqm.send_callback.return_value = True
    s = StrategyModule(tqm)
    assert s._host_pinned is True
    assert s.get_host_list() == ['localhost']
    s.add_host('test')
    assert s.get_host_list() == ['localhost', 'test']



# Generated at 2022-06-13 15:10:09.094511
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    strg = StrategyModule(tqm)
    assert strg._host_pinned == True

# Generated at 2022-06-13 15:10:09.867975
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    sm = StrategyModule(1)
    assert sm._host_pinned == True

# Generated at 2022-06-13 15:10:10.940426
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    sm = StrategyModule(tqm=None)
    assert sm._host_pinned is True


# Generated at 2022-06-13 15:10:14.536692
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    host_pinned_object = StrategyModule("Ansible")
    assert host_pinned_object._host_pinned == True
    assert host_pinned_object._step_return is None

# Generated at 2022-06-13 15:11:51.230623
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = "tqm"
    strategy = StrategyModule(tqm)
    assert strategy is not None
    assert strategy._host_pinned is True
    assert strategy._tqm is tqm

# Generated at 2022-06-13 15:11:53.032622
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    #TODO: create a test that makes sure that constructor works
    pass

# Generated at 2022-06-13 15:11:53.878482
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert type(StrategyModule) == type

# Generated at 2022-06-13 15:11:54.683446
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule.__name__ == 'StrategyModule'

# Generated at 2022-06-13 15:11:55.777629
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
  strategy = StrategyModule(tqm)
  assert strategy._host_pinned

# Generated at 2022-06-13 15:11:57.508629
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = 'test_tqm'
    strategy = StrategyModule(tqm)
    assert strategy._host_pinned == True

# Generated at 2022-06-13 15:11:59.508680
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    """
    Test constructor of class StrategyModule
    """
    tqm_obj = ('tqm')
    StrategyModule(tqm_obj)



# Generated at 2022-06-13 15:11:59.957637
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass

# Generated at 2022-06-13 15:12:00.694894
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule(0)._host_pinned

# Generated at 2022-06-13 15:12:02.445805
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    """
    Unit test for constructor of class StrategyModule
    """
    tqm = None
    sm = StrategyModule(tqm)
    assert sm._host_pinned

# Generated at 2022-06-13 15:15:16.334893
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy = StrategyModule("test")
    assert(strategy._host_pinned)

# Generated at 2022-06-13 15:15:17.089240
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule is not None

# Generated at 2022-06-13 15:15:18.667531
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy = StrategyModule("tqm")
    assert strategy._host_pinned

if __name__ == '__main__':
    test_StrategyModule()

# Generated at 2022-06-13 15:15:20.172976
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    result = StrategyModule(tqm)
    assert result._host_pinned == True

# Generated at 2022-06-13 15:15:22.328500
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    stc = StrategyModule(tqm)
    assert stc._display==Display()
    assert stc._tqm==tqm
    assert stc._host_pinned

# Generated at 2022-06-13 15:15:24.515001
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = object()
    strategy = StrategyModule(tqm)
    assert strategy._host_pinned == True

# Generated at 2022-06-13 15:15:29.127280
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.plugins.strategy.host_pinned import StrategyModule
    from ansible.executor.task_queue_manager import TaskQueueManager
    tqm = TaskQueueManager(None, None, None, None, None)
    StrategyModule(tqm)

# Make sure the names are correct
test_StrategyModule()

# Generated at 2022-06-13 15:15:30.710018
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert 'Ansible' in StrategyModule(tqm)

# Generated at 2022-06-13 15:15:31.243329
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass

# Generated at 2022-06-13 15:15:35.077115
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.plugins.strategy.host_pinned import StrategyModule
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.utils.display import Display
    from ansible.plugins.loader import plugin_loader
    import ansible.context
    from ansible.config.manager import ConfigManager

    options = plugin_loader.load_options(
        config=dict(config_manager=ConfigManager(['/etc/ansible/ansible.cfg'])),
        variables=dict(context=ansible.context)
        )
