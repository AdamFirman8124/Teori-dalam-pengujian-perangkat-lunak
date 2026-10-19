

# Generated at 2022-06-13 15:06:25.857347
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    obj = StrategyModule(tqm)
    assert obj._host_pinned == True

# Generated at 2022-06-13 15:06:27.870581
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.plugins.strategy.host_pinned import StrategyModule
    tqm = None
    strategy_module = StrategyModule(tqm)
    assert strategy_module._host_pinned

# Generated at 2022-06-13 15:06:29.177194
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = object
    strategy = StrategyModule(tqm)
    assert strategy._host_pinned == True

# Generated at 2022-06-13 15:06:34.928701
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.plugins.strategy.host_pinned import StrategyModule
    obj = StrategyModule(tqm=[])
    assert obj.get_name() == 'host_pinned'
    assert str(obj._display) == '<ansible.utils.display.Display object at 0x7fd7fd526fd0>'
    assert obj.get_option('_host_pinned') == True

# Generated at 2022-06-13 15:06:35.774775
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # TODO
    pass

# Generated at 2022-06-13 15:06:37.227593
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert hasattr(StrategyModule, '_host_pinned')

# Generated at 2022-06-13 15:06:37.851454
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass

# Generated at 2022-06-13 15:06:38.477465
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule

# Generated at 2022-06-13 15:06:40.415946
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy = StrategyModule(tqm)
    assert strategy.name == 'host_pinned'
    assert strategy._host_pinned is True

# Generated at 2022-06-13 15:06:41.740993
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert issubclass(StrategyModule, FreeStrategyModule)
    strategy_module = StrategyModule(None)
    assert isinstance(strategy_module, StrategyModule)

# Generated at 2022-06-13 15:06:45.053270
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule(tqm=None)

# Generated at 2022-06-13 15:06:54.614158
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.plugins.strategy.host_pinned import StrategyModule
    from ansible.plugins.strategy import ActionModule
    import ansible.constants

    ansible.constants.HOST_KEY_CHECKING = False
    tqm = ActionModule.ActionModule(forks=1, timeout=0, remote_user=None, private_key_file=None, ssh_common_args=None, ssh_extra_args=None,
                                    sftp_extra_args=None, scp_extra_args=None, become=None, become_method=None, become_user=None,
                                    verbosity=None, check=None)
    strategy = StrategyModule(tqm=tqm)

    assert hasattr(strategy, '_host_pinned')
    assert strategy._host_pinned is False



# Generated at 2022-06-13 15:06:54.978853
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True

# Generated at 2022-06-13 15:06:56.433128
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    myStrategyModule = StrategyModule()
    assert myStrategyModule.get_host_pinned() == True

# Generated at 2022-06-13 15:06:58.410316
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    class tqm:
        def __init__(self):
            self._host_pinned = True

    obj = StrategyModule(tqm)
    return obj

# Generated at 2022-06-13 15:06:59.860544
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule(1)

# Generated at 2022-06-13 15:07:00.385296
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule

# Generated at 2022-06-13 15:07:04.444153
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    display = Display()
    tqm = FreeStrategyModule(__file__)
    display.debug(tqm)
    assert tqm._host_pinned == True


# Generated at 2022-06-13 15:07:13.080744
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    import unittest # avoid import errors if this isn't built yet
    from ansible.playbook.task_include import TaskInclude
    from ansible.executor.task_result import TaskResult
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.parsing.dataloader import DataLoader
    import ansible.constants
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.plugins.loader import callback_loader, connection_loader, lookup_loader
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.utils.vars import combine_vars
    from ansible.inventory.host import Host

# Generated at 2022-06-13 15:07:15.213618
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    s = StrategyModule(None)
    assert hasattr(s, "_host_pinned")
    assert s._host_pinned == True

