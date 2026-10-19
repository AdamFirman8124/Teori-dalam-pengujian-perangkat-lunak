

# Generated at 2022-06-13 15:06:25.230714
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True

# Generated at 2022-06-13 15:06:26.048772
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule


# noinspection PyMethodMayBeStatic

# Generated at 2022-06-13 15:06:26.396194
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule

# Generated at 2022-06-13 15:06:32.195873
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = object()
    sm = StrategyModule(tqm)
    assert sm._tqm == tqm
    assert sm.name == 'host_pinned'
    assert sm.get_host_list() == []
    assert sm._min_serial_task_count() == 0
    assert sm._serialized_tasks == []
    assert sm._display == display
    assert sm._host_pinned

# Generated at 2022-06-13 15:06:34.827771
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    print("Testing")
    tqm = {}
    strategy_module = StrategyModule(tqm)
    assert strategy_module.get_host_pinned() == True

# Generated at 2022-06-13 15:06:36.472081
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule(None)

from ansible.plugins.strategy.host_pinned import StrategyModule

# Generated at 2022-06-13 15:06:40.983789
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    """Unit test for constructor of class StrategyModule"""
    tqm = MagicMock()
    tqm.__class__ = 'ansible.executor.task_queue_manager'
    assert StrategyModule(tqm) != None
    assert StrategyModule(tqm) != ""
    assert StrategyModule(tqm).__class__ == StrategyModule


# Generated at 2022-06-13 15:06:41.347944
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass

# Generated at 2022-06-13 15:06:42.744463
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    import pprint
    import mock
    from ansible.plugins.strategy.host_pinned import StrategyModule
    strategy = StrategyModule(mock.MagicMock())
    pprint.pprint(dir(strategy))

# Generated at 2022-06-13 15:06:46.097055
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule.__name__ == 'StrategyModule' 
    assert strategy(tqm) == 'host_pinned'

# Generated at 2022-06-13 15:06:47.942560
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert isinstance(StrategyModule, object)

# Generated at 2022-06-13 15:06:50.391508
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    class TestTaskQueueManager:
        pass
    tqm = TestTaskQueueManager()
    strategy = StrategyModule(tqm)
    assert True == strategy._host_pinned

# Generated at 2022-06-13 15:06:51.295625
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    test_strategy = StrategyModule(tqm)

# Generated at 2022-06-13 15:06:52.471103
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_obj = StrategyModule(None)
    assert strategy_obj is not None

# Generated at 2022-06-13 15:06:53.150517
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True

# Generated at 2022-06-13 15:06:54.610309
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule.__doc__
    assert StrategyModule.__init__.__doc__

# Generated at 2022-06-13 15:06:55.457286
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule(tqm)

# Generated at 2022-06-13 15:06:57.188868
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = 'self._host_pinned'
    assert StrategyModule(tqm)._host_pinned == True
    return 1

# Generated at 2022-06-13 15:06:59.964289
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert not StrategyModule.__doc__ == None
    assert not StrategyModule.__init__.__doc__ == None



# Generated at 2022-06-13 15:07:02.310300
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm =  None
    try:
        x = StrategyModule(tqm)
    except:
        assert True
    else:
        assert False

# Generated at 2022-06-13 15:07:05.298296
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule


# Generated at 2022-06-13 15:07:06.816787
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
  tqm = None
  StrategyModule(tqm)


# Generated at 2022-06-13 15:07:07.443491
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True

# Generated at 2022-06-13 15:07:10.709352
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    """
    Constructor for class StrategyModule
    """
    from ansible.plugins.strategy import StrategyModule
    from ansible.plugins.strategy.free import StrategyModule as FreeStrategyModule
    import ansible.plugins.loader as plugin_loader
    display = Display()
    plugin_loader.add_directory('./plugins/strategy')
    strategy_loader = plugin_loader.get('strategy', class_only=True)

    strategy_loader_list = list(strategy_loader.values())
    StrategyModule = strategy_loader_list[0]
    obj = StrategyModule(display)
    assert isinstance(obj, FreeStrategyModule)

# Generated at 2022-06-13 15:07:14.469538
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    ''' Unit test for constructor of class StrategyModule '''
    # Create StrategyModule object.
    tqm = StrategyModule(tqm)

    # Assert that tqm is of class StrategyModule.
    assert isinstance(tqm, StrategyModule)

