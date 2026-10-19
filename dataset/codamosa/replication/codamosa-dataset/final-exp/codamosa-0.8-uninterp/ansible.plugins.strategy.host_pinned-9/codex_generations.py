

# Generated at 2022-06-13 15:06:30.082873
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True

# Generated at 2022-06-13 15:06:31.727762
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_module = StrategyModule(tqm)
    assert strategy_module._host_pinned == True

# Generated at 2022-06-13 15:06:32.235405
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    StrategyModule(1)

# Generated at 2022-06-13 15:06:33.403615
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule('task_queue_manager') != None


# Generated at 2022-06-13 15:06:42.693031
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    s = FreeStrategyModule(tqm=None)
    # assert(s.__len__() == 6)
    s._tqm = 10
    s._inventory = ''
    s._variables = ''
    s._loader = ''
    s._final_q = ''
    s._blocked_hosts = ''
    s._workers = ''
    s.pause = ''
    s.module_name = ''
    s._queue_empty = ''
    s._max_workers = ''
    s._host_pinned = True
    s.queue_error = ''
    s.default_q = ''
    s.test = ''
    s.display = ''
    s.inventory = ''
    s.loader = ''
    s.variable_manager = ''
    s.play = ''
    s.remote_user

# Generated at 2022-06-13 15:06:44.800679
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    test_success_tqm = 'test_success'
    strategy_module = StrategyModule(test_success_tqm)
    assert strategy_module._host_pinned == True


# Generated at 2022-06-13 15:06:46.096420
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    StrategyModule(tqm)

# Generated at 2022-06-13 15:06:47.808568
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = {}
    sm = StrategyModule(tqm)
    assert sm._host_pinned is True

# Generated at 2022-06-13 15:06:54.100342
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from units.mock.loader import DictDataLoader
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor

    loader = DictDataLoader({
        "hosts": [
            {
                "hostname": "host1",
            }
        ]
    })

    inventory = Inventory(
        loader=loader,
        variable_manager=VariableManager(),
        host_list=['host1'],
    )

    playbook = PlaybookExecutor(
        playbooks=['playbooks/playbook.yml'],
        inventory=inventory,
        variable_manager=VariableManager(),
        loader=loader,
    )
    tqm = Task

# Generated at 2022-06-13 15:06:59.201426
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
  class TestClass:
    def __init__(self):
      self.callbacks = None
      self.stats = None
      self.hostvars = None
  tqm = TestClass()
  s = StrategyModule(tqm)
  assert s._host_pinned is True

if __name__ == '__main__':
  test_StrategyModule()

# Generated at 2022-06-13 15:07:01.827969
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy = StrategyModule(tqm=None)
    assert strategy
    assert strategy._host_pinned is True

# Generated at 2022-06-13 15:07:07.283210
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    import ansible.plugins.strategy.host_pinned
    strategy_module = ansible.plugins.strategy.host_pinned.StrategyModule('1')
    assert strategy_module != None

    print(strategy_module._host_pinned)
    assert strategy_module._host_pinned == True

# Generated at 2022-06-13 15:07:13.281883
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    """
        This testcase is used to test the constructor of the class StrategyModule
    """
    from ansible.executor.task_queue_manager import TaskQueueManager

    tqm = TaskQueueManager(None, None, None, None, None, None, None, None)
    strategy = StrategyModule(tqm)

# Generated at 2022-06-13 15:07:17.335294
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule.__name__ == 'StrategyModule'
    assert StrategyModule.__init__.__name__ == '__init__'
    assert StrategyModule.__module__ == 'ansible.plugins.strategy.host_pinned'
    assert StrategyModule.__bases__[0] == FreeStrategyModule
    assert StrategyModule.__dict__['_host_pinned'] == True

# Generated at 2022-06-13 15:07:18.064772
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    a = StrategyModule(tqm)



# Generated at 2022-06-13 15:07:19.196440
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    sm = StrategyModule(True)
    assert isinstance(sm, StrategyModule)
    assert sm._host_pinned == True

# Generated at 2022-06-13 15:07:24.960860
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.plugins.strategy import StrategyModule
    from ansible.plugins.loader import strategy_loader

    strategy = strategy_loader.get("host_pinned", None)
    print("Testing Strategy = %s" % strategy)

    # TODO: figure out how to initialize play_context for StrategyModule, for now we can only test constructor
    strategy.__init__("tqm")