# Generated at 2022-06-13 15:07:21.549006
# Unit test for constructor of class StrategyModule
def test_StrategyModule():

    class FakeTqm:
        def __init__(self):
            self.hostvars = {}

    tqm = FakeTqm()
    sm = StrategyModule(tqm)
    assert sm._host_pinned == True


# Generated at 2022-06-13 15:07:23.635342
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    mod = StrategyModule()
    assert mod.__class__.__name__ == 'StrategyModule'

# Generated at 2022-06-13 15:07:24.473576
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategyModule = StrategyModule(None)
    assert strategyModule._host_pinned == True



# Generated at 2022-06-13 15:07:25.877605
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_module = StrategyModule()
    assert strategy_module._host_pinned == True

# Generated at 2022-06-13 15:07:26.281792
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    module = StrategyModule()

# Generated at 2022-06-13 15:07:29.337283
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    strategyModule = StrategyModule(tqm)
    assert strategyModule._host_pinned == True
    assert strategyModule._tqm is None
    return

test_StrategyModule()

# Generated at 2022-06-13 15:07:39.113678
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.plugins.connection.local import Connection
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.inventory.manager import InventoryManager


# Generated at 2022-06-13 15:07:41.017886
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    print("Unit testing Strategy Module")
    strategyModuleObj = StrategyModule(tqm)
    assert strategyModuleObj._host_pinned == True

# Generated at 2022-06-13 15:07:41.530855
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    StrategyModule(None)

# Generated at 2022-06-13 15:07:43.819156
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    foo = StrategyModule(tqm='tqm')
    assert foo.__class__.__name__ == 'StrategyModule'
    assert foo._host_pinned == True



# Generated at 2022-06-13 15:07:59.487108
# Unit test for constructor of class StrategyModule

# Generated at 2022-06-13 15:08:06.797322
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    class TestTqm(object):
        def __init__(self):
            self.tasks = []
            self.send_callback = None
    class TestDisplay():
        def __init__(self):
            pass
        def display(self, msg, color=None, stderr=False, screen_only=False, log_only=False):
            return
    class TestTaskQueueManager(TestTqm):
        def __init__(self, *args, **kwargs):
            super(TestTaskQueueManager, self).__init__()
            self.display = TestDisplay()

    host_pinned_strategy = StrategyModule(TestTaskQueueManager())
    assert host_pinned_strategy._host_pinned

if __name__ == '__main__':
    test_StrategyModule()

# Generated at 2022-06-13 15:08:07.610426
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy = StrategyModule(tqm = None)
    assert strategy != None
    assert strategy._host_pinned == True

# Generated at 2022-06-13 15:08:09.086820
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy = StrategyModule('tqm')
    assert strategy._host_pinned == True

# Generated at 2022-06-13 15:08:10.463088
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = object()
    obj = StrategyModule(tqm)

# Generated at 2022-06-13 15:08:12.700527
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    sm = StrategyModule('tqm')
    assert sm._host_pinned == True


# Generated at 2022-06-13 15:08:16.182544
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = "test_StrategyModule_tqm"
    sm = StrategyModule(tqm)
    assert sm._tqm == "test_StrategyModule_tqm"
    assert sm._host_pinned == True

# Generated at 2022-06-13 15:08:17.200153
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    StrategyModule()


# Generated at 2022-06-13 15:08:18.907432
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = dict()
    sm = StrategyModule(tqm)
    assert sm is not None
    assert sm._host_pinned == True

# Generated at 2022-06-13 15:08:20.050036
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule(FreeStrategyModule) is not None


# Generated at 2022-06-13 15:08:29.400834
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert issubclass(StrategyModule, FreeStrategyModule)

# Generated at 2022-06-13 15:08:30.762736
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    import ansible.plugins.strategy.host_pinned as hp
    sm = hp.StrategyModule(None)
    assert hp._host_pinned == True

# Generated at 2022-06-13 15:08:32.724508
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert issubclass(StrategyModule, FreeStrategyModule)

# Generated at 2022-06-13 15:08:33.504011
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True