# Generated at 2022-06-13 15:07:16.124966
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = StrategyModule()
    assert tqm

# Generated at 2022-06-13 15:07:20.012182
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = object()
    strategy_module = StrategyModule(tqm)
    assert(strategy_module._host_pinned == True)
    assert(strategy_module._tqm == tqm)

# Generated at 2022-06-13 15:07:21.601457
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule.__name__ == 'StrategyModule'


# Generated at 2022-06-13 15:07:22.269465
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule(tqm) != None

# Generated at 2022-06-13 15:07:23.154182
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    StrategyModule(tqm="test")


# Generated at 2022-06-13 15:07:31.219371
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.plugins.strategy import StrategyModule
    from ansible.plugins.strategy.host_pinned import StrategyModule as host_pinned
    from ansible.plugins.loader import strategy_loader

    strategy_loader.add('free', host_pinned)
    strategy = host_pinned()
    assert strategy._host_pinned == True

# Generated at 2022-06-13 15:07:34.713413
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = 1
    result =  StrategyModule(tqm)
    assert result._host_pinned == True
    assert result._always_run_modules == []
    assert result._no_hosts == False
    assert result._subset == None

# Generated at 2022-06-13 15:07:36.302266
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    #Create an instance of class StrategyModule
    strategy = StrategyModule(None)
    assert strategy._host_pinned == True

# Generated at 2022-06-13 15:07:37.232940
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass
# end of constructor test

# Generated at 2022-06-13 15:07:38.535369
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    id = StrategyModule({})
    assert isinstance(id,StrategyModule)

# Generated at 2022-06-13 15:07:40.436745
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = FreeStrategyModule('')
    test = StrategyModule(tqm)
    assert test._host_pinned == True

# Generated at 2022-06-13 15:07:41.293906
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule.__doc__ != None

# Generated at 2022-06-13 15:07:41.771140
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    StrategyModule(object())

# Generated at 2022-06-13 15:07:45.610038
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.playbook.task_include import TaskInclude
    strategy = StrategyModule(None)
    assert strategy._host_pinned == True


# Generated at 2022-06-13 15:07:48.176329
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    display = Display()
    tqm = None
    strategy_module = StrategyModule(tqm)
    assert strategy_module._host_pinned == True

# Generated at 2022-06-13 15:07:57.483758
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass

# Generated at 2022-06-13 15:08:00.550075
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    display = Display()
    class_object = StrategyModule(display)
    assert class_object is not None, "Failed to construct StrategyModule object"

# test_StrategyModule()

# Generated at 2022-06-13 15:08:03.062925
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    s = StrategyModule('test')
    assert s._host_pinned == True

if __name__ == '__main__':
    test_StrategyModule()

# Generated at 2022-06-13 15:08:06.083817
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    StrategyModule.__init__(FreeStrategyModule.__init__(self, tqm))
    assert StrategyModule._host_pinned == True

# Generated at 2022-06-13 15:08:07.702317
# Unit test for constructor of class StrategyModule
def test_StrategyModule():     
    test_StrategyModule = StrategyModule()
    assert test_StrategyModule

# Generated at 2022-06-13 15:08:12.125273
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule.__name__ == 'StrategyModule'
    strategy = StrategyModule(object())
    assert strategy._host_pinned == True
    assert strategy._tqm.__name__ == 'AnsibleTaskQueueManager'
    assert strategy._display.__name__ == 'Display'



# Generated at 2022-06-13 15:08:13.454923
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert (StrategyModule != None)

# Generated at 2022-06-13 15:08:13.979234
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass

# Generated at 2022-06-13 15:08:16.031515
# Unit test for constructor of class StrategyModule
def test_StrategyModule():

    tqm = None
    strategy_module = StrategyModule(tqm)
    assert strategy_module._host_pinned == True


# Generated at 2022-06-13 15:08:16.883119
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert (StrategyModule.__doc__ is not None)

# Generated at 2022-06-13 15:08:35.974595
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    import ansible.plugins.strategy.host_pinned
    import ansible.plugins.strategy.free
    assert StrategyModule is ansible.plugins.strategy.host_pinned.StrategyModule
    assert FreeStrategyModule == ansible.plugins.strategy.free.StrategyModule

# Generated at 2022-06-13 15:08:36.395806
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tmp = StrategyModule()