# Generated at 2022-06-13 15:07:29.281353
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    testTqm = object
    testStrategy = StrategyModule(testTqm)
    assert len(testStrategy.tqm.queue) == 0
    assert testStrategy.tqm._final_q.qsize() == 0
    assert testStrategy._display.verbosity == 3
    assert testStrategy.batch_size == 1
    assert testStrategy.pending_results == 0
    assert testStrategy._host_pinned == True

# Generated at 2022-06-13 15:07:31.264743
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    sm = FreeStrategyModule(None)
    assert isinstance(sm, FreeStrategyModule)

# Generated at 2022-06-13 15:07:40.637422
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.playbook.play import Play
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.task_queue_manager import TaskQueueManager

    loader = DataLoader()
    play = Play.load(dict(name="test play", hosts="localhost", gather_facts="no", tasks=""), loader=loader)
    host = play.get_variable_manager().get_vars().get("inventory_hostname")
    queue = [dict(host=host, task=play.get_tasks()[0])]
    tasks = [dict(action=dict(module='debug', args=dict(msg='sdkf')))]
    play.set_tasks(tasks)


# Generated at 2022-06-13 15:07:43.186499
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True

# Generated at 2022-06-13 15:07:45.889637
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    await1 = StrategyModule(None)

# Generated at 2022-06-13 15:07:47.967617
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = object
    sm = StrategyModule(tqm)
    assert sm._host_pinned

# Generated at 2022-06-13 15:07:50.148251
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm  = TQM()
    sm = StrategyModule(tqm)
    assert sm._host_pinned

# Generated at 2022-06-13 15:07:52.550176
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # Test function for Strategy class, for now only for constructor.
    # Create a fake task queue manager
    from ansible.executor.task_queue_manager import TaskQueueManager
    tqm = TaskQueueManager(None)
    sm = StrategyModule(tqm)
    assert sm._host_pinned is True

# Generated at 2022-06-13 15:07:59.688047
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.plugins.strategy.host_pinned import StrategyModule
    from ansible.plugins.strategy import PLUGIN_LOADER
    PLUGIN_LOADER.set_options(None)
    PLUGIN_LOADER.set_global_vars(None)
    strategy = StrategyModule(None)
    assert strategy is not None
    assert strategy.__class__.__name__ is not None
    assert strategy._host_pinned is True

# Generated at 2022-06-13 15:08:03.265522
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule.__name__ == "StrategyModule"
    assert StrategyModule.__doc__ == "StrategyModule"
    # assert StrategyModule.__dict__ == dict(StrategyModule)

# Generated at 2022-06-13 15:08:06.005176
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert getattr(StrategyModule, '__init__') != getattr(FreeStrategyModule, '__init__')

# Generated at 2022-06-13 15:08:08.105627
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    s = StrategyModule(tqm = {})
    assert s._host_pinned == True

# Generated at 2022-06-13 15:08:09.133994
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule(None)._host_pinned

# Generated at 2022-06-13 15:08:15.014602
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy = StrategyModule('tqm')
    display.display(strategy._host_pinned)

# test_StrategyModule()

# Generated at 2022-06-13 15:08:15.762286
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule

# Generated at 2022-06-13 15:08:16.294659
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule

# Generated at 2022-06-13 15:08:20.723123
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.plugins.strategy.host_pinned import StrategyModule
    from ansible.plugins.strategy import StrategyBase
    from ansible.config.manager import ConfigManager
    c = ConfigManager()
    tqm = type('tqm', (object,), {'_options':c})()
    strategy = StrategyModule(tqm)
    assert isinstance(strategy, StrategyBase.StrategyBase)

# Generated at 2022-06-13 15:08:22.424108
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # test strategy module constructor
    strategy_module = StrategyModule("test_strategy_module")
    assert strategy_module._host_pinned == True

test_StrategyModule()

# Generated at 2022-06-13 15:08:25.137298
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
      assert(StrategyModule.__name__ == "StrategyModule")
      assert(StrategyModule.__init__())

# Generated at 2022-06-13 15:08:28.955495
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    StrategyModule(tqm=None)

if __name__ == '__main__':
    # Unit test for constructor of class StrategyModule
    test_StrategyModule()

# Generated at 2022-06-13 15:08:29.610428
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    StrategyModule(42)

# Generated at 2022-06-13 15:08:30.656848
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass



# Generated at 2022-06-13 15:08:32.614049
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert (StrategyModule.__name__ == 'StrategyModule')

# Generated at 2022-06-13 15:08:44.088740
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    import mock
    tqm = mock.MagicMock()
    fsm = FreeStrategyModule(tqm)
    sm = StrategyModule(tqm)
    assert sm._tqm is tqm
    assert sm._host_pinned is True
    assert sm._batch_size == 1
    assert fsm._batch_size == 1

# Generated at 2022-06-13 15:08:46.681778
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    m = StrategyModule()
    assert m._host_pinned

# Generated at 2022-06-13 15:08:48.455178
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_obj = StrategyModule(tqm=None)
    assert isinstance(strategy_obj, StrategyModule)

# Generated at 2022-06-13 15:08:51.187524
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    strategy = StrategyModule(tqm)
    assert strategy._host_pinned



# Generated at 2022-06-13 15:08:53.929564
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = 1
    s = StrategyModule(tqm)
    assert s._tqm == tqm
    assert s._batch_size == 0
    assert s._play_context.serial == 0
    assert s._workers == dict()

# Generated at 2022-06-13 15:08:54.957257
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
	assert StrategyModule.__name__ == "StrategyModule"

# Generated at 2022-06-13 15:08:55.790158
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass

# Unit test without pytest

# Generated at 2022-06-13 15:09:02.504172
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    class FakeTqm(object):
        def __init__(self, module, tqm_util, loader, variable_manager, inventory, options, stdout_callback):
            self.module = module
            self.tqm_util = tqm_util
            self.loader = loader
            self.variable_manager = variable_manager
            self.inventory = inventory
            self.options = options
            self.stdout_callback = stdout_callback

    tqm = FakeTqm(
        module = None,
        tqm_util = None,
        loader = None,
        variable_manager = None,
        inventory = None,
        options = None,
        stdout_callback = None
    )
    strategy = StrategyModule(tqm)
    assert strategy._host_pinned == True

# Unit test

# Generated at 2022-06-13 15:09:03.005260
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass

# Generated at 2022-06-13 15:09:11.032384
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    global t
    global display
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.inventory.group import Group
    from ansible.inventory.host import Host
    from ansible.playbook.play import Play
    from ansible.playbook.playbook import Playbook
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    import os

    class Test:
        def __init__(self):
            self._host_pinned = True

    loader = DataLoader()
   

# Generated at 2022-06-13 15:09:33.314125
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass

# Generated at 2022-06-13 15:09:35.298928
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    host = StrategyModule(tqm)
    assert host.__class__.__name__ == 'StrategyModule'

# Generated at 2022-06-13 15:09:36.391515
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass

# Generated at 2022-06-13 15:09:37.008856
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass

# Generated at 2022-06-13 15:09:38.200845
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategymodule = StrategyModule()
    assert strategymodule._host_pinned


# Generated at 2022-06-13 15:09:47.140403
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    import sys
    import os
    import unittest
    import mock
    sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
    from strategy_plugins import host_pinned

    class TestDisplay(unittest.TestCase):
        def test_strategy_module(self):
            with mock.patch.object(host_pinned.display, 'verbosity', 0):
                tqm = mock.MagicMock()
                tqm._final_q = None
                tqm._initial_q = None
                tqm.send_callback.side_effect = None
                obj = host_pinned.StrategyModule(tqm)
                obj._host_pinned = True
                self.assertTrue(obj._host_pinned)


# Generated at 2022-06-13 15:09:48.378102
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy = StrategyModule()
    assert(strategy._host_pinned)

# Generated at 2022-06-13 15:09:50.227551
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    s = StrategyModule()
    assert '_host_pinned' in s.__dict__
    assert '_tqm' in s.__dict__

# Generated at 2022-06-13 15:09:51.592790
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    fsm = StrategyModule(None)
    assert not fsm._host_pinned

# Generated at 2022-06-13 15:09:52.128816
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass

# Generated at 2022-06-13 15:10:32.477158
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy = 'host_pinned'
    variables = {}
    display.verbosity = 4
    try:
        if StrategyModule(strategy, variables, display)._host_pinned == True:
            print('SUCCESS')
            return True
        else:
            print('FAILURE')
            return False
    except:
        print('FAILURE')
        return False

if __name__ == '__main__':
    test_StrategyModule()

# Generated at 2022-06-13 15:10:33.789895
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    module = StrategyModule(tqm="tqm_value")
    assert module._host_pinned == True