# Generated at 2022-06-13 15:08:35.519438
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = object()
    strategy_module = StrategyModule(tqm)
    assert(strategy_module._host_pinned == True)

# Generated at 2022-06-13 15:08:37.370006
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    strat = StrategyModule(tqm)
    print(strat._host_pinned)

# test_StrategyModule()

# Generated at 2022-06-13 15:08:40.142989
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    host_pinned_module = StrategyModule(object)
    assert host_pinned_module._host_pinned == True

# Generated at 2022-06-13 15:08:47.269032
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.plugins.strategy.host_pinned import StrategyModule
    from ansible.config.manager import ConfigManager
    from ansible_collections.ansible.community.plugins.module_utils.common.removed import removed_class
    from ansible_collections.ansible.community.tests.unit.mock.manager import create_manager

    config_manager = ConfigManager()
    config_data = {"strategy_plugins": "host_pinned"}
    config_manager._set_runtime_facts(config_data)
    config_manager._configure_logging()

    tqm = removed_class()
    tqm._stdout_callback = None
    tqm.config_data = config_manager

    strategy = StrategyModule(tqm)
    assert isinstance(strategy, StrategyModule)

    #

# Generated at 2022-06-13 15:08:48.680017
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert hasattr(StrategyModule, '_host_pinned')

# Generated at 2022-06-13 15:08:49.606863
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass

# Generated at 2022-06-13 15:09:08.638796
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule

# Generated at 2022-06-13 15:09:11.360192
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    """ Unit test for constructor of class StrategyModule """
    tqm = None
    strategy_module = StrategyModule(tqm)
    assert isinstance(strategy_module, StrategyModule)
    assert strategy_module._host_pinned is True
    assert strategy_module._display is display

# Generated at 2022-06-13 15:09:11.982301
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True

# Generated at 2022-06-13 15:09:13.529360
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    st = StrategyModule(tqm=None)
    assert st is not None

# Generated at 2022-06-13 15:09:20.368584
# Unit test for constructor of class StrategyModule

# Generated at 2022-06-13 15:09:21.879633
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule



# Generated at 2022-06-13 15:09:23.753112
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_module = StrategyModule('tqm')
    assert strategy_module is not None
    assert strategy_module._host_pinned



# Generated at 2022-06-13 15:09:25.913447
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    test_display = Display()
    test_tqm = AnsibleQueueManager(test_display)
    StrategyModule(test_tqm)

# Generated at 2022-06-13 15:09:26.713828
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule(tqm)

# Generated at 2022-06-13 15:09:34.081797
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    import ansible
    from ansible.plugins.strategy.host_pinned import StrategyModule
    ansible_version = int(ansible.__version__[:1])
    if ansible_version >= 2:
        from ansible.executor.task_queue_manager import TaskQueueManager
        from ansible.parsing.dataloader import DataLoader
        from ansible.vars.manager import VariableManager
        from ansible.inventory.manager import InventoryManager
        from ansible.playbook.play import Play
        from ansible.executor.playbook_executor import PlaybookExecutor
        from ansible.module_utils.common.collections import ImmutableDict
        loader = DataLoader()
        variable_manager = VariableManager()
        inventory = InventoryManager(loader=loader, sources='localhost,')

# Generated at 2022-06-13 15:10:13.317485
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy = StrategyModule(None)
    assert strategy

# Generated at 2022-06-13 15:10:18.134764
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_module = StrategyModule(tqm=None)
    assert strategy_module is not None
    assert strategy_module.get_host_pinned() is True

# Generated at 2022-06-13 15:10:21.110473
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule
    # initialize StrategyModule with tqm
    s = StrategyModule(tqm='tqm')
    assert s.__class__.__name__ == 'StrategyModule'

# Generated at 2022-06-13 15:10:22.353540
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule('test') is not None