# Generated at 2022-06-13 15:08:38.733938
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = FreeStrategyModule.__init__
    strategy = StrategyModule(tqm)
    assert strategy._host_pinned == True
    assert strategy._display.display("message") == display.display("message")


# Generated at 2022-06-13 15:08:40.901452
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    test_tqm = ''
    s = StrategyModule(test_tqm)
    assert s._host_pinned == True

# Generated at 2022-06-13 15:08:43.033854
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    sm = StrategyModule(None)
    assert sm

# Test to check value of _host_pinned value

# Generated at 2022-06-13 15:08:53.929316
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.plugins.strategy.host_pinned import StrategyModule
    from ansible.plugins.strategy import _STRATEGY_PLUGIN_PATH
    tqm=1
    strategy = StrategyModule(tqm)
    print("---Unit test for Ansible strategy plugins module----")
    print("Test Case 1:")
    print("Testing the register_variable of free.py plugin")
    print("Type of the registered variable should be string - ")
    result = type (strategy._host_pinned) == str
    print("Input: ")
    print(result)
    print("Output:")
    print(True)
    print("Test Result:")
    print(result)
    if (result):
        print("PASS")
    else:
        print("FAIL")
    print("----------------------------------------------------")
   

# Generated at 2022-06-13 15:08:55.320634
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert(StrategyModule.__init__.__doc__ == 'None')

# Generated at 2022-06-13 15:08:57.870772
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.playbook.task_queue_manager import TaskQueueManager
    print(StrategyModule.__init__)
    tqm = TaskQueueManager()
    StrategyModule(tqm)

test_StrategyModule()

# Generated at 2022-06-13 15:08:59.431994
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy = StrategyModule(tqm)
    assert strategy


# Generated at 2022-06-13 15:09:05.067784
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    class Tqm:
        def __init__(self):
            self.hostvars = {}
            self.sent_layer = {'hosts': { 'a': None}}
            self.vars = {}
            self.class_vars = {}
            self.cur_included_file = None
            self.filter = None
            self.setup_cache = None
            self.cache = None
            self.runner_queue = None
            self.inventory = None
            self.variable_manager = None
            self.loader = None
            self.stdout_callback = None
            self.stats = None
            self.stdout_callback = None
            self.callbacks = None
            self.runners = None
    tqm = Tqm()
    new_strategy = StrategyModule(tqm)
    assert new_

# Generated at 2022-06-13 15:09:50.540310
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    ansible_plugin_strategy_free = StrategyModule('tqm')
    assert ansible_plugin_strategy_free is not None
    assert ansible_plugin_strategy_free._host_pinned is True

# Generated at 2022-06-13 15:09:51.211716
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass

# Generated at 2022-06-13 15:09:52.130250
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    StrategyModule()


# Generated at 2022-06-13 15:10:03.216943
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.playbook.task_queue_manager import TaskQueueManager
    from ansible.executor.task_queue_manager import TaskQueueManager as TaskQueueManagerExecutor
    from ansible.executor.playbook_executor import PlaybookExecutor
    import ansible.constants as C

    playbook = PlaybookExecutor(playbooks=[C.DEFAULT_PLAYBOOK_PATH], inventory=TaskQueueManager._inventory, variable_manager=TaskQueueManager._variable_manager, loader=TaskQueueManager._loader, options=TaskQueueManager._options, passwords=TaskQueueManager._passwords)

# Generated at 2022-06-13 15:10:10.873568
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.task import Task
    from ansible.playbook import Play
    from ansible.playbook import Playbook
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.inventory.inventory import Inventory
    from ansible.template import Templar
    from io import StringIO
    import json
    import sys

    # This part of the code creates all the objects required to instantiate an object of class StrategyModule
    # We create a Playbook object and then a Play object and then a Task object
    # Since the StrategyModule object needs a TaskQueueManager object which needs a Playbook object
    # We create a playbook object which is added to the TaskQueueManager object

    # Create the playbook object
    playbook = Playbook()

   

# Generated at 2022-06-13 15:10:11.777125
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    Sm = StrategyModule('tqm')
    assert Sm._host_pinned

# Generated at 2022-06-13 15:10:13.041491
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    StrategyModule(tqm)