# Generated at 2022-06-13 15:10:35.207455
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
  strategy_module = StrategyModule(object)
  strategy_module._host_pinned == True

# Generated at 2022-06-13 15:10:37.280633
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule.__doc__ is not None

# Generated at 2022-06-13 15:10:38.416962
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule.__init__

# Generated at 2022-06-13 15:10:39.566279
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule(None)

# Generated at 2022-06-13 15:10:41.382807
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy = StrategyModule(tqm=None)
    assert strategy._host_pinned

# Generated at 2022-06-13 15:10:43.658162
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategyModule = StrategyModule(tqm=None)
    assert strategyModule._host_pinned

if __name__ == '__main__':
    test_StrategyModule()

# Generated at 2022-06-13 15:10:45.969083
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from collections import namedtuple
    FakeTQM = namedtuple('FakeTQM', ('host_pinned'))
    FakeTQM.host_pinned = True
    assert StrategyModule(FakeTQM)._host_pinned == True

# Generated at 2022-06-13 15:10:46.474025
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    StrategyModule(None)

# Generated at 2022-06-13 15:12:28.303894
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule is not None


# Generated at 2022-06-13 15:12:35.425228
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.plugins.strategy import StrategyModule
    from ansible.playbook.play import Play
    import ansible.utils
    class TestTQM(object):
        def __init__(self):
            self.inventory = ansible.utils.parse_yaml("""
                all:
                    children:
                        group1:
                            hosts:
                                localhost:
                                    ansible_connection: local
                        group2:
                            hosts:
                                localhost:
                                    ansible_connection: local
                """)
    tqm = TestTQM()
    strategy = StrategyModule(tqm)
    play = Play.load(dict(name='', hosts='group1,group2'), tqm.inventory, tqm.var_manager, tqm.loader)
    strategy.add_t

# Generated at 2022-06-13 15:12:36.525954
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True

# Generated at 2022-06-13 15:12:39.471040
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = "tqm.py"
    strategy = StrategyModule(tqm)
    assert strategy._host_pinned == True

# Generated at 2022-06-13 15:12:40.637302
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    StrategyModule(None)


# Generated at 2022-06-13 15:12:42.737647
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    print("Testing constructor of class StrategyModule")
    strmodule = StrategyModule(None)

# Testing StrategyModule class
test_StrategyModule()

# Generated at 2022-06-13 15:12:48.038479
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert issubclass(StrategyModule, FreeStrategyModule)
    assert StrategyModule.__doc__ == "Executes tasks on each host without interruption"
    assert issubclass(FreeStrategyModule, StrategyModule)
    assert FreeStrategyModule.__doc__ == "Optimized for network appliances; serializes or constrains hosts to a serialization group"
    x = StrategyModule("tqm")
    assert x._host_pinned == True

# Generated at 2022-06-13 15:12:48.627461
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    StrategyModule("test")

# Generated at 2022-06-13 15:12:57.568303
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    import ansible.constants as C
    import ansible.plugins.strategy.host_pinned as host_pinned_strategy
    import ansible.plugins.strategy.free as free_strategy

    # set up a dummy tqm object
    class TQM:
        def __init__(self):
            self.hostvars = {}

        def send_callback(self, *args, **kwargs):
            print(args)

    # set up a dummy inventory
    class Inventory:
        def __init__(self):
            self.hosts = {}
            self.groups = {}
            self.patterns = {}

        def list_hosts(self, *args, **kwargs):
            return self.hosts.keys()

        def get_groups(self, *args, **kwargs):
            return self

# Generated at 2022-06-13 15:13:00.065840
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    '''Unit test for constructor of class StrategyModule
    '''
    tqm = {'something': 'something else'}

    strategy = StrategyModule(tqm)
    assert strategy._host_pinned is True

# Generated at 2022-06-13 15:16:26.132259
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    global display
    display.verbosity = 3
    from ansible.errors import AnsibleError
    from ansible.inventory.host import Host
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.inventory.inventory import Inventory
    from ansible.vars.manager import VariableManager
    host = Host(name="my_host")
    hosts = [host]
    inventory = Inventory(hosts=hosts)
    variable_manager = VariableManager()
    loader = variable_manager._loader

# Generated at 2022-06-13 15:16:28.173457
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy = StrategyModule(tqm=None)
    assert(strategy._host_pinned == True)