# Generated at 2022-06-13 15:10:25.381298
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = 'tqm'
    display = 'display'
    tqm.display = display
    strategymodule = StrategyModule(tqm)
    strategymodule._host_pinned = True
    assert strategymodule._host_pinned

# Generated at 2022-06-13 15:10:28.668156
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_module = StrategyModule("")
    assert isinstance(strategy_module, StrategyModule)
    assert isinstance(strategy_module, FreeStrategyModule)
    assert strategy_module._host_pinned == True

# Generated at 2022-06-13 15:10:29.194694
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True

# Generated at 2022-06-13 15:10:30.665946
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    strategy_module = StrategyModule(tqm)
    assert strategy_module is not None

# Generated at 2022-06-13 15:10:32.084000
# Unit test for constructor of class StrategyModule
def test_StrategyModule():

    # Construct a strategy module object
    obj = StrategyModule("test")
    # Assert that object construction is successful
    assert obj is not None

# Generated at 2022-06-13 15:10:32.773774
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass


__all__ = ['StrategyModule']

# Generated at 2022-06-13 15:12:20.330270
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.playbook.task import Task
    from ansible.playbook.play import Play

    # Define the number of forks so each host gets its own to avoid error
    forks = len(hosts)
    # Create a task for each host
    for host in hosts:
        task = Task()
        task.set_loader(loader)
        task.action = "command"
        task.args["_raw_params"] = "echo 'Hello world'"
        play.add_task(task)
    # Create a play
    play = Play().load(dict(
        name = "Ansible Play",
        hosts = 'all',
        gather_facts = 'no',
        tasks = []
    ), loader = loader)
    # Create a TQM
    tqm = None

# Generated at 2022-06-13 15:12:30.113037
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule.__module__ == 'ansible.plugins.strategy.host_pinned'
    assert StrategyModule.__doc__ == 'Executes tasks on each host without interruption'

# Generated at 2022-06-13 15:12:32.580649
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = {}
    strategy_mod_obj = StrategyModule(tqm)
    assert strategy_mod_obj

if __name__ == '__main__':
    test_StrategyModule()

# Generated at 2022-06-13 15:12:37.214637
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    """ this builds a test to check that the StrategyModule class was built correctly """
    # build test object StrategyModule
    testobj = StrategyModule('tqm')
    # assert that the StrategyModule _host_pinned bool is set to True
    assert testobj._host_pinned

# Generated at 2022-06-13 15:12:39.057004
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    st = StrategyModule()
    assert st._host_pinned == True

# Generated at 2022-06-13 15:12:42.015284
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    class TestStrategyModule():
        def __init__(self):
            self.host_pinned = True
            self.host_pinned = True

    assert TestStrategyModule().host_pinned is True

# Generated at 2022-06-13 15:12:42.973561
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule is not None


# Generated at 2022-06-13 15:12:45.284120
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    ''' unit test for StrategyModule '''
    tqm = 'tqm'
    StrategyModule(tqm)

# Generated at 2022-06-13 15:12:46.391858
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    startobj = StrategyModule(None)
    assert startobj is not None


# Generated at 2022-06-13 15:12:47.126216
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True

# Generated at 2022-06-13 15:16:14.430235
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.inventory import Inventory
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.hostvars import HostVars
    from ansible.vars.hostvars import HostVarsVars


# Generated at 2022-06-13 15:16:15.746006
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    test_strategy = StrategyModule()
    assert test_strategy._host_pinned == True


# Generated at 2022-06-13 15:16:18.909112
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm_mock = 'ansible.plugins.strategy.host_pinned.tqm'
    test_obj = StrategyModule(tqm_mock)
    assert test_obj._host_pinned == True


# Generated at 2022-06-13 15:16:22.444009
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # Create a fake display instance to pass as argument to the StrategyModule constructor
    display = {'Display': 0, 'colorize': 0, 'columns': 0, 'write': 0}
    strategymodule = StrategyModule(display)
    assert strategymodule._host_pinned == True