# Generated at 2022-06-13 15:10:19.637342
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    class Tqm():
        def __init__(self):
            self.host_set = ['localhost']
            self.inventory = []
            self.stats = ['localhost']
    smm = StrategyModule(Tqm())
    assert smm._host_pinned == True


# Generated at 2022-06-13 15:10:26.909470
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    class Test1:
        pass
    tqm = Test1()
    tqm.stats = Test1()
    tqm.stats.percentage = 100
    tqm.add_queue = Test1()
    tqm.add_queue.qsize = Test1()
    tqm.setup_cache = Test1()
    tqm.host_pinned = True
    tqm.host_setup_msg = Test1()
    tqm.host_pinned_value = Test1()
    sm = StrategyModule(tqm)
    assert sm._host_pinned

# Generated at 2022-06-13 15:10:27.317451
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    StrategyModule()

# Generated at 2022-06-13 15:12:08.115139
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    class Options(object):
        pattern = 'all'
        forks = 100
        subset = None
        verbose = 5
        extra_vars = None
        inventory = None
        listhosts = None
        module_path = None
        step = None
        start_at_task = None
        become = None
        become_method = None
        become_user = None
        become_ask_pass = None
        tags = None
        skip_tags = None
        one_line = None
        tree = None
        ask_vault_pass = None
        ansible_ssh_pass = None
        vault_password_file = None
        private_key_file = None
        remote_user = None
        connection = None
        timeout = None
        ssh_common_args = None
        sftp_extra_args = None
       

# Generated at 2022-06-13 15:12:10.107888
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_module = StrategyModule.__init__()
    assert_equals(strategy_module, "_host_pinned=True")


# Generated at 2022-06-13 15:12:11.237664
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    d = StrategyModule('tqm')
    assert d._host_pinned == True

# Generated at 2022-06-13 15:12:12.623874
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass

# Generated at 2022-06-13 15:12:13.469114
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True

# Generated at 2022-06-13 15:12:15.235821
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = MagicMock()
    StrategyModule(tqm)

# vim: set et ts=4 sw=4 :

# Generated at 2022-06-13 15:12:17.083021
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.plugins.strategy.host_pinned import StrategyModule
    tqm = 0
    strategy = StrategyModule(tqm)
    assert strategy

# Generated at 2022-06-13 15:12:19.692676
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule(tqm)._host_pinned == True

# Generated at 2022-06-13 15:12:21.621319
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    module = StrategyModule(tqm = None)
    assert module._host_pinned == True

# Generated at 2022-06-13 15:12:22.524746
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule is not None


# Generated at 2022-06-13 15:15:39.412629
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule.__name__ == 'StrategyModule'
    tqm = object()
    obj = StrategyModule(tqm)
    assert obj.tqm == tqm
    assert obj._tqm == tqm
    assert obj._batch_size == 0
    assert len(obj._queue) == 0
    assert len(obj._unreachable_hosts) == 0
    assert len(obj._failed_hosts) == 0
    assert obj._host_pinned == True


# Generated at 2022-06-13 15:15:41.382511
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = {}
    my_object = StrategyModule(tqm)
    assert my_object._host_pinned == True

# Generated at 2022-06-13 15:15:42.012517
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule



# Generated at 2022-06-13 15:15:43.802917
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_module = StrategyModule('tqm')
    assert strategy_module._host_pinned == True, "'_host_pinned' was not initialized as expected"

# Generated at 2022-06-13 15:15:44.702197
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass


# Generated at 2022-06-13 15:15:48.431599
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert issubclass(StrategyModule, FreeStrategyModule)
    tqm = 'dummy'
    strategy = StrategyModule(tqm)
    display.assert_called_with('StrategyModule class instantiated.')
    assert strategy._host_pinned



# Generated at 2022-06-13 15:15:52.768471
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # Create a host queue manager
    from ansible.executor.task_queue_manager import TaskQueueManager
    tqm = TaskQueueManager(None, None)

    # Create a strategy module object
    strategy_module = StrategyModule(tqm)

    # Check the execution of constructor
    assert strategy_module._host_pinned == True

# Generated at 2022-06-13 15:15:53.843620
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy = StrategyModule()
    assert strategy._host_pinned == True

# Generated at 2022-06-13 15:15:55.342652
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    mod = StrategyModule(tqm = None)
    assert isinstance(mod, StrategyModule)



# Generated at 2022-06-13 15:15:55.826171
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule