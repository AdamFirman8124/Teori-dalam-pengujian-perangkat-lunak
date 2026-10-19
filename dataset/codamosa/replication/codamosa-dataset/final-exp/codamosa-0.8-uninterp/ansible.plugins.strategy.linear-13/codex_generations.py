

# Generated at 2022-06-13 15:18:03.606457
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_module = StrategyModule(None, None, None, None, None, None, None, None, None)


# Generated at 2022-06-13 15:18:11.325405
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():

    class Iter(object):
        def add_tasks(self, host, block):
            pass

    # Instance to test
    strategyModule = StrategyModule(123, None)
    strategyModule._tqm = 123
    strategyModule._tqm.RUN_OK = 123
    strategyModule._tqm._terminated = False
    strategyModule._tqm._failed_hosts = {'failed_hosts': 123}
    strategyModule._tqm.send_callback = MagicMock(return_value=None)
    strategyModule._tqm.RUN_UNKNOWN_ERROR = 123

    strategyModule._variable_manager = 123
    strategyModule._variable_manager.get_vars = MagicMock(return_value='get_vars')
    strategyModule._variable_manager.add_nonpersistent_facts = Magic

# Generated at 2022-06-13 15:18:13.335589
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
  Iterator = Iterator()
  PlayContext = PlayContext()
  StrategyModule = StrategyModule()

  if (StrategyModule.run(Iterator, PlayContext)):
    pass
  else:
    print("Failed")




# Generated at 2022-06-13 15:18:15.275040
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # Construction of the StrategyModule class
    strategy_module = StrategyModule()


# Generated at 2022-06-13 15:18:17.534997
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule(tqm=None)


# Generated at 2022-06-13 15:18:24.830016
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    import unittest
    import os

    # in moto, os.getuid() always returns 0
    for module_finder_test in [unittest.mock.MagicMock(return_value=0), unittest.mock.MagicMock(return_value=1000)]:
        mock_tqm = unittest.mock.MagicMock(name='mock_tqm')
        mock_variable_manager = unittest.mock.MagicMock(name='mock_variable_manager')
        mock_loader = unittest.mock.MagicMock(name='mock_loader')

        mock_tqm.get_variable_manager = unittest.mock.MagicMock(name='get_variable_manager', return_value=mock_variable_manager)
        mock_tq

# Generated at 2022-06-13 15:18:29.587221
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    module = 'StrategyModule'
    current_play = ''
    hosts = 'hosts'
    iterator = ''
    play_context = ''
    strategy_ = StrategyModule()
    assert strategy_.run(iterator, play_context) == None

# unit test for method _get_next_task_lockstep of class StrategyModule

# Generated at 2022-06-13 15:18:32.938138
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    strategyModule = StrategyModule(None, None, None)
    strategyModule.id = 'test-id'
    assert strategyModule.run(None, None) == 0x1000000

# Generated at 2022-06-13 15:18:38.987080
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    # Create StrategyModule object
    strategy_module = StrategyModule()

    # Create iterator object
    iterator = type('', (), {})()
    iterator.batch_size = 10

    # Create play_context object
    play_context = type('', (), {})()

    # Call method run of StrategyModule
    result = strategy_module.run(iterator, play_context)
    assert result == 0

# Generated at 2022-06-13 15:18:49.818829
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    #setup
    host_results = list()
    item_results = MagicMock()
    host_results.append(item_results)
    item_results_1 = MagicMock()
    host_results.append(item_results_1)
    iterator = MagicMock()
    play_context = MagicMock()
    strategy_module = StrategyModule()
    strategy_module._tqm = MagicMock()
    strategy_module._tqm.RUN_OK = True
    strategy_module._tqm._terminated = False
    strategy_module._set_hosts_cache = MagicMock()
    strategy_module.get_hosts_left = MagicMock()
    strategy_module.get_hosts_left.return_value = host_results

# Generated at 2022-06-13 15:19:25.629547
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass


# Generated at 2022-06-13 15:19:28.357785
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy = StrategyModule(tqm=None)

    assert(strategy.get_name() == 'linear')

# Generated at 2022-06-13 15:19:29.823194
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy = StrategyModule()
    assert isinstance(strategy, StrategyModule) is True

# Generated at 2022-06-13 15:19:39.000734
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    """
    Test method run of class StrategyModule
    """
    try:
        import __builtin__ as builtins
    except ImportError:
        import builtins
    import re
    import subprocess
    import tempfile
    import time

    import ansible.constants as C
    import ansible.executor.task_queue_manager as T
    import ansible.inventory
    import ansible.playbook.play
    import ansible.playbook.play_context
    import ansible.playbook.playbook
    import ansible.playbook.task
    import ansible.plugins.loader
    import ansible.template
    from ansible.utils.display import Display
    from ansible.utils.color import ANSIBLE_COLOR
    from ansible.utils.display import Display
    from ansible.utils.vars import combine_

# Generated at 2022-06-13 15:19:40.736866
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_obj = StrategyModule()
    # Test that StrategyModule successfully instantiates
    assert strategy_obj is not None


# Generated at 2022-06-13 15:19:41.789105
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    assert True


# Generated at 2022-06-13 15:19:53.672810
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    # create an instance of the Ansible parser
    Parser = ansible.parsing.dataloader.DataLoader()

    # create an instance of the Ansible playbook
    Runner = ansible.executor.task_queue_manager.TaskQueueManager(
            inventory=inventory.InventoryManager(loader=Parser, sources=['localhost,',]),
            variable_manager=ansible.vars.manager.VariableManager(),
            loader=Parser,
            options=Options(),
            passwords=dict(), #{'conn_pass':'123456','become_pass':'123456'},
        )

    # create an instance of the ansible strategy module
    strategy_module = StrategyModule(
        tqm=Runner,
        host_list=inventory.InventoryManager(loader=Parser, sources=['localhost,',])
    )

    #

# Generated at 2022-06-13 15:19:54.879139
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_module = StrategyModule()


# Generated at 2022-06-13 15:19:56.719225
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_plugin = StrategyModule()
    assert strategy_plugin is not None


# Generated at 2022-06-13 15:19:59.353449
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy = StrategyModule()
    print(strategy)

if __name__ == '__main__':
    test_StrategyModule()

# Generated at 2022-06-13 15:20:43.790069
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    print("Running module unit test for StrategyModule...")
    my_strategyModule = StrategyModule(tqm=None)
    assert(my_strategyModule.__class__.__name__ == "StrategyModule")
    assert(my_strategyModule.__doc__ == "")
    assert(my_strategyModule.__init__.__doc__ == "")
    assert(my_strategyModule._get_next_task.__doc__ == "")
    assert(my_strategyModule._get_next_task_lockstep.__doc__ == "")
    assert(my_strategyModule.add_tqm_variables.__doc__ == "")
    assert(my_strategyModule.get_hosts_left.__doc__ == "")

# Generated at 2022-06-13 15:20:49.436128
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    module = ansible.plugins.strategy.StrategyModule(
        tqm = mock.MagicMock(),
        loader = mock.MagicMock(),
        variable_manager = mock.MagicMock(),
        shared_loader_obj = mock.MagicMock()
    )
    iterator = mock.MagicMock()
    play_context = mock.MagicMock()
    assert module.run(iterator, play_context) == 0



# Generated at 2022-06-13 15:20:50.674453
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_module = StrategyModule()
    print(strategy_module)


# Generated at 2022-06-13 15:20:52.415778
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_module = StrategyModule()
    assert isinstance(strategy_module, StrategyModule)


# Generated at 2022-06-13 15:20:53.498579
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy = StrategyModule()


# Generated at 2022-06-13 15:20:54.180104
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
  pass

# Generated at 2022-06-13 15:21:02.613871
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    import ansible.playbook.play
    import ansible.playbook.play_context
    from ansible.playbook.tqdm_callback import TqdmCallbackModule
    from ansible.playbook.task_queue_manager import TaskQueueManager
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.inventory.host import Host
    from ansible.plugins.loader import action_loader
    from ansible.plugins.loader import callback_loader
    from ansible.plugins.loader import module_loader
    from ansible.plugins.loader import lookup_loader

    from ansible.template import Templar


# Generated at 2022-06-13 15:21:06.665950
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    loader = DataLoader()
    variable_manager = VariableManager()
    result_callback_b = ResultCallback()
    runner_callback_b = RunnerCallback()
    strategy_module = StrategyModule(loader=loader, variable_manager=variable_manager,
                                     result_callback=result_callback_b, runner_callback=runner_callback_b)


# Generated at 2022-06-13 15:21:09.247143
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    strategy_module = StrategyModule()
    assert strategy_module != None, "Failed to instance StrategyModule"
    print("Success: instance StrategyModule")
#Unit test for method _get_next_task_lockstep of class StrategyModule

# Generated at 2022-06-13 15:21:15.932566
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    hc = HostManager(playbook_dir='.')
    tqm = TaskQueueManager(host_manager=hc)
    sm = StrategyModule(tqm)

    assert sm._hosts_cache is None
    assert sm._tqm is tqm
    assert sm._inventory is tqm.get_inventory()
    assert sm._variable_manager is tqm.get_variable_manager()



# Generated at 2022-06-13 15:22:31.466821
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    m = StrategyModule()
    play = Play()
    play._included_file_search_path = InMemoryIncludedFileSearchPath()
    include_file_path = '/tmp/include_file.yaml'

    m._copy_included_file = unittest.mock.MagicMock()
    m._load_included_file = unittest.mock.MagicMock()
    m._prepare_and_create_noop_block_from = unittest.mock.MagicMock()
    m.get_hosts_left = unittest.mock.MagicMock()
    m._get_next_task_lockstep = unittest.mock.MagicMock()
    m._execute_meta = unittest.mock.MagicMock()
    m._process_pending_results

# Generated at 2022-06-13 15:22:37.409148
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # type: () -> int
    obj = StrategyModule(loader=None, tqm=None)
    if obj._loader is None and obj._tqm is None and obj._failed_hosts == dict() and obj._blocked_hosts == dict() \
        and obj._tqm_variables == dict() and obj._final_q is None and obj._worker_prc is None and obj._initial_q is None \
        and obj._pending_results == 0 and obj._workers == list() and obj._stats is None:
        return True
    else:
        return False


# Generated at 2022-06-13 15:22:48.999511
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_module = StrategyModule(
        tqm=None,
        variable_manager=None,
        loader=None,
        shared_loader_obj=None,
        host_list=C.DEFAULT_HOST_LIST,
        stats=None,
        run_additional_callbacks=C.DEFAULT_RUN_ADDITIONAL_CALLBACKS,
        run_tree=False,
        subset=None,
        setup_cache=None,
        default_vars_template=C.DEFAULT_VARS_PLUGIN_CONFIG_FILE,
        extra_vars=None,
        passwords=None,
        module_vars=None,
        inventory=None,
        **kwargs
    )

    assert strategy_module.get_hosts_left(None) == []
    assert strategy_module

# Generated at 2022-06-13 15:22:51.546634
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    from ansible.utils.playbook_includes import IncludedFile
    pass


# Generated at 2022-06-13 15:22:53.687671
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_module = StrategyModule('', None, None)
    assert strategy_module.get_name() == 'linear'

# Generated at 2022-06-13 15:22:54.567545
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    #todo
    pass


# Generated at 2022-06-13 15:23:01.225655
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    def _test_InsideStrategyModule(self):
        assert self._tqm is not None
        assert self._only_tags is None
        assert self._skip_tags is None
        assert self._vulnerable_hosts is None
        assert self._vulnerable_variables is None
        assert self._pending_results == 0
        assert self._blocked_hosts == {}

    strategy_module = StrategyModule(_test_InsideStrategyModule)
    assert strategy_module._tqm is None
    assert strategy_module._only_tags is None
    assert strategy_module._skip_tags is None
    assert strategy_module._vulnerable_hosts is None
    assert strategy_module._vulnerable_variables is None
    assert strategy_module._pending_results == 0
    assert strategy_module._blocked_hosts == {}



# Generated at 2022-06-13 15:23:07.107326
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    '''
    This test will test the method run of class StrategyModule.
    '''
    def do_nothing(*args, **kwargs):
        pass

    # No assertion due to Ansible's idiosyncratic style :(
    # TODO: Improve tests for Ansible's code.
    (StrategyModule.__new__(StrategyModule)).run(
        do_nothing,
        do_nothing
    )


# Generated at 2022-06-13 15:23:08.063226
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule(tqm=None) is not None

# Generated at 2022-06-13 15:23:13.725393
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    try:
        tqm = TaskQueueManager(
            inventory=None,
            variable_manager=None,
            loader=None,
            passwords=None,
            stdout_callback='default',
            run_additional_callbacks=False,
            run_tree=False,
        )
    except Exception as e:
        print("initialization of TaskQueueManager failed:", e)
        exit(1)
    try:
        strategy_module = StrategyModule(tqm)
    except Exception as e:
        print("initialization of StrategyModule failed:", e)
        exit(1)
    exit(0)


# Generated at 2022-06-13 15:25:40.070059
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass

# Generated at 2022-06-13 15:25:46.641969
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_module = StrategyModule(
        tqm=None,
        connection_info={},
        loader=None,
        variable_manager=None,
        loader_on_failed=False,
    )
    assert strategy_module._tqm is None
    assert strategy_module.connection_info == {}
    assert strategy_module._loader == None
    assert strategy_module._variable_manager == None
    assert strategy_module._loader_on_failed == False


# Generated at 2022-06-13 15:25:49.378414
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_module = StrategyModule()

    assert(strategy_module is not None)
    assert(type(strategy_module) == StrategyModule)
    assert(isinstance(strategy_module, StrategyModule))

# Generated at 2022-06-13 15:25:51.248812
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    strategy = StrategyModule()
    iterator = None
    play_context = None
    print(strategy.run(iterator, play_context))


# Generated at 2022-06-13 15:25:54.993392
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    ''' strategy_module.py:TestStrategyModule.test_StrategyModule()'''
    module = StrategyModule(tqm=None)
    assert isinstance(module, StrategyModule)


# Generated at 2022-06-13 15:25:57.230800
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    module = StrategyModule(tqm=Mock(), variables=dict())
    assert isinstance(module, StrategyModule)

# Generated at 2022-06-13 15:25:58.507345
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy = StrategyModule()
    assert strategy is not None


# Generated at 2022-06-13 15:26:07.169306
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    hosts = [
        {
            "hostname": "localhost",
            "port": 22,
            "name": "localhost",
            "_ansible_ssh_host": "127.0.0.1",
            "_ansible_ssh_port": 22,
            "_ansible_ssh_user": "johndoe",
            "_ansible_become_pass": None,
            "_ansible_no_log": False,
            "task_vars": {
                "ansible_ssh_host": "127.0.0.1",
                "ansible_ssh_port": 22,
                "ansible_ssh_user": "johndoe",
                "ansible_become_pass": None,
                "ansible_no_log": False
            }
        }
    ]

# Generated at 2022-06-13 15:26:14.730590
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    inventory = InventoryManager(loader=None, sources=['localhost,'])
    loader = DataLoader()
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    display = Display()

# Generated at 2022-06-13 15:26:23.971599
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    host1 = Host('test1')
    host2 = Host('test2')
    test_play = Play().load(dict(
        name="Ansible Play",
        hosts=['test1', 'test2'],
        gather_facts='no',
        tasks=[
            dict(action=dict(module='debug', args=dict(msg='{{ my_var }}')),
                 register='debug_result'),
            dict(action=dict(module='shell', args=dict(warn=False, executable='/usr/bin/yes'))),
            dict(action=dict(module='shell', args=dict(warn=False, executable='/usr/bin/yes'))),
            dict(action=dict(module='shell', args=dict(warn=False, executable='/usr/bin/yes')))
        ]
    ))
    test